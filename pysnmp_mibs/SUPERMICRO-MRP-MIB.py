# SNMP MIB module (SUPERMICRO-MRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-MRP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:29 2025
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

(ieee8021BridgeBaseComponentId,
 ieee8021BridgeBasePort,
 ieee8021BridgeBasePortComponentId) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgeBaseComponentId",
    "ieee8021BridgeBasePort",
    "ieee8021BridgeBasePortComponentId")

(IEEE8021BridgePortNumber,
 IEEE8021VlanIndex) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber",
    "IEEE8021VlanIndex")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsmrp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27)
)
if mibBuilder.loadTexts:
    fsmrp.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(TextualConvention, Integer32):
    status = "current"
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



class RegAdminControlType(TextualConvention, Integer32):
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
        *(("normal", 0),
          ("fixed", 1),
          ("forbidden", 2))
    )



# MIB Managed Objects in the order of their OIDs

_FsMrpScalars_ObjectIdentity = ObjectIdentity
fsMrpScalars = _FsMrpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 1)
)


class _FsMrpGlobalTraceOption_Type(TruthValue):
    """Custom type fsMrpGlobalTraceOption based on TruthValue"""
    defaultValue = 2


_FsMrpGlobalTraceOption_Type.__name__ = "TruthValue"
_FsMrpGlobalTraceOption_Object = MibScalar
fsMrpGlobalTraceOption = _FsMrpGlobalTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 1, 1),
    _FsMrpGlobalTraceOption_Type()
)
fsMrpGlobalTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMrpGlobalTraceOption.setStatus("current")
_FsMrpInstance_ObjectIdentity = ObjectIdentity
fsMrpInstance = _FsMrpInstance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 2)
)
_FsMrpInstanceTable_Object = MibTable
fsMrpInstanceTable = _FsMrpInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 2, 1)
)
if mibBuilder.loadTexts:
    fsMrpInstanceTable.setStatus("current")
_FsMrpInstanceEntry_Object = MibTableRow
fsMrpInstanceEntry = _FsMrpInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 2, 1, 1)
)
fsMrpInstanceEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
)
if mibBuilder.loadTexts:
    fsMrpInstanceEntry.setStatus("current")


class _FsMrpInstanceSystemControl_Type(Integer32):
    """Custom type fsMrpInstanceSystemControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsMrpInstanceSystemControl_Type.__name__ = "Integer32"
_FsMrpInstanceSystemControl_Object = MibTableColumn
fsMrpInstanceSystemControl = _FsMrpInstanceSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 2, 1, 1, 1),
    _FsMrpInstanceSystemControl_Type()
)
fsMrpInstanceSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMrpInstanceSystemControl.setStatus("current")


class _FsMrpInstanceTraceInputString_Type(DisplayString):
    """Custom type fsMrpInstanceTraceInputString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsMrpInstanceTraceInputString_Type.__name__ = "DisplayString"
_FsMrpInstanceTraceInputString_Object = MibTableColumn
fsMrpInstanceTraceInputString = _FsMrpInstanceTraceInputString_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 2, 1, 1, 2),
    _FsMrpInstanceTraceInputString_Type()
)
fsMrpInstanceTraceInputString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMrpInstanceTraceInputString.setStatus("current")


class _FsMrpInstanceNotifyVlanRegFailure_Type(TruthValue):
    """Custom type fsMrpInstanceNotifyVlanRegFailure based on TruthValue"""
    defaultValue = 2


_FsMrpInstanceNotifyVlanRegFailure_Type.__name__ = "TruthValue"
_FsMrpInstanceNotifyVlanRegFailure_Object = MibTableColumn
fsMrpInstanceNotifyVlanRegFailure = _FsMrpInstanceNotifyVlanRegFailure_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 2, 1, 1, 3),
    _FsMrpInstanceNotifyVlanRegFailure_Type()
)
fsMrpInstanceNotifyVlanRegFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMrpInstanceNotifyVlanRegFailure.setStatus("current")


class _FsMrpInstanceNotifyMacRegFailure_Type(TruthValue):
    """Custom type fsMrpInstanceNotifyMacRegFailure based on TruthValue"""
    defaultValue = 2


_FsMrpInstanceNotifyMacRegFailure_Type.__name__ = "TruthValue"
_FsMrpInstanceNotifyMacRegFailure_Object = MibTableColumn
fsMrpInstanceNotifyMacRegFailure = _FsMrpInstanceNotifyMacRegFailure_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 2, 1, 1, 4),
    _FsMrpInstanceNotifyMacRegFailure_Type()
)
fsMrpInstanceNotifyMacRegFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMrpInstanceNotifyMacRegFailure.setStatus("current")


class _FsMrpInstanceBridgeMmrpEnabledStatus_Type(TruthValue):
    """Custom type fsMrpInstanceBridgeMmrpEnabledStatus based on TruthValue"""
    defaultValue = 1


_FsMrpInstanceBridgeMmrpEnabledStatus_Type.__name__ = "TruthValue"
_FsMrpInstanceBridgeMmrpEnabledStatus_Object = MibTableColumn
fsMrpInstanceBridgeMmrpEnabledStatus = _FsMrpInstanceBridgeMmrpEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 2, 1, 1, 5),
    _FsMrpInstanceBridgeMmrpEnabledStatus_Type()
)
fsMrpInstanceBridgeMmrpEnabledStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMrpInstanceBridgeMmrpEnabledStatus.setStatus("current")


class _FsMrpInstanceBridgeMvrpEnabledStatus_Type(TruthValue):
    """Custom type fsMrpInstanceBridgeMvrpEnabledStatus based on TruthValue"""
    defaultValue = 1


_FsMrpInstanceBridgeMvrpEnabledStatus_Type.__name__ = "TruthValue"
_FsMrpInstanceBridgeMvrpEnabledStatus_Object = MibTableColumn
fsMrpInstanceBridgeMvrpEnabledStatus = _FsMrpInstanceBridgeMvrpEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 2, 1, 1, 6),
    _FsMrpInstanceBridgeMvrpEnabledStatus_Type()
)
fsMrpInstanceBridgeMvrpEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMrpInstanceBridgeMvrpEnabledStatus.setStatus("current")
_FsMrpPortConfig_ObjectIdentity = ObjectIdentity
fsMrpPortConfig = _FsMrpPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 3)
)
_FsMrpPortTable_Object = MibTable
fsMrpPortTable = _FsMrpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 3, 1)
)
if mibBuilder.loadTexts:
    fsMrpPortTable.setStatus("current")
_FsMrpPortEntry_Object = MibTableRow
fsMrpPortEntry = _FsMrpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 3, 1, 1)
)
fsMrpPortEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
)
if mibBuilder.loadTexts:
    fsMrpPortEntry.setStatus("current")


class _FsMrpPortPeriodicSEMStatus_Type(EnabledStatus):
    """Custom type fsMrpPortPeriodicSEMStatus based on EnabledStatus"""
    defaultValue = 2


_FsMrpPortPeriodicSEMStatus_Type.__name__ = "EnabledStatus"
_FsMrpPortPeriodicSEMStatus_Object = MibTableColumn
fsMrpPortPeriodicSEMStatus = _FsMrpPortPeriodicSEMStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 3, 1, 1, 1),
    _FsMrpPortPeriodicSEMStatus_Type()
)
fsMrpPortPeriodicSEMStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMrpPortPeriodicSEMStatus.setStatus("current")


class _FsMrpPortParticipantType_Type(Integer32):
    """Custom type fsMrpPortParticipantType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullParticipant", 1),
          ("applicantOnly", 2))
    )


_FsMrpPortParticipantType_Type.__name__ = "Integer32"
_FsMrpPortParticipantType_Object = MibTableColumn
fsMrpPortParticipantType = _FsMrpPortParticipantType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 3, 1, 1, 2),
    _FsMrpPortParticipantType_Type()
)
fsMrpPortParticipantType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMrpPortParticipantType.setStatus("current")


class _FsMrpPortRegAdminControl_Type(RegAdminControlType):
    """Custom type fsMrpPortRegAdminControl based on RegAdminControlType"""
    defaultValue = 0


_FsMrpPortRegAdminControl_Type.__name__ = "RegAdminControlType"
_FsMrpPortRegAdminControl_Object = MibTableColumn
fsMrpPortRegAdminControl = _FsMrpPortRegAdminControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 3, 1, 1, 3),
    _FsMrpPortRegAdminControl_Type()
)
fsMrpPortRegAdminControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMrpPortRegAdminControl.setStatus("current")


class _FsMrpPortRestrictedGroupRegistration_Type(TruthValue):
    """Custom type fsMrpPortRestrictedGroupRegistration based on TruthValue"""
    defaultValue = 2


_FsMrpPortRestrictedGroupRegistration_Type.__name__ = "TruthValue"
_FsMrpPortRestrictedGroupRegistration_Object = MibTableColumn
fsMrpPortRestrictedGroupRegistration = _FsMrpPortRestrictedGroupRegistration_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 3, 1, 1, 4),
    _FsMrpPortRestrictedGroupRegistration_Type()
)
fsMrpPortRestrictedGroupRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMrpPortRestrictedGroupRegistration.setStatus("current")


class _FsMrpPortRestrictedVlanRegistration_Type(TruthValue):
    """Custom type fsMrpPortRestrictedVlanRegistration based on TruthValue"""
    defaultValue = 2


_FsMrpPortRestrictedVlanRegistration_Type.__name__ = "TruthValue"
_FsMrpPortRestrictedVlanRegistration_Object = MibTableColumn
fsMrpPortRestrictedVlanRegistration = _FsMrpPortRestrictedVlanRegistration_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 3, 1, 1, 5),
    _FsMrpPortRestrictedVlanRegistration_Type()
)
fsMrpPortRestrictedVlanRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMrpPortRestrictedVlanRegistration.setStatus("current")
_FsMvrpPortTable_Object = MibTable
fsMvrpPortTable = _FsMvrpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 3, 2)
)
if mibBuilder.loadTexts:
    fsMvrpPortTable.setStatus("current")
_FsMvrpPortEntry_Object = MibTableRow
fsMvrpPortEntry = _FsMvrpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 3, 2, 1)
)
fsMvrpPortEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
)
if mibBuilder.loadTexts:
    fsMvrpPortEntry.setStatus("current")


class _FsMvrpPortMvrpEnabledStatus_Type(TruthValue):
    """Custom type fsMvrpPortMvrpEnabledStatus based on TruthValue"""
    defaultValue = 1


_FsMvrpPortMvrpEnabledStatus_Type.__name__ = "TruthValue"
_FsMvrpPortMvrpEnabledStatus_Object = MibTableColumn
fsMvrpPortMvrpEnabledStatus = _FsMvrpPortMvrpEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 3, 2, 1, 1),
    _FsMvrpPortMvrpEnabledStatus_Type()
)
fsMvrpPortMvrpEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMvrpPortMvrpEnabledStatus.setStatus("current")
_FsMvrpPortMvrpFailedRegistrations_Type = Counter64
_FsMvrpPortMvrpFailedRegistrations_Object = MibTableColumn
fsMvrpPortMvrpFailedRegistrations = _FsMvrpPortMvrpFailedRegistrations_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 3, 2, 1, 2),
    _FsMvrpPortMvrpFailedRegistrations_Type()
)
fsMvrpPortMvrpFailedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMvrpPortMvrpFailedRegistrations.setStatus("current")
if mibBuilder.loadTexts:
    fsMvrpPortMvrpFailedRegistrations.setUnits("failed MVRP registrations")
_FsMvrpPortMvrpLastPduOrigin_Type = MacAddress
_FsMvrpPortMvrpLastPduOrigin_Object = MibTableColumn
fsMvrpPortMvrpLastPduOrigin = _FsMvrpPortMvrpLastPduOrigin_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 3, 2, 1, 3),
    _FsMvrpPortMvrpLastPduOrigin_Type()
)
fsMvrpPortMvrpLastPduOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMvrpPortMvrpLastPduOrigin.setStatus("current")
_FsMrpStatistics_ObjectIdentity = ObjectIdentity
fsMrpStatistics = _FsMrpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4)
)
_FsMrpPortStatsTable_Object = MibTable
fsMrpPortStatsTable = _FsMrpPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1)
)
if mibBuilder.loadTexts:
    fsMrpPortStatsTable.setStatus("current")
_FsMrpPortStatsEntry_Object = MibTableRow
fsMrpPortStatsEntry = _FsMrpPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1, 1)
)
fsMrpPortStatsEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "SUPERMICRO-MRP-MIB", "fsMrpApplicationAddress"),
)
if mibBuilder.loadTexts:
    fsMrpPortStatsEntry.setStatus("current")


class _FsMrpPortStatsClearStatistics_Type(TruthValue):
    """Custom type fsMrpPortStatsClearStatistics based on TruthValue"""
    defaultValue = 2


_FsMrpPortStatsClearStatistics_Type.__name__ = "TruthValue"
_FsMrpPortStatsClearStatistics_Object = MibTableColumn
fsMrpPortStatsClearStatistics = _FsMrpPortStatsClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1, 1, 1),
    _FsMrpPortStatsClearStatistics_Type()
)
fsMrpPortStatsClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMrpPortStatsClearStatistics.setStatus("current")
_FsMrpPortStatsNumberOfRegistrations_Type = Counter64
_FsMrpPortStatsNumberOfRegistrations_Object = MibTableColumn
fsMrpPortStatsNumberOfRegistrations = _FsMrpPortStatsNumberOfRegistrations_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1, 1, 2),
    _FsMrpPortStatsNumberOfRegistrations_Type()
)
fsMrpPortStatsNumberOfRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpPortStatsNumberOfRegistrations.setStatus("current")
_FsMrpPortStatsRxValidPduCount_Type = Counter64
_FsMrpPortStatsRxValidPduCount_Object = MibTableColumn
fsMrpPortStatsRxValidPduCount = _FsMrpPortStatsRxValidPduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1, 1, 3),
    _FsMrpPortStatsRxValidPduCount_Type()
)
fsMrpPortStatsRxValidPduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpPortStatsRxValidPduCount.setStatus("current")
_FsMrpPortStatsRxInvalidPduCount_Type = Counter64
_FsMrpPortStatsRxInvalidPduCount_Object = MibTableColumn
fsMrpPortStatsRxInvalidPduCount = _FsMrpPortStatsRxInvalidPduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1, 1, 4),
    _FsMrpPortStatsRxInvalidPduCount_Type()
)
fsMrpPortStatsRxInvalidPduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpPortStatsRxInvalidPduCount.setStatus("current")
_FsMrpPortStatsRxNewMsgCount_Type = Counter64
_FsMrpPortStatsRxNewMsgCount_Object = MibTableColumn
fsMrpPortStatsRxNewMsgCount = _FsMrpPortStatsRxNewMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1, 1, 5),
    _FsMrpPortStatsRxNewMsgCount_Type()
)
fsMrpPortStatsRxNewMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpPortStatsRxNewMsgCount.setStatus("current")
_FsMrpPortStatsRxJoinInMsgCount_Type = Counter64
_FsMrpPortStatsRxJoinInMsgCount_Object = MibTableColumn
fsMrpPortStatsRxJoinInMsgCount = _FsMrpPortStatsRxJoinInMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1, 1, 6),
    _FsMrpPortStatsRxJoinInMsgCount_Type()
)
fsMrpPortStatsRxJoinInMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpPortStatsRxJoinInMsgCount.setStatus("current")
_FsMrpPortStatsRxJoinMtMsgCount_Type = Counter64
_FsMrpPortStatsRxJoinMtMsgCount_Object = MibTableColumn
fsMrpPortStatsRxJoinMtMsgCount = _FsMrpPortStatsRxJoinMtMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1, 1, 7),
    _FsMrpPortStatsRxJoinMtMsgCount_Type()
)
fsMrpPortStatsRxJoinMtMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpPortStatsRxJoinMtMsgCount.setStatus("current")
_FsMrpPortStatsRxLeaveMsgCount_Type = Counter64
_FsMrpPortStatsRxLeaveMsgCount_Object = MibTableColumn
fsMrpPortStatsRxLeaveMsgCount = _FsMrpPortStatsRxLeaveMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1, 1, 8),
    _FsMrpPortStatsRxLeaveMsgCount_Type()
)
fsMrpPortStatsRxLeaveMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpPortStatsRxLeaveMsgCount.setStatus("current")
_FsMrpPortStatsRxEmptyMsgCount_Type = Counter64
_FsMrpPortStatsRxEmptyMsgCount_Object = MibTableColumn
fsMrpPortStatsRxEmptyMsgCount = _FsMrpPortStatsRxEmptyMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1, 1, 9),
    _FsMrpPortStatsRxEmptyMsgCount_Type()
)
fsMrpPortStatsRxEmptyMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpPortStatsRxEmptyMsgCount.setStatus("current")
_FsMrpPortStatsRxInMsgCount_Type = Counter64
_FsMrpPortStatsRxInMsgCount_Object = MibTableColumn
fsMrpPortStatsRxInMsgCount = _FsMrpPortStatsRxInMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1, 1, 10),
    _FsMrpPortStatsRxInMsgCount_Type()
)
fsMrpPortStatsRxInMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpPortStatsRxInMsgCount.setStatus("current")
_FsMrpPortStatsRxLeaveAllMsgCount_Type = Counter64
_FsMrpPortStatsRxLeaveAllMsgCount_Object = MibTableColumn
fsMrpPortStatsRxLeaveAllMsgCount = _FsMrpPortStatsRxLeaveAllMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1, 1, 11),
    _FsMrpPortStatsRxLeaveAllMsgCount_Type()
)
fsMrpPortStatsRxLeaveAllMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpPortStatsRxLeaveAllMsgCount.setStatus("current")
_FsMrpPortStatsTxPduCount_Type = Counter64
_FsMrpPortStatsTxPduCount_Object = MibTableColumn
fsMrpPortStatsTxPduCount = _FsMrpPortStatsTxPduCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1, 1, 12),
    _FsMrpPortStatsTxPduCount_Type()
)
fsMrpPortStatsTxPduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpPortStatsTxPduCount.setStatus("current")
_FsMrpPortStatsTxNewMsgCount_Type = Counter64
_FsMrpPortStatsTxNewMsgCount_Object = MibTableColumn
fsMrpPortStatsTxNewMsgCount = _FsMrpPortStatsTxNewMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1, 1, 13),
    _FsMrpPortStatsTxNewMsgCount_Type()
)
fsMrpPortStatsTxNewMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpPortStatsTxNewMsgCount.setStatus("current")
_FsMrpPortStatsTxJoinInMsgCount_Type = Counter64
_FsMrpPortStatsTxJoinInMsgCount_Object = MibTableColumn
fsMrpPortStatsTxJoinInMsgCount = _FsMrpPortStatsTxJoinInMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1, 1, 14),
    _FsMrpPortStatsTxJoinInMsgCount_Type()
)
fsMrpPortStatsTxJoinInMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpPortStatsTxJoinInMsgCount.setStatus("current")
_FsMrpPortStatsTxJoinMtMsgCount_Type = Counter64
_FsMrpPortStatsTxJoinMtMsgCount_Object = MibTableColumn
fsMrpPortStatsTxJoinMtMsgCount = _FsMrpPortStatsTxJoinMtMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1, 1, 15),
    _FsMrpPortStatsTxJoinMtMsgCount_Type()
)
fsMrpPortStatsTxJoinMtMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpPortStatsTxJoinMtMsgCount.setStatus("current")
_FsMrpPortStatsTxLeaveMsgCount_Type = Counter64
_FsMrpPortStatsTxLeaveMsgCount_Object = MibTableColumn
fsMrpPortStatsTxLeaveMsgCount = _FsMrpPortStatsTxLeaveMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1, 1, 16),
    _FsMrpPortStatsTxLeaveMsgCount_Type()
)
fsMrpPortStatsTxLeaveMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpPortStatsTxLeaveMsgCount.setStatus("current")
_FsMrpPortStatsTxEmptyMsgCount_Type = Counter64
_FsMrpPortStatsTxEmptyMsgCount_Object = MibTableColumn
fsMrpPortStatsTxEmptyMsgCount = _FsMrpPortStatsTxEmptyMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1, 1, 17),
    _FsMrpPortStatsTxEmptyMsgCount_Type()
)
fsMrpPortStatsTxEmptyMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpPortStatsTxEmptyMsgCount.setStatus("current")
_FsMrpPortStatsTxInMsgCount_Type = Counter64
_FsMrpPortStatsTxInMsgCount_Object = MibTableColumn
fsMrpPortStatsTxInMsgCount = _FsMrpPortStatsTxInMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1, 1, 18),
    _FsMrpPortStatsTxInMsgCount_Type()
)
fsMrpPortStatsTxInMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpPortStatsTxInMsgCount.setStatus("current")
_FsMrpPortStatsTxLeaveAllMsgCount_Type = Counter64
_FsMrpPortStatsTxLeaveAllMsgCount_Object = MibTableColumn
fsMrpPortStatsTxLeaveAllMsgCount = _FsMrpPortStatsTxLeaveAllMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 4, 1, 1, 19),
    _FsMrpPortStatsTxLeaveAllMsgCount_Type()
)
fsMrpPortStatsTxLeaveAllMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpPortStatsTxLeaveAllMsgCount.setStatus("current")
_FsMrpApplicantInfo_ObjectIdentity = ObjectIdentity
fsMrpApplicantInfo = _FsMrpApplicantInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 5)
)
_FsMrpApplicantControlTable_Object = MibTable
fsMrpApplicantControlTable = _FsMrpApplicantControlTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 5, 1)
)
if mibBuilder.loadTexts:
    fsMrpApplicantControlTable.setStatus("current")
_FsMrpApplicantControlEntry_Object = MibTableRow
fsMrpApplicantControlEntry = _FsMrpApplicantControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 5, 1, 1)
)
fsMrpApplicantControlEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "SUPERMICRO-MRP-MIB", "fsMrpApplicationAddress"),
    (0, "SUPERMICRO-MRP-MIB", "fsMrpAttributeType"),
)
if mibBuilder.loadTexts:
    fsMrpApplicantControlEntry.setStatus("current")
_FsMrpApplicationAddress_Type = MacAddress
_FsMrpApplicationAddress_Object = MibTableColumn
fsMrpApplicationAddress = _FsMrpApplicationAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 5, 1, 1, 1),
    _FsMrpApplicationAddress_Type()
)
fsMrpApplicationAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMrpApplicationAddress.setStatus("current")


class _FsMrpAttributeType_Type(Integer32):
    """Custom type fsMrpAttributeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsMrpAttributeType_Type.__name__ = "Integer32"
_FsMrpAttributeType_Object = MibTableColumn
fsMrpAttributeType = _FsMrpAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 5, 1, 1, 2),
    _FsMrpAttributeType_Type()
)
fsMrpAttributeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMrpAttributeType.setStatus("current")


class _FsMrpApplicantControlAdminStatus_Type(Integer32):
    """Custom type fsMrpApplicantControlAdminStatus based on Integer32"""
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
        *(("normal", 1),
          ("nonParticipant", 2),
          ("active", 3))
    )


_FsMrpApplicantControlAdminStatus_Type.__name__ = "Integer32"
_FsMrpApplicantControlAdminStatus_Object = MibTableColumn
fsMrpApplicantControlAdminStatus = _FsMrpApplicantControlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 5, 1, 1, 3),
    _FsMrpApplicantControlAdminStatus_Type()
)
fsMrpApplicantControlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMrpApplicantControlAdminStatus.setStatus("current")
_FsMrpStateMachine_ObjectIdentity = ObjectIdentity
fsMrpStateMachine = _FsMrpStateMachine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 6)
)
_FsMrpSEMTable_Object = MibTable
fsMrpSEMTable = _FsMrpSEMTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 6, 1)
)
if mibBuilder.loadTexts:
    fsMrpSEMTable.setStatus("current")
_FsMrpSEMEntry_Object = MibTableRow
fsMrpSEMEntry = _FsMrpSEMEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 6, 1, 1)
)
fsMrpSEMEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "SUPERMICRO-MRP-MIB", "fsMrpApplicationAddress"),
    (0, "SUPERMICRO-MRP-MIB", "fsMrpSEMMapContext"),
    (0, "SUPERMICRO-MRP-MIB", "fsMrpAttributeType"),
    (0, "SUPERMICRO-MRP-MIB", "fsMrpSEMAttributeValue"),
)
if mibBuilder.loadTexts:
    fsMrpSEMEntry.setStatus("current")


class _FsMrpSEMMapContext_Type(Integer32):
    """Custom type fsMrpSEMMapContext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_FsMrpSEMMapContext_Type.__name__ = "Integer32"
_FsMrpSEMMapContext_Object = MibTableColumn
fsMrpSEMMapContext = _FsMrpSEMMapContext_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 6, 1, 1, 1),
    _FsMrpSEMMapContext_Type()
)
fsMrpSEMMapContext.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMrpSEMMapContext.setStatus("current")


class _FsMrpSEMAttributeValue_Type(OctetString):
    """Custom type fsMrpSEMAttributeValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_FsMrpSEMAttributeValue_Type.__name__ = "OctetString"
_FsMrpSEMAttributeValue_Object = MibTableColumn
fsMrpSEMAttributeValue = _FsMrpSEMAttributeValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 6, 1, 1, 2),
    _FsMrpSEMAttributeValue_Type()
)
fsMrpSEMAttributeValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMrpSEMAttributeValue.setStatus("current")


class _FsMrpSEMApplicantState_Type(Integer32):
    """Custom type fsMrpSEMApplicantState based on Integer32"""
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
        *(("vo", 0),
          ("vp", 1),
          ("vn", 2),
          ("an", 3),
          ("aa", 4),
          ("qa", 5),
          ("la", 6),
          ("ao", 7),
          ("qo", 8),
          ("ap", 9),
          ("qp", 10),
          ("lo", 11))
    )


_FsMrpSEMApplicantState_Type.__name__ = "Integer32"
_FsMrpSEMApplicantState_Object = MibTableColumn
fsMrpSEMApplicantState = _FsMrpSEMApplicantState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 6, 1, 1, 3),
    _FsMrpSEMApplicantState_Type()
)
fsMrpSEMApplicantState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpSEMApplicantState.setStatus("current")


class _FsMrpSEMRegistrarState_Type(Integer32):
    """Custom type fsMrpSEMRegistrarState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mt", 0),
          ("in", 1),
          ("lv", 2))
    )


_FsMrpSEMRegistrarState_Type.__name__ = "Integer32"
_FsMrpSEMRegistrarState_Object = MibTableColumn
fsMrpSEMRegistrarState = _FsMrpSEMRegistrarState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 6, 1, 1, 4),
    _FsMrpSEMRegistrarState_Type()
)
fsMrpSEMRegistrarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpSEMRegistrarState.setStatus("current")
_FsMrpSEMOriginatorAddress_Type = MacAddress
_FsMrpSEMOriginatorAddress_Object = MibTableColumn
fsMrpSEMOriginatorAddress = _FsMrpSEMOriginatorAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 6, 1, 1, 5),
    _FsMrpSEMOriginatorAddress_Type()
)
fsMrpSEMOriginatorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMrpSEMOriginatorAddress.setStatus("current")
_FsMrpTraps_ObjectIdentity = ObjectIdentity
fsMrpTraps = _FsMrpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 7)
)
_FsMrpTrapNotificationCtrl_ObjectIdentity = ObjectIdentity
fsMrpTrapNotificationCtrl = _FsMrpTrapNotificationCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 7, 0)
)


class _FsMrpTrapContextName_Type(DisplayString):
    """Custom type fsMrpTrapContextName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsMrpTrapContextName_Type.__name__ = "DisplayString"
_FsMrpTrapContextName_Object = MibScalar
fsMrpTrapContextName = _FsMrpTrapContextName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 7, 1),
    _FsMrpTrapContextName_Type()
)
fsMrpTrapContextName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMrpTrapContextName.setStatus("current")
_FsMrpTrapBridgeBasePort_Type = IEEE8021BridgePortNumber
_FsMrpTrapBridgeBasePort_Object = MibScalar
fsMrpTrapBridgeBasePort = _FsMrpTrapBridgeBasePort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 7, 2),
    _FsMrpTrapBridgeBasePort_Type()
)
fsMrpTrapBridgeBasePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMrpTrapBridgeBasePort.setStatus("current")
_FsMrpTrapMvrpAttributeValue_Type = IEEE8021VlanIndex
_FsMrpTrapMvrpAttributeValue_Object = MibScalar
fsMrpTrapMvrpAttributeValue = _FsMrpTrapMvrpAttributeValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 7, 3),
    _FsMrpTrapMvrpAttributeValue_Type()
)
fsMrpTrapMvrpAttributeValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMrpTrapMvrpAttributeValue.setStatus("current")
_FsMrpTrapMmrpAttributeValue_Type = MacAddress
_FsMrpTrapMmrpAttributeValue_Object = MibScalar
fsMrpTrapMmrpAttributeValue = _FsMrpTrapMmrpAttributeValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 7, 4),
    _FsMrpTrapMmrpAttributeValue_Type()
)
fsMrpTrapMmrpAttributeValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMrpTrapMmrpAttributeValue.setStatus("current")
_FsMrpTrapAttrRegFailureReason_Type = DisplayString
_FsMrpTrapAttrRegFailureReason_Object = MibScalar
fsMrpTrapAttrRegFailureReason = _FsMrpTrapAttrRegFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 7, 5),
    _FsMrpTrapAttrRegFailureReason_Type()
)
fsMrpTrapAttrRegFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMrpTrapAttrRegFailureReason.setStatus("current")

# Managed Objects groups


# Notification objects

fsMrpVlanRegFailureNotifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 7, 0, 1)
)
fsMrpVlanRegFailureNotifyTrap.setObjects(
      *(("SUPERMICRO-MRP-MIB", "fsMrpTrapContextName"),
        ("SUPERMICRO-MRP-MIB", "fsMrpTrapBridgeBasePort"),
        ("SUPERMICRO-MRP-MIB", "fsMrpTrapMvrpAttributeValue"),
        ("SUPERMICRO-MRP-MIB", "fsMrpTrapAttrRegFailureReason"))
)
if mibBuilder.loadTexts:
    fsMrpVlanRegFailureNotifyTrap.setStatus(
        "current"
    )

fsMrpMacRegFailureNotifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 27, 7, 0, 2)
)
fsMrpMacRegFailureNotifyTrap.setObjects(
      *(("SUPERMICRO-MRP-MIB", "fsMrpTrapContextName"),
        ("SUPERMICRO-MRP-MIB", "fsMrpTrapBridgeBasePort"),
        ("SUPERMICRO-MRP-MIB", "fsMrpTrapMmrpAttributeValue"),
        ("SUPERMICRO-MRP-MIB", "fsMrpTrapAttrRegFailureReason"))
)
if mibBuilder.loadTexts:
    fsMrpMacRegFailureNotifyTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-MRP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "RegAdminControlType": RegAdminControlType,
       "fsmrp": fsmrp,
       "fsMrpScalars": fsMrpScalars,
       "fsMrpGlobalTraceOption": fsMrpGlobalTraceOption,
       "fsMrpInstance": fsMrpInstance,
       "fsMrpInstanceTable": fsMrpInstanceTable,
       "fsMrpInstanceEntry": fsMrpInstanceEntry,
       "fsMrpInstanceSystemControl": fsMrpInstanceSystemControl,
       "fsMrpInstanceTraceInputString": fsMrpInstanceTraceInputString,
       "fsMrpInstanceNotifyVlanRegFailure": fsMrpInstanceNotifyVlanRegFailure,
       "fsMrpInstanceNotifyMacRegFailure": fsMrpInstanceNotifyMacRegFailure,
       "fsMrpInstanceBridgeMmrpEnabledStatus": fsMrpInstanceBridgeMmrpEnabledStatus,
       "fsMrpInstanceBridgeMvrpEnabledStatus": fsMrpInstanceBridgeMvrpEnabledStatus,
       "fsMrpPortConfig": fsMrpPortConfig,
       "fsMrpPortTable": fsMrpPortTable,
       "fsMrpPortEntry": fsMrpPortEntry,
       "fsMrpPortPeriodicSEMStatus": fsMrpPortPeriodicSEMStatus,
       "fsMrpPortParticipantType": fsMrpPortParticipantType,
       "fsMrpPortRegAdminControl": fsMrpPortRegAdminControl,
       "fsMrpPortRestrictedGroupRegistration": fsMrpPortRestrictedGroupRegistration,
       "fsMrpPortRestrictedVlanRegistration": fsMrpPortRestrictedVlanRegistration,
       "fsMvrpPortTable": fsMvrpPortTable,
       "fsMvrpPortEntry": fsMvrpPortEntry,
       "fsMvrpPortMvrpEnabledStatus": fsMvrpPortMvrpEnabledStatus,
       "fsMvrpPortMvrpFailedRegistrations": fsMvrpPortMvrpFailedRegistrations,
       "fsMvrpPortMvrpLastPduOrigin": fsMvrpPortMvrpLastPduOrigin,
       "fsMrpStatistics": fsMrpStatistics,
       "fsMrpPortStatsTable": fsMrpPortStatsTable,
       "fsMrpPortStatsEntry": fsMrpPortStatsEntry,
       "fsMrpPortStatsClearStatistics": fsMrpPortStatsClearStatistics,
       "fsMrpPortStatsNumberOfRegistrations": fsMrpPortStatsNumberOfRegistrations,
       "fsMrpPortStatsRxValidPduCount": fsMrpPortStatsRxValidPduCount,
       "fsMrpPortStatsRxInvalidPduCount": fsMrpPortStatsRxInvalidPduCount,
       "fsMrpPortStatsRxNewMsgCount": fsMrpPortStatsRxNewMsgCount,
       "fsMrpPortStatsRxJoinInMsgCount": fsMrpPortStatsRxJoinInMsgCount,
       "fsMrpPortStatsRxJoinMtMsgCount": fsMrpPortStatsRxJoinMtMsgCount,
       "fsMrpPortStatsRxLeaveMsgCount": fsMrpPortStatsRxLeaveMsgCount,
       "fsMrpPortStatsRxEmptyMsgCount": fsMrpPortStatsRxEmptyMsgCount,
       "fsMrpPortStatsRxInMsgCount": fsMrpPortStatsRxInMsgCount,
       "fsMrpPortStatsRxLeaveAllMsgCount": fsMrpPortStatsRxLeaveAllMsgCount,
       "fsMrpPortStatsTxPduCount": fsMrpPortStatsTxPduCount,
       "fsMrpPortStatsTxNewMsgCount": fsMrpPortStatsTxNewMsgCount,
       "fsMrpPortStatsTxJoinInMsgCount": fsMrpPortStatsTxJoinInMsgCount,
       "fsMrpPortStatsTxJoinMtMsgCount": fsMrpPortStatsTxJoinMtMsgCount,
       "fsMrpPortStatsTxLeaveMsgCount": fsMrpPortStatsTxLeaveMsgCount,
       "fsMrpPortStatsTxEmptyMsgCount": fsMrpPortStatsTxEmptyMsgCount,
       "fsMrpPortStatsTxInMsgCount": fsMrpPortStatsTxInMsgCount,
       "fsMrpPortStatsTxLeaveAllMsgCount": fsMrpPortStatsTxLeaveAllMsgCount,
       "fsMrpApplicantInfo": fsMrpApplicantInfo,
       "fsMrpApplicantControlTable": fsMrpApplicantControlTable,
       "fsMrpApplicantControlEntry": fsMrpApplicantControlEntry,
       "fsMrpApplicationAddress": fsMrpApplicationAddress,
       "fsMrpAttributeType": fsMrpAttributeType,
       "fsMrpApplicantControlAdminStatus": fsMrpApplicantControlAdminStatus,
       "fsMrpStateMachine": fsMrpStateMachine,
       "fsMrpSEMTable": fsMrpSEMTable,
       "fsMrpSEMEntry": fsMrpSEMEntry,
       "fsMrpSEMMapContext": fsMrpSEMMapContext,
       "fsMrpSEMAttributeValue": fsMrpSEMAttributeValue,
       "fsMrpSEMApplicantState": fsMrpSEMApplicantState,
       "fsMrpSEMRegistrarState": fsMrpSEMRegistrarState,
       "fsMrpSEMOriginatorAddress": fsMrpSEMOriginatorAddress,
       "fsMrpTraps": fsMrpTraps,
       "fsMrpTrapNotificationCtrl": fsMrpTrapNotificationCtrl,
       "fsMrpVlanRegFailureNotifyTrap": fsMrpVlanRegFailureNotifyTrap,
       "fsMrpMacRegFailureNotifyTrap": fsMrpMacRegFailureNotifyTrap,
       "fsMrpTrapContextName": fsMrpTrapContextName,
       "fsMrpTrapBridgeBasePort": fsMrpTrapBridgeBasePort,
       "fsMrpTrapMvrpAttributeValue": fsMrpTrapMvrpAttributeValue,
       "fsMrpTrapMmrpAttributeValue": fsMrpTrapMmrpAttributeValue,
       "fsMrpTrapAttrRegFailureReason": fsMrpTrapAttrRegFailureReason}
)
