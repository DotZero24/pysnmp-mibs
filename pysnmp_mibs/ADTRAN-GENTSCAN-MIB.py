# SNMP MIB module (ADTRAN-GENTSCAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENTSCAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:47 2025
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

(adGenHDSL,
 adGenHDSLID) = mibBuilder.importSymbols(
    "ADTRAN-GENHDSL-MIB",
    "adGenHDSL",
    "adGenHDSLID")

(adEShdslInvIndex,) = mibBuilder.importSymbols(
    "ADTRAN-SHDSL-MIB",
    "adEShdslInvIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

adGenTSCANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 51, 1, 1)
)
if mibBuilder.loadTexts:
    adGenTSCANMIB.setRevisions(
        ("2012-09-05 00:00",
         "2009-07-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenTSCANmg_ObjectIdentity = ObjectIdentity
adGenTSCANmg = _AdGenTSCANmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1)
)
_AdGenTSCANProv_ObjectIdentity = ObjectIdentity
adGenTSCANProv = _AdGenTSCANProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1)
)
_AdGenTSCANProvTable_Object = MibTable
adGenTSCANProvTable = _AdGenTSCANProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adGenTSCANProvTable.setStatus("current")
_AdGenTSCANProvEntry_Object = MibTableRow
adGenTSCANProvEntry = _AdGenTSCANProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1)
)
adGenTSCANProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTSCANProvEntry.setStatus("current")


class _AdGenTSCANAccumTscanData_Type(Integer32):
    """Custom type adGenTSCANAccumTscanData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_AdGenTSCANAccumTscanData_Type.__name__ = "Integer32"
_AdGenTSCANAccumTscanData_Object = MibTableColumn
adGenTSCANAccumTscanData = _AdGenTSCANAccumTscanData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 1),
    _AdGenTSCANAccumTscanData_Type()
)
adGenTSCANAccumTscanData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTSCANAccumTscanData.setStatus("current")


class _AdGenTSCANTscanDataStatus_Type(Integer32):
    """Custom type adGenTSCANTscanDataStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("done", 1),
          ("accumulating", 2),
          ("idle", 3))
    )


_AdGenTSCANTscanDataStatus_Type.__name__ = "Integer32"
_AdGenTSCANTscanDataStatus_Object = MibTableColumn
adGenTSCANTscanDataStatus = _AdGenTSCANTscanDataStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 2),
    _AdGenTSCANTscanDataStatus_Type()
)
adGenTSCANTscanDataStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANTscanDataStatus.setStatus("current")
_AdGenTSCANECTG1B1_Type = DisplayString
_AdGenTSCANECTG1B1_Object = MibTableColumn
adGenTSCANECTG1B1 = _AdGenTSCANECTG1B1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 3),
    _AdGenTSCANECTG1B1_Type()
)
adGenTSCANECTG1B1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTG1B1.setStatus("current")
_AdGenTSCANECTG1B2_Type = DisplayString
_AdGenTSCANECTG1B2_Object = MibTableColumn
adGenTSCANECTG1B2 = _AdGenTSCANECTG1B2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 4),
    _AdGenTSCANECTG1B2_Type()
)
adGenTSCANECTG1B2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTG1B2.setStatus("current")
_AdGenTSCANECTG1B3_Type = DisplayString
_AdGenTSCANECTG1B3_Object = MibTableColumn
adGenTSCANECTG1B3 = _AdGenTSCANECTG1B3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 5),
    _AdGenTSCANECTG1B3_Type()
)
adGenTSCANECTG1B3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTG1B3.setStatus("current")
_AdGenTSCANECTG1B4_Type = DisplayString
_AdGenTSCANECTG1B4_Object = MibTableColumn
adGenTSCANECTG1B4 = _AdGenTSCANECTG1B4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 6),
    _AdGenTSCANECTG1B4_Type()
)
adGenTSCANECTG1B4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTG1B4.setStatus("current")
_AdGenTSCANECTG1B5_Type = DisplayString
_AdGenTSCANECTG1B5_Object = MibTableColumn
adGenTSCANECTG1B5 = _AdGenTSCANECTG1B5_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 7),
    _AdGenTSCANECTG1B5_Type()
)
adGenTSCANECTG1B5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTG1B5.setStatus("current")
_AdGenTSCANECTG1B6_Type = DisplayString
_AdGenTSCANECTG1B6_Object = MibTableColumn
adGenTSCANECTG1B6 = _AdGenTSCANECTG1B6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 8),
    _AdGenTSCANECTG1B6_Type()
)
adGenTSCANECTG1B6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTG1B6.setStatus("current")
_AdGenTSCANECTG1B7_Type = DisplayString
_AdGenTSCANECTG1B7_Object = MibTableColumn
adGenTSCANECTG1B7 = _AdGenTSCANECTG1B7_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 9),
    _AdGenTSCANECTG1B7_Type()
)
adGenTSCANECTG1B7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTG1B7.setStatus("current")
_AdGenTSCANECTG1B8_Type = DisplayString
_AdGenTSCANECTG1B8_Object = MibTableColumn
adGenTSCANECTG1B8 = _AdGenTSCANECTG1B8_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 10),
    _AdGenTSCANECTG1B8_Type()
)
adGenTSCANECTG1B8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTG1B8.setStatus("current")
_AdGenTSCANECTG1B9_Type = DisplayString
_AdGenTSCANECTG1B9_Object = MibTableColumn
adGenTSCANECTG1B9 = _AdGenTSCANECTG1B9_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 11),
    _AdGenTSCANECTG1B9_Type()
)
adGenTSCANECTG1B9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTG1B9.setStatus("current")
_AdGenTSCANECTG2B1_Type = DisplayString
_AdGenTSCANECTG2B1_Object = MibTableColumn
adGenTSCANECTG2B1 = _AdGenTSCANECTG2B1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 12),
    _AdGenTSCANECTG2B1_Type()
)
adGenTSCANECTG2B1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTG2B1.setStatus("current")
_AdGenTSCANECTG2B2_Type = DisplayString
_AdGenTSCANECTG2B2_Object = MibTableColumn
adGenTSCANECTG2B2 = _AdGenTSCANECTG2B2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 13),
    _AdGenTSCANECTG2B2_Type()
)
adGenTSCANECTG2B2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTG2B2.setStatus("current")
_AdGenTSCANECTG2B3_Type = DisplayString
_AdGenTSCANECTG2B3_Object = MibTableColumn
adGenTSCANECTG2B3 = _AdGenTSCANECTG2B3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 14),
    _AdGenTSCANECTG2B3_Type()
)
adGenTSCANECTG2B3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTG2B3.setStatus("current")
_AdGenTSCANECTG2B4_Type = DisplayString
_AdGenTSCANECTG2B4_Object = MibTableColumn
adGenTSCANECTG2B4 = _AdGenTSCANECTG2B4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 15),
    _AdGenTSCANECTG2B4_Type()
)
adGenTSCANECTG2B4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTG2B4.setStatus("current")
_AdGenTSCANECTG2B5_Type = DisplayString
_AdGenTSCANECTG2B5_Object = MibTableColumn
adGenTSCANECTG2B5 = _AdGenTSCANECTG2B5_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 16),
    _AdGenTSCANECTG2B5_Type()
)
adGenTSCANECTG2B5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTG2B5.setStatus("current")
_AdGenTSCANECTG2B6_Type = DisplayString
_AdGenTSCANECTG2B6_Object = MibTableColumn
adGenTSCANECTG2B6 = _AdGenTSCANECTG2B6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 17),
    _AdGenTSCANECTG2B6_Type()
)
adGenTSCANECTG2B6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTG2B6.setStatus("current")
_AdGenTSCANECTG2B7_Type = DisplayString
_AdGenTSCANECTG2B7_Object = MibTableColumn
adGenTSCANECTG2B7 = _AdGenTSCANECTG2B7_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 18),
    _AdGenTSCANECTG2B7_Type()
)
adGenTSCANECTG2B7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTG2B7.setStatus("current")
_AdGenTSCANECTG2B8_Type = DisplayString
_AdGenTSCANECTG2B8_Object = MibTableColumn
adGenTSCANECTG2B8 = _AdGenTSCANECTG2B8_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 19),
    _AdGenTSCANECTG2B8_Type()
)
adGenTSCANECTG2B8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTG2B8.setStatus("current")
_AdGenTSCANECTG2B9_Type = DisplayString
_AdGenTSCANECTG2B9_Object = MibTableColumn
adGenTSCANECTG2B9 = _AdGenTSCANECTG2B9_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 20),
    _AdGenTSCANECTG2B9_Type()
)
adGenTSCANECTG2B9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTG2B9.setStatus("current")
_AdGenTSCANECTB1B1_Type = DisplayString
_AdGenTSCANECTB1B1_Object = MibTableColumn
adGenTSCANECTB1B1 = _AdGenTSCANECTB1B1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 21),
    _AdGenTSCANECTB1B1_Type()
)
adGenTSCANECTB1B1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB1B1.setStatus("current")
_AdGenTSCANECTB1B2_Type = DisplayString
_AdGenTSCANECTB1B2_Object = MibTableColumn
adGenTSCANECTB1B2 = _AdGenTSCANECTB1B2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 22),
    _AdGenTSCANECTB1B2_Type()
)
adGenTSCANECTB1B2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB1B2.setStatus("current")
_AdGenTSCANECTB1B3_Type = DisplayString
_AdGenTSCANECTB1B3_Object = MibTableColumn
adGenTSCANECTB1B3 = _AdGenTSCANECTB1B3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 23),
    _AdGenTSCANECTB1B3_Type()
)
adGenTSCANECTB1B3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB1B3.setStatus("current")
_AdGenTSCANECTB1B4_Type = DisplayString
_AdGenTSCANECTB1B4_Object = MibTableColumn
adGenTSCANECTB1B4 = _AdGenTSCANECTB1B4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 24),
    _AdGenTSCANECTB1B4_Type()
)
adGenTSCANECTB1B4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB1B4.setStatus("current")
_AdGenTSCANECTB1B5_Type = DisplayString
_AdGenTSCANECTB1B5_Object = MibTableColumn
adGenTSCANECTB1B5 = _AdGenTSCANECTB1B5_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 25),
    _AdGenTSCANECTB1B5_Type()
)
adGenTSCANECTB1B5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB1B5.setStatus("current")
_AdGenTSCANECTB1B6_Type = DisplayString
_AdGenTSCANECTB1B6_Object = MibTableColumn
adGenTSCANECTB1B6 = _AdGenTSCANECTB1B6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 26),
    _AdGenTSCANECTB1B6_Type()
)
adGenTSCANECTB1B6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB1B6.setStatus("current")
_AdGenTSCANECTB1B7_Type = DisplayString
_AdGenTSCANECTB1B7_Object = MibTableColumn
adGenTSCANECTB1B7 = _AdGenTSCANECTB1B7_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 27),
    _AdGenTSCANECTB1B7_Type()
)
adGenTSCANECTB1B7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB1B7.setStatus("current")
_AdGenTSCANECTB1B8_Type = DisplayString
_AdGenTSCANECTB1B8_Object = MibTableColumn
adGenTSCANECTB1B8 = _AdGenTSCANECTB1B8_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 28),
    _AdGenTSCANECTB1B8_Type()
)
adGenTSCANECTB1B8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB1B8.setStatus("current")
_AdGenTSCANECTB1B9_Type = DisplayString
_AdGenTSCANECTB1B9_Object = MibTableColumn
adGenTSCANECTB1B9 = _AdGenTSCANECTB1B9_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 29),
    _AdGenTSCANECTB1B9_Type()
)
adGenTSCANECTB1B9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB1B9.setStatus("current")
_AdGenTSCANECTB2B1_Type = DisplayString
_AdGenTSCANECTB2B1_Object = MibTableColumn
adGenTSCANECTB2B1 = _AdGenTSCANECTB2B1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 30),
    _AdGenTSCANECTB2B1_Type()
)
adGenTSCANECTB2B1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB2B1.setStatus("current")
_AdGenTSCANECTB2B2_Type = DisplayString
_AdGenTSCANECTB2B2_Object = MibTableColumn
adGenTSCANECTB2B2 = _AdGenTSCANECTB2B2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 31),
    _AdGenTSCANECTB2B2_Type()
)
adGenTSCANECTB2B2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB2B2.setStatus("current")
_AdGenTSCANECTB2B3_Type = DisplayString
_AdGenTSCANECTB2B3_Object = MibTableColumn
adGenTSCANECTB2B3 = _AdGenTSCANECTB2B3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 32),
    _AdGenTSCANECTB2B3_Type()
)
adGenTSCANECTB2B3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB2B3.setStatus("current")
_AdGenTSCANECTB2B4_Type = DisplayString
_AdGenTSCANECTB2B4_Object = MibTableColumn
adGenTSCANECTB2B4 = _AdGenTSCANECTB2B4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 33),
    _AdGenTSCANECTB2B4_Type()
)
adGenTSCANECTB2B4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB2B4.setStatus("current")
_AdGenTSCANECTB2B5_Type = DisplayString
_AdGenTSCANECTB2B5_Object = MibTableColumn
adGenTSCANECTB2B5 = _AdGenTSCANECTB2B5_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 34),
    _AdGenTSCANECTB2B5_Type()
)
adGenTSCANECTB2B5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB2B5.setStatus("current")
_AdGenTSCANECTB2B6_Type = DisplayString
_AdGenTSCANECTB2B6_Object = MibTableColumn
adGenTSCANECTB2B6 = _AdGenTSCANECTB2B6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 35),
    _AdGenTSCANECTB2B6_Type()
)
adGenTSCANECTB2B6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB2B6.setStatus("current")
_AdGenTSCANECTB2B7_Type = DisplayString
_AdGenTSCANECTB2B7_Object = MibTableColumn
adGenTSCANECTB2B7 = _AdGenTSCANECTB2B7_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 36),
    _AdGenTSCANECTB2B7_Type()
)
adGenTSCANECTB2B7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB2B7.setStatus("current")
_AdGenTSCANECTB2B8_Type = DisplayString
_AdGenTSCANECTB2B8_Object = MibTableColumn
adGenTSCANECTB2B8 = _AdGenTSCANECTB2B8_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 37),
    _AdGenTSCANECTB2B8_Type()
)
adGenTSCANECTB2B8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB2B8.setStatus("current")
_AdGenTSCANECTB2B9_Type = DisplayString
_AdGenTSCANECTB2B9_Object = MibTableColumn
adGenTSCANECTB2B9 = _AdGenTSCANECTB2B9_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 38),
    _AdGenTSCANECTB2B9_Type()
)
adGenTSCANECTB2B9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB2B9.setStatus("current")
_AdGenTSCANST1B_Type = DisplayString
_AdGenTSCANST1B_Object = MibTableColumn
adGenTSCANST1B = _AdGenTSCANST1B_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 39),
    _AdGenTSCANST1B_Type()
)
adGenTSCANST1B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANST1B.setStatus("current")
_AdGenTSCANST2B_Type = DisplayString
_AdGenTSCANST2B_Object = MibTableColumn
adGenTSCANST2B = _AdGenTSCANST2B_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 40),
    _AdGenTSCANST2B_Type()
)
adGenTSCANST2B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANST2B.setStatus("current")


class _AdGenTSCANLS1_Type(Integer32):
    """Custom type adGenTSCANLS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("complete", 2))
    )


_AdGenTSCANLS1_Type.__name__ = "Integer32"
_AdGenTSCANLS1_Object = MibTableColumn
adGenTSCANLS1 = _AdGenTSCANLS1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 41),
    _AdGenTSCANLS1_Type()
)
adGenTSCANLS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANLS1.setStatus("current")


class _AdGenTSCANLS2_Type(Integer32):
    """Custom type adGenTSCANLS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("complete", 2))
    )


_AdGenTSCANLS2_Type.__name__ = "Integer32"
_AdGenTSCANLS2_Object = MibTableColumn
adGenTSCANLS2 = _AdGenTSCANLS2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 42),
    _AdGenTSCANLS2_Type()
)
adGenTSCANLS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANLS2.setStatus("current")


class _AdGenTSCANRate_Type(Integer32):
    """Custom type adGenTSCANRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sixteenDS0s", 1),
          ("thirtytwoDS0s", 2))
    )


_AdGenTSCANRate_Type.__name__ = "Integer32"
_AdGenTSCANRate_Object = MibTableColumn
adGenTSCANRate = _AdGenTSCANRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 43),
    _AdGenTSCANRate_Type()
)
adGenTSCANRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTSCANRate.setStatus("current")
_AdGenTSCANLastTime_Type = TimeTicks
_AdGenTSCANLastTime_Object = MibTableColumn
adGenTSCANLastTime = _AdGenTSCANLastTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 44),
    _AdGenTSCANLastTime_Type()
)
adGenTSCANLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANLastTime.setStatus("current")


class _AdGenTSCANRepeaterIndex_Type(Integer32):
    """Custom type adGenTSCANRepeaterIndex based on Integer32"""
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
        *(("htuc", 1),
          ("hre1", 2),
          ("hre2", 3),
          ("hre3", 4))
    )


_AdGenTSCANRepeaterIndex_Type.__name__ = "Integer32"
_AdGenTSCANRepeaterIndex_Object = MibTableColumn
adGenTSCANRepeaterIndex = _AdGenTSCANRepeaterIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 45),
    _AdGenTSCANRepeaterIndex_Type()
)
adGenTSCANRepeaterIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTSCANRepeaterIndex.setStatus("current")
_AdGenTSCANECTB1B10_Type = DisplayString
_AdGenTSCANECTB1B10_Object = MibTableColumn
adGenTSCANECTB1B10 = _AdGenTSCANECTB1B10_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 46),
    _AdGenTSCANECTB1B10_Type()
)
adGenTSCANECTB1B10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB1B10.setStatus("current")
_AdGenTSCANECTB1B11_Type = DisplayString
_AdGenTSCANECTB1B11_Object = MibTableColumn
adGenTSCANECTB1B11 = _AdGenTSCANECTB1B11_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 47),
    _AdGenTSCANECTB1B11_Type()
)
adGenTSCANECTB1B11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB1B11.setStatus("current")
_AdGenTSCANECTB1B12_Type = DisplayString
_AdGenTSCANECTB1B12_Object = MibTableColumn
adGenTSCANECTB1B12 = _AdGenTSCANECTB1B12_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 48),
    _AdGenTSCANECTB1B12_Type()
)
adGenTSCANECTB1B12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB1B12.setStatus("current")
_AdGenTSCANECTB2B10_Type = DisplayString
_AdGenTSCANECTB2B10_Object = MibTableColumn
adGenTSCANECTB2B10 = _AdGenTSCANECTB2B10_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 49),
    _AdGenTSCANECTB2B10_Type()
)
adGenTSCANECTB2B10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB2B10.setStatus("current")
_AdGenTSCANECTB2B11_Type = DisplayString
_AdGenTSCANECTB2B11_Object = MibTableColumn
adGenTSCANECTB2B11 = _AdGenTSCANECTB2B11_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 50),
    _AdGenTSCANECTB2B11_Type()
)
adGenTSCANECTB2B11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB2B11.setStatus("current")
_AdGenTSCANECTB2B12_Type = DisplayString
_AdGenTSCANECTB2B12_Object = MibTableColumn
adGenTSCANECTB2B12 = _AdGenTSCANECTB2B12_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 51),
    _AdGenTSCANECTB2B12_Type()
)
adGenTSCANECTB2B12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANECTB2B12.setStatus("current")


class _AdGenTSCANHybridConfig_Type(Integer32):
    """Custom type adGenTSCANHybridConfig based on Integer32"""
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


_AdGenTSCANHybridConfig_Type.__name__ = "Integer32"
_AdGenTSCANHybridConfig_Object = MibTableColumn
adGenTSCANHybridConfig = _AdGenTSCANHybridConfig_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 52),
    _AdGenTSCANHybridConfig_Type()
)
adGenTSCANHybridConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTSCANHybridConfig.setStatus("current")
_AdGenTSCANFullRangeRate_Type = Unsigned32
_AdGenTSCANFullRangeRate_Object = MibTableColumn
adGenTSCANFullRangeRate = _AdGenTSCANFullRangeRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 1, 1, 1, 53),
    _AdGenTSCANFullRangeRate_Type()
)
adGenTSCANFullRangeRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTSCANFullRangeRate.setStatus("current")
_AdGenTSCANMibConformance_ObjectIdentity = ObjectIdentity
adGenTSCANMibConformance = _AdGenTSCANMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 2)
)
_AdGenTSCANMibGroups_ObjectIdentity = ObjectIdentity
adGenTSCANMibGroups = _AdGenTSCANMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 2, 1)
)
_AdGenTSCANRepeater_ObjectIdentity = ObjectIdentity
adGenTSCANRepeater = _AdGenTSCANRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 3)
)
_AdGenTSCANRepeaterTable_Object = MibTable
adGenTSCANRepeaterTable = _AdGenTSCANRepeaterTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 3, 1)
)
if mibBuilder.loadTexts:
    adGenTSCANRepeaterTable.setStatus("current")
_AdGenTSCANRepeaterEntry_Object = MibTableRow
adGenTSCANRepeaterEntry = _AdGenTSCANRepeaterEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 3, 1, 1)
)
adGenTSCANRepeaterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
)
if mibBuilder.loadTexts:
    adGenTSCANRepeaterEntry.setStatus("current")


class _AdGenTSCANRepeaterStart_Type(Integer32):
    """Custom type adGenTSCANRepeaterStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_AdGenTSCANRepeaterStart_Type.__name__ = "Integer32"
_AdGenTSCANRepeaterStart_Object = MibTableColumn
adGenTSCANRepeaterStart = _AdGenTSCANRepeaterStart_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 3, 1, 1, 1),
    _AdGenTSCANRepeaterStart_Type()
)
adGenTSCANRepeaterStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTSCANRepeaterStart.setStatus("current")


class _AdGenTSCANRepeaterStatus_Type(Integer32):
    """Custom type adGenTSCANRepeaterStatus based on Integer32"""
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
        *(("done", 1),
          ("accumulatingData", 2),
          ("idle", 3),
          ("error", 4))
    )


_AdGenTSCANRepeaterStatus_Type.__name__ = "Integer32"
_AdGenTSCANRepeaterStatus_Object = MibTableColumn
adGenTSCANRepeaterStatus = _AdGenTSCANRepeaterStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 3, 1, 1, 2),
    _AdGenTSCANRepeaterStatus_Type()
)
adGenTSCANRepeaterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANRepeaterStatus.setStatus("current")
_AdGenTSCANRepeaterLastTestCompleted_Type = DisplayString
_AdGenTSCANRepeaterLastTestCompleted_Object = MibTableColumn
adGenTSCANRepeaterLastTestCompleted = _AdGenTSCANRepeaterLastTestCompleted_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 3, 1, 1, 3),
    _AdGenTSCANRepeaterLastTestCompleted_Type()
)
adGenTSCANRepeaterLastTestCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANRepeaterLastTestCompleted.setStatus("current")


class _AdGenTSCANRepeaterFault_Type(Integer32):
    """Custom type adGenTSCANRepeaterFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("open", 1),
          ("short", 2),
          ("gfi", 3),
          ("singleOpen", 4),
          ("ok", 5))
    )


_AdGenTSCANRepeaterFault_Type.__name__ = "Integer32"
_AdGenTSCANRepeaterFault_Object = MibTableColumn
adGenTSCANRepeaterFault = _AdGenTSCANRepeaterFault_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 3, 1, 1, 4),
    _AdGenTSCANRepeaterFault_Type()
)
adGenTSCANRepeaterFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANRepeaterFault.setStatus("current")
_AdGenTSCANRepeaterDistanceInFeet_Type = Integer32
_AdGenTSCANRepeaterDistanceInFeet_Object = MibTableColumn
adGenTSCANRepeaterDistanceInFeet = _AdGenTSCANRepeaterDistanceInFeet_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 3, 1, 1, 5),
    _AdGenTSCANRepeaterDistanceInFeet_Type()
)
adGenTSCANRepeaterDistanceInFeet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANRepeaterDistanceInFeet.setStatus("current")
_AdGenTSCANRepeaterDistanceInMeters_Type = Integer32
_AdGenTSCANRepeaterDistanceInMeters_Object = MibTableColumn
adGenTSCANRepeaterDistanceInMeters = _AdGenTSCANRepeaterDistanceInMeters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 3, 1, 1, 6),
    _AdGenTSCANRepeaterDistanceInMeters_Type()
)
adGenTSCANRepeaterDistanceInMeters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANRepeaterDistanceInMeters.setStatus("current")
_AdGenTSCANRepeaterRate_Type = Integer32
_AdGenTSCANRepeaterRate_Object = MibTableColumn
adGenTSCANRepeaterRate = _AdGenTSCANRepeaterRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 3, 1, 1, 7),
    _AdGenTSCANRepeaterRate_Type()
)
adGenTSCANRepeaterRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTSCANRepeaterRate.setStatus("current")
_AdGenTSCANRepeaterPortTable_Object = MibTable
adGenTSCANRepeaterPortTable = _AdGenTSCANRepeaterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 3, 2)
)
if mibBuilder.loadTexts:
    adGenTSCANRepeaterPortTable.setStatus("current")
_AdGenTSCANRepeaterPortEntry_Object = MibTableRow
adGenTSCANRepeaterPortEntry = _AdGenTSCANRepeaterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 3, 2, 1)
)
adGenTSCANRepeaterPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTSCANRepeaterPortEntry.setStatus("current")
_AdGenTSCANRepeaterPortLastErrorString_Type = DisplayString
_AdGenTSCANRepeaterPortLastErrorString_Object = MibTableColumn
adGenTSCANRepeaterPortLastErrorString = _AdGenTSCANRepeaterPortLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 3, 2, 1, 1),
    _AdGenTSCANRepeaterPortLastErrorString_Type()
)
adGenTSCANRepeaterPortLastErrorString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTSCANRepeaterPortLastErrorString.setStatus("current")

# Managed Objects groups

adGenTSCANGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 51, 1, 2, 1, 1)
)
adGenTSCANGroup.setObjects(
      *(("ADTRAN-GENTSCAN-MIB", "adGenTSCANAccumTscanData"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANTscanDataStatus"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTG1B1"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTG1B2"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTG1B3"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTG1B4"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTG1B5"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTG1B6"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTG1B7"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTG1B8"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTG1B9"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTG2B1"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTG2B2"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTG2B3"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTG2B4"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTG2B5"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTG2B6"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTG2B7"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTG2B8"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTG2B9"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB1B1"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB1B2"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB1B3"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB1B4"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB1B5"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB1B6"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB1B7"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB1B8"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB1B9"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB2B1"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB2B2"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB2B3"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB2B4"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB2B5"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB2B6"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB2B7"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB2B8"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB2B9"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANST1B"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANST2B"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANLS1"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANLS2"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANRate"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANLastTime"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANRepeaterIndex"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB1B10"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB1B11"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB1B12"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB2B10"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB2B11"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANECTB2B12"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANHybridConfig"),
        ("ADTRAN-GENTSCAN-MIB", "adGenTSCANFullRangeRate"))
)
if mibBuilder.loadTexts:
    adGenTSCANGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENTSCAN-MIB",
    **{"adGenTSCANmg": adGenTSCANmg,
       "adGenTSCANProv": adGenTSCANProv,
       "adGenTSCANProvTable": adGenTSCANProvTable,
       "adGenTSCANProvEntry": adGenTSCANProvEntry,
       "adGenTSCANAccumTscanData": adGenTSCANAccumTscanData,
       "adGenTSCANTscanDataStatus": adGenTSCANTscanDataStatus,
       "adGenTSCANECTG1B1": adGenTSCANECTG1B1,
       "adGenTSCANECTG1B2": adGenTSCANECTG1B2,
       "adGenTSCANECTG1B3": adGenTSCANECTG1B3,
       "adGenTSCANECTG1B4": adGenTSCANECTG1B4,
       "adGenTSCANECTG1B5": adGenTSCANECTG1B5,
       "adGenTSCANECTG1B6": adGenTSCANECTG1B6,
       "adGenTSCANECTG1B7": adGenTSCANECTG1B7,
       "adGenTSCANECTG1B8": adGenTSCANECTG1B8,
       "adGenTSCANECTG1B9": adGenTSCANECTG1B9,
       "adGenTSCANECTG2B1": adGenTSCANECTG2B1,
       "adGenTSCANECTG2B2": adGenTSCANECTG2B2,
       "adGenTSCANECTG2B3": adGenTSCANECTG2B3,
       "adGenTSCANECTG2B4": adGenTSCANECTG2B4,
       "adGenTSCANECTG2B5": adGenTSCANECTG2B5,
       "adGenTSCANECTG2B6": adGenTSCANECTG2B6,
       "adGenTSCANECTG2B7": adGenTSCANECTG2B7,
       "adGenTSCANECTG2B8": adGenTSCANECTG2B8,
       "adGenTSCANECTG2B9": adGenTSCANECTG2B9,
       "adGenTSCANECTB1B1": adGenTSCANECTB1B1,
       "adGenTSCANECTB1B2": adGenTSCANECTB1B2,
       "adGenTSCANECTB1B3": adGenTSCANECTB1B3,
       "adGenTSCANECTB1B4": adGenTSCANECTB1B4,
       "adGenTSCANECTB1B5": adGenTSCANECTB1B5,
       "adGenTSCANECTB1B6": adGenTSCANECTB1B6,
       "adGenTSCANECTB1B7": adGenTSCANECTB1B7,
       "adGenTSCANECTB1B8": adGenTSCANECTB1B8,
       "adGenTSCANECTB1B9": adGenTSCANECTB1B9,
       "adGenTSCANECTB2B1": adGenTSCANECTB2B1,
       "adGenTSCANECTB2B2": adGenTSCANECTB2B2,
       "adGenTSCANECTB2B3": adGenTSCANECTB2B3,
       "adGenTSCANECTB2B4": adGenTSCANECTB2B4,
       "adGenTSCANECTB2B5": adGenTSCANECTB2B5,
       "adGenTSCANECTB2B6": adGenTSCANECTB2B6,
       "adGenTSCANECTB2B7": adGenTSCANECTB2B7,
       "adGenTSCANECTB2B8": adGenTSCANECTB2B8,
       "adGenTSCANECTB2B9": adGenTSCANECTB2B9,
       "adGenTSCANST1B": adGenTSCANST1B,
       "adGenTSCANST2B": adGenTSCANST2B,
       "adGenTSCANLS1": adGenTSCANLS1,
       "adGenTSCANLS2": adGenTSCANLS2,
       "adGenTSCANRate": adGenTSCANRate,
       "adGenTSCANLastTime": adGenTSCANLastTime,
       "adGenTSCANRepeaterIndex": adGenTSCANRepeaterIndex,
       "adGenTSCANECTB1B10": adGenTSCANECTB1B10,
       "adGenTSCANECTB1B11": adGenTSCANECTB1B11,
       "adGenTSCANECTB1B12": adGenTSCANECTB1B12,
       "adGenTSCANECTB2B10": adGenTSCANECTB2B10,
       "adGenTSCANECTB2B11": adGenTSCANECTB2B11,
       "adGenTSCANECTB2B12": adGenTSCANECTB2B12,
       "adGenTSCANHybridConfig": adGenTSCANHybridConfig,
       "adGenTSCANFullRangeRate": adGenTSCANFullRangeRate,
       "adGenTSCANMibConformance": adGenTSCANMibConformance,
       "adGenTSCANMibGroups": adGenTSCANMibGroups,
       "adGenTSCANGroup": adGenTSCANGroup,
       "adGenTSCANRepeater": adGenTSCANRepeater,
       "adGenTSCANRepeaterTable": adGenTSCANRepeaterTable,
       "adGenTSCANRepeaterEntry": adGenTSCANRepeaterEntry,
       "adGenTSCANRepeaterStart": adGenTSCANRepeaterStart,
       "adGenTSCANRepeaterStatus": adGenTSCANRepeaterStatus,
       "adGenTSCANRepeaterLastTestCompleted": adGenTSCANRepeaterLastTestCompleted,
       "adGenTSCANRepeaterFault": adGenTSCANRepeaterFault,
       "adGenTSCANRepeaterDistanceInFeet": adGenTSCANRepeaterDistanceInFeet,
       "adGenTSCANRepeaterDistanceInMeters": adGenTSCANRepeaterDistanceInMeters,
       "adGenTSCANRepeaterRate": adGenTSCANRepeaterRate,
       "adGenTSCANRepeaterPortTable": adGenTSCANRepeaterPortTable,
       "adGenTSCANRepeaterPortEntry": adGenTSCANRepeaterPortEntry,
       "adGenTSCANRepeaterPortLastErrorString": adGenTSCANRepeaterPortLastErrorString,
       "adGenTSCANMIB": adGenTSCANMIB}
)
