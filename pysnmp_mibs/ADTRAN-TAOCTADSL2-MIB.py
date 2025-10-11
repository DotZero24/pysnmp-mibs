# SNMP MIB module (ADTRAN-TAOCTADSL2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TAOCTADSL2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:56 2025
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

(adslLineConfProfileName,) = mibBuilder.importSymbols(
    "ADSL-LINE-MIB",
    "adslLineConfProfileName")

(adIdentity,
 adMgmt,
 adProducts) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity",
    "adMgmt",
    "adProducts")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

adTAOctAdslID = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 432)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTAOctAdsl_ObjectIdentity = ObjectIdentity
adTAOctAdsl = _AdTAOctAdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1, 432)
)
_AdTAOctAdslalarms_ObjectIdentity = ObjectIdentity
adTAOctAdslalarms = _AdTAOctAdslalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1, 432, 101)
)
_AdTAOctAdslwPOTS_ObjectIdentity = ObjectIdentity
adTAOctAdslwPOTS = _AdTAOctAdslwPOTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1, 455)
)
_AdTA5k32pADSL2_ObjectIdentity = ObjectIdentity
adTA5k32pADSL2 = _AdTA5k32pADSL2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1, 752)
)
_AdTA5k24pPOTSADSL2_ObjectIdentity = ObjectIdentity
adTA5k24pPOTSADSL2 = _AdTA5k24pPOTSADSL2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1, 858)
)
_AdTA5k32pADSL2int_ObjectIdentity = ObjectIdentity
adTA5k32pADSL2int = _AdTA5k32pADSL2int_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1, 1043)
)
_AdTAOctAdslmg_ObjectIdentity = ObjectIdentity
adTAOctAdslmg = _AdTAOctAdslmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 432)
)
_AdTAOctAdslProv_ObjectIdentity = ObjectIdentity
adTAOctAdslProv = _AdTAOctAdslProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 1)
)
_AdTAOctAdslProv2_ObjectIdentity = ObjectIdentity
adTAOctAdslProv2 = _AdTAOctAdslProv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 2)
)
_AdTAOctAdslConfProfileExtTable_Object = MibTable
adTAOctAdslConfProfileExtTable = _AdTAOctAdslConfProfileExtTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 2, 1)
)
if mibBuilder.loadTexts:
    adTAOctAdslConfProfileExtTable.setStatus("current")
_AdTAOctAdslConfProfileExtEntry_Object = MibTableRow
adTAOctAdslConfProfileExtEntry = _AdTAOctAdslConfProfileExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 2, 1, 1)
)
adTAOctAdslConfProfileExtEntry.setIndexNames(
    (1, "ADSL-LINE-MIB", "adslLineConfProfileName"),
)
if mibBuilder.loadTexts:
    adTAOctAdslConfProfileExtEntry.setStatus("current")


class _AdTAOctAdslConfProfileLineType_Type(Integer32):
    """Custom type adTAOctAdslConfProfileLineType based on Integer32"""
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
        *(("noChannel", 1),
          ("fastOnly", 2),
          ("interleavedOnly", 3),
          ("fastOrInterleaved", 4),
          ("fastAndInterleaved", 5))
    )


_AdTAOctAdslConfProfileLineType_Type.__name__ = "Integer32"
_AdTAOctAdslConfProfileLineType_Object = MibTableColumn
adTAOctAdslConfProfileLineType = _AdTAOctAdslConfProfileLineType_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 2, 1, 1, 1),
    _AdTAOctAdslConfProfileLineType_Type()
)
adTAOctAdslConfProfileLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAOctAdslConfProfileLineType.setStatus("current")


class _AdTAOctAdslConfProfileServiceMode_Type(Integer32):
    """Custom type adTAOctAdslConfProfileServiceMode based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("multiMode", 1),
          ("t1413", 2),
          ("gDMT", 3),
          ("gLite", 4),
          ("g9923", 5),
          ("g9924", 6),
          ("g9925", 7),
          ("readsl", 8),
          ("adsl1MultiMode", 9),
          ("g9925AnxM", 10))
    )


_AdTAOctAdslConfProfileServiceMode_Type.__name__ = "Integer32"
_AdTAOctAdslConfProfileServiceMode_Object = MibTableColumn
adTAOctAdslConfProfileServiceMode = _AdTAOctAdslConfProfileServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 2, 1, 1, 2),
    _AdTAOctAdslConfProfileServiceMode_Type()
)
adTAOctAdslConfProfileServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAOctAdslConfProfileServiceMode.setStatus("current")


class _AdTAOctAdslConfProfileIndexApplied_Type(Integer32):
    """Custom type adTAOctAdslConfProfileIndexApplied based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdTAOctAdslConfProfileIndexApplied_Type.__name__ = "Integer32"
_AdTAOctAdslConfProfileIndexApplied_Object = MibTableColumn
adTAOctAdslConfProfileIndexApplied = _AdTAOctAdslConfProfileIndexApplied_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 2, 1, 1, 3),
    _AdTAOctAdslConfProfileIndexApplied_Type()
)
adTAOctAdslConfProfileIndexApplied.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAOctAdslConfProfileIndexApplied.setStatus("current")


class _AdTAOctAdslConfProfileName_Type(SnmpAdminString):
    """Custom type adTAOctAdslConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdTAOctAdslConfProfileName_Type.__name__ = "SnmpAdminString"
_AdTAOctAdslConfProfileName_Object = MibTableColumn
adTAOctAdslConfProfileName = _AdTAOctAdslConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 2, 1, 1, 4),
    _AdTAOctAdslConfProfileName_Type()
)
adTAOctAdslConfProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAOctAdslConfProfileName.setStatus("current")


class _AdTAOctAdslAtucConfProfileInterleaveMinINP_Type(Integer32):
    """Custom type adTAOctAdslAtucConfProfileInterleaveMinINP based on Integer32"""
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
        *(("zeroDMTSymbols", 1),
          ("halfDMTSymbols", 2),
          ("oneDMTSymbols", 3),
          ("twoDMTSymbols", 4))
    )


_AdTAOctAdslAtucConfProfileInterleaveMinINP_Type.__name__ = "Integer32"
_AdTAOctAdslAtucConfProfileInterleaveMinINP_Object = MibTableColumn
adTAOctAdslAtucConfProfileInterleaveMinINP = _AdTAOctAdslAtucConfProfileInterleaveMinINP_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 2, 1, 1, 5),
    _AdTAOctAdslAtucConfProfileInterleaveMinINP_Type()
)
adTAOctAdslAtucConfProfileInterleaveMinINP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAOctAdslAtucConfProfileInterleaveMinINP.setStatus("obsolete")


class _AdTAOctAdslAturConfProfileInterleaveMinINP_Type(Integer32):
    """Custom type adTAOctAdslAturConfProfileInterleaveMinINP based on Integer32"""
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
        *(("zeroDMTSymbols", 1),
          ("halfDMTSymbols", 2),
          ("oneDMTSymbols", 3),
          ("twoDMTSymbols", 4))
    )


_AdTAOctAdslAturConfProfileInterleaveMinINP_Type.__name__ = "Integer32"
_AdTAOctAdslAturConfProfileInterleaveMinINP_Object = MibTableColumn
adTAOctAdslAturConfProfileInterleaveMinINP = _AdTAOctAdslAturConfProfileInterleaveMinINP_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 2, 1, 1, 6),
    _AdTAOctAdslAturConfProfileInterleaveMinINP_Type()
)
adTAOctAdslAturConfProfileInterleaveMinINP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslAturConfProfileInterleaveMinINP.setStatus("obsolete")
if mibBuilder.loadTexts:
    adTAOctAdslAturConfProfileInterleaveMinINP.setUnits("0.5 DMT symbols")


class _AdTAOctAdslAtucConfProfileInterleaveMinInpRev2_Type(Integer32):
    """Custom type adTAOctAdslAtucConfProfileInterleaveMinInpRev2 based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("zeroDMTSymbols", 1),
          ("halfDMTSymbols", 2),
          ("oneDMTSymbols", 3),
          ("twoDMTSymbols", 4),
          ("threeDMTSymbols", 5),
          ("fourDMTSymbols", 6),
          ("fiveDMTSymbols", 7),
          ("sixDMTSymbols", 8),
          ("sevenDMTSymbols", 9),
          ("eightDMTSymbols", 10),
          ("nineDMTSymbols", 11),
          ("tenDMTSymbols", 12),
          ("elevenDMTSymbols", 13),
          ("twelveDMTSymbols", 14),
          ("thirteenDMTSymbols", 15),
          ("fourteenDMTSymbols", 16),
          ("fifteenDMTSymbols", 17),
          ("sixteenDMTSymbols", 18))
    )


_AdTAOctAdslAtucConfProfileInterleaveMinInpRev2_Type.__name__ = "Integer32"
_AdTAOctAdslAtucConfProfileInterleaveMinInpRev2_Object = MibTableColumn
adTAOctAdslAtucConfProfileInterleaveMinInpRev2 = _AdTAOctAdslAtucConfProfileInterleaveMinInpRev2_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 2, 1, 1, 7),
    _AdTAOctAdslAtucConfProfileInterleaveMinInpRev2_Type()
)
adTAOctAdslAtucConfProfileInterleaveMinInpRev2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAOctAdslAtucConfProfileInterleaveMinInpRev2.setStatus("current")


class _AdTAOctAdslAturConfProfileInterleaveMinInpRev2_Type(Integer32):
    """Custom type adTAOctAdslAturConfProfileInterleaveMinInpRev2 based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("zeroDMTSymbols", 1),
          ("halfDMTSymbols", 2),
          ("oneDMTSymbols", 3),
          ("twoDMTSymbols", 4),
          ("threeDMTSymbols", 5),
          ("fourDMTSymbols", 6),
          ("fiveDMTSymbols", 7),
          ("sixDMTSymbols", 8),
          ("sevenDMTSymbols", 9),
          ("eightDMTSymbols", 10),
          ("nineDMTSymbols", 11),
          ("tenDMTSymbols", 12),
          ("elevenDMTSymbols", 13),
          ("twelveDMTSymbols", 14),
          ("thirteenDMTSymbols", 15),
          ("fourteenDMTSymbols", 16),
          ("fifteenDMTSymbols", 17),
          ("sixteenDMTSymbols", 18))
    )


_AdTAOctAdslAturConfProfileInterleaveMinInpRev2_Type.__name__ = "Integer32"
_AdTAOctAdslAturConfProfileInterleaveMinInpRev2_Object = MibTableColumn
adTAOctAdslAturConfProfileInterleaveMinInpRev2 = _AdTAOctAdslAturConfProfileInterleaveMinInpRev2_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 2, 1, 1, 8),
    _AdTAOctAdslAturConfProfileInterleaveMinInpRev2_Type()
)
adTAOctAdslAturConfProfileInterleaveMinInpRev2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAOctAdslAturConfProfileInterleaveMinInpRev2.setStatus("current")
_AdTAOctAdslConfLineTable_Object = MibTable
adTAOctAdslConfLineTable = _AdTAOctAdslConfLineTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 2, 2)
)
if mibBuilder.loadTexts:
    adTAOctAdslConfLineTable.setStatus("current")
_AdTAOctAdslConfLineEntry_Object = MibTableRow
adTAOctAdslConfLineEntry = _AdTAOctAdslConfLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 2, 2, 1)
)
adTAOctAdslConfLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTAOctAdslConfLineEntry.setStatus("current")


class _AdTAOctAdslHamBandMask_Type(Integer32):
    """Custom type adTAOctAdslHamBandMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdTAOctAdslHamBandMask_Type.__name__ = "Integer32"
_AdTAOctAdslHamBandMask_Object = MibTableColumn
adTAOctAdslHamBandMask = _AdTAOctAdslHamBandMask_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 2, 2, 1, 1),
    _AdTAOctAdslHamBandMask_Type()
)
adTAOctAdslHamBandMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAOctAdslHamBandMask.setStatus("current")


class _AdTAOctAdslCabinetMode_Type(Integer32):
    """Custom type adTAOctAdslCabinetMode based on Integer32"""
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
        *(("disable", 1),
          ("enableTone110", 2),
          ("enableTone130", 3),
          ("enableTone250", 4))
    )


_AdTAOctAdslCabinetMode_Type.__name__ = "Integer32"
_AdTAOctAdslCabinetMode_Object = MibTableColumn
adTAOctAdslCabinetMode = _AdTAOctAdslCabinetMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 2, 2, 1, 2),
    _AdTAOctAdslCabinetMode_Type()
)
adTAOctAdslCabinetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAOctAdslCabinetMode.setStatus("current")


class _AdTAOctAdslPowerThreshold_Type(Integer32):
    """Custom type adTAOctAdslPowerThreshold based on Integer32"""
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
        *(("disable", 1),
          ("dBm10", 2),
          ("dBm12", 3),
          ("dBm14", 4))
    )


_AdTAOctAdslPowerThreshold_Type.__name__ = "Integer32"
_AdTAOctAdslPowerThreshold_Object = MibTableColumn
adTAOctAdslPowerThreshold = _AdTAOctAdslPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 2, 2, 1, 3),
    _AdTAOctAdslPowerThreshold_Type()
)
adTAOctAdslPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAOctAdslPowerThreshold.setStatus("current")
_AdTAOctAdslAtucCarrierMask_Type = OctetString
_AdTAOctAdslAtucCarrierMask_Object = MibTableColumn
adTAOctAdslAtucCarrierMask = _AdTAOctAdslAtucCarrierMask_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 2, 2, 1, 4),
    _AdTAOctAdslAtucCarrierMask_Type()
)
adTAOctAdslAtucCarrierMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAOctAdslAtucCarrierMask.setStatus("current")
_AdTAOctAdslAturCarrierMask_Type = OctetString
_AdTAOctAdslAturCarrierMask_Object = MibTableColumn
adTAOctAdslAturCarrierMask = _AdTAOctAdslAturCarrierMask_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 2, 2, 1, 5),
    _AdTAOctAdslAturCarrierMask_Type()
)
adTAOctAdslAturCarrierMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAOctAdslAturCarrierMask.setStatus("current")
_AdTAOctAdslStatus2_ObjectIdentity = ObjectIdentity
adTAOctAdslStatus2 = _AdTAOctAdslStatus2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4)
)
_AdTAOctAdslLineTable_Object = MibTable
adTAOctAdslLineTable = _AdTAOctAdslLineTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 1)
)
if mibBuilder.loadTexts:
    adTAOctAdslLineTable.setStatus("current")
_AdTAOctAdslLineEntry_Object = MibTableRow
adTAOctAdslLineEntry = _AdTAOctAdslLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 1, 1)
)
adTAOctAdslLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTAOctAdslLineEntry.setStatus("current")


class _AdTAOctAdslCurrLinkStatus_Type(Integer32):
    """Custom type adTAOctAdslCurrLinkStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("training", 4))
    )


_AdTAOctAdslCurrLinkStatus_Type.__name__ = "Integer32"
_AdTAOctAdslCurrLinkStatus_Object = MibTableColumn
adTAOctAdslCurrLinkStatus = _AdTAOctAdslCurrLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 1, 1, 1),
    _AdTAOctAdslCurrLinkStatus_Type()
)
adTAOctAdslCurrLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslCurrLinkStatus.setStatus("current")


class _AdTAOctAdslCurrStandard_Type(Integer32):
    """Custom type adTAOctAdslCurrStandard based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 1),
          ("t1413", 2),
          ("gDMT", 3),
          ("gLite", 4),
          ("g9923", 5),
          ("g9924", 6),
          ("g9925", 7),
          ("readsl", 8),
          ("adsl1MultiMode", 9),
          ("g9925AnxM", 10))
    )


_AdTAOctAdslCurrStandard_Type.__name__ = "Integer32"
_AdTAOctAdslCurrStandard_Object = MibTableColumn
adTAOctAdslCurrStandard = _AdTAOctAdslCurrStandard_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 1, 1, 2),
    _AdTAOctAdslCurrStandard_Type()
)
adTAOctAdslCurrStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslCurrStandard.setStatus("current")


class _AdTAOctAdslBitAllocationMap_Type(OctetString):
    """Custom type adTAOctAdslBitAllocationMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_AdTAOctAdslBitAllocationMap_Type.__name__ = "OctetString"
_AdTAOctAdslBitAllocationMap_Object = MibTableColumn
adTAOctAdslBitAllocationMap = _AdTAOctAdslBitAllocationMap_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 1, 1, 3),
    _AdTAOctAdslBitAllocationMap_Type()
)
adTAOctAdslBitAllocationMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslBitAllocationMap.setStatus("current")


class _AdTAOctAdslBitAllocationMapGroup2_Type(OctetString):
    """Custom type adTAOctAdslBitAllocationMapGroup2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_AdTAOctAdslBitAllocationMapGroup2_Type.__name__ = "OctetString"
_AdTAOctAdslBitAllocationMapGroup2_Object = MibTableColumn
adTAOctAdslBitAllocationMapGroup2 = _AdTAOctAdslBitAllocationMapGroup2_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 1, 1, 4),
    _AdTAOctAdslBitAllocationMapGroup2_Type()
)
adTAOctAdslBitAllocationMapGroup2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslBitAllocationMapGroup2.setStatus("current")


class _AdTAOctAdslUsSnrMarginMap_Type(OctetString):
    """Custom type adTAOctAdslUsSnrMarginMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_AdTAOctAdslUsSnrMarginMap_Type.__name__ = "OctetString"
_AdTAOctAdslUsSnrMarginMap_Object = MibTableColumn
adTAOctAdslUsSnrMarginMap = _AdTAOctAdslUsSnrMarginMap_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 1, 1, 5),
    _AdTAOctAdslUsSnrMarginMap_Type()
)
adTAOctAdslUsSnrMarginMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslUsSnrMarginMap.setStatus("current")
if mibBuilder.loadTexts:
    adTAOctAdslUsSnrMarginMap.setUnits("0.1 dB")
_AdTAOctAdslAtucPhysTable_Object = MibTable
adTAOctAdslAtucPhysTable = _AdTAOctAdslAtucPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 2)
)
if mibBuilder.loadTexts:
    adTAOctAdslAtucPhysTable.setStatus("current")
_AdTAOctAdslAtucPhysEntry_Object = MibTableRow
adTAOctAdslAtucPhysEntry = _AdTAOctAdslAtucPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 2, 1)
)
adTAOctAdslAtucPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTAOctAdslAtucPhysEntry.setStatus("current")
_AdTAOctAdslAtucNumParityBytes_Type = Integer32
_AdTAOctAdslAtucNumParityBytes_Object = MibTableColumn
adTAOctAdslAtucNumParityBytes = _AdTAOctAdslAtucNumParityBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 2, 1, 2),
    _AdTAOctAdslAtucNumParityBytes_Type()
)
adTAOctAdslAtucNumParityBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslAtucNumParityBytes.setStatus("current")
_AdTAOctAdslAtucFramesPerCodeword_Type = Integer32
_AdTAOctAdslAtucFramesPerCodeword_Object = MibTableColumn
adTAOctAdslAtucFramesPerCodeword = _AdTAOctAdslAtucFramesPerCodeword_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 2, 1, 3),
    _AdTAOctAdslAtucFramesPerCodeword_Type()
)
adTAOctAdslAtucFramesPerCodeword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslAtucFramesPerCodeword.setStatus("current")
_AdTAOctAdslAtucInterleavingDepth_Type = Integer32
_AdTAOctAdslAtucInterleavingDepth_Object = MibTableColumn
adTAOctAdslAtucInterleavingDepth = _AdTAOctAdslAtucInterleavingDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 2, 1, 4),
    _AdTAOctAdslAtucInterleavingDepth_Type()
)
adTAOctAdslAtucInterleavingDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslAtucInterleavingDepth.setStatus("current")
_AdTAOctAdslAturPhysTable_Object = MibTable
adTAOctAdslAturPhysTable = _AdTAOctAdslAturPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 3)
)
if mibBuilder.loadTexts:
    adTAOctAdslAturPhysTable.setStatus("current")
_AdTAOctAdslAturPhysEntry_Object = MibTableRow
adTAOctAdslAturPhysEntry = _AdTAOctAdslAturPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 3, 1)
)
adTAOctAdslAturPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTAOctAdslAturPhysEntry.setStatus("current")
_AdTAOctAdslAturNumParityBytes_Type = Integer32
_AdTAOctAdslAturNumParityBytes_Object = MibTableColumn
adTAOctAdslAturNumParityBytes = _AdTAOctAdslAturNumParityBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 3, 1, 2),
    _AdTAOctAdslAturNumParityBytes_Type()
)
adTAOctAdslAturNumParityBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslAturNumParityBytes.setStatus("current")
_AdTAOctAdslAturFramesPerCodeword_Type = Integer32
_AdTAOctAdslAturFramesPerCodeword_Object = MibTableColumn
adTAOctAdslAturFramesPerCodeword = _AdTAOctAdslAturFramesPerCodeword_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 3, 1, 3),
    _AdTAOctAdslAturFramesPerCodeword_Type()
)
adTAOctAdslAturFramesPerCodeword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslAturFramesPerCodeword.setStatus("current")
_AdTAOctAdslAturInterleavingDepth_Type = Integer32
_AdTAOctAdslAturInterleavingDepth_Object = MibTableColumn
adTAOctAdslAturInterleavingDepth = _AdTAOctAdslAturInterleavingDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 3, 1, 4),
    _AdTAOctAdslAturInterleavingDepth_Type()
)
adTAOctAdslAturInterleavingDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslAturInterleavingDepth.setStatus("current")


class _AdTAOctAdslAturCapabilities_Type(Integer32):
    """Custom type adTAOctAdslAturCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048575),
    )


_AdTAOctAdslAturCapabilities_Type.__name__ = "Integer32"
_AdTAOctAdslAturCapabilities_Object = MibTableColumn
adTAOctAdslAturCapabilities = _AdTAOctAdslAturCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 3, 1, 5),
    _AdTAOctAdslAturCapabilities_Type()
)
adTAOctAdslAturCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslAturCapabilities.setStatus("current")
_AdTAOctAdslAturInvProviderCode_Type = SnmpAdminString
_AdTAOctAdslAturInvProviderCode_Object = MibTableColumn
adTAOctAdslAturInvProviderCode = _AdTAOctAdslAturInvProviderCode_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 3, 1, 6),
    _AdTAOctAdslAturInvProviderCode_Type()
)
adTAOctAdslAturInvProviderCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslAturInvProviderCode.setStatus("current")
_AdTAOctAdslAtucChanTable_Object = MibTable
adTAOctAdslAtucChanTable = _AdTAOctAdslAtucChanTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 4)
)
if mibBuilder.loadTexts:
    adTAOctAdslAtucChanTable.setStatus("current")
_AdTAOctAdslAtucChanEntry_Object = MibTableRow
adTAOctAdslAtucChanEntry = _AdTAOctAdslAtucChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 4, 1)
)
adTAOctAdslAtucChanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTAOctAdslAtucChanEntry.setStatus("current")
_AdTAOctAdslAtucChanINP_Type = Gauge32
_AdTAOctAdslAtucChanINP_Object = MibTableColumn
adTAOctAdslAtucChanINP = _AdTAOctAdslAtucChanINP_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 4, 1, 1),
    _AdTAOctAdslAtucChanINP_Type()
)
adTAOctAdslAtucChanINP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslAtucChanINP.setStatus("current")
if mibBuilder.loadTexts:
    adTAOctAdslAtucChanINP.setUnits("0.01 dmt symbols")
_AdTAOctAdslAtucRelativeCap_Type = Gauge32
_AdTAOctAdslAtucRelativeCap_Object = MibTableColumn
adTAOctAdslAtucRelativeCap = _AdTAOctAdslAtucRelativeCap_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 4, 1, 2),
    _AdTAOctAdslAtucRelativeCap_Type()
)
adTAOctAdslAtucRelativeCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslAtucRelativeCap.setStatus("current")
if mibBuilder.loadTexts:
    adTAOctAdslAtucRelativeCap.setUnits("0.1 percent")
_AdTAOctAdslAturChanTable_Object = MibTable
adTAOctAdslAturChanTable = _AdTAOctAdslAturChanTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 5)
)
if mibBuilder.loadTexts:
    adTAOctAdslAturChanTable.setStatus("current")
_AdTAOctAdslAturChanEntry_Object = MibTableRow
adTAOctAdslAturChanEntry = _AdTAOctAdslAturChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 5, 1)
)
adTAOctAdslAturChanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTAOctAdslAturChanEntry.setStatus("current")
_AdTAOctAdslAturChanINP_Type = Gauge32
_AdTAOctAdslAturChanINP_Object = MibTableColumn
adTAOctAdslAturChanINP = _AdTAOctAdslAturChanINP_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 5, 1, 1),
    _AdTAOctAdslAturChanINP_Type()
)
adTAOctAdslAturChanINP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslAturChanINP.setStatus("current")
if mibBuilder.loadTexts:
    adTAOctAdslAturChanINP.setUnits("0.01 dmt symbols")
_AdTAOctAdslAturRelativeCap_Type = Gauge32
_AdTAOctAdslAturRelativeCap_Object = MibTableColumn
adTAOctAdslAturRelativeCap = _AdTAOctAdslAturRelativeCap_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 5, 1, 2),
    _AdTAOctAdslAturRelativeCap_Type()
)
adTAOctAdslAturRelativeCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslAturRelativeCap.setStatus("current")
if mibBuilder.loadTexts:
    adTAOctAdslAturRelativeCap.setUnits("0.1 percent")
_AdTAOctAdslAtmAtucCellCountTable_Object = MibTable
adTAOctAdslAtmAtucCellCountTable = _AdTAOctAdslAtmAtucCellCountTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 6)
)
if mibBuilder.loadTexts:
    adTAOctAdslAtmAtucCellCountTable.setStatus("current")
_AdTAOctAdslAtmAtucCellCountEntry_Object = MibTableRow
adTAOctAdslAtmAtucCellCountEntry = _AdTAOctAdslAtmAtucCellCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 6, 1)
)
adTAOctAdslAtmAtucCellCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTAOctAdslAtmAtucCellCountEntry.setStatus("current")
_AdTAOctAdslAtmAtucCellCount_Type = Unsigned32
_AdTAOctAdslAtmAtucCellCount_Object = MibTableColumn
adTAOctAdslAtmAtucCellCount = _AdTAOctAdslAtmAtucCellCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 6, 1, 1),
    _AdTAOctAdslAtmAtucCellCount_Type()
)
adTAOctAdslAtmAtucCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslAtmAtucCellCount.setStatus("current")
_AdTAOctAdslAtmAtucIdleCellCount_Type = Unsigned32
_AdTAOctAdslAtmAtucIdleCellCount_Object = MibTableColumn
adTAOctAdslAtmAtucIdleCellCount = _AdTAOctAdslAtmAtucIdleCellCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 6, 1, 2),
    _AdTAOctAdslAtmAtucIdleCellCount_Type()
)
adTAOctAdslAtmAtucIdleCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslAtmAtucIdleCellCount.setStatus("current")
_AdTAOctAdslAtmAtucHecErrorCount_Type = Unsigned32
_AdTAOctAdslAtmAtucHecErrorCount_Object = MibTableColumn
adTAOctAdslAtmAtucHecErrorCount = _AdTAOctAdslAtmAtucHecErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 6, 1, 3),
    _AdTAOctAdslAtmAtucHecErrorCount_Type()
)
adTAOctAdslAtmAtucHecErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslAtmAtucHecErrorCount.setStatus("current")
_AdTAOctAdslAtmAturCellCountTable_Object = MibTable
adTAOctAdslAtmAturCellCountTable = _AdTAOctAdslAtmAturCellCountTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 7)
)
if mibBuilder.loadTexts:
    adTAOctAdslAtmAturCellCountTable.setStatus("current")
_AdTAOctAdslAtmAturCellCountEntry_Object = MibTableRow
adTAOctAdslAtmAturCellCountEntry = _AdTAOctAdslAtmAturCellCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 7, 1)
)
adTAOctAdslAtmAturCellCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTAOctAdslAtmAturCellCountEntry.setStatus("current")
_AdTAOctAdslAtmAturCellCount_Type = Unsigned32
_AdTAOctAdslAtmAturCellCount_Object = MibTableColumn
adTAOctAdslAtmAturCellCount = _AdTAOctAdslAtmAturCellCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 7, 1, 1),
    _AdTAOctAdslAtmAturCellCount_Type()
)
adTAOctAdslAtmAturCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslAtmAturCellCount.setStatus("current")
_AdTAOctAdslAtmAturIdleCellCount_Type = Unsigned32
_AdTAOctAdslAtmAturIdleCellCount_Object = MibTableColumn
adTAOctAdslAtmAturIdleCellCount = _AdTAOctAdslAtmAturIdleCellCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 432, 4, 7, 1, 2),
    _AdTAOctAdslAtmAturIdleCellCount_Type()
)
adTAOctAdslAtmAturIdleCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTAOctAdslAtmAturIdleCellCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TAOCTADSL2-MIB",
    **{"adTAOctAdsl": adTAOctAdsl,
       "adTAOctAdslalarms": adTAOctAdslalarms,
       "adTAOctAdslwPOTS": adTAOctAdslwPOTS,
       "adTA5k32pADSL2": adTA5k32pADSL2,
       "adTA5k24pPOTSADSL2": adTA5k24pPOTSADSL2,
       "adTA5k32pADSL2int": adTA5k32pADSL2int,
       "adTAOctAdslmg": adTAOctAdslmg,
       "adTAOctAdslProv": adTAOctAdslProv,
       "adTAOctAdslProv2": adTAOctAdslProv2,
       "adTAOctAdslConfProfileExtTable": adTAOctAdslConfProfileExtTable,
       "adTAOctAdslConfProfileExtEntry": adTAOctAdslConfProfileExtEntry,
       "adTAOctAdslConfProfileLineType": adTAOctAdslConfProfileLineType,
       "adTAOctAdslConfProfileServiceMode": adTAOctAdslConfProfileServiceMode,
       "adTAOctAdslConfProfileIndexApplied": adTAOctAdslConfProfileIndexApplied,
       "adTAOctAdslConfProfileName": adTAOctAdslConfProfileName,
       "adTAOctAdslAtucConfProfileInterleaveMinINP": adTAOctAdslAtucConfProfileInterleaveMinINP,
       "adTAOctAdslAturConfProfileInterleaveMinINP": adTAOctAdslAturConfProfileInterleaveMinINP,
       "adTAOctAdslAtucConfProfileInterleaveMinInpRev2": adTAOctAdslAtucConfProfileInterleaveMinInpRev2,
       "adTAOctAdslAturConfProfileInterleaveMinInpRev2": adTAOctAdslAturConfProfileInterleaveMinInpRev2,
       "adTAOctAdslConfLineTable": adTAOctAdslConfLineTable,
       "adTAOctAdslConfLineEntry": adTAOctAdslConfLineEntry,
       "adTAOctAdslHamBandMask": adTAOctAdslHamBandMask,
       "adTAOctAdslCabinetMode": adTAOctAdslCabinetMode,
       "adTAOctAdslPowerThreshold": adTAOctAdslPowerThreshold,
       "adTAOctAdslAtucCarrierMask": adTAOctAdslAtucCarrierMask,
       "adTAOctAdslAturCarrierMask": adTAOctAdslAturCarrierMask,
       "adTAOctAdslStatus2": adTAOctAdslStatus2,
       "adTAOctAdslLineTable": adTAOctAdslLineTable,
       "adTAOctAdslLineEntry": adTAOctAdslLineEntry,
       "adTAOctAdslCurrLinkStatus": adTAOctAdslCurrLinkStatus,
       "adTAOctAdslCurrStandard": adTAOctAdslCurrStandard,
       "adTAOctAdslBitAllocationMap": adTAOctAdslBitAllocationMap,
       "adTAOctAdslBitAllocationMapGroup2": adTAOctAdslBitAllocationMapGroup2,
       "adTAOctAdslUsSnrMarginMap": adTAOctAdslUsSnrMarginMap,
       "adTAOctAdslAtucPhysTable": adTAOctAdslAtucPhysTable,
       "adTAOctAdslAtucPhysEntry": adTAOctAdslAtucPhysEntry,
       "adTAOctAdslAtucNumParityBytes": adTAOctAdslAtucNumParityBytes,
       "adTAOctAdslAtucFramesPerCodeword": adTAOctAdslAtucFramesPerCodeword,
       "adTAOctAdslAtucInterleavingDepth": adTAOctAdslAtucInterleavingDepth,
       "adTAOctAdslAturPhysTable": adTAOctAdslAturPhysTable,
       "adTAOctAdslAturPhysEntry": adTAOctAdslAturPhysEntry,
       "adTAOctAdslAturNumParityBytes": adTAOctAdslAturNumParityBytes,
       "adTAOctAdslAturFramesPerCodeword": adTAOctAdslAturFramesPerCodeword,
       "adTAOctAdslAturInterleavingDepth": adTAOctAdslAturInterleavingDepth,
       "adTAOctAdslAturCapabilities": adTAOctAdslAturCapabilities,
       "adTAOctAdslAturInvProviderCode": adTAOctAdslAturInvProviderCode,
       "adTAOctAdslAtucChanTable": adTAOctAdslAtucChanTable,
       "adTAOctAdslAtucChanEntry": adTAOctAdslAtucChanEntry,
       "adTAOctAdslAtucChanINP": adTAOctAdslAtucChanINP,
       "adTAOctAdslAtucRelativeCap": adTAOctAdslAtucRelativeCap,
       "adTAOctAdslAturChanTable": adTAOctAdslAturChanTable,
       "adTAOctAdslAturChanEntry": adTAOctAdslAturChanEntry,
       "adTAOctAdslAturChanINP": adTAOctAdslAturChanINP,
       "adTAOctAdslAturRelativeCap": adTAOctAdslAturRelativeCap,
       "adTAOctAdslAtmAtucCellCountTable": adTAOctAdslAtmAtucCellCountTable,
       "adTAOctAdslAtmAtucCellCountEntry": adTAOctAdslAtmAtucCellCountEntry,
       "adTAOctAdslAtmAtucCellCount": adTAOctAdslAtmAtucCellCount,
       "adTAOctAdslAtmAtucIdleCellCount": adTAOctAdslAtmAtucIdleCellCount,
       "adTAOctAdslAtmAtucHecErrorCount": adTAOctAdslAtmAtucHecErrorCount,
       "adTAOctAdslAtmAturCellCountTable": adTAOctAdslAtmAturCellCountTable,
       "adTAOctAdslAtmAturCellCountEntry": adTAOctAdslAtmAturCellCountEntry,
       "adTAOctAdslAtmAturCellCount": adTAOctAdslAtmAturCellCount,
       "adTAOctAdslAtmAturIdleCellCount": adTAOctAdslAtmAturIdleCellCount,
       "adTAOctAdslID": adTAOctAdslID}
)
