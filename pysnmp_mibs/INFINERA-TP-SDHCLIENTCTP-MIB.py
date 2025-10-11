# SNMP MIB module (INFINERA-TP-SDHCLIENTCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-SDHCLIENTCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:25 2025
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

(InfnClientAction,
 InfnEnableDisable,
 InfnJ0MessageCompliance,
 InfnJ0TraceMode,
 InfnLoopbackType,
 InfnPmHistStatsControl,
 InfnSMQ,
 InfnServiceMode,
 InfnServiceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnClientAction",
    "InfnEnableDisable",
    "InfnJ0MessageCompliance",
    "InfnJ0TraceMode",
    "InfnLoopbackType",
    "InfnPmHistStatsControl",
    "InfnSMQ",
    "InfnServiceMode",
    "InfnServiceType")

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

sdhClientCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15)
)
if mibBuilder.loadTexts:
    sdhClientCtpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SdhClientCtpTable_Object = MibTable
sdhClientCtpTable = _SdhClientCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1)
)
if mibBuilder.loadTexts:
    sdhClientCtpTable.setStatus("current")
_SdhClientCtpEntry_Object = MibTableRow
sdhClientCtpEntry = _SdhClientCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1)
)
sdhClientCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sdhClientCtpEntry.setStatus("current")


class _SdhClientCtpTribPrbsGenMode_Type(InfnEnableDisable):
    """Custom type sdhClientCtpTribPrbsGenMode based on InfnEnableDisable"""
    defaultValue = 1


_SdhClientCtpTribPrbsGenMode_Type.__name__ = "InfnEnableDisable"
_SdhClientCtpTribPrbsGenMode_Object = MibTableColumn
sdhClientCtpTribPrbsGenMode = _SdhClientCtpTribPrbsGenMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 1),
    _SdhClientCtpTribPrbsGenMode_Type()
)
sdhClientCtpTribPrbsGenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTribPrbsGenMode.setStatus("current")


class _SdhClientCtpTribPrbsMonMode_Type(InfnEnableDisable):
    """Custom type sdhClientCtpTribPrbsMonMode based on InfnEnableDisable"""
    defaultValue = 1


_SdhClientCtpTribPrbsMonMode_Type.__name__ = "InfnEnableDisable"
_SdhClientCtpTribPrbsMonMode_Object = MibTableColumn
sdhClientCtpTribPrbsMonMode = _SdhClientCtpTribPrbsMonMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 2),
    _SdhClientCtpTribPrbsMonMode_Type()
)
sdhClientCtpTribPrbsMonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTribPrbsMonMode.setStatus("current")
_SdhClientCtpSupportingCircuitIdList_Type = DisplayString
_SdhClientCtpSupportingCircuitIdList_Object = MibTableColumn
sdhClientCtpSupportingCircuitIdList = _SdhClientCtpSupportingCircuitIdList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 3),
    _SdhClientCtpSupportingCircuitIdList_Type()
)
sdhClientCtpSupportingCircuitIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpSupportingCircuitIdList.setStatus("current")


class _SdhClientCtpLoopback_Type(InfnLoopbackType):
    """Custom type sdhClientCtpLoopback based on InfnLoopbackType"""
    defaultValue = 1


_SdhClientCtpLoopback_Type.__name__ = "InfnLoopbackType"
_SdhClientCtpLoopback_Object = MibTableColumn
sdhClientCtpLoopback = _SdhClientCtpLoopback_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 4),
    _SdhClientCtpLoopback_Type()
)
sdhClientCtpLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpLoopback.setStatus("current")


class _SdhClientCtpPmHistStatsEnable_Type(InfnPmHistStatsControl):
    """Custom type sdhClientCtpPmHistStatsEnable based on InfnPmHistStatsControl"""
    defaultValue = 1


_SdhClientCtpPmHistStatsEnable_Type.__name__ = "InfnPmHistStatsControl"
_SdhClientCtpPmHistStatsEnable_Object = MibTableColumn
sdhClientCtpPmHistStatsEnable = _SdhClientCtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 5),
    _SdhClientCtpPmHistStatsEnable_Type()
)
sdhClientCtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpPmHistStatsEnable.setStatus("current")
_SdhClientCtpConfiguredServiceType_Type = InfnServiceType
_SdhClientCtpConfiguredServiceType_Object = MibTableColumn
sdhClientCtpConfiguredServiceType = _SdhClientCtpConfiguredServiceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 6),
    _SdhClientCtpConfiguredServiceType_Type()
)
sdhClientCtpConfiguredServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpConfiguredServiceType.setStatus("current")
_SdhClientCtpRxJ0_Type = DisplayString
_SdhClientCtpRxJ0_Object = MibTableColumn
sdhClientCtpRxJ0 = _SdhClientCtpRxJ0_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 7),
    _SdhClientCtpRxJ0_Type()
)
sdhClientCtpRxJ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpRxJ0.setStatus("current")
_SdhClientCtpExpectedRxJ0_Type = DisplayString
_SdhClientCtpExpectedRxJ0_Object = MibTableColumn
sdhClientCtpExpectedRxJ0 = _SdhClientCtpExpectedRxJ0_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 8),
    _SdhClientCtpExpectedRxJ0_Type()
)
sdhClientCtpExpectedRxJ0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpExpectedRxJ0.setStatus("current")
_SdhClientCtpTransmittedJ0_Type = DisplayString
_SdhClientCtpTransmittedJ0_Object = MibTableColumn
sdhClientCtpTransmittedJ0 = _SdhClientCtpTransmittedJ0_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 9),
    _SdhClientCtpTransmittedJ0_Type()
)
sdhClientCtpTransmittedJ0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTransmittedJ0.setStatus("current")


class _SdhClientCtpRxJ0MessageLength_Type(Integer32):
    """Custom type sdhClientCtpRxJ0MessageLength based on Integer32"""
    defaultValue = 16


_SdhClientCtpRxJ0MessageLength_Type.__name__ = "Integer32"
_SdhClientCtpRxJ0MessageLength_Object = MibTableColumn
sdhClientCtpRxJ0MessageLength = _SdhClientCtpRxJ0MessageLength_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 10),
    _SdhClientCtpRxJ0MessageLength_Type()
)
sdhClientCtpRxJ0MessageLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxJ0MessageLength.setStatus("current")


class _SdhClientCtpRxJ0MismatchReporting_Type(InfnEnableDisable):
    """Custom type sdhClientCtpRxJ0MismatchReporting based on InfnEnableDisable"""
    defaultValue = 1


_SdhClientCtpRxJ0MismatchReporting_Type.__name__ = "InfnEnableDisable"
_SdhClientCtpRxJ0MismatchReporting_Object = MibTableColumn
sdhClientCtpRxJ0MismatchReporting = _SdhClientCtpRxJ0MismatchReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 11),
    _SdhClientCtpRxJ0MismatchReporting_Type()
)
sdhClientCtpRxJ0MismatchReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxJ0MismatchReporting.setStatus("current")


class _SdhClientCtpRxJ0TraceMode_Type(InfnJ0TraceMode):
    """Custom type sdhClientCtpRxJ0TraceMode based on InfnJ0TraceMode"""
    defaultValue = 1


_SdhClientCtpRxJ0TraceMode_Type.__name__ = "InfnJ0TraceMode"
_SdhClientCtpRxJ0TraceMode_Object = MibTableColumn
sdhClientCtpRxJ0TraceMode = _SdhClientCtpRxJ0TraceMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 12),
    _SdhClientCtpRxJ0TraceMode_Type()
)
sdhClientCtpRxJ0TraceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxJ0TraceMode.setStatus("current")


class _SdhClientCtpRxJ0MessageCompliance_Type(InfnJ0MessageCompliance):
    """Custom type sdhClientCtpRxJ0MessageCompliance based on InfnJ0MessageCompliance"""
    defaultValue = 2


_SdhClientCtpRxJ0MessageCompliance_Type.__name__ = "InfnJ0MessageCompliance"
_SdhClientCtpRxJ0MessageCompliance_Object = MibTableColumn
sdhClientCtpRxJ0MessageCompliance = _SdhClientCtpRxJ0MessageCompliance_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 13),
    _SdhClientCtpRxJ0MessageCompliance_Type()
)
sdhClientCtpRxJ0MessageCompliance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxJ0MessageCompliance.setStatus("current")
_SdhClientCtpRxBe15MinutesTce_Type = Counter64
_SdhClientCtpRxBe15MinutesTce_Object = MibTableColumn
sdhClientCtpRxBe15MinutesTce = _SdhClientCtpRxBe15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 14),
    _SdhClientCtpRxBe15MinutesTce_Type()
)
sdhClientCtpRxBe15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxBe15MinutesTce.setStatus("current")


class _SdhClientCtpRxEs15MinutesTce_Type(Integer32):
    """Custom type sdhClientCtpRxEs15MinutesTce based on Integer32"""
    defaultValue = 120


_SdhClientCtpRxEs15MinutesTce_Type.__name__ = "Integer32"
_SdhClientCtpRxEs15MinutesTce_Object = MibTableColumn
sdhClientCtpRxEs15MinutesTce = _SdhClientCtpRxEs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 15),
    _SdhClientCtpRxEs15MinutesTce_Type()
)
sdhClientCtpRxEs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxEs15MinutesTce.setStatus("current")


class _SdhClientCtpRxSes15MinutesTce_Type(Integer32):
    """Custom type sdhClientCtpRxSes15MinutesTce based on Integer32"""
    defaultValue = 3


_SdhClientCtpRxSes15MinutesTce_Type.__name__ = "Integer32"
_SdhClientCtpRxSes15MinutesTce_Object = MibTableColumn
sdhClientCtpRxSes15MinutesTce = _SdhClientCtpRxSes15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 16),
    _SdhClientCtpRxSes15MinutesTce_Type()
)
sdhClientCtpRxSes15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxSes15MinutesTce.setStatus("current")


class _SdhClientCtpRxOfs15MinutesTce_Type(Integer32):
    """Custom type sdhClientCtpRxOfs15MinutesTce based on Integer32"""
    defaultValue = 3


_SdhClientCtpRxOfs15MinutesTce_Type.__name__ = "Integer32"
_SdhClientCtpRxOfs15MinutesTce_Object = MibTableColumn
sdhClientCtpRxOfs15MinutesTce = _SdhClientCtpRxOfs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 17),
    _SdhClientCtpRxOfs15MinutesTce_Type()
)
sdhClientCtpRxOfs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxOfs15MinutesTce.setStatus("current")


class _SdhClientCtpRxLoss15MinutesTce_Type(Integer32):
    """Custom type sdhClientCtpRxLoss15MinutesTce based on Integer32"""
    defaultValue = 3


_SdhClientCtpRxLoss15MinutesTce_Type.__name__ = "Integer32"
_SdhClientCtpRxLoss15MinutesTce_Object = MibTableColumn
sdhClientCtpRxLoss15MinutesTce = _SdhClientCtpRxLoss15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 18),
    _SdhClientCtpRxLoss15MinutesTce_Type()
)
sdhClientCtpRxLoss15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxLoss15MinutesTce.setStatus("current")
_SdhClientCtpRxBeDayTce_Type = Counter64
_SdhClientCtpRxBeDayTce_Object = MibTableColumn
sdhClientCtpRxBeDayTce = _SdhClientCtpRxBeDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 19),
    _SdhClientCtpRxBeDayTce_Type()
)
sdhClientCtpRxBeDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxBeDayTce.setStatus("current")


class _SdhClientCtpRxEsDayTce_Type(Integer32):
    """Custom type sdhClientCtpRxEsDayTce based on Integer32"""
    defaultValue = 1200


_SdhClientCtpRxEsDayTce_Type.__name__ = "Integer32"
_SdhClientCtpRxEsDayTce_Object = MibTableColumn
sdhClientCtpRxEsDayTce = _SdhClientCtpRxEsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 20),
    _SdhClientCtpRxEsDayTce_Type()
)
sdhClientCtpRxEsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxEsDayTce.setStatus("current")


class _SdhClientCtpRxSesDayTce_Type(Integer32):
    """Custom type sdhClientCtpRxSesDayTce based on Integer32"""
    defaultValue = 7


_SdhClientCtpRxSesDayTce_Type.__name__ = "Integer32"
_SdhClientCtpRxSesDayTce_Object = MibTableColumn
sdhClientCtpRxSesDayTce = _SdhClientCtpRxSesDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 21),
    _SdhClientCtpRxSesDayTce_Type()
)
sdhClientCtpRxSesDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxSesDayTce.setStatus("current")


class _SdhClientCtpRxOfsDayTce_Type(Integer32):
    """Custom type sdhClientCtpRxOfsDayTce based on Integer32"""
    defaultValue = 7


_SdhClientCtpRxOfsDayTce_Type.__name__ = "Integer32"
_SdhClientCtpRxOfsDayTce_Object = MibTableColumn
sdhClientCtpRxOfsDayTce = _SdhClientCtpRxOfsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 22),
    _SdhClientCtpRxOfsDayTce_Type()
)
sdhClientCtpRxOfsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxOfsDayTce.setStatus("current")


class _SdhClientCtpRxLossDayTce_Type(Integer32):
    """Custom type sdhClientCtpRxLossDayTce based on Integer32"""
    defaultValue = 3


_SdhClientCtpRxLossDayTce_Type.__name__ = "Integer32"
_SdhClientCtpRxLossDayTce_Object = MibTableColumn
sdhClientCtpRxLossDayTce = _SdhClientCtpRxLossDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 23),
    _SdhClientCtpRxLossDayTce_Type()
)
sdhClientCtpRxLossDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxLossDayTce.setStatus("current")
_SdhClientCtpTxBe15MinutesTce_Type = Counter64
_SdhClientCtpTxBe15MinutesTce_Object = MibTableColumn
sdhClientCtpTxBe15MinutesTce = _SdhClientCtpTxBe15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 24),
    _SdhClientCtpTxBe15MinutesTce_Type()
)
sdhClientCtpTxBe15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTxBe15MinutesTce.setStatus("current")


class _SdhClientCtpTxEs15MinutesTce_Type(Integer32):
    """Custom type sdhClientCtpTxEs15MinutesTce based on Integer32"""
    defaultValue = 120


_SdhClientCtpTxEs15MinutesTce_Type.__name__ = "Integer32"
_SdhClientCtpTxEs15MinutesTce_Object = MibTableColumn
sdhClientCtpTxEs15MinutesTce = _SdhClientCtpTxEs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 25),
    _SdhClientCtpTxEs15MinutesTce_Type()
)
sdhClientCtpTxEs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTxEs15MinutesTce.setStatus("current")


class _SdhClientCtpTxSes15MinutesTce_Type(Integer32):
    """Custom type sdhClientCtpTxSes15MinutesTce based on Integer32"""
    defaultValue = 3


_SdhClientCtpTxSes15MinutesTce_Type.__name__ = "Integer32"
_SdhClientCtpTxSes15MinutesTce_Object = MibTableColumn
sdhClientCtpTxSes15MinutesTce = _SdhClientCtpTxSes15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 26),
    _SdhClientCtpTxSes15MinutesTce_Type()
)
sdhClientCtpTxSes15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTxSes15MinutesTce.setStatus("current")


class _SdhClientCtpTxOfs15MinutesTce_Type(Integer32):
    """Custom type sdhClientCtpTxOfs15MinutesTce based on Integer32"""
    defaultValue = 3


_SdhClientCtpTxOfs15MinutesTce_Type.__name__ = "Integer32"
_SdhClientCtpTxOfs15MinutesTce_Object = MibTableColumn
sdhClientCtpTxOfs15MinutesTce = _SdhClientCtpTxOfs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 27),
    _SdhClientCtpTxOfs15MinutesTce_Type()
)
sdhClientCtpTxOfs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTxOfs15MinutesTce.setStatus("current")
_SdhClientCtpTxBeDayTce_Type = Counter64
_SdhClientCtpTxBeDayTce_Object = MibTableColumn
sdhClientCtpTxBeDayTce = _SdhClientCtpTxBeDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 28),
    _SdhClientCtpTxBeDayTce_Type()
)
sdhClientCtpTxBeDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTxBeDayTce.setStatus("current")


class _SdhClientCtpTxEsDayTce_Type(Integer32):
    """Custom type sdhClientCtpTxEsDayTce based on Integer32"""
    defaultValue = 1200


_SdhClientCtpTxEsDayTce_Type.__name__ = "Integer32"
_SdhClientCtpTxEsDayTce_Object = MibTableColumn
sdhClientCtpTxEsDayTce = _SdhClientCtpTxEsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 29),
    _SdhClientCtpTxEsDayTce_Type()
)
sdhClientCtpTxEsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTxEsDayTce.setStatus("current")


class _SdhClientCtpTxSesDayTce_Type(Integer32):
    """Custom type sdhClientCtpTxSesDayTce based on Integer32"""
    defaultValue = 7


_SdhClientCtpTxSesDayTce_Type.__name__ = "Integer32"
_SdhClientCtpTxSesDayTce_Object = MibTableColumn
sdhClientCtpTxSesDayTce = _SdhClientCtpTxSesDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 30),
    _SdhClientCtpTxSesDayTce_Type()
)
sdhClientCtpTxSesDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTxSesDayTce.setStatus("current")


class _SdhClientCtpTxOfsDayTce_Type(Integer32):
    """Custom type sdhClientCtpTxOfsDayTce based on Integer32"""
    defaultValue = 7


_SdhClientCtpTxOfsDayTce_Type.__name__ = "Integer32"
_SdhClientCtpTxOfsDayTce_Object = MibTableColumn
sdhClientCtpTxOfsDayTce = _SdhClientCtpTxOfsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 31),
    _SdhClientCtpTxOfsDayTce_Type()
)
sdhClientCtpTxOfsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTxOfsDayTce.setStatus("current")


class _SdhClientCtpRxBe15MinutesTceReporting_Type(TruthValue):
    """Custom type sdhClientCtpRxBe15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpRxBe15MinutesTceReporting_Type.__name__ = "TruthValue"
_SdhClientCtpRxBe15MinutesTceReporting_Object = MibTableColumn
sdhClientCtpRxBe15MinutesTceReporting = _SdhClientCtpRxBe15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 32),
    _SdhClientCtpRxBe15MinutesTceReporting_Type()
)
sdhClientCtpRxBe15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxBe15MinutesTceReporting.setStatus("current")


class _SdhClientCtpRxEs15MinutesTceReporting_Type(TruthValue):
    """Custom type sdhClientCtpRxEs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpRxEs15MinutesTceReporting_Type.__name__ = "TruthValue"
_SdhClientCtpRxEs15MinutesTceReporting_Object = MibTableColumn
sdhClientCtpRxEs15MinutesTceReporting = _SdhClientCtpRxEs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 33),
    _SdhClientCtpRxEs15MinutesTceReporting_Type()
)
sdhClientCtpRxEs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxEs15MinutesTceReporting.setStatus("current")


class _SdhClientCtpRxSes15MinutesTceReporting_Type(TruthValue):
    """Custom type sdhClientCtpRxSes15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpRxSes15MinutesTceReporting_Type.__name__ = "TruthValue"
_SdhClientCtpRxSes15MinutesTceReporting_Object = MibTableColumn
sdhClientCtpRxSes15MinutesTceReporting = _SdhClientCtpRxSes15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 34),
    _SdhClientCtpRxSes15MinutesTceReporting_Type()
)
sdhClientCtpRxSes15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxSes15MinutesTceReporting.setStatus("current")


class _SdhClientCtpRxBeDayTceReporting_Type(TruthValue):
    """Custom type sdhClientCtpRxBeDayTceReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpRxBeDayTceReporting_Type.__name__ = "TruthValue"
_SdhClientCtpRxBeDayTceReporting_Object = MibTableColumn
sdhClientCtpRxBeDayTceReporting = _SdhClientCtpRxBeDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 35),
    _SdhClientCtpRxBeDayTceReporting_Type()
)
sdhClientCtpRxBeDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxBeDayTceReporting.setStatus("current")


class _SdhClientCtpRxEsDayTceReporting_Type(TruthValue):
    """Custom type sdhClientCtpRxEsDayTceReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpRxEsDayTceReporting_Type.__name__ = "TruthValue"
_SdhClientCtpRxEsDayTceReporting_Object = MibTableColumn
sdhClientCtpRxEsDayTceReporting = _SdhClientCtpRxEsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 36),
    _SdhClientCtpRxEsDayTceReporting_Type()
)
sdhClientCtpRxEsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxEsDayTceReporting.setStatus("current")


class _SdhClientCtpRxSesDayTceReporting_Type(TruthValue):
    """Custom type sdhClientCtpRxSesDayTceReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpRxSesDayTceReporting_Type.__name__ = "TruthValue"
_SdhClientCtpRxSesDayTceReporting_Object = MibTableColumn
sdhClientCtpRxSesDayTceReporting = _SdhClientCtpRxSesDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 37),
    _SdhClientCtpRxSesDayTceReporting_Type()
)
sdhClientCtpRxSesDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxSesDayTceReporting.setStatus("current")


class _SdhClientCtpRxOfs15MinutesTceReporting_Type(TruthValue):
    """Custom type sdhClientCtpRxOfs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpRxOfs15MinutesTceReporting_Type.__name__ = "TruthValue"
_SdhClientCtpRxOfs15MinutesTceReporting_Object = MibTableColumn
sdhClientCtpRxOfs15MinutesTceReporting = _SdhClientCtpRxOfs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 38),
    _SdhClientCtpRxOfs15MinutesTceReporting_Type()
)
sdhClientCtpRxOfs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxOfs15MinutesTceReporting.setStatus("current")


class _SdhClientCtpRxOfsDayReporting_Type(TruthValue):
    """Custom type sdhClientCtpRxOfsDayReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpRxOfsDayReporting_Type.__name__ = "TruthValue"
_SdhClientCtpRxOfsDayReporting_Object = MibTableColumn
sdhClientCtpRxOfsDayReporting = _SdhClientCtpRxOfsDayReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 39),
    _SdhClientCtpRxOfsDayReporting_Type()
)
sdhClientCtpRxOfsDayReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxOfsDayReporting.setStatus("current")


class _SdhClientCtpRxLoss15MinutesTceReporting_Type(TruthValue):
    """Custom type sdhClientCtpRxLoss15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpRxLoss15MinutesTceReporting_Type.__name__ = "TruthValue"
_SdhClientCtpRxLoss15MinutesTceReporting_Object = MibTableColumn
sdhClientCtpRxLoss15MinutesTceReporting = _SdhClientCtpRxLoss15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 40),
    _SdhClientCtpRxLoss15MinutesTceReporting_Type()
)
sdhClientCtpRxLoss15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxLoss15MinutesTceReporting.setStatus("current")


class _SdhClientCtpRxLossDayReporting_Type(TruthValue):
    """Custom type sdhClientCtpRxLossDayReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpRxLossDayReporting_Type.__name__ = "TruthValue"
_SdhClientCtpRxLossDayReporting_Object = MibTableColumn
sdhClientCtpRxLossDayReporting = _SdhClientCtpRxLossDayReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 41),
    _SdhClientCtpRxLossDayReporting_Type()
)
sdhClientCtpRxLossDayReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxLossDayReporting.setStatus("current")


class _SdhClientCtpTxBe15MinutesTceReporting_Type(TruthValue):
    """Custom type sdhClientCtpTxBe15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpTxBe15MinutesTceReporting_Type.__name__ = "TruthValue"
_SdhClientCtpTxBe15MinutesTceReporting_Object = MibTableColumn
sdhClientCtpTxBe15MinutesTceReporting = _SdhClientCtpTxBe15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 42),
    _SdhClientCtpTxBe15MinutesTceReporting_Type()
)
sdhClientCtpTxBe15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTxBe15MinutesTceReporting.setStatus("current")


class _SdhClientCtpTxEs15MinutesTceReporting_Type(TruthValue):
    """Custom type sdhClientCtpTxEs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpTxEs15MinutesTceReporting_Type.__name__ = "TruthValue"
_SdhClientCtpTxEs15MinutesTceReporting_Object = MibTableColumn
sdhClientCtpTxEs15MinutesTceReporting = _SdhClientCtpTxEs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 43),
    _SdhClientCtpTxEs15MinutesTceReporting_Type()
)
sdhClientCtpTxEs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTxEs15MinutesTceReporting.setStatus("current")


class _SdhClientCtpTxSes15MinutesTceReporting_Type(TruthValue):
    """Custom type sdhClientCtpTxSes15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpTxSes15MinutesTceReporting_Type.__name__ = "TruthValue"
_SdhClientCtpTxSes15MinutesTceReporting_Object = MibTableColumn
sdhClientCtpTxSes15MinutesTceReporting = _SdhClientCtpTxSes15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 44),
    _SdhClientCtpTxSes15MinutesTceReporting_Type()
)
sdhClientCtpTxSes15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTxSes15MinutesTceReporting.setStatus("current")


class _SdhClientCtpTxBeDayTceReporting_Type(TruthValue):
    """Custom type sdhClientCtpTxBeDayTceReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpTxBeDayTceReporting_Type.__name__ = "TruthValue"
_SdhClientCtpTxBeDayTceReporting_Object = MibTableColumn
sdhClientCtpTxBeDayTceReporting = _SdhClientCtpTxBeDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 45),
    _SdhClientCtpTxBeDayTceReporting_Type()
)
sdhClientCtpTxBeDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTxBeDayTceReporting.setStatus("current")


class _SdhClientCtpTxEsDayTceReporting_Type(TruthValue):
    """Custom type sdhClientCtpTxEsDayTceReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpTxEsDayTceReporting_Type.__name__ = "TruthValue"
_SdhClientCtpTxEsDayTceReporting_Object = MibTableColumn
sdhClientCtpTxEsDayTceReporting = _SdhClientCtpTxEsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 46),
    _SdhClientCtpTxEsDayTceReporting_Type()
)
sdhClientCtpTxEsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTxEsDayTceReporting.setStatus("current")


class _SdhClientCtpTxSesDayTceReporting_Type(TruthValue):
    """Custom type sdhClientCtpTxSesDayTceReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpTxSesDayTceReporting_Type.__name__ = "TruthValue"
_SdhClientCtpTxSesDayTceReporting_Object = MibTableColumn
sdhClientCtpTxSesDayTceReporting = _SdhClientCtpTxSesDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 47),
    _SdhClientCtpTxSesDayTceReporting_Type()
)
sdhClientCtpTxSesDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTxSesDayTceReporting.setStatus("current")


class _SdhClientCtpTxOfs15MinutesTceReporting_Type(TruthValue):
    """Custom type sdhClientCtpTxOfs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpTxOfs15MinutesTceReporting_Type.__name__ = "TruthValue"
_SdhClientCtpTxOfs15MinutesTceReporting_Object = MibTableColumn
sdhClientCtpTxOfs15MinutesTceReporting = _SdhClientCtpTxOfs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 48),
    _SdhClientCtpTxOfs15MinutesTceReporting_Type()
)
sdhClientCtpTxOfs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTxOfs15MinutesTceReporting.setStatus("current")


class _SdhClientCtpTxOfsDayReporting_Type(TruthValue):
    """Custom type sdhClientCtpTxOfsDayReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpTxOfsDayReporting_Type.__name__ = "TruthValue"
_SdhClientCtpTxOfsDayReporting_Object = MibTableColumn
sdhClientCtpTxOfsDayReporting = _SdhClientCtpTxOfsDayReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 49),
    _SdhClientCtpTxOfsDayReporting_Type()
)
sdhClientCtpTxOfsDayReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTxOfsDayReporting.setStatus("current")


class _SdhClientCtpUasMonitoring_Type(InfnEnableDisable):
    """Custom type sdhClientCtpUasMonitoring based on InfnEnableDisable"""
    defaultValue = 1


_SdhClientCtpUasMonitoring_Type.__name__ = "InfnEnableDisable"
_SdhClientCtpUasMonitoring_Object = MibTableColumn
sdhClientCtpUasMonitoring = _SdhClientCtpUasMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 50),
    _SdhClientCtpUasMonitoring_Type()
)
sdhClientCtpUasMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpUasMonitoring.setStatus("current")


class _SdhClientCtpRxUas15MinutesTce_Type(Integer32):
    """Custom type sdhClientCtpRxUas15MinutesTce based on Integer32"""
    defaultValue = 1


_SdhClientCtpRxUas15MinutesTce_Type.__name__ = "Integer32"
_SdhClientCtpRxUas15MinutesTce_Object = MibTableColumn
sdhClientCtpRxUas15MinutesTce = _SdhClientCtpRxUas15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 51),
    _SdhClientCtpRxUas15MinutesTce_Type()
)
sdhClientCtpRxUas15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxUas15MinutesTce.setStatus("current")


class _SdhClientCtpRxUasDayTce_Type(Integer32):
    """Custom type sdhClientCtpRxUasDayTce based on Integer32"""
    defaultValue = 1


_SdhClientCtpRxUasDayTce_Type.__name__ = "Integer32"
_SdhClientCtpRxUasDayTce_Object = MibTableColumn
sdhClientCtpRxUasDayTce = _SdhClientCtpRxUasDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 52),
    _SdhClientCtpRxUasDayTce_Type()
)
sdhClientCtpRxUasDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxUasDayTce.setStatus("current")


class _SdhClientCtpTxUas15MinutesTce_Type(Integer32):
    """Custom type sdhClientCtpTxUas15MinutesTce based on Integer32"""
    defaultValue = 1


_SdhClientCtpTxUas15MinutesTce_Type.__name__ = "Integer32"
_SdhClientCtpTxUas15MinutesTce_Object = MibTableColumn
sdhClientCtpTxUas15MinutesTce = _SdhClientCtpTxUas15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 53),
    _SdhClientCtpTxUas15MinutesTce_Type()
)
sdhClientCtpTxUas15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTxUas15MinutesTce.setStatus("current")


class _SdhClientCtpTxUasDayTce_Type(Integer32):
    """Custom type sdhClientCtpTxUasDayTce based on Integer32"""
    defaultValue = 1


_SdhClientCtpTxUasDayTce_Type.__name__ = "Integer32"
_SdhClientCtpTxUasDayTce_Object = MibTableColumn
sdhClientCtpTxUasDayTce = _SdhClientCtpTxUasDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 54),
    _SdhClientCtpTxUasDayTce_Type()
)
sdhClientCtpTxUasDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTxUasDayTce.setStatus("current")


class _SdhClientCtpRxUas15MinutesTceReporting_Type(TruthValue):
    """Custom type sdhClientCtpRxUas15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpRxUas15MinutesTceReporting_Type.__name__ = "TruthValue"
_SdhClientCtpRxUas15MinutesTceReporting_Object = MibTableColumn
sdhClientCtpRxUas15MinutesTceReporting = _SdhClientCtpRxUas15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 55),
    _SdhClientCtpRxUas15MinutesTceReporting_Type()
)
sdhClientCtpRxUas15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxUas15MinutesTceReporting.setStatus("current")


class _SdhClientCtpRxUasDayTceReporting_Type(TruthValue):
    """Custom type sdhClientCtpRxUasDayTceReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpRxUasDayTceReporting_Type.__name__ = "TruthValue"
_SdhClientCtpRxUasDayTceReporting_Object = MibTableColumn
sdhClientCtpRxUasDayTceReporting = _SdhClientCtpRxUasDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 56),
    _SdhClientCtpRxUasDayTceReporting_Type()
)
sdhClientCtpRxUasDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpRxUasDayTceReporting.setStatus("current")


class _SdhClientCtpTxUas15MinutesTceReporting_Type(TruthValue):
    """Custom type sdhClientCtpTxUas15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpTxUas15MinutesTceReporting_Type.__name__ = "TruthValue"
_SdhClientCtpTxUas15MinutesTceReporting_Object = MibTableColumn
sdhClientCtpTxUas15MinutesTceReporting = _SdhClientCtpTxUas15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 57),
    _SdhClientCtpTxUas15MinutesTceReporting_Type()
)
sdhClientCtpTxUas15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTxUas15MinutesTceReporting.setStatus("current")


class _SdhClientCtpTxUasDayTceReporting_Type(TruthValue):
    """Custom type sdhClientCtpTxUasDayTceReporting based on TruthValue"""
    defaultValue = 2


_SdhClientCtpTxUasDayTceReporting_Type.__name__ = "TruthValue"
_SdhClientCtpTxUasDayTceReporting_Object = MibTableColumn
sdhClientCtpTxUasDayTceReporting = _SdhClientCtpTxUasDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 58),
    _SdhClientCtpTxUasDayTceReporting_Type()
)
sdhClientCtpTxUasDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpTxUasDayTceReporting.setStatus("current")


class _SdhClientCtpLinePrbsGenMode_Type(InfnEnableDisable):
    """Custom type sdhClientCtpLinePrbsGenMode based on InfnEnableDisable"""
    defaultValue = 1


_SdhClientCtpLinePrbsGenMode_Type.__name__ = "InfnEnableDisable"
_SdhClientCtpLinePrbsGenMode_Object = MibTableColumn
sdhClientCtpLinePrbsGenMode = _SdhClientCtpLinePrbsGenMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 59),
    _SdhClientCtpLinePrbsGenMode_Type()
)
sdhClientCtpLinePrbsGenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpLinePrbsGenMode.setStatus("current")


class _SdhClientCtpLinePrbsMonMode_Type(InfnEnableDisable):
    """Custom type sdhClientCtpLinePrbsMonMode based on InfnEnableDisable"""
    defaultValue = 1


_SdhClientCtpLinePrbsMonMode_Type.__name__ = "InfnEnableDisable"
_SdhClientCtpLinePrbsMonMode_Object = MibTableColumn
sdhClientCtpLinePrbsMonMode = _SdhClientCtpLinePrbsMonMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 60),
    _SdhClientCtpLinePrbsMonMode_Type()
)
sdhClientCtpLinePrbsMonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpLinePrbsMonMode.setStatus("current")
_SdhClientCtpServiceMode_Type = InfnServiceMode
_SdhClientCtpServiceMode_Object = MibTableColumn
sdhClientCtpServiceMode = _SdhClientCtpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 61),
    _SdhClientCtpServiceMode_Type()
)
sdhClientCtpServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpServiceMode.setStatus("current")
_SdhClientCtpServiceModeQualifier_Type = InfnSMQ
_SdhClientCtpServiceModeQualifier_Object = MibTableColumn
sdhClientCtpServiceModeQualifier = _SdhClientCtpServiceModeQualifier_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 62),
    _SdhClientCtpServiceModeQualifier_Type()
)
sdhClientCtpServiceModeQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpServiceModeQualifier.setStatus("current")
_SdhClientCtpEncapClientDisableAction_Type = InfnClientAction
_SdhClientCtpEncapClientDisableAction_Object = MibTableColumn
sdhClientCtpEncapClientDisableAction = _SdhClientCtpEncapClientDisableAction_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 1, 1, 63),
    _SdhClientCtpEncapClientDisableAction_Type()
)
sdhClientCtpEncapClientDisableAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhClientCtpEncapClientDisableAction.setStatus("current")
_SdhClientCtpConformance_ObjectIdentity = ObjectIdentity
sdhClientCtpConformance = _SdhClientCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 3)
)
_SdhClientCtpCompliances_ObjectIdentity = ObjectIdentity
sdhClientCtpCompliances = _SdhClientCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 3, 1)
)
_SdhClientCtpGroups_ObjectIdentity = ObjectIdentity
sdhClientCtpGroups = _SdhClientCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 3, 2)
)

# Managed Objects groups

sdhClientCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 3, 2, 1)
)
sdhClientCtpGroup.setObjects(
      *(("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTribPrbsGenMode"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTribPrbsMonMode"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpSupportingCircuitIdList"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpLoopback"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpPmHistStatsEnable"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpConfiguredServiceType"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxJ0"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpExpectedRxJ0"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTransmittedJ0"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxJ0MessageLength"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxJ0MismatchReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxJ0TraceMode"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxJ0MessageCompliance"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxBe15MinutesTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxEs15MinutesTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxSes15MinutesTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxOfs15MinutesTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxLoss15MinutesTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxBeDayTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxEsDayTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxSesDayTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxOfsDayTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxLossDayTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTxBe15MinutesTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTxEs15MinutesTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTxSes15MinutesTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTxOfs15MinutesTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTxBeDayTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTxEsDayTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTxSesDayTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTxOfsDayTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxBe15MinutesTceReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxEs15MinutesTceReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxSes15MinutesTceReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxBeDayTceReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxEsDayTceReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxSesDayTceReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxOfs15MinutesTceReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxOfsDayReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxLoss15MinutesTceReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxLossDayReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTxBe15MinutesTceReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTxEs15MinutesTceReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTxSes15MinutesTceReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTxBeDayTceReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTxEsDayTceReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTxSesDayTceReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTxOfs15MinutesTceReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTxOfsDayReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpUasMonitoring"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxUasDayTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTxUasDayTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTxUas15MinutesTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxUas15MinutesTce"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxUas15MinutesTceReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTxUas15MinutesTceReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpRxUasDayTceReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpTxUasDayTceReporting"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpServiceMode"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpServiceModeQualifier"),
        ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpEncapClientDisableAction"))
)
if mibBuilder.loadTexts:
    sdhClientCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sdhClientCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 15, 3, 1, 1)
)
sdhClientCtpCompliance.setObjects(
    ("INFINERA-TP-SDHCLIENTCTP-MIB", "sdhClientCtpGroup")
)
if mibBuilder.loadTexts:
    sdhClientCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-SDHCLIENTCTP-MIB",
    **{"sdhClientCtpMIB": sdhClientCtpMIB,
       "sdhClientCtpTable": sdhClientCtpTable,
       "sdhClientCtpEntry": sdhClientCtpEntry,
       "sdhClientCtpTribPrbsGenMode": sdhClientCtpTribPrbsGenMode,
       "sdhClientCtpTribPrbsMonMode": sdhClientCtpTribPrbsMonMode,
       "sdhClientCtpSupportingCircuitIdList": sdhClientCtpSupportingCircuitIdList,
       "sdhClientCtpLoopback": sdhClientCtpLoopback,
       "sdhClientCtpPmHistStatsEnable": sdhClientCtpPmHistStatsEnable,
       "sdhClientCtpConfiguredServiceType": sdhClientCtpConfiguredServiceType,
       "sdhClientCtpRxJ0": sdhClientCtpRxJ0,
       "sdhClientCtpExpectedRxJ0": sdhClientCtpExpectedRxJ0,
       "sdhClientCtpTransmittedJ0": sdhClientCtpTransmittedJ0,
       "sdhClientCtpRxJ0MessageLength": sdhClientCtpRxJ0MessageLength,
       "sdhClientCtpRxJ0MismatchReporting": sdhClientCtpRxJ0MismatchReporting,
       "sdhClientCtpRxJ0TraceMode": sdhClientCtpRxJ0TraceMode,
       "sdhClientCtpRxJ0MessageCompliance": sdhClientCtpRxJ0MessageCompliance,
       "sdhClientCtpRxBe15MinutesTce": sdhClientCtpRxBe15MinutesTce,
       "sdhClientCtpRxEs15MinutesTce": sdhClientCtpRxEs15MinutesTce,
       "sdhClientCtpRxSes15MinutesTce": sdhClientCtpRxSes15MinutesTce,
       "sdhClientCtpRxOfs15MinutesTce": sdhClientCtpRxOfs15MinutesTce,
       "sdhClientCtpRxLoss15MinutesTce": sdhClientCtpRxLoss15MinutesTce,
       "sdhClientCtpRxBeDayTce": sdhClientCtpRxBeDayTce,
       "sdhClientCtpRxEsDayTce": sdhClientCtpRxEsDayTce,
       "sdhClientCtpRxSesDayTce": sdhClientCtpRxSesDayTce,
       "sdhClientCtpRxOfsDayTce": sdhClientCtpRxOfsDayTce,
       "sdhClientCtpRxLossDayTce": sdhClientCtpRxLossDayTce,
       "sdhClientCtpTxBe15MinutesTce": sdhClientCtpTxBe15MinutesTce,
       "sdhClientCtpTxEs15MinutesTce": sdhClientCtpTxEs15MinutesTce,
       "sdhClientCtpTxSes15MinutesTce": sdhClientCtpTxSes15MinutesTce,
       "sdhClientCtpTxOfs15MinutesTce": sdhClientCtpTxOfs15MinutesTce,
       "sdhClientCtpTxBeDayTce": sdhClientCtpTxBeDayTce,
       "sdhClientCtpTxEsDayTce": sdhClientCtpTxEsDayTce,
       "sdhClientCtpTxSesDayTce": sdhClientCtpTxSesDayTce,
       "sdhClientCtpTxOfsDayTce": sdhClientCtpTxOfsDayTce,
       "sdhClientCtpRxBe15MinutesTceReporting": sdhClientCtpRxBe15MinutesTceReporting,
       "sdhClientCtpRxEs15MinutesTceReporting": sdhClientCtpRxEs15MinutesTceReporting,
       "sdhClientCtpRxSes15MinutesTceReporting": sdhClientCtpRxSes15MinutesTceReporting,
       "sdhClientCtpRxBeDayTceReporting": sdhClientCtpRxBeDayTceReporting,
       "sdhClientCtpRxEsDayTceReporting": sdhClientCtpRxEsDayTceReporting,
       "sdhClientCtpRxSesDayTceReporting": sdhClientCtpRxSesDayTceReporting,
       "sdhClientCtpRxOfs15MinutesTceReporting": sdhClientCtpRxOfs15MinutesTceReporting,
       "sdhClientCtpRxOfsDayReporting": sdhClientCtpRxOfsDayReporting,
       "sdhClientCtpRxLoss15MinutesTceReporting": sdhClientCtpRxLoss15MinutesTceReporting,
       "sdhClientCtpRxLossDayReporting": sdhClientCtpRxLossDayReporting,
       "sdhClientCtpTxBe15MinutesTceReporting": sdhClientCtpTxBe15MinutesTceReporting,
       "sdhClientCtpTxEs15MinutesTceReporting": sdhClientCtpTxEs15MinutesTceReporting,
       "sdhClientCtpTxSes15MinutesTceReporting": sdhClientCtpTxSes15MinutesTceReporting,
       "sdhClientCtpTxBeDayTceReporting": sdhClientCtpTxBeDayTceReporting,
       "sdhClientCtpTxEsDayTceReporting": sdhClientCtpTxEsDayTceReporting,
       "sdhClientCtpTxSesDayTceReporting": sdhClientCtpTxSesDayTceReporting,
       "sdhClientCtpTxOfs15MinutesTceReporting": sdhClientCtpTxOfs15MinutesTceReporting,
       "sdhClientCtpTxOfsDayReporting": sdhClientCtpTxOfsDayReporting,
       "sdhClientCtpUasMonitoring": sdhClientCtpUasMonitoring,
       "sdhClientCtpRxUas15MinutesTce": sdhClientCtpRxUas15MinutesTce,
       "sdhClientCtpRxUasDayTce": sdhClientCtpRxUasDayTce,
       "sdhClientCtpTxUas15MinutesTce": sdhClientCtpTxUas15MinutesTce,
       "sdhClientCtpTxUasDayTce": sdhClientCtpTxUasDayTce,
       "sdhClientCtpRxUas15MinutesTceReporting": sdhClientCtpRxUas15MinutesTceReporting,
       "sdhClientCtpRxUasDayTceReporting": sdhClientCtpRxUasDayTceReporting,
       "sdhClientCtpTxUas15MinutesTceReporting": sdhClientCtpTxUas15MinutesTceReporting,
       "sdhClientCtpTxUasDayTceReporting": sdhClientCtpTxUasDayTceReporting,
       "sdhClientCtpLinePrbsGenMode": sdhClientCtpLinePrbsGenMode,
       "sdhClientCtpLinePrbsMonMode": sdhClientCtpLinePrbsMonMode,
       "sdhClientCtpServiceMode": sdhClientCtpServiceMode,
       "sdhClientCtpServiceModeQualifier": sdhClientCtpServiceModeQualifier,
       "sdhClientCtpEncapClientDisableAction": sdhClientCtpEncapClientDisableAction,
       "sdhClientCtpConformance": sdhClientCtpConformance,
       "sdhClientCtpCompliances": sdhClientCtpCompliances,
       "sdhClientCtpCompliance": sdhClientCtpCompliance,
       "sdhClientCtpGroups": sdhClientCtpGroups,
       "sdhClientCtpGroup": sdhClientCtpGroup}
)
