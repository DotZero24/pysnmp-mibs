# SNMP MIB module (INFINERA-TP-SONETCLIENTCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-SONETCLIENTCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:06 2025
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

sonetClientCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16)
)
if mibBuilder.loadTexts:
    sonetClientCtpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonetClientCtpTable_Object = MibTable
sonetClientCtpTable = _SonetClientCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1)
)
if mibBuilder.loadTexts:
    sonetClientCtpTable.setStatus("current")
_SonetClientCtpEntry_Object = MibTableRow
sonetClientCtpEntry = _SonetClientCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1)
)
sonetClientCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sonetClientCtpEntry.setStatus("current")


class _SonetClientCtpTribPrbsGenMode_Type(InfnEnableDisable):
    """Custom type sonetClientCtpTribPrbsGenMode based on InfnEnableDisable"""
    defaultValue = 1


_SonetClientCtpTribPrbsGenMode_Type.__name__ = "InfnEnableDisable"
_SonetClientCtpTribPrbsGenMode_Object = MibTableColumn
sonetClientCtpTribPrbsGenMode = _SonetClientCtpTribPrbsGenMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 1),
    _SonetClientCtpTribPrbsGenMode_Type()
)
sonetClientCtpTribPrbsGenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpTribPrbsGenMode.setStatus("current")


class _SonetClientCtpTribPrbsMonMode_Type(InfnEnableDisable):
    """Custom type sonetClientCtpTribPrbsMonMode based on InfnEnableDisable"""
    defaultValue = 1


_SonetClientCtpTribPrbsMonMode_Type.__name__ = "InfnEnableDisable"
_SonetClientCtpTribPrbsMonMode_Object = MibTableColumn
sonetClientCtpTribPrbsMonMode = _SonetClientCtpTribPrbsMonMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 2),
    _SonetClientCtpTribPrbsMonMode_Type()
)
sonetClientCtpTribPrbsMonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpTribPrbsMonMode.setStatus("current")
_SonetClientCtpSupportingCircuitIdList_Type = DisplayString
_SonetClientCtpSupportingCircuitIdList_Object = MibTableColumn
sonetClientCtpSupportingCircuitIdList = _SonetClientCtpSupportingCircuitIdList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 3),
    _SonetClientCtpSupportingCircuitIdList_Type()
)
sonetClientCtpSupportingCircuitIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpSupportingCircuitIdList.setStatus("current")


class _SonetClientCtpLoopback_Type(InfnLoopbackType):
    """Custom type sonetClientCtpLoopback based on InfnLoopbackType"""
    defaultValue = 1


_SonetClientCtpLoopback_Type.__name__ = "InfnLoopbackType"
_SonetClientCtpLoopback_Object = MibTableColumn
sonetClientCtpLoopback = _SonetClientCtpLoopback_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 4),
    _SonetClientCtpLoopback_Type()
)
sonetClientCtpLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpLoopback.setStatus("current")


class _SonetClientCtpPmHistStatsEnable_Type(InfnPmHistStatsControl):
    """Custom type sonetClientCtpPmHistStatsEnable based on InfnPmHistStatsControl"""
    defaultValue = 1


_SonetClientCtpPmHistStatsEnable_Type.__name__ = "InfnPmHistStatsControl"
_SonetClientCtpPmHistStatsEnable_Object = MibTableColumn
sonetClientCtpPmHistStatsEnable = _SonetClientCtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 5),
    _SonetClientCtpPmHistStatsEnable_Type()
)
sonetClientCtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpPmHistStatsEnable.setStatus("current")
_SonetClientCtpConfiguredServiceType_Type = InfnServiceType
_SonetClientCtpConfiguredServiceType_Object = MibTableColumn
sonetClientCtpConfiguredServiceType = _SonetClientCtpConfiguredServiceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 6),
    _SonetClientCtpConfiguredServiceType_Type()
)
sonetClientCtpConfiguredServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpConfiguredServiceType.setStatus("current")
_SonetClientCtpRxJ0_Type = DisplayString
_SonetClientCtpRxJ0_Object = MibTableColumn
sonetClientCtpRxJ0 = _SonetClientCtpRxJ0_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 7),
    _SonetClientCtpRxJ0_Type()
)
sonetClientCtpRxJ0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpRxJ0.setStatus("current")
_SonetClientCtpExpectedRxJ0_Type = DisplayString
_SonetClientCtpExpectedRxJ0_Object = MibTableColumn
sonetClientCtpExpectedRxJ0 = _SonetClientCtpExpectedRxJ0_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 8),
    _SonetClientCtpExpectedRxJ0_Type()
)
sonetClientCtpExpectedRxJ0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpExpectedRxJ0.setStatus("current")
_SonetClientCtpTransmittedJ0_Type = DisplayString
_SonetClientCtpTransmittedJ0_Object = MibTableColumn
sonetClientCtpTransmittedJ0 = _SonetClientCtpTransmittedJ0_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 9),
    _SonetClientCtpTransmittedJ0_Type()
)
sonetClientCtpTransmittedJ0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpTransmittedJ0.setStatus("current")


class _SonetClientCtpRxJ0MessageLength_Type(Integer32):
    """Custom type sonetClientCtpRxJ0MessageLength based on Integer32"""
    defaultValue = 16


_SonetClientCtpRxJ0MessageLength_Type.__name__ = "Integer32"
_SonetClientCtpRxJ0MessageLength_Object = MibTableColumn
sonetClientCtpRxJ0MessageLength = _SonetClientCtpRxJ0MessageLength_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 10),
    _SonetClientCtpRxJ0MessageLength_Type()
)
sonetClientCtpRxJ0MessageLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpRxJ0MessageLength.setStatus("current")


class _SonetClientCtpRxJ0MismatchReporting_Type(InfnEnableDisable):
    """Custom type sonetClientCtpRxJ0MismatchReporting based on InfnEnableDisable"""
    defaultValue = 1


_SonetClientCtpRxJ0MismatchReporting_Type.__name__ = "InfnEnableDisable"
_SonetClientCtpRxJ0MismatchReporting_Object = MibTableColumn
sonetClientCtpRxJ0MismatchReporting = _SonetClientCtpRxJ0MismatchReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 11),
    _SonetClientCtpRxJ0MismatchReporting_Type()
)
sonetClientCtpRxJ0MismatchReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpRxJ0MismatchReporting.setStatus("current")


class _SonetClientCtpRxJ0TraceMode_Type(InfnJ0TraceMode):
    """Custom type sonetClientCtpRxJ0TraceMode based on InfnJ0TraceMode"""
    defaultValue = 1


_SonetClientCtpRxJ0TraceMode_Type.__name__ = "InfnJ0TraceMode"
_SonetClientCtpRxJ0TraceMode_Object = MibTableColumn
sonetClientCtpRxJ0TraceMode = _SonetClientCtpRxJ0TraceMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 12),
    _SonetClientCtpRxJ0TraceMode_Type()
)
sonetClientCtpRxJ0TraceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpRxJ0TraceMode.setStatus("current")


class _SonetClientCtpRxJ0MessageCompliance_Type(InfnJ0MessageCompliance):
    """Custom type sonetClientCtpRxJ0MessageCompliance based on InfnJ0MessageCompliance"""
    defaultValue = 2


_SonetClientCtpRxJ0MessageCompliance_Type.__name__ = "InfnJ0MessageCompliance"
_SonetClientCtpRxJ0MessageCompliance_Object = MibTableColumn
sonetClientCtpRxJ0MessageCompliance = _SonetClientCtpRxJ0MessageCompliance_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 13),
    _SonetClientCtpRxJ0MessageCompliance_Type()
)
sonetClientCtpRxJ0MessageCompliance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpRxJ0MessageCompliance.setStatus("current")
_SonetClientCtpRxCv15MinutesTce_Type = Counter64
_SonetClientCtpRxCv15MinutesTce_Object = MibTableColumn
sonetClientCtpRxCv15MinutesTce = _SonetClientCtpRxCv15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 14),
    _SonetClientCtpRxCv15MinutesTce_Type()
)
sonetClientCtpRxCv15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpRxCv15MinutesTce.setStatus("current")


class _SonetClientCtpRxSefs15MinutesTce_Type(Integer32):
    """Custom type sonetClientCtpRxSefs15MinutesTce based on Integer32"""
    defaultValue = 3


_SonetClientCtpRxSefs15MinutesTce_Type.__name__ = "Integer32"
_SonetClientCtpRxSefs15MinutesTce_Object = MibTableColumn
sonetClientCtpRxSefs15MinutesTce = _SonetClientCtpRxSefs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 15),
    _SonetClientCtpRxSefs15MinutesTce_Type()
)
sonetClientCtpRxSefs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpRxSefs15MinutesTce.setStatus("current")


class _SonetClientCtpRxEs15MinutesTce_Type(Integer32):
    """Custom type sonetClientCtpRxEs15MinutesTce based on Integer32"""
    defaultValue = 120


_SonetClientCtpRxEs15MinutesTce_Type.__name__ = "Integer32"
_SonetClientCtpRxEs15MinutesTce_Object = MibTableColumn
sonetClientCtpRxEs15MinutesTce = _SonetClientCtpRxEs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 16),
    _SonetClientCtpRxEs15MinutesTce_Type()
)
sonetClientCtpRxEs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpRxEs15MinutesTce.setStatus("current")


class _SonetClientCtpRxSes15MinutesTce_Type(Integer32):
    """Custom type sonetClientCtpRxSes15MinutesTce based on Integer32"""
    defaultValue = 3


_SonetClientCtpRxSes15MinutesTce_Type.__name__ = "Integer32"
_SonetClientCtpRxSes15MinutesTce_Object = MibTableColumn
sonetClientCtpRxSes15MinutesTce = _SonetClientCtpRxSes15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 17),
    _SonetClientCtpRxSes15MinutesTce_Type()
)
sonetClientCtpRxSes15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpRxSes15MinutesTce.setStatus("current")
_SonetClientCtpRxCvDayTce_Type = Counter64
_SonetClientCtpRxCvDayTce_Object = MibTableColumn
sonetClientCtpRxCvDayTce = _SonetClientCtpRxCvDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 18),
    _SonetClientCtpRxCvDayTce_Type()
)
sonetClientCtpRxCvDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpRxCvDayTce.setStatus("current")


class _SonetClientCtpRxSefsDayTce_Type(Integer32):
    """Custom type sonetClientCtpRxSefsDayTce based on Integer32"""
    defaultValue = 7


_SonetClientCtpRxSefsDayTce_Type.__name__ = "Integer32"
_SonetClientCtpRxSefsDayTce_Object = MibTableColumn
sonetClientCtpRxSefsDayTce = _SonetClientCtpRxSefsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 19),
    _SonetClientCtpRxSefsDayTce_Type()
)
sonetClientCtpRxSefsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpRxSefsDayTce.setStatus("current")


class _SonetClientCtpRxEsDayTce_Type(Integer32):
    """Custom type sonetClientCtpRxEsDayTce based on Integer32"""
    defaultValue = 1200


_SonetClientCtpRxEsDayTce_Type.__name__ = "Integer32"
_SonetClientCtpRxEsDayTce_Object = MibTableColumn
sonetClientCtpRxEsDayTce = _SonetClientCtpRxEsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 20),
    _SonetClientCtpRxEsDayTce_Type()
)
sonetClientCtpRxEsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpRxEsDayTce.setStatus("current")


class _SonetClientCtpRxSesDayTce_Type(Integer32):
    """Custom type sonetClientCtpRxSesDayTce based on Integer32"""
    defaultValue = 7


_SonetClientCtpRxSesDayTce_Type.__name__ = "Integer32"
_SonetClientCtpRxSesDayTce_Object = MibTableColumn
sonetClientCtpRxSesDayTce = _SonetClientCtpRxSesDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 21),
    _SonetClientCtpRxSesDayTce_Type()
)
sonetClientCtpRxSesDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpRxSesDayTce.setStatus("current")
_SonetClientCtpTxCv15MinutesTce_Type = Counter64
_SonetClientCtpTxCv15MinutesTce_Object = MibTableColumn
sonetClientCtpTxCv15MinutesTce = _SonetClientCtpTxCv15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 22),
    _SonetClientCtpTxCv15MinutesTce_Type()
)
sonetClientCtpTxCv15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpTxCv15MinutesTce.setStatus("current")


class _SonetClientCtpTxSefs15MinutesTce_Type(Integer32):
    """Custom type sonetClientCtpTxSefs15MinutesTce based on Integer32"""
    defaultValue = 3


_SonetClientCtpTxSefs15MinutesTce_Type.__name__ = "Integer32"
_SonetClientCtpTxSefs15MinutesTce_Object = MibTableColumn
sonetClientCtpTxSefs15MinutesTce = _SonetClientCtpTxSefs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 23),
    _SonetClientCtpTxSefs15MinutesTce_Type()
)
sonetClientCtpTxSefs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpTxSefs15MinutesTce.setStatus("current")


class _SonetClientCtpTxEs15MinutesTce_Type(Integer32):
    """Custom type sonetClientCtpTxEs15MinutesTce based on Integer32"""
    defaultValue = 120


_SonetClientCtpTxEs15MinutesTce_Type.__name__ = "Integer32"
_SonetClientCtpTxEs15MinutesTce_Object = MibTableColumn
sonetClientCtpTxEs15MinutesTce = _SonetClientCtpTxEs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 24),
    _SonetClientCtpTxEs15MinutesTce_Type()
)
sonetClientCtpTxEs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpTxEs15MinutesTce.setStatus("current")


class _SonetClientCtpTxSes15MinutesTce_Type(Integer32):
    """Custom type sonetClientCtpTxSes15MinutesTce based on Integer32"""
    defaultValue = 3


_SonetClientCtpTxSes15MinutesTce_Type.__name__ = "Integer32"
_SonetClientCtpTxSes15MinutesTce_Object = MibTableColumn
sonetClientCtpTxSes15MinutesTce = _SonetClientCtpTxSes15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 25),
    _SonetClientCtpTxSes15MinutesTce_Type()
)
sonetClientCtpTxSes15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpTxSes15MinutesTce.setStatus("current")
_SonetClientCtpTxCvDayTce_Type = Counter64
_SonetClientCtpTxCvDayTce_Object = MibTableColumn
sonetClientCtpTxCvDayTce = _SonetClientCtpTxCvDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 26),
    _SonetClientCtpTxCvDayTce_Type()
)
sonetClientCtpTxCvDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpTxCvDayTce.setStatus("current")


class _SonetClientCtpTxSefsDayTce_Type(Integer32):
    """Custom type sonetClientCtpTxSefsDayTce based on Integer32"""
    defaultValue = 7


_SonetClientCtpTxSefsDayTce_Type.__name__ = "Integer32"
_SonetClientCtpTxSefsDayTce_Object = MibTableColumn
sonetClientCtpTxSefsDayTce = _SonetClientCtpTxSefsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 27),
    _SonetClientCtpTxSefsDayTce_Type()
)
sonetClientCtpTxSefsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpTxSefsDayTce.setStatus("current")


class _SonetClientCtpTxEsDayTce_Type(Integer32):
    """Custom type sonetClientCtpTxEsDayTce based on Integer32"""
    defaultValue = 1200


_SonetClientCtpTxEsDayTce_Type.__name__ = "Integer32"
_SonetClientCtpTxEsDayTce_Object = MibTableColumn
sonetClientCtpTxEsDayTce = _SonetClientCtpTxEsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 28),
    _SonetClientCtpTxEsDayTce_Type()
)
sonetClientCtpTxEsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpTxEsDayTce.setStatus("current")


class _SonetClientCtpTxSesDayTce_Type(Integer32):
    """Custom type sonetClientCtpTxSesDayTce based on Integer32"""
    defaultValue = 7


_SonetClientCtpTxSesDayTce_Type.__name__ = "Integer32"
_SonetClientCtpTxSesDayTce_Object = MibTableColumn
sonetClientCtpTxSesDayTce = _SonetClientCtpTxSesDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 29),
    _SonetClientCtpTxSesDayTce_Type()
)
sonetClientCtpTxSesDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpTxSesDayTce.setStatus("current")


class _SonetClientCtpRxCv15MinutesTceReporting_Type(TruthValue):
    """Custom type sonetClientCtpRxCv15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_SonetClientCtpRxCv15MinutesTceReporting_Type.__name__ = "TruthValue"
_SonetClientCtpRxCv15MinutesTceReporting_Object = MibTableColumn
sonetClientCtpRxCv15MinutesTceReporting = _SonetClientCtpRxCv15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 30),
    _SonetClientCtpRxCv15MinutesTceReporting_Type()
)
sonetClientCtpRxCv15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpRxCv15MinutesTceReporting.setStatus("current")


class _SonetClientCtpRxSefs15MinutesTceReporting_Type(TruthValue):
    """Custom type sonetClientCtpRxSefs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_SonetClientCtpRxSefs15MinutesTceReporting_Type.__name__ = "TruthValue"
_SonetClientCtpRxSefs15MinutesTceReporting_Object = MibTableColumn
sonetClientCtpRxSefs15MinutesTceReporting = _SonetClientCtpRxSefs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 31),
    _SonetClientCtpRxSefs15MinutesTceReporting_Type()
)
sonetClientCtpRxSefs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpRxSefs15MinutesTceReporting.setStatus("current")


class _SonetClientCtpRxEs15MinutesTceReporting_Type(TruthValue):
    """Custom type sonetClientCtpRxEs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_SonetClientCtpRxEs15MinutesTceReporting_Type.__name__ = "TruthValue"
_SonetClientCtpRxEs15MinutesTceReporting_Object = MibTableColumn
sonetClientCtpRxEs15MinutesTceReporting = _SonetClientCtpRxEs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 32),
    _SonetClientCtpRxEs15MinutesTceReporting_Type()
)
sonetClientCtpRxEs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpRxEs15MinutesTceReporting.setStatus("current")


class _SonetClientCtpRxSes15MinutesTceReporting_Type(TruthValue):
    """Custom type sonetClientCtpRxSes15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_SonetClientCtpRxSes15MinutesTceReporting_Type.__name__ = "TruthValue"
_SonetClientCtpRxSes15MinutesTceReporting_Object = MibTableColumn
sonetClientCtpRxSes15MinutesTceReporting = _SonetClientCtpRxSes15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 33),
    _SonetClientCtpRxSes15MinutesTceReporting_Type()
)
sonetClientCtpRxSes15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpRxSes15MinutesTceReporting.setStatus("current")


class _SonetClientCtpRxCvDayTceReporting_Type(TruthValue):
    """Custom type sonetClientCtpRxCvDayTceReporting based on TruthValue"""
    defaultValue = 2


_SonetClientCtpRxCvDayTceReporting_Type.__name__ = "TruthValue"
_SonetClientCtpRxCvDayTceReporting_Object = MibTableColumn
sonetClientCtpRxCvDayTceReporting = _SonetClientCtpRxCvDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 34),
    _SonetClientCtpRxCvDayTceReporting_Type()
)
sonetClientCtpRxCvDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpRxCvDayTceReporting.setStatus("current")


class _SonetClientCtpRxSefsDayTceReporting_Type(TruthValue):
    """Custom type sonetClientCtpRxSefsDayTceReporting based on TruthValue"""
    defaultValue = 2


_SonetClientCtpRxSefsDayTceReporting_Type.__name__ = "TruthValue"
_SonetClientCtpRxSefsDayTceReporting_Object = MibTableColumn
sonetClientCtpRxSefsDayTceReporting = _SonetClientCtpRxSefsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 35),
    _SonetClientCtpRxSefsDayTceReporting_Type()
)
sonetClientCtpRxSefsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpRxSefsDayTceReporting.setStatus("current")


class _SonetClientCtpRxEsDayTceReporting_Type(TruthValue):
    """Custom type sonetClientCtpRxEsDayTceReporting based on TruthValue"""
    defaultValue = 2


_SonetClientCtpRxEsDayTceReporting_Type.__name__ = "TruthValue"
_SonetClientCtpRxEsDayTceReporting_Object = MibTableColumn
sonetClientCtpRxEsDayTceReporting = _SonetClientCtpRxEsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 36),
    _SonetClientCtpRxEsDayTceReporting_Type()
)
sonetClientCtpRxEsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpRxEsDayTceReporting.setStatus("current")


class _SonetClientCtpRxSesDayTceReporting_Type(TruthValue):
    """Custom type sonetClientCtpRxSesDayTceReporting based on TruthValue"""
    defaultValue = 2


_SonetClientCtpRxSesDayTceReporting_Type.__name__ = "TruthValue"
_SonetClientCtpRxSesDayTceReporting_Object = MibTableColumn
sonetClientCtpRxSesDayTceReporting = _SonetClientCtpRxSesDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 37),
    _SonetClientCtpRxSesDayTceReporting_Type()
)
sonetClientCtpRxSesDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpRxSesDayTceReporting.setStatus("current")


class _SonetClientCtpTxCv15MinutesTceReporting_Type(TruthValue):
    """Custom type sonetClientCtpTxCv15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_SonetClientCtpTxCv15MinutesTceReporting_Type.__name__ = "TruthValue"
_SonetClientCtpTxCv15MinutesTceReporting_Object = MibTableColumn
sonetClientCtpTxCv15MinutesTceReporting = _SonetClientCtpTxCv15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 38),
    _SonetClientCtpTxCv15MinutesTceReporting_Type()
)
sonetClientCtpTxCv15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpTxCv15MinutesTceReporting.setStatus("current")


class _SonetClientCtpTxSefs15MinutesTceReporting_Type(TruthValue):
    """Custom type sonetClientCtpTxSefs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_SonetClientCtpTxSefs15MinutesTceReporting_Type.__name__ = "TruthValue"
_SonetClientCtpTxSefs15MinutesTceReporting_Object = MibTableColumn
sonetClientCtpTxSefs15MinutesTceReporting = _SonetClientCtpTxSefs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 39),
    _SonetClientCtpTxSefs15MinutesTceReporting_Type()
)
sonetClientCtpTxSefs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpTxSefs15MinutesTceReporting.setStatus("current")


class _SonetClientCtpTxEs15MinutesTceReporting_Type(TruthValue):
    """Custom type sonetClientCtpTxEs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_SonetClientCtpTxEs15MinutesTceReporting_Type.__name__ = "TruthValue"
_SonetClientCtpTxEs15MinutesTceReporting_Object = MibTableColumn
sonetClientCtpTxEs15MinutesTceReporting = _SonetClientCtpTxEs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 40),
    _SonetClientCtpTxEs15MinutesTceReporting_Type()
)
sonetClientCtpTxEs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpTxEs15MinutesTceReporting.setStatus("current")


class _SonetClientCtpTxSes15MinutesTceReporting_Type(TruthValue):
    """Custom type sonetClientCtpTxSes15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_SonetClientCtpTxSes15MinutesTceReporting_Type.__name__ = "TruthValue"
_SonetClientCtpTxSes15MinutesTceReporting_Object = MibTableColumn
sonetClientCtpTxSes15MinutesTceReporting = _SonetClientCtpTxSes15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 41),
    _SonetClientCtpTxSes15MinutesTceReporting_Type()
)
sonetClientCtpTxSes15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpTxSes15MinutesTceReporting.setStatus("current")


class _SonetClientCtpTxCvDayTceReporting_Type(TruthValue):
    """Custom type sonetClientCtpTxCvDayTceReporting based on TruthValue"""
    defaultValue = 2


_SonetClientCtpTxCvDayTceReporting_Type.__name__ = "TruthValue"
_SonetClientCtpTxCvDayTceReporting_Object = MibTableColumn
sonetClientCtpTxCvDayTceReporting = _SonetClientCtpTxCvDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 42),
    _SonetClientCtpTxCvDayTceReporting_Type()
)
sonetClientCtpTxCvDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpTxCvDayTceReporting.setStatus("current")


class _SonetClientCtpTxSefsDayTceReporting_Type(TruthValue):
    """Custom type sonetClientCtpTxSefsDayTceReporting based on TruthValue"""
    defaultValue = 2


_SonetClientCtpTxSefsDayTceReporting_Type.__name__ = "TruthValue"
_SonetClientCtpTxSefsDayTceReporting_Object = MibTableColumn
sonetClientCtpTxSefsDayTceReporting = _SonetClientCtpTxSefsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 43),
    _SonetClientCtpTxSefsDayTceReporting_Type()
)
sonetClientCtpTxSefsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpTxSefsDayTceReporting.setStatus("current")


class _SonetClientCtpTxEsDayTceReporting_Type(TruthValue):
    """Custom type sonetClientCtpTxEsDayTceReporting based on TruthValue"""
    defaultValue = 2


_SonetClientCtpTxEsDayTceReporting_Type.__name__ = "TruthValue"
_SonetClientCtpTxEsDayTceReporting_Object = MibTableColumn
sonetClientCtpTxEsDayTceReporting = _SonetClientCtpTxEsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 44),
    _SonetClientCtpTxEsDayTceReporting_Type()
)
sonetClientCtpTxEsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpTxEsDayTceReporting.setStatus("current")


class _SonetClientCtpTxSesDayTceReporting_Type(TruthValue):
    """Custom type sonetClientCtpTxSesDayTceReporting based on TruthValue"""
    defaultValue = 2


_SonetClientCtpTxSesDayTceReporting_Type.__name__ = "TruthValue"
_SonetClientCtpTxSesDayTceReporting_Object = MibTableColumn
sonetClientCtpTxSesDayTceReporting = _SonetClientCtpTxSesDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 45),
    _SonetClientCtpTxSesDayTceReporting_Type()
)
sonetClientCtpTxSesDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpTxSesDayTceReporting.setStatus("current")


class _SonetClientCtpLinePrbsGenMode_Type(InfnEnableDisable):
    """Custom type sonetClientCtpLinePrbsGenMode based on InfnEnableDisable"""
    defaultValue = 1


_SonetClientCtpLinePrbsGenMode_Type.__name__ = "InfnEnableDisable"
_SonetClientCtpLinePrbsGenMode_Object = MibTableColumn
sonetClientCtpLinePrbsGenMode = _SonetClientCtpLinePrbsGenMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 46),
    _SonetClientCtpLinePrbsGenMode_Type()
)
sonetClientCtpLinePrbsGenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpLinePrbsGenMode.setStatus("current")


class _SonetClientCtpLinePrbsMonMode_Type(InfnEnableDisable):
    """Custom type sonetClientCtpLinePrbsMonMode based on InfnEnableDisable"""
    defaultValue = 1


_SonetClientCtpLinePrbsMonMode_Type.__name__ = "InfnEnableDisable"
_SonetClientCtpLinePrbsMonMode_Object = MibTableColumn
sonetClientCtpLinePrbsMonMode = _SonetClientCtpLinePrbsMonMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 47),
    _SonetClientCtpLinePrbsMonMode_Type()
)
sonetClientCtpLinePrbsMonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpLinePrbsMonMode.setStatus("current")
_SonetClientCtpServiceMode_Type = InfnServiceMode
_SonetClientCtpServiceMode_Object = MibTableColumn
sonetClientCtpServiceMode = _SonetClientCtpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 48),
    _SonetClientCtpServiceMode_Type()
)
sonetClientCtpServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpServiceMode.setStatus("current")
_SonetClientCtpServiceModeQualifier_Type = InfnSMQ
_SonetClientCtpServiceModeQualifier_Object = MibTableColumn
sonetClientCtpServiceModeQualifier = _SonetClientCtpServiceModeQualifier_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 49),
    _SonetClientCtpServiceModeQualifier_Type()
)
sonetClientCtpServiceModeQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpServiceModeQualifier.setStatus("current")
_SonetClientCtpEncapClientDisableAction_Type = InfnClientAction
_SonetClientCtpEncapClientDisableAction_Object = MibTableColumn
sonetClientCtpEncapClientDisableAction = _SonetClientCtpEncapClientDisableAction_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 1, 1, 50),
    _SonetClientCtpEncapClientDisableAction_Type()
)
sonetClientCtpEncapClientDisableAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonetClientCtpEncapClientDisableAction.setStatus("current")
_SonetClientCtpConformance_ObjectIdentity = ObjectIdentity
sonetClientCtpConformance = _SonetClientCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 3)
)
_SonetClientCtpCompliances_ObjectIdentity = ObjectIdentity
sonetClientCtpCompliances = _SonetClientCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 3, 1)
)
_SonetClientCtpGroups_ObjectIdentity = ObjectIdentity
sonetClientCtpGroups = _SonetClientCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 3, 2)
)

# Managed Objects groups

sonetClientCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 3, 2, 1)
)
sonetClientCtpGroup.setObjects(
      *(("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpTribPrbsGenMode"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpTribPrbsMonMode"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpSupportingCircuitIdList"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpLoopback"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpPmHistStatsEnable"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpConfiguredServiceType"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxJ0"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpExpectedRxJ0"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpTransmittedJ0"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxJ0MessageLength"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxJ0MismatchReporting"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxJ0TraceMode"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxJ0MessageCompliance"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxCv15MinutesTce"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxSefs15MinutesTce"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxEs15MinutesTce"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxSes15MinutesTce"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxCvDayTce"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxSefsDayTce"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxEsDayTce"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxSesDayTce"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpTxCv15MinutesTce"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpTxSefs15MinutesTce"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpTxEs15MinutesTce"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpTxSes15MinutesTce"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpTxCvDayTce"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpTxSefsDayTce"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpTxEsDayTce"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpTxSesDayTce"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxCv15MinutesTceReporting"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxSefs15MinutesTceReporting"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxEs15MinutesTceReporting"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxSes15MinutesTceReporting"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxCvDayTceReporting"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxSefsDayTceReporting"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxEsDayTceReporting"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpRxSesDayTceReporting"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpTxCv15MinutesTceReporting"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpTxSefs15MinutesTceReporting"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpTxEs15MinutesTceReporting"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpTxSes15MinutesTceReporting"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpTxCvDayTceReporting"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpTxSefsDayTceReporting"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpTxEsDayTceReporting"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpTxSesDayTceReporting"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpLinePrbsGenMode"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpLinePrbsMonMode"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpServiceMode"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpServiceModeQualifier"),
        ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpEncapClientDisableAction"))
)
if mibBuilder.loadTexts:
    sonetClientCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sonetClientCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 16, 3, 1, 1)
)
sonetClientCtpCompliance.setObjects(
    ("INFINERA-TP-SONETCLIENTCTP-MIB", "sonetClientCtpGroup")
)
if mibBuilder.loadTexts:
    sonetClientCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-SONETCLIENTCTP-MIB",
    **{"sonetClientCtpMIB": sonetClientCtpMIB,
       "sonetClientCtpTable": sonetClientCtpTable,
       "sonetClientCtpEntry": sonetClientCtpEntry,
       "sonetClientCtpTribPrbsGenMode": sonetClientCtpTribPrbsGenMode,
       "sonetClientCtpTribPrbsMonMode": sonetClientCtpTribPrbsMonMode,
       "sonetClientCtpSupportingCircuitIdList": sonetClientCtpSupportingCircuitIdList,
       "sonetClientCtpLoopback": sonetClientCtpLoopback,
       "sonetClientCtpPmHistStatsEnable": sonetClientCtpPmHistStatsEnable,
       "sonetClientCtpConfiguredServiceType": sonetClientCtpConfiguredServiceType,
       "sonetClientCtpRxJ0": sonetClientCtpRxJ0,
       "sonetClientCtpExpectedRxJ0": sonetClientCtpExpectedRxJ0,
       "sonetClientCtpTransmittedJ0": sonetClientCtpTransmittedJ0,
       "sonetClientCtpRxJ0MessageLength": sonetClientCtpRxJ0MessageLength,
       "sonetClientCtpRxJ0MismatchReporting": sonetClientCtpRxJ0MismatchReporting,
       "sonetClientCtpRxJ0TraceMode": sonetClientCtpRxJ0TraceMode,
       "sonetClientCtpRxJ0MessageCompliance": sonetClientCtpRxJ0MessageCompliance,
       "sonetClientCtpRxCv15MinutesTce": sonetClientCtpRxCv15MinutesTce,
       "sonetClientCtpRxSefs15MinutesTce": sonetClientCtpRxSefs15MinutesTce,
       "sonetClientCtpRxEs15MinutesTce": sonetClientCtpRxEs15MinutesTce,
       "sonetClientCtpRxSes15MinutesTce": sonetClientCtpRxSes15MinutesTce,
       "sonetClientCtpRxCvDayTce": sonetClientCtpRxCvDayTce,
       "sonetClientCtpRxSefsDayTce": sonetClientCtpRxSefsDayTce,
       "sonetClientCtpRxEsDayTce": sonetClientCtpRxEsDayTce,
       "sonetClientCtpRxSesDayTce": sonetClientCtpRxSesDayTce,
       "sonetClientCtpTxCv15MinutesTce": sonetClientCtpTxCv15MinutesTce,
       "sonetClientCtpTxSefs15MinutesTce": sonetClientCtpTxSefs15MinutesTce,
       "sonetClientCtpTxEs15MinutesTce": sonetClientCtpTxEs15MinutesTce,
       "sonetClientCtpTxSes15MinutesTce": sonetClientCtpTxSes15MinutesTce,
       "sonetClientCtpTxCvDayTce": sonetClientCtpTxCvDayTce,
       "sonetClientCtpTxSefsDayTce": sonetClientCtpTxSefsDayTce,
       "sonetClientCtpTxEsDayTce": sonetClientCtpTxEsDayTce,
       "sonetClientCtpTxSesDayTce": sonetClientCtpTxSesDayTce,
       "sonetClientCtpRxCv15MinutesTceReporting": sonetClientCtpRxCv15MinutesTceReporting,
       "sonetClientCtpRxSefs15MinutesTceReporting": sonetClientCtpRxSefs15MinutesTceReporting,
       "sonetClientCtpRxEs15MinutesTceReporting": sonetClientCtpRxEs15MinutesTceReporting,
       "sonetClientCtpRxSes15MinutesTceReporting": sonetClientCtpRxSes15MinutesTceReporting,
       "sonetClientCtpRxCvDayTceReporting": sonetClientCtpRxCvDayTceReporting,
       "sonetClientCtpRxSefsDayTceReporting": sonetClientCtpRxSefsDayTceReporting,
       "sonetClientCtpRxEsDayTceReporting": sonetClientCtpRxEsDayTceReporting,
       "sonetClientCtpRxSesDayTceReporting": sonetClientCtpRxSesDayTceReporting,
       "sonetClientCtpTxCv15MinutesTceReporting": sonetClientCtpTxCv15MinutesTceReporting,
       "sonetClientCtpTxSefs15MinutesTceReporting": sonetClientCtpTxSefs15MinutesTceReporting,
       "sonetClientCtpTxEs15MinutesTceReporting": sonetClientCtpTxEs15MinutesTceReporting,
       "sonetClientCtpTxSes15MinutesTceReporting": sonetClientCtpTxSes15MinutesTceReporting,
       "sonetClientCtpTxCvDayTceReporting": sonetClientCtpTxCvDayTceReporting,
       "sonetClientCtpTxSefsDayTceReporting": sonetClientCtpTxSefsDayTceReporting,
       "sonetClientCtpTxEsDayTceReporting": sonetClientCtpTxEsDayTceReporting,
       "sonetClientCtpTxSesDayTceReporting": sonetClientCtpTxSesDayTceReporting,
       "sonetClientCtpLinePrbsGenMode": sonetClientCtpLinePrbsGenMode,
       "sonetClientCtpLinePrbsMonMode": sonetClientCtpLinePrbsMonMode,
       "sonetClientCtpServiceMode": sonetClientCtpServiceMode,
       "sonetClientCtpServiceModeQualifier": sonetClientCtpServiceModeQualifier,
       "sonetClientCtpEncapClientDisableAction": sonetClientCtpEncapClientDisableAction,
       "sonetClientCtpConformance": sonetClientCtpConformance,
       "sonetClientCtpCompliances": sonetClientCtpCompliances,
       "sonetClientCtpCompliance": sonetClientCtpCompliance,
       "sonetClientCtpGroups": sonetClientCtpGroups,
       "sonetClientCtpGroup": sonetClientCtpGroup}
)
