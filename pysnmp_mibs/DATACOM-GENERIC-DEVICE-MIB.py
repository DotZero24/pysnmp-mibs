# SNMP MIB module (DATACOM-GENERIC-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/datacom/DATACOM-GENERIC-DEVICE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:04:46 2025
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

(datacomGenericMIBs,
 datacomModules) = mibBuilder.importSymbols(
    "DATACOM-SMI",
    "datacomGenericMIBs",
    "datacomModules")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class DmUnsigned(Unsigned32):
    """Custom type DmUnsigned based on Unsigned32"""




class DmDevIndex(Integer32):
    """Custom type DmDevIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )





class DmDevLocalIndex(Integer32):
    """Custom type DmDevLocalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )





class DmSlotIndex(Integer32):
    """Custom type DmSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )





class DmPortIndex(Integer32):
    """Custom type DmPortIndex based on Integer32"""




class DmTrapIndex(Integer32):
    """Custom type DmTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DatacomGenericDeviceMIBModule_ObjectIdentity = ObjectIdentity
datacomGenericDeviceMIBModule = _DatacomGenericDeviceMIBModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 1, 1, 23)
)
_DmGenericDeviceMIB_ObjectIdentity = ObjectIdentity
dmGenericDeviceMIB = _DmGenericDeviceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3)
)
_DmGenDvInf_ObjectIdentity = ObjectIdentity
dmGenDvInf = _DmGenDvInf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1)
)
_GenDvInfMibVersion_Type = DisplayString
_GenDvInfMibVersion_Object = MibScalar
genDvInfMibVersion = _GenDvInfMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 1),
    _GenDvInfMibVersion_Type()
)
genDvInfMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfMibVersion.setStatus("mandatory")
_GenDvInfDeviceTable_Object = MibTable
genDvInfDeviceTable = _GenDvInfDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 10)
)
if mibBuilder.loadTexts:
    genDvInfDeviceTable.setStatus("mandatory")
_GenDvInfDeviceEntry_Object = MibTableRow
genDvInfDeviceEntry = _GenDvInfDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 10, 1)
)
genDvInfDeviceEntry.setIndexNames(
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvInfDeviceDevNo"),
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvInfDeviceDevLocalId"),
)
if mibBuilder.loadTexts:
    genDvInfDeviceEntry.setStatus("mandatory")
_GenDvInfDeviceDevNo_Type = DmDevIndex
_GenDvInfDeviceDevNo_Object = MibTableColumn
genDvInfDeviceDevNo = _GenDvInfDeviceDevNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 10, 1, 1),
    _GenDvInfDeviceDevNo_Type()
)
genDvInfDeviceDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfDeviceDevNo.setStatus("mandatory")
_GenDvInfDeviceDevLocalId_Type = DmDevLocalIndex
_GenDvInfDeviceDevLocalId_Object = MibTableColumn
genDvInfDeviceDevLocalId = _GenDvInfDeviceDevLocalId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 10, 1, 2),
    _GenDvInfDeviceDevLocalId_Type()
)
genDvInfDeviceDevLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfDeviceDevLocalId.setStatus("mandatory")
_GenDvInfDeviceProduct_Type = ObjectIdentifier
_GenDvInfDeviceProduct_Object = MibTableColumn
genDvInfDeviceProduct = _GenDvInfDeviceProduct_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 10, 1, 3),
    _GenDvInfDeviceProduct_Type()
)
genDvInfDeviceProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfDeviceProduct.setStatus("mandatory")


class _GenDvInfDeviceFirmVersion_Type(Integer32):
    """Custom type genDvInfDeviceFirmVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GenDvInfDeviceFirmVersion_Type.__name__ = "Integer32"
_GenDvInfDeviceFirmVersion_Object = MibTableColumn
genDvInfDeviceFirmVersion = _GenDvInfDeviceFirmVersion_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 10, 1, 4),
    _GenDvInfDeviceFirmVersion_Type()
)
genDvInfDeviceFirmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfDeviceFirmVersion.setStatus("mandatory")
_GenDvInfDeviceBootVersion_Type = DisplayString
_GenDvInfDeviceBootVersion_Object = MibTableColumn
genDvInfDeviceBootVersion = _GenDvInfDeviceBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 10, 1, 5),
    _GenDvInfDeviceBootVersion_Type()
)
genDvInfDeviceBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfDeviceBootVersion.setStatus("mandatory")
_GenDvInfDeviceHWVersion_Type = DisplayString
_GenDvInfDeviceHWVersion_Object = MibTableColumn
genDvInfDeviceHWVersion = _GenDvInfDeviceHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 10, 1, 6),
    _GenDvInfDeviceHWVersion_Type()
)
genDvInfDeviceHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfDeviceHWVersion.setStatus("mandatory")
_GenDvInfDeviceSerialNo_Type = DisplayString
_GenDvInfDeviceSerialNo_Object = MibTableColumn
genDvInfDeviceSerialNo = _GenDvInfDeviceSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 10, 1, 7),
    _GenDvInfDeviceSerialNo_Type()
)
genDvInfDeviceSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfDeviceSerialNo.setStatus("mandatory")
_GenDvInfDeviceIdent_Type = Integer32
_GenDvInfDeviceIdent_Object = MibTableColumn
genDvInfDeviceIdent = _GenDvInfDeviceIdent_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 10, 1, 8),
    _GenDvInfDeviceIdent_Type()
)
genDvInfDeviceIdent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genDvInfDeviceIdent.setStatus("mandatory")
_GenDvInfDeviceFirmReleaseDate_Type = DisplayString
_GenDvInfDeviceFirmReleaseDate_Object = MibTableColumn
genDvInfDeviceFirmReleaseDate = _GenDvInfDeviceFirmReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 10, 1, 9),
    _GenDvInfDeviceFirmReleaseDate_Type()
)
genDvInfDeviceFirmReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfDeviceFirmReleaseDate.setStatus("mandatory")
_GenDvInfDeviceE2PROMversion_Type = Integer32
_GenDvInfDeviceE2PROMversion_Object = MibTableColumn
genDvInfDeviceE2PROMversion = _GenDvInfDeviceE2PROMversion_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 10, 1, 10),
    _GenDvInfDeviceE2PROMversion_Type()
)
genDvInfDeviceE2PROMversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfDeviceE2PROMversion.setStatus("mandatory")
_GenDvInfDeviceFirmVersionString_Type = DisplayString
_GenDvInfDeviceFirmVersionString_Object = MibTableColumn
genDvInfDeviceFirmVersionString = _GenDvInfDeviceFirmVersionString_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 10, 1, 11),
    _GenDvInfDeviceFirmVersionString_Type()
)
genDvInfDeviceFirmVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfDeviceFirmVersionString.setStatus("mandatory")


class _GenDvInfDeviceVendor_Type(Integer32):
    """Custom type genDvInfDeviceVendor based on Integer32"""
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
              2000000254,
              2000000255)
        )
    )
    namedValues = NamedValues(
        *(("datacom", 1),
          ("ieru", 2),
          ("asga", 3),
          ("parks", 4),
          ("digitel", 5),
          ("none", 6),
          ("eletech", 7),
          ("xb-systems", 8),
          ("osp", 9),
          ("actelis", 10),
          ("juniper", 11),
          ("gdc", 12),
          ("monytel", 13),
          ("digistar", 14),
          ("objectNonexistentInModel", 2000000254),
          ("infNotAvailable", 2000000255))
    )


_GenDvInfDeviceVendor_Type.__name__ = "Integer32"
_GenDvInfDeviceVendor_Object = MibTableColumn
genDvInfDeviceVendor = _GenDvInfDeviceVendor_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 10, 1, 20),
    _GenDvInfDeviceVendor_Type()
)
genDvInfDeviceVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfDeviceVendor.setStatus("mandatory")
_GenDvInfPortTable_Object = MibTable
genDvInfPortTable = _GenDvInfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 12)
)
if mibBuilder.loadTexts:
    genDvInfPortTable.setStatus("mandatory")
_GenDvInfPortEntry_Object = MibTableRow
genDvInfPortEntry = _GenDvInfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 12, 1)
)
genDvInfPortEntry.setIndexNames(
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvInfPortDevNo"),
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvInfPortDevLocalId"),
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvInfPortSlotNo"),
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvInfPortPortNo"),
)
if mibBuilder.loadTexts:
    genDvInfPortEntry.setStatus("mandatory")
_GenDvInfPortDevNo_Type = DmDevIndex
_GenDvInfPortDevNo_Object = MibTableColumn
genDvInfPortDevNo = _GenDvInfPortDevNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 12, 1, 1),
    _GenDvInfPortDevNo_Type()
)
genDvInfPortDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfPortDevNo.setStatus("mandatory")
_GenDvInfPortDevLocalId_Type = DmDevLocalIndex
_GenDvInfPortDevLocalId_Object = MibTableColumn
genDvInfPortDevLocalId = _GenDvInfPortDevLocalId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 12, 1, 2),
    _GenDvInfPortDevLocalId_Type()
)
genDvInfPortDevLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfPortDevLocalId.setStatus("mandatory")
_GenDvInfPortSlotNo_Type = DmSlotIndex
_GenDvInfPortSlotNo_Object = MibTableColumn
genDvInfPortSlotNo = _GenDvInfPortSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 12, 1, 3),
    _GenDvInfPortSlotNo_Type()
)
genDvInfPortSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfPortSlotNo.setStatus("mandatory")
_GenDvInfPortPortNo_Type = DmPortIndex
_GenDvInfPortPortNo_Object = MibTableColumn
genDvInfPortPortNo = _GenDvInfPortPortNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 12, 1, 4),
    _GenDvInfPortPortNo_Type()
)
genDvInfPortPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfPortPortNo.setStatus("mandatory")


class _GenDvInfPortModel_Type(Integer32):
    """Custom type genDvInfPortModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              129,
              137,
              139,
              144,
              170,
              193,
              208,
              231,
              247,
              301,
              302,
              303,
              304,
              305,
              341,
              361,
              381,
              382,
              391,
              399,
              401,
              402,
              403,
              404,
              405,
              421,
              422,
              423,
              424,
              425,
              441,
              461,
              481,
              482,
              491,
              499,
              501,
              521,
              531,
              541,
              573,
              631,
              661,
              731,
              761,
              831,
              851,
              861,
              931,
              951,
              961,
              1011,
              1012,
              1031,
              1061,
              1101,
              1102,
              1103,
              1104,
              1105,
              1141,
              1161,
              1167,
              1211,
              1212,
              1231,
              1261,
              1311,
              1312,
              1331,
              1351,
              1361,
              1411,
              1412,
              1431,
              1451,
              1461,
              1501,
              1502,
              1503,
              1504,
              1505,
              1541,
              1551,
              1561,
              1567,
              1598,
              1599,
              1601,
              1602,
              1603,
              1604,
              1605,
              1641,
              1661,
              1667,
              1698,
              1699,
              1701,
              1711,
              1712,
              1731,
              2006,
              2007,
              2008,
              2009,
              2010,
              2041,
              2061,
              2081,
              2082,
              2099,
              2111,
              2112,
              2113,
              2114,
              2115,
              2141,
              2161,
              2181,
              2182,
              2199,
              2301,
              2302,
              2303,
              2304,
              2305,
              2341,
              2361,
              2381,
              2383,
              2391,
              2398,
              2399,
              2401,
              2402,
              2403,
              2404,
              2405,
              2441,
              2461,
              2481,
              2483,
              2491,
              2498,
              2499,
              5001,
              5002,
              5003,
              5004,
              5005,
              5051,
              5061,
              5101,
              5105,
              5110,
              5115,
              5120,
              5125,
              5130,
              5135,
              5140,
              5180,
              5185,
              5201,
              5205,
              5210,
              5215,
              5251,
              5401,
              5405,
              5410,
              5415,
              5420,
              6001,
              6002,
              6003,
              2000000254,
              2000000255)
        )
    )
    namedValues = NamedValues(
        *(("dm705-ROUTER", 10),
          ("dm705-BBM", 129),
          ("dm705-GSHDSL-D", 137),
          ("dm705-GSHDSL", 139),
          ("dm705-FO", 144),
          ("dm705-E1", 170),
          ("dm705-POTS", 193),
          ("dm705-10BT", 208),
          ("dm705-V35D", 231),
          ("dm705-G64", 247),
          ("dm16E1-E3-G703", 301),
          ("dm16E1-E3-MM", 302),
          ("dm16E1-E3-SM", 303),
          ("dm16E1-E3-B13", 304),
          ("dm16E1-E3-B15", 305),
          ("dm16E1-E1", 341),
          ("dm16E1-V35", 361),
          ("dm16E1-10BT", 381),
          ("dm16E1-10BT-HW2", 382),
          ("dm16E1-G703-E3i", 391),
          ("dm16E1-ROUTER", 399),
          ("dm4E1-E3-G703", 401),
          ("dm4E1-E3-MM", 402),
          ("dm4E1-E3-SM", 403),
          ("dm4E1-E3-B13", 404),
          ("dm4E1-E3-B15", 405),
          ("dm4E1-E2-G703", 421),
          ("dm4E1-E2-MM", 422),
          ("dm4E1-E2-SM", 423),
          ("dm4E1-E2-B13", 424),
          ("dm4E1-E2-B15", 425),
          ("dm4E1-E1", 441),
          ("dm4E1-V35", 461),
          ("dm4E1-10BT", 481),
          ("dm4E1-10BT-HW2", 482),
          ("dm4E1-G703-E3i", 491),
          ("dm4E1-ROUTER", 499),
          ("dm706C-ROUTER", 501),
          ("dm706C-FO", 521),
          ("dm706C-E1", 531),
          ("dm706C-FXS", 541),
          ("dm706C-V35", 573),
          ("dm704C-E1", 631),
          ("dm704C-V35", 661),
          ("dm704S-E1", 731),
          ("dm704S-V35", 761),
          ("dm704CE-E1", 831),
          ("dm704CE-Bridge", 851),
          ("dm704CE-V35", 861),
          ("dm704SE-E1", 931),
          ("dm704SE-Bridge", 951),
          ("dm704SE-V35", 961),
          ("dm991C-GSHDSL", 1011),
          ("dm991C-GSHDSL-4F", 1012),
          ("dm991C-E1", 1031),
          ("dm991C-V35D", 1061),
          ("dm4E1S-E", 1101),
          ("dm4E1S-MM", 1102),
          ("dm4E1S-SM", 1103),
          ("dm4E1S-B13", 1104),
          ("dm4E1S-B15", 1105),
          ("dm4E1S-E1", 1141),
          ("dm4E1S-V35", 1161),
          ("dm4E1S-V28", 1167),
          ("dm991S-GSHDSL", 1211),
          ("dm991S-GSHDSL-4F", 1212),
          ("dm991S-E1", 1231),
          ("dm991S-V35D", 1261),
          ("dm991CE-GSHDSL", 1311),
          ("dm991CE-GSHDSL-4F", 1312),
          ("dm991CE-E1", 1331),
          ("dm991CE-Bridge", 1351),
          ("dm991CE-V35D", 1361),
          ("dm991SE-GSHDSL", 1411),
          ("dm991SE-GSHDSL-4F", 1412),
          ("dm991SE-E1", 1431),
          ("dm991SE-Bridge", 1451),
          ("dm991SE-V35D", 1461),
          ("dm300-8E1B-E", 1501),
          ("dm300-8E1B-MM", 1502),
          ("dm300-8E1B-SM", 1503),
          ("dm300-8E1B-B13", 1504),
          ("dm300-8E1B-B15", 1505),
          ("dm300-8E1B-E1", 1541),
          ("dm300-8E1B-Bridge", 1551),
          ("dm300-8E1B-V35", 1561),
          ("dm300-8E1B-V28", 1567),
          ("dm300-8E1B-DmLan", 1598),
          ("dm300-8E1B-ROUTER", 1599),
          ("dm300-8E1-E", 1601),
          ("dm300-8E1-MM", 1602),
          ("dm300-8E1-SM", 1603),
          ("dm300-8E1-B13", 1604),
          ("dm300-8E1-B15", 1605),
          ("dm300-8E1-E1", 1641),
          ("dm300-8E1-V35", 1661),
          ("dm300-8E1-V28", 1667),
          ("dm300-8E1-DmLan", 1698),
          ("dm300-8E1-ROUTER", 1699),
          ("dm991CR-Wan", 1701),
          ("dm991CR-GSHDSL", 1711),
          ("dm991CR-GSHDSL-4F", 1712),
          ("dm991CR-E1", 1731),
          ("dm16E1PacSeq-E3-G703", 2006),
          ("dm16E1PacSeq-E3-MM", 2007),
          ("dm16E1PacSeq-E3-SM", 2008),
          ("dm16E1PacSeq-E3-B13", 2009),
          ("dm16E1PacSeq-E3-B15", 2010),
          ("dm16E1PacSeq-E1", 2041),
          ("dm16E1PacSeq-V35", 2061),
          ("dm16E1PacSeq-10BT", 2081),
          ("dm16E1PacSeq-10BT-HW2", 2082),
          ("dm16E1PacSeq-ROUTER", 2099),
          ("dm4E1PacSeq-E3-G703", 2111),
          ("dm4E1PacSeq-E3-MM", 2112),
          ("dm4E1PacSeq-E3-SM", 2113),
          ("dm4E1PacSeq-E3-B13", 2114),
          ("dm4E1PacSeq-E3-B15", 2115),
          ("dm4E1PacSeq-E1", 2141),
          ("dm4E1PacSeq-V35", 2161),
          ("dm4E1PacSeq-10BT", 2181),
          ("dm4E1PacSeq-10BT-HW2", 2182),
          ("dm4E1PacSeq-ROUTER", 2199),
          ("dm16E1sII-E3-G703", 2301),
          ("dm16E1sII-E3-MM", 2302),
          ("dm16E1sII-E3-SM", 2303),
          ("dm16E1sII-E3-B13", 2304),
          ("dm16E1sII-E3-B15", 2305),
          ("dm16E1sII-E1", 2341),
          ("dm16E1sII-V35", 2361),
          ("dm16E1sII-Bridge", 2381),
          ("dm16E1sII-Bridge2", 2383),
          ("dm16E1sII-G703-E3i", 2391),
          ("dm16E1sII-DmLan", 2398),
          ("dm16E1sII-ROUTER", 2399),
          ("dm4E1sII-E3-G703", 2401),
          ("dm4E1sII-E3-MM", 2402),
          ("dm4E1sII-E3-SM", 2403),
          ("dm4E1sII-E3-B13", 2404),
          ("dm4E1sII-E3-B15", 2405),
          ("dm4E1sII-E1", 2441),
          ("dm4E1sII-V35", 2461),
          ("dm4E1sII-Bridge", 2481),
          ("dm4E1sII-Bridge2", 2483),
          ("dm4E1sII-G703-E3i", 2491),
          ("dm4E1sII-DmLan", 2498),
          ("dm4E1sII-ROUTER", 2499),
          ("dmStm1-Agg-MM", 5001),
          ("dmStm1-Agg-SM", 5002),
          ("dmStm1-Agg-B13", 5003),
          ("dmStm1-Agg-B15", 5004),
          ("dmStm1-Agg-E", 5005),
          ("dmStm1-Trib-E1-TR24E1", 5051),
          ("dmStm1-Trib-ETH-TRETH", 5061),
          ("dmStm1-Cpu-Eth", 5101),
          ("dmStm1-Cpu-V11", 5105),
          ("dmStm1-Cpu-RelayIn", 5110),
          ("dmStm1-Cpu-RelayOut", 5115),
          ("dmStm1-Cpu-Voice", 5120),
          ("dmStm1-Cpu-ClkIn", 5125),
          ("dmStm1-Cpu-ClkInt", 5130),
          ("dmStm1-Cpu-Fan", 5135),
          ("dmStm1-Cpu-PwrSupply", 5140),
          ("dmStm1-Cpu-SlotAgg", 5180),
          ("dmStm1-Cpu-SlotTrib", 5185),
          ("dmStm1-Log-Vc12-Vc11", 5201),
          ("dmStm1-Log-Vc3", 5205),
          ("dmStm1-Log-Vc4", 5210),
          ("dmStm1-Log-Stm1", 5215),
          ("dmStm1-Log-Wan-TR24E1", 5251),
          ("dmStm1-Log-Cpu-SysClk", 5401),
          ("dmStm1-Log-Cpu-ClkHier", 5405),
          ("dmStm1-Log-Cpu-Wan", 5410),
          ("dmStm1-Log-Cpu-Manag", 5415),
          ("dmStm1-Log-Prot-Group", 5420),
          ("dm1801-ETH", 6001),
          ("dm1801-GPRS", 6002),
          ("dm1801-AUX", 6003),
          ("objectNonexistentInModel", 2000000254),
          ("infNotAvailable", 2000000255))
    )


_GenDvInfPortModel_Type.__name__ = "Integer32"
_GenDvInfPortModel_Object = MibTableColumn
genDvInfPortModel = _GenDvInfPortModel_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 12, 1, 5),
    _GenDvInfPortModel_Type()
)
genDvInfPortModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfPortModel.setStatus("mandatory")
_GenDvInfPortFirmVersion_Type = Integer32
_GenDvInfPortFirmVersion_Object = MibTableColumn
genDvInfPortFirmVersion = _GenDvInfPortFirmVersion_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 12, 1, 6),
    _GenDvInfPortFirmVersion_Type()
)
genDvInfPortFirmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfPortFirmVersion.setStatus("mandatory")
_GenDvInfPortHwId_Type = Integer32
_GenDvInfPortHwId_Object = MibTableColumn
genDvInfPortHwId = _GenDvInfPortHwId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 12, 1, 7),
    _GenDvInfPortHwId_Type()
)
genDvInfPortHwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfPortHwId.setStatus("mandatory")
_GenDvInfPortCardMib_Type = ObjectIdentifier
_GenDvInfPortCardMib_Object = MibTableColumn
genDvInfPortCardMib = _GenDvInfPortCardMib_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 12, 1, 8),
    _GenDvInfPortCardMib_Type()
)
genDvInfPortCardMib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfPortCardMib.setStatus("mandatory")
_GenDvInfPortConfigMode_Type = Integer32
_GenDvInfPortConfigMode_Object = MibTableColumn
genDvInfPortConfigMode = _GenDvInfPortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 12, 1, 9),
    _GenDvInfPortConfigMode_Type()
)
genDvInfPortConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfPortConfigMode.setStatus("mandatory")
_GenDvInfAllDevTable_Object = MibTable
genDvInfAllDevTable = _GenDvInfAllDevTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 15)
)
if mibBuilder.loadTexts:
    genDvInfAllDevTable.setStatus("mandatory")
_GenDvInfAllDevEntry_Object = MibTableRow
genDvInfAllDevEntry = _GenDvInfAllDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 15, 1)
)
genDvInfAllDevEntry.setIndexNames(
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvInfAllDevDevNo"),
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvInfAllDevDevLocalId"),
)
if mibBuilder.loadTexts:
    genDvInfAllDevEntry.setStatus("mandatory")
_GenDvInfAllDevDevNo_Type = DmDevIndex
_GenDvInfAllDevDevNo_Object = MibTableColumn
genDvInfAllDevDevNo = _GenDvInfAllDevDevNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 15, 1, 1),
    _GenDvInfAllDevDevNo_Type()
)
genDvInfAllDevDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfAllDevDevNo.setStatus("mandatory")
_GenDvInfAllDevDevLocalId_Type = DmDevLocalIndex
_GenDvInfAllDevDevLocalId_Object = MibTableColumn
genDvInfAllDevDevLocalId = _GenDvInfAllDevDevLocalId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 15, 1, 2),
    _GenDvInfAllDevDevLocalId_Type()
)
genDvInfAllDevDevLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfAllDevDevLocalId.setStatus("mandatory")
_GenDvInfAllDevProduct_Type = ObjectIdentifier
_GenDvInfAllDevProduct_Object = MibTableColumn
genDvInfAllDevProduct = _GenDvInfAllDevProduct_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 15, 1, 3),
    _GenDvInfAllDevProduct_Type()
)
genDvInfAllDevProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfAllDevProduct.setStatus("mandatory")


class _GenDvInfAllDevFirmVersion_Type(Integer32):
    """Custom type genDvInfAllDevFirmVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GenDvInfAllDevFirmVersion_Type.__name__ = "Integer32"
_GenDvInfAllDevFirmVersion_Object = MibTableColumn
genDvInfAllDevFirmVersion = _GenDvInfAllDevFirmVersion_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 15, 1, 4),
    _GenDvInfAllDevFirmVersion_Type()
)
genDvInfAllDevFirmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfAllDevFirmVersion.setStatus("mandatory")
_GenDvInfAllDevSerialNo_Type = DisplayString
_GenDvInfAllDevSerialNo_Object = MibTableColumn
genDvInfAllDevSerialNo = _GenDvInfAllDevSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 15, 1, 5),
    _GenDvInfAllDevSerialNo_Type()
)
genDvInfAllDevSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfAllDevSerialNo.setStatus("mandatory")
_GenDvInfAllDevIdent_Type = Integer32
_GenDvInfAllDevIdent_Object = MibTableColumn
genDvInfAllDevIdent = _GenDvInfAllDevIdent_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 15, 1, 6),
    _GenDvInfAllDevIdent_Type()
)
genDvInfAllDevIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfAllDevIdent.setStatus("mandatory")
_GenDvInfEquStTable_Object = MibTable
genDvInfEquStTable = _GenDvInfEquStTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 20)
)
if mibBuilder.loadTexts:
    genDvInfEquStTable.setStatus("mandatory")
_GenDvInfEquStEntry_Object = MibTableRow
genDvInfEquStEntry = _GenDvInfEquStEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 20, 1)
)
genDvInfEquStEntry.setIndexNames(
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvInfEquStDevNo"),
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvInfEquStDevLocalId"),
)
if mibBuilder.loadTexts:
    genDvInfEquStEntry.setStatus("mandatory")
_GenDvInfEquStDevNo_Type = DmDevIndex
_GenDvInfEquStDevNo_Object = MibTableColumn
genDvInfEquStDevNo = _GenDvInfEquStDevNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 20, 1, 1),
    _GenDvInfEquStDevNo_Type()
)
genDvInfEquStDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfEquStDevNo.setStatus("mandatory")
_GenDvInfEquStDevLocalId_Type = DmDevLocalIndex
_GenDvInfEquStDevLocalId_Object = MibTableColumn
genDvInfEquStDevLocalId = _GenDvInfEquStDevLocalId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 20, 1, 2),
    _GenDvInfEquStDevLocalId_Type()
)
genDvInfEquStDevLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvInfEquStDevLocalId.setStatus("mandatory")


class _GenDvInfEquStStatus_Type(Integer32):
    """Custom type genDvInfEquStStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("licensedOper", 1),
          ("trialOper", 2),
          ("objectNonexistentInModel", 254),
          ("infNotAvailable", 255))
    )


_GenDvInfEquStStatus_Type.__name__ = "Integer32"
_GenDvInfEquStStatus_Object = MibTableColumn
genDvInfEquStStatus = _GenDvInfEquStStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 20, 1, 3),
    _GenDvInfEquStStatus_Type()
)
genDvInfEquStStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genDvInfEquStStatus.setStatus("mandatory")


class _GenDvInfEquStTmRem_Type(Integer32):
    """Custom type genDvInfEquStTmRem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
        ValueRangeConstraint(2000000254, 2000000254),
        ValueRangeConstraint(2000000255, 2000000255),
    )


_GenDvInfEquStTmRem_Type.__name__ = "Integer32"
_GenDvInfEquStTmRem_Object = MibTableColumn
genDvInfEquStTmRem = _GenDvInfEquStTmRem_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 20, 1, 4),
    _GenDvInfEquStTmRem_Type()
)
genDvInfEquStTmRem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genDvInfEquStTmRem.setStatus("mandatory")
_GenDvInfEquStLicInput_Type = DisplayString
_GenDvInfEquStLicInput_Object = MibTableColumn
genDvInfEquStLicInput = _GenDvInfEquStLicInput_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 1, 20, 1, 5),
    _GenDvInfEquStLicInput_Type()
)
genDvInfEquStLicInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genDvInfEquStLicInput.setStatus("mandatory")
_DmGenDvStatus_ObjectIdentity = ObjectIdentity
dmGenDvStatus = _DmGenDvStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2)
)


class _GenDvStSnmpManagementStatus_Type(Integer32):
    """Custom type genDvStSnmpManagementStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fullManagementEnabled", 1),
          ("disabledBecauseRs232Active", 2),
          ("disabledBecauseInterfaceWasDown", 3),
          ("disabledByConfiguration", 4),
          ("disabledByConfigWithRemManagement", 5),
          ("objectNonexistentInModel", 254),
          ("infNotAvailable", 255))
    )


_GenDvStSnmpManagementStatus_Type.__name__ = "Integer32"
_GenDvStSnmpManagementStatus_Object = MibScalar
genDvStSnmpManagementStatus = _GenDvStSnmpManagementStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 1),
    _GenDvStSnmpManagementStatus_Type()
)
genDvStSnmpManagementStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genDvStSnmpManagementStatus.setStatus("mandatory")


class _GenDvStLatchedPossibleNewCfg_Type(Integer32):
    """Custom type genDvStLatchedPossibleNewCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("possibleNewConfig", 2))
    )


_GenDvStLatchedPossibleNewCfg_Type.__name__ = "Integer32"
_GenDvStLatchedPossibleNewCfg_Object = MibScalar
genDvStLatchedPossibleNewCfg = _GenDvStLatchedPossibleNewCfg_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 2),
    _GenDvStLatchedPossibleNewCfg_Type()
)
genDvStLatchedPossibleNewCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genDvStLatchedPossibleNewCfg.setStatus("mandatory")
_GenDvStDeviceTable_Object = MibTable
genDvStDeviceTable = _GenDvStDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 10)
)
if mibBuilder.loadTexts:
    genDvStDeviceTable.setStatus("mandatory")
_GenDvStDeviceEntry_Object = MibTableRow
genDvStDeviceEntry = _GenDvStDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 10, 1)
)
genDvStDeviceEntry.setIndexNames(
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvStDeviceDevNo"),
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvStDeviceDevLocalId"),
)
if mibBuilder.loadTexts:
    genDvStDeviceEntry.setStatus("mandatory")
_GenDvStDeviceDevNo_Type = DmDevIndex
_GenDvStDeviceDevNo_Object = MibTableColumn
genDvStDeviceDevNo = _GenDvStDeviceDevNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 10, 1, 1),
    _GenDvStDeviceDevNo_Type()
)
genDvStDeviceDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvStDeviceDevNo.setStatus("mandatory")
_GenDvStDeviceDevLocalId_Type = DmDevLocalIndex
_GenDvStDeviceDevLocalId_Object = MibTableColumn
genDvStDeviceDevLocalId = _GenDvStDeviceDevLocalId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 10, 1, 2),
    _GenDvStDeviceDevLocalId_Type()
)
genDvStDeviceDevLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvStDeviceDevLocalId.setStatus("mandatory")
_GenDvStDeviceLstHwChangeTmSp_Type = TimeTicks
_GenDvStDeviceLstHwChangeTmSp_Object = MibTableColumn
genDvStDeviceLstHwChangeTmSp = _GenDvStDeviceLstHwChangeTmSp_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 10, 1, 3),
    _GenDvStDeviceLstHwChangeTmSp_Type()
)
genDvStDeviceLstHwChangeTmSp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvStDeviceLstHwChangeTmSp.setStatus("mandatory")
_GenDvStDeviceLstStChangeTmSp_Type = TimeTicks
_GenDvStDeviceLstStChangeTmSp_Object = MibTableColumn
genDvStDeviceLstStChangeTmSp = _GenDvStDeviceLstStChangeTmSp_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 10, 1, 4),
    _GenDvStDeviceLstStChangeTmSp_Type()
)
genDvStDeviceLstStChangeTmSp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvStDeviceLstStChangeTmSp.setStatus("mandatory")
_GenDvStDeviceResets_Type = Counter32
_GenDvStDeviceResets_Object = MibTableColumn
genDvStDeviceResets = _GenDvStDeviceResets_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 10, 1, 5),
    _GenDvStDeviceResets_Type()
)
genDvStDeviceResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvStDeviceResets.setStatus("mandatory")
_GenDvStDeviceLstCfgChange_Type = Counter32
_GenDvStDeviceLstCfgChange_Object = MibTableColumn
genDvStDeviceLstCfgChange = _GenDvStDeviceLstCfgChange_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 10, 1, 6),
    _GenDvStDeviceLstCfgChange_Type()
)
genDvStDeviceLstCfgChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvStDeviceLstCfgChange.setStatus("mandatory")
_GenDvStDeviceNmsVersion_Type = Counter32
_GenDvStDeviceNmsVersion_Object = MibTableColumn
genDvStDeviceNmsVersion = _GenDvStDeviceNmsVersion_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 10, 1, 7),
    _GenDvStDeviceNmsVersion_Type()
)
genDvStDeviceNmsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvStDeviceNmsVersion.setStatus("mandatory")


class _GenDvStDeviceResetStatus_Type(Integer32):
    """Custom type genDvStDeviceResetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notResetingAgent", 1),
          ("resetAgent", 2),
          ("objectNonexistentInModel", 254),
          ("infNotAvailable", 255))
    )


_GenDvStDeviceResetStatus_Type.__name__ = "Integer32"
_GenDvStDeviceResetStatus_Object = MibTableColumn
genDvStDeviceResetStatus = _GenDvStDeviceResetStatus_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 10, 1, 10),
    _GenDvStDeviceResetStatus_Type()
)
genDvStDeviceResetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genDvStDeviceResetStatus.setStatus("mandatory")
_GenDvEquipTmTable_Object = MibTable
genDvEquipTmTable = _GenDvEquipTmTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 13)
)
if mibBuilder.loadTexts:
    genDvEquipTmTable.setStatus("mandatory")
_GenDvEquipTmEntry_Object = MibTableRow
genDvEquipTmEntry = _GenDvEquipTmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 13, 1)
)
genDvEquipTmEntry.setIndexNames(
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvEquipTmDevNo"),
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvEquipTmDevLocalId"),
)
if mibBuilder.loadTexts:
    genDvEquipTmEntry.setStatus("mandatory")
_GenDvEquipTmDevNo_Type = DmDevIndex
_GenDvEquipTmDevNo_Object = MibTableColumn
genDvEquipTmDevNo = _GenDvEquipTmDevNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 13, 1, 1),
    _GenDvEquipTmDevNo_Type()
)
genDvEquipTmDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvEquipTmDevNo.setStatus("mandatory")
_GenDvEquipTmDevLocalId_Type = DmDevLocalIndex
_GenDvEquipTmDevLocalId_Object = MibTableColumn
genDvEquipTmDevLocalId = _GenDvEquipTmDevLocalId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 13, 1, 2),
    _GenDvEquipTmDevLocalId_Type()
)
genDvEquipTmDevLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvEquipTmDevLocalId.setStatus("mandatory")
_GenDvEquipTmUtc_Type = DmUnsigned
_GenDvEquipTmUtc_Object = MibTableColumn
genDvEquipTmUtc = _GenDvEquipTmUtc_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 13, 1, 3),
    _GenDvEquipTmUtc_Type()
)
genDvEquipTmUtc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvEquipTmUtc.setStatus("mandatory")
_GenDvEquipTmTimezone_Type = Integer32
_GenDvEquipTmTimezone_Object = MibTableColumn
genDvEquipTmTimezone = _GenDvEquipTmTimezone_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 13, 1, 4),
    _GenDvEquipTmTimezone_Type()
)
genDvEquipTmTimezone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvEquipTmTimezone.setStatus("mandatory")
_GenDvEquipTmUpTm_Type = TimeTicks
_GenDvEquipTmUpTm_Object = MibTableColumn
genDvEquipTmUpTm = _GenDvEquipTmUpTm_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 13, 1, 5),
    _GenDvEquipTmUpTm_Type()
)
genDvEquipTmUpTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvEquipTmUpTm.setStatus("mandatory")
_GenDvStActTable_Object = MibTable
genDvStActTable = _GenDvStActTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 15)
)
if mibBuilder.loadTexts:
    genDvStActTable.setStatus("mandatory")
_GenDvStActEntry_Object = MibTableRow
genDvStActEntry = _GenDvStActEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 15, 1)
)
genDvStActEntry.setIndexNames(
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvStActDevNo"),
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvStActDevLocalId"),
)
if mibBuilder.loadTexts:
    genDvStActEntry.setStatus("mandatory")
_GenDvStActDevNo_Type = DmDevIndex
_GenDvStActDevNo_Object = MibTableColumn
genDvStActDevNo = _GenDvStActDevNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 15, 1, 1),
    _GenDvStActDevNo_Type()
)
genDvStActDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvStActDevNo.setStatus("mandatory")
_GenDvStActDevLocalId_Type = DmDevLocalIndex
_GenDvStActDevLocalId_Object = MibTableColumn
genDvStActDevLocalId = _GenDvStActDevLocalId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 15, 1, 2),
    _GenDvStActDevLocalId_Type()
)
genDvStActDevLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvStActDevLocalId.setStatus("mandatory")
_GenDvStActUpTm_Type = TimeTicks
_GenDvStActUpTm_Object = MibTableColumn
genDvStActUpTm = _GenDvStActUpTm_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 15, 1, 3),
    _GenDvStActUpTm_Type()
)
genDvStActUpTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvStActUpTm.setStatus("mandatory")
_GenDvStActResets_Type = Counter32
_GenDvStActResets_Object = MibTableColumn
genDvStActResets = _GenDvStActResets_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 15, 1, 4),
    _GenDvStActResets_Type()
)
genDvStActResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvStActResets.setStatus("mandatory")
_GenDvStPhSlotTable_Object = MibTable
genDvStPhSlotTable = _GenDvStPhSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 17)
)
if mibBuilder.loadTexts:
    genDvStPhSlotTable.setStatus("mandatory")
_GenDvStPhSlotEntry_Object = MibTableRow
genDvStPhSlotEntry = _GenDvStPhSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 17, 1)
)
genDvStPhSlotEntry.setIndexNames(
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvStPhSlotDevNo"),
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvStPhSlotDevLocalId"),
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvStPhSlotSlotNo"),
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvStPhSlotPortNo"),
)
if mibBuilder.loadTexts:
    genDvStPhSlotEntry.setStatus("mandatory")
_GenDvStPhSlotDevNo_Type = DmDevIndex
_GenDvStPhSlotDevNo_Object = MibTableColumn
genDvStPhSlotDevNo = _GenDvStPhSlotDevNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 17, 1, 1),
    _GenDvStPhSlotDevNo_Type()
)
genDvStPhSlotDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvStPhSlotDevNo.setStatus("mandatory")
_GenDvStPhSlotDevLocalId_Type = DmDevLocalIndex
_GenDvStPhSlotDevLocalId_Object = MibTableColumn
genDvStPhSlotDevLocalId = _GenDvStPhSlotDevLocalId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 17, 1, 2),
    _GenDvStPhSlotDevLocalId_Type()
)
genDvStPhSlotDevLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvStPhSlotDevLocalId.setStatus("mandatory")
_GenDvStPhSlotSlotNo_Type = DmSlotIndex
_GenDvStPhSlotSlotNo_Object = MibTableColumn
genDvStPhSlotSlotNo = _GenDvStPhSlotSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 17, 1, 3),
    _GenDvStPhSlotSlotNo_Type()
)
genDvStPhSlotSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvStPhSlotSlotNo.setStatus("mandatory")
_GenDvStPhSlotPortNo_Type = DmPortIndex
_GenDvStPhSlotPortNo_Object = MibTableColumn
genDvStPhSlotPortNo = _GenDvStPhSlotPortNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 17, 1, 4),
    _GenDvStPhSlotPortNo_Type()
)
genDvStPhSlotPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvStPhSlotPortNo.setStatus("mandatory")


class _GenDvStPhSlotPresence_Type(Integer32):
    """Custom type genDvStPhSlotPresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("present", 2),
          ("objectNonexistentInModel", 254),
          ("infNotAvailable", 255))
    )


_GenDvStPhSlotPresence_Type.__name__ = "Integer32"
_GenDvStPhSlotPresence_Object = MibTableColumn
genDvStPhSlotPresence = _GenDvStPhSlotPresence_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 17, 1, 6),
    _GenDvStPhSlotPresence_Type()
)
genDvStPhSlotPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvStPhSlotPresence.setStatus("mandatory")


class _GenDvStPhSlotStFail_Type(Integer32):
    """Custom type genDvStPhSlotStFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("failure", 2),
          ("objectNonexistentInModel", 254),
          ("infNotAvailable", 255))
    )


_GenDvStPhSlotStFail_Type.__name__ = "Integer32"
_GenDvStPhSlotStFail_Object = MibTableColumn
genDvStPhSlotStFail = _GenDvStPhSlotStFail_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 17, 1, 7),
    _GenDvStPhSlotStFail_Type()
)
genDvStPhSlotStFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvStPhSlotStFail.setStatus("mandatory")
_GenDvStPhSlotOperTm_Type = Counter32
_GenDvStPhSlotOperTm_Object = MibTableColumn
genDvStPhSlotOperTm = _GenDvStPhSlotOperTm_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 17, 1, 8),
    _GenDvStPhSlotOperTm_Type()
)
genDvStPhSlotOperTm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvStPhSlotOperTm.setStatus("mandatory")


class _GenDvStPhSlotOperSt_Type(Integer32):
    """Custom type genDvStPhSlotOperSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("prevMaintReq", 1),
          ("prevMaintNotReq", 2),
          ("objectNonexistentInModel", 254),
          ("infNotAvailable", 255))
    )


_GenDvStPhSlotOperSt_Type.__name__ = "Integer32"
_GenDvStPhSlotOperSt_Object = MibTableColumn
genDvStPhSlotOperSt = _GenDvStPhSlotOperSt_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 17, 1, 9),
    _GenDvStPhSlotOperSt_Type()
)
genDvStPhSlotOperSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvStPhSlotOperSt.setStatus("mandatory")
_GenDvStPhSlotResets_Type = Counter32
_GenDvStPhSlotResets_Object = MibTableColumn
genDvStPhSlotResets = _GenDvStPhSlotResets_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 2, 17, 1, 10),
    _GenDvStPhSlotResets_Type()
)
genDvStPhSlotResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvStPhSlotResets.setStatus("mandatory")
_DmGenDvConfig_ObjectIdentity = ObjectIdentity
dmGenDvConfig = _DmGenDvConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 3)
)
_GenDvCfgMngDownItfTm_Type = Integer32
_GenDvCfgMngDownItfTm_Object = MibScalar
genDvCfgMngDownItfTm = _GenDvCfgMngDownItfTm_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 3, 1),
    _GenDvCfgMngDownItfTm_Type()
)
genDvCfgMngDownItfTm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genDvCfgMngDownItfTm.setStatus("mandatory")
_GenDvCfgMngUpItfTm_Type = Integer32
_GenDvCfgMngUpItfTm_Object = MibScalar
genDvCfgMngUpItfTm = _GenDvCfgMngUpItfTm_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 3, 2),
    _GenDvCfgMngUpItfTm_Type()
)
genDvCfgMngUpItfTm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genDvCfgMngUpItfTm.setStatus("mandatory")
_DmGenDvAlarms_ObjectIdentity = ObjectIdentity
dmGenDvAlarms = _DmGenDvAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 5)
)
_GenDvAlDeviceCfgTable_Object = MibTable
genDvAlDeviceCfgTable = _GenDvAlDeviceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 5, 10)
)
if mibBuilder.loadTexts:
    genDvAlDeviceCfgTable.setStatus("mandatory")
_GenDvAlDeviceCfgEntry_Object = MibTableRow
genDvAlDeviceCfgEntry = _GenDvAlDeviceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 5, 10, 1)
)
genDvAlDeviceCfgEntry.setIndexNames(
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvAlDeviceCfgDevNo"),
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvAlDeviceCfgDevLocalId"),
)
if mibBuilder.loadTexts:
    genDvAlDeviceCfgEntry.setStatus("mandatory")
_GenDvAlDeviceCfgDevNo_Type = DmDevIndex
_GenDvAlDeviceCfgDevNo_Object = MibTableColumn
genDvAlDeviceCfgDevNo = _GenDvAlDeviceCfgDevNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 5, 10, 1, 1),
    _GenDvAlDeviceCfgDevNo_Type()
)
genDvAlDeviceCfgDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvAlDeviceCfgDevNo.setStatus("mandatory")
_GenDvAlDeviceCfgDevLocalId_Type = DmDevLocalIndex
_GenDvAlDeviceCfgDevLocalId_Object = MibTableColumn
genDvAlDeviceCfgDevLocalId = _GenDvAlDeviceCfgDevLocalId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 5, 10, 1, 2),
    _GenDvAlDeviceCfgDevLocalId_Type()
)
genDvAlDeviceCfgDevLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvAlDeviceCfgDevLocalId.setStatus("mandatory")


class _GenDvAlDeviceCfgTrapSt_Type(Integer32):
    """Custom type genDvAlDeviceCfgTrapSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("objectNonexistentInModel", 254),
          ("infNotAvailable", 255))
    )


_GenDvAlDeviceCfgTrapSt_Type.__name__ = "Integer32"
_GenDvAlDeviceCfgTrapSt_Object = MibTableColumn
genDvAlDeviceCfgTrapSt = _GenDvAlDeviceCfgTrapSt_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 5, 10, 1, 3),
    _GenDvAlDeviceCfgTrapSt_Type()
)
genDvAlDeviceCfgTrapSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genDvAlDeviceCfgTrapSt.setStatus("mandatory")
_GenDvAlDevTrapCfgTable_Object = MibTable
genDvAlDevTrapCfgTable = _GenDvAlDevTrapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 5, 11)
)
if mibBuilder.loadTexts:
    genDvAlDevTrapCfgTable.setStatus("mandatory")
_GenDvAlDevTrapCfgEntry_Object = MibTableRow
genDvAlDevTrapCfgEntry = _GenDvAlDevTrapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 5, 11, 1)
)
genDvAlDevTrapCfgEntry.setIndexNames(
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvAlDevTrapCfgDevNo"),
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvAlDevTrapCfgDevLocalId"),
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvAlDevTrapCfgTrapId"),
)
if mibBuilder.loadTexts:
    genDvAlDevTrapCfgEntry.setStatus("mandatory")
_GenDvAlDevTrapCfgDevNo_Type = DmDevIndex
_GenDvAlDevTrapCfgDevNo_Object = MibTableColumn
genDvAlDevTrapCfgDevNo = _GenDvAlDevTrapCfgDevNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 5, 11, 1, 1),
    _GenDvAlDevTrapCfgDevNo_Type()
)
genDvAlDevTrapCfgDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvAlDevTrapCfgDevNo.setStatus("mandatory")
_GenDvAlDevTrapCfgDevLocalId_Type = DmDevLocalIndex
_GenDvAlDevTrapCfgDevLocalId_Object = MibTableColumn
genDvAlDevTrapCfgDevLocalId = _GenDvAlDevTrapCfgDevLocalId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 5, 11, 1, 2),
    _GenDvAlDevTrapCfgDevLocalId_Type()
)
genDvAlDevTrapCfgDevLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvAlDevTrapCfgDevLocalId.setStatus("mandatory")
_GenDvAlDevTrapCfgTrapId_Type = DmTrapIndex
_GenDvAlDevTrapCfgTrapId_Object = MibTableColumn
genDvAlDevTrapCfgTrapId = _GenDvAlDevTrapCfgTrapId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 5, 11, 1, 3),
    _GenDvAlDevTrapCfgTrapId_Type()
)
genDvAlDevTrapCfgTrapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvAlDevTrapCfgTrapId.setStatus("mandatory")


class _GenDvAlDevTrapCfgSt_Type(Integer32):
    """Custom type genDvAlDevTrapCfgSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("masked", 3),
          ("objectNonexistentInModel", 254),
          ("infNotAvailable", 255))
    )


_GenDvAlDevTrapCfgSt_Type.__name__ = "Integer32"
_GenDvAlDevTrapCfgSt_Object = MibTableColumn
genDvAlDevTrapCfgSt = _GenDvAlDevTrapCfgSt_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 5, 11, 1, 4),
    _GenDvAlDevTrapCfgSt_Type()
)
genDvAlDevTrapCfgSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genDvAlDevTrapCfgSt.setStatus("mandatory")
_GenDvAlPortCfgTable_Object = MibTable
genDvAlPortCfgTable = _GenDvAlPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 5, 13)
)
if mibBuilder.loadTexts:
    genDvAlPortCfgTable.setStatus("mandatory")
_GenDvAlPortCfgEntry_Object = MibTableRow
genDvAlPortCfgEntry = _GenDvAlPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 5, 13, 1)
)
genDvAlPortCfgEntry.setIndexNames(
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvAlPortCfgDevNo"),
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvAlPortCfgDevLocalId"),
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvAlPortCfgSlotNo"),
    (0, "DATACOM-GENERIC-DEVICE-MIB", "genDvAlPortCfgPortNo"),
)
if mibBuilder.loadTexts:
    genDvAlPortCfgEntry.setStatus("mandatory")
_GenDvAlPortCfgDevNo_Type = DmDevIndex
_GenDvAlPortCfgDevNo_Object = MibTableColumn
genDvAlPortCfgDevNo = _GenDvAlPortCfgDevNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 5, 13, 1, 1),
    _GenDvAlPortCfgDevNo_Type()
)
genDvAlPortCfgDevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvAlPortCfgDevNo.setStatus("mandatory")
_GenDvAlPortCfgDevLocalId_Type = DmDevLocalIndex
_GenDvAlPortCfgDevLocalId_Object = MibTableColumn
genDvAlPortCfgDevLocalId = _GenDvAlPortCfgDevLocalId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 5, 13, 1, 2),
    _GenDvAlPortCfgDevLocalId_Type()
)
genDvAlPortCfgDevLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvAlPortCfgDevLocalId.setStatus("mandatory")
_GenDvAlPortCfgSlotNo_Type = DmSlotIndex
_GenDvAlPortCfgSlotNo_Object = MibTableColumn
genDvAlPortCfgSlotNo = _GenDvAlPortCfgSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 5, 13, 1, 3),
    _GenDvAlPortCfgSlotNo_Type()
)
genDvAlPortCfgSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvAlPortCfgSlotNo.setStatus("mandatory")
_GenDvAlPortCfgPortNo_Type = DmPortIndex
_GenDvAlPortCfgPortNo_Object = MibTableColumn
genDvAlPortCfgPortNo = _GenDvAlPortCfgPortNo_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 5, 13, 1, 4),
    _GenDvAlPortCfgPortNo_Type()
)
genDvAlPortCfgPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genDvAlPortCfgPortNo.setStatus("mandatory")


class _GenDvAlPortCfgTrapSt_Type(Integer32):
    """Custom type genDvAlPortCfgTrapSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("masked", 3),
          ("objectNonexistentInModel", 254),
          ("infNotAvailable", 255))
    )


_GenDvAlPortCfgTrapSt_Type.__name__ = "Integer32"
_GenDvAlPortCfgTrapSt_Object = MibTableColumn
genDvAlPortCfgTrapSt = _GenDvAlPortCfgTrapSt_Object(
    (1, 3, 6, 1, 4, 1, 3709, 2, 3, 5, 13, 1, 5),
    _GenDvAlPortCfgTrapSt_Type()
)
genDvAlPortCfgTrapSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genDvAlPortCfgTrapSt.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DATACOM-GENERIC-DEVICE-MIB",
    **{"DisplayString": DisplayString,
       "DmUnsigned": DmUnsigned,
       "DmDevIndex": DmDevIndex,
       "DmDevLocalIndex": DmDevLocalIndex,
       "DmSlotIndex": DmSlotIndex,
       "DmPortIndex": DmPortIndex,
       "DmTrapIndex": DmTrapIndex,
       "datacomGenericDeviceMIBModule": datacomGenericDeviceMIBModule,
       "dmGenericDeviceMIB": dmGenericDeviceMIB,
       "dmGenDvInf": dmGenDvInf,
       "genDvInfMibVersion": genDvInfMibVersion,
       "genDvInfDeviceTable": genDvInfDeviceTable,
       "genDvInfDeviceEntry": genDvInfDeviceEntry,
       "genDvInfDeviceDevNo": genDvInfDeviceDevNo,
       "genDvInfDeviceDevLocalId": genDvInfDeviceDevLocalId,
       "genDvInfDeviceProduct": genDvInfDeviceProduct,
       "genDvInfDeviceFirmVersion": genDvInfDeviceFirmVersion,
       "genDvInfDeviceBootVersion": genDvInfDeviceBootVersion,
       "genDvInfDeviceHWVersion": genDvInfDeviceHWVersion,
       "genDvInfDeviceSerialNo": genDvInfDeviceSerialNo,
       "genDvInfDeviceIdent": genDvInfDeviceIdent,
       "genDvInfDeviceFirmReleaseDate": genDvInfDeviceFirmReleaseDate,
       "genDvInfDeviceE2PROMversion": genDvInfDeviceE2PROMversion,
       "genDvInfDeviceFirmVersionString": genDvInfDeviceFirmVersionString,
       "genDvInfDeviceVendor": genDvInfDeviceVendor,
       "genDvInfPortTable": genDvInfPortTable,
       "genDvInfPortEntry": genDvInfPortEntry,
       "genDvInfPortDevNo": genDvInfPortDevNo,
       "genDvInfPortDevLocalId": genDvInfPortDevLocalId,
       "genDvInfPortSlotNo": genDvInfPortSlotNo,
       "genDvInfPortPortNo": genDvInfPortPortNo,
       "genDvInfPortModel": genDvInfPortModel,
       "genDvInfPortFirmVersion": genDvInfPortFirmVersion,
       "genDvInfPortHwId": genDvInfPortHwId,
       "genDvInfPortCardMib": genDvInfPortCardMib,
       "genDvInfPortConfigMode": genDvInfPortConfigMode,
       "genDvInfAllDevTable": genDvInfAllDevTable,
       "genDvInfAllDevEntry": genDvInfAllDevEntry,
       "genDvInfAllDevDevNo": genDvInfAllDevDevNo,
       "genDvInfAllDevDevLocalId": genDvInfAllDevDevLocalId,
       "genDvInfAllDevProduct": genDvInfAllDevProduct,
       "genDvInfAllDevFirmVersion": genDvInfAllDevFirmVersion,
       "genDvInfAllDevSerialNo": genDvInfAllDevSerialNo,
       "genDvInfAllDevIdent": genDvInfAllDevIdent,
       "genDvInfEquStTable": genDvInfEquStTable,
       "genDvInfEquStEntry": genDvInfEquStEntry,
       "genDvInfEquStDevNo": genDvInfEquStDevNo,
       "genDvInfEquStDevLocalId": genDvInfEquStDevLocalId,
       "genDvInfEquStStatus": genDvInfEquStStatus,
       "genDvInfEquStTmRem": genDvInfEquStTmRem,
       "genDvInfEquStLicInput": genDvInfEquStLicInput,
       "dmGenDvStatus": dmGenDvStatus,
       "genDvStSnmpManagementStatus": genDvStSnmpManagementStatus,
       "genDvStLatchedPossibleNewCfg": genDvStLatchedPossibleNewCfg,
       "genDvStDeviceTable": genDvStDeviceTable,
       "genDvStDeviceEntry": genDvStDeviceEntry,
       "genDvStDeviceDevNo": genDvStDeviceDevNo,
       "genDvStDeviceDevLocalId": genDvStDeviceDevLocalId,
       "genDvStDeviceLstHwChangeTmSp": genDvStDeviceLstHwChangeTmSp,
       "genDvStDeviceLstStChangeTmSp": genDvStDeviceLstStChangeTmSp,
       "genDvStDeviceResets": genDvStDeviceResets,
       "genDvStDeviceLstCfgChange": genDvStDeviceLstCfgChange,
       "genDvStDeviceNmsVersion": genDvStDeviceNmsVersion,
       "genDvStDeviceResetStatus": genDvStDeviceResetStatus,
       "genDvEquipTmTable": genDvEquipTmTable,
       "genDvEquipTmEntry": genDvEquipTmEntry,
       "genDvEquipTmDevNo": genDvEquipTmDevNo,
       "genDvEquipTmDevLocalId": genDvEquipTmDevLocalId,
       "genDvEquipTmUtc": genDvEquipTmUtc,
       "genDvEquipTmTimezone": genDvEquipTmTimezone,
       "genDvEquipTmUpTm": genDvEquipTmUpTm,
       "genDvStActTable": genDvStActTable,
       "genDvStActEntry": genDvStActEntry,
       "genDvStActDevNo": genDvStActDevNo,
       "genDvStActDevLocalId": genDvStActDevLocalId,
       "genDvStActUpTm": genDvStActUpTm,
       "genDvStActResets": genDvStActResets,
       "genDvStPhSlotTable": genDvStPhSlotTable,
       "genDvStPhSlotEntry": genDvStPhSlotEntry,
       "genDvStPhSlotDevNo": genDvStPhSlotDevNo,
       "genDvStPhSlotDevLocalId": genDvStPhSlotDevLocalId,
       "genDvStPhSlotSlotNo": genDvStPhSlotSlotNo,
       "genDvStPhSlotPortNo": genDvStPhSlotPortNo,
       "genDvStPhSlotPresence": genDvStPhSlotPresence,
       "genDvStPhSlotStFail": genDvStPhSlotStFail,
       "genDvStPhSlotOperTm": genDvStPhSlotOperTm,
       "genDvStPhSlotOperSt": genDvStPhSlotOperSt,
       "genDvStPhSlotResets": genDvStPhSlotResets,
       "dmGenDvConfig": dmGenDvConfig,
       "genDvCfgMngDownItfTm": genDvCfgMngDownItfTm,
       "genDvCfgMngUpItfTm": genDvCfgMngUpItfTm,
       "dmGenDvAlarms": dmGenDvAlarms,
       "genDvAlDeviceCfgTable": genDvAlDeviceCfgTable,
       "genDvAlDeviceCfgEntry": genDvAlDeviceCfgEntry,
       "genDvAlDeviceCfgDevNo": genDvAlDeviceCfgDevNo,
       "genDvAlDeviceCfgDevLocalId": genDvAlDeviceCfgDevLocalId,
       "genDvAlDeviceCfgTrapSt": genDvAlDeviceCfgTrapSt,
       "genDvAlDevTrapCfgTable": genDvAlDevTrapCfgTable,
       "genDvAlDevTrapCfgEntry": genDvAlDevTrapCfgEntry,
       "genDvAlDevTrapCfgDevNo": genDvAlDevTrapCfgDevNo,
       "genDvAlDevTrapCfgDevLocalId": genDvAlDevTrapCfgDevLocalId,
       "genDvAlDevTrapCfgTrapId": genDvAlDevTrapCfgTrapId,
       "genDvAlDevTrapCfgSt": genDvAlDevTrapCfgSt,
       "genDvAlPortCfgTable": genDvAlPortCfgTable,
       "genDvAlPortCfgEntry": genDvAlPortCfgEntry,
       "genDvAlPortCfgDevNo": genDvAlPortCfgDevNo,
       "genDvAlPortCfgDevLocalId": genDvAlPortCfgDevLocalId,
       "genDvAlPortCfgSlotNo": genDvAlPortCfgSlotNo,
       "genDvAlPortCfgPortNo": genDvAlPortCfgPortNo,
       "genDvAlPortCfgTrapSt": genDvAlPortCfgTrapSt}
)
