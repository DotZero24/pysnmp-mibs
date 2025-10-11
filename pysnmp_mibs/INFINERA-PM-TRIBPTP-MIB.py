# SNMP MIB module (INFINERA-PM-TRIBPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-TRIBPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:56 2025
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

(commonPerfMon,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "commonPerfMon")

(FloatHundredths,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths")

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

tribPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3)
)
if mibBuilder.loadTexts:
    tribPtpPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TribPtpPmRealTable_Object = MibTable
tribPtpPmRealTable = _TribPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 1)
)
if mibBuilder.loadTexts:
    tribPtpPmRealTable.setStatus("current")
_TribPtpPmRealEntry_Object = MibTableRow
tribPtpPmRealEntry = _TribPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 1, 1)
)
tribPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tribPtpPmRealEntry.setStatus("current")
_TribPtpPmRealTomTxLBC_Type = FloatHundredths
_TribPtpPmRealTomTxLBC_Object = MibTableColumn
tribPtpPmRealTomTxLBC = _TribPtpPmRealTomTxLBC_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 1, 1, 1),
    _TribPtpPmRealTomTxLBC_Type()
)
tribPtpPmRealTomTxLBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmRealTomTxLBC.setStatus("current")
_TribPtpPmRealTomOpt_Type = FloatHundredths
_TribPtpPmRealTomOpt_Object = MibTableColumn
tribPtpPmRealTomOpt = _TribPtpPmRealTomOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 1, 1, 2),
    _TribPtpPmRealTomOpt_Type()
)
tribPtpPmRealTomOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmRealTomOpt.setStatus("current")
_TribPtpPmRealTomOpr_Type = FloatHundredths
_TribPtpPmRealTomOpr_Object = MibTableColumn
tribPtpPmRealTomOpr = _TribPtpPmRealTomOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 1, 1, 3),
    _TribPtpPmRealTomOpr_Type()
)
tribPtpPmRealTomOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmRealTomOpr.setStatus("current")
_TribPtpPmRealTomTxLBC02_Type = FloatHundredths
_TribPtpPmRealTomTxLBC02_Object = MibTableColumn
tribPtpPmRealTomTxLBC02 = _TribPtpPmRealTomTxLBC02_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 1, 1, 4),
    _TribPtpPmRealTomTxLBC02_Type()
)
tribPtpPmRealTomTxLBC02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmRealTomTxLBC02.setStatus("current")
_TribPtpPmRealTomOpt02_Type = FloatHundredths
_TribPtpPmRealTomOpt02_Object = MibTableColumn
tribPtpPmRealTomOpt02 = _TribPtpPmRealTomOpt02_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 1, 1, 5),
    _TribPtpPmRealTomOpt02_Type()
)
tribPtpPmRealTomOpt02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmRealTomOpt02.setStatus("current")
_TribPtpPmRealTomOpr02_Type = FloatHundredths
_TribPtpPmRealTomOpr02_Object = MibTableColumn
tribPtpPmRealTomOpr02 = _TribPtpPmRealTomOpr02_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 1, 1, 6),
    _TribPtpPmRealTomOpr02_Type()
)
tribPtpPmRealTomOpr02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmRealTomOpr02.setStatus("current")
_TribPtpPmRealTomTxLBC03_Type = FloatHundredths
_TribPtpPmRealTomTxLBC03_Object = MibTableColumn
tribPtpPmRealTomTxLBC03 = _TribPtpPmRealTomTxLBC03_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 1, 1, 7),
    _TribPtpPmRealTomTxLBC03_Type()
)
tribPtpPmRealTomTxLBC03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmRealTomTxLBC03.setStatus("current")
_TribPtpPmRealTomOpt03_Type = FloatHundredths
_TribPtpPmRealTomOpt03_Object = MibTableColumn
tribPtpPmRealTomOpt03 = _TribPtpPmRealTomOpt03_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 1, 1, 8),
    _TribPtpPmRealTomOpt03_Type()
)
tribPtpPmRealTomOpt03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmRealTomOpt03.setStatus("current")
_TribPtpPmRealTomOpr03_Type = FloatHundredths
_TribPtpPmRealTomOpr03_Object = MibTableColumn
tribPtpPmRealTomOpr03 = _TribPtpPmRealTomOpr03_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 1, 1, 9),
    _TribPtpPmRealTomOpr03_Type()
)
tribPtpPmRealTomOpr03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmRealTomOpr03.setStatus("current")
_TribPtpPmRealTomTxLBC04_Type = FloatHundredths
_TribPtpPmRealTomTxLBC04_Object = MibTableColumn
tribPtpPmRealTomTxLBC04 = _TribPtpPmRealTomTxLBC04_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 1, 1, 10),
    _TribPtpPmRealTomTxLBC04_Type()
)
tribPtpPmRealTomTxLBC04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmRealTomTxLBC04.setStatus("current")
_TribPtpPmRealTomOpt04_Type = FloatHundredths
_TribPtpPmRealTomOpt04_Object = MibTableColumn
tribPtpPmRealTomOpt04 = _TribPtpPmRealTomOpt04_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 1, 1, 11),
    _TribPtpPmRealTomOpt04_Type()
)
tribPtpPmRealTomOpt04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmRealTomOpt04.setStatus("current")
_TribPtpPmRealTomOpr04_Type = FloatHundredths
_TribPtpPmRealTomOpr04_Object = MibTableColumn
tribPtpPmRealTomOpr04 = _TribPtpPmRealTomOpr04_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 1, 1, 12),
    _TribPtpPmRealTomOpr04_Type()
)
tribPtpPmRealTomOpr04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmRealTomOpr04.setStatus("current")
_TribPtpPmRealTomOptTotal_Type = FloatHundredths
_TribPtpPmRealTomOptTotal_Object = MibTableColumn
tribPtpPmRealTomOptTotal = _TribPtpPmRealTomOptTotal_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 1, 1, 13),
    _TribPtpPmRealTomOptTotal_Type()
)
tribPtpPmRealTomOptTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmRealTomOptTotal.setStatus("current")
_TribPtpPmRealTomOprTotal_Type = FloatHundredths
_TribPtpPmRealTomOprTotal_Object = MibTableColumn
tribPtpPmRealTomOprTotal = _TribPtpPmRealTomOprTotal_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 1, 1, 14),
    _TribPtpPmRealTomOprTotal_Type()
)
tribPtpPmRealTomOprTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmRealTomOprTotal.setStatus("current")
_TribPtpPmTable_Object = MibTable
tribPtpPmTable = _TribPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2)
)
if mibBuilder.loadTexts:
    tribPtpPmTable.setStatus("current")
_TribPtpPmEntry_Object = MibTableRow
tribPtpPmEntry = _TribPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1)
)
tribPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-TRIBPTP-MIB", "tribPtpPmSampleDuration"),
    (0, "INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    tribPtpPmEntry.setStatus("current")


class _TribPtpPmTimestamp_Type(Integer32):
    """Custom type tribPtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TribPtpPmTimestamp_Type.__name__ = "Integer32"
_TribPtpPmTimestamp_Object = MibTableColumn
tribPtpPmTimestamp = _TribPtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 1),
    _TribPtpPmTimestamp_Type()
)
tribPtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tribPtpPmTimestamp.setStatus("current")


class _TribPtpPmSampleDuration_Type(Integer32):
    """Custom type tribPtpPmSampleDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 1),
          ("day", 2))
    )


_TribPtpPmSampleDuration_Type.__name__ = "Integer32"
_TribPtpPmSampleDuration_Object = MibTableColumn
tribPtpPmSampleDuration = _TribPtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 2),
    _TribPtpPmSampleDuration_Type()
)
tribPtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tribPtpPmSampleDuration.setStatus("current")
_TribPtpPmValidity_Type = TruthValue
_TribPtpPmValidity_Object = MibTableColumn
tribPtpPmValidity = _TribPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 3),
    _TribPtpPmValidity_Type()
)
tribPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmValidity.setStatus("current")
_TribPtpPmTomTxLBCMin_Type = FloatHundredths
_TribPtpPmTomTxLBCMin_Object = MibTableColumn
tribPtpPmTomTxLBCMin = _TribPtpPmTomTxLBCMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 4),
    _TribPtpPmTomTxLBCMin_Type()
)
tribPtpPmTomTxLBCMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomTxLBCMin.setStatus("current")
_TribPtpPmTomTxLBCMax_Type = FloatHundredths
_TribPtpPmTomTxLBCMax_Object = MibTableColumn
tribPtpPmTomTxLBCMax = _TribPtpPmTomTxLBCMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 5),
    _TribPtpPmTomTxLBCMax_Type()
)
tribPtpPmTomTxLBCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomTxLBCMax.setStatus("current")
_TribPtpPmTomTxLBCAve_Type = FloatHundredths
_TribPtpPmTomTxLBCAve_Object = MibTableColumn
tribPtpPmTomTxLBCAve = _TribPtpPmTomTxLBCAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 6),
    _TribPtpPmTomTxLBCAve_Type()
)
tribPtpPmTomTxLBCAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomTxLBCAve.setStatus("current")
_TribPtpPmTomOptMin_Type = FloatHundredths
_TribPtpPmTomOptMin_Object = MibTableColumn
tribPtpPmTomOptMin = _TribPtpPmTomOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 7),
    _TribPtpPmTomOptMin_Type()
)
tribPtpPmTomOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOptMin.setStatus("current")
_TribPtpPmTomOptMax_Type = FloatHundredths
_TribPtpPmTomOptMax_Object = MibTableColumn
tribPtpPmTomOptMax = _TribPtpPmTomOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 8),
    _TribPtpPmTomOptMax_Type()
)
tribPtpPmTomOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOptMax.setStatus("current")
_TribPtpPmTomOptAve_Type = FloatHundredths
_TribPtpPmTomOptAve_Object = MibTableColumn
tribPtpPmTomOptAve = _TribPtpPmTomOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 9),
    _TribPtpPmTomOptAve_Type()
)
tribPtpPmTomOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOptAve.setStatus("current")
_TribPtpPmTomOprMin_Type = FloatHundredths
_TribPtpPmTomOprMin_Object = MibTableColumn
tribPtpPmTomOprMin = _TribPtpPmTomOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 10),
    _TribPtpPmTomOprMin_Type()
)
tribPtpPmTomOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOprMin.setStatus("current")
_TribPtpPmTomOprMax_Type = FloatHundredths
_TribPtpPmTomOprMax_Object = MibTableColumn
tribPtpPmTomOprMax = _TribPtpPmTomOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 11),
    _TribPtpPmTomOprMax_Type()
)
tribPtpPmTomOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOprMax.setStatus("current")
_TribPtpPmTomOprAve_Type = FloatHundredths
_TribPtpPmTomOprAve_Object = MibTableColumn
tribPtpPmTomOprAve = _TribPtpPmTomOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 12),
    _TribPtpPmTomOprAve_Type()
)
tribPtpPmTomOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOprAve.setStatus("current")
_TribPtpPmTomTxLBC02Min_Type = FloatHundredths
_TribPtpPmTomTxLBC02Min_Object = MibTableColumn
tribPtpPmTomTxLBC02Min = _TribPtpPmTomTxLBC02Min_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 13),
    _TribPtpPmTomTxLBC02Min_Type()
)
tribPtpPmTomTxLBC02Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomTxLBC02Min.setStatus("current")
_TribPtpPmTomTxLBC02Max_Type = FloatHundredths
_TribPtpPmTomTxLBC02Max_Object = MibTableColumn
tribPtpPmTomTxLBC02Max = _TribPtpPmTomTxLBC02Max_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 14),
    _TribPtpPmTomTxLBC02Max_Type()
)
tribPtpPmTomTxLBC02Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomTxLBC02Max.setStatus("current")
_TribPtpPmTomTxLBC02Ave_Type = FloatHundredths
_TribPtpPmTomTxLBC02Ave_Object = MibTableColumn
tribPtpPmTomTxLBC02Ave = _TribPtpPmTomTxLBC02Ave_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 15),
    _TribPtpPmTomTxLBC02Ave_Type()
)
tribPtpPmTomTxLBC02Ave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomTxLBC02Ave.setStatus("current")
_TribPtpPmTomOpt02Min_Type = FloatHundredths
_TribPtpPmTomOpt02Min_Object = MibTableColumn
tribPtpPmTomOpt02Min = _TribPtpPmTomOpt02Min_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 16),
    _TribPtpPmTomOpt02Min_Type()
)
tribPtpPmTomOpt02Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOpt02Min.setStatus("current")
_TribPtpPmTomOpt02Max_Type = FloatHundredths
_TribPtpPmTomOpt02Max_Object = MibTableColumn
tribPtpPmTomOpt02Max = _TribPtpPmTomOpt02Max_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 17),
    _TribPtpPmTomOpt02Max_Type()
)
tribPtpPmTomOpt02Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOpt02Max.setStatus("current")
_TribPtpPmTomOpt02Ave_Type = FloatHundredths
_TribPtpPmTomOpt02Ave_Object = MibTableColumn
tribPtpPmTomOpt02Ave = _TribPtpPmTomOpt02Ave_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 18),
    _TribPtpPmTomOpt02Ave_Type()
)
tribPtpPmTomOpt02Ave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOpt02Ave.setStatus("current")
_TribPtpPmTomOpr02Min_Type = FloatHundredths
_TribPtpPmTomOpr02Min_Object = MibTableColumn
tribPtpPmTomOpr02Min = _TribPtpPmTomOpr02Min_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 19),
    _TribPtpPmTomOpr02Min_Type()
)
tribPtpPmTomOpr02Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOpr02Min.setStatus("current")
_TribPtpPmTomOpr02Max_Type = FloatHundredths
_TribPtpPmTomOpr02Max_Object = MibTableColumn
tribPtpPmTomOpr02Max = _TribPtpPmTomOpr02Max_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 20),
    _TribPtpPmTomOpr02Max_Type()
)
tribPtpPmTomOpr02Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOpr02Max.setStatus("current")
_TribPtpPmTomOpr02Ave_Type = FloatHundredths
_TribPtpPmTomOpr02Ave_Object = MibTableColumn
tribPtpPmTomOpr02Ave = _TribPtpPmTomOpr02Ave_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 21),
    _TribPtpPmTomOpr02Ave_Type()
)
tribPtpPmTomOpr02Ave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOpr02Ave.setStatus("current")
_TribPtpPmTomTxLBC03Min_Type = FloatHundredths
_TribPtpPmTomTxLBC03Min_Object = MibTableColumn
tribPtpPmTomTxLBC03Min = _TribPtpPmTomTxLBC03Min_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 22),
    _TribPtpPmTomTxLBC03Min_Type()
)
tribPtpPmTomTxLBC03Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomTxLBC03Min.setStatus("current")
_TribPtpPmTomTxLBC03Max_Type = FloatHundredths
_TribPtpPmTomTxLBC03Max_Object = MibTableColumn
tribPtpPmTomTxLBC03Max = _TribPtpPmTomTxLBC03Max_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 23),
    _TribPtpPmTomTxLBC03Max_Type()
)
tribPtpPmTomTxLBC03Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomTxLBC03Max.setStatus("current")
_TribPtpPmTomTxLBC03Ave_Type = FloatHundredths
_TribPtpPmTomTxLBC03Ave_Object = MibTableColumn
tribPtpPmTomTxLBC03Ave = _TribPtpPmTomTxLBC03Ave_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 24),
    _TribPtpPmTomTxLBC03Ave_Type()
)
tribPtpPmTomTxLBC03Ave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomTxLBC03Ave.setStatus("current")
_TribPtpPmTomOpt03Min_Type = FloatHundredths
_TribPtpPmTomOpt03Min_Object = MibTableColumn
tribPtpPmTomOpt03Min = _TribPtpPmTomOpt03Min_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 25),
    _TribPtpPmTomOpt03Min_Type()
)
tribPtpPmTomOpt03Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOpt03Min.setStatus("current")
_TribPtpPmTomOpt03Max_Type = FloatHundredths
_TribPtpPmTomOpt03Max_Object = MibTableColumn
tribPtpPmTomOpt03Max = _TribPtpPmTomOpt03Max_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 26),
    _TribPtpPmTomOpt03Max_Type()
)
tribPtpPmTomOpt03Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOpt03Max.setStatus("current")
_TribPtpPmTomOpt03Ave_Type = FloatHundredths
_TribPtpPmTomOpt03Ave_Object = MibTableColumn
tribPtpPmTomOpt03Ave = _TribPtpPmTomOpt03Ave_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 27),
    _TribPtpPmTomOpt03Ave_Type()
)
tribPtpPmTomOpt03Ave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOpt03Ave.setStatus("current")
_TribPtpPmTomOpr03Min_Type = FloatHundredths
_TribPtpPmTomOpr03Min_Object = MibTableColumn
tribPtpPmTomOpr03Min = _TribPtpPmTomOpr03Min_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 28),
    _TribPtpPmTomOpr03Min_Type()
)
tribPtpPmTomOpr03Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOpr03Min.setStatus("current")
_TribPtpPmTomOpr03Max_Type = FloatHundredths
_TribPtpPmTomOpr03Max_Object = MibTableColumn
tribPtpPmTomOpr03Max = _TribPtpPmTomOpr03Max_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 29),
    _TribPtpPmTomOpr03Max_Type()
)
tribPtpPmTomOpr03Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOpr03Max.setStatus("current")
_TribPtpPmTomOpr03Ave_Type = FloatHundredths
_TribPtpPmTomOpr03Ave_Object = MibTableColumn
tribPtpPmTomOpr03Ave = _TribPtpPmTomOpr03Ave_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 30),
    _TribPtpPmTomOpr03Ave_Type()
)
tribPtpPmTomOpr03Ave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOpr03Ave.setStatus("current")
_TribPtpPmTomTxLBC04Min_Type = FloatHundredths
_TribPtpPmTomTxLBC04Min_Object = MibTableColumn
tribPtpPmTomTxLBC04Min = _TribPtpPmTomTxLBC04Min_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 31),
    _TribPtpPmTomTxLBC04Min_Type()
)
tribPtpPmTomTxLBC04Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomTxLBC04Min.setStatus("current")
_TribPtpPmTomTxLBC04Max_Type = FloatHundredths
_TribPtpPmTomTxLBC04Max_Object = MibTableColumn
tribPtpPmTomTxLBC04Max = _TribPtpPmTomTxLBC04Max_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 32),
    _TribPtpPmTomTxLBC04Max_Type()
)
tribPtpPmTomTxLBC04Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomTxLBC04Max.setStatus("current")
_TribPtpPmTomTxLBC04Ave_Type = FloatHundredths
_TribPtpPmTomTxLBC04Ave_Object = MibTableColumn
tribPtpPmTomTxLBC04Ave = _TribPtpPmTomTxLBC04Ave_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 33),
    _TribPtpPmTomTxLBC04Ave_Type()
)
tribPtpPmTomTxLBC04Ave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomTxLBC04Ave.setStatus("current")
_TribPtpPmTomOpt04Min_Type = FloatHundredths
_TribPtpPmTomOpt04Min_Object = MibTableColumn
tribPtpPmTomOpt04Min = _TribPtpPmTomOpt04Min_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 34),
    _TribPtpPmTomOpt04Min_Type()
)
tribPtpPmTomOpt04Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOpt04Min.setStatus("current")
_TribPtpPmTomOpt04Max_Type = FloatHundredths
_TribPtpPmTomOpt04Max_Object = MibTableColumn
tribPtpPmTomOpt04Max = _TribPtpPmTomOpt04Max_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 35),
    _TribPtpPmTomOpt04Max_Type()
)
tribPtpPmTomOpt04Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOpt04Max.setStatus("current")
_TribPtpPmTomOpt04Ave_Type = FloatHundredths
_TribPtpPmTomOpt04Ave_Object = MibTableColumn
tribPtpPmTomOpt04Ave = _TribPtpPmTomOpt04Ave_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 36),
    _TribPtpPmTomOpt04Ave_Type()
)
tribPtpPmTomOpt04Ave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOpt04Ave.setStatus("current")
_TribPtpPmTomOpr04Min_Type = FloatHundredths
_TribPtpPmTomOpr04Min_Object = MibTableColumn
tribPtpPmTomOpr04Min = _TribPtpPmTomOpr04Min_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 37),
    _TribPtpPmTomOpr04Min_Type()
)
tribPtpPmTomOpr04Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOpr04Min.setStatus("current")
_TribPtpPmTomOpr04Max_Type = FloatHundredths
_TribPtpPmTomOpr04Max_Object = MibTableColumn
tribPtpPmTomOpr04Max = _TribPtpPmTomOpr04Max_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 38),
    _TribPtpPmTomOpr04Max_Type()
)
tribPtpPmTomOpr04Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOpr04Max.setStatus("current")
_TribPtpPmTomOpr04Ave_Type = FloatHundredths
_TribPtpPmTomOpr04Ave_Object = MibTableColumn
tribPtpPmTomOpr04Ave = _TribPtpPmTomOpr04Ave_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 39),
    _TribPtpPmTomOpr04Ave_Type()
)
tribPtpPmTomOpr04Ave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOpr04Ave.setStatus("current")
_TribPtpPmTomOptTotalMin_Type = FloatHundredths
_TribPtpPmTomOptTotalMin_Object = MibTableColumn
tribPtpPmTomOptTotalMin = _TribPtpPmTomOptTotalMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 40),
    _TribPtpPmTomOptTotalMin_Type()
)
tribPtpPmTomOptTotalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOptTotalMin.setStatus("current")
_TribPtpPmTomOptTotalMax_Type = FloatHundredths
_TribPtpPmTomOptTotalMax_Object = MibTableColumn
tribPtpPmTomOptTotalMax = _TribPtpPmTomOptTotalMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 41),
    _TribPtpPmTomOptTotalMax_Type()
)
tribPtpPmTomOptTotalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOptTotalMax.setStatus("current")
_TribPtpPmTomOptTotalAve_Type = FloatHundredths
_TribPtpPmTomOptTotalAve_Object = MibTableColumn
tribPtpPmTomOptTotalAve = _TribPtpPmTomOptTotalAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 42),
    _TribPtpPmTomOptTotalAve_Type()
)
tribPtpPmTomOptTotalAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOptTotalAve.setStatus("current")
_TribPtpPmTomOprTotalMin_Type = FloatHundredths
_TribPtpPmTomOprTotalMin_Object = MibTableColumn
tribPtpPmTomOprTotalMin = _TribPtpPmTomOprTotalMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 43),
    _TribPtpPmTomOprTotalMin_Type()
)
tribPtpPmTomOprTotalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOprTotalMin.setStatus("current")
_TribPtpPmTomOprTotalMax_Type = FloatHundredths
_TribPtpPmTomOprTotalMax_Object = MibTableColumn
tribPtpPmTomOprTotalMax = _TribPtpPmTomOprTotalMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 44),
    _TribPtpPmTomOprTotalMax_Type()
)
tribPtpPmTomOprTotalMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOprTotalMax.setStatus("current")
_TribPtpPmTomOprTotalAve_Type = FloatHundredths
_TribPtpPmTomOprTotalAve_Object = MibTableColumn
tribPtpPmTomOprTotalAve = _TribPtpPmTomOprTotalAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 2, 1, 45),
    _TribPtpPmTomOprTotalAve_Type()
)
tribPtpPmTomOprTotalAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tribPtpPmTomOprTotalAve.setStatus("current")
_TribPtpPmConformance_ObjectIdentity = ObjectIdentity
tribPtpPmConformance = _TribPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 3)
)
_TribPtpPmCompliances_ObjectIdentity = ObjectIdentity
tribPtpPmCompliances = _TribPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 3, 1)
)
_TribPtpPmGroups_ObjectIdentity = ObjectIdentity
tribPtpPmGroups = _TribPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 3, 2)
)

# Managed Objects groups

tribPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 3, 2, 1)
)
tribPtpPmGroup.setObjects(
      *(("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmValidity"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomTxLBCMin"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomTxLBCMax"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomTxLBCAve"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOptMin"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOptMax"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOptAve"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOprMin"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOprMax"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOprAve"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomTxLBC02Min"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomTxLBC02Max"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomTxLBC02Ave"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOpt02Min"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOpt02Max"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOpt02Ave"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOpr02Min"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOpr02Max"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOpr02Ave"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomTxLBC03Min"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomTxLBC03Max"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomTxLBC03Ave"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOpt03Min"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOpt03Max"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOpt03Ave"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOpr03Min"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOpr03Max"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOpr03Ave"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomTxLBC04Min"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomTxLBC04Max"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomTxLBC04Ave"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOpt04Min"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOpt04Max"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOpt04Ave"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOpr04Min"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOpr04Max"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOpr04Ave"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOptTotalMin"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOptTotalMax"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOptTotalAve"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOprTotalMin"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOprTotalMax"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmTomOprTotalAve"))
)
if mibBuilder.loadTexts:
    tribPtpPmGroup.setStatus("current")

tribPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 3, 2, 2)
)
tribPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmRealTomTxLBC"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmRealTomOpt"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmRealTomOpr"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmRealTomTxLBC02"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmRealTomOpt02"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmRealTomOpr02"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmRealTomTxLBC03"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmRealTomOpt03"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmRealTomOpr03"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmRealTomTxLBC04"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmRealTomOpt04"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmRealTomOpr04"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmRealTomOptTotal"),
        ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmRealTomOprTotal"))
)
if mibBuilder.loadTexts:
    tribPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tribPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 3, 1, 1)
)
tribPtpPmCompliance.setObjects(
    ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmGroup")
)
if mibBuilder.loadTexts:
    tribPtpPmCompliance.setStatus(
        "current"
    )

tribPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 3, 3, 1, 2)
)
tribPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-TRIBPTP-MIB", "tribPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    tribPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-TRIBPTP-MIB",
    **{"tribPtpPmMIB": tribPtpPmMIB,
       "tribPtpPmRealTable": tribPtpPmRealTable,
       "tribPtpPmRealEntry": tribPtpPmRealEntry,
       "tribPtpPmRealTomTxLBC": tribPtpPmRealTomTxLBC,
       "tribPtpPmRealTomOpt": tribPtpPmRealTomOpt,
       "tribPtpPmRealTomOpr": tribPtpPmRealTomOpr,
       "tribPtpPmRealTomTxLBC02": tribPtpPmRealTomTxLBC02,
       "tribPtpPmRealTomOpt02": tribPtpPmRealTomOpt02,
       "tribPtpPmRealTomOpr02": tribPtpPmRealTomOpr02,
       "tribPtpPmRealTomTxLBC03": tribPtpPmRealTomTxLBC03,
       "tribPtpPmRealTomOpt03": tribPtpPmRealTomOpt03,
       "tribPtpPmRealTomOpr03": tribPtpPmRealTomOpr03,
       "tribPtpPmRealTomTxLBC04": tribPtpPmRealTomTxLBC04,
       "tribPtpPmRealTomOpt04": tribPtpPmRealTomOpt04,
       "tribPtpPmRealTomOpr04": tribPtpPmRealTomOpr04,
       "tribPtpPmRealTomOptTotal": tribPtpPmRealTomOptTotal,
       "tribPtpPmRealTomOprTotal": tribPtpPmRealTomOprTotal,
       "tribPtpPmTable": tribPtpPmTable,
       "tribPtpPmEntry": tribPtpPmEntry,
       "tribPtpPmTimestamp": tribPtpPmTimestamp,
       "tribPtpPmSampleDuration": tribPtpPmSampleDuration,
       "tribPtpPmValidity": tribPtpPmValidity,
       "tribPtpPmTomTxLBCMin": tribPtpPmTomTxLBCMin,
       "tribPtpPmTomTxLBCMax": tribPtpPmTomTxLBCMax,
       "tribPtpPmTomTxLBCAve": tribPtpPmTomTxLBCAve,
       "tribPtpPmTomOptMin": tribPtpPmTomOptMin,
       "tribPtpPmTomOptMax": tribPtpPmTomOptMax,
       "tribPtpPmTomOptAve": tribPtpPmTomOptAve,
       "tribPtpPmTomOprMin": tribPtpPmTomOprMin,
       "tribPtpPmTomOprMax": tribPtpPmTomOprMax,
       "tribPtpPmTomOprAve": tribPtpPmTomOprAve,
       "tribPtpPmTomTxLBC02Min": tribPtpPmTomTxLBC02Min,
       "tribPtpPmTomTxLBC02Max": tribPtpPmTomTxLBC02Max,
       "tribPtpPmTomTxLBC02Ave": tribPtpPmTomTxLBC02Ave,
       "tribPtpPmTomOpt02Min": tribPtpPmTomOpt02Min,
       "tribPtpPmTomOpt02Max": tribPtpPmTomOpt02Max,
       "tribPtpPmTomOpt02Ave": tribPtpPmTomOpt02Ave,
       "tribPtpPmTomOpr02Min": tribPtpPmTomOpr02Min,
       "tribPtpPmTomOpr02Max": tribPtpPmTomOpr02Max,
       "tribPtpPmTomOpr02Ave": tribPtpPmTomOpr02Ave,
       "tribPtpPmTomTxLBC03Min": tribPtpPmTomTxLBC03Min,
       "tribPtpPmTomTxLBC03Max": tribPtpPmTomTxLBC03Max,
       "tribPtpPmTomTxLBC03Ave": tribPtpPmTomTxLBC03Ave,
       "tribPtpPmTomOpt03Min": tribPtpPmTomOpt03Min,
       "tribPtpPmTomOpt03Max": tribPtpPmTomOpt03Max,
       "tribPtpPmTomOpt03Ave": tribPtpPmTomOpt03Ave,
       "tribPtpPmTomOpr03Min": tribPtpPmTomOpr03Min,
       "tribPtpPmTomOpr03Max": tribPtpPmTomOpr03Max,
       "tribPtpPmTomOpr03Ave": tribPtpPmTomOpr03Ave,
       "tribPtpPmTomTxLBC04Min": tribPtpPmTomTxLBC04Min,
       "tribPtpPmTomTxLBC04Max": tribPtpPmTomTxLBC04Max,
       "tribPtpPmTomTxLBC04Ave": tribPtpPmTomTxLBC04Ave,
       "tribPtpPmTomOpt04Min": tribPtpPmTomOpt04Min,
       "tribPtpPmTomOpt04Max": tribPtpPmTomOpt04Max,
       "tribPtpPmTomOpt04Ave": tribPtpPmTomOpt04Ave,
       "tribPtpPmTomOpr04Min": tribPtpPmTomOpr04Min,
       "tribPtpPmTomOpr04Max": tribPtpPmTomOpr04Max,
       "tribPtpPmTomOpr04Ave": tribPtpPmTomOpr04Ave,
       "tribPtpPmTomOptTotalMin": tribPtpPmTomOptTotalMin,
       "tribPtpPmTomOptTotalMax": tribPtpPmTomOptTotalMax,
       "tribPtpPmTomOptTotalAve": tribPtpPmTomOptTotalAve,
       "tribPtpPmTomOprTotalMin": tribPtpPmTomOprTotalMin,
       "tribPtpPmTomOprTotalMax": tribPtpPmTomOprTotalMax,
       "tribPtpPmTomOprTotalAve": tribPtpPmTomOprTotalAve,
       "tribPtpPmConformance": tribPtpPmConformance,
       "tribPtpPmCompliances": tribPtpPmCompliances,
       "tribPtpPmCompliance": tribPtpPmCompliance,
       "tribPtpPmRealCompliance": tribPtpPmRealCompliance,
       "tribPtpPmGroups": tribPtpPmGroups,
       "tribPtpPmGroup": tribPtpPmGroup,
       "tribPtpPmRealGroup": tribPtpPmRealGroup}
)
