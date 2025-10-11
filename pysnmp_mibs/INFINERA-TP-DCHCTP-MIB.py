# SNMP MIB module (INFINERA-TP-DCHCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-DCHCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:35 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(InfnLoopbackType,
 InfnServiceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnLoopbackType",
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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

dchCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DchCtpTable_Object = MibTable
dchCtpTable = _DchCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1)
)
if mibBuilder.loadTexts:
    dchCtpTable.setStatus("current")
_DchCtpEntry_Object = MibTableRow
dchCtpEntry = _DchCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1)
)
dchCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dchCtpEntry.setStatus("current")


class _DchCtpTribPrbsGenMode_Type(Integer32):
    """Custom type dchCtpTribPrbsGenMode based on Integer32"""
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
          ("enabled", 2),
          ("unknown", 3))
    )


_DchCtpTribPrbsGenMode_Type.__name__ = "Integer32"
_DchCtpTribPrbsGenMode_Object = MibTableColumn
dchCtpTribPrbsGenMode = _DchCtpTribPrbsGenMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 1),
    _DchCtpTribPrbsGenMode_Type()
)
dchCtpTribPrbsGenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpTribPrbsGenMode.setStatus("current")


class _DchCtpTribPrbsMonMode_Type(Integer32):
    """Custom type dchCtpTribPrbsMonMode based on Integer32"""
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
          ("enabled", 2),
          ("unknown", 3))
    )


_DchCtpTribPrbsMonMode_Type.__name__ = "Integer32"
_DchCtpTribPrbsMonMode_Object = MibTableColumn
dchCtpTribPrbsMonMode = _DchCtpTribPrbsMonMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 2),
    _DchCtpTribPrbsMonMode_Type()
)
dchCtpTribPrbsMonMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpTribPrbsMonMode.setStatus("current")
_DchCtpSupportingCircuitIdList_Type = DisplayString
_DchCtpSupportingCircuitIdList_Object = MibTableColumn
dchCtpSupportingCircuitIdList = _DchCtpSupportingCircuitIdList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 3),
    _DchCtpSupportingCircuitIdList_Type()
)
dchCtpSupportingCircuitIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpSupportingCircuitIdList.setStatus("current")
_DchCtpLoopback_Type = InfnLoopbackType
_DchCtpLoopback_Object = MibTableColumn
dchCtpLoopback = _DchCtpLoopback_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 4),
    _DchCtpLoopback_Type()
)
dchCtpLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpLoopback.setStatus("current")
_DchCtpConfiguredServiceType_Type = InfnServiceType
_DchCtpConfiguredServiceType_Object = MibTableColumn
dchCtpConfiguredServiceType = _DchCtpConfiguredServiceType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 5),
    _DchCtpConfiguredServiceType_Type()
)
dchCtpConfiguredServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpConfiguredServiceType.setStatus("current")
_DchCtpExpectedDtsTTI_Type = DisplayString
_DchCtpExpectedDtsTTI_Object = MibTableColumn
dchCtpExpectedDtsTTI = _DchCtpExpectedDtsTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 6),
    _DchCtpExpectedDtsTTI_Type()
)
dchCtpExpectedDtsTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpExpectedDtsTTI.setStatus("current")


class _DchCtpDtsTTIMismatchReporting_Type(Integer32):
    """Custom type dchCtpDtsTTIMismatchReporting based on Integer32"""
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


_DchCtpDtsTTIMismatchReporting_Type.__name__ = "Integer32"
_DchCtpDtsTTIMismatchReporting_Object = MibTableColumn
dchCtpDtsTTIMismatchReporting = _DchCtpDtsTTIMismatchReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 7),
    _DchCtpDtsTTIMismatchReporting_Type()
)
dchCtpDtsTTIMismatchReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpDtsTTIMismatchReporting.setStatus("current")
_DchCtpTxDtsTTI_Type = DisplayString
_DchCtpTxDtsTTI_Object = MibTableColumn
dchCtpTxDtsTTI = _DchCtpTxDtsTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 8),
    _DchCtpTxDtsTTI_Type()
)
dchCtpTxDtsTTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpTxDtsTTI.setStatus("current")
_DchCtpRxDtsTTI_Type = DisplayString
_DchCtpRxDtsTTI_Object = MibTableColumn
dchCtpRxDtsTTI = _DchCtpRxDtsTTI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 9),
    _DchCtpRxDtsTTI_Type()
)
dchCtpRxDtsTTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpRxDtsTTI.setStatus("current")
_DchCtpPreFecThresholdOrder_Type = Integer32
_DchCtpPreFecThresholdOrder_Object = MibTableColumn
dchCtpPreFecThresholdOrder = _DchCtpPreFecThresholdOrder_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 10),
    _DchCtpPreFecThresholdOrder_Type()
)
dchCtpPreFecThresholdOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpPreFecThresholdOrder.setStatus("current")


class _DchCtpDataPlaneTransparency_Type(Integer32):
    """Custom type dchCtpDataPlaneTransparency based on Integer32"""
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
          ("enabled", 2),
          ("unknown", 3))
    )


_DchCtpDataPlaneTransparency_Type.__name__ = "Integer32"
_DchCtpDataPlaneTransparency_Object = MibTableColumn
dchCtpDataPlaneTransparency = _DchCtpDataPlaneTransparency_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 11),
    _DchCtpDataPlaneTransparency_Type()
)
dchCtpDataPlaneTransparency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpDataPlaneTransparency.setStatus("current")


class _DchCtpSignalDegradeReportingControl_Type(Integer32):
    """Custom type dchCtpSignalDegradeReportingControl based on Integer32"""
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
          ("enabled", 2),
          ("unknown", 3))
    )


_DchCtpSignalDegradeReportingControl_Type.__name__ = "Integer32"
_DchCtpSignalDegradeReportingControl_Object = MibTableColumn
dchCtpSignalDegradeReportingControl = _DchCtpSignalDegradeReportingControl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 12),
    _DchCtpSignalDegradeReportingControl_Type()
)
dchCtpSignalDegradeReportingControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpSignalDegradeReportingControl.setStatus("current")


class _DchCtpDtsFecSupport_Type(Integer32):
    """Custom type dchCtpDtsFecSupport based on Integer32"""
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
          ("enabled", 2),
          ("unknown", 3))
    )


_DchCtpDtsFecSupport_Type.__name__ = "Integer32"
_DchCtpDtsFecSupport_Object = MibTableColumn
dchCtpDtsFecSupport = _DchCtpDtsFecSupport_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 13),
    _DchCtpDtsFecSupport_Type()
)
dchCtpDtsFecSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpDtsFecSupport.setStatus("current")
_DchCtpPreFecThresholdMantissa_Type = Integer32
_DchCtpPreFecThresholdMantissa_Object = MibTableColumn
dchCtpPreFecThresholdMantissa = _DchCtpPreFecThresholdMantissa_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 14),
    _DchCtpPreFecThresholdMantissa_Type()
)
dchCtpPreFecThresholdMantissa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpPreFecThresholdMantissa.setStatus("current")
_DchCtpDtsCv15MinutesTce_Type = Counter64
_DchCtpDtsCv15MinutesTce_Object = MibTableColumn
dchCtpDtsCv15MinutesTce = _DchCtpDtsCv15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 15),
    _DchCtpDtsCv15MinutesTce_Type()
)
dchCtpDtsCv15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpDtsCv15MinutesTce.setStatus("current")
_DchCtpDtsEs15MinutesTce_Type = Integer32
_DchCtpDtsEs15MinutesTce_Object = MibTableColumn
dchCtpDtsEs15MinutesTce = _DchCtpDtsEs15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 16),
    _DchCtpDtsEs15MinutesTce_Type()
)
dchCtpDtsEs15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpDtsEs15MinutesTce.setStatus("current")
_DchCtpDtsSes15MinutesTce_Type = Integer32
_DchCtpDtsSes15MinutesTce_Object = MibTableColumn
dchCtpDtsSes15MinutesTce = _DchCtpDtsSes15MinutesTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 17),
    _DchCtpDtsSes15MinutesTce_Type()
)
dchCtpDtsSes15MinutesTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpDtsSes15MinutesTce.setStatus("current")
_DchCtpDtsCvDayTce_Type = Counter64
_DchCtpDtsCvDayTce_Object = MibTableColumn
dchCtpDtsCvDayTce = _DchCtpDtsCvDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 18),
    _DchCtpDtsCvDayTce_Type()
)
dchCtpDtsCvDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpDtsCvDayTce.setStatus("current")
_DchCtpDtsEsDayTce_Type = Integer32
_DchCtpDtsEsDayTce_Object = MibTableColumn
dchCtpDtsEsDayTce = _DchCtpDtsEsDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 19),
    _DchCtpDtsEsDayTce_Type()
)
dchCtpDtsEsDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpDtsEsDayTce.setStatus("current")
_DchCtpDtsSesDayTce_Type = Integer32
_DchCtpDtsSesDayTce_Object = MibTableColumn
dchCtpDtsSesDayTce = _DchCtpDtsSesDayTce_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 20),
    _DchCtpDtsSesDayTce_Type()
)
dchCtpDtsSesDayTce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpDtsSesDayTce.setStatus("current")
_DchCtpDtsCv15MinutesTceReporting_Type = TruthValue
_DchCtpDtsCv15MinutesTceReporting_Object = MibTableColumn
dchCtpDtsCv15MinutesTceReporting = _DchCtpDtsCv15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 21),
    _DchCtpDtsCv15MinutesTceReporting_Type()
)
dchCtpDtsCv15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpDtsCv15MinutesTceReporting.setStatus("current")
_DchCtpDtsEs15MinutesTceReporting_Type = TruthValue
_DchCtpDtsEs15MinutesTceReporting_Object = MibTableColumn
dchCtpDtsEs15MinutesTceReporting = _DchCtpDtsEs15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 22),
    _DchCtpDtsEs15MinutesTceReporting_Type()
)
dchCtpDtsEs15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpDtsEs15MinutesTceReporting.setStatus("current")
_DchCtpDtsSes15MinutesTceReporting_Type = TruthValue
_DchCtpDtsSes15MinutesTceReporting_Object = MibTableColumn
dchCtpDtsSes15MinutesTceReporting = _DchCtpDtsSes15MinutesTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 23),
    _DchCtpDtsSes15MinutesTceReporting_Type()
)
dchCtpDtsSes15MinutesTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpDtsSes15MinutesTceReporting.setStatus("current")
_DchCtpDtsCvDayTceReporting_Type = TruthValue
_DchCtpDtsCvDayTceReporting_Object = MibTableColumn
dchCtpDtsCvDayTceReporting = _DchCtpDtsCvDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 24),
    _DchCtpDtsCvDayTceReporting_Type()
)
dchCtpDtsCvDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpDtsCvDayTceReporting.setStatus("current")
_DchCtpDtsEsDayTceReporting_Type = TruthValue
_DchCtpDtsEsDayTceReporting_Object = MibTableColumn
dchCtpDtsEsDayTceReporting = _DchCtpDtsEsDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 25),
    _DchCtpDtsEsDayTceReporting_Type()
)
dchCtpDtsEsDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpDtsEsDayTceReporting.setStatus("current")
_DchCtpDtsSesDayTceReporting_Type = TruthValue
_DchCtpDtsSesDayTceReporting_Object = MibTableColumn
dchCtpDtsSesDayTceReporting = _DchCtpDtsSesDayTceReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 26),
    _DchCtpDtsSesDayTceReporting_Type()
)
dchCtpDtsSesDayTceReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpDtsSesDayTceReporting.setStatus("current")


class _DchCtpPmHistStatsEnable_Type(Integer32):
    """Custom type dchCtpPmHistStatsEnable based on Integer32"""
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


_DchCtpPmHistStatsEnable_Type.__name__ = "Integer32"
_DchCtpPmHistStatsEnable_Object = MibTableColumn
dchCtpPmHistStatsEnable = _DchCtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 27),
    _DchCtpPmHistStatsEnable_Type()
)
dchCtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpPmHistStatsEnable.setStatus("current")


class _DchCtpConnectivityVerification_Type(Integer32):
    """Custom type dchCtpConnectivityVerification based on Integer32"""
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


_DchCtpConnectivityVerification_Type.__name__ = "Integer32"
_DchCtpConnectivityVerification_Object = MibTableColumn
dchCtpConnectivityVerification = _DchCtpConnectivityVerification_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 1, 1, 28),
    _DchCtpConnectivityVerification_Type()
)
dchCtpConnectivityVerification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dchCtpConnectivityVerification.setStatus("current")
_DchCtpConformance_ObjectIdentity = ObjectIdentity
dchCtpConformance = _DchCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 3)
)
_DchCtpCompliances_ObjectIdentity = ObjectIdentity
dchCtpCompliances = _DchCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 3, 1)
)
_DchCtpGroups_ObjectIdentity = ObjectIdentity
dchCtpGroups = _DchCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 3, 2)
)

# Managed Objects groups

dchCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 3, 2, 1)
)
dchCtpGroup.setObjects(
      *(("INFINERA-TP-DCHCTP-MIB", "dchCtpTribPrbsGenMode"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpTribPrbsMonMode"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpSupportingCircuitIdList"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpLoopback"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpConfiguredServiceType"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpExpectedDtsTTI"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpDtsTTIMismatchReporting"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpTxDtsTTI"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpRxDtsTTI"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpPreFecThresholdOrder"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpDataPlaneTransparency"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpSignalDegradeReportingControl"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpDtsFecSupport"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpPreFecThresholdMantissa"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpDtsCv15MinutesTce"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpDtsEs15MinutesTce"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpDtsSes15MinutesTce"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpDtsCvDayTce"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpDtsEsDayTce"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpDtsSesDayTce"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpDtsCv15MinutesTceReporting"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpDtsEs15MinutesTceReporting"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpDtsSes15MinutesTceReporting"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpDtsCvDayTceReporting"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpDtsEsDayTceReporting"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpDtsSesDayTceReporting"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpPmHistStatsEnable"),
        ("INFINERA-TP-DCHCTP-MIB", "dchCtpConnectivityVerification"))
)
if mibBuilder.loadTexts:
    dchCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dchCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 18, 3, 1, 1)
)
dchCtpCompliance.setObjects(
    ("INFINERA-TP-DCHCTP-MIB", "dchCtpGroup")
)
if mibBuilder.loadTexts:
    dchCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-DCHCTP-MIB",
    **{"dchCtpMIB": dchCtpMIB,
       "dchCtpTable": dchCtpTable,
       "dchCtpEntry": dchCtpEntry,
       "dchCtpTribPrbsGenMode": dchCtpTribPrbsGenMode,
       "dchCtpTribPrbsMonMode": dchCtpTribPrbsMonMode,
       "dchCtpSupportingCircuitIdList": dchCtpSupportingCircuitIdList,
       "dchCtpLoopback": dchCtpLoopback,
       "dchCtpConfiguredServiceType": dchCtpConfiguredServiceType,
       "dchCtpExpectedDtsTTI": dchCtpExpectedDtsTTI,
       "dchCtpDtsTTIMismatchReporting": dchCtpDtsTTIMismatchReporting,
       "dchCtpTxDtsTTI": dchCtpTxDtsTTI,
       "dchCtpRxDtsTTI": dchCtpRxDtsTTI,
       "dchCtpPreFecThresholdOrder": dchCtpPreFecThresholdOrder,
       "dchCtpDataPlaneTransparency": dchCtpDataPlaneTransparency,
       "dchCtpSignalDegradeReportingControl": dchCtpSignalDegradeReportingControl,
       "dchCtpDtsFecSupport": dchCtpDtsFecSupport,
       "dchCtpPreFecThresholdMantissa": dchCtpPreFecThresholdMantissa,
       "dchCtpDtsCv15MinutesTce": dchCtpDtsCv15MinutesTce,
       "dchCtpDtsEs15MinutesTce": dchCtpDtsEs15MinutesTce,
       "dchCtpDtsSes15MinutesTce": dchCtpDtsSes15MinutesTce,
       "dchCtpDtsCvDayTce": dchCtpDtsCvDayTce,
       "dchCtpDtsEsDayTce": dchCtpDtsEsDayTce,
       "dchCtpDtsSesDayTce": dchCtpDtsSesDayTce,
       "dchCtpDtsCv15MinutesTceReporting": dchCtpDtsCv15MinutesTceReporting,
       "dchCtpDtsEs15MinutesTceReporting": dchCtpDtsEs15MinutesTceReporting,
       "dchCtpDtsSes15MinutesTceReporting": dchCtpDtsSes15MinutesTceReporting,
       "dchCtpDtsCvDayTceReporting": dchCtpDtsCvDayTceReporting,
       "dchCtpDtsEsDayTceReporting": dchCtpDtsEsDayTceReporting,
       "dchCtpDtsSesDayTceReporting": dchCtpDtsSesDayTceReporting,
       "dchCtpPmHistStatsEnable": dchCtpPmHistStatsEnable,
       "dchCtpConnectivityVerification": dchCtpConnectivityVerification,
       "dchCtpConformance": dchCtpConformance,
       "dchCtpCompliances": dchCtpCompliances,
       "dchCtpCompliance": dchCtpCompliance,
       "dchCtpGroups": dchCtpGroups,
       "dchCtpGroup": dchCtpGroup}
)
