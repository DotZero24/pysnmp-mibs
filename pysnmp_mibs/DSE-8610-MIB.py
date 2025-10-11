# SNMP MIB module (DSE-8610-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dse/DSE-8610-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:09:42 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dseVendor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41385)
)
if mibBuilder.loadTexts:
    dseVendor.setRevisions(
        ("2017-08-15 00:00",
         "2017-08-09 00:00",
         "2017-06-06 00:00",
         "2017-06-06 00:00",
         "2017-03-15 00:00",
         "2017-03-13 00:00",
         "2017-02-17 00:00",
         "2017-02-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ChargeVoltsDiv10(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )



class FreqDiv10(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 70),
    )



class VoltsLNDiv10(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )



class VoltsLLDiv10(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )



class CurrentDiv10(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )



class RPMDiv1000(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-3"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4211),
    )



class AirFilterDiv10(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 125),
    )



class ElectricalPotentialDiv10(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-1"


class AverageFuelDiv100(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



class PowerFactorDiv100(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )



class PowerPCDiv10(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, 999),
    )



class VAPCDiv10(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )



class PowerPCDiv100(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )



class CrankPressureDiv100(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-25000, 25000),
    )



class InjectorRailPressureDiv100(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2509),
    )



class OilPressureDiv100(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



# MIB Managed Objects in the order of their OIDs

_DseProduct_ObjectIdentity = ObjectIdentity
dseProduct = _DseProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41385, 1)
)
_UcdTraps_ObjectIdentity = ObjectIdentity
ucdTraps = _UcdTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0)
)
_Dse8610_ObjectIdentity = ObjectIdentity
dse8610 = _Dse8610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5)
)
_DseInstrumentsSection_ObjectIdentity = ObjectIdentity
dseInstrumentsSection = _DseInstrumentsSection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1)
)
_GeneratorTable_Object = MibTable
generatorTable = _GeneratorTable_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    generatorTable.setStatus("current")
_GeneratorEntry_Object = MibTableRow
generatorEntry = _GeneratorEntry_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1)
)
generatorEntry.setIndexNames(
    (0, "DSE-8610-MIB", "genKeyID"),
)
if mibBuilder.loadTexts:
    generatorEntry.setStatus("current")


class _GenKeyID_Type(Integer32):
    """Custom type genKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GenKeyID_Type.__name__ = "Integer32"
_GenKeyID_Object = MibTableColumn
genKeyID = _GenKeyID_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 1),
    _GenKeyID_Type()
)
genKeyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    genKeyID.setStatus("current")
_GenFreq_Type = FreqDiv10
_GenFreq_Object = MibTableColumn
genFreq = _GenFreq_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 2),
    _GenFreq_Type()
)
genFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genFreq.setStatus("current")
_GenL1Volts_Type = VoltsLNDiv10
_GenL1Volts_Object = MibTableColumn
genL1Volts = _GenL1Volts_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 3),
    _GenL1Volts_Type()
)
genL1Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genL1Volts.setStatus("current")
_GenL2Volts_Type = VoltsLNDiv10
_GenL2Volts_Object = MibTableColumn
genL2Volts = _GenL2Volts_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 4),
    _GenL2Volts_Type()
)
genL2Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genL2Volts.setStatus("current")
_GenL3Volts_Type = VoltsLNDiv10
_GenL3Volts_Object = MibTableColumn
genL3Volts = _GenL3Volts_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 5),
    _GenL3Volts_Type()
)
genL3Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genL3Volts.setStatus("current")
_GenL1L2Volts_Type = VoltsLLDiv10
_GenL1L2Volts_Object = MibTableColumn
genL1L2Volts = _GenL1L2Volts_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 6),
    _GenL1L2Volts_Type()
)
genL1L2Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genL1L2Volts.setStatus("current")
_GenL2L3Volts_Type = VoltsLLDiv10
_GenL2L3Volts_Object = MibTableColumn
genL2L3Volts = _GenL2L3Volts_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 7),
    _GenL2L3Volts_Type()
)
genL2L3Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genL2L3Volts.setStatus("current")
_GenL3L1Volts_Type = VoltsLLDiv10
_GenL3L1Volts_Object = MibTableColumn
genL3L1Volts = _GenL3L1Volts_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 8),
    _GenL3L1Volts_Type()
)
genL3L1Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genL3L1Volts.setStatus("current")
_GenL1Current_Type = CurrentDiv10
_GenL1Current_Object = MibTableColumn
genL1Current = _GenL1Current_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 9),
    _GenL1Current_Type()
)
genL1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genL1Current.setStatus("current")
_GenL2Current_Type = CurrentDiv10
_GenL2Current_Object = MibTableColumn
genL2Current = _GenL2Current_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 10),
    _GenL2Current_Type()
)
genL2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genL2Current.setStatus("current")
_GenL3Current_Type = CurrentDiv10
_GenL3Current_Object = MibTableColumn
genL3Current = _GenL3Current_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 11),
    _GenL3Current_Type()
)
genL3Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genL3Current.setStatus("current")
_GenECurrent_Type = CurrentDiv10
_GenECurrent_Object = MibTableColumn
genECurrent = _GenECurrent_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 12),
    _GenECurrent_Type()
)
genECurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genECurrent.setStatus("current")


class _GenL1Watts_Type(Integer32):
    """Custom type genL1Watts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99999999, 99999999),
    )


_GenL1Watts_Type.__name__ = "Integer32"
_GenL1Watts_Object = MibTableColumn
genL1Watts = _GenL1Watts_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 13),
    _GenL1Watts_Type()
)
genL1Watts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genL1Watts.setStatus("current")


class _GenL2Watts_Type(Integer32):
    """Custom type genL2Watts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99999999, 99999999),
    )


_GenL2Watts_Type.__name__ = "Integer32"
_GenL2Watts_Object = MibTableColumn
genL2Watts = _GenL2Watts_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 14),
    _GenL2Watts_Type()
)
genL2Watts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genL2Watts.setStatus("current")


class _GenL3Watts_Type(Integer32):
    """Custom type genL3Watts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99999999, 99999999),
    )


_GenL3Watts_Type.__name__ = "Integer32"
_GenL3Watts_Object = MibTableColumn
genL3Watts = _GenL3Watts_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 15),
    _GenL3Watts_Type()
)
genL3Watts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genL3Watts.setStatus("current")


class _GenRotation_Type(Integer32):
    """Custom type genRotation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_GenRotation_Type.__name__ = "Integer32"
_GenRotation_Object = MibTableColumn
genRotation = _GenRotation_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 16),
    _GenRotation_Type()
)
genRotation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genRotation.setStatus("current")


class _GenWattsTotal_Type(Integer32):
    """Custom type genWattsTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99999999, 99999999),
    )


_GenWattsTotal_Type.__name__ = "Integer32"
_GenWattsTotal_Object = MibTableColumn
genWattsTotal = _GenWattsTotal_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 17),
    _GenWattsTotal_Type()
)
genWattsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genWattsTotal.setStatus("current")


class _GenL1VA_Type(Unsigned32):
    """Custom type genL1VA based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999999),
    )


_GenL1VA_Type.__name__ = "Unsigned32"
_GenL1VA_Object = MibTableColumn
genL1VA = _GenL1VA_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 18),
    _GenL1VA_Type()
)
genL1VA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genL1VA.setStatus("current")


class _GenL2VA_Type(Unsigned32):
    """Custom type genL2VA based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999999),
    )


_GenL2VA_Type.__name__ = "Unsigned32"
_GenL2VA_Object = MibTableColumn
genL2VA = _GenL2VA_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 19),
    _GenL2VA_Type()
)
genL2VA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genL2VA.setStatus("current")


class _GenL3VA_Type(Unsigned32):
    """Custom type genL3VA based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999999),
    )


_GenL3VA_Type.__name__ = "Unsigned32"
_GenL3VA_Object = MibTableColumn
genL3VA = _GenL3VA_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 20),
    _GenL3VA_Type()
)
genL3VA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genL3VA.setStatus("current")


class _GenTotalVA_Type(Unsigned32):
    """Custom type genTotalVA based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999999),
    )


_GenTotalVA_Type.__name__ = "Unsigned32"
_GenTotalVA_Object = MibTableColumn
genTotalVA = _GenTotalVA_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 21),
    _GenTotalVA_Type()
)
genTotalVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genTotalVA.setStatus("current")


class _GenL1VAr_Type(Integer32):
    """Custom type genL1VAr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99999999, 99999999),
    )


_GenL1VAr_Type.__name__ = "Integer32"
_GenL1VAr_Object = MibTableColumn
genL1VAr = _GenL1VAr_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 22),
    _GenL1VAr_Type()
)
genL1VAr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genL1VAr.setStatus("current")


class _GenL2VAr_Type(Integer32):
    """Custom type genL2VAr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99999999, 99999999),
    )


_GenL2VAr_Type.__name__ = "Integer32"
_GenL2VAr_Object = MibTableColumn
genL2VAr = _GenL2VAr_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 23),
    _GenL2VAr_Type()
)
genL2VAr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genL2VAr.setStatus("current")


class _GenL3VAr_Type(Integer32):
    """Custom type genL3VAr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99999999, 99999999),
    )


_GenL3VAr_Type.__name__ = "Integer32"
_GenL3VAr_Object = MibTableColumn
genL3VAr = _GenL3VAr_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 24),
    _GenL3VAr_Type()
)
genL3VAr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genL3VAr.setStatus("current")


class _GenTotalVAr_Type(Integer32):
    """Custom type genTotalVAr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99999999, 99999999),
    )


_GenTotalVAr_Type.__name__ = "Integer32"
_GenTotalVAr_Object = MibTableColumn
genTotalVAr = _GenTotalVAr_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 25),
    _GenTotalVAr_Type()
)
genTotalVAr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genTotalVAr.setStatus("current")
_GenPowerFactorL1_Type = PowerFactorDiv100
_GenPowerFactorL1_Object = MibTableColumn
genPowerFactorL1 = _GenPowerFactorL1_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 26),
    _GenPowerFactorL1_Type()
)
genPowerFactorL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPowerFactorL1.setStatus("current")
_GenPowerFactorL2_Type = PowerFactorDiv100
_GenPowerFactorL2_Object = MibTableColumn
genPowerFactorL2 = _GenPowerFactorL2_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 27),
    _GenPowerFactorL2_Type()
)
genPowerFactorL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPowerFactorL2.setStatus("current")
_GenPowerFactorL3_Type = PowerFactorDiv100
_GenPowerFactorL3_Object = MibTableColumn
genPowerFactorL3 = _GenPowerFactorL3_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 28),
    _GenPowerFactorL3_Type()
)
genPowerFactorL3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPowerFactorL3.setStatus("current")
_GenAvgPowerFactor_Type = PowerFactorDiv100
_GenAvgPowerFactor_Object = MibTableColumn
genAvgPowerFactor = _GenAvgPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 29),
    _GenAvgPowerFactor_Type()
)
genAvgPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genAvgPowerFactor.setStatus("current")


class _GenPowerTotalPC_Type(Integer32):
    """Custom type genPowerTotalPC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_GenPowerTotalPC_Type.__name__ = "Integer32"
_GenPowerTotalPC_Object = MibTableColumn
genPowerTotalPC = _GenPowerTotalPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 30),
    _GenPowerTotalPC_Type()
)
genPowerTotalPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPowerTotalPC.setStatus("current")


class _GenVARTotalPC_Type(Integer32):
    """Custom type genVARTotalPC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_GenVARTotalPC_Type.__name__ = "Integer32"
_GenVARTotalPC_Object = MibTableColumn
genVARTotalPC = _GenVARTotalPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 31),
    _GenVARTotalPC_Type()
)
genVARTotalPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVARTotalPC.setStatus("current")


class _GenPhase1_Type(Unsigned32):
    """Custom type genPhase1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_GenPhase1_Type.__name__ = "Unsigned32"
_GenPhase1_Object = MibTableColumn
genPhase1 = _GenPhase1_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 32),
    _GenPhase1_Type()
)
genPhase1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPhase1.setStatus("current")


class _GenPhase2_Type(Unsigned32):
    """Custom type genPhase2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_GenPhase2_Type.__name__ = "Unsigned32"
_GenPhase2_Object = MibTableColumn
genPhase2 = _GenPhase2_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 33),
    _GenPhase2_Type()
)
genPhase2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPhase2.setStatus("current")


class _GenPhase3_Type(Unsigned32):
    """Custom type genPhase3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_GenPhase3_Type.__name__ = "Unsigned32"
_GenPhase3_Object = MibTableColumn
genPhase3 = _GenPhase3_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 34),
    _GenPhase3_Type()
)
genPhase3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPhase3.setStatus("current")


class _GenPhaseTotal_Type(Unsigned32):
    """Custom type genPhaseTotal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_GenPhaseTotal_Type.__name__ = "Unsigned32"
_GenPhaseTotal_Object = MibTableColumn
genPhaseTotal = _GenPhaseTotal_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 35),
    _GenPhaseTotal_Type()
)
genPhaseTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPhaseTotal.setStatus("current")


class _GenPowerL1PC_Type(Integer32):
    """Custom type genPowerL1PC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_GenPowerL1PC_Type.__name__ = "Integer32"
_GenPowerL1PC_Object = MibTableColumn
genPowerL1PC = _GenPowerL1PC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 36),
    _GenPowerL1PC_Type()
)
genPowerL1PC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPowerL1PC.setStatus("current")


class _GenPowerL2PC_Type(Integer32):
    """Custom type genPowerL2PC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_GenPowerL2PC_Type.__name__ = "Integer32"
_GenPowerL2PC_Object = MibTableColumn
genPowerL2PC = _GenPowerL2PC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 37),
    _GenPowerL2PC_Type()
)
genPowerL2PC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPowerL2PC.setStatus("current")


class _GenPowerL3PC_Type(Integer32):
    """Custom type genPowerL3PC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9999, 9999),
    )


_GenPowerL3PC_Type.__name__ = "Integer32"
_GenPowerL3PC_Object = MibTableColumn
genPowerL3PC = _GenPowerL3PC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 38),
    _GenPowerL3PC_Type()
)
genPowerL3PC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPowerL3PC.setStatus("current")
_GenVoltageLNAvg_Type = VoltsLNDiv10
_GenVoltageLNAvg_Object = MibTableColumn
genVoltageLNAvg = _GenVoltageLNAvg_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 39),
    _GenVoltageLNAvg_Type()
)
genVoltageLNAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVoltageLNAvg.setStatus("current")
_GenVoltageLNDiff_Type = VoltsLNDiv10
_GenVoltageLNDiff_Object = MibTableColumn
genVoltageLNDiff = _GenVoltageLNDiff_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 40),
    _GenVoltageLNDiff_Type()
)
genVoltageLNDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVoltageLNDiff.setStatus("current")
_GenVoltageLNMin_Type = VoltsLNDiv10
_GenVoltageLNMin_Object = MibTableColumn
genVoltageLNMin = _GenVoltageLNMin_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 41),
    _GenVoltageLNMin_Type()
)
genVoltageLNMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVoltageLNMin.setStatus("current")
_GenVoltageLNMax_Type = VoltsLNDiv10
_GenVoltageLNMax_Object = MibTableColumn
genVoltageLNMax = _GenVoltageLNMax_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 42),
    _GenVoltageLNMax_Type()
)
genVoltageLNMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVoltageLNMax.setStatus("current")
_GenVoltageLLAvg_Type = VoltsLLDiv10
_GenVoltageLLAvg_Object = MibTableColumn
genVoltageLLAvg = _GenVoltageLLAvg_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 43),
    _GenVoltageLLAvg_Type()
)
genVoltageLLAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVoltageLLAvg.setStatus("current")
_GenVoltageLLDiff_Type = VoltsLLDiv10
_GenVoltageLLDiff_Object = MibTableColumn
genVoltageLLDiff = _GenVoltageLLDiff_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 44),
    _GenVoltageLLDiff_Type()
)
genVoltageLLDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVoltageLLDiff.setStatus("current")
_GenVoltageLLMin_Type = VoltsLLDiv10
_GenVoltageLLMin_Object = MibTableColumn
genVoltageLLMin = _GenVoltageLLMin_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 45),
    _GenVoltageLLMin_Type()
)
genVoltageLLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVoltageLLMin.setStatus("current")
_GenVoltageLLMax_Type = VoltsLLDiv10
_GenVoltageLLMax_Object = MibTableColumn
genVoltageLLMax = _GenVoltageLLMax_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 46),
    _GenVoltageLLMax_Type()
)
genVoltageLLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVoltageLLMax.setStatus("current")
_GenCurrentAve_Type = CurrentDiv10
_GenCurrentAve_Object = MibTableColumn
genCurrentAve = _GenCurrentAve_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 47),
    _GenCurrentAve_Type()
)
genCurrentAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCurrentAve.setStatus("current")
_GenCurrentDif_Type = CurrentDiv10
_GenCurrentDif_Object = MibTableColumn
genCurrentDif = _GenCurrentDif_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 48),
    _GenCurrentDif_Type()
)
genCurrentDif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCurrentDif.setStatus("current")
_GenCurrentMin_Type = CurrentDiv10
_GenCurrentMin_Object = MibTableColumn
genCurrentMin = _GenCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 49),
    _GenCurrentMin_Type()
)
genCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCurrentMin.setStatus("current")
_GenCurrentMax_Type = CurrentDiv10
_GenCurrentMax_Object = MibTableColumn
genCurrentMax = _GenCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 50),
    _GenCurrentMax_Type()
)
genCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genCurrentMax.setStatus("current")
_GenPowerTotalAvgPC_Type = PowerPCDiv100
_GenPowerTotalAvgPC_Object = MibTableColumn
genPowerTotalAvgPC = _GenPowerTotalAvgPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 51),
    _GenPowerTotalAvgPC_Type()
)
genPowerTotalAvgPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPowerTotalAvgPC.setStatus("current")
_GenPowerTotalDiffPC_Type = PowerPCDiv10
_GenPowerTotalDiffPC_Object = MibTableColumn
genPowerTotalDiffPC = _GenPowerTotalDiffPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 52),
    _GenPowerTotalDiffPC_Type()
)
genPowerTotalDiffPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPowerTotalDiffPC.setStatus("current")
_GenPowerTotalMinPC_Type = PowerPCDiv10
_GenPowerTotalMinPC_Object = MibTableColumn
genPowerTotalMinPC = _GenPowerTotalMinPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 53),
    _GenPowerTotalMinPC_Type()
)
genPowerTotalMinPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPowerTotalMinPC.setStatus("current")
_GenPowerTotalMaxPC_Type = PowerPCDiv10
_GenPowerTotalMaxPC_Object = MibTableColumn
genPowerTotalMaxPC = _GenPowerTotalMaxPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 54),
    _GenPowerTotalMaxPC_Type()
)
genPowerTotalMaxPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPowerTotalMaxPC.setStatus("current")
_GenVATotalAvgPC_Type = VAPCDiv10
_GenVATotalAvgPC_Object = MibTableColumn
genVATotalAvgPC = _GenVATotalAvgPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 55),
    _GenVATotalAvgPC_Type()
)
genVATotalAvgPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVATotalAvgPC.setStatus("current")
_GenVADiffPC_Type = VAPCDiv10
_GenVADiffPC_Object = MibTableColumn
genVADiffPC = _GenVADiffPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 56),
    _GenVADiffPC_Type()
)
genVADiffPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVADiffPC.setStatus("current")
_GenVAMinPC_Type = VAPCDiv10
_GenVAMinPC_Object = MibTableColumn
genVAMinPC = _GenVAMinPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 57),
    _GenVAMinPC_Type()
)
genVAMinPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVAMinPC.setStatus("current")
_GenVAMaxPC_Type = VAPCDiv10
_GenVAMaxPC_Object = MibTableColumn
genVAMaxPC = _GenVAMaxPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 58),
    _GenVAMaxPC_Type()
)
genVAMaxPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVAMaxPC.setStatus("current")
_GenVARTotalAvgPC_Type = PowerPCDiv10
_GenVARTotalAvgPC_Object = MibTableColumn
genVARTotalAvgPC = _GenVARTotalAvgPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 59),
    _GenVARTotalAvgPC_Type()
)
genVARTotalAvgPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVARTotalAvgPC.setStatus("current")
_GenVARDiffPC_Type = PowerPCDiv10
_GenVARDiffPC_Object = MibTableColumn
genVARDiffPC = _GenVARDiffPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 60),
    _GenVARDiffPC_Type()
)
genVARDiffPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVARDiffPC.setStatus("current")
_GenVARMinPC_Type = PowerPCDiv10
_GenVARMinPC_Object = MibTableColumn
genVARMinPC = _GenVARMinPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 61),
    _GenVARMinPC_Type()
)
genVARMinPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVARMinPC.setStatus("current")
_GenVARMaxPC_Type = PowerPCDiv10
_GenVARMaxPC_Object = MibTableColumn
genVARMaxPC = _GenVARMaxPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 62),
    _GenVARMaxPC_Type()
)
genVARMaxPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genVARMaxPC.setStatus("current")
_GenPFTotalAvgPC_Type = PowerFactorDiv100
_GenPFTotalAvgPC_Object = MibTableColumn
genPFTotalAvgPC = _GenPFTotalAvgPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 63),
    _GenPFTotalAvgPC_Type()
)
genPFTotalAvgPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPFTotalAvgPC.setStatus("current")
_GenPFDiffPC_Type = PowerFactorDiv100
_GenPFDiffPC_Object = MibTableColumn
genPFDiffPC = _GenPFDiffPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 64),
    _GenPFDiffPC_Type()
)
genPFDiffPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPFDiffPC.setStatus("current")
_GenPFMinPC_Type = PowerFactorDiv100
_GenPFMinPC_Object = MibTableColumn
genPFMinPC = _GenPFMinPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 65),
    _GenPFMinPC_Type()
)
genPFMinPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPFMinPC.setStatus("current")
_GenPFMaxPC_Type = PowerFactorDiv100
_GenPFMaxPC_Object = MibTableColumn
genPFMaxPC = _GenPFMaxPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 2, 1, 66),
    _GenPFMaxPC_Type()
)
genPFMaxPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genPFMaxPC.setStatus("current")
_EngineTable_Object = MibTable
engineTable = _EngineTable_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    engineTable.setStatus("current")
_EngineEntry_Object = MibTableRow
engineEntry = _EngineEntry_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1)
)
engineEntry.setIndexNames(
    (0, "DSE-8610-MIB", "engKeyID"),
)
if mibBuilder.loadTexts:
    engineEntry.setStatus("current")


class _EngKeyID_Type(Integer32):
    """Custom type engKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EngKeyID_Type.__name__ = "Integer32"
_EngKeyID_Object = MibTableColumn
engKeyID = _EngKeyID_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 1),
    _EngKeyID_Type()
)
engKeyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    engKeyID.setStatus("current")
_EngOilPress_Type = OilPressureDiv100
_EngOilPress_Object = MibTableColumn
engOilPress = _EngOilPress_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 2),
    _EngOilPress_Type()
)
engOilPress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engOilPress.setStatus("current")
_EngTemp_Type = Integer32
_EngTemp_Object = MibTableColumn
engTemp = _EngTemp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 3),
    _EngTemp_Type()
)
engTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engTemp.setStatus("current")
_EngOilTemp_Type = Integer32
_EngOilTemp_Object = MibTableColumn
engOilTemp = _EngOilTemp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 4),
    _EngOilTemp_Type()
)
engOilTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engOilTemp.setStatus("current")


class _EngFuelLevel_Type(Unsigned32):
    """Custom type engFuelLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 130),
    )


_EngFuelLevel_Type.__name__ = "Unsigned32"
_EngFuelLevel_Object = MibTableColumn
engFuelLevel = _EngFuelLevel_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 5),
    _EngFuelLevel_Type()
)
engFuelLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engFuelLevel.setStatus("current")
_EngChargeAltVolts_Type = ChargeVoltsDiv10
_EngChargeAltVolts_Object = MibTableColumn
engChargeAltVolts = _EngChargeAltVolts_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 6),
    _EngChargeAltVolts_Type()
)
engChargeAltVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engChargeAltVolts.setStatus("current")
_EngBatteryVolts_Type = ChargeVoltsDiv10
_EngBatteryVolts_Object = MibTableColumn
engBatteryVolts = _EngBatteryVolts_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 7),
    _EngBatteryVolts_Type()
)
engBatteryVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engBatteryVolts.setStatus("current")


class _EngSpeedDisplay_Type(Unsigned32):
    """Custom type engSpeedDisplay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_EngSpeedDisplay_Type.__name__ = "Unsigned32"
_EngSpeedDisplay_Object = MibTableColumn
engSpeedDisplay = _EngSpeedDisplay_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 8),
    _EngSpeedDisplay_Type()
)
engSpeedDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engSpeedDisplay.setStatus("current")


class _EngCoolantP1_Type(Unsigned32):
    """Custom type engCoolantP1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EngCoolantP1_Type.__name__ = "Unsigned32"
_EngCoolantP1_Object = MibTableColumn
engCoolantP1 = _EngCoolantP1_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 9),
    _EngCoolantP1_Type()
)
engCoolantP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engCoolantP1.setStatus("current")


class _EngCoolantP2_Type(Unsigned32):
    """Custom type engCoolantP2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EngCoolantP2_Type.__name__ = "Unsigned32"
_EngCoolantP2_Object = MibTableColumn
engCoolantP2 = _EngCoolantP2_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 10),
    _EngCoolantP2_Type()
)
engCoolantP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engCoolantP2.setStatus("current")


class _EngFuelP1_Type(Unsigned32):
    """Custom type engFuelP1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EngFuelP1_Type.__name__ = "Unsigned32"
_EngFuelP1_Object = MibTableColumn
engFuelP1 = _EngFuelP1_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 11),
    _EngFuelP1_Type()
)
engFuelP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engFuelP1.setStatus("current")


class _EngFuelP2_Type(Unsigned32):
    """Custom type engFuelP2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EngFuelP2_Type.__name__ = "Unsigned32"
_EngFuelP2_Object = MibTableColumn
engFuelP2 = _EngFuelP2_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 12),
    _EngFuelP2_Type()
)
engFuelP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engFuelP2.setStatus("current")


class _EngTurboP1_Type(Unsigned32):
    """Custom type engTurboP1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EngTurboP1_Type.__name__ = "Unsigned32"
_EngTurboP1_Object = MibTableColumn
engTurboP1 = _EngTurboP1_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 13),
    _EngTurboP1_Type()
)
engTurboP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engTurboP1.setStatus("current")


class _EngTurboP2_Type(Unsigned32):
    """Custom type engTurboP2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EngTurboP2_Type.__name__ = "Unsigned32"
_EngTurboP2_Object = MibTableColumn
engTurboP2 = _EngTurboP2_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 14),
    _EngTurboP2_Type()
)
engTurboP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engTurboP2.setStatus("current")


class _EngInMainfoldT1_Type(Unsigned32):
    """Custom type engInMainfoldT1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_EngInMainfoldT1_Type.__name__ = "Unsigned32"
_EngInMainfoldT1_Object = MibTableColumn
engInMainfoldT1 = _EngInMainfoldT1_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 15),
    _EngInMainfoldT1_Type()
)
engInMainfoldT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engInMainfoldT1.setStatus("current")


class _EngInMainfoldT2_Type(Integer32):
    """Custom type engInMainfoldT2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 10000),
    )


_EngInMainfoldT2_Type.__name__ = "Integer32"
_EngInMainfoldT2_Object = MibTableColumn
engInMainfoldT2 = _EngInMainfoldT2_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 16),
    _EngInMainfoldT2_Type()
)
engInMainfoldT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engInMainfoldT2.setStatus("current")


class _EngExhaustT1_Type(Integer32):
    """Custom type engExhaustT1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 10000),
    )


_EngExhaustT1_Type.__name__ = "Integer32"
_EngExhaustT1_Object = MibTableColumn
engExhaustT1 = _EngExhaustT1_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 17),
    _EngExhaustT1_Type()
)
engExhaustT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhaustT1.setStatus("current")


class _EngExhaustT2_Type(Integer32):
    """Custom type engExhaustT2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 10000),
    )


_EngExhaustT2_Type.__name__ = "Integer32"
_EngExhaustT2_Object = MibTableColumn
engExhaustT2 = _EngExhaustT2_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 18),
    _EngExhaustT2_Type()
)
engExhaustT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhaustT2.setStatus("current")
_EngFuelConsumption_Type = AverageFuelDiv100
_EngFuelConsumption_Object = MibTableColumn
engFuelConsumption = _EngFuelConsumption_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 19),
    _EngFuelConsumption_Type()
)
engFuelConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engFuelConsumption.setStatus("current")
_EngWaterInFuel_Type = Unsigned32
_EngWaterInFuel_Object = MibTableColumn
engWaterInFuel = _EngWaterInFuel_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 20),
    _EngWaterInFuel_Type()
)
engWaterInFuel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engWaterInFuel.setStatus("current")
_EngCANBitData_Type = Unsigned32
_EngCANBitData_Object = MibTableColumn
engCANBitData = _EngCANBitData_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 21),
    _EngCANBitData_Type()
)
engCANBitData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engCANBitData.setStatus("current")
_EngAtmosphericP_Type = Unsigned32
_EngAtmosphericP_Object = MibTableColumn
engAtmosphericP = _EngAtmosphericP_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 22),
    _EngAtmosphericP_Type()
)
engAtmosphericP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engAtmosphericP.setStatus("current")
_EngFuelT_Type = Integer32
_EngFuelT_Object = MibTableColumn
engFuelT = _EngFuelT_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 23),
    _EngFuelT_Type()
)
engFuelT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engFuelT.setStatus("current")


class _EngFuelLevelUnits_Type(Unsigned32):
    """Custom type engFuelLevelUnits based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999999),
    )


_EngFuelLevelUnits_Type.__name__ = "Unsigned32"
_EngFuelLevelUnits_Object = MibTableColumn
engFuelLevelUnits = _EngFuelLevelUnits_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 24),
    _EngFuelLevelUnits_Type()
)
engFuelLevelUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engFuelLevelUnits.setStatus("current")


class _EngTankFuelUnits_Type(Unsigned32):
    """Custom type engTankFuelUnits based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_EngTankFuelUnits_Type.__name__ = "Unsigned32"
_EngTankFuelUnits_Object = MibTableColumn
engTankFuelUnits = _EngTankFuelUnits_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 25),
    _EngTankFuelUnits_Type()
)
engTankFuelUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engTankFuelUnits.setStatus("current")


class _EngAfttrt1FuelUSed_Type(Unsigned32):
    """Custom type engAfttrt1FuelUSed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2105),
    )


_EngAfttrt1FuelUSed_Type.__name__ = "Unsigned32"
_EngAfttrt1FuelUSed_Object = MibTableColumn
engAfttrt1FuelUSed = _EngAfttrt1FuelUSed_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 26),
    _EngAfttrt1FuelUSed_Type()
)
engAfttrt1FuelUSed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engAfttrt1FuelUSed.setStatus("current")


class _EngAfttrt1ExGasT1_Type(Integer32):
    """Custom type engAfttrt1ExGasT1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngAfttrt1ExGasT1_Type.__name__ = "Integer32"
_EngAfttrt1ExGasT1_Object = MibTableColumn
engAfttrt1ExGasT1 = _EngAfttrt1ExGasT1_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 27),
    _EngAfttrt1ExGasT1_Type()
)
engAfttrt1ExGasT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engAfttrt1ExGasT1.setStatus("current")


class _EngAfttrt1ExGasT3_Type(Integer32):
    """Custom type engAfttrt1ExGasT3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngAfttrt1ExGasT3_Type.__name__ = "Integer32"
_EngAfttrt1ExGasT3_Object = MibTableColumn
engAfttrt1ExGasT3 = _EngAfttrt1ExGasT3_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 28),
    _EngAfttrt1ExGasT3_Type()
)
engAfttrt1ExGasT3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engAfttrt1ExGasT3.setStatus("current")


class _EngRefTorque_Type(Unsigned32):
    """Custom type engRefTorque based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6425),
    )


_EngRefTorque_Type.__name__ = "Unsigned32"
_EngRefTorque_Object = MibTableColumn
engRefTorque = _EngRefTorque_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 29),
    _EngRefTorque_Type()
)
engRefTorque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engRefTorque.setStatus("current")
_EngPerTorque_Type = Integer32
_EngPerTorque_Object = MibTableColumn
engPerTorque = _EngPerTorque_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 30),
    _EngPerTorque_Type()
)
engPerTorque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engPerTorque.setStatus("current")
_EngDemandPerTorque_Type = Integer32
_EngDemandPerTorque_Object = MibTableColumn
engDemandPerTorque = _EngDemandPerTorque_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 31),
    _EngDemandPerTorque_Type()
)
engDemandPerTorque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engDemandPerTorque.setStatus("current")


class _EngPCLoadAtSpeed_Type(Unsigned32):
    """Custom type engPCLoadAtSpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_EngPCLoadAtSpeed_Type.__name__ = "Unsigned32"
_EngPCLoadAtSpeed_Object = MibTableColumn
engPCLoadAtSpeed = _EngPCLoadAtSpeed_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 32),
    _EngPCLoadAtSpeed_Type()
)
engPCLoadAtSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engPCLoadAtSpeed.setStatus("current")


class _EngAccelPedalPos_Type(Unsigned32):
    """Custom type engAccelPedalPos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EngAccelPedalPos_Type.__name__ = "Unsigned32"
_EngAccelPedalPos_Object = MibTableColumn
engAccelPedalPos = _EngAccelPedalPos_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 33),
    _EngAccelPedalPos_Type()
)
engAccelPedalPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engAccelPedalPos.setStatus("current")


class _EngNomFricPerTorque_Type(Integer32):
    """Custom type engNomFricPerTorque based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-125, 125),
    )


_EngNomFricPerTorque_Type.__name__ = "Integer32"
_EngNomFricPerTorque_Object = MibTableColumn
engNomFricPerTorque = _EngNomFricPerTorque_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 34),
    _EngNomFricPerTorque_Type()
)
engNomFricPerTorque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engNomFricPerTorque.setStatus("current")
_EngOilLevel_Type = Unsigned32
_EngOilLevel_Object = MibTableColumn
engOilLevel = _EngOilLevel_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 35),
    _EngOilLevel_Type()
)
engOilLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engOilLevel.setStatus("current")
_EngCrankCasePress_Type = CrankPressureDiv100
_EngCrankCasePress_Object = MibTableColumn
engCrankCasePress = _EngCrankCasePress_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 36),
    _EngCrankCasePress_Type()
)
engCrankCasePress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engCrankCasePress.setStatus("current")


class _EngCoolantLevel_Type(Integer32):
    """Custom type engCoolantLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-25000, 25000),
    )


_EngCoolantLevel_Type.__name__ = "Integer32"
_EngCoolantLevel_Object = MibTableColumn
engCoolantLevel = _EngCoolantLevel_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 37),
    _EngCoolantLevel_Type()
)
engCoolantLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engCoolantLevel.setStatus("current")
_EngInjectorRail1_Type = InjectorRailPressureDiv100
_EngInjectorRail1_Object = MibTableColumn
engInjectorRail1 = _EngInjectorRail1_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 38),
    _EngInjectorRail1_Type()
)
engInjectorRail1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engInjectorRail1.setStatus("current")
_EngInjectorRail2_Type = InjectorRailPressureDiv100
_EngInjectorRail2_Object = MibTableColumn
engInjectorRail2 = _EngInjectorRail2_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 39),
    _EngInjectorRail2_Type()
)
engInjectorRail2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engInjectorRail2.setStatus("current")


class _EngEgrFlowRate_Type(Unsigned32):
    """Custom type engEgrFlowRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3212),
    )


_EngEgrFlowRate_Type.__name__ = "Unsigned32"
_EngEgrFlowRate_Object = MibTableColumn
engEgrFlowRate = _EngEgrFlowRate_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 40),
    _EngEgrFlowRate_Type()
)
engEgrFlowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engEgrFlowRate.setStatus("current")


class _EngPreFilOilPress_Type(Unsigned32):
    """Custom type engPreFilOilPress based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_EngPreFilOilPress_Type.__name__ = "Unsigned32"
_EngPreFilOilPress_Object = MibTableColumn
engPreFilOilPress = _EngPreFilOilPress_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 41),
    _EngPreFilOilPress_Type()
)
engPreFilOilPress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engPreFilOilPress.setStatus("current")


class _EngInstBreakPower_Type(Unsigned32):
    """Custom type engInstBreakPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3212),
    )


_EngInstBreakPower_Type.__name__ = "Unsigned32"
_EngInstBreakPower_Object = MibTableColumn
engInstBreakPower = _EngInstBreakPower_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 42),
    _EngInstBreakPower_Type()
)
engInstBreakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engInstBreakPower.setStatus("current")


class _EngExhGasPort1Temp_Type(Integer32):
    """Custom type engExhGasPort1Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngExhGasPort1Temp_Type.__name__ = "Integer32"
_EngExhGasPort1Temp_Object = MibTableColumn
engExhGasPort1Temp = _EngExhGasPort1Temp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 43),
    _EngExhGasPort1Temp_Type()
)
engExhGasPort1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhGasPort1Temp.setStatus("current")


class _EngExhGasPort2Temp_Type(Integer32):
    """Custom type engExhGasPort2Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngExhGasPort2Temp_Type.__name__ = "Integer32"
_EngExhGasPort2Temp_Object = MibTableColumn
engExhGasPort2Temp = _EngExhGasPort2Temp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 44),
    _EngExhGasPort2Temp_Type()
)
engExhGasPort2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhGasPort2Temp.setStatus("current")


class _EngExhGasPort3Temp_Type(Integer32):
    """Custom type engExhGasPort3Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngExhGasPort3Temp_Type.__name__ = "Integer32"
_EngExhGasPort3Temp_Object = MibTableColumn
engExhGasPort3Temp = _EngExhGasPort3Temp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 45),
    _EngExhGasPort3Temp_Type()
)
engExhGasPort3Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhGasPort3Temp.setStatus("current")


class _EngExhGasPort4Temp_Type(Integer32):
    """Custom type engExhGasPort4Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngExhGasPort4Temp_Type.__name__ = "Integer32"
_EngExhGasPort4Temp_Object = MibTableColumn
engExhGasPort4Temp = _EngExhGasPort4Temp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 46),
    _EngExhGasPort4Temp_Type()
)
engExhGasPort4Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhGasPort4Temp.setStatus("current")


class _EngExhGasPort5Temp_Type(Integer32):
    """Custom type engExhGasPort5Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngExhGasPort5Temp_Type.__name__ = "Integer32"
_EngExhGasPort5Temp_Object = MibTableColumn
engExhGasPort5Temp = _EngExhGasPort5Temp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 47),
    _EngExhGasPort5Temp_Type()
)
engExhGasPort5Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhGasPort5Temp.setStatus("current")


class _EngExhGasPort6Temp_Type(Integer32):
    """Custom type engExhGasPort6Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngExhGasPort6Temp_Type.__name__ = "Integer32"
_EngExhGasPort6Temp_Object = MibTableColumn
engExhGasPort6Temp = _EngExhGasPort6Temp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 48),
    _EngExhGasPort6Temp_Type()
)
engExhGasPort6Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhGasPort6Temp.setStatus("current")


class _EngExhGasPort7Temp_Type(Integer32):
    """Custom type engExhGasPort7Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngExhGasPort7Temp_Type.__name__ = "Integer32"
_EngExhGasPort7Temp_Object = MibTableColumn
engExhGasPort7Temp = _EngExhGasPort7Temp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 49),
    _EngExhGasPort7Temp_Type()
)
engExhGasPort7Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhGasPort7Temp.setStatus("current")


class _EngExhGasPort8Temp_Type(Integer32):
    """Custom type engExhGasPort8Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngExhGasPort8Temp_Type.__name__ = "Integer32"
_EngExhGasPort8Temp_Object = MibTableColumn
engExhGasPort8Temp = _EngExhGasPort8Temp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 50),
    _EngExhGasPort8Temp_Type()
)
engExhGasPort8Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhGasPort8Temp.setStatus("current")


class _EngExhGasPort9Temp_Type(Integer32):
    """Custom type engExhGasPort9Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngExhGasPort9Temp_Type.__name__ = "Integer32"
_EngExhGasPort9Temp_Object = MibTableColumn
engExhGasPort9Temp = _EngExhGasPort9Temp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 51),
    _EngExhGasPort9Temp_Type()
)
engExhGasPort9Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhGasPort9Temp.setStatus("current")


class _EngExhGasPort10Temp_Type(Integer32):
    """Custom type engExhGasPort10Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngExhGasPort10Temp_Type.__name__ = "Integer32"
_EngExhGasPort10Temp_Object = MibTableColumn
engExhGasPort10Temp = _EngExhGasPort10Temp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 52),
    _EngExhGasPort10Temp_Type()
)
engExhGasPort10Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhGasPort10Temp.setStatus("current")


class _EngExhGasPort11Temp_Type(Integer32):
    """Custom type engExhGasPort11Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngExhGasPort11Temp_Type.__name__ = "Integer32"
_EngExhGasPort11Temp_Object = MibTableColumn
engExhGasPort11Temp = _EngExhGasPort11Temp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 53),
    _EngExhGasPort11Temp_Type()
)
engExhGasPort11Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhGasPort11Temp.setStatus("current")


class _EngExhGasPort12Temp_Type(Integer32):
    """Custom type engExhGasPort12Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngExhGasPort12Temp_Type.__name__ = "Integer32"
_EngExhGasPort12Temp_Object = MibTableColumn
engExhGasPort12Temp = _EngExhGasPort12Temp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 54),
    _EngExhGasPort12Temp_Type()
)
engExhGasPort12Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhGasPort12Temp.setStatus("current")


class _EngExhGasPort13Temp_Type(Integer32):
    """Custom type engExhGasPort13Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngExhGasPort13Temp_Type.__name__ = "Integer32"
_EngExhGasPort13Temp_Object = MibTableColumn
engExhGasPort13Temp = _EngExhGasPort13Temp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 55),
    _EngExhGasPort13Temp_Type()
)
engExhGasPort13Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhGasPort13Temp.setStatus("current")


class _EngExhGasPort14Temp_Type(Integer32):
    """Custom type engExhGasPort14Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngExhGasPort14Temp_Type.__name__ = "Integer32"
_EngExhGasPort14Temp_Object = MibTableColumn
engExhGasPort14Temp = _EngExhGasPort14Temp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 56),
    _EngExhGasPort14Temp_Type()
)
engExhGasPort14Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhGasPort14Temp.setStatus("current")


class _EngExhGasPort15Temp_Type(Integer32):
    """Custom type engExhGasPort15Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngExhGasPort15Temp_Type.__name__ = "Integer32"
_EngExhGasPort15Temp_Object = MibTableColumn
engExhGasPort15Temp = _EngExhGasPort15Temp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 57),
    _EngExhGasPort15Temp_Type()
)
engExhGasPort15Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhGasPort15Temp.setStatus("current")


class _EngExhGasPort16Temp_Type(Integer32):
    """Custom type engExhGasPort16Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngExhGasPort16Temp_Type.__name__ = "Integer32"
_EngExhGasPort16Temp_Object = MibTableColumn
engExhGasPort16Temp = _EngExhGasPort16Temp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 58),
    _EngExhGasPort16Temp_Type()
)
engExhGasPort16Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhGasPort16Temp.setStatus("current")


class _EngIntercoolerTemp_Type(Integer32):
    """Custom type engIntercoolerTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 210),
    )


_EngIntercoolerTemp_Type.__name__ = "Integer32"
_EngIntercoolerTemp_Object = MibTableColumn
engIntercoolerTemp = _EngIntercoolerTemp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 59),
    _EngIntercoolerTemp_Type()
)
engIntercoolerTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engIntercoolerTemp.setStatus("current")


class _EngTurboOilTemp_Type(Unsigned32):
    """Custom type engTurboOilTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8031),
    )


_EngTurboOilTemp_Type.__name__ = "Unsigned32"
_EngTurboOilTemp_Object = MibTableColumn
engTurboOilTemp = _EngTurboOilTemp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 60),
    _EngTurboOilTemp_Type()
)
engTurboOilTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engTurboOilTemp.setStatus("current")


class _EngECUTemp_Type(Integer32):
    """Custom type engECUTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngECUTemp_Type.__name__ = "Integer32"
_EngECUTemp_Object = MibTableColumn
engECUTemp = _EngECUTemp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 61),
    _EngECUTemp_Type()
)
engECUTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engECUTemp.setStatus("current")


class _EngFanSpeed_Type(Unsigned32):
    """Custom type engFanSpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8031),
    )


_EngFanSpeed_Type.__name__ = "Unsigned32"
_EngFanSpeed_Object = MibTableColumn
engFanSpeed = _EngFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 62),
    _EngFanSpeed_Type()
)
engFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engFanSpeed.setStatus("current")
_EngTotalRev_Type = RPMDiv1000
_EngTotalRev_Object = MibTableColumn
engTotalRev = _EngTotalRev_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 63),
    _EngTotalRev_Type()
)
engTotalRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engTotalRev.setStatus("current")


class _EngAirInPress_Type(Unsigned32):
    """Custom type engAirInPress based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_EngAirInPress_Type.__name__ = "Unsigned32"
_EngAirInPress_Object = MibTableColumn
engAirInPress = _EngAirInPress_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 64),
    _EngAirInPress_Type()
)
engAirInPress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engAirInPress.setStatus("current")
_EngAirFilDiffPres_Type = AirFilterDiv10
_EngAirFilDiffPres_Object = MibTableColumn
engAirFilDiffPres = _EngAirFilDiffPres_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 65),
    _EngAirFilDiffPres_Type()
)
engAirFilDiffPres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engAirFilDiffPres.setStatus("current")


class _EngTrapInPress_Type(Unsigned32):
    """Custom type engTrapInPress based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 125),
    )


_EngTrapInPress_Type.__name__ = "Unsigned32"
_EngTrapInPress_Object = MibTableColumn
engTrapInPress = _EngTrapInPress_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 66),
    _EngTrapInPress_Type()
)
engTrapInPress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engTrapInPress.setStatus("current")


class _EngTurboP3_Type(Unsigned32):
    """Custom type engTurboP3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8031),
    )


_EngTurboP3_Type.__name__ = "Unsigned32"
_EngTurboP3_Object = MibTableColumn
engTurboP3 = _EngTurboP3_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 67),
    _EngTurboP3_Type()
)
engTurboP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engTurboP3.setStatus("current")


class _EngTurboP4_Type(Unsigned32):
    """Custom type engTurboP4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8031),
    )


_EngTurboP4_Type.__name__ = "Unsigned32"
_EngTurboP4_Object = MibTableColumn
engTurboP4 = _EngTurboP4_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 68),
    _EngTurboP4_Type()
)
engTurboP4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engTurboP4.setStatus("current")


class _EngInMainfoldT3_Type(Integer32):
    """Custom type engInMainfoldT3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 210),
    )


_EngInMainfoldT3_Type.__name__ = "Integer32"
_EngInMainfoldT3_Object = MibTableColumn
engInMainfoldT3 = _EngInMainfoldT3_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 69),
    _EngInMainfoldT3_Type()
)
engInMainfoldT3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engInMainfoldT3.setStatus("current")


class _EngInMainfoldT4_Type(Integer32):
    """Custom type engInMainfoldT4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 210),
    )


_EngInMainfoldT4_Type.__name__ = "Integer32"
_EngInMainfoldT4_Object = MibTableColumn
engInMainfoldT4 = _EngInMainfoldT4_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 70),
    _EngInMainfoldT4_Type()
)
engInMainfoldT4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engInMainfoldT4.setStatus("current")


class _EngInMainfoldT5_Type(Integer32):
    """Custom type engInMainfoldT5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 210),
    )


_EngInMainfoldT5_Type.__name__ = "Integer32"
_EngInMainfoldT5_Object = MibTableColumn
engInMainfoldT5 = _EngInMainfoldT5_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 71),
    _EngInMainfoldT5_Type()
)
engInMainfoldT5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engInMainfoldT5.setStatus("current")


class _EngInMainfoldT6_Type(Integer32):
    """Custom type engInMainfoldT6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 210),
    )


_EngInMainfoldT6_Type.__name__ = "Integer32"
_EngInMainfoldT6_Object = MibTableColumn
engInMainfoldT6 = _EngInMainfoldT6_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 72),
    _EngInMainfoldT6_Type()
)
engInMainfoldT6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engInMainfoldT6.setStatus("current")
_EngTripFuel_Type = Unsigned32
_EngTripFuel_Object = MibTableColumn
engTripFuel = _EngTripFuel_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 73),
    _EngTripFuel_Type()
)
engTripFuel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engTripFuel.setStatus("current")
_EngElectPotential_Type = ElectricalPotentialDiv10
_EngElectPotential_Object = MibTableColumn
engElectPotential = _EngElectPotential_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 74),
    _EngElectPotential_Type()
)
engElectPotential.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engElectPotential.setStatus("current")
_EngPGIEngType_Type = Unsigned32
_EngPGIEngType_Object = MibTableColumn
engPGIEngType = _EngPGIEngType_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 75),
    _EngPGIEngType_Type()
)
engPGIEngType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engPGIEngType.setStatus("current")
_EngPGIVerNum_Type = Unsigned32
_EngPGIVerNum_Object = MibTableColumn
engPGIVerNum = _EngPGIVerNum_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 76),
    _EngPGIVerNum_Type()
)
engPGIVerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engPGIVerNum.setStatus("current")


class _EngDPTCFilLampCmd_Type(Integer32):
    """Custom type engDPTCFilLampCmd based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("onSolid", 1),
          ("reservedSAE1", 2),
          ("reservedSAE2", 3),
          ("fastBlink", 4),
          ("reservedSAE3", 5),
          ("reservedSAE4", 6),
          ("notAvailable", 7))
    )


_EngDPTCFilLampCmd_Type.__name__ = "Integer32"
_EngDPTCFilLampCmd_Object = MibTableColumn
engDPTCFilLampCmd = _EngDPTCFilLampCmd_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 77),
    _EngDPTCFilLampCmd_Type()
)
engDPTCFilLampCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engDPTCFilLampCmd.setStatus("current")


class _EngExhSysHighTemp_Type(Integer32):
    """Custom type engExhSysHighTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("engineStopped", 0),
          ("preStart", 1),
          ("availableSAE5", 2),
          ("availableSAE6", 3),
          ("availableSAE7", 4),
          ("availableSAE8", 5),
          ("availableSAE9", 6))
    )


_EngExhSysHighTemp_Type.__name__ = "Integer32"
_EngExhSysHighTemp_Object = MibTableColumn
engExhSysHighTemp = _EngExhSysHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 78),
    _EngExhSysHighTemp_Type()
)
engExhSysHighTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhSysHighTemp.setStatus("current")


class _EngDPTCActRegFor_Type(Integer32):
    """Custom type engDPTCActRegFor based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("activeForcedBySwitch", 1),
          ("activeForcedByServiceTool", 2),
          ("notAvailable1", 3),
          ("notAvailable2", 4),
          ("notAvailable3", 5),
          ("notAvailable4", 6),
          ("notAvailable5", 7))
    )


_EngDPTCActRegFor_Type.__name__ = "Integer32"
_EngDPTCActRegFor_Object = MibTableColumn
engDPTCActRegFor = _EngDPTCActRegFor_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 79),
    _EngDPTCActRegFor_Type()
)
engDPTCActRegFor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engDPTCActRegFor.setStatus("current")


class _EngSDWNWaitStart_Type(Integer32):
    """Custom type engSDWNWaitStart based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("engineStopped2", 0),
          ("preStart2", 1),
          ("warnimgUp2", 2),
          ("running2", 3),
          ("coolingDown2", 4),
          ("engineStoped2", 5),
          ("postRun2", 6),
          ("unknown2", 7),
          ("availableSAE10", 8),
          ("availableSAE11", 9),
          ("availableSAE12", 10),
          ("availableSAE13", 11),
          ("availableSAE14", 12),
          ("availableSAE15", 13),
          ("availableSAE16", 14),
          ("availableSAE17", 15))
    )


_EngSDWNWaitStart_Type.__name__ = "Integer32"
_EngSDWNWaitStart_Object = MibTableColumn
engSDWNWaitStart = _EngSDWNWaitStart_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 80),
    _EngSDWNWaitStart_Type()
)
engSDWNWaitStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engSDWNWaitStart.setStatus("current")
_EngSDWNProtection_Type = Unsigned32
_EngSDWNProtection_Object = MibTableColumn
engSDWNProtection = _EngSDWNProtection_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 81),
    _EngSDWNProtection_Type()
)
engSDWNProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engSDWNProtection.setStatus("current")
_EngSDWNApproaching_Type = Unsigned32
_EngSDWNApproaching_Object = MibTableColumn
engSDWNApproaching = _EngSDWNApproaching_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 82),
    _EngSDWNApproaching_Type()
)
engSDWNApproaching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engSDWNApproaching.setStatus("current")
_EngOperatingState_Type = Unsigned32
_EngOperatingState_Object = MibTableColumn
engOperatingState = _EngOperatingState_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 83),
    _EngOperatingState_Type()
)
engOperatingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engOperatingState.setStatus("current")
_EngSDWNClOverride_Type = Unsigned32
_EngSDWNClOverride_Object = MibTableColumn
engSDWNClOverride = _EngSDWNClOverride_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 84),
    _EngSDWNClOverride_Type()
)
engSDWNClOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engSDWNClOverride.setStatus("current")
_EngBattleshortOvr_Type = Unsigned32
_EngBattleshortOvr_Object = MibTableColumn
engBattleshortOvr = _EngBattleshortOvr_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 85),
    _EngBattleshortOvr_Type()
)
engBattleshortOvr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engBattleshortOvr.setStatus("current")
_EngModHours_Type = Unsigned32
_EngModHours_Object = MibTableColumn
engModHours = _EngModHours_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 86),
    _EngModHours_Type()
)
engModHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engModHours.setStatus("current")
_EngModOilPress_Type = Unsigned32
_EngModOilPress_Object = MibTableColumn
engModOilPress = _EngModOilPress_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 87),
    _EngModOilPress_Type()
)
engModOilPress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engModOilPress.setStatus("current")
_EngModCoolTemp_Type = Unsigned32
_EngModCoolTemp_Object = MibTableColumn
engModCoolTemp = _EngModCoolTemp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 88),
    _EngModCoolTemp_Type()
)
engModCoolTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engModCoolTemp.setStatus("current")
_EngModRPM_Type = Unsigned32
_EngModRPM_Object = MibTableColumn
engModRPM = _EngModRPM_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 89),
    _EngModRPM_Type()
)
engModRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engModRPM.setStatus("current")
_EngModChargeAlt_Type = Unsigned32
_EngModChargeAlt_Object = MibTableColumn
engModChargeAlt = _EngModChargeAlt_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 90),
    _EngModChargeAlt_Type()
)
engModChargeAlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engModChargeAlt.setStatus("current")
_EngModSpeedFeed_Type = Unsigned32
_EngModSpeedFeed_Object = MibTableColumn
engModSpeedFeed = _EngModSpeedFeed_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 91),
    _EngModSpeedFeed_Type()
)
engModSpeedFeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engModSpeedFeed.setStatus("current")
_EngModFreqAdj_Type = Unsigned32
_EngModFreqAdj_Object = MibTableColumn
engModFreqAdj = _EngModFreqAdj_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 92),
    _EngModFreqAdj_Type()
)
engModFreqAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engModFreqAdj.setStatus("current")
_EngAlarmWarn_Type = Unsigned32
_EngAlarmWarn_Object = MibTableColumn
engAlarmWarn = _EngAlarmWarn_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 93),
    _EngAlarmWarn_Type()
)
engAlarmWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engAlarmWarn.setStatus("current")
_EngAlarmShdwn_Type = Unsigned32
_EngAlarmShdwn_Object = MibTableColumn
engAlarmShdwn = _EngAlarmShdwn_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 94),
    _EngAlarmShdwn_Type()
)
engAlarmShdwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engAlarmShdwn.setStatus("current")
_EngAlarmElectr_Type = Unsigned32
_EngAlarmElectr_Object = MibTableColumn
engAlarmElectr = _EngAlarmElectr_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 95),
    _EngAlarmElectr_Type()
)
engAlarmElectr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engAlarmElectr.setStatus("current")
_EngAmberStopLamp_Type = Unsigned32
_EngAmberStopLamp_Object = MibTableColumn
engAmberStopLamp = _EngAmberStopLamp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 96),
    _EngAmberStopLamp_Type()
)
engAmberStopLamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engAmberStopLamp.setStatus("current")
_EngAmberLampFlash_Type = Unsigned32
_EngAmberLampFlash_Object = MibTableColumn
engAmberLampFlash = _EngAmberLampFlash_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 97),
    _EngAmberLampFlash_Type()
)
engAmberLampFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engAmberLampFlash.setStatus("current")
_EngRedStopLamp_Type = Unsigned32
_EngRedStopLamp_Object = MibTableColumn
engRedStopLamp = _EngRedStopLamp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 98),
    _EngRedStopLamp_Type()
)
engRedStopLamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engRedStopLamp.setStatus("current")
_EngRedLampFlash_Type = Unsigned32
_EngRedLampFlash_Object = MibTableColumn
engRedLampFlash = _EngRedLampFlash_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 99),
    _EngRedLampFlash_Type()
)
engRedLampFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engRedLampFlash.setStatus("current")
_EngProtLamp_Type = Unsigned32
_EngProtLamp_Object = MibTableColumn
engProtLamp = _EngProtLamp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 100),
    _EngProtLamp_Type()
)
engProtLamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engProtLamp.setStatus("current")
_EngProtLampFlash_Type = Unsigned32
_EngProtLampFlash_Object = MibTableColumn
engProtLampFlash = _EngProtLampFlash_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 101),
    _EngProtLampFlash_Type()
)
engProtLampFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engProtLampFlash.setStatus("current")
_EngMalfLamp_Type = Unsigned32
_EngMalfLamp_Object = MibTableColumn
engMalfLamp = _EngMalfLamp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 102),
    _EngMalfLamp_Type()
)
engMalfLamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engMalfLamp.setStatus("current")
_EngMalfLampFlash_Type = Unsigned32
_EngMalfLampFlash_Object = MibTableColumn
engMalfLampFlash = _EngMalfLampFlash_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 103),
    _EngMalfLampFlash_Type()
)
engMalfLampFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engMalfLampFlash.setStatus("current")
_EngBattSwitched_Type = Unsigned32
_EngBattSwitched_Object = MibTableColumn
engBattSwitched = _EngBattSwitched_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 104),
    _EngBattSwitched_Type()
)
engBattSwitched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engBattSwitched.setStatus("current")
_EngChargPotential_Type = Unsigned32
_EngChargPotential_Object = MibTableColumn
engChargPotential = _EngChargPotential_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 105),
    _EngChargPotential_Type()
)
engChargPotential.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engChargPotential.setStatus("current")
_EngCharAltCurr_Type = Unsigned32
_EngCharAltCurr_Object = MibTableColumn
engCharAltCurr = _EngCharAltCurr_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 106),
    _EngCharAltCurr_Type()
)
engCharAltCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engCharAltCurr.setStatus("current")
_EngBattCurr_Type = Unsigned32
_EngBattCurr_Object = MibTableColumn
engBattCurr = _EngBattCurr_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 107),
    _EngBattCurr_Type()
)
engBattCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engBattCurr.setStatus("current")
_EngTorqueMode_Type = Unsigned32
_EngTorqueMode_Object = MibTableColumn
engTorqueMode = _EngTorqueMode_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 108),
    _EngTorqueMode_Type()
)
engTorqueMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engTorqueMode.setStatus("current")
_EngStarterMode_Type = Unsigned32
_EngStarterMode_Object = MibTableColumn
engStarterMode = _EngStarterMode_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 109),
    _EngStarterMode_Type()
)
engStarterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engStarterMode.setStatus("current")
_EngCIStatus_Type = Unsigned32
_EngCIStatus_Object = MibTableColumn
engCIStatus = _EngCIStatus_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 110),
    _EngCIStatus_Type()
)
engCIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engCIStatus.setStatus("current")
_EngDemandedSpeed_Type = Unsigned32
_EngDemandedSpeed_Object = MibTableColumn
engDemandedSpeed = _EngDemandedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 111),
    _EngDemandedSpeed_Type()
)
engDemandedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engDemandedSpeed.setStatus("current")
_EngSpeedFBUp_Type = Unsigned32
_EngSpeedFBUp_Object = MibTableColumn
engSpeedFBUp = _EngSpeedFBUp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 112),
    _EngSpeedFBUp_Type()
)
engSpeedFBUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engSpeedFBUp.setStatus("current")
_EngSpeedFBDown_Type = Unsigned32
_EngSpeedFBDown_Object = MibTableColumn
engSpeedFBDown = _EngSpeedFBDown_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 113),
    _EngSpeedFBDown_Type()
)
engSpeedFBDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engSpeedFBDown.setStatus("current")
_EngSpeedFailMode_Type = Unsigned32
_EngSpeedFailMode_Object = MibTableColumn
engSpeedFailMode = _EngSpeedFailMode_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 114),
    _EngSpeedFailMode_Type()
)
engSpeedFailMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engSpeedFailMode.setStatus("current")
_EngCurrSDSrc_Type = Unsigned32
_EngCurrSDSrc_Object = MibTableColumn
engCurrSDSrc = _EngCurrSDSrc_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 115),
    _EngCurrSDSrc_Type()
)
engCurrSDSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engCurrSDSrc.setStatus("current")
_EngFbackSDCAN_Type = Unsigned32
_EngFbackSDCAN_Object = MibTableColumn
engFbackSDCAN = _EngFbackSDCAN_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 116),
    _EngFbackSDCAN_Type()
)
engFbackSDCAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engFbackSDCAN.setStatus("current")
_EngFbackSDAnalog_Type = Unsigned32
_EngFbackSDAnalog_Object = MibTableColumn
engFbackSDAnalog = _EngFbackSDAnalog_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 117),
    _EngFbackSDAnalog_Type()
)
engFbackSDAnalog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engFbackSDAnalog.setStatus("current")
_EngFailureCodes_Type = Unsigned32
_EngFailureCodes_Object = MibTableColumn
engFailureCodes = _EngFailureCodes_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 118),
    _EngFailureCodes_Type()
)
engFailureCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engFailureCodes.setStatus("current")
_EngActDrop_Type = Unsigned32
_EngActDrop_Object = MibTableColumn
engActDrop = _EngActDrop_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 119),
    _EngActDrop_Type()
)
engActDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engActDrop.setStatus("current")
_EngStartStatus_Type = Unsigned32
_EngStartStatus_Object = MibTableColumn
engStartStatus = _EngStartStatus_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 120),
    _EngStartStatus_Type()
)
engStartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engStartStatus.setStatus("current")
_EngProtOrStatus_Type = Unsigned32
_EngProtOrStatus_Object = MibTableColumn
engProtOrStatus = _EngProtOrStatus_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 121),
    _EngProtOrStatus_Type()
)
engProtOrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engProtOrStatus.setStatus("current")
_EngMTURuniingState_Type = Unsigned32
_EngMTURuniingState_Object = MibTableColumn
engMTURuniingState = _EngMTURuniingState_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 122),
    _EngMTURuniingState_Type()
)
engMTURuniingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engMTURuniingState.setStatus("current")
_EngCylCutOff_Type = Unsigned32
_EngCylCutOff_Object = MibTableColumn
engCylCutOff = _EngCylCutOff_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 123),
    _EngCylCutOff_Type()
)
engCylCutOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engCylCutOff.setStatus("current")
_EngLoadGenStatus_Type = Unsigned32
_EngLoadGenStatus_Object = MibTableColumn
engLoadGenStatus = _EngLoadGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 124),
    _EngLoadGenStatus_Type()
)
engLoadGenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engLoadGenStatus.setStatus("current")
_EngEtxStopState_Type = Unsigned32
_EngEtxStopState_Object = MibTableColumn
engEtxStopState = _EngEtxStopState_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 125),
    _EngEtxStopState_Type()
)
engEtxStopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engEtxStopState.setStatus("current")
_EngCurrOPMode_Type = Unsigned32
_EngCurrOPMode_Object = MibTableColumn
engCurrOPMode = _EngCurrOPMode_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 126),
    _EngCurrOPMode_Type()
)
engCurrOPMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engCurrOPMode.setStatus("current")
_EngMTUReqTorque_Type = Unsigned32
_EngMTUReqTorque_Object = MibTableColumn
engMTUReqTorque = _EngMTUReqTorque_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 127),
    _EngMTUReqTorque_Type()
)
engMTUReqTorque.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engMTUReqTorque.setStatus("current")
_EngTripAvgFuel_Type = AverageFuelDiv100
_EngTripAvgFuel_Object = MibTableColumn
engTripAvgFuel = _EngTripAvgFuel_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 128),
    _EngTripAvgFuel_Type()
)
engTripAvgFuel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engTripAvgFuel.setStatus("current")
_EngECURatedPower_Type = Unsigned32
_EngECURatedPower_Object = MibTableColumn
engECURatedPower = _EngECURatedPower_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 129),
    _EngECURatedPower_Type()
)
engECURatedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engECURatedPower.setStatus("current")
_EngECURatedSpeed_Type = Unsigned32
_EngECURatedSpeed_Object = MibTableColumn
engECURatedSpeed = _EngECURatedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 130),
    _EngECURatedSpeed_Type()
)
engECURatedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engECURatedSpeed.setStatus("current")
_EngECUIdleSpeed_Type = Unsigned32
_EngECUIdleSpeed_Object = MibTableColumn
engECUIdleSpeed = _EngECUIdleSpeed_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 131),
    _EngECUIdleSpeed_Type()
)
engECUIdleSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engECUIdleSpeed.setStatus("current")
_EngECUDesirSpeed_Type = Unsigned32
_EngECUDesirSpeed_Object = MibTableColumn
engECUDesirSpeed = _EngECUDesirSpeed_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 132),
    _EngECUDesirSpeed_Type()
)
engECUDesirSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engECUDesirSpeed.setStatus("current")
_EngECUPreheatStat_Type = Unsigned32
_EngECUPreheatStat_Object = MibTableColumn
engECUPreheatStat = _EngECUPreheatStat_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 133),
    _EngECUPreheatStat_Type()
)
engECUPreheatStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engECUPreheatStat.setStatus("current")
_EngManiFoldPres_Type = Unsigned32
_EngManiFoldPres_Object = MibTableColumn
engManiFoldPres = _EngManiFoldPres_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 134),
    _EngManiFoldPres_Type()
)
engManiFoldPres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engManiFoldPres.setStatus("current")
_EngIntercoolerLevel_Type = Unsigned32
_EngIntercoolerLevel_Object = MibTableColumn
engIntercoolerLevel = _EngIntercoolerLevel_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 135),
    _EngIntercoolerLevel_Type()
)
engIntercoolerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engIntercoolerLevel.setStatus("current")
_EngCANLinkState_Type = Unsigned32
_EngCANLinkState_Object = MibTableColumn
engCANLinkState = _EngCANLinkState_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 136),
    _EngCANLinkState_Type()
)
engCANLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engCANLinkState.setStatus("current")
_EngAutoDFPRegInh_Type = Unsigned32
_EngAutoDFPRegInh_Object = MibTableColumn
engAutoDFPRegInh = _EngAutoDFPRegInh_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 137),
    _EngAutoDFPRegInh_Type()
)
engAutoDFPRegInh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engAutoDFPRegInh.setStatus("current")
_EngDPTCActRegInhSwitch_Type = Unsigned32
_EngDPTCActRegInhSwitch_Object = MibTableColumn
engDPTCActRegInhSwitch = _EngDPTCActRegInhSwitch_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 138),
    _EngDPTCActRegInhSwitch_Type()
)
engDPTCActRegInhSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engDPTCActRegInhSwitch.setStatus("current")
_EngSootLoadPC_Type = Unsigned32
_EngSootLoadPC_Object = MibTableColumn
engSootLoadPC = _EngSootLoadPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 139),
    _EngSootLoadPC_Type()
)
engSootLoadPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engSootLoadPC.setStatus("current")
_EngAshLoadPC_Type = Unsigned32
_EngAshLoadPC_Object = MibTableColumn
engAshLoadPC = _EngAshLoadPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 140),
    _EngAshLoadPC_Type()
)
engAshLoadPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engAshLoadPC.setStatus("current")
_EngDefTankLevel_Type = Unsigned32
_EngDefTankLevel_Object = MibTableColumn
engDefTankLevel = _EngDefTankLevel_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 141),
    _EngDefTankLevel_Type()
)
engDefTankLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engDefTankLevel.setStatus("current")
_EngDefTankTemp_Type = Unsigned32
_EngDefTankTemp_Object = MibTableColumn
engDefTankTemp = _EngDefTankTemp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 142),
    _EngDefTankTemp_Type()
)
engDefTankTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engDefTankTemp.setStatus("current")
_EngDefLevelWarn_Type = Unsigned32
_EngDefLevelWarn_Object = MibTableColumn
engDefLevelWarn = _EngDefLevelWarn_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 143),
    _EngDefLevelWarn_Type()
)
engDefLevelWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engDefLevelWarn.setStatus("current")
_EngDefReagentCons_Type = Unsigned32
_EngDefReagentCons_Object = MibTableColumn
engDefReagentCons = _EngDefReagentCons_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 144),
    _EngDefReagentCons_Type()
)
engDefReagentCons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engDefReagentCons.setStatus("current")
_EngDefInducReason_Type = Unsigned32
_EngDefInducReason_Object = MibTableColumn
engDefInducReason = _EngDefInducReason_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 145),
    _EngDefInducReason_Type()
)
engDefInducReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engDefInducReason.setStatus("current")
_EngDefInducSever_Type = Unsigned32
_EngDefInducSever_Object = MibTableColumn
engDefInducSever = _EngDefInducSever_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 146),
    _EngDefInducSever_Type()
)
engDefInducSever.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engDefInducSever.setStatus("current")
_EngDefCounterMin_Type = Unsigned32
_EngDefCounterMin_Object = MibTableColumn
engDefCounterMin = _EngDefCounterMin_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 147),
    _EngDefCounterMin_Type()
)
engDefCounterMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engDefCounterMin.setStatus("current")
_EngTLTTorqueReduc_Type = Unsigned32
_EngTLTTorqueReduc_Object = MibTableColumn
engTLTTorqueReduc = _EngTLTTorqueReduc_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 148),
    _EngTLTTorqueReduc_Type()
)
engTLTTorqueReduc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engTLTTorqueReduc.setStatus("current")
_EngTLTVehspdReduc_Type = Unsigned32
_EngTLTVehspdReduc_Object = MibTableColumn
engTLTVehspdReduc = _EngTLTVehspdReduc_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 149),
    _EngTLTVehspdReduc_Type()
)
engTLTVehspdReduc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engTLTVehspdReduc.setStatus("current")
_EngEGRPress_Type = Unsigned32
_EngEGRPress_Object = MibTableColumn
engEGRPress = _EngEGRPress_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 150),
    _EngEGRPress_Type()
)
engEGRPress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engEGRPress.setStatus("current")
_EngEGRTemp_Type = Unsigned32
_EngEGRTemp_Object = MibTableColumn
engEGRTemp = _EngEGRTemp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 151),
    _EngEGRTemp_Type()
)
engEGRTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engEGRTemp.setStatus("current")
_EngAmbAirTemp_Type = Unsigned32
_EngAmbAirTemp_Object = MibTableColumn
engAmbAirTemp = _EngAmbAirTemp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 152),
    _EngAmbAirTemp_Type()
)
engAmbAirTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engAmbAirTemp.setStatus("current")
_EngAirIntakeTemp_Type = Unsigned32
_EngAirIntakeTemp_Object = MibTableColumn
engAirIntakeTemp = _EngAirIntakeTemp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 153),
    _EngAirIntakeTemp_Type()
)
engAirIntakeTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engAirIntakeTemp.setStatus("current")


class _EngSRCOperatInduc_Type(Unsigned32):
    """Custom type engSRCOperatInduc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_EngSRCOperatInduc_Type.__name__ = "Unsigned32"
_EngSRCOperatInduc_Object = MibTableColumn
engSRCOperatInduc = _EngSRCOperatInduc_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 154),
    _EngSRCOperatInduc_Type()
)
engSRCOperatInduc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engSRCOperatInduc.setStatus("current")


class _EngTankLevLowLost_Type(Unsigned32):
    """Custom type engTankLevLowLost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_EngTankLevLowLost_Type.__name__ = "Unsigned32"
_EngTankLevLowLost_Object = MibTableColumn
engTankLevLowLost = _EngTankLevLowLost_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 155),
    _EngTankLevLowLost_Type()
)
engTankLevLowLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engTankLevLowLost.setStatus("current")


class _EngMiscAltSpeedSel_Type(Unsigned32):
    """Custom type engMiscAltSpeedSel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EngMiscAltSpeedSel_Type.__name__ = "Unsigned32"
_EngMiscAltSpeedSel_Object = MibTableColumn
engMiscAltSpeedSel = _EngMiscAltSpeedSel_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 156),
    _EngMiscAltSpeedSel_Type()
)
engMiscAltSpeedSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engMiscAltSpeedSel.setStatus("current")


class _EngExhGasP17Temp_Type(Integer32):
    """Custom type engExhGasP17Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngExhGasP17Temp_Type.__name__ = "Integer32"
_EngExhGasP17Temp_Object = MibTableColumn
engExhGasP17Temp = _EngExhGasP17Temp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 157),
    _EngExhGasP17Temp_Type()
)
engExhGasP17Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhGasP17Temp.setStatus("current")


class _EngExhGasP18Temp_Type(Integer32):
    """Custom type engExhGasP18Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngExhGasP18Temp_Type.__name__ = "Integer32"
_EngExhGasP18Temp_Object = MibTableColumn
engExhGasP18Temp = _EngExhGasP18Temp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 158),
    _EngExhGasP18Temp_Type()
)
engExhGasP18Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhGasP18Temp.setStatus("current")


class _EngExhGasP19Temp_Type(Integer32):
    """Custom type engExhGasP19Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngExhGasP19Temp_Type.__name__ = "Integer32"
_EngExhGasP19Temp_Object = MibTableColumn
engExhGasP19Temp = _EngExhGasP19Temp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 159),
    _EngExhGasP19Temp_Type()
)
engExhGasP19Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhGasP19Temp.setStatus("current")


class _EngExhGasP20Temp_Type(Integer32):
    """Custom type engExhGasP20Temp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-273, 1735),
    )


_EngExhGasP20Temp_Type.__name__ = "Integer32"
_EngExhGasP20Temp_Object = MibTableColumn
engExhGasP20Temp = _EngExhGasP20Temp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 160),
    _EngExhGasP20Temp_Type()
)
engExhGasP20Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engExhGasP20Temp.setStatus("current")
_EngInstFuelRate_Type = Unsigned32
_EngInstFuelRate_Object = MibTableColumn
engInstFuelRate = _EngInstFuelRate_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 161),
    _EngInstFuelRate_Type()
)
engInstFuelRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engInstFuelRate.setStatus("current")
_EngDPTCFiltStat_Type = Unsigned32
_EngDPTCFiltStat_Object = MibTableColumn
engDPTCFiltStat = _EngDPTCFiltStat_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 162),
    _EngDPTCFiltStat_Type()
)
engDPTCFiltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engDPTCFiltStat.setStatus("current")
_EngDPTCActRegInh_Type = Unsigned32
_EngDPTCActRegInh_Object = MibTableColumn
engDPTCActRegInh = _EngDPTCActRegInh_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 163),
    _EngDPTCActRegInh_Type()
)
engDPTCActRegInh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engDPTCActRegInh.setStatus("current")
_EngDPTCActRegInhEt_Type = Unsigned32
_EngDPTCActRegInhEt_Object = MibTableColumn
engDPTCActRegInhEt = _EngDPTCActRegInhEt_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 164),
    _EngDPTCActRegInhEt_Type()
)
engDPTCActRegInhEt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engDPTCActRegInhEt.setStatus("current")
_EngDefTankStat_Type = Unsigned32
_EngDefTankStat_Object = MibTableColumn
engDefTankStat = _EngDefTankStat_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 165),
    _EngDefTankStat_Type()
)
engDefTankStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engDefTankStat.setStatus("current")
_EngFuelGasPress_Type = Unsigned32
_EngFuelGasPress_Object = MibTableColumn
engFuelGasPress = _EngFuelGasPress_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 166),
    _EngFuelGasPress_Type()
)
engFuelGasPress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engFuelGasPress.setStatus("current")
_EngThrotPos1_Type = Unsigned32
_EngThrotPos1_Object = MibTableColumn
engThrotPos1 = _EngThrotPos1_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 167),
    _EngThrotPos1_Type()
)
engThrotPos1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engThrotPos1.setStatus("current")
_EngThrotPos2_Type = Unsigned32
_EngThrotPos2_Object = MibTableColumn
engThrotPos2 = _EngThrotPos2_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 3, 1, 168),
    _EngThrotPos2_Type()
)
engThrotPos2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    engThrotPos2.setStatus("current")
_GencommSection_ObjectIdentity = ObjectIdentity
gencommSection = _GencommSection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4)
)
_GencommP166Table_Object = MibTable
gencommP166Table = _GencommP166Table_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    gencommP166Table.setStatus("current")
_GencommP166Entry_Object = MibTableRow
gencommP166Entry = _GencommP166Entry_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1)
)
gencommP166Entry.setIndexNames(
    (0, "DSE-8610-MIB", "gencommP166KeyID"),
)
if mibBuilder.loadTexts:
    gencommP166Entry.setStatus("current")


class _GencommP166KeyID_Type(Integer32):
    """Custom type gencommP166KeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GencommP166KeyID_Type.__name__ = "Integer32"
_GencommP166KeyID_Object = MibTableColumn
gencommP166KeyID = _GencommP166KeyID_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 1),
    _GencommP166KeyID_Type()
)
gencommP166KeyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gencommP166KeyID.setStatus("current")
_GencommP166Reg_0_1_Type = Unsigned32
_GencommP166Reg_0_1_Object = MibTableColumn
gencommP166Reg_0_1 = _GencommP166Reg_0_1_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 2),
    _GencommP166Reg_0_1_Type()
)
gencommP166Reg_0_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_0_1.setStatus("current")
_GencommP166Reg_2_3_Type = Unsigned32
_GencommP166Reg_2_3_Object = MibTableColumn
gencommP166Reg_2_3 = _GencommP166Reg_2_3_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 3),
    _GencommP166Reg_2_3_Type()
)
gencommP166Reg_2_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_2_3.setStatus("current")
_GencommP166Reg_4_5_Type = Unsigned32
_GencommP166Reg_4_5_Object = MibTableColumn
gencommP166Reg_4_5 = _GencommP166Reg_4_5_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 4),
    _GencommP166Reg_4_5_Type()
)
gencommP166Reg_4_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_4_5.setStatus("current")
_GencommP166Reg_6_7_Type = Unsigned32
_GencommP166Reg_6_7_Object = MibTableColumn
gencommP166Reg_6_7 = _GencommP166Reg_6_7_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 5),
    _GencommP166Reg_6_7_Type()
)
gencommP166Reg_6_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_6_7.setStatus("current")
_GencommP166Reg_8_9_Type = Unsigned32
_GencommP166Reg_8_9_Object = MibTableColumn
gencommP166Reg_8_9 = _GencommP166Reg_8_9_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 6),
    _GencommP166Reg_8_9_Type()
)
gencommP166Reg_8_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_8_9.setStatus("current")
_GencommP166Reg_10_11_Type = Unsigned32
_GencommP166Reg_10_11_Object = MibTableColumn
gencommP166Reg_10_11 = _GencommP166Reg_10_11_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 7),
    _GencommP166Reg_10_11_Type()
)
gencommP166Reg_10_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_10_11.setStatus("current")
_GencommP166Reg_12_13_Type = Unsigned32
_GencommP166Reg_12_13_Object = MibTableColumn
gencommP166Reg_12_13 = _GencommP166Reg_12_13_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 8),
    _GencommP166Reg_12_13_Type()
)
gencommP166Reg_12_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_12_13.setStatus("current")
_GencommP166Reg_14_15_Type = Unsigned32
_GencommP166Reg_14_15_Object = MibTableColumn
gencommP166Reg_14_15 = _GencommP166Reg_14_15_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 9),
    _GencommP166Reg_14_15_Type()
)
gencommP166Reg_14_15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_14_15.setStatus("current")
_GencommP166Reg_16_17_Type = Unsigned32
_GencommP166Reg_16_17_Object = MibTableColumn
gencommP166Reg_16_17 = _GencommP166Reg_16_17_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 10),
    _GencommP166Reg_16_17_Type()
)
gencommP166Reg_16_17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_16_17.setStatus("current")
_GencommP166Reg_18_19_Type = Unsigned32
_GencommP166Reg_18_19_Object = MibTableColumn
gencommP166Reg_18_19 = _GencommP166Reg_18_19_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 11),
    _GencommP166Reg_18_19_Type()
)
gencommP166Reg_18_19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_18_19.setStatus("current")
_GencommP166Reg_20_21_Type = Unsigned32
_GencommP166Reg_20_21_Object = MibTableColumn
gencommP166Reg_20_21 = _GencommP166Reg_20_21_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 12),
    _GencommP166Reg_20_21_Type()
)
gencommP166Reg_20_21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_20_21.setStatus("current")
_GencommP166Reg_22_23_Type = Unsigned32
_GencommP166Reg_22_23_Object = MibTableColumn
gencommP166Reg_22_23 = _GencommP166Reg_22_23_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 13),
    _GencommP166Reg_22_23_Type()
)
gencommP166Reg_22_23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_22_23.setStatus("current")
_GencommP166Reg_24_25_Type = Unsigned32
_GencommP166Reg_24_25_Object = MibTableColumn
gencommP166Reg_24_25 = _GencommP166Reg_24_25_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 14),
    _GencommP166Reg_24_25_Type()
)
gencommP166Reg_24_25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_24_25.setStatus("current")
_GencommP166Reg_26_27_Type = Unsigned32
_GencommP166Reg_26_27_Object = MibTableColumn
gencommP166Reg_26_27 = _GencommP166Reg_26_27_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 15),
    _GencommP166Reg_26_27_Type()
)
gencommP166Reg_26_27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_26_27.setStatus("current")
_GencommP166Reg_28_29_Type = Unsigned32
_GencommP166Reg_28_29_Object = MibTableColumn
gencommP166Reg_28_29 = _GencommP166Reg_28_29_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 16),
    _GencommP166Reg_28_29_Type()
)
gencommP166Reg_28_29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_28_29.setStatus("current")
_GencommP166Reg_30_31_Type = Unsigned32
_GencommP166Reg_30_31_Object = MibTableColumn
gencommP166Reg_30_31 = _GencommP166Reg_30_31_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 17),
    _GencommP166Reg_30_31_Type()
)
gencommP166Reg_30_31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_30_31.setStatus("current")
_GencommP166Reg_32_33_Type = Unsigned32
_GencommP166Reg_32_33_Object = MibTableColumn
gencommP166Reg_32_33 = _GencommP166Reg_32_33_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 18),
    _GencommP166Reg_32_33_Type()
)
gencommP166Reg_32_33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_32_33.setStatus("current")
_GencommP166Reg_34_35_Type = Unsigned32
_GencommP166Reg_34_35_Object = MibTableColumn
gencommP166Reg_34_35 = _GencommP166Reg_34_35_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 19),
    _GencommP166Reg_34_35_Type()
)
gencommP166Reg_34_35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_34_35.setStatus("current")
_GencommP166Reg_36_37_Type = Unsigned32
_GencommP166Reg_36_37_Object = MibTableColumn
gencommP166Reg_36_37 = _GencommP166Reg_36_37_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 20),
    _GencommP166Reg_36_37_Type()
)
gencommP166Reg_36_37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_36_37.setStatus("current")
_GencommP166Reg_38_39_Type = Unsigned32
_GencommP166Reg_38_39_Object = MibTableColumn
gencommP166Reg_38_39 = _GencommP166Reg_38_39_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 21),
    _GencommP166Reg_38_39_Type()
)
gencommP166Reg_38_39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_38_39.setStatus("current")
_GencommP166Reg_40_41_Type = Unsigned32
_GencommP166Reg_40_41_Object = MibTableColumn
gencommP166Reg_40_41 = _GencommP166Reg_40_41_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 22),
    _GencommP166Reg_40_41_Type()
)
gencommP166Reg_40_41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_40_41.setStatus("current")
_GencommP166Reg_42_43_Type = Unsigned32
_GencommP166Reg_42_43_Object = MibTableColumn
gencommP166Reg_42_43 = _GencommP166Reg_42_43_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 23),
    _GencommP166Reg_42_43_Type()
)
gencommP166Reg_42_43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_42_43.setStatus("current")
_GencommP166Reg_44_45_Type = Unsigned32
_GencommP166Reg_44_45_Object = MibTableColumn
gencommP166Reg_44_45 = _GencommP166Reg_44_45_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 24),
    _GencommP166Reg_44_45_Type()
)
gencommP166Reg_44_45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_44_45.setStatus("current")
_GencommP166Reg_46_47_Type = Unsigned32
_GencommP166Reg_46_47_Object = MibTableColumn
gencommP166Reg_46_47 = _GencommP166Reg_46_47_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 25),
    _GencommP166Reg_46_47_Type()
)
gencommP166Reg_46_47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_46_47.setStatus("current")
_GencommP166Reg_48_49_Type = Unsigned32
_GencommP166Reg_48_49_Object = MibTableColumn
gencommP166Reg_48_49 = _GencommP166Reg_48_49_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 26),
    _GencommP166Reg_48_49_Type()
)
gencommP166Reg_48_49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_48_49.setStatus("current")
_GencommP166Reg_50_51_Type = Unsigned32
_GencommP166Reg_50_51_Object = MibTableColumn
gencommP166Reg_50_51 = _GencommP166Reg_50_51_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 27),
    _GencommP166Reg_50_51_Type()
)
gencommP166Reg_50_51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_50_51.setStatus("current")
_GencommP166Reg_52_53_Type = Unsigned32
_GencommP166Reg_52_53_Object = MibTableColumn
gencommP166Reg_52_53 = _GencommP166Reg_52_53_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 28),
    _GencommP166Reg_52_53_Type()
)
gencommP166Reg_52_53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_52_53.setStatus("current")
_GencommP166Reg_54_55_Type = Unsigned32
_GencommP166Reg_54_55_Object = MibTableColumn
gencommP166Reg_54_55 = _GencommP166Reg_54_55_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 29),
    _GencommP166Reg_54_55_Type()
)
gencommP166Reg_54_55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_54_55.setStatus("current")
_GencommP166Reg_56_57_Type = Unsigned32
_GencommP166Reg_56_57_Object = MibTableColumn
gencommP166Reg_56_57 = _GencommP166Reg_56_57_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 30),
    _GencommP166Reg_56_57_Type()
)
gencommP166Reg_56_57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_56_57.setStatus("current")
_GencommP166Reg_58_59_Type = Unsigned32
_GencommP166Reg_58_59_Object = MibTableColumn
gencommP166Reg_58_59 = _GencommP166Reg_58_59_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 31),
    _GencommP166Reg_58_59_Type()
)
gencommP166Reg_58_59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_58_59.setStatus("current")
_GencommP166Reg_60_61_Type = Unsigned32
_GencommP166Reg_60_61_Object = MibTableColumn
gencommP166Reg_60_61 = _GencommP166Reg_60_61_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 32),
    _GencommP166Reg_60_61_Type()
)
gencommP166Reg_60_61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_60_61.setStatus("current")
_GencommP166Reg_62_63_Type = Unsigned32
_GencommP166Reg_62_63_Object = MibTableColumn
gencommP166Reg_62_63 = _GencommP166Reg_62_63_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 33),
    _GencommP166Reg_62_63_Type()
)
gencommP166Reg_62_63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_62_63.setStatus("current")
_GencommP166Reg_64_65_Type = Unsigned32
_GencommP166Reg_64_65_Object = MibTableColumn
gencommP166Reg_64_65 = _GencommP166Reg_64_65_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 34),
    _GencommP166Reg_64_65_Type()
)
gencommP166Reg_64_65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_64_65.setStatus("current")
_GencommP166Reg_66_67_Type = Unsigned32
_GencommP166Reg_66_67_Object = MibTableColumn
gencommP166Reg_66_67 = _GencommP166Reg_66_67_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 35),
    _GencommP166Reg_66_67_Type()
)
gencommP166Reg_66_67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_66_67.setStatus("current")
_GencommP166Reg_68_69_Type = Unsigned32
_GencommP166Reg_68_69_Object = MibTableColumn
gencommP166Reg_68_69 = _GencommP166Reg_68_69_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 36),
    _GencommP166Reg_68_69_Type()
)
gencommP166Reg_68_69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_68_69.setStatus("current")
_GencommP166Reg_70_71_Type = Unsigned32
_GencommP166Reg_70_71_Object = MibTableColumn
gencommP166Reg_70_71 = _GencommP166Reg_70_71_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 37),
    _GencommP166Reg_70_71_Type()
)
gencommP166Reg_70_71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_70_71.setStatus("current")
_GencommP166Reg_72_73_Type = Unsigned32
_GencommP166Reg_72_73_Object = MibTableColumn
gencommP166Reg_72_73 = _GencommP166Reg_72_73_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 38),
    _GencommP166Reg_72_73_Type()
)
gencommP166Reg_72_73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_72_73.setStatus("current")
_GencommP166Reg_74_75_Type = Unsigned32
_GencommP166Reg_74_75_Object = MibTableColumn
gencommP166Reg_74_75 = _GencommP166Reg_74_75_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 39),
    _GencommP166Reg_74_75_Type()
)
gencommP166Reg_74_75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_74_75.setStatus("current")
_GencommP166Reg_76_77_Type = Unsigned32
_GencommP166Reg_76_77_Object = MibTableColumn
gencommP166Reg_76_77 = _GencommP166Reg_76_77_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 40),
    _GencommP166Reg_76_77_Type()
)
gencommP166Reg_76_77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_76_77.setStatus("current")
_GencommP166Reg_78_79_Type = Unsigned32
_GencommP166Reg_78_79_Object = MibTableColumn
gencommP166Reg_78_79 = _GencommP166Reg_78_79_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 41),
    _GencommP166Reg_78_79_Type()
)
gencommP166Reg_78_79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_78_79.setStatus("current")
_GencommP166Reg_80_81_Type = Unsigned32
_GencommP166Reg_80_81_Object = MibTableColumn
gencommP166Reg_80_81 = _GencommP166Reg_80_81_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 42),
    _GencommP166Reg_80_81_Type()
)
gencommP166Reg_80_81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_80_81.setStatus("current")
_GencommP166Reg_82_83_Type = Unsigned32
_GencommP166Reg_82_83_Object = MibTableColumn
gencommP166Reg_82_83 = _GencommP166Reg_82_83_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 43),
    _GencommP166Reg_82_83_Type()
)
gencommP166Reg_82_83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_82_83.setStatus("current")
_GencommP166Reg_84_85_Type = Unsigned32
_GencommP166Reg_84_85_Object = MibTableColumn
gencommP166Reg_84_85 = _GencommP166Reg_84_85_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 44),
    _GencommP166Reg_84_85_Type()
)
gencommP166Reg_84_85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_84_85.setStatus("current")
_GencommP166Reg_86_87_Type = Unsigned32
_GencommP166Reg_86_87_Object = MibTableColumn
gencommP166Reg_86_87 = _GencommP166Reg_86_87_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 45),
    _GencommP166Reg_86_87_Type()
)
gencommP166Reg_86_87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_86_87.setStatus("current")
_GencommP166Reg_88_89_Type = Unsigned32
_GencommP166Reg_88_89_Object = MibTableColumn
gencommP166Reg_88_89 = _GencommP166Reg_88_89_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 46),
    _GencommP166Reg_88_89_Type()
)
gencommP166Reg_88_89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_88_89.setStatus("current")
_GencommP166Reg_90_91_Type = Unsigned32
_GencommP166Reg_90_91_Object = MibTableColumn
gencommP166Reg_90_91 = _GencommP166Reg_90_91_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 47),
    _GencommP166Reg_90_91_Type()
)
gencommP166Reg_90_91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_90_91.setStatus("current")
_GencommP166Reg_92_93_Type = Unsigned32
_GencommP166Reg_92_93_Object = MibTableColumn
gencommP166Reg_92_93 = _GencommP166Reg_92_93_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 48),
    _GencommP166Reg_92_93_Type()
)
gencommP166Reg_92_93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_92_93.setStatus("current")
_GencommP166Reg_94_95_Type = Unsigned32
_GencommP166Reg_94_95_Object = MibTableColumn
gencommP166Reg_94_95 = _GencommP166Reg_94_95_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 49),
    _GencommP166Reg_94_95_Type()
)
gencommP166Reg_94_95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_94_95.setStatus("current")
_GencommP166Reg_96_97_Type = Unsigned32
_GencommP166Reg_96_97_Object = MibTableColumn
gencommP166Reg_96_97 = _GencommP166Reg_96_97_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 50),
    _GencommP166Reg_96_97_Type()
)
gencommP166Reg_96_97.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_96_97.setStatus("current")
_GencommP166Reg_98_99_Type = Unsigned32
_GencommP166Reg_98_99_Object = MibTableColumn
gencommP166Reg_98_99 = _GencommP166Reg_98_99_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 51),
    _GencommP166Reg_98_99_Type()
)
gencommP166Reg_98_99.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_98_99.setStatus("current")
_GencommP166Reg_100_101_Type = Unsigned32
_GencommP166Reg_100_101_Object = MibTableColumn
gencommP166Reg_100_101 = _GencommP166Reg_100_101_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 52),
    _GencommP166Reg_100_101_Type()
)
gencommP166Reg_100_101.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_100_101.setStatus("current")
_GencommP166Reg_102_103_Type = Unsigned32
_GencommP166Reg_102_103_Object = MibTableColumn
gencommP166Reg_102_103 = _GencommP166Reg_102_103_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 53),
    _GencommP166Reg_102_103_Type()
)
gencommP166Reg_102_103.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_102_103.setStatus("current")
_GencommP166Reg_104_105_Type = Unsigned32
_GencommP166Reg_104_105_Object = MibTableColumn
gencommP166Reg_104_105 = _GencommP166Reg_104_105_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 54),
    _GencommP166Reg_104_105_Type()
)
gencommP166Reg_104_105.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_104_105.setStatus("current")
_GencommP166Reg_106_107_Type = Unsigned32
_GencommP166Reg_106_107_Object = MibTableColumn
gencommP166Reg_106_107 = _GencommP166Reg_106_107_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 55),
    _GencommP166Reg_106_107_Type()
)
gencommP166Reg_106_107.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_106_107.setStatus("current")
_GencommP166Reg_108_109_Type = Unsigned32
_GencommP166Reg_108_109_Object = MibTableColumn
gencommP166Reg_108_109 = _GencommP166Reg_108_109_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 56),
    _GencommP166Reg_108_109_Type()
)
gencommP166Reg_108_109.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_108_109.setStatus("current")
_GencommP166Reg_110_111_Type = Unsigned32
_GencommP166Reg_110_111_Object = MibTableColumn
gencommP166Reg_110_111 = _GencommP166Reg_110_111_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 57),
    _GencommP166Reg_110_111_Type()
)
gencommP166Reg_110_111.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_110_111.setStatus("current")
_GencommP166Reg_112_113_Type = Unsigned32
_GencommP166Reg_112_113_Object = MibTableColumn
gencommP166Reg_112_113 = _GencommP166Reg_112_113_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 58),
    _GencommP166Reg_112_113_Type()
)
gencommP166Reg_112_113.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_112_113.setStatus("current")
_GencommP166Reg_114_115_Type = Unsigned32
_GencommP166Reg_114_115_Object = MibTableColumn
gencommP166Reg_114_115 = _GencommP166Reg_114_115_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 59),
    _GencommP166Reg_114_115_Type()
)
gencommP166Reg_114_115.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_114_115.setStatus("current")
_GencommP166Reg_116_117_Type = Unsigned32
_GencommP166Reg_116_117_Object = MibTableColumn
gencommP166Reg_116_117 = _GencommP166Reg_116_117_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 60),
    _GencommP166Reg_116_117_Type()
)
gencommP166Reg_116_117.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_116_117.setStatus("current")
_GencommP166Reg_118_119_Type = Unsigned32
_GencommP166Reg_118_119_Object = MibTableColumn
gencommP166Reg_118_119 = _GencommP166Reg_118_119_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 61),
    _GencommP166Reg_118_119_Type()
)
gencommP166Reg_118_119.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_118_119.setStatus("current")
_GencommP166Reg_120_121_Type = Unsigned32
_GencommP166Reg_120_121_Object = MibTableColumn
gencommP166Reg_120_121 = _GencommP166Reg_120_121_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 62),
    _GencommP166Reg_120_121_Type()
)
gencommP166Reg_120_121.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_120_121.setStatus("current")
_GencommP166Reg_122_123_Type = Unsigned32
_GencommP166Reg_122_123_Object = MibTableColumn
gencommP166Reg_122_123 = _GencommP166Reg_122_123_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 63),
    _GencommP166Reg_122_123_Type()
)
gencommP166Reg_122_123.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_122_123.setStatus("current")
_GencommP166Reg_124_125_Type = Unsigned32
_GencommP166Reg_124_125_Object = MibTableColumn
gencommP166Reg_124_125 = _GencommP166Reg_124_125_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 64),
    _GencommP166Reg_124_125_Type()
)
gencommP166Reg_124_125.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_124_125.setStatus("current")
_GencommP166Reg_126_127_Type = Unsigned32
_GencommP166Reg_126_127_Object = MibTableColumn
gencommP166Reg_126_127 = _GencommP166Reg_126_127_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 65),
    _GencommP166Reg_126_127_Type()
)
gencommP166Reg_126_127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_126_127.setStatus("current")
_GencommP166Reg_128_129_Type = Unsigned32
_GencommP166Reg_128_129_Object = MibTableColumn
gencommP166Reg_128_129 = _GencommP166Reg_128_129_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 66),
    _GencommP166Reg_128_129_Type()
)
gencommP166Reg_128_129.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_128_129.setStatus("current")
_GencommP166Reg_130_131_Type = Unsigned32
_GencommP166Reg_130_131_Object = MibTableColumn
gencommP166Reg_130_131 = _GencommP166Reg_130_131_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 67),
    _GencommP166Reg_130_131_Type()
)
gencommP166Reg_130_131.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_130_131.setStatus("current")
_GencommP166Reg_132_133_Type = Unsigned32
_GencommP166Reg_132_133_Object = MibTableColumn
gencommP166Reg_132_133 = _GencommP166Reg_132_133_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 68),
    _GencommP166Reg_132_133_Type()
)
gencommP166Reg_132_133.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_132_133.setStatus("current")
_GencommP166Reg_134_135_Type = Unsigned32
_GencommP166Reg_134_135_Object = MibTableColumn
gencommP166Reg_134_135 = _GencommP166Reg_134_135_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 69),
    _GencommP166Reg_134_135_Type()
)
gencommP166Reg_134_135.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_134_135.setStatus("current")
_GencommP166Reg_136_137_Type = Unsigned32
_GencommP166Reg_136_137_Object = MibTableColumn
gencommP166Reg_136_137 = _GencommP166Reg_136_137_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 70),
    _GencommP166Reg_136_137_Type()
)
gencommP166Reg_136_137.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_136_137.setStatus("current")
_GencommP166Reg_138_139_Type = Unsigned32
_GencommP166Reg_138_139_Object = MibTableColumn
gencommP166Reg_138_139 = _GencommP166Reg_138_139_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 71),
    _GencommP166Reg_138_139_Type()
)
gencommP166Reg_138_139.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_138_139.setStatus("current")
_GencommP166Reg_140_141_Type = Unsigned32
_GencommP166Reg_140_141_Object = MibTableColumn
gencommP166Reg_140_141 = _GencommP166Reg_140_141_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 72),
    _GencommP166Reg_140_141_Type()
)
gencommP166Reg_140_141.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_140_141.setStatus("current")
_GencommP166Reg_142_143_Type = Unsigned32
_GencommP166Reg_142_143_Object = MibTableColumn
gencommP166Reg_142_143 = _GencommP166Reg_142_143_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 73),
    _GencommP166Reg_142_143_Type()
)
gencommP166Reg_142_143.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_142_143.setStatus("current")
_GencommP166Reg_144_145_Type = Unsigned32
_GencommP166Reg_144_145_Object = MibTableColumn
gencommP166Reg_144_145 = _GencommP166Reg_144_145_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 74),
    _GencommP166Reg_144_145_Type()
)
gencommP166Reg_144_145.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_144_145.setStatus("current")
_GencommP166Reg_146_147_Type = Unsigned32
_GencommP166Reg_146_147_Object = MibTableColumn
gencommP166Reg_146_147 = _GencommP166Reg_146_147_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 75),
    _GencommP166Reg_146_147_Type()
)
gencommP166Reg_146_147.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_146_147.setStatus("current")
_GencommP166Reg_148_149_Type = Unsigned32
_GencommP166Reg_148_149_Object = MibTableColumn
gencommP166Reg_148_149 = _GencommP166Reg_148_149_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 76),
    _GencommP166Reg_148_149_Type()
)
gencommP166Reg_148_149.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_148_149.setStatus("current")
_GencommP166Reg_150_151_Type = Unsigned32
_GencommP166Reg_150_151_Object = MibTableColumn
gencommP166Reg_150_151 = _GencommP166Reg_150_151_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 77),
    _GencommP166Reg_150_151_Type()
)
gencommP166Reg_150_151.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_150_151.setStatus("current")
_GencommP166Reg_152_153_Type = Unsigned32
_GencommP166Reg_152_153_Object = MibTableColumn
gencommP166Reg_152_153 = _GencommP166Reg_152_153_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 78),
    _GencommP166Reg_152_153_Type()
)
gencommP166Reg_152_153.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_152_153.setStatus("current")
_GencommP166Reg_154_155_Type = Unsigned32
_GencommP166Reg_154_155_Object = MibTableColumn
gencommP166Reg_154_155 = _GencommP166Reg_154_155_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 79),
    _GencommP166Reg_154_155_Type()
)
gencommP166Reg_154_155.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_154_155.setStatus("current")
_GencommP166Reg_156_157_Type = Unsigned32
_GencommP166Reg_156_157_Object = MibTableColumn
gencommP166Reg_156_157 = _GencommP166Reg_156_157_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 80),
    _GencommP166Reg_156_157_Type()
)
gencommP166Reg_156_157.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_156_157.setStatus("current")
_GencommP166Reg_158_159_Type = Unsigned32
_GencommP166Reg_158_159_Object = MibTableColumn
gencommP166Reg_158_159 = _GencommP166Reg_158_159_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 81),
    _GencommP166Reg_158_159_Type()
)
gencommP166Reg_158_159.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_158_159.setStatus("current")
_GencommP166Reg_160_161_Type = Unsigned32
_GencommP166Reg_160_161_Object = MibTableColumn
gencommP166Reg_160_161 = _GencommP166Reg_160_161_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 82),
    _GencommP166Reg_160_161_Type()
)
gencommP166Reg_160_161.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_160_161.setStatus("current")
_GencommP166Reg_162_163_Type = Unsigned32
_GencommP166Reg_162_163_Object = MibTableColumn
gencommP166Reg_162_163 = _GencommP166Reg_162_163_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 83),
    _GencommP166Reg_162_163_Type()
)
gencommP166Reg_162_163.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_162_163.setStatus("current")
_GencommP166Reg_164_165_Type = Unsigned32
_GencommP166Reg_164_165_Object = MibTableColumn
gencommP166Reg_164_165 = _GencommP166Reg_164_165_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 84),
    _GencommP166Reg_164_165_Type()
)
gencommP166Reg_164_165.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_164_165.setStatus("current")
_GencommP166Reg_166_167_Type = Unsigned32
_GencommP166Reg_166_167_Object = MibTableColumn
gencommP166Reg_166_167 = _GencommP166Reg_166_167_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 85),
    _GencommP166Reg_166_167_Type()
)
gencommP166Reg_166_167.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_166_167.setStatus("current")
_GencommP166Reg_168_169_Type = Unsigned32
_GencommP166Reg_168_169_Object = MibTableColumn
gencommP166Reg_168_169 = _GencommP166Reg_168_169_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 86),
    _GencommP166Reg_168_169_Type()
)
gencommP166Reg_168_169.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_168_169.setStatus("current")
_GencommP166Reg_170_171_Type = Unsigned32
_GencommP166Reg_170_171_Object = MibTableColumn
gencommP166Reg_170_171 = _GencommP166Reg_170_171_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 87),
    _GencommP166Reg_170_171_Type()
)
gencommP166Reg_170_171.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_170_171.setStatus("current")
_GencommP166Reg_172_173_Type = Unsigned32
_GencommP166Reg_172_173_Object = MibTableColumn
gencommP166Reg_172_173 = _GencommP166Reg_172_173_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 88),
    _GencommP166Reg_172_173_Type()
)
gencommP166Reg_172_173.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_172_173.setStatus("current")
_GencommP166Reg_174_175_Type = Unsigned32
_GencommP166Reg_174_175_Object = MibTableColumn
gencommP166Reg_174_175 = _GencommP166Reg_174_175_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 89),
    _GencommP166Reg_174_175_Type()
)
gencommP166Reg_174_175.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_174_175.setStatus("current")
_GencommP166Reg_176_177_Type = Unsigned32
_GencommP166Reg_176_177_Object = MibTableColumn
gencommP166Reg_176_177 = _GencommP166Reg_176_177_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 90),
    _GencommP166Reg_176_177_Type()
)
gencommP166Reg_176_177.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_176_177.setStatus("current")
_GencommP166Reg_178_179_Type = Unsigned32
_GencommP166Reg_178_179_Object = MibTableColumn
gencommP166Reg_178_179 = _GencommP166Reg_178_179_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 91),
    _GencommP166Reg_178_179_Type()
)
gencommP166Reg_178_179.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_178_179.setStatus("current")
_GencommP166Reg_180_181_Type = Unsigned32
_GencommP166Reg_180_181_Object = MibTableColumn
gencommP166Reg_180_181 = _GencommP166Reg_180_181_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 92),
    _GencommP166Reg_180_181_Type()
)
gencommP166Reg_180_181.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_180_181.setStatus("current")
_GencommP166Reg_182_183_Type = Unsigned32
_GencommP166Reg_182_183_Object = MibTableColumn
gencommP166Reg_182_183 = _GencommP166Reg_182_183_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 93),
    _GencommP166Reg_182_183_Type()
)
gencommP166Reg_182_183.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_182_183.setStatus("current")
_GencommP166Reg_184_185_Type = Unsigned32
_GencommP166Reg_184_185_Object = MibTableColumn
gencommP166Reg_184_185 = _GencommP166Reg_184_185_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 94),
    _GencommP166Reg_184_185_Type()
)
gencommP166Reg_184_185.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_184_185.setStatus("current")
_GencommP166Reg_186_187_Type = Unsigned32
_GencommP166Reg_186_187_Object = MibTableColumn
gencommP166Reg_186_187 = _GencommP166Reg_186_187_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 95),
    _GencommP166Reg_186_187_Type()
)
gencommP166Reg_186_187.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_186_187.setStatus("current")
_GencommP166Reg_188_189_Type = Unsigned32
_GencommP166Reg_188_189_Object = MibTableColumn
gencommP166Reg_188_189 = _GencommP166Reg_188_189_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 96),
    _GencommP166Reg_188_189_Type()
)
gencommP166Reg_188_189.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_188_189.setStatus("current")
_GencommP166Reg_190_191_Type = Unsigned32
_GencommP166Reg_190_191_Object = MibTableColumn
gencommP166Reg_190_191 = _GencommP166Reg_190_191_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 97),
    _GencommP166Reg_190_191_Type()
)
gencommP166Reg_190_191.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_190_191.setStatus("current")
_GencommP166Reg_192_193_Type = Unsigned32
_GencommP166Reg_192_193_Object = MibTableColumn
gencommP166Reg_192_193 = _GencommP166Reg_192_193_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 98),
    _GencommP166Reg_192_193_Type()
)
gencommP166Reg_192_193.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_192_193.setStatus("current")
_GencommP166Reg_194_195_Type = Unsigned32
_GencommP166Reg_194_195_Object = MibTableColumn
gencommP166Reg_194_195 = _GencommP166Reg_194_195_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 99),
    _GencommP166Reg_194_195_Type()
)
gencommP166Reg_194_195.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_194_195.setStatus("current")
_GencommP166Reg_196_197_Type = Unsigned32
_GencommP166Reg_196_197_Object = MibTableColumn
gencommP166Reg_196_197 = _GencommP166Reg_196_197_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 100),
    _GencommP166Reg_196_197_Type()
)
gencommP166Reg_196_197.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_196_197.setStatus("current")
_GencommP166Reg_198_199_Type = Unsigned32
_GencommP166Reg_198_199_Object = MibTableColumn
gencommP166Reg_198_199 = _GencommP166Reg_198_199_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 101),
    _GencommP166Reg_198_199_Type()
)
gencommP166Reg_198_199.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_198_199.setStatus("current")
_GencommP166Reg_200_201_Type = Unsigned32
_GencommP166Reg_200_201_Object = MibTableColumn
gencommP166Reg_200_201 = _GencommP166Reg_200_201_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 102),
    _GencommP166Reg_200_201_Type()
)
gencommP166Reg_200_201.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_200_201.setStatus("current")
_GencommP166Reg_202_203_Type = Unsigned32
_GencommP166Reg_202_203_Object = MibTableColumn
gencommP166Reg_202_203 = _GencommP166Reg_202_203_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 103),
    _GencommP166Reg_202_203_Type()
)
gencommP166Reg_202_203.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_202_203.setStatus("current")
_GencommP166Reg_204_205_Type = Unsigned32
_GencommP166Reg_204_205_Object = MibTableColumn
gencommP166Reg_204_205 = _GencommP166Reg_204_205_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 104),
    _GencommP166Reg_204_205_Type()
)
gencommP166Reg_204_205.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_204_205.setStatus("current")
_GencommP166Reg_206_207_Type = Unsigned32
_GencommP166Reg_206_207_Object = MibTableColumn
gencommP166Reg_206_207 = _GencommP166Reg_206_207_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 105),
    _GencommP166Reg_206_207_Type()
)
gencommP166Reg_206_207.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_206_207.setStatus("current")
_GencommP166Reg_208_209_Type = Unsigned32
_GencommP166Reg_208_209_Object = MibTableColumn
gencommP166Reg_208_209 = _GencommP166Reg_208_209_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 106),
    _GencommP166Reg_208_209_Type()
)
gencommP166Reg_208_209.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_208_209.setStatus("current")
_GencommP166Reg_210_211_Type = Unsigned32
_GencommP166Reg_210_211_Object = MibTableColumn
gencommP166Reg_210_211 = _GencommP166Reg_210_211_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 107),
    _GencommP166Reg_210_211_Type()
)
gencommP166Reg_210_211.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_210_211.setStatus("current")
_GencommP166Reg_212_213_Type = Unsigned32
_GencommP166Reg_212_213_Object = MibTableColumn
gencommP166Reg_212_213 = _GencommP166Reg_212_213_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 108),
    _GencommP166Reg_212_213_Type()
)
gencommP166Reg_212_213.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_212_213.setStatus("current")
_GencommP166Reg_214_215_Type = Unsigned32
_GencommP166Reg_214_215_Object = MibTableColumn
gencommP166Reg_214_215 = _GencommP166Reg_214_215_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 109),
    _GencommP166Reg_214_215_Type()
)
gencommP166Reg_214_215.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_214_215.setStatus("current")
_GencommP166Reg_216_217_Type = Unsigned32
_GencommP166Reg_216_217_Object = MibTableColumn
gencommP166Reg_216_217 = _GencommP166Reg_216_217_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 110),
    _GencommP166Reg_216_217_Type()
)
gencommP166Reg_216_217.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_216_217.setStatus("current")
_GencommP166Reg_218_219_Type = Unsigned32
_GencommP166Reg_218_219_Object = MibTableColumn
gencommP166Reg_218_219 = _GencommP166Reg_218_219_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 111),
    _GencommP166Reg_218_219_Type()
)
gencommP166Reg_218_219.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_218_219.setStatus("current")
_GencommP166Reg_220_221_Type = Unsigned32
_GencommP166Reg_220_221_Object = MibTableColumn
gencommP166Reg_220_221 = _GencommP166Reg_220_221_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 112),
    _GencommP166Reg_220_221_Type()
)
gencommP166Reg_220_221.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_220_221.setStatus("current")
_GencommP166Reg_222_223_Type = Unsigned32
_GencommP166Reg_222_223_Object = MibTableColumn
gencommP166Reg_222_223 = _GencommP166Reg_222_223_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 113),
    _GencommP166Reg_222_223_Type()
)
gencommP166Reg_222_223.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_222_223.setStatus("current")
_GencommP166Reg_224_225_Type = Unsigned32
_GencommP166Reg_224_225_Object = MibTableColumn
gencommP166Reg_224_225 = _GencommP166Reg_224_225_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 114),
    _GencommP166Reg_224_225_Type()
)
gencommP166Reg_224_225.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_224_225.setStatus("current")
_GencommP166Reg_226_227_Type = Unsigned32
_GencommP166Reg_226_227_Object = MibTableColumn
gencommP166Reg_226_227 = _GencommP166Reg_226_227_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 115),
    _GencommP166Reg_226_227_Type()
)
gencommP166Reg_226_227.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_226_227.setStatus("current")
_GencommP166Reg_228_229_Type = Unsigned32
_GencommP166Reg_228_229_Object = MibTableColumn
gencommP166Reg_228_229 = _GencommP166Reg_228_229_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 116),
    _GencommP166Reg_228_229_Type()
)
gencommP166Reg_228_229.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_228_229.setStatus("current")
_GencommP166Reg_230_231_Type = Unsigned32
_GencommP166Reg_230_231_Object = MibTableColumn
gencommP166Reg_230_231 = _GencommP166Reg_230_231_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 117),
    _GencommP166Reg_230_231_Type()
)
gencommP166Reg_230_231.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_230_231.setStatus("current")
_GencommP166Reg_232_233_Type = Unsigned32
_GencommP166Reg_232_233_Object = MibTableColumn
gencommP166Reg_232_233 = _GencommP166Reg_232_233_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 118),
    _GencommP166Reg_232_233_Type()
)
gencommP166Reg_232_233.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_232_233.setStatus("current")
_GencommP166Reg_234_235_Type = Unsigned32
_GencommP166Reg_234_235_Object = MibTableColumn
gencommP166Reg_234_235 = _GencommP166Reg_234_235_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 119),
    _GencommP166Reg_234_235_Type()
)
gencommP166Reg_234_235.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_234_235.setStatus("current")
_GencommP166Reg_236_237_Type = Unsigned32
_GencommP166Reg_236_237_Object = MibTableColumn
gencommP166Reg_236_237 = _GencommP166Reg_236_237_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 120),
    _GencommP166Reg_236_237_Type()
)
gencommP166Reg_236_237.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_236_237.setStatus("current")
_GencommP166Reg_238_239_Type = Unsigned32
_GencommP166Reg_238_239_Object = MibTableColumn
gencommP166Reg_238_239 = _GencommP166Reg_238_239_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 121),
    _GencommP166Reg_238_239_Type()
)
gencommP166Reg_238_239.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_238_239.setStatus("current")
_GencommP166Reg_240_241_Type = Unsigned32
_GencommP166Reg_240_241_Object = MibTableColumn
gencommP166Reg_240_241 = _GencommP166Reg_240_241_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 122),
    _GencommP166Reg_240_241_Type()
)
gencommP166Reg_240_241.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_240_241.setStatus("current")
_GencommP166Reg_242_243_Type = Unsigned32
_GencommP166Reg_242_243_Object = MibTableColumn
gencommP166Reg_242_243 = _GencommP166Reg_242_243_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 123),
    _GencommP166Reg_242_243_Type()
)
gencommP166Reg_242_243.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_242_243.setStatus("current")
_GencommP166Reg_244_245_Type = Unsigned32
_GencommP166Reg_244_245_Object = MibTableColumn
gencommP166Reg_244_245 = _GencommP166Reg_244_245_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 124),
    _GencommP166Reg_244_245_Type()
)
gencommP166Reg_244_245.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_244_245.setStatus("current")
_GencommP166Reg_246_247_Type = Unsigned32
_GencommP166Reg_246_247_Object = MibTableColumn
gencommP166Reg_246_247 = _GencommP166Reg_246_247_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 125),
    _GencommP166Reg_246_247_Type()
)
gencommP166Reg_246_247.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_246_247.setStatus("current")
_GencommP166Reg_248_249_Type = Unsigned32
_GencommP166Reg_248_249_Object = MibTableColumn
gencommP166Reg_248_249 = _GencommP166Reg_248_249_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 126),
    _GencommP166Reg_248_249_Type()
)
gencommP166Reg_248_249.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_248_249.setStatus("current")
_GencommP166Reg_250_251_Type = Unsigned32
_GencommP166Reg_250_251_Object = MibTableColumn
gencommP166Reg_250_251 = _GencommP166Reg_250_251_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 127),
    _GencommP166Reg_250_251_Type()
)
gencommP166Reg_250_251.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_250_251.setStatus("current")
_GencommP166Reg_252_253_Type = Unsigned32
_GencommP166Reg_252_253_Object = MibTableColumn
gencommP166Reg_252_253 = _GencommP166Reg_252_253_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 128),
    _GencommP166Reg_252_253_Type()
)
gencommP166Reg_252_253.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_252_253.setStatus("current")
_GencommP166Reg_254_255_Type = Unsigned32
_GencommP166Reg_254_255_Object = MibTableColumn
gencommP166Reg_254_255 = _GencommP166Reg_254_255_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 1, 1, 129),
    _GencommP166Reg_254_255_Type()
)
gencommP166Reg_254_255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP166Reg_254_255.setStatus("current")
_GencommP167Table_Object = MibTable
gencommP167Table = _GencommP167Table_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2)
)
if mibBuilder.loadTexts:
    gencommP167Table.setStatus("current")
_GencommP167Entry_Object = MibTableRow
gencommP167Entry = _GencommP167Entry_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1)
)
gencommP167Entry.setIndexNames(
    (0, "DSE-8610-MIB", "gencommP167KeyID"),
)
if mibBuilder.loadTexts:
    gencommP167Entry.setStatus("current")


class _GencommP167KeyID_Type(Integer32):
    """Custom type gencommP167KeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GencommP167KeyID_Type.__name__ = "Integer32"
_GencommP167KeyID_Object = MibTableColumn
gencommP167KeyID = _GencommP167KeyID_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 1),
    _GencommP167KeyID_Type()
)
gencommP167KeyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gencommP167KeyID.setStatus("current")
_GencommP167Reg_0_1_Type = Unsigned32
_GencommP167Reg_0_1_Object = MibTableColumn
gencommP167Reg_0_1 = _GencommP167Reg_0_1_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 2),
    _GencommP167Reg_0_1_Type()
)
gencommP167Reg_0_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_0_1.setStatus("current")
_GencommP167Reg_2_3_Type = Unsigned32
_GencommP167Reg_2_3_Object = MibTableColumn
gencommP167Reg_2_3 = _GencommP167Reg_2_3_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 3),
    _GencommP167Reg_2_3_Type()
)
gencommP167Reg_2_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_2_3.setStatus("current")
_GencommP167Reg_4_5_Type = Unsigned32
_GencommP167Reg_4_5_Object = MibTableColumn
gencommP167Reg_4_5 = _GencommP167Reg_4_5_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 4),
    _GencommP167Reg_4_5_Type()
)
gencommP167Reg_4_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_4_5.setStatus("current")
_GencommP167Reg_6_7_Type = Unsigned32
_GencommP167Reg_6_7_Object = MibTableColumn
gencommP167Reg_6_7 = _GencommP167Reg_6_7_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 5),
    _GencommP167Reg_6_7_Type()
)
gencommP167Reg_6_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_6_7.setStatus("current")
_GencommP167Reg_8_9_Type = Unsigned32
_GencommP167Reg_8_9_Object = MibTableColumn
gencommP167Reg_8_9 = _GencommP167Reg_8_9_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 6),
    _GencommP167Reg_8_9_Type()
)
gencommP167Reg_8_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_8_9.setStatus("current")
_GencommP167Reg_10_11_Type = Unsigned32
_GencommP167Reg_10_11_Object = MibTableColumn
gencommP167Reg_10_11 = _GencommP167Reg_10_11_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 7),
    _GencommP167Reg_10_11_Type()
)
gencommP167Reg_10_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_10_11.setStatus("current")
_GencommP167Reg_12_13_Type = Unsigned32
_GencommP167Reg_12_13_Object = MibTableColumn
gencommP167Reg_12_13 = _GencommP167Reg_12_13_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 8),
    _GencommP167Reg_12_13_Type()
)
gencommP167Reg_12_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_12_13.setStatus("current")
_GencommP167Reg_14_15_Type = Unsigned32
_GencommP167Reg_14_15_Object = MibTableColumn
gencommP167Reg_14_15 = _GencommP167Reg_14_15_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 9),
    _GencommP167Reg_14_15_Type()
)
gencommP167Reg_14_15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_14_15.setStatus("current")
_GencommP167Reg_16_17_Type = Unsigned32
_GencommP167Reg_16_17_Object = MibTableColumn
gencommP167Reg_16_17 = _GencommP167Reg_16_17_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 10),
    _GencommP167Reg_16_17_Type()
)
gencommP167Reg_16_17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_16_17.setStatus("current")
_GencommP167Reg_18_19_Type = Unsigned32
_GencommP167Reg_18_19_Object = MibTableColumn
gencommP167Reg_18_19 = _GencommP167Reg_18_19_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 11),
    _GencommP167Reg_18_19_Type()
)
gencommP167Reg_18_19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_18_19.setStatus("current")
_GencommP167Reg_20_21_Type = Unsigned32
_GencommP167Reg_20_21_Object = MibTableColumn
gencommP167Reg_20_21 = _GencommP167Reg_20_21_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 12),
    _GencommP167Reg_20_21_Type()
)
gencommP167Reg_20_21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_20_21.setStatus("current")
_GencommP167Reg_22_23_Type = Unsigned32
_GencommP167Reg_22_23_Object = MibTableColumn
gencommP167Reg_22_23 = _GencommP167Reg_22_23_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 13),
    _GencommP167Reg_22_23_Type()
)
gencommP167Reg_22_23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_22_23.setStatus("current")
_GencommP167Reg_24_25_Type = Unsigned32
_GencommP167Reg_24_25_Object = MibTableColumn
gencommP167Reg_24_25 = _GencommP167Reg_24_25_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 14),
    _GencommP167Reg_24_25_Type()
)
gencommP167Reg_24_25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_24_25.setStatus("current")
_GencommP167Reg_26_27_Type = Unsigned32
_GencommP167Reg_26_27_Object = MibTableColumn
gencommP167Reg_26_27 = _GencommP167Reg_26_27_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 15),
    _GencommP167Reg_26_27_Type()
)
gencommP167Reg_26_27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_26_27.setStatus("current")
_GencommP167Reg_28_29_Type = Unsigned32
_GencommP167Reg_28_29_Object = MibTableColumn
gencommP167Reg_28_29 = _GencommP167Reg_28_29_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 16),
    _GencommP167Reg_28_29_Type()
)
gencommP167Reg_28_29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_28_29.setStatus("current")
_GencommP167Reg_30_31_Type = Unsigned32
_GencommP167Reg_30_31_Object = MibTableColumn
gencommP167Reg_30_31 = _GencommP167Reg_30_31_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 17),
    _GencommP167Reg_30_31_Type()
)
gencommP167Reg_30_31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_30_31.setStatus("current")
_GencommP167Reg_32_33_Type = Unsigned32
_GencommP167Reg_32_33_Object = MibTableColumn
gencommP167Reg_32_33 = _GencommP167Reg_32_33_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 18),
    _GencommP167Reg_32_33_Type()
)
gencommP167Reg_32_33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_32_33.setStatus("current")
_GencommP167Reg_34_35_Type = Unsigned32
_GencommP167Reg_34_35_Object = MibTableColumn
gencommP167Reg_34_35 = _GencommP167Reg_34_35_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 19),
    _GencommP167Reg_34_35_Type()
)
gencommP167Reg_34_35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_34_35.setStatus("current")
_GencommP167Reg_36_37_Type = Unsigned32
_GencommP167Reg_36_37_Object = MibTableColumn
gencommP167Reg_36_37 = _GencommP167Reg_36_37_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 20),
    _GencommP167Reg_36_37_Type()
)
gencommP167Reg_36_37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_36_37.setStatus("current")
_GencommP167Reg_38_39_Type = Unsigned32
_GencommP167Reg_38_39_Object = MibTableColumn
gencommP167Reg_38_39 = _GencommP167Reg_38_39_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 21),
    _GencommP167Reg_38_39_Type()
)
gencommP167Reg_38_39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_38_39.setStatus("current")
_GencommP167Reg_40_41_Type = Unsigned32
_GencommP167Reg_40_41_Object = MibTableColumn
gencommP167Reg_40_41 = _GencommP167Reg_40_41_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 22),
    _GencommP167Reg_40_41_Type()
)
gencommP167Reg_40_41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_40_41.setStatus("current")
_GencommP167Reg_42_43_Type = Unsigned32
_GencommP167Reg_42_43_Object = MibTableColumn
gencommP167Reg_42_43 = _GencommP167Reg_42_43_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 23),
    _GencommP167Reg_42_43_Type()
)
gencommP167Reg_42_43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_42_43.setStatus("current")
_GencommP167Reg_44_45_Type = Unsigned32
_GencommP167Reg_44_45_Object = MibTableColumn
gencommP167Reg_44_45 = _GencommP167Reg_44_45_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 24),
    _GencommP167Reg_44_45_Type()
)
gencommP167Reg_44_45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_44_45.setStatus("current")
_GencommP167Reg_46_47_Type = Unsigned32
_GencommP167Reg_46_47_Object = MibTableColumn
gencommP167Reg_46_47 = _GencommP167Reg_46_47_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 25),
    _GencommP167Reg_46_47_Type()
)
gencommP167Reg_46_47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_46_47.setStatus("current")
_GencommP167Reg_48_49_Type = Unsigned32
_GencommP167Reg_48_49_Object = MibTableColumn
gencommP167Reg_48_49 = _GencommP167Reg_48_49_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 26),
    _GencommP167Reg_48_49_Type()
)
gencommP167Reg_48_49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_48_49.setStatus("current")
_GencommP167Reg_50_51_Type = Unsigned32
_GencommP167Reg_50_51_Object = MibTableColumn
gencommP167Reg_50_51 = _GencommP167Reg_50_51_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 27),
    _GencommP167Reg_50_51_Type()
)
gencommP167Reg_50_51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_50_51.setStatus("current")
_GencommP167Reg_52_53_Type = Unsigned32
_GencommP167Reg_52_53_Object = MibTableColumn
gencommP167Reg_52_53 = _GencommP167Reg_52_53_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 28),
    _GencommP167Reg_52_53_Type()
)
gencommP167Reg_52_53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_52_53.setStatus("current")
_GencommP167Reg_54_55_Type = Unsigned32
_GencommP167Reg_54_55_Object = MibTableColumn
gencommP167Reg_54_55 = _GencommP167Reg_54_55_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 29),
    _GencommP167Reg_54_55_Type()
)
gencommP167Reg_54_55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_54_55.setStatus("current")
_GencommP167Reg_56_57_Type = Unsigned32
_GencommP167Reg_56_57_Object = MibTableColumn
gencommP167Reg_56_57 = _GencommP167Reg_56_57_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 30),
    _GencommP167Reg_56_57_Type()
)
gencommP167Reg_56_57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_56_57.setStatus("current")
_GencommP167Reg_58_59_Type = Unsigned32
_GencommP167Reg_58_59_Object = MibTableColumn
gencommP167Reg_58_59 = _GencommP167Reg_58_59_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 31),
    _GencommP167Reg_58_59_Type()
)
gencommP167Reg_58_59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_58_59.setStatus("current")
_GencommP167Reg_60_61_Type = Unsigned32
_GencommP167Reg_60_61_Object = MibTableColumn
gencommP167Reg_60_61 = _GencommP167Reg_60_61_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 32),
    _GencommP167Reg_60_61_Type()
)
gencommP167Reg_60_61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_60_61.setStatus("current")
_GencommP167Reg_62_63_Type = Unsigned32
_GencommP167Reg_62_63_Object = MibTableColumn
gencommP167Reg_62_63 = _GencommP167Reg_62_63_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 33),
    _GencommP167Reg_62_63_Type()
)
gencommP167Reg_62_63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_62_63.setStatus("current")
_GencommP167Reg_64_65_Type = Unsigned32
_GencommP167Reg_64_65_Object = MibTableColumn
gencommP167Reg_64_65 = _GencommP167Reg_64_65_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 34),
    _GencommP167Reg_64_65_Type()
)
gencommP167Reg_64_65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_64_65.setStatus("current")
_GencommP167Reg_66_67_Type = Unsigned32
_GencommP167Reg_66_67_Object = MibTableColumn
gencommP167Reg_66_67 = _GencommP167Reg_66_67_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 35),
    _GencommP167Reg_66_67_Type()
)
gencommP167Reg_66_67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_66_67.setStatus("current")
_GencommP167Reg_68_69_Type = Unsigned32
_GencommP167Reg_68_69_Object = MibTableColumn
gencommP167Reg_68_69 = _GencommP167Reg_68_69_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 36),
    _GencommP167Reg_68_69_Type()
)
gencommP167Reg_68_69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_68_69.setStatus("current")
_GencommP167Reg_70_71_Type = Unsigned32
_GencommP167Reg_70_71_Object = MibTableColumn
gencommP167Reg_70_71 = _GencommP167Reg_70_71_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 37),
    _GencommP167Reg_70_71_Type()
)
gencommP167Reg_70_71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_70_71.setStatus("current")
_GencommP167Reg_72_73_Type = Unsigned32
_GencommP167Reg_72_73_Object = MibTableColumn
gencommP167Reg_72_73 = _GencommP167Reg_72_73_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 38),
    _GencommP167Reg_72_73_Type()
)
gencommP167Reg_72_73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_72_73.setStatus("current")
_GencommP167Reg_74_75_Type = Unsigned32
_GencommP167Reg_74_75_Object = MibTableColumn
gencommP167Reg_74_75 = _GencommP167Reg_74_75_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 39),
    _GencommP167Reg_74_75_Type()
)
gencommP167Reg_74_75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_74_75.setStatus("current")
_GencommP167Reg_76_77_Type = Unsigned32
_GencommP167Reg_76_77_Object = MibTableColumn
gencommP167Reg_76_77 = _GencommP167Reg_76_77_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 40),
    _GencommP167Reg_76_77_Type()
)
gencommP167Reg_76_77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_76_77.setStatus("current")
_GencommP167Reg_78_79_Type = Unsigned32
_GencommP167Reg_78_79_Object = MibTableColumn
gencommP167Reg_78_79 = _GencommP167Reg_78_79_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 41),
    _GencommP167Reg_78_79_Type()
)
gencommP167Reg_78_79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_78_79.setStatus("current")
_GencommP167Reg_80_81_Type = Unsigned32
_GencommP167Reg_80_81_Object = MibTableColumn
gencommP167Reg_80_81 = _GencommP167Reg_80_81_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 42),
    _GencommP167Reg_80_81_Type()
)
gencommP167Reg_80_81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_80_81.setStatus("current")
_GencommP167Reg_82_83_Type = Unsigned32
_GencommP167Reg_82_83_Object = MibTableColumn
gencommP167Reg_82_83 = _GencommP167Reg_82_83_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 43),
    _GencommP167Reg_82_83_Type()
)
gencommP167Reg_82_83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_82_83.setStatus("current")
_GencommP167Reg_84_85_Type = Unsigned32
_GencommP167Reg_84_85_Object = MibTableColumn
gencommP167Reg_84_85 = _GencommP167Reg_84_85_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 44),
    _GencommP167Reg_84_85_Type()
)
gencommP167Reg_84_85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_84_85.setStatus("current")
_GencommP167Reg_86_87_Type = Unsigned32
_GencommP167Reg_86_87_Object = MibTableColumn
gencommP167Reg_86_87 = _GencommP167Reg_86_87_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 45),
    _GencommP167Reg_86_87_Type()
)
gencommP167Reg_86_87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_86_87.setStatus("current")
_GencommP167Reg_88_89_Type = Unsigned32
_GencommP167Reg_88_89_Object = MibTableColumn
gencommP167Reg_88_89 = _GencommP167Reg_88_89_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 46),
    _GencommP167Reg_88_89_Type()
)
gencommP167Reg_88_89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_88_89.setStatus("current")
_GencommP167Reg_90_91_Type = Unsigned32
_GencommP167Reg_90_91_Object = MibTableColumn
gencommP167Reg_90_91 = _GencommP167Reg_90_91_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 47),
    _GencommP167Reg_90_91_Type()
)
gencommP167Reg_90_91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_90_91.setStatus("current")
_GencommP167Reg_92_93_Type = Unsigned32
_GencommP167Reg_92_93_Object = MibTableColumn
gencommP167Reg_92_93 = _GencommP167Reg_92_93_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 48),
    _GencommP167Reg_92_93_Type()
)
gencommP167Reg_92_93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_92_93.setStatus("current")
_GencommP167Reg_94_95_Type = Unsigned32
_GencommP167Reg_94_95_Object = MibTableColumn
gencommP167Reg_94_95 = _GencommP167Reg_94_95_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 49),
    _GencommP167Reg_94_95_Type()
)
gencommP167Reg_94_95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_94_95.setStatus("current")
_GencommP167Reg_96_97_Type = Unsigned32
_GencommP167Reg_96_97_Object = MibTableColumn
gencommP167Reg_96_97 = _GencommP167Reg_96_97_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 50),
    _GencommP167Reg_96_97_Type()
)
gencommP167Reg_96_97.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_96_97.setStatus("current")
_GencommP167Reg_98_99_Type = Unsigned32
_GencommP167Reg_98_99_Object = MibTableColumn
gencommP167Reg_98_99 = _GencommP167Reg_98_99_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 51),
    _GencommP167Reg_98_99_Type()
)
gencommP167Reg_98_99.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_98_99.setStatus("current")
_GencommP167Reg_100_101_Type = Unsigned32
_GencommP167Reg_100_101_Object = MibTableColumn
gencommP167Reg_100_101 = _GencommP167Reg_100_101_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 52),
    _GencommP167Reg_100_101_Type()
)
gencommP167Reg_100_101.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_100_101.setStatus("current")
_GencommP167Reg_102_103_Type = Unsigned32
_GencommP167Reg_102_103_Object = MibTableColumn
gencommP167Reg_102_103 = _GencommP167Reg_102_103_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 53),
    _GencommP167Reg_102_103_Type()
)
gencommP167Reg_102_103.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_102_103.setStatus("current")
_GencommP167Reg_104_105_Type = Unsigned32
_GencommP167Reg_104_105_Object = MibTableColumn
gencommP167Reg_104_105 = _GencommP167Reg_104_105_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 54),
    _GencommP167Reg_104_105_Type()
)
gencommP167Reg_104_105.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_104_105.setStatus("current")
_GencommP167Reg_106_107_Type = Unsigned32
_GencommP167Reg_106_107_Object = MibTableColumn
gencommP167Reg_106_107 = _GencommP167Reg_106_107_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 55),
    _GencommP167Reg_106_107_Type()
)
gencommP167Reg_106_107.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_106_107.setStatus("current")
_GencommP167Reg_108_109_Type = Unsigned32
_GencommP167Reg_108_109_Object = MibTableColumn
gencommP167Reg_108_109 = _GencommP167Reg_108_109_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 56),
    _GencommP167Reg_108_109_Type()
)
gencommP167Reg_108_109.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_108_109.setStatus("current")
_GencommP167Reg_110_111_Type = Unsigned32
_GencommP167Reg_110_111_Object = MibTableColumn
gencommP167Reg_110_111 = _GencommP167Reg_110_111_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 57),
    _GencommP167Reg_110_111_Type()
)
gencommP167Reg_110_111.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_110_111.setStatus("current")
_GencommP167Reg_112_113_Type = Unsigned32
_GencommP167Reg_112_113_Object = MibTableColumn
gencommP167Reg_112_113 = _GencommP167Reg_112_113_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 58),
    _GencommP167Reg_112_113_Type()
)
gencommP167Reg_112_113.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_112_113.setStatus("current")
_GencommP167Reg_114_115_Type = Unsigned32
_GencommP167Reg_114_115_Object = MibTableColumn
gencommP167Reg_114_115 = _GencommP167Reg_114_115_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 59),
    _GencommP167Reg_114_115_Type()
)
gencommP167Reg_114_115.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_114_115.setStatus("current")
_GencommP167Reg_116_117_Type = Unsigned32
_GencommP167Reg_116_117_Object = MibTableColumn
gencommP167Reg_116_117 = _GencommP167Reg_116_117_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 60),
    _GencommP167Reg_116_117_Type()
)
gencommP167Reg_116_117.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_116_117.setStatus("current")
_GencommP167Reg_118_119_Type = Unsigned32
_GencommP167Reg_118_119_Object = MibTableColumn
gencommP167Reg_118_119 = _GencommP167Reg_118_119_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 61),
    _GencommP167Reg_118_119_Type()
)
gencommP167Reg_118_119.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_118_119.setStatus("current")
_GencommP167Reg_120_121_Type = Unsigned32
_GencommP167Reg_120_121_Object = MibTableColumn
gencommP167Reg_120_121 = _GencommP167Reg_120_121_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 62),
    _GencommP167Reg_120_121_Type()
)
gencommP167Reg_120_121.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_120_121.setStatus("current")
_GencommP167Reg_122_123_Type = Unsigned32
_GencommP167Reg_122_123_Object = MibTableColumn
gencommP167Reg_122_123 = _GencommP167Reg_122_123_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 63),
    _GencommP167Reg_122_123_Type()
)
gencommP167Reg_122_123.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_122_123.setStatus("current")
_GencommP167Reg_124_125_Type = Unsigned32
_GencommP167Reg_124_125_Object = MibTableColumn
gencommP167Reg_124_125 = _GencommP167Reg_124_125_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 64),
    _GencommP167Reg_124_125_Type()
)
gencommP167Reg_124_125.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_124_125.setStatus("current")
_GencommP167Reg_126_127_Type = Unsigned32
_GencommP167Reg_126_127_Object = MibTableColumn
gencommP167Reg_126_127 = _GencommP167Reg_126_127_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 65),
    _GencommP167Reg_126_127_Type()
)
gencommP167Reg_126_127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_126_127.setStatus("current")
_GencommP167Reg_128_129_Type = Unsigned32
_GencommP167Reg_128_129_Object = MibTableColumn
gencommP167Reg_128_129 = _GencommP167Reg_128_129_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 66),
    _GencommP167Reg_128_129_Type()
)
gencommP167Reg_128_129.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_128_129.setStatus("current")
_GencommP167Reg_130_131_Type = Unsigned32
_GencommP167Reg_130_131_Object = MibTableColumn
gencommP167Reg_130_131 = _GencommP167Reg_130_131_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 67),
    _GencommP167Reg_130_131_Type()
)
gencommP167Reg_130_131.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_130_131.setStatus("current")
_GencommP167Reg_132_133_Type = Unsigned32
_GencommP167Reg_132_133_Object = MibTableColumn
gencommP167Reg_132_133 = _GencommP167Reg_132_133_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 68),
    _GencommP167Reg_132_133_Type()
)
gencommP167Reg_132_133.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_132_133.setStatus("current")
_GencommP167Reg_134_135_Type = Unsigned32
_GencommP167Reg_134_135_Object = MibTableColumn
gencommP167Reg_134_135 = _GencommP167Reg_134_135_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 69),
    _GencommP167Reg_134_135_Type()
)
gencommP167Reg_134_135.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_134_135.setStatus("current")
_GencommP167Reg_136_137_Type = Unsigned32
_GencommP167Reg_136_137_Object = MibTableColumn
gencommP167Reg_136_137 = _GencommP167Reg_136_137_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 70),
    _GencommP167Reg_136_137_Type()
)
gencommP167Reg_136_137.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_136_137.setStatus("current")
_GencommP167Reg_138_139_Type = Unsigned32
_GencommP167Reg_138_139_Object = MibTableColumn
gencommP167Reg_138_139 = _GencommP167Reg_138_139_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 71),
    _GencommP167Reg_138_139_Type()
)
gencommP167Reg_138_139.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_138_139.setStatus("current")
_GencommP167Reg_140_141_Type = Unsigned32
_GencommP167Reg_140_141_Object = MibTableColumn
gencommP167Reg_140_141 = _GencommP167Reg_140_141_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 72),
    _GencommP167Reg_140_141_Type()
)
gencommP167Reg_140_141.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_140_141.setStatus("current")
_GencommP167Reg_142_143_Type = Unsigned32
_GencommP167Reg_142_143_Object = MibTableColumn
gencommP167Reg_142_143 = _GencommP167Reg_142_143_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 73),
    _GencommP167Reg_142_143_Type()
)
gencommP167Reg_142_143.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_142_143.setStatus("current")
_GencommP167Reg_144_145_Type = Unsigned32
_GencommP167Reg_144_145_Object = MibTableColumn
gencommP167Reg_144_145 = _GencommP167Reg_144_145_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 74),
    _GencommP167Reg_144_145_Type()
)
gencommP167Reg_144_145.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_144_145.setStatus("current")
_GencommP167Reg_146_147_Type = Unsigned32
_GencommP167Reg_146_147_Object = MibTableColumn
gencommP167Reg_146_147 = _GencommP167Reg_146_147_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 75),
    _GencommP167Reg_146_147_Type()
)
gencommP167Reg_146_147.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_146_147.setStatus("current")
_GencommP167Reg_148_149_Type = Unsigned32
_GencommP167Reg_148_149_Object = MibTableColumn
gencommP167Reg_148_149 = _GencommP167Reg_148_149_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 76),
    _GencommP167Reg_148_149_Type()
)
gencommP167Reg_148_149.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_148_149.setStatus("current")
_GencommP167Reg_150_151_Type = Unsigned32
_GencommP167Reg_150_151_Object = MibTableColumn
gencommP167Reg_150_151 = _GencommP167Reg_150_151_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 77),
    _GencommP167Reg_150_151_Type()
)
gencommP167Reg_150_151.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_150_151.setStatus("current")
_GencommP167Reg_152_153_Type = Unsigned32
_GencommP167Reg_152_153_Object = MibTableColumn
gencommP167Reg_152_153 = _GencommP167Reg_152_153_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 78),
    _GencommP167Reg_152_153_Type()
)
gencommP167Reg_152_153.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_152_153.setStatus("current")
_GencommP167Reg_154_155_Type = Unsigned32
_GencommP167Reg_154_155_Object = MibTableColumn
gencommP167Reg_154_155 = _GencommP167Reg_154_155_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 79),
    _GencommP167Reg_154_155_Type()
)
gencommP167Reg_154_155.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_154_155.setStatus("current")
_GencommP167Reg_156_157_Type = Unsigned32
_GencommP167Reg_156_157_Object = MibTableColumn
gencommP167Reg_156_157 = _GencommP167Reg_156_157_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 80),
    _GencommP167Reg_156_157_Type()
)
gencommP167Reg_156_157.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_156_157.setStatus("current")
_GencommP167Reg_158_159_Type = Unsigned32
_GencommP167Reg_158_159_Object = MibTableColumn
gencommP167Reg_158_159 = _GencommP167Reg_158_159_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 81),
    _GencommP167Reg_158_159_Type()
)
gencommP167Reg_158_159.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_158_159.setStatus("current")
_GencommP167Reg_160_161_Type = Unsigned32
_GencommP167Reg_160_161_Object = MibTableColumn
gencommP167Reg_160_161 = _GencommP167Reg_160_161_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 82),
    _GencommP167Reg_160_161_Type()
)
gencommP167Reg_160_161.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_160_161.setStatus("current")
_GencommP167Reg_162_163_Type = Unsigned32
_GencommP167Reg_162_163_Object = MibTableColumn
gencommP167Reg_162_163 = _GencommP167Reg_162_163_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 83),
    _GencommP167Reg_162_163_Type()
)
gencommP167Reg_162_163.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_162_163.setStatus("current")
_GencommP167Reg_164_165_Type = Unsigned32
_GencommP167Reg_164_165_Object = MibTableColumn
gencommP167Reg_164_165 = _GencommP167Reg_164_165_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 84),
    _GencommP167Reg_164_165_Type()
)
gencommP167Reg_164_165.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_164_165.setStatus("current")
_GencommP167Reg_166_167_Type = Unsigned32
_GencommP167Reg_166_167_Object = MibTableColumn
gencommP167Reg_166_167 = _GencommP167Reg_166_167_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 85),
    _GencommP167Reg_166_167_Type()
)
gencommP167Reg_166_167.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_166_167.setStatus("current")
_GencommP167Reg_168_169_Type = Unsigned32
_GencommP167Reg_168_169_Object = MibTableColumn
gencommP167Reg_168_169 = _GencommP167Reg_168_169_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 86),
    _GencommP167Reg_168_169_Type()
)
gencommP167Reg_168_169.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_168_169.setStatus("current")
_GencommP167Reg_170_171_Type = Unsigned32
_GencommP167Reg_170_171_Object = MibTableColumn
gencommP167Reg_170_171 = _GencommP167Reg_170_171_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 87),
    _GencommP167Reg_170_171_Type()
)
gencommP167Reg_170_171.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_170_171.setStatus("current")
_GencommP167Reg_172_173_Type = Unsigned32
_GencommP167Reg_172_173_Object = MibTableColumn
gencommP167Reg_172_173 = _GencommP167Reg_172_173_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 88),
    _GencommP167Reg_172_173_Type()
)
gencommP167Reg_172_173.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_172_173.setStatus("current")
_GencommP167Reg_174_175_Type = Unsigned32
_GencommP167Reg_174_175_Object = MibTableColumn
gencommP167Reg_174_175 = _GencommP167Reg_174_175_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 89),
    _GencommP167Reg_174_175_Type()
)
gencommP167Reg_174_175.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_174_175.setStatus("current")
_GencommP167Reg_176_177_Type = Unsigned32
_GencommP167Reg_176_177_Object = MibTableColumn
gencommP167Reg_176_177 = _GencommP167Reg_176_177_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 90),
    _GencommP167Reg_176_177_Type()
)
gencommP167Reg_176_177.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_176_177.setStatus("current")
_GencommP167Reg_178_179_Type = Unsigned32
_GencommP167Reg_178_179_Object = MibTableColumn
gencommP167Reg_178_179 = _GencommP167Reg_178_179_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 91),
    _GencommP167Reg_178_179_Type()
)
gencommP167Reg_178_179.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_178_179.setStatus("current")
_GencommP167Reg_180_181_Type = Unsigned32
_GencommP167Reg_180_181_Object = MibTableColumn
gencommP167Reg_180_181 = _GencommP167Reg_180_181_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 92),
    _GencommP167Reg_180_181_Type()
)
gencommP167Reg_180_181.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_180_181.setStatus("current")
_GencommP167Reg_182_183_Type = Unsigned32
_GencommP167Reg_182_183_Object = MibTableColumn
gencommP167Reg_182_183 = _GencommP167Reg_182_183_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 93),
    _GencommP167Reg_182_183_Type()
)
gencommP167Reg_182_183.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_182_183.setStatus("current")
_GencommP167Reg_184_185_Type = Unsigned32
_GencommP167Reg_184_185_Object = MibTableColumn
gencommP167Reg_184_185 = _GencommP167Reg_184_185_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 94),
    _GencommP167Reg_184_185_Type()
)
gencommP167Reg_184_185.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_184_185.setStatus("current")
_GencommP167Reg_186_187_Type = Unsigned32
_GencommP167Reg_186_187_Object = MibTableColumn
gencommP167Reg_186_187 = _GencommP167Reg_186_187_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 95),
    _GencommP167Reg_186_187_Type()
)
gencommP167Reg_186_187.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_186_187.setStatus("current")
_GencommP167Reg_188_189_Type = Unsigned32
_GencommP167Reg_188_189_Object = MibTableColumn
gencommP167Reg_188_189 = _GencommP167Reg_188_189_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 96),
    _GencommP167Reg_188_189_Type()
)
gencommP167Reg_188_189.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_188_189.setStatus("current")
_GencommP167Reg_190_191_Type = Unsigned32
_GencommP167Reg_190_191_Object = MibTableColumn
gencommP167Reg_190_191 = _GencommP167Reg_190_191_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 97),
    _GencommP167Reg_190_191_Type()
)
gencommP167Reg_190_191.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_190_191.setStatus("current")
_GencommP167Reg_192_193_Type = Unsigned32
_GencommP167Reg_192_193_Object = MibTableColumn
gencommP167Reg_192_193 = _GencommP167Reg_192_193_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 98),
    _GencommP167Reg_192_193_Type()
)
gencommP167Reg_192_193.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_192_193.setStatus("current")
_GencommP167Reg_194_195_Type = Unsigned32
_GencommP167Reg_194_195_Object = MibTableColumn
gencommP167Reg_194_195 = _GencommP167Reg_194_195_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 99),
    _GencommP167Reg_194_195_Type()
)
gencommP167Reg_194_195.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_194_195.setStatus("current")
_GencommP167Reg_196_197_Type = Unsigned32
_GencommP167Reg_196_197_Object = MibTableColumn
gencommP167Reg_196_197 = _GencommP167Reg_196_197_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 100),
    _GencommP167Reg_196_197_Type()
)
gencommP167Reg_196_197.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_196_197.setStatus("current")
_GencommP167Reg_198_199_Type = Unsigned32
_GencommP167Reg_198_199_Object = MibTableColumn
gencommP167Reg_198_199 = _GencommP167Reg_198_199_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 101),
    _GencommP167Reg_198_199_Type()
)
gencommP167Reg_198_199.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_198_199.setStatus("current")
_GencommP167Reg_200_201_Type = Unsigned32
_GencommP167Reg_200_201_Object = MibTableColumn
gencommP167Reg_200_201 = _GencommP167Reg_200_201_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 102),
    _GencommP167Reg_200_201_Type()
)
gencommP167Reg_200_201.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_200_201.setStatus("current")
_GencommP167Reg_202_203_Type = Unsigned32
_GencommP167Reg_202_203_Object = MibTableColumn
gencommP167Reg_202_203 = _GencommP167Reg_202_203_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 103),
    _GencommP167Reg_202_203_Type()
)
gencommP167Reg_202_203.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_202_203.setStatus("current")
_GencommP167Reg_204_205_Type = Unsigned32
_GencommP167Reg_204_205_Object = MibTableColumn
gencommP167Reg_204_205 = _GencommP167Reg_204_205_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 104),
    _GencommP167Reg_204_205_Type()
)
gencommP167Reg_204_205.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_204_205.setStatus("current")
_GencommP167Reg_206_207_Type = Unsigned32
_GencommP167Reg_206_207_Object = MibTableColumn
gencommP167Reg_206_207 = _GencommP167Reg_206_207_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 105),
    _GencommP167Reg_206_207_Type()
)
gencommP167Reg_206_207.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_206_207.setStatus("current")
_GencommP167Reg_208_209_Type = Unsigned32
_GencommP167Reg_208_209_Object = MibTableColumn
gencommP167Reg_208_209 = _GencommP167Reg_208_209_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 106),
    _GencommP167Reg_208_209_Type()
)
gencommP167Reg_208_209.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_208_209.setStatus("current")
_GencommP167Reg_210_211_Type = Unsigned32
_GencommP167Reg_210_211_Object = MibTableColumn
gencommP167Reg_210_211 = _GencommP167Reg_210_211_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 107),
    _GencommP167Reg_210_211_Type()
)
gencommP167Reg_210_211.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_210_211.setStatus("current")
_GencommP167Reg_212_213_Type = Unsigned32
_GencommP167Reg_212_213_Object = MibTableColumn
gencommP167Reg_212_213 = _GencommP167Reg_212_213_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 108),
    _GencommP167Reg_212_213_Type()
)
gencommP167Reg_212_213.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_212_213.setStatus("current")
_GencommP167Reg_214_215_Type = Unsigned32
_GencommP167Reg_214_215_Object = MibTableColumn
gencommP167Reg_214_215 = _GencommP167Reg_214_215_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 109),
    _GencommP167Reg_214_215_Type()
)
gencommP167Reg_214_215.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_214_215.setStatus("current")
_GencommP167Reg_216_217_Type = Unsigned32
_GencommP167Reg_216_217_Object = MibTableColumn
gencommP167Reg_216_217 = _GencommP167Reg_216_217_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 110),
    _GencommP167Reg_216_217_Type()
)
gencommP167Reg_216_217.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_216_217.setStatus("current")
_GencommP167Reg_218_219_Type = Unsigned32
_GencommP167Reg_218_219_Object = MibTableColumn
gencommP167Reg_218_219 = _GencommP167Reg_218_219_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 111),
    _GencommP167Reg_218_219_Type()
)
gencommP167Reg_218_219.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_218_219.setStatus("current")
_GencommP167Reg_220_221_Type = Unsigned32
_GencommP167Reg_220_221_Object = MibTableColumn
gencommP167Reg_220_221 = _GencommP167Reg_220_221_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 112),
    _GencommP167Reg_220_221_Type()
)
gencommP167Reg_220_221.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_220_221.setStatus("current")
_GencommP167Reg_222_223_Type = Unsigned32
_GencommP167Reg_222_223_Object = MibTableColumn
gencommP167Reg_222_223 = _GencommP167Reg_222_223_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 113),
    _GencommP167Reg_222_223_Type()
)
gencommP167Reg_222_223.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_222_223.setStatus("current")
_GencommP167Reg_224_225_Type = Unsigned32
_GencommP167Reg_224_225_Object = MibTableColumn
gencommP167Reg_224_225 = _GencommP167Reg_224_225_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 114),
    _GencommP167Reg_224_225_Type()
)
gencommP167Reg_224_225.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_224_225.setStatus("current")
_GencommP167Reg_226_227_Type = Unsigned32
_GencommP167Reg_226_227_Object = MibTableColumn
gencommP167Reg_226_227 = _GencommP167Reg_226_227_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 115),
    _GencommP167Reg_226_227_Type()
)
gencommP167Reg_226_227.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_226_227.setStatus("current")
_GencommP167Reg_228_229_Type = Unsigned32
_GencommP167Reg_228_229_Object = MibTableColumn
gencommP167Reg_228_229 = _GencommP167Reg_228_229_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 116),
    _GencommP167Reg_228_229_Type()
)
gencommP167Reg_228_229.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_228_229.setStatus("current")
_GencommP167Reg_230_231_Type = Unsigned32
_GencommP167Reg_230_231_Object = MibTableColumn
gencommP167Reg_230_231 = _GencommP167Reg_230_231_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 117),
    _GencommP167Reg_230_231_Type()
)
gencommP167Reg_230_231.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_230_231.setStatus("current")
_GencommP167Reg_232_233_Type = Unsigned32
_GencommP167Reg_232_233_Object = MibTableColumn
gencommP167Reg_232_233 = _GencommP167Reg_232_233_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 118),
    _GencommP167Reg_232_233_Type()
)
gencommP167Reg_232_233.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_232_233.setStatus("current")
_GencommP167Reg_234_235_Type = Unsigned32
_GencommP167Reg_234_235_Object = MibTableColumn
gencommP167Reg_234_235 = _GencommP167Reg_234_235_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 119),
    _GencommP167Reg_234_235_Type()
)
gencommP167Reg_234_235.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_234_235.setStatus("current")
_GencommP167Reg_236_237_Type = Unsigned32
_GencommP167Reg_236_237_Object = MibTableColumn
gencommP167Reg_236_237 = _GencommP167Reg_236_237_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 120),
    _GencommP167Reg_236_237_Type()
)
gencommP167Reg_236_237.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_236_237.setStatus("current")
_GencommP167Reg_238_239_Type = Unsigned32
_GencommP167Reg_238_239_Object = MibTableColumn
gencommP167Reg_238_239 = _GencommP167Reg_238_239_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 121),
    _GencommP167Reg_238_239_Type()
)
gencommP167Reg_238_239.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_238_239.setStatus("current")
_GencommP167Reg_240_241_Type = Unsigned32
_GencommP167Reg_240_241_Object = MibTableColumn
gencommP167Reg_240_241 = _GencommP167Reg_240_241_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 122),
    _GencommP167Reg_240_241_Type()
)
gencommP167Reg_240_241.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_240_241.setStatus("current")
_GencommP167Reg_242_243_Type = Unsigned32
_GencommP167Reg_242_243_Object = MibTableColumn
gencommP167Reg_242_243 = _GencommP167Reg_242_243_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 123),
    _GencommP167Reg_242_243_Type()
)
gencommP167Reg_242_243.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_242_243.setStatus("current")
_GencommP167Reg_244_245_Type = Unsigned32
_GencommP167Reg_244_245_Object = MibTableColumn
gencommP167Reg_244_245 = _GencommP167Reg_244_245_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 124),
    _GencommP167Reg_244_245_Type()
)
gencommP167Reg_244_245.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_244_245.setStatus("current")
_GencommP167Reg_246_247_Type = Unsigned32
_GencommP167Reg_246_247_Object = MibTableColumn
gencommP167Reg_246_247 = _GencommP167Reg_246_247_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 125),
    _GencommP167Reg_246_247_Type()
)
gencommP167Reg_246_247.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_246_247.setStatus("current")
_GencommP167Reg_248_249_Type = Unsigned32
_GencommP167Reg_248_249_Object = MibTableColumn
gencommP167Reg_248_249 = _GencommP167Reg_248_249_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 126),
    _GencommP167Reg_248_249_Type()
)
gencommP167Reg_248_249.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_248_249.setStatus("current")
_GencommP167Reg_250_251_Type = Unsigned32
_GencommP167Reg_250_251_Object = MibTableColumn
gencommP167Reg_250_251 = _GencommP167Reg_250_251_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 127),
    _GencommP167Reg_250_251_Type()
)
gencommP167Reg_250_251.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_250_251.setStatus("current")
_GencommP167Reg_252_253_Type = Unsigned32
_GencommP167Reg_252_253_Object = MibTableColumn
gencommP167Reg_252_253 = _GencommP167Reg_252_253_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 128),
    _GencommP167Reg_252_253_Type()
)
gencommP167Reg_252_253.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_252_253.setStatus("current")
_GencommP167Reg_254_255_Type = Unsigned32
_GencommP167Reg_254_255_Object = MibTableColumn
gencommP167Reg_254_255 = _GencommP167Reg_254_255_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 2, 1, 129),
    _GencommP167Reg_254_255_Type()
)
gencommP167Reg_254_255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP167Reg_254_255.setStatus("current")
_GencommP168Table_Object = MibTable
gencommP168Table = _GencommP168Table_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3)
)
if mibBuilder.loadTexts:
    gencommP168Table.setStatus("current")
_GencommP168Entry_Object = MibTableRow
gencommP168Entry = _GencommP168Entry_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1)
)
gencommP168Entry.setIndexNames(
    (0, "DSE-8610-MIB", "gencommP168KeyID"),
)
if mibBuilder.loadTexts:
    gencommP168Entry.setStatus("current")


class _GencommP168KeyID_Type(Integer32):
    """Custom type gencommP168KeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GencommP168KeyID_Type.__name__ = "Integer32"
_GencommP168KeyID_Object = MibTableColumn
gencommP168KeyID = _GencommP168KeyID_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 1),
    _GencommP168KeyID_Type()
)
gencommP168KeyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gencommP168KeyID.setStatus("current")
_GencommP168Reg_0_1_Type = Unsigned32
_GencommP168Reg_0_1_Object = MibTableColumn
gencommP168Reg_0_1 = _GencommP168Reg_0_1_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 2),
    _GencommP168Reg_0_1_Type()
)
gencommP168Reg_0_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_0_1.setStatus("current")
_GencommP168Reg_2_3_Type = Unsigned32
_GencommP168Reg_2_3_Object = MibTableColumn
gencommP168Reg_2_3 = _GencommP168Reg_2_3_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 3),
    _GencommP168Reg_2_3_Type()
)
gencommP168Reg_2_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_2_3.setStatus("current")
_GencommP168Reg_4_5_Type = Unsigned32
_GencommP168Reg_4_5_Object = MibTableColumn
gencommP168Reg_4_5 = _GencommP168Reg_4_5_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 4),
    _GencommP168Reg_4_5_Type()
)
gencommP168Reg_4_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_4_5.setStatus("current")
_GencommP168Reg_6_7_Type = Unsigned32
_GencommP168Reg_6_7_Object = MibTableColumn
gencommP168Reg_6_7 = _GencommP168Reg_6_7_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 5),
    _GencommP168Reg_6_7_Type()
)
gencommP168Reg_6_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_6_7.setStatus("current")
_GencommP168Reg_8_9_Type = Unsigned32
_GencommP168Reg_8_9_Object = MibTableColumn
gencommP168Reg_8_9 = _GencommP168Reg_8_9_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 6),
    _GencommP168Reg_8_9_Type()
)
gencommP168Reg_8_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_8_9.setStatus("current")
_GencommP168Reg_10_11_Type = Unsigned32
_GencommP168Reg_10_11_Object = MibTableColumn
gencommP168Reg_10_11 = _GencommP168Reg_10_11_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 7),
    _GencommP168Reg_10_11_Type()
)
gencommP168Reg_10_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_10_11.setStatus("current")
_GencommP168Reg_12_13_Type = Unsigned32
_GencommP168Reg_12_13_Object = MibTableColumn
gencommP168Reg_12_13 = _GencommP168Reg_12_13_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 8),
    _GencommP168Reg_12_13_Type()
)
gencommP168Reg_12_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_12_13.setStatus("current")
_GencommP168Reg_14_15_Type = Unsigned32
_GencommP168Reg_14_15_Object = MibTableColumn
gencommP168Reg_14_15 = _GencommP168Reg_14_15_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 9),
    _GencommP168Reg_14_15_Type()
)
gencommP168Reg_14_15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_14_15.setStatus("current")
_GencommP168Reg_16_17_Type = Unsigned32
_GencommP168Reg_16_17_Object = MibTableColumn
gencommP168Reg_16_17 = _GencommP168Reg_16_17_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 10),
    _GencommP168Reg_16_17_Type()
)
gencommP168Reg_16_17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_16_17.setStatus("current")
_GencommP168Reg_18_19_Type = Unsigned32
_GencommP168Reg_18_19_Object = MibTableColumn
gencommP168Reg_18_19 = _GencommP168Reg_18_19_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 11),
    _GencommP168Reg_18_19_Type()
)
gencommP168Reg_18_19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_18_19.setStatus("current")
_GencommP168Reg_20_21_Type = Unsigned32
_GencommP168Reg_20_21_Object = MibTableColumn
gencommP168Reg_20_21 = _GencommP168Reg_20_21_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 12),
    _GencommP168Reg_20_21_Type()
)
gencommP168Reg_20_21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_20_21.setStatus("current")
_GencommP168Reg_22_23_Type = Unsigned32
_GencommP168Reg_22_23_Object = MibTableColumn
gencommP168Reg_22_23 = _GencommP168Reg_22_23_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 13),
    _GencommP168Reg_22_23_Type()
)
gencommP168Reg_22_23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_22_23.setStatus("current")
_GencommP168Reg_24_25_Type = Unsigned32
_GencommP168Reg_24_25_Object = MibTableColumn
gencommP168Reg_24_25 = _GencommP168Reg_24_25_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 14),
    _GencommP168Reg_24_25_Type()
)
gencommP168Reg_24_25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_24_25.setStatus("current")
_GencommP168Reg_26_27_Type = Unsigned32
_GencommP168Reg_26_27_Object = MibTableColumn
gencommP168Reg_26_27 = _GencommP168Reg_26_27_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 15),
    _GencommP168Reg_26_27_Type()
)
gencommP168Reg_26_27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_26_27.setStatus("current")
_GencommP168Reg_28_29_Type = Unsigned32
_GencommP168Reg_28_29_Object = MibTableColumn
gencommP168Reg_28_29 = _GencommP168Reg_28_29_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 16),
    _GencommP168Reg_28_29_Type()
)
gencommP168Reg_28_29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_28_29.setStatus("current")
_GencommP168Reg_30_31_Type = Unsigned32
_GencommP168Reg_30_31_Object = MibTableColumn
gencommP168Reg_30_31 = _GencommP168Reg_30_31_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 17),
    _GencommP168Reg_30_31_Type()
)
gencommP168Reg_30_31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_30_31.setStatus("current")
_GencommP168Reg_32_33_Type = Unsigned32
_GencommP168Reg_32_33_Object = MibTableColumn
gencommP168Reg_32_33 = _GencommP168Reg_32_33_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 18),
    _GencommP168Reg_32_33_Type()
)
gencommP168Reg_32_33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_32_33.setStatus("current")
_GencommP168Reg_34_35_Type = Unsigned32
_GencommP168Reg_34_35_Object = MibTableColumn
gencommP168Reg_34_35 = _GencommP168Reg_34_35_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 19),
    _GencommP168Reg_34_35_Type()
)
gencommP168Reg_34_35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_34_35.setStatus("current")
_GencommP168Reg_36_37_Type = Unsigned32
_GencommP168Reg_36_37_Object = MibTableColumn
gencommP168Reg_36_37 = _GencommP168Reg_36_37_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 20),
    _GencommP168Reg_36_37_Type()
)
gencommP168Reg_36_37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_36_37.setStatus("current")
_GencommP168Reg_38_39_Type = Unsigned32
_GencommP168Reg_38_39_Object = MibTableColumn
gencommP168Reg_38_39 = _GencommP168Reg_38_39_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 21),
    _GencommP168Reg_38_39_Type()
)
gencommP168Reg_38_39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_38_39.setStatus("current")
_GencommP168Reg_40_41_Type = Unsigned32
_GencommP168Reg_40_41_Object = MibTableColumn
gencommP168Reg_40_41 = _GencommP168Reg_40_41_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 22),
    _GencommP168Reg_40_41_Type()
)
gencommP168Reg_40_41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_40_41.setStatus("current")
_GencommP168Reg_42_43_Type = Unsigned32
_GencommP168Reg_42_43_Object = MibTableColumn
gencommP168Reg_42_43 = _GencommP168Reg_42_43_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 23),
    _GencommP168Reg_42_43_Type()
)
gencommP168Reg_42_43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_42_43.setStatus("current")
_GencommP168Reg_44_45_Type = Unsigned32
_GencommP168Reg_44_45_Object = MibTableColumn
gencommP168Reg_44_45 = _GencommP168Reg_44_45_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 24),
    _GencommP168Reg_44_45_Type()
)
gencommP168Reg_44_45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_44_45.setStatus("current")
_GencommP168Reg_46_47_Type = Unsigned32
_GencommP168Reg_46_47_Object = MibTableColumn
gencommP168Reg_46_47 = _GencommP168Reg_46_47_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 25),
    _GencommP168Reg_46_47_Type()
)
gencommP168Reg_46_47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_46_47.setStatus("current")
_GencommP168Reg_48_49_Type = Unsigned32
_GencommP168Reg_48_49_Object = MibTableColumn
gencommP168Reg_48_49 = _GencommP168Reg_48_49_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 26),
    _GencommP168Reg_48_49_Type()
)
gencommP168Reg_48_49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_48_49.setStatus("current")
_GencommP168Reg_50_51_Type = Unsigned32
_GencommP168Reg_50_51_Object = MibTableColumn
gencommP168Reg_50_51 = _GencommP168Reg_50_51_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 27),
    _GencommP168Reg_50_51_Type()
)
gencommP168Reg_50_51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_50_51.setStatus("current")
_GencommP168Reg_52_53_Type = Unsigned32
_GencommP168Reg_52_53_Object = MibTableColumn
gencommP168Reg_52_53 = _GencommP168Reg_52_53_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 28),
    _GencommP168Reg_52_53_Type()
)
gencommP168Reg_52_53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_52_53.setStatus("current")
_GencommP168Reg_54_55_Type = Unsigned32
_GencommP168Reg_54_55_Object = MibTableColumn
gencommP168Reg_54_55 = _GencommP168Reg_54_55_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 29),
    _GencommP168Reg_54_55_Type()
)
gencommP168Reg_54_55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_54_55.setStatus("current")
_GencommP168Reg_56_57_Type = Unsigned32
_GencommP168Reg_56_57_Object = MibTableColumn
gencommP168Reg_56_57 = _GencommP168Reg_56_57_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 30),
    _GencommP168Reg_56_57_Type()
)
gencommP168Reg_56_57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_56_57.setStatus("current")
_GencommP168Reg_58_59_Type = Unsigned32
_GencommP168Reg_58_59_Object = MibTableColumn
gencommP168Reg_58_59 = _GencommP168Reg_58_59_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 31),
    _GencommP168Reg_58_59_Type()
)
gencommP168Reg_58_59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_58_59.setStatus("current")
_GencommP168Reg_60_61_Type = Unsigned32
_GencommP168Reg_60_61_Object = MibTableColumn
gencommP168Reg_60_61 = _GencommP168Reg_60_61_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 32),
    _GencommP168Reg_60_61_Type()
)
gencommP168Reg_60_61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_60_61.setStatus("current")
_GencommP168Reg_62_63_Type = Unsigned32
_GencommP168Reg_62_63_Object = MibTableColumn
gencommP168Reg_62_63 = _GencommP168Reg_62_63_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 33),
    _GencommP168Reg_62_63_Type()
)
gencommP168Reg_62_63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_62_63.setStatus("current")
_GencommP168Reg_64_65_Type = Unsigned32
_GencommP168Reg_64_65_Object = MibTableColumn
gencommP168Reg_64_65 = _GencommP168Reg_64_65_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 34),
    _GencommP168Reg_64_65_Type()
)
gencommP168Reg_64_65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_64_65.setStatus("current")
_GencommP168Reg_66_67_Type = Unsigned32
_GencommP168Reg_66_67_Object = MibTableColumn
gencommP168Reg_66_67 = _GencommP168Reg_66_67_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 35),
    _GencommP168Reg_66_67_Type()
)
gencommP168Reg_66_67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_66_67.setStatus("current")
_GencommP168Reg_68_69_Type = Unsigned32
_GencommP168Reg_68_69_Object = MibTableColumn
gencommP168Reg_68_69 = _GencommP168Reg_68_69_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 36),
    _GencommP168Reg_68_69_Type()
)
gencommP168Reg_68_69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_68_69.setStatus("current")
_GencommP168Reg_70_71_Type = Unsigned32
_GencommP168Reg_70_71_Object = MibTableColumn
gencommP168Reg_70_71 = _GencommP168Reg_70_71_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 37),
    _GencommP168Reg_70_71_Type()
)
gencommP168Reg_70_71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_70_71.setStatus("current")
_GencommP168Reg_72_73_Type = Unsigned32
_GencommP168Reg_72_73_Object = MibTableColumn
gencommP168Reg_72_73 = _GencommP168Reg_72_73_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 38),
    _GencommP168Reg_72_73_Type()
)
gencommP168Reg_72_73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_72_73.setStatus("current")
_GencommP168Reg_74_75_Type = Unsigned32
_GencommP168Reg_74_75_Object = MibTableColumn
gencommP168Reg_74_75 = _GencommP168Reg_74_75_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 39),
    _GencommP168Reg_74_75_Type()
)
gencommP168Reg_74_75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_74_75.setStatus("current")
_GencommP168Reg_76_77_Type = Unsigned32
_GencommP168Reg_76_77_Object = MibTableColumn
gencommP168Reg_76_77 = _GencommP168Reg_76_77_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 40),
    _GencommP168Reg_76_77_Type()
)
gencommP168Reg_76_77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_76_77.setStatus("current")
_GencommP168Reg_78_79_Type = Unsigned32
_GencommP168Reg_78_79_Object = MibTableColumn
gencommP168Reg_78_79 = _GencommP168Reg_78_79_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 41),
    _GencommP168Reg_78_79_Type()
)
gencommP168Reg_78_79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_78_79.setStatus("current")
_GencommP168Reg_80_81_Type = Unsigned32
_GencommP168Reg_80_81_Object = MibTableColumn
gencommP168Reg_80_81 = _GencommP168Reg_80_81_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 42),
    _GencommP168Reg_80_81_Type()
)
gencommP168Reg_80_81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_80_81.setStatus("current")
_GencommP168Reg_82_83_Type = Unsigned32
_GencommP168Reg_82_83_Object = MibTableColumn
gencommP168Reg_82_83 = _GencommP168Reg_82_83_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 43),
    _GencommP168Reg_82_83_Type()
)
gencommP168Reg_82_83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_82_83.setStatus("current")
_GencommP168Reg_84_85_Type = Unsigned32
_GencommP168Reg_84_85_Object = MibTableColumn
gencommP168Reg_84_85 = _GencommP168Reg_84_85_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 44),
    _GencommP168Reg_84_85_Type()
)
gencommP168Reg_84_85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_84_85.setStatus("current")
_GencommP168Reg_86_87_Type = Unsigned32
_GencommP168Reg_86_87_Object = MibTableColumn
gencommP168Reg_86_87 = _GencommP168Reg_86_87_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 45),
    _GencommP168Reg_86_87_Type()
)
gencommP168Reg_86_87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_86_87.setStatus("current")
_GencommP168Reg_88_89_Type = Unsigned32
_GencommP168Reg_88_89_Object = MibTableColumn
gencommP168Reg_88_89 = _GencommP168Reg_88_89_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 46),
    _GencommP168Reg_88_89_Type()
)
gencommP168Reg_88_89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_88_89.setStatus("current")
_GencommP168Reg_90_91_Type = Unsigned32
_GencommP168Reg_90_91_Object = MibTableColumn
gencommP168Reg_90_91 = _GencommP168Reg_90_91_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 47),
    _GencommP168Reg_90_91_Type()
)
gencommP168Reg_90_91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_90_91.setStatus("current")
_GencommP168Reg_92_93_Type = Unsigned32
_GencommP168Reg_92_93_Object = MibTableColumn
gencommP168Reg_92_93 = _GencommP168Reg_92_93_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 48),
    _GencommP168Reg_92_93_Type()
)
gencommP168Reg_92_93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_92_93.setStatus("current")
_GencommP168Reg_94_95_Type = Unsigned32
_GencommP168Reg_94_95_Object = MibTableColumn
gencommP168Reg_94_95 = _GencommP168Reg_94_95_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 49),
    _GencommP168Reg_94_95_Type()
)
gencommP168Reg_94_95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_94_95.setStatus("current")
_GencommP168Reg_96_97_Type = Unsigned32
_GencommP168Reg_96_97_Object = MibTableColumn
gencommP168Reg_96_97 = _GencommP168Reg_96_97_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 50),
    _GencommP168Reg_96_97_Type()
)
gencommP168Reg_96_97.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_96_97.setStatus("current")
_GencommP168Reg_98_99_Type = Unsigned32
_GencommP168Reg_98_99_Object = MibTableColumn
gencommP168Reg_98_99 = _GencommP168Reg_98_99_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 51),
    _GencommP168Reg_98_99_Type()
)
gencommP168Reg_98_99.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_98_99.setStatus("current")
_GencommP168Reg_100_101_Type = Unsigned32
_GencommP168Reg_100_101_Object = MibTableColumn
gencommP168Reg_100_101 = _GencommP168Reg_100_101_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 52),
    _GencommP168Reg_100_101_Type()
)
gencommP168Reg_100_101.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_100_101.setStatus("current")
_GencommP168Reg_102_103_Type = Unsigned32
_GencommP168Reg_102_103_Object = MibTableColumn
gencommP168Reg_102_103 = _GencommP168Reg_102_103_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 53),
    _GencommP168Reg_102_103_Type()
)
gencommP168Reg_102_103.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_102_103.setStatus("current")
_GencommP168Reg_104_105_Type = Unsigned32
_GencommP168Reg_104_105_Object = MibTableColumn
gencommP168Reg_104_105 = _GencommP168Reg_104_105_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 54),
    _GencommP168Reg_104_105_Type()
)
gencommP168Reg_104_105.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_104_105.setStatus("current")
_GencommP168Reg_106_107_Type = Unsigned32
_GencommP168Reg_106_107_Object = MibTableColumn
gencommP168Reg_106_107 = _GencommP168Reg_106_107_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 55),
    _GencommP168Reg_106_107_Type()
)
gencommP168Reg_106_107.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_106_107.setStatus("current")
_GencommP168Reg_108_109_Type = Unsigned32
_GencommP168Reg_108_109_Object = MibTableColumn
gencommP168Reg_108_109 = _GencommP168Reg_108_109_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 56),
    _GencommP168Reg_108_109_Type()
)
gencommP168Reg_108_109.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_108_109.setStatus("current")
_GencommP168Reg_110_111_Type = Unsigned32
_GencommP168Reg_110_111_Object = MibTableColumn
gencommP168Reg_110_111 = _GencommP168Reg_110_111_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 57),
    _GencommP168Reg_110_111_Type()
)
gencommP168Reg_110_111.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_110_111.setStatus("current")
_GencommP168Reg_112_113_Type = Unsigned32
_GencommP168Reg_112_113_Object = MibTableColumn
gencommP168Reg_112_113 = _GencommP168Reg_112_113_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 58),
    _GencommP168Reg_112_113_Type()
)
gencommP168Reg_112_113.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_112_113.setStatus("current")
_GencommP168Reg_114_115_Type = Unsigned32
_GencommP168Reg_114_115_Object = MibTableColumn
gencommP168Reg_114_115 = _GencommP168Reg_114_115_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 59),
    _GencommP168Reg_114_115_Type()
)
gencommP168Reg_114_115.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_114_115.setStatus("current")
_GencommP168Reg_116_117_Type = Unsigned32
_GencommP168Reg_116_117_Object = MibTableColumn
gencommP168Reg_116_117 = _GencommP168Reg_116_117_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 60),
    _GencommP168Reg_116_117_Type()
)
gencommP168Reg_116_117.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_116_117.setStatus("current")
_GencommP168Reg_118_119_Type = Unsigned32
_GencommP168Reg_118_119_Object = MibTableColumn
gencommP168Reg_118_119 = _GencommP168Reg_118_119_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 61),
    _GencommP168Reg_118_119_Type()
)
gencommP168Reg_118_119.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_118_119.setStatus("current")
_GencommP168Reg_120_121_Type = Unsigned32
_GencommP168Reg_120_121_Object = MibTableColumn
gencommP168Reg_120_121 = _GencommP168Reg_120_121_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 62),
    _GencommP168Reg_120_121_Type()
)
gencommP168Reg_120_121.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_120_121.setStatus("current")
_GencommP168Reg_122_123_Type = Unsigned32
_GencommP168Reg_122_123_Object = MibTableColumn
gencommP168Reg_122_123 = _GencommP168Reg_122_123_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 63),
    _GencommP168Reg_122_123_Type()
)
gencommP168Reg_122_123.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_122_123.setStatus("current")
_GencommP168Reg_124_125_Type = Unsigned32
_GencommP168Reg_124_125_Object = MibTableColumn
gencommP168Reg_124_125 = _GencommP168Reg_124_125_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 64),
    _GencommP168Reg_124_125_Type()
)
gencommP168Reg_124_125.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_124_125.setStatus("current")
_GencommP168Reg_126_127_Type = Unsigned32
_GencommP168Reg_126_127_Object = MibTableColumn
gencommP168Reg_126_127 = _GencommP168Reg_126_127_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 65),
    _GencommP168Reg_126_127_Type()
)
gencommP168Reg_126_127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_126_127.setStatus("current")
_GencommP168Reg_128_129_Type = Unsigned32
_GencommP168Reg_128_129_Object = MibTableColumn
gencommP168Reg_128_129 = _GencommP168Reg_128_129_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 66),
    _GencommP168Reg_128_129_Type()
)
gencommP168Reg_128_129.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_128_129.setStatus("current")
_GencommP168Reg_130_131_Type = Unsigned32
_GencommP168Reg_130_131_Object = MibTableColumn
gencommP168Reg_130_131 = _GencommP168Reg_130_131_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 67),
    _GencommP168Reg_130_131_Type()
)
gencommP168Reg_130_131.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_130_131.setStatus("current")
_GencommP168Reg_132_133_Type = Unsigned32
_GencommP168Reg_132_133_Object = MibTableColumn
gencommP168Reg_132_133 = _GencommP168Reg_132_133_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 68),
    _GencommP168Reg_132_133_Type()
)
gencommP168Reg_132_133.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_132_133.setStatus("current")
_GencommP168Reg_134_135_Type = Unsigned32
_GencommP168Reg_134_135_Object = MibTableColumn
gencommP168Reg_134_135 = _GencommP168Reg_134_135_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 69),
    _GencommP168Reg_134_135_Type()
)
gencommP168Reg_134_135.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_134_135.setStatus("current")
_GencommP168Reg_136_137_Type = Unsigned32
_GencommP168Reg_136_137_Object = MibTableColumn
gencommP168Reg_136_137 = _GencommP168Reg_136_137_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 70),
    _GencommP168Reg_136_137_Type()
)
gencommP168Reg_136_137.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_136_137.setStatus("current")
_GencommP168Reg_138_139_Type = Unsigned32
_GencommP168Reg_138_139_Object = MibTableColumn
gencommP168Reg_138_139 = _GencommP168Reg_138_139_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 71),
    _GencommP168Reg_138_139_Type()
)
gencommP168Reg_138_139.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_138_139.setStatus("current")
_GencommP168Reg_140_141_Type = Unsigned32
_GencommP168Reg_140_141_Object = MibTableColumn
gencommP168Reg_140_141 = _GencommP168Reg_140_141_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 72),
    _GencommP168Reg_140_141_Type()
)
gencommP168Reg_140_141.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_140_141.setStatus("current")
_GencommP168Reg_142_143_Type = Unsigned32
_GencommP168Reg_142_143_Object = MibTableColumn
gencommP168Reg_142_143 = _GencommP168Reg_142_143_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 73),
    _GencommP168Reg_142_143_Type()
)
gencommP168Reg_142_143.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_142_143.setStatus("current")
_GencommP168Reg_144_145_Type = Unsigned32
_GencommP168Reg_144_145_Object = MibTableColumn
gencommP168Reg_144_145 = _GencommP168Reg_144_145_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 74),
    _GencommP168Reg_144_145_Type()
)
gencommP168Reg_144_145.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_144_145.setStatus("current")
_GencommP168Reg_146_147_Type = Unsigned32
_GencommP168Reg_146_147_Object = MibTableColumn
gencommP168Reg_146_147 = _GencommP168Reg_146_147_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 75),
    _GencommP168Reg_146_147_Type()
)
gencommP168Reg_146_147.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_146_147.setStatus("current")
_GencommP168Reg_148_149_Type = Unsigned32
_GencommP168Reg_148_149_Object = MibTableColumn
gencommP168Reg_148_149 = _GencommP168Reg_148_149_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 76),
    _GencommP168Reg_148_149_Type()
)
gencommP168Reg_148_149.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_148_149.setStatus("current")
_GencommP168Reg_150_151_Type = Unsigned32
_GencommP168Reg_150_151_Object = MibTableColumn
gencommP168Reg_150_151 = _GencommP168Reg_150_151_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 77),
    _GencommP168Reg_150_151_Type()
)
gencommP168Reg_150_151.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_150_151.setStatus("current")
_GencommP168Reg_152_153_Type = Unsigned32
_GencommP168Reg_152_153_Object = MibTableColumn
gencommP168Reg_152_153 = _GencommP168Reg_152_153_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 78),
    _GencommP168Reg_152_153_Type()
)
gencommP168Reg_152_153.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_152_153.setStatus("current")
_GencommP168Reg_154_155_Type = Unsigned32
_GencommP168Reg_154_155_Object = MibTableColumn
gencommP168Reg_154_155 = _GencommP168Reg_154_155_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 79),
    _GencommP168Reg_154_155_Type()
)
gencommP168Reg_154_155.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_154_155.setStatus("current")
_GencommP168Reg_156_157_Type = Unsigned32
_GencommP168Reg_156_157_Object = MibTableColumn
gencommP168Reg_156_157 = _GencommP168Reg_156_157_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 80),
    _GencommP168Reg_156_157_Type()
)
gencommP168Reg_156_157.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_156_157.setStatus("current")
_GencommP168Reg_158_159_Type = Unsigned32
_GencommP168Reg_158_159_Object = MibTableColumn
gencommP168Reg_158_159 = _GencommP168Reg_158_159_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 81),
    _GencommP168Reg_158_159_Type()
)
gencommP168Reg_158_159.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_158_159.setStatus("current")
_GencommP168Reg_160_161_Type = Unsigned32
_GencommP168Reg_160_161_Object = MibTableColumn
gencommP168Reg_160_161 = _GencommP168Reg_160_161_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 82),
    _GencommP168Reg_160_161_Type()
)
gencommP168Reg_160_161.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_160_161.setStatus("current")
_GencommP168Reg_162_163_Type = Unsigned32
_GencommP168Reg_162_163_Object = MibTableColumn
gencommP168Reg_162_163 = _GencommP168Reg_162_163_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 83),
    _GencommP168Reg_162_163_Type()
)
gencommP168Reg_162_163.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_162_163.setStatus("current")
_GencommP168Reg_164_165_Type = Unsigned32
_GencommP168Reg_164_165_Object = MibTableColumn
gencommP168Reg_164_165 = _GencommP168Reg_164_165_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 84),
    _GencommP168Reg_164_165_Type()
)
gencommP168Reg_164_165.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_164_165.setStatus("current")
_GencommP168Reg_166_167_Type = Unsigned32
_GencommP168Reg_166_167_Object = MibTableColumn
gencommP168Reg_166_167 = _GencommP168Reg_166_167_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 85),
    _GencommP168Reg_166_167_Type()
)
gencommP168Reg_166_167.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_166_167.setStatus("current")
_GencommP168Reg_168_169_Type = Unsigned32
_GencommP168Reg_168_169_Object = MibTableColumn
gencommP168Reg_168_169 = _GencommP168Reg_168_169_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 86),
    _GencommP168Reg_168_169_Type()
)
gencommP168Reg_168_169.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_168_169.setStatus("current")
_GencommP168Reg_170_171_Type = Unsigned32
_GencommP168Reg_170_171_Object = MibTableColumn
gencommP168Reg_170_171 = _GencommP168Reg_170_171_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 87),
    _GencommP168Reg_170_171_Type()
)
gencommP168Reg_170_171.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_170_171.setStatus("current")
_GencommP168Reg_172_173_Type = Unsigned32
_GencommP168Reg_172_173_Object = MibTableColumn
gencommP168Reg_172_173 = _GencommP168Reg_172_173_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 88),
    _GencommP168Reg_172_173_Type()
)
gencommP168Reg_172_173.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_172_173.setStatus("current")
_GencommP168Reg_174_175_Type = Unsigned32
_GencommP168Reg_174_175_Object = MibTableColumn
gencommP168Reg_174_175 = _GencommP168Reg_174_175_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 89),
    _GencommP168Reg_174_175_Type()
)
gencommP168Reg_174_175.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_174_175.setStatus("current")
_GencommP168Reg_176_177_Type = Unsigned32
_GencommP168Reg_176_177_Object = MibTableColumn
gencommP168Reg_176_177 = _GencommP168Reg_176_177_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 90),
    _GencommP168Reg_176_177_Type()
)
gencommP168Reg_176_177.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_176_177.setStatus("current")
_GencommP168Reg_178_179_Type = Unsigned32
_GencommP168Reg_178_179_Object = MibTableColumn
gencommP168Reg_178_179 = _GencommP168Reg_178_179_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 91),
    _GencommP168Reg_178_179_Type()
)
gencommP168Reg_178_179.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_178_179.setStatus("current")
_GencommP168Reg_180_181_Type = Unsigned32
_GencommP168Reg_180_181_Object = MibTableColumn
gencommP168Reg_180_181 = _GencommP168Reg_180_181_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 92),
    _GencommP168Reg_180_181_Type()
)
gencommP168Reg_180_181.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_180_181.setStatus("current")
_GencommP168Reg_182_183_Type = Unsigned32
_GencommP168Reg_182_183_Object = MibTableColumn
gencommP168Reg_182_183 = _GencommP168Reg_182_183_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 93),
    _GencommP168Reg_182_183_Type()
)
gencommP168Reg_182_183.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_182_183.setStatus("current")
_GencommP168Reg_184_185_Type = Unsigned32
_GencommP168Reg_184_185_Object = MibTableColumn
gencommP168Reg_184_185 = _GencommP168Reg_184_185_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 94),
    _GencommP168Reg_184_185_Type()
)
gencommP168Reg_184_185.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_184_185.setStatus("current")
_GencommP168Reg_186_187_Type = Unsigned32
_GencommP168Reg_186_187_Object = MibTableColumn
gencommP168Reg_186_187 = _GencommP168Reg_186_187_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 95),
    _GencommP168Reg_186_187_Type()
)
gencommP168Reg_186_187.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_186_187.setStatus("current")
_GencommP168Reg_188_189_Type = Unsigned32
_GencommP168Reg_188_189_Object = MibTableColumn
gencommP168Reg_188_189 = _GencommP168Reg_188_189_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 96),
    _GencommP168Reg_188_189_Type()
)
gencommP168Reg_188_189.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_188_189.setStatus("current")
_GencommP168Reg_190_191_Type = Unsigned32
_GencommP168Reg_190_191_Object = MibTableColumn
gencommP168Reg_190_191 = _GencommP168Reg_190_191_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 97),
    _GencommP168Reg_190_191_Type()
)
gencommP168Reg_190_191.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_190_191.setStatus("current")
_GencommP168Reg_192_193_Type = Unsigned32
_GencommP168Reg_192_193_Object = MibTableColumn
gencommP168Reg_192_193 = _GencommP168Reg_192_193_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 98),
    _GencommP168Reg_192_193_Type()
)
gencommP168Reg_192_193.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_192_193.setStatus("current")
_GencommP168Reg_194_195_Type = Unsigned32
_GencommP168Reg_194_195_Object = MibTableColumn
gencommP168Reg_194_195 = _GencommP168Reg_194_195_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 99),
    _GencommP168Reg_194_195_Type()
)
gencommP168Reg_194_195.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_194_195.setStatus("current")
_GencommP168Reg_196_197_Type = Unsigned32
_GencommP168Reg_196_197_Object = MibTableColumn
gencommP168Reg_196_197 = _GencommP168Reg_196_197_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 100),
    _GencommP168Reg_196_197_Type()
)
gencommP168Reg_196_197.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_196_197.setStatus("current")
_GencommP168Reg_198_199_Type = Unsigned32
_GencommP168Reg_198_199_Object = MibTableColumn
gencommP168Reg_198_199 = _GencommP168Reg_198_199_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 101),
    _GencommP168Reg_198_199_Type()
)
gencommP168Reg_198_199.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_198_199.setStatus("current")
_GencommP168Reg_200_201_Type = Unsigned32
_GencommP168Reg_200_201_Object = MibTableColumn
gencommP168Reg_200_201 = _GencommP168Reg_200_201_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 102),
    _GencommP168Reg_200_201_Type()
)
gencommP168Reg_200_201.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_200_201.setStatus("current")
_GencommP168Reg_202_203_Type = Unsigned32
_GencommP168Reg_202_203_Object = MibTableColumn
gencommP168Reg_202_203 = _GencommP168Reg_202_203_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 103),
    _GencommP168Reg_202_203_Type()
)
gencommP168Reg_202_203.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_202_203.setStatus("current")
_GencommP168Reg_204_205_Type = Unsigned32
_GencommP168Reg_204_205_Object = MibTableColumn
gencommP168Reg_204_205 = _GencommP168Reg_204_205_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 104),
    _GencommP168Reg_204_205_Type()
)
gencommP168Reg_204_205.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_204_205.setStatus("current")
_GencommP168Reg_206_207_Type = Unsigned32
_GencommP168Reg_206_207_Object = MibTableColumn
gencommP168Reg_206_207 = _GencommP168Reg_206_207_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 105),
    _GencommP168Reg_206_207_Type()
)
gencommP168Reg_206_207.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_206_207.setStatus("current")
_GencommP168Reg_208_209_Type = Unsigned32
_GencommP168Reg_208_209_Object = MibTableColumn
gencommP168Reg_208_209 = _GencommP168Reg_208_209_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 106),
    _GencommP168Reg_208_209_Type()
)
gencommP168Reg_208_209.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_208_209.setStatus("current")
_GencommP168Reg_210_211_Type = Unsigned32
_GencommP168Reg_210_211_Object = MibTableColumn
gencommP168Reg_210_211 = _GencommP168Reg_210_211_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 107),
    _GencommP168Reg_210_211_Type()
)
gencommP168Reg_210_211.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_210_211.setStatus("current")
_GencommP168Reg_212_213_Type = Unsigned32
_GencommP168Reg_212_213_Object = MibTableColumn
gencommP168Reg_212_213 = _GencommP168Reg_212_213_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 108),
    _GencommP168Reg_212_213_Type()
)
gencommP168Reg_212_213.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_212_213.setStatus("current")
_GencommP168Reg_214_215_Type = Unsigned32
_GencommP168Reg_214_215_Object = MibTableColumn
gencommP168Reg_214_215 = _GencommP168Reg_214_215_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 109),
    _GencommP168Reg_214_215_Type()
)
gencommP168Reg_214_215.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_214_215.setStatus("current")
_GencommP168Reg_216_217_Type = Unsigned32
_GencommP168Reg_216_217_Object = MibTableColumn
gencommP168Reg_216_217 = _GencommP168Reg_216_217_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 110),
    _GencommP168Reg_216_217_Type()
)
gencommP168Reg_216_217.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_216_217.setStatus("current")
_GencommP168Reg_218_219_Type = Unsigned32
_GencommP168Reg_218_219_Object = MibTableColumn
gencommP168Reg_218_219 = _GencommP168Reg_218_219_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 111),
    _GencommP168Reg_218_219_Type()
)
gencommP168Reg_218_219.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_218_219.setStatus("current")
_GencommP168Reg_220_221_Type = Unsigned32
_GencommP168Reg_220_221_Object = MibTableColumn
gencommP168Reg_220_221 = _GencommP168Reg_220_221_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 112),
    _GencommP168Reg_220_221_Type()
)
gencommP168Reg_220_221.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_220_221.setStatus("current")
_GencommP168Reg_222_223_Type = Unsigned32
_GencommP168Reg_222_223_Object = MibTableColumn
gencommP168Reg_222_223 = _GencommP168Reg_222_223_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 113),
    _GencommP168Reg_222_223_Type()
)
gencommP168Reg_222_223.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_222_223.setStatus("current")
_GencommP168Reg_224_225_Type = Unsigned32
_GencommP168Reg_224_225_Object = MibTableColumn
gencommP168Reg_224_225 = _GencommP168Reg_224_225_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 114),
    _GencommP168Reg_224_225_Type()
)
gencommP168Reg_224_225.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_224_225.setStatus("current")
_GencommP168Reg_226_227_Type = Unsigned32
_GencommP168Reg_226_227_Object = MibTableColumn
gencommP168Reg_226_227 = _GencommP168Reg_226_227_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 115),
    _GencommP168Reg_226_227_Type()
)
gencommP168Reg_226_227.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_226_227.setStatus("current")
_GencommP168Reg_228_229_Type = Unsigned32
_GencommP168Reg_228_229_Object = MibTableColumn
gencommP168Reg_228_229 = _GencommP168Reg_228_229_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 116),
    _GencommP168Reg_228_229_Type()
)
gencommP168Reg_228_229.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_228_229.setStatus("current")
_GencommP168Reg_230_231_Type = Unsigned32
_GencommP168Reg_230_231_Object = MibTableColumn
gencommP168Reg_230_231 = _GencommP168Reg_230_231_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 117),
    _GencommP168Reg_230_231_Type()
)
gencommP168Reg_230_231.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_230_231.setStatus("current")
_GencommP168Reg_232_233_Type = Unsigned32
_GencommP168Reg_232_233_Object = MibTableColumn
gencommP168Reg_232_233 = _GencommP168Reg_232_233_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 118),
    _GencommP168Reg_232_233_Type()
)
gencommP168Reg_232_233.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_232_233.setStatus("current")
_GencommP168Reg_234_235_Type = Unsigned32
_GencommP168Reg_234_235_Object = MibTableColumn
gencommP168Reg_234_235 = _GencommP168Reg_234_235_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 119),
    _GencommP168Reg_234_235_Type()
)
gencommP168Reg_234_235.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_234_235.setStatus("current")
_GencommP168Reg_236_237_Type = Unsigned32
_GencommP168Reg_236_237_Object = MibTableColumn
gencommP168Reg_236_237 = _GencommP168Reg_236_237_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 120),
    _GencommP168Reg_236_237_Type()
)
gencommP168Reg_236_237.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_236_237.setStatus("current")
_GencommP168Reg_238_239_Type = Unsigned32
_GencommP168Reg_238_239_Object = MibTableColumn
gencommP168Reg_238_239 = _GencommP168Reg_238_239_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 121),
    _GencommP168Reg_238_239_Type()
)
gencommP168Reg_238_239.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_238_239.setStatus("current")
_GencommP168Reg_240_241_Type = Unsigned32
_GencommP168Reg_240_241_Object = MibTableColumn
gencommP168Reg_240_241 = _GencommP168Reg_240_241_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 122),
    _GencommP168Reg_240_241_Type()
)
gencommP168Reg_240_241.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_240_241.setStatus("current")
_GencommP168Reg_242_243_Type = Unsigned32
_GencommP168Reg_242_243_Object = MibTableColumn
gencommP168Reg_242_243 = _GencommP168Reg_242_243_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 123),
    _GencommP168Reg_242_243_Type()
)
gencommP168Reg_242_243.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_242_243.setStatus("current")
_GencommP168Reg_244_245_Type = Unsigned32
_GencommP168Reg_244_245_Object = MibTableColumn
gencommP168Reg_244_245 = _GencommP168Reg_244_245_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 124),
    _GencommP168Reg_244_245_Type()
)
gencommP168Reg_244_245.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_244_245.setStatus("current")
_GencommP168Reg_246_247_Type = Unsigned32
_GencommP168Reg_246_247_Object = MibTableColumn
gencommP168Reg_246_247 = _GencommP168Reg_246_247_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 125),
    _GencommP168Reg_246_247_Type()
)
gencommP168Reg_246_247.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_246_247.setStatus("current")
_GencommP168Reg_248_249_Type = Unsigned32
_GencommP168Reg_248_249_Object = MibTableColumn
gencommP168Reg_248_249 = _GencommP168Reg_248_249_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 126),
    _GencommP168Reg_248_249_Type()
)
gencommP168Reg_248_249.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_248_249.setStatus("current")
_GencommP168Reg_250_251_Type = Unsigned32
_GencommP168Reg_250_251_Object = MibTableColumn
gencommP168Reg_250_251 = _GencommP168Reg_250_251_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 127),
    _GencommP168Reg_250_251_Type()
)
gencommP168Reg_250_251.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_250_251.setStatus("current")
_GencommP168Reg_252_253_Type = Unsigned32
_GencommP168Reg_252_253_Object = MibTableColumn
gencommP168Reg_252_253 = _GencommP168Reg_252_253_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 128),
    _GencommP168Reg_252_253_Type()
)
gencommP168Reg_252_253.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_252_253.setStatus("current")
_GencommP168Reg_254_255_Type = Unsigned32
_GencommP168Reg_254_255_Object = MibTableColumn
gencommP168Reg_254_255 = _GencommP168Reg_254_255_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 3, 1, 129),
    _GencommP168Reg_254_255_Type()
)
gencommP168Reg_254_255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP168Reg_254_255.setStatus("current")
_GencommP169Table_Object = MibTable
gencommP169Table = _GencommP169Table_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4)
)
if mibBuilder.loadTexts:
    gencommP169Table.setStatus("current")
_GencommP169Entry_Object = MibTableRow
gencommP169Entry = _GencommP169Entry_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1)
)
gencommP169Entry.setIndexNames(
    (0, "DSE-8610-MIB", "gencommP169KeyID"),
)
if mibBuilder.loadTexts:
    gencommP169Entry.setStatus("current")


class _GencommP169KeyID_Type(Integer32):
    """Custom type gencommP169KeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GencommP169KeyID_Type.__name__ = "Integer32"
_GencommP169KeyID_Object = MibTableColumn
gencommP169KeyID = _GencommP169KeyID_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 1),
    _GencommP169KeyID_Type()
)
gencommP169KeyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gencommP169KeyID.setStatus("current")
_GencommP169Reg_0_1_Type = Unsigned32
_GencommP169Reg_0_1_Object = MibTableColumn
gencommP169Reg_0_1 = _GencommP169Reg_0_1_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 2),
    _GencommP169Reg_0_1_Type()
)
gencommP169Reg_0_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_0_1.setStatus("current")
_GencommP169Reg_2_3_Type = Unsigned32
_GencommP169Reg_2_3_Object = MibTableColumn
gencommP169Reg_2_3 = _GencommP169Reg_2_3_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 3),
    _GencommP169Reg_2_3_Type()
)
gencommP169Reg_2_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_2_3.setStatus("current")
_GencommP169Reg_4_5_Type = Unsigned32
_GencommP169Reg_4_5_Object = MibTableColumn
gencommP169Reg_4_5 = _GencommP169Reg_4_5_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 4),
    _GencommP169Reg_4_5_Type()
)
gencommP169Reg_4_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_4_5.setStatus("current")
_GencommP169Reg_6_7_Type = Unsigned32
_GencommP169Reg_6_7_Object = MibTableColumn
gencommP169Reg_6_7 = _GencommP169Reg_6_7_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 5),
    _GencommP169Reg_6_7_Type()
)
gencommP169Reg_6_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_6_7.setStatus("current")
_GencommP169Reg_8_9_Type = Unsigned32
_GencommP169Reg_8_9_Object = MibTableColumn
gencommP169Reg_8_9 = _GencommP169Reg_8_9_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 6),
    _GencommP169Reg_8_9_Type()
)
gencommP169Reg_8_9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_8_9.setStatus("current")
_GencommP169Reg_10_11_Type = Unsigned32
_GencommP169Reg_10_11_Object = MibTableColumn
gencommP169Reg_10_11 = _GencommP169Reg_10_11_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 7),
    _GencommP169Reg_10_11_Type()
)
gencommP169Reg_10_11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_10_11.setStatus("current")
_GencommP169Reg_12_13_Type = Unsigned32
_GencommP169Reg_12_13_Object = MibTableColumn
gencommP169Reg_12_13 = _GencommP169Reg_12_13_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 8),
    _GencommP169Reg_12_13_Type()
)
gencommP169Reg_12_13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_12_13.setStatus("current")
_GencommP169Reg_14_15_Type = Unsigned32
_GencommP169Reg_14_15_Object = MibTableColumn
gencommP169Reg_14_15 = _GencommP169Reg_14_15_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 9),
    _GencommP169Reg_14_15_Type()
)
gencommP169Reg_14_15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_14_15.setStatus("current")
_GencommP169Reg_16_17_Type = Unsigned32
_GencommP169Reg_16_17_Object = MibTableColumn
gencommP169Reg_16_17 = _GencommP169Reg_16_17_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 10),
    _GencommP169Reg_16_17_Type()
)
gencommP169Reg_16_17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_16_17.setStatus("current")
_GencommP169Reg_18_19_Type = Unsigned32
_GencommP169Reg_18_19_Object = MibTableColumn
gencommP169Reg_18_19 = _GencommP169Reg_18_19_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 11),
    _GencommP169Reg_18_19_Type()
)
gencommP169Reg_18_19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_18_19.setStatus("current")
_GencommP169Reg_20_21_Type = Unsigned32
_GencommP169Reg_20_21_Object = MibTableColumn
gencommP169Reg_20_21 = _GencommP169Reg_20_21_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 12),
    _GencommP169Reg_20_21_Type()
)
gencommP169Reg_20_21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_20_21.setStatus("current")
_GencommP169Reg_22_23_Type = Unsigned32
_GencommP169Reg_22_23_Object = MibTableColumn
gencommP169Reg_22_23 = _GencommP169Reg_22_23_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 13),
    _GencommP169Reg_22_23_Type()
)
gencommP169Reg_22_23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_22_23.setStatus("current")
_GencommP169Reg_24_25_Type = Unsigned32
_GencommP169Reg_24_25_Object = MibTableColumn
gencommP169Reg_24_25 = _GencommP169Reg_24_25_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 14),
    _GencommP169Reg_24_25_Type()
)
gencommP169Reg_24_25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_24_25.setStatus("current")
_GencommP169Reg_26_27_Type = Unsigned32
_GencommP169Reg_26_27_Object = MibTableColumn
gencommP169Reg_26_27 = _GencommP169Reg_26_27_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 15),
    _GencommP169Reg_26_27_Type()
)
gencommP169Reg_26_27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_26_27.setStatus("current")
_GencommP169Reg_28_29_Type = Unsigned32
_GencommP169Reg_28_29_Object = MibTableColumn
gencommP169Reg_28_29 = _GencommP169Reg_28_29_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 16),
    _GencommP169Reg_28_29_Type()
)
gencommP169Reg_28_29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_28_29.setStatus("current")
_GencommP169Reg_30_31_Type = Unsigned32
_GencommP169Reg_30_31_Object = MibTableColumn
gencommP169Reg_30_31 = _GencommP169Reg_30_31_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 17),
    _GencommP169Reg_30_31_Type()
)
gencommP169Reg_30_31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_30_31.setStatus("current")
_GencommP169Reg_32_33_Type = Unsigned32
_GencommP169Reg_32_33_Object = MibTableColumn
gencommP169Reg_32_33 = _GencommP169Reg_32_33_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 18),
    _GencommP169Reg_32_33_Type()
)
gencommP169Reg_32_33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_32_33.setStatus("current")
_GencommP169Reg_34_35_Type = Unsigned32
_GencommP169Reg_34_35_Object = MibTableColumn
gencommP169Reg_34_35 = _GencommP169Reg_34_35_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 19),
    _GencommP169Reg_34_35_Type()
)
gencommP169Reg_34_35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_34_35.setStatus("current")
_GencommP169Reg_36_37_Type = Unsigned32
_GencommP169Reg_36_37_Object = MibTableColumn
gencommP169Reg_36_37 = _GencommP169Reg_36_37_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 20),
    _GencommP169Reg_36_37_Type()
)
gencommP169Reg_36_37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_36_37.setStatus("current")
_GencommP169Reg_38_39_Type = Unsigned32
_GencommP169Reg_38_39_Object = MibTableColumn
gencommP169Reg_38_39 = _GencommP169Reg_38_39_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 21),
    _GencommP169Reg_38_39_Type()
)
gencommP169Reg_38_39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_38_39.setStatus("current")
_GencommP169Reg_40_41_Type = Unsigned32
_GencommP169Reg_40_41_Object = MibTableColumn
gencommP169Reg_40_41 = _GencommP169Reg_40_41_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 22),
    _GencommP169Reg_40_41_Type()
)
gencommP169Reg_40_41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_40_41.setStatus("current")
_GencommP169Reg_42_43_Type = Unsigned32
_GencommP169Reg_42_43_Object = MibTableColumn
gencommP169Reg_42_43 = _GencommP169Reg_42_43_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 23),
    _GencommP169Reg_42_43_Type()
)
gencommP169Reg_42_43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_42_43.setStatus("current")
_GencommP169Reg_44_45_Type = Unsigned32
_GencommP169Reg_44_45_Object = MibTableColumn
gencommP169Reg_44_45 = _GencommP169Reg_44_45_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 24),
    _GencommP169Reg_44_45_Type()
)
gencommP169Reg_44_45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_44_45.setStatus("current")
_GencommP169Reg_46_47_Type = Unsigned32
_GencommP169Reg_46_47_Object = MibTableColumn
gencommP169Reg_46_47 = _GencommP169Reg_46_47_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 25),
    _GencommP169Reg_46_47_Type()
)
gencommP169Reg_46_47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_46_47.setStatus("current")
_GencommP169Reg_48_49_Type = Unsigned32
_GencommP169Reg_48_49_Object = MibTableColumn
gencommP169Reg_48_49 = _GencommP169Reg_48_49_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 26),
    _GencommP169Reg_48_49_Type()
)
gencommP169Reg_48_49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_48_49.setStatus("current")
_GencommP169Reg_50_51_Type = Unsigned32
_GencommP169Reg_50_51_Object = MibTableColumn
gencommP169Reg_50_51 = _GencommP169Reg_50_51_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 27),
    _GencommP169Reg_50_51_Type()
)
gencommP169Reg_50_51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_50_51.setStatus("current")
_GencommP169Reg_52_53_Type = Unsigned32
_GencommP169Reg_52_53_Object = MibTableColumn
gencommP169Reg_52_53 = _GencommP169Reg_52_53_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 28),
    _GencommP169Reg_52_53_Type()
)
gencommP169Reg_52_53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_52_53.setStatus("current")
_GencommP169Reg_54_55_Type = Unsigned32
_GencommP169Reg_54_55_Object = MibTableColumn
gencommP169Reg_54_55 = _GencommP169Reg_54_55_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 29),
    _GencommP169Reg_54_55_Type()
)
gencommP169Reg_54_55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_54_55.setStatus("current")
_GencommP169Reg_56_57_Type = Unsigned32
_GencommP169Reg_56_57_Object = MibTableColumn
gencommP169Reg_56_57 = _GencommP169Reg_56_57_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 30),
    _GencommP169Reg_56_57_Type()
)
gencommP169Reg_56_57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_56_57.setStatus("current")
_GencommP169Reg_58_59_Type = Unsigned32
_GencommP169Reg_58_59_Object = MibTableColumn
gencommP169Reg_58_59 = _GencommP169Reg_58_59_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 31),
    _GencommP169Reg_58_59_Type()
)
gencommP169Reg_58_59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_58_59.setStatus("current")
_GencommP169Reg_60_61_Type = Unsigned32
_GencommP169Reg_60_61_Object = MibTableColumn
gencommP169Reg_60_61 = _GencommP169Reg_60_61_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 32),
    _GencommP169Reg_60_61_Type()
)
gencommP169Reg_60_61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_60_61.setStatus("current")
_GencommP169Reg_62_63_Type = Unsigned32
_GencommP169Reg_62_63_Object = MibTableColumn
gencommP169Reg_62_63 = _GencommP169Reg_62_63_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 33),
    _GencommP169Reg_62_63_Type()
)
gencommP169Reg_62_63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_62_63.setStatus("current")
_GencommP169Reg_64_65_Type = Unsigned32
_GencommP169Reg_64_65_Object = MibTableColumn
gencommP169Reg_64_65 = _GencommP169Reg_64_65_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 34),
    _GencommP169Reg_64_65_Type()
)
gencommP169Reg_64_65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_64_65.setStatus("current")
_GencommP169Reg_66_67_Type = Unsigned32
_GencommP169Reg_66_67_Object = MibTableColumn
gencommP169Reg_66_67 = _GencommP169Reg_66_67_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 35),
    _GencommP169Reg_66_67_Type()
)
gencommP169Reg_66_67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_66_67.setStatus("current")
_GencommP169Reg_68_69_Type = Unsigned32
_GencommP169Reg_68_69_Object = MibTableColumn
gencommP169Reg_68_69 = _GencommP169Reg_68_69_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 36),
    _GencommP169Reg_68_69_Type()
)
gencommP169Reg_68_69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_68_69.setStatus("current")
_GencommP169Reg_70_71_Type = Unsigned32
_GencommP169Reg_70_71_Object = MibTableColumn
gencommP169Reg_70_71 = _GencommP169Reg_70_71_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 37),
    _GencommP169Reg_70_71_Type()
)
gencommP169Reg_70_71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_70_71.setStatus("current")
_GencommP169Reg_72_73_Type = Unsigned32
_GencommP169Reg_72_73_Object = MibTableColumn
gencommP169Reg_72_73 = _GencommP169Reg_72_73_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 38),
    _GencommP169Reg_72_73_Type()
)
gencommP169Reg_72_73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_72_73.setStatus("current")
_GencommP169Reg_74_75_Type = Unsigned32
_GencommP169Reg_74_75_Object = MibTableColumn
gencommP169Reg_74_75 = _GencommP169Reg_74_75_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 39),
    _GencommP169Reg_74_75_Type()
)
gencommP169Reg_74_75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_74_75.setStatus("current")
_GencommP169Reg_76_77_Type = Unsigned32
_GencommP169Reg_76_77_Object = MibTableColumn
gencommP169Reg_76_77 = _GencommP169Reg_76_77_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 40),
    _GencommP169Reg_76_77_Type()
)
gencommP169Reg_76_77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_76_77.setStatus("current")
_GencommP169Reg_78_79_Type = Unsigned32
_GencommP169Reg_78_79_Object = MibTableColumn
gencommP169Reg_78_79 = _GencommP169Reg_78_79_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 41),
    _GencommP169Reg_78_79_Type()
)
gencommP169Reg_78_79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_78_79.setStatus("current")
_GencommP169Reg_80_81_Type = Unsigned32
_GencommP169Reg_80_81_Object = MibTableColumn
gencommP169Reg_80_81 = _GencommP169Reg_80_81_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 42),
    _GencommP169Reg_80_81_Type()
)
gencommP169Reg_80_81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_80_81.setStatus("current")
_GencommP169Reg_82_83_Type = Unsigned32
_GencommP169Reg_82_83_Object = MibTableColumn
gencommP169Reg_82_83 = _GencommP169Reg_82_83_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 43),
    _GencommP169Reg_82_83_Type()
)
gencommP169Reg_82_83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_82_83.setStatus("current")
_GencommP169Reg_84_85_Type = Unsigned32
_GencommP169Reg_84_85_Object = MibTableColumn
gencommP169Reg_84_85 = _GencommP169Reg_84_85_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 44),
    _GencommP169Reg_84_85_Type()
)
gencommP169Reg_84_85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_84_85.setStatus("current")
_GencommP169Reg_86_87_Type = Unsigned32
_GencommP169Reg_86_87_Object = MibTableColumn
gencommP169Reg_86_87 = _GencommP169Reg_86_87_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 45),
    _GencommP169Reg_86_87_Type()
)
gencommP169Reg_86_87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_86_87.setStatus("current")
_GencommP169Reg_88_89_Type = Unsigned32
_GencommP169Reg_88_89_Object = MibTableColumn
gencommP169Reg_88_89 = _GencommP169Reg_88_89_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 46),
    _GencommP169Reg_88_89_Type()
)
gencommP169Reg_88_89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_88_89.setStatus("current")
_GencommP169Reg_90_91_Type = Unsigned32
_GencommP169Reg_90_91_Object = MibTableColumn
gencommP169Reg_90_91 = _GencommP169Reg_90_91_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 47),
    _GencommP169Reg_90_91_Type()
)
gencommP169Reg_90_91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_90_91.setStatus("current")
_GencommP169Reg_92_93_Type = Unsigned32
_GencommP169Reg_92_93_Object = MibTableColumn
gencommP169Reg_92_93 = _GencommP169Reg_92_93_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 48),
    _GencommP169Reg_92_93_Type()
)
gencommP169Reg_92_93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_92_93.setStatus("current")
_GencommP169Reg_94_95_Type = Unsigned32
_GencommP169Reg_94_95_Object = MibTableColumn
gencommP169Reg_94_95 = _GencommP169Reg_94_95_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 49),
    _GencommP169Reg_94_95_Type()
)
gencommP169Reg_94_95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_94_95.setStatus("current")
_GencommP169Reg_96_97_Type = Unsigned32
_GencommP169Reg_96_97_Object = MibTableColumn
gencommP169Reg_96_97 = _GencommP169Reg_96_97_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 50),
    _GencommP169Reg_96_97_Type()
)
gencommP169Reg_96_97.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_96_97.setStatus("current")
_GencommP169Reg_98_99_Type = Unsigned32
_GencommP169Reg_98_99_Object = MibTableColumn
gencommP169Reg_98_99 = _GencommP169Reg_98_99_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 51),
    _GencommP169Reg_98_99_Type()
)
gencommP169Reg_98_99.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_98_99.setStatus("current")
_GencommP169Reg_100_101_Type = Unsigned32
_GencommP169Reg_100_101_Object = MibTableColumn
gencommP169Reg_100_101 = _GencommP169Reg_100_101_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 52),
    _GencommP169Reg_100_101_Type()
)
gencommP169Reg_100_101.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_100_101.setStatus("current")
_GencommP169Reg_102_103_Type = Unsigned32
_GencommP169Reg_102_103_Object = MibTableColumn
gencommP169Reg_102_103 = _GencommP169Reg_102_103_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 53),
    _GencommP169Reg_102_103_Type()
)
gencommP169Reg_102_103.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_102_103.setStatus("current")
_GencommP169Reg_104_105_Type = Unsigned32
_GencommP169Reg_104_105_Object = MibTableColumn
gencommP169Reg_104_105 = _GencommP169Reg_104_105_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 54),
    _GencommP169Reg_104_105_Type()
)
gencommP169Reg_104_105.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_104_105.setStatus("current")
_GencommP169Reg_106_107_Type = Unsigned32
_GencommP169Reg_106_107_Object = MibTableColumn
gencommP169Reg_106_107 = _GencommP169Reg_106_107_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 55),
    _GencommP169Reg_106_107_Type()
)
gencommP169Reg_106_107.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_106_107.setStatus("current")
_GencommP169Reg_108_109_Type = Unsigned32
_GencommP169Reg_108_109_Object = MibTableColumn
gencommP169Reg_108_109 = _GencommP169Reg_108_109_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 56),
    _GencommP169Reg_108_109_Type()
)
gencommP169Reg_108_109.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_108_109.setStatus("current")
_GencommP169Reg_110_111_Type = Unsigned32
_GencommP169Reg_110_111_Object = MibTableColumn
gencommP169Reg_110_111 = _GencommP169Reg_110_111_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 57),
    _GencommP169Reg_110_111_Type()
)
gencommP169Reg_110_111.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_110_111.setStatus("current")
_GencommP169Reg_112_113_Type = Unsigned32
_GencommP169Reg_112_113_Object = MibTableColumn
gencommP169Reg_112_113 = _GencommP169Reg_112_113_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 58),
    _GencommP169Reg_112_113_Type()
)
gencommP169Reg_112_113.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_112_113.setStatus("current")
_GencommP169Reg_114_115_Type = Unsigned32
_GencommP169Reg_114_115_Object = MibTableColumn
gencommP169Reg_114_115 = _GencommP169Reg_114_115_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 59),
    _GencommP169Reg_114_115_Type()
)
gencommP169Reg_114_115.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_114_115.setStatus("current")
_GencommP169Reg_116_117_Type = Unsigned32
_GencommP169Reg_116_117_Object = MibTableColumn
gencommP169Reg_116_117 = _GencommP169Reg_116_117_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 60),
    _GencommP169Reg_116_117_Type()
)
gencommP169Reg_116_117.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_116_117.setStatus("current")
_GencommP169Reg_118_119_Type = Unsigned32
_GencommP169Reg_118_119_Object = MibTableColumn
gencommP169Reg_118_119 = _GencommP169Reg_118_119_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 61),
    _GencommP169Reg_118_119_Type()
)
gencommP169Reg_118_119.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_118_119.setStatus("current")
_GencommP169Reg_120_121_Type = Unsigned32
_GencommP169Reg_120_121_Object = MibTableColumn
gencommP169Reg_120_121 = _GencommP169Reg_120_121_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 62),
    _GencommP169Reg_120_121_Type()
)
gencommP169Reg_120_121.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_120_121.setStatus("current")
_GencommP169Reg_122_123_Type = Unsigned32
_GencommP169Reg_122_123_Object = MibTableColumn
gencommP169Reg_122_123 = _GencommP169Reg_122_123_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 63),
    _GencommP169Reg_122_123_Type()
)
gencommP169Reg_122_123.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_122_123.setStatus("current")
_GencommP169Reg_124_125_Type = Unsigned32
_GencommP169Reg_124_125_Object = MibTableColumn
gencommP169Reg_124_125 = _GencommP169Reg_124_125_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 64),
    _GencommP169Reg_124_125_Type()
)
gencommP169Reg_124_125.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_124_125.setStatus("current")
_GencommP169Reg_126_127_Type = Unsigned32
_GencommP169Reg_126_127_Object = MibTableColumn
gencommP169Reg_126_127 = _GencommP169Reg_126_127_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 65),
    _GencommP169Reg_126_127_Type()
)
gencommP169Reg_126_127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_126_127.setStatus("current")
_GencommP169Reg_128_129_Type = Unsigned32
_GencommP169Reg_128_129_Object = MibTableColumn
gencommP169Reg_128_129 = _GencommP169Reg_128_129_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 66),
    _GencommP169Reg_128_129_Type()
)
gencommP169Reg_128_129.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_128_129.setStatus("current")
_GencommP169Reg_130_131_Type = Unsigned32
_GencommP169Reg_130_131_Object = MibTableColumn
gencommP169Reg_130_131 = _GencommP169Reg_130_131_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 67),
    _GencommP169Reg_130_131_Type()
)
gencommP169Reg_130_131.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_130_131.setStatus("current")
_GencommP169Reg_132_133_Type = Unsigned32
_GencommP169Reg_132_133_Object = MibTableColumn
gencommP169Reg_132_133 = _GencommP169Reg_132_133_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 68),
    _GencommP169Reg_132_133_Type()
)
gencommP169Reg_132_133.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_132_133.setStatus("current")
_GencommP169Reg_134_135_Type = Unsigned32
_GencommP169Reg_134_135_Object = MibTableColumn
gencommP169Reg_134_135 = _GencommP169Reg_134_135_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 69),
    _GencommP169Reg_134_135_Type()
)
gencommP169Reg_134_135.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_134_135.setStatus("current")
_GencommP169Reg_136_137_Type = Unsigned32
_GencommP169Reg_136_137_Object = MibTableColumn
gencommP169Reg_136_137 = _GencommP169Reg_136_137_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 70),
    _GencommP169Reg_136_137_Type()
)
gencommP169Reg_136_137.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_136_137.setStatus("current")
_GencommP169Reg_138_139_Type = Unsigned32
_GencommP169Reg_138_139_Object = MibTableColumn
gencommP169Reg_138_139 = _GencommP169Reg_138_139_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 71),
    _GencommP169Reg_138_139_Type()
)
gencommP169Reg_138_139.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_138_139.setStatus("current")
_GencommP169Reg_140_141_Type = Unsigned32
_GencommP169Reg_140_141_Object = MibTableColumn
gencommP169Reg_140_141 = _GencommP169Reg_140_141_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 72),
    _GencommP169Reg_140_141_Type()
)
gencommP169Reg_140_141.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_140_141.setStatus("current")
_GencommP169Reg_142_143_Type = Unsigned32
_GencommP169Reg_142_143_Object = MibTableColumn
gencommP169Reg_142_143 = _GencommP169Reg_142_143_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 73),
    _GencommP169Reg_142_143_Type()
)
gencommP169Reg_142_143.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_142_143.setStatus("current")
_GencommP169Reg_144_145_Type = Unsigned32
_GencommP169Reg_144_145_Object = MibTableColumn
gencommP169Reg_144_145 = _GencommP169Reg_144_145_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 74),
    _GencommP169Reg_144_145_Type()
)
gencommP169Reg_144_145.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_144_145.setStatus("current")
_GencommP169Reg_146_147_Type = Unsigned32
_GencommP169Reg_146_147_Object = MibTableColumn
gencommP169Reg_146_147 = _GencommP169Reg_146_147_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 75),
    _GencommP169Reg_146_147_Type()
)
gencommP169Reg_146_147.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_146_147.setStatus("current")
_GencommP169Reg_148_149_Type = Unsigned32
_GencommP169Reg_148_149_Object = MibTableColumn
gencommP169Reg_148_149 = _GencommP169Reg_148_149_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 76),
    _GencommP169Reg_148_149_Type()
)
gencommP169Reg_148_149.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_148_149.setStatus("current")
_GencommP169Reg_150_151_Type = Unsigned32
_GencommP169Reg_150_151_Object = MibTableColumn
gencommP169Reg_150_151 = _GencommP169Reg_150_151_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 77),
    _GencommP169Reg_150_151_Type()
)
gencommP169Reg_150_151.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_150_151.setStatus("current")
_GencommP169Reg_152_153_Type = Unsigned32
_GencommP169Reg_152_153_Object = MibTableColumn
gencommP169Reg_152_153 = _GencommP169Reg_152_153_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 78),
    _GencommP169Reg_152_153_Type()
)
gencommP169Reg_152_153.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_152_153.setStatus("current")
_GencommP169Reg_154_155_Type = Unsigned32
_GencommP169Reg_154_155_Object = MibTableColumn
gencommP169Reg_154_155 = _GencommP169Reg_154_155_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 79),
    _GencommP169Reg_154_155_Type()
)
gencommP169Reg_154_155.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_154_155.setStatus("current")
_GencommP169Reg_156_157_Type = Unsigned32
_GencommP169Reg_156_157_Object = MibTableColumn
gencommP169Reg_156_157 = _GencommP169Reg_156_157_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 80),
    _GencommP169Reg_156_157_Type()
)
gencommP169Reg_156_157.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_156_157.setStatus("current")
_GencommP169Reg_158_159_Type = Unsigned32
_GencommP169Reg_158_159_Object = MibTableColumn
gencommP169Reg_158_159 = _GencommP169Reg_158_159_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 81),
    _GencommP169Reg_158_159_Type()
)
gencommP169Reg_158_159.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_158_159.setStatus("current")
_GencommP169Reg_160_161_Type = Unsigned32
_GencommP169Reg_160_161_Object = MibTableColumn
gencommP169Reg_160_161 = _GencommP169Reg_160_161_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 82),
    _GencommP169Reg_160_161_Type()
)
gencommP169Reg_160_161.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_160_161.setStatus("current")
_GencommP169Reg_162_163_Type = Unsigned32
_GencommP169Reg_162_163_Object = MibTableColumn
gencommP169Reg_162_163 = _GencommP169Reg_162_163_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 83),
    _GencommP169Reg_162_163_Type()
)
gencommP169Reg_162_163.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_162_163.setStatus("current")
_GencommP169Reg_164_165_Type = Unsigned32
_GencommP169Reg_164_165_Object = MibTableColumn
gencommP169Reg_164_165 = _GencommP169Reg_164_165_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 84),
    _GencommP169Reg_164_165_Type()
)
gencommP169Reg_164_165.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_164_165.setStatus("current")
_GencommP169Reg_166_167_Type = Unsigned32
_GencommP169Reg_166_167_Object = MibTableColumn
gencommP169Reg_166_167 = _GencommP169Reg_166_167_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 85),
    _GencommP169Reg_166_167_Type()
)
gencommP169Reg_166_167.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_166_167.setStatus("current")
_GencommP169Reg_168_169_Type = Unsigned32
_GencommP169Reg_168_169_Object = MibTableColumn
gencommP169Reg_168_169 = _GencommP169Reg_168_169_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 86),
    _GencommP169Reg_168_169_Type()
)
gencommP169Reg_168_169.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_168_169.setStatus("current")
_GencommP169Reg_170_171_Type = Unsigned32
_GencommP169Reg_170_171_Object = MibTableColumn
gencommP169Reg_170_171 = _GencommP169Reg_170_171_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 87),
    _GencommP169Reg_170_171_Type()
)
gencommP169Reg_170_171.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_170_171.setStatus("current")
_GencommP169Reg_172_173_Type = Unsigned32
_GencommP169Reg_172_173_Object = MibTableColumn
gencommP169Reg_172_173 = _GencommP169Reg_172_173_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 88),
    _GencommP169Reg_172_173_Type()
)
gencommP169Reg_172_173.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_172_173.setStatus("current")
_GencommP169Reg_174_175_Type = Unsigned32
_GencommP169Reg_174_175_Object = MibTableColumn
gencommP169Reg_174_175 = _GencommP169Reg_174_175_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 89),
    _GencommP169Reg_174_175_Type()
)
gencommP169Reg_174_175.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_174_175.setStatus("current")
_GencommP169Reg_176_177_Type = Unsigned32
_GencommP169Reg_176_177_Object = MibTableColumn
gencommP169Reg_176_177 = _GencommP169Reg_176_177_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 90),
    _GencommP169Reg_176_177_Type()
)
gencommP169Reg_176_177.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_176_177.setStatus("current")
_GencommP169Reg_178_179_Type = Unsigned32
_GencommP169Reg_178_179_Object = MibTableColumn
gencommP169Reg_178_179 = _GencommP169Reg_178_179_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 91),
    _GencommP169Reg_178_179_Type()
)
gencommP169Reg_178_179.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_178_179.setStatus("current")
_GencommP169Reg_180_181_Type = Unsigned32
_GencommP169Reg_180_181_Object = MibTableColumn
gencommP169Reg_180_181 = _GencommP169Reg_180_181_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 92),
    _GencommP169Reg_180_181_Type()
)
gencommP169Reg_180_181.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_180_181.setStatus("current")
_GencommP169Reg_182_183_Type = Unsigned32
_GencommP169Reg_182_183_Object = MibTableColumn
gencommP169Reg_182_183 = _GencommP169Reg_182_183_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 93),
    _GencommP169Reg_182_183_Type()
)
gencommP169Reg_182_183.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_182_183.setStatus("current")
_GencommP169Reg_184_185_Type = Unsigned32
_GencommP169Reg_184_185_Object = MibTableColumn
gencommP169Reg_184_185 = _GencommP169Reg_184_185_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 94),
    _GencommP169Reg_184_185_Type()
)
gencommP169Reg_184_185.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_184_185.setStatus("current")
_GencommP169Reg_186_187_Type = Unsigned32
_GencommP169Reg_186_187_Object = MibTableColumn
gencommP169Reg_186_187 = _GencommP169Reg_186_187_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 95),
    _GencommP169Reg_186_187_Type()
)
gencommP169Reg_186_187.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_186_187.setStatus("current")
_GencommP169Reg_188_189_Type = Unsigned32
_GencommP169Reg_188_189_Object = MibTableColumn
gencommP169Reg_188_189 = _GencommP169Reg_188_189_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 96),
    _GencommP169Reg_188_189_Type()
)
gencommP169Reg_188_189.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_188_189.setStatus("current")
_GencommP169Reg_190_191_Type = Unsigned32
_GencommP169Reg_190_191_Object = MibTableColumn
gencommP169Reg_190_191 = _GencommP169Reg_190_191_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 97),
    _GencommP169Reg_190_191_Type()
)
gencommP169Reg_190_191.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_190_191.setStatus("current")
_GencommP169Reg_192_193_Type = Unsigned32
_GencommP169Reg_192_193_Object = MibTableColumn
gencommP169Reg_192_193 = _GencommP169Reg_192_193_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 98),
    _GencommP169Reg_192_193_Type()
)
gencommP169Reg_192_193.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_192_193.setStatus("current")
_GencommP169Reg_194_195_Type = Unsigned32
_GencommP169Reg_194_195_Object = MibTableColumn
gencommP169Reg_194_195 = _GencommP169Reg_194_195_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 99),
    _GencommP169Reg_194_195_Type()
)
gencommP169Reg_194_195.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_194_195.setStatus("current")
_GencommP169Reg_196_197_Type = Unsigned32
_GencommP169Reg_196_197_Object = MibTableColumn
gencommP169Reg_196_197 = _GencommP169Reg_196_197_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 100),
    _GencommP169Reg_196_197_Type()
)
gencommP169Reg_196_197.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_196_197.setStatus("current")
_GencommP169Reg_198_199_Type = Unsigned32
_GencommP169Reg_198_199_Object = MibTableColumn
gencommP169Reg_198_199 = _GencommP169Reg_198_199_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 101),
    _GencommP169Reg_198_199_Type()
)
gencommP169Reg_198_199.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_198_199.setStatus("current")
_GencommP169Reg_200_201_Type = Unsigned32
_GencommP169Reg_200_201_Object = MibTableColumn
gencommP169Reg_200_201 = _GencommP169Reg_200_201_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 102),
    _GencommP169Reg_200_201_Type()
)
gencommP169Reg_200_201.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_200_201.setStatus("current")
_GencommP169Reg_202_203_Type = Unsigned32
_GencommP169Reg_202_203_Object = MibTableColumn
gencommP169Reg_202_203 = _GencommP169Reg_202_203_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 103),
    _GencommP169Reg_202_203_Type()
)
gencommP169Reg_202_203.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_202_203.setStatus("current")
_GencommP169Reg_204_205_Type = Unsigned32
_GencommP169Reg_204_205_Object = MibTableColumn
gencommP169Reg_204_205 = _GencommP169Reg_204_205_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 104),
    _GencommP169Reg_204_205_Type()
)
gencommP169Reg_204_205.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_204_205.setStatus("current")
_GencommP169Reg_206_207_Type = Unsigned32
_GencommP169Reg_206_207_Object = MibTableColumn
gencommP169Reg_206_207 = _GencommP169Reg_206_207_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 105),
    _GencommP169Reg_206_207_Type()
)
gencommP169Reg_206_207.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_206_207.setStatus("current")
_GencommP169Reg_208_209_Type = Unsigned32
_GencommP169Reg_208_209_Object = MibTableColumn
gencommP169Reg_208_209 = _GencommP169Reg_208_209_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 106),
    _GencommP169Reg_208_209_Type()
)
gencommP169Reg_208_209.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_208_209.setStatus("current")
_GencommP169Reg_210_211_Type = Unsigned32
_GencommP169Reg_210_211_Object = MibTableColumn
gencommP169Reg_210_211 = _GencommP169Reg_210_211_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 107),
    _GencommP169Reg_210_211_Type()
)
gencommP169Reg_210_211.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_210_211.setStatus("current")
_GencommP169Reg_212_213_Type = Unsigned32
_GencommP169Reg_212_213_Object = MibTableColumn
gencommP169Reg_212_213 = _GencommP169Reg_212_213_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 108),
    _GencommP169Reg_212_213_Type()
)
gencommP169Reg_212_213.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_212_213.setStatus("current")
_GencommP169Reg_214_215_Type = Unsigned32
_GencommP169Reg_214_215_Object = MibTableColumn
gencommP169Reg_214_215 = _GencommP169Reg_214_215_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 109),
    _GencommP169Reg_214_215_Type()
)
gencommP169Reg_214_215.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_214_215.setStatus("current")
_GencommP169Reg_216_217_Type = Unsigned32
_GencommP169Reg_216_217_Object = MibTableColumn
gencommP169Reg_216_217 = _GencommP169Reg_216_217_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 110),
    _GencommP169Reg_216_217_Type()
)
gencommP169Reg_216_217.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_216_217.setStatus("current")
_GencommP169Reg_218_219_Type = Unsigned32
_GencommP169Reg_218_219_Object = MibTableColumn
gencommP169Reg_218_219 = _GencommP169Reg_218_219_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 111),
    _GencommP169Reg_218_219_Type()
)
gencommP169Reg_218_219.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_218_219.setStatus("current")
_GencommP169Reg_220_221_Type = Unsigned32
_GencommP169Reg_220_221_Object = MibTableColumn
gencommP169Reg_220_221 = _GencommP169Reg_220_221_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 112),
    _GencommP169Reg_220_221_Type()
)
gencommP169Reg_220_221.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_220_221.setStatus("current")
_GencommP169Reg_222_223_Type = Unsigned32
_GencommP169Reg_222_223_Object = MibTableColumn
gencommP169Reg_222_223 = _GencommP169Reg_222_223_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 113),
    _GencommP169Reg_222_223_Type()
)
gencommP169Reg_222_223.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_222_223.setStatus("current")
_GencommP169Reg_224_225_Type = Unsigned32
_GencommP169Reg_224_225_Object = MibTableColumn
gencommP169Reg_224_225 = _GencommP169Reg_224_225_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 114),
    _GencommP169Reg_224_225_Type()
)
gencommP169Reg_224_225.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_224_225.setStatus("current")
_GencommP169Reg_226_227_Type = Unsigned32
_GencommP169Reg_226_227_Object = MibTableColumn
gencommP169Reg_226_227 = _GencommP169Reg_226_227_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 115),
    _GencommP169Reg_226_227_Type()
)
gencommP169Reg_226_227.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_226_227.setStatus("current")
_GencommP169Reg_228_229_Type = Unsigned32
_GencommP169Reg_228_229_Object = MibTableColumn
gencommP169Reg_228_229 = _GencommP169Reg_228_229_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 116),
    _GencommP169Reg_228_229_Type()
)
gencommP169Reg_228_229.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_228_229.setStatus("current")
_GencommP169Reg_230_231_Type = Unsigned32
_GencommP169Reg_230_231_Object = MibTableColumn
gencommP169Reg_230_231 = _GencommP169Reg_230_231_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 117),
    _GencommP169Reg_230_231_Type()
)
gencommP169Reg_230_231.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_230_231.setStatus("current")
_GencommP169Reg_232_233_Type = Unsigned32
_GencommP169Reg_232_233_Object = MibTableColumn
gencommP169Reg_232_233 = _GencommP169Reg_232_233_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 118),
    _GencommP169Reg_232_233_Type()
)
gencommP169Reg_232_233.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_232_233.setStatus("current")
_GencommP169Reg_234_235_Type = Unsigned32
_GencommP169Reg_234_235_Object = MibTableColumn
gencommP169Reg_234_235 = _GencommP169Reg_234_235_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 119),
    _GencommP169Reg_234_235_Type()
)
gencommP169Reg_234_235.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_234_235.setStatus("current")
_GencommP169Reg_236_237_Type = Unsigned32
_GencommP169Reg_236_237_Object = MibTableColumn
gencommP169Reg_236_237 = _GencommP169Reg_236_237_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 120),
    _GencommP169Reg_236_237_Type()
)
gencommP169Reg_236_237.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_236_237.setStatus("current")
_GencommP169Reg_238_239_Type = Unsigned32
_GencommP169Reg_238_239_Object = MibTableColumn
gencommP169Reg_238_239 = _GencommP169Reg_238_239_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 121),
    _GencommP169Reg_238_239_Type()
)
gencommP169Reg_238_239.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_238_239.setStatus("current")
_GencommP169Reg_240_241_Type = Unsigned32
_GencommP169Reg_240_241_Object = MibTableColumn
gencommP169Reg_240_241 = _GencommP169Reg_240_241_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 122),
    _GencommP169Reg_240_241_Type()
)
gencommP169Reg_240_241.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_240_241.setStatus("current")
_GencommP169Reg_242_243_Type = Unsigned32
_GencommP169Reg_242_243_Object = MibTableColumn
gencommP169Reg_242_243 = _GencommP169Reg_242_243_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 123),
    _GencommP169Reg_242_243_Type()
)
gencommP169Reg_242_243.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_242_243.setStatus("current")
_GencommP169Reg_244_245_Type = Unsigned32
_GencommP169Reg_244_245_Object = MibTableColumn
gencommP169Reg_244_245 = _GencommP169Reg_244_245_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 124),
    _GencommP169Reg_244_245_Type()
)
gencommP169Reg_244_245.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_244_245.setStatus("current")
_GencommP169Reg_246_247_Type = Unsigned32
_GencommP169Reg_246_247_Object = MibTableColumn
gencommP169Reg_246_247 = _GencommP169Reg_246_247_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 125),
    _GencommP169Reg_246_247_Type()
)
gencommP169Reg_246_247.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_246_247.setStatus("current")
_GencommP169Reg_248_249_Type = Unsigned32
_GencommP169Reg_248_249_Object = MibTableColumn
gencommP169Reg_248_249 = _GencommP169Reg_248_249_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 126),
    _GencommP169Reg_248_249_Type()
)
gencommP169Reg_248_249.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_248_249.setStatus("current")
_GencommP169Reg_250_251_Type = Unsigned32
_GencommP169Reg_250_251_Object = MibTableColumn
gencommP169Reg_250_251 = _GencommP169Reg_250_251_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 127),
    _GencommP169Reg_250_251_Type()
)
gencommP169Reg_250_251.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_250_251.setStatus("current")
_GencommP169Reg_252_253_Type = Unsigned32
_GencommP169Reg_252_253_Object = MibTableColumn
gencommP169Reg_252_253 = _GencommP169Reg_252_253_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 128),
    _GencommP169Reg_252_253_Type()
)
gencommP169Reg_252_253.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_252_253.setStatus("current")
_GencommP169Reg_254_255_Type = Unsigned32
_GencommP169Reg_254_255_Object = MibTableColumn
gencommP169Reg_254_255 = _GencommP169Reg_254_255_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 4, 4, 1, 129),
    _GencommP169Reg_254_255_Type()
)
gencommP169Reg_254_255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gencommP169Reg_254_255.setStatus("current")
_BusTable_Object = MibTable
busTable = _BusTable_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9)
)
if mibBuilder.loadTexts:
    busTable.setStatus("current")
_BusTableEntry_Object = MibTableRow
busTableEntry = _BusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1)
)
busTableEntry.setIndexNames(
    (0, "DSE-8610-MIB", "busKeyId"),
)
if mibBuilder.loadTexts:
    busTableEntry.setStatus("current")


class _BusKeyId_Type(Integer32):
    """Custom type busKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BusKeyId_Type.__name__ = "Integer32"
_BusKeyId_Object = MibTableColumn
busKeyId = _BusKeyId_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 1),
    _BusKeyId_Type()
)
busKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    busKeyId.setStatus("current")
_BusFreq_Type = FreqDiv10
_BusFreq_Object = MibTableColumn
busFreq = _BusFreq_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 2),
    _BusFreq_Type()
)
busFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busFreq.setStatus("current")
_BusL1Volts_Type = VoltsLNDiv10
_BusL1Volts_Object = MibTableColumn
busL1Volts = _BusL1Volts_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 3),
    _BusL1Volts_Type()
)
busL1Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busL1Volts.setStatus("current")
_BusL2Volts_Type = VoltsLNDiv10
_BusL2Volts_Object = MibTableColumn
busL2Volts = _BusL2Volts_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 4),
    _BusL2Volts_Type()
)
busL2Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busL2Volts.setStatus("current")
_BusL3Volts_Type = VoltsLNDiv10
_BusL3Volts_Object = MibTableColumn
busL3Volts = _BusL3Volts_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 5),
    _BusL3Volts_Type()
)
busL3Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busL3Volts.setStatus("current")
_BusL1L2Volts_Type = VoltsLLDiv10
_BusL1L2Volts_Object = MibTableColumn
busL1L2Volts = _BusL1L2Volts_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 6),
    _BusL1L2Volts_Type()
)
busL1L2Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busL1L2Volts.setStatus("current")
_BusL2L3Volts_Type = VoltsLLDiv10
_BusL2L3Volts_Object = MibTableColumn
busL2L3Volts = _BusL2L3Volts_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 7),
    _BusL2L3Volts_Type()
)
busL2L3Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busL2L3Volts.setStatus("current")
_BusL3L1Volts_Type = VoltsLLDiv10
_BusL3L1Volts_Object = MibTableColumn
busL3L1Volts = _BusL3L1Volts_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 8),
    _BusL3L1Volts_Type()
)
busL3L1Volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busL3L1Volts.setStatus("current")
_BusL1Current_Type = CurrentDiv10
_BusL1Current_Object = MibTableColumn
busL1Current = _BusL1Current_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 9),
    _BusL1Current_Type()
)
busL1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busL1Current.setStatus("current")
_BusL2Current_Type = CurrentDiv10
_BusL2Current_Object = MibTableColumn
busL2Current = _BusL2Current_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 10),
    _BusL2Current_Type()
)
busL2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busL2Current.setStatus("current")
_BusL3Current_Type = CurrentDiv10
_BusL3Current_Object = MibTableColumn
busL3Current = _BusL3Current_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 11),
    _BusL3Current_Type()
)
busL3Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busL3Current.setStatus("current")
_BusECurrent_Type = CurrentDiv10
_BusECurrent_Object = MibTableColumn
busECurrent = _BusECurrent_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 12),
    _BusECurrent_Type()
)
busECurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busECurrent.setStatus("current")


class _BusL1Watts_Type(Integer32):
    """Custom type busL1Watts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999999999, 999999999),
    )


_BusL1Watts_Type.__name__ = "Integer32"
_BusL1Watts_Object = MibTableColumn
busL1Watts = _BusL1Watts_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 13),
    _BusL1Watts_Type()
)
busL1Watts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busL1Watts.setStatus("current")


class _BusL2Watts_Type(Integer32):
    """Custom type busL2Watts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999999999, 999999999),
    )


_BusL2Watts_Type.__name__ = "Integer32"
_BusL2Watts_Object = MibTableColumn
busL2Watts = _BusL2Watts_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 14),
    _BusL2Watts_Type()
)
busL2Watts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busL2Watts.setStatus("current")


class _BusL3Watts_Type(Integer32):
    """Custom type busL3Watts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999999999, 999999999),
    )


_BusL3Watts_Type.__name__ = "Integer32"
_BusL3Watts_Object = MibTableColumn
busL3Watts = _BusL3Watts_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 15),
    _BusL3Watts_Type()
)
busL3Watts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busL3Watts.setStatus("current")


class _BusRotations_Type(Integer32):
    """Custom type busRotations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_BusRotations_Type.__name__ = "Integer32"
_BusRotations_Object = MibTableColumn
busRotations = _BusRotations_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 16),
    _BusRotations_Type()
)
busRotations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busRotations.setStatus("current")


class _BusWattsTotal_Type(Integer32):
    """Custom type busWattsTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999999999, 999999999),
    )


_BusWattsTotal_Type.__name__ = "Integer32"
_BusWattsTotal_Object = MibTableColumn
busWattsTotal = _BusWattsTotal_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 17),
    _BusWattsTotal_Type()
)
busWattsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busWattsTotal.setStatus("current")


class _BusL1VA_Type(Unsigned32):
    """Custom type busL1VA based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999999),
    )


_BusL1VA_Type.__name__ = "Unsigned32"
_BusL1VA_Object = MibTableColumn
busL1VA = _BusL1VA_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 18),
    _BusL1VA_Type()
)
busL1VA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busL1VA.setStatus("current")


class _BusL2VA_Type(Unsigned32):
    """Custom type busL2VA based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999999),
    )


_BusL2VA_Type.__name__ = "Unsigned32"
_BusL2VA_Object = MibTableColumn
busL2VA = _BusL2VA_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 19),
    _BusL2VA_Type()
)
busL2VA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busL2VA.setStatus("current")


class _BusL3VA_Type(Unsigned32):
    """Custom type busL3VA based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999999),
    )


_BusL3VA_Type.__name__ = "Unsigned32"
_BusL3VA_Object = MibTableColumn
busL3VA = _BusL3VA_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 20),
    _BusL3VA_Type()
)
busL3VA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busL3VA.setStatus("current")


class _BusTotalVA_Type(Unsigned32):
    """Custom type busTotalVA based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999999),
    )


_BusTotalVA_Type.__name__ = "Unsigned32"
_BusTotalVA_Object = MibTableColumn
busTotalVA = _BusTotalVA_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 21),
    _BusTotalVA_Type()
)
busTotalVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busTotalVA.setStatus("current")


class _BusL1VAr_Type(Integer32):
    """Custom type busL1VAr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99999999, 99999999),
    )


_BusL1VAr_Type.__name__ = "Integer32"
_BusL1VAr_Object = MibTableColumn
busL1VAr = _BusL1VAr_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 22),
    _BusL1VAr_Type()
)
busL1VAr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busL1VAr.setStatus("current")


class _BusL2VAr_Type(Integer32):
    """Custom type busL2VAr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99999999, 99999999),
    )


_BusL2VAr_Type.__name__ = "Integer32"
_BusL2VAr_Object = MibTableColumn
busL2VAr = _BusL2VAr_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 23),
    _BusL2VAr_Type()
)
busL2VAr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busL2VAr.setStatus("current")


class _BusL3VAr_Type(Integer32):
    """Custom type busL3VAr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99999999, 99999999),
    )


_BusL3VAr_Type.__name__ = "Integer32"
_BusL3VAr_Object = MibTableColumn
busL3VAr = _BusL3VAr_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 24),
    _BusL3VAr_Type()
)
busL3VAr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busL3VAr.setStatus("current")


class _BusTotalVAr_Type(Integer32):
    """Custom type busTotalVAr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999999999, 999999999),
    )


_BusTotalVAr_Type.__name__ = "Integer32"
_BusTotalVAr_Object = MibTableColumn
busTotalVAr = _BusTotalVAr_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 25),
    _BusTotalVAr_Type()
)
busTotalVAr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busTotalVAr.setStatus("current")
_BusPowerFactorL1_Type = PowerFactorDiv100
_BusPowerFactorL1_Object = MibTableColumn
busPowerFactorL1 = _BusPowerFactorL1_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 26),
    _BusPowerFactorL1_Type()
)
busPowerFactorL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busPowerFactorL1.setStatus("current")
_BusPowerFactorL2_Type = PowerFactorDiv100
_BusPowerFactorL2_Object = MibTableColumn
busPowerFactorL2 = _BusPowerFactorL2_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 27),
    _BusPowerFactorL2_Type()
)
busPowerFactorL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busPowerFactorL2.setStatus("current")
_BusPowerFactorL3_Type = PowerFactorDiv100
_BusPowerFactorL3_Object = MibTableColumn
busPowerFactorL3 = _BusPowerFactorL3_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 28),
    _BusPowerFactorL3_Type()
)
busPowerFactorL3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busPowerFactorL3.setStatus("current")
_BusAvgPowerFactor_Type = PowerFactorDiv100
_BusAvgPowerFactor_Object = MibTableColumn
busAvgPowerFactor = _BusAvgPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 29),
    _BusAvgPowerFactor_Type()
)
busAvgPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busAvgPowerFactor.setStatus("current")
_BusPowerTotalPC_Type = PowerPCDiv10
_BusPowerTotalPC_Object = MibTableColumn
busPowerTotalPC = _BusPowerTotalPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 30),
    _BusPowerTotalPC_Type()
)
busPowerTotalPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busPowerTotalPC.setStatus("current")
_BusVARTotalPC_Type = PowerPCDiv10
_BusVARTotalPC_Object = MibTableColumn
busVARTotalPC = _BusVARTotalPC_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 31),
    _BusVARTotalPC_Type()
)
busVARTotalPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busVARTotalPC.setStatus("current")
_BusVoltageLNAvg_Type = VoltsLNDiv10
_BusVoltageLNAvg_Object = MibTableColumn
busVoltageLNAvg = _BusVoltageLNAvg_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 32),
    _BusVoltageLNAvg_Type()
)
busVoltageLNAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busVoltageLNAvg.setStatus("current")
_BusVoltageLNDiff_Type = VoltsLNDiv10
_BusVoltageLNDiff_Object = MibTableColumn
busVoltageLNDiff = _BusVoltageLNDiff_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 33),
    _BusVoltageLNDiff_Type()
)
busVoltageLNDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busVoltageLNDiff.setStatus("current")
_BusVoltageLNMin_Type = VoltsLNDiv10
_BusVoltageLNMin_Object = MibTableColumn
busVoltageLNMin = _BusVoltageLNMin_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 34),
    _BusVoltageLNMin_Type()
)
busVoltageLNMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busVoltageLNMin.setStatus("current")
_BusVoltageLNMax_Type = VoltsLNDiv10
_BusVoltageLNMax_Object = MibTableColumn
busVoltageLNMax = _BusVoltageLNMax_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 35),
    _BusVoltageLNMax_Type()
)
busVoltageLNMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busVoltageLNMax.setStatus("current")
_BusVoltageLLAvg_Type = VoltsLLDiv10
_BusVoltageLLAvg_Object = MibTableColumn
busVoltageLLAvg = _BusVoltageLLAvg_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 36),
    _BusVoltageLLAvg_Type()
)
busVoltageLLAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busVoltageLLAvg.setStatus("current")
_BusVoltageLLDiff_Type = VoltsLLDiv10
_BusVoltageLLDiff_Object = MibTableColumn
busVoltageLLDiff = _BusVoltageLLDiff_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 37),
    _BusVoltageLLDiff_Type()
)
busVoltageLLDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busVoltageLLDiff.setStatus("current")
_BusVoltageLLMin_Type = VoltsLLDiv10
_BusVoltageLLMin_Object = MibTableColumn
busVoltageLLMin = _BusVoltageLLMin_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 38),
    _BusVoltageLLMin_Type()
)
busVoltageLLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busVoltageLLMin.setStatus("current")
_BusVoltageLLMax_Type = VoltsLLDiv10
_BusVoltageLLMax_Object = MibTableColumn
busVoltageLLMax = _BusVoltageLLMax_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 1, 9, 1, 39),
    _BusVoltageLLMax_Type()
)
busVoltageLLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busVoltageLLMax.setStatus("current")
_Dse8610Control_ObjectIdentity = ObjectIdentity
dse8610Control = _Dse8610Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 2)
)
_DseKeypressTable_Object = MibTable
dseKeypressTable = _DseKeypressTable_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    dseKeypressTable.setStatus("current")
_DseKeypressEntry_Object = MibTableRow
dseKeypressEntry = _DseKeypressEntry_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 2, 1, 1)
)
dseKeypressEntry.setIndexNames(
    (0, "DSE-8610-MIB", "keypressKeyID"),
)
if mibBuilder.loadTexts:
    dseKeypressEntry.setStatus("current")


class _KeypressKeyID_Type(Integer32):
    """Custom type keypressKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_KeypressKeyID_Type.__name__ = "Integer32"
_KeypressKeyID_Object = MibTableColumn
keypressKeyID = _KeypressKeyID_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 2, 1, 1, 1),
    _KeypressKeyID_Type()
)
keypressKeyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    keypressKeyID.setStatus("current")
_Keypress_Type = OctetString
_Keypress_Object = MibTableColumn
keypress = _Keypress_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 2, 1, 1, 2),
    _Keypress_Type()
)
keypress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keypress.setStatus("current")
_SnmpMIBConformance_ObjectIdentity = ObjectIdentity
snmpMIBConformance = _SnmpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 100)
)
_SnmpMIBCompliances_ObjectIdentity = ObjectIdentity
snmpMIBCompliances = _SnmpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 100, 1)
)
_SnmpMIBGroups_ObjectIdentity = ObjectIdentity
snmpMIBGroups = _SnmpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 100, 2)
)
_Dse8610AlarmsMngr_ObjectIdentity = ObjectIdentity
dse8610AlarmsMngr = _Dse8610AlarmsMngr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 150)
)
_Dse8610AlarmStateTable_Object = MibTable
dse8610AlarmStateTable = _Dse8610AlarmStateTable_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 150, 1)
)
if mibBuilder.loadTexts:
    dse8610AlarmStateTable.setStatus("current")
_Dse8610AlarmStateEntry_Object = MibTableRow
dse8610AlarmStateEntry = _Dse8610AlarmStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 150, 1, 1)
)
dse8610AlarmStateEntry.setIndexNames(
    (0, "DSE-8610-MIB", "dse8610AlarmKeyID"),
)
if mibBuilder.loadTexts:
    dse8610AlarmStateEntry.setStatus("current")


class _Dse8610AlarmKeyID_Type(Integer32):
    """Custom type dse8610AlarmKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Dse8610AlarmKeyID_Type.__name__ = "Integer32"
_Dse8610AlarmKeyID_Object = MibTableColumn
dse8610AlarmKeyID = _Dse8610AlarmKeyID_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 150, 1, 1, 1),
    _Dse8610AlarmKeyID_Type()
)
dse8610AlarmKeyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dse8610AlarmKeyID.setStatus("current")
_Dse8610SeqNr_Type = Counter32
_Dse8610SeqNr_Object = MibTableColumn
dse8610SeqNr = _Dse8610SeqNr_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 150, 1, 1, 2),
    _Dse8610SeqNr_Type()
)
dse8610SeqNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dse8610SeqNr.setStatus("current")


class _Dse8610TrapID_Type(Integer32):
    """Custom type dse8610TrapID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 28671),
    )


_Dse8610TrapID_Type.__name__ = "Integer32"
_Dse8610TrapID_Object = MibTableColumn
dse8610TrapID = _Dse8610TrapID_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 150, 1, 1, 3),
    _Dse8610TrapID_Type()
)
dse8610TrapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dse8610TrapID.setStatus("current")


class _Dse8610TrapState_Type(Integer32):
    """Custom type dse8610TrapState based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("alarmNormal", 1),
          ("alarmWarning", 2),
          ("alarmElectricalTrip", 3),
          ("alarmShutdown", 4),
          ("modeStop", 5),
          ("modeManual", 6),
          ("modeTest", 7),
          ("modeAuto", 8),
          ("modeConfig", 9),
          ("singleEventNotification", 10),
          ("ecuLampOff", 11),
          ("ecuLampFlashSlow", 12),
          ("ecuLampFlashFast", 13),
          ("ecuLampOnSteady", 14),
          ("fuelLevelUsageNormal", 15),
          ("fuelLevelEndFill", 16),
          ("fuelLevelStartFill", 17),
          ("fuelLevelUsageTheftAlarm", 18),
          ("fuelLevelUsageLevelAlarm", 19))
    )


_Dse8610TrapState_Type.__name__ = "Integer32"
_Dse8610TrapState_Object = MibTableColumn
dse8610TrapState = _Dse8610TrapState_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 150, 1, 1, 4),
    _Dse8610TrapState_Type()
)
dse8610TrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dse8610TrapState.setStatus("current")
_Dse8610TrapTimeStamp_Type = TimeTicks
_Dse8610TrapTimeStamp_Object = MibTableColumn
dse8610TrapTimeStamp = _Dse8610TrapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 150, 1, 1, 6),
    _Dse8610TrapTimeStamp_Type()
)
dse8610TrapTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dse8610TrapTimeStamp.setStatus("current")

# Managed Objects groups

generatorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 100, 2, 2)
)
generatorGroup.setObjects(
      *(("DSE-8610-MIB", "genFreq"),
        ("DSE-8610-MIB", "genL1Volts"),
        ("DSE-8610-MIB", "genL2Volts"),
        ("DSE-8610-MIB", "genL3Volts"),
        ("DSE-8610-MIB", "genL1L2Volts"),
        ("DSE-8610-MIB", "genL2L3Volts"),
        ("DSE-8610-MIB", "genL3L1Volts"),
        ("DSE-8610-MIB", "genL1Current"),
        ("DSE-8610-MIB", "genL2Current"),
        ("DSE-8610-MIB", "genL3Current"),
        ("DSE-8610-MIB", "genECurrent"),
        ("DSE-8610-MIB", "genL1Watts"),
        ("DSE-8610-MIB", "genL2Watts"),
        ("DSE-8610-MIB", "genL3Watts"),
        ("DSE-8610-MIB", "genRotation"),
        ("DSE-8610-MIB", "genWattsTotal"),
        ("DSE-8610-MIB", "genL1VA"),
        ("DSE-8610-MIB", "genL2VA"),
        ("DSE-8610-MIB", "genL3VA"),
        ("DSE-8610-MIB", "genTotalVA"),
        ("DSE-8610-MIB", "genL1VAr"),
        ("DSE-8610-MIB", "genL2VAr"),
        ("DSE-8610-MIB", "genL3VAr"),
        ("DSE-8610-MIB", "genTotalVAr"),
        ("DSE-8610-MIB", "genPowerFactorL1"),
        ("DSE-8610-MIB", "genPowerFactorL2"),
        ("DSE-8610-MIB", "genPowerFactorL3"),
        ("DSE-8610-MIB", "genAvgPowerFactor"),
        ("DSE-8610-MIB", "genPowerTotalPC"),
        ("DSE-8610-MIB", "genVARTotalPC"),
        ("DSE-8610-MIB", "genPhase1"),
        ("DSE-8610-MIB", "genPhase2"),
        ("DSE-8610-MIB", "genPhase3"),
        ("DSE-8610-MIB", "genPhaseTotal"),
        ("DSE-8610-MIB", "genPowerL1PC"),
        ("DSE-8610-MIB", "genPowerL2PC"),
        ("DSE-8610-MIB", "genPowerL3PC"),
        ("DSE-8610-MIB", "genVoltageLNAvg"),
        ("DSE-8610-MIB", "genVoltageLNDiff"),
        ("DSE-8610-MIB", "genVoltageLNMin"),
        ("DSE-8610-MIB", "genVoltageLNMax"),
        ("DSE-8610-MIB", "genVoltageLLAvg"),
        ("DSE-8610-MIB", "genVoltageLLDiff"),
        ("DSE-8610-MIB", "genVoltageLLMin"),
        ("DSE-8610-MIB", "genVoltageLLMax"),
        ("DSE-8610-MIB", "genCurrentAve"),
        ("DSE-8610-MIB", "genCurrentDif"),
        ("DSE-8610-MIB", "genCurrentMin"),
        ("DSE-8610-MIB", "genCurrentMax"),
        ("DSE-8610-MIB", "genPowerTotalAvgPC"),
        ("DSE-8610-MIB", "genPowerTotalDiffPC"),
        ("DSE-8610-MIB", "genPowerTotalMinPC"),
        ("DSE-8610-MIB", "genPowerTotalMaxPC"),
        ("DSE-8610-MIB", "genVATotalAvgPC"),
        ("DSE-8610-MIB", "genVADiffPC"),
        ("DSE-8610-MIB", "genVAMinPC"),
        ("DSE-8610-MIB", "genVAMaxPC"),
        ("DSE-8610-MIB", "genVARTotalAvgPC"),
        ("DSE-8610-MIB", "genVARDiffPC"),
        ("DSE-8610-MIB", "genVARMinPC"),
        ("DSE-8610-MIB", "genVARMaxPC"),
        ("DSE-8610-MIB", "genPFTotalAvgPC"),
        ("DSE-8610-MIB", "genPFDiffPC"),
        ("DSE-8610-MIB", "genPFMinPC"),
        ("DSE-8610-MIB", "genPFMaxPC"))
)
if mibBuilder.loadTexts:
    generatorGroup.setStatus("current")

engineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 100, 2, 3)
)
engineGroup.setObjects(
      *(("DSE-8610-MIB", "engOilPress"),
        ("DSE-8610-MIB", "engTemp"),
        ("DSE-8610-MIB", "engOilTemp"),
        ("DSE-8610-MIB", "engFuelLevel"),
        ("DSE-8610-MIB", "engChargeAltVolts"),
        ("DSE-8610-MIB", "engBatteryVolts"),
        ("DSE-8610-MIB", "engSpeedDisplay"),
        ("DSE-8610-MIB", "engCoolantP1"),
        ("DSE-8610-MIB", "engCoolantP2"),
        ("DSE-8610-MIB", "engFuelP1"),
        ("DSE-8610-MIB", "engFuelP2"),
        ("DSE-8610-MIB", "engTurboP1"),
        ("DSE-8610-MIB", "engTurboP2"),
        ("DSE-8610-MIB", "engInMainfoldT1"),
        ("DSE-8610-MIB", "engInMainfoldT2"),
        ("DSE-8610-MIB", "engExhaustT1"),
        ("DSE-8610-MIB", "engExhaustT2"),
        ("DSE-8610-MIB", "engFuelConsumption"),
        ("DSE-8610-MIB", "engWaterInFuel"),
        ("DSE-8610-MIB", "engCANBitData"),
        ("DSE-8610-MIB", "engAtmosphericP"),
        ("DSE-8610-MIB", "engFuelT"),
        ("DSE-8610-MIB", "engFuelLevelUnits"),
        ("DSE-8610-MIB", "engTankFuelUnits"),
        ("DSE-8610-MIB", "engAfttrt1FuelUSed"),
        ("DSE-8610-MIB", "engAfttrt1ExGasT1"),
        ("DSE-8610-MIB", "engAfttrt1ExGasT3"),
        ("DSE-8610-MIB", "engRefTorque"),
        ("DSE-8610-MIB", "engPerTorque"),
        ("DSE-8610-MIB", "engDemandPerTorque"),
        ("DSE-8610-MIB", "engPCLoadAtSpeed"),
        ("DSE-8610-MIB", "engAccelPedalPos"),
        ("DSE-8610-MIB", "engNomFricPerTorque"),
        ("DSE-8610-MIB", "engOilLevel"),
        ("DSE-8610-MIB", "engCrankCasePress"),
        ("DSE-8610-MIB", "engCoolantLevel"),
        ("DSE-8610-MIB", "engInjectorRail1"),
        ("DSE-8610-MIB", "engInjectorRail2"),
        ("DSE-8610-MIB", "engEgrFlowRate"),
        ("DSE-8610-MIB", "engPreFilOilPress"),
        ("DSE-8610-MIB", "engInstBreakPower"),
        ("DSE-8610-MIB", "engExhGasPort1Temp"),
        ("DSE-8610-MIB", "engExhGasPort2Temp"),
        ("DSE-8610-MIB", "engExhGasPort3Temp"),
        ("DSE-8610-MIB", "engExhGasPort4Temp"),
        ("DSE-8610-MIB", "engExhGasPort5Temp"),
        ("DSE-8610-MIB", "engExhGasPort6Temp"),
        ("DSE-8610-MIB", "engExhGasPort7Temp"),
        ("DSE-8610-MIB", "engExhGasPort8Temp"),
        ("DSE-8610-MIB", "engExhGasPort9Temp"),
        ("DSE-8610-MIB", "engExhGasPort10Temp"),
        ("DSE-8610-MIB", "engExhGasPort11Temp"),
        ("DSE-8610-MIB", "engExhGasPort12Temp"),
        ("DSE-8610-MIB", "engExhGasPort13Temp"),
        ("DSE-8610-MIB", "engExhGasPort14Temp"),
        ("DSE-8610-MIB", "engExhGasPort15Temp"),
        ("DSE-8610-MIB", "engExhGasPort16Temp"),
        ("DSE-8610-MIB", "engIntercoolerTemp"),
        ("DSE-8610-MIB", "engTurboOilTemp"),
        ("DSE-8610-MIB", "engECUTemp"),
        ("DSE-8610-MIB", "engFanSpeed"),
        ("DSE-8610-MIB", "engTotalRev"),
        ("DSE-8610-MIB", "engAirInPress"),
        ("DSE-8610-MIB", "engAirFilDiffPres"),
        ("DSE-8610-MIB", "engTrapInPress"),
        ("DSE-8610-MIB", "engTurboP3"),
        ("DSE-8610-MIB", "engTurboP4"),
        ("DSE-8610-MIB", "engInMainfoldT3"),
        ("DSE-8610-MIB", "engInMainfoldT4"),
        ("DSE-8610-MIB", "engInMainfoldT5"),
        ("DSE-8610-MIB", "engInMainfoldT6"),
        ("DSE-8610-MIB", "engTripFuel"),
        ("DSE-8610-MIB", "engElectPotential"),
        ("DSE-8610-MIB", "engPGIEngType"),
        ("DSE-8610-MIB", "engPGIVerNum"),
        ("DSE-8610-MIB", "engDPTCFilLampCmd"),
        ("DSE-8610-MIB", "engExhSysHighTemp"),
        ("DSE-8610-MIB", "engDPTCActRegFor"),
        ("DSE-8610-MIB", "engSDWNWaitStart"),
        ("DSE-8610-MIB", "engSDWNProtection"),
        ("DSE-8610-MIB", "engSDWNApproaching"),
        ("DSE-8610-MIB", "engOperatingState"),
        ("DSE-8610-MIB", "engSDWNClOverride"),
        ("DSE-8610-MIB", "engBattleshortOvr"),
        ("DSE-8610-MIB", "engModHours"),
        ("DSE-8610-MIB", "engModOilPress"),
        ("DSE-8610-MIB", "engModCoolTemp"),
        ("DSE-8610-MIB", "engModRPM"),
        ("DSE-8610-MIB", "engModChargeAlt"),
        ("DSE-8610-MIB", "engModSpeedFeed"),
        ("DSE-8610-MIB", "engModFreqAdj"),
        ("DSE-8610-MIB", "engAlarmWarn"),
        ("DSE-8610-MIB", "engAlarmShdwn"),
        ("DSE-8610-MIB", "engAlarmElectr"),
        ("DSE-8610-MIB", "engAmberStopLamp"),
        ("DSE-8610-MIB", "engAmberLampFlash"),
        ("DSE-8610-MIB", "engRedStopLamp"),
        ("DSE-8610-MIB", "engRedLampFlash"),
        ("DSE-8610-MIB", "engProtLamp"),
        ("DSE-8610-MIB", "engProtLampFlash"),
        ("DSE-8610-MIB", "engMalfLamp"),
        ("DSE-8610-MIB", "engMalfLampFlash"),
        ("DSE-8610-MIB", "engBattSwitched"),
        ("DSE-8610-MIB", "engChargPotential"),
        ("DSE-8610-MIB", "engCharAltCurr"),
        ("DSE-8610-MIB", "engBattCurr"),
        ("DSE-8610-MIB", "engTorqueMode"),
        ("DSE-8610-MIB", "engStarterMode"),
        ("DSE-8610-MIB", "engCIStatus"),
        ("DSE-8610-MIB", "engDemandedSpeed"),
        ("DSE-8610-MIB", "engSpeedFBUp"),
        ("DSE-8610-MIB", "engSpeedFBDown"),
        ("DSE-8610-MIB", "engSpeedFailMode"),
        ("DSE-8610-MIB", "engCurrSDSrc"),
        ("DSE-8610-MIB", "engFbackSDCAN"),
        ("DSE-8610-MIB", "engFbackSDAnalog"),
        ("DSE-8610-MIB", "engFailureCodes"),
        ("DSE-8610-MIB", "engActDrop"),
        ("DSE-8610-MIB", "engStartStatus"),
        ("DSE-8610-MIB", "engProtOrStatus"),
        ("DSE-8610-MIB", "engMTURuniingState"),
        ("DSE-8610-MIB", "engCylCutOff"),
        ("DSE-8610-MIB", "engLoadGenStatus"),
        ("DSE-8610-MIB", "engEtxStopState"),
        ("DSE-8610-MIB", "engCurrOPMode"),
        ("DSE-8610-MIB", "engMTUReqTorque"),
        ("DSE-8610-MIB", "engTripAvgFuel"),
        ("DSE-8610-MIB", "engECURatedPower"),
        ("DSE-8610-MIB", "engECURatedSpeed"),
        ("DSE-8610-MIB", "engECUIdleSpeed"),
        ("DSE-8610-MIB", "engECUDesirSpeed"),
        ("DSE-8610-MIB", "engECUPreheatStat"),
        ("DSE-8610-MIB", "engManiFoldPres"),
        ("DSE-8610-MIB", "engIntercoolerLevel"),
        ("DSE-8610-MIB", "engCANLinkState"),
        ("DSE-8610-MIB", "engAutoDFPRegInh"),
        ("DSE-8610-MIB", "engDPTCActRegInhSwitch"),
        ("DSE-8610-MIB", "engSootLoadPC"),
        ("DSE-8610-MIB", "engAshLoadPC"),
        ("DSE-8610-MIB", "engDefTankLevel"),
        ("DSE-8610-MIB", "engDefTankTemp"),
        ("DSE-8610-MIB", "engDefLevelWarn"),
        ("DSE-8610-MIB", "engDefReagentCons"),
        ("DSE-8610-MIB", "engDefInducReason"),
        ("DSE-8610-MIB", "engDefInducSever"),
        ("DSE-8610-MIB", "engDefCounterMin"),
        ("DSE-8610-MIB", "engTLTTorqueReduc"),
        ("DSE-8610-MIB", "engTLTVehspdReduc"),
        ("DSE-8610-MIB", "engEGRPress"),
        ("DSE-8610-MIB", "engEGRTemp"),
        ("DSE-8610-MIB", "engAmbAirTemp"),
        ("DSE-8610-MIB", "engAirIntakeTemp"),
        ("DSE-8610-MIB", "engSRCOperatInduc"),
        ("DSE-8610-MIB", "engTankLevLowLost"),
        ("DSE-8610-MIB", "engMiscAltSpeedSel"),
        ("DSE-8610-MIB", "engExhGasP17Temp"),
        ("DSE-8610-MIB", "engExhGasP18Temp"),
        ("DSE-8610-MIB", "engExhGasP19Temp"),
        ("DSE-8610-MIB", "engExhGasP20Temp"),
        ("DSE-8610-MIB", "engInstFuelRate"),
        ("DSE-8610-MIB", "engDPTCFiltStat"),
        ("DSE-8610-MIB", "engDPTCActRegInh"),
        ("DSE-8610-MIB", "engDPTCActRegInhEt"),
        ("DSE-8610-MIB", "engDefTankStat"),
        ("DSE-8610-MIB", "engFuelGasPress"),
        ("DSE-8610-MIB", "engThrotPos1"),
        ("DSE-8610-MIB", "engThrotPos2"))
)
if mibBuilder.loadTexts:
    engineGroup.setStatus("current")

busGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 100, 2, 4)
)
busGroup.setObjects(
      *(("DSE-8610-MIB", "busFreq"),
        ("DSE-8610-MIB", "busL1Volts"),
        ("DSE-8610-MIB", "busL2Volts"),
        ("DSE-8610-MIB", "busL3Volts"),
        ("DSE-8610-MIB", "busL1L2Volts"),
        ("DSE-8610-MIB", "busL2L3Volts"),
        ("DSE-8610-MIB", "busL3L1Volts"),
        ("DSE-8610-MIB", "busL1Current"),
        ("DSE-8610-MIB", "busL2Current"),
        ("DSE-8610-MIB", "busL3Current"),
        ("DSE-8610-MIB", "busECurrent"),
        ("DSE-8610-MIB", "busL1Watts"),
        ("DSE-8610-MIB", "busL2Watts"),
        ("DSE-8610-MIB", "busL3Watts"),
        ("DSE-8610-MIB", "busRotations"),
        ("DSE-8610-MIB", "busWattsTotal"),
        ("DSE-8610-MIB", "busL1VA"),
        ("DSE-8610-MIB", "busL2VA"),
        ("DSE-8610-MIB", "busL3VA"),
        ("DSE-8610-MIB", "busTotalVA"),
        ("DSE-8610-MIB", "busL1VAr"),
        ("DSE-8610-MIB", "busL2VAr"),
        ("DSE-8610-MIB", "busL3VAr"),
        ("DSE-8610-MIB", "busTotalVAr"),
        ("DSE-8610-MIB", "busPowerFactorL1"),
        ("DSE-8610-MIB", "busPowerFactorL2"),
        ("DSE-8610-MIB", "busPowerFactorL3"),
        ("DSE-8610-MIB", "busAvgPowerFactor"),
        ("DSE-8610-MIB", "busPowerTotalPC"),
        ("DSE-8610-MIB", "busVARTotalPC"),
        ("DSE-8610-MIB", "busVoltageLNAvg"),
        ("DSE-8610-MIB", "busVoltageLNDiff"),
        ("DSE-8610-MIB", "busVoltageLNMin"),
        ("DSE-8610-MIB", "busVoltageLNMax"),
        ("DSE-8610-MIB", "busVoltageLLAvg"),
        ("DSE-8610-MIB", "busVoltageLLDiff"),
        ("DSE-8610-MIB", "busVoltageLLMin"),
        ("DSE-8610-MIB", "busVoltageLLMax"))
)
if mibBuilder.loadTexts:
    busGroup.setStatus("current")

gencommP166Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 100, 2, 5)
)
gencommP166Group.setObjects(
      *(("DSE-8610-MIB", "gencommP166Reg-0-1"),
        ("DSE-8610-MIB", "gencommP166Reg-2-3"),
        ("DSE-8610-MIB", "gencommP166Reg-4-5"),
        ("DSE-8610-MIB", "gencommP166Reg-6-7"),
        ("DSE-8610-MIB", "gencommP166Reg-8-9"),
        ("DSE-8610-MIB", "gencommP166Reg-10-11"),
        ("DSE-8610-MIB", "gencommP166Reg-12-13"),
        ("DSE-8610-MIB", "gencommP166Reg-14-15"),
        ("DSE-8610-MIB", "gencommP166Reg-16-17"),
        ("DSE-8610-MIB", "gencommP166Reg-18-19"),
        ("DSE-8610-MIB", "gencommP166Reg-20-21"),
        ("DSE-8610-MIB", "gencommP166Reg-22-23"),
        ("DSE-8610-MIB", "gencommP166Reg-24-25"),
        ("DSE-8610-MIB", "gencommP166Reg-26-27"),
        ("DSE-8610-MIB", "gencommP166Reg-28-29"),
        ("DSE-8610-MIB", "gencommP166Reg-30-31"),
        ("DSE-8610-MIB", "gencommP166Reg-32-33"),
        ("DSE-8610-MIB", "gencommP166Reg-34-35"),
        ("DSE-8610-MIB", "gencommP166Reg-36-37"),
        ("DSE-8610-MIB", "gencommP166Reg-38-39"),
        ("DSE-8610-MIB", "gencommP166Reg-40-41"),
        ("DSE-8610-MIB", "gencommP166Reg-42-43"),
        ("DSE-8610-MIB", "gencommP166Reg-44-45"),
        ("DSE-8610-MIB", "gencommP166Reg-46-47"),
        ("DSE-8610-MIB", "gencommP166Reg-48-49"),
        ("DSE-8610-MIB", "gencommP166Reg-50-51"),
        ("DSE-8610-MIB", "gencommP166Reg-52-53"),
        ("DSE-8610-MIB", "gencommP166Reg-54-55"),
        ("DSE-8610-MIB", "gencommP166Reg-56-57"),
        ("DSE-8610-MIB", "gencommP166Reg-58-59"),
        ("DSE-8610-MIB", "gencommP166Reg-60-61"),
        ("DSE-8610-MIB", "gencommP166Reg-62-63"),
        ("DSE-8610-MIB", "gencommP166Reg-64-65"),
        ("DSE-8610-MIB", "gencommP166Reg-66-67"),
        ("DSE-8610-MIB", "gencommP166Reg-68-69"),
        ("DSE-8610-MIB", "gencommP166Reg-70-71"),
        ("DSE-8610-MIB", "gencommP166Reg-72-73"),
        ("DSE-8610-MIB", "gencommP166Reg-74-75"),
        ("DSE-8610-MIB", "gencommP166Reg-76-77"),
        ("DSE-8610-MIB", "gencommP166Reg-78-79"),
        ("DSE-8610-MIB", "gencommP166Reg-80-81"),
        ("DSE-8610-MIB", "gencommP166Reg-82-83"),
        ("DSE-8610-MIB", "gencommP166Reg-84-85"),
        ("DSE-8610-MIB", "gencommP166Reg-86-87"),
        ("DSE-8610-MIB", "gencommP166Reg-88-89"),
        ("DSE-8610-MIB", "gencommP166Reg-90-91"),
        ("DSE-8610-MIB", "gencommP166Reg-92-93"),
        ("DSE-8610-MIB", "gencommP166Reg-94-95"),
        ("DSE-8610-MIB", "gencommP166Reg-96-97"),
        ("DSE-8610-MIB", "gencommP166Reg-98-99"),
        ("DSE-8610-MIB", "gencommP166Reg-100-101"),
        ("DSE-8610-MIB", "gencommP166Reg-102-103"),
        ("DSE-8610-MIB", "gencommP166Reg-104-105"),
        ("DSE-8610-MIB", "gencommP166Reg-106-107"),
        ("DSE-8610-MIB", "gencommP166Reg-108-109"),
        ("DSE-8610-MIB", "gencommP166Reg-110-111"),
        ("DSE-8610-MIB", "gencommP166Reg-112-113"),
        ("DSE-8610-MIB", "gencommP166Reg-114-115"),
        ("DSE-8610-MIB", "gencommP166Reg-116-117"),
        ("DSE-8610-MIB", "gencommP166Reg-118-119"),
        ("DSE-8610-MIB", "gencommP166Reg-120-121"),
        ("DSE-8610-MIB", "gencommP166Reg-122-123"),
        ("DSE-8610-MIB", "gencommP166Reg-124-125"),
        ("DSE-8610-MIB", "gencommP166Reg-126-127"),
        ("DSE-8610-MIB", "gencommP166Reg-128-129"),
        ("DSE-8610-MIB", "gencommP166Reg-130-131"),
        ("DSE-8610-MIB", "gencommP166Reg-132-133"),
        ("DSE-8610-MIB", "gencommP166Reg-134-135"),
        ("DSE-8610-MIB", "gencommP166Reg-136-137"),
        ("DSE-8610-MIB", "gencommP166Reg-138-139"),
        ("DSE-8610-MIB", "gencommP166Reg-140-141"),
        ("DSE-8610-MIB", "gencommP166Reg-142-143"),
        ("DSE-8610-MIB", "gencommP166Reg-144-145"),
        ("DSE-8610-MIB", "gencommP166Reg-146-147"),
        ("DSE-8610-MIB", "gencommP166Reg-148-149"),
        ("DSE-8610-MIB", "gencommP166Reg-150-151"),
        ("DSE-8610-MIB", "gencommP166Reg-152-153"),
        ("DSE-8610-MIB", "gencommP166Reg-154-155"),
        ("DSE-8610-MIB", "gencommP166Reg-156-157"),
        ("DSE-8610-MIB", "gencommP166Reg-158-159"),
        ("DSE-8610-MIB", "gencommP166Reg-160-161"),
        ("DSE-8610-MIB", "gencommP166Reg-162-163"),
        ("DSE-8610-MIB", "gencommP166Reg-164-165"),
        ("DSE-8610-MIB", "gencommP166Reg-166-167"),
        ("DSE-8610-MIB", "gencommP166Reg-168-169"),
        ("DSE-8610-MIB", "gencommP166Reg-170-171"),
        ("DSE-8610-MIB", "gencommP166Reg-172-173"),
        ("DSE-8610-MIB", "gencommP166Reg-174-175"),
        ("DSE-8610-MIB", "gencommP166Reg-176-177"),
        ("DSE-8610-MIB", "gencommP166Reg-178-179"),
        ("DSE-8610-MIB", "gencommP166Reg-180-181"),
        ("DSE-8610-MIB", "gencommP166Reg-182-183"),
        ("DSE-8610-MIB", "gencommP166Reg-184-185"),
        ("DSE-8610-MIB", "gencommP166Reg-186-187"),
        ("DSE-8610-MIB", "gencommP166Reg-188-189"),
        ("DSE-8610-MIB", "gencommP166Reg-190-191"),
        ("DSE-8610-MIB", "gencommP166Reg-192-193"),
        ("DSE-8610-MIB", "gencommP166Reg-194-195"),
        ("DSE-8610-MIB", "gencommP166Reg-196-197"),
        ("DSE-8610-MIB", "gencommP166Reg-198-199"),
        ("DSE-8610-MIB", "gencommP166Reg-200-201"),
        ("DSE-8610-MIB", "gencommP166Reg-202-203"),
        ("DSE-8610-MIB", "gencommP166Reg-204-205"),
        ("DSE-8610-MIB", "gencommP166Reg-206-207"),
        ("DSE-8610-MIB", "gencommP166Reg-208-209"),
        ("DSE-8610-MIB", "gencommP166Reg-210-211"),
        ("DSE-8610-MIB", "gencommP166Reg-212-213"),
        ("DSE-8610-MIB", "gencommP166Reg-214-215"),
        ("DSE-8610-MIB", "gencommP166Reg-216-217"),
        ("DSE-8610-MIB", "gencommP166Reg-218-219"),
        ("DSE-8610-MIB", "gencommP166Reg-220-221"),
        ("DSE-8610-MIB", "gencommP166Reg-222-223"),
        ("DSE-8610-MIB", "gencommP166Reg-224-225"),
        ("DSE-8610-MIB", "gencommP166Reg-226-227"),
        ("DSE-8610-MIB", "gencommP166Reg-228-229"),
        ("DSE-8610-MIB", "gencommP166Reg-230-231"),
        ("DSE-8610-MIB", "gencommP166Reg-232-233"),
        ("DSE-8610-MIB", "gencommP166Reg-234-235"),
        ("DSE-8610-MIB", "gencommP166Reg-236-237"),
        ("DSE-8610-MIB", "gencommP166Reg-238-239"),
        ("DSE-8610-MIB", "gencommP166Reg-240-241"),
        ("DSE-8610-MIB", "gencommP166Reg-242-243"),
        ("DSE-8610-MIB", "gencommP166Reg-244-245"),
        ("DSE-8610-MIB", "gencommP166Reg-246-247"),
        ("DSE-8610-MIB", "gencommP166Reg-248-249"),
        ("DSE-8610-MIB", "gencommP166Reg-250-251"),
        ("DSE-8610-MIB", "gencommP166Reg-252-253"),
        ("DSE-8610-MIB", "gencommP166Reg-254-255"))
)
if mibBuilder.loadTexts:
    gencommP166Group.setStatus("current")

gencommP167Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 100, 2, 6)
)
gencommP167Group.setObjects(
      *(("DSE-8610-MIB", "gencommP167Reg-0-1"),
        ("DSE-8610-MIB", "gencommP167Reg-2-3"),
        ("DSE-8610-MIB", "gencommP167Reg-4-5"),
        ("DSE-8610-MIB", "gencommP167Reg-6-7"),
        ("DSE-8610-MIB", "gencommP167Reg-8-9"),
        ("DSE-8610-MIB", "gencommP167Reg-10-11"),
        ("DSE-8610-MIB", "gencommP167Reg-12-13"),
        ("DSE-8610-MIB", "gencommP167Reg-14-15"),
        ("DSE-8610-MIB", "gencommP167Reg-16-17"),
        ("DSE-8610-MIB", "gencommP167Reg-18-19"),
        ("DSE-8610-MIB", "gencommP167Reg-20-21"),
        ("DSE-8610-MIB", "gencommP167Reg-22-23"),
        ("DSE-8610-MIB", "gencommP167Reg-24-25"),
        ("DSE-8610-MIB", "gencommP167Reg-26-27"),
        ("DSE-8610-MIB", "gencommP167Reg-28-29"),
        ("DSE-8610-MIB", "gencommP167Reg-30-31"),
        ("DSE-8610-MIB", "gencommP167Reg-32-33"),
        ("DSE-8610-MIB", "gencommP167Reg-34-35"),
        ("DSE-8610-MIB", "gencommP167Reg-36-37"),
        ("DSE-8610-MIB", "gencommP167Reg-38-39"),
        ("DSE-8610-MIB", "gencommP167Reg-40-41"),
        ("DSE-8610-MIB", "gencommP167Reg-42-43"),
        ("DSE-8610-MIB", "gencommP167Reg-44-45"),
        ("DSE-8610-MIB", "gencommP167Reg-46-47"),
        ("DSE-8610-MIB", "gencommP167Reg-48-49"),
        ("DSE-8610-MIB", "gencommP167Reg-50-51"),
        ("DSE-8610-MIB", "gencommP167Reg-52-53"),
        ("DSE-8610-MIB", "gencommP167Reg-54-55"),
        ("DSE-8610-MIB", "gencommP167Reg-56-57"),
        ("DSE-8610-MIB", "gencommP167Reg-58-59"),
        ("DSE-8610-MIB", "gencommP167Reg-60-61"),
        ("DSE-8610-MIB", "gencommP167Reg-62-63"),
        ("DSE-8610-MIB", "gencommP167Reg-64-65"),
        ("DSE-8610-MIB", "gencommP167Reg-66-67"),
        ("DSE-8610-MIB", "gencommP167Reg-68-69"),
        ("DSE-8610-MIB", "gencommP167Reg-70-71"),
        ("DSE-8610-MIB", "gencommP167Reg-72-73"),
        ("DSE-8610-MIB", "gencommP167Reg-74-75"),
        ("DSE-8610-MIB", "gencommP167Reg-76-77"),
        ("DSE-8610-MIB", "gencommP167Reg-78-79"),
        ("DSE-8610-MIB", "gencommP167Reg-80-81"),
        ("DSE-8610-MIB", "gencommP167Reg-82-83"),
        ("DSE-8610-MIB", "gencommP167Reg-84-85"),
        ("DSE-8610-MIB", "gencommP167Reg-86-87"),
        ("DSE-8610-MIB", "gencommP167Reg-88-89"),
        ("DSE-8610-MIB", "gencommP167Reg-90-91"),
        ("DSE-8610-MIB", "gencommP167Reg-92-93"),
        ("DSE-8610-MIB", "gencommP167Reg-94-95"),
        ("DSE-8610-MIB", "gencommP167Reg-96-97"),
        ("DSE-8610-MIB", "gencommP167Reg-98-99"),
        ("DSE-8610-MIB", "gencommP167Reg-100-101"),
        ("DSE-8610-MIB", "gencommP167Reg-102-103"),
        ("DSE-8610-MIB", "gencommP167Reg-104-105"),
        ("DSE-8610-MIB", "gencommP167Reg-106-107"),
        ("DSE-8610-MIB", "gencommP167Reg-108-109"),
        ("DSE-8610-MIB", "gencommP167Reg-110-111"),
        ("DSE-8610-MIB", "gencommP167Reg-112-113"),
        ("DSE-8610-MIB", "gencommP167Reg-114-115"),
        ("DSE-8610-MIB", "gencommP167Reg-116-117"),
        ("DSE-8610-MIB", "gencommP167Reg-118-119"),
        ("DSE-8610-MIB", "gencommP167Reg-120-121"),
        ("DSE-8610-MIB", "gencommP167Reg-122-123"),
        ("DSE-8610-MIB", "gencommP167Reg-124-125"),
        ("DSE-8610-MIB", "gencommP167Reg-126-127"),
        ("DSE-8610-MIB", "gencommP167Reg-128-129"),
        ("DSE-8610-MIB", "gencommP167Reg-130-131"),
        ("DSE-8610-MIB", "gencommP167Reg-132-133"),
        ("DSE-8610-MIB", "gencommP167Reg-134-135"),
        ("DSE-8610-MIB", "gencommP167Reg-136-137"),
        ("DSE-8610-MIB", "gencommP167Reg-138-139"),
        ("DSE-8610-MIB", "gencommP167Reg-140-141"),
        ("DSE-8610-MIB", "gencommP167Reg-142-143"),
        ("DSE-8610-MIB", "gencommP167Reg-144-145"),
        ("DSE-8610-MIB", "gencommP167Reg-146-147"),
        ("DSE-8610-MIB", "gencommP167Reg-148-149"),
        ("DSE-8610-MIB", "gencommP167Reg-150-151"),
        ("DSE-8610-MIB", "gencommP167Reg-152-153"),
        ("DSE-8610-MIB", "gencommP167Reg-154-155"),
        ("DSE-8610-MIB", "gencommP167Reg-156-157"),
        ("DSE-8610-MIB", "gencommP167Reg-158-159"),
        ("DSE-8610-MIB", "gencommP167Reg-160-161"),
        ("DSE-8610-MIB", "gencommP167Reg-162-163"),
        ("DSE-8610-MIB", "gencommP167Reg-164-165"),
        ("DSE-8610-MIB", "gencommP167Reg-166-167"),
        ("DSE-8610-MIB", "gencommP167Reg-168-169"),
        ("DSE-8610-MIB", "gencommP167Reg-170-171"),
        ("DSE-8610-MIB", "gencommP167Reg-172-173"),
        ("DSE-8610-MIB", "gencommP167Reg-174-175"),
        ("DSE-8610-MIB", "gencommP167Reg-176-177"),
        ("DSE-8610-MIB", "gencommP167Reg-178-179"),
        ("DSE-8610-MIB", "gencommP167Reg-180-181"),
        ("DSE-8610-MIB", "gencommP167Reg-182-183"),
        ("DSE-8610-MIB", "gencommP167Reg-184-185"),
        ("DSE-8610-MIB", "gencommP167Reg-186-187"),
        ("DSE-8610-MIB", "gencommP167Reg-188-189"),
        ("DSE-8610-MIB", "gencommP167Reg-190-191"),
        ("DSE-8610-MIB", "gencommP167Reg-192-193"),
        ("DSE-8610-MIB", "gencommP167Reg-194-195"),
        ("DSE-8610-MIB", "gencommP167Reg-196-197"),
        ("DSE-8610-MIB", "gencommP167Reg-198-199"),
        ("DSE-8610-MIB", "gencommP167Reg-200-201"),
        ("DSE-8610-MIB", "gencommP167Reg-202-203"),
        ("DSE-8610-MIB", "gencommP167Reg-204-205"),
        ("DSE-8610-MIB", "gencommP167Reg-206-207"),
        ("DSE-8610-MIB", "gencommP167Reg-208-209"),
        ("DSE-8610-MIB", "gencommP167Reg-210-211"),
        ("DSE-8610-MIB", "gencommP167Reg-212-213"),
        ("DSE-8610-MIB", "gencommP167Reg-214-215"),
        ("DSE-8610-MIB", "gencommP167Reg-216-217"),
        ("DSE-8610-MIB", "gencommP167Reg-218-219"),
        ("DSE-8610-MIB", "gencommP167Reg-220-221"),
        ("DSE-8610-MIB", "gencommP167Reg-222-223"),
        ("DSE-8610-MIB", "gencommP167Reg-224-225"),
        ("DSE-8610-MIB", "gencommP167Reg-226-227"),
        ("DSE-8610-MIB", "gencommP167Reg-228-229"),
        ("DSE-8610-MIB", "gencommP167Reg-230-231"),
        ("DSE-8610-MIB", "gencommP167Reg-232-233"),
        ("DSE-8610-MIB", "gencommP167Reg-234-235"),
        ("DSE-8610-MIB", "gencommP167Reg-236-237"),
        ("DSE-8610-MIB", "gencommP167Reg-238-239"),
        ("DSE-8610-MIB", "gencommP167Reg-240-241"),
        ("DSE-8610-MIB", "gencommP167Reg-242-243"),
        ("DSE-8610-MIB", "gencommP167Reg-244-245"),
        ("DSE-8610-MIB", "gencommP167Reg-246-247"),
        ("DSE-8610-MIB", "gencommP167Reg-248-249"),
        ("DSE-8610-MIB", "gencommP167Reg-250-251"),
        ("DSE-8610-MIB", "gencommP167Reg-252-253"),
        ("DSE-8610-MIB", "gencommP167Reg-254-255"))
)
if mibBuilder.loadTexts:
    gencommP167Group.setStatus("current")

gencommP168Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 100, 2, 7)
)
gencommP168Group.setObjects(
      *(("DSE-8610-MIB", "gencommP168Reg-0-1"),
        ("DSE-8610-MIB", "gencommP168Reg-2-3"),
        ("DSE-8610-MIB", "gencommP168Reg-4-5"),
        ("DSE-8610-MIB", "gencommP168Reg-6-7"),
        ("DSE-8610-MIB", "gencommP168Reg-8-9"),
        ("DSE-8610-MIB", "gencommP168Reg-10-11"),
        ("DSE-8610-MIB", "gencommP168Reg-12-13"),
        ("DSE-8610-MIB", "gencommP168Reg-14-15"),
        ("DSE-8610-MIB", "gencommP168Reg-16-17"),
        ("DSE-8610-MIB", "gencommP168Reg-18-19"),
        ("DSE-8610-MIB", "gencommP168Reg-20-21"),
        ("DSE-8610-MIB", "gencommP168Reg-22-23"),
        ("DSE-8610-MIB", "gencommP168Reg-24-25"),
        ("DSE-8610-MIB", "gencommP168Reg-26-27"),
        ("DSE-8610-MIB", "gencommP168Reg-28-29"),
        ("DSE-8610-MIB", "gencommP168Reg-30-31"),
        ("DSE-8610-MIB", "gencommP168Reg-32-33"),
        ("DSE-8610-MIB", "gencommP168Reg-34-35"),
        ("DSE-8610-MIB", "gencommP168Reg-36-37"),
        ("DSE-8610-MIB", "gencommP168Reg-38-39"),
        ("DSE-8610-MIB", "gencommP168Reg-40-41"),
        ("DSE-8610-MIB", "gencommP168Reg-42-43"),
        ("DSE-8610-MIB", "gencommP168Reg-44-45"),
        ("DSE-8610-MIB", "gencommP168Reg-46-47"),
        ("DSE-8610-MIB", "gencommP168Reg-48-49"),
        ("DSE-8610-MIB", "gencommP168Reg-50-51"),
        ("DSE-8610-MIB", "gencommP168Reg-52-53"),
        ("DSE-8610-MIB", "gencommP168Reg-54-55"),
        ("DSE-8610-MIB", "gencommP168Reg-56-57"),
        ("DSE-8610-MIB", "gencommP168Reg-58-59"),
        ("DSE-8610-MIB", "gencommP168Reg-60-61"),
        ("DSE-8610-MIB", "gencommP168Reg-62-63"),
        ("DSE-8610-MIB", "gencommP168Reg-64-65"),
        ("DSE-8610-MIB", "gencommP168Reg-66-67"),
        ("DSE-8610-MIB", "gencommP168Reg-68-69"),
        ("DSE-8610-MIB", "gencommP168Reg-70-71"),
        ("DSE-8610-MIB", "gencommP168Reg-72-73"),
        ("DSE-8610-MIB", "gencommP168Reg-74-75"),
        ("DSE-8610-MIB", "gencommP168Reg-76-77"),
        ("DSE-8610-MIB", "gencommP168Reg-78-79"),
        ("DSE-8610-MIB", "gencommP168Reg-80-81"),
        ("DSE-8610-MIB", "gencommP168Reg-82-83"),
        ("DSE-8610-MIB", "gencommP168Reg-84-85"),
        ("DSE-8610-MIB", "gencommP168Reg-86-87"),
        ("DSE-8610-MIB", "gencommP168Reg-88-89"),
        ("DSE-8610-MIB", "gencommP168Reg-90-91"),
        ("DSE-8610-MIB", "gencommP168Reg-92-93"),
        ("DSE-8610-MIB", "gencommP168Reg-94-95"),
        ("DSE-8610-MIB", "gencommP168Reg-96-97"),
        ("DSE-8610-MIB", "gencommP168Reg-98-99"),
        ("DSE-8610-MIB", "gencommP168Reg-100-101"),
        ("DSE-8610-MIB", "gencommP168Reg-102-103"),
        ("DSE-8610-MIB", "gencommP168Reg-104-105"),
        ("DSE-8610-MIB", "gencommP168Reg-106-107"),
        ("DSE-8610-MIB", "gencommP168Reg-108-109"),
        ("DSE-8610-MIB", "gencommP168Reg-110-111"),
        ("DSE-8610-MIB", "gencommP168Reg-112-113"),
        ("DSE-8610-MIB", "gencommP168Reg-114-115"),
        ("DSE-8610-MIB", "gencommP168Reg-116-117"),
        ("DSE-8610-MIB", "gencommP168Reg-118-119"),
        ("DSE-8610-MIB", "gencommP168Reg-120-121"),
        ("DSE-8610-MIB", "gencommP168Reg-122-123"),
        ("DSE-8610-MIB", "gencommP168Reg-124-125"),
        ("DSE-8610-MIB", "gencommP168Reg-126-127"),
        ("DSE-8610-MIB", "gencommP168Reg-128-129"),
        ("DSE-8610-MIB", "gencommP168Reg-130-131"),
        ("DSE-8610-MIB", "gencommP168Reg-132-133"),
        ("DSE-8610-MIB", "gencommP168Reg-134-135"),
        ("DSE-8610-MIB", "gencommP168Reg-136-137"),
        ("DSE-8610-MIB", "gencommP168Reg-138-139"),
        ("DSE-8610-MIB", "gencommP168Reg-140-141"),
        ("DSE-8610-MIB", "gencommP168Reg-142-143"),
        ("DSE-8610-MIB", "gencommP168Reg-144-145"),
        ("DSE-8610-MIB", "gencommP168Reg-146-147"),
        ("DSE-8610-MIB", "gencommP168Reg-148-149"),
        ("DSE-8610-MIB", "gencommP168Reg-150-151"),
        ("DSE-8610-MIB", "gencommP168Reg-152-153"),
        ("DSE-8610-MIB", "gencommP168Reg-154-155"),
        ("DSE-8610-MIB", "gencommP168Reg-156-157"),
        ("DSE-8610-MIB", "gencommP168Reg-158-159"),
        ("DSE-8610-MIB", "gencommP168Reg-160-161"),
        ("DSE-8610-MIB", "gencommP168Reg-162-163"),
        ("DSE-8610-MIB", "gencommP168Reg-164-165"),
        ("DSE-8610-MIB", "gencommP168Reg-166-167"),
        ("DSE-8610-MIB", "gencommP168Reg-168-169"),
        ("DSE-8610-MIB", "gencommP168Reg-170-171"),
        ("DSE-8610-MIB", "gencommP168Reg-172-173"),
        ("DSE-8610-MIB", "gencommP168Reg-174-175"),
        ("DSE-8610-MIB", "gencommP168Reg-176-177"),
        ("DSE-8610-MIB", "gencommP168Reg-178-179"),
        ("DSE-8610-MIB", "gencommP168Reg-180-181"),
        ("DSE-8610-MIB", "gencommP168Reg-182-183"),
        ("DSE-8610-MIB", "gencommP168Reg-184-185"),
        ("DSE-8610-MIB", "gencommP168Reg-186-187"),
        ("DSE-8610-MIB", "gencommP168Reg-188-189"),
        ("DSE-8610-MIB", "gencommP168Reg-190-191"),
        ("DSE-8610-MIB", "gencommP168Reg-192-193"),
        ("DSE-8610-MIB", "gencommP168Reg-194-195"),
        ("DSE-8610-MIB", "gencommP168Reg-196-197"),
        ("DSE-8610-MIB", "gencommP168Reg-198-199"),
        ("DSE-8610-MIB", "gencommP168Reg-200-201"),
        ("DSE-8610-MIB", "gencommP168Reg-202-203"),
        ("DSE-8610-MIB", "gencommP168Reg-204-205"),
        ("DSE-8610-MIB", "gencommP168Reg-206-207"),
        ("DSE-8610-MIB", "gencommP168Reg-208-209"),
        ("DSE-8610-MIB", "gencommP168Reg-210-211"),
        ("DSE-8610-MIB", "gencommP168Reg-212-213"),
        ("DSE-8610-MIB", "gencommP168Reg-214-215"),
        ("DSE-8610-MIB", "gencommP168Reg-216-217"),
        ("DSE-8610-MIB", "gencommP168Reg-218-219"),
        ("DSE-8610-MIB", "gencommP168Reg-220-221"),
        ("DSE-8610-MIB", "gencommP168Reg-222-223"),
        ("DSE-8610-MIB", "gencommP168Reg-224-225"),
        ("DSE-8610-MIB", "gencommP168Reg-226-227"),
        ("DSE-8610-MIB", "gencommP168Reg-228-229"),
        ("DSE-8610-MIB", "gencommP168Reg-230-231"),
        ("DSE-8610-MIB", "gencommP168Reg-232-233"),
        ("DSE-8610-MIB", "gencommP168Reg-234-235"),
        ("DSE-8610-MIB", "gencommP168Reg-236-237"),
        ("DSE-8610-MIB", "gencommP168Reg-238-239"),
        ("DSE-8610-MIB", "gencommP168Reg-240-241"),
        ("DSE-8610-MIB", "gencommP168Reg-242-243"),
        ("DSE-8610-MIB", "gencommP168Reg-244-245"),
        ("DSE-8610-MIB", "gencommP168Reg-246-247"),
        ("DSE-8610-MIB", "gencommP168Reg-248-249"),
        ("DSE-8610-MIB", "gencommP168Reg-250-251"),
        ("DSE-8610-MIB", "gencommP168Reg-252-253"),
        ("DSE-8610-MIB", "gencommP168Reg-254-255"))
)
if mibBuilder.loadTexts:
    gencommP168Group.setStatus("current")

gencommP169Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 100, 2, 8)
)
gencommP169Group.setObjects(
      *(("DSE-8610-MIB", "gencommP169Reg-0-1"),
        ("DSE-8610-MIB", "gencommP169Reg-2-3"),
        ("DSE-8610-MIB", "gencommP169Reg-4-5"),
        ("DSE-8610-MIB", "gencommP169Reg-6-7"),
        ("DSE-8610-MIB", "gencommP169Reg-8-9"),
        ("DSE-8610-MIB", "gencommP169Reg-10-11"),
        ("DSE-8610-MIB", "gencommP169Reg-12-13"),
        ("DSE-8610-MIB", "gencommP169Reg-14-15"),
        ("DSE-8610-MIB", "gencommP169Reg-16-17"),
        ("DSE-8610-MIB", "gencommP169Reg-18-19"),
        ("DSE-8610-MIB", "gencommP169Reg-20-21"),
        ("DSE-8610-MIB", "gencommP169Reg-22-23"),
        ("DSE-8610-MIB", "gencommP169Reg-24-25"),
        ("DSE-8610-MIB", "gencommP169Reg-26-27"),
        ("DSE-8610-MIB", "gencommP169Reg-28-29"),
        ("DSE-8610-MIB", "gencommP169Reg-30-31"),
        ("DSE-8610-MIB", "gencommP169Reg-32-33"),
        ("DSE-8610-MIB", "gencommP169Reg-34-35"),
        ("DSE-8610-MIB", "gencommP169Reg-36-37"),
        ("DSE-8610-MIB", "gencommP169Reg-38-39"),
        ("DSE-8610-MIB", "gencommP169Reg-40-41"),
        ("DSE-8610-MIB", "gencommP169Reg-42-43"),
        ("DSE-8610-MIB", "gencommP169Reg-44-45"),
        ("DSE-8610-MIB", "gencommP169Reg-46-47"),
        ("DSE-8610-MIB", "gencommP169Reg-48-49"),
        ("DSE-8610-MIB", "gencommP169Reg-50-51"),
        ("DSE-8610-MIB", "gencommP169Reg-52-53"),
        ("DSE-8610-MIB", "gencommP169Reg-54-55"),
        ("DSE-8610-MIB", "gencommP169Reg-56-57"),
        ("DSE-8610-MIB", "gencommP169Reg-58-59"),
        ("DSE-8610-MIB", "gencommP169Reg-60-61"),
        ("DSE-8610-MIB", "gencommP169Reg-62-63"),
        ("DSE-8610-MIB", "gencommP169Reg-64-65"),
        ("DSE-8610-MIB", "gencommP169Reg-66-67"),
        ("DSE-8610-MIB", "gencommP169Reg-68-69"),
        ("DSE-8610-MIB", "gencommP169Reg-70-71"),
        ("DSE-8610-MIB", "gencommP169Reg-72-73"),
        ("DSE-8610-MIB", "gencommP169Reg-74-75"),
        ("DSE-8610-MIB", "gencommP169Reg-76-77"),
        ("DSE-8610-MIB", "gencommP169Reg-78-79"),
        ("DSE-8610-MIB", "gencommP169Reg-80-81"),
        ("DSE-8610-MIB", "gencommP169Reg-82-83"),
        ("DSE-8610-MIB", "gencommP169Reg-84-85"),
        ("DSE-8610-MIB", "gencommP169Reg-86-87"),
        ("DSE-8610-MIB", "gencommP169Reg-88-89"),
        ("DSE-8610-MIB", "gencommP169Reg-90-91"),
        ("DSE-8610-MIB", "gencommP169Reg-92-93"),
        ("DSE-8610-MIB", "gencommP169Reg-94-95"),
        ("DSE-8610-MIB", "gencommP169Reg-96-97"),
        ("DSE-8610-MIB", "gencommP169Reg-98-99"),
        ("DSE-8610-MIB", "gencommP169Reg-100-101"),
        ("DSE-8610-MIB", "gencommP169Reg-102-103"),
        ("DSE-8610-MIB", "gencommP169Reg-104-105"),
        ("DSE-8610-MIB", "gencommP169Reg-106-107"),
        ("DSE-8610-MIB", "gencommP169Reg-108-109"),
        ("DSE-8610-MIB", "gencommP169Reg-110-111"),
        ("DSE-8610-MIB", "gencommP169Reg-112-113"),
        ("DSE-8610-MIB", "gencommP169Reg-114-115"),
        ("DSE-8610-MIB", "gencommP169Reg-116-117"),
        ("DSE-8610-MIB", "gencommP169Reg-118-119"),
        ("DSE-8610-MIB", "gencommP169Reg-120-121"),
        ("DSE-8610-MIB", "gencommP169Reg-122-123"),
        ("DSE-8610-MIB", "gencommP169Reg-124-125"),
        ("DSE-8610-MIB", "gencommP169Reg-126-127"),
        ("DSE-8610-MIB", "gencommP169Reg-128-129"),
        ("DSE-8610-MIB", "gencommP169Reg-130-131"),
        ("DSE-8610-MIB", "gencommP169Reg-132-133"),
        ("DSE-8610-MIB", "gencommP169Reg-134-135"),
        ("DSE-8610-MIB", "gencommP169Reg-136-137"),
        ("DSE-8610-MIB", "gencommP169Reg-138-139"),
        ("DSE-8610-MIB", "gencommP169Reg-140-141"),
        ("DSE-8610-MIB", "gencommP169Reg-142-143"),
        ("DSE-8610-MIB", "gencommP169Reg-144-145"),
        ("DSE-8610-MIB", "gencommP169Reg-146-147"),
        ("DSE-8610-MIB", "gencommP169Reg-148-149"),
        ("DSE-8610-MIB", "gencommP169Reg-150-151"),
        ("DSE-8610-MIB", "gencommP169Reg-152-153"),
        ("DSE-8610-MIB", "gencommP169Reg-154-155"),
        ("DSE-8610-MIB", "gencommP169Reg-156-157"),
        ("DSE-8610-MIB", "gencommP169Reg-158-159"),
        ("DSE-8610-MIB", "gencommP169Reg-160-161"),
        ("DSE-8610-MIB", "gencommP169Reg-162-163"),
        ("DSE-8610-MIB", "gencommP169Reg-164-165"),
        ("DSE-8610-MIB", "gencommP169Reg-166-167"),
        ("DSE-8610-MIB", "gencommP169Reg-168-169"),
        ("DSE-8610-MIB", "gencommP169Reg-170-171"),
        ("DSE-8610-MIB", "gencommP169Reg-172-173"),
        ("DSE-8610-MIB", "gencommP169Reg-174-175"),
        ("DSE-8610-MIB", "gencommP169Reg-176-177"),
        ("DSE-8610-MIB", "gencommP169Reg-178-179"),
        ("DSE-8610-MIB", "gencommP169Reg-180-181"),
        ("DSE-8610-MIB", "gencommP169Reg-182-183"),
        ("DSE-8610-MIB", "gencommP169Reg-184-185"),
        ("DSE-8610-MIB", "gencommP169Reg-186-187"),
        ("DSE-8610-MIB", "gencommP169Reg-188-189"),
        ("DSE-8610-MIB", "gencommP169Reg-190-191"),
        ("DSE-8610-MIB", "gencommP169Reg-192-193"),
        ("DSE-8610-MIB", "gencommP169Reg-194-195"),
        ("DSE-8610-MIB", "gencommP169Reg-196-197"),
        ("DSE-8610-MIB", "gencommP169Reg-198-199"),
        ("DSE-8610-MIB", "gencommP169Reg-200-201"),
        ("DSE-8610-MIB", "gencommP169Reg-202-203"),
        ("DSE-8610-MIB", "gencommP169Reg-204-205"),
        ("DSE-8610-MIB", "gencommP169Reg-206-207"),
        ("DSE-8610-MIB", "gencommP169Reg-208-209"),
        ("DSE-8610-MIB", "gencommP169Reg-210-211"),
        ("DSE-8610-MIB", "gencommP169Reg-212-213"),
        ("DSE-8610-MIB", "gencommP169Reg-214-215"),
        ("DSE-8610-MIB", "gencommP169Reg-216-217"),
        ("DSE-8610-MIB", "gencommP169Reg-218-219"),
        ("DSE-8610-MIB", "gencommP169Reg-220-221"),
        ("DSE-8610-MIB", "gencommP169Reg-222-223"),
        ("DSE-8610-MIB", "gencommP169Reg-224-225"),
        ("DSE-8610-MIB", "gencommP169Reg-226-227"),
        ("DSE-8610-MIB", "gencommP169Reg-228-229"),
        ("DSE-8610-MIB", "gencommP169Reg-230-231"),
        ("DSE-8610-MIB", "gencommP169Reg-232-233"),
        ("DSE-8610-MIB", "gencommP169Reg-234-235"),
        ("DSE-8610-MIB", "gencommP169Reg-236-237"),
        ("DSE-8610-MIB", "gencommP169Reg-238-239"),
        ("DSE-8610-MIB", "gencommP169Reg-240-241"),
        ("DSE-8610-MIB", "gencommP169Reg-242-243"),
        ("DSE-8610-MIB", "gencommP169Reg-244-245"),
        ("DSE-8610-MIB", "gencommP169Reg-246-247"),
        ("DSE-8610-MIB", "gencommP169Reg-248-249"),
        ("DSE-8610-MIB", "gencommP169Reg-250-251"),
        ("DSE-8610-MIB", "gencommP169Reg-252-253"),
        ("DSE-8610-MIB", "gencommP169Reg-254-255"))
)
if mibBuilder.loadTexts:
    gencommP169Group.setStatus("current")

keypressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 100, 2, 9)
)
keypressGroup.setObjects(
    ("DSE-8610-MIB", "keypress")
)
if mibBuilder.loadTexts:
    keypressGroup.setStatus("current")

trapVarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 100, 2, 10)
)
trapVarsGroup.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapVarsGroup.setStatus("current")


# Notification objects

namedAlarmEmergencyStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4096)
)
namedAlarmEmergencyStop.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmEmergencyStop.setStatus(
        "current"
    )

namedAlarmLowOilPressure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4097)
)
namedAlarmLowOilPressure.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmLowOilPressure.setStatus(
        "current"
    )

namedAlarmHighCoolantTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4098)
)
namedAlarmHighCoolantTemp.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmHighCoolantTemp.setStatus(
        "current"
    )

namedAlarmLowCoolantTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4099)
)
namedAlarmLowCoolantTemp.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmLowCoolantTemp.setStatus(
        "current"
    )

namedAlarmUnderSpeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4100)
)
namedAlarmUnderSpeed.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmUnderSpeed.setStatus(
        "current"
    )

namedAlarmOverSpeed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4101)
)
namedAlarmOverSpeed.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmOverSpeed.setStatus(
        "current"
    )

namedAlarmGeneratorUnderFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4102)
)
namedAlarmGeneratorUnderFrequency.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmGeneratorUnderFrequency.setStatus(
        "current"
    )

namedAlarmGeneratorOverFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4103)
)
namedAlarmGeneratorOverFrequency.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmGeneratorOverFrequency.setStatus(
        "current"
    )

namedAlarmGeneratorUnderVolts = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4104)
)
namedAlarmGeneratorUnderVolts.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmGeneratorUnderVolts.setStatus(
        "current"
    )

namedAlarmGeneratorOverVolts = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4105)
)
namedAlarmGeneratorOverVolts.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmGeneratorOverVolts.setStatus(
        "current"
    )

namedAlarmBatteryUnderVolts = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4106)
)
namedAlarmBatteryUnderVolts.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmBatteryUnderVolts.setStatus(
        "current"
    )

namedAlarmBatteryOverVolts = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4107)
)
namedAlarmBatteryOverVolts.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmBatteryOverVolts.setStatus(
        "current"
    )

namedAlarmChargeAlternatorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4108)
)
namedAlarmChargeAlternatorFailure.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmChargeAlternatorFailure.setStatus(
        "current"
    )

namedAlarmFailToStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4109)
)
namedAlarmFailToStart.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmFailToStart.setStatus(
        "current"
    )

namedAlarmFailToStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4110)
)
namedAlarmFailToStop.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmFailToStop.setStatus(
        "current"
    )

namedAlarmGeneratorFailedToClose = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4111)
)
namedAlarmGeneratorFailedToClose.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmGeneratorFailedToClose.setStatus(
        "current"
    )

namedAlarmMainsFailedToClose = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4112)
)
namedAlarmMainsFailedToClose.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMainsFailedToClose.setStatus(
        "current"
    )

namedAlarmOilPressureSensorOpenCircuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4113)
)
namedAlarmOilPressureSensorOpenCircuit.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmOilPressureSensorOpenCircuit.setStatus(
        "current"
    )

namedAlarmLossOfMagPickupSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4114)
)
namedAlarmLossOfMagPickupSignal.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmLossOfMagPickupSignal.setStatus(
        "current"
    )

namedAlarmMagPickupOpenCircuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4115)
)
namedAlarmMagPickupOpenCircuit.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMagPickupOpenCircuit.setStatus(
        "current"
    )

namedAlarmGeneratorOverCurrent = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4116)
)
namedAlarmGeneratorOverCurrent.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmGeneratorOverCurrent.setStatus(
        "current"
    )

namedAlarmCalibrationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4117)
)
namedAlarmCalibrationLost.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmCalibrationLost.setStatus(
        "current"
    )

namedAlarmLowFuelLevel = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4118)
)
namedAlarmLowFuelLevel.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmLowFuelLevel.setStatus(
        "current"
    )

namedAlarmECUAmber = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4119)
)
namedAlarmECUAmber.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmECUAmber.setStatus(
        "current"
    )

namedAlarmECURed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4120)
)
namedAlarmECURed.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmECURed.setStatus(
        "current"
    )

namedAlarmECUDataFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4121)
)
namedAlarmECUDataFail.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmECUDataFail.setStatus(
        "current"
    )

namedAlarmLowOilPressureSwitchAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4122)
)
namedAlarmLowOilPressureSwitchAlarm.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmLowOilPressureSwitchAlarm.setStatus(
        "current"
    )

namedAlarmHighTemperatureSwitchAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4123)
)
namedAlarmHighTemperatureSwitchAlarm.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmHighTemperatureSwitchAlarm.setStatus(
        "current"
    )

namedAlarmLowFuelSwitchAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4124)
)
namedAlarmLowFuelSwitchAlarm.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmLowFuelSwitchAlarm.setStatus(
        "current"
    )

namedAlarmExpansionUnitWatchdogAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4125)
)
namedAlarmExpansionUnitWatchdogAlarm.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmExpansionUnitWatchdogAlarm.setStatus(
        "current"
    )

namedAlarmkWOverloadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4126)
)
namedAlarmkWOverloadAlarm.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmkWOverloadAlarm.setStatus(
        "current"
    )

namedAlarmNegativePhaseSequenceAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4127)
)
namedAlarmNegativePhaseSequenceAlarm.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmNegativePhaseSequenceAlarm.setStatus(
        "current"
    )

namedAlarmEarthFaultTrip = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4128)
)
namedAlarmEarthFaultTrip.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmEarthFaultTrip.setStatus(
        "current"
    )

namedAlarmGeneratorPhaseRotationAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4129)
)
namedAlarmGeneratorPhaseRotationAlarm.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmGeneratorPhaseRotationAlarm.setStatus(
        "current"
    )

namedAlarmAutoVoltageSenseFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4130)
)
namedAlarmAutoVoltageSenseFail.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmAutoVoltageSenseFail.setStatus(
        "current"
    )

namedAlarmMaintenanceAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4131)
)
namedAlarmMaintenanceAlarm.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMaintenanceAlarm.setStatus(
        "current"
    )

namedAlarmFailtoReachLoadingVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4133)
)
namedAlarmFailtoReachLoadingVoltage.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmFailtoReachLoadingVoltage.setStatus(
        "current"
    )

namedAlarmFuelUsageRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4134)
)
namedAlarmFuelUsageRunning.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmFuelUsageRunning.setStatus(
        "current"
    )

namedAlarmFuelUsageStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4135)
)
namedAlarmFuelUsageStopped.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmFuelUsageStopped.setStatus(
        "current"
    )

namedAlarmProtectionsDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4136)
)
namedAlarmProtectionsDisabled.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmProtectionsDisabled.setStatus(
        "current"
    )

namedAlarmGeneratorBreakerFailedToOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4138)
)
namedAlarmGeneratorBreakerFailedToOpen.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmGeneratorBreakerFailedToOpen.setStatus(
        "current"
    )

namedAlarmMainsBreakerFailedToOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4139)
)
namedAlarmMainsBreakerFailedToOpen.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMainsBreakerFailedToOpen.setStatus(
        "current"
    )

namedAlarmBusBreakerFailedToClose = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4140)
)
namedAlarmBusBreakerFailedToClose.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmBusBreakerFailedToClose.setStatus(
        "current"
    )

namedAlarmBusBreakerFailedToOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4141)
)
namedAlarmBusBreakerFailedToOpen.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmBusBreakerFailedToOpen.setStatus(
        "current"
    )

namedAlarmGeneratorReversePowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4142)
)
namedAlarmGeneratorReversePowerAlarm.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmGeneratorReversePowerAlarm.setStatus(
        "current"
    )

namedAlarmShortCircuitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4143)
)
namedAlarmShortCircuitAlarm.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmShortCircuitAlarm.setStatus(
        "current"
    )

namedAlarmAirFlapClosedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4144)
)
namedAlarmAirFlapClosedAlarm.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmAirFlapClosedAlarm.setStatus(
        "current"
    )

namedAlarmFailToSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4145)
)
namedAlarmFailToSync.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmFailToSync.setStatus(
        "current"
    )

namedAlarmBusLive = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4146)
)
namedAlarmBusLive.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmBusLive.setStatus(
        "current"
    )

namedAlarmBusNotLive = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4147)
)
namedAlarmBusNotLive.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmBusNotLive.setStatus(
        "current"
    )

namedAlarmBusPhaseRotation = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4148)
)
namedAlarmBusPhaseRotation.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmBusPhaseRotation.setStatus(
        "current"
    )

namedAlarmPrioritySelectionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4149)
)
namedAlarmPrioritySelectionError.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmPrioritySelectionError.setStatus(
        "current"
    )

namedAlarmMSCDataError = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4150)
)
namedAlarmMSCDataError.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMSCDataError.setStatus(
        "current"
    )

namedAlarmMSCIDError = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4151)
)
namedAlarmMSCIDError.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMSCIDError.setStatus(
        "current"
    )

namedAlarmBusLowVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4152)
)
namedAlarmBusLowVoltage.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmBusLowVoltage.setStatus(
        "current"
    )

namedAlarmBusHighVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4153)
)
namedAlarmBusHighVoltage.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmBusHighVoltage.setStatus(
        "current"
    )

namedAlarmBusLowFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4154)
)
namedAlarmBusLowFrequency.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmBusLowFrequency.setStatus(
        "current"
    )

namedAlarmBusHighFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4155)
)
namedAlarmBusHighFrequency.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmBusHighFrequency.setStatus(
        "current"
    )

namedAlarmMSCFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4156)
)
namedAlarmMSCFailure.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMSCFailure.setStatus(
        "current"
    )

namedAlarmMSCTooFewSets = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4157)
)
namedAlarmMSCTooFewSets.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMSCTooFewSets.setStatus(
        "current"
    )

namedAlarmMSCAlarmsInhibited = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4158)
)
namedAlarmMSCAlarmsInhibited.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMSCAlarmsInhibited.setStatus(
        "current"
    )

namedAlarmMSCOldVersionUnitsOnTheBus = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4159)
)
namedAlarmMSCOldVersionUnitsOnTheBus.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMSCOldVersionUnitsOnTheBus.setStatus(
        "current"
    )

namedAlarmMainsReversePowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4160)
)
namedAlarmMainsReversePowerAlarm.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMainsReversePowerAlarm.setStatus(
        "current"
    )

namedAlarmMinimumSetsNotReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4161)
)
namedAlarmMinimumSetsNotReached.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMinimumSetsNotReached.setStatus(
        "current"
    )

namedAlarmInsufficientCapacity = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4162)
)
namedAlarmInsufficientCapacity.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmInsufficientCapacity.setStatus(
        "current"
    )

namedAlarmOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4163)
)
namedAlarmOutOfSync.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmOutOfSync.setStatus(
        "current"
    )

namedAlarmAlternativeAuxMainsFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4164)
)
namedAlarmAlternativeAuxMainsFail.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmAlternativeAuxMainsFail.setStatus(
        "current"
    )

namedAlarmLossOfExcitation = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4165)
)
namedAlarmLossOfExcitation.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmLossOfExcitation.setStatus(
        "current"
    )

namedAlarmMainsROCOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4166)
)
namedAlarmMainsROCOF.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMainsROCOF.setStatus(
        "current"
    )

namedAlarmMainsVectorShift = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4167)
)
namedAlarmMainsVectorShift.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMainsVectorShift.setStatus(
        "current"
    )

namedAlarmMainsDecouplingLowFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4168)
)
namedAlarmMainsDecouplingLowFrequency.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMainsDecouplingLowFrequency.setStatus(
        "current"
    )

namedAlarmMainsDecouplingHighFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4169)
)
namedAlarmMainsDecouplingHighFrequency.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMainsDecouplingHighFrequency.setStatus(
        "current"
    )

namedAlarmMainsDecouplingLowVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4170)
)
namedAlarmMainsDecouplingLowVoltage.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMainsDecouplingLowVoltage.setStatus(
        "current"
    )

namedAlarmMainsDecouplingHighVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4171)
)
namedAlarmMainsDecouplingHighVoltage.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMainsDecouplingHighVoltage.setStatus(
        "current"
    )

namedAlarmMainsDecouplingCombinedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4172)
)
namedAlarmMainsDecouplingCombinedAlarm.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMainsDecouplingCombinedAlarm.setStatus(
        "current"
    )

namedAlarmMainsPhaseRotationAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4174)
)
namedAlarmMainsPhaseRotationAlarm.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMainsPhaseRotationAlarm.setStatus(
        "current"
    )

namedAlarmAVRMaxTrimLimitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4175)
)
namedAlarmAVRMaxTrimLimitAlarm.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmAVRMaxTrimLimitAlarm.setStatus(
        "current"
    )

namedAlarmHighCoolantTempElecTripAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4176)
)
namedAlarmHighCoolantTempElecTripAlarm.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmHighCoolantTempElecTripAlarm.setStatus(
        "current"
    )

namedAlarmTempSenderOpenCircuitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4177)
)
namedAlarmTempSenderOpenCircuitAlarm.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmTempSenderOpenCircuitAlarm.setStatus(
        "current"
    )

namedAlarmFailtoReachLoadingFrequency = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4178)
)
namedAlarmFailtoReachLoadingFrequency.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmFailtoReachLoadingFrequency.setStatus(
        "current"
    )

namedAlarmProtectionsBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4187)
)
namedAlarmProtectionsBlocked.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmProtectionsBlocked.setStatus(
        "current"
    )

namedAlarmOutOfSyncBus = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4188)
)
namedAlarmOutOfSyncBus.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmOutOfSyncBus.setStatus(
        "current"
    )

namedAlarmOutOfSyncMains = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4189)
)
namedAlarmOutOfSyncMains.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmOutOfSyncMains.setStatus(
        "current"
    )

namedAlarmECUControlledHeaters = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4197)
)
namedAlarmECUControlledHeaters.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmECUControlledHeaters.setStatus(
        "current"
    )

namedAlarmECUControlledCoolers = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4198)
)
namedAlarmECUControlledCoolers.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmECUControlledCoolers.setStatus(
        "current"
    )

namedAlarmECUProtect = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4199)
)
namedAlarmECUProtect.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmECUProtect.setStatus(
        "current"
    )

namedAlarmECUMalfunction = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4200)
)
namedAlarmECUMalfunction.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmECUMalfunction.setStatus(
        "current"
    )

namedAlarmIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4201)
)
namedAlarmIndication.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmIndication.setStatus(
        "current"
    )

namedAlarmWaterinFuel = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4206)
)
namedAlarmWaterinFuel.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmWaterinFuel.setStatus(
        "current"
    )

namedAlarmHESTActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4225)
)
namedAlarmHESTActive.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmHESTActive.setStatus(
        "current"
    )

namedAlarmDPTCFilter = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4226)
)
namedAlarmDPTCFilter.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmDPTCFilter.setStatus(
        "current"
    )

namedAlarmHighFuelLevel = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4227)
)
namedAlarmHighFuelLevel.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmHighFuelLevel.setStatus(
        "current"
    )

namedAlarmHeaterSensorFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4233)
)
namedAlarmHeaterSensorFailureAlarm.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmHeaterSensorFailureAlarm.setStatus(
        "current"
    )

namedAlarmDEFLevelLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4313)
)
namedAlarmDEFLevelLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmDEFLevelLow.setStatus(
        "current"
    )

namedAlarmSCRInducement = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4314)
)
namedAlarmSCRInducement.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmSCRInducement.setStatus(
        "current"
    )

namedAlarmInletTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4364)
)
namedAlarmInletTemperature.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmInletTemperature.setStatus(
        "current"
    )

namedAlarmElectricalTripStopInhibited = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4367)
)
namedAlarmElectricalTripStopInhibited.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmElectricalTripStopInhibited.setStatus(
        "current"
    )

namedAlarmFuelTankBundLevelHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4372)
)
namedAlarmFuelTankBundLevelHigh.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmFuelTankBundLevelHigh.setStatus(
        "current"
    )

namedAlarmMSCLink1DataError = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4379)
)
namedAlarmMSCLink1DataError.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMSCLink1DataError.setStatus(
        "current"
    )

namedAlarmMSCLink2DataError = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4380)
)
namedAlarmMSCLink2DataError.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMSCLink2DataError.setStatus(
        "current"
    )

namedAlarmMSCLink1Failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4381)
)
namedAlarmMSCLink1Failure.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMSCLink1Failure.setStatus(
        "current"
    )

namedAlarmMSCLink2Failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4382)
)
namedAlarmMSCLink2Failure.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMSCLink2Failure.setStatus(
        "current"
    )

namedAlarmMSCLink1TooFewSets = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4383)
)
namedAlarmMSCLink1TooFewSets.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMSCLink1TooFewSets.setStatus(
        "current"
    )

namedAlarmMSCLink2TooFewSets = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4384)
)
namedAlarmMSCLink2TooFewSets.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMSCLink2TooFewSets.setStatus(
        "current"
    )

namedAlarmMSCLink1and2Failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4385)
)
namedAlarmMSCLink1and2Failure.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmMSCLink1and2Failure.setStatus(
        "current"
    )

namedAlarmElectricalTripfrom8660 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 4387)
)
namedAlarmElectricalTripfrom8660.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    namedAlarmElectricalTripfrom8660.setStatus(
        "current"
    )

unnamedAlarmDigitalInputA = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8192)
)
unnamedAlarmDigitalInputA.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmDigitalInputA.setStatus(
        "current"
    )

unnamedAlarmDigitalInputB = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8193)
)
unnamedAlarmDigitalInputB.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmDigitalInputB.setStatus(
        "current"
    )

unnamedAlarmDigitalInputC = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8194)
)
unnamedAlarmDigitalInputC.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmDigitalInputC.setStatus(
        "current"
    )

unnamedAlarmDigitalInputD = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8195)
)
unnamedAlarmDigitalInputD.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmDigitalInputD.setStatus(
        "current"
    )

unnamedAlarmDigitalInputE = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8196)
)
unnamedAlarmDigitalInputE.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmDigitalInputE.setStatus(
        "current"
    )

unnamedAlarmDigitalInputF = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8197)
)
unnamedAlarmDigitalInputF.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmDigitalInputF.setStatus(
        "current"
    )

unnamedAlarmDigitalInputG = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8198)
)
unnamedAlarmDigitalInputG.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmDigitalInputG.setStatus(
        "current"
    )

unnamedAlarmDigitalInputH = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8199)
)
unnamedAlarmDigitalInputH.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmDigitalInputH.setStatus(
        "current"
    )

unnamedAlarmDigitalInputI = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8200)
)
unnamedAlarmDigitalInputI.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmDigitalInputI.setStatus(
        "current"
    )

unnamedAlarmDigitalInputJ = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8201)
)
unnamedAlarmDigitalInputJ.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmDigitalInputJ.setStatus(
        "current"
    )

unnamedAlarmDigitalInputK = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8202)
)
unnamedAlarmDigitalInputK.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmDigitalInputK.setStatus(
        "current"
    )

unnamedAlarmDigitalInputL = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8203)
)
unnamedAlarmDigitalInputL.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmDigitalInputL.setStatus(
        "current"
    )

unnamedAlarmAnalogueInputBDigital = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8208)
)
unnamedAlarmAnalogueInputBDigital.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmAnalogueInputBDigital.setStatus(
        "current"
    )

unnamedAlarmAnalogueInputCDigital = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8209)
)
unnamedAlarmAnalogueInputCDigital.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmAnalogueInputCDigital.setStatus(
        "current"
    )

unnamedAlarmAnalogueInputDDigital = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8210)
)
unnamedAlarmAnalogueInputDDigital.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmAnalogueInputDDigital.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID0DigitalInputA = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8224)
)
unnamedAlarm2130ExpansionModuleID0DigitalInputA.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID0DigitalInputA.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID0DigitalInputB = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8225)
)
unnamedAlarm2130ExpansionModuleID0DigitalInputB.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID0DigitalInputB.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID0DigitalInputC = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8226)
)
unnamedAlarm2130ExpansionModuleID0DigitalInputC.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID0DigitalInputC.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID0DigitalInputD = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8227)
)
unnamedAlarm2130ExpansionModuleID0DigitalInputD.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID0DigitalInputD.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID0DigitalInputE = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8228)
)
unnamedAlarm2130ExpansionModuleID0DigitalInputE.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID0DigitalInputE.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID0DigitalInputF = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8229)
)
unnamedAlarm2130ExpansionModuleID0DigitalInputF.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID0DigitalInputF.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID0DigitalInputG = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8230)
)
unnamedAlarm2130ExpansionModuleID0DigitalInputG.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID0DigitalInputG.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID0DigitalInputH = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8231)
)
unnamedAlarm2130ExpansionModuleID0DigitalInputH.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID0DigitalInputH.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID1DigitalInputA = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8232)
)
unnamedAlarm2130ExpansionModuleID1DigitalInputA.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID1DigitalInputA.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID1DigitalInputB = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8233)
)
unnamedAlarm2130ExpansionModuleID1DigitalInputB.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID1DigitalInputB.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID1DigitalInputC = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8234)
)
unnamedAlarm2130ExpansionModuleID1DigitalInputC.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID1DigitalInputC.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID1DigitalInputD = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8235)
)
unnamedAlarm2130ExpansionModuleID1DigitalInputD.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID1DigitalInputD.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID1DigitalInputE = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8236)
)
unnamedAlarm2130ExpansionModuleID1DigitalInputE.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID1DigitalInputE.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID1DigitalInputF = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8237)
)
unnamedAlarm2130ExpansionModuleID1DigitalInputF.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID1DigitalInputF.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID1DigitalInputG = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8238)
)
unnamedAlarm2130ExpansionModuleID1DigitalInputG.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID1DigitalInputG.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID1DigitalInputH = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8239)
)
unnamedAlarm2130ExpansionModuleID1DigitalInputH.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID1DigitalInputH.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID2DigitalInputA = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8240)
)
unnamedAlarm2130ExpansionModuleID2DigitalInputA.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID2DigitalInputA.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID2DigitalInputB = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8241)
)
unnamedAlarm2130ExpansionModuleID2DigitalInputB.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID2DigitalInputB.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID2DigitalInputC = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8242)
)
unnamedAlarm2130ExpansionModuleID2DigitalInputC.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID2DigitalInputC.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID2DigitalInputD = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8243)
)
unnamedAlarm2130ExpansionModuleID2DigitalInputD.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID2DigitalInputD.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID2DigitalInputE = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8244)
)
unnamedAlarm2130ExpansionModuleID2DigitalInputE.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID2DigitalInputE.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID2DigitalInputF = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8245)
)
unnamedAlarm2130ExpansionModuleID2DigitalInputF.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID2DigitalInputF.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID2DigitalInputG = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8246)
)
unnamedAlarm2130ExpansionModuleID2DigitalInputG.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID2DigitalInputG.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID2DigitalInputH = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8247)
)
unnamedAlarm2130ExpansionModuleID2DigitalInputH.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID2DigitalInputH.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID3DigitalInputA = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8248)
)
unnamedAlarm2130ExpansionModuleID3DigitalInputA.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID3DigitalInputA.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID3DigitalInputB = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8249)
)
unnamedAlarm2130ExpansionModuleID3DigitalInputB.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID3DigitalInputB.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID3DigitalInputC = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8250)
)
unnamedAlarm2130ExpansionModuleID3DigitalInputC.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID3DigitalInputC.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID3DigitalInputD = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8251)
)
unnamedAlarm2130ExpansionModuleID3DigitalInputD.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID3DigitalInputD.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID3DigitalInputE = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8252)
)
unnamedAlarm2130ExpansionModuleID3DigitalInputE.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID3DigitalInputE.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID3DigitalInputF = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8253)
)
unnamedAlarm2130ExpansionModuleID3DigitalInputF.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID3DigitalInputF.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID3DigitalInputG = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8254)
)
unnamedAlarm2130ExpansionModuleID3DigitalInputG.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID3DigitalInputG.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID3DigitalInputH = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8255)
)
unnamedAlarm2130ExpansionModuleID3DigitalInputH.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID3DigitalInputH.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0DigitalInputA = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8256)
)
unnamedAlarm2131ExpansionModuleID0DigitalInputA.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0DigitalInputA.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0DigitalInputB = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8257)
)
unnamedAlarm2131ExpansionModuleID0DigitalInputB.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0DigitalInputB.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0DigitalInputC = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8258)
)
unnamedAlarm2131ExpansionModuleID0DigitalInputC.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0DigitalInputC.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0DigitalInputD = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8259)
)
unnamedAlarm2131ExpansionModuleID0DigitalInputD.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0DigitalInputD.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0DigitalInputE = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8260)
)
unnamedAlarm2131ExpansionModuleID0DigitalInputE.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0DigitalInputE.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0DigitalInputF = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8261)
)
unnamedAlarm2131ExpansionModuleID0DigitalInputF.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0DigitalInputF.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0DigitalInputG = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8262)
)
unnamedAlarm2131ExpansionModuleID0DigitalInputG.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0DigitalInputG.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0DigitalInputH = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8263)
)
unnamedAlarm2131ExpansionModuleID0DigitalInputH.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0DigitalInputH.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0DigitalInputI = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8264)
)
unnamedAlarm2131ExpansionModuleID0DigitalInputI.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0DigitalInputI.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0DigitalInputJ = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8265)
)
unnamedAlarm2131ExpansionModuleID0DigitalInputJ.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0DigitalInputJ.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1DigitalInputA = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8266)
)
unnamedAlarm2131ExpansionModuleID1DigitalInputA.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1DigitalInputA.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1DigitalInputB = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8267)
)
unnamedAlarm2131ExpansionModuleID1DigitalInputB.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1DigitalInputB.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1DigitalInputC = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8268)
)
unnamedAlarm2131ExpansionModuleID1DigitalInputC.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1DigitalInputC.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1DigitalInputD = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8269)
)
unnamedAlarm2131ExpansionModuleID1DigitalInputD.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1DigitalInputD.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1DigitalInputE = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8270)
)
unnamedAlarm2131ExpansionModuleID1DigitalInputE.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1DigitalInputE.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1DigitalInputF = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8271)
)
unnamedAlarm2131ExpansionModuleID1DigitalInputF.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1DigitalInputF.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1DigitalInputG = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8272)
)
unnamedAlarm2131ExpansionModuleID1DigitalInputG.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1DigitalInputG.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1DigitalInputH = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8273)
)
unnamedAlarm2131ExpansionModuleID1DigitalInputH.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1DigitalInputH.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1DigitalInputI = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8274)
)
unnamedAlarm2131ExpansionModuleID1DigitalInputI.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1DigitalInputI.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1DigitalInputJ = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8275)
)
unnamedAlarm2131ExpansionModuleID1DigitalInputJ.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1DigitalInputJ.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2DigitalInputA = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8276)
)
unnamedAlarm2131ExpansionModuleID2DigitalInputA.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2DigitalInputA.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2DigitalInputB = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8277)
)
unnamedAlarm2131ExpansionModuleID2DigitalInputB.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2DigitalInputB.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2DigitalInputC = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8278)
)
unnamedAlarm2131ExpansionModuleID2DigitalInputC.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2DigitalInputC.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2DigitalInputD = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8279)
)
unnamedAlarm2131ExpansionModuleID2DigitalInputD.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2DigitalInputD.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2DigitalInputE = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8280)
)
unnamedAlarm2131ExpansionModuleID2DigitalInputE.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2DigitalInputE.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2DigitalInputF = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8281)
)
unnamedAlarm2131ExpansionModuleID2DigitalInputF.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2DigitalInputF.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2DigitalInputG = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8282)
)
unnamedAlarm2131ExpansionModuleID2DigitalInputG.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2DigitalInputG.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2DigitalInputH = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8283)
)
unnamedAlarm2131ExpansionModuleID2DigitalInputH.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2DigitalInputH.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2DigitalInputI = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8284)
)
unnamedAlarm2131ExpansionModuleID2DigitalInputI.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2DigitalInputI.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2DigitalInputJ = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8285)
)
unnamedAlarm2131ExpansionModuleID2DigitalInputJ.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2DigitalInputJ.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3DigitalInputA = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8286)
)
unnamedAlarm2131ExpansionModuleID3DigitalInputA.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3DigitalInputA.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3DigitalInputB = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8287)
)
unnamedAlarm2131ExpansionModuleID3DigitalInputB.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3DigitalInputB.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3DigitalInputC = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8288)
)
unnamedAlarm2131ExpansionModuleID3DigitalInputC.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3DigitalInputC.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3DigitalInputD = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8289)
)
unnamedAlarm2131ExpansionModuleID3DigitalInputD.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3DigitalInputD.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3DigitalInputE = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8290)
)
unnamedAlarm2131ExpansionModuleID3DigitalInputE.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3DigitalInputE.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3DigitalInputF = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8291)
)
unnamedAlarm2131ExpansionModuleID3DigitalInputF.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3DigitalInputF.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3DigitalInputG = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8292)
)
unnamedAlarm2131ExpansionModuleID3DigitalInputG.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3DigitalInputG.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3DigitalInputH = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8293)
)
unnamedAlarm2131ExpansionModuleID3DigitalInputH.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3DigitalInputH.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3DigitalInputI = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8294)
)
unnamedAlarm2131ExpansionModuleID3DigitalInputI.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3DigitalInputI.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3DigitalInputJ = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8295)
)
unnamedAlarm2131ExpansionModuleID3DigitalInputJ.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3DigitalInputJ.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID0AnalogueInputELow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8304)
)
unnamedAlarm2130ExpansionModuleID0AnalogueInputELow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID0AnalogueInputELow.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID0AnalogueInputEHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8305)
)
unnamedAlarm2130ExpansionModuleID0AnalogueInputEHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID0AnalogueInputEHi.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID0AnalogueInputFLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8306)
)
unnamedAlarm2130ExpansionModuleID0AnalogueInputFLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID0AnalogueInputFLow.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID0AnalogueInputFHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8307)
)
unnamedAlarm2130ExpansionModuleID0AnalogueInputFHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID0AnalogueInputFHi.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID0AnalogueInputGLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8308)
)
unnamedAlarm2130ExpansionModuleID0AnalogueInputGLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID0AnalogueInputGLow.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID0AnalogueInputGHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8309)
)
unnamedAlarm2130ExpansionModuleID0AnalogueInputGHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID0AnalogueInputGHi.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID0AnalogueInputHLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8310)
)
unnamedAlarm2130ExpansionModuleID0AnalogueInputHLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID0AnalogueInputHLow.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID0AnalogueInputHHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8311)
)
unnamedAlarm2130ExpansionModuleID0AnalogueInputHHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID0AnalogueInputHHi.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID1AnalogueInputELow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8312)
)
unnamedAlarm2130ExpansionModuleID1AnalogueInputELow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID1AnalogueInputELow.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID1AnalogueInputEHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8313)
)
unnamedAlarm2130ExpansionModuleID1AnalogueInputEHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID1AnalogueInputEHi.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID1AnalogueInputFLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8314)
)
unnamedAlarm2130ExpansionModuleID1AnalogueInputFLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID1AnalogueInputFLow.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID1AnalogueInputFHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8315)
)
unnamedAlarm2130ExpansionModuleID1AnalogueInputFHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID1AnalogueInputFHi.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID1AnalogueInputGLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8316)
)
unnamedAlarm2130ExpansionModuleID1AnalogueInputGLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID1AnalogueInputGLow.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID1AnalogueInputGHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8317)
)
unnamedAlarm2130ExpansionModuleID1AnalogueInputGHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID1AnalogueInputGHi.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID1AnalogueInputHLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8318)
)
unnamedAlarm2130ExpansionModuleID1AnalogueInputHLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID1AnalogueInputHLow.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID1AnalogueInputHHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8319)
)
unnamedAlarm2130ExpansionModuleID1AnalogueInputHHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID1AnalogueInputHHi.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID2AnalogueInputELow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8320)
)
unnamedAlarm2130ExpansionModuleID2AnalogueInputELow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID2AnalogueInputELow.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID2AnalogueInputEHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8321)
)
unnamedAlarm2130ExpansionModuleID2AnalogueInputEHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID2AnalogueInputEHi.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID2AnalogueInputFLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8322)
)
unnamedAlarm2130ExpansionModuleID2AnalogueInputFLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID2AnalogueInputFLow.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID2AnalogueInputFHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8323)
)
unnamedAlarm2130ExpansionModuleID2AnalogueInputFHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID2AnalogueInputFHi.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID2AnalogueInputGLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8324)
)
unnamedAlarm2130ExpansionModuleID2AnalogueInputGLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID2AnalogueInputGLow.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID2AnalogueInputGHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8325)
)
unnamedAlarm2130ExpansionModuleID2AnalogueInputGHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID2AnalogueInputGHi.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID2AnalogueInputHLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8326)
)
unnamedAlarm2130ExpansionModuleID2AnalogueInputHLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID2AnalogueInputHLow.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID2AnalogueInputHHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8327)
)
unnamedAlarm2130ExpansionModuleID2AnalogueInputHHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID2AnalogueInputHHi.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID3AnalogueInputGLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8332)
)
unnamedAlarm2130ExpansionModuleID3AnalogueInputGLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID3AnalogueInputGLow.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID3AnalogueInputGHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8333)
)
unnamedAlarm2130ExpansionModuleID3AnalogueInputGHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID3AnalogueInputGHi.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID3AnalogueInputHLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8334)
)
unnamedAlarm2130ExpansionModuleID3AnalogueInputHLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID3AnalogueInputHLow.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID3AnalogueInputHHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8335)
)
unnamedAlarm2130ExpansionModuleID3AnalogueInputHHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID3AnalogueInputHHi.setStatus(
        "current"
    )

unnamedAlarmFlexibleSensorBLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8386)
)
unnamedAlarmFlexibleSensorBLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmFlexibleSensorBLow.setStatus(
        "current"
    )

unnamedAlarmFlexibleSensorBHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8387)
)
unnamedAlarmFlexibleSensorBHigh.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmFlexibleSensorBHigh.setStatus(
        "current"
    )

unnamedAlarmFlexibleSensorCLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8388)
)
unnamedAlarmFlexibleSensorCLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmFlexibleSensorCLow.setStatus(
        "current"
    )

unnamedAlarmFlexibleSensorCHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8389)
)
unnamedAlarmFlexibleSensorCHigh.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmFlexibleSensorCHigh.setStatus(
        "current"
    )

unnamedAlarmFlexibleSensorDLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8390)
)
unnamedAlarmFlexibleSensorDLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmFlexibleSensorDLow.setStatus(
        "current"
    )

unnamedAlarmFlexibleSensorDHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8391)
)
unnamedAlarmFlexibleSensorDHigh.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmFlexibleSensorDHigh.setStatus(
        "current"
    )

unnamedAlarmMaintenanceAlarm1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8394)
)
unnamedAlarmMaintenanceAlarm1.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmMaintenanceAlarm1.setStatus(
        "current"
    )

unnamedAlarmMaintenanceAlarm2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8395)
)
unnamedAlarmMaintenanceAlarm2.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmMaintenanceAlarm2.setStatus(
        "current"
    )

unnamedAlarmMaintenanceAlarm3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8396)
)
unnamedAlarmMaintenanceAlarm3.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmMaintenanceAlarm3.setStatus(
        "current"
    )

unnamedAlarmPLCAlarm1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8397)
)
unnamedAlarmPLCAlarm1.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmPLCAlarm1.setStatus(
        "current"
    )

unnamedAlarmPLCAlarm2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8398)
)
unnamedAlarmPLCAlarm2.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmPLCAlarm2.setStatus(
        "current"
    )

unnamedAlarmPLCAlarm3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8399)
)
unnamedAlarmPLCAlarm3.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmPLCAlarm3.setStatus(
        "current"
    )

unnamedAlarmPLCAlarm4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8400)
)
unnamedAlarmPLCAlarm4.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmPLCAlarm4.setStatus(
        "current"
    )

unnamedAlarmPLCAlarm5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8401)
)
unnamedAlarmPLCAlarm5.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmPLCAlarm5.setStatus(
        "current"
    )

unnamedAlarmPLCAlarm6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8402)
)
unnamedAlarmPLCAlarm6.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmPLCAlarm6.setStatus(
        "current"
    )

unnamedAlarmPLCAlarm7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8403)
)
unnamedAlarmPLCAlarm7.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmPLCAlarm7.setStatus(
        "current"
    )

unnamedAlarmPLCAlarm8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8404)
)
unnamedAlarmPLCAlarm8.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmPLCAlarm8.setStatus(
        "current"
    )

unnamedAlarmPLCAlarm9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8405)
)
unnamedAlarmPLCAlarm9.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmPLCAlarm9.setStatus(
        "current"
    )

unnamedAlarmPLCAlarm10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8406)
)
unnamedAlarmPLCAlarm10.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmPLCAlarm10.setStatus(
        "current"
    )

unnamedAlarmPLCAlarm11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8407)
)
unnamedAlarmPLCAlarm11.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmPLCAlarm11.setStatus(
        "current"
    )

unnamedAlarmPLCAlarm12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8408)
)
unnamedAlarmPLCAlarm12.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmPLCAlarm12.setStatus(
        "current"
    )

unnamedAlarmPLCAlarm13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8409)
)
unnamedAlarmPLCAlarm13.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmPLCAlarm13.setStatus(
        "current"
    )

unnamedAlarmPLCAlarm14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8410)
)
unnamedAlarmPLCAlarm14.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmPLCAlarm14.setStatus(
        "current"
    )

unnamedAlarmPLCAlarm15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8411)
)
unnamedAlarmPLCAlarm15.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmPLCAlarm15.setStatus(
        "current"
    )

unnamedAlarmPLCAlarm16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8412)
)
unnamedAlarmPLCAlarm16.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmPLCAlarm16.setStatus(
        "current"
    )

unnamedAlarmPLCAlarm17 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8413)
)
unnamedAlarmPLCAlarm17.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmPLCAlarm17.setStatus(
        "current"
    )

unnamedAlarmPLCAlarm18 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8414)
)
unnamedAlarmPLCAlarm18.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmPLCAlarm18.setStatus(
        "current"
    )

unnamedAlarmPLCAlarm19 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8415)
)
unnamedAlarmPLCAlarm19.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmPLCAlarm19.setStatus(
        "current"
    )

unnamedAlarmPLCAlarm20 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8416)
)
unnamedAlarmPLCAlarm20.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmPLCAlarm20.setStatus(
        "current"
    )

unnamedAlarmLowLoad = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8437)
)
unnamedAlarmLowLoad.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmLowLoad.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0AnalogueInputALow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8444)
)
unnamedAlarm2131ExpansionModuleID0AnalogueInputALow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0AnalogueInputALow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0AnalogueInputAHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8445)
)
unnamedAlarm2131ExpansionModuleID0AnalogueInputAHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0AnalogueInputAHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0AnalogueInputBLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8446)
)
unnamedAlarm2131ExpansionModuleID0AnalogueInputBLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0AnalogueInputBLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0AnalogueInputBHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8447)
)
unnamedAlarm2131ExpansionModuleID0AnalogueInputBHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0AnalogueInputBHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0AnalogueInputCLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8448)
)
unnamedAlarm2131ExpansionModuleID0AnalogueInputCLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0AnalogueInputCLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0AnalogueInputCHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8449)
)
unnamedAlarm2131ExpansionModuleID0AnalogueInputCHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0AnalogueInputCHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0AnalogueInputDLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8450)
)
unnamedAlarm2131ExpansionModuleID0AnalogueInputDLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0AnalogueInputDLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0AnalogueInputDHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8451)
)
unnamedAlarm2131ExpansionModuleID0AnalogueInputDHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0AnalogueInputDHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0AnalogueInputELow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8452)
)
unnamedAlarm2131ExpansionModuleID0AnalogueInputELow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0AnalogueInputELow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0AnalogueInputEHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8453)
)
unnamedAlarm2131ExpansionModuleID0AnalogueInputEHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0AnalogueInputEHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0AnalogueInputFLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8454)
)
unnamedAlarm2131ExpansionModuleID0AnalogueInputFLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0AnalogueInputFLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0AnalogueInputFHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8455)
)
unnamedAlarm2131ExpansionModuleID0AnalogueInputFHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0AnalogueInputFHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0AnalogueInputGLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8456)
)
unnamedAlarm2131ExpansionModuleID0AnalogueInputGLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0AnalogueInputGLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0AnalogueInputGHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8457)
)
unnamedAlarm2131ExpansionModuleID0AnalogueInputGHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0AnalogueInputGHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0AnalogueInputHLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8458)
)
unnamedAlarm2131ExpansionModuleID0AnalogueInputHLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0AnalogueInputHLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0AnalogueInputHHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8459)
)
unnamedAlarm2131ExpansionModuleID0AnalogueInputHHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0AnalogueInputHHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0AnalogueInputILow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8460)
)
unnamedAlarm2131ExpansionModuleID0AnalogueInputILow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0AnalogueInputILow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0AnalogueInputIHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8461)
)
unnamedAlarm2131ExpansionModuleID0AnalogueInputIHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0AnalogueInputIHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0AnalogueInputJLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8462)
)
unnamedAlarm2131ExpansionModuleID0AnalogueInputJLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0AnalogueInputJLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID0AnalogueInputJHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8463)
)
unnamedAlarm2131ExpansionModuleID0AnalogueInputJHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID0AnalogueInputJHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1AnalogueInputALow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8464)
)
unnamedAlarm2131ExpansionModuleID1AnalogueInputALow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1AnalogueInputALow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1AnalogueInputAHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8465)
)
unnamedAlarm2131ExpansionModuleID1AnalogueInputAHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1AnalogueInputAHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1AnalogueInputBLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8466)
)
unnamedAlarm2131ExpansionModuleID1AnalogueInputBLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1AnalogueInputBLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1AnalogueInputBHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8467)
)
unnamedAlarm2131ExpansionModuleID1AnalogueInputBHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1AnalogueInputBHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1AnalogueInputCLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8468)
)
unnamedAlarm2131ExpansionModuleID1AnalogueInputCLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1AnalogueInputCLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1AnalogueInputCHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8469)
)
unnamedAlarm2131ExpansionModuleID1AnalogueInputCHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1AnalogueInputCHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1AnalogueInputDLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8470)
)
unnamedAlarm2131ExpansionModuleID1AnalogueInputDLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1AnalogueInputDLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1AnalogueInputDHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8471)
)
unnamedAlarm2131ExpansionModuleID1AnalogueInputDHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1AnalogueInputDHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1AnalogueInputELow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8472)
)
unnamedAlarm2131ExpansionModuleID1AnalogueInputELow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1AnalogueInputELow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1AnalogueInputEHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8473)
)
unnamedAlarm2131ExpansionModuleID1AnalogueInputEHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1AnalogueInputEHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1AnalogueInputFLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8474)
)
unnamedAlarm2131ExpansionModuleID1AnalogueInputFLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1AnalogueInputFLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1AnalogueInputFHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8475)
)
unnamedAlarm2131ExpansionModuleID1AnalogueInputFHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1AnalogueInputFHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1AnalogueInputGLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8476)
)
unnamedAlarm2131ExpansionModuleID1AnalogueInputGLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1AnalogueInputGLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1AnalogueInputGHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8477)
)
unnamedAlarm2131ExpansionModuleID1AnalogueInputGHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1AnalogueInputGHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1AnalogueInputHLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8478)
)
unnamedAlarm2131ExpansionModuleID1AnalogueInputHLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1AnalogueInputHLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1AnalogueInputHHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8479)
)
unnamedAlarm2131ExpansionModuleID1AnalogueInputHHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1AnalogueInputHHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1AnalogueInputILow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8480)
)
unnamedAlarm2131ExpansionModuleID1AnalogueInputILow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1AnalogueInputILow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1AnalogueInputIHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8481)
)
unnamedAlarm2131ExpansionModuleID1AnalogueInputIHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1AnalogueInputIHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1AnalogueInputJLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8482)
)
unnamedAlarm2131ExpansionModuleID1AnalogueInputJLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1AnalogueInputJLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID1AnalogueInputJHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8483)
)
unnamedAlarm2131ExpansionModuleID1AnalogueInputJHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID1AnalogueInputJHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2AnalogueInputALow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8484)
)
unnamedAlarm2131ExpansionModuleID2AnalogueInputALow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2AnalogueInputALow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2AnalogueInputAHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8485)
)
unnamedAlarm2131ExpansionModuleID2AnalogueInputAHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2AnalogueInputAHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2AnalogueInputBLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8486)
)
unnamedAlarm2131ExpansionModuleID2AnalogueInputBLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2AnalogueInputBLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2AnalogueInputBHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8487)
)
unnamedAlarm2131ExpansionModuleID2AnalogueInputBHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2AnalogueInputBHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2AnalogueInputCLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8488)
)
unnamedAlarm2131ExpansionModuleID2AnalogueInputCLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2AnalogueInputCLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2AnalogueInputCHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8489)
)
unnamedAlarm2131ExpansionModuleID2AnalogueInputCHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2AnalogueInputCHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2AnalogueInputDLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8490)
)
unnamedAlarm2131ExpansionModuleID2AnalogueInputDLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2AnalogueInputDLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2AnalogueInputDHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8491)
)
unnamedAlarm2131ExpansionModuleID2AnalogueInputDHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2AnalogueInputDHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2AnalogueInputELow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8492)
)
unnamedAlarm2131ExpansionModuleID2AnalogueInputELow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2AnalogueInputELow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2AnalogueInputEHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8493)
)
unnamedAlarm2131ExpansionModuleID2AnalogueInputEHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2AnalogueInputEHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2AnalogueInputFLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8494)
)
unnamedAlarm2131ExpansionModuleID2AnalogueInputFLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2AnalogueInputFLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2AnalogueInputFHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8495)
)
unnamedAlarm2131ExpansionModuleID2AnalogueInputFHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2AnalogueInputFHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2AnalogueInputGLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8496)
)
unnamedAlarm2131ExpansionModuleID2AnalogueInputGLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2AnalogueInputGLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2AnalogueInputGHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8497)
)
unnamedAlarm2131ExpansionModuleID2AnalogueInputGHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2AnalogueInputGHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2AnalogueInputHLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8498)
)
unnamedAlarm2131ExpansionModuleID2AnalogueInputHLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2AnalogueInputHLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2AnalogueInputHHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8499)
)
unnamedAlarm2131ExpansionModuleID2AnalogueInputHHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2AnalogueInputHHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2AnalogueInputILow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8500)
)
unnamedAlarm2131ExpansionModuleID2AnalogueInputILow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2AnalogueInputILow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2AnalogueInputIHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8501)
)
unnamedAlarm2131ExpansionModuleID2AnalogueInputIHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2AnalogueInputIHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2AnalogueInputJLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8502)
)
unnamedAlarm2131ExpansionModuleID2AnalogueInputJLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2AnalogueInputJLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID2AnalogueInputJHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8503)
)
unnamedAlarm2131ExpansionModuleID2AnalogueInputJHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID2AnalogueInputJHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3AnalogueInputALow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8504)
)
unnamedAlarm2131ExpansionModuleID3AnalogueInputALow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3AnalogueInputALow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3AnalogueInputAHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8505)
)
unnamedAlarm2131ExpansionModuleID3AnalogueInputAHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3AnalogueInputAHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3AnalogueInputBLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8506)
)
unnamedAlarm2131ExpansionModuleID3AnalogueInputBLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3AnalogueInputBLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3AnalogueInputBHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8507)
)
unnamedAlarm2131ExpansionModuleID3AnalogueInputBHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3AnalogueInputBHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3AnalogueInputCLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8508)
)
unnamedAlarm2131ExpansionModuleID3AnalogueInputCLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3AnalogueInputCLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3AnalogueInputCHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8509)
)
unnamedAlarm2131ExpansionModuleID3AnalogueInputCHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3AnalogueInputCHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3AnalogueInputDLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8510)
)
unnamedAlarm2131ExpansionModuleID3AnalogueInputDLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3AnalogueInputDLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3AnalogueInputDHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8511)
)
unnamedAlarm2131ExpansionModuleID3AnalogueInputDHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3AnalogueInputDHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3AnalogueInputELow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8512)
)
unnamedAlarm2131ExpansionModuleID3AnalogueInputELow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3AnalogueInputELow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3AnalogueInputEHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8513)
)
unnamedAlarm2131ExpansionModuleID3AnalogueInputEHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3AnalogueInputEHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3AnalogueInputFLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8514)
)
unnamedAlarm2131ExpansionModuleID3AnalogueInputFLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3AnalogueInputFLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3AnalogueInputFHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8515)
)
unnamedAlarm2131ExpansionModuleID3AnalogueInputFHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3AnalogueInputFHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3AnalogueInputGLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8516)
)
unnamedAlarm2131ExpansionModuleID3AnalogueInputGLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3AnalogueInputGLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3AnalogueInputGHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8517)
)
unnamedAlarm2131ExpansionModuleID3AnalogueInputGHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3AnalogueInputGHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3AnalogueInputHLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8518)
)
unnamedAlarm2131ExpansionModuleID3AnalogueInputHLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3AnalogueInputHLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3AnalogueInputHHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8519)
)
unnamedAlarm2131ExpansionModuleID3AnalogueInputHHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3AnalogueInputHHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3AnalogueInputILow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8520)
)
unnamedAlarm2131ExpansionModuleID3AnalogueInputILow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3AnalogueInputILow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3AnalogueInputIHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8521)
)
unnamedAlarm2131ExpansionModuleID3AnalogueInputIHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3AnalogueInputIHi.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3AnalogueInputJLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8522)
)
unnamedAlarm2131ExpansionModuleID3AnalogueInputJLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3AnalogueInputJLow.setStatus(
        "current"
    )

unnamedAlarm2131ExpansionModuleID3AnalogueInputJHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8523)
)
unnamedAlarm2131ExpansionModuleID3AnalogueInputJHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2131ExpansionModuleID3AnalogueInputJHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID0AnalogueInputALow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8524)
)
unnamedAlarm2133ExpansionModuleID0AnalogueInputALow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID0AnalogueInputALow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID0AnalogueInputAHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8525)
)
unnamedAlarm2133ExpansionModuleID0AnalogueInputAHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID0AnalogueInputAHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID0AnalogueInputBLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8526)
)
unnamedAlarm2133ExpansionModuleID0AnalogueInputBLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID0AnalogueInputBLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID0AnalogueInputBHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8527)
)
unnamedAlarm2133ExpansionModuleID0AnalogueInputBHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID0AnalogueInputBHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID0AnalogueInputCLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8528)
)
unnamedAlarm2133ExpansionModuleID0AnalogueInputCLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID0AnalogueInputCLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID0AnalogueInputCHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8529)
)
unnamedAlarm2133ExpansionModuleID0AnalogueInputCHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID0AnalogueInputCHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID0AnalogueInputDLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8530)
)
unnamedAlarm2133ExpansionModuleID0AnalogueInputDLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID0AnalogueInputDLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID0AnalogueInputDHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8531)
)
unnamedAlarm2133ExpansionModuleID0AnalogueInputDHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID0AnalogueInputDHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID0AnalogueInputELow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8532)
)
unnamedAlarm2133ExpansionModuleID0AnalogueInputELow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID0AnalogueInputELow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID0AnalogueInputEHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8533)
)
unnamedAlarm2133ExpansionModuleID0AnalogueInputEHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID0AnalogueInputEHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID0AnalogueInputFLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8534)
)
unnamedAlarm2133ExpansionModuleID0AnalogueInputFLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID0AnalogueInputFLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID0AnalogueInputFHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8535)
)
unnamedAlarm2133ExpansionModuleID0AnalogueInputFHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID0AnalogueInputFHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID0AnalogueInputGLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8536)
)
unnamedAlarm2133ExpansionModuleID0AnalogueInputGLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID0AnalogueInputGLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID0AnalogueInputGHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8537)
)
unnamedAlarm2133ExpansionModuleID0AnalogueInputGHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID0AnalogueInputGHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID0AnalogueInputHLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8538)
)
unnamedAlarm2133ExpansionModuleID0AnalogueInputHLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID0AnalogueInputHLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID0AnalogueInputHHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8539)
)
unnamedAlarm2133ExpansionModuleID0AnalogueInputHHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID0AnalogueInputHHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID1AnalogueInputALow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8540)
)
unnamedAlarm2133ExpansionModuleID1AnalogueInputALow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID1AnalogueInputALow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID1AnalogueInputAHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8541)
)
unnamedAlarm2133ExpansionModuleID1AnalogueInputAHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID1AnalogueInputAHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID1AnalogueInputBLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8542)
)
unnamedAlarm2133ExpansionModuleID1AnalogueInputBLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID1AnalogueInputBLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID1AnalogueInputBHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8543)
)
unnamedAlarm2133ExpansionModuleID1AnalogueInputBHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID1AnalogueInputBHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID1AnalogueInputCLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8544)
)
unnamedAlarm2133ExpansionModuleID1AnalogueInputCLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID1AnalogueInputCLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID1AnalogueInputCHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8545)
)
unnamedAlarm2133ExpansionModuleID1AnalogueInputCHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID1AnalogueInputCHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID1AnalogueInputDLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8546)
)
unnamedAlarm2133ExpansionModuleID1AnalogueInputDLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID1AnalogueInputDLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID1AnalogueInputDHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8547)
)
unnamedAlarm2133ExpansionModuleID1AnalogueInputDHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID1AnalogueInputDHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID1AnalogueInputELow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8548)
)
unnamedAlarm2133ExpansionModuleID1AnalogueInputELow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID1AnalogueInputELow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID1AnalogueInputEHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8549)
)
unnamedAlarm2133ExpansionModuleID1AnalogueInputEHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID1AnalogueInputEHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID1AnalogueInputFLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8550)
)
unnamedAlarm2133ExpansionModuleID1AnalogueInputFLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID1AnalogueInputFLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID1AnalogueInputFHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8551)
)
unnamedAlarm2133ExpansionModuleID1AnalogueInputFHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID1AnalogueInputFHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID1AnalogueInputGLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8552)
)
unnamedAlarm2133ExpansionModuleID1AnalogueInputGLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID1AnalogueInputGLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID1AnalogueInputGHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8553)
)
unnamedAlarm2133ExpansionModuleID1AnalogueInputGHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID1AnalogueInputGHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID1AnalogueInputHLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8554)
)
unnamedAlarm2133ExpansionModuleID1AnalogueInputHLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID1AnalogueInputHLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID1AnalogueInputHHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8555)
)
unnamedAlarm2133ExpansionModuleID1AnalogueInputHHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID1AnalogueInputHHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID2AnalogueInputALow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8556)
)
unnamedAlarm2133ExpansionModuleID2AnalogueInputALow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID2AnalogueInputALow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID2AnalogueInputAHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8557)
)
unnamedAlarm2133ExpansionModuleID2AnalogueInputAHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID2AnalogueInputAHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID2AnalogueInputBLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8558)
)
unnamedAlarm2133ExpansionModuleID2AnalogueInputBLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID2AnalogueInputBLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID2AnalogueInputBHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8559)
)
unnamedAlarm2133ExpansionModuleID2AnalogueInputBHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID2AnalogueInputBHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID2AnalogueInputCLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8560)
)
unnamedAlarm2133ExpansionModuleID2AnalogueInputCLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID2AnalogueInputCLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID2AnalogueInputCHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8561)
)
unnamedAlarm2133ExpansionModuleID2AnalogueInputCHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID2AnalogueInputCHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID2AnalogueInputDLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8562)
)
unnamedAlarm2133ExpansionModuleID2AnalogueInputDLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID2AnalogueInputDLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID2AnalogueInputDHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8563)
)
unnamedAlarm2133ExpansionModuleID2AnalogueInputDHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID2AnalogueInputDHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID2AnalogueInputELow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8564)
)
unnamedAlarm2133ExpansionModuleID2AnalogueInputELow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID2AnalogueInputELow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID2AnalogueInputEHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8565)
)
unnamedAlarm2133ExpansionModuleID2AnalogueInputEHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID2AnalogueInputEHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID2AnalogueInputFLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8566)
)
unnamedAlarm2133ExpansionModuleID2AnalogueInputFLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID2AnalogueInputFLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID2AnalogueInputFHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8567)
)
unnamedAlarm2133ExpansionModuleID2AnalogueInputFHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID2AnalogueInputFHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID2AnalogueInputGLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8568)
)
unnamedAlarm2133ExpansionModuleID2AnalogueInputGLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID2AnalogueInputGLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID2AnalogueInputGHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8569)
)
unnamedAlarm2133ExpansionModuleID2AnalogueInputGHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID2AnalogueInputGHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID2AnalogueInputHLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8570)
)
unnamedAlarm2133ExpansionModuleID2AnalogueInputHLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID2AnalogueInputHLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID2AnalogueInputHHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8571)
)
unnamedAlarm2133ExpansionModuleID2AnalogueInputHHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID2AnalogueInputHHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID3AnalogueInputALow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8572)
)
unnamedAlarm2133ExpansionModuleID3AnalogueInputALow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID3AnalogueInputALow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID3AnalogueInputAHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8573)
)
unnamedAlarm2133ExpansionModuleID3AnalogueInputAHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID3AnalogueInputAHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID3AnalogueInputBLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8574)
)
unnamedAlarm2133ExpansionModuleID3AnalogueInputBLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID3AnalogueInputBLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID3AnalogueInputBHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8575)
)
unnamedAlarm2133ExpansionModuleID3AnalogueInputBHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID3AnalogueInputBHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID3AnalogueInputCLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8576)
)
unnamedAlarm2133ExpansionModuleID3AnalogueInputCLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID3AnalogueInputCLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID3AnalogueInputCHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8577)
)
unnamedAlarm2133ExpansionModuleID3AnalogueInputCHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID3AnalogueInputCHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID3AnalogueInputDLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8578)
)
unnamedAlarm2133ExpansionModuleID3AnalogueInputDLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID3AnalogueInputDLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID3AnalogueInputDHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8579)
)
unnamedAlarm2133ExpansionModuleID3AnalogueInputDHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID3AnalogueInputDHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID3AnalogueInputELow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8580)
)
unnamedAlarm2133ExpansionModuleID3AnalogueInputELow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID3AnalogueInputELow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID3AnalogueInputEHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8581)
)
unnamedAlarm2133ExpansionModuleID3AnalogueInputEHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID3AnalogueInputEHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID3AnalogueInputFLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8582)
)
unnamedAlarm2133ExpansionModuleID3AnalogueInputFLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID3AnalogueInputFLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID3AnalogueInputFHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8583)
)
unnamedAlarm2133ExpansionModuleID3AnalogueInputFHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID3AnalogueInputFHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID3AnalogueInputGLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8584)
)
unnamedAlarm2133ExpansionModuleID3AnalogueInputGLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID3AnalogueInputGLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID3AnalogueInputGHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8585)
)
unnamedAlarm2133ExpansionModuleID3AnalogueInputGHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID3AnalogueInputGHi.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID3AnalogueInputHLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8586)
)
unnamedAlarm2133ExpansionModuleID3AnalogueInputHLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID3AnalogueInputHLow.setStatus(
        "current"
    )

unnamedAlarm2133ExpansionModuleID3AnalogueInputHHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8587)
)
unnamedAlarm2133ExpansionModuleID3AnalogueInputHHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2133ExpansionModuleID3AnalogueInputHHi.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID3AnalogueInputELow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8616)
)
unnamedAlarm2130ExpansionModuleID3AnalogueInputELow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID3AnalogueInputELow.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID3AnalogueInputEHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8617)
)
unnamedAlarm2130ExpansionModuleID3AnalogueInputEHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID3AnalogueInputEHi.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID3AnalogueInputFLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8618)
)
unnamedAlarm2130ExpansionModuleID3AnalogueInputFLow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID3AnalogueInputFLow.setStatus(
        "current"
    )

unnamedAlarm2130ExpansionModuleID3AnalogueInputFHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8619)
)
unnamedAlarm2130ExpansionModuleID3AnalogueInputFHi.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarm2130ExpansionModuleID3AnalogueInputFHi.setStatus(
        "current"
    )

unnamedAlarmAnalogueInputADigital = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8737)
)
unnamedAlarmAnalogueInputADigital.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmAnalogueInputADigital.setStatus(
        "current"
    )

unnamedAlarmFlexibleSensorALow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8738)
)
unnamedAlarmFlexibleSensorALow.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmFlexibleSensorALow.setStatus(
        "current"
    )

unnamedAlarmFlexibleSensorAHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8739)
)
unnamedAlarmFlexibleSensorAHigh.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmFlexibleSensorAHigh.setStatus(
        "current"
    )

unnamedAlarmChargerID0CommonShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8754)
)
unnamedAlarmChargerID0CommonShutdown.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmChargerID0CommonShutdown.setStatus(
        "current"
    )

unnamedAlarmChargerID0CommonWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8755)
)
unnamedAlarmChargerID0CommonWarning.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmChargerID0CommonWarning.setStatus(
        "current"
    )

unnamedAlarmChargerID1CommonShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8756)
)
unnamedAlarmChargerID1CommonShutdown.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmChargerID1CommonShutdown.setStatus(
        "current"
    )

unnamedAlarmChargerID1CommonWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8757)
)
unnamedAlarmChargerID1CommonWarning.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmChargerID1CommonWarning.setStatus(
        "current"
    )

unnamedAlarmChargerID2CommonShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8758)
)
unnamedAlarmChargerID2CommonShutdown.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmChargerID2CommonShutdown.setStatus(
        "current"
    )

unnamedAlarmChargerID2CommonWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8759)
)
unnamedAlarmChargerID2CommonWarning.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmChargerID2CommonWarning.setStatus(
        "current"
    )

unnamedAlarmChargerID3CommonShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8760)
)
unnamedAlarmChargerID3CommonShutdown.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmChargerID3CommonShutdown.setStatus(
        "current"
    )

unnamedAlarmChargerID3CommonWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 8761)
)
unnamedAlarmChargerID3CommonWarning.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    unnamedAlarmChargerID3CommonWarning.setStatus(
        "current"
    )

notifModuleRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 12297)
)
notifModuleRestart.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    notifModuleRestart.setStatus(
        "current"
    )

notifEngineStops = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 12299)
)
notifEngineStops.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    notifEngineStops.setStatus(
        "current"
    )

notifMainsFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 12391)
)
notifMainsFail.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    notifMainsFail.setStatus(
        "current"
    )

notifMainsReturn = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 12392)
)
notifMainsReturn.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    notifMainsReturn.setStatus(
        "current"
    )

notifEngineStarts = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 12591)
)
notifEngineStarts.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    notifEngineStarts.setStatus(
        "current"
    )

notifModeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 16384)
)
notifModeChange.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    notifModeChange.setStatus(
        "current"
    )

notifECUlampProtect = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 20480)
)
notifECUlampProtect.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    notifECUlampProtect.setStatus(
        "current"
    )

notifECUlampMalfunction = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 20481)
)
notifECUlampMalfunction.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    notifECUlampMalfunction.setStatus(
        "current"
    )

notifECUlampShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 20482)
)
notifECUlampShutdown.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    notifECUlampShutdown.setStatus(
        "current"
    )

notifECUlampWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 20483)
)
notifECUlampWarning.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    notifECUlampWarning.setStatus(
        "current"
    )

notifLevelStatusMonitoring = NotificationType(
    (1, 3, 6, 1, 4, 1, 41385, 1, 0, 24576)
)
notifLevelStatusMonitoring.setObjects(
      *(("DSE-8610-MIB", "dse8610SeqNr"),
        ("DSE-8610-MIB", "dse8610TrapID"),
        ("DSE-8610-MIB", "dse8610TrapState"),
        ("DSE-8610-MIB", "dse8610TrapTimeStamp"))
)
if mibBuilder.loadTexts:
    notifLevelStatusMonitoring.setStatus(
        "current"
    )


# Notifications groups

snmpBasicNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 100, 2, 11)
)
snmpBasicNotificationsGroup.setObjects(
      *(("DSE-8610-MIB", "namedAlarmEmergencyStop"),
        ("DSE-8610-MIB", "namedAlarmLowOilPressure"),
        ("DSE-8610-MIB", "namedAlarmHighCoolantTemp"),
        ("DSE-8610-MIB", "namedAlarmLowCoolantTemp"),
        ("DSE-8610-MIB", "namedAlarmUnderSpeed"),
        ("DSE-8610-MIB", "namedAlarmOverSpeed"),
        ("DSE-8610-MIB", "namedAlarmGeneratorUnderFrequency"),
        ("DSE-8610-MIB", "namedAlarmGeneratorOverFrequency"),
        ("DSE-8610-MIB", "namedAlarmGeneratorUnderVolts"),
        ("DSE-8610-MIB", "namedAlarmGeneratorOverVolts"),
        ("DSE-8610-MIB", "namedAlarmBatteryUnderVolts"),
        ("DSE-8610-MIB", "namedAlarmBatteryOverVolts"),
        ("DSE-8610-MIB", "namedAlarmChargeAlternatorFailure"),
        ("DSE-8610-MIB", "namedAlarmFailToStart"),
        ("DSE-8610-MIB", "namedAlarmFailToStop"),
        ("DSE-8610-MIB", "namedAlarmGeneratorFailedToClose"),
        ("DSE-8610-MIB", "namedAlarmMainsFailedToClose"),
        ("DSE-8610-MIB", "namedAlarmOilPressureSensorOpenCircuit"),
        ("DSE-8610-MIB", "namedAlarmLossOfMagPickupSignal"),
        ("DSE-8610-MIB", "namedAlarmMagPickupOpenCircuit"),
        ("DSE-8610-MIB", "namedAlarmGeneratorOverCurrent"),
        ("DSE-8610-MIB", "namedAlarmCalibrationLost"),
        ("DSE-8610-MIB", "namedAlarmLowFuelLevel"),
        ("DSE-8610-MIB", "namedAlarmECUAmber"),
        ("DSE-8610-MIB", "namedAlarmECURed"),
        ("DSE-8610-MIB", "namedAlarmECUDataFail"),
        ("DSE-8610-MIB", "namedAlarmLowOilPressureSwitchAlarm"),
        ("DSE-8610-MIB", "namedAlarmHighTemperatureSwitchAlarm"),
        ("DSE-8610-MIB", "namedAlarmLowFuelSwitchAlarm"),
        ("DSE-8610-MIB", "namedAlarmExpansionUnitWatchdogAlarm"),
        ("DSE-8610-MIB", "namedAlarmkWOverloadAlarm"),
        ("DSE-8610-MIB", "namedAlarmNegativePhaseSequenceAlarm"),
        ("DSE-8610-MIB", "namedAlarmEarthFaultTrip"),
        ("DSE-8610-MIB", "namedAlarmGeneratorPhaseRotationAlarm"),
        ("DSE-8610-MIB", "namedAlarmAutoVoltageSenseFail"),
        ("DSE-8610-MIB", "namedAlarmMaintenanceAlarm"),
        ("DSE-8610-MIB", "namedAlarmFailtoReachLoadingVoltage"),
        ("DSE-8610-MIB", "namedAlarmFuelUsageRunning"),
        ("DSE-8610-MIB", "namedAlarmFuelUsageStopped"),
        ("DSE-8610-MIB", "namedAlarmProtectionsDisabled"),
        ("DSE-8610-MIB", "namedAlarmGeneratorBreakerFailedToOpen"),
        ("DSE-8610-MIB", "namedAlarmMainsBreakerFailedToOpen"),
        ("DSE-8610-MIB", "namedAlarmBusBreakerFailedToClose"),
        ("DSE-8610-MIB", "namedAlarmBusBreakerFailedToOpen"),
        ("DSE-8610-MIB", "namedAlarmGeneratorReversePowerAlarm"),
        ("DSE-8610-MIB", "namedAlarmShortCircuitAlarm"),
        ("DSE-8610-MIB", "namedAlarmAirFlapClosedAlarm"),
        ("DSE-8610-MIB", "namedAlarmFailToSync"),
        ("DSE-8610-MIB", "namedAlarmBusLive"),
        ("DSE-8610-MIB", "namedAlarmBusNotLive"),
        ("DSE-8610-MIB", "namedAlarmBusPhaseRotation"),
        ("DSE-8610-MIB", "namedAlarmPrioritySelectionError"),
        ("DSE-8610-MIB", "namedAlarmMSCDataError"),
        ("DSE-8610-MIB", "namedAlarmMSCIDError"),
        ("DSE-8610-MIB", "namedAlarmBusLowVoltage"),
        ("DSE-8610-MIB", "namedAlarmBusHighVoltage"),
        ("DSE-8610-MIB", "namedAlarmBusLowFrequency"),
        ("DSE-8610-MIB", "namedAlarmBusHighFrequency"),
        ("DSE-8610-MIB", "namedAlarmMSCFailure"),
        ("DSE-8610-MIB", "namedAlarmMSCTooFewSets"),
        ("DSE-8610-MIB", "namedAlarmMSCAlarmsInhibited"),
        ("DSE-8610-MIB", "namedAlarmMSCOldVersionUnitsOnTheBus"),
        ("DSE-8610-MIB", "namedAlarmMainsReversePowerAlarm"),
        ("DSE-8610-MIB", "namedAlarmMinimumSetsNotReached"),
        ("DSE-8610-MIB", "namedAlarmInsufficientCapacity"),
        ("DSE-8610-MIB", "namedAlarmOutOfSync"),
        ("DSE-8610-MIB", "namedAlarmAlternativeAuxMainsFail"),
        ("DSE-8610-MIB", "namedAlarmLossOfExcitation"),
        ("DSE-8610-MIB", "namedAlarmMainsROCOF"),
        ("DSE-8610-MIB", "namedAlarmMainsVectorShift"),
        ("DSE-8610-MIB", "namedAlarmMainsDecouplingLowFrequency"),
        ("DSE-8610-MIB", "namedAlarmMainsDecouplingHighFrequency"),
        ("DSE-8610-MIB", "namedAlarmMainsDecouplingLowVoltage"),
        ("DSE-8610-MIB", "namedAlarmMainsDecouplingHighVoltage"),
        ("DSE-8610-MIB", "namedAlarmMainsDecouplingCombinedAlarm"),
        ("DSE-8610-MIB", "namedAlarmMainsPhaseRotationAlarm"),
        ("DSE-8610-MIB", "namedAlarmAVRMaxTrimLimitAlarm"),
        ("DSE-8610-MIB", "namedAlarmHighCoolantTempElecTripAlarm"),
        ("DSE-8610-MIB", "namedAlarmTempSenderOpenCircuitAlarm"),
        ("DSE-8610-MIB", "namedAlarmFailtoReachLoadingFrequency"),
        ("DSE-8610-MIB", "namedAlarmProtectionsBlocked"),
        ("DSE-8610-MIB", "namedAlarmOutOfSyncBus"),
        ("DSE-8610-MIB", "namedAlarmOutOfSyncMains"),
        ("DSE-8610-MIB", "namedAlarmECUControlledHeaters"),
        ("DSE-8610-MIB", "namedAlarmECUControlledCoolers"),
        ("DSE-8610-MIB", "namedAlarmECUProtect"),
        ("DSE-8610-MIB", "namedAlarmECUMalfunction"),
        ("DSE-8610-MIB", "namedAlarmIndication"),
        ("DSE-8610-MIB", "namedAlarmWaterinFuel"),
        ("DSE-8610-MIB", "namedAlarmHESTActive"),
        ("DSE-8610-MIB", "namedAlarmDPTCFilter"),
        ("DSE-8610-MIB", "namedAlarmHighFuelLevel"),
        ("DSE-8610-MIB", "namedAlarmHeaterSensorFailureAlarm"),
        ("DSE-8610-MIB", "namedAlarmDEFLevelLow"),
        ("DSE-8610-MIB", "namedAlarmSCRInducement"),
        ("DSE-8610-MIB", "namedAlarmInletTemperature"),
        ("DSE-8610-MIB", "namedAlarmElectricalTripStopInhibited"),
        ("DSE-8610-MIB", "namedAlarmFuelTankBundLevelHigh"),
        ("DSE-8610-MIB", "namedAlarmMSCLink1DataError"),
        ("DSE-8610-MIB", "namedAlarmMSCLink2DataError"),
        ("DSE-8610-MIB", "namedAlarmMSCLink1Failure"),
        ("DSE-8610-MIB", "namedAlarmMSCLink2Failure"),
        ("DSE-8610-MIB", "namedAlarmMSCLink1TooFewSets"),
        ("DSE-8610-MIB", "namedAlarmMSCLink2TooFewSets"),
        ("DSE-8610-MIB", "namedAlarmMSCLink1and2Failure"),
        ("DSE-8610-MIB", "namedAlarmElectricalTripfrom8660"),
        ("DSE-8610-MIB", "unnamedAlarmDigitalInputA"),
        ("DSE-8610-MIB", "unnamedAlarmDigitalInputB"),
        ("DSE-8610-MIB", "unnamedAlarmDigitalInputC"),
        ("DSE-8610-MIB", "unnamedAlarmDigitalInputD"),
        ("DSE-8610-MIB", "unnamedAlarmDigitalInputE"),
        ("DSE-8610-MIB", "unnamedAlarmDigitalInputF"),
        ("DSE-8610-MIB", "unnamedAlarmDigitalInputG"),
        ("DSE-8610-MIB", "unnamedAlarmDigitalInputH"),
        ("DSE-8610-MIB", "unnamedAlarmDigitalInputI"),
        ("DSE-8610-MIB", "unnamedAlarmDigitalInputJ"),
        ("DSE-8610-MIB", "unnamedAlarmDigitalInputK"),
        ("DSE-8610-MIB", "unnamedAlarmDigitalInputL"),
        ("DSE-8610-MIB", "unnamedAlarmAnalogueInputBDigital"),
        ("DSE-8610-MIB", "unnamedAlarmAnalogueInputCDigital"),
        ("DSE-8610-MIB", "unnamedAlarmAnalogueInputDDigital"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID0DigitalInputA"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID0DigitalInputB"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID0DigitalInputC"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID0DigitalInputD"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID0DigitalInputE"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID0DigitalInputF"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID0DigitalInputG"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID0DigitalInputH"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID1DigitalInputA"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID1DigitalInputB"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID1DigitalInputC"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID1DigitalInputD"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID1DigitalInputE"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID1DigitalInputF"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID1DigitalInputG"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID1DigitalInputH"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID2DigitalInputA"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID2DigitalInputB"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID2DigitalInputC"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID2DigitalInputD"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID2DigitalInputE"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID2DigitalInputF"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID2DigitalInputG"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID2DigitalInputH"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID3DigitalInputA"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID3DigitalInputB"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID3DigitalInputC"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID3DigitalInputD"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID3DigitalInputE"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID3DigitalInputF"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID3DigitalInputG"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID3DigitalInputH"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0DigitalInputA"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0DigitalInputB"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0DigitalInputC"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0DigitalInputD"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0DigitalInputE"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0DigitalInputF"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0DigitalInputG"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0DigitalInputH"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0DigitalInputI"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0DigitalInputJ"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1DigitalInputA"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1DigitalInputB"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1DigitalInputC"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1DigitalInputD"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1DigitalInputE"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1DigitalInputF"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1DigitalInputG"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1DigitalInputH"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1DigitalInputI"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1DigitalInputJ"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2DigitalInputA"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2DigitalInputB"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2DigitalInputC"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2DigitalInputD"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2DigitalInputE"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2DigitalInputF"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2DigitalInputG"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2DigitalInputH"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2DigitalInputI"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2DigitalInputJ"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3DigitalInputA"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3DigitalInputB"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3DigitalInputC"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3DigitalInputD"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3DigitalInputE"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3DigitalInputF"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3DigitalInputG"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3DigitalInputH"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3DigitalInputI"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3DigitalInputJ"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID0AnalogueInputELow"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID0AnalogueInputEHi"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID0AnalogueInputFLow"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID0AnalogueInputFHi"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID0AnalogueInputGLow"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID0AnalogueInputGHi"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID0AnalogueInputHLow"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID0AnalogueInputHHi"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID1AnalogueInputELow"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID1AnalogueInputEHi"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID1AnalogueInputFLow"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID1AnalogueInputFHi"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID1AnalogueInputGLow"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID1AnalogueInputGHi"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID1AnalogueInputHLow"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID1AnalogueInputHHi"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID2AnalogueInputELow"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID2AnalogueInputEHi"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID2AnalogueInputFLow"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID2AnalogueInputFHi"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID2AnalogueInputGLow"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID2AnalogueInputGHi"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID2AnalogueInputHLow"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID2AnalogueInputHHi"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID3AnalogueInputGLow"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID3AnalogueInputGHi"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID3AnalogueInputHLow"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID3AnalogueInputHHi"),
        ("DSE-8610-MIB", "unnamedAlarmFlexibleSensorBLow"),
        ("DSE-8610-MIB", "unnamedAlarmFlexibleSensorBHigh"),
        ("DSE-8610-MIB", "unnamedAlarmFlexibleSensorCLow"),
        ("DSE-8610-MIB", "unnamedAlarmFlexibleSensorCHigh"),
        ("DSE-8610-MIB", "unnamedAlarmFlexibleSensorDLow"),
        ("DSE-8610-MIB", "unnamedAlarmFlexibleSensorDHigh"),
        ("DSE-8610-MIB", "unnamedAlarmMaintenanceAlarm1"),
        ("DSE-8610-MIB", "unnamedAlarmMaintenanceAlarm2"),
        ("DSE-8610-MIB", "unnamedAlarmMaintenanceAlarm3"),
        ("DSE-8610-MIB", "unnamedAlarmPLCAlarm1"),
        ("DSE-8610-MIB", "unnamedAlarmPLCAlarm2"),
        ("DSE-8610-MIB", "unnamedAlarmPLCAlarm3"),
        ("DSE-8610-MIB", "unnamedAlarmPLCAlarm4"),
        ("DSE-8610-MIB", "unnamedAlarmPLCAlarm5"),
        ("DSE-8610-MIB", "unnamedAlarmPLCAlarm6"),
        ("DSE-8610-MIB", "unnamedAlarmPLCAlarm7"),
        ("DSE-8610-MIB", "unnamedAlarmPLCAlarm8"),
        ("DSE-8610-MIB", "unnamedAlarmPLCAlarm9"),
        ("DSE-8610-MIB", "unnamedAlarmPLCAlarm10"),
        ("DSE-8610-MIB", "unnamedAlarmPLCAlarm11"),
        ("DSE-8610-MIB", "unnamedAlarmPLCAlarm12"),
        ("DSE-8610-MIB", "unnamedAlarmPLCAlarm13"),
        ("DSE-8610-MIB", "unnamedAlarmPLCAlarm14"),
        ("DSE-8610-MIB", "unnamedAlarmPLCAlarm15"),
        ("DSE-8610-MIB", "unnamedAlarmPLCAlarm16"),
        ("DSE-8610-MIB", "unnamedAlarmPLCAlarm17"),
        ("DSE-8610-MIB", "unnamedAlarmPLCAlarm18"),
        ("DSE-8610-MIB", "unnamedAlarmPLCAlarm19"),
        ("DSE-8610-MIB", "unnamedAlarmPLCAlarm20"),
        ("DSE-8610-MIB", "unnamedAlarmLowLoad"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0AnalogueInputALow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0AnalogueInputAHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0AnalogueInputBLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0AnalogueInputBHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0AnalogueInputCLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0AnalogueInputCHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0AnalogueInputDLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0AnalogueInputDHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0AnalogueInputELow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0AnalogueInputEHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0AnalogueInputFLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0AnalogueInputFHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0AnalogueInputGLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0AnalogueInputGHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0AnalogueInputHLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0AnalogueInputHHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0AnalogueInputILow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0AnalogueInputIHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0AnalogueInputJLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID0AnalogueInputJHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1AnalogueInputALow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1AnalogueInputAHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1AnalogueInputBLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1AnalogueInputBHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1AnalogueInputCLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1AnalogueInputCHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1AnalogueInputDLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1AnalogueInputDHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1AnalogueInputELow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1AnalogueInputEHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1AnalogueInputFLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1AnalogueInputFHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1AnalogueInputGLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1AnalogueInputGHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1AnalogueInputHLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1AnalogueInputHHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1AnalogueInputILow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1AnalogueInputIHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1AnalogueInputJLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID1AnalogueInputJHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2AnalogueInputALow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2AnalogueInputAHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2AnalogueInputBLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2AnalogueInputBHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2AnalogueInputCLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2AnalogueInputCHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2AnalogueInputDLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2AnalogueInputDHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2AnalogueInputELow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2AnalogueInputEHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2AnalogueInputFLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2AnalogueInputFHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2AnalogueInputGLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2AnalogueInputGHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2AnalogueInputHLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2AnalogueInputHHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2AnalogueInputILow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2AnalogueInputIHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2AnalogueInputJLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID2AnalogueInputJHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3AnalogueInputALow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3AnalogueInputAHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3AnalogueInputBLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3AnalogueInputBHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3AnalogueInputCLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3AnalogueInputCHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3AnalogueInputDLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3AnalogueInputDHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3AnalogueInputELow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3AnalogueInputEHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3AnalogueInputFLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3AnalogueInputFHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3AnalogueInputGLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3AnalogueInputGHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3AnalogueInputHLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3AnalogueInputHHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3AnalogueInputILow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3AnalogueInputIHi"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3AnalogueInputJLow"),
        ("DSE-8610-MIB", "unnamedAlarm2131ExpansionModuleID3AnalogueInputJHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID0AnalogueInputALow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID0AnalogueInputAHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID0AnalogueInputBLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID0AnalogueInputBHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID0AnalogueInputCLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID0AnalogueInputCHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID0AnalogueInputDLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID0AnalogueInputDHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID0AnalogueInputELow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID0AnalogueInputEHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID0AnalogueInputFLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID0AnalogueInputFHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID0AnalogueInputGLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID0AnalogueInputGHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID0AnalogueInputHLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID0AnalogueInputHHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID1AnalogueInputALow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID1AnalogueInputAHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID1AnalogueInputBLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID1AnalogueInputBHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID1AnalogueInputCLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID1AnalogueInputCHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID1AnalogueInputDLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID1AnalogueInputDHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID1AnalogueInputELow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID1AnalogueInputEHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID1AnalogueInputFLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID1AnalogueInputFHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID1AnalogueInputGLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID1AnalogueInputGHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID1AnalogueInputHLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID1AnalogueInputHHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID2AnalogueInputALow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID2AnalogueInputAHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID2AnalogueInputBLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID2AnalogueInputBHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID2AnalogueInputCLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID2AnalogueInputCHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID2AnalogueInputDLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID2AnalogueInputDHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID2AnalogueInputELow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID2AnalogueInputEHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID2AnalogueInputFLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID2AnalogueInputFHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID2AnalogueInputGLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID2AnalogueInputGHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID2AnalogueInputHLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID2AnalogueInputHHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID3AnalogueInputALow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID3AnalogueInputAHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID3AnalogueInputBLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID3AnalogueInputBHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID3AnalogueInputCLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID3AnalogueInputCHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID3AnalogueInputDLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID3AnalogueInputDHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID3AnalogueInputELow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID3AnalogueInputEHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID3AnalogueInputFLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID3AnalogueInputFHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID3AnalogueInputGLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID3AnalogueInputGHi"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID3AnalogueInputHLow"),
        ("DSE-8610-MIB", "unnamedAlarm2133ExpansionModuleID3AnalogueInputHHi"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID3AnalogueInputELow"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID3AnalogueInputEHi"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID3AnalogueInputFLow"),
        ("DSE-8610-MIB", "unnamedAlarm2130ExpansionModuleID3AnalogueInputFHi"),
        ("DSE-8610-MIB", "unnamedAlarmAnalogueInputADigital"),
        ("DSE-8610-MIB", "unnamedAlarmFlexibleSensorALow"),
        ("DSE-8610-MIB", "unnamedAlarmFlexibleSensorAHigh"),
        ("DSE-8610-MIB", "unnamedAlarmChargerID0CommonShutdown"),
        ("DSE-8610-MIB", "unnamedAlarmChargerID0CommonWarning"),
        ("DSE-8610-MIB", "unnamedAlarmChargerID1CommonShutdown"),
        ("DSE-8610-MIB", "unnamedAlarmChargerID1CommonWarning"),
        ("DSE-8610-MIB", "unnamedAlarmChargerID2CommonShutdown"),
        ("DSE-8610-MIB", "unnamedAlarmChargerID2CommonWarning"),
        ("DSE-8610-MIB", "unnamedAlarmChargerID3CommonShutdown"),
        ("DSE-8610-MIB", "unnamedAlarmChargerID3CommonWarning"),
        ("DSE-8610-MIB", "notifModeChange"),
        ("DSE-8610-MIB", "notifModuleRestart"),
        ("DSE-8610-MIB", "notifEngineStarts"),
        ("DSE-8610-MIB", "notifEngineStops"),
        ("DSE-8610-MIB", "notifMainsFail"),
        ("DSE-8610-MIB", "notifMainsReturn"),
        ("DSE-8610-MIB", "notifECUlampProtect"),
        ("DSE-8610-MIB", "notifECUlampMalfunction"),
        ("DSE-8610-MIB", "notifECUlampShutdown"),
        ("DSE-8610-MIB", "notifECUlampWarning"),
        ("DSE-8610-MIB", "notifLevelStatusMonitoring"))
)
if mibBuilder.loadTexts:
    snmpBasicNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

snmpBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 41385, 1, 5, 100, 1, 1)
)
snmpBasicCompliance.setObjects(
      *(("DSE-8610-MIB", "generatorGroup"),
        ("DSE-8610-MIB", "engineGroup"),
        ("DSE-8610-MIB", "busGroup"),
        ("DSE-8610-MIB", "gencommP166Group"),
        ("DSE-8610-MIB", "gencommP167Group"),
        ("DSE-8610-MIB", "gencommP168Group"),
        ("DSE-8610-MIB", "gencommP169Group"),
        ("DSE-8610-MIB", "keypressGroup"),
        ("DSE-8610-MIB", "trapVarsGroup"),
        ("DSE-8610-MIB", "snmpBasicNotificationsGroup"),
        ("DSE-8610-MIB", "trapVarsGroup"))
)
if mibBuilder.loadTexts:
    snmpBasicCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DSE-8610-MIB",
    **{"ChargeVoltsDiv10": ChargeVoltsDiv10,
       "FreqDiv10": FreqDiv10,
       "VoltsLNDiv10": VoltsLNDiv10,
       "VoltsLLDiv10": VoltsLLDiv10,
       "CurrentDiv10": CurrentDiv10,
       "RPMDiv1000": RPMDiv1000,
       "AirFilterDiv10": AirFilterDiv10,
       "ElectricalPotentialDiv10": ElectricalPotentialDiv10,
       "AverageFuelDiv100": AverageFuelDiv100,
       "PowerFactorDiv100": PowerFactorDiv100,
       "PowerPCDiv10": PowerPCDiv10,
       "VAPCDiv10": VAPCDiv10,
       "PowerPCDiv100": PowerPCDiv100,
       "CrankPressureDiv100": CrankPressureDiv100,
       "InjectorRailPressureDiv100": InjectorRailPressureDiv100,
       "OilPressureDiv100": OilPressureDiv100,
       "dseVendor": dseVendor,
       "dseProduct": dseProduct,
       "ucdTraps": ucdTraps,
       "namedAlarmEmergencyStop": namedAlarmEmergencyStop,
       "namedAlarmLowOilPressure": namedAlarmLowOilPressure,
       "namedAlarmHighCoolantTemp": namedAlarmHighCoolantTemp,
       "namedAlarmLowCoolantTemp": namedAlarmLowCoolantTemp,
       "namedAlarmUnderSpeed": namedAlarmUnderSpeed,
       "namedAlarmOverSpeed": namedAlarmOverSpeed,
       "namedAlarmGeneratorUnderFrequency": namedAlarmGeneratorUnderFrequency,
       "namedAlarmGeneratorOverFrequency": namedAlarmGeneratorOverFrequency,
       "namedAlarmGeneratorUnderVolts": namedAlarmGeneratorUnderVolts,
       "namedAlarmGeneratorOverVolts": namedAlarmGeneratorOverVolts,
       "namedAlarmBatteryUnderVolts": namedAlarmBatteryUnderVolts,
       "namedAlarmBatteryOverVolts": namedAlarmBatteryOverVolts,
       "namedAlarmChargeAlternatorFailure": namedAlarmChargeAlternatorFailure,
       "namedAlarmFailToStart": namedAlarmFailToStart,
       "namedAlarmFailToStop": namedAlarmFailToStop,
       "namedAlarmGeneratorFailedToClose": namedAlarmGeneratorFailedToClose,
       "namedAlarmMainsFailedToClose": namedAlarmMainsFailedToClose,
       "namedAlarmOilPressureSensorOpenCircuit": namedAlarmOilPressureSensorOpenCircuit,
       "namedAlarmLossOfMagPickupSignal": namedAlarmLossOfMagPickupSignal,
       "namedAlarmMagPickupOpenCircuit": namedAlarmMagPickupOpenCircuit,
       "namedAlarmGeneratorOverCurrent": namedAlarmGeneratorOverCurrent,
       "namedAlarmCalibrationLost": namedAlarmCalibrationLost,
       "namedAlarmLowFuelLevel": namedAlarmLowFuelLevel,
       "namedAlarmECUAmber": namedAlarmECUAmber,
       "namedAlarmECURed": namedAlarmECURed,
       "namedAlarmECUDataFail": namedAlarmECUDataFail,
       "namedAlarmLowOilPressureSwitchAlarm": namedAlarmLowOilPressureSwitchAlarm,
       "namedAlarmHighTemperatureSwitchAlarm": namedAlarmHighTemperatureSwitchAlarm,
       "namedAlarmLowFuelSwitchAlarm": namedAlarmLowFuelSwitchAlarm,
       "namedAlarmExpansionUnitWatchdogAlarm": namedAlarmExpansionUnitWatchdogAlarm,
       "namedAlarmkWOverloadAlarm": namedAlarmkWOverloadAlarm,
       "namedAlarmNegativePhaseSequenceAlarm": namedAlarmNegativePhaseSequenceAlarm,
       "namedAlarmEarthFaultTrip": namedAlarmEarthFaultTrip,
       "namedAlarmGeneratorPhaseRotationAlarm": namedAlarmGeneratorPhaseRotationAlarm,
       "namedAlarmAutoVoltageSenseFail": namedAlarmAutoVoltageSenseFail,
       "namedAlarmMaintenanceAlarm": namedAlarmMaintenanceAlarm,
       "namedAlarmFailtoReachLoadingVoltage": namedAlarmFailtoReachLoadingVoltage,
       "namedAlarmFuelUsageRunning": namedAlarmFuelUsageRunning,
       "namedAlarmFuelUsageStopped": namedAlarmFuelUsageStopped,
       "namedAlarmProtectionsDisabled": namedAlarmProtectionsDisabled,
       "namedAlarmGeneratorBreakerFailedToOpen": namedAlarmGeneratorBreakerFailedToOpen,
       "namedAlarmMainsBreakerFailedToOpen": namedAlarmMainsBreakerFailedToOpen,
       "namedAlarmBusBreakerFailedToClose": namedAlarmBusBreakerFailedToClose,
       "namedAlarmBusBreakerFailedToOpen": namedAlarmBusBreakerFailedToOpen,
       "namedAlarmGeneratorReversePowerAlarm": namedAlarmGeneratorReversePowerAlarm,
       "namedAlarmShortCircuitAlarm": namedAlarmShortCircuitAlarm,
       "namedAlarmAirFlapClosedAlarm": namedAlarmAirFlapClosedAlarm,
       "namedAlarmFailToSync": namedAlarmFailToSync,
       "namedAlarmBusLive": namedAlarmBusLive,
       "namedAlarmBusNotLive": namedAlarmBusNotLive,
       "namedAlarmBusPhaseRotation": namedAlarmBusPhaseRotation,
       "namedAlarmPrioritySelectionError": namedAlarmPrioritySelectionError,
       "namedAlarmMSCDataError": namedAlarmMSCDataError,
       "namedAlarmMSCIDError": namedAlarmMSCIDError,
       "namedAlarmBusLowVoltage": namedAlarmBusLowVoltage,
       "namedAlarmBusHighVoltage": namedAlarmBusHighVoltage,
       "namedAlarmBusLowFrequency": namedAlarmBusLowFrequency,
       "namedAlarmBusHighFrequency": namedAlarmBusHighFrequency,
       "namedAlarmMSCFailure": namedAlarmMSCFailure,
       "namedAlarmMSCTooFewSets": namedAlarmMSCTooFewSets,
       "namedAlarmMSCAlarmsInhibited": namedAlarmMSCAlarmsInhibited,
       "namedAlarmMSCOldVersionUnitsOnTheBus": namedAlarmMSCOldVersionUnitsOnTheBus,
       "namedAlarmMainsReversePowerAlarm": namedAlarmMainsReversePowerAlarm,
       "namedAlarmMinimumSetsNotReached": namedAlarmMinimumSetsNotReached,
       "namedAlarmInsufficientCapacity": namedAlarmInsufficientCapacity,
       "namedAlarmOutOfSync": namedAlarmOutOfSync,
       "namedAlarmAlternativeAuxMainsFail": namedAlarmAlternativeAuxMainsFail,
       "namedAlarmLossOfExcitation": namedAlarmLossOfExcitation,
       "namedAlarmMainsROCOF": namedAlarmMainsROCOF,
       "namedAlarmMainsVectorShift": namedAlarmMainsVectorShift,
       "namedAlarmMainsDecouplingLowFrequency": namedAlarmMainsDecouplingLowFrequency,
       "namedAlarmMainsDecouplingHighFrequency": namedAlarmMainsDecouplingHighFrequency,
       "namedAlarmMainsDecouplingLowVoltage": namedAlarmMainsDecouplingLowVoltage,
       "namedAlarmMainsDecouplingHighVoltage": namedAlarmMainsDecouplingHighVoltage,
       "namedAlarmMainsDecouplingCombinedAlarm": namedAlarmMainsDecouplingCombinedAlarm,
       "namedAlarmMainsPhaseRotationAlarm": namedAlarmMainsPhaseRotationAlarm,
       "namedAlarmAVRMaxTrimLimitAlarm": namedAlarmAVRMaxTrimLimitAlarm,
       "namedAlarmHighCoolantTempElecTripAlarm": namedAlarmHighCoolantTempElecTripAlarm,
       "namedAlarmTempSenderOpenCircuitAlarm": namedAlarmTempSenderOpenCircuitAlarm,
       "namedAlarmFailtoReachLoadingFrequency": namedAlarmFailtoReachLoadingFrequency,
       "namedAlarmProtectionsBlocked": namedAlarmProtectionsBlocked,
       "namedAlarmOutOfSyncBus": namedAlarmOutOfSyncBus,
       "namedAlarmOutOfSyncMains": namedAlarmOutOfSyncMains,
       "namedAlarmECUControlledHeaters": namedAlarmECUControlledHeaters,
       "namedAlarmECUControlledCoolers": namedAlarmECUControlledCoolers,
       "namedAlarmECUProtect": namedAlarmECUProtect,
       "namedAlarmECUMalfunction": namedAlarmECUMalfunction,
       "namedAlarmIndication": namedAlarmIndication,
       "namedAlarmWaterinFuel": namedAlarmWaterinFuel,
       "namedAlarmHESTActive": namedAlarmHESTActive,
       "namedAlarmDPTCFilter": namedAlarmDPTCFilter,
       "namedAlarmHighFuelLevel": namedAlarmHighFuelLevel,
       "namedAlarmHeaterSensorFailureAlarm": namedAlarmHeaterSensorFailureAlarm,
       "namedAlarmDEFLevelLow": namedAlarmDEFLevelLow,
       "namedAlarmSCRInducement": namedAlarmSCRInducement,
       "namedAlarmInletTemperature": namedAlarmInletTemperature,
       "namedAlarmElectricalTripStopInhibited": namedAlarmElectricalTripStopInhibited,
       "namedAlarmFuelTankBundLevelHigh": namedAlarmFuelTankBundLevelHigh,
       "namedAlarmMSCLink1DataError": namedAlarmMSCLink1DataError,
       "namedAlarmMSCLink2DataError": namedAlarmMSCLink2DataError,
       "namedAlarmMSCLink1Failure": namedAlarmMSCLink1Failure,
       "namedAlarmMSCLink2Failure": namedAlarmMSCLink2Failure,
       "namedAlarmMSCLink1TooFewSets": namedAlarmMSCLink1TooFewSets,
       "namedAlarmMSCLink2TooFewSets": namedAlarmMSCLink2TooFewSets,
       "namedAlarmMSCLink1and2Failure": namedAlarmMSCLink1and2Failure,
       "namedAlarmElectricalTripfrom8660": namedAlarmElectricalTripfrom8660,
       "unnamedAlarmDigitalInputA": unnamedAlarmDigitalInputA,
       "unnamedAlarmDigitalInputB": unnamedAlarmDigitalInputB,
       "unnamedAlarmDigitalInputC": unnamedAlarmDigitalInputC,
       "unnamedAlarmDigitalInputD": unnamedAlarmDigitalInputD,
       "unnamedAlarmDigitalInputE": unnamedAlarmDigitalInputE,
       "unnamedAlarmDigitalInputF": unnamedAlarmDigitalInputF,
       "unnamedAlarmDigitalInputG": unnamedAlarmDigitalInputG,
       "unnamedAlarmDigitalInputH": unnamedAlarmDigitalInputH,
       "unnamedAlarmDigitalInputI": unnamedAlarmDigitalInputI,
       "unnamedAlarmDigitalInputJ": unnamedAlarmDigitalInputJ,
       "unnamedAlarmDigitalInputK": unnamedAlarmDigitalInputK,
       "unnamedAlarmDigitalInputL": unnamedAlarmDigitalInputL,
       "unnamedAlarmAnalogueInputBDigital": unnamedAlarmAnalogueInputBDigital,
       "unnamedAlarmAnalogueInputCDigital": unnamedAlarmAnalogueInputCDigital,
       "unnamedAlarmAnalogueInputDDigital": unnamedAlarmAnalogueInputDDigital,
       "unnamedAlarm2130ExpansionModuleID0DigitalInputA": unnamedAlarm2130ExpansionModuleID0DigitalInputA,
       "unnamedAlarm2130ExpansionModuleID0DigitalInputB": unnamedAlarm2130ExpansionModuleID0DigitalInputB,
       "unnamedAlarm2130ExpansionModuleID0DigitalInputC": unnamedAlarm2130ExpansionModuleID0DigitalInputC,
       "unnamedAlarm2130ExpansionModuleID0DigitalInputD": unnamedAlarm2130ExpansionModuleID0DigitalInputD,
       "unnamedAlarm2130ExpansionModuleID0DigitalInputE": unnamedAlarm2130ExpansionModuleID0DigitalInputE,
       "unnamedAlarm2130ExpansionModuleID0DigitalInputF": unnamedAlarm2130ExpansionModuleID0DigitalInputF,
       "unnamedAlarm2130ExpansionModuleID0DigitalInputG": unnamedAlarm2130ExpansionModuleID0DigitalInputG,
       "unnamedAlarm2130ExpansionModuleID0DigitalInputH": unnamedAlarm2130ExpansionModuleID0DigitalInputH,
       "unnamedAlarm2130ExpansionModuleID1DigitalInputA": unnamedAlarm2130ExpansionModuleID1DigitalInputA,
       "unnamedAlarm2130ExpansionModuleID1DigitalInputB": unnamedAlarm2130ExpansionModuleID1DigitalInputB,
       "unnamedAlarm2130ExpansionModuleID1DigitalInputC": unnamedAlarm2130ExpansionModuleID1DigitalInputC,
       "unnamedAlarm2130ExpansionModuleID1DigitalInputD": unnamedAlarm2130ExpansionModuleID1DigitalInputD,
       "unnamedAlarm2130ExpansionModuleID1DigitalInputE": unnamedAlarm2130ExpansionModuleID1DigitalInputE,
       "unnamedAlarm2130ExpansionModuleID1DigitalInputF": unnamedAlarm2130ExpansionModuleID1DigitalInputF,
       "unnamedAlarm2130ExpansionModuleID1DigitalInputG": unnamedAlarm2130ExpansionModuleID1DigitalInputG,
       "unnamedAlarm2130ExpansionModuleID1DigitalInputH": unnamedAlarm2130ExpansionModuleID1DigitalInputH,
       "unnamedAlarm2130ExpansionModuleID2DigitalInputA": unnamedAlarm2130ExpansionModuleID2DigitalInputA,
       "unnamedAlarm2130ExpansionModuleID2DigitalInputB": unnamedAlarm2130ExpansionModuleID2DigitalInputB,
       "unnamedAlarm2130ExpansionModuleID2DigitalInputC": unnamedAlarm2130ExpansionModuleID2DigitalInputC,
       "unnamedAlarm2130ExpansionModuleID2DigitalInputD": unnamedAlarm2130ExpansionModuleID2DigitalInputD,
       "unnamedAlarm2130ExpansionModuleID2DigitalInputE": unnamedAlarm2130ExpansionModuleID2DigitalInputE,
       "unnamedAlarm2130ExpansionModuleID2DigitalInputF": unnamedAlarm2130ExpansionModuleID2DigitalInputF,
       "unnamedAlarm2130ExpansionModuleID2DigitalInputG": unnamedAlarm2130ExpansionModuleID2DigitalInputG,
       "unnamedAlarm2130ExpansionModuleID2DigitalInputH": unnamedAlarm2130ExpansionModuleID2DigitalInputH,
       "unnamedAlarm2130ExpansionModuleID3DigitalInputA": unnamedAlarm2130ExpansionModuleID3DigitalInputA,
       "unnamedAlarm2130ExpansionModuleID3DigitalInputB": unnamedAlarm2130ExpansionModuleID3DigitalInputB,
       "unnamedAlarm2130ExpansionModuleID3DigitalInputC": unnamedAlarm2130ExpansionModuleID3DigitalInputC,
       "unnamedAlarm2130ExpansionModuleID3DigitalInputD": unnamedAlarm2130ExpansionModuleID3DigitalInputD,
       "unnamedAlarm2130ExpansionModuleID3DigitalInputE": unnamedAlarm2130ExpansionModuleID3DigitalInputE,
       "unnamedAlarm2130ExpansionModuleID3DigitalInputF": unnamedAlarm2130ExpansionModuleID3DigitalInputF,
       "unnamedAlarm2130ExpansionModuleID3DigitalInputG": unnamedAlarm2130ExpansionModuleID3DigitalInputG,
       "unnamedAlarm2130ExpansionModuleID3DigitalInputH": unnamedAlarm2130ExpansionModuleID3DigitalInputH,
       "unnamedAlarm2131ExpansionModuleID0DigitalInputA": unnamedAlarm2131ExpansionModuleID0DigitalInputA,
       "unnamedAlarm2131ExpansionModuleID0DigitalInputB": unnamedAlarm2131ExpansionModuleID0DigitalInputB,
       "unnamedAlarm2131ExpansionModuleID0DigitalInputC": unnamedAlarm2131ExpansionModuleID0DigitalInputC,
       "unnamedAlarm2131ExpansionModuleID0DigitalInputD": unnamedAlarm2131ExpansionModuleID0DigitalInputD,
       "unnamedAlarm2131ExpansionModuleID0DigitalInputE": unnamedAlarm2131ExpansionModuleID0DigitalInputE,
       "unnamedAlarm2131ExpansionModuleID0DigitalInputF": unnamedAlarm2131ExpansionModuleID0DigitalInputF,
       "unnamedAlarm2131ExpansionModuleID0DigitalInputG": unnamedAlarm2131ExpansionModuleID0DigitalInputG,
       "unnamedAlarm2131ExpansionModuleID0DigitalInputH": unnamedAlarm2131ExpansionModuleID0DigitalInputH,
       "unnamedAlarm2131ExpansionModuleID0DigitalInputI": unnamedAlarm2131ExpansionModuleID0DigitalInputI,
       "unnamedAlarm2131ExpansionModuleID0DigitalInputJ": unnamedAlarm2131ExpansionModuleID0DigitalInputJ,
       "unnamedAlarm2131ExpansionModuleID1DigitalInputA": unnamedAlarm2131ExpansionModuleID1DigitalInputA,
       "unnamedAlarm2131ExpansionModuleID1DigitalInputB": unnamedAlarm2131ExpansionModuleID1DigitalInputB,
       "unnamedAlarm2131ExpansionModuleID1DigitalInputC": unnamedAlarm2131ExpansionModuleID1DigitalInputC,
       "unnamedAlarm2131ExpansionModuleID1DigitalInputD": unnamedAlarm2131ExpansionModuleID1DigitalInputD,
       "unnamedAlarm2131ExpansionModuleID1DigitalInputE": unnamedAlarm2131ExpansionModuleID1DigitalInputE,
       "unnamedAlarm2131ExpansionModuleID1DigitalInputF": unnamedAlarm2131ExpansionModuleID1DigitalInputF,
       "unnamedAlarm2131ExpansionModuleID1DigitalInputG": unnamedAlarm2131ExpansionModuleID1DigitalInputG,
       "unnamedAlarm2131ExpansionModuleID1DigitalInputH": unnamedAlarm2131ExpansionModuleID1DigitalInputH,
       "unnamedAlarm2131ExpansionModuleID1DigitalInputI": unnamedAlarm2131ExpansionModuleID1DigitalInputI,
       "unnamedAlarm2131ExpansionModuleID1DigitalInputJ": unnamedAlarm2131ExpansionModuleID1DigitalInputJ,
       "unnamedAlarm2131ExpansionModuleID2DigitalInputA": unnamedAlarm2131ExpansionModuleID2DigitalInputA,
       "unnamedAlarm2131ExpansionModuleID2DigitalInputB": unnamedAlarm2131ExpansionModuleID2DigitalInputB,
       "unnamedAlarm2131ExpansionModuleID2DigitalInputC": unnamedAlarm2131ExpansionModuleID2DigitalInputC,
       "unnamedAlarm2131ExpansionModuleID2DigitalInputD": unnamedAlarm2131ExpansionModuleID2DigitalInputD,
       "unnamedAlarm2131ExpansionModuleID2DigitalInputE": unnamedAlarm2131ExpansionModuleID2DigitalInputE,
       "unnamedAlarm2131ExpansionModuleID2DigitalInputF": unnamedAlarm2131ExpansionModuleID2DigitalInputF,
       "unnamedAlarm2131ExpansionModuleID2DigitalInputG": unnamedAlarm2131ExpansionModuleID2DigitalInputG,
       "unnamedAlarm2131ExpansionModuleID2DigitalInputH": unnamedAlarm2131ExpansionModuleID2DigitalInputH,
       "unnamedAlarm2131ExpansionModuleID2DigitalInputI": unnamedAlarm2131ExpansionModuleID2DigitalInputI,
       "unnamedAlarm2131ExpansionModuleID2DigitalInputJ": unnamedAlarm2131ExpansionModuleID2DigitalInputJ,
       "unnamedAlarm2131ExpansionModuleID3DigitalInputA": unnamedAlarm2131ExpansionModuleID3DigitalInputA,
       "unnamedAlarm2131ExpansionModuleID3DigitalInputB": unnamedAlarm2131ExpansionModuleID3DigitalInputB,
       "unnamedAlarm2131ExpansionModuleID3DigitalInputC": unnamedAlarm2131ExpansionModuleID3DigitalInputC,
       "unnamedAlarm2131ExpansionModuleID3DigitalInputD": unnamedAlarm2131ExpansionModuleID3DigitalInputD,
       "unnamedAlarm2131ExpansionModuleID3DigitalInputE": unnamedAlarm2131ExpansionModuleID3DigitalInputE,
       "unnamedAlarm2131ExpansionModuleID3DigitalInputF": unnamedAlarm2131ExpansionModuleID3DigitalInputF,
       "unnamedAlarm2131ExpansionModuleID3DigitalInputG": unnamedAlarm2131ExpansionModuleID3DigitalInputG,
       "unnamedAlarm2131ExpansionModuleID3DigitalInputH": unnamedAlarm2131ExpansionModuleID3DigitalInputH,
       "unnamedAlarm2131ExpansionModuleID3DigitalInputI": unnamedAlarm2131ExpansionModuleID3DigitalInputI,
       "unnamedAlarm2131ExpansionModuleID3DigitalInputJ": unnamedAlarm2131ExpansionModuleID3DigitalInputJ,
       "unnamedAlarm2130ExpansionModuleID0AnalogueInputELow": unnamedAlarm2130ExpansionModuleID0AnalogueInputELow,
       "unnamedAlarm2130ExpansionModuleID0AnalogueInputEHi": unnamedAlarm2130ExpansionModuleID0AnalogueInputEHi,
       "unnamedAlarm2130ExpansionModuleID0AnalogueInputFLow": unnamedAlarm2130ExpansionModuleID0AnalogueInputFLow,
       "unnamedAlarm2130ExpansionModuleID0AnalogueInputFHi": unnamedAlarm2130ExpansionModuleID0AnalogueInputFHi,
       "unnamedAlarm2130ExpansionModuleID0AnalogueInputGLow": unnamedAlarm2130ExpansionModuleID0AnalogueInputGLow,
       "unnamedAlarm2130ExpansionModuleID0AnalogueInputGHi": unnamedAlarm2130ExpansionModuleID0AnalogueInputGHi,
       "unnamedAlarm2130ExpansionModuleID0AnalogueInputHLow": unnamedAlarm2130ExpansionModuleID0AnalogueInputHLow,
       "unnamedAlarm2130ExpansionModuleID0AnalogueInputHHi": unnamedAlarm2130ExpansionModuleID0AnalogueInputHHi,
       "unnamedAlarm2130ExpansionModuleID1AnalogueInputELow": unnamedAlarm2130ExpansionModuleID1AnalogueInputELow,
       "unnamedAlarm2130ExpansionModuleID1AnalogueInputEHi": unnamedAlarm2130ExpansionModuleID1AnalogueInputEHi,
       "unnamedAlarm2130ExpansionModuleID1AnalogueInputFLow": unnamedAlarm2130ExpansionModuleID1AnalogueInputFLow,
       "unnamedAlarm2130ExpansionModuleID1AnalogueInputFHi": unnamedAlarm2130ExpansionModuleID1AnalogueInputFHi,
       "unnamedAlarm2130ExpansionModuleID1AnalogueInputGLow": unnamedAlarm2130ExpansionModuleID1AnalogueInputGLow,
       "unnamedAlarm2130ExpansionModuleID1AnalogueInputGHi": unnamedAlarm2130ExpansionModuleID1AnalogueInputGHi,
       "unnamedAlarm2130ExpansionModuleID1AnalogueInputHLow": unnamedAlarm2130ExpansionModuleID1AnalogueInputHLow,
       "unnamedAlarm2130ExpansionModuleID1AnalogueInputHHi": unnamedAlarm2130ExpansionModuleID1AnalogueInputHHi,
       "unnamedAlarm2130ExpansionModuleID2AnalogueInputELow": unnamedAlarm2130ExpansionModuleID2AnalogueInputELow,
       "unnamedAlarm2130ExpansionModuleID2AnalogueInputEHi": unnamedAlarm2130ExpansionModuleID2AnalogueInputEHi,
       "unnamedAlarm2130ExpansionModuleID2AnalogueInputFLow": unnamedAlarm2130ExpansionModuleID2AnalogueInputFLow,
       "unnamedAlarm2130ExpansionModuleID2AnalogueInputFHi": unnamedAlarm2130ExpansionModuleID2AnalogueInputFHi,
       "unnamedAlarm2130ExpansionModuleID2AnalogueInputGLow": unnamedAlarm2130ExpansionModuleID2AnalogueInputGLow,
       "unnamedAlarm2130ExpansionModuleID2AnalogueInputGHi": unnamedAlarm2130ExpansionModuleID2AnalogueInputGHi,
       "unnamedAlarm2130ExpansionModuleID2AnalogueInputHLow": unnamedAlarm2130ExpansionModuleID2AnalogueInputHLow,
       "unnamedAlarm2130ExpansionModuleID2AnalogueInputHHi": unnamedAlarm2130ExpansionModuleID2AnalogueInputHHi,
       "unnamedAlarm2130ExpansionModuleID3AnalogueInputGLow": unnamedAlarm2130ExpansionModuleID3AnalogueInputGLow,
       "unnamedAlarm2130ExpansionModuleID3AnalogueInputGHi": unnamedAlarm2130ExpansionModuleID3AnalogueInputGHi,
       "unnamedAlarm2130ExpansionModuleID3AnalogueInputHLow": unnamedAlarm2130ExpansionModuleID3AnalogueInputHLow,
       "unnamedAlarm2130ExpansionModuleID3AnalogueInputHHi": unnamedAlarm2130ExpansionModuleID3AnalogueInputHHi,
       "unnamedAlarmFlexibleSensorBLow": unnamedAlarmFlexibleSensorBLow,
       "unnamedAlarmFlexibleSensorBHigh": unnamedAlarmFlexibleSensorBHigh,
       "unnamedAlarmFlexibleSensorCLow": unnamedAlarmFlexibleSensorCLow,
       "unnamedAlarmFlexibleSensorCHigh": unnamedAlarmFlexibleSensorCHigh,
       "unnamedAlarmFlexibleSensorDLow": unnamedAlarmFlexibleSensorDLow,
       "unnamedAlarmFlexibleSensorDHigh": unnamedAlarmFlexibleSensorDHigh,
       "unnamedAlarmMaintenanceAlarm1": unnamedAlarmMaintenanceAlarm1,
       "unnamedAlarmMaintenanceAlarm2": unnamedAlarmMaintenanceAlarm2,
       "unnamedAlarmMaintenanceAlarm3": unnamedAlarmMaintenanceAlarm3,
       "unnamedAlarmPLCAlarm1": unnamedAlarmPLCAlarm1,
       "unnamedAlarmPLCAlarm2": unnamedAlarmPLCAlarm2,
       "unnamedAlarmPLCAlarm3": unnamedAlarmPLCAlarm3,
       "unnamedAlarmPLCAlarm4": unnamedAlarmPLCAlarm4,
       "unnamedAlarmPLCAlarm5": unnamedAlarmPLCAlarm5,
       "unnamedAlarmPLCAlarm6": unnamedAlarmPLCAlarm6,
       "unnamedAlarmPLCAlarm7": unnamedAlarmPLCAlarm7,
       "unnamedAlarmPLCAlarm8": unnamedAlarmPLCAlarm8,
       "unnamedAlarmPLCAlarm9": unnamedAlarmPLCAlarm9,
       "unnamedAlarmPLCAlarm10": unnamedAlarmPLCAlarm10,
       "unnamedAlarmPLCAlarm11": unnamedAlarmPLCAlarm11,
       "unnamedAlarmPLCAlarm12": unnamedAlarmPLCAlarm12,
       "unnamedAlarmPLCAlarm13": unnamedAlarmPLCAlarm13,
       "unnamedAlarmPLCAlarm14": unnamedAlarmPLCAlarm14,
       "unnamedAlarmPLCAlarm15": unnamedAlarmPLCAlarm15,
       "unnamedAlarmPLCAlarm16": unnamedAlarmPLCAlarm16,
       "unnamedAlarmPLCAlarm17": unnamedAlarmPLCAlarm17,
       "unnamedAlarmPLCAlarm18": unnamedAlarmPLCAlarm18,
       "unnamedAlarmPLCAlarm19": unnamedAlarmPLCAlarm19,
       "unnamedAlarmPLCAlarm20": unnamedAlarmPLCAlarm20,
       "unnamedAlarmLowLoad": unnamedAlarmLowLoad,
       "unnamedAlarm2131ExpansionModuleID0AnalogueInputALow": unnamedAlarm2131ExpansionModuleID0AnalogueInputALow,
       "unnamedAlarm2131ExpansionModuleID0AnalogueInputAHi": unnamedAlarm2131ExpansionModuleID0AnalogueInputAHi,
       "unnamedAlarm2131ExpansionModuleID0AnalogueInputBLow": unnamedAlarm2131ExpansionModuleID0AnalogueInputBLow,
       "unnamedAlarm2131ExpansionModuleID0AnalogueInputBHi": unnamedAlarm2131ExpansionModuleID0AnalogueInputBHi,
       "unnamedAlarm2131ExpansionModuleID0AnalogueInputCLow": unnamedAlarm2131ExpansionModuleID0AnalogueInputCLow,
       "unnamedAlarm2131ExpansionModuleID0AnalogueInputCHi": unnamedAlarm2131ExpansionModuleID0AnalogueInputCHi,
       "unnamedAlarm2131ExpansionModuleID0AnalogueInputDLow": unnamedAlarm2131ExpansionModuleID0AnalogueInputDLow,
       "unnamedAlarm2131ExpansionModuleID0AnalogueInputDHi": unnamedAlarm2131ExpansionModuleID0AnalogueInputDHi,
       "unnamedAlarm2131ExpansionModuleID0AnalogueInputELow": unnamedAlarm2131ExpansionModuleID0AnalogueInputELow,
       "unnamedAlarm2131ExpansionModuleID0AnalogueInputEHi": unnamedAlarm2131ExpansionModuleID0AnalogueInputEHi,
       "unnamedAlarm2131ExpansionModuleID0AnalogueInputFLow": unnamedAlarm2131ExpansionModuleID0AnalogueInputFLow,
       "unnamedAlarm2131ExpansionModuleID0AnalogueInputFHi": unnamedAlarm2131ExpansionModuleID0AnalogueInputFHi,
       "unnamedAlarm2131ExpansionModuleID0AnalogueInputGLow": unnamedAlarm2131ExpansionModuleID0AnalogueInputGLow,
       "unnamedAlarm2131ExpansionModuleID0AnalogueInputGHi": unnamedAlarm2131ExpansionModuleID0AnalogueInputGHi,
       "unnamedAlarm2131ExpansionModuleID0AnalogueInputHLow": unnamedAlarm2131ExpansionModuleID0AnalogueInputHLow,
       "unnamedAlarm2131ExpansionModuleID0AnalogueInputHHi": unnamedAlarm2131ExpansionModuleID0AnalogueInputHHi,
       "unnamedAlarm2131ExpansionModuleID0AnalogueInputILow": unnamedAlarm2131ExpansionModuleID0AnalogueInputILow,
       "unnamedAlarm2131ExpansionModuleID0AnalogueInputIHi": unnamedAlarm2131ExpansionModuleID0AnalogueInputIHi,
       "unnamedAlarm2131ExpansionModuleID0AnalogueInputJLow": unnamedAlarm2131ExpansionModuleID0AnalogueInputJLow,
       "unnamedAlarm2131ExpansionModuleID0AnalogueInputJHi": unnamedAlarm2131ExpansionModuleID0AnalogueInputJHi,
       "unnamedAlarm2131ExpansionModuleID1AnalogueInputALow": unnamedAlarm2131ExpansionModuleID1AnalogueInputALow,
       "unnamedAlarm2131ExpansionModuleID1AnalogueInputAHi": unnamedAlarm2131ExpansionModuleID1AnalogueInputAHi,
       "unnamedAlarm2131ExpansionModuleID1AnalogueInputBLow": unnamedAlarm2131ExpansionModuleID1AnalogueInputBLow,
       "unnamedAlarm2131ExpansionModuleID1AnalogueInputBHi": unnamedAlarm2131ExpansionModuleID1AnalogueInputBHi,
       "unnamedAlarm2131ExpansionModuleID1AnalogueInputCLow": unnamedAlarm2131ExpansionModuleID1AnalogueInputCLow,
       "unnamedAlarm2131ExpansionModuleID1AnalogueInputCHi": unnamedAlarm2131ExpansionModuleID1AnalogueInputCHi,
       "unnamedAlarm2131ExpansionModuleID1AnalogueInputDLow": unnamedAlarm2131ExpansionModuleID1AnalogueInputDLow,
       "unnamedAlarm2131ExpansionModuleID1AnalogueInputDHi": unnamedAlarm2131ExpansionModuleID1AnalogueInputDHi,
       "unnamedAlarm2131ExpansionModuleID1AnalogueInputELow": unnamedAlarm2131ExpansionModuleID1AnalogueInputELow,
       "unnamedAlarm2131ExpansionModuleID1AnalogueInputEHi": unnamedAlarm2131ExpansionModuleID1AnalogueInputEHi,
       "unnamedAlarm2131ExpansionModuleID1AnalogueInputFLow": unnamedAlarm2131ExpansionModuleID1AnalogueInputFLow,
       "unnamedAlarm2131ExpansionModuleID1AnalogueInputFHi": unnamedAlarm2131ExpansionModuleID1AnalogueInputFHi,
       "unnamedAlarm2131ExpansionModuleID1AnalogueInputGLow": unnamedAlarm2131ExpansionModuleID1AnalogueInputGLow,
       "unnamedAlarm2131ExpansionModuleID1AnalogueInputGHi": unnamedAlarm2131ExpansionModuleID1AnalogueInputGHi,
       "unnamedAlarm2131ExpansionModuleID1AnalogueInputHLow": unnamedAlarm2131ExpansionModuleID1AnalogueInputHLow,
       "unnamedAlarm2131ExpansionModuleID1AnalogueInputHHi": unnamedAlarm2131ExpansionModuleID1AnalogueInputHHi,
       "unnamedAlarm2131ExpansionModuleID1AnalogueInputILow": unnamedAlarm2131ExpansionModuleID1AnalogueInputILow,
       "unnamedAlarm2131ExpansionModuleID1AnalogueInputIHi": unnamedAlarm2131ExpansionModuleID1AnalogueInputIHi,
       "unnamedAlarm2131ExpansionModuleID1AnalogueInputJLow": unnamedAlarm2131ExpansionModuleID1AnalogueInputJLow,
       "unnamedAlarm2131ExpansionModuleID1AnalogueInputJHi": unnamedAlarm2131ExpansionModuleID1AnalogueInputJHi,
       "unnamedAlarm2131ExpansionModuleID2AnalogueInputALow": unnamedAlarm2131ExpansionModuleID2AnalogueInputALow,
       "unnamedAlarm2131ExpansionModuleID2AnalogueInputAHi": unnamedAlarm2131ExpansionModuleID2AnalogueInputAHi,
       "unnamedAlarm2131ExpansionModuleID2AnalogueInputBLow": unnamedAlarm2131ExpansionModuleID2AnalogueInputBLow,
       "unnamedAlarm2131ExpansionModuleID2AnalogueInputBHi": unnamedAlarm2131ExpansionModuleID2AnalogueInputBHi,
       "unnamedAlarm2131ExpansionModuleID2AnalogueInputCLow": unnamedAlarm2131ExpansionModuleID2AnalogueInputCLow,
       "unnamedAlarm2131ExpansionModuleID2AnalogueInputCHi": unnamedAlarm2131ExpansionModuleID2AnalogueInputCHi,
       "unnamedAlarm2131ExpansionModuleID2AnalogueInputDLow": unnamedAlarm2131ExpansionModuleID2AnalogueInputDLow,
       "unnamedAlarm2131ExpansionModuleID2AnalogueInputDHi": unnamedAlarm2131ExpansionModuleID2AnalogueInputDHi,
       "unnamedAlarm2131ExpansionModuleID2AnalogueInputELow": unnamedAlarm2131ExpansionModuleID2AnalogueInputELow,
       "unnamedAlarm2131ExpansionModuleID2AnalogueInputEHi": unnamedAlarm2131ExpansionModuleID2AnalogueInputEHi,
       "unnamedAlarm2131ExpansionModuleID2AnalogueInputFLow": unnamedAlarm2131ExpansionModuleID2AnalogueInputFLow,
       "unnamedAlarm2131ExpansionModuleID2AnalogueInputFHi": unnamedAlarm2131ExpansionModuleID2AnalogueInputFHi,
       "unnamedAlarm2131ExpansionModuleID2AnalogueInputGLow": unnamedAlarm2131ExpansionModuleID2AnalogueInputGLow,
       "unnamedAlarm2131ExpansionModuleID2AnalogueInputGHi": unnamedAlarm2131ExpansionModuleID2AnalogueInputGHi,
       "unnamedAlarm2131ExpansionModuleID2AnalogueInputHLow": unnamedAlarm2131ExpansionModuleID2AnalogueInputHLow,
       "unnamedAlarm2131ExpansionModuleID2AnalogueInputHHi": unnamedAlarm2131ExpansionModuleID2AnalogueInputHHi,
       "unnamedAlarm2131ExpansionModuleID2AnalogueInputILow": unnamedAlarm2131ExpansionModuleID2AnalogueInputILow,
       "unnamedAlarm2131ExpansionModuleID2AnalogueInputIHi": unnamedAlarm2131ExpansionModuleID2AnalogueInputIHi,
       "unnamedAlarm2131ExpansionModuleID2AnalogueInputJLow": unnamedAlarm2131ExpansionModuleID2AnalogueInputJLow,
       "unnamedAlarm2131ExpansionModuleID2AnalogueInputJHi": unnamedAlarm2131ExpansionModuleID2AnalogueInputJHi,
       "unnamedAlarm2131ExpansionModuleID3AnalogueInputALow": unnamedAlarm2131ExpansionModuleID3AnalogueInputALow,
       "unnamedAlarm2131ExpansionModuleID3AnalogueInputAHi": unnamedAlarm2131ExpansionModuleID3AnalogueInputAHi,
       "unnamedAlarm2131ExpansionModuleID3AnalogueInputBLow": unnamedAlarm2131ExpansionModuleID3AnalogueInputBLow,
       "unnamedAlarm2131ExpansionModuleID3AnalogueInputBHi": unnamedAlarm2131ExpansionModuleID3AnalogueInputBHi,
       "unnamedAlarm2131ExpansionModuleID3AnalogueInputCLow": unnamedAlarm2131ExpansionModuleID3AnalogueInputCLow,
       "unnamedAlarm2131ExpansionModuleID3AnalogueInputCHi": unnamedAlarm2131ExpansionModuleID3AnalogueInputCHi,
       "unnamedAlarm2131ExpansionModuleID3AnalogueInputDLow": unnamedAlarm2131ExpansionModuleID3AnalogueInputDLow,
       "unnamedAlarm2131ExpansionModuleID3AnalogueInputDHi": unnamedAlarm2131ExpansionModuleID3AnalogueInputDHi,
       "unnamedAlarm2131ExpansionModuleID3AnalogueInputELow": unnamedAlarm2131ExpansionModuleID3AnalogueInputELow,
       "unnamedAlarm2131ExpansionModuleID3AnalogueInputEHi": unnamedAlarm2131ExpansionModuleID3AnalogueInputEHi,
       "unnamedAlarm2131ExpansionModuleID3AnalogueInputFLow": unnamedAlarm2131ExpansionModuleID3AnalogueInputFLow,
       "unnamedAlarm2131ExpansionModuleID3AnalogueInputFHi": unnamedAlarm2131ExpansionModuleID3AnalogueInputFHi,
       "unnamedAlarm2131ExpansionModuleID3AnalogueInputGLow": unnamedAlarm2131ExpansionModuleID3AnalogueInputGLow,
       "unnamedAlarm2131ExpansionModuleID3AnalogueInputGHi": unnamedAlarm2131ExpansionModuleID3AnalogueInputGHi,
       "unnamedAlarm2131ExpansionModuleID3AnalogueInputHLow": unnamedAlarm2131ExpansionModuleID3AnalogueInputHLow,
       "unnamedAlarm2131ExpansionModuleID3AnalogueInputHHi": unnamedAlarm2131ExpansionModuleID3AnalogueInputHHi,
       "unnamedAlarm2131ExpansionModuleID3AnalogueInputILow": unnamedAlarm2131ExpansionModuleID3AnalogueInputILow,
       "unnamedAlarm2131ExpansionModuleID3AnalogueInputIHi": unnamedAlarm2131ExpansionModuleID3AnalogueInputIHi,
       "unnamedAlarm2131ExpansionModuleID3AnalogueInputJLow": unnamedAlarm2131ExpansionModuleID3AnalogueInputJLow,
       "unnamedAlarm2131ExpansionModuleID3AnalogueInputJHi": unnamedAlarm2131ExpansionModuleID3AnalogueInputJHi,
       "unnamedAlarm2133ExpansionModuleID0AnalogueInputALow": unnamedAlarm2133ExpansionModuleID0AnalogueInputALow,
       "unnamedAlarm2133ExpansionModuleID0AnalogueInputAHi": unnamedAlarm2133ExpansionModuleID0AnalogueInputAHi,
       "unnamedAlarm2133ExpansionModuleID0AnalogueInputBLow": unnamedAlarm2133ExpansionModuleID0AnalogueInputBLow,
       "unnamedAlarm2133ExpansionModuleID0AnalogueInputBHi": unnamedAlarm2133ExpansionModuleID0AnalogueInputBHi,
       "unnamedAlarm2133ExpansionModuleID0AnalogueInputCLow": unnamedAlarm2133ExpansionModuleID0AnalogueInputCLow,
       "unnamedAlarm2133ExpansionModuleID0AnalogueInputCHi": unnamedAlarm2133ExpansionModuleID0AnalogueInputCHi,
       "unnamedAlarm2133ExpansionModuleID0AnalogueInputDLow": unnamedAlarm2133ExpansionModuleID0AnalogueInputDLow,
       "unnamedAlarm2133ExpansionModuleID0AnalogueInputDHi": unnamedAlarm2133ExpansionModuleID0AnalogueInputDHi,
       "unnamedAlarm2133ExpansionModuleID0AnalogueInputELow": unnamedAlarm2133ExpansionModuleID0AnalogueInputELow,
       "unnamedAlarm2133ExpansionModuleID0AnalogueInputEHi": unnamedAlarm2133ExpansionModuleID0AnalogueInputEHi,
       "unnamedAlarm2133ExpansionModuleID0AnalogueInputFLow": unnamedAlarm2133ExpansionModuleID0AnalogueInputFLow,
       "unnamedAlarm2133ExpansionModuleID0AnalogueInputFHi": unnamedAlarm2133ExpansionModuleID0AnalogueInputFHi,
       "unnamedAlarm2133ExpansionModuleID0AnalogueInputGLow": unnamedAlarm2133ExpansionModuleID0AnalogueInputGLow,
       "unnamedAlarm2133ExpansionModuleID0AnalogueInputGHi": unnamedAlarm2133ExpansionModuleID0AnalogueInputGHi,
       "unnamedAlarm2133ExpansionModuleID0AnalogueInputHLow": unnamedAlarm2133ExpansionModuleID0AnalogueInputHLow,
       "unnamedAlarm2133ExpansionModuleID0AnalogueInputHHi": unnamedAlarm2133ExpansionModuleID0AnalogueInputHHi,
       "unnamedAlarm2133ExpansionModuleID1AnalogueInputALow": unnamedAlarm2133ExpansionModuleID1AnalogueInputALow,
       "unnamedAlarm2133ExpansionModuleID1AnalogueInputAHi": unnamedAlarm2133ExpansionModuleID1AnalogueInputAHi,
       "unnamedAlarm2133ExpansionModuleID1AnalogueInputBLow": unnamedAlarm2133ExpansionModuleID1AnalogueInputBLow,
       "unnamedAlarm2133ExpansionModuleID1AnalogueInputBHi": unnamedAlarm2133ExpansionModuleID1AnalogueInputBHi,
       "unnamedAlarm2133ExpansionModuleID1AnalogueInputCLow": unnamedAlarm2133ExpansionModuleID1AnalogueInputCLow,
       "unnamedAlarm2133ExpansionModuleID1AnalogueInputCHi": unnamedAlarm2133ExpansionModuleID1AnalogueInputCHi,
       "unnamedAlarm2133ExpansionModuleID1AnalogueInputDLow": unnamedAlarm2133ExpansionModuleID1AnalogueInputDLow,
       "unnamedAlarm2133ExpansionModuleID1AnalogueInputDHi": unnamedAlarm2133ExpansionModuleID1AnalogueInputDHi,
       "unnamedAlarm2133ExpansionModuleID1AnalogueInputELow": unnamedAlarm2133ExpansionModuleID1AnalogueInputELow,
       "unnamedAlarm2133ExpansionModuleID1AnalogueInputEHi": unnamedAlarm2133ExpansionModuleID1AnalogueInputEHi,
       "unnamedAlarm2133ExpansionModuleID1AnalogueInputFLow": unnamedAlarm2133ExpansionModuleID1AnalogueInputFLow,
       "unnamedAlarm2133ExpansionModuleID1AnalogueInputFHi": unnamedAlarm2133ExpansionModuleID1AnalogueInputFHi,
       "unnamedAlarm2133ExpansionModuleID1AnalogueInputGLow": unnamedAlarm2133ExpansionModuleID1AnalogueInputGLow,
       "unnamedAlarm2133ExpansionModuleID1AnalogueInputGHi": unnamedAlarm2133ExpansionModuleID1AnalogueInputGHi,
       "unnamedAlarm2133ExpansionModuleID1AnalogueInputHLow": unnamedAlarm2133ExpansionModuleID1AnalogueInputHLow,
       "unnamedAlarm2133ExpansionModuleID1AnalogueInputHHi": unnamedAlarm2133ExpansionModuleID1AnalogueInputHHi,
       "unnamedAlarm2133ExpansionModuleID2AnalogueInputALow": unnamedAlarm2133ExpansionModuleID2AnalogueInputALow,
       "unnamedAlarm2133ExpansionModuleID2AnalogueInputAHi": unnamedAlarm2133ExpansionModuleID2AnalogueInputAHi,
       "unnamedAlarm2133ExpansionModuleID2AnalogueInputBLow": unnamedAlarm2133ExpansionModuleID2AnalogueInputBLow,
       "unnamedAlarm2133ExpansionModuleID2AnalogueInputBHi": unnamedAlarm2133ExpansionModuleID2AnalogueInputBHi,
       "unnamedAlarm2133ExpansionModuleID2AnalogueInputCLow": unnamedAlarm2133ExpansionModuleID2AnalogueInputCLow,
       "unnamedAlarm2133ExpansionModuleID2AnalogueInputCHi": unnamedAlarm2133ExpansionModuleID2AnalogueInputCHi,
       "unnamedAlarm2133ExpansionModuleID2AnalogueInputDLow": unnamedAlarm2133ExpansionModuleID2AnalogueInputDLow,
       "unnamedAlarm2133ExpansionModuleID2AnalogueInputDHi": unnamedAlarm2133ExpansionModuleID2AnalogueInputDHi,
       "unnamedAlarm2133ExpansionModuleID2AnalogueInputELow": unnamedAlarm2133ExpansionModuleID2AnalogueInputELow,
       "unnamedAlarm2133ExpansionModuleID2AnalogueInputEHi": unnamedAlarm2133ExpansionModuleID2AnalogueInputEHi,
       "unnamedAlarm2133ExpansionModuleID2AnalogueInputFLow": unnamedAlarm2133ExpansionModuleID2AnalogueInputFLow,
       "unnamedAlarm2133ExpansionModuleID2AnalogueInputFHi": unnamedAlarm2133ExpansionModuleID2AnalogueInputFHi,
       "unnamedAlarm2133ExpansionModuleID2AnalogueInputGLow": unnamedAlarm2133ExpansionModuleID2AnalogueInputGLow,
       "unnamedAlarm2133ExpansionModuleID2AnalogueInputGHi": unnamedAlarm2133ExpansionModuleID2AnalogueInputGHi,
       "unnamedAlarm2133ExpansionModuleID2AnalogueInputHLow": unnamedAlarm2133ExpansionModuleID2AnalogueInputHLow,
       "unnamedAlarm2133ExpansionModuleID2AnalogueInputHHi": unnamedAlarm2133ExpansionModuleID2AnalogueInputHHi,
       "unnamedAlarm2133ExpansionModuleID3AnalogueInputALow": unnamedAlarm2133ExpansionModuleID3AnalogueInputALow,
       "unnamedAlarm2133ExpansionModuleID3AnalogueInputAHi": unnamedAlarm2133ExpansionModuleID3AnalogueInputAHi,
       "unnamedAlarm2133ExpansionModuleID3AnalogueInputBLow": unnamedAlarm2133ExpansionModuleID3AnalogueInputBLow,
       "unnamedAlarm2133ExpansionModuleID3AnalogueInputBHi": unnamedAlarm2133ExpansionModuleID3AnalogueInputBHi,
       "unnamedAlarm2133ExpansionModuleID3AnalogueInputCLow": unnamedAlarm2133ExpansionModuleID3AnalogueInputCLow,
       "unnamedAlarm2133ExpansionModuleID3AnalogueInputCHi": unnamedAlarm2133ExpansionModuleID3AnalogueInputCHi,
       "unnamedAlarm2133ExpansionModuleID3AnalogueInputDLow": unnamedAlarm2133ExpansionModuleID3AnalogueInputDLow,
       "unnamedAlarm2133ExpansionModuleID3AnalogueInputDHi": unnamedAlarm2133ExpansionModuleID3AnalogueInputDHi,
       "unnamedAlarm2133ExpansionModuleID3AnalogueInputELow": unnamedAlarm2133ExpansionModuleID3AnalogueInputELow,
       "unnamedAlarm2133ExpansionModuleID3AnalogueInputEHi": unnamedAlarm2133ExpansionModuleID3AnalogueInputEHi,
       "unnamedAlarm2133ExpansionModuleID3AnalogueInputFLow": unnamedAlarm2133ExpansionModuleID3AnalogueInputFLow,
       "unnamedAlarm2133ExpansionModuleID3AnalogueInputFHi": unnamedAlarm2133ExpansionModuleID3AnalogueInputFHi,
       "unnamedAlarm2133ExpansionModuleID3AnalogueInputGLow": unnamedAlarm2133ExpansionModuleID3AnalogueInputGLow,
       "unnamedAlarm2133ExpansionModuleID3AnalogueInputGHi": unnamedAlarm2133ExpansionModuleID3AnalogueInputGHi,
       "unnamedAlarm2133ExpansionModuleID3AnalogueInputHLow": unnamedAlarm2133ExpansionModuleID3AnalogueInputHLow,
       "unnamedAlarm2133ExpansionModuleID3AnalogueInputHHi": unnamedAlarm2133ExpansionModuleID3AnalogueInputHHi,
       "unnamedAlarm2130ExpansionModuleID3AnalogueInputELow": unnamedAlarm2130ExpansionModuleID3AnalogueInputELow,
       "unnamedAlarm2130ExpansionModuleID3AnalogueInputEHi": unnamedAlarm2130ExpansionModuleID3AnalogueInputEHi,
       "unnamedAlarm2130ExpansionModuleID3AnalogueInputFLow": unnamedAlarm2130ExpansionModuleID3AnalogueInputFLow,
       "unnamedAlarm2130ExpansionModuleID3AnalogueInputFHi": unnamedAlarm2130ExpansionModuleID3AnalogueInputFHi,
       "unnamedAlarmAnalogueInputADigital": unnamedAlarmAnalogueInputADigital,
       "unnamedAlarmFlexibleSensorALow": unnamedAlarmFlexibleSensorALow,
       "unnamedAlarmFlexibleSensorAHigh": unnamedAlarmFlexibleSensorAHigh,
       "unnamedAlarmChargerID0CommonShutdown": unnamedAlarmChargerID0CommonShutdown,
       "unnamedAlarmChargerID0CommonWarning": unnamedAlarmChargerID0CommonWarning,
       "unnamedAlarmChargerID1CommonShutdown": unnamedAlarmChargerID1CommonShutdown,
       "unnamedAlarmChargerID1CommonWarning": unnamedAlarmChargerID1CommonWarning,
       "unnamedAlarmChargerID2CommonShutdown": unnamedAlarmChargerID2CommonShutdown,
       "unnamedAlarmChargerID2CommonWarning": unnamedAlarmChargerID2CommonWarning,
       "unnamedAlarmChargerID3CommonShutdown": unnamedAlarmChargerID3CommonShutdown,
       "unnamedAlarmChargerID3CommonWarning": unnamedAlarmChargerID3CommonWarning,
       "notifModuleRestart": notifModuleRestart,
       "notifEngineStops": notifEngineStops,
       "notifMainsFail": notifMainsFail,
       "notifMainsReturn": notifMainsReturn,
       "notifEngineStarts": notifEngineStarts,
       "notifModeChange": notifModeChange,
       "notifECUlampProtect": notifECUlampProtect,
       "notifECUlampMalfunction": notifECUlampMalfunction,
       "notifECUlampShutdown": notifECUlampShutdown,
       "notifECUlampWarning": notifECUlampWarning,
       "notifLevelStatusMonitoring": notifLevelStatusMonitoring,
       "dse8610": dse8610,
       "dseInstrumentsSection": dseInstrumentsSection,
       "generatorTable": generatorTable,
       "generatorEntry": generatorEntry,
       "genKeyID": genKeyID,
       "genFreq": genFreq,
       "genL1Volts": genL1Volts,
       "genL2Volts": genL2Volts,
       "genL3Volts": genL3Volts,
       "genL1L2Volts": genL1L2Volts,
       "genL2L3Volts": genL2L3Volts,
       "genL3L1Volts": genL3L1Volts,
       "genL1Current": genL1Current,
       "genL2Current": genL2Current,
       "genL3Current": genL3Current,
       "genECurrent": genECurrent,
       "genL1Watts": genL1Watts,
       "genL2Watts": genL2Watts,
       "genL3Watts": genL3Watts,
       "genRotation": genRotation,
       "genWattsTotal": genWattsTotal,
       "genL1VA": genL1VA,
       "genL2VA": genL2VA,
       "genL3VA": genL3VA,
       "genTotalVA": genTotalVA,
       "genL1VAr": genL1VAr,
       "genL2VAr": genL2VAr,
       "genL3VAr": genL3VAr,
       "genTotalVAr": genTotalVAr,
       "genPowerFactorL1": genPowerFactorL1,
       "genPowerFactorL2": genPowerFactorL2,
       "genPowerFactorL3": genPowerFactorL3,
       "genAvgPowerFactor": genAvgPowerFactor,
       "genPowerTotalPC": genPowerTotalPC,
       "genVARTotalPC": genVARTotalPC,
       "genPhase1": genPhase1,
       "genPhase2": genPhase2,
       "genPhase3": genPhase3,
       "genPhaseTotal": genPhaseTotal,
       "genPowerL1PC": genPowerL1PC,
       "genPowerL2PC": genPowerL2PC,
       "genPowerL3PC": genPowerL3PC,
       "genVoltageLNAvg": genVoltageLNAvg,
       "genVoltageLNDiff": genVoltageLNDiff,
       "genVoltageLNMin": genVoltageLNMin,
       "genVoltageLNMax": genVoltageLNMax,
       "genVoltageLLAvg": genVoltageLLAvg,
       "genVoltageLLDiff": genVoltageLLDiff,
       "genVoltageLLMin": genVoltageLLMin,
       "genVoltageLLMax": genVoltageLLMax,
       "genCurrentAve": genCurrentAve,
       "genCurrentDif": genCurrentDif,
       "genCurrentMin": genCurrentMin,
       "genCurrentMax": genCurrentMax,
       "genPowerTotalAvgPC": genPowerTotalAvgPC,
       "genPowerTotalDiffPC": genPowerTotalDiffPC,
       "genPowerTotalMinPC": genPowerTotalMinPC,
       "genPowerTotalMaxPC": genPowerTotalMaxPC,
       "genVATotalAvgPC": genVATotalAvgPC,
       "genVADiffPC": genVADiffPC,
       "genVAMinPC": genVAMinPC,
       "genVAMaxPC": genVAMaxPC,
       "genVARTotalAvgPC": genVARTotalAvgPC,
       "genVARDiffPC": genVARDiffPC,
       "genVARMinPC": genVARMinPC,
       "genVARMaxPC": genVARMaxPC,
       "genPFTotalAvgPC": genPFTotalAvgPC,
       "genPFDiffPC": genPFDiffPC,
       "genPFMinPC": genPFMinPC,
       "genPFMaxPC": genPFMaxPC,
       "engineTable": engineTable,
       "engineEntry": engineEntry,
       "engKeyID": engKeyID,
       "engOilPress": engOilPress,
       "engTemp": engTemp,
       "engOilTemp": engOilTemp,
       "engFuelLevel": engFuelLevel,
       "engChargeAltVolts": engChargeAltVolts,
       "engBatteryVolts": engBatteryVolts,
       "engSpeedDisplay": engSpeedDisplay,
       "engCoolantP1": engCoolantP1,
       "engCoolantP2": engCoolantP2,
       "engFuelP1": engFuelP1,
       "engFuelP2": engFuelP2,
       "engTurboP1": engTurboP1,
       "engTurboP2": engTurboP2,
       "engInMainfoldT1": engInMainfoldT1,
       "engInMainfoldT2": engInMainfoldT2,
       "engExhaustT1": engExhaustT1,
       "engExhaustT2": engExhaustT2,
       "engFuelConsumption": engFuelConsumption,
       "engWaterInFuel": engWaterInFuel,
       "engCANBitData": engCANBitData,
       "engAtmosphericP": engAtmosphericP,
       "engFuelT": engFuelT,
       "engFuelLevelUnits": engFuelLevelUnits,
       "engTankFuelUnits": engTankFuelUnits,
       "engAfttrt1FuelUSed": engAfttrt1FuelUSed,
       "engAfttrt1ExGasT1": engAfttrt1ExGasT1,
       "engAfttrt1ExGasT3": engAfttrt1ExGasT3,
       "engRefTorque": engRefTorque,
       "engPerTorque": engPerTorque,
       "engDemandPerTorque": engDemandPerTorque,
       "engPCLoadAtSpeed": engPCLoadAtSpeed,
       "engAccelPedalPos": engAccelPedalPos,
       "engNomFricPerTorque": engNomFricPerTorque,
       "engOilLevel": engOilLevel,
       "engCrankCasePress": engCrankCasePress,
       "engCoolantLevel": engCoolantLevel,
       "engInjectorRail1": engInjectorRail1,
       "engInjectorRail2": engInjectorRail2,
       "engEgrFlowRate": engEgrFlowRate,
       "engPreFilOilPress": engPreFilOilPress,
       "engInstBreakPower": engInstBreakPower,
       "engExhGasPort1Temp": engExhGasPort1Temp,
       "engExhGasPort2Temp": engExhGasPort2Temp,
       "engExhGasPort3Temp": engExhGasPort3Temp,
       "engExhGasPort4Temp": engExhGasPort4Temp,
       "engExhGasPort5Temp": engExhGasPort5Temp,
       "engExhGasPort6Temp": engExhGasPort6Temp,
       "engExhGasPort7Temp": engExhGasPort7Temp,
       "engExhGasPort8Temp": engExhGasPort8Temp,
       "engExhGasPort9Temp": engExhGasPort9Temp,
       "engExhGasPort10Temp": engExhGasPort10Temp,
       "engExhGasPort11Temp": engExhGasPort11Temp,
       "engExhGasPort12Temp": engExhGasPort12Temp,
       "engExhGasPort13Temp": engExhGasPort13Temp,
       "engExhGasPort14Temp": engExhGasPort14Temp,
       "engExhGasPort15Temp": engExhGasPort15Temp,
       "engExhGasPort16Temp": engExhGasPort16Temp,
       "engIntercoolerTemp": engIntercoolerTemp,
       "engTurboOilTemp": engTurboOilTemp,
       "engECUTemp": engECUTemp,
       "engFanSpeed": engFanSpeed,
       "engTotalRev": engTotalRev,
       "engAirInPress": engAirInPress,
       "engAirFilDiffPres": engAirFilDiffPres,
       "engTrapInPress": engTrapInPress,
       "engTurboP3": engTurboP3,
       "engTurboP4": engTurboP4,
       "engInMainfoldT3": engInMainfoldT3,
       "engInMainfoldT4": engInMainfoldT4,
       "engInMainfoldT5": engInMainfoldT5,
       "engInMainfoldT6": engInMainfoldT6,
       "engTripFuel": engTripFuel,
       "engElectPotential": engElectPotential,
       "engPGIEngType": engPGIEngType,
       "engPGIVerNum": engPGIVerNum,
       "engDPTCFilLampCmd": engDPTCFilLampCmd,
       "engExhSysHighTemp": engExhSysHighTemp,
       "engDPTCActRegFor": engDPTCActRegFor,
       "engSDWNWaitStart": engSDWNWaitStart,
       "engSDWNProtection": engSDWNProtection,
       "engSDWNApproaching": engSDWNApproaching,
       "engOperatingState": engOperatingState,
       "engSDWNClOverride": engSDWNClOverride,
       "engBattleshortOvr": engBattleshortOvr,
       "engModHours": engModHours,
       "engModOilPress": engModOilPress,
       "engModCoolTemp": engModCoolTemp,
       "engModRPM": engModRPM,
       "engModChargeAlt": engModChargeAlt,
       "engModSpeedFeed": engModSpeedFeed,
       "engModFreqAdj": engModFreqAdj,
       "engAlarmWarn": engAlarmWarn,
       "engAlarmShdwn": engAlarmShdwn,
       "engAlarmElectr": engAlarmElectr,
       "engAmberStopLamp": engAmberStopLamp,
       "engAmberLampFlash": engAmberLampFlash,
       "engRedStopLamp": engRedStopLamp,
       "engRedLampFlash": engRedLampFlash,
       "engProtLamp": engProtLamp,
       "engProtLampFlash": engProtLampFlash,
       "engMalfLamp": engMalfLamp,
       "engMalfLampFlash": engMalfLampFlash,
       "engBattSwitched": engBattSwitched,
       "engChargPotential": engChargPotential,
       "engCharAltCurr": engCharAltCurr,
       "engBattCurr": engBattCurr,
       "engTorqueMode": engTorqueMode,
       "engStarterMode": engStarterMode,
       "engCIStatus": engCIStatus,
       "engDemandedSpeed": engDemandedSpeed,
       "engSpeedFBUp": engSpeedFBUp,
       "engSpeedFBDown": engSpeedFBDown,
       "engSpeedFailMode": engSpeedFailMode,
       "engCurrSDSrc": engCurrSDSrc,
       "engFbackSDCAN": engFbackSDCAN,
       "engFbackSDAnalog": engFbackSDAnalog,
       "engFailureCodes": engFailureCodes,
       "engActDrop": engActDrop,
       "engStartStatus": engStartStatus,
       "engProtOrStatus": engProtOrStatus,
       "engMTURuniingState": engMTURuniingState,
       "engCylCutOff": engCylCutOff,
       "engLoadGenStatus": engLoadGenStatus,
       "engEtxStopState": engEtxStopState,
       "engCurrOPMode": engCurrOPMode,
       "engMTUReqTorque": engMTUReqTorque,
       "engTripAvgFuel": engTripAvgFuel,
       "engECURatedPower": engECURatedPower,
       "engECURatedSpeed": engECURatedSpeed,
       "engECUIdleSpeed": engECUIdleSpeed,
       "engECUDesirSpeed": engECUDesirSpeed,
       "engECUPreheatStat": engECUPreheatStat,
       "engManiFoldPres": engManiFoldPres,
       "engIntercoolerLevel": engIntercoolerLevel,
       "engCANLinkState": engCANLinkState,
       "engAutoDFPRegInh": engAutoDFPRegInh,
       "engDPTCActRegInhSwitch": engDPTCActRegInhSwitch,
       "engSootLoadPC": engSootLoadPC,
       "engAshLoadPC": engAshLoadPC,
       "engDefTankLevel": engDefTankLevel,
       "engDefTankTemp": engDefTankTemp,
       "engDefLevelWarn": engDefLevelWarn,
       "engDefReagentCons": engDefReagentCons,
       "engDefInducReason": engDefInducReason,
       "engDefInducSever": engDefInducSever,
       "engDefCounterMin": engDefCounterMin,
       "engTLTTorqueReduc": engTLTTorqueReduc,
       "engTLTVehspdReduc": engTLTVehspdReduc,
       "engEGRPress": engEGRPress,
       "engEGRTemp": engEGRTemp,
       "engAmbAirTemp": engAmbAirTemp,
       "engAirIntakeTemp": engAirIntakeTemp,
       "engSRCOperatInduc": engSRCOperatInduc,
       "engTankLevLowLost": engTankLevLowLost,
       "engMiscAltSpeedSel": engMiscAltSpeedSel,
       "engExhGasP17Temp": engExhGasP17Temp,
       "engExhGasP18Temp": engExhGasP18Temp,
       "engExhGasP19Temp": engExhGasP19Temp,
       "engExhGasP20Temp": engExhGasP20Temp,
       "engInstFuelRate": engInstFuelRate,
       "engDPTCFiltStat": engDPTCFiltStat,
       "engDPTCActRegInh": engDPTCActRegInh,
       "engDPTCActRegInhEt": engDPTCActRegInhEt,
       "engDefTankStat": engDefTankStat,
       "engFuelGasPress": engFuelGasPress,
       "engThrotPos1": engThrotPos1,
       "engThrotPos2": engThrotPos2,
       "gencommSection": gencommSection,
       "gencommP166Table": gencommP166Table,
       "gencommP166Entry": gencommP166Entry,
       "gencommP166KeyID": gencommP166KeyID,
       "gencommP166Reg-0-1": gencommP166Reg_0_1,
       "gencommP166Reg-2-3": gencommP166Reg_2_3,
       "gencommP166Reg-4-5": gencommP166Reg_4_5,
       "gencommP166Reg-6-7": gencommP166Reg_6_7,
       "gencommP166Reg-8-9": gencommP166Reg_8_9,
       "gencommP166Reg-10-11": gencommP166Reg_10_11,
       "gencommP166Reg-12-13": gencommP166Reg_12_13,
       "gencommP166Reg-14-15": gencommP166Reg_14_15,
       "gencommP166Reg-16-17": gencommP166Reg_16_17,
       "gencommP166Reg-18-19": gencommP166Reg_18_19,
       "gencommP166Reg-20-21": gencommP166Reg_20_21,
       "gencommP166Reg-22-23": gencommP166Reg_22_23,
       "gencommP166Reg-24-25": gencommP166Reg_24_25,
       "gencommP166Reg-26-27": gencommP166Reg_26_27,
       "gencommP166Reg-28-29": gencommP166Reg_28_29,
       "gencommP166Reg-30-31": gencommP166Reg_30_31,
       "gencommP166Reg-32-33": gencommP166Reg_32_33,
       "gencommP166Reg-34-35": gencommP166Reg_34_35,
       "gencommP166Reg-36-37": gencommP166Reg_36_37,
       "gencommP166Reg-38-39": gencommP166Reg_38_39,
       "gencommP166Reg-40-41": gencommP166Reg_40_41,
       "gencommP166Reg-42-43": gencommP166Reg_42_43,
       "gencommP166Reg-44-45": gencommP166Reg_44_45,
       "gencommP166Reg-46-47": gencommP166Reg_46_47,
       "gencommP166Reg-48-49": gencommP166Reg_48_49,
       "gencommP166Reg-50-51": gencommP166Reg_50_51,
       "gencommP166Reg-52-53": gencommP166Reg_52_53,
       "gencommP166Reg-54-55": gencommP166Reg_54_55,
       "gencommP166Reg-56-57": gencommP166Reg_56_57,
       "gencommP166Reg-58-59": gencommP166Reg_58_59,
       "gencommP166Reg-60-61": gencommP166Reg_60_61,
       "gencommP166Reg-62-63": gencommP166Reg_62_63,
       "gencommP166Reg-64-65": gencommP166Reg_64_65,
       "gencommP166Reg-66-67": gencommP166Reg_66_67,
       "gencommP166Reg-68-69": gencommP166Reg_68_69,
       "gencommP166Reg-70-71": gencommP166Reg_70_71,
       "gencommP166Reg-72-73": gencommP166Reg_72_73,
       "gencommP166Reg-74-75": gencommP166Reg_74_75,
       "gencommP166Reg-76-77": gencommP166Reg_76_77,
       "gencommP166Reg-78-79": gencommP166Reg_78_79,
       "gencommP166Reg-80-81": gencommP166Reg_80_81,
       "gencommP166Reg-82-83": gencommP166Reg_82_83,
       "gencommP166Reg-84-85": gencommP166Reg_84_85,
       "gencommP166Reg-86-87": gencommP166Reg_86_87,
       "gencommP166Reg-88-89": gencommP166Reg_88_89,
       "gencommP166Reg-90-91": gencommP166Reg_90_91,
       "gencommP166Reg-92-93": gencommP166Reg_92_93,
       "gencommP166Reg-94-95": gencommP166Reg_94_95,
       "gencommP166Reg-96-97": gencommP166Reg_96_97,
       "gencommP166Reg-98-99": gencommP166Reg_98_99,
       "gencommP166Reg-100-101": gencommP166Reg_100_101,
       "gencommP166Reg-102-103": gencommP166Reg_102_103,
       "gencommP166Reg-104-105": gencommP166Reg_104_105,
       "gencommP166Reg-106-107": gencommP166Reg_106_107,
       "gencommP166Reg-108-109": gencommP166Reg_108_109,
       "gencommP166Reg-110-111": gencommP166Reg_110_111,
       "gencommP166Reg-112-113": gencommP166Reg_112_113,
       "gencommP166Reg-114-115": gencommP166Reg_114_115,
       "gencommP166Reg-116-117": gencommP166Reg_116_117,
       "gencommP166Reg-118-119": gencommP166Reg_118_119,
       "gencommP166Reg-120-121": gencommP166Reg_120_121,
       "gencommP166Reg-122-123": gencommP166Reg_122_123,
       "gencommP166Reg-124-125": gencommP166Reg_124_125,
       "gencommP166Reg-126-127": gencommP166Reg_126_127,
       "gencommP166Reg-128-129": gencommP166Reg_128_129,
       "gencommP166Reg-130-131": gencommP166Reg_130_131,
       "gencommP166Reg-132-133": gencommP166Reg_132_133,
       "gencommP166Reg-134-135": gencommP166Reg_134_135,
       "gencommP166Reg-136-137": gencommP166Reg_136_137,
       "gencommP166Reg-138-139": gencommP166Reg_138_139,
       "gencommP166Reg-140-141": gencommP166Reg_140_141,
       "gencommP166Reg-142-143": gencommP166Reg_142_143,
       "gencommP166Reg-144-145": gencommP166Reg_144_145,
       "gencommP166Reg-146-147": gencommP166Reg_146_147,
       "gencommP166Reg-148-149": gencommP166Reg_148_149,
       "gencommP166Reg-150-151": gencommP166Reg_150_151,
       "gencommP166Reg-152-153": gencommP166Reg_152_153,
       "gencommP166Reg-154-155": gencommP166Reg_154_155,
       "gencommP166Reg-156-157": gencommP166Reg_156_157,
       "gencommP166Reg-158-159": gencommP166Reg_158_159,
       "gencommP166Reg-160-161": gencommP166Reg_160_161,
       "gencommP166Reg-162-163": gencommP166Reg_162_163,
       "gencommP166Reg-164-165": gencommP166Reg_164_165,
       "gencommP166Reg-166-167": gencommP166Reg_166_167,
       "gencommP166Reg-168-169": gencommP166Reg_168_169,
       "gencommP166Reg-170-171": gencommP166Reg_170_171,
       "gencommP166Reg-172-173": gencommP166Reg_172_173,
       "gencommP166Reg-174-175": gencommP166Reg_174_175,
       "gencommP166Reg-176-177": gencommP166Reg_176_177,
       "gencommP166Reg-178-179": gencommP166Reg_178_179,
       "gencommP166Reg-180-181": gencommP166Reg_180_181,
       "gencommP166Reg-182-183": gencommP166Reg_182_183,
       "gencommP166Reg-184-185": gencommP166Reg_184_185,
       "gencommP166Reg-186-187": gencommP166Reg_186_187,
       "gencommP166Reg-188-189": gencommP166Reg_188_189,
       "gencommP166Reg-190-191": gencommP166Reg_190_191,
       "gencommP166Reg-192-193": gencommP166Reg_192_193,
       "gencommP166Reg-194-195": gencommP166Reg_194_195,
       "gencommP166Reg-196-197": gencommP166Reg_196_197,
       "gencommP166Reg-198-199": gencommP166Reg_198_199,
       "gencommP166Reg-200-201": gencommP166Reg_200_201,
       "gencommP166Reg-202-203": gencommP166Reg_202_203,
       "gencommP166Reg-204-205": gencommP166Reg_204_205,
       "gencommP166Reg-206-207": gencommP166Reg_206_207,
       "gencommP166Reg-208-209": gencommP166Reg_208_209,
       "gencommP166Reg-210-211": gencommP166Reg_210_211,
       "gencommP166Reg-212-213": gencommP166Reg_212_213,
       "gencommP166Reg-214-215": gencommP166Reg_214_215,
       "gencommP166Reg-216-217": gencommP166Reg_216_217,
       "gencommP166Reg-218-219": gencommP166Reg_218_219,
       "gencommP166Reg-220-221": gencommP166Reg_220_221,
       "gencommP166Reg-222-223": gencommP166Reg_222_223,
       "gencommP166Reg-224-225": gencommP166Reg_224_225,
       "gencommP166Reg-226-227": gencommP166Reg_226_227,
       "gencommP166Reg-228-229": gencommP166Reg_228_229,
       "gencommP166Reg-230-231": gencommP166Reg_230_231,
       "gencommP166Reg-232-233": gencommP166Reg_232_233,
       "gencommP166Reg-234-235": gencommP166Reg_234_235,
       "gencommP166Reg-236-237": gencommP166Reg_236_237,
       "gencommP166Reg-238-239": gencommP166Reg_238_239,
       "gencommP166Reg-240-241": gencommP166Reg_240_241,
       "gencommP166Reg-242-243": gencommP166Reg_242_243,
       "gencommP166Reg-244-245": gencommP166Reg_244_245,
       "gencommP166Reg-246-247": gencommP166Reg_246_247,
       "gencommP166Reg-248-249": gencommP166Reg_248_249,
       "gencommP166Reg-250-251": gencommP166Reg_250_251,
       "gencommP166Reg-252-253": gencommP166Reg_252_253,
       "gencommP166Reg-254-255": gencommP166Reg_254_255,
       "gencommP167Table": gencommP167Table,
       "gencommP167Entry": gencommP167Entry,
       "gencommP167KeyID": gencommP167KeyID,
       "gencommP167Reg-0-1": gencommP167Reg_0_1,
       "gencommP167Reg-2-3": gencommP167Reg_2_3,
       "gencommP167Reg-4-5": gencommP167Reg_4_5,
       "gencommP167Reg-6-7": gencommP167Reg_6_7,
       "gencommP167Reg-8-9": gencommP167Reg_8_9,
       "gencommP167Reg-10-11": gencommP167Reg_10_11,
       "gencommP167Reg-12-13": gencommP167Reg_12_13,
       "gencommP167Reg-14-15": gencommP167Reg_14_15,
       "gencommP167Reg-16-17": gencommP167Reg_16_17,
       "gencommP167Reg-18-19": gencommP167Reg_18_19,
       "gencommP167Reg-20-21": gencommP167Reg_20_21,
       "gencommP167Reg-22-23": gencommP167Reg_22_23,
       "gencommP167Reg-24-25": gencommP167Reg_24_25,
       "gencommP167Reg-26-27": gencommP167Reg_26_27,
       "gencommP167Reg-28-29": gencommP167Reg_28_29,
       "gencommP167Reg-30-31": gencommP167Reg_30_31,
       "gencommP167Reg-32-33": gencommP167Reg_32_33,
       "gencommP167Reg-34-35": gencommP167Reg_34_35,
       "gencommP167Reg-36-37": gencommP167Reg_36_37,
       "gencommP167Reg-38-39": gencommP167Reg_38_39,
       "gencommP167Reg-40-41": gencommP167Reg_40_41,
       "gencommP167Reg-42-43": gencommP167Reg_42_43,
       "gencommP167Reg-44-45": gencommP167Reg_44_45,
       "gencommP167Reg-46-47": gencommP167Reg_46_47,
       "gencommP167Reg-48-49": gencommP167Reg_48_49,
       "gencommP167Reg-50-51": gencommP167Reg_50_51,
       "gencommP167Reg-52-53": gencommP167Reg_52_53,
       "gencommP167Reg-54-55": gencommP167Reg_54_55,
       "gencommP167Reg-56-57": gencommP167Reg_56_57,
       "gencommP167Reg-58-59": gencommP167Reg_58_59,
       "gencommP167Reg-60-61": gencommP167Reg_60_61,
       "gencommP167Reg-62-63": gencommP167Reg_62_63,
       "gencommP167Reg-64-65": gencommP167Reg_64_65,
       "gencommP167Reg-66-67": gencommP167Reg_66_67,
       "gencommP167Reg-68-69": gencommP167Reg_68_69,
       "gencommP167Reg-70-71": gencommP167Reg_70_71,
       "gencommP167Reg-72-73": gencommP167Reg_72_73,
       "gencommP167Reg-74-75": gencommP167Reg_74_75,
       "gencommP167Reg-76-77": gencommP167Reg_76_77,
       "gencommP167Reg-78-79": gencommP167Reg_78_79,
       "gencommP167Reg-80-81": gencommP167Reg_80_81,
       "gencommP167Reg-82-83": gencommP167Reg_82_83,
       "gencommP167Reg-84-85": gencommP167Reg_84_85,
       "gencommP167Reg-86-87": gencommP167Reg_86_87,
       "gencommP167Reg-88-89": gencommP167Reg_88_89,
       "gencommP167Reg-90-91": gencommP167Reg_90_91,
       "gencommP167Reg-92-93": gencommP167Reg_92_93,
       "gencommP167Reg-94-95": gencommP167Reg_94_95,
       "gencommP167Reg-96-97": gencommP167Reg_96_97,
       "gencommP167Reg-98-99": gencommP167Reg_98_99,
       "gencommP167Reg-100-101": gencommP167Reg_100_101,
       "gencommP167Reg-102-103": gencommP167Reg_102_103,
       "gencommP167Reg-104-105": gencommP167Reg_104_105,
       "gencommP167Reg-106-107": gencommP167Reg_106_107,
       "gencommP167Reg-108-109": gencommP167Reg_108_109,
       "gencommP167Reg-110-111": gencommP167Reg_110_111,
       "gencommP167Reg-112-113": gencommP167Reg_112_113,
       "gencommP167Reg-114-115": gencommP167Reg_114_115,
       "gencommP167Reg-116-117": gencommP167Reg_116_117,
       "gencommP167Reg-118-119": gencommP167Reg_118_119,
       "gencommP167Reg-120-121": gencommP167Reg_120_121,
       "gencommP167Reg-122-123": gencommP167Reg_122_123,
       "gencommP167Reg-124-125": gencommP167Reg_124_125,
       "gencommP167Reg-126-127": gencommP167Reg_126_127,
       "gencommP167Reg-128-129": gencommP167Reg_128_129,
       "gencommP167Reg-130-131": gencommP167Reg_130_131,
       "gencommP167Reg-132-133": gencommP167Reg_132_133,
       "gencommP167Reg-134-135": gencommP167Reg_134_135,
       "gencommP167Reg-136-137": gencommP167Reg_136_137,
       "gencommP167Reg-138-139": gencommP167Reg_138_139,
       "gencommP167Reg-140-141": gencommP167Reg_140_141,
       "gencommP167Reg-142-143": gencommP167Reg_142_143,
       "gencommP167Reg-144-145": gencommP167Reg_144_145,
       "gencommP167Reg-146-147": gencommP167Reg_146_147,
       "gencommP167Reg-148-149": gencommP167Reg_148_149,
       "gencommP167Reg-150-151": gencommP167Reg_150_151,
       "gencommP167Reg-152-153": gencommP167Reg_152_153,
       "gencommP167Reg-154-155": gencommP167Reg_154_155,
       "gencommP167Reg-156-157": gencommP167Reg_156_157,
       "gencommP167Reg-158-159": gencommP167Reg_158_159,
       "gencommP167Reg-160-161": gencommP167Reg_160_161,
       "gencommP167Reg-162-163": gencommP167Reg_162_163,
       "gencommP167Reg-164-165": gencommP167Reg_164_165,
       "gencommP167Reg-166-167": gencommP167Reg_166_167,
       "gencommP167Reg-168-169": gencommP167Reg_168_169,
       "gencommP167Reg-170-171": gencommP167Reg_170_171,
       "gencommP167Reg-172-173": gencommP167Reg_172_173,
       "gencommP167Reg-174-175": gencommP167Reg_174_175,
       "gencommP167Reg-176-177": gencommP167Reg_176_177,
       "gencommP167Reg-178-179": gencommP167Reg_178_179,
       "gencommP167Reg-180-181": gencommP167Reg_180_181,
       "gencommP167Reg-182-183": gencommP167Reg_182_183,
       "gencommP167Reg-184-185": gencommP167Reg_184_185,
       "gencommP167Reg-186-187": gencommP167Reg_186_187,
       "gencommP167Reg-188-189": gencommP167Reg_188_189,
       "gencommP167Reg-190-191": gencommP167Reg_190_191,
       "gencommP167Reg-192-193": gencommP167Reg_192_193,
       "gencommP167Reg-194-195": gencommP167Reg_194_195,
       "gencommP167Reg-196-197": gencommP167Reg_196_197,
       "gencommP167Reg-198-199": gencommP167Reg_198_199,
       "gencommP167Reg-200-201": gencommP167Reg_200_201,
       "gencommP167Reg-202-203": gencommP167Reg_202_203,
       "gencommP167Reg-204-205": gencommP167Reg_204_205,
       "gencommP167Reg-206-207": gencommP167Reg_206_207,
       "gencommP167Reg-208-209": gencommP167Reg_208_209,
       "gencommP167Reg-210-211": gencommP167Reg_210_211,
       "gencommP167Reg-212-213": gencommP167Reg_212_213,
       "gencommP167Reg-214-215": gencommP167Reg_214_215,
       "gencommP167Reg-216-217": gencommP167Reg_216_217,
       "gencommP167Reg-218-219": gencommP167Reg_218_219,
       "gencommP167Reg-220-221": gencommP167Reg_220_221,
       "gencommP167Reg-222-223": gencommP167Reg_222_223,
       "gencommP167Reg-224-225": gencommP167Reg_224_225,
       "gencommP167Reg-226-227": gencommP167Reg_226_227,
       "gencommP167Reg-228-229": gencommP167Reg_228_229,
       "gencommP167Reg-230-231": gencommP167Reg_230_231,
       "gencommP167Reg-232-233": gencommP167Reg_232_233,
       "gencommP167Reg-234-235": gencommP167Reg_234_235,
       "gencommP167Reg-236-237": gencommP167Reg_236_237,
       "gencommP167Reg-238-239": gencommP167Reg_238_239,
       "gencommP167Reg-240-241": gencommP167Reg_240_241,
       "gencommP167Reg-242-243": gencommP167Reg_242_243,
       "gencommP167Reg-244-245": gencommP167Reg_244_245,
       "gencommP167Reg-246-247": gencommP167Reg_246_247,
       "gencommP167Reg-248-249": gencommP167Reg_248_249,
       "gencommP167Reg-250-251": gencommP167Reg_250_251,
       "gencommP167Reg-252-253": gencommP167Reg_252_253,
       "gencommP167Reg-254-255": gencommP167Reg_254_255,
       "gencommP168Table": gencommP168Table,
       "gencommP168Entry": gencommP168Entry,
       "gencommP168KeyID": gencommP168KeyID,
       "gencommP168Reg-0-1": gencommP168Reg_0_1,
       "gencommP168Reg-2-3": gencommP168Reg_2_3,
       "gencommP168Reg-4-5": gencommP168Reg_4_5,
       "gencommP168Reg-6-7": gencommP168Reg_6_7,
       "gencommP168Reg-8-9": gencommP168Reg_8_9,
       "gencommP168Reg-10-11": gencommP168Reg_10_11,
       "gencommP168Reg-12-13": gencommP168Reg_12_13,
       "gencommP168Reg-14-15": gencommP168Reg_14_15,
       "gencommP168Reg-16-17": gencommP168Reg_16_17,
       "gencommP168Reg-18-19": gencommP168Reg_18_19,
       "gencommP168Reg-20-21": gencommP168Reg_20_21,
       "gencommP168Reg-22-23": gencommP168Reg_22_23,
       "gencommP168Reg-24-25": gencommP168Reg_24_25,
       "gencommP168Reg-26-27": gencommP168Reg_26_27,
       "gencommP168Reg-28-29": gencommP168Reg_28_29,
       "gencommP168Reg-30-31": gencommP168Reg_30_31,
       "gencommP168Reg-32-33": gencommP168Reg_32_33,
       "gencommP168Reg-34-35": gencommP168Reg_34_35,
       "gencommP168Reg-36-37": gencommP168Reg_36_37,
       "gencommP168Reg-38-39": gencommP168Reg_38_39,
       "gencommP168Reg-40-41": gencommP168Reg_40_41,
       "gencommP168Reg-42-43": gencommP168Reg_42_43,
       "gencommP168Reg-44-45": gencommP168Reg_44_45,
       "gencommP168Reg-46-47": gencommP168Reg_46_47,
       "gencommP168Reg-48-49": gencommP168Reg_48_49,
       "gencommP168Reg-50-51": gencommP168Reg_50_51,
       "gencommP168Reg-52-53": gencommP168Reg_52_53,
       "gencommP168Reg-54-55": gencommP168Reg_54_55,
       "gencommP168Reg-56-57": gencommP168Reg_56_57,
       "gencommP168Reg-58-59": gencommP168Reg_58_59,
       "gencommP168Reg-60-61": gencommP168Reg_60_61,
       "gencommP168Reg-62-63": gencommP168Reg_62_63,
       "gencommP168Reg-64-65": gencommP168Reg_64_65,
       "gencommP168Reg-66-67": gencommP168Reg_66_67,
       "gencommP168Reg-68-69": gencommP168Reg_68_69,
       "gencommP168Reg-70-71": gencommP168Reg_70_71,
       "gencommP168Reg-72-73": gencommP168Reg_72_73,
       "gencommP168Reg-74-75": gencommP168Reg_74_75,
       "gencommP168Reg-76-77": gencommP168Reg_76_77,
       "gencommP168Reg-78-79": gencommP168Reg_78_79,
       "gencommP168Reg-80-81": gencommP168Reg_80_81,
       "gencommP168Reg-82-83": gencommP168Reg_82_83,
       "gencommP168Reg-84-85": gencommP168Reg_84_85,
       "gencommP168Reg-86-87": gencommP168Reg_86_87,
       "gencommP168Reg-88-89": gencommP168Reg_88_89,
       "gencommP168Reg-90-91": gencommP168Reg_90_91,
       "gencommP168Reg-92-93": gencommP168Reg_92_93,
       "gencommP168Reg-94-95": gencommP168Reg_94_95,
       "gencommP168Reg-96-97": gencommP168Reg_96_97,
       "gencommP168Reg-98-99": gencommP168Reg_98_99,
       "gencommP168Reg-100-101": gencommP168Reg_100_101,
       "gencommP168Reg-102-103": gencommP168Reg_102_103,
       "gencommP168Reg-104-105": gencommP168Reg_104_105,
       "gencommP168Reg-106-107": gencommP168Reg_106_107,
       "gencommP168Reg-108-109": gencommP168Reg_108_109,
       "gencommP168Reg-110-111": gencommP168Reg_110_111,
       "gencommP168Reg-112-113": gencommP168Reg_112_113,
       "gencommP168Reg-114-115": gencommP168Reg_114_115,
       "gencommP168Reg-116-117": gencommP168Reg_116_117,
       "gencommP168Reg-118-119": gencommP168Reg_118_119,
       "gencommP168Reg-120-121": gencommP168Reg_120_121,
       "gencommP168Reg-122-123": gencommP168Reg_122_123,
       "gencommP168Reg-124-125": gencommP168Reg_124_125,
       "gencommP168Reg-126-127": gencommP168Reg_126_127,
       "gencommP168Reg-128-129": gencommP168Reg_128_129,
       "gencommP168Reg-130-131": gencommP168Reg_130_131,
       "gencommP168Reg-132-133": gencommP168Reg_132_133,
       "gencommP168Reg-134-135": gencommP168Reg_134_135,
       "gencommP168Reg-136-137": gencommP168Reg_136_137,
       "gencommP168Reg-138-139": gencommP168Reg_138_139,
       "gencommP168Reg-140-141": gencommP168Reg_140_141,
       "gencommP168Reg-142-143": gencommP168Reg_142_143,
       "gencommP168Reg-144-145": gencommP168Reg_144_145,
       "gencommP168Reg-146-147": gencommP168Reg_146_147,
       "gencommP168Reg-148-149": gencommP168Reg_148_149,
       "gencommP168Reg-150-151": gencommP168Reg_150_151,
       "gencommP168Reg-152-153": gencommP168Reg_152_153,
       "gencommP168Reg-154-155": gencommP168Reg_154_155,
       "gencommP168Reg-156-157": gencommP168Reg_156_157,
       "gencommP168Reg-158-159": gencommP168Reg_158_159,
       "gencommP168Reg-160-161": gencommP168Reg_160_161,
       "gencommP168Reg-162-163": gencommP168Reg_162_163,
       "gencommP168Reg-164-165": gencommP168Reg_164_165,
       "gencommP168Reg-166-167": gencommP168Reg_166_167,
       "gencommP168Reg-168-169": gencommP168Reg_168_169,
       "gencommP168Reg-170-171": gencommP168Reg_170_171,
       "gencommP168Reg-172-173": gencommP168Reg_172_173,
       "gencommP168Reg-174-175": gencommP168Reg_174_175,
       "gencommP168Reg-176-177": gencommP168Reg_176_177,
       "gencommP168Reg-178-179": gencommP168Reg_178_179,
       "gencommP168Reg-180-181": gencommP168Reg_180_181,
       "gencommP168Reg-182-183": gencommP168Reg_182_183,
       "gencommP168Reg-184-185": gencommP168Reg_184_185,
       "gencommP168Reg-186-187": gencommP168Reg_186_187,
       "gencommP168Reg-188-189": gencommP168Reg_188_189,
       "gencommP168Reg-190-191": gencommP168Reg_190_191,
       "gencommP168Reg-192-193": gencommP168Reg_192_193,
       "gencommP168Reg-194-195": gencommP168Reg_194_195,
       "gencommP168Reg-196-197": gencommP168Reg_196_197,
       "gencommP168Reg-198-199": gencommP168Reg_198_199,
       "gencommP168Reg-200-201": gencommP168Reg_200_201,
       "gencommP168Reg-202-203": gencommP168Reg_202_203,
       "gencommP168Reg-204-205": gencommP168Reg_204_205,
       "gencommP168Reg-206-207": gencommP168Reg_206_207,
       "gencommP168Reg-208-209": gencommP168Reg_208_209,
       "gencommP168Reg-210-211": gencommP168Reg_210_211,
       "gencommP168Reg-212-213": gencommP168Reg_212_213,
       "gencommP168Reg-214-215": gencommP168Reg_214_215,
       "gencommP168Reg-216-217": gencommP168Reg_216_217,
       "gencommP168Reg-218-219": gencommP168Reg_218_219,
       "gencommP168Reg-220-221": gencommP168Reg_220_221,
       "gencommP168Reg-222-223": gencommP168Reg_222_223,
       "gencommP168Reg-224-225": gencommP168Reg_224_225,
       "gencommP168Reg-226-227": gencommP168Reg_226_227,
       "gencommP168Reg-228-229": gencommP168Reg_228_229,
       "gencommP168Reg-230-231": gencommP168Reg_230_231,
       "gencommP168Reg-232-233": gencommP168Reg_232_233,
       "gencommP168Reg-234-235": gencommP168Reg_234_235,
       "gencommP168Reg-236-237": gencommP168Reg_236_237,
       "gencommP168Reg-238-239": gencommP168Reg_238_239,
       "gencommP168Reg-240-241": gencommP168Reg_240_241,
       "gencommP168Reg-242-243": gencommP168Reg_242_243,
       "gencommP168Reg-244-245": gencommP168Reg_244_245,
       "gencommP168Reg-246-247": gencommP168Reg_246_247,
       "gencommP168Reg-248-249": gencommP168Reg_248_249,
       "gencommP168Reg-250-251": gencommP168Reg_250_251,
       "gencommP168Reg-252-253": gencommP168Reg_252_253,
       "gencommP168Reg-254-255": gencommP168Reg_254_255,
       "gencommP169Table": gencommP169Table,
       "gencommP169Entry": gencommP169Entry,
       "gencommP169KeyID": gencommP169KeyID,
       "gencommP169Reg-0-1": gencommP169Reg_0_1,
       "gencommP169Reg-2-3": gencommP169Reg_2_3,
       "gencommP169Reg-4-5": gencommP169Reg_4_5,
       "gencommP169Reg-6-7": gencommP169Reg_6_7,
       "gencommP169Reg-8-9": gencommP169Reg_8_9,
       "gencommP169Reg-10-11": gencommP169Reg_10_11,
       "gencommP169Reg-12-13": gencommP169Reg_12_13,
       "gencommP169Reg-14-15": gencommP169Reg_14_15,
       "gencommP169Reg-16-17": gencommP169Reg_16_17,
       "gencommP169Reg-18-19": gencommP169Reg_18_19,
       "gencommP169Reg-20-21": gencommP169Reg_20_21,
       "gencommP169Reg-22-23": gencommP169Reg_22_23,
       "gencommP169Reg-24-25": gencommP169Reg_24_25,
       "gencommP169Reg-26-27": gencommP169Reg_26_27,
       "gencommP169Reg-28-29": gencommP169Reg_28_29,
       "gencommP169Reg-30-31": gencommP169Reg_30_31,
       "gencommP169Reg-32-33": gencommP169Reg_32_33,
       "gencommP169Reg-34-35": gencommP169Reg_34_35,
       "gencommP169Reg-36-37": gencommP169Reg_36_37,
       "gencommP169Reg-38-39": gencommP169Reg_38_39,
       "gencommP169Reg-40-41": gencommP169Reg_40_41,
       "gencommP169Reg-42-43": gencommP169Reg_42_43,
       "gencommP169Reg-44-45": gencommP169Reg_44_45,
       "gencommP169Reg-46-47": gencommP169Reg_46_47,
       "gencommP169Reg-48-49": gencommP169Reg_48_49,
       "gencommP169Reg-50-51": gencommP169Reg_50_51,
       "gencommP169Reg-52-53": gencommP169Reg_52_53,
       "gencommP169Reg-54-55": gencommP169Reg_54_55,
       "gencommP169Reg-56-57": gencommP169Reg_56_57,
       "gencommP169Reg-58-59": gencommP169Reg_58_59,
       "gencommP169Reg-60-61": gencommP169Reg_60_61,
       "gencommP169Reg-62-63": gencommP169Reg_62_63,
       "gencommP169Reg-64-65": gencommP169Reg_64_65,
       "gencommP169Reg-66-67": gencommP169Reg_66_67,
       "gencommP169Reg-68-69": gencommP169Reg_68_69,
       "gencommP169Reg-70-71": gencommP169Reg_70_71,
       "gencommP169Reg-72-73": gencommP169Reg_72_73,
       "gencommP169Reg-74-75": gencommP169Reg_74_75,
       "gencommP169Reg-76-77": gencommP169Reg_76_77,
       "gencommP169Reg-78-79": gencommP169Reg_78_79,
       "gencommP169Reg-80-81": gencommP169Reg_80_81,
       "gencommP169Reg-82-83": gencommP169Reg_82_83,
       "gencommP169Reg-84-85": gencommP169Reg_84_85,
       "gencommP169Reg-86-87": gencommP169Reg_86_87,
       "gencommP169Reg-88-89": gencommP169Reg_88_89,
       "gencommP169Reg-90-91": gencommP169Reg_90_91,
       "gencommP169Reg-92-93": gencommP169Reg_92_93,
       "gencommP169Reg-94-95": gencommP169Reg_94_95,
       "gencommP169Reg-96-97": gencommP169Reg_96_97,
       "gencommP169Reg-98-99": gencommP169Reg_98_99,
       "gencommP169Reg-100-101": gencommP169Reg_100_101,
       "gencommP169Reg-102-103": gencommP169Reg_102_103,
       "gencommP169Reg-104-105": gencommP169Reg_104_105,
       "gencommP169Reg-106-107": gencommP169Reg_106_107,
       "gencommP169Reg-108-109": gencommP169Reg_108_109,
       "gencommP169Reg-110-111": gencommP169Reg_110_111,
       "gencommP169Reg-112-113": gencommP169Reg_112_113,
       "gencommP169Reg-114-115": gencommP169Reg_114_115,
       "gencommP169Reg-116-117": gencommP169Reg_116_117,
       "gencommP169Reg-118-119": gencommP169Reg_118_119,
       "gencommP169Reg-120-121": gencommP169Reg_120_121,
       "gencommP169Reg-122-123": gencommP169Reg_122_123,
       "gencommP169Reg-124-125": gencommP169Reg_124_125,
       "gencommP169Reg-126-127": gencommP169Reg_126_127,
       "gencommP169Reg-128-129": gencommP169Reg_128_129,
       "gencommP169Reg-130-131": gencommP169Reg_130_131,
       "gencommP169Reg-132-133": gencommP169Reg_132_133,
       "gencommP169Reg-134-135": gencommP169Reg_134_135,
       "gencommP169Reg-136-137": gencommP169Reg_136_137,
       "gencommP169Reg-138-139": gencommP169Reg_138_139,
       "gencommP169Reg-140-141": gencommP169Reg_140_141,
       "gencommP169Reg-142-143": gencommP169Reg_142_143,
       "gencommP169Reg-144-145": gencommP169Reg_144_145,
       "gencommP169Reg-146-147": gencommP169Reg_146_147,
       "gencommP169Reg-148-149": gencommP169Reg_148_149,
       "gencommP169Reg-150-151": gencommP169Reg_150_151,
       "gencommP169Reg-152-153": gencommP169Reg_152_153,
       "gencommP169Reg-154-155": gencommP169Reg_154_155,
       "gencommP169Reg-156-157": gencommP169Reg_156_157,
       "gencommP169Reg-158-159": gencommP169Reg_158_159,
       "gencommP169Reg-160-161": gencommP169Reg_160_161,
       "gencommP169Reg-162-163": gencommP169Reg_162_163,
       "gencommP169Reg-164-165": gencommP169Reg_164_165,
       "gencommP169Reg-166-167": gencommP169Reg_166_167,
       "gencommP169Reg-168-169": gencommP169Reg_168_169,
       "gencommP169Reg-170-171": gencommP169Reg_170_171,
       "gencommP169Reg-172-173": gencommP169Reg_172_173,
       "gencommP169Reg-174-175": gencommP169Reg_174_175,
       "gencommP169Reg-176-177": gencommP169Reg_176_177,
       "gencommP169Reg-178-179": gencommP169Reg_178_179,
       "gencommP169Reg-180-181": gencommP169Reg_180_181,
       "gencommP169Reg-182-183": gencommP169Reg_182_183,
       "gencommP169Reg-184-185": gencommP169Reg_184_185,
       "gencommP169Reg-186-187": gencommP169Reg_186_187,
       "gencommP169Reg-188-189": gencommP169Reg_188_189,
       "gencommP169Reg-190-191": gencommP169Reg_190_191,
       "gencommP169Reg-192-193": gencommP169Reg_192_193,
       "gencommP169Reg-194-195": gencommP169Reg_194_195,
       "gencommP169Reg-196-197": gencommP169Reg_196_197,
       "gencommP169Reg-198-199": gencommP169Reg_198_199,
       "gencommP169Reg-200-201": gencommP169Reg_200_201,
       "gencommP169Reg-202-203": gencommP169Reg_202_203,
       "gencommP169Reg-204-205": gencommP169Reg_204_205,
       "gencommP169Reg-206-207": gencommP169Reg_206_207,
       "gencommP169Reg-208-209": gencommP169Reg_208_209,
       "gencommP169Reg-210-211": gencommP169Reg_210_211,
       "gencommP169Reg-212-213": gencommP169Reg_212_213,
       "gencommP169Reg-214-215": gencommP169Reg_214_215,
       "gencommP169Reg-216-217": gencommP169Reg_216_217,
       "gencommP169Reg-218-219": gencommP169Reg_218_219,
       "gencommP169Reg-220-221": gencommP169Reg_220_221,
       "gencommP169Reg-222-223": gencommP169Reg_222_223,
       "gencommP169Reg-224-225": gencommP169Reg_224_225,
       "gencommP169Reg-226-227": gencommP169Reg_226_227,
       "gencommP169Reg-228-229": gencommP169Reg_228_229,
       "gencommP169Reg-230-231": gencommP169Reg_230_231,
       "gencommP169Reg-232-233": gencommP169Reg_232_233,
       "gencommP169Reg-234-235": gencommP169Reg_234_235,
       "gencommP169Reg-236-237": gencommP169Reg_236_237,
       "gencommP169Reg-238-239": gencommP169Reg_238_239,
       "gencommP169Reg-240-241": gencommP169Reg_240_241,
       "gencommP169Reg-242-243": gencommP169Reg_242_243,
       "gencommP169Reg-244-245": gencommP169Reg_244_245,
       "gencommP169Reg-246-247": gencommP169Reg_246_247,
       "gencommP169Reg-248-249": gencommP169Reg_248_249,
       "gencommP169Reg-250-251": gencommP169Reg_250_251,
       "gencommP169Reg-252-253": gencommP169Reg_252_253,
       "gencommP169Reg-254-255": gencommP169Reg_254_255,
       "busTable": busTable,
       "busTableEntry": busTableEntry,
       "busKeyId": busKeyId,
       "busFreq": busFreq,
       "busL1Volts": busL1Volts,
       "busL2Volts": busL2Volts,
       "busL3Volts": busL3Volts,
       "busL1L2Volts": busL1L2Volts,
       "busL2L3Volts": busL2L3Volts,
       "busL3L1Volts": busL3L1Volts,
       "busL1Current": busL1Current,
       "busL2Current": busL2Current,
       "busL3Current": busL3Current,
       "busECurrent": busECurrent,
       "busL1Watts": busL1Watts,
       "busL2Watts": busL2Watts,
       "busL3Watts": busL3Watts,
       "busRotations": busRotations,
       "busWattsTotal": busWattsTotal,
       "busL1VA": busL1VA,
       "busL2VA": busL2VA,
       "busL3VA": busL3VA,
       "busTotalVA": busTotalVA,
       "busL1VAr": busL1VAr,
       "busL2VAr": busL2VAr,
       "busL3VAr": busL3VAr,
       "busTotalVAr": busTotalVAr,
       "busPowerFactorL1": busPowerFactorL1,
       "busPowerFactorL2": busPowerFactorL2,
       "busPowerFactorL3": busPowerFactorL3,
       "busAvgPowerFactor": busAvgPowerFactor,
       "busPowerTotalPC": busPowerTotalPC,
       "busVARTotalPC": busVARTotalPC,
       "busVoltageLNAvg": busVoltageLNAvg,
       "busVoltageLNDiff": busVoltageLNDiff,
       "busVoltageLNMin": busVoltageLNMin,
       "busVoltageLNMax": busVoltageLNMax,
       "busVoltageLLAvg": busVoltageLLAvg,
       "busVoltageLLDiff": busVoltageLLDiff,
       "busVoltageLLMin": busVoltageLLMin,
       "busVoltageLLMax": busVoltageLLMax,
       "dse8610Control": dse8610Control,
       "dseKeypressTable": dseKeypressTable,
       "dseKeypressEntry": dseKeypressEntry,
       "keypressKeyID": keypressKeyID,
       "keypress": keypress,
       "snmpMIBConformance": snmpMIBConformance,
       "snmpMIBCompliances": snmpMIBCompliances,
       "snmpBasicCompliance": snmpBasicCompliance,
       "snmpMIBGroups": snmpMIBGroups,
       "generatorGroup": generatorGroup,
       "engineGroup": engineGroup,
       "busGroup": busGroup,
       "gencommP166Group": gencommP166Group,
       "gencommP167Group": gencommP167Group,
       "gencommP168Group": gencommP168Group,
       "gencommP169Group": gencommP169Group,
       "keypressGroup": keypressGroup,
       "trapVarsGroup": trapVarsGroup,
       "snmpBasicNotificationsGroup": snmpBasicNotificationsGroup,
       "dse8610AlarmsMngr": dse8610AlarmsMngr,
       "dse8610AlarmStateTable": dse8610AlarmStateTable,
       "dse8610AlarmStateEntry": dse8610AlarmStateEntry,
       "dse8610AlarmKeyID": dse8610AlarmKeyID,
       "dse8610SeqNr": dse8610SeqNr,
       "dse8610TrapID": dse8610TrapID,
       "dse8610TrapState": dse8610TrapState,
       "dse8610TrapTimeStamp": dse8610TrapTimeStamp}
)
