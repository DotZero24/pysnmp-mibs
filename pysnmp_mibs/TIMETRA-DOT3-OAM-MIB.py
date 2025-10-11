# SNMP MIB module (TIMETRA-DOT3-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-DOT3-OAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:58:16 2025
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

(EightOTwoOui,
 dot3OamEntry,
 dot3OamEventConfigEntry,
 dot3OamEventLogEntry,
 dot3OamEventLogEventTotal,
 dot3OamEventLogLocation,
 dot3OamEventLogOui,
 dot3OamEventLogRunningTotal,
 dot3OamEventLogThresholdHi,
 dot3OamEventLogThresholdLo,
 dot3OamEventLogTimestamp,
 dot3OamEventLogType,
 dot3OamEventLogValue,
 dot3OamEventLogWindowHi,
 dot3OamEventLogWindowLo,
 dot3OamLoopbackEntry,
 dot3OamPeerEntry,
 dot3OamPeerMacAddress) = mibBuilder.importSymbols(
    "DOT3-OAM-MIB",
    "EightOTwoOui",
    "dot3OamEntry",
    "dot3OamEventConfigEntry",
    "dot3OamEventLogEntry",
    "dot3OamEventLogEventTotal",
    "dot3OamEventLogLocation",
    "dot3OamEventLogOui",
    "dot3OamEventLogRunningTotal",
    "dot3OamEventLogThresholdHi",
    "dot3OamEventLogThresholdLo",
    "dot3OamEventLogTimestamp",
    "dot3OamEventLogType",
    "dot3OamEventLogValue",
    "dot3OamEventLogWindowHi",
    "dot3OamEventLogWindowLo",
    "dot3OamLoopbackEntry",
    "dot3OamPeerEntry",
    "dot3OamPeerMacAddress")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
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

(TmnxEnabledDisabled,) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TmnxEnabledDisabled")


# MODULE-IDENTITY

timetraDOT3OAMMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 42)
)
if mibBuilder.loadTexts:
    timetraDOT3OAMMIBModule.setRevisions(
        ("2016-01-01 00:00",
         "2015-01-01 00:00",
         "2012-07-01 00:00",
         "2008-07-01 00:00",
         "2008-01-01 00:00",
         "2006-08-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxLocalPortAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("logOnly", 1),
          ("outOfService", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxDot3OamMIBConformance_ObjectIdentity = ObjectIdentity
tmnxDot3OamMIBConformance = _TmnxDot3OamMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42)
)
_TmnxDot3OamMIBCompliances_ObjectIdentity = ObjectIdentity
tmnxDot3OamMIBCompliances = _TmnxDot3OamMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 1)
)
_TmnxDot3OamMIBGroups_ObjectIdentity = ObjectIdentity
tmnxDot3OamMIBGroups = _TmnxDot3OamMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2)
)
_TmnxDot3OamObjs_ObjectIdentity = ObjectIdentity
tmnxDot3OamObjs = _TmnxDot3OamObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42)
)
_TmnxDot3OamEntryObjs_ObjectIdentity = ObjectIdentity
tmnxDot3OamEntryObjs = _TmnxDot3OamEntryObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1)
)
_TmnxDot3OamTable_Object = MibTable
tmnxDot3OamTable = _TmnxDot3OamTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxDot3OamTable.setStatus("current")
_TmnxDot3OamEntry_Object = MibTableRow
tmnxDot3OamEntry = _TmnxDot3OamEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxDot3OamEntry.setStatus("current")
_TmnxDot3OamLastChanged_Type = TimeStamp
_TmnxDot3OamLastChanged_Object = MibTableColumn
tmnxDot3OamLastChanged = _TmnxDot3OamLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 1),
    _TmnxDot3OamLastChanged_Type()
)
tmnxDot3OamLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamLastChanged.setStatus("current")


class _TmnxDot3OamInterval_Type(Unsigned32):
    """Custom type tmnxDot3OamInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_TmnxDot3OamInterval_Type.__name__ = "Unsigned32"
_TmnxDot3OamInterval_Object = MibTableColumn
tmnxDot3OamInterval = _TmnxDot3OamInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 2),
    _TmnxDot3OamInterval_Type()
)
tmnxDot3OamInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot3OamInterval.setUnits("deciseconds")


class _TmnxDot3OamMultiplier_Type(Unsigned32):
    """Custom type tmnxDot3OamMultiplier based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_TmnxDot3OamMultiplier_Type.__name__ = "Unsigned32"
_TmnxDot3OamMultiplier_Object = MibTableColumn
tmnxDot3OamMultiplier = _TmnxDot3OamMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 3),
    _TmnxDot3OamMultiplier_Type()
)
tmnxDot3OamMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamMultiplier.setStatus("current")


class _TmnxDot3OamTunneling_Type(TruthValue):
    """Custom type tmnxDot3OamTunneling based on TruthValue"""
    defaultValue = 2


_TmnxDot3OamTunneling_Type.__name__ = "TruthValue"
_TmnxDot3OamTunneling_Object = MibTableColumn
tmnxDot3OamTunneling = _TmnxDot3OamTunneling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 4),
    _TmnxDot3OamTunneling_Type()
)
tmnxDot3OamTunneling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamTunneling.setStatus("current")


class _TmnxDot3OamLooped_Type(TruthValue):
    """Custom type tmnxDot3OamLooped based on TruthValue"""
    defaultValue = 2


_TmnxDot3OamLooped_Type.__name__ = "TruthValue"
_TmnxDot3OamLooped_Object = MibTableColumn
tmnxDot3OamLooped = _TmnxDot3OamLooped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 5),
    _TmnxDot3OamLooped_Type()
)
tmnxDot3OamLooped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamLooped.setStatus("current")


class _TmnxDot3OamHoldTime_Type(Unsigned32):
    """Custom type tmnxDot3OamHoldTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_TmnxDot3OamHoldTime_Type.__name__ = "Unsigned32"
_TmnxDot3OamHoldTime_Object = MibTableColumn
tmnxDot3OamHoldTime = _TmnxDot3OamHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 6),
    _TmnxDot3OamHoldTime_Type()
)
tmnxDot3OamHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot3OamHoldTime.setUnits("seconds")


class _TmnxDot3OamIgnoreEfmState_Type(TruthValue):
    """Custom type tmnxDot3OamIgnoreEfmState based on TruthValue"""
    defaultValue = 2


_TmnxDot3OamIgnoreEfmState_Type.__name__ = "TruthValue"
_TmnxDot3OamIgnoreEfmState_Object = MibTableColumn
tmnxDot3OamIgnoreEfmState = _TmnxDot3OamIgnoreEfmState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 7),
    _TmnxDot3OamIgnoreEfmState_Type()
)
tmnxDot3OamIgnoreEfmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamIgnoreEfmState.setStatus("current")


class _TmnxDot3OamGraceTxEnabled_Type(TruthValue):
    """Custom type tmnxDot3OamGraceTxEnabled based on TruthValue"""
    defaultValue = 1


_TmnxDot3OamGraceTxEnabled_Type.__name__ = "TruthValue"
_TmnxDot3OamGraceTxEnabled_Object = MibTableColumn
tmnxDot3OamGraceTxEnabled = _TmnxDot3OamGraceTxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 8),
    _TmnxDot3OamGraceTxEnabled_Type()
)
tmnxDot3OamGraceTxEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamGraceTxEnabled.setStatus("current")
_TmnxDot3OamGraceTxState_Type = TruthValue
_TmnxDot3OamGraceTxState_Object = MibTableColumn
tmnxDot3OamGraceTxState = _TmnxDot3OamGraceTxState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 9),
    _TmnxDot3OamGraceTxState_Type()
)
tmnxDot3OamGraceTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamGraceTxState.setStatus("current")


class _TmnxDot3OamPrRdiRxDyingGasp_Type(TmnxLocalPortAction):
    """Custom type tmnxDot3OamPrRdiRxDyingGasp based on TmnxLocalPortAction"""
    defaultValue = 2


_TmnxDot3OamPrRdiRxDyingGasp_Type.__name__ = "TmnxLocalPortAction"
_TmnxDot3OamPrRdiRxDyingGasp_Object = MibTableColumn
tmnxDot3OamPrRdiRxDyingGasp = _TmnxDot3OamPrRdiRxDyingGasp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 10),
    _TmnxDot3OamPrRdiRxDyingGasp_Type()
)
tmnxDot3OamPrRdiRxDyingGasp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamPrRdiRxDyingGasp.setStatus("current")


class _TmnxDot3OamPrRdiRxCriticalEvent_Type(TmnxLocalPortAction):
    """Custom type tmnxDot3OamPrRdiRxCriticalEvent based on TmnxLocalPortAction"""
    defaultValue = 2


_TmnxDot3OamPrRdiRxCriticalEvent_Type.__name__ = "TmnxLocalPortAction"
_TmnxDot3OamPrRdiRxCriticalEvent_Object = MibTableColumn
tmnxDot3OamPrRdiRxCriticalEvent = _TmnxDot3OamPrRdiRxCriticalEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 11),
    _TmnxDot3OamPrRdiRxCriticalEvent_Type()
)
tmnxDot3OamPrRdiRxCriticalEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamPrRdiRxCriticalEvent.setStatus("current")


class _TmnxDot3OamPrRdiRxLinkFault_Type(TmnxLocalPortAction):
    """Custom type tmnxDot3OamPrRdiRxLinkFault based on TmnxLocalPortAction"""
    defaultValue = 2


_TmnxDot3OamPrRdiRxLinkFault_Type.__name__ = "TmnxLocalPortAction"
_TmnxDot3OamPrRdiRxLinkFault_Object = MibTableColumn
tmnxDot3OamPrRdiRxLinkFault = _TmnxDot3OamPrRdiRxLinkFault_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 12),
    _TmnxDot3OamPrRdiRxLinkFault_Type()
)
tmnxDot3OamPrRdiRxLinkFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamPrRdiRxLinkFault.setStatus("current")


class _TmnxDot3OamPrRdiRxEventNotif_Type(TmnxLocalPortAction):
    """Custom type tmnxDot3OamPrRdiRxEventNotif based on TmnxLocalPortAction"""
    defaultValue = 1


_TmnxDot3OamPrRdiRxEventNotif_Type.__name__ = "TmnxLocalPortAction"
_TmnxDot3OamPrRdiRxEventNotif_Object = MibTableColumn
tmnxDot3OamPrRdiRxEventNotif = _TmnxDot3OamPrRdiRxEventNotif_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 13),
    _TmnxDot3OamPrRdiRxEventNotif_Type()
)
tmnxDot3OamPrRdiRxEventNotif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamPrRdiRxEventNotif.setStatus("current")


class _TmnxDot3OamDiscAdCapLinkMon_Type(TruthValue):
    """Custom type tmnxDot3OamDiscAdCapLinkMon based on TruthValue"""
    defaultValue = 1


_TmnxDot3OamDiscAdCapLinkMon_Type.__name__ = "TruthValue"
_TmnxDot3OamDiscAdCapLinkMon_Object = MibTableColumn
tmnxDot3OamDiscAdCapLinkMon = _TmnxDot3OamDiscAdCapLinkMon_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 14),
    _TmnxDot3OamDiscAdCapLinkMon_Type()
)
tmnxDot3OamDiscAdCapLinkMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamDiscAdCapLinkMon.setStatus("current")
_TmnxDot3OamVendorOui_Type = EightOTwoOui
_TmnxDot3OamVendorOui_Object = MibTableColumn
tmnxDot3OamVendorOui = _TmnxDot3OamVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 15),
    _TmnxDot3OamVendorOui_Type()
)
tmnxDot3OamVendorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamVendorOui.setStatus("current")
_TmnxDot3OamVendorInfo_Type = Unsigned32
_TmnxDot3OamVendorInfo_Object = MibTableColumn
tmnxDot3OamVendorInfo = _TmnxDot3OamVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 16),
    _TmnxDot3OamVendorInfo_Type()
)
tmnxDot3OamVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamVendorInfo.setStatus("current")


class _TmnxDot3OamGraceVendorOui_Type(EightOTwoOui):
    """Custom type tmnxDot3OamGraceVendorOui based on EightOTwoOui"""
    defaultHexValue = "00164D"


_TmnxDot3OamGraceVendorOui_Type.__name__ = "EightOTwoOui"
_TmnxDot3OamGraceVendorOui_Object = MibTableColumn
tmnxDot3OamGraceVendorOui = _TmnxDot3OamGraceVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 17),
    _TmnxDot3OamGraceVendorOui_Type()
)
tmnxDot3OamGraceVendorOui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamGraceVendorOui.setStatus("current")


class _TmnxDot3OamDyingGaspOnReset_Type(TruthValue):
    """Custom type tmnxDot3OamDyingGaspOnReset based on TruthValue"""
    defaultValue = 1


_TmnxDot3OamDyingGaspOnReset_Type.__name__ = "TruthValue"
_TmnxDot3OamDyingGaspOnReset_Object = MibTableColumn
tmnxDot3OamDyingGaspOnReset = _TmnxDot3OamDyingGaspOnReset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 18),
    _TmnxDot3OamDyingGaspOnReset_Type()
)
tmnxDot3OamDyingGaspOnReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamDyingGaspOnReset.setStatus("current")
_TmnxDot3OamDyingGaspOnResetState_Type = TruthValue
_TmnxDot3OamDyingGaspOnResetState_Object = MibTableColumn
tmnxDot3OamDyingGaspOnResetState = _TmnxDot3OamDyingGaspOnResetState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 19),
    _TmnxDot3OamDyingGaspOnResetState_Type()
)
tmnxDot3OamDyingGaspOnResetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamDyingGaspOnResetState.setStatus("current")


class _TmnxDot3OamTriggerFault_Type(Integer32):
    """Custom type tmnxDot3OamTriggerFault based on Integer32"""
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
        *(("none", 1),
          ("dyingGasp", 2),
          ("criticalEvent", 3))
    )


_TmnxDot3OamTriggerFault_Type.__name__ = "Integer32"
_TmnxDot3OamTriggerFault_Object = MibTableColumn
tmnxDot3OamTriggerFault = _TmnxDot3OamTriggerFault_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 20),
    _TmnxDot3OamTriggerFault_Type()
)
tmnxDot3OamTriggerFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamTriggerFault.setStatus("current")


class _TmnxDot3OamSoftResetAction_Type(Integer32):
    """Custom type tmnxDot3OamSoftResetAction based on Integer32"""
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
          ("grace", 2),
          ("dyingGasp", 3))
    )


_TmnxDot3OamSoftResetAction_Type.__name__ = "Integer32"
_TmnxDot3OamSoftResetAction_Object = MibTableColumn
tmnxDot3OamSoftResetAction = _TmnxDot3OamSoftResetAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 1, 1, 1, 21),
    _TmnxDot3OamSoftResetAction_Type()
)
tmnxDot3OamSoftResetAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamSoftResetAction.setStatus("current")
_TmnxDot3OamLoopbackObjs_ObjectIdentity = ObjectIdentity
tmnxDot3OamLoopbackObjs = _TmnxDot3OamLoopbackObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 2)
)
_TmnxDot3OamLoopbackTable_Object = MibTable
tmnxDot3OamLoopbackTable = _TmnxDot3OamLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxDot3OamLoopbackTable.setStatus("current")
_TmnxDot3OamLoopbackEntry_Object = MibTableRow
tmnxDot3OamLoopbackEntry = _TmnxDot3OamLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxDot3OamLoopbackEntry.setStatus("current")
_TmnxDot3OamLoopbackLastChanged_Type = TimeStamp
_TmnxDot3OamLoopbackLastChanged_Object = MibTableColumn
tmnxDot3OamLoopbackLastChanged = _TmnxDot3OamLoopbackLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 2, 1, 1, 1),
    _TmnxDot3OamLoopbackLastChanged_Type()
)
tmnxDot3OamLoopbackLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamLoopbackLastChanged.setStatus("current")


class _TmnxDot3OamLoopbackLocalStatus_Type(Integer32):
    """Custom type tmnxDot3OamLoopbackLocalStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noLoopback", 1),
          ("localLoopback", 2))
    )


_TmnxDot3OamLoopbackLocalStatus_Type.__name__ = "Integer32"
_TmnxDot3OamLoopbackLocalStatus_Object = MibTableColumn
tmnxDot3OamLoopbackLocalStatus = _TmnxDot3OamLoopbackLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 2, 1, 1, 2),
    _TmnxDot3OamLoopbackLocalStatus_Type()
)
tmnxDot3OamLoopbackLocalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamLoopbackLocalStatus.setStatus("current")
_TmnxDot3OamGlobalObjs_ObjectIdentity = ObjectIdentity
tmnxDot3OamGlobalObjs = _TmnxDot3OamGlobalObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 3)
)
_TmnxDot3OamSystemScalarsGroup_ObjectIdentity = ObjectIdentity
tmnxDot3OamSystemScalarsGroup = _TmnxDot3OamSystemScalarsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 3, 1)
)


class _TmnxDot3OamSystemGraceTxEnable_Type(TruthValue):
    """Custom type tmnxDot3OamSystemGraceTxEnable based on TruthValue"""
    defaultValue = 2


_TmnxDot3OamSystemGraceTxEnable_Type.__name__ = "TruthValue"
_TmnxDot3OamSystemGraceTxEnable_Object = MibScalar
tmnxDot3OamSystemGraceTxEnable = _TmnxDot3OamSystemGraceTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 3, 1, 1),
    _TmnxDot3OamSystemGraceTxEnable_Type()
)
tmnxDot3OamSystemGraceTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamSystemGraceTxEnable.setStatus("current")


class _TmnxDot3OamSystemDyingGaspOnRst_Type(TruthValue):
    """Custom type tmnxDot3OamSystemDyingGaspOnRst based on TruthValue"""
    defaultValue = 2


_TmnxDot3OamSystemDyingGaspOnRst_Type.__name__ = "TruthValue"
_TmnxDot3OamSystemDyingGaspOnRst_Object = MibScalar
tmnxDot3OamSystemDyingGaspOnRst = _TmnxDot3OamSystemDyingGaspOnRst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 3, 1, 2),
    _TmnxDot3OamSystemDyingGaspOnRst_Type()
)
tmnxDot3OamSystemDyingGaspOnRst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamSystemDyingGaspOnRst.setStatus("current")
_TmnxDot3OamPeerTable_Object = MibTable
tmnxDot3OamPeerTable = _TmnxDot3OamPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 4)
)
if mibBuilder.loadTexts:
    tmnxDot3OamPeerTable.setStatus("current")
_TmnxDot3OamPeerEntry_Object = MibTableRow
tmnxDot3OamPeerEntry = _TmnxDot3OamPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxDot3OamPeerEntry.setStatus("current")
_TmnxDot3OamPeerGraceRx_Type = TruthValue
_TmnxDot3OamPeerGraceRx_Object = MibTableColumn
tmnxDot3OamPeerGraceRx = _TmnxDot3OamPeerGraceRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 4, 1, 1),
    _TmnxDot3OamPeerGraceRx_Type()
)
tmnxDot3OamPeerGraceRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamPeerGraceRx.setStatus("current")
_TmnxDot3OamEventObjs_ObjectIdentity = ObjectIdentity
tmnxDot3OamEventObjs = _TmnxDot3OamEventObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5)
)
_TmnxDot3OamEventCfgTblLastChange_Type = TimeStamp
_TmnxDot3OamEventCfgTblLastChange_Object = MibScalar
tmnxDot3OamEventCfgTblLastChange = _TmnxDot3OamEventCfgTblLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 1),
    _TmnxDot3OamEventCfgTblLastChange_Type()
)
tmnxDot3OamEventCfgTblLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamEventCfgTblLastChange.setStatus("current")
_TmnxDot3OamEventConfigTable_Object = MibTable
tmnxDot3OamEventConfigTable = _TmnxDot3OamEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 2)
)
if mibBuilder.loadTexts:
    tmnxDot3OamEventConfigTable.setStatus("current")
_TmnxDot3OamEventConfigEntry_Object = MibTableRow
tmnxDot3OamEventConfigEntry = _TmnxDot3OamEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxDot3OamEventConfigEntry.setStatus("current")
_TmnxDot3OamEventCfgLastChanged_Type = TimeStamp
_TmnxDot3OamEventCfgLastChanged_Object = MibTableColumn
tmnxDot3OamEventCfgLastChanged = _TmnxDot3OamEventCfgLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 2, 1, 1),
    _TmnxDot3OamEventCfgLastChanged_Type()
)
tmnxDot3OamEventCfgLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamEventCfgLastChanged.setStatus("current")


class _TmnxDot3OamLinkMonEnabled_Type(TmnxEnabledDisabled):
    """Custom type tmnxDot3OamLinkMonEnabled based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxDot3OamLinkMonEnabled_Type.__name__ = "TmnxEnabledDisabled"
_TmnxDot3OamLinkMonEnabled_Object = MibTableColumn
tmnxDot3OamLinkMonEnabled = _TmnxDot3OamLinkMonEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 2, 1, 2),
    _TmnxDot3OamLinkMonEnabled_Type()
)
tmnxDot3OamLinkMonEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamLinkMonEnabled.setStatus("current")


class _TmnxDot3OamLocalSfActEventBurst_Type(Unsigned32):
    """Custom type tmnxDot3OamLocalSfActEventBurst based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TmnxDot3OamLocalSfActEventBurst_Type.__name__ = "Unsigned32"
_TmnxDot3OamLocalSfActEventBurst_Object = MibTableColumn
tmnxDot3OamLocalSfActEventBurst = _TmnxDot3OamLocalSfActEventBurst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 2, 1, 3),
    _TmnxDot3OamLocalSfActEventBurst_Type()
)
tmnxDot3OamLocalSfActEventBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamLocalSfActEventBurst.setStatus("current")


class _TmnxDot3OamLocalSfActPortAction_Type(TmnxLocalPortAction):
    """Custom type tmnxDot3OamLocalSfActPortAction based on TmnxLocalPortAction"""
    defaultValue = 2


_TmnxDot3OamLocalSfActPortAction_Type.__name__ = "TmnxLocalPortAction"
_TmnxDot3OamLocalSfActPortAction_Object = MibTableColumn
tmnxDot3OamLocalSfActPortAction = _TmnxDot3OamLocalSfActPortAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 2, 1, 4),
    _TmnxDot3OamLocalSfActPortAction_Type()
)
tmnxDot3OamLocalSfActPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamLocalSfActPortAction.setStatus("current")


class _TmnxDot3OamErrFrmEnabled_Type(TmnxEnabledDisabled):
    """Custom type tmnxDot3OamErrFrmEnabled based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxDot3OamErrFrmEnabled_Type.__name__ = "TmnxEnabledDisabled"
_TmnxDot3OamErrFrmEnabled_Object = MibTableColumn
tmnxDot3OamErrFrmEnabled = _TmnxDot3OamErrFrmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 2, 1, 5),
    _TmnxDot3OamErrFrmEnabled_Type()
)
tmnxDot3OamErrFrmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamErrFrmEnabled.setStatus("current")


class _TmnxDot3OamErrFrmSdThreshold_Type(Unsigned32):
    """Custom type tmnxDot3OamErrFrmSdThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TmnxDot3OamErrFrmSdThreshold_Type.__name__ = "Unsigned32"
_TmnxDot3OamErrFrmSdThreshold_Object = MibTableColumn
tmnxDot3OamErrFrmSdThreshold = _TmnxDot3OamErrFrmSdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 2, 1, 6),
    _TmnxDot3OamErrFrmSdThreshold_Type()
)
tmnxDot3OamErrFrmSdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamErrFrmSdThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot3OamErrFrmSdThreshold.setUnits("frames")


class _TmnxDot3OamErrFrmPrdEnabled_Type(TmnxEnabledDisabled):
    """Custom type tmnxDot3OamErrFrmPrdEnabled based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxDot3OamErrFrmPrdEnabled_Type.__name__ = "TmnxEnabledDisabled"
_TmnxDot3OamErrFrmPrdEnabled_Object = MibTableColumn
tmnxDot3OamErrFrmPrdEnabled = _TmnxDot3OamErrFrmPrdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 2, 1, 7),
    _TmnxDot3OamErrFrmPrdEnabled_Type()
)
tmnxDot3OamErrFrmPrdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamErrFrmPrdEnabled.setStatus("current")


class _TmnxDot3OamErrFrmPrdSdThreshold_Type(Unsigned32):
    """Custom type tmnxDot3OamErrFrmPrdSdThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TmnxDot3OamErrFrmPrdSdThreshold_Type.__name__ = "Unsigned32"
_TmnxDot3OamErrFrmPrdSdThreshold_Object = MibTableColumn
tmnxDot3OamErrFrmPrdSdThreshold = _TmnxDot3OamErrFrmPrdSdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 2, 1, 8),
    _TmnxDot3OamErrFrmPrdSdThreshold_Type()
)
tmnxDot3OamErrFrmPrdSdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamErrFrmPrdSdThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot3OamErrFrmPrdSdThreshold.setUnits("frames")


class _TmnxDot3OamErrFrmSecEnabled_Type(TmnxEnabledDisabled):
    """Custom type tmnxDot3OamErrFrmSecEnabled based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxDot3OamErrFrmSecEnabled_Type.__name__ = "TmnxEnabledDisabled"
_TmnxDot3OamErrFrmSecEnabled_Object = MibTableColumn
tmnxDot3OamErrFrmSecEnabled = _TmnxDot3OamErrFrmSecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 2, 1, 9),
    _TmnxDot3OamErrFrmSecEnabled_Type()
)
tmnxDot3OamErrFrmSecEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamErrFrmSecEnabled.setStatus("current")


class _TmnxDot3OamErrFrmSecSdThreshold_Type(Unsigned32):
    """Custom type tmnxDot3OamErrFrmSecSdThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_TmnxDot3OamErrFrmSecSdThreshold_Type.__name__ = "Unsigned32"
_TmnxDot3OamErrFrmSecSdThreshold_Object = MibTableColumn
tmnxDot3OamErrFrmSecSdThreshold = _TmnxDot3OamErrFrmSecSdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 2, 1, 10),
    _TmnxDot3OamErrFrmSecSdThreshold_Type()
)
tmnxDot3OamErrFrmSecSdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamErrFrmSecSdThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot3OamErrFrmSecSdThreshold.setUnits("errored frame seconds")


class _TmnxDot3OamErrSymPrdEnabled_Type(TmnxEnabledDisabled):
    """Custom type tmnxDot3OamErrSymPrdEnabled based on TmnxEnabledDisabled"""
    defaultValue = 2


_TmnxDot3OamErrSymPrdEnabled_Type.__name__ = "TmnxEnabledDisabled"
_TmnxDot3OamErrSymPrdEnabled_Object = MibTableColumn
tmnxDot3OamErrSymPrdEnabled = _TmnxDot3OamErrSymPrdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 2, 1, 11),
    _TmnxDot3OamErrSymPrdEnabled_Type()
)
tmnxDot3OamErrSymPrdEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamErrSymPrdEnabled.setStatus("current")


class _TmnxDot3OamErrSymPrdSdThreshold_Type(Unsigned32):
    """Custom type tmnxDot3OamErrSymPrdSdThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TmnxDot3OamErrSymPrdSdThreshold_Type.__name__ = "Unsigned32"
_TmnxDot3OamErrSymPrdSdThreshold_Object = MibTableColumn
tmnxDot3OamErrSymPrdSdThreshold = _TmnxDot3OamErrSymPrdSdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 2, 1, 12),
    _TmnxDot3OamErrSymPrdSdThreshold_Type()
)
tmnxDot3OamErrSymPrdSdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamErrSymPrdSdThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot3OamErrSymPrdSdThreshold.setUnits("symbols")


class _TmnxDot3OamErrSymPrdWindowTime_Type(Unsigned32):
    """Custom type tmnxDot3OamErrSymPrdWindowTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_TmnxDot3OamErrSymPrdWindowTime_Type.__name__ = "Unsigned32"
_TmnxDot3OamErrSymPrdWindowTime_Object = MibTableColumn
tmnxDot3OamErrSymPrdWindowTime = _TmnxDot3OamErrSymPrdWindowTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 2, 1, 13),
    _TmnxDot3OamErrSymPrdWindowTime_Type()
)
tmnxDot3OamErrSymPrdWindowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot3OamErrSymPrdWindowTime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot3OamErrSymPrdWindowTime.setUnits("deciseconds")
_TmnxDot3OamEventLogTable_Object = MibTable
tmnxDot3OamEventLogTable = _TmnxDot3OamEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 3)
)
if mibBuilder.loadTexts:
    tmnxDot3OamEventLogTable.setStatus("current")
_TmnxDot3OamEventLogEntry_Object = MibTableRow
tmnxDot3OamEventLogEntry = _TmnxDot3OamEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxDot3OamEventLogEntry.setStatus("current")
_TmnxDot3OamEventLogCleared_Type = TruthValue
_TmnxDot3OamEventLogCleared_Object = MibTableColumn
tmnxDot3OamEventLogCleared = _TmnxDot3OamEventLogCleared_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 3, 1, 1),
    _TmnxDot3OamEventLogCleared_Type()
)
tmnxDot3OamEventLogCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamEventLogCleared.setStatus("current")
_TmnxDot3OamSdEventLogTable_Object = MibTable
tmnxDot3OamSdEventLogTable = _TmnxDot3OamSdEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 4)
)
if mibBuilder.loadTexts:
    tmnxDot3OamSdEventLogTable.setStatus("current")
_TmnxDot3OamSdEventLogEntry_Object = MibTableRow
tmnxDot3OamSdEventLogEntry = _TmnxDot3OamSdEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 4, 1)
)
tmnxDot3OamSdEventLogEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogIndex"),
)
if mibBuilder.loadTexts:
    tmnxDot3OamSdEventLogEntry.setStatus("current")


class _TmnxDot3OamSdEventLogIndex_Type(Unsigned32):
    """Custom type tmnxDot3OamSdEventLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxDot3OamSdEventLogIndex_Type.__name__ = "Unsigned32"
_TmnxDot3OamSdEventLogIndex_Object = MibTableColumn
tmnxDot3OamSdEventLogIndex = _TmnxDot3OamSdEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 4, 1, 1),
    _TmnxDot3OamSdEventLogIndex_Type()
)
tmnxDot3OamSdEventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot3OamSdEventLogIndex.setStatus("current")
_TmnxDot3OamSdEventLogTimestamp_Type = TimeStamp
_TmnxDot3OamSdEventLogTimestamp_Object = MibTableColumn
tmnxDot3OamSdEventLogTimestamp = _TmnxDot3OamSdEventLogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 4, 1, 2),
    _TmnxDot3OamSdEventLogTimestamp_Type()
)
tmnxDot3OamSdEventLogTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamSdEventLogTimestamp.setStatus("current")
_TmnxDot3OamSdEventLogOui_Type = EightOTwoOui
_TmnxDot3OamSdEventLogOui_Object = MibTableColumn
tmnxDot3OamSdEventLogOui = _TmnxDot3OamSdEventLogOui_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 4, 1, 3),
    _TmnxDot3OamSdEventLogOui_Type()
)
tmnxDot3OamSdEventLogOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamSdEventLogOui.setStatus("current")
_TmnxDot3OamSdEventLogType_Type = Unsigned32
_TmnxDot3OamSdEventLogType_Object = MibTableColumn
tmnxDot3OamSdEventLogType = _TmnxDot3OamSdEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 4, 1, 4),
    _TmnxDot3OamSdEventLogType_Type()
)
tmnxDot3OamSdEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamSdEventLogType.setStatus("current")


class _TmnxDot3OamSdEventLogLocation_Type(Integer32):
    """Custom type tmnxDot3OamSdEventLogLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_TmnxDot3OamSdEventLogLocation_Type.__name__ = "Integer32"
_TmnxDot3OamSdEventLogLocation_Object = MibTableColumn
tmnxDot3OamSdEventLogLocation = _TmnxDot3OamSdEventLogLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 4, 1, 5),
    _TmnxDot3OamSdEventLogLocation_Type()
)
tmnxDot3OamSdEventLogLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamSdEventLogLocation.setStatus("current")
_TmnxDot3OamSdEventLogWindowHi_Type = Unsigned32
_TmnxDot3OamSdEventLogWindowHi_Object = MibTableColumn
tmnxDot3OamSdEventLogWindowHi = _TmnxDot3OamSdEventLogWindowHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 4, 1, 6),
    _TmnxDot3OamSdEventLogWindowHi_Type()
)
tmnxDot3OamSdEventLogWindowHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamSdEventLogWindowHi.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot3OamSdEventLogWindowHi.setUnits("2^32 deciseconds")
_TmnxDot3OamSdEventLogWindowLo_Type = Unsigned32
_TmnxDot3OamSdEventLogWindowLo_Object = MibTableColumn
tmnxDot3OamSdEventLogWindowLo = _TmnxDot3OamSdEventLogWindowLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 4, 1, 7),
    _TmnxDot3OamSdEventLogWindowLo_Type()
)
tmnxDot3OamSdEventLogWindowLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamSdEventLogWindowLo.setStatus("current")
if mibBuilder.loadTexts:
    tmnxDot3OamSdEventLogWindowLo.setUnits("deciseconds")
_TmnxDot3OamSdEventLogThresholdHi_Type = Unsigned32
_TmnxDot3OamSdEventLogThresholdHi_Object = MibTableColumn
tmnxDot3OamSdEventLogThresholdHi = _TmnxDot3OamSdEventLogThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 4, 1, 8),
    _TmnxDot3OamSdEventLogThresholdHi_Type()
)
tmnxDot3OamSdEventLogThresholdHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamSdEventLogThresholdHi.setStatus("current")
_TmnxDot3OamSdEventLogThresholdLo_Type = Unsigned32
_TmnxDot3OamSdEventLogThresholdLo_Object = MibTableColumn
tmnxDot3OamSdEventLogThresholdLo = _TmnxDot3OamSdEventLogThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 4, 1, 9),
    _TmnxDot3OamSdEventLogThresholdLo_Type()
)
tmnxDot3OamSdEventLogThresholdLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamSdEventLogThresholdLo.setStatus("current")
_TmnxDot3OamSdEventLogValue_Type = CounterBasedGauge64
_TmnxDot3OamSdEventLogValue_Object = MibTableColumn
tmnxDot3OamSdEventLogValue = _TmnxDot3OamSdEventLogValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 4, 1, 10),
    _TmnxDot3OamSdEventLogValue_Type()
)
tmnxDot3OamSdEventLogValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamSdEventLogValue.setStatus("current")
_TmnxDot3OamSdEventLogRunTotal_Type = CounterBasedGauge64
_TmnxDot3OamSdEventLogRunTotal_Object = MibTableColumn
tmnxDot3OamSdEventLogRunTotal = _TmnxDot3OamSdEventLogRunTotal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 4, 1, 11),
    _TmnxDot3OamSdEventLogRunTotal_Type()
)
tmnxDot3OamSdEventLogRunTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamSdEventLogRunTotal.setStatus("current")
_TmnxDot3OamSdEventLogEventTotal_Type = Unsigned32
_TmnxDot3OamSdEventLogEventTotal_Object = MibTableColumn
tmnxDot3OamSdEventLogEventTotal = _TmnxDot3OamSdEventLogEventTotal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 4, 1, 12),
    _TmnxDot3OamSdEventLogEventTotal_Type()
)
tmnxDot3OamSdEventLogEventTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamSdEventLogEventTotal.setStatus("current")
_TmnxDot3OamSdEventLogCleared_Type = TruthValue
_TmnxDot3OamSdEventLogCleared_Object = MibTableColumn
tmnxDot3OamSdEventLogCleared = _TmnxDot3OamSdEventLogCleared_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 42, 5, 4, 1, 13),
    _TmnxDot3OamSdEventLogCleared_Type()
)
tmnxDot3OamSdEventLogCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot3OamSdEventLogCleared.setStatus("current")
_TmnxDot3OamNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxDot3OamNotifyPrefix = _TmnxDot3OamNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42)
)
_TmnxDot3OamNotificationsPrefix_ObjectIdentity = ObjectIdentity
tmnxDot3OamNotificationsPrefix = _TmnxDot3OamNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42, 42)
)
_TmnxDot3OamNotifications_ObjectIdentity = ObjectIdentity
tmnxDot3OamNotifications = _TmnxDot3OamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42, 42, 0)
)
dot3OamEntry.registerAugmentions(
    ("TIMETRA-DOT3-OAM-MIB",
     "tmnxDot3OamEntry")
)
tmnxDot3OamEntry.setIndexNames(*dot3OamEntry.getIndexNames())
dot3OamLoopbackEntry.registerAugmentions(
    ("TIMETRA-DOT3-OAM-MIB",
     "tmnxDot3OamLoopbackEntry")
)
tmnxDot3OamLoopbackEntry.setIndexNames(*dot3OamLoopbackEntry.getIndexNames())
dot3OamPeerEntry.registerAugmentions(
    ("TIMETRA-DOT3-OAM-MIB",
     "tmnxDot3OamPeerEntry")
)
tmnxDot3OamPeerEntry.setIndexNames(*dot3OamPeerEntry.getIndexNames())
dot3OamEventConfigEntry.registerAugmentions(
    ("TIMETRA-DOT3-OAM-MIB",
     "tmnxDot3OamEventConfigEntry")
)
tmnxDot3OamEventConfigEntry.setIndexNames(*dot3OamEventConfigEntry.getIndexNames())
dot3OamEventLogEntry.registerAugmentions(
    ("TIMETRA-DOT3-OAM-MIB",
     "tmnxDot3OamEventLogEntry")
)
tmnxDot3OamEventLogEntry.setIndexNames(*dot3OamEventLogEntry.getIndexNames())

# Managed Objects groups

tmnxDot3OamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 1)
)
tmnxDot3OamGroup.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLastChanged"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamInterval"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamMultiplier"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamTunneling"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamGroup.setStatus("obsolete")

tmnxDot3OamLoopbackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 2)
)
tmnxDot3OamLoopbackGroup.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopbackLastChanged"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopbackLocalStatus"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamLoopbackGroup.setStatus("current")

tmnxDot3OamV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 5)
)
tmnxDot3OamV6v0Group.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLastChanged"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamInterval"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamMultiplier"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamTunneling"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLooped"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamV6v0Group.setStatus("current")

tmnxDot3OamV6v1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 6)
)
tmnxDot3OamV6v1Group.setObjects(
    ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamHoldTime")
)
if mibBuilder.loadTexts:
    tmnxDot3OamV6v1Group.setStatus("current")

tmnxDot3OamV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 7)
)
tmnxDot3OamV11v0Group.setObjects(
    ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamIgnoreEfmState")
)
if mibBuilder.loadTexts:
    tmnxDot3OamV11v0Group.setStatus("current")

tmnxDot3OamGraceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 8)
)
tmnxDot3OamGraceGroup.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSystemGraceTxEnable"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamGraceTxEnabled"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamGraceTxState"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamPeerGraceRx"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamGraceGroup.setStatus("current")

tmnxDot3OamLinkMonGroupV12v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 9)
)
tmnxDot3OamLinkMonGroupV12v0.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamEventCfgTblLastChange"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamEventCfgLastChanged"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLinkMonEnabled"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamErrFrmEnabled"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLocalSfActEventBurst"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLocalSfActPortAction"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamPrRdiRxDyingGasp"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamPrRdiRxCriticalEvent"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamPrRdiRxLinkFault"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamPrRdiRxEventNotif"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamDiscAdCapLinkMon"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamEventLogCleared"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamLinkMonGroupV12v0.setStatus("current")

tmnxDot3OamLinkMonGroupV13v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 10)
)
tmnxDot3OamLinkMonGroupV13v0.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogTimestamp"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogOui"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogType"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogLocation"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogWindowHi"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogWindowLo"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogThresholdHi"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogThresholdLo"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogValue"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogRunTotal"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogEventTotal"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogCleared"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamErrFrmSdThreshold"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamErrFrmPrdEnabled"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamErrFrmPrdSdThreshold"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamErrFrmSecEnabled"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamErrFrmSecSdThreshold"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamErrSymPrdEnabled"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamErrSymPrdSdThreshold"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamErrSymPrdWindowTime"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamLinkMonGroupV13v0.setStatus("current")

tmnxDot3OamGroupV14v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 12)
)
tmnxDot3OamGroupV14v0.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamVendorOui"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamVendorInfo"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSystemDyingGaspOnRst"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamGraceVendorOui"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamDyingGaspOnReset"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamDyingGaspOnResetState"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamTriggerFault"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSoftResetAction"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamGroupV14v0.setStatus("current")


# Notification objects

tmnxDot3OamPeerChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42, 42, 0, 1)
)
tmnxDot3OamPeerChanged.setObjects(
    ("DOT3-OAM-MIB", "dot3OamPeerMacAddress")
)
if mibBuilder.loadTexts:
    tmnxDot3OamPeerChanged.setStatus(
        "current"
    )

tmnxDot3OamLoopDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42, 42, 0, 2)
)
tmnxDot3OamLoopDetected.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    tmnxDot3OamLoopDetected.setStatus(
        "current"
    )

tmnxDot3OamLoopCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42, 42, 0, 3)
)
tmnxDot3OamLoopCleared.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    tmnxDot3OamLoopCleared.setStatus(
        "current"
    )

tmnxDot3OamSdThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42, 42, 0, 4)
)
tmnxDot3OamSdThresholdEvent.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogTimestamp"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogOui"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogType"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogLocation"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogWindowHi"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogWindowLo"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogThresholdHi"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogThresholdLo"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogValue"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogRunTotal"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogEventTotal"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdEventLogCleared"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamSdThresholdEvent.setStatus(
        "current"
    )

tmnxDot3OamThresholdEventClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42, 42, 0, 5)
)
tmnxDot3OamThresholdEventClr.setObjects(
      *(("DOT3-OAM-MIB", "dot3OamEventLogTimestamp"),
        ("DOT3-OAM-MIB", "dot3OamEventLogOui"),
        ("DOT3-OAM-MIB", "dot3OamEventLogType"),
        ("DOT3-OAM-MIB", "dot3OamEventLogLocation"),
        ("DOT3-OAM-MIB", "dot3OamEventLogWindowHi"),
        ("DOT3-OAM-MIB", "dot3OamEventLogWindowLo"),
        ("DOT3-OAM-MIB", "dot3OamEventLogThresholdHi"),
        ("DOT3-OAM-MIB", "dot3OamEventLogThresholdLo"),
        ("DOT3-OAM-MIB", "dot3OamEventLogValue"),
        ("DOT3-OAM-MIB", "dot3OamEventLogRunningTotal"),
        ("DOT3-OAM-MIB", "dot3OamEventLogEventTotal"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamThresholdEventClr.setStatus(
        "current"
    )

tmnxDot3OamNonThresholdEventClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 42, 42, 0, 6)
)
tmnxDot3OamNonThresholdEventClr.setObjects(
      *(("DOT3-OAM-MIB", "dot3OamEventLogTimestamp"),
        ("DOT3-OAM-MIB", "dot3OamEventLogOui"),
        ("DOT3-OAM-MIB", "dot3OamEventLogType"),
        ("DOT3-OAM-MIB", "dot3OamEventLogLocation"),
        ("DOT3-OAM-MIB", "dot3OamEventLogEventTotal"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamNonThresholdEventClr.setStatus(
        "current"
    )


# Notifications groups

tmnxDot3OamNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 3)
)
tmnxDot3OamNotificationGroup.setObjects(
    ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamPeerChanged")
)
if mibBuilder.loadTexts:
    tmnxDot3OamNotificationGroup.setStatus(
        "obsolete"
    )

tmnxDot3OamNotificationV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 4)
)
tmnxDot3OamNotificationV6v0Group.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamPeerChanged"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopDetected"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopCleared"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamNotificationV6v0Group.setStatus(
        "current"
    )

tmnxDot3OamNotificationGrpV13v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 2, 11)
)
tmnxDot3OamNotificationGrpV13v0.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamSdThresholdEvent"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamThresholdEventClr"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamNonThresholdEventClr"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamNotificationGrpV13v0.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxDot3OamMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 1, 1)
)
tmnxDot3OamMIBCompliance.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamGroup"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopbackGroup"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamNotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamMIBCompliance.setStatus(
        "obsolete"
    )

tmnxDot3OamMIBV6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 1, 2)
)
tmnxDot3OamMIBV6v0Compliance.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamV6v0Group"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopbackGroup"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamNotificationV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamMIBV6v0Compliance.setStatus(
        "obsolete"
    )

tmnxDot3OamMIBV6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 1, 3)
)
tmnxDot3OamMIBV6v1Compliance.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamV6v0Group"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamV6v1Group"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopbackGroup"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamNotificationV6v0Group"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamMIBV6v1Compliance.setStatus(
        "obsolete"
    )

tmnxDot3OamMIBV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 1, 4)
)
tmnxDot3OamMIBV11v0Compliance.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamV6v0Group"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamV6v1Group"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamV11v0Group"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLoopbackGroup"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamNotificationV6v0Group"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamGraceGroup"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamMIBV11v0Compliance.setStatus(
        "current"
    )

tmnxDot3OamMIBV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 1, 5)
)
tmnxDot3OamMIBV12v0Compliance.setObjects(
    ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLinkMonGroupV12v0")
)
if mibBuilder.loadTexts:
    tmnxDot3OamMIBV12v0Compliance.setStatus(
        "current"
    )

tmnxDot3OamMIBV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 1, 6)
)
tmnxDot3OamMIBV13v0Compliance.setObjects(
      *(("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamLinkMonGroupV13v0"),
        ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamNotificationGrpV13v0"))
)
if mibBuilder.loadTexts:
    tmnxDot3OamMIBV13v0Compliance.setStatus(
        "current"
    )

tmnxDot3OamMIBV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 42, 1, 7)
)
tmnxDot3OamMIBV14v0Compliance.setObjects(
    ("TIMETRA-DOT3-OAM-MIB", "tmnxDot3OamGroupV14v0")
)
if mibBuilder.loadTexts:
    tmnxDot3OamMIBV14v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-DOT3-OAM-MIB",
    **{"TmnxLocalPortAction": TmnxLocalPortAction,
       "timetraDOT3OAMMIBModule": timetraDOT3OAMMIBModule,
       "tmnxDot3OamMIBConformance": tmnxDot3OamMIBConformance,
       "tmnxDot3OamMIBCompliances": tmnxDot3OamMIBCompliances,
       "tmnxDot3OamMIBCompliance": tmnxDot3OamMIBCompliance,
       "tmnxDot3OamMIBV6v0Compliance": tmnxDot3OamMIBV6v0Compliance,
       "tmnxDot3OamMIBV6v1Compliance": tmnxDot3OamMIBV6v1Compliance,
       "tmnxDot3OamMIBV11v0Compliance": tmnxDot3OamMIBV11v0Compliance,
       "tmnxDot3OamMIBV12v0Compliance": tmnxDot3OamMIBV12v0Compliance,
       "tmnxDot3OamMIBV13v0Compliance": tmnxDot3OamMIBV13v0Compliance,
       "tmnxDot3OamMIBV14v0Compliance": tmnxDot3OamMIBV14v0Compliance,
       "tmnxDot3OamMIBGroups": tmnxDot3OamMIBGroups,
       "tmnxDot3OamGroup": tmnxDot3OamGroup,
       "tmnxDot3OamLoopbackGroup": tmnxDot3OamLoopbackGroup,
       "tmnxDot3OamNotificationGroup": tmnxDot3OamNotificationGroup,
       "tmnxDot3OamNotificationV6v0Group": tmnxDot3OamNotificationV6v0Group,
       "tmnxDot3OamV6v0Group": tmnxDot3OamV6v0Group,
       "tmnxDot3OamV6v1Group": tmnxDot3OamV6v1Group,
       "tmnxDot3OamV11v0Group": tmnxDot3OamV11v0Group,
       "tmnxDot3OamGraceGroup": tmnxDot3OamGraceGroup,
       "tmnxDot3OamLinkMonGroupV12v0": tmnxDot3OamLinkMonGroupV12v0,
       "tmnxDot3OamLinkMonGroupV13v0": tmnxDot3OamLinkMonGroupV13v0,
       "tmnxDot3OamNotificationGrpV13v0": tmnxDot3OamNotificationGrpV13v0,
       "tmnxDot3OamGroupV14v0": tmnxDot3OamGroupV14v0,
       "tmnxDot3OamObjs": tmnxDot3OamObjs,
       "tmnxDot3OamEntryObjs": tmnxDot3OamEntryObjs,
       "tmnxDot3OamTable": tmnxDot3OamTable,
       "tmnxDot3OamEntry": tmnxDot3OamEntry,
       "tmnxDot3OamLastChanged": tmnxDot3OamLastChanged,
       "tmnxDot3OamInterval": tmnxDot3OamInterval,
       "tmnxDot3OamMultiplier": tmnxDot3OamMultiplier,
       "tmnxDot3OamTunneling": tmnxDot3OamTunneling,
       "tmnxDot3OamLooped": tmnxDot3OamLooped,
       "tmnxDot3OamHoldTime": tmnxDot3OamHoldTime,
       "tmnxDot3OamIgnoreEfmState": tmnxDot3OamIgnoreEfmState,
       "tmnxDot3OamGraceTxEnabled": tmnxDot3OamGraceTxEnabled,
       "tmnxDot3OamGraceTxState": tmnxDot3OamGraceTxState,
       "tmnxDot3OamPrRdiRxDyingGasp": tmnxDot3OamPrRdiRxDyingGasp,
       "tmnxDot3OamPrRdiRxCriticalEvent": tmnxDot3OamPrRdiRxCriticalEvent,
       "tmnxDot3OamPrRdiRxLinkFault": tmnxDot3OamPrRdiRxLinkFault,
       "tmnxDot3OamPrRdiRxEventNotif": tmnxDot3OamPrRdiRxEventNotif,
       "tmnxDot3OamDiscAdCapLinkMon": tmnxDot3OamDiscAdCapLinkMon,
       "tmnxDot3OamVendorOui": tmnxDot3OamVendorOui,
       "tmnxDot3OamVendorInfo": tmnxDot3OamVendorInfo,
       "tmnxDot3OamGraceVendorOui": tmnxDot3OamGraceVendorOui,
       "tmnxDot3OamDyingGaspOnReset": tmnxDot3OamDyingGaspOnReset,
       "tmnxDot3OamDyingGaspOnResetState": tmnxDot3OamDyingGaspOnResetState,
       "tmnxDot3OamTriggerFault": tmnxDot3OamTriggerFault,
       "tmnxDot3OamSoftResetAction": tmnxDot3OamSoftResetAction,
       "tmnxDot3OamLoopbackObjs": tmnxDot3OamLoopbackObjs,
       "tmnxDot3OamLoopbackTable": tmnxDot3OamLoopbackTable,
       "tmnxDot3OamLoopbackEntry": tmnxDot3OamLoopbackEntry,
       "tmnxDot3OamLoopbackLastChanged": tmnxDot3OamLoopbackLastChanged,
       "tmnxDot3OamLoopbackLocalStatus": tmnxDot3OamLoopbackLocalStatus,
       "tmnxDot3OamGlobalObjs": tmnxDot3OamGlobalObjs,
       "tmnxDot3OamSystemScalarsGroup": tmnxDot3OamSystemScalarsGroup,
       "tmnxDot3OamSystemGraceTxEnable": tmnxDot3OamSystemGraceTxEnable,
       "tmnxDot3OamSystemDyingGaspOnRst": tmnxDot3OamSystemDyingGaspOnRst,
       "tmnxDot3OamPeerTable": tmnxDot3OamPeerTable,
       "tmnxDot3OamPeerEntry": tmnxDot3OamPeerEntry,
       "tmnxDot3OamPeerGraceRx": tmnxDot3OamPeerGraceRx,
       "tmnxDot3OamEventObjs": tmnxDot3OamEventObjs,
       "tmnxDot3OamEventCfgTblLastChange": tmnxDot3OamEventCfgTblLastChange,
       "tmnxDot3OamEventConfigTable": tmnxDot3OamEventConfigTable,
       "tmnxDot3OamEventConfigEntry": tmnxDot3OamEventConfigEntry,
       "tmnxDot3OamEventCfgLastChanged": tmnxDot3OamEventCfgLastChanged,
       "tmnxDot3OamLinkMonEnabled": tmnxDot3OamLinkMonEnabled,
       "tmnxDot3OamLocalSfActEventBurst": tmnxDot3OamLocalSfActEventBurst,
       "tmnxDot3OamLocalSfActPortAction": tmnxDot3OamLocalSfActPortAction,
       "tmnxDot3OamErrFrmEnabled": tmnxDot3OamErrFrmEnabled,
       "tmnxDot3OamErrFrmSdThreshold": tmnxDot3OamErrFrmSdThreshold,
       "tmnxDot3OamErrFrmPrdEnabled": tmnxDot3OamErrFrmPrdEnabled,
       "tmnxDot3OamErrFrmPrdSdThreshold": tmnxDot3OamErrFrmPrdSdThreshold,
       "tmnxDot3OamErrFrmSecEnabled": tmnxDot3OamErrFrmSecEnabled,
       "tmnxDot3OamErrFrmSecSdThreshold": tmnxDot3OamErrFrmSecSdThreshold,
       "tmnxDot3OamErrSymPrdEnabled": tmnxDot3OamErrSymPrdEnabled,
       "tmnxDot3OamErrSymPrdSdThreshold": tmnxDot3OamErrSymPrdSdThreshold,
       "tmnxDot3OamErrSymPrdWindowTime": tmnxDot3OamErrSymPrdWindowTime,
       "tmnxDot3OamEventLogTable": tmnxDot3OamEventLogTable,
       "tmnxDot3OamEventLogEntry": tmnxDot3OamEventLogEntry,
       "tmnxDot3OamEventLogCleared": tmnxDot3OamEventLogCleared,
       "tmnxDot3OamSdEventLogTable": tmnxDot3OamSdEventLogTable,
       "tmnxDot3OamSdEventLogEntry": tmnxDot3OamSdEventLogEntry,
       "tmnxDot3OamSdEventLogIndex": tmnxDot3OamSdEventLogIndex,
       "tmnxDot3OamSdEventLogTimestamp": tmnxDot3OamSdEventLogTimestamp,
       "tmnxDot3OamSdEventLogOui": tmnxDot3OamSdEventLogOui,
       "tmnxDot3OamSdEventLogType": tmnxDot3OamSdEventLogType,
       "tmnxDot3OamSdEventLogLocation": tmnxDot3OamSdEventLogLocation,
       "tmnxDot3OamSdEventLogWindowHi": tmnxDot3OamSdEventLogWindowHi,
       "tmnxDot3OamSdEventLogWindowLo": tmnxDot3OamSdEventLogWindowLo,
       "tmnxDot3OamSdEventLogThresholdHi": tmnxDot3OamSdEventLogThresholdHi,
       "tmnxDot3OamSdEventLogThresholdLo": tmnxDot3OamSdEventLogThresholdLo,
       "tmnxDot3OamSdEventLogValue": tmnxDot3OamSdEventLogValue,
       "tmnxDot3OamSdEventLogRunTotal": tmnxDot3OamSdEventLogRunTotal,
       "tmnxDot3OamSdEventLogEventTotal": tmnxDot3OamSdEventLogEventTotal,
       "tmnxDot3OamSdEventLogCleared": tmnxDot3OamSdEventLogCleared,
       "tmnxDot3OamNotifyPrefix": tmnxDot3OamNotifyPrefix,
       "tmnxDot3OamNotificationsPrefix": tmnxDot3OamNotificationsPrefix,
       "tmnxDot3OamNotifications": tmnxDot3OamNotifications,
       "tmnxDot3OamPeerChanged": tmnxDot3OamPeerChanged,
       "tmnxDot3OamLoopDetected": tmnxDot3OamLoopDetected,
       "tmnxDot3OamLoopCleared": tmnxDot3OamLoopCleared,
       "tmnxDot3OamSdThresholdEvent": tmnxDot3OamSdThresholdEvent,
       "tmnxDot3OamThresholdEventClr": tmnxDot3OamThresholdEventClr,
       "tmnxDot3OamNonThresholdEventClr": tmnxDot3OamNonThresholdEventClr}
)
