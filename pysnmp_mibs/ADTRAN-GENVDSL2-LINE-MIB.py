# SNMP MIB module (ADTRAN-GENVDSL2-LINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENVDSL2-LINE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:29:43 2025
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

(adGenPortTrapIdentifier,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortTrapIdentifier")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adGenVdsl2,
 adGenVdsl2ID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-VDSL2-MIB",
    "adGenVdsl2",
    "adGenVdsl2ID")

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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

adGenVdsl2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 65, 1, 1)
)
if mibBuilder.loadTexts:
    adGenVdsl2MIB.setRevisions(
        ("2020-05-11 00:00",
         "2018-02-26 00:00",
         "2017-10-26 00:00",
         "2017-10-13 00:00",
         "2017-09-06 00:00",
         "2017-08-04 00:00",
         "2015-09-16 00:00",
         "2015-06-03 00:00",
         "2015-03-17 00:00",
         "2015-01-14 00:00",
         "2014-01-24 00:00",
         "2013-12-12 00:00",
         "2013-09-18 00:00",
         "2013-07-17 00:00",
         "2013-03-06 00:00",
         "2012-10-08 00:00",
         "2012-09-25 00:00",
         "2011-09-19 00:00",
         "2011-06-02 00:00",
         "2010-09-09 00:00",
         "2010-08-16 00:00",
         "2010-08-09 00:00",
         "2008-07-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Adtran_ObjectIdentity = ObjectIdentity
adtran = _Adtran_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664)
)
_AdProducts_ObjectIdentity = ObjectIdentity
adProducts = _AdProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1)
)
_AdTA5k24pVDSL2Combo_ObjectIdentity = ObjectIdentity
adTA5k24pVDSL2Combo = _AdTA5k24pVDSL2Combo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1, 891)
)
_AdTA5k32pVDSL2_ObjectIdentity = ObjectIdentity
adTA5k32pVDSL2 = _AdTA5k32pVDSL2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1, 892)
)
_AdTA5k32pVDSL2Spltr_ObjectIdentity = ObjectIdentity
adTA5k32pVDSL2Spltr = _AdTA5k32pVDSL2Spltr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1, 893)
)
_AdGenVdsl2Prov_ObjectIdentity = ObjectIdentity
adGenVdsl2Prov = _AdGenVdsl2Prov_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1)
)
_AdGenVdsl2LineConfProfileTable_Object = MibTable
adGenVdsl2LineConfProfileTable = _AdGenVdsl2LineConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adGenVdsl2LineConfProfileTable.setStatus("current")
_AdGenVdsl2LineConfProfileEntry_Object = MibTableRow
adGenVdsl2LineConfProfileEntry = _AdGenVdsl2LineConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1)
)
adGenVdsl2LineConfProfileEntry.setIndexNames(
    (1, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2LineConfProfileName"),
)
if mibBuilder.loadTexts:
    adGenVdsl2LineConfProfileEntry.setStatus("current")


class _AdGenVdsl2LineConfProfileName_Type(DisplayString):
    """Custom type adGenVdsl2LineConfProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_AdGenVdsl2LineConfProfileName_Type.__name__ = "DisplayString"
_AdGenVdsl2LineConfProfileName_Object = MibTableColumn
adGenVdsl2LineConfProfileName = _AdGenVdsl2LineConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 1),
    _AdGenVdsl2LineConfProfileName_Type()
)
adGenVdsl2LineConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVdsl2LineConfProfileName.setStatus("current")


class _AdGenVdsl2ConfDsRateMode_Type(Integer32):
    """Custom type adGenVdsl2ConfDsRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("adaptAtStartup", 2),
          ("adaptAtRuntime", 3))
    )


_AdGenVdsl2ConfDsRateMode_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsRateMode_Object = MibTableColumn
adGenVdsl2ConfDsRateMode = _AdGenVdsl2ConfDsRateMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 2),
    _AdGenVdsl2ConfDsRateMode_Type()
)
adGenVdsl2ConfDsRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsRateMode.setStatus("current")


class _AdGenVdsl2ConfDsTargetSnrMgn_Type(Integer32):
    """Custom type adGenVdsl2ConfDsTargetSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_AdGenVdsl2ConfDsTargetSnrMgn_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsTargetSnrMgn_Object = MibTableColumn
adGenVdsl2ConfDsTargetSnrMgn = _AdGenVdsl2ConfDsTargetSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 3),
    _AdGenVdsl2ConfDsTargetSnrMgn_Type()
)
adGenVdsl2ConfDsTargetSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsTargetSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsTargetSnrMgn.setUnits("tenth dB")


class _AdGenVdsl2ConfDsMaxSnrMgn_Type(Integer32):
    """Custom type adGenVdsl2ConfDsMaxSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_AdGenVdsl2ConfDsMaxSnrMgn_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsMaxSnrMgn_Object = MibTableColumn
adGenVdsl2ConfDsMaxSnrMgn = _AdGenVdsl2ConfDsMaxSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 4),
    _AdGenVdsl2ConfDsMaxSnrMgn_Type()
)
adGenVdsl2ConfDsMaxSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsMaxSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsMaxSnrMgn.setUnits("tenth dB")


class _AdGenVdsl2ConfDsMinSnrMgn_Type(Integer32):
    """Custom type adGenVdsl2ConfDsMinSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_AdGenVdsl2ConfDsMinSnrMgn_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsMinSnrMgn_Object = MibTableColumn
adGenVdsl2ConfDsMinSnrMgn = _AdGenVdsl2ConfDsMinSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 5),
    _AdGenVdsl2ConfDsMinSnrMgn_Type()
)
adGenVdsl2ConfDsMinSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsMinSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsMinSnrMgn.setUnits("tenth dB")


class _AdGenVdsl2ConfUsTargetSnrMgn_Type(Integer32):
    """Custom type adGenVdsl2ConfUsTargetSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_AdGenVdsl2ConfUsTargetSnrMgn_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsTargetSnrMgn_Object = MibTableColumn
adGenVdsl2ConfUsTargetSnrMgn = _AdGenVdsl2ConfUsTargetSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 6),
    _AdGenVdsl2ConfUsTargetSnrMgn_Type()
)
adGenVdsl2ConfUsTargetSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsTargetSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsTargetSnrMgn.setUnits("tenth dB")


class _AdGenVdsl2ConfUsMaxSnrMgn_Type(Integer32):
    """Custom type adGenVdsl2ConfUsMaxSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_AdGenVdsl2ConfUsMaxSnrMgn_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsMaxSnrMgn_Object = MibTableColumn
adGenVdsl2ConfUsMaxSnrMgn = _AdGenVdsl2ConfUsMaxSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 7),
    _AdGenVdsl2ConfUsMaxSnrMgn_Type()
)
adGenVdsl2ConfUsMaxSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsMaxSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsMaxSnrMgn.setUnits("tenth dB")


class _AdGenVdsl2ConfUsMinSnrMgn_Type(Integer32):
    """Custom type adGenVdsl2ConfUsMinSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_AdGenVdsl2ConfUsMinSnrMgn_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsMinSnrMgn_Object = MibTableColumn
adGenVdsl2ConfUsMinSnrMgn = _AdGenVdsl2ConfUsMinSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 8),
    _AdGenVdsl2ConfUsMinSnrMgn_Type()
)
adGenVdsl2ConfUsMinSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsMinSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsMinSnrMgn.setUnits("tenth dB")
_AdGenVdsl2LineConfProfileRowStatus_Type = RowStatus
_AdGenVdsl2LineConfProfileRowStatus_Object = MibTableColumn
adGenVdsl2LineConfProfileRowStatus = _AdGenVdsl2LineConfProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 9),
    _AdGenVdsl2LineConfProfileRowStatus_Type()
)
adGenVdsl2LineConfProfileRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2LineConfProfileRowStatus.setStatus("current")


class _AdGenVdsl2ConfServiceMode_Type(Integer32):
    """Custom type adGenVdsl2ConfServiceMode based on Integer32"""
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
              255)
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
          ("g9925AnxM", 10),
          ("g9931", 11),
          ("g9932", 12),
          ("vdsl2MultiMode", 13),
          ("vdsl2PtmFallback", 14),
          ("tseMultimode", 255))
    )


_AdGenVdsl2ConfServiceMode_Type.__name__ = "Integer32"
_AdGenVdsl2ConfServiceMode_Object = MibTableColumn
adGenVdsl2ConfServiceMode = _AdGenVdsl2ConfServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 10),
    _AdGenVdsl2ConfServiceMode_Type()
)
adGenVdsl2ConfServiceMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfServiceMode.setStatus("current")
_AdGenVdsl2ConfMultiModeDmtTse_Type = Unsigned32
_AdGenVdsl2ConfMultiModeDmtTse_Object = MibTableColumn
adGenVdsl2ConfMultiModeDmtTse = _AdGenVdsl2ConfMultiModeDmtTse_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 11),
    _AdGenVdsl2ConfMultiModeDmtTse_Type()
)
adGenVdsl2ConfMultiModeDmtTse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfMultiModeDmtTse.setStatus("current")
_AdGenVdsl2ConfBandProfiles_Type = Unsigned32
_AdGenVdsl2ConfBandProfiles_Object = MibTableColumn
adGenVdsl2ConfBandProfiles = _AdGenVdsl2ConfBandProfiles_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 12),
    _AdGenVdsl2ConfBandProfiles_Type()
)
adGenVdsl2ConfBandProfiles.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfBandProfiles.setStatus("current")


class _AdGenVdsl2ConfSpecificPsdSelect_Type(Integer32):
    """Custom type adGenVdsl2ConfSpecificPsdSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(21,
              22,
              23,
              24,
              41,
              42,
              43,
              44,
              45,
              46,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              121,
              129,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              309,
              310,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              409,
              410,
              411,
              412,
              413,
              414,
              415,
              416,
              419,
              420,
              421,
              422,
              431,
              432,
              501,
              502,
              503,
              504,
              505,
              506,
              601)
        )
    )
    namedValues = NamedValues(
        *(("vdsl1-ansi-fttcab-m1", 21),
          ("vdsl1-ansi-fttcab-m2", 22),
          ("vdsl1-ansi-fttex-m1", 23),
          ("vdsl1-ansi-fttex-m2", 24),
          ("vdsl1-etsi-fttcab-pcab-m1", 41),
          ("vdsl1-etsi-fttcab-pcab-m2", 42),
          ("vdsl1-etsi-fttex-p1-m1-o-isdn", 43),
          ("vdsl1-etsi-fttex-p1-m2-o-isdn", 44),
          ("vdsl1-etsi-fttex-p2-m1-o-pots", 45),
          ("vdsl1-etsi-fttex-p2-m2-o-pots", 46),
          ("vdsl2-a-m1-eu32", 101),
          ("vdsl2-a-m2-eu36", 102),
          ("vdsl2-a-m3-eu40", 103),
          ("vdsl2-a-m4-eu44", 104),
          ("vdsl2-a-m5-eu48", 105),
          ("vdsl2-a-m6-eu52", 106),
          ("vdsl2-a-m7-eu56", 107),
          ("vdsl2-a-m8-eu60", 108),
          ("vdsl2-a-m9-eu64", 109),
          ("vdsl2-a-eu128", 110),
          ("vdsl2-a-m1-998-35b-eu32", 121),
          ("vdsl2-a-m9-998-35b-eu64", 129),
          ("vdsl2-a-m1-adlu32", 201),
          ("vdsl2-a-m2-adlu36", 202),
          ("vdsl2-a-m3-adlu40", 203),
          ("vdsl2-a-m4-adlu44", 204),
          ("vdsl2-a-m5-adlu48", 205),
          ("vdsl2-a-m6-adlu52", 206),
          ("vdsl2-a-m7-adlu56", 207),
          ("vdsl2-a-m8-adlu60", 208),
          ("vdsl2-a-m9-adlu64", 209),
          ("vdsl2-a-adlu128", 210),
          ("vdsl2-b7-1-997-m1c-a-7", 301),
          ("vdsl2-b7-2-997-m1x-m-8", 302),
          ("vdsl2-b7-3-997-m1x-m", 303),
          ("vdsl2-b7-4-997-m2x-m-8", 304),
          ("vdsl2-b7-5-997-m2x-a", 305),
          ("vdsl2-b7-6-997-m2x-m", 306),
          ("vdsl2-b7-7-hpe17-m1-nus0", 307),
          ("vdsl2-b7-8-hpe30-m1-nus0", 308),
          ("vdsl2-b7-9-997e17-m2x-nus0", 309),
          ("vdsl2-b7-10-997e30-m2x-nus0", 310),
          ("vdsl2-b8-1-998-m1x-a", 401),
          ("vdsl2-b8-2-998-m1x-b", 402),
          ("vdsl2-b8-3-998-m1x-nus0", 403),
          ("vdsl2-b8-4-998-m2x-a", 404),
          ("vdsl2-b8-5-998-m2x-m", 405),
          ("vdsl2-b8-6-998-m2x-b", 406),
          ("vdsl2-b8-7-998-m2x-nus0", 407),
          ("vdsl2-b8-8-998e17-m2x-nus0", 408),
          ("vdsl2-b8-9-998e17-m2x-nus0-m", 409),
          ("vdsl2-b8-10-998ade17-m2x-nus0-m", 410),
          ("vdsl2-b8-11-998ade17-m2x-a", 411),
          ("vdsl2-b8-12-998ade17-m2x-b", 412),
          ("vdsl2-b8-13-998e30-m2x-nus0", 413),
          ("vdsl2-b8-14-998e30-m2x-nus0-m", 414),
          ("vdsl2-b8-15-998ade30-m2x-nus0-m", 415),
          ("vdsl2-b8-16-998ade30-m2x-nus0-a", 416),
          ("vdsl2-b8-19-998e35-m2x-a", 419),
          ("vdsl2-b8-20-998ade35-m2x-a", 420),
          ("vdsl2-b8-21-998ade35-m2x-b", 421),
          ("vdsl2-b8-22-998ade35-m2x-m", 422),
          ("vdsl2-b8-998ade17-m2x-m", 431),
          ("vdsl2-b8-998e17-m2x-a", 432),
          ("vdsl2-c-fttcab-a", 501),
          ("vdsl2-c-fttcab-m", 502),
          ("vdsl2-c-fttex-a", 503),
          ("vdsl2-c-fttex-m", 504),
          ("vdsl2-c-o-adsl", 505),
          ("vdsl2-c-o-tcmisdn", 506),
          ("vdsl2-c-anfp", 601))
    )


_AdGenVdsl2ConfSpecificPsdSelect_Type.__name__ = "Integer32"
_AdGenVdsl2ConfSpecificPsdSelect_Object = MibTableColumn
adGenVdsl2ConfSpecificPsdSelect = _AdGenVdsl2ConfSpecificPsdSelect_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 13),
    _AdGenVdsl2ConfSpecificPsdSelect_Type()
)
adGenVdsl2ConfSpecificPsdSelect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfSpecificPsdSelect.setStatus("current")


class _AdGenVdsl2ConfUsPsdMaskU0Select_Type(Integer32):
    """Custom type adGenVdsl2ConfUsPsdMaskU0Select based on Integer32"""
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


_AdGenVdsl2ConfUsPsdMaskU0Select_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsPsdMaskU0Select_Object = MibTableColumn
adGenVdsl2ConfUsPsdMaskU0Select = _AdGenVdsl2ConfUsPsdMaskU0Select_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 14),
    _AdGenVdsl2ConfUsPsdMaskU0Select_Type()
)
adGenVdsl2ConfUsPsdMaskU0Select.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsPsdMaskU0Select.setStatus("current")


class _AdGenVdsl2ConfUsTrellis_Type(Integer32):
    """Custom type adGenVdsl2ConfUsTrellis based on Integer32"""
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


_AdGenVdsl2ConfUsTrellis_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsTrellis_Object = MibTableColumn
adGenVdsl2ConfUsTrellis = _AdGenVdsl2ConfUsTrellis_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 15),
    _AdGenVdsl2ConfUsTrellis_Type()
)
adGenVdsl2ConfUsTrellis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsTrellis.setStatus("current")


class _AdGenVdsl2ConfDsTrellis_Type(Integer32):
    """Custom type adGenVdsl2ConfDsTrellis based on Integer32"""
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


_AdGenVdsl2ConfDsTrellis_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsTrellis_Object = MibTableColumn
adGenVdsl2ConfDsTrellis = _AdGenVdsl2ConfDsTrellis_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 16),
    _AdGenVdsl2ConfDsTrellis_Type()
)
adGenVdsl2ConfDsTrellis.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsTrellis.setStatus("current")


class _AdGenVdsl2ConfUsPboSetting_Type(Integer32):
    """Custom type adGenVdsl2ConfUsPboSetting based on Integer32"""
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
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("pboOff", 0),
          ("pboEnvA", 1),
          ("pboEnvB", 2),
          ("pboEnvC", 3),
          ("pboEnvD", 4),
          ("pboEnvE", 5),
          ("pboEnvF", 6),
          ("pboANFP", 7),
          ("pboAuto", 254),
          ("pboCustom", 255))
    )


_AdGenVdsl2ConfUsPboSetting_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsPboSetting_Object = MibTableColumn
adGenVdsl2ConfUsPboSetting = _AdGenVdsl2ConfUsPboSetting_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 17),
    _AdGenVdsl2ConfUsPboSetting_Type()
)
adGenVdsl2ConfUsPboSetting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsPboSetting.setStatus("current")


class _AdGenVdsl2ConfDsPboSetting_Type(Integer32):
    """Custom type adGenVdsl2ConfDsPboSetting based on Integer32"""
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
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("pboOff", 0),
          ("pboEnvA", 1),
          ("pboEnvB", 2),
          ("pboEnvC", 3),
          ("pboEnvD", 4),
          ("pboEnvE", 5),
          ("pboEnvF", 6),
          ("pboANFP", 7),
          ("pboAuto", 254),
          ("pboCustom", 255))
    )


_AdGenVdsl2ConfDsPboSetting_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsPboSetting_Object = MibTableColumn
adGenVdsl2ConfDsPboSetting = _AdGenVdsl2ConfDsPboSetting_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 18),
    _AdGenVdsl2ConfDsPboSetting_Type()
)
adGenVdsl2ConfDsPboSetting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsPboSetting.setStatus("current")


class _AdGenVdsl2ConfUsVnoiseSetting_Type(Integer32):
    """Custom type adGenVdsl2ConfUsVnoiseSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("low", 1),
          ("med", 2),
          ("high", 3),
          ("auto", 254),
          ("custom", 255))
    )


_AdGenVdsl2ConfUsVnoiseSetting_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsVnoiseSetting_Object = MibTableColumn
adGenVdsl2ConfUsVnoiseSetting = _AdGenVdsl2ConfUsVnoiseSetting_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 19),
    _AdGenVdsl2ConfUsVnoiseSetting_Type()
)
adGenVdsl2ConfUsVnoiseSetting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsVnoiseSetting.setStatus("current")


class _AdGenVdsl2ConfDsVnoiseSetting_Type(Integer32):
    """Custom type adGenVdsl2ConfDsVnoiseSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("low", 1),
          ("med", 2),
          ("high", 3),
          ("auto", 254),
          ("custom", 255))
    )


_AdGenVdsl2ConfDsVnoiseSetting_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsVnoiseSetting_Object = MibTableColumn
adGenVdsl2ConfDsVnoiseSetting = _AdGenVdsl2ConfDsVnoiseSetting_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 20),
    _AdGenVdsl2ConfDsVnoiseSetting_Type()
)
adGenVdsl2ConfDsVnoiseSetting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsVnoiseSetting.setStatus("current")


class _AdGenVdsl2ConfUsBitSwap_Type(Integer32):
    """Custom type adGenVdsl2ConfUsBitSwap based on Integer32"""
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


_AdGenVdsl2ConfUsBitSwap_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsBitSwap_Object = MibTableColumn
adGenVdsl2ConfUsBitSwap = _AdGenVdsl2ConfUsBitSwap_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 21),
    _AdGenVdsl2ConfUsBitSwap_Type()
)
adGenVdsl2ConfUsBitSwap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsBitSwap.setStatus("current")


class _AdGenVdsl2ConfDsBitSwap_Type(Integer32):
    """Custom type adGenVdsl2ConfDsBitSwap based on Integer32"""
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


_AdGenVdsl2ConfDsBitSwap_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsBitSwap_Object = MibTableColumn
adGenVdsl2ConfDsBitSwap = _AdGenVdsl2ConfDsBitSwap_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 22),
    _AdGenVdsl2ConfDsBitSwap_Type()
)
adGenVdsl2ConfDsBitSwap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsBitSwap.setStatus("current")
_AdGenVdsl2ConfHamBandNotches_Type = Unsigned32
_AdGenVdsl2ConfHamBandNotches_Object = MibTableColumn
adGenVdsl2ConfHamBandNotches = _AdGenVdsl2ConfHamBandNotches_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 23),
    _AdGenVdsl2ConfHamBandNotches_Type()
)
adGenVdsl2ConfHamBandNotches.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfHamBandNotches.setStatus("current")


class _AdGenVdsl2ConfUsNomAggTxPwr_Type(Integer32):
    """Custom type adGenVdsl2ConfUsNomAggTxPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenVdsl2ConfUsNomAggTxPwr_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsNomAggTxPwr_Object = MibTableColumn
adGenVdsl2ConfUsNomAggTxPwr = _AdGenVdsl2ConfUsNomAggTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 24),
    _AdGenVdsl2ConfUsNomAggTxPwr_Type()
)
adGenVdsl2ConfUsNomAggTxPwr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsNomAggTxPwr.setStatus("current")
_AdGenVdsl2ConfDsNomAggTxPwr_Type = Integer32
_AdGenVdsl2ConfDsNomAggTxPwr_Object = MibTableColumn
adGenVdsl2ConfDsNomAggTxPwr = _AdGenVdsl2ConfDsNomAggTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 25),
    _AdGenVdsl2ConfDsNomAggTxPwr_Type()
)
adGenVdsl2ConfDsNomAggTxPwr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsNomAggTxPwr.setStatus("current")


class _AdGenVdsl2ConfUsMaxNomTxPsd_Type(Integer32):
    """Custom type adGenVdsl2ConfUsMaxNomTxPsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 300),
    )


_AdGenVdsl2ConfUsMaxNomTxPsd_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsMaxNomTxPsd_Object = MibTableColumn
adGenVdsl2ConfUsMaxNomTxPsd = _AdGenVdsl2ConfUsMaxNomTxPsd_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 26),
    _AdGenVdsl2ConfUsMaxNomTxPsd_Type()
)
adGenVdsl2ConfUsMaxNomTxPsd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsMaxNomTxPsd.setStatus("current")


class _AdGenVdsl2ConfDsMaxNomTxPsd_Type(Integer32):
    """Custom type adGenVdsl2ConfDsMaxNomTxPsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 300),
    )


_AdGenVdsl2ConfDsMaxNomTxPsd_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsMaxNomTxPsd_Object = MibTableColumn
adGenVdsl2ConfDsMaxNomTxPsd = _AdGenVdsl2ConfDsMaxNomTxPsd_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 27),
    _AdGenVdsl2ConfDsMaxNomTxPsd_Type()
)
adGenVdsl2ConfDsMaxNomTxPsd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsMaxNomTxPsd.setStatus("current")


class _AdGenVdsl2ConfUsMaxAggRxPwr_Type(Integer32):
    """Custom type adGenVdsl2ConfUsMaxAggRxPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_AdGenVdsl2ConfUsMaxAggRxPwr_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsMaxAggRxPwr_Object = MibTableColumn
adGenVdsl2ConfUsMaxAggRxPwr = _AdGenVdsl2ConfUsMaxAggRxPwr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 28),
    _AdGenVdsl2ConfUsMaxAggRxPwr_Type()
)
adGenVdsl2ConfUsMaxAggRxPwr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsMaxAggRxPwr.setStatus("current")


class _AdGenVdsl2ConfFramingMode_Type(Integer32):
    """Custom type adGenVdsl2ConfFramingMode based on Integer32"""
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
        *(("auto", 0),
          ("atm", 1),
          ("efm", 2),
          ("hdlc", 3))
    )


_AdGenVdsl2ConfFramingMode_Type.__name__ = "Integer32"
_AdGenVdsl2ConfFramingMode_Object = MibTableColumn
adGenVdsl2ConfFramingMode = _AdGenVdsl2ConfFramingMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 29),
    _AdGenVdsl2ConfFramingMode_Type()
)
adGenVdsl2ConfFramingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfFramingMode.setStatus("current")


class _AdGenVdsl2ConfUsLp0MaxPayloadRate_Type(Unsigned32):
    """Custom type adGenVdsl2ConfUsLp0MaxPayloadRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96000000),
    )


_AdGenVdsl2ConfUsLp0MaxPayloadRate_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfUsLp0MaxPayloadRate_Object = MibTableColumn
adGenVdsl2ConfUsLp0MaxPayloadRate = _AdGenVdsl2ConfUsLp0MaxPayloadRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 30),
    _AdGenVdsl2ConfUsLp0MaxPayloadRate_Type()
)
adGenVdsl2ConfUsLp0MaxPayloadRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0MaxPayloadRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0MaxPayloadRate.setUnits("bps")


class _AdGenVdsl2ConfUsLp0MinPayloadRate_Type(Unsigned32):
    """Custom type adGenVdsl2ConfUsLp0MinPayloadRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96000000),
    )


_AdGenVdsl2ConfUsLp0MinPayloadRate_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfUsLp0MinPayloadRate_Object = MibTableColumn
adGenVdsl2ConfUsLp0MinPayloadRate = _AdGenVdsl2ConfUsLp0MinPayloadRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 31),
    _AdGenVdsl2ConfUsLp0MinPayloadRate_Type()
)
adGenVdsl2ConfUsLp0MinPayloadRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0MinPayloadRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0MinPayloadRate.setUnits("bps")


class _AdGenVdsl2ConfUsLp0MaxDelay_Type(Unsigned32):
    """Custom type adGenVdsl2ConfUsLp0MaxDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenVdsl2ConfUsLp0MaxDelay_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfUsLp0MaxDelay_Object = MibTableColumn
adGenVdsl2ConfUsLp0MaxDelay = _AdGenVdsl2ConfUsLp0MaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 32),
    _AdGenVdsl2ConfUsLp0MaxDelay_Type()
)
adGenVdsl2ConfUsLp0MaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0MaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0MaxDelay.setUnits("msec")


class _AdGenVdsl2ConfUsLp0MinProtection_Type(Unsigned32):
    """Custom type adGenVdsl2ConfUsLp0MinProtection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AdGenVdsl2ConfUsLp0MinProtection_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfUsLp0MinProtection_Object = MibTableColumn
adGenVdsl2ConfUsLp0MinProtection = _AdGenVdsl2ConfUsLp0MinProtection_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 33),
    _AdGenVdsl2ConfUsLp0MinProtection_Type()
)
adGenVdsl2ConfUsLp0MinProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0MinProtection.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0MinProtection.setUnits("0.5 Sym")


class _AdGenVdsl2ConfUsLp0RaRatio_Type(Integer32):
    """Custom type adGenVdsl2ConfUsLp0RaRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenVdsl2ConfUsLp0RaRatio_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsLp0RaRatio_Object = MibTableColumn
adGenVdsl2ConfUsLp0RaRatio = _AdGenVdsl2ConfUsLp0RaRatio_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 34),
    _AdGenVdsl2ConfUsLp0RaRatio_Type()
)
adGenVdsl2ConfUsLp0RaRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0RaRatio.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0RaRatio.setUnits("%")


class _AdGenVdsl2ConfUsLp0InitPolicy_Type(Integer32):
    """Custom type adGenVdsl2ConfUsLp0InitPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ndr", 0),
          ("inp", 1))
    )


_AdGenVdsl2ConfUsLp0InitPolicy_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsLp0InitPolicy_Object = MibTableColumn
adGenVdsl2ConfUsLp0InitPolicy = _AdGenVdsl2ConfUsLp0InitPolicy_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 35),
    _AdGenVdsl2ConfUsLp0InitPolicy_Type()
)
adGenVdsl2ConfUsLp0InitPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0InitPolicy.setStatus("current")


class _AdGenVdsl2ConfDsLp0MaxPayloadRate_Type(Unsigned32):
    """Custom type adGenVdsl2ConfDsLp0MaxPayloadRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 350000000),
    )


_AdGenVdsl2ConfDsLp0MaxPayloadRate_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfDsLp0MaxPayloadRate_Object = MibTableColumn
adGenVdsl2ConfDsLp0MaxPayloadRate = _AdGenVdsl2ConfDsLp0MaxPayloadRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 36),
    _AdGenVdsl2ConfDsLp0MaxPayloadRate_Type()
)
adGenVdsl2ConfDsLp0MaxPayloadRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0MaxPayloadRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0MaxPayloadRate.setUnits("bps")


class _AdGenVdsl2ConfDsLp0MinPayloadRate_Type(Unsigned32):
    """Custom type adGenVdsl2ConfDsLp0MinPayloadRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 350000000),
    )


_AdGenVdsl2ConfDsLp0MinPayloadRate_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfDsLp0MinPayloadRate_Object = MibTableColumn
adGenVdsl2ConfDsLp0MinPayloadRate = _AdGenVdsl2ConfDsLp0MinPayloadRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 37),
    _AdGenVdsl2ConfDsLp0MinPayloadRate_Type()
)
adGenVdsl2ConfDsLp0MinPayloadRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0MinPayloadRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0MinPayloadRate.setUnits("bps")


class _AdGenVdsl2ConfDsLp0MaxDelay_Type(Unsigned32):
    """Custom type adGenVdsl2ConfDsLp0MaxDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenVdsl2ConfDsLp0MaxDelay_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfDsLp0MaxDelay_Object = MibTableColumn
adGenVdsl2ConfDsLp0MaxDelay = _AdGenVdsl2ConfDsLp0MaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 38),
    _AdGenVdsl2ConfDsLp0MaxDelay_Type()
)
adGenVdsl2ConfDsLp0MaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0MaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0MaxDelay.setUnits("msec")


class _AdGenVdsl2ConfDsLp0MinProtection_Type(Unsigned32):
    """Custom type adGenVdsl2ConfDsLp0MinProtection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AdGenVdsl2ConfDsLp0MinProtection_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfDsLp0MinProtection_Object = MibTableColumn
adGenVdsl2ConfDsLp0MinProtection = _AdGenVdsl2ConfDsLp0MinProtection_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 39),
    _AdGenVdsl2ConfDsLp0MinProtection_Type()
)
adGenVdsl2ConfDsLp0MinProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0MinProtection.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0MinProtection.setUnits("0.5 Sym")


class _AdGenVdsl2ConfDsLp0RaRatio_Type(Integer32):
    """Custom type adGenVdsl2ConfDsLp0RaRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenVdsl2ConfDsLp0RaRatio_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsLp0RaRatio_Object = MibTableColumn
adGenVdsl2ConfDsLp0RaRatio = _AdGenVdsl2ConfDsLp0RaRatio_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 40),
    _AdGenVdsl2ConfDsLp0RaRatio_Type()
)
adGenVdsl2ConfDsLp0RaRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0RaRatio.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0RaRatio.setUnits("%")


class _AdGenVdsl2ConfDsLp0InitPolicy_Type(Integer32):
    """Custom type adGenVdsl2ConfDsLp0InitPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ndr", 0),
          ("inp", 1))
    )


_AdGenVdsl2ConfDsLp0InitPolicy_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsLp0InitPolicy_Object = MibTableColumn
adGenVdsl2ConfDsLp0InitPolicy = _AdGenVdsl2ConfDsLp0InitPolicy_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 41),
    _AdGenVdsl2ConfDsLp0InitPolicy_Type()
)
adGenVdsl2ConfDsLp0InitPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0InitPolicy.setStatus("current")


class _AdGenVdsl2ConfUsLp1MaxPayloadRate_Type(Unsigned32):
    """Custom type adGenVdsl2ConfUsLp1MaxPayloadRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96000000),
    )


_AdGenVdsl2ConfUsLp1MaxPayloadRate_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfUsLp1MaxPayloadRate_Object = MibTableColumn
adGenVdsl2ConfUsLp1MaxPayloadRate = _AdGenVdsl2ConfUsLp1MaxPayloadRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 42),
    _AdGenVdsl2ConfUsLp1MaxPayloadRate_Type()
)
adGenVdsl2ConfUsLp1MaxPayloadRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1MaxPayloadRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1MaxPayloadRate.setUnits("bps")


class _AdGenVdsl2ConfUsLp1MinPayloadRate_Type(Unsigned32):
    """Custom type adGenVdsl2ConfUsLp1MinPayloadRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96000000),
    )


_AdGenVdsl2ConfUsLp1MinPayloadRate_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfUsLp1MinPayloadRate_Object = MibTableColumn
adGenVdsl2ConfUsLp1MinPayloadRate = _AdGenVdsl2ConfUsLp1MinPayloadRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 43),
    _AdGenVdsl2ConfUsLp1MinPayloadRate_Type()
)
adGenVdsl2ConfUsLp1MinPayloadRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1MinPayloadRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1MinPayloadRate.setUnits("bps")


class _AdGenVdsl2ConfUsLp1MaxDelay_Type(Unsigned32):
    """Custom type adGenVdsl2ConfUsLp1MaxDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenVdsl2ConfUsLp1MaxDelay_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfUsLp1MaxDelay_Object = MibTableColumn
adGenVdsl2ConfUsLp1MaxDelay = _AdGenVdsl2ConfUsLp1MaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 44),
    _AdGenVdsl2ConfUsLp1MaxDelay_Type()
)
adGenVdsl2ConfUsLp1MaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1MaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1MaxDelay.setUnits("msec")


class _AdGenVdsl2ConfUsLp1MinProtection_Type(Unsigned32):
    """Custom type adGenVdsl2ConfUsLp1MinProtection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AdGenVdsl2ConfUsLp1MinProtection_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfUsLp1MinProtection_Object = MibTableColumn
adGenVdsl2ConfUsLp1MinProtection = _AdGenVdsl2ConfUsLp1MinProtection_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 45),
    _AdGenVdsl2ConfUsLp1MinProtection_Type()
)
adGenVdsl2ConfUsLp1MinProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1MinProtection.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1MinProtection.setUnits("0.5 Sym")


class _AdGenVdsl2ConfUsLp1RaRatio_Type(Integer32):
    """Custom type adGenVdsl2ConfUsLp1RaRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenVdsl2ConfUsLp1RaRatio_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsLp1RaRatio_Object = MibTableColumn
adGenVdsl2ConfUsLp1RaRatio = _AdGenVdsl2ConfUsLp1RaRatio_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 46),
    _AdGenVdsl2ConfUsLp1RaRatio_Type()
)
adGenVdsl2ConfUsLp1RaRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1RaRatio.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1RaRatio.setUnits("%")


class _AdGenVdsl2ConfUsLp1InitPolicy_Type(Integer32):
    """Custom type adGenVdsl2ConfUsLp1InitPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ndr", 0),
          ("inp", 1))
    )


_AdGenVdsl2ConfUsLp1InitPolicy_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsLp1InitPolicy_Object = MibTableColumn
adGenVdsl2ConfUsLp1InitPolicy = _AdGenVdsl2ConfUsLp1InitPolicy_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 47),
    _AdGenVdsl2ConfUsLp1InitPolicy_Type()
)
adGenVdsl2ConfUsLp1InitPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1InitPolicy.setStatus("current")


class _AdGenVdsl2ConfDsLp1MaxPayloadRate_Type(Unsigned32):
    """Custom type adGenVdsl2ConfDsLp1MaxPayloadRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 350000000),
    )


_AdGenVdsl2ConfDsLp1MaxPayloadRate_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfDsLp1MaxPayloadRate_Object = MibTableColumn
adGenVdsl2ConfDsLp1MaxPayloadRate = _AdGenVdsl2ConfDsLp1MaxPayloadRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 48),
    _AdGenVdsl2ConfDsLp1MaxPayloadRate_Type()
)
adGenVdsl2ConfDsLp1MaxPayloadRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1MaxPayloadRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1MaxPayloadRate.setUnits("bps")


class _AdGenVdsl2ConfDsLp1MinPayloadRate_Type(Unsigned32):
    """Custom type adGenVdsl2ConfDsLp1MinPayloadRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 350000000),
    )


_AdGenVdsl2ConfDsLp1MinPayloadRate_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfDsLp1MinPayloadRate_Object = MibTableColumn
adGenVdsl2ConfDsLp1MinPayloadRate = _AdGenVdsl2ConfDsLp1MinPayloadRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 49),
    _AdGenVdsl2ConfDsLp1MinPayloadRate_Type()
)
adGenVdsl2ConfDsLp1MinPayloadRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1MinPayloadRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1MinPayloadRate.setUnits("bps")


class _AdGenVdsl2ConfDsLp1MaxDelay_Type(Unsigned32):
    """Custom type adGenVdsl2ConfDsLp1MaxDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenVdsl2ConfDsLp1MaxDelay_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfDsLp1MaxDelay_Object = MibTableColumn
adGenVdsl2ConfDsLp1MaxDelay = _AdGenVdsl2ConfDsLp1MaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 50),
    _AdGenVdsl2ConfDsLp1MaxDelay_Type()
)
adGenVdsl2ConfDsLp1MaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1MaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1MaxDelay.setUnits("msec")


class _AdGenVdsl2ConfDsLp1MinProtection_Type(Unsigned32):
    """Custom type adGenVdsl2ConfDsLp1MinProtection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AdGenVdsl2ConfDsLp1MinProtection_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfDsLp1MinProtection_Object = MibTableColumn
adGenVdsl2ConfDsLp1MinProtection = _AdGenVdsl2ConfDsLp1MinProtection_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 51),
    _AdGenVdsl2ConfDsLp1MinProtection_Type()
)
adGenVdsl2ConfDsLp1MinProtection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1MinProtection.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1MinProtection.setUnits("0.5 Sym")


class _AdGenVdsl2ConfDsLp1RaRatio_Type(Integer32):
    """Custom type adGenVdsl2ConfDsLp1RaRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AdGenVdsl2ConfDsLp1RaRatio_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsLp1RaRatio_Object = MibTableColumn
adGenVdsl2ConfDsLp1RaRatio = _AdGenVdsl2ConfDsLp1RaRatio_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 52),
    _AdGenVdsl2ConfDsLp1RaRatio_Type()
)
adGenVdsl2ConfDsLp1RaRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1RaRatio.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1RaRatio.setUnits("%")


class _AdGenVdsl2ConfDsLp1InitPolicy_Type(Integer32):
    """Custom type adGenVdsl2ConfDsLp1InitPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ndr", 0),
          ("inp", 1))
    )


_AdGenVdsl2ConfDsLp1InitPolicy_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsLp1InitPolicy_Object = MibTableColumn
adGenVdsl2ConfDsLp1InitPolicy = _AdGenVdsl2ConfDsLp1InitPolicy_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 53),
    _AdGenVdsl2ConfDsLp1InitPolicy_Type()
)
adGenVdsl2ConfDsLp1InitPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1InitPolicy.setStatus("current")


class _AdGenVdsl2ConfUsLp0Type_Type(Integer32):
    """Custom type adGenVdsl2ConfUsLp0Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noChannel", 1),
          ("fastOnly", 2),
          ("interleavedOnly", 3))
    )


_AdGenVdsl2ConfUsLp0Type_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsLp0Type_Object = MibTableColumn
adGenVdsl2ConfUsLp0Type = _AdGenVdsl2ConfUsLp0Type_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 54),
    _AdGenVdsl2ConfUsLp0Type_Type()
)
adGenVdsl2ConfUsLp0Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0Type.setStatus("current")


class _AdGenVdsl2ConfDsLp0Type_Type(Integer32):
    """Custom type adGenVdsl2ConfDsLp0Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noChannel", 1),
          ("fastOnly", 2),
          ("interleavedOnly", 3))
    )


_AdGenVdsl2ConfDsLp0Type_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsLp0Type_Object = MibTableColumn
adGenVdsl2ConfDsLp0Type = _AdGenVdsl2ConfDsLp0Type_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 55),
    _AdGenVdsl2ConfDsLp0Type_Type()
)
adGenVdsl2ConfDsLp0Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0Type.setStatus("current")


class _AdGenVdsl2ConfUsLp1Type_Type(Integer32):
    """Custom type adGenVdsl2ConfUsLp1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noChannel", 1),
          ("fastOnly", 2),
          ("interleavedOnly", 3))
    )


_AdGenVdsl2ConfUsLp1Type_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsLp1Type_Object = MibTableColumn
adGenVdsl2ConfUsLp1Type = _AdGenVdsl2ConfUsLp1Type_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 56),
    _AdGenVdsl2ConfUsLp1Type_Type()
)
adGenVdsl2ConfUsLp1Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1Type.setStatus("current")


class _AdGenVdsl2ConfDsLp1Type_Type(Integer32):
    """Custom type adGenVdsl2ConfDsLp1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noChannel", 1),
          ("fastOnly", 2),
          ("interleavedOnly", 3))
    )


_AdGenVdsl2ConfDsLp1Type_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsLp1Type_Object = MibTableColumn
adGenVdsl2ConfDsLp1Type = _AdGenVdsl2ConfDsLp1Type_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 57),
    _AdGenVdsl2ConfDsLp1Type_Type()
)
adGenVdsl2ConfDsLp1Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1Type.setStatus("current")


class _AdGenVdsl2ConfUsRateMode_Type(Integer32):
    """Custom type adGenVdsl2ConfUsRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("adaptAtStartup", 2),
          ("adaptAtRuntime", 3))
    )


_AdGenVdsl2ConfUsRateMode_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsRateMode_Object = MibTableColumn
adGenVdsl2ConfUsRateMode = _AdGenVdsl2ConfUsRateMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 58),
    _AdGenVdsl2ConfUsRateMode_Type()
)
adGenVdsl2ConfUsRateMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsRateMode.setStatus("current")


class _AdGenVdsl2ConfUsCustomPboElecLenKL_Type(Integer32):
    """Custom type adGenVdsl2ConfUsCustomPboElecLenKL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1280),
    )


_AdGenVdsl2ConfUsCustomPboElecLenKL_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsCustomPboElecLenKL_Object = MibTableColumn
adGenVdsl2ConfUsCustomPboElecLenKL = _AdGenVdsl2ConfUsCustomPboElecLenKL_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 59),
    _AdGenVdsl2ConfUsCustomPboElecLenKL_Type()
)
adGenVdsl2ConfUsCustomPboElecLenKL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsCustomPboElecLenKL.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsCustomPboElecLenKL.setUnits("0.1 dB")


class _AdGenVdsl2ConfUsCustomPboForceLen_Type(Integer32):
    """Custom type adGenVdsl2ConfUsCustomPboForceLen based on Integer32"""
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


_AdGenVdsl2ConfUsCustomPboForceLen_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsCustomPboForceLen_Object = MibTableColumn
adGenVdsl2ConfUsCustomPboForceLen = _AdGenVdsl2ConfUsCustomPboForceLen_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 60),
    _AdGenVdsl2ConfUsCustomPboForceLen_Type()
)
adGenVdsl2ConfUsCustomPboForceLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsCustomPboForceLen.setStatus("current")


class _AdGenVdsl2ConfUsCustomPboBoostMode_Type(Integer32):
    """Custom type adGenVdsl2ConfUsCustomPboBoostMode based on Integer32"""
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


_AdGenVdsl2ConfUsCustomPboBoostMode_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsCustomPboBoostMode_Object = MibTableColumn
adGenVdsl2ConfUsCustomPboBoostMode = _AdGenVdsl2ConfUsCustomPboBoostMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 61),
    _AdGenVdsl2ConfUsCustomPboBoostMode_Type()
)
adGenVdsl2ConfUsCustomPboBoostMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsCustomPboBoostMode.setStatus("current")


class _AdGenVdsl2ConfDsCustomPboElecLen_Type(Integer32):
    """Custom type adGenVdsl2ConfDsCustomPboElecLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2555),
    )


_AdGenVdsl2ConfDsCustomPboElecLen_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsCustomPboElecLen_Object = MibTableColumn
adGenVdsl2ConfDsCustomPboElecLen = _AdGenVdsl2ConfDsCustomPboElecLen_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 62),
    _AdGenVdsl2ConfDsCustomPboElecLen_Type()
)
adGenVdsl2ConfDsCustomPboElecLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsCustomPboElecLen.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsCustomPboElecLen.setUnits("0.1 dB")


class _AdGenVdsl2ConfDsCustomPboCableA_Type(Integer32):
    """Custom type adGenVdsl2ConfDsCustomPboCableA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 640),
    )


_AdGenVdsl2ConfDsCustomPboCableA_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsCustomPboCableA_Object = MibTableColumn
adGenVdsl2ConfDsCustomPboCableA = _AdGenVdsl2ConfDsCustomPboCableA_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 63),
    _AdGenVdsl2ConfDsCustomPboCableA_Type()
)
adGenVdsl2ConfDsCustomPboCableA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsCustomPboCableA.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsCustomPboCableA.setUnits("scalar")


class _AdGenVdsl2ConfDsCustomPboCableB_Type(Integer32):
    """Custom type adGenVdsl2ConfDsCustomPboCableB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 640),
    )


_AdGenVdsl2ConfDsCustomPboCableB_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsCustomPboCableB_Object = MibTableColumn
adGenVdsl2ConfDsCustomPboCableB = _AdGenVdsl2ConfDsCustomPboCableB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 64),
    _AdGenVdsl2ConfDsCustomPboCableB_Type()
)
adGenVdsl2ConfDsCustomPboCableB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsCustomPboCableB.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsCustomPboCableB.setUnits("scalar")


class _AdGenVdsl2ConfDsCustomPboCableC_Type(Integer32):
    """Custom type adGenVdsl2ConfDsCustomPboCableC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 640),
    )


_AdGenVdsl2ConfDsCustomPboCableC_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsCustomPboCableC_Object = MibTableColumn
adGenVdsl2ConfDsCustomPboCableC = _AdGenVdsl2ConfDsCustomPboCableC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 65),
    _AdGenVdsl2ConfDsCustomPboCableC_Type()
)
adGenVdsl2ConfDsCustomPboCableC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsCustomPboCableC.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsCustomPboCableC.setUnits("scalar")


class _AdGenVdsl2ConfDsCustomPboMinSignal_Type(Integer32):
    """Custom type adGenVdsl2ConfDsCustomPboMinSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1275),
    )


_AdGenVdsl2ConfDsCustomPboMinSignal_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsCustomPboMinSignal_Object = MibTableColumn
adGenVdsl2ConfDsCustomPboMinSignal = _AdGenVdsl2ConfDsCustomPboMinSignal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 66),
    _AdGenVdsl2ConfDsCustomPboMinSignal_Type()
)
adGenVdsl2ConfDsCustomPboMinSignal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsCustomPboMinSignal.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsCustomPboMinSignal.setUnits("0.1 dB")


class _AdGenVdsl2ConfDsCustomPboMinFreq_Type(Integer32):
    """Custom type adGenVdsl2ConfDsCustomPboMinFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_AdGenVdsl2ConfDsCustomPboMinFreq_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsCustomPboMinFreq_Object = MibTableColumn
adGenVdsl2ConfDsCustomPboMinFreq = _AdGenVdsl2ConfDsCustomPboMinFreq_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 67),
    _AdGenVdsl2ConfDsCustomPboMinFreq_Type()
)
adGenVdsl2ConfDsCustomPboMinFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsCustomPboMinFreq.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsCustomPboMinFreq.setUnits("4.3125kHz tones")


class _AdGenVdsl2ConfDsCustomPboMaxFreq_Type(Integer32):
    """Custom type adGenVdsl2ConfDsCustomPboMaxFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 4095),
    )


_AdGenVdsl2ConfDsCustomPboMaxFreq_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsCustomPboMaxFreq_Object = MibTableColumn
adGenVdsl2ConfDsCustomPboMaxFreq = _AdGenVdsl2ConfDsCustomPboMaxFreq_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 68),
    _AdGenVdsl2ConfDsCustomPboMaxFreq_Type()
)
adGenVdsl2ConfDsCustomPboMaxFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsCustomPboMaxFreq.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsCustomPboMaxFreq.setUnits("4.3125kHz tones")


class _AdGenVdsl2ConfAnfpCalValue_Type(Integer32):
    """Custom type adGenVdsl2ConfAnfpCalValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_AdGenVdsl2ConfAnfpCalValue_Type.__name__ = "Integer32"
_AdGenVdsl2ConfAnfpCalValue_Object = MibTableColumn
adGenVdsl2ConfAnfpCalValue = _AdGenVdsl2ConfAnfpCalValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 69),
    _AdGenVdsl2ConfAnfpCalValue_Type()
)
adGenVdsl2ConfAnfpCalValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfAnfpCalValue.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfAnfpCalValue.setUnits("dB")


class _AdGenVdsl2ConfDsDownshiftSnrMgn_Type(Integer32):
    """Custom type adGenVdsl2ConfDsDownshiftSnrMgn based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_AdGenVdsl2ConfDsDownshiftSnrMgn_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsDownshiftSnrMgn_Object = MibTableColumn
adGenVdsl2ConfDsDownshiftSnrMgn = _AdGenVdsl2ConfDsDownshiftSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 70),
    _AdGenVdsl2ConfDsDownshiftSnrMgn_Type()
)
adGenVdsl2ConfDsDownshiftSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsDownshiftSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsDownshiftSnrMgn.setUnits("tenth dB")


class _AdGenVdsl2ConfDsUpshiftSnrMgn_Type(Integer32):
    """Custom type adGenVdsl2ConfDsUpshiftSnrMgn based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_AdGenVdsl2ConfDsUpshiftSnrMgn_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsUpshiftSnrMgn_Object = MibTableColumn
adGenVdsl2ConfDsUpshiftSnrMgn = _AdGenVdsl2ConfDsUpshiftSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 71),
    _AdGenVdsl2ConfDsUpshiftSnrMgn_Type()
)
adGenVdsl2ConfDsUpshiftSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsUpshiftSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsUpshiftSnrMgn.setUnits("tenth dB")


class _AdGenVdsl2ConfDsMinUpshiftTime_Type(Unsigned32):
    """Custom type adGenVdsl2ConfDsMinUpshiftTime based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_AdGenVdsl2ConfDsMinUpshiftTime_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfDsMinUpshiftTime_Object = MibTableColumn
adGenVdsl2ConfDsMinUpshiftTime = _AdGenVdsl2ConfDsMinUpshiftTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 72),
    _AdGenVdsl2ConfDsMinUpshiftTime_Type()
)
adGenVdsl2ConfDsMinUpshiftTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsMinUpshiftTime.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsMinUpshiftTime.setUnits("seconds")


class _AdGenVdsl2ConfDsMinDownshiftTime_Type(Unsigned32):
    """Custom type adGenVdsl2ConfDsMinDownshiftTime based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_AdGenVdsl2ConfDsMinDownshiftTime_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfDsMinDownshiftTime_Object = MibTableColumn
adGenVdsl2ConfDsMinDownshiftTime = _AdGenVdsl2ConfDsMinDownshiftTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 73),
    _AdGenVdsl2ConfDsMinDownshiftTime_Type()
)
adGenVdsl2ConfDsMinDownshiftTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsMinDownshiftTime.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsMinDownshiftTime.setUnits("seconds")


class _AdGenVdsl2ConfUsDownshiftSnrMgn_Type(Integer32):
    """Custom type adGenVdsl2ConfUsDownshiftSnrMgn based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_AdGenVdsl2ConfUsDownshiftSnrMgn_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsDownshiftSnrMgn_Object = MibTableColumn
adGenVdsl2ConfUsDownshiftSnrMgn = _AdGenVdsl2ConfUsDownshiftSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 74),
    _AdGenVdsl2ConfUsDownshiftSnrMgn_Type()
)
adGenVdsl2ConfUsDownshiftSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsDownshiftSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsDownshiftSnrMgn.setUnits("tenth dB")


class _AdGenVdsl2ConfUsUpshiftSnrMgn_Type(Integer32):
    """Custom type adGenVdsl2ConfUsUpshiftSnrMgn based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_AdGenVdsl2ConfUsUpshiftSnrMgn_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsUpshiftSnrMgn_Object = MibTableColumn
adGenVdsl2ConfUsUpshiftSnrMgn = _AdGenVdsl2ConfUsUpshiftSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 75),
    _AdGenVdsl2ConfUsUpshiftSnrMgn_Type()
)
adGenVdsl2ConfUsUpshiftSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsUpshiftSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsUpshiftSnrMgn.setUnits("tenth dB")


class _AdGenVdsl2ConfUsMinUpshiftTime_Type(Unsigned32):
    """Custom type adGenVdsl2ConfUsMinUpshiftTime based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_AdGenVdsl2ConfUsMinUpshiftTime_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfUsMinUpshiftTime_Object = MibTableColumn
adGenVdsl2ConfUsMinUpshiftTime = _AdGenVdsl2ConfUsMinUpshiftTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 76),
    _AdGenVdsl2ConfUsMinUpshiftTime_Type()
)
adGenVdsl2ConfUsMinUpshiftTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsMinUpshiftTime.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsMinUpshiftTime.setUnits("seconds")


class _AdGenVdsl2ConfUsMinDownshiftTime_Type(Unsigned32):
    """Custom type adGenVdsl2ConfUsMinDownshiftTime based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_AdGenVdsl2ConfUsMinDownshiftTime_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfUsMinDownshiftTime_Object = MibTableColumn
adGenVdsl2ConfUsMinDownshiftTime = _AdGenVdsl2ConfUsMinDownshiftTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 77),
    _AdGenVdsl2ConfUsMinDownshiftTime_Type()
)
adGenVdsl2ConfUsMinDownshiftTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsMinDownshiftTime.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsMinDownshiftTime.setUnits("seconds")


class _AdGenVdsl2ConfUsLp0RtxSetting_Type(Integer32):
    """Custom type adGenVdsl2ConfUsLp0RtxSetting based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              255)
        )
    )
    namedValues = NamedValues(
        *(("rtxOff", 0),
          ("rtxCustom", 255))
    )


_AdGenVdsl2ConfUsLp0RtxSetting_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsLp0RtxSetting_Object = MibTableColumn
adGenVdsl2ConfUsLp0RtxSetting = _AdGenVdsl2ConfUsLp0RtxSetting_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 78),
    _AdGenVdsl2ConfUsLp0RtxSetting_Type()
)
adGenVdsl2ConfUsLp0RtxSetting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0RtxSetting.setStatus("current")


class _AdGenVdsl2ConfUsLp0CustomRtxMaxNdr_Type(Unsigned32):
    """Custom type adGenVdsl2ConfUsLp0CustomRtxMaxNdr based on Unsigned32"""
    defaultValue = 50000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96000000),
    )


_AdGenVdsl2ConfUsLp0CustomRtxMaxNdr_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfUsLp0CustomRtxMaxNdr_Object = MibTableColumn
adGenVdsl2ConfUsLp0CustomRtxMaxNdr = _AdGenVdsl2ConfUsLp0CustomRtxMaxNdr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 79),
    _AdGenVdsl2ConfUsLp0CustomRtxMaxNdr_Type()
)
adGenVdsl2ConfUsLp0CustomRtxMaxNdr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0CustomRtxMaxNdr.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0CustomRtxMaxNdr.setUnits("bps")


class _AdGenVdsl2ConfUsLp0CustomRtxMinDelay_Type(Integer32):
    """Custom type adGenVdsl2ConfUsLp0CustomRtxMinDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenVdsl2ConfUsLp0CustomRtxMinDelay_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsLp0CustomRtxMinDelay_Object = MibTableColumn
adGenVdsl2ConfUsLp0CustomRtxMinDelay = _AdGenVdsl2ConfUsLp0CustomRtxMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 80),
    _AdGenVdsl2ConfUsLp0CustomRtxMinDelay_Type()
)
adGenVdsl2ConfUsLp0CustomRtxMinDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0CustomRtxMinDelay.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0CustomRtxMinDelay.setUnits("ms")


class _AdGenVdsl2ConfUsLp0CustomRtxMaxDelay_Type(Integer32):
    """Custom type adGenVdsl2ConfUsLp0CustomRtxMaxDelay based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_AdGenVdsl2ConfUsLp0CustomRtxMaxDelay_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsLp0CustomRtxMaxDelay_Object = MibTableColumn
adGenVdsl2ConfUsLp0CustomRtxMaxDelay = _AdGenVdsl2ConfUsLp0CustomRtxMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 81),
    _AdGenVdsl2ConfUsLp0CustomRtxMaxDelay_Type()
)
adGenVdsl2ConfUsLp0CustomRtxMaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0CustomRtxMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0CustomRtxMaxDelay.setUnits("ms")


class _AdGenVdsl2ConfUsLp0CustomRtxInpMinShine_Type(Integer32):
    """Custom type adGenVdsl2ConfUsLp0CustomRtxInpMinShine based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenVdsl2ConfUsLp0CustomRtxInpMinShine_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsLp0CustomRtxInpMinShine_Object = MibTableColumn
adGenVdsl2ConfUsLp0CustomRtxInpMinShine = _AdGenVdsl2ConfUsLp0CustomRtxInpMinShine_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 82),
    _AdGenVdsl2ConfUsLp0CustomRtxInpMinShine_Type()
)
adGenVdsl2ConfUsLp0CustomRtxInpMinShine.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0CustomRtxInpMinShine.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0CustomRtxInpMinShine.setUnits("DMT symbols")


class _AdGenVdsl2ConfUsLp0CustomRtxInpMinRein_Type(Integer32):
    """Custom type adGenVdsl2ConfUsLp0CustomRtxInpMinRein based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenVdsl2ConfUsLp0CustomRtxInpMinRein_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsLp0CustomRtxInpMinRein_Object = MibTableColumn
adGenVdsl2ConfUsLp0CustomRtxInpMinRein = _AdGenVdsl2ConfUsLp0CustomRtxInpMinRein_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 83),
    _AdGenVdsl2ConfUsLp0CustomRtxInpMinRein_Type()
)
adGenVdsl2ConfUsLp0CustomRtxInpMinRein.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0CustomRtxInpMinRein.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0CustomRtxInpMinRein.setUnits("DMT symbols")


class _AdGenVdsl2ConfUsLp0CustomRtxIatRein_Type(Integer32):
    """Custom type adGenVdsl2ConfUsLp0CustomRtxIatRein based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtxRein100Hz", 1),
          ("rtxRein120Hz", 2))
    )


_AdGenVdsl2ConfUsLp0CustomRtxIatRein_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsLp0CustomRtxIatRein_Object = MibTableColumn
adGenVdsl2ConfUsLp0CustomRtxIatRein = _AdGenVdsl2ConfUsLp0CustomRtxIatRein_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 84),
    _AdGenVdsl2ConfUsLp0CustomRtxIatRein_Type()
)
adGenVdsl2ConfUsLp0CustomRtxIatRein.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0CustomRtxIatRein.setStatus("current")


class _AdGenVdsl2ConfUsLp0CustomRtxLeftrThresh_Type(Integer32):
    """Custom type adGenVdsl2ConfUsLp0CustomRtxLeftrThresh based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AdGenVdsl2ConfUsLp0CustomRtxLeftrThresh_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsLp0CustomRtxLeftrThresh_Object = MibTableColumn
adGenVdsl2ConfUsLp0CustomRtxLeftrThresh = _AdGenVdsl2ConfUsLp0CustomRtxLeftrThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 85),
    _AdGenVdsl2ConfUsLp0CustomRtxLeftrThresh_Type()
)
adGenVdsl2ConfUsLp0CustomRtxLeftrThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0CustomRtxLeftrThresh.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp0CustomRtxLeftrThresh.setUnits("Percent of NDR")


class _AdGenVdsl2ConfDsLp0RtxSetting_Type(Integer32):
    """Custom type adGenVdsl2ConfDsLp0RtxSetting based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              255)
        )
    )
    namedValues = NamedValues(
        *(("rtxOff", 0),
          ("rtxCustom", 255))
    )


_AdGenVdsl2ConfDsLp0RtxSetting_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsLp0RtxSetting_Object = MibTableColumn
adGenVdsl2ConfDsLp0RtxSetting = _AdGenVdsl2ConfDsLp0RtxSetting_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 86),
    _AdGenVdsl2ConfDsLp0RtxSetting_Type()
)
adGenVdsl2ConfDsLp0RtxSetting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0RtxSetting.setStatus("current")


class _AdGenVdsl2ConfDsLp0CustomRtxMaxNdr_Type(Unsigned32):
    """Custom type adGenVdsl2ConfDsLp0CustomRtxMaxNdr based on Unsigned32"""
    defaultValue = 100000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 350000000),
    )


_AdGenVdsl2ConfDsLp0CustomRtxMaxNdr_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfDsLp0CustomRtxMaxNdr_Object = MibTableColumn
adGenVdsl2ConfDsLp0CustomRtxMaxNdr = _AdGenVdsl2ConfDsLp0CustomRtxMaxNdr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 87),
    _AdGenVdsl2ConfDsLp0CustomRtxMaxNdr_Type()
)
adGenVdsl2ConfDsLp0CustomRtxMaxNdr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0CustomRtxMaxNdr.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0CustomRtxMaxNdr.setUnits("bps")


class _AdGenVdsl2ConfDsLp0CustomRtxMinDelay_Type(Integer32):
    """Custom type adGenVdsl2ConfDsLp0CustomRtxMinDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenVdsl2ConfDsLp0CustomRtxMinDelay_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsLp0CustomRtxMinDelay_Object = MibTableColumn
adGenVdsl2ConfDsLp0CustomRtxMinDelay = _AdGenVdsl2ConfDsLp0CustomRtxMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 88),
    _AdGenVdsl2ConfDsLp0CustomRtxMinDelay_Type()
)
adGenVdsl2ConfDsLp0CustomRtxMinDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0CustomRtxMinDelay.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0CustomRtxMinDelay.setUnits("ms")


class _AdGenVdsl2ConfDsLp0CustomRtxMaxDelay_Type(Integer32):
    """Custom type adGenVdsl2ConfDsLp0CustomRtxMaxDelay based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_AdGenVdsl2ConfDsLp0CustomRtxMaxDelay_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsLp0CustomRtxMaxDelay_Object = MibTableColumn
adGenVdsl2ConfDsLp0CustomRtxMaxDelay = _AdGenVdsl2ConfDsLp0CustomRtxMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 89),
    _AdGenVdsl2ConfDsLp0CustomRtxMaxDelay_Type()
)
adGenVdsl2ConfDsLp0CustomRtxMaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0CustomRtxMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0CustomRtxMaxDelay.setUnits("ms")


class _AdGenVdsl2ConfDsLp0CustomRtxInpMinShine_Type(Integer32):
    """Custom type adGenVdsl2ConfDsLp0CustomRtxInpMinShine based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenVdsl2ConfDsLp0CustomRtxInpMinShine_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsLp0CustomRtxInpMinShine_Object = MibTableColumn
adGenVdsl2ConfDsLp0CustomRtxInpMinShine = _AdGenVdsl2ConfDsLp0CustomRtxInpMinShine_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 90),
    _AdGenVdsl2ConfDsLp0CustomRtxInpMinShine_Type()
)
adGenVdsl2ConfDsLp0CustomRtxInpMinShine.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0CustomRtxInpMinShine.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0CustomRtxInpMinShine.setUnits("DMT symbols")


class _AdGenVdsl2ConfDsLp0CustomRtxInpMinRein_Type(Integer32):
    """Custom type adGenVdsl2ConfDsLp0CustomRtxInpMinRein based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenVdsl2ConfDsLp0CustomRtxInpMinRein_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsLp0CustomRtxInpMinRein_Object = MibTableColumn
adGenVdsl2ConfDsLp0CustomRtxInpMinRein = _AdGenVdsl2ConfDsLp0CustomRtxInpMinRein_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 91),
    _AdGenVdsl2ConfDsLp0CustomRtxInpMinRein_Type()
)
adGenVdsl2ConfDsLp0CustomRtxInpMinRein.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0CustomRtxInpMinRein.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0CustomRtxInpMinRein.setUnits("DMT symbols")


class _AdGenVdsl2ConfDsLp0CustomRtxIatRein_Type(Integer32):
    """Custom type adGenVdsl2ConfDsLp0CustomRtxIatRein based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtxRein100Hz", 1),
          ("rtxRein120Hz", 2))
    )


_AdGenVdsl2ConfDsLp0CustomRtxIatRein_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsLp0CustomRtxIatRein_Object = MibTableColumn
adGenVdsl2ConfDsLp0CustomRtxIatRein = _AdGenVdsl2ConfDsLp0CustomRtxIatRein_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 92),
    _AdGenVdsl2ConfDsLp0CustomRtxIatRein_Type()
)
adGenVdsl2ConfDsLp0CustomRtxIatRein.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0CustomRtxIatRein.setStatus("current")


class _AdGenVdsl2ConfDsLp0CustomRtxLeftrThresh_Type(Integer32):
    """Custom type adGenVdsl2ConfDsLp0CustomRtxLeftrThresh based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AdGenVdsl2ConfDsLp0CustomRtxLeftrThresh_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsLp0CustomRtxLeftrThresh_Object = MibTableColumn
adGenVdsl2ConfDsLp0CustomRtxLeftrThresh = _AdGenVdsl2ConfDsLp0CustomRtxLeftrThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 93),
    _AdGenVdsl2ConfDsLp0CustomRtxLeftrThresh_Type()
)
adGenVdsl2ConfDsLp0CustomRtxLeftrThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0CustomRtxLeftrThresh.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp0CustomRtxLeftrThresh.setUnits("Percent of NDR")


class _AdGenVdsl2ConfUsLp1RtxSetting_Type(Integer32):
    """Custom type adGenVdsl2ConfUsLp1RtxSetting based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              255)
        )
    )
    namedValues = NamedValues(
        *(("rtxOff", 0),
          ("rtxCustom", 255))
    )


_AdGenVdsl2ConfUsLp1RtxSetting_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsLp1RtxSetting_Object = MibTableColumn
adGenVdsl2ConfUsLp1RtxSetting = _AdGenVdsl2ConfUsLp1RtxSetting_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 94),
    _AdGenVdsl2ConfUsLp1RtxSetting_Type()
)
adGenVdsl2ConfUsLp1RtxSetting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1RtxSetting.setStatus("current")


class _AdGenVdsl2ConfUsLp1CustomRtxMaxNdr_Type(Unsigned32):
    """Custom type adGenVdsl2ConfUsLp1CustomRtxMaxNdr based on Unsigned32"""
    defaultValue = 50000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96000000),
    )


_AdGenVdsl2ConfUsLp1CustomRtxMaxNdr_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfUsLp1CustomRtxMaxNdr_Object = MibTableColumn
adGenVdsl2ConfUsLp1CustomRtxMaxNdr = _AdGenVdsl2ConfUsLp1CustomRtxMaxNdr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 95),
    _AdGenVdsl2ConfUsLp1CustomRtxMaxNdr_Type()
)
adGenVdsl2ConfUsLp1CustomRtxMaxNdr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1CustomRtxMaxNdr.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1CustomRtxMaxNdr.setUnits("bps")


class _AdGenVdsl2ConfUsLp1CustomRtxMinDelay_Type(Integer32):
    """Custom type adGenVdsl2ConfUsLp1CustomRtxMinDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenVdsl2ConfUsLp1CustomRtxMinDelay_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsLp1CustomRtxMinDelay_Object = MibTableColumn
adGenVdsl2ConfUsLp1CustomRtxMinDelay = _AdGenVdsl2ConfUsLp1CustomRtxMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 96),
    _AdGenVdsl2ConfUsLp1CustomRtxMinDelay_Type()
)
adGenVdsl2ConfUsLp1CustomRtxMinDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1CustomRtxMinDelay.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1CustomRtxMinDelay.setUnits("ms")


class _AdGenVdsl2ConfUsLp1CustomRtxMaxDelay_Type(Integer32):
    """Custom type adGenVdsl2ConfUsLp1CustomRtxMaxDelay based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_AdGenVdsl2ConfUsLp1CustomRtxMaxDelay_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsLp1CustomRtxMaxDelay_Object = MibTableColumn
adGenVdsl2ConfUsLp1CustomRtxMaxDelay = _AdGenVdsl2ConfUsLp1CustomRtxMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 97),
    _AdGenVdsl2ConfUsLp1CustomRtxMaxDelay_Type()
)
adGenVdsl2ConfUsLp1CustomRtxMaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1CustomRtxMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1CustomRtxMaxDelay.setUnits("ms")


class _AdGenVdsl2ConfUsLp1CustomRtxInpMinShine_Type(Integer32):
    """Custom type adGenVdsl2ConfUsLp1CustomRtxInpMinShine based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenVdsl2ConfUsLp1CustomRtxInpMinShine_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsLp1CustomRtxInpMinShine_Object = MibTableColumn
adGenVdsl2ConfUsLp1CustomRtxInpMinShine = _AdGenVdsl2ConfUsLp1CustomRtxInpMinShine_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 98),
    _AdGenVdsl2ConfUsLp1CustomRtxInpMinShine_Type()
)
adGenVdsl2ConfUsLp1CustomRtxInpMinShine.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1CustomRtxInpMinShine.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1CustomRtxInpMinShine.setUnits("DMT symbols")


class _AdGenVdsl2ConfUsLp1CustomRtxInpMinRein_Type(Integer32):
    """Custom type adGenVdsl2ConfUsLp1CustomRtxInpMinRein based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenVdsl2ConfUsLp1CustomRtxInpMinRein_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsLp1CustomRtxInpMinRein_Object = MibTableColumn
adGenVdsl2ConfUsLp1CustomRtxInpMinRein = _AdGenVdsl2ConfUsLp1CustomRtxInpMinRein_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 99),
    _AdGenVdsl2ConfUsLp1CustomRtxInpMinRein_Type()
)
adGenVdsl2ConfUsLp1CustomRtxInpMinRein.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1CustomRtxInpMinRein.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1CustomRtxInpMinRein.setUnits("DMT symbols")


class _AdGenVdsl2ConfUsLp1CustomRtxIatRein_Type(Integer32):
    """Custom type adGenVdsl2ConfUsLp1CustomRtxIatRein based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtxRein100Hz", 1),
          ("rtxRein120Hz", 2))
    )


_AdGenVdsl2ConfUsLp1CustomRtxIatRein_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsLp1CustomRtxIatRein_Object = MibTableColumn
adGenVdsl2ConfUsLp1CustomRtxIatRein = _AdGenVdsl2ConfUsLp1CustomRtxIatRein_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 100),
    _AdGenVdsl2ConfUsLp1CustomRtxIatRein_Type()
)
adGenVdsl2ConfUsLp1CustomRtxIatRein.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1CustomRtxIatRein.setStatus("current")


class _AdGenVdsl2ConfUsLp1CustomRtxLeftrThresh_Type(Integer32):
    """Custom type adGenVdsl2ConfUsLp1CustomRtxLeftrThresh based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AdGenVdsl2ConfUsLp1CustomRtxLeftrThresh_Type.__name__ = "Integer32"
_AdGenVdsl2ConfUsLp1CustomRtxLeftrThresh_Object = MibTableColumn
adGenVdsl2ConfUsLp1CustomRtxLeftrThresh = _AdGenVdsl2ConfUsLp1CustomRtxLeftrThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 101),
    _AdGenVdsl2ConfUsLp1CustomRtxLeftrThresh_Type()
)
adGenVdsl2ConfUsLp1CustomRtxLeftrThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1CustomRtxLeftrThresh.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfUsLp1CustomRtxLeftrThresh.setUnits("Percent of NDR")


class _AdGenVdsl2ConfDsLp1RtxSetting_Type(Integer32):
    """Custom type adGenVdsl2ConfDsLp1RtxSetting based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              255)
        )
    )
    namedValues = NamedValues(
        *(("rtxOff", 0),
          ("rtxCustom", 255))
    )


_AdGenVdsl2ConfDsLp1RtxSetting_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsLp1RtxSetting_Object = MibTableColumn
adGenVdsl2ConfDsLp1RtxSetting = _AdGenVdsl2ConfDsLp1RtxSetting_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 102),
    _AdGenVdsl2ConfDsLp1RtxSetting_Type()
)
adGenVdsl2ConfDsLp1RtxSetting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1RtxSetting.setStatus("current")


class _AdGenVdsl2ConfDsLp1CustomRtxMaxNdr_Type(Unsigned32):
    """Custom type adGenVdsl2ConfDsLp1CustomRtxMaxNdr based on Unsigned32"""
    defaultValue = 100000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 350000000),
    )


_AdGenVdsl2ConfDsLp1CustomRtxMaxNdr_Type.__name__ = "Unsigned32"
_AdGenVdsl2ConfDsLp1CustomRtxMaxNdr_Object = MibTableColumn
adGenVdsl2ConfDsLp1CustomRtxMaxNdr = _AdGenVdsl2ConfDsLp1CustomRtxMaxNdr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 103),
    _AdGenVdsl2ConfDsLp1CustomRtxMaxNdr_Type()
)
adGenVdsl2ConfDsLp1CustomRtxMaxNdr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1CustomRtxMaxNdr.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1CustomRtxMaxNdr.setUnits("bps")


class _AdGenVdsl2ConfDsLp1CustomRtxMinDelay_Type(Integer32):
    """Custom type adGenVdsl2ConfDsLp1CustomRtxMinDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenVdsl2ConfDsLp1CustomRtxMinDelay_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsLp1CustomRtxMinDelay_Object = MibTableColumn
adGenVdsl2ConfDsLp1CustomRtxMinDelay = _AdGenVdsl2ConfDsLp1CustomRtxMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 104),
    _AdGenVdsl2ConfDsLp1CustomRtxMinDelay_Type()
)
adGenVdsl2ConfDsLp1CustomRtxMinDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1CustomRtxMinDelay.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1CustomRtxMinDelay.setUnits("ms")


class _AdGenVdsl2ConfDsLp1CustomRtxMaxDelay_Type(Integer32):
    """Custom type adGenVdsl2ConfDsLp1CustomRtxMaxDelay based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_AdGenVdsl2ConfDsLp1CustomRtxMaxDelay_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsLp1CustomRtxMaxDelay_Object = MibTableColumn
adGenVdsl2ConfDsLp1CustomRtxMaxDelay = _AdGenVdsl2ConfDsLp1CustomRtxMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 105),
    _AdGenVdsl2ConfDsLp1CustomRtxMaxDelay_Type()
)
adGenVdsl2ConfDsLp1CustomRtxMaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1CustomRtxMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1CustomRtxMaxDelay.setUnits("ms")


class _AdGenVdsl2ConfDsLp1CustomRtxInpMinShine_Type(Integer32):
    """Custom type adGenVdsl2ConfDsLp1CustomRtxInpMinShine based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenVdsl2ConfDsLp1CustomRtxInpMinShine_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsLp1CustomRtxInpMinShine_Object = MibTableColumn
adGenVdsl2ConfDsLp1CustomRtxInpMinShine = _AdGenVdsl2ConfDsLp1CustomRtxInpMinShine_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 106),
    _AdGenVdsl2ConfDsLp1CustomRtxInpMinShine_Type()
)
adGenVdsl2ConfDsLp1CustomRtxInpMinShine.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1CustomRtxInpMinShine.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1CustomRtxInpMinShine.setUnits("DMT symbols")


class _AdGenVdsl2ConfDsLp1CustomRtxInpMinRein_Type(Integer32):
    """Custom type adGenVdsl2ConfDsLp1CustomRtxInpMinRein based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenVdsl2ConfDsLp1CustomRtxInpMinRein_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsLp1CustomRtxInpMinRein_Object = MibTableColumn
adGenVdsl2ConfDsLp1CustomRtxInpMinRein = _AdGenVdsl2ConfDsLp1CustomRtxInpMinRein_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 107),
    _AdGenVdsl2ConfDsLp1CustomRtxInpMinRein_Type()
)
adGenVdsl2ConfDsLp1CustomRtxInpMinRein.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1CustomRtxInpMinRein.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1CustomRtxInpMinRein.setUnits("DMT symbols")


class _AdGenVdsl2ConfDsLp1CustomRtxIatRein_Type(Integer32):
    """Custom type adGenVdsl2ConfDsLp1CustomRtxIatRein based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rtxRein100Hz", 1),
          ("rtxRein120Hz", 2))
    )


_AdGenVdsl2ConfDsLp1CustomRtxIatRein_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsLp1CustomRtxIatRein_Object = MibTableColumn
adGenVdsl2ConfDsLp1CustomRtxIatRein = _AdGenVdsl2ConfDsLp1CustomRtxIatRein_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 108),
    _AdGenVdsl2ConfDsLp1CustomRtxIatRein_Type()
)
adGenVdsl2ConfDsLp1CustomRtxIatRein.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1CustomRtxIatRein.setStatus("current")


class _AdGenVdsl2ConfDsLp1CustomRtxLeftrThresh_Type(Integer32):
    """Custom type adGenVdsl2ConfDsLp1CustomRtxLeftrThresh based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AdGenVdsl2ConfDsLp1CustomRtxLeftrThresh_Type.__name__ = "Integer32"
_AdGenVdsl2ConfDsLp1CustomRtxLeftrThresh_Object = MibTableColumn
adGenVdsl2ConfDsLp1CustomRtxLeftrThresh = _AdGenVdsl2ConfDsLp1CustomRtxLeftrThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 109),
    _AdGenVdsl2ConfDsLp1CustomRtxLeftrThresh_Type()
)
adGenVdsl2ConfDsLp1CustomRtxLeftrThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1CustomRtxLeftrThresh.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfDsLp1CustomRtxLeftrThresh.setUnits("Percent of NDR")


class _AdGenVdsl2ConfAmRadioFreqMask1_Type(Integer32):
    """Custom type adGenVdsl2ConfAmRadioFreqMask1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(540, 1700),
    )


_AdGenVdsl2ConfAmRadioFreqMask1_Type.__name__ = "Integer32"
_AdGenVdsl2ConfAmRadioFreqMask1_Object = MibTableColumn
adGenVdsl2ConfAmRadioFreqMask1 = _AdGenVdsl2ConfAmRadioFreqMask1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 110),
    _AdGenVdsl2ConfAmRadioFreqMask1_Type()
)
adGenVdsl2ConfAmRadioFreqMask1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfAmRadioFreqMask1.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfAmRadioFreqMask1.setUnits("kHz")


class _AdGenVdsl2ConfAmRadioFreqMask2_Type(Integer32):
    """Custom type adGenVdsl2ConfAmRadioFreqMask2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(540, 1700),
    )


_AdGenVdsl2ConfAmRadioFreqMask2_Type.__name__ = "Integer32"
_AdGenVdsl2ConfAmRadioFreqMask2_Object = MibTableColumn
adGenVdsl2ConfAmRadioFreqMask2 = _AdGenVdsl2ConfAmRadioFreqMask2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 111),
    _AdGenVdsl2ConfAmRadioFreqMask2_Type()
)
adGenVdsl2ConfAmRadioFreqMask2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfAmRadioFreqMask2.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfAmRadioFreqMask2.setUnits("kHz")


class _AdGenVdsl2ConfAmRadioFreqMask3_Type(Integer32):
    """Custom type adGenVdsl2ConfAmRadioFreqMask3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(540, 1700),
    )


_AdGenVdsl2ConfAmRadioFreqMask3_Type.__name__ = "Integer32"
_AdGenVdsl2ConfAmRadioFreqMask3_Object = MibTableColumn
adGenVdsl2ConfAmRadioFreqMask3 = _AdGenVdsl2ConfAmRadioFreqMask3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 112),
    _AdGenVdsl2ConfAmRadioFreqMask3_Type()
)
adGenVdsl2ConfAmRadioFreqMask3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfAmRadioFreqMask3.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfAmRadioFreqMask3.setUnits("kHz")


class _AdGenVdsl2ConfAmRadioFreqMask4_Type(Integer32):
    """Custom type adGenVdsl2ConfAmRadioFreqMask4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(540, 1700),
    )


_AdGenVdsl2ConfAmRadioFreqMask4_Type.__name__ = "Integer32"
_AdGenVdsl2ConfAmRadioFreqMask4_Object = MibTableColumn
adGenVdsl2ConfAmRadioFreqMask4 = _AdGenVdsl2ConfAmRadioFreqMask4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 113),
    _AdGenVdsl2ConfAmRadioFreqMask4_Type()
)
adGenVdsl2ConfAmRadioFreqMask4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfAmRadioFreqMask4.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfAmRadioFreqMask4.setUnits("kHz")


class _AdGenVdsl2ConfAmRadioFreqMask5_Type(Integer32):
    """Custom type adGenVdsl2ConfAmRadioFreqMask5 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(540, 1700),
    )


_AdGenVdsl2ConfAmRadioFreqMask5_Type.__name__ = "Integer32"
_AdGenVdsl2ConfAmRadioFreqMask5_Object = MibTableColumn
adGenVdsl2ConfAmRadioFreqMask5 = _AdGenVdsl2ConfAmRadioFreqMask5_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 114),
    _AdGenVdsl2ConfAmRadioFreqMask5_Type()
)
adGenVdsl2ConfAmRadioFreqMask5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfAmRadioFreqMask5.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfAmRadioFreqMask5.setUnits("kHz")


class _AdGenVdsl2ConfAmRadioFreqMask6_Type(Integer32):
    """Custom type adGenVdsl2ConfAmRadioFreqMask6 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(540, 1700),
    )


_AdGenVdsl2ConfAmRadioFreqMask6_Type.__name__ = "Integer32"
_AdGenVdsl2ConfAmRadioFreqMask6_Object = MibTableColumn
adGenVdsl2ConfAmRadioFreqMask6 = _AdGenVdsl2ConfAmRadioFreqMask6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 115),
    _AdGenVdsl2ConfAmRadioFreqMask6_Type()
)
adGenVdsl2ConfAmRadioFreqMask6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfAmRadioFreqMask6.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ConfAmRadioFreqMask6.setUnits("kHz")


class _AdGenVdsl2ConfMemorySplitRatio_Type(Integer32):
    """Custom type adGenVdsl2ConfMemorySplitRatio based on Integer32"""
    defaultValue = 2

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
        *(("oneToOne", 1),
          ("twoToOne", 2),
          ("threeToOne", 3),
          ("fourToOne", 4),
          ("fiveToOne", 5))
    )


_AdGenVdsl2ConfMemorySplitRatio_Type.__name__ = "Integer32"
_AdGenVdsl2ConfMemorySplitRatio_Object = MibTableColumn
adGenVdsl2ConfMemorySplitRatio = _AdGenVdsl2ConfMemorySplitRatio_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 116),
    _AdGenVdsl2ConfMemorySplitRatio_Type()
)
adGenVdsl2ConfMemorySplitRatio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfMemorySplitRatio.setStatus("current")


class _AdGenVdsl2ConfRateAdaptConfigMode_Type(Integer32):
    """Custom type adGenVdsl2ConfRateAdaptConfigMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("auto", 2))
    )


_AdGenVdsl2ConfRateAdaptConfigMode_Type.__name__ = "Integer32"
_AdGenVdsl2ConfRateAdaptConfigMode_Object = MibTableColumn
adGenVdsl2ConfRateAdaptConfigMode = _AdGenVdsl2ConfRateAdaptConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 1, 1, 117),
    _AdGenVdsl2ConfRateAdaptConfigMode_Type()
)
adGenVdsl2ConfRateAdaptConfigMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ConfRateAdaptConfigMode.setStatus("current")
_AdGenVdsl2LineAlarmConfProfileTable_Object = MibTable
adGenVdsl2LineAlarmConfProfileTable = _AdGenVdsl2LineAlarmConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2)
)
if mibBuilder.loadTexts:
    adGenVdsl2LineAlarmConfProfileTable.setStatus("current")
_AdGenVdsl2LineAlarmConfProfileEntry_Object = MibTableRow
adGenVdsl2LineAlarmConfProfileEntry = _AdGenVdsl2LineAlarmConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1)
)
adGenVdsl2LineAlarmConfProfileEntry.setIndexNames(
    (1, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2LineAlarmConfProfileName"),
)
if mibBuilder.loadTexts:
    adGenVdsl2LineAlarmConfProfileEntry.setStatus("current")


class _AdGenVdsl2LineAlarmConfProfileName_Type(DisplayString):
    """Custom type adGenVdsl2LineAlarmConfProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_AdGenVdsl2LineAlarmConfProfileName_Type.__name__ = "DisplayString"
_AdGenVdsl2LineAlarmConfProfileName_Object = MibTableColumn
adGenVdsl2LineAlarmConfProfileName = _AdGenVdsl2LineAlarmConfProfileName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 1),
    _AdGenVdsl2LineAlarmConfProfileName_Type()
)
adGenVdsl2LineAlarmConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVdsl2LineAlarmConfProfileName.setStatus("current")


class _AdGenVdsl2VtucThreshSnrMgn_Type(Integer32):
    """Custom type adGenVdsl2VtucThreshSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AdGenVdsl2VtucThreshSnrMgn_Type.__name__ = "Integer32"
_AdGenVdsl2VtucThreshSnrMgn_Object = MibTableColumn
adGenVdsl2VtucThreshSnrMgn = _AdGenVdsl2VtucThreshSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 2),
    _AdGenVdsl2VtucThreshSnrMgn_Type()
)
adGenVdsl2VtucThreshSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2VtucThreshSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucThreshSnrMgn.setUnits("dB")


class _AdGenVdsl2VtucThresh15MinLofs_Type(Gauge32):
    """Custom type adGenVdsl2VtucThresh15MinLofs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenVdsl2VtucThresh15MinLofs_Type.__name__ = "Gauge32"
_AdGenVdsl2VtucThresh15MinLofs_Object = MibTableColumn
adGenVdsl2VtucThresh15MinLofs = _AdGenVdsl2VtucThresh15MinLofs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 3),
    _AdGenVdsl2VtucThresh15MinLofs_Type()
)
adGenVdsl2VtucThresh15MinLofs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2VtucThresh15MinLofs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucThresh15MinLofs.setUnits("seconds")


class _AdGenVdsl2VtucThresh15MinLoss_Type(Gauge32):
    """Custom type adGenVdsl2VtucThresh15MinLoss based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenVdsl2VtucThresh15MinLoss_Type.__name__ = "Gauge32"
_AdGenVdsl2VtucThresh15MinLoss_Object = MibTableColumn
adGenVdsl2VtucThresh15MinLoss = _AdGenVdsl2VtucThresh15MinLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 4),
    _AdGenVdsl2VtucThresh15MinLoss_Type()
)
adGenVdsl2VtucThresh15MinLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2VtucThresh15MinLoss.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucThresh15MinLoss.setUnits("seconds")


class _AdGenVdsl2VtucThresh15MinLols_Type(Gauge32):
    """Custom type adGenVdsl2VtucThresh15MinLols based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenVdsl2VtucThresh15MinLols_Type.__name__ = "Gauge32"
_AdGenVdsl2VtucThresh15MinLols_Object = MibTableColumn
adGenVdsl2VtucThresh15MinLols = _AdGenVdsl2VtucThresh15MinLols_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 5),
    _AdGenVdsl2VtucThresh15MinLols_Type()
)
adGenVdsl2VtucThresh15MinLols.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2VtucThresh15MinLols.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucThresh15MinLols.setUnits("seconds")


class _AdGenVdsl2VtucThresh15MinLprs_Type(Gauge32):
    """Custom type adGenVdsl2VtucThresh15MinLprs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenVdsl2VtucThresh15MinLprs_Type.__name__ = "Gauge32"
_AdGenVdsl2VtucThresh15MinLprs_Object = MibTableColumn
adGenVdsl2VtucThresh15MinLprs = _AdGenVdsl2VtucThresh15MinLprs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 6),
    _AdGenVdsl2VtucThresh15MinLprs_Type()
)
adGenVdsl2VtucThresh15MinLprs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2VtucThresh15MinLprs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucThresh15MinLprs.setUnits("seconds")
_AdGenVdsl2VtucThresh15MinEs_Type = Gauge32
_AdGenVdsl2VtucThresh15MinEs_Object = MibTableColumn
adGenVdsl2VtucThresh15MinEs = _AdGenVdsl2VtucThresh15MinEs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 7),
    _AdGenVdsl2VtucThresh15MinEs_Type()
)
adGenVdsl2VtucThresh15MinEs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2VtucThresh15MinEs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucThresh15MinEs.setUnits("seconds")


class _AdGenVdsl2VtucThresh15MinSes_Type(Gauge32):
    """Custom type adGenVdsl2VtucThresh15MinSes based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenVdsl2VtucThresh15MinSes_Type.__name__ = "Gauge32"
_AdGenVdsl2VtucThresh15MinSes_Object = MibTableColumn
adGenVdsl2VtucThresh15MinSes = _AdGenVdsl2VtucThresh15MinSes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 8),
    _AdGenVdsl2VtucThresh15MinSes_Type()
)
adGenVdsl2VtucThresh15MinSes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2VtucThresh15MinSes.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucThresh15MinSes.setUnits("seconds")


class _AdGenVdsl2VtucThresh15MinUas_Type(Gauge32):
    """Custom type adGenVdsl2VtucThresh15MinUas based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenVdsl2VtucThresh15MinUas_Type.__name__ = "Gauge32"
_AdGenVdsl2VtucThresh15MinUas_Object = MibTableColumn
adGenVdsl2VtucThresh15MinUas = _AdGenVdsl2VtucThresh15MinUas_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 9),
    _AdGenVdsl2VtucThresh15MinUas_Type()
)
adGenVdsl2VtucThresh15MinUas.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2VtucThresh15MinUas.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucThresh15MinUas.setUnits("seconds")


class _AdGenVdsl2VturThreshSnrMgn_Type(Integer32):
    """Custom type adGenVdsl2VturThreshSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AdGenVdsl2VturThreshSnrMgn_Type.__name__ = "Integer32"
_AdGenVdsl2VturThreshSnrMgn_Object = MibTableColumn
adGenVdsl2VturThreshSnrMgn = _AdGenVdsl2VturThreshSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 10),
    _AdGenVdsl2VturThreshSnrMgn_Type()
)
adGenVdsl2VturThreshSnrMgn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2VturThreshSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturThreshSnrMgn.setUnits("dB")


class _AdGenVdsl2VturThresh15MinLofs_Type(Gauge32):
    """Custom type adGenVdsl2VturThresh15MinLofs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenVdsl2VturThresh15MinLofs_Type.__name__ = "Gauge32"
_AdGenVdsl2VturThresh15MinLofs_Object = MibTableColumn
adGenVdsl2VturThresh15MinLofs = _AdGenVdsl2VturThresh15MinLofs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 11),
    _AdGenVdsl2VturThresh15MinLofs_Type()
)
adGenVdsl2VturThresh15MinLofs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2VturThresh15MinLofs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturThresh15MinLofs.setUnits("seconds")


class _AdGenVdsl2VturThresh15MinLoss_Type(Gauge32):
    """Custom type adGenVdsl2VturThresh15MinLoss based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenVdsl2VturThresh15MinLoss_Type.__name__ = "Gauge32"
_AdGenVdsl2VturThresh15MinLoss_Object = MibTableColumn
adGenVdsl2VturThresh15MinLoss = _AdGenVdsl2VturThresh15MinLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 12),
    _AdGenVdsl2VturThresh15MinLoss_Type()
)
adGenVdsl2VturThresh15MinLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2VturThresh15MinLoss.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturThresh15MinLoss.setUnits("seconds")


class _AdGenVdsl2VturThresh15MinLprs_Type(Gauge32):
    """Custom type adGenVdsl2VturThresh15MinLprs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenVdsl2VturThresh15MinLprs_Type.__name__ = "Gauge32"
_AdGenVdsl2VturThresh15MinLprs_Object = MibTableColumn
adGenVdsl2VturThresh15MinLprs = _AdGenVdsl2VturThresh15MinLprs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 13),
    _AdGenVdsl2VturThresh15MinLprs_Type()
)
adGenVdsl2VturThresh15MinLprs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2VturThresh15MinLprs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturThresh15MinLprs.setUnits("seconds")


class _AdGenVdsl2VturThresh15MinEs_Type(Gauge32):
    """Custom type adGenVdsl2VturThresh15MinEs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdGenVdsl2VturThresh15MinEs_Type.__name__ = "Gauge32"
_AdGenVdsl2VturThresh15MinEs_Object = MibTableColumn
adGenVdsl2VturThresh15MinEs = _AdGenVdsl2VturThresh15MinEs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 14),
    _AdGenVdsl2VturThresh15MinEs_Type()
)
adGenVdsl2VturThresh15MinEs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2VturThresh15MinEs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturThresh15MinEs.setUnits("seconds")


class _AdGenVdsl2VturThresh15MinSes_Type(Gauge32):
    """Custom type adGenVdsl2VturThresh15MinSes based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenVdsl2VturThresh15MinSes_Type.__name__ = "Gauge32"
_AdGenVdsl2VturThresh15MinSes_Object = MibTableColumn
adGenVdsl2VturThresh15MinSes = _AdGenVdsl2VturThresh15MinSes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 15),
    _AdGenVdsl2VturThresh15MinSes_Type()
)
adGenVdsl2VturThresh15MinSes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2VturThresh15MinSes.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturThresh15MinSes.setUnits("seconds")


class _AdGenVdsl2VturThresh15MinUas_Type(Gauge32):
    """Custom type adGenVdsl2VturThresh15MinUas based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AdGenVdsl2VturThresh15MinUas_Type.__name__ = "Gauge32"
_AdGenVdsl2VturThresh15MinUas_Object = MibTableColumn
adGenVdsl2VturThresh15MinUas = _AdGenVdsl2VturThresh15MinUas_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 16),
    _AdGenVdsl2VturThresh15MinUas_Type()
)
adGenVdsl2VturThresh15MinUas.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2VturThresh15MinUas.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturThresh15MinUas.setUnits("seconds")
_AdGenVdsl2LineAlarmConfProfileRowStatus_Type = RowStatus
_AdGenVdsl2LineAlarmConfProfileRowStatus_Object = MibTableColumn
adGenVdsl2LineAlarmConfProfileRowStatus = _AdGenVdsl2LineAlarmConfProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 17),
    _AdGenVdsl2LineAlarmConfProfileRowStatus_Type()
)
adGenVdsl2LineAlarmConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2LineAlarmConfProfileRowStatus.setStatus("current")
_AdGenVdsl2ThreshUsLp0RateUp_Type = Gauge32
_AdGenVdsl2ThreshUsLp0RateUp_Object = MibTableColumn
adGenVdsl2ThreshUsLp0RateUp = _AdGenVdsl2ThreshUsLp0RateUp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 18),
    _AdGenVdsl2ThreshUsLp0RateUp_Type()
)
adGenVdsl2ThreshUsLp0RateUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ThreshUsLp0RateUp.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ThreshUsLp0RateUp.setUnits("bps")
_AdGenVdsl2ThreshUsLp0RateDown_Type = Gauge32
_AdGenVdsl2ThreshUsLp0RateDown_Object = MibTableColumn
adGenVdsl2ThreshUsLp0RateDown = _AdGenVdsl2ThreshUsLp0RateDown_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 19),
    _AdGenVdsl2ThreshUsLp0RateDown_Type()
)
adGenVdsl2ThreshUsLp0RateDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ThreshUsLp0RateDown.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ThreshUsLp0RateDown.setUnits("bps")
_AdGenVdsl2ThreshDsLp0RateUp_Type = Gauge32
_AdGenVdsl2ThreshDsLp0RateUp_Object = MibTableColumn
adGenVdsl2ThreshDsLp0RateUp = _AdGenVdsl2ThreshDsLp0RateUp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 20),
    _AdGenVdsl2ThreshDsLp0RateUp_Type()
)
adGenVdsl2ThreshDsLp0RateUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ThreshDsLp0RateUp.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ThreshDsLp0RateUp.setUnits("bps")
_AdGenVdsl2ThreshDsLp0RateDown_Type = Gauge32
_AdGenVdsl2ThreshDsLp0RateDown_Object = MibTableColumn
adGenVdsl2ThreshDsLp0RateDown = _AdGenVdsl2ThreshDsLp0RateDown_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 21),
    _AdGenVdsl2ThreshDsLp0RateDown_Type()
)
adGenVdsl2ThreshDsLp0RateDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ThreshDsLp0RateDown.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ThreshDsLp0RateDown.setUnits("bps")
_AdGenVdsl2ThreshUsLp1RateUp_Type = Gauge32
_AdGenVdsl2ThreshUsLp1RateUp_Object = MibTableColumn
adGenVdsl2ThreshUsLp1RateUp = _AdGenVdsl2ThreshUsLp1RateUp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 22),
    _AdGenVdsl2ThreshUsLp1RateUp_Type()
)
adGenVdsl2ThreshUsLp1RateUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ThreshUsLp1RateUp.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ThreshUsLp1RateUp.setUnits("bps")
_AdGenVdsl2ThreshUsLp1RateDown_Type = Gauge32
_AdGenVdsl2ThreshUsLp1RateDown_Object = MibTableColumn
adGenVdsl2ThreshUsLp1RateDown = _AdGenVdsl2ThreshUsLp1RateDown_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 23),
    _AdGenVdsl2ThreshUsLp1RateDown_Type()
)
adGenVdsl2ThreshUsLp1RateDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ThreshUsLp1RateDown.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ThreshUsLp1RateDown.setUnits("bps")
_AdGenVdsl2ThreshDsLp1RateUp_Type = Gauge32
_AdGenVdsl2ThreshDsLp1RateUp_Object = MibTableColumn
adGenVdsl2ThreshDsLp1RateUp = _AdGenVdsl2ThreshDsLp1RateUp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 24),
    _AdGenVdsl2ThreshDsLp1RateUp_Type()
)
adGenVdsl2ThreshDsLp1RateUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ThreshDsLp1RateUp.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ThreshDsLp1RateUp.setUnits("bps")
_AdGenVdsl2ThreshDsLp1RateDown_Type = Gauge32
_AdGenVdsl2ThreshDsLp1RateDown_Object = MibTableColumn
adGenVdsl2ThreshDsLp1RateDown = _AdGenVdsl2ThreshDsLp1RateDown_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 2, 1, 25),
    _AdGenVdsl2ThreshDsLp1RateDown_Type()
)
adGenVdsl2ThreshDsLp1RateDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2ThreshDsLp1RateDown.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ThreshDsLp1RateDown.setUnits("bps")
_AdGenVdsl2RestoreDefaultTable_Object = MibTable
adGenVdsl2RestoreDefaultTable = _AdGenVdsl2RestoreDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 3)
)
if mibBuilder.loadTexts:
    adGenVdsl2RestoreDefaultTable.setStatus("current")
_AdGenVdsl2RestoreDefaultEntry_Object = MibTableRow
adGenVdsl2RestoreDefaultEntry = _AdGenVdsl2RestoreDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 3, 1)
)
adGenVdsl2RestoreDefaultEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenVdsl2RestoreDefaultEntry.setStatus("current")


class _AdGenVdsl2ConfRestoreDefaults_Type(Integer32):
    """Custom type adGenVdsl2ConfRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("restoreProvisioning", 1),
          ("restoreAlarms", 2),
          ("restoreAll", 3))
    )


_AdGenVdsl2ConfRestoreDefaults_Type.__name__ = "Integer32"
_AdGenVdsl2ConfRestoreDefaults_Object = MibTableColumn
adGenVdsl2ConfRestoreDefaults = _AdGenVdsl2ConfRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 3, 1, 1),
    _AdGenVdsl2ConfRestoreDefaults_Type()
)
adGenVdsl2ConfRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVdsl2ConfRestoreDefaults.setStatus("current")
_AdGenVdsl2BandConfProfileTable_Object = MibTable
adGenVdsl2BandConfProfileTable = _AdGenVdsl2BandConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 4)
)
if mibBuilder.loadTexts:
    adGenVdsl2BandConfProfileTable.setStatus("current")
_AdGenVdsl2BandConfProfileEntry_Object = MibTableRow
adGenVdsl2BandConfProfileEntry = _AdGenVdsl2BandConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 4, 1)
)
adGenVdsl2BandConfProfileEntry.setIndexNames(
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2LineConfProfileName"),
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2BandNumber"),
)
if mibBuilder.loadTexts:
    adGenVdsl2BandConfProfileEntry.setStatus("current")


class _AdGenVdsl2BandNumber_Type(Integer32):
    """Custom type adGenVdsl2BandNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AdGenVdsl2BandNumber_Type.__name__ = "Integer32"
_AdGenVdsl2BandNumber_Object = MibTableColumn
adGenVdsl2BandNumber = _AdGenVdsl2BandNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 4, 1, 1),
    _AdGenVdsl2BandNumber_Type()
)
adGenVdsl2BandNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2BandNumber.setStatus("current")


class _AdGenVdsl2BandConfUsCustomPboCableA_Type(Unsigned32):
    """Custom type adGenVdsl2BandConfUsCustomPboCableA based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 8095),
    )


_AdGenVdsl2BandConfUsCustomPboCableA_Type.__name__ = "Unsigned32"
_AdGenVdsl2BandConfUsCustomPboCableA_Object = MibTableColumn
adGenVdsl2BandConfUsCustomPboCableA = _AdGenVdsl2BandConfUsCustomPboCableA_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 4, 1, 2),
    _AdGenVdsl2BandConfUsCustomPboCableA_Type()
)
adGenVdsl2BandConfUsCustomPboCableA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2BandConfUsCustomPboCableA.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2BandConfUsCustomPboCableA.setUnits("0.01 dBm/Hz")


class _AdGenVdsl2BandConfUsCustomPboCableB_Type(Unsigned32):
    """Custom type adGenVdsl2BandConfUsCustomPboCableB based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AdGenVdsl2BandConfUsCustomPboCableB_Type.__name__ = "Unsigned32"
_AdGenVdsl2BandConfUsCustomPboCableB_Object = MibTableColumn
adGenVdsl2BandConfUsCustomPboCableB = _AdGenVdsl2BandConfUsCustomPboCableB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 4, 1, 3),
    _AdGenVdsl2BandConfUsCustomPboCableB_Type()
)
adGenVdsl2BandConfUsCustomPboCableB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVdsl2BandConfUsCustomPboCableB.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2BandConfUsCustomPboCableB.setUnits("0.01 dBm/Hz")
_AdGenVdsl2AlarmSlotProvTable_Object = MibTable
adGenVdsl2AlarmSlotProvTable = _AdGenVdsl2AlarmSlotProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 5)
)
if mibBuilder.loadTexts:
    adGenVdsl2AlarmSlotProvTable.setStatus("current")
_AdGenVdsl2AlarmSlotProvEntry_Object = MibTableRow
adGenVdsl2AlarmSlotProvEntry = _AdGenVdsl2AlarmSlotProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 5, 1)
)
adGenVdsl2AlarmSlotProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenVdsl2AlarmSlotProvEntry.setStatus("current")


class _AdGenVdsl2AlmSlotLinkdownSeverity_Type(Integer32):
    """Custom type adGenVdsl2AlmSlotLinkdownSeverity based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenVdsl2AlmSlotLinkdownSeverity_Type.__name__ = "Integer32"
_AdGenVdsl2AlmSlotLinkdownSeverity_Object = MibTableColumn
adGenVdsl2AlmSlotLinkdownSeverity = _AdGenVdsl2AlmSlotLinkdownSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 1, 5, 1, 1),
    _AdGenVdsl2AlmSlotLinkdownSeverity_Type()
)
adGenVdsl2AlmSlotLinkdownSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVdsl2AlmSlotLinkdownSeverity.setStatus("current")
_AdGenVdsl2Status_ObjectIdentity = ObjectIdentity
adGenVdsl2Status = _AdGenVdsl2Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2)
)
_AdGenVdsl2LineTable_Object = MibTable
adGenVdsl2LineTable = _AdGenVdsl2LineTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 1)
)
if mibBuilder.loadTexts:
    adGenVdsl2LineTable.setStatus("current")
_AdGenVdsl2LineEntry_Object = MibTableRow
adGenVdsl2LineEntry = _AdGenVdsl2LineEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 1, 1)
)
adGenVdsl2LineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenVdsl2LineEntry.setStatus("current")


class _AdGenVdsl2LineCoding_Type(Integer32):
    """Custom type adGenVdsl2LineCoding based on Integer32"""
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
        *(("other", 1),
          ("dmt", 2),
          ("cap", 3),
          ("qam", 4))
    )


_AdGenVdsl2LineCoding_Type.__name__ = "Integer32"
_AdGenVdsl2LineCoding_Object = MibTableColumn
adGenVdsl2LineCoding = _AdGenVdsl2LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 1, 1, 1),
    _AdGenVdsl2LineCoding_Type()
)
adGenVdsl2LineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2LineCoding.setStatus("current")


class _AdGenVdsl2LinePortServiceState_Type(Integer32):
    """Custom type adGenVdsl2LinePortServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("is", 1),
          ("oosUas", 2),
          ("oosMA", 3))
    )


_AdGenVdsl2LinePortServiceState_Type.__name__ = "Integer32"
_AdGenVdsl2LinePortServiceState_Object = MibTableColumn
adGenVdsl2LinePortServiceState = _AdGenVdsl2LinePortServiceState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 1, 1, 3),
    _AdGenVdsl2LinePortServiceState_Type()
)
adGenVdsl2LinePortServiceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVdsl2LinePortServiceState.setStatus("current")


class _AdGenVdsl2LineStatus_Type(Integer32):
    """Custom type adGenVdsl2LineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("portDown", 1),
          ("portTraining", 2),
          ("showtime", 3))
    )


_AdGenVdsl2LineStatus_Type.__name__ = "Integer32"
_AdGenVdsl2LineStatus_Object = MibTableColumn
adGenVdsl2LineStatus = _AdGenVdsl2LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 1, 1, 6),
    _AdGenVdsl2LineStatus_Type()
)
adGenVdsl2LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2LineStatus.setStatus("current")
_AdGenVdsl2LineUpTime_Type = Gauge32
_AdGenVdsl2LineUpTime_Object = MibTableColumn
adGenVdsl2LineUpTime = _AdGenVdsl2LineUpTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 1, 1, 7),
    _AdGenVdsl2LineUpTime_Type()
)
adGenVdsl2LineUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2LineUpTime.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2LineUpTime.setUnits("seconds")


class _AdGenVdsl2LineCurrTransSysMode_Type(Integer32):
    """Custom type adGenVdsl2LineCurrTransSysMode based on Integer32"""
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
              28)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("multimode", 1),
          ("t1413", 2),
          ("g9921a", 3),
          ("g9921b", 4),
          ("g9921c", 5),
          ("g9921h", 6),
          ("g9921i", 7),
          ("g9922", 8),
          ("g9922c", 9),
          ("g9923a", 10),
          ("g9923b", 11),
          ("g9923i", 12),
          ("g9923j", 13),
          ("g9923m", 14),
          ("g9923l", 15),
          ("g9924a", 16),
          ("g9924i", 17),
          ("g9925a", 18),
          ("g9925b", 19),
          ("g9925i", 20),
          ("g9925j", 21),
          ("g9925m", 22),
          ("g9931", 23),
          ("g9932a", 24),
          ("g9932b", 25),
          ("g9932c", 26),
          ("g9935", 27),
          ("g9932y", 28))
    )


_AdGenVdsl2LineCurrTransSysMode_Type.__name__ = "Integer32"
_AdGenVdsl2LineCurrTransSysMode_Object = MibTableColumn
adGenVdsl2LineCurrTransSysMode = _AdGenVdsl2LineCurrTransSysMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 1, 1, 8),
    _AdGenVdsl2LineCurrTransSysMode_Type()
)
adGenVdsl2LineCurrTransSysMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2LineCurrTransSysMode.setStatus("current")


class _AdGenVdsl2LineCurrBandProfile_Type(Integer32):
    """Custom type adGenVdsl2LineCurrBandProfile based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("g99328a", 1),
          ("g99328b", 2),
          ("g99328c", 3),
          ("g99328d", 4),
          ("g993212a", 5),
          ("g993212b", 6),
          ("g993217a", 7),
          ("g993230a", 8),
          ("g993217b", 9),
          ("g993235b", 10))
    )


_AdGenVdsl2LineCurrBandProfile_Type.__name__ = "Integer32"
_AdGenVdsl2LineCurrBandProfile_Object = MibTableColumn
adGenVdsl2LineCurrBandProfile = _AdGenVdsl2LineCurrBandProfile_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 1, 1, 9),
    _AdGenVdsl2LineCurrBandProfile_Type()
)
adGenVdsl2LineCurrBandProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2LineCurrBandProfile.setStatus("current")
_AdGenVdsl2LineCurrEstimatedLength_Type = Gauge32
_AdGenVdsl2LineCurrEstimatedLength_Object = MibTableColumn
adGenVdsl2LineCurrEstimatedLength = _AdGenVdsl2LineCurrEstimatedLength_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 1, 1, 10),
    _AdGenVdsl2LineCurrEstimatedLength_Type()
)
adGenVdsl2LineCurrEstimatedLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2LineCurrEstimatedLength.setStatus("current")


class _AdGenVdsl2LineCurrTpsTcFramingMode_Type(Integer32):
    """Custom type adGenVdsl2LineCurrTpsTcFramingMode based on Integer32"""
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
        *(("auto", 0),
          ("atm", 1),
          ("efm", 2),
          ("hdlc", 3))
    )


_AdGenVdsl2LineCurrTpsTcFramingMode_Type.__name__ = "Integer32"
_AdGenVdsl2LineCurrTpsTcFramingMode_Object = MibTableColumn
adGenVdsl2LineCurrTpsTcFramingMode = _AdGenVdsl2LineCurrTpsTcFramingMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 1, 1, 11),
    _AdGenVdsl2LineCurrTpsTcFramingMode_Type()
)
adGenVdsl2LineCurrTpsTcFramingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2LineCurrTpsTcFramingMode.setStatus("current")
_AdGenVdsl2VtucPhysTable_Object = MibTable
adGenVdsl2VtucPhysTable = _AdGenVdsl2VtucPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2)
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucPhysTable.setStatus("current")
_AdGenVdsl2VtucPhysEntry_Object = MibTableRow
adGenVdsl2VtucPhysEntry = _AdGenVdsl2VtucPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1)
)
adGenVdsl2VtucPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucPhysEntry.setStatus("current")
_AdGenVdsl2VtucInvSerialNumber_Type = DisplayString
_AdGenVdsl2VtucInvSerialNumber_Object = MibTableColumn
adGenVdsl2VtucInvSerialNumber = _AdGenVdsl2VtucInvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 1),
    _AdGenVdsl2VtucInvSerialNumber_Type()
)
adGenVdsl2VtucInvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucInvSerialNumber.setStatus("current")
_AdGenVdsl2VtucInvVendorID_Type = DisplayString
_AdGenVdsl2VtucInvVendorID_Object = MibTableColumn
adGenVdsl2VtucInvVendorID = _AdGenVdsl2VtucInvVendorID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 2),
    _AdGenVdsl2VtucInvVendorID_Type()
)
adGenVdsl2VtucInvVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucInvVendorID.setStatus("current")
_AdGenVdsl2VtucInvVersionNumber_Type = DisplayString
_AdGenVdsl2VtucInvVersionNumber_Object = MibTableColumn
adGenVdsl2VtucInvVersionNumber = _AdGenVdsl2VtucInvVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 3),
    _AdGenVdsl2VtucInvVersionNumber_Type()
)
adGenVdsl2VtucInvVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucInvVersionNumber.setStatus("current")


class _AdGenVdsl2CurrUSSnrMgn_Type(Integer32):
    """Custom type adGenVdsl2CurrUSSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-640, 640),
    )


_AdGenVdsl2CurrUSSnrMgn_Type.__name__ = "Integer32"
_AdGenVdsl2CurrUSSnrMgn_Object = MibTableColumn
adGenVdsl2CurrUSSnrMgn = _AdGenVdsl2CurrUSSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 4),
    _AdGenVdsl2CurrUSSnrMgn_Type()
)
adGenVdsl2CurrUSSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2CurrUSSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2CurrUSSnrMgn.setUnits("tenth dB")


class _AdGenVdsl2CurrUSAtn_Type(Integer32):
    """Custom type adGenVdsl2CurrUSAtn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 630),
    )


_AdGenVdsl2CurrUSAtn_Type.__name__ = "Integer32"
_AdGenVdsl2CurrUSAtn_Object = MibTableColumn
adGenVdsl2CurrUSAtn = _AdGenVdsl2CurrUSAtn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 5),
    _AdGenVdsl2CurrUSAtn_Type()
)
adGenVdsl2CurrUSAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2CurrUSAtn.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2CurrUSAtn.setUnits("tenth dB")
_AdGenVdsl2VtucCurrStatus_Type = Unsigned32
_AdGenVdsl2VtucCurrStatus_Object = MibTableColumn
adGenVdsl2VtucCurrStatus = _AdGenVdsl2VtucCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 6),
    _AdGenVdsl2VtucCurrStatus_Type()
)
adGenVdsl2VtucCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucCurrStatus.setStatus("current")


class _AdGenVdsl2VtucCurrOutputPwr_Type(Integer32):
    """Custom type adGenVdsl2VtucCurrOutputPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-310, 310),
    )


_AdGenVdsl2VtucCurrOutputPwr_Type.__name__ = "Integer32"
_AdGenVdsl2VtucCurrOutputPwr_Object = MibTableColumn
adGenVdsl2VtucCurrOutputPwr = _AdGenVdsl2VtucCurrOutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 7),
    _AdGenVdsl2VtucCurrOutputPwr_Type()
)
adGenVdsl2VtucCurrOutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucCurrOutputPwr.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucCurrOutputPwr.setUnits("tenth dBm")
_AdGenVdsl2VtucCurrAttainableRate_Type = Gauge32
_AdGenVdsl2VtucCurrAttainableRate_Object = MibTableColumn
adGenVdsl2VtucCurrAttainableRate = _AdGenVdsl2VtucCurrAttainableRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 8),
    _AdGenVdsl2VtucCurrAttainableRate_Type()
)
adGenVdsl2VtucCurrAttainableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucCurrAttainableRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucCurrAttainableRate.setUnits("bps")
_AdGenVdsl2VtucCurrTxRate_Type = Gauge32
_AdGenVdsl2VtucCurrTxRate_Object = MibTableColumn
adGenVdsl2VtucCurrTxRate = _AdGenVdsl2VtucCurrTxRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 9),
    _AdGenVdsl2VtucCurrTxRate_Type()
)
adGenVdsl2VtucCurrTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucCurrTxRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucCurrTxRate.setUnits("bps")
_AdGenVdsl2VtucPrevTxRate_Type = Gauge32
_AdGenVdsl2VtucPrevTxRate_Object = MibTableColumn
adGenVdsl2VtucPrevTxRate = _AdGenVdsl2VtucPrevTxRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 10),
    _AdGenVdsl2VtucPrevTxRate_Type()
)
adGenVdsl2VtucPrevTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPrevTxRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPrevTxRate.setUnits("bps")


class _AdGenVdsl2VtucActTxPsd_Type(Integer32):
    """Custom type adGenVdsl2VtucActTxPsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-900, 0),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_AdGenVdsl2VtucActTxPsd_Type.__name__ = "Integer32"
_AdGenVdsl2VtucActTxPsd_Object = MibTableColumn
adGenVdsl2VtucActTxPsd = _AdGenVdsl2VtucActTxPsd_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 11),
    _AdGenVdsl2VtucActTxPsd_Type()
)
adGenVdsl2VtucActTxPsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucActTxPsd.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucActTxPsd.setUnits("0.1 dB")


class _AdGenVdsl2VtucCurrTpsTcStatus_Type(Integer32):
    """Custom type adGenVdsl2VtucCurrTpsTcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noDefect", 0),
          ("outOfSync", 1))
    )


_AdGenVdsl2VtucCurrTpsTcStatus_Type.__name__ = "Integer32"
_AdGenVdsl2VtucCurrTpsTcStatus_Object = MibTableColumn
adGenVdsl2VtucCurrTpsTcStatus = _AdGenVdsl2VtucCurrTpsTcStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 12),
    _AdGenVdsl2VtucCurrTpsTcStatus_Type()
)
adGenVdsl2VtucCurrTpsTcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucCurrTpsTcStatus.setStatus("current")
_AdGenVdsl2VtucCurrTxLineRate_Type = Gauge32
_AdGenVdsl2VtucCurrTxLineRate_Object = MibTableColumn
adGenVdsl2VtucCurrTxLineRate = _AdGenVdsl2VtucCurrTxLineRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 13),
    _AdGenVdsl2VtucCurrTxLineRate_Type()
)
adGenVdsl2VtucCurrTxLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucCurrTxLineRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucCurrTxLineRate.setUnits("bps")
_AdGenVdsl2VtucPrevTxLineRate_Type = Gauge32
_AdGenVdsl2VtucPrevTxLineRate_Object = MibTableColumn
adGenVdsl2VtucPrevTxLineRate = _AdGenVdsl2VtucPrevTxLineRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 14),
    _AdGenVdsl2VtucPrevTxLineRate_Type()
)
adGenVdsl2VtucPrevTxLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPrevTxLineRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPrevTxLineRate.setUnits("bps")
_AdGenVdsl2VtucCircuitProviderCode_Type = DisplayString
_AdGenVdsl2VtucCircuitProviderCode_Object = MibTableColumn
adGenVdsl2VtucCircuitProviderCode = _AdGenVdsl2VtucCircuitProviderCode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 15),
    _AdGenVdsl2VtucCircuitProviderCode_Type()
)
adGenVdsl2VtucCircuitProviderCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucCircuitProviderCode.setStatus("current")
_AdGenVdsl2VtucCurrTxRateMax_Type = Gauge32
_AdGenVdsl2VtucCurrTxRateMax_Object = MibTableColumn
adGenVdsl2VtucCurrTxRateMax = _AdGenVdsl2VtucCurrTxRateMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 16),
    _AdGenVdsl2VtucCurrTxRateMax_Type()
)
adGenVdsl2VtucCurrTxRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucCurrTxRateMax.setStatus("current")
_AdGenVdsl2VtucCurrTxRateMin_Type = Gauge32
_AdGenVdsl2VtucCurrTxRateMin_Object = MibTableColumn
adGenVdsl2VtucCurrTxRateMin = _AdGenVdsl2VtucCurrTxRateMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 17),
    _AdGenVdsl2VtucCurrTxRateMin_Type()
)
adGenVdsl2VtucCurrTxRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucCurrTxRateMin.setStatus("current")
_AdGenVdsl2VtucLastSraDownshift_Type = TimeStamp
_AdGenVdsl2VtucLastSraDownshift_Object = MibTableColumn
adGenVdsl2VtucLastSraDownshift = _AdGenVdsl2VtucLastSraDownshift_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 18),
    _AdGenVdsl2VtucLastSraDownshift_Type()
)
adGenVdsl2VtucLastSraDownshift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucLastSraDownshift.setStatus("current")
_AdGenVdsl2VtucLastSraUpshift_Type = TimeStamp
_AdGenVdsl2VtucLastSraUpshift_Object = MibTableColumn
adGenVdsl2VtucLastSraUpshift = _AdGenVdsl2VtucLastSraUpshift_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 19),
    _AdGenVdsl2VtucLastSraUpshift_Type()
)
adGenVdsl2VtucLastSraUpshift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucLastSraUpshift.setStatus("current")


class _AdGenVdsl2VtucRtxUsed_Type(Integer32):
    """Custom type adGenVdsl2VtucRtxUsed based on Integer32"""
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
        *(("rtxInUse", 1),
          ("rtxNotInUseForbidden", 2),
          ("rtxNotInUseNotSupportedXTUC", 3),
          ("rtxNotInUseNotSupportedXTUR", 4),
          ("rtxNotInUseNotSupportedXTUCAndXTUR", 5))
    )


_AdGenVdsl2VtucRtxUsed_Type.__name__ = "Integer32"
_AdGenVdsl2VtucRtxUsed_Object = MibTableColumn
adGenVdsl2VtucRtxUsed = _AdGenVdsl2VtucRtxUsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 20),
    _AdGenVdsl2VtucRtxUsed_Type()
)
adGenVdsl2VtucRtxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucRtxUsed.setStatus("current")
_AdGenVdsl2VtucRtxEtr_Type = Gauge32
_AdGenVdsl2VtucRtxEtr_Object = MibTableColumn
adGenVdsl2VtucRtxEtr = _AdGenVdsl2VtucRtxEtr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 2, 1, 21),
    _AdGenVdsl2VtucRtxEtr_Type()
)
adGenVdsl2VtucRtxEtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucRtxEtr.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucRtxEtr.setUnits("bps")
_AdGenVdsl2VturPhysTable_Object = MibTable
adGenVdsl2VturPhysTable = _AdGenVdsl2VturPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3)
)
if mibBuilder.loadTexts:
    adGenVdsl2VturPhysTable.setStatus("current")
_AdGenVdsl2VturPhysEntry_Object = MibTableRow
adGenVdsl2VturPhysEntry = _AdGenVdsl2VturPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1)
)
adGenVdsl2VturPhysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenVdsl2VturPhysEntry.setStatus("current")
_AdGenVdsl2VturInvSerialNumber_Type = DisplayString
_AdGenVdsl2VturInvSerialNumber_Object = MibTableColumn
adGenVdsl2VturInvSerialNumber = _AdGenVdsl2VturInvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 1),
    _AdGenVdsl2VturInvSerialNumber_Type()
)
adGenVdsl2VturInvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturInvSerialNumber.setStatus("current")
_AdGenVdsl2VturInvVendorID_Type = DisplayString
_AdGenVdsl2VturInvVendorID_Object = MibTableColumn
adGenVdsl2VturInvVendorID = _AdGenVdsl2VturInvVendorID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 2),
    _AdGenVdsl2VturInvVendorID_Type()
)
adGenVdsl2VturInvVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturInvVendorID.setStatus("current")
_AdGenVdsl2VturInvVersionNumber_Type = DisplayString
_AdGenVdsl2VturInvVersionNumber_Object = MibTableColumn
adGenVdsl2VturInvVersionNumber = _AdGenVdsl2VturInvVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 3),
    _AdGenVdsl2VturInvVersionNumber_Type()
)
adGenVdsl2VturInvVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturInvVersionNumber.setStatus("current")


class _AdGenVdsl2CurrDSSnrMgn_Type(Integer32):
    """Custom type adGenVdsl2CurrDSSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-640, 640),
    )


_AdGenVdsl2CurrDSSnrMgn_Type.__name__ = "Integer32"
_AdGenVdsl2CurrDSSnrMgn_Object = MibTableColumn
adGenVdsl2CurrDSSnrMgn = _AdGenVdsl2CurrDSSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 4),
    _AdGenVdsl2CurrDSSnrMgn_Type()
)
adGenVdsl2CurrDSSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2CurrDSSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2CurrDSSnrMgn.setUnits("tenth dB")


class _AdGenVdsl2CurrDSAtn_Type(Integer32):
    """Custom type adGenVdsl2CurrDSAtn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 630),
    )


_AdGenVdsl2CurrDSAtn_Type.__name__ = "Integer32"
_AdGenVdsl2CurrDSAtn_Object = MibTableColumn
adGenVdsl2CurrDSAtn = _AdGenVdsl2CurrDSAtn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 5),
    _AdGenVdsl2CurrDSAtn_Type()
)
adGenVdsl2CurrDSAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2CurrDSAtn.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2CurrDSAtn.setUnits("tenth dB")
_AdGenVdsl2VturCurrStatus_Type = Unsigned32
_AdGenVdsl2VturCurrStatus_Object = MibTableColumn
adGenVdsl2VturCurrStatus = _AdGenVdsl2VturCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 6),
    _AdGenVdsl2VturCurrStatus_Type()
)
adGenVdsl2VturCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturCurrStatus.setStatus("current")


class _AdGenVdsl2VturCurrOutputPwr_Type(Integer32):
    """Custom type adGenVdsl2VturCurrOutputPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-310, 310),
    )


_AdGenVdsl2VturCurrOutputPwr_Type.__name__ = "Integer32"
_AdGenVdsl2VturCurrOutputPwr_Object = MibTableColumn
adGenVdsl2VturCurrOutputPwr = _AdGenVdsl2VturCurrOutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 7),
    _AdGenVdsl2VturCurrOutputPwr_Type()
)
adGenVdsl2VturCurrOutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturCurrOutputPwr.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturCurrOutputPwr.setUnits("tenth dBm")
_AdGenVdsl2VturCurrAttainableRate_Type = Gauge32
_AdGenVdsl2VturCurrAttainableRate_Object = MibTableColumn
adGenVdsl2VturCurrAttainableRate = _AdGenVdsl2VturCurrAttainableRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 8),
    _AdGenVdsl2VturCurrAttainableRate_Type()
)
adGenVdsl2VturCurrAttainableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturCurrAttainableRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturCurrAttainableRate.setUnits("bps")
_AdGenVdsl2VturCurrTxRate_Type = Gauge32
_AdGenVdsl2VturCurrTxRate_Object = MibTableColumn
adGenVdsl2VturCurrTxRate = _AdGenVdsl2VturCurrTxRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 9),
    _AdGenVdsl2VturCurrTxRate_Type()
)
adGenVdsl2VturCurrTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturCurrTxRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturCurrTxRate.setUnits("bps")
_AdGenVdsl2VturPrevTxRate_Type = Gauge32
_AdGenVdsl2VturPrevTxRate_Object = MibTableColumn
adGenVdsl2VturPrevTxRate = _AdGenVdsl2VturPrevTxRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 10),
    _AdGenVdsl2VturPrevTxRate_Type()
)
adGenVdsl2VturPrevTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPrevTxRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPrevTxRate.setUnits("bps")


class _AdGenVdsl2VturActTxPsd_Type(Integer32):
    """Custom type adGenVdsl2VturActTxPsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-900, 0),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_AdGenVdsl2VturActTxPsd_Type.__name__ = "Integer32"
_AdGenVdsl2VturActTxPsd_Object = MibTableColumn
adGenVdsl2VturActTxPsd = _AdGenVdsl2VturActTxPsd_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 11),
    _AdGenVdsl2VturActTxPsd_Type()
)
adGenVdsl2VturActTxPsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturActTxPsd.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturActTxPsd.setUnits("0.1 dB")
_AdGenVdsl2VturCurrTxLineRate_Type = Gauge32
_AdGenVdsl2VturCurrTxLineRate_Object = MibTableColumn
adGenVdsl2VturCurrTxLineRate = _AdGenVdsl2VturCurrTxLineRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 12),
    _AdGenVdsl2VturCurrTxLineRate_Type()
)
adGenVdsl2VturCurrTxLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturCurrTxLineRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturCurrTxLineRate.setUnits("bps")
_AdGenVdsl2VturPrevTxLineRate_Type = Gauge32
_AdGenVdsl2VturPrevTxLineRate_Object = MibTableColumn
adGenVdsl2VturPrevTxLineRate = _AdGenVdsl2VturPrevTxLineRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 13),
    _AdGenVdsl2VturPrevTxLineRate_Type()
)
adGenVdsl2VturPrevTxLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPrevTxLineRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPrevTxLineRate.setUnits("bps")
_AdGenVdsl2VturCircuitProviderCode_Type = DisplayString
_AdGenVdsl2VturCircuitProviderCode_Object = MibTableColumn
adGenVdsl2VturCircuitProviderCode = _AdGenVdsl2VturCircuitProviderCode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 14),
    _AdGenVdsl2VturCircuitProviderCode_Type()
)
adGenVdsl2VturCircuitProviderCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturCircuitProviderCode.setStatus("current")


class _AdGenVdsl2VturCircuitCapabilities_Type(OctetString):
    """Custom type adGenVdsl2VturCircuitCapabilities based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_AdGenVdsl2VturCircuitCapabilities_Type.__name__ = "OctetString"
_AdGenVdsl2VturCircuitCapabilities_Object = MibTableColumn
adGenVdsl2VturCircuitCapabilities = _AdGenVdsl2VturCircuitCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 15),
    _AdGenVdsl2VturCircuitCapabilities_Type()
)
adGenVdsl2VturCircuitCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturCircuitCapabilities.setStatus("current")
_AdGenVdsl2VturCurrTxRateMax_Type = Gauge32
_AdGenVdsl2VturCurrTxRateMax_Object = MibTableColumn
adGenVdsl2VturCurrTxRateMax = _AdGenVdsl2VturCurrTxRateMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 16),
    _AdGenVdsl2VturCurrTxRateMax_Type()
)
adGenVdsl2VturCurrTxRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturCurrTxRateMax.setStatus("current")
_AdGenVdsl2VturCurrTxRateMin_Type = Gauge32
_AdGenVdsl2VturCurrTxRateMin_Object = MibTableColumn
adGenVdsl2VturCurrTxRateMin = _AdGenVdsl2VturCurrTxRateMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 17),
    _AdGenVdsl2VturCurrTxRateMin_Type()
)
adGenVdsl2VturCurrTxRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturCurrTxRateMin.setStatus("current")
_AdGenVdsl2VturLastSraDownshift_Type = TimeStamp
_AdGenVdsl2VturLastSraDownshift_Object = MibTableColumn
adGenVdsl2VturLastSraDownshift = _AdGenVdsl2VturLastSraDownshift_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 18),
    _AdGenVdsl2VturLastSraDownshift_Type()
)
adGenVdsl2VturLastSraDownshift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturLastSraDownshift.setStatus("current")
_AdGenVdsl2VturLastSraUpshift_Type = TimeStamp
_AdGenVdsl2VturLastSraUpshift_Object = MibTableColumn
adGenVdsl2VturLastSraUpshift = _AdGenVdsl2VturLastSraUpshift_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 19),
    _AdGenVdsl2VturLastSraUpshift_Type()
)
adGenVdsl2VturLastSraUpshift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturLastSraUpshift.setStatus("current")


class _AdGenVdsl2VturRtxUsed_Type(Integer32):
    """Custom type adGenVdsl2VturRtxUsed based on Integer32"""
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
        *(("rtxInUse", 1),
          ("rtxNotInUseForbidden", 2),
          ("rtxNotInUseNotSupportedXTUC", 3),
          ("rtxNotInUseNotSupportedXTUR", 4),
          ("rtxNotInUseNotSupportedXTUCAndXTUR", 5))
    )


_AdGenVdsl2VturRtxUsed_Type.__name__ = "Integer32"
_AdGenVdsl2VturRtxUsed_Object = MibTableColumn
adGenVdsl2VturRtxUsed = _AdGenVdsl2VturRtxUsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 20),
    _AdGenVdsl2VturRtxUsed_Type()
)
adGenVdsl2VturRtxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturRtxUsed.setStatus("current")
_AdGenVdsl2VturRtxEtr_Type = Gauge32
_AdGenVdsl2VturRtxEtr_Object = MibTableColumn
adGenVdsl2VturRtxEtr = _AdGenVdsl2VturRtxEtr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 3, 1, 21),
    _AdGenVdsl2VturRtxEtr_Type()
)
adGenVdsl2VturRtxEtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturRtxEtr.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturRtxEtr.setUnits("bps")
_AdGenVdsl2VtucChanTable_Object = MibTable
adGenVdsl2VtucChanTable = _AdGenVdsl2VtucChanTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 4)
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanTable.setStatus("current")
_AdGenVdsl2VtucChanEntry_Object = MibTableRow
adGenVdsl2VtucChanEntry = _AdGenVdsl2VtucChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 4, 1)
)
adGenVdsl2VtucChanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChannelNumber"),
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanEntry.setStatus("current")


class _AdGenVdsl2VtucChannelNumber_Type(Integer32):
    """Custom type adGenVdsl2VtucChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AdGenVdsl2VtucChannelNumber_Type.__name__ = "Integer32"
_AdGenVdsl2VtucChannelNumber_Object = MibTableColumn
adGenVdsl2VtucChannelNumber = _AdGenVdsl2VtucChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 4, 1, 1),
    _AdGenVdsl2VtucChannelNumber_Type()
)
adGenVdsl2VtucChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChannelNumber.setStatus("current")
_AdGenVdsl2VtucChanInterleaveDelay_Type = Gauge32
_AdGenVdsl2VtucChanInterleaveDelay_Object = MibTableColumn
adGenVdsl2VtucChanInterleaveDelay = _AdGenVdsl2VtucChanInterleaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 4, 1, 2),
    _AdGenVdsl2VtucChanInterleaveDelay_Type()
)
adGenVdsl2VtucChanInterleaveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanInterleaveDelay.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanInterleaveDelay.setUnits("0.1 milli-seconds")
_AdGenVdsl2VtucChanCurrTxRate_Type = Gauge32
_AdGenVdsl2VtucChanCurrTxRate_Object = MibTableColumn
adGenVdsl2VtucChanCurrTxRate = _AdGenVdsl2VtucChanCurrTxRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 4, 1, 3),
    _AdGenVdsl2VtucChanCurrTxRate_Type()
)
adGenVdsl2VtucChanCurrTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanCurrTxRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanCurrTxRate.setUnits("bps")
_AdGenVdsl2VtucChanPrevTxRate_Type = Gauge32
_AdGenVdsl2VtucChanPrevTxRate_Object = MibTableColumn
adGenVdsl2VtucChanPrevTxRate = _AdGenVdsl2VtucChanPrevTxRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 4, 1, 4),
    _AdGenVdsl2VtucChanPrevTxRate_Type()
)
adGenVdsl2VtucChanPrevTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPrevTxRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPrevTxRate.setUnits("bps")
_AdGenVdsl2VtucChanCrcBlockLength_Type = Gauge32
_AdGenVdsl2VtucChanCrcBlockLength_Object = MibTableColumn
adGenVdsl2VtucChanCrcBlockLength = _AdGenVdsl2VtucChanCrcBlockLength_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 4, 1, 5),
    _AdGenVdsl2VtucChanCrcBlockLength_Type()
)
adGenVdsl2VtucChanCrcBlockLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanCrcBlockLength.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanCrcBlockLength.setUnits("byte")
_AdGenVdsl2VtucChanINP_Type = Gauge32
_AdGenVdsl2VtucChanINP_Object = MibTableColumn
adGenVdsl2VtucChanINP = _AdGenVdsl2VtucChanINP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 4, 1, 6),
    _AdGenVdsl2VtucChanINP_Type()
)
adGenVdsl2VtucChanINP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanINP.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanINP.setUnits("0.1 dmt symbols")
_AdGenVdsl2VtucChanINPRein_Type = Gauge32
_AdGenVdsl2VtucChanINPRein_Object = MibTableColumn
adGenVdsl2VtucChanINPRein = _AdGenVdsl2VtucChanINPRein_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 4, 1, 7),
    _AdGenVdsl2VtucChanINPRein_Type()
)
adGenVdsl2VtucChanINPRein.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanINPRein.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanINPRein.setUnits("0.1 dmt symbols")
_AdGenVdsl2VturChanTable_Object = MibTable
adGenVdsl2VturChanTable = _AdGenVdsl2VturChanTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 5)
)
if mibBuilder.loadTexts:
    adGenVdsl2VturChanTable.setStatus("current")
_AdGenVdsl2VturChanEntry_Object = MibTableRow
adGenVdsl2VturChanEntry = _AdGenVdsl2VturChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 5, 1)
)
adGenVdsl2VturChanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChannelNumber"),
)
if mibBuilder.loadTexts:
    adGenVdsl2VturChanEntry.setStatus("current")


class _AdGenVdsl2VturChannelNumber_Type(Integer32):
    """Custom type adGenVdsl2VturChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AdGenVdsl2VturChannelNumber_Type.__name__ = "Integer32"
_AdGenVdsl2VturChannelNumber_Object = MibTableColumn
adGenVdsl2VturChannelNumber = _AdGenVdsl2VturChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 5, 1, 1),
    _AdGenVdsl2VturChannelNumber_Type()
)
adGenVdsl2VturChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChannelNumber.setStatus("current")
_AdGenVdsl2VturChanInterleaveDelay_Type = Gauge32
_AdGenVdsl2VturChanInterleaveDelay_Object = MibTableColumn
adGenVdsl2VturChanInterleaveDelay = _AdGenVdsl2VturChanInterleaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 5, 1, 2),
    _AdGenVdsl2VturChanInterleaveDelay_Type()
)
adGenVdsl2VturChanInterleaveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanInterleaveDelay.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanInterleaveDelay.setUnits("0.1 milli-seconds")
_AdGenVdsl2VturChanCurrTxRate_Type = Gauge32
_AdGenVdsl2VturChanCurrTxRate_Object = MibTableColumn
adGenVdsl2VturChanCurrTxRate = _AdGenVdsl2VturChanCurrTxRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 5, 1, 3),
    _AdGenVdsl2VturChanCurrTxRate_Type()
)
adGenVdsl2VturChanCurrTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanCurrTxRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanCurrTxRate.setUnits("bps")
_AdGenVdsl2VturChanPrevTxRate_Type = Gauge32
_AdGenVdsl2VturChanPrevTxRate_Object = MibTableColumn
adGenVdsl2VturChanPrevTxRate = _AdGenVdsl2VturChanPrevTxRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 5, 1, 4),
    _AdGenVdsl2VturChanPrevTxRate_Type()
)
adGenVdsl2VturChanPrevTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPrevTxRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPrevTxRate.setUnits("bps")
_AdGenVdsl2VturChanCrcBlockLength_Type = Gauge32
_AdGenVdsl2VturChanCrcBlockLength_Object = MibTableColumn
adGenVdsl2VturChanCrcBlockLength = _AdGenVdsl2VturChanCrcBlockLength_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 5, 1, 5),
    _AdGenVdsl2VturChanCrcBlockLength_Type()
)
adGenVdsl2VturChanCrcBlockLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanCrcBlockLength.setStatus("current")
_AdGenVdsl2VturChanINP_Type = Gauge32
_AdGenVdsl2VturChanINP_Object = MibTableColumn
adGenVdsl2VturChanINP = _AdGenVdsl2VturChanINP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 5, 1, 6),
    _AdGenVdsl2VturChanINP_Type()
)
adGenVdsl2VturChanINP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanINP.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanINP.setUnits("0.1 dmt symbols")
_AdGenVdsl2VturChanINPRein_Type = Gauge32
_AdGenVdsl2VturChanINPRein_Object = MibTableColumn
adGenVdsl2VturChanINPRein = _AdGenVdsl2VturChanINPRein_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 5, 1, 7),
    _AdGenVdsl2VturChanINPRein_Type()
)
adGenVdsl2VturChanINPRein.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanINPRein.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanINPRein.setUnits("0.1 dmt symbols")
_AdGenVdsl2BandStatusTable_Object = MibTable
adGenVdsl2BandStatusTable = _AdGenVdsl2BandStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 6)
)
if mibBuilder.loadTexts:
    adGenVdsl2BandStatusTable.setStatus("current")
_AdGenVdsl2BandStatusEntry_Object = MibTableRow
adGenVdsl2BandStatusEntry = _AdGenVdsl2BandStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 6, 1)
)
adGenVdsl2BandStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2BandNumber"),
)
if mibBuilder.loadTexts:
    adGenVdsl2BandStatusEntry.setStatus("current")


class _AdGenVdsl2BandStatusNumber_Type(Integer32):
    """Custom type adGenVdsl2BandStatusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AdGenVdsl2BandStatusNumber_Type.__name__ = "Integer32"
_AdGenVdsl2BandStatusNumber_Object = MibTableColumn
adGenVdsl2BandStatusNumber = _AdGenVdsl2BandStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 6, 1, 1),
    _AdGenVdsl2BandStatusNumber_Type()
)
adGenVdsl2BandStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2BandStatusNumber.setStatus("current")


class _AdGenVdsl2BandStatusUsStartCarrier_Type(Unsigned32):
    """Custom type adGenVdsl2BandStatusUsStartCarrier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_AdGenVdsl2BandStatusUsStartCarrier_Type.__name__ = "Unsigned32"
_AdGenVdsl2BandStatusUsStartCarrier_Object = MibTableColumn
adGenVdsl2BandStatusUsStartCarrier = _AdGenVdsl2BandStatusUsStartCarrier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 6, 1, 2),
    _AdGenVdsl2BandStatusUsStartCarrier_Type()
)
adGenVdsl2BandStatusUsStartCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2BandStatusUsStartCarrier.setStatus("current")


class _AdGenVdsl2BandStatusUsStopCarrier_Type(Unsigned32):
    """Custom type adGenVdsl2BandStatusUsStopCarrier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_AdGenVdsl2BandStatusUsStopCarrier_Type.__name__ = "Unsigned32"
_AdGenVdsl2BandStatusUsStopCarrier_Object = MibTableColumn
adGenVdsl2BandStatusUsStopCarrier = _AdGenVdsl2BandStatusUsStopCarrier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 6, 1, 3),
    _AdGenVdsl2BandStatusUsStopCarrier_Type()
)
adGenVdsl2BandStatusUsStopCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2BandStatusUsStopCarrier.setStatus("current")


class _AdGenVdsl2BandStatusUsMargin_Type(Integer32):
    """Custom type adGenVdsl2BandStatusUsMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-641, 630),
    )


_AdGenVdsl2BandStatusUsMargin_Type.__name__ = "Integer32"
_AdGenVdsl2BandStatusUsMargin_Object = MibTableColumn
adGenVdsl2BandStatusUsMargin = _AdGenVdsl2BandStatusUsMargin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 6, 1, 4),
    _AdGenVdsl2BandStatusUsMargin_Type()
)
adGenVdsl2BandStatusUsMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2BandStatusUsMargin.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2BandStatusUsMargin.setUnits("0.1 dB")


class _AdGenVdsl2BandStatusUsLatn_Type(Integer32):
    """Custom type adGenVdsl2BandStatusUsLatn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
    )


_AdGenVdsl2BandStatusUsLatn_Type.__name__ = "Integer32"
_AdGenVdsl2BandStatusUsLatn_Object = MibTableColumn
adGenVdsl2BandStatusUsLatn = _AdGenVdsl2BandStatusUsLatn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 6, 1, 5),
    _AdGenVdsl2BandStatusUsLatn_Type()
)
adGenVdsl2BandStatusUsLatn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2BandStatusUsLatn.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2BandStatusUsLatn.setUnits("0.1 dB")


class _AdGenVdsl2BandStatusUsSatn_Type(Integer32):
    """Custom type adGenVdsl2BandStatusUsSatn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
    )


_AdGenVdsl2BandStatusUsSatn_Type.__name__ = "Integer32"
_AdGenVdsl2BandStatusUsSatn_Object = MibTableColumn
adGenVdsl2BandStatusUsSatn = _AdGenVdsl2BandStatusUsSatn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 6, 1, 6),
    _AdGenVdsl2BandStatusUsSatn_Type()
)
adGenVdsl2BandStatusUsSatn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2BandStatusUsSatn.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2BandStatusUsSatn.setUnits("0.1 dB")


class _AdGenVdsl2BandStatusDsStartCarrier_Type(Unsigned32):
    """Custom type adGenVdsl2BandStatusDsStartCarrier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_AdGenVdsl2BandStatusDsStartCarrier_Type.__name__ = "Unsigned32"
_AdGenVdsl2BandStatusDsStartCarrier_Object = MibTableColumn
adGenVdsl2BandStatusDsStartCarrier = _AdGenVdsl2BandStatusDsStartCarrier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 6, 1, 7),
    _AdGenVdsl2BandStatusDsStartCarrier_Type()
)
adGenVdsl2BandStatusDsStartCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2BandStatusDsStartCarrier.setStatus("current")


class _AdGenVdsl2BandStatusDsStopCarrier_Type(Unsigned32):
    """Custom type adGenVdsl2BandStatusDsStopCarrier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_AdGenVdsl2BandStatusDsStopCarrier_Type.__name__ = "Unsigned32"
_AdGenVdsl2BandStatusDsStopCarrier_Object = MibTableColumn
adGenVdsl2BandStatusDsStopCarrier = _AdGenVdsl2BandStatusDsStopCarrier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 6, 1, 8),
    _AdGenVdsl2BandStatusDsStopCarrier_Type()
)
adGenVdsl2BandStatusDsStopCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2BandStatusDsStopCarrier.setStatus("current")


class _AdGenVdsl2BandStatusDsMargin_Type(Integer32):
    """Custom type adGenVdsl2BandStatusDsMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-641, 630),
    )


_AdGenVdsl2BandStatusDsMargin_Type.__name__ = "Integer32"
_AdGenVdsl2BandStatusDsMargin_Object = MibTableColumn
adGenVdsl2BandStatusDsMargin = _AdGenVdsl2BandStatusDsMargin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 6, 1, 9),
    _AdGenVdsl2BandStatusDsMargin_Type()
)
adGenVdsl2BandStatusDsMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2BandStatusDsMargin.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2BandStatusDsMargin.setUnits("0.1 dB")


class _AdGenVdsl2BandStatusDsLatn_Type(Integer32):
    """Custom type adGenVdsl2BandStatusDsLatn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
    )


_AdGenVdsl2BandStatusDsLatn_Type.__name__ = "Integer32"
_AdGenVdsl2BandStatusDsLatn_Object = MibTableColumn
adGenVdsl2BandStatusDsLatn = _AdGenVdsl2BandStatusDsLatn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 6, 1, 10),
    _AdGenVdsl2BandStatusDsLatn_Type()
)
adGenVdsl2BandStatusDsLatn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2BandStatusDsLatn.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2BandStatusDsLatn.setUnits("0.1 dB")


class _AdGenVdsl2BandStatusDsSatn_Type(Integer32):
    """Custom type adGenVdsl2BandStatusDsSatn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
    )


_AdGenVdsl2BandStatusDsSatn_Type.__name__ = "Integer32"
_AdGenVdsl2BandStatusDsSatn_Object = MibTableColumn
adGenVdsl2BandStatusDsSatn = _AdGenVdsl2BandStatusDsSatn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 6, 1, 11),
    _AdGenVdsl2BandStatusDsSatn_Type()
)
adGenVdsl2BandStatusDsSatn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2BandStatusDsSatn.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2BandStatusDsSatn.setUnits("0.1 dB")
_AdGenVdsl2ScStatusTable_Object = MibTable
adGenVdsl2ScStatusTable = _AdGenVdsl2ScStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 7)
)
if mibBuilder.loadTexts:
    adGenVdsl2ScStatusTable.setStatus("current")
_AdGenVdsl2ScStatusEntry_Object = MibTableRow
adGenVdsl2ScStatusEntry = _AdGenVdsl2ScStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 7, 1)
)
adGenVdsl2ScStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ScStatusNumber"),
)
if mibBuilder.loadTexts:
    adGenVdsl2ScStatusEntry.setStatus("current")


class _AdGenVdsl2ScStatusNumber_Type(Integer32):
    """Custom type adGenVdsl2ScStatusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_AdGenVdsl2ScStatusNumber_Type.__name__ = "Integer32"
_AdGenVdsl2ScStatusNumber_Object = MibTableColumn
adGenVdsl2ScStatusNumber = _AdGenVdsl2ScStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 7, 1, 1),
    _AdGenVdsl2ScStatusNumber_Type()
)
adGenVdsl2ScStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2ScStatusNumber.setStatus("current")


class _AdGenVdsl2ScStatusUsBits_Type(Integer32):
    """Custom type adGenVdsl2ScStatusUsBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AdGenVdsl2ScStatusUsBits_Type.__name__ = "Integer32"
_AdGenVdsl2ScStatusUsBits_Object = MibTableColumn
adGenVdsl2ScStatusUsBits = _AdGenVdsl2ScStatusUsBits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 7, 1, 2),
    _AdGenVdsl2ScStatusUsBits_Type()
)
adGenVdsl2ScStatusUsBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2ScStatusUsBits.setStatus("current")


class _AdGenVdsl2ScStatusUsGain_Type(Integer32):
    """Custom type adGenVdsl2ScStatusUsGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AdGenVdsl2ScStatusUsGain_Type.__name__ = "Integer32"
_AdGenVdsl2ScStatusUsGain_Object = MibTableColumn
adGenVdsl2ScStatusUsGain = _AdGenVdsl2ScStatusUsGain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 7, 1, 3),
    _AdGenVdsl2ScStatusUsGain_Type()
)
adGenVdsl2ScStatusUsGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2ScStatusUsGain.setStatus("current")


class _AdGenVdsl2ScStatusUsSnr_Type(Integer32):
    """Custom type adGenVdsl2ScStatusUsSnr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 955),
    )


_AdGenVdsl2ScStatusUsSnr_Type.__name__ = "Integer32"
_AdGenVdsl2ScStatusUsSnr_Object = MibTableColumn
adGenVdsl2ScStatusUsSnr = _AdGenVdsl2ScStatusUsSnr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 7, 1, 4),
    _AdGenVdsl2ScStatusUsSnr_Type()
)
adGenVdsl2ScStatusUsSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2ScStatusUsSnr.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ScStatusUsSnr.setUnits("0.1 dB")


class _AdGenVdsl2ScStatusDsBits_Type(Integer32):
    """Custom type adGenVdsl2ScStatusDsBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AdGenVdsl2ScStatusDsBits_Type.__name__ = "Integer32"
_AdGenVdsl2ScStatusDsBits_Object = MibTableColumn
adGenVdsl2ScStatusDsBits = _AdGenVdsl2ScStatusDsBits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 7, 1, 5),
    _AdGenVdsl2ScStatusDsBits_Type()
)
adGenVdsl2ScStatusDsBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2ScStatusDsBits.setStatus("current")


class _AdGenVdsl2ScStatusDsGain_Type(Integer32):
    """Custom type adGenVdsl2ScStatusDsGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AdGenVdsl2ScStatusDsGain_Type.__name__ = "Integer32"
_AdGenVdsl2ScStatusDsGain_Object = MibTableColumn
adGenVdsl2ScStatusDsGain = _AdGenVdsl2ScStatusDsGain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 7, 1, 6),
    _AdGenVdsl2ScStatusDsGain_Type()
)
adGenVdsl2ScStatusDsGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2ScStatusDsGain.setStatus("current")


class _AdGenVdsl2ScStatusDsSnr_Type(Integer32):
    """Custom type adGenVdsl2ScStatusDsSnr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 955),
    )


_AdGenVdsl2ScStatusDsSnr_Type.__name__ = "Integer32"
_AdGenVdsl2ScStatusDsSnr_Object = MibTableColumn
adGenVdsl2ScStatusDsSnr = _AdGenVdsl2ScStatusDsSnr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 7, 1, 7),
    _AdGenVdsl2ScStatusDsSnr_Type()
)
adGenVdsl2ScStatusDsSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2ScStatusDsSnr.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ScStatusDsSnr.setUnits("0.1 dB")


class _AdGenVdsl2ScStatusUsQln_Type(Integer32):
    """Custom type adGenVdsl2ScStatusUsQln based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1505, -230),
    )


_AdGenVdsl2ScStatusUsQln_Type.__name__ = "Integer32"
_AdGenVdsl2ScStatusUsQln_Object = MibTableColumn
adGenVdsl2ScStatusUsQln = _AdGenVdsl2ScStatusUsQln_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 7, 1, 8),
    _AdGenVdsl2ScStatusUsQln_Type()
)
adGenVdsl2ScStatusUsQln.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2ScStatusUsQln.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ScStatusUsQln.setUnits("0.1 dBm/Hz")


class _AdGenVdsl2ScStatusDsQln_Type(Integer32):
    """Custom type adGenVdsl2ScStatusDsQln based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1505, -230),
    )


_AdGenVdsl2ScStatusDsQln_Type.__name__ = "Integer32"
_AdGenVdsl2ScStatusDsQln_Object = MibTableColumn
adGenVdsl2ScStatusDsQln = _AdGenVdsl2ScStatusDsQln_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 7, 1, 9),
    _AdGenVdsl2ScStatusDsQln_Type()
)
adGenVdsl2ScStatusDsQln.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2ScStatusDsQln.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ScStatusDsQln.setUnits("0.1 dBm/Hz")


class _AdGenVdsl2ScStatusUsHlog_Type(Integer32):
    """Custom type adGenVdsl2ScStatusUsHlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-963, 60),
    )


_AdGenVdsl2ScStatusUsHlog_Type.__name__ = "Integer32"
_AdGenVdsl2ScStatusUsHlog_Object = MibTableColumn
adGenVdsl2ScStatusUsHlog = _AdGenVdsl2ScStatusUsHlog_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 7, 1, 10),
    _AdGenVdsl2ScStatusUsHlog_Type()
)
adGenVdsl2ScStatusUsHlog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2ScStatusUsHlog.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ScStatusUsHlog.setUnits("0.1 dB")


class _AdGenVdsl2ScStatusDsHlog_Type(Integer32):
    """Custom type adGenVdsl2ScStatusDsHlog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-963, 60),
    )


_AdGenVdsl2ScStatusDsHlog_Type.__name__ = "Integer32"
_AdGenVdsl2ScStatusDsHlog_Object = MibTableColumn
adGenVdsl2ScStatusDsHlog = _AdGenVdsl2ScStatusDsHlog_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 7, 1, 11),
    _AdGenVdsl2ScStatusDsHlog_Type()
)
adGenVdsl2ScStatusDsHlog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2ScStatusDsHlog.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2ScStatusDsHlog.setUnits("0.1 dB")
_AdGenVdsl2ReserveInstanceBulkVDSLTlvTable_Object = MibTable
adGenVdsl2ReserveInstanceBulkVDSLTlvTable = _AdGenVdsl2ReserveInstanceBulkVDSLTlvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 8)
)
if mibBuilder.loadTexts:
    adGenVdsl2ReserveInstanceBulkVDSLTlvTable.setStatus("current")
_AdGenVdsl2ReserveInstanceBulkVDSLTlvEntry_Object = MibTableRow
adGenVdsl2ReserveInstanceBulkVDSLTlvEntry = _AdGenVdsl2ReserveInstanceBulkVDSLTlvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 8, 1)
)
adGenVdsl2ReserveInstanceBulkVDSLTlvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenVdsl2ReserveInstanceBulkVDSLTlvEntry.setStatus("current")
_AdGenVdsl2ReserveInstanceBulkVDSLSlotInstance_Type = Integer32
_AdGenVdsl2ReserveInstanceBulkVDSLSlotInstance_Object = MibTableColumn
adGenVdsl2ReserveInstanceBulkVDSLSlotInstance = _AdGenVdsl2ReserveInstanceBulkVDSLSlotInstance_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 8, 1, 1),
    _AdGenVdsl2ReserveInstanceBulkVDSLSlotInstance_Type()
)
adGenVdsl2ReserveInstanceBulkVDSLSlotInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2ReserveInstanceBulkVDSLSlotInstance.setStatus("current")
_AdGenVdsl2BulkVDSLTlvTable_Object = MibTable
adGenVdsl2BulkVDSLTlvTable = _AdGenVdsl2BulkVDSLTlvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 9)
)
if mibBuilder.loadTexts:
    adGenVdsl2BulkVDSLTlvTable.setStatus("current")
_AdGenVdsl2BulkVDSLTlvEntry_Object = MibTableRow
adGenVdsl2BulkVDSLTlvEntry = _AdGenVdsl2BulkVDSLTlvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 9, 1)
)
adGenVdsl2BulkVDSLTlvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2BulkVDSLTlvInstance"),
)
if mibBuilder.loadTexts:
    adGenVdsl2BulkVDSLTlvEntry.setStatus("current")
_AdGenVdsl2BulkVDSLTlvInstance_Type = Integer32
_AdGenVdsl2BulkVDSLTlvInstance_Object = MibTableColumn
adGenVdsl2BulkVDSLTlvInstance = _AdGenVdsl2BulkVDSLTlvInstance_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 9, 1, 1),
    _AdGenVdsl2BulkVDSLTlvInstance_Type()
)
adGenVdsl2BulkVDSLTlvInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVdsl2BulkVDSLTlvInstance.setStatus("current")


class _AdGenVdsl2BulkVDSLTlvType_Type(Integer32):
    """Custom type adGenVdsl2BulkVDSLTlvType based on Integer32"""
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
        *(("bat", 1),
          ("snr", 2),
          ("qln", 3),
          ("hlog", 4))
    )


_AdGenVdsl2BulkVDSLTlvType_Type.__name__ = "Integer32"
_AdGenVdsl2BulkVDSLTlvType_Object = MibTableColumn
adGenVdsl2BulkVDSLTlvType = _AdGenVdsl2BulkVDSLTlvType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 9, 1, 2),
    _AdGenVdsl2BulkVDSLTlvType_Type()
)
adGenVdsl2BulkVDSLTlvType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVdsl2BulkVDSLTlvType.setStatus("current")


class _AdGenVdsl2BulkVDSLTlvPort_Type(Unsigned32):
    """Custom type adGenVdsl2BulkVDSLTlvPort based on Unsigned32"""
    defaultValue = 1


_AdGenVdsl2BulkVDSLTlvPort_Type.__name__ = "Unsigned32"
_AdGenVdsl2BulkVDSLTlvPort_Object = MibTableColumn
adGenVdsl2BulkVDSLTlvPort = _AdGenVdsl2BulkVDSLTlvPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 9, 1, 3),
    _AdGenVdsl2BulkVDSLTlvPort_Type()
)
adGenVdsl2BulkVDSLTlvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVdsl2BulkVDSLTlvPort.setStatus("current")


class _AdGenVdsl2BulkVDLSTlvCreate_Type(Integer32):
    """Custom type adGenVdsl2BulkVDLSTlvCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("updateinstance", 1)
    )


_AdGenVdsl2BulkVDLSTlvCreate_Type.__name__ = "Integer32"
_AdGenVdsl2BulkVDLSTlvCreate_Object = MibTableColumn
adGenVdsl2BulkVDLSTlvCreate = _AdGenVdsl2BulkVDLSTlvCreate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 2, 9, 1, 4),
    _AdGenVdsl2BulkVDLSTlvCreate_Type()
)
adGenVdsl2BulkVDLSTlvCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVdsl2BulkVDLSTlvCreate.setStatus("current")
_AdGenVdsl2PM_ObjectIdentity = ObjectIdentity
adGenVdsl2PM = _AdGenVdsl2PM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3)
)
_AdGenVdsl2VtucPerfDataTable_Object = MibTable
adGenVdsl2VtucPerfDataTable = _AdGenVdsl2VtucPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1)
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfDataTable.setStatus("current")
_AdGenVdsl2VtucPerfDataEntry_Object = MibTableRow
adGenVdsl2VtucPerfDataEntry = _AdGenVdsl2VtucPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1)
)
adGenVdsl2VtucPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfDataEntry.setStatus("current")
_AdGenVdsl2VtucPerfLofs_Type = Counter32
_AdGenVdsl2VtucPerfLofs_Object = MibTableColumn
adGenVdsl2VtucPerfLofs = _AdGenVdsl2VtucPerfLofs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 1),
    _AdGenVdsl2VtucPerfLofs_Type()
)
adGenVdsl2VtucPerfLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfLofs.setStatus("current")
_AdGenVdsl2VtucPerfLoss_Type = Counter32
_AdGenVdsl2VtucPerfLoss_Object = MibTableColumn
adGenVdsl2VtucPerfLoss = _AdGenVdsl2VtucPerfLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 2),
    _AdGenVdsl2VtucPerfLoss_Type()
)
adGenVdsl2VtucPerfLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfLoss.setStatus("current")
_AdGenVdsl2VtucPerfLols_Type = Counter32
_AdGenVdsl2VtucPerfLols_Object = MibTableColumn
adGenVdsl2VtucPerfLols = _AdGenVdsl2VtucPerfLols_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 3),
    _AdGenVdsl2VtucPerfLols_Type()
)
adGenVdsl2VtucPerfLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfLols.setStatus("current")
_AdGenVdsl2VtucPerfLprs_Type = Counter32
_AdGenVdsl2VtucPerfLprs_Object = MibTableColumn
adGenVdsl2VtucPerfLprs = _AdGenVdsl2VtucPerfLprs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 4),
    _AdGenVdsl2VtucPerfLprs_Type()
)
adGenVdsl2VtucPerfLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfLprs.setStatus("current")
_AdGenVdsl2VtucPerfEs_Type = Counter32
_AdGenVdsl2VtucPerfEs_Object = MibTableColumn
adGenVdsl2VtucPerfEs = _AdGenVdsl2VtucPerfEs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 5),
    _AdGenVdsl2VtucPerfEs_Type()
)
adGenVdsl2VtucPerfEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfEs.setStatus("current")
_AdGenVdsl2VtucPerfInits_Type = Counter32
_AdGenVdsl2VtucPerfInits_Object = MibTableColumn
adGenVdsl2VtucPerfInits = _AdGenVdsl2VtucPerfInits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 6),
    _AdGenVdsl2VtucPerfInits_Type()
)
adGenVdsl2VtucPerfInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfInits.setStatus("current")
_AdGenVdsl2VtucPerfSes_Type = Counter32
_AdGenVdsl2VtucPerfSes_Object = MibTableColumn
adGenVdsl2VtucPerfSes = _AdGenVdsl2VtucPerfSes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 7),
    _AdGenVdsl2VtucPerfSes_Type()
)
adGenVdsl2VtucPerfSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfSes.setStatus("current")
_AdGenVdsl2VtucPerfUas_Type = Counter32
_AdGenVdsl2VtucPerfUas_Object = MibTableColumn
adGenVdsl2VtucPerfUas = _AdGenVdsl2VtucPerfUas_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 8),
    _AdGenVdsl2VtucPerfUas_Type()
)
adGenVdsl2VtucPerfUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfUas.setStatus("current")
_AdGenVdsl2VtucPerfFecs_Type = Counter32
_AdGenVdsl2VtucPerfFecs_Object = MibTableColumn
adGenVdsl2VtucPerfFecs = _AdGenVdsl2VtucPerfFecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 9),
    _AdGenVdsl2VtucPerfFecs_Type()
)
adGenVdsl2VtucPerfFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfFecs.setStatus("current")
_AdGenVdsl2VtucPerfCrc_Type = Counter32
_AdGenVdsl2VtucPerfCrc_Object = MibTableColumn
adGenVdsl2VtucPerfCrc = _AdGenVdsl2VtucPerfCrc_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 10),
    _AdGenVdsl2VtucPerfCrc_Type()
)
adGenVdsl2VtucPerfCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCrc.setStatus("current")
_AdGenVdsl2VtucPerfFec_Type = Counter32
_AdGenVdsl2VtucPerfFec_Object = MibTableColumn
adGenVdsl2VtucPerfFec = _AdGenVdsl2VtucPerfFec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 11),
    _AdGenVdsl2VtucPerfFec_Type()
)
adGenVdsl2VtucPerfFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfFec.setStatus("current")


class _AdGenVdsl2VtucPerfValidIntervals_Type(Integer32):
    """Custom type adGenVdsl2VtucPerfValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenVdsl2VtucPerfValidIntervals_Type.__name__ = "Integer32"
_AdGenVdsl2VtucPerfValidIntervals_Object = MibTableColumn
adGenVdsl2VtucPerfValidIntervals = _AdGenVdsl2VtucPerfValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 12),
    _AdGenVdsl2VtucPerfValidIntervals_Type()
)
adGenVdsl2VtucPerfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfValidIntervals.setStatus("current")


class _AdGenVdsl2VtucPerfInvalidIntervals_Type(Integer32):
    """Custom type adGenVdsl2VtucPerfInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenVdsl2VtucPerfInvalidIntervals_Type.__name__ = "Integer32"
_AdGenVdsl2VtucPerfInvalidIntervals_Object = MibTableColumn
adGenVdsl2VtucPerfInvalidIntervals = _AdGenVdsl2VtucPerfInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 13),
    _AdGenVdsl2VtucPerfInvalidIntervals_Type()
)
adGenVdsl2VtucPerfInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfInvalidIntervals.setStatus("current")


class _AdGenVdsl2VtucPerfCurr15MinTimeElapsed_Type(Gauge32):
    """Custom type adGenVdsl2VtucPerfCurr15MinTimeElapsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AdGenVdsl2VtucPerfCurr15MinTimeElapsed_Type.__name__ = "Gauge32"
_AdGenVdsl2VtucPerfCurr15MinTimeElapsed_Object = MibTableColumn
adGenVdsl2VtucPerfCurr15MinTimeElapsed = _AdGenVdsl2VtucPerfCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 14),
    _AdGenVdsl2VtucPerfCurr15MinTimeElapsed_Type()
)
adGenVdsl2VtucPerfCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinTimeElapsed.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr15MinLofs_Type = Counter32
_AdGenVdsl2VtucPerfCurr15MinLofs_Object = MibTableColumn
adGenVdsl2VtucPerfCurr15MinLofs = _AdGenVdsl2VtucPerfCurr15MinLofs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 15),
    _AdGenVdsl2VtucPerfCurr15MinLofs_Type()
)
adGenVdsl2VtucPerfCurr15MinLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinLofs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinLofs.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr15MinLoss_Type = Counter32
_AdGenVdsl2VtucPerfCurr15MinLoss_Object = MibTableColumn
adGenVdsl2VtucPerfCurr15MinLoss = _AdGenVdsl2VtucPerfCurr15MinLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 16),
    _AdGenVdsl2VtucPerfCurr15MinLoss_Type()
)
adGenVdsl2VtucPerfCurr15MinLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinLoss.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinLoss.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr15MinLols_Type = Counter32
_AdGenVdsl2VtucPerfCurr15MinLols_Object = MibTableColumn
adGenVdsl2VtucPerfCurr15MinLols = _AdGenVdsl2VtucPerfCurr15MinLols_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 17),
    _AdGenVdsl2VtucPerfCurr15MinLols_Type()
)
adGenVdsl2VtucPerfCurr15MinLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinLols.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinLols.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr15MinLprs_Type = Counter32
_AdGenVdsl2VtucPerfCurr15MinLprs_Object = MibTableColumn
adGenVdsl2VtucPerfCurr15MinLprs = _AdGenVdsl2VtucPerfCurr15MinLprs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 18),
    _AdGenVdsl2VtucPerfCurr15MinLprs_Type()
)
adGenVdsl2VtucPerfCurr15MinLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinLprs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinLprs.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr15MinEs_Type = Counter32
_AdGenVdsl2VtucPerfCurr15MinEs_Object = MibTableColumn
adGenVdsl2VtucPerfCurr15MinEs = _AdGenVdsl2VtucPerfCurr15MinEs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 19),
    _AdGenVdsl2VtucPerfCurr15MinEs_Type()
)
adGenVdsl2VtucPerfCurr15MinEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinEs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinEs.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr15MinInits_Type = Counter32
_AdGenVdsl2VtucPerfCurr15MinInits_Object = MibTableColumn
adGenVdsl2VtucPerfCurr15MinInits = _AdGenVdsl2VtucPerfCurr15MinInits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 20),
    _AdGenVdsl2VtucPerfCurr15MinInits_Type()
)
adGenVdsl2VtucPerfCurr15MinInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinInits.setStatus("current")
_AdGenVdsl2VtucPerfCurr15MinSes_Type = Counter32
_AdGenVdsl2VtucPerfCurr15MinSes_Object = MibTableColumn
adGenVdsl2VtucPerfCurr15MinSes = _AdGenVdsl2VtucPerfCurr15MinSes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 21),
    _AdGenVdsl2VtucPerfCurr15MinSes_Type()
)
adGenVdsl2VtucPerfCurr15MinSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinSes.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinSes.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr15MinUas_Type = Counter32
_AdGenVdsl2VtucPerfCurr15MinUas_Object = MibTableColumn
adGenVdsl2VtucPerfCurr15MinUas = _AdGenVdsl2VtucPerfCurr15MinUas_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 22),
    _AdGenVdsl2VtucPerfCurr15MinUas_Type()
)
adGenVdsl2VtucPerfCurr15MinUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinUas.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinUas.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr15MinFecs_Type = Counter32
_AdGenVdsl2VtucPerfCurr15MinFecs_Object = MibTableColumn
adGenVdsl2VtucPerfCurr15MinFecs = _AdGenVdsl2VtucPerfCurr15MinFecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 23),
    _AdGenVdsl2VtucPerfCurr15MinFecs_Type()
)
adGenVdsl2VtucPerfCurr15MinFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinFecs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinFecs.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr15MinCrc_Type = Counter32
_AdGenVdsl2VtucPerfCurr15MinCrc_Object = MibTableColumn
adGenVdsl2VtucPerfCurr15MinCrc = _AdGenVdsl2VtucPerfCurr15MinCrc_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 24),
    _AdGenVdsl2VtucPerfCurr15MinCrc_Type()
)
adGenVdsl2VtucPerfCurr15MinCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinCrc.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinCrc.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr15MinFec_Type = Counter32
_AdGenVdsl2VtucPerfCurr15MinFec_Object = MibTableColumn
adGenVdsl2VtucPerfCurr15MinFec = _AdGenVdsl2VtucPerfCurr15MinFec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 25),
    _AdGenVdsl2VtucPerfCurr15MinFec_Type()
)
adGenVdsl2VtucPerfCurr15MinFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinFec.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinFec.setUnits("seconds")


class _AdGenVdsl2VtucPerfCurr1DayTimeElapsed_Type(Gauge32):
    """Custom type adGenVdsl2VtucPerfCurr1DayTimeElapsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_AdGenVdsl2VtucPerfCurr1DayTimeElapsed_Type.__name__ = "Gauge32"
_AdGenVdsl2VtucPerfCurr1DayTimeElapsed_Object = MibTableColumn
adGenVdsl2VtucPerfCurr1DayTimeElapsed = _AdGenVdsl2VtucPerfCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 26),
    _AdGenVdsl2VtucPerfCurr1DayTimeElapsed_Type()
)
adGenVdsl2VtucPerfCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayTimeElapsed.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr1DayLofs_Type = Counter32
_AdGenVdsl2VtucPerfCurr1DayLofs_Object = MibTableColumn
adGenVdsl2VtucPerfCurr1DayLofs = _AdGenVdsl2VtucPerfCurr1DayLofs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 27),
    _AdGenVdsl2VtucPerfCurr1DayLofs_Type()
)
adGenVdsl2VtucPerfCurr1DayLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayLofs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayLofs.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr1DayLoss_Type = Counter32
_AdGenVdsl2VtucPerfCurr1DayLoss_Object = MibTableColumn
adGenVdsl2VtucPerfCurr1DayLoss = _AdGenVdsl2VtucPerfCurr1DayLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 28),
    _AdGenVdsl2VtucPerfCurr1DayLoss_Type()
)
adGenVdsl2VtucPerfCurr1DayLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayLoss.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayLoss.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr1DayLols_Type = Counter32
_AdGenVdsl2VtucPerfCurr1DayLols_Object = MibTableColumn
adGenVdsl2VtucPerfCurr1DayLols = _AdGenVdsl2VtucPerfCurr1DayLols_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 29),
    _AdGenVdsl2VtucPerfCurr1DayLols_Type()
)
adGenVdsl2VtucPerfCurr1DayLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayLols.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayLols.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr1DayLprs_Type = Counter32
_AdGenVdsl2VtucPerfCurr1DayLprs_Object = MibTableColumn
adGenVdsl2VtucPerfCurr1DayLprs = _AdGenVdsl2VtucPerfCurr1DayLprs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 30),
    _AdGenVdsl2VtucPerfCurr1DayLprs_Type()
)
adGenVdsl2VtucPerfCurr1DayLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayLprs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayLprs.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr1DayEs_Type = Counter32
_AdGenVdsl2VtucPerfCurr1DayEs_Object = MibTableColumn
adGenVdsl2VtucPerfCurr1DayEs = _AdGenVdsl2VtucPerfCurr1DayEs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 31),
    _AdGenVdsl2VtucPerfCurr1DayEs_Type()
)
adGenVdsl2VtucPerfCurr1DayEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayEs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayEs.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr1DayInits_Type = Counter32
_AdGenVdsl2VtucPerfCurr1DayInits_Object = MibTableColumn
adGenVdsl2VtucPerfCurr1DayInits = _AdGenVdsl2VtucPerfCurr1DayInits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 32),
    _AdGenVdsl2VtucPerfCurr1DayInits_Type()
)
adGenVdsl2VtucPerfCurr1DayInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayInits.setStatus("current")
_AdGenVdsl2VtucPerfCurr1DaySes_Type = Counter32
_AdGenVdsl2VtucPerfCurr1DaySes_Object = MibTableColumn
adGenVdsl2VtucPerfCurr1DaySes = _AdGenVdsl2VtucPerfCurr1DaySes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 33),
    _AdGenVdsl2VtucPerfCurr1DaySes_Type()
)
adGenVdsl2VtucPerfCurr1DaySes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DaySes.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DaySes.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr1DayUas_Type = Counter32
_AdGenVdsl2VtucPerfCurr1DayUas_Object = MibTableColumn
adGenVdsl2VtucPerfCurr1DayUas = _AdGenVdsl2VtucPerfCurr1DayUas_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 34),
    _AdGenVdsl2VtucPerfCurr1DayUas_Type()
)
adGenVdsl2VtucPerfCurr1DayUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayUas.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayUas.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr1DayFecs_Type = Counter32
_AdGenVdsl2VtucPerfCurr1DayFecs_Object = MibTableColumn
adGenVdsl2VtucPerfCurr1DayFecs = _AdGenVdsl2VtucPerfCurr1DayFecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 35),
    _AdGenVdsl2VtucPerfCurr1DayFecs_Type()
)
adGenVdsl2VtucPerfCurr1DayFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayFecs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayFecs.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr1DayCrc_Type = Counter32
_AdGenVdsl2VtucPerfCurr1DayCrc_Object = MibTableColumn
adGenVdsl2VtucPerfCurr1DayCrc = _AdGenVdsl2VtucPerfCurr1DayCrc_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 36),
    _AdGenVdsl2VtucPerfCurr1DayCrc_Type()
)
adGenVdsl2VtucPerfCurr1DayCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayCrc.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayCrc.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr1DayFec_Type = Counter32
_AdGenVdsl2VtucPerfCurr1DayFec_Object = MibTableColumn
adGenVdsl2VtucPerfCurr1DayFec = _AdGenVdsl2VtucPerfCurr1DayFec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 37),
    _AdGenVdsl2VtucPerfCurr1DayFec_Type()
)
adGenVdsl2VtucPerfCurr1DayFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayFec.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayFec.setUnits("seconds")
_AdGenVdsl2VtucPerfTcTxUnits_Type = Counter32
_AdGenVdsl2VtucPerfTcTxUnits_Object = MibTableColumn
adGenVdsl2VtucPerfTcTxUnits = _AdGenVdsl2VtucPerfTcTxUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 38),
    _AdGenVdsl2VtucPerfTcTxUnits_Type()
)
adGenVdsl2VtucPerfTcTxUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfTcTxUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfTcTxUnits.setUnits("pkts/cells")
_AdGenVdsl2VtucPerfTcTxDataUnits_Type = Counter32
_AdGenVdsl2VtucPerfTcTxDataUnits_Object = MibTableColumn
adGenVdsl2VtucPerfTcTxDataUnits = _AdGenVdsl2VtucPerfTcTxDataUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 39),
    _AdGenVdsl2VtucPerfTcTxDataUnits_Type()
)
adGenVdsl2VtucPerfTcTxDataUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfTcTxDataUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfTcTxDataUnits.setUnits("pkts/cells")
_AdGenVdsl2VtucPerfTcTxDataOctets_Type = Counter32
_AdGenVdsl2VtucPerfTcTxDataOctets_Object = MibTableColumn
adGenVdsl2VtucPerfTcTxDataOctets = _AdGenVdsl2VtucPerfTcTxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 40),
    _AdGenVdsl2VtucPerfTcTxDataOctets_Type()
)
adGenVdsl2VtucPerfTcTxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfTcTxDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfTcTxDataOctets.setUnits("octets")
_AdGenVdsl2VtucPerfTcTxIdleUnits_Type = Counter32
_AdGenVdsl2VtucPerfTcTxIdleUnits_Object = MibTableColumn
adGenVdsl2VtucPerfTcTxIdleUnits = _AdGenVdsl2VtucPerfTcTxIdleUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 41),
    _AdGenVdsl2VtucPerfTcTxIdleUnits_Type()
)
adGenVdsl2VtucPerfTcTxIdleUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfTcTxIdleUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfTcTxIdleUnits.setUnits("pkts/cells")
_AdGenVdsl2VtucPerfTcRxUnits_Type = Counter32
_AdGenVdsl2VtucPerfTcRxUnits_Object = MibTableColumn
adGenVdsl2VtucPerfTcRxUnits = _AdGenVdsl2VtucPerfTcRxUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 42),
    _AdGenVdsl2VtucPerfTcRxUnits_Type()
)
adGenVdsl2VtucPerfTcRxUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfTcRxUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfTcRxUnits.setUnits("pkts/cells")
_AdGenVdsl2VtucPerfTcRxDataUnits_Type = Counter32
_AdGenVdsl2VtucPerfTcRxDataUnits_Object = MibTableColumn
adGenVdsl2VtucPerfTcRxDataUnits = _AdGenVdsl2VtucPerfTcRxDataUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 43),
    _AdGenVdsl2VtucPerfTcRxDataUnits_Type()
)
adGenVdsl2VtucPerfTcRxDataUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfTcRxDataUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfTcRxDataUnits.setUnits("pkts/cells")
_AdGenVdsl2VtucPerfTcRxDataOctets_Type = Counter32
_AdGenVdsl2VtucPerfTcRxDataOctets_Object = MibTableColumn
adGenVdsl2VtucPerfTcRxDataOctets = _AdGenVdsl2VtucPerfTcRxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 44),
    _AdGenVdsl2VtucPerfTcRxDataOctets_Type()
)
adGenVdsl2VtucPerfTcRxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfTcRxDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfTcRxDataOctets.setUnits("octets")
_AdGenVdsl2VtucPerfTcRxIdleUnits_Type = Counter32
_AdGenVdsl2VtucPerfTcRxIdleUnits_Object = MibTableColumn
adGenVdsl2VtucPerfTcRxIdleUnits = _AdGenVdsl2VtucPerfTcRxIdleUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 45),
    _AdGenVdsl2VtucPerfTcRxIdleUnits_Type()
)
adGenVdsl2VtucPerfTcRxIdleUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfTcRxIdleUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfTcRxIdleUnits.setUnits("pkts/cells")
_AdGenVdsl2VtucPerfTcRxErroredUnits_Type = Counter32
_AdGenVdsl2VtucPerfTcRxErroredUnits_Object = MibTableColumn
adGenVdsl2VtucPerfTcRxErroredUnits = _AdGenVdsl2VtucPerfTcRxErroredUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 46),
    _AdGenVdsl2VtucPerfTcRxErroredUnits_Type()
)
adGenVdsl2VtucPerfTcRxErroredUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfTcRxErroredUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfTcRxErroredUnits.setUnits("pkts/cells")
_AdGenVdsl2VtucPerfSraDownshifts_Type = Counter32
_AdGenVdsl2VtucPerfSraDownshifts_Object = MibTableColumn
adGenVdsl2VtucPerfSraDownshifts = _AdGenVdsl2VtucPerfSraDownshifts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 47),
    _AdGenVdsl2VtucPerfSraDownshifts_Type()
)
adGenVdsl2VtucPerfSraDownshifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfSraDownshifts.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfSraDownshifts.setUnits("downshifts")
_AdGenVdsl2VtucPerfSraUpshifts_Type = Counter32
_AdGenVdsl2VtucPerfSraUpshifts_Object = MibTableColumn
adGenVdsl2VtucPerfSraUpshifts = _AdGenVdsl2VtucPerfSraUpshifts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 48),
    _AdGenVdsl2VtucPerfSraUpshifts_Type()
)
adGenVdsl2VtucPerfSraUpshifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfSraUpshifts.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfSraUpshifts.setUnits("upshifts")
_AdGenVdsl2VtucPerfCurr15MinSraDownshifts_Type = Counter32
_AdGenVdsl2VtucPerfCurr15MinSraDownshifts_Object = MibTableColumn
adGenVdsl2VtucPerfCurr15MinSraDownshifts = _AdGenVdsl2VtucPerfCurr15MinSraDownshifts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 49),
    _AdGenVdsl2VtucPerfCurr15MinSraDownshifts_Type()
)
adGenVdsl2VtucPerfCurr15MinSraDownshifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinSraDownshifts.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinSraDownshifts.setUnits("downshifts")
_AdGenVdsl2VtucPerfCurr15MinSraUpshifts_Type = Counter32
_AdGenVdsl2VtucPerfCurr15MinSraUpshifts_Object = MibTableColumn
adGenVdsl2VtucPerfCurr15MinSraUpshifts = _AdGenVdsl2VtucPerfCurr15MinSraUpshifts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 50),
    _AdGenVdsl2VtucPerfCurr15MinSraUpshifts_Type()
)
adGenVdsl2VtucPerfCurr15MinSraUpshifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinSraUpshifts.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinSraUpshifts.setUnits("upshifts")
_AdGenVdsl2VtucPerfCurr15MinSraRateMax_Type = Gauge32
_AdGenVdsl2VtucPerfCurr15MinSraRateMax_Object = MibTableColumn
adGenVdsl2VtucPerfCurr15MinSraRateMax = _AdGenVdsl2VtucPerfCurr15MinSraRateMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 51),
    _AdGenVdsl2VtucPerfCurr15MinSraRateMax_Type()
)
adGenVdsl2VtucPerfCurr15MinSraRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinSraRateMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinSraRateMax.setUnits("bps")
_AdGenVdsl2VtucPerfCurr15MinSraRateMin_Type = Gauge32
_AdGenVdsl2VtucPerfCurr15MinSraRateMin_Object = MibTableColumn
adGenVdsl2VtucPerfCurr15MinSraRateMin = _AdGenVdsl2VtucPerfCurr15MinSraRateMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 52),
    _AdGenVdsl2VtucPerfCurr15MinSraRateMin_Type()
)
adGenVdsl2VtucPerfCurr15MinSraRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinSraRateMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinSraRateMin.setUnits("bps")
_AdGenVdsl2VtucPerfCurr1DaySraDownshifts_Type = Counter32
_AdGenVdsl2VtucPerfCurr1DaySraDownshifts_Object = MibTableColumn
adGenVdsl2VtucPerfCurr1DaySraDownshifts = _AdGenVdsl2VtucPerfCurr1DaySraDownshifts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 53),
    _AdGenVdsl2VtucPerfCurr1DaySraDownshifts_Type()
)
adGenVdsl2VtucPerfCurr1DaySraDownshifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DaySraDownshifts.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DaySraDownshifts.setUnits("downshifts")
_AdGenVdsl2VtucPerfCurr1DaySraUpshifts_Type = Counter32
_AdGenVdsl2VtucPerfCurr1DaySraUpshifts_Object = MibTableColumn
adGenVdsl2VtucPerfCurr1DaySraUpshifts = _AdGenVdsl2VtucPerfCurr1DaySraUpshifts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 54),
    _AdGenVdsl2VtucPerfCurr1DaySraUpshifts_Type()
)
adGenVdsl2VtucPerfCurr1DaySraUpshifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DaySraUpshifts.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DaySraUpshifts.setUnits("upshifts")
_AdGenVdsl2VtucPerfCurr1DaySraRateMax_Type = Gauge32
_AdGenVdsl2VtucPerfCurr1DaySraRateMax_Object = MibTableColumn
adGenVdsl2VtucPerfCurr1DaySraRateMax = _AdGenVdsl2VtucPerfCurr1DaySraRateMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 55),
    _AdGenVdsl2VtucPerfCurr1DaySraRateMax_Type()
)
adGenVdsl2VtucPerfCurr1DaySraRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DaySraRateMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DaySraRateMax.setUnits("bps")
_AdGenVdsl2VtucPerfCurr1DaySraRateMin_Type = Gauge32
_AdGenVdsl2VtucPerfCurr1DaySraRateMin_Object = MibTableColumn
adGenVdsl2VtucPerfCurr1DaySraRateMin = _AdGenVdsl2VtucPerfCurr1DaySraRateMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 56),
    _AdGenVdsl2VtucPerfCurr1DaySraRateMin_Type()
)
adGenVdsl2VtucPerfCurr1DaySraRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DaySraRateMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DaySraRateMin.setUnits("bps")
_AdGenVdsl2VtucPerfRtxMinEftr_Type = Gauge32
_AdGenVdsl2VtucPerfRtxMinEftr_Object = MibTableColumn
adGenVdsl2VtucPerfRtxMinEftr = _AdGenVdsl2VtucPerfRtxMinEftr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 57),
    _AdGenVdsl2VtucPerfRtxMinEftr_Type()
)
adGenVdsl2VtucPerfRtxMinEftr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfRtxMinEftr.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfRtxMinEftr.setUnits("bps")
_AdGenVdsl2VtucPerfRtxLeftrs_Type = Counter32
_AdGenVdsl2VtucPerfRtxLeftrs_Object = MibTableColumn
adGenVdsl2VtucPerfRtxLeftrs = _AdGenVdsl2VtucPerfRtxLeftrs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 58),
    _AdGenVdsl2VtucPerfRtxLeftrs_Type()
)
adGenVdsl2VtucPerfRtxLeftrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfRtxLeftrs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfRtxLeftrs.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr15MinRtxMinEftr_Type = Gauge32
_AdGenVdsl2VtucPerfCurr15MinRtxMinEftr_Object = MibTableColumn
adGenVdsl2VtucPerfCurr15MinRtxMinEftr = _AdGenVdsl2VtucPerfCurr15MinRtxMinEftr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 59),
    _AdGenVdsl2VtucPerfCurr15MinRtxMinEftr_Type()
)
adGenVdsl2VtucPerfCurr15MinRtxMinEftr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinRtxMinEftr.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinRtxMinEftr.setUnits("bps")
_AdGenVdsl2VtucPerfCurr15MinRtxLeftrs_Type = Counter32
_AdGenVdsl2VtucPerfCurr15MinRtxLeftrs_Object = MibTableColumn
adGenVdsl2VtucPerfCurr15MinRtxLeftrs = _AdGenVdsl2VtucPerfCurr15MinRtxLeftrs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 60),
    _AdGenVdsl2VtucPerfCurr15MinRtxLeftrs_Type()
)
adGenVdsl2VtucPerfCurr15MinRtxLeftrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinRtxLeftrs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr15MinRtxLeftrs.setUnits("seconds")
_AdGenVdsl2VtucPerfCurr1DayRtxMinEftr_Type = Gauge32
_AdGenVdsl2VtucPerfCurr1DayRtxMinEftr_Object = MibTableColumn
adGenVdsl2VtucPerfCurr1DayRtxMinEftr = _AdGenVdsl2VtucPerfCurr1DayRtxMinEftr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 61),
    _AdGenVdsl2VtucPerfCurr1DayRtxMinEftr_Type()
)
adGenVdsl2VtucPerfCurr1DayRtxMinEftr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayRtxMinEftr.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayRtxMinEftr.setUnits("bps")
_AdGenVdsl2VtucPerfCurr1DayRtxLeftrs_Type = Counter32
_AdGenVdsl2VtucPerfCurr1DayRtxLeftrs_Object = MibTableColumn
adGenVdsl2VtucPerfCurr1DayRtxLeftrs = _AdGenVdsl2VtucPerfCurr1DayRtxLeftrs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 1, 1, 62),
    _AdGenVdsl2VtucPerfCurr1DayRtxLeftrs_Type()
)
adGenVdsl2VtucPerfCurr1DayRtxLeftrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayRtxLeftrs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucPerfCurr1DayRtxLeftrs.setUnits("seconds")
_AdGenVdsl2VturPerfDataTable_Object = MibTable
adGenVdsl2VturPerfDataTable = _AdGenVdsl2VturPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2)
)
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfDataTable.setStatus("current")
_AdGenVdsl2VturPerfDataEntry_Object = MibTableRow
adGenVdsl2VturPerfDataEntry = _AdGenVdsl2VturPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1)
)
adGenVdsl2VturPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfDataEntry.setStatus("current")
_AdGenVdsl2VturPerfLofs_Type = Counter32
_AdGenVdsl2VturPerfLofs_Object = MibTableColumn
adGenVdsl2VturPerfLofs = _AdGenVdsl2VturPerfLofs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 1),
    _AdGenVdsl2VturPerfLofs_Type()
)
adGenVdsl2VturPerfLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfLofs.setStatus("current")
_AdGenVdsl2VturPerfLoss_Type = Counter32
_AdGenVdsl2VturPerfLoss_Object = MibTableColumn
adGenVdsl2VturPerfLoss = _AdGenVdsl2VturPerfLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 2),
    _AdGenVdsl2VturPerfLoss_Type()
)
adGenVdsl2VturPerfLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfLoss.setStatus("current")
_AdGenVdsl2VturPerfLprs_Type = Counter32
_AdGenVdsl2VturPerfLprs_Object = MibTableColumn
adGenVdsl2VturPerfLprs = _AdGenVdsl2VturPerfLprs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 3),
    _AdGenVdsl2VturPerfLprs_Type()
)
adGenVdsl2VturPerfLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfLprs.setStatus("current")
_AdGenVdsl2VturPerfEs_Type = Counter32
_AdGenVdsl2VturPerfEs_Object = MibTableColumn
adGenVdsl2VturPerfEs = _AdGenVdsl2VturPerfEs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 4),
    _AdGenVdsl2VturPerfEs_Type()
)
adGenVdsl2VturPerfEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfEs.setStatus("current")
_AdGenVdsl2VturPerfSes_Type = Counter32
_AdGenVdsl2VturPerfSes_Object = MibTableColumn
adGenVdsl2VturPerfSes = _AdGenVdsl2VturPerfSes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 5),
    _AdGenVdsl2VturPerfSes_Type()
)
adGenVdsl2VturPerfSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfSes.setStatus("current")
_AdGenVdsl2VturPerfUas_Type = Counter32
_AdGenVdsl2VturPerfUas_Object = MibTableColumn
adGenVdsl2VturPerfUas = _AdGenVdsl2VturPerfUas_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 6),
    _AdGenVdsl2VturPerfUas_Type()
)
adGenVdsl2VturPerfUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfUas.setStatus("current")
_AdGenVdsl2VturPerfFecs_Type = Counter32
_AdGenVdsl2VturPerfFecs_Object = MibTableColumn
adGenVdsl2VturPerfFecs = _AdGenVdsl2VturPerfFecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 7),
    _AdGenVdsl2VturPerfFecs_Type()
)
adGenVdsl2VturPerfFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfFecs.setStatus("current")
_AdGenVdsl2VturPerfCrc_Type = Counter32
_AdGenVdsl2VturPerfCrc_Object = MibTableColumn
adGenVdsl2VturPerfCrc = _AdGenVdsl2VturPerfCrc_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 8),
    _AdGenVdsl2VturPerfCrc_Type()
)
adGenVdsl2VturPerfCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCrc.setStatus("current")
_AdGenVdsl2VturPerfFec_Type = Counter32
_AdGenVdsl2VturPerfFec_Object = MibTableColumn
adGenVdsl2VturPerfFec = _AdGenVdsl2VturPerfFec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 9),
    _AdGenVdsl2VturPerfFec_Type()
)
adGenVdsl2VturPerfFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfFec.setStatus("current")


class _AdGenVdsl2VturPerfValidIntervals_Type(Integer32):
    """Custom type adGenVdsl2VturPerfValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenVdsl2VturPerfValidIntervals_Type.__name__ = "Integer32"
_AdGenVdsl2VturPerfValidIntervals_Object = MibTableColumn
adGenVdsl2VturPerfValidIntervals = _AdGenVdsl2VturPerfValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 10),
    _AdGenVdsl2VturPerfValidIntervals_Type()
)
adGenVdsl2VturPerfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfValidIntervals.setStatus("current")


class _AdGenVdsl2VturPerfInvalidIntervals_Type(Integer32):
    """Custom type adGenVdsl2VturPerfInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenVdsl2VturPerfInvalidIntervals_Type.__name__ = "Integer32"
_AdGenVdsl2VturPerfInvalidIntervals_Object = MibTableColumn
adGenVdsl2VturPerfInvalidIntervals = _AdGenVdsl2VturPerfInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 11),
    _AdGenVdsl2VturPerfInvalidIntervals_Type()
)
adGenVdsl2VturPerfInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfInvalidIntervals.setStatus("current")


class _AdGenVdsl2VturPerfCurr15MinTimeElapsed_Type(Gauge32):
    """Custom type adGenVdsl2VturPerfCurr15MinTimeElapsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AdGenVdsl2VturPerfCurr15MinTimeElapsed_Type.__name__ = "Gauge32"
_AdGenVdsl2VturPerfCurr15MinTimeElapsed_Object = MibTableColumn
adGenVdsl2VturPerfCurr15MinTimeElapsed = _AdGenVdsl2VturPerfCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 12),
    _AdGenVdsl2VturPerfCurr15MinTimeElapsed_Type()
)
adGenVdsl2VturPerfCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinTimeElapsed.setUnits("seconds")
_AdGenVdsl2VturPerfCurr15MinLofs_Type = Counter32
_AdGenVdsl2VturPerfCurr15MinLofs_Object = MibTableColumn
adGenVdsl2VturPerfCurr15MinLofs = _AdGenVdsl2VturPerfCurr15MinLofs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 13),
    _AdGenVdsl2VturPerfCurr15MinLofs_Type()
)
adGenVdsl2VturPerfCurr15MinLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinLofs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinLofs.setUnits("seconds")
_AdGenVdsl2VturPerfCurr15MinLoss_Type = Counter32
_AdGenVdsl2VturPerfCurr15MinLoss_Object = MibTableColumn
adGenVdsl2VturPerfCurr15MinLoss = _AdGenVdsl2VturPerfCurr15MinLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 14),
    _AdGenVdsl2VturPerfCurr15MinLoss_Type()
)
adGenVdsl2VturPerfCurr15MinLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinLoss.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinLoss.setUnits("seconds")
_AdGenVdsl2VturPerfCurr15MinLprs_Type = Counter32
_AdGenVdsl2VturPerfCurr15MinLprs_Object = MibTableColumn
adGenVdsl2VturPerfCurr15MinLprs = _AdGenVdsl2VturPerfCurr15MinLprs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 15),
    _AdGenVdsl2VturPerfCurr15MinLprs_Type()
)
adGenVdsl2VturPerfCurr15MinLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinLprs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinLprs.setUnits("seconds")
_AdGenVdsl2VturPerfCurr15MinEs_Type = Counter32
_AdGenVdsl2VturPerfCurr15MinEs_Object = MibTableColumn
adGenVdsl2VturPerfCurr15MinEs = _AdGenVdsl2VturPerfCurr15MinEs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 16),
    _AdGenVdsl2VturPerfCurr15MinEs_Type()
)
adGenVdsl2VturPerfCurr15MinEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinEs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinEs.setUnits("seconds")
_AdGenVdsl2VturPerfCurr15MinSes_Type = Counter32
_AdGenVdsl2VturPerfCurr15MinSes_Object = MibTableColumn
adGenVdsl2VturPerfCurr15MinSes = _AdGenVdsl2VturPerfCurr15MinSes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 17),
    _AdGenVdsl2VturPerfCurr15MinSes_Type()
)
adGenVdsl2VturPerfCurr15MinSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinSes.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinSes.setUnits("seconds")
_AdGenVdsl2VturPerfCurr15MinUas_Type = Counter32
_AdGenVdsl2VturPerfCurr15MinUas_Object = MibTableColumn
adGenVdsl2VturPerfCurr15MinUas = _AdGenVdsl2VturPerfCurr15MinUas_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 18),
    _AdGenVdsl2VturPerfCurr15MinUas_Type()
)
adGenVdsl2VturPerfCurr15MinUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinUas.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinUas.setUnits("seconds")
_AdGenVdsl2VturPerfCurr15MinFecs_Type = Counter32
_AdGenVdsl2VturPerfCurr15MinFecs_Object = MibTableColumn
adGenVdsl2VturPerfCurr15MinFecs = _AdGenVdsl2VturPerfCurr15MinFecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 19),
    _AdGenVdsl2VturPerfCurr15MinFecs_Type()
)
adGenVdsl2VturPerfCurr15MinFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinFecs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinFecs.setUnits("seconds")
_AdGenVdsl2VturPerfCurr15MinCrc_Type = Counter32
_AdGenVdsl2VturPerfCurr15MinCrc_Object = MibTableColumn
adGenVdsl2VturPerfCurr15MinCrc = _AdGenVdsl2VturPerfCurr15MinCrc_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 20),
    _AdGenVdsl2VturPerfCurr15MinCrc_Type()
)
adGenVdsl2VturPerfCurr15MinCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinCrc.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinCrc.setUnits("seconds")
_AdGenVdsl2VturPerfCurr15MinFec_Type = Counter32
_AdGenVdsl2VturPerfCurr15MinFec_Object = MibTableColumn
adGenVdsl2VturPerfCurr15MinFec = _AdGenVdsl2VturPerfCurr15MinFec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 21),
    _AdGenVdsl2VturPerfCurr15MinFec_Type()
)
adGenVdsl2VturPerfCurr15MinFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinFec.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinFec.setUnits("seconds")


class _AdGenVdsl2VturPerfCurr1DayTimeElapsed_Type(Gauge32):
    """Custom type adGenVdsl2VturPerfCurr1DayTimeElapsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_AdGenVdsl2VturPerfCurr1DayTimeElapsed_Type.__name__ = "Gauge32"
_AdGenVdsl2VturPerfCurr1DayTimeElapsed_Object = MibTableColumn
adGenVdsl2VturPerfCurr1DayTimeElapsed = _AdGenVdsl2VturPerfCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 22),
    _AdGenVdsl2VturPerfCurr1DayTimeElapsed_Type()
)
adGenVdsl2VturPerfCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayTimeElapsed.setUnits("seconds")
_AdGenVdsl2VturPerfCurr1DayLofs_Type = Counter32
_AdGenVdsl2VturPerfCurr1DayLofs_Object = MibTableColumn
adGenVdsl2VturPerfCurr1DayLofs = _AdGenVdsl2VturPerfCurr1DayLofs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 23),
    _AdGenVdsl2VturPerfCurr1DayLofs_Type()
)
adGenVdsl2VturPerfCurr1DayLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayLofs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayLofs.setUnits("seconds")
_AdGenVdsl2VturPerfCurr1DayLoss_Type = Counter32
_AdGenVdsl2VturPerfCurr1DayLoss_Object = MibTableColumn
adGenVdsl2VturPerfCurr1DayLoss = _AdGenVdsl2VturPerfCurr1DayLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 24),
    _AdGenVdsl2VturPerfCurr1DayLoss_Type()
)
adGenVdsl2VturPerfCurr1DayLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayLoss.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayLoss.setUnits("seconds")
_AdGenVdsl2VturPerfCurr1DayLprs_Type = Counter32
_AdGenVdsl2VturPerfCurr1DayLprs_Object = MibTableColumn
adGenVdsl2VturPerfCurr1DayLprs = _AdGenVdsl2VturPerfCurr1DayLprs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 25),
    _AdGenVdsl2VturPerfCurr1DayLprs_Type()
)
adGenVdsl2VturPerfCurr1DayLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayLprs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayLprs.setUnits("seconds")
_AdGenVdsl2VturPerfCurr1DayEs_Type = Counter32
_AdGenVdsl2VturPerfCurr1DayEs_Object = MibTableColumn
adGenVdsl2VturPerfCurr1DayEs = _AdGenVdsl2VturPerfCurr1DayEs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 26),
    _AdGenVdsl2VturPerfCurr1DayEs_Type()
)
adGenVdsl2VturPerfCurr1DayEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayEs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayEs.setUnits("seconds")
_AdGenVdsl2VturPerfCurr1DaySes_Type = Counter32
_AdGenVdsl2VturPerfCurr1DaySes_Object = MibTableColumn
adGenVdsl2VturPerfCurr1DaySes = _AdGenVdsl2VturPerfCurr1DaySes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 27),
    _AdGenVdsl2VturPerfCurr1DaySes_Type()
)
adGenVdsl2VturPerfCurr1DaySes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DaySes.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DaySes.setUnits("seconds")
_AdGenVdsl2VturPerfCurr1DayUas_Type = Counter32
_AdGenVdsl2VturPerfCurr1DayUas_Object = MibTableColumn
adGenVdsl2VturPerfCurr1DayUas = _AdGenVdsl2VturPerfCurr1DayUas_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 28),
    _AdGenVdsl2VturPerfCurr1DayUas_Type()
)
adGenVdsl2VturPerfCurr1DayUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayUas.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayUas.setUnits("seconds")
_AdGenVdsl2VturPerfCurr1DayFecs_Type = Counter32
_AdGenVdsl2VturPerfCurr1DayFecs_Object = MibTableColumn
adGenVdsl2VturPerfCurr1DayFecs = _AdGenVdsl2VturPerfCurr1DayFecs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 29),
    _AdGenVdsl2VturPerfCurr1DayFecs_Type()
)
adGenVdsl2VturPerfCurr1DayFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayFecs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayFecs.setUnits("seconds")
_AdGenVdsl2VturPerfCurr1DayCrc_Type = Counter32
_AdGenVdsl2VturPerfCurr1DayCrc_Object = MibTableColumn
adGenVdsl2VturPerfCurr1DayCrc = _AdGenVdsl2VturPerfCurr1DayCrc_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 30),
    _AdGenVdsl2VturPerfCurr1DayCrc_Type()
)
adGenVdsl2VturPerfCurr1DayCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayCrc.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayCrc.setUnits("seconds")
_AdGenVdsl2VturPerfCurr1DayFec_Type = Counter32
_AdGenVdsl2VturPerfCurr1DayFec_Object = MibTableColumn
adGenVdsl2VturPerfCurr1DayFec = _AdGenVdsl2VturPerfCurr1DayFec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 31),
    _AdGenVdsl2VturPerfCurr1DayFec_Type()
)
adGenVdsl2VturPerfCurr1DayFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayFec.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayFec.setUnits("seconds")
_AdGenVdsl2VturPerfTcTxUnits_Type = Counter32
_AdGenVdsl2VturPerfTcTxUnits_Object = MibTableColumn
adGenVdsl2VturPerfTcTxUnits = _AdGenVdsl2VturPerfTcTxUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 32),
    _AdGenVdsl2VturPerfTcTxUnits_Type()
)
adGenVdsl2VturPerfTcTxUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfTcTxUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfTcTxUnits.setUnits("pkts/cells")
_AdGenVdsl2VturPerfTcTxDataUnits_Type = Counter32
_AdGenVdsl2VturPerfTcTxDataUnits_Object = MibTableColumn
adGenVdsl2VturPerfTcTxDataUnits = _AdGenVdsl2VturPerfTcTxDataUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 33),
    _AdGenVdsl2VturPerfTcTxDataUnits_Type()
)
adGenVdsl2VturPerfTcTxDataUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfTcTxDataUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfTcTxDataUnits.setUnits("pkts/cells")
_AdGenVdsl2VturPerfTcTxDataOctets_Type = Counter32
_AdGenVdsl2VturPerfTcTxDataOctets_Object = MibTableColumn
adGenVdsl2VturPerfTcTxDataOctets = _AdGenVdsl2VturPerfTcTxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 34),
    _AdGenVdsl2VturPerfTcTxDataOctets_Type()
)
adGenVdsl2VturPerfTcTxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfTcTxDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfTcTxDataOctets.setUnits("octets")
_AdGenVdsl2VturPerfTcTxIdleUnits_Type = Counter32
_AdGenVdsl2VturPerfTcTxIdleUnits_Object = MibTableColumn
adGenVdsl2VturPerfTcTxIdleUnits = _AdGenVdsl2VturPerfTcTxIdleUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 35),
    _AdGenVdsl2VturPerfTcTxIdleUnits_Type()
)
adGenVdsl2VturPerfTcTxIdleUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfTcTxIdleUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfTcTxIdleUnits.setUnits("pkts/cells")
_AdGenVdsl2VturPerfTcRxUnits_Type = Counter32
_AdGenVdsl2VturPerfTcRxUnits_Object = MibTableColumn
adGenVdsl2VturPerfTcRxUnits = _AdGenVdsl2VturPerfTcRxUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 36),
    _AdGenVdsl2VturPerfTcRxUnits_Type()
)
adGenVdsl2VturPerfTcRxUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfTcRxUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfTcRxUnits.setUnits("pkts/cells")
_AdGenVdsl2VturPerfTcRxDataUnits_Type = Counter32
_AdGenVdsl2VturPerfTcRxDataUnits_Object = MibTableColumn
adGenVdsl2VturPerfTcRxDataUnits = _AdGenVdsl2VturPerfTcRxDataUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 37),
    _AdGenVdsl2VturPerfTcRxDataUnits_Type()
)
adGenVdsl2VturPerfTcRxDataUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfTcRxDataUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfTcRxDataUnits.setUnits("pkts/cells")
_AdGenVdsl2VturPerfTcRxDataOctets_Type = Counter32
_AdGenVdsl2VturPerfTcRxDataOctets_Object = MibTableColumn
adGenVdsl2VturPerfTcRxDataOctets = _AdGenVdsl2VturPerfTcRxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 38),
    _AdGenVdsl2VturPerfTcRxDataOctets_Type()
)
adGenVdsl2VturPerfTcRxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfTcRxDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfTcRxDataOctets.setUnits("octets")
_AdGenVdsl2VturPerfTcRxIdleUnits_Type = Counter32
_AdGenVdsl2VturPerfTcRxIdleUnits_Object = MibTableColumn
adGenVdsl2VturPerfTcRxIdleUnits = _AdGenVdsl2VturPerfTcRxIdleUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 39),
    _AdGenVdsl2VturPerfTcRxIdleUnits_Type()
)
adGenVdsl2VturPerfTcRxIdleUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfTcRxIdleUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfTcRxIdleUnits.setUnits("pkts/cells")
_AdGenVdsl2VturPerfTcRxErroredUnits_Type = Counter32
_AdGenVdsl2VturPerfTcRxErroredUnits_Object = MibTableColumn
adGenVdsl2VturPerfTcRxErroredUnits = _AdGenVdsl2VturPerfTcRxErroredUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 40),
    _AdGenVdsl2VturPerfTcRxErroredUnits_Type()
)
adGenVdsl2VturPerfTcRxErroredUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfTcRxErroredUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfTcRxErroredUnits.setUnits("pkts/cells")
_AdGenVdsl2VturPerfSraDownshifts_Type = Counter32
_AdGenVdsl2VturPerfSraDownshifts_Object = MibTableColumn
adGenVdsl2VturPerfSraDownshifts = _AdGenVdsl2VturPerfSraDownshifts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 41),
    _AdGenVdsl2VturPerfSraDownshifts_Type()
)
adGenVdsl2VturPerfSraDownshifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfSraDownshifts.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfSraDownshifts.setUnits("downshifts")
_AdGenVdsl2VturPerfSraUpshifts_Type = Counter32
_AdGenVdsl2VturPerfSraUpshifts_Object = MibTableColumn
adGenVdsl2VturPerfSraUpshifts = _AdGenVdsl2VturPerfSraUpshifts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 42),
    _AdGenVdsl2VturPerfSraUpshifts_Type()
)
adGenVdsl2VturPerfSraUpshifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfSraUpshifts.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfSraUpshifts.setUnits("upshifts")
_AdGenVdsl2VturPerfCurr15MinSraDownshifts_Type = Counter32
_AdGenVdsl2VturPerfCurr15MinSraDownshifts_Object = MibTableColumn
adGenVdsl2VturPerfCurr15MinSraDownshifts = _AdGenVdsl2VturPerfCurr15MinSraDownshifts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 43),
    _AdGenVdsl2VturPerfCurr15MinSraDownshifts_Type()
)
adGenVdsl2VturPerfCurr15MinSraDownshifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinSraDownshifts.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinSraDownshifts.setUnits("downshifts")
_AdGenVdsl2VturPerfCurr15MinSraUpshifts_Type = Counter32
_AdGenVdsl2VturPerfCurr15MinSraUpshifts_Object = MibTableColumn
adGenVdsl2VturPerfCurr15MinSraUpshifts = _AdGenVdsl2VturPerfCurr15MinSraUpshifts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 44),
    _AdGenVdsl2VturPerfCurr15MinSraUpshifts_Type()
)
adGenVdsl2VturPerfCurr15MinSraUpshifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinSraUpshifts.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinSraUpshifts.setUnits("upshifts")
_AdGenVdsl2VturPerfCurr15MinSraRateMax_Type = Gauge32
_AdGenVdsl2VturPerfCurr15MinSraRateMax_Object = MibTableColumn
adGenVdsl2VturPerfCurr15MinSraRateMax = _AdGenVdsl2VturPerfCurr15MinSraRateMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 45),
    _AdGenVdsl2VturPerfCurr15MinSraRateMax_Type()
)
adGenVdsl2VturPerfCurr15MinSraRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinSraRateMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinSraRateMax.setUnits("bps")
_AdGenVdsl2VturPerfCurr15MinSraRateMin_Type = Gauge32
_AdGenVdsl2VturPerfCurr15MinSraRateMin_Object = MibTableColumn
adGenVdsl2VturPerfCurr15MinSraRateMin = _AdGenVdsl2VturPerfCurr15MinSraRateMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 46),
    _AdGenVdsl2VturPerfCurr15MinSraRateMin_Type()
)
adGenVdsl2VturPerfCurr15MinSraRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinSraRateMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinSraRateMin.setUnits("bps")
_AdGenVdsl2VturPerfCurr1DaySraDownshifts_Type = Counter32
_AdGenVdsl2VturPerfCurr1DaySraDownshifts_Object = MibTableColumn
adGenVdsl2VturPerfCurr1DaySraDownshifts = _AdGenVdsl2VturPerfCurr1DaySraDownshifts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 47),
    _AdGenVdsl2VturPerfCurr1DaySraDownshifts_Type()
)
adGenVdsl2VturPerfCurr1DaySraDownshifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DaySraDownshifts.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DaySraDownshifts.setUnits("downshifts")
_AdGenVdsl2VturPerfCurr1DaySraUpshifts_Type = Counter32
_AdGenVdsl2VturPerfCurr1DaySraUpshifts_Object = MibTableColumn
adGenVdsl2VturPerfCurr1DaySraUpshifts = _AdGenVdsl2VturPerfCurr1DaySraUpshifts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 48),
    _AdGenVdsl2VturPerfCurr1DaySraUpshifts_Type()
)
adGenVdsl2VturPerfCurr1DaySraUpshifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DaySraUpshifts.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DaySraUpshifts.setUnits("upshifts")
_AdGenVdsl2VturPerfCurr1DaySraRateMax_Type = Gauge32
_AdGenVdsl2VturPerfCurr1DaySraRateMax_Object = MibTableColumn
adGenVdsl2VturPerfCurr1DaySraRateMax = _AdGenVdsl2VturPerfCurr1DaySraRateMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 49),
    _AdGenVdsl2VturPerfCurr1DaySraRateMax_Type()
)
adGenVdsl2VturPerfCurr1DaySraRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DaySraRateMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DaySraRateMax.setUnits("bps")
_AdGenVdsl2VturPerfCurr1DaySraRateMin_Type = Gauge32
_AdGenVdsl2VturPerfCurr1DaySraRateMin_Object = MibTableColumn
adGenVdsl2VturPerfCurr1DaySraRateMin = _AdGenVdsl2VturPerfCurr1DaySraRateMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 50),
    _AdGenVdsl2VturPerfCurr1DaySraRateMin_Type()
)
adGenVdsl2VturPerfCurr1DaySraRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DaySraRateMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DaySraRateMin.setUnits("bps")
_AdGenVdsl2VturPerfRtxMinEftr_Type = Gauge32
_AdGenVdsl2VturPerfRtxMinEftr_Object = MibTableColumn
adGenVdsl2VturPerfRtxMinEftr = _AdGenVdsl2VturPerfRtxMinEftr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 51),
    _AdGenVdsl2VturPerfRtxMinEftr_Type()
)
adGenVdsl2VturPerfRtxMinEftr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfRtxMinEftr.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfRtxMinEftr.setUnits("bps")
_AdGenVdsl2VturPerfRtxLeftrs_Type = Counter32
_AdGenVdsl2VturPerfRtxLeftrs_Object = MibTableColumn
adGenVdsl2VturPerfRtxLeftrs = _AdGenVdsl2VturPerfRtxLeftrs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 52),
    _AdGenVdsl2VturPerfRtxLeftrs_Type()
)
adGenVdsl2VturPerfRtxLeftrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfRtxLeftrs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfRtxLeftrs.setUnits("seconds")
_AdGenVdsl2VturPerfCurr15MinRtxMinEftr_Type = Gauge32
_AdGenVdsl2VturPerfCurr15MinRtxMinEftr_Object = MibTableColumn
adGenVdsl2VturPerfCurr15MinRtxMinEftr = _AdGenVdsl2VturPerfCurr15MinRtxMinEftr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 53),
    _AdGenVdsl2VturPerfCurr15MinRtxMinEftr_Type()
)
adGenVdsl2VturPerfCurr15MinRtxMinEftr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinRtxMinEftr.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinRtxMinEftr.setUnits("bps")
_AdGenVdsl2VturPerfCurr15MinRtxLeftrs_Type = Counter32
_AdGenVdsl2VturPerfCurr15MinRtxLeftrs_Object = MibTableColumn
adGenVdsl2VturPerfCurr15MinRtxLeftrs = _AdGenVdsl2VturPerfCurr15MinRtxLeftrs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 54),
    _AdGenVdsl2VturPerfCurr15MinRtxLeftrs_Type()
)
adGenVdsl2VturPerfCurr15MinRtxLeftrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinRtxLeftrs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr15MinRtxLeftrs.setUnits("seconds")
_AdGenVdsl2VturPerfCurr1DayRtxMinEftr_Type = Gauge32
_AdGenVdsl2VturPerfCurr1DayRtxMinEftr_Object = MibTableColumn
adGenVdsl2VturPerfCurr1DayRtxMinEftr = _AdGenVdsl2VturPerfCurr1DayRtxMinEftr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 55),
    _AdGenVdsl2VturPerfCurr1DayRtxMinEftr_Type()
)
adGenVdsl2VturPerfCurr1DayRtxMinEftr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayRtxMinEftr.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayRtxMinEftr.setUnits("bps")
_AdGenVdsl2VturPerfCurr1DayRtxLeftrs_Type = Counter32
_AdGenVdsl2VturPerfCurr1DayRtxLeftrs_Object = MibTableColumn
adGenVdsl2VturPerfCurr1DayRtxLeftrs = _AdGenVdsl2VturPerfCurr1DayRtxLeftrs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 2, 1, 56),
    _AdGenVdsl2VturPerfCurr1DayRtxLeftrs_Type()
)
adGenVdsl2VturPerfCurr1DayRtxLeftrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayRtxLeftrs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturPerfCurr1DayRtxLeftrs.setUnits("seconds")
_AdGenVdsl2VtucIntervalTable_Object = MibTable
adGenVdsl2VtucIntervalTable = _AdGenVdsl2VtucIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3)
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalTable.setStatus("current")
_AdGenVdsl2VtucIntervalEntry_Object = MibTableRow
adGenVdsl2VtucIntervalEntry = _AdGenVdsl2VtucIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3, 1)
)
adGenVdsl2VtucIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalEntry.setStatus("current")


class _AdGenVdsl2VtucIntervalNumber_Type(Integer32):
    """Custom type adGenVdsl2VtucIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdGenVdsl2VtucIntervalNumber_Type.__name__ = "Integer32"
_AdGenVdsl2VtucIntervalNumber_Object = MibTableColumn
adGenVdsl2VtucIntervalNumber = _AdGenVdsl2VtucIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3, 1, 1),
    _AdGenVdsl2VtucIntervalNumber_Type()
)
adGenVdsl2VtucIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalNumber.setStatus("current")
_AdGenVdsl2VtucIntervalLofs_Type = Counter32
_AdGenVdsl2VtucIntervalLofs_Object = MibTableColumn
adGenVdsl2VtucIntervalLofs = _AdGenVdsl2VtucIntervalLofs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3, 1, 2),
    _AdGenVdsl2VtucIntervalLofs_Type()
)
adGenVdsl2VtucIntervalLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalLofs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalLofs.setUnits("seconds")
_AdGenVdsl2VtucIntervalLoss_Type = Counter32
_AdGenVdsl2VtucIntervalLoss_Object = MibTableColumn
adGenVdsl2VtucIntervalLoss = _AdGenVdsl2VtucIntervalLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3, 1, 3),
    _AdGenVdsl2VtucIntervalLoss_Type()
)
adGenVdsl2VtucIntervalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalLoss.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalLoss.setUnits("seconds")
_AdGenVdsl2VtucIntervalLols_Type = Counter32
_AdGenVdsl2VtucIntervalLols_Object = MibTableColumn
adGenVdsl2VtucIntervalLols = _AdGenVdsl2VtucIntervalLols_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3, 1, 4),
    _AdGenVdsl2VtucIntervalLols_Type()
)
adGenVdsl2VtucIntervalLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalLols.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalLols.setUnits("seconds")
_AdGenVdsl2VtucIntervalLprs_Type = Counter32
_AdGenVdsl2VtucIntervalLprs_Object = MibTableColumn
adGenVdsl2VtucIntervalLprs = _AdGenVdsl2VtucIntervalLprs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3, 1, 5),
    _AdGenVdsl2VtucIntervalLprs_Type()
)
adGenVdsl2VtucIntervalLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalLprs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalLprs.setUnits("seconds")
_AdGenVdsl2VtucIntervalES_Type = Counter32
_AdGenVdsl2VtucIntervalES_Object = MibTableColumn
adGenVdsl2VtucIntervalES = _AdGenVdsl2VtucIntervalES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3, 1, 6),
    _AdGenVdsl2VtucIntervalES_Type()
)
adGenVdsl2VtucIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalES.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalES.setUnits("seconds")
_AdGenVdsl2VtucIntervalInits_Type = Counter32
_AdGenVdsl2VtucIntervalInits_Object = MibTableColumn
adGenVdsl2VtucIntervalInits = _AdGenVdsl2VtucIntervalInits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3, 1, 7),
    _AdGenVdsl2VtucIntervalInits_Type()
)
adGenVdsl2VtucIntervalInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalInits.setStatus("current")


class _AdGenVdsl2VtucIntervalValidData_Type(Integer32):
    """Custom type adGenVdsl2VtucIntervalValidData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("notValid", 2))
    )


_AdGenVdsl2VtucIntervalValidData_Type.__name__ = "Integer32"
_AdGenVdsl2VtucIntervalValidData_Object = MibTableColumn
adGenVdsl2VtucIntervalValidData = _AdGenVdsl2VtucIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3, 1, 8),
    _AdGenVdsl2VtucIntervalValidData_Type()
)
adGenVdsl2VtucIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalValidData.setStatus("current")
_AdGenVdsl2VtucIntervalSES_Type = Counter32
_AdGenVdsl2VtucIntervalSES_Object = MibTableColumn
adGenVdsl2VtucIntervalSES = _AdGenVdsl2VtucIntervalSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3, 1, 9),
    _AdGenVdsl2VtucIntervalSES_Type()
)
adGenVdsl2VtucIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalSES.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalSES.setUnits("seconds")
_AdGenVdsl2VtucIntervalUAS_Type = Counter32
_AdGenVdsl2VtucIntervalUAS_Object = MibTableColumn
adGenVdsl2VtucIntervalUAS = _AdGenVdsl2VtucIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3, 1, 10),
    _AdGenVdsl2VtucIntervalUAS_Type()
)
adGenVdsl2VtucIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalUAS.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalUAS.setUnits("seconds")
_AdGenVdsl2VtucIntervalFECs_Type = Counter32
_AdGenVdsl2VtucIntervalFECs_Object = MibTableColumn
adGenVdsl2VtucIntervalFECs = _AdGenVdsl2VtucIntervalFECs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3, 1, 11),
    _AdGenVdsl2VtucIntervalFECs_Type()
)
adGenVdsl2VtucIntervalFECs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalFECs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalFECs.setUnits("seconds")
_AdGenVdsl2VtucIntervalFEC_Type = Counter32
_AdGenVdsl2VtucIntervalFEC_Object = MibTableColumn
adGenVdsl2VtucIntervalFEC = _AdGenVdsl2VtucIntervalFEC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3, 1, 12),
    _AdGenVdsl2VtucIntervalFEC_Type()
)
adGenVdsl2VtucIntervalFEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalFEC.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalFEC.setUnits("seconds")
_AdGenVdsl2VtucIntervalCRC_Type = Counter32
_AdGenVdsl2VtucIntervalCRC_Object = MibTableColumn
adGenVdsl2VtucIntervalCRC = _AdGenVdsl2VtucIntervalCRC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3, 1, 13),
    _AdGenVdsl2VtucIntervalCRC_Type()
)
adGenVdsl2VtucIntervalCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalCRC.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalCRC.setUnits("seconds")
_AdGenVdsl2VtucIntervalSraDownshifts_Type = Counter32
_AdGenVdsl2VtucIntervalSraDownshifts_Object = MibTableColumn
adGenVdsl2VtucIntervalSraDownshifts = _AdGenVdsl2VtucIntervalSraDownshifts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3, 1, 14),
    _AdGenVdsl2VtucIntervalSraDownshifts_Type()
)
adGenVdsl2VtucIntervalSraDownshifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalSraDownshifts.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalSraDownshifts.setUnits("downshifts")
_AdGenVdsl2VtucIntervalSraUpshifts_Type = Counter32
_AdGenVdsl2VtucIntervalSraUpshifts_Object = MibTableColumn
adGenVdsl2VtucIntervalSraUpshifts = _AdGenVdsl2VtucIntervalSraUpshifts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3, 1, 15),
    _AdGenVdsl2VtucIntervalSraUpshifts_Type()
)
adGenVdsl2VtucIntervalSraUpshifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalSraUpshifts.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalSraUpshifts.setUnits("upshifts")
_AdGenVdsl2VtucIntervalSraRateMax_Type = Gauge32
_AdGenVdsl2VtucIntervalSraRateMax_Object = MibTableColumn
adGenVdsl2VtucIntervalSraRateMax = _AdGenVdsl2VtucIntervalSraRateMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3, 1, 16),
    _AdGenVdsl2VtucIntervalSraRateMax_Type()
)
adGenVdsl2VtucIntervalSraRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalSraRateMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalSraRateMax.setUnits("bps")
_AdGenVdsl2VtucIntervalSraRateMin_Type = Gauge32
_AdGenVdsl2VtucIntervalSraRateMin_Object = MibTableColumn
adGenVdsl2VtucIntervalSraRateMin = _AdGenVdsl2VtucIntervalSraRateMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3, 1, 17),
    _AdGenVdsl2VtucIntervalSraRateMin_Type()
)
adGenVdsl2VtucIntervalSraRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalSraRateMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalSraRateMin.setUnits("bps")
_AdGenVdsl2VtucIntervalRtxMinEftr_Type = Gauge32
_AdGenVdsl2VtucIntervalRtxMinEftr_Object = MibTableColumn
adGenVdsl2VtucIntervalRtxMinEftr = _AdGenVdsl2VtucIntervalRtxMinEftr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3, 1, 18),
    _AdGenVdsl2VtucIntervalRtxMinEftr_Type()
)
adGenVdsl2VtucIntervalRtxMinEftr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalRtxMinEftr.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalRtxMinEftr.setUnits("bps")
_AdGenVdsl2VtucIntervalRtxLeftrs_Type = Counter32
_AdGenVdsl2VtucIntervalRtxLeftrs_Object = MibTableColumn
adGenVdsl2VtucIntervalRtxLeftrs = _AdGenVdsl2VtucIntervalRtxLeftrs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 3, 1, 19),
    _AdGenVdsl2VtucIntervalRtxLeftrs_Type()
)
adGenVdsl2VtucIntervalRtxLeftrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalRtxLeftrs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucIntervalRtxLeftrs.setUnits("seconds")
_AdGenVdsl2VturIntervalTable_Object = MibTable
adGenVdsl2VturIntervalTable = _AdGenVdsl2VturIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 4)
)
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalTable.setStatus("current")
_AdGenVdsl2VturIntervalEntry_Object = MibTableRow
adGenVdsl2VturIntervalEntry = _AdGenVdsl2VturIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 4, 1)
)
adGenVdsl2VturIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalEntry.setStatus("current")


class _AdGenVdsl2VturIntervalNumber_Type(Integer32):
    """Custom type adGenVdsl2VturIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdGenVdsl2VturIntervalNumber_Type.__name__ = "Integer32"
_AdGenVdsl2VturIntervalNumber_Object = MibTableColumn
adGenVdsl2VturIntervalNumber = _AdGenVdsl2VturIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 4, 1, 1),
    _AdGenVdsl2VturIntervalNumber_Type()
)
adGenVdsl2VturIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalNumber.setStatus("current")
_AdGenVdsl2VturIntervalLofs_Type = Counter32
_AdGenVdsl2VturIntervalLofs_Object = MibTableColumn
adGenVdsl2VturIntervalLofs = _AdGenVdsl2VturIntervalLofs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 4, 1, 2),
    _AdGenVdsl2VturIntervalLofs_Type()
)
adGenVdsl2VturIntervalLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalLofs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalLofs.setUnits("seconds")
_AdGenVdsl2VturIntervalLoss_Type = Counter32
_AdGenVdsl2VturIntervalLoss_Object = MibTableColumn
adGenVdsl2VturIntervalLoss = _AdGenVdsl2VturIntervalLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 4, 1, 3),
    _AdGenVdsl2VturIntervalLoss_Type()
)
adGenVdsl2VturIntervalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalLoss.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalLoss.setUnits("seconds")
_AdGenVdsl2VturIntervalLprs_Type = Counter32
_AdGenVdsl2VturIntervalLprs_Object = MibTableColumn
adGenVdsl2VturIntervalLprs = _AdGenVdsl2VturIntervalLprs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 4, 1, 4),
    _AdGenVdsl2VturIntervalLprs_Type()
)
adGenVdsl2VturIntervalLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalLprs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalLprs.setUnits("seconds")
_AdGenVdsl2VturIntervalES_Type = Counter32
_AdGenVdsl2VturIntervalES_Object = MibTableColumn
adGenVdsl2VturIntervalES = _AdGenVdsl2VturIntervalES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 4, 1, 5),
    _AdGenVdsl2VturIntervalES_Type()
)
adGenVdsl2VturIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalES.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalES.setUnits("seconds")


class _AdGenVdsl2VturIntervalValidData_Type(Integer32):
    """Custom type adGenVdsl2VturIntervalValidData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("notValid", 2))
    )


_AdGenVdsl2VturIntervalValidData_Type.__name__ = "Integer32"
_AdGenVdsl2VturIntervalValidData_Object = MibTableColumn
adGenVdsl2VturIntervalValidData = _AdGenVdsl2VturIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 4, 1, 6),
    _AdGenVdsl2VturIntervalValidData_Type()
)
adGenVdsl2VturIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalValidData.setStatus("current")
_AdGenVdsl2VturIntervalSES_Type = Counter32
_AdGenVdsl2VturIntervalSES_Object = MibTableColumn
adGenVdsl2VturIntervalSES = _AdGenVdsl2VturIntervalSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 4, 1, 7),
    _AdGenVdsl2VturIntervalSES_Type()
)
adGenVdsl2VturIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalSES.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalSES.setUnits("seconds")
_AdGenVdsl2VturIntervalUAS_Type = Counter32
_AdGenVdsl2VturIntervalUAS_Object = MibTableColumn
adGenVdsl2VturIntervalUAS = _AdGenVdsl2VturIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 4, 1, 8),
    _AdGenVdsl2VturIntervalUAS_Type()
)
adGenVdsl2VturIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalUAS.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalUAS.setUnits("seconds")
_AdGenVdsl2VturIntervalFECs_Type = Counter32
_AdGenVdsl2VturIntervalFECs_Object = MibTableColumn
adGenVdsl2VturIntervalFECs = _AdGenVdsl2VturIntervalFECs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 4, 1, 9),
    _AdGenVdsl2VturIntervalFECs_Type()
)
adGenVdsl2VturIntervalFECs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalFECs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalFECs.setUnits("seconds")
_AdGenVdsl2VturIntervalFEC_Type = Counter32
_AdGenVdsl2VturIntervalFEC_Object = MibTableColumn
adGenVdsl2VturIntervalFEC = _AdGenVdsl2VturIntervalFEC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 4, 1, 10),
    _AdGenVdsl2VturIntervalFEC_Type()
)
adGenVdsl2VturIntervalFEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalFEC.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalFEC.setUnits("seconds")
_AdGenVdsl2VturIntervalCRC_Type = Counter32
_AdGenVdsl2VturIntervalCRC_Object = MibTableColumn
adGenVdsl2VturIntervalCRC = _AdGenVdsl2VturIntervalCRC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 4, 1, 11),
    _AdGenVdsl2VturIntervalCRC_Type()
)
adGenVdsl2VturIntervalCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalCRC.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalCRC.setUnits("seconds")
_AdGenVdsl2VturIntervalSraDownshifts_Type = Counter32
_AdGenVdsl2VturIntervalSraDownshifts_Object = MibTableColumn
adGenVdsl2VturIntervalSraDownshifts = _AdGenVdsl2VturIntervalSraDownshifts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 4, 1, 12),
    _AdGenVdsl2VturIntervalSraDownshifts_Type()
)
adGenVdsl2VturIntervalSraDownshifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalSraDownshifts.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalSraDownshifts.setUnits("downshifts")
_AdGenVdsl2VturIntervalSraUpshifts_Type = Counter32
_AdGenVdsl2VturIntervalSraUpshifts_Object = MibTableColumn
adGenVdsl2VturIntervalSraUpshifts = _AdGenVdsl2VturIntervalSraUpshifts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 4, 1, 13),
    _AdGenVdsl2VturIntervalSraUpshifts_Type()
)
adGenVdsl2VturIntervalSraUpshifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalSraUpshifts.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalSraUpshifts.setUnits("upshifts")
_AdGenVdsl2VturIntervalSraRateMax_Type = Gauge32
_AdGenVdsl2VturIntervalSraRateMax_Object = MibTableColumn
adGenVdsl2VturIntervalSraRateMax = _AdGenVdsl2VturIntervalSraRateMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 4, 1, 14),
    _AdGenVdsl2VturIntervalSraRateMax_Type()
)
adGenVdsl2VturIntervalSraRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalSraRateMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalSraRateMax.setUnits("bps")
_AdGenVdsl2VturIntervalSraRateMin_Type = Gauge32
_AdGenVdsl2VturIntervalSraRateMin_Object = MibTableColumn
adGenVdsl2VturIntervalSraRateMin = _AdGenVdsl2VturIntervalSraRateMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 4, 1, 15),
    _AdGenVdsl2VturIntervalSraRateMin_Type()
)
adGenVdsl2VturIntervalSraRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalSraRateMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalSraRateMin.setUnits("bps")
_AdGenVdsl2VturIntervalRtxMinEftr_Type = Gauge32
_AdGenVdsl2VturIntervalRtxMinEftr_Object = MibTableColumn
adGenVdsl2VturIntervalRtxMinEftr = _AdGenVdsl2VturIntervalRtxMinEftr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 4, 1, 16),
    _AdGenVdsl2VturIntervalRtxMinEftr_Type()
)
adGenVdsl2VturIntervalRtxMinEftr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalRtxMinEftr.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalRtxMinEftr.setUnits("bps")
_AdGenVdsl2VturIntervalRtxLeftrs_Type = Counter32
_AdGenVdsl2VturIntervalRtxLeftrs_Object = MibTableColumn
adGenVdsl2VturIntervalRtxLeftrs = _AdGenVdsl2VturIntervalRtxLeftrs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 4, 1, 17),
    _AdGenVdsl2VturIntervalRtxLeftrs_Type()
)
adGenVdsl2VturIntervalRtxLeftrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalRtxLeftrs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturIntervalRtxLeftrs.setUnits("seconds")
_AdGenVdsl2VtucChanPerfDataTable_Object = MibTable
adGenVdsl2VtucChanPerfDataTable = _AdGenVdsl2VtucChanPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5)
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfDataTable.setStatus("current")
_AdGenVdsl2VtucChanPerfDataEntry_Object = MibTableRow
adGenVdsl2VtucChanPerfDataEntry = _AdGenVdsl2VtucChanPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1)
)
adGenVdsl2VtucChanPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanNumber"),
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfDataEntry.setStatus("current")


class _AdGenVdsl2VtucChanNumber_Type(Integer32):
    """Custom type adGenVdsl2VtucChanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AdGenVdsl2VtucChanNumber_Type.__name__ = "Integer32"
_AdGenVdsl2VtucChanNumber_Object = MibTableColumn
adGenVdsl2VtucChanNumber = _AdGenVdsl2VtucChanNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 1),
    _AdGenVdsl2VtucChanNumber_Type()
)
adGenVdsl2VtucChanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanNumber.setStatus("current")
_AdGenVdsl2VtucChanReceivedBlks_Type = Counter32
_AdGenVdsl2VtucChanReceivedBlks_Object = MibTableColumn
adGenVdsl2VtucChanReceivedBlks = _AdGenVdsl2VtucChanReceivedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 2),
    _AdGenVdsl2VtucChanReceivedBlks_Type()
)
adGenVdsl2VtucChanReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanReceivedBlks.setStatus("current")
_AdGenVdsl2VtucChanTransmittedBlks_Type = Counter32
_AdGenVdsl2VtucChanTransmittedBlks_Object = MibTableColumn
adGenVdsl2VtucChanTransmittedBlks = _AdGenVdsl2VtucChanTransmittedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 3),
    _AdGenVdsl2VtucChanTransmittedBlks_Type()
)
adGenVdsl2VtucChanTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanTransmittedBlks.setStatus("current")
_AdGenVdsl2VtucChanCorrectedBlks_Type = Counter32
_AdGenVdsl2VtucChanCorrectedBlks_Object = MibTableColumn
adGenVdsl2VtucChanCorrectedBlks = _AdGenVdsl2VtucChanCorrectedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 4),
    _AdGenVdsl2VtucChanCorrectedBlks_Type()
)
adGenVdsl2VtucChanCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanCorrectedBlks.setStatus("current")
_AdGenVdsl2VtucChanUncorrectBlks_Type = Counter32
_AdGenVdsl2VtucChanUncorrectBlks_Object = MibTableColumn
adGenVdsl2VtucChanUncorrectBlks = _AdGenVdsl2VtucChanUncorrectBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 5),
    _AdGenVdsl2VtucChanUncorrectBlks_Type()
)
adGenVdsl2VtucChanUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanUncorrectBlks.setStatus("current")


class _AdGenVdsl2VtucChanPerfValidIntervals_Type(Integer32):
    """Custom type adGenVdsl2VtucChanPerfValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenVdsl2VtucChanPerfValidIntervals_Type.__name__ = "Integer32"
_AdGenVdsl2VtucChanPerfValidIntervals_Object = MibTableColumn
adGenVdsl2VtucChanPerfValidIntervals = _AdGenVdsl2VtucChanPerfValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 6),
    _AdGenVdsl2VtucChanPerfValidIntervals_Type()
)
adGenVdsl2VtucChanPerfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfValidIntervals.setStatus("current")


class _AdGenVdsl2VtucChanPerfInvalidIntervals_Type(Integer32):
    """Custom type adGenVdsl2VtucChanPerfInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenVdsl2VtucChanPerfInvalidIntervals_Type.__name__ = "Integer32"
_AdGenVdsl2VtucChanPerfInvalidIntervals_Object = MibTableColumn
adGenVdsl2VtucChanPerfInvalidIntervals = _AdGenVdsl2VtucChanPerfInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 7),
    _AdGenVdsl2VtucChanPerfInvalidIntervals_Type()
)
adGenVdsl2VtucChanPerfInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfInvalidIntervals.setStatus("current")


class _AdGenVdsl2VtucChanPerfCurr15MinTimeElapsed_Type(Gauge32):
    """Custom type adGenVdsl2VtucChanPerfCurr15MinTimeElapsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AdGenVdsl2VtucChanPerfCurr15MinTimeElapsed_Type.__name__ = "Gauge32"
_AdGenVdsl2VtucChanPerfCurr15MinTimeElapsed_Object = MibTableColumn
adGenVdsl2VtucChanPerfCurr15MinTimeElapsed = _AdGenVdsl2VtucChanPerfCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 8),
    _AdGenVdsl2VtucChanPerfCurr15MinTimeElapsed_Type()
)
adGenVdsl2VtucChanPerfCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr15MinTimeElapsed.setUnits("seconds")
_AdGenVdsl2VtucChanPerfCurr15MinReceivedBlks_Type = Counter32
_AdGenVdsl2VtucChanPerfCurr15MinReceivedBlks_Object = MibTableColumn
adGenVdsl2VtucChanPerfCurr15MinReceivedBlks = _AdGenVdsl2VtucChanPerfCurr15MinReceivedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 9),
    _AdGenVdsl2VtucChanPerfCurr15MinReceivedBlks_Type()
)
adGenVdsl2VtucChanPerfCurr15MinReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr15MinReceivedBlks.setStatus("current")
_AdGenVdsl2VtucChanPerfCurr15MinTransmittedBlks_Type = Counter32
_AdGenVdsl2VtucChanPerfCurr15MinTransmittedBlks_Object = MibTableColumn
adGenVdsl2VtucChanPerfCurr15MinTransmittedBlks = _AdGenVdsl2VtucChanPerfCurr15MinTransmittedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 10),
    _AdGenVdsl2VtucChanPerfCurr15MinTransmittedBlks_Type()
)
adGenVdsl2VtucChanPerfCurr15MinTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr15MinTransmittedBlks.setStatus("current")
_AdGenVdsl2VtucChanPerfCurr15MinCorrectedBlks_Type = Counter32
_AdGenVdsl2VtucChanPerfCurr15MinCorrectedBlks_Object = MibTableColumn
adGenVdsl2VtucChanPerfCurr15MinCorrectedBlks = _AdGenVdsl2VtucChanPerfCurr15MinCorrectedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 11),
    _AdGenVdsl2VtucChanPerfCurr15MinCorrectedBlks_Type()
)
adGenVdsl2VtucChanPerfCurr15MinCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr15MinCorrectedBlks.setStatus("current")
_AdGenVdsl2VtucChanPerfCurr15MinUncorrectBlks_Type = Counter32
_AdGenVdsl2VtucChanPerfCurr15MinUncorrectBlks_Object = MibTableColumn
adGenVdsl2VtucChanPerfCurr15MinUncorrectBlks = _AdGenVdsl2VtucChanPerfCurr15MinUncorrectBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 12),
    _AdGenVdsl2VtucChanPerfCurr15MinUncorrectBlks_Type()
)
adGenVdsl2VtucChanPerfCurr15MinUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr15MinUncorrectBlks.setStatus("current")


class _AdGenVdsl2VtucChanPerfCurr1DayTimeElapsed_Type(Gauge32):
    """Custom type adGenVdsl2VtucChanPerfCurr1DayTimeElapsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_AdGenVdsl2VtucChanPerfCurr1DayTimeElapsed_Type.__name__ = "Gauge32"
_AdGenVdsl2VtucChanPerfCurr1DayTimeElapsed_Object = MibTableColumn
adGenVdsl2VtucChanPerfCurr1DayTimeElapsed = _AdGenVdsl2VtucChanPerfCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 13),
    _AdGenVdsl2VtucChanPerfCurr1DayTimeElapsed_Type()
)
adGenVdsl2VtucChanPerfCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr1DayTimeElapsed.setUnits("seconds")
_AdGenVdsl2VtucChanPerfCurr1DayReceivedBlks_Type = Counter32
_AdGenVdsl2VtucChanPerfCurr1DayReceivedBlks_Object = MibTableColumn
adGenVdsl2VtucChanPerfCurr1DayReceivedBlks = _AdGenVdsl2VtucChanPerfCurr1DayReceivedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 14),
    _AdGenVdsl2VtucChanPerfCurr1DayReceivedBlks_Type()
)
adGenVdsl2VtucChanPerfCurr1DayReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr1DayReceivedBlks.setStatus("current")
_AdGenVdsl2VtucChanPerfCurr1DayTransmittedBlks_Type = Counter32
_AdGenVdsl2VtucChanPerfCurr1DayTransmittedBlks_Object = MibTableColumn
adGenVdsl2VtucChanPerfCurr1DayTransmittedBlks = _AdGenVdsl2VtucChanPerfCurr1DayTransmittedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 15),
    _AdGenVdsl2VtucChanPerfCurr1DayTransmittedBlks_Type()
)
adGenVdsl2VtucChanPerfCurr1DayTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr1DayTransmittedBlks.setStatus("current")
_AdGenVdsl2VtucChanPerfCurr1DayCorrectedBlks_Type = Counter32
_AdGenVdsl2VtucChanPerfCurr1DayCorrectedBlks_Object = MibTableColumn
adGenVdsl2VtucChanPerfCurr1DayCorrectedBlks = _AdGenVdsl2VtucChanPerfCurr1DayCorrectedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 16),
    _AdGenVdsl2VtucChanPerfCurr1DayCorrectedBlks_Type()
)
adGenVdsl2VtucChanPerfCurr1DayCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr1DayCorrectedBlks.setStatus("current")
_AdGenVdsl2VtucChanPerfCurr1DayUncorrectBlks_Type = Counter32
_AdGenVdsl2VtucChanPerfCurr1DayUncorrectBlks_Object = MibTableColumn
adGenVdsl2VtucChanPerfCurr1DayUncorrectBlks = _AdGenVdsl2VtucChanPerfCurr1DayUncorrectBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 17),
    _AdGenVdsl2VtucChanPerfCurr1DayUncorrectBlks_Type()
)
adGenVdsl2VtucChanPerfCurr1DayUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr1DayUncorrectBlks.setStatus("current")
_AdGenVdsl2VtucChanPerfTcTxUnits_Type = Counter32
_AdGenVdsl2VtucChanPerfTcTxUnits_Object = MibTableColumn
adGenVdsl2VtucChanPerfTcTxUnits = _AdGenVdsl2VtucChanPerfTcTxUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 18),
    _AdGenVdsl2VtucChanPerfTcTxUnits_Type()
)
adGenVdsl2VtucChanPerfTcTxUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfTcTxUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfTcTxUnits.setUnits("pkts/cells")
_AdGenVdsl2VtucChanPerfTcTxDataUnits_Type = Counter32
_AdGenVdsl2VtucChanPerfTcTxDataUnits_Object = MibTableColumn
adGenVdsl2VtucChanPerfTcTxDataUnits = _AdGenVdsl2VtucChanPerfTcTxDataUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 19),
    _AdGenVdsl2VtucChanPerfTcTxDataUnits_Type()
)
adGenVdsl2VtucChanPerfTcTxDataUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfTcTxDataUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfTcTxDataUnits.setUnits("pkts/cells")
_AdGenVdsl2VtucChanPerfTcTxDataOctets_Type = Counter32
_AdGenVdsl2VtucChanPerfTcTxDataOctets_Object = MibTableColumn
adGenVdsl2VtucChanPerfTcTxDataOctets = _AdGenVdsl2VtucChanPerfTcTxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 20),
    _AdGenVdsl2VtucChanPerfTcTxDataOctets_Type()
)
adGenVdsl2VtucChanPerfTcTxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfTcTxDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfTcTxDataOctets.setUnits("octets")
_AdGenVdsl2VtucChanPerfTcTxIdleUnits_Type = Counter32
_AdGenVdsl2VtucChanPerfTcTxIdleUnits_Object = MibTableColumn
adGenVdsl2VtucChanPerfTcTxIdleUnits = _AdGenVdsl2VtucChanPerfTcTxIdleUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 21),
    _AdGenVdsl2VtucChanPerfTcTxIdleUnits_Type()
)
adGenVdsl2VtucChanPerfTcTxIdleUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfTcTxIdleUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfTcTxIdleUnits.setUnits("pkts/cells")
_AdGenVdsl2VtucChanPerfTcRxUnits_Type = Counter32
_AdGenVdsl2VtucChanPerfTcRxUnits_Object = MibTableColumn
adGenVdsl2VtucChanPerfTcRxUnits = _AdGenVdsl2VtucChanPerfTcRxUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 22),
    _AdGenVdsl2VtucChanPerfTcRxUnits_Type()
)
adGenVdsl2VtucChanPerfTcRxUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfTcRxUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfTcRxUnits.setUnits("pkts/cells")
_AdGenVdsl2VtucChanPerfTcRxDataUnits_Type = Counter32
_AdGenVdsl2VtucChanPerfTcRxDataUnits_Object = MibTableColumn
adGenVdsl2VtucChanPerfTcRxDataUnits = _AdGenVdsl2VtucChanPerfTcRxDataUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 23),
    _AdGenVdsl2VtucChanPerfTcRxDataUnits_Type()
)
adGenVdsl2VtucChanPerfTcRxDataUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfTcRxDataUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfTcRxDataUnits.setUnits("pkts/cells")
_AdGenVdsl2VtucChanPerfTcRxDataOctets_Type = Counter32
_AdGenVdsl2VtucChanPerfTcRxDataOctets_Object = MibTableColumn
adGenVdsl2VtucChanPerfTcRxDataOctets = _AdGenVdsl2VtucChanPerfTcRxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 24),
    _AdGenVdsl2VtucChanPerfTcRxDataOctets_Type()
)
adGenVdsl2VtucChanPerfTcRxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfTcRxDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfTcRxDataOctets.setUnits("octets")
_AdGenVdsl2VtucChanPerfTcRxIdleUnits_Type = Counter32
_AdGenVdsl2VtucChanPerfTcRxIdleUnits_Object = MibTableColumn
adGenVdsl2VtucChanPerfTcRxIdleUnits = _AdGenVdsl2VtucChanPerfTcRxIdleUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 25),
    _AdGenVdsl2VtucChanPerfTcRxIdleUnits_Type()
)
adGenVdsl2VtucChanPerfTcRxIdleUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfTcRxIdleUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfTcRxIdleUnits.setUnits("pkts/cells")
_AdGenVdsl2VtucChanPerfTcRxErroredUnits_Type = Counter32
_AdGenVdsl2VtucChanPerfTcRxErroredUnits_Object = MibTableColumn
adGenVdsl2VtucChanPerfTcRxErroredUnits = _AdGenVdsl2VtucChanPerfTcRxErroredUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 26),
    _AdGenVdsl2VtucChanPerfTcRxErroredUnits_Type()
)
adGenVdsl2VtucChanPerfTcRxErroredUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfTcRxErroredUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfTcRxErroredUnits.setUnits("pkts/cells")
_AdGenVdsl2VtucChanPerfRtxUncorrectedDtu_Type = Counter32
_AdGenVdsl2VtucChanPerfRtxUncorrectedDtu_Object = MibTableColumn
adGenVdsl2VtucChanPerfRtxUncorrectedDtu = _AdGenVdsl2VtucChanPerfRtxUncorrectedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 27),
    _AdGenVdsl2VtucChanPerfRtxUncorrectedDtu_Type()
)
adGenVdsl2VtucChanPerfRtxUncorrectedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfRtxUncorrectedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfRtxUncorrectedDtu.setUnits("dtus")
_AdGenVdsl2VtucChanPerfRtxCorrectedDtu_Type = Counter32
_AdGenVdsl2VtucChanPerfRtxCorrectedDtu_Object = MibTableColumn
adGenVdsl2VtucChanPerfRtxCorrectedDtu = _AdGenVdsl2VtucChanPerfRtxCorrectedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 28),
    _AdGenVdsl2VtucChanPerfRtxCorrectedDtu_Type()
)
adGenVdsl2VtucChanPerfRtxCorrectedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfRtxCorrectedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfRtxCorrectedDtu.setUnits("dtus")
_AdGenVdsl2VtucChanPerfRtxRetransmittedDtu_Type = Counter32
_AdGenVdsl2VtucChanPerfRtxRetransmittedDtu_Object = MibTableColumn
adGenVdsl2VtucChanPerfRtxRetransmittedDtu = _AdGenVdsl2VtucChanPerfRtxRetransmittedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 29),
    _AdGenVdsl2VtucChanPerfRtxRetransmittedDtu_Type()
)
adGenVdsl2VtucChanPerfRtxRetransmittedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfRtxRetransmittedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfRtxRetransmittedDtu.setUnits("dtus")
_AdGenVdsl2VtucChanPerfCurr15MinRtxUncorrectedDtu_Type = Counter32
_AdGenVdsl2VtucChanPerfCurr15MinRtxUncorrectedDtu_Object = MibTableColumn
adGenVdsl2VtucChanPerfCurr15MinRtxUncorrectedDtu = _AdGenVdsl2VtucChanPerfCurr15MinRtxUncorrectedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 30),
    _AdGenVdsl2VtucChanPerfCurr15MinRtxUncorrectedDtu_Type()
)
adGenVdsl2VtucChanPerfCurr15MinRtxUncorrectedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr15MinRtxUncorrectedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr15MinRtxUncorrectedDtu.setUnits("dtus")
_AdGenVdsl2VtucChanPerfCurr15MinRtxCorrectedDtu_Type = Counter32
_AdGenVdsl2VtucChanPerfCurr15MinRtxCorrectedDtu_Object = MibTableColumn
adGenVdsl2VtucChanPerfCurr15MinRtxCorrectedDtu = _AdGenVdsl2VtucChanPerfCurr15MinRtxCorrectedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 31),
    _AdGenVdsl2VtucChanPerfCurr15MinRtxCorrectedDtu_Type()
)
adGenVdsl2VtucChanPerfCurr15MinRtxCorrectedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr15MinRtxCorrectedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr15MinRtxCorrectedDtu.setUnits("dtus")
_AdGenVdsl2VtucChanPerfCurr15MinRtxRetransmittedDtu_Type = Counter32
_AdGenVdsl2VtucChanPerfCurr15MinRtxRetransmittedDtu_Object = MibTableColumn
adGenVdsl2VtucChanPerfCurr15MinRtxRetransmittedDtu = _AdGenVdsl2VtucChanPerfCurr15MinRtxRetransmittedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 32),
    _AdGenVdsl2VtucChanPerfCurr15MinRtxRetransmittedDtu_Type()
)
adGenVdsl2VtucChanPerfCurr15MinRtxRetransmittedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr15MinRtxRetransmittedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr15MinRtxRetransmittedDtu.setUnits("dtus")
_AdGenVdsl2VtucChanPerfCurr1DayRtxUncorrectedDtu_Type = Counter32
_AdGenVdsl2VtucChanPerfCurr1DayRtxUncorrectedDtu_Object = MibTableColumn
adGenVdsl2VtucChanPerfCurr1DayRtxUncorrectedDtu = _AdGenVdsl2VtucChanPerfCurr1DayRtxUncorrectedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 33),
    _AdGenVdsl2VtucChanPerfCurr1DayRtxUncorrectedDtu_Type()
)
adGenVdsl2VtucChanPerfCurr1DayRtxUncorrectedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr1DayRtxUncorrectedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr1DayRtxUncorrectedDtu.setUnits("dtus")
_AdGenVdsl2VtucChanPerfCurr1DayRtxCorrectedDtu_Type = Counter32
_AdGenVdsl2VtucChanPerfCurr1DayRtxCorrectedDtu_Object = MibTableColumn
adGenVdsl2VtucChanPerfCurr1DayRtxCorrectedDtu = _AdGenVdsl2VtucChanPerfCurr1DayRtxCorrectedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 34),
    _AdGenVdsl2VtucChanPerfCurr1DayRtxCorrectedDtu_Type()
)
adGenVdsl2VtucChanPerfCurr1DayRtxCorrectedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr1DayRtxCorrectedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr1DayRtxCorrectedDtu.setUnits("dtus")
_AdGenVdsl2VtucChanPerfCurr1DayRtxRetransmittedDtu_Type = Counter32
_AdGenVdsl2VtucChanPerfCurr1DayRtxRetransmittedDtu_Object = MibTableColumn
adGenVdsl2VtucChanPerfCurr1DayRtxRetransmittedDtu = _AdGenVdsl2VtucChanPerfCurr1DayRtxRetransmittedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 5, 1, 35),
    _AdGenVdsl2VtucChanPerfCurr1DayRtxRetransmittedDtu_Type()
)
adGenVdsl2VtucChanPerfCurr1DayRtxRetransmittedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr1DayRtxRetransmittedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanPerfCurr1DayRtxRetransmittedDtu.setUnits("dtus")
_AdGenVdsl2VturChanPerfDataTable_Object = MibTable
adGenVdsl2VturChanPerfDataTable = _AdGenVdsl2VturChanPerfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6)
)
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfDataTable.setStatus("current")
_AdGenVdsl2VturChanPerfDataEntry_Object = MibTableRow
adGenVdsl2VturChanPerfDataEntry = _AdGenVdsl2VturChanPerfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1)
)
adGenVdsl2VturChanPerfDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanNumber"),
)
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfDataEntry.setStatus("current")


class _AdGenVdsl2VturChanNumber_Type(Integer32):
    """Custom type adGenVdsl2VturChanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AdGenVdsl2VturChanNumber_Type.__name__ = "Integer32"
_AdGenVdsl2VturChanNumber_Object = MibTableColumn
adGenVdsl2VturChanNumber = _AdGenVdsl2VturChanNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 1),
    _AdGenVdsl2VturChanNumber_Type()
)
adGenVdsl2VturChanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanNumber.setStatus("current")
_AdGenVdsl2VturChanReceivedBlks_Type = Counter32
_AdGenVdsl2VturChanReceivedBlks_Object = MibTableColumn
adGenVdsl2VturChanReceivedBlks = _AdGenVdsl2VturChanReceivedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 2),
    _AdGenVdsl2VturChanReceivedBlks_Type()
)
adGenVdsl2VturChanReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanReceivedBlks.setStatus("current")
_AdGenVdsl2VturChanTransmittedBlks_Type = Counter32
_AdGenVdsl2VturChanTransmittedBlks_Object = MibTableColumn
adGenVdsl2VturChanTransmittedBlks = _AdGenVdsl2VturChanTransmittedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 3),
    _AdGenVdsl2VturChanTransmittedBlks_Type()
)
adGenVdsl2VturChanTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanTransmittedBlks.setStatus("current")
_AdGenVdsl2VturChanCorrectedBlks_Type = Counter32
_AdGenVdsl2VturChanCorrectedBlks_Object = MibTableColumn
adGenVdsl2VturChanCorrectedBlks = _AdGenVdsl2VturChanCorrectedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 4),
    _AdGenVdsl2VturChanCorrectedBlks_Type()
)
adGenVdsl2VturChanCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanCorrectedBlks.setStatus("current")
_AdGenVdsl2VturChanUncorrectBlks_Type = Counter32
_AdGenVdsl2VturChanUncorrectBlks_Object = MibTableColumn
adGenVdsl2VturChanUncorrectBlks = _AdGenVdsl2VturChanUncorrectBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 5),
    _AdGenVdsl2VturChanUncorrectBlks_Type()
)
adGenVdsl2VturChanUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanUncorrectBlks.setStatus("current")


class _AdGenVdsl2VturChanPerfValidIntervals_Type(Integer32):
    """Custom type adGenVdsl2VturChanPerfValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenVdsl2VturChanPerfValidIntervals_Type.__name__ = "Integer32"
_AdGenVdsl2VturChanPerfValidIntervals_Object = MibTableColumn
adGenVdsl2VturChanPerfValidIntervals = _AdGenVdsl2VturChanPerfValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 6),
    _AdGenVdsl2VturChanPerfValidIntervals_Type()
)
adGenVdsl2VturChanPerfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfValidIntervals.setStatus("current")


class _AdGenVdsl2VturChanPerfInvalidIntervals_Type(Integer32):
    """Custom type adGenVdsl2VturChanPerfInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenVdsl2VturChanPerfInvalidIntervals_Type.__name__ = "Integer32"
_AdGenVdsl2VturChanPerfInvalidIntervals_Object = MibTableColumn
adGenVdsl2VturChanPerfInvalidIntervals = _AdGenVdsl2VturChanPerfInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 7),
    _AdGenVdsl2VturChanPerfInvalidIntervals_Type()
)
adGenVdsl2VturChanPerfInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfInvalidIntervals.setStatus("current")


class _AdGenVdsl2VturChanPerfCurr15MinTimeElapsed_Type(Gauge32):
    """Custom type adGenVdsl2VturChanPerfCurr15MinTimeElapsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_AdGenVdsl2VturChanPerfCurr15MinTimeElapsed_Type.__name__ = "Gauge32"
_AdGenVdsl2VturChanPerfCurr15MinTimeElapsed_Object = MibTableColumn
adGenVdsl2VturChanPerfCurr15MinTimeElapsed = _AdGenVdsl2VturChanPerfCurr15MinTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 8),
    _AdGenVdsl2VturChanPerfCurr15MinTimeElapsed_Type()
)
adGenVdsl2VturChanPerfCurr15MinTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr15MinTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr15MinTimeElapsed.setUnits("seconds")
_AdGenVdsl2VturChanPerfCurr15MinReceivedBlks_Type = Counter32
_AdGenVdsl2VturChanPerfCurr15MinReceivedBlks_Object = MibTableColumn
adGenVdsl2VturChanPerfCurr15MinReceivedBlks = _AdGenVdsl2VturChanPerfCurr15MinReceivedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 9),
    _AdGenVdsl2VturChanPerfCurr15MinReceivedBlks_Type()
)
adGenVdsl2VturChanPerfCurr15MinReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr15MinReceivedBlks.setStatus("current")
_AdGenVdsl2VturChanPerfCurr15MinTransmittedBlks_Type = Counter32
_AdGenVdsl2VturChanPerfCurr15MinTransmittedBlks_Object = MibTableColumn
adGenVdsl2VturChanPerfCurr15MinTransmittedBlks = _AdGenVdsl2VturChanPerfCurr15MinTransmittedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 10),
    _AdGenVdsl2VturChanPerfCurr15MinTransmittedBlks_Type()
)
adGenVdsl2VturChanPerfCurr15MinTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr15MinTransmittedBlks.setStatus("current")
_AdGenVdsl2VturChanPerfCurr15MinCorrectedBlks_Type = Counter32
_AdGenVdsl2VturChanPerfCurr15MinCorrectedBlks_Object = MibTableColumn
adGenVdsl2VturChanPerfCurr15MinCorrectedBlks = _AdGenVdsl2VturChanPerfCurr15MinCorrectedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 11),
    _AdGenVdsl2VturChanPerfCurr15MinCorrectedBlks_Type()
)
adGenVdsl2VturChanPerfCurr15MinCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr15MinCorrectedBlks.setStatus("current")
_AdGenVdsl2VturChanPerfCurr15MinUncorrectBlks_Type = Counter32
_AdGenVdsl2VturChanPerfCurr15MinUncorrectBlks_Object = MibTableColumn
adGenVdsl2VturChanPerfCurr15MinUncorrectBlks = _AdGenVdsl2VturChanPerfCurr15MinUncorrectBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 12),
    _AdGenVdsl2VturChanPerfCurr15MinUncorrectBlks_Type()
)
adGenVdsl2VturChanPerfCurr15MinUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr15MinUncorrectBlks.setStatus("current")


class _AdGenVdsl2VturChanPerfCurr1DayTimeElapsed_Type(Gauge32):
    """Custom type adGenVdsl2VturChanPerfCurr1DayTimeElapsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_AdGenVdsl2VturChanPerfCurr1DayTimeElapsed_Type.__name__ = "Gauge32"
_AdGenVdsl2VturChanPerfCurr1DayTimeElapsed_Object = MibTableColumn
adGenVdsl2VturChanPerfCurr1DayTimeElapsed = _AdGenVdsl2VturChanPerfCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 13),
    _AdGenVdsl2VturChanPerfCurr1DayTimeElapsed_Type()
)
adGenVdsl2VturChanPerfCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr1DayTimeElapsed.setUnits("seconds")
_AdGenVdsl2VturChanPerfCurr1DayReceivedBlks_Type = Counter32
_AdGenVdsl2VturChanPerfCurr1DayReceivedBlks_Object = MibTableColumn
adGenVdsl2VturChanPerfCurr1DayReceivedBlks = _AdGenVdsl2VturChanPerfCurr1DayReceivedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 14),
    _AdGenVdsl2VturChanPerfCurr1DayReceivedBlks_Type()
)
adGenVdsl2VturChanPerfCurr1DayReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr1DayReceivedBlks.setStatus("current")
_AdGenVdsl2VturChanPerfCurr1DayTransmittedBlks_Type = Counter32
_AdGenVdsl2VturChanPerfCurr1DayTransmittedBlks_Object = MibTableColumn
adGenVdsl2VturChanPerfCurr1DayTransmittedBlks = _AdGenVdsl2VturChanPerfCurr1DayTransmittedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 15),
    _AdGenVdsl2VturChanPerfCurr1DayTransmittedBlks_Type()
)
adGenVdsl2VturChanPerfCurr1DayTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr1DayTransmittedBlks.setStatus("current")
_AdGenVdsl2VturChanPerfCurr1DayCorrectedBlks_Type = Counter32
_AdGenVdsl2VturChanPerfCurr1DayCorrectedBlks_Object = MibTableColumn
adGenVdsl2VturChanPerfCurr1DayCorrectedBlks = _AdGenVdsl2VturChanPerfCurr1DayCorrectedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 16),
    _AdGenVdsl2VturChanPerfCurr1DayCorrectedBlks_Type()
)
adGenVdsl2VturChanPerfCurr1DayCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr1DayCorrectedBlks.setStatus("current")
_AdGenVdsl2VturChanPerfCurr1DayUncorrectBlks_Type = Counter32
_AdGenVdsl2VturChanPerfCurr1DayUncorrectBlks_Object = MibTableColumn
adGenVdsl2VturChanPerfCurr1DayUncorrectBlks = _AdGenVdsl2VturChanPerfCurr1DayUncorrectBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 17),
    _AdGenVdsl2VturChanPerfCurr1DayUncorrectBlks_Type()
)
adGenVdsl2VturChanPerfCurr1DayUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr1DayUncorrectBlks.setStatus("current")
_AdGenVdsl2VturChanPerfTcTxUnits_Type = Counter32
_AdGenVdsl2VturChanPerfTcTxUnits_Object = MibTableColumn
adGenVdsl2VturChanPerfTcTxUnits = _AdGenVdsl2VturChanPerfTcTxUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 18),
    _AdGenVdsl2VturChanPerfTcTxUnits_Type()
)
adGenVdsl2VturChanPerfTcTxUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfTcTxUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfTcTxUnits.setUnits("pkts/cells")
_AdGenVdsl2VturChanPerfTcTxDataUnits_Type = Counter32
_AdGenVdsl2VturChanPerfTcTxDataUnits_Object = MibTableColumn
adGenVdsl2VturChanPerfTcTxDataUnits = _AdGenVdsl2VturChanPerfTcTxDataUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 19),
    _AdGenVdsl2VturChanPerfTcTxDataUnits_Type()
)
adGenVdsl2VturChanPerfTcTxDataUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfTcTxDataUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfTcTxDataUnits.setUnits("pkts/cells")
_AdGenVdsl2VturChanPerfTcTxDataOctets_Type = Counter32
_AdGenVdsl2VturChanPerfTcTxDataOctets_Object = MibTableColumn
adGenVdsl2VturChanPerfTcTxDataOctets = _AdGenVdsl2VturChanPerfTcTxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 20),
    _AdGenVdsl2VturChanPerfTcTxDataOctets_Type()
)
adGenVdsl2VturChanPerfTcTxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfTcTxDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfTcTxDataOctets.setUnits("octets")
_AdGenVdsl2VturChanPerfTcTxIdleUnits_Type = Counter32
_AdGenVdsl2VturChanPerfTcTxIdleUnits_Object = MibTableColumn
adGenVdsl2VturChanPerfTcTxIdleUnits = _AdGenVdsl2VturChanPerfTcTxIdleUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 21),
    _AdGenVdsl2VturChanPerfTcTxIdleUnits_Type()
)
adGenVdsl2VturChanPerfTcTxIdleUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfTcTxIdleUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfTcTxIdleUnits.setUnits("pkts/cells")
_AdGenVdsl2VturChanPerfTcRxUnits_Type = Counter32
_AdGenVdsl2VturChanPerfTcRxUnits_Object = MibTableColumn
adGenVdsl2VturChanPerfTcRxUnits = _AdGenVdsl2VturChanPerfTcRxUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 22),
    _AdGenVdsl2VturChanPerfTcRxUnits_Type()
)
adGenVdsl2VturChanPerfTcRxUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfTcRxUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfTcRxUnits.setUnits("pkts/cells")
_AdGenVdsl2VturChanPerfTcRxDataUnits_Type = Counter32
_AdGenVdsl2VturChanPerfTcRxDataUnits_Object = MibTableColumn
adGenVdsl2VturChanPerfTcRxDataUnits = _AdGenVdsl2VturChanPerfTcRxDataUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 23),
    _AdGenVdsl2VturChanPerfTcRxDataUnits_Type()
)
adGenVdsl2VturChanPerfTcRxDataUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfTcRxDataUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfTcRxDataUnits.setUnits("pkts/cells")
_AdGenVdsl2VturChanPerfTcRxDataOctets_Type = Counter32
_AdGenVdsl2VturChanPerfTcRxDataOctets_Object = MibTableColumn
adGenVdsl2VturChanPerfTcRxDataOctets = _AdGenVdsl2VturChanPerfTcRxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 24),
    _AdGenVdsl2VturChanPerfTcRxDataOctets_Type()
)
adGenVdsl2VturChanPerfTcRxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfTcRxDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfTcRxDataOctets.setUnits("octets")
_AdGenVdsl2VturChanPerfTcRxIdleUnits_Type = Counter32
_AdGenVdsl2VturChanPerfTcRxIdleUnits_Object = MibTableColumn
adGenVdsl2VturChanPerfTcRxIdleUnits = _AdGenVdsl2VturChanPerfTcRxIdleUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 25),
    _AdGenVdsl2VturChanPerfTcRxIdleUnits_Type()
)
adGenVdsl2VturChanPerfTcRxIdleUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfTcRxIdleUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfTcRxIdleUnits.setUnits("pkts/cells")
_AdGenVdsl2VturChanPerfTcRxErroredUnits_Type = Counter32
_AdGenVdsl2VturChanPerfTcRxErroredUnits_Object = MibTableColumn
adGenVdsl2VturChanPerfTcRxErroredUnits = _AdGenVdsl2VturChanPerfTcRxErroredUnits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 26),
    _AdGenVdsl2VturChanPerfTcRxErroredUnits_Type()
)
adGenVdsl2VturChanPerfTcRxErroredUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfTcRxErroredUnits.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfTcRxErroredUnits.setUnits("pkts/cells")
_AdGenVdsl2VturChanPerfRtxUncorrectedDtu_Type = Counter32
_AdGenVdsl2VturChanPerfRtxUncorrectedDtu_Object = MibTableColumn
adGenVdsl2VturChanPerfRtxUncorrectedDtu = _AdGenVdsl2VturChanPerfRtxUncorrectedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 27),
    _AdGenVdsl2VturChanPerfRtxUncorrectedDtu_Type()
)
adGenVdsl2VturChanPerfRtxUncorrectedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfRtxUncorrectedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfRtxUncorrectedDtu.setUnits("dtus")
_AdGenVdsl2VturChanPerfRtxCorrectedDtu_Type = Counter32
_AdGenVdsl2VturChanPerfRtxCorrectedDtu_Object = MibTableColumn
adGenVdsl2VturChanPerfRtxCorrectedDtu = _AdGenVdsl2VturChanPerfRtxCorrectedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 28),
    _AdGenVdsl2VturChanPerfRtxCorrectedDtu_Type()
)
adGenVdsl2VturChanPerfRtxCorrectedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfRtxCorrectedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfRtxCorrectedDtu.setUnits("dtus")
_AdGenVdsl2VturChanPerfRtxRetransmittedDtu_Type = Counter32
_AdGenVdsl2VturChanPerfRtxRetransmittedDtu_Object = MibTableColumn
adGenVdsl2VturChanPerfRtxRetransmittedDtu = _AdGenVdsl2VturChanPerfRtxRetransmittedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 29),
    _AdGenVdsl2VturChanPerfRtxRetransmittedDtu_Type()
)
adGenVdsl2VturChanPerfRtxRetransmittedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfRtxRetransmittedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfRtxRetransmittedDtu.setUnits("dtus")
_AdGenVdsl2VturChanPerfCurr15MinRtxUncorrectedDtu_Type = Counter32
_AdGenVdsl2VturChanPerfCurr15MinRtxUncorrectedDtu_Object = MibTableColumn
adGenVdsl2VturChanPerfCurr15MinRtxUncorrectedDtu = _AdGenVdsl2VturChanPerfCurr15MinRtxUncorrectedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 30),
    _AdGenVdsl2VturChanPerfCurr15MinRtxUncorrectedDtu_Type()
)
adGenVdsl2VturChanPerfCurr15MinRtxUncorrectedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr15MinRtxUncorrectedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr15MinRtxUncorrectedDtu.setUnits("dtus")
_AdGenVdsl2VturChanPerfCurr15MinRtxCorrectedDtu_Type = Counter32
_AdGenVdsl2VturChanPerfCurr15MinRtxCorrectedDtu_Object = MibTableColumn
adGenVdsl2VturChanPerfCurr15MinRtxCorrectedDtu = _AdGenVdsl2VturChanPerfCurr15MinRtxCorrectedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 31),
    _AdGenVdsl2VturChanPerfCurr15MinRtxCorrectedDtu_Type()
)
adGenVdsl2VturChanPerfCurr15MinRtxCorrectedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr15MinRtxCorrectedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr15MinRtxCorrectedDtu.setUnits("dtus")
_AdGenVdsl2VturChanPerfCurr15MinRtxRetransmittedDtu_Type = Counter32
_AdGenVdsl2VturChanPerfCurr15MinRtxRetransmittedDtu_Object = MibTableColumn
adGenVdsl2VturChanPerfCurr15MinRtxRetransmittedDtu = _AdGenVdsl2VturChanPerfCurr15MinRtxRetransmittedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 32),
    _AdGenVdsl2VturChanPerfCurr15MinRtxRetransmittedDtu_Type()
)
adGenVdsl2VturChanPerfCurr15MinRtxRetransmittedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr15MinRtxRetransmittedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr15MinRtxRetransmittedDtu.setUnits("dtus")
_AdGenVdsl2VturChanPerfCurr1DayRtxUncorrectedDtu_Type = Counter32
_AdGenVdsl2VturChanPerfCurr1DayRtxUncorrectedDtu_Object = MibTableColumn
adGenVdsl2VturChanPerfCurr1DayRtxUncorrectedDtu = _AdGenVdsl2VturChanPerfCurr1DayRtxUncorrectedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 33),
    _AdGenVdsl2VturChanPerfCurr1DayRtxUncorrectedDtu_Type()
)
adGenVdsl2VturChanPerfCurr1DayRtxUncorrectedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr1DayRtxUncorrectedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr1DayRtxUncorrectedDtu.setUnits("dtus")
_AdGenVdsl2VturChanPerfCurr1DayRtxCorrectedDtu_Type = Counter32
_AdGenVdsl2VturChanPerfCurr1DayRtxCorrectedDtu_Object = MibTableColumn
adGenVdsl2VturChanPerfCurr1DayRtxCorrectedDtu = _AdGenVdsl2VturChanPerfCurr1DayRtxCorrectedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 34),
    _AdGenVdsl2VturChanPerfCurr1DayRtxCorrectedDtu_Type()
)
adGenVdsl2VturChanPerfCurr1DayRtxCorrectedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr1DayRtxCorrectedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr1DayRtxCorrectedDtu.setUnits("dtus")
_AdGenVdsl2VturChanPerfCurr1DayRtxRetransmittedDtu_Type = Counter32
_AdGenVdsl2VturChanPerfCurr1DayRtxRetransmittedDtu_Object = MibTableColumn
adGenVdsl2VturChanPerfCurr1DayRtxRetransmittedDtu = _AdGenVdsl2VturChanPerfCurr1DayRtxRetransmittedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 6, 1, 35),
    _AdGenVdsl2VturChanPerfCurr1DayRtxRetransmittedDtu_Type()
)
adGenVdsl2VturChanPerfCurr1DayRtxRetransmittedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr1DayRtxRetransmittedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanPerfCurr1DayRtxRetransmittedDtu.setUnits("dtus")
_AdGenVdsl2VtucChanIntervalTable_Object = MibTable
adGenVdsl2VtucChanIntervalTable = _AdGenVdsl2VtucChanIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 7)
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanIntervalTable.setStatus("current")
_AdGenVdsl2VtucChanIntervalEntry_Object = MibTableRow
adGenVdsl2VtucChanIntervalEntry = _AdGenVdsl2VtucChanIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 7, 1)
)
adGenVdsl2VtucChanIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanNum"),
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanIntervalEntry.setStatus("current")


class _AdGenVdsl2VtucChanNum_Type(Integer32):
    """Custom type adGenVdsl2VtucChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AdGenVdsl2VtucChanNum_Type.__name__ = "Integer32"
_AdGenVdsl2VtucChanNum_Object = MibTableColumn
adGenVdsl2VtucChanNum = _AdGenVdsl2VtucChanNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 7, 1, 1),
    _AdGenVdsl2VtucChanNum_Type()
)
adGenVdsl2VtucChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanNum.setStatus("current")


class _AdGenVdsl2VtucChanIntervalNumber_Type(Integer32):
    """Custom type adGenVdsl2VtucChanIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdGenVdsl2VtucChanIntervalNumber_Type.__name__ = "Integer32"
_AdGenVdsl2VtucChanIntervalNumber_Object = MibTableColumn
adGenVdsl2VtucChanIntervalNumber = _AdGenVdsl2VtucChanIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 7, 1, 2),
    _AdGenVdsl2VtucChanIntervalNumber_Type()
)
adGenVdsl2VtucChanIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanIntervalNumber.setStatus("current")
_AdGenVdsl2VtucChanIntervalReceivedBlks_Type = Counter32
_AdGenVdsl2VtucChanIntervalReceivedBlks_Object = MibTableColumn
adGenVdsl2VtucChanIntervalReceivedBlks = _AdGenVdsl2VtucChanIntervalReceivedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 7, 1, 3),
    _AdGenVdsl2VtucChanIntervalReceivedBlks_Type()
)
adGenVdsl2VtucChanIntervalReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanIntervalReceivedBlks.setStatus("current")
_AdGenVdsl2VtucChanIntervalTransmittedBlks_Type = Counter32
_AdGenVdsl2VtucChanIntervalTransmittedBlks_Object = MibTableColumn
adGenVdsl2VtucChanIntervalTransmittedBlks = _AdGenVdsl2VtucChanIntervalTransmittedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 7, 1, 4),
    _AdGenVdsl2VtucChanIntervalTransmittedBlks_Type()
)
adGenVdsl2VtucChanIntervalTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanIntervalTransmittedBlks.setStatus("current")
_AdGenVdsl2VtucChanIntervalCorrectedBlks_Type = Counter32
_AdGenVdsl2VtucChanIntervalCorrectedBlks_Object = MibTableColumn
adGenVdsl2VtucChanIntervalCorrectedBlks = _AdGenVdsl2VtucChanIntervalCorrectedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 7, 1, 5),
    _AdGenVdsl2VtucChanIntervalCorrectedBlks_Type()
)
adGenVdsl2VtucChanIntervalCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanIntervalCorrectedBlks.setStatus("current")
_AdGenVdsl2VtucChanIntervalUncorrectBlks_Type = Counter32
_AdGenVdsl2VtucChanIntervalUncorrectBlks_Object = MibTableColumn
adGenVdsl2VtucChanIntervalUncorrectBlks = _AdGenVdsl2VtucChanIntervalUncorrectBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 7, 1, 6),
    _AdGenVdsl2VtucChanIntervalUncorrectBlks_Type()
)
adGenVdsl2VtucChanIntervalUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanIntervalUncorrectBlks.setStatus("current")


class _AdGenVdsl2VtucChanIntervalValidData_Type(Integer32):
    """Custom type adGenVdsl2VtucChanIntervalValidData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("notValid", 2))
    )


_AdGenVdsl2VtucChanIntervalValidData_Type.__name__ = "Integer32"
_AdGenVdsl2VtucChanIntervalValidData_Object = MibTableColumn
adGenVdsl2VtucChanIntervalValidData = _AdGenVdsl2VtucChanIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 7, 1, 7),
    _AdGenVdsl2VtucChanIntervalValidData_Type()
)
adGenVdsl2VtucChanIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanIntervalValidData.setStatus("current")
_AdGenVdsl2VtucChanIntervalRtxUncorrectedDtu_Type = Counter32
_AdGenVdsl2VtucChanIntervalRtxUncorrectedDtu_Object = MibTableColumn
adGenVdsl2VtucChanIntervalRtxUncorrectedDtu = _AdGenVdsl2VtucChanIntervalRtxUncorrectedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 7, 1, 8),
    _AdGenVdsl2VtucChanIntervalRtxUncorrectedDtu_Type()
)
adGenVdsl2VtucChanIntervalRtxUncorrectedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanIntervalRtxUncorrectedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanIntervalRtxUncorrectedDtu.setUnits("dtus")
_AdGenVdsl2VtucChanIntervalRtxCorrectedDtu_Type = Counter32
_AdGenVdsl2VtucChanIntervalRtxCorrectedDtu_Object = MibTableColumn
adGenVdsl2VtucChanIntervalRtxCorrectedDtu = _AdGenVdsl2VtucChanIntervalRtxCorrectedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 7, 1, 9),
    _AdGenVdsl2VtucChanIntervalRtxCorrectedDtu_Type()
)
adGenVdsl2VtucChanIntervalRtxCorrectedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanIntervalRtxCorrectedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanIntervalRtxCorrectedDtu.setUnits("dtus")
_AdGenVdsl2VtucChanIntervalRtxRetransmittedDtu_Type = Counter32
_AdGenVdsl2VtucChanIntervalRtxRetransmittedDtu_Object = MibTableColumn
adGenVdsl2VtucChanIntervalRtxRetransmittedDtu = _AdGenVdsl2VtucChanIntervalRtxRetransmittedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 7, 1, 10),
    _AdGenVdsl2VtucChanIntervalRtxRetransmittedDtu_Type()
)
adGenVdsl2VtucChanIntervalRtxRetransmittedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanIntervalRtxRetransmittedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChanIntervalRtxRetransmittedDtu.setUnits("dtus")
_AdGenVdsl2VturChanIntervalTable_Object = MibTable
adGenVdsl2VturChanIntervalTable = _AdGenVdsl2VturChanIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 8)
)
if mibBuilder.loadTexts:
    adGenVdsl2VturChanIntervalTable.setStatus("current")
_AdGenVdsl2VturChanIntervalEntry_Object = MibTableRow
adGenVdsl2VturChanIntervalEntry = _AdGenVdsl2VturChanIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 8, 1)
)
adGenVdsl2VturChanIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanNum"),
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenVdsl2VturChanIntervalEntry.setStatus("current")


class _AdGenVdsl2VturChanNum_Type(Integer32):
    """Custom type adGenVdsl2VturChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AdGenVdsl2VturChanNum_Type.__name__ = "Integer32"
_AdGenVdsl2VturChanNum_Object = MibTableColumn
adGenVdsl2VturChanNum = _AdGenVdsl2VturChanNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 8, 1, 1),
    _AdGenVdsl2VturChanNum_Type()
)
adGenVdsl2VturChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanNum.setStatus("current")


class _AdGenVdsl2VturChanIntervalNumber_Type(Integer32):
    """Custom type adGenVdsl2VturChanIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdGenVdsl2VturChanIntervalNumber_Type.__name__ = "Integer32"
_AdGenVdsl2VturChanIntervalNumber_Object = MibTableColumn
adGenVdsl2VturChanIntervalNumber = _AdGenVdsl2VturChanIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 8, 1, 2),
    _AdGenVdsl2VturChanIntervalNumber_Type()
)
adGenVdsl2VturChanIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanIntervalNumber.setStatus("current")
_AdGenVdsl2VturChanIntervalReceivedBlks_Type = Counter32
_AdGenVdsl2VturChanIntervalReceivedBlks_Object = MibTableColumn
adGenVdsl2VturChanIntervalReceivedBlks = _AdGenVdsl2VturChanIntervalReceivedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 8, 1, 3),
    _AdGenVdsl2VturChanIntervalReceivedBlks_Type()
)
adGenVdsl2VturChanIntervalReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanIntervalReceivedBlks.setStatus("current")
_AdGenVdsl2VturChanIntervalTransmittedBlks_Type = Counter32
_AdGenVdsl2VturChanIntervalTransmittedBlks_Object = MibTableColumn
adGenVdsl2VturChanIntervalTransmittedBlks = _AdGenVdsl2VturChanIntervalTransmittedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 8, 1, 4),
    _AdGenVdsl2VturChanIntervalTransmittedBlks_Type()
)
adGenVdsl2VturChanIntervalTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanIntervalTransmittedBlks.setStatus("current")
_AdGenVdsl2VturChanIntervalCorrectedBlks_Type = Counter32
_AdGenVdsl2VturChanIntervalCorrectedBlks_Object = MibTableColumn
adGenVdsl2VturChanIntervalCorrectedBlks = _AdGenVdsl2VturChanIntervalCorrectedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 8, 1, 5),
    _AdGenVdsl2VturChanIntervalCorrectedBlks_Type()
)
adGenVdsl2VturChanIntervalCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanIntervalCorrectedBlks.setStatus("current")
_AdGenVdsl2VturChanIntervalUncorrectBlks_Type = Counter32
_AdGenVdsl2VturChanIntervalUncorrectBlks_Object = MibTableColumn
adGenVdsl2VturChanIntervalUncorrectBlks = _AdGenVdsl2VturChanIntervalUncorrectBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 8, 1, 6),
    _AdGenVdsl2VturChanIntervalUncorrectBlks_Type()
)
adGenVdsl2VturChanIntervalUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanIntervalUncorrectBlks.setStatus("current")


class _AdGenVdsl2VturChanIntervalValidData_Type(Integer32):
    """Custom type adGenVdsl2VturChanIntervalValidData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("notValid", 2))
    )


_AdGenVdsl2VturChanIntervalValidData_Type.__name__ = "Integer32"
_AdGenVdsl2VturChanIntervalValidData_Object = MibTableColumn
adGenVdsl2VturChanIntervalValidData = _AdGenVdsl2VturChanIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 8, 1, 7),
    _AdGenVdsl2VturChanIntervalValidData_Type()
)
adGenVdsl2VturChanIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanIntervalValidData.setStatus("current")
_AdGenVdsl2VturChanIntervalRtxUncorrectedDtu_Type = Counter32
_AdGenVdsl2VturChanIntervalRtxUncorrectedDtu_Object = MibTableColumn
adGenVdsl2VturChanIntervalRtxUncorrectedDtu = _AdGenVdsl2VturChanIntervalRtxUncorrectedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 8, 1, 8),
    _AdGenVdsl2VturChanIntervalRtxUncorrectedDtu_Type()
)
adGenVdsl2VturChanIntervalRtxUncorrectedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanIntervalRtxUncorrectedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanIntervalRtxUncorrectedDtu.setUnits("dtus")
_AdGenVdsl2VturChanIntervalRtxCorrectedDtu_Type = Counter32
_AdGenVdsl2VturChanIntervalRtxCorrectedDtu_Object = MibTableColumn
adGenVdsl2VturChanIntervalRtxCorrectedDtu = _AdGenVdsl2VturChanIntervalRtxCorrectedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 8, 1, 9),
    _AdGenVdsl2VturChanIntervalRtxCorrectedDtu_Type()
)
adGenVdsl2VturChanIntervalRtxCorrectedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanIntervalRtxCorrectedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanIntervalRtxCorrectedDtu.setUnits("dtus")
_AdGenVdsl2VturChanIntervalRtxRetransmittedDtu_Type = Counter32
_AdGenVdsl2VturChanIntervalRtxRetransmittedDtu_Object = MibTableColumn
adGenVdsl2VturChanIntervalRtxRetransmittedDtu = _AdGenVdsl2VturChanIntervalRtxRetransmittedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 8, 1, 10),
    _AdGenVdsl2VturChanIntervalRtxRetransmittedDtu_Type()
)
adGenVdsl2VturChanIntervalRtxRetransmittedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanIntervalRtxRetransmittedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChanIntervalRtxRetransmittedDtu.setUnits("dtus")
_AdGenVdsl2Vtuc1DayIntervalTable_Object = MibTable
adGenVdsl2Vtuc1DayIntervalTable = _AdGenVdsl2Vtuc1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9)
)
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalTable.setStatus("current")
_AdGenVdsl2Vtuc1DayIntervalEntry_Object = MibTableRow
adGenVdsl2Vtuc1DayIntervalEntry = _AdGenVdsl2Vtuc1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9, 1)
)
adGenVdsl2Vtuc1DayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtuc1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalEntry.setStatus("current")


class _AdGenVdsl2Vtuc1DayIntervalNumber_Type(Integer32):
    """Custom type adGenVdsl2Vtuc1DayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AdGenVdsl2Vtuc1DayIntervalNumber_Type.__name__ = "Integer32"
_AdGenVdsl2Vtuc1DayIntervalNumber_Object = MibTableColumn
adGenVdsl2Vtuc1DayIntervalNumber = _AdGenVdsl2Vtuc1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9, 1, 1),
    _AdGenVdsl2Vtuc1DayIntervalNumber_Type()
)
adGenVdsl2Vtuc1DayIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalNumber.setStatus("current")
_AdGenVdsl2Vtuc1DayIntervalLofs_Type = Counter32
_AdGenVdsl2Vtuc1DayIntervalLofs_Object = MibTableColumn
adGenVdsl2Vtuc1DayIntervalLofs = _AdGenVdsl2Vtuc1DayIntervalLofs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9, 1, 2),
    _AdGenVdsl2Vtuc1DayIntervalLofs_Type()
)
adGenVdsl2Vtuc1DayIntervalLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalLofs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalLofs.setUnits("seconds")
_AdGenVdsl2Vtuc1DayIntervalLoss_Type = Counter32
_AdGenVdsl2Vtuc1DayIntervalLoss_Object = MibTableColumn
adGenVdsl2Vtuc1DayIntervalLoss = _AdGenVdsl2Vtuc1DayIntervalLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9, 1, 3),
    _AdGenVdsl2Vtuc1DayIntervalLoss_Type()
)
adGenVdsl2Vtuc1DayIntervalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalLoss.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalLoss.setUnits("seconds")
_AdGenVdsl2Vtuc1DayIntervalLols_Type = Counter32
_AdGenVdsl2Vtuc1DayIntervalLols_Object = MibTableColumn
adGenVdsl2Vtuc1DayIntervalLols = _AdGenVdsl2Vtuc1DayIntervalLols_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9, 1, 4),
    _AdGenVdsl2Vtuc1DayIntervalLols_Type()
)
adGenVdsl2Vtuc1DayIntervalLols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalLols.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalLols.setUnits("seconds")
_AdGenVdsl2Vtuc1DayIntervalLprs_Type = Counter32
_AdGenVdsl2Vtuc1DayIntervalLprs_Object = MibTableColumn
adGenVdsl2Vtuc1DayIntervalLprs = _AdGenVdsl2Vtuc1DayIntervalLprs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9, 1, 5),
    _AdGenVdsl2Vtuc1DayIntervalLprs_Type()
)
adGenVdsl2Vtuc1DayIntervalLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalLprs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalLprs.setUnits("seconds")
_AdGenVdsl2Vtuc1DayIntervalES_Type = Counter32
_AdGenVdsl2Vtuc1DayIntervalES_Object = MibTableColumn
adGenVdsl2Vtuc1DayIntervalES = _AdGenVdsl2Vtuc1DayIntervalES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9, 1, 6),
    _AdGenVdsl2Vtuc1DayIntervalES_Type()
)
adGenVdsl2Vtuc1DayIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalES.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalES.setUnits("seconds")
_AdGenVdsl2Vtuc1DayIntervalInits_Type = Counter32
_AdGenVdsl2Vtuc1DayIntervalInits_Object = MibTableColumn
adGenVdsl2Vtuc1DayIntervalInits = _AdGenVdsl2Vtuc1DayIntervalInits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9, 1, 7),
    _AdGenVdsl2Vtuc1DayIntervalInits_Type()
)
adGenVdsl2Vtuc1DayIntervalInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalInits.setStatus("current")


class _AdGenVdsl2Vtuc1DayIntervalValidData_Type(Integer32):
    """Custom type adGenVdsl2Vtuc1DayIntervalValidData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("notValid", 2))
    )


_AdGenVdsl2Vtuc1DayIntervalValidData_Type.__name__ = "Integer32"
_AdGenVdsl2Vtuc1DayIntervalValidData_Object = MibTableColumn
adGenVdsl2Vtuc1DayIntervalValidData = _AdGenVdsl2Vtuc1DayIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9, 1, 8),
    _AdGenVdsl2Vtuc1DayIntervalValidData_Type()
)
adGenVdsl2Vtuc1DayIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalValidData.setStatus("current")
_AdGenVdsl2Vtuc1DayIntervalSES_Type = Counter32
_AdGenVdsl2Vtuc1DayIntervalSES_Object = MibTableColumn
adGenVdsl2Vtuc1DayIntervalSES = _AdGenVdsl2Vtuc1DayIntervalSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9, 1, 9),
    _AdGenVdsl2Vtuc1DayIntervalSES_Type()
)
adGenVdsl2Vtuc1DayIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalSES.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalSES.setUnits("seconds")
_AdGenVdsl2Vtuc1DayIntervalUAS_Type = Counter32
_AdGenVdsl2Vtuc1DayIntervalUAS_Object = MibTableColumn
adGenVdsl2Vtuc1DayIntervalUAS = _AdGenVdsl2Vtuc1DayIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9, 1, 10),
    _AdGenVdsl2Vtuc1DayIntervalUAS_Type()
)
adGenVdsl2Vtuc1DayIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalUAS.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalUAS.setUnits("seconds")
_AdGenVdsl2Vtuc1DayIntervalFECs_Type = Counter32
_AdGenVdsl2Vtuc1DayIntervalFECs_Object = MibTableColumn
adGenVdsl2Vtuc1DayIntervalFECs = _AdGenVdsl2Vtuc1DayIntervalFECs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9, 1, 11),
    _AdGenVdsl2Vtuc1DayIntervalFECs_Type()
)
adGenVdsl2Vtuc1DayIntervalFECs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalFECs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalFECs.setUnits("seconds")
_AdGenVdsl2Vtuc1DayIntervalFEC_Type = Counter32
_AdGenVdsl2Vtuc1DayIntervalFEC_Object = MibTableColumn
adGenVdsl2Vtuc1DayIntervalFEC = _AdGenVdsl2Vtuc1DayIntervalFEC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9, 1, 12),
    _AdGenVdsl2Vtuc1DayIntervalFEC_Type()
)
adGenVdsl2Vtuc1DayIntervalFEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalFEC.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalFEC.setUnits("seconds")
_AdGenVdsl2Vtuc1DayIntervalCRC_Type = Counter32
_AdGenVdsl2Vtuc1DayIntervalCRC_Object = MibTableColumn
adGenVdsl2Vtuc1DayIntervalCRC = _AdGenVdsl2Vtuc1DayIntervalCRC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9, 1, 13),
    _AdGenVdsl2Vtuc1DayIntervalCRC_Type()
)
adGenVdsl2Vtuc1DayIntervalCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalCRC.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalCRC.setUnits("seconds")
_AdGenVdsl2Vtuc1DayIntervalSraDownshifts_Type = Counter32
_AdGenVdsl2Vtuc1DayIntervalSraDownshifts_Object = MibTableColumn
adGenVdsl2Vtuc1DayIntervalSraDownshifts = _AdGenVdsl2Vtuc1DayIntervalSraDownshifts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9, 1, 14),
    _AdGenVdsl2Vtuc1DayIntervalSraDownshifts_Type()
)
adGenVdsl2Vtuc1DayIntervalSraDownshifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalSraDownshifts.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalSraDownshifts.setUnits("downshifts")
_AdGenVdsl2Vtuc1DayIntervalSraUpshifts_Type = Counter32
_AdGenVdsl2Vtuc1DayIntervalSraUpshifts_Object = MibTableColumn
adGenVdsl2Vtuc1DayIntervalSraUpshifts = _AdGenVdsl2Vtuc1DayIntervalSraUpshifts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9, 1, 15),
    _AdGenVdsl2Vtuc1DayIntervalSraUpshifts_Type()
)
adGenVdsl2Vtuc1DayIntervalSraUpshifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalSraUpshifts.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalSraUpshifts.setUnits("upshifts")
_AdGenVdsl2Vtuc1DayIntervalSraRateMax_Type = Gauge32
_AdGenVdsl2Vtuc1DayIntervalSraRateMax_Object = MibTableColumn
adGenVdsl2Vtuc1DayIntervalSraRateMax = _AdGenVdsl2Vtuc1DayIntervalSraRateMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9, 1, 16),
    _AdGenVdsl2Vtuc1DayIntervalSraRateMax_Type()
)
adGenVdsl2Vtuc1DayIntervalSraRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalSraRateMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalSraRateMax.setUnits("bps")
_AdGenVdsl2Vtuc1DayIntervalSraRateMin_Type = Gauge32
_AdGenVdsl2Vtuc1DayIntervalSraRateMin_Object = MibTableColumn
adGenVdsl2Vtuc1DayIntervalSraRateMin = _AdGenVdsl2Vtuc1DayIntervalSraRateMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9, 1, 17),
    _AdGenVdsl2Vtuc1DayIntervalSraRateMin_Type()
)
adGenVdsl2Vtuc1DayIntervalSraRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalSraRateMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalSraRateMin.setUnits("bps")
_AdGenVdsl2Vtuc1DayIntervalRtxMinEftr_Type = Gauge32
_AdGenVdsl2Vtuc1DayIntervalRtxMinEftr_Object = MibTableColumn
adGenVdsl2Vtuc1DayIntervalRtxMinEftr = _AdGenVdsl2Vtuc1DayIntervalRtxMinEftr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9, 1, 18),
    _AdGenVdsl2Vtuc1DayIntervalRtxMinEftr_Type()
)
adGenVdsl2Vtuc1DayIntervalRtxMinEftr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalRtxMinEftr.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalRtxMinEftr.setUnits("bps")
_AdGenVdsl2Vtuc1DayIntervalRtxLeftrs_Type = Counter32
_AdGenVdsl2Vtuc1DayIntervalRtxLeftrs_Object = MibTableColumn
adGenVdsl2Vtuc1DayIntervalRtxLeftrs = _AdGenVdsl2Vtuc1DayIntervalRtxLeftrs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 9, 1, 19),
    _AdGenVdsl2Vtuc1DayIntervalRtxLeftrs_Type()
)
adGenVdsl2Vtuc1DayIntervalRtxLeftrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalRtxLeftrs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayIntervalRtxLeftrs.setUnits("seconds")
_AdGenVdsl2Vtur1DayIntervalTable_Object = MibTable
adGenVdsl2Vtur1DayIntervalTable = _AdGenVdsl2Vtur1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 10)
)
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalTable.setStatus("current")
_AdGenVdsl2Vtur1DayIntervalEntry_Object = MibTableRow
adGenVdsl2Vtur1DayIntervalEntry = _AdGenVdsl2Vtur1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 10, 1)
)
adGenVdsl2Vtur1DayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtur1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalEntry.setStatus("current")


class _AdGenVdsl2Vtur1DayIntervalNumber_Type(Integer32):
    """Custom type adGenVdsl2Vtur1DayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AdGenVdsl2Vtur1DayIntervalNumber_Type.__name__ = "Integer32"
_AdGenVdsl2Vtur1DayIntervalNumber_Object = MibTableColumn
adGenVdsl2Vtur1DayIntervalNumber = _AdGenVdsl2Vtur1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 10, 1, 1),
    _AdGenVdsl2Vtur1DayIntervalNumber_Type()
)
adGenVdsl2Vtur1DayIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalNumber.setStatus("current")
_AdGenVdsl2Vtur1DayIntervalLofs_Type = Counter32
_AdGenVdsl2Vtur1DayIntervalLofs_Object = MibTableColumn
adGenVdsl2Vtur1DayIntervalLofs = _AdGenVdsl2Vtur1DayIntervalLofs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 10, 1, 2),
    _AdGenVdsl2Vtur1DayIntervalLofs_Type()
)
adGenVdsl2Vtur1DayIntervalLofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalLofs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalLofs.setUnits("seconds")
_AdGenVdsl2Vtur1DayIntervalLoss_Type = Counter32
_AdGenVdsl2Vtur1DayIntervalLoss_Object = MibTableColumn
adGenVdsl2Vtur1DayIntervalLoss = _AdGenVdsl2Vtur1DayIntervalLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 10, 1, 3),
    _AdGenVdsl2Vtur1DayIntervalLoss_Type()
)
adGenVdsl2Vtur1DayIntervalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalLoss.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalLoss.setUnits("seconds")
_AdGenVdsl2Vtur1DayIntervalLprs_Type = Counter32
_AdGenVdsl2Vtur1DayIntervalLprs_Object = MibTableColumn
adGenVdsl2Vtur1DayIntervalLprs = _AdGenVdsl2Vtur1DayIntervalLprs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 10, 1, 4),
    _AdGenVdsl2Vtur1DayIntervalLprs_Type()
)
adGenVdsl2Vtur1DayIntervalLprs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalLprs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalLprs.setUnits("seconds")
_AdGenVdsl2Vtur1DayIntervalES_Type = Counter32
_AdGenVdsl2Vtur1DayIntervalES_Object = MibTableColumn
adGenVdsl2Vtur1DayIntervalES = _AdGenVdsl2Vtur1DayIntervalES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 10, 1, 5),
    _AdGenVdsl2Vtur1DayIntervalES_Type()
)
adGenVdsl2Vtur1DayIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalES.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalES.setUnits("seconds")


class _AdGenVdsl2Vtur1DayIntervalValidData_Type(Integer32):
    """Custom type adGenVdsl2Vtur1DayIntervalValidData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("notValid", 2))
    )


_AdGenVdsl2Vtur1DayIntervalValidData_Type.__name__ = "Integer32"
_AdGenVdsl2Vtur1DayIntervalValidData_Object = MibTableColumn
adGenVdsl2Vtur1DayIntervalValidData = _AdGenVdsl2Vtur1DayIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 10, 1, 6),
    _AdGenVdsl2Vtur1DayIntervalValidData_Type()
)
adGenVdsl2Vtur1DayIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalValidData.setStatus("current")
_AdGenVdsl2Vtur1DayIntervalSES_Type = Counter32
_AdGenVdsl2Vtur1DayIntervalSES_Object = MibTableColumn
adGenVdsl2Vtur1DayIntervalSES = _AdGenVdsl2Vtur1DayIntervalSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 10, 1, 7),
    _AdGenVdsl2Vtur1DayIntervalSES_Type()
)
adGenVdsl2Vtur1DayIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalSES.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalSES.setUnits("seconds")
_AdGenVdsl2Vtur1DayIntervalUAS_Type = Counter32
_AdGenVdsl2Vtur1DayIntervalUAS_Object = MibTableColumn
adGenVdsl2Vtur1DayIntervalUAS = _AdGenVdsl2Vtur1DayIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 10, 1, 8),
    _AdGenVdsl2Vtur1DayIntervalUAS_Type()
)
adGenVdsl2Vtur1DayIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalUAS.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalUAS.setUnits("seconds")
_AdGenVdsl2Vtur1DayIntervalFECs_Type = Counter32
_AdGenVdsl2Vtur1DayIntervalFECs_Object = MibTableColumn
adGenVdsl2Vtur1DayIntervalFECs = _AdGenVdsl2Vtur1DayIntervalFECs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 10, 1, 9),
    _AdGenVdsl2Vtur1DayIntervalFECs_Type()
)
adGenVdsl2Vtur1DayIntervalFECs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalFECs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalFECs.setUnits("seconds")
_AdGenVdsl2Vtur1DayIntervalFEC_Type = Counter32
_AdGenVdsl2Vtur1DayIntervalFEC_Object = MibTableColumn
adGenVdsl2Vtur1DayIntervalFEC = _AdGenVdsl2Vtur1DayIntervalFEC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 10, 1, 10),
    _AdGenVdsl2Vtur1DayIntervalFEC_Type()
)
adGenVdsl2Vtur1DayIntervalFEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalFEC.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalFEC.setUnits("seconds")
_AdGenVdsl2Vtur1DayIntervalCRC_Type = Counter32
_AdGenVdsl2Vtur1DayIntervalCRC_Object = MibTableColumn
adGenVdsl2Vtur1DayIntervalCRC = _AdGenVdsl2Vtur1DayIntervalCRC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 10, 1, 11),
    _AdGenVdsl2Vtur1DayIntervalCRC_Type()
)
adGenVdsl2Vtur1DayIntervalCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalCRC.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalCRC.setUnits("seconds")
_AdGenVdsl2Vtur1DayIntervalSraDownshifts_Type = Counter32
_AdGenVdsl2Vtur1DayIntervalSraDownshifts_Object = MibTableColumn
adGenVdsl2Vtur1DayIntervalSraDownshifts = _AdGenVdsl2Vtur1DayIntervalSraDownshifts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 10, 1, 12),
    _AdGenVdsl2Vtur1DayIntervalSraDownshifts_Type()
)
adGenVdsl2Vtur1DayIntervalSraDownshifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalSraDownshifts.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalSraDownshifts.setUnits("downshifts")
_AdGenVdsl2Vtur1DayIntervalSraUpshifts_Type = Counter32
_AdGenVdsl2Vtur1DayIntervalSraUpshifts_Object = MibTableColumn
adGenVdsl2Vtur1DayIntervalSraUpshifts = _AdGenVdsl2Vtur1DayIntervalSraUpshifts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 10, 1, 13),
    _AdGenVdsl2Vtur1DayIntervalSraUpshifts_Type()
)
adGenVdsl2Vtur1DayIntervalSraUpshifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalSraUpshifts.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalSraUpshifts.setUnits("upshifts")
_AdGenVdsl2Vtur1DayIntervalSraRateMax_Type = Gauge32
_AdGenVdsl2Vtur1DayIntervalSraRateMax_Object = MibTableColumn
adGenVdsl2Vtur1DayIntervalSraRateMax = _AdGenVdsl2Vtur1DayIntervalSraRateMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 10, 1, 14),
    _AdGenVdsl2Vtur1DayIntervalSraRateMax_Type()
)
adGenVdsl2Vtur1DayIntervalSraRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalSraRateMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalSraRateMax.setUnits("bps")
_AdGenVdsl2Vtur1DayIntervalSraRateMin_Type = Gauge32
_AdGenVdsl2Vtur1DayIntervalSraRateMin_Object = MibTableColumn
adGenVdsl2Vtur1DayIntervalSraRateMin = _AdGenVdsl2Vtur1DayIntervalSraRateMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 10, 1, 15),
    _AdGenVdsl2Vtur1DayIntervalSraRateMin_Type()
)
adGenVdsl2Vtur1DayIntervalSraRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalSraRateMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalSraRateMin.setUnits("bps")
_AdGenVdsl2Vtur1DayIntervalRtxMinEftr_Type = Gauge32
_AdGenVdsl2Vtur1DayIntervalRtxMinEftr_Object = MibTableColumn
adGenVdsl2Vtur1DayIntervalRtxMinEftr = _AdGenVdsl2Vtur1DayIntervalRtxMinEftr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 10, 1, 16),
    _AdGenVdsl2Vtur1DayIntervalRtxMinEftr_Type()
)
adGenVdsl2Vtur1DayIntervalRtxMinEftr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalRtxMinEftr.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalRtxMinEftr.setUnits("bps")
_AdGenVdsl2Vtur1DayIntervalRtxLeftrs_Type = Counter32
_AdGenVdsl2Vtur1DayIntervalRtxLeftrs_Object = MibTableColumn
adGenVdsl2Vtur1DayIntervalRtxLeftrs = _AdGenVdsl2Vtur1DayIntervalRtxLeftrs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 10, 1, 17),
    _AdGenVdsl2Vtur1DayIntervalRtxLeftrs_Type()
)
adGenVdsl2Vtur1DayIntervalRtxLeftrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalRtxLeftrs.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayIntervalRtxLeftrs.setUnits("seconds")
_AdGenVdsl2VtucChan1DayIntervalTable_Object = MibTable
adGenVdsl2VtucChan1DayIntervalTable = _AdGenVdsl2VtucChan1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 11)
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucChan1DayIntervalTable.setStatus("current")
_AdGenVdsl2VtucChan1DayIntervalEntry_Object = MibTableRow
adGenVdsl2VtucChan1DayIntervalEntry = _AdGenVdsl2VtucChan1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 11, 1)
)
adGenVdsl2VtucChan1DayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtuc1DayChanNum"),
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChan1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucChan1DayIntervalEntry.setStatus("current")


class _AdGenVdsl2Vtuc1DayChanNum_Type(Integer32):
    """Custom type adGenVdsl2Vtuc1DayChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AdGenVdsl2Vtuc1DayChanNum_Type.__name__ = "Integer32"
_AdGenVdsl2Vtuc1DayChanNum_Object = MibTableColumn
adGenVdsl2Vtuc1DayChanNum = _AdGenVdsl2Vtuc1DayChanNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 11, 1, 1),
    _AdGenVdsl2Vtuc1DayChanNum_Type()
)
adGenVdsl2Vtuc1DayChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtuc1DayChanNum.setStatus("current")


class _AdGenVdsl2VtucChan1DayIntervalNumber_Type(Integer32):
    """Custom type adGenVdsl2VtucChan1DayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AdGenVdsl2VtucChan1DayIntervalNumber_Type.__name__ = "Integer32"
_AdGenVdsl2VtucChan1DayIntervalNumber_Object = MibTableColumn
adGenVdsl2VtucChan1DayIntervalNumber = _AdGenVdsl2VtucChan1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 11, 1, 2),
    _AdGenVdsl2VtucChan1DayIntervalNumber_Type()
)
adGenVdsl2VtucChan1DayIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChan1DayIntervalNumber.setStatus("current")
_AdGenVdsl2VtucChan1DayIntervalReceivedBlks_Type = Counter32
_AdGenVdsl2VtucChan1DayIntervalReceivedBlks_Object = MibTableColumn
adGenVdsl2VtucChan1DayIntervalReceivedBlks = _AdGenVdsl2VtucChan1DayIntervalReceivedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 11, 1, 3),
    _AdGenVdsl2VtucChan1DayIntervalReceivedBlks_Type()
)
adGenVdsl2VtucChan1DayIntervalReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChan1DayIntervalReceivedBlks.setStatus("current")
_AdGenVdsl2VtucChan1DayIntervalTransmittedBlks_Type = Counter32
_AdGenVdsl2VtucChan1DayIntervalTransmittedBlks_Object = MibTableColumn
adGenVdsl2VtucChan1DayIntervalTransmittedBlks = _AdGenVdsl2VtucChan1DayIntervalTransmittedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 11, 1, 4),
    _AdGenVdsl2VtucChan1DayIntervalTransmittedBlks_Type()
)
adGenVdsl2VtucChan1DayIntervalTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChan1DayIntervalTransmittedBlks.setStatus("current")
_AdGenVdsl2VtucChan1DayIntervalCorrectedBlks_Type = Counter32
_AdGenVdsl2VtucChan1DayIntervalCorrectedBlks_Object = MibTableColumn
adGenVdsl2VtucChan1DayIntervalCorrectedBlks = _AdGenVdsl2VtucChan1DayIntervalCorrectedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 11, 1, 5),
    _AdGenVdsl2VtucChan1DayIntervalCorrectedBlks_Type()
)
adGenVdsl2VtucChan1DayIntervalCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChan1DayIntervalCorrectedBlks.setStatus("current")
_AdGenVdsl2VtucChan1DayIntervalUncorrectBlks_Type = Counter32
_AdGenVdsl2VtucChan1DayIntervalUncorrectBlks_Object = MibTableColumn
adGenVdsl2VtucChan1DayIntervalUncorrectBlks = _AdGenVdsl2VtucChan1DayIntervalUncorrectBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 11, 1, 6),
    _AdGenVdsl2VtucChan1DayIntervalUncorrectBlks_Type()
)
adGenVdsl2VtucChan1DayIntervalUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChan1DayIntervalUncorrectBlks.setStatus("current")


class _AdGenVdsl2VtucChan1DayIntervalValidData_Type(Integer32):
    """Custom type adGenVdsl2VtucChan1DayIntervalValidData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("notValid", 2))
    )


_AdGenVdsl2VtucChan1DayIntervalValidData_Type.__name__ = "Integer32"
_AdGenVdsl2VtucChan1DayIntervalValidData_Object = MibTableColumn
adGenVdsl2VtucChan1DayIntervalValidData = _AdGenVdsl2VtucChan1DayIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 11, 1, 7),
    _AdGenVdsl2VtucChan1DayIntervalValidData_Type()
)
adGenVdsl2VtucChan1DayIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChan1DayIntervalValidData.setStatus("current")
_AdGenVdsl2VtucChan1DayIntervalRtxUncorrectedDtu_Type = Counter32
_AdGenVdsl2VtucChan1DayIntervalRtxUncorrectedDtu_Object = MibTableColumn
adGenVdsl2VtucChan1DayIntervalRtxUncorrectedDtu = _AdGenVdsl2VtucChan1DayIntervalRtxUncorrectedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 11, 1, 8),
    _AdGenVdsl2VtucChan1DayIntervalRtxUncorrectedDtu_Type()
)
adGenVdsl2VtucChan1DayIntervalRtxUncorrectedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChan1DayIntervalRtxUncorrectedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChan1DayIntervalRtxUncorrectedDtu.setUnits("dtus")
_AdGenVdsl2VtucChan1DayIntervalRtxCorrectedDtu_Type = Counter32
_AdGenVdsl2VtucChan1DayIntervalRtxCorrectedDtu_Object = MibTableColumn
adGenVdsl2VtucChan1DayIntervalRtxCorrectedDtu = _AdGenVdsl2VtucChan1DayIntervalRtxCorrectedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 11, 1, 9),
    _AdGenVdsl2VtucChan1DayIntervalRtxCorrectedDtu_Type()
)
adGenVdsl2VtucChan1DayIntervalRtxCorrectedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChan1DayIntervalRtxCorrectedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChan1DayIntervalRtxCorrectedDtu.setUnits("dtus")
_AdGenVdsl2VtucChan1DayIntervalRtxRetransmittedDtu_Type = Counter32
_AdGenVdsl2VtucChan1DayIntervalRtxRetransmittedDtu_Object = MibTableColumn
adGenVdsl2VtucChan1DayIntervalRtxRetransmittedDtu = _AdGenVdsl2VtucChan1DayIntervalRtxRetransmittedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 11, 1, 10),
    _AdGenVdsl2VtucChan1DayIntervalRtxRetransmittedDtu_Type()
)
adGenVdsl2VtucChan1DayIntervalRtxRetransmittedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChan1DayIntervalRtxRetransmittedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VtucChan1DayIntervalRtxRetransmittedDtu.setUnits("dtus")
_AdGenVdsl2VturChan1DayIntervalTable_Object = MibTable
adGenVdsl2VturChan1DayIntervalTable = _AdGenVdsl2VturChan1DayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 12)
)
if mibBuilder.loadTexts:
    adGenVdsl2VturChan1DayIntervalTable.setStatus("current")
_AdGenVdsl2VturChan1DayIntervalEntry_Object = MibTableRow
adGenVdsl2VturChan1DayIntervalEntry = _AdGenVdsl2VturChan1DayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 12, 1)
)
adGenVdsl2VturChan1DayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtur1DayChanNum"),
    (0, "ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChan1DayIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenVdsl2VturChan1DayIntervalEntry.setStatus("current")


class _AdGenVdsl2Vtur1DayChanNum_Type(Integer32):
    """Custom type adGenVdsl2Vtur1DayChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AdGenVdsl2Vtur1DayChanNum_Type.__name__ = "Integer32"
_AdGenVdsl2Vtur1DayChanNum_Object = MibTableColumn
adGenVdsl2Vtur1DayChanNum = _AdGenVdsl2Vtur1DayChanNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 12, 1, 1),
    _AdGenVdsl2Vtur1DayChanNum_Type()
)
adGenVdsl2Vtur1DayChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2Vtur1DayChanNum.setStatus("current")


class _AdGenVdsl2VturChan1DayIntervalNumber_Type(Integer32):
    """Custom type adGenVdsl2VturChan1DayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AdGenVdsl2VturChan1DayIntervalNumber_Type.__name__ = "Integer32"
_AdGenVdsl2VturChan1DayIntervalNumber_Object = MibTableColumn
adGenVdsl2VturChan1DayIntervalNumber = _AdGenVdsl2VturChan1DayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 12, 1, 2),
    _AdGenVdsl2VturChan1DayIntervalNumber_Type()
)
adGenVdsl2VturChan1DayIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChan1DayIntervalNumber.setStatus("current")
_AdGenVdsl2VturChan1DayIntervalReceivedBlks_Type = Counter32
_AdGenVdsl2VturChan1DayIntervalReceivedBlks_Object = MibTableColumn
adGenVdsl2VturChan1DayIntervalReceivedBlks = _AdGenVdsl2VturChan1DayIntervalReceivedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 12, 1, 3),
    _AdGenVdsl2VturChan1DayIntervalReceivedBlks_Type()
)
adGenVdsl2VturChan1DayIntervalReceivedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChan1DayIntervalReceivedBlks.setStatus("current")
_AdGenVdsl2VturChan1DayIntervalTransmittedBlks_Type = Counter32
_AdGenVdsl2VturChan1DayIntervalTransmittedBlks_Object = MibTableColumn
adGenVdsl2VturChan1DayIntervalTransmittedBlks = _AdGenVdsl2VturChan1DayIntervalTransmittedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 12, 1, 4),
    _AdGenVdsl2VturChan1DayIntervalTransmittedBlks_Type()
)
adGenVdsl2VturChan1DayIntervalTransmittedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChan1DayIntervalTransmittedBlks.setStatus("current")
_AdGenVdsl2VturChan1DayIntervalCorrectedBlks_Type = Counter32
_AdGenVdsl2VturChan1DayIntervalCorrectedBlks_Object = MibTableColumn
adGenVdsl2VturChan1DayIntervalCorrectedBlks = _AdGenVdsl2VturChan1DayIntervalCorrectedBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 12, 1, 5),
    _AdGenVdsl2VturChan1DayIntervalCorrectedBlks_Type()
)
adGenVdsl2VturChan1DayIntervalCorrectedBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChan1DayIntervalCorrectedBlks.setStatus("current")
_AdGenVdsl2VturChan1DayIntervalUncorrectBlks_Type = Counter32
_AdGenVdsl2VturChan1DayIntervalUncorrectBlks_Object = MibTableColumn
adGenVdsl2VturChan1DayIntervalUncorrectBlks = _AdGenVdsl2VturChan1DayIntervalUncorrectBlks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 12, 1, 6),
    _AdGenVdsl2VturChan1DayIntervalUncorrectBlks_Type()
)
adGenVdsl2VturChan1DayIntervalUncorrectBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChan1DayIntervalUncorrectBlks.setStatus("current")


class _AdGenVdsl2VturChan1DayIntervalValidData_Type(Integer32):
    """Custom type adGenVdsl2VturChan1DayIntervalValidData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("notValid", 2))
    )


_AdGenVdsl2VturChan1DayIntervalValidData_Type.__name__ = "Integer32"
_AdGenVdsl2VturChan1DayIntervalValidData_Object = MibTableColumn
adGenVdsl2VturChan1DayIntervalValidData = _AdGenVdsl2VturChan1DayIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 12, 1, 7),
    _AdGenVdsl2VturChan1DayIntervalValidData_Type()
)
adGenVdsl2VturChan1DayIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChan1DayIntervalValidData.setStatus("current")
_AdGenVdsl2VturChan1DayIntervalRtxUncorrectedDtu_Type = Counter32
_AdGenVdsl2VturChan1DayIntervalRtxUncorrectedDtu_Object = MibTableColumn
adGenVdsl2VturChan1DayIntervalRtxUncorrectedDtu = _AdGenVdsl2VturChan1DayIntervalRtxUncorrectedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 12, 1, 8),
    _AdGenVdsl2VturChan1DayIntervalRtxUncorrectedDtu_Type()
)
adGenVdsl2VturChan1DayIntervalRtxUncorrectedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChan1DayIntervalRtxUncorrectedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChan1DayIntervalRtxUncorrectedDtu.setUnits("dtus")
_AdGenVdsl2VturChan1DayIntervalRtxCorrectedDtu_Type = Counter32
_AdGenVdsl2VturChan1DayIntervalRtxCorrectedDtu_Object = MibTableColumn
adGenVdsl2VturChan1DayIntervalRtxCorrectedDtu = _AdGenVdsl2VturChan1DayIntervalRtxCorrectedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 12, 1, 9),
    _AdGenVdsl2VturChan1DayIntervalRtxCorrectedDtu_Type()
)
adGenVdsl2VturChan1DayIntervalRtxCorrectedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChan1DayIntervalRtxCorrectedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChan1DayIntervalRtxCorrectedDtu.setUnits("dtus")
_AdGenVdsl2VturChan1DayIntervalRtxRetransmittedDtu_Type = Counter32
_AdGenVdsl2VturChan1DayIntervalRtxRetransmittedDtu_Object = MibTableColumn
adGenVdsl2VturChan1DayIntervalRtxRetransmittedDtu = _AdGenVdsl2VturChan1DayIntervalRtxRetransmittedDtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 3, 12, 1, 10),
    _AdGenVdsl2VturChan1DayIntervalRtxRetransmittedDtu_Type()
)
adGenVdsl2VturChan1DayIntervalRtxRetransmittedDtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVdsl2VturChan1DayIntervalRtxRetransmittedDtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenVdsl2VturChan1DayIntervalRtxRetransmittedDtu.setUnits("dtus")
_AdGenVdsl2Traps_ObjectIdentity = ObjectIdentity
adGenVdsl2Traps = _AdGenVdsl2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4)
)
_AdGenVdsl2VtucTrapPrefix_ObjectIdentity = ObjectIdentity
adGenVdsl2VtucTrapPrefix = _AdGenVdsl2VtucTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 1)
)
_AdGenVdsl2VtucTraps_ObjectIdentity = ObjectIdentity
adGenVdsl2VtucTraps = _AdGenVdsl2VtucTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 1, 0)
)
_AdGenVdsl2VturTrapPrefix_ObjectIdentity = ObjectIdentity
adGenVdsl2VturTrapPrefix = _AdGenVdsl2VturTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 2)
)
_AdGenVdsl2VturTraps_ObjectIdentity = ObjectIdentity
adGenVdsl2VturTraps = _AdGenVdsl2VturTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 2, 0)
)
_AdGenVdsl2VtucTrapPrefixRemote_ObjectIdentity = ObjectIdentity
adGenVdsl2VtucTrapPrefixRemote = _AdGenVdsl2VtucTrapPrefixRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 3)
)
_AdGenVdsl2VtucRemoteTraps_ObjectIdentity = ObjectIdentity
adGenVdsl2VtucRemoteTraps = _AdGenVdsl2VtucRemoteTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 3, 0)
)
_AdGenVdsl2VturTrapPrefixRemote_ObjectIdentity = ObjectIdentity
adGenVdsl2VturTrapPrefixRemote = _AdGenVdsl2VturTrapPrefixRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 4)
)
_AdGenVdsl2VturRemoteTraps_ObjectIdentity = ObjectIdentity
adGenVdsl2VturRemoteTraps = _AdGenVdsl2VturRemoteTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 4, 0)
)
_AdGenVdsl2ExtConfig_ObjectIdentity = ObjectIdentity
adGenVdsl2ExtConfig = _AdGenVdsl2ExtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 5)
)
_AdGenVdsl2ConfProfileExtTable_Object = MibTable
adGenVdsl2ConfProfileExtTable = _AdGenVdsl2ConfProfileExtTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 5, 1)
)
if mibBuilder.loadTexts:
    adGenVdsl2ConfProfileExtTable.setStatus("current")
_AdGenVdsl2ConfProfileExtEntry_Object = MibTableRow
adGenVdsl2ConfProfileExtEntry = _AdGenVdsl2ConfProfileExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 5, 1, 1)
)
adGenVdsl2ConfProfileExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenVdsl2ConfProfileExtEntry.setStatus("current")
_AdGenVdsl2LineManagementProfileNameApplied_Type = DisplayString
_AdGenVdsl2LineManagementProfileNameApplied_Object = MibTableColumn
adGenVdsl2LineManagementProfileNameApplied = _AdGenVdsl2LineManagementProfileNameApplied_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 5, 1, 1, 1),
    _AdGenVdsl2LineManagementProfileNameApplied_Type()
)
adGenVdsl2LineManagementProfileNameApplied.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVdsl2LineManagementProfileNameApplied.setStatus("current")
_AdGenVdsl2LineManagementProfileIndexApplied_Type = Unsigned32
_AdGenVdsl2LineManagementProfileIndexApplied_Object = MibTableColumn
adGenVdsl2LineManagementProfileIndexApplied = _AdGenVdsl2LineManagementProfileIndexApplied_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 5, 1, 1, 2),
    _AdGenVdsl2LineManagementProfileIndexApplied_Type()
)
adGenVdsl2LineManagementProfileIndexApplied.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVdsl2LineManagementProfileIndexApplied.setStatus("current")
_AdGenVdsl2LineCircuitID_Type = DisplayString
_AdGenVdsl2LineCircuitID_Object = MibTableColumn
adGenVdsl2LineCircuitID = _AdGenVdsl2LineCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 5, 1, 1, 3),
    _AdGenVdsl2LineCircuitID_Type()
)
adGenVdsl2LineCircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVdsl2LineCircuitID.setStatus("current")


class _AdGenVdsl2LineResetCounters_Type(Integer32):
    """Custom type adGenVdsl2LineResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("pmhistory", 2),
          ("current", 3),
          ("retrainne", 4),
          ("retrainfe", 5),
          ("rolling", 6))
    )


_AdGenVdsl2LineResetCounters_Type.__name__ = "Integer32"
_AdGenVdsl2LineResetCounters_Object = MibTableColumn
adGenVdsl2LineResetCounters = _AdGenVdsl2LineResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 5, 1, 1, 4),
    _AdGenVdsl2LineResetCounters_Type()
)
adGenVdsl2LineResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVdsl2LineResetCounters.setStatus("current")


class _AdGenVdsl2LineRetrainRequest_Type(Integer32):
    """Custom type adGenVdsl2LineRetrainRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("fast", 2))
    )


_AdGenVdsl2LineRetrainRequest_Type.__name__ = "Integer32"
_AdGenVdsl2LineRetrainRequest_Object = MibTableColumn
adGenVdsl2LineRetrainRequest = _AdGenVdsl2LineRetrainRequest_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 5, 1, 1, 5),
    _AdGenVdsl2LineRetrainRequest_Type()
)
adGenVdsl2LineRetrainRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVdsl2LineRetrainRequest.setStatus("current")
_AdGenVdsl2Test_ObjectIdentity = ObjectIdentity
adGenVdsl2Test = _AdGenVdsl2Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 6)
)
_AdGenVdsl2MibConformance_ObjectIdentity = ObjectIdentity
adGenVdsl2MibConformance = _AdGenVdsl2MibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 7)
)
_AdGenVdsl2MibGroups_ObjectIdentity = ObjectIdentity
adGenVdsl2MibGroups = _AdGenVdsl2MibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 7, 1)
)

# Managed Objects groups

adGenVdsl2ProvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 7, 1, 1)
)
adGenVdsl2ProvGroup.setObjects(
      *(("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsRateMode"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsTargetSnrMgn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsMaxSnrMgn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsMinSnrMgn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsTargetSnrMgn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsMaxSnrMgn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsMinSnrMgn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2LineConfProfileRowStatus"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfServiceMode"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfMultiModeDmtTse"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfBandProfiles"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfSpecificPsdSelect"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsPsdMaskU0Select"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsTrellis"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsTrellis"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsPboSetting"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsPboSetting"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsVnoiseSetting"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsVnoiseSetting"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsBitSwap"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsBitSwap"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfHamBandNotches"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsNomAggTxPwr"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsNomAggTxPwr"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsMaxNomTxPsd"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsMaxNomTxPsd"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsMaxAggRxPwr"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfFramingMode"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsLp0MaxPayloadRate"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsLp0MinPayloadRate"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsLp0MaxDelay"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsLp0MinProtection"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsLp0RaRatio"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsLp0InitPolicy"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsLp0MaxPayloadRate"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsLp0MinPayloadRate"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsLp0MaxDelay"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsLp0MinProtection"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsLp0RaRatio"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsLp0InitPolicy"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsLp1MaxPayloadRate"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsLp1MinPayloadRate"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsLp1MaxDelay"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsLp1MinProtection"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsLp1RaRatio"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfUsLp1InitPolicy"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsLp1MaxPayloadRate"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsLp1MinPayloadRate"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsLp1MaxDelay"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsLp1MinProtection"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsLp1RaRatio"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfDsLp1InitPolicy"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThreshSnrMgn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinLofs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinLoss"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinLols"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinLprs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinEs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinSes"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinUas"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThreshSnrMgn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinLofs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinLoss"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinLprs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinEs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinSes"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinUas"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2LineAlarmConfProfileRowStatus"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ThreshUsLp0RateUp"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ThreshUsLp0RateDown"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ThreshDsLp0RateUp"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ThreshDsLp0RateDown"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ThreshUsLp1RateUp"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ThreshUsLp1RateDown"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ThreshDsLp1RateUp"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ThreshDsLp1RateDown"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ConfRestoreDefaults"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2BandNumber"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2BandConfUsCustomPboCableA"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2BandConfUsCustomPboCableB"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2AlmSlotLinkdownSeverity"))
)
if mibBuilder.loadTexts:
    adGenVdsl2ProvGroup.setStatus("current")

adGenVdsl2StatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 7, 1, 2)
)
adGenVdsl2StatusGroup.setObjects(
      *(("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2LineCoding"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2LinePortServiceState"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2LineStatus"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2LineUpTime"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2LineCurrTransSysMode"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2LineCurrBandProfile"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2LineCurrEstimatedLength"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2LineCurrTpsTcFramingMode"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucInvSerialNumber"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucInvVendorID"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucInvVersionNumber"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2CurrUSSnrMgn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2CurrUSAtn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucCurrStatus"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucCurrOutputPwr"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucCurrAttainableRate"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucCurrTxRate"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPrevTxRate"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucActTxPsd"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucCurrTpsTcStatus"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturInvSerialNumber"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturInvVendorID"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturInvVersionNumber"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2CurrDSSnrMgn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2CurrDSAtn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturCurrStatus"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturCurrOutputPwr"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturCurrAttainableRate"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturCurrTxRate"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPrevTxRate"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturActTxPsd"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanInterleaveDelay"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanCurrTxRate"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPrevTxRate"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanCrcBlockLength"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanINP"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanInterleaveDelay"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanCurrTxRate"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPrevTxRate"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanCrcBlockLength"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanINP"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2BandStatusUsStartCarrier"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2BandStatusUsStopCarrier"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2BandStatusUsMargin"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2BandStatusUsLatn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2BandStatusUsSatn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2BandStatusDsStartCarrier"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2BandStatusDsStopCarrier"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2BandStatusDsMargin"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2BandStatusDsLatn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2BandStatusDsSatn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ScStatusUsBits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ScStatusUsGain"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ScStatusUsSnr"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ScStatusDsBits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ScStatusDsGain"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2ScStatusDsSnr"))
)
if mibBuilder.loadTexts:
    adGenVdsl2StatusGroup.setStatus("current")

adGenVdsl2PMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 7, 1, 3)
)
adGenVdsl2PMGroup.setObjects(
      *(("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfLofs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfLoss"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfLols"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfLprs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfEs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfInits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfSes"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfUas"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfFecs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCrc"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfFec"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfValidIntervals"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfInvalidIntervals"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinTimeElapsed"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinLofs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinLoss"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinLols"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinLprs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinEs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinInits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinSes"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinUas"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinFecs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinCrc"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinFec"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr1DayTimeElapsed"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr1DayLofs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr1DayLoss"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr1DayLols"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr1DayLprs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr1DayEs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr1DayInits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr1DaySes"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr1DayUas"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr1DayFecs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr1DayCrc"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr1DayFec"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfTcTxUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfTcTxDataUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfTcTxDataOctets"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfTcTxIdleUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfTcRxUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfTcRxDataUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfTcRxDataOctets"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfTcRxIdleUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfTcRxErroredUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfLofs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfLoss"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfLprs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfEs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfSes"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfUas"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfFecs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCrc"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfFec"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfValidIntervals"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfInvalidIntervals"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinTimeElapsed"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinLofs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinLoss"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinLprs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinEs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinSes"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinUas"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinFecs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinCrc"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinFec"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr1DayTimeElapsed"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr1DayLofs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr1DayLoss"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr1DayLprs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr1DayEs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr1DaySes"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr1DayUas"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr1DayFecs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr1DayCrc"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr1DayFec"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfTcTxUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfTcTxDataUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfTcTxDataOctets"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfTcTxIdleUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfTcRxUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfTcRxDataUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfTcRxDataOctets"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfTcRxIdleUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfTcRxErroredUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucIntervalNumber"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucIntervalLofs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucIntervalLoss"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucIntervalLols"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucIntervalLprs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucIntervalES"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucIntervalInits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucIntervalValidData"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucIntervalSES"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucIntervalUAS"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucIntervalFECs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucIntervalFEC"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucIntervalCRC"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturIntervalNumber"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturIntervalLofs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturIntervalLoss"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturIntervalLprs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturIntervalES"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturIntervalValidData"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturIntervalSES"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturIntervalUAS"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturIntervalFECs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturIntervalFEC"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturIntervalCRC"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanReceivedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanTransmittedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanCorrectedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanUncorrectBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfValidIntervals"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfInvalidIntervals"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfCurr15MinTimeElapsed"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfCurr15MinReceivedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfCurr15MinTransmittedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfCurr15MinCorrectedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfCurr15MinUncorrectBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfCurr1DayTimeElapsed"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfCurr1DayReceivedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfCurr1DayTransmittedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfCurr1DayCorrectedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfCurr1DayUncorrectBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfTcTxUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfTcTxDataUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfTcTxDataOctets"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfTcTxIdleUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfTcRxUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfTcRxDataUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfTcRxDataOctets"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfTcRxIdleUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanPerfTcRxErroredUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanReceivedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanTransmittedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanCorrectedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanUncorrectBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfValidIntervals"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfInvalidIntervals"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfCurr15MinTimeElapsed"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfCurr15MinReceivedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfCurr15MinTransmittedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfCurr15MinCorrectedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfCurr15MinUncorrectBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfCurr1DayTimeElapsed"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfCurr1DayReceivedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfCurr1DayTransmittedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfCurr1DayCorrectedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfCurr1DayUncorrectBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfTcTxUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfTcTxDataUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfTcTxDataOctets"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfTcTxIdleUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfTcRxUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfTcRxDataUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfTcRxDataOctets"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfTcRxIdleUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanPerfTcRxErroredUnits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanIntervalNumber"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanIntervalReceivedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanIntervalTransmittedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanIntervalCorrectedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanIntervalUncorrectBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucChanIntervalValidData"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanIntervalNumber"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanIntervalReceivedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanIntervalTransmittedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanIntervalCorrectedBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanIntervalUncorrectBlks"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturChanIntervalValidData"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtuc1DayIntervalNumber"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtuc1DayIntervalLofs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtuc1DayIntervalLoss"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtuc1DayIntervalLols"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtuc1DayIntervalLprs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtuc1DayIntervalES"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtuc1DayIntervalInits"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtuc1DayIntervalValidData"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtuc1DayIntervalSES"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtuc1DayIntervalUAS"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtuc1DayIntervalFECs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtuc1DayIntervalFEC"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtuc1DayIntervalCRC"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtur1DayIntervalNumber"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtur1DayIntervalLofs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtur1DayIntervalLoss"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtur1DayIntervalLprs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtur1DayIntervalES"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtur1DayIntervalValidData"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtur1DayIntervalSES"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtur1DayIntervalUAS"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtur1DayIntervalFECs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtur1DayIntervalFEC"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2Vtur1DayIntervalCRC"))
)
if mibBuilder.loadTexts:
    adGenVdsl2PMGroup.setStatus("current")

adGenVdsl2TrapsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 7, 1, 4)
)
adGenVdsl2TrapsGroup.setObjects(
      *(("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2CurrUSSnrMgn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThreshSnrMgn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinLofs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinLofs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinLoss"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinLoss"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinLols"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinLols"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinLprs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinLprs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinEs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinEs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinSes"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinSes"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinUas"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinUas"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2CurrDSSnrMgn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThreshSnrMgn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinLofs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinLofs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinLoss"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinLoss"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinLprs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinLprs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinEs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinEs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinSes"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinSes"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinUas"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinUas"))
)
if mibBuilder.loadTexts:
    adGenVdsl2TrapsGroup.setStatus("current")

adGenVdsl2ExtConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 7, 1, 5)
)
adGenVdsl2ExtConfigGroup.setObjects(
      *(("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2LineManagementProfileNameApplied"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2LineManagementProfileIndexApplied"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2LineCircuitID"))
)
if mibBuilder.loadTexts:
    adGenVdsl2ExtConfigGroup.setStatus("current")


# Notification objects

adGenVdsl2VtucSnrMgnThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 1, 0, 1)
)
adGenVdsl2VtucSnrMgnThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2CurrUSSnrMgn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThreshSnrMgn"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucSnrMgnThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VtucLofsThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 1, 0, 2)
)
adGenVdsl2VtucLofsThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinLofs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinLofs"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucLofsThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VtucLossThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 1, 0, 3)
)
adGenVdsl2VtucLossThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinLoss"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinLoss"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucLossThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VtucLolsThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 1, 0, 4)
)
adGenVdsl2VtucLolsThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinLols"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinLols"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucLolsThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VtucLprsThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 1, 0, 5)
)
adGenVdsl2VtucLprsThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinLprs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinLprs"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucLprsThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VtucESThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 1, 0, 6)
)
adGenVdsl2VtucESThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinEs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinEs"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucESThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VtucSESThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 1, 0, 7)
)
adGenVdsl2VtucSESThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinSes"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinSes"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucSESThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VtucUASThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 1, 0, 8)
)
adGenVdsl2VtucUASThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinUas"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinUas"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucUASThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VturSnrMgnThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 2, 0, 1)
)
adGenVdsl2VturSnrMgnThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2CurrDSSnrMgn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThreshSnrMgn"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VturSnrMgnThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VturLofsThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 2, 0, 2)
)
adGenVdsl2VturLofsThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinLofs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinLofs"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VturLofsThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VturLossThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 2, 0, 3)
)
adGenVdsl2VturLossThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinLoss"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinLoss"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VturLossThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VturLprsThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 2, 0, 4)
)
adGenVdsl2VturLprsThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinLprs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinLprs"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VturLprsThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VturESThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 2, 0, 5)
)
adGenVdsl2VturESThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinEs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinEs"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VturESThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VturSESThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 2, 0, 6)
)
adGenVdsl2VturSESThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinSes"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinSes"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VturSESThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VturUASThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 2, 0, 7)
)
adGenVdsl2VturUASThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinUas"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinUas"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VturUASThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VtucSnrMgnRemoteThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 3, 0, 1)
)
adGenVdsl2VtucSnrMgnRemoteThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2CurrUSSnrMgn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThreshSnrMgn"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucSnrMgnRemoteThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VtucLofsRemoteThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 3, 0, 2)
)
adGenVdsl2VtucLofsRemoteThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinLofs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinLofs"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucLofsRemoteThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VtucLossRemoteThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 3, 0, 3)
)
adGenVdsl2VtucLossRemoteThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinLoss"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinLoss"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucLossRemoteThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VtucLolsRemoteThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 3, 0, 4)
)
adGenVdsl2VtucLolsRemoteThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinLols"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinLols"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucLolsRemoteThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VtucLprsRemoteThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 3, 0, 5)
)
adGenVdsl2VtucLprsRemoteThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinLprs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinLprs"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucLprsRemoteThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VtucESRemoteThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 3, 0, 6)
)
adGenVdsl2VtucESRemoteThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinEs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinEs"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucESRemoteThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VtucSESRemoteThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 3, 0, 7)
)
adGenVdsl2VtucSESRemoteThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinSes"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinSes"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucSESRemoteThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VtucUASRemoteThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 3, 0, 8)
)
adGenVdsl2VtucUASRemoteThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucPerfCurr15MinUas"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VtucThresh15MinUas"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VtucUASRemoteThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VturSnrMgnRemoteThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 4, 0, 1)
)
adGenVdsl2VturSnrMgnRemoteThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2CurrDSSnrMgn"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThreshSnrMgn"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VturSnrMgnRemoteThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VturLofsRemoteThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 4, 0, 2)
)
adGenVdsl2VturLofsRemoteThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinLofs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinLofs"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VturLofsRemoteThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VturLossRemoteThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 4, 0, 3)
)
adGenVdsl2VturLossRemoteThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinLoss"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinLoss"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VturLossRemoteThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VturLprsRemoteThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 4, 0, 4)
)
adGenVdsl2VturLprsRemoteThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinLprs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinLprs"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VturLprsRemoteThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VturESRemoteThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 4, 0, 5)
)
adGenVdsl2VturESRemoteThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinEs"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinEs"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VturESRemoteThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VturSESRemoteThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 4, 0, 6)
)
adGenVdsl2VturSESRemoteThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinSes"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinSes"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VturSESRemoteThreshTrap.setStatus(
        "current"
    )

adGenVdsl2VturUASRemoteThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 65, 1, 4, 4, 0, 7)
)
adGenVdsl2VturUASRemoteThreshTrap.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturPerfCurr15MinUas"),
        ("ADTRAN-GENVDSL2-LINE-MIB", "adGenVdsl2VturThresh15MinUas"))
)
if mibBuilder.loadTexts:
    adGenVdsl2VturUASRemoteThreshTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENVDSL2-LINE-MIB",
    **{"adtran": adtran,
       "adProducts": adProducts,
       "adTA5k24pVDSL2Combo": adTA5k24pVDSL2Combo,
       "adTA5k32pVDSL2": adTA5k32pVDSL2,
       "adTA5k32pVDSL2Spltr": adTA5k32pVDSL2Spltr,
       "adGenVdsl2Prov": adGenVdsl2Prov,
       "adGenVdsl2LineConfProfileTable": adGenVdsl2LineConfProfileTable,
       "adGenVdsl2LineConfProfileEntry": adGenVdsl2LineConfProfileEntry,
       "adGenVdsl2LineConfProfileName": adGenVdsl2LineConfProfileName,
       "adGenVdsl2ConfDsRateMode": adGenVdsl2ConfDsRateMode,
       "adGenVdsl2ConfDsTargetSnrMgn": adGenVdsl2ConfDsTargetSnrMgn,
       "adGenVdsl2ConfDsMaxSnrMgn": adGenVdsl2ConfDsMaxSnrMgn,
       "adGenVdsl2ConfDsMinSnrMgn": adGenVdsl2ConfDsMinSnrMgn,
       "adGenVdsl2ConfUsTargetSnrMgn": adGenVdsl2ConfUsTargetSnrMgn,
       "adGenVdsl2ConfUsMaxSnrMgn": adGenVdsl2ConfUsMaxSnrMgn,
       "adGenVdsl2ConfUsMinSnrMgn": adGenVdsl2ConfUsMinSnrMgn,
       "adGenVdsl2LineConfProfileRowStatus": adGenVdsl2LineConfProfileRowStatus,
       "adGenVdsl2ConfServiceMode": adGenVdsl2ConfServiceMode,
       "adGenVdsl2ConfMultiModeDmtTse": adGenVdsl2ConfMultiModeDmtTse,
       "adGenVdsl2ConfBandProfiles": adGenVdsl2ConfBandProfiles,
       "adGenVdsl2ConfSpecificPsdSelect": adGenVdsl2ConfSpecificPsdSelect,
       "adGenVdsl2ConfUsPsdMaskU0Select": adGenVdsl2ConfUsPsdMaskU0Select,
       "adGenVdsl2ConfUsTrellis": adGenVdsl2ConfUsTrellis,
       "adGenVdsl2ConfDsTrellis": adGenVdsl2ConfDsTrellis,
       "adGenVdsl2ConfUsPboSetting": adGenVdsl2ConfUsPboSetting,
       "adGenVdsl2ConfDsPboSetting": adGenVdsl2ConfDsPboSetting,
       "adGenVdsl2ConfUsVnoiseSetting": adGenVdsl2ConfUsVnoiseSetting,
       "adGenVdsl2ConfDsVnoiseSetting": adGenVdsl2ConfDsVnoiseSetting,
       "adGenVdsl2ConfUsBitSwap": adGenVdsl2ConfUsBitSwap,
       "adGenVdsl2ConfDsBitSwap": adGenVdsl2ConfDsBitSwap,
       "adGenVdsl2ConfHamBandNotches": adGenVdsl2ConfHamBandNotches,
       "adGenVdsl2ConfUsNomAggTxPwr": adGenVdsl2ConfUsNomAggTxPwr,
       "adGenVdsl2ConfDsNomAggTxPwr": adGenVdsl2ConfDsNomAggTxPwr,
       "adGenVdsl2ConfUsMaxNomTxPsd": adGenVdsl2ConfUsMaxNomTxPsd,
       "adGenVdsl2ConfDsMaxNomTxPsd": adGenVdsl2ConfDsMaxNomTxPsd,
       "adGenVdsl2ConfUsMaxAggRxPwr": adGenVdsl2ConfUsMaxAggRxPwr,
       "adGenVdsl2ConfFramingMode": adGenVdsl2ConfFramingMode,
       "adGenVdsl2ConfUsLp0MaxPayloadRate": adGenVdsl2ConfUsLp0MaxPayloadRate,
       "adGenVdsl2ConfUsLp0MinPayloadRate": adGenVdsl2ConfUsLp0MinPayloadRate,
       "adGenVdsl2ConfUsLp0MaxDelay": adGenVdsl2ConfUsLp0MaxDelay,
       "adGenVdsl2ConfUsLp0MinProtection": adGenVdsl2ConfUsLp0MinProtection,
       "adGenVdsl2ConfUsLp0RaRatio": adGenVdsl2ConfUsLp0RaRatio,
       "adGenVdsl2ConfUsLp0InitPolicy": adGenVdsl2ConfUsLp0InitPolicy,
       "adGenVdsl2ConfDsLp0MaxPayloadRate": adGenVdsl2ConfDsLp0MaxPayloadRate,
       "adGenVdsl2ConfDsLp0MinPayloadRate": adGenVdsl2ConfDsLp0MinPayloadRate,
       "adGenVdsl2ConfDsLp0MaxDelay": adGenVdsl2ConfDsLp0MaxDelay,
       "adGenVdsl2ConfDsLp0MinProtection": adGenVdsl2ConfDsLp0MinProtection,
       "adGenVdsl2ConfDsLp0RaRatio": adGenVdsl2ConfDsLp0RaRatio,
       "adGenVdsl2ConfDsLp0InitPolicy": adGenVdsl2ConfDsLp0InitPolicy,
       "adGenVdsl2ConfUsLp1MaxPayloadRate": adGenVdsl2ConfUsLp1MaxPayloadRate,
       "adGenVdsl2ConfUsLp1MinPayloadRate": adGenVdsl2ConfUsLp1MinPayloadRate,
       "adGenVdsl2ConfUsLp1MaxDelay": adGenVdsl2ConfUsLp1MaxDelay,
       "adGenVdsl2ConfUsLp1MinProtection": adGenVdsl2ConfUsLp1MinProtection,
       "adGenVdsl2ConfUsLp1RaRatio": adGenVdsl2ConfUsLp1RaRatio,
       "adGenVdsl2ConfUsLp1InitPolicy": adGenVdsl2ConfUsLp1InitPolicy,
       "adGenVdsl2ConfDsLp1MaxPayloadRate": adGenVdsl2ConfDsLp1MaxPayloadRate,
       "adGenVdsl2ConfDsLp1MinPayloadRate": adGenVdsl2ConfDsLp1MinPayloadRate,
       "adGenVdsl2ConfDsLp1MaxDelay": adGenVdsl2ConfDsLp1MaxDelay,
       "adGenVdsl2ConfDsLp1MinProtection": adGenVdsl2ConfDsLp1MinProtection,
       "adGenVdsl2ConfDsLp1RaRatio": adGenVdsl2ConfDsLp1RaRatio,
       "adGenVdsl2ConfDsLp1InitPolicy": adGenVdsl2ConfDsLp1InitPolicy,
       "adGenVdsl2ConfUsLp0Type": adGenVdsl2ConfUsLp0Type,
       "adGenVdsl2ConfDsLp0Type": adGenVdsl2ConfDsLp0Type,
       "adGenVdsl2ConfUsLp1Type": adGenVdsl2ConfUsLp1Type,
       "adGenVdsl2ConfDsLp1Type": adGenVdsl2ConfDsLp1Type,
       "adGenVdsl2ConfUsRateMode": adGenVdsl2ConfUsRateMode,
       "adGenVdsl2ConfUsCustomPboElecLenKL": adGenVdsl2ConfUsCustomPboElecLenKL,
       "adGenVdsl2ConfUsCustomPboForceLen": adGenVdsl2ConfUsCustomPboForceLen,
       "adGenVdsl2ConfUsCustomPboBoostMode": adGenVdsl2ConfUsCustomPboBoostMode,
       "adGenVdsl2ConfDsCustomPboElecLen": adGenVdsl2ConfDsCustomPboElecLen,
       "adGenVdsl2ConfDsCustomPboCableA": adGenVdsl2ConfDsCustomPboCableA,
       "adGenVdsl2ConfDsCustomPboCableB": adGenVdsl2ConfDsCustomPboCableB,
       "adGenVdsl2ConfDsCustomPboCableC": adGenVdsl2ConfDsCustomPboCableC,
       "adGenVdsl2ConfDsCustomPboMinSignal": adGenVdsl2ConfDsCustomPboMinSignal,
       "adGenVdsl2ConfDsCustomPboMinFreq": adGenVdsl2ConfDsCustomPboMinFreq,
       "adGenVdsl2ConfDsCustomPboMaxFreq": adGenVdsl2ConfDsCustomPboMaxFreq,
       "adGenVdsl2ConfAnfpCalValue": adGenVdsl2ConfAnfpCalValue,
       "adGenVdsl2ConfDsDownshiftSnrMgn": adGenVdsl2ConfDsDownshiftSnrMgn,
       "adGenVdsl2ConfDsUpshiftSnrMgn": adGenVdsl2ConfDsUpshiftSnrMgn,
       "adGenVdsl2ConfDsMinUpshiftTime": adGenVdsl2ConfDsMinUpshiftTime,
       "adGenVdsl2ConfDsMinDownshiftTime": adGenVdsl2ConfDsMinDownshiftTime,
       "adGenVdsl2ConfUsDownshiftSnrMgn": adGenVdsl2ConfUsDownshiftSnrMgn,
       "adGenVdsl2ConfUsUpshiftSnrMgn": adGenVdsl2ConfUsUpshiftSnrMgn,
       "adGenVdsl2ConfUsMinUpshiftTime": adGenVdsl2ConfUsMinUpshiftTime,
       "adGenVdsl2ConfUsMinDownshiftTime": adGenVdsl2ConfUsMinDownshiftTime,
       "adGenVdsl2ConfUsLp0RtxSetting": adGenVdsl2ConfUsLp0RtxSetting,
       "adGenVdsl2ConfUsLp0CustomRtxMaxNdr": adGenVdsl2ConfUsLp0CustomRtxMaxNdr,
       "adGenVdsl2ConfUsLp0CustomRtxMinDelay": adGenVdsl2ConfUsLp0CustomRtxMinDelay,
       "adGenVdsl2ConfUsLp0CustomRtxMaxDelay": adGenVdsl2ConfUsLp0CustomRtxMaxDelay,
       "adGenVdsl2ConfUsLp0CustomRtxInpMinShine": adGenVdsl2ConfUsLp0CustomRtxInpMinShine,
       "adGenVdsl2ConfUsLp0CustomRtxInpMinRein": adGenVdsl2ConfUsLp0CustomRtxInpMinRein,
       "adGenVdsl2ConfUsLp0CustomRtxIatRein": adGenVdsl2ConfUsLp0CustomRtxIatRein,
       "adGenVdsl2ConfUsLp0CustomRtxLeftrThresh": adGenVdsl2ConfUsLp0CustomRtxLeftrThresh,
       "adGenVdsl2ConfDsLp0RtxSetting": adGenVdsl2ConfDsLp0RtxSetting,
       "adGenVdsl2ConfDsLp0CustomRtxMaxNdr": adGenVdsl2ConfDsLp0CustomRtxMaxNdr,
       "adGenVdsl2ConfDsLp0CustomRtxMinDelay": adGenVdsl2ConfDsLp0CustomRtxMinDelay,
       "adGenVdsl2ConfDsLp0CustomRtxMaxDelay": adGenVdsl2ConfDsLp0CustomRtxMaxDelay,
       "adGenVdsl2ConfDsLp0CustomRtxInpMinShine": adGenVdsl2ConfDsLp0CustomRtxInpMinShine,
       "adGenVdsl2ConfDsLp0CustomRtxInpMinRein": adGenVdsl2ConfDsLp0CustomRtxInpMinRein,
       "adGenVdsl2ConfDsLp0CustomRtxIatRein": adGenVdsl2ConfDsLp0CustomRtxIatRein,
       "adGenVdsl2ConfDsLp0CustomRtxLeftrThresh": adGenVdsl2ConfDsLp0CustomRtxLeftrThresh,
       "adGenVdsl2ConfUsLp1RtxSetting": adGenVdsl2ConfUsLp1RtxSetting,
       "adGenVdsl2ConfUsLp1CustomRtxMaxNdr": adGenVdsl2ConfUsLp1CustomRtxMaxNdr,
       "adGenVdsl2ConfUsLp1CustomRtxMinDelay": adGenVdsl2ConfUsLp1CustomRtxMinDelay,
       "adGenVdsl2ConfUsLp1CustomRtxMaxDelay": adGenVdsl2ConfUsLp1CustomRtxMaxDelay,
       "adGenVdsl2ConfUsLp1CustomRtxInpMinShine": adGenVdsl2ConfUsLp1CustomRtxInpMinShine,
       "adGenVdsl2ConfUsLp1CustomRtxInpMinRein": adGenVdsl2ConfUsLp1CustomRtxInpMinRein,
       "adGenVdsl2ConfUsLp1CustomRtxIatRein": adGenVdsl2ConfUsLp1CustomRtxIatRein,
       "adGenVdsl2ConfUsLp1CustomRtxLeftrThresh": adGenVdsl2ConfUsLp1CustomRtxLeftrThresh,
       "adGenVdsl2ConfDsLp1RtxSetting": adGenVdsl2ConfDsLp1RtxSetting,
       "adGenVdsl2ConfDsLp1CustomRtxMaxNdr": adGenVdsl2ConfDsLp1CustomRtxMaxNdr,
       "adGenVdsl2ConfDsLp1CustomRtxMinDelay": adGenVdsl2ConfDsLp1CustomRtxMinDelay,
       "adGenVdsl2ConfDsLp1CustomRtxMaxDelay": adGenVdsl2ConfDsLp1CustomRtxMaxDelay,
       "adGenVdsl2ConfDsLp1CustomRtxInpMinShine": adGenVdsl2ConfDsLp1CustomRtxInpMinShine,
       "adGenVdsl2ConfDsLp1CustomRtxInpMinRein": adGenVdsl2ConfDsLp1CustomRtxInpMinRein,
       "adGenVdsl2ConfDsLp1CustomRtxIatRein": adGenVdsl2ConfDsLp1CustomRtxIatRein,
       "adGenVdsl2ConfDsLp1CustomRtxLeftrThresh": adGenVdsl2ConfDsLp1CustomRtxLeftrThresh,
       "adGenVdsl2ConfAmRadioFreqMask1": adGenVdsl2ConfAmRadioFreqMask1,
       "adGenVdsl2ConfAmRadioFreqMask2": adGenVdsl2ConfAmRadioFreqMask2,
       "adGenVdsl2ConfAmRadioFreqMask3": adGenVdsl2ConfAmRadioFreqMask3,
       "adGenVdsl2ConfAmRadioFreqMask4": adGenVdsl2ConfAmRadioFreqMask4,
       "adGenVdsl2ConfAmRadioFreqMask5": adGenVdsl2ConfAmRadioFreqMask5,
       "adGenVdsl2ConfAmRadioFreqMask6": adGenVdsl2ConfAmRadioFreqMask6,
       "adGenVdsl2ConfMemorySplitRatio": adGenVdsl2ConfMemorySplitRatio,
       "adGenVdsl2ConfRateAdaptConfigMode": adGenVdsl2ConfRateAdaptConfigMode,
       "adGenVdsl2LineAlarmConfProfileTable": adGenVdsl2LineAlarmConfProfileTable,
       "adGenVdsl2LineAlarmConfProfileEntry": adGenVdsl2LineAlarmConfProfileEntry,
       "adGenVdsl2LineAlarmConfProfileName": adGenVdsl2LineAlarmConfProfileName,
       "adGenVdsl2VtucThreshSnrMgn": adGenVdsl2VtucThreshSnrMgn,
       "adGenVdsl2VtucThresh15MinLofs": adGenVdsl2VtucThresh15MinLofs,
       "adGenVdsl2VtucThresh15MinLoss": adGenVdsl2VtucThresh15MinLoss,
       "adGenVdsl2VtucThresh15MinLols": adGenVdsl2VtucThresh15MinLols,
       "adGenVdsl2VtucThresh15MinLprs": adGenVdsl2VtucThresh15MinLprs,
       "adGenVdsl2VtucThresh15MinEs": adGenVdsl2VtucThresh15MinEs,
       "adGenVdsl2VtucThresh15MinSes": adGenVdsl2VtucThresh15MinSes,
       "adGenVdsl2VtucThresh15MinUas": adGenVdsl2VtucThresh15MinUas,
       "adGenVdsl2VturThreshSnrMgn": adGenVdsl2VturThreshSnrMgn,
       "adGenVdsl2VturThresh15MinLofs": adGenVdsl2VturThresh15MinLofs,
       "adGenVdsl2VturThresh15MinLoss": adGenVdsl2VturThresh15MinLoss,
       "adGenVdsl2VturThresh15MinLprs": adGenVdsl2VturThresh15MinLprs,
       "adGenVdsl2VturThresh15MinEs": adGenVdsl2VturThresh15MinEs,
       "adGenVdsl2VturThresh15MinSes": adGenVdsl2VturThresh15MinSes,
       "adGenVdsl2VturThresh15MinUas": adGenVdsl2VturThresh15MinUas,
       "adGenVdsl2LineAlarmConfProfileRowStatus": adGenVdsl2LineAlarmConfProfileRowStatus,
       "adGenVdsl2ThreshUsLp0RateUp": adGenVdsl2ThreshUsLp0RateUp,
       "adGenVdsl2ThreshUsLp0RateDown": adGenVdsl2ThreshUsLp0RateDown,
       "adGenVdsl2ThreshDsLp0RateUp": adGenVdsl2ThreshDsLp0RateUp,
       "adGenVdsl2ThreshDsLp0RateDown": adGenVdsl2ThreshDsLp0RateDown,
       "adGenVdsl2ThreshUsLp1RateUp": adGenVdsl2ThreshUsLp1RateUp,
       "adGenVdsl2ThreshUsLp1RateDown": adGenVdsl2ThreshUsLp1RateDown,
       "adGenVdsl2ThreshDsLp1RateUp": adGenVdsl2ThreshDsLp1RateUp,
       "adGenVdsl2ThreshDsLp1RateDown": adGenVdsl2ThreshDsLp1RateDown,
       "adGenVdsl2RestoreDefaultTable": adGenVdsl2RestoreDefaultTable,
       "adGenVdsl2RestoreDefaultEntry": adGenVdsl2RestoreDefaultEntry,
       "adGenVdsl2ConfRestoreDefaults": adGenVdsl2ConfRestoreDefaults,
       "adGenVdsl2BandConfProfileTable": adGenVdsl2BandConfProfileTable,
       "adGenVdsl2BandConfProfileEntry": adGenVdsl2BandConfProfileEntry,
       "adGenVdsl2BandNumber": adGenVdsl2BandNumber,
       "adGenVdsl2BandConfUsCustomPboCableA": adGenVdsl2BandConfUsCustomPboCableA,
       "adGenVdsl2BandConfUsCustomPboCableB": adGenVdsl2BandConfUsCustomPboCableB,
       "adGenVdsl2AlarmSlotProvTable": adGenVdsl2AlarmSlotProvTable,
       "adGenVdsl2AlarmSlotProvEntry": adGenVdsl2AlarmSlotProvEntry,
       "adGenVdsl2AlmSlotLinkdownSeverity": adGenVdsl2AlmSlotLinkdownSeverity,
       "adGenVdsl2Status": adGenVdsl2Status,
       "adGenVdsl2LineTable": adGenVdsl2LineTable,
       "adGenVdsl2LineEntry": adGenVdsl2LineEntry,
       "adGenVdsl2LineCoding": adGenVdsl2LineCoding,
       "adGenVdsl2LinePortServiceState": adGenVdsl2LinePortServiceState,
       "adGenVdsl2LineStatus": adGenVdsl2LineStatus,
       "adGenVdsl2LineUpTime": adGenVdsl2LineUpTime,
       "adGenVdsl2LineCurrTransSysMode": adGenVdsl2LineCurrTransSysMode,
       "adGenVdsl2LineCurrBandProfile": adGenVdsl2LineCurrBandProfile,
       "adGenVdsl2LineCurrEstimatedLength": adGenVdsl2LineCurrEstimatedLength,
       "adGenVdsl2LineCurrTpsTcFramingMode": adGenVdsl2LineCurrTpsTcFramingMode,
       "adGenVdsl2VtucPhysTable": adGenVdsl2VtucPhysTable,
       "adGenVdsl2VtucPhysEntry": adGenVdsl2VtucPhysEntry,
       "adGenVdsl2VtucInvSerialNumber": adGenVdsl2VtucInvSerialNumber,
       "adGenVdsl2VtucInvVendorID": adGenVdsl2VtucInvVendorID,
       "adGenVdsl2VtucInvVersionNumber": adGenVdsl2VtucInvVersionNumber,
       "adGenVdsl2CurrUSSnrMgn": adGenVdsl2CurrUSSnrMgn,
       "adGenVdsl2CurrUSAtn": adGenVdsl2CurrUSAtn,
       "adGenVdsl2VtucCurrStatus": adGenVdsl2VtucCurrStatus,
       "adGenVdsl2VtucCurrOutputPwr": adGenVdsl2VtucCurrOutputPwr,
       "adGenVdsl2VtucCurrAttainableRate": adGenVdsl2VtucCurrAttainableRate,
       "adGenVdsl2VtucCurrTxRate": adGenVdsl2VtucCurrTxRate,
       "adGenVdsl2VtucPrevTxRate": adGenVdsl2VtucPrevTxRate,
       "adGenVdsl2VtucActTxPsd": adGenVdsl2VtucActTxPsd,
       "adGenVdsl2VtucCurrTpsTcStatus": adGenVdsl2VtucCurrTpsTcStatus,
       "adGenVdsl2VtucCurrTxLineRate": adGenVdsl2VtucCurrTxLineRate,
       "adGenVdsl2VtucPrevTxLineRate": adGenVdsl2VtucPrevTxLineRate,
       "adGenVdsl2VtucCircuitProviderCode": adGenVdsl2VtucCircuitProviderCode,
       "adGenVdsl2VtucCurrTxRateMax": adGenVdsl2VtucCurrTxRateMax,
       "adGenVdsl2VtucCurrTxRateMin": adGenVdsl2VtucCurrTxRateMin,
       "adGenVdsl2VtucLastSraDownshift": adGenVdsl2VtucLastSraDownshift,
       "adGenVdsl2VtucLastSraUpshift": adGenVdsl2VtucLastSraUpshift,
       "adGenVdsl2VtucRtxUsed": adGenVdsl2VtucRtxUsed,
       "adGenVdsl2VtucRtxEtr": adGenVdsl2VtucRtxEtr,
       "adGenVdsl2VturPhysTable": adGenVdsl2VturPhysTable,
       "adGenVdsl2VturPhysEntry": adGenVdsl2VturPhysEntry,
       "adGenVdsl2VturInvSerialNumber": adGenVdsl2VturInvSerialNumber,
       "adGenVdsl2VturInvVendorID": adGenVdsl2VturInvVendorID,
       "adGenVdsl2VturInvVersionNumber": adGenVdsl2VturInvVersionNumber,
       "adGenVdsl2CurrDSSnrMgn": adGenVdsl2CurrDSSnrMgn,
       "adGenVdsl2CurrDSAtn": adGenVdsl2CurrDSAtn,
       "adGenVdsl2VturCurrStatus": adGenVdsl2VturCurrStatus,
       "adGenVdsl2VturCurrOutputPwr": adGenVdsl2VturCurrOutputPwr,
       "adGenVdsl2VturCurrAttainableRate": adGenVdsl2VturCurrAttainableRate,
       "adGenVdsl2VturCurrTxRate": adGenVdsl2VturCurrTxRate,
       "adGenVdsl2VturPrevTxRate": adGenVdsl2VturPrevTxRate,
       "adGenVdsl2VturActTxPsd": adGenVdsl2VturActTxPsd,
       "adGenVdsl2VturCurrTxLineRate": adGenVdsl2VturCurrTxLineRate,
       "adGenVdsl2VturPrevTxLineRate": adGenVdsl2VturPrevTxLineRate,
       "adGenVdsl2VturCircuitProviderCode": adGenVdsl2VturCircuitProviderCode,
       "adGenVdsl2VturCircuitCapabilities": adGenVdsl2VturCircuitCapabilities,
       "adGenVdsl2VturCurrTxRateMax": adGenVdsl2VturCurrTxRateMax,
       "adGenVdsl2VturCurrTxRateMin": adGenVdsl2VturCurrTxRateMin,
       "adGenVdsl2VturLastSraDownshift": adGenVdsl2VturLastSraDownshift,
       "adGenVdsl2VturLastSraUpshift": adGenVdsl2VturLastSraUpshift,
       "adGenVdsl2VturRtxUsed": adGenVdsl2VturRtxUsed,
       "adGenVdsl2VturRtxEtr": adGenVdsl2VturRtxEtr,
       "adGenVdsl2VtucChanTable": adGenVdsl2VtucChanTable,
       "adGenVdsl2VtucChanEntry": adGenVdsl2VtucChanEntry,
       "adGenVdsl2VtucChannelNumber": adGenVdsl2VtucChannelNumber,
       "adGenVdsl2VtucChanInterleaveDelay": adGenVdsl2VtucChanInterleaveDelay,
       "adGenVdsl2VtucChanCurrTxRate": adGenVdsl2VtucChanCurrTxRate,
       "adGenVdsl2VtucChanPrevTxRate": adGenVdsl2VtucChanPrevTxRate,
       "adGenVdsl2VtucChanCrcBlockLength": adGenVdsl2VtucChanCrcBlockLength,
       "adGenVdsl2VtucChanINP": adGenVdsl2VtucChanINP,
       "adGenVdsl2VtucChanINPRein": adGenVdsl2VtucChanINPRein,
       "adGenVdsl2VturChanTable": adGenVdsl2VturChanTable,
       "adGenVdsl2VturChanEntry": adGenVdsl2VturChanEntry,
       "adGenVdsl2VturChannelNumber": adGenVdsl2VturChannelNumber,
       "adGenVdsl2VturChanInterleaveDelay": adGenVdsl2VturChanInterleaveDelay,
       "adGenVdsl2VturChanCurrTxRate": adGenVdsl2VturChanCurrTxRate,
       "adGenVdsl2VturChanPrevTxRate": adGenVdsl2VturChanPrevTxRate,
       "adGenVdsl2VturChanCrcBlockLength": adGenVdsl2VturChanCrcBlockLength,
       "adGenVdsl2VturChanINP": adGenVdsl2VturChanINP,
       "adGenVdsl2VturChanINPRein": adGenVdsl2VturChanINPRein,
       "adGenVdsl2BandStatusTable": adGenVdsl2BandStatusTable,
       "adGenVdsl2BandStatusEntry": adGenVdsl2BandStatusEntry,
       "adGenVdsl2BandStatusNumber": adGenVdsl2BandStatusNumber,
       "adGenVdsl2BandStatusUsStartCarrier": adGenVdsl2BandStatusUsStartCarrier,
       "adGenVdsl2BandStatusUsStopCarrier": adGenVdsl2BandStatusUsStopCarrier,
       "adGenVdsl2BandStatusUsMargin": adGenVdsl2BandStatusUsMargin,
       "adGenVdsl2BandStatusUsLatn": adGenVdsl2BandStatusUsLatn,
       "adGenVdsl2BandStatusUsSatn": adGenVdsl2BandStatusUsSatn,
       "adGenVdsl2BandStatusDsStartCarrier": adGenVdsl2BandStatusDsStartCarrier,
       "adGenVdsl2BandStatusDsStopCarrier": adGenVdsl2BandStatusDsStopCarrier,
       "adGenVdsl2BandStatusDsMargin": adGenVdsl2BandStatusDsMargin,
       "adGenVdsl2BandStatusDsLatn": adGenVdsl2BandStatusDsLatn,
       "adGenVdsl2BandStatusDsSatn": adGenVdsl2BandStatusDsSatn,
       "adGenVdsl2ScStatusTable": adGenVdsl2ScStatusTable,
       "adGenVdsl2ScStatusEntry": adGenVdsl2ScStatusEntry,
       "adGenVdsl2ScStatusNumber": adGenVdsl2ScStatusNumber,
       "adGenVdsl2ScStatusUsBits": adGenVdsl2ScStatusUsBits,
       "adGenVdsl2ScStatusUsGain": adGenVdsl2ScStatusUsGain,
       "adGenVdsl2ScStatusUsSnr": adGenVdsl2ScStatusUsSnr,
       "adGenVdsl2ScStatusDsBits": adGenVdsl2ScStatusDsBits,
       "adGenVdsl2ScStatusDsGain": adGenVdsl2ScStatusDsGain,
       "adGenVdsl2ScStatusDsSnr": adGenVdsl2ScStatusDsSnr,
       "adGenVdsl2ScStatusUsQln": adGenVdsl2ScStatusUsQln,
       "adGenVdsl2ScStatusDsQln": adGenVdsl2ScStatusDsQln,
       "adGenVdsl2ScStatusUsHlog": adGenVdsl2ScStatusUsHlog,
       "adGenVdsl2ScStatusDsHlog": adGenVdsl2ScStatusDsHlog,
       "adGenVdsl2ReserveInstanceBulkVDSLTlvTable": adGenVdsl2ReserveInstanceBulkVDSLTlvTable,
       "adGenVdsl2ReserveInstanceBulkVDSLTlvEntry": adGenVdsl2ReserveInstanceBulkVDSLTlvEntry,
       "adGenVdsl2ReserveInstanceBulkVDSLSlotInstance": adGenVdsl2ReserveInstanceBulkVDSLSlotInstance,
       "adGenVdsl2BulkVDSLTlvTable": adGenVdsl2BulkVDSLTlvTable,
       "adGenVdsl2BulkVDSLTlvEntry": adGenVdsl2BulkVDSLTlvEntry,
       "adGenVdsl2BulkVDSLTlvInstance": adGenVdsl2BulkVDSLTlvInstance,
       "adGenVdsl2BulkVDSLTlvType": adGenVdsl2BulkVDSLTlvType,
       "adGenVdsl2BulkVDSLTlvPort": adGenVdsl2BulkVDSLTlvPort,
       "adGenVdsl2BulkVDLSTlvCreate": adGenVdsl2BulkVDLSTlvCreate,
       "adGenVdsl2PM": adGenVdsl2PM,
       "adGenVdsl2VtucPerfDataTable": adGenVdsl2VtucPerfDataTable,
       "adGenVdsl2VtucPerfDataEntry": adGenVdsl2VtucPerfDataEntry,
       "adGenVdsl2VtucPerfLofs": adGenVdsl2VtucPerfLofs,
       "adGenVdsl2VtucPerfLoss": adGenVdsl2VtucPerfLoss,
       "adGenVdsl2VtucPerfLols": adGenVdsl2VtucPerfLols,
       "adGenVdsl2VtucPerfLprs": adGenVdsl2VtucPerfLprs,
       "adGenVdsl2VtucPerfEs": adGenVdsl2VtucPerfEs,
       "adGenVdsl2VtucPerfInits": adGenVdsl2VtucPerfInits,
       "adGenVdsl2VtucPerfSes": adGenVdsl2VtucPerfSes,
       "adGenVdsl2VtucPerfUas": adGenVdsl2VtucPerfUas,
       "adGenVdsl2VtucPerfFecs": adGenVdsl2VtucPerfFecs,
       "adGenVdsl2VtucPerfCrc": adGenVdsl2VtucPerfCrc,
       "adGenVdsl2VtucPerfFec": adGenVdsl2VtucPerfFec,
       "adGenVdsl2VtucPerfValidIntervals": adGenVdsl2VtucPerfValidIntervals,
       "adGenVdsl2VtucPerfInvalidIntervals": adGenVdsl2VtucPerfInvalidIntervals,
       "adGenVdsl2VtucPerfCurr15MinTimeElapsed": adGenVdsl2VtucPerfCurr15MinTimeElapsed,
       "adGenVdsl2VtucPerfCurr15MinLofs": adGenVdsl2VtucPerfCurr15MinLofs,
       "adGenVdsl2VtucPerfCurr15MinLoss": adGenVdsl2VtucPerfCurr15MinLoss,
       "adGenVdsl2VtucPerfCurr15MinLols": adGenVdsl2VtucPerfCurr15MinLols,
       "adGenVdsl2VtucPerfCurr15MinLprs": adGenVdsl2VtucPerfCurr15MinLprs,
       "adGenVdsl2VtucPerfCurr15MinEs": adGenVdsl2VtucPerfCurr15MinEs,
       "adGenVdsl2VtucPerfCurr15MinInits": adGenVdsl2VtucPerfCurr15MinInits,
       "adGenVdsl2VtucPerfCurr15MinSes": adGenVdsl2VtucPerfCurr15MinSes,
       "adGenVdsl2VtucPerfCurr15MinUas": adGenVdsl2VtucPerfCurr15MinUas,
       "adGenVdsl2VtucPerfCurr15MinFecs": adGenVdsl2VtucPerfCurr15MinFecs,
       "adGenVdsl2VtucPerfCurr15MinCrc": adGenVdsl2VtucPerfCurr15MinCrc,
       "adGenVdsl2VtucPerfCurr15MinFec": adGenVdsl2VtucPerfCurr15MinFec,
       "adGenVdsl2VtucPerfCurr1DayTimeElapsed": adGenVdsl2VtucPerfCurr1DayTimeElapsed,
       "adGenVdsl2VtucPerfCurr1DayLofs": adGenVdsl2VtucPerfCurr1DayLofs,
       "adGenVdsl2VtucPerfCurr1DayLoss": adGenVdsl2VtucPerfCurr1DayLoss,
       "adGenVdsl2VtucPerfCurr1DayLols": adGenVdsl2VtucPerfCurr1DayLols,
       "adGenVdsl2VtucPerfCurr1DayLprs": adGenVdsl2VtucPerfCurr1DayLprs,
       "adGenVdsl2VtucPerfCurr1DayEs": adGenVdsl2VtucPerfCurr1DayEs,
       "adGenVdsl2VtucPerfCurr1DayInits": adGenVdsl2VtucPerfCurr1DayInits,
       "adGenVdsl2VtucPerfCurr1DaySes": adGenVdsl2VtucPerfCurr1DaySes,
       "adGenVdsl2VtucPerfCurr1DayUas": adGenVdsl2VtucPerfCurr1DayUas,
       "adGenVdsl2VtucPerfCurr1DayFecs": adGenVdsl2VtucPerfCurr1DayFecs,
       "adGenVdsl2VtucPerfCurr1DayCrc": adGenVdsl2VtucPerfCurr1DayCrc,
       "adGenVdsl2VtucPerfCurr1DayFec": adGenVdsl2VtucPerfCurr1DayFec,
       "adGenVdsl2VtucPerfTcTxUnits": adGenVdsl2VtucPerfTcTxUnits,
       "adGenVdsl2VtucPerfTcTxDataUnits": adGenVdsl2VtucPerfTcTxDataUnits,
       "adGenVdsl2VtucPerfTcTxDataOctets": adGenVdsl2VtucPerfTcTxDataOctets,
       "adGenVdsl2VtucPerfTcTxIdleUnits": adGenVdsl2VtucPerfTcTxIdleUnits,
       "adGenVdsl2VtucPerfTcRxUnits": adGenVdsl2VtucPerfTcRxUnits,
       "adGenVdsl2VtucPerfTcRxDataUnits": adGenVdsl2VtucPerfTcRxDataUnits,
       "adGenVdsl2VtucPerfTcRxDataOctets": adGenVdsl2VtucPerfTcRxDataOctets,
       "adGenVdsl2VtucPerfTcRxIdleUnits": adGenVdsl2VtucPerfTcRxIdleUnits,
       "adGenVdsl2VtucPerfTcRxErroredUnits": adGenVdsl2VtucPerfTcRxErroredUnits,
       "adGenVdsl2VtucPerfSraDownshifts": adGenVdsl2VtucPerfSraDownshifts,
       "adGenVdsl2VtucPerfSraUpshifts": adGenVdsl2VtucPerfSraUpshifts,
       "adGenVdsl2VtucPerfCurr15MinSraDownshifts": adGenVdsl2VtucPerfCurr15MinSraDownshifts,
       "adGenVdsl2VtucPerfCurr15MinSraUpshifts": adGenVdsl2VtucPerfCurr15MinSraUpshifts,
       "adGenVdsl2VtucPerfCurr15MinSraRateMax": adGenVdsl2VtucPerfCurr15MinSraRateMax,
       "adGenVdsl2VtucPerfCurr15MinSraRateMin": adGenVdsl2VtucPerfCurr15MinSraRateMin,
       "adGenVdsl2VtucPerfCurr1DaySraDownshifts": adGenVdsl2VtucPerfCurr1DaySraDownshifts,
       "adGenVdsl2VtucPerfCurr1DaySraUpshifts": adGenVdsl2VtucPerfCurr1DaySraUpshifts,
       "adGenVdsl2VtucPerfCurr1DaySraRateMax": adGenVdsl2VtucPerfCurr1DaySraRateMax,
       "adGenVdsl2VtucPerfCurr1DaySraRateMin": adGenVdsl2VtucPerfCurr1DaySraRateMin,
       "adGenVdsl2VtucPerfRtxMinEftr": adGenVdsl2VtucPerfRtxMinEftr,
       "adGenVdsl2VtucPerfRtxLeftrs": adGenVdsl2VtucPerfRtxLeftrs,
       "adGenVdsl2VtucPerfCurr15MinRtxMinEftr": adGenVdsl2VtucPerfCurr15MinRtxMinEftr,
       "adGenVdsl2VtucPerfCurr15MinRtxLeftrs": adGenVdsl2VtucPerfCurr15MinRtxLeftrs,
       "adGenVdsl2VtucPerfCurr1DayRtxMinEftr": adGenVdsl2VtucPerfCurr1DayRtxMinEftr,
       "adGenVdsl2VtucPerfCurr1DayRtxLeftrs": adGenVdsl2VtucPerfCurr1DayRtxLeftrs,
       "adGenVdsl2VturPerfDataTable": adGenVdsl2VturPerfDataTable,
       "adGenVdsl2VturPerfDataEntry": adGenVdsl2VturPerfDataEntry,
       "adGenVdsl2VturPerfLofs": adGenVdsl2VturPerfLofs,
       "adGenVdsl2VturPerfLoss": adGenVdsl2VturPerfLoss,
       "adGenVdsl2VturPerfLprs": adGenVdsl2VturPerfLprs,
       "adGenVdsl2VturPerfEs": adGenVdsl2VturPerfEs,
       "adGenVdsl2VturPerfSes": adGenVdsl2VturPerfSes,
       "adGenVdsl2VturPerfUas": adGenVdsl2VturPerfUas,
       "adGenVdsl2VturPerfFecs": adGenVdsl2VturPerfFecs,
       "adGenVdsl2VturPerfCrc": adGenVdsl2VturPerfCrc,
       "adGenVdsl2VturPerfFec": adGenVdsl2VturPerfFec,
       "adGenVdsl2VturPerfValidIntervals": adGenVdsl2VturPerfValidIntervals,
       "adGenVdsl2VturPerfInvalidIntervals": adGenVdsl2VturPerfInvalidIntervals,
       "adGenVdsl2VturPerfCurr15MinTimeElapsed": adGenVdsl2VturPerfCurr15MinTimeElapsed,
       "adGenVdsl2VturPerfCurr15MinLofs": adGenVdsl2VturPerfCurr15MinLofs,
       "adGenVdsl2VturPerfCurr15MinLoss": adGenVdsl2VturPerfCurr15MinLoss,
       "adGenVdsl2VturPerfCurr15MinLprs": adGenVdsl2VturPerfCurr15MinLprs,
       "adGenVdsl2VturPerfCurr15MinEs": adGenVdsl2VturPerfCurr15MinEs,
       "adGenVdsl2VturPerfCurr15MinSes": adGenVdsl2VturPerfCurr15MinSes,
       "adGenVdsl2VturPerfCurr15MinUas": adGenVdsl2VturPerfCurr15MinUas,
       "adGenVdsl2VturPerfCurr15MinFecs": adGenVdsl2VturPerfCurr15MinFecs,
       "adGenVdsl2VturPerfCurr15MinCrc": adGenVdsl2VturPerfCurr15MinCrc,
       "adGenVdsl2VturPerfCurr15MinFec": adGenVdsl2VturPerfCurr15MinFec,
       "adGenVdsl2VturPerfCurr1DayTimeElapsed": adGenVdsl2VturPerfCurr1DayTimeElapsed,
       "adGenVdsl2VturPerfCurr1DayLofs": adGenVdsl2VturPerfCurr1DayLofs,
       "adGenVdsl2VturPerfCurr1DayLoss": adGenVdsl2VturPerfCurr1DayLoss,
       "adGenVdsl2VturPerfCurr1DayLprs": adGenVdsl2VturPerfCurr1DayLprs,
       "adGenVdsl2VturPerfCurr1DayEs": adGenVdsl2VturPerfCurr1DayEs,
       "adGenVdsl2VturPerfCurr1DaySes": adGenVdsl2VturPerfCurr1DaySes,
       "adGenVdsl2VturPerfCurr1DayUas": adGenVdsl2VturPerfCurr1DayUas,
       "adGenVdsl2VturPerfCurr1DayFecs": adGenVdsl2VturPerfCurr1DayFecs,
       "adGenVdsl2VturPerfCurr1DayCrc": adGenVdsl2VturPerfCurr1DayCrc,
       "adGenVdsl2VturPerfCurr1DayFec": adGenVdsl2VturPerfCurr1DayFec,
       "adGenVdsl2VturPerfTcTxUnits": adGenVdsl2VturPerfTcTxUnits,
       "adGenVdsl2VturPerfTcTxDataUnits": adGenVdsl2VturPerfTcTxDataUnits,
       "adGenVdsl2VturPerfTcTxDataOctets": adGenVdsl2VturPerfTcTxDataOctets,
       "adGenVdsl2VturPerfTcTxIdleUnits": adGenVdsl2VturPerfTcTxIdleUnits,
       "adGenVdsl2VturPerfTcRxUnits": adGenVdsl2VturPerfTcRxUnits,
       "adGenVdsl2VturPerfTcRxDataUnits": adGenVdsl2VturPerfTcRxDataUnits,
       "adGenVdsl2VturPerfTcRxDataOctets": adGenVdsl2VturPerfTcRxDataOctets,
       "adGenVdsl2VturPerfTcRxIdleUnits": adGenVdsl2VturPerfTcRxIdleUnits,
       "adGenVdsl2VturPerfTcRxErroredUnits": adGenVdsl2VturPerfTcRxErroredUnits,
       "adGenVdsl2VturPerfSraDownshifts": adGenVdsl2VturPerfSraDownshifts,
       "adGenVdsl2VturPerfSraUpshifts": adGenVdsl2VturPerfSraUpshifts,
       "adGenVdsl2VturPerfCurr15MinSraDownshifts": adGenVdsl2VturPerfCurr15MinSraDownshifts,
       "adGenVdsl2VturPerfCurr15MinSraUpshifts": adGenVdsl2VturPerfCurr15MinSraUpshifts,
       "adGenVdsl2VturPerfCurr15MinSraRateMax": adGenVdsl2VturPerfCurr15MinSraRateMax,
       "adGenVdsl2VturPerfCurr15MinSraRateMin": adGenVdsl2VturPerfCurr15MinSraRateMin,
       "adGenVdsl2VturPerfCurr1DaySraDownshifts": adGenVdsl2VturPerfCurr1DaySraDownshifts,
       "adGenVdsl2VturPerfCurr1DaySraUpshifts": adGenVdsl2VturPerfCurr1DaySraUpshifts,
       "adGenVdsl2VturPerfCurr1DaySraRateMax": adGenVdsl2VturPerfCurr1DaySraRateMax,
       "adGenVdsl2VturPerfCurr1DaySraRateMin": adGenVdsl2VturPerfCurr1DaySraRateMin,
       "adGenVdsl2VturPerfRtxMinEftr": adGenVdsl2VturPerfRtxMinEftr,
       "adGenVdsl2VturPerfRtxLeftrs": adGenVdsl2VturPerfRtxLeftrs,
       "adGenVdsl2VturPerfCurr15MinRtxMinEftr": adGenVdsl2VturPerfCurr15MinRtxMinEftr,
       "adGenVdsl2VturPerfCurr15MinRtxLeftrs": adGenVdsl2VturPerfCurr15MinRtxLeftrs,
       "adGenVdsl2VturPerfCurr1DayRtxMinEftr": adGenVdsl2VturPerfCurr1DayRtxMinEftr,
       "adGenVdsl2VturPerfCurr1DayRtxLeftrs": adGenVdsl2VturPerfCurr1DayRtxLeftrs,
       "adGenVdsl2VtucIntervalTable": adGenVdsl2VtucIntervalTable,
       "adGenVdsl2VtucIntervalEntry": adGenVdsl2VtucIntervalEntry,
       "adGenVdsl2VtucIntervalNumber": adGenVdsl2VtucIntervalNumber,
       "adGenVdsl2VtucIntervalLofs": adGenVdsl2VtucIntervalLofs,
       "adGenVdsl2VtucIntervalLoss": adGenVdsl2VtucIntervalLoss,
       "adGenVdsl2VtucIntervalLols": adGenVdsl2VtucIntervalLols,
       "adGenVdsl2VtucIntervalLprs": adGenVdsl2VtucIntervalLprs,
       "adGenVdsl2VtucIntervalES": adGenVdsl2VtucIntervalES,
       "adGenVdsl2VtucIntervalInits": adGenVdsl2VtucIntervalInits,
       "adGenVdsl2VtucIntervalValidData": adGenVdsl2VtucIntervalValidData,
       "adGenVdsl2VtucIntervalSES": adGenVdsl2VtucIntervalSES,
       "adGenVdsl2VtucIntervalUAS": adGenVdsl2VtucIntervalUAS,
       "adGenVdsl2VtucIntervalFECs": adGenVdsl2VtucIntervalFECs,
       "adGenVdsl2VtucIntervalFEC": adGenVdsl2VtucIntervalFEC,
       "adGenVdsl2VtucIntervalCRC": adGenVdsl2VtucIntervalCRC,
       "adGenVdsl2VtucIntervalSraDownshifts": adGenVdsl2VtucIntervalSraDownshifts,
       "adGenVdsl2VtucIntervalSraUpshifts": adGenVdsl2VtucIntervalSraUpshifts,
       "adGenVdsl2VtucIntervalSraRateMax": adGenVdsl2VtucIntervalSraRateMax,
       "adGenVdsl2VtucIntervalSraRateMin": adGenVdsl2VtucIntervalSraRateMin,
       "adGenVdsl2VtucIntervalRtxMinEftr": adGenVdsl2VtucIntervalRtxMinEftr,
       "adGenVdsl2VtucIntervalRtxLeftrs": adGenVdsl2VtucIntervalRtxLeftrs,
       "adGenVdsl2VturIntervalTable": adGenVdsl2VturIntervalTable,
       "adGenVdsl2VturIntervalEntry": adGenVdsl2VturIntervalEntry,
       "adGenVdsl2VturIntervalNumber": adGenVdsl2VturIntervalNumber,
       "adGenVdsl2VturIntervalLofs": adGenVdsl2VturIntervalLofs,
       "adGenVdsl2VturIntervalLoss": adGenVdsl2VturIntervalLoss,
       "adGenVdsl2VturIntervalLprs": adGenVdsl2VturIntervalLprs,
       "adGenVdsl2VturIntervalES": adGenVdsl2VturIntervalES,
       "adGenVdsl2VturIntervalValidData": adGenVdsl2VturIntervalValidData,
       "adGenVdsl2VturIntervalSES": adGenVdsl2VturIntervalSES,
       "adGenVdsl2VturIntervalUAS": adGenVdsl2VturIntervalUAS,
       "adGenVdsl2VturIntervalFECs": adGenVdsl2VturIntervalFECs,
       "adGenVdsl2VturIntervalFEC": adGenVdsl2VturIntervalFEC,
       "adGenVdsl2VturIntervalCRC": adGenVdsl2VturIntervalCRC,
       "adGenVdsl2VturIntervalSraDownshifts": adGenVdsl2VturIntervalSraDownshifts,
       "adGenVdsl2VturIntervalSraUpshifts": adGenVdsl2VturIntervalSraUpshifts,
       "adGenVdsl2VturIntervalSraRateMax": adGenVdsl2VturIntervalSraRateMax,
       "adGenVdsl2VturIntervalSraRateMin": adGenVdsl2VturIntervalSraRateMin,
       "adGenVdsl2VturIntervalRtxMinEftr": adGenVdsl2VturIntervalRtxMinEftr,
       "adGenVdsl2VturIntervalRtxLeftrs": adGenVdsl2VturIntervalRtxLeftrs,
       "adGenVdsl2VtucChanPerfDataTable": adGenVdsl2VtucChanPerfDataTable,
       "adGenVdsl2VtucChanPerfDataEntry": adGenVdsl2VtucChanPerfDataEntry,
       "adGenVdsl2VtucChanNumber": adGenVdsl2VtucChanNumber,
       "adGenVdsl2VtucChanReceivedBlks": adGenVdsl2VtucChanReceivedBlks,
       "adGenVdsl2VtucChanTransmittedBlks": adGenVdsl2VtucChanTransmittedBlks,
       "adGenVdsl2VtucChanCorrectedBlks": adGenVdsl2VtucChanCorrectedBlks,
       "adGenVdsl2VtucChanUncorrectBlks": adGenVdsl2VtucChanUncorrectBlks,
       "adGenVdsl2VtucChanPerfValidIntervals": adGenVdsl2VtucChanPerfValidIntervals,
       "adGenVdsl2VtucChanPerfInvalidIntervals": adGenVdsl2VtucChanPerfInvalidIntervals,
       "adGenVdsl2VtucChanPerfCurr15MinTimeElapsed": adGenVdsl2VtucChanPerfCurr15MinTimeElapsed,
       "adGenVdsl2VtucChanPerfCurr15MinReceivedBlks": adGenVdsl2VtucChanPerfCurr15MinReceivedBlks,
       "adGenVdsl2VtucChanPerfCurr15MinTransmittedBlks": adGenVdsl2VtucChanPerfCurr15MinTransmittedBlks,
       "adGenVdsl2VtucChanPerfCurr15MinCorrectedBlks": adGenVdsl2VtucChanPerfCurr15MinCorrectedBlks,
       "adGenVdsl2VtucChanPerfCurr15MinUncorrectBlks": adGenVdsl2VtucChanPerfCurr15MinUncorrectBlks,
       "adGenVdsl2VtucChanPerfCurr1DayTimeElapsed": adGenVdsl2VtucChanPerfCurr1DayTimeElapsed,
       "adGenVdsl2VtucChanPerfCurr1DayReceivedBlks": adGenVdsl2VtucChanPerfCurr1DayReceivedBlks,
       "adGenVdsl2VtucChanPerfCurr1DayTransmittedBlks": adGenVdsl2VtucChanPerfCurr1DayTransmittedBlks,
       "adGenVdsl2VtucChanPerfCurr1DayCorrectedBlks": adGenVdsl2VtucChanPerfCurr1DayCorrectedBlks,
       "adGenVdsl2VtucChanPerfCurr1DayUncorrectBlks": adGenVdsl2VtucChanPerfCurr1DayUncorrectBlks,
       "adGenVdsl2VtucChanPerfTcTxUnits": adGenVdsl2VtucChanPerfTcTxUnits,
       "adGenVdsl2VtucChanPerfTcTxDataUnits": adGenVdsl2VtucChanPerfTcTxDataUnits,
       "adGenVdsl2VtucChanPerfTcTxDataOctets": adGenVdsl2VtucChanPerfTcTxDataOctets,
       "adGenVdsl2VtucChanPerfTcTxIdleUnits": adGenVdsl2VtucChanPerfTcTxIdleUnits,
       "adGenVdsl2VtucChanPerfTcRxUnits": adGenVdsl2VtucChanPerfTcRxUnits,
       "adGenVdsl2VtucChanPerfTcRxDataUnits": adGenVdsl2VtucChanPerfTcRxDataUnits,
       "adGenVdsl2VtucChanPerfTcRxDataOctets": adGenVdsl2VtucChanPerfTcRxDataOctets,
       "adGenVdsl2VtucChanPerfTcRxIdleUnits": adGenVdsl2VtucChanPerfTcRxIdleUnits,
       "adGenVdsl2VtucChanPerfTcRxErroredUnits": adGenVdsl2VtucChanPerfTcRxErroredUnits,
       "adGenVdsl2VtucChanPerfRtxUncorrectedDtu": adGenVdsl2VtucChanPerfRtxUncorrectedDtu,
       "adGenVdsl2VtucChanPerfRtxCorrectedDtu": adGenVdsl2VtucChanPerfRtxCorrectedDtu,
       "adGenVdsl2VtucChanPerfRtxRetransmittedDtu": adGenVdsl2VtucChanPerfRtxRetransmittedDtu,
       "adGenVdsl2VtucChanPerfCurr15MinRtxUncorrectedDtu": adGenVdsl2VtucChanPerfCurr15MinRtxUncorrectedDtu,
       "adGenVdsl2VtucChanPerfCurr15MinRtxCorrectedDtu": adGenVdsl2VtucChanPerfCurr15MinRtxCorrectedDtu,
       "adGenVdsl2VtucChanPerfCurr15MinRtxRetransmittedDtu": adGenVdsl2VtucChanPerfCurr15MinRtxRetransmittedDtu,
       "adGenVdsl2VtucChanPerfCurr1DayRtxUncorrectedDtu": adGenVdsl2VtucChanPerfCurr1DayRtxUncorrectedDtu,
       "adGenVdsl2VtucChanPerfCurr1DayRtxCorrectedDtu": adGenVdsl2VtucChanPerfCurr1DayRtxCorrectedDtu,
       "adGenVdsl2VtucChanPerfCurr1DayRtxRetransmittedDtu": adGenVdsl2VtucChanPerfCurr1DayRtxRetransmittedDtu,
       "adGenVdsl2VturChanPerfDataTable": adGenVdsl2VturChanPerfDataTable,
       "adGenVdsl2VturChanPerfDataEntry": adGenVdsl2VturChanPerfDataEntry,
       "adGenVdsl2VturChanNumber": adGenVdsl2VturChanNumber,
       "adGenVdsl2VturChanReceivedBlks": adGenVdsl2VturChanReceivedBlks,
       "adGenVdsl2VturChanTransmittedBlks": adGenVdsl2VturChanTransmittedBlks,
       "adGenVdsl2VturChanCorrectedBlks": adGenVdsl2VturChanCorrectedBlks,
       "adGenVdsl2VturChanUncorrectBlks": adGenVdsl2VturChanUncorrectBlks,
       "adGenVdsl2VturChanPerfValidIntervals": adGenVdsl2VturChanPerfValidIntervals,
       "adGenVdsl2VturChanPerfInvalidIntervals": adGenVdsl2VturChanPerfInvalidIntervals,
       "adGenVdsl2VturChanPerfCurr15MinTimeElapsed": adGenVdsl2VturChanPerfCurr15MinTimeElapsed,
       "adGenVdsl2VturChanPerfCurr15MinReceivedBlks": adGenVdsl2VturChanPerfCurr15MinReceivedBlks,
       "adGenVdsl2VturChanPerfCurr15MinTransmittedBlks": adGenVdsl2VturChanPerfCurr15MinTransmittedBlks,
       "adGenVdsl2VturChanPerfCurr15MinCorrectedBlks": adGenVdsl2VturChanPerfCurr15MinCorrectedBlks,
       "adGenVdsl2VturChanPerfCurr15MinUncorrectBlks": adGenVdsl2VturChanPerfCurr15MinUncorrectBlks,
       "adGenVdsl2VturChanPerfCurr1DayTimeElapsed": adGenVdsl2VturChanPerfCurr1DayTimeElapsed,
       "adGenVdsl2VturChanPerfCurr1DayReceivedBlks": adGenVdsl2VturChanPerfCurr1DayReceivedBlks,
       "adGenVdsl2VturChanPerfCurr1DayTransmittedBlks": adGenVdsl2VturChanPerfCurr1DayTransmittedBlks,
       "adGenVdsl2VturChanPerfCurr1DayCorrectedBlks": adGenVdsl2VturChanPerfCurr1DayCorrectedBlks,
       "adGenVdsl2VturChanPerfCurr1DayUncorrectBlks": adGenVdsl2VturChanPerfCurr1DayUncorrectBlks,
       "adGenVdsl2VturChanPerfTcTxUnits": adGenVdsl2VturChanPerfTcTxUnits,
       "adGenVdsl2VturChanPerfTcTxDataUnits": adGenVdsl2VturChanPerfTcTxDataUnits,
       "adGenVdsl2VturChanPerfTcTxDataOctets": adGenVdsl2VturChanPerfTcTxDataOctets,
       "adGenVdsl2VturChanPerfTcTxIdleUnits": adGenVdsl2VturChanPerfTcTxIdleUnits,
       "adGenVdsl2VturChanPerfTcRxUnits": adGenVdsl2VturChanPerfTcRxUnits,
       "adGenVdsl2VturChanPerfTcRxDataUnits": adGenVdsl2VturChanPerfTcRxDataUnits,
       "adGenVdsl2VturChanPerfTcRxDataOctets": adGenVdsl2VturChanPerfTcRxDataOctets,
       "adGenVdsl2VturChanPerfTcRxIdleUnits": adGenVdsl2VturChanPerfTcRxIdleUnits,
       "adGenVdsl2VturChanPerfTcRxErroredUnits": adGenVdsl2VturChanPerfTcRxErroredUnits,
       "adGenVdsl2VturChanPerfRtxUncorrectedDtu": adGenVdsl2VturChanPerfRtxUncorrectedDtu,
       "adGenVdsl2VturChanPerfRtxCorrectedDtu": adGenVdsl2VturChanPerfRtxCorrectedDtu,
       "adGenVdsl2VturChanPerfRtxRetransmittedDtu": adGenVdsl2VturChanPerfRtxRetransmittedDtu,
       "adGenVdsl2VturChanPerfCurr15MinRtxUncorrectedDtu": adGenVdsl2VturChanPerfCurr15MinRtxUncorrectedDtu,
       "adGenVdsl2VturChanPerfCurr15MinRtxCorrectedDtu": adGenVdsl2VturChanPerfCurr15MinRtxCorrectedDtu,
       "adGenVdsl2VturChanPerfCurr15MinRtxRetransmittedDtu": adGenVdsl2VturChanPerfCurr15MinRtxRetransmittedDtu,
       "adGenVdsl2VturChanPerfCurr1DayRtxUncorrectedDtu": adGenVdsl2VturChanPerfCurr1DayRtxUncorrectedDtu,
       "adGenVdsl2VturChanPerfCurr1DayRtxCorrectedDtu": adGenVdsl2VturChanPerfCurr1DayRtxCorrectedDtu,
       "adGenVdsl2VturChanPerfCurr1DayRtxRetransmittedDtu": adGenVdsl2VturChanPerfCurr1DayRtxRetransmittedDtu,
       "adGenVdsl2VtucChanIntervalTable": adGenVdsl2VtucChanIntervalTable,
       "adGenVdsl2VtucChanIntervalEntry": adGenVdsl2VtucChanIntervalEntry,
       "adGenVdsl2VtucChanNum": adGenVdsl2VtucChanNum,
       "adGenVdsl2VtucChanIntervalNumber": adGenVdsl2VtucChanIntervalNumber,
       "adGenVdsl2VtucChanIntervalReceivedBlks": adGenVdsl2VtucChanIntervalReceivedBlks,
       "adGenVdsl2VtucChanIntervalTransmittedBlks": adGenVdsl2VtucChanIntervalTransmittedBlks,
       "adGenVdsl2VtucChanIntervalCorrectedBlks": adGenVdsl2VtucChanIntervalCorrectedBlks,
       "adGenVdsl2VtucChanIntervalUncorrectBlks": adGenVdsl2VtucChanIntervalUncorrectBlks,
       "adGenVdsl2VtucChanIntervalValidData": adGenVdsl2VtucChanIntervalValidData,
       "adGenVdsl2VtucChanIntervalRtxUncorrectedDtu": adGenVdsl2VtucChanIntervalRtxUncorrectedDtu,
       "adGenVdsl2VtucChanIntervalRtxCorrectedDtu": adGenVdsl2VtucChanIntervalRtxCorrectedDtu,
       "adGenVdsl2VtucChanIntervalRtxRetransmittedDtu": adGenVdsl2VtucChanIntervalRtxRetransmittedDtu,
       "adGenVdsl2VturChanIntervalTable": adGenVdsl2VturChanIntervalTable,
       "adGenVdsl2VturChanIntervalEntry": adGenVdsl2VturChanIntervalEntry,
       "adGenVdsl2VturChanNum": adGenVdsl2VturChanNum,
       "adGenVdsl2VturChanIntervalNumber": adGenVdsl2VturChanIntervalNumber,
       "adGenVdsl2VturChanIntervalReceivedBlks": adGenVdsl2VturChanIntervalReceivedBlks,
       "adGenVdsl2VturChanIntervalTransmittedBlks": adGenVdsl2VturChanIntervalTransmittedBlks,
       "adGenVdsl2VturChanIntervalCorrectedBlks": adGenVdsl2VturChanIntervalCorrectedBlks,
       "adGenVdsl2VturChanIntervalUncorrectBlks": adGenVdsl2VturChanIntervalUncorrectBlks,
       "adGenVdsl2VturChanIntervalValidData": adGenVdsl2VturChanIntervalValidData,
       "adGenVdsl2VturChanIntervalRtxUncorrectedDtu": adGenVdsl2VturChanIntervalRtxUncorrectedDtu,
       "adGenVdsl2VturChanIntervalRtxCorrectedDtu": adGenVdsl2VturChanIntervalRtxCorrectedDtu,
       "adGenVdsl2VturChanIntervalRtxRetransmittedDtu": adGenVdsl2VturChanIntervalRtxRetransmittedDtu,
       "adGenVdsl2Vtuc1DayIntervalTable": adGenVdsl2Vtuc1DayIntervalTable,
       "adGenVdsl2Vtuc1DayIntervalEntry": adGenVdsl2Vtuc1DayIntervalEntry,
       "adGenVdsl2Vtuc1DayIntervalNumber": adGenVdsl2Vtuc1DayIntervalNumber,
       "adGenVdsl2Vtuc1DayIntervalLofs": adGenVdsl2Vtuc1DayIntervalLofs,
       "adGenVdsl2Vtuc1DayIntervalLoss": adGenVdsl2Vtuc1DayIntervalLoss,
       "adGenVdsl2Vtuc1DayIntervalLols": adGenVdsl2Vtuc1DayIntervalLols,
       "adGenVdsl2Vtuc1DayIntervalLprs": adGenVdsl2Vtuc1DayIntervalLprs,
       "adGenVdsl2Vtuc1DayIntervalES": adGenVdsl2Vtuc1DayIntervalES,
       "adGenVdsl2Vtuc1DayIntervalInits": adGenVdsl2Vtuc1DayIntervalInits,
       "adGenVdsl2Vtuc1DayIntervalValidData": adGenVdsl2Vtuc1DayIntervalValidData,
       "adGenVdsl2Vtuc1DayIntervalSES": adGenVdsl2Vtuc1DayIntervalSES,
       "adGenVdsl2Vtuc1DayIntervalUAS": adGenVdsl2Vtuc1DayIntervalUAS,
       "adGenVdsl2Vtuc1DayIntervalFECs": adGenVdsl2Vtuc1DayIntervalFECs,
       "adGenVdsl2Vtuc1DayIntervalFEC": adGenVdsl2Vtuc1DayIntervalFEC,
       "adGenVdsl2Vtuc1DayIntervalCRC": adGenVdsl2Vtuc1DayIntervalCRC,
       "adGenVdsl2Vtuc1DayIntervalSraDownshifts": adGenVdsl2Vtuc1DayIntervalSraDownshifts,
       "adGenVdsl2Vtuc1DayIntervalSraUpshifts": adGenVdsl2Vtuc1DayIntervalSraUpshifts,
       "adGenVdsl2Vtuc1DayIntervalSraRateMax": adGenVdsl2Vtuc1DayIntervalSraRateMax,
       "adGenVdsl2Vtuc1DayIntervalSraRateMin": adGenVdsl2Vtuc1DayIntervalSraRateMin,
       "adGenVdsl2Vtuc1DayIntervalRtxMinEftr": adGenVdsl2Vtuc1DayIntervalRtxMinEftr,
       "adGenVdsl2Vtuc1DayIntervalRtxLeftrs": adGenVdsl2Vtuc1DayIntervalRtxLeftrs,
       "adGenVdsl2Vtur1DayIntervalTable": adGenVdsl2Vtur1DayIntervalTable,
       "adGenVdsl2Vtur1DayIntervalEntry": adGenVdsl2Vtur1DayIntervalEntry,
       "adGenVdsl2Vtur1DayIntervalNumber": adGenVdsl2Vtur1DayIntervalNumber,
       "adGenVdsl2Vtur1DayIntervalLofs": adGenVdsl2Vtur1DayIntervalLofs,
       "adGenVdsl2Vtur1DayIntervalLoss": adGenVdsl2Vtur1DayIntervalLoss,
       "adGenVdsl2Vtur1DayIntervalLprs": adGenVdsl2Vtur1DayIntervalLprs,
       "adGenVdsl2Vtur1DayIntervalES": adGenVdsl2Vtur1DayIntervalES,
       "adGenVdsl2Vtur1DayIntervalValidData": adGenVdsl2Vtur1DayIntervalValidData,
       "adGenVdsl2Vtur1DayIntervalSES": adGenVdsl2Vtur1DayIntervalSES,
       "adGenVdsl2Vtur1DayIntervalUAS": adGenVdsl2Vtur1DayIntervalUAS,
       "adGenVdsl2Vtur1DayIntervalFECs": adGenVdsl2Vtur1DayIntervalFECs,
       "adGenVdsl2Vtur1DayIntervalFEC": adGenVdsl2Vtur1DayIntervalFEC,
       "adGenVdsl2Vtur1DayIntervalCRC": adGenVdsl2Vtur1DayIntervalCRC,
       "adGenVdsl2Vtur1DayIntervalSraDownshifts": adGenVdsl2Vtur1DayIntervalSraDownshifts,
       "adGenVdsl2Vtur1DayIntervalSraUpshifts": adGenVdsl2Vtur1DayIntervalSraUpshifts,
       "adGenVdsl2Vtur1DayIntervalSraRateMax": adGenVdsl2Vtur1DayIntervalSraRateMax,
       "adGenVdsl2Vtur1DayIntervalSraRateMin": adGenVdsl2Vtur1DayIntervalSraRateMin,
       "adGenVdsl2Vtur1DayIntervalRtxMinEftr": adGenVdsl2Vtur1DayIntervalRtxMinEftr,
       "adGenVdsl2Vtur1DayIntervalRtxLeftrs": adGenVdsl2Vtur1DayIntervalRtxLeftrs,
       "adGenVdsl2VtucChan1DayIntervalTable": adGenVdsl2VtucChan1DayIntervalTable,
       "adGenVdsl2VtucChan1DayIntervalEntry": adGenVdsl2VtucChan1DayIntervalEntry,
       "adGenVdsl2Vtuc1DayChanNum": adGenVdsl2Vtuc1DayChanNum,
       "adGenVdsl2VtucChan1DayIntervalNumber": adGenVdsl2VtucChan1DayIntervalNumber,
       "adGenVdsl2VtucChan1DayIntervalReceivedBlks": adGenVdsl2VtucChan1DayIntervalReceivedBlks,
       "adGenVdsl2VtucChan1DayIntervalTransmittedBlks": adGenVdsl2VtucChan1DayIntervalTransmittedBlks,
       "adGenVdsl2VtucChan1DayIntervalCorrectedBlks": adGenVdsl2VtucChan1DayIntervalCorrectedBlks,
       "adGenVdsl2VtucChan1DayIntervalUncorrectBlks": adGenVdsl2VtucChan1DayIntervalUncorrectBlks,
       "adGenVdsl2VtucChan1DayIntervalValidData": adGenVdsl2VtucChan1DayIntervalValidData,
       "adGenVdsl2VtucChan1DayIntervalRtxUncorrectedDtu": adGenVdsl2VtucChan1DayIntervalRtxUncorrectedDtu,
       "adGenVdsl2VtucChan1DayIntervalRtxCorrectedDtu": adGenVdsl2VtucChan1DayIntervalRtxCorrectedDtu,
       "adGenVdsl2VtucChan1DayIntervalRtxRetransmittedDtu": adGenVdsl2VtucChan1DayIntervalRtxRetransmittedDtu,
       "adGenVdsl2VturChan1DayIntervalTable": adGenVdsl2VturChan1DayIntervalTable,
       "adGenVdsl2VturChan1DayIntervalEntry": adGenVdsl2VturChan1DayIntervalEntry,
       "adGenVdsl2Vtur1DayChanNum": adGenVdsl2Vtur1DayChanNum,
       "adGenVdsl2VturChan1DayIntervalNumber": adGenVdsl2VturChan1DayIntervalNumber,
       "adGenVdsl2VturChan1DayIntervalReceivedBlks": adGenVdsl2VturChan1DayIntervalReceivedBlks,
       "adGenVdsl2VturChan1DayIntervalTransmittedBlks": adGenVdsl2VturChan1DayIntervalTransmittedBlks,
       "adGenVdsl2VturChan1DayIntervalCorrectedBlks": adGenVdsl2VturChan1DayIntervalCorrectedBlks,
       "adGenVdsl2VturChan1DayIntervalUncorrectBlks": adGenVdsl2VturChan1DayIntervalUncorrectBlks,
       "adGenVdsl2VturChan1DayIntervalValidData": adGenVdsl2VturChan1DayIntervalValidData,
       "adGenVdsl2VturChan1DayIntervalRtxUncorrectedDtu": adGenVdsl2VturChan1DayIntervalRtxUncorrectedDtu,
       "adGenVdsl2VturChan1DayIntervalRtxCorrectedDtu": adGenVdsl2VturChan1DayIntervalRtxCorrectedDtu,
       "adGenVdsl2VturChan1DayIntervalRtxRetransmittedDtu": adGenVdsl2VturChan1DayIntervalRtxRetransmittedDtu,
       "adGenVdsl2Traps": adGenVdsl2Traps,
       "adGenVdsl2VtucTrapPrefix": adGenVdsl2VtucTrapPrefix,
       "adGenVdsl2VtucTraps": adGenVdsl2VtucTraps,
       "adGenVdsl2VtucSnrMgnThreshTrap": adGenVdsl2VtucSnrMgnThreshTrap,
       "adGenVdsl2VtucLofsThreshTrap": adGenVdsl2VtucLofsThreshTrap,
       "adGenVdsl2VtucLossThreshTrap": adGenVdsl2VtucLossThreshTrap,
       "adGenVdsl2VtucLolsThreshTrap": adGenVdsl2VtucLolsThreshTrap,
       "adGenVdsl2VtucLprsThreshTrap": adGenVdsl2VtucLprsThreshTrap,
       "adGenVdsl2VtucESThreshTrap": adGenVdsl2VtucESThreshTrap,
       "adGenVdsl2VtucSESThreshTrap": adGenVdsl2VtucSESThreshTrap,
       "adGenVdsl2VtucUASThreshTrap": adGenVdsl2VtucUASThreshTrap,
       "adGenVdsl2VturTrapPrefix": adGenVdsl2VturTrapPrefix,
       "adGenVdsl2VturTraps": adGenVdsl2VturTraps,
       "adGenVdsl2VturSnrMgnThreshTrap": adGenVdsl2VturSnrMgnThreshTrap,
       "adGenVdsl2VturLofsThreshTrap": adGenVdsl2VturLofsThreshTrap,
       "adGenVdsl2VturLossThreshTrap": adGenVdsl2VturLossThreshTrap,
       "adGenVdsl2VturLprsThreshTrap": adGenVdsl2VturLprsThreshTrap,
       "adGenVdsl2VturESThreshTrap": adGenVdsl2VturESThreshTrap,
       "adGenVdsl2VturSESThreshTrap": adGenVdsl2VturSESThreshTrap,
       "adGenVdsl2VturUASThreshTrap": adGenVdsl2VturUASThreshTrap,
       "adGenVdsl2VtucTrapPrefixRemote": adGenVdsl2VtucTrapPrefixRemote,
       "adGenVdsl2VtucRemoteTraps": adGenVdsl2VtucRemoteTraps,
       "adGenVdsl2VtucSnrMgnRemoteThreshTrap": adGenVdsl2VtucSnrMgnRemoteThreshTrap,
       "adGenVdsl2VtucLofsRemoteThreshTrap": adGenVdsl2VtucLofsRemoteThreshTrap,
       "adGenVdsl2VtucLossRemoteThreshTrap": adGenVdsl2VtucLossRemoteThreshTrap,
       "adGenVdsl2VtucLolsRemoteThreshTrap": adGenVdsl2VtucLolsRemoteThreshTrap,
       "adGenVdsl2VtucLprsRemoteThreshTrap": adGenVdsl2VtucLprsRemoteThreshTrap,
       "adGenVdsl2VtucESRemoteThreshTrap": adGenVdsl2VtucESRemoteThreshTrap,
       "adGenVdsl2VtucSESRemoteThreshTrap": adGenVdsl2VtucSESRemoteThreshTrap,
       "adGenVdsl2VtucUASRemoteThreshTrap": adGenVdsl2VtucUASRemoteThreshTrap,
       "adGenVdsl2VturTrapPrefixRemote": adGenVdsl2VturTrapPrefixRemote,
       "adGenVdsl2VturRemoteTraps": adGenVdsl2VturRemoteTraps,
       "adGenVdsl2VturSnrMgnRemoteThreshTrap": adGenVdsl2VturSnrMgnRemoteThreshTrap,
       "adGenVdsl2VturLofsRemoteThreshTrap": adGenVdsl2VturLofsRemoteThreshTrap,
       "adGenVdsl2VturLossRemoteThreshTrap": adGenVdsl2VturLossRemoteThreshTrap,
       "adGenVdsl2VturLprsRemoteThreshTrap": adGenVdsl2VturLprsRemoteThreshTrap,
       "adGenVdsl2VturESRemoteThreshTrap": adGenVdsl2VturESRemoteThreshTrap,
       "adGenVdsl2VturSESRemoteThreshTrap": adGenVdsl2VturSESRemoteThreshTrap,
       "adGenVdsl2VturUASRemoteThreshTrap": adGenVdsl2VturUASRemoteThreshTrap,
       "adGenVdsl2ExtConfig": adGenVdsl2ExtConfig,
       "adGenVdsl2ConfProfileExtTable": adGenVdsl2ConfProfileExtTable,
       "adGenVdsl2ConfProfileExtEntry": adGenVdsl2ConfProfileExtEntry,
       "adGenVdsl2LineManagementProfileNameApplied": adGenVdsl2LineManagementProfileNameApplied,
       "adGenVdsl2LineManagementProfileIndexApplied": adGenVdsl2LineManagementProfileIndexApplied,
       "adGenVdsl2LineCircuitID": adGenVdsl2LineCircuitID,
       "adGenVdsl2LineResetCounters": adGenVdsl2LineResetCounters,
       "adGenVdsl2LineRetrainRequest": adGenVdsl2LineRetrainRequest,
       "adGenVdsl2Test": adGenVdsl2Test,
       "adGenVdsl2MibConformance": adGenVdsl2MibConformance,
       "adGenVdsl2MibGroups": adGenVdsl2MibGroups,
       "adGenVdsl2ProvGroup": adGenVdsl2ProvGroup,
       "adGenVdsl2StatusGroup": adGenVdsl2StatusGroup,
       "adGenVdsl2PMGroup": adGenVdsl2PMGroup,
       "adGenVdsl2TrapsGroup": adGenVdsl2TrapsGroup,
       "adGenVdsl2ExtConfigGroup": adGenVdsl2ExtConfigGroup,
       "adGenVdsl2MIB": adGenVdsl2MIB}
)
