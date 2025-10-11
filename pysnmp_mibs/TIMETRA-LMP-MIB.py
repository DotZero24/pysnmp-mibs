# SNMP MIB module (TIMETRA-LMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-LMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:02:07 2025
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(TNamedItemOrEmpty,
 TmnxAdminState,
 TmnxPortID,
 TmnxVRtrID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TNamedItemOrEmpty",
    "TmnxAdminState",
    "TmnxPortID",
    "TmnxVRtrID")

(vRtrID,) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID")


# MODULE-IDENTITY

timetraLmpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 100)
)
if mibBuilder.loadTexts:
    timetraLmpMIBModule.setRevisions(
        ("2017-01-01 00:00",
         "2014-04-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxLmpConformance_ObjectIdentity = ObjectIdentity
tmnxLmpConformance = _TmnxLmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 100)
)
_TmnxLmpCompliances_ObjectIdentity = ObjectIdentity
tmnxLmpCompliances = _TmnxLmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 100, 1)
)
_TmnxLmpGroups_ObjectIdentity = ObjectIdentity
tmnxLmpGroups = _TmnxLmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 100, 2)
)
_TmnxLmpV13v0Groups_ObjectIdentity = ObjectIdentity
tmnxLmpV13v0Groups = _TmnxLmpV13v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 100, 2, 1)
)
_TmnxLmpV15v0Groups_ObjectIdentity = ObjectIdentity
tmnxLmpV15v0Groups = _TmnxLmpV15v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 100, 2, 2)
)
_TmnxLmpObjs_ObjectIdentity = ObjectIdentity
tmnxLmpObjs = _TmnxLmpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100)
)
_TmnxLmpConfigTimeStamps_ObjectIdentity = ObjectIdentity
tmnxLmpConfigTimeStamps = _TmnxLmpConfigTimeStamps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 1)
)
_TmnxLmpVRtrTableLastChanged_Type = TimeStamp
_TmnxLmpVRtrTableLastChanged_Object = MibScalar
tmnxLmpVRtrTableLastChanged = _TmnxLmpVRtrTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 1, 1),
    _TmnxLmpVRtrTableLastChanged_Type()
)
tmnxLmpVRtrTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrTableLastChanged.setStatus("current")
_TmnxLmpVRtrPeerTableLastChanged_Type = TimeStamp
_TmnxLmpVRtrPeerTableLastChanged_Object = MibScalar
tmnxLmpVRtrPeerTableLastChanged = _TmnxLmpVRtrPeerTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 1, 2),
    _TmnxLmpVRtrPeerTableLastChanged_Type()
)
tmnxLmpVRtrPeerTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrPeerTableLastChanged.setStatus("current")
_TmnxLmpVRtrCcTableLastChanged_Type = TimeStamp
_TmnxLmpVRtrCcTableLastChanged_Object = MibScalar
tmnxLmpVRtrCcTableLastChanged = _TmnxLmpVRtrCcTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 1, 3),
    _TmnxLmpVRtrCcTableLastChanged_Type()
)
tmnxLmpVRtrCcTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcTableLastChanged.setStatus("current")
_TmnxLmpVRtrTeLinkTableLastChange_Type = TimeStamp
_TmnxLmpVRtrTeLinkTableLastChange_Object = MibScalar
tmnxLmpVRtrTeLinkTableLastChange = _TmnxLmpVRtrTeLinkTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 1, 4),
    _TmnxLmpVRtrTeLinkTableLastChange_Type()
)
tmnxLmpVRtrTeLinkTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkTableLastChange.setStatus("current")
_TmnxLmpVRtrDbLinkTableLastChange_Type = TimeStamp
_TmnxLmpVRtrDbLinkTableLastChange_Object = MibScalar
tmnxLmpVRtrDbLinkTableLastChange = _TmnxLmpVRtrDbLinkTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 1, 5),
    _TmnxLmpVRtrDbLinkTableLastChange_Type()
)
tmnxLmpVRtrDbLinkTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrDbLinkTableLastChange.setStatus("current")
_TmnxLmpConfigurations_ObjectIdentity = ObjectIdentity
tmnxLmpConfigurations = _TmnxLmpConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2)
)
_TmnxLmpVRtrTable_Object = MibTable
tmnxLmpVRtrTable = _TmnxLmpVRtrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrTable.setStatus("current")
_TmnxLmpVRtrEntry_Object = MibTableRow
tmnxLmpVRtrEntry = _TmnxLmpVRtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 1, 1)
)
tmnxLmpVRtrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrEntry.setStatus("current")
_TmnxLmpVRtrRowStatus_Type = RowStatus
_TmnxLmpVRtrRowStatus_Object = MibTableColumn
tmnxLmpVRtrRowStatus = _TmnxLmpVRtrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 1, 1, 1),
    _TmnxLmpVRtrRowStatus_Type()
)
tmnxLmpVRtrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrRowStatus.setStatus("current")
_TmnxLmpVRtrLastChanged_Type = TimeStamp
_TmnxLmpVRtrLastChanged_Object = MibTableColumn
tmnxLmpVRtrLastChanged = _TmnxLmpVRtrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 1, 1, 2),
    _TmnxLmpVRtrLastChanged_Type()
)
tmnxLmpVRtrLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrLastChanged.setStatus("current")


class _TmnxLmpVRtrAdminState_Type(TmnxAdminState):
    """Custom type tmnxLmpVRtrAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxLmpVRtrAdminState_Type.__name__ = "TmnxAdminState"
_TmnxLmpVRtrAdminState_Object = MibTableColumn
tmnxLmpVRtrAdminState = _TmnxLmpVRtrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 1, 1, 3),
    _TmnxLmpVRtrAdminState_Type()
)
tmnxLmpVRtrAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrAdminState.setStatus("current")


class _TmnxLmpVRtrOperState_Type(Integer32):
    """Custom type tmnxLmpVRtrOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TmnxLmpVRtrOperState_Type.__name__ = "Integer32"
_TmnxLmpVRtrOperState_Object = MibTableColumn
tmnxLmpVRtrOperState = _TmnxLmpVRtrOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 1, 1, 4),
    _TmnxLmpVRtrOperState_Type()
)
tmnxLmpVRtrOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrOperState.setStatus("current")


class _TmnxLmpVRtrGmplsLoopbackAddrType_Type(InetAddressType):
    """Custom type tmnxLmpVRtrGmplsLoopbackAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxLmpVRtrGmplsLoopbackAddrType_Type.__name__ = "InetAddressType"
_TmnxLmpVRtrGmplsLoopbackAddrType_Object = MibTableColumn
tmnxLmpVRtrGmplsLoopbackAddrType = _TmnxLmpVRtrGmplsLoopbackAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 1, 1, 5),
    _TmnxLmpVRtrGmplsLoopbackAddrType_Type()
)
tmnxLmpVRtrGmplsLoopbackAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrGmplsLoopbackAddrType.setStatus("current")


class _TmnxLmpVRtrGmplsLoopbackAddress_Type(InetAddress):
    """Custom type tmnxLmpVRtrGmplsLoopbackAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxLmpVRtrGmplsLoopbackAddress_Type.__name__ = "InetAddress"
_TmnxLmpVRtrGmplsLoopbackAddress_Object = MibTableColumn
tmnxLmpVRtrGmplsLoopbackAddress = _TmnxLmpVRtrGmplsLoopbackAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 1, 1, 6),
    _TmnxLmpVRtrGmplsLoopbackAddress_Type()
)
tmnxLmpVRtrGmplsLoopbackAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrGmplsLoopbackAddress.setStatus("current")
_TmnxLmpVRtrPeerTable_Object = MibTable
tmnxLmpVRtrPeerTable = _TmnxLmpVRtrPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrPeerTable.setStatus("current")
_TmnxLmpVRtrPeerEntry_Object = MibTableRow
tmnxLmpVRtrPeerEntry = _TmnxLmpVRtrPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 2, 1)
)
tmnxLmpVRtrPeerEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LMP-MIB", "tmnxLmpVRtrPeerNodeId"),
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrPeerEntry.setStatus("current")


class _TmnxLmpVRtrPeerNodeId_Type(Unsigned32):
    """Custom type tmnxLmpVRtrPeerNodeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxLmpVRtrPeerNodeId_Type.__name__ = "Unsigned32"
_TmnxLmpVRtrPeerNodeId_Object = MibTableColumn
tmnxLmpVRtrPeerNodeId = _TmnxLmpVRtrPeerNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 2, 1, 1),
    _TmnxLmpVRtrPeerNodeId_Type()
)
tmnxLmpVRtrPeerNodeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLmpVRtrPeerNodeId.setStatus("current")
_TmnxLmpVRtrPeerRowStatus_Type = RowStatus
_TmnxLmpVRtrPeerRowStatus_Object = MibTableColumn
tmnxLmpVRtrPeerRowStatus = _TmnxLmpVRtrPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 2, 1, 2),
    _TmnxLmpVRtrPeerRowStatus_Type()
)
tmnxLmpVRtrPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrPeerRowStatus.setStatus("current")
_TmnxLmpVRtrPeerLastChanged_Type = TimeStamp
_TmnxLmpVRtrPeerLastChanged_Object = MibTableColumn
tmnxLmpVRtrPeerLastChanged = _TmnxLmpVRtrPeerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 2, 1, 3),
    _TmnxLmpVRtrPeerLastChanged_Type()
)
tmnxLmpVRtrPeerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrPeerLastChanged.setStatus("current")


class _TmnxLmpVRtrPeerAdminState_Type(TmnxAdminState):
    """Custom type tmnxLmpVRtrPeerAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxLmpVRtrPeerAdminState_Type.__name__ = "TmnxAdminState"
_TmnxLmpVRtrPeerAdminState_Object = MibTableColumn
tmnxLmpVRtrPeerAdminState = _TmnxLmpVRtrPeerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 2, 1, 4),
    _TmnxLmpVRtrPeerAdminState_Type()
)
tmnxLmpVRtrPeerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrPeerAdminState.setStatus("current")


class _TmnxLmpVRtrPeerOperState_Type(Integer32):
    """Custom type tmnxLmpVRtrPeerOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TmnxLmpVRtrPeerOperState_Type.__name__ = "Integer32"
_TmnxLmpVRtrPeerOperState_Object = MibTableColumn
tmnxLmpVRtrPeerOperState = _TmnxLmpVRtrPeerOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 2, 1, 5),
    _TmnxLmpVRtrPeerOperState_Type()
)
tmnxLmpVRtrPeerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrPeerOperState.setStatus("current")


class _TmnxLmpVRtrPeerLoopbackAddrType_Type(InetAddressType):
    """Custom type tmnxLmpVRtrPeerLoopbackAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxLmpVRtrPeerLoopbackAddrType_Type.__name__ = "InetAddressType"
_TmnxLmpVRtrPeerLoopbackAddrType_Object = MibTableColumn
tmnxLmpVRtrPeerLoopbackAddrType = _TmnxLmpVRtrPeerLoopbackAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 2, 1, 6),
    _TmnxLmpVRtrPeerLoopbackAddrType_Type()
)
tmnxLmpVRtrPeerLoopbackAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrPeerLoopbackAddrType.setStatus("current")


class _TmnxLmpVRtrPeerLoopbackAddress_Type(InetAddress):
    """Custom type tmnxLmpVRtrPeerLoopbackAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxLmpVRtrPeerLoopbackAddress_Type.__name__ = "InetAddress"
_TmnxLmpVRtrPeerLoopbackAddress_Object = MibTableColumn
tmnxLmpVRtrPeerLoopbackAddress = _TmnxLmpVRtrPeerLoopbackAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 2, 1, 7),
    _TmnxLmpVRtrPeerLoopbackAddress_Type()
)
tmnxLmpVRtrPeerLoopbackAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrPeerLoopbackAddress.setStatus("current")


class _TmnxLmpVRtrPeerRetransmitIntvl_Type(Unsigned32):
    """Custom type tmnxLmpVRtrPeerRetransmitIntvl based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60000),
    )


_TmnxLmpVRtrPeerRetransmitIntvl_Type.__name__ = "Unsigned32"
_TmnxLmpVRtrPeerRetransmitIntvl_Object = MibTableColumn
tmnxLmpVRtrPeerRetransmitIntvl = _TmnxLmpVRtrPeerRetransmitIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 2, 1, 8),
    _TmnxLmpVRtrPeerRetransmitIntvl_Type()
)
tmnxLmpVRtrPeerRetransmitIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrPeerRetransmitIntvl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLmpVRtrPeerRetransmitIntvl.setUnits("milliseconds")


class _TmnxLmpVRtrPeerRetryLimit_Type(Unsigned32):
    """Custom type tmnxLmpVRtrPeerRetryLimit based on Unsigned32"""
    defaultValue = 0


_TmnxLmpVRtrPeerRetryLimit_Type.__name__ = "Unsigned32"
_TmnxLmpVRtrPeerRetryLimit_Object = MibTableColumn
tmnxLmpVRtrPeerRetryLimit = _TmnxLmpVRtrPeerRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 2, 1, 9),
    _TmnxLmpVRtrPeerRetryLimit_Type()
)
tmnxLmpVRtrPeerRetryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrPeerRetryLimit.setStatus("current")
_TmnxLmpVRtrPeerRetransmitDelta_Type = Unsigned32
_TmnxLmpVRtrPeerRetransmitDelta_Object = MibTableColumn
tmnxLmpVRtrPeerRetransmitDelta = _TmnxLmpVRtrPeerRetransmitDelta_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 2, 1, 10),
    _TmnxLmpVRtrPeerRetransmitDelta_Type()
)
tmnxLmpVRtrPeerRetransmitDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrPeerRetransmitDelta.setStatus("current")


class _TmnxLmpVRtrPeerCcVRtrId_Type(TmnxVRtrID):
    """Custom type tmnxLmpVRtrPeerCcVRtrId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxLmpVRtrPeerCcVRtrId_Type.__name__ = "TmnxVRtrID"
_TmnxLmpVRtrPeerCcVRtrId_Object = MibTableColumn
tmnxLmpVRtrPeerCcVRtrId = _TmnxLmpVRtrPeerCcVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 2, 1, 11),
    _TmnxLmpVRtrPeerCcVRtrId_Type()
)
tmnxLmpVRtrPeerCcVRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrPeerCcVRtrId.setStatus("current")


class _TmnxLmpVRtrPeerGmplsLpbkAddrType_Type(InetAddressType):
    """Custom type tmnxLmpVRtrPeerGmplsLpbkAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxLmpVRtrPeerGmplsLpbkAddrType_Type.__name__ = "InetAddressType"
_TmnxLmpVRtrPeerGmplsLpbkAddrType_Object = MibTableColumn
tmnxLmpVRtrPeerGmplsLpbkAddrType = _TmnxLmpVRtrPeerGmplsLpbkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 2, 1, 12),
    _TmnxLmpVRtrPeerGmplsLpbkAddrType_Type()
)
tmnxLmpVRtrPeerGmplsLpbkAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrPeerGmplsLpbkAddrType.setStatus("current")


class _TmnxLmpVRtrPeerGmplsLpbkAddress_Type(InetAddress):
    """Custom type tmnxLmpVRtrPeerGmplsLpbkAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxLmpVRtrPeerGmplsLpbkAddress_Type.__name__ = "InetAddress"
_TmnxLmpVRtrPeerGmplsLpbkAddress_Object = MibTableColumn
tmnxLmpVRtrPeerGmplsLpbkAddress = _TmnxLmpVRtrPeerGmplsLpbkAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 2, 1, 13),
    _TmnxLmpVRtrPeerGmplsLpbkAddress_Type()
)
tmnxLmpVRtrPeerGmplsLpbkAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrPeerGmplsLpbkAddress.setStatus("current")
_TmnxLmpVRtrControlChannelTable_Object = MibTable
tmnxLmpVRtrControlChannelTable = _TmnxLmpVRtrControlChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrControlChannelTable.setStatus("current")
_TmnxLmpVRtrControlChannelEntry_Object = MibTableRow
tmnxLmpVRtrControlChannelEntry = _TmnxLmpVRtrControlChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 3, 1)
)
tmnxLmpVRtrControlChannelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LMP-MIB", "tmnxLmpVRtrPeerNodeId"),
    (0, "TIMETRA-LMP-MIB", "tmnxLmpVRtrCcId"),
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrControlChannelEntry.setStatus("current")


class _TmnxLmpVRtrCcId_Type(Unsigned32):
    """Custom type tmnxLmpVRtrCcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxLmpVRtrCcId_Type.__name__ = "Unsigned32"
_TmnxLmpVRtrCcId_Object = MibTableColumn
tmnxLmpVRtrCcId = _TmnxLmpVRtrCcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 3, 1, 1),
    _TmnxLmpVRtrCcId_Type()
)
tmnxLmpVRtrCcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcId.setStatus("current")
_TmnxLmpVRtrCcRowStatus_Type = RowStatus
_TmnxLmpVRtrCcRowStatus_Object = MibTableColumn
tmnxLmpVRtrCcRowStatus = _TmnxLmpVRtrCcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 3, 1, 2),
    _TmnxLmpVRtrCcRowStatus_Type()
)
tmnxLmpVRtrCcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcRowStatus.setStatus("current")
_TmnxLmpVRtrCcLastChanged_Type = TimeStamp
_TmnxLmpVRtrCcLastChanged_Object = MibTableColumn
tmnxLmpVRtrCcLastChanged = _TmnxLmpVRtrCcLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 3, 1, 3),
    _TmnxLmpVRtrCcLastChanged_Type()
)
tmnxLmpVRtrCcLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcLastChanged.setStatus("current")


class _TmnxLmpVRtrCcAdminState_Type(TmnxAdminState):
    """Custom type tmnxLmpVRtrCcAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxLmpVRtrCcAdminState_Type.__name__ = "TmnxAdminState"
_TmnxLmpVRtrCcAdminState_Object = MibTableColumn
tmnxLmpVRtrCcAdminState = _TmnxLmpVRtrCcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 3, 1, 4),
    _TmnxLmpVRtrCcAdminState_Type()
)
tmnxLmpVRtrCcAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcAdminState.setStatus("current")


class _TmnxLmpVRtrCcOperState_Type(Integer32):
    """Custom type tmnxLmpVRtrCcOperState based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("configSnd", 3),
          ("configRcv", 4),
          ("active", 5),
          ("goingDown", 6))
    )


_TmnxLmpVRtrCcOperState_Type.__name__ = "Integer32"
_TmnxLmpVRtrCcOperState_Object = MibTableColumn
tmnxLmpVRtrCcOperState = _TmnxLmpVRtrCcOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 3, 1, 5),
    _TmnxLmpVRtrCcOperState_Type()
)
tmnxLmpVRtrCcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcOperState.setStatus("current")
_TmnxLmpVRtrCcRemoteId_Type = Unsigned32
_TmnxLmpVRtrCcRemoteId_Object = MibTableColumn
tmnxLmpVRtrCcRemoteId = _TmnxLmpVRtrCcRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 3, 1, 6),
    _TmnxLmpVRtrCcRemoteId_Type()
)
tmnxLmpVRtrCcRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcRemoteId.setStatus("current")


class _TmnxLmpVRtrCcPeerIfAddressType_Type(InetAddressType):
    """Custom type tmnxLmpVRtrCcPeerIfAddressType based on InetAddressType"""
    defaultValue = 0


_TmnxLmpVRtrCcPeerIfAddressType_Type.__name__ = "InetAddressType"
_TmnxLmpVRtrCcPeerIfAddressType_Object = MibTableColumn
tmnxLmpVRtrCcPeerIfAddressType = _TmnxLmpVRtrCcPeerIfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 3, 1, 7),
    _TmnxLmpVRtrCcPeerIfAddressType_Type()
)
tmnxLmpVRtrCcPeerIfAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcPeerIfAddressType.setStatus("current")


class _TmnxLmpVRtrCcPeerIfAddress_Type(InetAddress):
    """Custom type tmnxLmpVRtrCcPeerIfAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxLmpVRtrCcPeerIfAddress_Type.__name__ = "InetAddress"
_TmnxLmpVRtrCcPeerIfAddress_Object = MibTableColumn
tmnxLmpVRtrCcPeerIfAddress = _TmnxLmpVRtrCcPeerIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 3, 1, 8),
    _TmnxLmpVRtrCcPeerIfAddress_Type()
)
tmnxLmpVRtrCcPeerIfAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcPeerIfAddress.setStatus("current")


class _TmnxLmpVRtrCcSetupRole_Type(Integer32):
    """Custom type tmnxLmpVRtrCcSetupRole based on Integer32"""
    defaultValue = 1

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


_TmnxLmpVRtrCcSetupRole_Type.__name__ = "Integer32"
_TmnxLmpVRtrCcSetupRole_Object = MibTableColumn
tmnxLmpVRtrCcSetupRole = _TmnxLmpVRtrCcSetupRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 3, 1, 9),
    _TmnxLmpVRtrCcSetupRole_Type()
)
tmnxLmpVRtrCcSetupRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcSetupRole.setStatus("current")


class _TmnxLmpVRtrCcHelloInterval_Type(Unsigned32):
    """Custom type tmnxLmpVRtrCcHelloInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535),
    )


_TmnxLmpVRtrCcHelloInterval_Type.__name__ = "Unsigned32"
_TmnxLmpVRtrCcHelloInterval_Object = MibTableColumn
tmnxLmpVRtrCcHelloInterval = _TmnxLmpVRtrCcHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 3, 1, 10),
    _TmnxLmpVRtrCcHelloInterval_Type()
)
tmnxLmpVRtrCcHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcHelloInterval.setUnits("milliseconds")
_TmnxLmpVRtrCcHelloIntvNeg_Type = Unsigned32
_TmnxLmpVRtrCcHelloIntvNeg_Object = MibTableColumn
tmnxLmpVRtrCcHelloIntvNeg = _TmnxLmpVRtrCcHelloIntvNeg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 3, 1, 11),
    _TmnxLmpVRtrCcHelloIntvNeg_Type()
)
tmnxLmpVRtrCcHelloIntvNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcHelloIntvNeg.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcHelloIntvNeg.setUnits("milliseconds")


class _TmnxLmpVRtrCcHelloDeadInterval_Type(Unsigned32):
    """Custom type tmnxLmpVRtrCcHelloDeadInterval based on Unsigned32"""
    defaultValue = 4000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3000, 65535),
    )


_TmnxLmpVRtrCcHelloDeadInterval_Type.__name__ = "Unsigned32"
_TmnxLmpVRtrCcHelloDeadInterval_Object = MibTableColumn
tmnxLmpVRtrCcHelloDeadInterval = _TmnxLmpVRtrCcHelloDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 3, 1, 12),
    _TmnxLmpVRtrCcHelloDeadInterval_Type()
)
tmnxLmpVRtrCcHelloDeadInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcHelloDeadInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcHelloDeadInterval.setUnits("milliseconds")
_TmnxLmpVRtrCcHelloDeadIntvNeg_Type = Unsigned32
_TmnxLmpVRtrCcHelloDeadIntvNeg_Object = MibTableColumn
tmnxLmpVRtrCcHelloDeadIntvNeg = _TmnxLmpVRtrCcHelloDeadIntvNeg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 3, 1, 13),
    _TmnxLmpVRtrCcHelloDeadIntvNeg_Type()
)
tmnxLmpVRtrCcHelloDeadIntvNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcHelloDeadIntvNeg.setStatus("current")


class _TmnxLmpVRtrCcTtl_Type(Unsigned32):
    """Custom type tmnxLmpVRtrCcTtl based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxLmpVRtrCcTtl_Type.__name__ = "Unsigned32"
_TmnxLmpVRtrCcTtl_Object = MibTableColumn
tmnxLmpVRtrCcTtl = _TmnxLmpVRtrCcTtl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 3, 1, 14),
    _TmnxLmpVRtrCcTtl_Type()
)
tmnxLmpVRtrCcTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcTtl.setStatus("current")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcTtl.setUnits("hops")
_TmnxLmpVRtrCcIsTunneled_Type = TruthValue
_TmnxLmpVRtrCcIsTunneled_Object = MibTableColumn
tmnxLmpVRtrCcIsTunneled = _TmnxLmpVRtrCcIsTunneled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 3, 1, 15),
    _TmnxLmpVRtrCcIsTunneled_Type()
)
tmnxLmpVRtrCcIsTunneled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcIsTunneled.setStatus("current")
_TmnxLmpVRtrTeLinkTable_Object = MibTable
tmnxLmpVRtrTeLinkTable = _TmnxLmpVRtrTeLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkTable.setStatus("current")
_TmnxLmpVRtrTeLinkEntry_Object = MibTableRow
tmnxLmpVRtrTeLinkEntry = _TmnxLmpVRtrTeLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 4, 1)
)
tmnxLmpVRtrTeLinkEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkId"),
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkEntry.setStatus("current")


class _TmnxLmpVRtrTeLinkId_Type(Unsigned32):
    """Custom type tmnxLmpVRtrTeLinkId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxLmpVRtrTeLinkId_Type.__name__ = "Unsigned32"
_TmnxLmpVRtrTeLinkId_Object = MibTableColumn
tmnxLmpVRtrTeLinkId = _TmnxLmpVRtrTeLinkId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 4, 1, 1),
    _TmnxLmpVRtrTeLinkId_Type()
)
tmnxLmpVRtrTeLinkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkId.setStatus("current")
_TmnxLmpVRtrTeLinkRowStatus_Type = RowStatus
_TmnxLmpVRtrTeLinkRowStatus_Object = MibTableColumn
tmnxLmpVRtrTeLinkRowStatus = _TmnxLmpVRtrTeLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 4, 1, 2),
    _TmnxLmpVRtrTeLinkRowStatus_Type()
)
tmnxLmpVRtrTeLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkRowStatus.setStatus("current")
_TmnxLmpVRtrTeLinkLastChanged_Type = TimeStamp
_TmnxLmpVRtrTeLinkLastChanged_Object = MibTableColumn
tmnxLmpVRtrTeLinkLastChanged = _TmnxLmpVRtrTeLinkLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 4, 1, 3),
    _TmnxLmpVRtrTeLinkLastChanged_Type()
)
tmnxLmpVRtrTeLinkLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkLastChanged.setStatus("current")


class _TmnxLmpVRtrTeLinkAdminState_Type(TmnxAdminState):
    """Custom type tmnxLmpVRtrTeLinkAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxLmpVRtrTeLinkAdminState_Type.__name__ = "TmnxAdminState"
_TmnxLmpVRtrTeLinkAdminState_Object = MibTableColumn
tmnxLmpVRtrTeLinkAdminState = _TmnxLmpVRtrTeLinkAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 4, 1, 4),
    _TmnxLmpVRtrTeLinkAdminState_Type()
)
tmnxLmpVRtrTeLinkAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkAdminState.setStatus("current")


class _TmnxLmpVRtrTeLinkOperState_Type(Integer32):
    """Custom type tmnxLmpVRtrTeLinkOperState based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("init", 4),
          ("degraded", 5))
    )


_TmnxLmpVRtrTeLinkOperState_Type.__name__ = "Integer32"
_TmnxLmpVRtrTeLinkOperState_Object = MibTableColumn
tmnxLmpVRtrTeLinkOperState = _TmnxLmpVRtrTeLinkOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 4, 1, 5),
    _TmnxLmpVRtrTeLinkOperState_Type()
)
tmnxLmpVRtrTeLinkOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkOperState.setStatus("current")


class _TmnxLmpVRtrTeLinkName_Type(TNamedItemOrEmpty):
    """Custom type tmnxLmpVRtrTeLinkName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxLmpVRtrTeLinkName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxLmpVRtrTeLinkName_Object = MibTableColumn
tmnxLmpVRtrTeLinkName = _TmnxLmpVRtrTeLinkName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 4, 1, 6),
    _TmnxLmpVRtrTeLinkName_Type()
)
tmnxLmpVRtrTeLinkName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkName.setStatus("current")


class _TmnxLmpVRtrTeLinkRemoteId_Type(Unsigned32):
    """Custom type tmnxLmpVRtrTeLinkRemoteId based on Unsigned32"""
    defaultValue = 0


_TmnxLmpVRtrTeLinkRemoteId_Type.__name__ = "Unsigned32"
_TmnxLmpVRtrTeLinkRemoteId_Object = MibTableColumn
tmnxLmpVRtrTeLinkRemoteId = _TmnxLmpVRtrTeLinkRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 4, 1, 7),
    _TmnxLmpVRtrTeLinkRemoteId_Type()
)
tmnxLmpVRtrTeLinkRemoteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkRemoteId.setStatus("current")


class _TmnxLmpVRtrTeLinkPeerNodeId_Type(Unsigned32):
    """Custom type tmnxLmpVRtrTeLinkPeerNodeId based on Unsigned32"""
    defaultValue = 0


_TmnxLmpVRtrTeLinkPeerNodeId_Type.__name__ = "Unsigned32"
_TmnxLmpVRtrTeLinkPeerNodeId_Object = MibTableColumn
tmnxLmpVRtrTeLinkPeerNodeId = _TmnxLmpVRtrTeLinkPeerNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 4, 1, 8),
    _TmnxLmpVRtrTeLinkPeerNodeId_Type()
)
tmnxLmpVRtrTeLinkPeerNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkPeerNodeId.setStatus("current")
_TmnxLmpVRtrDbLinkTable_Object = MibTable
tmnxLmpVRtrDbLinkTable = _TmnxLmpVRtrDbLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 5)
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrDbLinkTable.setStatus("current")
_TmnxLmpVRtrDbLinkEntry_Object = MibTableRow
tmnxLmpVRtrDbLinkEntry = _TmnxLmpVRtrDbLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 5, 1)
)
tmnxLmpVRtrDbLinkEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkId"),
    (0, "TIMETRA-LMP-MIB", "tmnxLmpVRtrDbLinkId"),
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrDbLinkEntry.setStatus("current")


class _TmnxLmpVRtrDbLinkId_Type(Unsigned32):
    """Custom type tmnxLmpVRtrDbLinkId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxLmpVRtrDbLinkId_Type.__name__ = "Unsigned32"
_TmnxLmpVRtrDbLinkId_Object = MibTableColumn
tmnxLmpVRtrDbLinkId = _TmnxLmpVRtrDbLinkId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 5, 1, 1),
    _TmnxLmpVRtrDbLinkId_Type()
)
tmnxLmpVRtrDbLinkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxLmpVRtrDbLinkId.setStatus("current")
_TmnxLmpVRtrDbLinkRowStatus_Type = RowStatus
_TmnxLmpVRtrDbLinkRowStatus_Object = MibTableColumn
tmnxLmpVRtrDbLinkRowStatus = _TmnxLmpVRtrDbLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 5, 1, 2),
    _TmnxLmpVRtrDbLinkRowStatus_Type()
)
tmnxLmpVRtrDbLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrDbLinkRowStatus.setStatus("current")
_TmnxLmpVRtrDbLinkLastChanged_Type = TimeStamp
_TmnxLmpVRtrDbLinkLastChanged_Object = MibTableColumn
tmnxLmpVRtrDbLinkLastChanged = _TmnxLmpVRtrDbLinkLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 5, 1, 3),
    _TmnxLmpVRtrDbLinkLastChanged_Type()
)
tmnxLmpVRtrDbLinkLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrDbLinkLastChanged.setStatus("current")


class _TmnxLmpVRtrDbLinkAdminState_Type(TmnxAdminState):
    """Custom type tmnxLmpVRtrDbLinkAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxLmpVRtrDbLinkAdminState_Type.__name__ = "TmnxAdminState"
_TmnxLmpVRtrDbLinkAdminState_Object = MibTableColumn
tmnxLmpVRtrDbLinkAdminState = _TmnxLmpVRtrDbLinkAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 5, 1, 4),
    _TmnxLmpVRtrDbLinkAdminState_Type()
)
tmnxLmpVRtrDbLinkAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrDbLinkAdminState.setStatus("current")


class _TmnxLmpVRtrDbLinkOperState_Type(Integer32):
    """Custom type tmnxLmpVRtrDbLinkOperState based on Integer32"""
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
        *(("upAlloc", 1),
          ("upFree", 2),
          ("down", 3),
          ("testing", 4))
    )


_TmnxLmpVRtrDbLinkOperState_Type.__name__ = "Integer32"
_TmnxLmpVRtrDbLinkOperState_Object = MibTableColumn
tmnxLmpVRtrDbLinkOperState = _TmnxLmpVRtrDbLinkOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 5, 1, 5),
    _TmnxLmpVRtrDbLinkOperState_Type()
)
tmnxLmpVRtrDbLinkOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrDbLinkOperState.setStatus("current")


class _TmnxLmpVRtrDbLinkPortId_Type(TmnxPortID):
    """Custom type tmnxLmpVRtrDbLinkPortId based on TmnxPortID"""
    defaultValue = 503316480


_TmnxLmpVRtrDbLinkPortId_Type.__name__ = "TmnxPortID"
_TmnxLmpVRtrDbLinkPortId_Object = MibTableColumn
tmnxLmpVRtrDbLinkPortId = _TmnxLmpVRtrDbLinkPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 5, 1, 6),
    _TmnxLmpVRtrDbLinkPortId_Type()
)
tmnxLmpVRtrDbLinkPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrDbLinkPortId.setStatus("current")


class _TmnxLmpVRtrDbLinkRemoteId_Type(Unsigned32):
    """Custom type tmnxLmpVRtrDbLinkRemoteId based on Unsigned32"""
    defaultValue = 0


_TmnxLmpVRtrDbLinkRemoteId_Type.__name__ = "Unsigned32"
_TmnxLmpVRtrDbLinkRemoteId_Object = MibTableColumn
tmnxLmpVRtrDbLinkRemoteId = _TmnxLmpVRtrDbLinkRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 5, 1, 7),
    _TmnxLmpVRtrDbLinkRemoteId_Type()
)
tmnxLmpVRtrDbLinkRemoteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLmpVRtrDbLinkRemoteId.setStatus("current")


class _TmnxLmpVRtrDbLinkReasonDownFlags_Type(Bits):
    """Custom type tmnxLmpVRtrDbLinkReasonDownFlags based on Bits"""
    namedValues = NamedValues(
        *(("unknown", 0),
          ("adminDn", 1),
          ("lpcFault", 2),
          ("remoteLkFault", 3),
          ("portAdminDn", 4),
          ("portFault", 5),
          ("gmplsTeDn", 6))
    )

_TmnxLmpVRtrDbLinkReasonDownFlags_Type.__name__ = "Bits"
_TmnxLmpVRtrDbLinkReasonDownFlags_Object = MibTableColumn
tmnxLmpVRtrDbLinkReasonDownFlags = _TmnxLmpVRtrDbLinkReasonDownFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 2, 5, 1, 8),
    _TmnxLmpVRtrDbLinkReasonDownFlags_Type()
)
tmnxLmpVRtrDbLinkReasonDownFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrDbLinkReasonDownFlags.setStatus("current")
_TmnxLmpStatistics_ObjectIdentity = ObjectIdentity
tmnxLmpStatistics = _TmnxLmpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3)
)
_TmnxLmpVRtrControlChanStatsTable_Object = MibTable
tmnxLmpVRtrControlChanStatsTable = _TmnxLmpVRtrControlChanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrControlChanStatsTable.setStatus("current")
_TmnxLmpVRtrControlChanStatsEntry_Object = MibTableRow
tmnxLmpVRtrControlChanStatsEntry = _TmnxLmpVRtrControlChanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1, 1)
)
tmnxLmpVRtrControlChanStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LMP-MIB", "tmnxLmpVRtrPeerNodeId"),
    (0, "TIMETRA-LMP-MIB", "tmnxLmpVRtrCcId"),
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrControlChanStatsEntry.setStatus("current")
_TmnxLmpVRtrCcInErrors_Type = Counter32
_TmnxLmpVRtrCcInErrors_Object = MibTableColumn
tmnxLmpVRtrCcInErrors = _TmnxLmpVRtrCcInErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1, 1, 1),
    _TmnxLmpVRtrCcInErrors_Type()
)
tmnxLmpVRtrCcInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcInErrors.setStatus("current")
_TmnxLmpVRtrCcOutErrors_Type = Counter32
_TmnxLmpVRtrCcOutErrors_Object = MibTableColumn
tmnxLmpVRtrCcOutErrors = _TmnxLmpVRtrCcOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1, 1, 2),
    _TmnxLmpVRtrCcOutErrors_Type()
)
tmnxLmpVRtrCcOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcOutErrors.setStatus("current")
_TmnxLmpVRtrCcConfigReceived_Type = Counter32
_TmnxLmpVRtrCcConfigReceived_Object = MibTableColumn
tmnxLmpVRtrCcConfigReceived = _TmnxLmpVRtrCcConfigReceived_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1, 1, 3),
    _TmnxLmpVRtrCcConfigReceived_Type()
)
tmnxLmpVRtrCcConfigReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcConfigReceived.setStatus("current")
_TmnxLmpVRtrCcConfigSent_Type = Counter32
_TmnxLmpVRtrCcConfigSent_Object = MibTableColumn
tmnxLmpVRtrCcConfigSent = _TmnxLmpVRtrCcConfigSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1, 1, 4),
    _TmnxLmpVRtrCcConfigSent_Type()
)
tmnxLmpVRtrCcConfigSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcConfigSent.setStatus("current")
_TmnxLmpVRtrCcConfigRetransmit_Type = Counter32
_TmnxLmpVRtrCcConfigRetransmit_Object = MibTableColumn
tmnxLmpVRtrCcConfigRetransmit = _TmnxLmpVRtrCcConfigRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1, 1, 5),
    _TmnxLmpVRtrCcConfigRetransmit_Type()
)
tmnxLmpVRtrCcConfigRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcConfigRetransmit.setStatus("current")
_TmnxLmpVRtrCcConfigAckReceived_Type = Counter32
_TmnxLmpVRtrCcConfigAckReceived_Object = MibTableColumn
tmnxLmpVRtrCcConfigAckReceived = _TmnxLmpVRtrCcConfigAckReceived_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1, 1, 6),
    _TmnxLmpVRtrCcConfigAckReceived_Type()
)
tmnxLmpVRtrCcConfigAckReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcConfigAckReceived.setStatus("current")
_TmnxLmpVRtrCcConfigAckSent_Type = Counter32
_TmnxLmpVRtrCcConfigAckSent_Object = MibTableColumn
tmnxLmpVRtrCcConfigAckSent = _TmnxLmpVRtrCcConfigAckSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1, 1, 7),
    _TmnxLmpVRtrCcConfigAckSent_Type()
)
tmnxLmpVRtrCcConfigAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcConfigAckSent.setStatus("current")
_TmnxLmpVRtrCcConfigNackReceived_Type = Counter32
_TmnxLmpVRtrCcConfigNackReceived_Object = MibTableColumn
tmnxLmpVRtrCcConfigNackReceived = _TmnxLmpVRtrCcConfigNackReceived_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1, 1, 8),
    _TmnxLmpVRtrCcConfigNackReceived_Type()
)
tmnxLmpVRtrCcConfigNackReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcConfigNackReceived.setStatus("current")
_TmnxLmpVRtrCcConfigNackSent_Type = Counter32
_TmnxLmpVRtrCcConfigNackSent_Object = MibTableColumn
tmnxLmpVRtrCcConfigNackSent = _TmnxLmpVRtrCcConfigNackSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1, 1, 9),
    _TmnxLmpVRtrCcConfigNackSent_Type()
)
tmnxLmpVRtrCcConfigNackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcConfigNackSent.setStatus("current")
_TmnxLmpVRtrCcHelloReceived_Type = Counter32
_TmnxLmpVRtrCcHelloReceived_Object = MibTableColumn
tmnxLmpVRtrCcHelloReceived = _TmnxLmpVRtrCcHelloReceived_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1, 1, 10),
    _TmnxLmpVRtrCcHelloReceived_Type()
)
tmnxLmpVRtrCcHelloReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcHelloReceived.setStatus("current")
_TmnxLmpVRtrCcHelloSent_Type = Counter32
_TmnxLmpVRtrCcHelloSent_Object = MibTableColumn
tmnxLmpVRtrCcHelloSent = _TmnxLmpVRtrCcHelloSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1, 1, 12),
    _TmnxLmpVRtrCcHelloSent_Type()
)
tmnxLmpVRtrCcHelloSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcHelloSent.setStatus("current")
_TmnxLmpVRtrCcLinkSumReceived_Type = Counter32
_TmnxLmpVRtrCcLinkSumReceived_Object = MibTableColumn
tmnxLmpVRtrCcLinkSumReceived = _TmnxLmpVRtrCcLinkSumReceived_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1, 1, 13),
    _TmnxLmpVRtrCcLinkSumReceived_Type()
)
tmnxLmpVRtrCcLinkSumReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcLinkSumReceived.setStatus("current")
_TmnxLmpVRtrCcLinkSumSent_Type = Counter32
_TmnxLmpVRtrCcLinkSumSent_Object = MibTableColumn
tmnxLmpVRtrCcLinkSumSent = _TmnxLmpVRtrCcLinkSumSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1, 1, 14),
    _TmnxLmpVRtrCcLinkSumSent_Type()
)
tmnxLmpVRtrCcLinkSumSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcLinkSumSent.setStatus("current")
_TmnxLmpVRtrCcLinkSumRetransmit_Type = Counter32
_TmnxLmpVRtrCcLinkSumRetransmit_Object = MibTableColumn
tmnxLmpVRtrCcLinkSumRetransmit = _TmnxLmpVRtrCcLinkSumRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1, 1, 15),
    _TmnxLmpVRtrCcLinkSumRetransmit_Type()
)
tmnxLmpVRtrCcLinkSumRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcLinkSumRetransmit.setStatus("current")
_TmnxLmpVRtrCcLinkSumAckReceived_Type = Counter32
_TmnxLmpVRtrCcLinkSumAckReceived_Object = MibTableColumn
tmnxLmpVRtrCcLinkSumAckReceived = _TmnxLmpVRtrCcLinkSumAckReceived_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1, 1, 16),
    _TmnxLmpVRtrCcLinkSumAckReceived_Type()
)
tmnxLmpVRtrCcLinkSumAckReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcLinkSumAckReceived.setStatus("current")
_TmnxLmpVRtrCcLinkSumAckSent_Type = Counter32
_TmnxLmpVRtrCcLinkSumAckSent_Object = MibTableColumn
tmnxLmpVRtrCcLinkSumAckSent = _TmnxLmpVRtrCcLinkSumAckSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1, 1, 17),
    _TmnxLmpVRtrCcLinkSumAckSent_Type()
)
tmnxLmpVRtrCcLinkSumAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcLinkSumAckSent.setStatus("current")
_TmnxLmpVRtrCcLinkSumNackReceived_Type = Counter32
_TmnxLmpVRtrCcLinkSumNackReceived_Object = MibTableColumn
tmnxLmpVRtrCcLinkSumNackReceived = _TmnxLmpVRtrCcLinkSumNackReceived_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1, 1, 18),
    _TmnxLmpVRtrCcLinkSumNackReceived_Type()
)
tmnxLmpVRtrCcLinkSumNackReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcLinkSumNackReceived.setStatus("current")
_TmnxLmpVRtrCcLinkSumNackSent_Type = Counter32
_TmnxLmpVRtrCcLinkSumNackSent_Object = MibTableColumn
tmnxLmpVRtrCcLinkSumNackSent = _TmnxLmpVRtrCcLinkSumNackSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1, 1, 19),
    _TmnxLmpVRtrCcLinkSumNackSent_Type()
)
tmnxLmpVRtrCcLinkSumNackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcLinkSumNackSent.setStatus("current")
_TmnxLmpVRtrCcDiscontinuityTime_Type = TimeStamp
_TmnxLmpVRtrCcDiscontinuityTime_Object = MibTableColumn
tmnxLmpVRtrCcDiscontinuityTime = _TmnxLmpVRtrCcDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 1, 1, 20),
    _TmnxLmpVRtrCcDiscontinuityTime_Type()
)
tmnxLmpVRtrCcDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcDiscontinuityTime.setStatus("current")
_TmnxLmpVRtrTeLinkStatsTable_Object = MibTable
tmnxLmpVRtrTeLinkStatsTable = _TmnxLmpVRtrTeLinkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkStatsTable.setStatus("current")
_TmnxLmpVRtrTeLinkStatsEntry_Object = MibTableRow
tmnxLmpVRtrTeLinkStatsEntry = _TmnxLmpVRtrTeLinkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 2, 1)
)
tmnxLmpVRtrTeLinkStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkId"),
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkStatsEntry.setStatus("current")
_TmnxLmpVRtrTeLinkSumReceived_Type = Counter32
_TmnxLmpVRtrTeLinkSumReceived_Object = MibTableColumn
tmnxLmpVRtrTeLinkSumReceived = _TmnxLmpVRtrTeLinkSumReceived_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 2, 1, 1),
    _TmnxLmpVRtrTeLinkSumReceived_Type()
)
tmnxLmpVRtrTeLinkSumReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkSumReceived.setStatus("current")
_TmnxLmpVRtrTeLinkSumSent_Type = Counter32
_TmnxLmpVRtrTeLinkSumSent_Object = MibTableColumn
tmnxLmpVRtrTeLinkSumSent = _TmnxLmpVRtrTeLinkSumSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 2, 1, 2),
    _TmnxLmpVRtrTeLinkSumSent_Type()
)
tmnxLmpVRtrTeLinkSumSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkSumSent.setStatus("current")
_TmnxLmpVRtrTeLinkSumRetransmit_Type = Counter32
_TmnxLmpVRtrTeLinkSumRetransmit_Object = MibTableColumn
tmnxLmpVRtrTeLinkSumRetransmit = _TmnxLmpVRtrTeLinkSumRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 2, 1, 3),
    _TmnxLmpVRtrTeLinkSumRetransmit_Type()
)
tmnxLmpVRtrTeLinkSumRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkSumRetransmit.setStatus("current")
_TmnxLmpVRtrTeLinkSumAckReceived_Type = Counter32
_TmnxLmpVRtrTeLinkSumAckReceived_Object = MibTableColumn
tmnxLmpVRtrTeLinkSumAckReceived = _TmnxLmpVRtrTeLinkSumAckReceived_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 2, 1, 4),
    _TmnxLmpVRtrTeLinkSumAckReceived_Type()
)
tmnxLmpVRtrTeLinkSumAckReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkSumAckReceived.setStatus("current")
_TmnxLmpVRtrTeLinkSumAckSent_Type = Counter32
_TmnxLmpVRtrTeLinkSumAckSent_Object = MibTableColumn
tmnxLmpVRtrTeLinkSumAckSent = _TmnxLmpVRtrTeLinkSumAckSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 2, 1, 5),
    _TmnxLmpVRtrTeLinkSumAckSent_Type()
)
tmnxLmpVRtrTeLinkSumAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkSumAckSent.setStatus("current")
_TmnxLmpVRtrTeLinkSumNackReceived_Type = Counter32
_TmnxLmpVRtrTeLinkSumNackReceived_Object = MibTableColumn
tmnxLmpVRtrTeLinkSumNackReceived = _TmnxLmpVRtrTeLinkSumNackReceived_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 2, 1, 6),
    _TmnxLmpVRtrTeLinkSumNackReceived_Type()
)
tmnxLmpVRtrTeLinkSumNackReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkSumNackReceived.setStatus("current")
_TmnxLmpVRtrTeLinkSumNackSent_Type = Counter32
_TmnxLmpVRtrTeLinkSumNackSent_Object = MibTableColumn
tmnxLmpVRtrTeLinkSumNackSent = _TmnxLmpVRtrTeLinkSumNackSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 2, 1, 7),
    _TmnxLmpVRtrTeLinkSumNackSent_Type()
)
tmnxLmpVRtrTeLinkSumNackSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkSumNackSent.setStatus("current")
_TmnxLmpVRtrTeLinkDiscntnuityTime_Type = TimeStamp
_TmnxLmpVRtrTeLinkDiscntnuityTime_Object = MibTableColumn
tmnxLmpVRtrTeLinkDiscntnuityTime = _TmnxLmpVRtrTeLinkDiscntnuityTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 3, 2, 1, 8),
    _TmnxLmpVRtrTeLinkDiscntnuityTime_Type()
)
tmnxLmpVRtrTeLinkDiscntnuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkDiscntnuityTime.setStatus("current")
_TmnxLmpNotifyObjects_ObjectIdentity = ObjectIdentity
tmnxLmpNotifyObjects = _TmnxLmpNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 100, 4)
)
_TmnxLmpNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxLmpNotifyPrefix = _TmnxLmpNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 100)
)
_TmnxLmpNotification_ObjectIdentity = ObjectIdentity
tmnxLmpNotification = _TmnxLmpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 100, 0)
)

# Managed Objects groups

tmnxLmpVRtrGroupV13v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 100, 2, 1, 1)
)
tmnxLmpVRtrGroupV13v0.setObjects(
      *(("TIMETRA-LMP-MIB", "tmnxLmpVRtrTableLastChanged"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrRowStatus"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrLastChanged"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrAdminState"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrOperState"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrGmplsLoopbackAddrType"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrGmplsLoopbackAddress"))
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrGroupV13v0.setStatus("current")

tmnxLmpVRtrPeerGroupV13v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 100, 2, 1, 2)
)
tmnxLmpVRtrPeerGroupV13v0.setObjects(
      *(("TIMETRA-LMP-MIB", "tmnxLmpVRtrPeerTableLastChanged"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrPeerRowStatus"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrPeerLastChanged"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrPeerAdminState"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrPeerOperState"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrPeerLoopbackAddrType"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrPeerLoopbackAddress"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrPeerRetransmitIntvl"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrPeerRetryLimit"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrPeerRetransmitDelta"))
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrPeerGroupV13v0.setStatus("current")

tmnxLmpVRtrCcGroupV13v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 100, 2, 1, 3)
)
tmnxLmpVRtrCcGroupV13v0.setObjects(
      *(("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcTableLastChanged"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcRowStatus"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcLastChanged"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcAdminState"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcOperState"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcRemoteId"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcPeerIfAddressType"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcPeerIfAddress"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcSetupRole"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcHelloInterval"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcHelloIntvNeg"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcHelloDeadInterval"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcHelloDeadIntvNeg"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcTtl"))
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcGroupV13v0.setStatus("current")

tmnxLmpVRtrTeLinkGroupV13v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 100, 2, 1, 4)
)
tmnxLmpVRtrTeLinkGroupV13v0.setObjects(
      *(("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkTableLastChange"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkRowStatus"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkLastChanged"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkAdminState"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkOperState"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkName"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkRemoteId"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkPeerNodeId"))
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkGroupV13v0.setStatus("current")

tmnxLmpVRtrDbLinkGroupV13v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 100, 2, 1, 5)
)
tmnxLmpVRtrDbLinkGroupV13v0.setObjects(
      *(("TIMETRA-LMP-MIB", "tmnxLmpVRtrDbLinkTableLastChange"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrDbLinkRowStatus"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrDbLinkLastChanged"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrDbLinkAdminState"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrDbLinkOperState"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrDbLinkPortId"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrDbLinkRemoteId"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrDbLinkReasonDownFlags"))
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrDbLinkGroupV13v0.setStatus("current")

tmnxLmpVRtrCcStatsGroupV13v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 100, 2, 1, 6)
)
tmnxLmpVRtrCcStatsGroupV13v0.setObjects(
      *(("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcInErrors"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcOutErrors"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcConfigReceived"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcConfigSent"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcConfigRetransmit"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcConfigAckReceived"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcConfigAckSent"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcConfigNackReceived"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcConfigNackSent"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcHelloReceived"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcHelloSent"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcLinkSumReceived"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcLinkSumSent"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcLinkSumRetransmit"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcLinkSumAckReceived"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcLinkSumAckSent"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcLinkSumNackReceived"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcLinkSumNackSent"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrCcStatsGroupV13v0.setStatus("current")

tmnxLmpVRtrTeLinkStatsGroupV13v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 100, 2, 1, 7)
)
tmnxLmpVRtrTeLinkStatsGroupV13v0.setObjects(
      *(("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkSumReceived"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkSumSent"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkSumRetransmit"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkSumAckReceived"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkSumAckSent"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkSumNackReceived"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkSumNackSent"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkDiscntnuityTime"))
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkStatsGroupV13v0.setStatus("current")

tmnxLmpVRtrPeerGroupV15v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 100, 2, 2, 1)
)
tmnxLmpVRtrPeerGroupV15v0.setObjects(
      *(("TIMETRA-LMP-MIB", "tmnxLmpVRtrPeerCcVRtrId"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrPeerGmplsLpbkAddrType"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrPeerGmplsLpbkAddress"))
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrPeerGroupV15v0.setStatus("current")

tmnxLmpVRtrCtrlChannelGroupV15v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 100, 2, 2, 2)
)
tmnxLmpVRtrCtrlChannelGroupV15v0.setObjects(
    ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcIsTunneled")
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrCtrlChannelGroupV15v0.setStatus("current")


# Notification objects

tmnxLmpVRtrTeLinkPropMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 100, 0, 1)
)
tmnxLmpVRtrTeLinkPropMismatch.setObjects(
      *(("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkRemoteId"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkPeerNodeId"))
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkPropMismatch.setStatus(
        "current"
    )

tmnxLmpVRtrTeLinkPropMismatchClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 100, 0, 2)
)
tmnxLmpVRtrTeLinkPropMismatchClr.setObjects(
      *(("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkRemoteId"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkPeerNodeId"))
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkPropMismatchClr.setStatus(
        "current"
    )

tmnxLmpVRtrDbLinkPropMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 100, 0, 3)
)
tmnxLmpVRtrDbLinkPropMismatch.setObjects(
    ("TIMETRA-LMP-MIB", "tmnxLmpVRtrDbLinkRemoteId")
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrDbLinkPropMismatch.setStatus(
        "current"
    )

tmnxLmpVRtrDbLinkPropMismatchClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 100, 0, 4)
)
tmnxLmpVRtrDbLinkPropMismatchClr.setObjects(
    ("TIMETRA-LMP-MIB", "tmnxLmpVRtrDbLinkRemoteId")
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrDbLinkPropMismatchClr.setStatus(
        "current"
    )

tmnxLmpVRtrControlChannelState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 100, 0, 5)
)
tmnxLmpVRtrControlChannelState.setObjects(
    ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcOperState")
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrControlChannelState.setStatus(
        "current"
    )

tmnxLmpVRtrTeLinkState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 100, 0, 6)
)
tmnxLmpVRtrTeLinkState.setObjects(
    ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkOperState")
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrTeLinkState.setStatus(
        "current"
    )


# Notifications groups

tmnxLmpVRtrNotifGroupV13v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 100, 2, 1, 8)
)
tmnxLmpVRtrNotifGroupV13v0.setObjects(
      *(("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkPropMismatch"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkPropMismatchClr"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrDbLinkPropMismatch"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrDbLinkPropMismatchClr"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrControlChannelState"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkState"))
)
if mibBuilder.loadTexts:
    tmnxLmpVRtrNotifGroupV13v0.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxLmpComplianceV13v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 100, 1, 1)
)
tmnxLmpComplianceV13v0.setObjects(
      *(("TIMETRA-LMP-MIB", "tmnxLmpVRtrGroupV13v0"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrPeerGroupV13v0"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcGroupV13v0"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkGroupV13v0"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrDbLinkGroupV13v0"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCcStatsGroupV13v0"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrTeLinkStatsGroupV13v0"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrNotifGroupV13v0"))
)
if mibBuilder.loadTexts:
    tmnxLmpComplianceV13v0.setStatus(
        "current"
    )

tmnxLmpComplianceV15v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 100, 1, 2)
)
tmnxLmpComplianceV15v0.setObjects(
      *(("TIMETRA-LMP-MIB", "tmnxLmpVRtrPeerGroupV15v0"),
        ("TIMETRA-LMP-MIB", "tmnxLmpVRtrCtrlChannelGroupV15v0"))
)
if mibBuilder.loadTexts:
    tmnxLmpComplianceV15v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-LMP-MIB",
    **{"timetraLmpMIBModule": timetraLmpMIBModule,
       "tmnxLmpConformance": tmnxLmpConformance,
       "tmnxLmpCompliances": tmnxLmpCompliances,
       "tmnxLmpComplianceV13v0": tmnxLmpComplianceV13v0,
       "tmnxLmpComplianceV15v0": tmnxLmpComplianceV15v0,
       "tmnxLmpGroups": tmnxLmpGroups,
       "tmnxLmpV13v0Groups": tmnxLmpV13v0Groups,
       "tmnxLmpVRtrGroupV13v0": tmnxLmpVRtrGroupV13v0,
       "tmnxLmpVRtrPeerGroupV13v0": tmnxLmpVRtrPeerGroupV13v0,
       "tmnxLmpVRtrCcGroupV13v0": tmnxLmpVRtrCcGroupV13v0,
       "tmnxLmpVRtrTeLinkGroupV13v0": tmnxLmpVRtrTeLinkGroupV13v0,
       "tmnxLmpVRtrDbLinkGroupV13v0": tmnxLmpVRtrDbLinkGroupV13v0,
       "tmnxLmpVRtrCcStatsGroupV13v0": tmnxLmpVRtrCcStatsGroupV13v0,
       "tmnxLmpVRtrTeLinkStatsGroupV13v0": tmnxLmpVRtrTeLinkStatsGroupV13v0,
       "tmnxLmpVRtrNotifGroupV13v0": tmnxLmpVRtrNotifGroupV13v0,
       "tmnxLmpV15v0Groups": tmnxLmpV15v0Groups,
       "tmnxLmpVRtrPeerGroupV15v0": tmnxLmpVRtrPeerGroupV15v0,
       "tmnxLmpVRtrCtrlChannelGroupV15v0": tmnxLmpVRtrCtrlChannelGroupV15v0,
       "tmnxLmpObjs": tmnxLmpObjs,
       "tmnxLmpConfigTimeStamps": tmnxLmpConfigTimeStamps,
       "tmnxLmpVRtrTableLastChanged": tmnxLmpVRtrTableLastChanged,
       "tmnxLmpVRtrPeerTableLastChanged": tmnxLmpVRtrPeerTableLastChanged,
       "tmnxLmpVRtrCcTableLastChanged": tmnxLmpVRtrCcTableLastChanged,
       "tmnxLmpVRtrTeLinkTableLastChange": tmnxLmpVRtrTeLinkTableLastChange,
       "tmnxLmpVRtrDbLinkTableLastChange": tmnxLmpVRtrDbLinkTableLastChange,
       "tmnxLmpConfigurations": tmnxLmpConfigurations,
       "tmnxLmpVRtrTable": tmnxLmpVRtrTable,
       "tmnxLmpVRtrEntry": tmnxLmpVRtrEntry,
       "tmnxLmpVRtrRowStatus": tmnxLmpVRtrRowStatus,
       "tmnxLmpVRtrLastChanged": tmnxLmpVRtrLastChanged,
       "tmnxLmpVRtrAdminState": tmnxLmpVRtrAdminState,
       "tmnxLmpVRtrOperState": tmnxLmpVRtrOperState,
       "tmnxLmpVRtrGmplsLoopbackAddrType": tmnxLmpVRtrGmplsLoopbackAddrType,
       "tmnxLmpVRtrGmplsLoopbackAddress": tmnxLmpVRtrGmplsLoopbackAddress,
       "tmnxLmpVRtrPeerTable": tmnxLmpVRtrPeerTable,
       "tmnxLmpVRtrPeerEntry": tmnxLmpVRtrPeerEntry,
       "tmnxLmpVRtrPeerNodeId": tmnxLmpVRtrPeerNodeId,
       "tmnxLmpVRtrPeerRowStatus": tmnxLmpVRtrPeerRowStatus,
       "tmnxLmpVRtrPeerLastChanged": tmnxLmpVRtrPeerLastChanged,
       "tmnxLmpVRtrPeerAdminState": tmnxLmpVRtrPeerAdminState,
       "tmnxLmpVRtrPeerOperState": tmnxLmpVRtrPeerOperState,
       "tmnxLmpVRtrPeerLoopbackAddrType": tmnxLmpVRtrPeerLoopbackAddrType,
       "tmnxLmpVRtrPeerLoopbackAddress": tmnxLmpVRtrPeerLoopbackAddress,
       "tmnxLmpVRtrPeerRetransmitIntvl": tmnxLmpVRtrPeerRetransmitIntvl,
       "tmnxLmpVRtrPeerRetryLimit": tmnxLmpVRtrPeerRetryLimit,
       "tmnxLmpVRtrPeerRetransmitDelta": tmnxLmpVRtrPeerRetransmitDelta,
       "tmnxLmpVRtrPeerCcVRtrId": tmnxLmpVRtrPeerCcVRtrId,
       "tmnxLmpVRtrPeerGmplsLpbkAddrType": tmnxLmpVRtrPeerGmplsLpbkAddrType,
       "tmnxLmpVRtrPeerGmplsLpbkAddress": tmnxLmpVRtrPeerGmplsLpbkAddress,
       "tmnxLmpVRtrControlChannelTable": tmnxLmpVRtrControlChannelTable,
       "tmnxLmpVRtrControlChannelEntry": tmnxLmpVRtrControlChannelEntry,
       "tmnxLmpVRtrCcId": tmnxLmpVRtrCcId,
       "tmnxLmpVRtrCcRowStatus": tmnxLmpVRtrCcRowStatus,
       "tmnxLmpVRtrCcLastChanged": tmnxLmpVRtrCcLastChanged,
       "tmnxLmpVRtrCcAdminState": tmnxLmpVRtrCcAdminState,
       "tmnxLmpVRtrCcOperState": tmnxLmpVRtrCcOperState,
       "tmnxLmpVRtrCcRemoteId": tmnxLmpVRtrCcRemoteId,
       "tmnxLmpVRtrCcPeerIfAddressType": tmnxLmpVRtrCcPeerIfAddressType,
       "tmnxLmpVRtrCcPeerIfAddress": tmnxLmpVRtrCcPeerIfAddress,
       "tmnxLmpVRtrCcSetupRole": tmnxLmpVRtrCcSetupRole,
       "tmnxLmpVRtrCcHelloInterval": tmnxLmpVRtrCcHelloInterval,
       "tmnxLmpVRtrCcHelloIntvNeg": tmnxLmpVRtrCcHelloIntvNeg,
       "tmnxLmpVRtrCcHelloDeadInterval": tmnxLmpVRtrCcHelloDeadInterval,
       "tmnxLmpVRtrCcHelloDeadIntvNeg": tmnxLmpVRtrCcHelloDeadIntvNeg,
       "tmnxLmpVRtrCcTtl": tmnxLmpVRtrCcTtl,
       "tmnxLmpVRtrCcIsTunneled": tmnxLmpVRtrCcIsTunneled,
       "tmnxLmpVRtrTeLinkTable": tmnxLmpVRtrTeLinkTable,
       "tmnxLmpVRtrTeLinkEntry": tmnxLmpVRtrTeLinkEntry,
       "tmnxLmpVRtrTeLinkId": tmnxLmpVRtrTeLinkId,
       "tmnxLmpVRtrTeLinkRowStatus": tmnxLmpVRtrTeLinkRowStatus,
       "tmnxLmpVRtrTeLinkLastChanged": tmnxLmpVRtrTeLinkLastChanged,
       "tmnxLmpVRtrTeLinkAdminState": tmnxLmpVRtrTeLinkAdminState,
       "tmnxLmpVRtrTeLinkOperState": tmnxLmpVRtrTeLinkOperState,
       "tmnxLmpVRtrTeLinkName": tmnxLmpVRtrTeLinkName,
       "tmnxLmpVRtrTeLinkRemoteId": tmnxLmpVRtrTeLinkRemoteId,
       "tmnxLmpVRtrTeLinkPeerNodeId": tmnxLmpVRtrTeLinkPeerNodeId,
       "tmnxLmpVRtrDbLinkTable": tmnxLmpVRtrDbLinkTable,
       "tmnxLmpVRtrDbLinkEntry": tmnxLmpVRtrDbLinkEntry,
       "tmnxLmpVRtrDbLinkId": tmnxLmpVRtrDbLinkId,
       "tmnxLmpVRtrDbLinkRowStatus": tmnxLmpVRtrDbLinkRowStatus,
       "tmnxLmpVRtrDbLinkLastChanged": tmnxLmpVRtrDbLinkLastChanged,
       "tmnxLmpVRtrDbLinkAdminState": tmnxLmpVRtrDbLinkAdminState,
       "tmnxLmpVRtrDbLinkOperState": tmnxLmpVRtrDbLinkOperState,
       "tmnxLmpVRtrDbLinkPortId": tmnxLmpVRtrDbLinkPortId,
       "tmnxLmpVRtrDbLinkRemoteId": tmnxLmpVRtrDbLinkRemoteId,
       "tmnxLmpVRtrDbLinkReasonDownFlags": tmnxLmpVRtrDbLinkReasonDownFlags,
       "tmnxLmpStatistics": tmnxLmpStatistics,
       "tmnxLmpVRtrControlChanStatsTable": tmnxLmpVRtrControlChanStatsTable,
       "tmnxLmpVRtrControlChanStatsEntry": tmnxLmpVRtrControlChanStatsEntry,
       "tmnxLmpVRtrCcInErrors": tmnxLmpVRtrCcInErrors,
       "tmnxLmpVRtrCcOutErrors": tmnxLmpVRtrCcOutErrors,
       "tmnxLmpVRtrCcConfigReceived": tmnxLmpVRtrCcConfigReceived,
       "tmnxLmpVRtrCcConfigSent": tmnxLmpVRtrCcConfigSent,
       "tmnxLmpVRtrCcConfigRetransmit": tmnxLmpVRtrCcConfigRetransmit,
       "tmnxLmpVRtrCcConfigAckReceived": tmnxLmpVRtrCcConfigAckReceived,
       "tmnxLmpVRtrCcConfigAckSent": tmnxLmpVRtrCcConfigAckSent,
       "tmnxLmpVRtrCcConfigNackReceived": tmnxLmpVRtrCcConfigNackReceived,
       "tmnxLmpVRtrCcConfigNackSent": tmnxLmpVRtrCcConfigNackSent,
       "tmnxLmpVRtrCcHelloReceived": tmnxLmpVRtrCcHelloReceived,
       "tmnxLmpVRtrCcHelloSent": tmnxLmpVRtrCcHelloSent,
       "tmnxLmpVRtrCcLinkSumReceived": tmnxLmpVRtrCcLinkSumReceived,
       "tmnxLmpVRtrCcLinkSumSent": tmnxLmpVRtrCcLinkSumSent,
       "tmnxLmpVRtrCcLinkSumRetransmit": tmnxLmpVRtrCcLinkSumRetransmit,
       "tmnxLmpVRtrCcLinkSumAckReceived": tmnxLmpVRtrCcLinkSumAckReceived,
       "tmnxLmpVRtrCcLinkSumAckSent": tmnxLmpVRtrCcLinkSumAckSent,
       "tmnxLmpVRtrCcLinkSumNackReceived": tmnxLmpVRtrCcLinkSumNackReceived,
       "tmnxLmpVRtrCcLinkSumNackSent": tmnxLmpVRtrCcLinkSumNackSent,
       "tmnxLmpVRtrCcDiscontinuityTime": tmnxLmpVRtrCcDiscontinuityTime,
       "tmnxLmpVRtrTeLinkStatsTable": tmnxLmpVRtrTeLinkStatsTable,
       "tmnxLmpVRtrTeLinkStatsEntry": tmnxLmpVRtrTeLinkStatsEntry,
       "tmnxLmpVRtrTeLinkSumReceived": tmnxLmpVRtrTeLinkSumReceived,
       "tmnxLmpVRtrTeLinkSumSent": tmnxLmpVRtrTeLinkSumSent,
       "tmnxLmpVRtrTeLinkSumRetransmit": tmnxLmpVRtrTeLinkSumRetransmit,
       "tmnxLmpVRtrTeLinkSumAckReceived": tmnxLmpVRtrTeLinkSumAckReceived,
       "tmnxLmpVRtrTeLinkSumAckSent": tmnxLmpVRtrTeLinkSumAckSent,
       "tmnxLmpVRtrTeLinkSumNackReceived": tmnxLmpVRtrTeLinkSumNackReceived,
       "tmnxLmpVRtrTeLinkSumNackSent": tmnxLmpVRtrTeLinkSumNackSent,
       "tmnxLmpVRtrTeLinkDiscntnuityTime": tmnxLmpVRtrTeLinkDiscntnuityTime,
       "tmnxLmpNotifyObjects": tmnxLmpNotifyObjects,
       "tmnxLmpNotifyPrefix": tmnxLmpNotifyPrefix,
       "tmnxLmpNotification": tmnxLmpNotification,
       "tmnxLmpVRtrTeLinkPropMismatch": tmnxLmpVRtrTeLinkPropMismatch,
       "tmnxLmpVRtrTeLinkPropMismatchClr": tmnxLmpVRtrTeLinkPropMismatchClr,
       "tmnxLmpVRtrDbLinkPropMismatch": tmnxLmpVRtrDbLinkPropMismatch,
       "tmnxLmpVRtrDbLinkPropMismatchClr": tmnxLmpVRtrDbLinkPropMismatchClr,
       "tmnxLmpVRtrControlChannelState": tmnxLmpVRtrControlChannelState,
       "tmnxLmpVRtrTeLinkState": tmnxLmpVRtrTeLinkState}
)
