# SNMP MIB module (INFINERA-TP-ODUCLIENTCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-ODUCLIENTCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:35 2025
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

(FloatTenths,
 InfnArc,
 InfnEnableDisable,
 InfnEqptType,
 InfnMonitoringMode,
 InfnNwLatencyMeasurementMode,
 InfnRate,
 InfnSMQ,
 InfnServiceMode,
 InfnServiceType,
 InfnTcmList,
 InfnTsgType,
 InfnXconType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnArc",
    "InfnEnableDisable",
    "InfnEqptType",
    "InfnMonitoringMode",
    "InfnNwLatencyMeasurementMode",
    "InfnRate",
    "InfnSMQ",
    "InfnServiceMode",
    "InfnServiceType",
    "InfnTcmList",
    "InfnTsgType",
    "InfnXconType")

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

oduClientCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23)
)
if mibBuilder.loadTexts:
    oduClientCtpMIB.setRevisions(
        ("2009-07-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OduClientCtpTable_Object = MibTable
oduClientCtpTable = _OduClientCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1)
)
if mibBuilder.loadTexts:
    oduClientCtpTable.setStatus("current")
_OduClientCtpEntry_Object = MibTableRow
oduClientCtpEntry = _OduClientCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1)
)
oduClientCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oduClientCtpEntry.setStatus("current")


class _OduClientCtpServiceMode_Type(InfnServiceMode):
    """Custom type oduClientCtpServiceMode based on InfnServiceMode"""
    defaultValue = 1


_OduClientCtpServiceMode_Type.__name__ = "InfnServiceMode"
_OduClientCtpServiceMode_Object = MibTableColumn
oduClientCtpServiceMode = _OduClientCtpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 1),
    _OduClientCtpServiceMode_Type()
)
oduClientCtpServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduClientCtpServiceMode.setStatus("current")


class _OduClientCtpServiceModeQualifier_Type(InfnSMQ):
    """Custom type oduClientCtpServiceModeQualifier based on InfnSMQ"""
    defaultValue = 1


_OduClientCtpServiceModeQualifier_Type.__name__ = "InfnSMQ"
_OduClientCtpServiceModeQualifier_Object = MibTableColumn
oduClientCtpServiceModeQualifier = _OduClientCtpServiceModeQualifier_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 2),
    _OduClientCtpServiceModeQualifier_Type()
)
oduClientCtpServiceModeQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduClientCtpServiceModeQualifier.setStatus("current")
_OduClientCtpFacMonitoringMode_Type = InfnMonitoringMode
_OduClientCtpFacMonitoringMode_Object = MibTableColumn
oduClientCtpFacMonitoringMode = _OduClientCtpFacMonitoringMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 3),
    _OduClientCtpFacMonitoringMode_Type()
)
oduClientCtpFacMonitoringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpFacMonitoringMode.setStatus("current")


class _OduClientCtpFacTxTTI_Type(DisplayString):
    """Custom type oduClientCtpFacTxTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OduClientCtpFacTxTTI_Type.__name__ = "DisplayString"
_OduClientCtpFacTxTTI_Object = MibTableColumn
oduClientCtpFacTxTTI = _OduClientCtpFacTxTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 4),
    _OduClientCtpFacTxTTI_Type()
)
oduClientCtpFacTxTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpFacTxTTI.setStatus("current")


class _OduClientCtpFacExpectedSAPI_Type(DisplayString):
    """Custom type oduClientCtpFacExpectedSAPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_OduClientCtpFacExpectedSAPI_Type.__name__ = "DisplayString"
_OduClientCtpFacExpectedSAPI_Object = MibTableColumn
oduClientCtpFacExpectedSAPI = _OduClientCtpFacExpectedSAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 5),
    _OduClientCtpFacExpectedSAPI_Type()
)
oduClientCtpFacExpectedSAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpFacExpectedSAPI.setStatus("current")


class _OduClientCtpFacExpectedDAPI_Type(DisplayString):
    """Custom type oduClientCtpFacExpectedDAPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_OduClientCtpFacExpectedDAPI_Type.__name__ = "DisplayString"
_OduClientCtpFacExpectedDAPI_Object = MibTableColumn
oduClientCtpFacExpectedDAPI = _OduClientCtpFacExpectedDAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 6),
    _OduClientCtpFacExpectedDAPI_Type()
)
oduClientCtpFacExpectedDAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpFacExpectedDAPI.setStatus("current")


class _OduClientCtpTermTxTTI_Type(DisplayString):
    """Custom type oduClientCtpTermTxTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OduClientCtpTermTxTTI_Type.__name__ = "DisplayString"
_OduClientCtpTermTxTTI_Object = MibTableColumn
oduClientCtpTermTxTTI = _OduClientCtpTermTxTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 7),
    _OduClientCtpTermTxTTI_Type()
)
oduClientCtpTermTxTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTermTxTTI.setStatus("current")


class _OduClientCtpTermExpectedSAPI_Type(DisplayString):
    """Custom type oduClientCtpTermExpectedSAPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_OduClientCtpTermExpectedSAPI_Type.__name__ = "DisplayString"
_OduClientCtpTermExpectedSAPI_Object = MibTableColumn
oduClientCtpTermExpectedSAPI = _OduClientCtpTermExpectedSAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 8),
    _OduClientCtpTermExpectedSAPI_Type()
)
oduClientCtpTermExpectedSAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTermExpectedSAPI.setStatus("current")


class _OduClientCtpTermExpectedDAPI_Type(DisplayString):
    """Custom type oduClientCtpTermExpectedDAPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_OduClientCtpTermExpectedDAPI_Type.__name__ = "DisplayString"
_OduClientCtpTermExpectedDAPI_Object = MibTableColumn
oduClientCtpTermExpectedDAPI = _OduClientCtpTermExpectedDAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 9),
    _OduClientCtpTermExpectedDAPI_Type()
)
oduClientCtpTermExpectedDAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTermExpectedDAPI.setStatus("current")


class _OduClientCtpFacReceivedTTI_Type(DisplayString):
    """Custom type oduClientCtpFacReceivedTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OduClientCtpFacReceivedTTI_Type.__name__ = "DisplayString"
_OduClientCtpFacReceivedTTI_Object = MibTableColumn
oduClientCtpFacReceivedTTI = _OduClientCtpFacReceivedTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 10),
    _OduClientCtpFacReceivedTTI_Type()
)
oduClientCtpFacReceivedTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduClientCtpFacReceivedTTI.setStatus("current")


class _OduClientCtpTermReceivedTTI_Type(DisplayString):
    """Custom type oduClientCtpTermReceivedTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OduClientCtpTermReceivedTTI_Type.__name__ = "DisplayString"
_OduClientCtpTermReceivedTTI_Object = MibTableColumn
oduClientCtpTermReceivedTTI = _OduClientCtpTermReceivedTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 11),
    _OduClientCtpTermReceivedTTI_Type()
)
oduClientCtpTermReceivedTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduClientCtpTermReceivedTTI.setStatus("current")


class _OduClientCtpRxEb15MinutesTce_Type(Integer32):
    """Custom type oduClientCtpRxEb15MinutesTce based on Integer32"""
    defaultValue = 1500


_OduClientCtpRxEb15MinutesTce_Type.__name__ = "Integer32"
_OduClientCtpRxEb15MinutesTce_Object = MibTableColumn
oduClientCtpRxEb15MinutesTce = _OduClientCtpRxEb15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 12),
    _OduClientCtpRxEb15MinutesTce_Type()
)
oduClientCtpRxEb15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpRxEb15MinutesTce.setStatus("current")


class _OduClientCtpTxEb15MinutesTce_Type(Integer32):
    """Custom type oduClientCtpTxEb15MinutesTce based on Integer32"""
    defaultValue = 1500


_OduClientCtpTxEb15MinutesTce_Type.__name__ = "Integer32"
_OduClientCtpTxEb15MinutesTce_Object = MibTableColumn
oduClientCtpTxEb15MinutesTce = _OduClientCtpTxEb15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 13),
    _OduClientCtpTxEb15MinutesTce_Type()
)
oduClientCtpTxEb15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTxEb15MinutesTce.setStatus("current")


class _OduClientCtpRxEbDayTce_Type(Integer32):
    """Custom type oduClientCtpRxEbDayTce based on Integer32"""
    defaultValue = 15000


_OduClientCtpRxEbDayTce_Type.__name__ = "Integer32"
_OduClientCtpRxEbDayTce_Object = MibTableColumn
oduClientCtpRxEbDayTce = _OduClientCtpRxEbDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 14),
    _OduClientCtpRxEbDayTce_Type()
)
oduClientCtpRxEbDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpRxEbDayTce.setStatus("current")


class _OduClientCtpTxEbDayTce_Type(Integer32):
    """Custom type oduClientCtpTxEbDayTce based on Integer32"""
    defaultValue = 15000


_OduClientCtpTxEbDayTce_Type.__name__ = "Integer32"
_OduClientCtpTxEbDayTce_Object = MibTableColumn
oduClientCtpTxEbDayTce = _OduClientCtpTxEbDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 15),
    _OduClientCtpTxEbDayTce_Type()
)
oduClientCtpTxEbDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTxEbDayTce.setStatus("current")


class _OduClientCtpRxDs15MinutesTce_Type(Integer32):
    """Custom type oduClientCtpRxDs15MinutesTce based on Integer32"""
    defaultValue = 120


_OduClientCtpRxDs15MinutesTce_Type.__name__ = "Integer32"
_OduClientCtpRxDs15MinutesTce_Object = MibTableColumn
oduClientCtpRxDs15MinutesTce = _OduClientCtpRxDs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 16),
    _OduClientCtpRxDs15MinutesTce_Type()
)
oduClientCtpRxDs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpRxDs15MinutesTce.setStatus("current")


class _OduClientCtpTxDs15MinutesTce_Type(Integer32):
    """Custom type oduClientCtpTxDs15MinutesTce based on Integer32"""
    defaultValue = 120


_OduClientCtpTxDs15MinutesTce_Type.__name__ = "Integer32"
_OduClientCtpTxDs15MinutesTce_Object = MibTableColumn
oduClientCtpTxDs15MinutesTce = _OduClientCtpTxDs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 17),
    _OduClientCtpTxDs15MinutesTce_Type()
)
oduClientCtpTxDs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTxDs15MinutesTce.setStatus("current")


class _OduClientCtpRxDsDayTce_Type(Integer32):
    """Custom type oduClientCtpRxDsDayTce based on Integer32"""
    defaultValue = 1200


_OduClientCtpRxDsDayTce_Type.__name__ = "Integer32"
_OduClientCtpRxDsDayTce_Object = MibTableColumn
oduClientCtpRxDsDayTce = _OduClientCtpRxDsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 18),
    _OduClientCtpRxDsDayTce_Type()
)
oduClientCtpRxDsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpRxDsDayTce.setStatus("current")


class _OduClientCtpTxDsDayTce_Type(Integer32):
    """Custom type oduClientCtpTxDsDayTce based on Integer32"""
    defaultValue = 1200


_OduClientCtpTxDsDayTce_Type.__name__ = "Integer32"
_OduClientCtpTxDsDayTce_Object = MibTableColumn
oduClientCtpTxDsDayTce = _OduClientCtpTxDsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 19),
    _OduClientCtpTxDsDayTce_Type()
)
oduClientCtpTxDsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTxDsDayTce.setStatus("current")


class _OduClientCtpRxEbDayTceReporting_Type(TruthValue):
    """Custom type oduClientCtpRxEbDayTceReporting based on TruthValue"""
    defaultValue = 2


_OduClientCtpRxEbDayTceReporting_Type.__name__ = "TruthValue"
_OduClientCtpRxEbDayTceReporting_Object = MibTableColumn
oduClientCtpRxEbDayTceReporting = _OduClientCtpRxEbDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 20),
    _OduClientCtpRxEbDayTceReporting_Type()
)
oduClientCtpRxEbDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpRxEbDayTceReporting.setStatus("current")


class _OduClientCtpRxEb15MinutesTceReporting_Type(TruthValue):
    """Custom type oduClientCtpRxEb15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OduClientCtpRxEb15MinutesTceReporting_Type.__name__ = "TruthValue"
_OduClientCtpRxEb15MinutesTceReporting_Object = MibTableColumn
oduClientCtpRxEb15MinutesTceReporting = _OduClientCtpRxEb15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 21),
    _OduClientCtpRxEb15MinutesTceReporting_Type()
)
oduClientCtpRxEb15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpRxEb15MinutesTceReporting.setStatus("current")


class _OduClientCtpTxEbDayTceReporting_Type(TruthValue):
    """Custom type oduClientCtpTxEbDayTceReporting based on TruthValue"""
    defaultValue = 2


_OduClientCtpTxEbDayTceReporting_Type.__name__ = "TruthValue"
_OduClientCtpTxEbDayTceReporting_Object = MibTableColumn
oduClientCtpTxEbDayTceReporting = _OduClientCtpTxEbDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 22),
    _OduClientCtpTxEbDayTceReporting_Type()
)
oduClientCtpTxEbDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTxEbDayTceReporting.setStatus("current")


class _OduClientCtpTxEb15MinutesTceReporting_Type(TruthValue):
    """Custom type oduClientCtpTxEb15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OduClientCtpTxEb15MinutesTceReporting_Type.__name__ = "TruthValue"
_OduClientCtpTxEb15MinutesTceReporting_Object = MibTableColumn
oduClientCtpTxEb15MinutesTceReporting = _OduClientCtpTxEb15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 23),
    _OduClientCtpTxEb15MinutesTceReporting_Type()
)
oduClientCtpTxEb15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTxEb15MinutesTceReporting.setStatus("current")


class _OduClientCtpRxDsDayTceReporting_Type(TruthValue):
    """Custom type oduClientCtpRxDsDayTceReporting based on TruthValue"""
    defaultValue = 2


_OduClientCtpRxDsDayTceReporting_Type.__name__ = "TruthValue"
_OduClientCtpRxDsDayTceReporting_Object = MibTableColumn
oduClientCtpRxDsDayTceReporting = _OduClientCtpRxDsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 24),
    _OduClientCtpRxDsDayTceReporting_Type()
)
oduClientCtpRxDsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpRxDsDayTceReporting.setStatus("current")


class _OduClientCtpRxDs15MinutesTceReporting_Type(TruthValue):
    """Custom type oduClientCtpRxDs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OduClientCtpRxDs15MinutesTceReporting_Type.__name__ = "TruthValue"
_OduClientCtpRxDs15MinutesTceReporting_Object = MibTableColumn
oduClientCtpRxDs15MinutesTceReporting = _OduClientCtpRxDs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 25),
    _OduClientCtpRxDs15MinutesTceReporting_Type()
)
oduClientCtpRxDs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpRxDs15MinutesTceReporting.setStatus("current")


class _OduClientCtpTxDsDayTceReporting_Type(TruthValue):
    """Custom type oduClientCtpTxDsDayTceReporting based on TruthValue"""
    defaultValue = 2


_OduClientCtpTxDsDayTceReporting_Type.__name__ = "TruthValue"
_OduClientCtpTxDsDayTceReporting_Object = MibTableColumn
oduClientCtpTxDsDayTceReporting = _OduClientCtpTxDsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 26),
    _OduClientCtpTxDsDayTceReporting_Type()
)
oduClientCtpTxDsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTxDsDayTceReporting.setStatus("current")


class _OduClientCtpTxDs15MinutesTceReporting_Type(TruthValue):
    """Custom type oduClientCtpTxDs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OduClientCtpTxDs15MinutesTceReporting_Type.__name__ = "TruthValue"
_OduClientCtpTxDs15MinutesTceReporting_Object = MibTableColumn
oduClientCtpTxDs15MinutesTceReporting = _OduClientCtpTxDs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 27),
    _OduClientCtpTxDs15MinutesTceReporting_Type()
)
oduClientCtpTxDs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTxDs15MinutesTceReporting.setStatus("current")


class _OduClientCtpFacTimDetMode_Type(Integer32):
    """Custom type oduClientCtpFacTimDetMode based on Integer32"""
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
        *(("off", 1),
          ("sapi", 2),
          ("dapi", 3),
          ("sapidapi", 4))
    )


_OduClientCtpFacTimDetMode_Type.__name__ = "Integer32"
_OduClientCtpFacTimDetMode_Object = MibTableColumn
oduClientCtpFacTimDetMode = _OduClientCtpFacTimDetMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 28),
    _OduClientCtpFacTimDetMode_Type()
)
oduClientCtpFacTimDetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpFacTimDetMode.setStatus("current")


class _OduClientCtpTermTimDetMode_Type(Integer32):
    """Custom type oduClientCtpTermTimDetMode based on Integer32"""
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
        *(("off", 1),
          ("sapi", 2),
          ("dapi", 3),
          ("sapidapi", 4))
    )


_OduClientCtpTermTimDetMode_Type.__name__ = "Integer32"
_OduClientCtpTermTimDetMode_Object = MibTableColumn
oduClientCtpTermTimDetMode = _OduClientCtpTermTimDetMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 29),
    _OduClientCtpTermTimDetMode_Type()
)
oduClientCtpTermTimDetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTermTimDetMode.setStatus("current")
_OduClientCtpTcmList_Type = InfnTcmList
_OduClientCtpTcmList_Object = MibTableColumn
oduClientCtpTcmList = _OduClientCtpTcmList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 30),
    _OduClientCtpTcmList_Type()
)
oduClientCtpTcmList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduClientCtpTcmList.setStatus("current")
_OduClientCtpConfiguredServiceType_Type = InfnServiceType
_OduClientCtpConfiguredServiceType_Object = MibTableColumn
oduClientCtpConfiguredServiceType = _OduClientCtpConfiguredServiceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 31),
    _OduClientCtpConfiguredServiceType_Type()
)
oduClientCtpConfiguredServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduClientCtpConfiguredServiceType.setStatus("current")
_OduClientCtpTamType_Type = InfnEqptType
_OduClientCtpTamType_Object = MibTableColumn
oduClientCtpTamType = _OduClientCtpTamType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 32),
    _OduClientCtpTamType_Type()
)
oduClientCtpTamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduClientCtpTamType.setStatus("obsolete")


class _OduClientCtpFacPmHistStatsEnable_Type(InfnEnableDisable):
    """Custom type oduClientCtpFacPmHistStatsEnable based on InfnEnableDisable"""
    defaultValue = 2


_OduClientCtpFacPmHistStatsEnable_Type.__name__ = "InfnEnableDisable"
_OduClientCtpFacPmHistStatsEnable_Object = MibTableColumn
oduClientCtpFacPmHistStatsEnable = _OduClientCtpFacPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 33),
    _OduClientCtpFacPmHistStatsEnable_Type()
)
oduClientCtpFacPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpFacPmHistStatsEnable.setStatus("current")


class _OduClientCtpTermPmHistStatsEnable_Type(InfnEnableDisable):
    """Custom type oduClientCtpTermPmHistStatsEnable based on InfnEnableDisable"""
    defaultValue = 2


_OduClientCtpTermPmHistStatsEnable_Type.__name__ = "InfnEnableDisable"
_OduClientCtpTermPmHistStatsEnable_Object = MibTableColumn
oduClientCtpTermPmHistStatsEnable = _OduClientCtpTermPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 34),
    _OduClientCtpTermPmHistStatsEnable_Type()
)
oduClientCtpTermPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTermPmHistStatsEnable.setStatus("current")


class _OduClientCtpAlarmReportControl_Type(InfnArc):
    """Custom type oduClientCtpAlarmReportControl based on InfnArc"""
    defaultValue = 1


_OduClientCtpAlarmReportControl_Type.__name__ = "InfnArc"
_OduClientCtpAlarmReportControl_Object = MibTableColumn
oduClientCtpAlarmReportControl = _OduClientCtpAlarmReportControl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 35),
    _OduClientCtpAlarmReportControl_Type()
)
oduClientCtpAlarmReportControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpAlarmReportControl.setStatus("current")
_OduClientCtpSupportingCircuitIdList_Type = DisplayString
_OduClientCtpSupportingCircuitIdList_Object = MibTableColumn
oduClientCtpSupportingCircuitIdList = _OduClientCtpSupportingCircuitIdList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 36),
    _OduClientCtpSupportingCircuitIdList_Type()
)
oduClientCtpSupportingCircuitIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduClientCtpSupportingCircuitIdList.setStatus("current")


class _OduClientCtpFacDSThreshold_Type(Integer32):
    """Custom type oduClientCtpFacDSThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OduClientCtpFacDSThreshold_Type.__name__ = "Integer32"
_OduClientCtpFacDSThreshold_Object = MibTableColumn
oduClientCtpFacDSThreshold = _OduClientCtpFacDSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 37),
    _OduClientCtpFacDSThreshold_Type()
)
oduClientCtpFacDSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpFacDSThreshold.setStatus("current")


class _OduClientCtpTermDSThreshold_Type(Integer32):
    """Custom type oduClientCtpTermDSThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OduClientCtpTermDSThreshold_Type.__name__ = "Integer32"
_OduClientCtpTermDSThreshold_Object = MibTableColumn
oduClientCtpTermDSThreshold = _OduClientCtpTermDSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 38),
    _OduClientCtpTermDSThreshold_Type()
)
oduClientCtpTermDSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTermDSThreshold.setStatus("current")
_OduClientCtpTermMonitoringMode_Type = InfnMonitoringMode
_OduClientCtpTermMonitoringMode_Object = MibTableColumn
oduClientCtpTermMonitoringMode = _OduClientCtpTermMonitoringMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 39),
    _OduClientCtpTermMonitoringMode_Type()
)
oduClientCtpTermMonitoringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTermMonitoringMode.setStatus("current")


class _OduClientCtpRxBei15MinutesTce_Type(Integer32):
    """Custom type oduClientCtpRxBei15MinutesTce based on Integer32"""
    defaultValue = 1500


_OduClientCtpRxBei15MinutesTce_Type.__name__ = "Integer32"
_OduClientCtpRxBei15MinutesTce_Object = MibTableColumn
oduClientCtpRxBei15MinutesTce = _OduClientCtpRxBei15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 40),
    _OduClientCtpRxBei15MinutesTce_Type()
)
oduClientCtpRxBei15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpRxBei15MinutesTce.setStatus("current")


class _OduClientCtpTxBei15MinutesTce_Type(Integer32):
    """Custom type oduClientCtpTxBei15MinutesTce based on Integer32"""
    defaultValue = 1500


_OduClientCtpTxBei15MinutesTce_Type.__name__ = "Integer32"
_OduClientCtpTxBei15MinutesTce_Object = MibTableColumn
oduClientCtpTxBei15MinutesTce = _OduClientCtpTxBei15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 41),
    _OduClientCtpTxBei15MinutesTce_Type()
)
oduClientCtpTxBei15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTxBei15MinutesTce.setStatus("current")


class _OduClientCtpRxBeiDayTce_Type(Integer32):
    """Custom type oduClientCtpRxBeiDayTce based on Integer32"""
    defaultValue = 15000


_OduClientCtpRxBeiDayTce_Type.__name__ = "Integer32"
_OduClientCtpRxBeiDayTce_Object = MibTableColumn
oduClientCtpRxBeiDayTce = _OduClientCtpRxBeiDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 42),
    _OduClientCtpRxBeiDayTce_Type()
)
oduClientCtpRxBeiDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpRxBeiDayTce.setStatus("current")


class _OduClientCtpTxBeiDayTce_Type(Integer32):
    """Custom type oduClientCtpTxBeiDayTce based on Integer32"""
    defaultValue = 15000


_OduClientCtpTxBeiDayTce_Type.__name__ = "Integer32"
_OduClientCtpTxBeiDayTce_Object = MibTableColumn
oduClientCtpTxBeiDayTce = _OduClientCtpTxBeiDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 43),
    _OduClientCtpTxBeiDayTce_Type()
)
oduClientCtpTxBeiDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTxBeiDayTce.setStatus("current")


class _OduClientCtpRxBeiDayTceReporting_Type(TruthValue):
    """Custom type oduClientCtpRxBeiDayTceReporting based on TruthValue"""
    defaultValue = 2


_OduClientCtpRxBeiDayTceReporting_Type.__name__ = "TruthValue"
_OduClientCtpRxBeiDayTceReporting_Object = MibTableColumn
oduClientCtpRxBeiDayTceReporting = _OduClientCtpRxBeiDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 44),
    _OduClientCtpRxBeiDayTceReporting_Type()
)
oduClientCtpRxBeiDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpRxBeiDayTceReporting.setStatus("current")


class _OduClientCtpRxBei15MinutesTceReporting_Type(TruthValue):
    """Custom type oduClientCtpRxBei15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OduClientCtpRxBei15MinutesTceReporting_Type.__name__ = "TruthValue"
_OduClientCtpRxBei15MinutesTceReporting_Object = MibTableColumn
oduClientCtpRxBei15MinutesTceReporting = _OduClientCtpRxBei15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 45),
    _OduClientCtpRxBei15MinutesTceReporting_Type()
)
oduClientCtpRxBei15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpRxBei15MinutesTceReporting.setStatus("current")


class _OduClientCtpTxBeiDayTceReporting_Type(TruthValue):
    """Custom type oduClientCtpTxBeiDayTceReporting based on TruthValue"""
    defaultValue = 2


_OduClientCtpTxBeiDayTceReporting_Type.__name__ = "TruthValue"
_OduClientCtpTxBeiDayTceReporting_Object = MibTableColumn
oduClientCtpTxBeiDayTceReporting = _OduClientCtpTxBeiDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 46),
    _OduClientCtpTxBeiDayTceReporting_Type()
)
oduClientCtpTxBeiDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTxBeiDayTceReporting.setStatus("current")


class _OduClientCtpTxBei15MinutesTceReporting_Type(TruthValue):
    """Custom type oduClientCtpTxBei15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OduClientCtpTxBei15MinutesTceReporting_Type.__name__ = "TruthValue"
_OduClientCtpTxBei15MinutesTceReporting_Object = MibTableColumn
oduClientCtpTxBei15MinutesTceReporting = _OduClientCtpTxBei15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 47),
    _OduClientCtpTxBei15MinutesTceReporting_Type()
)
oduClientCtpTxBei15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTxBei15MinutesTceReporting.setStatus("current")
_OduClientCtpTSCount_Type = Integer32
_OduClientCtpTSCount_Object = MibTableColumn
oduClientCtpTSCount = _OduClientCtpTSCount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 48),
    _OduClientCtpTSCount_Type()
)
oduClientCtpTSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduClientCtpTSCount.setStatus("current")
_OduClientCtprate_Type = DisplayString
_OduClientCtprate_Object = MibTableColumn
oduClientCtprate = _OduClientCtprate_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 49),
    _OduClientCtprate_Type()
)
oduClientCtprate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduClientCtprate.setStatus("current")
_OduClientCtpTributaryPortNumber_Type = Integer32
_OduClientCtpTributaryPortNumber_Object = MibTableColumn
oduClientCtpTributaryPortNumber = _OduClientCtpTributaryPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 50),
    _OduClientCtpTributaryPortNumber_Type()
)
oduClientCtpTributaryPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduClientCtpTributaryPortNumber.setStatus("current")
_OduClientCtpExpectedTPNs_Type = Integer32
_OduClientCtpExpectedTPNs_Object = MibTableColumn
oduClientCtpExpectedTPNs = _OduClientCtpExpectedTPNs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 51),
    _OduClientCtpExpectedTPNs_Type()
)
oduClientCtpExpectedTPNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduClientCtpExpectedTPNs.setStatus("current")
_OduClientCtpDetectedTPNs_Type = Integer32
_OduClientCtpDetectedTPNs_Object = MibTableColumn
oduClientCtpDetectedTPNs = _OduClientCtpDetectedTPNs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 52),
    _OduClientCtpDetectedTPNs_Type()
)
oduClientCtpDetectedTPNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduClientCtpDetectedTPNs.setStatus("current")
_OduClientCtpuserConfigured_Type = TruthValue
_OduClientCtpuserConfigured_Object = MibTableColumn
oduClientCtpuserConfigured = _OduClientCtpuserConfigured_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 53),
    _OduClientCtpuserConfigured_Type()
)
oduClientCtpuserConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpuserConfigured.setStatus("obsolete")
_OduClientCtpsupportingOPUTributarySlots_Type = DisplayString
_OduClientCtpsupportingOPUTributarySlots_Object = MibTableColumn
oduClientCtpsupportingOPUTributarySlots = _OduClientCtpsupportingOPUTributarySlots_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 54),
    _OduClientCtpsupportingOPUTributarySlots_Type()
)
oduClientCtpsupportingOPUTributarySlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpsupportingOPUTributarySlots.setStatus("current")
_OduClientCtpavailableOPUTributarySlots_Type = DisplayString
_OduClientCtpavailableOPUTributarySlots_Object = MibTableColumn
oduClientCtpavailableOPUTributarySlots = _OduClientCtpavailableOPUTributarySlots_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 55),
    _OduClientCtpavailableOPUTributarySlots_Type()
)
oduClientCtpavailableOPUTributarySlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduClientCtpavailableOPUTributarySlots.setStatus("current")
_OduClientCtpdatarate_Type = InfnRate
_OduClientCtpdatarate_Object = MibTableColumn
oduClientCtpdatarate = _OduClientCtpdatarate_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 56),
    _OduClientCtpdatarate_Type()
)
oduClientCtpdatarate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduClientCtpdatarate.setStatus("current")
_OduClientCtpCrossConnectType_Type = InfnXconType
_OduClientCtpCrossConnectType_Object = MibTableColumn
oduClientCtpCrossConnectType = _OduClientCtpCrossConnectType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 57),
    _OduClientCtpCrossConnectType_Type()
)
oduClientCtpCrossConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduClientCtpCrossConnectType.setStatus("current")
_OduClientCtpSupportingTP_Type = DisplayString
_OduClientCtpSupportingTP_Object = MibTableColumn
oduClientCtpSupportingTP = _OduClientCtpSupportingTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 58),
    _OduClientCtpSupportingTP_Type()
)
oduClientCtpSupportingTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpSupportingTP.setStatus("current")
_OduClientCtpTsg_Type = InfnTsgType
_OduClientCtpTsg_Object = MibTableColumn
oduClientCtpTsg = _OduClientCtpTsg_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 59),
    _OduClientCtpTsg_Type()
)
oduClientCtpTsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTsg.setStatus("current")
_OduClientCtpExpectedPayload_Type = InfnServiceType
_OduClientCtpExpectedPayload_Object = MibTableColumn
oduClientCtpExpectedPayload = _OduClientCtpExpectedPayload_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 60),
    _OduClientCtpExpectedPayload_Type()
)
oduClientCtpExpectedPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduClientCtpExpectedPayload.setStatus("current")


class _OduClientCtpLoopBack_Type(Integer32):
    """Custom type oduClientCtpLoopBack based on Integer32"""
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
          ("terminal", 2),
          ("facility", 3))
    )


_OduClientCtpLoopBack_Type.__name__ = "Integer32"
_OduClientCtpLoopBack_Object = MibTableColumn
oduClientCtpLoopBack = _OduClientCtpLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 61),
    _OduClientCtpLoopBack_Type()
)
oduClientCtpLoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpLoopBack.setStatus("current")


class _OduClientCtpFacSDThreshold_Type(Integer32):
    """Custom type oduClientCtpFacSDThreshold based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_OduClientCtpFacSDThreshold_Type.__name__ = "Integer32"
_OduClientCtpFacSDThreshold_Object = MibTableColumn
oduClientCtpFacSDThreshold = _OduClientCtpFacSDThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 62),
    _OduClientCtpFacSDThreshold_Type()
)
oduClientCtpFacSDThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpFacSDThreshold.setStatus("current")
_OduClientCtpFacPrbsGenMode_Type = InfnEnableDisable
_OduClientCtpFacPrbsGenMode_Object = MibTableColumn
oduClientCtpFacPrbsGenMode = _OduClientCtpFacPrbsGenMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 63),
    _OduClientCtpFacPrbsGenMode_Type()
)
oduClientCtpFacPrbsGenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpFacPrbsGenMode.setStatus("current")
_OduClientCtpFacPrbsMonMode_Type = InfnEnableDisable
_OduClientCtpFacPrbsMonMode_Object = MibTableColumn
oduClientCtpFacPrbsMonMode = _OduClientCtpFacPrbsMonMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 64),
    _OduClientCtpFacPrbsMonMode_Type()
)
oduClientCtpFacPrbsMonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpFacPrbsMonMode.setStatus("current")
_OduClientCtpTermPrbsGenMode_Type = InfnEnableDisable
_OduClientCtpTermPrbsGenMode_Object = MibTableColumn
oduClientCtpTermPrbsGenMode = _OduClientCtpTermPrbsGenMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 65),
    _OduClientCtpTermPrbsGenMode_Type()
)
oduClientCtpTermPrbsGenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTermPrbsGenMode.setStatus("current")
_OduClientCtpTermPrbsMonMode_Type = InfnEnableDisable
_OduClientCtpTermPrbsMonMode_Object = MibTableColumn
oduClientCtpTermPrbsMonMode = _OduClientCtpTermPrbsMonMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 66),
    _OduClientCtpTermPrbsMonMode_Type()
)
oduClientCtpTermPrbsMonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTermPrbsMonMode.setStatus("current")
_OduClientCtpDetectedPayloadType_Type = InfnServiceType
_OduClientCtpDetectedPayloadType_Object = MibTableColumn
oduClientCtpDetectedPayloadType = _OduClientCtpDetectedPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 67),
    _OduClientCtpDetectedPayloadType_Type()
)
oduClientCtpDetectedPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduClientCtpDetectedPayloadType.setStatus("current")
_OduClientCtpFacDMPELatencyMode_Type = InfnNwLatencyMeasurementMode
_OduClientCtpFacDMPELatencyMode_Object = MibTableColumn
oduClientCtpFacDMPELatencyMode = _OduClientCtpFacDMPELatencyMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 68),
    _OduClientCtpFacDMPELatencyMode_Type()
)
oduClientCtpFacDMPELatencyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpFacDMPELatencyMode.setStatus("current")
_OduClientCtpFacDMPSLatencyMode_Type = InfnNwLatencyMeasurementMode
_OduClientCtpFacDMPSLatencyMode_Object = MibTableColumn
oduClientCtpFacDMPSLatencyMode = _OduClientCtpFacDMPSLatencyMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 69),
    _OduClientCtpFacDMPSLatencyMode_Type()
)
oduClientCtpFacDMPSLatencyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpFacDMPSLatencyMode.setStatus("current")
_OduClientCtpTermDMPELatencyMode_Type = InfnNwLatencyMeasurementMode
_OduClientCtpTermDMPELatencyMode_Object = MibTableColumn
oduClientCtpTermDMPELatencyMode = _OduClientCtpTermDMPELatencyMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 70),
    _OduClientCtpTermDMPELatencyMode_Type()
)
oduClientCtpTermDMPELatencyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTermDMPELatencyMode.setStatus("current")
_OduClientCtpTermDMPSLatencyMode_Type = InfnNwLatencyMeasurementMode
_OduClientCtpTermDMPSLatencyMode_Object = MibTableColumn
oduClientCtpTermDMPSLatencyMode = _OduClientCtpTermDMPSLatencyMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 71),
    _OduClientCtpTermDMPSLatencyMode_Type()
)
oduClientCtpTermDMPSLatencyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTermDMPSLatencyMode.setStatus("current")
_OduClientCtpFacDMPELatHighThreshold_Type = FloatTenths
_OduClientCtpFacDMPELatHighThreshold_Object = MibTableColumn
oduClientCtpFacDMPELatHighThreshold = _OduClientCtpFacDMPELatHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 72),
    _OduClientCtpFacDMPELatHighThreshold_Type()
)
oduClientCtpFacDMPELatHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpFacDMPELatHighThreshold.setStatus("current")
_OduClientCtpFacDMPELatLowThreshold_Type = FloatTenths
_OduClientCtpFacDMPELatLowThreshold_Object = MibTableColumn
oduClientCtpFacDMPELatLowThreshold = _OduClientCtpFacDMPELatLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 73),
    _OduClientCtpFacDMPELatLowThreshold_Type()
)
oduClientCtpFacDMPELatLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpFacDMPELatLowThreshold.setStatus("current")
_OduClientCtpTermDMPELatHighThreshold_Type = FloatTenths
_OduClientCtpTermDMPELatHighThreshold_Object = MibTableColumn
oduClientCtpTermDMPELatHighThreshold = _OduClientCtpTermDMPELatHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 74),
    _OduClientCtpTermDMPELatHighThreshold_Type()
)
oduClientCtpTermDMPELatHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTermDMPELatHighThreshold.setStatus("current")
_OduClientCtpTermDMPELatLowThreshold_Type = FloatTenths
_OduClientCtpTermDMPELatLowThreshold_Object = MibTableColumn
oduClientCtpTermDMPELatLowThreshold = _OduClientCtpTermDMPELatLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 75),
    _OduClientCtpTermDMPELatLowThreshold_Type()
)
oduClientCtpTermDMPELatLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTermDMPELatLowThreshold.setStatus("current")
_OduClientCtpFacDMPSLatHighThreshold_Type = FloatTenths
_OduClientCtpFacDMPSLatHighThreshold_Object = MibTableColumn
oduClientCtpFacDMPSLatHighThreshold = _OduClientCtpFacDMPSLatHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 76),
    _OduClientCtpFacDMPSLatHighThreshold_Type()
)
oduClientCtpFacDMPSLatHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpFacDMPSLatHighThreshold.setStatus("current")
_OduClientCtpFacDMPSLatLowThreshold_Type = FloatTenths
_OduClientCtpFacDMPSLatLowThreshold_Object = MibTableColumn
oduClientCtpFacDMPSLatLowThreshold = _OduClientCtpFacDMPSLatLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 77),
    _OduClientCtpFacDMPSLatLowThreshold_Type()
)
oduClientCtpFacDMPSLatLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpFacDMPSLatLowThreshold.setStatus("current")
_OduClientCtpTermDMPSLatHighThreshold_Type = FloatTenths
_OduClientCtpTermDMPSLatHighThreshold_Object = MibTableColumn
oduClientCtpTermDMPSLatHighThreshold = _OduClientCtpTermDMPSLatHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 78),
    _OduClientCtpTermDMPSLatHighThreshold_Type()
)
oduClientCtpTermDMPSLatHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTermDMPSLatHighThreshold.setStatus("current")
_OduClientCtpTermDMPSLatLowThreshold_Type = FloatTenths
_OduClientCtpTermDMPSLatLowThreshold_Object = MibTableColumn
oduClientCtpTermDMPSLatLowThreshold = _OduClientCtpTermDMPSLatLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 79),
    _OduClientCtpTermDMPSLatLowThreshold_Type()
)
oduClientCtpTermDMPSLatLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpTermDMPSLatLowThreshold.setStatus("current")
_OduClientCtpDetectedTPNList_Type = DisplayString
_OduClientCtpDetectedTPNList_Object = MibTableColumn
oduClientCtpDetectedTPNList = _OduClientCtpDetectedTPNList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 1, 1, 80),
    _OduClientCtpDetectedTPNList_Type()
)
oduClientCtpDetectedTPNList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oduClientCtpDetectedTPNList.setStatus("current")
_OduClientCtpConformance_ObjectIdentity = ObjectIdentity
oduClientCtpConformance = _OduClientCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 3)
)
_OduClientCtpCompliances_ObjectIdentity = ObjectIdentity
oduClientCtpCompliances = _OduClientCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 3, 1)
)
_OduClientCtpGroups_ObjectIdentity = ObjectIdentity
oduClientCtpGroups = _OduClientCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 3, 2)
)

# Managed Objects groups

oduClientCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 3, 2, 1)
)
oduClientCtpGroup.setObjects(
      *(("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpServiceMode"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpFacMonitoringMode"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpFacTxTTI"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpFacExpectedSAPI"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpFacExpectedDAPI"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTermTxTTI"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTermExpectedSAPI"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTermExpectedDAPI"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpFacReceivedTTI"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTermReceivedTTI"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpRxEb15MinutesTce"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTxEb15MinutesTce"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpRxEbDayTce"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTxEbDayTce"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpRxDs15MinutesTce"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTxDs15MinutesTce"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpRxDsDayTce"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTxDsDayTce"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpRxEbDayTceReporting"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpRxEb15MinutesTceReporting"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTxEbDayTceReporting"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTxEb15MinutesTceReporting"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpRxDsDayTceReporting"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpRxDs15MinutesTceReporting"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTxDsDayTceReporting"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTxDs15MinutesTceReporting"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpFacTimDetMode"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTermTimDetMode"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTcmList"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpConfiguredServiceType"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTamType"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpFacPmHistStatsEnable"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTermPmHistStatsEnable"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpAlarmReportControl"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpSupportingCircuitIdList"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpFacDSThreshold"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTermDSThreshold"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpRxBei15MinutesTce"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTxBei15MinutesTce"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpRxBeiDayTce"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTxBeiDayTce"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpRxBeiDayTceReporting"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpRxBei15MinutesTceReporting"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTxBeiDayTceReporting"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTxBei15MinutesTceReporting"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTermMonitoringMode"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTSCount"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtprate"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTributaryPortNumber"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpExpectedTPNs"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpDetectedTPNs"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpuserConfigured"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpsupportingOPUTributarySlots"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpavailableOPUTributarySlots"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpdatarate"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpCrossConnectType"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpSupportingTP"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTsg"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpExpectedPayload"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpLoopBack"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpFacSDThreshold"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpFacPrbsGenMode"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpFacPrbsMonMode"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTermPrbsGenMode"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTermPrbsMonMode"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpDetectedPayloadType"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpFacDMPELatencyMode"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpFacDMPSLatencyMode"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTermDMPELatencyMode"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTermDMPSLatencyMode"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpFacDMPELatHighThreshold"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpFacDMPELatLowThreshold"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTermDMPELatHighThreshold"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTermDMPELatLowThreshold"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpFacDMPSLatHighThreshold"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpFacDMPSLatLowThreshold"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTermDMPSLatHighThreshold"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpTermDMPSLatLowThreshold"),
        ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpDetectedTPNList"))
)
if mibBuilder.loadTexts:
    oduClientCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oduClientCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 23, 3, 1, 1)
)
oduClientCtpCompliance.setObjects(
    ("INFINERA-TP-ODUCLIENTCTP-MIB", "oduClientCtpGroup")
)
if mibBuilder.loadTexts:
    oduClientCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-ODUCLIENTCTP-MIB",
    **{"oduClientCtpMIB": oduClientCtpMIB,
       "oduClientCtpTable": oduClientCtpTable,
       "oduClientCtpEntry": oduClientCtpEntry,
       "oduClientCtpServiceMode": oduClientCtpServiceMode,
       "oduClientCtpServiceModeQualifier": oduClientCtpServiceModeQualifier,
       "oduClientCtpFacMonitoringMode": oduClientCtpFacMonitoringMode,
       "oduClientCtpFacTxTTI": oduClientCtpFacTxTTI,
       "oduClientCtpFacExpectedSAPI": oduClientCtpFacExpectedSAPI,
       "oduClientCtpFacExpectedDAPI": oduClientCtpFacExpectedDAPI,
       "oduClientCtpTermTxTTI": oduClientCtpTermTxTTI,
       "oduClientCtpTermExpectedSAPI": oduClientCtpTermExpectedSAPI,
       "oduClientCtpTermExpectedDAPI": oduClientCtpTermExpectedDAPI,
       "oduClientCtpFacReceivedTTI": oduClientCtpFacReceivedTTI,
       "oduClientCtpTermReceivedTTI": oduClientCtpTermReceivedTTI,
       "oduClientCtpRxEb15MinutesTce": oduClientCtpRxEb15MinutesTce,
       "oduClientCtpTxEb15MinutesTce": oduClientCtpTxEb15MinutesTce,
       "oduClientCtpRxEbDayTce": oduClientCtpRxEbDayTce,
       "oduClientCtpTxEbDayTce": oduClientCtpTxEbDayTce,
       "oduClientCtpRxDs15MinutesTce": oduClientCtpRxDs15MinutesTce,
       "oduClientCtpTxDs15MinutesTce": oduClientCtpTxDs15MinutesTce,
       "oduClientCtpRxDsDayTce": oduClientCtpRxDsDayTce,
       "oduClientCtpTxDsDayTce": oduClientCtpTxDsDayTce,
       "oduClientCtpRxEbDayTceReporting": oduClientCtpRxEbDayTceReporting,
       "oduClientCtpRxEb15MinutesTceReporting": oduClientCtpRxEb15MinutesTceReporting,
       "oduClientCtpTxEbDayTceReporting": oduClientCtpTxEbDayTceReporting,
       "oduClientCtpTxEb15MinutesTceReporting": oduClientCtpTxEb15MinutesTceReporting,
       "oduClientCtpRxDsDayTceReporting": oduClientCtpRxDsDayTceReporting,
       "oduClientCtpRxDs15MinutesTceReporting": oduClientCtpRxDs15MinutesTceReporting,
       "oduClientCtpTxDsDayTceReporting": oduClientCtpTxDsDayTceReporting,
       "oduClientCtpTxDs15MinutesTceReporting": oduClientCtpTxDs15MinutesTceReporting,
       "oduClientCtpFacTimDetMode": oduClientCtpFacTimDetMode,
       "oduClientCtpTermTimDetMode": oduClientCtpTermTimDetMode,
       "oduClientCtpTcmList": oduClientCtpTcmList,
       "oduClientCtpConfiguredServiceType": oduClientCtpConfiguredServiceType,
       "oduClientCtpTamType": oduClientCtpTamType,
       "oduClientCtpFacPmHistStatsEnable": oduClientCtpFacPmHistStatsEnable,
       "oduClientCtpTermPmHistStatsEnable": oduClientCtpTermPmHistStatsEnable,
       "oduClientCtpAlarmReportControl": oduClientCtpAlarmReportControl,
       "oduClientCtpSupportingCircuitIdList": oduClientCtpSupportingCircuitIdList,
       "oduClientCtpFacDSThreshold": oduClientCtpFacDSThreshold,
       "oduClientCtpTermDSThreshold": oduClientCtpTermDSThreshold,
       "oduClientCtpTermMonitoringMode": oduClientCtpTermMonitoringMode,
       "oduClientCtpRxBei15MinutesTce": oduClientCtpRxBei15MinutesTce,
       "oduClientCtpTxBei15MinutesTce": oduClientCtpTxBei15MinutesTce,
       "oduClientCtpRxBeiDayTce": oduClientCtpRxBeiDayTce,
       "oduClientCtpTxBeiDayTce": oduClientCtpTxBeiDayTce,
       "oduClientCtpRxBeiDayTceReporting": oduClientCtpRxBeiDayTceReporting,
       "oduClientCtpRxBei15MinutesTceReporting": oduClientCtpRxBei15MinutesTceReporting,
       "oduClientCtpTxBeiDayTceReporting": oduClientCtpTxBeiDayTceReporting,
       "oduClientCtpTxBei15MinutesTceReporting": oduClientCtpTxBei15MinutesTceReporting,
       "oduClientCtpTSCount": oduClientCtpTSCount,
       "oduClientCtprate": oduClientCtprate,
       "oduClientCtpTributaryPortNumber": oduClientCtpTributaryPortNumber,
       "oduClientCtpExpectedTPNs": oduClientCtpExpectedTPNs,
       "oduClientCtpDetectedTPNs": oduClientCtpDetectedTPNs,
       "oduClientCtpuserConfigured": oduClientCtpuserConfigured,
       "oduClientCtpsupportingOPUTributarySlots": oduClientCtpsupportingOPUTributarySlots,
       "oduClientCtpavailableOPUTributarySlots": oduClientCtpavailableOPUTributarySlots,
       "oduClientCtpdatarate": oduClientCtpdatarate,
       "oduClientCtpCrossConnectType": oduClientCtpCrossConnectType,
       "oduClientCtpSupportingTP": oduClientCtpSupportingTP,
       "oduClientCtpTsg": oduClientCtpTsg,
       "oduClientCtpExpectedPayload": oduClientCtpExpectedPayload,
       "oduClientCtpLoopBack": oduClientCtpLoopBack,
       "oduClientCtpFacSDThreshold": oduClientCtpFacSDThreshold,
       "oduClientCtpFacPrbsGenMode": oduClientCtpFacPrbsGenMode,
       "oduClientCtpFacPrbsMonMode": oduClientCtpFacPrbsMonMode,
       "oduClientCtpTermPrbsGenMode": oduClientCtpTermPrbsGenMode,
       "oduClientCtpTermPrbsMonMode": oduClientCtpTermPrbsMonMode,
       "oduClientCtpDetectedPayloadType": oduClientCtpDetectedPayloadType,
       "oduClientCtpFacDMPELatencyMode": oduClientCtpFacDMPELatencyMode,
       "oduClientCtpFacDMPSLatencyMode": oduClientCtpFacDMPSLatencyMode,
       "oduClientCtpTermDMPELatencyMode": oduClientCtpTermDMPELatencyMode,
       "oduClientCtpTermDMPSLatencyMode": oduClientCtpTermDMPSLatencyMode,
       "oduClientCtpFacDMPELatHighThreshold": oduClientCtpFacDMPELatHighThreshold,
       "oduClientCtpFacDMPELatLowThreshold": oduClientCtpFacDMPELatLowThreshold,
       "oduClientCtpTermDMPELatHighThreshold": oduClientCtpTermDMPELatHighThreshold,
       "oduClientCtpTermDMPELatLowThreshold": oduClientCtpTermDMPELatLowThreshold,
       "oduClientCtpFacDMPSLatHighThreshold": oduClientCtpFacDMPSLatHighThreshold,
       "oduClientCtpFacDMPSLatLowThreshold": oduClientCtpFacDMPSLatLowThreshold,
       "oduClientCtpTermDMPSLatHighThreshold": oduClientCtpTermDMPSLatHighThreshold,
       "oduClientCtpTermDMPSLatLowThreshold": oduClientCtpTermDMPSLatLowThreshold,
       "oduClientCtpDetectedTPNList": oduClientCtpDetectedTPNList,
       "oduClientCtpConformance": oduClientCtpConformance,
       "oduClientCtpCompliances": oduClientCtpCompliances,
       "oduClientCtpCompliance": oduClientCtpCompliance,
       "oduClientCtpGroups": oduClientCtpGroups,
       "oduClientCtpGroup": oduClientCtpGroup}
)
