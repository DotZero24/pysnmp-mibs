# SNMP MIB module (QTECH-ROUTER-WIFI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-ROUTER-WIFI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:26 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

qtechWifiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133)
)
if mibBuilder.loadTexts:
    qtechWifiMIB.setRevisions(
        ("2014-12-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class QtechEableType(TextualConvention, Integer32):
    status = "current"
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



class QtechWlanType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ap", 1),
          ("station", 2))
    )



class QtechIsolateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isolate", 1),
          ("noisolate", 2))
    )



class QtechAuthenticationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("share-key", 2))
    )



class QtechWapPskCiphersType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes", 1),
          ("tkip", 2),
          ("auto", 3))
    )



class QtechWifiChanWidthType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twenty", 1),
          ("forty", 2))
    )



class QtechWifiSlotType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("short", 1),
          ("long", 2))
    )



class QtechWifiFreChanelType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("two-point-four", 1),
          ("five", 2))
    )



# MIB Managed Objects in the order of their OIDs

_QtechWifiMIBObjects_ObjectIdentity = ObjectIdentity
qtechWifiMIBObjects = _QtechWifiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1)
)
_QtechWifiDot11radioSupportObjects_ObjectIdentity = ObjectIdentity
qtechWifiDot11radioSupportObjects = _QtechWifiDot11radioSupportObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 1)
)
_QtechWifiDot11radioSupportTable_Object = MibTable
qtechWifiDot11radioSupportTable = _QtechWifiDot11radioSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qtechWifiDot11radioSupportTable.setStatus("current")
_QtechWifiDot11radioSupportEntry_Object = MibTableRow
qtechWifiDot11radioSupportEntry = _QtechWifiDot11radioSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 1, 1, 1)
)
qtechWifiDot11radioSupportEntry.setIndexNames(
    (0, "QTECH-ROUTER-WIFI-MIB", "qtechWifiDot11radioIndex"),
)
if mibBuilder.loadTexts:
    qtechWifiDot11radioSupportEntry.setStatus("current")
_QtechWifiDot11radioIndex_Type = Integer32
_QtechWifiDot11radioIndex_Object = MibTableColumn
qtechWifiDot11radioIndex = _QtechWifiDot11radioIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 1, 1, 1, 1),
    _QtechWifiDot11radioIndex_Type()
)
qtechWifiDot11radioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIndex.setStatus("current")
_QtechWifiDot11radioApMaxCnt_Type = Integer32
_QtechWifiDot11radioApMaxCnt_Object = MibTableColumn
qtechWifiDot11radioApMaxCnt = _QtechWifiDot11radioApMaxCnt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 1, 1, 1, 2),
    _QtechWifiDot11radioApMaxCnt_Type()
)
qtechWifiDot11radioApMaxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWifiDot11radioApMaxCnt.setStatus("current")
_QtechWifiDot11radioStationMaxCnt_Type = Integer32
_QtechWifiDot11radioStationMaxCnt_Object = MibTableColumn
qtechWifiDot11radioStationMaxCnt = _QtechWifiDot11radioStationMaxCnt_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 1, 1, 1, 3),
    _QtechWifiDot11radioStationMaxCnt_Type()
)
qtechWifiDot11radioStationMaxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWifiDot11radioStationMaxCnt.setStatus("current")
_QtechWifiWlanObjects_ObjectIdentity = ObjectIdentity
qtechWifiWlanObjects = _QtechWifiWlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 2)
)
_QtechWifiWlanIndexNext_Type = Integer32
_QtechWifiWlanIndexNext_Object = MibScalar
qtechWifiWlanIndexNext = _QtechWifiWlanIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 2, 1),
    _QtechWifiWlanIndexNext_Type()
)
qtechWifiWlanIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWifiWlanIndexNext.setStatus("current")
_QtechWifiVlanIndexNext_Type = Integer32
_QtechWifiVlanIndexNext_Object = MibScalar
qtechWifiVlanIndexNext = _QtechWifiVlanIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 2, 2),
    _QtechWifiVlanIndexNext_Type()
)
qtechWifiVlanIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWifiVlanIndexNext.setStatus("current")
_QtechWifiWlanTable_Object = MibTable
qtechWifiWlanTable = _QtechWifiWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 2, 3)
)
if mibBuilder.loadTexts:
    qtechWifiWlanTable.setStatus("current")
_QtechWifiWlanEntry_Object = MibTableRow
qtechWifiWlanEntry = _QtechWifiWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 2, 3, 1)
)
qtechWifiWlanEntry.setIndexNames(
    (0, "QTECH-ROUTER-WIFI-MIB", "qtechWifiWlanIndex"),
)
if mibBuilder.loadTexts:
    qtechWifiWlanEntry.setStatus("current")


class _QtechWifiWlanIndex_Type(Integer32):
    """Custom type qtechWifiWlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiWlanIndex_Type.__name__ = "Integer32"
_QtechWifiWlanIndex_Object = MibTableColumn
qtechWifiWlanIndex = _QtechWifiWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 2, 3, 1, 1),
    _QtechWifiWlanIndex_Type()
)
qtechWifiWlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWifiWlanIndex.setStatus("current")
_QtechWifiWlanType_Type = QtechWlanType
_QtechWifiWlanType_Object = MibTableColumn
qtechWifiWlanType = _QtechWifiWlanType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 2, 3, 1, 2),
    _QtechWifiWlanType_Type()
)
qtechWifiWlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiWlanType.setStatus("current")


class _QtechWifiWlanSsidName_Type(DisplayString):
    """Custom type qtechWifiWlanSsidName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechWifiWlanSsidName_Type.__name__ = "DisplayString"
_QtechWifiWlanSsidName_Object = MibTableColumn
qtechWifiWlanSsidName = _QtechWifiWlanSsidName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 2, 3, 1, 3),
    _QtechWifiWlanSsidName_Type()
)
qtechWifiWlanSsidName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiWlanSsidName.setStatus("current")


class _QtechWifiWlanVlanId_Type(Integer32):
    """Custom type qtechWifiWlanVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_QtechWifiWlanVlanId_Type.__name__ = "Integer32"
_QtechWifiWlanVlanId_Object = MibTableColumn
qtechWifiWlanVlanId = _QtechWifiWlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 2, 3, 1, 4),
    _QtechWifiWlanVlanId_Type()
)
qtechWifiWlanVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiWlanVlanId.setStatus("current")
_QtechWifiWlanRowStatus_Type = RowStatus
_QtechWifiWlanRowStatus_Object = MibTableColumn
qtechWifiWlanRowStatus = _QtechWifiWlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 2, 3, 1, 5),
    _QtechWifiWlanRowStatus_Type()
)
qtechWifiWlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiWlanRowStatus.setStatus("current")
_QtechWifiWlanBroadcastSsid_Type = QtechEableType
_QtechWifiWlanBroadcastSsid_Object = MibTableColumn
qtechWifiWlanBroadcastSsid = _QtechWifiWlanBroadcastSsid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 2, 3, 1, 6),
    _QtechWifiWlanBroadcastSsid_Type()
)
qtechWifiWlanBroadcastSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiWlanBroadcastSsid.setStatus("current")
_QtechWifiWlanIsolate_Type = QtechIsolateType
_QtechWifiWlanIsolate_Object = MibTableColumn
qtechWifiWlanIsolate = _QtechWifiWlanIsolate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 2, 3, 1, 7),
    _QtechWifiWlanIsolate_Type()
)
qtechWifiWlanIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiWlanIsolate.setStatus("current")
_QtechWifiWlanBssStaLimit_Type = Integer32
_QtechWifiWlanBssStaLimit_Object = MibTableColumn
qtechWifiWlanBssStaLimit = _QtechWifiWlanBssStaLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 2, 3, 1, 8),
    _QtechWifiWlanBssStaLimit_Type()
)
qtechWifiWlanBssStaLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiWlanBssStaLimit.setStatus("current")


class _RujieWifiWlanSecurityType_Type(Bits):
    """Custom type rujieWifiWlanSecurityType based on Bits"""
    namedValues = NamedValues(
        *(("null", 0),
          ("wep", 1),
          ("wpa-psk", 2),
          ("wpa2-psk", 3))
    )

_RujieWifiWlanSecurityType_Type.__name__ = "Bits"
_RujieWifiWlanSecurityType_Object = MibTableColumn
rujieWifiWlanSecurityType = _RujieWifiWlanSecurityType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 2, 3, 1, 9),
    _RujieWifiWlanSecurityType_Type()
)
rujieWifiWlanSecurityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rujieWifiWlanSecurityType.setStatus("current")
_QtechWifiWlanAuthenticationSetKey_Type = DisplayString
_QtechWifiWlanAuthenticationSetKey_Object = MibTableColumn
qtechWifiWlanAuthenticationSetKey = _QtechWifiWlanAuthenticationSetKey_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 2, 3, 1, 10),
    _QtechWifiWlanAuthenticationSetKey_Type()
)
qtechWifiWlanAuthenticationSetKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiWlanAuthenticationSetKey.setStatus("current")
_QtechWifiWlanWepAuthenticationType_Type = QtechAuthenticationType
_QtechWifiWlanWepAuthenticationType_Object = MibTableColumn
qtechWifiWlanWepAuthenticationType = _QtechWifiWlanWepAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 2, 3, 1, 11),
    _QtechWifiWlanWepAuthenticationType_Type()
)
qtechWifiWlanWepAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiWlanWepAuthenticationType.setStatus("current")
_QtechWifiWlanWpaPskCiphersType_Type = QtechWapPskCiphersType
_QtechWifiWlanWpaPskCiphersType_Object = MibTableColumn
qtechWifiWlanWpaPskCiphersType = _QtechWifiWlanWpaPskCiphersType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 2, 3, 1, 12),
    _QtechWifiWlanWpaPskCiphersType_Type()
)
qtechWifiWlanWpaPskCiphersType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiWlanWpaPskCiphersType.setStatus("current")
_QtechWifiWlanPassphrase_Type = DisplayString
_QtechWifiWlanPassphrase_Object = MibTableColumn
qtechWifiWlanPassphrase = _QtechWifiWlanPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 2, 3, 1, 13),
    _QtechWifiWlanPassphrase_Type()
)
qtechWifiWlanPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiWlanPassphrase.setStatus("current")
_QtechWifiWlanDot11RadioIfindex_Type = Integer32
_QtechWifiWlanDot11RadioIfindex_Object = MibTableColumn
qtechWifiWlanDot11RadioIfindex = _QtechWifiWlanDot11RadioIfindex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 2, 3, 1, 14),
    _QtechWifiWlanDot11RadioIfindex_Type()
)
qtechWifiWlanDot11RadioIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWifiWlanDot11RadioIfindex.setStatus("current")
_QtechWifiWlanDot11RadioSubIfindex_Type = Integer32
_QtechWifiWlanDot11RadioSubIfindex_Object = MibTableColumn
qtechWifiWlanDot11RadioSubIfindex = _QtechWifiWlanDot11RadioSubIfindex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 2, 3, 1, 15),
    _QtechWifiWlanDot11RadioSubIfindex_Type()
)
qtechWifiWlanDot11RadioSubIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWifiWlanDot11RadioSubIfindex.setStatus("current")
_QtechWifiDot11radioIfConfigObjects_ObjectIdentity = ObjectIdentity
qtechWifiDot11radioIfConfigObjects = _QtechWifiDot11radioIfConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3)
)
_QtechWifiDot11radioIfConfigTable_Object = MibTable
qtechWifiDot11radioIfConfigTable = _QtechWifiDot11radioIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1)
)
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigTable.setStatus("current")
_QtechWifiDot11radioIfConfigEntry_Object = MibTableRow
qtechWifiDot11radioIfConfigEntry = _QtechWifiDot11radioIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1)
)
qtechWifiDot11radioIfConfigEntry.setIndexNames(
    (0, "QTECH-ROUTER-WIFI-MIB", "qtechWifiDot11radioIfConfigIfIndex"),
)
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEntry.setStatus("current")
_QtechWifiDot11radioIfConfigIfIndex_Type = Integer32
_QtechWifiDot11radioIfConfigIfIndex_Object = MibTableColumn
qtechWifiDot11radioIfConfigIfIndex = _QtechWifiDot11radioIfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 1),
    _QtechWifiDot11radioIfConfigIfIndex_Type()
)
qtechWifiDot11radioIfConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigIfIndex.setStatus("current")
_QtechWifiDot11radioIfConfigRowStatus_Type = RowStatus
_QtechWifiDot11radioIfConfigRowStatus_Object = MibTableColumn
qtechWifiDot11radioIfConfigRowStatus = _QtechWifiDot11radioIfConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 2),
    _QtechWifiDot11radioIfConfigRowStatus_Type()
)
qtechWifiDot11radioIfConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigRowStatus.setStatus("current")
_QtechWifiDot11radioIfConfigFreBand_Type = QtechWifiFreChanelType
_QtechWifiDot11radioIfConfigFreBand_Object = MibTableColumn
qtechWifiDot11radioIfConfigFreBand = _QtechWifiDot11radioIfConfigFreBand_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 3),
    _QtechWifiDot11radioIfConfigFreBand_Type()
)
qtechWifiDot11radioIfConfigFreBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigFreBand.setStatus("current")
_QtechWifiDot11radioIfConfigChannel_Type = Integer32
_QtechWifiDot11radioIfConfigChannel_Object = MibTableColumn
qtechWifiDot11radioIfConfigChannel = _QtechWifiDot11radioIfConfigChannel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 4),
    _QtechWifiDot11radioIfConfigChannel_Type()
)
qtechWifiDot11radioIfConfigChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigChannel.setStatus("current")
_QtechWifiDot11radioIfConfigChanWidth_Type = QtechWifiChanWidthType
_QtechWifiDot11radioIfConfigChanWidth_Object = MibTableColumn
qtechWifiDot11radioIfConfigChanWidth = _QtechWifiDot11radioIfConfigChanWidth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 5),
    _QtechWifiDot11radioIfConfigChanWidth_Type()
)
qtechWifiDot11radioIfConfigChanWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigChanWidth.setStatus("current")
_QtechWifiDot11radioIfConfigCountryCode_Type = DisplayString
_QtechWifiDot11radioIfConfigCountryCode_Object = MibTableColumn
qtechWifiDot11radioIfConfigCountryCode = _QtechWifiDot11radioIfConfigCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 6),
    _QtechWifiDot11radioIfConfigCountryCode_Type()
)
qtechWifiDot11radioIfConfigCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigCountryCode.setStatus("current")


class _QtechWifiDot11radioIfConfigPowerLocal_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigPowerLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QtechWifiDot11radioIfConfigPowerLocal_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigPowerLocal_Object = MibTableColumn
qtechWifiDot11radioIfConfigPowerLocal = _QtechWifiDot11radioIfConfigPowerLocal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 7),
    _QtechWifiDot11radioIfConfigPowerLocal_Type()
)
qtechWifiDot11radioIfConfigPowerLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigPowerLocal.setStatus("current")


class _QtechWifiDot11radioIfConfigWirelessProSupport_Type(Bits):
    """Custom type qtechWifiDot11radioIfConfigWirelessProSupport based on Bits"""
    namedValues = NamedValues(
        *(("null", 0),
          ("b", 1),
          ("g", 2),
          ("n", 3))
    )

_QtechWifiDot11radioIfConfigWirelessProSupport_Type.__name__ = "Bits"
_QtechWifiDot11radioIfConfigWirelessProSupport_Object = MibTableColumn
qtechWifiDot11radioIfConfigWirelessProSupport = _QtechWifiDot11radioIfConfigWirelessProSupport_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 8),
    _QtechWifiDot11radioIfConfigWirelessProSupport_Type()
)
qtechWifiDot11radioIfConfigWirelessProSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigWirelessProSupport.setStatus("current")


class _QtechWifiDot11radioIfConfigStaLimit_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigStaLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_QtechWifiDot11radioIfConfigStaLimit_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigStaLimit_Object = MibTableColumn
qtechWifiDot11radioIfConfigStaLimit = _QtechWifiDot11radioIfConfigStaLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 9),
    _QtechWifiDot11radioIfConfigStaLimit_Type()
)
qtechWifiDot11radioIfConfigStaLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigStaLimit.setStatus("current")
_QtechWifiDot11radioIfConfig20ShortGiEnable_Type = QtechEableType
_QtechWifiDot11radioIfConfig20ShortGiEnable_Object = MibTableColumn
qtechWifiDot11radioIfConfig20ShortGiEnable = _QtechWifiDot11radioIfConfig20ShortGiEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 10),
    _QtechWifiDot11radioIfConfig20ShortGiEnable_Type()
)
qtechWifiDot11radioIfConfig20ShortGiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfig20ShortGiEnable.setStatus("current")
_QtechWifiDot11radioIfConfig40ShortGiEnable_Type = QtechEableType
_QtechWifiDot11radioIfConfig40ShortGiEnable_Object = MibTableColumn
qtechWifiDot11radioIfConfig40ShortGiEnable = _QtechWifiDot11radioIfConfig40ShortGiEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 11),
    _QtechWifiDot11radioIfConfig40ShortGiEnable_Type()
)
qtechWifiDot11radioIfConfig40ShortGiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfig40ShortGiEnable.setStatus("current")
_QtechWifiDot11radioIfConfigShortPreambleEnable_Type = QtechEableType
_QtechWifiDot11radioIfConfigShortPreambleEnable_Object = MibTableColumn
qtechWifiDot11radioIfConfigShortPreambleEnable = _QtechWifiDot11radioIfConfigShortPreambleEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 12),
    _QtechWifiDot11radioIfConfigShortPreambleEnable_Type()
)
qtechWifiDot11radioIfConfigShortPreambleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigShortPreambleEnable.setStatus("current")
_QtechWifiDot11radioIfConfigSlottime_Type = QtechWifiSlotType
_QtechWifiDot11radioIfConfigSlottime_Object = MibTableColumn
qtechWifiDot11radioIfConfigSlottime = _QtechWifiDot11radioIfConfigSlottime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 13),
    _QtechWifiDot11radioIfConfigSlottime_Type()
)
qtechWifiDot11radioIfConfigSlottime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigSlottime.setStatus("current")


class _QtechWifiDot11radioIfConfigRtsThreshold_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigRtsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(257, 2347),
    )


_QtechWifiDot11radioIfConfigRtsThreshold_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigRtsThreshold_Object = MibTableColumn
qtechWifiDot11radioIfConfigRtsThreshold = _QtechWifiDot11radioIfConfigRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 14),
    _QtechWifiDot11radioIfConfigRtsThreshold_Type()
)
qtechWifiDot11radioIfConfigRtsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigRtsThreshold.setStatus("current")


class _QtechWifiDot11radioIfConfigFragmentThreshold_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigFragmentThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_QtechWifiDot11radioIfConfigFragmentThreshold_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigFragmentThreshold_Object = MibTableColumn
qtechWifiDot11radioIfConfigFragmentThreshold = _QtechWifiDot11radioIfConfigFragmentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 15),
    _QtechWifiDot11radioIfConfigFragmentThreshold_Type()
)
qtechWifiDot11radioIfConfigFragmentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigFragmentThreshold.setStatus("current")


class _QtechWifiDot11radioIfConfigResponseRssi_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigResponseRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_QtechWifiDot11radioIfConfigResponseRssi_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigResponseRssi_Object = MibTableColumn
qtechWifiDot11radioIfConfigResponseRssi = _QtechWifiDot11radioIfConfigResponseRssi_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 16),
    _QtechWifiDot11radioIfConfigResponseRssi_Type()
)
qtechWifiDot11radioIfConfigResponseRssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigResponseRssi.setStatus("current")
_QtechWifiDot11radioIfConfigEnableQos_Type = QtechEableType
_QtechWifiDot11radioIfConfigEnableQos_Object = MibTableColumn
qtechWifiDot11radioIfConfigEnableQos = _QtechWifiDot11radioIfConfigEnableQos_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 17),
    _QtechWifiDot11radioIfConfigEnableQos_Type()
)
qtechWifiDot11radioIfConfigEnableQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEnableQos.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaClientBgAifsn_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaClientBgAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaClientBgAifsn_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaClientBgAifsn_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaClientBgAifsn = _QtechWifiDot11radioIfConfigEdcaClientBgAifsn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 18),
    _QtechWifiDot11radioIfConfigEdcaClientBgAifsn_Type()
)
qtechWifiDot11radioIfConfigEdcaClientBgAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaClientBgAifsn.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaClientBgCwmin_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaClientBgCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaClientBgCwmin_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaClientBgCwmin_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaClientBgCwmin = _QtechWifiDot11radioIfConfigEdcaClientBgCwmin_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 19),
    _QtechWifiDot11radioIfConfigEdcaClientBgCwmin_Type()
)
qtechWifiDot11radioIfConfigEdcaClientBgCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaClientBgCwmin.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaClientBgCwmax_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaClientBgCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaClientBgCwmax_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaClientBgCwmax_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaClientBgCwmax = _QtechWifiDot11radioIfConfigEdcaClientBgCwmax_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 20),
    _QtechWifiDot11radioIfConfigEdcaClientBgCwmax_Type()
)
qtechWifiDot11radioIfConfigEdcaClientBgCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaClientBgCwmax.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaClientBgTxop_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaClientBgTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechWifiDot11radioIfConfigEdcaClientBgTxop_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaClientBgTxop_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaClientBgTxop = _QtechWifiDot11radioIfConfigEdcaClientBgTxop_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 21),
    _QtechWifiDot11radioIfConfigEdcaClientBgTxop_Type()
)
qtechWifiDot11radioIfConfigEdcaClientBgTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaClientBgTxop.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaClientBeAifsn_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaClientBeAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaClientBeAifsn_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaClientBeAifsn_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaClientBeAifsn = _QtechWifiDot11radioIfConfigEdcaClientBeAifsn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 22),
    _QtechWifiDot11radioIfConfigEdcaClientBeAifsn_Type()
)
qtechWifiDot11radioIfConfigEdcaClientBeAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaClientBeAifsn.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaClientBeCwmin_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaClientBeCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaClientBeCwmin_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaClientBeCwmin_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaClientBeCwmin = _QtechWifiDot11radioIfConfigEdcaClientBeCwmin_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 23),
    _QtechWifiDot11radioIfConfigEdcaClientBeCwmin_Type()
)
qtechWifiDot11radioIfConfigEdcaClientBeCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaClientBeCwmin.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaClientBeCwmax_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaClientBeCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaClientBeCwmax_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaClientBeCwmax_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaClientBeCwmax = _QtechWifiDot11radioIfConfigEdcaClientBeCwmax_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 24),
    _QtechWifiDot11radioIfConfigEdcaClientBeCwmax_Type()
)
qtechWifiDot11radioIfConfigEdcaClientBeCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaClientBeCwmax.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaClientBeTxop_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaClientBeTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechWifiDot11radioIfConfigEdcaClientBeTxop_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaClientBeTxop_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaClientBeTxop = _QtechWifiDot11radioIfConfigEdcaClientBeTxop_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 25),
    _QtechWifiDot11radioIfConfigEdcaClientBeTxop_Type()
)
qtechWifiDot11radioIfConfigEdcaClientBeTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaClientBeTxop.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaClientViAifsn_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaClientViAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaClientViAifsn_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaClientViAifsn_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaClientViAifsn = _QtechWifiDot11radioIfConfigEdcaClientViAifsn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 26),
    _QtechWifiDot11radioIfConfigEdcaClientViAifsn_Type()
)
qtechWifiDot11radioIfConfigEdcaClientViAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaClientViAifsn.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaClientViCwmin_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaClientViCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaClientViCwmin_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaClientViCwmin_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaClientViCwmin = _QtechWifiDot11radioIfConfigEdcaClientViCwmin_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 27),
    _QtechWifiDot11radioIfConfigEdcaClientViCwmin_Type()
)
qtechWifiDot11radioIfConfigEdcaClientViCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaClientViCwmin.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaClientViCwmax_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaClientViCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaClientViCwmax_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaClientViCwmax_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaClientViCwmax = _QtechWifiDot11radioIfConfigEdcaClientViCwmax_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 28),
    _QtechWifiDot11radioIfConfigEdcaClientViCwmax_Type()
)
qtechWifiDot11radioIfConfigEdcaClientViCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaClientViCwmax.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaClientViTxop_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaClientViTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechWifiDot11radioIfConfigEdcaClientViTxop_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaClientViTxop_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaClientViTxop = _QtechWifiDot11radioIfConfigEdcaClientViTxop_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 29),
    _QtechWifiDot11radioIfConfigEdcaClientViTxop_Type()
)
qtechWifiDot11radioIfConfigEdcaClientViTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaClientViTxop.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaClientVoAifsn_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaClientVoAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaClientVoAifsn_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaClientVoAifsn_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaClientVoAifsn = _QtechWifiDot11radioIfConfigEdcaClientVoAifsn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 30),
    _QtechWifiDot11radioIfConfigEdcaClientVoAifsn_Type()
)
qtechWifiDot11radioIfConfigEdcaClientVoAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaClientVoAifsn.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaClientVoCwmin_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaClientVoCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaClientVoCwmin_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaClientVoCwmin_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaClientVoCwmin = _QtechWifiDot11radioIfConfigEdcaClientVoCwmin_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 31),
    _QtechWifiDot11radioIfConfigEdcaClientVoCwmin_Type()
)
qtechWifiDot11radioIfConfigEdcaClientVoCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaClientVoCwmin.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaClientVoCwmax_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaClientVoCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaClientVoCwmax_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaClientVoCwmax_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaClientVoCwmax = _QtechWifiDot11radioIfConfigEdcaClientVoCwmax_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 32),
    _QtechWifiDot11radioIfConfigEdcaClientVoCwmax_Type()
)
qtechWifiDot11radioIfConfigEdcaClientVoCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaClientVoCwmax.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaClientVoTxop_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaClientVoTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechWifiDot11radioIfConfigEdcaClientVoTxop_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaClientVoTxop_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaClientVoTxop = _QtechWifiDot11radioIfConfigEdcaClientVoTxop_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 33),
    _QtechWifiDot11radioIfConfigEdcaClientVoTxop_Type()
)
qtechWifiDot11radioIfConfigEdcaClientVoTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaClientVoTxop.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaRadioBgAifsn_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaRadioBgAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaRadioBgAifsn_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaRadioBgAifsn_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaRadioBgAifsn = _QtechWifiDot11radioIfConfigEdcaRadioBgAifsn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 34),
    _QtechWifiDot11radioIfConfigEdcaRadioBgAifsn_Type()
)
qtechWifiDot11radioIfConfigEdcaRadioBgAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaRadioBgAifsn.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaRadioBgCwmin_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaRadioBgCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaRadioBgCwmin_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaRadioBgCwmin_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaRadioBgCwmin = _QtechWifiDot11radioIfConfigEdcaRadioBgCwmin_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 35),
    _QtechWifiDot11radioIfConfigEdcaRadioBgCwmin_Type()
)
qtechWifiDot11radioIfConfigEdcaRadioBgCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaRadioBgCwmin.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaRadioBgCwmax_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaRadioBgCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaRadioBgCwmax_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaRadioBgCwmax_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaRadioBgCwmax = _QtechWifiDot11radioIfConfigEdcaRadioBgCwmax_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 36),
    _QtechWifiDot11radioIfConfigEdcaRadioBgCwmax_Type()
)
qtechWifiDot11radioIfConfigEdcaRadioBgCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaRadioBgCwmax.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaRadioBgTxop_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaRadioBgTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechWifiDot11radioIfConfigEdcaRadioBgTxop_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaRadioBgTxop_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaRadioBgTxop = _QtechWifiDot11radioIfConfigEdcaRadioBgTxop_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 37),
    _QtechWifiDot11radioIfConfigEdcaRadioBgTxop_Type()
)
qtechWifiDot11radioIfConfigEdcaRadioBgTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaRadioBgTxop.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaRadioBeAifsn_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaRadioBeAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaRadioBeAifsn_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaRadioBeAifsn_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaRadioBeAifsn = _QtechWifiDot11radioIfConfigEdcaRadioBeAifsn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 38),
    _QtechWifiDot11radioIfConfigEdcaRadioBeAifsn_Type()
)
qtechWifiDot11radioIfConfigEdcaRadioBeAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaRadioBeAifsn.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaRadioBeCwmin_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaRadioBeCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaRadioBeCwmin_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaRadioBeCwmin_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaRadioBeCwmin = _QtechWifiDot11radioIfConfigEdcaRadioBeCwmin_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 39),
    _QtechWifiDot11radioIfConfigEdcaRadioBeCwmin_Type()
)
qtechWifiDot11radioIfConfigEdcaRadioBeCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaRadioBeCwmin.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaRadioBeCwmax_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaRadioBeCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaRadioBeCwmax_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaRadioBeCwmax_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaRadioBeCwmax = _QtechWifiDot11radioIfConfigEdcaRadioBeCwmax_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 40),
    _QtechWifiDot11radioIfConfigEdcaRadioBeCwmax_Type()
)
qtechWifiDot11radioIfConfigEdcaRadioBeCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaRadioBeCwmax.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaRadioBeTxop_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaRadioBeTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechWifiDot11radioIfConfigEdcaRadioBeTxop_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaRadioBeTxop_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaRadioBeTxop = _QtechWifiDot11radioIfConfigEdcaRadioBeTxop_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 41),
    _QtechWifiDot11radioIfConfigEdcaRadioBeTxop_Type()
)
qtechWifiDot11radioIfConfigEdcaRadioBeTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaRadioBeTxop.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaRadioViAifsn_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaRadioViAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaRadioViAifsn_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaRadioViAifsn_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaRadioViAifsn = _QtechWifiDot11radioIfConfigEdcaRadioViAifsn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 42),
    _QtechWifiDot11radioIfConfigEdcaRadioViAifsn_Type()
)
qtechWifiDot11radioIfConfigEdcaRadioViAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaRadioViAifsn.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaRadioViCwmin_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaRadioViCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaRadioViCwmin_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaRadioViCwmin_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaRadioViCwmin = _QtechWifiDot11radioIfConfigEdcaRadioViCwmin_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 43),
    _QtechWifiDot11radioIfConfigEdcaRadioViCwmin_Type()
)
qtechWifiDot11radioIfConfigEdcaRadioViCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaRadioViCwmin.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaRadioViCwmax_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaRadioViCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaRadioViCwmax_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaRadioViCwmax_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaRadioViCwmax = _QtechWifiDot11radioIfConfigEdcaRadioViCwmax_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 44),
    _QtechWifiDot11radioIfConfigEdcaRadioViCwmax_Type()
)
qtechWifiDot11radioIfConfigEdcaRadioViCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaRadioViCwmax.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaRadioViTxop_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaRadioViTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechWifiDot11radioIfConfigEdcaRadioViTxop_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaRadioViTxop_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaRadioViTxop = _QtechWifiDot11radioIfConfigEdcaRadioViTxop_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 45),
    _QtechWifiDot11radioIfConfigEdcaRadioViTxop_Type()
)
qtechWifiDot11radioIfConfigEdcaRadioViTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaRadioViTxop.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaRadioVoAifsn_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaRadioVoAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaRadioVoAifsn_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaRadioVoAifsn_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaRadioVoAifsn = _QtechWifiDot11radioIfConfigEdcaRadioVoAifsn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 46),
    _QtechWifiDot11radioIfConfigEdcaRadioVoAifsn_Type()
)
qtechWifiDot11radioIfConfigEdcaRadioVoAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaRadioVoAifsn.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaRadioVoCwmin_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaRadioVoCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaRadioVoCwmin_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaRadioVoCwmin_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaRadioVoCwmin = _QtechWifiDot11radioIfConfigEdcaRadioVoCwmin_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 47),
    _QtechWifiDot11radioIfConfigEdcaRadioVoCwmin_Type()
)
qtechWifiDot11radioIfConfigEdcaRadioVoCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaRadioVoCwmin.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaRadioVoCwmax_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaRadioVoCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechWifiDot11radioIfConfigEdcaRadioVoCwmax_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaRadioVoCwmax_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaRadioVoCwmax = _QtechWifiDot11radioIfConfigEdcaRadioVoCwmax_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 48),
    _QtechWifiDot11radioIfConfigEdcaRadioVoCwmax_Type()
)
qtechWifiDot11radioIfConfigEdcaRadioVoCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaRadioVoCwmax.setStatus("current")


class _QtechWifiDot11radioIfConfigEdcaRadioVoTxop_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigEdcaRadioVoTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechWifiDot11radioIfConfigEdcaRadioVoTxop_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigEdcaRadioVoTxop_Object = MibTableColumn
qtechWifiDot11radioIfConfigEdcaRadioVoTxop = _QtechWifiDot11radioIfConfigEdcaRadioVoTxop_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 49),
    _QtechWifiDot11radioIfConfigEdcaRadioVoTxop_Type()
)
qtechWifiDot11radioIfConfigEdcaRadioVoTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigEdcaRadioVoTxop.setStatus("current")


class _QtechWifiDot11radioIfConfigAntennaTransChainmask_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigAntennaTransChainmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_QtechWifiDot11radioIfConfigAntennaTransChainmask_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigAntennaTransChainmask_Object = MibTableColumn
qtechWifiDot11radioIfConfigAntennaTransChainmask = _QtechWifiDot11radioIfConfigAntennaTransChainmask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 50),
    _QtechWifiDot11radioIfConfigAntennaTransChainmask_Type()
)
qtechWifiDot11radioIfConfigAntennaTransChainmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigAntennaTransChainmask.setStatus("current")


class _QtechWifiDot11radioIfConfigAntennaReceiveChainmask_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigAntennaReceiveChainmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_QtechWifiDot11radioIfConfigAntennaReceiveChainmask_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigAntennaReceiveChainmask_Object = MibTableColumn
qtechWifiDot11radioIfConfigAntennaReceiveChainmask = _QtechWifiDot11radioIfConfigAntennaReceiveChainmask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 51),
    _QtechWifiDot11radioIfConfigAntennaReceiveChainmask_Type()
)
qtechWifiDot11radioIfConfigAntennaReceiveChainmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigAntennaReceiveChainmask.setStatus("current")


class _QtechWifiDot11radioIfConfigBeaconDtimPeriod_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigBeaconDtimPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QtechWifiDot11radioIfConfigBeaconDtimPeriod_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigBeaconDtimPeriod_Object = MibTableColumn
qtechWifiDot11radioIfConfigBeaconDtimPeriod = _QtechWifiDot11radioIfConfigBeaconDtimPeriod_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 52),
    _QtechWifiDot11radioIfConfigBeaconDtimPeriod_Type()
)
qtechWifiDot11radioIfConfigBeaconDtimPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigBeaconDtimPeriod.setStatus("current")


class _QtechWifiDot11radioIfConfigBeaconPeriod_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigBeaconPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_QtechWifiDot11radioIfConfigBeaconPeriod_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigBeaconPeriod_Object = MibTableColumn
qtechWifiDot11radioIfConfigBeaconPeriod = _QtechWifiDot11radioIfConfigBeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 53),
    _QtechWifiDot11radioIfConfigBeaconPeriod_Type()
)
qtechWifiDot11radioIfConfigBeaconPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigBeaconPeriod.setStatus("current")


class _QtechWifiDot11radioIfConfigRetrieShortTime_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigRetrieShortTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_QtechWifiDot11radioIfConfigRetrieShortTime_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigRetrieShortTime_Object = MibTableColumn
qtechWifiDot11radioIfConfigRetrieShortTime = _QtechWifiDot11radioIfConfigRetrieShortTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 54),
    _QtechWifiDot11radioIfConfigRetrieShortTime_Type()
)
qtechWifiDot11radioIfConfigRetrieShortTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigRetrieShortTime.setStatus("current")


class _QtechWifiDot11radioIfConfigRetrieLongTime_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigRetrieLongTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_QtechWifiDot11radioIfConfigRetrieLongTime_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigRetrieLongTime_Object = MibTableColumn
qtechWifiDot11radioIfConfigRetrieLongTime = _QtechWifiDot11radioIfConfigRetrieLongTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 55),
    _QtechWifiDot11radioIfConfigRetrieLongTime_Type()
)
qtechWifiDot11radioIfConfigRetrieLongTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigRetrieLongTime.setStatus("current")


class _QtechWifiDot11radioIfConfigStaIdleTimeout_Type(Integer32):
    """Custom type qtechWifiDot11radioIfConfigStaIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_QtechWifiDot11radioIfConfigStaIdleTimeout_Type.__name__ = "Integer32"
_QtechWifiDot11radioIfConfigStaIdleTimeout_Object = MibTableColumn
qtechWifiDot11radioIfConfigStaIdleTimeout = _QtechWifiDot11radioIfConfigStaIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 56),
    _QtechWifiDot11radioIfConfigStaIdleTimeout_Type()
)
qtechWifiDot11radioIfConfigStaIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigStaIdleTimeout.setStatus("current")


class _QtechWifiDot11radioIfConfigWlanIdList_Type(Bits):
    """Custom type qtechWifiDot11radioIfConfigWlanIdList based on Bits"""
    namedValues = NamedValues(
        *(("w0", 0),
          ("w1", 1),
          ("w2", 2),
          ("w3", 3),
          ("w4", 4),
          ("w5", 5),
          ("w6", 6),
          ("w7", 7),
          ("w8", 8),
          ("w9", 9),
          ("w10", 10),
          ("w11", 11),
          ("w12", 12),
          ("w13", 13),
          ("w14", 14),
          ("w15", 15))
    )

_QtechWifiDot11radioIfConfigWlanIdList_Type.__name__ = "Bits"
_QtechWifiDot11radioIfConfigWlanIdList_Object = MibTableColumn
qtechWifiDot11radioIfConfigWlanIdList = _QtechWifiDot11radioIfConfigWlanIdList_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 3, 1, 1, 57),
    _QtechWifiDot11radioIfConfigWlanIdList_Type()
)
qtechWifiDot11radioIfConfigWlanIdList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWifiDot11radioIfConfigWlanIdList.setStatus("current")
_QtechWifiWlanAssociateObjects_ObjectIdentity = ObjectIdentity
qtechWifiWlanAssociateObjects = _QtechWifiWlanAssociateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 4)
)
_QtechWifiWlanAssociateTable_Object = MibTable
qtechWifiWlanAssociateTable = _QtechWifiWlanAssociateTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 4, 1)
)
if mibBuilder.loadTexts:
    qtechWifiWlanAssociateTable.setStatus("current")
_QtechWifiWlanAssociateEntry_Object = MibTableRow
qtechWifiWlanAssociateEntry = _QtechWifiWlanAssociateEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 4, 1, 1)
)
qtechWifiWlanAssociateEntry.setIndexNames(
    (0, "QTECH-ROUTER-WIFI-MIB", "qtechWifiWlanAssociateWlanId"),
    (0, "QTECH-ROUTER-WIFI-MIB", "qtechWifiWlanAssociateStaMacAdress"),
)
if mibBuilder.loadTexts:
    qtechWifiWlanAssociateEntry.setStatus("current")
_QtechWifiWlanAssociateWlanId_Type = Integer32
_QtechWifiWlanAssociateWlanId_Object = MibTableColumn
qtechWifiWlanAssociateWlanId = _QtechWifiWlanAssociateWlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 4, 1, 1, 1),
    _QtechWifiWlanAssociateWlanId_Type()
)
qtechWifiWlanAssociateWlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWifiWlanAssociateWlanId.setStatus("current")
_QtechWifiWlanAssociateStaMacAdress_Type = DisplayString
_QtechWifiWlanAssociateStaMacAdress_Object = MibTableColumn
qtechWifiWlanAssociateStaMacAdress = _QtechWifiWlanAssociateStaMacAdress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 4, 1, 1, 2),
    _QtechWifiWlanAssociateStaMacAdress_Type()
)
qtechWifiWlanAssociateStaMacAdress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWifiWlanAssociateStaMacAdress.setStatus("current")
_QtechWifiWlanAssociateSsidName_Type = DisplayString
_QtechWifiWlanAssociateSsidName_Object = MibTableColumn
qtechWifiWlanAssociateSsidName = _QtechWifiWlanAssociateSsidName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 4, 1, 1, 3),
    _QtechWifiWlanAssociateSsidName_Type()
)
qtechWifiWlanAssociateSsidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWifiWlanAssociateSsidName.setStatus("current")
_QtechWifiWlanAssociateStaIpAdress_Type = IpAddress
_QtechWifiWlanAssociateStaIpAdress_Object = MibTableColumn
qtechWifiWlanAssociateStaIpAdress = _QtechWifiWlanAssociateStaIpAdress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 4, 1, 1, 4),
    _QtechWifiWlanAssociateStaIpAdress_Type()
)
qtechWifiWlanAssociateStaIpAdress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWifiWlanAssociateStaIpAdress.setStatus("current")
_QtechWifiWlanAssociateStaMaskAdress_Type = IpAddress
_QtechWifiWlanAssociateStaMaskAdress_Object = MibTableColumn
qtechWifiWlanAssociateStaMaskAdress = _QtechWifiWlanAssociateStaMaskAdress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 4, 1, 1, 5),
    _QtechWifiWlanAssociateStaMaskAdress_Type()
)
qtechWifiWlanAssociateStaMaskAdress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWifiWlanAssociateStaMaskAdress.setStatus("current")
_QtechWifiWlanAssociateStaSigalStrength_Type = Integer32
_QtechWifiWlanAssociateStaSigalStrength_Object = MibTableColumn
qtechWifiWlanAssociateStaSigalStrength = _QtechWifiWlanAssociateStaSigalStrength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 4, 1, 1, 6),
    _QtechWifiWlanAssociateStaSigalStrength_Type()
)
qtechWifiWlanAssociateStaSigalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWifiWlanAssociateStaSigalStrength.setStatus("current")
_QtechWifiWlanAssociateStaConnectTime_Type = DisplayString
_QtechWifiWlanAssociateStaConnectTime_Object = MibTableColumn
qtechWifiWlanAssociateStaConnectTime = _QtechWifiWlanAssociateStaConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 4, 1, 1, 7),
    _QtechWifiWlanAssociateStaConnectTime_Type()
)
qtechWifiWlanAssociateStaConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWifiWlanAssociateStaConnectTime.setStatus("current")
_QtechWifiWlanAssociateStaConnectTimeLength_Type = DisplayString
_QtechWifiWlanAssociateStaConnectTimeLength_Object = MibTableColumn
qtechWifiWlanAssociateStaConnectTimeLength = _QtechWifiWlanAssociateStaConnectTimeLength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 4, 1, 1, 8),
    _QtechWifiWlanAssociateStaConnectTimeLength_Type()
)
qtechWifiWlanAssociateStaConnectTimeLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWifiWlanAssociateStaConnectTimeLength.setStatus("current")
_QtechWifiWlanAssociateStaGate_Type = IpAddress
_QtechWifiWlanAssociateStaGate_Object = MibTableColumn
qtechWifiWlanAssociateStaGate = _QtechWifiWlanAssociateStaGate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 4, 1, 1, 9),
    _QtechWifiWlanAssociateStaGate_Type()
)
qtechWifiWlanAssociateStaGate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWifiWlanAssociateStaGate.setStatus("current")
_QtechWifiWlanAssociateStaDns_Type = IpAddress
_QtechWifiWlanAssociateStaDns_Object = MibTableColumn
qtechWifiWlanAssociateStaDns = _QtechWifiWlanAssociateStaDns_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 133, 1, 4, 1, 1, 10),
    _QtechWifiWlanAssociateStaDns_Type()
)
qtechWifiWlanAssociateStaDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWifiWlanAssociateStaDns.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-ROUTER-WIFI-MIB",
    **{"QtechEableType": QtechEableType,
       "QtechWlanType": QtechWlanType,
       "QtechIsolateType": QtechIsolateType,
       "QtechAuthenticationType": QtechAuthenticationType,
       "QtechWapPskCiphersType": QtechWapPskCiphersType,
       "QtechWifiChanWidthType": QtechWifiChanWidthType,
       "QtechWifiSlotType": QtechWifiSlotType,
       "QtechWifiFreChanelType": QtechWifiFreChanelType,
       "qtechWifiMIB": qtechWifiMIB,
       "qtechWifiMIBObjects": qtechWifiMIBObjects,
       "qtechWifiDot11radioSupportObjects": qtechWifiDot11radioSupportObjects,
       "qtechWifiDot11radioSupportTable": qtechWifiDot11radioSupportTable,
       "qtechWifiDot11radioSupportEntry": qtechWifiDot11radioSupportEntry,
       "qtechWifiDot11radioIndex": qtechWifiDot11radioIndex,
       "qtechWifiDot11radioApMaxCnt": qtechWifiDot11radioApMaxCnt,
       "qtechWifiDot11radioStationMaxCnt": qtechWifiDot11radioStationMaxCnt,
       "qtechWifiWlanObjects": qtechWifiWlanObjects,
       "qtechWifiWlanIndexNext": qtechWifiWlanIndexNext,
       "qtechWifiVlanIndexNext": qtechWifiVlanIndexNext,
       "qtechWifiWlanTable": qtechWifiWlanTable,
       "qtechWifiWlanEntry": qtechWifiWlanEntry,
       "qtechWifiWlanIndex": qtechWifiWlanIndex,
       "qtechWifiWlanType": qtechWifiWlanType,
       "qtechWifiWlanSsidName": qtechWifiWlanSsidName,
       "qtechWifiWlanVlanId": qtechWifiWlanVlanId,
       "qtechWifiWlanRowStatus": qtechWifiWlanRowStatus,
       "qtechWifiWlanBroadcastSsid": qtechWifiWlanBroadcastSsid,
       "qtechWifiWlanIsolate": qtechWifiWlanIsolate,
       "qtechWifiWlanBssStaLimit": qtechWifiWlanBssStaLimit,
       "rujieWifiWlanSecurityType": rujieWifiWlanSecurityType,
       "qtechWifiWlanAuthenticationSetKey": qtechWifiWlanAuthenticationSetKey,
       "qtechWifiWlanWepAuthenticationType": qtechWifiWlanWepAuthenticationType,
       "qtechWifiWlanWpaPskCiphersType": qtechWifiWlanWpaPskCiphersType,
       "qtechWifiWlanPassphrase": qtechWifiWlanPassphrase,
       "qtechWifiWlanDot11RadioIfindex": qtechWifiWlanDot11RadioIfindex,
       "qtechWifiWlanDot11RadioSubIfindex": qtechWifiWlanDot11RadioSubIfindex,
       "qtechWifiDot11radioIfConfigObjects": qtechWifiDot11radioIfConfigObjects,
       "qtechWifiDot11radioIfConfigTable": qtechWifiDot11radioIfConfigTable,
       "qtechWifiDot11radioIfConfigEntry": qtechWifiDot11radioIfConfigEntry,
       "qtechWifiDot11radioIfConfigIfIndex": qtechWifiDot11radioIfConfigIfIndex,
       "qtechWifiDot11radioIfConfigRowStatus": qtechWifiDot11radioIfConfigRowStatus,
       "qtechWifiDot11radioIfConfigFreBand": qtechWifiDot11radioIfConfigFreBand,
       "qtechWifiDot11radioIfConfigChannel": qtechWifiDot11radioIfConfigChannel,
       "qtechWifiDot11radioIfConfigChanWidth": qtechWifiDot11radioIfConfigChanWidth,
       "qtechWifiDot11radioIfConfigCountryCode": qtechWifiDot11radioIfConfigCountryCode,
       "qtechWifiDot11radioIfConfigPowerLocal": qtechWifiDot11radioIfConfigPowerLocal,
       "qtechWifiDot11radioIfConfigWirelessProSupport": qtechWifiDot11radioIfConfigWirelessProSupport,
       "qtechWifiDot11radioIfConfigStaLimit": qtechWifiDot11radioIfConfigStaLimit,
       "qtechWifiDot11radioIfConfig20ShortGiEnable": qtechWifiDot11radioIfConfig20ShortGiEnable,
       "qtechWifiDot11radioIfConfig40ShortGiEnable": qtechWifiDot11radioIfConfig40ShortGiEnable,
       "qtechWifiDot11radioIfConfigShortPreambleEnable": qtechWifiDot11radioIfConfigShortPreambleEnable,
       "qtechWifiDot11radioIfConfigSlottime": qtechWifiDot11radioIfConfigSlottime,
       "qtechWifiDot11radioIfConfigRtsThreshold": qtechWifiDot11radioIfConfigRtsThreshold,
       "qtechWifiDot11radioIfConfigFragmentThreshold": qtechWifiDot11radioIfConfigFragmentThreshold,
       "qtechWifiDot11radioIfConfigResponseRssi": qtechWifiDot11radioIfConfigResponseRssi,
       "qtechWifiDot11radioIfConfigEnableQos": qtechWifiDot11radioIfConfigEnableQos,
       "qtechWifiDot11radioIfConfigEdcaClientBgAifsn": qtechWifiDot11radioIfConfigEdcaClientBgAifsn,
       "qtechWifiDot11radioIfConfigEdcaClientBgCwmin": qtechWifiDot11radioIfConfigEdcaClientBgCwmin,
       "qtechWifiDot11radioIfConfigEdcaClientBgCwmax": qtechWifiDot11radioIfConfigEdcaClientBgCwmax,
       "qtechWifiDot11radioIfConfigEdcaClientBgTxop": qtechWifiDot11radioIfConfigEdcaClientBgTxop,
       "qtechWifiDot11radioIfConfigEdcaClientBeAifsn": qtechWifiDot11radioIfConfigEdcaClientBeAifsn,
       "qtechWifiDot11radioIfConfigEdcaClientBeCwmin": qtechWifiDot11radioIfConfigEdcaClientBeCwmin,
       "qtechWifiDot11radioIfConfigEdcaClientBeCwmax": qtechWifiDot11radioIfConfigEdcaClientBeCwmax,
       "qtechWifiDot11radioIfConfigEdcaClientBeTxop": qtechWifiDot11radioIfConfigEdcaClientBeTxop,
       "qtechWifiDot11radioIfConfigEdcaClientViAifsn": qtechWifiDot11radioIfConfigEdcaClientViAifsn,
       "qtechWifiDot11radioIfConfigEdcaClientViCwmin": qtechWifiDot11radioIfConfigEdcaClientViCwmin,
       "qtechWifiDot11radioIfConfigEdcaClientViCwmax": qtechWifiDot11radioIfConfigEdcaClientViCwmax,
       "qtechWifiDot11radioIfConfigEdcaClientViTxop": qtechWifiDot11radioIfConfigEdcaClientViTxop,
       "qtechWifiDot11radioIfConfigEdcaClientVoAifsn": qtechWifiDot11radioIfConfigEdcaClientVoAifsn,
       "qtechWifiDot11radioIfConfigEdcaClientVoCwmin": qtechWifiDot11radioIfConfigEdcaClientVoCwmin,
       "qtechWifiDot11radioIfConfigEdcaClientVoCwmax": qtechWifiDot11radioIfConfigEdcaClientVoCwmax,
       "qtechWifiDot11radioIfConfigEdcaClientVoTxop": qtechWifiDot11radioIfConfigEdcaClientVoTxop,
       "qtechWifiDot11radioIfConfigEdcaRadioBgAifsn": qtechWifiDot11radioIfConfigEdcaRadioBgAifsn,
       "qtechWifiDot11radioIfConfigEdcaRadioBgCwmin": qtechWifiDot11radioIfConfigEdcaRadioBgCwmin,
       "qtechWifiDot11radioIfConfigEdcaRadioBgCwmax": qtechWifiDot11radioIfConfigEdcaRadioBgCwmax,
       "qtechWifiDot11radioIfConfigEdcaRadioBgTxop": qtechWifiDot11radioIfConfigEdcaRadioBgTxop,
       "qtechWifiDot11radioIfConfigEdcaRadioBeAifsn": qtechWifiDot11radioIfConfigEdcaRadioBeAifsn,
       "qtechWifiDot11radioIfConfigEdcaRadioBeCwmin": qtechWifiDot11radioIfConfigEdcaRadioBeCwmin,
       "qtechWifiDot11radioIfConfigEdcaRadioBeCwmax": qtechWifiDot11radioIfConfigEdcaRadioBeCwmax,
       "qtechWifiDot11radioIfConfigEdcaRadioBeTxop": qtechWifiDot11radioIfConfigEdcaRadioBeTxop,
       "qtechWifiDot11radioIfConfigEdcaRadioViAifsn": qtechWifiDot11radioIfConfigEdcaRadioViAifsn,
       "qtechWifiDot11radioIfConfigEdcaRadioViCwmin": qtechWifiDot11radioIfConfigEdcaRadioViCwmin,
       "qtechWifiDot11radioIfConfigEdcaRadioViCwmax": qtechWifiDot11radioIfConfigEdcaRadioViCwmax,
       "qtechWifiDot11radioIfConfigEdcaRadioViTxop": qtechWifiDot11radioIfConfigEdcaRadioViTxop,
       "qtechWifiDot11radioIfConfigEdcaRadioVoAifsn": qtechWifiDot11radioIfConfigEdcaRadioVoAifsn,
       "qtechWifiDot11radioIfConfigEdcaRadioVoCwmin": qtechWifiDot11radioIfConfigEdcaRadioVoCwmin,
       "qtechWifiDot11radioIfConfigEdcaRadioVoCwmax": qtechWifiDot11radioIfConfigEdcaRadioVoCwmax,
       "qtechWifiDot11radioIfConfigEdcaRadioVoTxop": qtechWifiDot11radioIfConfigEdcaRadioVoTxop,
       "qtechWifiDot11radioIfConfigAntennaTransChainmask": qtechWifiDot11radioIfConfigAntennaTransChainmask,
       "qtechWifiDot11radioIfConfigAntennaReceiveChainmask": qtechWifiDot11radioIfConfigAntennaReceiveChainmask,
       "qtechWifiDot11radioIfConfigBeaconDtimPeriod": qtechWifiDot11radioIfConfigBeaconDtimPeriod,
       "qtechWifiDot11radioIfConfigBeaconPeriod": qtechWifiDot11radioIfConfigBeaconPeriod,
       "qtechWifiDot11radioIfConfigRetrieShortTime": qtechWifiDot11radioIfConfigRetrieShortTime,
       "qtechWifiDot11radioIfConfigRetrieLongTime": qtechWifiDot11radioIfConfigRetrieLongTime,
       "qtechWifiDot11radioIfConfigStaIdleTimeout": qtechWifiDot11radioIfConfigStaIdleTimeout,
       "qtechWifiDot11radioIfConfigWlanIdList": qtechWifiDot11radioIfConfigWlanIdList,
       "qtechWifiWlanAssociateObjects": qtechWifiWlanAssociateObjects,
       "qtechWifiWlanAssociateTable": qtechWifiWlanAssociateTable,
       "qtechWifiWlanAssociateEntry": qtechWifiWlanAssociateEntry,
       "qtechWifiWlanAssociateWlanId": qtechWifiWlanAssociateWlanId,
       "qtechWifiWlanAssociateStaMacAdress": qtechWifiWlanAssociateStaMacAdress,
       "qtechWifiWlanAssociateSsidName": qtechWifiWlanAssociateSsidName,
       "qtechWifiWlanAssociateStaIpAdress": qtechWifiWlanAssociateStaIpAdress,
       "qtechWifiWlanAssociateStaMaskAdress": qtechWifiWlanAssociateStaMaskAdress,
       "qtechWifiWlanAssociateStaSigalStrength": qtechWifiWlanAssociateStaSigalStrength,
       "qtechWifiWlanAssociateStaConnectTime": qtechWifiWlanAssociateStaConnectTime,
       "qtechWifiWlanAssociateStaConnectTimeLength": qtechWifiWlanAssociateStaConnectTimeLength,
       "qtechWifiWlanAssociateStaGate": qtechWifiWlanAssociateStaGate,
       "qtechWifiWlanAssociateStaDns": qtechWifiWlanAssociateStaDns}
)
