# SNMP MIB module (QTECH-3G-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-3G-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:42 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

qtech3GMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95)
)
if mibBuilder.loadTexts:
    qtech3GMonitor.setRevisions(
        ("2011-02-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Qtech3GObjects_ObjectIdentity = ObjectIdentity
qtech3GObjects = _Qtech3GObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1)
)
_Qtech3GTable_Object = MibTable
qtech3GTable = _Qtech3GTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1)
)
if mibBuilder.loadTexts:
    qtech3GTable.setStatus("current")
_Qtech3GEntry_Object = MibTableRow
qtech3GEntry = _Qtech3GEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1)
)
qtech3GEntry.setIndexNames(
    (0, "QTECH-3G-MIB", "qtech3GIPAddr"),
)
if mibBuilder.loadTexts:
    qtech3GEntry.setStatus("current")
_Qtech3gUsername_Type = DisplayString
_Qtech3gUsername_Object = MibTableColumn
qtech3gUsername = _Qtech3gUsername_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 1),
    _Qtech3gUsername_Type()
)
qtech3gUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3gUsername.setStatus("current")


class _Qtech3GOnlineStatus_Type(Integer32):
    """Custom type qtech3GOnlineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("lpm", 0),
          ("online", 1),
          ("offline", 4),
          ("ftm", 5),
          ("reset", 6),
          ("rfOff", 7))
    )


_Qtech3GOnlineStatus_Type.__name__ = "Integer32"
_Qtech3GOnlineStatus_Object = MibTableColumn
qtech3GOnlineStatus = _Qtech3GOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 2),
    _Qtech3GOnlineStatus_Type()
)
qtech3GOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GOnlineStatus.setStatus("current")
_Qtech3GIMEI_Type = DisplayString
_Qtech3GIMEI_Object = MibTableColumn
qtech3GIMEI = _Qtech3GIMEI_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 3),
    _Qtech3GIMEI_Type()
)
qtech3GIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GIMEI.setStatus("current")


class _Qtech3GIPAddrType_Type(Integer32):
    """Custom type qtech3GIPAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4Addr", 1),
          ("ipv6Addr", 2))
    )


_Qtech3GIPAddrType_Type.__name__ = "Integer32"
_Qtech3GIPAddrType_Object = MibTableColumn
qtech3GIPAddrType = _Qtech3GIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 4),
    _Qtech3GIPAddrType_Type()
)
qtech3GIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GIPAddrType.setStatus("current")
_Qtech3GIPAddr_Type = IpAddress
_Qtech3GIPAddr_Object = MibTableColumn
qtech3GIPAddr = _Qtech3GIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 5),
    _Qtech3GIPAddr_Type()
)
qtech3GIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GIPAddr.setStatus("current")
_Qtech3GUplineTime_Type = TimeStamp
_Qtech3GUplineTime_Object = MibTableColumn
qtech3GUplineTime = _Qtech3GUplineTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 6),
    _Qtech3GUplineTime_Type()
)
qtech3GUplineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GUplineTime.setStatus("current")


class _Qtech3GActiveTime_Type(Integer32):
    """Custom type qtech3GActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Qtech3GActiveTime_Type.__name__ = "Integer32"
_Qtech3GActiveTime_Object = MibTableColumn
qtech3GActiveTime = _Qtech3GActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 7),
    _Qtech3GActiveTime_Type()
)
qtech3GActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GActiveTime.setStatus("current")


class _Qtech3GSignalStrength_Type(Integer32):
    """Custom type qtech3GSignalStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Qtech3GSignalStrength_Type.__name__ = "Integer32"
_Qtech3GSignalStrength_Object = MibTableColumn
qtech3GSignalStrength = _Qtech3GSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 8),
    _Qtech3GSignalStrength_Type()
)
qtech3GSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GSignalStrength.setStatus("current")


class _Qtech3GISP_Type(Integer32):
    """Custom type qtech3GISP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chinaUnicom", 1),
          ("chinaTelecom", 2),
          ("chinaMobile", 3))
    )


_Qtech3GISP_Type.__name__ = "Integer32"
_Qtech3GISP_Object = MibTableColumn
qtech3GISP = _Qtech3GISP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 9),
    _Qtech3GISP_Type()
)
qtech3GISP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GISP.setStatus("current")


class _Qtech3GSysMode_Type(Integer32):
    """Custom type qtech3GSysMode based on Integer32"""
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
              15,
              100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("noService", 0),
          ("amps", 1),
          ("cdma", 2),
          ("gsmGprs", 3),
          ("hdr", 4),
          ("wcdma", 5),
          ("gps", 6),
          ("gsmCdma", 7),
          ("cdmaHdrHybrid", 8),
          ("tdscdma", 15),
          ("td-1te", 100),
          ("fdd-lte", 101))
    )


_Qtech3GSysMode_Type.__name__ = "Integer32"
_Qtech3GSysMode_Object = MibTableColumn
qtech3GSysMode = _Qtech3GSysMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 10),
    _Qtech3GSysMode_Type()
)
qtech3GSysMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GSysMode.setStatus("current")


class _Qtech3GServiceStatus_Type(Integer32):
    """Custom type qtech3GServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noService", 0),
          ("restricted", 1),
          ("valid", 2),
          ("restrictedRegional", 3),
          ("powerSavingAndDeepSleepState", 4))
    )


_Qtech3GServiceStatus_Type.__name__ = "Integer32"
_Qtech3GServiceStatus_Object = MibTableColumn
qtech3GServiceStatus = _Qtech3GServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 11),
    _Qtech3GServiceStatus_Type()
)
qtech3GServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GServiceStatus.setStatus("current")


class _Qtech3GRoamingStatus_Type(Integer32):
    """Custom type qtech3GRoamingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noRoaming", 0),
          ("roaming", 1))
    )


_Qtech3GRoamingStatus_Type.__name__ = "Integer32"
_Qtech3GRoamingStatus_Object = MibTableColumn
qtech3GRoamingStatus = _Qtech3GRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 12),
    _Qtech3GRoamingStatus_Type()
)
qtech3GRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GRoamingStatus.setStatus("current")


class _Qtech3GDomain_Type(Integer32):
    """Custom type qtech3GDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              100,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noService", 0),
          ("onlyCS", 1),
          ("onlyPS", 2),
          ("pSCS", 3),
          ("pSCSnotRegistered", 4),
          ("ePSService", 100),
          ("cdmaNotSupport", 255))
    )


_Qtech3GDomain_Type.__name__ = "Integer32"
_Qtech3GDomain_Object = MibTableColumn
qtech3GDomain = _Qtech3GDomain_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 13),
    _Qtech3GDomain_Type()
)
qtech3GDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GDomain.setStatus("current")


class _Qtech3GSIMStatus_Type(Integer32):
    """Custom type qtech3GSIMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("invalidUsimCard", 0),
          ("validUsimCard", 1),
          ("invalidForCS", 2),
          ("invalidForPS", 3),
          ("invalidForCSPS", 4),
          ("noUsimCard", 255))
    )


_Qtech3GSIMStatus_Type.__name__ = "Integer32"
_Qtech3GSIMStatus_Object = MibTableColumn
qtech3GSIMStatus = _Qtech3GSIMStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 14),
    _Qtech3GSIMStatus_Type()
)
qtech3GSIMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GSIMStatus.setStatus("current")


class _Qtech3GSignalStrengthPercent_Type(Integer32):
    """Custom type qtech3GSignalStrengthPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Qtech3GSignalStrengthPercent_Type.__name__ = "Integer32"
_Qtech3GSignalStrengthPercent_Object = MibTableColumn
qtech3GSignalStrengthPercent = _Qtech3GSignalStrengthPercent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 15),
    _Qtech3GSignalStrengthPercent_Type()
)
qtech3GSignalStrengthPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GSignalStrengthPercent.setStatus("current")
_Qtech3GApn_Type = DisplayString
_Qtech3GApn_Object = MibTableColumn
qtech3GApn = _Qtech3GApn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 16),
    _Qtech3GApn_Type()
)
qtech3GApn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GApn.setStatus("current")


class _Qtech3GCellID_Type(Integer32):
    """Custom type qtech3GCellID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Qtech3GCellID_Type.__name__ = "Integer32"
_Qtech3GCellID_Object = MibTableColumn
qtech3GCellID = _Qtech3GCellID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 17),
    _Qtech3GCellID_Type()
)
qtech3GCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GCellID.setStatus("current")


class _Qtech3GLAC_Type(Integer32):
    """Custom type qtech3GLAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Qtech3GLAC_Type.__name__ = "Integer32"
_Qtech3GLAC_Object = MibTableColumn
qtech3GLAC = _Qtech3GLAC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 18),
    _Qtech3GLAC_Type()
)
qtech3GLAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GLAC.setStatus("current")


class _Qtech3GBSID_Type(Integer32):
    """Custom type qtech3GBSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Qtech3GBSID_Type.__name__ = "Integer32"
_Qtech3GBSID_Object = MibTableColumn
qtech3GBSID = _Qtech3GBSID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 19),
    _Qtech3GBSID_Type()
)
qtech3GBSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GBSID.setStatus("current")


class _Qtech3GNID_Type(Integer32):
    """Custom type qtech3GNID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Qtech3GNID_Type.__name__ = "Integer32"
_Qtech3GNID_Object = MibTableColumn
qtech3GNID = _Qtech3GNID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 20),
    _Qtech3GNID_Type()
)
qtech3GNID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GNID.setStatus("current")


class _Qtech3GSID_Type(Integer32):
    """Custom type qtech3GSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Qtech3GSID_Type.__name__ = "Integer32"
_Qtech3GSID_Object = MibTableColumn
qtech3GSID = _Qtech3GSID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 21),
    _Qtech3GSID_Type()
)
qtech3GSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GSID.setStatus("current")
_Qtech3GIMSI_Type = DisplayString
_Qtech3GIMSI_Object = MibTableColumn
qtech3GIMSI = _Qtech3GIMSI_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 22),
    _Qtech3GIMSI_Type()
)
qtech3GIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GIMSI.setStatus("current")
_Qtech3GESN_Type = DisplayString
_Qtech3GESN_Object = MibTableColumn
qtech3GESN = _Qtech3GESN_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 23),
    _Qtech3GESN_Type()
)
qtech3GESN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GESN.setStatus("current")
_Qtech3GPhoneNumber_Type = DisplayString
_Qtech3GPhoneNumber_Object = MibTableColumn
qtech3GPhoneNumber = _Qtech3GPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 24),
    _Qtech3GPhoneNumber_Type()
)
qtech3GPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GPhoneNumber.setStatus("current")
_Qtech3GifIndex_Type = Integer32
_Qtech3GifIndex_Object = MibTableColumn
qtech3GifIndex = _Qtech3GifIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 25),
    _Qtech3GifIndex_Type()
)
qtech3GifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GifIndex.setStatus("current")
_Qtech3GBSLONG_Type = Integer32
_Qtech3GBSLONG_Object = MibTableColumn
qtech3GBSLONG = _Qtech3GBSLONG_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 26),
    _Qtech3GBSLONG_Type()
)
qtech3GBSLONG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GBSLONG.setStatus("current")
_Qtech3GBSLAT_Type = Integer32
_Qtech3GBSLAT_Object = MibTableColumn
qtech3GBSLAT = _Qtech3GBSLAT_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 27),
    _Qtech3GBSLAT_Type()
)
qtech3GBSLAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GBSLAT.setStatus("current")


class _Qtech3GBackupInfo_Type(Integer32):
    """Custom type qtech3GBackupInfo based on Integer32"""
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
        *(("no-backup", 0),
          ("myself", 1),
          ("master", 2),
          ("slave", 3))
    )


_Qtech3GBackupInfo_Type.__name__ = "Integer32"
_Qtech3GBackupInfo_Object = MibTableColumn
qtech3GBackupInfo = _Qtech3GBackupInfo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 28),
    _Qtech3GBackupInfo_Type()
)
qtech3GBackupInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GBackupInfo.setStatus("current")
_Qtech3GSerialNumber_Type = DisplayString
_Qtech3GSerialNumber_Object = MibTableColumn
qtech3GSerialNumber = _Qtech3GSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 29),
    _Qtech3GSerialNumber_Type()
)
qtech3GSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GSerialNumber.setStatus("current")
_Qtech3GBackupIMSI_Type = DisplayString
_Qtech3GBackupIMSI_Object = MibTableColumn
qtech3GBackupIMSI = _Qtech3GBackupIMSI_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 30),
    _Qtech3GBackupIMSI_Type()
)
qtech3GBackupIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GBackupIMSI.setStatus("current")
_Qtech3GGatewayIPAddr_Type = IpAddress
_Qtech3GGatewayIPAddr_Object = MibTableColumn
qtech3GGatewayIPAddr = _Qtech3GGatewayIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 31),
    _Qtech3GGatewayIPAddr_Type()
)
qtech3GGatewayIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GGatewayIPAddr.setStatus("current")
_Qtech3GLineDownCause_Type = Integer32
_Qtech3GLineDownCause_Object = MibTableColumn
qtech3GLineDownCause = _Qtech3GLineDownCause_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 32),
    _Qtech3GLineDownCause_Type()
)
qtech3GLineDownCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GLineDownCause.setStatus("current")


class _Qtech3GModemType_Type(Integer32):
    """Custom type qtech3GModemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modem-type-3G", 1),
          ("modem-type-4G", 2))
    )


_Qtech3GModemType_Type.__name__ = "Integer32"
_Qtech3GModemType_Object = MibTableColumn
qtech3GModemType = _Qtech3GModemType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 1, 1, 33),
    _Qtech3GModemType_Type()
)
qtech3GModemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GModemType.setStatus("current")
_Qtech3GStatTable_Object = MibTable
qtech3GStatTable = _Qtech3GStatTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 2)
)
if mibBuilder.loadTexts:
    qtech3GStatTable.setStatus("current")
_Qtech3GStatEntry_Object = MibTableRow
qtech3GStatEntry = _Qtech3GStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 2, 1)
)
qtech3GStatEntry.setIndexNames(
    (0, "QTECH-3G-MIB", "qtech3GIPAddr"),
)
if mibBuilder.loadTexts:
    qtech3GStatEntry.setStatus("current")
_Qtech3GInOctets_Type = Counter64
_Qtech3GInOctets_Object = MibTableColumn
qtech3GInOctets = _Qtech3GInOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 2, 1, 1),
    _Qtech3GInOctets_Type()
)
qtech3GInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GInOctets.setStatus("current")
_Qtech3GOutOctets_Type = Counter64
_Qtech3GOutOctets_Object = MibTableColumn
qtech3GOutOctets = _Qtech3GOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 2, 1, 2),
    _Qtech3GOutOctets_Type()
)
qtech3GOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GOutOctets.setStatus("current")
_Qtech3GInSpeed_Type = Counter64
_Qtech3GInSpeed_Object = MibTableColumn
qtech3GInSpeed = _Qtech3GInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 2, 1, 3),
    _Qtech3GInSpeed_Type()
)
qtech3GInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GInSpeed.setStatus("current")
_Qtech3GOutSpeed_Type = Counter64
_Qtech3GOutSpeed_Object = MibTableColumn
qtech3GOutSpeed = _Qtech3GOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 2, 1, 4),
    _Qtech3GOutSpeed_Type()
)
qtech3GOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GOutSpeed.setStatus("current")
_Qtech3G2IMSI_Type = DisplayString
_Qtech3G2IMSI_Object = MibTableColumn
qtech3G2IMSI = _Qtech3G2IMSI_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 2, 1, 5),
    _Qtech3G2IMSI_Type()
)
qtech3G2IMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3G2IMSI.setStatus("current")
_Qtech3G2ifIndex_Type = Integer32
_Qtech3G2ifIndex_Object = MibTableColumn
qtech3G2ifIndex = _Qtech3G2ifIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 2, 1, 6),
    _Qtech3G2ifIndex_Type()
)
qtech3G2ifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3G2ifIndex.setStatus("current")
_Qtech3GTrap_ObjectIdentity = ObjectIdentity
qtech3GTrap = _Qtech3GTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 3)
)
_Qtech3GNotifications_ObjectIdentity = ObjectIdentity
qtech3GNotifications = _Qtech3GNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 3, 1)
)
_Qtech3GBsNumber_Type = Integer32
_Qtech3GBsNumber_Object = MibScalar
qtech3GBsNumber = _Qtech3GBsNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 4),
    _Qtech3GBsNumber_Type()
)
qtech3GBsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GBsNumber.setStatus("current")
_Qtech3GBsTable_Object = MibTable
qtech3GBsTable = _Qtech3GBsTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 5)
)
if mibBuilder.loadTexts:
    qtech3GBsTable.setStatus("current")
_Qtech3GBsEntry_Object = MibTableRow
qtech3GBsEntry = _Qtech3GBsEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 5, 1)
)
qtech3GBsEntry.setIndexNames(
    (0, "QTECH-3G-MIB", "qtech3GBsSN"),
)
if mibBuilder.loadTexts:
    qtech3GBsEntry.setStatus("current")
_Qtech3GBsSN_Type = Integer32
_Qtech3GBsSN_Object = MibTableColumn
qtech3GBsSN = _Qtech3GBsSN_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 5, 1, 1),
    _Qtech3GBsSN_Type()
)
qtech3GBsSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GBsSN.setStatus("current")


class _Qtech3GBsISP_Type(Integer32):
    """Custom type qtech3GBsISP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chinaUnicom", 1),
          ("chinaTelecom", 2),
          ("chinaMobile", 3))
    )


_Qtech3GBsISP_Type.__name__ = "Integer32"
_Qtech3GBsISP_Object = MibTableColumn
qtech3GBsISP = _Qtech3GBsISP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 5, 1, 2),
    _Qtech3GBsISP_Type()
)
qtech3GBsISP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GBsISP.setStatus("current")


class _Qtech3GBsMode_Type(Integer32):
    """Custom type qtech3GBsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sys2GMode", 1),
          ("sys3GMode", 2))
    )


_Qtech3GBsMode_Type.__name__ = "Integer32"
_Qtech3GBsMode_Object = MibTableColumn
qtech3GBsMode = _Qtech3GBsMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 5, 1, 3),
    _Qtech3GBsMode_Type()
)
qtech3GBsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GBsMode.setStatus("current")
_Qtech3GBsIMSI_Type = DisplayString
_Qtech3GBsIMSI_Object = MibTableColumn
qtech3GBsIMSI = _Qtech3GBsIMSI_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 5, 1, 4),
    _Qtech3GBsIMSI_Type()
)
qtech3GBsIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GBsIMSI.setStatus("current")
_Qtech3GBsLAC_Type = Integer32
_Qtech3GBsLAC_Object = MibTableColumn
qtech3GBsLAC = _Qtech3GBsLAC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 5, 1, 5),
    _Qtech3GBsLAC_Type()
)
qtech3GBsLAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GBsLAC.setStatus("current")
_Qtech3GBsCellID_Type = Integer32
_Qtech3GBsCellID_Object = MibTableColumn
qtech3GBsCellID = _Qtech3GBsCellID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 5, 1, 6),
    _Qtech3GBsCellID_Type()
)
qtech3GBsCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GBsCellID.setStatus("current")
_Qtech3GBsBSID_Type = Integer32
_Qtech3GBsBSID_Object = MibTableColumn
qtech3GBsBSID = _Qtech3GBsBSID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 5, 1, 7),
    _Qtech3GBsBSID_Type()
)
qtech3GBsBSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GBsBSID.setStatus("current")
_Qtech3GBsSID_Type = Integer32
_Qtech3GBsSID_Object = MibTableColumn
qtech3GBsSID = _Qtech3GBsSID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 5, 1, 8),
    _Qtech3GBsSID_Type()
)
qtech3GBsSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GBsSID.setStatus("current")
_Qtech3GBsNID_Type = Integer32
_Qtech3GBsNID_Object = MibTableColumn
qtech3GBsNID = _Qtech3GBsNID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 5, 1, 9),
    _Qtech3GBsNID_Type()
)
qtech3GBsNID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GBsNID.setStatus("current")
_Qtech3GBsRssi_Type = Integer32
_Qtech3GBsRssi_Object = MibTableColumn
qtech3GBsRssi = _Qtech3GBsRssi_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 5, 1, 10),
    _Qtech3GBsRssi_Type()
)
qtech3GBsRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GBsRssi.setStatus("current")
_Qtech3GBsBSLONG_Type = Integer32
_Qtech3GBsBSLONG_Object = MibTableColumn
qtech3GBsBSLONG = _Qtech3GBsBSLONG_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 5, 1, 11),
    _Qtech3GBsBSLONG_Type()
)
qtech3GBsBSLONG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GBsBSLONG.setStatus("current")
_Qtech3GBsBSLAT_Type = Integer32
_Qtech3GBsBSLAT_Object = MibTableColumn
qtech3GBsBSLAT = _Qtech3GBsBSLAT_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 5, 1, 12),
    _Qtech3GBsBSLAT_Type()
)
qtech3GBsBSLAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GBsBSLAT.setStatus("current")
_Qtech3GDeviceManagementTable_Object = MibTable
qtech3GDeviceManagementTable = _Qtech3GDeviceManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6)
)
if mibBuilder.loadTexts:
    qtech3GDeviceManagementTable.setStatus("current")
_Qtech3GDeviceManagementEntry_Object = MibTableRow
qtech3GDeviceManagementEntry = _Qtech3GDeviceManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1)
)
qtech3GDeviceManagementEntry.setIndexNames(
    (0, "QTECH-3G-MIB", "qtech3GRouterSlotNumber"),
)
if mibBuilder.loadTexts:
    qtech3GDeviceManagementEntry.setStatus("current")
_Qtech3GRouterType_Type = DisplayString
_Qtech3GRouterType_Object = MibTableColumn
qtech3GRouterType = _Qtech3GRouterType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 1),
    _Qtech3GRouterType_Type()
)
qtech3GRouterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GRouterType.setStatus("current")
_Qtech3GRouterSN_Type = DisplayString
_Qtech3GRouterSN_Object = MibTableColumn
qtech3GRouterSN = _Qtech3GRouterSN_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 2),
    _Qtech3GRouterSN_Type()
)
qtech3GRouterSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GRouterSN.setStatus("current")
_Qtech3GRouterSlotNumber_Type = DisplayString
_Qtech3GRouterSlotNumber_Object = MibTableColumn
qtech3GRouterSlotNumber = _Qtech3GRouterSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 3),
    _Qtech3GRouterSlotNumber_Type()
)
qtech3GRouterSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GRouterSlotNumber.setStatus("current")
_Qtech3GLineCardType_Type = DisplayString
_Qtech3GLineCardType_Object = MibTableColumn
qtech3GLineCardType = _Qtech3GLineCardType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 4),
    _Qtech3GLineCardType_Type()
)
qtech3GLineCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GLineCardType.setStatus("current")
_Qtech3GCardIMSI_Type = DisplayString
_Qtech3GCardIMSI_Object = MibTableColumn
qtech3GCardIMSI = _Qtech3GCardIMSI_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 5),
    _Qtech3GCardIMSI_Type()
)
qtech3GCardIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GCardIMSI.setStatus("current")
_Qtech3GModemIMEI_Type = DisplayString
_Qtech3GModemIMEI_Object = MibTableColumn
qtech3GModemIMEI = _Qtech3GModemIMEI_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 6),
    _Qtech3GModemIMEI_Type()
)
qtech3GModemIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GModemIMEI.setStatus("current")
_Qtech3GIntfIPAddr_Type = IpAddress
_Qtech3GIntfIPAddr_Object = MibTableColumn
qtech3GIntfIPAddr = _Qtech3GIntfIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 7),
    _Qtech3GIntfIPAddr_Type()
)
qtech3GIntfIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GIntfIPAddr.setStatus("current")
_Qtech3GCardPhoneNumber_Type = DisplayString
_Qtech3GCardPhoneNumber_Object = MibTableColumn
qtech3GCardPhoneNumber = _Qtech3GCardPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 8),
    _Qtech3GCardPhoneNumber_Type()
)
qtech3GCardPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GCardPhoneNumber.setStatus("current")
_Qtech3GLineDetected_Type = Unsigned32
_Qtech3GLineDetected_Object = MibTableColumn
qtech3GLineDetected = _Qtech3GLineDetected_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 9),
    _Qtech3GLineDetected_Type()
)
qtech3GLineDetected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtech3GLineDetected.setStatus("current")


class _Qtech3GLineDetectedResult_Type(Integer32):
    """Custom type qtech3GLineDetectedResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noRsponse", 0),
          ("pass", 1),
          ("failed", 2),
          ("using", 3),
          ("detecting", 4))
    )


_Qtech3GLineDetectedResult_Type.__name__ = "Integer32"
_Qtech3GLineDetectedResult_Object = MibTableColumn
qtech3GLineDetectedResult = _Qtech3GLineDetectedResult_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 10),
    _Qtech3GLineDetectedResult_Type()
)
qtech3GLineDetectedResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GLineDetectedResult.setStatus("current")


class _Qtech3GLineDetectedMainCause_Type(Integer32):
    """Custom type qtech3GLineDetectedMainCause based on Integer32"""
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
        *(("noGivenReason", 0),
          ("dialFailed", 1),
          ("pppFailed", 2),
          ("ipsecSetupFailed", 3))
    )


_Qtech3GLineDetectedMainCause_Type.__name__ = "Integer32"
_Qtech3GLineDetectedMainCause_Object = MibTableColumn
qtech3GLineDetectedMainCause = _Qtech3GLineDetectedMainCause_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 11),
    _Qtech3GLineDetectedMainCause_Type()
)
qtech3GLineDetectedMainCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GLineDetectedMainCause.setStatus("current")


class _Qtech3GLineDetectedSubCause_Type(Integer32):
    """Custom type qtech3GLineDetectedSubCause based on Integer32"""
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
        *(("noGivenReason", 0),
          ("simCardInvalid", 1),
          ("aPNInvalid", 2),
          ("powerlower", 3),
          ("userInfoError", 4),
          ("ipsecSetupFailed", 5))
    )


_Qtech3GLineDetectedSubCause_Type.__name__ = "Integer32"
_Qtech3GLineDetectedSubCause_Object = MibTableColumn
qtech3GLineDetectedSubCause = _Qtech3GLineDetectedSubCause_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 12),
    _Qtech3GLineDetectedSubCause_Type()
)
qtech3GLineDetectedSubCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GLineDetectedSubCause.setStatus("current")


class _Qtech3GDeviceBackupInfo_Type(Integer32):
    """Custom type qtech3GDeviceBackupInfo based on Integer32"""
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
        *(("no-backup", 0),
          ("myself", 1),
          ("master", 2),
          ("slave", 3))
    )


_Qtech3GDeviceBackupInfo_Type.__name__ = "Integer32"
_Qtech3GDeviceBackupInfo_Object = MibTableColumn
qtech3GDeviceBackupInfo = _Qtech3GDeviceBackupInfo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 13),
    _Qtech3GDeviceBackupInfo_Type()
)
qtech3GDeviceBackupInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GDeviceBackupInfo.setStatus("current")


class _Qtech3GRssiStrength_Type(Integer32):
    """Custom type qtech3GRssiStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Qtech3GRssiStrength_Type.__name__ = "Integer32"
_Qtech3GRssiStrength_Object = MibTableColumn
qtech3GRssiStrength = _Qtech3GRssiStrength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 14),
    _Qtech3GRssiStrength_Type()
)
qtech3GRssiStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GRssiStrength.setStatus("current")


class _Qtech3GRssiStrengthPercent_Type(Integer32):
    """Custom type qtech3GRssiStrengthPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Qtech3GRssiStrengthPercent_Type.__name__ = "Integer32"
_Qtech3GRssiStrengthPercent_Object = MibTableColumn
qtech3GRssiStrengthPercent = _Qtech3GRssiStrengthPercent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 15),
    _Qtech3GRssiStrengthPercent_Type()
)
qtech3GRssiStrengthPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GRssiStrengthPercent.setStatus("current")


class _Qtech3GNetworkISPMode_Type(Integer32):
    """Custom type qtech3GNetworkISPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chinaUnicom", 1),
          ("chinaTelecom", 2),
          ("chinaMobile", 3))
    )


_Qtech3GNetworkISPMode_Type.__name__ = "Integer32"
_Qtech3GNetworkISPMode_Object = MibTableColumn
qtech3GNetworkISPMode = _Qtech3GNetworkISPMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 16),
    _Qtech3GNetworkISPMode_Type()
)
qtech3GNetworkISPMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GNetworkISPMode.setStatus("current")


class _Qtech3GNetworkSysMode_Type(Integer32):
    """Custom type qtech3GNetworkSysMode based on Integer32"""
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
              15,
              100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("noService", 0),
          ("amps", 1),
          ("cdma", 2),
          ("gsmGprs", 3),
          ("hdr", 4),
          ("wcdma", 5),
          ("gps", 6),
          ("gsmCdma", 7),
          ("cdmaHdrHybrid", 8),
          ("td-scdma", 15),
          ("td-1te", 100),
          ("fdd-lte", 101))
    )


_Qtech3GNetworkSysMode_Type.__name__ = "Integer32"
_Qtech3GNetworkSysMode_Object = MibTableColumn
qtech3GNetworkSysMode = _Qtech3GNetworkSysMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 17),
    _Qtech3GNetworkSysMode_Type()
)
qtech3GNetworkSysMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtech3GNetworkSysMode.setStatus("current")


class _Qtech3GNetworkServiceStatus_Type(Integer32):
    """Custom type qtech3GNetworkServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noService", 0),
          ("restricted", 1),
          ("valid", 2),
          ("restrictedRegional", 3),
          ("powerSavingAndDeepSleepState", 4))
    )


_Qtech3GNetworkServiceStatus_Type.__name__ = "Integer32"
_Qtech3GNetworkServiceStatus_Object = MibTableColumn
qtech3GNetworkServiceStatus = _Qtech3GNetworkServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 18),
    _Qtech3GNetworkServiceStatus_Type()
)
qtech3GNetworkServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GNetworkServiceStatus.setStatus("current")


class _Qtech3GSIMCardStatus_Type(Integer32):
    """Custom type qtech3GSIMCardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("invalidUsimCard", 0),
          ("validUsimCard", 1),
          ("invalidForCS", 2),
          ("invalidForPS", 3),
          ("invalidForCSPS", 4),
          ("noUsimCard", 255))
    )


_Qtech3GSIMCardStatus_Type.__name__ = "Integer32"
_Qtech3GSIMCardStatus_Object = MibTableColumn
qtech3GSIMCardStatus = _Qtech3GSIMCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 19),
    _Qtech3GSIMCardStatus_Type()
)
qtech3GSIMCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GSIMCardStatus.setStatus("current")


class _Qtech3GDailMode_Type(Integer32):
    """Custom type qtech3GDailMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dialOnDemand", 0),
          ("autoDail", 1))
    )


_Qtech3GDailMode_Type.__name__ = "Integer32"
_Qtech3GDailMode_Object = MibTableColumn
qtech3GDailMode = _Qtech3GDailMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 20),
    _Qtech3GDailMode_Type()
)
qtech3GDailMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtech3GDailMode.setStatus("current")
_Qtech3GDeviceBackupIMSI_Type = DisplayString
_Qtech3GDeviceBackupIMSI_Object = MibTableColumn
qtech3GDeviceBackupIMSI = _Qtech3GDeviceBackupIMSI_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 21),
    _Qtech3GDeviceBackupIMSI_Type()
)
qtech3GDeviceBackupIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GDeviceBackupIMSI.setStatus("current")


class _Qtech3GLineDetectedMode_Type(Integer32):
    """Custom type qtech3GLineDetectedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vpdnMode", 0),
          ("ipsecMode", 1))
    )


_Qtech3GLineDetectedMode_Type.__name__ = "Integer32"
_Qtech3GLineDetectedMode_Object = MibTableColumn
qtech3GLineDetectedMode = _Qtech3GLineDetectedMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 22),
    _Qtech3GLineDetectedMode_Type()
)
qtech3GLineDetectedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtech3GLineDetectedMode.setStatus("current")
_Qtech3GPppUsername_Type = DisplayString
_Qtech3GPppUsername_Object = MibTableColumn
qtech3GPppUsername = _Qtech3GPppUsername_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 23),
    _Qtech3GPppUsername_Type()
)
qtech3GPppUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtech3GPppUsername.setStatus("current")
_Qtech3GUserApn_Type = DisplayString
_Qtech3GUserApn_Object = MibTableColumn
qtech3GUserApn = _Qtech3GUserApn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 24),
    _Qtech3GUserApn_Type()
)
qtech3GUserApn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtech3GUserApn.setStatus("current")


class _Qtech3GModemOnlineStatus_Type(Integer32):
    """Custom type qtech3GModemOnlineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("minimum-function", 0),
          ("fully-function", 1),
          ("offline-mode", 2),
          ("sim-activate", 3),
          ("sim-deactivate", 4))
    )


_Qtech3GModemOnlineStatus_Type.__name__ = "Integer32"
_Qtech3GModemOnlineStatus_Object = MibTableColumn
qtech3GModemOnlineStatus = _Qtech3GModemOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 25),
    _Qtech3GModemOnlineStatus_Type()
)
qtech3GModemOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GModemOnlineStatus.setStatus("current")


class _Qtech3GIntfIPAddrType_Type(Integer32):
    """Custom type qtech3GIntfIPAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4Addr", 1),
          ("ipv6Addr", 2))
    )


_Qtech3GIntfIPAddrType_Type.__name__ = "Integer32"
_Qtech3GIntfIPAddrType_Object = MibTableColumn
qtech3GIntfIPAddrType = _Qtech3GIntfIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 26),
    _Qtech3GIntfIPAddrType_Type()
)
qtech3GIntfIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GIntfIPAddrType.setStatus("current")
_Qtech3GUserUplineTime_Type = TimeStamp
_Qtech3GUserUplineTime_Object = MibTableColumn
qtech3GUserUplineTime = _Qtech3GUserUplineTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 27),
    _Qtech3GUserUplineTime_Type()
)
qtech3GUserUplineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GUserUplineTime.setStatus("current")


class _Qtech3GUserActiveTime_Type(Integer32):
    """Custom type qtech3GUserActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Qtech3GUserActiveTime_Type.__name__ = "Integer32"
_Qtech3GUserActiveTime_Object = MibTableColumn
qtech3GUserActiveTime = _Qtech3GUserActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 28),
    _Qtech3GUserActiveTime_Type()
)
qtech3GUserActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GUserActiveTime.setStatus("current")


class _Qtech3GSIMRoamingStatus_Type(Integer32):
    """Custom type qtech3GSIMRoamingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noRoaming", 0),
          ("roaming", 1))
    )


_Qtech3GSIMRoamingStatus_Type.__name__ = "Integer32"
_Qtech3GSIMRoamingStatus_Object = MibTableColumn
qtech3GSIMRoamingStatus = _Qtech3GSIMRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 29),
    _Qtech3GSIMRoamingStatus_Type()
)
qtech3GSIMRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GSIMRoamingStatus.setStatus("current")


class _Qtech3GAcessBSCellID_Type(Integer32):
    """Custom type qtech3GAcessBSCellID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Qtech3GAcessBSCellID_Type.__name__ = "Integer32"
_Qtech3GAcessBSCellID_Object = MibTableColumn
qtech3GAcessBSCellID = _Qtech3GAcessBSCellID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 30),
    _Qtech3GAcessBSCellID_Type()
)
qtech3GAcessBSCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GAcessBSCellID.setStatus("current")


class _Qtech3GAcessBSLAC_Type(Integer32):
    """Custom type qtech3GAcessBSLAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Qtech3GAcessBSLAC_Type.__name__ = "Integer32"
_Qtech3GAcessBSLAC_Object = MibTableColumn
qtech3GAcessBSLAC = _Qtech3GAcessBSLAC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 31),
    _Qtech3GAcessBSLAC_Type()
)
qtech3GAcessBSLAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GAcessBSLAC.setStatus("current")
_Qtech3GAcessBSLONG_Type = Integer32
_Qtech3GAcessBSLONG_Object = MibTableColumn
qtech3GAcessBSLONG = _Qtech3GAcessBSLONG_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 32),
    _Qtech3GAcessBSLONG_Type()
)
qtech3GAcessBSLONG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GAcessBSLONG.setStatus("current")
_Qtech3GAcessBSLAT_Type = Integer32
_Qtech3GAcessBSLAT_Object = MibTableColumn
qtech3GAcessBSLAT = _Qtech3GAcessBSLAT_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 33),
    _Qtech3GAcessBSLAT_Type()
)
qtech3GAcessBSLAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GAcessBSLAT.setStatus("current")
_Qtech3GDialOnDemandIfIndex_Type = Integer32
_Qtech3GDialOnDemandIfIndex_Object = MibTableColumn
qtech3GDialOnDemandIfIndex = _Qtech3GDialOnDemandIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 34),
    _Qtech3GDialOnDemandIfIndex_Type()
)
qtech3GDialOnDemandIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GDialOnDemandIfIndex.setStatus("current")


class _Qtech3GTrafficPreventMode_Type(Integer32):
    """Custom type qtech3GTrafficPreventMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Qtech3GTrafficPreventMode_Type.__name__ = "Integer32"
_Qtech3GTrafficPreventMode_Object = MibTableColumn
qtech3GTrafficPreventMode = _Qtech3GTrafficPreventMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 35),
    _Qtech3GTrafficPreventMode_Type()
)
qtech3GTrafficPreventMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GTrafficPreventMode.setStatus("current")
_Qtech3GTrafficPreventIfIndex_Type = Integer32
_Qtech3GTrafficPreventIfIndex_Object = MibTableColumn
qtech3GTrafficPreventIfIndex = _Qtech3GTrafficPreventIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 36),
    _Qtech3GTrafficPreventIfIndex_Type()
)
qtech3GTrafficPreventIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GTrafficPreventIfIndex.setStatus("current")
_Qtech3GTrafficPreventListID_Type = Integer32
_Qtech3GTrafficPreventListID_Object = MibTableColumn
qtech3GTrafficPreventListID = _Qtech3GTrafficPreventListID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 37),
    _Qtech3GTrafficPreventListID_Type()
)
qtech3GTrafficPreventListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GTrafficPreventListID.setStatus("current")
_Qtech3GTrafficPreventListName_Type = DisplayString
_Qtech3GTrafficPreventListName_Object = MibTableColumn
qtech3GTrafficPreventListName = _Qtech3GTrafficPreventListName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 38),
    _Qtech3GTrafficPreventListName_Type()
)
qtech3GTrafficPreventListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GTrafficPreventListName.setStatus("current")


class _Qtech3GDeviceModemType_Type(Integer32):
    """Custom type qtech3GDeviceModemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modem-type-3G", 1),
          ("modem-type-4G", 2))
    )


_Qtech3GDeviceModemType_Type.__name__ = "Integer32"
_Qtech3GDeviceModemType_Object = MibTableColumn
qtech3GDeviceModemType = _Qtech3GDeviceModemType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 39),
    _Qtech3GDeviceModemType_Type()
)
qtech3GDeviceModemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech3GDeviceModemType.setStatus("current")


class _Qtech3GTrafficTrapInterval_Type(Integer32):
    """Custom type qtech3GTrafficTrapInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_Qtech3GTrafficTrapInterval_Type.__name__ = "Integer32"
_Qtech3GTrafficTrapInterval_Object = MibTableColumn
qtech3GTrafficTrapInterval = _Qtech3GTrafficTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 40),
    _Qtech3GTrafficTrapInterval_Type()
)
qtech3GTrafficTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtech3GTrafficTrapInterval.setStatus("current")


class _Qtech3GRssiThreshold_Type(Integer32):
    """Custom type qtech3GRssiThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Qtech3GRssiThreshold_Type.__name__ = "Integer32"
_Qtech3GRssiThreshold_Object = MibTableColumn
qtech3GRssiThreshold = _Qtech3GRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 41),
    _Qtech3GRssiThreshold_Type()
)
qtech3GRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtech3GRssiThreshold.setStatus("current")


class _Qtech3GTrapFilterMode_Type(Integer32):
    """Custom type qtech3GTrapFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Qtech3GTrapFilterMode_Type.__name__ = "Integer32"
_Qtech3GTrapFilterMode_Object = MibTableColumn
qtech3GTrapFilterMode = _Qtech3GTrapFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 42),
    _Qtech3GTrapFilterMode_Type()
)
qtech3GTrapFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtech3GTrapFilterMode.setStatus("current")


class _Qtech3GISPtimeout_Type(Integer32):
    """Custom type qtech3GISPtimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 36000),
    )


_Qtech3GISPtimeout_Type.__name__ = "Integer32"
_Qtech3GISPtimeout_Object = MibTableColumn
qtech3GISPtimeout = _Qtech3GISPtimeout_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 43),
    _Qtech3GISPtimeout_Type()
)
qtech3GISPtimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtech3GISPtimeout.setStatus("current")


class _Qtech3GEncrypt_type_Type(Integer32):
    """Custom type qtech3GEncrypt_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ENCRYPT_NONE", 0),
          ("ENCRYPT_TEMP", 7))
    )


_Qtech3GEncrypt_type_Type.__name__ = "Integer32"
_Qtech3GEncrypt_type_Object = MibTableColumn
qtech3GEncrypt_type = _Qtech3GEncrypt_type_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 44),
    _Qtech3GEncrypt_type_Type()
)
qtech3GEncrypt_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtech3GEncrypt_type.setStatus("current")
_Qtech3GPassword_Type = DisplayString
_Qtech3GPassword_Object = MibTableColumn
qtech3GPassword = _Qtech3GPassword_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 6, 1, 45),
    _Qtech3GPassword_Type()
)
qtech3GPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtech3GPassword.setStatus("current")
_Qtech3GTrapNew_ObjectIdentity = ObjectIdentity
qtech3GTrapNew = _Qtech3GTrapNew_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 2)
)
_Qtech3GNotificationsNew_ObjectIdentity = ObjectIdentity
qtech3GNotificationsNew = _Qtech3GNotificationsNew_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 2, 1)
)

# Managed Objects groups


# Notification objects

qtech3GSignalThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 3, 1, 1)
)
qtech3GSignalThreshold.setObjects(
      *(("QTECH-3G-MIB", "qtech3GIPAddr"),
        ("QTECH-3G-MIB", "qtech3GSignalStrength"),
        ("QTECH-3G-MIB", "qtech3GSignalStrengthPercent"),
        ("QTECH-3G-MIB", "qtech3GIMSI"))
)
if mibBuilder.loadTexts:
    qtech3GSignalThreshold.setStatus(
        "current"
    )

qtech3GUpLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 3, 1, 2)
)
qtech3GUpLine.setObjects(
      *(("QTECH-3G-MIB", "qtech3GIPAddr"),
        ("QTECH-3G-MIB", "qtech3gUsername"),
        ("QTECH-3G-MIB", "qtech3GIMSI"),
        ("QTECH-3G-MIB", "qtech3GBackupInfo"),
        ("QTECH-3G-MIB", "qtech3GSerialNumber"),
        ("QTECH-3G-MIB", "qtech3GGatewayIPAddr"))
)
if mibBuilder.loadTexts:
    qtech3GUpLine.setStatus(
        "current"
    )

qtech3GDownLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 3, 1, 3)
)
qtech3GDownLine.setObjects(
      *(("QTECH-3G-MIB", "qtech3GLineDownCause"),
        ("QTECH-3G-MIB", "qtech3GIPAddr"),
        ("QTECH-3G-MIB", "qtech3gUsername"),
        ("QTECH-3G-MIB", "qtech3GIMSI"))
)
if mibBuilder.loadTexts:
    qtech3GDownLine.setStatus(
        "current"
    )

qtech3GChangeAccessPoint = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 3, 1, 4)
)
qtech3GChangeAccessPoint.setObjects(
      *(("QTECH-3G-MIB", "qtech3GIPAddr"),
        ("QTECH-3G-MIB", "qtech3GApn"),
        ("QTECH-3G-MIB", "qtech3gUsername"),
        ("QTECH-3G-MIB", "qtech3GIMSI"))
)
if mibBuilder.loadTexts:
    qtech3GChangeAccessPoint.setStatus(
        "current"
    )

qtech3GBackupIntfSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 3, 1, 5)
)
qtech3GBackupIntfSwitch.setObjects(
      *(("QTECH-3G-MIB", "qtech3GIPAddr"),
        ("QTECH-3G-MIB", "qtech3gUsername"),
        ("QTECH-3G-MIB", "qtech3GIMSI"),
        ("QTECH-3G-MIB", "qtech3GSerialNumber"),
        ("QTECH-3G-MIB", "qtech3GBackupIMSI"))
)
if mibBuilder.loadTexts:
    qtech3GBackupIntfSwitch.setStatus(
        "current"
    )

qtech3GBaseSationSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 3, 1, 6)
)
qtech3GBaseSationSwitch.setObjects(
      *(("QTECH-3G-MIB", "qtech3GISP"),
        ("QTECH-3G-MIB", "qtech3GCellID"),
        ("QTECH-3G-MIB", "qtech3GLAC"),
        ("QTECH-3G-MIB", "qtech3GBSID"),
        ("QTECH-3G-MIB", "qtech3GSID"),
        ("QTECH-3G-MIB", "qtech3GNID"),
        ("QTECH-3G-MIB", "qtech3GIMSI"),
        ("QTECH-3G-MIB", "qtech3GPhoneNumber"))
)
if mibBuilder.loadTexts:
    qtech3GBaseSationSwitch.setStatus(
        "current"
    )

qtech3GTrafficInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 1, 3, 1, 7)
)
qtech3GTrafficInformation.setObjects(
      *(("QTECH-3G-MIB", "qtech3GIPAddr"),
        ("QTECH-3G-MIB", "qtech3GIMSI"),
        ("QTECH-3G-MIB", "qtech3GSerialNumber"),
        ("QTECH-3G-MIB", "qtech3GInOctets"),
        ("QTECH-3G-MIB", "qtech3GOutOctets"))
)
if mibBuilder.loadTexts:
    qtech3GTrafficInformation.setStatus(
        "current"
    )

qtech3GLineDetectedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 2, 1, 1)
)
qtech3GLineDetectedNotification.setObjects(
      *(("QTECH-3G-MIB", "qtech3GRouterSN"),
        ("QTECH-3G-MIB", "qtech3GCardIMSI"),
        ("QTECH-3G-MIB", "qtech3GIntfIPAddr"),
        ("QTECH-3G-MIB", "qtech3GLineDetected"),
        ("QTECH-3G-MIB", "qtech3GLineDetectedResult"),
        ("QTECH-3G-MIB", "qtech3GLineDetectedMainCause"),
        ("QTECH-3G-MIB", "qtech3GLineDetectedSubCause"),
        ("QTECH-3G-MIB", "qtech3GDeviceBackupInfo"),
        ("QTECH-3G-MIB", "qtech3GRssiStrength"),
        ("QTECH-3G-MIB", "qtech3GDeviceBackupIMSI"))
)
if mibBuilder.loadTexts:
    qtech3GLineDetectedNotification.setStatus(
        "current"
    )

qtech3GUserUpLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 2, 1, 2)
)
qtech3GUserUpLine.setObjects(
      *(("QTECH-3G-MIB", "qtech3GRouterSlotNumber"),
        ("QTECH-3G-MIB", "qtech3GCardIMSI"),
        ("QTECH-3G-MIB", "qtech3GIntfIPAddr"),
        ("QTECH-3G-MIB", "qtech3GTrafficPreventListName"),
        ("QTECH-3G-MIB", "qtech3GTrafficPreventListID"),
        ("QTECH-3G-MIB", "qtech3GTrafficPreventIfIndex"),
        ("QTECH-3G-MIB", "qtech3GTrafficPreventMode"),
        ("QTECH-3G-MIB", "qtech3GPppUsername"),
        ("QTECH-3G-MIB", "qtech3GRouterSN"),
        ("QTECH-3G-MIB", "qtech3GCardPhoneNumber"),
        ("QTECH-3G-MIB", "qtech3GDailMode"),
        ("QTECH-3G-MIB", "qtech3GDialOnDemandIfIndex"),
        ("QTECH-3G-MIB", "qtech3GDeviceModemType"))
)
if mibBuilder.loadTexts:
    qtech3GUserUpLine.setStatus(
        "current"
    )

qtech3GUserDownLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 2, 1, 3)
)
qtech3GUserDownLine.setObjects(
      *(("QTECH-3G-MIB", "qtech3GRouterSlotNumber"),
        ("QTECH-3G-MIB", "qtech3GCardIMSI"),
        ("QTECH-3G-MIB", "qtech3GIntfIPAddr"),
        ("QTECH-3G-MIB", "qtech3GTrafficPreventListName"),
        ("QTECH-3G-MIB", "qtech3GTrafficPreventListID"),
        ("QTECH-3G-MIB", "qtech3GTrafficPreventIfIndex"),
        ("QTECH-3G-MIB", "qtech3GTrafficPreventMode"),
        ("QTECH-3G-MIB", "qtech3GPppUsername"),
        ("QTECH-3G-MIB", "qtech3GRouterSN"),
        ("QTECH-3G-MIB", "qtech3GCardPhoneNumber"),
        ("QTECH-3G-MIB", "qtech3GDailMode"),
        ("QTECH-3G-MIB", "qtech3GDialOnDemandIfIndex"),
        ("QTECH-3G-MIB", "qtech3GDeviceModemType"))
)
if mibBuilder.loadTexts:
    qtech3GUserDownLine.setStatus(
        "current"
    )

qtech3GRssiNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 2, 1, 4)
)
qtech3GRssiNotification.setObjects(
      *(("QTECH-3G-MIB", "qtech3GRouterSlotNumber"),
        ("QTECH-3G-MIB", "qtech3GCardIMSI"),
        ("QTECH-3G-MIB", "qtech3GRouterSN"),
        ("QTECH-3G-MIB", "qtech3GIntfIPAddr"),
        ("QTECH-3G-MIB", "qtech3GRssiStrengthPercent"),
        ("QTECH-3G-MIB", "qtech3GRssiStrength"),
        ("QTECH-3G-MIB", "qtech3GDeviceModemType"))
)
if mibBuilder.loadTexts:
    qtech3GRssiNotification.setStatus(
        "current"
    )

qtech3GTrafficInfoNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 2, 1, 5)
)
qtech3GTrafficInfoNotification.setObjects(
      *(("QTECH-3G-MIB", "qtech3GRouterSlotNumber"),
        ("QTECH-3G-MIB", "qtech3GCardIMSI"),
        ("QTECH-3G-MIB", "qtech3GRouterSN"),
        ("QTECH-3G-MIB", "qtech3GIntfIPAddr"),
        ("QTECH-3G-MIB", "qtech3GOutOctets"),
        ("QTECH-3G-MIB", "qtech3GInOctets"),
        ("QTECH-3G-MIB", "qtech3GDeviceModemType"),
        ("QTECH-3G-MIB", "qtech3GLineCardType"),
        ("QTECH-3G-MIB", "qtech3GModemIMEI"),
        ("QTECH-3G-MIB", "qtech3GCardPhoneNumber"),
        ("QTECH-3G-MIB", "qtech3GDeviceBackupInfo"),
        ("QTECH-3G-MIB", "qtech3GRssiStrength"),
        ("QTECH-3G-MIB", "qtech3GRssiStrengthPercent"),
        ("QTECH-3G-MIB", "qtech3GNetworkISPMode"),
        ("QTECH-3G-MIB", "qtech3GNetworkSysMode"),
        ("QTECH-3G-MIB", "qtech3GSIMCardStatus"),
        ("QTECH-3G-MIB", "qtech3GDailMode"),
        ("QTECH-3G-MIB", "qtech3GPppUsername"),
        ("QTECH-3G-MIB", "qtech3GUserActiveTime"),
        ("QTECH-3G-MIB", "qtech3GAcessBSCellID"),
        ("QTECH-3G-MIB", "qtech3GAcessBSLAC"),
        ("QTECH-3G-MIB", "qtech3GAcessBSLONG"),
        ("QTECH-3G-MIB", "qtech3GAcessBSLAT"),
        ("QTECH-3G-MIB", "qtech3GInSpeed"),
        ("QTECH-3G-MIB", "qtech3GOutSpeed"),
        ("QTECH-3G-MIB", "qtech3G2ifIndex"),
        ("QTECH-3G-MIB", "qtech3GTrafficTrapInterval"),
        ("QTECH-3G-MIB", "qtech3GRssiThreshold"),
        ("QTECH-3G-MIB", "qtech3GTrapFilterMode"),
        ("QTECH-3G-MIB", "qtech3GISPtimeout"))
)
if mibBuilder.loadTexts:
    qtech3GTrafficInfoNotification.setStatus(
        "current"
    )

qtech3GBackupMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 2, 1, 6)
)
qtech3GBackupMaster.setObjects(
      *(("QTECH-3G-MIB", "qtech3GRouterSlotNumber"),
        ("QTECH-3G-MIB", "qtech3GCardIMSI"),
        ("QTECH-3G-MIB", "qtech3GIntfIPAddr"),
        ("QTECH-3G-MIB", "qtech3GTrafficPreventListName"),
        ("QTECH-3G-MIB", "qtech3GTrafficPreventListID"),
        ("QTECH-3G-MIB", "qtech3GTrafficPreventIfIndex"),
        ("QTECH-3G-MIB", "qtech3GTrafficPreventMode"),
        ("QTECH-3G-MIB", "qtech3GPppUsername"),
        ("QTECH-3G-MIB", "qtech3GRouterSN"),
        ("QTECH-3G-MIB", "qtech3GCardPhoneNumber"),
        ("QTECH-3G-MIB", "qtech3GDailMode"),
        ("QTECH-3G-MIB", "qtech3GDialOnDemandIfIndex"),
        ("QTECH-3G-MIB", "qtech3GDeviceModemType"))
)
if mibBuilder.loadTexts:
    qtech3GBackupMaster.setStatus(
        "current"
    )

qtech3GBackupSlave = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 95, 2, 1, 7)
)
qtech3GBackupSlave.setObjects(
      *(("QTECH-3G-MIB", "qtech3GRouterSlotNumber"),
        ("QTECH-3G-MIB", "qtech3GCardIMSI"),
        ("QTECH-3G-MIB", "qtech3GIntfIPAddr"),
        ("QTECH-3G-MIB", "qtech3GTrafficPreventListName"),
        ("QTECH-3G-MIB", "qtech3GTrafficPreventListID"),
        ("QTECH-3G-MIB", "qtech3GTrafficPreventIfIndex"),
        ("QTECH-3G-MIB", "qtech3GTrafficPreventMode"),
        ("QTECH-3G-MIB", "qtech3GPppUsername"),
        ("QTECH-3G-MIB", "qtech3GRouterSN"),
        ("QTECH-3G-MIB", "qtech3GCardPhoneNumber"),
        ("QTECH-3G-MIB", "qtech3GDailMode"),
        ("QTECH-3G-MIB", "qtech3GDialOnDemandIfIndex"),
        ("QTECH-3G-MIB", "qtech3GDeviceModemType"))
)
if mibBuilder.loadTexts:
    qtech3GBackupSlave.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-3G-MIB",
    **{"qtech3GMonitor": qtech3GMonitor,
       "qtech3GObjects": qtech3GObjects,
       "qtech3GTable": qtech3GTable,
       "qtech3GEntry": qtech3GEntry,
       "qtech3gUsername": qtech3gUsername,
       "qtech3GOnlineStatus": qtech3GOnlineStatus,
       "qtech3GIMEI": qtech3GIMEI,
       "qtech3GIPAddrType": qtech3GIPAddrType,
       "qtech3GIPAddr": qtech3GIPAddr,
       "qtech3GUplineTime": qtech3GUplineTime,
       "qtech3GActiveTime": qtech3GActiveTime,
       "qtech3GSignalStrength": qtech3GSignalStrength,
       "qtech3GISP": qtech3GISP,
       "qtech3GSysMode": qtech3GSysMode,
       "qtech3GServiceStatus": qtech3GServiceStatus,
       "qtech3GRoamingStatus": qtech3GRoamingStatus,
       "qtech3GDomain": qtech3GDomain,
       "qtech3GSIMStatus": qtech3GSIMStatus,
       "qtech3GSignalStrengthPercent": qtech3GSignalStrengthPercent,
       "qtech3GApn": qtech3GApn,
       "qtech3GCellID": qtech3GCellID,
       "qtech3GLAC": qtech3GLAC,
       "qtech3GBSID": qtech3GBSID,
       "qtech3GNID": qtech3GNID,
       "qtech3GSID": qtech3GSID,
       "qtech3GIMSI": qtech3GIMSI,
       "qtech3GESN": qtech3GESN,
       "qtech3GPhoneNumber": qtech3GPhoneNumber,
       "qtech3GifIndex": qtech3GifIndex,
       "qtech3GBSLONG": qtech3GBSLONG,
       "qtech3GBSLAT": qtech3GBSLAT,
       "qtech3GBackupInfo": qtech3GBackupInfo,
       "qtech3GSerialNumber": qtech3GSerialNumber,
       "qtech3GBackupIMSI": qtech3GBackupIMSI,
       "qtech3GGatewayIPAddr": qtech3GGatewayIPAddr,
       "qtech3GLineDownCause": qtech3GLineDownCause,
       "qtech3GModemType": qtech3GModemType,
       "qtech3GStatTable": qtech3GStatTable,
       "qtech3GStatEntry": qtech3GStatEntry,
       "qtech3GInOctets": qtech3GInOctets,
       "qtech3GOutOctets": qtech3GOutOctets,
       "qtech3GInSpeed": qtech3GInSpeed,
       "qtech3GOutSpeed": qtech3GOutSpeed,
       "qtech3G2IMSI": qtech3G2IMSI,
       "qtech3G2ifIndex": qtech3G2ifIndex,
       "qtech3GTrap": qtech3GTrap,
       "qtech3GNotifications": qtech3GNotifications,
       "qtech3GSignalThreshold": qtech3GSignalThreshold,
       "qtech3GUpLine": qtech3GUpLine,
       "qtech3GDownLine": qtech3GDownLine,
       "qtech3GChangeAccessPoint": qtech3GChangeAccessPoint,
       "qtech3GBackupIntfSwitch": qtech3GBackupIntfSwitch,
       "qtech3GBaseSationSwitch": qtech3GBaseSationSwitch,
       "qtech3GTrafficInformation": qtech3GTrafficInformation,
       "qtech3GBsNumber": qtech3GBsNumber,
       "qtech3GBsTable": qtech3GBsTable,
       "qtech3GBsEntry": qtech3GBsEntry,
       "qtech3GBsSN": qtech3GBsSN,
       "qtech3GBsISP": qtech3GBsISP,
       "qtech3GBsMode": qtech3GBsMode,
       "qtech3GBsIMSI": qtech3GBsIMSI,
       "qtech3GBsLAC": qtech3GBsLAC,
       "qtech3GBsCellID": qtech3GBsCellID,
       "qtech3GBsBSID": qtech3GBsBSID,
       "qtech3GBsSID": qtech3GBsSID,
       "qtech3GBsNID": qtech3GBsNID,
       "qtech3GBsRssi": qtech3GBsRssi,
       "qtech3GBsBSLONG": qtech3GBsBSLONG,
       "qtech3GBsBSLAT": qtech3GBsBSLAT,
       "qtech3GDeviceManagementTable": qtech3GDeviceManagementTable,
       "qtech3GDeviceManagementEntry": qtech3GDeviceManagementEntry,
       "qtech3GRouterType": qtech3GRouterType,
       "qtech3GRouterSN": qtech3GRouterSN,
       "qtech3GRouterSlotNumber": qtech3GRouterSlotNumber,
       "qtech3GLineCardType": qtech3GLineCardType,
       "qtech3GCardIMSI": qtech3GCardIMSI,
       "qtech3GModemIMEI": qtech3GModemIMEI,
       "qtech3GIntfIPAddr": qtech3GIntfIPAddr,
       "qtech3GCardPhoneNumber": qtech3GCardPhoneNumber,
       "qtech3GLineDetected": qtech3GLineDetected,
       "qtech3GLineDetectedResult": qtech3GLineDetectedResult,
       "qtech3GLineDetectedMainCause": qtech3GLineDetectedMainCause,
       "qtech3GLineDetectedSubCause": qtech3GLineDetectedSubCause,
       "qtech3GDeviceBackupInfo": qtech3GDeviceBackupInfo,
       "qtech3GRssiStrength": qtech3GRssiStrength,
       "qtech3GRssiStrengthPercent": qtech3GRssiStrengthPercent,
       "qtech3GNetworkISPMode": qtech3GNetworkISPMode,
       "qtech3GNetworkSysMode": qtech3GNetworkSysMode,
       "qtech3GNetworkServiceStatus": qtech3GNetworkServiceStatus,
       "qtech3GSIMCardStatus": qtech3GSIMCardStatus,
       "qtech3GDailMode": qtech3GDailMode,
       "qtech3GDeviceBackupIMSI": qtech3GDeviceBackupIMSI,
       "qtech3GLineDetectedMode": qtech3GLineDetectedMode,
       "qtech3GPppUsername": qtech3GPppUsername,
       "qtech3GUserApn": qtech3GUserApn,
       "qtech3GModemOnlineStatus": qtech3GModemOnlineStatus,
       "qtech3GIntfIPAddrType": qtech3GIntfIPAddrType,
       "qtech3GUserUplineTime": qtech3GUserUplineTime,
       "qtech3GUserActiveTime": qtech3GUserActiveTime,
       "qtech3GSIMRoamingStatus": qtech3GSIMRoamingStatus,
       "qtech3GAcessBSCellID": qtech3GAcessBSCellID,
       "qtech3GAcessBSLAC": qtech3GAcessBSLAC,
       "qtech3GAcessBSLONG": qtech3GAcessBSLONG,
       "qtech3GAcessBSLAT": qtech3GAcessBSLAT,
       "qtech3GDialOnDemandIfIndex": qtech3GDialOnDemandIfIndex,
       "qtech3GTrafficPreventMode": qtech3GTrafficPreventMode,
       "qtech3GTrafficPreventIfIndex": qtech3GTrafficPreventIfIndex,
       "qtech3GTrafficPreventListID": qtech3GTrafficPreventListID,
       "qtech3GTrafficPreventListName": qtech3GTrafficPreventListName,
       "qtech3GDeviceModemType": qtech3GDeviceModemType,
       "qtech3GTrafficTrapInterval": qtech3GTrafficTrapInterval,
       "qtech3GRssiThreshold": qtech3GRssiThreshold,
       "qtech3GTrapFilterMode": qtech3GTrapFilterMode,
       "qtech3GISPtimeout": qtech3GISPtimeout,
       "qtech3GEncrypt_type": qtech3GEncrypt_type,
       "qtech3GPassword": qtech3GPassword,
       "qtech3GTrapNew": qtech3GTrapNew,
       "qtech3GNotificationsNew": qtech3GNotificationsNew,
       "qtech3GLineDetectedNotification": qtech3GLineDetectedNotification,
       "qtech3GUserUpLine": qtech3GUserUpLine,
       "qtech3GUserDownLine": qtech3GUserDownLine,
       "qtech3GRssiNotification": qtech3GRssiNotification,
       "qtech3GTrafficInfoNotification": qtech3GTrafficInfoNotification,
       "qtech3GBackupMaster": qtech3GBackupMaster,
       "qtech3GBackupSlave": qtech3GBackupSlave}
)
