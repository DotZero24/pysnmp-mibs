# SNMP MIB module (FS-4G-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-4G-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:21 2025
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

fs4GMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127)
)
if mibBuilder.loadTexts:
    fs4GMonitor.setRevisions(
        ("2014-03-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fs4GObjects_ObjectIdentity = ObjectIdentity
fs4GObjects = _Fs4GObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1)
)
_Fs4GTable_Object = MibTable
fs4GTable = _Fs4GTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1)
)
if mibBuilder.loadTexts:
    fs4GTable.setStatus("current")
_Fs4GEntry_Object = MibTableRow
fs4GEntry = _Fs4GEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1)
)
fs4GEntry.setIndexNames(
    (0, "FS-4G-MIB", "fs4GRouterSlotNumber"),
)
if mibBuilder.loadTexts:
    fs4GEntry.setStatus("current")
_Fs4GUsername_Type = DisplayString
_Fs4GUsername_Object = MibTableColumn
fs4GUsername = _Fs4GUsername_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 1),
    _Fs4GUsername_Type()
)
fs4GUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GUsername.setStatus("current")
_Fs4GApn_Type = DisplayString
_Fs4GApn_Object = MibTableColumn
fs4GApn = _Fs4GApn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 2),
    _Fs4GApn_Type()
)
fs4GApn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GApn.setStatus("current")


class _Fs4GOnlineStatus_Type(Integer32):
    """Custom type fs4GOnlineStatus based on Integer32"""
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


_Fs4GOnlineStatus_Type.__name__ = "Integer32"
_Fs4GOnlineStatus_Object = MibTableColumn
fs4GOnlineStatus = _Fs4GOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 3),
    _Fs4GOnlineStatus_Type()
)
fs4GOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GOnlineStatus.setStatus("current")
_Fs4GIMEI_Type = DisplayString
_Fs4GIMEI_Object = MibTableColumn
fs4GIMEI = _Fs4GIMEI_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 4),
    _Fs4GIMEI_Type()
)
fs4GIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GIMEI.setStatus("current")


class _Fs4GIPAddrType_Type(Integer32):
    """Custom type fs4GIPAddrType based on Integer32"""
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


_Fs4GIPAddrType_Type.__name__ = "Integer32"
_Fs4GIPAddrType_Object = MibTableColumn
fs4GIPAddrType = _Fs4GIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 5),
    _Fs4GIPAddrType_Type()
)
fs4GIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GIPAddrType.setStatus("current")
_Fs4GIPAddr_Type = IpAddress
_Fs4GIPAddr_Object = MibTableColumn
fs4GIPAddr = _Fs4GIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 6),
    _Fs4GIPAddr_Type()
)
fs4GIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GIPAddr.setStatus("current")
_Fs4GUplineTime_Type = TimeStamp
_Fs4GUplineTime_Object = MibTableColumn
fs4GUplineTime = _Fs4GUplineTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 7),
    _Fs4GUplineTime_Type()
)
fs4GUplineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GUplineTime.setStatus("current")


class _Fs4GActiveTime_Type(Integer32):
    """Custom type fs4GActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Fs4GActiveTime_Type.__name__ = "Integer32"
_Fs4GActiveTime_Object = MibTableColumn
fs4GActiveTime = _Fs4GActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 8),
    _Fs4GActiveTime_Type()
)
fs4GActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GActiveTime.setStatus("current")


class _Fs4GRSRP_Type(Integer32):
    """Custom type fs4GRSRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Fs4GRSRP_Type.__name__ = "Integer32"
_Fs4GRSRP_Object = MibTableColumn
fs4GRSRP = _Fs4GRSRP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 9),
    _Fs4GRSRP_Type()
)
fs4GRSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GRSRP.setStatus("current")


class _Fs4GSignalStrengthPercent_Type(Integer32):
    """Custom type fs4GSignalStrengthPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fs4GSignalStrengthPercent_Type.__name__ = "Integer32"
_Fs4GSignalStrengthPercent_Object = MibTableColumn
fs4GSignalStrengthPercent = _Fs4GSignalStrengthPercent_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 10),
    _Fs4GSignalStrengthPercent_Type()
)
fs4GSignalStrengthPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GSignalStrengthPercent.setStatus("current")


class _Fs4GISP_Type(Integer32):
    """Custom type fs4GISP based on Integer32"""
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
        *(("unknow", 0),
          ("chinaUnicom", 1),
          ("chinaTelecom", 2),
          ("chinaMobile", 3))
    )


_Fs4GISP_Type.__name__ = "Integer32"
_Fs4GISP_Object = MibTableColumn
fs4GISP = _Fs4GISP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 11),
    _Fs4GISP_Type()
)
fs4GISP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GISP.setStatus("current")


class _Fs4GSysMode_Type(Integer32):
    """Custom type fs4GSysMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              5,
              15,
              17)
        )
    )
    namedValues = NamedValues(
        *(("no-service", 0),
          ("gsm-gprs", 3),
          ("wcdma", 5),
          ("td-scdma", 15),
          ("lte", 17))
    )


_Fs4GSysMode_Type.__name__ = "Integer32"
_Fs4GSysMode_Object = MibTableColumn
fs4GSysMode = _Fs4GSysMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 12),
    _Fs4GSysMode_Type()
)
fs4GSysMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GSysMode.setStatus("current")


class _Fs4GServiceStatus_Type(Integer32):
    """Custom type fs4GServiceStatus based on Integer32"""
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


_Fs4GServiceStatus_Type.__name__ = "Integer32"
_Fs4GServiceStatus_Object = MibTableColumn
fs4GServiceStatus = _Fs4GServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 13),
    _Fs4GServiceStatus_Type()
)
fs4GServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GServiceStatus.setStatus("current")


class _Fs4GRoamingStatus_Type(Integer32):
    """Custom type fs4GRoamingStatus based on Integer32"""
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


_Fs4GRoamingStatus_Type.__name__ = "Integer32"
_Fs4GRoamingStatus_Object = MibTableColumn
fs4GRoamingStatus = _Fs4GRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 14),
    _Fs4GRoamingStatus_Type()
)
fs4GRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GRoamingStatus.setStatus("current")


class _Fs4GDomain_Type(Integer32):
    """Custom type fs4GDomain based on Integer32"""
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
          ("onlyCS", 1),
          ("onlyPS", 2),
          ("pSCS", 3),
          ("ePS", 4))
    )


_Fs4GDomain_Type.__name__ = "Integer32"
_Fs4GDomain_Object = MibTableColumn
fs4GDomain = _Fs4GDomain_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 15),
    _Fs4GDomain_Type()
)
fs4GDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GDomain.setStatus("current")


class _Fs4GSIMStatus_Type(Integer32):
    """Custom type fs4GSIMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("invalidUsimCard", 0),
          ("validUsimCard", 1),
          ("noUsimCard", 255))
    )


_Fs4GSIMStatus_Type.__name__ = "Integer32"
_Fs4GSIMStatus_Object = MibTableColumn
fs4GSIMStatus = _Fs4GSIMStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 16),
    _Fs4GSIMStatus_Type()
)
fs4GSIMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GSIMStatus.setStatus("current")


class _Fs4GCellID_Type(Integer32):
    """Custom type fs4GCellID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fs4GCellID_Type.__name__ = "Integer32"
_Fs4GCellID_Object = MibTableColumn
fs4GCellID = _Fs4GCellID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 17),
    _Fs4GCellID_Type()
)
fs4GCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GCellID.setStatus("current")


class _Fs4GLAC_Type(Integer32):
    """Custom type fs4GLAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Fs4GLAC_Type.__name__ = "Integer32"
_Fs4GLAC_Object = MibTableColumn
fs4GLAC = _Fs4GLAC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 18),
    _Fs4GLAC_Type()
)
fs4GLAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GLAC.setStatus("current")
_Fs4GIMSI_Type = DisplayString
_Fs4GIMSI_Object = MibTableColumn
fs4GIMSI = _Fs4GIMSI_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 19),
    _Fs4GIMSI_Type()
)
fs4GIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GIMSI.setStatus("current")
_Fs4GPhoneNumber_Type = DisplayString
_Fs4GPhoneNumber_Object = MibTableColumn
fs4GPhoneNumber = _Fs4GPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 20),
    _Fs4GPhoneNumber_Type()
)
fs4GPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GPhoneNumber.setStatus("current")
_Fs4GifIndex_Type = Integer32
_Fs4GifIndex_Object = MibTableColumn
fs4GifIndex = _Fs4GifIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 21),
    _Fs4GifIndex_Type()
)
fs4GifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GifIndex.setStatus("current")
_Fs4GInOctets_Type = Counter64
_Fs4GInOctets_Object = MibTableColumn
fs4GInOctets = _Fs4GInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 22),
    _Fs4GInOctets_Type()
)
fs4GInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GInOctets.setStatus("current")
_Fs4GOutOctets_Type = Counter64
_Fs4GOutOctets_Object = MibTableColumn
fs4GOutOctets = _Fs4GOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 23),
    _Fs4GOutOctets_Type()
)
fs4GOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GOutOctets.setStatus("current")
_Fs4GInSpeed_Type = Counter64
_Fs4GInSpeed_Object = MibTableColumn
fs4GInSpeed = _Fs4GInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 24),
    _Fs4GInSpeed_Type()
)
fs4GInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GInSpeed.setStatus("current")
_Fs4GOutSpeed_Type = Counter64
_Fs4GOutSpeed_Object = MibTableColumn
fs4GOutSpeed = _Fs4GOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 25),
    _Fs4GOutSpeed_Type()
)
fs4GOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GOutSpeed.setStatus("current")
_Fs4GBSLONG_Type = Integer32
_Fs4GBSLONG_Object = MibTableColumn
fs4GBSLONG = _Fs4GBSLONG_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 26),
    _Fs4GBSLONG_Type()
)
fs4GBSLONG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GBSLONG.setStatus("current")
_Fs4GBSLAT_Type = Integer32
_Fs4GBSLAT_Object = MibTableColumn
fs4GBSLAT = _Fs4GBSLAT_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 27),
    _Fs4GBSLAT_Type()
)
fs4GBSLAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GBSLAT.setStatus("current")
_Fs4GRouterType_Type = DisplayString
_Fs4GRouterType_Object = MibTableColumn
fs4GRouterType = _Fs4GRouterType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 28),
    _Fs4GRouterType_Type()
)
fs4GRouterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GRouterType.setStatus("current")
_Fs4GRouterSN_Type = DisplayString
_Fs4GRouterSN_Object = MibTableColumn
fs4GRouterSN = _Fs4GRouterSN_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 29),
    _Fs4GRouterSN_Type()
)
fs4GRouterSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GRouterSN.setStatus("current")
_Fs4GRouterSlotNumber_Type = DisplayString
_Fs4GRouterSlotNumber_Object = MibTableColumn
fs4GRouterSlotNumber = _Fs4GRouterSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 30),
    _Fs4GRouterSlotNumber_Type()
)
fs4GRouterSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GRouterSlotNumber.setStatus("current")
_Fs4GLineCardType_Type = DisplayString
_Fs4GLineCardType_Object = MibTableColumn
fs4GLineCardType = _Fs4GLineCardType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 31),
    _Fs4GLineCardType_Type()
)
fs4GLineCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GLineCardType.setStatus("current")


class _Fs4GDialdMode_Type(Integer32):
    """Custom type fs4GDialdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto-dial", 0),
          ("dial-on-demand", 1))
    )


_Fs4GDialdMode_Type.__name__ = "Integer32"
_Fs4GDialdMode_Object = MibTableColumn
fs4GDialdMode = _Fs4GDialdMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 32),
    _Fs4GDialdMode_Type()
)
fs4GDialdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GDialdMode.setStatus("current")
_Fs4GDialOnDemandIfIndex_Type = Integer32
_Fs4GDialOnDemandIfIndex_Object = MibTableColumn
fs4GDialOnDemandIfIndex = _Fs4GDialOnDemandIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 33),
    _Fs4GDialOnDemandIfIndex_Type()
)
fs4GDialOnDemandIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GDialOnDemandIfIndex.setStatus("current")


class _Fs4GTrafficPreventMode_Type(Integer32):
    """Custom type fs4GTrafficPreventMode based on Integer32"""
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


_Fs4GTrafficPreventMode_Type.__name__ = "Integer32"
_Fs4GTrafficPreventMode_Object = MibTableColumn
fs4GTrafficPreventMode = _Fs4GTrafficPreventMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 34),
    _Fs4GTrafficPreventMode_Type()
)
fs4GTrafficPreventMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GTrafficPreventMode.setStatus("current")
_Fs4GTrafficPreventIfIndex_Type = Integer32
_Fs4GTrafficPreventIfIndex_Object = MibTableColumn
fs4GTrafficPreventIfIndex = _Fs4GTrafficPreventIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 35),
    _Fs4GTrafficPreventIfIndex_Type()
)
fs4GTrafficPreventIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GTrafficPreventIfIndex.setStatus("current")
_Fs4GTrafficPreventListID_Type = Integer32
_Fs4GTrafficPreventListID_Object = MibTableColumn
fs4GTrafficPreventListID = _Fs4GTrafficPreventListID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 36),
    _Fs4GTrafficPreventListID_Type()
)
fs4GTrafficPreventListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GTrafficPreventListID.setStatus("current")
_Fs4GTrafficPreventListName_Type = DisplayString
_Fs4GTrafficPreventListName_Object = MibTableColumn
fs4GTrafficPreventListName = _Fs4GTrafficPreventListName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 1, 1, 1, 37),
    _Fs4GTrafficPreventListName_Type()
)
fs4GTrafficPreventListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fs4GTrafficPreventListName.setStatus("current")
_Fs4GTrap_ObjectIdentity = ObjectIdentity
fs4GTrap = _Fs4GTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 2)
)
_Fs4GNotifications_ObjectIdentity = ObjectIdentity
fs4GNotifications = _Fs4GNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 2, 1)
)

# Managed Objects groups


# Notification objects

fs4GUpLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 2, 1, 1)
)
fs4GUpLine.setObjects(
      *(("FS-4G-MIB", "fs4GRouterSlotNumber"),
        ("FS-4G-MIB", "fs4GIMSI"),
        ("FS-4G-MIB", "fs4GUsername"),
        ("FS-4G-MIB", "fs4GRouterSN"),
        ("FS-4G-MIB", "fs4GPhoneNumber"),
        ("FS-4G-MIB", "fs4GDialdMode"),
        ("FS-4G-MIB", "fs4GDialOnDemandIfIndex"),
        ("FS-4G-MIB", "fs4GTrafficPreventMode"),
        ("FS-4G-MIB", "fs4GTrafficPreventIfIndex"),
        ("FS-4G-MIB", "fs4GIPAddr"),
        ("FS-4G-MIB", "fs4GTrafficPreventListID"),
        ("FS-4G-MIB", "fs4GTrafficPreventListName"))
)
if mibBuilder.loadTexts:
    fs4GUpLine.setStatus(
        "current"
    )

fs4GDownLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 2, 1, 2)
)
fs4GDownLine.setObjects(
      *(("FS-4G-MIB", "fs4GRouterSlotNumber"),
        ("FS-4G-MIB", "fs4GIMSI"),
        ("FS-4G-MIB", "fs4GUsername"),
        ("FS-4G-MIB", "fs4GRouterSN"),
        ("FS-4G-MIB", "fs4GPhoneNumber"),
        ("FS-4G-MIB", "fs4GDialdMode"),
        ("FS-4G-MIB", "fs4GDialOnDemandIfIndex"),
        ("FS-4G-MIB", "fs4GTrafficPreventMode"),
        ("FS-4G-MIB", "fs4GTrafficPreventIfIndex"),
        ("FS-4G-MIB", "fs4GIPAddr"),
        ("FS-4G-MIB", "fs4GTrafficPreventListID"),
        ("FS-4G-MIB", "fs4GTrafficPreventListName"))
)
if mibBuilder.loadTexts:
    fs4GDownLine.setStatus(
        "current"
    )

fs4GSignalThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 2, 1, 3)
)
fs4GSignalThreshold.setObjects(
      *(("FS-4G-MIB", "fs4GRouterSlotNumber"),
        ("FS-4G-MIB", "fs4GIMSI"),
        ("FS-4G-MIB", "fs4GRSRP"),
        ("FS-4G-MIB", "fs4GSignalStrengthPercent"))
)
if mibBuilder.loadTexts:
    fs4GSignalThreshold.setStatus(
        "current"
    )

fs4GTrafficInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 2, 1, 4)
)
fs4GTrafficInformation.setObjects(
      *(("FS-4G-MIB", "fs4GRouterSlotNumber"),
        ("FS-4G-MIB", "fs4GIMSI"),
        ("FS-4G-MIB", "fs4GInOctets"),
        ("FS-4G-MIB", "fs4GOutOctets"))
)
if mibBuilder.loadTexts:
    fs4GTrafficInformation.setStatus(
        "current"
    )

fs4GBackupMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 2, 1, 5)
)
fs4GBackupMaster.setObjects(
      *(("FS-4G-MIB", "fs4GRouterSlotNumber"),
        ("FS-4G-MIB", "fs4GIMSI"),
        ("FS-4G-MIB", "fs4GUsername"),
        ("FS-4G-MIB", "fs4GRouterSN"),
        ("FS-4G-MIB", "fs4GPhoneNumber"),
        ("FS-4G-MIB", "fs4GDialdMode"),
        ("FS-4G-MIB", "fs4GDialOnDemandIfIndex"),
        ("FS-4G-MIB", "fs4GTrafficPreventMode"),
        ("FS-4G-MIB", "fs4GTrafficPreventIfIndex"),
        ("FS-4G-MIB", "fs4GIPAddr"),
        ("FS-4G-MIB", "fs4GTrafficPreventListID"),
        ("FS-4G-MIB", "fs4GTrafficPreventListName"))
)
if mibBuilder.loadTexts:
    fs4GBackupMaster.setStatus(
        "current"
    )

fs4GBackupSlave = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 127, 2, 1, 6)
)
fs4GBackupSlave.setObjects(
      *(("FS-4G-MIB", "fs4GRouterSlotNumber"),
        ("FS-4G-MIB", "fs4GIMSI"),
        ("FS-4G-MIB", "fs4GUsername"),
        ("FS-4G-MIB", "fs4GRouterSN"),
        ("FS-4G-MIB", "fs4GPhoneNumber"),
        ("FS-4G-MIB", "fs4GDialdMode"),
        ("FS-4G-MIB", "fs4GDialOnDemandIfIndex"),
        ("FS-4G-MIB", "fs4GTrafficPreventMode"),
        ("FS-4G-MIB", "fs4GTrafficPreventIfIndex"),
        ("FS-4G-MIB", "fs4GIPAddr"),
        ("FS-4G-MIB", "fs4GTrafficPreventListID"),
        ("FS-4G-MIB", "fs4GTrafficPreventListName"))
)
if mibBuilder.loadTexts:
    fs4GBackupSlave.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-4G-MIB",
    **{"fs4GMonitor": fs4GMonitor,
       "fs4GObjects": fs4GObjects,
       "fs4GTable": fs4GTable,
       "fs4GEntry": fs4GEntry,
       "fs4GUsername": fs4GUsername,
       "fs4GApn": fs4GApn,
       "fs4GOnlineStatus": fs4GOnlineStatus,
       "fs4GIMEI": fs4GIMEI,
       "fs4GIPAddrType": fs4GIPAddrType,
       "fs4GIPAddr": fs4GIPAddr,
       "fs4GUplineTime": fs4GUplineTime,
       "fs4GActiveTime": fs4GActiveTime,
       "fs4GRSRP": fs4GRSRP,
       "fs4GSignalStrengthPercent": fs4GSignalStrengthPercent,
       "fs4GISP": fs4GISP,
       "fs4GSysMode": fs4GSysMode,
       "fs4GServiceStatus": fs4GServiceStatus,
       "fs4GRoamingStatus": fs4GRoamingStatus,
       "fs4GDomain": fs4GDomain,
       "fs4GSIMStatus": fs4GSIMStatus,
       "fs4GCellID": fs4GCellID,
       "fs4GLAC": fs4GLAC,
       "fs4GIMSI": fs4GIMSI,
       "fs4GPhoneNumber": fs4GPhoneNumber,
       "fs4GifIndex": fs4GifIndex,
       "fs4GInOctets": fs4GInOctets,
       "fs4GOutOctets": fs4GOutOctets,
       "fs4GInSpeed": fs4GInSpeed,
       "fs4GOutSpeed": fs4GOutSpeed,
       "fs4GBSLONG": fs4GBSLONG,
       "fs4GBSLAT": fs4GBSLAT,
       "fs4GRouterType": fs4GRouterType,
       "fs4GRouterSN": fs4GRouterSN,
       "fs4GRouterSlotNumber": fs4GRouterSlotNumber,
       "fs4GLineCardType": fs4GLineCardType,
       "fs4GDialdMode": fs4GDialdMode,
       "fs4GDialOnDemandIfIndex": fs4GDialOnDemandIfIndex,
       "fs4GTrafficPreventMode": fs4GTrafficPreventMode,
       "fs4GTrafficPreventIfIndex": fs4GTrafficPreventIfIndex,
       "fs4GTrafficPreventListID": fs4GTrafficPreventListID,
       "fs4GTrafficPreventListName": fs4GTrafficPreventListName,
       "fs4GTrap": fs4GTrap,
       "fs4GNotifications": fs4GNotifications,
       "fs4GUpLine": fs4GUpLine,
       "fs4GDownLine": fs4GDownLine,
       "fs4GSignalThreshold": fs4GSignalThreshold,
       "fs4GTrafficInformation": fs4GTrafficInformation,
       "fs4GBackupMaster": fs4GBackupMaster,
       "fs4GBackupSlave": fs4GBackupSlave}
)
