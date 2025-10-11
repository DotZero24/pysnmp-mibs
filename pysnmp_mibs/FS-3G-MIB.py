# SNMP MIB module (FS-3G-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-3G-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:58 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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

fs3GMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95)
)
if mibBuilder.loadTexts:
    fs3GMonitor.setRevisions(
        ("2011-02-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fs3GObjects_ObjectIdentity = ObjectIdentity
fs3GObjects = _Fs3GObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1)
)
_Fs3GTable_Object = MibTable
fs3GTable = _Fs3GTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1)
)
if mibBuilder.loadTexts:
    fs3GTable.setStatus("current")
_Fs3GEntry_Object = MibTableRow
fs3GEntry = _Fs3GEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1)
)
fs3GEntry.setIndexNames(
    (0, "FS-3G-MIB", "fs3GIPAddr"),
)
if mibBuilder.loadTexts:
    fs3GEntry.setStatus("current")
_Fs3gUsername_Type = DisplayString
_Fs3gUsername_Object = MibTableColumn
fs3gUsername = _Fs3gUsername_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 1),
    _Fs3gUsername_Type()
)
fs3gUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3gUsername.setStatus("current")


class _Fs3GOnlineStatus_Type(Integer32):
    """Custom type fs3GOnlineStatus based on Integer32"""
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


_Fs3GOnlineStatus_Type.__name__ = "Integer32"
_Fs3GOnlineStatus_Object = MibTableColumn
fs3GOnlineStatus = _Fs3GOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 2),
    _Fs3GOnlineStatus_Type()
)
fs3GOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GOnlineStatus.setStatus("current")
_Fs3GIMEI_Type = DisplayString
_Fs3GIMEI_Object = MibTableColumn
fs3GIMEI = _Fs3GIMEI_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 3),
    _Fs3GIMEI_Type()
)
fs3GIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GIMEI.setStatus("current")


class _Fs3GIPAddrType_Type(Integer32):
    """Custom type fs3GIPAddrType based on Integer32"""
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


_Fs3GIPAddrType_Type.__name__ = "Integer32"
_Fs3GIPAddrType_Object = MibTableColumn
fs3GIPAddrType = _Fs3GIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 4),
    _Fs3GIPAddrType_Type()
)
fs3GIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GIPAddrType.setStatus("current")
_Fs3GIPAddr_Type = IpAddress
_Fs3GIPAddr_Object = MibTableColumn
fs3GIPAddr = _Fs3GIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 5),
    _Fs3GIPAddr_Type()
)
fs3GIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GIPAddr.setStatus("current")
_Fs3GUplineTime_Type = TimeStamp
_Fs3GUplineTime_Object = MibTableColumn
fs3GUplineTime = _Fs3GUplineTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 6),
    _Fs3GUplineTime_Type()
)
fs3GUplineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GUplineTime.setStatus("current")


class _Fs3GActiveTime_Type(Integer32):
    """Custom type fs3GActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Fs3GActiveTime_Type.__name__ = "Integer32"
_Fs3GActiveTime_Object = MibTableColumn
fs3GActiveTime = _Fs3GActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 7),
    _Fs3GActiveTime_Type()
)
fs3GActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GActiveTime.setStatus("current")


class _Fs3GSignalStrength_Type(Integer32):
    """Custom type fs3GSignalStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Fs3GSignalStrength_Type.__name__ = "Integer32"
_Fs3GSignalStrength_Object = MibTableColumn
fs3GSignalStrength = _Fs3GSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 8),
    _Fs3GSignalStrength_Type()
)
fs3GSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GSignalStrength.setStatus("current")


class _Fs3GISP_Type(Integer32):
    """Custom type fs3GISP based on Integer32"""
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


_Fs3GISP_Type.__name__ = "Integer32"
_Fs3GISP_Object = MibTableColumn
fs3GISP = _Fs3GISP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 9),
    _Fs3GISP_Type()
)
fs3GISP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GISP.setStatus("current")


class _Fs3GSysMode_Type(Integer32):
    """Custom type fs3GSysMode based on Integer32"""
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


_Fs3GSysMode_Type.__name__ = "Integer32"
_Fs3GSysMode_Object = MibTableColumn
fs3GSysMode = _Fs3GSysMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 10),
    _Fs3GSysMode_Type()
)
fs3GSysMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GSysMode.setStatus("current")


class _Fs3GServiceStatus_Type(Integer32):
    """Custom type fs3GServiceStatus based on Integer32"""
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


_Fs3GServiceStatus_Type.__name__ = "Integer32"
_Fs3GServiceStatus_Object = MibTableColumn
fs3GServiceStatus = _Fs3GServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 11),
    _Fs3GServiceStatus_Type()
)
fs3GServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GServiceStatus.setStatus("current")


class _Fs3GRoamingStatus_Type(Integer32):
    """Custom type fs3GRoamingStatus based on Integer32"""
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


_Fs3GRoamingStatus_Type.__name__ = "Integer32"
_Fs3GRoamingStatus_Object = MibTableColumn
fs3GRoamingStatus = _Fs3GRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 12),
    _Fs3GRoamingStatus_Type()
)
fs3GRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GRoamingStatus.setStatus("current")


class _Fs3GDomain_Type(Integer32):
    """Custom type fs3GDomain based on Integer32"""
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


_Fs3GDomain_Type.__name__ = "Integer32"
_Fs3GDomain_Object = MibTableColumn
fs3GDomain = _Fs3GDomain_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 13),
    _Fs3GDomain_Type()
)
fs3GDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GDomain.setStatus("current")


class _Fs3GSIMStatus_Type(Integer32):
    """Custom type fs3GSIMStatus based on Integer32"""
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


_Fs3GSIMStatus_Type.__name__ = "Integer32"
_Fs3GSIMStatus_Object = MibTableColumn
fs3GSIMStatus = _Fs3GSIMStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 14),
    _Fs3GSIMStatus_Type()
)
fs3GSIMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GSIMStatus.setStatus("current")


class _Fs3GSignalStrengthPercent_Type(Integer32):
    """Custom type fs3GSignalStrengthPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fs3GSignalStrengthPercent_Type.__name__ = "Integer32"
_Fs3GSignalStrengthPercent_Object = MibTableColumn
fs3GSignalStrengthPercent = _Fs3GSignalStrengthPercent_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 15),
    _Fs3GSignalStrengthPercent_Type()
)
fs3GSignalStrengthPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GSignalStrengthPercent.setStatus("current")
_Fs3GApn_Type = DisplayString
_Fs3GApn_Object = MibTableColumn
fs3GApn = _Fs3GApn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 16),
    _Fs3GApn_Type()
)
fs3GApn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GApn.setStatus("current")


class _Fs3GCellID_Type(Integer32):
    """Custom type fs3GCellID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fs3GCellID_Type.__name__ = "Integer32"
_Fs3GCellID_Object = MibTableColumn
fs3GCellID = _Fs3GCellID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 17),
    _Fs3GCellID_Type()
)
fs3GCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GCellID.setStatus("current")


class _Fs3GLAC_Type(Integer32):
    """Custom type fs3GLAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fs3GLAC_Type.__name__ = "Integer32"
_Fs3GLAC_Object = MibTableColumn
fs3GLAC = _Fs3GLAC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 18),
    _Fs3GLAC_Type()
)
fs3GLAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GLAC.setStatus("current")


class _Fs3GBSID_Type(Integer32):
    """Custom type fs3GBSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fs3GBSID_Type.__name__ = "Integer32"
_Fs3GBSID_Object = MibTableColumn
fs3GBSID = _Fs3GBSID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 19),
    _Fs3GBSID_Type()
)
fs3GBSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GBSID.setStatus("current")


class _Fs3GNID_Type(Integer32):
    """Custom type fs3GNID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fs3GNID_Type.__name__ = "Integer32"
_Fs3GNID_Object = MibTableColumn
fs3GNID = _Fs3GNID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 20),
    _Fs3GNID_Type()
)
fs3GNID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GNID.setStatus("current")


class _Fs3GSID_Type(Integer32):
    """Custom type fs3GSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fs3GSID_Type.__name__ = "Integer32"
_Fs3GSID_Object = MibTableColumn
fs3GSID = _Fs3GSID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 21),
    _Fs3GSID_Type()
)
fs3GSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GSID.setStatus("current")
_Fs3GIMSI_Type = DisplayString
_Fs3GIMSI_Object = MibTableColumn
fs3GIMSI = _Fs3GIMSI_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 22),
    _Fs3GIMSI_Type()
)
fs3GIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GIMSI.setStatus("current")
_Fs3GESN_Type = DisplayString
_Fs3GESN_Object = MibTableColumn
fs3GESN = _Fs3GESN_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 23),
    _Fs3GESN_Type()
)
fs3GESN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GESN.setStatus("current")
_Fs3GPhoneNumber_Type = DisplayString
_Fs3GPhoneNumber_Object = MibTableColumn
fs3GPhoneNumber = _Fs3GPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 24),
    _Fs3GPhoneNumber_Type()
)
fs3GPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GPhoneNumber.setStatus("current")
_Fs3GifIndex_Type = Integer32
_Fs3GifIndex_Object = MibTableColumn
fs3GifIndex = _Fs3GifIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 25),
    _Fs3GifIndex_Type()
)
fs3GifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GifIndex.setStatus("current")
_Fs3GBSLONG_Type = Integer32
_Fs3GBSLONG_Object = MibTableColumn
fs3GBSLONG = _Fs3GBSLONG_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 26),
    _Fs3GBSLONG_Type()
)
fs3GBSLONG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GBSLONG.setStatus("current")
_Fs3GBSLAT_Type = Integer32
_Fs3GBSLAT_Object = MibTableColumn
fs3GBSLAT = _Fs3GBSLAT_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 27),
    _Fs3GBSLAT_Type()
)
fs3GBSLAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GBSLAT.setStatus("current")


class _Fs3GBackupInfo_Type(Integer32):
    """Custom type fs3GBackupInfo based on Integer32"""
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


_Fs3GBackupInfo_Type.__name__ = "Integer32"
_Fs3GBackupInfo_Object = MibTableColumn
fs3GBackupInfo = _Fs3GBackupInfo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 28),
    _Fs3GBackupInfo_Type()
)
fs3GBackupInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GBackupInfo.setStatus("current")
_Fs3GSerialNumber_Type = DisplayString
_Fs3GSerialNumber_Object = MibTableColumn
fs3GSerialNumber = _Fs3GSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 29),
    _Fs3GSerialNumber_Type()
)
fs3GSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GSerialNumber.setStatus("current")
_Fs3GBackupIMSI_Type = DisplayString
_Fs3GBackupIMSI_Object = MibTableColumn
fs3GBackupIMSI = _Fs3GBackupIMSI_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 30),
    _Fs3GBackupIMSI_Type()
)
fs3GBackupIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GBackupIMSI.setStatus("current")
_Fs3GGatewayIPAddr_Type = IpAddress
_Fs3GGatewayIPAddr_Object = MibTableColumn
fs3GGatewayIPAddr = _Fs3GGatewayIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 31),
    _Fs3GGatewayIPAddr_Type()
)
fs3GGatewayIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GGatewayIPAddr.setStatus("current")
_Fs3GLineDownCause_Type = Integer32
_Fs3GLineDownCause_Object = MibTableColumn
fs3GLineDownCause = _Fs3GLineDownCause_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 32),
    _Fs3GLineDownCause_Type()
)
fs3GLineDownCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GLineDownCause.setStatus("current")


class _Fs3GModemType_Type(Integer32):
    """Custom type fs3GModemType based on Integer32"""
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


_Fs3GModemType_Type.__name__ = "Integer32"
_Fs3GModemType_Object = MibTableColumn
fs3GModemType = _Fs3GModemType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 1, 1, 33),
    _Fs3GModemType_Type()
)
fs3GModemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GModemType.setStatus("current")
_Fs3GStatTable_Object = MibTable
fs3GStatTable = _Fs3GStatTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 2)
)
if mibBuilder.loadTexts:
    fs3GStatTable.setStatus("current")
_Fs3GStatEntry_Object = MibTableRow
fs3GStatEntry = _Fs3GStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 2, 1)
)
fs3GStatEntry.setIndexNames(
    (0, "FS-3G-MIB", "fs3GIPAddr"),
)
if mibBuilder.loadTexts:
    fs3GStatEntry.setStatus("current")
_Fs3GInOctets_Type = Counter64
_Fs3GInOctets_Object = MibTableColumn
fs3GInOctets = _Fs3GInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 2, 1, 1),
    _Fs3GInOctets_Type()
)
fs3GInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GInOctets.setStatus("current")
_Fs3GOutOctets_Type = Counter64
_Fs3GOutOctets_Object = MibTableColumn
fs3GOutOctets = _Fs3GOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 2, 1, 2),
    _Fs3GOutOctets_Type()
)
fs3GOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GOutOctets.setStatus("current")
_Fs3GInSpeed_Type = Counter64
_Fs3GInSpeed_Object = MibTableColumn
fs3GInSpeed = _Fs3GInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 2, 1, 3),
    _Fs3GInSpeed_Type()
)
fs3GInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GInSpeed.setStatus("current")
_Fs3GOutSpeed_Type = Counter64
_Fs3GOutSpeed_Object = MibTableColumn
fs3GOutSpeed = _Fs3GOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 2, 1, 4),
    _Fs3GOutSpeed_Type()
)
fs3GOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GOutSpeed.setStatus("current")
_Fs3G2IMSI_Type = DisplayString
_Fs3G2IMSI_Object = MibTableColumn
fs3G2IMSI = _Fs3G2IMSI_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 2, 1, 5),
    _Fs3G2IMSI_Type()
)
fs3G2IMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3G2IMSI.setStatus("current")
_Fs3G2ifIndex_Type = Integer32
_Fs3G2ifIndex_Object = MibTableColumn
fs3G2ifIndex = _Fs3G2ifIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 2, 1, 6),
    _Fs3G2ifIndex_Type()
)
fs3G2ifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3G2ifIndex.setStatus("current")
_Fs3GTrap_ObjectIdentity = ObjectIdentity
fs3GTrap = _Fs3GTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 3)
)
_Fs3GNotifications_ObjectIdentity = ObjectIdentity
fs3GNotifications = _Fs3GNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 3, 1)
)
_Fs3GBsNumber_Type = Integer32
_Fs3GBsNumber_Object = MibScalar
fs3GBsNumber = _Fs3GBsNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 4),
    _Fs3GBsNumber_Type()
)
fs3GBsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GBsNumber.setStatus("current")
_Fs3GBsTable_Object = MibTable
fs3GBsTable = _Fs3GBsTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 5)
)
if mibBuilder.loadTexts:
    fs3GBsTable.setStatus("current")
_Fs3GBsEntry_Object = MibTableRow
fs3GBsEntry = _Fs3GBsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 5, 1)
)
fs3GBsEntry.setIndexNames(
    (0, "FS-3G-MIB", "fs3GBsSN"),
)
if mibBuilder.loadTexts:
    fs3GBsEntry.setStatus("current")
_Fs3GBsSN_Type = Integer32
_Fs3GBsSN_Object = MibTableColumn
fs3GBsSN = _Fs3GBsSN_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 5, 1, 1),
    _Fs3GBsSN_Type()
)
fs3GBsSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GBsSN.setStatus("current")


class _Fs3GBsISP_Type(Integer32):
    """Custom type fs3GBsISP based on Integer32"""
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


_Fs3GBsISP_Type.__name__ = "Integer32"
_Fs3GBsISP_Object = MibTableColumn
fs3GBsISP = _Fs3GBsISP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 5, 1, 2),
    _Fs3GBsISP_Type()
)
fs3GBsISP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GBsISP.setStatus("current")


class _Fs3GBsMode_Type(Integer32):
    """Custom type fs3GBsMode based on Integer32"""
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


_Fs3GBsMode_Type.__name__ = "Integer32"
_Fs3GBsMode_Object = MibTableColumn
fs3GBsMode = _Fs3GBsMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 5, 1, 3),
    _Fs3GBsMode_Type()
)
fs3GBsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GBsMode.setStatus("current")
_Fs3GBsIMSI_Type = DisplayString
_Fs3GBsIMSI_Object = MibTableColumn
fs3GBsIMSI = _Fs3GBsIMSI_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 5, 1, 4),
    _Fs3GBsIMSI_Type()
)
fs3GBsIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GBsIMSI.setStatus("current")
_Fs3GBsLAC_Type = Integer32
_Fs3GBsLAC_Object = MibTableColumn
fs3GBsLAC = _Fs3GBsLAC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 5, 1, 5),
    _Fs3GBsLAC_Type()
)
fs3GBsLAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GBsLAC.setStatus("current")
_Fs3GBsCellID_Type = Integer32
_Fs3GBsCellID_Object = MibTableColumn
fs3GBsCellID = _Fs3GBsCellID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 5, 1, 6),
    _Fs3GBsCellID_Type()
)
fs3GBsCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GBsCellID.setStatus("current")
_Fs3GBsBSID_Type = Integer32
_Fs3GBsBSID_Object = MibTableColumn
fs3GBsBSID = _Fs3GBsBSID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 5, 1, 7),
    _Fs3GBsBSID_Type()
)
fs3GBsBSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GBsBSID.setStatus("current")
_Fs3GBsSID_Type = Integer32
_Fs3GBsSID_Object = MibTableColumn
fs3GBsSID = _Fs3GBsSID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 5, 1, 8),
    _Fs3GBsSID_Type()
)
fs3GBsSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GBsSID.setStatus("current")
_Fs3GBsNID_Type = Integer32
_Fs3GBsNID_Object = MibTableColumn
fs3GBsNID = _Fs3GBsNID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 5, 1, 9),
    _Fs3GBsNID_Type()
)
fs3GBsNID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GBsNID.setStatus("current")
_Fs3GBsRssi_Type = Integer32
_Fs3GBsRssi_Object = MibTableColumn
fs3GBsRssi = _Fs3GBsRssi_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 5, 1, 10),
    _Fs3GBsRssi_Type()
)
fs3GBsRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GBsRssi.setStatus("current")
_Fs3GBsBSLONG_Type = Integer32
_Fs3GBsBSLONG_Object = MibTableColumn
fs3GBsBSLONG = _Fs3GBsBSLONG_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 5, 1, 11),
    _Fs3GBsBSLONG_Type()
)
fs3GBsBSLONG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GBsBSLONG.setStatus("current")
_Fs3GBsBSLAT_Type = Integer32
_Fs3GBsBSLAT_Object = MibTableColumn
fs3GBsBSLAT = _Fs3GBsBSLAT_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 5, 1, 12),
    _Fs3GBsBSLAT_Type()
)
fs3GBsBSLAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GBsBSLAT.setStatus("current")
_Fs3GDeviceManagementTable_Object = MibTable
fs3GDeviceManagementTable = _Fs3GDeviceManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6)
)
if mibBuilder.loadTexts:
    fs3GDeviceManagementTable.setStatus("current")
_Fs3GDeviceManagementEntry_Object = MibTableRow
fs3GDeviceManagementEntry = _Fs3GDeviceManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1)
)
fs3GDeviceManagementEntry.setIndexNames(
    (0, "FS-3G-MIB", "fs3GRouterSlotNumber"),
)
if mibBuilder.loadTexts:
    fs3GDeviceManagementEntry.setStatus("current")
_Fs3GRouterType_Type = DisplayString
_Fs3GRouterType_Object = MibTableColumn
fs3GRouterType = _Fs3GRouterType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 1),
    _Fs3GRouterType_Type()
)
fs3GRouterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GRouterType.setStatus("current")
_Fs3GRouterSN_Type = DisplayString
_Fs3GRouterSN_Object = MibTableColumn
fs3GRouterSN = _Fs3GRouterSN_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 2),
    _Fs3GRouterSN_Type()
)
fs3GRouterSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GRouterSN.setStatus("current")
_Fs3GRouterSlotNumber_Type = DisplayString
_Fs3GRouterSlotNumber_Object = MibTableColumn
fs3GRouterSlotNumber = _Fs3GRouterSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 3),
    _Fs3GRouterSlotNumber_Type()
)
fs3GRouterSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GRouterSlotNumber.setStatus("current")
_Fs3GLineCardType_Type = DisplayString
_Fs3GLineCardType_Object = MibTableColumn
fs3GLineCardType = _Fs3GLineCardType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 4),
    _Fs3GLineCardType_Type()
)
fs3GLineCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GLineCardType.setStatus("current")
_Fs3GCardIMSI_Type = DisplayString
_Fs3GCardIMSI_Object = MibTableColumn
fs3GCardIMSI = _Fs3GCardIMSI_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 5),
    _Fs3GCardIMSI_Type()
)
fs3GCardIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GCardIMSI.setStatus("current")
_Fs3GModemIMEI_Type = DisplayString
_Fs3GModemIMEI_Object = MibTableColumn
fs3GModemIMEI = _Fs3GModemIMEI_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 6),
    _Fs3GModemIMEI_Type()
)
fs3GModemIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GModemIMEI.setStatus("current")
_Fs3GIntfIPAddr_Type = IpAddress
_Fs3GIntfIPAddr_Object = MibTableColumn
fs3GIntfIPAddr = _Fs3GIntfIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 7),
    _Fs3GIntfIPAddr_Type()
)
fs3GIntfIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GIntfIPAddr.setStatus("current")
_Fs3GCardPhoneNumber_Type = DisplayString
_Fs3GCardPhoneNumber_Object = MibTableColumn
fs3GCardPhoneNumber = _Fs3GCardPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 8),
    _Fs3GCardPhoneNumber_Type()
)
fs3GCardPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GCardPhoneNumber.setStatus("current")
_Fs3GLineDetected_Type = Unsigned32
_Fs3GLineDetected_Object = MibTableColumn
fs3GLineDetected = _Fs3GLineDetected_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 9),
    _Fs3GLineDetected_Type()
)
fs3GLineDetected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fs3GLineDetected.setStatus("current")


class _Fs3GLineDetectedResult_Type(Integer32):
    """Custom type fs3GLineDetectedResult based on Integer32"""
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


_Fs3GLineDetectedResult_Type.__name__ = "Integer32"
_Fs3GLineDetectedResult_Object = MibTableColumn
fs3GLineDetectedResult = _Fs3GLineDetectedResult_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 10),
    _Fs3GLineDetectedResult_Type()
)
fs3GLineDetectedResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GLineDetectedResult.setStatus("current")


class _Fs3GLineDetectedMainCause_Type(Integer32):
    """Custom type fs3GLineDetectedMainCause based on Integer32"""
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


_Fs3GLineDetectedMainCause_Type.__name__ = "Integer32"
_Fs3GLineDetectedMainCause_Object = MibTableColumn
fs3GLineDetectedMainCause = _Fs3GLineDetectedMainCause_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 11),
    _Fs3GLineDetectedMainCause_Type()
)
fs3GLineDetectedMainCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GLineDetectedMainCause.setStatus("current")


class _Fs3GLineDetectedSubCause_Type(Integer32):
    """Custom type fs3GLineDetectedSubCause based on Integer32"""
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


_Fs3GLineDetectedSubCause_Type.__name__ = "Integer32"
_Fs3GLineDetectedSubCause_Object = MibTableColumn
fs3GLineDetectedSubCause = _Fs3GLineDetectedSubCause_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 12),
    _Fs3GLineDetectedSubCause_Type()
)
fs3GLineDetectedSubCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GLineDetectedSubCause.setStatus("current")


class _Fs3GDeviceBackupInfo_Type(Integer32):
    """Custom type fs3GDeviceBackupInfo based on Integer32"""
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


_Fs3GDeviceBackupInfo_Type.__name__ = "Integer32"
_Fs3GDeviceBackupInfo_Object = MibTableColumn
fs3GDeviceBackupInfo = _Fs3GDeviceBackupInfo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 13),
    _Fs3GDeviceBackupInfo_Type()
)
fs3GDeviceBackupInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GDeviceBackupInfo.setStatus("current")


class _Fs3GRssiStrength_Type(Integer32):
    """Custom type fs3GRssiStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Fs3GRssiStrength_Type.__name__ = "Integer32"
_Fs3GRssiStrength_Object = MibTableColumn
fs3GRssiStrength = _Fs3GRssiStrength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 14),
    _Fs3GRssiStrength_Type()
)
fs3GRssiStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GRssiStrength.setStatus("current")


class _Fs3GRssiStrengthPercent_Type(Integer32):
    """Custom type fs3GRssiStrengthPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fs3GRssiStrengthPercent_Type.__name__ = "Integer32"
_Fs3GRssiStrengthPercent_Object = MibTableColumn
fs3GRssiStrengthPercent = _Fs3GRssiStrengthPercent_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 15),
    _Fs3GRssiStrengthPercent_Type()
)
fs3GRssiStrengthPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GRssiStrengthPercent.setStatus("current")


class _Fs3GNetworkISPMode_Type(Integer32):
    """Custom type fs3GNetworkISPMode based on Integer32"""
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


_Fs3GNetworkISPMode_Type.__name__ = "Integer32"
_Fs3GNetworkISPMode_Object = MibTableColumn
fs3GNetworkISPMode = _Fs3GNetworkISPMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 16),
    _Fs3GNetworkISPMode_Type()
)
fs3GNetworkISPMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GNetworkISPMode.setStatus("current")


class _Fs3GNetworkSysMode_Type(Integer32):
    """Custom type fs3GNetworkSysMode based on Integer32"""
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


_Fs3GNetworkSysMode_Type.__name__ = "Integer32"
_Fs3GNetworkSysMode_Object = MibTableColumn
fs3GNetworkSysMode = _Fs3GNetworkSysMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 17),
    _Fs3GNetworkSysMode_Type()
)
fs3GNetworkSysMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fs3GNetworkSysMode.setStatus("current")


class _Fs3GNetworkServiceStatus_Type(Integer32):
    """Custom type fs3GNetworkServiceStatus based on Integer32"""
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


_Fs3GNetworkServiceStatus_Type.__name__ = "Integer32"
_Fs3GNetworkServiceStatus_Object = MibTableColumn
fs3GNetworkServiceStatus = _Fs3GNetworkServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 18),
    _Fs3GNetworkServiceStatus_Type()
)
fs3GNetworkServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GNetworkServiceStatus.setStatus("current")


class _Fs3GSIMCardStatus_Type(Integer32):
    """Custom type fs3GSIMCardStatus based on Integer32"""
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


_Fs3GSIMCardStatus_Type.__name__ = "Integer32"
_Fs3GSIMCardStatus_Object = MibTableColumn
fs3GSIMCardStatus = _Fs3GSIMCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 19),
    _Fs3GSIMCardStatus_Type()
)
fs3GSIMCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GSIMCardStatus.setStatus("current")


class _Fs3GDailMode_Type(Integer32):
    """Custom type fs3GDailMode based on Integer32"""
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


_Fs3GDailMode_Type.__name__ = "Integer32"
_Fs3GDailMode_Object = MibTableColumn
fs3GDailMode = _Fs3GDailMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 20),
    _Fs3GDailMode_Type()
)
fs3GDailMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fs3GDailMode.setStatus("current")
_Fs3GDeviceBackupIMSI_Type = DisplayString
_Fs3GDeviceBackupIMSI_Object = MibTableColumn
fs3GDeviceBackupIMSI = _Fs3GDeviceBackupIMSI_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 21),
    _Fs3GDeviceBackupIMSI_Type()
)
fs3GDeviceBackupIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GDeviceBackupIMSI.setStatus("current")


class _Fs3GLineDetectedMode_Type(Integer32):
    """Custom type fs3GLineDetectedMode based on Integer32"""
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


_Fs3GLineDetectedMode_Type.__name__ = "Integer32"
_Fs3GLineDetectedMode_Object = MibTableColumn
fs3GLineDetectedMode = _Fs3GLineDetectedMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 22),
    _Fs3GLineDetectedMode_Type()
)
fs3GLineDetectedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fs3GLineDetectedMode.setStatus("current")
_Fs3GPppUsername_Type = DisplayString
_Fs3GPppUsername_Object = MibTableColumn
fs3GPppUsername = _Fs3GPppUsername_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 23),
    _Fs3GPppUsername_Type()
)
fs3GPppUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fs3GPppUsername.setStatus("current")
_Fs3GUserApn_Type = DisplayString
_Fs3GUserApn_Object = MibTableColumn
fs3GUserApn = _Fs3GUserApn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 24),
    _Fs3GUserApn_Type()
)
fs3GUserApn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fs3GUserApn.setStatus("current")


class _Fs3GModemOnlineStatus_Type(Integer32):
    """Custom type fs3GModemOnlineStatus based on Integer32"""
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


_Fs3GModemOnlineStatus_Type.__name__ = "Integer32"
_Fs3GModemOnlineStatus_Object = MibTableColumn
fs3GModemOnlineStatus = _Fs3GModemOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 25),
    _Fs3GModemOnlineStatus_Type()
)
fs3GModemOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GModemOnlineStatus.setStatus("current")


class _Fs3GIntfIPAddrType_Type(Integer32):
    """Custom type fs3GIntfIPAddrType based on Integer32"""
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


_Fs3GIntfIPAddrType_Type.__name__ = "Integer32"
_Fs3GIntfIPAddrType_Object = MibTableColumn
fs3GIntfIPAddrType = _Fs3GIntfIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 26),
    _Fs3GIntfIPAddrType_Type()
)
fs3GIntfIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GIntfIPAddrType.setStatus("current")
_Fs3GUserUplineTime_Type = TimeStamp
_Fs3GUserUplineTime_Object = MibTableColumn
fs3GUserUplineTime = _Fs3GUserUplineTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 27),
    _Fs3GUserUplineTime_Type()
)
fs3GUserUplineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GUserUplineTime.setStatus("current")


class _Fs3GUserActiveTime_Type(Integer32):
    """Custom type fs3GUserActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Fs3GUserActiveTime_Type.__name__ = "Integer32"
_Fs3GUserActiveTime_Object = MibTableColumn
fs3GUserActiveTime = _Fs3GUserActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 28),
    _Fs3GUserActiveTime_Type()
)
fs3GUserActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GUserActiveTime.setStatus("current")


class _Fs3GSIMRoamingStatus_Type(Integer32):
    """Custom type fs3GSIMRoamingStatus based on Integer32"""
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


_Fs3GSIMRoamingStatus_Type.__name__ = "Integer32"
_Fs3GSIMRoamingStatus_Object = MibTableColumn
fs3GSIMRoamingStatus = _Fs3GSIMRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 29),
    _Fs3GSIMRoamingStatus_Type()
)
fs3GSIMRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GSIMRoamingStatus.setStatus("current")


class _Fs3GAcessBSCellID_Type(Integer32):
    """Custom type fs3GAcessBSCellID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fs3GAcessBSCellID_Type.__name__ = "Integer32"
_Fs3GAcessBSCellID_Object = MibTableColumn
fs3GAcessBSCellID = _Fs3GAcessBSCellID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 30),
    _Fs3GAcessBSCellID_Type()
)
fs3GAcessBSCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GAcessBSCellID.setStatus("current")


class _Fs3GAcessBSLAC_Type(Integer32):
    """Custom type fs3GAcessBSLAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fs3GAcessBSLAC_Type.__name__ = "Integer32"
_Fs3GAcessBSLAC_Object = MibTableColumn
fs3GAcessBSLAC = _Fs3GAcessBSLAC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 31),
    _Fs3GAcessBSLAC_Type()
)
fs3GAcessBSLAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GAcessBSLAC.setStatus("current")
_Fs3GAcessBSLONG_Type = Integer32
_Fs3GAcessBSLONG_Object = MibTableColumn
fs3GAcessBSLONG = _Fs3GAcessBSLONG_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 32),
    _Fs3GAcessBSLONG_Type()
)
fs3GAcessBSLONG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GAcessBSLONG.setStatus("current")
_Fs3GAcessBSLAT_Type = Integer32
_Fs3GAcessBSLAT_Object = MibTableColumn
fs3GAcessBSLAT = _Fs3GAcessBSLAT_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 33),
    _Fs3GAcessBSLAT_Type()
)
fs3GAcessBSLAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GAcessBSLAT.setStatus("current")
_Fs3GDialOnDemandIfIndex_Type = Integer32
_Fs3GDialOnDemandIfIndex_Object = MibTableColumn
fs3GDialOnDemandIfIndex = _Fs3GDialOnDemandIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 34),
    _Fs3GDialOnDemandIfIndex_Type()
)
fs3GDialOnDemandIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GDialOnDemandIfIndex.setStatus("current")


class _Fs3GTrafficPreventMode_Type(Integer32):
    """Custom type fs3GTrafficPreventMode based on Integer32"""
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


_Fs3GTrafficPreventMode_Type.__name__ = "Integer32"
_Fs3GTrafficPreventMode_Object = MibTableColumn
fs3GTrafficPreventMode = _Fs3GTrafficPreventMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 35),
    _Fs3GTrafficPreventMode_Type()
)
fs3GTrafficPreventMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GTrafficPreventMode.setStatus("current")
_Fs3GTrafficPreventIfIndex_Type = Integer32
_Fs3GTrafficPreventIfIndex_Object = MibTableColumn
fs3GTrafficPreventIfIndex = _Fs3GTrafficPreventIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 36),
    _Fs3GTrafficPreventIfIndex_Type()
)
fs3GTrafficPreventIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GTrafficPreventIfIndex.setStatus("current")
_Fs3GTrafficPreventListID_Type = Integer32
_Fs3GTrafficPreventListID_Object = MibTableColumn
fs3GTrafficPreventListID = _Fs3GTrafficPreventListID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 37),
    _Fs3GTrafficPreventListID_Type()
)
fs3GTrafficPreventListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GTrafficPreventListID.setStatus("current")
_Fs3GTrafficPreventListName_Type = DisplayString
_Fs3GTrafficPreventListName_Object = MibTableColumn
fs3GTrafficPreventListName = _Fs3GTrafficPreventListName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 38),
    _Fs3GTrafficPreventListName_Type()
)
fs3GTrafficPreventListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GTrafficPreventListName.setStatus("current")


class _Fs3GDeviceModemType_Type(Integer32):
    """Custom type fs3GDeviceModemType based on Integer32"""
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


_Fs3GDeviceModemType_Type.__name__ = "Integer32"
_Fs3GDeviceModemType_Object = MibTableColumn
fs3GDeviceModemType = _Fs3GDeviceModemType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 39),
    _Fs3GDeviceModemType_Type()
)
fs3GDeviceModemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GDeviceModemType.setStatus("current")


class _Fs3GTrafficTrapInterval_Type(Integer32):
    """Custom type fs3GTrafficTrapInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_Fs3GTrafficTrapInterval_Type.__name__ = "Integer32"
_Fs3GTrafficTrapInterval_Object = MibTableColumn
fs3GTrafficTrapInterval = _Fs3GTrafficTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 40),
    _Fs3GTrafficTrapInterval_Type()
)
fs3GTrafficTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fs3GTrafficTrapInterval.setStatus("current")


class _Fs3GRssiThreshold_Type(Integer32):
    """Custom type fs3GRssiThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Fs3GRssiThreshold_Type.__name__ = "Integer32"
_Fs3GRssiThreshold_Object = MibTableColumn
fs3GRssiThreshold = _Fs3GRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 41),
    _Fs3GRssiThreshold_Type()
)
fs3GRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fs3GRssiThreshold.setStatus("current")


class _Fs3GTrapFilterMode_Type(Integer32):
    """Custom type fs3GTrapFilterMode based on Integer32"""
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


_Fs3GTrapFilterMode_Type.__name__ = "Integer32"
_Fs3GTrapFilterMode_Object = MibTableColumn
fs3GTrapFilterMode = _Fs3GTrapFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 42),
    _Fs3GTrapFilterMode_Type()
)
fs3GTrapFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fs3GTrapFilterMode.setStatus("current")


class _Fs3GISPtimeout_Type(Integer32):
    """Custom type fs3GISPtimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 36000),
    )


_Fs3GISPtimeout_Type.__name__ = "Integer32"
_Fs3GISPtimeout_Object = MibTableColumn
fs3GISPtimeout = _Fs3GISPtimeout_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 43),
    _Fs3GISPtimeout_Type()
)
fs3GISPtimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fs3GISPtimeout.setStatus("current")


class _Fs3GEncrypt_type_Type(Integer32):
    """Custom type fs3GEncrypt_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              7)
        )
    )
    namedValues = NamedValues(
        *(("encrypt_none", 0),
          ("encrypt_temp", 7))
    )


_Fs3GEncrypt_type_Type.__name__ = "Integer32"
_Fs3GEncrypt_type_Object = MibTableColumn
fs3GEncrypt_type = _Fs3GEncrypt_type_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 44),
    _Fs3GEncrypt_type_Type()
)
fs3GEncrypt_type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fs3GEncrypt_type.setStatus("current")
_Fs3GPassword_Type = DisplayString
_Fs3GPassword_Object = MibTableColumn
fs3GPassword = _Fs3GPassword_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 45),
    _Fs3GPassword_Type()
)
fs3GPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fs3GPassword.setStatus("current")
_Fs3GNetworkISPName_Type = DisplayString
_Fs3GNetworkISPName_Object = MibTableColumn
fs3GNetworkISPName = _Fs3GNetworkISPName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 6, 1, 46),
    _Fs3GNetworkISPName_Type()
)
fs3GNetworkISPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs3GNetworkISPName.setStatus("current")
_Fs3GTrapNew_ObjectIdentity = ObjectIdentity
fs3GTrapNew = _Fs3GTrapNew_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 2)
)
_Fs3GNotificationsNew_ObjectIdentity = ObjectIdentity
fs3GNotificationsNew = _Fs3GNotificationsNew_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 2, 1)
)

# Managed Objects groups


# Notification objects

fs3GSignalThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 3, 1, 1)
)
fs3GSignalThreshold.setObjects(
      *(("FS-3G-MIB", "fs3GIPAddr"),
        ("FS-3G-MIB", "fs3GSignalStrength"),
        ("FS-3G-MIB", "fs3GSignalStrengthPercent"),
        ("FS-3G-MIB", "fs3GIMSI"))
)
if mibBuilder.loadTexts:
    fs3GSignalThreshold.setStatus(
        "current"
    )

fs3GUpLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 3, 1, 2)
)
fs3GUpLine.setObjects(
      *(("FS-3G-MIB", "fs3GIPAddr"),
        ("FS-3G-MIB", "fs3gUsername"),
        ("FS-3G-MIB", "fs3GIMSI"),
        ("FS-3G-MIB", "fs3GBackupInfo"),
        ("FS-3G-MIB", "fs3GSerialNumber"),
        ("FS-3G-MIB", "fs3GGatewayIPAddr"))
)
if mibBuilder.loadTexts:
    fs3GUpLine.setStatus(
        "current"
    )

fs3GDownLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 3, 1, 3)
)
fs3GDownLine.setObjects(
      *(("FS-3G-MIB", "fs3GLineDownCause"),
        ("FS-3G-MIB", "fs3GIPAddr"),
        ("FS-3G-MIB", "fs3gUsername"),
        ("FS-3G-MIB", "fs3GIMSI"))
)
if mibBuilder.loadTexts:
    fs3GDownLine.setStatus(
        "current"
    )

fs3GChangeAccessPoint = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 3, 1, 4)
)
fs3GChangeAccessPoint.setObjects(
      *(("FS-3G-MIB", "fs3GIPAddr"),
        ("FS-3G-MIB", "fs3GApn"),
        ("FS-3G-MIB", "fs3gUsername"),
        ("FS-3G-MIB", "fs3GIMSI"))
)
if mibBuilder.loadTexts:
    fs3GChangeAccessPoint.setStatus(
        "current"
    )

fs3GBackupIntfSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 3, 1, 5)
)
fs3GBackupIntfSwitch.setObjects(
      *(("FS-3G-MIB", "fs3GIPAddr"),
        ("FS-3G-MIB", "fs3gUsername"),
        ("FS-3G-MIB", "fs3GIMSI"),
        ("FS-3G-MIB", "fs3GSerialNumber"),
        ("FS-3G-MIB", "fs3GBackupIMSI"))
)
if mibBuilder.loadTexts:
    fs3GBackupIntfSwitch.setStatus(
        "current"
    )

fs3GBaseSationSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 3, 1, 6)
)
fs3GBaseSationSwitch.setObjects(
      *(("FS-3G-MIB", "fs3GISP"),
        ("FS-3G-MIB", "fs3GCellID"),
        ("FS-3G-MIB", "fs3GLAC"),
        ("FS-3G-MIB", "fs3GBSID"),
        ("FS-3G-MIB", "fs3GSID"),
        ("FS-3G-MIB", "fs3GNID"),
        ("FS-3G-MIB", "fs3GIMSI"),
        ("FS-3G-MIB", "fs3GPhoneNumber"))
)
if mibBuilder.loadTexts:
    fs3GBaseSationSwitch.setStatus(
        "current"
    )

fs3GTrafficInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 1, 3, 1, 7)
)
fs3GTrafficInformation.setObjects(
      *(("FS-3G-MIB", "fs3GIPAddr"),
        ("FS-3G-MIB", "fs3GIMSI"),
        ("FS-3G-MIB", "fs3GSerialNumber"),
        ("FS-3G-MIB", "fs3GInOctets"),
        ("FS-3G-MIB", "fs3GOutOctets"))
)
if mibBuilder.loadTexts:
    fs3GTrafficInformation.setStatus(
        "current"
    )

fs3GLineDetectedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 2, 1, 1)
)
fs3GLineDetectedNotification.setObjects(
      *(("FS-3G-MIB", "fs3GRouterSN"),
        ("FS-3G-MIB", "fs3GCardIMSI"),
        ("FS-3G-MIB", "fs3GIntfIPAddr"),
        ("FS-3G-MIB", "fs3GLineDetected"),
        ("FS-3G-MIB", "fs3GLineDetectedResult"),
        ("FS-3G-MIB", "fs3GLineDetectedMainCause"),
        ("FS-3G-MIB", "fs3GLineDetectedSubCause"),
        ("FS-3G-MIB", "fs3GDeviceBackupInfo"),
        ("FS-3G-MIB", "fs3GRssiStrength"),
        ("FS-3G-MIB", "fs3GDeviceBackupIMSI"))
)
if mibBuilder.loadTexts:
    fs3GLineDetectedNotification.setStatus(
        "current"
    )

fs3GUserUpLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 2, 1, 2)
)
fs3GUserUpLine.setObjects(
      *(("FS-3G-MIB", "fs3GRouterSlotNumber"),
        ("FS-3G-MIB", "fs3GCardIMSI"),
        ("FS-3G-MIB", "fs3GIntfIPAddr"),
        ("FS-3G-MIB", "fs3GTrafficPreventListName"),
        ("FS-3G-MIB", "fs3GTrafficPreventListID"),
        ("FS-3G-MIB", "fs3GTrafficPreventIfIndex"),
        ("FS-3G-MIB", "fs3GTrafficPreventMode"),
        ("FS-3G-MIB", "fs3GPppUsername"),
        ("FS-3G-MIB", "fs3GRouterSN"),
        ("FS-3G-MIB", "fs3GCardPhoneNumber"),
        ("FS-3G-MIB", "fs3GDailMode"),
        ("FS-3G-MIB", "fs3GDialOnDemandIfIndex"),
        ("FS-3G-MIB", "fs3GDeviceModemType"))
)
if mibBuilder.loadTexts:
    fs3GUserUpLine.setStatus(
        "current"
    )

fs3GUserDownLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 2, 1, 3)
)
fs3GUserDownLine.setObjects(
      *(("FS-3G-MIB", "fs3GRouterSlotNumber"),
        ("FS-3G-MIB", "fs3GCardIMSI"),
        ("FS-3G-MIB", "fs3GIntfIPAddr"),
        ("FS-3G-MIB", "fs3GTrafficPreventListName"),
        ("FS-3G-MIB", "fs3GTrafficPreventListID"),
        ("FS-3G-MIB", "fs3GTrafficPreventIfIndex"),
        ("FS-3G-MIB", "fs3GTrafficPreventMode"),
        ("FS-3G-MIB", "fs3GPppUsername"),
        ("FS-3G-MIB", "fs3GRouterSN"),
        ("FS-3G-MIB", "fs3GCardPhoneNumber"),
        ("FS-3G-MIB", "fs3GDailMode"),
        ("FS-3G-MIB", "fs3GDialOnDemandIfIndex"),
        ("FS-3G-MIB", "fs3GDeviceModemType"))
)
if mibBuilder.loadTexts:
    fs3GUserDownLine.setStatus(
        "current"
    )

fs3GRssiNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 2, 1, 4)
)
fs3GRssiNotification.setObjects(
      *(("FS-3G-MIB", "fs3GRouterSlotNumber"),
        ("FS-3G-MIB", "fs3GCardIMSI"),
        ("FS-3G-MIB", "fs3GRouterSN"),
        ("FS-3G-MIB", "fs3GIntfIPAddr"),
        ("FS-3G-MIB", "fs3GRssiStrengthPercent"),
        ("FS-3G-MIB", "fs3GRssiStrength"),
        ("FS-3G-MIB", "fs3GDeviceModemType"))
)
if mibBuilder.loadTexts:
    fs3GRssiNotification.setStatus(
        "current"
    )

fs3GTrafficInfoNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 2, 1, 5)
)
fs3GTrafficInfoNotification.setObjects(
      *(("FS-3G-MIB", "fs3GRouterSlotNumber"),
        ("FS-3G-MIB", "fs3GCardIMSI"),
        ("FS-3G-MIB", "fs3GRouterSN"),
        ("FS-3G-MIB", "fs3GIntfIPAddr"),
        ("FS-3G-MIB", "fs3GOutOctets"),
        ("FS-3G-MIB", "fs3GInOctets"),
        ("FS-3G-MIB", "fs3GDeviceModemType"),
        ("FS-3G-MIB", "fs3GLineCardType"),
        ("FS-3G-MIB", "fs3GModemIMEI"),
        ("FS-3G-MIB", "fs3GCardPhoneNumber"),
        ("FS-3G-MIB", "fs3GDeviceBackupInfo"),
        ("FS-3G-MIB", "fs3GRssiStrength"),
        ("FS-3G-MIB", "fs3GRssiStrengthPercent"),
        ("FS-3G-MIB", "fs3GNetworkISPMode"),
        ("FS-3G-MIB", "fs3GNetworkSysMode"),
        ("FS-3G-MIB", "fs3GSIMCardStatus"),
        ("FS-3G-MIB", "fs3GDailMode"),
        ("FS-3G-MIB", "fs3GPppUsername"),
        ("FS-3G-MIB", "fs3GUserActiveTime"),
        ("FS-3G-MIB", "fs3GAcessBSCellID"),
        ("FS-3G-MIB", "fs3GAcessBSLAC"),
        ("FS-3G-MIB", "fs3GAcessBSLONG"),
        ("FS-3G-MIB", "fs3GAcessBSLAT"),
        ("FS-3G-MIB", "fs3GInSpeed"),
        ("FS-3G-MIB", "fs3GOutSpeed"),
        ("FS-3G-MIB", "fs3G2ifIndex"),
        ("FS-3G-MIB", "fs3GTrafficTrapInterval"),
        ("FS-3G-MIB", "fs3GRssiThreshold"),
        ("FS-3G-MIB", "fs3GTrapFilterMode"),
        ("FS-3G-MIB", "fs3GISPtimeout"),
        ("FS-3G-MIB", "fs3GNetworkISPName"))
)
if mibBuilder.loadTexts:
    fs3GTrafficInfoNotification.setStatus(
        "current"
    )

fs3GBackupMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 2, 1, 6)
)
fs3GBackupMaster.setObjects(
      *(("FS-3G-MIB", "fs3GRouterSlotNumber"),
        ("FS-3G-MIB", "fs3GCardIMSI"),
        ("FS-3G-MIB", "fs3GIntfIPAddr"),
        ("FS-3G-MIB", "fs3GTrafficPreventListName"),
        ("FS-3G-MIB", "fs3GTrafficPreventListID"),
        ("FS-3G-MIB", "fs3GTrafficPreventIfIndex"),
        ("FS-3G-MIB", "fs3GTrafficPreventMode"),
        ("FS-3G-MIB", "fs3GPppUsername"),
        ("FS-3G-MIB", "fs3GRouterSN"),
        ("FS-3G-MIB", "fs3GCardPhoneNumber"),
        ("FS-3G-MIB", "fs3GDailMode"),
        ("FS-3G-MIB", "fs3GDialOnDemandIfIndex"),
        ("FS-3G-MIB", "fs3GDeviceModemType"))
)
if mibBuilder.loadTexts:
    fs3GBackupMaster.setStatus(
        "current"
    )

fs3GBackupSlave = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 95, 2, 1, 7)
)
fs3GBackupSlave.setObjects(
      *(("FS-3G-MIB", "fs3GRouterSlotNumber"),
        ("FS-3G-MIB", "fs3GCardIMSI"),
        ("FS-3G-MIB", "fs3GIntfIPAddr"),
        ("FS-3G-MIB", "fs3GTrafficPreventListName"),
        ("FS-3G-MIB", "fs3GTrafficPreventListID"),
        ("FS-3G-MIB", "fs3GTrafficPreventIfIndex"),
        ("FS-3G-MIB", "fs3GTrafficPreventMode"),
        ("FS-3G-MIB", "fs3GPppUsername"),
        ("FS-3G-MIB", "fs3GRouterSN"),
        ("FS-3G-MIB", "fs3GCardPhoneNumber"),
        ("FS-3G-MIB", "fs3GDailMode"),
        ("FS-3G-MIB", "fs3GDialOnDemandIfIndex"),
        ("FS-3G-MIB", "fs3GDeviceModemType"))
)
if mibBuilder.loadTexts:
    fs3GBackupSlave.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-3G-MIB",
    **{"fs3GMonitor": fs3GMonitor,
       "fs3GObjects": fs3GObjects,
       "fs3GTable": fs3GTable,
       "fs3GEntry": fs3GEntry,
       "fs3gUsername": fs3gUsername,
       "fs3GOnlineStatus": fs3GOnlineStatus,
       "fs3GIMEI": fs3GIMEI,
       "fs3GIPAddrType": fs3GIPAddrType,
       "fs3GIPAddr": fs3GIPAddr,
       "fs3GUplineTime": fs3GUplineTime,
       "fs3GActiveTime": fs3GActiveTime,
       "fs3GSignalStrength": fs3GSignalStrength,
       "fs3GISP": fs3GISP,
       "fs3GSysMode": fs3GSysMode,
       "fs3GServiceStatus": fs3GServiceStatus,
       "fs3GRoamingStatus": fs3GRoamingStatus,
       "fs3GDomain": fs3GDomain,
       "fs3GSIMStatus": fs3GSIMStatus,
       "fs3GSignalStrengthPercent": fs3GSignalStrengthPercent,
       "fs3GApn": fs3GApn,
       "fs3GCellID": fs3GCellID,
       "fs3GLAC": fs3GLAC,
       "fs3GBSID": fs3GBSID,
       "fs3GNID": fs3GNID,
       "fs3GSID": fs3GSID,
       "fs3GIMSI": fs3GIMSI,
       "fs3GESN": fs3GESN,
       "fs3GPhoneNumber": fs3GPhoneNumber,
       "fs3GifIndex": fs3GifIndex,
       "fs3GBSLONG": fs3GBSLONG,
       "fs3GBSLAT": fs3GBSLAT,
       "fs3GBackupInfo": fs3GBackupInfo,
       "fs3GSerialNumber": fs3GSerialNumber,
       "fs3GBackupIMSI": fs3GBackupIMSI,
       "fs3GGatewayIPAddr": fs3GGatewayIPAddr,
       "fs3GLineDownCause": fs3GLineDownCause,
       "fs3GModemType": fs3GModemType,
       "fs3GStatTable": fs3GStatTable,
       "fs3GStatEntry": fs3GStatEntry,
       "fs3GInOctets": fs3GInOctets,
       "fs3GOutOctets": fs3GOutOctets,
       "fs3GInSpeed": fs3GInSpeed,
       "fs3GOutSpeed": fs3GOutSpeed,
       "fs3G2IMSI": fs3G2IMSI,
       "fs3G2ifIndex": fs3G2ifIndex,
       "fs3GTrap": fs3GTrap,
       "fs3GNotifications": fs3GNotifications,
       "fs3GSignalThreshold": fs3GSignalThreshold,
       "fs3GUpLine": fs3GUpLine,
       "fs3GDownLine": fs3GDownLine,
       "fs3GChangeAccessPoint": fs3GChangeAccessPoint,
       "fs3GBackupIntfSwitch": fs3GBackupIntfSwitch,
       "fs3GBaseSationSwitch": fs3GBaseSationSwitch,
       "fs3GTrafficInformation": fs3GTrafficInformation,
       "fs3GBsNumber": fs3GBsNumber,
       "fs3GBsTable": fs3GBsTable,
       "fs3GBsEntry": fs3GBsEntry,
       "fs3GBsSN": fs3GBsSN,
       "fs3GBsISP": fs3GBsISP,
       "fs3GBsMode": fs3GBsMode,
       "fs3GBsIMSI": fs3GBsIMSI,
       "fs3GBsLAC": fs3GBsLAC,
       "fs3GBsCellID": fs3GBsCellID,
       "fs3GBsBSID": fs3GBsBSID,
       "fs3GBsSID": fs3GBsSID,
       "fs3GBsNID": fs3GBsNID,
       "fs3GBsRssi": fs3GBsRssi,
       "fs3GBsBSLONG": fs3GBsBSLONG,
       "fs3GBsBSLAT": fs3GBsBSLAT,
       "fs3GDeviceManagementTable": fs3GDeviceManagementTable,
       "fs3GDeviceManagementEntry": fs3GDeviceManagementEntry,
       "fs3GRouterType": fs3GRouterType,
       "fs3GRouterSN": fs3GRouterSN,
       "fs3GRouterSlotNumber": fs3GRouterSlotNumber,
       "fs3GLineCardType": fs3GLineCardType,
       "fs3GCardIMSI": fs3GCardIMSI,
       "fs3GModemIMEI": fs3GModemIMEI,
       "fs3GIntfIPAddr": fs3GIntfIPAddr,
       "fs3GCardPhoneNumber": fs3GCardPhoneNumber,
       "fs3GLineDetected": fs3GLineDetected,
       "fs3GLineDetectedResult": fs3GLineDetectedResult,
       "fs3GLineDetectedMainCause": fs3GLineDetectedMainCause,
       "fs3GLineDetectedSubCause": fs3GLineDetectedSubCause,
       "fs3GDeviceBackupInfo": fs3GDeviceBackupInfo,
       "fs3GRssiStrength": fs3GRssiStrength,
       "fs3GRssiStrengthPercent": fs3GRssiStrengthPercent,
       "fs3GNetworkISPMode": fs3GNetworkISPMode,
       "fs3GNetworkSysMode": fs3GNetworkSysMode,
       "fs3GNetworkServiceStatus": fs3GNetworkServiceStatus,
       "fs3GSIMCardStatus": fs3GSIMCardStatus,
       "fs3GDailMode": fs3GDailMode,
       "fs3GDeviceBackupIMSI": fs3GDeviceBackupIMSI,
       "fs3GLineDetectedMode": fs3GLineDetectedMode,
       "fs3GPppUsername": fs3GPppUsername,
       "fs3GUserApn": fs3GUserApn,
       "fs3GModemOnlineStatus": fs3GModemOnlineStatus,
       "fs3GIntfIPAddrType": fs3GIntfIPAddrType,
       "fs3GUserUplineTime": fs3GUserUplineTime,
       "fs3GUserActiveTime": fs3GUserActiveTime,
       "fs3GSIMRoamingStatus": fs3GSIMRoamingStatus,
       "fs3GAcessBSCellID": fs3GAcessBSCellID,
       "fs3GAcessBSLAC": fs3GAcessBSLAC,
       "fs3GAcessBSLONG": fs3GAcessBSLONG,
       "fs3GAcessBSLAT": fs3GAcessBSLAT,
       "fs3GDialOnDemandIfIndex": fs3GDialOnDemandIfIndex,
       "fs3GTrafficPreventMode": fs3GTrafficPreventMode,
       "fs3GTrafficPreventIfIndex": fs3GTrafficPreventIfIndex,
       "fs3GTrafficPreventListID": fs3GTrafficPreventListID,
       "fs3GTrafficPreventListName": fs3GTrafficPreventListName,
       "fs3GDeviceModemType": fs3GDeviceModemType,
       "fs3GTrafficTrapInterval": fs3GTrafficTrapInterval,
       "fs3GRssiThreshold": fs3GRssiThreshold,
       "fs3GTrapFilterMode": fs3GTrapFilterMode,
       "fs3GISPtimeout": fs3GISPtimeout,
       "fs3GEncrypt_type": fs3GEncrypt_type,
       "fs3GPassword": fs3GPassword,
       "fs3GNetworkISPName": fs3GNetworkISPName,
       "fs3GTrapNew": fs3GTrapNew,
       "fs3GNotificationsNew": fs3GNotificationsNew,
       "fs3GLineDetectedNotification": fs3GLineDetectedNotification,
       "fs3GUserUpLine": fs3GUserUpLine,
       "fs3GUserDownLine": fs3GUserDownLine,
       "fs3GRssiNotification": fs3GRssiNotification,
       "fs3GTrafficInfoNotification": fs3GTrafficInfoNotification,
       "fs3GBackupMaster": fs3GBackupMaster,
       "fs3GBackupSlave": fs3GBackupSlave}
)
