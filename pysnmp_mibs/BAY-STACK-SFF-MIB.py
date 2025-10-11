# SNMP MIB module (BAY-STACK-SFF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/BAY-STACK-SFF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:20:11 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackDdiSfpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 29)
)
if mibBuilder.loadTexts:
    bayStackDdiSfpMib.setRevisions(
        ("2012-06-05 00:00",
         "2008-06-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsDdiSfpNotifications_ObjectIdentity = ObjectIdentity
bsDdiSfpNotifications = _BsDdiSfpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 0)
)
_BsDdiSfpObjects_ObjectIdentity = ObjectIdentity
bsDdiSfpObjects = _BsDdiSfpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1)
)
_BsDdiSfpTable_Object = MibTable
bsDdiSfpTable = _BsDdiSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2)
)
if mibBuilder.loadTexts:
    bsDdiSfpTable.setStatus("current")
_BsDdiSfpEntry_Object = MibTableRow
bsDdiSfpEntry = _BsDdiSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1)
)
bsDdiSfpEntry.setIndexNames(
    (0, "BAY-STACK-SFF-MIB", "bsDdiSfpIfIndex"),
)
if mibBuilder.loadTexts:
    bsDdiSfpEntry.setStatus("current")
_BsDdiSfpIfIndex_Type = InterfaceIndex
_BsDdiSfpIfIndex_Object = MibTableColumn
bsDdiSfpIfIndex = _BsDdiSfpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 1),
    _BsDdiSfpIfIndex_Type()
)
bsDdiSfpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsDdiSfpIfIndex.setStatus("current")


class _BsDdiSfpCalibration_Type(Integer32):
    """Custom type bsDdiSfpCalibration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_BsDdiSfpCalibration_Type.__name__ = "Integer32"
_BsDdiSfpCalibration_Object = MibTableColumn
bsDdiSfpCalibration = _BsDdiSfpCalibration_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 2),
    _BsDdiSfpCalibration_Type()
)
bsDdiSfpCalibration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpCalibration.setStatus("current")


class _BsDdiSfpRxPowerMeasurement_Type(Integer32):
    """Custom type bsDdiSfpRxPowerMeasurement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oma", 1),
          ("averagePower", 2))
    )


_BsDdiSfpRxPowerMeasurement_Type.__name__ = "Integer32"
_BsDdiSfpRxPowerMeasurement_Object = MibTableColumn
bsDdiSfpRxPowerMeasurement = _BsDdiSfpRxPowerMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 3),
    _BsDdiSfpRxPowerMeasurement_Type()
)
bsDdiSfpRxPowerMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpRxPowerMeasurement.setStatus("current")


class _BsDdiSfpTempValue_Type(Integer32):
    """Custom type bsDdiSfpTempValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1280000, 1280000),
    )


_BsDdiSfpTempValue_Type.__name__ = "Integer32"
_BsDdiSfpTempValue_Object = MibTableColumn
bsDdiSfpTempValue = _BsDdiSfpTempValue_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 4),
    _BsDdiSfpTempValue_Type()
)
bsDdiSfpTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpTempValue.setStatus("current")


class _BsDdiSfpTempLowAlarmThreshold_Type(Integer32):
    """Custom type bsDdiSfpTempLowAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1280000, 1280000),
    )


_BsDdiSfpTempLowAlarmThreshold_Type.__name__ = "Integer32"
_BsDdiSfpTempLowAlarmThreshold_Object = MibTableColumn
bsDdiSfpTempLowAlarmThreshold = _BsDdiSfpTempLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 5),
    _BsDdiSfpTempLowAlarmThreshold_Type()
)
bsDdiSfpTempLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpTempLowAlarmThreshold.setStatus("current")


class _BsDdiSfpTempLowWarnThreshold_Type(Integer32):
    """Custom type bsDdiSfpTempLowWarnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1280000, 1280000),
    )


_BsDdiSfpTempLowWarnThreshold_Type.__name__ = "Integer32"
_BsDdiSfpTempLowWarnThreshold_Object = MibTableColumn
bsDdiSfpTempLowWarnThreshold = _BsDdiSfpTempLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 6),
    _BsDdiSfpTempLowWarnThreshold_Type()
)
bsDdiSfpTempLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpTempLowWarnThreshold.setStatus("current")


class _BsDdiSfpTempHighAlarmThreshold_Type(Integer32):
    """Custom type bsDdiSfpTempHighAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1280000, 1280000),
    )


_BsDdiSfpTempHighAlarmThreshold_Type.__name__ = "Integer32"
_BsDdiSfpTempHighAlarmThreshold_Object = MibTableColumn
bsDdiSfpTempHighAlarmThreshold = _BsDdiSfpTempHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 7),
    _BsDdiSfpTempHighAlarmThreshold_Type()
)
bsDdiSfpTempHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpTempHighAlarmThreshold.setStatus("current")


class _BsDdiSfpTempHighWarnThreshold_Type(Integer32):
    """Custom type bsDdiSfpTempHighWarnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1280000, 1280000),
    )


_BsDdiSfpTempHighWarnThreshold_Type.__name__ = "Integer32"
_BsDdiSfpTempHighWarnThreshold_Object = MibTableColumn
bsDdiSfpTempHighWarnThreshold = _BsDdiSfpTempHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 8),
    _BsDdiSfpTempHighWarnThreshold_Type()
)
bsDdiSfpTempHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpTempHighWarnThreshold.setStatus("current")


class _BsDdiSfpVoltageValue_Type(Integer32):
    """Custom type bsDdiSfpVoltageValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_BsDdiSfpVoltageValue_Type.__name__ = "Integer32"
_BsDdiSfpVoltageValue_Object = MibTableColumn
bsDdiSfpVoltageValue = _BsDdiSfpVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 9),
    _BsDdiSfpVoltageValue_Type()
)
bsDdiSfpVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpVoltageValue.setStatus("current")


class _BsDdiSfpVoltageLowAlarmThreshold_Type(Integer32):
    """Custom type bsDdiSfpVoltageLowAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_BsDdiSfpVoltageLowAlarmThreshold_Type.__name__ = "Integer32"
_BsDdiSfpVoltageLowAlarmThreshold_Object = MibTableColumn
bsDdiSfpVoltageLowAlarmThreshold = _BsDdiSfpVoltageLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 10),
    _BsDdiSfpVoltageLowAlarmThreshold_Type()
)
bsDdiSfpVoltageLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpVoltageLowAlarmThreshold.setStatus("current")


class _BsDdiSfpVoltageLowWarnThreshold_Type(Integer32):
    """Custom type bsDdiSfpVoltageLowWarnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_BsDdiSfpVoltageLowWarnThreshold_Type.__name__ = "Integer32"
_BsDdiSfpVoltageLowWarnThreshold_Object = MibTableColumn
bsDdiSfpVoltageLowWarnThreshold = _BsDdiSfpVoltageLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 11),
    _BsDdiSfpVoltageLowWarnThreshold_Type()
)
bsDdiSfpVoltageLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpVoltageLowWarnThreshold.setStatus("current")


class _BsDdiSfpVoltageHighAlarmThreshold_Type(Integer32):
    """Custom type bsDdiSfpVoltageHighAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_BsDdiSfpVoltageHighAlarmThreshold_Type.__name__ = "Integer32"
_BsDdiSfpVoltageHighAlarmThreshold_Object = MibTableColumn
bsDdiSfpVoltageHighAlarmThreshold = _BsDdiSfpVoltageHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 12),
    _BsDdiSfpVoltageHighAlarmThreshold_Type()
)
bsDdiSfpVoltageHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpVoltageHighAlarmThreshold.setStatus("current")


class _BsDdiSfpVoltageHighWarnThreshold_Type(Integer32):
    """Custom type bsDdiSfpVoltageHighWarnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_BsDdiSfpVoltageHighWarnThreshold_Type.__name__ = "Integer32"
_BsDdiSfpVoltageHighWarnThreshold_Object = MibTableColumn
bsDdiSfpVoltageHighWarnThreshold = _BsDdiSfpVoltageHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 13),
    _BsDdiSfpVoltageHighWarnThreshold_Type()
)
bsDdiSfpVoltageHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpVoltageHighWarnThreshold.setStatus("current")


class _BsDdiSfpBiasValue_Type(Integer32):
    """Custom type bsDdiSfpBiasValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1280000),
    )


_BsDdiSfpBiasValue_Type.__name__ = "Integer32"
_BsDdiSfpBiasValue_Object = MibTableColumn
bsDdiSfpBiasValue = _BsDdiSfpBiasValue_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 14),
    _BsDdiSfpBiasValue_Type()
)
bsDdiSfpBiasValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpBiasValue.setStatus("current")


class _BsDdiSfpBiasLowAlarmThreshold_Type(Integer32):
    """Custom type bsDdiSfpBiasLowAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1280000),
    )


_BsDdiSfpBiasLowAlarmThreshold_Type.__name__ = "Integer32"
_BsDdiSfpBiasLowAlarmThreshold_Object = MibTableColumn
bsDdiSfpBiasLowAlarmThreshold = _BsDdiSfpBiasLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 15),
    _BsDdiSfpBiasLowAlarmThreshold_Type()
)
bsDdiSfpBiasLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpBiasLowAlarmThreshold.setStatus("current")


class _BsDdiSfpBiasLowWarnThreshold_Type(Integer32):
    """Custom type bsDdiSfpBiasLowWarnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1280000),
    )


_BsDdiSfpBiasLowWarnThreshold_Type.__name__ = "Integer32"
_BsDdiSfpBiasLowWarnThreshold_Object = MibTableColumn
bsDdiSfpBiasLowWarnThreshold = _BsDdiSfpBiasLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 16),
    _BsDdiSfpBiasLowWarnThreshold_Type()
)
bsDdiSfpBiasLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpBiasLowWarnThreshold.setStatus("current")


class _BsDdiSfpBiasHighAlarmThreshold_Type(Integer32):
    """Custom type bsDdiSfpBiasHighAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1280000),
    )


_BsDdiSfpBiasHighAlarmThreshold_Type.__name__ = "Integer32"
_BsDdiSfpBiasHighAlarmThreshold_Object = MibTableColumn
bsDdiSfpBiasHighAlarmThreshold = _BsDdiSfpBiasHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 17),
    _BsDdiSfpBiasHighAlarmThreshold_Type()
)
bsDdiSfpBiasHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpBiasHighAlarmThreshold.setStatus("current")


class _BsDdiSfpBiasHighWarnThreshold_Type(Integer32):
    """Custom type bsDdiSfpBiasHighWarnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1280000),
    )


_BsDdiSfpBiasHighWarnThreshold_Type.__name__ = "Integer32"
_BsDdiSfpBiasHighWarnThreshold_Object = MibTableColumn
bsDdiSfpBiasHighWarnThreshold = _BsDdiSfpBiasHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 18),
    _BsDdiSfpBiasHighWarnThreshold_Type()
)
bsDdiSfpBiasHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpBiasHighWarnThreshold.setStatus("current")


class _BsDdiSfpTxPowerValue_Type(Integer32):
    """Custom type bsDdiSfpTxPowerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400000, 83000),
    )


_BsDdiSfpTxPowerValue_Type.__name__ = "Integer32"
_BsDdiSfpTxPowerValue_Object = MibTableColumn
bsDdiSfpTxPowerValue = _BsDdiSfpTxPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 19),
    _BsDdiSfpTxPowerValue_Type()
)
bsDdiSfpTxPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpTxPowerValue.setStatus("current")


class _BsDdiSfpTxPowerLowAlarmThreshold_Type(Integer32):
    """Custom type bsDdiSfpTxPowerLowAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400000, 83000),
    )


_BsDdiSfpTxPowerLowAlarmThreshold_Type.__name__ = "Integer32"
_BsDdiSfpTxPowerLowAlarmThreshold_Object = MibTableColumn
bsDdiSfpTxPowerLowAlarmThreshold = _BsDdiSfpTxPowerLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 20),
    _BsDdiSfpTxPowerLowAlarmThreshold_Type()
)
bsDdiSfpTxPowerLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpTxPowerLowAlarmThreshold.setStatus("current")


class _BsDdiSfpTxPowerLowWarnThreshold_Type(Integer32):
    """Custom type bsDdiSfpTxPowerLowWarnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400000, 83000),
    )


_BsDdiSfpTxPowerLowWarnThreshold_Type.__name__ = "Integer32"
_BsDdiSfpTxPowerLowWarnThreshold_Object = MibTableColumn
bsDdiSfpTxPowerLowWarnThreshold = _BsDdiSfpTxPowerLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 21),
    _BsDdiSfpTxPowerLowWarnThreshold_Type()
)
bsDdiSfpTxPowerLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpTxPowerLowWarnThreshold.setStatus("current")


class _BsDdiSfpTxPowerHighAlarmThreshold_Type(Integer32):
    """Custom type bsDdiSfpTxPowerHighAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400000, 83000),
    )


_BsDdiSfpTxPowerHighAlarmThreshold_Type.__name__ = "Integer32"
_BsDdiSfpTxPowerHighAlarmThreshold_Object = MibTableColumn
bsDdiSfpTxPowerHighAlarmThreshold = _BsDdiSfpTxPowerHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 22),
    _BsDdiSfpTxPowerHighAlarmThreshold_Type()
)
bsDdiSfpTxPowerHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpTxPowerHighAlarmThreshold.setStatus("current")


class _BsDdiSfpTxPowerHighWarnThreshold_Type(Integer32):
    """Custom type bsDdiSfpTxPowerHighWarnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400000, 83000),
    )


_BsDdiSfpTxPowerHighWarnThreshold_Type.__name__ = "Integer32"
_BsDdiSfpTxPowerHighWarnThreshold_Object = MibTableColumn
bsDdiSfpTxPowerHighWarnThreshold = _BsDdiSfpTxPowerHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 23),
    _BsDdiSfpTxPowerHighWarnThreshold_Type()
)
bsDdiSfpTxPowerHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpTxPowerHighWarnThreshold.setStatus("current")


class _BsDdiSfpRxPowerValue_Type(Integer32):
    """Custom type bsDdiSfpRxPowerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400000, 83000),
    )


_BsDdiSfpRxPowerValue_Type.__name__ = "Integer32"
_BsDdiSfpRxPowerValue_Object = MibTableColumn
bsDdiSfpRxPowerValue = _BsDdiSfpRxPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 24),
    _BsDdiSfpRxPowerValue_Type()
)
bsDdiSfpRxPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpRxPowerValue.setStatus("current")


class _BsDdiSfpRxPowerLowAlarmThreshold_Type(Integer32):
    """Custom type bsDdiSfpRxPowerLowAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400000, 83000),
    )


_BsDdiSfpRxPowerLowAlarmThreshold_Type.__name__ = "Integer32"
_BsDdiSfpRxPowerLowAlarmThreshold_Object = MibTableColumn
bsDdiSfpRxPowerLowAlarmThreshold = _BsDdiSfpRxPowerLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 25),
    _BsDdiSfpRxPowerLowAlarmThreshold_Type()
)
bsDdiSfpRxPowerLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpRxPowerLowAlarmThreshold.setStatus("current")


class _BsDdiSfpRxPowerLowWarnThreshold_Type(Integer32):
    """Custom type bsDdiSfpRxPowerLowWarnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400000, 83000),
    )


_BsDdiSfpRxPowerLowWarnThreshold_Type.__name__ = "Integer32"
_BsDdiSfpRxPowerLowWarnThreshold_Object = MibTableColumn
bsDdiSfpRxPowerLowWarnThreshold = _BsDdiSfpRxPowerLowWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 26),
    _BsDdiSfpRxPowerLowWarnThreshold_Type()
)
bsDdiSfpRxPowerLowWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpRxPowerLowWarnThreshold.setStatus("current")


class _BsDdiSfpRxPowerHighAlarmThreshold_Type(Integer32):
    """Custom type bsDdiSfpRxPowerHighAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400000, 83000),
    )


_BsDdiSfpRxPowerHighAlarmThreshold_Type.__name__ = "Integer32"
_BsDdiSfpRxPowerHighAlarmThreshold_Object = MibTableColumn
bsDdiSfpRxPowerHighAlarmThreshold = _BsDdiSfpRxPowerHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 27),
    _BsDdiSfpRxPowerHighAlarmThreshold_Type()
)
bsDdiSfpRxPowerHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpRxPowerHighAlarmThreshold.setStatus("current")


class _BsDdiSfpRxPowerHighWarnThreshold_Type(Integer32):
    """Custom type bsDdiSfpRxPowerHighWarnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400000, 83000),
    )


_BsDdiSfpRxPowerHighWarnThreshold_Type.__name__ = "Integer32"
_BsDdiSfpRxPowerHighWarnThreshold_Object = MibTableColumn
bsDdiSfpRxPowerHighWarnThreshold = _BsDdiSfpRxPowerHighWarnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 1, 2, 1, 28),
    _BsDdiSfpRxPowerHighWarnThreshold_Type()
)
bsDdiSfpRxPowerHighWarnThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsDdiSfpRxPowerHighWarnThreshold.setStatus("current")

# Managed Objects groups


# Notification objects

bsDdiSfpTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 0, 1)
)
bsDdiSfpTempAlarm.setObjects(
    ("BAY-STACK-SFF-MIB", "bsDdiSfpTempValue")
)
if mibBuilder.loadTexts:
    bsDdiSfpTempAlarm.setStatus(
        "current"
    )

bsDdiSfpTempWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 0, 2)
)
bsDdiSfpTempWarn.setObjects(
    ("BAY-STACK-SFF-MIB", "bsDdiSfpTempValue")
)
if mibBuilder.loadTexts:
    bsDdiSfpTempWarn.setStatus(
        "current"
    )

bsDdiSfpTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 0, 3)
)
bsDdiSfpTempNormal.setObjects(
    ("BAY-STACK-SFF-MIB", "bsDdiSfpTempValue")
)
if mibBuilder.loadTexts:
    bsDdiSfpTempNormal.setStatus(
        "current"
    )

bsDdiSfpVoltageAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 0, 4)
)
bsDdiSfpVoltageAlarm.setObjects(
    ("BAY-STACK-SFF-MIB", "bsDdiSfpVoltageValue")
)
if mibBuilder.loadTexts:
    bsDdiSfpVoltageAlarm.setStatus(
        "current"
    )

bsDdiSfpVoltageWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 0, 5)
)
bsDdiSfpVoltageWarn.setObjects(
    ("BAY-STACK-SFF-MIB", "bsDdiSfpVoltageValue")
)
if mibBuilder.loadTexts:
    bsDdiSfpVoltageWarn.setStatus(
        "current"
    )

bsDdiSfpVoltageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 0, 6)
)
bsDdiSfpVoltageNormal.setObjects(
    ("BAY-STACK-SFF-MIB", "bsDdiSfpVoltageValue")
)
if mibBuilder.loadTexts:
    bsDdiSfpVoltageNormal.setStatus(
        "current"
    )

bsDdiSfpBiasAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 0, 7)
)
bsDdiSfpBiasAlarm.setObjects(
    ("BAY-STACK-SFF-MIB", "bsDdiSfpBiasValue")
)
if mibBuilder.loadTexts:
    bsDdiSfpBiasAlarm.setStatus(
        "current"
    )

bsDdiSfpBiasWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 0, 8)
)
bsDdiSfpBiasWarn.setObjects(
    ("BAY-STACK-SFF-MIB", "bsDdiSfpBiasValue")
)
if mibBuilder.loadTexts:
    bsDdiSfpBiasWarn.setStatus(
        "current"
    )

bsDdiSfpBiasNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 0, 9)
)
bsDdiSfpBiasNormal.setObjects(
    ("BAY-STACK-SFF-MIB", "bsDdiSfpBiasValue")
)
if mibBuilder.loadTexts:
    bsDdiSfpBiasNormal.setStatus(
        "current"
    )

bsDdiSfpTxAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 0, 10)
)
bsDdiSfpTxAlarm.setObjects(
    ("BAY-STACK-SFF-MIB", "bsDdiSfpTxPowerValue")
)
if mibBuilder.loadTexts:
    bsDdiSfpTxAlarm.setStatus(
        "current"
    )

bsDdiSfpTxWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 0, 11)
)
bsDdiSfpTxWarn.setObjects(
    ("BAY-STACK-SFF-MIB", "bsDdiSfpTxPowerValue")
)
if mibBuilder.loadTexts:
    bsDdiSfpTxWarn.setStatus(
        "current"
    )

bsDdiSfpTxNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 0, 12)
)
bsDdiSfpTxNormal.setObjects(
    ("BAY-STACK-SFF-MIB", "bsDdiSfpTxPowerValue")
)
if mibBuilder.loadTexts:
    bsDdiSfpTxNormal.setStatus(
        "current"
    )

bsDdiSfpRxAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 0, 13)
)
bsDdiSfpRxAlarm.setObjects(
    ("BAY-STACK-SFF-MIB", "bsDdiSfpRxPowerValue")
)
if mibBuilder.loadTexts:
    bsDdiSfpRxAlarm.setStatus(
        "current"
    )

bsDdiSfpRxWarn = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 0, 14)
)
bsDdiSfpRxWarn.setObjects(
    ("BAY-STACK-SFF-MIB", "bsDdiSfpRxPowerValue")
)
if mibBuilder.loadTexts:
    bsDdiSfpRxWarn.setStatus(
        "current"
    )

bsDdiSfpRxNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 29, 0, 15)
)
bsDdiSfpRxNormal.setObjects(
    ("BAY-STACK-SFF-MIB", "bsDdiSfpRxPowerValue")
)
if mibBuilder.loadTexts:
    bsDdiSfpRxNormal.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-SFF-MIB",
    **{"bayStackDdiSfpMib": bayStackDdiSfpMib,
       "bsDdiSfpNotifications": bsDdiSfpNotifications,
       "bsDdiSfpTempAlarm": bsDdiSfpTempAlarm,
       "bsDdiSfpTempWarn": bsDdiSfpTempWarn,
       "bsDdiSfpTempNormal": bsDdiSfpTempNormal,
       "bsDdiSfpVoltageAlarm": bsDdiSfpVoltageAlarm,
       "bsDdiSfpVoltageWarn": bsDdiSfpVoltageWarn,
       "bsDdiSfpVoltageNormal": bsDdiSfpVoltageNormal,
       "bsDdiSfpBiasAlarm": bsDdiSfpBiasAlarm,
       "bsDdiSfpBiasWarn": bsDdiSfpBiasWarn,
       "bsDdiSfpBiasNormal": bsDdiSfpBiasNormal,
       "bsDdiSfpTxAlarm": bsDdiSfpTxAlarm,
       "bsDdiSfpTxWarn": bsDdiSfpTxWarn,
       "bsDdiSfpTxNormal": bsDdiSfpTxNormal,
       "bsDdiSfpRxAlarm": bsDdiSfpRxAlarm,
       "bsDdiSfpRxWarn": bsDdiSfpRxWarn,
       "bsDdiSfpRxNormal": bsDdiSfpRxNormal,
       "bsDdiSfpObjects": bsDdiSfpObjects,
       "bsDdiSfpTable": bsDdiSfpTable,
       "bsDdiSfpEntry": bsDdiSfpEntry,
       "bsDdiSfpIfIndex": bsDdiSfpIfIndex,
       "bsDdiSfpCalibration": bsDdiSfpCalibration,
       "bsDdiSfpRxPowerMeasurement": bsDdiSfpRxPowerMeasurement,
       "bsDdiSfpTempValue": bsDdiSfpTempValue,
       "bsDdiSfpTempLowAlarmThreshold": bsDdiSfpTempLowAlarmThreshold,
       "bsDdiSfpTempLowWarnThreshold": bsDdiSfpTempLowWarnThreshold,
       "bsDdiSfpTempHighAlarmThreshold": bsDdiSfpTempHighAlarmThreshold,
       "bsDdiSfpTempHighWarnThreshold": bsDdiSfpTempHighWarnThreshold,
       "bsDdiSfpVoltageValue": bsDdiSfpVoltageValue,
       "bsDdiSfpVoltageLowAlarmThreshold": bsDdiSfpVoltageLowAlarmThreshold,
       "bsDdiSfpVoltageLowWarnThreshold": bsDdiSfpVoltageLowWarnThreshold,
       "bsDdiSfpVoltageHighAlarmThreshold": bsDdiSfpVoltageHighAlarmThreshold,
       "bsDdiSfpVoltageHighWarnThreshold": bsDdiSfpVoltageHighWarnThreshold,
       "bsDdiSfpBiasValue": bsDdiSfpBiasValue,
       "bsDdiSfpBiasLowAlarmThreshold": bsDdiSfpBiasLowAlarmThreshold,
       "bsDdiSfpBiasLowWarnThreshold": bsDdiSfpBiasLowWarnThreshold,
       "bsDdiSfpBiasHighAlarmThreshold": bsDdiSfpBiasHighAlarmThreshold,
       "bsDdiSfpBiasHighWarnThreshold": bsDdiSfpBiasHighWarnThreshold,
       "bsDdiSfpTxPowerValue": bsDdiSfpTxPowerValue,
       "bsDdiSfpTxPowerLowAlarmThreshold": bsDdiSfpTxPowerLowAlarmThreshold,
       "bsDdiSfpTxPowerLowWarnThreshold": bsDdiSfpTxPowerLowWarnThreshold,
       "bsDdiSfpTxPowerHighAlarmThreshold": bsDdiSfpTxPowerHighAlarmThreshold,
       "bsDdiSfpTxPowerHighWarnThreshold": bsDdiSfpTxPowerHighWarnThreshold,
       "bsDdiSfpRxPowerValue": bsDdiSfpRxPowerValue,
       "bsDdiSfpRxPowerLowAlarmThreshold": bsDdiSfpRxPowerLowAlarmThreshold,
       "bsDdiSfpRxPowerLowWarnThreshold": bsDdiSfpRxPowerLowWarnThreshold,
       "bsDdiSfpRxPowerHighAlarmThreshold": bsDdiSfpRxPowerHighAlarmThreshold,
       "bsDdiSfpRxPowerHighWarnThreshold": bsDdiSfpRxPowerHighWarnThreshold}
)
