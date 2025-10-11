# SNMP MIB module (NORTEL-OME40G-PM-PROV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/NORTEL-OME40G-PM-PROV-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:20:49 2025
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

(nnOme40G,) = mibBuilder.importSymbols(
    "NORTEL-OME40G-MIB",
    "nnOme40G")

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

nnOme40GPmProv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4)
)
if mibBuilder.loadTexts:
    nnOme40GPmProv.setRevisions(
        ("2007-02-02 00:00",
         "2008-02-07 00:00",
         "2008-02-21 00:00",
         "2008-03-03 00:00",
         "2008-05-01 00:00",
         "2008-08-20 00:00",
         "2009-02-02 00:00")
    )


# Types definitions



class Boolean(Integer32):
    """Custom type Boolean based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )





class Montype(Integer32):
    """Custom type Montype based on Integer32"""
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70)
        )
    )
    namedValues = NamedValues(
        *(("eNILL", 0),
          ("eBRS-W", 1),
          ("eCV-L", 2),
          ("eCV-ODU", 3),
          ("eCV-OTU", 4),
          ("eCV-PCS", 5),
          ("eCV-S", 6),
          ("eDFR-E", 7),
          ("eDFR-W", 8),
          ("eES-E", 9),
          ("eES-L", 10),
          ("eES-ODU", 11),
          ("eES-OTU", 12),
          ("eES-PCS", 13),
          ("eES-S", 14),
          ("eES-W", 15),
          ("eFC-L", 16),
          ("eFC-ODU", 17),
          ("eFCSERR-E", 18),
          ("eFEC-OTU", 19),
          ("eHCCS-OTU", 20),
          ("eINFRAMEDISCDS-E", 21),
          ("eINFRAMESDISCDS-E", 22),
          ("eINFRAMES-E", 23),
          ("eINFRAMESERR-E", 24),
          ("eINFRAMESERR-W", 25),
          ("eINFRAMES-W", 26),
          ("eLDS-W", 27),
          ("eLKDS-E", 28),
          ("eLNKDS-W", 29),
          ("eLSDS-W", 30),
          ("eLUAS-W", 31),
          ("eOPRN-OCH", 32),
          ("eOPR-OCH", 33),
          ("eOPTN-OCH", 34),
          ("eOPT-OCH", 35),
          ("eOUTFRAMESDISCDS-E", 36),
          ("eOUTFRAMES-E", 37),
          ("eOUTFRAMESERR-E", 38),
          ("eOUTFRAMES-W", 39),
          ("ePFBERE-OTU", 40),
          ("ePRFBER-OTU", 41),
          ("ePSCP-L", 42),
          ("ePSCP-ODU", 43),
          ("ePSCW-L", 44),
          ("ePSCW-ODU", 45),
          ("ePSD-L", 46),
          ("ePSD-ODU", 47),
          ("eSBRS-W", 48),
          ("eSEFS-OTU", 49),
          ("eSEFS-S", 50),
          ("eSES-E", 51),
          ("eSES-L", 52),
          ("eSES-ODU", 53),
          ("eSES-OTU", 54),
          ("eSES-PCS", 55),
          ("eSES-S", 56),
          ("eSES-W", 57),
          ("eUAS-E", 58),
          ("eUAS-L", 59),
          ("eUAS-ODU", 60),
          ("eUAS-PCS", 61),
          ("eUAS-W", 62),
          ("eUTLMX-W", 63),
          ("eUTL-W", 64),
          ("eINDFR-E", 65),
          ("eOUTDFR-E", 66),
          ("eDGDAVG-OCH", 67),
          ("eDGDMAX-OCH", 68),
          ("eALL", 69),
          ("eMAX", 70))
    )





class Endpoint(Integer32):
    """Custom type Endpoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nill", 0),
          ("near-end", 1),
          ("far-end", 2),
          ("all", 3))
    )





class Direction(Integer32):
    """Custom type Direction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nill", 0),
          ("trmt", 1),
          ("rcv", 2),
          ("all", 3))
    )





class Binning(Integer32):
    """Custom type Binning based on Integer32"""
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
        *(("nill", 0),
          ("fifteen-min", 1),
          ("one-day", 2),
          ("one-unt", 3),
          ("baseline", 4),
          ("all", 5))
    )





class Profiles(Integer32):
    """Custom type Profiles based on Integer32"""
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
        *(("nill", 0),
          ("profile1", 1),
          ("profile2", 2),
          ("profile3", 3),
          ("profile4", 4),
          ("dflt", 5),
          ("alloff", 6),
          ("factorydflt", 7))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NnOme40GMonConfig_ObjectIdentity = ObjectIdentity
nnOme40GMonConfig = _NnOme40GMonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1)
)
_NnMonConfigTable_Object = MibTable
nnMonConfigTable = _NnMonConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    nnMonConfigTable.setStatus("current")
_NnMonConfigEntry_Object = MibTableRow
nnMonConfigEntry = _NnMonConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 1, 1)
)
nnMonConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nnMonConfigEntry.setStatus("current")
_HccsReference_Type = DisplayString
_HccsReference_Object = MibTableColumn
hccsReference = _HccsReference_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 1, 1, 1),
    _HccsReference_Type()
)
hccsReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hccsReference.setStatus("current")
_Init40GPmRegisters_Type = Binning
_Init40GPmRegisters_Object = MibTableColumn
init40GPmRegisters = _Init40GPmRegisters_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 1, 1, 2),
    _Init40GPmRegisters_Type()
)
init40GPmRegisters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    init40GPmRegisters.setStatus("current")
_Init40GOmCounts_Type = Boolean
_Init40GOmCounts_Object = MibTableColumn
init40GOmCounts = _Init40GOmCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 1, 1, 3),
    _Init40GOmCounts_Type()
)
init40GOmCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    init40GOmCounts.setStatus("current")
_NnMonTypeInstanceTable_Object = MibTable
nnMonTypeInstanceTable = _NnMonTypeInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2)
)
if mibBuilder.loadTexts:
    nnMonTypeInstanceTable.setStatus("current")
_NnMonTypeInstanceEntry_Object = MibTableRow
nnMonTypeInstanceEntry = _NnMonTypeInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2, 1)
)
nnMonTypeInstanceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "NORTEL-OME40G-PM-PROV-MIB", "monType"),
    (0, "NORTEL-OME40G-PM-PROV-MIB", "endpoint"),
    (0, "NORTEL-OME40G-PM-PROV-MIB", "direction"),
    (0, "NORTEL-OME40G-PM-PROV-MIB", "accumTimePeriod"),
)
if mibBuilder.loadTexts:
    nnMonTypeInstanceEntry.setStatus("current")
_MonType_Type = Montype
_MonType_Object = MibTableColumn
monType = _MonType_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2, 1, 1),
    _MonType_Type()
)
monType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    monType.setStatus("current")
_Endpoint_Type = Endpoint
_Endpoint_Object = MibTableColumn
endpoint = _Endpoint_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2, 1, 2),
    _Endpoint_Type()
)
endpoint.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    endpoint.setStatus("current")
_Direction_Type = Direction
_Direction_Object = MibTableColumn
direction = _Direction_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2, 1, 3),
    _Direction_Type()
)
direction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    direction.setStatus("current")
_AccumTimePeriod_Type = Binning
_AccumTimePeriod_Object = MibTableColumn
accumTimePeriod = _AccumTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2, 1, 4),
    _AccumTimePeriod_Type()
)
accumTimePeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accumTimePeriod.setStatus("current")
_MonVal_Type = Integer32
_MonVal_Object = MibTableColumn
monVal = _MonVal_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2, 1, 5),
    _MonVal_Type()
)
monVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monVal.setStatus("current")
_ThreshLevel_Type = DisplayString
_ThreshLevel_Object = MibTableColumn
threshLevel = _ThreshLevel_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2, 1, 6),
    _ThreshLevel_Type()
)
threshLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    threshLevel.setStatus("current")
_SrcProfileId_Type = Profiles
_SrcProfileId_Object = MibTableColumn
srcProfileId = _SrcProfileId_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2, 1, 7),
    _SrcProfileId_Type()
)
srcProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srcProfileId.setStatus("current")
_DstProfileId_Type = Profiles
_DstProfileId_Object = MibTableColumn
dstProfileId = _DstProfileId_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2, 1, 8),
    _DstProfileId_Type()
)
dstProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dstProfileId.setStatus("current")
_InitRegisters_Type = Boolean
_InitRegisters_Object = MibTableColumn
initRegisters = _InitRegisters_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 1, 2, 1, 9),
    _InitRegisters_Type()
)
initRegisters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    initRegisters.setStatus("current")
_InitShelf40GPmRegisters_Type = Binning
_InitShelf40GPmRegisters_Object = MibScalar
initShelf40GPmRegisters = _InitShelf40GPmRegisters_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 2),
    _InitShelf40GPmRegisters_Type()
)
initShelf40GPmRegisters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    initShelf40GPmRegisters.setStatus("current")
_InitShelfEthOmCounts_Type = Boolean
_InitShelfEthOmCounts_Object = MibScalar
initShelfEthOmCounts = _InitShelfEthOmCounts_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 4, 3),
    _InitShelfEthOmCounts_Type()
)
initShelfEthOmCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    initShelfEthOmCounts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NORTEL-OME40G-PM-PROV-MIB",
    **{"Boolean": Boolean,
       "Montype": Montype,
       "Endpoint": Endpoint,
       "Direction": Direction,
       "Binning": Binning,
       "Profiles": Profiles,
       "nnOme40GPmProv": nnOme40GPmProv,
       "nnOme40GMonConfig": nnOme40GMonConfig,
       "nnMonConfigTable": nnMonConfigTable,
       "nnMonConfigEntry": nnMonConfigEntry,
       "hccsReference": hccsReference,
       "init40GPmRegisters": init40GPmRegisters,
       "init40GOmCounts": init40GOmCounts,
       "nnMonTypeInstanceTable": nnMonTypeInstanceTable,
       "nnMonTypeInstanceEntry": nnMonTypeInstanceEntry,
       "monType": monType,
       "endpoint": endpoint,
       "direction": direction,
       "accumTimePeriod": accumTimePeriod,
       "monVal": monVal,
       "threshLevel": threshLevel,
       "srcProfileId": srcProfileId,
       "dstProfileId": dstProfileId,
       "initRegisters": initRegisters,
       "initShelf40GPmRegisters": initShelf40GPmRegisters,
       "initShelfEthOmCounts": initShelfEthOmCounts}
)
