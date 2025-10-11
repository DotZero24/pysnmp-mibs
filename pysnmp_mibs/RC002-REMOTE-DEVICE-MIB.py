# SNMP MIB module (RC002-REMOTE-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RC002-REMOTE-DEVICE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:02 2025
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

(rcftChassisIndex,
 rcftMibObjects,
 rcftSlotIndex) = mibBuilder.importSymbols(
    "RAISECOM-RCFT-MIB",
    "rcftChassisIndex",
    "rcftMibObjects",
    "rcftSlotIndex")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

rcftRemoteDeviceMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6)
)
if mibBuilder.loadTexts:
    rcftRemoteDeviceMib.setRevisions(
        ("1905-07-04 00:00",
         "1909-01-09 00:00",
         "1909-01-21 00:00",
         "1909-02-09 00:00",
         "1909-03-17 00:00",
         "1909-03-24 00:00",
         "1909-04-15 00:00",
         "1909-05-14 00:00",
         "1909-05-15 00:00",
         "1909-05-19 00:00",
         "1909-05-26 00:00",
         "1909-05-26 00:00",
         "1909-05-27 16:00",
         "1909-06-09 16:00",
         "1909-07-02 16:00",
         "1909-07-17 16:00",
         "1909-08-19 00:00",
         "1909-08-21 16:00",
         "1909-09-02 10:00",
         "1909-09-08 14:30",
         "1909-09-09 11:30",
         "1909-09-09 16:30",
         "1909-09-18 00:00",
         "1909-09-27 00:00",
         "1909-10-30 10:06",
         "1909-12-21 00:00",
         "1910-03-03 00:00",
         "1910-03-04 00:00",
         "1910-03-10 00:00",
         "1910-09-29 09:50",
         "1910-10-22 16:57",
         "1910-11-15 00:00",
         "1911-12-19 17:25",
         "1912-03-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcftRemoteDeviceSystemMIB_ObjectIdentity = ObjectIdentity
rcftRemoteDeviceSystemMIB = _RcftRemoteDeviceSystemMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1)
)
_RcftRemoteDeviceSysObjects_ObjectIdentity = ObjectIdentity
rcftRemoteDeviceSysObjects = _RcftRemoteDeviceSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1)
)
_RcftRemoteDeviceSysTable_Object = MibTable
rcftRemoteDeviceSysTable = _RcftRemoteDeviceSysTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteDeviceSysTable.setStatus("current")
_RcftRemoteDeviceSysEntry_Object = MibTableRow
rcftRemoteDeviceSysEntry = _RcftRemoteDeviceSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1)
)
rcftRemoteDeviceSysEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteDeviceSysEntry.setStatus("current")
_RcftRemoteDeviceIndex_Type = Integer32
_RcftRemoteDeviceIndex_Object = MibTableColumn
rcftRemoteDeviceIndex = _RcftRemoteDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 1),
    _RcftRemoteDeviceIndex_Type()
)
rcftRemoteDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDeviceIndex.setStatus("current")


class _RcftRemoteDeviceExist_Type(Integer32):
    """Custom type rcftRemoteDeviceExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("noexist", 2))
    )


_RcftRemoteDeviceExist_Type.__name__ = "Integer32"
_RcftRemoteDeviceExist_Object = MibTableColumn
rcftRemoteDeviceExist = _RcftRemoteDeviceExist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 2),
    _RcftRemoteDeviceExist_Type()
)
rcftRemoteDeviceExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDeviceExist.setStatus("current")


class _RcftRemoteDeviceType_Type(Integer32):
    """Custom type rcftRemoteDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5394,
              20001,
              20002,
              20003,
              20004,
              20005,
              20006,
              20007,
              20008,
              20009,
              20010,
              20011,
              20012,
              20013,
              20014,
              20015,
              20016,
              20017,
              20018,
              20019,
              20020,
              20021,
              20022,
              20023,
              20024,
              20025,
              20026,
              20027,
              20028,
              20029,
              20030,
              20031,
              20032,
              20033,
              20034,
              20035,
              20036,
              20037,
              20038,
              20039,
              20040,
              20041,
              20042,
              20043,
              20044,
              20045,
              20046,
              20047,
              20048,
              20049,
              20050,
              20051,
              20052,
              20053,
              20054,
              20055,
              20056,
              20057,
              20058,
              20059,
              20060,
              20061,
              20062,
              20063,
              20064,
              20065,
              20066,
              20067,
              20068,
              20069,
              20070,
              20073,
              20074,
              20075,
              20076,
              20077,
              20078,
              20079,
              21001,
              21002,
              21003,
              21004,
              21005,
              21006,
              21007,
              22050,
              22051,
              22052,
              22053,
              22054,
              22055,
              22056,
              22057,
              22058,
              22059,
              22060,
              22061,
              22062,
              22063,
              22064,
              22065,
              22066,
              22070,
              22071,
              22072,
              22073,
              22074,
              22075,
              22076,
              22077,
              22078,
              22079,
              22081,
              22082,
              22083,
              22084,
              25004,
              25005,
              25006,
              25007,
              26008,
              26011,
              26099,
              26100,
              45313,
              45314,
              45318,
              62128,
              62471,
              62514,
              62518,
              62521,
              62526,
              62529,
              62533,
              62536,
              62540,
              62543,
              62546,
              62550,
              62553,
              62557,
              62560,
              62563,
              62567,
              62571,
              62575,
              62578,
              62582,
              62589,
              62592,
              62595,
              62598,
              62603,
              62606,
              62607,
              62611,
              62615,
              62616,
              62618,
              64769,
              64770,
              64771,
              206915,
              206918,
              206919)
        )
    )
    namedValues = NamedValues(
        *(("rcftTypeRCMS2802-240GE-REV-A-REMOTE", 5394),
          ("rcftTypeRC501-FE-REV-C", 20001),
          ("rcftTypeRC601-FE-REV-C", 20002),
          ("rcftTypeRC511-FE-REV-A", 20003),
          ("rcftTypeRC952-FEE1-REV-A", 20004),
          ("rcftTypeRC952-FXE1-REV-A", 20005),
          ("rcftTypeRC601-FE-REV-E", 20006),
          ("rcftTypeRC511-4FE-REV-A", 20007),
          ("rcftTypeRC511-FE-C-REV-A", 20008),
          ("rcftTypeRC951-FEE1-REV-A", 20009),
          ("rcftTypeRC513-FE-REV-A", 20010),
          ("rcftTypeRC513-FE-C-REV-A", 20011),
          ("rcftTypeRC954-FE4E1-REV-A", 20012),
          ("rcftTypeRC954-FX4E1-REV-A", 20013),
          ("rcftTypeRC953-FE4E1-REV-A", 20014),
          ("rcftTypeRC953-FX4E1-REV-A", 20015),
          ("rcftTypeRC953-FE8E1-REV-A", 20016),
          ("rcftTypeRC953-FX8E1-REV-A", 20017),
          ("rcftTypeRC953-FE8E1-BL-REV-A", 20018),
          ("rcftTypeRC953-FX8E1-BL-REV-A", 20019),
          ("rcftTypeRC532-FE-REV-A", 20020),
          ("rcftTypeRC531-FE-REV-A", 20021),
          ("rcftTypeRC532-2FE-REV-A", 20022),
          ("rcftTypeRC1102-E1-SLAVE-REV-B1", 20023),
          ("rcftTypeRC1102-E1-SLAVE-BL-REV-A1", 20024),
          ("rcftTypeRC954-2FE4E1-BL-REV-A", 20025),
          ("rcftTypeRC954-FE4E1-BL-REV-A", 20026),
          ("rcftTypeRC954-FX4E1-BL-REV-A", 20027),
          ("rcftTypeRC954-2FE8E1-BL-REV-A", 20028),
          ("rcftTypeRC1102-V35-REV-A1", 20029),
          ("rcftTypeRC1102-V35-REV-B", 20030),
          ("rcftTypeRC602-GEF-REV-B", 20031),
          ("rcftTypeRC802-DS3E3-REV-A", 20032),
          ("rcftTypeE-SUBM-FE4E1-A", 20033),
          ("rcftTypeRC954-FE8E1-REV-A", 20034),
          ("rcftTypeRC1102-E1-REV-B2", 20035),
          ("rcftTypeRC1102-E1-BL-REV-A2", 20036),
          ("rcftTypeRC952-FE-DS3E3-REV-A-SLAVE", 20037),
          ("rcftTypeRC802-DS1-REV-A-SLAVE", 20038),
          ("rcftTypeRC952-FE-DS1-REV-A-SLAVE", 20039),
          ("rcftTypeRC952-FE-DS3E3-F-REV-A-SLAVE", 20040),
          ("rcftTypeRC852-30-SLAVE-REV-B", 20041),
          ("rcftTypeRC951-4FEE1-REV-A", 20042),
          ("rcftTypeRC512-FE-REV-A-SLAVE-M", 20043),
          ("rcftTypeRC512-FE-REV-A-SLAVE-S1", 20044),
          ("rcftTypeRC512-FE-REV-A-SLAVE-S2", 20045),
          ("rcftTypeRC512-FE-REV-A-SLAVE-S3", 20046),
          ("rcftTypeRC512-FE-REV-A-SLAVE-noOptical", 20047),
          ("rcftTypeRC512-FE-REV-A-SLAVE-SS13", 20048),
          ("rcftTypeRC512-FE-REV-A-SLAVE-SS23", 20049),
          ("rcftTypeRC512-FE-REV-A-SLAVE-SS34", 20050),
          ("rcftTypeRC512-FE-REV-A-S-M", 20051),
          ("rcftTypeRC512-FE-REV-A-S-S1", 20052),
          ("rcftTypeRC512-FE-REV-A-S-S2", 20053),
          ("rcftTypeRC512-FE-REV-A-S-S3", 20054),
          ("rcftTypeRC512-FE-REV-A-S-noOptical", 20055),
          ("rcftTypeRC512-FE-REV-A-S-SS13", 20056),
          ("rcftTypeRC512-FE-REV-A-S-SS23", 20057),
          ("rcftTypeRC512-FE-REV-A-S-SS34", 20058),
          ("rcftTypeRC512-FE-REV-A-C-M", 20059),
          ("rcftTypeRC512-FE-REV-A-C-S1", 20060),
          ("rcftTypeRC512-FE-REV-A-C-S2", 20061),
          ("rcftTypeRC512-FE-REV-A-C-S3", 20062),
          ("rcftTypeRC512-FE-REV-A-C-noOptical", 20063),
          ("rcftTypeRC512-FE-REV-A-C-SS13", 20064),
          ("rcftTypeRC512-FE-REV-A-C-SS23", 20065),
          ("rcftTypeRC512-FE-REV-A-C-SS34", 20066),
          ("rcftTypeRC952-FXE1-REV-C-SLAVE", 20067),
          ("rcftTypeRC511-4FE-REV-B-SLAVE", 20068),
          ("rcftTypeRC952-FEE1-REV-B-REMOTE", 20069),
          ("rcftTypeRC906H-FEE1-REMOTE-PRIVATE", 20070),
          ("rcftTypeRC521H-FE-DoubleFiber-S", 20073),
          ("rcftTypeRC521H-FE-SingleFiber-S", 20074),
          ("rcftTypeRC521H-FE-S", 20075),
          ("rcftTypeRC522E-FE-REMOTE", 20076),
          ("rcftTypeRC521E-FE", 20077),
          ("rcftTypeRC512-FE", 20078),
          ("rcftTypeRC512-FE-SLAVE", 20079),
          ("rcftTypeRC551-FE-REV-A", 21001),
          ("rcftTypeRC551-GE-REV-A", 21002),
          ("rcftTypeRC551-4FE-REV-A", 21003),
          ("rcftTypeRC551-GE-REV-A1", 21004),
          ("rcftTypeRC552-GE-REV-C", 21005),
          ("rcftTypeRC954-FX8E1-REV-A", 21006),
          ("rcftTypeRC552-FE-REV-B", 21007),
          ("rcftTypeRC831-120-REV-A", 22050),
          ("rcftTypeRC831-240-REV-A", 22051),
          ("rcftTypeRC831-240E-REV-A", 22052),
          ("rcftTypeRC831-30-FV35-REV-A", 22053),
          ("rcftTypeRC831-60-FV35-REV-A", 22054),
          ("rcftTypeRC832-30-SLAVE-REV-A", 22055),
          ("rcftTypeRC832-30-FV35-SLAVE-REV-A", 22056),
          ("rcftTypeRC832-60-SLAVE-REV-A", 22057),
          ("rcftTypeRC832-120L-SLAVE-REV-A", 22058),
          ("rcftTypeRC832-240L-SLAVE-REV-A", 22059),
          ("rcftTypeRCMS2801-30FE-FV35-REV-A", 22060),
          ("rcftTypeRCMS2801-60FE-FV35-REV-A", 22061),
          ("rcftTypeRCMS2801-120FE-SLAVE-REV-A", 22062),
          ("rcftTypeRCMS2801-240FE-SLAVE-REV-A", 22063),
          ("rcftTypeRCMS2801-240EFE-SLAVE-REV-A", 22064),
          ("rcftTypeRCMS2802-30FE-SLAVE-REV-A", 22065),
          ("rcftTypeRCMS2802-60FE-SLAVE-REV-A", 22066),
          ("rcftTypeRCMS2802-120LFE-SLAVE-REV-A", 22070),
          ("rcftTypeRCMS2802-240LFE-SLAVE-REV-A", 22071),
          ("rcftTypeRC832-30-FV35-SLAVE-REVB", 22072),
          ("rcftTypeRC804-30B-S1-SLAVE-REV-A", 22073),
          ("rcftTypeRC806-30B-S1-SLAVE-REV-A", 22074),
          ("rcftTypeRC832-30-FV35-SLAVE-REVA1", 22075),
          ("rcftTypeRC831-30-FV35-SLAVE-REVA1", 22076),
          ("rcftTypeRC831-60-FV35-SLAVE-REVA1", 22077),
          ("rcftTypeRCMS2801-30FE-FV35-SLAVE-REVA1", 22078),
          ("rcftTypeRCMS2801-60FE-FV35-SLAVE-REVA1", 22079),
          ("rcftTypeRCMS2802-2T1-FE-SLAVE-REV-A", 22081),
          ("rcftTypeRCMS2802-4T1-FE-SLAVE-REV-A", 22082),
          ("rcftTypeRCMS2802-8T1-FE-SLAVE-REV-A", 22083),
          ("rcftTypeRCMS2802-60FX-SLAVE-REV-A", 22084),
          ("rcftTypeRC1101-FEV35E1-REV-A", 25004),
          ("rcftTypeRC1102-FE-REV-B-SLAVE", 25005),
          ("rcftTypeRC1102-FE-4W-REV-A-SLAVE", 25006),
          ("rcftTypeRC1101-FE-V35E1-REV-B", 25007),
          ("rcftTypeRCMS2802-120LGE-BL-A-SLAVE", 26008),
          ("rcftTypeRCMS2802-240LGE-BL-A-SLAVE", 26011),
          ("rcftTypeRCMS2802-60GE-BL-A-SLAVE", 26099),
          ("rcftTypeRCMS2802-30GE-BL-A-SLAVE", 26100),
          ("rcftTypeRC906H-FEE1-REV-A-REMOTE", 45313),
          ("rcftTypeRC906H-FXE1-REV-A-REMOTE", 45314),
          ("rcftTypeRC602-GEF-REV-C", 45318),
          ("rcftTypeTHIRD-PARTY-PRODUCT", 62128),
          ("rcftTypeRCMS2802-60GE-BL-REV-B-REMOTE", 62471),
          ("rcftTypeRC904-PE1-REMOTE", 62514),
          ("rcftTypeRCMS2802-120LGE-BL-REV-B-REMOTE", 62518),
          ("rcftTypeRCMS2802-240LGE-BL-REV-B-REMOTE", 62521),
          ("rcftTypeRC958-FE4E1-REV-A-REMOTE", 62526),
          ("rcftTypeRC958-FE8E1-REV-A-REMOTE", 62529),
          ("rcftTypeRC958-FX4E1-REV-A-REMOTE", 62533),
          ("rcftTypeRC958-FX8E1-REV-A-REMOTE", 62536),
          ("rcftTypeRC908-FEV35-REV-A-REMOTE", 62540),
          ("rcftTypeRC958-FEE1-REV-A-REMOTE", 62543),
          ("rcftTypeRC958-FXE1-REV-A-REMOTE", 62546),
          ("rcftTypeRC906G-FE4E1-REMOTE", 62550),
          ("rcftTypeRC906G-FX4E1-REMOTE", 62553),
          ("rcftTypeRC906G-FEE1-REMOTE", 62557),
          ("rcftTypeRC906G-FXE1-REMOTE", 62560),
          ("rcftTypeRC906G-FE8E1-REMOTE", 62563),
          ("rcftTypeRC906G-FX8E1-REMOTE", 62567),
          ("rcftTypeRCVS1000-901UL-REMOTE", 62571),
          ("rcftTypeRCMS2912-4E1T1GE-REV-A", 62575),
          ("rcftTypeRCMS2912-8E1T1GE-REV-A", 62578),
          ("rcftTypeRC952-SE1M-REMOTE", 62582),
          ("rcftTypeRCMS2902-120LFE-REMOTE", 62589),
          ("rcftTypeRCMS2902-240LFE-REMOTE", 62592),
          ("rcftTypeRCMS2902-60FE-REMOTE", 62595),
          ("rcftTypeRC862-60-REMOTE", 62598),
          ("rcftTypeRC862-30-REMOTE", 62603),
          ("rcftTypeRC952-CSE1M-REMOTE", 62606),
          ("rcftTypeRCMS2911-480FE", 62607),
          ("rcftTypeRCMS2912-480FE-REMOTE", 62611),
          ("rcftTypeRCMS2912-240FE-REMOTE", 62615),
          ("rcftTypeRCMS2901-480EFE", 62616),
          ("rcftTypeRC861-480E", 62618),
          ("rcftTypeTS1000-UNCONFIG-PRODUCT", 64769),
          ("rcftTypeRC521-FE-REV-C", 64770),
          ("rcftTypeRC521-FE-REV-D", 64771),
          ("rcftTypeRCVS1000-504A", 206915),
          ("rcftTypeRCVS1000-501B", 206918),
          ("rcftTypeRCVS1000-502B", 206919))
    )


_RcftRemoteDeviceType_Type.__name__ = "Integer32"
_RcftRemoteDeviceType_Object = MibTableColumn
rcftRemoteDeviceType = _RcftRemoteDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 3),
    _RcftRemoteDeviceType_Type()
)
rcftRemoteDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDeviceType.setStatus("current")


class _RcftRemoteDeviceLocalPortType_Type(Integer32):
    """Custom type rcftRemoteDeviceLocalPortType based on Integer32"""
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
        *(("ethport", 1),
          ("optical", 2),
          ("e1port", 3),
          ("ghdsl", 4))
    )


_RcftRemoteDeviceLocalPortType_Type.__name__ = "Integer32"
_RcftRemoteDeviceLocalPortType_Object = MibTableColumn
rcftRemoteDeviceLocalPortType = _RcftRemoteDeviceLocalPortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 4),
    _RcftRemoteDeviceLocalPortType_Type()
)
rcftRemoteDeviceLocalPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDeviceLocalPortType.setStatus("current")
_RcftRemoteDeviceLocalPortIndex_Type = Integer32
_RcftRemoteDeviceLocalPortIndex_Object = MibTableColumn
rcftRemoteDeviceLocalPortIndex = _RcftRemoteDeviceLocalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 5),
    _RcftRemoteDeviceLocalPortIndex_Type()
)
rcftRemoteDeviceLocalPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDeviceLocalPortIndex.setStatus("current")


class _RcftRemoteDeviceVersionInfo_Type(OctetString):
    """Custom type rcftRemoteDeviceVersionInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RcftRemoteDeviceVersionInfo_Type.__name__ = "OctetString"
_RcftRemoteDeviceVersionInfo_Object = MibTableColumn
rcftRemoteDeviceVersionInfo = _RcftRemoteDeviceVersionInfo_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 6),
    _RcftRemoteDeviceVersionInfo_Type()
)
rcftRemoteDeviceVersionInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDeviceVersionInfo.setStatus("current")
_RcftRemoteSysTemperature_Type = Integer32
_RcftRemoteSysTemperature_Object = MibTableColumn
rcftRemoteSysTemperature = _RcftRemoteSysTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 7),
    _RcftRemoteSysTemperature_Type()
)
rcftRemoteSysTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSysTemperature.setStatus("current")


class _RcftRemoteSysVoltageStatus_Type(Integer32):
    """Custom type rcftRemoteSysVoltageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("toohigh", 2),
          ("toolow", 3))
    )


_RcftRemoteSysVoltageStatus_Type.__name__ = "Integer32"
_RcftRemoteSysVoltageStatus_Object = MibTableColumn
rcftRemoteSysVoltageStatus = _RcftRemoteSysVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 8),
    _RcftRemoteSysVoltageStatus_Type()
)
rcftRemoteSysVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSysVoltageStatus.setStatus("current")


class _RcftRemoteDeviceWorkMode_Type(Integer32):
    """Custom type rcftRemoteDeviceWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("masterCtrl", 1),
          ("slaveCtrl", 2))
    )


_RcftRemoteDeviceWorkMode_Type.__name__ = "Integer32"
_RcftRemoteDeviceWorkMode_Object = MibTableColumn
rcftRemoteDeviceWorkMode = _RcftRemoteDeviceWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 9),
    _RcftRemoteDeviceWorkMode_Type()
)
rcftRemoteDeviceWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDeviceWorkMode.setStatus("current")


class _RcftRemoteDeviceFrameLen_Type(Integer32):
    """Custom type rcftRemoteDeviceFrameLen based on Integer32"""
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
        *(("framelen1916B", 1),
          ("framelen1536B", 2),
          ("framelen9728B", 3),
          ("framelen1518B", 4),
          ("framelen9kB", 5),
          ("framelen2048", 6))
    )


_RcftRemoteDeviceFrameLen_Type.__name__ = "Integer32"
_RcftRemoteDeviceFrameLen_Object = MibTableColumn
rcftRemoteDeviceFrameLen = _RcftRemoteDeviceFrameLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 10),
    _RcftRemoteDeviceFrameLen_Type()
)
rcftRemoteDeviceFrameLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceFrameLen.setStatus("current")


class _RcftRemoteDeviceOrder_Type(Integer32):
    """Custom type rcftRemoteDeviceOrder based on Integer32"""
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
              17,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("reqInfoStart", 2),
          ("reqInfoStop", 3),
          ("shdslPortReset", 4),
          ("shdslPortInisdeLoopEnable", 5),
          ("shdslPortOutsideLoopEnable", 6),
          ("shdslPortInisdeLoopDisable", 7),
          ("shdslPortOutsideLoopDisable", 8),
          ("e1UnUsedAlarmMask", 9),
          ("e1UnUsedAlarmUnMask", 10),
          ("pdhPortOutsideLoopEnable", 11),
          ("ds3E3PortOutsideLoopEnable", 12),
          ("allLoopDisable", 13),
          ("errorCodeTestEnable", 14),
          ("errorCodeTestDisable", 15),
          ("portOutsideLoopEnable", 17),
          ("statisticInfoClear", 24),
          ("defaultConfigData", 25))
    )


_RcftRemoteDeviceOrder_Type.__name__ = "Integer32"
_RcftRemoteDeviceOrder_Object = MibTableColumn
rcftRemoteDeviceOrder = _RcftRemoteDeviceOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 11),
    _RcftRemoteDeviceOrder_Type()
)
rcftRemoteDeviceOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceOrder.setStatus("current")


class _RcftRemoteDeviceConfigFlag_Type(Integer32):
    """Custom type rcftRemoteDeviceConfigFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("set", 1)
    )


_RcftRemoteDeviceConfigFlag_Type.__name__ = "Integer32"
_RcftRemoteDeviceConfigFlag_Object = MibTableColumn
rcftRemoteDeviceConfigFlag = _RcftRemoteDeviceConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 12),
    _RcftRemoteDeviceConfigFlag_Type()
)
rcftRemoteDeviceConfigFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceConfigFlag.setStatus("current")


class _RcftRemoteSlotAutoCutErrLineEn_Type(Integer32):
    """Custom type rcftRemoteSlotAutoCutErrLineEn based on Integer32"""
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


_RcftRemoteSlotAutoCutErrLineEn_Type.__name__ = "Integer32"
_RcftRemoteSlotAutoCutErrLineEn_Object = MibTableColumn
rcftRemoteSlotAutoCutErrLineEn = _RcftRemoteSlotAutoCutErrLineEn_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 13),
    _RcftRemoteSlotAutoCutErrLineEn_Type()
)
rcftRemoteSlotAutoCutErrLineEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSlotAutoCutErrLineEn.setStatus("current")


class _RcftRemotePowerSupply_Type(Integer32):
    """Custom type rcftRemotePowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ac220v", 1),
          ("dc-48v", 2),
          ("dc24v", 3))
    )


_RcftRemotePowerSupply_Type.__name__ = "Integer32"
_RcftRemotePowerSupply_Object = MibTableColumn
rcftRemotePowerSupply = _RcftRemotePowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 14),
    _RcftRemotePowerSupply_Type()
)
rcftRemotePowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemotePowerSupply.setStatus("current")


class _RcftRemoteDevicePowerDown_Type(Integer32):
    """Custom type rcftRemoteDevicePowerDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("powerdown", 2))
    )


_RcftRemoteDevicePowerDown_Type.__name__ = "Integer32"
_RcftRemoteDevicePowerDown_Object = MibTableColumn
rcftRemoteDevicePowerDown = _RcftRemoteDevicePowerDown_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 15),
    _RcftRemoteDevicePowerDown_Type()
)
rcftRemoteDevicePowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDevicePowerDown.setStatus("current")


class _RcftRemoteDeviceClkMode_Type(Integer32):
    """Custom type rcftRemoteDeviceClkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              100)
        )
    )
    namedValues = NamedValues(
        *(("masterClk", 1),
          ("e1PortClk", 2),
          ("gPortClk", 3),
          ("secondary", 4),
          ("v35PortClk", 5),
          ("reserved", 100))
    )


_RcftRemoteDeviceClkMode_Type.__name__ = "Integer32"
_RcftRemoteDeviceClkMode_Object = MibTableColumn
rcftRemoteDeviceClkMode = _RcftRemoteDeviceClkMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 16),
    _RcftRemoteDeviceClkMode_Type()
)
rcftRemoteDeviceClkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceClkMode.setStatus("current")
_RcftRemoteDeviceE1SubCardType_Type = Integer32
_RcftRemoteDeviceE1SubCardType_Object = MibTableColumn
rcftRemoteDeviceE1SubCardType = _RcftRemoteDeviceE1SubCardType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 17),
    _RcftRemoteDeviceE1SubCardType_Type()
)
rcftRemoteDeviceE1SubCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDeviceE1SubCardType.setStatus("current")


class _RcftRemoteDeviceGateway_Type(OctetString):
    """Custom type rcftRemoteDeviceGateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftRemoteDeviceGateway_Type.__name__ = "OctetString"
_RcftRemoteDeviceGateway_Object = MibTableColumn
rcftRemoteDeviceGateway = _RcftRemoteDeviceGateway_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 18),
    _RcftRemoteDeviceGateway_Type()
)
rcftRemoteDeviceGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceGateway.setStatus("current")


class _RcftRemoteDeviceIP_Type(OctetString):
    """Custom type rcftRemoteDeviceIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftRemoteDeviceIP_Type.__name__ = "OctetString"
_RcftRemoteDeviceIP_Object = MibTableColumn
rcftRemoteDeviceIP = _RcftRemoteDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 19),
    _RcftRemoteDeviceIP_Type()
)
rcftRemoteDeviceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceIP.setStatus("current")


class _RcftRemoteDeviceSubnetMask_Type(OctetString):
    """Custom type rcftRemoteDeviceSubnetMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftRemoteDeviceSubnetMask_Type.__name__ = "OctetString"
_RcftRemoteDeviceSubnetMask_Object = MibTableColumn
rcftRemoteDeviceSubnetMask = _RcftRemoteDeviceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 20),
    _RcftRemoteDeviceSubnetMask_Type()
)
rcftRemoteDeviceSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceSubnetMask.setStatus("current")
_RcftRemoteDeviceVLANID_Type = Integer32
_RcftRemoteDeviceVLANID_Object = MibTableColumn
rcftRemoteDeviceVLANID = _RcftRemoteDeviceVLANID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 21),
    _RcftRemoteDeviceVLANID_Type()
)
rcftRemoteDeviceVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceVLANID.setStatus("current")


class _RcftRemoteDeviceCommunityRW_Type(Integer32):
    """Custom type rcftRemoteDeviceCommunityRW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("readwrite", 2),
          ("clear", 3))
    )


_RcftRemoteDeviceCommunityRW_Type.__name__ = "Integer32"
_RcftRemoteDeviceCommunityRW_Object = MibTableColumn
rcftRemoteDeviceCommunityRW = _RcftRemoteDeviceCommunityRW_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 22),
    _RcftRemoteDeviceCommunityRW_Type()
)
rcftRemoteDeviceCommunityRW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceCommunityRW.setStatus("current")
_RcftRemoteDeviceCommunityLength_Type = Integer32
_RcftRemoteDeviceCommunityLength_Object = MibTableColumn
rcftRemoteDeviceCommunityLength = _RcftRemoteDeviceCommunityLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 23),
    _RcftRemoteDeviceCommunityLength_Type()
)
rcftRemoteDeviceCommunityLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceCommunityLength.setStatus("current")


class _RcftRemoteDeviceCommunity_Type(OctetString):
    """Custom type rcftRemoteDeviceCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftRemoteDeviceCommunity_Type.__name__ = "OctetString"
_RcftRemoteDeviceCommunity_Object = MibTableColumn
rcftRemoteDeviceCommunity = _RcftRemoteDeviceCommunity_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 24),
    _RcftRemoteDeviceCommunity_Type()
)
rcftRemoteDeviceCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceCommunity.setStatus("current")
_RcftRemoteDeviceVoltageValue_Type = Unsigned32
_RcftRemoteDeviceVoltageValue_Object = MibTableColumn
rcftRemoteDeviceVoltageValue = _RcftRemoteDeviceVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 25),
    _RcftRemoteDeviceVoltageValue_Type()
)
rcftRemoteDeviceVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDeviceVoltageValue.setStatus("current")
_RcftRemoteDeviceStatus_Type = Integer32
_RcftRemoteDeviceStatus_Object = MibTableColumn
rcftRemoteDeviceStatus = _RcftRemoteDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 26),
    _RcftRemoteDeviceStatus_Type()
)
rcftRemoteDeviceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceStatus.setStatus("current")
_RcftRemoteSubModuleExist_Type = Integer32
_RcftRemoteSubModuleExist_Object = MibTableColumn
rcftRemoteSubModuleExist = _RcftRemoteSubModuleExist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 27),
    _RcftRemoteSubModuleExist_Type()
)
rcftRemoteSubModuleExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSubModuleExist.setStatus("current")


class _RcftRemoteMultiE1LoopOrder_Type(OctetString):
    """Custom type rcftRemoteMultiE1LoopOrder based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RcftRemoteMultiE1LoopOrder_Type.__name__ = "OctetString"
_RcftRemoteMultiE1LoopOrder_Object = MibTableColumn
rcftRemoteMultiE1LoopOrder = _RcftRemoteMultiE1LoopOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 28),
    _RcftRemoteMultiE1LoopOrder_Type()
)
rcftRemoteMultiE1LoopOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteMultiE1LoopOrder.setStatus("current")
_RcftRemoteOrderTimeParameter_Type = Integer32
_RcftRemoteOrderTimeParameter_Object = MibTableColumn
rcftRemoteOrderTimeParameter = _RcftRemoteOrderTimeParameter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 29),
    _RcftRemoteOrderTimeParameter_Type()
)
rcftRemoteOrderTimeParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteOrderTimeParameter.setStatus("current")
_RcftRemoteOrderModeParameter_Type = Integer32
_RcftRemoteOrderModeParameter_Object = MibTableColumn
rcftRemoteOrderModeParameter = _RcftRemoteOrderModeParameter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 30),
    _RcftRemoteOrderModeParameter_Type()
)
rcftRemoteOrderModeParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteOrderModeParameter.setStatus("current")
_RcftRemoteSDRAMBuf_Type = Integer32
_RcftRemoteSDRAMBuf_Object = MibTableColumn
rcftRemoteSDRAMBuf = _RcftRemoteSDRAMBuf_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 31),
    _RcftRemoteSDRAMBuf_Type()
)
rcftRemoteSDRAMBuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSDRAMBuf.setStatus("current")
_RcftRemoteRLPStatus_Type = Integer32
_RcftRemoteRLPStatus_Object = MibTableColumn
rcftRemoteRLPStatus = _RcftRemoteRLPStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 32),
    _RcftRemoteRLPStatus_Type()
)
rcftRemoteRLPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteRLPStatus.setStatus("current")
_RcftRemoteLALStatus_Type = Integer32
_RcftRemoteLALStatus_Object = MibTableColumn
rcftRemoteLALStatus = _RcftRemoteLALStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 33),
    _RcftRemoteLALStatus_Type()
)
rcftRemoteLALStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteLALStatus.setStatus("current")
_RcftRemoteRALStatus_Type = Integer32
_RcftRemoteRALStatus_Object = MibTableColumn
rcftRemoteRALStatus = _RcftRemoteRALStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 34),
    _RcftRemoteRALStatus_Type()
)
rcftRemoteRALStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteRALStatus.setStatus("current")
_RcftRemoteDeviceSwitchStatus_Type = Integer32
_RcftRemoteDeviceSwitchStatus_Object = MibTableColumn
rcftRemoteDeviceSwitchStatus = _RcftRemoteDeviceSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 35),
    _RcftRemoteDeviceSwitchStatus_Type()
)
rcftRemoteDeviceSwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDeviceSwitchStatus.setStatus("current")
_RcftRemoteDeviceMoudleExist_Type = Integer32
_RcftRemoteDeviceMoudleExist_Object = MibTableColumn
rcftRemoteDeviceMoudleExist = _RcftRemoteDeviceMoudleExist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 36),
    _RcftRemoteDeviceMoudleExist_Type()
)
rcftRemoteDeviceMoudleExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDeviceMoudleExist.setStatus("current")


class _RcftRemoteCardInformation_Type(OctetString):
    """Custom type rcftRemoteCardInformation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftRemoteCardInformation_Type.__name__ = "OctetString"
_RcftRemoteCardInformation_Object = MibTableColumn
rcftRemoteCardInformation = _RcftRemoteCardInformation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 37),
    _RcftRemoteCardInformation_Type()
)
rcftRemoteCardInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteCardInformation.setStatus("current")
_RcftRemoteSwitchType_Type = Integer32
_RcftRemoteSwitchType_Object = MibTableColumn
rcftRemoteSwitchType = _RcftRemoteSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 38),
    _RcftRemoteSwitchType_Type()
)
rcftRemoteSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSwitchType.setStatus("current")
_RcftRemoteConnectMode_Type = Integer32
_RcftRemoteConnectMode_Object = MibTableColumn
rcftRemoteConnectMode = _RcftRemoteConnectMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 39),
    _RcftRemoteConnectMode_Type()
)
rcftRemoteConnectMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteConnectMode.setStatus("current")
_RcftRemoteQosEnable_Type = Integer32
_RcftRemoteQosEnable_Object = MibTableColumn
rcftRemoteQosEnable = _RcftRemoteQosEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 40),
    _RcftRemoteQosEnable_Type()
)
rcftRemoteQosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteQosEnable.setStatus("current")
_RcftRemoteBaseCOS_Type = Integer32
_RcftRemoteBaseCOS_Object = MibTableColumn
rcftRemoteBaseCOS = _RcftRemoteBaseCOS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 41),
    _RcftRemoteBaseCOS_Type()
)
rcftRemoteBaseCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteBaseCOS.setStatus("current")


class _RcftRemoteDSCP_Type(OctetString):
    """Custom type rcftRemoteDSCP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_RcftRemoteDSCP_Type.__name__ = "OctetString"
_RcftRemoteDSCP_Object = MibTableColumn
rcftRemoteDSCP = _RcftRemoteDSCP_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 42),
    _RcftRemoteDSCP_Type()
)
rcftRemoteDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDSCP.setStatus("current")
_RcftRemoteQueuesPolicy_Type = Integer32
_RcftRemoteQueuesPolicy_Object = MibTableColumn
rcftRemoteQueuesPolicy = _RcftRemoteQueuesPolicy_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 43),
    _RcftRemoteQueuesPolicy_Type()
)
rcftRemoteQueuesPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteQueuesPolicy.setStatus("current")


class _RcftRemoteMultiE1AlarmRejectOrder_Type(OctetString):
    """Custom type rcftRemoteMultiE1AlarmRejectOrder based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RcftRemoteMultiE1AlarmRejectOrder_Type.__name__ = "OctetString"
_RcftRemoteMultiE1AlarmRejectOrder_Object = MibTableColumn
rcftRemoteMultiE1AlarmRejectOrder = _RcftRemoteMultiE1AlarmRejectOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 44),
    _RcftRemoteMultiE1AlarmRejectOrder_Type()
)
rcftRemoteMultiE1AlarmRejectOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteMultiE1AlarmRejectOrder.setStatus("current")
_RcftRemoteT1PortPulseWaveForm_Type = Integer32
_RcftRemoteT1PortPulseWaveForm_Object = MibTableColumn
rcftRemoteT1PortPulseWaveForm = _RcftRemoteT1PortPulseWaveForm_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 45),
    _RcftRemoteT1PortPulseWaveForm_Type()
)
rcftRemoteT1PortPulseWaveForm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteT1PortPulseWaveForm.setStatus("current")
_RcftRemoteT1PortCodeType_Type = Integer32
_RcftRemoteT1PortCodeType_Object = MibTableColumn
rcftRemoteT1PortCodeType = _RcftRemoteT1PortCodeType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 46),
    _RcftRemoteT1PortCodeType_Type()
)
rcftRemoteT1PortCodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteT1PortCodeType.setStatus("current")
_RcftRemoteDeviceSabitMode_Type = Integer32
_RcftRemoteDeviceSabitMode_Object = MibTableColumn
rcftRemoteDeviceSabitMode = _RcftRemoteDeviceSabitMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 47),
    _RcftRemoteDeviceSabitMode_Type()
)
rcftRemoteDeviceSabitMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDeviceSabitMode.setStatus("current")


class _RcftRemoteDeviceApsWaitToRestore_Type(Integer32):
    """Custom type rcftRemoteDeviceApsWaitToRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RcftRemoteDeviceApsWaitToRestore_Type.__name__ = "Integer32"
_RcftRemoteDeviceApsWaitToRestore_Object = MibTableColumn
rcftRemoteDeviceApsWaitToRestore = _RcftRemoteDeviceApsWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 48),
    _RcftRemoteDeviceApsWaitToRestore_Type()
)
rcftRemoteDeviceApsWaitToRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceApsWaitToRestore.setStatus("current")
_RcftRemoteDeviceCLKChannel_Type = Integer32
_RcftRemoteDeviceCLKChannel_Object = MibTableColumn
rcftRemoteDeviceCLKChannel = _RcftRemoteDeviceCLKChannel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 49),
    _RcftRemoteDeviceCLKChannel_Type()
)
rcftRemoteDeviceCLKChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDeviceCLKChannel.setStatus("current")
_RcftRemoteDeviceRmcChannelType_Type = Integer32
_RcftRemoteDeviceRmcChannelType_Object = MibTableColumn
rcftRemoteDeviceRmcChannelType = _RcftRemoteDeviceRmcChannelType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 50),
    _RcftRemoteDeviceRmcChannelType_Type()
)
rcftRemoteDeviceRmcChannelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceRmcChannelType.setStatus("current")


class _RcftRemoteDeviceProductType_Type(OctetString):
    """Custom type rcftRemoteDeviceProductType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RcftRemoteDeviceProductType_Type.__name__ = "OctetString"
_RcftRemoteDeviceProductType_Object = MibTableColumn
rcftRemoteDeviceProductType = _RcftRemoteDeviceProductType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 51),
    _RcftRemoteDeviceProductType_Type()
)
rcftRemoteDeviceProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDeviceProductType.setStatus("current")
_RcftRemoteDeviceProtocolVer_Type = Integer32
_RcftRemoteDeviceProtocolVer_Object = MibTableColumn
rcftRemoteDeviceProtocolVer = _RcftRemoteDeviceProtocolVer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 52),
    _RcftRemoteDeviceProtocolVer_Type()
)
rcftRemoteDeviceProtocolVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDeviceProtocolVer.setStatus("current")
_RcftRemoteDeviceVenderCode_Type = Integer32
_RcftRemoteDeviceVenderCode_Object = MibTableColumn
rcftRemoteDeviceVenderCode = _RcftRemoteDeviceVenderCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 53),
    _RcftRemoteDeviceVenderCode_Type()
)
rcftRemoteDeviceVenderCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDeviceVenderCode.setStatus("current")
_RcftRemoteDeviceModelID_Type = Integer32
_RcftRemoteDeviceModelID_Object = MibTableColumn
rcftRemoteDeviceModelID = _RcftRemoteDeviceModelID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 54),
    _RcftRemoteDeviceModelID_Type()
)
rcftRemoteDeviceModelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDeviceModelID.setStatus("current")
_RcftRemoteE1PortNumber_Type = Integer32
_RcftRemoteE1PortNumber_Object = MibTableColumn
rcftRemoteE1PortNumber = _RcftRemoteE1PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 55),
    _RcftRemoteE1PortNumber_Type()
)
rcftRemoteE1PortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1PortNumber.setStatus("current")
_RcftRemoteDeviceVLANType_Type = Integer32
_RcftRemoteDeviceVLANType_Object = MibTableColumn
rcftRemoteDeviceVLANType = _RcftRemoteDeviceVLANType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 56),
    _RcftRemoteDeviceVLANType_Type()
)
rcftRemoteDeviceVLANType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceVLANType.setStatus("current")
_RcftRemoteDeviceQoSPolicy_Type = Integer32
_RcftRemoteDeviceQoSPolicy_Object = MibTableColumn
rcftRemoteDeviceQoSPolicy = _RcftRemoteDeviceQoSPolicy_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 57),
    _RcftRemoteDeviceQoSPolicy_Type()
)
rcftRemoteDeviceQoSPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceQoSPolicy.setStatus("current")
_RcftRemoteDeviceApsE3SwitchDelay_Type = Integer32
_RcftRemoteDeviceApsE3SwitchDelay_Object = MibTableColumn
rcftRemoteDeviceApsE3SwitchDelay = _RcftRemoteDeviceApsE3SwitchDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 58),
    _RcftRemoteDeviceApsE3SwitchDelay_Type()
)
rcftRemoteDeviceApsE3SwitchDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceApsE3SwitchDelay.setStatus("current")
_RcftRemoteDeviceApsE6SwitchDelay_Type = Integer32
_RcftRemoteDeviceApsE6SwitchDelay_Object = MibTableColumn
rcftRemoteDeviceApsE6SwitchDelay = _RcftRemoteDeviceApsE6SwitchDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 59),
    _RcftRemoteDeviceApsE6SwitchDelay_Type()
)
rcftRemoteDeviceApsE6SwitchDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceApsE6SwitchDelay.setStatus("current")
_RcftRemoteDeviceVLANTagDirection_Type = Integer32
_RcftRemoteDeviceVLANTagDirection_Object = MibTableColumn
rcftRemoteDeviceVLANTagDirection = _RcftRemoteDeviceVLANTagDirection_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 60),
    _RcftRemoteDeviceVLANTagDirection_Type()
)
rcftRemoteDeviceVLANTagDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceVLANTagDirection.setStatus("current")
_RcftRemoteDeviceVLANTagModule_Type = Integer32
_RcftRemoteDeviceVLANTagModule_Object = MibTableColumn
rcftRemoteDeviceVLANTagModule = _RcftRemoteDeviceVLANTagModule_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 61),
    _RcftRemoteDeviceVLANTagModule_Type()
)
rcftRemoteDeviceVLANTagModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceVLANTagModule.setStatus("current")
_RcftRemoteDeviceISPTPID_Type = Integer32
_RcftRemoteDeviceISPTPID_Object = MibTableColumn
rcftRemoteDeviceISPTPID = _RcftRemoteDeviceISPTPID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 62),
    _RcftRemoteDeviceISPTPID_Type()
)
rcftRemoteDeviceISPTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceISPTPID.setStatus("current")
_RcftRemoteE1DS1PortType_Type = Integer32
_RcftRemoteE1DS1PortType_Object = MibTableColumn
rcftRemoteE1DS1PortType = _RcftRemoteE1DS1PortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 63),
    _RcftRemoteE1DS1PortType_Type()
)
rcftRemoteE1DS1PortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteE1DS1PortType.setStatus("current")
_RcftRemoteDeviceE1FrameChannel_Type = Integer32
_RcftRemoteDeviceE1FrameChannel_Object = MibTableColumn
rcftRemoteDeviceE1FrameChannel = _RcftRemoteDeviceE1FrameChannel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 64),
    _RcftRemoteDeviceE1FrameChannel_Type()
)
rcftRemoteDeviceE1FrameChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceE1FrameChannel.setStatus("current")
_RcftRemoteDeviceManageID_Type = Integer32
_RcftRemoteDeviceManageID_Object = MibTableColumn
rcftRemoteDeviceManageID = _RcftRemoteDeviceManageID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 65),
    _RcftRemoteDeviceManageID_Type()
)
rcftRemoteDeviceManageID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceManageID.setStatus("current")


class _RcftRemoteDeviceMibUse_Type(Integer32):
    """Custom type rcftRemoteDeviceMibUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mib002", 1),
          ("rccomlib", 2))
    )


_RcftRemoteDeviceMibUse_Type.__name__ = "Integer32"
_RcftRemoteDeviceMibUse_Object = MibTableColumn
rcftRemoteDeviceMibUse = _RcftRemoteDeviceMibUse_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 1, 1, 66),
    _RcftRemoteDeviceMibUse_Type()
)
rcftRemoteDeviceMibUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDeviceMibUse.setStatus("current")
_RcftRemoteDeviceConfigFlagTable_Object = MibTable
rcftRemoteDeviceConfigFlagTable = _RcftRemoteDeviceConfigFlagTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rcftRemoteDeviceConfigFlagTable.setStatus("current")
_RcftRemoteDeviceConfigFlagEntry_Object = MibTableRow
rcftRemoteDeviceConfigFlagEntry = _RcftRemoteDeviceConfigFlagEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 2, 1)
)
rcftRemoteDeviceConfigFlagEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteDeviceConfigFlagEntry.setStatus("current")
_RcftRemoteDeviceConfigFinishFlag_Type = Integer32
_RcftRemoteDeviceConfigFinishFlag_Object = MibTableColumn
rcftRemoteDeviceConfigFinishFlag = _RcftRemoteDeviceConfigFinishFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 1, 2, 1, 1),
    _RcftRemoteDeviceConfigFinishFlag_Type()
)
rcftRemoteDeviceConfigFinishFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDeviceConfigFinishFlag.setStatus("current")
_RcftRemoteDeviceSysTraps_ObjectIdentity = ObjectIdentity
rcftRemoteDeviceSysTraps = _RcftRemoteDeviceSysTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 2)
)
_RcftRemoteDeviceEthMIB_ObjectIdentity = ObjectIdentity
rcftRemoteDeviceEthMIB = _RcftRemoteDeviceEthMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2)
)
_RcftRemoteDeviceEthFeMIB_ObjectIdentity = ObjectIdentity
rcftRemoteDeviceEthFeMIB = _RcftRemoteDeviceEthFeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1)
)
_RcftRemoteDeviceEthFeObjects_ObjectIdentity = ObjectIdentity
rcftRemoteDeviceEthFeObjects = _RcftRemoteDeviceEthFeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1)
)
_RcftRemoteEthFePortTable_Object = MibTable
rcftRemoteEthFePortTable = _RcftRemoteEthFePortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteEthFePortTable.setStatus("current")
_RcftRemoteEthFePortEntry_Object = MibTableRow
rcftRemoteEthFePortEntry = _RcftRemoteEthFePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1)
)
rcftRemoteEthFePortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFeIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteEthFePortEntry.setStatus("current")
_RcftRemoteEthFeIndex_Type = Integer32
_RcftRemoteEthFeIndex_Object = MibTableColumn
rcftRemoteEthFeIndex = _RcftRemoteEthFeIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 1),
    _RcftRemoteEthFeIndex_Type()
)
rcftRemoteEthFeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFeIndex.setStatus("current")


class _RcftRemoteEthFeLinkStatus_Type(Integer32):
    """Custom type rcftRemoteEthFeLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkup", 1),
          ("linkdown", 2))
    )


_RcftRemoteEthFeLinkStatus_Type.__name__ = "Integer32"
_RcftRemoteEthFeLinkStatus_Object = MibTableColumn
rcftRemoteEthFeLinkStatus = _RcftRemoteEthFeLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 2),
    _RcftRemoteEthFeLinkStatus_Type()
)
rcftRemoteEthFeLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFeLinkStatus.setStatus("current")


class _RcftRemoteEthFeShutDown_Type(Integer32):
    """Custom type rcftRemoteEthFeShutDown based on Integer32"""
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
        *(("open", 1),
          ("close", 2),
          ("closebyLocalOtherPortFault", 3),
          ("closebyOppositeFePortFault", 4),
          ("closebyLoopBack", 5))
    )


_RcftRemoteEthFeShutDown_Type.__name__ = "Integer32"
_RcftRemoteEthFeShutDown_Object = MibTableColumn
rcftRemoteEthFeShutDown = _RcftRemoteEthFeShutDown_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 3),
    _RcftRemoteEthFeShutDown_Type()
)
rcftRemoteEthFeShutDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFeShutDown.setStatus("current")


class _RcftRemoteEthFeAutoNegotiation_Type(Integer32):
    """Custom type rcftRemoteEthFeAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manul", 2))
    )


_RcftRemoteEthFeAutoNegotiation_Type.__name__ = "Integer32"
_RcftRemoteEthFeAutoNegotiation_Object = MibTableColumn
rcftRemoteEthFeAutoNegotiation = _RcftRemoteEthFeAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 4),
    _RcftRemoteEthFeAutoNegotiation_Type()
)
rcftRemoteEthFeAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFeAutoNegotiation.setStatus("current")


class _RcftRemoteEthFeSpeed_Type(Integer32):
    """Custom type rcftRemoteEthFeSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("rcft10Mbps", 1),
          ("rcft100Mbps", 2),
          ("rcft1000Mbps", 3),
          ("rcft10Gbps", 4),
          ("other", 16))
    )


_RcftRemoteEthFeSpeed_Type.__name__ = "Integer32"
_RcftRemoteEthFeSpeed_Object = MibTableColumn
rcftRemoteEthFeSpeed = _RcftRemoteEthFeSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 5),
    _RcftRemoteEthFeSpeed_Type()
)
rcftRemoteEthFeSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFeSpeed.setStatus("current")


class _RcftRemoteEthFeDuplex_Type(Integer32):
    """Custom type rcftRemoteEthFeDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2))
    )


_RcftRemoteEthFeDuplex_Type.__name__ = "Integer32"
_RcftRemoteEthFeDuplex_Object = MibTableColumn
rcftRemoteEthFeDuplex = _RcftRemoteEthFeDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 6),
    _RcftRemoteEthFeDuplex_Type()
)
rcftRemoteEthFeDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFeDuplex.setStatus("current")


class _RcftRemoteEthFeFlowControl_Type(Integer32):
    """Custom type rcftRemoteEthFeFlowControl based on Integer32"""
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


_RcftRemoteEthFeFlowControl_Type.__name__ = "Integer32"
_RcftRemoteEthFeFlowControl_Object = MibTableColumn
rcftRemoteEthFeFlowControl = _RcftRemoteEthFeFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 7),
    _RcftRemoteEthFeFlowControl_Type()
)
rcftRemoteEthFeFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFeFlowControl.setStatus("current")
_RcftRemoteEthFeRestrictSpeed_Type = Integer32
_RcftRemoteEthFeRestrictSpeed_Object = MibTableColumn
rcftRemoteEthFeRestrictSpeed = _RcftRemoteEthFeRestrictSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 8),
    _RcftRemoteEthFeRestrictSpeed_Type()
)
rcftRemoteEthFeRestrictSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFeRestrictSpeed.setStatus("current")


class _RcftRemoteEthFeFaultPass_Type(Integer32):
    """Custom type rcftRemoteEthFeFaultPass based on Integer32"""
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


_RcftRemoteEthFeFaultPass_Type.__name__ = "Integer32"
_RcftRemoteEthFeFaultPass_Object = MibTableColumn
rcftRemoteEthFeFaultPass = _RcftRemoteEthFeFaultPass_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 9),
    _RcftRemoteEthFeFaultPass_Type()
)
rcftRemoteEthFeFaultPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFeFaultPass.setStatus("current")


class _RcftRemoteEthFeDisabledByRemoteTP_Type(Integer32):
    """Custom type rcftRemoteEthFeDisabledByRemoteTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_RcftRemoteEthFeDisabledByRemoteTP_Type.__name__ = "Integer32"
_RcftRemoteEthFeDisabledByRemoteTP_Object = MibTableColumn
rcftRemoteEthFeDisabledByRemoteTP = _RcftRemoteEthFeDisabledByRemoteTP_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 10),
    _RcftRemoteEthFeDisabledByRemoteTP_Type()
)
rcftRemoteEthFeDisabledByRemoteTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFeDisabledByRemoteTP.setStatus("current")


class _RcftRemoteEthFeDisabledByFxToFeFP_Type(Integer32):
    """Custom type rcftRemoteEthFeDisabledByFxToFeFP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_RcftRemoteEthFeDisabledByFxToFeFP_Type.__name__ = "Integer32"
_RcftRemoteEthFeDisabledByFxToFeFP_Object = MibTableColumn
rcftRemoteEthFeDisabledByFxToFeFP = _RcftRemoteEthFeDisabledByFxToFeFP_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 11),
    _RcftRemoteEthFeDisabledByFxToFeFP_Type()
)
rcftRemoteEthFeDisabledByFxToFeFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFeDisabledByFxToFeFP.setStatus("current")
_RcftRemoteEthFeTxRestrictSpeed_Type = Integer32
_RcftRemoteEthFeTxRestrictSpeed_Object = MibTableColumn
rcftRemoteEthFeTxRestrictSpeed = _RcftRemoteEthFeTxRestrictSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 12),
    _RcftRemoteEthFeTxRestrictSpeed_Type()
)
rcftRemoteEthFeTxRestrictSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFeTxRestrictSpeed.setStatus("current")


class _RcftRemoteEthFeTag_Type(Integer32):
    """Custom type rcftRemoteEthFeTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tag", 1),
          ("untag", 2))
    )


_RcftRemoteEthFeTag_Type.__name__ = "Integer32"
_RcftRemoteEthFeTag_Object = MibTableColumn
rcftRemoteEthFeTag = _RcftRemoteEthFeTag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 13),
    _RcftRemoteEthFeTag_Type()
)
rcftRemoteEthFeTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFeTag.setStatus("current")
_RcftRemoteEthFePortStatus_Type = Integer32
_RcftRemoteEthFePortStatus_Object = MibTableColumn
rcftRemoteEthFePortStatus = _RcftRemoteEthFePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 14),
    _RcftRemoteEthFePortStatus_Type()
)
rcftRemoteEthFePortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFePortStatus.setStatus("current")
_RcftRemoteEthFeRestrictSpeedStep_Type = Integer32
_RcftRemoteEthFeRestrictSpeedStep_Object = MibTableColumn
rcftRemoteEthFeRestrictSpeedStep = _RcftRemoteEthFeRestrictSpeedStep_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 15),
    _RcftRemoteEthFeRestrictSpeedStep_Type()
)
rcftRemoteEthFeRestrictSpeedStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFeRestrictSpeedStep.setStatus("current")
_RcftRemoteEthFeOrderTimeParameter_Type = Integer32
_RcftRemoteEthFeOrderTimeParameter_Object = MibTableColumn
rcftRemoteEthFeOrderTimeParameter = _RcftRemoteEthFeOrderTimeParameter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 16),
    _RcftRemoteEthFeOrderTimeParameter_Type()
)
rcftRemoteEthFeOrderTimeParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFeOrderTimeParameter.setStatus("current")
_RcftRemoteEthFeOrderModeParameter_Type = Integer32
_RcftRemoteEthFeOrderModeParameter_Object = MibTableColumn
rcftRemoteEthFeOrderModeParameter = _RcftRemoteEthFeOrderModeParameter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 17),
    _RcftRemoteEthFeOrderModeParameter_Type()
)
rcftRemoteEthFeOrderModeParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFeOrderModeParameter.setStatus("current")
_RcftRemoteEthFeOrder_Type = Integer32
_RcftRemoteEthFeOrder_Object = MibTableColumn
rcftRemoteEthFeOrder = _RcftRemoteEthFeOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 18),
    _RcftRemoteEthFeOrder_Type()
)
rcftRemoteEthFeOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFeOrder.setStatus("current")
_RcftRemoteEthFePortStatusExtend_Type = Integer32
_RcftRemoteEthFePortStatusExtend_Object = MibTableColumn
rcftRemoteEthFePortStatusExtend = _RcftRemoteEthFePortStatusExtend_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 19),
    _RcftRemoteEthFePortStatusExtend_Type()
)
rcftRemoteEthFePortStatusExtend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFePortStatusExtend.setStatus("current")
_RcftRemoteEthFeStormControl_Type = Integer32
_RcftRemoteEthFeStormControl_Object = MibTableColumn
rcftRemoteEthFeStormControl = _RcftRemoteEthFeStormControl_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 20),
    _RcftRemoteEthFeStormControl_Type()
)
rcftRemoteEthFeStormControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFeStormControl.setStatus("current")
_RcftRemoteEthFePVID_Type = Integer32
_RcftRemoteEthFePVID_Object = MibTableColumn
rcftRemoteEthFePVID = _RcftRemoteEthFePVID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 21),
    _RcftRemoteEthFePVID_Type()
)
rcftRemoteEthFePVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFePVID.setStatus("current")
_RcftRemoteEthFeDefaultCOS_Type = Integer32
_RcftRemoteEthFeDefaultCOS_Object = MibTableColumn
rcftRemoteEthFeDefaultCOS = _RcftRemoteEthFeDefaultCOS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 22),
    _RcftRemoteEthFeDefaultCOS_Type()
)
rcftRemoteEthFeDefaultCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFeDefaultCOS.setStatus("current")
_RcftRemoteEthFeQoSPolicy_Type = Integer32
_RcftRemoteEthFeQoSPolicy_Object = MibTableColumn
rcftRemoteEthFeQoSPolicy = _RcftRemoteEthFeQoSPolicy_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 1, 1, 23),
    _RcftRemoteEthFeQoSPolicy_Type()
)
rcftRemoteEthFeQoSPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFeQoSPolicy.setStatus("current")
_RcftRemoteEthFeStatisticTable_Object = MibTable
rcftRemoteEthFeStatisticTable = _RcftRemoteEthFeStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rcftRemoteEthFeStatisticTable.setStatus("current")
_RcftRemoteEthFeStatisticEntry_Object = MibTableRow
rcftRemoteEthFeStatisticEntry = _RcftRemoteEthFeStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteEthFeStatisticEntry.setStatus("current")
_RcftRemoteEthFeTxPackets_Type = Counter32
_RcftRemoteEthFeTxPackets_Object = MibTableColumn
rcftRemoteEthFeTxPackets = _RcftRemoteEthFeTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 2, 1, 1),
    _RcftRemoteEthFeTxPackets_Type()
)
rcftRemoteEthFeTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFeTxPackets.setStatus("current")
_RcftRemoteEthFeTxBytes_Type = Counter32
_RcftRemoteEthFeTxBytes_Object = MibTableColumn
rcftRemoteEthFeTxBytes = _RcftRemoteEthFeTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 2, 1, 2),
    _RcftRemoteEthFeTxBytes_Type()
)
rcftRemoteEthFeTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFeTxBytes.setStatus("current")
_RcftRemoteEthFeRxPackets_Type = Counter32
_RcftRemoteEthFeRxPackets_Object = MibTableColumn
rcftRemoteEthFeRxPackets = _RcftRemoteEthFeRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 2, 1, 3),
    _RcftRemoteEthFeRxPackets_Type()
)
rcftRemoteEthFeRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFeRxPackets.setStatus("current")
_RcftRemoteEthFeRxBytes_Type = Counter32
_RcftRemoteEthFeRxBytes_Object = MibTableColumn
rcftRemoteEthFeRxBytes = _RcftRemoteEthFeRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 2, 1, 4),
    _RcftRemoteEthFeRxBytes_Type()
)
rcftRemoteEthFeRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFeRxBytes.setStatus("current")
_RcftRemoteEthFeRxLostPackets_Type = Counter32
_RcftRemoteEthFeRxLostPackets_Object = MibTableColumn
rcftRemoteEthFeRxLostPackets = _RcftRemoteEthFeRxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 2, 1, 5),
    _RcftRemoteEthFeRxLostPackets_Type()
)
rcftRemoteEthFeRxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFeRxLostPackets.setStatus("current")
_RcftRemoteEthFeFluxTimer_Type = Counter32
_RcftRemoteEthFeFluxTimer_Object = MibTableColumn
rcftRemoteEthFeFluxTimer = _RcftRemoteEthFeFluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 2, 1, 6),
    _RcftRemoteEthFeFluxTimer_Type()
)
rcftRemoteEthFeFluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFeFluxTimer.setStatus("current")
_RcftRemoteEthFeTxLostPackets_Type = Counter32
_RcftRemoteEthFeTxLostPackets_Object = MibTableColumn
rcftRemoteEthFeTxLostPackets = _RcftRemoteEthFeTxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 2, 1, 7),
    _RcftRemoteEthFeTxLostPackets_Type()
)
rcftRemoteEthFeTxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFeTxLostPackets.setStatus("current")
_RcftRemoteEthFePortConfTable_Object = MibTable
rcftRemoteEthFePortConfTable = _RcftRemoteEthFePortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    rcftRemoteEthFePortConfTable.setStatus("current")
_RcftRemoteEthFePortConfEntry_Object = MibTableRow
rcftRemoteEthFePortConfEntry = _RcftRemoteEthFePortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 3, 1)
)
rcftRemoteEthFePortConfEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFeIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteEthFePortConfEntry.setStatus("current")


class _RcftRemoteEthFeConfSpeed_Type(Integer32):
    """Custom type rcftRemoteEthFeConfSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("rcft10Mbps", 1),
          ("rcft100Mbps", 2),
          ("rcft1000Mbps", 3),
          ("rcft10Gbps", 4),
          ("other", 16))
    )


_RcftRemoteEthFeConfSpeed_Type.__name__ = "Integer32"
_RcftRemoteEthFeConfSpeed_Object = MibTableColumn
rcftRemoteEthFeConfSpeed = _RcftRemoteEthFeConfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 3, 1, 1),
    _RcftRemoteEthFeConfSpeed_Type()
)
rcftRemoteEthFeConfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFeConfSpeed.setStatus("current")


class _RcftRemoteEthFeConfDuplex_Type(Integer32):
    """Custom type rcftRemoteEthFeConfDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2))
    )


_RcftRemoteEthFeConfDuplex_Type.__name__ = "Integer32"
_RcftRemoteEthFeConfDuplex_Object = MibTableColumn
rcftRemoteEthFeConfDuplex = _RcftRemoteEthFeConfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 1, 3, 1, 2),
    _RcftRemoteEthFeConfDuplex_Type()
)
rcftRemoteEthFeConfDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFeConfDuplex.setStatus("current")
_RcftRemoteDeviceEthFeTraps_ObjectIdentity = ObjectIdentity
rcftRemoteDeviceEthFeTraps = _RcftRemoteDeviceEthFeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 2)
)
_RcftRemoteDeviceEthFxMIB_ObjectIdentity = ObjectIdentity
rcftRemoteDeviceEthFxMIB = _RcftRemoteDeviceEthFxMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2)
)
_RcftRemoteDeviceEthFxObjects_ObjectIdentity = ObjectIdentity
rcftRemoteDeviceEthFxObjects = _RcftRemoteDeviceEthFxObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1)
)
_RcftRemoteEthFxPortTable_Object = MibTable
rcftRemoteEthFxPortTable = _RcftRemoteEthFxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortTable.setStatus("current")
_RcftRemoteEthFxPortEntry_Object = MibTableRow
rcftRemoteEthFxPortEntry = _RcftRemoteEthFxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1)
)
rcftRemoteEthFxPortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortEntry.setStatus("current")
_RcftRemoteEthFxIndex_Type = Integer32
_RcftRemoteEthFxIndex_Object = MibTableColumn
rcftRemoteEthFxIndex = _RcftRemoteEthFxIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 1),
    _RcftRemoteEthFxIndex_Type()
)
rcftRemoteEthFxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxIndex.setStatus("current")


class _RcftRemoteEthFxFlowControl_Type(Integer32):
    """Custom type rcftRemoteEthFxFlowControl based on Integer32"""
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


_RcftRemoteEthFxFlowControl_Type.__name__ = "Integer32"
_RcftRemoteEthFxFlowControl_Object = MibTableColumn
rcftRemoteEthFxFlowControl = _RcftRemoteEthFxFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 2),
    _RcftRemoteEthFxFlowControl_Type()
)
rcftRemoteEthFxFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFxFlowControl.setStatus("current")


class _RcftRemoteEthFxPortRLK_Type(Integer32):
    """Custom type rcftRemoteEthFxPortRLK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("unlink", 2))
    )


_RcftRemoteEthFxPortRLK_Type.__name__ = "Integer32"
_RcftRemoteEthFxPortRLK_Object = MibTableColumn
rcftRemoteEthFxPortRLK = _RcftRemoteEthFxPortRLK_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 3),
    _RcftRemoteEthFxPortRLK_Type()
)
rcftRemoteEthFxPortRLK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortRLK.setStatus("current")


class _RcftRemoteEthFxPortTLK_Type(Integer32):
    """Custom type rcftRemoteEthFxPortTLK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("unlink", 2))
    )


_RcftRemoteEthFxPortTLK_Type.__name__ = "Integer32"
_RcftRemoteEthFxPortTLK_Object = MibTableColumn
rcftRemoteEthFxPortTLK = _RcftRemoteEthFxPortTLK_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 4),
    _RcftRemoteEthFxPortTLK_Type()
)
rcftRemoteEthFxPortTLK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortTLK.setStatus("current")


class _RcftRemoteEthFxPortSD_Type(Integer32):
    """Custom type rcftRemoteEthFxPortSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("sd", 2))
    )


_RcftRemoteEthFxPortSD_Type.__name__ = "Integer32"
_RcftRemoteEthFxPortSD_Object = MibTableColumn
rcftRemoteEthFxPortSD = _RcftRemoteEthFxPortSD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 5),
    _RcftRemoteEthFxPortSD_Type()
)
rcftRemoteEthFxPortSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortSD.setStatus("current")


class _RcftRemoteEthFxPortTxPowerAbnormal_Type(Integer32):
    """Custom type rcftRemoteEthFxPortTxPowerAbnormal based on Integer32"""
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


_RcftRemoteEthFxPortTxPowerAbnormal_Type.__name__ = "Integer32"
_RcftRemoteEthFxPortTxPowerAbnormal_Object = MibTableColumn
rcftRemoteEthFxPortTxPowerAbnormal = _RcftRemoteEthFxPortTxPowerAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 6),
    _RcftRemoteEthFxPortTxPowerAbnormal_Type()
)
rcftRemoteEthFxPortTxPowerAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortTxPowerAbnormal.setStatus("current")


class _RcftRemoteEthFxPortRxSensitiveAbnormal_Type(Integer32):
    """Custom type rcftRemoteEthFxPortRxSensitiveAbnormal based on Integer32"""
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


_RcftRemoteEthFxPortRxSensitiveAbnormal_Type.__name__ = "Integer32"
_RcftRemoteEthFxPortRxSensitiveAbnormal_Object = MibTableColumn
rcftRemoteEthFxPortRxSensitiveAbnormal = _RcftRemoteEthFxPortRxSensitiveAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 7),
    _RcftRemoteEthFxPortRxSensitiveAbnormal_Type()
)
rcftRemoteEthFxPortRxSensitiveAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortRxSensitiveAbnormal.setStatus("current")


class _RcftRemoteEthFxPortLaserAbnormal_Type(Integer32):
    """Custom type rcftRemoteEthFxPortLaserAbnormal based on Integer32"""
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


_RcftRemoteEthFxPortLaserAbnormal_Type.__name__ = "Integer32"
_RcftRemoteEthFxPortLaserAbnormal_Object = MibTableColumn
rcftRemoteEthFxPortLaserAbnormal = _RcftRemoteEthFxPortLaserAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 8),
    _RcftRemoteEthFxPortLaserAbnormal_Type()
)
rcftRemoteEthFxPortLaserAbnormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortLaserAbnormal.setStatus("current")


class _RcftRemoteEthFxShutDown_Type(Integer32):
    """Custom type rcftRemoteEthFxShutDown based on Integer32"""
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
        *(("open", 1),
          ("close", 2),
          ("closeByFP", 3),
          ("closeByALS", 4),
          ("closeByLP", 5))
    )


_RcftRemoteEthFxShutDown_Type.__name__ = "Integer32"
_RcftRemoteEthFxShutDown_Object = MibTableColumn
rcftRemoteEthFxShutDown = _RcftRemoteEthFxShutDown_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 9),
    _RcftRemoteEthFxShutDown_Type()
)
rcftRemoteEthFxShutDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFxShutDown.setStatus("current")


class _RcftRemoteEthFxModuleType_Type(Integer32):
    """Custom type rcftRemoteEthFxModuleType based on Integer32"""
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
              12,
              15,
              100)
        )
    )
    namedValues = NamedValues(
        *(("optical-M", 1),
          ("optical-S1", 2),
          ("optical-S2", 3),
          ("optical-S3", 4),
          ("optical-SS13", 5),
          ("optical-SS15", 6),
          ("optical-SS23", 7),
          ("optical-SS25", 8),
          ("optical-SS34", 9),
          ("optical-SS35", 10),
          ("optical-S15", 12),
          ("optical-SFP", 15),
          ("unknown-type", 100))
    )


_RcftRemoteEthFxModuleType_Type.__name__ = "Integer32"
_RcftRemoteEthFxModuleType_Object = MibTableColumn
rcftRemoteEthFxModuleType = _RcftRemoteEthFxModuleType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 10),
    _RcftRemoteEthFxModuleType_Type()
)
rcftRemoteEthFxModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxModuleType.setStatus("current")


class _RcftRemoteEthFxFaultPass_Type(Integer32):
    """Custom type rcftRemoteEthFxFaultPass based on Integer32"""
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


_RcftRemoteEthFxFaultPass_Type.__name__ = "Integer32"
_RcftRemoteEthFxFaultPass_Object = MibTableColumn
rcftRemoteEthFxFaultPass = _RcftRemoteEthFxFaultPass_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 11),
    _RcftRemoteEthFxFaultPass_Type()
)
rcftRemoteEthFxFaultPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFxFaultPass.setStatus("current")


class _RcftRemoteEthFxPortLink_Type(Integer32):
    """Custom type rcftRemoteEthFxPortLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("unlink", 2))
    )


_RcftRemoteEthFxPortLink_Type.__name__ = "Integer32"
_RcftRemoteEthFxPortLink_Object = MibTableColumn
rcftRemoteEthFxPortLink = _RcftRemoteEthFxPortLink_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 12),
    _RcftRemoteEthFxPortLink_Type()
)
rcftRemoteEthFxPortLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortLink.setStatus("current")


class _RcftRemoteEthFxRxToTxFaultPass_Type(Integer32):
    """Custom type rcftRemoteEthFxRxToTxFaultPass based on Integer32"""
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


_RcftRemoteEthFxRxToTxFaultPass_Type.__name__ = "Integer32"
_RcftRemoteEthFxRxToTxFaultPass_Object = MibTableColumn
rcftRemoteEthFxRxToTxFaultPass = _RcftRemoteEthFxRxToTxFaultPass_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 13),
    _RcftRemoteEthFxRxToTxFaultPass_Type()
)
rcftRemoteEthFxRxToTxFaultPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFxRxToTxFaultPass.setStatus("current")


class _RcftRemoteEthFxTxDisabledByFR_Type(Integer32):
    """Custom type rcftRemoteEthFxTxDisabledByFR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_RcftRemoteEthFxTxDisabledByFR_Type.__name__ = "Integer32"
_RcftRemoteEthFxTxDisabledByFR_Object = MibTableColumn
rcftRemoteEthFxTxDisabledByFR = _RcftRemoteEthFxTxDisabledByFR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 14),
    _RcftRemoteEthFxTxDisabledByFR_Type()
)
rcftRemoteEthFxTxDisabledByFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxTxDisabledByFR.setStatus("current")
_RcftRemoteEthFxOrderTimeParameter_Type = Integer32
_RcftRemoteEthFxOrderTimeParameter_Object = MibTableColumn
rcftRemoteEthFxOrderTimeParameter = _RcftRemoteEthFxOrderTimeParameter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 15),
    _RcftRemoteEthFxOrderTimeParameter_Type()
)
rcftRemoteEthFxOrderTimeParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFxOrderTimeParameter.setStatus("current")
_RcftRemoteEthFxOrderModeParameter_Type = Integer32
_RcftRemoteEthFxOrderModeParameter_Object = MibTableColumn
rcftRemoteEthFxOrderModeParameter = _RcftRemoteEthFxOrderModeParameter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 16),
    _RcftRemoteEthFxOrderModeParameter_Type()
)
rcftRemoteEthFxOrderModeParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFxOrderModeParameter.setStatus("current")
_RcftRemoteEthFxOrder_Type = Integer32
_RcftRemoteEthFxOrder_Object = MibTableColumn
rcftRemoteEthFxOrder = _RcftRemoteEthFxOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 17),
    _RcftRemoteEthFxOrder_Type()
)
rcftRemoteEthFxOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFxOrder.setStatus("current")


class _RcftRemoteEthFxPortExist_Type(Integer32):
    """Custom type rcftRemoteEthFxPortExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("no-exist", 2))
    )


_RcftRemoteEthFxPortExist_Type.__name__ = "Integer32"
_RcftRemoteEthFxPortExist_Object = MibTableColumn
rcftRemoteEthFxPortExist = _RcftRemoteEthFxPortExist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 18),
    _RcftRemoteEthFxPortExist_Type()
)
rcftRemoteEthFxPortExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortExist.setStatus("current")


class _RcftRemoteEthFxPortAuto_Type(Integer32):
    """Custom type rcftRemoteEthFxPortAuto based on Integer32"""
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


_RcftRemoteEthFxPortAuto_Type.__name__ = "Integer32"
_RcftRemoteEthFxPortAuto_Object = MibTableColumn
rcftRemoteEthFxPortAuto = _RcftRemoteEthFxPortAuto_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 19),
    _RcftRemoteEthFxPortAuto_Type()
)
rcftRemoteEthFxPortAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortAuto.setStatus("current")


class _RcftRemoteEthFxModuleMaxSpeed_Type(Integer32):
    """Custom type rcftRemoteEthFxModuleMaxSpeed based on Integer32"""
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
        *(("stm16", 1),
          ("stm8", 2),
          ("stm4", 3),
          ("stm1", 4))
    )


_RcftRemoteEthFxModuleMaxSpeed_Type.__name__ = "Integer32"
_RcftRemoteEthFxModuleMaxSpeed_Object = MibTableColumn
rcftRemoteEthFxModuleMaxSpeed = _RcftRemoteEthFxModuleMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 20),
    _RcftRemoteEthFxModuleMaxSpeed_Type()
)
rcftRemoteEthFxModuleMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxModuleMaxSpeed.setStatus("current")
_RcftRemoteEthFxTranDistance_Type = Integer32
_RcftRemoteEthFxTranDistance_Object = MibTableColumn
rcftRemoteEthFxTranDistance = _RcftRemoteEthFxTranDistance_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 21),
    _RcftRemoteEthFxTranDistance_Type()
)
rcftRemoteEthFxTranDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxTranDistance.setStatus("current")
_RcftRemoteEthFxModuleWaveLen_Type = Integer32
_RcftRemoteEthFxModuleWaveLen_Object = MibTableColumn
rcftRemoteEthFxModuleWaveLen = _RcftRemoteEthFxModuleWaveLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 22),
    _RcftRemoteEthFxModuleWaveLen_Type()
)
rcftRemoteEthFxModuleWaveLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxModuleWaveLen.setStatus("current")


class _RcftRemoteEthFxPortConnectorType_Type(Integer32):
    """Custom type rcftRemoteEthFxPortConnectorType based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("unkkown", 1),
          ("rj45", 2),
          ("sc", 3),
          ("style1", 4),
          ("style2", 5),
          ("bnctnc", 6),
          ("coaheader", 7),
          ("jack", 8),
          ("lc", 9),
          ("mtrj", 10),
          ("mu", 11),
          ("sg", 12),
          ("opticalpigtail", 13),
          ("hssdc2", 14),
          ("copperpigtail", 15))
    )


_RcftRemoteEthFxPortConnectorType_Type.__name__ = "Integer32"
_RcftRemoteEthFxPortConnectorType_Object = MibTableColumn
rcftRemoteEthFxPortConnectorType = _RcftRemoteEthFxPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 23),
    _RcftRemoteEthFxPortConnectorType_Type()
)
rcftRemoteEthFxPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortConnectorType.setStatus("current")


class _RcftRemoteEthFxPortTransmitMedia_Type(Integer32):
    """Custom type rcftRemoteEthFxPortTransmitMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              15)
        )
    )
    namedValues = NamedValues(
        *(("unkkown", 1),
          ("singleMode9um", 2),
          ("multiMode50um", 3),
          ("multiMode62point5um", 4),
          ("copperline", 15))
    )


_RcftRemoteEthFxPortTransmitMedia_Type.__name__ = "Integer32"
_RcftRemoteEthFxPortTransmitMedia_Object = MibTableColumn
rcftRemoteEthFxPortTransmitMedia = _RcftRemoteEthFxPortTransmitMedia_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 24),
    _RcftRemoteEthFxPortTransmitMedia_Type()
)
rcftRemoteEthFxPortTransmitMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortTransmitMedia.setStatus("current")


class _RcftRemoteEthFxModuleManufacturer_Type(OctetString):
    """Custom type rcftRemoteEthFxModuleManufacturer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftRemoteEthFxModuleManufacturer_Type.__name__ = "OctetString"
_RcftRemoteEthFxModuleManufacturer_Object = MibTableColumn
rcftRemoteEthFxModuleManufacturer = _RcftRemoteEthFxModuleManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 25),
    _RcftRemoteEthFxModuleManufacturer_Type()
)
rcftRemoteEthFxModuleManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxModuleManufacturer.setStatus("current")


class _RcftRemoteEthFxModuleDescr_Type(OctetString):
    """Custom type rcftRemoteEthFxModuleDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftRemoteEthFxModuleDescr_Type.__name__ = "OctetString"
_RcftRemoteEthFxModuleDescr_Object = MibTableColumn
rcftRemoteEthFxModuleDescr = _RcftRemoteEthFxModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 26),
    _RcftRemoteEthFxModuleDescr_Type()
)
rcftRemoteEthFxModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxModuleDescr.setStatus("current")


class _RcftRemoteEthFxPortModuleVersion_Type(OctetString):
    """Custom type rcftRemoteEthFxPortModuleVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RcftRemoteEthFxPortModuleVersion_Type.__name__ = "OctetString"
_RcftRemoteEthFxPortModuleVersion_Object = MibTableColumn
rcftRemoteEthFxPortModuleVersion = _RcftRemoteEthFxPortModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 27),
    _RcftRemoteEthFxPortModuleVersion_Type()
)
rcftRemoteEthFxPortModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortModuleVersion.setStatus("current")


class _RcftRemoteEthFxModuleSerialNumber_Type(OctetString):
    """Custom type rcftRemoteEthFxModuleSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftRemoteEthFxModuleSerialNumber_Type.__name__ = "OctetString"
_RcftRemoteEthFxModuleSerialNumber_Object = MibTableColumn
rcftRemoteEthFxModuleSerialNumber = _RcftRemoteEthFxModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 28),
    _RcftRemoteEthFxModuleSerialNumber_Type()
)
rcftRemoteEthFxModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxModuleSerialNumber.setStatus("current")
_RcftRemoteEthFxPortSFPDiagnoInfo_Type = Integer32
_RcftRemoteEthFxPortSFPDiagnoInfo_Object = MibTableColumn
rcftRemoteEthFxPortSFPDiagnoInfo = _RcftRemoteEthFxPortSFPDiagnoInfo_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 29),
    _RcftRemoteEthFxPortSFPDiagnoInfo_Type()
)
rcftRemoteEthFxPortSFPDiagnoInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortSFPDiagnoInfo.setStatus("current")
_RcftRemoteEthFxSFPDiagnoAlarmStatus_Type = Integer32
_RcftRemoteEthFxSFPDiagnoAlarmStatus_Object = MibTableColumn
rcftRemoteEthFxSFPDiagnoAlarmStatus = _RcftRemoteEthFxSFPDiagnoAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 30),
    _RcftRemoteEthFxSFPDiagnoAlarmStatus_Type()
)
rcftRemoteEthFxSFPDiagnoAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxSFPDiagnoAlarmStatus.setStatus("current")
_RcftRemoteEthFxPortStatus_Type = Integer32
_RcftRemoteEthFxPortStatus_Object = MibTableColumn
rcftRemoteEthFxPortStatus = _RcftRemoteEthFxPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 31),
    _RcftRemoteEthFxPortStatus_Type()
)
rcftRemoteEthFxPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortStatus.setStatus("current")
_RcftRemoteEthFxUntag_Type = Integer32
_RcftRemoteEthFxUntag_Object = MibTableColumn
rcftRemoteEthFxUntag = _RcftRemoteEthFxUntag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 32),
    _RcftRemoteEthFxUntag_Type()
)
rcftRemoteEthFxUntag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFxUntag.setStatus("current")
_RcftRemoteEthFxPVID_Type = Integer32
_RcftRemoteEthFxPVID_Object = MibTableColumn
rcftRemoteEthFxPVID = _RcftRemoteEthFxPVID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 33),
    _RcftRemoteEthFxPVID_Type()
)
rcftRemoteEthFxPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPVID.setStatus("current")


class _RcftRemoteEthFxPortSFPType_Type(Integer32):
    """Custom type rcftRemoteEthFxPortSFPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("utp", 1),
          ("fiber", 2))
    )


_RcftRemoteEthFxPortSFPType_Type.__name__ = "Integer32"
_RcftRemoteEthFxPortSFPType_Object = MibTableColumn
rcftRemoteEthFxPortSFPType = _RcftRemoteEthFxPortSFPType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 34),
    _RcftRemoteEthFxPortSFPType_Type()
)
rcftRemoteEthFxPortSFPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortSFPType.setStatus("current")
_RcftRemoteEthFxPortSFPInfo_Type = Integer32
_RcftRemoteEthFxPortSFPInfo_Object = MibTableColumn
rcftRemoteEthFxPortSFPInfo = _RcftRemoteEthFxPortSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 35),
    _RcftRemoteEthFxPortSFPInfo_Type()
)
rcftRemoteEthFxPortSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortSFPInfo.setStatus("current")
_RcftRemoteEthFxPortLoopStatus_Type = Integer32
_RcftRemoteEthFxPortLoopStatus_Object = MibTableColumn
rcftRemoteEthFxPortLoopStatus = _RcftRemoteEthFxPortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 36),
    _RcftRemoteEthFxPortLoopStatus_Type()
)
rcftRemoteEthFxPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortLoopStatus.setStatus("current")
_RcftRemoteEthFxPortRxRestrictSpeed_Type = Integer32
_RcftRemoteEthFxPortRxRestrictSpeed_Object = MibTableColumn
rcftRemoteEthFxPortRxRestrictSpeed = _RcftRemoteEthFxPortRxRestrictSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 37),
    _RcftRemoteEthFxPortRxRestrictSpeed_Type()
)
rcftRemoteEthFxPortRxRestrictSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortRxRestrictSpeed.setStatus("current")
_RcftRemoteEthFxPortTxRestrictSpeed_Type = Integer32
_RcftRemoteEthFxPortTxRestrictSpeed_Object = MibTableColumn
rcftRemoteEthFxPortTxRestrictSpeed = _RcftRemoteEthFxPortTxRestrictSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 38),
    _RcftRemoteEthFxPortTxRestrictSpeed_Type()
)
rcftRemoteEthFxPortTxRestrictSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortTxRestrictSpeed.setStatus("current")
_RcftRemoteEthFxSFPDiagnoWarningStatus_Type = Integer32
_RcftRemoteEthFxSFPDiagnoWarningStatus_Object = MibTableColumn
rcftRemoteEthFxSFPDiagnoWarningStatus = _RcftRemoteEthFxSFPDiagnoWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 39),
    _RcftRemoteEthFxSFPDiagnoWarningStatus_Type()
)
rcftRemoteEthFxSFPDiagnoWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxSFPDiagnoWarningStatus.setStatus("current")
_RcftRemoteEthFxPortLineOrClient_Type = Integer32
_RcftRemoteEthFxPortLineOrClient_Object = MibTableColumn
rcftRemoteEthFxPortLineOrClient = _RcftRemoteEthFxPortLineOrClient_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 40),
    _RcftRemoteEthFxPortLineOrClient_Type()
)
rcftRemoteEthFxPortLineOrClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortLineOrClient.setStatus("current")
_RcftRemoteEthFxCOS_Type = Integer32
_RcftRemoteEthFxCOS_Object = MibTableColumn
rcftRemoteEthFxCOS = _RcftRemoteEthFxCOS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 1, 1, 41),
    _RcftRemoteEthFxCOS_Type()
)
rcftRemoteEthFxCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteEthFxCOS.setStatus("current")
_RcftRemoteEthFxStatisticTable_Object = MibTable
rcftRemoteEthFxStatisticTable = _RcftRemoteEthFxStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxStatisticTable.setStatus("current")
_RcftRemoteEthFxStatisticEntry_Object = MibTableRow
rcftRemoteEthFxStatisticEntry = _RcftRemoteEthFxStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxStatisticEntry.setStatus("current")
_RcftRemoteEthFxTxPackets_Type = Counter32
_RcftRemoteEthFxTxPackets_Object = MibTableColumn
rcftRemoteEthFxTxPackets = _RcftRemoteEthFxTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 2, 1, 1),
    _RcftRemoteEthFxTxPackets_Type()
)
rcftRemoteEthFxTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxTxPackets.setStatus("current")
_RcftRemoteEthFxTxBytes_Type = Counter32
_RcftRemoteEthFxTxBytes_Object = MibTableColumn
rcftRemoteEthFxTxBytes = _RcftRemoteEthFxTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 2, 1, 2),
    _RcftRemoteEthFxTxBytes_Type()
)
rcftRemoteEthFxTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxTxBytes.setStatus("current")
_RcftRemoteEthFxRxPackets_Type = Counter32
_RcftRemoteEthFxRxPackets_Object = MibTableColumn
rcftRemoteEthFxRxPackets = _RcftRemoteEthFxRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 2, 1, 3),
    _RcftRemoteEthFxRxPackets_Type()
)
rcftRemoteEthFxRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxRxPackets.setStatus("current")
_RcftRemoteEthFxRxBytes_Type = Counter32
_RcftRemoteEthFxRxBytes_Object = MibTableColumn
rcftRemoteEthFxRxBytes = _RcftRemoteEthFxRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 2, 1, 4),
    _RcftRemoteEthFxRxBytes_Type()
)
rcftRemoteEthFxRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxRxBytes.setStatus("current")
_RcftRemoteEthFxRxLostPackets_Type = Counter32
_RcftRemoteEthFxRxLostPackets_Object = MibTableColumn
rcftRemoteEthFxRxLostPackets = _RcftRemoteEthFxRxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 2, 1, 5),
    _RcftRemoteEthFxRxLostPackets_Type()
)
rcftRemoteEthFxRxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxRxLostPackets.setStatus("current")
_RcftRemoteEthFxFluxTimer_Type = Counter32
_RcftRemoteEthFxFluxTimer_Object = MibTableColumn
rcftRemoteEthFxFluxTimer = _RcftRemoteEthFxFluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 2, 1, 6),
    _RcftRemoteEthFxFluxTimer_Type()
)
rcftRemoteEthFxFluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxFluxTimer.setStatus("current")
_RcftRemoteEthFxTxLostPackets_Type = Counter32
_RcftRemoteEthFxTxLostPackets_Object = MibTableColumn
rcftRemoteEthFxTxLostPackets = _RcftRemoteEthFxTxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 2, 1, 7),
    _RcftRemoteEthFxTxLostPackets_Type()
)
rcftRemoteEthFxTxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxTxLostPackets.setStatus("current")
_RcftRemoteEthFx64TxBytes_Type = Counter64
_RcftRemoteEthFx64TxBytes_Object = MibTableColumn
rcftRemoteEthFx64TxBytes = _RcftRemoteEthFx64TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 2, 1, 8),
    _RcftRemoteEthFx64TxBytes_Type()
)
rcftRemoteEthFx64TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFx64TxBytes.setStatus("current")
_RcftRemoteEthFx64RxBytes_Type = Counter64
_RcftRemoteEthFx64RxBytes_Object = MibTableColumn
rcftRemoteEthFx64RxBytes = _RcftRemoteEthFx64RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 1, 2, 1, 9),
    _RcftRemoteEthFx64RxBytes_Type()
)
rcftRemoteEthFx64RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFx64RxBytes.setStatus("current")
_RcftRemoteDeviceEthFxTraps_ObjectIdentity = ObjectIdentity
rcftRemoteDeviceEthFxTraps = _RcftRemoteDeviceEthFxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2)
)
_RcftRemoteDeviceEthFxPerformance_ObjectIdentity = ObjectIdentity
rcftRemoteDeviceEthFxPerformance = _RcftRemoteDeviceEthFxPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3)
)
_RcftRemoteEthFxPortCurrentTable_Object = MibTable
rcftRemoteEthFxPortCurrentTable = _RcftRemoteEthFxPortCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortCurrentTable.setStatus("current")
_RcftRemoteEthFxPortCurrentEntry_Object = MibTableRow
rcftRemoteEthFxPortCurrentEntry = _RcftRemoteEthFxPortCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 1, 1)
)
rcftRemoteEthFxPortCurrentEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortCurrentEntry.setStatus("current")


class _RcftRemoteEthFxCurrentTemperature_Type(OctetString):
    """Custom type rcftRemoteEthFxCurrentTemperature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftRemoteEthFxCurrentTemperature_Type.__name__ = "OctetString"
_RcftRemoteEthFxCurrentTemperature_Object = MibTableColumn
rcftRemoteEthFxCurrentTemperature = _RcftRemoteEthFxCurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 1, 1, 1),
    _RcftRemoteEthFxCurrentTemperature_Type()
)
rcftRemoteEthFxCurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxCurrentTemperature.setStatus("current")


class _RcftRemoteEthFxCurrentVoltage_Type(OctetString):
    """Custom type rcftRemoteEthFxCurrentVoltage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftRemoteEthFxCurrentVoltage_Type.__name__ = "OctetString"
_RcftRemoteEthFxCurrentVoltage_Object = MibTableColumn
rcftRemoteEthFxCurrentVoltage = _RcftRemoteEthFxCurrentVoltage_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 1, 1, 2),
    _RcftRemoteEthFxCurrentVoltage_Type()
)
rcftRemoteEthFxCurrentVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxCurrentVoltage.setStatus("current")


class _RcftRemoteEthFxCurrentOffsetCurr_Type(OctetString):
    """Custom type rcftRemoteEthFxCurrentOffsetCurr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftRemoteEthFxCurrentOffsetCurr_Type.__name__ = "OctetString"
_RcftRemoteEthFxCurrentOffsetCurr_Object = MibTableColumn
rcftRemoteEthFxCurrentOffsetCurr = _RcftRemoteEthFxCurrentOffsetCurr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 1, 1, 3),
    _RcftRemoteEthFxCurrentOffsetCurr_Type()
)
rcftRemoteEthFxCurrentOffsetCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxCurrentOffsetCurr.setStatus("current")


class _RcftRemoteEthFxCurrentRecvPower_Type(OctetString):
    """Custom type rcftRemoteEthFxCurrentRecvPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftRemoteEthFxCurrentRecvPower_Type.__name__ = "OctetString"
_RcftRemoteEthFxCurrentRecvPower_Object = MibTableColumn
rcftRemoteEthFxCurrentRecvPower = _RcftRemoteEthFxCurrentRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 1, 1, 4),
    _RcftRemoteEthFxCurrentRecvPower_Type()
)
rcftRemoteEthFxCurrentRecvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxCurrentRecvPower.setStatus("current")


class _RcftRemoteEthFxCurrentSendPower_Type(OctetString):
    """Custom type rcftRemoteEthFxCurrentSendPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftRemoteEthFxCurrentSendPower_Type.__name__ = "OctetString"
_RcftRemoteEthFxCurrentSendPower_Object = MibTableColumn
rcftRemoteEthFxCurrentSendPower = _RcftRemoteEthFxCurrentSendPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 1, 1, 5),
    _RcftRemoteEthFxCurrentSendPower_Type()
)
rcftRemoteEthFxCurrentSendPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxCurrentSendPower.setStatus("current")
_RcftRemoteEthFxPortIntervalTable_Object = MibTable
rcftRemoteEthFxPortIntervalTable = _RcftRemoteEthFxPortIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortIntervalTable.setStatus("current")
_RcftRemoteEthFxPortIntervalEntry_Object = MibTableRow
rcftRemoteEthFxPortIntervalEntry = _RcftRemoteEthFxPortIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 2, 1)
)
rcftRemoteEthFxPortIntervalEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxIntervalNumber"),
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortIntervalEntry.setStatus("current")
_RcftRemoteEthFxIntervalNumber_Type = Integer32
_RcftRemoteEthFxIntervalNumber_Object = MibTableColumn
rcftRemoteEthFxIntervalNumber = _RcftRemoteEthFxIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 2, 1, 1),
    _RcftRemoteEthFxIntervalNumber_Type()
)
rcftRemoteEthFxIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxIntervalNumber.setStatus("current")


class _RcftRemoteEthFxIntervalTemperature_Type(OctetString):
    """Custom type rcftRemoteEthFxIntervalTemperature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftRemoteEthFxIntervalTemperature_Type.__name__ = "OctetString"
_RcftRemoteEthFxIntervalTemperature_Object = MibTableColumn
rcftRemoteEthFxIntervalTemperature = _RcftRemoteEthFxIntervalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 2, 1, 2),
    _RcftRemoteEthFxIntervalTemperature_Type()
)
rcftRemoteEthFxIntervalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxIntervalTemperature.setStatus("current")


class _RcftRemoteEthFxIntervalVoltage_Type(OctetString):
    """Custom type rcftRemoteEthFxIntervalVoltage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftRemoteEthFxIntervalVoltage_Type.__name__ = "OctetString"
_RcftRemoteEthFxIntervalVoltage_Object = MibTableColumn
rcftRemoteEthFxIntervalVoltage = _RcftRemoteEthFxIntervalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 2, 1, 3),
    _RcftRemoteEthFxIntervalVoltage_Type()
)
rcftRemoteEthFxIntervalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxIntervalVoltage.setStatus("current")


class _RcftRemoteEthFxIntervalOffsetCurr_Type(OctetString):
    """Custom type rcftRemoteEthFxIntervalOffsetCurr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftRemoteEthFxIntervalOffsetCurr_Type.__name__ = "OctetString"
_RcftRemoteEthFxIntervalOffsetCurr_Object = MibTableColumn
rcftRemoteEthFxIntervalOffsetCurr = _RcftRemoteEthFxIntervalOffsetCurr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 2, 1, 4),
    _RcftRemoteEthFxIntervalOffsetCurr_Type()
)
rcftRemoteEthFxIntervalOffsetCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxIntervalOffsetCurr.setStatus("current")


class _RcftRemoteEthFxIntervalRecvPower_Type(OctetString):
    """Custom type rcftRemoteEthFxIntervalRecvPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftRemoteEthFxIntervalRecvPower_Type.__name__ = "OctetString"
_RcftRemoteEthFxIntervalRecvPower_Object = MibTableColumn
rcftRemoteEthFxIntervalRecvPower = _RcftRemoteEthFxIntervalRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 2, 1, 5),
    _RcftRemoteEthFxIntervalRecvPower_Type()
)
rcftRemoteEthFxIntervalRecvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxIntervalRecvPower.setStatus("current")


class _RcftRemoteEthFxIntervalSendPower_Type(OctetString):
    """Custom type rcftRemoteEthFxIntervalSendPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftRemoteEthFxIntervalSendPower_Type.__name__ = "OctetString"
_RcftRemoteEthFxIntervalSendPower_Object = MibTableColumn
rcftRemoteEthFxIntervalSendPower = _RcftRemoteEthFxIntervalSendPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 2, 1, 6),
    _RcftRemoteEthFxIntervalSendPower_Type()
)
rcftRemoteEthFxIntervalSendPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxIntervalSendPower.setStatus("current")
_RcftRemoteEthFxPortPerTable_Object = MibTable
rcftRemoteEthFxPortPerTable = _RcftRemoteEthFxPortPerTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 3)
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortPerTable.setStatus("current")
_RcftRemoteEthFxPortPerEntry_Object = MibTableRow
rcftRemoteEthFxPortPerEntry = _RcftRemoteEthFxPortPerEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 3, 1)
)
rcftRemoteEthFxPortPerEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortPerEntry.setStatus("current")


class _RcftRemoteEthFxPortPerTemperature_Type(OctetString):
    """Custom type rcftRemoteEthFxPortPerTemperature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftRemoteEthFxPortPerTemperature_Type.__name__ = "OctetString"
_RcftRemoteEthFxPortPerTemperature_Object = MibTableColumn
rcftRemoteEthFxPortPerTemperature = _RcftRemoteEthFxPortPerTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 3, 1, 1),
    _RcftRemoteEthFxPortPerTemperature_Type()
)
rcftRemoteEthFxPortPerTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortPerTemperature.setStatus("current")


class _RcftRemoteEthFxPortPerVoltage_Type(OctetString):
    """Custom type rcftRemoteEthFxPortPerVoltage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftRemoteEthFxPortPerVoltage_Type.__name__ = "OctetString"
_RcftRemoteEthFxPortPerVoltage_Object = MibTableColumn
rcftRemoteEthFxPortPerVoltage = _RcftRemoteEthFxPortPerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 3, 1, 2),
    _RcftRemoteEthFxPortPerVoltage_Type()
)
rcftRemoteEthFxPortPerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortPerVoltage.setStatus("current")


class _RcftRemoteEthFxPortPerOffsetCurr_Type(OctetString):
    """Custom type rcftRemoteEthFxPortPerOffsetCurr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftRemoteEthFxPortPerOffsetCurr_Type.__name__ = "OctetString"
_RcftRemoteEthFxPortPerOffsetCurr_Object = MibTableColumn
rcftRemoteEthFxPortPerOffsetCurr = _RcftRemoteEthFxPortPerOffsetCurr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 3, 1, 3),
    _RcftRemoteEthFxPortPerOffsetCurr_Type()
)
rcftRemoteEthFxPortPerOffsetCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortPerOffsetCurr.setStatus("current")


class _RcftRemoteEthFxPortPerRecvPower_Type(OctetString):
    """Custom type rcftRemoteEthFxPortPerRecvPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftRemoteEthFxPortPerRecvPower_Type.__name__ = "OctetString"
_RcftRemoteEthFxPortPerRecvPower_Object = MibTableColumn
rcftRemoteEthFxPortPerRecvPower = _RcftRemoteEthFxPortPerRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 3, 1, 4),
    _RcftRemoteEthFxPortPerRecvPower_Type()
)
rcftRemoteEthFxPortPerRecvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortPerRecvPower.setStatus("current")


class _RcftRemoteEthFxPortPerSendPower_Type(OctetString):
    """Custom type rcftRemoteEthFxPortPerSendPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftRemoteEthFxPortPerSendPower_Type.__name__ = "OctetString"
_RcftRemoteEthFxPortPerSendPower_Object = MibTableColumn
rcftRemoteEthFxPortPerSendPower = _RcftRemoteEthFxPortPerSendPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 3, 3, 1, 5),
    _RcftRemoteEthFxPortPerSendPower_Type()
)
rcftRemoteEthFxPortPerSendPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortPerSendPower.setStatus("current")
_RcftRemoteDeviceE1MIB_ObjectIdentity = ObjectIdentity
rcftRemoteDeviceE1MIB = _RcftRemoteDeviceE1MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3)
)
_RcftRemoteDeviceE1Objects_ObjectIdentity = ObjectIdentity
rcftRemoteDeviceE1Objects = _RcftRemoteDeviceE1Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1)
)
_RcftRemoteDeviceE1Table_Object = MibTable
rcftRemoteDeviceE1Table = _RcftRemoteDeviceE1Table_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteDeviceE1Table.setStatus("current")
_RcftRemoteDeviceE1Entry_Object = MibTableRow
rcftRemoteDeviceE1Entry = _RcftRemoteDeviceE1Entry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1)
)
rcftRemoteDeviceE1Entry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteE1Index"),
)
if mibBuilder.loadTexts:
    rcftRemoteDeviceE1Entry.setStatus("current")
_RcftRemoteE1Index_Type = Integer32
_RcftRemoteE1Index_Object = MibTableColumn
rcftRemoteE1Index = _RcftRemoteE1Index_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 1),
    _RcftRemoteE1Index_Type()
)
rcftRemoteE1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1Index.setStatus("current")


class _RcftRemoteE1BertEnable_Type(Integer32):
    """Custom type rcftRemoteE1BertEnable based on Integer32"""
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


_RcftRemoteE1BertEnable_Type.__name__ = "Integer32"
_RcftRemoteE1BertEnable_Object = MibTableColumn
rcftRemoteE1BertEnable = _RcftRemoteE1BertEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 2),
    _RcftRemoteE1BertEnable_Type()
)
rcftRemoteE1BertEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteE1BertEnable.setStatus("current")


class _RcftRemoteE1ClockMode_Type(Integer32):
    """Custom type rcftRemoteE1ClockMode based on Integer32"""
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
        *(("master", 1),
          ("secondary", 2),
          ("transparent", 3),
          ("e1received", 4))
    )


_RcftRemoteE1ClockMode_Type.__name__ = "Integer32"
_RcftRemoteE1ClockMode_Object = MibTableColumn
rcftRemoteE1ClockMode = _RcftRemoteE1ClockMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 3),
    _RcftRemoteE1ClockMode_Type()
)
rcftRemoteE1ClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteE1ClockMode.setStatus("current")


class _RcftRemoteE1FrameEnable_Type(Integer32):
    """Custom type rcftRemoteE1FrameEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 1),
          ("pcm", 2))
    )


_RcftRemoteE1FrameEnable_Type.__name__ = "Integer32"
_RcftRemoteE1FrameEnable_Object = MibTableColumn
rcftRemoteE1FrameEnable = _RcftRemoteE1FrameEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 4),
    _RcftRemoteE1FrameEnable_Type()
)
rcftRemoteE1FrameEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteE1FrameEnable.setStatus("current")
_RcftRemoteE1AlarmStatus_Type = Integer32
_RcftRemoteE1AlarmStatus_Object = MibTableColumn
rcftRemoteE1AlarmStatus = _RcftRemoteE1AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 5),
    _RcftRemoteE1AlarmStatus_Type()
)
rcftRemoteE1AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1AlarmStatus.setStatus("current")
_RcftRemoteE1SubSpeed_Type = Unsigned32
_RcftRemoteE1SubSpeed_Object = MibTableColumn
rcftRemoteE1SubSpeed = _RcftRemoteE1SubSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 6),
    _RcftRemoteE1SubSpeed_Type()
)
rcftRemoteE1SubSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteE1SubSpeed.setStatus("current")


class _RcftRemoteE1CRCDetectEnable_Type(Integer32):
    """Custom type rcftRemoteE1CRCDetectEnable based on Integer32"""
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


_RcftRemoteE1CRCDetectEnable_Type.__name__ = "Integer32"
_RcftRemoteE1CRCDetectEnable_Object = MibTableColumn
rcftRemoteE1CRCDetectEnable = _RcftRemoteE1CRCDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 7),
    _RcftRemoteE1CRCDetectEnable_Type()
)
rcftRemoteE1CRCDetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteE1CRCDetectEnable.setStatus("current")
_RcftRemoteE1ErrCodeSecCnt_Type = Counter32
_RcftRemoteE1ErrCodeSecCnt_Object = MibTableColumn
rcftRemoteE1ErrCodeSecCnt = _RcftRemoteE1ErrCodeSecCnt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 8),
    _RcftRemoteE1ErrCodeSecCnt_Type()
)
rcftRemoteE1ErrCodeSecCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1ErrCodeSecCnt.setStatus("current")
_RcftRemoteE1SErrCodeSecCnt_Type = Counter32
_RcftRemoteE1SErrCodeSecCnt_Object = MibTableColumn
rcftRemoteE1SErrCodeSecCnt = _RcftRemoteE1SErrCodeSecCnt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 9),
    _RcftRemoteE1SErrCodeSecCnt_Type()
)
rcftRemoteE1SErrCodeSecCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1SErrCodeSecCnt.setStatus("current")


class _RcftRemoteE1TransErrorCode_Type(Integer32):
    """Custom type rcftRemoteE1TransErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("less10E-6", 1),
          ("more10E-6", 2),
          ("more10E-3", 3))
    )


_RcftRemoteE1TransErrorCode_Type.__name__ = "Integer32"
_RcftRemoteE1TransErrorCode_Object = MibTableColumn
rcftRemoteE1TransErrorCode = _RcftRemoteE1TransErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 10),
    _RcftRemoteE1TransErrorCode_Type()
)
rcftRemoteE1TransErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1TransErrorCode.setStatus("current")


class _RcftRemoteE1CRCStatus_Type(Integer32):
    """Custom type rcftRemoteE1CRCStatus based on Integer32"""
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


_RcftRemoteE1CRCStatus_Type.__name__ = "Integer32"
_RcftRemoteE1CRCStatus_Object = MibTableColumn
rcftRemoteE1CRCStatus = _RcftRemoteE1CRCStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 11),
    _RcftRemoteE1CRCStatus_Type()
)
rcftRemoteE1CRCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1CRCStatus.setStatus("current")


class _RcftRemoteE1FaultPass_Type(Integer32):
    """Custom type rcftRemoteE1FaultPass based on Integer32"""
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


_RcftRemoteE1FaultPass_Type.__name__ = "Integer32"
_RcftRemoteE1FaultPass_Object = MibTableColumn
rcftRemoteE1FaultPass = _RcftRemoteE1FaultPass_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 12),
    _RcftRemoteE1FaultPass_Type()
)
rcftRemoteE1FaultPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteE1FaultPass.setStatus("current")


class _RcftRemoteE1LocalLoopEn_Type(Integer32):
    """Custom type rcftRemoteE1LocalLoopEn based on Integer32"""
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


_RcftRemoteE1LocalLoopEn_Type.__name__ = "Integer32"
_RcftRemoteE1LocalLoopEn_Object = MibTableColumn
rcftRemoteE1LocalLoopEn = _RcftRemoteE1LocalLoopEn_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 13),
    _RcftRemoteE1LocalLoopEn_Type()
)
rcftRemoteE1LocalLoopEn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1LocalLoopEn.setStatus("current")


class _RcftRemoteE1Location_Type(Integer32):
    """Custom type rcftRemoteE1Location based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("e1-1", 1),
          ("e1-2", 2),
          ("e1-3", 3),
          ("e1-4", 4),
          ("e1-5", 5),
          ("e1-6", 6),
          ("e1-7", 7),
          ("e1-8", 8),
          ("unknown", 100))
    )


_RcftRemoteE1Location_Type.__name__ = "Integer32"
_RcftRemoteE1Location_Object = MibTableColumn
rcftRemoteE1Location = _RcftRemoteE1Location_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 14),
    _RcftRemoteE1Location_Type()
)
rcftRemoteE1Location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteE1Location.setStatus("current")


class _RcftRemoteE1FoundLink_Type(Integer32):
    """Custom type rcftRemoteE1FoundLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failForDelay", 2),
          ("failForOtherReason", 100))
    )


_RcftRemoteE1FoundLink_Type.__name__ = "Integer32"
_RcftRemoteE1FoundLink_Object = MibTableColumn
rcftRemoteE1FoundLink = _RcftRemoteE1FoundLink_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 15),
    _RcftRemoteE1FoundLink_Type()
)
rcftRemoteE1FoundLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1FoundLink.setStatus("current")


class _RcftRemoteE1UnUsed_Type(Integer32):
    """Custom type rcftRemoteE1UnUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unused", 1),
          ("used", 2))
    )


_RcftRemoteE1UnUsed_Type.__name__ = "Integer32"
_RcftRemoteE1UnUsed_Object = MibTableColumn
rcftRemoteE1UnUsed = _RcftRemoteE1UnUsed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 16),
    _RcftRemoteE1UnUsed_Type()
)
rcftRemoteE1UnUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteE1UnUsed.setStatus("current")
_RcftRemoteToLocalE1AlarmStatus_Type = Integer32
_RcftRemoteToLocalE1AlarmStatus_Object = MibTableColumn
rcftRemoteToLocalE1AlarmStatus = _RcftRemoteToLocalE1AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 17),
    _RcftRemoteToLocalE1AlarmStatus_Type()
)
rcftRemoteToLocalE1AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteToLocalE1AlarmStatus.setStatus("current")


class _RcftRemoteE1Balance_Type(Integer32):
    """Custom type rcftRemoteE1Balance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("balance", 1),
          ("imbalance", 2))
    )


_RcftRemoteE1Balance_Type.__name__ = "Integer32"
_RcftRemoteE1Balance_Object = MibTableColumn
rcftRemoteE1Balance = _RcftRemoteE1Balance_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 18),
    _RcftRemoteE1Balance_Type()
)
rcftRemoteE1Balance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1Balance.setStatus("current")
_RcftRemoteE1PortStatus_Type = Integer32
_RcftRemoteE1PortStatus_Object = MibTableColumn
rcftRemoteE1PortStatus = _RcftRemoteE1PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 19),
    _RcftRemoteE1PortStatus_Type()
)
rcftRemoteE1PortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteE1PortStatus.setStatus("current")
_RcftRemoteE1PortTS0Mode_Type = Integer32
_RcftRemoteE1PortTS0Mode_Object = MibTableColumn
rcftRemoteE1PortTS0Mode = _RcftRemoteE1PortTS0Mode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 20),
    _RcftRemoteE1PortTS0Mode_Type()
)
rcftRemoteE1PortTS0Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteE1PortTS0Mode.setStatus("current")
_RcftRemoteE1PortIdleCode_Type = Integer32
_RcftRemoteE1PortIdleCode_Object = MibTableColumn
rcftRemoteE1PortIdleCode = _RcftRemoteE1PortIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 21),
    _RcftRemoteE1PortIdleCode_Type()
)
rcftRemoteE1PortIdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteE1PortIdleCode.setStatus("current")


class _RcftRemoteE1LoopStatus_Type(Integer32):
    """Custom type rcftRemoteE1LoopStatus based on Integer32"""
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
        *(("localDoubleLoopEnable", 1),
          ("localDoubleLoopDisable", 2),
          ("remoteDoubleLoopEnable", 3),
          ("remoteDoubleLoopDisable", 4))
    )


_RcftRemoteE1LoopStatus_Type.__name__ = "Integer32"
_RcftRemoteE1LoopStatus_Object = MibTableColumn
rcftRemoteE1LoopStatus = _RcftRemoteE1LoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 22),
    _RcftRemoteE1LoopStatus_Type()
)
rcftRemoteE1LoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1LoopStatus.setStatus("current")
_RcftRemoteE1OrderTimeParameter_Type = Integer32
_RcftRemoteE1OrderTimeParameter_Object = MibTableColumn
rcftRemoteE1OrderTimeParameter = _RcftRemoteE1OrderTimeParameter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 23),
    _RcftRemoteE1OrderTimeParameter_Type()
)
rcftRemoteE1OrderTimeParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteE1OrderTimeParameter.setStatus("current")
_RcftRemoteE1OrderModeParameter_Type = Integer32
_RcftRemoteE1OrderModeParameter_Object = MibTableColumn
rcftRemoteE1OrderModeParameter = _RcftRemoteE1OrderModeParameter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 24),
    _RcftRemoteE1OrderModeParameter_Type()
)
rcftRemoteE1OrderModeParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteE1OrderModeParameter.setStatus("current")
_RcftRemoteE1Order_Type = Integer32
_RcftRemoteE1Order_Object = MibTableColumn
rcftRemoteE1Order = _RcftRemoteE1Order_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 25),
    _RcftRemoteE1Order_Type()
)
rcftRemoteE1Order.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteE1Order.setStatus("current")
_RcftRemoteE1PortType_Type = Integer32
_RcftRemoteE1PortType_Object = MibTableColumn
rcftRemoteE1PortType = _RcftRemoteE1PortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 26),
    _RcftRemoteE1PortType_Type()
)
rcftRemoteE1PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1PortType.setStatus("current")
_RcftRemoteE1BertStatus_Type = Integer32
_RcftRemoteE1BertStatus_Object = MibTableColumn
rcftRemoteE1BertStatus = _RcftRemoteE1BertStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 27),
    _RcftRemoteE1BertStatus_Type()
)
rcftRemoteE1BertStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteE1BertStatus.setStatus("current")
_RcftRemoteE1BertTime_Type = Unsigned32
_RcftRemoteE1BertTime_Object = MibTableColumn
rcftRemoteE1BertTime = _RcftRemoteE1BertTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 28),
    _RcftRemoteE1BertTime_Type()
)
rcftRemoteE1BertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1BertTime.setStatus("current")
_RcftRemoteE1BertErrCode_Type = Unsigned32
_RcftRemoteE1BertErrCode_Object = MibTableColumn
rcftRemoteE1BertErrCode = _RcftRemoteE1BertErrCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 29),
    _RcftRemoteE1BertErrCode_Type()
)
rcftRemoteE1BertErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1BertErrCode.setStatus("current")
_RcftRemoteE1BertUnusedTime_Type = Unsigned32
_RcftRemoteE1BertUnusedTime_Object = MibTableColumn
rcftRemoteE1BertUnusedTime = _RcftRemoteE1BertUnusedTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 30),
    _RcftRemoteE1BertUnusedTime_Type()
)
rcftRemoteE1BertUnusedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1BertUnusedTime.setStatus("current")
_RcftRemoteE1BertPortSpeed_Type = Unsigned32
_RcftRemoteE1BertPortSpeed_Object = MibTableColumn
rcftRemoteE1BertPortSpeed = _RcftRemoteE1BertPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 31),
    _RcftRemoteE1BertPortSpeed_Type()
)
rcftRemoteE1BertPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1BertPortSpeed.setStatus("current")
_RcftRemoteE1BertCodeType_Type = Integer32
_RcftRemoteE1BertCodeType_Object = MibTableColumn
rcftRemoteE1BertCodeType = _RcftRemoteE1BertCodeType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 32),
    _RcftRemoteE1BertCodeType_Type()
)
rcftRemoteE1BertCodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteE1BertCodeType.setStatus("current")
_RcftRemoteE1BertCodeNum_Type = Integer32
_RcftRemoteE1BertCodeNum_Object = MibTableColumn
rcftRemoteE1BertCodeNum = _RcftRemoteE1BertCodeNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 33),
    _RcftRemoteE1BertCodeNum_Type()
)
rcftRemoteE1BertCodeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteE1BertCodeNum.setStatus("current")
_RcftRemoteE1LoopSwitchStatus_Type = Integer32
_RcftRemoteE1LoopSwitchStatus_Object = MibTableColumn
rcftRemoteE1LoopSwitchStatus = _RcftRemoteE1LoopSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 34),
    _RcftRemoteE1LoopSwitchStatus_Type()
)
rcftRemoteE1LoopSwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1LoopSwitchStatus.setStatus("current")
_RcftRemoteE1AlarmRejest_Type = Integer32
_RcftRemoteE1AlarmRejest_Object = MibTableColumn
rcftRemoteE1AlarmRejest = _RcftRemoteE1AlarmRejest_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 35),
    _RcftRemoteE1AlarmRejest_Type()
)
rcftRemoteE1AlarmRejest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1AlarmRejest.setStatus("current")
_RcftRemoteT1AlarmStatus_Type = Integer32
_RcftRemoteT1AlarmStatus_Object = MibTableColumn
rcftRemoteT1AlarmStatus = _RcftRemoteT1AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 36),
    _RcftRemoteT1AlarmStatus_Type()
)
rcftRemoteT1AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteT1AlarmStatus.setStatus("current")
_RcftRemoteE1PortVCGNumber_Type = Integer32
_RcftRemoteE1PortVCGNumber_Object = MibTableColumn
rcftRemoteE1PortVCGNumber = _RcftRemoteE1PortVCGNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 37),
    _RcftRemoteE1PortVCGNumber_Type()
)
rcftRemoteE1PortVCGNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1PortVCGNumber.setStatus("current")
_RcftRemoteE1ToLNumber_Type = Integer32
_RcftRemoteE1ToLNumber_Object = MibTableColumn
rcftRemoteE1ToLNumber = _RcftRemoteE1ToLNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 38),
    _RcftRemoteE1ToLNumber_Type()
)
rcftRemoteE1ToLNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1ToLNumber.setStatus("current")
_RcftRemoteE1CVCnt_Type = Integer32
_RcftRemoteE1CVCnt_Object = MibTableColumn
rcftRemoteE1CVCnt = _RcftRemoteE1CVCnt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 1, 1, 39),
    _RcftRemoteE1CVCnt_Type()
)
rcftRemoteE1CVCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1CVCnt.setStatus("current")
_RcftRemoteE1StatisticTable_Object = MibTable
rcftRemoteE1StatisticTable = _RcftRemoteE1StatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 2)
)
if mibBuilder.loadTexts:
    rcftRemoteE1StatisticTable.setStatus("current")
_RcftRemoteE1StatisticEntry_Object = MibTableRow
rcftRemoteE1StatisticEntry = _RcftRemoteE1StatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteE1StatisticEntry.setStatus("current")
_RcftRemoteE1TxPackets_Type = Counter32
_RcftRemoteE1TxPackets_Object = MibTableColumn
rcftRemoteE1TxPackets = _RcftRemoteE1TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 2, 1, 1),
    _RcftRemoteE1TxPackets_Type()
)
rcftRemoteE1TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1TxPackets.setStatus("current")
_RcftRemoteE1TxBytes_Type = Counter32
_RcftRemoteE1TxBytes_Object = MibTableColumn
rcftRemoteE1TxBytes = _RcftRemoteE1TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 2, 1, 2),
    _RcftRemoteE1TxBytes_Type()
)
rcftRemoteE1TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1TxBytes.setStatus("current")
_RcftRemoteE1RxPackets_Type = Counter32
_RcftRemoteE1RxPackets_Object = MibTableColumn
rcftRemoteE1RxPackets = _RcftRemoteE1RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 2, 1, 3),
    _RcftRemoteE1RxPackets_Type()
)
rcftRemoteE1RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1RxPackets.setStatus("current")
_RcftRemoteE1RxBytes_Type = Counter32
_RcftRemoteE1RxBytes_Object = MibTableColumn
rcftRemoteE1RxBytes = _RcftRemoteE1RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 2, 1, 4),
    _RcftRemoteE1RxBytes_Type()
)
rcftRemoteE1RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1RxBytes.setStatus("current")
_RcftRemoteE1RxERRPackets_Type = Counter32
_RcftRemoteE1RxERRPackets_Object = MibTableColumn
rcftRemoteE1RxERRPackets = _RcftRemoteE1RxERRPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 2, 1, 5),
    _RcftRemoteE1RxERRPackets_Type()
)
rcftRemoteE1RxERRPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1RxERRPackets.setStatus("current")
_RcftRemoteE1FluxTimer_Type = Counter32
_RcftRemoteE1FluxTimer_Object = MibTableColumn
rcftRemoteE1FluxTimer = _RcftRemoteE1FluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 2, 1, 6),
    _RcftRemoteE1FluxTimer_Type()
)
rcftRemoteE1FluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1FluxTimer.setStatus("current")
_RcftRemoteE1LANTxPackets_Type = Counter32
_RcftRemoteE1LANTxPackets_Object = MibTableColumn
rcftRemoteE1LANTxPackets = _RcftRemoteE1LANTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 2, 1, 7),
    _RcftRemoteE1LANTxPackets_Type()
)
rcftRemoteE1LANTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1LANTxPackets.setStatus("current")
_RcftRemoteE1LANRxPackets_Type = Counter32
_RcftRemoteE1LANRxPackets_Object = MibTableColumn
rcftRemoteE1LANRxPackets = _RcftRemoteE1LANRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 2, 1, 8),
    _RcftRemoteE1LANRxPackets_Type()
)
rcftRemoteE1LANRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1LANRxPackets.setStatus("current")
_RcftRemoteE1LANRxLosPackets_Type = Counter32
_RcftRemoteE1LANRxLosPackets_Object = MibTableColumn
rcftRemoteE1LANRxLosPackets = _RcftRemoteE1LANRxLosPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 1, 2, 1, 9),
    _RcftRemoteE1LANRxLosPackets_Type()
)
rcftRemoteE1LANRxLosPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteE1LANRxLosPackets.setStatus("current")
_RcftRemoteDeviceE1Traps_ObjectIdentity = ObjectIdentity
rcftRemoteDeviceE1Traps = _RcftRemoteDeviceE1Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 2)
)
_RcftRemoteDeviceSHDSLMIB_ObjectIdentity = ObjectIdentity
rcftRemoteDeviceSHDSLMIB = _RcftRemoteDeviceSHDSLMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4)
)
_RcftRemoteSHDSLPortObjects_ObjectIdentity = ObjectIdentity
rcftRemoteSHDSLPortObjects = _RcftRemoteSHDSLPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1)
)
_RcftRemoteSHDSLPortTable_Object = MibTable
rcftRemoteSHDSLPortTable = _RcftRemoteSHDSLPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortTable.setStatus("current")
_RcftRemoteSHDSLPortEntry_Object = MibTableRow
rcftRemoteSHDSLPortEntry = _RcftRemoteSHDSLPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1)
)
rcftRemoteSHDSLPortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteSHDSLPortIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortEntry.setStatus("current")
_RcftRemoteSHDSLPortIndex_Type = Integer32
_RcftRemoteSHDSLPortIndex_Object = MibTableColumn
rcftRemoteSHDSLPortIndex = _RcftRemoteSHDSLPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 1),
    _RcftRemoteSHDSLPortIndex_Type()
)
rcftRemoteSHDSLPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIndex.setStatus("current")
_RcftRemoteSHDSLPortAlarmStatus_Type = Integer32
_RcftRemoteSHDSLPortAlarmStatus_Object = MibTableColumn
rcftRemoteSHDSLPortAlarmStatus = _RcftRemoteSHDSLPortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 2),
    _RcftRemoteSHDSLPortAlarmStatus_Type()
)
rcftRemoteSHDSLPortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortAlarmStatus.setStatus("current")
_RcftRemoteSHDSLPortStatus_Type = Integer32
_RcftRemoteSHDSLPortStatus_Object = MibTableColumn
rcftRemoteSHDSLPortStatus = _RcftRemoteSHDSLPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 3),
    _RcftRemoteSHDSLPortStatus_Type()
)
rcftRemoteSHDSLPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortStatus.setStatus("current")
_RcftRemoteSHDSLPortCapableSpeed_Type = Integer32
_RcftRemoteSHDSLPortCapableSpeed_Object = MibTableColumn
rcftRemoteSHDSLPortCapableSpeed = _RcftRemoteSHDSLPortCapableSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 4),
    _RcftRemoteSHDSLPortCapableSpeed_Type()
)
rcftRemoteSHDSLPortCapableSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCapableSpeed.setStatus("current")
_RcftRemoteSHDSLPortWorkSpeed_Type = Integer32
_RcftRemoteSHDSLPortWorkSpeed_Object = MibTableColumn
rcftRemoteSHDSLPortWorkSpeed = _RcftRemoteSHDSLPortWorkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 5),
    _RcftRemoteSHDSLPortWorkSpeed_Type()
)
rcftRemoteSHDSLPortWorkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortWorkSpeed.setStatus("current")
_RcftRemoteSHDSLPortProbeMaxSpeed_Type = Integer32
_RcftRemoteSHDSLPortProbeMaxSpeed_Object = MibTableColumn
rcftRemoteSHDSLPortProbeMaxSpeed = _RcftRemoteSHDSLPortProbeMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 6),
    _RcftRemoteSHDSLPortProbeMaxSpeed_Type()
)
rcftRemoteSHDSLPortProbeMaxSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortProbeMaxSpeed.setStatus("current")
_RcftRemoteSHDSLPortProbeMinSpeed_Type = Integer32
_RcftRemoteSHDSLPortProbeMinSpeed_Object = MibTableColumn
rcftRemoteSHDSLPortProbeMinSpeed = _RcftRemoteSHDSLPortProbeMinSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 7),
    _RcftRemoteSHDSLPortProbeMinSpeed_Type()
)
rcftRemoteSHDSLPortProbeMinSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortProbeMinSpeed.setStatus("current")
_RcftRemoteSDHSLPortSNR_Type = Integer32
_RcftRemoteSDHSLPortSNR_Object = MibTableColumn
rcftRemoteSDHSLPortSNR = _RcftRemoteSDHSLPortSNR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 8),
    _RcftRemoteSDHSLPortSNR_Type()
)
rcftRemoteSDHSLPortSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSDHSLPortSNR.setStatus("current")
_RcftRemoteSHDSLPortConfigSNR_Type = Integer32
_RcftRemoteSHDSLPortConfigSNR_Object = MibTableColumn
rcftRemoteSHDSLPortConfigSNR = _RcftRemoteSHDSLPortConfigSNR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 9),
    _RcftRemoteSHDSLPortConfigSNR_Type()
)
rcftRemoteSHDSLPortConfigSNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortConfigSNR.setStatus("current")
_RcftRemoteSHDSLPortSNRThreshold_Type = Integer32
_RcftRemoteSHDSLPortSNRThreshold_Object = MibTableColumn
rcftRemoteSHDSLPortSNRThreshold = _RcftRemoteSHDSLPortSNRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 10),
    _RcftRemoteSHDSLPortSNRThreshold_Type()
)
rcftRemoteSHDSLPortSNRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortSNRThreshold.setStatus("current")
_RcftRemoteSHDSLPortAttenuation_Type = Integer32
_RcftRemoteSHDSLPortAttenuation_Object = MibTableColumn
rcftRemoteSHDSLPortAttenuation = _RcftRemoteSHDSLPortAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 11),
    _RcftRemoteSHDSLPortAttenuation_Type()
)
rcftRemoteSHDSLPortAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortAttenuation.setStatus("current")
_RcftRemoteSHDSLPortAttenuationThreshold_Type = Integer32
_RcftRemoteSHDSLPortAttenuationThreshold_Object = MibTableColumn
rcftRemoteSHDSLPortAttenuationThreshold = _RcftRemoteSHDSLPortAttenuationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 12),
    _RcftRemoteSHDSLPortAttenuationThreshold_Type()
)
rcftRemoteSHDSLPortAttenuationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortAttenuationThreshold.setStatus("current")
_RcftRemoteSHDSLPortPBO_Type = Integer32
_RcftRemoteSHDSLPortPBO_Object = MibTableColumn
rcftRemoteSHDSLPortPBO = _RcftRemoteSHDSLPortPBO_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 13),
    _RcftRemoteSHDSLPortPBO_Type()
)
rcftRemoteSHDSLPortPBO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortPBO.setStatus("current")
_RcftRemoteSHDSLPortLOSThreshold_Type = Integer32
_RcftRemoteSHDSLPortLOSThreshold_Object = MibTableColumn
rcftRemoteSHDSLPortLOSThreshold = _RcftRemoteSHDSLPortLOSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 14),
    _RcftRemoteSHDSLPortLOSThreshold_Type()
)
rcftRemoteSHDSLPortLOSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortLOSThreshold.setStatus("current")
_RcftRemoteSHDSLPortLOSWThreshold_Type = Integer32
_RcftRemoteSHDSLPortLOSWThreshold_Object = MibTableColumn
rcftRemoteSHDSLPortLOSWThreshold = _RcftRemoteSHDSLPortLOSWThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 15),
    _RcftRemoteSHDSLPortLOSWThreshold_Type()
)
rcftRemoteSHDSLPortLOSWThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortLOSWThreshold.setStatus("current")
_RcftRemoteSHDSLPortLOLKThreshold_Type = Integer32
_RcftRemoteSHDSLPortLOLKThreshold_Object = MibTableColumn
rcftRemoteSHDSLPortLOLKThreshold = _RcftRemoteSHDSLPortLOLKThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 16),
    _RcftRemoteSHDSLPortLOLKThreshold_Type()
)
rcftRemoteSHDSLPortLOLKThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortLOLKThreshold.setStatus("current")
_RcftRemoteSHDSLPortESThreshold_Type = Integer32
_RcftRemoteSHDSLPortESThreshold_Object = MibTableColumn
rcftRemoteSHDSLPortESThreshold = _RcftRemoteSHDSLPortESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 17),
    _RcftRemoteSHDSLPortESThreshold_Type()
)
rcftRemoteSHDSLPortESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortESThreshold.setStatus("current")


class _RcftRemoteSHDSLPortLoopStatus_Type(Integer32):
    """Custom type rcftRemoteSHDSLPortLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("insideLoop", 1),
          ("outsideLoop", 2),
          ("doubleloop", 3),
          ("normal", 100))
    )


_RcftRemoteSHDSLPortLoopStatus_Type.__name__ = "Integer32"
_RcftRemoteSHDSLPortLoopStatus_Object = MibTableColumn
rcftRemoteSHDSLPortLoopStatus = _RcftRemoteSHDSLPortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 18),
    _RcftRemoteSHDSLPortLoopStatus_Type()
)
rcftRemoteSHDSLPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortLoopStatus.setStatus("current")
_RcftRemoteSHDSLPortAttenuationInitThreshhold_Type = Integer32
_RcftRemoteSHDSLPortAttenuationInitThreshhold_Object = MibTableColumn
rcftRemoteSHDSLPortAttenuationInitThreshhold = _RcftRemoteSHDSLPortAttenuationInitThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 19),
    _RcftRemoteSHDSLPortAttenuationInitThreshhold_Type()
)
rcftRemoteSHDSLPortAttenuationInitThreshhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortAttenuationInitThreshhold.setStatus("current")
_RcftRemoteSHDSLPortOrderTimeParameter_Type = Integer32
_RcftRemoteSHDSLPortOrderTimeParameter_Object = MibTableColumn
rcftRemoteSHDSLPortOrderTimeParameter = _RcftRemoteSHDSLPortOrderTimeParameter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 20),
    _RcftRemoteSHDSLPortOrderTimeParameter_Type()
)
rcftRemoteSHDSLPortOrderTimeParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortOrderTimeParameter.setStatus("current")
_RcftRemoteSHDSLPortOrderModeParameter_Type = Integer32
_RcftRemoteSHDSLPortOrderModeParameter_Object = MibTableColumn
rcftRemoteSHDSLPortOrderModeParameter = _RcftRemoteSHDSLPortOrderModeParameter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 21),
    _RcftRemoteSHDSLPortOrderModeParameter_Type()
)
rcftRemoteSHDSLPortOrderModeParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortOrderModeParameter.setStatus("current")
_RcftRemoteSHDSLPortOrder_Type = Integer32
_RcftRemoteSHDSLPortOrder_Object = MibTableColumn
rcftRemoteSHDSLPortOrder = _RcftRemoteSHDSLPortOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 22),
    _RcftRemoteSHDSLPortOrder_Type()
)
rcftRemoteSHDSLPortOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortOrder.setStatus("current")
_RcftRemoteSHDSLPortPBOAmount_Type = Integer32
_RcftRemoteSHDSLPortPBOAmount_Object = MibTableColumn
rcftRemoteSHDSLPortPBOAmount = _RcftRemoteSHDSLPortPBOAmount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 23),
    _RcftRemoteSHDSLPortPBOAmount_Type()
)
rcftRemoteSHDSLPortPBOAmount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortPBOAmount.setStatus("current")
_RcftRemoteSHDSLBertStatus_Type = Integer32
_RcftRemoteSHDSLBertStatus_Object = MibTableColumn
rcftRemoteSHDSLBertStatus = _RcftRemoteSHDSLBertStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 24),
    _RcftRemoteSHDSLBertStatus_Type()
)
rcftRemoteSHDSLBertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLBertStatus.setStatus("current")
_RcftRemoteSHDSLBertTime_Type = Unsigned32
_RcftRemoteSHDSLBertTime_Object = MibTableColumn
rcftRemoteSHDSLBertTime = _RcftRemoteSHDSLBertTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 25),
    _RcftRemoteSHDSLBertTime_Type()
)
rcftRemoteSHDSLBertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLBertTime.setStatus("current")
_RcftRemoteSHDSLBertErrCode_Type = Unsigned32
_RcftRemoteSHDSLBertErrCode_Object = MibTableColumn
rcftRemoteSHDSLBertErrCode = _RcftRemoteSHDSLBertErrCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 26),
    _RcftRemoteSHDSLBertErrCode_Type()
)
rcftRemoteSHDSLBertErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLBertErrCode.setStatus("current")
_RcftRemoteSHDSLBertUnusedTime_Type = Unsigned32
_RcftRemoteSHDSLBertUnusedTime_Object = MibTableColumn
rcftRemoteSHDSLBertUnusedTime = _RcftRemoteSHDSLBertUnusedTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 27),
    _RcftRemoteSHDSLBertUnusedTime_Type()
)
rcftRemoteSHDSLBertUnusedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLBertUnusedTime.setStatus("current")
_RcftRemoteSHDSLBertPortSpeed_Type = Unsigned32
_RcftRemoteSHDSLBertPortSpeed_Object = MibTableColumn
rcftRemoteSHDSLBertPortSpeed = _RcftRemoteSHDSLBertPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 28),
    _RcftRemoteSHDSLBertPortSpeed_Type()
)
rcftRemoteSHDSLBertPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLBertPortSpeed.setStatus("current")
_RcftRemoteSHDSLBertCodeType_Type = Integer32
_RcftRemoteSHDSLBertCodeType_Object = MibTableColumn
rcftRemoteSHDSLBertCodeType = _RcftRemoteSHDSLBertCodeType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 29),
    _RcftRemoteSHDSLBertCodeType_Type()
)
rcftRemoteSHDSLBertCodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLBertCodeType.setStatus("current")
_RcftRemoteSHDSLBertCodeNum_Type = Integer32
_RcftRemoteSHDSLBertCodeNum_Object = MibTableColumn
rcftRemoteSHDSLBertCodeNum = _RcftRemoteSHDSLBertCodeNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 30),
    _RcftRemoteSHDSLBertCodeNum_Type()
)
rcftRemoteSHDSLBertCodeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLBertCodeNum.setStatus("current")


class _RcftRemoteSHDSLLoopStatus_Type(Integer32):
    """Custom type rcftRemoteSHDSLLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("localDoubleLoopEnable", 1),
          ("localDoubleLoopDisable", 2),
          ("remoteDoubleLoopEnable", 3),
          ("remoteDoubleLoopDisable", 4),
          ("normal", 5),
          ("localInSideLoopEnale", 6),
          ("localOutSideLoopEnable", 7))
    )


_RcftRemoteSHDSLLoopStatus_Type.__name__ = "Integer32"
_RcftRemoteSHDSLLoopStatus_Object = MibTableColumn
rcftRemoteSHDSLLoopStatus = _RcftRemoteSHDSLLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 1, 1, 1, 31),
    _RcftRemoteSHDSLLoopStatus_Type()
)
rcftRemoteSHDSLLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLLoopStatus.setStatus("current")
_RcftRemoteSHDSLPortPerformance_ObjectIdentity = ObjectIdentity
rcftRemoteSHDSLPortPerformance = _RcftRemoteSHDSLPortPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2)
)
_RcftRemoteSHDSLPortCurrentTable_Object = MibTable
rcftRemoteSHDSLPortCurrentTable = _RcftRemoteSHDSLPortCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentTable.setStatus("current")
_RcftRemoteSHDSLPortCurrentEntry_Object = MibTableRow
rcftRemoteSHDSLPortCurrentEntry = _RcftRemoteSHDSLPortCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 1, 1)
)
rcftRemoteSHDSLPortCurrentEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteSHDSLPortIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentEntry.setStatus("current")
_RcftRemoteSHDSLPortCurrentLOSTimes_Type = Integer32
_RcftRemoteSHDSLPortCurrentLOSTimes_Object = MibTableColumn
rcftRemoteSHDSLPortCurrentLOSTimes = _RcftRemoteSHDSLPortCurrentLOSTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 1, 1, 1),
    _RcftRemoteSHDSLPortCurrentLOSTimes_Type()
)
rcftRemoteSHDSLPortCurrentLOSTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentLOSTimes.setStatus("current")
_RcftRemoteSHDSLPortCurrentLOSWTimes_Type = Integer32
_RcftRemoteSHDSLPortCurrentLOSWTimes_Object = MibTableColumn
rcftRemoteSHDSLPortCurrentLOSWTimes = _RcftRemoteSHDSLPortCurrentLOSWTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 1, 1, 2),
    _RcftRemoteSHDSLPortCurrentLOSWTimes_Type()
)
rcftRemoteSHDSLPortCurrentLOSWTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentLOSWTimes.setStatus("current")
_RcftRemoteSHDSLPortCurrentLOLKTimes_Type = Integer32
_RcftRemoteSHDSLPortCurrentLOLKTimes_Object = MibTableColumn
rcftRemoteSHDSLPortCurrentLOLKTimes = _RcftRemoteSHDSLPortCurrentLOLKTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 1, 1, 3),
    _RcftRemoteSHDSLPortCurrentLOLKTimes_Type()
)
rcftRemoteSHDSLPortCurrentLOLKTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentLOLKTimes.setStatus("current")
_RcftRemoteSHDSLPortCurrentCVTimes_Type = Integer32
_RcftRemoteSHDSLPortCurrentCVTimes_Object = MibTableColumn
rcftRemoteSHDSLPortCurrentCVTimes = _RcftRemoteSHDSLPortCurrentCVTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 1, 1, 4),
    _RcftRemoteSHDSLPortCurrentCVTimes_Type()
)
rcftRemoteSHDSLPortCurrentCVTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentCVTimes.setStatus("current")
_RcftRemoteSHDSLPortCurrentES_Type = Integer32
_RcftRemoteSHDSLPortCurrentES_Object = MibTableColumn
rcftRemoteSHDSLPortCurrentES = _RcftRemoteSHDSLPortCurrentES_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 1, 1, 5),
    _RcftRemoteSHDSLPortCurrentES_Type()
)
rcftRemoteSHDSLPortCurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentES.setStatus("current")
_RcftRemoteSHDSLPortCurrentSES_Type = Integer32
_RcftRemoteSHDSLPortCurrentSES_Object = MibTableColumn
rcftRemoteSHDSLPortCurrentSES = _RcftRemoteSHDSLPortCurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 1, 1, 6),
    _RcftRemoteSHDSLPortCurrentSES_Type()
)
rcftRemoteSHDSLPortCurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentSES.setStatus("current")
_RcftRemoteSHDSLPortCurrentUAS_Type = Integer32
_RcftRemoteSHDSLPortCurrentUAS_Object = MibTableColumn
rcftRemoteSHDSLPortCurrentUAS = _RcftRemoteSHDSLPortCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 1, 1, 7),
    _RcftRemoteSHDSLPortCurrentUAS_Type()
)
rcftRemoteSHDSLPortCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentUAS.setStatus("current")
_RcftRemoteSHDSLPortCurrentLOSWS_Type = Integer32
_RcftRemoteSHDSLPortCurrentLOSWS_Object = MibTableColumn
rcftRemoteSHDSLPortCurrentLOSWS = _RcftRemoteSHDSLPortCurrentLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 1, 1, 8),
    _RcftRemoteSHDSLPortCurrentLOSWS_Type()
)
rcftRemoteSHDSLPortCurrentLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentLOSWS.setStatus("current")
_RcftRemoteSHDSLPortCurrentCRCTimes_Type = Integer32
_RcftRemoteSHDSLPortCurrentCRCTimes_Object = MibTableColumn
rcftRemoteSHDSLPortCurrentCRCTimes = _RcftRemoteSHDSLPortCurrentCRCTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 1, 1, 9),
    _RcftRemoteSHDSLPortCurrentCRCTimes_Type()
)
rcftRemoteSHDSLPortCurrentCRCTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentCRCTimes.setStatus("current")
_RcftRemoteSHDSLPortIntervalTable_Object = MibTable
rcftRemoteSHDSLPortIntervalTable = _RcftRemoteSHDSLPortIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 2)
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalTable.setStatus("current")
_RcftRemoteSHDSLPortIntervalEntry_Object = MibTableRow
rcftRemoteSHDSLPortIntervalEntry = _RcftRemoteSHDSLPortIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 2, 1)
)
rcftRemoteSHDSLPortIntervalEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteSHDSLPortIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteSHDSLPortIntervalNumber"),
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalEntry.setStatus("current")
_RcftRemoteSHDSLPortIntervalNumber_Type = Integer32
_RcftRemoteSHDSLPortIntervalNumber_Object = MibTableColumn
rcftRemoteSHDSLPortIntervalNumber = _RcftRemoteSHDSLPortIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 2, 1, 1),
    _RcftRemoteSHDSLPortIntervalNumber_Type()
)
rcftRemoteSHDSLPortIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalNumber.setStatus("current")
_RcftRemoteSHDSLPortIntervalLOSTimes_Type = Integer32
_RcftRemoteSHDSLPortIntervalLOSTimes_Object = MibTableColumn
rcftRemoteSHDSLPortIntervalLOSTimes = _RcftRemoteSHDSLPortIntervalLOSTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 2, 1, 2),
    _RcftRemoteSHDSLPortIntervalLOSTimes_Type()
)
rcftRemoteSHDSLPortIntervalLOSTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalLOSTimes.setStatus("current")
_RcftRemoteSHDSLPortIntervalLOSWTimes_Type = Integer32
_RcftRemoteSHDSLPortIntervalLOSWTimes_Object = MibTableColumn
rcftRemoteSHDSLPortIntervalLOSWTimes = _RcftRemoteSHDSLPortIntervalLOSWTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 2, 1, 3),
    _RcftRemoteSHDSLPortIntervalLOSWTimes_Type()
)
rcftRemoteSHDSLPortIntervalLOSWTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalLOSWTimes.setStatus("current")
_RcftRemoteSHDSLPortIntervalLOLKTimes_Type = Integer32
_RcftRemoteSHDSLPortIntervalLOLKTimes_Object = MibTableColumn
rcftRemoteSHDSLPortIntervalLOLKTimes = _RcftRemoteSHDSLPortIntervalLOLKTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 2, 1, 4),
    _RcftRemoteSHDSLPortIntervalLOLKTimes_Type()
)
rcftRemoteSHDSLPortIntervalLOLKTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalLOLKTimes.setStatus("current")
_RcftRemoteSHDSLPortIntervalCVTimes_Type = Integer32
_RcftRemoteSHDSLPortIntervalCVTimes_Object = MibTableColumn
rcftRemoteSHDSLPortIntervalCVTimes = _RcftRemoteSHDSLPortIntervalCVTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 2, 1, 5),
    _RcftRemoteSHDSLPortIntervalCVTimes_Type()
)
rcftRemoteSHDSLPortIntervalCVTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalCVTimes.setStatus("current")
_RcftRemoteSHDSLPortIntervalES_Type = Integer32
_RcftRemoteSHDSLPortIntervalES_Object = MibTableColumn
rcftRemoteSHDSLPortIntervalES = _RcftRemoteSHDSLPortIntervalES_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 2, 1, 6),
    _RcftRemoteSHDSLPortIntervalES_Type()
)
rcftRemoteSHDSLPortIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalES.setStatus("current")
_RcftRemoteSHDSLPortIntervalSES_Type = Integer32
_RcftRemoteSHDSLPortIntervalSES_Object = MibTableColumn
rcftRemoteSHDSLPortIntervalSES = _RcftRemoteSHDSLPortIntervalSES_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 2, 1, 7),
    _RcftRemoteSHDSLPortIntervalSES_Type()
)
rcftRemoteSHDSLPortIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalSES.setStatus("current")
_RcftRemoteSHDSLPortIntervalUAS_Type = Integer32
_RcftRemoteSHDSLPortIntervalUAS_Object = MibTableColumn
rcftRemoteSHDSLPortIntervalUAS = _RcftRemoteSHDSLPortIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 2, 1, 8),
    _RcftRemoteSHDSLPortIntervalUAS_Type()
)
rcftRemoteSHDSLPortIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalUAS.setStatus("current")
_RcftRemoteSHDSLPortIntervalLOSWS_Type = Integer32
_RcftRemoteSHDSLPortIntervalLOSWS_Object = MibTableColumn
rcftRemoteSHDSLPortIntervalLOSWS = _RcftRemoteSHDSLPortIntervalLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 2, 1, 9),
    _RcftRemoteSHDSLPortIntervalLOSWS_Type()
)
rcftRemoteSHDSLPortIntervalLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalLOSWS.setStatus("current")
_RcftRemoteSHDSLPortIntervalCRCTimes_Type = Integer32
_RcftRemoteSHDSLPortIntervalCRCTimes_Object = MibTableColumn
rcftRemoteSHDSLPortIntervalCRCTimes = _RcftRemoteSHDSLPortIntervalCRCTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 2, 1, 10),
    _RcftRemoteSHDSLPortIntervalCRCTimes_Type()
)
rcftRemoteSHDSLPortIntervalCRCTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalCRCTimes.setStatus("current")
_RcftRemoteSHDSLPortCurrentDayTable_Object = MibTable
rcftRemoteSHDSLPortCurrentDayTable = _RcftRemoteSHDSLPortCurrentDayTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 3)
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentDayTable.setStatus("current")
_RcftRemoteSHDSLPortCurrentDayEntry_Object = MibTableRow
rcftRemoteSHDSLPortCurrentDayEntry = _RcftRemoteSHDSLPortCurrentDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 3, 1)
)
rcftRemoteSHDSLPortCurrentDayEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteSHDSLPortIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentDayEntry.setStatus("current")
_RcftRemoteSHDSLPortCurrentDayLOSTimes_Type = Integer32
_RcftRemoteSHDSLPortCurrentDayLOSTimes_Object = MibTableColumn
rcftRemoteSHDSLPortCurrentDayLOSTimes = _RcftRemoteSHDSLPortCurrentDayLOSTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 3, 1, 1),
    _RcftRemoteSHDSLPortCurrentDayLOSTimes_Type()
)
rcftRemoteSHDSLPortCurrentDayLOSTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentDayLOSTimes.setStatus("current")
_RcftRemoteSHDSLPortCurrentDayLOSWTimes_Type = Integer32
_RcftRemoteSHDSLPortCurrentDayLOSWTimes_Object = MibTableColumn
rcftRemoteSHDSLPortCurrentDayLOSWTimes = _RcftRemoteSHDSLPortCurrentDayLOSWTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 3, 1, 2),
    _RcftRemoteSHDSLPortCurrentDayLOSWTimes_Type()
)
rcftRemoteSHDSLPortCurrentDayLOSWTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentDayLOSWTimes.setStatus("current")
_RcftRemoteSHDSLPortCurrentDayLOLKTimes_Type = Integer32
_RcftRemoteSHDSLPortCurrentDayLOLKTimes_Object = MibTableColumn
rcftRemoteSHDSLPortCurrentDayLOLKTimes = _RcftRemoteSHDSLPortCurrentDayLOLKTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 3, 1, 3),
    _RcftRemoteSHDSLPortCurrentDayLOLKTimes_Type()
)
rcftRemoteSHDSLPortCurrentDayLOLKTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentDayLOLKTimes.setStatus("current")
_RcftRemoteSHDSLPortCurrentDayCVTimes_Type = Integer32
_RcftRemoteSHDSLPortCurrentDayCVTimes_Object = MibTableColumn
rcftRemoteSHDSLPortCurrentDayCVTimes = _RcftRemoteSHDSLPortCurrentDayCVTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 3, 1, 4),
    _RcftRemoteSHDSLPortCurrentDayCVTimes_Type()
)
rcftRemoteSHDSLPortCurrentDayCVTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentDayCVTimes.setStatus("current")
_RcftRemoteSHDSLPortCurrentDayES_Type = Integer32
_RcftRemoteSHDSLPortCurrentDayES_Object = MibTableColumn
rcftRemoteSHDSLPortCurrentDayES = _RcftRemoteSHDSLPortCurrentDayES_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 3, 1, 5),
    _RcftRemoteSHDSLPortCurrentDayES_Type()
)
rcftRemoteSHDSLPortCurrentDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentDayES.setStatus("current")
_RcftRemoteSHDSLPortCurrentDaySES_Type = Integer32
_RcftRemoteSHDSLPortCurrentDaySES_Object = MibTableColumn
rcftRemoteSHDSLPortCurrentDaySES = _RcftRemoteSHDSLPortCurrentDaySES_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 3, 1, 6),
    _RcftRemoteSHDSLPortCurrentDaySES_Type()
)
rcftRemoteSHDSLPortCurrentDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentDaySES.setStatus("current")
_RcftRemoteSHDSLPortCurrentDayUAS_Type = Integer32
_RcftRemoteSHDSLPortCurrentDayUAS_Object = MibTableColumn
rcftRemoteSHDSLPortCurrentDayUAS = _RcftRemoteSHDSLPortCurrentDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 3, 1, 7),
    _RcftRemoteSHDSLPortCurrentDayUAS_Type()
)
rcftRemoteSHDSLPortCurrentDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentDayUAS.setStatus("current")
_RcftRemoteSHDSLPortCurrentDayLOSWS_Type = Integer32
_RcftRemoteSHDSLPortCurrentDayLOSWS_Object = MibTableColumn
rcftRemoteSHDSLPortCurrentDayLOSWS = _RcftRemoteSHDSLPortCurrentDayLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 3, 1, 8),
    _RcftRemoteSHDSLPortCurrentDayLOSWS_Type()
)
rcftRemoteSHDSLPortCurrentDayLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentDayLOSWS.setStatus("current")
_RcftRemoteSHDSLPortCurrentDayCRCTimes_Type = Integer32
_RcftRemoteSHDSLPortCurrentDayCRCTimes_Object = MibTableColumn
rcftRemoteSHDSLPortCurrentDayCRCTimes = _RcftRemoteSHDSLPortCurrentDayCRCTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 3, 1, 9),
    _RcftRemoteSHDSLPortCurrentDayCRCTimes_Type()
)
rcftRemoteSHDSLPortCurrentDayCRCTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCurrentDayCRCTimes.setStatus("current")
_RcftRemoteSHDSLPortIntervalDayTable_Object = MibTable
rcftRemoteSHDSLPortIntervalDayTable = _RcftRemoteSHDSLPortIntervalDayTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 4)
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalDayTable.setStatus("current")
_RcftRemoteSHDSLPortIntervalDayEntry_Object = MibTableRow
rcftRemoteSHDSLPortIntervalDayEntry = _RcftRemoteSHDSLPortIntervalDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 4, 1)
)
rcftRemoteSHDSLPortIntervalDayEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteSHDSLPortIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteSHDSLPortIntervalDayNumber"),
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalDayEntry.setStatus("current")
_RcftRemoteSHDSLPortIntervalDayNumber_Type = Integer32
_RcftRemoteSHDSLPortIntervalDayNumber_Object = MibTableColumn
rcftRemoteSHDSLPortIntervalDayNumber = _RcftRemoteSHDSLPortIntervalDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 4, 1, 1),
    _RcftRemoteSHDSLPortIntervalDayNumber_Type()
)
rcftRemoteSHDSLPortIntervalDayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalDayNumber.setStatus("current")
_RcftRemoteSHDSLPortIntervalDayLOSTimes_Type = Integer32
_RcftRemoteSHDSLPortIntervalDayLOSTimes_Object = MibTableColumn
rcftRemoteSHDSLPortIntervalDayLOSTimes = _RcftRemoteSHDSLPortIntervalDayLOSTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 4, 1, 2),
    _RcftRemoteSHDSLPortIntervalDayLOSTimes_Type()
)
rcftRemoteSHDSLPortIntervalDayLOSTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalDayLOSTimes.setStatus("current")
_RcftRemoteSHDSLPortIntervalDayLOSWTimes_Type = Integer32
_RcftRemoteSHDSLPortIntervalDayLOSWTimes_Object = MibTableColumn
rcftRemoteSHDSLPortIntervalDayLOSWTimes = _RcftRemoteSHDSLPortIntervalDayLOSWTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 4, 1, 3),
    _RcftRemoteSHDSLPortIntervalDayLOSWTimes_Type()
)
rcftRemoteSHDSLPortIntervalDayLOSWTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalDayLOSWTimes.setStatus("current")
_RcftRemoteSHDSLPortIntervalDayLOLKTimes_Type = Integer32
_RcftRemoteSHDSLPortIntervalDayLOLKTimes_Object = MibTableColumn
rcftRemoteSHDSLPortIntervalDayLOLKTimes = _RcftRemoteSHDSLPortIntervalDayLOLKTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 4, 1, 4),
    _RcftRemoteSHDSLPortIntervalDayLOLKTimes_Type()
)
rcftRemoteSHDSLPortIntervalDayLOLKTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalDayLOLKTimes.setStatus("current")
_RcftRemoteSHDSLPortIntervalDayCVTimes_Type = Integer32
_RcftRemoteSHDSLPortIntervalDayCVTimes_Object = MibTableColumn
rcftRemoteSHDSLPortIntervalDayCVTimes = _RcftRemoteSHDSLPortIntervalDayCVTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 4, 1, 5),
    _RcftRemoteSHDSLPortIntervalDayCVTimes_Type()
)
rcftRemoteSHDSLPortIntervalDayCVTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalDayCVTimes.setStatus("current")
_RcftRemoteSHDSLPortIntervalDayES_Type = Integer32
_RcftRemoteSHDSLPortIntervalDayES_Object = MibTableColumn
rcftRemoteSHDSLPortIntervalDayES = _RcftRemoteSHDSLPortIntervalDayES_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 4, 1, 6),
    _RcftRemoteSHDSLPortIntervalDayES_Type()
)
rcftRemoteSHDSLPortIntervalDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalDayES.setStatus("current")
_RcftRemoteSHDSLPortIntervalDaySES_Type = Integer32
_RcftRemoteSHDSLPortIntervalDaySES_Object = MibTableColumn
rcftRemoteSHDSLPortIntervalDaySES = _RcftRemoteSHDSLPortIntervalDaySES_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 4, 1, 7),
    _RcftRemoteSHDSLPortIntervalDaySES_Type()
)
rcftRemoteSHDSLPortIntervalDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalDaySES.setStatus("current")
_RcftRemoteSHDSLPortIntervalDayUAS_Type = Integer32
_RcftRemoteSHDSLPortIntervalDayUAS_Object = MibTableColumn
rcftRemoteSHDSLPortIntervalDayUAS = _RcftRemoteSHDSLPortIntervalDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 4, 1, 8),
    _RcftRemoteSHDSLPortIntervalDayUAS_Type()
)
rcftRemoteSHDSLPortIntervalDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalDayUAS.setStatus("current")
_RcftRemoteSHDSLPortIntervalDayLOSWS_Type = Integer32
_RcftRemoteSHDSLPortIntervalDayLOSWS_Object = MibTableColumn
rcftRemoteSHDSLPortIntervalDayLOSWS = _RcftRemoteSHDSLPortIntervalDayLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 4, 1, 9),
    _RcftRemoteSHDSLPortIntervalDayLOSWS_Type()
)
rcftRemoteSHDSLPortIntervalDayLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalDayLOSWS.setStatus("current")
_RcftRemoteSHDSLPortIntervalDayCRCTimes_Type = Integer32
_RcftRemoteSHDSLPortIntervalDayCRCTimes_Object = MibTableColumn
rcftRemoteSHDSLPortIntervalDayCRCTimes = _RcftRemoteSHDSLPortIntervalDayCRCTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 2, 4, 1, 10),
    _RcftRemoteSHDSLPortIntervalDayCRCTimes_Type()
)
rcftRemoteSHDSLPortIntervalDayCRCTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortIntervalDayCRCTimes.setStatus("current")
_RcftRemoteSHDSLPortTraps_ObjectIdentity = ObjectIdentity
rcftRemoteSHDSLPortTraps = _RcftRemoteSHDSLPortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 10)
)
_RcftRemoteDeviceV35MIB_ObjectIdentity = ObjectIdentity
rcftRemoteDeviceV35MIB = _RcftRemoteDeviceV35MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5)
)
_RcftRemoteV35PortObjects_ObjectIdentity = ObjectIdentity
rcftRemoteV35PortObjects = _RcftRemoteV35PortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 1)
)
_RcftRemoteV35PortTable_Object = MibTable
rcftRemoteV35PortTable = _RcftRemoteV35PortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteV35PortTable.setStatus("current")
_RcftRemoteV35PortEntry_Object = MibTableRow
rcftRemoteV35PortEntry = _RcftRemoteV35PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 1, 1, 1)
)
rcftRemoteV35PortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteV35PortIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteV35PortEntry.setStatus("current")
_RcftRemoteV35PortIndex_Type = Integer32
_RcftRemoteV35PortIndex_Object = MibTableColumn
rcftRemoteV35PortIndex = _RcftRemoteV35PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 1, 1, 1, 1),
    _RcftRemoteV35PortIndex_Type()
)
rcftRemoteV35PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteV35PortIndex.setStatus("current")
_RcftRemoteV35PortAlarmStatus_Type = Integer32
_RcftRemoteV35PortAlarmStatus_Object = MibTableColumn
rcftRemoteV35PortAlarmStatus = _RcftRemoteV35PortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 1, 1, 1, 2),
    _RcftRemoteV35PortAlarmStatus_Type()
)
rcftRemoteV35PortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteV35PortAlarmStatus.setStatus("current")
_RcftRemoteV35PortStatus_Type = Integer32
_RcftRemoteV35PortStatus_Object = MibTableColumn
rcftRemoteV35PortStatus = _RcftRemoteV35PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 1, 1, 1, 3),
    _RcftRemoteV35PortStatus_Type()
)
rcftRemoteV35PortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteV35PortStatus.setStatus("current")
_RcftRemoteV35PortSpeed_Type = Integer32
_RcftRemoteV35PortSpeed_Object = MibTableColumn
rcftRemoteV35PortSpeed = _RcftRemoteV35PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 1, 1, 1, 4),
    _RcftRemoteV35PortSpeed_Type()
)
rcftRemoteV35PortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteV35PortSpeed.setStatus("current")
_RcftRemoteV35PortOrderTimeParameter_Type = Integer32
_RcftRemoteV35PortOrderTimeParameter_Object = MibTableColumn
rcftRemoteV35PortOrderTimeParameter = _RcftRemoteV35PortOrderTimeParameter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 1, 1, 1, 5),
    _RcftRemoteV35PortOrderTimeParameter_Type()
)
rcftRemoteV35PortOrderTimeParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteV35PortOrderTimeParameter.setStatus("current")
_RcftRemoteV35PortOrderModeParameter_Type = Integer32
_RcftRemoteV35PortOrderModeParameter_Object = MibTableColumn
rcftRemoteV35PortOrderModeParameter = _RcftRemoteV35PortOrderModeParameter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 1, 1, 1, 6),
    _RcftRemoteV35PortOrderModeParameter_Type()
)
rcftRemoteV35PortOrderModeParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteV35PortOrderModeParameter.setStatus("current")
_RcftRemoteV35PortOrder_Type = Integer32
_RcftRemoteV35PortOrder_Object = MibTableColumn
rcftRemoteV35PortOrder = _RcftRemoteV35PortOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 1, 1, 1, 7),
    _RcftRemoteV35PortOrder_Type()
)
rcftRemoteV35PortOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteV35PortOrder.setStatus("current")
_RcftRemoteV35BertStatus_Type = Integer32
_RcftRemoteV35BertStatus_Object = MibTableColumn
rcftRemoteV35BertStatus = _RcftRemoteV35BertStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 1, 1, 1, 8),
    _RcftRemoteV35BertStatus_Type()
)
rcftRemoteV35BertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteV35BertStatus.setStatus("current")
_RcftRemoteV35BertTime_Type = Unsigned32
_RcftRemoteV35BertTime_Object = MibTableColumn
rcftRemoteV35BertTime = _RcftRemoteV35BertTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 1, 1, 1, 9),
    _RcftRemoteV35BertTime_Type()
)
rcftRemoteV35BertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteV35BertTime.setStatus("current")
_RcftRemoteV35BertErrCode_Type = Unsigned32
_RcftRemoteV35BertErrCode_Object = MibTableColumn
rcftRemoteV35BertErrCode = _RcftRemoteV35BertErrCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 1, 1, 1, 10),
    _RcftRemoteV35BertErrCode_Type()
)
rcftRemoteV35BertErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteV35BertErrCode.setStatus("current")
_RcftRemoteV35BertUnusedTime_Type = Unsigned32
_RcftRemoteV35BertUnusedTime_Object = MibTableColumn
rcftRemoteV35BertUnusedTime = _RcftRemoteV35BertUnusedTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 1, 1, 1, 11),
    _RcftRemoteV35BertUnusedTime_Type()
)
rcftRemoteV35BertUnusedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteV35BertUnusedTime.setStatus("current")
_RcftRemoteV35BertPortSpeed_Type = Unsigned32
_RcftRemoteV35BertPortSpeed_Object = MibTableColumn
rcftRemoteV35BertPortSpeed = _RcftRemoteV35BertPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 1, 1, 1, 12),
    _RcftRemoteV35BertPortSpeed_Type()
)
rcftRemoteV35BertPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteV35BertPortSpeed.setStatus("current")
_RcftRemoteV35BertCodeType_Type = Integer32
_RcftRemoteV35BertCodeType_Object = MibTableColumn
rcftRemoteV35BertCodeType = _RcftRemoteV35BertCodeType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 1, 1, 1, 13),
    _RcftRemoteV35BertCodeType_Type()
)
rcftRemoteV35BertCodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteV35BertCodeType.setStatus("current")
_RcftRemoteV35BertCodeNum_Type = Integer32
_RcftRemoteV35BertCodeNum_Object = MibTableColumn
rcftRemoteV35BertCodeNum = _RcftRemoteV35BertCodeNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 1, 1, 1, 14),
    _RcftRemoteV35BertCodeNum_Type()
)
rcftRemoteV35BertCodeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteV35BertCodeNum.setStatus("current")


class _RcftRemoteV35LoopStatus_Type(Integer32):
    """Custom type rcftRemoteV35LoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("localDoubleLoopEnable", 1),
          ("localDoubleLoopDisable", 2),
          ("remoteDoubleLoopEnable", 3),
          ("remoteDoubleLoopDisable", 4),
          ("normal", 5),
          ("localInSideLoopEnale", 6),
          ("localOutSideLoopEnable", 7))
    )


_RcftRemoteV35LoopStatus_Type.__name__ = "Integer32"
_RcftRemoteV35LoopStatus_Object = MibTableColumn
rcftRemoteV35LoopStatus = _RcftRemoteV35LoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 1, 1, 1, 15),
    _RcftRemoteV35LoopStatus_Type()
)
rcftRemoteV35LoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteV35LoopStatus.setStatus("current")
_RcftRemoteV35PortPerformance_ObjectIdentity = ObjectIdentity
rcftRemoteV35PortPerformance = _RcftRemoteV35PortPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 2)
)
_RcftRemoteV35PortTraps_ObjectIdentity = ObjectIdentity
rcftRemoteV35PortTraps = _RcftRemoteV35PortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 3)
)
_RcftRemoteDS3E3PortMIB_ObjectIdentity = ObjectIdentity
rcftRemoteDS3E3PortMIB = _RcftRemoteDS3E3PortMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6)
)
_RcftRemoteDS3E3PortObjects_ObjectIdentity = ObjectIdentity
rcftRemoteDS3E3PortObjects = _RcftRemoteDS3E3PortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 1)
)
_RcftRemoteDS3E3PortTable_Object = MibTable
rcftRemoteDS3E3PortTable = _RcftRemoteDS3E3PortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortTable.setStatus("current")
_RcftRemoteDS3E3PortEntry_Object = MibTableRow
rcftRemoteDS3E3PortEntry = _RcftRemoteDS3E3PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 1, 1, 1)
)
rcftRemoteDS3E3PortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS3E3PortIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortEntry.setStatus("current")
_RcftRemoteDS3E3PortIndex_Type = Integer32
_RcftRemoteDS3E3PortIndex_Object = MibTableColumn
rcftRemoteDS3E3PortIndex = _RcftRemoteDS3E3PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 1, 1, 1, 1),
    _RcftRemoteDS3E3PortIndex_Type()
)
rcftRemoteDS3E3PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortIndex.setStatus("current")
_RcftRemoteDS3E3PortAlarmStatus_Type = Integer32
_RcftRemoteDS3E3PortAlarmStatus_Object = MibTableColumn
rcftRemoteDS3E3PortAlarmStatus = _RcftRemoteDS3E3PortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 1, 1, 1, 2),
    _RcftRemoteDS3E3PortAlarmStatus_Type()
)
rcftRemoteDS3E3PortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortAlarmStatus.setStatus("current")
_RcftRemoteDS3E3PortStatus_Type = Integer32
_RcftRemoteDS3E3PortStatus_Object = MibTableColumn
rcftRemoteDS3E3PortStatus = _RcftRemoteDS3E3PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 1, 1, 1, 3),
    _RcftRemoteDS3E3PortStatus_Type()
)
rcftRemoteDS3E3PortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortStatus.setStatus("current")
_RcftRemoteDS3E3PortESCont_Type = Integer32
_RcftRemoteDS3E3PortESCont_Object = MibTableColumn
rcftRemoteDS3E3PortESCont = _RcftRemoteDS3E3PortESCont_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 1, 1, 1, 4),
    _RcftRemoteDS3E3PortESCont_Type()
)
rcftRemoteDS3E3PortESCont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortESCont.setStatus("current")
_RcftRemoteDS3E3PortBertStatus_Type = Integer32
_RcftRemoteDS3E3PortBertStatus_Object = MibTableColumn
rcftRemoteDS3E3PortBertStatus = _RcftRemoteDS3E3PortBertStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 1, 1, 1, 5),
    _RcftRemoteDS3E3PortBertStatus_Type()
)
rcftRemoteDS3E3PortBertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortBertStatus.setStatus("current")
_RcftRemoteDS3E3PortFaultFass_Type = Integer32
_RcftRemoteDS3E3PortFaultFass_Object = MibTableColumn
rcftRemoteDS3E3PortFaultFass = _RcftRemoteDS3E3PortFaultFass_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 1, 1, 1, 6),
    _RcftRemoteDS3E3PortFaultFass_Type()
)
rcftRemoteDS3E3PortFaultFass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortFaultFass.setStatus("current")
_RcftRemoteDS3E3PortLoopStatus_Type = Integer32
_RcftRemoteDS3E3PortLoopStatus_Object = MibTableColumn
rcftRemoteDS3E3PortLoopStatus = _RcftRemoteDS3E3PortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 1, 1, 1, 7),
    _RcftRemoteDS3E3PortLoopStatus_Type()
)
rcftRemoteDS3E3PortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortLoopStatus.setStatus("current")
_RcftRemoteDS3E3PortOrder_Type = Integer32
_RcftRemoteDS3E3PortOrder_Object = MibTableColumn
rcftRemoteDS3E3PortOrder = _RcftRemoteDS3E3PortOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 1, 1, 1, 8),
    _RcftRemoteDS3E3PortOrder_Type()
)
rcftRemoteDS3E3PortOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortOrder.setStatus("current")
_RcftRemoteDS3E3PortPerformance_ObjectIdentity = ObjectIdentity
rcftRemoteDS3E3PortPerformance = _RcftRemoteDS3E3PortPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 2)
)
_RcftRemoteDS3E3StatisticTable_Object = MibTable
rcftRemoteDS3E3StatisticTable = _RcftRemoteDS3E3StatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 2, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3StatisticTable.setStatus("current")
_RcftRemoteDS3E3StatisticEntry_Object = MibTableRow
rcftRemoteDS3E3StatisticEntry = _RcftRemoteDS3E3StatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3StatisticEntry.setStatus("current")
_RcftRemoteDS3E3TxPackets_Type = Counter32
_RcftRemoteDS3E3TxPackets_Object = MibTableColumn
rcftRemoteDS3E3TxPackets = _RcftRemoteDS3E3TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 2, 1, 1, 1),
    _RcftRemoteDS3E3TxPackets_Type()
)
rcftRemoteDS3E3TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS3E3TxPackets.setStatus("current")
_RcftRemoteDS3E3TxBytes_Type = Counter32
_RcftRemoteDS3E3TxBytes_Object = MibTableColumn
rcftRemoteDS3E3TxBytes = _RcftRemoteDS3E3TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 2, 1, 1, 2),
    _RcftRemoteDS3E3TxBytes_Type()
)
rcftRemoteDS3E3TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS3E3TxBytes.setStatus("current")
_RcftRemoteDS3E3TxFailurePackets_Type = Counter32
_RcftRemoteDS3E3TxFailurePackets_Object = MibTableColumn
rcftRemoteDS3E3TxFailurePackets = _RcftRemoteDS3E3TxFailurePackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 2, 1, 1, 3),
    _RcftRemoteDS3E3TxFailurePackets_Type()
)
rcftRemoteDS3E3TxFailurePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS3E3TxFailurePackets.setStatus("current")
_RcftRemoteDS3E3RxPackets_Type = Counter32
_RcftRemoteDS3E3RxPackets_Object = MibTableColumn
rcftRemoteDS3E3RxPackets = _RcftRemoteDS3E3RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 2, 1, 1, 4),
    _RcftRemoteDS3E3RxPackets_Type()
)
rcftRemoteDS3E3RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS3E3RxPackets.setStatus("current")
_RcftRemoteDS3E3RxBytes_Type = Counter32
_RcftRemoteDS3E3RxBytes_Object = MibTableColumn
rcftRemoteDS3E3RxBytes = _RcftRemoteDS3E3RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 2, 1, 1, 5),
    _RcftRemoteDS3E3RxBytes_Type()
)
rcftRemoteDS3E3RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS3E3RxBytes.setStatus("current")
_RcftRemoteDS3E3RxErrorPackets_Type = Counter32
_RcftRemoteDS3E3RxErrorPackets_Object = MibTableColumn
rcftRemoteDS3E3RxErrorPackets = _RcftRemoteDS3E3RxErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 2, 1, 1, 6),
    _RcftRemoteDS3E3RxErrorPackets_Type()
)
rcftRemoteDS3E3RxErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS3E3RxErrorPackets.setStatus("current")
_RcftRemoteDS3E3FluxTimer_Type = Counter32
_RcftRemoteDS3E3FluxTimer_Object = MibTableColumn
rcftRemoteDS3E3FluxTimer = _RcftRemoteDS3E3FluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 2, 1, 1, 7),
    _RcftRemoteDS3E3FluxTimer_Type()
)
rcftRemoteDS3E3FluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS3E3FluxTimer.setStatus("current")
_RcftRemoteDS3E3PortTraps_ObjectIdentity = ObjectIdentity
rcftRemoteDS3E3PortTraps = _RcftRemoteDS3E3PortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 10)
)
_RcftRemotePdhPortMIB_ObjectIdentity = ObjectIdentity
rcftRemotePdhPortMIB = _RcftRemotePdhPortMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7)
)
_RcftRemotePdhPortObjects_ObjectIdentity = ObjectIdentity
rcftRemotePdhPortObjects = _RcftRemotePdhPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 1)
)
_RcftRemotePdhPortTable_Object = MibTable
rcftRemotePdhPortTable = _RcftRemotePdhPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemotePdhPortTable.setStatus("current")
_RcftRemotePdhPortEntry_Object = MibTableRow
rcftRemotePdhPortEntry = _RcftRemotePdhPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 1, 1, 1)
)
rcftRemotePdhPortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemotePdhPortIndex"),
)
if mibBuilder.loadTexts:
    rcftRemotePdhPortEntry.setStatus("current")
_RcftRemotePdhPortIndex_Type = Integer32
_RcftRemotePdhPortIndex_Object = MibTableColumn
rcftRemotePdhPortIndex = _RcftRemotePdhPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 1, 1, 1, 1),
    _RcftRemotePdhPortIndex_Type()
)
rcftRemotePdhPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemotePdhPortIndex.setStatus("current")


class _RcftRemotePdhPortModuleType_Type(Integer32):
    """Custom type rcftRemotePdhPortModuleType based on Integer32"""
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
              12,
              15,
              23,
              50,
              51,
              52,
              53,
              100)
        )
    )
    namedValues = NamedValues(
        *(("optical-M", 1),
          ("optical-S1", 2),
          ("optical-S2", 3),
          ("optical-S3", 4),
          ("optical-SS13", 5),
          ("optical-SS15", 6),
          ("optical-SS23", 7),
          ("optical-SS25", 8),
          ("optical-SS34", 9),
          ("optical-SS35", 10),
          ("optical-S15", 12),
          ("optical-SFP", 15),
          ("optical-SS24", 23),
          ("optical-S1FC", 50),
          ("optical-S1A", 51),
          ("optical-S2A", 52),
          ("optical-S3A", 53),
          ("unknown-type", 100))
    )


_RcftRemotePdhPortModuleType_Type.__name__ = "Integer32"
_RcftRemotePdhPortModuleType_Object = MibTableColumn
rcftRemotePdhPortModuleType = _RcftRemotePdhPortModuleType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 1, 1, 1, 2),
    _RcftRemotePdhPortModuleType_Type()
)
rcftRemotePdhPortModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemotePdhPortModuleType.setStatus("current")
_RcftRemotePdhPortAlarmStatus_Type = Integer32
_RcftRemotePdhPortAlarmStatus_Object = MibTableColumn
rcftRemotePdhPortAlarmStatus = _RcftRemotePdhPortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 1, 1, 1, 3),
    _RcftRemotePdhPortAlarmStatus_Type()
)
rcftRemotePdhPortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemotePdhPortAlarmStatus.setStatus("current")
_RcftRemotePdhPortStatus_Type = Integer32
_RcftRemotePdhPortStatus_Object = MibTableColumn
rcftRemotePdhPortStatus = _RcftRemotePdhPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 1, 1, 1, 4),
    _RcftRemotePdhPortStatus_Type()
)
rcftRemotePdhPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemotePdhPortStatus.setStatus("current")
_RcftRemotePdhPortECSCnt_Type = Integer32
_RcftRemotePdhPortECSCnt_Object = MibTableColumn
rcftRemotePdhPortECSCnt = _RcftRemotePdhPortECSCnt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 1, 1, 1, 5),
    _RcftRemotePdhPortECSCnt_Type()
)
rcftRemotePdhPortECSCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemotePdhPortECSCnt.setStatus("current")
_RcftRemotePdhPortSECSCnt_Type = Integer32
_RcftRemotePdhPortSECSCnt_Object = MibTableColumn
rcftRemotePdhPortSECSCnt = _RcftRemotePdhPortSECSCnt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 1, 1, 1, 6),
    _RcftRemotePdhPortSECSCnt_Type()
)
rcftRemotePdhPortSECSCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemotePdhPortSECSCnt.setStatus("current")
_RcftRemotePdhPortLoopStatus_Type = Integer32
_RcftRemotePdhPortLoopStatus_Object = MibTableColumn
rcftRemotePdhPortLoopStatus = _RcftRemotePdhPortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 1, 1, 1, 7),
    _RcftRemotePdhPortLoopStatus_Type()
)
rcftRemotePdhPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemotePdhPortLoopStatus.setStatus("current")
_RcftRemotePdhPortOrder_Type = Integer32
_RcftRemotePdhPortOrder_Object = MibTableColumn
rcftRemotePdhPortOrder = _RcftRemotePdhPortOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 1, 1, 1, 8),
    _RcftRemotePdhPortOrder_Type()
)
rcftRemotePdhPortOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemotePdhPortOrder.setStatus("current")
_RcftRemotePdhPortBertStatus_Type = Integer32
_RcftRemotePdhPortBertStatus_Object = MibTableColumn
rcftRemotePdhPortBertStatus = _RcftRemotePdhPortBertStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 1, 1, 1, 9),
    _RcftRemotePdhPortBertStatus_Type()
)
rcftRemotePdhPortBertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemotePdhPortBertStatus.setStatus("current")
_RcftRemotePdhPortBertErrCode_Type = Unsigned32
_RcftRemotePdhPortBertErrCode_Object = MibTableColumn
rcftRemotePdhPortBertErrCode = _RcftRemotePdhPortBertErrCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 1, 1, 1, 10),
    _RcftRemotePdhPortBertErrCode_Type()
)
rcftRemotePdhPortBertErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemotePdhPortBertErrCode.setStatus("current")
_RcftRemotePdhPortPerformance_ObjectIdentity = ObjectIdentity
rcftRemotePdhPortPerformance = _RcftRemotePdhPortPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 2)
)
_RcftRemotePdhPortTraps_ObjectIdentity = ObjectIdentity
rcftRemotePdhPortTraps = _RcftRemotePdhPortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 10)
)
_RcftRemoteDS1PortMIB_ObjectIdentity = ObjectIdentity
rcftRemoteDS1PortMIB = _RcftRemoteDS1PortMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8)
)
_RcftRemoteDS1PortObjects_ObjectIdentity = ObjectIdentity
rcftRemoteDS1PortObjects = _RcftRemoteDS1PortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 1)
)
_RcftRemoteDS1PortTable_Object = MibTable
rcftRemoteDS1PortTable = _RcftRemoteDS1PortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteDS1PortTable.setStatus("current")
_RcftRemoteDS1PortEntry_Object = MibTableRow
rcftRemoteDS1PortEntry = _RcftRemoteDS1PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 1, 1, 1)
)
rcftRemoteDS1PortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS1PortIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteDS1PortEntry.setStatus("current")
_RcftRemoteDS1PortIndex_Type = Integer32
_RcftRemoteDS1PortIndex_Object = MibTableColumn
rcftRemoteDS1PortIndex = _RcftRemoteDS1PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 1, 1, 1, 1),
    _RcftRemoteDS1PortIndex_Type()
)
rcftRemoteDS1PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS1PortIndex.setStatus("current")
_RcftRemoteDS1PortAlarmStatus_Type = Integer32
_RcftRemoteDS1PortAlarmStatus_Object = MibTableColumn
rcftRemoteDS1PortAlarmStatus = _RcftRemoteDS1PortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 1, 1, 1, 2),
    _RcftRemoteDS1PortAlarmStatus_Type()
)
rcftRemoteDS1PortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS1PortAlarmStatus.setStatus("current")
_RcftRemoteDS1PortStatus_Type = Integer32
_RcftRemoteDS1PortStatus_Object = MibTableColumn
rcftRemoteDS1PortStatus = _RcftRemoteDS1PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 1, 1, 1, 3),
    _RcftRemoteDS1PortStatus_Type()
)
rcftRemoteDS1PortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDS1PortStatus.setStatus("current")
_RcftRemoteDS1PortESCont_Type = Integer32
_RcftRemoteDS1PortESCont_Object = MibTableColumn
rcftRemoteDS1PortESCont = _RcftRemoteDS1PortESCont_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 1, 1, 1, 4),
    _RcftRemoteDS1PortESCont_Type()
)
rcftRemoteDS1PortESCont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS1PortESCont.setStatus("current")
_RcftRemoteDS1PortSESCont_Type = Integer32
_RcftRemoteDS1PortSESCont_Object = MibTableColumn
rcftRemoteDS1PortSESCont = _RcftRemoteDS1PortSESCont_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 1, 1, 1, 5),
    _RcftRemoteDS1PortSESCont_Type()
)
rcftRemoteDS1PortSESCont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS1PortSESCont.setStatus("current")
_RcftRemoteDS1PortBertStatus_Type = Integer32
_RcftRemoteDS1PortBertStatus_Object = MibTableColumn
rcftRemoteDS1PortBertStatus = _RcftRemoteDS1PortBertStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 1, 1, 1, 6),
    _RcftRemoteDS1PortBertStatus_Type()
)
rcftRemoteDS1PortBertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS1PortBertStatus.setStatus("current")
_RcftRemoteDS1PortFaultPass_Type = Integer32
_RcftRemoteDS1PortFaultPass_Object = MibTableColumn
rcftRemoteDS1PortFaultPass = _RcftRemoteDS1PortFaultPass_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 1, 1, 1, 7),
    _RcftRemoteDS1PortFaultPass_Type()
)
rcftRemoteDS1PortFaultPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDS1PortFaultPass.setStatus("current")
_RcftRemoteDS1PortLoopStatus_Type = Integer32
_RcftRemoteDS1PortLoopStatus_Object = MibTableColumn
rcftRemoteDS1PortLoopStatus = _RcftRemoteDS1PortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 1, 1, 1, 8),
    _RcftRemoteDS1PortLoopStatus_Type()
)
rcftRemoteDS1PortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS1PortLoopStatus.setStatus("current")
_RcftRemoteDS1PortOrder_Type = Integer32
_RcftRemoteDS1PortOrder_Object = MibTableColumn
rcftRemoteDS1PortOrder = _RcftRemoteDS1PortOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 1, 1, 1, 9),
    _RcftRemoteDS1PortOrder_Type()
)
rcftRemoteDS1PortOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDS1PortOrder.setStatus("current")
_RcftRemoteDS1PortTranLength_Type = Integer32
_RcftRemoteDS1PortTranLength_Object = MibTableColumn
rcftRemoteDS1PortTranLength = _RcftRemoteDS1PortTranLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 1, 1, 1, 10),
    _RcftRemoteDS1PortTranLength_Type()
)
rcftRemoteDS1PortTranLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDS1PortTranLength.setStatus("current")
_RcftRemoteDS1PortFaultPassIndicator_Type = Integer32
_RcftRemoteDS1PortFaultPassIndicator_Object = MibTableColumn
rcftRemoteDS1PortFaultPassIndicator = _RcftRemoteDS1PortFaultPassIndicator_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 1, 1, 1, 11),
    _RcftRemoteDS1PortFaultPassIndicator_Type()
)
rcftRemoteDS1PortFaultPassIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS1PortFaultPassIndicator.setStatus("current")
_RcftRemoteDS1PortframeType_Type = Integer32
_RcftRemoteDS1PortframeType_Object = MibTableColumn
rcftRemoteDS1PortframeType = _RcftRemoteDS1PortframeType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 1, 1, 1, 12),
    _RcftRemoteDS1PortframeType_Type()
)
rcftRemoteDS1PortframeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDS1PortframeType.setStatus("current")
_RcftRemoteDS1PortChannel_Type = Integer32
_RcftRemoteDS1PortChannel_Object = MibTableColumn
rcftRemoteDS1PortChannel = _RcftRemoteDS1PortChannel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 1, 1, 1, 13),
    _RcftRemoteDS1PortChannel_Type()
)
rcftRemoteDS1PortChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDS1PortChannel.setStatus("current")
_RcftRemoteDS1PortPerformance_ObjectIdentity = ObjectIdentity
rcftRemoteDS1PortPerformance = _RcftRemoteDS1PortPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 2)
)
_RcftRemoteDS1StatisticTable_Object = MibTable
rcftRemoteDS1StatisticTable = _RcftRemoteDS1StatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 2, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteDS1StatisticTable.setStatus("current")
_RcftRemoteDS1StatisticEntry_Object = MibTableRow
rcftRemoteDS1StatisticEntry = _RcftRemoteDS1StatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteDS1StatisticEntry.setStatus("current")
_RcftRemoteDS1TxPackets_Type = Counter32
_RcftRemoteDS1TxPackets_Object = MibTableColumn
rcftRemoteDS1TxPackets = _RcftRemoteDS1TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 2, 1, 1, 1),
    _RcftRemoteDS1TxPackets_Type()
)
rcftRemoteDS1TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS1TxPackets.setStatus("current")
_RcftRemoteDS1TxBytes_Type = Counter32
_RcftRemoteDS1TxBytes_Object = MibTableColumn
rcftRemoteDS1TxBytes = _RcftRemoteDS1TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 2, 1, 1, 2),
    _RcftRemoteDS1TxBytes_Type()
)
rcftRemoteDS1TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS1TxBytes.setStatus("current")
_RcftRemoteDS1TxFailurePackets_Type = Counter32
_RcftRemoteDS1TxFailurePackets_Object = MibTableColumn
rcftRemoteDS1TxFailurePackets = _RcftRemoteDS1TxFailurePackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 2, 1, 1, 3),
    _RcftRemoteDS1TxFailurePackets_Type()
)
rcftRemoteDS1TxFailurePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS1TxFailurePackets.setStatus("current")
_RcftRemoteDS1RxPackets_Type = Counter32
_RcftRemoteDS1RxPackets_Object = MibTableColumn
rcftRemoteDS1RxPackets = _RcftRemoteDS1RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 2, 1, 1, 4),
    _RcftRemoteDS1RxPackets_Type()
)
rcftRemoteDS1RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS1RxPackets.setStatus("current")
_RcftRemoteDS1RxBytes_Type = Counter32
_RcftRemoteDS1RxBytes_Object = MibTableColumn
rcftRemoteDS1RxBytes = _RcftRemoteDS1RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 2, 1, 1, 5),
    _RcftRemoteDS1RxBytes_Type()
)
rcftRemoteDS1RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS1RxBytes.setStatus("current")
_RcftRemoteDS1RxErrorPackets_Type = Counter32
_RcftRemoteDS1RxErrorPackets_Object = MibTableColumn
rcftRemoteDS1RxErrorPackets = _RcftRemoteDS1RxErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 2, 1, 1, 6),
    _RcftRemoteDS1RxErrorPackets_Type()
)
rcftRemoteDS1RxErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS1RxErrorPackets.setStatus("current")
_RcftRemoteDS1FluxTimer_Type = Counter32
_RcftRemoteDS1FluxTimer_Object = MibTableColumn
rcftRemoteDS1FluxTimer = _RcftRemoteDS1FluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 2, 1, 1, 7),
    _RcftRemoteDS1FluxTimer_Type()
)
rcftRemoteDS1FluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDS1FluxTimer.setStatus("current")
_RcftRemoteDS1PortTraps_ObjectIdentity = ObjectIdentity
rcftRemoteDS1PortTraps = _RcftRemoteDS1PortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 10)
)
_RcftRemoteMoudleMIB_ObjectIdentity = ObjectIdentity
rcftRemoteMoudleMIB = _RcftRemoteMoudleMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9)
)
_RcftRemoteMoudle_ObjectIdentity = ObjectIdentity
rcftRemoteMoudle = _RcftRemoteMoudle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 1)
)
_RcftRemoteMoudleObjects_ObjectIdentity = ObjectIdentity
rcftRemoteMoudleObjects = _RcftRemoteMoudleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 1, 1)
)
_RcftRemoteMoudleTable_Object = MibTable
rcftRemoteMoudleTable = _RcftRemoteMoudleTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteMoudleTable.setStatus("current")
_RcftRemoteMoudleEntry_Object = MibTableRow
rcftRemoteMoudleEntry = _RcftRemoteMoudleEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 1, 1, 1, 1)
)
rcftRemoteMoudleEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteMoudleIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteMoudleEntry.setStatus("current")
_RcftRemoteMoudleIndex_Type = Integer32
_RcftRemoteMoudleIndex_Object = MibTableColumn
rcftRemoteMoudleIndex = _RcftRemoteMoudleIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 1, 1, 1, 1, 1),
    _RcftRemoteMoudleIndex_Type()
)
rcftRemoteMoudleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleIndex.setStatus("current")


class _RcftRemoteMoudleExist_Type(Integer32):
    """Custom type rcftRemoteMoudleExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("notExist", 2))
    )


_RcftRemoteMoudleExist_Type.__name__ = "Integer32"
_RcftRemoteMoudleExist_Object = MibTableColumn
rcftRemoteMoudleExist = _RcftRemoteMoudleExist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 1, 1, 1, 1, 2),
    _RcftRemoteMoudleExist_Type()
)
rcftRemoteMoudleExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleExist.setStatus("current")


class _RcftRemoteMoudleType_Type(Integer32):
    """Custom type rcftRemoteMoudleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6402,
              6422,
              6423,
              6424,
              6425,
              6427,
              6428)
        )
    )
    namedValues = NamedValues(
        *(("e-SUBM-2E1-A", 6402),
          ("e-SUBM-2FV35-A", 6422),
          ("e-SUBM-2FE-A", 6423),
          ("e-SUBM-FE4E1-A", 6424),
          ("e-SUBM-FV35-A", 6425),
          ("e-SUBM-FV35-B", 6427),
          ("e-SUBM-2FV35-B", 6428))
    )


_RcftRemoteMoudleType_Type.__name__ = "Integer32"
_RcftRemoteMoudleType_Object = MibTableColumn
rcftRemoteMoudleType = _RcftRemoteMoudleType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 1, 1, 1, 1, 3),
    _RcftRemoteMoudleType_Type()
)
rcftRemoteMoudleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteMoudleType.setStatus("current")
_RcftRemoteMoudleStatus_Type = Integer32
_RcftRemoteMoudleStatus_Object = MibTableColumn
rcftRemoteMoudleStatus = _RcftRemoteMoudleStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 1, 1, 1, 1, 4),
    _RcftRemoteMoudleStatus_Type()
)
rcftRemoteMoudleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteMoudleStatus.setStatus("current")


class _RcftRemoteMoudleSigleChipDescr_Type(OctetString):
    """Custom type rcftRemoteMoudleSigleChipDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftRemoteMoudleSigleChipDescr_Type.__name__ = "OctetString"
_RcftRemoteMoudleSigleChipDescr_Object = MibTableColumn
rcftRemoteMoudleSigleChipDescr = _RcftRemoteMoudleSigleChipDescr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 1, 1, 1, 1, 5),
    _RcftRemoteMoudleSigleChipDescr_Type()
)
rcftRemoteMoudleSigleChipDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleSigleChipDescr.setStatus("current")


class _RcftRemoteMoudleHardWareDescr_Type(OctetString):
    """Custom type rcftRemoteMoudleHardWareDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftRemoteMoudleHardWareDescr_Type.__name__ = "OctetString"
_RcftRemoteMoudleHardWareDescr_Object = MibTableColumn
rcftRemoteMoudleHardWareDescr = _RcftRemoteMoudleHardWareDescr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 1, 1, 1, 1, 6),
    _RcftRemoteMoudleHardWareDescr_Type()
)
rcftRemoteMoudleHardWareDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleHardWareDescr.setStatus("current")


class _RcftRemoteMoudleFPGADescr_Type(OctetString):
    """Custom type rcftRemoteMoudleFPGADescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftRemoteMoudleFPGADescr_Type.__name__ = "OctetString"
_RcftRemoteMoudleFPGADescr_Object = MibTableColumn
rcftRemoteMoudleFPGADescr = _RcftRemoteMoudleFPGADescr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 1, 1, 1, 1, 7),
    _RcftRemoteMoudleFPGADescr_Type()
)
rcftRemoteMoudleFPGADescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleFPGADescr.setStatus("current")
_RcftRemoteMoudleOrder_Type = Integer32
_RcftRemoteMoudleOrder_Object = MibTableColumn
rcftRemoteMoudleOrder = _RcftRemoteMoudleOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 1, 1, 1, 1, 8),
    _RcftRemoteMoudleOrder_Type()
)
rcftRemoteMoudleOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteMoudleOrder.setStatus("current")


class _RcftRemoteMoudleIFOrder_Type(OctetString):
    """Custom type rcftRemoteMoudleIFOrder based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftRemoteMoudleIFOrder_Type.__name__ = "OctetString"
_RcftRemoteMoudleIFOrder_Object = MibTableColumn
rcftRemoteMoudleIFOrder = _RcftRemoteMoudleIFOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 1, 1, 1, 1, 9),
    _RcftRemoteMoudleIFOrder_Type()
)
rcftRemoteMoudleIFOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteMoudleIFOrder.setStatus("current")
_RcftRemoteMoudleTraps_ObjectIdentity = ObjectIdentity
rcftRemoteMoudleTraps = _RcftRemoteMoudleTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 1, 10)
)
_RcftRemoteMoudleEthFe_ObjectIdentity = ObjectIdentity
rcftRemoteMoudleEthFe = _RcftRemoteMoudleEthFe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2)
)
_RcftRemoteMoudleEthFeObjects_ObjectIdentity = ObjectIdentity
rcftRemoteMoudleEthFeObjects = _RcftRemoteMoudleEthFeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 1)
)
_RcftRemoteMoudleEthFeTable_Object = MibTable
rcftRemoteMoudleEthFeTable = _RcftRemoteMoudleEthFeTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteMoudleEthFeTable.setStatus("current")
_RcftRemoteMoudleEthFeEntry_Object = MibTableRow
rcftRemoteMoudleEthFeEntry = _RcftRemoteMoudleEthFeEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 1, 1, 1)
)
rcftRemoteMoudleEthFeEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteMoudleIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteMoudleEthFeIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteMoudleEthFeEntry.setStatus("current")
_RcftRemoteMoudleEthFeIndex_Type = Integer32
_RcftRemoteMoudleEthFeIndex_Object = MibTableColumn
rcftRemoteMoudleEthFeIndex = _RcftRemoteMoudleEthFeIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 1, 1, 1, 1),
    _RcftRemoteMoudleEthFeIndex_Type()
)
rcftRemoteMoudleEthFeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleEthFeIndex.setStatus("current")
_RcftRemoteMoudleEthFeStatus_Type = Integer32
_RcftRemoteMoudleEthFeStatus_Object = MibTableColumn
rcftRemoteMoudleEthFeStatus = _RcftRemoteMoudleEthFeStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 1, 1, 1, 2),
    _RcftRemoteMoudleEthFeStatus_Type()
)
rcftRemoteMoudleEthFeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteMoudleEthFeStatus.setStatus("current")
_RcftRemoteMoudleEthFeRxRestrictSpeed_Type = Integer32
_RcftRemoteMoudleEthFeRxRestrictSpeed_Object = MibTableColumn
rcftRemoteMoudleEthFeRxRestrictSpeed = _RcftRemoteMoudleEthFeRxRestrictSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 1, 1, 1, 3),
    _RcftRemoteMoudleEthFeRxRestrictSpeed_Type()
)
rcftRemoteMoudleEthFeRxRestrictSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteMoudleEthFeRxRestrictSpeed.setStatus("current")
_RcftRemoteMoudleEthFeTxRestrictSpeed_Type = Integer32
_RcftRemoteMoudleEthFeTxRestrictSpeed_Object = MibTableColumn
rcftRemoteMoudleEthFeTxRestrictSpeed = _RcftRemoteMoudleEthFeTxRestrictSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 1, 1, 1, 4),
    _RcftRemoteMoudleEthFeTxRestrictSpeed_Type()
)
rcftRemoteMoudleEthFeTxRestrictSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteMoudleEthFeTxRestrictSpeed.setStatus("current")
_RcftRemoteMoudleEthFeRestrictSpeedStep_Type = Integer32
_RcftRemoteMoudleEthFeRestrictSpeedStep_Object = MibTableColumn
rcftRemoteMoudleEthFeRestrictSpeedStep = _RcftRemoteMoudleEthFeRestrictSpeedStep_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 1, 1, 1, 5),
    _RcftRemoteMoudleEthFeRestrictSpeedStep_Type()
)
rcftRemoteMoudleEthFeRestrictSpeedStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleEthFeRestrictSpeedStep.setStatus("current")
_RcftRemoteMoudleEthFeAlarmStatus_Type = Integer32
_RcftRemoteMoudleEthFeAlarmStatus_Object = MibTableColumn
rcftRemoteMoudleEthFeAlarmStatus = _RcftRemoteMoudleEthFeAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 1, 1, 1, 6),
    _RcftRemoteMoudleEthFeAlarmStatus_Type()
)
rcftRemoteMoudleEthFeAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleEthFeAlarmStatus.setStatus("current")
_RcftRemoteMoudleEthFePerformance_ObjectIdentity = ObjectIdentity
rcftRemoteMoudleEthFePerformance = _RcftRemoteMoudleEthFePerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 2)
)
_RcftRemoteMoudleEthFeStatisticTable_Object = MibTable
rcftRemoteMoudleEthFeStatisticTable = _RcftRemoteMoudleEthFeStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteMoudleEthFeStatisticTable.setStatus("current")
_RcftRemoteMoudleEthFeStatisticEntry_Object = MibTableRow
rcftRemoteMoudleEthFeStatisticEntry = _RcftRemoteMoudleEthFeStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteMoudleEthFeStatisticEntry.setStatus("current")
_RcftRemoteMoudleEthFeTxPackets_Type = Counter32
_RcftRemoteMoudleEthFeTxPackets_Object = MibTableColumn
rcftRemoteMoudleEthFeTxPackets = _RcftRemoteMoudleEthFeTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 2, 1, 1, 1),
    _RcftRemoteMoudleEthFeTxPackets_Type()
)
rcftRemoteMoudleEthFeTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleEthFeTxPackets.setStatus("current")
_RcftRemoteMoudleEthFeTxBytes_Type = Counter32
_RcftRemoteMoudleEthFeTxBytes_Object = MibTableColumn
rcftRemoteMoudleEthFeTxBytes = _RcftRemoteMoudleEthFeTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 2, 1, 1, 2),
    _RcftRemoteMoudleEthFeTxBytes_Type()
)
rcftRemoteMoudleEthFeTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleEthFeTxBytes.setStatus("current")
_RcftRemoteMoudleEthFeTxFailurePackets_Type = Counter32
_RcftRemoteMoudleEthFeTxFailurePackets_Object = MibTableColumn
rcftRemoteMoudleEthFeTxFailurePackets = _RcftRemoteMoudleEthFeTxFailurePackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 2, 1, 1, 3),
    _RcftRemoteMoudleEthFeTxFailurePackets_Type()
)
rcftRemoteMoudleEthFeTxFailurePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleEthFeTxFailurePackets.setStatus("current")
_RcftRemoteMoudleEthFeRxPackets_Type = Counter32
_RcftRemoteMoudleEthFeRxPackets_Object = MibTableColumn
rcftRemoteMoudleEthFeRxPackets = _RcftRemoteMoudleEthFeRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 2, 1, 1, 4),
    _RcftRemoteMoudleEthFeRxPackets_Type()
)
rcftRemoteMoudleEthFeRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleEthFeRxPackets.setStatus("current")
_RcftRemoteMoudleEthFeRxBytes_Type = Counter32
_RcftRemoteMoudleEthFeRxBytes_Object = MibTableColumn
rcftRemoteMoudleEthFeRxBytes = _RcftRemoteMoudleEthFeRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 2, 1, 1, 5),
    _RcftRemoteMoudleEthFeRxBytes_Type()
)
rcftRemoteMoudleEthFeRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleEthFeRxBytes.setStatus("current")
_RcftRemoteMoudleEthFeRxErrorPackets_Type = Counter32
_RcftRemoteMoudleEthFeRxErrorPackets_Object = MibTableColumn
rcftRemoteMoudleEthFeRxErrorPackets = _RcftRemoteMoudleEthFeRxErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 2, 1, 1, 6),
    _RcftRemoteMoudleEthFeRxErrorPackets_Type()
)
rcftRemoteMoudleEthFeRxErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleEthFeRxErrorPackets.setStatus("current")
_RcftRemoteMoudleEthFeFluxTimer_Type = Counter32
_RcftRemoteMoudleEthFeFluxTimer_Object = MibTableColumn
rcftRemoteMoudleEthFeFluxTimer = _RcftRemoteMoudleEthFeFluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 2, 1, 1, 7),
    _RcftRemoteMoudleEthFeFluxTimer_Type()
)
rcftRemoteMoudleEthFeFluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleEthFeFluxTimer.setStatus("current")
_RcftRemoteMoudleEthFeTraps_ObjectIdentity = ObjectIdentity
rcftRemoteMoudleEthFeTraps = _RcftRemoteMoudleEthFeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 10)
)
_RcftRemoteMoudlePdh_ObjectIdentity = ObjectIdentity
rcftRemoteMoudlePdh = _RcftRemoteMoudlePdh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 3)
)
_RcftRemoteMoudlePdhObjects_ObjectIdentity = ObjectIdentity
rcftRemoteMoudlePdhObjects = _RcftRemoteMoudlePdhObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 3, 1)
)
_RcftRemoteMoudlePdhTable_Object = MibTable
rcftRemoteMoudlePdhTable = _RcftRemoteMoudlePdhTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 3, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteMoudlePdhTable.setStatus("current")
_RcftRemoteMoudlePdhEntry_Object = MibTableRow
rcftRemoteMoudlePdhEntry = _RcftRemoteMoudlePdhEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 3, 1, 1, 1)
)
rcftRemoteMoudlePdhEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteMoudleIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteMoudlePdhIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteMoudlePdhEntry.setStatus("current")
_RcftRemoteMoudlePdhIndex_Type = Integer32
_RcftRemoteMoudlePdhIndex_Object = MibTableColumn
rcftRemoteMoudlePdhIndex = _RcftRemoteMoudlePdhIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 3, 1, 1, 1, 1),
    _RcftRemoteMoudlePdhIndex_Type()
)
rcftRemoteMoudlePdhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudlePdhIndex.setStatus("current")
_RcftRemoteMoudlePdhAlarmStatus_Type = Integer32
_RcftRemoteMoudlePdhAlarmStatus_Object = MibTableColumn
rcftRemoteMoudlePdhAlarmStatus = _RcftRemoteMoudlePdhAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 3, 1, 1, 1, 2),
    _RcftRemoteMoudlePdhAlarmStatus_Type()
)
rcftRemoteMoudlePdhAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudlePdhAlarmStatus.setStatus("current")
_RcftRemoteMoudlePdhStatus_Type = Integer32
_RcftRemoteMoudlePdhStatus_Object = MibTableColumn
rcftRemoteMoudlePdhStatus = _RcftRemoteMoudlePdhStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 3, 1, 1, 1, 3),
    _RcftRemoteMoudlePdhStatus_Type()
)
rcftRemoteMoudlePdhStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteMoudlePdhStatus.setStatus("current")
_RcftRemoteMoudlePdhTraps_ObjectIdentity = ObjectIdentity
rcftRemoteMoudlePdhTraps = _RcftRemoteMoudlePdhTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 3, 10)
)
_RcftRemoteMoudleE1_ObjectIdentity = ObjectIdentity
rcftRemoteMoudleE1 = _RcftRemoteMoudleE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4)
)
_RcftRemoteMoudleE1Objects_ObjectIdentity = ObjectIdentity
rcftRemoteMoudleE1Objects = _RcftRemoteMoudleE1Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 1)
)
_RcftRemoteMoudleE1Table_Object = MibTable
rcftRemoteMoudleE1Table = _RcftRemoteMoudleE1Table_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1Table.setStatus("current")
_RcftRemoteMoudleE1Entry_Object = MibTableRow
rcftRemoteMoudleE1Entry = _RcftRemoteMoudleE1Entry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 1, 1, 1)
)
rcftRemoteMoudleE1Entry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteMoudleIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteMoudleE1Index"),
)
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1Entry.setStatus("current")
_RcftRemoteMoudleE1Index_Type = Integer32
_RcftRemoteMoudleE1Index_Object = MibTableColumn
rcftRemoteMoudleE1Index = _RcftRemoteMoudleE1Index_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 1, 1, 1, 1),
    _RcftRemoteMoudleE1Index_Type()
)
rcftRemoteMoudleE1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1Index.setStatus("current")
_RcftRemoteMoudleE1AlarmStatus_Type = Integer32
_RcftRemoteMoudleE1AlarmStatus_Object = MibTableColumn
rcftRemoteMoudleE1AlarmStatus = _RcftRemoteMoudleE1AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 1, 1, 1, 2),
    _RcftRemoteMoudleE1AlarmStatus_Type()
)
rcftRemoteMoudleE1AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1AlarmStatus.setStatus("current")
_RcftRemoteMoudleE1Status_Type = Integer32
_RcftRemoteMoudleE1Status_Object = MibTableColumn
rcftRemoteMoudleE1Status = _RcftRemoteMoudleE1Status_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 1, 1, 1, 3),
    _RcftRemoteMoudleE1Status_Type()
)
rcftRemoteMoudleE1Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1Status.setStatus("current")
_RcftRemoteMoudleE1TimeSlots_Type = Integer32
_RcftRemoteMoudleE1TimeSlots_Object = MibTableColumn
rcftRemoteMoudleE1TimeSlots = _RcftRemoteMoudleE1TimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 1, 1, 1, 4),
    _RcftRemoteMoudleE1TimeSlots_Type()
)
rcftRemoteMoudleE1TimeSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1TimeSlots.setStatus("current")
_RcftRemoteMoudleE1TS0Mode_Type = Integer32
_RcftRemoteMoudleE1TS0Mode_Object = MibTableColumn
rcftRemoteMoudleE1TS0Mode = _RcftRemoteMoudleE1TS0Mode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 1, 1, 1, 5),
    _RcftRemoteMoudleE1TS0Mode_Type()
)
rcftRemoteMoudleE1TS0Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1TS0Mode.setStatus("current")
_RcftRemoteMoudleE1LoopStatus_Type = Integer32
_RcftRemoteMoudleE1LoopStatus_Object = MibTableColumn
rcftRemoteMoudleE1LoopStatus = _RcftRemoteMoudleE1LoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 1, 1, 1, 6),
    _RcftRemoteMoudleE1LoopStatus_Type()
)
rcftRemoteMoudleE1LoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1LoopStatus.setStatus("current")
_RcftRemoteMoudleE1ESCnt_Type = Integer32
_RcftRemoteMoudleE1ESCnt_Object = MibTableColumn
rcftRemoteMoudleE1ESCnt = _RcftRemoteMoudleE1ESCnt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 1, 1, 1, 7),
    _RcftRemoteMoudleE1ESCnt_Type()
)
rcftRemoteMoudleE1ESCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1ESCnt.setStatus("current")
_RcftRemoteMoudleE1SESCnt_Type = Integer32
_RcftRemoteMoudleE1SESCnt_Object = MibTableColumn
rcftRemoteMoudleE1SESCnt = _RcftRemoteMoudleE1SESCnt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 1, 1, 1, 8),
    _RcftRemoteMoudleE1SESCnt_Type()
)
rcftRemoteMoudleE1SESCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1SESCnt.setStatus("current")
_RcftRemoteMoudleE1Performance_ObjectIdentity = ObjectIdentity
rcftRemoteMoudleE1Performance = _RcftRemoteMoudleE1Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 2)
)
_RcftRemoteMoudleE1StatisticTable_Object = MibTable
rcftRemoteMoudleE1StatisticTable = _RcftRemoteMoudleE1StatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 2, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1StatisticTable.setStatus("current")
_RcftRemoteMoudleE1StatisticEntry_Object = MibTableRow
rcftRemoteMoudleE1StatisticEntry = _RcftRemoteMoudleE1StatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1StatisticEntry.setStatus("current")
_RcftRemoteMoudleE1TxPackets_Type = Counter32
_RcftRemoteMoudleE1TxPackets_Object = MibTableColumn
rcftRemoteMoudleE1TxPackets = _RcftRemoteMoudleE1TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 2, 1, 1, 1),
    _RcftRemoteMoudleE1TxPackets_Type()
)
rcftRemoteMoudleE1TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1TxPackets.setStatus("current")
_RcftRemoteMoudleE1TxBytes_Type = Counter32
_RcftRemoteMoudleE1TxBytes_Object = MibTableColumn
rcftRemoteMoudleE1TxBytes = _RcftRemoteMoudleE1TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 2, 1, 1, 2),
    _RcftRemoteMoudleE1TxBytes_Type()
)
rcftRemoteMoudleE1TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1TxBytes.setStatus("current")
_RcftRemoteMoudleE1TxFailurePackets_Type = Counter32
_RcftRemoteMoudleE1TxFailurePackets_Object = MibTableColumn
rcftRemoteMoudleE1TxFailurePackets = _RcftRemoteMoudleE1TxFailurePackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 2, 1, 1, 3),
    _RcftRemoteMoudleE1TxFailurePackets_Type()
)
rcftRemoteMoudleE1TxFailurePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1TxFailurePackets.setStatus("current")
_RcftRemoteMoudleE1RxPackets_Type = Counter32
_RcftRemoteMoudleE1RxPackets_Object = MibTableColumn
rcftRemoteMoudleE1RxPackets = _RcftRemoteMoudleE1RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 2, 1, 1, 4),
    _RcftRemoteMoudleE1RxPackets_Type()
)
rcftRemoteMoudleE1RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1RxPackets.setStatus("current")
_RcftRemoteMoudleE1RxBytes_Type = Counter32
_RcftRemoteMoudleE1RxBytes_Object = MibTableColumn
rcftRemoteMoudleE1RxBytes = _RcftRemoteMoudleE1RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 2, 1, 1, 5),
    _RcftRemoteMoudleE1RxBytes_Type()
)
rcftRemoteMoudleE1RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1RxBytes.setStatus("current")
_RcftRemoteMoudleE1RxErrorPackets_Type = Counter32
_RcftRemoteMoudleE1RxErrorPackets_Object = MibTableColumn
rcftRemoteMoudleE1RxErrorPackets = _RcftRemoteMoudleE1RxErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 2, 1, 1, 6),
    _RcftRemoteMoudleE1RxErrorPackets_Type()
)
rcftRemoteMoudleE1RxErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1RxErrorPackets.setStatus("current")
_RcftRemoteMoudleE1FluxTimer_Type = Counter32
_RcftRemoteMoudleE1FluxTimer_Object = MibTableColumn
rcftRemoteMoudleE1FluxTimer = _RcftRemoteMoudleE1FluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 2, 1, 1, 7),
    _RcftRemoteMoudleE1FluxTimer_Type()
)
rcftRemoteMoudleE1FluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1FluxTimer.setStatus("current")
_RcftRemoteMoudleE1Traps_ObjectIdentity = ObjectIdentity
rcftRemoteMoudleE1Traps = _RcftRemoteMoudleE1Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 10)
)
_RcftRemoteMoudleV35_ObjectIdentity = ObjectIdentity
rcftRemoteMoudleV35 = _RcftRemoteMoudleV35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 5)
)
_RcftRemoteMoudleV35Objects_ObjectIdentity = ObjectIdentity
rcftRemoteMoudleV35Objects = _RcftRemoteMoudleV35Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 5, 1)
)
_RcftRemoteMoudleV35Table_Object = MibTable
rcftRemoteMoudleV35Table = _RcftRemoteMoudleV35Table_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 5, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteMoudleV35Table.setStatus("current")
_RcftRemoteMoudleV35Entry_Object = MibTableRow
rcftRemoteMoudleV35Entry = _RcftRemoteMoudleV35Entry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 5, 1, 1, 1)
)
rcftRemoteMoudleV35Entry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteMoudleIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteMoudleV35Index"),
)
if mibBuilder.loadTexts:
    rcftRemoteMoudleV35Entry.setStatus("current")
_RcftRemoteMoudleV35Index_Type = Integer32
_RcftRemoteMoudleV35Index_Object = MibTableColumn
rcftRemoteMoudleV35Index = _RcftRemoteMoudleV35Index_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 5, 1, 1, 1, 1),
    _RcftRemoteMoudleV35Index_Type()
)
rcftRemoteMoudleV35Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleV35Index.setStatus("current")
_RcftRemoteMoudleV35AlarmStatus_Type = Integer32
_RcftRemoteMoudleV35AlarmStatus_Object = MibTableColumn
rcftRemoteMoudleV35AlarmStatus = _RcftRemoteMoudleV35AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 5, 1, 1, 1, 2),
    _RcftRemoteMoudleV35AlarmStatus_Type()
)
rcftRemoteMoudleV35AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteMoudleV35AlarmStatus.setStatus("current")
_RcftRemoteMoudleV35Status_Type = Integer32
_RcftRemoteMoudleV35Status_Object = MibTableColumn
rcftRemoteMoudleV35Status = _RcftRemoteMoudleV35Status_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 5, 1, 1, 1, 3),
    _RcftRemoteMoudleV35Status_Type()
)
rcftRemoteMoudleV35Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteMoudleV35Status.setStatus("current")
_RcftRemoteMoudleV35Traps_ObjectIdentity = ObjectIdentity
rcftRemoteMoudleV35Traps = _RcftRemoteMoudleV35Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 5, 10)
)
_RcftRemoteAudioPortMIB_ObjectIdentity = ObjectIdentity
rcftRemoteAudioPortMIB = _RcftRemoteAudioPortMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 10)
)
_RcftRemoteAudioPortObjects_ObjectIdentity = ObjectIdentity
rcftRemoteAudioPortObjects = _RcftRemoteAudioPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 10, 1)
)
_RcftRemoteAudioPortTable_Object = MibTable
rcftRemoteAudioPortTable = _RcftRemoteAudioPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 10, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteAudioPortTable.setStatus("current")
_RcftRemoteAudioPortEntry_Object = MibTableRow
rcftRemoteAudioPortEntry = _RcftRemoteAudioPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 10, 1, 1, 1)
)
rcftRemoteAudioPortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteAudioPortIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteAudioPortEntry.setStatus("current")
_RcftRemoteAudioPortIndex_Type = Integer32
_RcftRemoteAudioPortIndex_Object = MibTableColumn
rcftRemoteAudioPortIndex = _RcftRemoteAudioPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 10, 1, 1, 1, 1),
    _RcftRemoteAudioPortIndex_Type()
)
rcftRemoteAudioPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteAudioPortIndex.setStatus("current")
_RcftRemoteAudioPortStatus_Type = Integer32
_RcftRemoteAudioPortStatus_Object = MibTableColumn
rcftRemoteAudioPortStatus = _RcftRemoteAudioPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 10, 1, 1, 1, 2),
    _RcftRemoteAudioPortStatus_Type()
)
rcftRemoteAudioPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteAudioPortStatus.setStatus("current")
_RcftRemoteAudioPortPosition_Type = Integer32
_RcftRemoteAudioPortPosition_Object = MibTableColumn
rcftRemoteAudioPortPosition = _RcftRemoteAudioPortPosition_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 10, 1, 1, 1, 3),
    _RcftRemoteAudioPortPosition_Type()
)
rcftRemoteAudioPortPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteAudioPortPosition.setStatus("current")
_RcftRemoteAudioPortType_Type = Integer32
_RcftRemoteAudioPortType_Object = MibTableColumn
rcftRemoteAudioPortType = _RcftRemoteAudioPortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 10, 1, 1, 1, 4),
    _RcftRemoteAudioPortType_Type()
)
rcftRemoteAudioPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteAudioPortType.setStatus("current")
_RcftRemoteAudioPortPerformance_ObjectIdentity = ObjectIdentity
rcftRemoteAudioPortPerformance = _RcftRemoteAudioPortPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 10, 2)
)
_RcftRemoteAudioPortTraps_ObjectIdentity = ObjectIdentity
rcftRemoteAudioPortTraps = _RcftRemoteAudioPortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 10, 10)
)
_RcftRemoteVideoPortMIB_ObjectIdentity = ObjectIdentity
rcftRemoteVideoPortMIB = _RcftRemoteVideoPortMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 11)
)
_RcftRemoteVideoPortObjects_ObjectIdentity = ObjectIdentity
rcftRemoteVideoPortObjects = _RcftRemoteVideoPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 11, 1)
)
_RcftRemoteVideoPortTable_Object = MibTable
rcftRemoteVideoPortTable = _RcftRemoteVideoPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 11, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteVideoPortTable.setStatus("current")
_RcftRemoteVideoPortEntry_Object = MibTableRow
rcftRemoteVideoPortEntry = _RcftRemoteVideoPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 11, 1, 1, 1)
)
rcftRemoteVideoPortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteVideoPortIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteVideoPortEntry.setStatus("current")
_RcftRemoteVideoPortIndex_Type = Integer32
_RcftRemoteVideoPortIndex_Object = MibTableColumn
rcftRemoteVideoPortIndex = _RcftRemoteVideoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 11, 1, 1, 1, 1),
    _RcftRemoteVideoPortIndex_Type()
)
rcftRemoteVideoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVideoPortIndex.setStatus("current")
_RcftRemoteVideoPortStatus_Type = Integer32
_RcftRemoteVideoPortStatus_Object = MibTableColumn
rcftRemoteVideoPortStatus = _RcftRemoteVideoPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 11, 1, 1, 1, 2),
    _RcftRemoteVideoPortStatus_Type()
)
rcftRemoteVideoPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteVideoPortStatus.setStatus("current")
_RcftRemoteVideoPortPosition_Type = Integer32
_RcftRemoteVideoPortPosition_Object = MibTableColumn
rcftRemoteVideoPortPosition = _RcftRemoteVideoPortPosition_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 11, 1, 1, 1, 3),
    _RcftRemoteVideoPortPosition_Type()
)
rcftRemoteVideoPortPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVideoPortPosition.setStatus("current")
_RcftRemoteVideoPortSourceID_Type = Integer32
_RcftRemoteVideoPortSourceID_Object = MibTableColumn
rcftRemoteVideoPortSourceID = _RcftRemoteVideoPortSourceID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 11, 1, 1, 1, 4),
    _RcftRemoteVideoPortSourceID_Type()
)
rcftRemoteVideoPortSourceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteVideoPortSourceID.setStatus("current")
_RcftRemoteVideoPortPerformance_ObjectIdentity = ObjectIdentity
rcftRemoteVideoPortPerformance = _RcftRemoteVideoPortPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 11, 2)
)
_RcftRemoteVideoPortTraps_ObjectIdentity = ObjectIdentity
rcftRemoteVideoPortTraps = _RcftRemoteVideoPortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 11, 10)
)
_RcftRemoteDataPortMIB_ObjectIdentity = ObjectIdentity
rcftRemoteDataPortMIB = _RcftRemoteDataPortMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 12)
)
_RcftRemoteDataPortObjects_ObjectIdentity = ObjectIdentity
rcftRemoteDataPortObjects = _RcftRemoteDataPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 12, 1)
)
_RcftRemoteDataPortTable_Object = MibTable
rcftRemoteDataPortTable = _RcftRemoteDataPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 12, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteDataPortTable.setStatus("current")
_RcftRemoteDataPortEntry_Object = MibTableRow
rcftRemoteDataPortEntry = _RcftRemoteDataPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 12, 1, 1, 1)
)
rcftRemoteDataPortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDataPortIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteDataPortEntry.setStatus("current")
_RcftRemoteDataPortIndex_Type = Integer32
_RcftRemoteDataPortIndex_Object = MibTableColumn
rcftRemoteDataPortIndex = _RcftRemoteDataPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 12, 1, 1, 1, 1),
    _RcftRemoteDataPortIndex_Type()
)
rcftRemoteDataPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDataPortIndex.setStatus("current")
_RcftRemoteDataPortStatus_Type = Integer32
_RcftRemoteDataPortStatus_Object = MibTableColumn
rcftRemoteDataPortStatus = _RcftRemoteDataPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 12, 1, 1, 1, 2),
    _RcftRemoteDataPortStatus_Type()
)
rcftRemoteDataPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteDataPortStatus.setStatus("current")
_RcftRemoteDataPortPosition_Type = Integer32
_RcftRemoteDataPortPosition_Object = MibTableColumn
rcftRemoteDataPortPosition = _RcftRemoteDataPortPosition_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 12, 1, 1, 1, 3),
    _RcftRemoteDataPortPosition_Type()
)
rcftRemoteDataPortPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDataPortPosition.setStatus("current")
_RcftRemoteDataPortType_Type = Integer32
_RcftRemoteDataPortType_Object = MibTableColumn
rcftRemoteDataPortType = _RcftRemoteDataPortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 12, 1, 1, 1, 4),
    _RcftRemoteDataPortType_Type()
)
rcftRemoteDataPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteDataPortType.setStatus("current")
_RcftRemoteDataPortPerformance_ObjectIdentity = ObjectIdentity
rcftRemoteDataPortPerformance = _RcftRemoteDataPortPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 12, 2)
)
_RcftRemoteDataPortTraps_ObjectIdentity = ObjectIdentity
rcftRemoteDataPortTraps = _RcftRemoteDataPortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 12, 10)
)
_RcftRemoteSimpleModuleMIB_ObjectIdentity = ObjectIdentity
rcftRemoteSimpleModuleMIB = _RcftRemoteSimpleModuleMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 13)
)
_RcftRemoteSimpleModuleObjects_ObjectIdentity = ObjectIdentity
rcftRemoteSimpleModuleObjects = _RcftRemoteSimpleModuleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 13, 1)
)
_RcftRemoteSimpleModuleTable_Object = MibTable
rcftRemoteSimpleModuleTable = _RcftRemoteSimpleModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 13, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteSimpleModuleTable.setStatus("current")
_RcftRemoteSimpleModuleEntry_Object = MibTableRow
rcftRemoteSimpleModuleEntry = _RcftRemoteSimpleModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 13, 1, 1, 1)
)
rcftRemoteSimpleModuleEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteSimpleModuleIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteSimpleModuleEntry.setStatus("current")
_RcftRemoteSimpleModuleIndex_Type = Integer32
_RcftRemoteSimpleModuleIndex_Object = MibTableColumn
rcftRemoteSimpleModuleIndex = _RcftRemoteSimpleModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 13, 1, 1, 1, 1),
    _RcftRemoteSimpleModuleIndex_Type()
)
rcftRemoteSimpleModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSimpleModuleIndex.setStatus("current")
_RcftRemoteSimpleModuleExist_Type = Integer32
_RcftRemoteSimpleModuleExist_Object = MibTableColumn
rcftRemoteSimpleModuleExist = _RcftRemoteSimpleModuleExist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 13, 1, 1, 1, 2),
    _RcftRemoteSimpleModuleExist_Type()
)
rcftRemoteSimpleModuleExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSimpleModuleExist.setStatus("current")
_RcftRemoteSimpleModulePosition_Type = Integer32
_RcftRemoteSimpleModulePosition_Object = MibTableColumn
rcftRemoteSimpleModulePosition = _RcftRemoteSimpleModulePosition_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 13, 1, 1, 1, 3),
    _RcftRemoteSimpleModulePosition_Type()
)
rcftRemoteSimpleModulePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSimpleModulePosition.setStatus("current")
_RcftRemoteSimpleModuleStatus_Type = Integer32
_RcftRemoteSimpleModuleStatus_Object = MibTableColumn
rcftRemoteSimpleModuleStatus = _RcftRemoteSimpleModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 13, 1, 1, 1, 4),
    _RcftRemoteSimpleModuleStatus_Type()
)
rcftRemoteSimpleModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteSimpleModuleStatus.setStatus("current")
_RcftRemoteSimpleModuleType_Type = Integer32
_RcftRemoteSimpleModuleType_Object = MibTableColumn
rcftRemoteSimpleModuleType = _RcftRemoteSimpleModuleType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 13, 1, 1, 1, 5),
    _RcftRemoteSimpleModuleType_Type()
)
rcftRemoteSimpleModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteSimpleModuleType.setStatus("current")
_RcftRemoteSimpleModulePerformance_ObjectIdentity = ObjectIdentity
rcftRemoteSimpleModulePerformance = _RcftRemoteSimpleModulePerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 13, 2)
)
_RcftRemoteSimpleModuleTraps_ObjectIdentity = ObjectIdentity
rcftRemoteSimpleModuleTraps = _RcftRemoteSimpleModuleTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 13, 10)
)
_RcftRemoteVLANMIB_ObjectIdentity = ObjectIdentity
rcftRemoteVLANMIB = _RcftRemoteVLANMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 14)
)
_RcftRemoteVLANObjects_ObjectIdentity = ObjectIdentity
rcftRemoteVLANObjects = _RcftRemoteVLANObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 14, 1)
)
_RcftRemoteVLANTable_Object = MibTable
rcftRemoteVLANTable = _RcftRemoteVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 14, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteVLANTable.setStatus("current")
_RcftRemoteVLANEntry_Object = MibTableRow
rcftRemoteVLANEntry = _RcftRemoteVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 14, 1, 1, 1)
)
rcftRemoteVLANEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteVLANIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteVLANEntry.setStatus("current")
_RcftRemoteVLANIndex_Type = Integer32
_RcftRemoteVLANIndex_Object = MibTableColumn
rcftRemoteVLANIndex = _RcftRemoteVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 14, 1, 1, 1, 1),
    _RcftRemoteVLANIndex_Type()
)
rcftRemoteVLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVLANIndex.setStatus("current")
_RcftRemoteVLANStatus_Type = Integer32
_RcftRemoteVLANStatus_Object = MibTableColumn
rcftRemoteVLANStatus = _RcftRemoteVLANStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 14, 1, 1, 1, 2),
    _RcftRemoteVLANStatus_Type()
)
rcftRemoteVLANStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteVLANStatus.setStatus("current")
_RcftRemoteVLANmember_Type = Integer32
_RcftRemoteVLANmember_Object = MibTableColumn
rcftRemoteVLANmember = _RcftRemoteVLANmember_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 14, 1, 1, 1, 3),
    _RcftRemoteVLANmember_Type()
)
rcftRemoteVLANmember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteVLANmember.setStatus("current")
_RcftRemoteVID_Type = Integer32
_RcftRemoteVID_Object = MibTableColumn
rcftRemoteVID = _RcftRemoteVID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 14, 1, 1, 1, 4),
    _RcftRemoteVID_Type()
)
rcftRemoteVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteVID.setStatus("current")
_RcftRemotePerformaceMib_ObjectIdentity = ObjectIdentity
rcftRemotePerformaceMib = _RcftRemotePerformaceMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15)
)
_RcftRemoteStatisticPerformance_ObjectIdentity = ObjectIdentity
rcftRemoteStatisticPerformance = _RcftRemoteStatisticPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15, 1)
)
_RcftRemoteStatisticTable_Object = MibTable
rcftRemoteStatisticTable = _RcftRemoteStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteStatisticTable.setStatus("current")
_RcftRemoteStatisticEntry_Object = MibTableRow
rcftRemoteStatisticEntry = _RcftRemoteStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15, 1, 1, 1)
)
rcftRemoteStatisticEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemotePortIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteStatisticEntry.setStatus("current")
_RcftRemotePortIndex_Type = Integer32
_RcftRemotePortIndex_Object = MibTableColumn
rcftRemotePortIndex = _RcftRemotePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15, 1, 1, 1, 1),
    _RcftRemotePortIndex_Type()
)
rcftRemotePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemotePortIndex.setStatus("current")
_RcftRemotePortType_Type = Integer32
_RcftRemotePortType_Object = MibTableColumn
rcftRemotePortType = _RcftRemotePortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15, 1, 1, 1, 2),
    _RcftRemotePortType_Type()
)
rcftRemotePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemotePortType.setStatus("current")
_RcftRemoteRxPackets_Type = Counter32
_RcftRemoteRxPackets_Object = MibTableColumn
rcftRemoteRxPackets = _RcftRemoteRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15, 1, 1, 1, 3),
    _RcftRemoteRxPackets_Type()
)
rcftRemoteRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteRxPackets.setStatus("current")
_RcftRemoteRxLosPackets_Type = Counter32
_RcftRemoteRxLosPackets_Object = MibTableColumn
rcftRemoteRxLosPackets = _RcftRemoteRxLosPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15, 1, 1, 1, 4),
    _RcftRemoteRxLosPackets_Type()
)
rcftRemoteRxLosPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteRxLosPackets.setStatus("current")
_RcftRemoteRxPreabErrPackets_Type = Counter32
_RcftRemoteRxPreabErrPackets_Object = MibTableColumn
rcftRemoteRxPreabErrPackets = _RcftRemoteRxPreabErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15, 1, 1, 1, 5),
    _RcftRemoteRxPreabErrPackets_Type()
)
rcftRemoteRxPreabErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteRxPreabErrPackets.setStatus("current")
_RcftRemoteRxFCSErrPackets_Type = Counter32
_RcftRemoteRxFCSErrPackets_Object = MibTableColumn
rcftRemoteRxFCSErrPackets = _RcftRemoteRxFCSErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15, 1, 1, 1, 6),
    _RcftRemoteRxFCSErrPackets_Type()
)
rcftRemoteRxFCSErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteRxFCSErrPackets.setStatus("current")
_RcftRemoteRxUnderSizePackets_Type = Counter32
_RcftRemoteRxUnderSizePackets_Object = MibTableColumn
rcftRemoteRxUnderSizePackets = _RcftRemoteRxUnderSizePackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15, 1, 1, 1, 7),
    _RcftRemoteRxUnderSizePackets_Type()
)
rcftRemoteRxUnderSizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteRxUnderSizePackets.setStatus("current")
_RcftRemoteRxOverSizePackets_Type = Counter32
_RcftRemoteRxOverSizePackets_Object = MibTableColumn
rcftRemoteRxOverSizePackets = _RcftRemoteRxOverSizePackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15, 1, 1, 1, 8),
    _RcftRemoteRxOverSizePackets_Type()
)
rcftRemoteRxOverSizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteRxOverSizePackets.setStatus("current")
_RcftRemoteRxPausePackets_Type = Counter32
_RcftRemoteRxPausePackets_Object = MibTableColumn
rcftRemoteRxPausePackets = _RcftRemoteRxPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15, 1, 1, 1, 9),
    _RcftRemoteRxPausePackets_Type()
)
rcftRemoteRxPausePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteRxPausePackets.setStatus("current")
_RcftRemoteRxOamPackets_Type = Counter32
_RcftRemoteRxOamPackets_Object = MibTableColumn
rcftRemoteRxOamPackets = _RcftRemoteRxOamPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15, 1, 1, 1, 10),
    _RcftRemoteRxOamPackets_Type()
)
rcftRemoteRxOamPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteRxOamPackets.setStatus("current")
_RcftRemoteRxBytes_Type = Counter32
_RcftRemoteRxBytes_Object = MibTableColumn
rcftRemoteRxBytes = _RcftRemoteRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15, 1, 1, 1, 11),
    _RcftRemoteRxBytes_Type()
)
rcftRemoteRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteRxBytes.setStatus("current")
_RcftRemoteTxPackets_Type = Counter32
_RcftRemoteTxPackets_Object = MibTableColumn
rcftRemoteTxPackets = _RcftRemoteTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15, 1, 1, 1, 12),
    _RcftRemoteTxPackets_Type()
)
rcftRemoteTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteTxPackets.setStatus("current")
_RcftRemoteTxFCSErrPackets_Type = Counter32
_RcftRemoteTxFCSErrPackets_Object = MibTableColumn
rcftRemoteTxFCSErrPackets = _RcftRemoteTxFCSErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15, 1, 1, 1, 13),
    _RcftRemoteTxFCSErrPackets_Type()
)
rcftRemoteTxFCSErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteTxFCSErrPackets.setStatus("current")
_RcftRemoteTxPausePackets_Type = Counter32
_RcftRemoteTxPausePackets_Object = MibTableColumn
rcftRemoteTxPausePackets = _RcftRemoteTxPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15, 1, 1, 1, 14),
    _RcftRemoteTxPausePackets_Type()
)
rcftRemoteTxPausePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteTxPausePackets.setStatus("current")
_RcftRemoteTxOamPackets_Type = Counter32
_RcftRemoteTxOamPackets_Object = MibTableColumn
rcftRemoteTxOamPackets = _RcftRemoteTxOamPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15, 1, 1, 1, 15),
    _RcftRemoteTxOamPackets_Type()
)
rcftRemoteTxOamPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteTxOamPackets.setStatus("current")
_RcftRemoteTxBytes_Type = Counter32
_RcftRemoteTxBytes_Object = MibTableColumn
rcftRemoteTxBytes = _RcftRemoteTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15, 1, 1, 1, 16),
    _RcftRemoteTxBytes_Type()
)
rcftRemoteTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteTxBytes.setStatus("current")
_RcftRemoteFluxTimer_Type = Counter32
_RcftRemoteFluxTimer_Object = MibTableColumn
rcftRemoteFluxTimer = _RcftRemoteFluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 15, 1, 1, 1, 17),
    _RcftRemoteFluxTimer_Type()
)
rcftRemoteFluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteFluxTimer.setStatus("current")
_RcftRemoteVCGMib_ObjectIdentity = ObjectIdentity
rcftRemoteVCGMib = _RcftRemoteVCGMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16)
)
_RcftRemoteVCGObjects_ObjectIdentity = ObjectIdentity
rcftRemoteVCGObjects = _RcftRemoteVCGObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1)
)
_RcftRemoteVCGTable_Object = MibTable
rcftRemoteVCGTable = _RcftRemoteVCGTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteVCGTable.setStatus("current")
_RcftRemoteVCGEntry_Object = MibTableRow
rcftRemoteVCGEntry = _RcftRemoteVCGEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1, 1, 1)
)
rcftRemoteVCGEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceIndex"),
    (0, "RC002-REMOTE-DEVICE-MIB", "rcftRemoteVCGIndex"),
)
if mibBuilder.loadTexts:
    rcftRemoteVCGEntry.setStatus("current")
_RcftRemoteVCGIndex_Type = Integer32
_RcftRemoteVCGIndex_Object = MibTableColumn
rcftRemoteVCGIndex = _RcftRemoteVCGIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1, 1, 1, 1),
    _RcftRemoteVCGIndex_Type()
)
rcftRemoteVCGIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGIndex.setStatus("current")
_RcftRemoteVCGStatus_Type = Integer32
_RcftRemoteVCGStatus_Object = MibTableColumn
rcftRemoteVCGStatus = _RcftRemoteVCGStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1, 1, 1, 2),
    _RcftRemoteVCGStatus_Type()
)
rcftRemoteVCGStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteVCGStatus.setStatus("current")
_RcftRemoteVCGLoopStatus_Type = Integer32
_RcftRemoteVCGLoopStatus_Object = MibTableColumn
rcftRemoteVCGLoopStatus = _RcftRemoteVCGLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1, 1, 1, 3),
    _RcftRemoteVCGLoopStatus_Type()
)
rcftRemoteVCGLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGLoopStatus.setStatus("current")
_RcftRemoteVCGLcasXPR_Type = Integer32
_RcftRemoteVCGLcasXPR_Object = MibTableColumn
rcftRemoteVCGLcasXPR = _RcftRemoteVCGLcasXPR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1, 1, 1, 4),
    _RcftRemoteVCGLcasXPR_Type()
)
rcftRemoteVCGLcasXPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGLcasXPR.setStatus("current")
_RcftRemoteVCGLcasXAR_Type = Integer32
_RcftRemoteVCGLcasXAR_Object = MibTableColumn
rcftRemoteVCGLcasXAR = _RcftRemoteVCGLcasXAR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1, 1, 1, 5),
    _RcftRemoteVCGLcasXAR_Type()
)
rcftRemoteVCGLcasXAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGLcasXAR.setStatus("current")
_RcftRemoteVCGLcasXPT_Type = Integer32
_RcftRemoteVCGLcasXPT_Object = MibTableColumn
rcftRemoteVCGLcasXPT = _RcftRemoteVCGLcasXPT_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1, 1, 1, 6),
    _RcftRemoteVCGLcasXPT_Type()
)
rcftRemoteVCGLcasXPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGLcasXPT.setStatus("current")
_RcftRemoteVCGLcasXAT_Type = Integer32
_RcftRemoteVCGLcasXAT_Object = MibTableColumn
rcftRemoteVCGLcasXAT = _RcftRemoteVCGLcasXAT_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1, 1, 1, 7),
    _RcftRemoteVCGLcasXAT_Type()
)
rcftRemoteVCGLcasXAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGLcasXAT.setStatus("current")
_RcftRemoteVCGAlarmStatus_Type = Integer32
_RcftRemoteVCGAlarmStatus_Object = MibTableColumn
rcftRemoteVCGAlarmStatus = _RcftRemoteVCGAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1, 1, 1, 8),
    _RcftRemoteVCGAlarmStatus_Type()
)
rcftRemoteVCGAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGAlarmStatus.setStatus("current")
_RcftRemoteVCGRxISPTPID_Type = Integer32
_RcftRemoteVCGRxISPTPID_Object = MibTableColumn
rcftRemoteVCGRxISPTPID = _RcftRemoteVCGRxISPTPID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1, 1, 1, 9),
    _RcftRemoteVCGRxISPTPID_Type()
)
rcftRemoteVCGRxISPTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteVCGRxISPTPID.setStatus("current")
_RcftRemoteVCGTxISPTPID_Type = Integer32
_RcftRemoteVCGTxISPTPID_Object = MibTableColumn
rcftRemoteVCGTxISPTPID = _RcftRemoteVCGTxISPTPID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1, 1, 1, 10),
    _RcftRemoteVCGTxISPTPID_Type()
)
rcftRemoteVCGTxISPTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteVCGTxISPTPID.setStatus("current")
_RcftRemoteVCGBaseCoS_Type = Integer32
_RcftRemoteVCGBaseCoS_Object = MibTableColumn
rcftRemoteVCGBaseCoS = _RcftRemoteVCGBaseCoS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1, 1, 1, 11),
    _RcftRemoteVCGBaseCoS_Type()
)
rcftRemoteVCGBaseCoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteVCGBaseCoS.setStatus("current")
_RcftRemoteVCGVLANID_Type = Integer32
_RcftRemoteVCGVLANID_Object = MibTableColumn
rcftRemoteVCGVLANID = _RcftRemoteVCGVLANID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1, 1, 1, 12),
    _RcftRemoteVCGVLANID_Type()
)
rcftRemoteVCGVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteVCGVLANID.setStatus("current")


class _RcftRemoteVCGMemberList_Type(OctetString):
    """Custom type rcftRemoteVCGMemberList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RcftRemoteVCGMemberList_Type.__name__ = "OctetString"
_RcftRemoteVCGMemberList_Object = MibTableColumn
rcftRemoteVCGMemberList = _RcftRemoteVCGMemberList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1, 1, 1, 13),
    _RcftRemoteVCGMemberList_Type()
)
rcftRemoteVCGMemberList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteVCGMemberList.setStatus("current")


class _RcftRemoteVCGMemberStatus_Type(OctetString):
    """Custom type rcftRemoteVCGMemberStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RcftRemoteVCGMemberStatus_Type.__name__ = "OctetString"
_RcftRemoteVCGMemberStatus_Object = MibTableColumn
rcftRemoteVCGMemberStatus = _RcftRemoteVCGMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1, 1, 1, 14),
    _RcftRemoteVCGMemberStatus_Type()
)
rcftRemoteVCGMemberStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRemoteVCGMemberStatus.setStatus("current")


class _RcftRemoteVCGMemberRxCode_Type(OctetString):
    """Custom type rcftRemoteVCGMemberRxCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RcftRemoteVCGMemberRxCode_Type.__name__ = "OctetString"
_RcftRemoteVCGMemberRxCode_Object = MibTableColumn
rcftRemoteVCGMemberRxCode = _RcftRemoteVCGMemberRxCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1, 1, 1, 15),
    _RcftRemoteVCGMemberRxCode_Type()
)
rcftRemoteVCGMemberRxCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGMemberRxCode.setStatus("current")


class _RcftRemoteVCGMemberTxCode_Type(OctetString):
    """Custom type rcftRemoteVCGMemberTxCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RcftRemoteVCGMemberTxCode_Type.__name__ = "OctetString"
_RcftRemoteVCGMemberTxCode_Object = MibTableColumn
rcftRemoteVCGMemberTxCode = _RcftRemoteVCGMemberTxCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1, 1, 1, 16),
    _RcftRemoteVCGMemberTxCode_Type()
)
rcftRemoteVCGMemberTxCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGMemberTxCode.setStatus("current")


class _RcftRemoteVCGMemberAlarmStatus_Type(OctetString):
    """Custom type rcftRemoteVCGMemberAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RcftRemoteVCGMemberAlarmStatus_Type.__name__ = "OctetString"
_RcftRemoteVCGMemberAlarmStatus_Object = MibTableColumn
rcftRemoteVCGMemberAlarmStatus = _RcftRemoteVCGMemberAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1, 1, 1, 17),
    _RcftRemoteVCGMemberAlarmStatus_Type()
)
rcftRemoteVCGMemberAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGMemberAlarmStatus.setStatus("current")


class _RcftRemoteToLVCGMemberAlarmStatus_Type(OctetString):
    """Custom type rcftRemoteToLVCGMemberAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RcftRemoteToLVCGMemberAlarmStatus_Type.__name__ = "OctetString"
_RcftRemoteToLVCGMemberAlarmStatus_Object = MibTableColumn
rcftRemoteToLVCGMemberAlarmStatus = _RcftRemoteToLVCGMemberAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 1, 1, 1, 18),
    _RcftRemoteToLVCGMemberAlarmStatus_Type()
)
rcftRemoteToLVCGMemberAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteToLVCGMemberAlarmStatus.setStatus("current")
_RcftRemoteVCGPerformance_ObjectIdentity = ObjectIdentity
rcftRemoteVCGPerformance = _RcftRemoteVCGPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2)
)
_RcftRemoteVCGStatisticTable_Object = MibTable
rcftRemoteVCGStatisticTable = _RcftRemoteVCGStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteVCGStatisticTable.setStatus("current")
_RcftRemoteVCGStatisticEntry_Object = MibTableRow
rcftRemoteVCGStatisticEntry = _RcftRemoteVCGStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rcftRemoteVCGStatisticEntry.setStatus("current")
_RcftRemoteVCGRxClientPackets_Type = Counter32
_RcftRemoteVCGRxClientPackets_Object = MibTableColumn
rcftRemoteVCGRxClientPackets = _RcftRemoteVCGRxClientPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1, 1, 1),
    _RcftRemoteVCGRxClientPackets_Type()
)
rcftRemoteVCGRxClientPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGRxClientPackets.setStatus("current")
_RcftRemoteVCGRxIdlePackets_Type = Counter32
_RcftRemoteVCGRxIdlePackets_Object = MibTableColumn
rcftRemoteVCGRxIdlePackets = _RcftRemoteVCGRxIdlePackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1, 1, 2),
    _RcftRemoteVCGRxIdlePackets_Type()
)
rcftRemoteVCGRxIdlePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGRxIdlePackets.setStatus("current")
_RcftRemoteVCGRxMgmntPackets_Type = Counter32
_RcftRemoteVCGRxMgmntPackets_Object = MibTableColumn
rcftRemoteVCGRxMgmntPackets = _RcftRemoteVCGRxMgmntPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1, 1, 3),
    _RcftRemoteVCGRxMgmntPackets_Type()
)
rcftRemoteVCGRxMgmntPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGRxMgmntPackets.setStatus("current")
_RcftRemoteVCGRxFCSErrMgmntPackets_Type = Counter32
_RcftRemoteVCGRxFCSErrMgmntPackets_Object = MibTableColumn
rcftRemoteVCGRxFCSErrMgmntPackets = _RcftRemoteVCGRxFCSErrMgmntPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1, 1, 4),
    _RcftRemoteVCGRxFCSErrMgmntPackets_Type()
)
rcftRemoteVCGRxFCSErrMgmntPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGRxFCSErrMgmntPackets.setStatus("current")
_RcftRemoteVCGRxLenErrPackets_Type = Counter32
_RcftRemoteVCGRxLenErrPackets_Object = MibTableColumn
rcftRemoteVCGRxLenErrPackets = _RcftRemoteVCGRxLenErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1, 1, 5),
    _RcftRemoteVCGRxLenErrPackets_Type()
)
rcftRemoteVCGRxLenErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGRxLenErrPackets.setStatus("current")
_RcftRemoteVCGRxFCSErrClientPackets_Type = Counter32
_RcftRemoteVCGRxFCSErrClientPackets_Object = MibTableColumn
rcftRemoteVCGRxFCSErrClientPackets = _RcftRemoteVCGRxFCSErrClientPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1, 1, 6),
    _RcftRemoteVCGRxFCSErrClientPackets_Type()
)
rcftRemoteVCGRxFCSErrClientPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGRxFCSErrClientPackets.setStatus("current")
_RcftRemoteVCGRxThecErrPackets_Type = Counter32
_RcftRemoteVCGRxThecErrPackets_Object = MibTableColumn
rcftRemoteVCGRxThecErrPackets = _RcftRemoteVCGRxThecErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1, 1, 7),
    _RcftRemoteVCGRxThecErrPackets_Type()
)
rcftRemoteVCGRxThecErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGRxThecErrPackets.setStatus("current")
_RcftRemoteVCGRxEhecErrPackets_Type = Counter32
_RcftRemoteVCGRxEhecErrPackets_Object = MibTableColumn
rcftRemoteVCGRxEhecErrPackets = _RcftRemoteVCGRxEhecErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1, 1, 8),
    _RcftRemoteVCGRxEhecErrPackets_Type()
)
rcftRemoteVCGRxEhecErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGRxEhecErrPackets.setStatus("current")
_RcftRemoteVCGRxCIDErrPackets_Type = Counter32
_RcftRemoteVCGRxCIDErrPackets_Object = MibTableColumn
rcftRemoteVCGRxCIDErrPackets = _RcftRemoteVCGRxCIDErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1, 1, 9),
    _RcftRemoteVCGRxCIDErrPackets_Type()
)
rcftRemoteVCGRxCIDErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGRxCIDErrPackets.setStatus("current")
_RcftRemoteVCGRxSpareErrPackets_Type = Counter32
_RcftRemoteVCGRxSpareErrPackets_Object = MibTableColumn
rcftRemoteVCGRxSpareErrPackets = _RcftRemoteVCGRxSpareErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1, 1, 10),
    _RcftRemoteVCGRxSpareErrPackets_Type()
)
rcftRemoteVCGRxSpareErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGRxSpareErrPackets.setStatus("current")
_RcftRemoteVCGRxChecCorPackets_Type = Counter32
_RcftRemoteVCGRxChecCorPackets_Object = MibTableColumn
rcftRemoteVCGRxChecCorPackets = _RcftRemoteVCGRxChecCorPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1, 1, 11),
    _RcftRemoteVCGRxChecCorPackets_Type()
)
rcftRemoteVCGRxChecCorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGRxChecCorPackets.setStatus("current")
_RcftRemoteVCGRxThecCorPackets_Type = Counter32
_RcftRemoteVCGRxThecCorPackets_Object = MibTableColumn
rcftRemoteVCGRxThecCorPackets = _RcftRemoteVCGRxThecCorPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1, 1, 12),
    _RcftRemoteVCGRxThecCorPackets_Type()
)
rcftRemoteVCGRxThecCorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGRxThecCorPackets.setStatus("current")
_RcftRemoteVCGRxEhecCorPackets_Type = Counter32
_RcftRemoteVCGRxEhecCorPackets_Object = MibTableColumn
rcftRemoteVCGRxEhecCorPackets = _RcftRemoteVCGRxEhecCorPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1, 1, 13),
    _RcftRemoteVCGRxEhecCorPackets_Type()
)
rcftRemoteVCGRxEhecCorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGRxEhecCorPackets.setStatus("current")
_RcftRemoteVCGRxBytes_Type = Counter32
_RcftRemoteVCGRxBytes_Object = MibTableColumn
rcftRemoteVCGRxBytes = _RcftRemoteVCGRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1, 1, 14),
    _RcftRemoteVCGRxBytes_Type()
)
rcftRemoteVCGRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGRxBytes.setStatus("current")
_RcftRemoteVCGTxClientPackets_Type = Counter32
_RcftRemoteVCGTxClientPackets_Object = MibTableColumn
rcftRemoteVCGTxClientPackets = _RcftRemoteVCGTxClientPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1, 1, 15),
    _RcftRemoteVCGTxClientPackets_Type()
)
rcftRemoteVCGTxClientPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGTxClientPackets.setStatus("current")
_RcftRemoteVCGTxIdlePackets_Type = Counter32
_RcftRemoteVCGTxIdlePackets_Object = MibTableColumn
rcftRemoteVCGTxIdlePackets = _RcftRemoteVCGTxIdlePackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1, 1, 16),
    _RcftRemoteVCGTxIdlePackets_Type()
)
rcftRemoteVCGTxIdlePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGTxIdlePackets.setStatus("current")
_RcftRemoteVCGTxMgmntPackets_Type = Counter32
_RcftRemoteVCGTxMgmntPackets_Object = MibTableColumn
rcftRemoteVCGTxMgmntPackets = _RcftRemoteVCGTxMgmntPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1, 1, 17),
    _RcftRemoteVCGTxMgmntPackets_Type()
)
rcftRemoteVCGTxMgmntPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGTxMgmntPackets.setStatus("current")
_RcftRemoteVCGTxBytes_Type = Counter32
_RcftRemoteVCGTxBytes_Object = MibTableColumn
rcftRemoteVCGTxBytes = _RcftRemoteVCGTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1, 1, 18),
    _RcftRemoteVCGTxBytes_Type()
)
rcftRemoteVCGTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGTxBytes.setStatus("current")
_RcftRemoteVCGFluxTimer_Type = Counter32
_RcftRemoteVCGFluxTimer_Object = MibTableColumn
rcftRemoteVCGFluxTimer = _RcftRemoteVCGFluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 2, 1, 1, 19),
    _RcftRemoteVCGFluxTimer_Type()
)
rcftRemoteVCGFluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRemoteVCGFluxTimer.setStatus("current")
_RcftRemoteVCGTraps_ObjectIdentity = ObjectIdentity
rcftRemoteVCGTraps = _RcftRemoteVCGTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 10)
)
rcftRemoteEthFePortEntry.registerAugmentions(
    ("RC002-REMOTE-DEVICE-MIB",
     "rcftRemoteEthFeStatisticEntry")
)
rcftRemoteEthFeStatisticEntry.setIndexNames(*rcftRemoteEthFePortEntry.getIndexNames())
rcftRemoteEthFxPortEntry.registerAugmentions(
    ("RC002-REMOTE-DEVICE-MIB",
     "rcftRemoteEthFxStatisticEntry")
)
rcftRemoteEthFxStatisticEntry.setIndexNames(*rcftRemoteEthFxPortEntry.getIndexNames())
rcftRemoteDeviceE1Entry.registerAugmentions(
    ("RC002-REMOTE-DEVICE-MIB",
     "rcftRemoteE1StatisticEntry")
)
rcftRemoteE1StatisticEntry.setIndexNames(*rcftRemoteDeviceE1Entry.getIndexNames())
rcftRemoteDS3E3PortEntry.registerAugmentions(
    ("RC002-REMOTE-DEVICE-MIB",
     "rcftRemoteDS3E3StatisticEntry")
)
rcftRemoteDS3E3StatisticEntry.setIndexNames(*rcftRemoteDS3E3PortEntry.getIndexNames())
rcftRemoteDS1PortEntry.registerAugmentions(
    ("RC002-REMOTE-DEVICE-MIB",
     "rcftRemoteDS1StatisticEntry")
)
rcftRemoteDS1StatisticEntry.setIndexNames(*rcftRemoteDS1PortEntry.getIndexNames())
rcftRemoteMoudleEthFeEntry.registerAugmentions(
    ("RC002-REMOTE-DEVICE-MIB",
     "rcftRemoteMoudleEthFeStatisticEntry")
)
rcftRemoteMoudleEthFeStatisticEntry.setIndexNames(*rcftRemoteMoudleEthFeEntry.getIndexNames())
rcftRemoteMoudleE1Entry.registerAugmentions(
    ("RC002-REMOTE-DEVICE-MIB",
     "rcftRemoteMoudleE1StatisticEntry")
)
rcftRemoteMoudleE1StatisticEntry.setIndexNames(*rcftRemoteMoudleE1Entry.getIndexNames())
rcftRemoteVCGEntry.registerAugmentions(
    ("RC002-REMOTE-DEVICE-MIB",
     "rcftRemoteVCGStatisticEntry")
)
rcftRemoteVCGStatisticEntry.setIndexNames(*rcftRemoteVCGEntry.getIndexNames())

# Managed Objects groups


# Notification objects

rcftRemoteDevExistTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 2, 1)
)
rcftRemoteDevExistTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceExist")
)
if mibBuilder.loadTexts:
    rcftRemoteDevExistTrap.setStatus(
        "current"
    )

rcftRemoteDevVoltTooHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 2, 2)
)
rcftRemoteDevVoltTooHighTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteSysVoltageStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDevVoltTooHighTrap.setStatus(
        "current"
    )

rcftRemoteDevVoltTooLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 2, 3)
)
rcftRemoteDevVoltTooLowTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteSysVoltageStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDevVoltTooLowTrap.setStatus(
        "current"
    )

rcftRemoteDevTmptTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 2, 4)
)
rcftRemoteDevTmptTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteSysTemperature")
)
if mibBuilder.loadTexts:
    rcftRemoteDevTmptTrap.setStatus(
        "current"
    )

rcftRemoteDevPowerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 2, 5)
)
rcftRemoteDevPowerDownTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDevicePowerDown")
)
if mibBuilder.loadTexts:
    rcftRemoteDevPowerDownTrap.setStatus(
        "current"
    )

rcftRemoteDevPSChannelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 2, 6)
)
rcftRemoteDevPSChannelTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDevPSChannelTrap.setStatus(
        "current"
    )

rcftRemoteDevSPChannelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 1, 2, 7)
)
rcftRemoteDevSPChannelTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDeviceStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDevSPChannelTrap.setStatus(
        "current"
    )

rcftRemoteEthFeLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 1, 2, 1)
)
rcftRemoteEthFeLinkTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFeLinkStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFeLinkTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortRLKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 1)
)
rcftRemoteEthFxPortRLKTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxPortRLK")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortRLKTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortTLKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 2)
)
rcftRemoteEthFxPortTLKTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxPortTLK")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortTLKTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortTxPowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 3)
)
rcftRemoteEthFxPortTxPowerTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxPortTxPowerAbnormal")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortTxPowerTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortRxSensitiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 4)
)
rcftRemoteEthFxPortRxSensitiveTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxPortRxSensitiveAbnormal")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortRxSensitiveTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortLaserTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 5)
)
rcftRemoteEthFxPortLaserTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxPortLaserAbnormal")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortLaserTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortSDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 6)
)
rcftRemoteEthFxPortSDTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxPortSD")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortSDTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 7)
)
rcftRemoteEthFxPortLinkTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxPortLink")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortLinkTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortExitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 8)
)
rcftRemoteEthFxPortExitTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxPortExist")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortExitTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortTempHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 9)
)
rcftRemoteEthFxPortTempHighTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortTempHighTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortTempLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 10)
)
rcftRemoteEthFxPortTempLowTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortTempLowTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortVoltageHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 11)
)
rcftRemoteEthFxPortVoltageHighTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortVoltageHighTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortVoltageLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 12)
)
rcftRemoteEthFxPortVoltageLowTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortVoltageLowTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortOffsetCurrHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 13)
)
rcftRemoteEthFxPortOffsetCurrHighTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortOffsetCurrHighTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortOffsetCurrLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 14)
)
rcftRemoteEthFxPortOffsetCurrLowTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortOffsetCurrLowTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortSendPowerHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 15)
)
rcftRemoteEthFxPortSendPowerHighTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortSendPowerHighTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortSendPowerLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 16)
)
rcftRemoteEthFxPortSendPowerLowTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortSendPowerLowTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortRecvPowerHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 17)
)
rcftRemoteEthFxPortRecvPowerHighTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortRecvPowerHighTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortRecvPowerLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 18)
)
rcftRemoteEthFxPortRecvPowerLowTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortRecvPowerLowTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortRemotePowerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 19)
)
rcftRemoteEthFxPortRemotePowerDownTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortRemotePowerDownTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortInputSignalLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 20)
)
rcftRemoteEthFxPortInputSignalLosTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxPortSFPInfo")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortInputSignalLosTrap.setStatus(
        "current"
    )

rcftRemoteEthFxPortTempHighWarnning = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 21)
)
rcftRemoteEthFxPortTempHighWarnning.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortTempHighWarnning.setStatus(
        "current"
    )

rcftRemoteEthFxPortTempLowWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 22)
)
rcftRemoteEthFxPortTempLowWarning.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoWarningStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortTempLowWarning.setStatus(
        "current"
    )

rcftRemoteEthFxPortVoltageHighWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 23)
)
rcftRemoteEthFxPortVoltageHighWarning.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoWarningStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortVoltageHighWarning.setStatus(
        "current"
    )

rcftRemoteEthFxPortVoltageLowWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 24)
)
rcftRemoteEthFxPortVoltageLowWarning.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoWarningStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortVoltageLowWarning.setStatus(
        "current"
    )

rcftRemoteEthFxPortOffsetCurrHighWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 25)
)
rcftRemoteEthFxPortOffsetCurrHighWarning.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoWarningStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortOffsetCurrHighWarning.setStatus(
        "current"
    )

rcftRemoteEthFxPortOffsetCurrLowWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 26)
)
rcftRemoteEthFxPortOffsetCurrLowWarning.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoWarningStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortOffsetCurrLowWarning.setStatus(
        "current"
    )

rcftRemoteEthFxPortSendPowerHighWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 27)
)
rcftRemoteEthFxPortSendPowerHighWarning.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoWarningStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortSendPowerHighWarning.setStatus(
        "current"
    )

rcftRemoteEthFxPortSendPowerLowWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 28)
)
rcftRemoteEthFxPortSendPowerLowWarning.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoWarningStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortSendPowerLowWarning.setStatus(
        "current"
    )

rcftRemoteEthFxPortRecvPowerHighWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 29)
)
rcftRemoteEthFxPortRecvPowerHighWarning.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoWarningStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortRecvPowerHighWarning.setStatus(
        "current"
    )

rcftRemoteEthFxPortRecvPowerLowWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 2, 2, 2, 30)
)
rcftRemoteEthFxPortRecvPowerLowWarning.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteEthFxSFPDiagnoWarningStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteEthFxPortRecvPowerLowWarning.setStatus(
        "current"
    )

rcftRemoteDevE1LOSTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 2, 1)
)
rcftRemoteDevE1LOSTRAP.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteE1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDevE1LOSTRAP.setStatus(
        "current"
    )

rcftRemoteDevE1LOFTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 2, 2)
)
rcftRemoteDevE1LOFTRAP.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteE1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDevE1LOFTRAP.setStatus(
        "current"
    )

rcftRemoteDevE1CRCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 2, 3)
)
rcftRemoteDevE1CRCTRAP.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteE1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDevE1CRCTRAP.setStatus(
        "current"
    )

rcftRemoteDevE1AISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 2, 4)
)
rcftRemoteDevE1AISTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteE1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDevE1AISTrap.setStatus(
        "current"
    )

rcftRemoteDevE1TransErrorCodeMore10E_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 2, 5)
)
rcftRemoteDevE1TransErrorCodeMore10E_3.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteE1TransErrorCode")
)
if mibBuilder.loadTexts:
    rcftRemoteDevE1TransErrorCodeMore10E_3.setStatus(
        "current"
    )

rcftRemoteDevE1TransErrorCodeMore10E_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 2, 6)
)
rcftRemoteDevE1TransErrorCodeMore10E_6.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteE1TransErrorCode")
)
if mibBuilder.loadTexts:
    rcftRemoteDevE1TransErrorCodeMore10E_6.setStatus(
        "current"
    )

rcftRemoteDevToLocalDevE1LOSTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 2, 7)
)
rcftRemoteDevToLocalDevE1LOSTRAP.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteToLocalE1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDevToLocalDevE1LOSTRAP.setStatus(
        "current"
    )

rcftRemoteDevToLocalDevE1LOFTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 2, 8)
)
rcftRemoteDevToLocalDevE1LOFTRAP.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteToLocalE1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDevToLocalDevE1LOFTRAP.setStatus(
        "current"
    )

rcftRemoteDevToLocalDevE1CRCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 2, 9)
)
rcftRemoteDevToLocalDevE1CRCTRAP.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteToLocalE1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDevToLocalDevE1CRCTRAP.setStatus(
        "current"
    )

rcftRemoteDevToLocalDevE1AISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 2, 10)
)
rcftRemoteDevToLocalDevE1AISTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteToLocalE1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDevToLocalDevE1AISTrap.setStatus(
        "current"
    )

rcftRemoteDevE1CVTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 2, 11)
)
rcftRemoteDevE1CVTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteE1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDevE1CVTrap.setStatus(
        "current"
    )

rcftRemoteDevE1LOMFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 2, 12)
)
rcftRemoteDevE1LOMFTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteE1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDevE1LOMFTrap.setStatus(
        "current"
    )

rcftRemoteDevT1LOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 2, 13)
)
rcftRemoteDevT1LOSTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteT1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDevT1LOSTrap.setStatus(
        "current"
    )

rcftRemoteDevT1AISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 2, 14)
)
rcftRemoteDevT1AISTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteT1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDevT1AISTrap.setStatus(
        "current"
    )

rcftRemoteDevE1TSDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 2, 15)
)
rcftRemoteDevE1TSDTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteE1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDevE1TSDTrap.setStatus(
        "current"
    )

rcftRemoteE1PortToLTSDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 2, 16)
)
rcftRemoteE1PortToLTSDTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteE1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteE1PortToLTSDTrap.setStatus(
        "current"
    )

rcftRemoteDevE1RDITrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 2, 17)
)
rcftRemoteDevE1RDITrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteE1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDevE1RDITrap.setStatus(
        "current"
    )

rcftRemoteE1PortToLLOMFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 3, 2, 18)
)
rcftRemoteE1PortToLLOMFTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteE1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteE1PortToLLOMFTrap.setStatus(
        "current"
    )

rcftRemoteSHDSLPortLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 10, 1)
)
rcftRemoteSHDSLPortLOSTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteSHDSLPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortLOSTrap.setStatus(
        "current"
    )

rcftRemoteSHDSLPortLOSWTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 10, 2)
)
rcftRemoteSHDSLPortLOSWTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteSHDSLPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortLOSWTrap.setStatus(
        "current"
    )

rcftRemoteSHDSLPortLINKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 10, 3)
)
rcftRemoteSHDSLPortLINKTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteSHDSLPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortLINKTrap.setStatus(
        "current"
    )

rcftRemoteSHDSLPortFECTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 10, 4)
)
rcftRemoteSHDSLPortFECTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteSHDSLPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortFECTrap.setStatus(
        "current"
    )

rcftRemoteSHDSLPortCRCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 10, 5)
)
rcftRemoteSHDSLPortCRCTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteSHDSLPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortCRCTrap.setStatus(
        "current"
    )

rcftRemoteSHDSLPortSNRThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 10, 6)
)
rcftRemoteSHDSLPortSNRThresholdTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteSHDSLPortSNRThreshold")
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortSNRThresholdTrap.setStatus(
        "current"
    )

rcftRemoteSHDSLPortAttenuationThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 10, 7)
)
rcftRemoteSHDSLPortAttenuationThresholdTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteSHDSLPortAttenuationThreshold")
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortAttenuationThresholdTrap.setStatus(
        "current"
    )

rcftRemoteSHDSLPortLOSThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 10, 8)
)
rcftRemoteSHDSLPortLOSThresholdTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteSHDSLPortLOSThreshold")
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortLOSThresholdTrap.setStatus(
        "current"
    )

rcftRemoteSHDSLPortLOSWThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 10, 9)
)
rcftRemoteSHDSLPortLOSWThresholdTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteSHDSLPortLOSWThreshold")
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortLOSWThresholdTrap.setStatus(
        "current"
    )

rcftRemoteSHDSLPortLOLKThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 10, 10)
)
rcftRemoteSHDSLPortLOLKThresholdTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteSHDSLPortLOLKThreshold")
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortLOLKThresholdTrap.setStatus(
        "current"
    )

rcftRemoteSHDSLPortESThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 4, 10, 11)
)
rcftRemoteSHDSLPortESThresholdTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteSHDSLPortESThreshold")
)
if mibBuilder.loadTexts:
    rcftRemoteSHDSLPortESThresholdTrap.setStatus(
        "current"
    )

rcftRemoteV35PortDCDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 3, 1)
)
rcftRemoteV35PortDCDTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteV35PortDCDTrap.setStatus(
        "current"
    )

rcftRemoteV35PortCTSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 3, 2)
)
rcftRemoteV35PortCTSTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteV35PortCTSTrap.setStatus(
        "current"
    )

rcftRemoteV35PortDTRTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 3, 3)
)
rcftRemoteV35PortDTRTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteV35PortDTRTrap.setStatus(
        "current"
    )

rcftRemoteV35PortRTSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 3, 4)
)
rcftRemoteV35PortRTSTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteV35PortRTSTrap.setStatus(
        "current"
    )

rcftRemoteV35PortCRCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 3, 5)
)
rcftRemoteV35PortCRCTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteV35PortCRCTrap.setStatus(
        "current"
    )

rcftRemoteV35PortPATTTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 3, 6)
)
rcftRemoteV35PortPATTTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteV35PortPATTTrap.setStatus(
        "current"
    )

rcftRemoteV35PortLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 3, 7)
)
rcftRemoteV35PortLOFTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteV35PortLOFTrap.setStatus(
        "current"
    )

rcftRemoteV35PortCVTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 3, 8)
)
rcftRemoteV35PortCVTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteV35PortCVTrap.setStatus(
        "current"
    )

rcftRemoteV35PortAISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 3, 9)
)
rcftRemoteV35PortAISTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteV35PortAISTrap.setStatus(
        "current"
    )

rcftRemoteV35PortToLLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 3, 10)
)
rcftRemoteV35PortToLLOFTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteV35PortToLLOFTrap.setStatus(
        "current"
    )

rcftRemoteV35PortToLCVTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 3, 11)
)
rcftRemoteV35PortToLCVTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteV35PortToLCVTrap.setStatus(
        "current"
    )

rcftRemoteV35PortToLAISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 3, 12)
)
rcftRemoteV35PortToLAISTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteV35PortToLAISTrap.setStatus(
        "current"
    )

rcftRemoteV35PortDSRTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 5, 3, 13)
)
rcftRemoteV35PortDSRTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteV35PortDSRTrap.setStatus(
        "current"
    )

rcftRemoteDS3E3PortAISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 10, 1)
)
rcftRemoteDS3E3PortAISTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortAISTrap.setStatus(
        "current"
    )

rcftRemoteDS3E3PortLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 10, 2)
)
rcftRemoteDS3E3PortLOSTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortLOSTrap.setStatus(
        "current"
    )

rcftRemoteDS3E3PortLOLTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 10, 3)
)
rcftRemoteDS3E3PortLOLTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortLOLTrap.setStatus(
        "current"
    )

rcftRemoteDS3E3PortDMOTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 10, 4)
)
rcftRemoteDS3E3PortDMOTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortDMOTrap.setStatus(
        "current"
    )

rcftRemoteDS3E3PortCVTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 10, 5)
)
rcftRemoteDS3E3PortCVTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortCVTrap.setStatus(
        "current"
    )

rcftRemoteDS3E3PortCRCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 10, 6)
)
rcftRemoteDS3E3PortCRCTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortCRCTrap.setStatus(
        "current"
    )

rcftRemoteDS3E3PortToLAISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 10, 7)
)
rcftRemoteDS3E3PortToLAISTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortToLAISTrap.setStatus(
        "current"
    )

rcftRemoteDS3E3PortToLLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 10, 8)
)
rcftRemoteDS3E3PortToLLOSTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortToLLOSTrap.setStatus(
        "current"
    )

rcftRemoteDS3E3PortToLLOLTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 10, 9)
)
rcftRemoteDS3E3PortToLLOLTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortToLLOLTrap.setStatus(
        "current"
    )

rcftRemoteDS3E3PortToLDMOTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 10, 10)
)
rcftRemoteDS3E3PortToLDMOTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortToLDMOTrap.setStatus(
        "current"
    )

rcftRemoteDS3E3PortToLCVTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 10, 11)
)
rcftRemoteDS3E3PortToLCVTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortToLCVTrap.setStatus(
        "current"
    )

rcftRemoteDS3E3PortToLCRCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 10, 12)
)
rcftRemoteDS3E3PortToLCRCTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortToLCRCTrap.setStatus(
        "current"
    )

rcftRemoteDS3E3PortLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 10, 13)
)
rcftRemoteDS3E3PortLOFTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortLOFTrap.setStatus(
        "current"
    )

rcftRemoteDS3E3PortToLLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 10, 14)
)
rcftRemoteDS3E3PortToLLOFTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortToLLOFTrap.setStatus(
        "current"
    )

rcftRemoteDS3E3PortRAITrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 10, 15)
)
rcftRemoteDS3E3PortRAITrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortRAITrap.setStatus(
        "current"
    )

rcftRemoteDS3E3PortToLRAITrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 10, 16)
)
rcftRemoteDS3E3PortToLRAITrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortToLRAITrap.setStatus(
        "current"
    )

rcftRemoteDS3E3PortOOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 10, 17)
)
rcftRemoteDS3E3PortOOFTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortOOFTrap.setStatus(
        "current"
    )

rcftRemoteDS3E3PortToLOOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 6, 10, 18)
)
rcftRemoteDS3E3PortToLOOFTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS3E3PortToLOOFTrap.setStatus(
        "current"
    )

rcftRemotePdhPortLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 10, 1)
)
rcftRemotePdhPortLOSTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemotePdhPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemotePdhPortLOSTrap.setStatus(
        "current"
    )

rcftRemotePdhPortLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 10, 2)
)
rcftRemotePdhPortLOFTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemotePdhPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemotePdhPortLOFTrap.setStatus(
        "current"
    )

rcftRemotePdhPortE3Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 10, 3)
)
rcftRemotePdhPortE3Trap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemotePdhPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemotePdhPortE3Trap.setStatus(
        "current"
    )

rcftRemotePdhPortE6Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 10, 4)
)
rcftRemotePdhPortE6Trap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemotePdhPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemotePdhPortE6Trap.setStatus(
        "current"
    )

rcftRemotePdhPortToLLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 10, 5)
)
rcftRemotePdhPortToLLOSTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemotePdhPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemotePdhPortToLLOSTrap.setStatus(
        "current"
    )

rcftRemotePdhPortToLLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 10, 6)
)
rcftRemotePdhPortToLLOFTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemotePdhPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemotePdhPortToLLOFTrap.setStatus(
        "current"
    )

rcftRemotePdhPortToLE3Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 10, 7)
)
rcftRemotePdhPortToLE3Trap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemotePdhPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemotePdhPortToLE3Trap.setStatus(
        "current"
    )

rcftRemotePdhPortToLE6rap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 10, 8)
)
rcftRemotePdhPortToLE6rap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemotePdhPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemotePdhPortToLE6rap.setStatus(
        "current"
    )

rcftRemotePdhPortToRPowerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 7, 10, 9)
)
rcftRemotePdhPortToRPowerDown.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemotePdhPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemotePdhPortToRPowerDown.setStatus(
        "current"
    )

rcftRemoteDS1PortAISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 10, 1)
)
rcftRemoteDS1PortAISTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS1PortAISTrap.setStatus(
        "current"
    )

rcftRemoteDS1PortLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 10, 2)
)
rcftRemoteDS1PortLOSTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS1PortLOSTrap.setStatus(
        "current"
    )

rcftRemoteDS1PortToLAISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 10, 3)
)
rcftRemoteDS1PortToLAISTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS1PortToLAISTrap.setStatus(
        "current"
    )

rcftRemoteDS1PortToLLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 10, 4)
)
rcftRemoteDS1PortToLLOSTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS1PortToLLOSTrap.setStatus(
        "current"
    )

rcftRemoteDS1PortLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 10, 5)
)
rcftRemoteDS1PortLOFTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS1PortLOFTrap.setStatus(
        "current"
    )

rcftRemoteDS1PortCRCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 10, 6)
)
rcftRemoteDS1PortCRCTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS1PortCRCTrap.setStatus(
        "current"
    )

rcftRemoteDS1PortToLLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 10, 7)
)
rcftRemoteDS1PortToLLOFTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS1PortToLLOFTrap.setStatus(
        "current"
    )

rcftRemoteDS1PortToLCRCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 10, 8)
)
rcftRemoteDS1PortToLCRCTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS1PortToLCRCTrap.setStatus(
        "current"
    )

rcftRemoteDS1PortFaultPassIndicatorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 10, 9)
)
rcftRemoteDS1PortFaultPassIndicatorTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS1PortFaultPassIndicator")
)
if mibBuilder.loadTexts:
    rcftRemoteDS1PortFaultPassIndicatorTrap.setStatus(
        "current"
    )

rcftRemoteDS1PortDMOTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 10, 10)
)
rcftRemoteDS1PortDMOTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS1PortDMOTrap.setStatus(
        "current"
    )

rcftRemoteDS1PortCVTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 10, 11)
)
rcftRemoteDS1PortCVTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS1PortCVTrap.setStatus(
        "current"
    )

rcftRemoteDS1PortYELTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 10, 12)
)
rcftRemoteDS1PortYELTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS1PortYELTrap.setStatus(
        "current"
    )

rcftRemoteDS1PortREDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 8, 10, 13)
)
rcftRemoteDS1PortREDTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteDS1PortREDTrap.setStatus(
        "current"
    )

rcftRemoteMoudleExistTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 1, 10, 1)
)
rcftRemoteMoudleExistTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteMoudleExist")
)
if mibBuilder.loadTexts:
    rcftRemoteMoudleExistTrap.setStatus(
        "current"
    )

rcftRemoteMoudleEthFeLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 2, 10, 1)
)
rcftRemoteMoudleEthFeLinkTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteMoudleEthFeStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteMoudleEthFeLinkTrap.setStatus(
        "current"
    )

rcftRemoteMoudlePdhLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 3, 10, 1)
)
rcftRemoteMoudlePdhLOSTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteMoudlePdhAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteMoudlePdhLOSTrap.setStatus(
        "current"
    )

rcftRemoteMoudlePdhLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 3, 10, 2)
)
rcftRemoteMoudlePdhLOFTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteMoudlePdhAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteMoudlePdhLOFTrap.setStatus(
        "current"
    )

rcftRemoteMoudleE1LOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 10, 1)
)
rcftRemoteMoudleE1LOSTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteMoudleE1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1LOSTrap.setStatus(
        "current"
    )

rcftRemoteMoudleE1AISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 10, 2)
)
rcftRemoteMoudleE1AISTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteMoudleE1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1AISTrap.setStatus(
        "current"
    )

rcftRemoteMoudleE1CRCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 10, 3)
)
rcftRemoteMoudleE1CRCTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteMoudleE1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1CRCTrap.setStatus(
        "current"
    )

rcftRemoteMoudleE1CVTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 10, 4)
)
rcftRemoteMoudleE1CVTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteMoudleE1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1CVTrap.setStatus(
        "current"
    )

rcftRemoteMoudleE1LOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 10, 5)
)
rcftRemoteMoudleE1LOFTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteMoudleE1AlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1LOFTrap.setStatus(
        "current"
    )

rcftRemoteMoudleE1ErrorCodeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 9, 4, 10, 6)
)
rcftRemoteMoudleE1ErrorCodeTrap.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteMoudleE1Status")
)
if mibBuilder.loadTexts:
    rcftRemoteMoudleE1ErrorCodeTrap.setStatus(
        "current"
    )

rcftRemoteVideoPortSignalLos = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 11, 10, 1)
)
rcftRemoteVideoPortSignalLos.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteVideoPortStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteVideoPortSignalLos.setStatus(
        "current"
    )

rcftRemoteVideoPortSignalInLos = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 11, 10, 2)
)
rcftRemoteVideoPortSignalInLos.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteVideoPortStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteVideoPortSignalInLos.setStatus(
        "current"
    )

rcftRemoteVideoPortSignalOutLos = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 11, 10, 3)
)
rcftRemoteVideoPortSignalOutLos.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteVideoPortStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteVideoPortSignalOutLos.setStatus(
        "current"
    )

rcftRemoteVCGGIDTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 10, 1)
)
rcftRemoteVCGGIDTraps.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteVCGAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteVCGGIDTraps.setStatus(
        "current"
    )

rcftRemoteVCGLOATraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 10, 2)
)
rcftRemoteVCGLOATraps.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteVCGAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteVCGLOATraps.setStatus(
        "current"
    )

rcftRemoteVCGLFDTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 10, 3)
)
rcftRemoteVCGLFDTraps.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteVCGAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteVCGLFDTraps.setStatus(
        "current"
    )

rcftRemoteVCGCSFTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 10, 4)
)
rcftRemoteVCGCSFTraps.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteVCGAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteVCGCSFTraps.setStatus(
        "current"
    )

rcftRemoteVCGTLCTTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 10, 5)
)
rcftRemoteVCGTLCTTraps.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteVCGAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteVCGTLCTTraps.setStatus(
        "current"
    )

rcftRemoteVCGTLCRTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 10, 6)
)
rcftRemoteVCGTLCRTraps.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteVCGAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteVCGTLCRTraps.setStatus(
        "current"
    )

rcftRemoteVCGToLGIDTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 10, 7)
)
rcftRemoteVCGToLGIDTraps.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteVCGAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteVCGToLGIDTraps.setStatus(
        "current"
    )

rcftRemoteVCGToLLOATraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 10, 8)
)
rcftRemoteVCGToLLOATraps.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteVCGAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteVCGToLLOATraps.setStatus(
        "current"
    )

rcftRemoteVCGToLLFDTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 10, 9)
)
rcftRemoteVCGToLLFDTraps.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteVCGAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteVCGToLLFDTraps.setStatus(
        "current"
    )

rcftRemoteVCGMemberLOMTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 10, 10)
)
rcftRemoteVCGMemberLOMTraps.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteVCGMemberAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteVCGMemberLOMTraps.setStatus(
        "current"
    )

rcftRemoteVCGMemberSQMTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 10, 11)
)
rcftRemoteVCGMemberSQMTraps.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteVCGMemberAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteVCGMemberSQMTraps.setStatus(
        "current"
    )

rcftRemoteVCGMemberCRCTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 10, 12)
)
rcftRemoteVCGMemberCRCTraps.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteVCGMemberAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteVCGMemberCRCTraps.setStatus(
        "current"
    )

rcftRemoteVCGMemberLOATraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 10, 13)
)
rcftRemoteVCGMemberLOATraps.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteVCGMemberAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteVCGMemberLOATraps.setStatus(
        "current"
    )

rcftRemoteVCGToLMemberLOMTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 10, 14)
)
rcftRemoteVCGToLMemberLOMTraps.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteToLVCGMemberAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteVCGToLMemberLOMTraps.setStatus(
        "current"
    )

rcftRemoteVCGToLMemberSQMTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 10, 15)
)
rcftRemoteVCGToLMemberSQMTraps.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteToLVCGMemberAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteVCGToLMemberSQMTraps.setStatus(
        "current"
    )

rcftRemoteVCGToLMemberCRCTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 10, 16)
)
rcftRemoteVCGToLMemberCRCTraps.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteToLVCGMemberAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteVCGToLMemberCRCTraps.setStatus(
        "current"
    )

rcftRemoteVCGToLMemberLOATraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 6, 16, 10, 17)
)
rcftRemoteVCGToLMemberLOATraps.setObjects(
    ("RC002-REMOTE-DEVICE-MIB", "rcftRemoteToLVCGMemberAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftRemoteVCGToLMemberLOATraps.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RC002-REMOTE-DEVICE-MIB",
    **{"rcftRemoteDeviceMib": rcftRemoteDeviceMib,
       "rcftRemoteDeviceSystemMIB": rcftRemoteDeviceSystemMIB,
       "rcftRemoteDeviceSysObjects": rcftRemoteDeviceSysObjects,
       "rcftRemoteDeviceSysTable": rcftRemoteDeviceSysTable,
       "rcftRemoteDeviceSysEntry": rcftRemoteDeviceSysEntry,
       "rcftRemoteDeviceIndex": rcftRemoteDeviceIndex,
       "rcftRemoteDeviceExist": rcftRemoteDeviceExist,
       "rcftRemoteDeviceType": rcftRemoteDeviceType,
       "rcftRemoteDeviceLocalPortType": rcftRemoteDeviceLocalPortType,
       "rcftRemoteDeviceLocalPortIndex": rcftRemoteDeviceLocalPortIndex,
       "rcftRemoteDeviceVersionInfo": rcftRemoteDeviceVersionInfo,
       "rcftRemoteSysTemperature": rcftRemoteSysTemperature,
       "rcftRemoteSysVoltageStatus": rcftRemoteSysVoltageStatus,
       "rcftRemoteDeviceWorkMode": rcftRemoteDeviceWorkMode,
       "rcftRemoteDeviceFrameLen": rcftRemoteDeviceFrameLen,
       "rcftRemoteDeviceOrder": rcftRemoteDeviceOrder,
       "rcftRemoteDeviceConfigFlag": rcftRemoteDeviceConfigFlag,
       "rcftRemoteSlotAutoCutErrLineEn": rcftRemoteSlotAutoCutErrLineEn,
       "rcftRemotePowerSupply": rcftRemotePowerSupply,
       "rcftRemoteDevicePowerDown": rcftRemoteDevicePowerDown,
       "rcftRemoteDeviceClkMode": rcftRemoteDeviceClkMode,
       "rcftRemoteDeviceE1SubCardType": rcftRemoteDeviceE1SubCardType,
       "rcftRemoteDeviceGateway": rcftRemoteDeviceGateway,
       "rcftRemoteDeviceIP": rcftRemoteDeviceIP,
       "rcftRemoteDeviceSubnetMask": rcftRemoteDeviceSubnetMask,
       "rcftRemoteDeviceVLANID": rcftRemoteDeviceVLANID,
       "rcftRemoteDeviceCommunityRW": rcftRemoteDeviceCommunityRW,
       "rcftRemoteDeviceCommunityLength": rcftRemoteDeviceCommunityLength,
       "rcftRemoteDeviceCommunity": rcftRemoteDeviceCommunity,
       "rcftRemoteDeviceVoltageValue": rcftRemoteDeviceVoltageValue,
       "rcftRemoteDeviceStatus": rcftRemoteDeviceStatus,
       "rcftRemoteSubModuleExist": rcftRemoteSubModuleExist,
       "rcftRemoteMultiE1LoopOrder": rcftRemoteMultiE1LoopOrder,
       "rcftRemoteOrderTimeParameter": rcftRemoteOrderTimeParameter,
       "rcftRemoteOrderModeParameter": rcftRemoteOrderModeParameter,
       "rcftRemoteSDRAMBuf": rcftRemoteSDRAMBuf,
       "rcftRemoteRLPStatus": rcftRemoteRLPStatus,
       "rcftRemoteLALStatus": rcftRemoteLALStatus,
       "rcftRemoteRALStatus": rcftRemoteRALStatus,
       "rcftRemoteDeviceSwitchStatus": rcftRemoteDeviceSwitchStatus,
       "rcftRemoteDeviceMoudleExist": rcftRemoteDeviceMoudleExist,
       "rcftRemoteCardInformation": rcftRemoteCardInformation,
       "rcftRemoteSwitchType": rcftRemoteSwitchType,
       "rcftRemoteConnectMode": rcftRemoteConnectMode,
       "rcftRemoteQosEnable": rcftRemoteQosEnable,
       "rcftRemoteBaseCOS": rcftRemoteBaseCOS,
       "rcftRemoteDSCP": rcftRemoteDSCP,
       "rcftRemoteQueuesPolicy": rcftRemoteQueuesPolicy,
       "rcftRemoteMultiE1AlarmRejectOrder": rcftRemoteMultiE1AlarmRejectOrder,
       "rcftRemoteT1PortPulseWaveForm": rcftRemoteT1PortPulseWaveForm,
       "rcftRemoteT1PortCodeType": rcftRemoteT1PortCodeType,
       "rcftRemoteDeviceSabitMode": rcftRemoteDeviceSabitMode,
       "rcftRemoteDeviceApsWaitToRestore": rcftRemoteDeviceApsWaitToRestore,
       "rcftRemoteDeviceCLKChannel": rcftRemoteDeviceCLKChannel,
       "rcftRemoteDeviceRmcChannelType": rcftRemoteDeviceRmcChannelType,
       "rcftRemoteDeviceProductType": rcftRemoteDeviceProductType,
       "rcftRemoteDeviceProtocolVer": rcftRemoteDeviceProtocolVer,
       "rcftRemoteDeviceVenderCode": rcftRemoteDeviceVenderCode,
       "rcftRemoteDeviceModelID": rcftRemoteDeviceModelID,
       "rcftRemoteE1PortNumber": rcftRemoteE1PortNumber,
       "rcftRemoteDeviceVLANType": rcftRemoteDeviceVLANType,
       "rcftRemoteDeviceQoSPolicy": rcftRemoteDeviceQoSPolicy,
       "rcftRemoteDeviceApsE3SwitchDelay": rcftRemoteDeviceApsE3SwitchDelay,
       "rcftRemoteDeviceApsE6SwitchDelay": rcftRemoteDeviceApsE6SwitchDelay,
       "rcftRemoteDeviceVLANTagDirection": rcftRemoteDeviceVLANTagDirection,
       "rcftRemoteDeviceVLANTagModule": rcftRemoteDeviceVLANTagModule,
       "rcftRemoteDeviceISPTPID": rcftRemoteDeviceISPTPID,
       "rcftRemoteE1DS1PortType": rcftRemoteE1DS1PortType,
       "rcftRemoteDeviceE1FrameChannel": rcftRemoteDeviceE1FrameChannel,
       "rcftRemoteDeviceManageID": rcftRemoteDeviceManageID,
       "rcftRemoteDeviceMibUse": rcftRemoteDeviceMibUse,
       "rcftRemoteDeviceConfigFlagTable": rcftRemoteDeviceConfigFlagTable,
       "rcftRemoteDeviceConfigFlagEntry": rcftRemoteDeviceConfigFlagEntry,
       "rcftRemoteDeviceConfigFinishFlag": rcftRemoteDeviceConfigFinishFlag,
       "rcftRemoteDeviceSysTraps": rcftRemoteDeviceSysTraps,
       "rcftRemoteDevExistTrap": rcftRemoteDevExistTrap,
       "rcftRemoteDevVoltTooHighTrap": rcftRemoteDevVoltTooHighTrap,
       "rcftRemoteDevVoltTooLowTrap": rcftRemoteDevVoltTooLowTrap,
       "rcftRemoteDevTmptTrap": rcftRemoteDevTmptTrap,
       "rcftRemoteDevPowerDownTrap": rcftRemoteDevPowerDownTrap,
       "rcftRemoteDevPSChannelTrap": rcftRemoteDevPSChannelTrap,
       "rcftRemoteDevSPChannelTrap": rcftRemoteDevSPChannelTrap,
       "rcftRemoteDeviceEthMIB": rcftRemoteDeviceEthMIB,
       "rcftRemoteDeviceEthFeMIB": rcftRemoteDeviceEthFeMIB,
       "rcftRemoteDeviceEthFeObjects": rcftRemoteDeviceEthFeObjects,
       "rcftRemoteEthFePortTable": rcftRemoteEthFePortTable,
       "rcftRemoteEthFePortEntry": rcftRemoteEthFePortEntry,
       "rcftRemoteEthFeIndex": rcftRemoteEthFeIndex,
       "rcftRemoteEthFeLinkStatus": rcftRemoteEthFeLinkStatus,
       "rcftRemoteEthFeShutDown": rcftRemoteEthFeShutDown,
       "rcftRemoteEthFeAutoNegotiation": rcftRemoteEthFeAutoNegotiation,
       "rcftRemoteEthFeSpeed": rcftRemoteEthFeSpeed,
       "rcftRemoteEthFeDuplex": rcftRemoteEthFeDuplex,
       "rcftRemoteEthFeFlowControl": rcftRemoteEthFeFlowControl,
       "rcftRemoteEthFeRestrictSpeed": rcftRemoteEthFeRestrictSpeed,
       "rcftRemoteEthFeFaultPass": rcftRemoteEthFeFaultPass,
       "rcftRemoteEthFeDisabledByRemoteTP": rcftRemoteEthFeDisabledByRemoteTP,
       "rcftRemoteEthFeDisabledByFxToFeFP": rcftRemoteEthFeDisabledByFxToFeFP,
       "rcftRemoteEthFeTxRestrictSpeed": rcftRemoteEthFeTxRestrictSpeed,
       "rcftRemoteEthFeTag": rcftRemoteEthFeTag,
       "rcftRemoteEthFePortStatus": rcftRemoteEthFePortStatus,
       "rcftRemoteEthFeRestrictSpeedStep": rcftRemoteEthFeRestrictSpeedStep,
       "rcftRemoteEthFeOrderTimeParameter": rcftRemoteEthFeOrderTimeParameter,
       "rcftRemoteEthFeOrderModeParameter": rcftRemoteEthFeOrderModeParameter,
       "rcftRemoteEthFeOrder": rcftRemoteEthFeOrder,
       "rcftRemoteEthFePortStatusExtend": rcftRemoteEthFePortStatusExtend,
       "rcftRemoteEthFeStormControl": rcftRemoteEthFeStormControl,
       "rcftRemoteEthFePVID": rcftRemoteEthFePVID,
       "rcftRemoteEthFeDefaultCOS": rcftRemoteEthFeDefaultCOS,
       "rcftRemoteEthFeQoSPolicy": rcftRemoteEthFeQoSPolicy,
       "rcftRemoteEthFeStatisticTable": rcftRemoteEthFeStatisticTable,
       "rcftRemoteEthFeStatisticEntry": rcftRemoteEthFeStatisticEntry,
       "rcftRemoteEthFeTxPackets": rcftRemoteEthFeTxPackets,
       "rcftRemoteEthFeTxBytes": rcftRemoteEthFeTxBytes,
       "rcftRemoteEthFeRxPackets": rcftRemoteEthFeRxPackets,
       "rcftRemoteEthFeRxBytes": rcftRemoteEthFeRxBytes,
       "rcftRemoteEthFeRxLostPackets": rcftRemoteEthFeRxLostPackets,
       "rcftRemoteEthFeFluxTimer": rcftRemoteEthFeFluxTimer,
       "rcftRemoteEthFeTxLostPackets": rcftRemoteEthFeTxLostPackets,
       "rcftRemoteEthFePortConfTable": rcftRemoteEthFePortConfTable,
       "rcftRemoteEthFePortConfEntry": rcftRemoteEthFePortConfEntry,
       "rcftRemoteEthFeConfSpeed": rcftRemoteEthFeConfSpeed,
       "rcftRemoteEthFeConfDuplex": rcftRemoteEthFeConfDuplex,
       "rcftRemoteDeviceEthFeTraps": rcftRemoteDeviceEthFeTraps,
       "rcftRemoteEthFeLinkTrap": rcftRemoteEthFeLinkTrap,
       "rcftRemoteDeviceEthFxMIB": rcftRemoteDeviceEthFxMIB,
       "rcftRemoteDeviceEthFxObjects": rcftRemoteDeviceEthFxObjects,
       "rcftRemoteEthFxPortTable": rcftRemoteEthFxPortTable,
       "rcftRemoteEthFxPortEntry": rcftRemoteEthFxPortEntry,
       "rcftRemoteEthFxIndex": rcftRemoteEthFxIndex,
       "rcftRemoteEthFxFlowControl": rcftRemoteEthFxFlowControl,
       "rcftRemoteEthFxPortRLK": rcftRemoteEthFxPortRLK,
       "rcftRemoteEthFxPortTLK": rcftRemoteEthFxPortTLK,
       "rcftRemoteEthFxPortSD": rcftRemoteEthFxPortSD,
       "rcftRemoteEthFxPortTxPowerAbnormal": rcftRemoteEthFxPortTxPowerAbnormal,
       "rcftRemoteEthFxPortRxSensitiveAbnormal": rcftRemoteEthFxPortRxSensitiveAbnormal,
       "rcftRemoteEthFxPortLaserAbnormal": rcftRemoteEthFxPortLaserAbnormal,
       "rcftRemoteEthFxShutDown": rcftRemoteEthFxShutDown,
       "rcftRemoteEthFxModuleType": rcftRemoteEthFxModuleType,
       "rcftRemoteEthFxFaultPass": rcftRemoteEthFxFaultPass,
       "rcftRemoteEthFxPortLink": rcftRemoteEthFxPortLink,
       "rcftRemoteEthFxRxToTxFaultPass": rcftRemoteEthFxRxToTxFaultPass,
       "rcftRemoteEthFxTxDisabledByFR": rcftRemoteEthFxTxDisabledByFR,
       "rcftRemoteEthFxOrderTimeParameter": rcftRemoteEthFxOrderTimeParameter,
       "rcftRemoteEthFxOrderModeParameter": rcftRemoteEthFxOrderModeParameter,
       "rcftRemoteEthFxOrder": rcftRemoteEthFxOrder,
       "rcftRemoteEthFxPortExist": rcftRemoteEthFxPortExist,
       "rcftRemoteEthFxPortAuto": rcftRemoteEthFxPortAuto,
       "rcftRemoteEthFxModuleMaxSpeed": rcftRemoteEthFxModuleMaxSpeed,
       "rcftRemoteEthFxTranDistance": rcftRemoteEthFxTranDistance,
       "rcftRemoteEthFxModuleWaveLen": rcftRemoteEthFxModuleWaveLen,
       "rcftRemoteEthFxPortConnectorType": rcftRemoteEthFxPortConnectorType,
       "rcftRemoteEthFxPortTransmitMedia": rcftRemoteEthFxPortTransmitMedia,
       "rcftRemoteEthFxModuleManufacturer": rcftRemoteEthFxModuleManufacturer,
       "rcftRemoteEthFxModuleDescr": rcftRemoteEthFxModuleDescr,
       "rcftRemoteEthFxPortModuleVersion": rcftRemoteEthFxPortModuleVersion,
       "rcftRemoteEthFxModuleSerialNumber": rcftRemoteEthFxModuleSerialNumber,
       "rcftRemoteEthFxPortSFPDiagnoInfo": rcftRemoteEthFxPortSFPDiagnoInfo,
       "rcftRemoteEthFxSFPDiagnoAlarmStatus": rcftRemoteEthFxSFPDiagnoAlarmStatus,
       "rcftRemoteEthFxPortStatus": rcftRemoteEthFxPortStatus,
       "rcftRemoteEthFxUntag": rcftRemoteEthFxUntag,
       "rcftRemoteEthFxPVID": rcftRemoteEthFxPVID,
       "rcftRemoteEthFxPortSFPType": rcftRemoteEthFxPortSFPType,
       "rcftRemoteEthFxPortSFPInfo": rcftRemoteEthFxPortSFPInfo,
       "rcftRemoteEthFxPortLoopStatus": rcftRemoteEthFxPortLoopStatus,
       "rcftRemoteEthFxPortRxRestrictSpeed": rcftRemoteEthFxPortRxRestrictSpeed,
       "rcftRemoteEthFxPortTxRestrictSpeed": rcftRemoteEthFxPortTxRestrictSpeed,
       "rcftRemoteEthFxSFPDiagnoWarningStatus": rcftRemoteEthFxSFPDiagnoWarningStatus,
       "rcftRemoteEthFxPortLineOrClient": rcftRemoteEthFxPortLineOrClient,
       "rcftRemoteEthFxCOS": rcftRemoteEthFxCOS,
       "rcftRemoteEthFxStatisticTable": rcftRemoteEthFxStatisticTable,
       "rcftRemoteEthFxStatisticEntry": rcftRemoteEthFxStatisticEntry,
       "rcftRemoteEthFxTxPackets": rcftRemoteEthFxTxPackets,
       "rcftRemoteEthFxTxBytes": rcftRemoteEthFxTxBytes,
       "rcftRemoteEthFxRxPackets": rcftRemoteEthFxRxPackets,
       "rcftRemoteEthFxRxBytes": rcftRemoteEthFxRxBytes,
       "rcftRemoteEthFxRxLostPackets": rcftRemoteEthFxRxLostPackets,
       "rcftRemoteEthFxFluxTimer": rcftRemoteEthFxFluxTimer,
       "rcftRemoteEthFxTxLostPackets": rcftRemoteEthFxTxLostPackets,
       "rcftRemoteEthFx64TxBytes": rcftRemoteEthFx64TxBytes,
       "rcftRemoteEthFx64RxBytes": rcftRemoteEthFx64RxBytes,
       "rcftRemoteDeviceEthFxTraps": rcftRemoteDeviceEthFxTraps,
       "rcftRemoteEthFxPortRLKTrap": rcftRemoteEthFxPortRLKTrap,
       "rcftRemoteEthFxPortTLKTrap": rcftRemoteEthFxPortTLKTrap,
       "rcftRemoteEthFxPortTxPowerTrap": rcftRemoteEthFxPortTxPowerTrap,
       "rcftRemoteEthFxPortRxSensitiveTrap": rcftRemoteEthFxPortRxSensitiveTrap,
       "rcftRemoteEthFxPortLaserTrap": rcftRemoteEthFxPortLaserTrap,
       "rcftRemoteEthFxPortSDTrap": rcftRemoteEthFxPortSDTrap,
       "rcftRemoteEthFxPortLinkTrap": rcftRemoteEthFxPortLinkTrap,
       "rcftRemoteEthFxPortExitTrap": rcftRemoteEthFxPortExitTrap,
       "rcftRemoteEthFxPortTempHighTrap": rcftRemoteEthFxPortTempHighTrap,
       "rcftRemoteEthFxPortTempLowTrap": rcftRemoteEthFxPortTempLowTrap,
       "rcftRemoteEthFxPortVoltageHighTrap": rcftRemoteEthFxPortVoltageHighTrap,
       "rcftRemoteEthFxPortVoltageLowTrap": rcftRemoteEthFxPortVoltageLowTrap,
       "rcftRemoteEthFxPortOffsetCurrHighTrap": rcftRemoteEthFxPortOffsetCurrHighTrap,
       "rcftRemoteEthFxPortOffsetCurrLowTrap": rcftRemoteEthFxPortOffsetCurrLowTrap,
       "rcftRemoteEthFxPortSendPowerHighTrap": rcftRemoteEthFxPortSendPowerHighTrap,
       "rcftRemoteEthFxPortSendPowerLowTrap": rcftRemoteEthFxPortSendPowerLowTrap,
       "rcftRemoteEthFxPortRecvPowerHighTrap": rcftRemoteEthFxPortRecvPowerHighTrap,
       "rcftRemoteEthFxPortRecvPowerLowTrap": rcftRemoteEthFxPortRecvPowerLowTrap,
       "rcftRemoteEthFxPortRemotePowerDownTrap": rcftRemoteEthFxPortRemotePowerDownTrap,
       "rcftRemoteEthFxPortInputSignalLosTrap": rcftRemoteEthFxPortInputSignalLosTrap,
       "rcftRemoteEthFxPortTempHighWarnning": rcftRemoteEthFxPortTempHighWarnning,
       "rcftRemoteEthFxPortTempLowWarning": rcftRemoteEthFxPortTempLowWarning,
       "rcftRemoteEthFxPortVoltageHighWarning": rcftRemoteEthFxPortVoltageHighWarning,
       "rcftRemoteEthFxPortVoltageLowWarning": rcftRemoteEthFxPortVoltageLowWarning,
       "rcftRemoteEthFxPortOffsetCurrHighWarning": rcftRemoteEthFxPortOffsetCurrHighWarning,
       "rcftRemoteEthFxPortOffsetCurrLowWarning": rcftRemoteEthFxPortOffsetCurrLowWarning,
       "rcftRemoteEthFxPortSendPowerHighWarning": rcftRemoteEthFxPortSendPowerHighWarning,
       "rcftRemoteEthFxPortSendPowerLowWarning": rcftRemoteEthFxPortSendPowerLowWarning,
       "rcftRemoteEthFxPortRecvPowerHighWarning": rcftRemoteEthFxPortRecvPowerHighWarning,
       "rcftRemoteEthFxPortRecvPowerLowWarning": rcftRemoteEthFxPortRecvPowerLowWarning,
       "rcftRemoteDeviceEthFxPerformance": rcftRemoteDeviceEthFxPerformance,
       "rcftRemoteEthFxPortCurrentTable": rcftRemoteEthFxPortCurrentTable,
       "rcftRemoteEthFxPortCurrentEntry": rcftRemoteEthFxPortCurrentEntry,
       "rcftRemoteEthFxCurrentTemperature": rcftRemoteEthFxCurrentTemperature,
       "rcftRemoteEthFxCurrentVoltage": rcftRemoteEthFxCurrentVoltage,
       "rcftRemoteEthFxCurrentOffsetCurr": rcftRemoteEthFxCurrentOffsetCurr,
       "rcftRemoteEthFxCurrentRecvPower": rcftRemoteEthFxCurrentRecvPower,
       "rcftRemoteEthFxCurrentSendPower": rcftRemoteEthFxCurrentSendPower,
       "rcftRemoteEthFxPortIntervalTable": rcftRemoteEthFxPortIntervalTable,
       "rcftRemoteEthFxPortIntervalEntry": rcftRemoteEthFxPortIntervalEntry,
       "rcftRemoteEthFxIntervalNumber": rcftRemoteEthFxIntervalNumber,
       "rcftRemoteEthFxIntervalTemperature": rcftRemoteEthFxIntervalTemperature,
       "rcftRemoteEthFxIntervalVoltage": rcftRemoteEthFxIntervalVoltage,
       "rcftRemoteEthFxIntervalOffsetCurr": rcftRemoteEthFxIntervalOffsetCurr,
       "rcftRemoteEthFxIntervalRecvPower": rcftRemoteEthFxIntervalRecvPower,
       "rcftRemoteEthFxIntervalSendPower": rcftRemoteEthFxIntervalSendPower,
       "rcftRemoteEthFxPortPerTable": rcftRemoteEthFxPortPerTable,
       "rcftRemoteEthFxPortPerEntry": rcftRemoteEthFxPortPerEntry,
       "rcftRemoteEthFxPortPerTemperature": rcftRemoteEthFxPortPerTemperature,
       "rcftRemoteEthFxPortPerVoltage": rcftRemoteEthFxPortPerVoltage,
       "rcftRemoteEthFxPortPerOffsetCurr": rcftRemoteEthFxPortPerOffsetCurr,
       "rcftRemoteEthFxPortPerRecvPower": rcftRemoteEthFxPortPerRecvPower,
       "rcftRemoteEthFxPortPerSendPower": rcftRemoteEthFxPortPerSendPower,
       "rcftRemoteDeviceE1MIB": rcftRemoteDeviceE1MIB,
       "rcftRemoteDeviceE1Objects": rcftRemoteDeviceE1Objects,
       "rcftRemoteDeviceE1Table": rcftRemoteDeviceE1Table,
       "rcftRemoteDeviceE1Entry": rcftRemoteDeviceE1Entry,
       "rcftRemoteE1Index": rcftRemoteE1Index,
       "rcftRemoteE1BertEnable": rcftRemoteE1BertEnable,
       "rcftRemoteE1ClockMode": rcftRemoteE1ClockMode,
       "rcftRemoteE1FrameEnable": rcftRemoteE1FrameEnable,
       "rcftRemoteE1AlarmStatus": rcftRemoteE1AlarmStatus,
       "rcftRemoteE1SubSpeed": rcftRemoteE1SubSpeed,
       "rcftRemoteE1CRCDetectEnable": rcftRemoteE1CRCDetectEnable,
       "rcftRemoteE1ErrCodeSecCnt": rcftRemoteE1ErrCodeSecCnt,
       "rcftRemoteE1SErrCodeSecCnt": rcftRemoteE1SErrCodeSecCnt,
       "rcftRemoteE1TransErrorCode": rcftRemoteE1TransErrorCode,
       "rcftRemoteE1CRCStatus": rcftRemoteE1CRCStatus,
       "rcftRemoteE1FaultPass": rcftRemoteE1FaultPass,
       "rcftRemoteE1LocalLoopEn": rcftRemoteE1LocalLoopEn,
       "rcftRemoteE1Location": rcftRemoteE1Location,
       "rcftRemoteE1FoundLink": rcftRemoteE1FoundLink,
       "rcftRemoteE1UnUsed": rcftRemoteE1UnUsed,
       "rcftRemoteToLocalE1AlarmStatus": rcftRemoteToLocalE1AlarmStatus,
       "rcftRemoteE1Balance": rcftRemoteE1Balance,
       "rcftRemoteE1PortStatus": rcftRemoteE1PortStatus,
       "rcftRemoteE1PortTS0Mode": rcftRemoteE1PortTS0Mode,
       "rcftRemoteE1PortIdleCode": rcftRemoteE1PortIdleCode,
       "rcftRemoteE1LoopStatus": rcftRemoteE1LoopStatus,
       "rcftRemoteE1OrderTimeParameter": rcftRemoteE1OrderTimeParameter,
       "rcftRemoteE1OrderModeParameter": rcftRemoteE1OrderModeParameter,
       "rcftRemoteE1Order": rcftRemoteE1Order,
       "rcftRemoteE1PortType": rcftRemoteE1PortType,
       "rcftRemoteE1BertStatus": rcftRemoteE1BertStatus,
       "rcftRemoteE1BertTime": rcftRemoteE1BertTime,
       "rcftRemoteE1BertErrCode": rcftRemoteE1BertErrCode,
       "rcftRemoteE1BertUnusedTime": rcftRemoteE1BertUnusedTime,
       "rcftRemoteE1BertPortSpeed": rcftRemoteE1BertPortSpeed,
       "rcftRemoteE1BertCodeType": rcftRemoteE1BertCodeType,
       "rcftRemoteE1BertCodeNum": rcftRemoteE1BertCodeNum,
       "rcftRemoteE1LoopSwitchStatus": rcftRemoteE1LoopSwitchStatus,
       "rcftRemoteE1AlarmRejest": rcftRemoteE1AlarmRejest,
       "rcftRemoteT1AlarmStatus": rcftRemoteT1AlarmStatus,
       "rcftRemoteE1PortVCGNumber": rcftRemoteE1PortVCGNumber,
       "rcftRemoteE1ToLNumber": rcftRemoteE1ToLNumber,
       "rcftRemoteE1CVCnt": rcftRemoteE1CVCnt,
       "rcftRemoteE1StatisticTable": rcftRemoteE1StatisticTable,
       "rcftRemoteE1StatisticEntry": rcftRemoteE1StatisticEntry,
       "rcftRemoteE1TxPackets": rcftRemoteE1TxPackets,
       "rcftRemoteE1TxBytes": rcftRemoteE1TxBytes,
       "rcftRemoteE1RxPackets": rcftRemoteE1RxPackets,
       "rcftRemoteE1RxBytes": rcftRemoteE1RxBytes,
       "rcftRemoteE1RxERRPackets": rcftRemoteE1RxERRPackets,
       "rcftRemoteE1FluxTimer": rcftRemoteE1FluxTimer,
       "rcftRemoteE1LANTxPackets": rcftRemoteE1LANTxPackets,
       "rcftRemoteE1LANRxPackets": rcftRemoteE1LANRxPackets,
       "rcftRemoteE1LANRxLosPackets": rcftRemoteE1LANRxLosPackets,
       "rcftRemoteDeviceE1Traps": rcftRemoteDeviceE1Traps,
       "rcftRemoteDevE1LOSTRAP": rcftRemoteDevE1LOSTRAP,
       "rcftRemoteDevE1LOFTRAP": rcftRemoteDevE1LOFTRAP,
       "rcftRemoteDevE1CRCTRAP": rcftRemoteDevE1CRCTRAP,
       "rcftRemoteDevE1AISTrap": rcftRemoteDevE1AISTrap,
       "rcftRemoteDevE1TransErrorCodeMore10E-3": rcftRemoteDevE1TransErrorCodeMore10E_3,
       "rcftRemoteDevE1TransErrorCodeMore10E-6": rcftRemoteDevE1TransErrorCodeMore10E_6,
       "rcftRemoteDevToLocalDevE1LOSTRAP": rcftRemoteDevToLocalDevE1LOSTRAP,
       "rcftRemoteDevToLocalDevE1LOFTRAP": rcftRemoteDevToLocalDevE1LOFTRAP,
       "rcftRemoteDevToLocalDevE1CRCTRAP": rcftRemoteDevToLocalDevE1CRCTRAP,
       "rcftRemoteDevToLocalDevE1AISTrap": rcftRemoteDevToLocalDevE1AISTrap,
       "rcftRemoteDevE1CVTrap": rcftRemoteDevE1CVTrap,
       "rcftRemoteDevE1LOMFTrap": rcftRemoteDevE1LOMFTrap,
       "rcftRemoteDevT1LOSTrap": rcftRemoteDevT1LOSTrap,
       "rcftRemoteDevT1AISTrap": rcftRemoteDevT1AISTrap,
       "rcftRemoteDevE1TSDTrap": rcftRemoteDevE1TSDTrap,
       "rcftRemoteE1PortToLTSDTrap": rcftRemoteE1PortToLTSDTrap,
       "rcftRemoteDevE1RDITrap": rcftRemoteDevE1RDITrap,
       "rcftRemoteE1PortToLLOMFTrap": rcftRemoteE1PortToLLOMFTrap,
       "rcftRemoteDeviceSHDSLMIB": rcftRemoteDeviceSHDSLMIB,
       "rcftRemoteSHDSLPortObjects": rcftRemoteSHDSLPortObjects,
       "rcftRemoteSHDSLPortTable": rcftRemoteSHDSLPortTable,
       "rcftRemoteSHDSLPortEntry": rcftRemoteSHDSLPortEntry,
       "rcftRemoteSHDSLPortIndex": rcftRemoteSHDSLPortIndex,
       "rcftRemoteSHDSLPortAlarmStatus": rcftRemoteSHDSLPortAlarmStatus,
       "rcftRemoteSHDSLPortStatus": rcftRemoteSHDSLPortStatus,
       "rcftRemoteSHDSLPortCapableSpeed": rcftRemoteSHDSLPortCapableSpeed,
       "rcftRemoteSHDSLPortWorkSpeed": rcftRemoteSHDSLPortWorkSpeed,
       "rcftRemoteSHDSLPortProbeMaxSpeed": rcftRemoteSHDSLPortProbeMaxSpeed,
       "rcftRemoteSHDSLPortProbeMinSpeed": rcftRemoteSHDSLPortProbeMinSpeed,
       "rcftRemoteSDHSLPortSNR": rcftRemoteSDHSLPortSNR,
       "rcftRemoteSHDSLPortConfigSNR": rcftRemoteSHDSLPortConfigSNR,
       "rcftRemoteSHDSLPortSNRThreshold": rcftRemoteSHDSLPortSNRThreshold,
       "rcftRemoteSHDSLPortAttenuation": rcftRemoteSHDSLPortAttenuation,
       "rcftRemoteSHDSLPortAttenuationThreshold": rcftRemoteSHDSLPortAttenuationThreshold,
       "rcftRemoteSHDSLPortPBO": rcftRemoteSHDSLPortPBO,
       "rcftRemoteSHDSLPortLOSThreshold": rcftRemoteSHDSLPortLOSThreshold,
       "rcftRemoteSHDSLPortLOSWThreshold": rcftRemoteSHDSLPortLOSWThreshold,
       "rcftRemoteSHDSLPortLOLKThreshold": rcftRemoteSHDSLPortLOLKThreshold,
       "rcftRemoteSHDSLPortESThreshold": rcftRemoteSHDSLPortESThreshold,
       "rcftRemoteSHDSLPortLoopStatus": rcftRemoteSHDSLPortLoopStatus,
       "rcftRemoteSHDSLPortAttenuationInitThreshhold": rcftRemoteSHDSLPortAttenuationInitThreshhold,
       "rcftRemoteSHDSLPortOrderTimeParameter": rcftRemoteSHDSLPortOrderTimeParameter,
       "rcftRemoteSHDSLPortOrderModeParameter": rcftRemoteSHDSLPortOrderModeParameter,
       "rcftRemoteSHDSLPortOrder": rcftRemoteSHDSLPortOrder,
       "rcftRemoteSHDSLPortPBOAmount": rcftRemoteSHDSLPortPBOAmount,
       "rcftRemoteSHDSLBertStatus": rcftRemoteSHDSLBertStatus,
       "rcftRemoteSHDSLBertTime": rcftRemoteSHDSLBertTime,
       "rcftRemoteSHDSLBertErrCode": rcftRemoteSHDSLBertErrCode,
       "rcftRemoteSHDSLBertUnusedTime": rcftRemoteSHDSLBertUnusedTime,
       "rcftRemoteSHDSLBertPortSpeed": rcftRemoteSHDSLBertPortSpeed,
       "rcftRemoteSHDSLBertCodeType": rcftRemoteSHDSLBertCodeType,
       "rcftRemoteSHDSLBertCodeNum": rcftRemoteSHDSLBertCodeNum,
       "rcftRemoteSHDSLLoopStatus": rcftRemoteSHDSLLoopStatus,
       "rcftRemoteSHDSLPortPerformance": rcftRemoteSHDSLPortPerformance,
       "rcftRemoteSHDSLPortCurrentTable": rcftRemoteSHDSLPortCurrentTable,
       "rcftRemoteSHDSLPortCurrentEntry": rcftRemoteSHDSLPortCurrentEntry,
       "rcftRemoteSHDSLPortCurrentLOSTimes": rcftRemoteSHDSLPortCurrentLOSTimes,
       "rcftRemoteSHDSLPortCurrentLOSWTimes": rcftRemoteSHDSLPortCurrentLOSWTimes,
       "rcftRemoteSHDSLPortCurrentLOLKTimes": rcftRemoteSHDSLPortCurrentLOLKTimes,
       "rcftRemoteSHDSLPortCurrentCVTimes": rcftRemoteSHDSLPortCurrentCVTimes,
       "rcftRemoteSHDSLPortCurrentES": rcftRemoteSHDSLPortCurrentES,
       "rcftRemoteSHDSLPortCurrentSES": rcftRemoteSHDSLPortCurrentSES,
       "rcftRemoteSHDSLPortCurrentUAS": rcftRemoteSHDSLPortCurrentUAS,
       "rcftRemoteSHDSLPortCurrentLOSWS": rcftRemoteSHDSLPortCurrentLOSWS,
       "rcftRemoteSHDSLPortCurrentCRCTimes": rcftRemoteSHDSLPortCurrentCRCTimes,
       "rcftRemoteSHDSLPortIntervalTable": rcftRemoteSHDSLPortIntervalTable,
       "rcftRemoteSHDSLPortIntervalEntry": rcftRemoteSHDSLPortIntervalEntry,
       "rcftRemoteSHDSLPortIntervalNumber": rcftRemoteSHDSLPortIntervalNumber,
       "rcftRemoteSHDSLPortIntervalLOSTimes": rcftRemoteSHDSLPortIntervalLOSTimes,
       "rcftRemoteSHDSLPortIntervalLOSWTimes": rcftRemoteSHDSLPortIntervalLOSWTimes,
       "rcftRemoteSHDSLPortIntervalLOLKTimes": rcftRemoteSHDSLPortIntervalLOLKTimes,
       "rcftRemoteSHDSLPortIntervalCVTimes": rcftRemoteSHDSLPortIntervalCVTimes,
       "rcftRemoteSHDSLPortIntervalES": rcftRemoteSHDSLPortIntervalES,
       "rcftRemoteSHDSLPortIntervalSES": rcftRemoteSHDSLPortIntervalSES,
       "rcftRemoteSHDSLPortIntervalUAS": rcftRemoteSHDSLPortIntervalUAS,
       "rcftRemoteSHDSLPortIntervalLOSWS": rcftRemoteSHDSLPortIntervalLOSWS,
       "rcftRemoteSHDSLPortIntervalCRCTimes": rcftRemoteSHDSLPortIntervalCRCTimes,
       "rcftRemoteSHDSLPortCurrentDayTable": rcftRemoteSHDSLPortCurrentDayTable,
       "rcftRemoteSHDSLPortCurrentDayEntry": rcftRemoteSHDSLPortCurrentDayEntry,
       "rcftRemoteSHDSLPortCurrentDayLOSTimes": rcftRemoteSHDSLPortCurrentDayLOSTimes,
       "rcftRemoteSHDSLPortCurrentDayLOSWTimes": rcftRemoteSHDSLPortCurrentDayLOSWTimes,
       "rcftRemoteSHDSLPortCurrentDayLOLKTimes": rcftRemoteSHDSLPortCurrentDayLOLKTimes,
       "rcftRemoteSHDSLPortCurrentDayCVTimes": rcftRemoteSHDSLPortCurrentDayCVTimes,
       "rcftRemoteSHDSLPortCurrentDayES": rcftRemoteSHDSLPortCurrentDayES,
       "rcftRemoteSHDSLPortCurrentDaySES": rcftRemoteSHDSLPortCurrentDaySES,
       "rcftRemoteSHDSLPortCurrentDayUAS": rcftRemoteSHDSLPortCurrentDayUAS,
       "rcftRemoteSHDSLPortCurrentDayLOSWS": rcftRemoteSHDSLPortCurrentDayLOSWS,
       "rcftRemoteSHDSLPortCurrentDayCRCTimes": rcftRemoteSHDSLPortCurrentDayCRCTimes,
       "rcftRemoteSHDSLPortIntervalDayTable": rcftRemoteSHDSLPortIntervalDayTable,
       "rcftRemoteSHDSLPortIntervalDayEntry": rcftRemoteSHDSLPortIntervalDayEntry,
       "rcftRemoteSHDSLPortIntervalDayNumber": rcftRemoteSHDSLPortIntervalDayNumber,
       "rcftRemoteSHDSLPortIntervalDayLOSTimes": rcftRemoteSHDSLPortIntervalDayLOSTimes,
       "rcftRemoteSHDSLPortIntervalDayLOSWTimes": rcftRemoteSHDSLPortIntervalDayLOSWTimes,
       "rcftRemoteSHDSLPortIntervalDayLOLKTimes": rcftRemoteSHDSLPortIntervalDayLOLKTimes,
       "rcftRemoteSHDSLPortIntervalDayCVTimes": rcftRemoteSHDSLPortIntervalDayCVTimes,
       "rcftRemoteSHDSLPortIntervalDayES": rcftRemoteSHDSLPortIntervalDayES,
       "rcftRemoteSHDSLPortIntervalDaySES": rcftRemoteSHDSLPortIntervalDaySES,
       "rcftRemoteSHDSLPortIntervalDayUAS": rcftRemoteSHDSLPortIntervalDayUAS,
       "rcftRemoteSHDSLPortIntervalDayLOSWS": rcftRemoteSHDSLPortIntervalDayLOSWS,
       "rcftRemoteSHDSLPortIntervalDayCRCTimes": rcftRemoteSHDSLPortIntervalDayCRCTimes,
       "rcftRemoteSHDSLPortTraps": rcftRemoteSHDSLPortTraps,
       "rcftRemoteSHDSLPortLOSTrap": rcftRemoteSHDSLPortLOSTrap,
       "rcftRemoteSHDSLPortLOSWTrap": rcftRemoteSHDSLPortLOSWTrap,
       "rcftRemoteSHDSLPortLINKTrap": rcftRemoteSHDSLPortLINKTrap,
       "rcftRemoteSHDSLPortFECTrap": rcftRemoteSHDSLPortFECTrap,
       "rcftRemoteSHDSLPortCRCTrap": rcftRemoteSHDSLPortCRCTrap,
       "rcftRemoteSHDSLPortSNRThresholdTrap": rcftRemoteSHDSLPortSNRThresholdTrap,
       "rcftRemoteSHDSLPortAttenuationThresholdTrap": rcftRemoteSHDSLPortAttenuationThresholdTrap,
       "rcftRemoteSHDSLPortLOSThresholdTrap": rcftRemoteSHDSLPortLOSThresholdTrap,
       "rcftRemoteSHDSLPortLOSWThresholdTrap": rcftRemoteSHDSLPortLOSWThresholdTrap,
       "rcftRemoteSHDSLPortLOLKThresholdTrap": rcftRemoteSHDSLPortLOLKThresholdTrap,
       "rcftRemoteSHDSLPortESThresholdTrap": rcftRemoteSHDSLPortESThresholdTrap,
       "rcftRemoteDeviceV35MIB": rcftRemoteDeviceV35MIB,
       "rcftRemoteV35PortObjects": rcftRemoteV35PortObjects,
       "rcftRemoteV35PortTable": rcftRemoteV35PortTable,
       "rcftRemoteV35PortEntry": rcftRemoteV35PortEntry,
       "rcftRemoteV35PortIndex": rcftRemoteV35PortIndex,
       "rcftRemoteV35PortAlarmStatus": rcftRemoteV35PortAlarmStatus,
       "rcftRemoteV35PortStatus": rcftRemoteV35PortStatus,
       "rcftRemoteV35PortSpeed": rcftRemoteV35PortSpeed,
       "rcftRemoteV35PortOrderTimeParameter": rcftRemoteV35PortOrderTimeParameter,
       "rcftRemoteV35PortOrderModeParameter": rcftRemoteV35PortOrderModeParameter,
       "rcftRemoteV35PortOrder": rcftRemoteV35PortOrder,
       "rcftRemoteV35BertStatus": rcftRemoteV35BertStatus,
       "rcftRemoteV35BertTime": rcftRemoteV35BertTime,
       "rcftRemoteV35BertErrCode": rcftRemoteV35BertErrCode,
       "rcftRemoteV35BertUnusedTime": rcftRemoteV35BertUnusedTime,
       "rcftRemoteV35BertPortSpeed": rcftRemoteV35BertPortSpeed,
       "rcftRemoteV35BertCodeType": rcftRemoteV35BertCodeType,
       "rcftRemoteV35BertCodeNum": rcftRemoteV35BertCodeNum,
       "rcftRemoteV35LoopStatus": rcftRemoteV35LoopStatus,
       "rcftRemoteV35PortPerformance": rcftRemoteV35PortPerformance,
       "rcftRemoteV35PortTraps": rcftRemoteV35PortTraps,
       "rcftRemoteV35PortDCDTrap": rcftRemoteV35PortDCDTrap,
       "rcftRemoteV35PortCTSTrap": rcftRemoteV35PortCTSTrap,
       "rcftRemoteV35PortDTRTrap": rcftRemoteV35PortDTRTrap,
       "rcftRemoteV35PortRTSTrap": rcftRemoteV35PortRTSTrap,
       "rcftRemoteV35PortCRCTrap": rcftRemoteV35PortCRCTrap,
       "rcftRemoteV35PortPATTTrap": rcftRemoteV35PortPATTTrap,
       "rcftRemoteV35PortLOFTrap": rcftRemoteV35PortLOFTrap,
       "rcftRemoteV35PortCVTrap": rcftRemoteV35PortCVTrap,
       "rcftRemoteV35PortAISTrap": rcftRemoteV35PortAISTrap,
       "rcftRemoteV35PortToLLOFTrap": rcftRemoteV35PortToLLOFTrap,
       "rcftRemoteV35PortToLCVTrap": rcftRemoteV35PortToLCVTrap,
       "rcftRemoteV35PortToLAISTrap": rcftRemoteV35PortToLAISTrap,
       "rcftRemoteV35PortDSRTrap": rcftRemoteV35PortDSRTrap,
       "rcftRemoteDS3E3PortMIB": rcftRemoteDS3E3PortMIB,
       "rcftRemoteDS3E3PortObjects": rcftRemoteDS3E3PortObjects,
       "rcftRemoteDS3E3PortTable": rcftRemoteDS3E3PortTable,
       "rcftRemoteDS3E3PortEntry": rcftRemoteDS3E3PortEntry,
       "rcftRemoteDS3E3PortIndex": rcftRemoteDS3E3PortIndex,
       "rcftRemoteDS3E3PortAlarmStatus": rcftRemoteDS3E3PortAlarmStatus,
       "rcftRemoteDS3E3PortStatus": rcftRemoteDS3E3PortStatus,
       "rcftRemoteDS3E3PortESCont": rcftRemoteDS3E3PortESCont,
       "rcftRemoteDS3E3PortBertStatus": rcftRemoteDS3E3PortBertStatus,
       "rcftRemoteDS3E3PortFaultFass": rcftRemoteDS3E3PortFaultFass,
       "rcftRemoteDS3E3PortLoopStatus": rcftRemoteDS3E3PortLoopStatus,
       "rcftRemoteDS3E3PortOrder": rcftRemoteDS3E3PortOrder,
       "rcftRemoteDS3E3PortPerformance": rcftRemoteDS3E3PortPerformance,
       "rcftRemoteDS3E3StatisticTable": rcftRemoteDS3E3StatisticTable,
       "rcftRemoteDS3E3StatisticEntry": rcftRemoteDS3E3StatisticEntry,
       "rcftRemoteDS3E3TxPackets": rcftRemoteDS3E3TxPackets,
       "rcftRemoteDS3E3TxBytes": rcftRemoteDS3E3TxBytes,
       "rcftRemoteDS3E3TxFailurePackets": rcftRemoteDS3E3TxFailurePackets,
       "rcftRemoteDS3E3RxPackets": rcftRemoteDS3E3RxPackets,
       "rcftRemoteDS3E3RxBytes": rcftRemoteDS3E3RxBytes,
       "rcftRemoteDS3E3RxErrorPackets": rcftRemoteDS3E3RxErrorPackets,
       "rcftRemoteDS3E3FluxTimer": rcftRemoteDS3E3FluxTimer,
       "rcftRemoteDS3E3PortTraps": rcftRemoteDS3E3PortTraps,
       "rcftRemoteDS3E3PortAISTrap": rcftRemoteDS3E3PortAISTrap,
       "rcftRemoteDS3E3PortLOSTrap": rcftRemoteDS3E3PortLOSTrap,
       "rcftRemoteDS3E3PortLOLTrap": rcftRemoteDS3E3PortLOLTrap,
       "rcftRemoteDS3E3PortDMOTrap": rcftRemoteDS3E3PortDMOTrap,
       "rcftRemoteDS3E3PortCVTrap": rcftRemoteDS3E3PortCVTrap,
       "rcftRemoteDS3E3PortCRCTrap": rcftRemoteDS3E3PortCRCTrap,
       "rcftRemoteDS3E3PortToLAISTrap": rcftRemoteDS3E3PortToLAISTrap,
       "rcftRemoteDS3E3PortToLLOSTrap": rcftRemoteDS3E3PortToLLOSTrap,
       "rcftRemoteDS3E3PortToLLOLTrap": rcftRemoteDS3E3PortToLLOLTrap,
       "rcftRemoteDS3E3PortToLDMOTrap": rcftRemoteDS3E3PortToLDMOTrap,
       "rcftRemoteDS3E3PortToLCVTrap": rcftRemoteDS3E3PortToLCVTrap,
       "rcftRemoteDS3E3PortToLCRCTrap": rcftRemoteDS3E3PortToLCRCTrap,
       "rcftRemoteDS3E3PortLOFTrap": rcftRemoteDS3E3PortLOFTrap,
       "rcftRemoteDS3E3PortToLLOFTrap": rcftRemoteDS3E3PortToLLOFTrap,
       "rcftRemoteDS3E3PortRAITrap": rcftRemoteDS3E3PortRAITrap,
       "rcftRemoteDS3E3PortToLRAITrap": rcftRemoteDS3E3PortToLRAITrap,
       "rcftRemoteDS3E3PortOOFTrap": rcftRemoteDS3E3PortOOFTrap,
       "rcftRemoteDS3E3PortToLOOFTrap": rcftRemoteDS3E3PortToLOOFTrap,
       "rcftRemotePdhPortMIB": rcftRemotePdhPortMIB,
       "rcftRemotePdhPortObjects": rcftRemotePdhPortObjects,
       "rcftRemotePdhPortTable": rcftRemotePdhPortTable,
       "rcftRemotePdhPortEntry": rcftRemotePdhPortEntry,
       "rcftRemotePdhPortIndex": rcftRemotePdhPortIndex,
       "rcftRemotePdhPortModuleType": rcftRemotePdhPortModuleType,
       "rcftRemotePdhPortAlarmStatus": rcftRemotePdhPortAlarmStatus,
       "rcftRemotePdhPortStatus": rcftRemotePdhPortStatus,
       "rcftRemotePdhPortECSCnt": rcftRemotePdhPortECSCnt,
       "rcftRemotePdhPortSECSCnt": rcftRemotePdhPortSECSCnt,
       "rcftRemotePdhPortLoopStatus": rcftRemotePdhPortLoopStatus,
       "rcftRemotePdhPortOrder": rcftRemotePdhPortOrder,
       "rcftRemotePdhPortBertStatus": rcftRemotePdhPortBertStatus,
       "rcftRemotePdhPortBertErrCode": rcftRemotePdhPortBertErrCode,
       "rcftRemotePdhPortPerformance": rcftRemotePdhPortPerformance,
       "rcftRemotePdhPortTraps": rcftRemotePdhPortTraps,
       "rcftRemotePdhPortLOSTrap": rcftRemotePdhPortLOSTrap,
       "rcftRemotePdhPortLOFTrap": rcftRemotePdhPortLOFTrap,
       "rcftRemotePdhPortE3Trap": rcftRemotePdhPortE3Trap,
       "rcftRemotePdhPortE6Trap": rcftRemotePdhPortE6Trap,
       "rcftRemotePdhPortToLLOSTrap": rcftRemotePdhPortToLLOSTrap,
       "rcftRemotePdhPortToLLOFTrap": rcftRemotePdhPortToLLOFTrap,
       "rcftRemotePdhPortToLE3Trap": rcftRemotePdhPortToLE3Trap,
       "rcftRemotePdhPortToLE6rap": rcftRemotePdhPortToLE6rap,
       "rcftRemotePdhPortToRPowerDown": rcftRemotePdhPortToRPowerDown,
       "rcftRemoteDS1PortMIB": rcftRemoteDS1PortMIB,
       "rcftRemoteDS1PortObjects": rcftRemoteDS1PortObjects,
       "rcftRemoteDS1PortTable": rcftRemoteDS1PortTable,
       "rcftRemoteDS1PortEntry": rcftRemoteDS1PortEntry,
       "rcftRemoteDS1PortIndex": rcftRemoteDS1PortIndex,
       "rcftRemoteDS1PortAlarmStatus": rcftRemoteDS1PortAlarmStatus,
       "rcftRemoteDS1PortStatus": rcftRemoteDS1PortStatus,
       "rcftRemoteDS1PortESCont": rcftRemoteDS1PortESCont,
       "rcftRemoteDS1PortSESCont": rcftRemoteDS1PortSESCont,
       "rcftRemoteDS1PortBertStatus": rcftRemoteDS1PortBertStatus,
       "rcftRemoteDS1PortFaultPass": rcftRemoteDS1PortFaultPass,
       "rcftRemoteDS1PortLoopStatus": rcftRemoteDS1PortLoopStatus,
       "rcftRemoteDS1PortOrder": rcftRemoteDS1PortOrder,
       "rcftRemoteDS1PortTranLength": rcftRemoteDS1PortTranLength,
       "rcftRemoteDS1PortFaultPassIndicator": rcftRemoteDS1PortFaultPassIndicator,
       "rcftRemoteDS1PortframeType": rcftRemoteDS1PortframeType,
       "rcftRemoteDS1PortChannel": rcftRemoteDS1PortChannel,
       "rcftRemoteDS1PortPerformance": rcftRemoteDS1PortPerformance,
       "rcftRemoteDS1StatisticTable": rcftRemoteDS1StatisticTable,
       "rcftRemoteDS1StatisticEntry": rcftRemoteDS1StatisticEntry,
       "rcftRemoteDS1TxPackets": rcftRemoteDS1TxPackets,
       "rcftRemoteDS1TxBytes": rcftRemoteDS1TxBytes,
       "rcftRemoteDS1TxFailurePackets": rcftRemoteDS1TxFailurePackets,
       "rcftRemoteDS1RxPackets": rcftRemoteDS1RxPackets,
       "rcftRemoteDS1RxBytes": rcftRemoteDS1RxBytes,
       "rcftRemoteDS1RxErrorPackets": rcftRemoteDS1RxErrorPackets,
       "rcftRemoteDS1FluxTimer": rcftRemoteDS1FluxTimer,
       "rcftRemoteDS1PortTraps": rcftRemoteDS1PortTraps,
       "rcftRemoteDS1PortAISTrap": rcftRemoteDS1PortAISTrap,
       "rcftRemoteDS1PortLOSTrap": rcftRemoteDS1PortLOSTrap,
       "rcftRemoteDS1PortToLAISTrap": rcftRemoteDS1PortToLAISTrap,
       "rcftRemoteDS1PortToLLOSTrap": rcftRemoteDS1PortToLLOSTrap,
       "rcftRemoteDS1PortLOFTrap": rcftRemoteDS1PortLOFTrap,
       "rcftRemoteDS1PortCRCTrap": rcftRemoteDS1PortCRCTrap,
       "rcftRemoteDS1PortToLLOFTrap": rcftRemoteDS1PortToLLOFTrap,
       "rcftRemoteDS1PortToLCRCTrap": rcftRemoteDS1PortToLCRCTrap,
       "rcftRemoteDS1PortFaultPassIndicatorTrap": rcftRemoteDS1PortFaultPassIndicatorTrap,
       "rcftRemoteDS1PortDMOTrap": rcftRemoteDS1PortDMOTrap,
       "rcftRemoteDS1PortCVTrap": rcftRemoteDS1PortCVTrap,
       "rcftRemoteDS1PortYELTrap": rcftRemoteDS1PortYELTrap,
       "rcftRemoteDS1PortREDTrap": rcftRemoteDS1PortREDTrap,
       "rcftRemoteMoudleMIB": rcftRemoteMoudleMIB,
       "rcftRemoteMoudle": rcftRemoteMoudle,
       "rcftRemoteMoudleObjects": rcftRemoteMoudleObjects,
       "rcftRemoteMoudleTable": rcftRemoteMoudleTable,
       "rcftRemoteMoudleEntry": rcftRemoteMoudleEntry,
       "rcftRemoteMoudleIndex": rcftRemoteMoudleIndex,
       "rcftRemoteMoudleExist": rcftRemoteMoudleExist,
       "rcftRemoteMoudleType": rcftRemoteMoudleType,
       "rcftRemoteMoudleStatus": rcftRemoteMoudleStatus,
       "rcftRemoteMoudleSigleChipDescr": rcftRemoteMoudleSigleChipDescr,
       "rcftRemoteMoudleHardWareDescr": rcftRemoteMoudleHardWareDescr,
       "rcftRemoteMoudleFPGADescr": rcftRemoteMoudleFPGADescr,
       "rcftRemoteMoudleOrder": rcftRemoteMoudleOrder,
       "rcftRemoteMoudleIFOrder": rcftRemoteMoudleIFOrder,
       "rcftRemoteMoudleTraps": rcftRemoteMoudleTraps,
       "rcftRemoteMoudleExistTrap": rcftRemoteMoudleExistTrap,
       "rcftRemoteMoudleEthFe": rcftRemoteMoudleEthFe,
       "rcftRemoteMoudleEthFeObjects": rcftRemoteMoudleEthFeObjects,
       "rcftRemoteMoudleEthFeTable": rcftRemoteMoudleEthFeTable,
       "rcftRemoteMoudleEthFeEntry": rcftRemoteMoudleEthFeEntry,
       "rcftRemoteMoudleEthFeIndex": rcftRemoteMoudleEthFeIndex,
       "rcftRemoteMoudleEthFeStatus": rcftRemoteMoudleEthFeStatus,
       "rcftRemoteMoudleEthFeRxRestrictSpeed": rcftRemoteMoudleEthFeRxRestrictSpeed,
       "rcftRemoteMoudleEthFeTxRestrictSpeed": rcftRemoteMoudleEthFeTxRestrictSpeed,
       "rcftRemoteMoudleEthFeRestrictSpeedStep": rcftRemoteMoudleEthFeRestrictSpeedStep,
       "rcftRemoteMoudleEthFeAlarmStatus": rcftRemoteMoudleEthFeAlarmStatus,
       "rcftRemoteMoudleEthFePerformance": rcftRemoteMoudleEthFePerformance,
       "rcftRemoteMoudleEthFeStatisticTable": rcftRemoteMoudleEthFeStatisticTable,
       "rcftRemoteMoudleEthFeStatisticEntry": rcftRemoteMoudleEthFeStatisticEntry,
       "rcftRemoteMoudleEthFeTxPackets": rcftRemoteMoudleEthFeTxPackets,
       "rcftRemoteMoudleEthFeTxBytes": rcftRemoteMoudleEthFeTxBytes,
       "rcftRemoteMoudleEthFeTxFailurePackets": rcftRemoteMoudleEthFeTxFailurePackets,
       "rcftRemoteMoudleEthFeRxPackets": rcftRemoteMoudleEthFeRxPackets,
       "rcftRemoteMoudleEthFeRxBytes": rcftRemoteMoudleEthFeRxBytes,
       "rcftRemoteMoudleEthFeRxErrorPackets": rcftRemoteMoudleEthFeRxErrorPackets,
       "rcftRemoteMoudleEthFeFluxTimer": rcftRemoteMoudleEthFeFluxTimer,
       "rcftRemoteMoudleEthFeTraps": rcftRemoteMoudleEthFeTraps,
       "rcftRemoteMoudleEthFeLinkTrap": rcftRemoteMoudleEthFeLinkTrap,
       "rcftRemoteMoudlePdh": rcftRemoteMoudlePdh,
       "rcftRemoteMoudlePdhObjects": rcftRemoteMoudlePdhObjects,
       "rcftRemoteMoudlePdhTable": rcftRemoteMoudlePdhTable,
       "rcftRemoteMoudlePdhEntry": rcftRemoteMoudlePdhEntry,
       "rcftRemoteMoudlePdhIndex": rcftRemoteMoudlePdhIndex,
       "rcftRemoteMoudlePdhAlarmStatus": rcftRemoteMoudlePdhAlarmStatus,
       "rcftRemoteMoudlePdhStatus": rcftRemoteMoudlePdhStatus,
       "rcftRemoteMoudlePdhTraps": rcftRemoteMoudlePdhTraps,
       "rcftRemoteMoudlePdhLOSTrap": rcftRemoteMoudlePdhLOSTrap,
       "rcftRemoteMoudlePdhLOFTrap": rcftRemoteMoudlePdhLOFTrap,
       "rcftRemoteMoudleE1": rcftRemoteMoudleE1,
       "rcftRemoteMoudleE1Objects": rcftRemoteMoudleE1Objects,
       "rcftRemoteMoudleE1Table": rcftRemoteMoudleE1Table,
       "rcftRemoteMoudleE1Entry": rcftRemoteMoudleE1Entry,
       "rcftRemoteMoudleE1Index": rcftRemoteMoudleE1Index,
       "rcftRemoteMoudleE1AlarmStatus": rcftRemoteMoudleE1AlarmStatus,
       "rcftRemoteMoudleE1Status": rcftRemoteMoudleE1Status,
       "rcftRemoteMoudleE1TimeSlots": rcftRemoteMoudleE1TimeSlots,
       "rcftRemoteMoudleE1TS0Mode": rcftRemoteMoudleE1TS0Mode,
       "rcftRemoteMoudleE1LoopStatus": rcftRemoteMoudleE1LoopStatus,
       "rcftRemoteMoudleE1ESCnt": rcftRemoteMoudleE1ESCnt,
       "rcftRemoteMoudleE1SESCnt": rcftRemoteMoudleE1SESCnt,
       "rcftRemoteMoudleE1Performance": rcftRemoteMoudleE1Performance,
       "rcftRemoteMoudleE1StatisticTable": rcftRemoteMoudleE1StatisticTable,
       "rcftRemoteMoudleE1StatisticEntry": rcftRemoteMoudleE1StatisticEntry,
       "rcftRemoteMoudleE1TxPackets": rcftRemoteMoudleE1TxPackets,
       "rcftRemoteMoudleE1TxBytes": rcftRemoteMoudleE1TxBytes,
       "rcftRemoteMoudleE1TxFailurePackets": rcftRemoteMoudleE1TxFailurePackets,
       "rcftRemoteMoudleE1RxPackets": rcftRemoteMoudleE1RxPackets,
       "rcftRemoteMoudleE1RxBytes": rcftRemoteMoudleE1RxBytes,
       "rcftRemoteMoudleE1RxErrorPackets": rcftRemoteMoudleE1RxErrorPackets,
       "rcftRemoteMoudleE1FluxTimer": rcftRemoteMoudleE1FluxTimer,
       "rcftRemoteMoudleE1Traps": rcftRemoteMoudleE1Traps,
       "rcftRemoteMoudleE1LOSTrap": rcftRemoteMoudleE1LOSTrap,
       "rcftRemoteMoudleE1AISTrap": rcftRemoteMoudleE1AISTrap,
       "rcftRemoteMoudleE1CRCTrap": rcftRemoteMoudleE1CRCTrap,
       "rcftRemoteMoudleE1CVTrap": rcftRemoteMoudleE1CVTrap,
       "rcftRemoteMoudleE1LOFTrap": rcftRemoteMoudleE1LOFTrap,
       "rcftRemoteMoudleE1ErrorCodeTrap": rcftRemoteMoudleE1ErrorCodeTrap,
       "rcftRemoteMoudleV35": rcftRemoteMoudleV35,
       "rcftRemoteMoudleV35Objects": rcftRemoteMoudleV35Objects,
       "rcftRemoteMoudleV35Table": rcftRemoteMoudleV35Table,
       "rcftRemoteMoudleV35Entry": rcftRemoteMoudleV35Entry,
       "rcftRemoteMoudleV35Index": rcftRemoteMoudleV35Index,
       "rcftRemoteMoudleV35AlarmStatus": rcftRemoteMoudleV35AlarmStatus,
       "rcftRemoteMoudleV35Status": rcftRemoteMoudleV35Status,
       "rcftRemoteMoudleV35Traps": rcftRemoteMoudleV35Traps,
       "rcftRemoteAudioPortMIB": rcftRemoteAudioPortMIB,
       "rcftRemoteAudioPortObjects": rcftRemoteAudioPortObjects,
       "rcftRemoteAudioPortTable": rcftRemoteAudioPortTable,
       "rcftRemoteAudioPortEntry": rcftRemoteAudioPortEntry,
       "rcftRemoteAudioPortIndex": rcftRemoteAudioPortIndex,
       "rcftRemoteAudioPortStatus": rcftRemoteAudioPortStatus,
       "rcftRemoteAudioPortPosition": rcftRemoteAudioPortPosition,
       "rcftRemoteAudioPortType": rcftRemoteAudioPortType,
       "rcftRemoteAudioPortPerformance": rcftRemoteAudioPortPerformance,
       "rcftRemoteAudioPortTraps": rcftRemoteAudioPortTraps,
       "rcftRemoteVideoPortMIB": rcftRemoteVideoPortMIB,
       "rcftRemoteVideoPortObjects": rcftRemoteVideoPortObjects,
       "rcftRemoteVideoPortTable": rcftRemoteVideoPortTable,
       "rcftRemoteVideoPortEntry": rcftRemoteVideoPortEntry,
       "rcftRemoteVideoPortIndex": rcftRemoteVideoPortIndex,
       "rcftRemoteVideoPortStatus": rcftRemoteVideoPortStatus,
       "rcftRemoteVideoPortPosition": rcftRemoteVideoPortPosition,
       "rcftRemoteVideoPortSourceID": rcftRemoteVideoPortSourceID,
       "rcftRemoteVideoPortPerformance": rcftRemoteVideoPortPerformance,
       "rcftRemoteVideoPortTraps": rcftRemoteVideoPortTraps,
       "rcftRemoteVideoPortSignalLos": rcftRemoteVideoPortSignalLos,
       "rcftRemoteVideoPortSignalInLos": rcftRemoteVideoPortSignalInLos,
       "rcftRemoteVideoPortSignalOutLos": rcftRemoteVideoPortSignalOutLos,
       "rcftRemoteDataPortMIB": rcftRemoteDataPortMIB,
       "rcftRemoteDataPortObjects": rcftRemoteDataPortObjects,
       "rcftRemoteDataPortTable": rcftRemoteDataPortTable,
       "rcftRemoteDataPortEntry": rcftRemoteDataPortEntry,
       "rcftRemoteDataPortIndex": rcftRemoteDataPortIndex,
       "rcftRemoteDataPortStatus": rcftRemoteDataPortStatus,
       "rcftRemoteDataPortPosition": rcftRemoteDataPortPosition,
       "rcftRemoteDataPortType": rcftRemoteDataPortType,
       "rcftRemoteDataPortPerformance": rcftRemoteDataPortPerformance,
       "rcftRemoteDataPortTraps": rcftRemoteDataPortTraps,
       "rcftRemoteSimpleModuleMIB": rcftRemoteSimpleModuleMIB,
       "rcftRemoteSimpleModuleObjects": rcftRemoteSimpleModuleObjects,
       "rcftRemoteSimpleModuleTable": rcftRemoteSimpleModuleTable,
       "rcftRemoteSimpleModuleEntry": rcftRemoteSimpleModuleEntry,
       "rcftRemoteSimpleModuleIndex": rcftRemoteSimpleModuleIndex,
       "rcftRemoteSimpleModuleExist": rcftRemoteSimpleModuleExist,
       "rcftRemoteSimpleModulePosition": rcftRemoteSimpleModulePosition,
       "rcftRemoteSimpleModuleStatus": rcftRemoteSimpleModuleStatus,
       "rcftRemoteSimpleModuleType": rcftRemoteSimpleModuleType,
       "rcftRemoteSimpleModulePerformance": rcftRemoteSimpleModulePerformance,
       "rcftRemoteSimpleModuleTraps": rcftRemoteSimpleModuleTraps,
       "rcftRemoteVLANMIB": rcftRemoteVLANMIB,
       "rcftRemoteVLANObjects": rcftRemoteVLANObjects,
       "rcftRemoteVLANTable": rcftRemoteVLANTable,
       "rcftRemoteVLANEntry": rcftRemoteVLANEntry,
       "rcftRemoteVLANIndex": rcftRemoteVLANIndex,
       "rcftRemoteVLANStatus": rcftRemoteVLANStatus,
       "rcftRemoteVLANmember": rcftRemoteVLANmember,
       "rcftRemoteVID": rcftRemoteVID,
       "rcftRemotePerformaceMib": rcftRemotePerformaceMib,
       "rcftRemoteStatisticPerformance": rcftRemoteStatisticPerformance,
       "rcftRemoteStatisticTable": rcftRemoteStatisticTable,
       "rcftRemoteStatisticEntry": rcftRemoteStatisticEntry,
       "rcftRemotePortIndex": rcftRemotePortIndex,
       "rcftRemotePortType": rcftRemotePortType,
       "rcftRemoteRxPackets": rcftRemoteRxPackets,
       "rcftRemoteRxLosPackets": rcftRemoteRxLosPackets,
       "rcftRemoteRxPreabErrPackets": rcftRemoteRxPreabErrPackets,
       "rcftRemoteRxFCSErrPackets": rcftRemoteRxFCSErrPackets,
       "rcftRemoteRxUnderSizePackets": rcftRemoteRxUnderSizePackets,
       "rcftRemoteRxOverSizePackets": rcftRemoteRxOverSizePackets,
       "rcftRemoteRxPausePackets": rcftRemoteRxPausePackets,
       "rcftRemoteRxOamPackets": rcftRemoteRxOamPackets,
       "rcftRemoteRxBytes": rcftRemoteRxBytes,
       "rcftRemoteTxPackets": rcftRemoteTxPackets,
       "rcftRemoteTxFCSErrPackets": rcftRemoteTxFCSErrPackets,
       "rcftRemoteTxPausePackets": rcftRemoteTxPausePackets,
       "rcftRemoteTxOamPackets": rcftRemoteTxOamPackets,
       "rcftRemoteTxBytes": rcftRemoteTxBytes,
       "rcftRemoteFluxTimer": rcftRemoteFluxTimer,
       "rcftRemoteVCGMib": rcftRemoteVCGMib,
       "rcftRemoteVCGObjects": rcftRemoteVCGObjects,
       "rcftRemoteVCGTable": rcftRemoteVCGTable,
       "rcftRemoteVCGEntry": rcftRemoteVCGEntry,
       "rcftRemoteVCGIndex": rcftRemoteVCGIndex,
       "rcftRemoteVCGStatus": rcftRemoteVCGStatus,
       "rcftRemoteVCGLoopStatus": rcftRemoteVCGLoopStatus,
       "rcftRemoteVCGLcasXPR": rcftRemoteVCGLcasXPR,
       "rcftRemoteVCGLcasXAR": rcftRemoteVCGLcasXAR,
       "rcftRemoteVCGLcasXPT": rcftRemoteVCGLcasXPT,
       "rcftRemoteVCGLcasXAT": rcftRemoteVCGLcasXAT,
       "rcftRemoteVCGAlarmStatus": rcftRemoteVCGAlarmStatus,
       "rcftRemoteVCGRxISPTPID": rcftRemoteVCGRxISPTPID,
       "rcftRemoteVCGTxISPTPID": rcftRemoteVCGTxISPTPID,
       "rcftRemoteVCGBaseCoS": rcftRemoteVCGBaseCoS,
       "rcftRemoteVCGVLANID": rcftRemoteVCGVLANID,
       "rcftRemoteVCGMemberList": rcftRemoteVCGMemberList,
       "rcftRemoteVCGMemberStatus": rcftRemoteVCGMemberStatus,
       "rcftRemoteVCGMemberRxCode": rcftRemoteVCGMemberRxCode,
       "rcftRemoteVCGMemberTxCode": rcftRemoteVCGMemberTxCode,
       "rcftRemoteVCGMemberAlarmStatus": rcftRemoteVCGMemberAlarmStatus,
       "rcftRemoteToLVCGMemberAlarmStatus": rcftRemoteToLVCGMemberAlarmStatus,
       "rcftRemoteVCGPerformance": rcftRemoteVCGPerformance,
       "rcftRemoteVCGStatisticTable": rcftRemoteVCGStatisticTable,
       "rcftRemoteVCGStatisticEntry": rcftRemoteVCGStatisticEntry,
       "rcftRemoteVCGRxClientPackets": rcftRemoteVCGRxClientPackets,
       "rcftRemoteVCGRxIdlePackets": rcftRemoteVCGRxIdlePackets,
       "rcftRemoteVCGRxMgmntPackets": rcftRemoteVCGRxMgmntPackets,
       "rcftRemoteVCGRxFCSErrMgmntPackets": rcftRemoteVCGRxFCSErrMgmntPackets,
       "rcftRemoteVCGRxLenErrPackets": rcftRemoteVCGRxLenErrPackets,
       "rcftRemoteVCGRxFCSErrClientPackets": rcftRemoteVCGRxFCSErrClientPackets,
       "rcftRemoteVCGRxThecErrPackets": rcftRemoteVCGRxThecErrPackets,
       "rcftRemoteVCGRxEhecErrPackets": rcftRemoteVCGRxEhecErrPackets,
       "rcftRemoteVCGRxCIDErrPackets": rcftRemoteVCGRxCIDErrPackets,
       "rcftRemoteVCGRxSpareErrPackets": rcftRemoteVCGRxSpareErrPackets,
       "rcftRemoteVCGRxChecCorPackets": rcftRemoteVCGRxChecCorPackets,
       "rcftRemoteVCGRxThecCorPackets": rcftRemoteVCGRxThecCorPackets,
       "rcftRemoteVCGRxEhecCorPackets": rcftRemoteVCGRxEhecCorPackets,
       "rcftRemoteVCGRxBytes": rcftRemoteVCGRxBytes,
       "rcftRemoteVCGTxClientPackets": rcftRemoteVCGTxClientPackets,
       "rcftRemoteVCGTxIdlePackets": rcftRemoteVCGTxIdlePackets,
       "rcftRemoteVCGTxMgmntPackets": rcftRemoteVCGTxMgmntPackets,
       "rcftRemoteVCGTxBytes": rcftRemoteVCGTxBytes,
       "rcftRemoteVCGFluxTimer": rcftRemoteVCGFluxTimer,
       "rcftRemoteVCGTraps": rcftRemoteVCGTraps,
       "rcftRemoteVCGGIDTraps": rcftRemoteVCGGIDTraps,
       "rcftRemoteVCGLOATraps": rcftRemoteVCGLOATraps,
       "rcftRemoteVCGLFDTraps": rcftRemoteVCGLFDTraps,
       "rcftRemoteVCGCSFTraps": rcftRemoteVCGCSFTraps,
       "rcftRemoteVCGTLCTTraps": rcftRemoteVCGTLCTTraps,
       "rcftRemoteVCGTLCRTraps": rcftRemoteVCGTLCRTraps,
       "rcftRemoteVCGToLGIDTraps": rcftRemoteVCGToLGIDTraps,
       "rcftRemoteVCGToLLOATraps": rcftRemoteVCGToLLOATraps,
       "rcftRemoteVCGToLLFDTraps": rcftRemoteVCGToLLFDTraps,
       "rcftRemoteVCGMemberLOMTraps": rcftRemoteVCGMemberLOMTraps,
       "rcftRemoteVCGMemberSQMTraps": rcftRemoteVCGMemberSQMTraps,
       "rcftRemoteVCGMemberCRCTraps": rcftRemoteVCGMemberCRCTraps,
       "rcftRemoteVCGMemberLOATraps": rcftRemoteVCGMemberLOATraps,
       "rcftRemoteVCGToLMemberLOMTraps": rcftRemoteVCGToLMemberLOMTraps,
       "rcftRemoteVCGToLMemberSQMTraps": rcftRemoteVCGToLMemberSQMTraps,
       "rcftRemoteVCGToLMemberCRCTraps": rcftRemoteVCGToLMemberCRCTraps,
       "rcftRemoteVCGToLMemberLOATraps": rcftRemoteVCGToLMemberLOATraps}
)
