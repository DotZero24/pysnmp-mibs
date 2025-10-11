# SNMP MIB module (INFINERA-TP-CHANNELCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-CHANNELCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:23 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

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

channelCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    channelCtpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChannelCtpTable_Object = MibTable
channelCtpTable = _ChannelCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    channelCtpTable.setStatus("current")
_ChannelCtpEntry_Object = MibTableRow
channelCtpEntry = _ChannelCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1)
)
channelCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    channelCtpEntry.setStatus("current")


class _ChannelCtpPreFecThresholdOrder_Type(Integer32):
    """Custom type channelCtpPreFecThresholdOrder based on Integer32"""
    defaultValue = -4


_ChannelCtpPreFecThresholdOrder_Type.__name__ = "Integer32"
_ChannelCtpPreFecThresholdOrder_Object = MibTableColumn
channelCtpPreFecThresholdOrder = _ChannelCtpPreFecThresholdOrder_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 1),
    _ChannelCtpPreFecThresholdOrder_Type()
)
channelCtpPreFecThresholdOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpPreFecThresholdOrder.setStatus("current")


class _ChannelCtpPreFecThresholdMantissa_Type(Integer32):
    """Custom type channelCtpPreFecThresholdMantissa based on Integer32"""
    defaultValue = 1


_ChannelCtpPreFecThresholdMantissa_Type.__name__ = "Integer32"
_ChannelCtpPreFecThresholdMantissa_Object = MibTableColumn
channelCtpPreFecThresholdMantissa = _ChannelCtpPreFecThresholdMantissa_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 2),
    _ChannelCtpPreFecThresholdMantissa_Type()
)
channelCtpPreFecThresholdMantissa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpPreFecThresholdMantissa.setStatus("current")


class _ChannelCtpSignalDegradeReporting_Type(Integer32):
    """Custom type channelCtpSignalDegradeReporting based on Integer32"""
    defaultValue = 2

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


_ChannelCtpSignalDegradeReporting_Type.__name__ = "Integer32"
_ChannelCtpSignalDegradeReporting_Object = MibTableColumn
channelCtpSignalDegradeReporting = _ChannelCtpSignalDegradeReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 3),
    _ChannelCtpSignalDegradeReporting_Type()
)
channelCtpSignalDegradeReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpSignalDegradeReporting.setStatus("current")


class _ChannelCtpInsertDtsTti_Type(TruthValue):
    """Custom type channelCtpInsertDtsTti based on TruthValue"""
    defaultValue = 2


_ChannelCtpInsertDtsTti_Type.__name__ = "TruthValue"
_ChannelCtpInsertDtsTti_Object = MibTableColumn
channelCtpInsertDtsTti = _ChannelCtpInsertDtsTti_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 4),
    _ChannelCtpInsertDtsTti_Type()
)
channelCtpInsertDtsTti.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpInsertDtsTti.setStatus("current")


class _ChannelCtpDtsTtiAlarmReporting_Type(Integer32):
    """Custom type channelCtpDtsTtiAlarmReporting based on Integer32"""
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


_ChannelCtpDtsTtiAlarmReporting_Type.__name__ = "Integer32"
_ChannelCtpDtsTtiAlarmReporting_Object = MibTableColumn
channelCtpDtsTtiAlarmReporting = _ChannelCtpDtsTtiAlarmReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 5),
    _ChannelCtpDtsTtiAlarmReporting_Type()
)
channelCtpDtsTtiAlarmReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpDtsTtiAlarmReporting.setStatus("current")
_ChannelCtpTxDtsTti_Type = DisplayString
_ChannelCtpTxDtsTti_Object = MibTableColumn
channelCtpTxDtsTti = _ChannelCtpTxDtsTti_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 6),
    _ChannelCtpTxDtsTti_Type()
)
channelCtpTxDtsTti.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpTxDtsTti.setStatus("current")
_ChannelCtpExpectedDtsTti_Type = DisplayString
_ChannelCtpExpectedDtsTti_Object = MibTableColumn
channelCtpExpectedDtsTti = _ChannelCtpExpectedDtsTti_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 7),
    _ChannelCtpExpectedDtsTti_Type()
)
channelCtpExpectedDtsTti.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpExpectedDtsTti.setStatus("current")
_ChannelCtpRxDtsTti_Type = DisplayString
_ChannelCtpRxDtsTti_Object = MibTableColumn
channelCtpRxDtsTti = _ChannelCtpRxDtsTti_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 8),
    _ChannelCtpRxDtsTti_Type()
)
channelCtpRxDtsTti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpRxDtsTti.setStatus("current")


class _ChannelCtpDtsCv15MinutesTce_Type(Integer32):
    """Custom type channelCtpDtsCv15MinutesTce based on Integer32"""
    defaultValue = 1500


_ChannelCtpDtsCv15MinutesTce_Type.__name__ = "Integer32"
_ChannelCtpDtsCv15MinutesTce_Object = MibTableColumn
channelCtpDtsCv15MinutesTce = _ChannelCtpDtsCv15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 9),
    _ChannelCtpDtsCv15MinutesTce_Type()
)
channelCtpDtsCv15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpDtsCv15MinutesTce.setStatus("current")


class _ChannelCtpDtsEs15MinutesTce_Type(Integer32):
    """Custom type channelCtpDtsEs15MinutesTce based on Integer32"""
    defaultValue = 120


_ChannelCtpDtsEs15MinutesTce_Type.__name__ = "Integer32"
_ChannelCtpDtsEs15MinutesTce_Object = MibTableColumn
channelCtpDtsEs15MinutesTce = _ChannelCtpDtsEs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 10),
    _ChannelCtpDtsEs15MinutesTce_Type()
)
channelCtpDtsEs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpDtsEs15MinutesTce.setStatus("current")


class _ChannelCtpDtsSes15MinutesTce_Type(Integer32):
    """Custom type channelCtpDtsSes15MinutesTce based on Integer32"""
    defaultValue = 3


_ChannelCtpDtsSes15MinutesTce_Type.__name__ = "Integer32"
_ChannelCtpDtsSes15MinutesTce_Object = MibTableColumn
channelCtpDtsSes15MinutesTce = _ChannelCtpDtsSes15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 11),
    _ChannelCtpDtsSes15MinutesTce_Type()
)
channelCtpDtsSes15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpDtsSes15MinutesTce.setStatus("current")


class _ChannelCtpDtsCvDayTce_Type(Integer32):
    """Custom type channelCtpDtsCvDayTce based on Integer32"""
    defaultValue = 15000


_ChannelCtpDtsCvDayTce_Type.__name__ = "Integer32"
_ChannelCtpDtsCvDayTce_Object = MibTableColumn
channelCtpDtsCvDayTce = _ChannelCtpDtsCvDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 12),
    _ChannelCtpDtsCvDayTce_Type()
)
channelCtpDtsCvDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpDtsCvDayTce.setStatus("current")


class _ChannelCtpDtsEsDayTce_Type(Integer32):
    """Custom type channelCtpDtsEsDayTce based on Integer32"""
    defaultValue = 1200


_ChannelCtpDtsEsDayTce_Type.__name__ = "Integer32"
_ChannelCtpDtsEsDayTce_Object = MibTableColumn
channelCtpDtsEsDayTce = _ChannelCtpDtsEsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 13),
    _ChannelCtpDtsEsDayTce_Type()
)
channelCtpDtsEsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpDtsEsDayTce.setStatus("current")


class _ChannelCtpDtsSesDayTce_Type(Integer32):
    """Custom type channelCtpDtsSesDayTce based on Integer32"""
    defaultValue = 7


_ChannelCtpDtsSesDayTce_Type.__name__ = "Integer32"
_ChannelCtpDtsSesDayTce_Object = MibTableColumn
channelCtpDtsSesDayTce = _ChannelCtpDtsSesDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 14),
    _ChannelCtpDtsSesDayTce_Type()
)
channelCtpDtsSesDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpDtsSesDayTce.setStatus("current")


class _ChannelCtpDtsCv15MinutesTceReporting_Type(TruthValue):
    """Custom type channelCtpDtsCv15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_ChannelCtpDtsCv15MinutesTceReporting_Type.__name__ = "TruthValue"
_ChannelCtpDtsCv15MinutesTceReporting_Object = MibTableColumn
channelCtpDtsCv15MinutesTceReporting = _ChannelCtpDtsCv15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 15),
    _ChannelCtpDtsCv15MinutesTceReporting_Type()
)
channelCtpDtsCv15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpDtsCv15MinutesTceReporting.setStatus("current")


class _ChannelCtpDtsEs15MinutesTceReporting_Type(TruthValue):
    """Custom type channelCtpDtsEs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_ChannelCtpDtsEs15MinutesTceReporting_Type.__name__ = "TruthValue"
_ChannelCtpDtsEs15MinutesTceReporting_Object = MibTableColumn
channelCtpDtsEs15MinutesTceReporting = _ChannelCtpDtsEs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 16),
    _ChannelCtpDtsEs15MinutesTceReporting_Type()
)
channelCtpDtsEs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpDtsEs15MinutesTceReporting.setStatus("current")


class _ChannelCtpDtsSes15MinutesTceReporting_Type(TruthValue):
    """Custom type channelCtpDtsSes15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_ChannelCtpDtsSes15MinutesTceReporting_Type.__name__ = "TruthValue"
_ChannelCtpDtsSes15MinutesTceReporting_Object = MibTableColumn
channelCtpDtsSes15MinutesTceReporting = _ChannelCtpDtsSes15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 17),
    _ChannelCtpDtsSes15MinutesTceReporting_Type()
)
channelCtpDtsSes15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpDtsSes15MinutesTceReporting.setStatus("current")


class _ChannelCtpDtsCvDayTceReporting_Type(TruthValue):
    """Custom type channelCtpDtsCvDayTceReporting based on TruthValue"""
    defaultValue = 2


_ChannelCtpDtsCvDayTceReporting_Type.__name__ = "TruthValue"
_ChannelCtpDtsCvDayTceReporting_Object = MibTableColumn
channelCtpDtsCvDayTceReporting = _ChannelCtpDtsCvDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 18),
    _ChannelCtpDtsCvDayTceReporting_Type()
)
channelCtpDtsCvDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpDtsCvDayTceReporting.setStatus("current")


class _ChannelCtpDtsEsDayTceReporting_Type(TruthValue):
    """Custom type channelCtpDtsEsDayTceReporting based on TruthValue"""
    defaultValue = 2


_ChannelCtpDtsEsDayTceReporting_Type.__name__ = "TruthValue"
_ChannelCtpDtsEsDayTceReporting_Object = MibTableColumn
channelCtpDtsEsDayTceReporting = _ChannelCtpDtsEsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 19),
    _ChannelCtpDtsEsDayTceReporting_Type()
)
channelCtpDtsEsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpDtsEsDayTceReporting.setStatus("current")


class _ChannelCtpDtsSesDayTceReporting_Type(TruthValue):
    """Custom type channelCtpDtsSesDayTceReporting based on TruthValue"""
    defaultValue = 2


_ChannelCtpDtsSesDayTceReporting_Type.__name__ = "TruthValue"
_ChannelCtpDtsSesDayTceReporting_Object = MibTableColumn
channelCtpDtsSesDayTceReporting = _ChannelCtpDtsSesDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 20),
    _ChannelCtpDtsSesDayTceReporting_Type()
)
channelCtpDtsSesDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpDtsSesDayTceReporting.setStatus("current")


class _ChannelCtpPrbsGenerationMode_Type(Integer32):
    """Custom type channelCtpPrbsGenerationMode based on Integer32"""
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


_ChannelCtpPrbsGenerationMode_Type.__name__ = "Integer32"
_ChannelCtpPrbsGenerationMode_Object = MibTableColumn
channelCtpPrbsGenerationMode = _ChannelCtpPrbsGenerationMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 21),
    _ChannelCtpPrbsGenerationMode_Type()
)
channelCtpPrbsGenerationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpPrbsGenerationMode.setStatus("current")


class _ChannelCtpPrbsMonitoringMode_Type(Integer32):
    """Custom type channelCtpPrbsMonitoringMode based on Integer32"""
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


_ChannelCtpPrbsMonitoringMode_Type.__name__ = "Integer32"
_ChannelCtpPrbsMonitoringMode_Object = MibTableColumn
channelCtpPrbsMonitoringMode = _ChannelCtpPrbsMonitoringMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 22),
    _ChannelCtpPrbsMonitoringMode_Type()
)
channelCtpPrbsMonitoringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpPrbsMonitoringMode.setStatus("current")


class _ChannelCtpTEEnabled_Type(TruthValue):
    """Custom type channelCtpTEEnabled based on TruthValue"""
    defaultValue = 1


_ChannelCtpTEEnabled_Type.__name__ = "TruthValue"
_ChannelCtpTEEnabled_Object = MibTableColumn
channelCtpTEEnabled = _ChannelCtpTEEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 23),
    _ChannelCtpTEEnabled_Type()
)
channelCtpTEEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpTEEnabled.setStatus("current")


class _ChannelCtpPmHistStatsEnable_Type(Integer32):
    """Custom type channelCtpPmHistStatsEnable based on Integer32"""
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


_ChannelCtpPmHistStatsEnable_Type.__name__ = "Integer32"
_ChannelCtpPmHistStatsEnable_Object = MibTableColumn
channelCtpPmHistStatsEnable = _ChannelCtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 1, 1, 24),
    _ChannelCtpPmHistStatsEnable_Type()
)
channelCtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelCtpPmHistStatsEnable.setStatus("current")
_ChannelCtpConformance_ObjectIdentity = ObjectIdentity
channelCtpConformance = _ChannelCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 3)
)
_ChannelCtpCompliances_ObjectIdentity = ObjectIdentity
channelCtpCompliances = _ChannelCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 3, 1)
)
_ChannelCtpGroups_ObjectIdentity = ObjectIdentity
channelCtpGroups = _ChannelCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 3, 2)
)

# Managed Objects groups

channelCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 3, 2, 1)
)
channelCtpGroup.setObjects(
      *(("INFINERA-TP-CHANNELCTP-MIB", "channelCtpPreFecThresholdOrder"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpPreFecThresholdMantissa"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpSignalDegradeReporting"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpInsertDtsTti"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpDtsTtiAlarmReporting"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpTxDtsTti"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpExpectedDtsTti"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpRxDtsTti"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpDtsCv15MinutesTce"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpDtsEs15MinutesTce"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpDtsSes15MinutesTce"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpDtsCvDayTce"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpDtsEsDayTce"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpDtsSesDayTce"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpDtsCv15MinutesTceReporting"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpDtsEs15MinutesTceReporting"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpDtsSes15MinutesTceReporting"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpDtsCvDayTceReporting"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpDtsEsDayTceReporting"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpDtsSesDayTceReporting"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpPrbsGenerationMode"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpPrbsMonitoringMode"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpTEEnabled"),
        ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpPmHistStatsEnable"))
)
if mibBuilder.loadTexts:
    channelCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

channelCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 4, 3, 1, 1)
)
channelCtpCompliance.setObjects(
    ("INFINERA-TP-CHANNELCTP-MIB", "channelCtpGroup")
)
if mibBuilder.loadTexts:
    channelCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-CHANNELCTP-MIB",
    **{"channelCtpMIB": channelCtpMIB,
       "channelCtpTable": channelCtpTable,
       "channelCtpEntry": channelCtpEntry,
       "channelCtpPreFecThresholdOrder": channelCtpPreFecThresholdOrder,
       "channelCtpPreFecThresholdMantissa": channelCtpPreFecThresholdMantissa,
       "channelCtpSignalDegradeReporting": channelCtpSignalDegradeReporting,
       "channelCtpInsertDtsTti": channelCtpInsertDtsTti,
       "channelCtpDtsTtiAlarmReporting": channelCtpDtsTtiAlarmReporting,
       "channelCtpTxDtsTti": channelCtpTxDtsTti,
       "channelCtpExpectedDtsTti": channelCtpExpectedDtsTti,
       "channelCtpRxDtsTti": channelCtpRxDtsTti,
       "channelCtpDtsCv15MinutesTce": channelCtpDtsCv15MinutesTce,
       "channelCtpDtsEs15MinutesTce": channelCtpDtsEs15MinutesTce,
       "channelCtpDtsSes15MinutesTce": channelCtpDtsSes15MinutesTce,
       "channelCtpDtsCvDayTce": channelCtpDtsCvDayTce,
       "channelCtpDtsEsDayTce": channelCtpDtsEsDayTce,
       "channelCtpDtsSesDayTce": channelCtpDtsSesDayTce,
       "channelCtpDtsCv15MinutesTceReporting": channelCtpDtsCv15MinutesTceReporting,
       "channelCtpDtsEs15MinutesTceReporting": channelCtpDtsEs15MinutesTceReporting,
       "channelCtpDtsSes15MinutesTceReporting": channelCtpDtsSes15MinutesTceReporting,
       "channelCtpDtsCvDayTceReporting": channelCtpDtsCvDayTceReporting,
       "channelCtpDtsEsDayTceReporting": channelCtpDtsEsDayTceReporting,
       "channelCtpDtsSesDayTceReporting": channelCtpDtsSesDayTceReporting,
       "channelCtpPrbsGenerationMode": channelCtpPrbsGenerationMode,
       "channelCtpPrbsMonitoringMode": channelCtpPrbsMonitoringMode,
       "channelCtpTEEnabled": channelCtpTEEnabled,
       "channelCtpPmHistStatsEnable": channelCtpPmHistStatsEnable,
       "channelCtpConformance": channelCtpConformance,
       "channelCtpCompliances": channelCtpCompliances,
       "channelCtpCompliance": channelCtpCompliance,
       "channelCtpGroups": channelCtpGroups,
       "channelCtpGroup": channelCtpGroup}
)
