# SNMP MIB module (ARICENT-ELPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-ELPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:42 2025
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

(Dot1agCfmMepId,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMepId")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fselps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25)
)
if mibBuilder.loadTexts:
    fselps.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PgId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class PgType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("individual", 1),
          ("list", 2),
          ("all", 3))
    )



class PgServiceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 1),
          ("mplsLSP", 2),
          ("mplsPW", 3))
    )



class PgServiceValue(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class PgServiceValueOrNone(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )



class PgMonitorMechanismType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cfm", 1),
          ("mplsOam", 2),
          ("none", 3))
    )



class PgExtCmd(TextualConvention, Integer32):
    status = "current"
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
        *(("lockOutProtection", 1),
          ("forceSwitchToProtection", 2),
          ("manualSwitchToProtection", 3),
          ("exercise", 4),
          ("clear", 5),
          ("freeze", 6),
          ("clearFreeze", 7),
          ("manualSwitchToWorking", 8))
    )



class PgLocalCondition(TextualConvention, Integer32):
    status = "current"
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
        *(("signalFailOnWorking", 1),
          ("recoverSignalFailOnWorking", 2),
          ("signalFailOnProtection", 3),
          ("recoverSignalFailOnProtection", 4),
          ("waitToRestoreExpiry", 5))
    )



class PgFarEndRequest(TextualConvention, Integer32):
    status = "current"
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("lockOutProtection", 1),
          ("signalFailOnProtection", 2),
          ("forceSwitchToProtection", 3),
          ("signalFailOnWorking", 4),
          ("manualSwitchToProtection", 5),
          ("waitToRestore", 6),
          ("exerciseOnWorking", 7),
          ("exerciseOnProtection", 8),
          ("reverseRequestOnWorking", 9),
          ("reverseRequestOnProtection", 10),
          ("noRequestOnWorking", 11),
          ("noRequestOnProtection", 12),
          ("doNotRevert", 13),
          ("manualSwitchToWorking", 14))
    )



class PgActiveRequest(TextualConvention, Integer32):
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("localLockOutProtection", 0),
          ("localForcedSwitchToProtection", 1),
          ("localSignalFailOnWorking", 2),
          ("localRecoverSignalFailOnWorking", 3),
          ("localSignalFailOnProtection", 4),
          ("localRecoverSignalFailOnProtection", 5),
          ("localManualSwitchToProtection", 6),
          ("localManualSwitchToWorking", 7),
          ("localClear", 8),
          ("localExercise", 9),
          ("localWaitToRestoreExpiry", 10),
          ("farLockOutProtection", 11),
          ("farSignalFailOnProtection", 12),
          ("farForceSwitchToProtection", 13),
          ("farSignalFailOnWorking", 14),
          ("farManualSwitchToProtection", 15),
          ("farManualSwitchToWorking", 16),
          ("farWaitToRestore", 17),
          ("farExerciseOnWorking", 18),
          ("farExerciseOnProtection", 19),
          ("farReverseRequestOnWorking", 20),
          ("farReverseRequestOnProtection", 21),
          ("farNoRequestOnWorking", 22),
          ("farNoRequestOnProtection", 23),
          ("farDoNotRevert", 24))
    )



class PgSemState(TextualConvention, Integer32):
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
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("noRequestOnWorking", 0),
          ("noRequestOnProtection", 1),
          ("lockOutProtection", 2),
          ("forceSwitchToProtection", 3),
          ("signalFailOnWorking", 4),
          ("signalFailOnProtection", 5),
          ("manualSwitchToProtection", 6),
          ("manualSwitchToWorking", 7),
          ("waitToRestore", 8),
          ("doNotRevert", 9),
          ("exerciseOnWorking", 10),
          ("exerciseOnProtection", 11),
          ("reverseRequestOnWorking", 12),
          ("reverseRequestOnProtection", 13))
    )



class PgStatus(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("protectionDisabled", 0),
          ("workingPathActive", 1),
          ("protectionPathActive", 2),
          ("waitToRestoreState", 3),
          ("holdOffState", 4),
          ("switchingFailed", 5),
          ("unavailable", 6),
          ("doNotRevert", 7))
    )



# MIB Managed Objects in the order of their OIDs

_FsElpsSystem_ObjectIdentity = ObjectIdentity
fsElpsSystem = _FsElpsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 1)
)


class _FsElpsGlobalTraceOption_Type(TruthValue):
    """Custom type fsElpsGlobalTraceOption based on TruthValue"""
    defaultValue = 2


_FsElpsGlobalTraceOption_Type.__name__ = "TruthValue"
_FsElpsGlobalTraceOption_Object = MibScalar
fsElpsGlobalTraceOption = _FsElpsGlobalTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 1, 1),
    _FsElpsGlobalTraceOption_Type()
)
fsElpsGlobalTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsGlobalTraceOption.setStatus("current")


class _FsElpsPSCChannelCode_Type(Unsigned32):
    """Custom type fsElpsPSCChannelCode based on Unsigned32"""
    defaultValue = 9

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 32),
    )


_FsElpsPSCChannelCode_Type.__name__ = "Unsigned32"
_FsElpsPSCChannelCode_Object = MibScalar
fsElpsPSCChannelCode = _FsElpsPSCChannelCode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 1, 2),
    _FsElpsPSCChannelCode_Type()
)
fsElpsPSCChannelCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPSCChannelCode.setStatus("obsolete")


class _FsElpsRapidTxTime_Type(Unsigned32):
    """Custom type fsElpsRapidTxTime based on Unsigned32"""
    defaultValue = 3300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 3300),
    )


_FsElpsRapidTxTime_Type.__name__ = "Unsigned32"
_FsElpsRapidTxTime_Object = MibScalar
fsElpsRapidTxTime = _FsElpsRapidTxTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 1, 3),
    _FsElpsRapidTxTime_Type()
)
fsElpsRapidTxTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsRapidTxTime.setStatus("current")
if mibBuilder.loadTexts:
    fsElpsRapidTxTime.setUnits("microseconds")
_FsElpsContext_ObjectIdentity = ObjectIdentity
fsElpsContext = _FsElpsContext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 2)
)
_FsElpsContextTable_Object = MibTable
fsElpsContextTable = _FsElpsContextTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 2, 1)
)
if mibBuilder.loadTexts:
    fsElpsContextTable.setStatus("current")
_FsElpsContextEntry_Object = MibTableRow
fsElpsContextEntry = _FsElpsContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 2, 1, 1)
)
fsElpsContextEntry.setIndexNames(
    (0, "ARICENT-ELPS-MIB", "fsElpsContextId"),
)
if mibBuilder.loadTexts:
    fsElpsContextEntry.setStatus("current")
_FsElpsContextId_Type = Unsigned32
_FsElpsContextId_Object = MibTableColumn
fsElpsContextId = _FsElpsContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 2, 1, 1, 1),
    _FsElpsContextId_Type()
)
fsElpsContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsElpsContextId.setStatus("current")


class _FsElpsContextSystemControl_Type(Integer32):
    """Custom type fsElpsContextSystemControl based on Integer32"""
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


_FsElpsContextSystemControl_Type.__name__ = "Integer32"
_FsElpsContextSystemControl_Object = MibTableColumn
fsElpsContextSystemControl = _FsElpsContextSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 2, 1, 1, 2),
    _FsElpsContextSystemControl_Type()
)
fsElpsContextSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsContextSystemControl.setStatus("current")


class _FsElpsContextModuleStatus_Type(Integer32):
    """Custom type fsElpsContextModuleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FsElpsContextModuleStatus_Type.__name__ = "Integer32"
_FsElpsContextModuleStatus_Object = MibTableColumn
fsElpsContextModuleStatus = _FsElpsContextModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 2, 1, 1, 3),
    _FsElpsContextModuleStatus_Type()
)
fsElpsContextModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsContextModuleStatus.setStatus("current")


class _FsElpsContextTraceInputString_Type(DisplayString):
    """Custom type fsElpsContextTraceInputString based on DisplayString"""
    defaultValue = OctetString("critical")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsElpsContextTraceInputString_Type.__name__ = "DisplayString"
_FsElpsContextTraceInputString_Object = MibTableColumn
fsElpsContextTraceInputString = _FsElpsContextTraceInputString_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 2, 1, 1, 4),
    _FsElpsContextTraceInputString_Type()
)
fsElpsContextTraceInputString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsContextTraceInputString.setStatus("current")


class _FsElpsContextEnableTrap_Type(TruthValue):
    """Custom type fsElpsContextEnableTrap based on TruthValue"""
    defaultValue = 1


_FsElpsContextEnableTrap_Type.__name__ = "TruthValue"
_FsElpsContextEnableTrap_Object = MibTableColumn
fsElpsContextEnableTrap = _FsElpsContextEnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 2, 1, 1, 5),
    _FsElpsContextEnableTrap_Type()
)
fsElpsContextEnableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsContextEnableTrap.setStatus("current")


class _FsElpsContextVlanGroupManager_Type(Integer32):
    """Custom type fsElpsContextVlanGroupManager based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 1),
          ("elps", 2))
    )


_FsElpsContextVlanGroupManager_Type.__name__ = "Integer32"
_FsElpsContextVlanGroupManager_Object = MibTableColumn
fsElpsContextVlanGroupManager = _FsElpsContextVlanGroupManager_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 2, 1, 1, 6),
    _FsElpsContextVlanGroupManager_Type()
)
fsElpsContextVlanGroupManager.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsContextVlanGroupManager.setStatus("current")
_FsElpsPg_ObjectIdentity = ObjectIdentity
fsElpsPg = _FsElpsPg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3)
)
_FsElpsPgConfigTable_Object = MibTable
fsElpsPgConfigTable = _FsElpsPgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1)
)
if mibBuilder.loadTexts:
    fsElpsPgConfigTable.setStatus("current")
_FsElpsPgConfigEntry_Object = MibTableRow
fsElpsPgConfigEntry = _FsElpsPgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1)
)
fsElpsPgConfigEntry.setIndexNames(
    (0, "ARICENT-ELPS-MIB", "fsElpsContextId"),
    (0, "ARICENT-ELPS-MIB", "fsElpsPgConfigPgId"),
)
if mibBuilder.loadTexts:
    fsElpsPgConfigEntry.setStatus("current")
_FsElpsPgConfigPgId_Type = PgId
_FsElpsPgConfigPgId_Object = MibTableColumn
fsElpsPgConfigPgId = _FsElpsPgConfigPgId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1, 1),
    _FsElpsPgConfigPgId_Type()
)
fsElpsPgConfigPgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsElpsPgConfigPgId.setStatus("current")


class _FsElpsPgConfigType_Type(PgType):
    """Custom type fsElpsPgConfigType based on PgType"""
    defaultValue = 1


_FsElpsPgConfigType_Type.__name__ = "PgType"
_FsElpsPgConfigType_Object = MibTableColumn
fsElpsPgConfigType = _FsElpsPgConfigType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1, 2),
    _FsElpsPgConfigType_Type()
)
fsElpsPgConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgConfigType.setStatus("current")


class _FsElpsPgConfigServiceType_Type(PgServiceType):
    """Custom type fsElpsPgConfigServiceType based on PgServiceType"""
    defaultValue = 1


_FsElpsPgConfigServiceType_Type.__name__ = "PgServiceType"
_FsElpsPgConfigServiceType_Object = MibTableColumn
fsElpsPgConfigServiceType = _FsElpsPgConfigServiceType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1, 3),
    _FsElpsPgConfigServiceType_Type()
)
fsElpsPgConfigServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgConfigServiceType.setStatus("current")


class _FsElpsPgConfigMonitorMechanism_Type(PgMonitorMechanismType):
    """Custom type fsElpsPgConfigMonitorMechanism based on PgMonitorMechanismType"""
    defaultValue = 1


_FsElpsPgConfigMonitorMechanism_Type.__name__ = "PgMonitorMechanismType"
_FsElpsPgConfigMonitorMechanism_Object = MibTableColumn
fsElpsPgConfigMonitorMechanism = _FsElpsPgConfigMonitorMechanism_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1, 4),
    _FsElpsPgConfigMonitorMechanism_Type()
)
fsElpsPgConfigMonitorMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgConfigMonitorMechanism.setStatus("current")
_FsElpsPgConfigIngressPort_Type = InterfaceIndexOrZero
_FsElpsPgConfigIngressPort_Object = MibTableColumn
fsElpsPgConfigIngressPort = _FsElpsPgConfigIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1, 5),
    _FsElpsPgConfigIngressPort_Type()
)
fsElpsPgConfigIngressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgConfigIngressPort.setStatus("current")
_FsElpsPgConfigWorkingPort_Type = InterfaceIndexOrZero
_FsElpsPgConfigWorkingPort_Object = MibTableColumn
fsElpsPgConfigWorkingPort = _FsElpsPgConfigWorkingPort_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1, 6),
    _FsElpsPgConfigWorkingPort_Type()
)
fsElpsPgConfigWorkingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgConfigWorkingPort.setStatus("current")
_FsElpsPgConfigProtectionPort_Type = InterfaceIndexOrZero
_FsElpsPgConfigProtectionPort_Object = MibTableColumn
fsElpsPgConfigProtectionPort = _FsElpsPgConfigProtectionPort_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1, 7),
    _FsElpsPgConfigProtectionPort_Type()
)
fsElpsPgConfigProtectionPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgConfigProtectionPort.setStatus("current")
_FsElpsPgConfigWorkingServiceValue_Type = PgServiceValueOrNone
_FsElpsPgConfigWorkingServiceValue_Object = MibTableColumn
fsElpsPgConfigWorkingServiceValue = _FsElpsPgConfigWorkingServiceValue_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1, 8),
    _FsElpsPgConfigWorkingServiceValue_Type()
)
fsElpsPgConfigWorkingServiceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgConfigWorkingServiceValue.setStatus("current")
_FsElpsPgConfigProtectionServiceValue_Type = PgServiceValueOrNone
_FsElpsPgConfigProtectionServiceValue_Object = MibTableColumn
fsElpsPgConfigProtectionServiceValue = _FsElpsPgConfigProtectionServiceValue_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1, 9),
    _FsElpsPgConfigProtectionServiceValue_Type()
)
fsElpsPgConfigProtectionServiceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgConfigProtectionServiceValue.setStatus("current")


class _FsElpsPgConfigOperType_Type(Integer32):
    """Custom type fsElpsPgConfigOperType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("revertive", 1),
          ("nonRevertive", 2))
    )


_FsElpsPgConfigOperType_Type.__name__ = "Integer32"
_FsElpsPgConfigOperType_Object = MibTableColumn
fsElpsPgConfigOperType = _FsElpsPgConfigOperType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1, 10),
    _FsElpsPgConfigOperType_Type()
)
fsElpsPgConfigOperType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgConfigOperType.setStatus("current")


class _FsElpsPgConfigProtType_Type(Integer32):
    """Custom type fsElpsPgConfigProtType based on Integer32"""
    defaultValue = 1

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
        *(("oneIsToOneBidirectionalWithAps", 1),
          ("onePlusOneBidirectionalWithAps", 2),
          ("onePlusOneUnidirectionalWithAps", 3),
          ("onePlusOneUnidirectionalWithOutAps", 4))
    )


_FsElpsPgConfigProtType_Type.__name__ = "Integer32"
_FsElpsPgConfigProtType_Object = MibTableColumn
fsElpsPgConfigProtType = _FsElpsPgConfigProtType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1, 11),
    _FsElpsPgConfigProtType_Type()
)
fsElpsPgConfigProtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgConfigProtType.setStatus("current")


class _FsElpsPgConfigName_Type(DisplayString):
    """Custom type fsElpsPgConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsElpsPgConfigName_Type.__name__ = "DisplayString"
_FsElpsPgConfigName_Object = MibTableColumn
fsElpsPgConfigName = _FsElpsPgConfigName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1, 12),
    _FsElpsPgConfigName_Type()
)
fsElpsPgConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgConfigName.setStatus("current")
_FsElpsPgConfigRowStatus_Type = RowStatus
_FsElpsPgConfigRowStatus_Object = MibTableColumn
fsElpsPgConfigRowStatus = _FsElpsPgConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1, 13),
    _FsElpsPgConfigRowStatus_Type()
)
fsElpsPgConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgConfigRowStatus.setStatus("current")
_FsElpsPgConfigWorkingServicePointer_Type = RowPointer
_FsElpsPgConfigWorkingServicePointer_Object = MibTableColumn
fsElpsPgConfigWorkingServicePointer = _FsElpsPgConfigWorkingServicePointer_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1, 14),
    _FsElpsPgConfigWorkingServicePointer_Type()
)
fsElpsPgConfigWorkingServicePointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgConfigWorkingServicePointer.setStatus("current")
_FsElpsPgConfigWorkingReverseServicePointer_Type = RowPointer
_FsElpsPgConfigWorkingReverseServicePointer_Object = MibTableColumn
fsElpsPgConfigWorkingReverseServicePointer = _FsElpsPgConfigWorkingReverseServicePointer_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1, 15),
    _FsElpsPgConfigWorkingReverseServicePointer_Type()
)
fsElpsPgConfigWorkingReverseServicePointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgConfigWorkingReverseServicePointer.setStatus("current")
_FsElpsPgConfigProtectionServicePointer_Type = RowPointer
_FsElpsPgConfigProtectionServicePointer_Object = MibTableColumn
fsElpsPgConfigProtectionServicePointer = _FsElpsPgConfigProtectionServicePointer_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1, 16),
    _FsElpsPgConfigProtectionServicePointer_Type()
)
fsElpsPgConfigProtectionServicePointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgConfigProtectionServicePointer.setStatus("current")
_FsElpsPgConfigProtectionReverseServicePointer_Type = RowPointer
_FsElpsPgConfigProtectionReverseServicePointer_Object = MibTableColumn
fsElpsPgConfigProtectionReverseServicePointer = _FsElpsPgConfigProtectionReverseServicePointer_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1, 17),
    _FsElpsPgConfigProtectionReverseServicePointer_Type()
)
fsElpsPgConfigProtectionReverseServicePointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgConfigProtectionReverseServicePointer.setStatus("current")


class _FsElpsPgConfigWorkingInstanceId_Type(Unsigned32):
    """Custom type fsElpsPgConfigWorkingInstanceId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_FsElpsPgConfigWorkingInstanceId_Type.__name__ = "Unsigned32"
_FsElpsPgConfigWorkingInstanceId_Object = MibTableColumn
fsElpsPgConfigWorkingInstanceId = _FsElpsPgConfigWorkingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1, 18),
    _FsElpsPgConfigWorkingInstanceId_Type()
)
fsElpsPgConfigWorkingInstanceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgConfigWorkingInstanceId.setStatus("current")


class _FsElpsPgConfigProtectionInstanceId_Type(Unsigned32):
    """Custom type fsElpsPgConfigProtectionInstanceId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_FsElpsPgConfigProtectionInstanceId_Type.__name__ = "Unsigned32"
_FsElpsPgConfigProtectionInstanceId_Object = MibTableColumn
fsElpsPgConfigProtectionInstanceId = _FsElpsPgConfigProtectionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1, 19),
    _FsElpsPgConfigProtectionInstanceId_Type()
)
fsElpsPgConfigProtectionInstanceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgConfigProtectionInstanceId.setStatus("current")


class _FsElpsPgPscVersion_Type(Unsigned32):
    """Custom type fsElpsPgPscVersion based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsElpsPgPscVersion_Type.__name__ = "Unsigned32"
_FsElpsPgPscVersion_Object = MibTableColumn
fsElpsPgPscVersion = _FsElpsPgPscVersion_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 1, 1, 20),
    _FsElpsPgPscVersion_Type()
)
fsElpsPgPscVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgPscVersion.setStatus("current")
_FsElpsPgCmdTable_Object = MibTable
fsElpsPgCmdTable = _FsElpsPgCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 2)
)
if mibBuilder.loadTexts:
    fsElpsPgCmdTable.setStatus("current")
_FsElpsPgCmdEntry_Object = MibTableRow
fsElpsPgCmdEntry = _FsElpsPgCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 2, 1)
)
fsElpsPgCmdEntry.setIndexNames(
    (0, "ARICENT-ELPS-MIB", "fsElpsContextId"),
    (0, "ARICENT-ELPS-MIB", "fsElpsPgConfigPgId"),
)
if mibBuilder.loadTexts:
    fsElpsPgCmdEntry.setStatus("current")


class _FsElpsPgCmdHoTime_Type(Unsigned32):
    """Custom type fsElpsPgCmdHoTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FsElpsPgCmdHoTime_Type.__name__ = "Unsigned32"
_FsElpsPgCmdHoTime_Object = MibTableColumn
fsElpsPgCmdHoTime = _FsElpsPgCmdHoTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 2, 1, 1),
    _FsElpsPgCmdHoTime_Type()
)
fsElpsPgCmdHoTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgCmdHoTime.setStatus("current")


class _FsElpsPgCmdWTR_Type(Unsigned32):
    """Custom type fsElpsPgCmdWTR based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_FsElpsPgCmdWTR_Type.__name__ = "Unsigned32"
_FsElpsPgCmdWTR_Object = MibTableColumn
fsElpsPgCmdWTR = _FsElpsPgCmdWTR_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 2, 1, 2),
    _FsElpsPgCmdWTR_Type()
)
fsElpsPgCmdWTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgCmdWTR.setStatus("current")


class _FsElpsPgCmdExtCmd_Type(PgExtCmd):
    """Custom type fsElpsPgCmdExtCmd based on PgExtCmd"""
    defaultValue = 5


_FsElpsPgCmdExtCmd_Type.__name__ = "PgExtCmd"
_FsElpsPgCmdExtCmd_Object = MibTableColumn
fsElpsPgCmdExtCmd = _FsElpsPgCmdExtCmd_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 2, 1, 3),
    _FsElpsPgCmdExtCmd_Type()
)
fsElpsPgCmdExtCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgCmdExtCmd.setStatus("current")


class _FsElpsPgCmdExtCmdStatus_Type(Integer32):
    """Custom type fsElpsPgCmdExtCmdStatus based on Integer32"""
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
        *(("accepted", 1),
          ("overruled", 2),
          ("notApplicable", 3),
          ("rejected", 4))
    )


_FsElpsPgCmdExtCmdStatus_Type.__name__ = "Integer32"
_FsElpsPgCmdExtCmdStatus_Object = MibTableColumn
fsElpsPgCmdExtCmdStatus = _FsElpsPgCmdExtCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 2, 1, 4),
    _FsElpsPgCmdExtCmdStatus_Type()
)
fsElpsPgCmdExtCmdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsPgCmdExtCmdStatus.setStatus("current")
_FsElpsPgCmdLocalCondition_Type = PgLocalCondition
_FsElpsPgCmdLocalCondition_Object = MibTableColumn
fsElpsPgCmdLocalCondition = _FsElpsPgCmdLocalCondition_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 2, 1, 5),
    _FsElpsPgCmdLocalCondition_Type()
)
fsElpsPgCmdLocalCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsPgCmdLocalCondition.setStatus("current")


class _FsElpsPgCmdLocalConditionStatus_Type(Integer32):
    """Custom type fsElpsPgCmdLocalConditionStatus based on Integer32"""
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
        *(("accepted", 1),
          ("overruled", 2),
          ("notApplicable", 3),
          ("rejected", 4))
    )


_FsElpsPgCmdLocalConditionStatus_Type.__name__ = "Integer32"
_FsElpsPgCmdLocalConditionStatus_Object = MibTableColumn
fsElpsPgCmdLocalConditionStatus = _FsElpsPgCmdLocalConditionStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 2, 1, 6),
    _FsElpsPgCmdLocalConditionStatus_Type()
)
fsElpsPgCmdLocalConditionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsPgCmdLocalConditionStatus.setStatus("current")
_FsElpsPgCmdFarEndRequest_Type = PgFarEndRequest
_FsElpsPgCmdFarEndRequest_Object = MibTableColumn
fsElpsPgCmdFarEndRequest = _FsElpsPgCmdFarEndRequest_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 2, 1, 7),
    _FsElpsPgCmdFarEndRequest_Type()
)
fsElpsPgCmdFarEndRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsPgCmdFarEndRequest.setStatus("current")


class _FsElpsPgCmdFarEndRequestStatus_Type(Integer32):
    """Custom type fsElpsPgCmdFarEndRequestStatus based on Integer32"""
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
        *(("accepted", 1),
          ("overruled", 2),
          ("notApplicable", 3),
          ("rejected", 4))
    )


_FsElpsPgCmdFarEndRequestStatus_Type.__name__ = "Integer32"
_FsElpsPgCmdFarEndRequestStatus_Object = MibTableColumn
fsElpsPgCmdFarEndRequestStatus = _FsElpsPgCmdFarEndRequestStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 2, 1, 8),
    _FsElpsPgCmdFarEndRequestStatus_Type()
)
fsElpsPgCmdFarEndRequestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsPgCmdFarEndRequestStatus.setStatus("current")
_FsElpsPgCmdActiveRequest_Type = PgActiveRequest
_FsElpsPgCmdActiveRequest_Object = MibTableColumn
fsElpsPgCmdActiveRequest = _FsElpsPgCmdActiveRequest_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 2, 1, 9),
    _FsElpsPgCmdActiveRequest_Type()
)
fsElpsPgCmdActiveRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsPgCmdActiveRequest.setStatus("current")
_FsElpsPgCmdSemState_Type = PgSemState
_FsElpsPgCmdSemState_Object = MibTableColumn
fsElpsPgCmdSemState = _FsElpsPgCmdSemState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 2, 1, 10),
    _FsElpsPgCmdSemState_Type()
)
fsElpsPgCmdSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsPgCmdSemState.setStatus("current")
_FsElpsPgCmdPgStatus_Type = PgStatus
_FsElpsPgCmdPgStatus_Object = MibTableColumn
fsElpsPgCmdPgStatus = _FsElpsPgCmdPgStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 2, 1, 11),
    _FsElpsPgCmdPgStatus_Type()
)
fsElpsPgCmdPgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsPgCmdPgStatus.setStatus("current")


class _FsElpsPgCmdApsPeriodicTime_Type(Unsigned32):
    """Custom type fsElpsPgCmdApsPeriodicTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_FsElpsPgCmdApsPeriodicTime_Type.__name__ = "Unsigned32"
_FsElpsPgCmdApsPeriodicTime_Object = MibTableColumn
fsElpsPgCmdApsPeriodicTime = _FsElpsPgCmdApsPeriodicTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 2, 1, 12),
    _FsElpsPgCmdApsPeriodicTime_Type()
)
fsElpsPgCmdApsPeriodicTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgCmdApsPeriodicTime.setStatus("current")
if mibBuilder.loadTexts:
    fsElpsPgCmdApsPeriodicTime.setUnits("seconds")
_FsElpsPgCfmTable_Object = MibTable
fsElpsPgCfmTable = _FsElpsPgCfmTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 3)
)
if mibBuilder.loadTexts:
    fsElpsPgCfmTable.setStatus("current")
_FsElpsPgCfmEntry_Object = MibTableRow
fsElpsPgCfmEntry = _FsElpsPgCfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 3, 1)
)
fsElpsPgCfmEntry.setIndexNames(
    (0, "ARICENT-ELPS-MIB", "fsElpsContextId"),
    (0, "ARICENT-ELPS-MIB", "fsElpsPgConfigPgId"),
)
if mibBuilder.loadTexts:
    fsElpsPgCfmEntry.setStatus("current")
_FsElpsPgCfmWorkingMEG_Type = Unsigned32
_FsElpsPgCfmWorkingMEG_Object = MibTableColumn
fsElpsPgCfmWorkingMEG = _FsElpsPgCfmWorkingMEG_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 3, 1, 1),
    _FsElpsPgCfmWorkingMEG_Type()
)
fsElpsPgCfmWorkingMEG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgCfmWorkingMEG.setStatus("current")
_FsElpsPgCfmWorkingME_Type = Unsigned32
_FsElpsPgCfmWorkingME_Object = MibTableColumn
fsElpsPgCfmWorkingME = _FsElpsPgCfmWorkingME_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 3, 1, 2),
    _FsElpsPgCfmWorkingME_Type()
)
fsElpsPgCfmWorkingME.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgCfmWorkingME.setStatus("current")
_FsElpsPgCfmWorkingMEP_Type = Dot1agCfmMepId
_FsElpsPgCfmWorkingMEP_Object = MibTableColumn
fsElpsPgCfmWorkingMEP = _FsElpsPgCfmWorkingMEP_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 3, 1, 3),
    _FsElpsPgCfmWorkingMEP_Type()
)
fsElpsPgCfmWorkingMEP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgCfmWorkingMEP.setStatus("current")
_FsElpsPgCfmProtectionMEG_Type = Unsigned32
_FsElpsPgCfmProtectionMEG_Object = MibTableColumn
fsElpsPgCfmProtectionMEG = _FsElpsPgCfmProtectionMEG_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 3, 1, 4),
    _FsElpsPgCfmProtectionMEG_Type()
)
fsElpsPgCfmProtectionMEG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgCfmProtectionMEG.setStatus("current")
_FsElpsPgCfmProtectionME_Type = Unsigned32
_FsElpsPgCfmProtectionME_Object = MibTableColumn
fsElpsPgCfmProtectionME = _FsElpsPgCfmProtectionME_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 3, 1, 5),
    _FsElpsPgCfmProtectionME_Type()
)
fsElpsPgCfmProtectionME.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgCfmProtectionME.setStatus("current")
_FsElpsPgCfmProtectionMEP_Type = Dot1agCfmMepId
_FsElpsPgCfmProtectionMEP_Object = MibTableColumn
fsElpsPgCfmProtectionMEP = _FsElpsPgCfmProtectionMEP_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 3, 1, 6),
    _FsElpsPgCfmProtectionMEP_Type()
)
fsElpsPgCfmProtectionMEP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgCfmProtectionMEP.setStatus("current")
_FsElpsPgCfmRowStatus_Type = RowStatus
_FsElpsPgCfmRowStatus_Object = MibTableColumn
fsElpsPgCfmRowStatus = _FsElpsPgCfmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 3, 1, 7),
    _FsElpsPgCfmRowStatus_Type()
)
fsElpsPgCfmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgCfmRowStatus.setStatus("current")
_FsElpsPgCfmWorkingReverseMEG_Type = Unsigned32
_FsElpsPgCfmWorkingReverseMEG_Object = MibTableColumn
fsElpsPgCfmWorkingReverseMEG = _FsElpsPgCfmWorkingReverseMEG_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 3, 1, 8),
    _FsElpsPgCfmWorkingReverseMEG_Type()
)
fsElpsPgCfmWorkingReverseMEG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgCfmWorkingReverseMEG.setStatus("current")
_FsElpsPgCfmWorkingReverseME_Type = Unsigned32
_FsElpsPgCfmWorkingReverseME_Object = MibTableColumn
fsElpsPgCfmWorkingReverseME = _FsElpsPgCfmWorkingReverseME_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 3, 1, 9),
    _FsElpsPgCfmWorkingReverseME_Type()
)
fsElpsPgCfmWorkingReverseME.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgCfmWorkingReverseME.setStatus("current")
_FsElpsPgCfmWorkingReverseMEP_Type = Dot1agCfmMepId
_FsElpsPgCfmWorkingReverseMEP_Object = MibTableColumn
fsElpsPgCfmWorkingReverseMEP = _FsElpsPgCfmWorkingReverseMEP_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 3, 1, 10),
    _FsElpsPgCfmWorkingReverseMEP_Type()
)
fsElpsPgCfmWorkingReverseMEP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgCfmWorkingReverseMEP.setStatus("current")
_FsElpsPgCfmProtectionReverseMEG_Type = Unsigned32
_FsElpsPgCfmProtectionReverseMEG_Object = MibTableColumn
fsElpsPgCfmProtectionReverseMEG = _FsElpsPgCfmProtectionReverseMEG_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 3, 1, 11),
    _FsElpsPgCfmProtectionReverseMEG_Type()
)
fsElpsPgCfmProtectionReverseMEG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgCfmProtectionReverseMEG.setStatus("current")
_FsElpsPgCfmProtectionReverseME_Type = Unsigned32
_FsElpsPgCfmProtectionReverseME_Object = MibTableColumn
fsElpsPgCfmProtectionReverseME = _FsElpsPgCfmProtectionReverseME_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 3, 1, 12),
    _FsElpsPgCfmProtectionReverseME_Type()
)
fsElpsPgCfmProtectionReverseME.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgCfmProtectionReverseME.setStatus("current")
_FsElpsPgCfmProtectionReverseMEP_Type = Dot1agCfmMepId
_FsElpsPgCfmProtectionReverseMEP_Object = MibTableColumn
fsElpsPgCfmProtectionReverseMEP = _FsElpsPgCfmProtectionReverseMEP_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 3, 1, 13),
    _FsElpsPgCfmProtectionReverseMEP_Type()
)
fsElpsPgCfmProtectionReverseMEP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgCfmProtectionReverseMEP.setStatus("current")
_FsElpsPgServiceListTable_Object = MibTable
fsElpsPgServiceListTable = _FsElpsPgServiceListTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 4)
)
if mibBuilder.loadTexts:
    fsElpsPgServiceListTable.setStatus("current")
_FsElpsPgServiceListEntry_Object = MibTableRow
fsElpsPgServiceListEntry = _FsElpsPgServiceListEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 4, 1)
)
fsElpsPgServiceListEntry.setIndexNames(
    (0, "ARICENT-ELPS-MIB", "fsElpsContextId"),
    (0, "ARICENT-ELPS-MIB", "fsElpsPgConfigPgId"),
    (0, "ARICENT-ELPS-MIB", "fsElpsPgServiceListValue"),
)
if mibBuilder.loadTexts:
    fsElpsPgServiceListEntry.setStatus("current")
_FsElpsPgServiceListValue_Type = PgServiceValue
_FsElpsPgServiceListValue_Object = MibTableColumn
fsElpsPgServiceListValue = _FsElpsPgServiceListValue_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 4, 1, 1),
    _FsElpsPgServiceListValue_Type()
)
fsElpsPgServiceListValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsElpsPgServiceListValue.setStatus("current")
_FsElpsPgServiceListRowStatus_Type = RowStatus
_FsElpsPgServiceListRowStatus_Object = MibTableColumn
fsElpsPgServiceListRowStatus = _FsElpsPgServiceListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 4, 1, 2),
    _FsElpsPgServiceListRowStatus_Type()
)
fsElpsPgServiceListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgServiceListRowStatus.setStatus("current")
_FsElpsPgShareTable_Object = MibTable
fsElpsPgShareTable = _FsElpsPgShareTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 5)
)
if mibBuilder.loadTexts:
    fsElpsPgShareTable.setStatus("current")
_FsElpsPgShareEntry_Object = MibTableRow
fsElpsPgShareEntry = _FsElpsPgShareEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 5, 1)
)
fsElpsPgShareEntry.setIndexNames(
    (0, "ARICENT-ELPS-MIB", "fsElpsContextId"),
    (0, "ARICENT-ELPS-MIB", "fsElpsPgShareProtectionPort"),
    (0, "ARICENT-ELPS-MIB", "fsElpsPgConfigPgId"),
)
if mibBuilder.loadTexts:
    fsElpsPgShareEntry.setStatus("current")
_FsElpsPgShareProtectionPort_Type = InterfaceIndex
_FsElpsPgShareProtectionPort_Object = MibTableColumn
fsElpsPgShareProtectionPort = _FsElpsPgShareProtectionPort_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 5, 1, 1),
    _FsElpsPgShareProtectionPort_Type()
)
fsElpsPgShareProtectionPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsElpsPgShareProtectionPort.setStatus("current")
_FsElpsPgSharePgStatus_Type = PgStatus
_FsElpsPgSharePgStatus_Object = MibTableColumn
fsElpsPgSharePgStatus = _FsElpsPgSharePgStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 5, 1, 2),
    _FsElpsPgSharePgStatus_Type()
)
fsElpsPgSharePgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsPgSharePgStatus.setStatus("current")
_FsElpsPgStatsTable_Object = MibTable
fsElpsPgStatsTable = _FsElpsPgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 6)
)
if mibBuilder.loadTexts:
    fsElpsPgStatsTable.setStatus("current")
_FsElpsPgStatsEntry_Object = MibTableRow
fsElpsPgStatsEntry = _FsElpsPgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 6, 1)
)
fsElpsPgStatsEntry.setIndexNames(
    (0, "ARICENT-ELPS-MIB", "fsElpsContextId"),
    (0, "ARICENT-ELPS-MIB", "fsElpsPgConfigPgId"),
)
if mibBuilder.loadTexts:
    fsElpsPgStatsEntry.setStatus("current")
_FsElpsPgStatsAutoProtectionSwitchCount_Type = Counter32
_FsElpsPgStatsAutoProtectionSwitchCount_Object = MibTableColumn
fsElpsPgStatsAutoProtectionSwitchCount = _FsElpsPgStatsAutoProtectionSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 6, 1, 1),
    _FsElpsPgStatsAutoProtectionSwitchCount_Type()
)
fsElpsPgStatsAutoProtectionSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsPgStatsAutoProtectionSwitchCount.setStatus("current")
_FsElpsPgStatsForcedSwitchCount_Type = Counter32
_FsElpsPgStatsForcedSwitchCount_Object = MibTableColumn
fsElpsPgStatsForcedSwitchCount = _FsElpsPgStatsForcedSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 6, 1, 2),
    _FsElpsPgStatsForcedSwitchCount_Type()
)
fsElpsPgStatsForcedSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsPgStatsForcedSwitchCount.setStatus("current")
_FsElpsPgStatsManualSwitchCount_Type = Counter32
_FsElpsPgStatsManualSwitchCount_Object = MibTableColumn
fsElpsPgStatsManualSwitchCount = _FsElpsPgStatsManualSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 6, 1, 3),
    _FsElpsPgStatsManualSwitchCount_Type()
)
fsElpsPgStatsManualSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsPgStatsManualSwitchCount.setStatus("current")
_FsElpsPgStatsClearStatistics_Type = TruthValue
_FsElpsPgStatsClearStatistics_Object = MibTableColumn
fsElpsPgStatsClearStatistics = _FsElpsPgStatsClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 6, 1, 4),
    _FsElpsPgStatsClearStatistics_Type()
)
fsElpsPgStatsClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgStatsClearStatistics.setStatus("current")
_FsElpsPgStatsApsPktTxCount_Type = Counter32
_FsElpsPgStatsApsPktTxCount_Object = MibTableColumn
fsElpsPgStatsApsPktTxCount = _FsElpsPgStatsApsPktTxCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 6, 1, 5),
    _FsElpsPgStatsApsPktTxCount_Type()
)
fsElpsPgStatsApsPktTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsPgStatsApsPktTxCount.setStatus("current")
_FsElpsPgStatsApsPktRxCount_Type = Counter32
_FsElpsPgStatsApsPktRxCount_Object = MibTableColumn
fsElpsPgStatsApsPktRxCount = _FsElpsPgStatsApsPktRxCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 6, 1, 6),
    _FsElpsPgStatsApsPktRxCount_Type()
)
fsElpsPgStatsApsPktRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsPgStatsApsPktRxCount.setStatus("current")
_FsElpsPgStatsApsPktDiscardCount_Type = Counter32
_FsElpsPgStatsApsPktDiscardCount_Object = MibTableColumn
fsElpsPgStatsApsPktDiscardCount = _FsElpsPgStatsApsPktDiscardCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 6, 1, 7),
    _FsElpsPgStatsApsPktDiscardCount_Type()
)
fsElpsPgStatsApsPktDiscardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsPgStatsApsPktDiscardCount.setStatus("current")
_FsElpsPgLRSFRxTime_Type = Unsigned32
_FsElpsPgLRSFRxTime_Object = MibTableColumn
fsElpsPgLRSFRxTime = _FsElpsPgLRSFRxTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 6, 1, 8),
    _FsElpsPgLRSFRxTime_Type()
)
fsElpsPgLRSFRxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsPgLRSFRxTime.setStatus("current")
_FsElpsPgLRSFTxTime_Type = Unsigned32
_FsElpsPgLRSFTxTime_Object = MibTableColumn
fsElpsPgLRSFTxTime = _FsElpsPgLRSFTxTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 6, 1, 9),
    _FsElpsPgLRSFTxTime_Type()
)
fsElpsPgLRSFTxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsPgLRSFTxTime.setStatus("current")
_FsElpsPgFRSFRxTime_Type = Unsigned32
_FsElpsPgFRSFRxTime_Object = MibTableColumn
fsElpsPgFRSFRxTime = _FsElpsPgFRSFRxTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 6, 1, 10),
    _FsElpsPgFRSFRxTime_Type()
)
fsElpsPgFRSFRxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsPgFRSFRxTime.setStatus("current")
_FsElpsPgStateChgTime_Type = Unsigned32
_FsElpsPgStateChgTime_Object = MibTableColumn
fsElpsPgStateChgTime = _FsElpsPgStateChgTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 6, 1, 11),
    _FsElpsPgStateChgTime_Type()
)
fsElpsPgStateChgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsPgStateChgTime.setStatus("current")
_FsElpsPgServiceListPointerTable_Object = MibTable
fsElpsPgServiceListPointerTable = _FsElpsPgServiceListPointerTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 7)
)
if mibBuilder.loadTexts:
    fsElpsPgServiceListPointerTable.setStatus("current")
_FsElpsPgServiceListPointerEntry_Object = MibTableRow
fsElpsPgServiceListPointerEntry = _FsElpsPgServiceListPointerEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 7, 1)
)
fsElpsPgServiceListPointerEntry.setIndexNames(
    (0, "ARICENT-ELPS-MIB", "fsElpsContextId"),
    (0, "ARICENT-ELPS-MIB", "fsElpsPgConfigPgId"),
    (0, "ARICENT-ELPS-MIB", "fsElpsPgServiceListId"),
)
if mibBuilder.loadTexts:
    fsElpsPgServiceListPointerEntry.setStatus("current")
_FsElpsPgServiceListId_Type = Unsigned32
_FsElpsPgServiceListId_Object = MibTableColumn
fsElpsPgServiceListId = _FsElpsPgServiceListId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 7, 1, 1),
    _FsElpsPgServiceListId_Type()
)
fsElpsPgServiceListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsElpsPgServiceListId.setStatus("current")
_FsElpsPgWorkingServiceListPointer_Type = RowPointer
_FsElpsPgWorkingServiceListPointer_Object = MibTableColumn
fsElpsPgWorkingServiceListPointer = _FsElpsPgWorkingServiceListPointer_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 7, 1, 2),
    _FsElpsPgWorkingServiceListPointer_Type()
)
fsElpsPgWorkingServiceListPointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgWorkingServiceListPointer.setStatus("current")
_FsElpsPgWorkingReverseServiceListPointer_Type = RowPointer
_FsElpsPgWorkingReverseServiceListPointer_Object = MibTableColumn
fsElpsPgWorkingReverseServiceListPointer = _FsElpsPgWorkingReverseServiceListPointer_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 7, 1, 3),
    _FsElpsPgWorkingReverseServiceListPointer_Type()
)
fsElpsPgWorkingReverseServiceListPointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgWorkingReverseServiceListPointer.setStatus("current")
_FsElpsPgProtectionServiceListPointer_Type = RowPointer
_FsElpsPgProtectionServiceListPointer_Object = MibTableColumn
fsElpsPgProtectionServiceListPointer = _FsElpsPgProtectionServiceListPointer_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 7, 1, 4),
    _FsElpsPgProtectionServiceListPointer_Type()
)
fsElpsPgProtectionServiceListPointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgProtectionServiceListPointer.setStatus("current")
_FsElpsPgProtectionReverseServiceListPointer_Type = RowPointer
_FsElpsPgProtectionReverseServiceListPointer_Object = MibTableColumn
fsElpsPgProtectionReverseServiceListPointer = _FsElpsPgProtectionReverseServiceListPointer_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 7, 1, 5),
    _FsElpsPgProtectionReverseServiceListPointer_Type()
)
fsElpsPgProtectionReverseServiceListPointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgProtectionReverseServiceListPointer.setStatus("current")
_FsElpsPgServiceListPointerRowStatus_Type = RowStatus
_FsElpsPgServiceListPointerRowStatus_Object = MibTableColumn
fsElpsPgServiceListPointerRowStatus = _FsElpsPgServiceListPointerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 3, 7, 1, 6),
    _FsElpsPgServiceListPointerRowStatus_Type()
)
fsElpsPgServiceListPointerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElpsPgServiceListPointerRowStatus.setStatus("current")
_FsElpsPgNotifications_ObjectIdentity = ObjectIdentity
fsElpsPgNotifications = _FsElpsPgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 4)
)
_FsElpsTraps_ObjectIdentity = ObjectIdentity
fsElpsTraps = _FsElpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 4, 0)
)


class _FsElpsTrapContextName_Type(DisplayString):
    """Custom type fsElpsTrapContextName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsElpsTrapContextName_Type.__name__ = "DisplayString"
_FsElpsTrapContextName_Object = MibScalar
fsElpsTrapContextName = _FsElpsTrapContextName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 4, 1),
    _FsElpsTrapContextName_Type()
)
fsElpsTrapContextName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsElpsTrapContextName.setStatus("current")


class _FsElpsTrapSwitchingMechanism_Type(DisplayString):
    """Custom type fsElpsTrapSwitchingMechanism based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsElpsTrapSwitchingMechanism_Type.__name__ = "DisplayString"
_FsElpsTrapSwitchingMechanism_Object = MibScalar
fsElpsTrapSwitchingMechanism = _FsElpsTrapSwitchingMechanism_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 4, 2),
    _FsElpsTrapSwitchingMechanism_Type()
)
fsElpsTrapSwitchingMechanism.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsElpsTrapSwitchingMechanism.setStatus("current")


class _FsElpsTrapMismatchType_Type(DisplayString):
    """Custom type fsElpsTrapMismatchType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsElpsTrapMismatchType_Type.__name__ = "DisplayString"
_FsElpsTrapMismatchType_Object = MibScalar
fsElpsTrapMismatchType = _FsElpsTrapMismatchType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 4, 3),
    _FsElpsTrapMismatchType_Type()
)
fsElpsTrapMismatchType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsElpsTrapMismatchType.setStatus("current")


class _FsElpsTypeOfFailure_Type(DisplayString):
    """Custom type fsElpsTypeOfFailure based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsElpsTypeOfFailure_Type.__name__ = "DisplayString"
_FsElpsTypeOfFailure_Object = MibScalar
fsElpsTypeOfFailure = _FsElpsTypeOfFailure_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 4, 4),
    _FsElpsTypeOfFailure_Type()
)
fsElpsTypeOfFailure.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsElpsTypeOfFailure.setStatus("current")
_FsElpsScalars_ObjectIdentity = ObjectIdentity
fsElpsScalars = _FsElpsScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 5)
)
_FsElpsStatsOneIsToOneApsPktTxCount_Type = Counter32
_FsElpsStatsOneIsToOneApsPktTxCount_Object = MibScalar
fsElpsStatsOneIsToOneApsPktTxCount = _FsElpsStatsOneIsToOneApsPktTxCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 5, 1),
    _FsElpsStatsOneIsToOneApsPktTxCount_Type()
)
fsElpsStatsOneIsToOneApsPktTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsStatsOneIsToOneApsPktTxCount.setStatus("current")
_FsElpsStatsOneIsToOneApsPktRxCount_Type = Counter32
_FsElpsStatsOneIsToOneApsPktRxCount_Object = MibScalar
fsElpsStatsOneIsToOneApsPktRxCount = _FsElpsStatsOneIsToOneApsPktRxCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 5, 2),
    _FsElpsStatsOneIsToOneApsPktRxCount_Type()
)
fsElpsStatsOneIsToOneApsPktRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsStatsOneIsToOneApsPktRxCount.setStatus("current")
_FsElpsStatsOneIsToOneApsPktDiscardCount_Type = Counter32
_FsElpsStatsOneIsToOneApsPktDiscardCount_Object = MibScalar
fsElpsStatsOneIsToOneApsPktDiscardCount = _FsElpsStatsOneIsToOneApsPktDiscardCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 5, 3),
    _FsElpsStatsOneIsToOneApsPktDiscardCount_Type()
)
fsElpsStatsOneIsToOneApsPktDiscardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsStatsOneIsToOneApsPktDiscardCount.setStatus("current")
_FsElpsStatsOnePlusOneApsPktTxCount_Type = Counter32
_FsElpsStatsOnePlusOneApsPktTxCount_Object = MibScalar
fsElpsStatsOnePlusOneApsPktTxCount = _FsElpsStatsOnePlusOneApsPktTxCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 5, 4),
    _FsElpsStatsOnePlusOneApsPktTxCount_Type()
)
fsElpsStatsOnePlusOneApsPktTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsStatsOnePlusOneApsPktTxCount.setStatus("current")
_FsElpsStatsOnePlusOneApsPktRxCount_Type = Counter32
_FsElpsStatsOnePlusOneApsPktRxCount_Object = MibScalar
fsElpsStatsOnePlusOneApsPktRxCount = _FsElpsStatsOnePlusOneApsPktRxCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 5, 5),
    _FsElpsStatsOnePlusOneApsPktRxCount_Type()
)
fsElpsStatsOnePlusOneApsPktRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsStatsOnePlusOneApsPktRxCount.setStatus("current")
_FsElpsStatsOnePlusOneApsPktDiscardCount_Type = Counter32
_FsElpsStatsOnePlusOneApsPktDiscardCount_Object = MibScalar
fsElpsStatsOnePlusOneApsPktDiscardCount = _FsElpsStatsOnePlusOneApsPktDiscardCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 5, 6),
    _FsElpsStatsOnePlusOneApsPktDiscardCount_Type()
)
fsElpsStatsOnePlusOneApsPktDiscardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElpsStatsOnePlusOneApsPktDiscardCount.setStatus("current")

# Managed Objects groups


# Notification objects

fsElpsProtectionSwitchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 4, 0, 1)
)
fsElpsProtectionSwitchTrap.setObjects(
      *(("ARICENT-ELPS-MIB", "fsElpsTrapContextName"),
        ("ARICENT-ELPS-MIB", "fsElpsPgCmdPgStatus"),
        ("ARICENT-ELPS-MIB", "fsElpsTrapSwitchingMechanism"))
)
if mibBuilder.loadTexts:
    fsElpsProtectionSwitchTrap.setStatus(
        "current"
    )

fsElpsProtectionSwitchFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 4, 0, 2)
)
fsElpsProtectionSwitchFailureTrap.setObjects(
      *(("ARICENT-ELPS-MIB", "fsElpsTrapContextName"),
        ("ARICENT-ELPS-MIB", "fsElpsPgCmdPgStatus"),
        ("ARICENT-ELPS-MIB", "fsElpsTypeOfFailure"))
)
if mibBuilder.loadTexts:
    fsElpsProtectionSwitchFailureTrap.setStatus(
        "current"
    )

fsElpsProtectionTypeMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 25, 4, 0, 3)
)
fsElpsProtectionTypeMismatchTrap.setObjects(
      *(("ARICENT-ELPS-MIB", "fsElpsTrapContextName"),
        ("ARICENT-ELPS-MIB", "fsElpsPgCmdPgStatus"),
        ("ARICENT-ELPS-MIB", "fsElpsTrapMismatchType"))
)
if mibBuilder.loadTexts:
    fsElpsProtectionTypeMismatchTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-ELPS-MIB",
    **{"PgId": PgId,
       "PgType": PgType,
       "PgServiceType": PgServiceType,
       "PgServiceValue": PgServiceValue,
       "PgServiceValueOrNone": PgServiceValueOrNone,
       "PgMonitorMechanismType": PgMonitorMechanismType,
       "PgExtCmd": PgExtCmd,
       "PgLocalCondition": PgLocalCondition,
       "PgFarEndRequest": PgFarEndRequest,
       "PgActiveRequest": PgActiveRequest,
       "PgSemState": PgSemState,
       "PgStatus": PgStatus,
       "fselps": fselps,
       "fsElpsSystem": fsElpsSystem,
       "fsElpsGlobalTraceOption": fsElpsGlobalTraceOption,
       "fsElpsPSCChannelCode": fsElpsPSCChannelCode,
       "fsElpsRapidTxTime": fsElpsRapidTxTime,
       "fsElpsContext": fsElpsContext,
       "fsElpsContextTable": fsElpsContextTable,
       "fsElpsContextEntry": fsElpsContextEntry,
       "fsElpsContextId": fsElpsContextId,
       "fsElpsContextSystemControl": fsElpsContextSystemControl,
       "fsElpsContextModuleStatus": fsElpsContextModuleStatus,
       "fsElpsContextTraceInputString": fsElpsContextTraceInputString,
       "fsElpsContextEnableTrap": fsElpsContextEnableTrap,
       "fsElpsContextVlanGroupManager": fsElpsContextVlanGroupManager,
       "fsElpsPg": fsElpsPg,
       "fsElpsPgConfigTable": fsElpsPgConfigTable,
       "fsElpsPgConfigEntry": fsElpsPgConfigEntry,
       "fsElpsPgConfigPgId": fsElpsPgConfigPgId,
       "fsElpsPgConfigType": fsElpsPgConfigType,
       "fsElpsPgConfigServiceType": fsElpsPgConfigServiceType,
       "fsElpsPgConfigMonitorMechanism": fsElpsPgConfigMonitorMechanism,
       "fsElpsPgConfigIngressPort": fsElpsPgConfigIngressPort,
       "fsElpsPgConfigWorkingPort": fsElpsPgConfigWorkingPort,
       "fsElpsPgConfigProtectionPort": fsElpsPgConfigProtectionPort,
       "fsElpsPgConfigWorkingServiceValue": fsElpsPgConfigWorkingServiceValue,
       "fsElpsPgConfigProtectionServiceValue": fsElpsPgConfigProtectionServiceValue,
       "fsElpsPgConfigOperType": fsElpsPgConfigOperType,
       "fsElpsPgConfigProtType": fsElpsPgConfigProtType,
       "fsElpsPgConfigName": fsElpsPgConfigName,
       "fsElpsPgConfigRowStatus": fsElpsPgConfigRowStatus,
       "fsElpsPgConfigWorkingServicePointer": fsElpsPgConfigWorkingServicePointer,
       "fsElpsPgConfigWorkingReverseServicePointer": fsElpsPgConfigWorkingReverseServicePointer,
       "fsElpsPgConfigProtectionServicePointer": fsElpsPgConfigProtectionServicePointer,
       "fsElpsPgConfigProtectionReverseServicePointer": fsElpsPgConfigProtectionReverseServicePointer,
       "fsElpsPgConfigWorkingInstanceId": fsElpsPgConfigWorkingInstanceId,
       "fsElpsPgConfigProtectionInstanceId": fsElpsPgConfigProtectionInstanceId,
       "fsElpsPgPscVersion": fsElpsPgPscVersion,
       "fsElpsPgCmdTable": fsElpsPgCmdTable,
       "fsElpsPgCmdEntry": fsElpsPgCmdEntry,
       "fsElpsPgCmdHoTime": fsElpsPgCmdHoTime,
       "fsElpsPgCmdWTR": fsElpsPgCmdWTR,
       "fsElpsPgCmdExtCmd": fsElpsPgCmdExtCmd,
       "fsElpsPgCmdExtCmdStatus": fsElpsPgCmdExtCmdStatus,
       "fsElpsPgCmdLocalCondition": fsElpsPgCmdLocalCondition,
       "fsElpsPgCmdLocalConditionStatus": fsElpsPgCmdLocalConditionStatus,
       "fsElpsPgCmdFarEndRequest": fsElpsPgCmdFarEndRequest,
       "fsElpsPgCmdFarEndRequestStatus": fsElpsPgCmdFarEndRequestStatus,
       "fsElpsPgCmdActiveRequest": fsElpsPgCmdActiveRequest,
       "fsElpsPgCmdSemState": fsElpsPgCmdSemState,
       "fsElpsPgCmdPgStatus": fsElpsPgCmdPgStatus,
       "fsElpsPgCmdApsPeriodicTime": fsElpsPgCmdApsPeriodicTime,
       "fsElpsPgCfmTable": fsElpsPgCfmTable,
       "fsElpsPgCfmEntry": fsElpsPgCfmEntry,
       "fsElpsPgCfmWorkingMEG": fsElpsPgCfmWorkingMEG,
       "fsElpsPgCfmWorkingME": fsElpsPgCfmWorkingME,
       "fsElpsPgCfmWorkingMEP": fsElpsPgCfmWorkingMEP,
       "fsElpsPgCfmProtectionMEG": fsElpsPgCfmProtectionMEG,
       "fsElpsPgCfmProtectionME": fsElpsPgCfmProtectionME,
       "fsElpsPgCfmProtectionMEP": fsElpsPgCfmProtectionMEP,
       "fsElpsPgCfmRowStatus": fsElpsPgCfmRowStatus,
       "fsElpsPgCfmWorkingReverseMEG": fsElpsPgCfmWorkingReverseMEG,
       "fsElpsPgCfmWorkingReverseME": fsElpsPgCfmWorkingReverseME,
       "fsElpsPgCfmWorkingReverseMEP": fsElpsPgCfmWorkingReverseMEP,
       "fsElpsPgCfmProtectionReverseMEG": fsElpsPgCfmProtectionReverseMEG,
       "fsElpsPgCfmProtectionReverseME": fsElpsPgCfmProtectionReverseME,
       "fsElpsPgCfmProtectionReverseMEP": fsElpsPgCfmProtectionReverseMEP,
       "fsElpsPgServiceListTable": fsElpsPgServiceListTable,
       "fsElpsPgServiceListEntry": fsElpsPgServiceListEntry,
       "fsElpsPgServiceListValue": fsElpsPgServiceListValue,
       "fsElpsPgServiceListRowStatus": fsElpsPgServiceListRowStatus,
       "fsElpsPgShareTable": fsElpsPgShareTable,
       "fsElpsPgShareEntry": fsElpsPgShareEntry,
       "fsElpsPgShareProtectionPort": fsElpsPgShareProtectionPort,
       "fsElpsPgSharePgStatus": fsElpsPgSharePgStatus,
       "fsElpsPgStatsTable": fsElpsPgStatsTable,
       "fsElpsPgStatsEntry": fsElpsPgStatsEntry,
       "fsElpsPgStatsAutoProtectionSwitchCount": fsElpsPgStatsAutoProtectionSwitchCount,
       "fsElpsPgStatsForcedSwitchCount": fsElpsPgStatsForcedSwitchCount,
       "fsElpsPgStatsManualSwitchCount": fsElpsPgStatsManualSwitchCount,
       "fsElpsPgStatsClearStatistics": fsElpsPgStatsClearStatistics,
       "fsElpsPgStatsApsPktTxCount": fsElpsPgStatsApsPktTxCount,
       "fsElpsPgStatsApsPktRxCount": fsElpsPgStatsApsPktRxCount,
       "fsElpsPgStatsApsPktDiscardCount": fsElpsPgStatsApsPktDiscardCount,
       "fsElpsPgLRSFRxTime": fsElpsPgLRSFRxTime,
       "fsElpsPgLRSFTxTime": fsElpsPgLRSFTxTime,
       "fsElpsPgFRSFRxTime": fsElpsPgFRSFRxTime,
       "fsElpsPgStateChgTime": fsElpsPgStateChgTime,
       "fsElpsPgServiceListPointerTable": fsElpsPgServiceListPointerTable,
       "fsElpsPgServiceListPointerEntry": fsElpsPgServiceListPointerEntry,
       "fsElpsPgServiceListId": fsElpsPgServiceListId,
       "fsElpsPgWorkingServiceListPointer": fsElpsPgWorkingServiceListPointer,
       "fsElpsPgWorkingReverseServiceListPointer": fsElpsPgWorkingReverseServiceListPointer,
       "fsElpsPgProtectionServiceListPointer": fsElpsPgProtectionServiceListPointer,
       "fsElpsPgProtectionReverseServiceListPointer": fsElpsPgProtectionReverseServiceListPointer,
       "fsElpsPgServiceListPointerRowStatus": fsElpsPgServiceListPointerRowStatus,
       "fsElpsPgNotifications": fsElpsPgNotifications,
       "fsElpsTraps": fsElpsTraps,
       "fsElpsProtectionSwitchTrap": fsElpsProtectionSwitchTrap,
       "fsElpsProtectionSwitchFailureTrap": fsElpsProtectionSwitchFailureTrap,
       "fsElpsProtectionTypeMismatchTrap": fsElpsProtectionTypeMismatchTrap,
       "fsElpsTrapContextName": fsElpsTrapContextName,
       "fsElpsTrapSwitchingMechanism": fsElpsTrapSwitchingMechanism,
       "fsElpsTrapMismatchType": fsElpsTrapMismatchType,
       "fsElpsTypeOfFailure": fsElpsTypeOfFailure,
       "fsElpsScalars": fsElpsScalars,
       "fsElpsStatsOneIsToOneApsPktTxCount": fsElpsStatsOneIsToOneApsPktTxCount,
       "fsElpsStatsOneIsToOneApsPktRxCount": fsElpsStatsOneIsToOneApsPktRxCount,
       "fsElpsStatsOneIsToOneApsPktDiscardCount": fsElpsStatsOneIsToOneApsPktDiscardCount,
       "fsElpsStatsOnePlusOneApsPktTxCount": fsElpsStatsOnePlusOneApsPktTxCount,
       "fsElpsStatsOnePlusOneApsPktRxCount": fsElpsStatsOnePlusOneApsPktRxCount,
       "fsElpsStatsOnePlusOneApsPktDiscardCount": fsElpsStatsOnePlusOneApsPktDiscardCount}
)
