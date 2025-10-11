# SNMP MIB module (ENTERASYS-ETH-OAM-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-ETH-OAM-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:07 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsysEthOamExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78)
)
if mibBuilder.loadTexts:
    etsysEthOamExtMIB.setRevisions(
        ("2012-02-07 14:54",
         "2010-11-23 19:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EtsysOamExtErrActions(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("syslog", 0),
          ("disable", 1))
    )


# MIB Managed Objects in the order of their OIDs

_EtsysEthOamExtObjects_ObjectIdentity = ObjectIdentity
etsysEthOamExtObjects = _EtsysEthOamExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1)
)
_EtsysEthOamExtTable_Object = MibTable
etsysEthOamExtTable = _EtsysEthOamExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 1)
)
if mibBuilder.loadTexts:
    etsysEthOamExtTable.setStatus("current")
_EtsysEthOamExtEntry_Object = MibTableRow
etsysEthOamExtEntry = _EtsysEthOamExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 1, 1)
)
etsysEthOamExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysEthOamExtEntry.setStatus("current")


class _EtsysEthOamExtOperStatus_Type(Integer32):
    """Custom type etsysEthOamExtOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("disabled", 2))
    )


_EtsysEthOamExtOperStatus_Type.__name__ = "Integer32"
_EtsysEthOamExtOperStatus_Object = MibTableColumn
etsysEthOamExtOperStatus = _EtsysEthOamExtOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 1, 1, 1),
    _EtsysEthOamExtOperStatus_Type()
)
etsysEthOamExtOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEthOamExtOperStatus.setStatus("current")
_EtsysEthOamExtEventConfigTable_Object = MibTable
etsysEthOamExtEventConfigTable = _EtsysEthOamExtEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 2)
)
if mibBuilder.loadTexts:
    etsysEthOamExtEventConfigTable.setStatus("current")
_EtsysEthOamExtEventConfigEntry_Object = MibTableRow
etsysEthOamExtEventConfigEntry = _EtsysEthOamExtEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 2, 1)
)
etsysEthOamExtEventConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysEthOamExtEventConfigEntry.setStatus("current")


class _EtsysEthOamExtEventConfigErrSymPeriodActions_Type(EtsysOamExtErrActions):
    """Custom type etsysEthOamExtEventConfigErrSymPeriodActions based on EtsysOamExtErrActions"""
    defaultHexValue = ""


_EtsysEthOamExtEventConfigErrSymPeriodActions_Type.__name__ = "EtsysOamExtErrActions"
_EtsysEthOamExtEventConfigErrSymPeriodActions_Object = MibTableColumn
etsysEthOamExtEventConfigErrSymPeriodActions = _EtsysEthOamExtEventConfigErrSymPeriodActions_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 2, 1, 1),
    _EtsysEthOamExtEventConfigErrSymPeriodActions_Type()
)
etsysEthOamExtEventConfigErrSymPeriodActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEthOamExtEventConfigErrSymPeriodActions.setStatus("current")


class _EtsysEthOamExtEventConfigErrFramePeriodActions_Type(EtsysOamExtErrActions):
    """Custom type etsysEthOamExtEventConfigErrFramePeriodActions based on EtsysOamExtErrActions"""
    defaultHexValue = ""


_EtsysEthOamExtEventConfigErrFramePeriodActions_Type.__name__ = "EtsysOamExtErrActions"
_EtsysEthOamExtEventConfigErrFramePeriodActions_Object = MibTableColumn
etsysEthOamExtEventConfigErrFramePeriodActions = _EtsysEthOamExtEventConfigErrFramePeriodActions_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 2, 1, 2),
    _EtsysEthOamExtEventConfigErrFramePeriodActions_Type()
)
etsysEthOamExtEventConfigErrFramePeriodActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEthOamExtEventConfigErrFramePeriodActions.setStatus("current")


class _EtsysEthOamExtEventConfigErrFrameActions_Type(EtsysOamExtErrActions):
    """Custom type etsysEthOamExtEventConfigErrFrameActions based on EtsysOamExtErrActions"""
    defaultHexValue = ""


_EtsysEthOamExtEventConfigErrFrameActions_Type.__name__ = "EtsysOamExtErrActions"
_EtsysEthOamExtEventConfigErrFrameActions_Object = MibTableColumn
etsysEthOamExtEventConfigErrFrameActions = _EtsysEthOamExtEventConfigErrFrameActions_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 2, 1, 3),
    _EtsysEthOamExtEventConfigErrFrameActions_Type()
)
etsysEthOamExtEventConfigErrFrameActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEthOamExtEventConfigErrFrameActions.setStatus("current")


class _EtsysEthOamExtEventConfigErrFrameSecsActions_Type(EtsysOamExtErrActions):
    """Custom type etsysEthOamExtEventConfigErrFrameSecsActions based on EtsysOamExtErrActions"""
    defaultHexValue = ""


_EtsysEthOamExtEventConfigErrFrameSecsActions_Type.__name__ = "EtsysOamExtErrActions"
_EtsysEthOamExtEventConfigErrFrameSecsActions_Object = MibTableColumn
etsysEthOamExtEventConfigErrFrameSecsActions = _EtsysEthOamExtEventConfigErrFrameSecsActions_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 2, 1, 4),
    _EtsysEthOamExtEventConfigErrFrameSecsActions_Type()
)
etsysEthOamExtEventConfigErrFrameSecsActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEthOamExtEventConfigErrFrameSecsActions.setStatus("current")


class _EtsysEthOamExtEventConfigErrNotifRetry_Type(Unsigned32):
    """Custom type etsysEthOamExtEventConfigErrNotifRetry based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_EtsysEthOamExtEventConfigErrNotifRetry_Type.__name__ = "Unsigned32"
_EtsysEthOamExtEventConfigErrNotifRetry_Object = MibTableColumn
etsysEthOamExtEventConfigErrNotifRetry = _EtsysEthOamExtEventConfigErrNotifRetry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 2, 1, 5),
    _EtsysEthOamExtEventConfigErrNotifRetry_Type()
)
etsysEthOamExtEventConfigErrNotifRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEthOamExtEventConfigErrNotifRetry.setStatus("current")
_EtsysEthOamExtUld_ObjectIdentity = ObjectIdentity
etsysEthOamExtUld = _EtsysEthOamExtUld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3)
)
_EtsysEthOamExtUldGroupTable_Object = MibTable
etsysEthOamExtUldGroupTable = _EtsysEthOamExtUldGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3, 1)
)
if mibBuilder.loadTexts:
    etsysEthOamExtUldGroupTable.setStatus("current")
_EtsysEthOamExtUldGroupEntry_Object = MibTableRow
etsysEthOamExtUldGroupEntry = _EtsysEthOamExtUldGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3, 1, 1)
)
etsysEthOamExtUldGroupEntry.setIndexNames(
    (0, "ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtUldGroupIndex"),
)
if mibBuilder.loadTexts:
    etsysEthOamExtUldGroupEntry.setStatus("current")
_EtsysEthOamExtUldGroupIndex_Type = Unsigned32
_EtsysEthOamExtUldGroupIndex_Object = MibTableColumn
etsysEthOamExtUldGroupIndex = _EtsysEthOamExtUldGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3, 1, 1, 1),
    _EtsysEthOamExtUldGroupIndex_Type()
)
etsysEthOamExtUldGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysEthOamExtUldGroupIndex.setStatus("current")
_EtsysEthOamExtUldGroupMaxFastPorts_Type = Unsigned32
_EtsysEthOamExtUldGroupMaxFastPorts_Object = MibTableColumn
etsysEthOamExtUldGroupMaxFastPorts = _EtsysEthOamExtUldGroupMaxFastPorts_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3, 1, 1, 2),
    _EtsysEthOamExtUldGroupMaxFastPorts_Type()
)
etsysEthOamExtUldGroupMaxFastPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEthOamExtUldGroupMaxFastPorts.setStatus("current")
_EtsysEthOamExtUldGroupFastPortsInUse_Type = Gauge32
_EtsysEthOamExtUldGroupFastPortsInUse_Object = MibTableColumn
etsysEthOamExtUldGroupFastPortsInUse = _EtsysEthOamExtUldGroupFastPortsInUse_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3, 1, 1, 3),
    _EtsysEthOamExtUldGroupFastPortsInUse_Type()
)
etsysEthOamExtUldGroupFastPortsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEthOamExtUldGroupFastPortsInUse.setStatus("current")
_EtsysEthOamExtUldPortTable_Object = MibTable
etsysEthOamExtUldPortTable = _EtsysEthOamExtUldPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3, 2)
)
if mibBuilder.loadTexts:
    etsysEthOamExtUldPortTable.setStatus("current")
_EtsysEthOamExtUldPortEntry_Object = MibTableRow
etsysEthOamExtUldPortEntry = _EtsysEthOamExtUldPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3, 2, 1)
)
etsysEthOamExtUldPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysEthOamExtUldPortEntry.setStatus("current")


class _EtsysEthOamExtUldPortMode_Type(Integer32):
    """Custom type etsysEthOamExtUldPortMode based on Integer32"""
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
        *(("disabled", 1),
          ("standard", 2),
          ("fast", 3))
    )


_EtsysEthOamExtUldPortMode_Type.__name__ = "Integer32"
_EtsysEthOamExtUldPortMode_Object = MibTableColumn
etsysEthOamExtUldPortMode = _EtsysEthOamExtUldPortMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3, 2, 1, 1),
    _EtsysEthOamExtUldPortMode_Type()
)
etsysEthOamExtUldPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEthOamExtUldPortMode.setStatus("current")


class _EtsysEthOamExtUldPortAction_Type(Integer32):
    """Custom type etsysEthOamExtUldPortAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("syslogOnly", 1),
          ("disablePort", 2))
    )


_EtsysEthOamExtUldPortAction_Type.__name__ = "Integer32"
_EtsysEthOamExtUldPortAction_Object = MibTableColumn
etsysEthOamExtUldPortAction = _EtsysEthOamExtUldPortAction_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3, 2, 1, 2),
    _EtsysEthOamExtUldPortAction_Type()
)
etsysEthOamExtUldPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEthOamExtUldPortAction.setStatus("current")
_EtsysEthOamExtUldPortActiveStatus_Type = TruthValue
_EtsysEthOamExtUldPortActiveStatus_Object = MibTableColumn
etsysEthOamExtUldPortActiveStatus = _EtsysEthOamExtUldPortActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3, 2, 1, 3),
    _EtsysEthOamExtUldPortActiveStatus_Type()
)
etsysEthOamExtUldPortActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEthOamExtUldPortActiveStatus.setStatus("current")


class _EtsysEthOamExtUldPortFastTimerConfig_Type(Unsigned32):
    """Custom type etsysEthOamExtUldPortFastTimerConfig based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_EtsysEthOamExtUldPortFastTimerConfig_Type.__name__ = "Unsigned32"
_EtsysEthOamExtUldPortFastTimerConfig_Object = MibTableColumn
etsysEthOamExtUldPortFastTimerConfig = _EtsysEthOamExtUldPortFastTimerConfig_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3, 2, 1, 4),
    _EtsysEthOamExtUldPortFastTimerConfig_Type()
)
etsysEthOamExtUldPortFastTimerConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEthOamExtUldPortFastTimerConfig.setStatus("current")
if mibBuilder.loadTexts:
    etsysEthOamExtUldPortFastTimerConfig.setUnits("deciseconds")
_EtsysEthOamExtUldPortActiveFastTimer_Type = Unsigned32
_EtsysEthOamExtUldPortActiveFastTimer_Object = MibTableColumn
etsysEthOamExtUldPortActiveFastTimer = _EtsysEthOamExtUldPortActiveFastTimer_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3, 2, 1, 5),
    _EtsysEthOamExtUldPortActiveFastTimer_Type()
)
etsysEthOamExtUldPortActiveFastTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEthOamExtUldPortActiveFastTimer.setStatus("current")
if mibBuilder.loadTexts:
    etsysEthOamExtUldPortActiveFastTimer.setUnits("deciseconds")


class _EtsysEthOamExtUldPortActiveFastStatus_Type(Integer32):
    """Custom type etsysEthOamExtUldPortActiveFastStatus based on Integer32"""
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
        *(("notActive", 1),
          ("activeSlow", 2),
          ("activeFast", 3),
          ("faultDetected", 4))
    )


_EtsysEthOamExtUldPortActiveFastStatus_Type.__name__ = "Integer32"
_EtsysEthOamExtUldPortActiveFastStatus_Object = MibTableColumn
etsysEthOamExtUldPortActiveFastStatus = _EtsysEthOamExtUldPortActiveFastStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3, 2, 1, 6),
    _EtsysEthOamExtUldPortActiveFastStatus_Type()
)
etsysEthOamExtUldPortActiveFastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEthOamExtUldPortActiveFastStatus.setStatus("current")


class _EtsysEthOamExtUldPortOperStatus_Type(Integer32):
    """Custom type etsysEthOamExtUldPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("disabled", 2))
    )


_EtsysEthOamExtUldPortOperStatus_Type.__name__ = "Integer32"
_EtsysEthOamExtUldPortOperStatus_Object = MibTableColumn
etsysEthOamExtUldPortOperStatus = _EtsysEthOamExtUldPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3, 2, 1, 7),
    _EtsysEthOamExtUldPortOperStatus_Type()
)
etsysEthOamExtUldPortOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEthOamExtUldPortOperStatus.setStatus("current")
_EtsysEthOamExtUldPortFastTxCount_Type = Counter32
_EtsysEthOamExtUldPortFastTxCount_Object = MibTableColumn
etsysEthOamExtUldPortFastTxCount = _EtsysEthOamExtUldPortFastTxCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3, 2, 1, 8),
    _EtsysEthOamExtUldPortFastTxCount_Type()
)
etsysEthOamExtUldPortFastTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEthOamExtUldPortFastTxCount.setStatus("current")
_EtsysEthOamExtUldPortFastRxCount_Type = Counter32
_EtsysEthOamExtUldPortFastRxCount_Object = MibTableColumn
etsysEthOamExtUldPortFastRxCount = _EtsysEthOamExtUldPortFastRxCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3, 2, 1, 9),
    _EtsysEthOamExtUldPortFastRxCount_Type()
)
etsysEthOamExtUldPortFastRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEthOamExtUldPortFastRxCount.setStatus("current")
_EtsysEthOamExtUldPortFastRxErrorCount_Type = Counter32
_EtsysEthOamExtUldPortFastRxErrorCount_Object = MibTableColumn
etsysEthOamExtUldPortFastRxErrorCount = _EtsysEthOamExtUldPortFastRxErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3, 2, 1, 10),
    _EtsysEthOamExtUldPortFastRxErrorCount_Type()
)
etsysEthOamExtUldPortFastRxErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEthOamExtUldPortFastRxErrorCount.setStatus("current")
_EtsysEthOamExtUldPortLastFastRxTime_Type = TimeTicks
_EtsysEthOamExtUldPortLastFastRxTime_Object = MibTableColumn
etsysEthOamExtUldPortLastFastRxTime = _EtsysEthOamExtUldPortLastFastRxTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3, 2, 1, 11),
    _EtsysEthOamExtUldPortLastFastRxTime_Type()
)
etsysEthOamExtUldPortLastFastRxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEthOamExtUldPortLastFastRxTime.setStatus("current")
_EtsysEthOamExtUldPortGroupIndex_Type = Unsigned32
_EtsysEthOamExtUldPortGroupIndex_Object = MibTableColumn
etsysEthOamExtUldPortGroupIndex = _EtsysEthOamExtUldPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3, 2, 1, 12),
    _EtsysEthOamExtUldPortGroupIndex_Type()
)
etsysEthOamExtUldPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEthOamExtUldPortGroupIndex.setStatus("current")


class _EtsysEthOamExtUldPortActiveOamMode_Type(Integer32):
    """Custom type etsysEthOamExtUldPortActiveOamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passive", 1),
          ("active", 2))
    )


_EtsysEthOamExtUldPortActiveOamMode_Type.__name__ = "Integer32"
_EtsysEthOamExtUldPortActiveOamMode_Object = MibTableColumn
etsysEthOamExtUldPortActiveOamMode = _EtsysEthOamExtUldPortActiveOamMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 1, 3, 2, 1, 13),
    _EtsysEthOamExtUldPortActiveOamMode_Type()
)
etsysEthOamExtUldPortActiveOamMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysEthOamExtUldPortActiveOamMode.setStatus("current")
_EtsysEthOamExtConformance_ObjectIdentity = ObjectIdentity
etsysEthOamExtConformance = _EtsysEthOamExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 2)
)
_EtsysEthOamExtGroups_ObjectIdentity = ObjectIdentity
etsysEthOamExtGroups = _EtsysEthOamExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 2, 1)
)
_EtsysEthOamExtCompliances_ObjectIdentity = ObjectIdentity
etsysEthOamExtCompliances = _EtsysEthOamExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 2, 2)
)

# Managed Objects groups

etsysEthOamExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 2, 1, 1)
)
etsysEthOamExtGroup.setObjects(
    ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtOperStatus")
)
if mibBuilder.loadTexts:
    etsysEthOamExtGroup.setStatus("current")

etsysEthOamExtEventConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 2, 1, 2)
)
etsysEthOamExtEventConfigGroup.setObjects(
      *(("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtEventConfigErrSymPeriodActions"),
        ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtEventConfigErrFramePeriodActions"),
        ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtEventConfigErrFrameActions"),
        ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtEventConfigErrFrameSecsActions"),
        ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtEventConfigErrNotifRetry"))
)
if mibBuilder.loadTexts:
    etsysEthOamExtEventConfigGroup.setStatus("current")

etsysEthOamExtUldConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 2, 1, 3)
)
etsysEthOamExtUldConfigGroup.setObjects(
      *(("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtUldGroupMaxFastPorts"),
        ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtUldGroupFastPortsInUse"),
        ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtUldPortMode"),
        ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtUldPortAction"),
        ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtUldPortActiveStatus"),
        ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtUldPortFastTimerConfig"),
        ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtUldPortActiveFastTimer"),
        ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtUldPortActiveFastStatus"),
        ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtUldPortOperStatus"),
        ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtUldPortFastTxCount"),
        ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtUldPortFastRxCount"),
        ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtUldPortFastRxErrorCount"),
        ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtUldPortLastFastRxTime"),
        ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtUldPortGroupIndex"),
        ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtUldPortActiveOamMode"))
)
if mibBuilder.loadTexts:
    etsysEthOamExtUldConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysEthOamExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 78, 2, 2, 1)
)
etsysEthOamExtCompliance.setObjects(
      *(("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtGroup"),
        ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtEventConfigGroup"),
        ("ENTERASYS-ETH-OAM-EXT-MIB", "etsysEthOamExtUldConfigGroup"))
)
if mibBuilder.loadTexts:
    etsysEthOamExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-ETH-OAM-EXT-MIB",
    **{"EtsysOamExtErrActions": EtsysOamExtErrActions,
       "etsysEthOamExtMIB": etsysEthOamExtMIB,
       "etsysEthOamExtObjects": etsysEthOamExtObjects,
       "etsysEthOamExtTable": etsysEthOamExtTable,
       "etsysEthOamExtEntry": etsysEthOamExtEntry,
       "etsysEthOamExtOperStatus": etsysEthOamExtOperStatus,
       "etsysEthOamExtEventConfigTable": etsysEthOamExtEventConfigTable,
       "etsysEthOamExtEventConfigEntry": etsysEthOamExtEventConfigEntry,
       "etsysEthOamExtEventConfigErrSymPeriodActions": etsysEthOamExtEventConfigErrSymPeriodActions,
       "etsysEthOamExtEventConfigErrFramePeriodActions": etsysEthOamExtEventConfigErrFramePeriodActions,
       "etsysEthOamExtEventConfigErrFrameActions": etsysEthOamExtEventConfigErrFrameActions,
       "etsysEthOamExtEventConfigErrFrameSecsActions": etsysEthOamExtEventConfigErrFrameSecsActions,
       "etsysEthOamExtEventConfigErrNotifRetry": etsysEthOamExtEventConfigErrNotifRetry,
       "etsysEthOamExtUld": etsysEthOamExtUld,
       "etsysEthOamExtUldGroupTable": etsysEthOamExtUldGroupTable,
       "etsysEthOamExtUldGroupEntry": etsysEthOamExtUldGroupEntry,
       "etsysEthOamExtUldGroupIndex": etsysEthOamExtUldGroupIndex,
       "etsysEthOamExtUldGroupMaxFastPorts": etsysEthOamExtUldGroupMaxFastPorts,
       "etsysEthOamExtUldGroupFastPortsInUse": etsysEthOamExtUldGroupFastPortsInUse,
       "etsysEthOamExtUldPortTable": etsysEthOamExtUldPortTable,
       "etsysEthOamExtUldPortEntry": etsysEthOamExtUldPortEntry,
       "etsysEthOamExtUldPortMode": etsysEthOamExtUldPortMode,
       "etsysEthOamExtUldPortAction": etsysEthOamExtUldPortAction,
       "etsysEthOamExtUldPortActiveStatus": etsysEthOamExtUldPortActiveStatus,
       "etsysEthOamExtUldPortFastTimerConfig": etsysEthOamExtUldPortFastTimerConfig,
       "etsysEthOamExtUldPortActiveFastTimer": etsysEthOamExtUldPortActiveFastTimer,
       "etsysEthOamExtUldPortActiveFastStatus": etsysEthOamExtUldPortActiveFastStatus,
       "etsysEthOamExtUldPortOperStatus": etsysEthOamExtUldPortOperStatus,
       "etsysEthOamExtUldPortFastTxCount": etsysEthOamExtUldPortFastTxCount,
       "etsysEthOamExtUldPortFastRxCount": etsysEthOamExtUldPortFastRxCount,
       "etsysEthOamExtUldPortFastRxErrorCount": etsysEthOamExtUldPortFastRxErrorCount,
       "etsysEthOamExtUldPortLastFastRxTime": etsysEthOamExtUldPortLastFastRxTime,
       "etsysEthOamExtUldPortGroupIndex": etsysEthOamExtUldPortGroupIndex,
       "etsysEthOamExtUldPortActiveOamMode": etsysEthOamExtUldPortActiveOamMode,
       "etsysEthOamExtConformance": etsysEthOamExtConformance,
       "etsysEthOamExtGroups": etsysEthOamExtGroups,
       "etsysEthOamExtGroup": etsysEthOamExtGroup,
       "etsysEthOamExtEventConfigGroup": etsysEthOamExtEventConfigGroup,
       "etsysEthOamExtUldConfigGroup": etsysEthOamExtUldConfigGroup,
       "etsysEthOamExtCompliances": etsysEthOamExtCompliances,
       "etsysEthOamExtCompliance": etsysEthOamExtCompliance}
)
