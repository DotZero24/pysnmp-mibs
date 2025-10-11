# SNMP MIB module (ZTE-AN-OTDR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-OTDR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:10 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(zxAnOfd,) = mibBuilder.importSymbols(
    "ZTE-AN-OFD-SMI",
    "zxAnOfd")


# MODULE-IDENTITY

zxAnOtdrMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5)
)
if mibBuilder.loadTexts:
    zxAnOtdrMib.setRevisions(
        ("2013-03-05 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnOtdrGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnOtdrGlobalObjects = _ZxAnOtdrGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 1)
)
_ZxAnOtdrCapacityGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnOtdrCapacityGlobalObjects = _ZxAnOtdrCapacityGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 1, 1)
)


class _ZxAnOtdrWaveLengthList_Type(DisplayString):
    """Custom type zxAnOtdrWaveLengthList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnOtdrWaveLengthList_Type.__name__ = "DisplayString"
_ZxAnOtdrWaveLengthList_Object = MibScalar
zxAnOtdrWaveLengthList = _ZxAnOtdrWaveLengthList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 1, 1, 1),
    _ZxAnOtdrWaveLengthList_Type()
)
zxAnOtdrWaveLengthList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOtdrWaveLengthList.setStatus("current")


class _ZxAnOtdrTestPulseWidthList_Type(DisplayString):
    """Custom type zxAnOtdrTestPulseWidthList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnOtdrTestPulseWidthList_Type.__name__ = "DisplayString"
_ZxAnOtdrTestPulseWidthList_Object = MibScalar
zxAnOtdrTestPulseWidthList = _ZxAnOtdrTestPulseWidthList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 1, 1, 2),
    _ZxAnOtdrTestPulseWidthList_Type()
)
zxAnOtdrTestPulseWidthList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOtdrTestPulseWidthList.setStatus("current")


class _ZxAnOtdrTotalPorts_Type(Integer32):
    """Custom type zxAnOtdrTotalPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_ZxAnOtdrTotalPorts_Type.__name__ = "Integer32"
_ZxAnOtdrTotalPorts_Object = MibScalar
zxAnOtdrTotalPorts = _ZxAnOtdrTotalPorts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 1, 1, 3),
    _ZxAnOtdrTotalPorts_Type()
)
zxAnOtdrTotalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOtdrTotalPorts.setStatus("current")
_ZxAnOtdrEnvGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnOtdrEnvGlobalObjects = _ZxAnOtdrEnvGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 1, 2)
)
_ZxAnOtdrEnvCtrlCardGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnOtdrEnvCtrlCardGlobalObjects = _ZxAnOtdrEnvCtrlCardGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 1, 2, 1)
)
_ZxAnOtdrCtrlCardCurrentTemp_Type = Integer32
_ZxAnOtdrCtrlCardCurrentTemp_Object = MibScalar
zxAnOtdrCtrlCardCurrentTemp = _ZxAnOtdrCtrlCardCurrentTemp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 1, 2, 1, 1),
    _ZxAnOtdrCtrlCardCurrentTemp_Type()
)
zxAnOtdrCtrlCardCurrentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOtdrCtrlCardCurrentTemp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOtdrCtrlCardCurrentTemp.setUnits("Centigrade")


class _ZxAnOtdrCtrlCardTempHighThresh_Type(Integer32):
    """Custom type zxAnOtdrCtrlCardTempHighThresh based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(75, 95),
    )


_ZxAnOtdrCtrlCardTempHighThresh_Type.__name__ = "Integer32"
_ZxAnOtdrCtrlCardTempHighThresh_Object = MibScalar
zxAnOtdrCtrlCardTempHighThresh = _ZxAnOtdrCtrlCardTempHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 1, 2, 1, 2),
    _ZxAnOtdrCtrlCardTempHighThresh_Type()
)
zxAnOtdrCtrlCardTempHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOtdrCtrlCardTempHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOtdrCtrlCardTempHighThresh.setUnits("Centigrade")


class _ZxAnOtdrCtrlCardTempLowThresh_Type(Integer32):
    """Custom type zxAnOtdrCtrlCardTempLowThresh based on Integer32"""
    defaultValue = -45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-45, -25),
    )


_ZxAnOtdrCtrlCardTempLowThresh_Type.__name__ = "Integer32"
_ZxAnOtdrCtrlCardTempLowThresh_Object = MibScalar
zxAnOtdrCtrlCardTempLowThresh = _ZxAnOtdrCtrlCardTempLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 1, 2, 1, 3),
    _ZxAnOtdrCtrlCardTempLowThresh_Type()
)
zxAnOtdrCtrlCardTempLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOtdrCtrlCardTempLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOtdrCtrlCardTempLowThresh.setUnits("Centigrade")
_ZxAnOtdrEnvFanGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnOtdrEnvFanGlobalObjects = _ZxAnOtdrEnvFanGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 1, 2, 2)
)


class _ZxAnOtdrEnvFanStatus_Type(Integer32):
    """Custom type zxAnOtdrEnvFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_ZxAnOtdrEnvFanStatus_Type.__name__ = "Integer32"
_ZxAnOtdrEnvFanStatus_Object = MibScalar
zxAnOtdrEnvFanStatus = _ZxAnOtdrEnvFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 1, 2, 2, 1),
    _ZxAnOtdrEnvFanStatus_Type()
)
zxAnOtdrEnvFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOtdrEnvFanStatus.setStatus("current")


class _ZxAnOtdrEnvFanOperStatus_Type(Integer32):
    """Custom type zxAnOtdrEnvFanOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ZxAnOtdrEnvFanOperStatus_Type.__name__ = "Integer32"
_ZxAnOtdrEnvFanOperStatus_Object = MibScalar
zxAnOtdrEnvFanOperStatus = _ZxAnOtdrEnvFanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 1, 2, 2, 2),
    _ZxAnOtdrEnvFanOperStatus_Type()
)
zxAnOtdrEnvFanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOtdrEnvFanOperStatus.setStatus("current")
_ZxAnOtdrEnvApdGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnOtdrEnvApdGlobalObjects = _ZxAnOtdrEnvApdGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 1, 2, 3)
)
_ZxAnOtdrEnvApdCurrentTemp_Type = Integer32
_ZxAnOtdrEnvApdCurrentTemp_Object = MibScalar
zxAnOtdrEnvApdCurrentTemp = _ZxAnOtdrEnvApdCurrentTemp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 1, 2, 3, 1),
    _ZxAnOtdrEnvApdCurrentTemp_Type()
)
zxAnOtdrEnvApdCurrentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOtdrEnvApdCurrentTemp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOtdrEnvApdCurrentTemp.setUnits("Centigrade")


class _ZxAnOtdrEnvApdTempHighThresh_Type(Integer32):
    """Custom type zxAnOtdrEnvApdTempHighThresh based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 100),
    )


_ZxAnOtdrEnvApdTempHighThresh_Type.__name__ = "Integer32"
_ZxAnOtdrEnvApdTempHighThresh_Object = MibScalar
zxAnOtdrEnvApdTempHighThresh = _ZxAnOtdrEnvApdTempHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 1, 2, 3, 2),
    _ZxAnOtdrEnvApdTempHighThresh_Type()
)
zxAnOtdrEnvApdTempHighThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOtdrEnvApdTempHighThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOtdrEnvApdTempHighThresh.setUnits("Centigrade")


class _ZxAnOtdrEnvApdTempLowThresh_Type(Integer32):
    """Custom type zxAnOtdrEnvApdTempLowThresh based on Integer32"""
    defaultValue = -20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-55, -20),
    )


_ZxAnOtdrEnvApdTempLowThresh_Type.__name__ = "Integer32"
_ZxAnOtdrEnvApdTempLowThresh_Object = MibScalar
zxAnOtdrEnvApdTempLowThresh = _ZxAnOtdrEnvApdTempLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 1, 2, 3, 3),
    _ZxAnOtdrEnvApdTempLowThresh_Type()
)
zxAnOtdrEnvApdTempLowThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOtdrEnvApdTempLowThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOtdrEnvApdTempLowThresh.setUnits("Centigrade")
_ZxAnOtdrObjects_ObjectIdentity = ObjectIdentity
zxAnOtdrObjects = _ZxAnOtdrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2)
)
_ZxAnOtdrIfObjects_ObjectIdentity = ObjectIdentity
zxAnOtdrIfObjects = _ZxAnOtdrIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1)
)
_ZxAnOtdrTestParamPrfTable_Object = MibTable
zxAnOtdrTestParamPrfTable = _ZxAnOtdrTestParamPrfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfTable.setStatus("current")
_ZxAnOtdrTestParamPrfEntry_Object = MibTableRow
zxAnOtdrTestParamPrfEntry = _ZxAnOtdrTestParamPrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 2, 1)
)
zxAnOtdrTestParamPrfEntry.setIndexNames(
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrTestParamPrfName"),
)
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfEntry.setStatus("current")


class _ZxAnOtdrTestParamPrfName_Type(DisplayString):
    """Custom type zxAnOtdrTestParamPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnOtdrTestParamPrfName_Type.__name__ = "DisplayString"
_ZxAnOtdrTestParamPrfName_Object = MibTableColumn
zxAnOtdrTestParamPrfName = _ZxAnOtdrTestParamPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 2, 1, 1),
    _ZxAnOtdrTestParamPrfName_Type()
)
zxAnOtdrTestParamPrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfName.setStatus("current")


class _ZxAnOtdrTestParamPrfMode_Type(Integer32):
    """Custom type zxAnOtdrTestParamPrfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pulseMethod", 1),
          ("periodicSequenceMethod", 2),
          ("nonperiodicSequenceMethod", 3))
    )


_ZxAnOtdrTestParamPrfMode_Type.__name__ = "Integer32"
_ZxAnOtdrTestParamPrfMode_Object = MibTableColumn
zxAnOtdrTestParamPrfMode = _ZxAnOtdrTestParamPrfMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 2, 1, 2),
    _ZxAnOtdrTestParamPrfMode_Type()
)
zxAnOtdrTestParamPrfMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfMode.setStatus("current")


class _ZxAnOtdrTestParamPrfWaveLength_Type(Integer32):
    """Custom type zxAnOtdrTestParamPrfWaveLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1625, 1650),
    )


_ZxAnOtdrTestParamPrfWaveLength_Type.__name__ = "Integer32"
_ZxAnOtdrTestParamPrfWaveLength_Object = MibTableColumn
zxAnOtdrTestParamPrfWaveLength = _ZxAnOtdrTestParamPrfWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 2, 1, 3),
    _ZxAnOtdrTestParamPrfWaveLength_Type()
)
zxAnOtdrTestParamPrfWaveLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfWaveLength.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfWaveLength.setUnits("nm")


class _ZxAnOtdrTestParamPrfDistance_Type(Integer32):
    """Custom type zxAnOtdrTestParamPrfDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_ZxAnOtdrTestParamPrfDistance_Type.__name__ = "Integer32"
_ZxAnOtdrTestParamPrfDistance_Object = MibTableColumn
zxAnOtdrTestParamPrfDistance = _ZxAnOtdrTestParamPrfDistance_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 2, 1, 4),
    _ZxAnOtdrTestParamPrfDistance_Type()
)
zxAnOtdrTestParamPrfDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfDistance.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfDistance.setUnits("meter")


class _ZxAnOtdrTestParamPrfFiberIor_Type(Integer32):
    """Custom type zxAnOtdrTestParamPrfFiberIor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1400000, 1500000),
    )


_ZxAnOtdrTestParamPrfFiberIor_Type.__name__ = "Integer32"
_ZxAnOtdrTestParamPrfFiberIor_Object = MibTableColumn
zxAnOtdrTestParamPrfFiberIor = _ZxAnOtdrTestParamPrfFiberIor_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 2, 1, 5),
    _ZxAnOtdrTestParamPrfFiberIor_Type()
)
zxAnOtdrTestParamPrfFiberIor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfFiberIor.setStatus("current")


class _ZxAnOtdrTestParamPrfPulseWidth_Type(Integer32):
    """Custom type zxAnOtdrTestParamPrfPulseWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 20000),
    )


_ZxAnOtdrTestParamPrfPulseWidth_Type.__name__ = "Integer32"
_ZxAnOtdrTestParamPrfPulseWidth_Object = MibTableColumn
zxAnOtdrTestParamPrfPulseWidth = _ZxAnOtdrTestParamPrfPulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 2, 1, 6),
    _ZxAnOtdrTestParamPrfPulseWidth_Type()
)
zxAnOtdrTestParamPrfPulseWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfPulseWidth.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfPulseWidth.setUnits("ns")


class _ZxAnOtdrTestParamPrfDuration_Type(Integer32):
    """Custom type zxAnOtdrTestParamPrfDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 3600),
    )


_ZxAnOtdrTestParamPrfDuration_Type.__name__ = "Integer32"
_ZxAnOtdrTestParamPrfDuration_Object = MibTableColumn
zxAnOtdrTestParamPrfDuration = _ZxAnOtdrTestParamPrfDuration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 2, 1, 7),
    _ZxAnOtdrTestParamPrfDuration_Type()
)
zxAnOtdrTestParamPrfDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfDuration.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfDuration.setUnits("seconds")


class _ZxAnOtdrTestParamPrfSeqCode_Type(Integer32):
    """Custom type zxAnOtdrTestParamPrfSeqCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("complementaryCode", 1),
          ("pseudoRandomCode", 2),
          ("notConfigured", 255))
    )


_ZxAnOtdrTestParamPrfSeqCode_Type.__name__ = "Integer32"
_ZxAnOtdrTestParamPrfSeqCode_Object = MibTableColumn
zxAnOtdrTestParamPrfSeqCode = _ZxAnOtdrTestParamPrfSeqCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 2, 1, 8),
    _ZxAnOtdrTestParamPrfSeqCode_Type()
)
zxAnOtdrTestParamPrfSeqCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfSeqCode.setStatus("current")


class _ZxAnOtdrTestParamPrfSeqCodeLen_Type(Integer32):
    """Custom type zxAnOtdrTestParamPrfSeqCodeLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32000),
    )


_ZxAnOtdrTestParamPrfSeqCodeLen_Type.__name__ = "Integer32"
_ZxAnOtdrTestParamPrfSeqCodeLen_Object = MibTableColumn
zxAnOtdrTestParamPrfSeqCodeLen = _ZxAnOtdrTestParamPrfSeqCodeLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 2, 1, 9),
    _ZxAnOtdrTestParamPrfSeqCodeLen_Type()
)
zxAnOtdrTestParamPrfSeqCodeLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfSeqCodeLen.setStatus("current")


class _ZxAnOtdrTestParamPrfCodeWidth_Type(Integer32):
    """Custom type zxAnOtdrTestParamPrfCodeWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(50, 60),
    )


_ZxAnOtdrTestParamPrfCodeWidth_Type.__name__ = "Integer32"
_ZxAnOtdrTestParamPrfCodeWidth_Object = MibTableColumn
zxAnOtdrTestParamPrfCodeWidth = _ZxAnOtdrTestParamPrfCodeWidth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 2, 1, 10),
    _ZxAnOtdrTestParamPrfCodeWidth_Type()
)
zxAnOtdrTestParamPrfCodeWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfCodeWidth.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfCodeWidth.setUnits("ns")


class _ZxAnOtdrTestParamPrfTimes_Type(Integer32):
    """Custom type zxAnOtdrTestParamPrfTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_ZxAnOtdrTestParamPrfTimes_Type.__name__ = "Integer32"
_ZxAnOtdrTestParamPrfTimes_Object = MibTableColumn
zxAnOtdrTestParamPrfTimes = _ZxAnOtdrTestParamPrfTimes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 2, 1, 11),
    _ZxAnOtdrTestParamPrfTimes_Type()
)
zxAnOtdrTestParamPrfTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfTimes.setStatus("current")


class _ZxAnOtdrTestParamPrfInterval_Type(Integer32):
    """Custom type zxAnOtdrTestParamPrfInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_ZxAnOtdrTestParamPrfInterval_Type.__name__ = "Integer32"
_ZxAnOtdrTestParamPrfInterval_Object = MibTableColumn
zxAnOtdrTestParamPrfInterval = _ZxAnOtdrTestParamPrfInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 2, 1, 12),
    _ZxAnOtdrTestParamPrfInterval_Type()
)
zxAnOtdrTestParamPrfInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfInterval.setUnits("us")
_ZxAnOtdrTestParamPrfRowStatus_Type = RowStatus
_ZxAnOtdrTestParamPrfRowStatus_Object = MibTableColumn
zxAnOtdrTestParamPrfRowStatus = _ZxAnOtdrTestParamPrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 2, 1, 50),
    _ZxAnOtdrTestParamPrfRowStatus_Type()
)
zxAnOtdrTestParamPrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrTestParamPrfRowStatus.setStatus("current")
_ZxAnOtdrIfTable_Object = MibTable
zxAnOtdrIfTable = _ZxAnOtdrIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnOtdrIfTable.setStatus("current")
_ZxAnOtdrIfEntry_Object = MibTableRow
zxAnOtdrIfEntry = _ZxAnOtdrIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 3, 1)
)
zxAnOtdrIfEntry.setIndexNames(
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrIfRack"),
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrIfShelf"),
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrIfSlot"),
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrIfPort"),
)
if mibBuilder.loadTexts:
    zxAnOtdrIfEntry.setStatus("current")
_ZxAnOtdrIfRack_Type = Integer32
_ZxAnOtdrIfRack_Object = MibTableColumn
zxAnOtdrIfRack = _ZxAnOtdrIfRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 3, 1, 1),
    _ZxAnOtdrIfRack_Type()
)
zxAnOtdrIfRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOtdrIfRack.setStatus("current")
_ZxAnOtdrIfShelf_Type = Integer32
_ZxAnOtdrIfShelf_Object = MibTableColumn
zxAnOtdrIfShelf = _ZxAnOtdrIfShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 3, 1, 2),
    _ZxAnOtdrIfShelf_Type()
)
zxAnOtdrIfShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOtdrIfShelf.setStatus("current")
_ZxAnOtdrIfSlot_Type = Integer32
_ZxAnOtdrIfSlot_Object = MibTableColumn
zxAnOtdrIfSlot = _ZxAnOtdrIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 3, 1, 3),
    _ZxAnOtdrIfSlot_Type()
)
zxAnOtdrIfSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOtdrIfSlot.setStatus("current")
_ZxAnOtdrIfPort_Type = Integer32
_ZxAnOtdrIfPort_Object = MibTableColumn
zxAnOtdrIfPort = _ZxAnOtdrIfPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 3, 1, 4),
    _ZxAnOtdrIfPort_Type()
)
zxAnOtdrIfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOtdrIfPort.setStatus("current")


class _ZxAnOtdrIfAlias_Type(DisplayString):
    """Custom type zxAnOtdrIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnOtdrIfAlias_Type.__name__ = "DisplayString"
_ZxAnOtdrIfAlias_Object = MibTableColumn
zxAnOtdrIfAlias = _ZxAnOtdrIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 3, 1, 5),
    _ZxAnOtdrIfAlias_Type()
)
zxAnOtdrIfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOtdrIfAlias.setStatus("current")


class _ZxAnOtdrIfFastTestParamPrf_Type(DisplayString):
    """Custom type zxAnOtdrIfFastTestParamPrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnOtdrIfFastTestParamPrf_Type.__name__ = "DisplayString"
_ZxAnOtdrIfFastTestParamPrf_Object = MibTableColumn
zxAnOtdrIfFastTestParamPrf = _ZxAnOtdrIfFastTestParamPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 3, 1, 6),
    _ZxAnOtdrIfFastTestParamPrf_Type()
)
zxAnOtdrIfFastTestParamPrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOtdrIfFastTestParamPrf.setStatus("current")


class _ZxAnOtdrIfRoutineTestParamPrf_Type(DisplayString):
    """Custom type zxAnOtdrIfRoutineTestParamPrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnOtdrIfRoutineTestParamPrf_Type.__name__ = "DisplayString"
_ZxAnOtdrIfRoutineTestParamPrf_Object = MibTableColumn
zxAnOtdrIfRoutineTestParamPrf = _ZxAnOtdrIfRoutineTestParamPrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 1, 3, 1, 7),
    _ZxAnOtdrIfRoutineTestParamPrf_Type()
)
zxAnOtdrIfRoutineTestParamPrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOtdrIfRoutineTestParamPrf.setStatus("current")
_ZxAnOtdrFastTestObjects_ObjectIdentity = ObjectIdentity
zxAnOtdrFastTestObjects = _ZxAnOtdrFastTestObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2)
)
_ZxAnOtdrFastTestConfObjects_ObjectIdentity = ObjectIdentity
zxAnOtdrFastTestConfObjects = _ZxAnOtdrFastTestConfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 1)
)
_ZxAnOtdrFastTestActionObjects_ObjectIdentity = ObjectIdentity
zxAnOtdrFastTestActionObjects = _ZxAnOtdrFastTestActionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 1, 1)
)


class _ZxAnOtdrFastTestSn_Type(DisplayString):
    """Custom type zxAnOtdrFastTestSn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ZxAnOtdrFastTestSn_Type.__name__ = "DisplayString"
_ZxAnOtdrFastTestSn_Object = MibScalar
zxAnOtdrFastTestSn = _ZxAnOtdrFastTestSn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 1, 1, 1),
    _ZxAnOtdrFastTestSn_Type()
)
zxAnOtdrFastTestSn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOtdrFastTestSn.setStatus("current")


class _ZxAnOtdrFastTestAction_Type(Integer32):
    """Custom type zxAnOtdrFastTestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_ZxAnOtdrFastTestAction_Type.__name__ = "Integer32"
_ZxAnOtdrFastTestAction_Object = MibScalar
zxAnOtdrFastTestAction = _ZxAnOtdrFastTestAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 1, 1, 2),
    _ZxAnOtdrFastTestAction_Type()
)
zxAnOtdrFastTestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOtdrFastTestAction.setStatus("current")
_ZxAnOtdrFastTestIfTable_Object = MibTable
zxAnOtdrFastTestIfTable = _ZxAnOtdrFastTestIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnOtdrFastTestIfTable.setStatus("current")
_ZxAnOtdrFastTestIfEntry_Object = MibTableRow
zxAnOtdrFastTestIfEntry = _ZxAnOtdrFastTestIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 1, 2, 1)
)
zxAnOtdrFastTestIfEntry.setIndexNames(
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrFastTestIfSn"),
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrFastTestIfRack"),
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrFastTestIfShelf"),
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrFastTestIfSlot"),
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrFastTestIfPort"),
)
if mibBuilder.loadTexts:
    zxAnOtdrFastTestIfEntry.setStatus("current")


class _ZxAnOtdrFastTestIfSn_Type(DisplayString):
    """Custom type zxAnOtdrFastTestIfSn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ZxAnOtdrFastTestIfSn_Type.__name__ = "DisplayString"
_ZxAnOtdrFastTestIfSn_Object = MibTableColumn
zxAnOtdrFastTestIfSn = _ZxAnOtdrFastTestIfSn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 1, 2, 1, 1),
    _ZxAnOtdrFastTestIfSn_Type()
)
zxAnOtdrFastTestIfSn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOtdrFastTestIfSn.setStatus("current")
_ZxAnOtdrFastTestIfRack_Type = Integer32
_ZxAnOtdrFastTestIfRack_Object = MibTableColumn
zxAnOtdrFastTestIfRack = _ZxAnOtdrFastTestIfRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 1, 2, 1, 2),
    _ZxAnOtdrFastTestIfRack_Type()
)
zxAnOtdrFastTestIfRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOtdrFastTestIfRack.setStatus("current")
_ZxAnOtdrFastTestIfShelf_Type = Integer32
_ZxAnOtdrFastTestIfShelf_Object = MibTableColumn
zxAnOtdrFastTestIfShelf = _ZxAnOtdrFastTestIfShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 1, 2, 1, 3),
    _ZxAnOtdrFastTestIfShelf_Type()
)
zxAnOtdrFastTestIfShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOtdrFastTestIfShelf.setStatus("current")
_ZxAnOtdrFastTestIfSlot_Type = Integer32
_ZxAnOtdrFastTestIfSlot_Object = MibTableColumn
zxAnOtdrFastTestIfSlot = _ZxAnOtdrFastTestIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 1, 2, 1, 4),
    _ZxAnOtdrFastTestIfSlot_Type()
)
zxAnOtdrFastTestIfSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOtdrFastTestIfSlot.setStatus("current")
_ZxAnOtdrFastTestIfPort_Type = Integer32
_ZxAnOtdrFastTestIfPort_Object = MibTableColumn
zxAnOtdrFastTestIfPort = _ZxAnOtdrFastTestIfPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 1, 2, 1, 5),
    _ZxAnOtdrFastTestIfPort_Type()
)
zxAnOtdrFastTestIfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOtdrFastTestIfPort.setStatus("current")
_ZxAnOtdrFastTestIfRowStatus_Type = RowStatus
_ZxAnOtdrFastTestIfRowStatus_Object = MibTableColumn
zxAnOtdrFastTestIfRowStatus = _ZxAnOtdrFastTestIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 1, 2, 1, 50),
    _ZxAnOtdrFastTestIfRowStatus_Type()
)
zxAnOtdrFastTestIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrFastTestIfRowStatus.setStatus("current")
_ZxAnOtdrFastTestStatusObjects_ObjectIdentity = ObjectIdentity
zxAnOtdrFastTestStatusObjects = _ZxAnOtdrFastTestStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 2)
)
_ZxAnOtdrFastTestStatusGlbObjects_ObjectIdentity = ObjectIdentity
zxAnOtdrFastTestStatusGlbObjects = _ZxAnOtdrFastTestStatusGlbObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 2, 1)
)


class _ZxAnOtdrFastTestCurrentPort_Type(DisplayString):
    """Custom type zxAnOtdrFastTestCurrentPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnOtdrFastTestCurrentPort_Type.__name__ = "DisplayString"
_ZxAnOtdrFastTestCurrentPort_Object = MibScalar
zxAnOtdrFastTestCurrentPort = _ZxAnOtdrFastTestCurrentPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 2, 1, 1),
    _ZxAnOtdrFastTestCurrentPort_Type()
)
zxAnOtdrFastTestCurrentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOtdrFastTestCurrentPort.setStatus("current")


class _ZxAnOtdrFastTestWaitTestPorts_Type(Integer32):
    """Custom type zxAnOtdrFastTestWaitTestPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnOtdrFastTestWaitTestPorts_Type.__name__ = "Integer32"
_ZxAnOtdrFastTestWaitTestPorts_Object = MibScalar
zxAnOtdrFastTestWaitTestPorts = _ZxAnOtdrFastTestWaitTestPorts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 2, 1, 2),
    _ZxAnOtdrFastTestWaitTestPorts_Type()
)
zxAnOtdrFastTestWaitTestPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOtdrFastTestWaitTestPorts.setStatus("current")
_ZxAnOtdrFastTestIfStatusTable_Object = MibTable
zxAnOtdrFastTestIfStatusTable = _ZxAnOtdrFastTestIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnOtdrFastTestIfStatusTable.setStatus("current")
_ZxAnOtdrFastTestIfStatusEntry_Object = MibTableRow
zxAnOtdrFastTestIfStatusEntry = _ZxAnOtdrFastTestIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 2, 2, 1)
)
zxAnOtdrFastTestIfStatusEntry.setIndexNames(
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrFastTestIfSn"),
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrFastTestIfRack"),
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrFastTestIfShelf"),
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrFastTestIfSlot"),
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrFastTestIfPort"),
)
if mibBuilder.loadTexts:
    zxAnOtdrFastTestIfStatusEntry.setStatus("current")


class _ZxAnOtdrFastTestIfStatus_Type(Integer32):
    """Custom type zxAnOtdrFastTestIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notStarted", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4),
          ("stopped", 5))
    )


_ZxAnOtdrFastTestIfStatus_Type.__name__ = "Integer32"
_ZxAnOtdrFastTestIfStatus_Object = MibTableColumn
zxAnOtdrFastTestIfStatus = _ZxAnOtdrFastTestIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 2, 2, 1, 1),
    _ZxAnOtdrFastTestIfStatus_Type()
)
zxAnOtdrFastTestIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOtdrFastTestIfStatus.setStatus("current")


class _ZxAnOtdrFastTestIfFailedReason_Type(Integer32):
    """Custom type zxAnOtdrFastTestIfFailedReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("otherErrors", 255))
    )


_ZxAnOtdrFastTestIfFailedReason_Type.__name__ = "Integer32"
_ZxAnOtdrFastTestIfFailedReason_Object = MibTableColumn
zxAnOtdrFastTestIfFailedReason = _ZxAnOtdrFastTestIfFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 2, 2, 1, 2),
    _ZxAnOtdrFastTestIfFailedReason_Type()
)
zxAnOtdrFastTestIfFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOtdrFastTestIfFailedReason.setStatus("current")


class _ZxAnOtdrFastTestIfResultFile_Type(DisplayString):
    """Custom type zxAnOtdrFastTestIfResultFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnOtdrFastTestIfResultFile_Type.__name__ = "DisplayString"
_ZxAnOtdrFastTestIfResultFile_Object = MibTableColumn
zxAnOtdrFastTestIfResultFile = _ZxAnOtdrFastTestIfResultFile_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 2, 2, 1, 3),
    _ZxAnOtdrFastTestIfResultFile_Type()
)
zxAnOtdrFastTestIfResultFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOtdrFastTestIfResultFile.setStatus("current")
_ZxAnOtdrFastTestFileFtpObjects_ObjectIdentity = ObjectIdentity
zxAnOtdrFastTestFileFtpObjects = _ZxAnOtdrFastTestFileFtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 3)
)
_ZxAnOtdrFileFtpObjects_ObjectIdentity = ObjectIdentity
zxAnOtdrFileFtpObjects = _ZxAnOtdrFileFtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 3, 1)
)


class _ZxAnOtdrFileFtpIpAddressType_Type(InetAddressType):
    """Custom type zxAnOtdrFileFtpIpAddressType based on InetAddressType"""
    defaultValue = 1


_ZxAnOtdrFileFtpIpAddressType_Type.__name__ = "InetAddressType"
_ZxAnOtdrFileFtpIpAddressType_Object = MibScalar
zxAnOtdrFileFtpIpAddressType = _ZxAnOtdrFileFtpIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 3, 1, 1),
    _ZxAnOtdrFileFtpIpAddressType_Type()
)
zxAnOtdrFileFtpIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOtdrFileFtpIpAddressType.setStatus("current")
_ZxAnOtdrFileFtpIpAddress_Type = InetAddress
_ZxAnOtdrFileFtpIpAddress_Object = MibScalar
zxAnOtdrFileFtpIpAddress = _ZxAnOtdrFileFtpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 3, 1, 2),
    _ZxAnOtdrFileFtpIpAddress_Type()
)
zxAnOtdrFileFtpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOtdrFileFtpIpAddress.setStatus("current")


class _ZxAnOtdrFileFtpProtocolType_Type(Integer32):
    """Custom type zxAnOtdrFileFtpProtocolType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("sftp", 2))
    )


_ZxAnOtdrFileFtpProtocolType_Type.__name__ = "Integer32"
_ZxAnOtdrFileFtpProtocolType_Object = MibScalar
zxAnOtdrFileFtpProtocolType = _ZxAnOtdrFileFtpProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 3, 1, 3),
    _ZxAnOtdrFileFtpProtocolType_Type()
)
zxAnOtdrFileFtpProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOtdrFileFtpProtocolType.setStatus("current")


class _ZxAnOtdrFileFtpUserName_Type(DisplayString):
    """Custom type zxAnOtdrFileFtpUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnOtdrFileFtpUserName_Type.__name__ = "DisplayString"
_ZxAnOtdrFileFtpUserName_Object = MibScalar
zxAnOtdrFileFtpUserName = _ZxAnOtdrFileFtpUserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 3, 1, 4),
    _ZxAnOtdrFileFtpUserName_Type()
)
zxAnOtdrFileFtpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOtdrFileFtpUserName.setStatus("current")


class _ZxAnOtdrFileFtpUserPwd_Type(DisplayString):
    """Custom type zxAnOtdrFileFtpUserPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnOtdrFileFtpUserPwd_Type.__name__ = "DisplayString"
_ZxAnOtdrFileFtpUserPwd_Object = MibScalar
zxAnOtdrFileFtpUserPwd = _ZxAnOtdrFileFtpUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 3, 1, 5),
    _ZxAnOtdrFileFtpUserPwd_Type()
)
zxAnOtdrFileFtpUserPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOtdrFileFtpUserPwd.setStatus("current")


class _ZxAnOtdrFileFtpPath_Type(DisplayString):
    """Custom type zxAnOtdrFileFtpPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ZxAnOtdrFileFtpPath_Type.__name__ = "DisplayString"
_ZxAnOtdrFileFtpPath_Object = MibScalar
zxAnOtdrFileFtpPath = _ZxAnOtdrFileFtpPath_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 3, 1, 6),
    _ZxAnOtdrFileFtpPath_Type()
)
zxAnOtdrFileFtpPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOtdrFileFtpPath.setStatus("current")


class _ZxAnOtdrFileFtpFileName_Type(DisplayString):
    """Custom type zxAnOtdrFileFtpFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnOtdrFileFtpFileName_Type.__name__ = "DisplayString"
_ZxAnOtdrFileFtpFileName_Object = MibScalar
zxAnOtdrFileFtpFileName = _ZxAnOtdrFileFtpFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 3, 1, 7),
    _ZxAnOtdrFileFtpFileName_Type()
)
zxAnOtdrFileFtpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOtdrFileFtpFileName.setStatus("current")
_ZxAnOtdrFileFtpUploadStatusTable_Object = MibTable
zxAnOtdrFileFtpUploadStatusTable = _ZxAnOtdrFileFtpUploadStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    zxAnOtdrFileFtpUploadStatusTable.setStatus("current")
_ZxAnOtdrFileFtpUploadStatusEntry_Object = MibTableRow
zxAnOtdrFileFtpUploadStatusEntry = _ZxAnOtdrFileFtpUploadStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 3, 2, 1)
)
zxAnOtdrFileFtpUploadStatusEntry.setIndexNames(
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrFileFtpUploadFileName"),
)
if mibBuilder.loadTexts:
    zxAnOtdrFileFtpUploadStatusEntry.setStatus("current")


class _ZxAnOtdrFileFtpUploadFileName_Type(DisplayString):
    """Custom type zxAnOtdrFileFtpUploadFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnOtdrFileFtpUploadFileName_Type.__name__ = "DisplayString"
_ZxAnOtdrFileFtpUploadFileName_Object = MibTableColumn
zxAnOtdrFileFtpUploadFileName = _ZxAnOtdrFileFtpUploadFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 3, 2, 1, 1),
    _ZxAnOtdrFileFtpUploadFileName_Type()
)
zxAnOtdrFileFtpUploadFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOtdrFileFtpUploadFileName.setStatus("current")


class _ZxAnOtdrFileFtpUploadStatus_Type(Integer32):
    """Custom type zxAnOtdrFileFtpUploadStatus based on Integer32"""
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
        *(("notStarted", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_ZxAnOtdrFileFtpUploadStatus_Type.__name__ = "Integer32"
_ZxAnOtdrFileFtpUploadStatus_Object = MibTableColumn
zxAnOtdrFileFtpUploadStatus = _ZxAnOtdrFileFtpUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 3, 2, 1, 2),
    _ZxAnOtdrFileFtpUploadStatus_Type()
)
zxAnOtdrFileFtpUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOtdrFileFtpUploadStatus.setStatus("current")


class _ZxAnOtdrFileFtpUploadFailReason_Type(Integer32):
    """Custom type zxAnOtdrFileFtpUploadFailReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("fileNotExists", 2),
          ("connectionFailed", 3),
          ("otherErrors", 255))
    )


_ZxAnOtdrFileFtpUploadFailReason_Type.__name__ = "Integer32"
_ZxAnOtdrFileFtpUploadFailReason_Object = MibTableColumn
zxAnOtdrFileFtpUploadFailReason = _ZxAnOtdrFileFtpUploadFailReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 2, 3, 2, 1, 3),
    _ZxAnOtdrFileFtpUploadFailReason_Type()
)
zxAnOtdrFileFtpUploadFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOtdrFileFtpUploadFailReason.setStatus("current")
_ZxAnOtdrRoutineTestObjects_ObjectIdentity = ObjectIdentity
zxAnOtdrRoutineTestObjects = _ZxAnOtdrRoutineTestObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3)
)
_ZxAnOtdrRoutineTaskIfTable_Object = MibTable
zxAnOtdrRoutineTaskIfTable = _ZxAnOtdrRoutineTaskIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 2)
)
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskIfTable.setStatus("current")
_ZxAnOtdrRoutineTaskIfEntry_Object = MibTableRow
zxAnOtdrRoutineTaskIfEntry = _ZxAnOtdrRoutineTaskIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 2, 1)
)
zxAnOtdrRoutineTaskIfEntry.setIndexNames(
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrRoutineTaskName"),
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrRoutineTaskIfRack"),
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrRoutineTaskIfShelf"),
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrRoutineTaskIfSlot"),
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrRoutineTaskIfPort"),
)
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskIfEntry.setStatus("current")
_ZxAnOtdrRoutineTaskIfRack_Type = Integer32
_ZxAnOtdrRoutineTaskIfRack_Object = MibTableColumn
zxAnOtdrRoutineTaskIfRack = _ZxAnOtdrRoutineTaskIfRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 2, 1, 1),
    _ZxAnOtdrRoutineTaskIfRack_Type()
)
zxAnOtdrRoutineTaskIfRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskIfRack.setStatus("current")
_ZxAnOtdrRoutineTaskIfShelf_Type = Integer32
_ZxAnOtdrRoutineTaskIfShelf_Object = MibTableColumn
zxAnOtdrRoutineTaskIfShelf = _ZxAnOtdrRoutineTaskIfShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 2, 1, 2),
    _ZxAnOtdrRoutineTaskIfShelf_Type()
)
zxAnOtdrRoutineTaskIfShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskIfShelf.setStatus("current")
_ZxAnOtdrRoutineTaskIfSlot_Type = Integer32
_ZxAnOtdrRoutineTaskIfSlot_Object = MibTableColumn
zxAnOtdrRoutineTaskIfSlot = _ZxAnOtdrRoutineTaskIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 2, 1, 3),
    _ZxAnOtdrRoutineTaskIfSlot_Type()
)
zxAnOtdrRoutineTaskIfSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskIfSlot.setStatus("current")
_ZxAnOtdrRoutineTaskIfPort_Type = Integer32
_ZxAnOtdrRoutineTaskIfPort_Object = MibTableColumn
zxAnOtdrRoutineTaskIfPort = _ZxAnOtdrRoutineTaskIfPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 2, 1, 4),
    _ZxAnOtdrRoutineTaskIfPort_Type()
)
zxAnOtdrRoutineTaskIfPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskIfPort.setStatus("current")
_ZxAnOtdrRoutineTaskIfRowStatus_Type = RowStatus
_ZxAnOtdrRoutineTaskIfRowStatus_Object = MibTableColumn
zxAnOtdrRoutineTaskIfRowStatus = _ZxAnOtdrRoutineTaskIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 2, 1, 50),
    _ZxAnOtdrRoutineTaskIfRowStatus_Type()
)
zxAnOtdrRoutineTaskIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskIfRowStatus.setStatus("current")
_ZxAnOtdrRoutineTaskTable_Object = MibTable
zxAnOtdrRoutineTaskTable = _ZxAnOtdrRoutineTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 3)
)
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskTable.setStatus("current")
_ZxAnOtdrRoutineTaskEntry_Object = MibTableRow
zxAnOtdrRoutineTaskEntry = _ZxAnOtdrRoutineTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 3, 1)
)
zxAnOtdrRoutineTaskEntry.setIndexNames(
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrRoutineTaskName"),
)
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskEntry.setStatus("current")


class _ZxAnOtdrRoutineTaskName_Type(DisplayString):
    """Custom type zxAnOtdrRoutineTaskName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnOtdrRoutineTaskName_Type.__name__ = "DisplayString"
_ZxAnOtdrRoutineTaskName_Object = MibTableColumn
zxAnOtdrRoutineTaskName = _ZxAnOtdrRoutineTaskName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 3, 1, 1),
    _ZxAnOtdrRoutineTaskName_Type()
)
zxAnOtdrRoutineTaskName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskName.setStatus("current")
_ZxAnOtdrRoutineTaskStartTime_Type = DateAndTime
_ZxAnOtdrRoutineTaskStartTime_Object = MibTableColumn
zxAnOtdrRoutineTaskStartTime = _ZxAnOtdrRoutineTaskStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 3, 1, 2),
    _ZxAnOtdrRoutineTaskStartTime_Type()
)
zxAnOtdrRoutineTaskStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskStartTime.setStatus("current")


class _ZxAnOtdrRoutineTaskInterval_Type(Integer32):
    """Custom type zxAnOtdrRoutineTaskInterval based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 525600),
    )


_ZxAnOtdrRoutineTaskInterval_Type.__name__ = "Integer32"
_ZxAnOtdrRoutineTaskInterval_Object = MibTableColumn
zxAnOtdrRoutineTaskInterval = _ZxAnOtdrRoutineTaskInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 3, 1, 3),
    _ZxAnOtdrRoutineTaskInterval_Type()
)
zxAnOtdrRoutineTaskInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskInterval.setUnits("minutes")


class _ZxAnOtdrRoutineTaskActiveStatus_Type(Integer32):
    """Custom type zxAnOtdrRoutineTaskActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("stopped", 2))
    )


_ZxAnOtdrRoutineTaskActiveStatus_Type.__name__ = "Integer32"
_ZxAnOtdrRoutineTaskActiveStatus_Object = MibTableColumn
zxAnOtdrRoutineTaskActiveStatus = _ZxAnOtdrRoutineTaskActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 3, 1, 4),
    _ZxAnOtdrRoutineTaskActiveStatus_Type()
)
zxAnOtdrRoutineTaskActiveStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskActiveStatus.setStatus("current")
_ZxAnOtdrRoutineTaskCurrStartTime_Type = DateAndTime
_ZxAnOtdrRoutineTaskCurrStartTime_Object = MibTableColumn
zxAnOtdrRoutineTaskCurrStartTime = _ZxAnOtdrRoutineTaskCurrStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 3, 1, 5),
    _ZxAnOtdrRoutineTaskCurrStartTime_Type()
)
zxAnOtdrRoutineTaskCurrStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskCurrStartTime.setStatus("current")


class _ZxAnOtdrRoutineTaskOperStatus_Type(Integer32):
    """Custom type zxAnOtdrRoutineTaskOperStatus based on Integer32"""
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
        *(("notStarted", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_ZxAnOtdrRoutineTaskOperStatus_Type.__name__ = "Integer32"
_ZxAnOtdrRoutineTaskOperStatus_Object = MibTableColumn
zxAnOtdrRoutineTaskOperStatus = _ZxAnOtdrRoutineTaskOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 3, 1, 6),
    _ZxAnOtdrRoutineTaskOperStatus_Type()
)
zxAnOtdrRoutineTaskOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskOperStatus.setStatus("current")


class _ZxAnOtdrRoutineTaskFailedReason_Type(Integer32):
    """Custom type zxAnOtdrRoutineTaskFailedReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("otherErrors", 255))
    )


_ZxAnOtdrRoutineTaskFailedReason_Type.__name__ = "Integer32"
_ZxAnOtdrRoutineTaskFailedReason_Object = MibTableColumn
zxAnOtdrRoutineTaskFailedReason = _ZxAnOtdrRoutineTaskFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 3, 1, 7),
    _ZxAnOtdrRoutineTaskFailedReason_Type()
)
zxAnOtdrRoutineTaskFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskFailedReason.setStatus("current")


class _ZxAnOtdrRoutineTaskResultFile_Type(DisplayString):
    """Custom type zxAnOtdrRoutineTaskResultFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnOtdrRoutineTaskResultFile_Type.__name__ = "DisplayString"
_ZxAnOtdrRoutineTaskResultFile_Object = MibTableColumn
zxAnOtdrRoutineTaskResultFile = _ZxAnOtdrRoutineTaskResultFile_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 3, 1, 8),
    _ZxAnOtdrRoutineTaskResultFile_Type()
)
zxAnOtdrRoutineTaskResultFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskResultFile.setStatus("current")
_ZxAnOtdrRoutineTaskRowStatus_Type = RowStatus
_ZxAnOtdrRoutineTaskRowStatus_Object = MibTableColumn
zxAnOtdrRoutineTaskRowStatus = _ZxAnOtdrRoutineTaskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 3, 1, 50),
    _ZxAnOtdrRoutineTaskRowStatus_Type()
)
zxAnOtdrRoutineTaskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskRowStatus.setStatus("current")
_ZxAnOtdrRoutineTaskIfStatusTable_Object = MibTable
zxAnOtdrRoutineTaskIfStatusTable = _ZxAnOtdrRoutineTaskIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 4)
)
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskIfStatusTable.setStatus("current")
_ZxAnOtdrRoutineTaskIfStatusEntry_Object = MibTableRow
zxAnOtdrRoutineTaskIfStatusEntry = _ZxAnOtdrRoutineTaskIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 4, 1)
)
zxAnOtdrRoutineTaskIfStatusEntry.setIndexNames(
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrRoutineTaskIfRack"),
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrRoutineTaskIfShelf"),
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrRoutineTaskIfSlot"),
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrRoutineTaskIfPort"),
)
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskIfStatusEntry.setStatus("current")


class _ZxAnOtdrRoutineTaskIfStatus_Type(Integer32):
    """Custom type zxAnOtdrRoutineTaskIfStatus based on Integer32"""
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
        *(("notStarted", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_ZxAnOtdrRoutineTaskIfStatus_Type.__name__ = "Integer32"
_ZxAnOtdrRoutineTaskIfStatus_Object = MibTableColumn
zxAnOtdrRoutineTaskIfStatus = _ZxAnOtdrRoutineTaskIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 4, 1, 1),
    _ZxAnOtdrRoutineTaskIfStatus_Type()
)
zxAnOtdrRoutineTaskIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskIfStatus.setStatus("current")


class _ZxAnOtdrRoutineTaskIfFailReason_Type(Integer32):
    """Custom type zxAnOtdrRoutineTaskIfFailReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("otherErrors", 255))
    )


_ZxAnOtdrRoutineTaskIfFailReason_Type.__name__ = "Integer32"
_ZxAnOtdrRoutineTaskIfFailReason_Object = MibTableColumn
zxAnOtdrRoutineTaskIfFailReason = _ZxAnOtdrRoutineTaskIfFailReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 3, 4, 1, 2),
    _ZxAnOtdrRoutineTaskIfFailReason_Type()
)
zxAnOtdrRoutineTaskIfFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskIfFailReason.setStatus("current")
_ZxAnOtdrFtpServerObjects_ObjectIdentity = ObjectIdentity
zxAnOtdrFtpServerObjects = _ZxAnOtdrFtpServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 4)
)
_ZxAnOtdrFtpServerTable_Object = MibTable
zxAnOtdrFtpServerTable = _ZxAnOtdrFtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 4, 2)
)
if mibBuilder.loadTexts:
    zxAnOtdrFtpServerTable.setStatus("current")
_ZxAnOtdrFtpServerEntry_Object = MibTableRow
zxAnOtdrFtpServerEntry = _ZxAnOtdrFtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 4, 2, 1)
)
zxAnOtdrFtpServerEntry.setIndexNames(
    (0, "ZTE-AN-OTDR-MIB", "zxAnOtdrFtpServerId"),
)
if mibBuilder.loadTexts:
    zxAnOtdrFtpServerEntry.setStatus("current")


class _ZxAnOtdrFtpServerId_Type(DisplayString):
    """Custom type zxAnOtdrFtpServerId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnOtdrFtpServerId_Type.__name__ = "DisplayString"
_ZxAnOtdrFtpServerId_Object = MibTableColumn
zxAnOtdrFtpServerId = _ZxAnOtdrFtpServerId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 4, 2, 1, 1),
    _ZxAnOtdrFtpServerId_Type()
)
zxAnOtdrFtpServerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnOtdrFtpServerId.setStatus("current")


class _ZxAnOtdrFtpServerIpAddressType_Type(InetAddressType):
    """Custom type zxAnOtdrFtpServerIpAddressType based on InetAddressType"""
    defaultValue = 1


_ZxAnOtdrFtpServerIpAddressType_Type.__name__ = "InetAddressType"
_ZxAnOtdrFtpServerIpAddressType_Object = MibTableColumn
zxAnOtdrFtpServerIpAddressType = _ZxAnOtdrFtpServerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 4, 2, 1, 2),
    _ZxAnOtdrFtpServerIpAddressType_Type()
)
zxAnOtdrFtpServerIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrFtpServerIpAddressType.setStatus("current")
_ZxAnOtdrFtpServerIpAddress_Type = InetAddress
_ZxAnOtdrFtpServerIpAddress_Object = MibTableColumn
zxAnOtdrFtpServerIpAddress = _ZxAnOtdrFtpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 4, 2, 1, 3),
    _ZxAnOtdrFtpServerIpAddress_Type()
)
zxAnOtdrFtpServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrFtpServerIpAddress.setStatus("current")


class _ZxAnOtdrFtpServerProtocolType_Type(Integer32):
    """Custom type zxAnOtdrFtpServerProtocolType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("sftp", 2))
    )


_ZxAnOtdrFtpServerProtocolType_Type.__name__ = "Integer32"
_ZxAnOtdrFtpServerProtocolType_Object = MibTableColumn
zxAnOtdrFtpServerProtocolType = _ZxAnOtdrFtpServerProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 4, 2, 1, 4),
    _ZxAnOtdrFtpServerProtocolType_Type()
)
zxAnOtdrFtpServerProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrFtpServerProtocolType.setStatus("current")


class _ZxAnOtdrFtpServerUserName_Type(DisplayString):
    """Custom type zxAnOtdrFtpServerUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnOtdrFtpServerUserName_Type.__name__ = "DisplayString"
_ZxAnOtdrFtpServerUserName_Object = MibTableColumn
zxAnOtdrFtpServerUserName = _ZxAnOtdrFtpServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 4, 2, 1, 5),
    _ZxAnOtdrFtpServerUserName_Type()
)
zxAnOtdrFtpServerUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrFtpServerUserName.setStatus("current")


class _ZxAnOtdrFtpServerUserPwd_Type(DisplayString):
    """Custom type zxAnOtdrFtpServerUserPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnOtdrFtpServerUserPwd_Type.__name__ = "DisplayString"
_ZxAnOtdrFtpServerUserPwd_Object = MibTableColumn
zxAnOtdrFtpServerUserPwd = _ZxAnOtdrFtpServerUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 4, 2, 1, 6),
    _ZxAnOtdrFtpServerUserPwd_Type()
)
zxAnOtdrFtpServerUserPwd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrFtpServerUserPwd.setStatus("current")


class _ZxAnOtdrFtpServerPath_Type(DisplayString):
    """Custom type zxAnOtdrFtpServerPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ZxAnOtdrFtpServerPath_Type.__name__ = "DisplayString"
_ZxAnOtdrFtpServerPath_Object = MibTableColumn
zxAnOtdrFtpServerPath = _ZxAnOtdrFtpServerPath_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 4, 2, 1, 7),
    _ZxAnOtdrFtpServerPath_Type()
)
zxAnOtdrFtpServerPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrFtpServerPath.setStatus("current")
_ZxAnOtdrFtpServerRowStatus_Type = RowStatus
_ZxAnOtdrFtpServerRowStatus_Object = MibTableColumn
zxAnOtdrFtpServerRowStatus = _ZxAnOtdrFtpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 2, 4, 2, 1, 50),
    _ZxAnOtdrFtpServerRowStatus_Type()
)
zxAnOtdrFtpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnOtdrFtpServerRowStatus.setStatus("current")
_ZxAnOtdrNotifications_ObjectIdentity = ObjectIdentity
zxAnOtdrNotifications = _ZxAnOtdrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 3)
)
_ZxAnOtdrEnvTraps_ObjectIdentity = ObjectIdentity
zxAnOtdrEnvTraps = _ZxAnOtdrEnvTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 3, 50)
)

# Managed Objects groups


# Notification objects

zxAnOtdrRoutineTaskFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 3, 1)
)
zxAnOtdrRoutineTaskFinished.setObjects(
      *(("ZTE-AN-OTDR-MIB", "zxAnOtdrRoutineTaskCurrStartTime"),
        ("ZTE-AN-OTDR-MIB", "zxAnOtdrRoutineTaskOperStatus"),
        ("ZTE-AN-OTDR-MIB", "zxAnOtdrRoutineTaskFailedReason"),
        ("ZTE-AN-OTDR-MIB", "zxAnOtdrRoutineTaskResultFile"))
)
if mibBuilder.loadTexts:
    zxAnOtdrRoutineTaskFinished.setStatus(
        "current"
    )

zxAnOtdrEnvCtrlCardHighTempAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 3, 50, 1)
)
zxAnOtdrEnvCtrlCardHighTempAlm.setObjects(
      *(("ZTE-AN-OTDR-MIB", "zxAnOtdrCtrlCardCurrentTemp"),
        ("ZTE-AN-OTDR-MIB", "zxAnOtdrCtrlCardTempHighThresh"))
)
if mibBuilder.loadTexts:
    zxAnOtdrEnvCtrlCardHighTempAlm.setStatus(
        "current"
    )

zxAnOtdrEnvCtrlCardHighTempClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 3, 50, 2)
)
zxAnOtdrEnvCtrlCardHighTempClr.setObjects(
      *(("ZTE-AN-OTDR-MIB", "zxAnOtdrCtrlCardCurrentTemp"),
        ("ZTE-AN-OTDR-MIB", "zxAnOtdrCtrlCardTempHighThresh"))
)
if mibBuilder.loadTexts:
    zxAnOtdrEnvCtrlCardHighTempClr.setStatus(
        "current"
    )

zxAnOtdrEnvCtrlCardLowTempAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 3, 50, 3)
)
zxAnOtdrEnvCtrlCardLowTempAlm.setObjects(
      *(("ZTE-AN-OTDR-MIB", "zxAnOtdrCtrlCardCurrentTemp"),
        ("ZTE-AN-OTDR-MIB", "zxAnOtdrCtrlCardTempLowThresh"))
)
if mibBuilder.loadTexts:
    zxAnOtdrEnvCtrlCardLowTempAlm.setStatus(
        "current"
    )

zxAnOtdrEnvCtrlCardLowTempClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 3, 50, 4)
)
zxAnOtdrEnvCtrlCardLowTempClr.setObjects(
      *(("ZTE-AN-OTDR-MIB", "zxAnOtdrCtrlCardCurrentTemp"),
        ("ZTE-AN-OTDR-MIB", "zxAnOtdrCtrlCardTempLowThresh"))
)
if mibBuilder.loadTexts:
    zxAnOtdrEnvCtrlCardLowTempClr.setStatus(
        "current"
    )

zxAnOtdrEnvFanFailureAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 3, 50, 5)
)
zxAnOtdrEnvFanFailureAlm.setObjects(
      *(("ZTE-AN-OTDR-MIB", "zxAnOtdrEnvFanStatus"),
        ("ZTE-AN-OTDR-MIB", "zxAnOtdrEnvFanOperStatus"))
)
if mibBuilder.loadTexts:
    zxAnOtdrEnvFanFailureAlm.setStatus(
        "current"
    )

zxAnOtdrEnvFanFailureClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 3, 50, 6)
)
zxAnOtdrEnvFanFailureClr.setObjects(
      *(("ZTE-AN-OTDR-MIB", "zxAnOtdrEnvFanStatus"),
        ("ZTE-AN-OTDR-MIB", "zxAnOtdrEnvFanOperStatus"))
)
if mibBuilder.loadTexts:
    zxAnOtdrEnvFanFailureClr.setStatus(
        "current"
    )

zxAnOtdrEnvApdHighTempAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 3, 50, 7)
)
zxAnOtdrEnvApdHighTempAlm.setObjects(
      *(("ZTE-AN-OTDR-MIB", "zxAnOtdrEnvApdCurrentTemp"),
        ("ZTE-AN-OTDR-MIB", "zxAnOtdrEnvApdTempHighThresh"))
)
if mibBuilder.loadTexts:
    zxAnOtdrEnvApdHighTempAlm.setStatus(
        "current"
    )

zxAnOtdrEnvApdHighTempClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 3, 50, 8)
)
zxAnOtdrEnvApdHighTempClr.setObjects(
      *(("ZTE-AN-OTDR-MIB", "zxAnOtdrEnvApdCurrentTemp"),
        ("ZTE-AN-OTDR-MIB", "zxAnOtdrEnvApdTempHighThresh"))
)
if mibBuilder.loadTexts:
    zxAnOtdrEnvApdHighTempClr.setStatus(
        "current"
    )

zxAnOtdrEnvApdLowTempAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 3, 50, 9)
)
zxAnOtdrEnvApdLowTempAlm.setObjects(
      *(("ZTE-AN-OTDR-MIB", "zxAnOtdrEnvApdCurrentTemp"),
        ("ZTE-AN-OTDR-MIB", "zxAnOtdrEnvApdTempLowThresh"))
)
if mibBuilder.loadTexts:
    zxAnOtdrEnvApdLowTempAlm.setStatus(
        "current"
    )

zxAnOtdrEnvApdLowTempClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1083, 5, 3, 50, 10)
)
zxAnOtdrEnvApdLowTempClr.setObjects(
      *(("ZTE-AN-OTDR-MIB", "zxAnOtdrApdCurrentTemperature"),
        ("ZTE-AN-OTDR-MIB", "zxAnOtdrEnvApdCurrentTemp"))
)
if mibBuilder.loadTexts:
    zxAnOtdrEnvApdLowTempClr.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-OTDR-MIB",
    **{"zxAnOtdrMib": zxAnOtdrMib,
       "zxAnOtdrGlobalObjects": zxAnOtdrGlobalObjects,
       "zxAnOtdrCapacityGlobalObjects": zxAnOtdrCapacityGlobalObjects,
       "zxAnOtdrWaveLengthList": zxAnOtdrWaveLengthList,
       "zxAnOtdrTestPulseWidthList": zxAnOtdrTestPulseWidthList,
       "zxAnOtdrTotalPorts": zxAnOtdrTotalPorts,
       "zxAnOtdrEnvGlobalObjects": zxAnOtdrEnvGlobalObjects,
       "zxAnOtdrEnvCtrlCardGlobalObjects": zxAnOtdrEnvCtrlCardGlobalObjects,
       "zxAnOtdrCtrlCardCurrentTemp": zxAnOtdrCtrlCardCurrentTemp,
       "zxAnOtdrCtrlCardTempHighThresh": zxAnOtdrCtrlCardTempHighThresh,
       "zxAnOtdrCtrlCardTempLowThresh": zxAnOtdrCtrlCardTempLowThresh,
       "zxAnOtdrEnvFanGlobalObjects": zxAnOtdrEnvFanGlobalObjects,
       "zxAnOtdrEnvFanStatus": zxAnOtdrEnvFanStatus,
       "zxAnOtdrEnvFanOperStatus": zxAnOtdrEnvFanOperStatus,
       "zxAnOtdrEnvApdGlobalObjects": zxAnOtdrEnvApdGlobalObjects,
       "zxAnOtdrEnvApdCurrentTemp": zxAnOtdrEnvApdCurrentTemp,
       "zxAnOtdrEnvApdTempHighThresh": zxAnOtdrEnvApdTempHighThresh,
       "zxAnOtdrEnvApdTempLowThresh": zxAnOtdrEnvApdTempLowThresh,
       "zxAnOtdrObjects": zxAnOtdrObjects,
       "zxAnOtdrIfObjects": zxAnOtdrIfObjects,
       "zxAnOtdrTestParamPrfTable": zxAnOtdrTestParamPrfTable,
       "zxAnOtdrTestParamPrfEntry": zxAnOtdrTestParamPrfEntry,
       "zxAnOtdrTestParamPrfName": zxAnOtdrTestParamPrfName,
       "zxAnOtdrTestParamPrfMode": zxAnOtdrTestParamPrfMode,
       "zxAnOtdrTestParamPrfWaveLength": zxAnOtdrTestParamPrfWaveLength,
       "zxAnOtdrTestParamPrfDistance": zxAnOtdrTestParamPrfDistance,
       "zxAnOtdrTestParamPrfFiberIor": zxAnOtdrTestParamPrfFiberIor,
       "zxAnOtdrTestParamPrfPulseWidth": zxAnOtdrTestParamPrfPulseWidth,
       "zxAnOtdrTestParamPrfDuration": zxAnOtdrTestParamPrfDuration,
       "zxAnOtdrTestParamPrfSeqCode": zxAnOtdrTestParamPrfSeqCode,
       "zxAnOtdrTestParamPrfSeqCodeLen": zxAnOtdrTestParamPrfSeqCodeLen,
       "zxAnOtdrTestParamPrfCodeWidth": zxAnOtdrTestParamPrfCodeWidth,
       "zxAnOtdrTestParamPrfTimes": zxAnOtdrTestParamPrfTimes,
       "zxAnOtdrTestParamPrfInterval": zxAnOtdrTestParamPrfInterval,
       "zxAnOtdrTestParamPrfRowStatus": zxAnOtdrTestParamPrfRowStatus,
       "zxAnOtdrIfTable": zxAnOtdrIfTable,
       "zxAnOtdrIfEntry": zxAnOtdrIfEntry,
       "zxAnOtdrIfRack": zxAnOtdrIfRack,
       "zxAnOtdrIfShelf": zxAnOtdrIfShelf,
       "zxAnOtdrIfSlot": zxAnOtdrIfSlot,
       "zxAnOtdrIfPort": zxAnOtdrIfPort,
       "zxAnOtdrIfAlias": zxAnOtdrIfAlias,
       "zxAnOtdrIfFastTestParamPrf": zxAnOtdrIfFastTestParamPrf,
       "zxAnOtdrIfRoutineTestParamPrf": zxAnOtdrIfRoutineTestParamPrf,
       "zxAnOtdrFastTestObjects": zxAnOtdrFastTestObjects,
       "zxAnOtdrFastTestConfObjects": zxAnOtdrFastTestConfObjects,
       "zxAnOtdrFastTestActionObjects": zxAnOtdrFastTestActionObjects,
       "zxAnOtdrFastTestSn": zxAnOtdrFastTestSn,
       "zxAnOtdrFastTestAction": zxAnOtdrFastTestAction,
       "zxAnOtdrFastTestIfTable": zxAnOtdrFastTestIfTable,
       "zxAnOtdrFastTestIfEntry": zxAnOtdrFastTestIfEntry,
       "zxAnOtdrFastTestIfSn": zxAnOtdrFastTestIfSn,
       "zxAnOtdrFastTestIfRack": zxAnOtdrFastTestIfRack,
       "zxAnOtdrFastTestIfShelf": zxAnOtdrFastTestIfShelf,
       "zxAnOtdrFastTestIfSlot": zxAnOtdrFastTestIfSlot,
       "zxAnOtdrFastTestIfPort": zxAnOtdrFastTestIfPort,
       "zxAnOtdrFastTestIfRowStatus": zxAnOtdrFastTestIfRowStatus,
       "zxAnOtdrFastTestStatusObjects": zxAnOtdrFastTestStatusObjects,
       "zxAnOtdrFastTestStatusGlbObjects": zxAnOtdrFastTestStatusGlbObjects,
       "zxAnOtdrFastTestCurrentPort": zxAnOtdrFastTestCurrentPort,
       "zxAnOtdrFastTestWaitTestPorts": zxAnOtdrFastTestWaitTestPorts,
       "zxAnOtdrFastTestIfStatusTable": zxAnOtdrFastTestIfStatusTable,
       "zxAnOtdrFastTestIfStatusEntry": zxAnOtdrFastTestIfStatusEntry,
       "zxAnOtdrFastTestIfStatus": zxAnOtdrFastTestIfStatus,
       "zxAnOtdrFastTestIfFailedReason": zxAnOtdrFastTestIfFailedReason,
       "zxAnOtdrFastTestIfResultFile": zxAnOtdrFastTestIfResultFile,
       "zxAnOtdrFastTestFileFtpObjects": zxAnOtdrFastTestFileFtpObjects,
       "zxAnOtdrFileFtpObjects": zxAnOtdrFileFtpObjects,
       "zxAnOtdrFileFtpIpAddressType": zxAnOtdrFileFtpIpAddressType,
       "zxAnOtdrFileFtpIpAddress": zxAnOtdrFileFtpIpAddress,
       "zxAnOtdrFileFtpProtocolType": zxAnOtdrFileFtpProtocolType,
       "zxAnOtdrFileFtpUserName": zxAnOtdrFileFtpUserName,
       "zxAnOtdrFileFtpUserPwd": zxAnOtdrFileFtpUserPwd,
       "zxAnOtdrFileFtpPath": zxAnOtdrFileFtpPath,
       "zxAnOtdrFileFtpFileName": zxAnOtdrFileFtpFileName,
       "zxAnOtdrFileFtpUploadStatusTable": zxAnOtdrFileFtpUploadStatusTable,
       "zxAnOtdrFileFtpUploadStatusEntry": zxAnOtdrFileFtpUploadStatusEntry,
       "zxAnOtdrFileFtpUploadFileName": zxAnOtdrFileFtpUploadFileName,
       "zxAnOtdrFileFtpUploadStatus": zxAnOtdrFileFtpUploadStatus,
       "zxAnOtdrFileFtpUploadFailReason": zxAnOtdrFileFtpUploadFailReason,
       "zxAnOtdrRoutineTestObjects": zxAnOtdrRoutineTestObjects,
       "zxAnOtdrRoutineTaskIfTable": zxAnOtdrRoutineTaskIfTable,
       "zxAnOtdrRoutineTaskIfEntry": zxAnOtdrRoutineTaskIfEntry,
       "zxAnOtdrRoutineTaskIfRack": zxAnOtdrRoutineTaskIfRack,
       "zxAnOtdrRoutineTaskIfShelf": zxAnOtdrRoutineTaskIfShelf,
       "zxAnOtdrRoutineTaskIfSlot": zxAnOtdrRoutineTaskIfSlot,
       "zxAnOtdrRoutineTaskIfPort": zxAnOtdrRoutineTaskIfPort,
       "zxAnOtdrRoutineTaskIfRowStatus": zxAnOtdrRoutineTaskIfRowStatus,
       "zxAnOtdrRoutineTaskTable": zxAnOtdrRoutineTaskTable,
       "zxAnOtdrRoutineTaskEntry": zxAnOtdrRoutineTaskEntry,
       "zxAnOtdrRoutineTaskName": zxAnOtdrRoutineTaskName,
       "zxAnOtdrRoutineTaskStartTime": zxAnOtdrRoutineTaskStartTime,
       "zxAnOtdrRoutineTaskInterval": zxAnOtdrRoutineTaskInterval,
       "zxAnOtdrRoutineTaskActiveStatus": zxAnOtdrRoutineTaskActiveStatus,
       "zxAnOtdrRoutineTaskCurrStartTime": zxAnOtdrRoutineTaskCurrStartTime,
       "zxAnOtdrRoutineTaskOperStatus": zxAnOtdrRoutineTaskOperStatus,
       "zxAnOtdrRoutineTaskFailedReason": zxAnOtdrRoutineTaskFailedReason,
       "zxAnOtdrRoutineTaskResultFile": zxAnOtdrRoutineTaskResultFile,
       "zxAnOtdrRoutineTaskRowStatus": zxAnOtdrRoutineTaskRowStatus,
       "zxAnOtdrRoutineTaskIfStatusTable": zxAnOtdrRoutineTaskIfStatusTable,
       "zxAnOtdrRoutineTaskIfStatusEntry": zxAnOtdrRoutineTaskIfStatusEntry,
       "zxAnOtdrRoutineTaskIfStatus": zxAnOtdrRoutineTaskIfStatus,
       "zxAnOtdrRoutineTaskIfFailReason": zxAnOtdrRoutineTaskIfFailReason,
       "zxAnOtdrFtpServerObjects": zxAnOtdrFtpServerObjects,
       "zxAnOtdrFtpServerTable": zxAnOtdrFtpServerTable,
       "zxAnOtdrFtpServerEntry": zxAnOtdrFtpServerEntry,
       "zxAnOtdrFtpServerId": zxAnOtdrFtpServerId,
       "zxAnOtdrFtpServerIpAddressType": zxAnOtdrFtpServerIpAddressType,
       "zxAnOtdrFtpServerIpAddress": zxAnOtdrFtpServerIpAddress,
       "zxAnOtdrFtpServerProtocolType": zxAnOtdrFtpServerProtocolType,
       "zxAnOtdrFtpServerUserName": zxAnOtdrFtpServerUserName,
       "zxAnOtdrFtpServerUserPwd": zxAnOtdrFtpServerUserPwd,
       "zxAnOtdrFtpServerPath": zxAnOtdrFtpServerPath,
       "zxAnOtdrFtpServerRowStatus": zxAnOtdrFtpServerRowStatus,
       "zxAnOtdrNotifications": zxAnOtdrNotifications,
       "zxAnOtdrRoutineTaskFinished": zxAnOtdrRoutineTaskFinished,
       "zxAnOtdrEnvTraps": zxAnOtdrEnvTraps,
       "zxAnOtdrEnvCtrlCardHighTempAlm": zxAnOtdrEnvCtrlCardHighTempAlm,
       "zxAnOtdrEnvCtrlCardHighTempClr": zxAnOtdrEnvCtrlCardHighTempClr,
       "zxAnOtdrEnvCtrlCardLowTempAlm": zxAnOtdrEnvCtrlCardLowTempAlm,
       "zxAnOtdrEnvCtrlCardLowTempClr": zxAnOtdrEnvCtrlCardLowTempClr,
       "zxAnOtdrEnvFanFailureAlm": zxAnOtdrEnvFanFailureAlm,
       "zxAnOtdrEnvFanFailureClr": zxAnOtdrEnvFanFailureClr,
       "zxAnOtdrEnvApdHighTempAlm": zxAnOtdrEnvApdHighTempAlm,
       "zxAnOtdrEnvApdHighTempClr": zxAnOtdrEnvApdHighTempClr,
       "zxAnOtdrEnvApdLowTempAlm": zxAnOtdrEnvApdLowTempAlm,
       "zxAnOtdrEnvApdLowTempClr": zxAnOtdrEnvApdLowTempClr}
)
