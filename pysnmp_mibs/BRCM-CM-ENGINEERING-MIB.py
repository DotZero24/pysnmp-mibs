# SNMP MIB module (BRCM-CM-ENGINEERING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-CM-ENGINEERING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:07:57 2025
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

(cableDataEngineering,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-ENGINEERING-MIB",
    "cableDataEngineering")

(cmDsCalOffsetIndex,) = mibBuilder.importSymbols(
    "BRCM-CM-FACTORY-MIB",
    "cmDsCalOffsetIndex")

(TenthdB,
 TenthdBmV) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdB",
    "TenthdBmV")

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
 RowPointer,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cablemodemEngineering = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cablemodemEngineering.setRevisions(
        ("2011-04-14 00:00",
         "2010-10-20 00:00",
         "2009-10-06 00:00",
         "2009-04-03 00:00",
         "2008-11-03 00:00",
         "2008-09-23 00:00",
         "2007-02-05 00:00",
         "2003-06-23 00:00",
         "2003-04-24 00:00",
         "2003-01-03 00:00",
         "2002-12-23 00:00",
         "2002-12-11 00:00",
         "2002-11-11 00:00",
         "2002-10-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmEngrBase_ObjectIdentity = ObjectIdentity
cmEngrBase = _CmEngrBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 1)
)
_CmEngr33xxOpcode_Type = Unsigned32
_CmEngr33xxOpcode_Object = MibScalar
cmEngr33xxOpcode = _CmEngr33xxOpcode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 1, 1),
    _CmEngr33xxOpcode_Type()
)
cmEngr33xxOpcode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEngr33xxOpcode.setStatus("current")
_CmEngr33xxData_Type = Unsigned32
_CmEngr33xxData_Object = MibScalar
cmEngr33xxData = _CmEngr33xxData_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 1, 2),
    _CmEngr33xxData_Type()
)
cmEngr33xxData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEngr33xxData.setStatus("current")


class _CmEngr33xxCommand_Type(Integer32):
    """Custom type cmEngr33xxCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("read", 0),
          ("write", 1))
    )


_CmEngr33xxCommand_Type.__name__ = "Integer32"
_CmEngr33xxCommand_Object = MibScalar
cmEngr33xxCommand = _CmEngr33xxCommand_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 1, 3),
    _CmEngr33xxCommand_Type()
)
cmEngr33xxCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmEngr33xxCommand.setStatus("current")
_CmEngrDownstreamCalibration_ObjectIdentity = ObjectIdentity
cmEngrDownstreamCalibration = _CmEngrDownstreamCalibration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2)
)
_CmDsCalZeroTunerCoefs_Type = TruthValue
_CmDsCalZeroTunerCoefs_Object = MibScalar
cmDsCalZeroTunerCoefs = _CmDsCalZeroTunerCoefs_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 1),
    _CmDsCalZeroTunerCoefs_Type()
)
cmDsCalZeroTunerCoefs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalZeroTunerCoefs.setStatus("current")


class _CmDsCalNumTunerCoefs_Type(Unsigned32):
    """Custom type cmDsCalNumTunerCoefs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CmDsCalNumTunerCoefs_Type.__name__ = "Unsigned32"
_CmDsCalNumTunerCoefs_Object = MibScalar
cmDsCalNumTunerCoefs = _CmDsCalNumTunerCoefs_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 2),
    _CmDsCalNumTunerCoefs_Type()
)
cmDsCalNumTunerCoefs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalNumTunerCoefs.setStatus("current")
_CmDsCalTunerCoefTable_Object = MibTable
cmDsCalTunerCoefTable = _CmDsCalTunerCoefTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 3)
)
if mibBuilder.loadTexts:
    cmDsCalTunerCoefTable.setStatus("current")
_CmDsCalTunerCoefEntry_Object = MibTableRow
cmDsCalTunerCoefEntry = _CmDsCalTunerCoefEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 3, 1)
)
cmDsCalTunerCoefEntry.setIndexNames(
    (0, "BRCM-CM-FACTORY-MIB", "cmDsCalOffsetIndex"),
    (0, "BRCM-CM-ENGINEERING-MIB", "cmDsCalTunerCoefIndex"),
)
if mibBuilder.loadTexts:
    cmDsCalTunerCoefEntry.setStatus("current")


class _CmDsCalTunerCoefIndex_Type(Integer32):
    """Custom type cmDsCalTunerCoefIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CmDsCalTunerCoefIndex_Type.__name__ = "Integer32"
_CmDsCalTunerCoefIndex_Object = MibTableColumn
cmDsCalTunerCoefIndex = _CmDsCalTunerCoefIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 3, 1, 1),
    _CmDsCalTunerCoefIndex_Type()
)
cmDsCalTunerCoefIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmDsCalTunerCoefIndex.setStatus("current")
_CmDsCalTunerCoefFrequency_Type = Integer32
_CmDsCalTunerCoefFrequency_Object = MibTableColumn
cmDsCalTunerCoefFrequency = _CmDsCalTunerCoefFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 3, 1, 2),
    _CmDsCalTunerCoefFrequency_Type()
)
cmDsCalTunerCoefFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalTunerCoefFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalTunerCoefFrequency.setUnits("hertz")


class _CmDsCalTunerCoefValue_Type(Unsigned32):
    """Custom type cmDsCalTunerCoefValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CmDsCalTunerCoefValue_Type.__name__ = "Unsigned32"
_CmDsCalTunerCoefValue_Object = MibTableColumn
cmDsCalTunerCoefValue = _CmDsCalTunerCoefValue_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 3, 1, 3),
    _CmDsCalTunerCoefValue_Type()
)
cmDsCalTunerCoefValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalTunerCoefValue.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalTunerCoefValue.setUnits("millionth")
_CmDsCalTunerCoefCopyFrom_Type = Integer32
_CmDsCalTunerCoefCopyFrom_Object = MibTableColumn
cmDsCalTunerCoefCopyFrom = _CmDsCalTunerCoefCopyFrom_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 3, 1, 4),
    _CmDsCalTunerCoefCopyFrom_Type()
)
cmDsCalTunerCoefCopyFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalTunerCoefCopyFrom.setStatus("current")
_CmDsCalZeroIFCoefs_Type = TruthValue
_CmDsCalZeroIFCoefs_Object = MibScalar
cmDsCalZeroIFCoefs = _CmDsCalZeroIFCoefs_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 4),
    _CmDsCalZeroIFCoefs_Type()
)
cmDsCalZeroIFCoefs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalZeroIFCoefs.setStatus("current")


class _CmDsCalNumIFCoefs_Type(Unsigned32):
    """Custom type cmDsCalNumIFCoefs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CmDsCalNumIFCoefs_Type.__name__ = "Unsigned32"
_CmDsCalNumIFCoefs_Object = MibScalar
cmDsCalNumIFCoefs = _CmDsCalNumIFCoefs_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 5),
    _CmDsCalNumIFCoefs_Type()
)
cmDsCalNumIFCoefs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalNumIFCoefs.setStatus("current")
_CmDsCalIFCoefTable_Object = MibTable
cmDsCalIFCoefTable = _CmDsCalIFCoefTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 6)
)
if mibBuilder.loadTexts:
    cmDsCalIFCoefTable.setStatus("current")
_CmDsCalIFCoefEntry_Object = MibTableRow
cmDsCalIFCoefEntry = _CmDsCalIFCoefEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 6, 1)
)
cmDsCalIFCoefEntry.setIndexNames(
    (0, "BRCM-CM-FACTORY-MIB", "cmDsCalOffsetIndex"),
    (0, "BRCM-CM-ENGINEERING-MIB", "cmDsCalIFCoefIndex"),
)
if mibBuilder.loadTexts:
    cmDsCalIFCoefEntry.setStatus("current")


class _CmDsCalIFCoefIndex_Type(Integer32):
    """Custom type cmDsCalIFCoefIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CmDsCalIFCoefIndex_Type.__name__ = "Integer32"
_CmDsCalIFCoefIndex_Object = MibTableColumn
cmDsCalIFCoefIndex = _CmDsCalIFCoefIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 6, 1, 1),
    _CmDsCalIFCoefIndex_Type()
)
cmDsCalIFCoefIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmDsCalIFCoefIndex.setStatus("current")
_CmDsCalIFCoefFrequency_Type = Integer32
_CmDsCalIFCoefFrequency_Object = MibTableColumn
cmDsCalIFCoefFrequency = _CmDsCalIFCoefFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 6, 1, 2),
    _CmDsCalIFCoefFrequency_Type()
)
cmDsCalIFCoefFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalIFCoefFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalIFCoefFrequency.setUnits("hertz")
_CmDsCalIFCoefValue_Type = Integer32
_CmDsCalIFCoefValue_Object = MibTableColumn
cmDsCalIFCoefValue = _CmDsCalIFCoefValue_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 6, 1, 3),
    _CmDsCalIFCoefValue_Type()
)
cmDsCalIFCoefValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalIFCoefValue.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalIFCoefValue.setUnits("hundred-thousandth")
_CmDsCalIFCoefCopyFrom_Type = Integer32
_CmDsCalIFCoefCopyFrom_Object = MibTableColumn
cmDsCalIFCoefCopyFrom = _CmDsCalIFCoefCopyFrom_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 6, 1, 4),
    _CmDsCalIFCoefCopyFrom_Type()
)
cmDsCalIFCoefCopyFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalIFCoefCopyFrom.setStatus("current")
_CmDsCalZeroFineCoefs_Type = TruthValue
_CmDsCalZeroFineCoefs_Object = MibScalar
cmDsCalZeroFineCoefs = _CmDsCalZeroFineCoefs_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 7),
    _CmDsCalZeroFineCoefs_Type()
)
cmDsCalZeroFineCoefs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalZeroFineCoefs.setStatus("current")


class _CmDsCalNumFineCoefs_Type(Unsigned32):
    """Custom type cmDsCalNumFineCoefs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CmDsCalNumFineCoefs_Type.__name__ = "Unsigned32"
_CmDsCalNumFineCoefs_Object = MibScalar
cmDsCalNumFineCoefs = _CmDsCalNumFineCoefs_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 8),
    _CmDsCalNumFineCoefs_Type()
)
cmDsCalNumFineCoefs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalNumFineCoefs.setStatus("current")
_CmDsCalFineCoefTable_Object = MibTable
cmDsCalFineCoefTable = _CmDsCalFineCoefTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 9)
)
if mibBuilder.loadTexts:
    cmDsCalFineCoefTable.setStatus("current")
_CmDsCalFineCoefEntry_Object = MibTableRow
cmDsCalFineCoefEntry = _CmDsCalFineCoefEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 9, 1)
)
cmDsCalFineCoefEntry.setIndexNames(
    (0, "BRCM-CM-FACTORY-MIB", "cmDsCalOffsetIndex"),
    (0, "BRCM-CM-ENGINEERING-MIB", "cmDsCalFineCoefIndex"),
)
if mibBuilder.loadTexts:
    cmDsCalFineCoefEntry.setStatus("current")


class _CmDsCalFineCoefIndex_Type(Integer32):
    """Custom type cmDsCalFineCoefIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CmDsCalFineCoefIndex_Type.__name__ = "Integer32"
_CmDsCalFineCoefIndex_Object = MibTableColumn
cmDsCalFineCoefIndex = _CmDsCalFineCoefIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 9, 1, 1),
    _CmDsCalFineCoefIndex_Type()
)
cmDsCalFineCoefIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmDsCalFineCoefIndex.setStatus("current")
_CmDsCalFineCoefFrequency_Type = Integer32
_CmDsCalFineCoefFrequency_Object = MibTableColumn
cmDsCalFineCoefFrequency = _CmDsCalFineCoefFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 9, 1, 2),
    _CmDsCalFineCoefFrequency_Type()
)
cmDsCalFineCoefFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalFineCoefFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalFineCoefFrequency.setUnits("hertz")
_CmDsCalFineCoefValue_Type = Integer32
_CmDsCalFineCoefValue_Object = MibTableColumn
cmDsCalFineCoefValue = _CmDsCalFineCoefValue_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 9, 1, 3),
    _CmDsCalFineCoefValue_Type()
)
cmDsCalFineCoefValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalFineCoefValue.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalFineCoefValue.setUnits("millionth")
_CmDsCalFineCoefCopyFrom_Type = Integer32
_CmDsCalFineCoefCopyFrom_Object = MibTableColumn
cmDsCalFineCoefCopyFrom = _CmDsCalFineCoefCopyFrom_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 9, 1, 4),
    _CmDsCalFineCoefCopyFrom_Type()
)
cmDsCalFineCoefCopyFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalFineCoefCopyFrom.setStatus("current")
_CmDsCalZeroEqCoefs_Type = TruthValue
_CmDsCalZeroEqCoefs_Object = MibScalar
cmDsCalZeroEqCoefs = _CmDsCalZeroEqCoefs_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 10),
    _CmDsCalZeroEqCoefs_Type()
)
cmDsCalZeroEqCoefs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalZeroEqCoefs.setStatus("current")


class _CmDsCalNumEqCoefs_Type(Unsigned32):
    """Custom type cmDsCalNumEqCoefs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CmDsCalNumEqCoefs_Type.__name__ = "Unsigned32"
_CmDsCalNumEqCoefs_Object = MibScalar
cmDsCalNumEqCoefs = _CmDsCalNumEqCoefs_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 11),
    _CmDsCalNumEqCoefs_Type()
)
cmDsCalNumEqCoefs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalNumEqCoefs.setStatus("current")
_CmDsCalEqCoefTable_Object = MibTable
cmDsCalEqCoefTable = _CmDsCalEqCoefTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 12)
)
if mibBuilder.loadTexts:
    cmDsCalEqCoefTable.setStatus("current")
_CmDsCalEqCoefEntry_Object = MibTableRow
cmDsCalEqCoefEntry = _CmDsCalEqCoefEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 12, 1)
)
cmDsCalEqCoefEntry.setIndexNames(
    (0, "BRCM-CM-FACTORY-MIB", "cmDsCalOffsetIndex"),
    (0, "BRCM-CM-ENGINEERING-MIB", "cmDsCalEqCoefIndex"),
)
if mibBuilder.loadTexts:
    cmDsCalEqCoefEntry.setStatus("current")


class _CmDsCalEqCoefIndex_Type(Integer32):
    """Custom type cmDsCalEqCoefIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CmDsCalEqCoefIndex_Type.__name__ = "Integer32"
_CmDsCalEqCoefIndex_Object = MibTableColumn
cmDsCalEqCoefIndex = _CmDsCalEqCoefIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 12, 1, 1),
    _CmDsCalEqCoefIndex_Type()
)
cmDsCalEqCoefIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmDsCalEqCoefIndex.setStatus("current")
_CmDsCalEqCoefFrequency_Type = Integer32
_CmDsCalEqCoefFrequency_Object = MibTableColumn
cmDsCalEqCoefFrequency = _CmDsCalEqCoefFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 12, 1, 2),
    _CmDsCalEqCoefFrequency_Type()
)
cmDsCalEqCoefFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalEqCoefFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalEqCoefFrequency.setUnits("hertz")
_CmDsCalEqCoefValue_Type = Integer32
_CmDsCalEqCoefValue_Object = MibTableColumn
cmDsCalEqCoefValue = _CmDsCalEqCoefValue_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 12, 1, 3),
    _CmDsCalEqCoefValue_Type()
)
cmDsCalEqCoefValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalEqCoefValue.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalEqCoefValue.setUnits("hundred-thousandth")
_CmDsCalEqCoefCopyFrom_Type = Integer32
_CmDsCalEqCoefCopyFrom_Object = MibTableColumn
cmDsCalEqCoefCopyFrom = _CmDsCalEqCoefCopyFrom_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 12, 1, 4),
    _CmDsCalEqCoefCopyFrom_Type()
)
cmDsCalEqCoefCopyFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalEqCoefCopyFrom.setStatus("current")


class _CmDsCalNumLDAIxReads_Type(Unsigned32):
    """Custom type cmDsCalNumLDAIxReads based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmDsCalNumLDAIxReads_Type.__name__ = "Unsigned32"
_CmDsCalNumLDAIxReads_Object = MibScalar
cmDsCalNumLDAIxReads = _CmDsCalNumLDAIxReads_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 13),
    _CmDsCalNumLDAIxReads_Type()
)
cmDsCalNumLDAIxReads.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalNumLDAIxReads.setStatus("current")


class _CmDsCalLDAIxReadInterval_Type(Unsigned32):
    """Custom type cmDsCalLDAIxReadInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmDsCalLDAIxReadInterval_Type.__name__ = "Unsigned32"
_CmDsCalLDAIxReadInterval_Object = MibScalar
cmDsCalLDAIxReadInterval = _CmDsCalLDAIxReadInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 14),
    _CmDsCalLDAIxReadInterval_Type()
)
cmDsCalLDAIxReadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalLDAIxReadInterval.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalLDAIxReadInterval.setUnits("milliseconds")


class _CmDsCalTunerStep_Type(Unsigned32):
    """Custom type cmDsCalTunerStep based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 800),
    )


_CmDsCalTunerStep_Type.__name__ = "Unsigned32"
_CmDsCalTunerStep_Object = MibScalar
cmDsCalTunerStep = _CmDsCalTunerStep_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 15),
    _CmDsCalTunerStep_Type()
)
cmDsCalTunerStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalTunerStep.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalTunerStep.setUnits("hundredth dBmV")


class _CmDsCalMasterPowerOffset_Type(Integer32):
    """Custom type cmDsCalMasterPowerOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32700, 32700),
    )


_CmDsCalMasterPowerOffset_Type.__name__ = "Integer32"
_CmDsCalMasterPowerOffset_Object = MibScalar
cmDsCalMasterPowerOffset = _CmDsCalMasterPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 16),
    _CmDsCalMasterPowerOffset_Type()
)
cmDsCalMasterPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalMasterPowerOffset.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalMasterPowerOffset.setUnits("hundredth dBmV")
_CmDsCalCharacterizeNow_Type = TruthValue
_CmDsCalCharacterizeNow_Object = MibScalar
cmDsCalCharacterizeNow = _CmDsCalCharacterizeNow_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 17),
    _CmDsCalCharacterizeNow_Type()
)
cmDsCalCharacterizeNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalCharacterizeNow.setStatus("current")
_CmDsCalNormalLDAIT_Type = Unsigned32
_CmDsCalNormalLDAIT_Object = MibScalar
cmDsCalNormalLDAIT = _CmDsCalNormalLDAIT_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 18),
    _CmDsCalNormalLDAIT_Type()
)
cmDsCalNormalLDAIT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalNormalLDAIT.setStatus("current")
_CmDsCalNormalLDAIF_Type = Unsigned32
_CmDsCalNormalLDAIF_Object = MibScalar
cmDsCalNormalLDAIF = _CmDsCalNormalLDAIF_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 19),
    _CmDsCalNormalLDAIF_Type()
)
cmDsCalNormalLDAIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalNormalLDAIF.setStatus("current")
_CmDsCalNormalLDAII_Type = Unsigned32
_CmDsCalNormalLDAII_Object = MibScalar
cmDsCalNormalLDAII = _CmDsCalNormalLDAII_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 20),
    _CmDsCalNormalLDAII_Type()
)
cmDsCalNormalLDAII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalNormalLDAII.setStatus("current")
_CmDsCalFrozenLDAIT_Type = Unsigned32
_CmDsCalFrozenLDAIT_Object = MibScalar
cmDsCalFrozenLDAIT = _CmDsCalFrozenLDAIT_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 21),
    _CmDsCalFrozenLDAIT_Type()
)
cmDsCalFrozenLDAIT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalFrozenLDAIT.setStatus("current")
_CmDsCalFrozenLDAIF_Type = Unsigned32
_CmDsCalFrozenLDAIF_Object = MibScalar
cmDsCalFrozenLDAIF = _CmDsCalFrozenLDAIF_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 22),
    _CmDsCalFrozenLDAIF_Type()
)
cmDsCalFrozenLDAIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalFrozenLDAIF.setStatus("current")
_CmDsCalFrozenLDAII_Type = Unsigned32
_CmDsCalFrozenLDAII_Object = MibScalar
cmDsCalFrozenLDAII = _CmDsCalFrozenLDAII_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 23),
    _CmDsCalFrozenLDAII_Type()
)
cmDsCalFrozenLDAII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalFrozenLDAII.setStatus("current")
_CmDsCalFGainTap_Type = Unsigned32
_CmDsCalFGainTap_Object = MibScalar
cmDsCalFGainTap = _CmDsCalFGainTap_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 24),
    _CmDsCalFGainTap_Type()
)
cmDsCalFGainTap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalFGainTap.setStatus("current")
_CmDsCalTGainTap_Type = Unsigned32
_CmDsCalTGainTap_Object = MibScalar
cmDsCalTGainTap = _CmDsCalTGainTap_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 25),
    _CmDsCalTGainTap_Type()
)
cmDsCalTGainTap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalTGainTap.setStatus("current")
_CmDsCalIGainTap_Type = Unsigned32
_CmDsCalIGainTap_Object = MibScalar
cmDsCalIGainTap = _CmDsCalIGainTap_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 26),
    _CmDsCalIGainTap_Type()
)
cmDsCalIGainTap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalIGainTap.setStatus("current")
_CmDsCalFrequencyError_Type = Integer32
_CmDsCalFrequencyError_Object = MibScalar
cmDsCalFrequencyError = _CmDsCalFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 27),
    _CmDsCalFrequencyError_Type()
)
cmDsCalFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalFrequencyError.setUnits("hertz")
_CmDsCalTunerCoefTablePopulate_Type = TruthValue
_CmDsCalTunerCoefTablePopulate_Object = MibScalar
cmDsCalTunerCoefTablePopulate = _CmDsCalTunerCoefTablePopulate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 28),
    _CmDsCalTunerCoefTablePopulate_Type()
)
cmDsCalTunerCoefTablePopulate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalTunerCoefTablePopulate.setStatus("current")
_CmDsCalIFCoefTablePopulate_Type = TruthValue
_CmDsCalIFCoefTablePopulate_Object = MibScalar
cmDsCalIFCoefTablePopulate = _CmDsCalIFCoefTablePopulate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 29),
    _CmDsCalIFCoefTablePopulate_Type()
)
cmDsCalIFCoefTablePopulate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalIFCoefTablePopulate.setStatus("current")
_CmDsCalFineCoefTablePopulate_Type = TruthValue
_CmDsCalFineCoefTablePopulate_Object = MibScalar
cmDsCalFineCoefTablePopulate = _CmDsCalFineCoefTablePopulate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 30),
    _CmDsCalFineCoefTablePopulate_Type()
)
cmDsCalFineCoefTablePopulate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalFineCoefTablePopulate.setStatus("current")
_CmDsCalEqCoefTablePopulate_Type = TruthValue
_CmDsCalEqCoefTablePopulate_Object = MibScalar
cmDsCalEqCoefTablePopulate = _CmDsCalEqCoefTablePopulate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 31),
    _CmDsCalEqCoefTablePopulate_Type()
)
cmDsCalEqCoefTablePopulate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalEqCoefTablePopulate.setStatus("current")
_CmDsCalTunerTable_Object = MibTable
cmDsCalTunerTable = _CmDsCalTunerTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 32)
)
if mibBuilder.loadTexts:
    cmDsCalTunerTable.setStatus("current")
_CmDsCalTunerEntry_Object = MibTableRow
cmDsCalTunerEntry = _CmDsCalTunerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 32, 1)
)
cmDsCalTunerEntry.setIndexNames(
    (0, "BRCM-CM-ENGINEERING-MIB", "cmDsCalTunerIndex"),
)
if mibBuilder.loadTexts:
    cmDsCalTunerEntry.setStatus("current")


class _CmDsCalTunerIndex_Type(Integer32):
    """Custom type cmDsCalTunerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CmDsCalTunerIndex_Type.__name__ = "Integer32"
_CmDsCalTunerIndex_Object = MibTableColumn
cmDsCalTunerIndex = _CmDsCalTunerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 32, 1, 1),
    _CmDsCalTunerIndex_Type()
)
cmDsCalTunerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmDsCalTunerIndex.setStatus("current")


class _CmDsCalTunerType_Type(Integer32):
    """Custom type cmDsCalTunerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("temic473x", 1),
          ("temic4937", 2),
          ("celISG2000", 3),
          ("celISG2000EU", 4),
          ("celISG3300", 5),
          ("celISG3300EU", 6),
          ("celISG3300DS", 7),
          ("celISG3300DSEU", 8),
          ("panasonicET10", 9),
          ("panasonicET03", 10),
          ("alps", 11),
          ("bcm3400", 12),
          ("temic4706", 13),
          ("bcm3415", 14),
          ("alpsEU", 15),
          ("philips1236", 16),
          ("vendor", 17),
          ("bcm3416", 18),
          ("bcm3419", 19),
          ("bcm3418", 20),
          ("bcm3420", 21),
          ("bcm3421", 22),
          ("bcm3422", 23),
          ("bcmInternal", 24))
    )


_CmDsCalTunerType_Type.__name__ = "Integer32"
_CmDsCalTunerType_Object = MibTableColumn
cmDsCalTunerType = _CmDsCalTunerType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 32, 1, 2),
    _CmDsCalTunerType_Type()
)
cmDsCalTunerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalTunerType.setStatus("current")


class _CmDsCalTunerNumChannels_Type(Integer32):
    """Custom type cmDsCalTunerNumChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_CmDsCalTunerNumChannels_Type.__name__ = "Integer32"
_CmDsCalTunerNumChannels_Object = MibTableColumn
cmDsCalTunerNumChannels = _CmDsCalTunerNumChannels_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 32, 1, 3),
    _CmDsCalTunerNumChannels_Type()
)
cmDsCalTunerNumChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalTunerNumChannels.setStatus("current")


class _CmDsCalTunerFrequency_Type(Integer32):
    """Custom type cmDsCalTunerFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CmDsCalTunerFrequency_Type.__name__ = "Integer32"
_CmDsCalTunerFrequency_Object = MibTableColumn
cmDsCalTunerFrequency = _CmDsCalTunerFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 32, 1, 4),
    _CmDsCalTunerFrequency_Type()
)
cmDsCalTunerFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalTunerFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalTunerFrequency.setUnits("hertz")
_CmDsCalTunerTuneNow_Type = TruthValue
_CmDsCalTunerTuneNow_Object = MibTableColumn
cmDsCalTunerTuneNow = _CmDsCalTunerTuneNow_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 32, 1, 5),
    _CmDsCalTunerTuneNow_Type()
)
cmDsCalTunerTuneNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalTunerTuneNow.setStatus("current")
_CmDsCalPhyTable_Object = MibTable
cmDsCalPhyTable = _CmDsCalPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 33)
)
if mibBuilder.loadTexts:
    cmDsCalPhyTable.setStatus("current")
_CmDsCalPhyEntry_Object = MibTableRow
cmDsCalPhyEntry = _CmDsCalPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 33, 1)
)
cmDsCalPhyEntry.setIndexNames(
    (0, "BRCM-CM-ENGINEERING-MIB", "cmDsCalPhyIndex"),
)
if mibBuilder.loadTexts:
    cmDsCalPhyEntry.setStatus("current")


class _CmDsCalPhyIndex_Type(Integer32):
    """Custom type cmDsCalPhyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_CmDsCalPhyIndex_Type.__name__ = "Integer32"
_CmDsCalPhyIndex_Object = MibTableColumn
cmDsCalPhyIndex = _CmDsCalPhyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 33, 1, 1),
    _CmDsCalPhyIndex_Type()
)
cmDsCalPhyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmDsCalPhyIndex.setStatus("current")


class _CmDsCalPhyTuner_Type(Integer32):
    """Custom type cmDsCalPhyTuner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CmDsCalPhyTuner_Type.__name__ = "Integer32"
_CmDsCalPhyTuner_Object = MibTableColumn
cmDsCalPhyTuner = _CmDsCalPhyTuner_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 33, 1, 2),
    _CmDsCalPhyTuner_Type()
)
cmDsCalPhyTuner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalPhyTuner.setStatus("current")


class _CmDsCalPhyTunerChannel_Type(Integer32):
    """Custom type cmDsCalPhyTunerChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-8, 8),
    )


_CmDsCalPhyTunerChannel_Type.__name__ = "Integer32"
_CmDsCalPhyTunerChannel_Object = MibTableColumn
cmDsCalPhyTunerChannel = _CmDsCalPhyTunerChannel_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 33, 1, 3),
    _CmDsCalPhyTunerChannel_Type()
)
cmDsCalPhyTunerChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalPhyTunerChannel.setStatus("current")


class _CmDsCalPhyModulation_Type(Integer32):
    """Custom type cmDsCalPhyModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("qam64", 3),
          ("qam256", 4),
          ("qam1024", 5))
    )


_CmDsCalPhyModulation_Type.__name__ = "Integer32"
_CmDsCalPhyModulation_Object = MibTableColumn
cmDsCalPhyModulation = _CmDsCalPhyModulation_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 33, 1, 4),
    _CmDsCalPhyModulation_Type()
)
cmDsCalPhyModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalPhyModulation.setStatus("current")
_CmDsCalPhyLockNow_Type = TruthValue
_CmDsCalPhyLockNow_Object = MibTableColumn
cmDsCalPhyLockNow = _CmDsCalPhyLockNow_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 33, 1, 5),
    _CmDsCalPhyLockNow_Type()
)
cmDsCalPhyLockNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmDsCalPhyLockNow.setStatus("current")
_CmDsCalPhyQamLocked_Type = TruthValue
_CmDsCalPhyQamLocked_Object = MibTableColumn
cmDsCalPhyQamLocked = _CmDsCalPhyQamLocked_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 33, 1, 6),
    _CmDsCalPhyQamLocked_Type()
)
cmDsCalPhyQamLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalPhyQamLocked.setStatus("current")
_CmDsCalPhyFecLocked_Type = TruthValue
_CmDsCalPhyFecLocked_Object = MibTableColumn
cmDsCalPhyFecLocked = _CmDsCalPhyFecLocked_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 33, 1, 7),
    _CmDsCalPhyFecLocked_Type()
)
cmDsCalPhyFecLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalPhyFecLocked.setStatus("current")
_CmDsCalPhySignalNoise_Type = TenthdB
_CmDsCalPhySignalNoise_Object = MibTableColumn
cmDsCalPhySignalNoise = _CmDsCalPhySignalNoise_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 33, 1, 8),
    _CmDsCalPhySignalNoise_Type()
)
cmDsCalPhySignalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalPhySignalNoise.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalPhySignalNoise.setUnits("TenthdB")
_CmDsCalPhyPower_Type = TenthdBmV
_CmDsCalPhyPower_Object = MibTableColumn
cmDsCalPhyPower = _CmDsCalPhyPower_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 33, 1, 9),
    _CmDsCalPhyPower_Type()
)
cmDsCalPhyPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalPhyPower.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalPhyPower.setUnits("dBmV")
_CmDsCalPhyFrequency_Type = Integer32
_CmDsCalPhyFrequency_Object = MibTableColumn
cmDsCalPhyFrequency = _CmDsCalPhyFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 33, 1, 10),
    _CmDsCalPhyFrequency_Type()
)
cmDsCalPhyFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalPhyFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalPhyFrequency.setUnits("hertz")
_CmDsCalPhyFrequencyError_Type = Integer32
_CmDsCalPhyFrequencyError_Object = MibTableColumn
cmDsCalPhyFrequencyError = _CmDsCalPhyFrequencyError_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 33, 1, 11),
    _CmDsCalPhyFrequencyError_Type()
)
cmDsCalPhyFrequencyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalPhyFrequencyError.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalPhyFrequencyError.setUnits("hertz")
_CmDsCalPhySymbolRate_Type = Integer32
_CmDsCalPhySymbolRate_Object = MibTableColumn
cmDsCalPhySymbolRate = _CmDsCalPhySymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 2, 33, 1, 12),
    _CmDsCalPhySymbolRate_Type()
)
cmDsCalPhySymbolRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmDsCalPhySymbolRate.setStatus("current")
if mibBuilder.loadTexts:
    cmDsCalPhySymbolRate.setUnits("symbols per second")
_CmEngrUpstreamCalibration_ObjectIdentity = ObjectIdentity
cmEngrUpstreamCalibration = _CmEngrUpstreamCalibration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3)
)


class _CmUsCalControlStartPower_Type(Integer32):
    """Custom type cmUsCalControlStartPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmUsCalControlStartPower_Type.__name__ = "Integer32"
_CmUsCalControlStartPower_Object = MibScalar
cmUsCalControlStartPower = _CmUsCalControlStartPower_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3, 1),
    _CmUsCalControlStartPower_Type()
)
cmUsCalControlStartPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalControlStartPower.setStatus("current")
if mibBuilder.loadTexts:
    cmUsCalControlStartPower.setUnits("dBmV")


class _CmUsCalControlEndPower_Type(Integer32):
    """Custom type cmUsCalControlEndPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmUsCalControlEndPower_Type.__name__ = "Integer32"
_CmUsCalControlEndPower_Object = MibScalar
cmUsCalControlEndPower = _CmUsCalControlEndPower_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3, 2),
    _CmUsCalControlEndPower_Type()
)
cmUsCalControlEndPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalControlEndPower.setStatus("current")
if mibBuilder.loadTexts:
    cmUsCalControlEndPower.setUnits("dBmV")


class _CmUsCalControlResolution_Type(Integer32):
    """Custom type cmUsCalControlResolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmUsCalControlResolution_Type.__name__ = "Integer32"
_CmUsCalControlResolution_Object = MibScalar
cmUsCalControlResolution = _CmUsCalControlResolution_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3, 3),
    _CmUsCalControlResolution_Type()
)
cmUsCalControlResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalControlResolution.setStatus("current")
if mibBuilder.loadTexts:
    cmUsCalControlResolution.setUnits("hundredth dBmV")
_CmUsCalZeroControl_Type = TruthValue
_CmUsCalZeroControl_Object = MibScalar
cmUsCalZeroControl = _CmUsCalZeroControl_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3, 4),
    _CmUsCalZeroControl_Type()
)
cmUsCalZeroControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalZeroControl.setStatus("current")
_CmUsCalControlTable_Object = MibTable
cmUsCalControlTable = _CmUsCalControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3, 5)
)
if mibBuilder.loadTexts:
    cmUsCalControlTable.setStatus("current")
_CmUsCalControlEntry_Object = MibTableRow
cmUsCalControlEntry = _CmUsCalControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3, 5, 1)
)
cmUsCalControlEntry.setIndexNames(
    (0, "BRCM-CM-ENGINEERING-MIB", "cmUsCalControlIndex"),
)
if mibBuilder.loadTexts:
    cmUsCalControlEntry.setStatus("current")


class _CmUsCalControlIndex_Type(Integer32):
    """Custom type cmUsCalControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CmUsCalControlIndex_Type.__name__ = "Integer32"
_CmUsCalControlIndex_Object = MibTableColumn
cmUsCalControlIndex = _CmUsCalControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3, 5, 1, 1),
    _CmUsCalControlIndex_Type()
)
cmUsCalControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmUsCalControlIndex.setStatus("current")


class _CmUsCalControlPower_Type(Integer32):
    """Custom type cmUsCalControlPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmUsCalControlPower_Type.__name__ = "Integer32"
_CmUsCalControlPower_Object = MibTableColumn
cmUsCalControlPower = _CmUsCalControlPower_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3, 5, 1, 2),
    _CmUsCalControlPower_Type()
)
cmUsCalControlPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmUsCalControlPower.setStatus("current")
if mibBuilder.loadTexts:
    cmUsCalControlPower.setUnits("hundredth dBmV")


class _CmUsCalControlAmpGain_Type(Unsigned32):
    """Custom type cmUsCalControlAmpGain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmUsCalControlAmpGain_Type.__name__ = "Unsigned32"
_CmUsCalControlAmpGain_Object = MibTableColumn
cmUsCalControlAmpGain = _CmUsCalControlAmpGain_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3, 5, 1, 3),
    _CmUsCalControlAmpGain_Type()
)
cmUsCalControlAmpGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalControlAmpGain.setStatus("current")


class _CmUsCalControlDacAtten_Type(Unsigned32):
    """Custom type cmUsCalControlDacAtten based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmUsCalControlDacAtten_Type.__name__ = "Unsigned32"
_CmUsCalControlDacAtten_Object = MibTableColumn
cmUsCalControlDacAtten = _CmUsCalControlDacAtten_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3, 5, 1, 4),
    _CmUsCalControlDacAtten_Type()
)
cmUsCalControlDacAtten.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalControlDacAtten.setStatus("current")


class _CmUsCalOffsetStartFreq_Type(Integer32):
    """Custom type cmUsCalOffsetStartFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmUsCalOffsetStartFreq_Type.__name__ = "Integer32"
_CmUsCalOffsetStartFreq_Object = MibScalar
cmUsCalOffsetStartFreq = _CmUsCalOffsetStartFreq_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3, 6),
    _CmUsCalOffsetStartFreq_Type()
)
cmUsCalOffsetStartFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalOffsetStartFreq.setStatus("current")
if mibBuilder.loadTexts:
    cmUsCalOffsetStartFreq.setUnits("megahertz")


class _CmUsCalOffsetEndFreq_Type(Integer32):
    """Custom type cmUsCalOffsetEndFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmUsCalOffsetEndFreq_Type.__name__ = "Integer32"
_CmUsCalOffsetEndFreq_Object = MibScalar
cmUsCalOffsetEndFreq = _CmUsCalOffsetEndFreq_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3, 7),
    _CmUsCalOffsetEndFreq_Type()
)
cmUsCalOffsetEndFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalOffsetEndFreq.setStatus("current")
if mibBuilder.loadTexts:
    cmUsCalOffsetEndFreq.setUnits("megahertz")


class _CmUsCalOffsetResolution_Type(Integer32):
    """Custom type cmUsCalOffsetResolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmUsCalOffsetResolution_Type.__name__ = "Integer32"
_CmUsCalOffsetResolution_Object = MibScalar
cmUsCalOffsetResolution = _CmUsCalOffsetResolution_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3, 8),
    _CmUsCalOffsetResolution_Type()
)
cmUsCalOffsetResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalOffsetResolution.setStatus("current")
if mibBuilder.loadTexts:
    cmUsCalOffsetResolution.setUnits("hundredth megahertz (10 kHz)")


class _CmUsCalBoardType_Type(Integer32):
    """Custom type cmUsCalBoardType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("genericUnknownDontCare", 0),
          ("bcm93350AV2US", 1),
          ("bcm93350AV3US", 2),
          ("bcm93350CV0US", 3),
          ("bcm93350iV1aUS", 4),
          ("bcm93350iV1bUS", 5),
          ("bcm93350VV1US", 6),
          ("bcm93352VV0US", 7),
          ("bcm93350AV2Euro", 8),
          ("bcm93350AV3Euro", 9),
          ("bcm93350CV0Euro", 10),
          ("bcm93350iV1aEuro", 11),
          ("bcm93350iV1bEuro", 12),
          ("bcm93350VV1Euro", 13),
          ("bcm93352VV0Euro", 14),
          ("bcm93350CV2US", 15),
          ("bcm93350CV2Euro", 16),
          ("bcm93345I", 17),
          ("bcm93345A", 18))
    )


_CmUsCalBoardType_Type.__name__ = "Integer32"
_CmUsCalBoardType_Object = MibScalar
cmUsCalBoardType = _CmUsCalBoardType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3, 9),
    _CmUsCalBoardType_Type()
)
cmUsCalBoardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalBoardType.setStatus("current")


class _CmUsCalAmpType_Type(Integer32):
    """Custom type cmUsCalAmpType based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("lucentATTV4910", 1),
          ("lucentATTV4911", 2),
          ("celISG2000", 3),
          ("anadigicsARA5050", 4),
          ("adi8321", 5),
          ("maxim3510", 6),
          ("celISG3300", 7),
          ("adi8322", 8),
          ("broadcomInternal", 9))
    )


_CmUsCalAmpType_Type.__name__ = "Integer32"
_CmUsCalAmpType_Object = MibScalar
cmUsCalAmpType = _CmUsCalAmpType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3, 10),
    _CmUsCalAmpType_Type()
)
cmUsCalAmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalAmpType.setStatus("current")


class _CmUsCalAmpGain_Type(Unsigned32):
    """Custom type cmUsCalAmpGain based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmUsCalAmpGain_Type.__name__ = "Unsigned32"
_CmUsCalAmpGain_Object = MibScalar
cmUsCalAmpGain = _CmUsCalAmpGain_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3, 11),
    _CmUsCalAmpGain_Type()
)
cmUsCalAmpGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalAmpGain.setStatus("current")


class _CmUsCalDacAtten_Type(Unsigned32):
    """Custom type cmUsCalDacAtten based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmUsCalDacAtten_Type.__name__ = "Unsigned32"
_CmUsCalDacAtten_Object = MibScalar
cmUsCalDacAtten = _CmUsCalDacAtten_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3, 12),
    _CmUsCalDacAtten_Type()
)
cmUsCalDacAtten.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalDacAtten.setStatus("current")


class _CmUsCalTransmitNow_Type(Integer32):
    """Custom type cmUsCalTransmitNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cw", 1),
          ("bits23", 2))
    )


_CmUsCalTransmitNow_Type.__name__ = "Integer32"
_CmUsCalTransmitNow_Object = MibScalar
cmUsCalTransmitNow = _CmUsCalTransmitNow_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3, 13),
    _CmUsCalTransmitNow_Type()
)
cmUsCalTransmitNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalTransmitNow.setStatus("current")
_CmUsCalControlTablePopulate_Type = TruthValue
_CmUsCalControlTablePopulate_Object = MibScalar
cmUsCalControlTablePopulate = _CmUsCalControlTablePopulate_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3, 14),
    _CmUsCalControlTablePopulate_Type()
)
cmUsCalControlTablePopulate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalControlTablePopulate.setStatus("current")


class _CmUsCalDiplexerType_Type(Integer32):
    """Custom type cmUsCalDiplexerType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowSplit", 1),
          ("midSplit", 2))
    )


_CmUsCalDiplexerType_Type.__name__ = "Integer32"
_CmUsCalDiplexerType_Object = MibScalar
cmUsCalDiplexerType = _CmUsCalDiplexerType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 3, 15),
    _CmUsCalDiplexerType_Type()
)
cmUsCalDiplexerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmUsCalDiplexerType.setStatus("current")
_CmEngrHardware_ObjectIdentity = ObjectIdentity
cmEngrHardware = _CmEngrHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 4)
)


class _CmHwDSAGI_Type(Unsigned32):
    """Custom type cmHwDSAGI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmHwDSAGI_Type.__name__ = "Unsigned32"
_CmHwDSAGI_Object = MibScalar
cmHwDSAGI = _CmHwDSAGI_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 4, 1),
    _CmHwDSAGI_Type()
)
cmHwDSAGI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmHwDSAGI.setStatus("current")


class _CmHwDSAGT_Type(Unsigned32):
    """Custom type cmHwDSAGT based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmHwDSAGT_Type.__name__ = "Unsigned32"
_CmHwDSAGT_Object = MibScalar
cmHwDSAGT = _CmHwDSAGT_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 4, 2),
    _CmHwDSAGT_Type()
)
cmHwDSAGT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmHwDSAGT.setStatus("current")


class _CmHwSTPGA1_Type(Unsigned32):
    """Custom type cmHwSTPGA1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_CmHwSTPGA1_Type.__name__ = "Unsigned32"
_CmHwSTPGA1_Object = MibScalar
cmHwSTPGA1 = _CmHwSTPGA1_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 4, 3),
    _CmHwSTPGA1_Type()
)
cmHwSTPGA1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmHwSTPGA1.setStatus("current")


class _CmHwSTABW_Type(Unsigned32):
    """Custom type cmHwSTABW based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmHwSTABW_Type.__name__ = "Unsigned32"
_CmHwSTABW_Object = MibScalar
cmHwSTABW = _CmHwSTABW_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 4, 4),
    _CmHwSTABW_Type()
)
cmHwSTABW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmHwSTABW.setStatus("current")


class _CmHwSTABW2_Type(Unsigned32):
    """Custom type cmHwSTABW2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmHwSTABW2_Type.__name__ = "Unsigned32"
_CmHwSTABW2_Object = MibScalar
cmHwSTABW2 = _CmHwSTABW2_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 4, 5),
    _CmHwSTABW2_Type()
)
cmHwSTABW2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmHwSTABW2.setStatus("current")
_CmEngrBpi_ObjectIdentity = ObjectIdentity
cmEngrBpi = _CmEngrBpi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 5)
)


class _CmBpiTekEven_Type(OctetString):
    """Custom type cmBpiTekEven based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )


_CmBpiTekEven_Type.__name__ = "OctetString"
_CmBpiTekEven_Object = MibScalar
cmBpiTekEven = _CmBpiTekEven_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 5, 1),
    _CmBpiTekEven_Type()
)
cmBpiTekEven.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBpiTekEven.setStatus("current")


class _CmBpiTekOdd_Type(OctetString):
    """Custom type cmBpiTekOdd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )


_CmBpiTekOdd_Type.__name__ = "OctetString"
_CmBpiTekOdd_Object = MibScalar
cmBpiTekOdd = _CmBpiTekOdd_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 5, 2),
    _CmBpiTekOdd_Type()
)
cmBpiTekOdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBpiTekOdd.setStatus("current")


class _CmBpiCbcIvEven_Type(OctetString):
    """Custom type cmBpiCbcIvEven based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )


_CmBpiCbcIvEven_Type.__name__ = "OctetString"
_CmBpiCbcIvEven_Object = MibScalar
cmBpiCbcIvEven = _CmBpiCbcIvEven_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 5, 3),
    _CmBpiCbcIvEven_Type()
)
cmBpiCbcIvEven.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBpiCbcIvEven.setStatus("current")


class _CmBpiCbcIvOdd_Type(OctetString):
    """Custom type cmBpiCbcIvOdd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )


_CmBpiCbcIvOdd_Type.__name__ = "OctetString"
_CmBpiCbcIvOdd_Object = MibScalar
cmBpiCbcIvOdd = _CmBpiCbcIvOdd_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 2, 5, 4),
    _CmBpiCbcIvOdd_Type()
)
cmBpiCbcIvOdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmBpiCbcIvOdd.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-CM-ENGINEERING-MIB",
    **{"cablemodemEngineering": cablemodemEngineering,
       "cmEngrBase": cmEngrBase,
       "cmEngr33xxOpcode": cmEngr33xxOpcode,
       "cmEngr33xxData": cmEngr33xxData,
       "cmEngr33xxCommand": cmEngr33xxCommand,
       "cmEngrDownstreamCalibration": cmEngrDownstreamCalibration,
       "cmDsCalZeroTunerCoefs": cmDsCalZeroTunerCoefs,
       "cmDsCalNumTunerCoefs": cmDsCalNumTunerCoefs,
       "cmDsCalTunerCoefTable": cmDsCalTunerCoefTable,
       "cmDsCalTunerCoefEntry": cmDsCalTunerCoefEntry,
       "cmDsCalTunerCoefIndex": cmDsCalTunerCoefIndex,
       "cmDsCalTunerCoefFrequency": cmDsCalTunerCoefFrequency,
       "cmDsCalTunerCoefValue": cmDsCalTunerCoefValue,
       "cmDsCalTunerCoefCopyFrom": cmDsCalTunerCoefCopyFrom,
       "cmDsCalZeroIFCoefs": cmDsCalZeroIFCoefs,
       "cmDsCalNumIFCoefs": cmDsCalNumIFCoefs,
       "cmDsCalIFCoefTable": cmDsCalIFCoefTable,
       "cmDsCalIFCoefEntry": cmDsCalIFCoefEntry,
       "cmDsCalIFCoefIndex": cmDsCalIFCoefIndex,
       "cmDsCalIFCoefFrequency": cmDsCalIFCoefFrequency,
       "cmDsCalIFCoefValue": cmDsCalIFCoefValue,
       "cmDsCalIFCoefCopyFrom": cmDsCalIFCoefCopyFrom,
       "cmDsCalZeroFineCoefs": cmDsCalZeroFineCoefs,
       "cmDsCalNumFineCoefs": cmDsCalNumFineCoefs,
       "cmDsCalFineCoefTable": cmDsCalFineCoefTable,
       "cmDsCalFineCoefEntry": cmDsCalFineCoefEntry,
       "cmDsCalFineCoefIndex": cmDsCalFineCoefIndex,
       "cmDsCalFineCoefFrequency": cmDsCalFineCoefFrequency,
       "cmDsCalFineCoefValue": cmDsCalFineCoefValue,
       "cmDsCalFineCoefCopyFrom": cmDsCalFineCoefCopyFrom,
       "cmDsCalZeroEqCoefs": cmDsCalZeroEqCoefs,
       "cmDsCalNumEqCoefs": cmDsCalNumEqCoefs,
       "cmDsCalEqCoefTable": cmDsCalEqCoefTable,
       "cmDsCalEqCoefEntry": cmDsCalEqCoefEntry,
       "cmDsCalEqCoefIndex": cmDsCalEqCoefIndex,
       "cmDsCalEqCoefFrequency": cmDsCalEqCoefFrequency,
       "cmDsCalEqCoefValue": cmDsCalEqCoefValue,
       "cmDsCalEqCoefCopyFrom": cmDsCalEqCoefCopyFrom,
       "cmDsCalNumLDAIxReads": cmDsCalNumLDAIxReads,
       "cmDsCalLDAIxReadInterval": cmDsCalLDAIxReadInterval,
       "cmDsCalTunerStep": cmDsCalTunerStep,
       "cmDsCalMasterPowerOffset": cmDsCalMasterPowerOffset,
       "cmDsCalCharacterizeNow": cmDsCalCharacterizeNow,
       "cmDsCalNormalLDAIT": cmDsCalNormalLDAIT,
       "cmDsCalNormalLDAIF": cmDsCalNormalLDAIF,
       "cmDsCalNormalLDAII": cmDsCalNormalLDAII,
       "cmDsCalFrozenLDAIT": cmDsCalFrozenLDAIT,
       "cmDsCalFrozenLDAIF": cmDsCalFrozenLDAIF,
       "cmDsCalFrozenLDAII": cmDsCalFrozenLDAII,
       "cmDsCalFGainTap": cmDsCalFGainTap,
       "cmDsCalTGainTap": cmDsCalTGainTap,
       "cmDsCalIGainTap": cmDsCalIGainTap,
       "cmDsCalFrequencyError": cmDsCalFrequencyError,
       "cmDsCalTunerCoefTablePopulate": cmDsCalTunerCoefTablePopulate,
       "cmDsCalIFCoefTablePopulate": cmDsCalIFCoefTablePopulate,
       "cmDsCalFineCoefTablePopulate": cmDsCalFineCoefTablePopulate,
       "cmDsCalEqCoefTablePopulate": cmDsCalEqCoefTablePopulate,
       "cmDsCalTunerTable": cmDsCalTunerTable,
       "cmDsCalTunerEntry": cmDsCalTunerEntry,
       "cmDsCalTunerIndex": cmDsCalTunerIndex,
       "cmDsCalTunerType": cmDsCalTunerType,
       "cmDsCalTunerNumChannels": cmDsCalTunerNumChannels,
       "cmDsCalTunerFrequency": cmDsCalTunerFrequency,
       "cmDsCalTunerTuneNow": cmDsCalTunerTuneNow,
       "cmDsCalPhyTable": cmDsCalPhyTable,
       "cmDsCalPhyEntry": cmDsCalPhyEntry,
       "cmDsCalPhyIndex": cmDsCalPhyIndex,
       "cmDsCalPhyTuner": cmDsCalPhyTuner,
       "cmDsCalPhyTunerChannel": cmDsCalPhyTunerChannel,
       "cmDsCalPhyModulation": cmDsCalPhyModulation,
       "cmDsCalPhyLockNow": cmDsCalPhyLockNow,
       "cmDsCalPhyQamLocked": cmDsCalPhyQamLocked,
       "cmDsCalPhyFecLocked": cmDsCalPhyFecLocked,
       "cmDsCalPhySignalNoise": cmDsCalPhySignalNoise,
       "cmDsCalPhyPower": cmDsCalPhyPower,
       "cmDsCalPhyFrequency": cmDsCalPhyFrequency,
       "cmDsCalPhyFrequencyError": cmDsCalPhyFrequencyError,
       "cmDsCalPhySymbolRate": cmDsCalPhySymbolRate,
       "cmEngrUpstreamCalibration": cmEngrUpstreamCalibration,
       "cmUsCalControlStartPower": cmUsCalControlStartPower,
       "cmUsCalControlEndPower": cmUsCalControlEndPower,
       "cmUsCalControlResolution": cmUsCalControlResolution,
       "cmUsCalZeroControl": cmUsCalZeroControl,
       "cmUsCalControlTable": cmUsCalControlTable,
       "cmUsCalControlEntry": cmUsCalControlEntry,
       "cmUsCalControlIndex": cmUsCalControlIndex,
       "cmUsCalControlPower": cmUsCalControlPower,
       "cmUsCalControlAmpGain": cmUsCalControlAmpGain,
       "cmUsCalControlDacAtten": cmUsCalControlDacAtten,
       "cmUsCalOffsetStartFreq": cmUsCalOffsetStartFreq,
       "cmUsCalOffsetEndFreq": cmUsCalOffsetEndFreq,
       "cmUsCalOffsetResolution": cmUsCalOffsetResolution,
       "cmUsCalBoardType": cmUsCalBoardType,
       "cmUsCalAmpType": cmUsCalAmpType,
       "cmUsCalAmpGain": cmUsCalAmpGain,
       "cmUsCalDacAtten": cmUsCalDacAtten,
       "cmUsCalTransmitNow": cmUsCalTransmitNow,
       "cmUsCalControlTablePopulate": cmUsCalControlTablePopulate,
       "cmUsCalDiplexerType": cmUsCalDiplexerType,
       "cmEngrHardware": cmEngrHardware,
       "cmHwDSAGI": cmHwDSAGI,
       "cmHwDSAGT": cmHwDSAGT,
       "cmHwSTPGA1": cmHwSTPGA1,
       "cmHwSTABW": cmHwSTABW,
       "cmHwSTABW2": cmHwSTABW2,
       "cmEngrBpi": cmEngrBpi,
       "cmBpiTekEven": cmBpiTekEven,
       "cmBpiTekOdd": cmBpiTekOdd,
       "cmBpiCbcIvEven": cmBpiCbcIvEven,
       "cmBpiCbcIvOdd": cmBpiCbcIvOdd}
)
