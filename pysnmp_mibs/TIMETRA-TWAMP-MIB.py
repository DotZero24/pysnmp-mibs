# SNMP MIB module (TIMETRA-TWAMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-TWAMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:59:40 2025
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
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

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
 TTcpUdpPort,
 TmnxAdminState,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TTcpUdpPort",
    "TmnxAdminState",
    "TmnxOperState")


# MODULE-IDENTITY

timetraTwampMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 76)
)
if mibBuilder.loadTexts:
    timetraTwampMIBModule.setRevisions(
        ("2016-01-01 00:00",
         "2011-02-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxTwampSrvConnectionCount(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )



class TmnxTwampSrvSessionCount(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxTwampConformance_ObjectIdentity = ObjectIdentity
tmnxTwampConformance = _TmnxTwampConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 76)
)
_TmnxTwampComplianceObjs_ObjectIdentity = ObjectIdentity
tmnxTwampComplianceObjs = _TmnxTwampComplianceObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 76, 1)
)
_TmnxTwampGroupObjs_ObjectIdentity = ObjectIdentity
tmnxTwampGroupObjs = _TmnxTwampGroupObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 76, 2)
)
_TmnxTwampV9v0GroupObjs_ObjectIdentity = ObjectIdentity
tmnxTwampV9v0GroupObjs = _TmnxTwampV9v0GroupObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 76, 2, 1)
)
_TmnxTwampV14v0GroupObjs_ObjectIdentity = ObjectIdentity
tmnxTwampV14v0GroupObjs = _TmnxTwampV14v0GroupObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 76, 2, 2)
)
_TmnxTwampV19v0GroupObjs_ObjectIdentity = ObjectIdentity
tmnxTwampV19v0GroupObjs = _TmnxTwampV19v0GroupObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 76, 2, 3)
)
_TmnxTwampObjs_ObjectIdentity = ObjectIdentity
tmnxTwampObjs = _TmnxTwampObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76)
)
_TmnxTwampTableLastChangeObjs_ObjectIdentity = ObjectIdentity
tmnxTwampTableLastChangeObjs = _TmnxTwampTableLastChangeObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 1)
)
_TmnxTwampSrvPrefixTblLastChg_Type = TimeStamp
_TmnxTwampSrvPrefixTblLastChg_Object = MibScalar
tmnxTwampSrvPrefixTblLastChg = _TmnxTwampSrvPrefixTblLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 1, 1),
    _TmnxTwampSrvPrefixTblLastChg_Type()
)
tmnxTwampSrvPrefixTblLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvPrefixTblLastChg.setStatus("current")
_TmnxTwampConfigObjs_ObjectIdentity = ObjectIdentity
tmnxTwampConfigObjs = _TmnxTwampConfigObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 2)
)
_TmnxTwampConfigScalarObjs_ObjectIdentity = ObjectIdentity
tmnxTwampConfigScalarObjs = _TmnxTwampConfigScalarObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 2, 1)
)


class _TmnxTwampSrvAdminState_Type(TmnxAdminState):
    """Custom type tmnxTwampSrvAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxTwampSrvAdminState_Type.__name__ = "TmnxAdminState"
_TmnxTwampSrvAdminState_Object = MibScalar
tmnxTwampSrvAdminState = _TmnxTwampSrvAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 2, 1, 1),
    _TmnxTwampSrvAdminState_Type()
)
tmnxTwampSrvAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTwampSrvAdminState.setStatus("current")


class _TmnxTwampSrvInactTimeout_Type(Unsigned32):
    """Custom type tmnxTwampSrvInactTimeout based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_TmnxTwampSrvInactTimeout_Type.__name__ = "Unsigned32"
_TmnxTwampSrvInactTimeout_Object = MibScalar
tmnxTwampSrvInactTimeout = _TmnxTwampSrvInactTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 2, 1, 2),
    _TmnxTwampSrvInactTimeout_Type()
)
tmnxTwampSrvInactTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTwampSrvInactTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTwampSrvInactTimeout.setUnits("seconds")


class _TmnxTwampSrvMaxConnections_Type(TmnxTwampSrvConnectionCount):
    """Custom type tmnxTwampSrvMaxConnections based on TmnxTwampSrvConnectionCount"""
    defaultValue = 32


_TmnxTwampSrvMaxConnections_Type.__name__ = "TmnxTwampSrvConnectionCount"
_TmnxTwampSrvMaxConnections_Object = MibScalar
tmnxTwampSrvMaxConnections = _TmnxTwampSrvMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 2, 1, 3),
    _TmnxTwampSrvMaxConnections_Type()
)
tmnxTwampSrvMaxConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTwampSrvMaxConnections.setStatus("current")


class _TmnxTwampSrvMaxSessions_Type(TmnxTwampSrvSessionCount):
    """Custom type tmnxTwampSrvMaxSessions based on TmnxTwampSrvSessionCount"""
    defaultValue = 32


_TmnxTwampSrvMaxSessions_Type.__name__ = "TmnxTwampSrvSessionCount"
_TmnxTwampSrvMaxSessions_Object = MibScalar
tmnxTwampSrvMaxSessions = _TmnxTwampSrvMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 2, 1, 4),
    _TmnxTwampSrvMaxSessions_Type()
)
tmnxTwampSrvMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTwampSrvMaxSessions.setStatus("current")


class _TmnxTwampRflInactTimeout_Type(Unsigned32):
    """Custom type tmnxTwampRflInactTimeout based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_TmnxTwampRflInactTimeout_Type.__name__ = "Unsigned32"
_TmnxTwampRflInactTimeout_Object = MibScalar
tmnxTwampRflInactTimeout = _TmnxTwampRflInactTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 2, 1, 5),
    _TmnxTwampRflInactTimeout_Type()
)
tmnxTwampRflInactTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxTwampRflInactTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTwampRflInactTimeout.setUnits("seconds")
_TmnxTwampConfigTableObjs_ObjectIdentity = ObjectIdentity
tmnxTwampConfigTableObjs = _TmnxTwampConfigTableObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 2, 2)
)
_TmnxTwampSrvPrefixTable_Object = MibTable
tmnxTwampSrvPrefixTable = _TmnxTwampSrvPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxTwampSrvPrefixTable.setStatus("current")
_TmnxTwampSrvPrefixEntry_Object = MibTableRow
tmnxTwampSrvPrefixEntry = _TmnxTwampSrvPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 2, 2, 1, 1)
)
tmnxTwampSrvPrefixEntry.setIndexNames(
    (0, "TIMETRA-TWAMP-MIB", "tmnxTwampSrvPrefixAddrType"),
    (0, "TIMETRA-TWAMP-MIB", "tmnxTwampSrvPrefixAddr"),
    (0, "TIMETRA-TWAMP-MIB", "tmnxTwampSrvPrefixLen"),
)
if mibBuilder.loadTexts:
    tmnxTwampSrvPrefixEntry.setStatus("current")
_TmnxTwampSrvPrefixAddrType_Type = InetAddressType
_TmnxTwampSrvPrefixAddrType_Object = MibTableColumn
tmnxTwampSrvPrefixAddrType = _TmnxTwampSrvPrefixAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 2, 2, 1, 1, 1),
    _TmnxTwampSrvPrefixAddrType_Type()
)
tmnxTwampSrvPrefixAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTwampSrvPrefixAddrType.setStatus("current")


class _TmnxTwampSrvPrefixAddr_Type(InetAddress):
    """Custom type tmnxTwampSrvPrefixAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxTwampSrvPrefixAddr_Type.__name__ = "InetAddress"
_TmnxTwampSrvPrefixAddr_Object = MibTableColumn
tmnxTwampSrvPrefixAddr = _TmnxTwampSrvPrefixAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 2, 2, 1, 1, 2),
    _TmnxTwampSrvPrefixAddr_Type()
)
tmnxTwampSrvPrefixAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTwampSrvPrefixAddr.setStatus("current")


class _TmnxTwampSrvPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxTwampSrvPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxTwampSrvPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxTwampSrvPrefixLen_Object = MibTableColumn
tmnxTwampSrvPrefixLen = _TmnxTwampSrvPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 2, 2, 1, 1, 3),
    _TmnxTwampSrvPrefixLen_Type()
)
tmnxTwampSrvPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTwampSrvPrefixLen.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTwampSrvPrefixLen.setUnits("bits")
_TmnxTwampSrvPrefixRowStatus_Type = RowStatus
_TmnxTwampSrvPrefixRowStatus_Object = MibTableColumn
tmnxTwampSrvPrefixRowStatus = _TmnxTwampSrvPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 2, 2, 1, 1, 4),
    _TmnxTwampSrvPrefixRowStatus_Type()
)
tmnxTwampSrvPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTwampSrvPrefixRowStatus.setStatus("current")
_TmnxTwampSrvPrefixLastChg_Type = TimeStamp
_TmnxTwampSrvPrefixLastChg_Object = MibTableColumn
tmnxTwampSrvPrefixLastChg = _TmnxTwampSrvPrefixLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 2, 2, 1, 1, 5),
    _TmnxTwampSrvPrefixLastChg_Type()
)
tmnxTwampSrvPrefixLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvPrefixLastChg.setStatus("current")


class _TmnxTwampSrvPrefixDescription_Type(TItemDescription):
    """Custom type tmnxTwampSrvPrefixDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxTwampSrvPrefixDescription_Type.__name__ = "TItemDescription"
_TmnxTwampSrvPrefixDescription_Object = MibTableColumn
tmnxTwampSrvPrefixDescription = _TmnxTwampSrvPrefixDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 2, 2, 1, 1, 6),
    _TmnxTwampSrvPrefixDescription_Type()
)
tmnxTwampSrvPrefixDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTwampSrvPrefixDescription.setStatus("current")


class _TmnxTwampSrvPrefixMaxConnections_Type(TmnxTwampSrvConnectionCount):
    """Custom type tmnxTwampSrvPrefixMaxConnections based on TmnxTwampSrvConnectionCount"""
    defaultValue = 32


_TmnxTwampSrvPrefixMaxConnections_Type.__name__ = "TmnxTwampSrvConnectionCount"
_TmnxTwampSrvPrefixMaxConnections_Object = MibTableColumn
tmnxTwampSrvPrefixMaxConnections = _TmnxTwampSrvPrefixMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 2, 2, 1, 1, 7),
    _TmnxTwampSrvPrefixMaxConnections_Type()
)
tmnxTwampSrvPrefixMaxConnections.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTwampSrvPrefixMaxConnections.setStatus("current")


class _TmnxTwampSrvPrefixMaxSessions_Type(TmnxTwampSrvSessionCount):
    """Custom type tmnxTwampSrvPrefixMaxSessions based on TmnxTwampSrvSessionCount"""
    defaultValue = 32


_TmnxTwampSrvPrefixMaxSessions_Type.__name__ = "TmnxTwampSrvSessionCount"
_TmnxTwampSrvPrefixMaxSessions_Object = MibTableColumn
tmnxTwampSrvPrefixMaxSessions = _TmnxTwampSrvPrefixMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 2, 2, 1, 1, 8),
    _TmnxTwampSrvPrefixMaxSessions_Type()
)
tmnxTwampSrvPrefixMaxSessions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxTwampSrvPrefixMaxSessions.setStatus("current")
_TmnxTwampStatisticsObjs_ObjectIdentity = ObjectIdentity
tmnxTwampStatisticsObjs = _TmnxTwampStatisticsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3)
)
_TmnxTwampStatisticsScalarObjs_ObjectIdentity = ObjectIdentity
tmnxTwampStatisticsScalarObjs = _TmnxTwampStatisticsScalarObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 1)
)
_TmnxTwampSrvOperState_Type = TmnxOperState
_TmnxTwampSrvOperState_Object = MibScalar
tmnxTwampSrvOperState = _TmnxTwampSrvOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 1, 1),
    _TmnxTwampSrvOperState_Type()
)
tmnxTwampSrvOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvOperState.setStatus("current")
_TmnxTwampSrvUpTime_Type = Counter32
_TmnxTwampSrvUpTime_Object = MibScalar
tmnxTwampSrvUpTime = _TmnxTwampSrvUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 1, 2),
    _TmnxTwampSrvUpTime_Type()
)
tmnxTwampSrvUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvUpTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTwampSrvUpTime.setUnits("seconds")
_TmnxTwampSrvConnectionCount_Type = TmnxTwampSrvConnectionCount
_TmnxTwampSrvConnectionCount_Object = MibScalar
tmnxTwampSrvConnectionCount = _TmnxTwampSrvConnectionCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 1, 3),
    _TmnxTwampSrvConnectionCount_Type()
)
tmnxTwampSrvConnectionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvConnectionCount.setStatus("current")
_TmnxTwampSrvConnectionsRejected_Type = Counter32
_TmnxTwampSrvConnectionsRejected_Object = MibScalar
tmnxTwampSrvConnectionsRejected = _TmnxTwampSrvConnectionsRejected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 1, 4),
    _TmnxTwampSrvConnectionsRejected_Type()
)
tmnxTwampSrvConnectionsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvConnectionsRejected.setStatus("current")
_TmnxTwampSrvSessionCount_Type = TmnxTwampSrvSessionCount
_TmnxTwampSrvSessionCount_Object = MibScalar
tmnxTwampSrvSessionCount = _TmnxTwampSrvSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 1, 5),
    _TmnxTwampSrvSessionCount_Type()
)
tmnxTwampSrvSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvSessionCount.setStatus("current")
_TmnxTwampSrvTestSessCompleted_Type = Counter32
_TmnxTwampSrvTestSessCompleted_Object = MibScalar
tmnxTwampSrvTestSessCompleted = _TmnxTwampSrvTestSessCompleted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 1, 6),
    _TmnxTwampSrvTestSessCompleted_Type()
)
tmnxTwampSrvTestSessCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvTestSessCompleted.setStatus("current")
_TmnxTwampSrvTestSessRejected_Type = Counter32
_TmnxTwampSrvTestSessRejected_Object = MibScalar
tmnxTwampSrvTestSessRejected = _TmnxTwampSrvTestSessRejected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 1, 7),
    _TmnxTwampSrvTestSessRejected_Type()
)
tmnxTwampSrvTestSessRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvTestSessRejected.setStatus("current")
_TmnxTwampSrvTestSessAborted_Type = Counter32
_TmnxTwampSrvTestSessAborted_Object = MibScalar
tmnxTwampSrvTestSessAborted = _TmnxTwampSrvTestSessAborted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 1, 8),
    _TmnxTwampSrvTestSessAborted_Type()
)
tmnxTwampSrvTestSessAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvTestSessAborted.setStatus("current")
_TmnxTwampSrvTestPacketsRx_Type = Counter32
_TmnxTwampSrvTestPacketsRx_Object = MibScalar
tmnxTwampSrvTestPacketsRx = _TmnxTwampSrvTestPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 1, 9),
    _TmnxTwampSrvTestPacketsRx_Type()
)
tmnxTwampSrvTestPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvTestPacketsRx.setStatus("current")
_TmnxTwampSrvTestPacketsTx_Type = Counter32
_TmnxTwampSrvTestPacketsTx_Object = MibScalar
tmnxTwampSrvTestPacketsTx = _TmnxTwampSrvTestPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 1, 10),
    _TmnxTwampSrvTestPacketsTx_Type()
)
tmnxTwampSrvTestPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvTestPacketsTx.setStatus("current")


class _TmnxTwampSrvCapabilities_Type(Bits):
    """Custom type tmnxTwampSrvCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("unauthenticated", 0),
          ("authenticated", 1),
          ("encrypted", 2),
          ("unauthTestEncryptControl", 3),
          ("individualSessionControl", 4),
          ("reflectOctets", 5),
          ("symmetricalSizeSenderTestPkt", 6),
          ("ikeV2DerivedMode", 7),
          ("dscpAndEcnMonitoring", 8))
    )

_TmnxTwampSrvCapabilities_Type.__name__ = "Bits"
_TmnxTwampSrvCapabilities_Object = MibScalar
tmnxTwampSrvCapabilities = _TmnxTwampSrvCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 1, 11),
    _TmnxTwampSrvCapabilities_Type()
)
tmnxTwampSrvCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvCapabilities.setStatus("current")
_TmnxTwampStatisticsTableObjs_ObjectIdentity = ObjectIdentity
tmnxTwampStatisticsTableObjs = _TmnxTwampStatisticsTableObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2)
)
_TmnxTwampSrvPrefixStatsTable_Object = MibTable
tmnxTwampSrvPrefixStatsTable = _TmnxTwampSrvPrefixStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxTwampSrvPrefixStatsTable.setStatus("current")
_TmnxTwampSrvPrefixStatsEntry_Object = MibTableRow
tmnxTwampSrvPrefixStatsEntry = _TmnxTwampSrvPrefixStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxTwampSrvPrefixStatsEntry.setStatus("current")
_TmnxTwampSrvPfxConnCount_Type = TmnxTwampSrvConnectionCount
_TmnxTwampSrvPfxConnCount_Object = MibTableColumn
tmnxTwampSrvPfxConnCount = _TmnxTwampSrvPfxConnCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 1, 1, 1),
    _TmnxTwampSrvPfxConnCount_Type()
)
tmnxTwampSrvPfxConnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvPfxConnCount.setStatus("current")
_TmnxTwampSrvPfxConnsRejected_Type = Counter32
_TmnxTwampSrvPfxConnsRejected_Object = MibTableColumn
tmnxTwampSrvPfxConnsRejected = _TmnxTwampSrvPfxConnsRejected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 1, 1, 2),
    _TmnxTwampSrvPfxConnsRejected_Type()
)
tmnxTwampSrvPfxConnsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvPfxConnsRejected.setStatus("current")
_TmnxTwampSrvPfxSessionCount_Type = TmnxTwampSrvSessionCount
_TmnxTwampSrvPfxSessionCount_Object = MibTableColumn
tmnxTwampSrvPfxSessionCount = _TmnxTwampSrvPfxSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 1, 1, 3),
    _TmnxTwampSrvPfxSessionCount_Type()
)
tmnxTwampSrvPfxSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvPfxSessionCount.setStatus("current")
_TmnxTwampSrvPfxTestSessCompleted_Type = Counter32
_TmnxTwampSrvPfxTestSessCompleted_Object = MibTableColumn
tmnxTwampSrvPfxTestSessCompleted = _TmnxTwampSrvPfxTestSessCompleted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 1, 1, 4),
    _TmnxTwampSrvPfxTestSessCompleted_Type()
)
tmnxTwampSrvPfxTestSessCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvPfxTestSessCompleted.setStatus("current")
_TmnxTwampSrvPfxTestSessRejected_Type = Counter32
_TmnxTwampSrvPfxTestSessRejected_Object = MibTableColumn
tmnxTwampSrvPfxTestSessRejected = _TmnxTwampSrvPfxTestSessRejected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 1, 1, 5),
    _TmnxTwampSrvPfxTestSessRejected_Type()
)
tmnxTwampSrvPfxTestSessRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvPfxTestSessRejected.setStatus("current")
_TmnxTwampSrvPfxTestSessAbort_Type = Counter32
_TmnxTwampSrvPfxTestSessAbort_Object = MibTableColumn
tmnxTwampSrvPfxTestSessAbort = _TmnxTwampSrvPfxTestSessAbort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 1, 1, 6),
    _TmnxTwampSrvPfxTestSessAbort_Type()
)
tmnxTwampSrvPfxTestSessAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvPfxTestSessAbort.setStatus("current")
_TmnxTwampSrvPfxTestPacketsRx_Type = Counter32
_TmnxTwampSrvPfxTestPacketsRx_Object = MibTableColumn
tmnxTwampSrvPfxTestPacketsRx = _TmnxTwampSrvPfxTestPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 1, 1, 7),
    _TmnxTwampSrvPfxTestPacketsRx_Type()
)
tmnxTwampSrvPfxTestPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvPfxTestPacketsRx.setStatus("current")
_TmnxTwampSrvPfxTestPacketsTx_Type = Counter32
_TmnxTwampSrvPfxTestPacketsTx_Object = MibTableColumn
tmnxTwampSrvPfxTestPacketsTx = _TmnxTwampSrvPfxTestPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 1, 1, 8),
    _TmnxTwampSrvPfxTestPacketsTx_Type()
)
tmnxTwampSrvPfxTestPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvPfxTestPacketsTx.setStatus("current")
_TmnxTwampSrvConnStatsTable_Object = MibTable
tmnxTwampSrvConnStatsTable = _TmnxTwampSrvConnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxTwampSrvConnStatsTable.setStatus("current")
_TmnxTwampSrvConnStatsEntry_Object = MibTableRow
tmnxTwampSrvConnStatsEntry = _TmnxTwampSrvConnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 2, 1)
)
tmnxTwampSrvConnStatsEntry.setIndexNames(
    (0, "TIMETRA-TWAMP-MIB", "tmnxTwampSrvPrefixAddrType"),
    (0, "TIMETRA-TWAMP-MIB", "tmnxTwampSrvPrefixAddr"),
    (0, "TIMETRA-TWAMP-MIB", "tmnxTwampSrvPrefixLen"),
    (0, "TIMETRA-TWAMP-MIB", "tmnxTwampSrvConnClientAddrType"),
    (0, "TIMETRA-TWAMP-MIB", "tmnxTwampSrvConnClientAddr"),
    (0, "TIMETRA-TWAMP-MIB", "tmnxTwampSrvConnSeqNum"),
)
if mibBuilder.loadTexts:
    tmnxTwampSrvConnStatsEntry.setStatus("current")
_TmnxTwampSrvConnClientAddrType_Type = InetAddressType
_TmnxTwampSrvConnClientAddrType_Object = MibTableColumn
tmnxTwampSrvConnClientAddrType = _TmnxTwampSrvConnClientAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 2, 1, 1),
    _TmnxTwampSrvConnClientAddrType_Type()
)
tmnxTwampSrvConnClientAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTwampSrvConnClientAddrType.setStatus("current")


class _TmnxTwampSrvConnClientAddr_Type(InetAddress):
    """Custom type tmnxTwampSrvConnClientAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxTwampSrvConnClientAddr_Type.__name__ = "InetAddress"
_TmnxTwampSrvConnClientAddr_Object = MibTableColumn
tmnxTwampSrvConnClientAddr = _TmnxTwampSrvConnClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 2, 1, 2),
    _TmnxTwampSrvConnClientAddr_Type()
)
tmnxTwampSrvConnClientAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTwampSrvConnClientAddr.setStatus("current")


class _TmnxTwampSrvConnSeqNum_Type(Unsigned32):
    """Custom type tmnxTwampSrvConnSeqNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxTwampSrvConnSeqNum_Type.__name__ = "Unsigned32"
_TmnxTwampSrvConnSeqNum_Object = MibTableColumn
tmnxTwampSrvConnSeqNum = _TmnxTwampSrvConnSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 2, 1, 3),
    _TmnxTwampSrvConnSeqNum_Type()
)
tmnxTwampSrvConnSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTwampSrvConnSeqNum.setStatus("current")


class _TmnxTwampSrvConnState_Type(Integer32):
    """Custom type tmnxTwampSrvConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("settingUp", 1),
          ("ready", 2),
          ("running", 3))
    )


_TmnxTwampSrvConnState_Type.__name__ = "Integer32"
_TmnxTwampSrvConnState_Object = MibTableColumn
tmnxTwampSrvConnState = _TmnxTwampSrvConnState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 2, 1, 4),
    _TmnxTwampSrvConnState_Type()
)
tmnxTwampSrvConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvConnState.setStatus("current")
_TmnxTwampSrvConnIdleTime_Type = Unsigned32
_TmnxTwampSrvConnIdleTime_Object = MibTableColumn
tmnxTwampSrvConnIdleTime = _TmnxTwampSrvConnIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 2, 1, 5),
    _TmnxTwampSrvConnIdleTime_Type()
)
tmnxTwampSrvConnIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvConnIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxTwampSrvConnIdleTime.setUnits("seconds")
_TmnxTwampSrvConnSessionCount_Type = TmnxTwampSrvSessionCount
_TmnxTwampSrvConnSessionCount_Object = MibTableColumn
tmnxTwampSrvConnSessionCount = _TmnxTwampSrvConnSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 2, 1, 6),
    _TmnxTwampSrvConnSessionCount_Type()
)
tmnxTwampSrvConnSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvConnSessionCount.setStatus("current")
_TmnxTwampSrvConnTestSessComplete_Type = Counter32
_TmnxTwampSrvConnTestSessComplete_Object = MibTableColumn
tmnxTwampSrvConnTestSessComplete = _TmnxTwampSrvConnTestSessComplete_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 2, 1, 7),
    _TmnxTwampSrvConnTestSessComplete_Type()
)
tmnxTwampSrvConnTestSessComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvConnTestSessComplete.setStatus("current")
_TmnxTwampSrvConnTestSessRejected_Type = Counter32
_TmnxTwampSrvConnTestSessRejected_Object = MibTableColumn
tmnxTwampSrvConnTestSessRejected = _TmnxTwampSrvConnTestSessRejected_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 2, 1, 8),
    _TmnxTwampSrvConnTestSessRejected_Type()
)
tmnxTwampSrvConnTestSessRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvConnTestSessRejected.setStatus("current")
_TmnxTwampSrvConnTestPacketsRx_Type = Counter32
_TmnxTwampSrvConnTestPacketsRx_Object = MibTableColumn
tmnxTwampSrvConnTestPacketsRx = _TmnxTwampSrvConnTestPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 2, 1, 9),
    _TmnxTwampSrvConnTestPacketsRx_Type()
)
tmnxTwampSrvConnTestPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvConnTestPacketsRx.setStatus("current")
_TmnxTwampSrvConnTestPacketsTx_Type = Counter32
_TmnxTwampSrvConnTestPacketsTx_Object = MibTableColumn
tmnxTwampSrvConnTestPacketsTx = _TmnxTwampSrvConnTestPacketsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 2, 1, 10),
    _TmnxTwampSrvConnTestPacketsTx_Type()
)
tmnxTwampSrvConnTestPacketsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvConnTestPacketsTx.setStatus("current")
_TmnxTwampSrvSessStatsTable_Object = MibTable
tmnxTwampSrvSessStatsTable = _TmnxTwampSrvSessStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxTwampSrvSessStatsTable.setStatus("current")
_TmnxTwampSrvSessStatsEntry_Object = MibTableRow
tmnxTwampSrvSessStatsEntry = _TmnxTwampSrvSessStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 3, 1)
)
tmnxTwampSrvSessStatsEntry.setIndexNames(
    (0, "TIMETRA-TWAMP-MIB", "tmnxTwampSrvConnClientAddrType"),
    (0, "TIMETRA-TWAMP-MIB", "tmnxTwampSrvConnClientAddr"),
    (0, "TIMETRA-TWAMP-MIB", "tmnxTwampSrvConnSeqNum"),
    (0, "TIMETRA-TWAMP-MIB", "tmnxTwampSrvSessSeqNum"),
)
if mibBuilder.loadTexts:
    tmnxTwampSrvSessStatsEntry.setStatus("current")


class _TmnxTwampSrvSessSeqNum_Type(Unsigned32):
    """Custom type tmnxTwampSrvSessSeqNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxTwampSrvSessSeqNum_Type.__name__ = "Unsigned32"
_TmnxTwampSrvSessSeqNum_Object = MibTableColumn
tmnxTwampSrvSessSeqNum = _TmnxTwampSrvSessSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 3, 1, 1),
    _TmnxTwampSrvSessSeqNum_Type()
)
tmnxTwampSrvSessSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxTwampSrvSessSeqNum.setStatus("current")


class _TmnxTwampSrvSessID_Type(OctetString):
    """Custom type tmnxTwampSrvSessID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TmnxTwampSrvSessID_Type.__name__ = "OctetString"
_TmnxTwampSrvSessID_Object = MibTableColumn
tmnxTwampSrvSessID = _TmnxTwampSrvSessID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 3, 1, 2),
    _TmnxTwampSrvSessID_Type()
)
tmnxTwampSrvSessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvSessID.setStatus("current")


class _TmnxTwampSrvSessOperState_Type(Integer32):
    """Custom type tmnxTwampSrvSessOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("active", 2),
          ("stop", 3))
    )


_TmnxTwampSrvSessOperState_Type.__name__ = "Integer32"
_TmnxTwampSrvSessOperState_Object = MibTableColumn
tmnxTwampSrvSessOperState = _TmnxTwampSrvSessOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 3, 1, 3),
    _TmnxTwampSrvSessOperState_Type()
)
tmnxTwampSrvSessOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvSessOperState.setStatus("current")
_TmnxTwampSrvSessSenderAddrType_Type = InetAddressType
_TmnxTwampSrvSessSenderAddrType_Object = MibTableColumn
tmnxTwampSrvSessSenderAddrType = _TmnxTwampSrvSessSenderAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 3, 1, 4),
    _TmnxTwampSrvSessSenderAddrType_Type()
)
tmnxTwampSrvSessSenderAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvSessSenderAddrType.setStatus("current")


class _TmnxTwampSrvSessSenderAddress_Type(InetAddress):
    """Custom type tmnxTwampSrvSessSenderAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxTwampSrvSessSenderAddress_Type.__name__ = "InetAddress"
_TmnxTwampSrvSessSenderAddress_Object = MibTableColumn
tmnxTwampSrvSessSenderAddress = _TmnxTwampSrvSessSenderAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 3, 1, 5),
    _TmnxTwampSrvSessSenderAddress_Type()
)
tmnxTwampSrvSessSenderAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvSessSenderAddress.setStatus("current")
_TmnxTwampSrvSessSenderUdpPort_Type = InetPortNumber
_TmnxTwampSrvSessSenderUdpPort_Object = MibTableColumn
tmnxTwampSrvSessSenderUdpPort = _TmnxTwampSrvSessSenderUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 3, 1, 6),
    _TmnxTwampSrvSessSenderUdpPort_Type()
)
tmnxTwampSrvSessSenderUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvSessSenderUdpPort.setStatus("current")
_TmnxTwampSrvSessReflectorAddrTyp_Type = InetAddressType
_TmnxTwampSrvSessReflectorAddrTyp_Object = MibTableColumn
tmnxTwampSrvSessReflectorAddrTyp = _TmnxTwampSrvSessReflectorAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 3, 1, 7),
    _TmnxTwampSrvSessReflectorAddrTyp_Type()
)
tmnxTwampSrvSessReflectorAddrTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvSessReflectorAddrTyp.setStatus("current")


class _TmnxTwampSrvSessReflectorAddress_Type(InetAddress):
    """Custom type tmnxTwampSrvSessReflectorAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxTwampSrvSessReflectorAddress_Type.__name__ = "InetAddress"
_TmnxTwampSrvSessReflectorAddress_Object = MibTableColumn
tmnxTwampSrvSessReflectorAddress = _TmnxTwampSrvSessReflectorAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 3, 1, 8),
    _TmnxTwampSrvSessReflectorAddress_Type()
)
tmnxTwampSrvSessReflectorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvSessReflectorAddress.setStatus("current")
_TmnxTwampSrvSessReflectorUdpPort_Type = InetPortNumber
_TmnxTwampSrvSessReflectorUdpPort_Object = MibTableColumn
tmnxTwampSrvSessReflectorUdpPort = _TmnxTwampSrvSessReflectorUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 3, 2, 3, 1, 9),
    _TmnxTwampSrvSessReflectorUdpPort_Type()
)
tmnxTwampSrvSessReflectorUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxTwampSrvSessReflectorUdpPort.setStatus("current")
_TmnxTwampNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxTwampNotificationObjs = _TmnxTwampNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 4)
)
_TmnxTwampSrvNotifClientAddrType_Type = InetAddressType
_TmnxTwampSrvNotifClientAddrType_Object = MibScalar
tmnxTwampSrvNotifClientAddrType = _TmnxTwampSrvNotifClientAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 4, 1),
    _TmnxTwampSrvNotifClientAddrType_Type()
)
tmnxTwampSrvNotifClientAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTwampSrvNotifClientAddrType.setStatus("current")


class _TmnxTwampSrvNotifClientAddr_Type(InetAddress):
    """Custom type tmnxTwampSrvNotifClientAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxTwampSrvNotifClientAddr_Type.__name__ = "InetAddress"
_TmnxTwampSrvNotifClientAddr_Object = MibScalar
tmnxTwampSrvNotifClientAddr = _TmnxTwampSrvNotifClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 4, 2),
    _TmnxTwampSrvNotifClientAddr_Type()
)
tmnxTwampSrvNotifClientAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTwampSrvNotifClientAddr.setStatus("current")
_TmnxTwampRflNotifLocalAddrType_Type = InetAddressType
_TmnxTwampRflNotifLocalAddrType_Object = MibScalar
tmnxTwampRflNotifLocalAddrType = _TmnxTwampRflNotifLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 4, 3),
    _TmnxTwampRflNotifLocalAddrType_Type()
)
tmnxTwampRflNotifLocalAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTwampRflNotifLocalAddrType.setStatus("current")


class _TmnxTwampRflNotifLocalAddr_Type(InetAddress):
    """Custom type tmnxTwampRflNotifLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxTwampRflNotifLocalAddr_Type.__name__ = "InetAddress"
_TmnxTwampRflNotifLocalAddr_Object = MibScalar
tmnxTwampRflNotifLocalAddr = _TmnxTwampRflNotifLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 4, 4),
    _TmnxTwampRflNotifLocalAddr_Type()
)
tmnxTwampRflNotifLocalAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTwampRflNotifLocalAddr.setStatus("current")
_TmnxTwampRflNotifLocalUdpPort_Type = TTcpUdpPort
_TmnxTwampRflNotifLocalUdpPort_Object = MibScalar
tmnxTwampRflNotifLocalUdpPort = _TmnxTwampRflNotifLocalUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 4, 5),
    _TmnxTwampRflNotifLocalUdpPort_Type()
)
tmnxTwampRflNotifLocalUdpPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTwampRflNotifLocalUdpPort.setStatus("current")
_TmnxTwampRflNotifRemoteAddrType_Type = InetAddressType
_TmnxTwampRflNotifRemoteAddrType_Object = MibScalar
tmnxTwampRflNotifRemoteAddrType = _TmnxTwampRflNotifRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 4, 6),
    _TmnxTwampRflNotifRemoteAddrType_Type()
)
tmnxTwampRflNotifRemoteAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTwampRflNotifRemoteAddrType.setStatus("current")


class _TmnxTwampRflNotifRemoteAddr_Type(InetAddress):
    """Custom type tmnxTwampRflNotifRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxTwampRflNotifRemoteAddr_Type.__name__ = "InetAddress"
_TmnxTwampRflNotifRemoteAddr_Object = MibScalar
tmnxTwampRflNotifRemoteAddr = _TmnxTwampRflNotifRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 4, 7),
    _TmnxTwampRflNotifRemoteAddr_Type()
)
tmnxTwampRflNotifRemoteAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTwampRflNotifRemoteAddr.setStatus("current")
_TmnxTwampRflNotifRemoteUdpPort_Type = TTcpUdpPort
_TmnxTwampRflNotifRemoteUdpPort_Object = MibScalar
tmnxTwampRflNotifRemoteUdpPort = _TmnxTwampRflNotifRemoteUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 76, 4, 8),
    _TmnxTwampRflNotifRemoteUdpPort_Type()
)
tmnxTwampRflNotifRemoteUdpPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxTwampRflNotifRemoteUdpPort.setStatus("current")
_TmnxTwampNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxTwampNotifyPrefix = _TmnxTwampNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 76)
)
_TmnxTwampNotifications_ObjectIdentity = ObjectIdentity
tmnxTwampNotifications = _TmnxTwampNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 76, 0)
)
tmnxTwampSrvPrefixEntry.registerAugmentions(
    ("TIMETRA-TWAMP-MIB",
     "tmnxTwampSrvPrefixStatsEntry")
)
tmnxTwampSrvPrefixStatsEntry.setIndexNames(*tmnxTwampSrvPrefixEntry.getIndexNames())

# Managed Objects groups

tmnxTwampSrvV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 76, 2, 1, 1)
)
tmnxTwampSrvV9v0Group.setObjects(
      *(("TIMETRA-TWAMP-MIB", "tmnxTwampSrvAdminState"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvInactTimeout"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvMaxConnections"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvMaxSessions"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvPrefixTblLastChg"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvPrefixRowStatus"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvPrefixLastChg"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvPrefixDescription"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvPrefixMaxConnections"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvPrefixMaxSessions"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvOperState"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvUpTime"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvConnectionCount"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvConnectionsRejected"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvSessionCount"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvTestSessCompleted"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvTestSessRejected"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvTestSessAborted"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvTestPacketsRx"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvTestPacketsTx"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvPfxConnCount"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvPfxConnsRejected"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvPfxSessionCount"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvPfxTestSessCompleted"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvPfxTestSessRejected"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvPfxTestSessAbort"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvPfxTestPacketsRx"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvPfxTestPacketsTx"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvConnState"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvConnIdleTime"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvConnSessionCount"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvConnTestSessComplete"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvConnTestSessRejected"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvConnTestPacketsRx"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvConnTestPacketsTx"))
)
if mibBuilder.loadTexts:
    tmnxTwampSrvV9v0Group.setStatus("current")

tmnxTwampSrvNotifyObjsV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 76, 2, 1, 3)
)
tmnxTwampSrvNotifyObjsV9v0Group.setObjects(
      *(("TIMETRA-TWAMP-MIB", "tmnxTwampSrvNotifClientAddrType"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvNotifClientAddr"))
)
if mibBuilder.loadTexts:
    tmnxTwampSrvNotifyObjsV9v0Group.setStatus("current")

tmnxTwampSrvV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 76, 2, 2, 1)
)
tmnxTwampSrvV14v0Group.setObjects(
      *(("TIMETRA-TWAMP-MIB", "tmnxTwampSrvCapabilities"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvSessID"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvSessOperState"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvSessReflectorAddrTyp"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvSessReflectorAddress"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvSessReflectorUdpPort"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvSessSenderAddrType"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvSessSenderAddress"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvSessSenderUdpPort"))
)
if mibBuilder.loadTexts:
    tmnxTwampSrvV14v0Group.setStatus("current")

tmnxTwampRflInactivityV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 76, 2, 3, 1)
)
tmnxTwampRflInactivityV19v0Group.setObjects(
    ("TIMETRA-TWAMP-MIB", "tmnxTwampRflInactTimeout")
)
if mibBuilder.loadTexts:
    tmnxTwampRflInactivityV19v0Group.setStatus("current")

tmnxTwampRflInNotifyObjsV19v0Grp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 76, 2, 3, 3)
)
tmnxTwampRflInNotifyObjsV19v0Grp.setObjects(
      *(("TIMETRA-TWAMP-MIB", "tmnxTwampRflNotifLocalAddr"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampRflNotifLocalAddrType"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampRflNotifLocalUdpPort"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampRflNotifRemoteAddr"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampRflNotifRemoteAddrType"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampRflNotifRemoteUdpPort"))
)
if mibBuilder.loadTexts:
    tmnxTwampRflInNotifyObjsV19v0Grp.setStatus("current")


# Notification objects

tmnxTwampSrvInactivityTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 76, 0, 1)
)
tmnxTwampSrvInactivityTimeout.setObjects(
    ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvConnIdleTime")
)
if mibBuilder.loadTexts:
    tmnxTwampSrvInactivityTimeout.setStatus(
        "current"
    )

tmnxTwampSrvMaxConnsExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 76, 0, 2)
)
tmnxTwampSrvMaxConnsExceeded.setObjects(
      *(("TIMETRA-TWAMP-MIB", "tmnxTwampSrvConnectionCount"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvNotifClientAddrType"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvNotifClientAddr"))
)
if mibBuilder.loadTexts:
    tmnxTwampSrvMaxConnsExceeded.setStatus(
        "current"
    )

tmnxTwampSrvPfxMaxConnsExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 76, 0, 3)
)
tmnxTwampSrvPfxMaxConnsExceeded.setObjects(
      *(("TIMETRA-TWAMP-MIB", "tmnxTwampSrvPfxConnCount"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvNotifClientAddrType"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvNotifClientAddr"))
)
if mibBuilder.loadTexts:
    tmnxTwampSrvPfxMaxConnsExceeded.setStatus(
        "current"
    )

tmnxTwampSrvMaxSessExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 76, 0, 4)
)
tmnxTwampSrvMaxSessExceeded.setObjects(
      *(("TIMETRA-TWAMP-MIB", "tmnxTwampSrvSessionCount"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvNotifClientAddrType"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvNotifClientAddr"))
)
if mibBuilder.loadTexts:
    tmnxTwampSrvMaxSessExceeded.setStatus(
        "current"
    )

tmnxTwampSrvPfxMaxSessExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 76, 0, 5)
)
tmnxTwampSrvPfxMaxSessExceeded.setObjects(
      *(("TIMETRA-TWAMP-MIB", "tmnxTwampSrvPfxSessionCount"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvNotifClientAddrType"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvNotifClientAddr"))
)
if mibBuilder.loadTexts:
    tmnxTwampSrvPfxMaxSessExceeded.setStatus(
        "current"
    )

tmnxTwampRflInactivityTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 76, 0, 6)
)
tmnxTwampRflInactivityTimeout.setObjects(
      *(("TIMETRA-TWAMP-MIB", "tmnxTwampSrvNotifClientAddrType"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvNotifClientAddr"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampRflNotifLocalAddrType"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampRflNotifLocalAddr"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampRflNotifLocalUdpPort"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampRflNotifRemoteAddrType"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampRflNotifRemoteAddr"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampRflNotifRemoteUdpPort"))
)
if mibBuilder.loadTexts:
    tmnxTwampRflInactivityTimeout.setStatus(
        "current"
    )


# Notifications groups

tmnxTwampSrvNotifyV9v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 76, 2, 1, 2)
)
tmnxTwampSrvNotifyV9v0Group.setObjects(
      *(("TIMETRA-TWAMP-MIB", "tmnxTwampSrvInactivityTimeout"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvMaxConnsExceeded"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvPfxMaxConnsExceeded"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvMaxSessExceeded"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvPfxMaxSessExceeded"))
)
if mibBuilder.loadTexts:
    tmnxTwampSrvNotifyV9v0Group.setStatus(
        "current"
    )

tmnxTwampRflInactNotifV19v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 76, 2, 3, 2)
)
tmnxTwampRflInactNotifV19v0Group.setObjects(
    ("TIMETRA-TWAMP-MIB", "tmnxTwampRflInactivityTimeout")
)
if mibBuilder.loadTexts:
    tmnxTwampRflInactNotifV19v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxTwampCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 76, 1, 1)
)
tmnxTwampCompliance.setObjects(
      *(("TIMETRA-TWAMP-MIB", "tmnxTwampRflInactNotifV19v0Group"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvNotifyV9v0Group"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampRflInNotifyObjsV19v0Grp"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampRflInactivityV19v0Group"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvNotifyObjsV9v0Group"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvV14v0Group"),
        ("TIMETRA-TWAMP-MIB", "tmnxTwampSrvV9v0Group"))
)
if mibBuilder.loadTexts:
    tmnxTwampCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-TWAMP-MIB",
    **{"TmnxTwampSrvConnectionCount": TmnxTwampSrvConnectionCount,
       "TmnxTwampSrvSessionCount": TmnxTwampSrvSessionCount,
       "timetraTwampMIBModule": timetraTwampMIBModule,
       "tmnxTwampConformance": tmnxTwampConformance,
       "tmnxTwampComplianceObjs": tmnxTwampComplianceObjs,
       "tmnxTwampCompliance": tmnxTwampCompliance,
       "tmnxTwampGroupObjs": tmnxTwampGroupObjs,
       "tmnxTwampV9v0GroupObjs": tmnxTwampV9v0GroupObjs,
       "tmnxTwampSrvV9v0Group": tmnxTwampSrvV9v0Group,
       "tmnxTwampSrvNotifyV9v0Group": tmnxTwampSrvNotifyV9v0Group,
       "tmnxTwampSrvNotifyObjsV9v0Group": tmnxTwampSrvNotifyObjsV9v0Group,
       "tmnxTwampV14v0GroupObjs": tmnxTwampV14v0GroupObjs,
       "tmnxTwampSrvV14v0Group": tmnxTwampSrvV14v0Group,
       "tmnxTwampV19v0GroupObjs": tmnxTwampV19v0GroupObjs,
       "tmnxTwampRflInactivityV19v0Group": tmnxTwampRflInactivityV19v0Group,
       "tmnxTwampRflInactNotifV19v0Group": tmnxTwampRflInactNotifV19v0Group,
       "tmnxTwampRflInNotifyObjsV19v0Grp": tmnxTwampRflInNotifyObjsV19v0Grp,
       "tmnxTwampObjs": tmnxTwampObjs,
       "tmnxTwampTableLastChangeObjs": tmnxTwampTableLastChangeObjs,
       "tmnxTwampSrvPrefixTblLastChg": tmnxTwampSrvPrefixTblLastChg,
       "tmnxTwampConfigObjs": tmnxTwampConfigObjs,
       "tmnxTwampConfigScalarObjs": tmnxTwampConfigScalarObjs,
       "tmnxTwampSrvAdminState": tmnxTwampSrvAdminState,
       "tmnxTwampSrvInactTimeout": tmnxTwampSrvInactTimeout,
       "tmnxTwampSrvMaxConnections": tmnxTwampSrvMaxConnections,
       "tmnxTwampSrvMaxSessions": tmnxTwampSrvMaxSessions,
       "tmnxTwampRflInactTimeout": tmnxTwampRflInactTimeout,
       "tmnxTwampConfigTableObjs": tmnxTwampConfigTableObjs,
       "tmnxTwampSrvPrefixTable": tmnxTwampSrvPrefixTable,
       "tmnxTwampSrvPrefixEntry": tmnxTwampSrvPrefixEntry,
       "tmnxTwampSrvPrefixAddrType": tmnxTwampSrvPrefixAddrType,
       "tmnxTwampSrvPrefixAddr": tmnxTwampSrvPrefixAddr,
       "tmnxTwampSrvPrefixLen": tmnxTwampSrvPrefixLen,
       "tmnxTwampSrvPrefixRowStatus": tmnxTwampSrvPrefixRowStatus,
       "tmnxTwampSrvPrefixLastChg": tmnxTwampSrvPrefixLastChg,
       "tmnxTwampSrvPrefixDescription": tmnxTwampSrvPrefixDescription,
       "tmnxTwampSrvPrefixMaxConnections": tmnxTwampSrvPrefixMaxConnections,
       "tmnxTwampSrvPrefixMaxSessions": tmnxTwampSrvPrefixMaxSessions,
       "tmnxTwampStatisticsObjs": tmnxTwampStatisticsObjs,
       "tmnxTwampStatisticsScalarObjs": tmnxTwampStatisticsScalarObjs,
       "tmnxTwampSrvOperState": tmnxTwampSrvOperState,
       "tmnxTwampSrvUpTime": tmnxTwampSrvUpTime,
       "tmnxTwampSrvConnectionCount": tmnxTwampSrvConnectionCount,
       "tmnxTwampSrvConnectionsRejected": tmnxTwampSrvConnectionsRejected,
       "tmnxTwampSrvSessionCount": tmnxTwampSrvSessionCount,
       "tmnxTwampSrvTestSessCompleted": tmnxTwampSrvTestSessCompleted,
       "tmnxTwampSrvTestSessRejected": tmnxTwampSrvTestSessRejected,
       "tmnxTwampSrvTestSessAborted": tmnxTwampSrvTestSessAborted,
       "tmnxTwampSrvTestPacketsRx": tmnxTwampSrvTestPacketsRx,
       "tmnxTwampSrvTestPacketsTx": tmnxTwampSrvTestPacketsTx,
       "tmnxTwampSrvCapabilities": tmnxTwampSrvCapabilities,
       "tmnxTwampStatisticsTableObjs": tmnxTwampStatisticsTableObjs,
       "tmnxTwampSrvPrefixStatsTable": tmnxTwampSrvPrefixStatsTable,
       "tmnxTwampSrvPrefixStatsEntry": tmnxTwampSrvPrefixStatsEntry,
       "tmnxTwampSrvPfxConnCount": tmnxTwampSrvPfxConnCount,
       "tmnxTwampSrvPfxConnsRejected": tmnxTwampSrvPfxConnsRejected,
       "tmnxTwampSrvPfxSessionCount": tmnxTwampSrvPfxSessionCount,
       "tmnxTwampSrvPfxTestSessCompleted": tmnxTwampSrvPfxTestSessCompleted,
       "tmnxTwampSrvPfxTestSessRejected": tmnxTwampSrvPfxTestSessRejected,
       "tmnxTwampSrvPfxTestSessAbort": tmnxTwampSrvPfxTestSessAbort,
       "tmnxTwampSrvPfxTestPacketsRx": tmnxTwampSrvPfxTestPacketsRx,
       "tmnxTwampSrvPfxTestPacketsTx": tmnxTwampSrvPfxTestPacketsTx,
       "tmnxTwampSrvConnStatsTable": tmnxTwampSrvConnStatsTable,
       "tmnxTwampSrvConnStatsEntry": tmnxTwampSrvConnStatsEntry,
       "tmnxTwampSrvConnClientAddrType": tmnxTwampSrvConnClientAddrType,
       "tmnxTwampSrvConnClientAddr": tmnxTwampSrvConnClientAddr,
       "tmnxTwampSrvConnSeqNum": tmnxTwampSrvConnSeqNum,
       "tmnxTwampSrvConnState": tmnxTwampSrvConnState,
       "tmnxTwampSrvConnIdleTime": tmnxTwampSrvConnIdleTime,
       "tmnxTwampSrvConnSessionCount": tmnxTwampSrvConnSessionCount,
       "tmnxTwampSrvConnTestSessComplete": tmnxTwampSrvConnTestSessComplete,
       "tmnxTwampSrvConnTestSessRejected": tmnxTwampSrvConnTestSessRejected,
       "tmnxTwampSrvConnTestPacketsRx": tmnxTwampSrvConnTestPacketsRx,
       "tmnxTwampSrvConnTestPacketsTx": tmnxTwampSrvConnTestPacketsTx,
       "tmnxTwampSrvSessStatsTable": tmnxTwampSrvSessStatsTable,
       "tmnxTwampSrvSessStatsEntry": tmnxTwampSrvSessStatsEntry,
       "tmnxTwampSrvSessSeqNum": tmnxTwampSrvSessSeqNum,
       "tmnxTwampSrvSessID": tmnxTwampSrvSessID,
       "tmnxTwampSrvSessOperState": tmnxTwampSrvSessOperState,
       "tmnxTwampSrvSessSenderAddrType": tmnxTwampSrvSessSenderAddrType,
       "tmnxTwampSrvSessSenderAddress": tmnxTwampSrvSessSenderAddress,
       "tmnxTwampSrvSessSenderUdpPort": tmnxTwampSrvSessSenderUdpPort,
       "tmnxTwampSrvSessReflectorAddrTyp": tmnxTwampSrvSessReflectorAddrTyp,
       "tmnxTwampSrvSessReflectorAddress": tmnxTwampSrvSessReflectorAddress,
       "tmnxTwampSrvSessReflectorUdpPort": tmnxTwampSrvSessReflectorUdpPort,
       "tmnxTwampNotificationObjs": tmnxTwampNotificationObjs,
       "tmnxTwampSrvNotifClientAddrType": tmnxTwampSrvNotifClientAddrType,
       "tmnxTwampSrvNotifClientAddr": tmnxTwampSrvNotifClientAddr,
       "tmnxTwampRflNotifLocalAddrType": tmnxTwampRflNotifLocalAddrType,
       "tmnxTwampRflNotifLocalAddr": tmnxTwampRflNotifLocalAddr,
       "tmnxTwampRflNotifLocalUdpPort": tmnxTwampRflNotifLocalUdpPort,
       "tmnxTwampRflNotifRemoteAddrType": tmnxTwampRflNotifRemoteAddrType,
       "tmnxTwampRflNotifRemoteAddr": tmnxTwampRflNotifRemoteAddr,
       "tmnxTwampRflNotifRemoteUdpPort": tmnxTwampRflNotifRemoteUdpPort,
       "tmnxTwampNotifyPrefix": tmnxTwampNotifyPrefix,
       "tmnxTwampNotifications": tmnxTwampNotifications,
       "tmnxTwampSrvInactivityTimeout": tmnxTwampSrvInactivityTimeout,
       "tmnxTwampSrvMaxConnsExceeded": tmnxTwampSrvMaxConnsExceeded,
       "tmnxTwampSrvPfxMaxConnsExceeded": tmnxTwampSrvPfxMaxConnsExceeded,
       "tmnxTwampSrvMaxSessExceeded": tmnxTwampSrvMaxSessExceeded,
       "tmnxTwampSrvPfxMaxSessExceeded": tmnxTwampSrvPfxMaxSessExceeded,
       "tmnxTwampRflInactivityTimeout": tmnxTwampRflInactivityTimeout}
)
