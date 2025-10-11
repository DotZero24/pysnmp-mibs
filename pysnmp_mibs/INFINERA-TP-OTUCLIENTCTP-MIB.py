# SNMP MIB module (INFINERA-TP-OTUCLIENTCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-OTUCLIENTCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:27 2025
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

(InfnArc,
 InfnEnableDisable,
 InfnEqptType,
 InfnLoopbackType,
 InfnMonitoringMode,
 InfnSMQ,
 InfnServiceMode,
 InfnServiceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnArc",
    "InfnEnableDisable",
    "InfnEqptType",
    "InfnLoopbackType",
    "InfnMonitoringMode",
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

otuClientCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25)
)
if mibBuilder.loadTexts:
    otuClientCtpMIB.setRevisions(
        ("2009-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OtuClientCtpTable_Object = MibTable
otuClientCtpTable = _OtuClientCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1)
)
if mibBuilder.loadTexts:
    otuClientCtpTable.setStatus("current")
_OtuClientCtpEntry_Object = MibTableRow
otuClientCtpEntry = _OtuClientCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1)
)
otuClientCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    otuClientCtpEntry.setStatus("current")


class _OtuClientCtpFacPrbsGenMode_Type(InfnEnableDisable):
    """Custom type otuClientCtpFacPrbsGenMode based on InfnEnableDisable"""
    defaultValue = 1


_OtuClientCtpFacPrbsGenMode_Type.__name__ = "InfnEnableDisable"
_OtuClientCtpFacPrbsGenMode_Object = MibTableColumn
otuClientCtpFacPrbsGenMode = _OtuClientCtpFacPrbsGenMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 1),
    _OtuClientCtpFacPrbsGenMode_Type()
)
otuClientCtpFacPrbsGenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpFacPrbsGenMode.setStatus("current")


class _OtuClientCtpFacPrbsMonMode_Type(InfnEnableDisable):
    """Custom type otuClientCtpFacPrbsMonMode based on InfnEnableDisable"""
    defaultValue = 1


_OtuClientCtpFacPrbsMonMode_Type.__name__ = "InfnEnableDisable"
_OtuClientCtpFacPrbsMonMode_Object = MibTableColumn
otuClientCtpFacPrbsMonMode = _OtuClientCtpFacPrbsMonMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 2),
    _OtuClientCtpFacPrbsMonMode_Type()
)
otuClientCtpFacPrbsMonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpFacPrbsMonMode.setStatus("current")


class _OtuClientCtpServiceMode_Type(InfnServiceMode):
    """Custom type otuClientCtpServiceMode based on InfnServiceMode"""
    defaultValue = 1


_OtuClientCtpServiceMode_Type.__name__ = "InfnServiceMode"
_OtuClientCtpServiceMode_Object = MibTableColumn
otuClientCtpServiceMode = _OtuClientCtpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 3),
    _OtuClientCtpServiceMode_Type()
)
otuClientCtpServiceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuClientCtpServiceMode.setStatus("current")


class _OtuClientCtpServiceModeQualifier_Type(InfnSMQ):
    """Custom type otuClientCtpServiceModeQualifier based on InfnSMQ"""
    defaultValue = 1


_OtuClientCtpServiceModeQualifier_Type.__name__ = "InfnSMQ"
_OtuClientCtpServiceModeQualifier_Object = MibTableColumn
otuClientCtpServiceModeQualifier = _OtuClientCtpServiceModeQualifier_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 4),
    _OtuClientCtpServiceModeQualifier_Type()
)
otuClientCtpServiceModeQualifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuClientCtpServiceModeQualifier.setStatus("current")


class _OtuClientCtpFecCorrection_Type(InfnEnableDisable):
    """Custom type otuClientCtpFecCorrection based on InfnEnableDisable"""
    defaultValue = 2


_OtuClientCtpFecCorrection_Type.__name__ = "InfnEnableDisable"
_OtuClientCtpFecCorrection_Object = MibTableColumn
otuClientCtpFecCorrection = _OtuClientCtpFecCorrection_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 5),
    _OtuClientCtpFecCorrection_Type()
)
otuClientCtpFecCorrection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpFecCorrection.setStatus("current")


class _OtuClientCtpFecEnabled_Type(InfnEnableDisable):
    """Custom type otuClientCtpFecEnabled based on InfnEnableDisable"""
    defaultValue = 2


_OtuClientCtpFecEnabled_Type.__name__ = "InfnEnableDisable"
_OtuClientCtpFecEnabled_Object = MibTableColumn
otuClientCtpFecEnabled = _OtuClientCtpFecEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 6),
    _OtuClientCtpFecEnabled_Type()
)
otuClientCtpFecEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpFecEnabled.setStatus("current")


class _OtuClientCtpTermTxTTI_Type(DisplayString):
    """Custom type otuClientCtpTermTxTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OtuClientCtpTermTxTTI_Type.__name__ = "DisplayString"
_OtuClientCtpTermTxTTI_Object = MibTableColumn
otuClientCtpTermTxTTI = _OtuClientCtpTermTxTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 7),
    _OtuClientCtpTermTxTTI_Type()
)
otuClientCtpTermTxTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTermTxTTI.setStatus("current")


class _OtuClientCtpTermExpectedSAPI_Type(DisplayString):
    """Custom type otuClientCtpTermExpectedSAPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_OtuClientCtpTermExpectedSAPI_Type.__name__ = "DisplayString"
_OtuClientCtpTermExpectedSAPI_Object = MibTableColumn
otuClientCtpTermExpectedSAPI = _OtuClientCtpTermExpectedSAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 8),
    _OtuClientCtpTermExpectedSAPI_Type()
)
otuClientCtpTermExpectedSAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTermExpectedSAPI.setStatus("current")


class _OtuClientCtpTermExpectedDAPI_Type(DisplayString):
    """Custom type otuClientCtpTermExpectedDAPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_OtuClientCtpTermExpectedDAPI_Type.__name__ = "DisplayString"
_OtuClientCtpTermExpectedDAPI_Object = MibTableColumn
otuClientCtpTermExpectedDAPI = _OtuClientCtpTermExpectedDAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 9),
    _OtuClientCtpTermExpectedDAPI_Type()
)
otuClientCtpTermExpectedDAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTermExpectedDAPI.setStatus("current")


class _OtuClientCtpFacTxTTI_Type(DisplayString):
    """Custom type otuClientCtpFacTxTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OtuClientCtpFacTxTTI_Type.__name__ = "DisplayString"
_OtuClientCtpFacTxTTI_Object = MibTableColumn
otuClientCtpFacTxTTI = _OtuClientCtpFacTxTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 10),
    _OtuClientCtpFacTxTTI_Type()
)
otuClientCtpFacTxTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpFacTxTTI.setStatus("current")


class _OtuClientCtpFacExpectedSAPI_Type(DisplayString):
    """Custom type otuClientCtpFacExpectedSAPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_OtuClientCtpFacExpectedSAPI_Type.__name__ = "DisplayString"
_OtuClientCtpFacExpectedSAPI_Object = MibTableColumn
otuClientCtpFacExpectedSAPI = _OtuClientCtpFacExpectedSAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 11),
    _OtuClientCtpFacExpectedSAPI_Type()
)
otuClientCtpFacExpectedSAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpFacExpectedSAPI.setStatus("current")


class _OtuClientCtpFacExpectedDAPI_Type(DisplayString):
    """Custom type otuClientCtpFacExpectedDAPI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_OtuClientCtpFacExpectedDAPI_Type.__name__ = "DisplayString"
_OtuClientCtpFacExpectedDAPI_Object = MibTableColumn
otuClientCtpFacExpectedDAPI = _OtuClientCtpFacExpectedDAPI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 12),
    _OtuClientCtpFacExpectedDAPI_Type()
)
otuClientCtpFacExpectedDAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpFacExpectedDAPI.setStatus("current")


class _OtuClientCtpTermReceivedTTI_Type(DisplayString):
    """Custom type otuClientCtpTermReceivedTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OtuClientCtpTermReceivedTTI_Type.__name__ = "DisplayString"
_OtuClientCtpTermReceivedTTI_Object = MibTableColumn
otuClientCtpTermReceivedTTI = _OtuClientCtpTermReceivedTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 13),
    _OtuClientCtpTermReceivedTTI_Type()
)
otuClientCtpTermReceivedTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuClientCtpTermReceivedTTI.setStatus("current")


class _OtuClientCtpFacReceivedTTI_Type(DisplayString):
    """Custom type otuClientCtpFacReceivedTTI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_OtuClientCtpFacReceivedTTI_Type.__name__ = "DisplayString"
_OtuClientCtpFacReceivedTTI_Object = MibTableColumn
otuClientCtpFacReceivedTTI = _OtuClientCtpFacReceivedTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 14),
    _OtuClientCtpFacReceivedTTI_Type()
)
otuClientCtpFacReceivedTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuClientCtpFacReceivedTTI.setStatus("current")


class _OtuClientCtpRxEb15MinutesTce_Type(Integer32):
    """Custom type otuClientCtpRxEb15MinutesTce based on Integer32"""
    defaultValue = 1500


_OtuClientCtpRxEb15MinutesTce_Type.__name__ = "Integer32"
_OtuClientCtpRxEb15MinutesTce_Object = MibTableColumn
otuClientCtpRxEb15MinutesTce = _OtuClientCtpRxEb15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 15),
    _OtuClientCtpRxEb15MinutesTce_Type()
)
otuClientCtpRxEb15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpRxEb15MinutesTce.setStatus("current")


class _OtuClientCtpTxEb15MinutesTce_Type(Integer32):
    """Custom type otuClientCtpTxEb15MinutesTce based on Integer32"""
    defaultValue = 1500


_OtuClientCtpTxEb15MinutesTce_Type.__name__ = "Integer32"
_OtuClientCtpTxEb15MinutesTce_Object = MibTableColumn
otuClientCtpTxEb15MinutesTce = _OtuClientCtpTxEb15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 16),
    _OtuClientCtpTxEb15MinutesTce_Type()
)
otuClientCtpTxEb15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTxEb15MinutesTce.setStatus("current")


class _OtuClientCtpRxEbDayTce_Type(Integer32):
    """Custom type otuClientCtpRxEbDayTce based on Integer32"""
    defaultValue = 15000


_OtuClientCtpRxEbDayTce_Type.__name__ = "Integer32"
_OtuClientCtpRxEbDayTce_Object = MibTableColumn
otuClientCtpRxEbDayTce = _OtuClientCtpRxEbDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 17),
    _OtuClientCtpRxEbDayTce_Type()
)
otuClientCtpRxEbDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpRxEbDayTce.setStatus("current")


class _OtuClientCtpTxEbDayTce_Type(Integer32):
    """Custom type otuClientCtpTxEbDayTce based on Integer32"""
    defaultValue = 15000


_OtuClientCtpTxEbDayTce_Type.__name__ = "Integer32"
_OtuClientCtpTxEbDayTce_Object = MibTableColumn
otuClientCtpTxEbDayTce = _OtuClientCtpTxEbDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 18),
    _OtuClientCtpTxEbDayTce_Type()
)
otuClientCtpTxEbDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTxEbDayTce.setStatus("current")


class _OtuClientCtpRxDs15MinutesTce_Type(Integer32):
    """Custom type otuClientCtpRxDs15MinutesTce based on Integer32"""
    defaultValue = 120


_OtuClientCtpRxDs15MinutesTce_Type.__name__ = "Integer32"
_OtuClientCtpRxDs15MinutesTce_Object = MibTableColumn
otuClientCtpRxDs15MinutesTce = _OtuClientCtpRxDs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 19),
    _OtuClientCtpRxDs15MinutesTce_Type()
)
otuClientCtpRxDs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpRxDs15MinutesTce.setStatus("current")


class _OtuClientCtpTxDs15MinutesTce_Type(Integer32):
    """Custom type otuClientCtpTxDs15MinutesTce based on Integer32"""
    defaultValue = 120


_OtuClientCtpTxDs15MinutesTce_Type.__name__ = "Integer32"
_OtuClientCtpTxDs15MinutesTce_Object = MibTableColumn
otuClientCtpTxDs15MinutesTce = _OtuClientCtpTxDs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 20),
    _OtuClientCtpTxDs15MinutesTce_Type()
)
otuClientCtpTxDs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTxDs15MinutesTce.setStatus("current")


class _OtuClientCtpRxDsDayTce_Type(Integer32):
    """Custom type otuClientCtpRxDsDayTce based on Integer32"""
    defaultValue = 1200


_OtuClientCtpRxDsDayTce_Type.__name__ = "Integer32"
_OtuClientCtpRxDsDayTce_Object = MibTableColumn
otuClientCtpRxDsDayTce = _OtuClientCtpRxDsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 21),
    _OtuClientCtpRxDsDayTce_Type()
)
otuClientCtpRxDsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpRxDsDayTce.setStatus("current")


class _OtuClientCtpTxDsDayTce_Type(Integer32):
    """Custom type otuClientCtpTxDsDayTce based on Integer32"""
    defaultValue = 1200


_OtuClientCtpTxDsDayTce_Type.__name__ = "Integer32"
_OtuClientCtpTxDsDayTce_Object = MibTableColumn
otuClientCtpTxDsDayTce = _OtuClientCtpTxDsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 22),
    _OtuClientCtpTxDsDayTce_Type()
)
otuClientCtpTxDsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTxDsDayTce.setStatus("current")


class _OtuClientCtpRxEbDayTceReporting_Type(TruthValue):
    """Custom type otuClientCtpRxEbDayTceReporting based on TruthValue"""
    defaultValue = 2


_OtuClientCtpRxEbDayTceReporting_Type.__name__ = "TruthValue"
_OtuClientCtpRxEbDayTceReporting_Object = MibTableColumn
otuClientCtpRxEbDayTceReporting = _OtuClientCtpRxEbDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 23),
    _OtuClientCtpRxEbDayTceReporting_Type()
)
otuClientCtpRxEbDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpRxEbDayTceReporting.setStatus("current")


class _OtuClientCtpRxEb15MinutesTceReporting_Type(TruthValue):
    """Custom type otuClientCtpRxEb15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OtuClientCtpRxEb15MinutesTceReporting_Type.__name__ = "TruthValue"
_OtuClientCtpRxEb15MinutesTceReporting_Object = MibTableColumn
otuClientCtpRxEb15MinutesTceReporting = _OtuClientCtpRxEb15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 24),
    _OtuClientCtpRxEb15MinutesTceReporting_Type()
)
otuClientCtpRxEb15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpRxEb15MinutesTceReporting.setStatus("current")


class _OtuClientCtpTxEbDayTceReporting_Type(TruthValue):
    """Custom type otuClientCtpTxEbDayTceReporting based on TruthValue"""
    defaultValue = 2


_OtuClientCtpTxEbDayTceReporting_Type.__name__ = "TruthValue"
_OtuClientCtpTxEbDayTceReporting_Object = MibTableColumn
otuClientCtpTxEbDayTceReporting = _OtuClientCtpTxEbDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 25),
    _OtuClientCtpTxEbDayTceReporting_Type()
)
otuClientCtpTxEbDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTxEbDayTceReporting.setStatus("current")


class _OtuClientCtpTxEb15MinutesTceReporting_Type(TruthValue):
    """Custom type otuClientCtpTxEb15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OtuClientCtpTxEb15MinutesTceReporting_Type.__name__ = "TruthValue"
_OtuClientCtpTxEb15MinutesTceReporting_Object = MibTableColumn
otuClientCtpTxEb15MinutesTceReporting = _OtuClientCtpTxEb15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 26),
    _OtuClientCtpTxEb15MinutesTceReporting_Type()
)
otuClientCtpTxEb15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTxEb15MinutesTceReporting.setStatus("current")


class _OtuClientCtpRxDsDayTceReporting_Type(TruthValue):
    """Custom type otuClientCtpRxDsDayTceReporting based on TruthValue"""
    defaultValue = 2


_OtuClientCtpRxDsDayTceReporting_Type.__name__ = "TruthValue"
_OtuClientCtpRxDsDayTceReporting_Object = MibTableColumn
otuClientCtpRxDsDayTceReporting = _OtuClientCtpRxDsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 27),
    _OtuClientCtpRxDsDayTceReporting_Type()
)
otuClientCtpRxDsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpRxDsDayTceReporting.setStatus("current")


class _OtuClientCtpRxDs15MinutesTceReporting_Type(TruthValue):
    """Custom type otuClientCtpRxDs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OtuClientCtpRxDs15MinutesTceReporting_Type.__name__ = "TruthValue"
_OtuClientCtpRxDs15MinutesTceReporting_Object = MibTableColumn
otuClientCtpRxDs15MinutesTceReporting = _OtuClientCtpRxDs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 28),
    _OtuClientCtpRxDs15MinutesTceReporting_Type()
)
otuClientCtpRxDs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpRxDs15MinutesTceReporting.setStatus("current")


class _OtuClientCtpTxDsDayTceReporting_Type(TruthValue):
    """Custom type otuClientCtpTxDsDayTceReporting based on TruthValue"""
    defaultValue = 2


_OtuClientCtpTxDsDayTceReporting_Type.__name__ = "TruthValue"
_OtuClientCtpTxDsDayTceReporting_Object = MibTableColumn
otuClientCtpTxDsDayTceReporting = _OtuClientCtpTxDsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 29),
    _OtuClientCtpTxDsDayTceReporting_Type()
)
otuClientCtpTxDsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTxDsDayTceReporting.setStatus("current")


class _OtuClientCtpTxDs15MinutesTceReporting_Type(TruthValue):
    """Custom type otuClientCtpTxDs15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OtuClientCtpTxDs15MinutesTceReporting_Type.__name__ = "TruthValue"
_OtuClientCtpTxDs15MinutesTceReporting_Object = MibTableColumn
otuClientCtpTxDs15MinutesTceReporting = _OtuClientCtpTxDs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 30),
    _OtuClientCtpTxDs15MinutesTceReporting_Type()
)
otuClientCtpTxDs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTxDs15MinutesTceReporting.setStatus("current")


class _OtuClientCtpTermTimDetMode_Type(Integer32):
    """Custom type otuClientCtpTermTimDetMode based on Integer32"""
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


_OtuClientCtpTermTimDetMode_Type.__name__ = "Integer32"
_OtuClientCtpTermTimDetMode_Object = MibTableColumn
otuClientCtpTermTimDetMode = _OtuClientCtpTermTimDetMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 31),
    _OtuClientCtpTermTimDetMode_Type()
)
otuClientCtpTermTimDetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTermTimDetMode.setStatus("current")


class _OtuClientCtpFacTimDetMode_Type(Integer32):
    """Custom type otuClientCtpFacTimDetMode based on Integer32"""
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


_OtuClientCtpFacTimDetMode_Type.__name__ = "Integer32"
_OtuClientCtpFacTimDetMode_Object = MibTableColumn
otuClientCtpFacTimDetMode = _OtuClientCtpFacTimDetMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 32),
    _OtuClientCtpFacTimDetMode_Type()
)
otuClientCtpFacTimDetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpFacTimDetMode.setStatus("current")
_OtuClientCtpConfiguredServiceType_Type = InfnServiceType
_OtuClientCtpConfiguredServiceType_Object = MibTableColumn
otuClientCtpConfiguredServiceType = _OtuClientCtpConfiguredServiceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 33),
    _OtuClientCtpConfiguredServiceType_Type()
)
otuClientCtpConfiguredServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuClientCtpConfiguredServiceType.setStatus("current")
_OtuClientCtpTamType_Type = InfnEqptType
_OtuClientCtpTamType_Object = MibTableColumn
otuClientCtpTamType = _OtuClientCtpTamType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 34),
    _OtuClientCtpTamType_Type()
)
otuClientCtpTamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuClientCtpTamType.setStatus("obsolete")


class _OtuClientCtpLoopback_Type(InfnLoopbackType):
    """Custom type otuClientCtpLoopback based on InfnLoopbackType"""
    defaultValue = 1


_OtuClientCtpLoopback_Type.__name__ = "InfnLoopbackType"
_OtuClientCtpLoopback_Object = MibTableColumn
otuClientCtpLoopback = _OtuClientCtpLoopback_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 35),
    _OtuClientCtpLoopback_Type()
)
otuClientCtpLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpLoopback.setStatus("current")


class _OtuClientCtpFacPmHistStatsEnable_Type(InfnEnableDisable):
    """Custom type otuClientCtpFacPmHistStatsEnable based on InfnEnableDisable"""
    defaultValue = 2


_OtuClientCtpFacPmHistStatsEnable_Type.__name__ = "InfnEnableDisable"
_OtuClientCtpFacPmHistStatsEnable_Object = MibTableColumn
otuClientCtpFacPmHistStatsEnable = _OtuClientCtpFacPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 36),
    _OtuClientCtpFacPmHistStatsEnable_Type()
)
otuClientCtpFacPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpFacPmHistStatsEnable.setStatus("current")


class _OtuClientCtpTermPmHistStatsEnable_Type(InfnEnableDisable):
    """Custom type otuClientCtpTermPmHistStatsEnable based on InfnEnableDisable"""
    defaultValue = 2


_OtuClientCtpTermPmHistStatsEnable_Type.__name__ = "InfnEnableDisable"
_OtuClientCtpTermPmHistStatsEnable_Object = MibTableColumn
otuClientCtpTermPmHistStatsEnable = _OtuClientCtpTermPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 37),
    _OtuClientCtpTermPmHistStatsEnable_Type()
)
otuClientCtpTermPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTermPmHistStatsEnable.setStatus("current")


class _OtuClientCtpAlarmReportControl_Type(InfnArc):
    """Custom type otuClientCtpAlarmReportControl based on InfnArc"""
    defaultValue = 1


_OtuClientCtpAlarmReportControl_Type.__name__ = "InfnArc"
_OtuClientCtpAlarmReportControl_Object = MibTableColumn
otuClientCtpAlarmReportControl = _OtuClientCtpAlarmReportControl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 38),
    _OtuClientCtpAlarmReportControl_Type()
)
otuClientCtpAlarmReportControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpAlarmReportControl.setStatus("current")
_OtuClientCtpSupportingCircuitIdList_Type = DisplayString
_OtuClientCtpSupportingCircuitIdList_Object = MibTableColumn
otuClientCtpSupportingCircuitIdList = _OtuClientCtpSupportingCircuitIdList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 39),
    _OtuClientCtpSupportingCircuitIdList_Type()
)
otuClientCtpSupportingCircuitIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuClientCtpSupportingCircuitIdList.setStatus("current")


class _OtuClientCtpFacDSThreshold_Type(Integer32):
    """Custom type otuClientCtpFacDSThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OtuClientCtpFacDSThreshold_Type.__name__ = "Integer32"
_OtuClientCtpFacDSThreshold_Object = MibTableColumn
otuClientCtpFacDSThreshold = _OtuClientCtpFacDSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 40),
    _OtuClientCtpFacDSThreshold_Type()
)
otuClientCtpFacDSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpFacDSThreshold.setStatus("current")


class _OtuClientCtpTermDSThreshold_Type(Integer32):
    """Custom type otuClientCtpTermDSThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OtuClientCtpTermDSThreshold_Type.__name__ = "Integer32"
_OtuClientCtpTermDSThreshold_Object = MibTableColumn
otuClientCtpTermDSThreshold = _OtuClientCtpTermDSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 41),
    _OtuClientCtpTermDSThreshold_Type()
)
otuClientCtpTermDSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTermDSThreshold.setStatus("current")


class _OtuClientCtpTermPrbsGenMode_Type(InfnEnableDisable):
    """Custom type otuClientCtpTermPrbsGenMode based on InfnEnableDisable"""
    defaultValue = 1


_OtuClientCtpTermPrbsGenMode_Type.__name__ = "InfnEnableDisable"
_OtuClientCtpTermPrbsGenMode_Object = MibTableColumn
otuClientCtpTermPrbsGenMode = _OtuClientCtpTermPrbsGenMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 42),
    _OtuClientCtpTermPrbsGenMode_Type()
)
otuClientCtpTermPrbsGenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTermPrbsGenMode.setStatus("current")


class _OtuClientCtpTermPrbsMonMode_Type(InfnEnableDisable):
    """Custom type otuClientCtpTermPrbsMonMode based on InfnEnableDisable"""
    defaultValue = 1


_OtuClientCtpTermPrbsMonMode_Type.__name__ = "InfnEnableDisable"
_OtuClientCtpTermPrbsMonMode_Object = MibTableColumn
otuClientCtpTermPrbsMonMode = _OtuClientCtpTermPrbsMonMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 43),
    _OtuClientCtpTermPrbsMonMode_Type()
)
otuClientCtpTermPrbsMonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTermPrbsMonMode.setStatus("current")
_OtuClientCtpFacMonitoringMode_Type = InfnMonitoringMode
_OtuClientCtpFacMonitoringMode_Object = MibTableColumn
otuClientCtpFacMonitoringMode = _OtuClientCtpFacMonitoringMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 44),
    _OtuClientCtpFacMonitoringMode_Type()
)
otuClientCtpFacMonitoringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpFacMonitoringMode.setStatus("current")
_OtuClientCtpTermMonitoringMode_Type = InfnMonitoringMode
_OtuClientCtpTermMonitoringMode_Object = MibTableColumn
otuClientCtpTermMonitoringMode = _OtuClientCtpTermMonitoringMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 45),
    _OtuClientCtpTermMonitoringMode_Type()
)
otuClientCtpTermMonitoringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTermMonitoringMode.setStatus("current")


class _OtuClientCtpRxBei15MinutesTce_Type(Integer32):
    """Custom type otuClientCtpRxBei15MinutesTce based on Integer32"""
    defaultValue = 1500


_OtuClientCtpRxBei15MinutesTce_Type.__name__ = "Integer32"
_OtuClientCtpRxBei15MinutesTce_Object = MibTableColumn
otuClientCtpRxBei15MinutesTce = _OtuClientCtpRxBei15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 46),
    _OtuClientCtpRxBei15MinutesTce_Type()
)
otuClientCtpRxBei15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpRxBei15MinutesTce.setStatus("current")


class _OtuClientCtpTxBei15MinutesTce_Type(Integer32):
    """Custom type otuClientCtpTxBei15MinutesTce based on Integer32"""
    defaultValue = 1500


_OtuClientCtpTxBei15MinutesTce_Type.__name__ = "Integer32"
_OtuClientCtpTxBei15MinutesTce_Object = MibTableColumn
otuClientCtpTxBei15MinutesTce = _OtuClientCtpTxBei15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 47),
    _OtuClientCtpTxBei15MinutesTce_Type()
)
otuClientCtpTxBei15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTxBei15MinutesTce.setStatus("current")


class _OtuClientCtpRxBeiDayTce_Type(Integer32):
    """Custom type otuClientCtpRxBeiDayTce based on Integer32"""
    defaultValue = 15000


_OtuClientCtpRxBeiDayTce_Type.__name__ = "Integer32"
_OtuClientCtpRxBeiDayTce_Object = MibTableColumn
otuClientCtpRxBeiDayTce = _OtuClientCtpRxBeiDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 48),
    _OtuClientCtpRxBeiDayTce_Type()
)
otuClientCtpRxBeiDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpRxBeiDayTce.setStatus("current")


class _OtuClientCtpTxBeiDayTce_Type(Integer32):
    """Custom type otuClientCtpTxBeiDayTce based on Integer32"""
    defaultValue = 15000


_OtuClientCtpTxBeiDayTce_Type.__name__ = "Integer32"
_OtuClientCtpTxBeiDayTce_Object = MibTableColumn
otuClientCtpTxBeiDayTce = _OtuClientCtpTxBeiDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 49),
    _OtuClientCtpTxBeiDayTce_Type()
)
otuClientCtpTxBeiDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTxBeiDayTce.setStatus("current")


class _OtuClientCtpRxBeiDayTceReporting_Type(TruthValue):
    """Custom type otuClientCtpRxBeiDayTceReporting based on TruthValue"""
    defaultValue = 2


_OtuClientCtpRxBeiDayTceReporting_Type.__name__ = "TruthValue"
_OtuClientCtpRxBeiDayTceReporting_Object = MibTableColumn
otuClientCtpRxBeiDayTceReporting = _OtuClientCtpRxBeiDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 50),
    _OtuClientCtpRxBeiDayTceReporting_Type()
)
otuClientCtpRxBeiDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpRxBeiDayTceReporting.setStatus("current")


class _OtuClientCtpRxBei15MinutesTceReporting_Type(TruthValue):
    """Custom type otuClientCtpRxBei15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OtuClientCtpRxBei15MinutesTceReporting_Type.__name__ = "TruthValue"
_OtuClientCtpRxBei15MinutesTceReporting_Object = MibTableColumn
otuClientCtpRxBei15MinutesTceReporting = _OtuClientCtpRxBei15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 51),
    _OtuClientCtpRxBei15MinutesTceReporting_Type()
)
otuClientCtpRxBei15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpRxBei15MinutesTceReporting.setStatus("current")


class _OtuClientCtpTxBeiDayTceReporting_Type(TruthValue):
    """Custom type otuClientCtpTxBeiDayTceReporting based on TruthValue"""
    defaultValue = 2


_OtuClientCtpTxBeiDayTceReporting_Type.__name__ = "TruthValue"
_OtuClientCtpTxBeiDayTceReporting_Object = MibTableColumn
otuClientCtpTxBeiDayTceReporting = _OtuClientCtpTxBeiDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 52),
    _OtuClientCtpTxBeiDayTceReporting_Type()
)
otuClientCtpTxBeiDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTxBeiDayTceReporting.setStatus("current")


class _OtuClientCtpTxBei15MinutesTceReporting_Type(TruthValue):
    """Custom type otuClientCtpTxBei15MinutesTceReporting based on TruthValue"""
    defaultValue = 2


_OtuClientCtpTxBei15MinutesTceReporting_Type.__name__ = "TruthValue"
_OtuClientCtpTxBei15MinutesTceReporting_Object = MibTableColumn
otuClientCtpTxBei15MinutesTceReporting = _OtuClientCtpTxBei15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 1, 1, 53),
    _OtuClientCtpTxBei15MinutesTceReporting_Type()
)
otuClientCtpTxBei15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otuClientCtpTxBei15MinutesTceReporting.setStatus("current")
_OtuClientCtpConformance_ObjectIdentity = ObjectIdentity
otuClientCtpConformance = _OtuClientCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 3)
)
_OtuClientCtpCompliances_ObjectIdentity = ObjectIdentity
otuClientCtpCompliances = _OtuClientCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 3, 1)
)
_OtuClientCtpGroups_ObjectIdentity = ObjectIdentity
otuClientCtpGroups = _OtuClientCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 3, 2)
)

# Managed Objects groups

otuClientCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 3, 2, 1)
)
otuClientCtpGroup.setObjects(
      *(("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpFacPrbsGenMode"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpFacPrbsMonMode"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpServiceMode"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpServiceModeQualifier"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpFecCorrection"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpFecEnabled"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpTermTxTTI"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpTermExpectedSAPI"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpTermExpectedDAPI"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpFacTxTTI"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpFacExpectedSAPI"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpFacExpectedDAPI"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpTermReceivedTTI"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpFacReceivedTTI"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpTermTimDetMode"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpFacTimDetMode"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpRxEb15MinutesTce"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpTxEb15MinutesTce"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpRxEbDayTce"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpTxEbDayTce"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpRxDs15MinutesTce"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpTxDs15MinutesTce"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpRxDsDayTce"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpTxDsDayTce"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpRxEbDayTceReporting"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpRxEb15MinutesTceReporting"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpTxEbDayTceReporting"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpTxEb15MinutesTceReporting"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpRxDsDayTceReporting"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpRxDs15MinutesTceReporting"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpTxDsDayTceReporting"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpTxDs15MinutesTceReporting"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpConfiguredServiceType"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpTamType"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpLoopback"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpFacPmHistStatsEnable"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpTermPmHistStatsEnable"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpAlarmReportControl"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpSupportingCircuitIdList"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpFacDSThreshold"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpFacMonitoringMode"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpTermMonitoringMode"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpRxBei15MinutesTce"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpTxBei15MinutesTce"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpRxBeiDayTce"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpTxBeiDayTce"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpRxBeiDayTceReporting"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpRxBei15MinutesTceReporting"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpTxBeiDayTceReporting"),
        ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpTxBei15MinutesTceReporting"))
)
if mibBuilder.loadTexts:
    otuClientCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

otuClientCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 25, 3, 1, 1)
)
otuClientCtpCompliance.setObjects(
    ("INFINERA-TP-OTUCLIENTCTP-MIB", "otuClientCtpGroup")
)
if mibBuilder.loadTexts:
    otuClientCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-OTUCLIENTCTP-MIB",
    **{"otuClientCtpMIB": otuClientCtpMIB,
       "otuClientCtpTable": otuClientCtpTable,
       "otuClientCtpEntry": otuClientCtpEntry,
       "otuClientCtpFacPrbsGenMode": otuClientCtpFacPrbsGenMode,
       "otuClientCtpFacPrbsMonMode": otuClientCtpFacPrbsMonMode,
       "otuClientCtpServiceMode": otuClientCtpServiceMode,
       "otuClientCtpServiceModeQualifier": otuClientCtpServiceModeQualifier,
       "otuClientCtpFecCorrection": otuClientCtpFecCorrection,
       "otuClientCtpFecEnabled": otuClientCtpFecEnabled,
       "otuClientCtpTermTxTTI": otuClientCtpTermTxTTI,
       "otuClientCtpTermExpectedSAPI": otuClientCtpTermExpectedSAPI,
       "otuClientCtpTermExpectedDAPI": otuClientCtpTermExpectedDAPI,
       "otuClientCtpFacTxTTI": otuClientCtpFacTxTTI,
       "otuClientCtpFacExpectedSAPI": otuClientCtpFacExpectedSAPI,
       "otuClientCtpFacExpectedDAPI": otuClientCtpFacExpectedDAPI,
       "otuClientCtpTermReceivedTTI": otuClientCtpTermReceivedTTI,
       "otuClientCtpFacReceivedTTI": otuClientCtpFacReceivedTTI,
       "otuClientCtpRxEb15MinutesTce": otuClientCtpRxEb15MinutesTce,
       "otuClientCtpTxEb15MinutesTce": otuClientCtpTxEb15MinutesTce,
       "otuClientCtpRxEbDayTce": otuClientCtpRxEbDayTce,
       "otuClientCtpTxEbDayTce": otuClientCtpTxEbDayTce,
       "otuClientCtpRxDs15MinutesTce": otuClientCtpRxDs15MinutesTce,
       "otuClientCtpTxDs15MinutesTce": otuClientCtpTxDs15MinutesTce,
       "otuClientCtpRxDsDayTce": otuClientCtpRxDsDayTce,
       "otuClientCtpTxDsDayTce": otuClientCtpTxDsDayTce,
       "otuClientCtpRxEbDayTceReporting": otuClientCtpRxEbDayTceReporting,
       "otuClientCtpRxEb15MinutesTceReporting": otuClientCtpRxEb15MinutesTceReporting,
       "otuClientCtpTxEbDayTceReporting": otuClientCtpTxEbDayTceReporting,
       "otuClientCtpTxEb15MinutesTceReporting": otuClientCtpTxEb15MinutesTceReporting,
       "otuClientCtpRxDsDayTceReporting": otuClientCtpRxDsDayTceReporting,
       "otuClientCtpRxDs15MinutesTceReporting": otuClientCtpRxDs15MinutesTceReporting,
       "otuClientCtpTxDsDayTceReporting": otuClientCtpTxDsDayTceReporting,
       "otuClientCtpTxDs15MinutesTceReporting": otuClientCtpTxDs15MinutesTceReporting,
       "otuClientCtpTermTimDetMode": otuClientCtpTermTimDetMode,
       "otuClientCtpFacTimDetMode": otuClientCtpFacTimDetMode,
       "otuClientCtpConfiguredServiceType": otuClientCtpConfiguredServiceType,
       "otuClientCtpTamType": otuClientCtpTamType,
       "otuClientCtpLoopback": otuClientCtpLoopback,
       "otuClientCtpFacPmHistStatsEnable": otuClientCtpFacPmHistStatsEnable,
       "otuClientCtpTermPmHistStatsEnable": otuClientCtpTermPmHistStatsEnable,
       "otuClientCtpAlarmReportControl": otuClientCtpAlarmReportControl,
       "otuClientCtpSupportingCircuitIdList": otuClientCtpSupportingCircuitIdList,
       "otuClientCtpFacDSThreshold": otuClientCtpFacDSThreshold,
       "otuClientCtpTermDSThreshold": otuClientCtpTermDSThreshold,
       "otuClientCtpTermPrbsGenMode": otuClientCtpTermPrbsGenMode,
       "otuClientCtpTermPrbsMonMode": otuClientCtpTermPrbsMonMode,
       "otuClientCtpFacMonitoringMode": otuClientCtpFacMonitoringMode,
       "otuClientCtpTermMonitoringMode": otuClientCtpTermMonitoringMode,
       "otuClientCtpRxBei15MinutesTce": otuClientCtpRxBei15MinutesTce,
       "otuClientCtpTxBei15MinutesTce": otuClientCtpTxBei15MinutesTce,
       "otuClientCtpRxBeiDayTce": otuClientCtpRxBeiDayTce,
       "otuClientCtpTxBeiDayTce": otuClientCtpTxBeiDayTce,
       "otuClientCtpRxBeiDayTceReporting": otuClientCtpRxBeiDayTceReporting,
       "otuClientCtpRxBei15MinutesTceReporting": otuClientCtpRxBei15MinutesTceReporting,
       "otuClientCtpTxBeiDayTceReporting": otuClientCtpTxBeiDayTceReporting,
       "otuClientCtpTxBei15MinutesTceReporting": otuClientCtpTxBei15MinutesTceReporting,
       "otuClientCtpConformance": otuClientCtpConformance,
       "otuClientCtpCompliances": otuClientCtpCompliances,
       "otuClientCtpCompliance": otuClientCtpCompliance,
       "otuClientCtpGroups": otuClientCtpGroups,
       "otuClientCtpGroup": otuClientCtpGroup}
)
