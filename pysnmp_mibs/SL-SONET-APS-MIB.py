# SNMP MIB module (SL-SONET-APS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/smartoptics/SL-SONET-APS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:31:04 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(slSonetMib,) = mibBuilder.importSymbols(
    "SL-SONET-MIB",
    "slSonetMib")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

slSonetApsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SlSonetApsConfig_ObjectIdentity = ObjectIdentity
slSonetApsConfig = _SlSonetApsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1)
)
_SlSonetApsConfigTable_Object = MibTable
slSonetApsConfigTable = _SlSonetApsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1)
)
if mibBuilder.loadTexts:
    slSonetApsConfigTable.setStatus("current")
_SlSonetApsConfigEntry_Object = MibTableRow
slSonetApsConfigEntry = _SlSonetApsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1)
)
slSonetApsConfigEntry.setIndexNames(
    (0, "SL-SONET-APS-MIB", "slSonetApsWorkingIndex"),
)
if mibBuilder.loadTexts:
    slSonetApsConfigEntry.setStatus("current")
_SlSonetApsWorkingIndex_Type = InterfaceIndex
_SlSonetApsWorkingIndex_Object = MibTableColumn
slSonetApsWorkingIndex = _SlSonetApsWorkingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 1),
    _SlSonetApsWorkingIndex_Type()
)
slSonetApsWorkingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetApsWorkingIndex.setStatus("current")
_SlSonetApsProtectionIndex_Type = InterfaceIndex
_SlSonetApsProtectionIndex_Object = MibTableColumn
slSonetApsProtectionIndex = _SlSonetApsProtectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 2),
    _SlSonetApsProtectionIndex_Type()
)
slSonetApsProtectionIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slSonetApsProtectionIndex.setStatus("current")


class _SlSonetApsEnable_Type(Integer32):
    """Custom type slSonetApsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slSonetApsDisabled", 1),
          ("slSonetApsEnabled", 2))
    )


_SlSonetApsEnable_Type.__name__ = "Integer32"
_SlSonetApsEnable_Object = MibTableColumn
slSonetApsEnable = _SlSonetApsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 3),
    _SlSonetApsEnable_Type()
)
slSonetApsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slSonetApsEnable.setStatus("current")


class _SlSonetApsArchMode_Type(Integer32):
    """Custom type slSonetApsArchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onePlusOne", 1),
          ("oneToOne", 2))
    )


_SlSonetApsArchMode_Type.__name__ = "Integer32"
_SlSonetApsArchMode_Object = MibTableColumn
slSonetApsArchMode = _SlSonetApsArchMode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 4),
    _SlSonetApsArchMode_Type()
)
slSonetApsArchMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slSonetApsArchMode.setStatus("current")


class _SlSonetApsActiveLineRx_Type(Integer32):
    """Custom type slSonetApsActiveLineRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slSonetApsWorkingLine", 1),
          ("slSonetApsProtectionLine", 2))
    )


_SlSonetApsActiveLineRx_Type.__name__ = "Integer32"
_SlSonetApsActiveLineRx_Object = MibTableColumn
slSonetApsActiveLineRx = _SlSonetApsActiveLineRx_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 5),
    _SlSonetApsActiveLineRx_Type()
)
slSonetApsActiveLineRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetApsActiveLineRx.setStatus("current")


class _SlSonetApsActiveLineTx_Type(Integer32):
    """Custom type slSonetApsActiveLineTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slSonetApsWorkingLine", 1),
          ("slSonetApsProtectionLine", 2))
    )


_SlSonetApsActiveLineTx_Type.__name__ = "Integer32"
_SlSonetApsActiveLineTx_Object = MibTableColumn
slSonetApsActiveLineTx = _SlSonetApsActiveLineTx_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 6),
    _SlSonetApsActiveLineTx_Type()
)
slSonetApsActiveLineTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetApsActiveLineTx.setStatus("current")


class _SlSonetApsWaitToRestore_Type(Unsigned32):
    """Custom type slSonetApsWaitToRestore based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SlSonetApsWaitToRestore_Type.__name__ = "Unsigned32"
_SlSonetApsWaitToRestore_Object = MibTableColumn
slSonetApsWaitToRestore = _SlSonetApsWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 7),
    _SlSonetApsWaitToRestore_Type()
)
slSonetApsWaitToRestore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slSonetApsWaitToRestore.setStatus("current")
if mibBuilder.loadTexts:
    slSonetApsWaitToRestore.setUnits("minutes")


class _SlSonetApsDirection_Type(Integer32):
    """Custom type slSonetApsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uniDirectional", 1),
          ("biDirectional", 2))
    )


_SlSonetApsDirection_Type.__name__ = "Integer32"
_SlSonetApsDirection_Object = MibTableColumn
slSonetApsDirection = _SlSonetApsDirection_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 8),
    _SlSonetApsDirection_Type()
)
slSonetApsDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slSonetApsDirection.setStatus("current")


class _SlSonetApsRevertive_Type(Integer32):
    """Custom type slSonetApsRevertive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 1),
          ("revertive", 2))
    )


_SlSonetApsRevertive_Type.__name__ = "Integer32"
_SlSonetApsRevertive_Object = MibTableColumn
slSonetApsRevertive = _SlSonetApsRevertive_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 9),
    _SlSonetApsRevertive_Type()
)
slSonetApsRevertive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slSonetApsRevertive.setStatus("current")


class _SlSonetApsDirectionOperational_Type(Integer32):
    """Custom type slSonetApsDirectionOperational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uniDirectional", 1),
          ("biDirectional", 2))
    )


_SlSonetApsDirectionOperational_Type.__name__ = "Integer32"
_SlSonetApsDirectionOperational_Object = MibTableColumn
slSonetApsDirectionOperational = _SlSonetApsDirectionOperational_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 10),
    _SlSonetApsDirectionOperational_Type()
)
slSonetApsDirectionOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetApsDirectionOperational.setStatus("current")


class _SlSonetApsArchModeOperational_Type(Integer32):
    """Custom type slSonetApsArchModeOperational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onePlusOne", 1),
          ("oneToOne", 2))
    )


_SlSonetApsArchModeOperational_Type.__name__ = "Integer32"
_SlSonetApsArchModeOperational_Object = MibTableColumn
slSonetApsArchModeOperational = _SlSonetApsArchModeOperational_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 11),
    _SlSonetApsArchModeOperational_Type()
)
slSonetApsArchModeOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetApsArchModeOperational.setStatus("current")


class _SlSonetApsChanStatus_Type(Bits):
    """Custom type slSonetApsChanStatus based on Bits"""
    namedValues = NamedValues(
        *(("lockedOut", 0),
          ("sdWorking", 1),
          ("sdProtecting", 2),
          ("sfWorking", 3),
          ("sfProtecting", 4),
          ("switched", 5),
          ("remoteRequest", 6))
    )

_SlSonetApsChanStatus_Type.__name__ = "Bits"
_SlSonetApsChanStatus_Object = MibTableColumn
slSonetApsChanStatus = _SlSonetApsChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 12),
    _SlSonetApsChanStatus_Type()
)
slSonetApsChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetApsChanStatus.setStatus("current")
_SlSonetApsChanSignalDegrades_Type = Counter32
_SlSonetApsChanSignalDegrades_Object = MibTableColumn
slSonetApsChanSignalDegrades = _SlSonetApsChanSignalDegrades_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 13),
    _SlSonetApsChanSignalDegrades_Type()
)
slSonetApsChanSignalDegrades.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetApsChanSignalDegrades.setStatus("current")
_SlSonetApsChanSignalFailures_Type = Counter32
_SlSonetApsChanSignalFailures_Object = MibTableColumn
slSonetApsChanSignalFailures = _SlSonetApsChanSignalFailures_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 14),
    _SlSonetApsChanSignalFailures_Type()
)
slSonetApsChanSignalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetApsChanSignalFailures.setStatus("current")
_SlSonetApsChanLastSwitchover_Type = TimeTicks
_SlSonetApsChanLastSwitchover_Object = MibTableColumn
slSonetApsChanLastSwitchover = _SlSonetApsChanLastSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 15),
    _SlSonetApsChanLastSwitchover_Type()
)
slSonetApsChanLastSwitchover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetApsChanLastSwitchover.setStatus("current")


class _SlSonetApsLineFailureCodeStatus_Type(Bits):
    """Custom type slSonetApsLineFailureCodeStatus based on Bits"""
    namedValues = NamedValues(
        *(("slSonetApsChannelMismatch", 0),
          ("slSonetApsProtectionByteFail", 1),
          ("slSonetApsFEProtectionFailure", 2),
          ("slSonetApsModeMismatch", 3))
    )

_SlSonetApsLineFailureCodeStatus_Type.__name__ = "Bits"
_SlSonetApsLineFailureCodeStatus_Object = MibTableColumn
slSonetApsLineFailureCodeStatus = _SlSonetApsLineFailureCodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 16),
    _SlSonetApsLineFailureCodeStatus_Type()
)
slSonetApsLineFailureCodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetApsLineFailureCodeStatus.setStatus("current")


class _SlSonetApsConfigSwitchCommand_Type(Integer32):
    """Custom type slSonetApsConfigSwitchCommand based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("lockoutOfProtection", 2),
          ("forcedSwitchOfWorking", 3),
          ("forcedSwitchOfProtection", 4),
          ("manualSwitchOfWorking", 5),
          ("manualSwitchOfProtection", 6),
          ("exercise", 7))
    )


_SlSonetApsConfigSwitchCommand_Type.__name__ = "Integer32"
_SlSonetApsConfigSwitchCommand_Object = MibTableColumn
slSonetApsConfigSwitchCommand = _SlSonetApsConfigSwitchCommand_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 17),
    _SlSonetApsConfigSwitchCommand_Type()
)
slSonetApsConfigSwitchCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slSonetApsConfigSwitchCommand.setStatus("current")


class _SlSonetApsLineSwitchReason_Type(Integer32):
    """Custom type slSonetApsLineSwitchReason based on Integer32"""
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
        *(("slSonetApsOther", 1),
          ("slSonetApsRevertive", 2),
          ("slSonetApsManual", 3),
          ("slSonetApsSignalDegrade", 4),
          ("slSonetApsSignalFailure", 5),
          ("slSonetApsForceSwitch", 6),
          ("slSonetApsRemoteRequest", 7),
          ("slSonetApsLockOut", 8))
    )


_SlSonetApsLineSwitchReason_Type.__name__ = "Integer32"
_SlSonetApsLineSwitchReason_Object = MibTableColumn
slSonetApsLineSwitchReason = _SlSonetApsLineSwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 18),
    _SlSonetApsLineSwitchReason_Type()
)
slSonetApsLineSwitchReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetApsLineSwitchReason.setStatus("current")


class _SlSonetApsResetCounters_Type(Integer32):
    """Custom type slSonetApsResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetCounters", 1)
    )


_SlSonetApsResetCounters_Type.__name__ = "Integer32"
_SlSonetApsResetCounters_Object = MibTableColumn
slSonetApsResetCounters = _SlSonetApsResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 19),
    _SlSonetApsResetCounters_Type()
)
slSonetApsResetCounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slSonetApsResetCounters.setStatus("current")


class _SlSonetApsConfigActiveRequest_Type(Integer32):
    """Custom type slSonetApsConfigActiveRequest based on Integer32"""
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
        *(("slSonetApsOther", 1),
          ("slSonetApsRevertive", 2),
          ("slSonetApsManual", 3),
          ("slSonetApsSignalDegrade", 4),
          ("slSonetApsSignalFailure", 5),
          ("slSonetApsForceSwitch", 6),
          ("slSonetApsRemoteRequest", 7),
          ("slSonetApsLockOut", 8))
    )


_SlSonetApsConfigActiveRequest_Type.__name__ = "Integer32"
_SlSonetApsConfigActiveRequest_Object = MibTableColumn
slSonetApsConfigActiveRequest = _SlSonetApsConfigActiveRequest_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 20),
    _SlSonetApsConfigActiveRequest_Type()
)
slSonetApsConfigActiveRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slSonetApsConfigActiveRequest.setStatus("current")
_SlSonetApsConfigExerciseResult_Type = TruthValue
_SlSonetApsConfigExerciseResult_Object = MibTableColumn
slSonetApsConfigExerciseResult = _SlSonetApsConfigExerciseResult_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 1, 1, 1, 21),
    _SlSonetApsConfigExerciseResult_Type()
)
slSonetApsConfigExerciseResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSonetApsConfigExerciseResult.setStatus("current")
_SlSonetApsTraps_ObjectIdentity = ObjectIdentity
slSonetApsTraps = _SlSonetApsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 2)
)

# Managed Objects groups


# Notification objects

slSonetApsTrapSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 2, 1)
)
slSonetApsTrapSwitchover.setObjects(
      *(("SL-SONET-APS-MIB", "slSonetApsWorkingIndex"),
        ("SL-SONET-APS-MIB", "slSonetApsActiveLineRx"),
        ("SL-SONET-APS-MIB", "slSonetApsLineSwitchReason"))
)
if mibBuilder.loadTexts:
    slSonetApsTrapSwitchover.setStatus(
        "current"
    )

slSonetApsTrapFailureCodeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 2, 2)
)
slSonetApsTrapFailureCodeChanged.setObjects(
      *(("SL-SONET-APS-MIB", "slSonetApsWorkingIndex"),
        ("SL-SONET-APS-MIB", "slSonetApsLineFailureCodeStatus"))
)
if mibBuilder.loadTexts:
    slSonetApsTrapFailureCodeChanged.setStatus(
        "current"
    )

slSonetApsTrapEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 6, 5, 2, 3)
)
slSonetApsTrapEnabled.setObjects(
      *(("SL-SONET-APS-MIB", "slSonetApsWorkingIndex"),
        ("SL-SONET-APS-MIB", "slSonetApsEnable"))
)
if mibBuilder.loadTexts:
    slSonetApsTrapEnabled.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-SONET-APS-MIB",
    **{"slSonetApsMib": slSonetApsMib,
       "slSonetApsConfig": slSonetApsConfig,
       "slSonetApsConfigTable": slSonetApsConfigTable,
       "slSonetApsConfigEntry": slSonetApsConfigEntry,
       "slSonetApsWorkingIndex": slSonetApsWorkingIndex,
       "slSonetApsProtectionIndex": slSonetApsProtectionIndex,
       "slSonetApsEnable": slSonetApsEnable,
       "slSonetApsArchMode": slSonetApsArchMode,
       "slSonetApsActiveLineRx": slSonetApsActiveLineRx,
       "slSonetApsActiveLineTx": slSonetApsActiveLineTx,
       "slSonetApsWaitToRestore": slSonetApsWaitToRestore,
       "slSonetApsDirection": slSonetApsDirection,
       "slSonetApsRevertive": slSonetApsRevertive,
       "slSonetApsDirectionOperational": slSonetApsDirectionOperational,
       "slSonetApsArchModeOperational": slSonetApsArchModeOperational,
       "slSonetApsChanStatus": slSonetApsChanStatus,
       "slSonetApsChanSignalDegrades": slSonetApsChanSignalDegrades,
       "slSonetApsChanSignalFailures": slSonetApsChanSignalFailures,
       "slSonetApsChanLastSwitchover": slSonetApsChanLastSwitchover,
       "slSonetApsLineFailureCodeStatus": slSonetApsLineFailureCodeStatus,
       "slSonetApsConfigSwitchCommand": slSonetApsConfigSwitchCommand,
       "slSonetApsLineSwitchReason": slSonetApsLineSwitchReason,
       "slSonetApsResetCounters": slSonetApsResetCounters,
       "slSonetApsConfigActiveRequest": slSonetApsConfigActiveRequest,
       "slSonetApsConfigExerciseResult": slSonetApsConfigExerciseResult,
       "slSonetApsTraps": slSonetApsTraps,
       "slSonetApsTrapSwitchover": slSonetApsTrapSwitchover,
       "slSonetApsTrapFailureCodeChanged": slSonetApsTrapFailureCodeChanged,
       "slSonetApsTrapEnabled": slSonetApsTrapEnabled}
)
