# SNMP MIB module (TIMETRA-PCEP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-PCEP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:02:57 2025
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
 TNamedItem,
 TmnxAdminState,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TmnxAdminState",
    "TmnxOperState")

(vRtrID,) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID")


# MODULE-IDENTITY

timetraPcepMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 101)
)
if mibBuilder.loadTexts:
    timetraPcepMIBModule.setRevisions(
        ("2016-01-01 00:00",
         "2015-01-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxPcepCapabilities(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("statefulDelegate", 0),
          ("statefulPce", 1),
          ("statefulOptimize", 2),
          ("segmentRtPath", 3),
          ("rsvpPath", 4),
          ("opticsGmpls", 5),
          ("pceInitiatedLsp", 6),
          ("stateless", 7),
          ("p2mp", 8),
          ("p2mp-delegate", 9),
          ("p2mp-initiate", 10),
          ("association", 11),
          ("multipath", 12))
    )


class TmnxPcepLspType(TextualConvention, Integer32):
    status = "current"
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
        *(("rsvpP2p", 1),
          ("rsvpP2mp", 2),
          ("segRt", 3),
          ("pceInitSegRt", 4))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxPcepConformance_ObjectIdentity = ObjectIdentity
tmnxPcepConformance = _TmnxPcepConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 101)
)
_TmnxPcepCompliances_ObjectIdentity = ObjectIdentity
tmnxPcepCompliances = _TmnxPcepCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 101, 1)
)
_TmnxPcepGroups_ObjectIdentity = ObjectIdentity
tmnxPcepGroups = _TmnxPcepGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 101, 2)
)
_TmnxPcepObjects_ObjectIdentity = ObjectIdentity
tmnxPcepObjects = _TmnxPcepObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101)
)
_TmnxPcepTableChangedObjects_ObjectIdentity = ObjectIdentity
tmnxPcepTableChangedObjects = _TmnxPcepTableChangedObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 1)
)
_TmnxPcepEntityTableLastChanged_Type = TimeStamp
_TmnxPcepEntityTableLastChanged_Object = MibScalar
tmnxPcepEntityTableLastChanged = _TmnxPcepEntityTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 1, 1),
    _TmnxPcepEntityTableLastChanged_Type()
)
tmnxPcepEntityTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepEntityTableLastChanged.setStatus("current")
_TmnxPcepPccEntityTblLastChgd_Type = TimeStamp
_TmnxPcepPccEntityTblLastChgd_Object = MibScalar
tmnxPcepPccEntityTblLastChgd = _TmnxPcepPccEntityTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 1, 2),
    _TmnxPcepPccEntityTblLastChgd_Type()
)
tmnxPcepPccEntityTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccEntityTblLastChgd.setStatus("current")
_TmnxPcepPccPeerTableLastChanged_Type = TimeStamp
_TmnxPcepPccPeerTableLastChanged_Object = MibScalar
tmnxPcepPccPeerTableLastChanged = _TmnxPcepPccPeerTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 1, 3),
    _TmnxPcepPccPeerTableLastChanged_Type()
)
tmnxPcepPccPeerTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccPeerTableLastChanged.setStatus("current")
_TmnxPcepConfigObjects_ObjectIdentity = ObjectIdentity
tmnxPcepConfigObjects = _TmnxPcepConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2)
)
_TmnxPcepPccConfigObjects_ObjectIdentity = ObjectIdentity
tmnxPcepPccConfigObjects = _TmnxPcepPccConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 1)
)
_TmnxPcepPccEntityTable_Object = MibTable
tmnxPcepPccEntityTable = _TmnxPcepPccEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxPcepPccEntityTable.setStatus("current")
_TmnxPcepPccEntityEntry_Object = MibTableRow
tmnxPcepPccEntityEntry = _TmnxPcepPccEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 1, 1, 1)
)
tmnxPcepPccEntityEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepEntityIndex"),
)
if mibBuilder.loadTexts:
    tmnxPcepPccEntityEntry.setStatus("current")
_TmnxPcepPccEntityLastChanged_Type = TimeStamp
_TmnxPcepPccEntityLastChanged_Object = MibTableColumn
tmnxPcepPccEntityLastChanged = _TmnxPcepPccEntityLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 1, 1, 1, 1),
    _TmnxPcepPccEntityLastChanged_Type()
)
tmnxPcepPccEntityLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccEntityLastChanged.setStatus("current")


class _TmnxPcepPccEntityAddrType_Type(InetAddressType):
    """Custom type tmnxPcepPccEntityAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxPcepPccEntityAddrType_Type.__name__ = "InetAddressType"
_TmnxPcepPccEntityAddrType_Object = MibTableColumn
tmnxPcepPccEntityAddrType = _TmnxPcepPccEntityAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 1, 1, 1, 2),
    _TmnxPcepPccEntityAddrType_Type()
)
tmnxPcepPccEntityAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccEntityAddrType.setStatus("current")


class _TmnxPcepPccEntityAddr_Type(InetAddress):
    """Custom type tmnxPcepPccEntityAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepPccEntityAddr_Type.__name__ = "InetAddress"
_TmnxPcepPccEntityAddr_Object = MibTableColumn
tmnxPcepPccEntityAddr = _TmnxPcepPccEntityAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 1, 1, 1, 3),
    _TmnxPcepPccEntityAddr_Type()
)
tmnxPcepPccEntityAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccEntityAddr.setStatus("current")


class _TmnxPcepPccEntityReportPathConst_Type(TruthValue):
    """Custom type tmnxPcepPccEntityReportPathConst based on TruthValue"""
    defaultValue = 1


_TmnxPcepPccEntityReportPathConst_Type.__name__ = "TruthValue"
_TmnxPcepPccEntityReportPathConst_Object = MibTableColumn
tmnxPcepPccEntityReportPathConst = _TmnxPcepPccEntityReportPathConst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 1, 1, 1, 4),
    _TmnxPcepPccEntityReportPathConst_Type()
)
tmnxPcepPccEntityReportPathConst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcepPccEntityReportPathConst.setStatus("current")


class _TmnxPcepPccRedelegationTimer_Type(Unsigned32):
    """Custom type tmnxPcepPccRedelegationTimer based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TmnxPcepPccRedelegationTimer_Type.__name__ = "Unsigned32"
_TmnxPcepPccRedelegationTimer_Object = MibTableColumn
tmnxPcepPccRedelegationTimer = _TmnxPcepPccRedelegationTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 1, 1, 1, 5),
    _TmnxPcepPccRedelegationTimer_Type()
)
tmnxPcepPccRedelegationTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcepPccRedelegationTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPcepPccRedelegationTimer.setUnits("seconds")


class _TmnxPcepPccStateTimer_Type(Unsigned32):
    """Custom type tmnxPcepPccStateTimer based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TmnxPcepPccStateTimer_Type.__name__ = "Unsigned32"
_TmnxPcepPccStateTimer_Object = MibTableColumn
tmnxPcepPccStateTimer = _TmnxPcepPccStateTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 1, 1, 1, 6),
    _TmnxPcepPccStateTimer_Type()
)
tmnxPcepPccStateTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcepPccStateTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPcepPccStateTimer.setUnits("seconds")


class _TmnxPcepPccStateTimerAction_Type(Integer32):
    """Custom type tmnxPcepPccStateTimerAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("remove", 1))
    )


_TmnxPcepPccStateTimerAction_Type.__name__ = "Integer32"
_TmnxPcepPccStateTimerAction_Object = MibTableColumn
tmnxPcepPccStateTimerAction = _TmnxPcepPccStateTimerAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 1, 1, 1, 7),
    _TmnxPcepPccStateTimerAction_Type()
)
tmnxPcepPccStateTimerAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcepPccStateTimerAction.setStatus("current")


class _TmnxPcepPccMaxSrtePceInitLsps_Type(Unsigned32):
    """Custom type tmnxPcepPccMaxSrtePceInitLsps based on Unsigned32"""
    defaultValue = 8191

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_TmnxPcepPccMaxSrtePceInitLsps_Type.__name__ = "Unsigned32"
_TmnxPcepPccMaxSrtePceInitLsps_Object = MibTableColumn
tmnxPcepPccMaxSrtePceInitLsps = _TmnxPcepPccMaxSrtePceInitLsps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 1, 1, 1, 8),
    _TmnxPcepPccMaxSrtePceInitLsps_Type()
)
tmnxPcepPccMaxSrtePceInitLsps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcepPccMaxSrtePceInitLsps.setStatus("current")


class _TmnxPcepPccEntityAddrIpv6Type_Type(InetAddressType):
    """Custom type tmnxPcepPccEntityAddrIpv6Type based on InetAddressType"""
    defaultValue = 0


_TmnxPcepPccEntityAddrIpv6Type_Type.__name__ = "InetAddressType"
_TmnxPcepPccEntityAddrIpv6Type_Object = MibTableColumn
tmnxPcepPccEntityAddrIpv6Type = _TmnxPcepPccEntityAddrIpv6Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 1, 1, 1, 9),
    _TmnxPcepPccEntityAddrIpv6Type_Type()
)
tmnxPcepPccEntityAddrIpv6Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccEntityAddrIpv6Type.setStatus("current")


class _TmnxPcepPccEntityAddrIpv6_Type(InetAddress):
    """Custom type tmnxPcepPccEntityAddrIpv6 based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepPccEntityAddrIpv6_Type.__name__ = "InetAddress"
_TmnxPcepPccEntityAddrIpv6_Object = MibTableColumn
tmnxPcepPccEntityAddrIpv6 = _TmnxPcepPccEntityAddrIpv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 1, 1, 1, 10),
    _TmnxPcepPccEntityAddrIpv6_Type()
)
tmnxPcepPccEntityAddrIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccEntityAddrIpv6.setStatus("current")
_TmnxPcepPceConfigObjects_ObjectIdentity = ObjectIdentity
tmnxPcepPceConfigObjects = _TmnxPcepPceConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 2)
)
_TmnxPcepEntityTable_Object = MibTable
tmnxPcepEntityTable = _TmnxPcepEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxPcepEntityTable.setStatus("current")
_TmnxPcepEntityEntry_Object = MibTableRow
tmnxPcepEntityEntry = _TmnxPcepEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 3, 1)
)
tmnxPcepEntityEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepEntityIndex"),
)
if mibBuilder.loadTexts:
    tmnxPcepEntityEntry.setStatus("current")


class _TmnxPcepEntityIndex_Type(Unsigned32):
    """Custom type tmnxPcepEntityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TmnxPcepEntityIndex_Type.__name__ = "Unsigned32"
_TmnxPcepEntityIndex_Object = MibTableColumn
tmnxPcepEntityIndex = _TmnxPcepEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 3, 1, 1),
    _TmnxPcepEntityIndex_Type()
)
tmnxPcepEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPcepEntityIndex.setStatus("current")
_TmnxPcepEntityRowStatus_Type = RowStatus
_TmnxPcepEntityRowStatus_Object = MibTableColumn
tmnxPcepEntityRowStatus = _TmnxPcepEntityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 3, 1, 2),
    _TmnxPcepEntityRowStatus_Type()
)
tmnxPcepEntityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcepEntityRowStatus.setStatus("current")
_TmnxPcepEntityLastChanged_Type = TimeStamp
_TmnxPcepEntityLastChanged_Object = MibTableColumn
tmnxPcepEntityLastChanged = _TmnxPcepEntityLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 3, 1, 3),
    _TmnxPcepEntityLastChanged_Type()
)
tmnxPcepEntityLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepEntityLastChanged.setStatus("current")


class _TmnxPcepEntityType_Type(Integer32):
    """Custom type tmnxPcepEntityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pcc", 1),
          ("pce", 2))
    )


_TmnxPcepEntityType_Type.__name__ = "Integer32"
_TmnxPcepEntityType_Object = MibTableColumn
tmnxPcepEntityType = _TmnxPcepEntityType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 3, 1, 4),
    _TmnxPcepEntityType_Type()
)
tmnxPcepEntityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcepEntityType.setStatus("current")


class _TmnxPcepEntityAdminState_Type(TmnxAdminState):
    """Custom type tmnxPcepEntityAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxPcepEntityAdminState_Type.__name__ = "TmnxAdminState"
_TmnxPcepEntityAdminState_Object = MibTableColumn
tmnxPcepEntityAdminState = _TmnxPcepEntityAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 3, 1, 5),
    _TmnxPcepEntityAdminState_Type()
)
tmnxPcepEntityAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcepEntityAdminState.setStatus("current")


class _TmnxPcepEntityLocalAddrType_Type(InetAddressType):
    """Custom type tmnxPcepEntityLocalAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxPcepEntityLocalAddrType_Type.__name__ = "InetAddressType"
_TmnxPcepEntityLocalAddrType_Object = MibTableColumn
tmnxPcepEntityLocalAddrType = _TmnxPcepEntityLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 3, 1, 6),
    _TmnxPcepEntityLocalAddrType_Type()
)
tmnxPcepEntityLocalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcepEntityLocalAddrType.setStatus("current")


class _TmnxPcepEntityLocalAddr_Type(InetAddress):
    """Custom type tmnxPcepEntityLocalAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepEntityLocalAddr_Type.__name__ = "InetAddress"
_TmnxPcepEntityLocalAddr_Object = MibTableColumn
tmnxPcepEntityLocalAddr = _TmnxPcepEntityLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 3, 1, 7),
    _TmnxPcepEntityLocalAddr_Type()
)
tmnxPcepEntityLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcepEntityLocalAddr.setStatus("current")


class _TmnxPcepEntityKeepAliveInterval_Type(Unsigned32):
    """Custom type tmnxPcepEntityKeepAliveInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxPcepEntityKeepAliveInterval_Type.__name__ = "Unsigned32"
_TmnxPcepEntityKeepAliveInterval_Object = MibTableColumn
tmnxPcepEntityKeepAliveInterval = _TmnxPcepEntityKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 3, 1, 8),
    _TmnxPcepEntityKeepAliveInterval_Type()
)
tmnxPcepEntityKeepAliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcepEntityKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPcepEntityKeepAliveInterval.setUnits("seconds")


class _TmnxPcepEntityDeadTimer_Type(Unsigned32):
    """Custom type tmnxPcepEntityDeadTimer based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxPcepEntityDeadTimer_Type.__name__ = "Unsigned32"
_TmnxPcepEntityDeadTimer_Object = MibTableColumn
tmnxPcepEntityDeadTimer = _TmnxPcepEntityDeadTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 3, 1, 9),
    _TmnxPcepEntityDeadTimer_Type()
)
tmnxPcepEntityDeadTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcepEntityDeadTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPcepEntityDeadTimer.setUnits("seconds")


class _TmnxPcepEntityMaxUnknownMsgs_Type(Unsigned32):
    """Custom type tmnxPcepEntityMaxUnknownMsgs based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxPcepEntityMaxUnknownMsgs_Type.__name__ = "Unsigned32"
_TmnxPcepEntityMaxUnknownMsgs_Object = MibTableColumn
tmnxPcepEntityMaxUnknownMsgs = _TmnxPcepEntityMaxUnknownMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 3, 1, 10),
    _TmnxPcepEntityMaxUnknownMsgs_Type()
)
tmnxPcepEntityMaxUnknownMsgs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcepEntityMaxUnknownMsgs.setStatus("current")
_TmnxPcepEntityCapability_Type = TmnxPcepCapabilities
_TmnxPcepEntityCapability_Object = MibTableColumn
tmnxPcepEntityCapability = _TmnxPcepEntityCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 3, 1, 11),
    _TmnxPcepEntityCapability_Type()
)
tmnxPcepEntityCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepEntityCapability.setStatus("current")
_TmnxPcepEntityIsOverloaded_Type = TruthValue
_TmnxPcepEntityIsOverloaded_Object = MibTableColumn
tmnxPcepEntityIsOverloaded = _TmnxPcepEntityIsOverloaded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 3, 1, 12),
    _TmnxPcepEntityIsOverloaded_Type()
)
tmnxPcepEntityIsOverloaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepEntityIsOverloaded.setStatus("current")


class _TmnxPcepEntityLocalAddrIpv6Type_Type(InetAddressType):
    """Custom type tmnxPcepEntityLocalAddrIpv6Type based on InetAddressType"""
    defaultValue = 0


_TmnxPcepEntityLocalAddrIpv6Type_Type.__name__ = "InetAddressType"
_TmnxPcepEntityLocalAddrIpv6Type_Object = MibTableColumn
tmnxPcepEntityLocalAddrIpv6Type = _TmnxPcepEntityLocalAddrIpv6Type_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 3, 1, 13),
    _TmnxPcepEntityLocalAddrIpv6Type_Type()
)
tmnxPcepEntityLocalAddrIpv6Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcepEntityLocalAddrIpv6Type.setStatus("current")


class _TmnxPcepEntityLocalAddrIpv6_Type(InetAddress):
    """Custom type tmnxPcepEntityLocalAddrIpv6 based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepEntityLocalAddrIpv6_Type.__name__ = "InetAddress"
_TmnxPcepEntityLocalAddrIpv6_Object = MibTableColumn
tmnxPcepEntityLocalAddrIpv6 = _TmnxPcepEntityLocalAddrIpv6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 3, 1, 14),
    _TmnxPcepEntityLocalAddrIpv6_Type()
)
tmnxPcepEntityLocalAddrIpv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcepEntityLocalAddrIpv6.setStatus("current")
_TmnxPcepPccPeerTable_Object = MibTable
tmnxPcepPccPeerTable = _TmnxPcepPccPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxPcepPccPeerTable.setStatus("current")
_TmnxPcepPccPeerEntry_Object = MibTableRow
tmnxPcepPccPeerEntry = _TmnxPcepPccPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 4, 1)
)
tmnxPcepPccPeerEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepEntityIndex"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepPccPeerAddrType"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepPccPeerAddr"),
)
if mibBuilder.loadTexts:
    tmnxPcepPccPeerEntry.setStatus("current")
_TmnxPcepPccPeerAddrType_Type = InetAddressType
_TmnxPcepPccPeerAddrType_Object = MibTableColumn
tmnxPcepPccPeerAddrType = _TmnxPcepPccPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 4, 1, 1),
    _TmnxPcepPccPeerAddrType_Type()
)
tmnxPcepPccPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPcepPccPeerAddrType.setStatus("current")


class _TmnxPcepPccPeerAddr_Type(InetAddress):
    """Custom type tmnxPcepPccPeerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepPccPeerAddr_Type.__name__ = "InetAddress"
_TmnxPcepPccPeerAddr_Object = MibTableColumn
tmnxPcepPccPeerAddr = _TmnxPcepPccPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 4, 1, 2),
    _TmnxPcepPccPeerAddr_Type()
)
tmnxPcepPccPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPcepPccPeerAddr.setStatus("current")
_TmnxPcepPccPeerRowStatus_Type = RowStatus
_TmnxPcepPccPeerRowStatus_Object = MibTableColumn
tmnxPcepPccPeerRowStatus = _TmnxPcepPccPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 4, 1, 3),
    _TmnxPcepPccPeerRowStatus_Type()
)
tmnxPcepPccPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcepPccPeerRowStatus.setStatus("current")
_TmnxPcepPccPeerLastChanged_Type = TimeStamp
_TmnxPcepPccPeerLastChanged_Object = MibTableColumn
tmnxPcepPccPeerLastChanged = _TmnxPcepPccPeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 4, 1, 4),
    _TmnxPcepPccPeerLastChanged_Type()
)
tmnxPcepPccPeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccPeerLastChanged.setStatus("current")


class _TmnxPcepPccPeerAdminState_Type(TmnxAdminState):
    """Custom type tmnxPcepPccPeerAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxPcepPccPeerAdminState_Type.__name__ = "TmnxAdminState"
_TmnxPcepPccPeerAdminState_Object = MibTableColumn
tmnxPcepPccPeerAdminState = _TmnxPcepPccPeerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 4, 1, 5),
    _TmnxPcepPccPeerAdminState_Type()
)
tmnxPcepPccPeerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcepPccPeerAdminState.setStatus("current")
_TmnxPcepPccPeerOperState_Type = TmnxOperState
_TmnxPcepPccPeerOperState_Object = MibTableColumn
tmnxPcepPccPeerOperState = _TmnxPcepPccPeerOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 4, 1, 6),
    _TmnxPcepPccPeerOperState_Type()
)
tmnxPcepPccPeerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccPeerOperState.setStatus("current")


class _TmnxPcepPccPeerSpeakerId_Type(OctetString):
    """Custom type tmnxPcepPccPeerSpeakerId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmnxPcepPccPeerSpeakerId_Type.__name__ = "OctetString"
_TmnxPcepPccPeerSpeakerId_Object = MibTableColumn
tmnxPcepPccPeerSpeakerId = _TmnxPcepPccPeerSpeakerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 4, 1, 7),
    _TmnxPcepPccPeerSpeakerId_Type()
)
tmnxPcepPccPeerSpeakerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccPeerSpeakerId.setStatus("current")
_TmnxPcepPccPeerCapability_Type = TmnxPcepCapabilities
_TmnxPcepPccPeerCapability_Object = MibTableColumn
tmnxPcepPccPeerCapability = _TmnxPcepPccPeerCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 4, 1, 8),
    _TmnxPcepPccPeerCapability_Type()
)
tmnxPcepPccPeerCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccPeerCapability.setStatus("current")


class _TmnxPcepPccPeerSyncState_Type(Integer32):
    """Custom type tmnxPcepPccPeerSyncState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInitialized", 0),
          ("inProgress", 1),
          ("done", 2))
    )


_TmnxPcepPccPeerSyncState_Type.__name__ = "Integer32"
_TmnxPcepPccPeerSyncState_Object = MibTableColumn
tmnxPcepPccPeerSyncState = _TmnxPcepPccPeerSyncState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 4, 1, 9),
    _TmnxPcepPccPeerSyncState_Type()
)
tmnxPcepPccPeerSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccPeerSyncState.setStatus("current")
_TmnxPcepPccPeerIsOverloaded_Type = TruthValue
_TmnxPcepPccPeerIsOverloaded_Object = MibTableColumn
tmnxPcepPccPeerIsOverloaded = _TmnxPcepPccPeerIsOverloaded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 4, 1, 10),
    _TmnxPcepPccPeerIsOverloaded_Type()
)
tmnxPcepPccPeerIsOverloaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccPeerIsOverloaded.setStatus("current")
_TmnxPcepPccPeerSessEstablishTime_Type = TimeStamp
_TmnxPcepPccPeerSessEstablishTime_Object = MibTableColumn
tmnxPcepPccPeerSessEstablishTime = _TmnxPcepPccPeerSessEstablishTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 4, 1, 11),
    _TmnxPcepPccPeerSessEstablishTime_Type()
)
tmnxPcepPccPeerSessEstablishTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccPeerSessEstablishTime.setStatus("current")
_TmnxPcepPccPeerOperKeepAlive_Type = Unsigned32
_TmnxPcepPccPeerOperKeepAlive_Object = MibTableColumn
tmnxPcepPccPeerOperKeepAlive = _TmnxPcepPccPeerOperKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 4, 1, 12),
    _TmnxPcepPccPeerOperKeepAlive_Type()
)
tmnxPcepPccPeerOperKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccPeerOperKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPcepPccPeerOperKeepAlive.setUnits("seconds")
_TmnxPcepPccPeerOperDeadTimer_Type = Unsigned32
_TmnxPcepPccPeerOperDeadTimer_Object = MibTableColumn
tmnxPcepPccPeerOperDeadTimer = _TmnxPcepPccPeerOperDeadTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 4, 1, 13),
    _TmnxPcepPccPeerOperDeadTimer_Type()
)
tmnxPcepPccPeerOperDeadTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccPeerOperDeadTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPcepPccPeerOperDeadTimer.setUnits("seconds")


class _TmnxPcepPccPeerPreference_Type(Unsigned32):
    """Custom type tmnxPcepPccPeerPreference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxPcepPccPeerPreference_Type.__name__ = "Unsigned32"
_TmnxPcepPccPeerPreference_Object = MibTableColumn
tmnxPcepPccPeerPreference = _TmnxPcepPccPeerPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 4, 1, 14),
    _TmnxPcepPccPeerPreference_Type()
)
tmnxPcepPccPeerPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPcepPccPeerPreference.setStatus("current")
_TmnxPcepPcePeerTable_Object = MibTable
tmnxPcepPcePeerTable = _TmnxPcepPcePeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 5)
)
if mibBuilder.loadTexts:
    tmnxPcepPcePeerTable.setStatus("current")
_TmnxPcepPcePeerEntry_Object = MibTableRow
tmnxPcepPcePeerEntry = _TmnxPcepPcePeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 5, 1)
)
tmnxPcepPcePeerEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepEntityIndex"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepPcePeerAddrType"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepPcePeerAddr"),
)
if mibBuilder.loadTexts:
    tmnxPcepPcePeerEntry.setStatus("current")
_TmnxPcepPcePeerAddrType_Type = InetAddressType
_TmnxPcepPcePeerAddrType_Object = MibTableColumn
tmnxPcepPcePeerAddrType = _TmnxPcepPcePeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 5, 1, 1),
    _TmnxPcepPcePeerAddrType_Type()
)
tmnxPcepPcePeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPcepPcePeerAddrType.setStatus("current")


class _TmnxPcepPcePeerAddr_Type(InetAddress):
    """Custom type tmnxPcepPcePeerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepPcePeerAddr_Type.__name__ = "InetAddress"
_TmnxPcepPcePeerAddr_Object = MibTableColumn
tmnxPcepPcePeerAddr = _TmnxPcepPcePeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 5, 1, 2),
    _TmnxPcepPcePeerAddr_Type()
)
tmnxPcepPcePeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPcepPcePeerAddr.setStatus("current")
_TmnxPcepPcePeerPort_Type = InetPortNumber
_TmnxPcepPcePeerPort_Object = MibTableColumn
tmnxPcepPcePeerPort = _TmnxPcepPcePeerPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 5, 1, 3),
    _TmnxPcepPcePeerPort_Type()
)
tmnxPcepPcePeerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPcePeerPort.setStatus("current")
_TmnxPcepPcePeerCapability_Type = TmnxPcepCapabilities
_TmnxPcepPcePeerCapability_Object = MibTableColumn
tmnxPcepPcePeerCapability = _TmnxPcepPcePeerCapability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 5, 1, 4),
    _TmnxPcepPcePeerCapability_Type()
)
tmnxPcepPcePeerCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPcePeerCapability.setStatus("current")


class _TmnxPcepPcePeerSyncState_Type(Integer32):
    """Custom type tmnxPcepPcePeerSyncState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInitialized", 0),
          ("inProgress", 1),
          ("done", 2))
    )


_TmnxPcepPcePeerSyncState_Type.__name__ = "Integer32"
_TmnxPcepPcePeerSyncState_Object = MibTableColumn
tmnxPcepPcePeerSyncState = _TmnxPcepPcePeerSyncState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 5, 1, 5),
    _TmnxPcepPcePeerSyncState_Type()
)
tmnxPcepPcePeerSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPcePeerSyncState.setStatus("current")


class _TmnxPcepPcePeerSpeakerId_Type(OctetString):
    """Custom type tmnxPcepPcePeerSpeakerId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TmnxPcepPcePeerSpeakerId_Type.__name__ = "OctetString"
_TmnxPcepPcePeerSpeakerId_Object = MibTableColumn
tmnxPcepPcePeerSpeakerId = _TmnxPcepPcePeerSpeakerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 5, 1, 6),
    _TmnxPcepPcePeerSpeakerId_Type()
)
tmnxPcepPcePeerSpeakerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPcePeerSpeakerId.setStatus("current")
_TmnxPcepPcePeerSessEstablishTime_Type = TimeStamp
_TmnxPcepPcePeerSessEstablishTime_Object = MibTableColumn
tmnxPcepPcePeerSessEstablishTime = _TmnxPcepPcePeerSessEstablishTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 5, 1, 7),
    _TmnxPcepPcePeerSessEstablishTime_Type()
)
tmnxPcepPcePeerSessEstablishTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPcePeerSessEstablishTime.setStatus("current")
_TmnxPcepPcePeerOperKeepAlive_Type = Unsigned32
_TmnxPcepPcePeerOperKeepAlive_Object = MibTableColumn
tmnxPcepPcePeerOperKeepAlive = _TmnxPcepPcePeerOperKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 5, 1, 8),
    _TmnxPcepPcePeerOperKeepAlive_Type()
)
tmnxPcepPcePeerOperKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPcePeerOperKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPcepPcePeerOperKeepAlive.setUnits("seconds")
_TmnxPcepPcePeerOperDeadTimer_Type = Unsigned32
_TmnxPcepPcePeerOperDeadTimer_Object = MibTableColumn
tmnxPcepPcePeerOperDeadTimer = _TmnxPcepPcePeerOperDeadTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 5, 1, 9),
    _TmnxPcepPcePeerOperDeadTimer_Type()
)
tmnxPcepPcePeerOperDeadTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPcePeerOperDeadTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPcepPcePeerOperDeadTimer.setUnits("seconds")
_TmnxPcepPccP2mpSrTreeTable_Object = MibTable
tmnxPcepPccP2mpSrTreeTable = _TmnxPcepPccP2mpSrTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 6)
)
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTreeTable.setStatus("current")
_TmnxPcepPccP2mpSrTreeEntry_Object = MibTableRow
tmnxPcepPccP2mpSrTreeEntry = _TmnxPcepPccP2mpSrTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 6, 1)
)
tmnxPcepPccP2mpSrTreeEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepEntityIndex"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdPLspId"),
)
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTreeEntry.setStatus("current")
_TmnxPcepPccP2mpSrTreeAssocId_Type = Unsigned32
_TmnxPcepPccP2mpSrTreeAssocId_Object = MibTableColumn
tmnxPcepPccP2mpSrTreeAssocId = _TmnxPcepPccP2mpSrTreeAssocId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 6, 1, 1),
    _TmnxPcepPccP2mpSrTreeAssocId_Type()
)
tmnxPcepPccP2mpSrTreeAssocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTreeAssocId.setStatus("current")


class _TmnxPcepPccP2mpSrTreeAssocType_Type(Integer32):
    """Custom type tmnxPcepPccP2mpSrTreeAssocType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pcepAssociationTypeP2mpSr", 0),
          ("pcepMaxAssociationType", 1))
    )


_TmnxPcepPccP2mpSrTreeAssocType_Type.__name__ = "Integer32"
_TmnxPcepPccP2mpSrTreeAssocType_Object = MibTableColumn
tmnxPcepPccP2mpSrTreeAssocType = _TmnxPcepPccP2mpSrTreeAssocType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 6, 1, 2),
    _TmnxPcepPccP2mpSrTreeAssocType_Type()
)
tmnxPcepPccP2mpSrTreeAssocType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTreeAssocType.setStatus("current")
_TmnxPcepPccP2mpSrTrAsSrcAddrType_Type = InetAddressType
_TmnxPcepPccP2mpSrTrAsSrcAddrType_Object = MibTableColumn
tmnxPcepPccP2mpSrTrAsSrcAddrType = _TmnxPcepPccP2mpSrTrAsSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 6, 1, 3),
    _TmnxPcepPccP2mpSrTrAsSrcAddrType_Type()
)
tmnxPcepPccP2mpSrTrAsSrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTrAsSrcAddrType.setStatus("current")


class _TmnxPcepPccP2mpSrTrAsSrcAddr_Type(InetAddress):
    """Custom type tmnxPcepPccP2mpSrTrAsSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxPcepPccP2mpSrTrAsSrcAddr_Type.__name__ = "InetAddress"
_TmnxPcepPccP2mpSrTrAsSrcAddr_Object = MibTableColumn
tmnxPcepPccP2mpSrTrAsSrcAddr = _TmnxPcepPccP2mpSrTrAsSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 6, 1, 4),
    _TmnxPcepPccP2mpSrTrAsSrcAddr_Type()
)
tmnxPcepPccP2mpSrTrAsSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTrAsSrcAddr.setStatus("current")
_TmnxPcepPccP2mpSrTrOrgNdAddrType_Type = InetAddressType
_TmnxPcepPccP2mpSrTrOrgNdAddrType_Object = MibTableColumn
tmnxPcepPccP2mpSrTrOrgNdAddrType = _TmnxPcepPccP2mpSrTrOrgNdAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 6, 1, 5),
    _TmnxPcepPccP2mpSrTrOrgNdAddrType_Type()
)
tmnxPcepPccP2mpSrTrOrgNdAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTrOrgNdAddrType.setStatus("current")


class _TmnxPcepPccP2mpSrTrCPOrgNdAddr_Type(InetAddress):
    """Custom type tmnxPcepPccP2mpSrTrCPOrgNdAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxPcepPccP2mpSrTrCPOrgNdAddr_Type.__name__ = "InetAddress"
_TmnxPcepPccP2mpSrTrCPOrgNdAddr_Object = MibTableColumn
tmnxPcepPccP2mpSrTrCPOrgNdAddr = _TmnxPcepPccP2mpSrTrCPOrgNdAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 6, 1, 6),
    _TmnxPcepPccP2mpSrTrCPOrgNdAddr_Type()
)
tmnxPcepPccP2mpSrTrCPOrgNdAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTrCPOrgNdAddr.setStatus("current")
_TmnxPcepPccP2mpSrTrRootAddrType_Type = InetAddressType
_TmnxPcepPccP2mpSrTrRootAddrType_Object = MibTableColumn
tmnxPcepPccP2mpSrTrRootAddrType = _TmnxPcepPccP2mpSrTrRootAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 6, 1, 7),
    _TmnxPcepPccP2mpSrTrRootAddrType_Type()
)
tmnxPcepPccP2mpSrTrRootAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTrRootAddrType.setStatus("current")


class _TmnxPcepPccP2mpSrTrRootAddr_Type(InetAddress):
    """Custom type tmnxPcepPccP2mpSrTrRootAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxPcepPccP2mpSrTrRootAddr_Type.__name__ = "InetAddress"
_TmnxPcepPccP2mpSrTrRootAddr_Object = MibTableColumn
tmnxPcepPccP2mpSrTrRootAddr = _TmnxPcepPccP2mpSrTrRootAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 6, 1, 8),
    _TmnxPcepPccP2mpSrTrRootAddr_Type()
)
tmnxPcepPccP2mpSrTrRootAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTrRootAddr.setStatus("current")


class _TmnxPcepPccP2mpSrTreeRootTreeId_Type(Unsigned32):
    """Custom type tmnxPcepPccP2mpSrTreeRootTreeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxPcepPccP2mpSrTreeRootTreeId_Type.__name__ = "Unsigned32"
_TmnxPcepPccP2mpSrTreeRootTreeId_Object = MibTableColumn
tmnxPcepPccP2mpSrTreeRootTreeId = _TmnxPcepPccP2mpSrTreeRootTreeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 6, 1, 9),
    _TmnxPcepPccP2mpSrTreeRootTreeId_Type()
)
tmnxPcepPccP2mpSrTreeRootTreeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTreeRootTreeId.setStatus("current")
_TmnxPcepPccP2mpSrTreeCdtPathName_Type = TNamedItem
_TmnxPcepPccP2mpSrTreeCdtPathName_Object = MibTableColumn
tmnxPcepPccP2mpSrTreeCdtPathName = _TmnxPcepPccP2mpSrTreeCdtPathName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 6, 1, 10),
    _TmnxPcepPccP2mpSrTreeCdtPathName_Type()
)
tmnxPcepPccP2mpSrTreeCdtPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTreeCdtPathName.setStatus("current")
_TmnxPcepPccP2mpSrTreePathInstId_Type = Unsigned32
_TmnxPcepPccP2mpSrTreePathInstId_Object = MibTableColumn
tmnxPcepPccP2mpSrTreePathInstId = _TmnxPcepPccP2mpSrTreePathInstId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 6, 1, 11),
    _TmnxPcepPccP2mpSrTreePathInstId_Type()
)
tmnxPcepPccP2mpSrTreePathInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTreePathInstId.setStatus("current")
_TmnxPcepPccP2mpSrTrDlPceAddrType_Type = InetAddressType
_TmnxPcepPccP2mpSrTrDlPceAddrType_Object = MibTableColumn
tmnxPcepPccP2mpSrTrDlPceAddrType = _TmnxPcepPccP2mpSrTrDlPceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 6, 1, 12),
    _TmnxPcepPccP2mpSrTrDlPceAddrType_Type()
)
tmnxPcepPccP2mpSrTrDlPceAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTrDlPceAddrType.setStatus("current")


class _TmnxPcepPccP2mpSrTrDlPceAddr_Type(InetAddress):
    """Custom type tmnxPcepPccP2mpSrTrDlPceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxPcepPccP2mpSrTrDlPceAddr_Type.__name__ = "InetAddress"
_TmnxPcepPccP2mpSrTrDlPceAddr_Object = MibTableColumn
tmnxPcepPccP2mpSrTrDlPceAddr = _TmnxPcepPccP2mpSrTrDlPceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 6, 1, 13),
    _TmnxPcepPccP2mpSrTrDlPceAddr_Type()
)
tmnxPcepPccP2mpSrTrDlPceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTrDlPceAddr.setStatus("current")


class _TmnxPcepPccP2mpSrTreeOperStatus_Type(Integer32):
    """Custom type tmnxPcepPccP2mpSrTreeOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("up", 1),
          ("down", 2))
    )


_TmnxPcepPccP2mpSrTreeOperStatus_Type.__name__ = "Integer32"
_TmnxPcepPccP2mpSrTreeOperStatus_Object = MibTableColumn
tmnxPcepPccP2mpSrTreeOperStatus = _TmnxPcepPccP2mpSrTreeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 6, 1, 14),
    _TmnxPcepPccP2mpSrTreeOperStatus_Type()
)
tmnxPcepPccP2mpSrTreeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTreeOperStatus.setStatus("current")
_TmnxPcepPccP2mpSrTrOriginatorAsn_Type = Unsigned32
_TmnxPcepPccP2mpSrTrOriginatorAsn_Object = MibTableColumn
tmnxPcepPccP2mpSrTrOriginatorAsn = _TmnxPcepPccP2mpSrTrOriginatorAsn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 6, 1, 15),
    _TmnxPcepPccP2mpSrTrOriginatorAsn_Type()
)
tmnxPcepPccP2mpSrTrOriginatorAsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTrOriginatorAsn.setStatus("current")
_TmnxPcepPccP2mpSrTrDiscriminator_Type = Unsigned32
_TmnxPcepPccP2mpSrTrDiscriminator_Object = MibTableColumn
tmnxPcepPccP2mpSrTrDiscriminator = _TmnxPcepPccP2mpSrTrDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 6, 1, 16),
    _TmnxPcepPccP2mpSrTrDiscriminator_Type()
)
tmnxPcepPccP2mpSrTrDiscriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTrDiscriminator.setStatus("current")


class _TmnxPcepPccP2mpSrTreePreference_Type(Unsigned32):
    """Custom type tmnxPcepPccP2mpSrTreePreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_TmnxPcepPccP2mpSrTreePreference_Type.__name__ = "Unsigned32"
_TmnxPcepPccP2mpSrTreePreference_Object = MibTableColumn
tmnxPcepPccP2mpSrTreePreference = _TmnxPcepPccP2mpSrTreePreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 6, 1, 17),
    _TmnxPcepPccP2mpSrTreePreference_Type()
)
tmnxPcepPccP2mpSrTreePreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTreePreference.setStatus("current")
_TmnxPcepPccP2mpSrTreeAddTable_Object = MibTable
tmnxPcepPccP2mpSrTreeAddTable = _TmnxPcepPccP2mpSrTreeAddTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 7)
)
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTreeAddTable.setStatus("current")
_TmnxPcepPccP2mpSrTreeAddEntry_Object = MibTableRow
tmnxPcepPccP2mpSrTreeAddEntry = _TmnxPcepPccP2mpSrTreeAddEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 7, 1)
)
tmnxPcepPccP2mpSrTreeAddEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepEntityIndex"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdPLspId"),
)
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTreeAddEntry.setStatus("current")


class _TmnxPcepPccP2mpSrTreeAddTreeId_Type(Unsigned32):
    """Custom type tmnxPcepPccP2mpSrTreeAddTreeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxPcepPccP2mpSrTreeAddTreeId_Type.__name__ = "Unsigned32"
_TmnxPcepPccP2mpSrTreeAddTreeId_Object = MibTableColumn
tmnxPcepPccP2mpSrTreeAddTreeId = _TmnxPcepPccP2mpSrTreeAddTreeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 7, 1, 1),
    _TmnxPcepPccP2mpSrTreeAddTreeId_Type()
)
tmnxPcepPccP2mpSrTreeAddTreeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTreeAddTreeId.setStatus("current")
_TmnxPcepPccP2mpSrTrAddRtAddrType_Type = InetAddressType
_TmnxPcepPccP2mpSrTrAddRtAddrType_Object = MibTableColumn
tmnxPcepPccP2mpSrTrAddRtAddrType = _TmnxPcepPccP2mpSrTrAddRtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 7, 1, 2),
    _TmnxPcepPccP2mpSrTrAddRtAddrType_Type()
)
tmnxPcepPccP2mpSrTrAddRtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTrAddRtAddrType.setStatus("current")


class _TmnxPcepPccP2mpSrTrAddRtAddr_Type(InetAddress):
    """Custom type tmnxPcepPccP2mpSrTrAddRtAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepPccP2mpSrTrAddRtAddr_Type.__name__ = "InetAddress"
_TmnxPcepPccP2mpSrTrAddRtAddr_Object = MibTableColumn
tmnxPcepPccP2mpSrTrAddRtAddr = _TmnxPcepPccP2mpSrTrAddRtAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 7, 1, 3),
    _TmnxPcepPccP2mpSrTrAddRtAddr_Type()
)
tmnxPcepPccP2mpSrTrAddRtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTrAddRtAddr.setStatus("current")
_TmnxPcepPccP2mpSrTAdLeafAddrType_Type = InetAddressType
_TmnxPcepPccP2mpSrTAdLeafAddrType_Object = MibTableColumn
tmnxPcepPccP2mpSrTAdLeafAddrType = _TmnxPcepPccP2mpSrTAdLeafAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 7, 1, 4),
    _TmnxPcepPccP2mpSrTAdLeafAddrType_Type()
)
tmnxPcepPccP2mpSrTAdLeafAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTAdLeafAddrType.setStatus("current")


class _TmnxPcepPccP2mpSrTAdLeafAddr_Type(InetAddress):
    """Custom type tmnxPcepPccP2mpSrTAdLeafAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepPccP2mpSrTAdLeafAddr_Type.__name__ = "InetAddress"
_TmnxPcepPccP2mpSrTAdLeafAddr_Object = MibTableColumn
tmnxPcepPccP2mpSrTAdLeafAddr = _TmnxPcepPccP2mpSrTAdLeafAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 7, 1, 5),
    _TmnxPcepPccP2mpSrTAdLeafAddr_Type()
)
tmnxPcepPccP2mpSrTAdLeafAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTAdLeafAddr.setStatus("current")
_TmnxPcepPccP2mpSrTreeRemoveTable_Object = MibTable
tmnxPcepPccP2mpSrTreeRemoveTable = _TmnxPcepPccP2mpSrTreeRemoveTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 8)
)
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTreeRemoveTable.setStatus("current")
_TmnxPcepPccP2mpSrTreeRemoveEntry_Object = MibTableRow
tmnxPcepPccP2mpSrTreeRemoveEntry = _TmnxPcepPccP2mpSrTreeRemoveEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 8, 1)
)
tmnxPcepPccP2mpSrTreeRemoveEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepEntityIndex"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdPLspId"),
)
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTreeRemoveEntry.setStatus("current")


class _TmnxPcepPccP2mpSrTrRemoveTrId_Type(Unsigned32):
    """Custom type tmnxPcepPccP2mpSrTrRemoveTrId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxPcepPccP2mpSrTrRemoveTrId_Type.__name__ = "Unsigned32"
_TmnxPcepPccP2mpSrTrRemoveTrId_Object = MibTableColumn
tmnxPcepPccP2mpSrTrRemoveTrId = _TmnxPcepPccP2mpSrTrRemoveTrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 8, 1, 1),
    _TmnxPcepPccP2mpSrTrRemoveTrId_Type()
)
tmnxPcepPccP2mpSrTrRemoveTrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTrRemoveTrId.setStatus("current")
_TmnxPcepPccP2mpSrTrRemRtAddrType_Type = InetAddressType
_TmnxPcepPccP2mpSrTrRemRtAddrType_Object = MibTableColumn
tmnxPcepPccP2mpSrTrRemRtAddrType = _TmnxPcepPccP2mpSrTrRemRtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 8, 1, 2),
    _TmnxPcepPccP2mpSrTrRemRtAddrType_Type()
)
tmnxPcepPccP2mpSrTrRemRtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTrRemRtAddrType.setStatus("current")


class _TmnxPcepPccP2mpSrTrRemRtAddr_Type(InetAddress):
    """Custom type tmnxPcepPccP2mpSrTrRemRtAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepPccP2mpSrTrRemRtAddr_Type.__name__ = "InetAddress"
_TmnxPcepPccP2mpSrTrRemRtAddr_Object = MibTableColumn
tmnxPcepPccP2mpSrTrRemRtAddr = _TmnxPcepPccP2mpSrTrRemRtAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 8, 1, 3),
    _TmnxPcepPccP2mpSrTrRemRtAddr_Type()
)
tmnxPcepPccP2mpSrTrRemRtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTrRemRtAddr.setStatus("current")
_TmnxPcepPccP2mpSrTRmLeafAddrType_Type = InetAddressType
_TmnxPcepPccP2mpSrTRmLeafAddrType_Object = MibTableColumn
tmnxPcepPccP2mpSrTRmLeafAddrType = _TmnxPcepPccP2mpSrTRmLeafAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 8, 1, 4),
    _TmnxPcepPccP2mpSrTRmLeafAddrType_Type()
)
tmnxPcepPccP2mpSrTRmLeafAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTRmLeafAddrType.setStatus("current")


class _TmnxPcepPccP2mpSrTRmLeafAddr_Type(InetAddress):
    """Custom type tmnxPcepPccP2mpSrTRmLeafAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepPccP2mpSrTRmLeafAddr_Type.__name__ = "InetAddress"
_TmnxPcepPccP2mpSrTRmLeafAddr_Object = MibTableColumn
tmnxPcepPccP2mpSrTRmLeafAddr = _TmnxPcepPccP2mpSrTRmLeafAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 8, 1, 5),
    _TmnxPcepPccP2mpSrTRmLeafAddr_Type()
)
tmnxPcepPccP2mpSrTRmLeafAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTRmLeafAddr.setStatus("current")
_TmnxPcepPccP2mpSrTreeOldTable_Object = MibTable
tmnxPcepPccP2mpSrTreeOldTable = _TmnxPcepPccP2mpSrTreeOldTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 9)
)
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTreeOldTable.setStatus("current")
_TmnxPcepPccP2mpSrTreeOldEntry_Object = MibTableRow
tmnxPcepPccP2mpSrTreeOldEntry = _TmnxPcepPccP2mpSrTreeOldEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 9, 1)
)
tmnxPcepPccP2mpSrTreeOldEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepEntityIndex"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdPLspId"),
)
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTreeOldEntry.setStatus("current")


class _TmnxPcepPccP2mpSrTreeOldTreeId_Type(Unsigned32):
    """Custom type tmnxPcepPccP2mpSrTreeOldTreeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxPcepPccP2mpSrTreeOldTreeId_Type.__name__ = "Unsigned32"
_TmnxPcepPccP2mpSrTreeOldTreeId_Object = MibTableColumn
tmnxPcepPccP2mpSrTreeOldTreeId = _TmnxPcepPccP2mpSrTreeOldTreeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 9, 1, 1),
    _TmnxPcepPccP2mpSrTreeOldTreeId_Type()
)
tmnxPcepPccP2mpSrTreeOldTreeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTreeOldTreeId.setStatus("current")
_TmnxPcepPccP2mpSrTrOldRtAddrType_Type = InetAddressType
_TmnxPcepPccP2mpSrTrOldRtAddrType_Object = MibTableColumn
tmnxPcepPccP2mpSrTrOldRtAddrType = _TmnxPcepPccP2mpSrTrOldRtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 9, 1, 2),
    _TmnxPcepPccP2mpSrTrOldRtAddrType_Type()
)
tmnxPcepPccP2mpSrTrOldRtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTrOldRtAddrType.setStatus("current")


class _TmnxPcepPccP2mpSrTrOldRtAddr_Type(InetAddress):
    """Custom type tmnxPcepPccP2mpSrTrOldRtAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepPccP2mpSrTrOldRtAddr_Type.__name__ = "InetAddress"
_TmnxPcepPccP2mpSrTrOldRtAddr_Object = MibTableColumn
tmnxPcepPccP2mpSrTrOldRtAddr = _TmnxPcepPccP2mpSrTrOldRtAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 9, 1, 3),
    _TmnxPcepPccP2mpSrTrOldRtAddr_Type()
)
tmnxPcepPccP2mpSrTrOldRtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTrOldRtAddr.setStatus("current")
_TmnxPcepPccP2mpSrTOdLeafAddrType_Type = InetAddressType
_TmnxPcepPccP2mpSrTOdLeafAddrType_Object = MibTableColumn
tmnxPcepPccP2mpSrTOdLeafAddrType = _TmnxPcepPccP2mpSrTOdLeafAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 9, 1, 4),
    _TmnxPcepPccP2mpSrTOdLeafAddrType_Type()
)
tmnxPcepPccP2mpSrTOdLeafAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTOdLeafAddrType.setStatus("current")


class _TmnxPcepPccP2mpSrTOdLeafAddr_Type(InetAddress):
    """Custom type tmnxPcepPccP2mpSrTOdLeafAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepPccP2mpSrTOdLeafAddr_Type.__name__ = "InetAddress"
_TmnxPcepPccP2mpSrTOdLeafAddr_Object = MibTableColumn
tmnxPcepPccP2mpSrTOdLeafAddr = _TmnxPcepPccP2mpSrTOdLeafAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 2, 9, 1, 5),
    _TmnxPcepPccP2mpSrTOdLeafAddr_Type()
)
tmnxPcepPccP2mpSrTOdLeafAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTOdLeafAddr.setStatus("current")
_TmnxPcepStatsObjects_ObjectIdentity = ObjectIdentity
tmnxPcepStatsObjects = _TmnxPcepStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3)
)
_TmnxPcepPccStatsObjects_ObjectIdentity = ObjectIdentity
tmnxPcepPccStatsObjects = _TmnxPcepPccStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1)
)
_TmnxPcepPccReqMsgInfoTable_Object = MibTable
tmnxPcepPccReqMsgInfoTable = _TmnxPcepPccReqMsgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgInfoTable.setStatus("current")
_TmnxPcepPccReqMsgInfoEntry_Object = MibTableRow
tmnxPcepPccReqMsgInfoEntry = _TmnxPcepPccReqMsgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1)
)
tmnxPcepPccReqMsgInfoEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepEntityIndex"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgRequestId"),
)
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgInfoEntry.setStatus("current")


class _TmnxPcepPccReqMsgRequestId_Type(Unsigned32):
    """Custom type tmnxPcepPccReqMsgRequestId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxPcepPccReqMsgRequestId_Type.__name__ = "Unsigned32"
_TmnxPcepPccReqMsgRequestId_Object = MibTableColumn
tmnxPcepPccReqMsgRequestId = _TmnxPcepPccReqMsgRequestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 1),
    _TmnxPcepPccReqMsgRequestId_Type()
)
tmnxPcepPccReqMsgRequestId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgRequestId.setStatus("current")
_TmnxPcepPccReqMsgLspType_Type = TmnxPcepLspType
_TmnxPcepPccReqMsgLspType_Object = MibTableColumn
tmnxPcepPccReqMsgLspType = _TmnxPcepPccReqMsgLspType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 2),
    _TmnxPcepPccReqMsgLspType_Type()
)
tmnxPcepPccReqMsgLspType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgLspType.setStatus("current")
_TmnxPcepPccReqMsgTunnelId_Type = Unsigned32
_TmnxPcepPccReqMsgTunnelId_Object = MibTableColumn
tmnxPcepPccReqMsgTunnelId = _TmnxPcepPccReqMsgTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 3),
    _TmnxPcepPccReqMsgTunnelId_Type()
)
tmnxPcepPccReqMsgTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgTunnelId.setStatus("current")
_TmnxPcepPccReqMsgLspId_Type = Unsigned32
_TmnxPcepPccReqMsgLspId_Object = MibTableColumn
tmnxPcepPccReqMsgLspId = _TmnxPcepPccReqMsgLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 4),
    _TmnxPcepPccReqMsgLspId_Type()
)
tmnxPcepPccReqMsgLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgLspId.setStatus("current")
_TmnxPcepPccReqMsgExtTunnelIdType_Type = InetAddressType
_TmnxPcepPccReqMsgExtTunnelIdType_Object = MibTableColumn
tmnxPcepPccReqMsgExtTunnelIdType = _TmnxPcepPccReqMsgExtTunnelIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 5),
    _TmnxPcepPccReqMsgExtTunnelIdType_Type()
)
tmnxPcepPccReqMsgExtTunnelIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgExtTunnelIdType.setStatus("current")


class _TmnxPcepPccReqMsgExtTunnelId_Type(InetAddress):
    """Custom type tmnxPcepPccReqMsgExtTunnelId based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepPccReqMsgExtTunnelId_Type.__name__ = "InetAddress"
_TmnxPcepPccReqMsgExtTunnelId_Object = MibTableColumn
tmnxPcepPccReqMsgExtTunnelId = _TmnxPcepPccReqMsgExtTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 6),
    _TmnxPcepPccReqMsgExtTunnelId_Type()
)
tmnxPcepPccReqMsgExtTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgExtTunnelId.setStatus("current")
_TmnxPcepPccReqMsgLspName_Type = TLNamedItemOrEmpty
_TmnxPcepPccReqMsgLspName_Object = MibTableColumn
tmnxPcepPccReqMsgLspName = _TmnxPcepPccReqMsgLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 7),
    _TmnxPcepPccReqMsgLspName_Type()
)
tmnxPcepPccReqMsgLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgLspName.setStatus("current")
_TmnxPcepPccReqMsgSrcAddrType_Type = InetAddressType
_TmnxPcepPccReqMsgSrcAddrType_Object = MibTableColumn
tmnxPcepPccReqMsgSrcAddrType = _TmnxPcepPccReqMsgSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 8),
    _TmnxPcepPccReqMsgSrcAddrType_Type()
)
tmnxPcepPccReqMsgSrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgSrcAddrType.setStatus("current")


class _TmnxPcepPccReqMsgSrcAddr_Type(InetAddress):
    """Custom type tmnxPcepPccReqMsgSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepPccReqMsgSrcAddr_Type.__name__ = "InetAddress"
_TmnxPcepPccReqMsgSrcAddr_Object = MibTableColumn
tmnxPcepPccReqMsgSrcAddr = _TmnxPcepPccReqMsgSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 9),
    _TmnxPcepPccReqMsgSrcAddr_Type()
)
tmnxPcepPccReqMsgSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgSrcAddr.setStatus("current")
_TmnxPcepPccReqMsgDstAddrType_Type = InetAddressType
_TmnxPcepPccReqMsgDstAddrType_Object = MibTableColumn
tmnxPcepPccReqMsgDstAddrType = _TmnxPcepPccReqMsgDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 10),
    _TmnxPcepPccReqMsgDstAddrType_Type()
)
tmnxPcepPccReqMsgDstAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgDstAddrType.setStatus("current")


class _TmnxPcepPccReqMsgDstAddr_Type(InetAddress):
    """Custom type tmnxPcepPccReqMsgDstAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepPccReqMsgDstAddr_Type.__name__ = "InetAddress"
_TmnxPcepPccReqMsgDstAddr_Object = MibTableColumn
tmnxPcepPccReqMsgDstAddr = _TmnxPcepPccReqMsgDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 11),
    _TmnxPcepPccReqMsgDstAddr_Type()
)
tmnxPcepPccReqMsgDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgDstAddr.setStatus("current")


class _TmnxPcepPccReqMsgState_Type(Integer32):
    """Custom type tmnxPcepPccReqMsgState based on Integer32"""
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
        *(("unknown", 0),
          ("requestParameter", 1),
          ("sentForCompute", 2),
          ("errorReceived", 3),
          ("notifyReceived", 4),
          ("cancel", 5),
          ("computeReceived", 6))
    )


_TmnxPcepPccReqMsgState_Type.__name__ = "Integer32"
_TmnxPcepPccReqMsgState_Object = MibTableColumn
tmnxPcepPccReqMsgState = _TmnxPcepPccReqMsgState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 12),
    _TmnxPcepPccReqMsgState_Type()
)
tmnxPcepPccReqMsgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgState.setStatus("current")
_TmnxPcepPccReqMsgSvecId_Type = Counter64
_TmnxPcepPccReqMsgSvecId_Object = MibTableColumn
tmnxPcepPccReqMsgSvecId = _TmnxPcepPccReqMsgSvecId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 13),
    _TmnxPcepPccReqMsgSvecId_Type()
)
tmnxPcepPccReqMsgSvecId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgSvecId.setStatus("current")
_TmnxPcepPccReqMsgIgpMetric_Type = Unsigned32
_TmnxPcepPccReqMsgIgpMetric_Object = MibTableColumn
tmnxPcepPccReqMsgIgpMetric = _TmnxPcepPccReqMsgIgpMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 14),
    _TmnxPcepPccReqMsgIgpMetric_Type()
)
tmnxPcepPccReqMsgIgpMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgIgpMetric.setStatus("current")
_TmnxPcepPccReqMsgTeMetric_Type = Unsigned32
_TmnxPcepPccReqMsgTeMetric_Object = MibTableColumn
tmnxPcepPccReqMsgTeMetric = _TmnxPcepPccReqMsgTeMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 15),
    _TmnxPcepPccReqMsgTeMetric_Type()
)
tmnxPcepPccReqMsgTeMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgTeMetric.setStatus("current")
_TmnxPcepPccReqMsgHopCount_Type = Unsigned32
_TmnxPcepPccReqMsgHopCount_Object = MibTableColumn
tmnxPcepPccReqMsgHopCount = _TmnxPcepPccReqMsgHopCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 16),
    _TmnxPcepPccReqMsgHopCount_Type()
)
tmnxPcepPccReqMsgHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgHopCount.setStatus("current")


class _TmnxPcepPccReqMsgMetricBound_Type(Bits):
    """Custom type tmnxPcepPccReqMsgMetricBound based on Bits"""
    namedValues = NamedValues(
        *(("igpMetric", 0),
          ("teMetric", 1),
          ("hopCount", 2))
    )

_TmnxPcepPccReqMsgMetricBound_Type.__name__ = "Bits"
_TmnxPcepPccReqMsgMetricBound_Object = MibTableColumn
tmnxPcepPccReqMsgMetricBound = _TmnxPcepPccReqMsgMetricBound_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 17),
    _TmnxPcepPccReqMsgMetricBound_Type()
)
tmnxPcepPccReqMsgMetricBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgMetricBound.setStatus("current")


class _TmnxPcepPccReqMsgMetricCompute_Type(Bits):
    """Custom type tmnxPcepPccReqMsgMetricCompute based on Bits"""
    namedValues = NamedValues(
        *(("igpMetric", 0),
          ("teMetric", 1),
          ("hopCount", 2))
    )

_TmnxPcepPccReqMsgMetricCompute_Type.__name__ = "Bits"
_TmnxPcepPccReqMsgMetricCompute_Object = MibTableColumn
tmnxPcepPccReqMsgMetricCompute = _TmnxPcepPccReqMsgMetricCompute_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 18),
    _TmnxPcepPccReqMsgMetricCompute_Type()
)
tmnxPcepPccReqMsgMetricCompute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgMetricCompute.setStatus("current")
_TmnxPcepPccReqMsgLclProtDesired_Type = TruthValue
_TmnxPcepPccReqMsgLclProtDesired_Object = MibTableColumn
tmnxPcepPccReqMsgLclProtDesired = _TmnxPcepPccReqMsgLclProtDesired_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 19),
    _TmnxPcepPccReqMsgLclProtDesired_Type()
)
tmnxPcepPccReqMsgLclProtDesired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgLclProtDesired.setStatus("current")


class _TmnxPcepPccReqMsgSetupPriority_Type(Unsigned32):
    """Custom type tmnxPcepPccReqMsgSetupPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxPcepPccReqMsgSetupPriority_Type.__name__ = "Unsigned32"
_TmnxPcepPccReqMsgSetupPriority_Object = MibTableColumn
tmnxPcepPccReqMsgSetupPriority = _TmnxPcepPccReqMsgSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 20),
    _TmnxPcepPccReqMsgSetupPriority_Type()
)
tmnxPcepPccReqMsgSetupPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgSetupPriority.setStatus("current")


class _TmnxPcepPccReqMsgHoldingPriority_Type(Unsigned32):
    """Custom type tmnxPcepPccReqMsgHoldingPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TmnxPcepPccReqMsgHoldingPriority_Type.__name__ = "Unsigned32"
_TmnxPcepPccReqMsgHoldingPriority_Object = MibTableColumn
tmnxPcepPccReqMsgHoldingPriority = _TmnxPcepPccReqMsgHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 21),
    _TmnxPcepPccReqMsgHoldingPriority_Type()
)
tmnxPcepPccReqMsgHoldingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgHoldingPriority.setStatus("current")
_TmnxPcepPccReqMsgExcludeAny_Type = Unsigned32
_TmnxPcepPccReqMsgExcludeAny_Object = MibTableColumn
tmnxPcepPccReqMsgExcludeAny = _TmnxPcepPccReqMsgExcludeAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 22),
    _TmnxPcepPccReqMsgExcludeAny_Type()
)
tmnxPcepPccReqMsgExcludeAny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgExcludeAny.setStatus("current")
_TmnxPcepPccReqMsgIncludeAny_Type = Unsigned32
_TmnxPcepPccReqMsgIncludeAny_Object = MibTableColumn
tmnxPcepPccReqMsgIncludeAny = _TmnxPcepPccReqMsgIncludeAny_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 23),
    _TmnxPcepPccReqMsgIncludeAny_Type()
)
tmnxPcepPccReqMsgIncludeAny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgIncludeAny.setStatus("current")
_TmnxPcepPccReqMsgIncludeAll_Type = Unsigned32
_TmnxPcepPccReqMsgIncludeAll_Object = MibTableColumn
tmnxPcepPccReqMsgIncludeAll = _TmnxPcepPccReqMsgIncludeAll_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 24),
    _TmnxPcepPccReqMsgIncludeAll_Type()
)
tmnxPcepPccReqMsgIncludeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgIncludeAll.setStatus("current")
_TmnxPcepPccReqMsgPriority_Type = Unsigned32
_TmnxPcepPccReqMsgPriority_Object = MibTableColumn
tmnxPcepPccReqMsgPriority = _TmnxPcepPccReqMsgPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 25),
    _TmnxPcepPccReqMsgPriority_Type()
)
tmnxPcepPccReqMsgPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgPriority.setStatus("current")
_TmnxPcepPccReqMsgReoptimization_Type = TruthValue
_TmnxPcepPccReqMsgReoptimization_Object = MibTableColumn
tmnxPcepPccReqMsgReoptimization = _TmnxPcepPccReqMsgReoptimization_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 26),
    _TmnxPcepPccReqMsgReoptimization_Type()
)
tmnxPcepPccReqMsgReoptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgReoptimization.setStatus("current")
_TmnxPcepPccReqMsgBidirectional_Type = TruthValue
_TmnxPcepPccReqMsgBidirectional_Object = MibTableColumn
tmnxPcepPccReqMsgBidirectional = _TmnxPcepPccReqMsgBidirectional_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 27),
    _TmnxPcepPccReqMsgBidirectional_Type()
)
tmnxPcepPccReqMsgBidirectional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgBidirectional.setStatus("current")
_TmnxPcepPccReqMsgStrictLoose_Type = TruthValue
_TmnxPcepPccReqMsgStrictLoose_Object = MibTableColumn
tmnxPcepPccReqMsgStrictLoose = _TmnxPcepPccReqMsgStrictLoose_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 28),
    _TmnxPcepPccReqMsgStrictLoose_Type()
)
tmnxPcepPccReqMsgStrictLoose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgStrictLoose.setStatus("current")
_TmnxPcepPccReqMsgLspBandwidth_Type = Unsigned32
_TmnxPcepPccReqMsgLspBandwidth_Object = MibTableColumn
tmnxPcepPccReqMsgLspBandwidth = _TmnxPcepPccReqMsgLspBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 29),
    _TmnxPcepPccReqMsgLspBandwidth_Type()
)
tmnxPcepPccReqMsgLspBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgLspBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgLspBandwidth.setUnits("Mbps")


class _TmnxPcepPccReqMsgMaxSrLabels_Type(Unsigned32):
    """Custom type tmnxPcepPccReqMsgMaxSrLabels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_TmnxPcepPccReqMsgMaxSrLabels_Type.__name__ = "Unsigned32"
_TmnxPcepPccReqMsgMaxSrLabels_Object = MibTableColumn
tmnxPcepPccReqMsgMaxSrLabels = _TmnxPcepPccReqMsgMaxSrLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 1, 1, 30),
    _TmnxPcepPccReqMsgMaxSrLabels_Type()
)
tmnxPcepPccReqMsgMaxSrLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgMaxSrLabels.setStatus("current")
_TmnxPcepPccReqPathProfInfoTable_Object = MibTable
tmnxPcepPccReqPathProfInfoTable = _TmnxPcepPccReqPathProfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxPcepPccReqPathProfInfoTable.setStatus("current")
_TmnxPcepPccReqPathProfInfoEntry_Object = MibTableRow
tmnxPcepPccReqPathProfInfoEntry = _TmnxPcepPccReqPathProfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 2, 1)
)
tmnxPcepPccReqPathProfInfoEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepEntityIndex"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgRequestId"),
)
if mibBuilder.loadTexts:
    tmnxPcepPccReqPathProfInfoEntry.setStatus("current")
_TmnxPcepPccReqPathProf1_Type = Unsigned32
_TmnxPcepPccReqPathProf1_Object = MibTableColumn
tmnxPcepPccReqPathProf1 = _TmnxPcepPccReqPathProf1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 2, 1, 1),
    _TmnxPcepPccReqPathProf1_Type()
)
tmnxPcepPccReqPathProf1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqPathProf1.setStatus("current")
_TmnxPcepPccReqExtendedPathProf1_Type = Unsigned32
_TmnxPcepPccReqExtendedPathProf1_Object = MibTableColumn
tmnxPcepPccReqExtendedPathProf1 = _TmnxPcepPccReqExtendedPathProf1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 2, 1, 2),
    _TmnxPcepPccReqExtendedPathProf1_Type()
)
tmnxPcepPccReqExtendedPathProf1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqExtendedPathProf1.setStatus("current")
_TmnxPcepPccReqPathProf2_Type = Unsigned32
_TmnxPcepPccReqPathProf2_Object = MibTableColumn
tmnxPcepPccReqPathProf2 = _TmnxPcepPccReqPathProf2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 2, 1, 3),
    _TmnxPcepPccReqPathProf2_Type()
)
tmnxPcepPccReqPathProf2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqPathProf2.setStatus("current")
_TmnxPcepPccReqExtendedPathProf2_Type = Unsigned32
_TmnxPcepPccReqExtendedPathProf2_Object = MibTableColumn
tmnxPcepPccReqExtendedPathProf2 = _TmnxPcepPccReqExtendedPathProf2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 2, 1, 4),
    _TmnxPcepPccReqExtendedPathProf2_Type()
)
tmnxPcepPccReqExtendedPathProf2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqExtendedPathProf2.setStatus("current")
_TmnxPcepPccReqPathProf3_Type = Unsigned32
_TmnxPcepPccReqPathProf3_Object = MibTableColumn
tmnxPcepPccReqPathProf3 = _TmnxPcepPccReqPathProf3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 2, 1, 5),
    _TmnxPcepPccReqPathProf3_Type()
)
tmnxPcepPccReqPathProf3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqPathProf3.setStatus("current")
_TmnxPcepPccReqExtendedPathProf3_Type = Unsigned32
_TmnxPcepPccReqExtendedPathProf3_Object = MibTableColumn
tmnxPcepPccReqExtendedPathProf3 = _TmnxPcepPccReqExtendedPathProf3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 2, 1, 6),
    _TmnxPcepPccReqExtendedPathProf3_Type()
)
tmnxPcepPccReqExtendedPathProf3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqExtendedPathProf3.setStatus("current")
_TmnxPcepPccReqPathProf4_Type = Unsigned32
_TmnxPcepPccReqPathProf4_Object = MibTableColumn
tmnxPcepPccReqPathProf4 = _TmnxPcepPccReqPathProf4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 2, 1, 7),
    _TmnxPcepPccReqPathProf4_Type()
)
tmnxPcepPccReqPathProf4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqPathProf4.setStatus("current")
_TmnxPcepPccReqExtendedPathProf4_Type = Unsigned32
_TmnxPcepPccReqExtendedPathProf4_Object = MibTableColumn
tmnxPcepPccReqExtendedPathProf4 = _TmnxPcepPccReqExtendedPathProf4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 2, 1, 8),
    _TmnxPcepPccReqExtendedPathProf4_Type()
)
tmnxPcepPccReqExtendedPathProf4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqExtendedPathProf4.setStatus("current")
_TmnxPcepPccReqPathProf5_Type = Unsigned32
_TmnxPcepPccReqPathProf5_Object = MibTableColumn
tmnxPcepPccReqPathProf5 = _TmnxPcepPccReqPathProf5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 2, 1, 9),
    _TmnxPcepPccReqPathProf5_Type()
)
tmnxPcepPccReqPathProf5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqPathProf5.setStatus("current")
_TmnxPcepPccReqExtendedPathProf5_Type = Unsigned32
_TmnxPcepPccReqExtendedPathProf5_Object = MibTableColumn
tmnxPcepPccReqExtendedPathProf5 = _TmnxPcepPccReqExtendedPathProf5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 2, 1, 10),
    _TmnxPcepPccReqExtendedPathProf5_Type()
)
tmnxPcepPccReqExtendedPathProf5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccReqExtendedPathProf5.setStatus("current")
_TmnxPcepPccLspUpdateInfoTable_Object = MibTable
tmnxPcepPccLspUpdateInfoTable = _TmnxPcepPccLspUpdateInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdateInfoTable.setStatus("current")
_TmnxPcepPccLspUpdateInfoEntry_Object = MibTableRow
tmnxPcepPccLspUpdateInfoEntry = _TmnxPcepPccLspUpdateInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3, 1)
)
tmnxPcepPccLspUpdateInfoEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepEntityIndex"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdPLspId"),
)
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdateInfoEntry.setStatus("current")


class _TmnxPcepPccLspUpdPLspId_Type(Unsigned32):
    """Custom type tmnxPcepPccLspUpdPLspId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxPcepPccLspUpdPLspId_Type.__name__ = "Unsigned32"
_TmnxPcepPccLspUpdPLspId_Object = MibTableColumn
tmnxPcepPccLspUpdPLspId = _TmnxPcepPccLspUpdPLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3, 1, 1),
    _TmnxPcepPccLspUpdPLspId_Type()
)
tmnxPcepPccLspUpdPLspId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdPLspId.setStatus("current")
_TmnxPcepPccLspUpdLspId_Type = Unsigned32
_TmnxPcepPccLspUpdLspId_Object = MibTableColumn
tmnxPcepPccLspUpdLspId = _TmnxPcepPccLspUpdLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3, 1, 2),
    _TmnxPcepPccLspUpdLspId_Type()
)
tmnxPcepPccLspUpdLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdLspId.setStatus("current")
_TmnxPcepPccLspUpdLspType_Type = TmnxPcepLspType
_TmnxPcepPccLspUpdLspType_Object = MibTableColumn
tmnxPcepPccLspUpdLspType = _TmnxPcepPccLspUpdLspType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3, 1, 3),
    _TmnxPcepPccLspUpdLspType_Type()
)
tmnxPcepPccLspUpdLspType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdLspType.setStatus("current")
_TmnxPcepPccLspUpdTunnelId_Type = Unsigned32
_TmnxPcepPccLspUpdTunnelId_Object = MibTableColumn
tmnxPcepPccLspUpdTunnelId = _TmnxPcepPccLspUpdTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3, 1, 4),
    _TmnxPcepPccLspUpdTunnelId_Type()
)
tmnxPcepPccLspUpdTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdTunnelId.setStatus("current")
_TmnxPcepPccLspUpdExtTunnelIdType_Type = InetAddressType
_TmnxPcepPccLspUpdExtTunnelIdType_Object = MibTableColumn
tmnxPcepPccLspUpdExtTunnelIdType = _TmnxPcepPccLspUpdExtTunnelIdType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3, 1, 5),
    _TmnxPcepPccLspUpdExtTunnelIdType_Type()
)
tmnxPcepPccLspUpdExtTunnelIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdExtTunnelIdType.setStatus("current")


class _TmnxPcepPccLspUpdExtTunnelId_Type(InetAddress):
    """Custom type tmnxPcepPccLspUpdExtTunnelId based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepPccLspUpdExtTunnelId_Type.__name__ = "InetAddress"
_TmnxPcepPccLspUpdExtTunnelId_Object = MibTableColumn
tmnxPcepPccLspUpdExtTunnelId = _TmnxPcepPccLspUpdExtTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3, 1, 6),
    _TmnxPcepPccLspUpdExtTunnelId_Type()
)
tmnxPcepPccLspUpdExtTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdExtTunnelId.setStatus("current")
_TmnxPcepPccLspUpdLspName_Type = TLNamedItemOrEmpty
_TmnxPcepPccLspUpdLspName_Object = MibTableColumn
tmnxPcepPccLspUpdLspName = _TmnxPcepPccLspUpdLspName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3, 1, 7),
    _TmnxPcepPccLspUpdLspName_Type()
)
tmnxPcepPccLspUpdLspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdLspName.setStatus("current")
_TmnxPcepPccLspUpdSenderType_Type = InetAddressType
_TmnxPcepPccLspUpdSenderType_Object = MibTableColumn
tmnxPcepPccLspUpdSenderType = _TmnxPcepPccLspUpdSenderType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3, 1, 8),
    _TmnxPcepPccLspUpdSenderType_Type()
)
tmnxPcepPccLspUpdSenderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdSenderType.setStatus("current")


class _TmnxPcepPccLspUpdSenderAddr_Type(InetAddress):
    """Custom type tmnxPcepPccLspUpdSenderAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepPccLspUpdSenderAddr_Type.__name__ = "InetAddress"
_TmnxPcepPccLspUpdSenderAddr_Object = MibTableColumn
tmnxPcepPccLspUpdSenderAddr = _TmnxPcepPccLspUpdSenderAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3, 1, 9),
    _TmnxPcepPccLspUpdSenderAddr_Type()
)
tmnxPcepPccLspUpdSenderAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdSenderAddr.setStatus("current")
_TmnxPcepPccLspUpdSourceType_Type = InetAddressType
_TmnxPcepPccLspUpdSourceType_Object = MibTableColumn
tmnxPcepPccLspUpdSourceType = _TmnxPcepPccLspUpdSourceType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3, 1, 10),
    _TmnxPcepPccLspUpdSourceType_Type()
)
tmnxPcepPccLspUpdSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdSourceType.setStatus("current")


class _TmnxPcepPccLspUpdSourceAddr_Type(InetAddress):
    """Custom type tmnxPcepPccLspUpdSourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepPccLspUpdSourceAddr_Type.__name__ = "InetAddress"
_TmnxPcepPccLspUpdSourceAddr_Object = MibTableColumn
tmnxPcepPccLspUpdSourceAddr = _TmnxPcepPccLspUpdSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3, 1, 11),
    _TmnxPcepPccLspUpdSourceAddr_Type()
)
tmnxPcepPccLspUpdSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdSourceAddr.setStatus("current")
_TmnxPcepPccLspUpdDestinationType_Type = InetAddressType
_TmnxPcepPccLspUpdDestinationType_Object = MibTableColumn
tmnxPcepPccLspUpdDestinationType = _TmnxPcepPccLspUpdDestinationType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3, 1, 12),
    _TmnxPcepPccLspUpdDestinationType_Type()
)
tmnxPcepPccLspUpdDestinationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdDestinationType.setStatus("current")


class _TmnxPcepPccLspUpdDestinationAddr_Type(InetAddress):
    """Custom type tmnxPcepPccLspUpdDestinationAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepPccLspUpdDestinationAddr_Type.__name__ = "InetAddress"
_TmnxPcepPccLspUpdDestinationAddr_Object = MibTableColumn
tmnxPcepPccLspUpdDestinationAddr = _TmnxPcepPccLspUpdDestinationAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3, 1, 13),
    _TmnxPcepPccLspUpdDestinationAddr_Type()
)
tmnxPcepPccLspUpdDestinationAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdDestinationAddr.setStatus("current")
_TmnxPcepPccLspUpdLspDelegated_Type = TruthValue
_TmnxPcepPccLspUpdLspDelegated_Object = MibTableColumn
tmnxPcepPccLspUpdLspDelegated = _TmnxPcepPccLspUpdLspDelegated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3, 1, 14),
    _TmnxPcepPccLspUpdLspDelegated_Type()
)
tmnxPcepPccLspUpdLspDelegated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdLspDelegated.setStatus("current")
_TmnxPcepPccLspUpdDelgatdPeerType_Type = InetAddressType
_TmnxPcepPccLspUpdDelgatdPeerType_Object = MibTableColumn
tmnxPcepPccLspUpdDelgatdPeerType = _TmnxPcepPccLspUpdDelgatdPeerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3, 1, 15),
    _TmnxPcepPccLspUpdDelgatdPeerType_Type()
)
tmnxPcepPccLspUpdDelgatdPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdDelgatdPeerType.setStatus("current")


class _TmnxPcepPccLspUpdDelgatdPeerAddr_Type(InetAddress):
    """Custom type tmnxPcepPccLspUpdDelgatdPeerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepPccLspUpdDelgatdPeerAddr_Type.__name__ = "InetAddress"
_TmnxPcepPccLspUpdDelgatdPeerAddr_Object = MibTableColumn
tmnxPcepPccLspUpdDelgatdPeerAddr = _TmnxPcepPccLspUpdDelgatdPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3, 1, 16),
    _TmnxPcepPccLspUpdDelgatdPeerAddr_Type()
)
tmnxPcepPccLspUpdDelgatdPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdDelgatdPeerAddr.setStatus("current")


class _TmnxPcepPccLspUpdOperState_Type(Integer32):
    """Custom type tmnxPcepPccLspUpdOperState based on Integer32"""
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
        *(("down", 0),
          ("up", 1),
          ("active", 2),
          ("goingDown", 3),
          ("goingUp", 4))
    )


_TmnxPcepPccLspUpdOperState_Type.__name__ = "Integer32"
_TmnxPcepPccLspUpdOperState_Object = MibTableColumn
tmnxPcepPccLspUpdOperState = _TmnxPcepPccLspUpdOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3, 1, 17),
    _TmnxPcepPccLspUpdOperState_Type()
)
tmnxPcepPccLspUpdOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdOperState.setStatus("current")


class _TmnxPcepPccLspUpdLspError_Type(Integer32):
    """Custom type tmnxPcepPccLspUpdLspError based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("unknownReason", 1),
          ("limitRchdForPceLsp", 2),
          ("manyPendingLspUpdate", 3),
          ("unacceptableParameters", 4),
          ("internalError", 5),
          ("lspAdminDown", 6),
          ("lspPreempted", 7),
          ("rsvpSignalingError", 8))
    )


_TmnxPcepPccLspUpdLspError_Type.__name__ = "Integer32"
_TmnxPcepPccLspUpdLspError_Object = MibTableColumn
tmnxPcepPccLspUpdLspError = _TmnxPcepPccLspUpdLspError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3, 1, 18),
    _TmnxPcepPccLspUpdLspError_Type()
)
tmnxPcepPccLspUpdLspError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdLspError.setStatus("current")


class _TmnxPcepPccLspUpdState_Type(Integer32):
    """Custom type tmnxPcepPccLspUpdState based on Integer32"""
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
        *(("notApplicable", 0),
          ("mbbInProgress", 1),
          ("mbbFail", 2),
          ("mbbSuccess", 3),
          ("updateDelegation", 4),
          ("lspDown", 5))
    )


_TmnxPcepPccLspUpdState_Type.__name__ = "Integer32"
_TmnxPcepPccLspUpdState_Object = MibTableColumn
tmnxPcepPccLspUpdState = _TmnxPcepPccLspUpdState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 1, 3, 1, 19),
    _TmnxPcepPccLspUpdState_Type()
)
tmnxPcepPccLspUpdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdState.setStatus("current")
_TmnxPcepPceStatsObjects_ObjectIdentity = ObjectIdentity
tmnxPcepPceStatsObjects = _TmnxPcepPceStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 2)
)
_TmnxPcepPeerStatsObjects_ObjectIdentity = ObjectIdentity
tmnxPcepPeerStatsObjects = _TmnxPcepPeerStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 3)
)
_TmnxPcepPeerStatsTable_Object = MibTable
tmnxPcepPeerStatsTable = _TmnxPcepPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxPcepPeerStatsTable.setStatus("current")
_TmnxPcepPeerStatsEntry_Object = MibTableRow
tmnxPcepPeerStatsEntry = _TmnxPcepPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 3, 1, 1)
)
tmnxPcepPeerStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepEntityIndex"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepPeerAddrType"),
    (0, "TIMETRA-PCEP-MIB", "tmnxPcepPeerAddr"),
)
if mibBuilder.loadTexts:
    tmnxPcepPeerStatsEntry.setStatus("current")
_TmnxPcepPeerAddrType_Type = InetAddressType
_TmnxPcepPeerAddrType_Object = MibTableColumn
tmnxPcepPeerAddrType = _TmnxPcepPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 3, 1, 1, 1),
    _TmnxPcepPeerAddrType_Type()
)
tmnxPcepPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPcepPeerAddrType.setStatus("current")


class _TmnxPcepPeerAddr_Type(InetAddress):
    """Custom type tmnxPcepPeerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxPcepPeerAddr_Type.__name__ = "InetAddress"
_TmnxPcepPeerAddr_Object = MibTableColumn
tmnxPcepPeerAddr = _TmnxPcepPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 3, 1, 1, 2),
    _TmnxPcepPeerAddr_Type()
)
tmnxPcepPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPcepPeerAddr.setStatus("current")
_TmnxPcepPeerNumPCRptSent_Type = Counter32
_TmnxPcepPeerNumPCRptSent_Object = MibTableColumn
tmnxPcepPeerNumPCRptSent = _TmnxPcepPeerNumPCRptSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 3, 1, 1, 3),
    _TmnxPcepPeerNumPCRptSent_Type()
)
tmnxPcepPeerNumPCRptSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPeerNumPCRptSent.setStatus("current")
_TmnxPcepPeerNumPCRptRcvd_Type = Counter32
_TmnxPcepPeerNumPCRptRcvd_Object = MibTableColumn
tmnxPcepPeerNumPCRptRcvd = _TmnxPcepPeerNumPCRptRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 3, 1, 1, 4),
    _TmnxPcepPeerNumPCRptRcvd_Type()
)
tmnxPcepPeerNumPCRptRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPeerNumPCRptRcvd.setStatus("current")
_TmnxPcepPeerNumPCUpdSent_Type = Counter32
_TmnxPcepPeerNumPCUpdSent_Object = MibTableColumn
tmnxPcepPeerNumPCUpdSent = _TmnxPcepPeerNumPCUpdSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 3, 1, 1, 5),
    _TmnxPcepPeerNumPCUpdSent_Type()
)
tmnxPcepPeerNumPCUpdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPeerNumPCUpdSent.setStatus("current")
_TmnxPcepPeerNumPCUpdRcvd_Type = Counter32
_TmnxPcepPeerNumPCUpdRcvd_Object = MibTableColumn
tmnxPcepPeerNumPCUpdRcvd = _TmnxPcepPeerNumPCUpdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 3, 1, 1, 6),
    _TmnxPcepPeerNumPCUpdRcvd_Type()
)
tmnxPcepPeerNumPCUpdRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPeerNumPCUpdRcvd.setStatus("current")
_TmnxPcepPeerNumRptSent_Type = Counter32
_TmnxPcepPeerNumRptSent_Object = MibTableColumn
tmnxPcepPeerNumRptSent = _TmnxPcepPeerNumRptSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 3, 1, 1, 7),
    _TmnxPcepPeerNumRptSent_Type()
)
tmnxPcepPeerNumRptSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPeerNumRptSent.setStatus("current")
_TmnxPcepPeerNumRptRcvd_Type = Counter32
_TmnxPcepPeerNumRptRcvd_Object = MibTableColumn
tmnxPcepPeerNumRptRcvd = _TmnxPcepPeerNumRptRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 3, 1, 1, 8),
    _TmnxPcepPeerNumRptRcvd_Type()
)
tmnxPcepPeerNumRptRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPeerNumRptRcvd.setStatus("current")
_TmnxPcepPeerNumPCInitSent_Type = Counter32
_TmnxPcepPeerNumPCInitSent_Object = MibTableColumn
tmnxPcepPeerNumPCInitSent = _TmnxPcepPeerNumPCInitSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 3, 1, 1, 9),
    _TmnxPcepPeerNumPCInitSent_Type()
)
tmnxPcepPeerNumPCInitSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPeerNumPCInitSent.setStatus("current")
_TmnxPcepPeerNumPCInitRcvd_Type = Counter32
_TmnxPcepPeerNumPCInitRcvd_Object = MibTableColumn
tmnxPcepPeerNumPCInitRcvd = _TmnxPcepPeerNumPCInitRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 101, 3, 3, 1, 1, 10),
    _TmnxPcepPeerNumPCInitRcvd_Type()
)
tmnxPcepPeerNumPCInitRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPcepPeerNumPCInitRcvd.setStatus("current")
_TmnxPcepNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxPcepNotifyPrefix = _TmnxPcepNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 101)
)
_TmnxPcepNotification_ObjectIdentity = ObjectIdentity
tmnxPcepNotification = _TmnxPcepNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 101, 0)
)

# Managed Objects groups

tmnxPcepTableChngdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 101, 2, 1)
)
tmnxPcepTableChngdGroup.setObjects(
      *(("TIMETRA-PCEP-MIB", "tmnxPcepEntityTableLastChanged"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccEntityTblLastChgd"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccPeerTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxPcepTableChngdGroup.setStatus("current")

tmnxPcepConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 101, 2, 2)
)
tmnxPcepConfigGroup.setObjects(
      *(("TIMETRA-PCEP-MIB", "tmnxPcepEntityRowStatus"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepEntityLastChanged"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepEntityType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepEntityAdminState"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepEntityLocalAddrType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepEntityLocalAddr"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepEntityKeepAliveInterval"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepEntityDeadTimer"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepEntityMaxUnknownMsgs"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepEntityCapability"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepEntityIsOverloaded"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepEntityLocalAddrIpv6Type"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepEntityLocalAddrIpv6"))
)
if mibBuilder.loadTexts:
    tmnxPcepConfigGroup.setStatus("current")

tmnxPcepPccConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 101, 2, 3)
)
tmnxPcepPccConfigGroup.setObjects(
      *(("TIMETRA-PCEP-MIB", "tmnxPcepPccEntityLastChanged"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccEntityAddrType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccEntityAddr"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccEntityReportPathConst"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccEntityAddrIpv6Type"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccEntityAddrIpv6"))
)
if mibBuilder.loadTexts:
    tmnxPcepPccConfigGroup.setStatus("current")

tmnxPcepPccPeerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 101, 2, 5)
)
tmnxPcepPccPeerConfigGroup.setObjects(
      *(("TIMETRA-PCEP-MIB", "tmnxPcepPccPeerRowStatus"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccPeerLastChanged"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccPeerAdminState"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccPeerOperState"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccPeerSpeakerId"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccPeerCapability"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccPeerSyncState"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccPeerIsOverloaded"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccPeerSessEstablishTime"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccPeerOperKeepAlive"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccPeerOperDeadTimer"))
)
if mibBuilder.loadTexts:
    tmnxPcepPccPeerConfigGroup.setStatus("current")

tmnxPcepPcePeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 101, 2, 6)
)
tmnxPcepPcePeerGroup.setObjects(
      *(("TIMETRA-PCEP-MIB", "tmnxPcepPcePeerPort"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPcePeerCapability"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPcePeerSyncState"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPcePeerSpeakerId"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPcePeerSessEstablishTime"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPcePeerOperKeepAlive"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPcePeerOperDeadTimer"))
)
if mibBuilder.loadTexts:
    tmnxPcepPcePeerGroup.setStatus("current")

tmnxPcepPccReqMsgInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 101, 2, 7)
)
tmnxPcepPccReqMsgInfoGroup.setObjects(
      *(("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgLspType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgTunnelId"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgLspId"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgExtTunnelIdType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgExtTunnelId"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgLspName"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgSrcAddrType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgSrcAddr"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgDstAddrType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgDstAddr"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgState"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgSvecId"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgIgpMetric"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgTeMetric"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgHopCount"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgMetricBound"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgMetricCompute"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgLclProtDesired"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgSetupPriority"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgHoldingPriority"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgExcludeAny"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgIncludeAny"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgIncludeAll"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgPriority"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgReoptimization"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgBidirectional"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgStrictLoose"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgLspBandwidth"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgMaxSrLabels"))
)
if mibBuilder.loadTexts:
    tmnxPcepPccReqMsgInfoGroup.setStatus("current")

tmnxPcepPccReqPathProfInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 101, 2, 8)
)
tmnxPcepPccReqPathProfInfoGroup.setObjects(
      *(("TIMETRA-PCEP-MIB", "tmnxPcepPccReqPathProf1"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqExtendedPathProf1"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqPathProf2"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqExtendedPathProf2"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqPathProf3"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqExtendedPathProf3"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqPathProf4"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqExtendedPathProf4"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqPathProf5"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqExtendedPathProf5"))
)
if mibBuilder.loadTexts:
    tmnxPcepPccReqPathProfInfoGroup.setStatus("current")

tmnxPcepPccLspUpdInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 101, 2, 9)
)
tmnxPcepPccLspUpdInfoGroup.setObjects(
      *(("TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdLspId"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdLspType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdTunnelId"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdExtTunnelIdType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdExtTunnelId"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdLspName"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdSenderType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdSenderAddr"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdSourceType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdSourceAddr"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdDestinationType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdDestinationAddr"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdLspDelegated"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdDelgatdPeerType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdDelgatdPeerAddr"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdOperState"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdLspError"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdState"))
)
if mibBuilder.loadTexts:
    tmnxPcepPccLspUpdInfoGroup.setStatus("current")

tmnxPcepPeerStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 101, 2, 10)
)
tmnxPcepPeerStatsGroup.setObjects(
      *(("TIMETRA-PCEP-MIB", "tmnxPcepPeerNumPCRptSent"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPeerNumPCRptRcvd"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPeerNumPCUpdSent"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPeerNumPCUpdRcvd"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPeerNumRptSent"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPeerNumRptRcvd"))
)
if mibBuilder.loadTexts:
    tmnxPcepPeerStatsGroup.setStatus("current")

tmnxPcepPccPeerObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 101, 2, 11)
)
tmnxPcepPccPeerObjectGroup.setObjects(
    ("TIMETRA-PCEP-MIB", "tmnxPcepPccPeerPreference")
)
if mibBuilder.loadTexts:
    tmnxPcepPccPeerObjectGroup.setStatus("current")

tmnxPcepPccTimerObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 101, 2, 12)
)
tmnxPcepPccTimerObjectGroup.setObjects(
      *(("TIMETRA-PCEP-MIB", "tmnxPcepPccRedelegationTimer"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccStateTimer"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccStateTimerAction"))
)
if mibBuilder.loadTexts:
    tmnxPcepPccTimerObjectGroup.setStatus("current")

tmnxPcepPccMaxSrteLspObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 101, 2, 13)
)
tmnxPcepPccMaxSrteLspObjectGroup.setObjects(
      *(("TIMETRA-PCEP-MIB", "tmnxPcepPccMaxSrtePceInitLsps"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPeerNumPCInitSent"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPeerNumPCInitRcvd"))
)
if mibBuilder.loadTexts:
    tmnxPcepPccMaxSrteLspObjectGroup.setStatus("current")

tmnxPcepPccP2mpSrTreeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 101, 2, 15)
)
tmnxPcepPccP2mpSrTreeGroup.setObjects(
      *(("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTreeAssocId"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTreeAssocType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTrAsSrcAddrType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTrAsSrcAddr"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTrOrgNdAddrType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTrCPOrgNdAddr"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTrRootAddrType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTrRootAddr"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTreeRootTreeId"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTreeCdtPathName"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTreePathInstId"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTrDlPceAddrType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTrDlPceAddr"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTreeOperStatus"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTrOriginatorAsn"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTrOrgNdAddrType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTrDiscriminator"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTreePreference"))
)
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTreeGroup.setStatus("current")

tmnxPcepPccP2mpSrTreeAdRmOdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 101, 2, 16)
)
tmnxPcepPccP2mpSrTreeAdRmOdGroup.setObjects(
      *(("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTreeAddTreeId"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTrAddRtAddrType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTrAddRtAddr"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTAdLeafAddrType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTAdLeafAddr"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTrRemoveTrId"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTrRemRtAddrType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTrRemRtAddr"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTRmLeafAddrType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTRmLeafAddr"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTreeOldTreeId"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTrOldRtAddrType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTrOldRtAddr"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTOdLeafAddrType"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTOdLeafAddr"))
)
if mibBuilder.loadTexts:
    tmnxPcepPccP2mpSrTreeAdRmOdGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxPcepCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 101, 1, 1)
)
tmnxPcepCompliance.setObjects(
      *(("TIMETRA-PCEP-MIB", "tmnxPcepTableChngdGroup"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepConfigGroup"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccConfigGroup"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccPeerConfigGroup"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPcePeerGroup"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqMsgInfoGroup"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccReqPathProfInfoGroup"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccLspUpdInfoGroup"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPeerStatsGroup"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccPeerObjectGroup"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccTimerObjectGroup"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccMaxSrteLspObjectGroup"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTreeGroup"),
        ("TIMETRA-PCEP-MIB", "tmnxPcepPccP2mpSrTreeAdRmOdGroup"))
)
if mibBuilder.loadTexts:
    tmnxPcepCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-PCEP-MIB",
    **{"TmnxPcepCapabilities": TmnxPcepCapabilities,
       "TmnxPcepLspType": TmnxPcepLspType,
       "timetraPcepMIBModule": timetraPcepMIBModule,
       "tmnxPcepConformance": tmnxPcepConformance,
       "tmnxPcepCompliances": tmnxPcepCompliances,
       "tmnxPcepCompliance": tmnxPcepCompliance,
       "tmnxPcepGroups": tmnxPcepGroups,
       "tmnxPcepTableChngdGroup": tmnxPcepTableChngdGroup,
       "tmnxPcepConfigGroup": tmnxPcepConfigGroup,
       "tmnxPcepPccConfigGroup": tmnxPcepPccConfigGroup,
       "tmnxPcepPccPeerConfigGroup": tmnxPcepPccPeerConfigGroup,
       "tmnxPcepPcePeerGroup": tmnxPcepPcePeerGroup,
       "tmnxPcepPccReqMsgInfoGroup": tmnxPcepPccReqMsgInfoGroup,
       "tmnxPcepPccReqPathProfInfoGroup": tmnxPcepPccReqPathProfInfoGroup,
       "tmnxPcepPccLspUpdInfoGroup": tmnxPcepPccLspUpdInfoGroup,
       "tmnxPcepPeerStatsGroup": tmnxPcepPeerStatsGroup,
       "tmnxPcepPccPeerObjectGroup": tmnxPcepPccPeerObjectGroup,
       "tmnxPcepPccTimerObjectGroup": tmnxPcepPccTimerObjectGroup,
       "tmnxPcepPccMaxSrteLspObjectGroup": tmnxPcepPccMaxSrteLspObjectGroup,
       "tmnxPcepPccP2mpSrTreeGroup": tmnxPcepPccP2mpSrTreeGroup,
       "tmnxPcepPccP2mpSrTreeAdRmOdGroup": tmnxPcepPccP2mpSrTreeAdRmOdGroup,
       "tmnxPcepObjects": tmnxPcepObjects,
       "tmnxPcepTableChangedObjects": tmnxPcepTableChangedObjects,
       "tmnxPcepEntityTableLastChanged": tmnxPcepEntityTableLastChanged,
       "tmnxPcepPccEntityTblLastChgd": tmnxPcepPccEntityTblLastChgd,
       "tmnxPcepPccPeerTableLastChanged": tmnxPcepPccPeerTableLastChanged,
       "tmnxPcepConfigObjects": tmnxPcepConfigObjects,
       "tmnxPcepPccConfigObjects": tmnxPcepPccConfigObjects,
       "tmnxPcepPccEntityTable": tmnxPcepPccEntityTable,
       "tmnxPcepPccEntityEntry": tmnxPcepPccEntityEntry,
       "tmnxPcepPccEntityLastChanged": tmnxPcepPccEntityLastChanged,
       "tmnxPcepPccEntityAddrType": tmnxPcepPccEntityAddrType,
       "tmnxPcepPccEntityAddr": tmnxPcepPccEntityAddr,
       "tmnxPcepPccEntityReportPathConst": tmnxPcepPccEntityReportPathConst,
       "tmnxPcepPccRedelegationTimer": tmnxPcepPccRedelegationTimer,
       "tmnxPcepPccStateTimer": tmnxPcepPccStateTimer,
       "tmnxPcepPccStateTimerAction": tmnxPcepPccStateTimerAction,
       "tmnxPcepPccMaxSrtePceInitLsps": tmnxPcepPccMaxSrtePceInitLsps,
       "tmnxPcepPccEntityAddrIpv6Type": tmnxPcepPccEntityAddrIpv6Type,
       "tmnxPcepPccEntityAddrIpv6": tmnxPcepPccEntityAddrIpv6,
       "tmnxPcepPceConfigObjects": tmnxPcepPceConfigObjects,
       "tmnxPcepEntityTable": tmnxPcepEntityTable,
       "tmnxPcepEntityEntry": tmnxPcepEntityEntry,
       "tmnxPcepEntityIndex": tmnxPcepEntityIndex,
       "tmnxPcepEntityRowStatus": tmnxPcepEntityRowStatus,
       "tmnxPcepEntityLastChanged": tmnxPcepEntityLastChanged,
       "tmnxPcepEntityType": tmnxPcepEntityType,
       "tmnxPcepEntityAdminState": tmnxPcepEntityAdminState,
       "tmnxPcepEntityLocalAddrType": tmnxPcepEntityLocalAddrType,
       "tmnxPcepEntityLocalAddr": tmnxPcepEntityLocalAddr,
       "tmnxPcepEntityKeepAliveInterval": tmnxPcepEntityKeepAliveInterval,
       "tmnxPcepEntityDeadTimer": tmnxPcepEntityDeadTimer,
       "tmnxPcepEntityMaxUnknownMsgs": tmnxPcepEntityMaxUnknownMsgs,
       "tmnxPcepEntityCapability": tmnxPcepEntityCapability,
       "tmnxPcepEntityIsOverloaded": tmnxPcepEntityIsOverloaded,
       "tmnxPcepEntityLocalAddrIpv6Type": tmnxPcepEntityLocalAddrIpv6Type,
       "tmnxPcepEntityLocalAddrIpv6": tmnxPcepEntityLocalAddrIpv6,
       "tmnxPcepPccPeerTable": tmnxPcepPccPeerTable,
       "tmnxPcepPccPeerEntry": tmnxPcepPccPeerEntry,
       "tmnxPcepPccPeerAddrType": tmnxPcepPccPeerAddrType,
       "tmnxPcepPccPeerAddr": tmnxPcepPccPeerAddr,
       "tmnxPcepPccPeerRowStatus": tmnxPcepPccPeerRowStatus,
       "tmnxPcepPccPeerLastChanged": tmnxPcepPccPeerLastChanged,
       "tmnxPcepPccPeerAdminState": tmnxPcepPccPeerAdminState,
       "tmnxPcepPccPeerOperState": tmnxPcepPccPeerOperState,
       "tmnxPcepPccPeerSpeakerId": tmnxPcepPccPeerSpeakerId,
       "tmnxPcepPccPeerCapability": tmnxPcepPccPeerCapability,
       "tmnxPcepPccPeerSyncState": tmnxPcepPccPeerSyncState,
       "tmnxPcepPccPeerIsOverloaded": tmnxPcepPccPeerIsOverloaded,
       "tmnxPcepPccPeerSessEstablishTime": tmnxPcepPccPeerSessEstablishTime,
       "tmnxPcepPccPeerOperKeepAlive": tmnxPcepPccPeerOperKeepAlive,
       "tmnxPcepPccPeerOperDeadTimer": tmnxPcepPccPeerOperDeadTimer,
       "tmnxPcepPccPeerPreference": tmnxPcepPccPeerPreference,
       "tmnxPcepPcePeerTable": tmnxPcepPcePeerTable,
       "tmnxPcepPcePeerEntry": tmnxPcepPcePeerEntry,
       "tmnxPcepPcePeerAddrType": tmnxPcepPcePeerAddrType,
       "tmnxPcepPcePeerAddr": tmnxPcepPcePeerAddr,
       "tmnxPcepPcePeerPort": tmnxPcepPcePeerPort,
       "tmnxPcepPcePeerCapability": tmnxPcepPcePeerCapability,
       "tmnxPcepPcePeerSyncState": tmnxPcepPcePeerSyncState,
       "tmnxPcepPcePeerSpeakerId": tmnxPcepPcePeerSpeakerId,
       "tmnxPcepPcePeerSessEstablishTime": tmnxPcepPcePeerSessEstablishTime,
       "tmnxPcepPcePeerOperKeepAlive": tmnxPcepPcePeerOperKeepAlive,
       "tmnxPcepPcePeerOperDeadTimer": tmnxPcepPcePeerOperDeadTimer,
       "tmnxPcepPccP2mpSrTreeTable": tmnxPcepPccP2mpSrTreeTable,
       "tmnxPcepPccP2mpSrTreeEntry": tmnxPcepPccP2mpSrTreeEntry,
       "tmnxPcepPccP2mpSrTreeAssocId": tmnxPcepPccP2mpSrTreeAssocId,
       "tmnxPcepPccP2mpSrTreeAssocType": tmnxPcepPccP2mpSrTreeAssocType,
       "tmnxPcepPccP2mpSrTrAsSrcAddrType": tmnxPcepPccP2mpSrTrAsSrcAddrType,
       "tmnxPcepPccP2mpSrTrAsSrcAddr": tmnxPcepPccP2mpSrTrAsSrcAddr,
       "tmnxPcepPccP2mpSrTrOrgNdAddrType": tmnxPcepPccP2mpSrTrOrgNdAddrType,
       "tmnxPcepPccP2mpSrTrCPOrgNdAddr": tmnxPcepPccP2mpSrTrCPOrgNdAddr,
       "tmnxPcepPccP2mpSrTrRootAddrType": tmnxPcepPccP2mpSrTrRootAddrType,
       "tmnxPcepPccP2mpSrTrRootAddr": tmnxPcepPccP2mpSrTrRootAddr,
       "tmnxPcepPccP2mpSrTreeRootTreeId": tmnxPcepPccP2mpSrTreeRootTreeId,
       "tmnxPcepPccP2mpSrTreeCdtPathName": tmnxPcepPccP2mpSrTreeCdtPathName,
       "tmnxPcepPccP2mpSrTreePathInstId": tmnxPcepPccP2mpSrTreePathInstId,
       "tmnxPcepPccP2mpSrTrDlPceAddrType": tmnxPcepPccP2mpSrTrDlPceAddrType,
       "tmnxPcepPccP2mpSrTrDlPceAddr": tmnxPcepPccP2mpSrTrDlPceAddr,
       "tmnxPcepPccP2mpSrTreeOperStatus": tmnxPcepPccP2mpSrTreeOperStatus,
       "tmnxPcepPccP2mpSrTrOriginatorAsn": tmnxPcepPccP2mpSrTrOriginatorAsn,
       "tmnxPcepPccP2mpSrTrDiscriminator": tmnxPcepPccP2mpSrTrDiscriminator,
       "tmnxPcepPccP2mpSrTreePreference": tmnxPcepPccP2mpSrTreePreference,
       "tmnxPcepPccP2mpSrTreeAddTable": tmnxPcepPccP2mpSrTreeAddTable,
       "tmnxPcepPccP2mpSrTreeAddEntry": tmnxPcepPccP2mpSrTreeAddEntry,
       "tmnxPcepPccP2mpSrTreeAddTreeId": tmnxPcepPccP2mpSrTreeAddTreeId,
       "tmnxPcepPccP2mpSrTrAddRtAddrType": tmnxPcepPccP2mpSrTrAddRtAddrType,
       "tmnxPcepPccP2mpSrTrAddRtAddr": tmnxPcepPccP2mpSrTrAddRtAddr,
       "tmnxPcepPccP2mpSrTAdLeafAddrType": tmnxPcepPccP2mpSrTAdLeafAddrType,
       "tmnxPcepPccP2mpSrTAdLeafAddr": tmnxPcepPccP2mpSrTAdLeafAddr,
       "tmnxPcepPccP2mpSrTreeRemoveTable": tmnxPcepPccP2mpSrTreeRemoveTable,
       "tmnxPcepPccP2mpSrTreeRemoveEntry": tmnxPcepPccP2mpSrTreeRemoveEntry,
       "tmnxPcepPccP2mpSrTrRemoveTrId": tmnxPcepPccP2mpSrTrRemoveTrId,
       "tmnxPcepPccP2mpSrTrRemRtAddrType": tmnxPcepPccP2mpSrTrRemRtAddrType,
       "tmnxPcepPccP2mpSrTrRemRtAddr": tmnxPcepPccP2mpSrTrRemRtAddr,
       "tmnxPcepPccP2mpSrTRmLeafAddrType": tmnxPcepPccP2mpSrTRmLeafAddrType,
       "tmnxPcepPccP2mpSrTRmLeafAddr": tmnxPcepPccP2mpSrTRmLeafAddr,
       "tmnxPcepPccP2mpSrTreeOldTable": tmnxPcepPccP2mpSrTreeOldTable,
       "tmnxPcepPccP2mpSrTreeOldEntry": tmnxPcepPccP2mpSrTreeOldEntry,
       "tmnxPcepPccP2mpSrTreeOldTreeId": tmnxPcepPccP2mpSrTreeOldTreeId,
       "tmnxPcepPccP2mpSrTrOldRtAddrType": tmnxPcepPccP2mpSrTrOldRtAddrType,
       "tmnxPcepPccP2mpSrTrOldRtAddr": tmnxPcepPccP2mpSrTrOldRtAddr,
       "tmnxPcepPccP2mpSrTOdLeafAddrType": tmnxPcepPccP2mpSrTOdLeafAddrType,
       "tmnxPcepPccP2mpSrTOdLeafAddr": tmnxPcepPccP2mpSrTOdLeafAddr,
       "tmnxPcepStatsObjects": tmnxPcepStatsObjects,
       "tmnxPcepPccStatsObjects": tmnxPcepPccStatsObjects,
       "tmnxPcepPccReqMsgInfoTable": tmnxPcepPccReqMsgInfoTable,
       "tmnxPcepPccReqMsgInfoEntry": tmnxPcepPccReqMsgInfoEntry,
       "tmnxPcepPccReqMsgRequestId": tmnxPcepPccReqMsgRequestId,
       "tmnxPcepPccReqMsgLspType": tmnxPcepPccReqMsgLspType,
       "tmnxPcepPccReqMsgTunnelId": tmnxPcepPccReqMsgTunnelId,
       "tmnxPcepPccReqMsgLspId": tmnxPcepPccReqMsgLspId,
       "tmnxPcepPccReqMsgExtTunnelIdType": tmnxPcepPccReqMsgExtTunnelIdType,
       "tmnxPcepPccReqMsgExtTunnelId": tmnxPcepPccReqMsgExtTunnelId,
       "tmnxPcepPccReqMsgLspName": tmnxPcepPccReqMsgLspName,
       "tmnxPcepPccReqMsgSrcAddrType": tmnxPcepPccReqMsgSrcAddrType,
       "tmnxPcepPccReqMsgSrcAddr": tmnxPcepPccReqMsgSrcAddr,
       "tmnxPcepPccReqMsgDstAddrType": tmnxPcepPccReqMsgDstAddrType,
       "tmnxPcepPccReqMsgDstAddr": tmnxPcepPccReqMsgDstAddr,
       "tmnxPcepPccReqMsgState": tmnxPcepPccReqMsgState,
       "tmnxPcepPccReqMsgSvecId": tmnxPcepPccReqMsgSvecId,
       "tmnxPcepPccReqMsgIgpMetric": tmnxPcepPccReqMsgIgpMetric,
       "tmnxPcepPccReqMsgTeMetric": tmnxPcepPccReqMsgTeMetric,
       "tmnxPcepPccReqMsgHopCount": tmnxPcepPccReqMsgHopCount,
       "tmnxPcepPccReqMsgMetricBound": tmnxPcepPccReqMsgMetricBound,
       "tmnxPcepPccReqMsgMetricCompute": tmnxPcepPccReqMsgMetricCompute,
       "tmnxPcepPccReqMsgLclProtDesired": tmnxPcepPccReqMsgLclProtDesired,
       "tmnxPcepPccReqMsgSetupPriority": tmnxPcepPccReqMsgSetupPriority,
       "tmnxPcepPccReqMsgHoldingPriority": tmnxPcepPccReqMsgHoldingPriority,
       "tmnxPcepPccReqMsgExcludeAny": tmnxPcepPccReqMsgExcludeAny,
       "tmnxPcepPccReqMsgIncludeAny": tmnxPcepPccReqMsgIncludeAny,
       "tmnxPcepPccReqMsgIncludeAll": tmnxPcepPccReqMsgIncludeAll,
       "tmnxPcepPccReqMsgPriority": tmnxPcepPccReqMsgPriority,
       "tmnxPcepPccReqMsgReoptimization": tmnxPcepPccReqMsgReoptimization,
       "tmnxPcepPccReqMsgBidirectional": tmnxPcepPccReqMsgBidirectional,
       "tmnxPcepPccReqMsgStrictLoose": tmnxPcepPccReqMsgStrictLoose,
       "tmnxPcepPccReqMsgLspBandwidth": tmnxPcepPccReqMsgLspBandwidth,
       "tmnxPcepPccReqMsgMaxSrLabels": tmnxPcepPccReqMsgMaxSrLabels,
       "tmnxPcepPccReqPathProfInfoTable": tmnxPcepPccReqPathProfInfoTable,
       "tmnxPcepPccReqPathProfInfoEntry": tmnxPcepPccReqPathProfInfoEntry,
       "tmnxPcepPccReqPathProf1": tmnxPcepPccReqPathProf1,
       "tmnxPcepPccReqExtendedPathProf1": tmnxPcepPccReqExtendedPathProf1,
       "tmnxPcepPccReqPathProf2": tmnxPcepPccReqPathProf2,
       "tmnxPcepPccReqExtendedPathProf2": tmnxPcepPccReqExtendedPathProf2,
       "tmnxPcepPccReqPathProf3": tmnxPcepPccReqPathProf3,
       "tmnxPcepPccReqExtendedPathProf3": tmnxPcepPccReqExtendedPathProf3,
       "tmnxPcepPccReqPathProf4": tmnxPcepPccReqPathProf4,
       "tmnxPcepPccReqExtendedPathProf4": tmnxPcepPccReqExtendedPathProf4,
       "tmnxPcepPccReqPathProf5": tmnxPcepPccReqPathProf5,
       "tmnxPcepPccReqExtendedPathProf5": tmnxPcepPccReqExtendedPathProf5,
       "tmnxPcepPccLspUpdateInfoTable": tmnxPcepPccLspUpdateInfoTable,
       "tmnxPcepPccLspUpdateInfoEntry": tmnxPcepPccLspUpdateInfoEntry,
       "tmnxPcepPccLspUpdPLspId": tmnxPcepPccLspUpdPLspId,
       "tmnxPcepPccLspUpdLspId": tmnxPcepPccLspUpdLspId,
       "tmnxPcepPccLspUpdLspType": tmnxPcepPccLspUpdLspType,
       "tmnxPcepPccLspUpdTunnelId": tmnxPcepPccLspUpdTunnelId,
       "tmnxPcepPccLspUpdExtTunnelIdType": tmnxPcepPccLspUpdExtTunnelIdType,
       "tmnxPcepPccLspUpdExtTunnelId": tmnxPcepPccLspUpdExtTunnelId,
       "tmnxPcepPccLspUpdLspName": tmnxPcepPccLspUpdLspName,
       "tmnxPcepPccLspUpdSenderType": tmnxPcepPccLspUpdSenderType,
       "tmnxPcepPccLspUpdSenderAddr": tmnxPcepPccLspUpdSenderAddr,
       "tmnxPcepPccLspUpdSourceType": tmnxPcepPccLspUpdSourceType,
       "tmnxPcepPccLspUpdSourceAddr": tmnxPcepPccLspUpdSourceAddr,
       "tmnxPcepPccLspUpdDestinationType": tmnxPcepPccLspUpdDestinationType,
       "tmnxPcepPccLspUpdDestinationAddr": tmnxPcepPccLspUpdDestinationAddr,
       "tmnxPcepPccLspUpdLspDelegated": tmnxPcepPccLspUpdLspDelegated,
       "tmnxPcepPccLspUpdDelgatdPeerType": tmnxPcepPccLspUpdDelgatdPeerType,
       "tmnxPcepPccLspUpdDelgatdPeerAddr": tmnxPcepPccLspUpdDelgatdPeerAddr,
       "tmnxPcepPccLspUpdOperState": tmnxPcepPccLspUpdOperState,
       "tmnxPcepPccLspUpdLspError": tmnxPcepPccLspUpdLspError,
       "tmnxPcepPccLspUpdState": tmnxPcepPccLspUpdState,
       "tmnxPcepPceStatsObjects": tmnxPcepPceStatsObjects,
       "tmnxPcepPeerStatsObjects": tmnxPcepPeerStatsObjects,
       "tmnxPcepPeerStatsTable": tmnxPcepPeerStatsTable,
       "tmnxPcepPeerStatsEntry": tmnxPcepPeerStatsEntry,
       "tmnxPcepPeerAddrType": tmnxPcepPeerAddrType,
       "tmnxPcepPeerAddr": tmnxPcepPeerAddr,
       "tmnxPcepPeerNumPCRptSent": tmnxPcepPeerNumPCRptSent,
       "tmnxPcepPeerNumPCRptRcvd": tmnxPcepPeerNumPCRptRcvd,
       "tmnxPcepPeerNumPCUpdSent": tmnxPcepPeerNumPCUpdSent,
       "tmnxPcepPeerNumPCUpdRcvd": tmnxPcepPeerNumPCUpdRcvd,
       "tmnxPcepPeerNumRptSent": tmnxPcepPeerNumRptSent,
       "tmnxPcepPeerNumRptRcvd": tmnxPcepPeerNumRptRcvd,
       "tmnxPcepPeerNumPCInitSent": tmnxPcepPeerNumPCInitSent,
       "tmnxPcepPeerNumPCInitRcvd": tmnxPcepPeerNumPCInitRcvd,
       "tmnxPcepNotifyPrefix": tmnxPcepNotifyPrefix,
       "tmnxPcepNotification": tmnxPcepNotification}
)
