# SNMP MIB module (TWAMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/datacom/TWAMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:04:48 2025
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

(datacomDevicesMIBs,) = mibBuilder.importSymbols(
    "DATACOM-SMI",
    "datacomDevicesMIBs")

(InetAddress,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetPortNumber")

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


# MODULE-IDENTITY

twampMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7)
)
if mibBuilder.loadTexts:
    twampMIB.setRevisions(
        ("2019-10-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TwampTestLossRatio(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



class TwampMeasure(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"


# MIB Managed Objects in the order of their OIDs

_TwampSessionTable_Object = MibTable
twampSessionTable = _TwampSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 1)
)
if mibBuilder.loadTexts:
    twampSessionTable.setStatus("current")
_TwampSessionEntry_Object = MibTableRow
twampSessionEntry = _TwampSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 1, 1)
)
twampSessionEntry.setIndexNames(
    (0, "TWAMP-MIB", "twampSessionId"),
)
if mibBuilder.loadTexts:
    twampSessionEntry.setStatus("current")


class _TwampSessionId_Type(Unsigned32):
    """Custom type twampSessionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TwampSessionId_Type.__name__ = "Unsigned32"
_TwampSessionId_Object = MibTableColumn
twampSessionId = _TwampSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 1, 1, 1),
    _TwampSessionId_Type()
)
twampSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampSessionId.setStatus("current")


class _TwampSessionDuration_Type(Unsigned32):
    """Custom type twampSessionDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TwampSessionDuration_Type.__name__ = "Unsigned32"
_TwampSessionDuration_Object = MibTableColumn
twampSessionDuration = _TwampSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 1, 1, 2),
    _TwampSessionDuration_Type()
)
twampSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampSessionDuration.setStatus("current")
if mibBuilder.loadTexts:
    twampSessionDuration.setUnits("s")


class _TwampSessionInterval_Type(Unsigned32):
    """Custom type twampSessionInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TwampSessionInterval_Type.__name__ = "Unsigned32"
_TwampSessionInterval_Object = MibTableColumn
twampSessionInterval = _TwampSessionInterval_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 1, 1, 3),
    _TwampSessionInterval_Type()
)
twampSessionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampSessionInterval.setStatus("current")
if mibBuilder.loadTexts:
    twampSessionInterval.setUnits("s")


class _TwampSessionState_Type(Integer32):
    """Custom type twampSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_TwampSessionState_Type.__name__ = "Integer32"
_TwampSessionState_Object = MibTableColumn
twampSessionState = _TwampSessionState_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 1, 1, 4),
    _TwampSessionState_Type()
)
twampSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampSessionState.setStatus("current")
_TwampSessionSrcAddr_Type = InetAddress
_TwampSessionSrcAddr_Object = MibTableColumn
twampSessionSrcAddr = _TwampSessionSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 1, 1, 5),
    _TwampSessionSrcAddr_Type()
)
twampSessionSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampSessionSrcAddr.setStatus("current")
_TwampSessionDstAddr_Type = InetAddress
_TwampSessionDstAddr_Object = MibTableColumn
twampSessionDstAddr = _TwampSessionDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 1, 1, 6),
    _TwampSessionDstAddr_Type()
)
twampSessionDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampSessionDstAddr.setStatus("current")
_TwampSessionDstPort_Type = InetPortNumber
_TwampSessionDstPort_Object = MibTableColumn
twampSessionDstPort = _TwampSessionDstPort_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 1, 1, 7),
    _TwampSessionDstPort_Type()
)
twampSessionDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampSessionDstPort.setStatus("current")


class _TwampSessionPktSize_Type(Unsigned32):
    """Custom type twampSessionPktSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TwampSessionPktSize_Type.__name__ = "Unsigned32"
_TwampSessionPktSize_Object = MibTableColumn
twampSessionPktSize = _TwampSessionPktSize_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 1, 1, 8),
    _TwampSessionPktSize_Type()
)
twampSessionPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampSessionPktSize.setStatus("current")
if mibBuilder.loadTexts:
    twampSessionPktSize.setUnits("B")


class _TwampSessionDSCP_Type(Unsigned32):
    """Custom type twampSessionDSCP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_TwampSessionDSCP_Type.__name__ = "Unsigned32"
_TwampSessionDSCP_Object = MibTableColumn
twampSessionDSCP = _TwampSessionDSCP_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 1, 1, 9),
    _TwampSessionDSCP_Type()
)
twampSessionDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampSessionDSCP.setStatus("current")


class _TwampSessionTotalTests_Type(Unsigned32):
    """Custom type twampSessionTotalTests based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TwampSessionTotalTests_Type.__name__ = "Unsigned32"
_TwampSessionTotalTests_Object = MibTableColumn
twampSessionTotalTests = _TwampSessionTotalTests_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 1, 1, 10),
    _TwampSessionTotalTests_Type()
)
twampSessionTotalTests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampSessionTotalTests.setStatus("current")


class _TwampSessionTotalTxPkts_Type(Unsigned32):
    """Custom type twampSessionTotalTxPkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TwampSessionTotalTxPkts_Type.__name__ = "Unsigned32"
_TwampSessionTotalTxPkts_Object = MibTableColumn
twampSessionTotalTxPkts = _TwampSessionTotalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 1, 1, 11),
    _TwampSessionTotalTxPkts_Type()
)
twampSessionTotalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampSessionTotalTxPkts.setStatus("current")


class _TwampSessionTotalRxPkts_Type(Unsigned32):
    """Custom type twampSessionTotalRxPkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TwampSessionTotalRxPkts_Type.__name__ = "Unsigned32"
_TwampSessionTotalRxPkts_Object = MibTableColumn
twampSessionTotalRxPkts = _TwampSessionTotalRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 1, 1, 12),
    _TwampSessionTotalRxPkts_Type()
)
twampSessionTotalRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampSessionTotalRxPkts.setStatus("current")
_TwampTestTable_Object = MibTable
twampTestTable = _TwampTestTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 2)
)
if mibBuilder.loadTexts:
    twampTestTable.setStatus("current")
_TwampTestEntry_Object = MibTableRow
twampTestEntry = _TwampTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 2, 1)
)
twampTestEntry.setIndexNames(
    (0, "TWAMP-MIB", "twampSessionId"),
    (0, "TWAMP-MIB", "twampTestIndex"),
)
if mibBuilder.loadTexts:
    twampTestEntry.setStatus("current")


class _TwampTestSessionId_Type(Unsigned32):
    """Custom type twampTestSessionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TwampTestSessionId_Type.__name__ = "Unsigned32"
_TwampTestSessionId_Object = MibTableColumn
twampTestSessionId = _TwampTestSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 2, 1, 1),
    _TwampTestSessionId_Type()
)
twampTestSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampTestSessionId.setStatus("current")


class _TwampTestIndex_Type(Unsigned32):
    """Custom type twampTestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TwampTestIndex_Type.__name__ = "Unsigned32"
_TwampTestIndex_Object = MibTableColumn
twampTestIndex = _TwampTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 2, 1, 2),
    _TwampTestIndex_Type()
)
twampTestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampTestIndex.setStatus("current")


class _TwampTestId_Type(Unsigned32):
    """Custom type twampTestId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TwampTestId_Type.__name__ = "Unsigned32"
_TwampTestId_Object = MibTableColumn
twampTestId = _TwampTestId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 2, 1, 3),
    _TwampTestId_Type()
)
twampTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampTestId.setStatus("current")
_TwampTestDelayMin_Type = TwampMeasure
_TwampTestDelayMin_Object = MibTableColumn
twampTestDelayMin = _TwampTestDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 2, 1, 4),
    _TwampTestDelayMin_Type()
)
twampTestDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampTestDelayMin.setStatus("current")
if mibBuilder.loadTexts:
    twampTestDelayMin.setUnits("ms")
_TwampTestDelayMax_Type = TwampMeasure
_TwampTestDelayMax_Object = MibTableColumn
twampTestDelayMax = _TwampTestDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 2, 1, 5),
    _TwampTestDelayMax_Type()
)
twampTestDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampTestDelayMax.setStatus("current")
if mibBuilder.loadTexts:
    twampTestDelayMax.setUnits("ms")
_TwampTestDelayAvg_Type = TwampMeasure
_TwampTestDelayAvg_Object = MibTableColumn
twampTestDelayAvg = _TwampTestDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 2, 1, 6),
    _TwampTestDelayAvg_Type()
)
twampTestDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampTestDelayAvg.setStatus("current")
if mibBuilder.loadTexts:
    twampTestDelayAvg.setUnits("ms")
_TwampTestJitterMin_Type = TwampMeasure
_TwampTestJitterMin_Object = MibTableColumn
twampTestJitterMin = _TwampTestJitterMin_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 2, 1, 7),
    _TwampTestJitterMin_Type()
)
twampTestJitterMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampTestJitterMin.setStatus("current")
if mibBuilder.loadTexts:
    twampTestJitterMin.setUnits("ms")
_TwampTestJitterMax_Type = TwampMeasure
_TwampTestJitterMax_Object = MibTableColumn
twampTestJitterMax = _TwampTestJitterMax_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 2, 1, 8),
    _TwampTestJitterMax_Type()
)
twampTestJitterMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampTestJitterMax.setStatus("current")
if mibBuilder.loadTexts:
    twampTestJitterMax.setUnits("ms")
_TwampTestJitterAvg_Type = TwampMeasure
_TwampTestJitterAvg_Object = MibTableColumn
twampTestJitterAvg = _TwampTestJitterAvg_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 2, 1, 9),
    _TwampTestJitterAvg_Type()
)
twampTestJitterAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampTestJitterAvg.setStatus("current")
if mibBuilder.loadTexts:
    twampTestJitterAvg.setUnits("ms")
_TwampTestTxPkts_Type = Unsigned32
_TwampTestTxPkts_Object = MibTableColumn
twampTestTxPkts = _TwampTestTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 2, 1, 10),
    _TwampTestTxPkts_Type()
)
twampTestTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampTestTxPkts.setStatus("current")
_TwampTestRxPkts_Type = Unsigned32
_TwampTestRxPkts_Object = MibTableColumn
twampTestRxPkts = _TwampTestRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 2, 1, 11),
    _TwampTestRxPkts_Type()
)
twampTestRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampTestRxPkts.setStatus("current")
_TwampTestLossRatio_Type = TwampTestLossRatio
_TwampTestLossRatio_Object = MibTableColumn
twampTestLossRatio = _TwampTestLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 2, 1, 12),
    _TwampTestLossRatio_Type()
)
twampTestLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampTestLossRatio.setStatus("current")


class _TwampTestConnectivity_Type(Integer32):
    """Custom type twampTestConnectivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TwampTestConnectivity_Type.__name__ = "Integer32"
_TwampTestConnectivity_Object = MibTableColumn
twampTestConnectivity = _TwampTestConnectivity_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 2, 1, 13),
    _TwampTestConnectivity_Type()
)
twampTestConnectivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampTestConnectivity.setStatus("current")
_TwampTestRoundTripDelayMin_Type = TwampMeasure
_TwampTestRoundTripDelayMin_Object = MibTableColumn
twampTestRoundTripDelayMin = _TwampTestRoundTripDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 2, 1, 14),
    _TwampTestRoundTripDelayMin_Type()
)
twampTestRoundTripDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampTestRoundTripDelayMin.setStatus("current")
if mibBuilder.loadTexts:
    twampTestRoundTripDelayMin.setUnits("ms")
_TwampTestRoundTripDelayMax_Type = TwampMeasure
_TwampTestRoundTripDelayMax_Object = MibTableColumn
twampTestRoundTripDelayMax = _TwampTestRoundTripDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 2, 1, 15),
    _TwampTestRoundTripDelayMax_Type()
)
twampTestRoundTripDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampTestRoundTripDelayMax.setStatus("current")
if mibBuilder.loadTexts:
    twampTestRoundTripDelayMax.setUnits("ms")
_TwampTestRoundTripDelayAvg_Type = TwampMeasure
_TwampTestRoundTripDelayAvg_Object = MibTableColumn
twampTestRoundTripDelayAvg = _TwampTestRoundTripDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 2, 1, 16),
    _TwampTestRoundTripDelayAvg_Type()
)
twampTestRoundTripDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampTestRoundTripDelayAvg.setStatus("current")
if mibBuilder.loadTexts:
    twampTestRoundTripDelayAvg.setUnits("ms")
_TwampFarEndTestTable_Object = MibTable
twampFarEndTestTable = _TwampFarEndTestTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 3)
)
if mibBuilder.loadTexts:
    twampFarEndTestTable.setStatus("current")
_TwampFarEndTestEntry_Object = MibTableRow
twampFarEndTestEntry = _TwampFarEndTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 3, 1)
)
twampFarEndTestEntry.setIndexNames(
    (0, "TWAMP-MIB", "twampSessionId"),
    (0, "TWAMP-MIB", "twampFarEndTestIndex"),
)
if mibBuilder.loadTexts:
    twampFarEndTestEntry.setStatus("current")


class _TwampFarEndTestSessionId_Type(Unsigned32):
    """Custom type twampFarEndTestSessionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TwampFarEndTestSessionId_Type.__name__ = "Unsigned32"
_TwampFarEndTestSessionId_Object = MibTableColumn
twampFarEndTestSessionId = _TwampFarEndTestSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 3, 1, 1),
    _TwampFarEndTestSessionId_Type()
)
twampFarEndTestSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampFarEndTestSessionId.setStatus("current")


class _TwampFarEndTestIndex_Type(Unsigned32):
    """Custom type twampFarEndTestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TwampFarEndTestIndex_Type.__name__ = "Unsigned32"
_TwampFarEndTestIndex_Object = MibTableColumn
twampFarEndTestIndex = _TwampFarEndTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 3, 1, 2),
    _TwampFarEndTestIndex_Type()
)
twampFarEndTestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampFarEndTestIndex.setStatus("current")


class _TwampFarEndTestId_Type(Unsigned32):
    """Custom type twampFarEndTestId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TwampFarEndTestId_Type.__name__ = "Unsigned32"
_TwampFarEndTestId_Object = MibTableColumn
twampFarEndTestId = _TwampFarEndTestId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 3, 1, 3),
    _TwampFarEndTestId_Type()
)
twampFarEndTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampFarEndTestId.setStatus("current")
_TwampFarEndTestDelayMin_Type = TwampMeasure
_TwampFarEndTestDelayMin_Object = MibTableColumn
twampFarEndTestDelayMin = _TwampFarEndTestDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 3, 1, 4),
    _TwampFarEndTestDelayMin_Type()
)
twampFarEndTestDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampFarEndTestDelayMin.setStatus("current")
if mibBuilder.loadTexts:
    twampFarEndTestDelayMin.setUnits("ms")
_TwampFarEndTestDelayMax_Type = TwampMeasure
_TwampFarEndTestDelayMax_Object = MibTableColumn
twampFarEndTestDelayMax = _TwampFarEndTestDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 3, 1, 5),
    _TwampFarEndTestDelayMax_Type()
)
twampFarEndTestDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampFarEndTestDelayMax.setStatus("current")
if mibBuilder.loadTexts:
    twampFarEndTestDelayMax.setUnits("ms")
_TwampFarEndTestDelayAvg_Type = TwampMeasure
_TwampFarEndTestDelayAvg_Object = MibTableColumn
twampFarEndTestDelayAvg = _TwampFarEndTestDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 3, 1, 6),
    _TwampFarEndTestDelayAvg_Type()
)
twampFarEndTestDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampFarEndTestDelayAvg.setStatus("current")
if mibBuilder.loadTexts:
    twampFarEndTestDelayAvg.setUnits("ms")
_TwampFarEndTestJitterMin_Type = TwampMeasure
_TwampFarEndTestJitterMin_Object = MibTableColumn
twampFarEndTestJitterMin = _TwampFarEndTestJitterMin_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 3, 1, 7),
    _TwampFarEndTestJitterMin_Type()
)
twampFarEndTestJitterMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampFarEndTestJitterMin.setStatus("current")
if mibBuilder.loadTexts:
    twampFarEndTestJitterMin.setUnits("ms")
_TwampFarEndTestJitterMax_Type = TwampMeasure
_TwampFarEndTestJitterMax_Object = MibTableColumn
twampFarEndTestJitterMax = _TwampFarEndTestJitterMax_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 3, 1, 8),
    _TwampFarEndTestJitterMax_Type()
)
twampFarEndTestJitterMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampFarEndTestJitterMax.setStatus("current")
if mibBuilder.loadTexts:
    twampFarEndTestJitterMax.setUnits("ms")
_TwampFarEndTestJitterAvg_Type = TwampMeasure
_TwampFarEndTestJitterAvg_Object = MibTableColumn
twampFarEndTestJitterAvg = _TwampFarEndTestJitterAvg_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 3, 1, 9),
    _TwampFarEndTestJitterAvg_Type()
)
twampFarEndTestJitterAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampFarEndTestJitterAvg.setStatus("current")
if mibBuilder.loadTexts:
    twampFarEndTestJitterAvg.setUnits("ms")
_TwampFarEndTestTxPkts_Type = Unsigned32
_TwampFarEndTestTxPkts_Object = MibTableColumn
twampFarEndTestTxPkts = _TwampFarEndTestTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 3, 1, 10),
    _TwampFarEndTestTxPkts_Type()
)
twampFarEndTestTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampFarEndTestTxPkts.setStatus("current")
_TwampFarEndTestRxPkts_Type = Unsigned32
_TwampFarEndTestRxPkts_Object = MibTableColumn
twampFarEndTestRxPkts = _TwampFarEndTestRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 3, 1, 11),
    _TwampFarEndTestRxPkts_Type()
)
twampFarEndTestRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampFarEndTestRxPkts.setStatus("current")
_TwampFarEndTestLossRatio_Type = TwampTestLossRatio
_TwampFarEndTestLossRatio_Object = MibTableColumn
twampFarEndTestLossRatio = _TwampFarEndTestLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 3, 1, 12),
    _TwampFarEndTestLossRatio_Type()
)
twampFarEndTestLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampFarEndTestLossRatio.setStatus("current")


class _TwampFarEndTestConnectivity_Type(Integer32):
    """Custom type twampFarEndTestConnectivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TwampFarEndTestConnectivity_Type.__name__ = "Integer32"
_TwampFarEndTestConnectivity_Object = MibTableColumn
twampFarEndTestConnectivity = _TwampFarEndTestConnectivity_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 3, 1, 13),
    _TwampFarEndTestConnectivity_Type()
)
twampFarEndTestConnectivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampFarEndTestConnectivity.setStatus("current")
_TwampNearEndTestTable_Object = MibTable
twampNearEndTestTable = _TwampNearEndTestTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 4)
)
if mibBuilder.loadTexts:
    twampNearEndTestTable.setStatus("current")
_TwampNearEndTestEntry_Object = MibTableRow
twampNearEndTestEntry = _TwampNearEndTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 4, 1)
)
twampNearEndTestEntry.setIndexNames(
    (0, "TWAMP-MIB", "twampSessionId"),
    (0, "TWAMP-MIB", "twampNearEndTestIndex"),
)
if mibBuilder.loadTexts:
    twampNearEndTestEntry.setStatus("current")


class _TwampNearEndTestSessionId_Type(Unsigned32):
    """Custom type twampNearEndTestSessionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TwampNearEndTestSessionId_Type.__name__ = "Unsigned32"
_TwampNearEndTestSessionId_Object = MibTableColumn
twampNearEndTestSessionId = _TwampNearEndTestSessionId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 4, 1, 1),
    _TwampNearEndTestSessionId_Type()
)
twampNearEndTestSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampNearEndTestSessionId.setStatus("current")


class _TwampNearEndTestIndex_Type(Unsigned32):
    """Custom type twampNearEndTestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TwampNearEndTestIndex_Type.__name__ = "Unsigned32"
_TwampNearEndTestIndex_Object = MibTableColumn
twampNearEndTestIndex = _TwampNearEndTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 4, 1, 2),
    _TwampNearEndTestIndex_Type()
)
twampNearEndTestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampNearEndTestIndex.setStatus("current")


class _TwampNearEndTestId_Type(Unsigned32):
    """Custom type twampNearEndTestId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TwampNearEndTestId_Type.__name__ = "Unsigned32"
_TwampNearEndTestId_Object = MibTableColumn
twampNearEndTestId = _TwampNearEndTestId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 4, 1, 3),
    _TwampNearEndTestId_Type()
)
twampNearEndTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampNearEndTestId.setStatus("current")
_TwampNearEndTestDelayMin_Type = TwampMeasure
_TwampNearEndTestDelayMin_Object = MibTableColumn
twampNearEndTestDelayMin = _TwampNearEndTestDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 4, 1, 4),
    _TwampNearEndTestDelayMin_Type()
)
twampNearEndTestDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampNearEndTestDelayMin.setStatus("current")
if mibBuilder.loadTexts:
    twampNearEndTestDelayMin.setUnits("ms")
_TwampNearEndTestDelayMax_Type = TwampMeasure
_TwampNearEndTestDelayMax_Object = MibTableColumn
twampNearEndTestDelayMax = _TwampNearEndTestDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 4, 1, 5),
    _TwampNearEndTestDelayMax_Type()
)
twampNearEndTestDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampNearEndTestDelayMax.setStatus("current")
if mibBuilder.loadTexts:
    twampNearEndTestDelayMax.setUnits("ms")
_TwampNearEndTestDelayAvg_Type = TwampMeasure
_TwampNearEndTestDelayAvg_Object = MibTableColumn
twampNearEndTestDelayAvg = _TwampNearEndTestDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 4, 1, 6),
    _TwampNearEndTestDelayAvg_Type()
)
twampNearEndTestDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampNearEndTestDelayAvg.setStatus("current")
if mibBuilder.loadTexts:
    twampNearEndTestDelayAvg.setUnits("ms")
_TwampNearEndTestJitterMin_Type = TwampMeasure
_TwampNearEndTestJitterMin_Object = MibTableColumn
twampNearEndTestJitterMin = _TwampNearEndTestJitterMin_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 4, 1, 7),
    _TwampNearEndTestJitterMin_Type()
)
twampNearEndTestJitterMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampNearEndTestJitterMin.setStatus("current")
if mibBuilder.loadTexts:
    twampNearEndTestJitterMin.setUnits("ms")
_TwampNearEndTestJitterMax_Type = TwampMeasure
_TwampNearEndTestJitterMax_Object = MibTableColumn
twampNearEndTestJitterMax = _TwampNearEndTestJitterMax_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 4, 1, 8),
    _TwampNearEndTestJitterMax_Type()
)
twampNearEndTestJitterMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampNearEndTestJitterMax.setStatus("current")
if mibBuilder.loadTexts:
    twampNearEndTestJitterMax.setUnits("ms")
_TwampNearEndTestJitterAvg_Type = TwampMeasure
_TwampNearEndTestJitterAvg_Object = MibTableColumn
twampNearEndTestJitterAvg = _TwampNearEndTestJitterAvg_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 4, 1, 9),
    _TwampNearEndTestJitterAvg_Type()
)
twampNearEndTestJitterAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampNearEndTestJitterAvg.setStatus("current")
if mibBuilder.loadTexts:
    twampNearEndTestJitterAvg.setUnits("ms")
_TwampNearEndTestTxPkts_Type = Unsigned32
_TwampNearEndTestTxPkts_Object = MibTableColumn
twampNearEndTestTxPkts = _TwampNearEndTestTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 4, 1, 10),
    _TwampNearEndTestTxPkts_Type()
)
twampNearEndTestTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampNearEndTestTxPkts.setStatus("current")
_TwampNearEndTestRxPkts_Type = Unsigned32
_TwampNearEndTestRxPkts_Object = MibTableColumn
twampNearEndTestRxPkts = _TwampNearEndTestRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 4, 1, 11),
    _TwampNearEndTestRxPkts_Type()
)
twampNearEndTestRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampNearEndTestRxPkts.setStatus("current")
_TwampNearEndTestLossRatio_Type = TwampTestLossRatio
_TwampNearEndTestLossRatio_Object = MibTableColumn
twampNearEndTestLossRatio = _TwampNearEndTestLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 4, 1, 12),
    _TwampNearEndTestLossRatio_Type()
)
twampNearEndTestLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampNearEndTestLossRatio.setStatus("current")


class _TwampNearEndTestConnectivity_Type(Integer32):
    """Custom type twampNearEndTestConnectivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TwampNearEndTestConnectivity_Type.__name__ = "Integer32"
_TwampNearEndTestConnectivity_Object = MibTableColumn
twampNearEndTestConnectivity = _TwampNearEndTestConnectivity_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 7, 4, 1, 13),
    _TwampNearEndTestConnectivity_Type()
)
twampNearEndTestConnectivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twampNearEndTestConnectivity.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TWAMP-MIB",
    **{"TwampTestLossRatio": TwampTestLossRatio,
       "TwampMeasure": TwampMeasure,
       "twampMIB": twampMIB,
       "twampSessionTable": twampSessionTable,
       "twampSessionEntry": twampSessionEntry,
       "twampSessionId": twampSessionId,
       "twampSessionDuration": twampSessionDuration,
       "twampSessionInterval": twampSessionInterval,
       "twampSessionState": twampSessionState,
       "twampSessionSrcAddr": twampSessionSrcAddr,
       "twampSessionDstAddr": twampSessionDstAddr,
       "twampSessionDstPort": twampSessionDstPort,
       "twampSessionPktSize": twampSessionPktSize,
       "twampSessionDSCP": twampSessionDSCP,
       "twampSessionTotalTests": twampSessionTotalTests,
       "twampSessionTotalTxPkts": twampSessionTotalTxPkts,
       "twampSessionTotalRxPkts": twampSessionTotalRxPkts,
       "twampTestTable": twampTestTable,
       "twampTestEntry": twampTestEntry,
       "twampTestSessionId": twampTestSessionId,
       "twampTestIndex": twampTestIndex,
       "twampTestId": twampTestId,
       "twampTestDelayMin": twampTestDelayMin,
       "twampTestDelayMax": twampTestDelayMax,
       "twampTestDelayAvg": twampTestDelayAvg,
       "twampTestJitterMin": twampTestJitterMin,
       "twampTestJitterMax": twampTestJitterMax,
       "twampTestJitterAvg": twampTestJitterAvg,
       "twampTestTxPkts": twampTestTxPkts,
       "twampTestRxPkts": twampTestRxPkts,
       "twampTestLossRatio": twampTestLossRatio,
       "twampTestConnectivity": twampTestConnectivity,
       "twampTestRoundTripDelayMin": twampTestRoundTripDelayMin,
       "twampTestRoundTripDelayMax": twampTestRoundTripDelayMax,
       "twampTestRoundTripDelayAvg": twampTestRoundTripDelayAvg,
       "twampFarEndTestTable": twampFarEndTestTable,
       "twampFarEndTestEntry": twampFarEndTestEntry,
       "twampFarEndTestSessionId": twampFarEndTestSessionId,
       "twampFarEndTestIndex": twampFarEndTestIndex,
       "twampFarEndTestId": twampFarEndTestId,
       "twampFarEndTestDelayMin": twampFarEndTestDelayMin,
       "twampFarEndTestDelayMax": twampFarEndTestDelayMax,
       "twampFarEndTestDelayAvg": twampFarEndTestDelayAvg,
       "twampFarEndTestJitterMin": twampFarEndTestJitterMin,
       "twampFarEndTestJitterMax": twampFarEndTestJitterMax,
       "twampFarEndTestJitterAvg": twampFarEndTestJitterAvg,
       "twampFarEndTestTxPkts": twampFarEndTestTxPkts,
       "twampFarEndTestRxPkts": twampFarEndTestRxPkts,
       "twampFarEndTestLossRatio": twampFarEndTestLossRatio,
       "twampFarEndTestConnectivity": twampFarEndTestConnectivity,
       "twampNearEndTestTable": twampNearEndTestTable,
       "twampNearEndTestEntry": twampNearEndTestEntry,
       "twampNearEndTestSessionId": twampNearEndTestSessionId,
       "twampNearEndTestIndex": twampNearEndTestIndex,
       "twampNearEndTestId": twampNearEndTestId,
       "twampNearEndTestDelayMin": twampNearEndTestDelayMin,
       "twampNearEndTestDelayMax": twampNearEndTestDelayMax,
       "twampNearEndTestDelayAvg": twampNearEndTestDelayAvg,
       "twampNearEndTestJitterMin": twampNearEndTestJitterMin,
       "twampNearEndTestJitterMax": twampNearEndTestJitterMax,
       "twampNearEndTestJitterAvg": twampNearEndTestJitterAvg,
       "twampNearEndTestTxPkts": twampNearEndTestTxPkts,
       "twampNearEndTestRxPkts": twampNearEndTestRxPkts,
       "twampNearEndTestLossRatio": twampNearEndTestLossRatio,
       "twampNearEndTestConnectivity": twampNearEndTestConnectivity}
)
