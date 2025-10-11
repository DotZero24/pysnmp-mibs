# SNMP MIB module (FS-ROUTER-WIFI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-ROUTER-WIFI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:28 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

fsWifiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133)
)
if mibBuilder.loadTexts:
    fsWifiMIB.setRevisions(
        ("2014-12-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FSEableType(TextualConvention, Integer32):
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



class FSWlanType(TextualConvention, Integer32):
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



class FSIsolateType(TextualConvention, Integer32):
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



class FSAuthenticationType(TextualConvention, Integer32):
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



class FSWapPskCiphersType(TextualConvention, Integer32):
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



class FSWifiChanWidthType(TextualConvention, Integer32):
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



class FSWifiSlotType(TextualConvention, Integer32):
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



class FSWifiFreChanelType(TextualConvention, Integer32):
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

_FsWifiMIBObjects_ObjectIdentity = ObjectIdentity
fsWifiMIBObjects = _FsWifiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1)
)
_FsWifiDot11radioSupportObjects_ObjectIdentity = ObjectIdentity
fsWifiDot11radioSupportObjects = _FsWifiDot11radioSupportObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 1)
)
_FsWifiDot11radioSupportTable_Object = MibTable
fsWifiDot11radioSupportTable = _FsWifiDot11radioSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsWifiDot11radioSupportTable.setStatus("current")
_FsWifiDot11radioSupportEntry_Object = MibTableRow
fsWifiDot11radioSupportEntry = _FsWifiDot11radioSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 1, 1, 1)
)
fsWifiDot11radioSupportEntry.setIndexNames(
    (0, "FS-ROUTER-WIFI-MIB", "fsWifiDot11radioIndex"),
)
if mibBuilder.loadTexts:
    fsWifiDot11radioSupportEntry.setStatus("current")
_FsWifiDot11radioIndex_Type = Integer32
_FsWifiDot11radioIndex_Object = MibTableColumn
fsWifiDot11radioIndex = _FsWifiDot11radioIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 1, 1, 1, 1),
    _FsWifiDot11radioIndex_Type()
)
fsWifiDot11radioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWifiDot11radioIndex.setStatus("current")
_FsWifiDot11radioApMaxCnt_Type = Integer32
_FsWifiDot11radioApMaxCnt_Object = MibTableColumn
fsWifiDot11radioApMaxCnt = _FsWifiDot11radioApMaxCnt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 1, 1, 1, 2),
    _FsWifiDot11radioApMaxCnt_Type()
)
fsWifiDot11radioApMaxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWifiDot11radioApMaxCnt.setStatus("current")
_FsWifiDot11radioStationMaxCnt_Type = Integer32
_FsWifiDot11radioStationMaxCnt_Object = MibTableColumn
fsWifiDot11radioStationMaxCnt = _FsWifiDot11radioStationMaxCnt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 1, 1, 1, 3),
    _FsWifiDot11radioStationMaxCnt_Type()
)
fsWifiDot11radioStationMaxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWifiDot11radioStationMaxCnt.setStatus("current")
_FsWifiWlanObjects_ObjectIdentity = ObjectIdentity
fsWifiWlanObjects = _FsWifiWlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 2)
)
_FsWifiWlanIndexNext_Type = Integer32
_FsWifiWlanIndexNext_Object = MibScalar
fsWifiWlanIndexNext = _FsWifiWlanIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 2, 1),
    _FsWifiWlanIndexNext_Type()
)
fsWifiWlanIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWifiWlanIndexNext.setStatus("current")
_FsWifiVlanIndexNext_Type = Integer32
_FsWifiVlanIndexNext_Object = MibScalar
fsWifiVlanIndexNext = _FsWifiVlanIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 2, 2),
    _FsWifiVlanIndexNext_Type()
)
fsWifiVlanIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWifiVlanIndexNext.setStatus("current")
_FsWifiWlanTable_Object = MibTable
fsWifiWlanTable = _FsWifiWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fsWifiWlanTable.setStatus("current")
_FsWifiWlanEntry_Object = MibTableRow
fsWifiWlanEntry = _FsWifiWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 2, 3, 1)
)
fsWifiWlanEntry.setIndexNames(
    (0, "FS-ROUTER-WIFI-MIB", "fsWifiWlanIndex"),
)
if mibBuilder.loadTexts:
    fsWifiWlanEntry.setStatus("current")


class _FsWifiWlanIndex_Type(Integer32):
    """Custom type fsWifiWlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiWlanIndex_Type.__name__ = "Integer32"
_FsWifiWlanIndex_Object = MibTableColumn
fsWifiWlanIndex = _FsWifiWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 2, 3, 1, 1),
    _FsWifiWlanIndex_Type()
)
fsWifiWlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWifiWlanIndex.setStatus("current")
_FsWifiWlanType_Type = FSWlanType
_FsWifiWlanType_Object = MibTableColumn
fsWifiWlanType = _FsWifiWlanType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 2, 3, 1, 2),
    _FsWifiWlanType_Type()
)
fsWifiWlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiWlanType.setStatus("current")


class _FsWifiWlanSsidName_Type(DisplayString):
    """Custom type fsWifiWlanSsidName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsWifiWlanSsidName_Type.__name__ = "DisplayString"
_FsWifiWlanSsidName_Object = MibTableColumn
fsWifiWlanSsidName = _FsWifiWlanSsidName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 2, 3, 1, 3),
    _FsWifiWlanSsidName_Type()
)
fsWifiWlanSsidName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiWlanSsidName.setStatus("current")


class _FsWifiWlanVlanId_Type(Integer32):
    """Custom type fsWifiWlanVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_FsWifiWlanVlanId_Type.__name__ = "Integer32"
_FsWifiWlanVlanId_Object = MibTableColumn
fsWifiWlanVlanId = _FsWifiWlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 2, 3, 1, 4),
    _FsWifiWlanVlanId_Type()
)
fsWifiWlanVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiWlanVlanId.setStatus("current")
_FsWifiWlanRowStatus_Type = RowStatus
_FsWifiWlanRowStatus_Object = MibTableColumn
fsWifiWlanRowStatus = _FsWifiWlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 2, 3, 1, 5),
    _FsWifiWlanRowStatus_Type()
)
fsWifiWlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiWlanRowStatus.setStatus("current")
_FsWifiWlanBroadcastSsid_Type = FSEableType
_FsWifiWlanBroadcastSsid_Object = MibTableColumn
fsWifiWlanBroadcastSsid = _FsWifiWlanBroadcastSsid_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 2, 3, 1, 6),
    _FsWifiWlanBroadcastSsid_Type()
)
fsWifiWlanBroadcastSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiWlanBroadcastSsid.setStatus("current")
_FsWifiWlanIsolate_Type = FSIsolateType
_FsWifiWlanIsolate_Object = MibTableColumn
fsWifiWlanIsolate = _FsWifiWlanIsolate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 2, 3, 1, 7),
    _FsWifiWlanIsolate_Type()
)
fsWifiWlanIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiWlanIsolate.setStatus("current")
_FsWifiWlanBssStaLimit_Type = Integer32
_FsWifiWlanBssStaLimit_Object = MibTableColumn
fsWifiWlanBssStaLimit = _FsWifiWlanBssStaLimit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 2, 3, 1, 8),
    _FsWifiWlanBssStaLimit_Type()
)
fsWifiWlanBssStaLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiWlanBssStaLimit.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 2, 3, 1, 9),
    _RujieWifiWlanSecurityType_Type()
)
rujieWifiWlanSecurityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rujieWifiWlanSecurityType.setStatus("current")
_FsWifiWlanAuthenticationSetKey_Type = DisplayString
_FsWifiWlanAuthenticationSetKey_Object = MibTableColumn
fsWifiWlanAuthenticationSetKey = _FsWifiWlanAuthenticationSetKey_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 2, 3, 1, 10),
    _FsWifiWlanAuthenticationSetKey_Type()
)
fsWifiWlanAuthenticationSetKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiWlanAuthenticationSetKey.setStatus("current")
_FsWifiWlanWepAuthenticationType_Type = FSAuthenticationType
_FsWifiWlanWepAuthenticationType_Object = MibTableColumn
fsWifiWlanWepAuthenticationType = _FsWifiWlanWepAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 2, 3, 1, 11),
    _FsWifiWlanWepAuthenticationType_Type()
)
fsWifiWlanWepAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiWlanWepAuthenticationType.setStatus("current")
_FsWifiWlanWpaPskCiphersType_Type = FSWapPskCiphersType
_FsWifiWlanWpaPskCiphersType_Object = MibTableColumn
fsWifiWlanWpaPskCiphersType = _FsWifiWlanWpaPskCiphersType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 2, 3, 1, 12),
    _FsWifiWlanWpaPskCiphersType_Type()
)
fsWifiWlanWpaPskCiphersType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiWlanWpaPskCiphersType.setStatus("current")
_FsWifiWlanPassphrase_Type = DisplayString
_FsWifiWlanPassphrase_Object = MibTableColumn
fsWifiWlanPassphrase = _FsWifiWlanPassphrase_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 2, 3, 1, 13),
    _FsWifiWlanPassphrase_Type()
)
fsWifiWlanPassphrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiWlanPassphrase.setStatus("current")
_FsWifiWlanDot11RadioIfindex_Type = Integer32
_FsWifiWlanDot11RadioIfindex_Object = MibTableColumn
fsWifiWlanDot11RadioIfindex = _FsWifiWlanDot11RadioIfindex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 2, 3, 1, 14),
    _FsWifiWlanDot11RadioIfindex_Type()
)
fsWifiWlanDot11RadioIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWifiWlanDot11RadioIfindex.setStatus("current")
_FsWifiWlanDot11RadioSubIfindex_Type = Integer32
_FsWifiWlanDot11RadioSubIfindex_Object = MibTableColumn
fsWifiWlanDot11RadioSubIfindex = _FsWifiWlanDot11RadioSubIfindex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 2, 3, 1, 15),
    _FsWifiWlanDot11RadioSubIfindex_Type()
)
fsWifiWlanDot11RadioSubIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWifiWlanDot11RadioSubIfindex.setStatus("current")
_FsWifiDot11radioIfConfigObjects_ObjectIdentity = ObjectIdentity
fsWifiDot11radioIfConfigObjects = _FsWifiDot11radioIfConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3)
)
_FsWifiDot11radioIfConfigTable_Object = MibTable
fsWifiDot11radioIfConfigTable = _FsWifiDot11radioIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigTable.setStatus("current")
_FsWifiDot11radioIfConfigEntry_Object = MibTableRow
fsWifiDot11radioIfConfigEntry = _FsWifiDot11radioIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1)
)
fsWifiDot11radioIfConfigEntry.setIndexNames(
    (0, "FS-ROUTER-WIFI-MIB", "fsWifiDot11radioIfConfigIfIndex"),
)
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEntry.setStatus("current")
_FsWifiDot11radioIfConfigIfIndex_Type = Integer32
_FsWifiDot11radioIfConfigIfIndex_Object = MibTableColumn
fsWifiDot11radioIfConfigIfIndex = _FsWifiDot11radioIfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 1),
    _FsWifiDot11radioIfConfigIfIndex_Type()
)
fsWifiDot11radioIfConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigIfIndex.setStatus("current")
_FsWifiDot11radioIfConfigRowStatus_Type = RowStatus
_FsWifiDot11radioIfConfigRowStatus_Object = MibTableColumn
fsWifiDot11radioIfConfigRowStatus = _FsWifiDot11radioIfConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 2),
    _FsWifiDot11radioIfConfigRowStatus_Type()
)
fsWifiDot11radioIfConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigRowStatus.setStatus("current")
_FsWifiDot11radioIfConfigFreBand_Type = FSWifiFreChanelType
_FsWifiDot11radioIfConfigFreBand_Object = MibTableColumn
fsWifiDot11radioIfConfigFreBand = _FsWifiDot11radioIfConfigFreBand_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 3),
    _FsWifiDot11radioIfConfigFreBand_Type()
)
fsWifiDot11radioIfConfigFreBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigFreBand.setStatus("current")
_FsWifiDot11radioIfConfigChannel_Type = Integer32
_FsWifiDot11radioIfConfigChannel_Object = MibTableColumn
fsWifiDot11radioIfConfigChannel = _FsWifiDot11radioIfConfigChannel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 4),
    _FsWifiDot11radioIfConfigChannel_Type()
)
fsWifiDot11radioIfConfigChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigChannel.setStatus("current")
_FsWifiDot11radioIfConfigChanWidth_Type = FSWifiChanWidthType
_FsWifiDot11radioIfConfigChanWidth_Object = MibTableColumn
fsWifiDot11radioIfConfigChanWidth = _FsWifiDot11radioIfConfigChanWidth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 5),
    _FsWifiDot11radioIfConfigChanWidth_Type()
)
fsWifiDot11radioIfConfigChanWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigChanWidth.setStatus("current")
_FsWifiDot11radioIfConfigCountryCode_Type = DisplayString
_FsWifiDot11radioIfConfigCountryCode_Object = MibTableColumn
fsWifiDot11radioIfConfigCountryCode = _FsWifiDot11radioIfConfigCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 6),
    _FsWifiDot11radioIfConfigCountryCode_Type()
)
fsWifiDot11radioIfConfigCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigCountryCode.setStatus("current")


class _FsWifiDot11radioIfConfigPowerLocal_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigPowerLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsWifiDot11radioIfConfigPowerLocal_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigPowerLocal_Object = MibTableColumn
fsWifiDot11radioIfConfigPowerLocal = _FsWifiDot11radioIfConfigPowerLocal_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 7),
    _FsWifiDot11radioIfConfigPowerLocal_Type()
)
fsWifiDot11radioIfConfigPowerLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigPowerLocal.setStatus("current")


class _FsWifiDot11radioIfConfigWirelessProSupport_Type(Bits):
    """Custom type fsWifiDot11radioIfConfigWirelessProSupport based on Bits"""
    namedValues = NamedValues(
        *(("null", 0),
          ("b", 1),
          ("g", 2),
          ("n", 3))
    )

_FsWifiDot11radioIfConfigWirelessProSupport_Type.__name__ = "Bits"
_FsWifiDot11radioIfConfigWirelessProSupport_Object = MibTableColumn
fsWifiDot11radioIfConfigWirelessProSupport = _FsWifiDot11radioIfConfigWirelessProSupport_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 8),
    _FsWifiDot11radioIfConfigWirelessProSupport_Type()
)
fsWifiDot11radioIfConfigWirelessProSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigWirelessProSupport.setStatus("current")


class _FsWifiDot11radioIfConfigStaLimit_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigStaLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_FsWifiDot11radioIfConfigStaLimit_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigStaLimit_Object = MibTableColumn
fsWifiDot11radioIfConfigStaLimit = _FsWifiDot11radioIfConfigStaLimit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 9),
    _FsWifiDot11radioIfConfigStaLimit_Type()
)
fsWifiDot11radioIfConfigStaLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigStaLimit.setStatus("current")
_FsWifiDot11radioIfConfig20ShortGiEnable_Type = FSEableType
_FsWifiDot11radioIfConfig20ShortGiEnable_Object = MibTableColumn
fsWifiDot11radioIfConfig20ShortGiEnable = _FsWifiDot11radioIfConfig20ShortGiEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 10),
    _FsWifiDot11radioIfConfig20ShortGiEnable_Type()
)
fsWifiDot11radioIfConfig20ShortGiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfig20ShortGiEnable.setStatus("current")
_FsWifiDot11radioIfConfig40ShortGiEnable_Type = FSEableType
_FsWifiDot11radioIfConfig40ShortGiEnable_Object = MibTableColumn
fsWifiDot11radioIfConfig40ShortGiEnable = _FsWifiDot11radioIfConfig40ShortGiEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 11),
    _FsWifiDot11radioIfConfig40ShortGiEnable_Type()
)
fsWifiDot11radioIfConfig40ShortGiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfig40ShortGiEnable.setStatus("current")
_FsWifiDot11radioIfConfigShortPreambleEnable_Type = FSEableType
_FsWifiDot11radioIfConfigShortPreambleEnable_Object = MibTableColumn
fsWifiDot11radioIfConfigShortPreambleEnable = _FsWifiDot11radioIfConfigShortPreambleEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 12),
    _FsWifiDot11radioIfConfigShortPreambleEnable_Type()
)
fsWifiDot11radioIfConfigShortPreambleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigShortPreambleEnable.setStatus("current")
_FsWifiDot11radioIfConfigSlottime_Type = FSWifiSlotType
_FsWifiDot11radioIfConfigSlottime_Object = MibTableColumn
fsWifiDot11radioIfConfigSlottime = _FsWifiDot11radioIfConfigSlottime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 13),
    _FsWifiDot11radioIfConfigSlottime_Type()
)
fsWifiDot11radioIfConfigSlottime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigSlottime.setStatus("current")


class _FsWifiDot11radioIfConfigRtsThreshold_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigRtsThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(257, 2347),
    )


_FsWifiDot11radioIfConfigRtsThreshold_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigRtsThreshold_Object = MibTableColumn
fsWifiDot11radioIfConfigRtsThreshold = _FsWifiDot11radioIfConfigRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 14),
    _FsWifiDot11radioIfConfigRtsThreshold_Type()
)
fsWifiDot11radioIfConfigRtsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigRtsThreshold.setStatus("current")


class _FsWifiDot11radioIfConfigFragmentThreshold_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigFragmentThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_FsWifiDot11radioIfConfigFragmentThreshold_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigFragmentThreshold_Object = MibTableColumn
fsWifiDot11radioIfConfigFragmentThreshold = _FsWifiDot11radioIfConfigFragmentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 15),
    _FsWifiDot11radioIfConfigFragmentThreshold_Type()
)
fsWifiDot11radioIfConfigFragmentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigFragmentThreshold.setStatus("current")


class _FsWifiDot11radioIfConfigResponseRssi_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigResponseRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsWifiDot11radioIfConfigResponseRssi_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigResponseRssi_Object = MibTableColumn
fsWifiDot11radioIfConfigResponseRssi = _FsWifiDot11radioIfConfigResponseRssi_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 16),
    _FsWifiDot11radioIfConfigResponseRssi_Type()
)
fsWifiDot11radioIfConfigResponseRssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigResponseRssi.setStatus("current")
_FsWifiDot11radioIfConfigEnableQos_Type = FSEableType
_FsWifiDot11radioIfConfigEnableQos_Object = MibTableColumn
fsWifiDot11radioIfConfigEnableQos = _FsWifiDot11radioIfConfigEnableQos_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 17),
    _FsWifiDot11radioIfConfigEnableQos_Type()
)
fsWifiDot11radioIfConfigEnableQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEnableQos.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaClientBgAifsn_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaClientBgAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaClientBgAifsn_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaClientBgAifsn_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaClientBgAifsn = _FsWifiDot11radioIfConfigEdcaClientBgAifsn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 18),
    _FsWifiDot11radioIfConfigEdcaClientBgAifsn_Type()
)
fsWifiDot11radioIfConfigEdcaClientBgAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaClientBgAifsn.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaClientBgCwmin_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaClientBgCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaClientBgCwmin_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaClientBgCwmin_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaClientBgCwmin = _FsWifiDot11radioIfConfigEdcaClientBgCwmin_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 19),
    _FsWifiDot11radioIfConfigEdcaClientBgCwmin_Type()
)
fsWifiDot11radioIfConfigEdcaClientBgCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaClientBgCwmin.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaClientBgCwmax_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaClientBgCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaClientBgCwmax_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaClientBgCwmax_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaClientBgCwmax = _FsWifiDot11radioIfConfigEdcaClientBgCwmax_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 20),
    _FsWifiDot11radioIfConfigEdcaClientBgCwmax_Type()
)
fsWifiDot11radioIfConfigEdcaClientBgCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaClientBgCwmax.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaClientBgTxop_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaClientBgTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsWifiDot11radioIfConfigEdcaClientBgTxop_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaClientBgTxop_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaClientBgTxop = _FsWifiDot11radioIfConfigEdcaClientBgTxop_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 21),
    _FsWifiDot11radioIfConfigEdcaClientBgTxop_Type()
)
fsWifiDot11radioIfConfigEdcaClientBgTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaClientBgTxop.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaClientBeAifsn_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaClientBeAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaClientBeAifsn_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaClientBeAifsn_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaClientBeAifsn = _FsWifiDot11radioIfConfigEdcaClientBeAifsn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 22),
    _FsWifiDot11radioIfConfigEdcaClientBeAifsn_Type()
)
fsWifiDot11radioIfConfigEdcaClientBeAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaClientBeAifsn.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaClientBeCwmin_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaClientBeCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaClientBeCwmin_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaClientBeCwmin_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaClientBeCwmin = _FsWifiDot11radioIfConfigEdcaClientBeCwmin_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 23),
    _FsWifiDot11radioIfConfigEdcaClientBeCwmin_Type()
)
fsWifiDot11radioIfConfigEdcaClientBeCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaClientBeCwmin.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaClientBeCwmax_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaClientBeCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaClientBeCwmax_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaClientBeCwmax_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaClientBeCwmax = _FsWifiDot11radioIfConfigEdcaClientBeCwmax_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 24),
    _FsWifiDot11radioIfConfigEdcaClientBeCwmax_Type()
)
fsWifiDot11radioIfConfigEdcaClientBeCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaClientBeCwmax.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaClientBeTxop_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaClientBeTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsWifiDot11radioIfConfigEdcaClientBeTxop_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaClientBeTxop_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaClientBeTxop = _FsWifiDot11radioIfConfigEdcaClientBeTxop_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 25),
    _FsWifiDot11radioIfConfigEdcaClientBeTxop_Type()
)
fsWifiDot11radioIfConfigEdcaClientBeTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaClientBeTxop.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaClientViAifsn_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaClientViAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaClientViAifsn_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaClientViAifsn_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaClientViAifsn = _FsWifiDot11radioIfConfigEdcaClientViAifsn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 26),
    _FsWifiDot11radioIfConfigEdcaClientViAifsn_Type()
)
fsWifiDot11radioIfConfigEdcaClientViAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaClientViAifsn.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaClientViCwmin_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaClientViCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaClientViCwmin_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaClientViCwmin_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaClientViCwmin = _FsWifiDot11radioIfConfigEdcaClientViCwmin_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 27),
    _FsWifiDot11radioIfConfigEdcaClientViCwmin_Type()
)
fsWifiDot11radioIfConfigEdcaClientViCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaClientViCwmin.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaClientViCwmax_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaClientViCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaClientViCwmax_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaClientViCwmax_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaClientViCwmax = _FsWifiDot11radioIfConfigEdcaClientViCwmax_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 28),
    _FsWifiDot11radioIfConfigEdcaClientViCwmax_Type()
)
fsWifiDot11radioIfConfigEdcaClientViCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaClientViCwmax.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaClientViTxop_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaClientViTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsWifiDot11radioIfConfigEdcaClientViTxop_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaClientViTxop_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaClientViTxop = _FsWifiDot11radioIfConfigEdcaClientViTxop_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 29),
    _FsWifiDot11radioIfConfigEdcaClientViTxop_Type()
)
fsWifiDot11radioIfConfigEdcaClientViTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaClientViTxop.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaClientVoAifsn_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaClientVoAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaClientVoAifsn_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaClientVoAifsn_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaClientVoAifsn = _FsWifiDot11radioIfConfigEdcaClientVoAifsn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 30),
    _FsWifiDot11radioIfConfigEdcaClientVoAifsn_Type()
)
fsWifiDot11radioIfConfigEdcaClientVoAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaClientVoAifsn.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaClientVoCwmin_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaClientVoCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaClientVoCwmin_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaClientVoCwmin_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaClientVoCwmin = _FsWifiDot11radioIfConfigEdcaClientVoCwmin_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 31),
    _FsWifiDot11radioIfConfigEdcaClientVoCwmin_Type()
)
fsWifiDot11radioIfConfigEdcaClientVoCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaClientVoCwmin.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaClientVoCwmax_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaClientVoCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaClientVoCwmax_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaClientVoCwmax_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaClientVoCwmax = _FsWifiDot11radioIfConfigEdcaClientVoCwmax_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 32),
    _FsWifiDot11radioIfConfigEdcaClientVoCwmax_Type()
)
fsWifiDot11radioIfConfigEdcaClientVoCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaClientVoCwmax.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaClientVoTxop_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaClientVoTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsWifiDot11radioIfConfigEdcaClientVoTxop_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaClientVoTxop_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaClientVoTxop = _FsWifiDot11radioIfConfigEdcaClientVoTxop_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 33),
    _FsWifiDot11radioIfConfigEdcaClientVoTxop_Type()
)
fsWifiDot11radioIfConfigEdcaClientVoTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaClientVoTxop.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaRadioBgAifsn_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaRadioBgAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaRadioBgAifsn_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaRadioBgAifsn_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaRadioBgAifsn = _FsWifiDot11radioIfConfigEdcaRadioBgAifsn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 34),
    _FsWifiDot11radioIfConfigEdcaRadioBgAifsn_Type()
)
fsWifiDot11radioIfConfigEdcaRadioBgAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaRadioBgAifsn.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaRadioBgCwmin_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaRadioBgCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaRadioBgCwmin_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaRadioBgCwmin_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaRadioBgCwmin = _FsWifiDot11radioIfConfigEdcaRadioBgCwmin_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 35),
    _FsWifiDot11radioIfConfigEdcaRadioBgCwmin_Type()
)
fsWifiDot11radioIfConfigEdcaRadioBgCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaRadioBgCwmin.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaRadioBgCwmax_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaRadioBgCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaRadioBgCwmax_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaRadioBgCwmax_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaRadioBgCwmax = _FsWifiDot11radioIfConfigEdcaRadioBgCwmax_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 36),
    _FsWifiDot11radioIfConfigEdcaRadioBgCwmax_Type()
)
fsWifiDot11radioIfConfigEdcaRadioBgCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaRadioBgCwmax.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaRadioBgTxop_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaRadioBgTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsWifiDot11radioIfConfigEdcaRadioBgTxop_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaRadioBgTxop_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaRadioBgTxop = _FsWifiDot11radioIfConfigEdcaRadioBgTxop_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 37),
    _FsWifiDot11radioIfConfigEdcaRadioBgTxop_Type()
)
fsWifiDot11radioIfConfigEdcaRadioBgTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaRadioBgTxop.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaRadioBeAifsn_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaRadioBeAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaRadioBeAifsn_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaRadioBeAifsn_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaRadioBeAifsn = _FsWifiDot11radioIfConfigEdcaRadioBeAifsn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 38),
    _FsWifiDot11radioIfConfigEdcaRadioBeAifsn_Type()
)
fsWifiDot11radioIfConfigEdcaRadioBeAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaRadioBeAifsn.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaRadioBeCwmin_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaRadioBeCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaRadioBeCwmin_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaRadioBeCwmin_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaRadioBeCwmin = _FsWifiDot11radioIfConfigEdcaRadioBeCwmin_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 39),
    _FsWifiDot11radioIfConfigEdcaRadioBeCwmin_Type()
)
fsWifiDot11radioIfConfigEdcaRadioBeCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaRadioBeCwmin.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaRadioBeCwmax_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaRadioBeCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaRadioBeCwmax_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaRadioBeCwmax_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaRadioBeCwmax = _FsWifiDot11radioIfConfigEdcaRadioBeCwmax_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 40),
    _FsWifiDot11radioIfConfigEdcaRadioBeCwmax_Type()
)
fsWifiDot11radioIfConfigEdcaRadioBeCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaRadioBeCwmax.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaRadioBeTxop_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaRadioBeTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsWifiDot11radioIfConfigEdcaRadioBeTxop_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaRadioBeTxop_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaRadioBeTxop = _FsWifiDot11radioIfConfigEdcaRadioBeTxop_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 41),
    _FsWifiDot11radioIfConfigEdcaRadioBeTxop_Type()
)
fsWifiDot11radioIfConfigEdcaRadioBeTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaRadioBeTxop.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaRadioViAifsn_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaRadioViAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaRadioViAifsn_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaRadioViAifsn_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaRadioViAifsn = _FsWifiDot11radioIfConfigEdcaRadioViAifsn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 42),
    _FsWifiDot11radioIfConfigEdcaRadioViAifsn_Type()
)
fsWifiDot11radioIfConfigEdcaRadioViAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaRadioViAifsn.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaRadioViCwmin_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaRadioViCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaRadioViCwmin_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaRadioViCwmin_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaRadioViCwmin = _FsWifiDot11radioIfConfigEdcaRadioViCwmin_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 43),
    _FsWifiDot11radioIfConfigEdcaRadioViCwmin_Type()
)
fsWifiDot11radioIfConfigEdcaRadioViCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaRadioViCwmin.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaRadioViCwmax_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaRadioViCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaRadioViCwmax_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaRadioViCwmax_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaRadioViCwmax = _FsWifiDot11radioIfConfigEdcaRadioViCwmax_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 44),
    _FsWifiDot11radioIfConfigEdcaRadioViCwmax_Type()
)
fsWifiDot11radioIfConfigEdcaRadioViCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaRadioViCwmax.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaRadioViTxop_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaRadioViTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsWifiDot11radioIfConfigEdcaRadioViTxop_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaRadioViTxop_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaRadioViTxop = _FsWifiDot11radioIfConfigEdcaRadioViTxop_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 45),
    _FsWifiDot11radioIfConfigEdcaRadioViTxop_Type()
)
fsWifiDot11radioIfConfigEdcaRadioViTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaRadioViTxop.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaRadioVoAifsn_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaRadioVoAifsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaRadioVoAifsn_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaRadioVoAifsn_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaRadioVoAifsn = _FsWifiDot11radioIfConfigEdcaRadioVoAifsn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 46),
    _FsWifiDot11radioIfConfigEdcaRadioVoAifsn_Type()
)
fsWifiDot11radioIfConfigEdcaRadioVoAifsn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaRadioVoAifsn.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaRadioVoCwmin_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaRadioVoCwmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaRadioVoCwmin_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaRadioVoCwmin_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaRadioVoCwmin = _FsWifiDot11radioIfConfigEdcaRadioVoCwmin_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 47),
    _FsWifiDot11radioIfConfigEdcaRadioVoCwmin_Type()
)
fsWifiDot11radioIfConfigEdcaRadioVoCwmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaRadioVoCwmin.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaRadioVoCwmax_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaRadioVoCwmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsWifiDot11radioIfConfigEdcaRadioVoCwmax_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaRadioVoCwmax_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaRadioVoCwmax = _FsWifiDot11radioIfConfigEdcaRadioVoCwmax_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 48),
    _FsWifiDot11radioIfConfigEdcaRadioVoCwmax_Type()
)
fsWifiDot11radioIfConfigEdcaRadioVoCwmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaRadioVoCwmax.setStatus("current")


class _FsWifiDot11radioIfConfigEdcaRadioVoTxop_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigEdcaRadioVoTxop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsWifiDot11radioIfConfigEdcaRadioVoTxop_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigEdcaRadioVoTxop_Object = MibTableColumn
fsWifiDot11radioIfConfigEdcaRadioVoTxop = _FsWifiDot11radioIfConfigEdcaRadioVoTxop_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 49),
    _FsWifiDot11radioIfConfigEdcaRadioVoTxop_Type()
)
fsWifiDot11radioIfConfigEdcaRadioVoTxop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigEdcaRadioVoTxop.setStatus("current")


class _FsWifiDot11radioIfConfigAntennaTransChainmask_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigAntennaTransChainmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsWifiDot11radioIfConfigAntennaTransChainmask_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigAntennaTransChainmask_Object = MibTableColumn
fsWifiDot11radioIfConfigAntennaTransChainmask = _FsWifiDot11radioIfConfigAntennaTransChainmask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 50),
    _FsWifiDot11radioIfConfigAntennaTransChainmask_Type()
)
fsWifiDot11radioIfConfigAntennaTransChainmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigAntennaTransChainmask.setStatus("current")


class _FsWifiDot11radioIfConfigAntennaReceiveChainmask_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigAntennaReceiveChainmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsWifiDot11radioIfConfigAntennaReceiveChainmask_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigAntennaReceiveChainmask_Object = MibTableColumn
fsWifiDot11radioIfConfigAntennaReceiveChainmask = _FsWifiDot11radioIfConfigAntennaReceiveChainmask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 51),
    _FsWifiDot11radioIfConfigAntennaReceiveChainmask_Type()
)
fsWifiDot11radioIfConfigAntennaReceiveChainmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigAntennaReceiveChainmask.setStatus("current")


class _FsWifiDot11radioIfConfigBeaconDtimPeriod_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigBeaconDtimPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsWifiDot11radioIfConfigBeaconDtimPeriod_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigBeaconDtimPeriod_Object = MibTableColumn
fsWifiDot11radioIfConfigBeaconDtimPeriod = _FsWifiDot11radioIfConfigBeaconDtimPeriod_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 52),
    _FsWifiDot11radioIfConfigBeaconDtimPeriod_Type()
)
fsWifiDot11radioIfConfigBeaconDtimPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigBeaconDtimPeriod.setStatus("current")


class _FsWifiDot11radioIfConfigBeaconPeriod_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigBeaconPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 1000),
    )


_FsWifiDot11radioIfConfigBeaconPeriod_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigBeaconPeriod_Object = MibTableColumn
fsWifiDot11radioIfConfigBeaconPeriod = _FsWifiDot11radioIfConfigBeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 53),
    _FsWifiDot11radioIfConfigBeaconPeriod_Type()
)
fsWifiDot11radioIfConfigBeaconPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigBeaconPeriod.setStatus("current")


class _FsWifiDot11radioIfConfigRetrieShortTime_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigRetrieShortTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_FsWifiDot11radioIfConfigRetrieShortTime_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigRetrieShortTime_Object = MibTableColumn
fsWifiDot11radioIfConfigRetrieShortTime = _FsWifiDot11radioIfConfigRetrieShortTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 54),
    _FsWifiDot11radioIfConfigRetrieShortTime_Type()
)
fsWifiDot11radioIfConfigRetrieShortTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigRetrieShortTime.setStatus("current")


class _FsWifiDot11radioIfConfigRetrieLongTime_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigRetrieLongTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_FsWifiDot11radioIfConfigRetrieLongTime_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigRetrieLongTime_Object = MibTableColumn
fsWifiDot11radioIfConfigRetrieLongTime = _FsWifiDot11radioIfConfigRetrieLongTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 55),
    _FsWifiDot11radioIfConfigRetrieLongTime_Type()
)
fsWifiDot11radioIfConfigRetrieLongTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigRetrieLongTime.setStatus("current")


class _FsWifiDot11radioIfConfigStaIdleTimeout_Type(Integer32):
    """Custom type fsWifiDot11radioIfConfigStaIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_FsWifiDot11radioIfConfigStaIdleTimeout_Type.__name__ = "Integer32"
_FsWifiDot11radioIfConfigStaIdleTimeout_Object = MibTableColumn
fsWifiDot11radioIfConfigStaIdleTimeout = _FsWifiDot11radioIfConfigStaIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 56),
    _FsWifiDot11radioIfConfigStaIdleTimeout_Type()
)
fsWifiDot11radioIfConfigStaIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigStaIdleTimeout.setStatus("current")


class _FsWifiDot11radioIfConfigWlanIdList_Type(Bits):
    """Custom type fsWifiDot11radioIfConfigWlanIdList based on Bits"""
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

_FsWifiDot11radioIfConfigWlanIdList_Type.__name__ = "Bits"
_FsWifiDot11radioIfConfigWlanIdList_Object = MibTableColumn
fsWifiDot11radioIfConfigWlanIdList = _FsWifiDot11radioIfConfigWlanIdList_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 3, 1, 1, 57),
    _FsWifiDot11radioIfConfigWlanIdList_Type()
)
fsWifiDot11radioIfConfigWlanIdList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWifiDot11radioIfConfigWlanIdList.setStatus("current")
_FsWifiWlanAssociateObjects_ObjectIdentity = ObjectIdentity
fsWifiWlanAssociateObjects = _FsWifiWlanAssociateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 4)
)
_FsWifiWlanAssociateTable_Object = MibTable
fsWifiWlanAssociateTable = _FsWifiWlanAssociateTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fsWifiWlanAssociateTable.setStatus("current")
_FsWifiWlanAssociateEntry_Object = MibTableRow
fsWifiWlanAssociateEntry = _FsWifiWlanAssociateEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 4, 1, 1)
)
fsWifiWlanAssociateEntry.setIndexNames(
    (0, "FS-ROUTER-WIFI-MIB", "fsWifiWlanAssociateWlanId"),
    (0, "FS-ROUTER-WIFI-MIB", "fsWifiWlanAssociateStaMacAdress"),
)
if mibBuilder.loadTexts:
    fsWifiWlanAssociateEntry.setStatus("current")
_FsWifiWlanAssociateWlanId_Type = Integer32
_FsWifiWlanAssociateWlanId_Object = MibTableColumn
fsWifiWlanAssociateWlanId = _FsWifiWlanAssociateWlanId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 4, 1, 1, 1),
    _FsWifiWlanAssociateWlanId_Type()
)
fsWifiWlanAssociateWlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWifiWlanAssociateWlanId.setStatus("current")
_FsWifiWlanAssociateStaMacAdress_Type = DisplayString
_FsWifiWlanAssociateStaMacAdress_Object = MibTableColumn
fsWifiWlanAssociateStaMacAdress = _FsWifiWlanAssociateStaMacAdress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 4, 1, 1, 2),
    _FsWifiWlanAssociateStaMacAdress_Type()
)
fsWifiWlanAssociateStaMacAdress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWifiWlanAssociateStaMacAdress.setStatus("current")
_FsWifiWlanAssociateSsidName_Type = DisplayString
_FsWifiWlanAssociateSsidName_Object = MibTableColumn
fsWifiWlanAssociateSsidName = _FsWifiWlanAssociateSsidName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 4, 1, 1, 3),
    _FsWifiWlanAssociateSsidName_Type()
)
fsWifiWlanAssociateSsidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWifiWlanAssociateSsidName.setStatus("current")
_FsWifiWlanAssociateStaIpAdress_Type = IpAddress
_FsWifiWlanAssociateStaIpAdress_Object = MibTableColumn
fsWifiWlanAssociateStaIpAdress = _FsWifiWlanAssociateStaIpAdress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 4, 1, 1, 4),
    _FsWifiWlanAssociateStaIpAdress_Type()
)
fsWifiWlanAssociateStaIpAdress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWifiWlanAssociateStaIpAdress.setStatus("current")
_FsWifiWlanAssociateStaMaskAdress_Type = IpAddress
_FsWifiWlanAssociateStaMaskAdress_Object = MibTableColumn
fsWifiWlanAssociateStaMaskAdress = _FsWifiWlanAssociateStaMaskAdress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 4, 1, 1, 5),
    _FsWifiWlanAssociateStaMaskAdress_Type()
)
fsWifiWlanAssociateStaMaskAdress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWifiWlanAssociateStaMaskAdress.setStatus("current")
_FsWifiWlanAssociateStaSigalStrength_Type = Integer32
_FsWifiWlanAssociateStaSigalStrength_Object = MibTableColumn
fsWifiWlanAssociateStaSigalStrength = _FsWifiWlanAssociateStaSigalStrength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 4, 1, 1, 6),
    _FsWifiWlanAssociateStaSigalStrength_Type()
)
fsWifiWlanAssociateStaSigalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWifiWlanAssociateStaSigalStrength.setStatus("current")
_FsWifiWlanAssociateStaConnectTime_Type = DisplayString
_FsWifiWlanAssociateStaConnectTime_Object = MibTableColumn
fsWifiWlanAssociateStaConnectTime = _FsWifiWlanAssociateStaConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 4, 1, 1, 7),
    _FsWifiWlanAssociateStaConnectTime_Type()
)
fsWifiWlanAssociateStaConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWifiWlanAssociateStaConnectTime.setStatus("current")
_FsWifiWlanAssociateStaConnectTimeLength_Type = DisplayString
_FsWifiWlanAssociateStaConnectTimeLength_Object = MibTableColumn
fsWifiWlanAssociateStaConnectTimeLength = _FsWifiWlanAssociateStaConnectTimeLength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 4, 1, 1, 8),
    _FsWifiWlanAssociateStaConnectTimeLength_Type()
)
fsWifiWlanAssociateStaConnectTimeLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWifiWlanAssociateStaConnectTimeLength.setStatus("current")
_FsWifiWlanAssociateStaGate_Type = IpAddress
_FsWifiWlanAssociateStaGate_Object = MibTableColumn
fsWifiWlanAssociateStaGate = _FsWifiWlanAssociateStaGate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 4, 1, 1, 9),
    _FsWifiWlanAssociateStaGate_Type()
)
fsWifiWlanAssociateStaGate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWifiWlanAssociateStaGate.setStatus("current")
_FsWifiWlanAssociateStaDns_Type = IpAddress
_FsWifiWlanAssociateStaDns_Object = MibTableColumn
fsWifiWlanAssociateStaDns = _FsWifiWlanAssociateStaDns_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 133, 1, 4, 1, 1, 10),
    _FsWifiWlanAssociateStaDns_Type()
)
fsWifiWlanAssociateStaDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWifiWlanAssociateStaDns.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-ROUTER-WIFI-MIB",
    **{"FSEableType": FSEableType,
       "FSWlanType": FSWlanType,
       "FSIsolateType": FSIsolateType,
       "FSAuthenticationType": FSAuthenticationType,
       "FSWapPskCiphersType": FSWapPskCiphersType,
       "FSWifiChanWidthType": FSWifiChanWidthType,
       "FSWifiSlotType": FSWifiSlotType,
       "FSWifiFreChanelType": FSWifiFreChanelType,
       "fsWifiMIB": fsWifiMIB,
       "fsWifiMIBObjects": fsWifiMIBObjects,
       "fsWifiDot11radioSupportObjects": fsWifiDot11radioSupportObjects,
       "fsWifiDot11radioSupportTable": fsWifiDot11radioSupportTable,
       "fsWifiDot11radioSupportEntry": fsWifiDot11radioSupportEntry,
       "fsWifiDot11radioIndex": fsWifiDot11radioIndex,
       "fsWifiDot11radioApMaxCnt": fsWifiDot11radioApMaxCnt,
       "fsWifiDot11radioStationMaxCnt": fsWifiDot11radioStationMaxCnt,
       "fsWifiWlanObjects": fsWifiWlanObjects,
       "fsWifiWlanIndexNext": fsWifiWlanIndexNext,
       "fsWifiVlanIndexNext": fsWifiVlanIndexNext,
       "fsWifiWlanTable": fsWifiWlanTable,
       "fsWifiWlanEntry": fsWifiWlanEntry,
       "fsWifiWlanIndex": fsWifiWlanIndex,
       "fsWifiWlanType": fsWifiWlanType,
       "fsWifiWlanSsidName": fsWifiWlanSsidName,
       "fsWifiWlanVlanId": fsWifiWlanVlanId,
       "fsWifiWlanRowStatus": fsWifiWlanRowStatus,
       "fsWifiWlanBroadcastSsid": fsWifiWlanBroadcastSsid,
       "fsWifiWlanIsolate": fsWifiWlanIsolate,
       "fsWifiWlanBssStaLimit": fsWifiWlanBssStaLimit,
       "rujieWifiWlanSecurityType": rujieWifiWlanSecurityType,
       "fsWifiWlanAuthenticationSetKey": fsWifiWlanAuthenticationSetKey,
       "fsWifiWlanWepAuthenticationType": fsWifiWlanWepAuthenticationType,
       "fsWifiWlanWpaPskCiphersType": fsWifiWlanWpaPskCiphersType,
       "fsWifiWlanPassphrase": fsWifiWlanPassphrase,
       "fsWifiWlanDot11RadioIfindex": fsWifiWlanDot11RadioIfindex,
       "fsWifiWlanDot11RadioSubIfindex": fsWifiWlanDot11RadioSubIfindex,
       "fsWifiDot11radioIfConfigObjects": fsWifiDot11radioIfConfigObjects,
       "fsWifiDot11radioIfConfigTable": fsWifiDot11radioIfConfigTable,
       "fsWifiDot11radioIfConfigEntry": fsWifiDot11radioIfConfigEntry,
       "fsWifiDot11radioIfConfigIfIndex": fsWifiDot11radioIfConfigIfIndex,
       "fsWifiDot11radioIfConfigRowStatus": fsWifiDot11radioIfConfigRowStatus,
       "fsWifiDot11radioIfConfigFreBand": fsWifiDot11radioIfConfigFreBand,
       "fsWifiDot11radioIfConfigChannel": fsWifiDot11radioIfConfigChannel,
       "fsWifiDot11radioIfConfigChanWidth": fsWifiDot11radioIfConfigChanWidth,
       "fsWifiDot11radioIfConfigCountryCode": fsWifiDot11radioIfConfigCountryCode,
       "fsWifiDot11radioIfConfigPowerLocal": fsWifiDot11radioIfConfigPowerLocal,
       "fsWifiDot11radioIfConfigWirelessProSupport": fsWifiDot11radioIfConfigWirelessProSupport,
       "fsWifiDot11radioIfConfigStaLimit": fsWifiDot11radioIfConfigStaLimit,
       "fsWifiDot11radioIfConfig20ShortGiEnable": fsWifiDot11radioIfConfig20ShortGiEnable,
       "fsWifiDot11radioIfConfig40ShortGiEnable": fsWifiDot11radioIfConfig40ShortGiEnable,
       "fsWifiDot11radioIfConfigShortPreambleEnable": fsWifiDot11radioIfConfigShortPreambleEnable,
       "fsWifiDot11radioIfConfigSlottime": fsWifiDot11radioIfConfigSlottime,
       "fsWifiDot11radioIfConfigRtsThreshold": fsWifiDot11radioIfConfigRtsThreshold,
       "fsWifiDot11radioIfConfigFragmentThreshold": fsWifiDot11radioIfConfigFragmentThreshold,
       "fsWifiDot11radioIfConfigResponseRssi": fsWifiDot11radioIfConfigResponseRssi,
       "fsWifiDot11radioIfConfigEnableQos": fsWifiDot11radioIfConfigEnableQos,
       "fsWifiDot11radioIfConfigEdcaClientBgAifsn": fsWifiDot11radioIfConfigEdcaClientBgAifsn,
       "fsWifiDot11radioIfConfigEdcaClientBgCwmin": fsWifiDot11radioIfConfigEdcaClientBgCwmin,
       "fsWifiDot11radioIfConfigEdcaClientBgCwmax": fsWifiDot11radioIfConfigEdcaClientBgCwmax,
       "fsWifiDot11radioIfConfigEdcaClientBgTxop": fsWifiDot11radioIfConfigEdcaClientBgTxop,
       "fsWifiDot11radioIfConfigEdcaClientBeAifsn": fsWifiDot11radioIfConfigEdcaClientBeAifsn,
       "fsWifiDot11radioIfConfigEdcaClientBeCwmin": fsWifiDot11radioIfConfigEdcaClientBeCwmin,
       "fsWifiDot11radioIfConfigEdcaClientBeCwmax": fsWifiDot11radioIfConfigEdcaClientBeCwmax,
       "fsWifiDot11radioIfConfigEdcaClientBeTxop": fsWifiDot11radioIfConfigEdcaClientBeTxop,
       "fsWifiDot11radioIfConfigEdcaClientViAifsn": fsWifiDot11radioIfConfigEdcaClientViAifsn,
       "fsWifiDot11radioIfConfigEdcaClientViCwmin": fsWifiDot11radioIfConfigEdcaClientViCwmin,
       "fsWifiDot11radioIfConfigEdcaClientViCwmax": fsWifiDot11radioIfConfigEdcaClientViCwmax,
       "fsWifiDot11radioIfConfigEdcaClientViTxop": fsWifiDot11radioIfConfigEdcaClientViTxop,
       "fsWifiDot11radioIfConfigEdcaClientVoAifsn": fsWifiDot11radioIfConfigEdcaClientVoAifsn,
       "fsWifiDot11radioIfConfigEdcaClientVoCwmin": fsWifiDot11radioIfConfigEdcaClientVoCwmin,
       "fsWifiDot11radioIfConfigEdcaClientVoCwmax": fsWifiDot11radioIfConfigEdcaClientVoCwmax,
       "fsWifiDot11radioIfConfigEdcaClientVoTxop": fsWifiDot11radioIfConfigEdcaClientVoTxop,
       "fsWifiDot11radioIfConfigEdcaRadioBgAifsn": fsWifiDot11radioIfConfigEdcaRadioBgAifsn,
       "fsWifiDot11radioIfConfigEdcaRadioBgCwmin": fsWifiDot11radioIfConfigEdcaRadioBgCwmin,
       "fsWifiDot11radioIfConfigEdcaRadioBgCwmax": fsWifiDot11radioIfConfigEdcaRadioBgCwmax,
       "fsWifiDot11radioIfConfigEdcaRadioBgTxop": fsWifiDot11radioIfConfigEdcaRadioBgTxop,
       "fsWifiDot11radioIfConfigEdcaRadioBeAifsn": fsWifiDot11radioIfConfigEdcaRadioBeAifsn,
       "fsWifiDot11radioIfConfigEdcaRadioBeCwmin": fsWifiDot11radioIfConfigEdcaRadioBeCwmin,
       "fsWifiDot11radioIfConfigEdcaRadioBeCwmax": fsWifiDot11radioIfConfigEdcaRadioBeCwmax,
       "fsWifiDot11radioIfConfigEdcaRadioBeTxop": fsWifiDot11radioIfConfigEdcaRadioBeTxop,
       "fsWifiDot11radioIfConfigEdcaRadioViAifsn": fsWifiDot11radioIfConfigEdcaRadioViAifsn,
       "fsWifiDot11radioIfConfigEdcaRadioViCwmin": fsWifiDot11radioIfConfigEdcaRadioViCwmin,
       "fsWifiDot11radioIfConfigEdcaRadioViCwmax": fsWifiDot11radioIfConfigEdcaRadioViCwmax,
       "fsWifiDot11radioIfConfigEdcaRadioViTxop": fsWifiDot11radioIfConfigEdcaRadioViTxop,
       "fsWifiDot11radioIfConfigEdcaRadioVoAifsn": fsWifiDot11radioIfConfigEdcaRadioVoAifsn,
       "fsWifiDot11radioIfConfigEdcaRadioVoCwmin": fsWifiDot11radioIfConfigEdcaRadioVoCwmin,
       "fsWifiDot11radioIfConfigEdcaRadioVoCwmax": fsWifiDot11radioIfConfigEdcaRadioVoCwmax,
       "fsWifiDot11radioIfConfigEdcaRadioVoTxop": fsWifiDot11radioIfConfigEdcaRadioVoTxop,
       "fsWifiDot11radioIfConfigAntennaTransChainmask": fsWifiDot11radioIfConfigAntennaTransChainmask,
       "fsWifiDot11radioIfConfigAntennaReceiveChainmask": fsWifiDot11radioIfConfigAntennaReceiveChainmask,
       "fsWifiDot11radioIfConfigBeaconDtimPeriod": fsWifiDot11radioIfConfigBeaconDtimPeriod,
       "fsWifiDot11radioIfConfigBeaconPeriod": fsWifiDot11radioIfConfigBeaconPeriod,
       "fsWifiDot11radioIfConfigRetrieShortTime": fsWifiDot11radioIfConfigRetrieShortTime,
       "fsWifiDot11radioIfConfigRetrieLongTime": fsWifiDot11radioIfConfigRetrieLongTime,
       "fsWifiDot11radioIfConfigStaIdleTimeout": fsWifiDot11radioIfConfigStaIdleTimeout,
       "fsWifiDot11radioIfConfigWlanIdList": fsWifiDot11radioIfConfigWlanIdList,
       "fsWifiWlanAssociateObjects": fsWifiWlanAssociateObjects,
       "fsWifiWlanAssociateTable": fsWifiWlanAssociateTable,
       "fsWifiWlanAssociateEntry": fsWifiWlanAssociateEntry,
       "fsWifiWlanAssociateWlanId": fsWifiWlanAssociateWlanId,
       "fsWifiWlanAssociateStaMacAdress": fsWifiWlanAssociateStaMacAdress,
       "fsWifiWlanAssociateSsidName": fsWifiWlanAssociateSsidName,
       "fsWifiWlanAssociateStaIpAdress": fsWifiWlanAssociateStaIpAdress,
       "fsWifiWlanAssociateStaMaskAdress": fsWifiWlanAssociateStaMaskAdress,
       "fsWifiWlanAssociateStaSigalStrength": fsWifiWlanAssociateStaSigalStrength,
       "fsWifiWlanAssociateStaConnectTime": fsWifiWlanAssociateStaConnectTime,
       "fsWifiWlanAssociateStaConnectTimeLength": fsWifiWlanAssociateStaConnectTimeLength,
       "fsWifiWlanAssociateStaGate": fsWifiWlanAssociateStaGate,
       "fsWifiWlanAssociateStaDns": fsWifiWlanAssociateStaDns}
)
