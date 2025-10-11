# SNMP MIB module (HNE-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/arris/HNE-DEVICE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:10:34 2025
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

(arrisProdIdRouter,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "arrisProdIdRouter")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hneMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3)
)
if mibBuilder.loadTexts:
    hneMib.setRevisions(
        ("2015-01-14 00:00",
         "2015-01-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HneMibObjects_ObjectIdentity = ObjectIdentity
hneMibObjects = _HneMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1)
)
_HneWiFiGWSupport_ObjectIdentity = ObjectIdentity
hneWiFiGWSupport = _HneWiFiGWSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1)
)
_HneWiFiGWSearch_Type = TruthValue
_HneWiFiGWSearch_Object = MibScalar
hneWiFiGWSearch = _HneWiFiGWSearch_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 1),
    _HneWiFiGWSearch_Type()
)
hneWiFiGWSearch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneWiFiGWSearch.setStatus("current")
_HneWiFiGWTable_Object = MibTable
hneWiFiGWTable = _HneWiFiGWTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hneWiFiGWTable.setStatus("current")
_HneWiFiGWEntry_Object = MibTableRow
hneWiFiGWEntry = _HneWiFiGWEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2, 1)
)
hneWiFiGWEntry.setIndexNames(
    (0, "HNE-DEVICE-MIB", "hneWiFiGWIndex"),
)
if mibBuilder.loadTexts:
    hneWiFiGWEntry.setStatus("current")
_HneWiFiGWIndex_Type = Unsigned32
_HneWiFiGWIndex_Object = MibTableColumn
hneWiFiGWIndex = _HneWiFiGWIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2, 1, 1),
    _HneWiFiGWIndex_Type()
)
hneWiFiGWIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hneWiFiGWIndex.setStatus("current")
_HneWiFiGWMACAddr_Type = MacAddress
_HneWiFiGWMACAddr_Object = MibTableColumn
hneWiFiGWMACAddr = _HneWiFiGWMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2, 1, 2),
    _HneWiFiGWMACAddr_Type()
)
hneWiFiGWMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneWiFiGWMACAddr.setStatus("current")
_HneWiFiGWIPAddrType_Type = InetAddressType
_HneWiFiGWIPAddrType_Object = MibTableColumn
hneWiFiGWIPAddrType = _HneWiFiGWIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2, 1, 3),
    _HneWiFiGWIPAddrType_Type()
)
hneWiFiGWIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneWiFiGWIPAddrType.setStatus("current")
_HneWiFiGWIPAddress_Type = InetAddress
_HneWiFiGWIPAddress_Object = MibTableColumn
hneWiFiGWIPAddress = _HneWiFiGWIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2, 1, 4),
    _HneWiFiGWIPAddress_Type()
)
hneWiFiGWIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneWiFiGWIPAddress.setStatus("current")
_HneWiFiGWARRISAutoCfgSupport_Type = TruthValue
_HneWiFiGWARRISAutoCfgSupport_Object = MibTableColumn
hneWiFiGWARRISAutoCfgSupport = _HneWiFiGWARRISAutoCfgSupport_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2, 1, 5),
    _HneWiFiGWARRISAutoCfgSupport_Type()
)
hneWiFiGWARRISAutoCfgSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneWiFiGWARRISAutoCfgSupport.setStatus("current")
_HneWiFiGWLocation_Type = DisplayString
_HneWiFiGWLocation_Object = MibTableColumn
hneWiFiGWLocation = _HneWiFiGWLocation_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2, 1, 6),
    _HneWiFiGWLocation_Type()
)
hneWiFiGWLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneWiFiGWLocation.setStatus("current")


class _HneWiFiGWManufacturer_Type(DisplayString):
    """Custom type hneWiFiGWManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HneWiFiGWManufacturer_Type.__name__ = "DisplayString"
_HneWiFiGWManufacturer_Object = MibTableColumn
hneWiFiGWManufacturer = _HneWiFiGWManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2, 1, 7),
    _HneWiFiGWManufacturer_Type()
)
hneWiFiGWManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneWiFiGWManufacturer.setStatus("current")


class _HneWiFiGWModelName_Type(DisplayString):
    """Custom type hneWiFiGWModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HneWiFiGWModelName_Type.__name__ = "DisplayString"
_HneWiFiGWModelName_Object = MibTableColumn
hneWiFiGWModelName = _HneWiFiGWModelName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2, 1, 8),
    _HneWiFiGWModelName_Type()
)
hneWiFiGWModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneWiFiGWModelName.setStatus("current")


class _HneWiFiGWModelNumber_Type(DisplayString):
    """Custom type hneWiFiGWModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HneWiFiGWModelNumber_Type.__name__ = "DisplayString"
_HneWiFiGWModelNumber_Object = MibTableColumn
hneWiFiGWModelNumber = _HneWiFiGWModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2, 1, 9),
    _HneWiFiGWModelNumber_Type()
)
hneWiFiGWModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneWiFiGWModelNumber.setStatus("current")


class _HneWiFiGWConfigurationId_Type(Unsigned32):
    """Custom type hneWiFiGWConfigurationId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_HneWiFiGWConfigurationId_Type.__name__ = "Unsigned32"
_HneWiFiGWConfigurationId_Object = MibTableColumn
hneWiFiGWConfigurationId = _HneWiFiGWConfigurationId_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2, 1, 10),
    _HneWiFiGWConfigurationId_Type()
)
hneWiFiGWConfigurationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneWiFiGWConfigurationId.setStatus("current")
_HneWiFiGWLastSynchAttemptTime_Type = DateAndTime
_HneWiFiGWLastSynchAttemptTime_Object = MibTableColumn
hneWiFiGWLastSynchAttemptTime = _HneWiFiGWLastSynchAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2, 1, 11),
    _HneWiFiGWLastSynchAttemptTime_Type()
)
hneWiFiGWLastSynchAttemptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneWiFiGWLastSynchAttemptTime.setStatus("current")


class _HneWiFiGWLastSynchAttemptResult_Type(Integer32):
    """Custom type hneWiFiGWLastSynchAttemptResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uninitialized", -1),
          ("pass", 0),
          ("failHTTPSSessionEstablishment", 1),
          ("failHTTPSPUT", 2))
    )


_HneWiFiGWLastSynchAttemptResult_Type.__name__ = "Integer32"
_HneWiFiGWLastSynchAttemptResult_Object = MibTableColumn
hneWiFiGWLastSynchAttemptResult = _HneWiFiGWLastSynchAttemptResult_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2, 1, 12),
    _HneWiFiGWLastSynchAttemptResult_Type()
)
hneWiFiGWLastSynchAttemptResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneWiFiGWLastSynchAttemptResult.setStatus("current")
_HneWiFiGWSynchedWithGW_Type = TruthValue
_HneWiFiGWSynchedWithGW_Object = MibTableColumn
hneWiFiGWSynchedWithGW = _HneWiFiGWSynchedWithGW_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2, 1, 13),
    _HneWiFiGWSynchedWithGW_Type()
)
hneWiFiGWSynchedWithGW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneWiFiGWSynchedWithGW.setStatus("current")


class _HneWiFiGWOverride24OutputPower_Type(Integer32):
    """Custom type hneWiFiGWOverride24OutputPower based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              12,
              25,
              50,
              75,
              100)
        )
    )
    namedValues = NamedValues(
        *(("gatewayDefault", 0),
          ("percent12", 12),
          ("percent25", 25),
          ("percent50", 50),
          ("percent75", 75),
          ("percent100", 100))
    )


_HneWiFiGWOverride24OutputPower_Type.__name__ = "Integer32"
_HneWiFiGWOverride24OutputPower_Object = MibTableColumn
hneWiFiGWOverride24OutputPower = _HneWiFiGWOverride24OutputPower_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2, 1, 14),
    _HneWiFiGWOverride24OutputPower_Type()
)
hneWiFiGWOverride24OutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneWiFiGWOverride24OutputPower.setStatus("current")


class _HneWiFiGWOverride50OutputPower_Type(Integer32):
    """Custom type hneWiFiGWOverride50OutputPower based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              12,
              25,
              50,
              75,
              100)
        )
    )
    namedValues = NamedValues(
        *(("gatewayDefault", 0),
          ("percent12", 12),
          ("percent25", 25),
          ("percent50", 50),
          ("percent75", 75),
          ("percent100", 100))
    )


_HneWiFiGWOverride50OutputPower_Type.__name__ = "Integer32"
_HneWiFiGWOverride50OutputPower_Object = MibTableColumn
hneWiFiGWOverride50OutputPower = _HneWiFiGWOverride50OutputPower_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2, 1, 15),
    _HneWiFiGWOverride50OutputPower_Type()
)
hneWiFiGWOverride50OutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneWiFiGWOverride50OutputPower.setStatus("current")


class _HneWiFiGWOverride24Channel_Type(Unsigned32):
    """Custom type hneWiFiGWOverride24Channel based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 216),
        ValueRangeConstraint(255, 255),
    )


_HneWiFiGWOverride24Channel_Type.__name__ = "Unsigned32"
_HneWiFiGWOverride24Channel_Object = MibTableColumn
hneWiFiGWOverride24Channel = _HneWiFiGWOverride24Channel_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2, 1, 16),
    _HneWiFiGWOverride24Channel_Type()
)
hneWiFiGWOverride24Channel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneWiFiGWOverride24Channel.setStatus("current")


class _HneWiFiGWOverride50Channel_Type(Unsigned32):
    """Custom type hneWiFiGWOverride50Channel based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 216),
        ValueRangeConstraint(255, 255),
    )


_HneWiFiGWOverride50Channel_Type.__name__ = "Unsigned32"
_HneWiFiGWOverride50Channel_Object = MibTableColumn
hneWiFiGWOverride50Channel = _HneWiFiGWOverride50Channel_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2, 1, 17),
    _HneWiFiGWOverride50Channel_Type()
)
hneWiFiGWOverride50Channel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneWiFiGWOverride50Channel.setStatus("current")


class _HneWiFiGWOverride24ChannelBW_Type(Integer32):
    """Custom type hneWiFiGWOverride24ChannelBW based on Integer32"""
    defaultValue = -2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gatewayDefault", -2),
          ("unknown", -1),
          ("width20MHz", 0),
          ("width40MHz", 1),
          ("width20and40Mhz", 2))
    )


_HneWiFiGWOverride24ChannelBW_Type.__name__ = "Integer32"
_HneWiFiGWOverride24ChannelBW_Object = MibTableColumn
hneWiFiGWOverride24ChannelBW = _HneWiFiGWOverride24ChannelBW_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2, 1, 18),
    _HneWiFiGWOverride24ChannelBW_Type()
)
hneWiFiGWOverride24ChannelBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneWiFiGWOverride24ChannelBW.setStatus("current")


class _HneWiFiGWOverride50ChannelBW_Type(Integer32):
    """Custom type hneWiFiGWOverride50ChannelBW based on Integer32"""
    defaultValue = -2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gatewayDefault", -2),
          ("unknown", -1),
          ("width20MHz", 0),
          ("width20and40Mhz", 2),
          ("width20and40and80Mhz", 3))
    )


_HneWiFiGWOverride50ChannelBW_Type.__name__ = "Integer32"
_HneWiFiGWOverride50ChannelBW_Object = MibTableColumn
hneWiFiGWOverride50ChannelBW = _HneWiFiGWOverride50ChannelBW_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 2, 1, 19),
    _HneWiFiGWOverride50ChannelBW_Type()
)
hneWiFiGWOverride50ChannelBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneWiFiGWOverride50ChannelBW.setStatus("current")
_HneWiFiGWSupportedTable_Object = MibTable
hneWiFiGWSupportedTable = _HneWiFiGWSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hneWiFiGWSupportedTable.setStatus("current")
_HneWiFiGWSupportedEntry_Object = MibTableRow
hneWiFiGWSupportedEntry = _HneWiFiGWSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 3, 1)
)
hneWiFiGWSupportedEntry.setIndexNames(
    (0, "HNE-DEVICE-MIB", "hneWiFiGWSupportedIndex"),
)
if mibBuilder.loadTexts:
    hneWiFiGWSupportedEntry.setStatus("current")
_HneWiFiGWSupportedIndex_Type = Unsigned32
_HneWiFiGWSupportedIndex_Object = MibTableColumn
hneWiFiGWSupportedIndex = _HneWiFiGWSupportedIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 3, 1, 1),
    _HneWiFiGWSupportedIndex_Type()
)
hneWiFiGWSupportedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hneWiFiGWSupportedIndex.setStatus("current")


class _HneWiFiGWSupportedManufacturer_Type(DisplayString):
    """Custom type hneWiFiGWSupportedManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HneWiFiGWSupportedManufacturer_Type.__name__ = "DisplayString"
_HneWiFiGWSupportedManufacturer_Object = MibTableColumn
hneWiFiGWSupportedManufacturer = _HneWiFiGWSupportedManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 3, 1, 2),
    _HneWiFiGWSupportedManufacturer_Type()
)
hneWiFiGWSupportedManufacturer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hneWiFiGWSupportedManufacturer.setStatus("current")


class _HneWiFiGWSupportedModelNumber_Type(DisplayString):
    """Custom type hneWiFiGWSupportedModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HneWiFiGWSupportedModelNumber_Type.__name__ = "DisplayString"
_HneWiFiGWSupportedModelNumber_Object = MibTableColumn
hneWiFiGWSupportedModelNumber = _HneWiFiGWSupportedModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 3, 1, 3),
    _HneWiFiGWSupportedModelNumber_Type()
)
hneWiFiGWSupportedModelNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hneWiFiGWSupportedModelNumber.setStatus("current")
_HneWiFiGWSupportedRowStatus_Type = RowStatus
_HneWiFiGWSupportedRowStatus_Object = MibTableColumn
hneWiFiGWSupportedRowStatus = _HneWiFiGWSupportedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 3, 1, 4),
    _HneWiFiGWSupportedRowStatus_Type()
)
hneWiFiGWSupportedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hneWiFiGWSupportedRowStatus.setStatus("current")


class _HneWiFiGWConfigAttempts_Type(Unsigned32):
    """Custom type hneWiFiGWConfigAttempts based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HneWiFiGWConfigAttempts_Type.__name__ = "Unsigned32"
_HneWiFiGWConfigAttempts_Object = MibScalar
hneWiFiGWConfigAttempts = _HneWiFiGWConfigAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 4),
    _HneWiFiGWConfigAttempts_Type()
)
hneWiFiGWConfigAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneWiFiGWConfigAttempts.setStatus("current")


class _HneWiFiGWConfigDuration_Type(Unsigned32):
    """Custom type hneWiFiGWConfigDuration based on Unsigned32"""
    defaultValue = 3600


_HneWiFiGWConfigDuration_Type.__name__ = "Unsigned32"
_HneWiFiGWConfigDuration_Object = MibScalar
hneWiFiGWConfigDuration = _HneWiFiGWConfigDuration_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 5),
    _HneWiFiGWConfigDuration_Type()
)
hneWiFiGWConfigDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneWiFiGWConfigDuration.setStatus("current")
if mibBuilder.loadTexts:
    hneWiFiGWConfigDuration.setUnits("seconds")


class _HneWiFiGWAutoConfigurationEnable_Type(TruthValue):
    """Custom type hneWiFiGWAutoConfigurationEnable based on TruthValue"""
    defaultValue = 2


_HneWiFiGWAutoConfigurationEnable_Type.__name__ = "TruthValue"
_HneWiFiGWAutoConfigurationEnable_Object = MibScalar
hneWiFiGWAutoConfigurationEnable = _HneWiFiGWAutoConfigurationEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 6),
    _HneWiFiGWAutoConfigurationEnable_Type()
)
hneWiFiGWAutoConfigurationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneWiFiGWAutoConfigurationEnable.setStatus("current")


class _HneWiFiGWSecurityEnable_Type(TruthValue):
    """Custom type hneWiFiGWSecurityEnable based on TruthValue"""
    defaultValue = 1


_HneWiFiGWSecurityEnable_Type.__name__ = "TruthValue"
_HneWiFiGWSecurityEnable_Object = MibScalar
hneWiFiGWSecurityEnable = _HneWiFiGWSecurityEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 1, 7),
    _HneWiFiGWSecurityEnable_Type()
)
hneWiFiGWSecurityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hneWiFiGWSecurityEnable.setStatus("current")
_HneLAN_ObjectIdentity = ObjectIdentity
hneLAN = _HneLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 2)
)
_HneLANTable_Object = MibTable
hneLANTable = _HneLANTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hneLANTable.setStatus("current")
_HneLANEntry_Object = MibTableRow
hneLANEntry = _HneLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 2, 1, 1)
)
hneLANEntry.setIndexNames(
    (0, "HNE-DEVICE-MIB", "hneLANIndex"),
    (0, "HNE-DEVICE-MIB", "hneLANGWMappingIndex"),
)
if mibBuilder.loadTexts:
    hneLANEntry.setStatus("current")
_HneLANIndex_Type = Unsigned32
_HneLANIndex_Object = MibTableColumn
hneLANIndex = _HneLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 2, 1, 1, 1),
    _HneLANIndex_Type()
)
hneLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hneLANIndex.setStatus("current")
_HneLANGWMappingIndex_Type = Unsigned32
_HneLANGWMappingIndex_Object = MibTableColumn
hneLANGWMappingIndex = _HneLANGWMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 2, 1, 1, 2),
    _HneLANGWMappingIndex_Type()
)
hneLANGWMappingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hneLANGWMappingIndex.setStatus("current")
_HneLANInterface_Type = DisplayString
_HneLANInterface_Object = MibTableColumn
hneLANInterface = _HneLANInterface_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 2, 1, 1, 3),
    _HneLANInterface_Type()
)
hneLANInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneLANInterface.setStatus("current")


class _HneLANInterfaceType_Type(Integer32):
    """Custom type hneLANInterfaceType based on Integer32"""
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
        *(("radio24Ghz", 0),
          ("radio50Ghz", 1),
          ("radio24GhzSsid", 2),
          ("radio50GhzSsid", 3),
          ("ethernet", 4))
    )


_HneLANInterfaceType_Type.__name__ = "Integer32"
_HneLANInterfaceType_Object = MibTableColumn
hneLANInterfaceType = _HneLANInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 2, 1, 1, 4),
    _HneLANInterfaceType_Type()
)
hneLANInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneLANInterfaceType.setStatus("current")
_HneLANBridgingMgmtPortInterface_Type = DisplayString
_HneLANBridgingMgmtPortInterface_Object = MibTableColumn
hneLANBridgingMgmtPortInterface = _HneLANBridgingMgmtPortInterface_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 2, 1, 1, 5),
    _HneLANBridgingMgmtPortInterface_Type()
)
hneLANBridgingMgmtPortInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneLANBridgingMgmtPortInterface.setStatus("current")
_HneLANVLANID_Type = Unsigned32
_HneLANVLANID_Object = MibTableColumn
hneLANVLANID = _HneLANVLANID_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20, 3, 1, 2, 1, 1, 6),
    _HneLANVLANID_Type()
)
hneLANVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hneLANVLANID.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HNE-DEVICE-MIB",
    **{"hneMib": hneMib,
       "hneMibObjects": hneMibObjects,
       "hneWiFiGWSupport": hneWiFiGWSupport,
       "hneWiFiGWSearch": hneWiFiGWSearch,
       "hneWiFiGWTable": hneWiFiGWTable,
       "hneWiFiGWEntry": hneWiFiGWEntry,
       "hneWiFiGWIndex": hneWiFiGWIndex,
       "hneWiFiGWMACAddr": hneWiFiGWMACAddr,
       "hneWiFiGWIPAddrType": hneWiFiGWIPAddrType,
       "hneWiFiGWIPAddress": hneWiFiGWIPAddress,
       "hneWiFiGWARRISAutoCfgSupport": hneWiFiGWARRISAutoCfgSupport,
       "hneWiFiGWLocation": hneWiFiGWLocation,
       "hneWiFiGWManufacturer": hneWiFiGWManufacturer,
       "hneWiFiGWModelName": hneWiFiGWModelName,
       "hneWiFiGWModelNumber": hneWiFiGWModelNumber,
       "hneWiFiGWConfigurationId": hneWiFiGWConfigurationId,
       "hneWiFiGWLastSynchAttemptTime": hneWiFiGWLastSynchAttemptTime,
       "hneWiFiGWLastSynchAttemptResult": hneWiFiGWLastSynchAttemptResult,
       "hneWiFiGWSynchedWithGW": hneWiFiGWSynchedWithGW,
       "hneWiFiGWOverride24OutputPower": hneWiFiGWOverride24OutputPower,
       "hneWiFiGWOverride50OutputPower": hneWiFiGWOverride50OutputPower,
       "hneWiFiGWOverride24Channel": hneWiFiGWOverride24Channel,
       "hneWiFiGWOverride50Channel": hneWiFiGWOverride50Channel,
       "hneWiFiGWOverride24ChannelBW": hneWiFiGWOverride24ChannelBW,
       "hneWiFiGWOverride50ChannelBW": hneWiFiGWOverride50ChannelBW,
       "hneWiFiGWSupportedTable": hneWiFiGWSupportedTable,
       "hneWiFiGWSupportedEntry": hneWiFiGWSupportedEntry,
       "hneWiFiGWSupportedIndex": hneWiFiGWSupportedIndex,
       "hneWiFiGWSupportedManufacturer": hneWiFiGWSupportedManufacturer,
       "hneWiFiGWSupportedModelNumber": hneWiFiGWSupportedModelNumber,
       "hneWiFiGWSupportedRowStatus": hneWiFiGWSupportedRowStatus,
       "hneWiFiGWConfigAttempts": hneWiFiGWConfigAttempts,
       "hneWiFiGWConfigDuration": hneWiFiGWConfigDuration,
       "hneWiFiGWAutoConfigurationEnable": hneWiFiGWAutoConfigurationEnable,
       "hneWiFiGWSecurityEnable": hneWiFiGWSecurityEnable,
       "hneLAN": hneLAN,
       "hneLANTable": hneLANTable,
       "hneLANEntry": hneLANEntry,
       "hneLANIndex": hneLANIndex,
       "hneLANGWMappingIndex": hneLANGWMappingIndex,
       "hneLANInterface": hneLANInterface,
       "hneLANInterfaceType": hneLANInterfaceType,
       "hneLANBridgingMgmtPortInterface": hneLANBridgingMgmtPortInterface,
       "hneLANVLANID": hneLANVLANID}
)
