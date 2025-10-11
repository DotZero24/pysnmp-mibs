# SNMP MIB module (QTECH-4G-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-4G-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:17 2025
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

qtech4GMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127)
)
if mibBuilder.loadTexts:
    qtech4GMonitor.setRevisions(
        ("2014-03-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Qtech4GObjects_ObjectIdentity = ObjectIdentity
qtech4GObjects = _Qtech4GObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1)
)
_Qtech4GTable_Object = MibTable
qtech4GTable = _Qtech4GTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1)
)
if mibBuilder.loadTexts:
    qtech4GTable.setStatus("current")
_Qtech4GEntry_Object = MibTableRow
qtech4GEntry = _Qtech4GEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1)
)
qtech4GEntry.setIndexNames(
    (0, "QTECH-4G-MIB", "qtech4GRouterSlotNumber"),
)
if mibBuilder.loadTexts:
    qtech4GEntry.setStatus("current")
_Qtech4GUsername_Type = DisplayString
_Qtech4GUsername_Object = MibTableColumn
qtech4GUsername = _Qtech4GUsername_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 1),
    _Qtech4GUsername_Type()
)
qtech4GUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GUsername.setStatus("current")
_Qtech4GApn_Type = DisplayString
_Qtech4GApn_Object = MibTableColumn
qtech4GApn = _Qtech4GApn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 2),
    _Qtech4GApn_Type()
)
qtech4GApn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GApn.setStatus("current")


class _Qtech4GOnlineStatus_Type(Integer32):
    """Custom type qtech4GOnlineStatus based on Integer32"""
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


_Qtech4GOnlineStatus_Type.__name__ = "Integer32"
_Qtech4GOnlineStatus_Object = MibTableColumn
qtech4GOnlineStatus = _Qtech4GOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 3),
    _Qtech4GOnlineStatus_Type()
)
qtech4GOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GOnlineStatus.setStatus("current")
_Qtech4GIMEI_Type = DisplayString
_Qtech4GIMEI_Object = MibTableColumn
qtech4GIMEI = _Qtech4GIMEI_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 4),
    _Qtech4GIMEI_Type()
)
qtech4GIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GIMEI.setStatus("current")


class _Qtech4GIPAddrType_Type(Integer32):
    """Custom type qtech4GIPAddrType based on Integer32"""
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


_Qtech4GIPAddrType_Type.__name__ = "Integer32"
_Qtech4GIPAddrType_Object = MibTableColumn
qtech4GIPAddrType = _Qtech4GIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 5),
    _Qtech4GIPAddrType_Type()
)
qtech4GIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GIPAddrType.setStatus("current")
_Qtech4GIPAddr_Type = IpAddress
_Qtech4GIPAddr_Object = MibTableColumn
qtech4GIPAddr = _Qtech4GIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 6),
    _Qtech4GIPAddr_Type()
)
qtech4GIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GIPAddr.setStatus("current")
_Qtech4GUplineTime_Type = TimeStamp
_Qtech4GUplineTime_Object = MibTableColumn
qtech4GUplineTime = _Qtech4GUplineTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 7),
    _Qtech4GUplineTime_Type()
)
qtech4GUplineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GUplineTime.setStatus("current")


class _Qtech4GActiveTime_Type(Integer32):
    """Custom type qtech4GActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Qtech4GActiveTime_Type.__name__ = "Integer32"
_Qtech4GActiveTime_Object = MibTableColumn
qtech4GActiveTime = _Qtech4GActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 8),
    _Qtech4GActiveTime_Type()
)
qtech4GActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GActiveTime.setStatus("current")


class _Qtech4GRSRP_Type(Integer32):
    """Custom type qtech4GRSRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 0),
    )


_Qtech4GRSRP_Type.__name__ = "Integer32"
_Qtech4GRSRP_Object = MibTableColumn
qtech4GRSRP = _Qtech4GRSRP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 9),
    _Qtech4GRSRP_Type()
)
qtech4GRSRP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GRSRP.setStatus("current")


class _Qtech4GSignalStrengthPercent_Type(Integer32):
    """Custom type qtech4GSignalStrengthPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Qtech4GSignalStrengthPercent_Type.__name__ = "Integer32"
_Qtech4GSignalStrengthPercent_Object = MibTableColumn
qtech4GSignalStrengthPercent = _Qtech4GSignalStrengthPercent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 10),
    _Qtech4GSignalStrengthPercent_Type()
)
qtech4GSignalStrengthPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GSignalStrengthPercent.setStatus("current")


class _Qtech4GISP_Type(Integer32):
    """Custom type qtech4GISP based on Integer32"""
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


_Qtech4GISP_Type.__name__ = "Integer32"
_Qtech4GISP_Object = MibTableColumn
qtech4GISP = _Qtech4GISP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 11),
    _Qtech4GISP_Type()
)
qtech4GISP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GISP.setStatus("current")


class _Qtech4GSysMode_Type(Integer32):
    """Custom type qtech4GSysMode based on Integer32"""
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


_Qtech4GSysMode_Type.__name__ = "Integer32"
_Qtech4GSysMode_Object = MibTableColumn
qtech4GSysMode = _Qtech4GSysMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 12),
    _Qtech4GSysMode_Type()
)
qtech4GSysMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GSysMode.setStatus("current")


class _Qtech4GServiceStatus_Type(Integer32):
    """Custom type qtech4GServiceStatus based on Integer32"""
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


_Qtech4GServiceStatus_Type.__name__ = "Integer32"
_Qtech4GServiceStatus_Object = MibTableColumn
qtech4GServiceStatus = _Qtech4GServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 13),
    _Qtech4GServiceStatus_Type()
)
qtech4GServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GServiceStatus.setStatus("current")


class _Qtech4GRoamingStatus_Type(Integer32):
    """Custom type qtech4GRoamingStatus based on Integer32"""
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


_Qtech4GRoamingStatus_Type.__name__ = "Integer32"
_Qtech4GRoamingStatus_Object = MibTableColumn
qtech4GRoamingStatus = _Qtech4GRoamingStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 14),
    _Qtech4GRoamingStatus_Type()
)
qtech4GRoamingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GRoamingStatus.setStatus("current")


class _Qtech4GDomain_Type(Integer32):
    """Custom type qtech4GDomain based on Integer32"""
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


_Qtech4GDomain_Type.__name__ = "Integer32"
_Qtech4GDomain_Object = MibTableColumn
qtech4GDomain = _Qtech4GDomain_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 15),
    _Qtech4GDomain_Type()
)
qtech4GDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GDomain.setStatus("current")


class _Qtech4GSIMStatus_Type(Integer32):
    """Custom type qtech4GSIMStatus based on Integer32"""
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


_Qtech4GSIMStatus_Type.__name__ = "Integer32"
_Qtech4GSIMStatus_Object = MibTableColumn
qtech4GSIMStatus = _Qtech4GSIMStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 16),
    _Qtech4GSIMStatus_Type()
)
qtech4GSIMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GSIMStatus.setStatus("current")


class _Qtech4GCellID_Type(Integer32):
    """Custom type qtech4GCellID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Qtech4GCellID_Type.__name__ = "Integer32"
_Qtech4GCellID_Object = MibTableColumn
qtech4GCellID = _Qtech4GCellID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 17),
    _Qtech4GCellID_Type()
)
qtech4GCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GCellID.setStatus("current")


class _Qtech4GLAC_Type(Integer32):
    """Custom type qtech4GLAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Qtech4GLAC_Type.__name__ = "Integer32"
_Qtech4GLAC_Object = MibTableColumn
qtech4GLAC = _Qtech4GLAC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 18),
    _Qtech4GLAC_Type()
)
qtech4GLAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GLAC.setStatus("current")
_Qtech4GIMSI_Type = DisplayString
_Qtech4GIMSI_Object = MibTableColumn
qtech4GIMSI = _Qtech4GIMSI_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 19),
    _Qtech4GIMSI_Type()
)
qtech4GIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GIMSI.setStatus("current")
_Qtech4GPhoneNumber_Type = DisplayString
_Qtech4GPhoneNumber_Object = MibTableColumn
qtech4GPhoneNumber = _Qtech4GPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 20),
    _Qtech4GPhoneNumber_Type()
)
qtech4GPhoneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GPhoneNumber.setStatus("current")
_Qtech4GifIndex_Type = Integer32
_Qtech4GifIndex_Object = MibTableColumn
qtech4GifIndex = _Qtech4GifIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 21),
    _Qtech4GifIndex_Type()
)
qtech4GifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GifIndex.setStatus("current")
_Qtech4GInOctets_Type = Counter64
_Qtech4GInOctets_Object = MibTableColumn
qtech4GInOctets = _Qtech4GInOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 22),
    _Qtech4GInOctets_Type()
)
qtech4GInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GInOctets.setStatus("current")
_Qtech4GOutOctets_Type = Counter64
_Qtech4GOutOctets_Object = MibTableColumn
qtech4GOutOctets = _Qtech4GOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 23),
    _Qtech4GOutOctets_Type()
)
qtech4GOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GOutOctets.setStatus("current")
_Qtech4GInSpeed_Type = Counter64
_Qtech4GInSpeed_Object = MibTableColumn
qtech4GInSpeed = _Qtech4GInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 24),
    _Qtech4GInSpeed_Type()
)
qtech4GInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GInSpeed.setStatus("current")
_Qtech4GOutSpeed_Type = Counter64
_Qtech4GOutSpeed_Object = MibTableColumn
qtech4GOutSpeed = _Qtech4GOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 25),
    _Qtech4GOutSpeed_Type()
)
qtech4GOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GOutSpeed.setStatus("current")
_Qtech4GBSLONG_Type = Integer32
_Qtech4GBSLONG_Object = MibTableColumn
qtech4GBSLONG = _Qtech4GBSLONG_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 26),
    _Qtech4GBSLONG_Type()
)
qtech4GBSLONG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GBSLONG.setStatus("current")
_Qtech4GBSLAT_Type = Integer32
_Qtech4GBSLAT_Object = MibTableColumn
qtech4GBSLAT = _Qtech4GBSLAT_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 27),
    _Qtech4GBSLAT_Type()
)
qtech4GBSLAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GBSLAT.setStatus("current")
_Qtech4GRouterType_Type = DisplayString
_Qtech4GRouterType_Object = MibTableColumn
qtech4GRouterType = _Qtech4GRouterType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 28),
    _Qtech4GRouterType_Type()
)
qtech4GRouterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GRouterType.setStatus("current")
_Qtech4GRouterSN_Type = DisplayString
_Qtech4GRouterSN_Object = MibTableColumn
qtech4GRouterSN = _Qtech4GRouterSN_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 29),
    _Qtech4GRouterSN_Type()
)
qtech4GRouterSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GRouterSN.setStatus("current")
_Qtech4GRouterSlotNumber_Type = DisplayString
_Qtech4GRouterSlotNumber_Object = MibTableColumn
qtech4GRouterSlotNumber = _Qtech4GRouterSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 30),
    _Qtech4GRouterSlotNumber_Type()
)
qtech4GRouterSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GRouterSlotNumber.setStatus("current")
_Qtech4GLineCardType_Type = DisplayString
_Qtech4GLineCardType_Object = MibTableColumn
qtech4GLineCardType = _Qtech4GLineCardType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 31),
    _Qtech4GLineCardType_Type()
)
qtech4GLineCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GLineCardType.setStatus("current")


class _Qtech4GDialdMode_Type(Integer32):
    """Custom type qtech4GDialdMode based on Integer32"""
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


_Qtech4GDialdMode_Type.__name__ = "Integer32"
_Qtech4GDialdMode_Object = MibTableColumn
qtech4GDialdMode = _Qtech4GDialdMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 32),
    _Qtech4GDialdMode_Type()
)
qtech4GDialdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GDialdMode.setStatus("current")
_Qtech4GDialOnDemandIfIndex_Type = Integer32
_Qtech4GDialOnDemandIfIndex_Object = MibTableColumn
qtech4GDialOnDemandIfIndex = _Qtech4GDialOnDemandIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 33),
    _Qtech4GDialOnDemandIfIndex_Type()
)
qtech4GDialOnDemandIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GDialOnDemandIfIndex.setStatus("current")


class _Qtech4GTrafficPreventMode_Type(Integer32):
    """Custom type qtech4GTrafficPreventMode based on Integer32"""
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


_Qtech4GTrafficPreventMode_Type.__name__ = "Integer32"
_Qtech4GTrafficPreventMode_Object = MibTableColumn
qtech4GTrafficPreventMode = _Qtech4GTrafficPreventMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 34),
    _Qtech4GTrafficPreventMode_Type()
)
qtech4GTrafficPreventMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GTrafficPreventMode.setStatus("current")
_Qtech4GTrafficPreventIfIndex_Type = Integer32
_Qtech4GTrafficPreventIfIndex_Object = MibTableColumn
qtech4GTrafficPreventIfIndex = _Qtech4GTrafficPreventIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 35),
    _Qtech4GTrafficPreventIfIndex_Type()
)
qtech4GTrafficPreventIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GTrafficPreventIfIndex.setStatus("current")
_Qtech4GTrafficPreventListID_Type = Integer32
_Qtech4GTrafficPreventListID_Object = MibTableColumn
qtech4GTrafficPreventListID = _Qtech4GTrafficPreventListID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 36),
    _Qtech4GTrafficPreventListID_Type()
)
qtech4GTrafficPreventListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GTrafficPreventListID.setStatus("current")
_Qtech4GTrafficPreventListName_Type = DisplayString
_Qtech4GTrafficPreventListName_Object = MibTableColumn
qtech4GTrafficPreventListName = _Qtech4GTrafficPreventListName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 1, 1, 1, 37),
    _Qtech4GTrafficPreventListName_Type()
)
qtech4GTrafficPreventListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtech4GTrafficPreventListName.setStatus("current")
_Qtech4GTrap_ObjectIdentity = ObjectIdentity
qtech4GTrap = _Qtech4GTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 2)
)
_Qtech4GNotifications_ObjectIdentity = ObjectIdentity
qtech4GNotifications = _Qtech4GNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 2, 1)
)

# Managed Objects groups


# Notification objects

qtech4GUpLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 2, 1, 1)
)
qtech4GUpLine.setObjects(
      *(("QTECH-4G-MIB", "qtech4GRouterSlotNumber"),
        ("QTECH-4G-MIB", "qtech4GIMSI"),
        ("QTECH-4G-MIB", "qtech4GUsername"),
        ("QTECH-4G-MIB", "qtech4GRouterSN"),
        ("QTECH-4G-MIB", "qtech4GPhoneNumber"),
        ("QTECH-4G-MIB", "qtech4GDialdMode"),
        ("QTECH-4G-MIB", "qtech4GDialOnDemandIfIndex"),
        ("QTECH-4G-MIB", "qtech4GTrafficPreventMode"),
        ("QTECH-4G-MIB", "qtech4GTrafficPreventIfIndex"),
        ("QTECH-4G-MIB", "qtech4GIPAddr"),
        ("QTECH-4G-MIB", "qtech4GTrafficPreventListID"),
        ("QTECH-4G-MIB", "qtech4GTrafficPreventListName"))
)
if mibBuilder.loadTexts:
    qtech4GUpLine.setStatus(
        "current"
    )

qtech4GDownLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 2, 1, 2)
)
qtech4GDownLine.setObjects(
      *(("QTECH-4G-MIB", "qtech4GRouterSlotNumber"),
        ("QTECH-4G-MIB", "qtech4GIMSI"),
        ("QTECH-4G-MIB", "qtech4GUsername"),
        ("QTECH-4G-MIB", "qtech4GRouterSN"),
        ("QTECH-4G-MIB", "qtech4GPhoneNumber"),
        ("QTECH-4G-MIB", "qtech4GDialdMode"),
        ("QTECH-4G-MIB", "qtech4GDialOnDemandIfIndex"),
        ("QTECH-4G-MIB", "qtech4GTrafficPreventMode"),
        ("QTECH-4G-MIB", "qtech4GTrafficPreventIfIndex"),
        ("QTECH-4G-MIB", "qtech4GIPAddr"),
        ("QTECH-4G-MIB", "qtech4GTrafficPreventListID"),
        ("QTECH-4G-MIB", "qtech4GTrafficPreventListName"))
)
if mibBuilder.loadTexts:
    qtech4GDownLine.setStatus(
        "current"
    )

qtech4GSignalThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 2, 1, 3)
)
qtech4GSignalThreshold.setObjects(
      *(("QTECH-4G-MIB", "qtech4GRouterSlotNumber"),
        ("QTECH-4G-MIB", "qtech4GIMSI"),
        ("QTECH-4G-MIB", "qtech4GRSRP"),
        ("QTECH-4G-MIB", "qtech4GSignalStrengthPercent"))
)
if mibBuilder.loadTexts:
    qtech4GSignalThreshold.setStatus(
        "current"
    )

qtech4GTrafficInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 2, 1, 4)
)
qtech4GTrafficInformation.setObjects(
      *(("QTECH-4G-MIB", "qtech4GRouterSlotNumber"),
        ("QTECH-4G-MIB", "qtech4GIMSI"),
        ("QTECH-4G-MIB", "qtech4GInOctets"),
        ("QTECH-4G-MIB", "qtech4GOutOctets"))
)
if mibBuilder.loadTexts:
    qtech4GTrafficInformation.setStatus(
        "current"
    )

qtech4GBackupMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 2, 1, 5)
)
qtech4GBackupMaster.setObjects(
      *(("QTECH-4G-MIB", "qtech4GRouterSlotNumber"),
        ("QTECH-4G-MIB", "qtech4GIMSI"),
        ("QTECH-4G-MIB", "qtech4GUsername"),
        ("QTECH-4G-MIB", "qtech4GRouterSN"),
        ("QTECH-4G-MIB", "qtech4GPhoneNumber"),
        ("QTECH-4G-MIB", "qtech4GDialdMode"),
        ("QTECH-4G-MIB", "qtech4GDialOnDemandIfIndex"),
        ("QTECH-4G-MIB", "qtech4GTrafficPreventMode"),
        ("QTECH-4G-MIB", "qtech4GTrafficPreventIfIndex"),
        ("QTECH-4G-MIB", "qtech4GIPAddr"),
        ("QTECH-4G-MIB", "qtech4GTrafficPreventListID"),
        ("QTECH-4G-MIB", "qtech4GTrafficPreventListName"))
)
if mibBuilder.loadTexts:
    qtech4GBackupMaster.setStatus(
        "current"
    )

qtech4GBackupSlave = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 127, 2, 1, 6)
)
qtech4GBackupSlave.setObjects(
      *(("QTECH-4G-MIB", "qtech4GRouterSlotNumber"),
        ("QTECH-4G-MIB", "qtech4GIMSI"),
        ("QTECH-4G-MIB", "qtech4GUsername"),
        ("QTECH-4G-MIB", "qtech4GRouterSN"),
        ("QTECH-4G-MIB", "qtech4GPhoneNumber"),
        ("QTECH-4G-MIB", "qtech4GDialdMode"),
        ("QTECH-4G-MIB", "qtech4GDialOnDemandIfIndex"),
        ("QTECH-4G-MIB", "qtech4GTrafficPreventMode"),
        ("QTECH-4G-MIB", "qtech4GTrafficPreventIfIndex"),
        ("QTECH-4G-MIB", "qtech4GIPAddr"),
        ("QTECH-4G-MIB", "qtech4GTrafficPreventListID"),
        ("QTECH-4G-MIB", "qtech4GTrafficPreventListName"))
)
if mibBuilder.loadTexts:
    qtech4GBackupSlave.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-4G-MIB",
    **{"qtech4GMonitor": qtech4GMonitor,
       "qtech4GObjects": qtech4GObjects,
       "qtech4GTable": qtech4GTable,
       "qtech4GEntry": qtech4GEntry,
       "qtech4GUsername": qtech4GUsername,
       "qtech4GApn": qtech4GApn,
       "qtech4GOnlineStatus": qtech4GOnlineStatus,
       "qtech4GIMEI": qtech4GIMEI,
       "qtech4GIPAddrType": qtech4GIPAddrType,
       "qtech4GIPAddr": qtech4GIPAddr,
       "qtech4GUplineTime": qtech4GUplineTime,
       "qtech4GActiveTime": qtech4GActiveTime,
       "qtech4GRSRP": qtech4GRSRP,
       "qtech4GSignalStrengthPercent": qtech4GSignalStrengthPercent,
       "qtech4GISP": qtech4GISP,
       "qtech4GSysMode": qtech4GSysMode,
       "qtech4GServiceStatus": qtech4GServiceStatus,
       "qtech4GRoamingStatus": qtech4GRoamingStatus,
       "qtech4GDomain": qtech4GDomain,
       "qtech4GSIMStatus": qtech4GSIMStatus,
       "qtech4GCellID": qtech4GCellID,
       "qtech4GLAC": qtech4GLAC,
       "qtech4GIMSI": qtech4GIMSI,
       "qtech4GPhoneNumber": qtech4GPhoneNumber,
       "qtech4GifIndex": qtech4GifIndex,
       "qtech4GInOctets": qtech4GInOctets,
       "qtech4GOutOctets": qtech4GOutOctets,
       "qtech4GInSpeed": qtech4GInSpeed,
       "qtech4GOutSpeed": qtech4GOutSpeed,
       "qtech4GBSLONG": qtech4GBSLONG,
       "qtech4GBSLAT": qtech4GBSLAT,
       "qtech4GRouterType": qtech4GRouterType,
       "qtech4GRouterSN": qtech4GRouterSN,
       "qtech4GRouterSlotNumber": qtech4GRouterSlotNumber,
       "qtech4GLineCardType": qtech4GLineCardType,
       "qtech4GDialdMode": qtech4GDialdMode,
       "qtech4GDialOnDemandIfIndex": qtech4GDialOnDemandIfIndex,
       "qtech4GTrafficPreventMode": qtech4GTrafficPreventMode,
       "qtech4GTrafficPreventIfIndex": qtech4GTrafficPreventIfIndex,
       "qtech4GTrafficPreventListID": qtech4GTrafficPreventListID,
       "qtech4GTrafficPreventListName": qtech4GTrafficPreventListName,
       "qtech4GTrap": qtech4GTrap,
       "qtech4GNotifications": qtech4GNotifications,
       "qtech4GUpLine": qtech4GUpLine,
       "qtech4GDownLine": qtech4GDownLine,
       "qtech4GSignalThreshold": qtech4GSignalThreshold,
       "qtech4GTrafficInformation": qtech4GTrafficInformation,
       "qtech4GBackupMaster": qtech4GBackupMaster,
       "qtech4GBackupSlave": qtech4GBackupSlave}
)
