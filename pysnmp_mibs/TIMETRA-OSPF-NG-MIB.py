# SNMP MIB module (TIMETRA-OSPF-NG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-OSPF-NG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:53:25 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber")

(DesignatedRouterPriority,
 HelloRange,
 Metric,
 Status) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "DesignatedRouterPriority",
    "HelloRange",
    "Metric",
    "Status")

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
 StorageType,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
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

(TLNamedItemOrEmpty,
 TNamedItemOrEmpty,
 TResolveStatus,
 TmnxAddressAndPrefixAddress,
 TmnxAddressAndPrefixPrefix,
 TmnxAddressAndPrefixType,
 TmnxAdminState,
 TmnxEnabledDisabled,
 TmnxHigh32,
 TmnxIgpSCFamilyType,
 TmnxLow32,
 TmnxOperState,
 TmnxOspfInstance,
 TmnxReferenceBandwidth) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TLNamedItemOrEmpty",
    "TNamedItemOrEmpty",
    "TResolveStatus",
    "TmnxAddressAndPrefixAddress",
    "TmnxAddressAndPrefixPrefix",
    "TmnxAddressAndPrefixType",
    "TmnxAdminState",
    "TmnxEnabledDisabled",
    "TmnxHigh32",
    "TmnxIgpSCFamilyType",
    "TmnxLow32",
    "TmnxOperState",
    "TmnxOspfInstance",
    "TmnxReferenceBandwidth")

(TmnxInetCidrNextHopOwner,
 vRtrID) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "TmnxInetCidrNextHopOwner",
    "vRtrID")


# MODULE-IDENTITY

timetraOspfNgMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 36)
)
if mibBuilder.loadTexts:
    timetraOspfNgMIBModule.setRevisions(
        ("2020-02-01 00:00",
         "2019-04-01 00:00",
         "2018-02-01 00:00",
         "2017-01-01 00:00",
         "2015-06-01 00:00",
         "2015-01-01 00:00",
         "2014-01-01 00:00",
         "2011-02-01 00:00",
         "2009-02-28 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00",
         "2007-01-01 00:00",
         "2006-03-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxOspfUpToRefreshIntervalTc(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )



class TmnxOspfDeadIntRangeTc(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )



class TmnxOspfRouterIdTc(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class TmnxOspfAreaIdTc(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class TmnxOspfIfInstIdTc(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxOspfPreference(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class TmnxOspfAuthenticationType(TextualConvention, Integer32):
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
        *(("none", 0),
          ("simplePassword", 1),
          ("md5", 2))
    )



class TmnxOspfIfMD5KeyId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TmnxOspfRestartReasonTc(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 0),
          ("swRestart", 1),
          ("swReload", 2),
          ("switchRed", 3))
    )



class TmnxOspfIfTypeTc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("broadcast", 1),
          ("nbma", 2),
          ("pointToPoint", 3),
          ("pointToMultipoint", 5),
          ("secondary", 6))
    )



class TmnxOspfShamIfMetricTc(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TmnxOspfLsaFilterOutTc(TextualConvention, Integer32):
    status = "current"
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
          ("all", 1),
          ("exceptOwnRtrLsa", 2),
          ("exceptOwnRtrLsaAndDefaults", 3))
    )



class TmnxSegmentRoutingId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class TmnxOspfSegmentRoutingRouteType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("intraArea", 1),
          ("interArea", 3),
          ("external", 5),
          ("nssaExternal", 7))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxOspfConformance_ObjectIdentity = ObjectIdentity
tmnxOspfConformance = _TmnxOspfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36)
)
_TmnxOspfCompliances_ObjectIdentity = ObjectIdentity
tmnxOspfCompliances = _TmnxOspfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 1)
)
_TmnxOspfGroups_ObjectIdentity = ObjectIdentity
tmnxOspfGroups = _TmnxOspfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2)
)
_TmnxOspfObjects_ObjectIdentity = ObjectIdentity
tmnxOspfObjects = _TmnxOspfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36)
)
_TmnxOspfScalars_ObjectIdentity = ObjectIdentity
tmnxOspfScalars = _TmnxOspfScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 1)
)
_TmnxOspfGeneralEntries_Type = Gauge32
_TmnxOspfGeneralEntries_Object = MibScalar
tmnxOspfGeneralEntries = _TmnxOspfGeneralEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 1, 1),
    _TmnxOspfGeneralEntries_Type()
)
tmnxOspfGeneralEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfGeneralEntries.setStatus("current")
_TmnxOspfGeneralTable_Object = MibTable
tmnxOspfGeneralTable = _TmnxOspfGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2)
)
if mibBuilder.loadTexts:
    tmnxOspfGeneralTable.setStatus("current")
_TmnxOspfGeneralEntry_Object = MibTableRow
tmnxOspfGeneralEntry = _TmnxOspfGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1)
)
tmnxOspfGeneralEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
)
if mibBuilder.loadTexts:
    tmnxOspfGeneralEntry.setStatus("current")


class _TmnxOspfVersion_Type(Integer32):
    """Custom type tmnxOspfVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("version2", 2),
          ("version3", 3))
    )


_TmnxOspfVersion_Type.__name__ = "Integer32"
_TmnxOspfVersion_Object = MibTableColumn
tmnxOspfVersion = _TmnxOspfVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 1),
    _TmnxOspfVersion_Type()
)
tmnxOspfVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfVersion.setStatus("current")
_TmnxOspfInstance_Type = TmnxOspfInstance
_TmnxOspfInstance_Object = MibTableColumn
tmnxOspfInstance = _TmnxOspfInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 2),
    _TmnxOspfInstance_Type()
)
tmnxOspfInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfInstance.setStatus("current")
_TmnxOspfGeneralLastChanged_Type = TimeStamp
_TmnxOspfGeneralLastChanged_Object = MibTableColumn
tmnxOspfGeneralLastChanged = _TmnxOspfGeneralLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 4),
    _TmnxOspfGeneralLastChanged_Type()
)
tmnxOspfGeneralLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfGeneralLastChanged.setStatus("current")
_TmnxOspfRouterId_Type = TmnxOspfRouterIdTc
_TmnxOspfRouterId_Object = MibTableColumn
tmnxOspfRouterId = _TmnxOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 5),
    _TmnxOspfRouterId_Type()
)
tmnxOspfRouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfRouterId.setStatus("current")
_TmnxOspfAdminState_Type = Status
_TmnxOspfAdminState_Object = MibTableColumn
tmnxOspfAdminState = _TmnxOspfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 6),
    _TmnxOspfAdminState_Type()
)
tmnxOspfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAdminState.setStatus("current")
_TmnxOspfASBdrRtrStatus_Type = TruthValue
_TmnxOspfASBdrRtrStatus_Object = MibTableColumn
tmnxOspfASBdrRtrStatus = _TmnxOspfASBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 7),
    _TmnxOspfASBdrRtrStatus_Type()
)
tmnxOspfASBdrRtrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfASBdrRtrStatus.setStatus("current")
_TmnxOspfRFC1583Compatibility_Type = TruthValue
_TmnxOspfRFC1583Compatibility_Object = MibTableColumn
tmnxOspfRFC1583Compatibility = _TmnxOspfRFC1583Compatibility_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 8),
    _TmnxOspfRFC1583Compatibility_Type()
)
tmnxOspfRFC1583Compatibility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfRFC1583Compatibility.setStatus("current")


class _TmnxOspfExtLsdbLimit_Type(Integer32):
    """Custom type tmnxOspfExtLsdbLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_TmnxOspfExtLsdbLimit_Type.__name__ = "Integer32"
_TmnxOspfExtLsdbLimit_Object = MibTableColumn
tmnxOspfExtLsdbLimit = _TmnxOspfExtLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 9),
    _TmnxOspfExtLsdbLimit_Type()
)
tmnxOspfExtLsdbLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfExtLsdbLimit.setStatus("current")


class _TmnxOspfMulticastExtensions_Type(Bits):
    """Custom type tmnxOspfMulticastExtensions based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("intraAreaMulticast", 0),
          ("interAreaMulticast", 1),
          ("interAsMulticast", 2))
    )

_TmnxOspfMulticastExtensions_Type.__name__ = "Bits"
_TmnxOspfMulticastExtensions_Object = MibTableColumn
tmnxOspfMulticastExtensions = _TmnxOspfMulticastExtensions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 10),
    _TmnxOspfMulticastExtensions_Type()
)
tmnxOspfMulticastExtensions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfMulticastExtensions.setStatus("current")


class _TmnxOspfExitOverflowInterval_Type(Unsigned32):
    """Custom type tmnxOspfExitOverflowInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxOspfExitOverflowInterval_Type.__name__ = "Unsigned32"
_TmnxOspfExitOverflowInterval_Object = MibTableColumn
tmnxOspfExitOverflowInterval = _TmnxOspfExitOverflowInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 11),
    _TmnxOspfExitOverflowInterval_Type()
)
tmnxOspfExitOverflowInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfExitOverflowInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfExitOverflowInterval.setUnits("seconds")
_TmnxOspfDemandExtensions_Type = TruthValue
_TmnxOspfDemandExtensions_Object = MibTableColumn
tmnxOspfDemandExtensions = _TmnxOspfDemandExtensions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 12),
    _TmnxOspfDemandExtensions_Type()
)
tmnxOspfDemandExtensions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfDemandExtensions.setStatus("current")


class _TmnxOspfReferenceBandwidth_Type(TmnxReferenceBandwidth):
    """Custom type tmnxOspfReferenceBandwidth based on TmnxReferenceBandwidth"""
    defaultValue = 100000000

    subtypeSpec = TmnxReferenceBandwidth.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000000000),
    )


_TmnxOspfReferenceBandwidth_Type.__name__ = "TmnxReferenceBandwidth"
_TmnxOspfReferenceBandwidth_Object = MibTableColumn
tmnxOspfReferenceBandwidth = _TmnxOspfReferenceBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 13),
    _TmnxOspfReferenceBandwidth_Type()
)
tmnxOspfReferenceBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfReferenceBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfReferenceBandwidth.setUnits("1000 bits per second")


class _TmnxOspfStrictLsaChecking_Type(TruthValue):
    """Custom type tmnxOspfStrictLsaChecking based on TruthValue"""
    defaultValue = 1


_TmnxOspfStrictLsaChecking_Type.__name__ = "TruthValue"
_TmnxOspfStrictLsaChecking_Object = MibTableColumn
tmnxOspfStrictLsaChecking = _TmnxOspfStrictLsaChecking_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 14),
    _TmnxOspfStrictLsaChecking_Type()
)
tmnxOspfStrictLsaChecking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfStrictLsaChecking.setStatus("current")


class _TmnxOspfRestartSupport_Type(Integer32):
    """Custom type tmnxOspfRestartSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("plannedOnly", 2),
          ("plannedAndUnplanned", 3))
    )


_TmnxOspfRestartSupport_Type.__name__ = "Integer32"
_TmnxOspfRestartSupport_Object = MibTableColumn
tmnxOspfRestartSupport = _TmnxOspfRestartSupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 15),
    _TmnxOspfRestartSupport_Type()
)
tmnxOspfRestartSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfRestartSupport.setStatus("current")
_TmnxOspfRestartInterval_Type = TmnxOspfUpToRefreshIntervalTc
_TmnxOspfRestartInterval_Object = MibTableColumn
tmnxOspfRestartInterval = _TmnxOspfRestartInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 16),
    _TmnxOspfRestartInterval_Type()
)
tmnxOspfRestartInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfRestartInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfRestartInterval.setUnits("seconds")


class _TmnxOspfPreference_Type(TmnxOspfPreference):
    """Custom type tmnxOspfPreference based on TmnxOspfPreference"""
    defaultValue = 10


_TmnxOspfPreference_Type.__name__ = "TmnxOspfPreference"
_TmnxOspfPreference_Object = MibTableColumn
tmnxOspfPreference = _TmnxOspfPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 17),
    _TmnxOspfPreference_Type()
)
tmnxOspfPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfPreference.setStatus("current")


class _TmnxOspfExternalPreference_Type(TmnxOspfPreference):
    """Custom type tmnxOspfExternalPreference based on TmnxOspfPreference"""
    defaultValue = 150


_TmnxOspfExternalPreference_Type.__name__ = "TmnxOspfPreference"
_TmnxOspfExternalPreference_Object = MibTableColumn
tmnxOspfExternalPreference = _TmnxOspfExternalPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 18),
    _TmnxOspfExternalPreference_Type()
)
tmnxOspfExternalPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfExternalPreference.setStatus("current")


class _TmnxOspfExportPolicy1_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfExportPolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfExportPolicy1_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfExportPolicy1_Object = MibTableColumn
tmnxOspfExportPolicy1 = _TmnxOspfExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 19),
    _TmnxOspfExportPolicy1_Type()
)
tmnxOspfExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfExportPolicy1.setStatus("current")


class _TmnxOspfExportPolicy2_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfExportPolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfExportPolicy2_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfExportPolicy2_Object = MibTableColumn
tmnxOspfExportPolicy2 = _TmnxOspfExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 20),
    _TmnxOspfExportPolicy2_Type()
)
tmnxOspfExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfExportPolicy2.setStatus("current")


class _TmnxOspfExportPolicy3_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfExportPolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfExportPolicy3_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfExportPolicy3_Object = MibTableColumn
tmnxOspfExportPolicy3 = _TmnxOspfExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 21),
    _TmnxOspfExportPolicy3_Type()
)
tmnxOspfExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfExportPolicy3.setStatus("current")


class _TmnxOspfExportPolicy4_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfExportPolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfExportPolicy4_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfExportPolicy4_Object = MibTableColumn
tmnxOspfExportPolicy4 = _TmnxOspfExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 22),
    _TmnxOspfExportPolicy4_Type()
)
tmnxOspfExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfExportPolicy4.setStatus("current")


class _TmnxOspfExportPolicy5_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfExportPolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfExportPolicy5_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfExportPolicy5_Object = MibTableColumn
tmnxOspfExportPolicy5 = _TmnxOspfExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 23),
    _TmnxOspfExportPolicy5_Type()
)
tmnxOspfExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfExportPolicy5.setStatus("current")


class _TmnxOspfManualSpfTrigger_Type(Integer32):
    """Custom type tmnxOspfManualSpfTrigger based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("runTotalSpf", 2),
          ("runExternalsSpf", 3))
    )


_TmnxOspfManualSpfTrigger_Type.__name__ = "Integer32"
_TmnxOspfManualSpfTrigger_Object = MibTableColumn
tmnxOspfManualSpfTrigger = _TmnxOspfManualSpfTrigger_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 24),
    _TmnxOspfManualSpfTrigger_Type()
)
tmnxOspfManualSpfTrigger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfManualSpfTrigger.setStatus("current")


class _TmnxOspfOverloadAdmState_Type(Status):
    """Custom type tmnxOspfOverloadAdmState based on Status"""
    defaultValue = 2


_TmnxOspfOverloadAdmState_Type.__name__ = "Status"
_TmnxOspfOverloadAdmState_Object = MibTableColumn
tmnxOspfOverloadAdmState = _TmnxOspfOverloadAdmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 25),
    _TmnxOspfOverloadAdmState_Type()
)
tmnxOspfOverloadAdmState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfOverloadAdmState.setStatus("current")


class _TmnxOspfOverloadInterval_Type(Unsigned32):
    """Custom type tmnxOspfOverloadInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_TmnxOspfOverloadInterval_Type.__name__ = "Unsigned32"
_TmnxOspfOverloadInterval_Object = MibTableColumn
tmnxOspfOverloadInterval = _TmnxOspfOverloadInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 26),
    _TmnxOspfOverloadInterval_Type()
)
tmnxOspfOverloadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfOverloadInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfOverloadInterval.setUnits("seconds")


class _TmnxOspfBootOverloadAdmState_Type(Integer32):
    """Custom type tmnxOspfBootOverloadAdmState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TmnxOspfBootOverloadAdmState_Type.__name__ = "Integer32"
_TmnxOspfBootOverloadAdmState_Object = MibTableColumn
tmnxOspfBootOverloadAdmState = _TmnxOspfBootOverloadAdmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 27),
    _TmnxOspfBootOverloadAdmState_Type()
)
tmnxOspfBootOverloadAdmState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfBootOverloadAdmState.setStatus("current")


class _TmnxOspfBootOverloadInterval_Type(Unsigned32):
    """Custom type tmnxOspfBootOverloadInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_TmnxOspfBootOverloadInterval_Type.__name__ = "Unsigned32"
_TmnxOspfBootOverloadInterval_Object = MibTableColumn
tmnxOspfBootOverloadInterval = _TmnxOspfBootOverloadInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 28),
    _TmnxOspfBootOverloadInterval_Type()
)
tmnxOspfBootOverloadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfBootOverloadInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfBootOverloadInterval.setUnits("seconds")


class _TmnxOspfOverloadStubs_Type(TruthValue):
    """Custom type tmnxOspfOverloadStubs based on TruthValue"""
    defaultValue = 2


_TmnxOspfOverloadStubs_Type.__name__ = "TruthValue"
_TmnxOspfOverloadStubs_Object = MibTableColumn
tmnxOspfOverloadStubs = _TmnxOspfOverloadStubs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 29),
    _TmnxOspfOverloadStubs_Type()
)
tmnxOspfOverloadStubs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfOverloadStubs.setStatus("current")


class _TmnxOspfSpfMaxWait_Type(Unsigned32):
    """Custom type tmnxOspfSpfMaxWait based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120000),
    )


_TmnxOspfSpfMaxWait_Type.__name__ = "Unsigned32"
_TmnxOspfSpfMaxWait_Object = MibTableColumn
tmnxOspfSpfMaxWait = _TmnxOspfSpfMaxWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 30),
    _TmnxOspfSpfMaxWait_Type()
)
tmnxOspfSpfMaxWait.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfSpfMaxWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfSpfMaxWait.setUnits("milliseconds")


class _TmnxOspfSpfInitialWait_Type(Unsigned32):
    """Custom type tmnxOspfSpfInitialWait based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_TmnxOspfSpfInitialWait_Type.__name__ = "Unsigned32"
_TmnxOspfSpfInitialWait_Object = MibTableColumn
tmnxOspfSpfInitialWait = _TmnxOspfSpfInitialWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 31),
    _TmnxOspfSpfInitialWait_Type()
)
tmnxOspfSpfInitialWait.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfSpfInitialWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfSpfInitialWait.setUnits("milliseconds")


class _TmnxOspfSpfSecondWait_Type(Unsigned32):
    """Custom type tmnxOspfSpfSecondWait based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_TmnxOspfSpfSecondWait_Type.__name__ = "Unsigned32"
_TmnxOspfSpfSecondWait_Object = MibTableColumn
tmnxOspfSpfSecondWait = _TmnxOspfSpfSecondWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 32),
    _TmnxOspfSpfSecondWait_Type()
)
tmnxOspfSpfSecondWait.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfSpfSecondWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfSpfSecondWait.setUnits("milliseconds")


class _TmnxOspfLsaGenMaxWait_Type(Unsigned32):
    """Custom type tmnxOspfLsaGenMaxWait based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600000),
    )


_TmnxOspfLsaGenMaxWait_Type.__name__ = "Unsigned32"
_TmnxOspfLsaGenMaxWait_Object = MibTableColumn
tmnxOspfLsaGenMaxWait = _TmnxOspfLsaGenMaxWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 33),
    _TmnxOspfLsaGenMaxWait_Type()
)
tmnxOspfLsaGenMaxWait.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfLsaGenMaxWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfLsaGenMaxWait.setUnits("milliseconds")


class _TmnxOspfLsaGenInitialWait_Type(Unsigned32):
    """Custom type tmnxOspfLsaGenInitialWait based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600000),
    )


_TmnxOspfLsaGenInitialWait_Type.__name__ = "Unsigned32"
_TmnxOspfLsaGenInitialWait_Object = MibTableColumn
tmnxOspfLsaGenInitialWait = _TmnxOspfLsaGenInitialWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 34),
    _TmnxOspfLsaGenInitialWait_Type()
)
tmnxOspfLsaGenInitialWait.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfLsaGenInitialWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfLsaGenInitialWait.setUnits("milliseconds")


class _TmnxOspfLsaGenSecondWait_Type(Unsigned32):
    """Custom type tmnxOspfLsaGenSecondWait based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600000),
    )


_TmnxOspfLsaGenSecondWait_Type.__name__ = "Unsigned32"
_TmnxOspfLsaGenSecondWait_Object = MibTableColumn
tmnxOspfLsaGenSecondWait = _TmnxOspfLsaGenSecondWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 35),
    _TmnxOspfLsaGenSecondWait_Type()
)
tmnxOspfLsaGenSecondWait.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfLsaGenSecondWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfLsaGenSecondWait.setUnits("milliseconds")


class _TmnxOspfLsaArrivalWait_Type(Unsigned32):
    """Custom type tmnxOspfLsaArrivalWait based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_TmnxOspfLsaArrivalWait_Type.__name__ = "Unsigned32"
_TmnxOspfLsaArrivalWait_Object = MibTableColumn
tmnxOspfLsaArrivalWait = _TmnxOspfLsaArrivalWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 36),
    _TmnxOspfLsaArrivalWait_Type()
)
tmnxOspfLsaArrivalWait.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfLsaArrivalWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfLsaArrivalWait.setUnits("milliseconds")


class _TmnxOspfTESupport_Type(TruthValue):
    """Custom type tmnxOspfTESupport based on TruthValue"""
    defaultValue = 2


_TmnxOspfTESupport_Type.__name__ = "TruthValue"
_TmnxOspfTESupport_Object = MibTableColumn
tmnxOspfTESupport = _TmnxOspfTESupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 37),
    _TmnxOspfTESupport_Type()
)
tmnxOspfTESupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfTESupport.setStatus("current")


class _TmnxOspfUnicastImport_Type(TruthValue):
    """Custom type tmnxOspfUnicastImport based on TruthValue"""
    defaultValue = 1


_TmnxOspfUnicastImport_Type.__name__ = "TruthValue"
_TmnxOspfUnicastImport_Object = MibTableColumn
tmnxOspfUnicastImport = _TmnxOspfUnicastImport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 38),
    _TmnxOspfUnicastImport_Type()
)
tmnxOspfUnicastImport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfUnicastImport.setStatus("current")


class _TmnxOspfMulticastImport_Type(TruthValue):
    """Custom type tmnxOspfMulticastImport based on TruthValue"""
    defaultValue = 2


_TmnxOspfMulticastImport_Type.__name__ = "TruthValue"
_TmnxOspfMulticastImport_Object = MibTableColumn
tmnxOspfMulticastImport = _TmnxOspfMulticastImport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 39),
    _TmnxOspfMulticastImport_Type()
)
tmnxOspfMulticastImport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfMulticastImport.setStatus("current")


class _TmnxOspfGREnable_Type(TruthValue):
    """Custom type tmnxOspfGREnable based on TruthValue"""
    defaultValue = 2


_TmnxOspfGREnable_Type.__name__ = "TruthValue"
_TmnxOspfGREnable_Object = MibTableColumn
tmnxOspfGREnable = _TmnxOspfGREnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 40),
    _TmnxOspfGREnable_Type()
)
tmnxOspfGREnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfGREnable.setStatus("current")


class _TmnxOspfGRHelperMode_Type(TruthValue):
    """Custom type tmnxOspfGRHelperMode based on TruthValue"""
    defaultValue = 2


_TmnxOspfGRHelperMode_Type.__name__ = "TruthValue"
_TmnxOspfGRHelperMode_Object = MibTableColumn
tmnxOspfGRHelperMode = _TmnxOspfGRHelperMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 41),
    _TmnxOspfGRHelperMode_Type()
)
tmnxOspfGRHelperMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfGRHelperMode.setStatus("current")
_TmnxOspfRowStatus_Type = RowStatus
_TmnxOspfRowStatus_Object = MibTableColumn
tmnxOspfRowStatus = _TmnxOspfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 42),
    _TmnxOspfRowStatus_Type()
)
tmnxOspfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfRowStatus.setStatus("current")


class _TmnxOspfAsbrDomainId_Type(Integer32):
    """Custom type tmnxOspfAsbrDomainId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 31),
    )


_TmnxOspfAsbrDomainId_Type.__name__ = "Integer32"
_TmnxOspfAsbrDomainId_Object = MibTableColumn
tmnxOspfAsbrDomainId = _TmnxOspfAsbrDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 43),
    _TmnxOspfAsbrDomainId_Type()
)
tmnxOspfAsbrDomainId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAsbrDomainId.setStatus("current")


class _TmnxOspfIgnoreDNBit_Type(TruthValue):
    """Custom type tmnxOspfIgnoreDNBit based on TruthValue"""
    defaultValue = 2


_TmnxOspfIgnoreDNBit_Type.__name__ = "TruthValue"
_TmnxOspfIgnoreDNBit_Object = MibTableColumn
tmnxOspfIgnoreDNBit = _TmnxOspfIgnoreDNBit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 44),
    _TmnxOspfIgnoreDNBit_Type()
)
tmnxOspfIgnoreDNBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIgnoreDNBit.setStatus("current")


class _TmnxOspfSuppressDNBit_Type(TruthValue):
    """Custom type tmnxOspfSuppressDNBit based on TruthValue"""
    defaultValue = 2


_TmnxOspfSuppressDNBit_Type.__name__ = "TruthValue"
_TmnxOspfSuppressDNBit_Object = MibTableColumn
tmnxOspfSuppressDNBit = _TmnxOspfSuppressDNBit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 45),
    _TmnxOspfSuppressDNBit_Type()
)
tmnxOspfSuppressDNBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfSuppressDNBit.setStatus("current")


class _TmnxOspfLdpSyncAdminState_Type(Status):
    """Custom type tmnxOspfLdpSyncAdminState based on Status"""
    defaultValue = 1


_TmnxOspfLdpSyncAdminState_Type.__name__ = "Status"
_TmnxOspfLdpSyncAdminState_Object = MibTableColumn
tmnxOspfLdpSyncAdminState = _TmnxOspfLdpSyncAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 46),
    _TmnxOspfLdpSyncAdminState_Type()
)
tmnxOspfLdpSyncAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfLdpSyncAdminState.setStatus("current")


class _TmnxOspfVpnDomainType_Type(Integer32):
    """Custom type tmnxOspfVpnDomainType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              261,
              517,
              32773)
        )
    )
    namedValues = NamedValues(
        *(("type0000", 0),
          ("type0005", 5),
          ("type0105", 261),
          ("type0205", 517),
          ("type8005", 32773))
    )


_TmnxOspfVpnDomainType_Type.__name__ = "Integer32"
_TmnxOspfVpnDomainType_Object = MibTableColumn
tmnxOspfVpnDomainType = _TmnxOspfVpnDomainType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 47),
    _TmnxOspfVpnDomainType_Type()
)
tmnxOspfVpnDomainType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfVpnDomainType.setStatus("current")


class _TmnxOspfVpnDomainId_Type(OctetString):
    """Custom type tmnxOspfVpnDomainId based on OctetString"""
    defaultHexValue = "000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_TmnxOspfVpnDomainId_Type.__name__ = "OctetString"
_TmnxOspfVpnDomainId_Object = MibTableColumn
tmnxOspfVpnDomainId = _TmnxOspfVpnDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 48),
    _TmnxOspfVpnDomainId_Type()
)
tmnxOspfVpnDomainId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfVpnDomainId.setStatus("current")


class _TmnxOspfVpnTag_Type(Unsigned32):
    """Custom type tmnxOspfVpnTag based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TmnxOspfVpnTag_Type.__name__ = "Unsigned32"
_TmnxOspfVpnTag_Object = MibTableColumn
tmnxOspfVpnTag = _TmnxOspfVpnTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 49),
    _TmnxOspfVpnTag_Type()
)
tmnxOspfVpnTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfVpnTag.setStatus("current")


class _TmnxOspfSuperBackBone_Type(TruthValue):
    """Custom type tmnxOspfSuperBackBone based on TruthValue"""
    defaultValue = 2


_TmnxOspfSuperBackBone_Type.__name__ = "TruthValue"
_TmnxOspfSuperBackBone_Object = MibTableColumn
tmnxOspfSuperBackBone = _TmnxOspfSuperBackBone_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 50),
    _TmnxOspfSuperBackBone_Type()
)
tmnxOspfSuperBackBone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfSuperBackBone.setStatus("current")


class _TmnxOspfLdpOverRsvp_Type(TmnxEnabledDisabled):
    """Custom type tmnxOspfLdpOverRsvp based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOspfLdpOverRsvp_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOspfLdpOverRsvp_Object = MibTableColumn
tmnxOspfLdpOverRsvp = _TmnxOspfLdpOverRsvp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 51),
    _TmnxOspfLdpOverRsvp_Type()
)
tmnxOspfLdpOverRsvp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfLdpOverRsvp.setStatus("current")


class _TmnxOspfExportLimit_Type(Unsigned32):
    """Custom type tmnxOspfExportLimit based on Unsigned32"""
    defaultValue = 0


_TmnxOspfExportLimit_Type.__name__ = "Unsigned32"
_TmnxOspfExportLimit_Object = MibTableColumn
tmnxOspfExportLimit = _TmnxOspfExportLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 52),
    _TmnxOspfExportLimit_Type()
)
tmnxOspfExportLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfExportLimit.setStatus("current")


class _TmnxOspfExportLimitLogPercent_Type(Unsigned32):
    """Custom type tmnxOspfExportLimitLogPercent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxOspfExportLimitLogPercent_Type.__name__ = "Unsigned32"
_TmnxOspfExportLimitLogPercent_Object = MibTableColumn
tmnxOspfExportLimitLogPercent = _TmnxOspfExportLimitLogPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 53),
    _TmnxOspfExportLimitLogPercent_Type()
)
tmnxOspfExportLimitLogPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfExportLimitLogPercent.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfExportLimitLogPercent.setUnits("percent")


class _TmnxOspfRsvpShortcut_Type(TruthValue):
    """Custom type tmnxOspfRsvpShortcut based on TruthValue"""
    defaultValue = 2


_TmnxOspfRsvpShortcut_Type.__name__ = "TruthValue"
_TmnxOspfRsvpShortcut_Object = MibTableColumn
tmnxOspfRsvpShortcut = _TmnxOspfRsvpShortcut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 54),
    _TmnxOspfRsvpShortcut_Type()
)
tmnxOspfRsvpShortcut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfRsvpShortcut.setStatus("obsolete")


class _TmnxOspfAdvertiseTunnelLink_Type(TruthValue):
    """Custom type tmnxOspfAdvertiseTunnelLink based on TruthValue"""
    defaultValue = 2


_TmnxOspfAdvertiseTunnelLink_Type.__name__ = "TruthValue"
_TmnxOspfAdvertiseTunnelLink_Object = MibTableColumn
tmnxOspfAdvertiseTunnelLink = _TmnxOspfAdvertiseTunnelLink_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 55),
    _TmnxOspfAdvertiseTunnelLink_Type()
)
tmnxOspfAdvertiseTunnelLink.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAdvertiseTunnelLink.setStatus("current")


class _TmnxOspfImportPolicy1_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfImportPolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfImportPolicy1_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfImportPolicy1_Object = MibTableColumn
tmnxOspfImportPolicy1 = _TmnxOspfImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 56),
    _TmnxOspfImportPolicy1_Type()
)
tmnxOspfImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfImportPolicy1.setStatus("current")


class _TmnxOspfImportPolicy2_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfImportPolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfImportPolicy2_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfImportPolicy2_Object = MibTableColumn
tmnxOspfImportPolicy2 = _TmnxOspfImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 57),
    _TmnxOspfImportPolicy2_Type()
)
tmnxOspfImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfImportPolicy2.setStatus("current")


class _TmnxOspfImportPolicy3_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfImportPolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfImportPolicy3_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfImportPolicy3_Object = MibTableColumn
tmnxOspfImportPolicy3 = _TmnxOspfImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 58),
    _TmnxOspfImportPolicy3_Type()
)
tmnxOspfImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfImportPolicy3.setStatus("current")


class _TmnxOspfImportPolicy4_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfImportPolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfImportPolicy4_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfImportPolicy4_Object = MibTableColumn
tmnxOspfImportPolicy4 = _TmnxOspfImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 59),
    _TmnxOspfImportPolicy4_Type()
)
tmnxOspfImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfImportPolicy4.setStatus("current")


class _TmnxOspfImportPolicy5_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfImportPolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfImportPolicy5_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfImportPolicy5_Object = MibTableColumn
tmnxOspfImportPolicy5 = _TmnxOspfImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 60),
    _TmnxOspfImportPolicy5_Type()
)
tmnxOspfImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfImportPolicy5.setStatus("current")


class _TmnxOspfLoopfreeAlternate_Type(TruthValue):
    """Custom type tmnxOspfLoopfreeAlternate based on TruthValue"""
    defaultValue = 2


_TmnxOspfLoopfreeAlternate_Type.__name__ = "TruthValue"
_TmnxOspfLoopfreeAlternate_Object = MibTableColumn
tmnxOspfLoopfreeAlternate = _TmnxOspfLoopfreeAlternate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 61),
    _TmnxOspfLoopfreeAlternate_Type()
)
tmnxOspfLoopfreeAlternate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfLoopfreeAlternate.setStatus("current")


class _TmnxOspfLsaAccumulate_Type(Unsigned32):
    """Custom type tmnxOspfLsaAccumulate based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TmnxOspfLsaAccumulate_Type.__name__ = "Unsigned32"
_TmnxOspfLsaAccumulate_Object = MibTableColumn
tmnxOspfLsaAccumulate = _TmnxOspfLsaAccumulate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 62),
    _TmnxOspfLsaAccumulate_Type()
)
tmnxOspfLsaAccumulate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfLsaAccumulate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfLsaAccumulate.setUnits("milliseconds")


class _TmnxOspfRedistDelay_Type(Unsigned32):
    """Custom type tmnxOspfRedistDelay based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TmnxOspfRedistDelay_Type.__name__ = "Unsigned32"
_TmnxOspfRedistDelay_Object = MibTableColumn
tmnxOspfRedistDelay = _TmnxOspfRedistDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 63),
    _TmnxOspfRedistDelay_Type()
)
tmnxOspfRedistDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfRedistDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfRedistDelay.setUnits("milliseconds")


class _TmnxOspfIncrSpfWait_Type(Unsigned32):
    """Custom type tmnxOspfIncrSpfWait based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TmnxOspfIncrSpfWait_Type.__name__ = "Unsigned32"
_TmnxOspfIncrSpfWait_Object = MibTableColumn
tmnxOspfIncrSpfWait = _TmnxOspfIncrSpfWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 64),
    _TmnxOspfIncrSpfWait_Type()
)
tmnxOspfIncrSpfWait.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIncrSpfWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfIncrSpfWait.setUnits("milliseconds")


class _TmnxOspfOverloadInclExt2_Type(TruthValue):
    """Custom type tmnxOspfOverloadInclExt2 based on TruthValue"""
    defaultValue = 2


_TmnxOspfOverloadInclExt2_Type.__name__ = "TruthValue"
_TmnxOspfOverloadInclExt2_Object = MibTableColumn
tmnxOspfOverloadInclExt2 = _TmnxOspfOverloadInclExt2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 2, 1, 65),
    _TmnxOspfOverloadInclExt2_Type()
)
tmnxOspfOverloadInclExt2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfOverloadInclExt2.setStatus("current")
_TmnxOspfStatusTable_Object = MibTable
tmnxOspfStatusTable = _TmnxOspfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3)
)
if mibBuilder.loadTexts:
    tmnxOspfStatusTable.setStatus("current")
_TmnxOspfStatusEntry_Object = MibTableRow
tmnxOspfStatusEntry = _TmnxOspfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxOspfStatusEntry.setStatus("current")
_TmnxOspfAreaBdrRtrStatus_Type = TruthValue
_TmnxOspfAreaBdrRtrStatus_Object = MibTableColumn
tmnxOspfAreaBdrRtrStatus = _TmnxOspfAreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 1),
    _TmnxOspfAreaBdrRtrStatus_Type()
)
tmnxOspfAreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaBdrRtrStatus.setStatus("current")
_TmnxOspfBackBoneRouter_Type = TruthValue
_TmnxOspfBackBoneRouter_Object = MibTableColumn
tmnxOspfBackBoneRouter = _TmnxOspfBackBoneRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 2),
    _TmnxOspfBackBoneRouter_Type()
)
tmnxOspfBackBoneRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfBackBoneRouter.setStatus("current")
_TmnxOspfStubRouterSupport_Type = TruthValue
_TmnxOspfStubRouterSupport_Object = MibTableColumn
tmnxOspfStubRouterSupport = _TmnxOspfStubRouterSupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 3),
    _TmnxOspfStubRouterSupport_Type()
)
tmnxOspfStubRouterSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfStubRouterSupport.setStatus("current")
_TmnxOspfAsScopeLsaCount_Type = Gauge32
_TmnxOspfAsScopeLsaCount_Object = MibTableColumn
tmnxOspfAsScopeLsaCount = _TmnxOspfAsScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 4),
    _TmnxOspfAsScopeLsaCount_Type()
)
tmnxOspfAsScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAsScopeLsaCount.setStatus("current")
_TmnxOspfAsScopeLsaCksumSum_Type = Integer32
_TmnxOspfAsScopeLsaCksumSum_Object = MibTableColumn
tmnxOspfAsScopeLsaCksumSum = _TmnxOspfAsScopeLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 5),
    _TmnxOspfAsScopeLsaCksumSum_Type()
)
tmnxOspfAsScopeLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAsScopeLsaCksumSum.setStatus("current")
_TmnxOspfAsScopeUnkLsaCount_Type = Gauge32
_TmnxOspfAsScopeUnkLsaCount_Object = MibTableColumn
tmnxOspfAsScopeUnkLsaCount = _TmnxOspfAsScopeUnkLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 6),
    _TmnxOspfAsScopeUnkLsaCount_Type()
)
tmnxOspfAsScopeUnkLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAsScopeUnkLsaCount.setStatus("current")
_TmnxOspfAsScopeUnkLsaCksumSum_Type = Integer32
_TmnxOspfAsScopeUnkLsaCksumSum_Object = MibTableColumn
tmnxOspfAsScopeUnkLsaCksumSum = _TmnxOspfAsScopeUnkLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 7),
    _TmnxOspfAsScopeUnkLsaCksumSum_Type()
)
tmnxOspfAsScopeUnkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAsScopeUnkLsaCksumSum.setStatus("current")
_TmnxOspfExternLsaCount_Type = Gauge32
_TmnxOspfExternLsaCount_Object = MibTableColumn
tmnxOspfExternLsaCount = _TmnxOspfExternLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 8),
    _TmnxOspfExternLsaCount_Type()
)
tmnxOspfExternLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfExternLsaCount.setStatus("current")
_TmnxOspfExternLsaCksumSum_Type = Integer32
_TmnxOspfExternLsaCksumSum_Object = MibTableColumn
tmnxOspfExternLsaCksumSum = _TmnxOspfExternLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 9),
    _TmnxOspfExternLsaCksumSum_Type()
)
tmnxOspfExternLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfExternLsaCksumSum.setStatus("current")
_TmnxOspfOpaqueLsaSupport_Type = TruthValue
_TmnxOspfOpaqueLsaSupport_Object = MibTableColumn
tmnxOspfOpaqueLsaSupport = _TmnxOspfOpaqueLsaSupport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 10),
    _TmnxOspfOpaqueLsaSupport_Type()
)
tmnxOspfOpaqueLsaSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfOpaqueLsaSupport.setStatus("current")


class _TmnxOspfRestartStatus_Type(Integer32):
    """Custom type tmnxOspfRestartStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRestarting", 1),
          ("plannedRestart", 2),
          ("unplannedRestart", 3))
    )


_TmnxOspfRestartStatus_Type.__name__ = "Integer32"
_TmnxOspfRestartStatus_Object = MibTableColumn
tmnxOspfRestartStatus = _TmnxOspfRestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 11),
    _TmnxOspfRestartStatus_Type()
)
tmnxOspfRestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfRestartStatus.setStatus("current")
_TmnxOspfRestartAge_Type = TmnxOspfUpToRefreshIntervalTc
_TmnxOspfRestartAge_Object = MibTableColumn
tmnxOspfRestartAge = _TmnxOspfRestartAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 12),
    _TmnxOspfRestartAge_Type()
)
tmnxOspfRestartAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfRestartAge.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfRestartAge.setUnits("seconds")


class _TmnxOspfRestartExitRc_Type(Integer32):
    """Custom type tmnxOspfRestartExitRc based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_TmnxOspfRestartExitRc_Type.__name__ = "Integer32"
_TmnxOspfRestartExitRc_Object = MibTableColumn
tmnxOspfRestartExitRc = _TmnxOspfRestartExitRc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 13),
    _TmnxOspfRestartExitRc_Type()
)
tmnxOspfRestartExitRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfRestartExitRc.setStatus("current")
_TmnxOspfDiscontinuityTime_Type = TimeStamp
_TmnxOspfDiscontinuityTime_Object = MibTableColumn
tmnxOspfDiscontinuityTime = _TmnxOspfDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 14),
    _TmnxOspfDiscontinuityTime_Type()
)
tmnxOspfDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfDiscontinuityTime.setStatus("obsolete")
_TmnxOspfLastEnabledTime_Type = TimeStamp
_TmnxOspfLastEnabledTime_Object = MibTableColumn
tmnxOspfLastEnabledTime = _TmnxOspfLastEnabledTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 15),
    _TmnxOspfLastEnabledTime_Type()
)
tmnxOspfLastEnabledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLastEnabledTime.setStatus("current")
_TmnxOspfLastOvrflwEnteredTime_Type = TimeStamp
_TmnxOspfLastOvrflwEnteredTime_Object = MibTableColumn
tmnxOspfLastOvrflwEnteredTime = _TmnxOspfLastOvrflwEnteredTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 16),
    _TmnxOspfLastOvrflwEnteredTime_Type()
)
tmnxOspfLastOvrflwEnteredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLastOvrflwEnteredTime.setStatus("current")
_TmnxOspfLastOverflowExitTime_Type = TimeStamp
_TmnxOspfLastOverflowExitTime_Object = MibTableColumn
tmnxOspfLastOverflowExitTime = _TmnxOspfLastOverflowExitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 17),
    _TmnxOspfLastOverflowExitTime_Type()
)
tmnxOspfLastOverflowExitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLastOverflowExitTime.setStatus("current")
_TmnxOspfInOverflowState_Type = TruthValue
_TmnxOspfInOverflowState_Object = MibTableColumn
tmnxOspfInOverflowState = _TmnxOspfInOverflowState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 18),
    _TmnxOspfInOverflowState_Type()
)
tmnxOspfInOverflowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfInOverflowState.setStatus("current")


class _TmnxOspfOverloadOperState_Type(Integer32):
    """Custom type tmnxOspfOverloadOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("overload", 1),
          ("noOverload", 2))
    )


_TmnxOspfOverloadOperState_Type.__name__ = "Integer32"
_TmnxOspfOverloadOperState_Object = MibTableColumn
tmnxOspfOverloadOperState = _TmnxOspfOverloadOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 19),
    _TmnxOspfOverloadOperState_Type()
)
tmnxOspfOverloadOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfOverloadOperState.setStatus("current")


class _TmnxOspfOverloadRemInterval_Type(TimeInterval):
    """Custom type tmnxOspfOverloadRemInterval based on TimeInterval"""
    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxOspfOverloadRemInterval_Type.__name__ = "TimeInterval"
_TmnxOspfOverloadRemInterval_Object = MibTableColumn
tmnxOspfOverloadRemInterval = _TmnxOspfOverloadRemInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 20),
    _TmnxOspfOverloadRemInterval_Type()
)
tmnxOspfOverloadRemInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfOverloadRemInterval.setStatus("current")
_TmnxOspfLastOverloadEntrdTime_Type = TimeStamp
_TmnxOspfLastOverloadEntrdTime_Object = MibTableColumn
tmnxOspfLastOverloadEntrdTime = _TmnxOspfLastOverloadEntrdTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 21),
    _TmnxOspfLastOverloadEntrdTime_Type()
)
tmnxOspfLastOverloadEntrdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLastOverloadEntrdTime.setStatus("current")
_TmnxOspfLastOverloadExitTime_Type = TimeStamp
_TmnxOspfLastOverloadExitTime_Object = MibTableColumn
tmnxOspfLastOverloadExitTime = _TmnxOspfLastOverloadExitTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 22),
    _TmnxOspfLastOverloadExitTime_Type()
)
tmnxOspfLastOverloadExitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLastOverloadExitTime.setStatus("current")


class _TmnxOspfLastOverloadEnterCode_Type(Integer32):
    """Custom type tmnxOspfLastOverloadEnterCode based on Integer32"""
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
        *(("none", 1),
          ("spfFailed", 2),
          ("bootOverload", 3),
          ("manualOverload", 4),
          ("singleSfm", 5),
          ("fibAddFail", 6),
          ("rtmAddFail", 7),
          ("rtrAdvLsaLimit", 8))
    )


_TmnxOspfLastOverloadEnterCode_Type.__name__ = "Integer32"
_TmnxOspfLastOverloadEnterCode_Object = MibTableColumn
tmnxOspfLastOverloadEnterCode = _TmnxOspfLastOverloadEnterCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 23),
    _TmnxOspfLastOverloadEnterCode_Type()
)
tmnxOspfLastOverloadEnterCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLastOverloadEnterCode.setStatus("current")


class _TmnxOspfLastOverloadExitCode_Type(Integer32):
    """Custom type tmnxOspfLastOverloadExitCode based on Integer32"""
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
        *(("none", 1),
          ("bgpSigRecv", 2),
          ("timerExpired", 3),
          ("manualExit", 4),
          ("singleSfm", 5))
    )


_TmnxOspfLastOverloadExitCode_Type.__name__ = "Integer32"
_TmnxOspfLastOverloadExitCode_Object = MibTableColumn
tmnxOspfLastOverloadExitCode = _TmnxOspfLastOverloadExitCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 24),
    _TmnxOspfLastOverloadExitCode_Type()
)
tmnxOspfLastOverloadExitCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLastOverloadExitCode.setStatus("current")
_TmnxOspfLastExtSpfRunTime_Type = TimeStamp
_TmnxOspfLastExtSpfRunTime_Object = MibTableColumn
tmnxOspfLastExtSpfRunTime = _TmnxOspfLastExtSpfRunTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 25),
    _TmnxOspfLastExtSpfRunTime_Type()
)
tmnxOspfLastExtSpfRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLastExtSpfRunTime.setStatus("current")
_TmnxOspfLastFullSpfRunTime_Type = TimeStamp
_TmnxOspfLastFullSpfRunTime_Object = MibTableColumn
tmnxOspfLastFullSpfRunTime = _TmnxOspfLastFullSpfRunTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 26),
    _TmnxOspfLastFullSpfRunTime_Type()
)
tmnxOspfLastFullSpfRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLastFullSpfRunTime.setStatus("current")
_TmnxOspfLastFullSpfInterval_Type = TimeInterval
_TmnxOspfLastFullSpfInterval_Object = MibTableColumn
tmnxOspfLastFullSpfInterval = _TmnxOspfLastFullSpfInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 27),
    _TmnxOspfLastFullSpfInterval_Type()
)
tmnxOspfLastFullSpfInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLastFullSpfInterval.setStatus("current")
_TmnxOspfMaxSpfRunInterval_Type = TimeInterval
_TmnxOspfMaxSpfRunInterval_Object = MibTableColumn
tmnxOspfMaxSpfRunInterval = _TmnxOspfMaxSpfRunInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 28),
    _TmnxOspfMaxSpfRunInterval_Type()
)
tmnxOspfMaxSpfRunInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfMaxSpfRunInterval.setStatus("current")
_TmnxOspfMinSpfRunInterval_Type = TimeInterval
_TmnxOspfMinSpfRunInterval_Object = MibTableColumn
tmnxOspfMinSpfRunInterval = _TmnxOspfMinSpfRunInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 29),
    _TmnxOspfMinSpfRunInterval_Type()
)
tmnxOspfMinSpfRunInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfMinSpfRunInterval.setStatus("current")
_TmnxOspfAvgSpfRunInterval_Type = TimeInterval
_TmnxOspfAvgSpfRunInterval_Object = MibTableColumn
tmnxOspfAvgSpfRunInterval = _TmnxOspfAvgSpfRunInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 30),
    _TmnxOspfAvgSpfRunInterval_Type()
)
tmnxOspfAvgSpfRunInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAvgSpfRunInterval.setStatus("current")
_TmnxOspfExtSpfRunInterval_Type = TimeInterval
_TmnxOspfExtSpfRunInterval_Object = MibTableColumn
tmnxOspfExtSpfRunInterval = _TmnxOspfExtSpfRunInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 31),
    _TmnxOspfExtSpfRunInterval_Type()
)
tmnxOspfExtSpfRunInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfExtSpfRunInterval.setStatus("current")
_TmnxOspfRoutesSubmitted_Type = Gauge32
_TmnxOspfRoutesSubmitted_Object = MibTableColumn
tmnxOspfRoutesSubmitted = _TmnxOspfRoutesSubmitted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 32),
    _TmnxOspfRoutesSubmitted_Type()
)
tmnxOspfRoutesSubmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfRoutesSubmitted.setStatus("current")
_TmnxOspfOperRouterId_Type = TmnxOspfRouterIdTc
_TmnxOspfOperRouterId_Object = MibTableColumn
tmnxOspfOperRouterId = _TmnxOspfOperRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 33),
    _TmnxOspfOperRouterId_Type()
)
tmnxOspfOperRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfOperRouterId.setStatus("current")
_TmnxOspfTotalExportedRoutes_Type = Gauge32
_TmnxOspfTotalExportedRoutes_Object = MibTableColumn
tmnxOspfTotalExportedRoutes = _TmnxOspfTotalExportedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 34),
    _TmnxOspfTotalExportedRoutes_Type()
)
tmnxOspfTotalExportedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfTotalExportedRoutes.setStatus("current")
_TmnxOspfLastLfaSpfRunTime_Type = TimeStamp
_TmnxOspfLastLfaSpfRunTime_Object = MibTableColumn
tmnxOspfLastLfaSpfRunTime = _TmnxOspfLastLfaSpfRunTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 35),
    _TmnxOspfLastLfaSpfRunTime_Type()
)
tmnxOspfLastLfaSpfRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLastLfaSpfRunTime.setStatus("current")
_TmnxOspfLdpOverRsvpStatus_Type = TmnxEnabledDisabled
_TmnxOspfLdpOverRsvpStatus_Object = MibTableColumn
tmnxOspfLdpOverRsvpStatus = _TmnxOspfLdpOverRsvpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 36),
    _TmnxOspfLdpOverRsvpStatus_Type()
)
tmnxOspfLdpOverRsvpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLdpOverRsvpStatus.setStatus("current")
_TmnxOspfRsvpShortcutStatus_Type = TruthValue
_TmnxOspfRsvpShortcutStatus_Object = MibTableColumn
tmnxOspfRsvpShortcutStatus = _TmnxOspfRsvpShortcutStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 37),
    _TmnxOspfRsvpShortcutStatus_Type()
)
tmnxOspfRsvpShortcutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfRsvpShortcutStatus.setStatus("current")
_TmnxOspfAdvertiseTunlLinkStatus_Type = TruthValue
_TmnxOspfAdvertiseTunlLinkStatus_Object = MibTableColumn
tmnxOspfAdvertiseTunlLinkStatus = _TmnxOspfAdvertiseTunlLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 38),
    _TmnxOspfAdvertiseTunlLinkStatus_Type()
)
tmnxOspfAdvertiseTunlLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAdvertiseTunlLinkStatus.setStatus("current")


class _TmnxOspfOvldLsaLimitRemInterval_Type(TimeInterval):
    """Custom type tmnxOspfOvldLsaLimitRemInterval based on TimeInterval"""
    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxOspfOvldLsaLimitRemInterval_Type.__name__ = "TimeInterval"
_TmnxOspfOvldLsaLimitRemInterval_Object = MibTableColumn
tmnxOspfOvldLsaLimitRemInterval = _TmnxOspfOvldLsaLimitRemInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 39),
    _TmnxOspfOvldLsaLimitRemInterval_Type()
)
tmnxOspfOvldLsaLimitRemInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfOvldLsaLimitRemInterval.setStatus("current")
_TmnxOspfDbAsn_Type = InetAutonomousSystemNumber
_TmnxOspfDbAsn_Object = MibTableColumn
tmnxOspfDbAsn = _TmnxOspfDbAsn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 40),
    _TmnxOspfDbAsn_Type()
)
tmnxOspfDbAsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfDbAsn.setStatus("current")
_TmnxOspfOperState_Type = TmnxEnabledDisabled
_TmnxOspfOperState_Object = MibTableColumn
tmnxOspfOperState = _TmnxOspfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 3, 1, 41),
    _TmnxOspfOperState_Type()
)
tmnxOspfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfOperState.setStatus("current")
_TmnxOspfStatisticsTable_Object = MibTable
tmnxOspfStatisticsTable = _TmnxOspfStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4)
)
if mibBuilder.loadTexts:
    tmnxOspfStatisticsTable.setStatus("current")
_TmnxOspfStatisticsEntry_Object = MibTableRow
tmnxOspfStatisticsEntry = _TmnxOspfStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxOspfStatisticsEntry.setStatus("current")
_TmnxOspfOriginateNewLsas_Type = Counter32
_TmnxOspfOriginateNewLsas_Object = MibTableColumn
tmnxOspfOriginateNewLsas = _TmnxOspfOriginateNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 2),
    _TmnxOspfOriginateNewLsas_Type()
)
tmnxOspfOriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfOriginateNewLsas.setStatus("current")
_TmnxOspfRxNewLsas_Type = Counter32
_TmnxOspfRxNewLsas_Object = MibTableColumn
tmnxOspfRxNewLsas = _TmnxOspfRxNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 3),
    _TmnxOspfRxNewLsas_Type()
)
tmnxOspfRxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfRxNewLsas.setStatus("current")
_TmnxOspfFullSpfRuns_Type = Counter32
_TmnxOspfFullSpfRuns_Object = MibTableColumn
tmnxOspfFullSpfRuns = _TmnxOspfFullSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 5),
    _TmnxOspfFullSpfRuns_Type()
)
tmnxOspfFullSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfFullSpfRuns.setStatus("current")
_TmnxOspfExtSpfRuns_Type = Counter32
_TmnxOspfExtSpfRuns_Object = MibTableColumn
tmnxOspfExtSpfRuns = _TmnxOspfExtSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 6),
    _TmnxOspfExtSpfRuns_Type()
)
tmnxOspfExtSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfExtSpfRuns.setStatus("current")
_TmnxOspfIncremntlInterSpfRuns_Type = Counter32
_TmnxOspfIncremntlInterSpfRuns_Object = MibTableColumn
tmnxOspfIncremntlInterSpfRuns = _TmnxOspfIncremntlInterSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 7),
    _TmnxOspfIncremntlInterSpfRuns_Type()
)
tmnxOspfIncremntlInterSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIncremntlInterSpfRuns.setStatus("current")
_TmnxOspfIncrementalExtSpfRuns_Type = Counter32
_TmnxOspfIncrementalExtSpfRuns_Object = MibTableColumn
tmnxOspfIncrementalExtSpfRuns = _TmnxOspfIncrementalExtSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 8),
    _TmnxOspfIncrementalExtSpfRuns_Type()
)
tmnxOspfIncrementalExtSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIncrementalExtSpfRuns.setStatus("current")
_TmnxOspfSpfAttemptsFailed_Type = Counter32
_TmnxOspfSpfAttemptsFailed_Object = MibTableColumn
tmnxOspfSpfAttemptsFailed = _TmnxOspfSpfAttemptsFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 9),
    _TmnxOspfSpfAttemptsFailed_Type()
)
tmnxOspfSpfAttemptsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSpfAttemptsFailed.setStatus("current")
_TmnxOspfNumTimesInOverload_Type = Counter32
_TmnxOspfNumTimesInOverload_Object = MibTableColumn
tmnxOspfNumTimesInOverload = _TmnxOspfNumTimesInOverload_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 10),
    _TmnxOspfNumTimesInOverload_Type()
)
tmnxOspfNumTimesInOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNumTimesInOverload.setStatus("current")
_TmnxOspfNumTimesInOverflow_Type = Counter32
_TmnxOspfNumTimesInOverflow_Object = MibTableColumn
tmnxOspfNumTimesInOverflow = _TmnxOspfNumTimesInOverflow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 11),
    _TmnxOspfNumTimesInOverflow_Type()
)
tmnxOspfNumTimesInOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNumTimesInOverflow.setStatus("current")
_TmnxOspfRoutesAddsFailed_Type = Counter32
_TmnxOspfRoutesAddsFailed_Object = MibTableColumn
tmnxOspfRoutesAddsFailed = _TmnxOspfRoutesAddsFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 12),
    _TmnxOspfRoutesAddsFailed_Type()
)
tmnxOspfRoutesAddsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfRoutesAddsFailed.setStatus("current")
_TmnxOspfRoutesDelsFailed_Type = Counter32
_TmnxOspfRoutesDelsFailed_Object = MibTableColumn
tmnxOspfRoutesDelsFailed = _TmnxOspfRoutesDelsFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 13),
    _TmnxOspfRoutesDelsFailed_Type()
)
tmnxOspfRoutesDelsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfRoutesDelsFailed.setStatus("current")
_TmnxOspfRoutesModsFailed_Type = Counter32
_TmnxOspfRoutesModsFailed_Object = MibTableColumn
tmnxOspfRoutesModsFailed = _TmnxOspfRoutesModsFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 14),
    _TmnxOspfRoutesModsFailed_Type()
)
tmnxOspfRoutesModsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfRoutesModsFailed.setStatus("current")
_TmnxOspfAreaEntries_Type = Gauge32
_TmnxOspfAreaEntries_Object = MibTableColumn
tmnxOspfAreaEntries = _TmnxOspfAreaEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 15),
    _TmnxOspfAreaEntries_Type()
)
tmnxOspfAreaEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaEntries.setStatus("current")
_TmnxOspfAreaLsaCountEntries_Type = Gauge32
_TmnxOspfAreaLsaCountEntries_Object = MibTableColumn
tmnxOspfAreaLsaCountEntries = _TmnxOspfAreaLsaCountEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 16),
    _TmnxOspfAreaLsaCountEntries_Type()
)
tmnxOspfAreaLsaCountEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaLsaCountEntries.setStatus("current")
_TmnxOspfAsLsdbEntries_Type = Gauge32
_TmnxOspfAsLsdbEntries_Object = MibTableColumn
tmnxOspfAsLsdbEntries = _TmnxOspfAsLsdbEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 17),
    _TmnxOspfAsLsdbEntries_Type()
)
tmnxOspfAsLsdbEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAsLsdbEntries.setStatus("current")
_TmnxOspfAreaLsdbEntries_Type = Gauge32
_TmnxOspfAreaLsdbEntries_Object = MibTableColumn
tmnxOspfAreaLsdbEntries = _TmnxOspfAreaLsdbEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 18),
    _TmnxOspfAreaLsdbEntries_Type()
)
tmnxOspfAreaLsdbEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaLsdbEntries.setStatus("current")
_TmnxOspfLinkLsdbEntries_Type = Gauge32
_TmnxOspfLinkLsdbEntries_Object = MibTableColumn
tmnxOspfLinkLsdbEntries = _TmnxOspfLinkLsdbEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 19),
    _TmnxOspfLinkLsdbEntries_Type()
)
tmnxOspfLinkLsdbEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLinkLsdbEntries.setStatus("current")
_TmnxOspfHostEntries_Type = Gauge32
_TmnxOspfHostEntries_Object = MibTableColumn
tmnxOspfHostEntries = _TmnxOspfHostEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 20),
    _TmnxOspfHostEntries_Type()
)
tmnxOspfHostEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfHostEntries.setStatus("current")
_TmnxOspfIfEntries_Type = Gauge32
_TmnxOspfIfEntries_Object = MibTableColumn
tmnxOspfIfEntries = _TmnxOspfIfEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 21),
    _TmnxOspfIfEntries_Type()
)
tmnxOspfIfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfEntries.setStatus("current")
_TmnxOspfVirtIfEntries_Type = Gauge32
_TmnxOspfVirtIfEntries_Object = MibTableColumn
tmnxOspfVirtIfEntries = _TmnxOspfVirtIfEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 22),
    _TmnxOspfVirtIfEntries_Type()
)
tmnxOspfVirtIfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfEntries.setStatus("current")
_TmnxOspfNbrEntries_Type = Gauge32
_TmnxOspfNbrEntries_Object = MibTableColumn
tmnxOspfNbrEntries = _TmnxOspfNbrEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 23),
    _TmnxOspfNbrEntries_Type()
)
tmnxOspfNbrEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrEntries.setStatus("current")
_TmnxOspfCfgNbrEntries_Type = Gauge32
_TmnxOspfCfgNbrEntries_Object = MibTableColumn
tmnxOspfCfgNbrEntries = _TmnxOspfCfgNbrEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 24),
    _TmnxOspfCfgNbrEntries_Type()
)
tmnxOspfCfgNbrEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfCfgNbrEntries.setStatus("current")
_TmnxOspfVirtNbrEntries_Type = Gauge32
_TmnxOspfVirtNbrEntries_Object = MibTableColumn
tmnxOspfVirtNbrEntries = _TmnxOspfVirtNbrEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 25),
    _TmnxOspfVirtNbrEntries_Type()
)
tmnxOspfVirtNbrEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrEntries.setStatus("current")
_TmnxOspfAreaAggrEntries_Type = Gauge32
_TmnxOspfAreaAggrEntries_Object = MibTableColumn
tmnxOspfAreaAggrEntries = _TmnxOspfAreaAggrEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 26),
    _TmnxOspfAreaAggrEntries_Type()
)
tmnxOspfAreaAggrEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaAggrEntries.setStatus("current")
_TmnxOspfIfMD5KeyEntries_Type = Gauge32
_TmnxOspfIfMD5KeyEntries_Object = MibTableColumn
tmnxOspfIfMD5KeyEntries = _TmnxOspfIfMD5KeyEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 27),
    _TmnxOspfIfMD5KeyEntries_Type()
)
tmnxOspfIfMD5KeyEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfMD5KeyEntries.setStatus("current")
_TmnxOspfVirtIfMD5KeyEntries_Type = Gauge32
_TmnxOspfVirtIfMD5KeyEntries_Object = MibTableColumn
tmnxOspfVirtIfMD5KeyEntries = _TmnxOspfVirtIfMD5KeyEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 28),
    _TmnxOspfVirtIfMD5KeyEntries_Type()
)
tmnxOspfVirtIfMD5KeyEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfMD5KeyEntries.setStatus("current")
_TmnxOspfCSPFRequests_Type = Counter32
_TmnxOspfCSPFRequests_Object = MibTableColumn
tmnxOspfCSPFRequests = _TmnxOspfCSPFRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 29),
    _TmnxOspfCSPFRequests_Type()
)
tmnxOspfCSPFRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfCSPFRequests.setStatus("current")
_TmnxOspfCSPFDroppedRequests_Type = Counter32
_TmnxOspfCSPFDroppedRequests_Object = MibTableColumn
tmnxOspfCSPFDroppedRequests = _TmnxOspfCSPFDroppedRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 30),
    _TmnxOspfCSPFDroppedRequests_Type()
)
tmnxOspfCSPFDroppedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfCSPFDroppedRequests.setStatus("current")
_TmnxOspfCSPFPathsFound_Type = Counter32
_TmnxOspfCSPFPathsFound_Object = MibTableColumn
tmnxOspfCSPFPathsFound = _TmnxOspfCSPFPathsFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 31),
    _TmnxOspfCSPFPathsFound_Type()
)
tmnxOspfCSPFPathsFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfCSPFPathsFound.setStatus("current")
_TmnxOspfCSPFPathsNotFound_Type = Counter32
_TmnxOspfCSPFPathsNotFound_Object = MibTableColumn
tmnxOspfCSPFPathsNotFound = _TmnxOspfCSPFPathsNotFound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 32),
    _TmnxOspfCSPFPathsNotFound_Type()
)
tmnxOspfCSPFPathsNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfCSPFPathsNotFound.setStatus("current")
_TmnxOspfShamIfEntries_Type = Gauge32
_TmnxOspfShamIfEntries_Object = MibTableColumn
tmnxOspfShamIfEntries = _TmnxOspfShamIfEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 33),
    _TmnxOspfShamIfEntries_Type()
)
tmnxOspfShamIfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfEntries.setStatus("current")
_TmnxOspfShamNbrEntries_Type = Gauge32
_TmnxOspfShamNbrEntries_Object = MibTableColumn
tmnxOspfShamNbrEntries = _TmnxOspfShamNbrEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 34),
    _TmnxOspfShamNbrEntries_Type()
)
tmnxOspfShamNbrEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrEntries.setStatus("current")
_TmnxOspfShamIfMD5KeyEntries_Type = Gauge32
_TmnxOspfShamIfMD5KeyEntries_Object = MibTableColumn
tmnxOspfShamIfMD5KeyEntries = _TmnxOspfShamIfMD5KeyEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 35),
    _TmnxOspfShamIfMD5KeyEntries_Type()
)
tmnxOspfShamIfMD5KeyEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfMD5KeyEntries.setStatus("current")
_TmnxOspfLfaSpfRuns_Type = Counter32
_TmnxOspfLfaSpfRuns_Object = MibTableColumn
tmnxOspfLfaSpfRuns = _TmnxOspfLfaSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 36),
    _TmnxOspfLfaSpfRuns_Type()
)
tmnxOspfLfaSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLfaSpfRuns.setStatus("current")
_TmnxOspfStatsRlfaRuns_Type = Counter32
_TmnxOspfStatsRlfaRuns_Object = MibTableColumn
tmnxOspfStatsRlfaRuns = _TmnxOspfStatsRlfaRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 37),
    _TmnxOspfStatsRlfaRuns_Type()
)
tmnxOspfStatsRlfaRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfStatsRlfaRuns.setStatus("current")
_TmnxOspfStatsSidLabelRangeErrs_Type = Counter32
_TmnxOspfStatsSidLabelRangeErrs_Object = MibTableColumn
tmnxOspfStatsSidLabelRangeErrs = _TmnxOspfStatsSidLabelRangeErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 38),
    _TmnxOspfStatsSidLabelRangeErrs_Type()
)
tmnxOspfStatsSidLabelRangeErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfStatsSidLabelRangeErrs.setStatus("current")
_TmnxOspfStatsSidDupErrs_Type = Counter32
_TmnxOspfStatsSidDupErrs_Object = MibTableColumn
tmnxOspfStatsSidDupErrs = _TmnxOspfStatsSidDupErrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 39),
    _TmnxOspfStatsSidDupErrs_Type()
)
tmnxOspfStatsSidDupErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfStatsSidDupErrs.setStatus("current")
_TmnxOspfStatsTiLfaRuns_Type = Counter32
_TmnxOspfStatsTiLfaRuns_Object = MibTableColumn
tmnxOspfStatsTiLfaRuns = _TmnxOspfStatsTiLfaRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 4, 1, 40),
    _TmnxOspfStatsTiLfaRuns_Type()
)
tmnxOspfStatsTiLfaRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfStatsTiLfaRuns.setStatus("current")
_TmnxOspfChangedTable_Object = MibTable
tmnxOspfChangedTable = _TmnxOspfChangedTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 5)
)
if mibBuilder.loadTexts:
    tmnxOspfChangedTable.setStatus("current")
_TmnxOspfChangedEntry_Object = MibTableRow
tmnxOspfChangedEntry = _TmnxOspfChangedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxOspfChangedEntry.setStatus("current")
_TmnxOspfAreaTableChanged_Type = TimeStamp
_TmnxOspfAreaTableChanged_Object = MibTableColumn
tmnxOspfAreaTableChanged = _TmnxOspfAreaTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 5, 1, 1),
    _TmnxOspfAreaTableChanged_Type()
)
tmnxOspfAreaTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaTableChanged.setStatus("current")
_TmnxOspfHostTableChanged_Type = TimeStamp
_TmnxOspfHostTableChanged_Object = MibTableColumn
tmnxOspfHostTableChanged = _TmnxOspfHostTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 5, 1, 2),
    _TmnxOspfHostTableChanged_Type()
)
tmnxOspfHostTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfHostTableChanged.setStatus("current")
_TmnxOspfIfTableChanged_Type = TimeStamp
_TmnxOspfIfTableChanged_Object = MibTableColumn
tmnxOspfIfTableChanged = _TmnxOspfIfTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 5, 1, 3),
    _TmnxOspfIfTableChanged_Type()
)
tmnxOspfIfTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfTableChanged.setStatus("current")
_TmnxOspfVirtIfTableChanged_Type = TimeStamp
_TmnxOspfVirtIfTableChanged_Object = MibTableColumn
tmnxOspfVirtIfTableChanged = _TmnxOspfVirtIfTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 5, 1, 4),
    _TmnxOspfVirtIfTableChanged_Type()
)
tmnxOspfVirtIfTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfTableChanged.setStatus("current")
_TmnxOspfNbrTableChanged_Type = TimeStamp
_TmnxOspfNbrTableChanged_Object = MibTableColumn
tmnxOspfNbrTableChanged = _TmnxOspfNbrTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 5, 1, 5),
    _TmnxOspfNbrTableChanged_Type()
)
tmnxOspfNbrTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrTableChanged.setStatus("current")
_TmnxOspfCfgNbrTableChanged_Type = TimeStamp
_TmnxOspfCfgNbrTableChanged_Object = MibTableColumn
tmnxOspfCfgNbrTableChanged = _TmnxOspfCfgNbrTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 5, 1, 6),
    _TmnxOspfCfgNbrTableChanged_Type()
)
tmnxOspfCfgNbrTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfCfgNbrTableChanged.setStatus("current")
_TmnxOspfVirtNbrTableChanged_Type = TimeStamp
_TmnxOspfVirtNbrTableChanged_Object = MibTableColumn
tmnxOspfVirtNbrTableChanged = _TmnxOspfVirtNbrTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 5, 1, 7),
    _TmnxOspfVirtNbrTableChanged_Type()
)
tmnxOspfVirtNbrTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrTableChanged.setStatus("current")
_TmnxOspfAreaAggTableChanged_Type = TimeStamp
_TmnxOspfAreaAggTableChanged_Object = MibTableColumn
tmnxOspfAreaAggTableChanged = _TmnxOspfAreaAggTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 5, 1, 8),
    _TmnxOspfAreaAggTableChanged_Type()
)
tmnxOspfAreaAggTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaAggTableChanged.setStatus("current")
_TmnxOspfIfMD5KeyTableChanged_Type = TimeStamp
_TmnxOspfIfMD5KeyTableChanged_Object = MibTableColumn
tmnxOspfIfMD5KeyTableChanged = _TmnxOspfIfMD5KeyTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 5, 1, 9),
    _TmnxOspfIfMD5KeyTableChanged_Type()
)
tmnxOspfIfMD5KeyTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfMD5KeyTableChanged.setStatus("current")
_TmnxOspfVirtIfMD5KeyTableChanged_Type = TimeStamp
_TmnxOspfVirtIfMD5KeyTableChanged_Object = MibTableColumn
tmnxOspfVirtIfMD5KeyTableChanged = _TmnxOspfVirtIfMD5KeyTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 5, 1, 10),
    _TmnxOspfVirtIfMD5KeyTableChanged_Type()
)
tmnxOspfVirtIfMD5KeyTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfMD5KeyTableChanged.setStatus("current")
_TmnxOspfShamIfTableChanged_Type = TimeStamp
_TmnxOspfShamIfTableChanged_Object = MibTableColumn
tmnxOspfShamIfTableChanged = _TmnxOspfShamIfTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 5, 1, 11),
    _TmnxOspfShamIfTableChanged_Type()
)
tmnxOspfShamIfTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfTableChanged.setStatus("current")
_TmnxOspfShamNbrTableChanged_Type = TimeStamp
_TmnxOspfShamNbrTableChanged_Object = MibTableColumn
tmnxOspfShamNbrTableChanged = _TmnxOspfShamNbrTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 5, 1, 12),
    _TmnxOspfShamNbrTableChanged_Type()
)
tmnxOspfShamNbrTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrTableChanged.setStatus("current")
_TmnxOspfShamIfMD5KeyTableChanged_Type = TimeStamp
_TmnxOspfShamIfMD5KeyTableChanged_Object = MibTableColumn
tmnxOspfShamIfMD5KeyTableChanged = _TmnxOspfShamIfMD5KeyTableChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 5, 1, 13),
    _TmnxOspfShamIfMD5KeyTableChanged_Type()
)
tmnxOspfShamIfMD5KeyTableChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfMD5KeyTableChanged.setStatus("current")
_TmnxOspfAreaTable_Object = MibTable
tmnxOspfAreaTable = _TmnxOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6)
)
if mibBuilder.loadTexts:
    tmnxOspfAreaTable.setStatus("current")
_TmnxOspfAreaEntry_Object = MibTableRow
tmnxOspfAreaEntry = _TmnxOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1)
)
tmnxOspfAreaEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaId"),
)
if mibBuilder.loadTexts:
    tmnxOspfAreaEntry.setStatus("current")
_TmnxOspfAreaId_Type = TmnxOspfAreaIdTc
_TmnxOspfAreaId_Object = MibTableColumn
tmnxOspfAreaId = _TmnxOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 1),
    _TmnxOspfAreaId_Type()
)
tmnxOspfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfAreaId.setStatus("current")
_TmnxOspfAreaStatus_Type = RowStatus
_TmnxOspfAreaStatus_Object = MibTableColumn
tmnxOspfAreaStatus = _TmnxOspfAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 2),
    _TmnxOspfAreaStatus_Type()
)
tmnxOspfAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaStatus.setStatus("current")
_TmnxOspfAreaLastChanged_Type = TimeStamp
_TmnxOspfAreaLastChanged_Object = MibTableColumn
tmnxOspfAreaLastChanged = _TmnxOspfAreaLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 3),
    _TmnxOspfAreaLastChanged_Type()
)
tmnxOspfAreaLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaLastChanged.setStatus("current")


class _TmnxOspfImportAsExtern_Type(Integer32):
    """Custom type tmnxOspfImportAsExtern based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("importExternal", 1),
          ("importNoExternal", 2),
          ("importNssa", 3))
    )


_TmnxOspfImportAsExtern_Type.__name__ = "Integer32"
_TmnxOspfImportAsExtern_Object = MibTableColumn
tmnxOspfImportAsExtern = _TmnxOspfImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 4),
    _TmnxOspfImportAsExtern_Type()
)
tmnxOspfImportAsExtern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfImportAsExtern.setStatus("current")


class _TmnxOspfAreaSummary_Type(Integer32):
    """Custom type tmnxOspfAreaSummary based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAreaSummary", 1),
          ("sendAreaSummary", 2))
    )


_TmnxOspfAreaSummary_Type.__name__ = "Integer32"
_TmnxOspfAreaSummary_Object = MibTableColumn
tmnxOspfAreaSummary = _TmnxOspfAreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 5),
    _TmnxOspfAreaSummary_Type()
)
tmnxOspfAreaSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaSummary.setStatus("current")


class _TmnxOspfAreaRangeBlackhole_Type(TruthValue):
    """Custom type tmnxOspfAreaRangeBlackhole based on TruthValue"""
    defaultValue = 1


_TmnxOspfAreaRangeBlackhole_Type.__name__ = "TruthValue"
_TmnxOspfAreaRangeBlackhole_Object = MibTableColumn
tmnxOspfAreaRangeBlackhole = _TmnxOspfAreaRangeBlackhole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 6),
    _TmnxOspfAreaRangeBlackhole_Type()
)
tmnxOspfAreaRangeBlackhole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaRangeBlackhole.setStatus("current")


class _TmnxOspfStubMetric_Type(Integer32):
    """Custom type tmnxOspfStubMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_TmnxOspfStubMetric_Type.__name__ = "Integer32"
_TmnxOspfStubMetric_Object = MibTableColumn
tmnxOspfStubMetric = _TmnxOspfStubMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 7),
    _TmnxOspfStubMetric_Type()
)
tmnxOspfStubMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfStubMetric.setStatus("current")


class _TmnxOspfAreaStubMetricType_Type(Integer32):
    """Custom type tmnxOspfAreaStubMetricType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ospfMetric", 1),
          ("comparableCost", 2),
          ("nonComparable", 3))
    )


_TmnxOspfAreaStubMetricType_Type.__name__ = "Integer32"
_TmnxOspfAreaStubMetricType_Object = MibTableColumn
tmnxOspfAreaStubMetricType = _TmnxOspfAreaStubMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 8),
    _TmnxOspfAreaStubMetricType_Type()
)
tmnxOspfAreaStubMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaStubMetricType.setStatus("current")


class _TmnxOspfAreaOriginateDefault_Type(Integer32):
    """Custom type tmnxOspfAreaOriginateDefault based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOriginate", 1),
          ("originateType3", 2),
          ("originateType7", 3))
    )


_TmnxOspfAreaOriginateDefault_Type.__name__ = "Integer32"
_TmnxOspfAreaOriginateDefault_Object = MibTableColumn
tmnxOspfAreaOriginateDefault = _TmnxOspfAreaOriginateDefault_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 9),
    _TmnxOspfAreaOriginateDefault_Type()
)
tmnxOspfAreaOriginateDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaOriginateDefault.setStatus("current")


class _TmnxOspfAreaNssaRedistribute_Type(TruthValue):
    """Custom type tmnxOspfAreaNssaRedistribute based on TruthValue"""
    defaultValue = 1


_TmnxOspfAreaNssaRedistribute_Type.__name__ = "TruthValue"
_TmnxOspfAreaNssaRedistribute_Object = MibTableColumn
tmnxOspfAreaNssaRedistribute = _TmnxOspfAreaNssaRedistribute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 10),
    _TmnxOspfAreaNssaRedistribute_Type()
)
tmnxOspfAreaNssaRedistribute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaNssaRedistribute.setStatus("current")


class _TmnxOspfAreaNssaTranslatorRole_Type(Integer32):
    """Custom type tmnxOspfAreaNssaTranslatorRole based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("candidate", 2))
    )


_TmnxOspfAreaNssaTranslatorRole_Type.__name__ = "Integer32"
_TmnxOspfAreaNssaTranslatorRole_Object = MibTableColumn
tmnxOspfAreaNssaTranslatorRole = _TmnxOspfAreaNssaTranslatorRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 11),
    _TmnxOspfAreaNssaTranslatorRole_Type()
)
tmnxOspfAreaNssaTranslatorRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaNssaTranslatorRole.setStatus("current")


class _TmnxOspfAreaNssaTranslatorStabInt_Type(Unsigned32):
    """Custom type tmnxOspfAreaNssaTranslatorStabInt based on Unsigned32"""
    defaultValue = 40


_TmnxOspfAreaNssaTranslatorStabInt_Type.__name__ = "Unsigned32"
_TmnxOspfAreaNssaTranslatorStabInt_Object = MibTableColumn
tmnxOspfAreaNssaTranslatorStabInt = _TmnxOspfAreaNssaTranslatorStabInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 12),
    _TmnxOspfAreaNssaTranslatorStabInt_Type()
)
tmnxOspfAreaNssaTranslatorStabInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaNssaTranslatorStabInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfAreaNssaTranslatorStabInt.setUnits("seconds")
_TmnxOspfAreaBdrRtrCount_Type = Gauge32
_TmnxOspfAreaBdrRtrCount_Object = MibTableColumn
tmnxOspfAreaBdrRtrCount = _TmnxOspfAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 13),
    _TmnxOspfAreaBdrRtrCount_Type()
)
tmnxOspfAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaBdrRtrCount.setStatus("current")
_TmnxOspfAreaAsBdrRtrCount_Type = Gauge32
_TmnxOspfAreaAsBdrRtrCount_Object = MibTableColumn
tmnxOspfAreaAsBdrRtrCount = _TmnxOspfAreaAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 14),
    _TmnxOspfAreaAsBdrRtrCount_Type()
)
tmnxOspfAreaAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaAsBdrRtrCount.setStatus("current")
_TmnxOspfAreaScopeLsaCount_Type = Gauge32
_TmnxOspfAreaScopeLsaCount_Object = MibTableColumn
tmnxOspfAreaScopeLsaCount = _TmnxOspfAreaScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 15),
    _TmnxOspfAreaScopeLsaCount_Type()
)
tmnxOspfAreaScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaScopeLsaCount.setStatus("current")
_TmnxOspfAreaScopeLsaCksumSum_Type = Integer32
_TmnxOspfAreaScopeLsaCksumSum_Object = MibTableColumn
tmnxOspfAreaScopeLsaCksumSum = _TmnxOspfAreaScopeLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 16),
    _TmnxOspfAreaScopeLsaCksumSum_Type()
)
tmnxOspfAreaScopeLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaScopeLsaCksumSum.setStatus("current")
_TmnxOspfAreaScopeUnkLsaCount_Type = Gauge32
_TmnxOspfAreaScopeUnkLsaCount_Object = MibTableColumn
tmnxOspfAreaScopeUnkLsaCount = _TmnxOspfAreaScopeUnkLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 17),
    _TmnxOspfAreaScopeUnkLsaCount_Type()
)
tmnxOspfAreaScopeUnkLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaScopeUnkLsaCount.setStatus("current")
_TmnxOspfAreaScopeUnkLsaCksumSum_Type = Integer32
_TmnxOspfAreaScopeUnkLsaCksumSum_Object = MibTableColumn
tmnxOspfAreaScopeUnkLsaCksumSum = _TmnxOspfAreaScopeUnkLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 18),
    _TmnxOspfAreaScopeUnkLsaCksumSum_Type()
)
tmnxOspfAreaScopeUnkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaScopeUnkLsaCksumSum.setStatus("current")


class _TmnxOspfAreaNssaTranslatorState_Type(Integer32):
    """Custom type tmnxOspfAreaNssaTranslatorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("elected", 2),
          ("disabled", 3))
    )


_TmnxOspfAreaNssaTranslatorState_Type.__name__ = "Integer32"
_TmnxOspfAreaNssaTranslatorState_Object = MibTableColumn
tmnxOspfAreaNssaTranslatorState = _TmnxOspfAreaNssaTranslatorState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 19),
    _TmnxOspfAreaNssaTranslatorState_Type()
)
tmnxOspfAreaNssaTranslatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaNssaTranslatorState.setStatus("current")
_TmnxOspfAreaActiveInterfaces_Type = Unsigned32
_TmnxOspfAreaActiveInterfaces_Object = MibTableColumn
tmnxOspfAreaActiveInterfaces = _TmnxOspfAreaActiveInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 20),
    _TmnxOspfAreaActiveInterfaces_Type()
)
tmnxOspfAreaActiveInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaActiveInterfaces.setStatus("current")
_TmnxOspfAreaInterfaceCount_Type = Unsigned32
_TmnxOspfAreaInterfaceCount_Object = MibTableColumn
tmnxOspfAreaInterfaceCount = _TmnxOspfAreaInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 21),
    _TmnxOspfAreaInterfaceCount_Type()
)
tmnxOspfAreaInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaInterfaceCount.setStatus("current")
_TmnxOspfAreaVirtualLinkCount_Type = Unsigned32
_TmnxOspfAreaVirtualLinkCount_Object = MibTableColumn
tmnxOspfAreaVirtualLinkCount = _TmnxOspfAreaVirtualLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 22),
    _TmnxOspfAreaVirtualLinkCount_Type()
)
tmnxOspfAreaVirtualLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaVirtualLinkCount.setStatus("current")
_TmnxOspfAreaLastSpfRunTime_Type = TimeStamp
_TmnxOspfAreaLastSpfRunTime_Object = MibTableColumn
tmnxOspfAreaLastSpfRunTime = _TmnxOspfAreaLastSpfRunTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 23),
    _TmnxOspfAreaLastSpfRunTime_Type()
)
tmnxOspfAreaLastSpfRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaLastSpfRunTime.setStatus("current")
_TmnxOspfAreaSpfRuns_Type = Counter32
_TmnxOspfAreaSpfRuns_Object = MibTableColumn
tmnxOspfAreaSpfRuns = _TmnxOspfAreaSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 24),
    _TmnxOspfAreaSpfRuns_Type()
)
tmnxOspfAreaSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaSpfRuns.setStatus("current")
_TmnxOspfAreaNssaTranslatorEvents_Type = Counter32
_TmnxOspfAreaNssaTranslatorEvents_Object = MibTableColumn
tmnxOspfAreaNssaTranslatorEvents = _TmnxOspfAreaNssaTranslatorEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 25),
    _TmnxOspfAreaNssaTranslatorEvents_Type()
)
tmnxOspfAreaNssaTranslatorEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaNssaTranslatorEvents.setStatus("current")
_TmnxOspfAreaNeighborCount_Type = Gauge32
_TmnxOspfAreaNeighborCount_Object = MibTableColumn
tmnxOspfAreaNeighborCount = _TmnxOspfAreaNeighborCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 26),
    _TmnxOspfAreaNeighborCount_Type()
)
tmnxOspfAreaNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaNeighborCount.setStatus("current")
_TmnxOspfAreaShamLinkCount_Type = Gauge32
_TmnxOspfAreaShamLinkCount_Object = MibTableColumn
tmnxOspfAreaShamLinkCount = _TmnxOspfAreaShamLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 27),
    _TmnxOspfAreaShamLinkCount_Type()
)
tmnxOspfAreaShamLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaShamLinkCount.setStatus("current")


class _TmnxOspfAreaKeyRolloverInterval_Type(Unsigned32):
    """Custom type tmnxOspfAreaKeyRolloverInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_TmnxOspfAreaKeyRolloverInterval_Type.__name__ = "Unsigned32"
_TmnxOspfAreaKeyRolloverInterval_Object = MibTableColumn
tmnxOspfAreaKeyRolloverInterval = _TmnxOspfAreaKeyRolloverInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 28),
    _TmnxOspfAreaKeyRolloverInterval_Type()
)
tmnxOspfAreaKeyRolloverInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaKeyRolloverInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfAreaKeyRolloverInterval.setUnits("seconds")


class _TmnxOspfAreaLoopfreeAltExclude_Type(TruthValue):
    """Custom type tmnxOspfAreaLoopfreeAltExclude based on TruthValue"""
    defaultValue = 2


_TmnxOspfAreaLoopfreeAltExclude_Type.__name__ = "TruthValue"
_TmnxOspfAreaLoopfreeAltExclude_Object = MibTableColumn
tmnxOspfAreaLoopfreeAltExclude = _TmnxOspfAreaLoopfreeAltExclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 29),
    _TmnxOspfAreaLoopfreeAltExclude_Type()
)
tmnxOspfAreaLoopfreeAltExclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaLoopfreeAltExclude.setStatus("current")


class _TmnxOspfAreaNssaAdjCheck_Type(TruthValue):
    """Custom type tmnxOspfAreaNssaAdjCheck based on TruthValue"""
    defaultValue = 2


_TmnxOspfAreaNssaAdjCheck_Type.__name__ = "TruthValue"
_TmnxOspfAreaNssaAdjCheck_Object = MibTableColumn
tmnxOspfAreaNssaAdjCheck = _TmnxOspfAreaNssaAdjCheck_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 30),
    _TmnxOspfAreaNssaAdjCheck_Type()
)
tmnxOspfAreaNssaAdjCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaNssaAdjCheck.setStatus("current")


class _TmnxOspfAreaAdvRtrCapability_Type(TruthValue):
    """Custom type tmnxOspfAreaAdvRtrCapability based on TruthValue"""
    defaultValue = 1


_TmnxOspfAreaAdvRtrCapability_Type.__name__ = "TruthValue"
_TmnxOspfAreaAdvRtrCapability_Object = MibTableColumn
tmnxOspfAreaAdvRtrCapability = _TmnxOspfAreaAdvRtrCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 31),
    _TmnxOspfAreaAdvRtrCapability_Type()
)
tmnxOspfAreaAdvRtrCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaAdvRtrCapability.setStatus("current")


class _TmnxOspfAreaDbExportExclude_Type(TruthValue):
    """Custom type tmnxOspfAreaDbExportExclude based on TruthValue"""
    defaultValue = 2


_TmnxOspfAreaDbExportExclude_Type.__name__ = "TruthValue"
_TmnxOspfAreaDbExportExclude_Object = MibTableColumn
tmnxOspfAreaDbExportExclude = _TmnxOspfAreaDbExportExclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 32),
    _TmnxOspfAreaDbExportExclude_Type()
)
tmnxOspfAreaDbExportExclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaDbExportExclude.setStatus("current")


class _TmnxOspfAreaExtendedLsa_Type(Integer32):
    """Custom type tmnxOspfAreaExtendedLsa based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inherit", 0),
          ("only", 1))
    )


_TmnxOspfAreaExtendedLsa_Type.__name__ = "Integer32"
_TmnxOspfAreaExtendedLsa_Object = MibTableColumn
tmnxOspfAreaExtendedLsa = _TmnxOspfAreaExtendedLsa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 33),
    _TmnxOspfAreaExtendedLsa_Type()
)
tmnxOspfAreaExtendedLsa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaExtendedLsa.setStatus("current")


class _TmnxOspfAreaImportPolicy1_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfAreaImportPolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfAreaImportPolicy1_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfAreaImportPolicy1_Object = MibTableColumn
tmnxOspfAreaImportPolicy1 = _TmnxOspfAreaImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 34),
    _TmnxOspfAreaImportPolicy1_Type()
)
tmnxOspfAreaImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaImportPolicy1.setStatus("current")


class _TmnxOspfAreaImportPolicy2_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfAreaImportPolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfAreaImportPolicy2_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfAreaImportPolicy2_Object = MibTableColumn
tmnxOspfAreaImportPolicy2 = _TmnxOspfAreaImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 35),
    _TmnxOspfAreaImportPolicy2_Type()
)
tmnxOspfAreaImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaImportPolicy2.setStatus("current")


class _TmnxOspfAreaImportPolicy3_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfAreaImportPolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfAreaImportPolicy3_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfAreaImportPolicy3_Object = MibTableColumn
tmnxOspfAreaImportPolicy3 = _TmnxOspfAreaImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 36),
    _TmnxOspfAreaImportPolicy3_Type()
)
tmnxOspfAreaImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaImportPolicy3.setStatus("current")


class _TmnxOspfAreaImportPolicy4_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfAreaImportPolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfAreaImportPolicy4_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfAreaImportPolicy4_Object = MibTableColumn
tmnxOspfAreaImportPolicy4 = _TmnxOspfAreaImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 37),
    _TmnxOspfAreaImportPolicy4_Type()
)
tmnxOspfAreaImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaImportPolicy4.setStatus("current")


class _TmnxOspfAreaImportPolicy5_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfAreaImportPolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfAreaImportPolicy5_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfAreaImportPolicy5_Object = MibTableColumn
tmnxOspfAreaImportPolicy5 = _TmnxOspfAreaImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 38),
    _TmnxOspfAreaImportPolicy5_Type()
)
tmnxOspfAreaImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaImportPolicy5.setStatus("current")


class _TmnxOspfAreaExportPolicy1_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfAreaExportPolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfAreaExportPolicy1_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfAreaExportPolicy1_Object = MibTableColumn
tmnxOspfAreaExportPolicy1 = _TmnxOspfAreaExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 39),
    _TmnxOspfAreaExportPolicy1_Type()
)
tmnxOspfAreaExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaExportPolicy1.setStatus("current")


class _TmnxOspfAreaExportPolicy2_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfAreaExportPolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfAreaExportPolicy2_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfAreaExportPolicy2_Object = MibTableColumn
tmnxOspfAreaExportPolicy2 = _TmnxOspfAreaExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 40),
    _TmnxOspfAreaExportPolicy2_Type()
)
tmnxOspfAreaExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaExportPolicy2.setStatus("current")


class _TmnxOspfAreaExportPolicy3_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfAreaExportPolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfAreaExportPolicy3_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfAreaExportPolicy3_Object = MibTableColumn
tmnxOspfAreaExportPolicy3 = _TmnxOspfAreaExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 41),
    _TmnxOspfAreaExportPolicy3_Type()
)
tmnxOspfAreaExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaExportPolicy3.setStatus("current")


class _TmnxOspfAreaExportPolicy4_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfAreaExportPolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfAreaExportPolicy4_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfAreaExportPolicy4_Object = MibTableColumn
tmnxOspfAreaExportPolicy4 = _TmnxOspfAreaExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 42),
    _TmnxOspfAreaExportPolicy4_Type()
)
tmnxOspfAreaExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaExportPolicy4.setStatus("current")


class _TmnxOspfAreaExportPolicy5_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfAreaExportPolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfAreaExportPolicy5_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfAreaExportPolicy5_Object = MibTableColumn
tmnxOspfAreaExportPolicy5 = _TmnxOspfAreaExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 43),
    _TmnxOspfAreaExportPolicy5_Type()
)
tmnxOspfAreaExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaExportPolicy5.setStatus("current")


class _TmnxOspfAreaAdvertiseNeProfile_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfAreaAdvertiseNeProfile based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfAreaAdvertiseNeProfile_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfAreaAdvertiseNeProfile_Object = MibTableColumn
tmnxOspfAreaAdvertiseNeProfile = _TmnxOspfAreaAdvertiseNeProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 44),
    _TmnxOspfAreaAdvertiseNeProfile_Type()
)
tmnxOspfAreaAdvertiseNeProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaAdvertiseNeProfile.setStatus("current")


class _TmnxOspfAreaBierTemplate_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfAreaBierTemplate based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfAreaBierTemplate_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfAreaBierTemplate_Object = MibTableColumn
tmnxOspfAreaBierTemplate = _TmnxOspfAreaBierTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 45),
    _TmnxOspfAreaBierTemplate_Type()
)
tmnxOspfAreaBierTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaBierTemplate.setStatus("current")


class _TmnxOspfAreaBierTemplAdminState_Type(TmnxAdminState):
    """Custom type tmnxOspfAreaBierTemplAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxOspfAreaBierTemplAdminState_Type.__name__ = "TmnxAdminState"
_TmnxOspfAreaBierTemplAdminState_Object = MibTableColumn
tmnxOspfAreaBierTemplAdminState = _TmnxOspfAreaBierTemplAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 6, 1, 46),
    _TmnxOspfAreaBierTemplAdminState_Type()
)
tmnxOspfAreaBierTemplAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaBierTemplAdminState.setStatus("current")
_TmnxOspfAreaLsaCountTable_Object = MibTable
tmnxOspfAreaLsaCountTable = _TmnxOspfAreaLsaCountTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 7)
)
if mibBuilder.loadTexts:
    tmnxOspfAreaLsaCountTable.setStatus("current")
_TmnxOspfAreaLsaCountEntry_Object = MibTableRow
tmnxOspfAreaLsaCountEntry = _TmnxOspfAreaLsaCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 7, 1)
)
tmnxOspfAreaLsaCountEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsaCountLsaType"),
)
if mibBuilder.loadTexts:
    tmnxOspfAreaLsaCountEntry.setStatus("current")


class _TmnxOspfAreaLsaCountLsaType_Type(Unsigned32):
    """Custom type tmnxOspfAreaLsaCountLsaType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxOspfAreaLsaCountLsaType_Type.__name__ = "Unsigned32"
_TmnxOspfAreaLsaCountLsaType_Object = MibTableColumn
tmnxOspfAreaLsaCountLsaType = _TmnxOspfAreaLsaCountLsaType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 7, 1, 1),
    _TmnxOspfAreaLsaCountLsaType_Type()
)
tmnxOspfAreaLsaCountLsaType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfAreaLsaCountLsaType.setStatus("current")
_TmnxOspfAreaLsaCountNumber_Type = Gauge32
_TmnxOspfAreaLsaCountNumber_Object = MibTableColumn
tmnxOspfAreaLsaCountNumber = _TmnxOspfAreaLsaCountNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 7, 1, 2),
    _TmnxOspfAreaLsaCountNumber_Type()
)
tmnxOspfAreaLsaCountNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaLsaCountNumber.setStatus("current")
_TmnxOspfAsLsdbTable_Object = MibTable
tmnxOspfAsLsdbTable = _TmnxOspfAsLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 8)
)
if mibBuilder.loadTexts:
    tmnxOspfAsLsdbTable.setStatus("current")
_TmnxOspfAsLsdbEntry_Object = MibTableRow
tmnxOspfAsLsdbEntry = _TmnxOspfAsLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 8, 1)
)
tmnxOspfAsLsdbEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAsLsdbType"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAsLsdbRouterId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAsLsdbLsid"),
)
if mibBuilder.loadTexts:
    tmnxOspfAsLsdbEntry.setStatus("current")


class _TmnxOspfAsLsdbType_Type(Unsigned32):
    """Custom type tmnxOspfAsLsdbType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TmnxOspfAsLsdbType_Type.__name__ = "Unsigned32"
_TmnxOspfAsLsdbType_Object = MibTableColumn
tmnxOspfAsLsdbType = _TmnxOspfAsLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 8, 1, 1),
    _TmnxOspfAsLsdbType_Type()
)
tmnxOspfAsLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfAsLsdbType.setStatus("current")
_TmnxOspfAsLsdbRouterId_Type = TmnxOspfRouterIdTc
_TmnxOspfAsLsdbRouterId_Object = MibTableColumn
tmnxOspfAsLsdbRouterId = _TmnxOspfAsLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 8, 1, 2),
    _TmnxOspfAsLsdbRouterId_Type()
)
tmnxOspfAsLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfAsLsdbRouterId.setStatus("current")
_TmnxOspfAsLsdbLsid_Type = Unsigned32
_TmnxOspfAsLsdbLsid_Object = MibTableColumn
tmnxOspfAsLsdbLsid = _TmnxOspfAsLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 8, 1, 3),
    _TmnxOspfAsLsdbLsid_Type()
)
tmnxOspfAsLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfAsLsdbLsid.setStatus("current")
_TmnxOspfAsLsdbSequence_Type = Integer32
_TmnxOspfAsLsdbSequence_Object = MibTableColumn
tmnxOspfAsLsdbSequence = _TmnxOspfAsLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 8, 1, 4),
    _TmnxOspfAsLsdbSequence_Type()
)
tmnxOspfAsLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAsLsdbSequence.setStatus("current")
_TmnxOspfAsLsdbAge_Type = Integer32
_TmnxOspfAsLsdbAge_Object = MibTableColumn
tmnxOspfAsLsdbAge = _TmnxOspfAsLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 8, 1, 5),
    _TmnxOspfAsLsdbAge_Type()
)
tmnxOspfAsLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAsLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfAsLsdbAge.setUnits("seconds")
_TmnxOspfAsLsdbChecksum_Type = Integer32
_TmnxOspfAsLsdbChecksum_Object = MibTableColumn
tmnxOspfAsLsdbChecksum = _TmnxOspfAsLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 8, 1, 6),
    _TmnxOspfAsLsdbChecksum_Type()
)
tmnxOspfAsLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAsLsdbChecksum.setStatus("current")


class _TmnxOspfAsLsdbAdvertisement_Type(OctetString):
    """Custom type tmnxOspfAsLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_TmnxOspfAsLsdbAdvertisement_Type.__name__ = "OctetString"
_TmnxOspfAsLsdbAdvertisement_Object = MibTableColumn
tmnxOspfAsLsdbAdvertisement = _TmnxOspfAsLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 8, 1, 7),
    _TmnxOspfAsLsdbAdvertisement_Type()
)
tmnxOspfAsLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAsLsdbAdvertisement.setStatus("current")
_TmnxOspfAsLsdbTypeKnown_Type = TruthValue
_TmnxOspfAsLsdbTypeKnown_Object = MibTableColumn
tmnxOspfAsLsdbTypeKnown = _TmnxOspfAsLsdbTypeKnown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 8, 1, 8),
    _TmnxOspfAsLsdbTypeKnown_Type()
)
tmnxOspfAsLsdbTypeKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAsLsdbTypeKnown.setStatus("current")
_TmnxOspfAreaLsdbTable_Object = MibTable
tmnxOspfAreaLsdbTable = _TmnxOspfAreaLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 9)
)
if mibBuilder.loadTexts:
    tmnxOspfAreaLsdbTable.setStatus("current")
_TmnxOspfAreaLsdbEntry_Object = MibTableRow
tmnxOspfAreaLsdbEntry = _TmnxOspfAreaLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 9, 1)
)
tmnxOspfAreaLsdbEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsdbAreaId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsdbType"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsdbRouterId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsdbLsid"),
)
if mibBuilder.loadTexts:
    tmnxOspfAreaLsdbEntry.setStatus("current")
_TmnxOspfAreaLsdbAreaId_Type = TmnxOspfAreaIdTc
_TmnxOspfAreaLsdbAreaId_Object = MibTableColumn
tmnxOspfAreaLsdbAreaId = _TmnxOspfAreaLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 9, 1, 1),
    _TmnxOspfAreaLsdbAreaId_Type()
)
tmnxOspfAreaLsdbAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfAreaLsdbAreaId.setStatus("current")


class _TmnxOspfAreaLsdbType_Type(Unsigned32):
    """Custom type tmnxOspfAreaLsdbType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TmnxOspfAreaLsdbType_Type.__name__ = "Unsigned32"
_TmnxOspfAreaLsdbType_Object = MibTableColumn
tmnxOspfAreaLsdbType = _TmnxOspfAreaLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 9, 1, 2),
    _TmnxOspfAreaLsdbType_Type()
)
tmnxOspfAreaLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfAreaLsdbType.setStatus("current")
_TmnxOspfAreaLsdbRouterId_Type = TmnxOspfRouterIdTc
_TmnxOspfAreaLsdbRouterId_Object = MibTableColumn
tmnxOspfAreaLsdbRouterId = _TmnxOspfAreaLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 9, 1, 3),
    _TmnxOspfAreaLsdbRouterId_Type()
)
tmnxOspfAreaLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfAreaLsdbRouterId.setStatus("current")
_TmnxOspfAreaLsdbLsid_Type = Unsigned32
_TmnxOspfAreaLsdbLsid_Object = MibTableColumn
tmnxOspfAreaLsdbLsid = _TmnxOspfAreaLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 9, 1, 4),
    _TmnxOspfAreaLsdbLsid_Type()
)
tmnxOspfAreaLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfAreaLsdbLsid.setStatus("current")
_TmnxOspfAreaLsdbSequence_Type = Integer32
_TmnxOspfAreaLsdbSequence_Object = MibTableColumn
tmnxOspfAreaLsdbSequence = _TmnxOspfAreaLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 9, 1, 5),
    _TmnxOspfAreaLsdbSequence_Type()
)
tmnxOspfAreaLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaLsdbSequence.setStatus("current")
_TmnxOspfAreaLsdbAge_Type = Integer32
_TmnxOspfAreaLsdbAge_Object = MibTableColumn
tmnxOspfAreaLsdbAge = _TmnxOspfAreaLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 9, 1, 6),
    _TmnxOspfAreaLsdbAge_Type()
)
tmnxOspfAreaLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfAreaLsdbAge.setUnits("seconds")
_TmnxOspfAreaLsdbChecksum_Type = Integer32
_TmnxOspfAreaLsdbChecksum_Object = MibTableColumn
tmnxOspfAreaLsdbChecksum = _TmnxOspfAreaLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 9, 1, 7),
    _TmnxOspfAreaLsdbChecksum_Type()
)
tmnxOspfAreaLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaLsdbChecksum.setStatus("current")


class _TmnxOspfAreaLsdbAdvertisement_Type(OctetString):
    """Custom type tmnxOspfAreaLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_TmnxOspfAreaLsdbAdvertisement_Type.__name__ = "OctetString"
_TmnxOspfAreaLsdbAdvertisement_Object = MibTableColumn
tmnxOspfAreaLsdbAdvertisement = _TmnxOspfAreaLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 9, 1, 8),
    _TmnxOspfAreaLsdbAdvertisement_Type()
)
tmnxOspfAreaLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaLsdbAdvertisement.setStatus("current")
_TmnxOspfAreaLsdbTypeKnown_Type = TruthValue
_TmnxOspfAreaLsdbTypeKnown_Object = MibTableColumn
tmnxOspfAreaLsdbTypeKnown = _TmnxOspfAreaLsdbTypeKnown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 9, 1, 9),
    _TmnxOspfAreaLsdbTypeKnown_Type()
)
tmnxOspfAreaLsdbTypeKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaLsdbTypeKnown.setStatus("current")
_TmnxOspfAreaLsdbImportFltrd_Type = TruthValue
_TmnxOspfAreaLsdbImportFltrd_Object = MibTableColumn
tmnxOspfAreaLsdbImportFltrd = _TmnxOspfAreaLsdbImportFltrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 9, 1, 10),
    _TmnxOspfAreaLsdbImportFltrd_Type()
)
tmnxOspfAreaLsdbImportFltrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaLsdbImportFltrd.setStatus("current")
_TmnxOspfAreaLsdbExportFltrd_Type = TruthValue
_TmnxOspfAreaLsdbExportFltrd_Object = MibTableColumn
tmnxOspfAreaLsdbExportFltrd = _TmnxOspfAreaLsdbExportFltrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 9, 1, 11),
    _TmnxOspfAreaLsdbExportFltrd_Type()
)
tmnxOspfAreaLsdbExportFltrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaLsdbExportFltrd.setStatus("current")
_TmnxOspfLinkLsdbTable_Object = MibTable
tmnxOspfLinkLsdbTable = _TmnxOspfLinkLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 10)
)
if mibBuilder.loadTexts:
    tmnxOspfLinkLsdbTable.setStatus("obsolete")
_TmnxOspfLinkLsdbEntry_Object = MibTableRow
tmnxOspfLinkLsdbEntry = _TmnxOspfLinkLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 10, 1)
)
tmnxOspfLinkLsdbEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkLsdbIfIndex"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkLsdbIfInstId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkLsdbType"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkLsdbRouterId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkLsdbLsid"),
)
if mibBuilder.loadTexts:
    tmnxOspfLinkLsdbEntry.setStatus("obsolete")
_TmnxOspfLinkLsdbIfIndex_Type = InterfaceIndex
_TmnxOspfLinkLsdbIfIndex_Object = MibTableColumn
tmnxOspfLinkLsdbIfIndex = _TmnxOspfLinkLsdbIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 10, 1, 1),
    _TmnxOspfLinkLsdbIfIndex_Type()
)
tmnxOspfLinkLsdbIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfLinkLsdbIfIndex.setStatus("obsolete")
_TmnxOspfLinkLsdbIfInstId_Type = TmnxOspfIfInstIdTc
_TmnxOspfLinkLsdbIfInstId_Object = MibTableColumn
tmnxOspfLinkLsdbIfInstId = _TmnxOspfLinkLsdbIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 10, 1, 2),
    _TmnxOspfLinkLsdbIfInstId_Type()
)
tmnxOspfLinkLsdbIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfLinkLsdbIfInstId.setStatus("obsolete")


class _TmnxOspfLinkLsdbType_Type(Unsigned32):
    """Custom type tmnxOspfLinkLsdbType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TmnxOspfLinkLsdbType_Type.__name__ = "Unsigned32"
_TmnxOspfLinkLsdbType_Object = MibTableColumn
tmnxOspfLinkLsdbType = _TmnxOspfLinkLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 10, 1, 3),
    _TmnxOspfLinkLsdbType_Type()
)
tmnxOspfLinkLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfLinkLsdbType.setStatus("obsolete")
_TmnxOspfLinkLsdbRouterId_Type = TmnxOspfRouterIdTc
_TmnxOspfLinkLsdbRouterId_Object = MibTableColumn
tmnxOspfLinkLsdbRouterId = _TmnxOspfLinkLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 10, 1, 4),
    _TmnxOspfLinkLsdbRouterId_Type()
)
tmnxOspfLinkLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfLinkLsdbRouterId.setStatus("obsolete")
_TmnxOspfLinkLsdbLsid_Type = Unsigned32
_TmnxOspfLinkLsdbLsid_Object = MibTableColumn
tmnxOspfLinkLsdbLsid = _TmnxOspfLinkLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 10, 1, 5),
    _TmnxOspfLinkLsdbLsid_Type()
)
tmnxOspfLinkLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfLinkLsdbLsid.setStatus("obsolete")
_TmnxOspfLinkLsdbSequence_Type = Integer32
_TmnxOspfLinkLsdbSequence_Object = MibTableColumn
tmnxOspfLinkLsdbSequence = _TmnxOspfLinkLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 10, 1, 6),
    _TmnxOspfLinkLsdbSequence_Type()
)
tmnxOspfLinkLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLinkLsdbSequence.setStatus("obsolete")
_TmnxOspfLinkLsdbAge_Type = Integer32
_TmnxOspfLinkLsdbAge_Object = MibTableColumn
tmnxOspfLinkLsdbAge = _TmnxOspfLinkLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 10, 1, 7),
    _TmnxOspfLinkLsdbAge_Type()
)
tmnxOspfLinkLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLinkLsdbAge.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOspfLinkLsdbAge.setUnits("seconds")
_TmnxOspfLinkLsdbChecksum_Type = Integer32
_TmnxOspfLinkLsdbChecksum_Object = MibTableColumn
tmnxOspfLinkLsdbChecksum = _TmnxOspfLinkLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 10, 1, 8),
    _TmnxOspfLinkLsdbChecksum_Type()
)
tmnxOspfLinkLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLinkLsdbChecksum.setStatus("obsolete")


class _TmnxOspfLinkLsdbAdvertisement_Type(OctetString):
    """Custom type tmnxOspfLinkLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_TmnxOspfLinkLsdbAdvertisement_Type.__name__ = "OctetString"
_TmnxOspfLinkLsdbAdvertisement_Object = MibTableColumn
tmnxOspfLinkLsdbAdvertisement = _TmnxOspfLinkLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 10, 1, 9),
    _TmnxOspfLinkLsdbAdvertisement_Type()
)
tmnxOspfLinkLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLinkLsdbAdvertisement.setStatus("obsolete")
_TmnxOspfLinkLsdbTypeKnown_Type = TruthValue
_TmnxOspfLinkLsdbTypeKnown_Object = MibTableColumn
tmnxOspfLinkLsdbTypeKnown = _TmnxOspfLinkLsdbTypeKnown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 10, 1, 10),
    _TmnxOspfLinkLsdbTypeKnown_Type()
)
tmnxOspfLinkLsdbTypeKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLinkLsdbTypeKnown.setStatus("obsolete")
_TmnxOspfHostTable_Object = MibTable
tmnxOspfHostTable = _TmnxOspfHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 11)
)
if mibBuilder.loadTexts:
    tmnxOspfHostTable.setStatus("current")
_TmnxOspfHostEntry_Object = MibTableRow
tmnxOspfHostEntry = _TmnxOspfHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 11, 1)
)
tmnxOspfHostEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfHostAddressType"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfHostAddress"),
)
if mibBuilder.loadTexts:
    tmnxOspfHostEntry.setStatus("current")
_TmnxOspfHostAddressType_Type = InetAddressType
_TmnxOspfHostAddressType_Object = MibTableColumn
tmnxOspfHostAddressType = _TmnxOspfHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 11, 1, 1),
    _TmnxOspfHostAddressType_Type()
)
tmnxOspfHostAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfHostAddressType.setStatus("current")


class _TmnxOspfHostAddress_Type(InetAddress):
    """Custom type tmnxOspfHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOspfHostAddress_Type.__name__ = "InetAddress"
_TmnxOspfHostAddress_Object = MibTableColumn
tmnxOspfHostAddress = _TmnxOspfHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 11, 1, 2),
    _TmnxOspfHostAddress_Type()
)
tmnxOspfHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfHostAddress.setStatus("current")
_TmnxOspfHostMetric_Type = Metric
_TmnxOspfHostMetric_Object = MibTableColumn
tmnxOspfHostMetric = _TmnxOspfHostMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 11, 1, 3),
    _TmnxOspfHostMetric_Type()
)
tmnxOspfHostMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfHostMetric.setStatus("current")
_TmnxOspfHostStatus_Type = RowStatus
_TmnxOspfHostStatus_Object = MibTableColumn
tmnxOspfHostStatus = _TmnxOspfHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 11, 1, 4),
    _TmnxOspfHostStatus_Type()
)
tmnxOspfHostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfHostStatus.setStatus("current")
_TmnxOspfHostLastChanged_Type = TimeStamp
_TmnxOspfHostLastChanged_Object = MibTableColumn
tmnxOspfHostLastChanged = _TmnxOspfHostLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 11, 1, 5),
    _TmnxOspfHostLastChanged_Type()
)
tmnxOspfHostLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfHostLastChanged.setStatus("current")
_TmnxOspfHostAreaID_Type = TmnxOspfAreaIdTc
_TmnxOspfHostAreaID_Object = MibTableColumn
tmnxOspfHostAreaID = _TmnxOspfHostAreaID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 11, 1, 6),
    _TmnxOspfHostAreaID_Type()
)
tmnxOspfHostAreaID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfHostAreaID.setStatus("current")
_TmnxOspfIfTable_Object = MibTable
tmnxOspfIfTable = _TmnxOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12)
)
if mibBuilder.loadTexts:
    tmnxOspfIfTable.setStatus("obsolete")
_TmnxOspfIfEntry_Object = MibTableRow
tmnxOspfIfEntry = _TmnxOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1)
)
tmnxOspfIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfIfIndex"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfIfInstId"),
)
if mibBuilder.loadTexts:
    tmnxOspfIfEntry.setStatus("obsolete")
_TmnxOspfIfIndex_Type = InterfaceIndex
_TmnxOspfIfIndex_Object = MibTableColumn
tmnxOspfIfIndex = _TmnxOspfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 1),
    _TmnxOspfIfIndex_Type()
)
tmnxOspfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfIfIndex.setStatus("obsolete")
_TmnxOspfIfInstId_Type = TmnxOspfIfInstIdTc
_TmnxOspfIfInstId_Object = MibTableColumn
tmnxOspfIfInstId = _TmnxOspfIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 2),
    _TmnxOspfIfInstId_Type()
)
tmnxOspfIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfIfInstId.setStatus("obsolete")
_TmnxOspfIfStatus_Type = RowStatus
_TmnxOspfIfStatus_Object = MibTableColumn
tmnxOspfIfStatus = _TmnxOspfIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 3),
    _TmnxOspfIfStatus_Type()
)
tmnxOspfIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfStatus.setStatus("obsolete")
_TmnxOspfIfLastChanged_Type = TimeStamp
_TmnxOspfIfLastChanged_Object = MibTableColumn
tmnxOspfIfLastChanged = _TmnxOspfIfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 4),
    _TmnxOspfIfLastChanged_Type()
)
tmnxOspfIfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfLastChanged.setStatus("obsolete")


class _TmnxOspfIfAreaId_Type(TmnxOspfAreaIdTc):
    """Custom type tmnxOspfIfAreaId based on TmnxOspfAreaIdTc"""
    defaultValue = 0


_TmnxOspfIfAreaId_Type.__name__ = "TmnxOspfAreaIdTc"
_TmnxOspfIfAreaId_Object = MibTableColumn
tmnxOspfIfAreaId = _TmnxOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 5),
    _TmnxOspfIfAreaId_Type()
)
tmnxOspfIfAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfAreaId.setStatus("obsolete")
_TmnxOspfIfCfgType_Type = TmnxOspfIfTypeTc
_TmnxOspfIfCfgType_Object = MibTableColumn
tmnxOspfIfCfgType = _TmnxOspfIfCfgType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 6),
    _TmnxOspfIfCfgType_Type()
)
tmnxOspfIfCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfCfgType.setStatus("obsolete")


class _TmnxOspfIfAdminState_Type(Status):
    """Custom type tmnxOspfIfAdminState based on Status"""
    defaultValue = 1


_TmnxOspfIfAdminState_Type.__name__ = "Status"
_TmnxOspfIfAdminState_Object = MibTableColumn
tmnxOspfIfAdminState = _TmnxOspfIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 7),
    _TmnxOspfIfAdminState_Type()
)
tmnxOspfIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfAdminState.setStatus("obsolete")


class _TmnxOspfIfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type tmnxOspfIfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_TmnxOspfIfRtrPriority_Type.__name__ = "DesignatedRouterPriority"
_TmnxOspfIfRtrPriority_Object = MibTableColumn
tmnxOspfIfRtrPriority = _TmnxOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 8),
    _TmnxOspfIfRtrPriority_Type()
)
tmnxOspfIfRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfRtrPriority.setStatus("obsolete")


class _TmnxOspfIfTransitDelay_Type(TmnxOspfUpToRefreshIntervalTc):
    """Custom type tmnxOspfIfTransitDelay based on TmnxOspfUpToRefreshIntervalTc"""
    defaultValue = 1

    subtypeSpec = TmnxOspfUpToRefreshIntervalTc.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_TmnxOspfIfTransitDelay_Type.__name__ = "TmnxOspfUpToRefreshIntervalTc"
_TmnxOspfIfTransitDelay_Object = MibTableColumn
tmnxOspfIfTransitDelay = _TmnxOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 9),
    _TmnxOspfIfTransitDelay_Type()
)
tmnxOspfIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfTransitDelay.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOspfIfTransitDelay.setUnits("seconds")


class _TmnxOspfIfRetransInterval_Type(TmnxOspfUpToRefreshIntervalTc):
    """Custom type tmnxOspfIfRetransInterval based on TmnxOspfUpToRefreshIntervalTc"""
    defaultValue = 5

    subtypeSpec = TmnxOspfUpToRefreshIntervalTc.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_TmnxOspfIfRetransInterval_Type.__name__ = "TmnxOspfUpToRefreshIntervalTc"
_TmnxOspfIfRetransInterval_Object = MibTableColumn
tmnxOspfIfRetransInterval = _TmnxOspfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 10),
    _TmnxOspfIfRetransInterval_Type()
)
tmnxOspfIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfRetransInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOspfIfRetransInterval.setUnits("seconds")


class _TmnxOspfIfHelloInterval_Type(HelloRange):
    """Custom type tmnxOspfIfHelloInterval based on HelloRange"""
    defaultValue = 10


_TmnxOspfIfHelloInterval_Type.__name__ = "HelloRange"
_TmnxOspfIfHelloInterval_Object = MibTableColumn
tmnxOspfIfHelloInterval = _TmnxOspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 11),
    _TmnxOspfIfHelloInterval_Type()
)
tmnxOspfIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfHelloInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOspfIfHelloInterval.setUnits("seconds")


class _TmnxOspfIfRtrDeadInterval_Type(TmnxOspfDeadIntRangeTc):
    """Custom type tmnxOspfIfRtrDeadInterval based on TmnxOspfDeadIntRangeTc"""
    defaultValue = 40


_TmnxOspfIfRtrDeadInterval_Type.__name__ = "TmnxOspfDeadIntRangeTc"
_TmnxOspfIfRtrDeadInterval_Object = MibTableColumn
tmnxOspfIfRtrDeadInterval = _TmnxOspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 12),
    _TmnxOspfIfRtrDeadInterval_Type()
)
tmnxOspfIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfRtrDeadInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOspfIfRtrDeadInterval.setUnits("seconds")


class _TmnxOspfIfPollInterval_Type(Unsigned32):
    """Custom type tmnxOspfIfPollInterval based on Unsigned32"""
    defaultValue = 120


_TmnxOspfIfPollInterval_Type.__name__ = "Unsigned32"
_TmnxOspfIfPollInterval_Object = MibTableColumn
tmnxOspfIfPollInterval = _TmnxOspfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 13),
    _TmnxOspfIfPollInterval_Type()
)
tmnxOspfIfPollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfPollInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOspfIfPollInterval.setUnits("seconds")


class _TmnxOspfIfMulticastForwarding_Type(Integer32):
    """Custom type tmnxOspfIfMulticastForwarding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("multicast", 2),
          ("unicast", 3))
    )


_TmnxOspfIfMulticastForwarding_Type.__name__ = "Integer32"
_TmnxOspfIfMulticastForwarding_Object = MibTableColumn
tmnxOspfIfMulticastForwarding = _TmnxOspfIfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 14),
    _TmnxOspfIfMulticastForwarding_Type()
)
tmnxOspfIfMulticastForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfMulticastForwarding.setStatus("obsolete")


class _TmnxOspfIfCfgMTU_Type(Integer32):
    """Custom type tmnxOspfIfCfgMTU based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9198),
    )


_TmnxOspfIfCfgMTU_Type.__name__ = "Integer32"
_TmnxOspfIfCfgMTU_Object = MibTableColumn
tmnxOspfIfCfgMTU = _TmnxOspfIfCfgMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 15),
    _TmnxOspfIfCfgMTU_Type()
)
tmnxOspfIfCfgMTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfCfgMTU.setStatus("obsolete")


class _TmnxOspfIfCfgMetric_Type(Metric):
    """Custom type tmnxOspfIfCfgMetric based on Metric"""
    defaultValue = 0


_TmnxOspfIfCfgMetric_Type.__name__ = "Metric"
_TmnxOspfIfCfgMetric_Object = MibTableColumn
tmnxOspfIfCfgMetric = _TmnxOspfIfCfgMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 16),
    _TmnxOspfIfCfgMetric_Type()
)
tmnxOspfIfCfgMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfCfgMetric.setStatus("obsolete")


class _TmnxOspfIfPassive_Type(TruthValue):
    """Custom type tmnxOspfIfPassive based on TruthValue"""
    defaultValue = 2


_TmnxOspfIfPassive_Type.__name__ = "TruthValue"
_TmnxOspfIfPassive_Object = MibTableColumn
tmnxOspfIfPassive = _TmnxOspfIfPassive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 17),
    _TmnxOspfIfPassive_Type()
)
tmnxOspfIfPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfPassive.setStatus("obsolete")


class _TmnxOspfIfAdvtSubnet_Type(TruthValue):
    """Custom type tmnxOspfIfAdvtSubnet based on TruthValue"""
    defaultValue = 1


_TmnxOspfIfAdvtSubnet_Type.__name__ = "TruthValue"
_TmnxOspfIfAdvtSubnet_Object = MibTableColumn
tmnxOspfIfAdvtSubnet = _TmnxOspfIfAdvtSubnet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 18),
    _TmnxOspfIfAdvtSubnet_Type()
)
tmnxOspfIfAdvtSubnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfAdvtSubnet.setStatus("obsolete")


class _TmnxOspfIfDemand_Type(TruthValue):
    """Custom type tmnxOspfIfDemand based on TruthValue"""
    defaultValue = 2


_TmnxOspfIfDemand_Type.__name__ = "TruthValue"
_TmnxOspfIfDemand_Object = MibTableColumn
tmnxOspfIfDemand = _TmnxOspfIfDemand_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 19),
    _TmnxOspfIfDemand_Type()
)
tmnxOspfIfDemand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfDemand.setStatus("obsolete")


class _TmnxOspfIfDemandNbrProbe_Type(TruthValue):
    """Custom type tmnxOspfIfDemandNbrProbe based on TruthValue"""
    defaultValue = 2


_TmnxOspfIfDemandNbrProbe_Type.__name__ = "TruthValue"
_TmnxOspfIfDemandNbrProbe_Object = MibTableColumn
tmnxOspfIfDemandNbrProbe = _TmnxOspfIfDemandNbrProbe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 20),
    _TmnxOspfIfDemandNbrProbe_Type()
)
tmnxOspfIfDemandNbrProbe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfDemandNbrProbe.setStatus("obsolete")


class _TmnxOspfIfDemandNbrProbeRetxLimit_Type(Unsigned32):
    """Custom type tmnxOspfIfDemandNbrProbeRetxLimit based on Unsigned32"""
    defaultValue = 10


_TmnxOspfIfDemandNbrProbeRetxLimit_Type.__name__ = "Unsigned32"
_TmnxOspfIfDemandNbrProbeRetxLimit_Object = MibTableColumn
tmnxOspfIfDemandNbrProbeRetxLimit = _TmnxOspfIfDemandNbrProbeRetxLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 21),
    _TmnxOspfIfDemandNbrProbeRetxLimit_Type()
)
tmnxOspfIfDemandNbrProbeRetxLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfDemandNbrProbeRetxLimit.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOspfIfDemandNbrProbeRetxLimit.setUnits("seconds")


class _TmnxOspfIfDemandNbrProbeInterval_Type(Unsigned32):
    """Custom type tmnxOspfIfDemandNbrProbeInterval based on Unsigned32"""
    defaultValue = 120


_TmnxOspfIfDemandNbrProbeInterval_Type.__name__ = "Unsigned32"
_TmnxOspfIfDemandNbrProbeInterval_Object = MibTableColumn
tmnxOspfIfDemandNbrProbeInterval = _TmnxOspfIfDemandNbrProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 22),
    _TmnxOspfIfDemandNbrProbeInterval_Type()
)
tmnxOspfIfDemandNbrProbeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfDemandNbrProbeInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOspfIfDemandNbrProbeInterval.setUnits("seconds")


class _TmnxOspfIfAuthType_Type(TmnxOspfAuthenticationType):
    """Custom type tmnxOspfIfAuthType based on TmnxOspfAuthenticationType"""
    defaultValue = 0


_TmnxOspfIfAuthType_Type.__name__ = "TmnxOspfAuthenticationType"
_TmnxOspfIfAuthType_Object = MibTableColumn
tmnxOspfIfAuthType = _TmnxOspfIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 23),
    _TmnxOspfIfAuthType_Type()
)
tmnxOspfIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfAuthType.setStatus("obsolete")


class _TmnxOspfIfAuthKey_Type(OctetString):
    """Custom type tmnxOspfIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TmnxOspfIfAuthKey_Type.__name__ = "OctetString"
_TmnxOspfIfAuthKey_Object = MibTableColumn
tmnxOspfIfAuthKey = _TmnxOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 24),
    _TmnxOspfIfAuthKey_Type()
)
tmnxOspfIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfAuthKey.setStatus("obsolete")


class _TmnxOspfIfState_Type(Integer32):
    """Custom type tmnxOspfIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("loopback", 2),
          ("waiting", 3),
          ("pointToPoint", 4),
          ("designatedRouter", 5),
          ("backupDesignatedRouter", 6),
          ("otherDesignatedRouter", 7))
    )


_TmnxOspfIfState_Type.__name__ = "Integer32"
_TmnxOspfIfState_Object = MibTableColumn
tmnxOspfIfState = _TmnxOspfIfState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 25),
    _TmnxOspfIfState_Type()
)
tmnxOspfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfState.setStatus("obsolete")
_TmnxOspfIfLastEnabledTime_Type = TimeStamp
_TmnxOspfIfLastEnabledTime_Object = MibTableColumn
tmnxOspfIfLastEnabledTime = _TmnxOspfIfLastEnabledTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 26),
    _TmnxOspfIfLastEnabledTime_Type()
)
tmnxOspfIfLastEnabledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfLastEnabledTime.setStatus("obsolete")
_TmnxOspfIfOperMTU_Type = Integer32
_TmnxOspfIfOperMTU_Object = MibTableColumn
tmnxOspfIfOperMTU = _TmnxOspfIfOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 27),
    _TmnxOspfIfOperMTU_Type()
)
tmnxOspfIfOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfOperMTU.setStatus("obsolete")
_TmnxOspfIfMetricValue_Type = Metric
_TmnxOspfIfMetricValue_Object = MibTableColumn
tmnxOspfIfMetricValue = _TmnxOspfIfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 28),
    _TmnxOspfIfMetricValue_Type()
)
tmnxOspfIfMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfMetricValue.setStatus("obsolete")
_TmnxOspfIfDRId_Type = TmnxOspfRouterIdTc
_TmnxOspfIfDRId_Object = MibTableColumn
tmnxOspfIfDRId = _TmnxOspfIfDRId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 29),
    _TmnxOspfIfDRId_Type()
)
tmnxOspfIfDRId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfDRId.setStatus("obsolete")
_TmnxOspfIfDRIpAddrType_Type = InetAddressType
_TmnxOspfIfDRIpAddrType_Object = MibTableColumn
tmnxOspfIfDRIpAddrType = _TmnxOspfIfDRIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 30),
    _TmnxOspfIfDRIpAddrType_Type()
)
tmnxOspfIfDRIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfDRIpAddrType.setStatus("obsolete")


class _TmnxOspfIfDRIpAddr_Type(InetAddress):
    """Custom type tmnxOspfIfDRIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(20, 20),
    )


_TmnxOspfIfDRIpAddr_Type.__name__ = "InetAddress"
_TmnxOspfIfDRIpAddr_Object = MibTableColumn
tmnxOspfIfDRIpAddr = _TmnxOspfIfDRIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 31),
    _TmnxOspfIfDRIpAddr_Type()
)
tmnxOspfIfDRIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfDRIpAddr.setStatus("obsolete")
_TmnxOspfIfBDRId_Type = TmnxOspfRouterIdTc
_TmnxOspfIfBDRId_Object = MibTableColumn
tmnxOspfIfBDRId = _TmnxOspfIfBDRId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 32),
    _TmnxOspfIfBDRId_Type()
)
tmnxOspfIfBDRId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfBDRId.setStatus("obsolete")
_TmnxOspfIfBDRIpAddrType_Type = InetAddressType
_TmnxOspfIfBDRIpAddrType_Object = MibTableColumn
tmnxOspfIfBDRIpAddrType = _TmnxOspfIfBDRIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 33),
    _TmnxOspfIfBDRIpAddrType_Type()
)
tmnxOspfIfBDRIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfBDRIpAddrType.setStatus("obsolete")


class _TmnxOspfIfBDRIpAddr_Type(InetAddress):
    """Custom type tmnxOspfIfBDRIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(20, 20),
    )


_TmnxOspfIfBDRIpAddr_Type.__name__ = "InetAddress"
_TmnxOspfIfBDRIpAddr_Object = MibTableColumn
tmnxOspfIfBDRIpAddr = _TmnxOspfIfBDRIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 34),
    _TmnxOspfIfBDRIpAddr_Type()
)
tmnxOspfIfBDRIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfBDRIpAddr.setStatus("obsolete")
_TmnxOspfIfLinkLsaCount_Type = Gauge32
_TmnxOspfIfLinkLsaCount_Object = MibTableColumn
tmnxOspfIfLinkLsaCount = _TmnxOspfIfLinkLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 35),
    _TmnxOspfIfLinkLsaCount_Type()
)
tmnxOspfIfLinkLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfLinkLsaCount.setStatus("obsolete")
_TmnxOspfIfLinkLsaCksumSum_Type = Integer32
_TmnxOspfIfLinkLsaCksumSum_Object = MibTableColumn
tmnxOspfIfLinkLsaCksumSum = _TmnxOspfIfLinkLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 36),
    _TmnxOspfIfLinkLsaCksumSum_Type()
)
tmnxOspfIfLinkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfLinkLsaCksumSum.setStatus("obsolete")
_TmnxOspfIfLinkUnkLsaCount_Type = Gauge32
_TmnxOspfIfLinkUnkLsaCount_Object = MibTableColumn
tmnxOspfIfLinkUnkLsaCount = _TmnxOspfIfLinkUnkLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 37),
    _TmnxOspfIfLinkUnkLsaCount_Type()
)
tmnxOspfIfLinkUnkLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfLinkUnkLsaCount.setStatus("obsolete")
_TmnxOspfIfLinkUnkLsaCksumSum_Type = Integer32
_TmnxOspfIfLinkUnkLsaCksumSum_Object = MibTableColumn
tmnxOspfIfLinkUnkLsaCksumSum = _TmnxOspfIfLinkUnkLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 38),
    _TmnxOspfIfLinkUnkLsaCksumSum_Type()
)
tmnxOspfIfLinkUnkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfLinkUnkLsaCksumSum.setStatus("obsolete")
_TmnxOspfIfMD5TransmitKeyId_Type = TmnxOspfIfMD5KeyId
_TmnxOspfIfMD5TransmitKeyId_Object = MibTableColumn
tmnxOspfIfMD5TransmitKeyId = _TmnxOspfIfMD5TransmitKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 39),
    _TmnxOspfIfMD5TransmitKeyId_Type()
)
tmnxOspfIfMD5TransmitKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfMD5TransmitKeyId.setStatus("obsolete")
_TmnxOspfIfLocalIpAddressType_Type = InetAddressType
_TmnxOspfIfLocalIpAddressType_Object = MibTableColumn
tmnxOspfIfLocalIpAddressType = _TmnxOspfIfLocalIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 40),
    _TmnxOspfIfLocalIpAddressType_Type()
)
tmnxOspfIfLocalIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfLocalIpAddressType.setStatus("obsolete")


class _TmnxOspfIfLocalIpAddress_Type(InetAddress):
    """Custom type tmnxOspfIfLocalIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(20, 20),
    )


_TmnxOspfIfLocalIpAddress_Type.__name__ = "InetAddress"
_TmnxOspfIfLocalIpAddress_Object = MibTableColumn
tmnxOspfIfLocalIpAddress = _TmnxOspfIfLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 41),
    _TmnxOspfIfLocalIpAddress_Type()
)
tmnxOspfIfLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfLocalIpAddress.setStatus("obsolete")
_TmnxOspfIfMD5NumKeys_Type = Gauge32
_TmnxOspfIfMD5NumKeys_Object = MibTableColumn
tmnxOspfIfMD5NumKeys = _TmnxOspfIfMD5NumKeys_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 42),
    _TmnxOspfIfMD5NumKeys_Type()
)
tmnxOspfIfMD5NumKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfMD5NumKeys.setStatus("obsolete")
_TmnxOspfIfType_Type = TmnxOspfIfTypeTc
_TmnxOspfIfType_Object = MibTableColumn
tmnxOspfIfType = _TmnxOspfIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 43),
    _TmnxOspfIfType_Type()
)
tmnxOspfIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfType.setStatus("obsolete")


class _TmnxOspfIfEnableBfd_Type(TruthValue):
    """Custom type tmnxOspfIfEnableBfd based on TruthValue"""
    defaultValue = 2


_TmnxOspfIfEnableBfd_Type.__name__ = "TruthValue"
_TmnxOspfIfEnableBfd_Object = MibTableColumn
tmnxOspfIfEnableBfd = _TmnxOspfIfEnableBfd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 44),
    _TmnxOspfIfEnableBfd_Type()
)
tmnxOspfIfEnableBfd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfEnableBfd.setStatus("obsolete")


class _TmnxOspfIfRemainDownOnFail_Type(TruthValue):
    """Custom type tmnxOspfIfRemainDownOnFail based on TruthValue"""
    defaultValue = 2


_TmnxOspfIfRemainDownOnFail_Type.__name__ = "TruthValue"
_TmnxOspfIfRemainDownOnFail_Object = MibTableColumn
tmnxOspfIfRemainDownOnFail = _TmnxOspfIfRemainDownOnFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 45),
    _TmnxOspfIfRemainDownOnFail_Type()
)
tmnxOspfIfRemainDownOnFail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfRemainDownOnFail.setStatus("obsolete")


class _TmnxOspfIfTeMetric_Type(Unsigned32):
    """Custom type tmnxOspfIfTeMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxOspfIfTeMetric_Type.__name__ = "Unsigned32"
_TmnxOspfIfTeMetric_Object = MibTableColumn
tmnxOspfIfTeMetric = _TmnxOspfIfTeMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 46),
    _TmnxOspfIfTeMetric_Type()
)
tmnxOspfIfTeMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfTeMetric.setStatus("obsolete")
_TmnxOspfIfTeState_Type = TmnxOperState
_TmnxOspfIfTeState_Object = MibTableColumn
tmnxOspfIfTeState = _TmnxOspfIfTeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 47),
    _TmnxOspfIfTeState_Type()
)
tmnxOspfIfTeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfTeState.setStatus("obsolete")
_TmnxOspfIfAdminGroup_Type = Unsigned32
_TmnxOspfIfAdminGroup_Object = MibTableColumn
tmnxOspfIfAdminGroup = _TmnxOspfIfAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 48),
    _TmnxOspfIfAdminGroup_Type()
)
tmnxOspfIfAdminGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfAdminGroup.setStatus("obsolete")
_TmnxOspfIfLdpSyncState_Type = TmnxOperState
_TmnxOspfIfLdpSyncState_Object = MibTableColumn
tmnxOspfIfLdpSyncState = _TmnxOspfIfLdpSyncState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 49),
    _TmnxOspfIfLdpSyncState_Type()
)
tmnxOspfIfLdpSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfLdpSyncState.setStatus("obsolete")
_TmnxOspfIfLdpSyncMaxMetric_Type = TruthValue
_TmnxOspfIfLdpSyncMaxMetric_Object = MibTableColumn
tmnxOspfIfLdpSyncMaxMetric = _TmnxOspfIfLdpSyncMaxMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 50),
    _TmnxOspfIfLdpSyncMaxMetric_Type()
)
tmnxOspfIfLdpSyncMaxMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfLdpSyncMaxMetric.setStatus("obsolete")


class _TmnxOspfIfLdpSyncTimerState_Type(Integer32):
    """Custom type tmnxOspfIfLdpSyncTimerState based on Integer32"""
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
        *(("waitForLdpAdj", 1),
          ("timerActive", 2),
          ("ldpExchgDone", 3),
          ("timerExpired", 4),
          ("manualExit", 5),
          ("disabled", 6))
    )


_TmnxOspfIfLdpSyncTimerState_Type.__name__ = "Integer32"
_TmnxOspfIfLdpSyncTimerState_Object = MibTableColumn
tmnxOspfIfLdpSyncTimerState = _TmnxOspfIfLdpSyncTimerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 51),
    _TmnxOspfIfLdpSyncTimerState_Type()
)
tmnxOspfIfLdpSyncTimerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfLdpSyncTimerState.setStatus("obsolete")


class _TmnxOspfIfLdpSyncTimeLeft_Type(Unsigned32):
    """Custom type tmnxOspfIfLdpSyncTimeLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_TmnxOspfIfLdpSyncTimeLeft_Type.__name__ = "Unsigned32"
_TmnxOspfIfLdpSyncTimeLeft_Object = MibTableColumn
tmnxOspfIfLdpSyncTimeLeft = _TmnxOspfIfLdpSyncTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 52),
    _TmnxOspfIfLdpSyncTimeLeft_Type()
)
tmnxOspfIfLdpSyncTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfLdpSyncTimeLeft.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOspfIfLdpSyncTimeLeft.setUnits("seconds")


class _TmnxOspfIfInboundSAName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfIfInboundSAName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfIfInboundSAName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfIfInboundSAName_Object = MibTableColumn
tmnxOspfIfInboundSAName = _TmnxOspfIfInboundSAName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 53),
    _TmnxOspfIfInboundSAName_Type()
)
tmnxOspfIfInboundSAName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfInboundSAName.setStatus("obsolete")


class _TmnxOspfIfOutboundSAName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfIfOutboundSAName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfIfOutboundSAName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfIfOutboundSAName_Object = MibTableColumn
tmnxOspfIfOutboundSAName = _TmnxOspfIfOutboundSAName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 54),
    _TmnxOspfIfOutboundSAName_Type()
)
tmnxOspfIfOutboundSAName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfOutboundSAName.setStatus("obsolete")


class _TmnxOspfIfOperInbSAName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfIfOperInbSAName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfIfOperInbSAName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfIfOperInbSAName_Object = MibTableColumn
tmnxOspfIfOperInbSAName = _TmnxOspfIfOperInbSAName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 55),
    _TmnxOspfIfOperInbSAName_Type()
)
tmnxOspfIfOperInbSAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfOperInbSAName.setStatus("obsolete")


class _TmnxOspfIfOperInbSANameTemp_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfIfOperInbSANameTemp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfIfOperInbSANameTemp_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfIfOperInbSANameTemp_Object = MibTableColumn
tmnxOspfIfOperInbSANameTemp = _TmnxOspfIfOperInbSANameTemp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 56),
    _TmnxOspfIfOperInbSANameTemp_Type()
)
tmnxOspfIfOperInbSANameTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfOperInbSANameTemp.setStatus("obsolete")


class _TmnxOspfIfOperOutbSAName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfIfOperOutbSAName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfIfOperOutbSAName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfIfOperOutbSAName_Object = MibTableColumn
tmnxOspfIfOperOutbSAName = _TmnxOspfIfOperOutbSAName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 12, 1, 57),
    _TmnxOspfIfOperOutbSAName_Type()
)
tmnxOspfIfOperOutbSAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfOperOutbSAName.setStatus("obsolete")
_TmnxOspfIfStatsTable_Object = MibTable
tmnxOspfIfStatsTable = _TmnxOspfIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13)
)
if mibBuilder.loadTexts:
    tmnxOspfIfStatsTable.setStatus("obsolete")
_TmnxOspfIfStatsEntry_Object = MibTableRow
tmnxOspfIfStatsEntry = _TmnxOspfIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1)
)
if mibBuilder.loadTexts:
    tmnxOspfIfStatsEntry.setStatus("obsolete")
_TmnxOspfIfEvents_Type = Counter32
_TmnxOspfIfEvents_Object = MibTableColumn
tmnxOspfIfEvents = _TmnxOspfIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 1),
    _TmnxOspfIfEvents_Type()
)
tmnxOspfIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfEvents.setStatus("obsolete")
_TmnxOspfIfTxPackets_Type = Counter32
_TmnxOspfIfTxPackets_Object = MibTableColumn
tmnxOspfIfTxPackets = _TmnxOspfIfTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 2),
    _TmnxOspfIfTxPackets_Type()
)
tmnxOspfIfTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfTxPackets.setStatus("obsolete")
_TmnxOspfIfTxHellos_Type = Counter32
_TmnxOspfIfTxHellos_Object = MibTableColumn
tmnxOspfIfTxHellos = _TmnxOspfIfTxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 3),
    _TmnxOspfIfTxHellos_Type()
)
tmnxOspfIfTxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfTxHellos.setStatus("obsolete")
_TmnxOspfIfTxDBDs_Type = Counter32
_TmnxOspfIfTxDBDs_Object = MibTableColumn
tmnxOspfIfTxDBDs = _TmnxOspfIfTxDBDs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 4),
    _TmnxOspfIfTxDBDs_Type()
)
tmnxOspfIfTxDBDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfTxDBDs.setStatus("obsolete")
_TmnxOspfIfTxLSRs_Type = Counter32
_TmnxOspfIfTxLSRs_Object = MibTableColumn
tmnxOspfIfTxLSRs = _TmnxOspfIfTxLSRs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 5),
    _TmnxOspfIfTxLSRs_Type()
)
tmnxOspfIfTxLSRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfTxLSRs.setStatus("obsolete")
_TmnxOspfIfTxLSUs_Type = Counter32
_TmnxOspfIfTxLSUs_Object = MibTableColumn
tmnxOspfIfTxLSUs = _TmnxOspfIfTxLSUs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 6),
    _TmnxOspfIfTxLSUs_Type()
)
tmnxOspfIfTxLSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfTxLSUs.setStatus("obsolete")
_TmnxOspfIfTxLSAcks_Type = Counter32
_TmnxOspfIfTxLSAcks_Object = MibTableColumn
tmnxOspfIfTxLSAcks = _TmnxOspfIfTxLSAcks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 7),
    _TmnxOspfIfTxLSAcks_Type()
)
tmnxOspfIfTxLSAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfTxLSAcks.setStatus("obsolete")
_TmnxOspfIfRxPackets_Type = Counter32
_TmnxOspfIfRxPackets_Object = MibTableColumn
tmnxOspfIfRxPackets = _TmnxOspfIfRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 8),
    _TmnxOspfIfRxPackets_Type()
)
tmnxOspfIfRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfRxPackets.setStatus("obsolete")
_TmnxOspfIfRxHellos_Type = Counter32
_TmnxOspfIfRxHellos_Object = MibTableColumn
tmnxOspfIfRxHellos = _TmnxOspfIfRxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 9),
    _TmnxOspfIfRxHellos_Type()
)
tmnxOspfIfRxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfRxHellos.setStatus("obsolete")
_TmnxOspfIfRxDBDs_Type = Counter32
_TmnxOspfIfRxDBDs_Object = MibTableColumn
tmnxOspfIfRxDBDs = _TmnxOspfIfRxDBDs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 10),
    _TmnxOspfIfRxDBDs_Type()
)
tmnxOspfIfRxDBDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfRxDBDs.setStatus("obsolete")
_TmnxOspfIfRxLSRs_Type = Counter32
_TmnxOspfIfRxLSRs_Object = MibTableColumn
tmnxOspfIfRxLSRs = _TmnxOspfIfRxLSRs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 11),
    _TmnxOspfIfRxLSRs_Type()
)
tmnxOspfIfRxLSRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfRxLSRs.setStatus("obsolete")
_TmnxOspfIfRxLSUs_Type = Counter32
_TmnxOspfIfRxLSUs_Object = MibTableColumn
tmnxOspfIfRxLSUs = _TmnxOspfIfRxLSUs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 12),
    _TmnxOspfIfRxLSUs_Type()
)
tmnxOspfIfRxLSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfRxLSUs.setStatus("obsolete")
_TmnxOspfIfRxLSAcks_Type = Counter32
_TmnxOspfIfRxLSAcks_Object = MibTableColumn
tmnxOspfIfRxLSAcks = _TmnxOspfIfRxLSAcks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 13),
    _TmnxOspfIfRxLSAcks_Type()
)
tmnxOspfIfRxLSAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfRxLSAcks.setStatus("obsolete")
_TmnxOspfIfDiscardPackets_Type = Counter32
_TmnxOspfIfDiscardPackets_Object = MibTableColumn
tmnxOspfIfDiscardPackets = _TmnxOspfIfDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 14),
    _TmnxOspfIfDiscardPackets_Type()
)
tmnxOspfIfDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfDiscardPackets.setStatus("obsolete")
_TmnxOspfIfRetransmitOuts_Type = Counter32
_TmnxOspfIfRetransmitOuts_Object = MibTableColumn
tmnxOspfIfRetransmitOuts = _TmnxOspfIfRetransmitOuts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 15),
    _TmnxOspfIfRetransmitOuts_Type()
)
tmnxOspfIfRetransmitOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfRetransmitOuts.setStatus("obsolete")
_TmnxOspfIfBadVersions_Type = Counter32
_TmnxOspfIfBadVersions_Object = MibTableColumn
tmnxOspfIfBadVersions = _TmnxOspfIfBadVersions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 16),
    _TmnxOspfIfBadVersions_Type()
)
tmnxOspfIfBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfBadVersions.setStatus("obsolete")
_TmnxOspfIfBadNetworks_Type = Counter32
_TmnxOspfIfBadNetworks_Object = MibTableColumn
tmnxOspfIfBadNetworks = _TmnxOspfIfBadNetworks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 17),
    _TmnxOspfIfBadNetworks_Type()
)
tmnxOspfIfBadNetworks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfBadNetworks.setStatus("obsolete")
_TmnxOspfIfBadVirtualLinks_Type = Counter32
_TmnxOspfIfBadVirtualLinks_Object = MibTableColumn
tmnxOspfIfBadVirtualLinks = _TmnxOspfIfBadVirtualLinks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 18),
    _TmnxOspfIfBadVirtualLinks_Type()
)
tmnxOspfIfBadVirtualLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfBadVirtualLinks.setStatus("obsolete")
_TmnxOspfIfBadAreas_Type = Counter32
_TmnxOspfIfBadAreas_Object = MibTableColumn
tmnxOspfIfBadAreas = _TmnxOspfIfBadAreas_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 19),
    _TmnxOspfIfBadAreas_Type()
)
tmnxOspfIfBadAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfBadAreas.setStatus("obsolete")
_TmnxOspfIfBadDstAddrs_Type = Counter32
_TmnxOspfIfBadDstAddrs_Object = MibTableColumn
tmnxOspfIfBadDstAddrs = _TmnxOspfIfBadDstAddrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 20),
    _TmnxOspfIfBadDstAddrs_Type()
)
tmnxOspfIfBadDstAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfBadDstAddrs.setStatus("obsolete")
_TmnxOspfIfBadNeighbors_Type = Counter32
_TmnxOspfIfBadNeighbors_Object = MibTableColumn
tmnxOspfIfBadNeighbors = _TmnxOspfIfBadNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 21),
    _TmnxOspfIfBadNeighbors_Type()
)
tmnxOspfIfBadNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfBadNeighbors.setStatus("obsolete")
_TmnxOspfIfBadPacketTypes_Type = Counter32
_TmnxOspfIfBadPacketTypes_Object = MibTableColumn
tmnxOspfIfBadPacketTypes = _TmnxOspfIfBadPacketTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 22),
    _TmnxOspfIfBadPacketTypes_Type()
)
tmnxOspfIfBadPacketTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfBadPacketTypes.setStatus("obsolete")
_TmnxOspfIfNeighborCount_Type = Integer32
_TmnxOspfIfNeighborCount_Object = MibTableColumn
tmnxOspfIfNeighborCount = _TmnxOspfIfNeighborCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 23),
    _TmnxOspfIfNeighborCount_Type()
)
tmnxOspfIfNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfNeighborCount.setStatus("obsolete")
_TmnxOspfIfLastEventTime_Type = TimeStamp
_TmnxOspfIfLastEventTime_Object = MibTableColumn
tmnxOspfIfLastEventTime = _TmnxOspfIfLastEventTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 24),
    _TmnxOspfIfLastEventTime_Type()
)
tmnxOspfIfLastEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfLastEventTime.setStatus("obsolete")
_TmnxOspfIfBadLengths_Type = Counter32
_TmnxOspfIfBadLengths_Object = MibTableColumn
tmnxOspfIfBadLengths = _TmnxOspfIfBadLengths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 25),
    _TmnxOspfIfBadLengths_Type()
)
tmnxOspfIfBadLengths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfBadLengths.setStatus("obsolete")
_TmnxOspfIfBadHelloIntervals_Type = Counter32
_TmnxOspfIfBadHelloIntervals_Object = MibTableColumn
tmnxOspfIfBadHelloIntervals = _TmnxOspfIfBadHelloIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 26),
    _TmnxOspfIfBadHelloIntervals_Type()
)
tmnxOspfIfBadHelloIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfBadHelloIntervals.setStatus("obsolete")
_TmnxOspfIfBadDeadIntervals_Type = Counter32
_TmnxOspfIfBadDeadIntervals_Object = MibTableColumn
tmnxOspfIfBadDeadIntervals = _TmnxOspfIfBadDeadIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 27),
    _TmnxOspfIfBadDeadIntervals_Type()
)
tmnxOspfIfBadDeadIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfBadDeadIntervals.setStatus("obsolete")
_TmnxOspfIfBadOptions_Type = Counter32
_TmnxOspfIfBadOptions_Object = MibTableColumn
tmnxOspfIfBadOptions = _TmnxOspfIfBadOptions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 28),
    _TmnxOspfIfBadOptions_Type()
)
tmnxOspfIfBadOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfBadOptions.setStatus("obsolete")
_TmnxOspfIfRxBadChecksums_Type = Counter32
_TmnxOspfIfRxBadChecksums_Object = MibTableColumn
tmnxOspfIfRxBadChecksums = _TmnxOspfIfRxBadChecksums_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 29),
    _TmnxOspfIfRxBadChecksums_Type()
)
tmnxOspfIfRxBadChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfRxBadChecksums.setStatus("obsolete")
_TmnxOspfIfBadAuthTypes_Type = Counter32
_TmnxOspfIfBadAuthTypes_Object = MibTableColumn
tmnxOspfIfBadAuthTypes = _TmnxOspfIfBadAuthTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 30),
    _TmnxOspfIfBadAuthTypes_Type()
)
tmnxOspfIfBadAuthTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfBadAuthTypes.setStatus("obsolete")
_TmnxOspfIfAuthFailures_Type = Counter32
_TmnxOspfIfAuthFailures_Object = MibTableColumn
tmnxOspfIfAuthFailures = _TmnxOspfIfAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 13, 1, 31),
    _TmnxOspfIfAuthFailures_Type()
)
tmnxOspfIfAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfAuthFailures.setStatus("obsolete")
_TmnxOspfVirtIfTable_Object = MibTable
tmnxOspfVirtIfTable = _TmnxOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14)
)
if mibBuilder.loadTexts:
    tmnxOspfVirtIfTable.setStatus("current")
_TmnxOspfVirtIfEntry_Object = MibTableRow
tmnxOspfVirtIfEntry = _TmnxOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1)
)
tmnxOspfVirtIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfAreaId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    tmnxOspfVirtIfEntry.setStatus("current")
_TmnxOspfVirtIfAreaId_Type = TmnxOspfAreaIdTc
_TmnxOspfVirtIfAreaId_Object = MibTableColumn
tmnxOspfVirtIfAreaId = _TmnxOspfVirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 1),
    _TmnxOspfVirtIfAreaId_Type()
)
tmnxOspfVirtIfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfAreaId.setStatus("current")
_TmnxOspfVirtIfNeighbor_Type = TmnxOspfRouterIdTc
_TmnxOspfVirtIfNeighbor_Object = MibTableColumn
tmnxOspfVirtIfNeighbor = _TmnxOspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 2),
    _TmnxOspfVirtIfNeighbor_Type()
)
tmnxOspfVirtIfNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfNeighbor.setStatus("current")
_TmnxOspfVirtIfStatus_Type = RowStatus
_TmnxOspfVirtIfStatus_Object = MibTableColumn
tmnxOspfVirtIfStatus = _TmnxOspfVirtIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 3),
    _TmnxOspfVirtIfStatus_Type()
)
tmnxOspfVirtIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfStatus.setStatus("current")
_TmnxOspfVirtIfLastChanged_Type = TimeStamp
_TmnxOspfVirtIfLastChanged_Object = MibTableColumn
tmnxOspfVirtIfLastChanged = _TmnxOspfVirtIfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 4),
    _TmnxOspfVirtIfLastChanged_Type()
)
tmnxOspfVirtIfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfLastChanged.setStatus("current")
_TmnxOspfVirtIfIndex_Type = InterfaceIndex
_TmnxOspfVirtIfIndex_Object = MibTableColumn
tmnxOspfVirtIfIndex = _TmnxOspfVirtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 5),
    _TmnxOspfVirtIfIndex_Type()
)
tmnxOspfVirtIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfIndex.setStatus("current")


class _TmnxOspfVirtIfInstId_Type(TmnxOspfIfInstIdTc):
    """Custom type tmnxOspfVirtIfInstId based on TmnxOspfIfInstIdTc"""
    defaultValue = 0


_TmnxOspfVirtIfInstId_Type.__name__ = "TmnxOspfIfInstIdTc"
_TmnxOspfVirtIfInstId_Object = MibTableColumn
tmnxOspfVirtIfInstId = _TmnxOspfVirtIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 6),
    _TmnxOspfVirtIfInstId_Type()
)
tmnxOspfVirtIfInstId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfInstId.setStatus("current")


class _TmnxOspfVirtIfAdminStat_Type(Status):
    """Custom type tmnxOspfVirtIfAdminStat based on Status"""
    defaultValue = 2


_TmnxOspfVirtIfAdminStat_Type.__name__ = "Status"
_TmnxOspfVirtIfAdminStat_Object = MibTableColumn
tmnxOspfVirtIfAdminStat = _TmnxOspfVirtIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 7),
    _TmnxOspfVirtIfAdminStat_Type()
)
tmnxOspfVirtIfAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfAdminStat.setStatus("current")


class _TmnxOspfVirtIfTransitDelay_Type(TmnxOspfUpToRefreshIntervalTc):
    """Custom type tmnxOspfVirtIfTransitDelay based on TmnxOspfUpToRefreshIntervalTc"""
    defaultValue = 1

    subtypeSpec = TmnxOspfUpToRefreshIntervalTc.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_TmnxOspfVirtIfTransitDelay_Type.__name__ = "TmnxOspfUpToRefreshIntervalTc"
_TmnxOspfVirtIfTransitDelay_Object = MibTableColumn
tmnxOspfVirtIfTransitDelay = _TmnxOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 8),
    _TmnxOspfVirtIfTransitDelay_Type()
)
tmnxOspfVirtIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfTransitDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfTransitDelay.setUnits("seconds")


class _TmnxOspfVirtIfRetransInterval_Type(TmnxOspfUpToRefreshIntervalTc):
    """Custom type tmnxOspfVirtIfRetransInterval based on TmnxOspfUpToRefreshIntervalTc"""
    defaultValue = 5

    subtypeSpec = TmnxOspfUpToRefreshIntervalTc.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_TmnxOspfVirtIfRetransInterval_Type.__name__ = "TmnxOspfUpToRefreshIntervalTc"
_TmnxOspfVirtIfRetransInterval_Object = MibTableColumn
tmnxOspfVirtIfRetransInterval = _TmnxOspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 9),
    _TmnxOspfVirtIfRetransInterval_Type()
)
tmnxOspfVirtIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfRetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfRetransInterval.setUnits("seconds")


class _TmnxOspfVirtIfHelloInterval_Type(HelloRange):
    """Custom type tmnxOspfVirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_TmnxOspfVirtIfHelloInterval_Type.__name__ = "HelloRange"
_TmnxOspfVirtIfHelloInterval_Object = MibTableColumn
tmnxOspfVirtIfHelloInterval = _TmnxOspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 10),
    _TmnxOspfVirtIfHelloInterval_Type()
)
tmnxOspfVirtIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfHelloInterval.setUnits("seconds")


class _TmnxOspfVirtIfRtrDeadInterval_Type(TmnxOspfDeadIntRangeTc):
    """Custom type tmnxOspfVirtIfRtrDeadInterval based on TmnxOspfDeadIntRangeTc"""
    defaultValue = 60


_TmnxOspfVirtIfRtrDeadInterval_Type.__name__ = "TmnxOspfDeadIntRangeTc"
_TmnxOspfVirtIfRtrDeadInterval_Object = MibTableColumn
tmnxOspfVirtIfRtrDeadInterval = _TmnxOspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 11),
    _TmnxOspfVirtIfRtrDeadInterval_Type()
)
tmnxOspfVirtIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfRtrDeadInterval.setUnits("seconds")


class _TmnxOspfVirtIfAuthType_Type(TmnxOspfAuthenticationType):
    """Custom type tmnxOspfVirtIfAuthType based on TmnxOspfAuthenticationType"""
    defaultValue = 0


_TmnxOspfVirtIfAuthType_Type.__name__ = "TmnxOspfAuthenticationType"
_TmnxOspfVirtIfAuthType_Object = MibTableColumn
tmnxOspfVirtIfAuthType = _TmnxOspfVirtIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 12),
    _TmnxOspfVirtIfAuthType_Type()
)
tmnxOspfVirtIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfAuthType.setStatus("current")


class _TmnxOspfVirtIfAuthKey_Type(OctetString):
    """Custom type tmnxOspfVirtIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TmnxOspfVirtIfAuthKey_Type.__name__ = "OctetString"
_TmnxOspfVirtIfAuthKey_Object = MibTableColumn
tmnxOspfVirtIfAuthKey = _TmnxOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 13),
    _TmnxOspfVirtIfAuthKey_Type()
)
tmnxOspfVirtIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfAuthKey.setStatus("current")


class _TmnxOspfVirtIfState_Type(Integer32):
    """Custom type tmnxOspfVirtIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("pointToPoint", 4))
    )


_TmnxOspfVirtIfState_Type.__name__ = "Integer32"
_TmnxOspfVirtIfState_Object = MibTableColumn
tmnxOspfVirtIfState = _TmnxOspfVirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 14),
    _TmnxOspfVirtIfState_Type()
)
tmnxOspfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfState.setStatus("current")
_TmnxOspfVirtIfLastEnabledTime_Type = TimeStamp
_TmnxOspfVirtIfLastEnabledTime_Object = MibTableColumn
tmnxOspfVirtIfLastEnabledTime = _TmnxOspfVirtIfLastEnabledTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 15),
    _TmnxOspfVirtIfLastEnabledTime_Type()
)
tmnxOspfVirtIfLastEnabledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfLastEnabledTime.setStatus("current")
_TmnxOspfVirtIfCost_Type = Metric
_TmnxOspfVirtIfCost_Object = MibTableColumn
tmnxOspfVirtIfCost = _TmnxOspfVirtIfCost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 16),
    _TmnxOspfVirtIfCost_Type()
)
tmnxOspfVirtIfCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfCost.setStatus("current")
_TmnxOspfVirtIfLinkLsaCount_Type = Gauge32
_TmnxOspfVirtIfLinkLsaCount_Object = MibTableColumn
tmnxOspfVirtIfLinkLsaCount = _TmnxOspfVirtIfLinkLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 17),
    _TmnxOspfVirtIfLinkLsaCount_Type()
)
tmnxOspfVirtIfLinkLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfLinkLsaCount.setStatus("current")
_TmnxOspfVirtIfLinkLsaCksumSum_Type = Integer32
_TmnxOspfVirtIfLinkLsaCksumSum_Object = MibTableColumn
tmnxOspfVirtIfLinkLsaCksumSum = _TmnxOspfVirtIfLinkLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 18),
    _TmnxOspfVirtIfLinkLsaCksumSum_Type()
)
tmnxOspfVirtIfLinkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfLinkLsaCksumSum.setStatus("current")
_TmnxOspfVirtIfLinkUnkLsaCount_Type = Gauge32
_TmnxOspfVirtIfLinkUnkLsaCount_Object = MibTableColumn
tmnxOspfVirtIfLinkUnkLsaCount = _TmnxOspfVirtIfLinkUnkLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 19),
    _TmnxOspfVirtIfLinkUnkLsaCount_Type()
)
tmnxOspfVirtIfLinkUnkLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfLinkUnkLsaCount.setStatus("current")
_TmnxOspfVirtIfLinkUnkLsaCksumSum_Type = Integer32
_TmnxOspfVirtIfLinkUnkLsaCksumSum_Object = MibTableColumn
tmnxOspfVirtIfLinkUnkLsaCksumSum = _TmnxOspfVirtIfLinkUnkLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 20),
    _TmnxOspfVirtIfLinkUnkLsaCksumSum_Type()
)
tmnxOspfVirtIfLinkUnkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfLinkUnkLsaCksumSum.setStatus("current")
_TmnxOspfVirtIfMD5TransmitKeyId_Type = TmnxOspfIfMD5KeyId
_TmnxOspfVirtIfMD5TransmitKeyId_Object = MibTableColumn
tmnxOspfVirtIfMD5TransmitKeyId = _TmnxOspfVirtIfMD5TransmitKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 21),
    _TmnxOspfVirtIfMD5TransmitKeyId_Type()
)
tmnxOspfVirtIfMD5TransmitKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfMD5TransmitKeyId.setStatus("current")
_TmnxOspfVirtIfLocalIpAddrType_Type = InetAddressType
_TmnxOspfVirtIfLocalIpAddrType_Object = MibTableColumn
tmnxOspfVirtIfLocalIpAddrType = _TmnxOspfVirtIfLocalIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 22),
    _TmnxOspfVirtIfLocalIpAddrType_Type()
)
tmnxOspfVirtIfLocalIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfLocalIpAddrType.setStatus("current")


class _TmnxOspfVirtIfLocalIpAddress_Type(InetAddress):
    """Custom type tmnxOspfVirtIfLocalIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOspfVirtIfLocalIpAddress_Type.__name__ = "InetAddress"
_TmnxOspfVirtIfLocalIpAddress_Object = MibTableColumn
tmnxOspfVirtIfLocalIpAddress = _TmnxOspfVirtIfLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 23),
    _TmnxOspfVirtIfLocalIpAddress_Type()
)
tmnxOspfVirtIfLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfLocalIpAddress.setStatus("current")
_TmnxOspfVirtIfMD5NumKeys_Type = Gauge32
_TmnxOspfVirtIfMD5NumKeys_Object = MibTableColumn
tmnxOspfVirtIfMD5NumKeys = _TmnxOspfVirtIfMD5NumKeys_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 24),
    _TmnxOspfVirtIfMD5NumKeys_Type()
)
tmnxOspfVirtIfMD5NumKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfMD5NumKeys.setStatus("current")


class _TmnxOspfVirtIfInboundSAName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfVirtIfInboundSAName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfVirtIfInboundSAName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfVirtIfInboundSAName_Object = MibTableColumn
tmnxOspfVirtIfInboundSAName = _TmnxOspfVirtIfInboundSAName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 25),
    _TmnxOspfVirtIfInboundSAName_Type()
)
tmnxOspfVirtIfInboundSAName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfInboundSAName.setStatus("current")


class _TmnxOspfVirtIfOutboundSAName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfVirtIfOutboundSAName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfVirtIfOutboundSAName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfVirtIfOutboundSAName_Object = MibTableColumn
tmnxOspfVirtIfOutboundSAName = _TmnxOspfVirtIfOutboundSAName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 26),
    _TmnxOspfVirtIfOutboundSAName_Type()
)
tmnxOspfVirtIfOutboundSAName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfOutboundSAName.setStatus("current")


class _TmnxOspfVirtIfOperInbSAName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfVirtIfOperInbSAName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfVirtIfOperInbSAName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfVirtIfOperInbSAName_Object = MibTableColumn
tmnxOspfVirtIfOperInbSAName = _TmnxOspfVirtIfOperInbSAName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 27),
    _TmnxOspfVirtIfOperInbSAName_Type()
)
tmnxOspfVirtIfOperInbSAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfOperInbSAName.setStatus("current")


class _TmnxOspfVirtIfOperInbSANameTemp_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfVirtIfOperInbSANameTemp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfVirtIfOperInbSANameTemp_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfVirtIfOperInbSANameTemp_Object = MibTableColumn
tmnxOspfVirtIfOperInbSANameTemp = _TmnxOspfVirtIfOperInbSANameTemp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 28),
    _TmnxOspfVirtIfOperInbSANameTemp_Type()
)
tmnxOspfVirtIfOperInbSANameTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfOperInbSANameTemp.setStatus("current")


class _TmnxOspfVirtIfOperOutbSAName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfVirtIfOperOutbSAName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfVirtIfOperOutbSAName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfVirtIfOperOutbSAName_Object = MibTableColumn
tmnxOspfVirtIfOperOutbSAName = _TmnxOspfVirtIfOperOutbSAName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 29),
    _TmnxOspfVirtIfOperOutbSAName_Type()
)
tmnxOspfVirtIfOperOutbSAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfOperOutbSAName.setStatus("current")


class _TmnxOspfVirtIfAuthKeyChain_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfVirtIfAuthKeyChain based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfVirtIfAuthKeyChain_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfVirtIfAuthKeyChain_Object = MibTableColumn
tmnxOspfVirtIfAuthKeyChain = _TmnxOspfVirtIfAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 14, 1, 30),
    _TmnxOspfVirtIfAuthKeyChain_Type()
)
tmnxOspfVirtIfAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfAuthKeyChain.setStatus("current")
_TmnxOspfVirtIfStatsTable_Object = MibTable
tmnxOspfVirtIfStatsTable = _TmnxOspfVirtIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15)
)
if mibBuilder.loadTexts:
    tmnxOspfVirtIfStatsTable.setStatus("current")
_TmnxOspfVirtIfStatsEntry_Object = MibTableRow
tmnxOspfVirtIfStatsEntry = _TmnxOspfVirtIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1)
)
if mibBuilder.loadTexts:
    tmnxOspfVirtIfStatsEntry.setStatus("current")
_TmnxOspfVirtIfEvents_Type = Counter32
_TmnxOspfVirtIfEvents_Object = MibTableColumn
tmnxOspfVirtIfEvents = _TmnxOspfVirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 1),
    _TmnxOspfVirtIfEvents_Type()
)
tmnxOspfVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfEvents.setStatus("current")
_TmnxOspfVirtIfTxPackets_Type = Counter32
_TmnxOspfVirtIfTxPackets_Object = MibTableColumn
tmnxOspfVirtIfTxPackets = _TmnxOspfVirtIfTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 2),
    _TmnxOspfVirtIfTxPackets_Type()
)
tmnxOspfVirtIfTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfTxPackets.setStatus("current")
_TmnxOspfVirtIfTxHellos_Type = Counter32
_TmnxOspfVirtIfTxHellos_Object = MibTableColumn
tmnxOspfVirtIfTxHellos = _TmnxOspfVirtIfTxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 3),
    _TmnxOspfVirtIfTxHellos_Type()
)
tmnxOspfVirtIfTxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfTxHellos.setStatus("current")
_TmnxOspfVirtIfTxDBDs_Type = Counter32
_TmnxOspfVirtIfTxDBDs_Object = MibTableColumn
tmnxOspfVirtIfTxDBDs = _TmnxOspfVirtIfTxDBDs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 4),
    _TmnxOspfVirtIfTxDBDs_Type()
)
tmnxOspfVirtIfTxDBDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfTxDBDs.setStatus("current")
_TmnxOspfVirtIfTxLSRs_Type = Counter32
_TmnxOspfVirtIfTxLSRs_Object = MibTableColumn
tmnxOspfVirtIfTxLSRs = _TmnxOspfVirtIfTxLSRs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 5),
    _TmnxOspfVirtIfTxLSRs_Type()
)
tmnxOspfVirtIfTxLSRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfTxLSRs.setStatus("current")
_TmnxOspfVirtIfTxLSUs_Type = Counter32
_TmnxOspfVirtIfTxLSUs_Object = MibTableColumn
tmnxOspfVirtIfTxLSUs = _TmnxOspfVirtIfTxLSUs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 6),
    _TmnxOspfVirtIfTxLSUs_Type()
)
tmnxOspfVirtIfTxLSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfTxLSUs.setStatus("current")
_TmnxOspfVirtIfTxLSAcks_Type = Counter32
_TmnxOspfVirtIfTxLSAcks_Object = MibTableColumn
tmnxOspfVirtIfTxLSAcks = _TmnxOspfVirtIfTxLSAcks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 7),
    _TmnxOspfVirtIfTxLSAcks_Type()
)
tmnxOspfVirtIfTxLSAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfTxLSAcks.setStatus("current")
_TmnxOspfVirtIfRxPackets_Type = Counter32
_TmnxOspfVirtIfRxPackets_Object = MibTableColumn
tmnxOspfVirtIfRxPackets = _TmnxOspfVirtIfRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 8),
    _TmnxOspfVirtIfRxPackets_Type()
)
tmnxOspfVirtIfRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfRxPackets.setStatus("current")
_TmnxOspfVirtIfRxHellos_Type = Counter32
_TmnxOspfVirtIfRxHellos_Object = MibTableColumn
tmnxOspfVirtIfRxHellos = _TmnxOspfVirtIfRxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 9),
    _TmnxOspfVirtIfRxHellos_Type()
)
tmnxOspfVirtIfRxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfRxHellos.setStatus("current")
_TmnxOspfVirtIfRxDBDs_Type = Counter32
_TmnxOspfVirtIfRxDBDs_Object = MibTableColumn
tmnxOspfVirtIfRxDBDs = _TmnxOspfVirtIfRxDBDs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 10),
    _TmnxOspfVirtIfRxDBDs_Type()
)
tmnxOspfVirtIfRxDBDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfRxDBDs.setStatus("current")
_TmnxOspfVirtIfRxLSRs_Type = Counter32
_TmnxOspfVirtIfRxLSRs_Object = MibTableColumn
tmnxOspfVirtIfRxLSRs = _TmnxOspfVirtIfRxLSRs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 11),
    _TmnxOspfVirtIfRxLSRs_Type()
)
tmnxOspfVirtIfRxLSRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfRxLSRs.setStatus("current")
_TmnxOspfVirtIfRxLSUs_Type = Counter32
_TmnxOspfVirtIfRxLSUs_Object = MibTableColumn
tmnxOspfVirtIfRxLSUs = _TmnxOspfVirtIfRxLSUs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 12),
    _TmnxOspfVirtIfRxLSUs_Type()
)
tmnxOspfVirtIfRxLSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfRxLSUs.setStatus("current")
_TmnxOspfVirtIfRxLSAcks_Type = Counter32
_TmnxOspfVirtIfRxLSAcks_Object = MibTableColumn
tmnxOspfVirtIfRxLSAcks = _TmnxOspfVirtIfRxLSAcks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 13),
    _TmnxOspfVirtIfRxLSAcks_Type()
)
tmnxOspfVirtIfRxLSAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfRxLSAcks.setStatus("current")
_TmnxOspfVirtIfDiscardPackets_Type = Counter32
_TmnxOspfVirtIfDiscardPackets_Object = MibTableColumn
tmnxOspfVirtIfDiscardPackets = _TmnxOspfVirtIfDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 14),
    _TmnxOspfVirtIfDiscardPackets_Type()
)
tmnxOspfVirtIfDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfDiscardPackets.setStatus("current")
_TmnxOspfVirtIfRetransmitOuts_Type = Counter32
_TmnxOspfVirtIfRetransmitOuts_Object = MibTableColumn
tmnxOspfVirtIfRetransmitOuts = _TmnxOspfVirtIfRetransmitOuts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 15),
    _TmnxOspfVirtIfRetransmitOuts_Type()
)
tmnxOspfVirtIfRetransmitOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfRetransmitOuts.setStatus("current")
_TmnxOspfVirtIfBadVersions_Type = Counter32
_TmnxOspfVirtIfBadVersions_Object = MibTableColumn
tmnxOspfVirtIfBadVersions = _TmnxOspfVirtIfBadVersions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 16),
    _TmnxOspfVirtIfBadVersions_Type()
)
tmnxOspfVirtIfBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfBadVersions.setStatus("current")
_TmnxOspfVirtIfBadNetworks_Type = Counter32
_TmnxOspfVirtIfBadNetworks_Object = MibTableColumn
tmnxOspfVirtIfBadNetworks = _TmnxOspfVirtIfBadNetworks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 17),
    _TmnxOspfVirtIfBadNetworks_Type()
)
tmnxOspfVirtIfBadNetworks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfBadNetworks.setStatus("current")
_TmnxOspfVirtIfBadAreas_Type = Counter32
_TmnxOspfVirtIfBadAreas_Object = MibTableColumn
tmnxOspfVirtIfBadAreas = _TmnxOspfVirtIfBadAreas_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 18),
    _TmnxOspfVirtIfBadAreas_Type()
)
tmnxOspfVirtIfBadAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfBadAreas.setStatus("current")
_TmnxOspfVirtIfBadDstAddrs_Type = Counter32
_TmnxOspfVirtIfBadDstAddrs_Object = MibTableColumn
tmnxOspfVirtIfBadDstAddrs = _TmnxOspfVirtIfBadDstAddrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 19),
    _TmnxOspfVirtIfBadDstAddrs_Type()
)
tmnxOspfVirtIfBadDstAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfBadDstAddrs.setStatus("current")
_TmnxOspfVirtIfBadNeighbors_Type = Counter32
_TmnxOspfVirtIfBadNeighbors_Object = MibTableColumn
tmnxOspfVirtIfBadNeighbors = _TmnxOspfVirtIfBadNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 20),
    _TmnxOspfVirtIfBadNeighbors_Type()
)
tmnxOspfVirtIfBadNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfBadNeighbors.setStatus("current")
_TmnxOspfVirtIfBadPacketTypes_Type = Counter32
_TmnxOspfVirtIfBadPacketTypes_Object = MibTableColumn
tmnxOspfVirtIfBadPacketTypes = _TmnxOspfVirtIfBadPacketTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 21),
    _TmnxOspfVirtIfBadPacketTypes_Type()
)
tmnxOspfVirtIfBadPacketTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfBadPacketTypes.setStatus("current")
_TmnxOspfVirtIfLastEventTime_Type = TimeStamp
_TmnxOspfVirtIfLastEventTime_Object = MibTableColumn
tmnxOspfVirtIfLastEventTime = _TmnxOspfVirtIfLastEventTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 22),
    _TmnxOspfVirtIfLastEventTime_Type()
)
tmnxOspfVirtIfLastEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfLastEventTime.setStatus("current")
_TmnxOspfVirtIfBadLengths_Type = Counter32
_TmnxOspfVirtIfBadLengths_Object = MibTableColumn
tmnxOspfVirtIfBadLengths = _TmnxOspfVirtIfBadLengths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 23),
    _TmnxOspfVirtIfBadLengths_Type()
)
tmnxOspfVirtIfBadLengths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfBadLengths.setStatus("current")
_TmnxOspfVirtIfBadHelloIntervls_Type = Counter32
_TmnxOspfVirtIfBadHelloIntervls_Object = MibTableColumn
tmnxOspfVirtIfBadHelloIntervls = _TmnxOspfVirtIfBadHelloIntervls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 24),
    _TmnxOspfVirtIfBadHelloIntervls_Type()
)
tmnxOspfVirtIfBadHelloIntervls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfBadHelloIntervls.setStatus("current")
_TmnxOspfVirtIfBadDeadIntervals_Type = Counter32
_TmnxOspfVirtIfBadDeadIntervals_Object = MibTableColumn
tmnxOspfVirtIfBadDeadIntervals = _TmnxOspfVirtIfBadDeadIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 25),
    _TmnxOspfVirtIfBadDeadIntervals_Type()
)
tmnxOspfVirtIfBadDeadIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfBadDeadIntervals.setStatus("current")
_TmnxOspfVirtIfBadOptions_Type = Counter32
_TmnxOspfVirtIfBadOptions_Object = MibTableColumn
tmnxOspfVirtIfBadOptions = _TmnxOspfVirtIfBadOptions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 26),
    _TmnxOspfVirtIfBadOptions_Type()
)
tmnxOspfVirtIfBadOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfBadOptions.setStatus("current")
_TmnxOspfVirtIfRxBadChecksums_Type = Counter32
_TmnxOspfVirtIfRxBadChecksums_Object = MibTableColumn
tmnxOspfVirtIfRxBadChecksums = _TmnxOspfVirtIfRxBadChecksums_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 27),
    _TmnxOspfVirtIfRxBadChecksums_Type()
)
tmnxOspfVirtIfRxBadChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfRxBadChecksums.setStatus("current")
_TmnxOspfVirtIfBadAuthTypes_Type = Counter32
_TmnxOspfVirtIfBadAuthTypes_Object = MibTableColumn
tmnxOspfVirtIfBadAuthTypes = _TmnxOspfVirtIfBadAuthTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 28),
    _TmnxOspfVirtIfBadAuthTypes_Type()
)
tmnxOspfVirtIfBadAuthTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfBadAuthTypes.setStatus("current")
_TmnxOspfVirtIfAuthFailures_Type = Counter32
_TmnxOspfVirtIfAuthFailures_Object = MibTableColumn
tmnxOspfVirtIfAuthFailures = _TmnxOspfVirtIfAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 29),
    _TmnxOspfVirtIfAuthFailures_Type()
)
tmnxOspfVirtIfAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfAuthFailures.setStatus("current")
_TmnxOspfVirtIfTxFailures_Type = Counter32
_TmnxOspfVirtIfTxFailures_Object = MibTableColumn
tmnxOspfVirtIfTxFailures = _TmnxOspfVirtIfTxFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 15, 1, 30),
    _TmnxOspfVirtIfTxFailures_Type()
)
tmnxOspfVirtIfTxFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfTxFailures.setStatus("current")
_TmnxOspfNbrTable_Object = MibTable
tmnxOspfNbrTable = _TmnxOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16)
)
if mibBuilder.loadTexts:
    tmnxOspfNbrTable.setStatus("obsolete")
_TmnxOspfNbrEntry_Object = MibTableRow
tmnxOspfNbrEntry = _TmnxOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1)
)
tmnxOspfNbrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrIfIndex"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrIfInstId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrRtrId"),
)
if mibBuilder.loadTexts:
    tmnxOspfNbrEntry.setStatus("obsolete")
_TmnxOspfNbrIfIndex_Type = InterfaceIndex
_TmnxOspfNbrIfIndex_Object = MibTableColumn
tmnxOspfNbrIfIndex = _TmnxOspfNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 1),
    _TmnxOspfNbrIfIndex_Type()
)
tmnxOspfNbrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfNbrIfIndex.setStatus("obsolete")
_TmnxOspfNbrIfInstId_Type = TmnxOspfIfInstIdTc
_TmnxOspfNbrIfInstId_Object = MibTableColumn
tmnxOspfNbrIfInstId = _TmnxOspfNbrIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 2),
    _TmnxOspfNbrIfInstId_Type()
)
tmnxOspfNbrIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfNbrIfInstId.setStatus("obsolete")
_TmnxOspfNbrRtrId_Type = TmnxOspfRouterIdTc
_TmnxOspfNbrRtrId_Object = MibTableColumn
tmnxOspfNbrRtrId = _TmnxOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 3),
    _TmnxOspfNbrRtrId_Type()
)
tmnxOspfNbrRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfNbrRtrId.setStatus("obsolete")
_TmnxOspfNbrAddressType_Type = InetAddressType
_TmnxOspfNbrAddressType_Object = MibTableColumn
tmnxOspfNbrAddressType = _TmnxOspfNbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 4),
    _TmnxOspfNbrAddressType_Type()
)
tmnxOspfNbrAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrAddressType.setStatus("obsolete")


class _TmnxOspfNbrAddress_Type(InetAddress):
    """Custom type tmnxOspfNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(20, 20),
    )


_TmnxOspfNbrAddress_Type.__name__ = "InetAddress"
_TmnxOspfNbrAddress_Object = MibTableColumn
tmnxOspfNbrAddress = _TmnxOspfNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 5),
    _TmnxOspfNbrAddress_Type()
)
tmnxOspfNbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrAddress.setStatus("obsolete")
_TmnxOspfNbrOptions_Type = Integer32
_TmnxOspfNbrOptions_Object = MibTableColumn
tmnxOspfNbrOptions = _TmnxOspfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 6),
    _TmnxOspfNbrOptions_Type()
)
tmnxOspfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrOptions.setStatus("obsolete")
_TmnxOspfNbrPriority_Type = DesignatedRouterPriority
_TmnxOspfNbrPriority_Object = MibTableColumn
tmnxOspfNbrPriority = _TmnxOspfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 7),
    _TmnxOspfNbrPriority_Type()
)
tmnxOspfNbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrPriority.setStatus("obsolete")


class _TmnxOspfNbrState_Type(Integer32):
    """Custom type tmnxOspfNbrState based on Integer32"""
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
        *(("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exchangeStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_TmnxOspfNbrState_Type.__name__ = "Integer32"
_TmnxOspfNbrState_Object = MibTableColumn
tmnxOspfNbrState = _TmnxOspfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 8),
    _TmnxOspfNbrState_Type()
)
tmnxOspfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrState.setStatus("obsolete")
_TmnxOspfNbrHelloSuppressed_Type = TruthValue
_TmnxOspfNbrHelloSuppressed_Object = MibTableColumn
tmnxOspfNbrHelloSuppressed = _TmnxOspfNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 9),
    _TmnxOspfNbrHelloSuppressed_Type()
)
tmnxOspfNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrHelloSuppressed.setStatus("obsolete")
_TmnxOspfNbrIfId_Type = InterfaceIndexOrZero
_TmnxOspfNbrIfId_Object = MibTableColumn
tmnxOspfNbrIfId = _TmnxOspfNbrIfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 10),
    _TmnxOspfNbrIfId_Type()
)
tmnxOspfNbrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrIfId.setStatus("obsolete")


class _TmnxOspfNbrRestartHelperStatus_Type(Integer32):
    """Custom type tmnxOspfNbrRestartHelperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notHelping", 1),
          ("helping", 2))
    )


_TmnxOspfNbrRestartHelperStatus_Type.__name__ = "Integer32"
_TmnxOspfNbrRestartHelperStatus_Object = MibTableColumn
tmnxOspfNbrRestartHelperStatus = _TmnxOspfNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 11),
    _TmnxOspfNbrRestartHelperStatus_Type()
)
tmnxOspfNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrRestartHelperStatus.setStatus("obsolete")
_TmnxOspfNbrRestartHelperAge_Type = TmnxOspfUpToRefreshIntervalTc
_TmnxOspfNbrRestartHelperAge_Object = MibTableColumn
tmnxOspfNbrRestartHelperAge = _TmnxOspfNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 12),
    _TmnxOspfNbrRestartHelperAge_Type()
)
tmnxOspfNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrRestartHelperAge.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOspfNbrRestartHelperAge.setUnits("seconds")


class _TmnxOspfNbrRestartHelperExitRc_Type(Integer32):
    """Custom type tmnxOspfNbrRestartHelperExitRc based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_TmnxOspfNbrRestartHelperExitRc_Type.__name__ = "Integer32"
_TmnxOspfNbrRestartHelperExitRc_Object = MibTableColumn
tmnxOspfNbrRestartHelperExitRc = _TmnxOspfNbrRestartHelperExitRc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 13),
    _TmnxOspfNbrRestartHelperExitRc_Type()
)
tmnxOspfNbrRestartHelperExitRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrRestartHelperExitRc.setStatus("obsolete")
_TmnxOspfNbrUpTime_Type = TimeInterval
_TmnxOspfNbrUpTime_Object = MibTableColumn
tmnxOspfNbrUpTime = _TmnxOspfNbrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 14),
    _TmnxOspfNbrUpTime_Type()
)
tmnxOspfNbrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrUpTime.setStatus("obsolete")
_TmnxOspfNbrLastEventTime_Type = TimeStamp
_TmnxOspfNbrLastEventTime_Object = MibTableColumn
tmnxOspfNbrLastEventTime = _TmnxOspfNbrLastEventTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 15),
    _TmnxOspfNbrLastEventTime_Type()
)
tmnxOspfNbrLastEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrLastEventTime.setStatus("obsolete")


class _TmnxOspfNbrDeadTimeOutstanding_Type(Unsigned32):
    """Custom type tmnxOspfNbrDeadTimeOutstanding based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxOspfNbrDeadTimeOutstanding_Type.__name__ = "Unsigned32"
_TmnxOspfNbrDeadTimeOutstanding_Object = MibTableColumn
tmnxOspfNbrDeadTimeOutstanding = _TmnxOspfNbrDeadTimeOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 16),
    _TmnxOspfNbrDeadTimeOutstanding_Type()
)
tmnxOspfNbrDeadTimeOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrDeadTimeOutstanding.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxOspfNbrDeadTimeOutstanding.setUnits("seconds")
_TmnxOspfNbrLastRestartTime_Type = TimeStamp
_TmnxOspfNbrLastRestartTime_Object = MibTableColumn
tmnxOspfNbrLastRestartTime = _TmnxOspfNbrLastRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 17),
    _TmnxOspfNbrLastRestartTime_Type()
)
tmnxOspfNbrLastRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrLastRestartTime.setStatus("obsolete")
_TmnxOspfNbrRestartReason_Type = TmnxOspfRestartReasonTc
_TmnxOspfNbrRestartReason_Object = MibTableColumn
tmnxOspfNbrRestartReason = _TmnxOspfNbrRestartReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 18),
    _TmnxOspfNbrRestartReason_Type()
)
tmnxOspfNbrRestartReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrRestartReason.setStatus("obsolete")
_TmnxOspfNbrBfdTracking_Type = TruthValue
_TmnxOspfNbrBfdTracking_Object = MibTableColumn
tmnxOspfNbrBfdTracking = _TmnxOspfNbrBfdTracking_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 19),
    _TmnxOspfNbrBfdTracking_Type()
)
tmnxOspfNbrBfdTracking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrBfdTracking.setStatus("obsolete")
_TmnxOspfNbrDrId_Type = TmnxOspfRouterIdTc
_TmnxOspfNbrDrId_Object = MibTableColumn
tmnxOspfNbrDrId = _TmnxOspfNbrDrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 20),
    _TmnxOspfNbrDrId_Type()
)
tmnxOspfNbrDrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrDrId.setStatus("obsolete")
_TmnxOspfNbrBdrId_Type = TmnxOspfRouterIdTc
_TmnxOspfNbrBdrId_Object = MibTableColumn
tmnxOspfNbrBdrId = _TmnxOspfNbrBdrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 16, 1, 21),
    _TmnxOspfNbrBdrId_Type()
)
tmnxOspfNbrBdrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrBdrId.setStatus("obsolete")
_TmnxOspfNbrStatsTable_Object = MibTable
tmnxOspfNbrStatsTable = _TmnxOspfNbrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 17)
)
if mibBuilder.loadTexts:
    tmnxOspfNbrStatsTable.setStatus("obsolete")
_TmnxOspfNbrStatsEntry_Object = MibTableRow
tmnxOspfNbrStatsEntry = _TmnxOspfNbrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 17, 1)
)
if mibBuilder.loadTexts:
    tmnxOspfNbrStatsEntry.setStatus("obsolete")
_TmnxOspfNbrEvents_Type = Counter32
_TmnxOspfNbrEvents_Object = MibTableColumn
tmnxOspfNbrEvents = _TmnxOspfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 17, 1, 1),
    _TmnxOspfNbrEvents_Type()
)
tmnxOspfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrEvents.setStatus("obsolete")
_TmnxOspfNbrLsRetransQLen_Type = Gauge32
_TmnxOspfNbrLsRetransQLen_Object = MibTableColumn
tmnxOspfNbrLsRetransQLen = _TmnxOspfNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 17, 1, 2),
    _TmnxOspfNbrLsRetransQLen_Type()
)
tmnxOspfNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrLsRetransQLen.setStatus("obsolete")
_TmnxOspfNbrBadNbrStates_Type = Counter32
_TmnxOspfNbrBadNbrStates_Object = MibTableColumn
tmnxOspfNbrBadNbrStates = _TmnxOspfNbrBadNbrStates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 17, 1, 3),
    _TmnxOspfNbrBadNbrStates_Type()
)
tmnxOspfNbrBadNbrStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrBadNbrStates.setStatus("obsolete")
_TmnxOspfNbrLsaInstallFailed_Type = Counter32
_TmnxOspfNbrLsaInstallFailed_Object = MibTableColumn
tmnxOspfNbrLsaInstallFailed = _TmnxOspfNbrLsaInstallFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 17, 1, 4),
    _TmnxOspfNbrLsaInstallFailed_Type()
)
tmnxOspfNbrLsaInstallFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrLsaInstallFailed.setStatus("obsolete")
_TmnxOspfNbrBadSeqNums_Type = Counter32
_TmnxOspfNbrBadSeqNums_Object = MibTableColumn
tmnxOspfNbrBadSeqNums = _TmnxOspfNbrBadSeqNums_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 17, 1, 5),
    _TmnxOspfNbrBadSeqNums_Type()
)
tmnxOspfNbrBadSeqNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrBadSeqNums.setStatus("obsolete")
_TmnxOspfNbrBadMTUs_Type = Counter32
_TmnxOspfNbrBadMTUs_Object = MibTableColumn
tmnxOspfNbrBadMTUs = _TmnxOspfNbrBadMTUs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 17, 1, 6),
    _TmnxOspfNbrBadMTUs_Type()
)
tmnxOspfNbrBadMTUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrBadMTUs.setStatus("obsolete")
_TmnxOspfNbrBadPackets_Type = Counter32
_TmnxOspfNbrBadPackets_Object = MibTableColumn
tmnxOspfNbrBadPackets = _TmnxOspfNbrBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 17, 1, 7),
    _TmnxOspfNbrBadPackets_Type()
)
tmnxOspfNbrBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrBadPackets.setStatus("obsolete")
_TmnxOspfNbrLsaNotInLsdbs_Type = Counter32
_TmnxOspfNbrLsaNotInLsdbs_Object = MibTableColumn
tmnxOspfNbrLsaNotInLsdbs = _TmnxOspfNbrLsaNotInLsdbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 17, 1, 8),
    _TmnxOspfNbrLsaNotInLsdbs_Type()
)
tmnxOspfNbrLsaNotInLsdbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrLsaNotInLsdbs.setStatus("obsolete")
_TmnxOspfNbrOptionMismatches_Type = Counter32
_TmnxOspfNbrOptionMismatches_Object = MibTableColumn
tmnxOspfNbrOptionMismatches = _TmnxOspfNbrOptionMismatches_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 17, 1, 9),
    _TmnxOspfNbrOptionMismatches_Type()
)
tmnxOspfNbrOptionMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrOptionMismatches.setStatus("obsolete")
_TmnxOspfNbrDuplicates_Type = Counter32
_TmnxOspfNbrDuplicates_Object = MibTableColumn
tmnxOspfNbrDuplicates = _TmnxOspfNbrDuplicates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 17, 1, 10),
    _TmnxOspfNbrDuplicates_Type()
)
tmnxOspfNbrDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrDuplicates.setStatus("obsolete")
_TmnxOspfNbrNumRestarts_Type = Counter32
_TmnxOspfNbrNumRestarts_Object = MibTableColumn
tmnxOspfNbrNumRestarts = _TmnxOspfNbrNumRestarts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 17, 1, 11),
    _TmnxOspfNbrNumRestarts_Type()
)
tmnxOspfNbrNumRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNbrNumRestarts.setStatus("obsolete")
_TmnxOspfCfgNbrTable_Object = MibTable
tmnxOspfCfgNbrTable = _TmnxOspfCfgNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 18)
)
if mibBuilder.loadTexts:
    tmnxOspfCfgNbrTable.setStatus("current")
_TmnxOspfCfgNbrEntry_Object = MibTableRow
tmnxOspfCfgNbrEntry = _TmnxOspfCfgNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 18, 1)
)
tmnxOspfCfgNbrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrIfIndex"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrIfInstId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrAddressType"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrAddress"),
)
if mibBuilder.loadTexts:
    tmnxOspfCfgNbrEntry.setStatus("current")
_TmnxOspfCfgNbrIfIndex_Type = InterfaceIndex
_TmnxOspfCfgNbrIfIndex_Object = MibTableColumn
tmnxOspfCfgNbrIfIndex = _TmnxOspfCfgNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 18, 1, 1),
    _TmnxOspfCfgNbrIfIndex_Type()
)
tmnxOspfCfgNbrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfCfgNbrIfIndex.setStatus("current")
_TmnxOspfCfgNbrIfInstId_Type = TmnxOspfIfInstIdTc
_TmnxOspfCfgNbrIfInstId_Object = MibTableColumn
tmnxOspfCfgNbrIfInstId = _TmnxOspfCfgNbrIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 18, 1, 2),
    _TmnxOspfCfgNbrIfInstId_Type()
)
tmnxOspfCfgNbrIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfCfgNbrIfInstId.setStatus("current")
_TmnxOspfCfgNbrAddressType_Type = InetAddressType
_TmnxOspfCfgNbrAddressType_Object = MibTableColumn
tmnxOspfCfgNbrAddressType = _TmnxOspfCfgNbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 18, 1, 3),
    _TmnxOspfCfgNbrAddressType_Type()
)
tmnxOspfCfgNbrAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfCfgNbrAddressType.setStatus("current")


class _TmnxOspfCfgNbrAddress_Type(InetAddress):
    """Custom type tmnxOspfCfgNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOspfCfgNbrAddress_Type.__name__ = "InetAddress"
_TmnxOspfCfgNbrAddress_Object = MibTableColumn
tmnxOspfCfgNbrAddress = _TmnxOspfCfgNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 18, 1, 4),
    _TmnxOspfCfgNbrAddress_Type()
)
tmnxOspfCfgNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfCfgNbrAddress.setStatus("current")
_TmnxOspfCfgNbrStatus_Type = RowStatus
_TmnxOspfCfgNbrStatus_Object = MibTableColumn
tmnxOspfCfgNbrStatus = _TmnxOspfCfgNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 18, 1, 5),
    _TmnxOspfCfgNbrStatus_Type()
)
tmnxOspfCfgNbrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfCfgNbrStatus.setStatus("current")


class _TmnxOspfCfgNbrStorageType_Type(StorageType):
    """Custom type tmnxOspfCfgNbrStorageType based on StorageType"""
    defaultValue = 3


_TmnxOspfCfgNbrStorageType_Type.__name__ = "StorageType"
_TmnxOspfCfgNbrStorageType_Object = MibTableColumn
tmnxOspfCfgNbrStorageType = _TmnxOspfCfgNbrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 18, 1, 6),
    _TmnxOspfCfgNbrStorageType_Type()
)
tmnxOspfCfgNbrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfCfgNbrStorageType.setStatus("obsolete")
_TmnxOspfCfgNbrLastChanged_Type = TimeStamp
_TmnxOspfCfgNbrLastChanged_Object = MibTableColumn
tmnxOspfCfgNbrLastChanged = _TmnxOspfCfgNbrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 18, 1, 7),
    _TmnxOspfCfgNbrLastChanged_Type()
)
tmnxOspfCfgNbrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfCfgNbrLastChanged.setStatus("current")


class _TmnxOspfCfgNbrPriority_Type(DesignatedRouterPriority):
    """Custom type tmnxOspfCfgNbrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_TmnxOspfCfgNbrPriority_Type.__name__ = "DesignatedRouterPriority"
_TmnxOspfCfgNbrPriority_Object = MibTableColumn
tmnxOspfCfgNbrPriority = _TmnxOspfCfgNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 18, 1, 8),
    _TmnxOspfCfgNbrPriority_Type()
)
tmnxOspfCfgNbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfCfgNbrPriority.setStatus("current")
_TmnxOspfCfgNbrRtrId_Type = TmnxOspfRouterIdTc
_TmnxOspfCfgNbrRtrId_Object = MibTableColumn
tmnxOspfCfgNbrRtrId = _TmnxOspfCfgNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 18, 1, 9),
    _TmnxOspfCfgNbrRtrId_Type()
)
tmnxOspfCfgNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfCfgNbrRtrId.setStatus("current")


class _TmnxOspfCfgNbrState_Type(Integer32):
    """Custom type tmnxOspfCfgNbrState based on Integer32"""
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
        *(("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exchangeStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_TmnxOspfCfgNbrState_Type.__name__ = "Integer32"
_TmnxOspfCfgNbrState_Object = MibTableColumn
tmnxOspfCfgNbrState = _TmnxOspfCfgNbrState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 18, 1, 10),
    _TmnxOspfCfgNbrState_Type()
)
tmnxOspfCfgNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfCfgNbrState.setStatus("current")
_TmnxOspfVirtNbrTable_Object = MibTable
tmnxOspfVirtNbrTable = _TmnxOspfVirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 19)
)
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrTable.setStatus("current")
_TmnxOspfVirtNbrEntry_Object = MibTableRow
tmnxOspfVirtNbrEntry = _TmnxOspfVirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 19, 1)
)
tmnxOspfVirtNbrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrArea"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrEntry.setStatus("current")
_TmnxOspfVirtNbrArea_Type = TmnxOspfAreaIdTc
_TmnxOspfVirtNbrArea_Object = MibTableColumn
tmnxOspfVirtNbrArea = _TmnxOspfVirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 19, 1, 1),
    _TmnxOspfVirtNbrArea_Type()
)
tmnxOspfVirtNbrArea.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrArea.setStatus("current")
_TmnxOspfVirtNbrRtrId_Type = TmnxOspfRouterIdTc
_TmnxOspfVirtNbrRtrId_Object = MibTableColumn
tmnxOspfVirtNbrRtrId = _TmnxOspfVirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 19, 1, 2),
    _TmnxOspfVirtNbrRtrId_Type()
)
tmnxOspfVirtNbrRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrRtrId.setStatus("current")
_TmnxOspfVirtNbrIfIndex_Type = InterfaceIndex
_TmnxOspfVirtNbrIfIndex_Object = MibTableColumn
tmnxOspfVirtNbrIfIndex = _TmnxOspfVirtNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 19, 1, 3),
    _TmnxOspfVirtNbrIfIndex_Type()
)
tmnxOspfVirtNbrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrIfIndex.setStatus("current")
_TmnxOspfVirtNbrIfInstId_Type = TmnxOspfIfInstIdTc
_TmnxOspfVirtNbrIfInstId_Object = MibTableColumn
tmnxOspfVirtNbrIfInstId = _TmnxOspfVirtNbrIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 19, 1, 4),
    _TmnxOspfVirtNbrIfInstId_Type()
)
tmnxOspfVirtNbrIfInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrIfInstId.setStatus("current")
_TmnxOspfVirtNbrAddressType_Type = InetAddressType
_TmnxOspfVirtNbrAddressType_Object = MibTableColumn
tmnxOspfVirtNbrAddressType = _TmnxOspfVirtNbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 19, 1, 5),
    _TmnxOspfVirtNbrAddressType_Type()
)
tmnxOspfVirtNbrAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrAddressType.setStatus("current")


class _TmnxOspfVirtNbrAddress_Type(InetAddress):
    """Custom type tmnxOspfVirtNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOspfVirtNbrAddress_Type.__name__ = "InetAddress"
_TmnxOspfVirtNbrAddress_Object = MibTableColumn
tmnxOspfVirtNbrAddress = _TmnxOspfVirtNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 19, 1, 6),
    _TmnxOspfVirtNbrAddress_Type()
)
tmnxOspfVirtNbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrAddress.setStatus("current")
_TmnxOspfVirtNbrOptions_Type = Integer32
_TmnxOspfVirtNbrOptions_Object = MibTableColumn
tmnxOspfVirtNbrOptions = _TmnxOspfVirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 19, 1, 7),
    _TmnxOspfVirtNbrOptions_Type()
)
tmnxOspfVirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrOptions.setStatus("current")


class _TmnxOspfVirtNbrState_Type(Integer32):
    """Custom type tmnxOspfVirtNbrState based on Integer32"""
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
        *(("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exchangeStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_TmnxOspfVirtNbrState_Type.__name__ = "Integer32"
_TmnxOspfVirtNbrState_Object = MibTableColumn
tmnxOspfVirtNbrState = _TmnxOspfVirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 19, 1, 8),
    _TmnxOspfVirtNbrState_Type()
)
tmnxOspfVirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrState.setStatus("current")
_TmnxOspfVirtNbrHelloSuppressed_Type = TruthValue
_TmnxOspfVirtNbrHelloSuppressed_Object = MibTableColumn
tmnxOspfVirtNbrHelloSuppressed = _TmnxOspfVirtNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 19, 1, 9),
    _TmnxOspfVirtNbrHelloSuppressed_Type()
)
tmnxOspfVirtNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrHelloSuppressed.setStatus("current")
_TmnxOspfVirtNbrIfId_Type = InterfaceIndexOrZero
_TmnxOspfVirtNbrIfId_Object = MibTableColumn
tmnxOspfVirtNbrIfId = _TmnxOspfVirtNbrIfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 19, 1, 10),
    _TmnxOspfVirtNbrIfId_Type()
)
tmnxOspfVirtNbrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrIfId.setStatus("current")


class _TmnxOspfVirtNbrRestartHelperStatus_Type(Integer32):
    """Custom type tmnxOspfVirtNbrRestartHelperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notHelping", 1),
          ("helping", 2))
    )


_TmnxOspfVirtNbrRestartHelperStatus_Type.__name__ = "Integer32"
_TmnxOspfVirtNbrRestartHelperStatus_Object = MibTableColumn
tmnxOspfVirtNbrRestartHelperStatus = _TmnxOspfVirtNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 19, 1, 11),
    _TmnxOspfVirtNbrRestartHelperStatus_Type()
)
tmnxOspfVirtNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrRestartHelperStatus.setStatus("current")
_TmnxOspfVirtNbrRestartHelperAge_Type = TmnxOspfUpToRefreshIntervalTc
_TmnxOspfVirtNbrRestartHelperAge_Object = MibTableColumn
tmnxOspfVirtNbrRestartHelperAge = _TmnxOspfVirtNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 19, 1, 12),
    _TmnxOspfVirtNbrRestartHelperAge_Type()
)
tmnxOspfVirtNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrRestartHelperAge.setUnits("seconds")


class _TmnxOspfVirtNbrRestartHelperExitRc_Type(Integer32):
    """Custom type tmnxOspfVirtNbrRestartHelperExitRc based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_TmnxOspfVirtNbrRestartHelperExitRc_Type.__name__ = "Integer32"
_TmnxOspfVirtNbrRestartHelperExitRc_Object = MibTableColumn
tmnxOspfVirtNbrRestartHelperExitRc = _TmnxOspfVirtNbrRestartHelperExitRc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 19, 1, 13),
    _TmnxOspfVirtNbrRestartHelperExitRc_Type()
)
tmnxOspfVirtNbrRestartHelperExitRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrRestartHelperExitRc.setStatus("current")
_TmnxOspfVirtNbrUpTime_Type = TimeInterval
_TmnxOspfVirtNbrUpTime_Object = MibTableColumn
tmnxOspfVirtNbrUpTime = _TmnxOspfVirtNbrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 19, 1, 14),
    _TmnxOspfVirtNbrUpTime_Type()
)
tmnxOspfVirtNbrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrUpTime.setStatus("current")
_TmnxOspfVirtNbrLastEventTime_Type = TimeStamp
_TmnxOspfVirtNbrLastEventTime_Object = MibTableColumn
tmnxOspfVirtNbrLastEventTime = _TmnxOspfVirtNbrLastEventTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 19, 1, 15),
    _TmnxOspfVirtNbrLastEventTime_Type()
)
tmnxOspfVirtNbrLastEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrLastEventTime.setStatus("current")


class _TmnxOspfVirtNbrDeadTmeOutstng_Type(Unsigned32):
    """Custom type tmnxOspfVirtNbrDeadTmeOutstng based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxOspfVirtNbrDeadTmeOutstng_Type.__name__ = "Unsigned32"
_TmnxOspfVirtNbrDeadTmeOutstng_Object = MibTableColumn
tmnxOspfVirtNbrDeadTmeOutstng = _TmnxOspfVirtNbrDeadTmeOutstng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 19, 1, 16),
    _TmnxOspfVirtNbrDeadTmeOutstng_Type()
)
tmnxOspfVirtNbrDeadTmeOutstng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrDeadTmeOutstng.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrDeadTmeOutstng.setUnits("seconds")
_TmnxOspfVirtNbrLastRestartTime_Type = TimeStamp
_TmnxOspfVirtNbrLastRestartTime_Object = MibTableColumn
tmnxOspfVirtNbrLastRestartTime = _TmnxOspfVirtNbrLastRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 19, 1, 17),
    _TmnxOspfVirtNbrLastRestartTime_Type()
)
tmnxOspfVirtNbrLastRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrLastRestartTime.setStatus("current")
_TmnxOspfVirtNbrRestartReason_Type = TmnxOspfRestartReasonTc
_TmnxOspfVirtNbrRestartReason_Object = MibTableColumn
tmnxOspfVirtNbrRestartReason = _TmnxOspfVirtNbrRestartReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 19, 1, 18),
    _TmnxOspfVirtNbrRestartReason_Type()
)
tmnxOspfVirtNbrRestartReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrRestartReason.setStatus("current")
_TmnxOspfVirtNbrStatsTable_Object = MibTable
tmnxOspfVirtNbrStatsTable = _TmnxOspfVirtNbrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 20)
)
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrStatsTable.setStatus("current")
_TmnxOspfVirtNbrStatsEntry_Object = MibTableRow
tmnxOspfVirtNbrStatsEntry = _TmnxOspfVirtNbrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 20, 1)
)
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrStatsEntry.setStatus("current")
_TmnxOspfVirtNbrEvents_Type = Counter32
_TmnxOspfVirtNbrEvents_Object = MibTableColumn
tmnxOspfVirtNbrEvents = _TmnxOspfVirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 20, 1, 1),
    _TmnxOspfVirtNbrEvents_Type()
)
tmnxOspfVirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrEvents.setStatus("current")
_TmnxOspfVirtNbrLsRetransQLen_Type = Gauge32
_TmnxOspfVirtNbrLsRetransQLen_Object = MibTableColumn
tmnxOspfVirtNbrLsRetransQLen = _TmnxOspfVirtNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 20, 1, 2),
    _TmnxOspfVirtNbrLsRetransQLen_Type()
)
tmnxOspfVirtNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrLsRetransQLen.setStatus("current")
_TmnxOspfVirtNbrBadNbrStates_Type = Counter32
_TmnxOspfVirtNbrBadNbrStates_Object = MibTableColumn
tmnxOspfVirtNbrBadNbrStates = _TmnxOspfVirtNbrBadNbrStates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 20, 1, 3),
    _TmnxOspfVirtNbrBadNbrStates_Type()
)
tmnxOspfVirtNbrBadNbrStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrBadNbrStates.setStatus("current")
_TmnxOspfVirtNbrLsaInstallFail_Type = Counter32
_TmnxOspfVirtNbrLsaInstallFail_Object = MibTableColumn
tmnxOspfVirtNbrLsaInstallFail = _TmnxOspfVirtNbrLsaInstallFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 20, 1, 4),
    _TmnxOspfVirtNbrLsaInstallFail_Type()
)
tmnxOspfVirtNbrLsaInstallFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrLsaInstallFail.setStatus("current")
_TmnxOspfVirtNbrBadSeqNums_Type = Counter32
_TmnxOspfVirtNbrBadSeqNums_Object = MibTableColumn
tmnxOspfVirtNbrBadSeqNums = _TmnxOspfVirtNbrBadSeqNums_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 20, 1, 5),
    _TmnxOspfVirtNbrBadSeqNums_Type()
)
tmnxOspfVirtNbrBadSeqNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrBadSeqNums.setStatus("current")
_TmnxOspfVirtNbrBadMTUs_Type = Counter32
_TmnxOspfVirtNbrBadMTUs_Object = MibTableColumn
tmnxOspfVirtNbrBadMTUs = _TmnxOspfVirtNbrBadMTUs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 20, 1, 6),
    _TmnxOspfVirtNbrBadMTUs_Type()
)
tmnxOspfVirtNbrBadMTUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrBadMTUs.setStatus("current")
_TmnxOspfVirtNbrBadPackets_Type = Counter32
_TmnxOspfVirtNbrBadPackets_Object = MibTableColumn
tmnxOspfVirtNbrBadPackets = _TmnxOspfVirtNbrBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 20, 1, 7),
    _TmnxOspfVirtNbrBadPackets_Type()
)
tmnxOspfVirtNbrBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrBadPackets.setStatus("current")
_TmnxOspfVirtNbrLsaNotInLsdbs_Type = Counter32
_TmnxOspfVirtNbrLsaNotInLsdbs_Object = MibTableColumn
tmnxOspfVirtNbrLsaNotInLsdbs = _TmnxOspfVirtNbrLsaNotInLsdbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 20, 1, 8),
    _TmnxOspfVirtNbrLsaNotInLsdbs_Type()
)
tmnxOspfVirtNbrLsaNotInLsdbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrLsaNotInLsdbs.setStatus("current")
_TmnxOspfVirtNbrOptionMismatch_Type = Counter32
_TmnxOspfVirtNbrOptionMismatch_Object = MibTableColumn
tmnxOspfVirtNbrOptionMismatch = _TmnxOspfVirtNbrOptionMismatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 20, 1, 9),
    _TmnxOspfVirtNbrOptionMismatch_Type()
)
tmnxOspfVirtNbrOptionMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrOptionMismatch.setStatus("current")
_TmnxOspfVirtNbrDuplicates_Type = Counter32
_TmnxOspfVirtNbrDuplicates_Object = MibTableColumn
tmnxOspfVirtNbrDuplicates = _TmnxOspfVirtNbrDuplicates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 20, 1, 10),
    _TmnxOspfVirtNbrDuplicates_Type()
)
tmnxOspfVirtNbrDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrDuplicates.setStatus("current")
_TmnxOspfVirtNbrNumRestarts_Type = Counter32
_TmnxOspfVirtNbrNumRestarts_Object = MibTableColumn
tmnxOspfVirtNbrNumRestarts = _TmnxOspfVirtNbrNumRestarts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 20, 1, 11),
    _TmnxOspfVirtNbrNumRestarts_Type()
)
tmnxOspfVirtNbrNumRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrNumRestarts.setStatus("current")
_TmnxOspfAreaAggrTable_Object = MibTable
tmnxOspfAreaAggrTable = _TmnxOspfAreaAggrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 21)
)
if mibBuilder.loadTexts:
    tmnxOspfAreaAggrTable.setStatus("current")
_TmnxOspfAreaAggrEntry_Object = MibTableRow
tmnxOspfAreaAggrEntry = _TmnxOspfAreaAggrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 21, 1)
)
tmnxOspfAreaAggrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrAreaID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrAreaLsdbType"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrPrefixType"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrPrefix"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrPrefixLength"),
)
if mibBuilder.loadTexts:
    tmnxOspfAreaAggrEntry.setStatus("current")
_TmnxOspfAreaAggrAreaID_Type = TmnxOspfAreaIdTc
_TmnxOspfAreaAggrAreaID_Object = MibTableColumn
tmnxOspfAreaAggrAreaID = _TmnxOspfAreaAggrAreaID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 21, 1, 1),
    _TmnxOspfAreaAggrAreaID_Type()
)
tmnxOspfAreaAggrAreaID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfAreaAggrAreaID.setStatus("current")


class _TmnxOspfAreaAggrAreaLsdbType_Type(Integer32):
    """Custom type tmnxOspfAreaAggrAreaLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              7,
              8195,
              8199)
        )
    )
    namedValues = NamedValues(
        *(("ospfv2InterAreaPrefixLsa", 3),
          ("ospfv2NssaExternalLsa", 7),
          ("interAreaPrefixLsa", 8195),
          ("nssaExternalLsa", 8199))
    )


_TmnxOspfAreaAggrAreaLsdbType_Type.__name__ = "Integer32"
_TmnxOspfAreaAggrAreaLsdbType_Object = MibTableColumn
tmnxOspfAreaAggrAreaLsdbType = _TmnxOspfAreaAggrAreaLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 21, 1, 2),
    _TmnxOspfAreaAggrAreaLsdbType_Type()
)
tmnxOspfAreaAggrAreaLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfAreaAggrAreaLsdbType.setStatus("current")
_TmnxOspfAreaAggrPrefixType_Type = TmnxAddressAndPrefixType
_TmnxOspfAreaAggrPrefixType_Object = MibTableColumn
tmnxOspfAreaAggrPrefixType = _TmnxOspfAreaAggrPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 21, 1, 3),
    _TmnxOspfAreaAggrPrefixType_Type()
)
tmnxOspfAreaAggrPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfAreaAggrPrefixType.setStatus("current")


class _TmnxOspfAreaAggrPrefix_Type(TmnxAddressAndPrefixAddress):
    """Custom type tmnxOspfAreaAggrPrefix based on TmnxAddressAndPrefixAddress"""
    subtypeSpec = TmnxAddressAndPrefixAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOspfAreaAggrPrefix_Type.__name__ = "TmnxAddressAndPrefixAddress"
_TmnxOspfAreaAggrPrefix_Object = MibTableColumn
tmnxOspfAreaAggrPrefix = _TmnxOspfAreaAggrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 21, 1, 4),
    _TmnxOspfAreaAggrPrefix_Type()
)
tmnxOspfAreaAggrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfAreaAggrPrefix.setStatus("current")


class _TmnxOspfAreaAggrPrefixLength_Type(TmnxAddressAndPrefixPrefix):
    """Custom type tmnxOspfAreaAggrPrefixLength based on TmnxAddressAndPrefixPrefix"""
    subtypeSpec = TmnxAddressAndPrefixPrefix.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxOspfAreaAggrPrefixLength_Type.__name__ = "TmnxAddressAndPrefixPrefix"
_TmnxOspfAreaAggrPrefixLength_Object = MibTableColumn
tmnxOspfAreaAggrPrefixLength = _TmnxOspfAreaAggrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 21, 1, 5),
    _TmnxOspfAreaAggrPrefixLength_Type()
)
tmnxOspfAreaAggrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfAreaAggrPrefixLength.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfAreaAggrPrefixLength.setUnits("bits")
_TmnxOspfAreaAggrStatus_Type = RowStatus
_TmnxOspfAreaAggrStatus_Object = MibTableColumn
tmnxOspfAreaAggrStatus = _TmnxOspfAreaAggrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 21, 1, 6),
    _TmnxOspfAreaAggrStatus_Type()
)
tmnxOspfAreaAggrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaAggrStatus.setStatus("current")
_TmnxOspfAreaAggrLastChanged_Type = TimeStamp
_TmnxOspfAreaAggrLastChanged_Object = MibTableColumn
tmnxOspfAreaAggrLastChanged = _TmnxOspfAreaAggrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 21, 1, 7),
    _TmnxOspfAreaAggrLastChanged_Type()
)
tmnxOspfAreaAggrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAreaAggrLastChanged.setStatus("current")


class _TmnxOspfAreaAggrEffect_Type(Integer32):
    """Custom type tmnxOspfAreaAggrEffect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertiseMatching", 1),
          ("doNotAdvertiseMatching", 2))
    )


_TmnxOspfAreaAggrEffect_Type.__name__ = "Integer32"
_TmnxOspfAreaAggrEffect_Object = MibTableColumn
tmnxOspfAreaAggrEffect = _TmnxOspfAreaAggrEffect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 21, 1, 8),
    _TmnxOspfAreaAggrEffect_Type()
)
tmnxOspfAreaAggrEffect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaAggrEffect.setStatus("current")


class _TmnxOspfAreaAggrRouteTag_Type(Integer32):
    """Custom type tmnxOspfAreaAggrRouteTag based on Integer32"""
    defaultValue = 0


_TmnxOspfAreaAggrRouteTag_Type.__name__ = "Integer32"
_TmnxOspfAreaAggrRouteTag_Object = MibTableColumn
tmnxOspfAreaAggrRouteTag = _TmnxOspfAreaAggrRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 21, 1, 9),
    _TmnxOspfAreaAggrRouteTag_Type()
)
tmnxOspfAreaAggrRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAreaAggrRouteTag.setStatus("current")
_TmnxOspfIfMD5KeyTable_Object = MibTable
tmnxOspfIfMD5KeyTable = _TmnxOspfIfMD5KeyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 22)
)
if mibBuilder.loadTexts:
    tmnxOspfIfMD5KeyTable.setStatus("obsolete")
_TmnxOspfIfMD5KeyEntry_Object = MibTableRow
tmnxOspfIfMD5KeyEntry = _TmnxOspfIfMD5KeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 22, 1)
)
tmnxOspfIfMD5KeyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfIfIndex"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfIfInstId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMD5KeyIndex"),
)
if mibBuilder.loadTexts:
    tmnxOspfIfMD5KeyEntry.setStatus("obsolete")
_TmnxOspfIfMD5KeyIndex_Type = TmnxOspfIfMD5KeyId
_TmnxOspfIfMD5KeyIndex_Object = MibTableColumn
tmnxOspfIfMD5KeyIndex = _TmnxOspfIfMD5KeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 22, 1, 1),
    _TmnxOspfIfMD5KeyIndex_Type()
)
tmnxOspfIfMD5KeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfIfMD5KeyIndex.setStatus("obsolete")
_TmnxOspfIfMD5KeyStatus_Type = RowStatus
_TmnxOspfIfMD5KeyStatus_Object = MibTableColumn
tmnxOspfIfMD5KeyStatus = _TmnxOspfIfMD5KeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 22, 1, 2),
    _TmnxOspfIfMD5KeyStatus_Type()
)
tmnxOspfIfMD5KeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfMD5KeyStatus.setStatus("obsolete")


class _TmnxOspfIfMD5KeyKey_Type(OctetString):
    """Custom type tmnxOspfIfMD5KeyKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmnxOspfIfMD5KeyKey_Type.__name__ = "OctetString"
_TmnxOspfIfMD5KeyKey_Object = MibTableColumn
tmnxOspfIfMD5KeyKey = _TmnxOspfIfMD5KeyKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 22, 1, 3),
    _TmnxOspfIfMD5KeyKey_Type()
)
tmnxOspfIfMD5KeyKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfMD5KeyKey.setStatus("obsolete")


class _TmnxOspfIfMD5KeyStartTime_Type(DateAndTime):
    """Custom type tmnxOspfIfMD5KeyStartTime based on DateAndTime"""
    defaultHexValue = "0000000000000000000000"


_TmnxOspfIfMD5KeyStartTime_Type.__name__ = "DateAndTime"
_TmnxOspfIfMD5KeyStartTime_Object = MibTableColumn
tmnxOspfIfMD5KeyStartTime = _TmnxOspfIfMD5KeyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 22, 1, 4),
    _TmnxOspfIfMD5KeyStartTime_Type()
)
tmnxOspfIfMD5KeyStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfMD5KeyStartTime.setStatus("obsolete")


class _TmnxOspfIfMD5KeyStopTime_Type(DateAndTime):
    """Custom type tmnxOspfIfMD5KeyStopTime based on DateAndTime"""
    defaultHexValue = "0000000000000000000000"


_TmnxOspfIfMD5KeyStopTime_Type.__name__ = "DateAndTime"
_TmnxOspfIfMD5KeyStopTime_Object = MibTableColumn
tmnxOspfIfMD5KeyStopTime = _TmnxOspfIfMD5KeyStopTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 22, 1, 5),
    _TmnxOspfIfMD5KeyStopTime_Type()
)
tmnxOspfIfMD5KeyStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfMD5KeyStopTime.setStatus("obsolete")
_TmnxOspfVirtIfMD5KeyTable_Object = MibTable
tmnxOspfVirtIfMD5KeyTable = _TmnxOspfVirtIfMD5KeyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 23)
)
if mibBuilder.loadTexts:
    tmnxOspfVirtIfMD5KeyTable.setStatus("current")
_TmnxOspfVirtIfMD5KeyEntry_Object = MibTableRow
tmnxOspfVirtIfMD5KeyEntry = _TmnxOspfVirtIfMD5KeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 23, 1)
)
tmnxOspfVirtIfMD5KeyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfAreaId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfNeighbor"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfMD5KeyIndex"),
)
if mibBuilder.loadTexts:
    tmnxOspfVirtIfMD5KeyEntry.setStatus("current")
_TmnxOspfVirtIfMD5KeyIndex_Type = TmnxOspfIfMD5KeyId
_TmnxOspfVirtIfMD5KeyIndex_Object = MibTableColumn
tmnxOspfVirtIfMD5KeyIndex = _TmnxOspfVirtIfMD5KeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 23, 1, 1),
    _TmnxOspfVirtIfMD5KeyIndex_Type()
)
tmnxOspfVirtIfMD5KeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfMD5KeyIndex.setStatus("current")
_TmnxOspfVirtIfMD5KeyStatus_Type = RowStatus
_TmnxOspfVirtIfMD5KeyStatus_Object = MibTableColumn
tmnxOspfVirtIfMD5KeyStatus = _TmnxOspfVirtIfMD5KeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 23, 1, 2),
    _TmnxOspfVirtIfMD5KeyStatus_Type()
)
tmnxOspfVirtIfMD5KeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfMD5KeyStatus.setStatus("current")


class _TmnxOspfVirtIfMD5KeyKey_Type(OctetString):
    """Custom type tmnxOspfVirtIfMD5KeyKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmnxOspfVirtIfMD5KeyKey_Type.__name__ = "OctetString"
_TmnxOspfVirtIfMD5KeyKey_Object = MibTableColumn
tmnxOspfVirtIfMD5KeyKey = _TmnxOspfVirtIfMD5KeyKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 23, 1, 3),
    _TmnxOspfVirtIfMD5KeyKey_Type()
)
tmnxOspfVirtIfMD5KeyKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfMD5KeyKey.setStatus("current")


class _TmnxOspfVirtIfMD5KeyStartTime_Type(DateAndTime):
    """Custom type tmnxOspfVirtIfMD5KeyStartTime based on DateAndTime"""
    defaultHexValue = "0000000000000000000000"


_TmnxOspfVirtIfMD5KeyStartTime_Type.__name__ = "DateAndTime"
_TmnxOspfVirtIfMD5KeyStartTime_Object = MibTableColumn
tmnxOspfVirtIfMD5KeyStartTime = _TmnxOspfVirtIfMD5KeyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 23, 1, 4),
    _TmnxOspfVirtIfMD5KeyStartTime_Type()
)
tmnxOspfVirtIfMD5KeyStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfMD5KeyStartTime.setStatus("obsolete")


class _TmnxOspfVirtIfMD5KeyStopTime_Type(DateAndTime):
    """Custom type tmnxOspfVirtIfMD5KeyStopTime based on DateAndTime"""
    defaultHexValue = "0000000000000000000000"


_TmnxOspfVirtIfMD5KeyStopTime_Type.__name__ = "DateAndTime"
_TmnxOspfVirtIfMD5KeyStopTime_Object = MibTableColumn
tmnxOspfVirtIfMD5KeyStopTime = _TmnxOspfVirtIfMD5KeyStopTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 23, 1, 5),
    _TmnxOspfVirtIfMD5KeyStopTime_Type()
)
tmnxOspfVirtIfMD5KeyStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfVirtIfMD5KeyStopTime.setStatus("obsolete")
_TmnxOspfNotifyObjs_ObjectIdentity = ObjectIdentity
tmnxOspfNotifyObjs = _TmnxOspfNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24)
)


class _TmnxOspfSetTrap_Type(OctetString):
    """Custom type tmnxOspfSetTrap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_TmnxOspfSetTrap_Type.__name__ = "OctetString"
_TmnxOspfSetTrap_Object = MibScalar
tmnxOspfSetTrap = _TmnxOspfSetTrap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 1),
    _TmnxOspfSetTrap_Type()
)
tmnxOspfSetTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOspfSetTrap.setStatus("current")


class _TmnxOspfConfigErrorType_Type(Integer32):
    """Custom type tmnxOspfConfigErrorType based on Integer32"""
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
              15,
              16,
              1001,
              1002,
              1003,
              1004,
              1005)
        )
    )
    namedValues = NamedValues(
        *(("badVersion", 1),
          ("areaMismatch", 2),
          ("unknownNbmaNbr", 3),
          ("unknownVirtualNbr", 4),
          ("authTypeMismatch", 5),
          ("authFailure", 6),
          ("netMaskMismatch", 7),
          ("helloIntervalMismatch", 8),
          ("deadIntervalMismatch", 9),
          ("optionMismatch", 10),
          ("mtuMismatch", 11),
          ("duplicateRouterId", 12),
          ("noError", 13),
          ("instanceMismatch", 14),
          ("unknownNbr", 15),
          ("tooManyNbrOnIf", 16),
          ("ifTypeMismatch", 1001),
          ("nullRouterId", 1002),
          ("ifAdminDown", 1003),
          ("ifPassive", 1004),
          ("subnetMismatch", 1005))
    )


_TmnxOspfConfigErrorType_Type.__name__ = "Integer32"
_TmnxOspfConfigErrorType_Object = MibScalar
tmnxOspfConfigErrorType = _TmnxOspfConfigErrorType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 2),
    _TmnxOspfConfigErrorType_Type()
)
tmnxOspfConfigErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfConfigErrorType.setStatus("current")


class _TmnxOspfPacketType_Type(Integer32):
    """Custom type tmnxOspfPacketType based on Integer32"""
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
        *(("hello", 1),
          ("dbDescript", 2),
          ("lsReq", 3),
          ("lsUpdate", 4),
          ("lsAck", 5),
          ("nullPacket", 6))
    )


_TmnxOspfPacketType_Type.__name__ = "Integer32"
_TmnxOspfPacketType_Object = MibScalar
tmnxOspfPacketType = _TmnxOspfPacketType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 3),
    _TmnxOspfPacketType_Type()
)
tmnxOspfPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfPacketType.setStatus("current")
_TmnxOspfPacketSrcAddressType_Type = InetAddressType
_TmnxOspfPacketSrcAddressType_Object = MibScalar
tmnxOspfPacketSrcAddressType = _TmnxOspfPacketSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 4),
    _TmnxOspfPacketSrcAddressType_Type()
)
tmnxOspfPacketSrcAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfPacketSrcAddressType.setStatus("current")


class _TmnxOspfPacketSrcAddress_Type(InetAddress):
    """Custom type tmnxOspfPacketSrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxOspfPacketSrcAddress_Type.__name__ = "InetAddress"
_TmnxOspfPacketSrcAddress_Object = MibScalar
tmnxOspfPacketSrcAddress = _TmnxOspfPacketSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 5),
    _TmnxOspfPacketSrcAddress_Type()
)
tmnxOspfPacketSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfPacketSrcAddress.setStatus("current")


class _TmnxOspfIfIpName_Type(DisplayString):
    """Custom type tmnxOspfIfIpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )


_TmnxOspfIfIpName_Type.__name__ = "DisplayString"
_TmnxOspfIfIpName_Object = MibScalar
tmnxOspfIfIpName = _TmnxOspfIfIpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 6),
    _TmnxOspfIfIpName_Type()
)
tmnxOspfIfIpName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOspfIfIpName.setStatus("current")


class _TmnxOspfIfEvent_Type(DisplayString):
    """Custom type tmnxOspfIfEvent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxOspfIfEvent_Type.__name__ = "DisplayString"
_TmnxOspfIfEvent_Object = MibScalar
tmnxOspfIfEvent = _TmnxOspfIfEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 7),
    _TmnxOspfIfEvent_Type()
)
tmnxOspfIfEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOspfIfEvent.setStatus("current")


class _TmnxOspfFailureReasonCode_Type(Integer32):
    """Custom type tmnxOspfFailureReasonCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("mallocFailure", 2),
          ("rtrLsaTooBig", 3),
          ("spfFailures", 4),
          ("rteTblAdd", 5),
          ("rteTblModify", 6),
          ("rteTblDelete", 7))
    )


_TmnxOspfFailureReasonCode_Type.__name__ = "Integer32"
_TmnxOspfFailureReasonCode_Object = MibScalar
tmnxOspfFailureReasonCode = _TmnxOspfFailureReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 8),
    _TmnxOspfFailureReasonCode_Type()
)
tmnxOspfFailureReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOspfFailureReasonCode.setStatus("current")


class _TmnxOspfBadPacketErrType_Type(Integer32):
    """Custom type tmnxOspfBadPacketErrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("wrongFormat", 1),
          ("wrongChksum", 2),
          ("ifOperDown", 3),
          ("badDstAddr", 4),
          ("badSrcAddr", 5),
          ("badLlsBlock", 6),
          ("doubleLlsMtu", 7))
    )


_TmnxOspfBadPacketErrType_Type.__name__ = "Integer32"
_TmnxOspfBadPacketErrType_Object = MibScalar
tmnxOspfBadPacketErrType = _TmnxOspfBadPacketErrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 9),
    _TmnxOspfBadPacketErrType_Type()
)
tmnxOspfBadPacketErrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOspfBadPacketErrType.setStatus("current")
_TmnxOspfNotifPfxSidRangeStartLbl_Type = Unsigned32
_TmnxOspfNotifPfxSidRangeStartLbl_Object = MibScalar
tmnxOspfNotifPfxSidRangeStartLbl = _TmnxOspfNotifPfxSidRangeStartLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 10),
    _TmnxOspfNotifPfxSidRangeStartLbl_Type()
)
tmnxOspfNotifPfxSidRangeStartLbl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOspfNotifPfxSidRangeStartLbl.setStatus("current")
_TmnxOspfNotifPfxSidRangeMaxIdx_Type = Unsigned32
_TmnxOspfNotifPfxSidRangeMaxIdx_Object = MibScalar
tmnxOspfNotifPfxSidRangeMaxIdx = _TmnxOspfNotifPfxSidRangeMaxIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 11),
    _TmnxOspfNotifPfxSidRangeMaxIdx_Type()
)
tmnxOspfNotifPfxSidRangeMaxIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOspfNotifPfxSidRangeMaxIdx.setStatus("current")
_TmnxOspfNotifPfxNhAdvRtr_Type = TmnxOspfRouterIdTc
_TmnxOspfNotifPfxNhAdvRtr_Object = MibScalar
tmnxOspfNotifPfxNhAdvRtr = _TmnxOspfNotifPfxNhAdvRtr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 12),
    _TmnxOspfNotifPfxNhAdvRtr_Type()
)
tmnxOspfNotifPfxNhAdvRtr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOspfNotifPfxNhAdvRtr.setStatus("current")
_TmnxOspfNotifyDescription_Type = DisplayString
_TmnxOspfNotifyDescription_Object = MibScalar
tmnxOspfNotifyDescription = _TmnxOspfNotifyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 13),
    _TmnxOspfNotifyDescription_Type()
)
tmnxOspfNotifyDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOspfNotifyDescription.setStatus("current")


class _TmnxOspfBfdSessSetupFailReason_Type(Integer32):
    """Custom type tmnxOspfBfdSessSetupFailReason based on Integer32"""
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("bfdSessNoError", 0),
          ("bfdSessFailMaxSessionLimit", 1),
          ("bfdSessFailCfgNotProper", 2),
          ("bfdSessFailSanityCheck", 3),
          ("bfdSessFailGeneral", 4),
          ("bfdSessFailInternalProgramming", 5),
          ("bfdSessFailCvDiscrNotFound", 6),
          ("bfdSessFailMaxPacketRate", 7),
          ("bfdSessFailHandleReplaced", 8),
          ("bfdSessFailBfdDisabledOnIntf", 9),
          ("bfdSessFailConflict", 10),
          ("bfdSessFailRemDiscrInvalid", 11))
    )


_TmnxOspfBfdSessSetupFailReason_Type.__name__ = "Integer32"
_TmnxOspfBfdSessSetupFailReason_Object = MibScalar
tmnxOspfBfdSessSetupFailReason = _TmnxOspfBfdSessSetupFailReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 14),
    _TmnxOspfBfdSessSetupFailReason_Type()
)
tmnxOspfBfdSessSetupFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOspfBfdSessSetupFailReason.setStatus("current")
_TmnxOspfNotifSrgbRangeStartLbl_Type = Unsigned32
_TmnxOspfNotifSrgbRangeStartLbl_Object = MibScalar
tmnxOspfNotifSrgbRangeStartLbl = _TmnxOspfNotifSrgbRangeStartLbl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 15),
    _TmnxOspfNotifSrgbRangeStartLbl_Type()
)
tmnxOspfNotifSrgbRangeStartLbl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOspfNotifSrgbRangeStartLbl.setStatus("current")
_TmnxOspfNotifSrgbRangeMaxIdx_Type = Unsigned32
_TmnxOspfNotifSrgbRangeMaxIdx_Object = MibScalar
tmnxOspfNotifSrgbRangeMaxIdx = _TmnxOspfNotifSrgbRangeMaxIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 16),
    _TmnxOspfNotifSrgbRangeMaxIdx_Type()
)
tmnxOspfNotifSrgbRangeMaxIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOspfNotifSrgbRangeMaxIdx.setStatus("current")
_TmnxOspfNotifSrgbAdvRtrID_Type = TmnxOspfRouterIdTc
_TmnxOspfNotifSrgbAdvRtrID_Object = MibScalar
tmnxOspfNotifSrgbAdvRtrID = _TmnxOspfNotifSrgbAdvRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 17),
    _TmnxOspfNotifSrgbAdvRtrID_Type()
)
tmnxOspfNotifSrgbAdvRtrID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOspfNotifSrgbAdvRtrID.setStatus("current")
_TmnxOspfNotifSrgbAreaId_Type = TmnxOspfAreaIdTc
_TmnxOspfNotifSrgbAreaId_Object = MibScalar
tmnxOspfNotifSrgbAreaId = _TmnxOspfNotifSrgbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 18),
    _TmnxOspfNotifSrgbAreaId_Type()
)
tmnxOspfNotifSrgbAreaId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOspfNotifSrgbAreaId.setStatus("current")
_TmnxOspfNotifyIfIndex_Type = InterfaceIndex
_TmnxOspfNotifyIfIndex_Object = MibScalar
tmnxOspfNotifyIfIndex = _TmnxOspfNotifyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 19),
    _TmnxOspfNotifyIfIndex_Type()
)
tmnxOspfNotifyIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOspfNotifyIfIndex.setStatus("current")
_TmnxOspfNotifyNbrRouterId_Type = TmnxOspfRouterIdTc
_TmnxOspfNotifyNbrRouterId_Object = MibScalar
tmnxOspfNotifyNbrRouterId = _TmnxOspfNotifyNbrRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 20),
    _TmnxOspfNotifyNbrRouterId_Type()
)
tmnxOspfNotifyNbrRouterId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOspfNotifyNbrRouterId.setStatus("current")


class _TmnxOspfNotifStatsIndexStatus_Type(Integer32):
    """Custom type tmnxOspfNotifStatsIndexStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("statsIndexAllocNoError", 0),
          ("statsIndexAllocNoResource", 1))
    )


_TmnxOspfNotifStatsIndexStatus_Type.__name__ = "Integer32"
_TmnxOspfNotifStatsIndexStatus_Object = MibScalar
tmnxOspfNotifStatsIndexStatus = _TmnxOspfNotifStatsIndexStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 24, 21),
    _TmnxOspfNotifStatsIndexStatus_Type()
)
tmnxOspfNotifStatsIndexStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOspfNotifStatsIndexStatus.setStatus("current")
_TmnxOspfShamIfTable_Object = MibTable
tmnxOspfShamIfTable = _TmnxOspfShamIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25)
)
if mibBuilder.loadTexts:
    tmnxOspfShamIfTable.setStatus("current")
_TmnxOspfShamIfEntry_Object = MibTableRow
tmnxOspfShamIfEntry = _TmnxOspfShamIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1)
)
tmnxOspfShamIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfIndex"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfInstId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRemoteNbrAddrType"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRemoteNbrAddress"),
)
if mibBuilder.loadTexts:
    tmnxOspfShamIfEntry.setStatus("current")
_TmnxOspfShamIfIndex_Type = InterfaceIndex
_TmnxOspfShamIfIndex_Object = MibTableColumn
tmnxOspfShamIfIndex = _TmnxOspfShamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 1),
    _TmnxOspfShamIfIndex_Type()
)
tmnxOspfShamIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfShamIfIndex.setStatus("current")
_TmnxOspfShamIfInstId_Type = TmnxOspfIfInstIdTc
_TmnxOspfShamIfInstId_Object = MibTableColumn
tmnxOspfShamIfInstId = _TmnxOspfShamIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 2),
    _TmnxOspfShamIfInstId_Type()
)
tmnxOspfShamIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfShamIfInstId.setStatus("current")
_TmnxOspfShamIfRemoteNbrAddrType_Type = InetAddressType
_TmnxOspfShamIfRemoteNbrAddrType_Object = MibTableColumn
tmnxOspfShamIfRemoteNbrAddrType = _TmnxOspfShamIfRemoteNbrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 3),
    _TmnxOspfShamIfRemoteNbrAddrType_Type()
)
tmnxOspfShamIfRemoteNbrAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfShamIfRemoteNbrAddrType.setStatus("current")


class _TmnxOspfShamIfRemoteNbrAddress_Type(InetAddress):
    """Custom type tmnxOspfShamIfRemoteNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOspfShamIfRemoteNbrAddress_Type.__name__ = "InetAddress"
_TmnxOspfShamIfRemoteNbrAddress_Object = MibTableColumn
tmnxOspfShamIfRemoteNbrAddress = _TmnxOspfShamIfRemoteNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 4),
    _TmnxOspfShamIfRemoteNbrAddress_Type()
)
tmnxOspfShamIfRemoteNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfShamIfRemoteNbrAddress.setStatus("current")
_TmnxOspfShamIfStatus_Type = RowStatus
_TmnxOspfShamIfStatus_Object = MibTableColumn
tmnxOspfShamIfStatus = _TmnxOspfShamIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 5),
    _TmnxOspfShamIfStatus_Type()
)
tmnxOspfShamIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfShamIfStatus.setStatus("current")
_TmnxOspfShamIfLastChanged_Type = TimeStamp
_TmnxOspfShamIfLastChanged_Object = MibTableColumn
tmnxOspfShamIfLastChanged = _TmnxOspfShamIfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 6),
    _TmnxOspfShamIfLastChanged_Type()
)
tmnxOspfShamIfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfLastChanged.setStatus("current")


class _TmnxOspfShamIfAreaId_Type(TmnxOspfAreaIdTc):
    """Custom type tmnxOspfShamIfAreaId based on TmnxOspfAreaIdTc"""
    defaultValue = 0


_TmnxOspfShamIfAreaId_Type.__name__ = "TmnxOspfAreaIdTc"
_TmnxOspfShamIfAreaId_Object = MibTableColumn
tmnxOspfShamIfAreaId = _TmnxOspfShamIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 7),
    _TmnxOspfShamIfAreaId_Type()
)
tmnxOspfShamIfAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfShamIfAreaId.setStatus("current")


class _TmnxOspfShamIfAdminState_Type(Status):
    """Custom type tmnxOspfShamIfAdminState based on Status"""
    defaultValue = 1


_TmnxOspfShamIfAdminState_Type.__name__ = "Status"
_TmnxOspfShamIfAdminState_Object = MibTableColumn
tmnxOspfShamIfAdminState = _TmnxOspfShamIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 8),
    _TmnxOspfShamIfAdminState_Type()
)
tmnxOspfShamIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfShamIfAdminState.setStatus("current")


class _TmnxOspfShamIfTransitDelay_Type(TmnxOspfUpToRefreshIntervalTc):
    """Custom type tmnxOspfShamIfTransitDelay based on TmnxOspfUpToRefreshIntervalTc"""
    defaultValue = 1

    subtypeSpec = TmnxOspfUpToRefreshIntervalTc.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_TmnxOspfShamIfTransitDelay_Type.__name__ = "TmnxOspfUpToRefreshIntervalTc"
_TmnxOspfShamIfTransitDelay_Object = MibTableColumn
tmnxOspfShamIfTransitDelay = _TmnxOspfShamIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 9),
    _TmnxOspfShamIfTransitDelay_Type()
)
tmnxOspfShamIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfShamIfTransitDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfShamIfTransitDelay.setUnits("seconds")


class _TmnxOspfShamIfRetransInterval_Type(TmnxOspfUpToRefreshIntervalTc):
    """Custom type tmnxOspfShamIfRetransInterval based on TmnxOspfUpToRefreshIntervalTc"""
    defaultValue = 5

    subtypeSpec = TmnxOspfUpToRefreshIntervalTc.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_TmnxOspfShamIfRetransInterval_Type.__name__ = "TmnxOspfUpToRefreshIntervalTc"
_TmnxOspfShamIfRetransInterval_Object = MibTableColumn
tmnxOspfShamIfRetransInterval = _TmnxOspfShamIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 10),
    _TmnxOspfShamIfRetransInterval_Type()
)
tmnxOspfShamIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfShamIfRetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfShamIfRetransInterval.setUnits("seconds")


class _TmnxOspfShamIfHelloInterval_Type(HelloRange):
    """Custom type tmnxOspfShamIfHelloInterval based on HelloRange"""
    defaultValue = 10


_TmnxOspfShamIfHelloInterval_Type.__name__ = "HelloRange"
_TmnxOspfShamIfHelloInterval_Object = MibTableColumn
tmnxOspfShamIfHelloInterval = _TmnxOspfShamIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 11),
    _TmnxOspfShamIfHelloInterval_Type()
)
tmnxOspfShamIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfShamIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfShamIfHelloInterval.setUnits("seconds")


class _TmnxOspfShamIfRtrDeadInterval_Type(TmnxOspfDeadIntRangeTc):
    """Custom type tmnxOspfShamIfRtrDeadInterval based on TmnxOspfDeadIntRangeTc"""
    defaultValue = 40


_TmnxOspfShamIfRtrDeadInterval_Type.__name__ = "TmnxOspfDeadIntRangeTc"
_TmnxOspfShamIfRtrDeadInterval_Object = MibTableColumn
tmnxOspfShamIfRtrDeadInterval = _TmnxOspfShamIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 12),
    _TmnxOspfShamIfRtrDeadInterval_Type()
)
tmnxOspfShamIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfShamIfRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfShamIfRtrDeadInterval.setUnits("seconds")


class _TmnxOspfShamIfCfgMetric_Type(TmnxOspfShamIfMetricTc):
    """Custom type tmnxOspfShamIfCfgMetric based on TmnxOspfShamIfMetricTc"""
    defaultValue = 1


_TmnxOspfShamIfCfgMetric_Type.__name__ = "TmnxOspfShamIfMetricTc"
_TmnxOspfShamIfCfgMetric_Object = MibTableColumn
tmnxOspfShamIfCfgMetric = _TmnxOspfShamIfCfgMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 13),
    _TmnxOspfShamIfCfgMetric_Type()
)
tmnxOspfShamIfCfgMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfShamIfCfgMetric.setStatus("current")


class _TmnxOspfShamIfAuthType_Type(TmnxOspfAuthenticationType):
    """Custom type tmnxOspfShamIfAuthType based on TmnxOspfAuthenticationType"""
    defaultValue = 0


_TmnxOspfShamIfAuthType_Type.__name__ = "TmnxOspfAuthenticationType"
_TmnxOspfShamIfAuthType_Object = MibTableColumn
tmnxOspfShamIfAuthType = _TmnxOspfShamIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 14),
    _TmnxOspfShamIfAuthType_Type()
)
tmnxOspfShamIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfShamIfAuthType.setStatus("current")


class _TmnxOspfShamIfAuthKey_Type(OctetString):
    """Custom type tmnxOspfShamIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_TmnxOspfShamIfAuthKey_Type.__name__ = "OctetString"
_TmnxOspfShamIfAuthKey_Object = MibTableColumn
tmnxOspfShamIfAuthKey = _TmnxOspfShamIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 15),
    _TmnxOspfShamIfAuthKey_Type()
)
tmnxOspfShamIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfShamIfAuthKey.setStatus("current")


class _TmnxOspfShamIfState_Type(Integer32):
    """Custom type tmnxOspfShamIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("pointToPoint", 4))
    )


_TmnxOspfShamIfState_Type.__name__ = "Integer32"
_TmnxOspfShamIfState_Object = MibTableColumn
tmnxOspfShamIfState = _TmnxOspfShamIfState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 16),
    _TmnxOspfShamIfState_Type()
)
tmnxOspfShamIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfState.setStatus("current")
_TmnxOspfShamIfLastEnabledTime_Type = TimeStamp
_TmnxOspfShamIfLastEnabledTime_Object = MibTableColumn
tmnxOspfShamIfLastEnabledTime = _TmnxOspfShamIfLastEnabledTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 17),
    _TmnxOspfShamIfLastEnabledTime_Type()
)
tmnxOspfShamIfLastEnabledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfLastEnabledTime.setStatus("current")
_TmnxOspfShamIfLinkLsaCount_Type = Gauge32
_TmnxOspfShamIfLinkLsaCount_Object = MibTableColumn
tmnxOspfShamIfLinkLsaCount = _TmnxOspfShamIfLinkLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 18),
    _TmnxOspfShamIfLinkLsaCount_Type()
)
tmnxOspfShamIfLinkLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfLinkLsaCount.setStatus("current")
_TmnxOspfShamIfLinkLsaCksumSum_Type = Integer32
_TmnxOspfShamIfLinkLsaCksumSum_Object = MibTableColumn
tmnxOspfShamIfLinkLsaCksumSum = _TmnxOspfShamIfLinkLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 19),
    _TmnxOspfShamIfLinkLsaCksumSum_Type()
)
tmnxOspfShamIfLinkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfLinkLsaCksumSum.setStatus("current")
_TmnxOspfShamIfLinkUnkLsaCount_Type = Gauge32
_TmnxOspfShamIfLinkUnkLsaCount_Object = MibTableColumn
tmnxOspfShamIfLinkUnkLsaCount = _TmnxOspfShamIfLinkUnkLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 20),
    _TmnxOspfShamIfLinkUnkLsaCount_Type()
)
tmnxOspfShamIfLinkUnkLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfLinkUnkLsaCount.setStatus("current")
_TmnxOspfShamIfLinkUnkLsaCksumSum_Type = Integer32
_TmnxOspfShamIfLinkUnkLsaCksumSum_Object = MibTableColumn
tmnxOspfShamIfLinkUnkLsaCksumSum = _TmnxOspfShamIfLinkUnkLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 21),
    _TmnxOspfShamIfLinkUnkLsaCksumSum_Type()
)
tmnxOspfShamIfLinkUnkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfLinkUnkLsaCksumSum.setStatus("current")
_TmnxOspfShamIfMD5TransmitKeyId_Type = TmnxOspfIfMD5KeyId
_TmnxOspfShamIfMD5TransmitKeyId_Object = MibTableColumn
tmnxOspfShamIfMD5TransmitKeyId = _TmnxOspfShamIfMD5TransmitKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 22),
    _TmnxOspfShamIfMD5TransmitKeyId_Type()
)
tmnxOspfShamIfMD5TransmitKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfMD5TransmitKeyId.setStatus("current")
_TmnxOspfShamIfLocalIpAddressType_Type = InetAddressType
_TmnxOspfShamIfLocalIpAddressType_Object = MibTableColumn
tmnxOspfShamIfLocalIpAddressType = _TmnxOspfShamIfLocalIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 23),
    _TmnxOspfShamIfLocalIpAddressType_Type()
)
tmnxOspfShamIfLocalIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfLocalIpAddressType.setStatus("current")


class _TmnxOspfShamIfLocalIpAddress_Type(InetAddress):
    """Custom type tmnxOspfShamIfLocalIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxOspfShamIfLocalIpAddress_Type.__name__ = "InetAddress"
_TmnxOspfShamIfLocalIpAddress_Object = MibTableColumn
tmnxOspfShamIfLocalIpAddress = _TmnxOspfShamIfLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 24),
    _TmnxOspfShamIfLocalIpAddress_Type()
)
tmnxOspfShamIfLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfLocalIpAddress.setStatus("current")
_TmnxOspfShamIfMD5NumKeys_Type = Gauge32
_TmnxOspfShamIfMD5NumKeys_Object = MibTableColumn
tmnxOspfShamIfMD5NumKeys = _TmnxOspfShamIfMD5NumKeys_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 25),
    _TmnxOspfShamIfMD5NumKeys_Type()
)
tmnxOspfShamIfMD5NumKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfMD5NumKeys.setStatus("current")


class _TmnxOspfShamIfAuthKeyChain_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfShamIfAuthKeyChain based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfShamIfAuthKeyChain_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfShamIfAuthKeyChain_Object = MibTableColumn
tmnxOspfShamIfAuthKeyChain = _TmnxOspfShamIfAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 25, 1, 26),
    _TmnxOspfShamIfAuthKeyChain_Type()
)
tmnxOspfShamIfAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfShamIfAuthKeyChain.setStatus("current")
_TmnxOspfShamIfStatsTable_Object = MibTable
tmnxOspfShamIfStatsTable = _TmnxOspfShamIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26)
)
if mibBuilder.loadTexts:
    tmnxOspfShamIfStatsTable.setStatus("current")
_TmnxOspfShamIfStatsEntry_Object = MibTableRow
tmnxOspfShamIfStatsEntry = _TmnxOspfShamIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1)
)
if mibBuilder.loadTexts:
    tmnxOspfShamIfStatsEntry.setStatus("current")
_TmnxOspfShamIfEvents_Type = Counter32
_TmnxOspfShamIfEvents_Object = MibTableColumn
tmnxOspfShamIfEvents = _TmnxOspfShamIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 1),
    _TmnxOspfShamIfEvents_Type()
)
tmnxOspfShamIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfEvents.setStatus("current")
_TmnxOspfShamIfTxPackets_Type = Counter32
_TmnxOspfShamIfTxPackets_Object = MibTableColumn
tmnxOspfShamIfTxPackets = _TmnxOspfShamIfTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 2),
    _TmnxOspfShamIfTxPackets_Type()
)
tmnxOspfShamIfTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfTxPackets.setStatus("current")
_TmnxOspfShamIfTxHellos_Type = Counter32
_TmnxOspfShamIfTxHellos_Object = MibTableColumn
tmnxOspfShamIfTxHellos = _TmnxOspfShamIfTxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 3),
    _TmnxOspfShamIfTxHellos_Type()
)
tmnxOspfShamIfTxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfTxHellos.setStatus("current")
_TmnxOspfShamIfTxDBDs_Type = Counter32
_TmnxOspfShamIfTxDBDs_Object = MibTableColumn
tmnxOspfShamIfTxDBDs = _TmnxOspfShamIfTxDBDs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 4),
    _TmnxOspfShamIfTxDBDs_Type()
)
tmnxOspfShamIfTxDBDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfTxDBDs.setStatus("current")
_TmnxOspfShamIfTxLSRs_Type = Counter32
_TmnxOspfShamIfTxLSRs_Object = MibTableColumn
tmnxOspfShamIfTxLSRs = _TmnxOspfShamIfTxLSRs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 5),
    _TmnxOspfShamIfTxLSRs_Type()
)
tmnxOspfShamIfTxLSRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfTxLSRs.setStatus("current")
_TmnxOspfShamIfTxLSUs_Type = Counter32
_TmnxOspfShamIfTxLSUs_Object = MibTableColumn
tmnxOspfShamIfTxLSUs = _TmnxOspfShamIfTxLSUs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 6),
    _TmnxOspfShamIfTxLSUs_Type()
)
tmnxOspfShamIfTxLSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfTxLSUs.setStatus("current")
_TmnxOspfShamIfTxLSAcks_Type = Counter32
_TmnxOspfShamIfTxLSAcks_Object = MibTableColumn
tmnxOspfShamIfTxLSAcks = _TmnxOspfShamIfTxLSAcks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 7),
    _TmnxOspfShamIfTxLSAcks_Type()
)
tmnxOspfShamIfTxLSAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfTxLSAcks.setStatus("current")
_TmnxOspfShamIfRxPackets_Type = Counter32
_TmnxOspfShamIfRxPackets_Object = MibTableColumn
tmnxOspfShamIfRxPackets = _TmnxOspfShamIfRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 8),
    _TmnxOspfShamIfRxPackets_Type()
)
tmnxOspfShamIfRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfRxPackets.setStatus("current")
_TmnxOspfShamIfRxHellos_Type = Counter32
_TmnxOspfShamIfRxHellos_Object = MibTableColumn
tmnxOspfShamIfRxHellos = _TmnxOspfShamIfRxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 9),
    _TmnxOspfShamIfRxHellos_Type()
)
tmnxOspfShamIfRxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfRxHellos.setStatus("current")
_TmnxOspfShamIfRxDBDs_Type = Counter32
_TmnxOspfShamIfRxDBDs_Object = MibTableColumn
tmnxOspfShamIfRxDBDs = _TmnxOspfShamIfRxDBDs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 10),
    _TmnxOspfShamIfRxDBDs_Type()
)
tmnxOspfShamIfRxDBDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfRxDBDs.setStatus("current")
_TmnxOspfShamIfRxLSRs_Type = Counter32
_TmnxOspfShamIfRxLSRs_Object = MibTableColumn
tmnxOspfShamIfRxLSRs = _TmnxOspfShamIfRxLSRs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 11),
    _TmnxOspfShamIfRxLSRs_Type()
)
tmnxOspfShamIfRxLSRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfRxLSRs.setStatus("current")
_TmnxOspfShamIfRxLSUs_Type = Counter32
_TmnxOspfShamIfRxLSUs_Object = MibTableColumn
tmnxOspfShamIfRxLSUs = _TmnxOspfShamIfRxLSUs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 12),
    _TmnxOspfShamIfRxLSUs_Type()
)
tmnxOspfShamIfRxLSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfRxLSUs.setStatus("current")
_TmnxOspfShamIfRxLSAcks_Type = Counter32
_TmnxOspfShamIfRxLSAcks_Object = MibTableColumn
tmnxOspfShamIfRxLSAcks = _TmnxOspfShamIfRxLSAcks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 13),
    _TmnxOspfShamIfRxLSAcks_Type()
)
tmnxOspfShamIfRxLSAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfRxLSAcks.setStatus("current")
_TmnxOspfShamIfDiscardPackets_Type = Counter32
_TmnxOspfShamIfDiscardPackets_Object = MibTableColumn
tmnxOspfShamIfDiscardPackets = _TmnxOspfShamIfDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 14),
    _TmnxOspfShamIfDiscardPackets_Type()
)
tmnxOspfShamIfDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfDiscardPackets.setStatus("current")
_TmnxOspfShamIfRetransmitOuts_Type = Counter32
_TmnxOspfShamIfRetransmitOuts_Object = MibTableColumn
tmnxOspfShamIfRetransmitOuts = _TmnxOspfShamIfRetransmitOuts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 15),
    _TmnxOspfShamIfRetransmitOuts_Type()
)
tmnxOspfShamIfRetransmitOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfRetransmitOuts.setStatus("current")
_TmnxOspfShamIfBadVersions_Type = Counter32
_TmnxOspfShamIfBadVersions_Object = MibTableColumn
tmnxOspfShamIfBadVersions = _TmnxOspfShamIfBadVersions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 16),
    _TmnxOspfShamIfBadVersions_Type()
)
tmnxOspfShamIfBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfBadVersions.setStatus("current")
_TmnxOspfShamIfBadNetworks_Type = Counter32
_TmnxOspfShamIfBadNetworks_Object = MibTableColumn
tmnxOspfShamIfBadNetworks = _TmnxOspfShamIfBadNetworks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 17),
    _TmnxOspfShamIfBadNetworks_Type()
)
tmnxOspfShamIfBadNetworks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfBadNetworks.setStatus("current")
_TmnxOspfShamIfBadAreas_Type = Counter32
_TmnxOspfShamIfBadAreas_Object = MibTableColumn
tmnxOspfShamIfBadAreas = _TmnxOspfShamIfBadAreas_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 18),
    _TmnxOspfShamIfBadAreas_Type()
)
tmnxOspfShamIfBadAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfBadAreas.setStatus("current")
_TmnxOspfShamIfBadDstAddrs_Type = Counter32
_TmnxOspfShamIfBadDstAddrs_Object = MibTableColumn
tmnxOspfShamIfBadDstAddrs = _TmnxOspfShamIfBadDstAddrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 19),
    _TmnxOspfShamIfBadDstAddrs_Type()
)
tmnxOspfShamIfBadDstAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfBadDstAddrs.setStatus("current")
_TmnxOspfShamIfBadNeighbors_Type = Counter32
_TmnxOspfShamIfBadNeighbors_Object = MibTableColumn
tmnxOspfShamIfBadNeighbors = _TmnxOspfShamIfBadNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 20),
    _TmnxOspfShamIfBadNeighbors_Type()
)
tmnxOspfShamIfBadNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfBadNeighbors.setStatus("current")
_TmnxOspfShamIfBadPacketTypes_Type = Counter32
_TmnxOspfShamIfBadPacketTypes_Object = MibTableColumn
tmnxOspfShamIfBadPacketTypes = _TmnxOspfShamIfBadPacketTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 21),
    _TmnxOspfShamIfBadPacketTypes_Type()
)
tmnxOspfShamIfBadPacketTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfBadPacketTypes.setStatus("current")
_TmnxOspfShamIfLastEventTime_Type = TimeStamp
_TmnxOspfShamIfLastEventTime_Object = MibTableColumn
tmnxOspfShamIfLastEventTime = _TmnxOspfShamIfLastEventTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 22),
    _TmnxOspfShamIfLastEventTime_Type()
)
tmnxOspfShamIfLastEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfLastEventTime.setStatus("current")
_TmnxOspfShamIfBadLengths_Type = Counter32
_TmnxOspfShamIfBadLengths_Object = MibTableColumn
tmnxOspfShamIfBadLengths = _TmnxOspfShamIfBadLengths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 23),
    _TmnxOspfShamIfBadLengths_Type()
)
tmnxOspfShamIfBadLengths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfBadLengths.setStatus("current")
_TmnxOspfShamIfBadHelloIntervals_Type = Counter32
_TmnxOspfShamIfBadHelloIntervals_Object = MibTableColumn
tmnxOspfShamIfBadHelloIntervals = _TmnxOspfShamIfBadHelloIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 24),
    _TmnxOspfShamIfBadHelloIntervals_Type()
)
tmnxOspfShamIfBadHelloIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfBadHelloIntervals.setStatus("current")
_TmnxOspfShamIfBadDeadIntervals_Type = Counter32
_TmnxOspfShamIfBadDeadIntervals_Object = MibTableColumn
tmnxOspfShamIfBadDeadIntervals = _TmnxOspfShamIfBadDeadIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 25),
    _TmnxOspfShamIfBadDeadIntervals_Type()
)
tmnxOspfShamIfBadDeadIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfBadDeadIntervals.setStatus("current")
_TmnxOspfShamIfBadOptions_Type = Counter32
_TmnxOspfShamIfBadOptions_Object = MibTableColumn
tmnxOspfShamIfBadOptions = _TmnxOspfShamIfBadOptions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 26),
    _TmnxOspfShamIfBadOptions_Type()
)
tmnxOspfShamIfBadOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfBadOptions.setStatus("current")
_TmnxOspfShamIfRxBadChecksums_Type = Counter32
_TmnxOspfShamIfRxBadChecksums_Object = MibTableColumn
tmnxOspfShamIfRxBadChecksums = _TmnxOspfShamIfRxBadChecksums_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 27),
    _TmnxOspfShamIfRxBadChecksums_Type()
)
tmnxOspfShamIfRxBadChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfRxBadChecksums.setStatus("current")
_TmnxOspfShamIfBadAuthTypes_Type = Counter32
_TmnxOspfShamIfBadAuthTypes_Object = MibTableColumn
tmnxOspfShamIfBadAuthTypes = _TmnxOspfShamIfBadAuthTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 28),
    _TmnxOspfShamIfBadAuthTypes_Type()
)
tmnxOspfShamIfBadAuthTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfBadAuthTypes.setStatus("current")
_TmnxOspfShamIfAuthFailures_Type = Counter32
_TmnxOspfShamIfAuthFailures_Object = MibTableColumn
tmnxOspfShamIfAuthFailures = _TmnxOspfShamIfAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 29),
    _TmnxOspfShamIfAuthFailures_Type()
)
tmnxOspfShamIfAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfAuthFailures.setStatus("current")
_TmnxOspfShamIfTxFailures_Type = Counter32
_TmnxOspfShamIfTxFailures_Object = MibTableColumn
tmnxOspfShamIfTxFailures = _TmnxOspfShamIfTxFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 26, 1, 30),
    _TmnxOspfShamIfTxFailures_Type()
)
tmnxOspfShamIfTxFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamIfTxFailures.setStatus("current")
_TmnxOspfShamIfMD5KeyTable_Object = MibTable
tmnxOspfShamIfMD5KeyTable = _TmnxOspfShamIfMD5KeyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 27)
)
if mibBuilder.loadTexts:
    tmnxOspfShamIfMD5KeyTable.setStatus("current")
_TmnxOspfShamIfMD5KeyEntry_Object = MibTableRow
tmnxOspfShamIfMD5KeyEntry = _TmnxOspfShamIfMD5KeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 27, 1)
)
tmnxOspfShamIfMD5KeyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfIndex"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfInstId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRemoteNbrAddrType"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRemoteNbrAddress"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfMD5KeyIndex"),
)
if mibBuilder.loadTexts:
    tmnxOspfShamIfMD5KeyEntry.setStatus("current")
_TmnxOspfShamIfMD5KeyIndex_Type = TmnxOspfIfMD5KeyId
_TmnxOspfShamIfMD5KeyIndex_Object = MibTableColumn
tmnxOspfShamIfMD5KeyIndex = _TmnxOspfShamIfMD5KeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 27, 1, 1),
    _TmnxOspfShamIfMD5KeyIndex_Type()
)
tmnxOspfShamIfMD5KeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfShamIfMD5KeyIndex.setStatus("current")
_TmnxOspfShamIfMD5KeyStatus_Type = RowStatus
_TmnxOspfShamIfMD5KeyStatus_Object = MibTableColumn
tmnxOspfShamIfMD5KeyStatus = _TmnxOspfShamIfMD5KeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 27, 1, 2),
    _TmnxOspfShamIfMD5KeyStatus_Type()
)
tmnxOspfShamIfMD5KeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfShamIfMD5KeyStatus.setStatus("current")


class _TmnxOspfShamIfMD5KeyKey_Type(OctetString):
    """Custom type tmnxOspfShamIfMD5KeyKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmnxOspfShamIfMD5KeyKey_Type.__name__ = "OctetString"
_TmnxOspfShamIfMD5KeyKey_Object = MibTableColumn
tmnxOspfShamIfMD5KeyKey = _TmnxOspfShamIfMD5KeyKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 27, 1, 3),
    _TmnxOspfShamIfMD5KeyKey_Type()
)
tmnxOspfShamIfMD5KeyKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfShamIfMD5KeyKey.setStatus("current")


class _TmnxOspfShamIfMD5KeyStartTime_Type(DateAndTime):
    """Custom type tmnxOspfShamIfMD5KeyStartTime based on DateAndTime"""
    defaultHexValue = "0000000000000000000000"


_TmnxOspfShamIfMD5KeyStartTime_Type.__name__ = "DateAndTime"
_TmnxOspfShamIfMD5KeyStartTime_Object = MibTableColumn
tmnxOspfShamIfMD5KeyStartTime = _TmnxOspfShamIfMD5KeyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 27, 1, 4),
    _TmnxOspfShamIfMD5KeyStartTime_Type()
)
tmnxOspfShamIfMD5KeyStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfShamIfMD5KeyStartTime.setStatus("obsolete")


class _TmnxOspfShamIfMD5KeyStopTime_Type(DateAndTime):
    """Custom type tmnxOspfShamIfMD5KeyStopTime based on DateAndTime"""
    defaultHexValue = "0000000000000000000000"


_TmnxOspfShamIfMD5KeyStopTime_Type.__name__ = "DateAndTime"
_TmnxOspfShamIfMD5KeyStopTime_Object = MibTableColumn
tmnxOspfShamIfMD5KeyStopTime = _TmnxOspfShamIfMD5KeyStopTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 27, 1, 5),
    _TmnxOspfShamIfMD5KeyStopTime_Type()
)
tmnxOspfShamIfMD5KeyStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfShamIfMD5KeyStopTime.setStatus("obsolete")
_TmnxOspfShamNbrTable_Object = MibTable
tmnxOspfShamNbrTable = _TmnxOspfShamNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 28)
)
if mibBuilder.loadTexts:
    tmnxOspfShamNbrTable.setStatus("current")
_TmnxOspfShamNbrEntry_Object = MibTableRow
tmnxOspfShamNbrEntry = _TmnxOspfShamNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 28, 1)
)
tmnxOspfShamNbrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrIfIndex"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrIfInstId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrAddressType"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrAddress"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrRtrId"),
)
if mibBuilder.loadTexts:
    tmnxOspfShamNbrEntry.setStatus("current")
_TmnxOspfShamNbrIfIndex_Type = InterfaceIndex
_TmnxOspfShamNbrIfIndex_Object = MibTableColumn
tmnxOspfShamNbrIfIndex = _TmnxOspfShamNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 28, 1, 1),
    _TmnxOspfShamNbrIfIndex_Type()
)
tmnxOspfShamNbrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrIfIndex.setStatus("current")
_TmnxOspfShamNbrIfInstId_Type = TmnxOspfIfInstIdTc
_TmnxOspfShamNbrIfInstId_Object = MibTableColumn
tmnxOspfShamNbrIfInstId = _TmnxOspfShamNbrIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 28, 1, 2),
    _TmnxOspfShamNbrIfInstId_Type()
)
tmnxOspfShamNbrIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrIfInstId.setStatus("current")
_TmnxOspfShamNbrAddressType_Type = InetAddressType
_TmnxOspfShamNbrAddressType_Object = MibTableColumn
tmnxOspfShamNbrAddressType = _TmnxOspfShamNbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 28, 1, 3),
    _TmnxOspfShamNbrAddressType_Type()
)
tmnxOspfShamNbrAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrAddressType.setStatus("current")


class _TmnxOspfShamNbrAddress_Type(InetAddress):
    """Custom type tmnxOspfShamNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOspfShamNbrAddress_Type.__name__ = "InetAddress"
_TmnxOspfShamNbrAddress_Object = MibTableColumn
tmnxOspfShamNbrAddress = _TmnxOspfShamNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 28, 1, 4),
    _TmnxOspfShamNbrAddress_Type()
)
tmnxOspfShamNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrAddress.setStatus("current")
_TmnxOspfShamNbrRtrId_Type = TmnxOspfRouterIdTc
_TmnxOspfShamNbrRtrId_Object = MibTableColumn
tmnxOspfShamNbrRtrId = _TmnxOspfShamNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 28, 1, 5),
    _TmnxOspfShamNbrRtrId_Type()
)
tmnxOspfShamNbrRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrRtrId.setStatus("current")
_TmnxOspfShamNbrOptions_Type = Integer32
_TmnxOspfShamNbrOptions_Object = MibTableColumn
tmnxOspfShamNbrOptions = _TmnxOspfShamNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 28, 1, 6),
    _TmnxOspfShamNbrOptions_Type()
)
tmnxOspfShamNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrOptions.setStatus("current")


class _TmnxOspfShamNbrState_Type(Integer32):
    """Custom type tmnxOspfShamNbrState based on Integer32"""
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
        *(("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exchangeStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_TmnxOspfShamNbrState_Type.__name__ = "Integer32"
_TmnxOspfShamNbrState_Object = MibTableColumn
tmnxOspfShamNbrState = _TmnxOspfShamNbrState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 28, 1, 7),
    _TmnxOspfShamNbrState_Type()
)
tmnxOspfShamNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrState.setStatus("current")
_TmnxOspfShamNbrHelloSuppressed_Type = TruthValue
_TmnxOspfShamNbrHelloSuppressed_Object = MibTableColumn
tmnxOspfShamNbrHelloSuppressed = _TmnxOspfShamNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 28, 1, 8),
    _TmnxOspfShamNbrHelloSuppressed_Type()
)
tmnxOspfShamNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrHelloSuppressed.setStatus("current")
_TmnxOspfShamNbrIfId_Type = InterfaceIndexOrZero
_TmnxOspfShamNbrIfId_Object = MibTableColumn
tmnxOspfShamNbrIfId = _TmnxOspfShamNbrIfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 28, 1, 9),
    _TmnxOspfShamNbrIfId_Type()
)
tmnxOspfShamNbrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrIfId.setStatus("current")


class _TmnxOspfShamNbrRestartHelperStatus_Type(Integer32):
    """Custom type tmnxOspfShamNbrRestartHelperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notHelping", 1),
          ("helping", 2))
    )


_TmnxOspfShamNbrRestartHelperStatus_Type.__name__ = "Integer32"
_TmnxOspfShamNbrRestartHelperStatus_Object = MibTableColumn
tmnxOspfShamNbrRestartHelperStatus = _TmnxOspfShamNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 28, 1, 10),
    _TmnxOspfShamNbrRestartHelperStatus_Type()
)
tmnxOspfShamNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrRestartHelperStatus.setStatus("current")
_TmnxOspfShamNbrRestartHelperAge_Type = TmnxOspfUpToRefreshIntervalTc
_TmnxOspfShamNbrRestartHelperAge_Object = MibTableColumn
tmnxOspfShamNbrRestartHelperAge = _TmnxOspfShamNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 28, 1, 11),
    _TmnxOspfShamNbrRestartHelperAge_Type()
)
tmnxOspfShamNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrRestartHelperAge.setUnits("seconds")


class _TmnxOspfShamNbrRestartHelperExitRc_Type(Integer32):
    """Custom type tmnxOspfShamNbrRestartHelperExitRc based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_TmnxOspfShamNbrRestartHelperExitRc_Type.__name__ = "Integer32"
_TmnxOspfShamNbrRestartHelperExitRc_Object = MibTableColumn
tmnxOspfShamNbrRestartHelperExitRc = _TmnxOspfShamNbrRestartHelperExitRc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 28, 1, 12),
    _TmnxOspfShamNbrRestartHelperExitRc_Type()
)
tmnxOspfShamNbrRestartHelperExitRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrRestartHelperExitRc.setStatus("current")
_TmnxOspfShamNbrUpTime_Type = TimeInterval
_TmnxOspfShamNbrUpTime_Object = MibTableColumn
tmnxOspfShamNbrUpTime = _TmnxOspfShamNbrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 28, 1, 13),
    _TmnxOspfShamNbrUpTime_Type()
)
tmnxOspfShamNbrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrUpTime.setStatus("current")
_TmnxOspfShamNbrLastEventTime_Type = TimeStamp
_TmnxOspfShamNbrLastEventTime_Object = MibTableColumn
tmnxOspfShamNbrLastEventTime = _TmnxOspfShamNbrLastEventTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 28, 1, 14),
    _TmnxOspfShamNbrLastEventTime_Type()
)
tmnxOspfShamNbrLastEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrLastEventTime.setStatus("current")


class _TmnxOspfShamNbrDeadTmeOutstng_Type(Unsigned32):
    """Custom type tmnxOspfShamNbrDeadTmeOutstng based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxOspfShamNbrDeadTmeOutstng_Type.__name__ = "Unsigned32"
_TmnxOspfShamNbrDeadTmeOutstng_Object = MibTableColumn
tmnxOspfShamNbrDeadTmeOutstng = _TmnxOspfShamNbrDeadTmeOutstng_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 28, 1, 15),
    _TmnxOspfShamNbrDeadTmeOutstng_Type()
)
tmnxOspfShamNbrDeadTmeOutstng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrDeadTmeOutstng.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrDeadTmeOutstng.setUnits("seconds")
_TmnxOspfShamNbrLastRestartTime_Type = TimeStamp
_TmnxOspfShamNbrLastRestartTime_Object = MibTableColumn
tmnxOspfShamNbrLastRestartTime = _TmnxOspfShamNbrLastRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 28, 1, 16),
    _TmnxOspfShamNbrLastRestartTime_Type()
)
tmnxOspfShamNbrLastRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrLastRestartTime.setStatus("current")
_TmnxOspfShamNbrRestartReason_Type = TmnxOspfRestartReasonTc
_TmnxOspfShamNbrRestartReason_Object = MibTableColumn
tmnxOspfShamNbrRestartReason = _TmnxOspfShamNbrRestartReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 28, 1, 17),
    _TmnxOspfShamNbrRestartReason_Type()
)
tmnxOspfShamNbrRestartReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrRestartReason.setStatus("current")
_TmnxOspfShamNbrStatsTable_Object = MibTable
tmnxOspfShamNbrStatsTable = _TmnxOspfShamNbrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 29)
)
if mibBuilder.loadTexts:
    tmnxOspfShamNbrStatsTable.setStatus("current")
_TmnxOspfShamNbrStatsEntry_Object = MibTableRow
tmnxOspfShamNbrStatsEntry = _TmnxOspfShamNbrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 29, 1)
)
if mibBuilder.loadTexts:
    tmnxOspfShamNbrStatsEntry.setStatus("current")
_TmnxOspfShamNbrEvents_Type = Counter32
_TmnxOspfShamNbrEvents_Object = MibTableColumn
tmnxOspfShamNbrEvents = _TmnxOspfShamNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 29, 1, 1),
    _TmnxOspfShamNbrEvents_Type()
)
tmnxOspfShamNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrEvents.setStatus("current")
_TmnxOspfShamNbrLsRetransQLen_Type = Gauge32
_TmnxOspfShamNbrLsRetransQLen_Object = MibTableColumn
tmnxOspfShamNbrLsRetransQLen = _TmnxOspfShamNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 29, 1, 2),
    _TmnxOspfShamNbrLsRetransQLen_Type()
)
tmnxOspfShamNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrLsRetransQLen.setStatus("current")
_TmnxOspfShamNbrBadNbrStates_Type = Counter32
_TmnxOspfShamNbrBadNbrStates_Object = MibTableColumn
tmnxOspfShamNbrBadNbrStates = _TmnxOspfShamNbrBadNbrStates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 29, 1, 3),
    _TmnxOspfShamNbrBadNbrStates_Type()
)
tmnxOspfShamNbrBadNbrStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrBadNbrStates.setStatus("current")
_TmnxOspfShamNbrLsaInstallFail_Type = Counter32
_TmnxOspfShamNbrLsaInstallFail_Object = MibTableColumn
tmnxOspfShamNbrLsaInstallFail = _TmnxOspfShamNbrLsaInstallFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 29, 1, 4),
    _TmnxOspfShamNbrLsaInstallFail_Type()
)
tmnxOspfShamNbrLsaInstallFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrLsaInstallFail.setStatus("current")
_TmnxOspfShamNbrBadSeqNums_Type = Counter32
_TmnxOspfShamNbrBadSeqNums_Object = MibTableColumn
tmnxOspfShamNbrBadSeqNums = _TmnxOspfShamNbrBadSeqNums_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 29, 1, 5),
    _TmnxOspfShamNbrBadSeqNums_Type()
)
tmnxOspfShamNbrBadSeqNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrBadSeqNums.setStatus("current")
_TmnxOspfShamNbrBadMTUs_Type = Counter32
_TmnxOspfShamNbrBadMTUs_Object = MibTableColumn
tmnxOspfShamNbrBadMTUs = _TmnxOspfShamNbrBadMTUs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 29, 1, 6),
    _TmnxOspfShamNbrBadMTUs_Type()
)
tmnxOspfShamNbrBadMTUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrBadMTUs.setStatus("current")
_TmnxOspfShamNbrBadPackets_Type = Counter32
_TmnxOspfShamNbrBadPackets_Object = MibTableColumn
tmnxOspfShamNbrBadPackets = _TmnxOspfShamNbrBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 29, 1, 7),
    _TmnxOspfShamNbrBadPackets_Type()
)
tmnxOspfShamNbrBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrBadPackets.setStatus("current")
_TmnxOspfShamNbrLsaNotInLsdbs_Type = Counter32
_TmnxOspfShamNbrLsaNotInLsdbs_Object = MibTableColumn
tmnxOspfShamNbrLsaNotInLsdbs = _TmnxOspfShamNbrLsaNotInLsdbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 29, 1, 8),
    _TmnxOspfShamNbrLsaNotInLsdbs_Type()
)
tmnxOspfShamNbrLsaNotInLsdbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrLsaNotInLsdbs.setStatus("current")
_TmnxOspfShamNbrOptionMismatch_Type = Counter32
_TmnxOspfShamNbrOptionMismatch_Object = MibTableColumn
tmnxOspfShamNbrOptionMismatch = _TmnxOspfShamNbrOptionMismatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 29, 1, 9),
    _TmnxOspfShamNbrOptionMismatch_Type()
)
tmnxOspfShamNbrOptionMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrOptionMismatch.setStatus("current")
_TmnxOspfShamNbrDuplicates_Type = Counter32
_TmnxOspfShamNbrDuplicates_Object = MibTableColumn
tmnxOspfShamNbrDuplicates = _TmnxOspfShamNbrDuplicates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 29, 1, 10),
    _TmnxOspfShamNbrDuplicates_Type()
)
tmnxOspfShamNbrDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrDuplicates.setStatus("current")
_TmnxOspfShamNbrNumRestarts_Type = Counter32
_TmnxOspfShamNbrNumRestarts_Object = MibTableColumn
tmnxOspfShamNbrNumRestarts = _TmnxOspfShamNbrNumRestarts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 29, 1, 11),
    _TmnxOspfShamNbrNumRestarts_Type()
)
tmnxOspfShamNbrNumRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfShamNbrNumRestarts.setStatus("current")
_TmnxOspfNgLinkLsdbTable_Object = MibTable
tmnxOspfNgLinkLsdbTable = _TmnxOspfNgLinkLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 30)
)
if mibBuilder.loadTexts:
    tmnxOspfNgLinkLsdbTable.setStatus("current")
_TmnxOspfNgLinkLsdbEntry_Object = MibTableRow
tmnxOspfNgLinkLsdbEntry = _TmnxOspfNgLinkLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 30, 1)
)
tmnxOspfNgLinkLsdbEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbIfIndex"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbIfInstId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbIfAreaId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbType"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbRouterId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbLsid"),
)
if mibBuilder.loadTexts:
    tmnxOspfNgLinkLsdbEntry.setStatus("current")
_TmnxOspfNgLinkLsdbIfIndex_Type = InterfaceIndex
_TmnxOspfNgLinkLsdbIfIndex_Object = MibTableColumn
tmnxOspfNgLinkLsdbIfIndex = _TmnxOspfNgLinkLsdbIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 30, 1, 1),
    _TmnxOspfNgLinkLsdbIfIndex_Type()
)
tmnxOspfNgLinkLsdbIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfNgLinkLsdbIfIndex.setStatus("current")
_TmnxOspfNgLinkLsdbIfInstId_Type = TmnxOspfIfInstIdTc
_TmnxOspfNgLinkLsdbIfInstId_Object = MibTableColumn
tmnxOspfNgLinkLsdbIfInstId = _TmnxOspfNgLinkLsdbIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 30, 1, 2),
    _TmnxOspfNgLinkLsdbIfInstId_Type()
)
tmnxOspfNgLinkLsdbIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfNgLinkLsdbIfInstId.setStatus("current")
_TmnxOspfNgLinkLsdbIfAreaId_Type = TmnxOspfAreaIdTc
_TmnxOspfNgLinkLsdbIfAreaId_Object = MibTableColumn
tmnxOspfNgLinkLsdbIfAreaId = _TmnxOspfNgLinkLsdbIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 30, 1, 3),
    _TmnxOspfNgLinkLsdbIfAreaId_Type()
)
tmnxOspfNgLinkLsdbIfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfNgLinkLsdbIfAreaId.setStatus("current")


class _TmnxOspfNgLinkLsdbType_Type(Unsigned32):
    """Custom type tmnxOspfNgLinkLsdbType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TmnxOspfNgLinkLsdbType_Type.__name__ = "Unsigned32"
_TmnxOspfNgLinkLsdbType_Object = MibTableColumn
tmnxOspfNgLinkLsdbType = _TmnxOspfNgLinkLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 30, 1, 4),
    _TmnxOspfNgLinkLsdbType_Type()
)
tmnxOspfNgLinkLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfNgLinkLsdbType.setStatus("current")
_TmnxOspfNgLinkLsdbRouterId_Type = TmnxOspfRouterIdTc
_TmnxOspfNgLinkLsdbRouterId_Object = MibTableColumn
tmnxOspfNgLinkLsdbRouterId = _TmnxOspfNgLinkLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 30, 1, 5),
    _TmnxOspfNgLinkLsdbRouterId_Type()
)
tmnxOspfNgLinkLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfNgLinkLsdbRouterId.setStatus("current")
_TmnxOspfNgLinkLsdbLsid_Type = Unsigned32
_TmnxOspfNgLinkLsdbLsid_Object = MibTableColumn
tmnxOspfNgLinkLsdbLsid = _TmnxOspfNgLinkLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 30, 1, 6),
    _TmnxOspfNgLinkLsdbLsid_Type()
)
tmnxOspfNgLinkLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfNgLinkLsdbLsid.setStatus("current")
_TmnxOspfNgLinkLsdbSequence_Type = Integer32
_TmnxOspfNgLinkLsdbSequence_Object = MibTableColumn
tmnxOspfNgLinkLsdbSequence = _TmnxOspfNgLinkLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 30, 1, 7),
    _TmnxOspfNgLinkLsdbSequence_Type()
)
tmnxOspfNgLinkLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgLinkLsdbSequence.setStatus("current")
_TmnxOspfNgLinkLsdbAge_Type = Integer32
_TmnxOspfNgLinkLsdbAge_Object = MibTableColumn
tmnxOspfNgLinkLsdbAge = _TmnxOspfNgLinkLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 30, 1, 8),
    _TmnxOspfNgLinkLsdbAge_Type()
)
tmnxOspfNgLinkLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgLinkLsdbAge.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfNgLinkLsdbAge.setUnits("seconds")
_TmnxOspfNgLinkLsdbChecksum_Type = Integer32
_TmnxOspfNgLinkLsdbChecksum_Object = MibTableColumn
tmnxOspfNgLinkLsdbChecksum = _TmnxOspfNgLinkLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 30, 1, 9),
    _TmnxOspfNgLinkLsdbChecksum_Type()
)
tmnxOspfNgLinkLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgLinkLsdbChecksum.setStatus("current")


class _TmnxOspfNgLinkLsdbAdvertisement_Type(OctetString):
    """Custom type tmnxOspfNgLinkLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_TmnxOspfNgLinkLsdbAdvertisement_Type.__name__ = "OctetString"
_TmnxOspfNgLinkLsdbAdvertisement_Object = MibTableColumn
tmnxOspfNgLinkLsdbAdvertisement = _TmnxOspfNgLinkLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 30, 1, 10),
    _TmnxOspfNgLinkLsdbAdvertisement_Type()
)
tmnxOspfNgLinkLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgLinkLsdbAdvertisement.setStatus("current")
_TmnxOspfNgLinkLsdbTypeKnown_Type = TruthValue
_TmnxOspfNgLinkLsdbTypeKnown_Object = MibTableColumn
tmnxOspfNgLinkLsdbTypeKnown = _TmnxOspfNgLinkLsdbTypeKnown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 30, 1, 11),
    _TmnxOspfNgLinkLsdbTypeKnown_Type()
)
tmnxOspfNgLinkLsdbTypeKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgLinkLsdbTypeKnown.setStatus("current")
_TmnxOspfNgIfTable_Object = MibTable
tmnxOspfNgIfTable = _TmnxOspfNgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31)
)
if mibBuilder.loadTexts:
    tmnxOspfNgIfTable.setStatus("current")
_TmnxOspfNgIfEntry_Object = MibTableRow
tmnxOspfNgIfEntry = _TmnxOspfNgIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1)
)
tmnxOspfNgIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfIndex"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfInstId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfAreaId"),
)
if mibBuilder.loadTexts:
    tmnxOspfNgIfEntry.setStatus("current")
_TmnxOspfNgIfIndex_Type = InterfaceIndex
_TmnxOspfNgIfIndex_Object = MibTableColumn
tmnxOspfNgIfIndex = _TmnxOspfNgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 1),
    _TmnxOspfNgIfIndex_Type()
)
tmnxOspfNgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfNgIfIndex.setStatus("current")
_TmnxOspfNgIfInstId_Type = TmnxOspfIfInstIdTc
_TmnxOspfNgIfInstId_Object = MibTableColumn
tmnxOspfNgIfInstId = _TmnxOspfNgIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 2),
    _TmnxOspfNgIfInstId_Type()
)
tmnxOspfNgIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfNgIfInstId.setStatus("current")
_TmnxOspfNgIfAreaId_Type = TmnxOspfAreaIdTc
_TmnxOspfNgIfAreaId_Object = MibTableColumn
tmnxOspfNgIfAreaId = _TmnxOspfNgIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 3),
    _TmnxOspfNgIfAreaId_Type()
)
tmnxOspfNgIfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfNgIfAreaId.setStatus("current")
_TmnxOspfNgIfStatus_Type = RowStatus
_TmnxOspfNgIfStatus_Object = MibTableColumn
tmnxOspfNgIfStatus = _TmnxOspfNgIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 4),
    _TmnxOspfNgIfStatus_Type()
)
tmnxOspfNgIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfStatus.setStatus("current")
_TmnxOspfNgIfLastChanged_Type = TimeStamp
_TmnxOspfNgIfLastChanged_Object = MibTableColumn
tmnxOspfNgIfLastChanged = _TmnxOspfNgIfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 5),
    _TmnxOspfNgIfLastChanged_Type()
)
tmnxOspfNgIfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfLastChanged.setStatus("current")
_TmnxOspfNgIfCfgType_Type = TmnxOspfIfTypeTc
_TmnxOspfNgIfCfgType_Object = MibTableColumn
tmnxOspfNgIfCfgType = _TmnxOspfNgIfCfgType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 6),
    _TmnxOspfNgIfCfgType_Type()
)
tmnxOspfNgIfCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfCfgType.setStatus("current")


class _TmnxOspfNgIfAdminState_Type(Status):
    """Custom type tmnxOspfNgIfAdminState based on Status"""
    defaultValue = 1


_TmnxOspfNgIfAdminState_Type.__name__ = "Status"
_TmnxOspfNgIfAdminState_Object = MibTableColumn
tmnxOspfNgIfAdminState = _TmnxOspfNgIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 7),
    _TmnxOspfNgIfAdminState_Type()
)
tmnxOspfNgIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfAdminState.setStatus("current")


class _TmnxOspfNgIfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type tmnxOspfNgIfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_TmnxOspfNgIfRtrPriority_Type.__name__ = "DesignatedRouterPriority"
_TmnxOspfNgIfRtrPriority_Object = MibTableColumn
tmnxOspfNgIfRtrPriority = _TmnxOspfNgIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 8),
    _TmnxOspfNgIfRtrPriority_Type()
)
tmnxOspfNgIfRtrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfRtrPriority.setStatus("current")


class _TmnxOspfNgIfTransitDelay_Type(TmnxOspfUpToRefreshIntervalTc):
    """Custom type tmnxOspfNgIfTransitDelay based on TmnxOspfUpToRefreshIntervalTc"""
    defaultValue = 1

    subtypeSpec = TmnxOspfUpToRefreshIntervalTc.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_TmnxOspfNgIfTransitDelay_Type.__name__ = "TmnxOspfUpToRefreshIntervalTc"
_TmnxOspfNgIfTransitDelay_Object = MibTableColumn
tmnxOspfNgIfTransitDelay = _TmnxOspfNgIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 9),
    _TmnxOspfNgIfTransitDelay_Type()
)
tmnxOspfNgIfTransitDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfTransitDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfNgIfTransitDelay.setUnits("seconds")


class _TmnxOspfNgIfRetransInterval_Type(TmnxOspfUpToRefreshIntervalTc):
    """Custom type tmnxOspfNgIfRetransInterval based on TmnxOspfUpToRefreshIntervalTc"""
    defaultValue = 5

    subtypeSpec = TmnxOspfUpToRefreshIntervalTc.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_TmnxOspfNgIfRetransInterval_Type.__name__ = "TmnxOspfUpToRefreshIntervalTc"
_TmnxOspfNgIfRetransInterval_Object = MibTableColumn
tmnxOspfNgIfRetransInterval = _TmnxOspfNgIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 10),
    _TmnxOspfNgIfRetransInterval_Type()
)
tmnxOspfNgIfRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfRetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfNgIfRetransInterval.setUnits("seconds")


class _TmnxOspfNgIfHelloInterval_Type(HelloRange):
    """Custom type tmnxOspfNgIfHelloInterval based on HelloRange"""
    defaultValue = 10


_TmnxOspfNgIfHelloInterval_Type.__name__ = "HelloRange"
_TmnxOspfNgIfHelloInterval_Object = MibTableColumn
tmnxOspfNgIfHelloInterval = _TmnxOspfNgIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 11),
    _TmnxOspfNgIfHelloInterval_Type()
)
tmnxOspfNgIfHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfNgIfHelloInterval.setUnits("seconds")


class _TmnxOspfNgIfRtrDeadInterval_Type(TmnxOspfDeadIntRangeTc):
    """Custom type tmnxOspfNgIfRtrDeadInterval based on TmnxOspfDeadIntRangeTc"""
    defaultValue = 40


_TmnxOspfNgIfRtrDeadInterval_Type.__name__ = "TmnxOspfDeadIntRangeTc"
_TmnxOspfNgIfRtrDeadInterval_Object = MibTableColumn
tmnxOspfNgIfRtrDeadInterval = _TmnxOspfNgIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 12),
    _TmnxOspfNgIfRtrDeadInterval_Type()
)
tmnxOspfNgIfRtrDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfRtrDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfNgIfRtrDeadInterval.setUnits("seconds")


class _TmnxOspfNgIfPollInterval_Type(Unsigned32):
    """Custom type tmnxOspfNgIfPollInterval based on Unsigned32"""
    defaultValue = 120


_TmnxOspfNgIfPollInterval_Type.__name__ = "Unsigned32"
_TmnxOspfNgIfPollInterval_Object = MibTableColumn
tmnxOspfNgIfPollInterval = _TmnxOspfNgIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 13),
    _TmnxOspfNgIfPollInterval_Type()
)
tmnxOspfNgIfPollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfNgIfPollInterval.setUnits("seconds")


class _TmnxOspfNgIfCfgMTU_Type(Integer32):
    """Custom type tmnxOspfNgIfCfgMTU based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9786),
    )


_TmnxOspfNgIfCfgMTU_Type.__name__ = "Integer32"
_TmnxOspfNgIfCfgMTU_Object = MibTableColumn
tmnxOspfNgIfCfgMTU = _TmnxOspfNgIfCfgMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 14),
    _TmnxOspfNgIfCfgMTU_Type()
)
tmnxOspfNgIfCfgMTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfCfgMTU.setStatus("current")


class _TmnxOspfNgIfCfgMetric_Type(Metric):
    """Custom type tmnxOspfNgIfCfgMetric based on Metric"""
    defaultValue = 0


_TmnxOspfNgIfCfgMetric_Type.__name__ = "Metric"
_TmnxOspfNgIfCfgMetric_Object = MibTableColumn
tmnxOspfNgIfCfgMetric = _TmnxOspfNgIfCfgMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 15),
    _TmnxOspfNgIfCfgMetric_Type()
)
tmnxOspfNgIfCfgMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfCfgMetric.setStatus("current")


class _TmnxOspfNgIfPassive_Type(TruthValue):
    """Custom type tmnxOspfNgIfPassive based on TruthValue"""
    defaultValue = 2


_TmnxOspfNgIfPassive_Type.__name__ = "TruthValue"
_TmnxOspfNgIfPassive_Object = MibTableColumn
tmnxOspfNgIfPassive = _TmnxOspfNgIfPassive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 16),
    _TmnxOspfNgIfPassive_Type()
)
tmnxOspfNgIfPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfPassive.setStatus("current")


class _TmnxOspfNgIfAdvtSubnet_Type(TruthValue):
    """Custom type tmnxOspfNgIfAdvtSubnet based on TruthValue"""
    defaultValue = 1


_TmnxOspfNgIfAdvtSubnet_Type.__name__ = "TruthValue"
_TmnxOspfNgIfAdvtSubnet_Object = MibTableColumn
tmnxOspfNgIfAdvtSubnet = _TmnxOspfNgIfAdvtSubnet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 17),
    _TmnxOspfNgIfAdvtSubnet_Type()
)
tmnxOspfNgIfAdvtSubnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfAdvtSubnet.setStatus("current")


class _TmnxOspfNgIfAuthType_Type(TmnxOspfAuthenticationType):
    """Custom type tmnxOspfNgIfAuthType based on TmnxOspfAuthenticationType"""
    defaultValue = 0


_TmnxOspfNgIfAuthType_Type.__name__ = "TmnxOspfAuthenticationType"
_TmnxOspfNgIfAuthType_Object = MibTableColumn
tmnxOspfNgIfAuthType = _TmnxOspfNgIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 18),
    _TmnxOspfNgIfAuthType_Type()
)
tmnxOspfNgIfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfAuthType.setStatus("current")


class _TmnxOspfNgIfAuthKey_Type(OctetString):
    """Custom type tmnxOspfNgIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TmnxOspfNgIfAuthKey_Type.__name__ = "OctetString"
_TmnxOspfNgIfAuthKey_Object = MibTableColumn
tmnxOspfNgIfAuthKey = _TmnxOspfNgIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 19),
    _TmnxOspfNgIfAuthKey_Type()
)
tmnxOspfNgIfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfAuthKey.setStatus("current")


class _TmnxOspfNgIfEnableBfd_Type(TruthValue):
    """Custom type tmnxOspfNgIfEnableBfd based on TruthValue"""
    defaultValue = 2


_TmnxOspfNgIfEnableBfd_Type.__name__ = "TruthValue"
_TmnxOspfNgIfEnableBfd_Object = MibTableColumn
tmnxOspfNgIfEnableBfd = _TmnxOspfNgIfEnableBfd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 20),
    _TmnxOspfNgIfEnableBfd_Type()
)
tmnxOspfNgIfEnableBfd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfEnableBfd.setStatus("current")


class _TmnxOspfNgIfRemainDownOnFail_Type(TruthValue):
    """Custom type tmnxOspfNgIfRemainDownOnFail based on TruthValue"""
    defaultValue = 2


_TmnxOspfNgIfRemainDownOnFail_Type.__name__ = "TruthValue"
_TmnxOspfNgIfRemainDownOnFail_Object = MibTableColumn
tmnxOspfNgIfRemainDownOnFail = _TmnxOspfNgIfRemainDownOnFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 21),
    _TmnxOspfNgIfRemainDownOnFail_Type()
)
tmnxOspfNgIfRemainDownOnFail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfRemainDownOnFail.setStatus("current")


class _TmnxOspfNgIfInboundSAName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfNgIfInboundSAName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfNgIfInboundSAName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfNgIfInboundSAName_Object = MibTableColumn
tmnxOspfNgIfInboundSAName = _TmnxOspfNgIfInboundSAName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 22),
    _TmnxOspfNgIfInboundSAName_Type()
)
tmnxOspfNgIfInboundSAName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfInboundSAName.setStatus("current")


class _TmnxOspfNgIfOutboundSAName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfNgIfOutboundSAName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfNgIfOutboundSAName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfNgIfOutboundSAName_Object = MibTableColumn
tmnxOspfNgIfOutboundSAName = _TmnxOspfNgIfOutboundSAName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 23),
    _TmnxOspfNgIfOutboundSAName_Type()
)
tmnxOspfNgIfOutboundSAName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfOutboundSAName.setStatus("current")


class _TmnxOspfNgIfLoopfreeAltExclude_Type(TruthValue):
    """Custom type tmnxOspfNgIfLoopfreeAltExclude based on TruthValue"""
    defaultValue = 2


_TmnxOspfNgIfLoopfreeAltExclude_Type.__name__ = "TruthValue"
_TmnxOspfNgIfLoopfreeAltExclude_Object = MibTableColumn
tmnxOspfNgIfLoopfreeAltExclude = _TmnxOspfNgIfLoopfreeAltExclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 24),
    _TmnxOspfNgIfLoopfreeAltExclude_Type()
)
tmnxOspfNgIfLoopfreeAltExclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfLoopfreeAltExclude.setStatus("current")


class _TmnxOspfNgIfLsaFilterOut_Type(TmnxOspfLsaFilterOutTc):
    """Custom type tmnxOspfNgIfLsaFilterOut based on TmnxOspfLsaFilterOutTc"""
    defaultValue = 0


_TmnxOspfNgIfLsaFilterOut_Type.__name__ = "TmnxOspfLsaFilterOutTc"
_TmnxOspfNgIfLsaFilterOut_Object = MibTableColumn
tmnxOspfNgIfLsaFilterOut = _TmnxOspfNgIfLsaFilterOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 25),
    _TmnxOspfNgIfLsaFilterOut_Type()
)
tmnxOspfNgIfLsaFilterOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfLsaFilterOut.setStatus("current")


class _TmnxOspfNgIfAdvRtrCapability_Type(TruthValue):
    """Custom type tmnxOspfNgIfAdvRtrCapability based on TruthValue"""
    defaultValue = 1


_TmnxOspfNgIfAdvRtrCapability_Type.__name__ = "TruthValue"
_TmnxOspfNgIfAdvRtrCapability_Object = MibTableColumn
tmnxOspfNgIfAdvRtrCapability = _TmnxOspfNgIfAdvRtrCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 26),
    _TmnxOspfNgIfAdvRtrCapability_Type()
)
tmnxOspfNgIfAdvRtrCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfAdvRtrCapability.setStatus("current")


class _TmnxOspfNgIfAuthKeyChain_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfNgIfAuthKeyChain based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfNgIfAuthKeyChain_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfNgIfAuthKeyChain_Object = MibTableColumn
tmnxOspfNgIfAuthKeyChain = _TmnxOspfNgIfAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 27),
    _TmnxOspfNgIfAuthKeyChain_Type()
)
tmnxOspfNgIfAuthKeyChain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfAuthKeyChain.setStatus("current")


class _TmnxOspfNgIfRouteNHTemplate_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfNgIfRouteNHTemplate based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfNgIfRouteNHTemplate_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfNgIfRouteNHTemplate_Object = MibTableColumn
tmnxOspfNgIfRouteNHTemplate = _TmnxOspfNgIfRouteNHTemplate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 28),
    _TmnxOspfNgIfRouteNHTemplate_Type()
)
tmnxOspfNgIfRouteNHTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfRouteNHTemplate.setStatus("current")


class _TmnxOspfNgIfPriorityUpdate_Type(Integer32):
    """Custom type tmnxOspfNgIfPriorityUpdate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("high", 2))
    )


_TmnxOspfNgIfPriorityUpdate_Type.__name__ = "Integer32"
_TmnxOspfNgIfPriorityUpdate_Object = MibTableColumn
tmnxOspfNgIfPriorityUpdate = _TmnxOspfNgIfPriorityUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 29),
    _TmnxOspfNgIfPriorityUpdate_Type()
)
tmnxOspfNgIfPriorityUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfPriorityUpdate.setStatus("current")


class _TmnxOspfNgIfSidType_Type(Integer32):
    """Custom type tmnxOspfNgIfSidType based on Integer32"""
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
        *(("none", 0),
          ("index", 1),
          ("label", 2))
    )


_TmnxOspfNgIfSidType_Type.__name__ = "Integer32"
_TmnxOspfNgIfSidType_Object = MibTableColumn
tmnxOspfNgIfSidType = _TmnxOspfNgIfSidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 30),
    _TmnxOspfNgIfSidType_Type()
)
tmnxOspfNgIfSidType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfSidType.setStatus("current")


class _TmnxOspfNgIfSidValue_Type(Unsigned32):
    """Custom type tmnxOspfNgIfSidValue based on Unsigned32"""
    defaultValue = 0


_TmnxOspfNgIfSidValue_Type.__name__ = "Unsigned32"
_TmnxOspfNgIfSidValue_Object = MibTableColumn
tmnxOspfNgIfSidValue = _TmnxOspfNgIfSidValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 31),
    _TmnxOspfNgIfSidValue_Type()
)
tmnxOspfNgIfSidValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfSidValue.setStatus("current")


class _TmnxOspfNgIfSidProtection_Type(Integer32):
    """Custom type tmnxOspfNgIfSidProtection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TmnxOspfNgIfSidProtection_Type.__name__ = "Integer32"
_TmnxOspfNgIfSidProtection_Object = MibTableColumn
tmnxOspfNgIfSidProtection = _TmnxOspfNgIfSidProtection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 32),
    _TmnxOspfNgIfSidProtection_Type()
)
tmnxOspfNgIfSidProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfSidProtection.setStatus("current")


class _TmnxOspfNgIfSidClearNFlag_Type(TruthValue):
    """Custom type tmnxOspfNgIfSidClearNFlag based on TruthValue"""
    defaultValue = 2


_TmnxOspfNgIfSidClearNFlag_Type.__name__ = "TruthValue"
_TmnxOspfNgIfSidClearNFlag_Object = MibTableColumn
tmnxOspfNgIfSidClearNFlag = _TmnxOspfNgIfSidClearNFlag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 33),
    _TmnxOspfNgIfSidClearNFlag_Type()
)
tmnxOspfNgIfSidClearNFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfSidClearNFlag.setStatus("current")


class _TmnxOspfNgIfAdjSidType_Type(Integer32):
    """Custom type tmnxOspfNgIfAdjSidType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("label", 2))
    )


_TmnxOspfNgIfAdjSidType_Type.__name__ = "Integer32"
_TmnxOspfNgIfAdjSidType_Object = MibTableColumn
tmnxOspfNgIfAdjSidType = _TmnxOspfNgIfAdjSidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 34),
    _TmnxOspfNgIfAdjSidType_Type()
)
tmnxOspfNgIfAdjSidType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfAdjSidType.setStatus("current")


class _TmnxOspfNgIfAdjSidValue_Type(Unsigned32):
    """Custom type tmnxOspfNgIfAdjSidValue based on Unsigned32"""
    defaultValue = 0


_TmnxOspfNgIfAdjSidValue_Type.__name__ = "Unsigned32"
_TmnxOspfNgIfAdjSidValue_Object = MibTableColumn
tmnxOspfNgIfAdjSidValue = _TmnxOspfNgIfAdjSidValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 35),
    _TmnxOspfNgIfAdjSidValue_Type()
)
tmnxOspfNgIfAdjSidValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfAdjSidValue.setStatus("current")


class _TmnxOspfNgIfLBAdminWeight_Type(Unsigned32):
    """Custom type tmnxOspfNgIfLBAdminWeight based on Unsigned32"""
    defaultValue = 0


_TmnxOspfNgIfLBAdminWeight_Type.__name__ = "Unsigned32"
_TmnxOspfNgIfLBAdminWeight_Object = MibTableColumn
tmnxOspfNgIfLBAdminWeight = _TmnxOspfNgIfLBAdminWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 31, 1, 37),
    _TmnxOspfNgIfLBAdminWeight_Type()
)
tmnxOspfNgIfLBAdminWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfLBAdminWeight.setStatus("current")
_TmnxOspfNgIfOperTable_Object = MibTable
tmnxOspfNgIfOperTable = _TmnxOspfNgIfOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32)
)
if mibBuilder.loadTexts:
    tmnxOspfNgIfOperTable.setStatus("current")
_TmnxOspfNgIfOperEntry_Object = MibTableRow
tmnxOspfNgIfOperEntry = _TmnxOspfNgIfOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1)
)
if mibBuilder.loadTexts:
    tmnxOspfNgIfOperEntry.setStatus("current")


class _TmnxOspfNgIfState_Type(Integer32):
    """Custom type tmnxOspfNgIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("loopback", 2),
          ("waiting", 3),
          ("pointToPoint", 4),
          ("designatedRouter", 5),
          ("backupDesignatedRouter", 6),
          ("otherDesignatedRouter", 7))
    )


_TmnxOspfNgIfState_Type.__name__ = "Integer32"
_TmnxOspfNgIfState_Object = MibTableColumn
tmnxOspfNgIfState = _TmnxOspfNgIfState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 1),
    _TmnxOspfNgIfState_Type()
)
tmnxOspfNgIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfState.setStatus("current")
_TmnxOspfNgIfLastEnabledTime_Type = TimeStamp
_TmnxOspfNgIfLastEnabledTime_Object = MibTableColumn
tmnxOspfNgIfLastEnabledTime = _TmnxOspfNgIfLastEnabledTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 2),
    _TmnxOspfNgIfLastEnabledTime_Type()
)
tmnxOspfNgIfLastEnabledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfLastEnabledTime.setStatus("current")
_TmnxOspfNgIfOperMTU_Type = Integer32
_TmnxOspfNgIfOperMTU_Object = MibTableColumn
tmnxOspfNgIfOperMTU = _TmnxOspfNgIfOperMTU_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 3),
    _TmnxOspfNgIfOperMTU_Type()
)
tmnxOspfNgIfOperMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfOperMTU.setStatus("current")
_TmnxOspfNgIfMetricValue_Type = Metric
_TmnxOspfNgIfMetricValue_Object = MibTableColumn
tmnxOspfNgIfMetricValue = _TmnxOspfNgIfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 4),
    _TmnxOspfNgIfMetricValue_Type()
)
tmnxOspfNgIfMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfMetricValue.setStatus("current")
_TmnxOspfNgIfDRId_Type = TmnxOspfRouterIdTc
_TmnxOspfNgIfDRId_Object = MibTableColumn
tmnxOspfNgIfDRId = _TmnxOspfNgIfDRId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 5),
    _TmnxOspfNgIfDRId_Type()
)
tmnxOspfNgIfDRId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfDRId.setStatus("current")
_TmnxOspfNgIfDRIpAddrType_Type = InetAddressType
_TmnxOspfNgIfDRIpAddrType_Object = MibTableColumn
tmnxOspfNgIfDRIpAddrType = _TmnxOspfNgIfDRIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 6),
    _TmnxOspfNgIfDRIpAddrType_Type()
)
tmnxOspfNgIfDRIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfDRIpAddrType.setStatus("current")


class _TmnxOspfNgIfDRIpAddr_Type(InetAddress):
    """Custom type tmnxOspfNgIfDRIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxOspfNgIfDRIpAddr_Type.__name__ = "InetAddress"
_TmnxOspfNgIfDRIpAddr_Object = MibTableColumn
tmnxOspfNgIfDRIpAddr = _TmnxOspfNgIfDRIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 7),
    _TmnxOspfNgIfDRIpAddr_Type()
)
tmnxOspfNgIfDRIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfDRIpAddr.setStatus("current")
_TmnxOspfNgIfBDRId_Type = TmnxOspfRouterIdTc
_TmnxOspfNgIfBDRId_Object = MibTableColumn
tmnxOspfNgIfBDRId = _TmnxOspfNgIfBDRId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 8),
    _TmnxOspfNgIfBDRId_Type()
)
tmnxOspfNgIfBDRId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfBDRId.setStatus("current")
_TmnxOspfNgIfBDRIpAddrType_Type = InetAddressType
_TmnxOspfNgIfBDRIpAddrType_Object = MibTableColumn
tmnxOspfNgIfBDRIpAddrType = _TmnxOspfNgIfBDRIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 9),
    _TmnxOspfNgIfBDRIpAddrType_Type()
)
tmnxOspfNgIfBDRIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfBDRIpAddrType.setStatus("current")


class _TmnxOspfNgIfBDRIpAddr_Type(InetAddress):
    """Custom type tmnxOspfNgIfBDRIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxOspfNgIfBDRIpAddr_Type.__name__ = "InetAddress"
_TmnxOspfNgIfBDRIpAddr_Object = MibTableColumn
tmnxOspfNgIfBDRIpAddr = _TmnxOspfNgIfBDRIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 10),
    _TmnxOspfNgIfBDRIpAddr_Type()
)
tmnxOspfNgIfBDRIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfBDRIpAddr.setStatus("current")
_TmnxOspfNgIfLinkLsaCount_Type = Gauge32
_TmnxOspfNgIfLinkLsaCount_Object = MibTableColumn
tmnxOspfNgIfLinkLsaCount = _TmnxOspfNgIfLinkLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 11),
    _TmnxOspfNgIfLinkLsaCount_Type()
)
tmnxOspfNgIfLinkLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfLinkLsaCount.setStatus("current")
_TmnxOspfNgIfLinkLsaCksumSum_Type = Integer32
_TmnxOspfNgIfLinkLsaCksumSum_Object = MibTableColumn
tmnxOspfNgIfLinkLsaCksumSum = _TmnxOspfNgIfLinkLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 12),
    _TmnxOspfNgIfLinkLsaCksumSum_Type()
)
tmnxOspfNgIfLinkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfLinkLsaCksumSum.setStatus("current")
_TmnxOspfNgIfMD5TransmitKeyId_Type = TmnxOspfIfMD5KeyId
_TmnxOspfNgIfMD5TransmitKeyId_Object = MibTableColumn
tmnxOspfNgIfMD5TransmitKeyId = _TmnxOspfNgIfMD5TransmitKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 13),
    _TmnxOspfNgIfMD5TransmitKeyId_Type()
)
tmnxOspfNgIfMD5TransmitKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfMD5TransmitKeyId.setStatus("current")
_TmnxOspfNgIfLocalIpAddressType_Type = InetAddressType
_TmnxOspfNgIfLocalIpAddressType_Object = MibTableColumn
tmnxOspfNgIfLocalIpAddressType = _TmnxOspfNgIfLocalIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 14),
    _TmnxOspfNgIfLocalIpAddressType_Type()
)
tmnxOspfNgIfLocalIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfLocalIpAddressType.setStatus("current")


class _TmnxOspfNgIfLocalIpAddress_Type(InetAddress):
    """Custom type tmnxOspfNgIfLocalIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxOspfNgIfLocalIpAddress_Type.__name__ = "InetAddress"
_TmnxOspfNgIfLocalIpAddress_Object = MibTableColumn
tmnxOspfNgIfLocalIpAddress = _TmnxOspfNgIfLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 15),
    _TmnxOspfNgIfLocalIpAddress_Type()
)
tmnxOspfNgIfLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfLocalIpAddress.setStatus("current")
_TmnxOspfNgIfMD5NumKeys_Type = Gauge32
_TmnxOspfNgIfMD5NumKeys_Object = MibTableColumn
tmnxOspfNgIfMD5NumKeys = _TmnxOspfNgIfMD5NumKeys_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 16),
    _TmnxOspfNgIfMD5NumKeys_Type()
)
tmnxOspfNgIfMD5NumKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfMD5NumKeys.setStatus("current")
_TmnxOspfNgIfType_Type = TmnxOspfIfTypeTc
_TmnxOspfNgIfType_Object = MibTableColumn
tmnxOspfNgIfType = _TmnxOspfNgIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 17),
    _TmnxOspfNgIfType_Type()
)
tmnxOspfNgIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfType.setStatus("current")


class _TmnxOspfNgIfTeMetric_Type(Unsigned32):
    """Custom type tmnxOspfNgIfTeMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_TmnxOspfNgIfTeMetric_Type.__name__ = "Unsigned32"
_TmnxOspfNgIfTeMetric_Object = MibTableColumn
tmnxOspfNgIfTeMetric = _TmnxOspfNgIfTeMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 18),
    _TmnxOspfNgIfTeMetric_Type()
)
tmnxOspfNgIfTeMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfTeMetric.setStatus("current")
_TmnxOspfNgIfTeState_Type = TmnxOperState
_TmnxOspfNgIfTeState_Object = MibTableColumn
tmnxOspfNgIfTeState = _TmnxOspfNgIfTeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 19),
    _TmnxOspfNgIfTeState_Type()
)
tmnxOspfNgIfTeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfTeState.setStatus("current")
_TmnxOspfNgIfAdminGroup_Type = Unsigned32
_TmnxOspfNgIfAdminGroup_Object = MibTableColumn
tmnxOspfNgIfAdminGroup = _TmnxOspfNgIfAdminGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 20),
    _TmnxOspfNgIfAdminGroup_Type()
)
tmnxOspfNgIfAdminGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfAdminGroup.setStatus("current")
_TmnxOspfNgIfLdpSyncState_Type = TmnxOperState
_TmnxOspfNgIfLdpSyncState_Object = MibTableColumn
tmnxOspfNgIfLdpSyncState = _TmnxOspfNgIfLdpSyncState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 21),
    _TmnxOspfNgIfLdpSyncState_Type()
)
tmnxOspfNgIfLdpSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfLdpSyncState.setStatus("current")
_TmnxOspfNgIfLdpSyncMaxMetric_Type = TruthValue
_TmnxOspfNgIfLdpSyncMaxMetric_Object = MibTableColumn
tmnxOspfNgIfLdpSyncMaxMetric = _TmnxOspfNgIfLdpSyncMaxMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 22),
    _TmnxOspfNgIfLdpSyncMaxMetric_Type()
)
tmnxOspfNgIfLdpSyncMaxMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfLdpSyncMaxMetric.setStatus("current")


class _TmnxOspfNgIfLdpSyncTimerState_Type(Integer32):
    """Custom type tmnxOspfNgIfLdpSyncTimerState based on Integer32"""
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
        *(("waitForLdpAdj", 1),
          ("timerActive", 2),
          ("ldpExchgDone", 3),
          ("timerExpired", 4),
          ("manualExit", 5),
          ("disabled", 6))
    )


_TmnxOspfNgIfLdpSyncTimerState_Type.__name__ = "Integer32"
_TmnxOspfNgIfLdpSyncTimerState_Object = MibTableColumn
tmnxOspfNgIfLdpSyncTimerState = _TmnxOspfNgIfLdpSyncTimerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 23),
    _TmnxOspfNgIfLdpSyncTimerState_Type()
)
tmnxOspfNgIfLdpSyncTimerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfLdpSyncTimerState.setStatus("current")


class _TmnxOspfNgIfLdpSyncTimeLeft_Type(Unsigned32):
    """Custom type tmnxOspfNgIfLdpSyncTimeLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1800),
    )


_TmnxOspfNgIfLdpSyncTimeLeft_Type.__name__ = "Unsigned32"
_TmnxOspfNgIfLdpSyncTimeLeft_Object = MibTableColumn
tmnxOspfNgIfLdpSyncTimeLeft = _TmnxOspfNgIfLdpSyncTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 24),
    _TmnxOspfNgIfLdpSyncTimeLeft_Type()
)
tmnxOspfNgIfLdpSyncTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfLdpSyncTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfNgIfLdpSyncTimeLeft.setUnits("seconds")


class _TmnxOspfNgIfOperInbSAName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfNgIfOperInbSAName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfNgIfOperInbSAName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfNgIfOperInbSAName_Object = MibTableColumn
tmnxOspfNgIfOperInbSAName = _TmnxOspfNgIfOperInbSAName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 25),
    _TmnxOspfNgIfOperInbSAName_Type()
)
tmnxOspfNgIfOperInbSAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfOperInbSAName.setStatus("current")


class _TmnxOspfNgIfOperInbSANameTemp_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfNgIfOperInbSANameTemp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfNgIfOperInbSANameTemp_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfNgIfOperInbSANameTemp_Object = MibTableColumn
tmnxOspfNgIfOperInbSANameTemp = _TmnxOspfNgIfOperInbSANameTemp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 26),
    _TmnxOspfNgIfOperInbSANameTemp_Type()
)
tmnxOspfNgIfOperInbSANameTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfOperInbSANameTemp.setStatus("current")


class _TmnxOspfNgIfOperOutbSAName_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfNgIfOperOutbSAName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfNgIfOperOutbSAName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfNgIfOperOutbSAName_Object = MibTableColumn
tmnxOspfNgIfOperOutbSAName = _TmnxOspfNgIfOperOutbSAName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 32, 1, 27),
    _TmnxOspfNgIfOperOutbSAName_Type()
)
tmnxOspfNgIfOperOutbSAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfOperOutbSAName.setStatus("current")
_TmnxOspfNgIfStatsTable_Object = MibTable
tmnxOspfNgIfStatsTable = _TmnxOspfNgIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33)
)
if mibBuilder.loadTexts:
    tmnxOspfNgIfStatsTable.setStatus("current")
_TmnxOspfNgIfStatsEntry_Object = MibTableRow
tmnxOspfNgIfStatsEntry = _TmnxOspfNgIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1)
)
if mibBuilder.loadTexts:
    tmnxOspfNgIfStatsEntry.setStatus("current")
_TmnxOspfNgIfEvents_Type = Counter32
_TmnxOspfNgIfEvents_Object = MibTableColumn
tmnxOspfNgIfEvents = _TmnxOspfNgIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 1),
    _TmnxOspfNgIfEvents_Type()
)
tmnxOspfNgIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfEvents.setStatus("current")
_TmnxOspfNgIfTxPackets_Type = Counter32
_TmnxOspfNgIfTxPackets_Object = MibTableColumn
tmnxOspfNgIfTxPackets = _TmnxOspfNgIfTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 2),
    _TmnxOspfNgIfTxPackets_Type()
)
tmnxOspfNgIfTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfTxPackets.setStatus("current")
_TmnxOspfNgIfTxHellos_Type = Counter32
_TmnxOspfNgIfTxHellos_Object = MibTableColumn
tmnxOspfNgIfTxHellos = _TmnxOspfNgIfTxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 3),
    _TmnxOspfNgIfTxHellos_Type()
)
tmnxOspfNgIfTxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfTxHellos.setStatus("current")
_TmnxOspfNgIfTxDBDs_Type = Counter32
_TmnxOspfNgIfTxDBDs_Object = MibTableColumn
tmnxOspfNgIfTxDBDs = _TmnxOspfNgIfTxDBDs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 4),
    _TmnxOspfNgIfTxDBDs_Type()
)
tmnxOspfNgIfTxDBDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfTxDBDs.setStatus("current")
_TmnxOspfNgIfTxLSRs_Type = Counter32
_TmnxOspfNgIfTxLSRs_Object = MibTableColumn
tmnxOspfNgIfTxLSRs = _TmnxOspfNgIfTxLSRs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 5),
    _TmnxOspfNgIfTxLSRs_Type()
)
tmnxOspfNgIfTxLSRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfTxLSRs.setStatus("current")
_TmnxOspfNgIfTxLSUs_Type = Counter32
_TmnxOspfNgIfTxLSUs_Object = MibTableColumn
tmnxOspfNgIfTxLSUs = _TmnxOspfNgIfTxLSUs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 6),
    _TmnxOspfNgIfTxLSUs_Type()
)
tmnxOspfNgIfTxLSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfTxLSUs.setStatus("current")
_TmnxOspfNgIfTxLSAcks_Type = Counter32
_TmnxOspfNgIfTxLSAcks_Object = MibTableColumn
tmnxOspfNgIfTxLSAcks = _TmnxOspfNgIfTxLSAcks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 7),
    _TmnxOspfNgIfTxLSAcks_Type()
)
tmnxOspfNgIfTxLSAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfTxLSAcks.setStatus("current")
_TmnxOspfNgIfRxPackets_Type = Counter32
_TmnxOspfNgIfRxPackets_Object = MibTableColumn
tmnxOspfNgIfRxPackets = _TmnxOspfNgIfRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 8),
    _TmnxOspfNgIfRxPackets_Type()
)
tmnxOspfNgIfRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfRxPackets.setStatus("current")
_TmnxOspfNgIfRxHellos_Type = Counter32
_TmnxOspfNgIfRxHellos_Object = MibTableColumn
tmnxOspfNgIfRxHellos = _TmnxOspfNgIfRxHellos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 9),
    _TmnxOspfNgIfRxHellos_Type()
)
tmnxOspfNgIfRxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfRxHellos.setStatus("current")
_TmnxOspfNgIfRxDBDs_Type = Counter32
_TmnxOspfNgIfRxDBDs_Object = MibTableColumn
tmnxOspfNgIfRxDBDs = _TmnxOspfNgIfRxDBDs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 10),
    _TmnxOspfNgIfRxDBDs_Type()
)
tmnxOspfNgIfRxDBDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfRxDBDs.setStatus("current")
_TmnxOspfNgIfRxLSRs_Type = Counter32
_TmnxOspfNgIfRxLSRs_Object = MibTableColumn
tmnxOspfNgIfRxLSRs = _TmnxOspfNgIfRxLSRs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 11),
    _TmnxOspfNgIfRxLSRs_Type()
)
tmnxOspfNgIfRxLSRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfRxLSRs.setStatus("current")
_TmnxOspfNgIfRxLSUs_Type = Counter32
_TmnxOspfNgIfRxLSUs_Object = MibTableColumn
tmnxOspfNgIfRxLSUs = _TmnxOspfNgIfRxLSUs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 12),
    _TmnxOspfNgIfRxLSUs_Type()
)
tmnxOspfNgIfRxLSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfRxLSUs.setStatus("current")
_TmnxOspfNgIfRxLSAcks_Type = Counter32
_TmnxOspfNgIfRxLSAcks_Object = MibTableColumn
tmnxOspfNgIfRxLSAcks = _TmnxOspfNgIfRxLSAcks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 13),
    _TmnxOspfNgIfRxLSAcks_Type()
)
tmnxOspfNgIfRxLSAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfRxLSAcks.setStatus("current")
_TmnxOspfNgIfDiscardPackets_Type = Counter32
_TmnxOspfNgIfDiscardPackets_Object = MibTableColumn
tmnxOspfNgIfDiscardPackets = _TmnxOspfNgIfDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 14),
    _TmnxOspfNgIfDiscardPackets_Type()
)
tmnxOspfNgIfDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfDiscardPackets.setStatus("current")
_TmnxOspfNgIfRetransmitOuts_Type = Counter32
_TmnxOspfNgIfRetransmitOuts_Object = MibTableColumn
tmnxOspfNgIfRetransmitOuts = _TmnxOspfNgIfRetransmitOuts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 15),
    _TmnxOspfNgIfRetransmitOuts_Type()
)
tmnxOspfNgIfRetransmitOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfRetransmitOuts.setStatus("current")
_TmnxOspfNgIfBadVersions_Type = Counter32
_TmnxOspfNgIfBadVersions_Object = MibTableColumn
tmnxOspfNgIfBadVersions = _TmnxOspfNgIfBadVersions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 16),
    _TmnxOspfNgIfBadVersions_Type()
)
tmnxOspfNgIfBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfBadVersions.setStatus("current")
_TmnxOspfNgIfBadNetworks_Type = Counter32
_TmnxOspfNgIfBadNetworks_Object = MibTableColumn
tmnxOspfNgIfBadNetworks = _TmnxOspfNgIfBadNetworks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 17),
    _TmnxOspfNgIfBadNetworks_Type()
)
tmnxOspfNgIfBadNetworks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfBadNetworks.setStatus("current")
_TmnxOspfNgIfBadVirtualLinks_Type = Counter32
_TmnxOspfNgIfBadVirtualLinks_Object = MibTableColumn
tmnxOspfNgIfBadVirtualLinks = _TmnxOspfNgIfBadVirtualLinks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 18),
    _TmnxOspfNgIfBadVirtualLinks_Type()
)
tmnxOspfNgIfBadVirtualLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfBadVirtualLinks.setStatus("current")
_TmnxOspfNgIfBadAreas_Type = Counter32
_TmnxOspfNgIfBadAreas_Object = MibTableColumn
tmnxOspfNgIfBadAreas = _TmnxOspfNgIfBadAreas_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 19),
    _TmnxOspfNgIfBadAreas_Type()
)
tmnxOspfNgIfBadAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfBadAreas.setStatus("current")
_TmnxOspfNgIfBadDstAddrs_Type = Counter32
_TmnxOspfNgIfBadDstAddrs_Object = MibTableColumn
tmnxOspfNgIfBadDstAddrs = _TmnxOspfNgIfBadDstAddrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 20),
    _TmnxOspfNgIfBadDstAddrs_Type()
)
tmnxOspfNgIfBadDstAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfBadDstAddrs.setStatus("current")
_TmnxOspfNgIfBadNeighbors_Type = Counter32
_TmnxOspfNgIfBadNeighbors_Object = MibTableColumn
tmnxOspfNgIfBadNeighbors = _TmnxOspfNgIfBadNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 21),
    _TmnxOspfNgIfBadNeighbors_Type()
)
tmnxOspfNgIfBadNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfBadNeighbors.setStatus("current")
_TmnxOspfNgIfBadPacketTypes_Type = Counter32
_TmnxOspfNgIfBadPacketTypes_Object = MibTableColumn
tmnxOspfNgIfBadPacketTypes = _TmnxOspfNgIfBadPacketTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 22),
    _TmnxOspfNgIfBadPacketTypes_Type()
)
tmnxOspfNgIfBadPacketTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfBadPacketTypes.setStatus("current")
_TmnxOspfNgIfNeighborCount_Type = Integer32
_TmnxOspfNgIfNeighborCount_Object = MibTableColumn
tmnxOspfNgIfNeighborCount = _TmnxOspfNgIfNeighborCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 23),
    _TmnxOspfNgIfNeighborCount_Type()
)
tmnxOspfNgIfNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfNeighborCount.setStatus("current")
_TmnxOspfNgIfLastEventTime_Type = TimeStamp
_TmnxOspfNgIfLastEventTime_Object = MibTableColumn
tmnxOspfNgIfLastEventTime = _TmnxOspfNgIfLastEventTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 24),
    _TmnxOspfNgIfLastEventTime_Type()
)
tmnxOspfNgIfLastEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfLastEventTime.setStatus("current")
_TmnxOspfNgIfBadLengths_Type = Counter32
_TmnxOspfNgIfBadLengths_Object = MibTableColumn
tmnxOspfNgIfBadLengths = _TmnxOspfNgIfBadLengths_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 25),
    _TmnxOspfNgIfBadLengths_Type()
)
tmnxOspfNgIfBadLengths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfBadLengths.setStatus("current")
_TmnxOspfNgIfBadHelloIntervals_Type = Counter32
_TmnxOspfNgIfBadHelloIntervals_Object = MibTableColumn
tmnxOspfNgIfBadHelloIntervals = _TmnxOspfNgIfBadHelloIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 26),
    _TmnxOspfNgIfBadHelloIntervals_Type()
)
tmnxOspfNgIfBadHelloIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfBadHelloIntervals.setStatus("current")
_TmnxOspfNgIfBadDeadIntervals_Type = Counter32
_TmnxOspfNgIfBadDeadIntervals_Object = MibTableColumn
tmnxOspfNgIfBadDeadIntervals = _TmnxOspfNgIfBadDeadIntervals_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 27),
    _TmnxOspfNgIfBadDeadIntervals_Type()
)
tmnxOspfNgIfBadDeadIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfBadDeadIntervals.setStatus("current")
_TmnxOspfNgIfBadOptions_Type = Counter32
_TmnxOspfNgIfBadOptions_Object = MibTableColumn
tmnxOspfNgIfBadOptions = _TmnxOspfNgIfBadOptions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 28),
    _TmnxOspfNgIfBadOptions_Type()
)
tmnxOspfNgIfBadOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfBadOptions.setStatus("current")
_TmnxOspfNgIfRxBadChecksums_Type = Counter32
_TmnxOspfNgIfRxBadChecksums_Object = MibTableColumn
tmnxOspfNgIfRxBadChecksums = _TmnxOspfNgIfRxBadChecksums_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 29),
    _TmnxOspfNgIfRxBadChecksums_Type()
)
tmnxOspfNgIfRxBadChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfRxBadChecksums.setStatus("current")
_TmnxOspfNgIfBadAuthTypes_Type = Counter32
_TmnxOspfNgIfBadAuthTypes_Object = MibTableColumn
tmnxOspfNgIfBadAuthTypes = _TmnxOspfNgIfBadAuthTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 30),
    _TmnxOspfNgIfBadAuthTypes_Type()
)
tmnxOspfNgIfBadAuthTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfBadAuthTypes.setStatus("current")
_TmnxOspfNgIfAuthFailures_Type = Counter32
_TmnxOspfNgIfAuthFailures_Object = MibTableColumn
tmnxOspfNgIfAuthFailures = _TmnxOspfNgIfAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 31),
    _TmnxOspfNgIfAuthFailures_Type()
)
tmnxOspfNgIfAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfAuthFailures.setStatus("current")
_TmnxOspfNgIfTxFailures_Type = Counter32
_TmnxOspfNgIfTxFailures_Object = MibTableColumn
tmnxOspfNgIfTxFailures = _TmnxOspfNgIfTxFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 33, 1, 32),
    _TmnxOspfNgIfTxFailures_Type()
)
tmnxOspfNgIfTxFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgIfTxFailures.setStatus("current")
_TmnxOspfNgNbrTable_Object = MibTable
tmnxOspfNgNbrTable = _TmnxOspfNgNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34)
)
if mibBuilder.loadTexts:
    tmnxOspfNgNbrTable.setStatus("current")
_TmnxOspfNgNbrEntry_Object = MibTableRow
tmnxOspfNgNbrEntry = _TmnxOspfNgNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1)
)
tmnxOspfNgNbrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrIfIndex"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrIfInstId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrIfAreaId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrRtrId"),
)
if mibBuilder.loadTexts:
    tmnxOspfNgNbrEntry.setStatus("current")
_TmnxOspfNgNbrIfIndex_Type = InterfaceIndex
_TmnxOspfNgNbrIfIndex_Object = MibTableColumn
tmnxOspfNgNbrIfIndex = _TmnxOspfNgNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 1),
    _TmnxOspfNgNbrIfIndex_Type()
)
tmnxOspfNgNbrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrIfIndex.setStatus("current")
_TmnxOspfNgNbrIfInstId_Type = TmnxOspfIfInstIdTc
_TmnxOspfNgNbrIfInstId_Object = MibTableColumn
tmnxOspfNgNbrIfInstId = _TmnxOspfNgNbrIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 2),
    _TmnxOspfNgNbrIfInstId_Type()
)
tmnxOspfNgNbrIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrIfInstId.setStatus("current")
_TmnxOspfNgNbrIfAreaId_Type = TmnxOspfAreaIdTc
_TmnxOspfNgNbrIfAreaId_Object = MibTableColumn
tmnxOspfNgNbrIfAreaId = _TmnxOspfNgNbrIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 3),
    _TmnxOspfNgNbrIfAreaId_Type()
)
tmnxOspfNgNbrIfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrIfAreaId.setStatus("current")
_TmnxOspfNgNbrRtrId_Type = TmnxOspfRouterIdTc
_TmnxOspfNgNbrRtrId_Object = MibTableColumn
tmnxOspfNgNbrRtrId = _TmnxOspfNgNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 4),
    _TmnxOspfNgNbrRtrId_Type()
)
tmnxOspfNgNbrRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrRtrId.setStatus("current")
_TmnxOspfNgNbrAddressType_Type = InetAddressType
_TmnxOspfNgNbrAddressType_Object = MibTableColumn
tmnxOspfNgNbrAddressType = _TmnxOspfNgNbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 5),
    _TmnxOspfNgNbrAddressType_Type()
)
tmnxOspfNgNbrAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrAddressType.setStatus("current")


class _TmnxOspfNgNbrAddress_Type(InetAddress):
    """Custom type tmnxOspfNgNbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(20, 20),
    )


_TmnxOspfNgNbrAddress_Type.__name__ = "InetAddress"
_TmnxOspfNgNbrAddress_Object = MibTableColumn
tmnxOspfNgNbrAddress = _TmnxOspfNgNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 6),
    _TmnxOspfNgNbrAddress_Type()
)
tmnxOspfNgNbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrAddress.setStatus("current")
_TmnxOspfNgNbrOptions_Type = Integer32
_TmnxOspfNgNbrOptions_Object = MibTableColumn
tmnxOspfNgNbrOptions = _TmnxOspfNgNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 7),
    _TmnxOspfNgNbrOptions_Type()
)
tmnxOspfNgNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrOptions.setStatus("current")
_TmnxOspfNgNbrPriority_Type = DesignatedRouterPriority
_TmnxOspfNgNbrPriority_Object = MibTableColumn
tmnxOspfNgNbrPriority = _TmnxOspfNgNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 8),
    _TmnxOspfNgNbrPriority_Type()
)
tmnxOspfNgNbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrPriority.setStatus("current")


class _TmnxOspfNgNbrState_Type(Integer32):
    """Custom type tmnxOspfNgNbrState based on Integer32"""
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
        *(("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exchangeStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_TmnxOspfNgNbrState_Type.__name__ = "Integer32"
_TmnxOspfNgNbrState_Object = MibTableColumn
tmnxOspfNgNbrState = _TmnxOspfNgNbrState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 9),
    _TmnxOspfNgNbrState_Type()
)
tmnxOspfNgNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrState.setStatus("current")
_TmnxOspfNgNbrHelloSuppressed_Type = TruthValue
_TmnxOspfNgNbrHelloSuppressed_Object = MibTableColumn
tmnxOspfNgNbrHelloSuppressed = _TmnxOspfNgNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 10),
    _TmnxOspfNgNbrHelloSuppressed_Type()
)
tmnxOspfNgNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrHelloSuppressed.setStatus("current")
_TmnxOspfNgNbrIfId_Type = InterfaceIndexOrZero
_TmnxOspfNgNbrIfId_Object = MibTableColumn
tmnxOspfNgNbrIfId = _TmnxOspfNgNbrIfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 11),
    _TmnxOspfNgNbrIfId_Type()
)
tmnxOspfNgNbrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrIfId.setStatus("current")


class _TmnxOspfNgNbrRestartHelperStatus_Type(Integer32):
    """Custom type tmnxOspfNgNbrRestartHelperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notHelping", 1),
          ("helping", 2))
    )


_TmnxOspfNgNbrRestartHelperStatus_Type.__name__ = "Integer32"
_TmnxOspfNgNbrRestartHelperStatus_Object = MibTableColumn
tmnxOspfNgNbrRestartHelperStatus = _TmnxOspfNgNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 12),
    _TmnxOspfNgNbrRestartHelperStatus_Type()
)
tmnxOspfNgNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrRestartHelperStatus.setStatus("current")
_TmnxOspfNgNbrRestartHelperAge_Type = TmnxOspfUpToRefreshIntervalTc
_TmnxOspfNgNbrRestartHelperAge_Object = MibTableColumn
tmnxOspfNgNbrRestartHelperAge = _TmnxOspfNgNbrRestartHelperAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 13),
    _TmnxOspfNgNbrRestartHelperAge_Type()
)
tmnxOspfNgNbrRestartHelperAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrRestartHelperAge.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrRestartHelperAge.setUnits("seconds")


class _TmnxOspfNgNbrRestartHelperExitRc_Type(Integer32):
    """Custom type tmnxOspfNgNbrRestartHelperExitRc based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("timedOut", 4),
          ("topologyChanged", 5),
          ("bfdDown", 6))
    )


_TmnxOspfNgNbrRestartHelperExitRc_Type.__name__ = "Integer32"
_TmnxOspfNgNbrRestartHelperExitRc_Object = MibTableColumn
tmnxOspfNgNbrRestartHelperExitRc = _TmnxOspfNgNbrRestartHelperExitRc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 14),
    _TmnxOspfNgNbrRestartHelperExitRc_Type()
)
tmnxOspfNgNbrRestartHelperExitRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrRestartHelperExitRc.setStatus("current")
_TmnxOspfNgNbrUpTime_Type = TimeInterval
_TmnxOspfNgNbrUpTime_Object = MibTableColumn
tmnxOspfNgNbrUpTime = _TmnxOspfNgNbrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 15),
    _TmnxOspfNgNbrUpTime_Type()
)
tmnxOspfNgNbrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrUpTime.setStatus("current")
_TmnxOspfNgNbrLastEventTime_Type = TimeStamp
_TmnxOspfNgNbrLastEventTime_Object = MibTableColumn
tmnxOspfNgNbrLastEventTime = _TmnxOspfNgNbrLastEventTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 16),
    _TmnxOspfNgNbrLastEventTime_Type()
)
tmnxOspfNgNbrLastEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrLastEventTime.setStatus("current")


class _TmnxOspfNgNbrDeadTimeOutstanding_Type(Unsigned32):
    """Custom type tmnxOspfNgNbrDeadTimeOutstanding based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmnxOspfNgNbrDeadTimeOutstanding_Type.__name__ = "Unsigned32"
_TmnxOspfNgNbrDeadTimeOutstanding_Object = MibTableColumn
tmnxOspfNgNbrDeadTimeOutstanding = _TmnxOspfNgNbrDeadTimeOutstanding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 17),
    _TmnxOspfNgNbrDeadTimeOutstanding_Type()
)
tmnxOspfNgNbrDeadTimeOutstanding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrDeadTimeOutstanding.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrDeadTimeOutstanding.setUnits("seconds")
_TmnxOspfNgNbrLastRestartTime_Type = TimeStamp
_TmnxOspfNgNbrLastRestartTime_Object = MibTableColumn
tmnxOspfNgNbrLastRestartTime = _TmnxOspfNgNbrLastRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 18),
    _TmnxOspfNgNbrLastRestartTime_Type()
)
tmnxOspfNgNbrLastRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrLastRestartTime.setStatus("current")
_TmnxOspfNgNbrRestartReason_Type = TmnxOspfRestartReasonTc
_TmnxOspfNgNbrRestartReason_Object = MibTableColumn
tmnxOspfNgNbrRestartReason = _TmnxOspfNgNbrRestartReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 19),
    _TmnxOspfNgNbrRestartReason_Type()
)
tmnxOspfNgNbrRestartReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrRestartReason.setStatus("current")
_TmnxOspfNgNbrBfdTracking_Type = TruthValue
_TmnxOspfNgNbrBfdTracking_Object = MibTableColumn
tmnxOspfNgNbrBfdTracking = _TmnxOspfNgNbrBfdTracking_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 20),
    _TmnxOspfNgNbrBfdTracking_Type()
)
tmnxOspfNgNbrBfdTracking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrBfdTracking.setStatus("current")
_TmnxOspfNgNbrDrId_Type = TmnxOspfRouterIdTc
_TmnxOspfNgNbrDrId_Object = MibTableColumn
tmnxOspfNgNbrDrId = _TmnxOspfNgNbrDrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 21),
    _TmnxOspfNgNbrDrId_Type()
)
tmnxOspfNgNbrDrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrDrId.setStatus("current")
_TmnxOspfNgNbrBdrId_Type = TmnxOspfRouterIdTc
_TmnxOspfNgNbrBdrId_Object = MibTableColumn
tmnxOspfNgNbrBdrId = _TmnxOspfNgNbrBdrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 22),
    _TmnxOspfNgNbrBdrId_Type()
)
tmnxOspfNgNbrBdrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrBdrId.setStatus("current")


class _TmnxOspfNgNbrSidType_Type(Integer32):
    """Custom type tmnxOspfNgNbrSidType based on Integer32"""
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
        *(("none", 0),
          ("index", 1),
          ("mplsLabel", 2))
    )


_TmnxOspfNgNbrSidType_Type.__name__ = "Integer32"
_TmnxOspfNgNbrSidType_Object = MibTableColumn
tmnxOspfNgNbrSidType = _TmnxOspfNgNbrSidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 23),
    _TmnxOspfNgNbrSidType_Type()
)
tmnxOspfNgNbrSidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrSidType.setStatus("current")


class _TmnxOspfNgNbrSidValue_Type(Unsigned32):
    """Custom type tmnxOspfNgNbrSidValue based on Unsigned32"""
    defaultValue = 0


_TmnxOspfNgNbrSidValue_Type.__name__ = "Unsigned32"
_TmnxOspfNgNbrSidValue_Object = MibTableColumn
tmnxOspfNgNbrSidValue = _TmnxOspfNgNbrSidValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 34, 1, 24),
    _TmnxOspfNgNbrSidValue_Type()
)
tmnxOspfNgNbrSidValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrSidValue.setStatus("current")
_TmnxOspfNgNbrStatsTable_Object = MibTable
tmnxOspfNgNbrStatsTable = _TmnxOspfNgNbrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 35)
)
if mibBuilder.loadTexts:
    tmnxOspfNgNbrStatsTable.setStatus("current")
_TmnxOspfNgNbrStatsEntry_Object = MibTableRow
tmnxOspfNgNbrStatsEntry = _TmnxOspfNgNbrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 35, 1)
)
if mibBuilder.loadTexts:
    tmnxOspfNgNbrStatsEntry.setStatus("current")
_TmnxOspfNgNbrEvents_Type = Counter32
_TmnxOspfNgNbrEvents_Object = MibTableColumn
tmnxOspfNgNbrEvents = _TmnxOspfNgNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 35, 1, 1),
    _TmnxOspfNgNbrEvents_Type()
)
tmnxOspfNgNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrEvents.setStatus("current")
_TmnxOspfNgNbrLsRetransQLen_Type = Gauge32
_TmnxOspfNgNbrLsRetransQLen_Object = MibTableColumn
tmnxOspfNgNbrLsRetransQLen = _TmnxOspfNgNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 35, 1, 2),
    _TmnxOspfNgNbrLsRetransQLen_Type()
)
tmnxOspfNgNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrLsRetransQLen.setStatus("current")
_TmnxOspfNgNbrBadNbrStates_Type = Counter32
_TmnxOspfNgNbrBadNbrStates_Object = MibTableColumn
tmnxOspfNgNbrBadNbrStates = _TmnxOspfNgNbrBadNbrStates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 35, 1, 3),
    _TmnxOspfNgNbrBadNbrStates_Type()
)
tmnxOspfNgNbrBadNbrStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrBadNbrStates.setStatus("current")
_TmnxOspfNgNbrLsaInstallFailed_Type = Counter32
_TmnxOspfNgNbrLsaInstallFailed_Object = MibTableColumn
tmnxOspfNgNbrLsaInstallFailed = _TmnxOspfNgNbrLsaInstallFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 35, 1, 4),
    _TmnxOspfNgNbrLsaInstallFailed_Type()
)
tmnxOspfNgNbrLsaInstallFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrLsaInstallFailed.setStatus("current")
_TmnxOspfNgNbrBadSeqNums_Type = Counter32
_TmnxOspfNgNbrBadSeqNums_Object = MibTableColumn
tmnxOspfNgNbrBadSeqNums = _TmnxOspfNgNbrBadSeqNums_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 35, 1, 5),
    _TmnxOspfNgNbrBadSeqNums_Type()
)
tmnxOspfNgNbrBadSeqNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrBadSeqNums.setStatus("current")
_TmnxOspfNgNbrBadMTUs_Type = Counter32
_TmnxOspfNgNbrBadMTUs_Object = MibTableColumn
tmnxOspfNgNbrBadMTUs = _TmnxOspfNgNbrBadMTUs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 35, 1, 6),
    _TmnxOspfNgNbrBadMTUs_Type()
)
tmnxOspfNgNbrBadMTUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrBadMTUs.setStatus("current")
_TmnxOspfNgNbrBadPackets_Type = Counter32
_TmnxOspfNgNbrBadPackets_Object = MibTableColumn
tmnxOspfNgNbrBadPackets = _TmnxOspfNgNbrBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 35, 1, 7),
    _TmnxOspfNgNbrBadPackets_Type()
)
tmnxOspfNgNbrBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrBadPackets.setStatus("current")
_TmnxOspfNgNbrLsaNotInLsdbs_Type = Counter32
_TmnxOspfNgNbrLsaNotInLsdbs_Object = MibTableColumn
tmnxOspfNgNbrLsaNotInLsdbs = _TmnxOspfNgNbrLsaNotInLsdbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 35, 1, 8),
    _TmnxOspfNgNbrLsaNotInLsdbs_Type()
)
tmnxOspfNgNbrLsaNotInLsdbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrLsaNotInLsdbs.setStatus("current")
_TmnxOspfNgNbrOptionMismatches_Type = Counter32
_TmnxOspfNgNbrOptionMismatches_Object = MibTableColumn
tmnxOspfNgNbrOptionMismatches = _TmnxOspfNgNbrOptionMismatches_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 35, 1, 9),
    _TmnxOspfNgNbrOptionMismatches_Type()
)
tmnxOspfNgNbrOptionMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrOptionMismatches.setStatus("current")
_TmnxOspfNgNbrDuplicates_Type = Counter32
_TmnxOspfNgNbrDuplicates_Object = MibTableColumn
tmnxOspfNgNbrDuplicates = _TmnxOspfNgNbrDuplicates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 35, 1, 10),
    _TmnxOspfNgNbrDuplicates_Type()
)
tmnxOspfNgNbrDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrDuplicates.setStatus("current")
_TmnxOspfNgNbrNumRestarts_Type = Counter32
_TmnxOspfNgNbrNumRestarts_Object = MibTableColumn
tmnxOspfNgNbrNumRestarts = _TmnxOspfNgNbrNumRestarts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 35, 1, 11),
    _TmnxOspfNgNbrNumRestarts_Type()
)
tmnxOspfNgNbrNumRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfNgNbrNumRestarts.setStatus("current")
_TmnxOspfNgIfMD5KeyTable_Object = MibTable
tmnxOspfNgIfMD5KeyTable = _TmnxOspfNgIfMD5KeyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 36)
)
if mibBuilder.loadTexts:
    tmnxOspfNgIfMD5KeyTable.setStatus("current")
_TmnxOspfNgIfMD5KeyEntry_Object = MibTableRow
tmnxOspfNgIfMD5KeyEntry = _TmnxOspfNgIfMD5KeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 36, 1)
)
tmnxOspfNgIfMD5KeyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfIndex"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfInstId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfAreaId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfMD5KeyIndex"),
)
if mibBuilder.loadTexts:
    tmnxOspfNgIfMD5KeyEntry.setStatus("current")
_TmnxOspfNgIfMD5KeyIndex_Type = TmnxOspfIfMD5KeyId
_TmnxOspfNgIfMD5KeyIndex_Object = MibTableColumn
tmnxOspfNgIfMD5KeyIndex = _TmnxOspfNgIfMD5KeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 36, 1, 1),
    _TmnxOspfNgIfMD5KeyIndex_Type()
)
tmnxOspfNgIfMD5KeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfNgIfMD5KeyIndex.setStatus("current")
_TmnxOspfNgIfMD5KeyStatus_Type = RowStatus
_TmnxOspfNgIfMD5KeyStatus_Object = MibTableColumn
tmnxOspfNgIfMD5KeyStatus = _TmnxOspfNgIfMD5KeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 36, 1, 2),
    _TmnxOspfNgIfMD5KeyStatus_Type()
)
tmnxOspfNgIfMD5KeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfMD5KeyStatus.setStatus("current")


class _TmnxOspfNgIfMD5KeyKey_Type(OctetString):
    """Custom type tmnxOspfNgIfMD5KeyKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmnxOspfNgIfMD5KeyKey_Type.__name__ = "OctetString"
_TmnxOspfNgIfMD5KeyKey_Object = MibTableColumn
tmnxOspfNgIfMD5KeyKey = _TmnxOspfNgIfMD5KeyKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 36, 1, 3),
    _TmnxOspfNgIfMD5KeyKey_Type()
)
tmnxOspfNgIfMD5KeyKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfMD5KeyKey.setStatus("current")


class _TmnxOspfNgIfMD5KeyStartTime_Type(DateAndTime):
    """Custom type tmnxOspfNgIfMD5KeyStartTime based on DateAndTime"""
    defaultHexValue = "0000000000000000000000"


_TmnxOspfNgIfMD5KeyStartTime_Type.__name__ = "DateAndTime"
_TmnxOspfNgIfMD5KeyStartTime_Object = MibTableColumn
tmnxOspfNgIfMD5KeyStartTime = _TmnxOspfNgIfMD5KeyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 36, 1, 4),
    _TmnxOspfNgIfMD5KeyStartTime_Type()
)
tmnxOspfNgIfMD5KeyStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfMD5KeyStartTime.setStatus("obsolete")


class _TmnxOspfNgIfMD5KeyStopTime_Type(DateAndTime):
    """Custom type tmnxOspfNgIfMD5KeyStopTime based on DateAndTime"""
    defaultHexValue = "0000000000000000000000"


_TmnxOspfNgIfMD5KeyStopTime_Type.__name__ = "DateAndTime"
_TmnxOspfNgIfMD5KeyStopTime_Object = MibTableColumn
tmnxOspfNgIfMD5KeyStopTime = _TmnxOspfNgIfMD5KeyStopTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 36, 1, 5),
    _TmnxOspfNgIfMD5KeyStopTime_Type()
)
tmnxOspfNgIfMD5KeyStopTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfNgIfMD5KeyStopTime.setStatus("obsolete")
_TmnxOspfLfaStatsTable_Object = MibTable
tmnxOspfLfaStatsTable = _TmnxOspfLfaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 37)
)
if mibBuilder.loadTexts:
    tmnxOspfLfaStatsTable.setStatus("current")
_TmnxOspfLfaStatsEntry_Object = MibTableRow
tmnxOspfLfaStatsEntry = _TmnxOspfLfaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 37, 1)
)
tmnxOspfLfaStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaId"),
)
if mibBuilder.loadTexts:
    tmnxOspfLfaStatsEntry.setStatus("current")
_TmnxOspfLfaNodesCovered_Type = Gauge32
_TmnxOspfLfaNodesCovered_Object = MibTableColumn
tmnxOspfLfaNodesCovered = _TmnxOspfLfaNodesCovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 37, 1, 1),
    _TmnxOspfLfaNodesCovered_Type()
)
tmnxOspfLfaNodesCovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLfaNodesCovered.setStatus("current")
_TmnxOspfLfaTotalNodes_Type = Gauge32
_TmnxOspfLfaTotalNodes_Object = MibTableColumn
tmnxOspfLfaTotalNodes = _TmnxOspfLfaTotalNodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 37, 1, 2),
    _TmnxOspfLfaTotalNodes_Type()
)
tmnxOspfLfaTotalNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLfaTotalNodes.setStatus("current")


class _TmnxOspfLfaCoverage_Type(Gauge32):
    """Custom type tmnxOspfLfaCoverage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxOspfLfaCoverage_Type.__name__ = "Gauge32"
_TmnxOspfLfaCoverage_Object = MibTableColumn
tmnxOspfLfaCoverage = _TmnxOspfLfaCoverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 37, 1, 3),
    _TmnxOspfLfaCoverage_Type()
)
tmnxOspfLfaCoverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLfaCoverage.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfLfaCoverage.setUnits("percent")
_TmnxOspfLfaPfxCovered_Type = Gauge32
_TmnxOspfLfaPfxCovered_Object = MibTableColumn
tmnxOspfLfaPfxCovered = _TmnxOspfLfaPfxCovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 37, 1, 4),
    _TmnxOspfLfaPfxCovered_Type()
)
tmnxOspfLfaPfxCovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLfaPfxCovered.setStatus("current")
_TmnxOspfLfaTotalPfx_Type = Gauge32
_TmnxOspfLfaTotalPfx_Object = MibTableColumn
tmnxOspfLfaTotalPfx = _TmnxOspfLfaTotalPfx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 37, 1, 5),
    _TmnxOspfLfaTotalPfx_Type()
)
tmnxOspfLfaTotalPfx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLfaTotalPfx.setStatus("current")


class _TmnxOspfLfaPfxCoverage_Type(Gauge32):
    """Custom type tmnxOspfLfaPfxCoverage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxOspfLfaPfxCoverage_Type.__name__ = "Gauge32"
_TmnxOspfLfaPfxCoverage_Object = MibTableColumn
tmnxOspfLfaPfxCoverage = _TmnxOspfLfaPfxCoverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 37, 1, 6),
    _TmnxOspfLfaPfxCoverage_Type()
)
tmnxOspfLfaPfxCoverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfLfaPfxCoverage.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfLfaPfxCoverage.setUnits("percent")
_TmnxOspfPathTable_Object = MibTable
tmnxOspfPathTable = _TmnxOspfPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 38)
)
if mibBuilder.loadTexts:
    tmnxOspfPathTable.setStatus("current")
_TmnxOspfPathEntry_Object = MibTableRow
tmnxOspfPathEntry = _TmnxOspfPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 38, 1)
)
tmnxOspfPathEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfPathDestRouterId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfPathIfIndex"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfPathNhopRouterId"),
)
if mibBuilder.loadTexts:
    tmnxOspfPathEntry.setStatus("current")
_TmnxOspfPathDestRouterId_Type = TmnxOspfRouterIdTc
_TmnxOspfPathDestRouterId_Object = MibTableColumn
tmnxOspfPathDestRouterId = _TmnxOspfPathDestRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 38, 1, 1),
    _TmnxOspfPathDestRouterId_Type()
)
tmnxOspfPathDestRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfPathDestRouterId.setStatus("current")
_TmnxOspfPathIfIndex_Type = InterfaceIndex
_TmnxOspfPathIfIndex_Object = MibTableColumn
tmnxOspfPathIfIndex = _TmnxOspfPathIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 38, 1, 2),
    _TmnxOspfPathIfIndex_Type()
)
tmnxOspfPathIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfPathIfIndex.setStatus("current")
_TmnxOspfPathNhopRouterId_Type = TmnxOspfRouterIdTc
_TmnxOspfPathNhopRouterId_Object = MibTableColumn
tmnxOspfPathNhopRouterId = _TmnxOspfPathNhopRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 38, 1, 3),
    _TmnxOspfPathNhopRouterId_Type()
)
tmnxOspfPathNhopRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfPathNhopRouterId.setStatus("current")
_TmnxOspfPathMetric_Type = Unsigned32
_TmnxOspfPathMetric_Object = MibTableColumn
tmnxOspfPathMetric = _TmnxOspfPathMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 38, 1, 4),
    _TmnxOspfPathMetric_Type()
)
tmnxOspfPathMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfPathMetric.setStatus("current")
_TmnxOspfPathLfaIfIndex_Type = InterfaceIndexOrZero
_TmnxOspfPathLfaIfIndex_Object = MibTableColumn
tmnxOspfPathLfaIfIndex = _TmnxOspfPathLfaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 38, 1, 5),
    _TmnxOspfPathLfaIfIndex_Type()
)
tmnxOspfPathLfaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfPathLfaIfIndex.setStatus("current")


class _TmnxOspfPathLfaType_Type(Integer32):
    """Custom type tmnxOspfPathLfaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noProtection", 0),
          ("nodeProtection", 1),
          ("linkProtection", 2))
    )


_TmnxOspfPathLfaType_Type.__name__ = "Integer32"
_TmnxOspfPathLfaType_Object = MibTableColumn
tmnxOspfPathLfaType = _TmnxOspfPathLfaType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 38, 1, 6),
    _TmnxOspfPathLfaType_Type()
)
tmnxOspfPathLfaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfPathLfaType.setStatus("current")
_TmnxOspfPathLfaNhopRouterId_Type = TmnxOspfRouterIdTc
_TmnxOspfPathLfaNhopRouterId_Object = MibTableColumn
tmnxOspfPathLfaNhopRouterId = _TmnxOspfPathLfaNhopRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 38, 1, 7),
    _TmnxOspfPathLfaNhopRouterId_Type()
)
tmnxOspfPathLfaNhopRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfPathLfaNhopRouterId.setStatus("current")
_TmnxOspfPathLfaMetric_Type = Unsigned32
_TmnxOspfPathLfaMetric_Object = MibTableColumn
tmnxOspfPathLfaMetric = _TmnxOspfPathLfaMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 38, 1, 8),
    _TmnxOspfPathLfaMetric_Type()
)
tmnxOspfPathLfaMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfPathLfaMetric.setStatus("current")
_TmnxOspfPathNhOwner_Type = TmnxInetCidrNextHopOwner
_TmnxOspfPathNhOwner_Object = MibTableColumn
tmnxOspfPathNhOwner = _TmnxOspfPathNhOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 38, 1, 9),
    _TmnxOspfPathNhOwner_Type()
)
tmnxOspfPathNhOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfPathNhOwner.setStatus("current")
_TmnxOspfPathLfaNhOwner_Type = TmnxInetCidrNextHopOwner
_TmnxOspfPathLfaNhOwner_Object = MibTableColumn
tmnxOspfPathLfaNhOwner = _TmnxOspfPathLfaNhOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 38, 1, 10),
    _TmnxOspfPathLfaNhOwner_Type()
)
tmnxOspfPathLfaNhOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfPathLfaNhOwner.setStatus("current")
_TmnxOspfGeneralExTable_Object = MibTable
tmnxOspfGeneralExTable = _TmnxOspfGeneralExTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39)
)
if mibBuilder.loadTexts:
    tmnxOspfGeneralExTable.setStatus("current")
_TmnxOspfGeneralExEntry_Object = MibTableRow
tmnxOspfGeneralExEntry = _TmnxOspfGeneralExEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1)
)
if mibBuilder.loadTexts:
    tmnxOspfGeneralExEntry.setStatus("current")
_TmnxOspfGeneralExLastChanged_Type = TimeStamp
_TmnxOspfGeneralExLastChanged_Object = MibTableColumn
tmnxOspfGeneralExLastChanged = _TmnxOspfGeneralExLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 1),
    _TmnxOspfGeneralExLastChanged_Type()
)
tmnxOspfGeneralExLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfGeneralExLastChanged.setStatus("current")


class _TmnxOspfAdvRtrCapability_Type(Integer32):
    """Custom type tmnxOspfAdvRtrCapability based on Integer32"""
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
        *(("disable", 0),
          ("link", 1),
          ("area", 2),
          ("as", 3))
    )


_TmnxOspfAdvRtrCapability_Type.__name__ = "Integer32"
_TmnxOspfAdvRtrCapability_Object = MibTableColumn
tmnxOspfAdvRtrCapability = _TmnxOspfAdvRtrCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 2),
    _TmnxOspfAdvRtrCapability_Type()
)
tmnxOspfAdvRtrCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAdvRtrCapability.setStatus("current")


class _TmnxOspfLFAExcludePolicy1_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfLFAExcludePolicy1 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfLFAExcludePolicy1_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfLFAExcludePolicy1_Object = MibTableColumn
tmnxOspfLFAExcludePolicy1 = _TmnxOspfLFAExcludePolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 3),
    _TmnxOspfLFAExcludePolicy1_Type()
)
tmnxOspfLFAExcludePolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfLFAExcludePolicy1.setStatus("current")


class _TmnxOspfLFAExcludePolicy2_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfLFAExcludePolicy2 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfLFAExcludePolicy2_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfLFAExcludePolicy2_Object = MibTableColumn
tmnxOspfLFAExcludePolicy2 = _TmnxOspfLFAExcludePolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 4),
    _TmnxOspfLFAExcludePolicy2_Type()
)
tmnxOspfLFAExcludePolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfLFAExcludePolicy2.setStatus("current")


class _TmnxOspfLFAExcludePolicy3_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfLFAExcludePolicy3 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfLFAExcludePolicy3_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfLFAExcludePolicy3_Object = MibTableColumn
tmnxOspfLFAExcludePolicy3 = _TmnxOspfLFAExcludePolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 5),
    _TmnxOspfLFAExcludePolicy3_Type()
)
tmnxOspfLFAExcludePolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfLFAExcludePolicy3.setStatus("current")


class _TmnxOspfLFAExcludePolicy4_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfLFAExcludePolicy4 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfLFAExcludePolicy4_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfLFAExcludePolicy4_Object = MibTableColumn
tmnxOspfLFAExcludePolicy4 = _TmnxOspfLFAExcludePolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 6),
    _TmnxOspfLFAExcludePolicy4_Type()
)
tmnxOspfLFAExcludePolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfLFAExcludePolicy4.setStatus("current")


class _TmnxOspfLFAExcludePolicy5_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfLFAExcludePolicy5 based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfLFAExcludePolicy5_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfLFAExcludePolicy5_Object = MibTableColumn
tmnxOspfLFAExcludePolicy5 = _TmnxOspfLFAExcludePolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 7),
    _TmnxOspfLFAExcludePolicy5_Type()
)
tmnxOspfLFAExcludePolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfLFAExcludePolicy5.setStatus("current")


class _TmnxOspfRibPriorityListHigh_Type(TNamedItemOrEmpty):
    """Custom type tmnxOspfRibPriorityListHigh based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfRibPriorityListHigh_Type.__name__ = "TNamedItemOrEmpty"
_TmnxOspfRibPriorityListHigh_Object = MibTableColumn
tmnxOspfRibPriorityListHigh = _TmnxOspfRibPriorityListHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 8),
    _TmnxOspfRibPriorityListHigh_Type()
)
tmnxOspfRibPriorityListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfRibPriorityListHigh.setStatus("current")


class _TmnxOspfPrefixSidRangeType_Type(Integer32):
    """Custom type tmnxOspfPrefixSidRangeType based on Integer32"""
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
        *(("none", 0),
          ("global", 1),
          ("local", 2))
    )


_TmnxOspfPrefixSidRangeType_Type.__name__ = "Integer32"
_TmnxOspfPrefixSidRangeType_Object = MibTableColumn
tmnxOspfPrefixSidRangeType = _TmnxOspfPrefixSidRangeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 9),
    _TmnxOspfPrefixSidRangeType_Type()
)
tmnxOspfPrefixSidRangeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfPrefixSidRangeType.setStatus("current")


class _TmnxOspfPrefixSidRangeStartLabel_Type(Unsigned32):
    """Custom type tmnxOspfPrefixSidRangeStartLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 524287),
    )


_TmnxOspfPrefixSidRangeStartLabel_Type.__name__ = "Unsigned32"
_TmnxOspfPrefixSidRangeStartLabel_Object = MibTableColumn
tmnxOspfPrefixSidRangeStartLabel = _TmnxOspfPrefixSidRangeStartLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 10),
    _TmnxOspfPrefixSidRangeStartLabel_Type()
)
tmnxOspfPrefixSidRangeStartLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfPrefixSidRangeStartLabel.setStatus("current")


class _TmnxOspfPrefixSidRangeMaxIdx_Type(Unsigned32):
    """Custom type tmnxOspfPrefixSidRangeMaxIdx based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 524287),
    )


_TmnxOspfPrefixSidRangeMaxIdx_Type.__name__ = "Unsigned32"
_TmnxOspfPrefixSidRangeMaxIdx_Object = MibTableColumn
tmnxOspfPrefixSidRangeMaxIdx = _TmnxOspfPrefixSidRangeMaxIdx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 11),
    _TmnxOspfPrefixSidRangeMaxIdx_Type()
)
tmnxOspfPrefixSidRangeMaxIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfPrefixSidRangeMaxIdx.setStatus("current")


class _TmnxOspfSrAdminState_Type(TmnxAdminState):
    """Custom type tmnxOspfSrAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxOspfSrAdminState_Type.__name__ = "TmnxAdminState"
_TmnxOspfSrAdminState_Object = MibTableColumn
tmnxOspfSrAdminState = _TmnxOspfSrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 12),
    _TmnxOspfSrAdminState_Type()
)
tmnxOspfSrAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfSrAdminState.setStatus("current")


class _TmnxOspfTunnelTablePreference_Type(Unsigned32):
    """Custom type tmnxOspfTunnelTablePreference based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxOspfTunnelTablePreference_Type.__name__ = "Unsigned32"
_TmnxOspfTunnelTablePreference_Object = MibTableColumn
tmnxOspfTunnelTablePreference = _TmnxOspfTunnelTablePreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 13),
    _TmnxOspfTunnelTablePreference_Type()
)
tmnxOspfTunnelTablePreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfTunnelTablePreference.setStatus("current")


class _TmnxOspfRemoteLFA_Type(TruthValue):
    """Custom type tmnxOspfRemoteLFA based on TruthValue"""
    defaultValue = 2


_TmnxOspfRemoteLFA_Type.__name__ = "TruthValue"
_TmnxOspfRemoteLFA_Object = MibTableColumn
tmnxOspfRemoteLFA = _TmnxOspfRemoteLFA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 14),
    _TmnxOspfRemoteLFA_Type()
)
tmnxOspfRemoteLFA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfRemoteLFA.setStatus("current")


class _TmnxOspfMaxPqCost_Type(Unsigned32):
    """Custom type tmnxOspfMaxPqCost based on Unsigned32"""
    defaultValue = 65535


_TmnxOspfMaxPqCost_Type.__name__ = "Unsigned32"
_TmnxOspfMaxPqCost_Object = MibTableColumn
tmnxOspfMaxPqCost = _TmnxOspfMaxPqCost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 15),
    _TmnxOspfMaxPqCost_Type()
)
tmnxOspfMaxPqCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfMaxPqCost.setStatus("current")


class _TmnxOspfTunnelMtu_Type(Unsigned32):
    """Custom type tmnxOspfTunnelMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9786),
    )


_TmnxOspfTunnelMtu_Type.__name__ = "Unsigned32"
_TmnxOspfTunnelMtu_Object = MibTableColumn
tmnxOspfTunnelMtu = _TmnxOspfTunnelMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 16),
    _TmnxOspfTunnelMtu_Type()
)
tmnxOspfTunnelMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfTunnelMtu.setStatus("current")


class _TmnxOspfAdvRtrLsaLimit_Type(Unsigned32):
    """Custom type tmnxOspfAdvRtrLsaLimit based on Unsigned32"""
    defaultValue = 0


_TmnxOspfAdvRtrLsaLimit_Type.__name__ = "Unsigned32"
_TmnxOspfAdvRtrLsaLimit_Object = MibTableColumn
tmnxOspfAdvRtrLsaLimit = _TmnxOspfAdvRtrLsaLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 17),
    _TmnxOspfAdvRtrLsaLimit_Type()
)
tmnxOspfAdvRtrLsaLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAdvRtrLsaLimit.setStatus("current")


class _TmnxOspfAdvRtrLsaLimitTimeout_Type(Unsigned32):
    """Custom type tmnxOspfAdvRtrLsaLimitTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1800),
    )


_TmnxOspfAdvRtrLsaLimitTimeout_Type.__name__ = "Unsigned32"
_TmnxOspfAdvRtrLsaLimitTimeout_Object = MibTableColumn
tmnxOspfAdvRtrLsaLimitTimeout = _TmnxOspfAdvRtrLsaLimitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 18),
    _TmnxOspfAdvRtrLsaLimitTimeout_Type()
)
tmnxOspfAdvRtrLsaLimitTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAdvRtrLsaLimitTimeout.setStatus("current")


class _TmnxOspfAdvRtrLsaLimitWarning_Type(Unsigned32):
    """Custom type tmnxOspfAdvRtrLsaLimitWarning based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxOspfAdvRtrLsaLimitWarning_Type.__name__ = "Unsigned32"
_TmnxOspfAdvRtrLsaLimitWarning_Object = MibTableColumn
tmnxOspfAdvRtrLsaLimitWarning = _TmnxOspfAdvRtrLsaLimitWarning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 19),
    _TmnxOspfAdvRtrLsaLimitWarning_Type()
)
tmnxOspfAdvRtrLsaLimitWarning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAdvRtrLsaLimitWarning.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfAdvRtrLsaLimitWarning.setUnits("percent")


class _TmnxOspfAdvRtrLsaLimitLogOnly_Type(TruthValue):
    """Custom type tmnxOspfAdvRtrLsaLimitLogOnly based on TruthValue"""
    defaultValue = 2


_TmnxOspfAdvRtrLsaLimitLogOnly_Type.__name__ = "TruthValue"
_TmnxOspfAdvRtrLsaLimitLogOnly_Object = MibTableColumn
tmnxOspfAdvRtrLsaLimitLogOnly = _TmnxOspfAdvRtrLsaLimitLogOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 20),
    _TmnxOspfAdvRtrLsaLimitLogOnly_Type()
)
tmnxOspfAdvRtrLsaLimitLogOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAdvRtrLsaLimitLogOnly.setStatus("current")


class _TmnxOspfSrAdjSidHold_Type(Unsigned32):
    """Custom type tmnxOspfSrAdjSidHold based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_TmnxOspfSrAdjSidHold_Type.__name__ = "Unsigned32"
_TmnxOspfSrAdjSidHold_Object = MibTableColumn
tmnxOspfSrAdjSidHold = _TmnxOspfSrAdjSidHold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 21),
    _TmnxOspfSrAdjSidHold_Type()
)
tmnxOspfSrAdjSidHold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfSrAdjSidHold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfSrAdjSidHold.setUnits("seconds")


class _TmnxOspfDatabaseExport_Type(TmnxEnabledDisabled):
    """Custom type tmnxOspfDatabaseExport based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxOspfDatabaseExport_Type.__name__ = "TmnxEnabledDisabled"
_TmnxOspfDatabaseExport_Object = MibTableColumn
tmnxOspfDatabaseExport = _TmnxOspfDatabaseExport_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 22),
    _TmnxOspfDatabaseExport_Type()
)
tmnxOspfDatabaseExport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfDatabaseExport.setStatus("current")


class _TmnxOspfDbExportIdentifierSet_Type(TruthValue):
    """Custom type tmnxOspfDbExportIdentifierSet based on TruthValue"""
    defaultValue = 2


_TmnxOspfDbExportIdentifierSet_Type.__name__ = "TruthValue"
_TmnxOspfDbExportIdentifierSet_Object = MibTableColumn
tmnxOspfDbExportIdentifierSet = _TmnxOspfDbExportIdentifierSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 23),
    _TmnxOspfDbExportIdentifierSet_Type()
)
tmnxOspfDbExportIdentifierSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfDbExportIdentifierSet.setStatus("current")


class _TmnxOspfDbExportIdentifierLow_Type(Unsigned32):
    """Custom type tmnxOspfDbExportIdentifierLow based on Unsigned32"""
    defaultValue = 0


_TmnxOspfDbExportIdentifierLow_Type.__name__ = "Unsigned32"
_TmnxOspfDbExportIdentifierLow_Object = MibTableColumn
tmnxOspfDbExportIdentifierLow = _TmnxOspfDbExportIdentifierLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 24),
    _TmnxOspfDbExportIdentifierLow_Type()
)
tmnxOspfDbExportIdentifierLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfDbExportIdentifierLow.setStatus("current")


class _TmnxOspfDbExportIdentifierHigh_Type(Unsigned32):
    """Custom type tmnxOspfDbExportIdentifierHigh based on Unsigned32"""
    defaultValue = 0


_TmnxOspfDbExportIdentifierHigh_Type.__name__ = "Unsigned32"
_TmnxOspfDbExportIdentifierHigh_Object = MibTableColumn
tmnxOspfDbExportIdentifierHigh = _TmnxOspfDbExportIdentifierHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 25),
    _TmnxOspfDbExportIdentifierHigh_Type()
)
tmnxOspfDbExportIdentifierHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfDbExportIdentifierHigh.setStatus("current")


class _TmnxOspfBgpLsIdentifierSet_Type(TruthValue):
    """Custom type tmnxOspfBgpLsIdentifierSet based on TruthValue"""
    defaultValue = 2


_TmnxOspfBgpLsIdentifierSet_Type.__name__ = "TruthValue"
_TmnxOspfBgpLsIdentifierSet_Object = MibTableColumn
tmnxOspfBgpLsIdentifierSet = _TmnxOspfBgpLsIdentifierSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 26),
    _TmnxOspfBgpLsIdentifierSet_Type()
)
tmnxOspfBgpLsIdentifierSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfBgpLsIdentifierSet.setStatus("current")


class _TmnxOspfBgpLsIdentifier_Type(Unsigned32):
    """Custom type tmnxOspfBgpLsIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TmnxOspfBgpLsIdentifier_Type.__name__ = "Unsigned32"
_TmnxOspfBgpLsIdentifier_Object = MibTableColumn
tmnxOspfBgpLsIdentifier = _TmnxOspfBgpLsIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 27),
    _TmnxOspfBgpLsIdentifier_Type()
)
tmnxOspfBgpLsIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfBgpLsIdentifier.setStatus("current")


class _TmnxOspfBackupNodeSidPfxType_Type(TmnxAddressAndPrefixType):
    """Custom type tmnxOspfBackupNodeSidPfxType based on TmnxAddressAndPrefixType"""
    defaultValue = 0


_TmnxOspfBackupNodeSidPfxType_Type.__name__ = "TmnxAddressAndPrefixType"
_TmnxOspfBackupNodeSidPfxType_Object = MibTableColumn
tmnxOspfBackupNodeSidPfxType = _TmnxOspfBackupNodeSidPfxType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 28),
    _TmnxOspfBackupNodeSidPfxType_Type()
)
tmnxOspfBackupNodeSidPfxType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfBackupNodeSidPfxType.setStatus("current")


class _TmnxOspfBackupNodeSidPfx_Type(TmnxAddressAndPrefixAddress):
    """Custom type tmnxOspfBackupNodeSidPfx based on TmnxAddressAndPrefixAddress"""
    defaultHexValue = ""

    subtypeSpec = TmnxAddressAndPrefixAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOspfBackupNodeSidPfx_Type.__name__ = "TmnxAddressAndPrefixAddress"
_TmnxOspfBackupNodeSidPfx_Object = MibTableColumn
tmnxOspfBackupNodeSidPfx = _TmnxOspfBackupNodeSidPfx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 29),
    _TmnxOspfBackupNodeSidPfx_Type()
)
tmnxOspfBackupNodeSidPfx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfBackupNodeSidPfx.setStatus("current")


class _TmnxOspfBackupNodeSidPfxLen_Type(TmnxAddressAndPrefixPrefix):
    """Custom type tmnxOspfBackupNodeSidPfxLen based on TmnxAddressAndPrefixPrefix"""
    defaultValue = 0


_TmnxOspfBackupNodeSidPfxLen_Type.__name__ = "TmnxAddressAndPrefixPrefix"
_TmnxOspfBackupNodeSidPfxLen_Object = MibTableColumn
tmnxOspfBackupNodeSidPfxLen = _TmnxOspfBackupNodeSidPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 30),
    _TmnxOspfBackupNodeSidPfxLen_Type()
)
tmnxOspfBackupNodeSidPfxLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfBackupNodeSidPfxLen.setStatus("current")


class _TmnxOspfBackupNodeSidType_Type(Integer32):
    """Custom type tmnxOspfBackupNodeSidType based on Integer32"""
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
        *(("none", 0),
          ("index", 1),
          ("label", 2))
    )


_TmnxOspfBackupNodeSidType_Type.__name__ = "Integer32"
_TmnxOspfBackupNodeSidType_Object = MibTableColumn
tmnxOspfBackupNodeSidType = _TmnxOspfBackupNodeSidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 31),
    _TmnxOspfBackupNodeSidType_Type()
)
tmnxOspfBackupNodeSidType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfBackupNodeSidType.setStatus("current")


class _TmnxOspfBackupNodeSidValue_Type(Unsigned32):
    """Custom type tmnxOspfBackupNodeSidValue based on Unsigned32"""
    defaultValue = 0


_TmnxOspfBackupNodeSidValue_Type.__name__ = "Unsigned32"
_TmnxOspfBackupNodeSidValue_Object = MibTableColumn
tmnxOspfBackupNodeSidValue = _TmnxOspfBackupNodeSidValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 32),
    _TmnxOspfBackupNodeSidValue_Type()
)
tmnxOspfBackupNodeSidValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfBackupNodeSidValue.setStatus("current")


class _TmnxOspfExtendedLsa_Type(Integer32):
    """Custom type tmnxOspfExtendedLsa based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sparse", 0),
          ("only", 1))
    )


_TmnxOspfExtendedLsa_Type.__name__ = "Integer32"
_TmnxOspfExtendedLsa_Object = MibTableColumn
tmnxOspfExtendedLsa = _TmnxOspfExtendedLsa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 33),
    _TmnxOspfExtendedLsa_Type()
)
tmnxOspfExtendedLsa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfExtendedLsa.setStatus("current")


class _TmnxOspfSrEntropyLabel_Type(Integer32):
    """Custom type tmnxOspfSrEntropyLabel based on Integer32"""
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
          ("forceDisable", 2))
    )


_TmnxOspfSrEntropyLabel_Type.__name__ = "Integer32"
_TmnxOspfSrEntropyLabel_Object = MibTableColumn
tmnxOspfSrEntropyLabel = _TmnxOspfSrEntropyLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 34),
    _TmnxOspfSrEntropyLabel_Type()
)
tmnxOspfSrEntropyLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfSrEntropyLabel.setStatus("current")


class _TmnxOspfTiLfa_Type(TruthValue):
    """Custom type tmnxOspfTiLfa based on TruthValue"""
    defaultValue = 2


_TmnxOspfTiLfa_Type.__name__ = "TruthValue"
_TmnxOspfTiLfa_Object = MibTableColumn
tmnxOspfTiLfa = _TmnxOspfTiLfa_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 35),
    _TmnxOspfTiLfa_Type()
)
tmnxOspfTiLfa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfTiLfa.setStatus("current")


class _TmnxOspfMaxSrFrrLabels_Type(Unsigned32):
    """Custom type tmnxOspfMaxSrFrrLabels based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TmnxOspfMaxSrFrrLabels_Type.__name__ = "Unsigned32"
_TmnxOspfMaxSrFrrLabels_Object = MibTableColumn
tmnxOspfMaxSrFrrLabels = _TmnxOspfMaxSrFrrLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 36),
    _TmnxOspfMaxSrFrrLabels_Type()
)
tmnxOspfMaxSrFrrLabels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfMaxSrFrrLabels.setStatus("current")


class _TmnxOspfOverrideTunnelElc_Type(Integer32):
    """Custom type tmnxOspfOverrideTunnelElc based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TmnxOspfOverrideTunnelElc_Type.__name__ = "Integer32"
_TmnxOspfOverrideTunnelElc_Object = MibTableColumn
tmnxOspfOverrideTunnelElc = _TmnxOspfOverrideTunnelElc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 37),
    _TmnxOspfOverrideTunnelElc_Type()
)
tmnxOspfOverrideTunnelElc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfOverrideTunnelElc.setStatus("current")


class _TmnxOspfSrMsAdminState_Type(TmnxAdminState):
    """Custom type tmnxOspfSrMsAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxOspfSrMsAdminState_Type.__name__ = "TmnxAdminState"
_TmnxOspfSrMsAdminState_Object = MibTableColumn
tmnxOspfSrMsAdminState = _TmnxOspfSrMsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 38),
    _TmnxOspfSrMsAdminState_Type()
)
tmnxOspfSrMsAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfSrMsAdminState.setStatus("current")


class _TmnxOspfSrExportTunnelTableProt_Type(Integer32):
    """Custom type tmnxOspfSrExportTunnelTableProt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ldp", 1))
    )


_TmnxOspfSrExportTunnelTableProt_Type.__name__ = "Integer32"
_TmnxOspfSrExportTunnelTableProt_Object = MibTableColumn
tmnxOspfSrExportTunnelTableProt = _TmnxOspfSrExportTunnelTableProt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 39),
    _TmnxOspfSrExportTunnelTableProt_Type()
)
tmnxOspfSrExportTunnelTableProt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfSrExportTunnelTableProt.setStatus("current")


class _TmnxOspfSrlbReservedLblBlockName_Type(TLNamedItemOrEmpty):
    """Custom type tmnxOspfSrlbReservedLblBlockName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxOspfSrlbReservedLblBlockName_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxOspfSrlbReservedLblBlockName_Object = MibTableColumn
tmnxOspfSrlbReservedLblBlockName = _TmnxOspfSrlbReservedLblBlockName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 40),
    _TmnxOspfSrlbReservedLblBlockName_Type()
)
tmnxOspfSrlbReservedLblBlockName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfSrlbReservedLblBlockName.setStatus("current")


class _TmnxOspfRemoteLfaNodeProtect_Type(TruthValue):
    """Custom type tmnxOspfRemoteLfaNodeProtect based on TruthValue"""
    defaultValue = 2


_TmnxOspfRemoteLfaNodeProtect_Type.__name__ = "TruthValue"
_TmnxOspfRemoteLfaNodeProtect_Object = MibTableColumn
tmnxOspfRemoteLfaNodeProtect = _TmnxOspfRemoteLfaNodeProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 41),
    _TmnxOspfRemoteLfaNodeProtect_Type()
)
tmnxOspfRemoteLfaNodeProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfRemoteLfaNodeProtect.setStatus("current")


class _TmnxOspfRemoteLfaMaxPqNodes_Type(Unsigned32):
    """Custom type tmnxOspfRemoteLfaMaxPqNodes based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TmnxOspfRemoteLfaMaxPqNodes_Type.__name__ = "Unsigned32"
_TmnxOspfRemoteLfaMaxPqNodes_Object = MibTableColumn
tmnxOspfRemoteLfaMaxPqNodes = _TmnxOspfRemoteLfaMaxPqNodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 42),
    _TmnxOspfRemoteLfaMaxPqNodes_Type()
)
tmnxOspfRemoteLfaMaxPqNodes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfRemoteLfaMaxPqNodes.setStatus("current")


class _TmnxOspfTiLfaNodeProtect_Type(TruthValue):
    """Custom type tmnxOspfTiLfaNodeProtect based on TruthValue"""
    defaultValue = 2


_TmnxOspfTiLfaNodeProtect_Type.__name__ = "TruthValue"
_TmnxOspfTiLfaNodeProtect_Object = MibTableColumn
tmnxOspfTiLfaNodeProtect = _TmnxOspfTiLfaNodeProtect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 43),
    _TmnxOspfTiLfaNodeProtect_Type()
)
tmnxOspfTiLfaNodeProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfTiLfaNodeProtect.setStatus("current")


class _TmnxOspfMultiInstance_Type(Integer32):
    """Custom type tmnxOspfMultiInstance based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TmnxOspfMultiInstance_Type.__name__ = "Integer32"
_TmnxOspfMultiInstance_Object = MibTableColumn
tmnxOspfMultiInstance = _TmnxOspfMultiInstance_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 44),
    _TmnxOspfMultiInstance_Type()
)
tmnxOspfMultiInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfMultiInstance.setStatus("current")


class _TmnxOspfReferenceBandwidthU64Hi_Type(TmnxHigh32):
    """Custom type tmnxOspfReferenceBandwidthU64Hi based on TmnxHigh32"""
    defaultValue = 0


_TmnxOspfReferenceBandwidthU64Hi_Type.__name__ = "TmnxHigh32"
_TmnxOspfReferenceBandwidthU64Hi_Object = MibTableColumn
tmnxOspfReferenceBandwidthU64Hi = _TmnxOspfReferenceBandwidthU64Hi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 45),
    _TmnxOspfReferenceBandwidthU64Hi_Type()
)
tmnxOspfReferenceBandwidthU64Hi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfReferenceBandwidthU64Hi.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfReferenceBandwidthU64Hi.setUnits("kilobps")


class _TmnxOspfReferenceBandwidthU64Lo_Type(TmnxLow32):
    """Custom type tmnxOspfReferenceBandwidthU64Lo based on TmnxLow32"""
    defaultValue = 100000000


_TmnxOspfReferenceBandwidthU64Lo_Type.__name__ = "TmnxLow32"
_TmnxOspfReferenceBandwidthU64Lo_Object = MibTableColumn
tmnxOspfReferenceBandwidthU64Lo = _TmnxOspfReferenceBandwidthU64Lo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 46),
    _TmnxOspfReferenceBandwidthU64Lo_Type()
)
tmnxOspfReferenceBandwidthU64Lo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfReferenceBandwidthU64Lo.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOspfReferenceBandwidthU64Lo.setUnits("kilobps")


class _TmnxOspfEgressStatsNodeSid_Type(TruthValue):
    """Custom type tmnxOspfEgressStatsNodeSid based on TruthValue"""
    defaultValue = 2


_TmnxOspfEgressStatsNodeSid_Type.__name__ = "TruthValue"
_TmnxOspfEgressStatsNodeSid_Object = MibTableColumn
tmnxOspfEgressStatsNodeSid = _TmnxOspfEgressStatsNodeSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 47),
    _TmnxOspfEgressStatsNodeSid_Type()
)
tmnxOspfEgressStatsNodeSid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfEgressStatsNodeSid.setStatus("current")


class _TmnxOspfEgressStatsAdjSid_Type(TruthValue):
    """Custom type tmnxOspfEgressStatsAdjSid based on TruthValue"""
    defaultValue = 2


_TmnxOspfEgressStatsAdjSid_Type.__name__ = "TruthValue"
_TmnxOspfEgressStatsAdjSid_Object = MibTableColumn
tmnxOspfEgressStatsAdjSid = _TmnxOspfEgressStatsAdjSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 48),
    _TmnxOspfEgressStatsAdjSid_Type()
)
tmnxOspfEgressStatsAdjSid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfEgressStatsAdjSid.setStatus("current")


class _TmnxOspfEgressStatsAdjSet_Type(TruthValue):
    """Custom type tmnxOspfEgressStatsAdjSet based on TruthValue"""
    defaultValue = 2


_TmnxOspfEgressStatsAdjSet_Type.__name__ = "TruthValue"
_TmnxOspfEgressStatsAdjSet_Object = MibTableColumn
tmnxOspfEgressStatsAdjSet = _TmnxOspfEgressStatsAdjSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 49),
    _TmnxOspfEgressStatsAdjSet_Type()
)
tmnxOspfEgressStatsAdjSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfEgressStatsAdjSet.setStatus("current")


class _TmnxOspfIngressStatsNodeSid_Type(TruthValue):
    """Custom type tmnxOspfIngressStatsNodeSid based on TruthValue"""
    defaultValue = 2


_TmnxOspfIngressStatsNodeSid_Type.__name__ = "TruthValue"
_TmnxOspfIngressStatsNodeSid_Object = MibTableColumn
tmnxOspfIngressStatsNodeSid = _TmnxOspfIngressStatsNodeSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 50),
    _TmnxOspfIngressStatsNodeSid_Type()
)
tmnxOspfIngressStatsNodeSid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIngressStatsNodeSid.setStatus("current")


class _TmnxOspfIngressStatsAdjSid_Type(TruthValue):
    """Custom type tmnxOspfIngressStatsAdjSid based on TruthValue"""
    defaultValue = 2


_TmnxOspfIngressStatsAdjSid_Type.__name__ = "TruthValue"
_TmnxOspfIngressStatsAdjSid_Object = MibTableColumn
tmnxOspfIngressStatsAdjSid = _TmnxOspfIngressStatsAdjSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 51),
    _TmnxOspfIngressStatsAdjSid_Type()
)
tmnxOspfIngressStatsAdjSid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIngressStatsAdjSid.setStatus("current")


class _TmnxOspfIngressStatsAdjSet_Type(TruthValue):
    """Custom type tmnxOspfIngressStatsAdjSet based on TruthValue"""
    defaultValue = 2


_TmnxOspfIngressStatsAdjSet_Type.__name__ = "TruthValue"
_TmnxOspfIngressStatsAdjSet_Object = MibTableColumn
tmnxOspfIngressStatsAdjSet = _TmnxOspfIngressStatsAdjSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 52),
    _TmnxOspfIngressStatsAdjSet_Type()
)
tmnxOspfIngressStatsAdjSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIngressStatsAdjSet.setStatus("current")


class _TmnxOspfOverloadInclExt1_Type(TruthValue):
    """Custom type tmnxOspfOverloadInclExt1 based on TruthValue"""
    defaultValue = 2


_TmnxOspfOverloadInclExt1_Type.__name__ = "TruthValue"
_TmnxOspfOverloadInclExt1_Object = MibTableColumn
tmnxOspfOverloadInclExt1 = _TmnxOspfOverloadInclExt1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 53),
    _TmnxOspfOverloadInclExt1_Type()
)
tmnxOspfOverloadInclExt1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfOverloadInclExt1.setStatus("current")


class _TmnxOspfSrClassForwarding_Type(TruthValue):
    """Custom type tmnxOspfSrClassForwarding based on TruthValue"""
    defaultValue = 2


_TmnxOspfSrClassForwarding_Type.__name__ = "TruthValue"
_TmnxOspfSrClassForwarding_Object = MibTableColumn
tmnxOspfSrClassForwarding = _TmnxOspfSrClassForwarding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 54),
    _TmnxOspfSrClassForwarding_Type()
)
tmnxOspfSrClassForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfSrClassForwarding.setStatus("current")


class _TmnxOspfTeOptsSrTe_Type(Integer32):
    """Custom type tmnxOspfTeOptsSrTe based on Integer32"""
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
        *(("false", 0),
          ("legacy", 1),
          ("appSpecificLinkAttr", 2))
    )


_TmnxOspfTeOptsSrTe_Type.__name__ = "Integer32"
_TmnxOspfTeOptsSrTe_Object = MibTableColumn
tmnxOspfTeOptsSrTe = _TmnxOspfTeOptsSrTe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 39, 1, 55),
    _TmnxOspfTeOptsSrTe_Type()
)
tmnxOspfTeOptsSrTe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfTeOptsSrTe.setStatus("current")
_TmnxOspfSrPfxTable_Object = MibTable
tmnxOspfSrPfxTable = _TmnxOspfSrPfxTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 40)
)
if mibBuilder.loadTexts:
    tmnxOspfSrPfxTable.setStatus("current")
_TmnxOspfSrPfxEntry_Object = MibTableRow
tmnxOspfSrPfxEntry = _TmnxOspfSrPfxEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 40, 1)
)
tmnxOspfSrPfxEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfSrPfxType"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfSrPfx"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfSrPfxLen"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfSrPfxAreaId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfSrPfxSidRtType"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfSrPfxSid"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfSrPfxAdvtRtrId"),
)
if mibBuilder.loadTexts:
    tmnxOspfSrPfxEntry.setStatus("current")
_TmnxOspfSrPfxType_Type = InetAddressType
_TmnxOspfSrPfxType_Object = MibTableColumn
tmnxOspfSrPfxType = _TmnxOspfSrPfxType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 40, 1, 1),
    _TmnxOspfSrPfxType_Type()
)
tmnxOspfSrPfxType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfSrPfxType.setStatus("current")


class _TmnxOspfSrPfx_Type(InetAddress):
    """Custom type tmnxOspfSrPfx based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOspfSrPfx_Type.__name__ = "InetAddress"
_TmnxOspfSrPfx_Object = MibTableColumn
tmnxOspfSrPfx = _TmnxOspfSrPfx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 40, 1, 2),
    _TmnxOspfSrPfx_Type()
)
tmnxOspfSrPfx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfSrPfx.setStatus("current")
_TmnxOspfSrPfxLen_Type = InetAddressPrefixLength
_TmnxOspfSrPfxLen_Object = MibTableColumn
tmnxOspfSrPfxLen = _TmnxOspfSrPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 40, 1, 3),
    _TmnxOspfSrPfxLen_Type()
)
tmnxOspfSrPfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfSrPfxLen.setStatus("current")
_TmnxOspfSrPfxAreaId_Type = TmnxOspfAreaIdTc
_TmnxOspfSrPfxAreaId_Object = MibTableColumn
tmnxOspfSrPfxAreaId = _TmnxOspfSrPfxAreaId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 40, 1, 4),
    _TmnxOspfSrPfxAreaId_Type()
)
tmnxOspfSrPfxAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfSrPfxAreaId.setStatus("current")
_TmnxOspfSrPfxSidRtType_Type = TmnxOspfSegmentRoutingRouteType
_TmnxOspfSrPfxSidRtType_Object = MibTableColumn
tmnxOspfSrPfxSidRtType = _TmnxOspfSrPfxSidRtType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 40, 1, 5),
    _TmnxOspfSrPfxSidRtType_Type()
)
tmnxOspfSrPfxSidRtType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfSrPfxSidRtType.setStatus("current")
_TmnxOspfSrPfxSid_Type = TmnxSegmentRoutingId
_TmnxOspfSrPfxSid_Object = MibTableColumn
tmnxOspfSrPfxSid = _TmnxOspfSrPfxSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 40, 1, 6),
    _TmnxOspfSrPfxSid_Type()
)
tmnxOspfSrPfxSid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfSrPfxSid.setStatus("current")
_TmnxOspfSrPfxAdvtRtrId_Type = TmnxOspfRouterIdTc
_TmnxOspfSrPfxAdvtRtrId_Object = MibTableColumn
tmnxOspfSrPfxAdvtRtrId = _TmnxOspfSrPfxAdvtRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 40, 1, 7),
    _TmnxOspfSrPfxAdvtRtrId_Type()
)
tmnxOspfSrPfxAdvtRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfSrPfxAdvtRtrId.setStatus("current")


class _TmnxOspfSrPfxSidFlags_Type(Bits):
    """Custom type tmnxOspfSrPfxSidFlags based on Bits"""
    namedValues = NamedValues(
        *(("bitN", 0),
          ("bitP", 1),
          ("bitM", 2),
          ("bitE", 3),
          ("bitV", 4),
          ("bitL", 5),
          ("bitIA", 6),
          ("bitAT", 7),
          ("bitB", 8))
    )

_TmnxOspfSrPfxSidFlags_Type.__name__ = "Bits"
_TmnxOspfSrPfxSidFlags_Object = MibTableColumn
tmnxOspfSrPfxSidFlags = _TmnxOspfSrPfxSidFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 40, 1, 8),
    _TmnxOspfSrPfxSidFlags_Type()
)
tmnxOspfSrPfxSidFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSrPfxSidFlags.setStatus("current")
_TmnxOspfSrPfxSidActive_Type = TruthValue
_TmnxOspfSrPfxSidActive_Object = MibTableColumn
tmnxOspfSrPfxSidActive = _TmnxOspfSrPfxSidActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 40, 1, 9),
    _TmnxOspfSrPfxSidActive_Type()
)
tmnxOspfSrPfxSidActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSrPfxSidActive.setStatus("obsolete")
_TmnxOspfSrPfxSidSRMS_Type = TruthValue
_TmnxOspfSrPfxSidSRMS_Object = MibTableColumn
tmnxOspfSrPfxSidSRMS = _TmnxOspfSrPfxSidSRMS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 40, 1, 10),
    _TmnxOspfSrPfxSidSRMS_Type()
)
tmnxOspfSrPfxSidSRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSrPfxSidSRMS.setStatus("current")
_TmnxOspfSrPfxSidSRMSSelected_Type = TruthValue
_TmnxOspfSrPfxSidSRMSSelected_Object = MibTableColumn
tmnxOspfSrPfxSidSRMSSelected = _TmnxOspfSrPfxSidSRMSSelected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 40, 1, 11),
    _TmnxOspfSrPfxSidSRMSSelected_Type()
)
tmnxOspfSrPfxSidSRMSSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSrPfxSidSRMSSelected.setStatus("current")
_TmnxOspfSrLfaStatsTable_Object = MibTable
tmnxOspfSrLfaStatsTable = _TmnxOspfSrLfaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 41)
)
if mibBuilder.loadTexts:
    tmnxOspfSrLfaStatsTable.setStatus("current")
_TmnxOspfSrLfaStatsEntry_Object = MibTableRow
tmnxOspfSrLfaStatsEntry = _TmnxOspfSrLfaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 41, 1)
)
tmnxOspfSrLfaStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfSrLfaStatsSidType"),
)
if mibBuilder.loadTexts:
    tmnxOspfSrLfaStatsEntry.setStatus("current")


class _TmnxOspfSrLfaStatsSidType_Type(Integer32):
    """Custom type tmnxOspfSrLfaStatsSidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nodeSid", 0),
          ("adjSid", 1),
          ("globAdjSid", 2))
    )


_TmnxOspfSrLfaStatsSidType_Type.__name__ = "Integer32"
_TmnxOspfSrLfaStatsSidType_Object = MibTableColumn
tmnxOspfSrLfaStatsSidType = _TmnxOspfSrLfaStatsSidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 41, 1, 1),
    _TmnxOspfSrLfaStatsSidType_Type()
)
tmnxOspfSrLfaStatsSidType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfSrLfaStatsSidType.setStatus("current")
_TmnxOspfSrLfaStatsTotalSid_Type = Gauge32
_TmnxOspfSrLfaStatsTotalSid_Object = MibTableColumn
tmnxOspfSrLfaStatsTotalSid = _TmnxOspfSrLfaStatsTotalSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 41, 1, 2),
    _TmnxOspfSrLfaStatsTotalSid_Type()
)
tmnxOspfSrLfaStatsTotalSid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSrLfaStatsTotalSid.setStatus("current")
_TmnxOspfSrLfaStatsLfaCovered_Type = Gauge32
_TmnxOspfSrLfaStatsLfaCovered_Object = MibTableColumn
tmnxOspfSrLfaStatsLfaCovered = _TmnxOspfSrLfaStatsLfaCovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 41, 1, 3),
    _TmnxOspfSrLfaStatsLfaCovered_Type()
)
tmnxOspfSrLfaStatsLfaCovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSrLfaStatsLfaCovered.setStatus("current")
_TmnxOspfSrLfaStatsRLfaCovered_Type = Gauge32
_TmnxOspfSrLfaStatsRLfaCovered_Object = MibTableColumn
tmnxOspfSrLfaStatsRLfaCovered = _TmnxOspfSrLfaStatsRLfaCovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 41, 1, 4),
    _TmnxOspfSrLfaStatsRLfaCovered_Type()
)
tmnxOspfSrLfaStatsRLfaCovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSrLfaStatsRLfaCovered.setStatus("current")
_TmnxOspfSrLfaStatsTiLfaCovered_Type = Gauge32
_TmnxOspfSrLfaStatsTiLfaCovered_Object = MibTableColumn
tmnxOspfSrLfaStatsTiLfaCovered = _TmnxOspfSrLfaStatsTiLfaCovered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 41, 1, 5),
    _TmnxOspfSrLfaStatsTiLfaCovered_Type()
)
tmnxOspfSrLfaStatsTiLfaCovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSrLfaStatsTiLfaCovered.setStatus("current")
_TmnxOspfIgpSCTable_Object = MibTable
tmnxOspfIgpSCTable = _TmnxOspfIgpSCTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 42)
)
if mibBuilder.loadTexts:
    tmnxOspfIgpSCTable.setStatus("current")
_TmnxOspfIgpSCEntry_Object = MibTableRow
tmnxOspfIgpSCEntry = _TmnxOspfIgpSCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 42, 1)
)
tmnxOspfIgpSCEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
)
if mibBuilder.loadTexts:
    tmnxOspfIgpSCEntry.setStatus("current")


class _TmnxOspfIgpSCAdminState_Type(TmnxAdminState):
    """Custom type tmnxOspfIgpSCAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxOspfIgpSCAdminState_Type.__name__ = "TmnxAdminState"
_TmnxOspfIgpSCAdminState_Object = MibTableColumn
tmnxOspfIgpSCAdminState = _TmnxOspfIgpSCAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 42, 1, 2),
    _TmnxOspfIgpSCAdminState_Type()
)
tmnxOspfIgpSCAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIgpSCAdminState.setStatus("current")
_TmnxOspfIgpSCTunnNextHopTable_Object = MibTable
tmnxOspfIgpSCTunnNextHopTable = _TmnxOspfIgpSCTunnNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 43)
)
if mibBuilder.loadTexts:
    tmnxOspfIgpSCTunnNextHopTable.setStatus("current")
_TmnxOspfIgpSCTunnNextHopEntry_Object = MibTableRow
tmnxOspfIgpSCTunnNextHopEntry = _TmnxOspfIgpSCTunnNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 43, 1)
)
tmnxOspfIgpSCTunnNextHopEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfIgpSCTunnNextHopFamily"),
)
if mibBuilder.loadTexts:
    tmnxOspfIgpSCTunnNextHopEntry.setStatus("current")
_TmnxOspfIgpSCTunnNextHopFamily_Type = TmnxIgpSCFamilyType
_TmnxOspfIgpSCTunnNextHopFamily_Object = MibTableColumn
tmnxOspfIgpSCTunnNextHopFamily = _TmnxOspfIgpSCTunnNextHopFamily_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 43, 1, 1),
    _TmnxOspfIgpSCTunnNextHopFamily_Type()
)
tmnxOspfIgpSCTunnNextHopFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfIgpSCTunnNextHopFamily.setStatus("current")
_TmnxOspfIgpSCTunnNextHopLstCh_Type = TimeStamp
_TmnxOspfIgpSCTunnNextHopLstCh_Object = MibTableColumn
tmnxOspfIgpSCTunnNextHopLstCh = _TmnxOspfIgpSCTunnNextHopLstCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 43, 1, 2),
    _TmnxOspfIgpSCTunnNextHopLstCh_Type()
)
tmnxOspfIgpSCTunnNextHopLstCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIgpSCTunnNextHopLstCh.setStatus("current")


class _TmnxOspfIgpSCTNHResolution_Type(TResolveStatus):
    """Custom type tmnxOspfIgpSCTNHResolution based on TResolveStatus"""
    defaultValue = 0


_TmnxOspfIgpSCTNHResolution_Type.__name__ = "TResolveStatus"
_TmnxOspfIgpSCTNHResolution_Object = MibTableColumn
tmnxOspfIgpSCTNHResolution = _TmnxOspfIgpSCTNHResolution_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 43, 1, 3),
    _TmnxOspfIgpSCTNHResolution_Type()
)
tmnxOspfIgpSCTNHResolution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIgpSCTNHResolution.setStatus("current")


class _TmnxOspfIgpSCTNHResFilterRsvp_Type(TruthValue):
    """Custom type tmnxOspfIgpSCTNHResFilterRsvp based on TruthValue"""
    defaultValue = 2


_TmnxOspfIgpSCTNHResFilterRsvp_Type.__name__ = "TruthValue"
_TmnxOspfIgpSCTNHResFilterRsvp_Object = MibTableColumn
tmnxOspfIgpSCTNHResFilterRsvp = _TmnxOspfIgpSCTNHResFilterRsvp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 43, 1, 4),
    _TmnxOspfIgpSCTNHResFilterRsvp_Type()
)
tmnxOspfIgpSCTNHResFilterRsvp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIgpSCTNHResFilterRsvp.setStatus("current")


class _TmnxOspfIgpSCTNHResFilterSrTe_Type(TruthValue):
    """Custom type tmnxOspfIgpSCTNHResFilterSrTe based on TruthValue"""
    defaultValue = 2


_TmnxOspfIgpSCTNHResFilterSrTe_Type.__name__ = "TruthValue"
_TmnxOspfIgpSCTNHResFilterSrTe_Object = MibTableColumn
tmnxOspfIgpSCTNHResFilterSrTe = _TmnxOspfIgpSCTNHResFilterSrTe_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 43, 1, 5),
    _TmnxOspfIgpSCTNHResFilterSrTe_Type()
)
tmnxOspfIgpSCTNHResFilterSrTe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIgpSCTNHResFilterSrTe.setStatus("current")
_TmnxOspfAdjSetTable_Object = MibTable
tmnxOspfAdjSetTable = _TmnxOspfAdjSetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 44)
)
if mibBuilder.loadTexts:
    tmnxOspfAdjSetTable.setStatus("current")
_TmnxOspfAdjSetEntry_Object = MibTableRow
tmnxOspfAdjSetEntry = _TmnxOspfAdjSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 44, 1)
)
tmnxOspfAdjSetEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetId"),
)
if mibBuilder.loadTexts:
    tmnxOspfAdjSetEntry.setStatus("current")


class _TmnxOspfAdjSetId_Type(Unsigned32):
    """Custom type tmnxOspfAdjSetId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOspfAdjSetId_Type.__name__ = "Unsigned32"
_TmnxOspfAdjSetId_Object = MibTableColumn
tmnxOspfAdjSetId = _TmnxOspfAdjSetId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 44, 1, 1),
    _TmnxOspfAdjSetId_Type()
)
tmnxOspfAdjSetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetId.setStatus("current")
_TmnxOspfAdjSetRowStatus_Type = RowStatus
_TmnxOspfAdjSetRowStatus_Object = MibTableColumn
tmnxOspfAdjSetRowStatus = _TmnxOspfAdjSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 44, 1, 2),
    _TmnxOspfAdjSetRowStatus_Type()
)
tmnxOspfAdjSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetRowStatus.setStatus("current")
_TmnxOspfAdjSetLastChanged_Type = TimeStamp
_TmnxOspfAdjSetLastChanged_Object = MibTableColumn
tmnxOspfAdjSetLastChanged = _TmnxOspfAdjSetLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 44, 1, 3),
    _TmnxOspfAdjSetLastChanged_Type()
)
tmnxOspfAdjSetLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetLastChanged.setStatus("current")


class _TmnxOspfAdjSetSidType_Type(Integer32):
    """Custom type tmnxOspfAdjSetSidType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("label", 2))
    )


_TmnxOspfAdjSetSidType_Type.__name__ = "Integer32"
_TmnxOspfAdjSetSidType_Object = MibTableColumn
tmnxOspfAdjSetSidType = _TmnxOspfAdjSetSidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 44, 1, 4),
    _TmnxOspfAdjSetSidType_Type()
)
tmnxOspfAdjSetSidType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetSidType.setStatus("current")


class _TmnxOspfAdjSetSidValue_Type(Unsigned32):
    """Custom type tmnxOspfAdjSetSidValue based on Unsigned32"""
    defaultValue = 0


_TmnxOspfAdjSetSidValue_Type.__name__ = "Unsigned32"
_TmnxOspfAdjSetSidValue_Object = MibTableColumn
tmnxOspfAdjSetSidValue = _TmnxOspfAdjSetSidValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 44, 1, 5),
    _TmnxOspfAdjSetSidValue_Type()
)
tmnxOspfAdjSetSidValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetSidValue.setStatus("current")


class _TmnxOspfAdjSetParallel_Type(TruthValue):
    """Custom type tmnxOspfAdjSetParallel based on TruthValue"""
    defaultValue = 1


_TmnxOspfAdjSetParallel_Type.__name__ = "TruthValue"
_TmnxOspfAdjSetParallel_Object = MibTableColumn
tmnxOspfAdjSetParallel = _TmnxOspfAdjSetParallel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 44, 1, 7),
    _TmnxOspfAdjSetParallel_Type()
)
tmnxOspfAdjSetParallel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetParallel.setStatus("current")


class _TmnxOspfAdjSetAdvertise_Type(TruthValue):
    """Custom type tmnxOspfAdjSetAdvertise based on TruthValue"""
    defaultValue = 1


_TmnxOspfAdjSetAdvertise_Type.__name__ = "TruthValue"
_TmnxOspfAdjSetAdvertise_Object = MibTableColumn
tmnxOspfAdjSetAdvertise = _TmnxOspfAdjSetAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 44, 1, 8),
    _TmnxOspfAdjSetAdvertise_Type()
)
tmnxOspfAdjSetAdvertise.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetAdvertise.setStatus("current")
_TmnxOspfAdjSetDynSidValue_Type = Unsigned32
_TmnxOspfAdjSetDynSidValue_Object = MibTableColumn
tmnxOspfAdjSetDynSidValue = _TmnxOspfAdjSetDynSidValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 44, 1, 9),
    _TmnxOspfAdjSetDynSidValue_Type()
)
tmnxOspfAdjSetDynSidValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetDynSidValue.setStatus("current")
_TmnxOspfAdjSetTunlDestType_Type = InetAddressType
_TmnxOspfAdjSetTunlDestType_Object = MibTableColumn
tmnxOspfAdjSetTunlDestType = _TmnxOspfAdjSetTunlDestType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 44, 1, 10),
    _TmnxOspfAdjSetTunlDestType_Type()
)
tmnxOspfAdjSetTunlDestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetTunlDestType.setStatus("current")


class _TmnxOspfAdjSetTunlDestIp_Type(InetAddress):
    """Custom type tmnxOspfAdjSetTunlDestIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxOspfAdjSetTunlDestIp_Type.__name__ = "InetAddress"
_TmnxOspfAdjSetTunlDestIp_Object = MibTableColumn
tmnxOspfAdjSetTunlDestIp = _TmnxOspfAdjSetTunlDestIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 44, 1, 11),
    _TmnxOspfAdjSetTunlDestIp_Type()
)
tmnxOspfAdjSetTunlDestIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetTunlDestIp.setStatus("current")
_TmnxOspfAdjSetNbrRtrId_Type = TmnxOspfRouterIdTc
_TmnxOspfAdjSetNbrRtrId_Object = MibTableColumn
tmnxOspfAdjSetNbrRtrId = _TmnxOspfAdjSetNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 44, 1, 12),
    _TmnxOspfAdjSetNbrRtrId_Type()
)
tmnxOspfAdjSetNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetNbrRtrId.setStatus("current")
_TmnxOspfAdjSetMembersCount_Type = Unsigned32
_TmnxOspfAdjSetMembersCount_Object = MibTableColumn
tmnxOspfAdjSetMembersCount = _TmnxOspfAdjSetMembersCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 44, 1, 13),
    _TmnxOspfAdjSetMembersCount_Type()
)
tmnxOspfAdjSetMembersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetMembersCount.setStatus("current")
_TmnxOspfAdjSetActiveMembers_Type = Unsigned32
_TmnxOspfAdjSetActiveMembers_Object = MibTableColumn
tmnxOspfAdjSetActiveMembers = _TmnxOspfAdjSetActiveMembers_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 44, 1, 14),
    _TmnxOspfAdjSetActiveMembers_Type()
)
tmnxOspfAdjSetActiveMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetActiveMembers.setStatus("current")
_TmnxOspfAdjSetUpTime_Type = Integer32
_TmnxOspfAdjSetUpTime_Object = MibTableColumn
tmnxOspfAdjSetUpTime = _TmnxOspfAdjSetUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 44, 1, 15),
    _TmnxOspfAdjSetUpTime_Type()
)
tmnxOspfAdjSetUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetUpTime.setStatus("current")


class _TmnxOspfAdjSetStatus_Type(Integer32):
    """Custom type tmnxOspfAdjSetStatus based on Integer32"""
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
        *(("notActive", 0),
          ("active", 1),
          ("activeIncomplete", 2),
          ("fibAddFailed", 3))
    )


_TmnxOspfAdjSetStatus_Type.__name__ = "Integer32"
_TmnxOspfAdjSetStatus_Object = MibTableColumn
tmnxOspfAdjSetStatus = _TmnxOspfAdjSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 44, 1, 16),
    _TmnxOspfAdjSetStatus_Type()
)
tmnxOspfAdjSetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetStatus.setStatus("current")
_TmnxOspfAdjSetMtu_Type = Unsigned32
_TmnxOspfAdjSetMtu_Object = MibTableColumn
tmnxOspfAdjSetMtu = _TmnxOspfAdjSetMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 44, 1, 17),
    _TmnxOspfAdjSetMtu_Type()
)
tmnxOspfAdjSetMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetMtu.setStatus("current")
_TmnxOspfIfAdjSetTable_Object = MibTable
tmnxOspfIfAdjSetTable = _TmnxOspfIfAdjSetTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 45)
)
if mibBuilder.loadTexts:
    tmnxOspfIfAdjSetTable.setStatus("current")
_TmnxOspfIfAdjSetEntry_Object = MibTableRow
tmnxOspfIfAdjSetEntry = _TmnxOspfIfAdjSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 45, 1)
)
tmnxOspfIfAdjSetEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfIndex"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfInstId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfAreaId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAdjSetId"),
)
if mibBuilder.loadTexts:
    tmnxOspfIfAdjSetEntry.setStatus("current")


class _TmnxOspfIfAdjSetId_Type(Unsigned32):
    """Custom type tmnxOspfIfAdjSetId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOspfIfAdjSetId_Type.__name__ = "Unsigned32"
_TmnxOspfIfAdjSetId_Object = MibTableColumn
tmnxOspfIfAdjSetId = _TmnxOspfIfAdjSetId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 45, 1, 1),
    _TmnxOspfIfAdjSetId_Type()
)
tmnxOspfIfAdjSetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfIfAdjSetId.setStatus("current")
_TmnxOspfIfAdjSetRowStatus_Type = RowStatus
_TmnxOspfIfAdjSetRowStatus_Object = MibTableColumn
tmnxOspfIfAdjSetRowStatus = _TmnxOspfIfAdjSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 45, 1, 2),
    _TmnxOspfIfAdjSetRowStatus_Type()
)
tmnxOspfIfAdjSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfIfAdjSetRowStatus.setStatus("current")
_TmnxOspfIfAdjSetLastChanged_Type = TimeStamp
_TmnxOspfIfAdjSetLastChanged_Object = MibTableColumn
tmnxOspfIfAdjSetLastChanged = _TmnxOspfIfAdjSetLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 45, 1, 3),
    _TmnxOspfIfAdjSetLastChanged_Type()
)
tmnxOspfIfAdjSetLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfIfAdjSetLastChanged.setStatus("current")
_TmnxOspfAdjSetNhopTable_Object = MibTable
tmnxOspfAdjSetNhopTable = _TmnxOspfAdjSetNhopTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 46)
)
if mibBuilder.loadTexts:
    tmnxOspfAdjSetNhopTable.setStatus("current")
_TmnxOspfAdjSetNhopEntry_Object = MibTableRow
tmnxOspfAdjSetNhopEntry = _TmnxOspfAdjSetNhopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 46, 1)
)
tmnxOspfAdjSetNhopEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetNhopId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetNhopRtrId"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetNhopIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxOspfAdjSetNhopEntry.setStatus("current")


class _TmnxOspfAdjSetNhopId_Type(Unsigned32):
    """Custom type tmnxOspfAdjSetNhopId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxOspfAdjSetNhopId_Type.__name__ = "Unsigned32"
_TmnxOspfAdjSetNhopId_Object = MibTableColumn
tmnxOspfAdjSetNhopId = _TmnxOspfAdjSetNhopId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 46, 1, 1),
    _TmnxOspfAdjSetNhopId_Type()
)
tmnxOspfAdjSetNhopId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetNhopId.setStatus("current")
_TmnxOspfAdjSetNhopRtrId_Type = TmnxOspfRouterIdTc
_TmnxOspfAdjSetNhopRtrId_Object = MibTableColumn
tmnxOspfAdjSetNhopRtrId = _TmnxOspfAdjSetNhopRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 46, 1, 2),
    _TmnxOspfAdjSetNhopRtrId_Type()
)
tmnxOspfAdjSetNhopRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetNhopRtrId.setStatus("current")
_TmnxOspfAdjSetNhopIfIndex_Type = InterfaceIndex
_TmnxOspfAdjSetNhopIfIndex_Object = MibTableColumn
tmnxOspfAdjSetNhopIfIndex = _TmnxOspfAdjSetNhopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 46, 1, 3),
    _TmnxOspfAdjSetNhopIfIndex_Type()
)
tmnxOspfAdjSetNhopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetNhopIfIndex.setStatus("current")
_TmnxOspfAdjSetNhopType_Type = InetAddressType
_TmnxOspfAdjSetNhopType_Object = MibTableColumn
tmnxOspfAdjSetNhopType = _TmnxOspfAdjSetNhopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 46, 1, 4),
    _TmnxOspfAdjSetNhopType_Type()
)
tmnxOspfAdjSetNhopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetNhopType.setStatus("current")


class _TmnxOspfAdjSetNhop_Type(InetAddress):
    """Custom type tmnxOspfAdjSetNhop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxOspfAdjSetNhop_Type.__name__ = "InetAddress"
_TmnxOspfAdjSetNhop_Object = MibTableColumn
tmnxOspfAdjSetNhop = _TmnxOspfAdjSetNhop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 46, 1, 5),
    _TmnxOspfAdjSetNhop_Type()
)
tmnxOspfAdjSetNhop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfAdjSetNhop.setStatus("current")
_TmnxOspfSRMSSidMapTable_Object = MibTable
tmnxOspfSRMSSidMapTable = _TmnxOspfSRMSSidMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 47)
)
if mibBuilder.loadTexts:
    tmnxOspfSRMSSidMapTable.setStatus("current")
_TmnxOspfSRMSSidMapEntry_Object = MibTableRow
tmnxOspfSRMSSidMapEntry = _TmnxOspfSRMSSidMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 47, 1)
)
tmnxOspfSRMSSidMapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfSRMSSidMapNodeSidIndex"),
)
if mibBuilder.loadTexts:
    tmnxOspfSRMSSidMapEntry.setStatus("current")
_TmnxOspfSRMSSidMapNodeSidIndex_Type = Unsigned32
_TmnxOspfSRMSSidMapNodeSidIndex_Object = MibTableColumn
tmnxOspfSRMSSidMapNodeSidIndex = _TmnxOspfSRMSSidMapNodeSidIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 47, 1, 1),
    _TmnxOspfSRMSSidMapNodeSidIndex_Type()
)
tmnxOspfSRMSSidMapNodeSidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfSRMSSidMapNodeSidIndex.setStatus("current")
_TmnxOspfSRMSSidMapRowStatus_Type = RowStatus
_TmnxOspfSRMSSidMapRowStatus_Object = MibTableColumn
tmnxOspfSRMSSidMapRowStatus = _TmnxOspfSRMSSidMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 47, 1, 2),
    _TmnxOspfSRMSSidMapRowStatus_Type()
)
tmnxOspfSRMSSidMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfSRMSSidMapRowStatus.setStatus("current")
_TmnxOspfSRMSSidMapLastCh_Type = TimeStamp
_TmnxOspfSRMSSidMapLastCh_Object = MibTableColumn
tmnxOspfSRMSSidMapLastCh = _TmnxOspfSRMSSidMapLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 47, 1, 3),
    _TmnxOspfSRMSSidMapLastCh_Type()
)
tmnxOspfSRMSSidMapLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSRMSSidMapLastCh.setStatus("current")
_TmnxOspfSRMSSidMapPrefixType_Type = TmnxAddressAndPrefixType
_TmnxOspfSRMSSidMapPrefixType_Object = MibTableColumn
tmnxOspfSRMSSidMapPrefixType = _TmnxOspfSRMSSidMapPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 47, 1, 4),
    _TmnxOspfSRMSSidMapPrefixType_Type()
)
tmnxOspfSRMSSidMapPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfSRMSSidMapPrefixType.setStatus("current")


class _TmnxOspfSRMSSidMapPrefix_Type(TmnxAddressAndPrefixAddress):
    """Custom type tmnxOspfSRMSSidMapPrefix based on TmnxAddressAndPrefixAddress"""
    subtypeSpec = TmnxAddressAndPrefixAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOspfSRMSSidMapPrefix_Type.__name__ = "TmnxAddressAndPrefixAddress"
_TmnxOspfSRMSSidMapPrefix_Object = MibTableColumn
tmnxOspfSRMSSidMapPrefix = _TmnxOspfSRMSSidMapPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 47, 1, 5),
    _TmnxOspfSRMSSidMapPrefix_Type()
)
tmnxOspfSRMSSidMapPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfSRMSSidMapPrefix.setStatus("current")
_TmnxOspfSRMSSidMapPrefixLength_Type = TmnxAddressAndPrefixPrefix
_TmnxOspfSRMSSidMapPrefixLength_Object = MibTableColumn
tmnxOspfSRMSSidMapPrefixLength = _TmnxOspfSRMSSidMapPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 47, 1, 6),
    _TmnxOspfSRMSSidMapPrefixLength_Type()
)
tmnxOspfSRMSSidMapPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfSRMSSidMapPrefixLength.setStatus("current")


class _TmnxOspfSRMSSidMapNodeSidRange_Type(Unsigned32):
    """Custom type tmnxOspfSRMSSidMapNodeSidRange based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxOspfSRMSSidMapNodeSidRange_Type.__name__ = "Unsigned32"
_TmnxOspfSRMSSidMapNodeSidRange_Object = MibTableColumn
tmnxOspfSRMSSidMapNodeSidRange = _TmnxOspfSRMSSidMapNodeSidRange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 47, 1, 7),
    _TmnxOspfSRMSSidMapNodeSidRange_Type()
)
tmnxOspfSRMSSidMapNodeSidRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfSRMSSidMapNodeSidRange.setStatus("current")


class _TmnxOspfSRMSSidMapScope_Type(Integer32):
    """Custom type tmnxOspfSRMSSidMapScope based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("as", 1),
          ("area", 2))
    )


_TmnxOspfSRMSSidMapScope_Type.__name__ = "Integer32"
_TmnxOspfSRMSSidMapScope_Object = MibTableColumn
tmnxOspfSRMSSidMapScope = _TmnxOspfSRMSSidMapScope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 47, 1, 8),
    _TmnxOspfSRMSSidMapScope_Type()
)
tmnxOspfSRMSSidMapScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfSRMSSidMapScope.setStatus("current")


class _TmnxOspfSRMSSidMapScopeArea_Type(TmnxOspfAreaIdTc):
    """Custom type tmnxOspfSRMSSidMapScopeArea based on TmnxOspfAreaIdTc"""
    defaultValue = 0


_TmnxOspfSRMSSidMapScopeArea_Type.__name__ = "TmnxOspfAreaIdTc"
_TmnxOspfSRMSSidMapScopeArea_Object = MibTableColumn
tmnxOspfSRMSSidMapScopeArea = _TmnxOspfSRMSSidMapScopeArea_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 47, 1, 9),
    _TmnxOspfSRMSSidMapScopeArea_Type()
)
tmnxOspfSRMSSidMapScopeArea.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOspfSRMSSidMapScopeArea.setStatus("current")
_TmnxOspfSidStatsTable_Object = MibTable
tmnxOspfSidStatsTable = _TmnxOspfSidStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 48)
)
if mibBuilder.loadTexts:
    tmnxOspfSidStatsTable.setStatus("current")
_TmnxOspfSidStatsEntry_Object = MibTableRow
tmnxOspfSidStatsEntry = _TmnxOspfSidStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 48, 1)
)
tmnxOspfSidStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfSidStatsSid"),
)
if mibBuilder.loadTexts:
    tmnxOspfSidStatsEntry.setStatus("current")
_TmnxOspfSidStatsSid_Type = Unsigned32
_TmnxOspfSidStatsSid_Object = MibTableColumn
tmnxOspfSidStatsSid = _TmnxOspfSidStatsSid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 48, 1, 1),
    _TmnxOspfSidStatsSid_Type()
)
tmnxOspfSidStatsSid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfSidStatsSid.setStatus("current")


class _TmnxOspfSidStatsSidType_Type(Integer32):
    """Custom type tmnxOspfSidStatsSidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("node", 0),
          ("adjacency", 1),
          ("adjacencySet", 2))
    )


_TmnxOspfSidStatsSidType_Type.__name__ = "Integer32"
_TmnxOspfSidStatsSidType_Object = MibTableColumn
tmnxOspfSidStatsSidType = _TmnxOspfSidStatsSidType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 48, 1, 2),
    _TmnxOspfSidStatsSidType_Type()
)
tmnxOspfSidStatsSidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSidStatsSidType.setStatus("current")
_TmnxOspfSidStatsPrefixType_Type = InetAddressType
_TmnxOspfSidStatsPrefixType_Object = MibTableColumn
tmnxOspfSidStatsPrefixType = _TmnxOspfSidStatsPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 48, 1, 3),
    _TmnxOspfSidStatsPrefixType_Type()
)
tmnxOspfSidStatsPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSidStatsPrefixType.setStatus("current")


class _TmnxOspfSidStatsPrefix_Type(InetAddress):
    """Custom type tmnxOspfSidStatsPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxOspfSidStatsPrefix_Type.__name__ = "InetAddress"
_TmnxOspfSidStatsPrefix_Object = MibTableColumn
tmnxOspfSidStatsPrefix = _TmnxOspfSidStatsPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 48, 1, 4),
    _TmnxOspfSidStatsPrefix_Type()
)
tmnxOspfSidStatsPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSidStatsPrefix.setStatus("current")
_TmnxOspfSidStatsPrefixLength_Type = InetAddressPrefixLength
_TmnxOspfSidStatsPrefixLength_Object = MibTableColumn
tmnxOspfSidStatsPrefixLength = _TmnxOspfSidStatsPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 48, 1, 5),
    _TmnxOspfSidStatsPrefixLength_Type()
)
tmnxOspfSidStatsPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSidStatsPrefixLength.setStatus("current")
_TmnxOspfSidStatsIfIndex_Type = InterfaceIndexOrZero
_TmnxOspfSidStatsIfIndex_Object = MibTableColumn
tmnxOspfSidStatsIfIndex = _TmnxOspfSidStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 48, 1, 6),
    _TmnxOspfSidStatsIfIndex_Type()
)
tmnxOspfSidStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSidStatsIfIndex.setStatus("current")


class _TmnxOspfSidStatsAdjSet_Type(Unsigned32):
    """Custom type tmnxOspfSidStatsAdjSet based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TmnxOspfSidStatsAdjSet_Type.__name__ = "Unsigned32"
_TmnxOspfSidStatsAdjSet_Object = MibTableColumn
tmnxOspfSidStatsAdjSet = _TmnxOspfSidStatsAdjSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 48, 1, 7),
    _TmnxOspfSidStatsAdjSet_Type()
)
tmnxOspfSidStatsAdjSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSidStatsAdjSet.setStatus("current")


class _TmnxOspfSidStatsIngressOperState_Type(Integer32):
    """Custom type tmnxOspfSidStatsIngressOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("noResource", 3))
    )


_TmnxOspfSidStatsIngressOperState_Type.__name__ = "Integer32"
_TmnxOspfSidStatsIngressOperState_Object = MibTableColumn
tmnxOspfSidStatsIngressOperState = _TmnxOspfSidStatsIngressOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 48, 1, 8),
    _TmnxOspfSidStatsIngressOperState_Type()
)
tmnxOspfSidStatsIngressOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSidStatsIngressOperState.setStatus("current")
_TmnxOspfSidStatsIngressOctets_Type = Counter64
_TmnxOspfSidStatsIngressOctets_Object = MibTableColumn
tmnxOspfSidStatsIngressOctets = _TmnxOspfSidStatsIngressOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 48, 1, 9),
    _TmnxOspfSidStatsIngressOctets_Type()
)
tmnxOspfSidStatsIngressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSidStatsIngressOctets.setStatus("current")
_TmnxOspfSidStatsIngressPackets_Type = Counter64
_TmnxOspfSidStatsIngressPackets_Object = MibTableColumn
tmnxOspfSidStatsIngressPackets = _TmnxOspfSidStatsIngressPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 48, 1, 10),
    _TmnxOspfSidStatsIngressPackets_Type()
)
tmnxOspfSidStatsIngressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSidStatsIngressPackets.setStatus("current")


class _TmnxOspfSidStatsEgressOperState_Type(Integer32):
    """Custom type tmnxOspfSidStatsEgressOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("noResource", 3))
    )


_TmnxOspfSidStatsEgressOperState_Type.__name__ = "Integer32"
_TmnxOspfSidStatsEgressOperState_Object = MibTableColumn
tmnxOspfSidStatsEgressOperState = _TmnxOspfSidStatsEgressOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 48, 1, 11),
    _TmnxOspfSidStatsEgressOperState_Type()
)
tmnxOspfSidStatsEgressOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSidStatsEgressOperState.setStatus("current")
_TmnxOspfSidStatsEgressOctets_Type = Counter64
_TmnxOspfSidStatsEgressOctets_Object = MibTableColumn
tmnxOspfSidStatsEgressOctets = _TmnxOspfSidStatsEgressOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 48, 1, 12),
    _TmnxOspfSidStatsEgressOctets_Type()
)
tmnxOspfSidStatsEgressOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSidStatsEgressOctets.setStatus("current")
_TmnxOspfSidStatsEgressPackets_Type = Counter64
_TmnxOspfSidStatsEgressPackets_Object = MibTableColumn
tmnxOspfSidStatsEgressPackets = _TmnxOspfSidStatsEgressPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 48, 1, 13),
    _TmnxOspfSidStatsEgressPackets_Type()
)
tmnxOspfSidStatsEgressPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSidStatsEgressPackets.setStatus("current")
_TmnxOspfHostnameTable_Object = MibTable
tmnxOspfHostnameTable = _TmnxOspfHostnameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 49)
)
if mibBuilder.loadTexts:
    tmnxOspfHostnameTable.setStatus("current")
_TmnxOspfHostnameEntry_Object = MibTableRow
tmnxOspfHostnameEntry = _TmnxOspfHostnameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 49, 1)
)
tmnxOspfHostnameEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfVersion"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfInstance"),
    (0, "TIMETRA-OSPF-NG-MIB", "tmnxOspfHostnameRtrId"),
)
if mibBuilder.loadTexts:
    tmnxOspfHostnameEntry.setStatus("current")
_TmnxOspfHostnameRtrId_Type = TmnxOspfRouterIdTc
_TmnxOspfHostnameRtrId_Object = MibTableColumn
tmnxOspfHostnameRtrId = _TmnxOspfHostnameRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 49, 1, 1),
    _TmnxOspfHostnameRtrId_Type()
)
tmnxOspfHostnameRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOspfHostnameRtrId.setStatus("current")
_TmnxOspfHostnameName_Type = DisplayString
_TmnxOspfHostnameName_Object = MibTableColumn
tmnxOspfHostnameName = _TmnxOspfHostnameName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 49, 1, 2),
    _TmnxOspfHostnameName_Type()
)
tmnxOspfHostnameName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfHostnameName.setStatus("current")
_TmnxOspfScalarObjs_ObjectIdentity = ObjectIdentity
tmnxOspfScalarObjs = _TmnxOspfScalarObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 50)
)


class _TmnxOspfScalarDynHostnames_Type(TruthValue):
    """Custom type tmnxOspfScalarDynHostnames based on TruthValue"""
    defaultValue = 2


_TmnxOspfScalarDynHostnames_Type.__name__ = "TruthValue"
_TmnxOspfScalarDynHostnames_Object = MibScalar
tmnxOspfScalarDynHostnames = _TmnxOspfScalarDynHostnames_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 50, 1),
    _TmnxOspfScalarDynHostnames_Type()
)
tmnxOspfScalarDynHostnames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOspfScalarDynHostnames.setStatus("current")
_TmnxOspfSegmentRoutingTable_Object = MibTable
tmnxOspfSegmentRoutingTable = _TmnxOspfSegmentRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 51)
)
if mibBuilder.loadTexts:
    tmnxOspfSegmentRoutingTable.setStatus("current")
_TmnxOspfSegmentRoutingEntry_Object = MibTableRow
tmnxOspfSegmentRoutingEntry = _TmnxOspfSegmentRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 51, 1)
)
if mibBuilder.loadTexts:
    tmnxOspfSegmentRoutingEntry.setStatus("current")
_TmnxOspfSrLastChanged_Type = TimeStamp
_TmnxOspfSrLastChanged_Object = MibTableColumn
tmnxOspfSrLastChanged = _TmnxOspfSrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 51, 1, 1),
    _TmnxOspfSrLastChanged_Type()
)
tmnxOspfSrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOspfSrLastChanged.setStatus("current")


class _TmnxOspfSrMsdOverrideBmi_Type(Integer32):
    """Custom type tmnxOspfSrMsdOverrideBmi based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 12),
    )


_TmnxOspfSrMsdOverrideBmi_Type.__name__ = "Integer32"
_TmnxOspfSrMsdOverrideBmi_Object = MibTableColumn
tmnxOspfSrMsdOverrideBmi = _TmnxOspfSrMsdOverrideBmi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 51, 1, 2),
    _TmnxOspfSrMsdOverrideBmi_Type()
)
tmnxOspfSrMsdOverrideBmi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOspfSrMsdOverrideBmi.setStatus("current")


class _TmnxOspfSrMsdOverrideErld_Type(Integer32):
    """Custom type tmnxOspfSrMsdOverrideErld based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 15),
    )


_TmnxOspfSrMsdOverrideErld_Type.__name__ = "Integer32"
_TmnxOspfSrMsdOverrideErld_Object = MibTableColumn
tmnxOspfSrMsdOverrideErld = _TmnxOspfSrMsdOverrideErld_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 36, 51, 1, 3),
    _TmnxOspfSrMsdOverrideErld_Type()
)
tmnxOspfSrMsdOverrideErld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOspfSrMsdOverrideErld.setStatus("current")
_TmnxOspfNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxOspfNotifyPrefix = _TmnxOspfNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36)
)
_TmnxOspfNotifications_ObjectIdentity = ObjectIdentity
tmnxOspfNotifications = _TmnxOspfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0)
)
tmnxOspfGeneralEntry.registerAugmentions(
    ("TIMETRA-OSPF-NG-MIB",
     "tmnxOspfStatusEntry")
)
tmnxOspfStatusEntry.setIndexNames(*tmnxOspfGeneralEntry.getIndexNames())
tmnxOspfGeneralEntry.registerAugmentions(
    ("TIMETRA-OSPF-NG-MIB",
     "tmnxOspfStatisticsEntry")
)
tmnxOspfStatisticsEntry.setIndexNames(*tmnxOspfGeneralEntry.getIndexNames())
tmnxOspfGeneralEntry.registerAugmentions(
    ("TIMETRA-OSPF-NG-MIB",
     "tmnxOspfChangedEntry")
)
tmnxOspfChangedEntry.setIndexNames(*tmnxOspfGeneralEntry.getIndexNames())
tmnxOspfIfEntry.registerAugmentions(
    ("TIMETRA-OSPF-NG-MIB",
     "tmnxOspfIfStatsEntry")
)
tmnxOspfIfStatsEntry.setIndexNames(*tmnxOspfIfEntry.getIndexNames())
tmnxOspfVirtIfEntry.registerAugmentions(
    ("TIMETRA-OSPF-NG-MIB",
     "tmnxOspfVirtIfStatsEntry")
)
tmnxOspfVirtIfStatsEntry.setIndexNames(*tmnxOspfVirtIfEntry.getIndexNames())
tmnxOspfNbrEntry.registerAugmentions(
    ("TIMETRA-OSPF-NG-MIB",
     "tmnxOspfNbrStatsEntry")
)
tmnxOspfNbrStatsEntry.setIndexNames(*tmnxOspfNbrEntry.getIndexNames())
tmnxOspfVirtNbrEntry.registerAugmentions(
    ("TIMETRA-OSPF-NG-MIB",
     "tmnxOspfVirtNbrStatsEntry")
)
tmnxOspfVirtNbrStatsEntry.setIndexNames(*tmnxOspfVirtNbrEntry.getIndexNames())
tmnxOspfShamIfEntry.registerAugmentions(
    ("TIMETRA-OSPF-NG-MIB",
     "tmnxOspfShamIfStatsEntry")
)
tmnxOspfShamIfStatsEntry.setIndexNames(*tmnxOspfShamIfEntry.getIndexNames())
tmnxOspfShamNbrEntry.registerAugmentions(
    ("TIMETRA-OSPF-NG-MIB",
     "tmnxOspfShamNbrStatsEntry")
)
tmnxOspfShamNbrStatsEntry.setIndexNames(*tmnxOspfShamNbrEntry.getIndexNames())
tmnxOspfNgIfEntry.registerAugmentions(
    ("TIMETRA-OSPF-NG-MIB",
     "tmnxOspfNgIfOperEntry")
)
tmnxOspfNgIfOperEntry.setIndexNames(*tmnxOspfNgIfEntry.getIndexNames())
tmnxOspfNgIfEntry.registerAugmentions(
    ("TIMETRA-OSPF-NG-MIB",
     "tmnxOspfNgIfStatsEntry")
)
tmnxOspfNgIfStatsEntry.setIndexNames(*tmnxOspfNgIfEntry.getIndexNames())
tmnxOspfNgNbrEntry.registerAugmentions(
    ("TIMETRA-OSPF-NG-MIB",
     "tmnxOspfNgNbrStatsEntry")
)
tmnxOspfNgNbrStatsEntry.setIndexNames(*tmnxOspfNgNbrEntry.getIndexNames())
tmnxOspfGeneralEntry.registerAugmentions(
    ("TIMETRA-OSPF-NG-MIB",
     "tmnxOspfGeneralExEntry")
)
tmnxOspfGeneralExEntry.setIndexNames(*tmnxOspfGeneralEntry.getIndexNames())
tmnxOspfGeneralEntry.registerAugmentions(
    ("TIMETRA-OSPF-NG-MIB",
     "tmnxOspfSegmentRoutingEntry")
)
tmnxOspfSegmentRoutingEntry.setIndexNames(*tmnxOspfGeneralEntry.getIndexNames())

# Managed Objects groups

tmnxOspfGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 1)
)
tmnxOspfGeneralGroup.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralLastChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdminState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfASBdrRtrStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRFC1583Compatibility"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExtLsdbLimit"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMulticastExtensions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExitOverflowInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfDemandExtensions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfReferenceBandwidth"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfStrictLsaChecking"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRestartSupport"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRestartInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPreference"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExternalPreference"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExportPolicy1"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExportPolicy2"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExportPolicy3"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExportPolicy4"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExportPolicy5"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfManualSpfTrigger"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOverloadAdmState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOverloadInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfBootOverloadAdmState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfBootOverloadInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOverloadStubs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSpfMaxWait"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSpfInitialWait"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSpfSecondWait"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLsaGenMaxWait"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLsaGenInitialWait"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLsaGenSecondWait"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLsaArrivalWait"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfTESupport"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfUnicastImport"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMulticastImport"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGREnable"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGRHelperMode"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaBdrRtrStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfBackBoneRouter"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfStubRouterSupport"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsScopeLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsScopeLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsScopeUnkLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsScopeUnkLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExternLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExternLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOpaqueLsaSupport"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRestartStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRestartAge"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRestartExitRc"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfDiscontinuityTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastEnabledTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastOvrflwEnteredTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastOverflowExitTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfInOverflowState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOverloadOperState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOverloadRemInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastOverloadEntrdTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastOverloadExitTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastOverloadEnterCode"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastOverloadExitCode"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastExtSpfRunTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastFullSpfRunTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastFullSpfInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMaxSpfRunInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMinSpfRunInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAvgSpfRunInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExtSpfRunInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRoutesSubmitted"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOriginateNewLsas"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRxNewLsas"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFullSpfRuns"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExtSpfRuns"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIncremntlInterSpfRuns"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIncrementalExtSpfRuns"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSpfAttemptsFailed"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNumTimesInOverload"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNumTimesInOverflow"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRoutesAddsFailed"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRoutesDelsFailed"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRoutesModsFailed"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsaCountEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsLsdbEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsdbEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkLsdbEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMD5KeyEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfMD5KeyEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCSPFRequests"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCSPFDroppedRequests"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCSPFPathsFound"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCSPFPathsNotFound"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMD5KeyTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfMD5KeyTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIgnoreDNBit"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSuppressDNBit"))
)
if mibBuilder.loadTexts:
    tmnxOspfGeneralGroup.setStatus("obsolete")

tmnxOspfAreaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 2)
)
tmnxOspfAreaGroup.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLastChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfImportAsExtern"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaSummary"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaRangeBlackhole"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfStubMetric"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaStubMetricType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaOriginateDefault"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaNssaRedistribute"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaNssaTranslatorRole"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaNssaTranslatorStabInt"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaBdrRtrCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAsBdrRtrCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaScopeLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaScopeLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaScopeUnkLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaScopeUnkLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaNssaTranslatorState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaActiveInterfaces"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaInterfaceCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaVirtualLinkCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLastSpfRunTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaSpfRuns"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaNssaTranslatorEvents"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaNeighborCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsaCountNumber"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsLsdbSequence"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsLsdbAge"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsLsdbChecksum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsLsdbAdvertisement"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsLsdbTypeKnown"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsdbSequence"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsdbAge"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsdbChecksum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsdbAdvertisement"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsdbTypeKnown"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkLsdbSequence"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkLsdbAge"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkLsdbChecksum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkLsdbAdvertisement"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkLsdbTypeKnown"))
)
if mibBuilder.loadTexts:
    tmnxOspfAreaGroup.setStatus("obsolete")

tmnxOspfHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 3)
)
tmnxOspfHostGroup.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostMetric"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostLastChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostAreaID"))
)
if mibBuilder.loadTexts:
    tmnxOspfHostGroup.setStatus("current")

tmnxOspfIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 4)
)
tmnxOspfIfGroup.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLastChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAreaId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfCfgType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAdminState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRtrPriority"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTransitDelay"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRetransInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfHelloInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRtrDeadInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfPollInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMulticastForwarding"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfCfgMTU"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfCfgMetric"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfPassive"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAdvtSubnet"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDemand"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDemandNbrProbe"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDemandNbrProbeRetxLimit"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDemandNbrProbeInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAuthType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAuthKey"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLastEnabledTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfOperMTU"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMetricValue"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDRId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDRIpAddrType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDRIpAddr"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBDRId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBDRIpAddrType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBDRIpAddr"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLinkLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLinkLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLinkUnkLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLinkUnkLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMD5TransmitKeyId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLocalIpAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLocalIpAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMD5NumKeys"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfEnableBfd"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfEvents"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTxPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTxHellos"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTxDBDs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTxLSRs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTxLSUs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTxLSAcks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxHellos"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxDBDs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxLSRs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxLSUs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxLSAcks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDiscardPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRetransmitOuts"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadVersions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadNetworks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadVirtualLinks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadAreas"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadDstAddrs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadNeighbors"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadPacketTypes"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfNeighborCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLastEventTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadLengths"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadHelloIntervals"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadDeadIntervals"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadOptions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxBadChecksums"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadAuthTypes"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAuthFailures"))
)
if mibBuilder.loadTexts:
    tmnxOspfIfGroup.setStatus("obsolete")

tmnxOspfVirtIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 5)
)
tmnxOspfVirtIfGroup.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfLastChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfIndex"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfInstId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfAdminStat"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfTransitDelay"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfRetransInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfHelloInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfRtrDeadInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfAuthType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfAuthKey"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfLastEnabledTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfCost"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfLinkLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfLinkLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfLinkUnkLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfLinkUnkLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfMD5TransmitKeyId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfLocalIpAddrType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfLocalIpAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfMD5NumKeys"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfEvents"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfTxPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfTxHellos"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfTxDBDs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfTxLSRs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfTxLSUs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfTxLSAcks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfRxPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfRxHellos"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfRxDBDs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfRxLSRs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfRxLSUs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfRxLSAcks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfDiscardPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfRetransmitOuts"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfBadVersions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfBadNetworks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfBadAreas"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfBadDstAddrs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfBadNeighbors"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfBadPacketTypes"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfLastEventTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfBadLengths"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfBadHelloIntervls"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfBadDeadIntervals"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfBadOptions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfRxBadChecksums"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfBadAuthTypes"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfAuthFailures"))
)
if mibBuilder.loadTexts:
    tmnxOspfVirtIfGroup.setStatus("current")

tmnxOspfNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 6)
)
tmnxOspfNbrGroup.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrOptions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrPriority"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrHelloSuppressed"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrIfId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrRestartHelperStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrRestartHelperAge"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrRestartHelperExitRc"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrUpTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrLastEventTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrDeadTimeOutstanding"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrLastRestartTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrRestartReason"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrBfdTracking"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrDrId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrBdrId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrEvents"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrLsRetransQLen"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrBadNbrStates"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrLsaInstallFailed"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrBadSeqNums"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrBadMTUs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrBadPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrLsaNotInLsdbs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrOptionMismatches"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrDuplicates"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrNumRestarts"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrStorageType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrLastChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrPriority"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrRtrId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrState"))
)
if mibBuilder.loadTexts:
    tmnxOspfNbrGroup.setStatus("obsolete")

tmnxOspfVirtNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 7)
)
tmnxOspfVirtNbrGroup.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrIfIndex"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrIfInstId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrOptions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrHelloSuppressed"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrIfId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrRestartHelperStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrRestartHelperAge"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrRestartHelperExitRc"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrUpTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrLastEventTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrDeadTmeOutstng"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrLastRestartTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrRestartReason"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrEvents"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrLsRetransQLen"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrBadNbrStates"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrLsaInstallFail"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrBadSeqNums"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrBadMTUs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrBadPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrLsaNotInLsdbs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrOptionMismatch"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrDuplicates"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrNumRestarts"))
)
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrGroup.setStatus("current")

tmnxOspfAreaAggrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 8)
)
tmnxOspfAreaAggrGroup.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrLastChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrEffect"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrRouteTag"))
)
if mibBuilder.loadTexts:
    tmnxOspfAreaAggrGroup.setStatus("current")

tmnxOspfMD5KeyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 9)
)
tmnxOspfMD5KeyGroup.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMD5KeyStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMD5KeyKey"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMD5KeyStartTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMD5KeyStopTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfMD5KeyStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfMD5KeyKey"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfMD5KeyStartTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfMD5KeyStopTime"))
)
if mibBuilder.loadTexts:
    tmnxOspfMD5KeyGroup.setStatus("obsolete")

tmnxOspfNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 10)
)
tmnxOspfNotifyObjsGroup.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfSetTrap"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfConfigErrorType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddress"))
)
if mibBuilder.loadTexts:
    tmnxOspfNotifyObjsGroup.setStatus("current")

tmnxOspfGeneralV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 12)
)
tmnxOspfGeneralV5v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralLastChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdminState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfASBdrRtrStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRFC1583Compatibility"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExtLsdbLimit"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMulticastExtensions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExitOverflowInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfDemandExtensions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfReferenceBandwidth"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfStrictLsaChecking"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRestartSupport"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRestartInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPreference"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExternalPreference"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExportPolicy1"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExportPolicy2"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExportPolicy3"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExportPolicy4"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExportPolicy5"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfManualSpfTrigger"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOverloadAdmState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOverloadInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfBootOverloadAdmState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfBootOverloadInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOverloadStubs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSpfMaxWait"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSpfInitialWait"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSpfSecondWait"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLsaGenMaxWait"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLsaGenInitialWait"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLsaGenSecondWait"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLsaArrivalWait"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfTESupport"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfUnicastImport"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMulticastImport"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGREnable"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGRHelperMode"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaBdrRtrStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfBackBoneRouter"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfStubRouterSupport"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsScopeLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsScopeLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsScopeUnkLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsScopeUnkLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExternLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExternLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOpaqueLsaSupport"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRestartStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRestartAge"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRestartExitRc"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfDiscontinuityTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastEnabledTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastOvrflwEnteredTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastOverflowExitTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfInOverflowState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOverloadOperState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOverloadRemInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastOverloadEntrdTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastOverloadExitTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastOverloadEnterCode"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastOverloadExitCode"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastExtSpfRunTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastFullSpfRunTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastFullSpfInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMaxSpfRunInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMinSpfRunInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAvgSpfRunInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExtSpfRunInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRoutesSubmitted"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOriginateNewLsas"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRxNewLsas"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFullSpfRuns"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExtSpfRuns"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIncremntlInterSpfRuns"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIncrementalExtSpfRuns"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSpfAttemptsFailed"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNumTimesInOverload"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNumTimesInOverflow"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRoutesAddsFailed"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRoutesDelsFailed"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRoutesModsFailed"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsaCountEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsLsdbEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsdbEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkLsdbEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMD5KeyEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfMD5KeyEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCSPFRequests"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCSPFDroppedRequests"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCSPFPathsFound"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCSPFPathsNotFound"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMD5KeyTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfMD5KeyTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRowStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOperRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsbrDomainId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIgnoreDNBit"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSuppressDNBit"))
)
if mibBuilder.loadTexts:
    tmnxOspfGeneralV5v0Group.setStatus("current")

tmnxOspfIfV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 13)
)
tmnxOspfIfV5v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLastChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAreaId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfCfgType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAdminState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRtrPriority"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTransitDelay"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRetransInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfHelloInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRtrDeadInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfPollInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMulticastForwarding"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfCfgMTU"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfCfgMetric"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfPassive"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAdvtSubnet"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDemand"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDemandNbrProbe"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDemandNbrProbeRetxLimit"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDemandNbrProbeInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAuthType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAuthKey"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLastEnabledTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfOperMTU"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMetricValue"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDRId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDRIpAddrType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDRIpAddr"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBDRId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBDRIpAddrType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBDRIpAddr"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLinkLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLinkLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLinkUnkLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLinkUnkLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMD5TransmitKeyId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLocalIpAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLocalIpAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMD5NumKeys"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfEnableBfd"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRemainDownOnFail"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfEvents"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTxPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTxHellos"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTxDBDs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTxLSRs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTxLSUs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTxLSAcks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxHellos"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxDBDs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxLSRs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxLSUs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxLSAcks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDiscardPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRetransmitOuts"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadVersions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadNetworks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadVirtualLinks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadAreas"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadDstAddrs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadNeighbors"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadPacketTypes"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfNeighborCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLastEventTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadLengths"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadHelloIntervals"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadDeadIntervals"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadOptions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxBadChecksums"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadAuthTypes"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAuthFailures"))
)
if mibBuilder.loadTexts:
    tmnxOspfIfV5v0Group.setStatus("obsolete")

tmnxOspfIfV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 14)
)
tmnxOspfIfV6v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTeMetric"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTeState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAdminGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLdpSyncState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLdpSyncMaxMetric"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLdpSyncTimerState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLdpSyncTimeLeft"))
)
if mibBuilder.loadTexts:
    tmnxOspfIfV6v0Group.setStatus("obsolete")

tmnxOspfGeneralV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 15)
)
tmnxOspfGeneralV6v0Group.setObjects(
    ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLdpSyncAdminState")
)
if mibBuilder.loadTexts:
    tmnxOspfGeneralV6v0Group.setStatus("current")

tmnxOspfNotifyObjsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 17)
)
tmnxOspfNotifyObjsV6v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfIpName"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfEvent"))
)
if mibBuilder.loadTexts:
    tmnxOspfNotifyObjsV6v0Group.setStatus("current")

tmnxOspfGeneralV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 18)
)
tmnxOspfGeneralV6v1Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfVpnDomainType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVpnDomainId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVpnTag"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSuperBackBone"))
)
if mibBuilder.loadTexts:
    tmnxOspfGeneralV6v1Group.setStatus("current")

tmnxOspfShamLinksV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 19)
)
tmnxOspfShamLinksV7v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfLastChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfAreaId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfAdminState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfTransitDelay"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRetransInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfHelloInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRtrDeadInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfCfgMetric"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfAuthType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfAuthKey"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfLastEnabledTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfLinkLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfLinkLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfLinkUnkLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfLinkUnkLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfMD5TransmitKeyId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfLocalIpAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfLocalIpAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfMD5NumKeys"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfEvents"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfTxPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfTxHellos"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfTxDBDs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfTxLSRs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfTxLSUs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfTxLSAcks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRxPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRxHellos"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRxDBDs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRxLSRs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRxLSUs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRxLSAcks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfDiscardPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRetransmitOuts"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadVersions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadNetworks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadAreas"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadDstAddrs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadNeighbors"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadPacketTypes"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfLastEventTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadLengths"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadHelloIntervals"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadDeadIntervals"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadOptions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRxBadChecksums"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadAuthTypes"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfAuthFailures"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfMD5KeyStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfMD5KeyKey"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfMD5KeyStartTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfMD5KeyStopTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrOptions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrHelloSuppressed"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrIfId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrRestartHelperStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrRestartHelperAge"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrRestartHelperExitRc"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrUpTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrLastEventTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrDeadTmeOutstng"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrLastRestartTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrRestartReason"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrEvents"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrLsRetransQLen"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrBadNbrStates"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrLsaInstallFail"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrBadSeqNums"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrBadMTUs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrBadPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrLsaNotInLsdbs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrOptionMismatch"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrDuplicates"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrNumRestarts"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfMD5KeyEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfMD5KeyTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaShamLinkCount"))
)
if mibBuilder.loadTexts:
    tmnxOspfShamLinksV7v0Group.setStatus("obsolete")

tmnxOspfNotifyObjsV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 21)
)
tmnxOspfNotifyObjsV7v0Group.setObjects(
    ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFailureReasonCode")
)
if mibBuilder.loadTexts:
    tmnxOspfNotifyObjsV7v0Group.setStatus("current")

tmnxOspfGeneralV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 22)
)
tmnxOspfGeneralV7v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfLdpOverRsvp"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExportLimit"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExportLimitLogPercent"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfTotalExportedRoutes"))
)
if mibBuilder.loadTexts:
    tmnxOspfGeneralV7v0Group.setStatus("current")

tmnxOspfAreaV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 24)
)
tmnxOspfAreaV8v0Group.setObjects(
    ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaKeyRolloverInterval")
)
if mibBuilder.loadTexts:
    tmnxOspfAreaV8v0Group.setStatus("obsolete")

tmnxOspfVirtIfV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 25)
)
tmnxOspfVirtIfV8v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfInboundSAName"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfOutboundSAName"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfOperInbSAName"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfOperInbSANameTemp"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfOperOutbSAName"))
)
if mibBuilder.loadTexts:
    tmnxOspfVirtIfV8v0Group.setStatus("current")

tmnxOspfIfV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 26)
)
tmnxOspfIfV8v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfInboundSAName"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfOutboundSAName"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfOperInbSAName"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfOperInbSANameTemp"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfOperOutbSAName"))
)
if mibBuilder.loadTexts:
    tmnxOspfIfV8v0Group.setStatus("current")

tmnxOspfNotifyObjsV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 27)
)
tmnxOspfNotifyObjsV8v0Group.setObjects(
    ("TIMETRA-OSPF-NG-MIB", "tmnxOspfBadPacketErrType")
)
if mibBuilder.loadTexts:
    tmnxOspfNotifyObjsV8v0Group.setStatus("current")

tmnxOspfGeneralV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 28)
)
tmnxOspfGeneralV8v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRsvpShortcut"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdvertiseTunnelLink"))
)
if mibBuilder.loadTexts:
    tmnxOspfGeneralV8v0Group.setStatus("current")

tmnxOspfAreaV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 29)
)
tmnxOspfAreaV9v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLastChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfImportAsExtern"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaSummary"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaRangeBlackhole"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfStubMetric"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaStubMetricType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaOriginateDefault"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaNssaRedistribute"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaNssaTranslatorRole"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaNssaTranslatorStabInt"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaBdrRtrCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAsBdrRtrCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaScopeLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaScopeLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaScopeUnkLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaScopeUnkLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaNssaTranslatorState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaActiveInterfaces"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaInterfaceCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaVirtualLinkCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLastSpfRunTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaSpfRuns"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaNssaTranslatorEvents"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaNeighborCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsaCountNumber"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsLsdbSequence"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsLsdbAge"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsLsdbChecksum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsLsdbAdvertisement"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsLsdbTypeKnown"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsdbSequence"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsdbAge"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsdbChecksum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsdbAdvertisement"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsdbTypeKnown"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaKeyRolloverInterval"))
)
if mibBuilder.loadTexts:
    tmnxOspfAreaV9v0Group.setStatus("current")

tmnxOspfNgLinkLsdbV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 30)
)
tmnxOspfNgLinkLsdbV9v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbSequence"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbAge"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbChecksum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbAdvertisement"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbTypeKnown"))
)
if mibBuilder.loadTexts:
    tmnxOspfNgLinkLsdbV9v0Group.setStatus("current")

tmnxOspfNgNbrV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 31)
)
tmnxOspfNgNbrV9v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrOptions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrPriority"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrHelloSuppressed"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrIfId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrRestartHelperStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrRestartHelperAge"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrRestartHelperExitRc"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrUpTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrLastEventTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrDeadTimeOutstanding"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrLastRestartTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrRestartReason"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrBfdTracking"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrDrId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrBdrId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrEvents"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrLsRetransQLen"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrBadNbrStates"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrLsaInstallFailed"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrBadSeqNums"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrBadMTUs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrBadPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrLsaNotInLsdbs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrOptionMismatches"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrDuplicates"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrNumRestarts"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrLastChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrPriority"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrRtrId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrStorageType"))
)
if mibBuilder.loadTexts:
    tmnxOspfNgNbrV9v0Group.setStatus("current")

tmnxOspfNgIfV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 32)
)
tmnxOspfNgIfV9v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfLastChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfCfgType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfAdminState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfRtrPriority"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfTransitDelay"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfRetransInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfHelloInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfRtrDeadInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfPollInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfCfgMTU"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfCfgMetric"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfPassive"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfAdvtSubnet"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfAuthType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfAuthKey"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfEnableBfd"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfRemainDownOnFail"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfInboundSAName"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfOutboundSAName"))
)
if mibBuilder.loadTexts:
    tmnxOspfNgIfV9v0Group.setStatus("current")

tmnxOspfNgIfOperV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 33)
)
tmnxOspfNgIfOperV9v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfLastEnabledTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfOperMTU"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfMetricValue"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfDRId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfDRIpAddrType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfDRIpAddr"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfBDRId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfBDRIpAddrType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfBDRIpAddr"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfLinkLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfLinkLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfMD5TransmitKeyId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfLocalIpAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfLocalIpAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfMD5NumKeys"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfTeMetric"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfTeState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfAdminGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfLdpSyncState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfLdpSyncMaxMetric"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfLdpSyncTimerState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfLdpSyncTimeLeft"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfOperInbSAName"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfOperInbSANameTemp"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfOperOutbSAName"))
)
if mibBuilder.loadTexts:
    tmnxOspfNgIfOperV9v0Group.setStatus("current")

tmnxOspfNgIfStatsV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 34)
)
tmnxOspfNgIfStatsV9v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfEvents"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfTxPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfTxHellos"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfTxDBDs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfTxLSRs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfTxLSUs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfTxLSAcks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfRxPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfRxHellos"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfRxDBDs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfRxLSRs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfRxLSUs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfRxLSAcks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfDiscardPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfRetransmitOuts"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfBadVersions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfBadNetworks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfBadVirtualLinks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfBadAreas"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfBadDstAddrs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfBadNeighbors"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfBadPacketTypes"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfNeighborCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfLastEventTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfBadLengths"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfBadHelloIntervals"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfBadDeadIntervals"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfBadOptions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfRxBadChecksums"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfBadAuthTypes"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfAuthFailures"))
)
if mibBuilder.loadTexts:
    tmnxOspfNgIfStatsV9v0Group.setStatus("current")

tmnxOspfMD5KeyV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 35)
)
tmnxOspfMD5KeyV9v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfMD5KeyStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfMD5KeyKey"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfMD5KeyStartTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfMD5KeyStopTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfMD5KeyStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfMD5KeyKey"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfMD5KeyStartTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfMD5KeyStopTime"))
)
if mibBuilder.loadTexts:
    tmnxOspfMD5KeyV9v0Group.setStatus("obsolete")

tmnxOspfObsoletedObjV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 37)
)
tmnxOspfObsoletedObjV9v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAdminGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAdminState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAdvtSubnet"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAreaId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAuthFailures"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAuthKey"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAuthType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBDRId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBDRIpAddr"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBDRIpAddrType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadAreas"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadAuthTypes"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadDeadIntervals"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadDstAddrs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadHelloIntervals"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadLengths"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadNeighbors"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadNetworks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadOptions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadPacketTypes"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadVersions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadVirtualLinks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfCfgMTU"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfCfgMetric"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfCfgType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDRId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDRIpAddr"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDRIpAddrType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDemand"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDemandNbrProbe"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDemandNbrProbeInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDemandNbrProbeRetxLimit"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfDiscardPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfEnableBfd"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfEvents"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfHelloInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfInboundSAName"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLastChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLastEnabledTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLastEventTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLdpSyncMaxMetric"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLdpSyncState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLdpSyncTimeLeft"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLdpSyncTimerState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLinkLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLinkLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLinkUnkLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLinkUnkLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLocalIpAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLocalIpAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMD5KeyKey"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMD5KeyStartTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMD5KeyStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMD5KeyStopTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMD5NumKeys"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMD5TransmitKeyId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMetricValue"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfMulticastForwarding"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfNeighborCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfOperInbSAName"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfOperInbSANameTemp"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfOperMTU"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfOperOutbSAName"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfOutboundSAName"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfPassive"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfPollInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRemainDownOnFail"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRetransInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRetransmitOuts"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRtrDeadInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRtrPriority"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxBadChecksums"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxDBDs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxHellos"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxLSAcks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxLSRs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxLSUs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTeMetric"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTeState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTransitDelay"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTxDBDs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTxHellos"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTxLSAcks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTxLSRs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTxLSUs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTxPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkLsdbAdvertisement"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkLsdbAge"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkLsdbChecksum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkLsdbSequence"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkLsdbTypeKnown"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrBadMTUs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrBadNbrStates"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrBadPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrBadSeqNums"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrBdrId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrBfdTracking"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrDeadTimeOutstanding"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrDrId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrDuplicates"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrEvents"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrHelloSuppressed"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrIfId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrLastEventTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrLastRestartTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrLsRetransQLen"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrLsaInstallFailed"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrLsaNotInLsdbs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrNumRestarts"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrOptionMismatches"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrOptions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrPriority"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrRestartHelperAge"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrRestartHelperExitRc"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrRestartHelperStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrRestartReason"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrUpTime"))
)
if mibBuilder.loadTexts:
    tmnxOspfObsoletedObjV9v0Group.setStatus("current")

tmnxOspfGeneralV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 38)
)
tmnxOspfGeneralV10v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfImportPolicy1"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfImportPolicy2"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfImportPolicy3"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfImportPolicy4"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfImportPolicy5"))
)
if mibBuilder.loadTexts:
    tmnxOspfGeneralV10v0Group.setStatus("current")

tmnxOspfFRRV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 39)
)
tmnxOspfFRRV10v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfLoopfreeAlternate"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLoopfreeAltExclude"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfLoopfreeAltExclude"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLfaSpfRuns"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastLfaSpfRunTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLfaNodesCovered"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLfaTotalNodes"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLfaCoverage"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLfaPfxCovered"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLfaTotalPfx"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLfaPfxCoverage"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPathMetric"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPathLfaIfIndex"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPathLfaType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPathLfaNhopRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPathLfaMetric"))
)
if mibBuilder.loadTexts:
    tmnxOspfFRRV10v0Group.setStatus("current")

tmnxOspfFRRV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 40)
)
tmnxOspfFRRV11v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfLsaFilterOut"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLsaAccumulate"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRedistDelay"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIncrSpfWait"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaNssaAdjCheck"))
)
if mibBuilder.loadTexts:
    tmnxOspfFRRV11v0Group.setStatus("current")

tmnxOspfGeneralV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 41)
)
tmnxOspfGeneralV11v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfPathNhOwner"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPathLfaNhOwner"))
)
if mibBuilder.loadTexts:
    tmnxOspfGeneralV11v0Group.setStatus("current")

tmnxOspfGeneralV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 42)
)
tmnxOspfGeneralV12v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralExLastChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdvRtrCapability"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAdvRtrCapability"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfAdvRtrCapability"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfAuthKeyChain"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfAuthKeyChain"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfAuthKeyChain"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOverloadInclExt2"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLFAExcludePolicy1"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLFAExcludePolicy2"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLFAExcludePolicy3"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLFAExcludePolicy4"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLFAExcludePolicy5"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfRouteNHTemplate"))
)
if mibBuilder.loadTexts:
    tmnxOspfGeneralV12v0Group.setStatus("current")

tmnxOspfGeneralV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 43)
)
tmnxOspfGeneralV13v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfPriorityUpdate"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRibPriorityListHigh"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLdpOverRsvpStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRsvpShortcutStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdvertiseTunlLinkStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrPfxSidFlags"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrPfxSidActive"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfStatsRlfaRuns"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfStatsSidLabelRangeErrs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfStatsSidDupErrs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfSidType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfSidValue"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrSidType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrSidValue"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPrefixSidRangeType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPrefixSidRangeStartLabel"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPrefixSidRangeMaxIdx"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrAdminState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfTunnelTablePreference"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRemoteLFA"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMaxPqCost"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfTunnelMtu"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdvRtrLsaLimit"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdvRtrLsaLimitTimeout"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOvldLsaLimitRemInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdvRtrLsaLimitWarning"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdvRtrLsaLimitLogOnly"))
)
if mibBuilder.loadTexts:
    tmnxOspfGeneralV13v0Group.setStatus("current")

tmnxOspfNotifyObjsV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 44)
)
tmnxOspfNotifyObjsV13v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifPfxSidRangeStartLbl"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifPfxSidRangeMaxIdx"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifPfxNhAdvRtr"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyDescription"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifSrgbRangeStartLbl"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifSrgbRangeMaxIdx"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifSrgbAdvRtrID"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifSrgbAreaId"))
)
if mibBuilder.loadTexts:
    tmnxOspfNotifyObjsV13v0Group.setStatus("current")

tmnxOspfMD5KeyV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 46)
)
tmnxOspfMD5KeyV13v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfMD5KeyStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfMD5KeyKey"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfMD5KeyStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfMD5KeyKey"))
)
if mibBuilder.loadTexts:
    tmnxOspfMD5KeyV13v0Group.setStatus("current")

tmnxOspfShamLinksV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 47)
)
tmnxOspfShamLinksV13v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfLastChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfAreaId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfAdminState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfTransitDelay"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRetransInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfHelloInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRtrDeadInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfCfgMetric"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfAuthType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfAuthKey"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfLastEnabledTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfLinkLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfLinkLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfLinkUnkLsaCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfLinkUnkLsaCksumSum"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfMD5TransmitKeyId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfLocalIpAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfLocalIpAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfMD5NumKeys"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfEvents"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfTxPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfTxHellos"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfTxDBDs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfTxLSRs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfTxLSUs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfTxLSAcks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRxPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRxHellos"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRxDBDs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRxLSRs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRxLSUs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRxLSAcks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfDiscardPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRetransmitOuts"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadVersions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadNetworks"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadAreas"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadDstAddrs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadNeighbors"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadPacketTypes"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfLastEventTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadLengths"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadHelloIntervals"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadDeadIntervals"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadOptions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRxBadChecksums"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadAuthTypes"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfAuthFailures"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfMD5KeyStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfMD5KeyKey"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrOptions"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrHelloSuppressed"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrIfId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrRestartHelperStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrRestartHelperAge"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrRestartHelperExitRc"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrUpTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrLastEventTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrDeadTmeOutstng"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrLastRestartTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrRestartReason"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrEvents"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrLsRetransQLen"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrBadNbrStates"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrLsaInstallFail"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrBadSeqNums"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrBadMTUs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrBadPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrLsaNotInLsdbs"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrOptionMismatch"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrDuplicates"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrNumRestarts"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfMD5KeyEntries"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfMD5KeyTableChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaShamLinkCount"))
)
if mibBuilder.loadTexts:
    tmnxOspfShamLinksV13v0Group.setStatus("current")

tmnxOspfObsoletedObjV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 48)
)
tmnxOspfObsoletedObjV13v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfMD5KeyStartTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfMD5KeyStopTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfMD5KeyStartTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfMD5KeyStopTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfMD5KeyStartTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfMD5KeyStopTime"))
)
if mibBuilder.loadTexts:
    tmnxOspfObsoletedObjV13v0Group.setStatus("current")

tmnxOspfNotifyObjsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 49)
)
tmnxOspfNotifyObjsV12v0Group.setObjects(
    ("TIMETRA-OSPF-NG-MIB", "tmnxOspfBfdSessSetupFailReason")
)
if mibBuilder.loadTexts:
    tmnxOspfNotifyObjsV12v0Group.setStatus("current")

tmnxOspfSegmentRoutingTEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 51)
)
tmnxOspfSegmentRoutingTEGroup.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrAdjSidHold"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfDatabaseExport"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfDbExportIdentifierSet"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfDbExportIdentifierLow"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfDbExportIdentifierHigh"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfBgpLsIdentifierSet"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfBgpLsIdentifier"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaDbExportExclude"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfSidProtection"))
)
if mibBuilder.loadTexts:
    tmnxOspfSegmentRoutingTEGroup.setStatus("current")

tmnxOspfGeneralV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 52)
)
tmnxOspfGeneralV14v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfBackupNodeSidPfxType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfBackupNodeSidPfx"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfBackupNodeSidPfxLen"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfBackupNodeSidType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfBackupNodeSidValue"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfDbAsn"))
)
if mibBuilder.loadTexts:
    tmnxOspfGeneralV14v0Group.setStatus("current")

tmnxOspfGeneralV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 53)
)
tmnxOspfGeneralV15v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfExtendedLsa"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaExtendedLsa"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrEntropyLabel"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOverrideTunnelElc"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfTiLfa"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMaxSrFrrLabels"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaImportPolicy1"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaImportPolicy2"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaImportPolicy3"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaImportPolicy4"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaImportPolicy5"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaExportPolicy1"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaExportPolicy2"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaExportPolicy3"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaExportPolicy4"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaExportPolicy5"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsdbImportFltrd"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsdbExportFltrd"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOperState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrLfaStatsTotalSid"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrLfaStatsLfaCovered"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrLfaStatsRLfaCovered"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrLfaStatsTiLfaCovered"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfStatsTiLfaRuns"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfSidClearNFlag"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfAdjSidType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfAdjSidValue"))
)
if mibBuilder.loadTexts:
    tmnxOspfGeneralV15v0Group.setStatus("current")

tmnxOspfIgpSC15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 54)
)
tmnxOspfIgpSC15v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfIgpSCAdminState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIgpSCTunnNextHopLstCh"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIgpSCTNHResolution"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIgpSCTNHResFilterRsvp"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIgpSCTNHResFilterSrTe"))
)
if mibBuilder.loadTexts:
    tmnxOspfIgpSC15v0Group.setStatus("current")

tmnxOspfObsolete15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 55)
)
tmnxOspfObsolete15v0Group.setObjects(
    ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRsvpShortcut")
)
if mibBuilder.loadTexts:
    tmnxOspfObsolete15v0Group.setStatus("current")

tmnxOspfObsolete16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 56)
)
tmnxOspfObsolete16v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfCfgNbrStorageType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrPfxSidActive"))
)
if mibBuilder.loadTexts:
    tmnxOspfObsolete16v0Group.setStatus("current")

tmnxOspfGeneralV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 57)
)
tmnxOspfGeneralV16v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrMsAdminState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetRowStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetLastChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetSidType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetSidValue"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetParallel"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetAdvertise"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetDynSidValue"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetTunlDestType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetTunlDestIp"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetNbrRtrId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetMembersCount"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetActiveMembers"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetUpTime"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetMtu"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAdjSetRowStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAdjSetLastChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetNhopType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetNhop"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrlbReservedLblBlockName"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrExportTunnelTableProt"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSRMSSidMapRowStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSRMSSidMapLastCh"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSRMSSidMapPrefixType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSRMSSidMapPrefix"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSRMSSidMapPrefixLength"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSRMSSidMapNodeSidRange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSRMSSidMapScope"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSRMSSidMapScopeArea"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrPfxSidSRMS"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrPfxSidSRMSSelected"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRemoteLfaNodeProtect"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRemoteLfaMaxPqNodes"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfTiLfaNodeProtect"))
)
if mibBuilder.loadTexts:
    tmnxOspfGeneralV16v0Group.setStatus("current")

tmnxOspfNotifyObjsV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 58)
)
tmnxOspfNotifyObjsV16v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyIfIndex"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyNbrRouterId"))
)
if mibBuilder.loadTexts:
    tmnxOspfNotifyObjsV16v0Group.setStatus("current")

tmnxOspfGeneralV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 60)
)
tmnxOspfGeneralV19v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfMultiInstance"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfReferenceBandwidthU64Hi"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfReferenceBandwidthU64Lo"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfLBAdminWeight"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfEgressStatsNodeSid"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfEgressStatsAdjSid"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfEgressStatsAdjSet"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIngressStatsNodeSid"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIngressStatsAdjSid"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIngressStatsAdjSet"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOverloadInclExt1"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSidStatsSidType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSidStatsPrefixType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSidStatsPrefix"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSidStatsPrefixLength"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSidStatsIfIndex"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSidStatsAdjSet"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSidStatsIngressOperState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSidStatsIngressOctets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSidStatsIngressPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSidStatsEgressOperState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSidStatsEgressOctets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSidStatsEgressPackets"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAdvertiseNeProfile"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostnameName"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfScalarDynHostnames"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrClassForwarding"))
)
if mibBuilder.loadTexts:
    tmnxOspfGeneralV19v0Group.setStatus("current")

tmnxOspfObsolete19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 61)
)
tmnxOspfObsolete19v0Group.setObjects(
    ("TIMETRA-OSPF-NG-MIB", "tmnxOspfDiscontinuityTime")
)
if mibBuilder.loadTexts:
    tmnxOspfObsolete19v0Group.setStatus("current")

tmnxOspfNotifyObjsV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 62)
)
tmnxOspfNotifyObjsV19v0Group.setObjects(
    ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifStatsIndexStatus")
)
if mibBuilder.loadTexts:
    tmnxOspfNotifyObjsV19v0Group.setStatus("current")

tmnxOspfNetworkElementV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 64)
)
tmnxOspfNetworkElementV16v0Group.setObjects(
    ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAdvertiseNeProfile")
)
if mibBuilder.loadTexts:
    tmnxOspfNetworkElementV16v0Group.setStatus("obsolete")

tmnxOspfGeneralV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 65)
)
tmnxOspfGeneralV20v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaBierTemplate"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaBierTemplAdminState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrLastChanged"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrMsdOverrideBmi"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrMsdOverrideErld"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfTeOptsSrTe"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfTxFailures"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfTxFailures"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfTxFailures"))
)
if mibBuilder.loadTexts:
    tmnxOspfGeneralV20v0Group.setStatus("current")


# Notification objects

tmnxOspfVirtIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 1)
)
tmnxOspfVirtIfStateChange.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfState"))
)
if mibBuilder.loadTexts:
    tmnxOspfVirtIfStateChange.setStatus(
        "current"
    )

tmnxOspfNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 2)
)
tmnxOspfNbrStateChange.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrState"))
)
if mibBuilder.loadTexts:
    tmnxOspfNbrStateChange.setStatus(
        "obsolete"
    )

tmnxOspfVirtNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 3)
)
tmnxOspfVirtNbrStateChange.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrState"))
)
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrStateChange.setStatus(
        "current"
    )

tmnxOspfIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 4)
)
tmnxOspfIfConfigError.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfConfigErrorType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxPackets"))
)
if mibBuilder.loadTexts:
    tmnxOspfIfConfigError.setStatus(
        "obsolete"
    )

tmnxOspfVirtIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 5)
)
tmnxOspfVirtIfConfigError.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfConfigErrorType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfRxPackets"))
)
if mibBuilder.loadTexts:
    tmnxOspfVirtIfConfigError.setStatus(
        "current"
    )

tmnxOspfIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 6)
)
tmnxOspfIfAuthFailure.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfConfigErrorType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAuthFailures"))
)
if mibBuilder.loadTexts:
    tmnxOspfIfAuthFailure.setStatus(
        "obsolete"
    )

tmnxOspfVirtIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 7)
)
tmnxOspfVirtIfAuthFailure.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfConfigErrorType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfAuthFailures"))
)
if mibBuilder.loadTexts:
    tmnxOspfVirtIfAuthFailure.setStatus(
        "current"
    )

tmnxOspfIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 8)
)
tmnxOspfIfRxBadPacket.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfBadPacketTypes"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfBadPacketErrType"))
)
if mibBuilder.loadTexts:
    tmnxOspfIfRxBadPacket.setStatus(
        "obsolete"
    )

tmnxOspfVirtIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 9)
)
tmnxOspfVirtIfRxBadPacket.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfBadPacketTypes"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfBadPacketErrType"))
)
if mibBuilder.loadTexts:
    tmnxOspfVirtIfRxBadPacket.setStatus(
        "current"
    )

tmnxOspfIfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 10)
)
tmnxOspfIfTxRetransmit.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrLsRetransQLen"))
)
if mibBuilder.loadTexts:
    tmnxOspfIfTxRetransmit.setStatus(
        "obsolete"
    )

tmnxOspfVirtIfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 11)
)
tmnxOspfVirtIfTxRetransmit.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrLsRetransQLen"))
)
if mibBuilder.loadTexts:
    tmnxOspfVirtIfTxRetransmit.setStatus(
        "obsolete"
    )

tmnxOspfAreaOriginateLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 12)
)
tmnxOspfAreaOriginateLsa.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsdbAge"))
)
if mibBuilder.loadTexts:
    tmnxOspfAreaOriginateLsa.setStatus(
        "current"
    )

tmnxOspfAreaMaxAgeLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 13)
)
tmnxOspfAreaMaxAgeLsa.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaLsdbAge"))
)
if mibBuilder.loadTexts:
    tmnxOspfAreaMaxAgeLsa.setStatus(
        "current"
    )

tmnxOspfLsdbOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 14)
)
tmnxOspfLsdbOverflow.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    tmnxOspfLsdbOverflow.setStatus(
        "current"
    )

tmnxOspfLsdbApproachingOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 15)
)
tmnxOspfLsdbApproachingOverflow.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExtLsdbLimit"))
)
if mibBuilder.loadTexts:
    tmnxOspfLsdbApproachingOverflow.setStatus(
        "current"
    )

tmnxOspfIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 16)
)
tmnxOspfIfStateChange.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfIpName"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfEvent"))
)
if mibBuilder.loadTexts:
    tmnxOspfIfStateChange.setStatus(
        "obsolete"
    )

tmnxOspfNssaTranslatorStatusChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 17)
)
tmnxOspfNssaTranslatorStatusChg.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaNssaTranslatorState"))
)
if mibBuilder.loadTexts:
    tmnxOspfNssaTranslatorStatusChg.setStatus(
        "current"
    )

tmnxOspfRestartStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 18)
)
tmnxOspfRestartStatusChange.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRestartStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRestartInterval"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRestartExitRc"))
)
if mibBuilder.loadTexts:
    tmnxOspfRestartStatusChange.setStatus(
        "current"
    )

tmnxOspfNbrRestartHlprStsChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 19)
)
tmnxOspfNbrRestartHlprStsChg.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrRestartHelperStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrRestartHelperAge"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrRestartHelperExitRc"))
)
if mibBuilder.loadTexts:
    tmnxOspfNbrRestartHlprStsChg.setStatus(
        "obsolete"
    )

tmnxOspfVirtNbrRestartHlprStsChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 20)
)
tmnxOspfVirtNbrRestartHlprStsChg.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrRestartHelperStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrRestartHelperAge"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrRestartHelperExitRc"))
)
if mibBuilder.loadTexts:
    tmnxOspfVirtNbrRestartHlprStsChg.setStatus(
        "current"
    )

tmnxOspfSpfRunsStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 21)
)
tmnxOspfSpfRunsStopped.setObjects(
    ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId")
)
if mibBuilder.loadTexts:
    tmnxOspfSpfRunsStopped.setStatus(
        "current"
    )

tmnxOspfSpfRunsRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 22)
)
tmnxOspfSpfRunsRestarted.setObjects(
    ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId")
)
if mibBuilder.loadTexts:
    tmnxOspfSpfRunsRestarted.setStatus(
        "current"
    )

tmnxOspfOverloadEntered = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 23)
)
tmnxOspfOverloadEntered.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastOverloadEnterCode"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxOspfOverloadEntered.setStatus(
        "current"
    )

tmnxOspfOverloadExited = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 24)
)
tmnxOspfOverloadExited.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastOverloadExitCode"))
)
if mibBuilder.loadTexts:
    tmnxOspfOverloadExited.setStatus(
        "current"
    )

tmnxOspfAsOriginateLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 25)
)
tmnxOspfAsOriginateLsa.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsLsdbAge"))
)
if mibBuilder.loadTexts:
    tmnxOspfAsOriginateLsa.setStatus(
        "current"
    )

tmnxOspfAsMaxAgeLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 26)
)
tmnxOspfAsMaxAgeLsa.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsLsdbAge"))
)
if mibBuilder.loadTexts:
    tmnxOspfAsMaxAgeLsa.setStatus(
        "current"
    )

tmnxOspfLinkOriginateLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 27)
)
tmnxOspfLinkOriginateLsa.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkLsdbAge"))
)
if mibBuilder.loadTexts:
    tmnxOspfLinkOriginateLsa.setStatus(
        "obsolete"
    )

tmnxOspfLinkMaxAgeLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 28)
)
tmnxOspfLinkMaxAgeLsa.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkLsdbAge"))
)
if mibBuilder.loadTexts:
    tmnxOspfLinkMaxAgeLsa.setStatus(
        "obsolete"
    )

tmnxOspfLdpSyncTimerStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 29)
)
tmnxOspfLdpSyncTimerStarted.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLdpSyncTimerState"))
)
if mibBuilder.loadTexts:
    tmnxOspfLdpSyncTimerStarted.setStatus(
        "obsolete"
    )

tmnxOspfLdpSyncExit = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 30)
)
tmnxOspfLdpSyncExit.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfLdpSyncTimerState"))
)
if mibBuilder.loadTexts:
    tmnxOspfLdpSyncExit.setStatus(
        "obsolete"
    )

tmnxOspfShamIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 31)
)
tmnxOspfShamIfStateChange.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfState"))
)
if mibBuilder.loadTexts:
    tmnxOspfShamIfStateChange.setStatus(
        "current"
    )

tmnxOspfShamNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 32)
)
tmnxOspfShamNbrStateChange.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrState"))
)
if mibBuilder.loadTexts:
    tmnxOspfShamNbrStateChange.setStatus(
        "current"
    )

tmnxOspfShamIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 33)
)
tmnxOspfShamIfConfigError.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfConfigErrorType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRxPackets"))
)
if mibBuilder.loadTexts:
    tmnxOspfShamIfConfigError.setStatus(
        "current"
    )

tmnxOspfShamIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 34)
)
tmnxOspfShamIfAuthFailure.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfConfigErrorType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfAuthFailures"))
)
if mibBuilder.loadTexts:
    tmnxOspfShamIfAuthFailure.setStatus(
        "current"
    )

tmnxOspfShamIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 35)
)
tmnxOspfShamIfRxBadPacket.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfBadPacketTypes"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfBadPacketErrType"))
)
if mibBuilder.loadTexts:
    tmnxOspfShamIfRxBadPacket.setStatus(
        "current"
    )

tmnxOspfShamIfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 36)
)
tmnxOspfShamIfTxRetransmit.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrLsRetransQLen"))
)
if mibBuilder.loadTexts:
    tmnxOspfShamIfTxRetransmit.setStatus(
        "obsolete"
    )

tmnxOspfShamNbrRestartHlprStsChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 37)
)
tmnxOspfShamNbrRestartHlprStsChg.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrRestartHelperStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrRestartHelperAge"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrRestartHelperExitRc"))
)
if mibBuilder.loadTexts:
    tmnxOspfShamNbrRestartHlprStsChg.setStatus(
        "current"
    )

tmnxOspfFailureDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 38)
)
tmnxOspfFailureDisabled.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFailureReasonCode"))
)
if mibBuilder.loadTexts:
    tmnxOspfFailureDisabled.setStatus(
        "current"
    )

tmnxOspfExportLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 39)
)
tmnxOspfExportLimitReached.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExportLimit"))
)
if mibBuilder.loadTexts:
    tmnxOspfExportLimitReached.setStatus(
        "current"
    )

tmnxOspfExportLimitWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 40)
)
tmnxOspfExportLimitWarning.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExportLimit"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExportLimitLogPercent"))
)
if mibBuilder.loadTexts:
    tmnxOspfExportLimitWarning.setStatus(
        "current"
    )

tmnxOspfRoutesExpLmtDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 41)
)
tmnxOspfRoutesExpLmtDropped.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExportLimit"))
)
if mibBuilder.loadTexts:
    tmnxOspfRoutesExpLmtDropped.setStatus(
        "current"
    )

tmnxOspfNgNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 42)
)
tmnxOspfNgNbrStateChange.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrState"))
)
if mibBuilder.loadTexts:
    tmnxOspfNgNbrStateChange.setStatus(
        "current"
    )

tmnxOspfNgIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 43)
)
tmnxOspfNgIfConfigError.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfConfigErrorType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfRxPackets"))
)
if mibBuilder.loadTexts:
    tmnxOspfNgIfConfigError.setStatus(
        "current"
    )

tmnxOspfNgIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 44)
)
tmnxOspfNgIfAuthFailure.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfConfigErrorType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfAuthFailures"))
)
if mibBuilder.loadTexts:
    tmnxOspfNgIfAuthFailure.setStatus(
        "current"
    )

tmnxOspfNgIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 45)
)
tmnxOspfNgIfRxBadPacket.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddressType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketSrcAddress"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfBadPacketTypes"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfBadPacketErrType"))
)
if mibBuilder.loadTexts:
    tmnxOspfNgIfRxBadPacket.setStatus(
        "current"
    )

tmnxOspfNgIfTxRetransmit = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 46)
)
tmnxOspfNgIfTxRetransmit.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfPacketType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrLsRetransQLen"))
)
if mibBuilder.loadTexts:
    tmnxOspfNgIfTxRetransmit.setStatus(
        "obsolete"
    )

tmnxOspfNgIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 47)
)
tmnxOspfNgIfStateChange.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfState"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfIpName"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfEvent"))
)
if mibBuilder.loadTexts:
    tmnxOspfNgIfStateChange.setStatus(
        "current"
    )

tmnxOspfNgNbrRestartHlprStsChg = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 48)
)
tmnxOspfNgNbrRestartHlprStsChg.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrRestartHelperStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrRestartHelperAge"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrRestartHelperExitRc"))
)
if mibBuilder.loadTexts:
    tmnxOspfNgNbrRestartHlprStsChg.setStatus(
        "current"
    )

tmnxOspfNgLinkOriginateLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 49)
)
tmnxOspfNgLinkOriginateLsa.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbAge"))
)
if mibBuilder.loadTexts:
    tmnxOspfNgLinkOriginateLsa.setStatus(
        "current"
    )

tmnxOspfNgLinkMaxAgeLsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 50)
)
tmnxOspfNgLinkMaxAgeLsa.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbAge"))
)
if mibBuilder.loadTexts:
    tmnxOspfNgLinkMaxAgeLsa.setStatus(
        "current"
    )

tmnxOspfNgLdpSyncTimerStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 51)
)
tmnxOspfNgLdpSyncTimerStarted.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfLdpSyncTimerState"))
)
if mibBuilder.loadTexts:
    tmnxOspfNgLdpSyncTimerStarted.setStatus(
        "current"
    )

tmnxOspfNgLdpSyncExit = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 52)
)
tmnxOspfNgLdpSyncExit.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfLdpSyncTimerState"))
)
if mibBuilder.loadTexts:
    tmnxOspfNgLdpSyncExit.setStatus(
        "current"
    )

tmnxOspfSrSidError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 53)
)
tmnxOspfSrSidError.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrPfxSidFlags"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxOspfSrSidError.setStatus(
        "current"
    )

tmnxOspfSrSidNotInLabelRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 54)
)
tmnxOspfSrSidNotInLabelRange.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrPfxSidFlags"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifPfxSidRangeStartLbl"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifPfxSidRangeMaxIdx"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifPfxNhAdvRtr"))
)
if mibBuilder.loadTexts:
    tmnxOspfSrSidNotInLabelRange.setStatus(
        "current"
    )

tmnxOspfOverloadWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 55)
)
tmnxOspfOverloadWarning.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLastOverloadEnterCode"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxOspfOverloadWarning.setStatus(
        "current"
    )

tmnxOspfRejectedAdjacencySid = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 56)
)
tmnxOspfRejectedAdjacencySid.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxOspfRejectedAdjacencySid.setStatus(
        "current"
    )

tmnxOspfAdjBfdSessionSetupFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 57)
)
tmnxOspfAdjBfdSessionSetupFail.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfBfdSessSetupFailReason"))
)
if mibBuilder.loadTexts:
    tmnxOspfAdjBfdSessionSetupFail.setStatus(
        "current"
    )

tmnxOspfSrgbBadLabelRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 58)
)
tmnxOspfSrgbBadLabelRange.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifSrgbRangeStartLbl"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifSrgbRangeMaxIdx"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifSrgbAdvRtrID"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifSrgbAreaId"))
)
if mibBuilder.loadTexts:
    tmnxOspfSrgbBadLabelRange.setStatus(
        "current"
    )

tmnxOspfRejectedAdjacencySet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 59)
)
tmnxOspfRejectedAdjacencySet.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjSetRowStatus"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyIfIndex"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyNbrRouterId"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxOspfRejectedAdjacencySet.setStatus(
        "current"
    )

tmnxOspfSidStatsIndexAlloc = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 60)
)
tmnxOspfSidStatsIndexAlloc.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfSidStatsSidType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSidStatsPrefixType"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSidStatsPrefix"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSidStatsPrefixLength"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSidStatsIfIndex"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSidStatsAdjSet"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifStatsIndexStatus"))
)
if mibBuilder.loadTexts:
    tmnxOspfSidStatsIndexAlloc.setStatus(
        "current"
    )

tmnxOspfDynHostnameDuplicate = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 61)
)
tmnxOspfDynHostnameDuplicate.setObjects(
    ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostnameName")
)
if mibBuilder.loadTexts:
    tmnxOspfDynHostnameDuplicate.setStatus(
        "current"
    )

tmnxOspfDynHostnameInconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 36, 0, 62)
)
tmnxOspfDynHostnameInconsistent.setObjects(
    ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostnameName")
)
if mibBuilder.loadTexts:
    tmnxOspfDynHostnameInconsistent.setStatus(
        "current"
    )


# Notifications groups

tmnxOspfNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 11)
)
tmnxOspfNotificationGroup.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfStateChange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrStateChange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrStateChange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfConfigError"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfConfigError"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfAuthFailure"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfAuthFailure"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfRxBadPacket"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfRxBadPacket"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfTxRetransmit"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfTxRetransmit"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaOriginateLsa"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaMaxAgeLsa"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLsdbOverflow"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLsdbApproachingOverflow"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfStateChange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNssaTranslatorStatusChg"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRestartStatusChange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrRestartHlprStsChg"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrRestartHlprStsChg"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSpfRunsStopped"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSpfRunsRestarted"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOverloadEntered"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOverloadExited"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsOriginateLsa"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsMaxAgeLsa"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkOriginateLsa"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLinkMaxAgeLsa"))
)
if mibBuilder.loadTexts:
    tmnxOspfNotificationGroup.setStatus(
        "obsolete"
    )

tmnxOspfNotificationV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 16)
)
tmnxOspfNotificationV6v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfLdpSyncTimerStarted"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLdpSyncExit"))
)
if mibBuilder.loadTexts:
    tmnxOspfNotificationV6v0Group.setStatus(
        "obsolete"
    )

tmnxOspfNotificationV7v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 20)
)
tmnxOspfNotificationV7v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfStateChange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrStateChange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfConfigError"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfAuthFailure"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRxBadPacket"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfTxRetransmit"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrRestartHlprStsChg"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFailureDisabled"))
)
if mibBuilder.loadTexts:
    tmnxOspfNotificationV7v0Group.setStatus(
        "obsolete"
    )

tmnxOspfGenNotificationV7v0Grp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 23)
)
tmnxOspfGenNotificationV7v0Grp.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfExportLimitReached"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfExportLimitWarning"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRoutesExpLmtDropped"))
)
if mibBuilder.loadTexts:
    tmnxOspfGenNotificationV7v0Grp.setStatus(
        "current"
    )

tmnxOspfNotificationV9v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 36)
)
tmnxOspfNotificationV9v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfStateChange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrStateChange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrStateChange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfConfigError"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfConfigError"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfAuthFailure"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfAuthFailure"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfRxBadPacket"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfRxBadPacket"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfTxRetransmit"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfTxRetransmit"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaOriginateLsa"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaMaxAgeLsa"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLsdbOverflow"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLsdbApproachingOverflow"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfStateChange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNssaTranslatorStatusChg"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRestartStatusChange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrRestartHlprStsChg"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrRestartHlprStsChg"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSpfRunsStopped"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSpfRunsRestarted"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOverloadEntered"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOverloadExited"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsOriginateLsa"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsMaxAgeLsa"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkOriginateLsa"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkMaxAgeLsa"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLdpSyncTimerStarted"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLdpSyncExit"))
)
if mibBuilder.loadTexts:
    tmnxOspfNotificationV9v0Group.setStatus(
        "obsolete"
    )

tmnxOspfNotificationV13v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 45)
)
tmnxOspfNotificationV13v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrSidError"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrSidNotInLabelRange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOverloadWarning"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRejectedAdjacencySid"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSrgbBadLabelRange"))
)
if mibBuilder.loadTexts:
    tmnxOspfNotificationV13v0Group.setStatus(
        "current"
    )

tmnxOspfNotificationV12v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 50)
)
tmnxOspfNotificationV12v0Group.setObjects(
    ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAdjBfdSessionSetupFail")
)
if mibBuilder.loadTexts:
    tmnxOspfNotificationV12v0Group.setStatus(
        "current"
    )

tmnxOspfNotificationV16v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 59)
)
tmnxOspfNotificationV16v0Group.setObjects(
    ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRejectedAdjacencySet")
)
if mibBuilder.loadTexts:
    tmnxOspfNotificationV16v0Group.setStatus(
        "current"
    )

tmnxOspfNotificationV19v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 63)
)
tmnxOspfNotificationV19v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfSidStatsIndexAlloc"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfDynHostnameDuplicate"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfDynHostnameInconsistent"))
)
if mibBuilder.loadTexts:
    tmnxOspfNotificationV19v0Group.setStatus(
        "current"
    )

tmnxOspfNotificationV20v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 66)
)
tmnxOspfNotificationV20v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfStateChange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrStateChange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfConfigError"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfAuthFailure"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfRxBadPacket"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamNbrRestartHlprStsChg"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFailureDisabled"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfStateChange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrStateChange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrStateChange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfConfigError"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfConfigError"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfAuthFailure"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfAuthFailure"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfRxBadPacket"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfRxBadPacket"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaOriginateLsa"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaMaxAgeLsa"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLsdbOverflow"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfLsdbApproachingOverflow"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfStateChange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNssaTranslatorStatusChg"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfRestartStatusChange"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrRestartHlprStsChg"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrRestartHlprStsChg"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSpfRunsStopped"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSpfRunsRestarted"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOverloadEntered"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfOverloadExited"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsOriginateLsa"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAsMaxAgeLsa"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkOriginateLsa"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkMaxAgeLsa"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLdpSyncTimerStarted"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLdpSyncExit"))
)
if mibBuilder.loadTexts:
    tmnxOspfNotificationV20v0Group.setStatus(
        "current"
    )

tmnxOspfObsoletedNotifV20v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 2, 67)
)
tmnxOspfObsoletedNotifV20v0Group.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfTxRetransmit"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamIfTxRetransmit"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfTxRetransmit"))
)
if mibBuilder.loadTexts:
    tmnxOspfObsoletedNotifV20v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxOspfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 1, 1)
)
tmnxOspfCompliance.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMD5KeyGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxOspfCompliance.setStatus(
        "obsolete"
    )

tmnxOspfV5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 1, 2)
)
tmnxOspfV5v0Compliance.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV5v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfV5v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMD5KeyGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxOspfV5v0Compliance.setStatus(
        "obsolete"
    )

tmnxOspfV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 1, 3)
)
tmnxOspfV6v0Compliance.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV5v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfV5v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMD5KeyGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOspfV6v0Compliance.setStatus(
        "obsolete"
    )

tmnxOspfV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 1, 4)
)
tmnxOspfV6v1Compliance.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV5v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfV5v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMD5KeyGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v1Group"))
)
if mibBuilder.loadTexts:
    tmnxOspfV6v1Compliance.setStatus(
        "obsolete"
    )

tmnxOspfV7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 1, 5)
)
tmnxOspfV7v0Compliance.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV5v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfV5v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMD5KeyGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v1Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamLinksV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGenNotificationV7v0Grp"))
)
if mibBuilder.loadTexts:
    tmnxOspfV7v0Compliance.setStatus(
        "obsolete"
    )

tmnxOspfV8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 1, 6)
)
tmnxOspfV8v0Compliance.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV5v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfV5v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMD5KeyGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v1Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamLinksV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGenNotificationV7v0Grp"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV8v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOspfV8v0Compliance.setStatus(
        "obsolete"
    )

tmnxOspfV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 1, 7)
)
tmnxOspfV9v0Compliance.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV5v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfOperV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfStatsV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMD5KeyV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v1Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamLinksV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGenNotificationV7v0Grp"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV8v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOspfV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxOspfV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 1, 8)
)
tmnxOspfV10v0Compliance.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV5v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfOperV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfStatsV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMD5KeyV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v1Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamLinksV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGenNotificationV7v0Grp"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV10v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFRRV10v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOspfV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxOspfV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 1, 9)
)
tmnxOspfV11v0Compliance.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV5v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfOperV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfStatsV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMD5KeyV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v1Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamLinksV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGenNotificationV7v0Grp"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV10v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFRRV10v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFRRV11v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV11v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOspfV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxOspfV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 1, 10)
)
tmnxOspfV12v0Compliance.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV5v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfOperV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfStatsV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMD5KeyV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v1Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamLinksV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGenNotificationV7v0Grp"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV10v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFRRV10v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFRRV11v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV11v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV12v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOspfV12v0Compliance.setStatus(
        "obsolete"
    )

tmnxOspfV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 1, 11)
)
tmnxOspfV13v0Compliance.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV5v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfOperV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfStatsV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMD5KeyV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v1Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamLinksV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGenNotificationV7v0Grp"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV10v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFRRV10v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFRRV11v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV11v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV12v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOspfV13v0Compliance.setStatus(
        "obsolete"
    )

tmnxOspfV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 1, 12)
)
tmnxOspfV14v0Compliance.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV5v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfOperV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfStatsV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMD5KeyV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v1Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamLinksV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGenNotificationV7v0Grp"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV10v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFRRV10v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFRRV11v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV11v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV12v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSegmentRoutingTEGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV12v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV14v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOspfV14v0Compliance.setStatus(
        "obsolete"
    )

tmnxOspfV15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 1, 13)
)
tmnxOspfV15v0Compliance.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV5v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfOperV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfStatsV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMD5KeyV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v1Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamLinksV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGenNotificationV7v0Grp"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV10v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFRRV10v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFRRV11v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV11v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV12v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSegmentRoutingTEGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV12v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV14v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV15v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIgpSC15v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfObsolete15v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOspfV15v0Compliance.setStatus(
        "obsolete"
    )

tmnxOspfV16v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 1, 14)
)
tmnxOspfV16v0Compliance.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV5v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfOperV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfStatsV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMD5KeyV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v1Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamLinksV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGenNotificationV7v0Grp"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV10v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFRRV10v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFRRV11v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV11v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV12v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSegmentRoutingTEGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV12v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV14v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV15v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIgpSC15v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfObsolete16v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV16v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsV16v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV16v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNetworkElementV16v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOspfV16v0Compliance.setStatus(
        "obsolete"
    )

tmnxOspfV19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 1, 15)
)
tmnxOspfV19v0Compliance.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV5v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfOperV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfStatsV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMD5KeyV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v1Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamLinksV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGenNotificationV7v0Grp"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV10v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFRRV10v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFRRV11v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV11v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV12v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSegmentRoutingTEGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV12v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV14v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV15v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIgpSC15v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfObsolete16v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV16v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsV16v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV16v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV19v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfObsolete19v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV19v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOspfV19v0Compliance.setStatus(
        "obsolete"
    )

tmnxOspfV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 36, 1, 16)
)
tmnxOspfV20v0Compliance.setObjects(
      *(("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV5v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgLinkLsdbV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfHostGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfOperV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgIfStatsV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNgNbrV9v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtNbrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfAreaAggrGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfMD5KeyV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV6v1Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfShamLinksV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV7v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGenNotificationV7v0Grp"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfVirtIfV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV8v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV10v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFRRV10v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfFRRV11v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV11v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV12v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfSegmentRoutingTEGroup"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV13v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV12v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV14v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV15v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfIgpSC15v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfObsolete16v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV16v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotifyObjsV16v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV16v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV19v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfObsolete19v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV19v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfGeneralV20v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfNotificationV20v0Group"),
        ("TIMETRA-OSPF-NG-MIB", "tmnxOspfObsoletedNotifV20v0Group"))
)
if mibBuilder.loadTexts:
    tmnxOspfV20v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-OSPF-NG-MIB",
    **{"TmnxOspfUpToRefreshIntervalTc": TmnxOspfUpToRefreshIntervalTc,
       "TmnxOspfDeadIntRangeTc": TmnxOspfDeadIntRangeTc,
       "TmnxOspfRouterIdTc": TmnxOspfRouterIdTc,
       "TmnxOspfAreaIdTc": TmnxOspfAreaIdTc,
       "TmnxOspfIfInstIdTc": TmnxOspfIfInstIdTc,
       "TmnxOspfPreference": TmnxOspfPreference,
       "TmnxOspfAuthenticationType": TmnxOspfAuthenticationType,
       "TmnxOspfIfMD5KeyId": TmnxOspfIfMD5KeyId,
       "TmnxOspfRestartReasonTc": TmnxOspfRestartReasonTc,
       "TmnxOspfIfTypeTc": TmnxOspfIfTypeTc,
       "TmnxOspfShamIfMetricTc": TmnxOspfShamIfMetricTc,
       "TmnxOspfLsaFilterOutTc": TmnxOspfLsaFilterOutTc,
       "TmnxSegmentRoutingId": TmnxSegmentRoutingId,
       "TmnxOspfSegmentRoutingRouteType": TmnxOspfSegmentRoutingRouteType,
       "timetraOspfNgMIBModule": timetraOspfNgMIBModule,
       "tmnxOspfConformance": tmnxOspfConformance,
       "tmnxOspfCompliances": tmnxOspfCompliances,
       "tmnxOspfCompliance": tmnxOspfCompliance,
       "tmnxOspfV5v0Compliance": tmnxOspfV5v0Compliance,
       "tmnxOspfV6v0Compliance": tmnxOspfV6v0Compliance,
       "tmnxOspfV6v1Compliance": tmnxOspfV6v1Compliance,
       "tmnxOspfV7v0Compliance": tmnxOspfV7v0Compliance,
       "tmnxOspfV8v0Compliance": tmnxOspfV8v0Compliance,
       "tmnxOspfV9v0Compliance": tmnxOspfV9v0Compliance,
       "tmnxOspfV10v0Compliance": tmnxOspfV10v0Compliance,
       "tmnxOspfV11v0Compliance": tmnxOspfV11v0Compliance,
       "tmnxOspfV12v0Compliance": tmnxOspfV12v0Compliance,
       "tmnxOspfV13v0Compliance": tmnxOspfV13v0Compliance,
       "tmnxOspfV14v0Compliance": tmnxOspfV14v0Compliance,
       "tmnxOspfV15v0Compliance": tmnxOspfV15v0Compliance,
       "tmnxOspfV16v0Compliance": tmnxOspfV16v0Compliance,
       "tmnxOspfV19v0Compliance": tmnxOspfV19v0Compliance,
       "tmnxOspfV20v0Compliance": tmnxOspfV20v0Compliance,
       "tmnxOspfGroups": tmnxOspfGroups,
       "tmnxOspfGeneralGroup": tmnxOspfGeneralGroup,
       "tmnxOspfAreaGroup": tmnxOspfAreaGroup,
       "tmnxOspfHostGroup": tmnxOspfHostGroup,
       "tmnxOspfIfGroup": tmnxOspfIfGroup,
       "tmnxOspfVirtIfGroup": tmnxOspfVirtIfGroup,
       "tmnxOspfNbrGroup": tmnxOspfNbrGroup,
       "tmnxOspfVirtNbrGroup": tmnxOspfVirtNbrGroup,
       "tmnxOspfAreaAggrGroup": tmnxOspfAreaAggrGroup,
       "tmnxOspfMD5KeyGroup": tmnxOspfMD5KeyGroup,
       "tmnxOspfNotifyObjsGroup": tmnxOspfNotifyObjsGroup,
       "tmnxOspfNotificationGroup": tmnxOspfNotificationGroup,
       "tmnxOspfGeneralV5v0Group": tmnxOspfGeneralV5v0Group,
       "tmnxOspfIfV5v0Group": tmnxOspfIfV5v0Group,
       "tmnxOspfIfV6v0Group": tmnxOspfIfV6v0Group,
       "tmnxOspfGeneralV6v0Group": tmnxOspfGeneralV6v0Group,
       "tmnxOspfNotificationV6v0Group": tmnxOspfNotificationV6v0Group,
       "tmnxOspfNotifyObjsV6v0Group": tmnxOspfNotifyObjsV6v0Group,
       "tmnxOspfGeneralV6v1Group": tmnxOspfGeneralV6v1Group,
       "tmnxOspfShamLinksV7v0Group": tmnxOspfShamLinksV7v0Group,
       "tmnxOspfNotificationV7v0Group": tmnxOspfNotificationV7v0Group,
       "tmnxOspfNotifyObjsV7v0Group": tmnxOspfNotifyObjsV7v0Group,
       "tmnxOspfGeneralV7v0Group": tmnxOspfGeneralV7v0Group,
       "tmnxOspfGenNotificationV7v0Grp": tmnxOspfGenNotificationV7v0Grp,
       "tmnxOspfAreaV8v0Group": tmnxOspfAreaV8v0Group,
       "tmnxOspfVirtIfV8v0Group": tmnxOspfVirtIfV8v0Group,
       "tmnxOspfIfV8v0Group": tmnxOspfIfV8v0Group,
       "tmnxOspfNotifyObjsV8v0Group": tmnxOspfNotifyObjsV8v0Group,
       "tmnxOspfGeneralV8v0Group": tmnxOspfGeneralV8v0Group,
       "tmnxOspfAreaV9v0Group": tmnxOspfAreaV9v0Group,
       "tmnxOspfNgLinkLsdbV9v0Group": tmnxOspfNgLinkLsdbV9v0Group,
       "tmnxOspfNgNbrV9v0Group": tmnxOspfNgNbrV9v0Group,
       "tmnxOspfNgIfV9v0Group": tmnxOspfNgIfV9v0Group,
       "tmnxOspfNgIfOperV9v0Group": tmnxOspfNgIfOperV9v0Group,
       "tmnxOspfNgIfStatsV9v0Group": tmnxOspfNgIfStatsV9v0Group,
       "tmnxOspfMD5KeyV9v0Group": tmnxOspfMD5KeyV9v0Group,
       "tmnxOspfNotificationV9v0Group": tmnxOspfNotificationV9v0Group,
       "tmnxOspfObsoletedObjV9v0Group": tmnxOspfObsoletedObjV9v0Group,
       "tmnxOspfGeneralV10v0Group": tmnxOspfGeneralV10v0Group,
       "tmnxOspfFRRV10v0Group": tmnxOspfFRRV10v0Group,
       "tmnxOspfFRRV11v0Group": tmnxOspfFRRV11v0Group,
       "tmnxOspfGeneralV11v0Group": tmnxOspfGeneralV11v0Group,
       "tmnxOspfGeneralV12v0Group": tmnxOspfGeneralV12v0Group,
       "tmnxOspfGeneralV13v0Group": tmnxOspfGeneralV13v0Group,
       "tmnxOspfNotifyObjsV13v0Group": tmnxOspfNotifyObjsV13v0Group,
       "tmnxOspfNotificationV13v0Group": tmnxOspfNotificationV13v0Group,
       "tmnxOspfMD5KeyV13v0Group": tmnxOspfMD5KeyV13v0Group,
       "tmnxOspfShamLinksV13v0Group": tmnxOspfShamLinksV13v0Group,
       "tmnxOspfObsoletedObjV13v0Group": tmnxOspfObsoletedObjV13v0Group,
       "tmnxOspfNotifyObjsV12v0Group": tmnxOspfNotifyObjsV12v0Group,
       "tmnxOspfNotificationV12v0Group": tmnxOspfNotificationV12v0Group,
       "tmnxOspfSegmentRoutingTEGroup": tmnxOspfSegmentRoutingTEGroup,
       "tmnxOspfGeneralV14v0Group": tmnxOspfGeneralV14v0Group,
       "tmnxOspfGeneralV15v0Group": tmnxOspfGeneralV15v0Group,
       "tmnxOspfIgpSC15v0Group": tmnxOspfIgpSC15v0Group,
       "tmnxOspfObsolete15v0Group": tmnxOspfObsolete15v0Group,
       "tmnxOspfObsolete16v0Group": tmnxOspfObsolete16v0Group,
       "tmnxOspfGeneralV16v0Group": tmnxOspfGeneralV16v0Group,
       "tmnxOspfNotifyObjsV16v0Group": tmnxOspfNotifyObjsV16v0Group,
       "tmnxOspfNotificationV16v0Group": tmnxOspfNotificationV16v0Group,
       "tmnxOspfGeneralV19v0Group": tmnxOspfGeneralV19v0Group,
       "tmnxOspfObsolete19v0Group": tmnxOspfObsolete19v0Group,
       "tmnxOspfNotifyObjsV19v0Group": tmnxOspfNotifyObjsV19v0Group,
       "tmnxOspfNotificationV19v0Group": tmnxOspfNotificationV19v0Group,
       "tmnxOspfNetworkElementV16v0Group": tmnxOspfNetworkElementV16v0Group,
       "tmnxOspfGeneralV20v0Group": tmnxOspfGeneralV20v0Group,
       "tmnxOspfNotificationV20v0Group": tmnxOspfNotificationV20v0Group,
       "tmnxOspfObsoletedNotifV20v0Group": tmnxOspfObsoletedNotifV20v0Group,
       "tmnxOspfObjects": tmnxOspfObjects,
       "tmnxOspfScalars": tmnxOspfScalars,
       "tmnxOspfGeneralEntries": tmnxOspfGeneralEntries,
       "tmnxOspfGeneralTable": tmnxOspfGeneralTable,
       "tmnxOspfGeneralEntry": tmnxOspfGeneralEntry,
       "tmnxOspfVersion": tmnxOspfVersion,
       "tmnxOspfInstance": tmnxOspfInstance,
       "tmnxOspfGeneralLastChanged": tmnxOspfGeneralLastChanged,
       "tmnxOspfRouterId": tmnxOspfRouterId,
       "tmnxOspfAdminState": tmnxOspfAdminState,
       "tmnxOspfASBdrRtrStatus": tmnxOspfASBdrRtrStatus,
       "tmnxOspfRFC1583Compatibility": tmnxOspfRFC1583Compatibility,
       "tmnxOspfExtLsdbLimit": tmnxOspfExtLsdbLimit,
       "tmnxOspfMulticastExtensions": tmnxOspfMulticastExtensions,
       "tmnxOspfExitOverflowInterval": tmnxOspfExitOverflowInterval,
       "tmnxOspfDemandExtensions": tmnxOspfDemandExtensions,
       "tmnxOspfReferenceBandwidth": tmnxOspfReferenceBandwidth,
       "tmnxOspfStrictLsaChecking": tmnxOspfStrictLsaChecking,
       "tmnxOspfRestartSupport": tmnxOspfRestartSupport,
       "tmnxOspfRestartInterval": tmnxOspfRestartInterval,
       "tmnxOspfPreference": tmnxOspfPreference,
       "tmnxOspfExternalPreference": tmnxOspfExternalPreference,
       "tmnxOspfExportPolicy1": tmnxOspfExportPolicy1,
       "tmnxOspfExportPolicy2": tmnxOspfExportPolicy2,
       "tmnxOspfExportPolicy3": tmnxOspfExportPolicy3,
       "tmnxOspfExportPolicy4": tmnxOspfExportPolicy4,
       "tmnxOspfExportPolicy5": tmnxOspfExportPolicy5,
       "tmnxOspfManualSpfTrigger": tmnxOspfManualSpfTrigger,
       "tmnxOspfOverloadAdmState": tmnxOspfOverloadAdmState,
       "tmnxOspfOverloadInterval": tmnxOspfOverloadInterval,
       "tmnxOspfBootOverloadAdmState": tmnxOspfBootOverloadAdmState,
       "tmnxOspfBootOverloadInterval": tmnxOspfBootOverloadInterval,
       "tmnxOspfOverloadStubs": tmnxOspfOverloadStubs,
       "tmnxOspfSpfMaxWait": tmnxOspfSpfMaxWait,
       "tmnxOspfSpfInitialWait": tmnxOspfSpfInitialWait,
       "tmnxOspfSpfSecondWait": tmnxOspfSpfSecondWait,
       "tmnxOspfLsaGenMaxWait": tmnxOspfLsaGenMaxWait,
       "tmnxOspfLsaGenInitialWait": tmnxOspfLsaGenInitialWait,
       "tmnxOspfLsaGenSecondWait": tmnxOspfLsaGenSecondWait,
       "tmnxOspfLsaArrivalWait": tmnxOspfLsaArrivalWait,
       "tmnxOspfTESupport": tmnxOspfTESupport,
       "tmnxOspfUnicastImport": tmnxOspfUnicastImport,
       "tmnxOspfMulticastImport": tmnxOspfMulticastImport,
       "tmnxOspfGREnable": tmnxOspfGREnable,
       "tmnxOspfGRHelperMode": tmnxOspfGRHelperMode,
       "tmnxOspfRowStatus": tmnxOspfRowStatus,
       "tmnxOspfAsbrDomainId": tmnxOspfAsbrDomainId,
       "tmnxOspfIgnoreDNBit": tmnxOspfIgnoreDNBit,
       "tmnxOspfSuppressDNBit": tmnxOspfSuppressDNBit,
       "tmnxOspfLdpSyncAdminState": tmnxOspfLdpSyncAdminState,
       "tmnxOspfVpnDomainType": tmnxOspfVpnDomainType,
       "tmnxOspfVpnDomainId": tmnxOspfVpnDomainId,
       "tmnxOspfVpnTag": tmnxOspfVpnTag,
       "tmnxOspfSuperBackBone": tmnxOspfSuperBackBone,
       "tmnxOspfLdpOverRsvp": tmnxOspfLdpOverRsvp,
       "tmnxOspfExportLimit": tmnxOspfExportLimit,
       "tmnxOspfExportLimitLogPercent": tmnxOspfExportLimitLogPercent,
       "tmnxOspfRsvpShortcut": tmnxOspfRsvpShortcut,
       "tmnxOspfAdvertiseTunnelLink": tmnxOspfAdvertiseTunnelLink,
       "tmnxOspfImportPolicy1": tmnxOspfImportPolicy1,
       "tmnxOspfImportPolicy2": tmnxOspfImportPolicy2,
       "tmnxOspfImportPolicy3": tmnxOspfImportPolicy3,
       "tmnxOspfImportPolicy4": tmnxOspfImportPolicy4,
       "tmnxOspfImportPolicy5": tmnxOspfImportPolicy5,
       "tmnxOspfLoopfreeAlternate": tmnxOspfLoopfreeAlternate,
       "tmnxOspfLsaAccumulate": tmnxOspfLsaAccumulate,
       "tmnxOspfRedistDelay": tmnxOspfRedistDelay,
       "tmnxOspfIncrSpfWait": tmnxOspfIncrSpfWait,
       "tmnxOspfOverloadInclExt2": tmnxOspfOverloadInclExt2,
       "tmnxOspfStatusTable": tmnxOspfStatusTable,
       "tmnxOspfStatusEntry": tmnxOspfStatusEntry,
       "tmnxOspfAreaBdrRtrStatus": tmnxOspfAreaBdrRtrStatus,
       "tmnxOspfBackBoneRouter": tmnxOspfBackBoneRouter,
       "tmnxOspfStubRouterSupport": tmnxOspfStubRouterSupport,
       "tmnxOspfAsScopeLsaCount": tmnxOspfAsScopeLsaCount,
       "tmnxOspfAsScopeLsaCksumSum": tmnxOspfAsScopeLsaCksumSum,
       "tmnxOspfAsScopeUnkLsaCount": tmnxOspfAsScopeUnkLsaCount,
       "tmnxOspfAsScopeUnkLsaCksumSum": tmnxOspfAsScopeUnkLsaCksumSum,
       "tmnxOspfExternLsaCount": tmnxOspfExternLsaCount,
       "tmnxOspfExternLsaCksumSum": tmnxOspfExternLsaCksumSum,
       "tmnxOspfOpaqueLsaSupport": tmnxOspfOpaqueLsaSupport,
       "tmnxOspfRestartStatus": tmnxOspfRestartStatus,
       "tmnxOspfRestartAge": tmnxOspfRestartAge,
       "tmnxOspfRestartExitRc": tmnxOspfRestartExitRc,
       "tmnxOspfDiscontinuityTime": tmnxOspfDiscontinuityTime,
       "tmnxOspfLastEnabledTime": tmnxOspfLastEnabledTime,
       "tmnxOspfLastOvrflwEnteredTime": tmnxOspfLastOvrflwEnteredTime,
       "tmnxOspfLastOverflowExitTime": tmnxOspfLastOverflowExitTime,
       "tmnxOspfInOverflowState": tmnxOspfInOverflowState,
       "tmnxOspfOverloadOperState": tmnxOspfOverloadOperState,
       "tmnxOspfOverloadRemInterval": tmnxOspfOverloadRemInterval,
       "tmnxOspfLastOverloadEntrdTime": tmnxOspfLastOverloadEntrdTime,
       "tmnxOspfLastOverloadExitTime": tmnxOspfLastOverloadExitTime,
       "tmnxOspfLastOverloadEnterCode": tmnxOspfLastOverloadEnterCode,
       "tmnxOspfLastOverloadExitCode": tmnxOspfLastOverloadExitCode,
       "tmnxOspfLastExtSpfRunTime": tmnxOspfLastExtSpfRunTime,
       "tmnxOspfLastFullSpfRunTime": tmnxOspfLastFullSpfRunTime,
       "tmnxOspfLastFullSpfInterval": tmnxOspfLastFullSpfInterval,
       "tmnxOspfMaxSpfRunInterval": tmnxOspfMaxSpfRunInterval,
       "tmnxOspfMinSpfRunInterval": tmnxOspfMinSpfRunInterval,
       "tmnxOspfAvgSpfRunInterval": tmnxOspfAvgSpfRunInterval,
       "tmnxOspfExtSpfRunInterval": tmnxOspfExtSpfRunInterval,
       "tmnxOspfRoutesSubmitted": tmnxOspfRoutesSubmitted,
       "tmnxOspfOperRouterId": tmnxOspfOperRouterId,
       "tmnxOspfTotalExportedRoutes": tmnxOspfTotalExportedRoutes,
       "tmnxOspfLastLfaSpfRunTime": tmnxOspfLastLfaSpfRunTime,
       "tmnxOspfLdpOverRsvpStatus": tmnxOspfLdpOverRsvpStatus,
       "tmnxOspfRsvpShortcutStatus": tmnxOspfRsvpShortcutStatus,
       "tmnxOspfAdvertiseTunlLinkStatus": tmnxOspfAdvertiseTunlLinkStatus,
       "tmnxOspfOvldLsaLimitRemInterval": tmnxOspfOvldLsaLimitRemInterval,
       "tmnxOspfDbAsn": tmnxOspfDbAsn,
       "tmnxOspfOperState": tmnxOspfOperState,
       "tmnxOspfStatisticsTable": tmnxOspfStatisticsTable,
       "tmnxOspfStatisticsEntry": tmnxOspfStatisticsEntry,
       "tmnxOspfOriginateNewLsas": tmnxOspfOriginateNewLsas,
       "tmnxOspfRxNewLsas": tmnxOspfRxNewLsas,
       "tmnxOspfFullSpfRuns": tmnxOspfFullSpfRuns,
       "tmnxOspfExtSpfRuns": tmnxOspfExtSpfRuns,
       "tmnxOspfIncremntlInterSpfRuns": tmnxOspfIncremntlInterSpfRuns,
       "tmnxOspfIncrementalExtSpfRuns": tmnxOspfIncrementalExtSpfRuns,
       "tmnxOspfSpfAttemptsFailed": tmnxOspfSpfAttemptsFailed,
       "tmnxOspfNumTimesInOverload": tmnxOspfNumTimesInOverload,
       "tmnxOspfNumTimesInOverflow": tmnxOspfNumTimesInOverflow,
       "tmnxOspfRoutesAddsFailed": tmnxOspfRoutesAddsFailed,
       "tmnxOspfRoutesDelsFailed": tmnxOspfRoutesDelsFailed,
       "tmnxOspfRoutesModsFailed": tmnxOspfRoutesModsFailed,
       "tmnxOspfAreaEntries": tmnxOspfAreaEntries,
       "tmnxOspfAreaLsaCountEntries": tmnxOspfAreaLsaCountEntries,
       "tmnxOspfAsLsdbEntries": tmnxOspfAsLsdbEntries,
       "tmnxOspfAreaLsdbEntries": tmnxOspfAreaLsdbEntries,
       "tmnxOspfLinkLsdbEntries": tmnxOspfLinkLsdbEntries,
       "tmnxOspfHostEntries": tmnxOspfHostEntries,
       "tmnxOspfIfEntries": tmnxOspfIfEntries,
       "tmnxOspfVirtIfEntries": tmnxOspfVirtIfEntries,
       "tmnxOspfNbrEntries": tmnxOspfNbrEntries,
       "tmnxOspfCfgNbrEntries": tmnxOspfCfgNbrEntries,
       "tmnxOspfVirtNbrEntries": tmnxOspfVirtNbrEntries,
       "tmnxOspfAreaAggrEntries": tmnxOspfAreaAggrEntries,
       "tmnxOspfIfMD5KeyEntries": tmnxOspfIfMD5KeyEntries,
       "tmnxOspfVirtIfMD5KeyEntries": tmnxOspfVirtIfMD5KeyEntries,
       "tmnxOspfCSPFRequests": tmnxOspfCSPFRequests,
       "tmnxOspfCSPFDroppedRequests": tmnxOspfCSPFDroppedRequests,
       "tmnxOspfCSPFPathsFound": tmnxOspfCSPFPathsFound,
       "tmnxOspfCSPFPathsNotFound": tmnxOspfCSPFPathsNotFound,
       "tmnxOspfShamIfEntries": tmnxOspfShamIfEntries,
       "tmnxOspfShamNbrEntries": tmnxOspfShamNbrEntries,
       "tmnxOspfShamIfMD5KeyEntries": tmnxOspfShamIfMD5KeyEntries,
       "tmnxOspfLfaSpfRuns": tmnxOspfLfaSpfRuns,
       "tmnxOspfStatsRlfaRuns": tmnxOspfStatsRlfaRuns,
       "tmnxOspfStatsSidLabelRangeErrs": tmnxOspfStatsSidLabelRangeErrs,
       "tmnxOspfStatsSidDupErrs": tmnxOspfStatsSidDupErrs,
       "tmnxOspfStatsTiLfaRuns": tmnxOspfStatsTiLfaRuns,
       "tmnxOspfChangedTable": tmnxOspfChangedTable,
       "tmnxOspfChangedEntry": tmnxOspfChangedEntry,
       "tmnxOspfAreaTableChanged": tmnxOspfAreaTableChanged,
       "tmnxOspfHostTableChanged": tmnxOspfHostTableChanged,
       "tmnxOspfIfTableChanged": tmnxOspfIfTableChanged,
       "tmnxOspfVirtIfTableChanged": tmnxOspfVirtIfTableChanged,
       "tmnxOspfNbrTableChanged": tmnxOspfNbrTableChanged,
       "tmnxOspfCfgNbrTableChanged": tmnxOspfCfgNbrTableChanged,
       "tmnxOspfVirtNbrTableChanged": tmnxOspfVirtNbrTableChanged,
       "tmnxOspfAreaAggTableChanged": tmnxOspfAreaAggTableChanged,
       "tmnxOspfIfMD5KeyTableChanged": tmnxOspfIfMD5KeyTableChanged,
       "tmnxOspfVirtIfMD5KeyTableChanged": tmnxOspfVirtIfMD5KeyTableChanged,
       "tmnxOspfShamIfTableChanged": tmnxOspfShamIfTableChanged,
       "tmnxOspfShamNbrTableChanged": tmnxOspfShamNbrTableChanged,
       "tmnxOspfShamIfMD5KeyTableChanged": tmnxOspfShamIfMD5KeyTableChanged,
       "tmnxOspfAreaTable": tmnxOspfAreaTable,
       "tmnxOspfAreaEntry": tmnxOspfAreaEntry,
       "tmnxOspfAreaId": tmnxOspfAreaId,
       "tmnxOspfAreaStatus": tmnxOspfAreaStatus,
       "tmnxOspfAreaLastChanged": tmnxOspfAreaLastChanged,
       "tmnxOspfImportAsExtern": tmnxOspfImportAsExtern,
       "tmnxOspfAreaSummary": tmnxOspfAreaSummary,
       "tmnxOspfAreaRangeBlackhole": tmnxOspfAreaRangeBlackhole,
       "tmnxOspfStubMetric": tmnxOspfStubMetric,
       "tmnxOspfAreaStubMetricType": tmnxOspfAreaStubMetricType,
       "tmnxOspfAreaOriginateDefault": tmnxOspfAreaOriginateDefault,
       "tmnxOspfAreaNssaRedistribute": tmnxOspfAreaNssaRedistribute,
       "tmnxOspfAreaNssaTranslatorRole": tmnxOspfAreaNssaTranslatorRole,
       "tmnxOspfAreaNssaTranslatorStabInt": tmnxOspfAreaNssaTranslatorStabInt,
       "tmnxOspfAreaBdrRtrCount": tmnxOspfAreaBdrRtrCount,
       "tmnxOspfAreaAsBdrRtrCount": tmnxOspfAreaAsBdrRtrCount,
       "tmnxOspfAreaScopeLsaCount": tmnxOspfAreaScopeLsaCount,
       "tmnxOspfAreaScopeLsaCksumSum": tmnxOspfAreaScopeLsaCksumSum,
       "tmnxOspfAreaScopeUnkLsaCount": tmnxOspfAreaScopeUnkLsaCount,
       "tmnxOspfAreaScopeUnkLsaCksumSum": tmnxOspfAreaScopeUnkLsaCksumSum,
       "tmnxOspfAreaNssaTranslatorState": tmnxOspfAreaNssaTranslatorState,
       "tmnxOspfAreaActiveInterfaces": tmnxOspfAreaActiveInterfaces,
       "tmnxOspfAreaInterfaceCount": tmnxOspfAreaInterfaceCount,
       "tmnxOspfAreaVirtualLinkCount": tmnxOspfAreaVirtualLinkCount,
       "tmnxOspfAreaLastSpfRunTime": tmnxOspfAreaLastSpfRunTime,
       "tmnxOspfAreaSpfRuns": tmnxOspfAreaSpfRuns,
       "tmnxOspfAreaNssaTranslatorEvents": tmnxOspfAreaNssaTranslatorEvents,
       "tmnxOspfAreaNeighborCount": tmnxOspfAreaNeighborCount,
       "tmnxOspfAreaShamLinkCount": tmnxOspfAreaShamLinkCount,
       "tmnxOspfAreaKeyRolloverInterval": tmnxOspfAreaKeyRolloverInterval,
       "tmnxOspfAreaLoopfreeAltExclude": tmnxOspfAreaLoopfreeAltExclude,
       "tmnxOspfAreaNssaAdjCheck": tmnxOspfAreaNssaAdjCheck,
       "tmnxOspfAreaAdvRtrCapability": tmnxOspfAreaAdvRtrCapability,
       "tmnxOspfAreaDbExportExclude": tmnxOspfAreaDbExportExclude,
       "tmnxOspfAreaExtendedLsa": tmnxOspfAreaExtendedLsa,
       "tmnxOspfAreaImportPolicy1": tmnxOspfAreaImportPolicy1,
       "tmnxOspfAreaImportPolicy2": tmnxOspfAreaImportPolicy2,
       "tmnxOspfAreaImportPolicy3": tmnxOspfAreaImportPolicy3,
       "tmnxOspfAreaImportPolicy4": tmnxOspfAreaImportPolicy4,
       "tmnxOspfAreaImportPolicy5": tmnxOspfAreaImportPolicy5,
       "tmnxOspfAreaExportPolicy1": tmnxOspfAreaExportPolicy1,
       "tmnxOspfAreaExportPolicy2": tmnxOspfAreaExportPolicy2,
       "tmnxOspfAreaExportPolicy3": tmnxOspfAreaExportPolicy3,
       "tmnxOspfAreaExportPolicy4": tmnxOspfAreaExportPolicy4,
       "tmnxOspfAreaExportPolicy5": tmnxOspfAreaExportPolicy5,
       "tmnxOspfAreaAdvertiseNeProfile": tmnxOspfAreaAdvertiseNeProfile,
       "tmnxOspfAreaBierTemplate": tmnxOspfAreaBierTemplate,
       "tmnxOspfAreaBierTemplAdminState": tmnxOspfAreaBierTemplAdminState,
       "tmnxOspfAreaLsaCountTable": tmnxOspfAreaLsaCountTable,
       "tmnxOspfAreaLsaCountEntry": tmnxOspfAreaLsaCountEntry,
       "tmnxOspfAreaLsaCountLsaType": tmnxOspfAreaLsaCountLsaType,
       "tmnxOspfAreaLsaCountNumber": tmnxOspfAreaLsaCountNumber,
       "tmnxOspfAsLsdbTable": tmnxOspfAsLsdbTable,
       "tmnxOspfAsLsdbEntry": tmnxOspfAsLsdbEntry,
       "tmnxOspfAsLsdbType": tmnxOspfAsLsdbType,
       "tmnxOspfAsLsdbRouterId": tmnxOspfAsLsdbRouterId,
       "tmnxOspfAsLsdbLsid": tmnxOspfAsLsdbLsid,
       "tmnxOspfAsLsdbSequence": tmnxOspfAsLsdbSequence,
       "tmnxOspfAsLsdbAge": tmnxOspfAsLsdbAge,
       "tmnxOspfAsLsdbChecksum": tmnxOspfAsLsdbChecksum,
       "tmnxOspfAsLsdbAdvertisement": tmnxOspfAsLsdbAdvertisement,
       "tmnxOspfAsLsdbTypeKnown": tmnxOspfAsLsdbTypeKnown,
       "tmnxOspfAreaLsdbTable": tmnxOspfAreaLsdbTable,
       "tmnxOspfAreaLsdbEntry": tmnxOspfAreaLsdbEntry,
       "tmnxOspfAreaLsdbAreaId": tmnxOspfAreaLsdbAreaId,
       "tmnxOspfAreaLsdbType": tmnxOspfAreaLsdbType,
       "tmnxOspfAreaLsdbRouterId": tmnxOspfAreaLsdbRouterId,
       "tmnxOspfAreaLsdbLsid": tmnxOspfAreaLsdbLsid,
       "tmnxOspfAreaLsdbSequence": tmnxOspfAreaLsdbSequence,
       "tmnxOspfAreaLsdbAge": tmnxOspfAreaLsdbAge,
       "tmnxOspfAreaLsdbChecksum": tmnxOspfAreaLsdbChecksum,
       "tmnxOspfAreaLsdbAdvertisement": tmnxOspfAreaLsdbAdvertisement,
       "tmnxOspfAreaLsdbTypeKnown": tmnxOspfAreaLsdbTypeKnown,
       "tmnxOspfAreaLsdbImportFltrd": tmnxOspfAreaLsdbImportFltrd,
       "tmnxOspfAreaLsdbExportFltrd": tmnxOspfAreaLsdbExportFltrd,
       "tmnxOspfLinkLsdbTable": tmnxOspfLinkLsdbTable,
       "tmnxOspfLinkLsdbEntry": tmnxOspfLinkLsdbEntry,
       "tmnxOspfLinkLsdbIfIndex": tmnxOspfLinkLsdbIfIndex,
       "tmnxOspfLinkLsdbIfInstId": tmnxOspfLinkLsdbIfInstId,
       "tmnxOspfLinkLsdbType": tmnxOspfLinkLsdbType,
       "tmnxOspfLinkLsdbRouterId": tmnxOspfLinkLsdbRouterId,
       "tmnxOspfLinkLsdbLsid": tmnxOspfLinkLsdbLsid,
       "tmnxOspfLinkLsdbSequence": tmnxOspfLinkLsdbSequence,
       "tmnxOspfLinkLsdbAge": tmnxOspfLinkLsdbAge,
       "tmnxOspfLinkLsdbChecksum": tmnxOspfLinkLsdbChecksum,
       "tmnxOspfLinkLsdbAdvertisement": tmnxOspfLinkLsdbAdvertisement,
       "tmnxOspfLinkLsdbTypeKnown": tmnxOspfLinkLsdbTypeKnown,
       "tmnxOspfHostTable": tmnxOspfHostTable,
       "tmnxOspfHostEntry": tmnxOspfHostEntry,
       "tmnxOspfHostAddressType": tmnxOspfHostAddressType,
       "tmnxOspfHostAddress": tmnxOspfHostAddress,
       "tmnxOspfHostMetric": tmnxOspfHostMetric,
       "tmnxOspfHostStatus": tmnxOspfHostStatus,
       "tmnxOspfHostLastChanged": tmnxOspfHostLastChanged,
       "tmnxOspfHostAreaID": tmnxOspfHostAreaID,
       "tmnxOspfIfTable": tmnxOspfIfTable,
       "tmnxOspfIfEntry": tmnxOspfIfEntry,
       "tmnxOspfIfIndex": tmnxOspfIfIndex,
       "tmnxOspfIfInstId": tmnxOspfIfInstId,
       "tmnxOspfIfStatus": tmnxOspfIfStatus,
       "tmnxOspfIfLastChanged": tmnxOspfIfLastChanged,
       "tmnxOspfIfAreaId": tmnxOspfIfAreaId,
       "tmnxOspfIfCfgType": tmnxOspfIfCfgType,
       "tmnxOspfIfAdminState": tmnxOspfIfAdminState,
       "tmnxOspfIfRtrPriority": tmnxOspfIfRtrPriority,
       "tmnxOspfIfTransitDelay": tmnxOspfIfTransitDelay,
       "tmnxOspfIfRetransInterval": tmnxOspfIfRetransInterval,
       "tmnxOspfIfHelloInterval": tmnxOspfIfHelloInterval,
       "tmnxOspfIfRtrDeadInterval": tmnxOspfIfRtrDeadInterval,
       "tmnxOspfIfPollInterval": tmnxOspfIfPollInterval,
       "tmnxOspfIfMulticastForwarding": tmnxOspfIfMulticastForwarding,
       "tmnxOspfIfCfgMTU": tmnxOspfIfCfgMTU,
       "tmnxOspfIfCfgMetric": tmnxOspfIfCfgMetric,
       "tmnxOspfIfPassive": tmnxOspfIfPassive,
       "tmnxOspfIfAdvtSubnet": tmnxOspfIfAdvtSubnet,
       "tmnxOspfIfDemand": tmnxOspfIfDemand,
       "tmnxOspfIfDemandNbrProbe": tmnxOspfIfDemandNbrProbe,
       "tmnxOspfIfDemandNbrProbeRetxLimit": tmnxOspfIfDemandNbrProbeRetxLimit,
       "tmnxOspfIfDemandNbrProbeInterval": tmnxOspfIfDemandNbrProbeInterval,
       "tmnxOspfIfAuthType": tmnxOspfIfAuthType,
       "tmnxOspfIfAuthKey": tmnxOspfIfAuthKey,
       "tmnxOspfIfState": tmnxOspfIfState,
       "tmnxOspfIfLastEnabledTime": tmnxOspfIfLastEnabledTime,
       "tmnxOspfIfOperMTU": tmnxOspfIfOperMTU,
       "tmnxOspfIfMetricValue": tmnxOspfIfMetricValue,
       "tmnxOspfIfDRId": tmnxOspfIfDRId,
       "tmnxOspfIfDRIpAddrType": tmnxOspfIfDRIpAddrType,
       "tmnxOspfIfDRIpAddr": tmnxOspfIfDRIpAddr,
       "tmnxOspfIfBDRId": tmnxOspfIfBDRId,
       "tmnxOspfIfBDRIpAddrType": tmnxOspfIfBDRIpAddrType,
       "tmnxOspfIfBDRIpAddr": tmnxOspfIfBDRIpAddr,
       "tmnxOspfIfLinkLsaCount": tmnxOspfIfLinkLsaCount,
       "tmnxOspfIfLinkLsaCksumSum": tmnxOspfIfLinkLsaCksumSum,
       "tmnxOspfIfLinkUnkLsaCount": tmnxOspfIfLinkUnkLsaCount,
       "tmnxOspfIfLinkUnkLsaCksumSum": tmnxOspfIfLinkUnkLsaCksumSum,
       "tmnxOspfIfMD5TransmitKeyId": tmnxOspfIfMD5TransmitKeyId,
       "tmnxOspfIfLocalIpAddressType": tmnxOspfIfLocalIpAddressType,
       "tmnxOspfIfLocalIpAddress": tmnxOspfIfLocalIpAddress,
       "tmnxOspfIfMD5NumKeys": tmnxOspfIfMD5NumKeys,
       "tmnxOspfIfType": tmnxOspfIfType,
       "tmnxOspfIfEnableBfd": tmnxOspfIfEnableBfd,
       "tmnxOspfIfRemainDownOnFail": tmnxOspfIfRemainDownOnFail,
       "tmnxOspfIfTeMetric": tmnxOspfIfTeMetric,
       "tmnxOspfIfTeState": tmnxOspfIfTeState,
       "tmnxOspfIfAdminGroup": tmnxOspfIfAdminGroup,
       "tmnxOspfIfLdpSyncState": tmnxOspfIfLdpSyncState,
       "tmnxOspfIfLdpSyncMaxMetric": tmnxOspfIfLdpSyncMaxMetric,
       "tmnxOspfIfLdpSyncTimerState": tmnxOspfIfLdpSyncTimerState,
       "tmnxOspfIfLdpSyncTimeLeft": tmnxOspfIfLdpSyncTimeLeft,
       "tmnxOspfIfInboundSAName": tmnxOspfIfInboundSAName,
       "tmnxOspfIfOutboundSAName": tmnxOspfIfOutboundSAName,
       "tmnxOspfIfOperInbSAName": tmnxOspfIfOperInbSAName,
       "tmnxOspfIfOperInbSANameTemp": tmnxOspfIfOperInbSANameTemp,
       "tmnxOspfIfOperOutbSAName": tmnxOspfIfOperOutbSAName,
       "tmnxOspfIfStatsTable": tmnxOspfIfStatsTable,
       "tmnxOspfIfStatsEntry": tmnxOspfIfStatsEntry,
       "tmnxOspfIfEvents": tmnxOspfIfEvents,
       "tmnxOspfIfTxPackets": tmnxOspfIfTxPackets,
       "tmnxOspfIfTxHellos": tmnxOspfIfTxHellos,
       "tmnxOspfIfTxDBDs": tmnxOspfIfTxDBDs,
       "tmnxOspfIfTxLSRs": tmnxOspfIfTxLSRs,
       "tmnxOspfIfTxLSUs": tmnxOspfIfTxLSUs,
       "tmnxOspfIfTxLSAcks": tmnxOspfIfTxLSAcks,
       "tmnxOspfIfRxPackets": tmnxOspfIfRxPackets,
       "tmnxOspfIfRxHellos": tmnxOspfIfRxHellos,
       "tmnxOspfIfRxDBDs": tmnxOspfIfRxDBDs,
       "tmnxOspfIfRxLSRs": tmnxOspfIfRxLSRs,
       "tmnxOspfIfRxLSUs": tmnxOspfIfRxLSUs,
       "tmnxOspfIfRxLSAcks": tmnxOspfIfRxLSAcks,
       "tmnxOspfIfDiscardPackets": tmnxOspfIfDiscardPackets,
       "tmnxOspfIfRetransmitOuts": tmnxOspfIfRetransmitOuts,
       "tmnxOspfIfBadVersions": tmnxOspfIfBadVersions,
       "tmnxOspfIfBadNetworks": tmnxOspfIfBadNetworks,
       "tmnxOspfIfBadVirtualLinks": tmnxOspfIfBadVirtualLinks,
       "tmnxOspfIfBadAreas": tmnxOspfIfBadAreas,
       "tmnxOspfIfBadDstAddrs": tmnxOspfIfBadDstAddrs,
       "tmnxOspfIfBadNeighbors": tmnxOspfIfBadNeighbors,
       "tmnxOspfIfBadPacketTypes": tmnxOspfIfBadPacketTypes,
       "tmnxOspfIfNeighborCount": tmnxOspfIfNeighborCount,
       "tmnxOspfIfLastEventTime": tmnxOspfIfLastEventTime,
       "tmnxOspfIfBadLengths": tmnxOspfIfBadLengths,
       "tmnxOspfIfBadHelloIntervals": tmnxOspfIfBadHelloIntervals,
       "tmnxOspfIfBadDeadIntervals": tmnxOspfIfBadDeadIntervals,
       "tmnxOspfIfBadOptions": tmnxOspfIfBadOptions,
       "tmnxOspfIfRxBadChecksums": tmnxOspfIfRxBadChecksums,
       "tmnxOspfIfBadAuthTypes": tmnxOspfIfBadAuthTypes,
       "tmnxOspfIfAuthFailures": tmnxOspfIfAuthFailures,
       "tmnxOspfVirtIfTable": tmnxOspfVirtIfTable,
       "tmnxOspfVirtIfEntry": tmnxOspfVirtIfEntry,
       "tmnxOspfVirtIfAreaId": tmnxOspfVirtIfAreaId,
       "tmnxOspfVirtIfNeighbor": tmnxOspfVirtIfNeighbor,
       "tmnxOspfVirtIfStatus": tmnxOspfVirtIfStatus,
       "tmnxOspfVirtIfLastChanged": tmnxOspfVirtIfLastChanged,
       "tmnxOspfVirtIfIndex": tmnxOspfVirtIfIndex,
       "tmnxOspfVirtIfInstId": tmnxOspfVirtIfInstId,
       "tmnxOspfVirtIfAdminStat": tmnxOspfVirtIfAdminStat,
       "tmnxOspfVirtIfTransitDelay": tmnxOspfVirtIfTransitDelay,
       "tmnxOspfVirtIfRetransInterval": tmnxOspfVirtIfRetransInterval,
       "tmnxOspfVirtIfHelloInterval": tmnxOspfVirtIfHelloInterval,
       "tmnxOspfVirtIfRtrDeadInterval": tmnxOspfVirtIfRtrDeadInterval,
       "tmnxOspfVirtIfAuthType": tmnxOspfVirtIfAuthType,
       "tmnxOspfVirtIfAuthKey": tmnxOspfVirtIfAuthKey,
       "tmnxOspfVirtIfState": tmnxOspfVirtIfState,
       "tmnxOspfVirtIfLastEnabledTime": tmnxOspfVirtIfLastEnabledTime,
       "tmnxOspfVirtIfCost": tmnxOspfVirtIfCost,
       "tmnxOspfVirtIfLinkLsaCount": tmnxOspfVirtIfLinkLsaCount,
       "tmnxOspfVirtIfLinkLsaCksumSum": tmnxOspfVirtIfLinkLsaCksumSum,
       "tmnxOspfVirtIfLinkUnkLsaCount": tmnxOspfVirtIfLinkUnkLsaCount,
       "tmnxOspfVirtIfLinkUnkLsaCksumSum": tmnxOspfVirtIfLinkUnkLsaCksumSum,
       "tmnxOspfVirtIfMD5TransmitKeyId": tmnxOspfVirtIfMD5TransmitKeyId,
       "tmnxOspfVirtIfLocalIpAddrType": tmnxOspfVirtIfLocalIpAddrType,
       "tmnxOspfVirtIfLocalIpAddress": tmnxOspfVirtIfLocalIpAddress,
       "tmnxOspfVirtIfMD5NumKeys": tmnxOspfVirtIfMD5NumKeys,
       "tmnxOspfVirtIfInboundSAName": tmnxOspfVirtIfInboundSAName,
       "tmnxOspfVirtIfOutboundSAName": tmnxOspfVirtIfOutboundSAName,
       "tmnxOspfVirtIfOperInbSAName": tmnxOspfVirtIfOperInbSAName,
       "tmnxOspfVirtIfOperInbSANameTemp": tmnxOspfVirtIfOperInbSANameTemp,
       "tmnxOspfVirtIfOperOutbSAName": tmnxOspfVirtIfOperOutbSAName,
       "tmnxOspfVirtIfAuthKeyChain": tmnxOspfVirtIfAuthKeyChain,
       "tmnxOspfVirtIfStatsTable": tmnxOspfVirtIfStatsTable,
       "tmnxOspfVirtIfStatsEntry": tmnxOspfVirtIfStatsEntry,
       "tmnxOspfVirtIfEvents": tmnxOspfVirtIfEvents,
       "tmnxOspfVirtIfTxPackets": tmnxOspfVirtIfTxPackets,
       "tmnxOspfVirtIfTxHellos": tmnxOspfVirtIfTxHellos,
       "tmnxOspfVirtIfTxDBDs": tmnxOspfVirtIfTxDBDs,
       "tmnxOspfVirtIfTxLSRs": tmnxOspfVirtIfTxLSRs,
       "tmnxOspfVirtIfTxLSUs": tmnxOspfVirtIfTxLSUs,
       "tmnxOspfVirtIfTxLSAcks": tmnxOspfVirtIfTxLSAcks,
       "tmnxOspfVirtIfRxPackets": tmnxOspfVirtIfRxPackets,
       "tmnxOspfVirtIfRxHellos": tmnxOspfVirtIfRxHellos,
       "tmnxOspfVirtIfRxDBDs": tmnxOspfVirtIfRxDBDs,
       "tmnxOspfVirtIfRxLSRs": tmnxOspfVirtIfRxLSRs,
       "tmnxOspfVirtIfRxLSUs": tmnxOspfVirtIfRxLSUs,
       "tmnxOspfVirtIfRxLSAcks": tmnxOspfVirtIfRxLSAcks,
       "tmnxOspfVirtIfDiscardPackets": tmnxOspfVirtIfDiscardPackets,
       "tmnxOspfVirtIfRetransmitOuts": tmnxOspfVirtIfRetransmitOuts,
       "tmnxOspfVirtIfBadVersions": tmnxOspfVirtIfBadVersions,
       "tmnxOspfVirtIfBadNetworks": tmnxOspfVirtIfBadNetworks,
       "tmnxOspfVirtIfBadAreas": tmnxOspfVirtIfBadAreas,
       "tmnxOspfVirtIfBadDstAddrs": tmnxOspfVirtIfBadDstAddrs,
       "tmnxOspfVirtIfBadNeighbors": tmnxOspfVirtIfBadNeighbors,
       "tmnxOspfVirtIfBadPacketTypes": tmnxOspfVirtIfBadPacketTypes,
       "tmnxOspfVirtIfLastEventTime": tmnxOspfVirtIfLastEventTime,
       "tmnxOspfVirtIfBadLengths": tmnxOspfVirtIfBadLengths,
       "tmnxOspfVirtIfBadHelloIntervls": tmnxOspfVirtIfBadHelloIntervls,
       "tmnxOspfVirtIfBadDeadIntervals": tmnxOspfVirtIfBadDeadIntervals,
       "tmnxOspfVirtIfBadOptions": tmnxOspfVirtIfBadOptions,
       "tmnxOspfVirtIfRxBadChecksums": tmnxOspfVirtIfRxBadChecksums,
       "tmnxOspfVirtIfBadAuthTypes": tmnxOspfVirtIfBadAuthTypes,
       "tmnxOspfVirtIfAuthFailures": tmnxOspfVirtIfAuthFailures,
       "tmnxOspfVirtIfTxFailures": tmnxOspfVirtIfTxFailures,
       "tmnxOspfNbrTable": tmnxOspfNbrTable,
       "tmnxOspfNbrEntry": tmnxOspfNbrEntry,
       "tmnxOspfNbrIfIndex": tmnxOspfNbrIfIndex,
       "tmnxOspfNbrIfInstId": tmnxOspfNbrIfInstId,
       "tmnxOspfNbrRtrId": tmnxOspfNbrRtrId,
       "tmnxOspfNbrAddressType": tmnxOspfNbrAddressType,
       "tmnxOspfNbrAddress": tmnxOspfNbrAddress,
       "tmnxOspfNbrOptions": tmnxOspfNbrOptions,
       "tmnxOspfNbrPriority": tmnxOspfNbrPriority,
       "tmnxOspfNbrState": tmnxOspfNbrState,
       "tmnxOspfNbrHelloSuppressed": tmnxOspfNbrHelloSuppressed,
       "tmnxOspfNbrIfId": tmnxOspfNbrIfId,
       "tmnxOspfNbrRestartHelperStatus": tmnxOspfNbrRestartHelperStatus,
       "tmnxOspfNbrRestartHelperAge": tmnxOspfNbrRestartHelperAge,
       "tmnxOspfNbrRestartHelperExitRc": tmnxOspfNbrRestartHelperExitRc,
       "tmnxOspfNbrUpTime": tmnxOspfNbrUpTime,
       "tmnxOspfNbrLastEventTime": tmnxOspfNbrLastEventTime,
       "tmnxOspfNbrDeadTimeOutstanding": tmnxOspfNbrDeadTimeOutstanding,
       "tmnxOspfNbrLastRestartTime": tmnxOspfNbrLastRestartTime,
       "tmnxOspfNbrRestartReason": tmnxOspfNbrRestartReason,
       "tmnxOspfNbrBfdTracking": tmnxOspfNbrBfdTracking,
       "tmnxOspfNbrDrId": tmnxOspfNbrDrId,
       "tmnxOspfNbrBdrId": tmnxOspfNbrBdrId,
       "tmnxOspfNbrStatsTable": tmnxOspfNbrStatsTable,
       "tmnxOspfNbrStatsEntry": tmnxOspfNbrStatsEntry,
       "tmnxOspfNbrEvents": tmnxOspfNbrEvents,
       "tmnxOspfNbrLsRetransQLen": tmnxOspfNbrLsRetransQLen,
       "tmnxOspfNbrBadNbrStates": tmnxOspfNbrBadNbrStates,
       "tmnxOspfNbrLsaInstallFailed": tmnxOspfNbrLsaInstallFailed,
       "tmnxOspfNbrBadSeqNums": tmnxOspfNbrBadSeqNums,
       "tmnxOspfNbrBadMTUs": tmnxOspfNbrBadMTUs,
       "tmnxOspfNbrBadPackets": tmnxOspfNbrBadPackets,
       "tmnxOspfNbrLsaNotInLsdbs": tmnxOspfNbrLsaNotInLsdbs,
       "tmnxOspfNbrOptionMismatches": tmnxOspfNbrOptionMismatches,
       "tmnxOspfNbrDuplicates": tmnxOspfNbrDuplicates,
       "tmnxOspfNbrNumRestarts": tmnxOspfNbrNumRestarts,
       "tmnxOspfCfgNbrTable": tmnxOspfCfgNbrTable,
       "tmnxOspfCfgNbrEntry": tmnxOspfCfgNbrEntry,
       "tmnxOspfCfgNbrIfIndex": tmnxOspfCfgNbrIfIndex,
       "tmnxOspfCfgNbrIfInstId": tmnxOspfCfgNbrIfInstId,
       "tmnxOspfCfgNbrAddressType": tmnxOspfCfgNbrAddressType,
       "tmnxOspfCfgNbrAddress": tmnxOspfCfgNbrAddress,
       "tmnxOspfCfgNbrStatus": tmnxOspfCfgNbrStatus,
       "tmnxOspfCfgNbrStorageType": tmnxOspfCfgNbrStorageType,
       "tmnxOspfCfgNbrLastChanged": tmnxOspfCfgNbrLastChanged,
       "tmnxOspfCfgNbrPriority": tmnxOspfCfgNbrPriority,
       "tmnxOspfCfgNbrRtrId": tmnxOspfCfgNbrRtrId,
       "tmnxOspfCfgNbrState": tmnxOspfCfgNbrState,
       "tmnxOspfVirtNbrTable": tmnxOspfVirtNbrTable,
       "tmnxOspfVirtNbrEntry": tmnxOspfVirtNbrEntry,
       "tmnxOspfVirtNbrArea": tmnxOspfVirtNbrArea,
       "tmnxOspfVirtNbrRtrId": tmnxOspfVirtNbrRtrId,
       "tmnxOspfVirtNbrIfIndex": tmnxOspfVirtNbrIfIndex,
       "tmnxOspfVirtNbrIfInstId": tmnxOspfVirtNbrIfInstId,
       "tmnxOspfVirtNbrAddressType": tmnxOspfVirtNbrAddressType,
       "tmnxOspfVirtNbrAddress": tmnxOspfVirtNbrAddress,
       "tmnxOspfVirtNbrOptions": tmnxOspfVirtNbrOptions,
       "tmnxOspfVirtNbrState": tmnxOspfVirtNbrState,
       "tmnxOspfVirtNbrHelloSuppressed": tmnxOspfVirtNbrHelloSuppressed,
       "tmnxOspfVirtNbrIfId": tmnxOspfVirtNbrIfId,
       "tmnxOspfVirtNbrRestartHelperStatus": tmnxOspfVirtNbrRestartHelperStatus,
       "tmnxOspfVirtNbrRestartHelperAge": tmnxOspfVirtNbrRestartHelperAge,
       "tmnxOspfVirtNbrRestartHelperExitRc": tmnxOspfVirtNbrRestartHelperExitRc,
       "tmnxOspfVirtNbrUpTime": tmnxOspfVirtNbrUpTime,
       "tmnxOspfVirtNbrLastEventTime": tmnxOspfVirtNbrLastEventTime,
       "tmnxOspfVirtNbrDeadTmeOutstng": tmnxOspfVirtNbrDeadTmeOutstng,
       "tmnxOspfVirtNbrLastRestartTime": tmnxOspfVirtNbrLastRestartTime,
       "tmnxOspfVirtNbrRestartReason": tmnxOspfVirtNbrRestartReason,
       "tmnxOspfVirtNbrStatsTable": tmnxOspfVirtNbrStatsTable,
       "tmnxOspfVirtNbrStatsEntry": tmnxOspfVirtNbrStatsEntry,
       "tmnxOspfVirtNbrEvents": tmnxOspfVirtNbrEvents,
       "tmnxOspfVirtNbrLsRetransQLen": tmnxOspfVirtNbrLsRetransQLen,
       "tmnxOspfVirtNbrBadNbrStates": tmnxOspfVirtNbrBadNbrStates,
       "tmnxOspfVirtNbrLsaInstallFail": tmnxOspfVirtNbrLsaInstallFail,
       "tmnxOspfVirtNbrBadSeqNums": tmnxOspfVirtNbrBadSeqNums,
       "tmnxOspfVirtNbrBadMTUs": tmnxOspfVirtNbrBadMTUs,
       "tmnxOspfVirtNbrBadPackets": tmnxOspfVirtNbrBadPackets,
       "tmnxOspfVirtNbrLsaNotInLsdbs": tmnxOspfVirtNbrLsaNotInLsdbs,
       "tmnxOspfVirtNbrOptionMismatch": tmnxOspfVirtNbrOptionMismatch,
       "tmnxOspfVirtNbrDuplicates": tmnxOspfVirtNbrDuplicates,
       "tmnxOspfVirtNbrNumRestarts": tmnxOspfVirtNbrNumRestarts,
       "tmnxOspfAreaAggrTable": tmnxOspfAreaAggrTable,
       "tmnxOspfAreaAggrEntry": tmnxOspfAreaAggrEntry,
       "tmnxOspfAreaAggrAreaID": tmnxOspfAreaAggrAreaID,
       "tmnxOspfAreaAggrAreaLsdbType": tmnxOspfAreaAggrAreaLsdbType,
       "tmnxOspfAreaAggrPrefixType": tmnxOspfAreaAggrPrefixType,
       "tmnxOspfAreaAggrPrefix": tmnxOspfAreaAggrPrefix,
       "tmnxOspfAreaAggrPrefixLength": tmnxOspfAreaAggrPrefixLength,
       "tmnxOspfAreaAggrStatus": tmnxOspfAreaAggrStatus,
       "tmnxOspfAreaAggrLastChanged": tmnxOspfAreaAggrLastChanged,
       "tmnxOspfAreaAggrEffect": tmnxOspfAreaAggrEffect,
       "tmnxOspfAreaAggrRouteTag": tmnxOspfAreaAggrRouteTag,
       "tmnxOspfIfMD5KeyTable": tmnxOspfIfMD5KeyTable,
       "tmnxOspfIfMD5KeyEntry": tmnxOspfIfMD5KeyEntry,
       "tmnxOspfIfMD5KeyIndex": tmnxOspfIfMD5KeyIndex,
       "tmnxOspfIfMD5KeyStatus": tmnxOspfIfMD5KeyStatus,
       "tmnxOspfIfMD5KeyKey": tmnxOspfIfMD5KeyKey,
       "tmnxOspfIfMD5KeyStartTime": tmnxOspfIfMD5KeyStartTime,
       "tmnxOspfIfMD5KeyStopTime": tmnxOspfIfMD5KeyStopTime,
       "tmnxOspfVirtIfMD5KeyTable": tmnxOspfVirtIfMD5KeyTable,
       "tmnxOspfVirtIfMD5KeyEntry": tmnxOspfVirtIfMD5KeyEntry,
       "tmnxOspfVirtIfMD5KeyIndex": tmnxOspfVirtIfMD5KeyIndex,
       "tmnxOspfVirtIfMD5KeyStatus": tmnxOspfVirtIfMD5KeyStatus,
       "tmnxOspfVirtIfMD5KeyKey": tmnxOspfVirtIfMD5KeyKey,
       "tmnxOspfVirtIfMD5KeyStartTime": tmnxOspfVirtIfMD5KeyStartTime,
       "tmnxOspfVirtIfMD5KeyStopTime": tmnxOspfVirtIfMD5KeyStopTime,
       "tmnxOspfNotifyObjs": tmnxOspfNotifyObjs,
       "tmnxOspfSetTrap": tmnxOspfSetTrap,
       "tmnxOspfConfigErrorType": tmnxOspfConfigErrorType,
       "tmnxOspfPacketType": tmnxOspfPacketType,
       "tmnxOspfPacketSrcAddressType": tmnxOspfPacketSrcAddressType,
       "tmnxOspfPacketSrcAddress": tmnxOspfPacketSrcAddress,
       "tmnxOspfIfIpName": tmnxOspfIfIpName,
       "tmnxOspfIfEvent": tmnxOspfIfEvent,
       "tmnxOspfFailureReasonCode": tmnxOspfFailureReasonCode,
       "tmnxOspfBadPacketErrType": tmnxOspfBadPacketErrType,
       "tmnxOspfNotifPfxSidRangeStartLbl": tmnxOspfNotifPfxSidRangeStartLbl,
       "tmnxOspfNotifPfxSidRangeMaxIdx": tmnxOspfNotifPfxSidRangeMaxIdx,
       "tmnxOspfNotifPfxNhAdvRtr": tmnxOspfNotifPfxNhAdvRtr,
       "tmnxOspfNotifyDescription": tmnxOspfNotifyDescription,
       "tmnxOspfBfdSessSetupFailReason": tmnxOspfBfdSessSetupFailReason,
       "tmnxOspfNotifSrgbRangeStartLbl": tmnxOspfNotifSrgbRangeStartLbl,
       "tmnxOspfNotifSrgbRangeMaxIdx": tmnxOspfNotifSrgbRangeMaxIdx,
       "tmnxOspfNotifSrgbAdvRtrID": tmnxOspfNotifSrgbAdvRtrID,
       "tmnxOspfNotifSrgbAreaId": tmnxOspfNotifSrgbAreaId,
       "tmnxOspfNotifyIfIndex": tmnxOspfNotifyIfIndex,
       "tmnxOspfNotifyNbrRouterId": tmnxOspfNotifyNbrRouterId,
       "tmnxOspfNotifStatsIndexStatus": tmnxOspfNotifStatsIndexStatus,
       "tmnxOspfShamIfTable": tmnxOspfShamIfTable,
       "tmnxOspfShamIfEntry": tmnxOspfShamIfEntry,
       "tmnxOspfShamIfIndex": tmnxOspfShamIfIndex,
       "tmnxOspfShamIfInstId": tmnxOspfShamIfInstId,
       "tmnxOspfShamIfRemoteNbrAddrType": tmnxOspfShamIfRemoteNbrAddrType,
       "tmnxOspfShamIfRemoteNbrAddress": tmnxOspfShamIfRemoteNbrAddress,
       "tmnxOspfShamIfStatus": tmnxOspfShamIfStatus,
       "tmnxOspfShamIfLastChanged": tmnxOspfShamIfLastChanged,
       "tmnxOspfShamIfAreaId": tmnxOspfShamIfAreaId,
       "tmnxOspfShamIfAdminState": tmnxOspfShamIfAdminState,
       "tmnxOspfShamIfTransitDelay": tmnxOspfShamIfTransitDelay,
       "tmnxOspfShamIfRetransInterval": tmnxOspfShamIfRetransInterval,
       "tmnxOspfShamIfHelloInterval": tmnxOspfShamIfHelloInterval,
       "tmnxOspfShamIfRtrDeadInterval": tmnxOspfShamIfRtrDeadInterval,
       "tmnxOspfShamIfCfgMetric": tmnxOspfShamIfCfgMetric,
       "tmnxOspfShamIfAuthType": tmnxOspfShamIfAuthType,
       "tmnxOspfShamIfAuthKey": tmnxOspfShamIfAuthKey,
       "tmnxOspfShamIfState": tmnxOspfShamIfState,
       "tmnxOspfShamIfLastEnabledTime": tmnxOspfShamIfLastEnabledTime,
       "tmnxOspfShamIfLinkLsaCount": tmnxOspfShamIfLinkLsaCount,
       "tmnxOspfShamIfLinkLsaCksumSum": tmnxOspfShamIfLinkLsaCksumSum,
       "tmnxOspfShamIfLinkUnkLsaCount": tmnxOspfShamIfLinkUnkLsaCount,
       "tmnxOspfShamIfLinkUnkLsaCksumSum": tmnxOspfShamIfLinkUnkLsaCksumSum,
       "tmnxOspfShamIfMD5TransmitKeyId": tmnxOspfShamIfMD5TransmitKeyId,
       "tmnxOspfShamIfLocalIpAddressType": tmnxOspfShamIfLocalIpAddressType,
       "tmnxOspfShamIfLocalIpAddress": tmnxOspfShamIfLocalIpAddress,
       "tmnxOspfShamIfMD5NumKeys": tmnxOspfShamIfMD5NumKeys,
       "tmnxOspfShamIfAuthKeyChain": tmnxOspfShamIfAuthKeyChain,
       "tmnxOspfShamIfStatsTable": tmnxOspfShamIfStatsTable,
       "tmnxOspfShamIfStatsEntry": tmnxOspfShamIfStatsEntry,
       "tmnxOspfShamIfEvents": tmnxOspfShamIfEvents,
       "tmnxOspfShamIfTxPackets": tmnxOspfShamIfTxPackets,
       "tmnxOspfShamIfTxHellos": tmnxOspfShamIfTxHellos,
       "tmnxOspfShamIfTxDBDs": tmnxOspfShamIfTxDBDs,
       "tmnxOspfShamIfTxLSRs": tmnxOspfShamIfTxLSRs,
       "tmnxOspfShamIfTxLSUs": tmnxOspfShamIfTxLSUs,
       "tmnxOspfShamIfTxLSAcks": tmnxOspfShamIfTxLSAcks,
       "tmnxOspfShamIfRxPackets": tmnxOspfShamIfRxPackets,
       "tmnxOspfShamIfRxHellos": tmnxOspfShamIfRxHellos,
       "tmnxOspfShamIfRxDBDs": tmnxOspfShamIfRxDBDs,
       "tmnxOspfShamIfRxLSRs": tmnxOspfShamIfRxLSRs,
       "tmnxOspfShamIfRxLSUs": tmnxOspfShamIfRxLSUs,
       "tmnxOspfShamIfRxLSAcks": tmnxOspfShamIfRxLSAcks,
       "tmnxOspfShamIfDiscardPackets": tmnxOspfShamIfDiscardPackets,
       "tmnxOspfShamIfRetransmitOuts": tmnxOspfShamIfRetransmitOuts,
       "tmnxOspfShamIfBadVersions": tmnxOspfShamIfBadVersions,
       "tmnxOspfShamIfBadNetworks": tmnxOspfShamIfBadNetworks,
       "tmnxOspfShamIfBadAreas": tmnxOspfShamIfBadAreas,
       "tmnxOspfShamIfBadDstAddrs": tmnxOspfShamIfBadDstAddrs,
       "tmnxOspfShamIfBadNeighbors": tmnxOspfShamIfBadNeighbors,
       "tmnxOspfShamIfBadPacketTypes": tmnxOspfShamIfBadPacketTypes,
       "tmnxOspfShamIfLastEventTime": tmnxOspfShamIfLastEventTime,
       "tmnxOspfShamIfBadLengths": tmnxOspfShamIfBadLengths,
       "tmnxOspfShamIfBadHelloIntervals": tmnxOspfShamIfBadHelloIntervals,
       "tmnxOspfShamIfBadDeadIntervals": tmnxOspfShamIfBadDeadIntervals,
       "tmnxOspfShamIfBadOptions": tmnxOspfShamIfBadOptions,
       "tmnxOspfShamIfRxBadChecksums": tmnxOspfShamIfRxBadChecksums,
       "tmnxOspfShamIfBadAuthTypes": tmnxOspfShamIfBadAuthTypes,
       "tmnxOspfShamIfAuthFailures": tmnxOspfShamIfAuthFailures,
       "tmnxOspfShamIfTxFailures": tmnxOspfShamIfTxFailures,
       "tmnxOspfShamIfMD5KeyTable": tmnxOspfShamIfMD5KeyTable,
       "tmnxOspfShamIfMD5KeyEntry": tmnxOspfShamIfMD5KeyEntry,
       "tmnxOspfShamIfMD5KeyIndex": tmnxOspfShamIfMD5KeyIndex,
       "tmnxOspfShamIfMD5KeyStatus": tmnxOspfShamIfMD5KeyStatus,
       "tmnxOspfShamIfMD5KeyKey": tmnxOspfShamIfMD5KeyKey,
       "tmnxOspfShamIfMD5KeyStartTime": tmnxOspfShamIfMD5KeyStartTime,
       "tmnxOspfShamIfMD5KeyStopTime": tmnxOspfShamIfMD5KeyStopTime,
       "tmnxOspfShamNbrTable": tmnxOspfShamNbrTable,
       "tmnxOspfShamNbrEntry": tmnxOspfShamNbrEntry,
       "tmnxOspfShamNbrIfIndex": tmnxOspfShamNbrIfIndex,
       "tmnxOspfShamNbrIfInstId": tmnxOspfShamNbrIfInstId,
       "tmnxOspfShamNbrAddressType": tmnxOspfShamNbrAddressType,
       "tmnxOspfShamNbrAddress": tmnxOspfShamNbrAddress,
       "tmnxOspfShamNbrRtrId": tmnxOspfShamNbrRtrId,
       "tmnxOspfShamNbrOptions": tmnxOspfShamNbrOptions,
       "tmnxOspfShamNbrState": tmnxOspfShamNbrState,
       "tmnxOspfShamNbrHelloSuppressed": tmnxOspfShamNbrHelloSuppressed,
       "tmnxOspfShamNbrIfId": tmnxOspfShamNbrIfId,
       "tmnxOspfShamNbrRestartHelperStatus": tmnxOspfShamNbrRestartHelperStatus,
       "tmnxOspfShamNbrRestartHelperAge": tmnxOspfShamNbrRestartHelperAge,
       "tmnxOspfShamNbrRestartHelperExitRc": tmnxOspfShamNbrRestartHelperExitRc,
       "tmnxOspfShamNbrUpTime": tmnxOspfShamNbrUpTime,
       "tmnxOspfShamNbrLastEventTime": tmnxOspfShamNbrLastEventTime,
       "tmnxOspfShamNbrDeadTmeOutstng": tmnxOspfShamNbrDeadTmeOutstng,
       "tmnxOspfShamNbrLastRestartTime": tmnxOspfShamNbrLastRestartTime,
       "tmnxOspfShamNbrRestartReason": tmnxOspfShamNbrRestartReason,
       "tmnxOspfShamNbrStatsTable": tmnxOspfShamNbrStatsTable,
       "tmnxOspfShamNbrStatsEntry": tmnxOspfShamNbrStatsEntry,
       "tmnxOspfShamNbrEvents": tmnxOspfShamNbrEvents,
       "tmnxOspfShamNbrLsRetransQLen": tmnxOspfShamNbrLsRetransQLen,
       "tmnxOspfShamNbrBadNbrStates": tmnxOspfShamNbrBadNbrStates,
       "tmnxOspfShamNbrLsaInstallFail": tmnxOspfShamNbrLsaInstallFail,
       "tmnxOspfShamNbrBadSeqNums": tmnxOspfShamNbrBadSeqNums,
       "tmnxOspfShamNbrBadMTUs": tmnxOspfShamNbrBadMTUs,
       "tmnxOspfShamNbrBadPackets": tmnxOspfShamNbrBadPackets,
       "tmnxOspfShamNbrLsaNotInLsdbs": tmnxOspfShamNbrLsaNotInLsdbs,
       "tmnxOspfShamNbrOptionMismatch": tmnxOspfShamNbrOptionMismatch,
       "tmnxOspfShamNbrDuplicates": tmnxOspfShamNbrDuplicates,
       "tmnxOspfShamNbrNumRestarts": tmnxOspfShamNbrNumRestarts,
       "tmnxOspfNgLinkLsdbTable": tmnxOspfNgLinkLsdbTable,
       "tmnxOspfNgLinkLsdbEntry": tmnxOspfNgLinkLsdbEntry,
       "tmnxOspfNgLinkLsdbIfIndex": tmnxOspfNgLinkLsdbIfIndex,
       "tmnxOspfNgLinkLsdbIfInstId": tmnxOspfNgLinkLsdbIfInstId,
       "tmnxOspfNgLinkLsdbIfAreaId": tmnxOspfNgLinkLsdbIfAreaId,
       "tmnxOspfNgLinkLsdbType": tmnxOspfNgLinkLsdbType,
       "tmnxOspfNgLinkLsdbRouterId": tmnxOspfNgLinkLsdbRouterId,
       "tmnxOspfNgLinkLsdbLsid": tmnxOspfNgLinkLsdbLsid,
       "tmnxOspfNgLinkLsdbSequence": tmnxOspfNgLinkLsdbSequence,
       "tmnxOspfNgLinkLsdbAge": tmnxOspfNgLinkLsdbAge,
       "tmnxOspfNgLinkLsdbChecksum": tmnxOspfNgLinkLsdbChecksum,
       "tmnxOspfNgLinkLsdbAdvertisement": tmnxOspfNgLinkLsdbAdvertisement,
       "tmnxOspfNgLinkLsdbTypeKnown": tmnxOspfNgLinkLsdbTypeKnown,
       "tmnxOspfNgIfTable": tmnxOspfNgIfTable,
       "tmnxOspfNgIfEntry": tmnxOspfNgIfEntry,
       "tmnxOspfNgIfIndex": tmnxOspfNgIfIndex,
       "tmnxOspfNgIfInstId": tmnxOspfNgIfInstId,
       "tmnxOspfNgIfAreaId": tmnxOspfNgIfAreaId,
       "tmnxOspfNgIfStatus": tmnxOspfNgIfStatus,
       "tmnxOspfNgIfLastChanged": tmnxOspfNgIfLastChanged,
       "tmnxOspfNgIfCfgType": tmnxOspfNgIfCfgType,
       "tmnxOspfNgIfAdminState": tmnxOspfNgIfAdminState,
       "tmnxOspfNgIfRtrPriority": tmnxOspfNgIfRtrPriority,
       "tmnxOspfNgIfTransitDelay": tmnxOspfNgIfTransitDelay,
       "tmnxOspfNgIfRetransInterval": tmnxOspfNgIfRetransInterval,
       "tmnxOspfNgIfHelloInterval": tmnxOspfNgIfHelloInterval,
       "tmnxOspfNgIfRtrDeadInterval": tmnxOspfNgIfRtrDeadInterval,
       "tmnxOspfNgIfPollInterval": tmnxOspfNgIfPollInterval,
       "tmnxOspfNgIfCfgMTU": tmnxOspfNgIfCfgMTU,
       "tmnxOspfNgIfCfgMetric": tmnxOspfNgIfCfgMetric,
       "tmnxOspfNgIfPassive": tmnxOspfNgIfPassive,
       "tmnxOspfNgIfAdvtSubnet": tmnxOspfNgIfAdvtSubnet,
       "tmnxOspfNgIfAuthType": tmnxOspfNgIfAuthType,
       "tmnxOspfNgIfAuthKey": tmnxOspfNgIfAuthKey,
       "tmnxOspfNgIfEnableBfd": tmnxOspfNgIfEnableBfd,
       "tmnxOspfNgIfRemainDownOnFail": tmnxOspfNgIfRemainDownOnFail,
       "tmnxOspfNgIfInboundSAName": tmnxOspfNgIfInboundSAName,
       "tmnxOspfNgIfOutboundSAName": tmnxOspfNgIfOutboundSAName,
       "tmnxOspfNgIfLoopfreeAltExclude": tmnxOspfNgIfLoopfreeAltExclude,
       "tmnxOspfNgIfLsaFilterOut": tmnxOspfNgIfLsaFilterOut,
       "tmnxOspfNgIfAdvRtrCapability": tmnxOspfNgIfAdvRtrCapability,
       "tmnxOspfNgIfAuthKeyChain": tmnxOspfNgIfAuthKeyChain,
       "tmnxOspfNgIfRouteNHTemplate": tmnxOspfNgIfRouteNHTemplate,
       "tmnxOspfNgIfPriorityUpdate": tmnxOspfNgIfPriorityUpdate,
       "tmnxOspfNgIfSidType": tmnxOspfNgIfSidType,
       "tmnxOspfNgIfSidValue": tmnxOspfNgIfSidValue,
       "tmnxOspfNgIfSidProtection": tmnxOspfNgIfSidProtection,
       "tmnxOspfNgIfSidClearNFlag": tmnxOspfNgIfSidClearNFlag,
       "tmnxOspfNgIfAdjSidType": tmnxOspfNgIfAdjSidType,
       "tmnxOspfNgIfAdjSidValue": tmnxOspfNgIfAdjSidValue,
       "tmnxOspfNgIfLBAdminWeight": tmnxOspfNgIfLBAdminWeight,
       "tmnxOspfNgIfOperTable": tmnxOspfNgIfOperTable,
       "tmnxOspfNgIfOperEntry": tmnxOspfNgIfOperEntry,
       "tmnxOspfNgIfState": tmnxOspfNgIfState,
       "tmnxOspfNgIfLastEnabledTime": tmnxOspfNgIfLastEnabledTime,
       "tmnxOspfNgIfOperMTU": tmnxOspfNgIfOperMTU,
       "tmnxOspfNgIfMetricValue": tmnxOspfNgIfMetricValue,
       "tmnxOspfNgIfDRId": tmnxOspfNgIfDRId,
       "tmnxOspfNgIfDRIpAddrType": tmnxOspfNgIfDRIpAddrType,
       "tmnxOspfNgIfDRIpAddr": tmnxOspfNgIfDRIpAddr,
       "tmnxOspfNgIfBDRId": tmnxOspfNgIfBDRId,
       "tmnxOspfNgIfBDRIpAddrType": tmnxOspfNgIfBDRIpAddrType,
       "tmnxOspfNgIfBDRIpAddr": tmnxOspfNgIfBDRIpAddr,
       "tmnxOspfNgIfLinkLsaCount": tmnxOspfNgIfLinkLsaCount,
       "tmnxOspfNgIfLinkLsaCksumSum": tmnxOspfNgIfLinkLsaCksumSum,
       "tmnxOspfNgIfMD5TransmitKeyId": tmnxOspfNgIfMD5TransmitKeyId,
       "tmnxOspfNgIfLocalIpAddressType": tmnxOspfNgIfLocalIpAddressType,
       "tmnxOspfNgIfLocalIpAddress": tmnxOspfNgIfLocalIpAddress,
       "tmnxOspfNgIfMD5NumKeys": tmnxOspfNgIfMD5NumKeys,
       "tmnxOspfNgIfType": tmnxOspfNgIfType,
       "tmnxOspfNgIfTeMetric": tmnxOspfNgIfTeMetric,
       "tmnxOspfNgIfTeState": tmnxOspfNgIfTeState,
       "tmnxOspfNgIfAdminGroup": tmnxOspfNgIfAdminGroup,
       "tmnxOspfNgIfLdpSyncState": tmnxOspfNgIfLdpSyncState,
       "tmnxOspfNgIfLdpSyncMaxMetric": tmnxOspfNgIfLdpSyncMaxMetric,
       "tmnxOspfNgIfLdpSyncTimerState": tmnxOspfNgIfLdpSyncTimerState,
       "tmnxOspfNgIfLdpSyncTimeLeft": tmnxOspfNgIfLdpSyncTimeLeft,
       "tmnxOspfNgIfOperInbSAName": tmnxOspfNgIfOperInbSAName,
       "tmnxOspfNgIfOperInbSANameTemp": tmnxOspfNgIfOperInbSANameTemp,
       "tmnxOspfNgIfOperOutbSAName": tmnxOspfNgIfOperOutbSAName,
       "tmnxOspfNgIfStatsTable": tmnxOspfNgIfStatsTable,
       "tmnxOspfNgIfStatsEntry": tmnxOspfNgIfStatsEntry,
       "tmnxOspfNgIfEvents": tmnxOspfNgIfEvents,
       "tmnxOspfNgIfTxPackets": tmnxOspfNgIfTxPackets,
       "tmnxOspfNgIfTxHellos": tmnxOspfNgIfTxHellos,
       "tmnxOspfNgIfTxDBDs": tmnxOspfNgIfTxDBDs,
       "tmnxOspfNgIfTxLSRs": tmnxOspfNgIfTxLSRs,
       "tmnxOspfNgIfTxLSUs": tmnxOspfNgIfTxLSUs,
       "tmnxOspfNgIfTxLSAcks": tmnxOspfNgIfTxLSAcks,
       "tmnxOspfNgIfRxPackets": tmnxOspfNgIfRxPackets,
       "tmnxOspfNgIfRxHellos": tmnxOspfNgIfRxHellos,
       "tmnxOspfNgIfRxDBDs": tmnxOspfNgIfRxDBDs,
       "tmnxOspfNgIfRxLSRs": tmnxOspfNgIfRxLSRs,
       "tmnxOspfNgIfRxLSUs": tmnxOspfNgIfRxLSUs,
       "tmnxOspfNgIfRxLSAcks": tmnxOspfNgIfRxLSAcks,
       "tmnxOspfNgIfDiscardPackets": tmnxOspfNgIfDiscardPackets,
       "tmnxOspfNgIfRetransmitOuts": tmnxOspfNgIfRetransmitOuts,
       "tmnxOspfNgIfBadVersions": tmnxOspfNgIfBadVersions,
       "tmnxOspfNgIfBadNetworks": tmnxOspfNgIfBadNetworks,
       "tmnxOspfNgIfBadVirtualLinks": tmnxOspfNgIfBadVirtualLinks,
       "tmnxOspfNgIfBadAreas": tmnxOspfNgIfBadAreas,
       "tmnxOspfNgIfBadDstAddrs": tmnxOspfNgIfBadDstAddrs,
       "tmnxOspfNgIfBadNeighbors": tmnxOspfNgIfBadNeighbors,
       "tmnxOspfNgIfBadPacketTypes": tmnxOspfNgIfBadPacketTypes,
       "tmnxOspfNgIfNeighborCount": tmnxOspfNgIfNeighborCount,
       "tmnxOspfNgIfLastEventTime": tmnxOspfNgIfLastEventTime,
       "tmnxOspfNgIfBadLengths": tmnxOspfNgIfBadLengths,
       "tmnxOspfNgIfBadHelloIntervals": tmnxOspfNgIfBadHelloIntervals,
       "tmnxOspfNgIfBadDeadIntervals": tmnxOspfNgIfBadDeadIntervals,
       "tmnxOspfNgIfBadOptions": tmnxOspfNgIfBadOptions,
       "tmnxOspfNgIfRxBadChecksums": tmnxOspfNgIfRxBadChecksums,
       "tmnxOspfNgIfBadAuthTypes": tmnxOspfNgIfBadAuthTypes,
       "tmnxOspfNgIfAuthFailures": tmnxOspfNgIfAuthFailures,
       "tmnxOspfNgIfTxFailures": tmnxOspfNgIfTxFailures,
       "tmnxOspfNgNbrTable": tmnxOspfNgNbrTable,
       "tmnxOspfNgNbrEntry": tmnxOspfNgNbrEntry,
       "tmnxOspfNgNbrIfIndex": tmnxOspfNgNbrIfIndex,
       "tmnxOspfNgNbrIfInstId": tmnxOspfNgNbrIfInstId,
       "tmnxOspfNgNbrIfAreaId": tmnxOspfNgNbrIfAreaId,
       "tmnxOspfNgNbrRtrId": tmnxOspfNgNbrRtrId,
       "tmnxOspfNgNbrAddressType": tmnxOspfNgNbrAddressType,
       "tmnxOspfNgNbrAddress": tmnxOspfNgNbrAddress,
       "tmnxOspfNgNbrOptions": tmnxOspfNgNbrOptions,
       "tmnxOspfNgNbrPriority": tmnxOspfNgNbrPriority,
       "tmnxOspfNgNbrState": tmnxOspfNgNbrState,
       "tmnxOspfNgNbrHelloSuppressed": tmnxOspfNgNbrHelloSuppressed,
       "tmnxOspfNgNbrIfId": tmnxOspfNgNbrIfId,
       "tmnxOspfNgNbrRestartHelperStatus": tmnxOspfNgNbrRestartHelperStatus,
       "tmnxOspfNgNbrRestartHelperAge": tmnxOspfNgNbrRestartHelperAge,
       "tmnxOspfNgNbrRestartHelperExitRc": tmnxOspfNgNbrRestartHelperExitRc,
       "tmnxOspfNgNbrUpTime": tmnxOspfNgNbrUpTime,
       "tmnxOspfNgNbrLastEventTime": tmnxOspfNgNbrLastEventTime,
       "tmnxOspfNgNbrDeadTimeOutstanding": tmnxOspfNgNbrDeadTimeOutstanding,
       "tmnxOspfNgNbrLastRestartTime": tmnxOspfNgNbrLastRestartTime,
       "tmnxOspfNgNbrRestartReason": tmnxOspfNgNbrRestartReason,
       "tmnxOspfNgNbrBfdTracking": tmnxOspfNgNbrBfdTracking,
       "tmnxOspfNgNbrDrId": tmnxOspfNgNbrDrId,
       "tmnxOspfNgNbrBdrId": tmnxOspfNgNbrBdrId,
       "tmnxOspfNgNbrSidType": tmnxOspfNgNbrSidType,
       "tmnxOspfNgNbrSidValue": tmnxOspfNgNbrSidValue,
       "tmnxOspfNgNbrStatsTable": tmnxOspfNgNbrStatsTable,
       "tmnxOspfNgNbrStatsEntry": tmnxOspfNgNbrStatsEntry,
       "tmnxOspfNgNbrEvents": tmnxOspfNgNbrEvents,
       "tmnxOspfNgNbrLsRetransQLen": tmnxOspfNgNbrLsRetransQLen,
       "tmnxOspfNgNbrBadNbrStates": tmnxOspfNgNbrBadNbrStates,
       "tmnxOspfNgNbrLsaInstallFailed": tmnxOspfNgNbrLsaInstallFailed,
       "tmnxOspfNgNbrBadSeqNums": tmnxOspfNgNbrBadSeqNums,
       "tmnxOspfNgNbrBadMTUs": tmnxOspfNgNbrBadMTUs,
       "tmnxOspfNgNbrBadPackets": tmnxOspfNgNbrBadPackets,
       "tmnxOspfNgNbrLsaNotInLsdbs": tmnxOspfNgNbrLsaNotInLsdbs,
       "tmnxOspfNgNbrOptionMismatches": tmnxOspfNgNbrOptionMismatches,
       "tmnxOspfNgNbrDuplicates": tmnxOspfNgNbrDuplicates,
       "tmnxOspfNgNbrNumRestarts": tmnxOspfNgNbrNumRestarts,
       "tmnxOspfNgIfMD5KeyTable": tmnxOspfNgIfMD5KeyTable,
       "tmnxOspfNgIfMD5KeyEntry": tmnxOspfNgIfMD5KeyEntry,
       "tmnxOspfNgIfMD5KeyIndex": tmnxOspfNgIfMD5KeyIndex,
       "tmnxOspfNgIfMD5KeyStatus": tmnxOspfNgIfMD5KeyStatus,
       "tmnxOspfNgIfMD5KeyKey": tmnxOspfNgIfMD5KeyKey,
       "tmnxOspfNgIfMD5KeyStartTime": tmnxOspfNgIfMD5KeyStartTime,
       "tmnxOspfNgIfMD5KeyStopTime": tmnxOspfNgIfMD5KeyStopTime,
       "tmnxOspfLfaStatsTable": tmnxOspfLfaStatsTable,
       "tmnxOspfLfaStatsEntry": tmnxOspfLfaStatsEntry,
       "tmnxOspfLfaNodesCovered": tmnxOspfLfaNodesCovered,
       "tmnxOspfLfaTotalNodes": tmnxOspfLfaTotalNodes,
       "tmnxOspfLfaCoverage": tmnxOspfLfaCoverage,
       "tmnxOspfLfaPfxCovered": tmnxOspfLfaPfxCovered,
       "tmnxOspfLfaTotalPfx": tmnxOspfLfaTotalPfx,
       "tmnxOspfLfaPfxCoverage": tmnxOspfLfaPfxCoverage,
       "tmnxOspfPathTable": tmnxOspfPathTable,
       "tmnxOspfPathEntry": tmnxOspfPathEntry,
       "tmnxOspfPathDestRouterId": tmnxOspfPathDestRouterId,
       "tmnxOspfPathIfIndex": tmnxOspfPathIfIndex,
       "tmnxOspfPathNhopRouterId": tmnxOspfPathNhopRouterId,
       "tmnxOspfPathMetric": tmnxOspfPathMetric,
       "tmnxOspfPathLfaIfIndex": tmnxOspfPathLfaIfIndex,
       "tmnxOspfPathLfaType": tmnxOspfPathLfaType,
       "tmnxOspfPathLfaNhopRouterId": tmnxOspfPathLfaNhopRouterId,
       "tmnxOspfPathLfaMetric": tmnxOspfPathLfaMetric,
       "tmnxOspfPathNhOwner": tmnxOspfPathNhOwner,
       "tmnxOspfPathLfaNhOwner": tmnxOspfPathLfaNhOwner,
       "tmnxOspfGeneralExTable": tmnxOspfGeneralExTable,
       "tmnxOspfGeneralExEntry": tmnxOspfGeneralExEntry,
       "tmnxOspfGeneralExLastChanged": tmnxOspfGeneralExLastChanged,
       "tmnxOspfAdvRtrCapability": tmnxOspfAdvRtrCapability,
       "tmnxOspfLFAExcludePolicy1": tmnxOspfLFAExcludePolicy1,
       "tmnxOspfLFAExcludePolicy2": tmnxOspfLFAExcludePolicy2,
       "tmnxOspfLFAExcludePolicy3": tmnxOspfLFAExcludePolicy3,
       "tmnxOspfLFAExcludePolicy4": tmnxOspfLFAExcludePolicy4,
       "tmnxOspfLFAExcludePolicy5": tmnxOspfLFAExcludePolicy5,
       "tmnxOspfRibPriorityListHigh": tmnxOspfRibPriorityListHigh,
       "tmnxOspfPrefixSidRangeType": tmnxOspfPrefixSidRangeType,
       "tmnxOspfPrefixSidRangeStartLabel": tmnxOspfPrefixSidRangeStartLabel,
       "tmnxOspfPrefixSidRangeMaxIdx": tmnxOspfPrefixSidRangeMaxIdx,
       "tmnxOspfSrAdminState": tmnxOspfSrAdminState,
       "tmnxOspfTunnelTablePreference": tmnxOspfTunnelTablePreference,
       "tmnxOspfRemoteLFA": tmnxOspfRemoteLFA,
       "tmnxOspfMaxPqCost": tmnxOspfMaxPqCost,
       "tmnxOspfTunnelMtu": tmnxOspfTunnelMtu,
       "tmnxOspfAdvRtrLsaLimit": tmnxOspfAdvRtrLsaLimit,
       "tmnxOspfAdvRtrLsaLimitTimeout": tmnxOspfAdvRtrLsaLimitTimeout,
       "tmnxOspfAdvRtrLsaLimitWarning": tmnxOspfAdvRtrLsaLimitWarning,
       "tmnxOspfAdvRtrLsaLimitLogOnly": tmnxOspfAdvRtrLsaLimitLogOnly,
       "tmnxOspfSrAdjSidHold": tmnxOspfSrAdjSidHold,
       "tmnxOspfDatabaseExport": tmnxOspfDatabaseExport,
       "tmnxOspfDbExportIdentifierSet": tmnxOspfDbExportIdentifierSet,
       "tmnxOspfDbExportIdentifierLow": tmnxOspfDbExportIdentifierLow,
       "tmnxOspfDbExportIdentifierHigh": tmnxOspfDbExportIdentifierHigh,
       "tmnxOspfBgpLsIdentifierSet": tmnxOspfBgpLsIdentifierSet,
       "tmnxOspfBgpLsIdentifier": tmnxOspfBgpLsIdentifier,
       "tmnxOspfBackupNodeSidPfxType": tmnxOspfBackupNodeSidPfxType,
       "tmnxOspfBackupNodeSidPfx": tmnxOspfBackupNodeSidPfx,
       "tmnxOspfBackupNodeSidPfxLen": tmnxOspfBackupNodeSidPfxLen,
       "tmnxOspfBackupNodeSidType": tmnxOspfBackupNodeSidType,
       "tmnxOspfBackupNodeSidValue": tmnxOspfBackupNodeSidValue,
       "tmnxOspfExtendedLsa": tmnxOspfExtendedLsa,
       "tmnxOspfSrEntropyLabel": tmnxOspfSrEntropyLabel,
       "tmnxOspfTiLfa": tmnxOspfTiLfa,
       "tmnxOspfMaxSrFrrLabels": tmnxOspfMaxSrFrrLabels,
       "tmnxOspfOverrideTunnelElc": tmnxOspfOverrideTunnelElc,
       "tmnxOspfSrMsAdminState": tmnxOspfSrMsAdminState,
       "tmnxOspfSrExportTunnelTableProt": tmnxOspfSrExportTunnelTableProt,
       "tmnxOspfSrlbReservedLblBlockName": tmnxOspfSrlbReservedLblBlockName,
       "tmnxOspfRemoteLfaNodeProtect": tmnxOspfRemoteLfaNodeProtect,
       "tmnxOspfRemoteLfaMaxPqNodes": tmnxOspfRemoteLfaMaxPqNodes,
       "tmnxOspfTiLfaNodeProtect": tmnxOspfTiLfaNodeProtect,
       "tmnxOspfMultiInstance": tmnxOspfMultiInstance,
       "tmnxOspfReferenceBandwidthU64Hi": tmnxOspfReferenceBandwidthU64Hi,
       "tmnxOspfReferenceBandwidthU64Lo": tmnxOspfReferenceBandwidthU64Lo,
       "tmnxOspfEgressStatsNodeSid": tmnxOspfEgressStatsNodeSid,
       "tmnxOspfEgressStatsAdjSid": tmnxOspfEgressStatsAdjSid,
       "tmnxOspfEgressStatsAdjSet": tmnxOspfEgressStatsAdjSet,
       "tmnxOspfIngressStatsNodeSid": tmnxOspfIngressStatsNodeSid,
       "tmnxOspfIngressStatsAdjSid": tmnxOspfIngressStatsAdjSid,
       "tmnxOspfIngressStatsAdjSet": tmnxOspfIngressStatsAdjSet,
       "tmnxOspfOverloadInclExt1": tmnxOspfOverloadInclExt1,
       "tmnxOspfSrClassForwarding": tmnxOspfSrClassForwarding,
       "tmnxOspfTeOptsSrTe": tmnxOspfTeOptsSrTe,
       "tmnxOspfSrPfxTable": tmnxOspfSrPfxTable,
       "tmnxOspfSrPfxEntry": tmnxOspfSrPfxEntry,
       "tmnxOspfSrPfxType": tmnxOspfSrPfxType,
       "tmnxOspfSrPfx": tmnxOspfSrPfx,
       "tmnxOspfSrPfxLen": tmnxOspfSrPfxLen,
       "tmnxOspfSrPfxAreaId": tmnxOspfSrPfxAreaId,
       "tmnxOspfSrPfxSidRtType": tmnxOspfSrPfxSidRtType,
       "tmnxOspfSrPfxSid": tmnxOspfSrPfxSid,
       "tmnxOspfSrPfxAdvtRtrId": tmnxOspfSrPfxAdvtRtrId,
       "tmnxOspfSrPfxSidFlags": tmnxOspfSrPfxSidFlags,
       "tmnxOspfSrPfxSidActive": tmnxOspfSrPfxSidActive,
       "tmnxOspfSrPfxSidSRMS": tmnxOspfSrPfxSidSRMS,
       "tmnxOspfSrPfxSidSRMSSelected": tmnxOspfSrPfxSidSRMSSelected,
       "tmnxOspfSrLfaStatsTable": tmnxOspfSrLfaStatsTable,
       "tmnxOspfSrLfaStatsEntry": tmnxOspfSrLfaStatsEntry,
       "tmnxOspfSrLfaStatsSidType": tmnxOspfSrLfaStatsSidType,
       "tmnxOspfSrLfaStatsTotalSid": tmnxOspfSrLfaStatsTotalSid,
       "tmnxOspfSrLfaStatsLfaCovered": tmnxOspfSrLfaStatsLfaCovered,
       "tmnxOspfSrLfaStatsRLfaCovered": tmnxOspfSrLfaStatsRLfaCovered,
       "tmnxOspfSrLfaStatsTiLfaCovered": tmnxOspfSrLfaStatsTiLfaCovered,
       "tmnxOspfIgpSCTable": tmnxOspfIgpSCTable,
       "tmnxOspfIgpSCEntry": tmnxOspfIgpSCEntry,
       "tmnxOspfIgpSCAdminState": tmnxOspfIgpSCAdminState,
       "tmnxOspfIgpSCTunnNextHopTable": tmnxOspfIgpSCTunnNextHopTable,
       "tmnxOspfIgpSCTunnNextHopEntry": tmnxOspfIgpSCTunnNextHopEntry,
       "tmnxOspfIgpSCTunnNextHopFamily": tmnxOspfIgpSCTunnNextHopFamily,
       "tmnxOspfIgpSCTunnNextHopLstCh": tmnxOspfIgpSCTunnNextHopLstCh,
       "tmnxOspfIgpSCTNHResolution": tmnxOspfIgpSCTNHResolution,
       "tmnxOspfIgpSCTNHResFilterRsvp": tmnxOspfIgpSCTNHResFilterRsvp,
       "tmnxOspfIgpSCTNHResFilterSrTe": tmnxOspfIgpSCTNHResFilterSrTe,
       "tmnxOspfAdjSetTable": tmnxOspfAdjSetTable,
       "tmnxOspfAdjSetEntry": tmnxOspfAdjSetEntry,
       "tmnxOspfAdjSetId": tmnxOspfAdjSetId,
       "tmnxOspfAdjSetRowStatus": tmnxOspfAdjSetRowStatus,
       "tmnxOspfAdjSetLastChanged": tmnxOspfAdjSetLastChanged,
       "tmnxOspfAdjSetSidType": tmnxOspfAdjSetSidType,
       "tmnxOspfAdjSetSidValue": tmnxOspfAdjSetSidValue,
       "tmnxOspfAdjSetParallel": tmnxOspfAdjSetParallel,
       "tmnxOspfAdjSetAdvertise": tmnxOspfAdjSetAdvertise,
       "tmnxOspfAdjSetDynSidValue": tmnxOspfAdjSetDynSidValue,
       "tmnxOspfAdjSetTunlDestType": tmnxOspfAdjSetTunlDestType,
       "tmnxOspfAdjSetTunlDestIp": tmnxOspfAdjSetTunlDestIp,
       "tmnxOspfAdjSetNbrRtrId": tmnxOspfAdjSetNbrRtrId,
       "tmnxOspfAdjSetMembersCount": tmnxOspfAdjSetMembersCount,
       "tmnxOspfAdjSetActiveMembers": tmnxOspfAdjSetActiveMembers,
       "tmnxOspfAdjSetUpTime": tmnxOspfAdjSetUpTime,
       "tmnxOspfAdjSetStatus": tmnxOspfAdjSetStatus,
       "tmnxOspfAdjSetMtu": tmnxOspfAdjSetMtu,
       "tmnxOspfIfAdjSetTable": tmnxOspfIfAdjSetTable,
       "tmnxOspfIfAdjSetEntry": tmnxOspfIfAdjSetEntry,
       "tmnxOspfIfAdjSetId": tmnxOspfIfAdjSetId,
       "tmnxOspfIfAdjSetRowStatus": tmnxOspfIfAdjSetRowStatus,
       "tmnxOspfIfAdjSetLastChanged": tmnxOspfIfAdjSetLastChanged,
       "tmnxOspfAdjSetNhopTable": tmnxOspfAdjSetNhopTable,
       "tmnxOspfAdjSetNhopEntry": tmnxOspfAdjSetNhopEntry,
       "tmnxOspfAdjSetNhopId": tmnxOspfAdjSetNhopId,
       "tmnxOspfAdjSetNhopRtrId": tmnxOspfAdjSetNhopRtrId,
       "tmnxOspfAdjSetNhopIfIndex": tmnxOspfAdjSetNhopIfIndex,
       "tmnxOspfAdjSetNhopType": tmnxOspfAdjSetNhopType,
       "tmnxOspfAdjSetNhop": tmnxOspfAdjSetNhop,
       "tmnxOspfSRMSSidMapTable": tmnxOspfSRMSSidMapTable,
       "tmnxOspfSRMSSidMapEntry": tmnxOspfSRMSSidMapEntry,
       "tmnxOspfSRMSSidMapNodeSidIndex": tmnxOspfSRMSSidMapNodeSidIndex,
       "tmnxOspfSRMSSidMapRowStatus": tmnxOspfSRMSSidMapRowStatus,
       "tmnxOspfSRMSSidMapLastCh": tmnxOspfSRMSSidMapLastCh,
       "tmnxOspfSRMSSidMapPrefixType": tmnxOspfSRMSSidMapPrefixType,
       "tmnxOspfSRMSSidMapPrefix": tmnxOspfSRMSSidMapPrefix,
       "tmnxOspfSRMSSidMapPrefixLength": tmnxOspfSRMSSidMapPrefixLength,
       "tmnxOspfSRMSSidMapNodeSidRange": tmnxOspfSRMSSidMapNodeSidRange,
       "tmnxOspfSRMSSidMapScope": tmnxOspfSRMSSidMapScope,
       "tmnxOspfSRMSSidMapScopeArea": tmnxOspfSRMSSidMapScopeArea,
       "tmnxOspfSidStatsTable": tmnxOspfSidStatsTable,
       "tmnxOspfSidStatsEntry": tmnxOspfSidStatsEntry,
       "tmnxOspfSidStatsSid": tmnxOspfSidStatsSid,
       "tmnxOspfSidStatsSidType": tmnxOspfSidStatsSidType,
       "tmnxOspfSidStatsPrefixType": tmnxOspfSidStatsPrefixType,
       "tmnxOspfSidStatsPrefix": tmnxOspfSidStatsPrefix,
       "tmnxOspfSidStatsPrefixLength": tmnxOspfSidStatsPrefixLength,
       "tmnxOspfSidStatsIfIndex": tmnxOspfSidStatsIfIndex,
       "tmnxOspfSidStatsAdjSet": tmnxOspfSidStatsAdjSet,
       "tmnxOspfSidStatsIngressOperState": tmnxOspfSidStatsIngressOperState,
       "tmnxOspfSidStatsIngressOctets": tmnxOspfSidStatsIngressOctets,
       "tmnxOspfSidStatsIngressPackets": tmnxOspfSidStatsIngressPackets,
       "tmnxOspfSidStatsEgressOperState": tmnxOspfSidStatsEgressOperState,
       "tmnxOspfSidStatsEgressOctets": tmnxOspfSidStatsEgressOctets,
       "tmnxOspfSidStatsEgressPackets": tmnxOspfSidStatsEgressPackets,
       "tmnxOspfHostnameTable": tmnxOspfHostnameTable,
       "tmnxOspfHostnameEntry": tmnxOspfHostnameEntry,
       "tmnxOspfHostnameRtrId": tmnxOspfHostnameRtrId,
       "tmnxOspfHostnameName": tmnxOspfHostnameName,
       "tmnxOspfScalarObjs": tmnxOspfScalarObjs,
       "tmnxOspfScalarDynHostnames": tmnxOspfScalarDynHostnames,
       "tmnxOspfSegmentRoutingTable": tmnxOspfSegmentRoutingTable,
       "tmnxOspfSegmentRoutingEntry": tmnxOspfSegmentRoutingEntry,
       "tmnxOspfSrLastChanged": tmnxOspfSrLastChanged,
       "tmnxOspfSrMsdOverrideBmi": tmnxOspfSrMsdOverrideBmi,
       "tmnxOspfSrMsdOverrideErld": tmnxOspfSrMsdOverrideErld,
       "tmnxOspfNotifyPrefix": tmnxOspfNotifyPrefix,
       "tmnxOspfNotifications": tmnxOspfNotifications,
       "tmnxOspfVirtIfStateChange": tmnxOspfVirtIfStateChange,
       "tmnxOspfNbrStateChange": tmnxOspfNbrStateChange,
       "tmnxOspfVirtNbrStateChange": tmnxOspfVirtNbrStateChange,
       "tmnxOspfIfConfigError": tmnxOspfIfConfigError,
       "tmnxOspfVirtIfConfigError": tmnxOspfVirtIfConfigError,
       "tmnxOspfIfAuthFailure": tmnxOspfIfAuthFailure,
       "tmnxOspfVirtIfAuthFailure": tmnxOspfVirtIfAuthFailure,
       "tmnxOspfIfRxBadPacket": tmnxOspfIfRxBadPacket,
       "tmnxOspfVirtIfRxBadPacket": tmnxOspfVirtIfRxBadPacket,
       "tmnxOspfIfTxRetransmit": tmnxOspfIfTxRetransmit,
       "tmnxOspfVirtIfTxRetransmit": tmnxOspfVirtIfTxRetransmit,
       "tmnxOspfAreaOriginateLsa": tmnxOspfAreaOriginateLsa,
       "tmnxOspfAreaMaxAgeLsa": tmnxOspfAreaMaxAgeLsa,
       "tmnxOspfLsdbOverflow": tmnxOspfLsdbOverflow,
       "tmnxOspfLsdbApproachingOverflow": tmnxOspfLsdbApproachingOverflow,
       "tmnxOspfIfStateChange": tmnxOspfIfStateChange,
       "tmnxOspfNssaTranslatorStatusChg": tmnxOspfNssaTranslatorStatusChg,
       "tmnxOspfRestartStatusChange": tmnxOspfRestartStatusChange,
       "tmnxOspfNbrRestartHlprStsChg": tmnxOspfNbrRestartHlprStsChg,
       "tmnxOspfVirtNbrRestartHlprStsChg": tmnxOspfVirtNbrRestartHlprStsChg,
       "tmnxOspfSpfRunsStopped": tmnxOspfSpfRunsStopped,
       "tmnxOspfSpfRunsRestarted": tmnxOspfSpfRunsRestarted,
       "tmnxOspfOverloadEntered": tmnxOspfOverloadEntered,
       "tmnxOspfOverloadExited": tmnxOspfOverloadExited,
       "tmnxOspfAsOriginateLsa": tmnxOspfAsOriginateLsa,
       "tmnxOspfAsMaxAgeLsa": tmnxOspfAsMaxAgeLsa,
       "tmnxOspfLinkOriginateLsa": tmnxOspfLinkOriginateLsa,
       "tmnxOspfLinkMaxAgeLsa": tmnxOspfLinkMaxAgeLsa,
       "tmnxOspfLdpSyncTimerStarted": tmnxOspfLdpSyncTimerStarted,
       "tmnxOspfLdpSyncExit": tmnxOspfLdpSyncExit,
       "tmnxOspfShamIfStateChange": tmnxOspfShamIfStateChange,
       "tmnxOspfShamNbrStateChange": tmnxOspfShamNbrStateChange,
       "tmnxOspfShamIfConfigError": tmnxOspfShamIfConfigError,
       "tmnxOspfShamIfAuthFailure": tmnxOspfShamIfAuthFailure,
       "tmnxOspfShamIfRxBadPacket": tmnxOspfShamIfRxBadPacket,
       "tmnxOspfShamIfTxRetransmit": tmnxOspfShamIfTxRetransmit,
       "tmnxOspfShamNbrRestartHlprStsChg": tmnxOspfShamNbrRestartHlprStsChg,
       "tmnxOspfFailureDisabled": tmnxOspfFailureDisabled,
       "tmnxOspfExportLimitReached": tmnxOspfExportLimitReached,
       "tmnxOspfExportLimitWarning": tmnxOspfExportLimitWarning,
       "tmnxOspfRoutesExpLmtDropped": tmnxOspfRoutesExpLmtDropped,
       "tmnxOspfNgNbrStateChange": tmnxOspfNgNbrStateChange,
       "tmnxOspfNgIfConfigError": tmnxOspfNgIfConfigError,
       "tmnxOspfNgIfAuthFailure": tmnxOspfNgIfAuthFailure,
       "tmnxOspfNgIfRxBadPacket": tmnxOspfNgIfRxBadPacket,
       "tmnxOspfNgIfTxRetransmit": tmnxOspfNgIfTxRetransmit,
       "tmnxOspfNgIfStateChange": tmnxOspfNgIfStateChange,
       "tmnxOspfNgNbrRestartHlprStsChg": tmnxOspfNgNbrRestartHlprStsChg,
       "tmnxOspfNgLinkOriginateLsa": tmnxOspfNgLinkOriginateLsa,
       "tmnxOspfNgLinkMaxAgeLsa": tmnxOspfNgLinkMaxAgeLsa,
       "tmnxOspfNgLdpSyncTimerStarted": tmnxOspfNgLdpSyncTimerStarted,
       "tmnxOspfNgLdpSyncExit": tmnxOspfNgLdpSyncExit,
       "tmnxOspfSrSidError": tmnxOspfSrSidError,
       "tmnxOspfSrSidNotInLabelRange": tmnxOspfSrSidNotInLabelRange,
       "tmnxOspfOverloadWarning": tmnxOspfOverloadWarning,
       "tmnxOspfRejectedAdjacencySid": tmnxOspfRejectedAdjacencySid,
       "tmnxOspfAdjBfdSessionSetupFail": tmnxOspfAdjBfdSessionSetupFail,
       "tmnxOspfSrgbBadLabelRange": tmnxOspfSrgbBadLabelRange,
       "tmnxOspfRejectedAdjacencySet": tmnxOspfRejectedAdjacencySet,
       "tmnxOspfSidStatsIndexAlloc": tmnxOspfSidStatsIndexAlloc,
       "tmnxOspfDynHostnameDuplicate": tmnxOspfDynHostnameDuplicate,
       "tmnxOspfDynHostnameInconsistent": tmnxOspfDynHostnameInconsistent}
)
