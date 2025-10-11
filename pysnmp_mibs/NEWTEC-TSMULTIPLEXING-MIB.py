# SNMP MIB module (NEWTEC-TSMULTIPLEXING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-TSMULTIPLEXING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:17 2025
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

(Float32TC,) = mibBuilder.importSymbols(
    "FLOAT-TC-MIB",
    "Float32TC")

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcAlarmState,
 NtcEnable) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcAlarmState",
    "NtcEnable")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ntcTsMultiplexing = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600)
)
if mibBuilder.loadTexts:
    ntcTsMultiplexing.setRevisions(
        ("2017-07-10 12:00",
         "2016-02-02 07:00",
         "2014-09-09 09:00",
         "2013-09-20 10:00",
         "2013-03-27 10:00",
         "2012-06-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcTsMuxObjects_ObjectIdentity = ObjectIdentity
ntcTsMuxObjects = _NtcTsMuxObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1)
)
if mibBuilder.loadTexts:
    ntcTsMuxObjects.setStatus("current")
_NtcInputSelectionTable_Object = MibTable
ntcInputSelectionTable = _NtcInputSelectionTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 1)
)
if mibBuilder.loadTexts:
    ntcInputSelectionTable.setStatus("deprecated")
_NtcInputSelectionEntry_Object = MibTableRow
ntcInputSelectionEntry = _NtcInputSelectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 1, 1)
)
ntcInputSelectionEntry.setIndexNames(
    (0, "NEWTEC-TSMULTIPLEXING-MIB", "ntcInputSelectionInputType"),
)
if mibBuilder.loadTexts:
    ntcInputSelectionEntry.setStatus("deprecated")


class _NtcInputSelectionInputType_Type(Integer32):
    """Custom type ntcInputSelectionInputType based on Integer32"""
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
        *(("asi", 0),
          ("tsOverIp", 1),
          ("mpe", 2),
          ("prbs", 3),
          ("protectedTsOverIp", 4))
    )


_NtcInputSelectionInputType_Type.__name__ = "Integer32"
_NtcInputSelectionInputType_Object = MibTableColumn
ntcInputSelectionInputType = _NtcInputSelectionInputType_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 1, 1, 1),
    _NtcInputSelectionInputType_Type()
)
ntcInputSelectionInputType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcInputSelectionInputType.setStatus("deprecated")


class _NtcInputSelectionEnable_Type(NtcEnable):
    """Custom type ntcInputSelectionEnable based on NtcEnable"""
    defaultValue = 0


_NtcInputSelectionEnable_Type.__name__ = "NtcEnable"
_NtcInputSelectionEnable_Object = MibTableColumn
ntcInputSelectionEnable = _NtcInputSelectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 1, 1, 2),
    _NtcInputSelectionEnable_Type()
)
ntcInputSelectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcInputSelectionEnable.setStatus("deprecated")
_NtcTsMuxRateAdapter_ObjectIdentity = ObjectIdentity
ntcTsMuxRateAdapter = _NtcTsMuxRateAdapter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 2)
)
if mibBuilder.loadTexts:
    ntcTsMuxRateAdapter.setStatus("current")


class _NtcTsMuxRaEnable_Type(NtcEnable):
    """Custom type ntcTsMuxRaEnable based on NtcEnable"""
    defaultValue = 1


_NtcTsMuxRaEnable_Type.__name__ = "NtcEnable"
_NtcTsMuxRaEnable_Object = MibScalar
ntcTsMuxRaEnable = _NtcTsMuxRaEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 2, 1),
    _NtcTsMuxRaEnable_Type()
)
ntcTsMuxRaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxRaEnable.setStatus("current")


class _NtcTsMuxRaNullPktDrop_Type(NtcEnable):
    """Custom type ntcTsMuxRaNullPktDrop based on NtcEnable"""
    defaultValue = 1


_NtcTsMuxRaNullPktDrop_Type.__name__ = "NtcEnable"
_NtcTsMuxRaNullPktDrop_Object = MibScalar
ntcTsMuxRaNullPktDrop = _NtcTsMuxRaNullPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 2, 2),
    _NtcTsMuxRaNullPktDrop_Type()
)
ntcTsMuxRaNullPktDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxRaNullPktDrop.setStatus("current")


class _NtcTsMuxRaPcrRestamp_Type(NtcEnable):
    """Custom type ntcTsMuxRaPcrRestamp based on NtcEnable"""
    defaultValue = 1


_NtcTsMuxRaPcrRestamp_Type.__name__ = "NtcEnable"
_NtcTsMuxRaPcrRestamp_Object = MibScalar
ntcTsMuxRaPcrRestamp = _NtcTsMuxRaPcrRestamp_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 2, 3),
    _NtcTsMuxRaPcrRestamp_Type()
)
ntcTsMuxRaPcrRestamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxRaPcrRestamp.setStatus("current")
_NtcTsMuxMonitor_ObjectIdentity = ObjectIdentity
ntcTsMuxMonitor = _NtcTsMuxMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 3)
)
if mibBuilder.loadTexts:
    ntcTsMuxMonitor.setStatus("current")


class _NtcTsMuxMonResetCounters_Type(Integer32):
    """Custom type ntcTsMuxMonResetCounters based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("counting", 0),
          ("reset", 1))
    )


_NtcTsMuxMonResetCounters_Type.__name__ = "Integer32"
_NtcTsMuxMonResetCounters_Object = MibScalar
ntcTsMuxMonResetCounters = _NtcTsMuxMonResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 3, 1),
    _NtcTsMuxMonResetCounters_Type()
)
ntcTsMuxMonResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxMonResetCounters.setStatus("current")
_NtcTsMuxMonStatisticsTable_Object = MibTable
ntcTsMuxMonStatisticsTable = _NtcTsMuxMonStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ntcTsMuxMonStatisticsTable.setStatus("current")
_NtcTsMuxMonStatisticsEntry_Object = MibTableRow
ntcTsMuxMonStatisticsEntry = _NtcTsMuxMonStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 3, 2, 1)
)
ntcTsMuxMonStatisticsEntry.setIndexNames(
    (0, "NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxMonStatisticsType"),
)
if mibBuilder.loadTexts:
    ntcTsMuxMonStatisticsEntry.setStatus("current")


class _NtcTsMuxMonStatisticsType_Type(Integer32):
    """Custom type ntcTsMuxMonStatisticsType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("asi", 0),
          ("tsOverIp", 1),
          ("mpe", 2),
          ("inputNullPackets", 3),
          ("signalling", 4),
          ("outputNullPackets", 5),
          ("outputDataPackets", 6),
          ("outputTotalPackets", 7),
          ("protectedTsOverIp", 8))
    )


_NtcTsMuxMonStatisticsType_Type.__name__ = "Integer32"
_NtcTsMuxMonStatisticsType_Object = MibTableColumn
ntcTsMuxMonStatisticsType = _NtcTsMuxMonStatisticsType_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 3, 2, 1, 1),
    _NtcTsMuxMonStatisticsType_Type()
)
ntcTsMuxMonStatisticsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcTsMuxMonStatisticsType.setStatus("current")
_NtcTsMuxMonPacketCount_Type = Counter32
_NtcTsMuxMonPacketCount_Object = MibTableColumn
ntcTsMuxMonPacketCount = _NtcTsMuxMonPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 3, 2, 1, 2),
    _NtcTsMuxMonPacketCount_Type()
)
ntcTsMuxMonPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsMuxMonPacketCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsMuxMonPacketCount.setUnits("packets")
_NtcTsMuxMonPacketRate_Type = Counter32
_NtcTsMuxMonPacketRate_Object = MibTableColumn
ntcTsMuxMonPacketRate = _NtcTsMuxMonPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 3, 2, 1, 3),
    _NtcTsMuxMonPacketRate_Type()
)
ntcTsMuxMonPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsMuxMonPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsMuxMonPacketRate.setUnits("pps")
_NtcTsMuxMonBitRatet_Type = Counter32
_NtcTsMuxMonBitRatet_Object = MibTableColumn
ntcTsMuxMonBitRatet = _NtcTsMuxMonBitRatet_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 3, 2, 1, 4),
    _NtcTsMuxMonBitRatet_Type()
)
ntcTsMuxMonBitRatet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsMuxMonBitRatet.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsMuxMonBitRatet.setUnits("bps")


class _NtcTsMuxMonBWOccopation_Type(Unsigned32):
    """Custom type ntcTsMuxMonBWOccopation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NtcTsMuxMonBWOccopation_Type.__name__ = "Unsigned32"
_NtcTsMuxMonBWOccopation_Object = MibTableColumn
ntcTsMuxMonBWOccopation = _NtcTsMuxMonBWOccopation_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 3, 2, 1, 5),
    _NtcTsMuxMonBWOccopation_Type()
)
ntcTsMuxMonBWOccopation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsMuxMonBWOccopation.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsMuxMonBWOccopation.setUnits("%")
_NtcTsMuxCarrierId_ObjectIdentity = ObjectIdentity
ntcTsMuxCarrierId = _NtcTsMuxCarrierId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 4)
)
if mibBuilder.loadTexts:
    ntcTsMuxCarrierId.setStatus("current")


class _NtcTsMuxCarIdEnable_Type(NtcEnable):
    """Custom type ntcTsMuxCarIdEnable based on NtcEnable"""
    defaultValue = 0


_NtcTsMuxCarIdEnable_Type.__name__ = "NtcEnable"
_NtcTsMuxCarIdEnable_Object = MibScalar
ntcTsMuxCarIdEnable = _NtcTsMuxCarIdEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 4, 1),
    _NtcTsMuxCarIdEnable_Type()
)
ntcTsMuxCarIdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxCarIdEnable.setStatus("current")


class _NtcTsMuxCarIdDescriptorTag_Type(Unsigned32):
    """Custom type ntcTsMuxCarIdDescriptorTag based on Unsigned32"""
    defaultValue = 196

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(192, 254),
    )


_NtcTsMuxCarIdDescriptorTag_Type.__name__ = "Unsigned32"
_NtcTsMuxCarIdDescriptorTag_Object = MibScalar
ntcTsMuxCarIdDescriptorTag = _NtcTsMuxCarIdDescriptorTag_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 4, 2),
    _NtcTsMuxCarIdDescriptorTag_Type()
)
ntcTsMuxCarIdDescriptorTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxCarIdDescriptorTag.setStatus("current")


class _NtcTsMuxCarIdModMfg_Type(DisplayString):
    """Custom type ntcTsMuxCarIdModMfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_NtcTsMuxCarIdModMfg_Type.__name__ = "DisplayString"
_NtcTsMuxCarIdModMfg_Object = MibScalar
ntcTsMuxCarIdModMfg = _NtcTsMuxCarIdModMfg_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 4, 3),
    _NtcTsMuxCarIdModMfg_Type()
)
ntcTsMuxCarIdModMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsMuxCarIdModMfg.setStatus("current")


class _NtcTsMuxCarIdModSerialNr_Type(DisplayString):
    """Custom type ntcTsMuxCarIdModSerialNr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_NtcTsMuxCarIdModSerialNr_Type.__name__ = "DisplayString"
_NtcTsMuxCarIdModSerialNr_Object = MibScalar
ntcTsMuxCarIdModSerialNr = _NtcTsMuxCarIdModSerialNr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 4, 4),
    _NtcTsMuxCarIdModSerialNr_Type()
)
ntcTsMuxCarIdModSerialNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsMuxCarIdModSerialNr.setStatus("current")


class _NtcTsMuxCarIdCarrierIdentifier_Type(DisplayString):
    """Custom type ntcTsMuxCarIdCarrierIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_NtcTsMuxCarIdCarrierIdentifier_Type.__name__ = "DisplayString"
_NtcTsMuxCarIdCarrierIdentifier_Object = MibScalar
ntcTsMuxCarIdCarrierIdentifier = _NtcTsMuxCarIdCarrierIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 4, 5),
    _NtcTsMuxCarIdCarrierIdentifier_Type()
)
ntcTsMuxCarIdCarrierIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxCarIdCarrierIdentifier.setStatus("current")


class _NtcTsMuxCarIdTelephoneNr_Type(DisplayString):
    """Custom type ntcTsMuxCarIdTelephoneNr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_NtcTsMuxCarIdTelephoneNr_Type.__name__ = "DisplayString"
_NtcTsMuxCarIdTelephoneNr_Object = MibScalar
ntcTsMuxCarIdTelephoneNr = _NtcTsMuxCarIdTelephoneNr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 4, 6),
    _NtcTsMuxCarIdTelephoneNr_Type()
)
ntcTsMuxCarIdTelephoneNr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxCarIdTelephoneNr.setStatus("current")


class _NtcTsMuxCarIdLongitude_Type(Float32TC):
    """Custom type ntcTsMuxCarIdLongitude based on Float32TC"""
    defaultHexValue = "00000000"


_NtcTsMuxCarIdLongitude_Type.__name__ = "Float32TC"
_NtcTsMuxCarIdLongitude_Object = MibScalar
ntcTsMuxCarIdLongitude = _NtcTsMuxCarIdLongitude_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 4, 7),
    _NtcTsMuxCarIdLongitude_Type()
)
ntcTsMuxCarIdLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxCarIdLongitude.setStatus("current")


class _NtcTsMuxCarIdLatitude_Type(Float32TC):
    """Custom type ntcTsMuxCarIdLatitude based on Float32TC"""
    defaultHexValue = "00000000"


_NtcTsMuxCarIdLatitude_Type.__name__ = "Float32TC"
_NtcTsMuxCarIdLatitude_Object = MibScalar
ntcTsMuxCarIdLatitude = _NtcTsMuxCarIdLatitude_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 4, 8),
    _NtcTsMuxCarIdLatitude_Type()
)
ntcTsMuxCarIdLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxCarIdLatitude.setStatus("current")


class _NtcTsMuxCarIdUserInfo_Type(DisplayString):
    """Custom type ntcTsMuxCarIdUserInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_NtcTsMuxCarIdUserInfo_Type.__name__ = "DisplayString"
_NtcTsMuxCarIdUserInfo_Object = MibScalar
ntcTsMuxCarIdUserInfo = _NtcTsMuxCarIdUserInfo_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 4, 9),
    _NtcTsMuxCarIdUserInfo_Type()
)
ntcTsMuxCarIdUserInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxCarIdUserInfo.setStatus("current")


class _NtcTsMuxCarIdLongitudeString_Type(DisplayString):
    """Custom type ntcTsMuxCarIdLongitudeString based on DisplayString"""
    defaultValue = OctetString("0.0000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_NtcTsMuxCarIdLongitudeString_Type.__name__ = "DisplayString"
_NtcTsMuxCarIdLongitudeString_Object = MibScalar
ntcTsMuxCarIdLongitudeString = _NtcTsMuxCarIdLongitudeString_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 4, 10),
    _NtcTsMuxCarIdLongitudeString_Type()
)
ntcTsMuxCarIdLongitudeString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxCarIdLongitudeString.setStatus("current")


class _NtcTsMuxCarIdLatitudeString_Type(DisplayString):
    """Custom type ntcTsMuxCarIdLatitudeString based on DisplayString"""
    defaultValue = OctetString("0.0000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_NtcTsMuxCarIdLatitudeString_Type.__name__ = "DisplayString"
_NtcTsMuxCarIdLatitudeString_Object = MibScalar
ntcTsMuxCarIdLatitudeString = _NtcTsMuxCarIdLatitudeString_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 4, 11),
    _NtcTsMuxCarIdLatitudeString_Type()
)
ntcTsMuxCarIdLatitudeString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxCarIdLatitudeString.setStatus("current")
_NtcTsMuxSignalling_ObjectIdentity = ObjectIdentity
ntcTsMuxSignalling = _NtcTsMuxSignalling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 5)
)
if mibBuilder.loadTexts:
    ntcTsMuxSignalling.setStatus("current")


class _NtcTsMuxSigNetworkId_Type(Unsigned32):
    """Custom type ntcTsMuxSigNetworkId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NtcTsMuxSigNetworkId_Type.__name__ = "Unsigned32"
_NtcTsMuxSigNetworkId_Object = MibScalar
ntcTsMuxSigNetworkId = _NtcTsMuxSigNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 5, 1),
    _NtcTsMuxSigNetworkId_Type()
)
ntcTsMuxSigNetworkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxSigNetworkId.setStatus("current")


class _NtcTsMuxSigTransportStreamId_Type(Unsigned32):
    """Custom type ntcTsMuxSigTransportStreamId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NtcTsMuxSigTransportStreamId_Type.__name__ = "Unsigned32"
_NtcTsMuxSigTransportStreamId_Object = MibScalar
ntcTsMuxSigTransportStreamId = _NtcTsMuxSigTransportStreamId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 5, 2),
    _NtcTsMuxSigTransportStreamId_Type()
)
ntcTsMuxSigTransportStreamId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxSigTransportStreamId.setStatus("current")


class _NtcTsMuxSigPatRepetitionRate_Type(Unsigned32):
    """Custom type ntcTsMuxSigPatRepetitionRate based on Unsigned32"""
    defaultValue = 400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 500),
    )


_NtcTsMuxSigPatRepetitionRate_Type.__name__ = "Unsigned32"
_NtcTsMuxSigPatRepetitionRate_Object = MibScalar
ntcTsMuxSigPatRepetitionRate = _NtcTsMuxSigPatRepetitionRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 5, 3),
    _NtcTsMuxSigPatRepetitionRate_Type()
)
ntcTsMuxSigPatRepetitionRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxSigPatRepetitionRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsMuxSigPatRepetitionRate.setUnits("ms")


class _NtcTsMuxSigSdtRepetitionRate_Type(Unsigned32):
    """Custom type ntcTsMuxSigSdtRepetitionRate based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 2000),
    )


_NtcTsMuxSigSdtRepetitionRate_Type.__name__ = "Unsigned32"
_NtcTsMuxSigSdtRepetitionRate_Object = MibScalar
ntcTsMuxSigSdtRepetitionRate = _NtcTsMuxSigSdtRepetitionRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 5, 4),
    _NtcTsMuxSigSdtRepetitionRate_Type()
)
ntcTsMuxSigSdtRepetitionRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxSigSdtRepetitionRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsMuxSigSdtRepetitionRate.setUnits("ms")


class _NtcTsMuxSigPmtRepetitionRate_Type(Unsigned32):
    """Custom type ntcTsMuxSigPmtRepetitionRate based on Unsigned32"""
    defaultValue = 400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 500),
    )


_NtcTsMuxSigPmtRepetitionRate_Type.__name__ = "Unsigned32"
_NtcTsMuxSigPmtRepetitionRate_Object = MibScalar
ntcTsMuxSigPmtRepetitionRate = _NtcTsMuxSigPmtRepetitionRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 5, 5),
    _NtcTsMuxSigPmtRepetitionRate_Type()
)
ntcTsMuxSigPmtRepetitionRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxSigPmtRepetitionRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsMuxSigPmtRepetitionRate.setUnits("ms")
_NtcTsMuxAlarm_ObjectIdentity = ObjectIdentity
ntcTsMuxAlarm = _NtcTsMuxAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 6)
)
if mibBuilder.loadTexts:
    ntcTsMuxAlarm.setStatus("current")
_NtcTsMuxAlmLocalPidOnInput_Type = NtcAlarmState
_NtcTsMuxAlmLocalPidOnInput_Object = MibScalar
ntcTsMuxAlmLocalPidOnInput = _NtcTsMuxAlmLocalPidOnInput_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 6, 1),
    _NtcTsMuxAlmLocalPidOnInput_Type()
)
ntcTsMuxAlmLocalPidOnInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsMuxAlmLocalPidOnInput.setStatus("current")
_NtcTsMuxAlmSignalTableProcError_Type = NtcAlarmState
_NtcTsMuxAlmSignalTableProcError_Object = MibScalar
ntcTsMuxAlmSignalTableProcError = _NtcTsMuxAlmSignalTableProcError_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 6, 2),
    _NtcTsMuxAlmSignalTableProcError_Type()
)
ntcTsMuxAlmSignalTableProcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsMuxAlmSignalTableProcError.setStatus("current")
_NtcTsMuxAlmSignalOverflow_Type = NtcAlarmState
_NtcTsMuxAlmSignalOverflow_Object = MibScalar
ntcTsMuxAlmSignalOverflow = _NtcTsMuxAlmSignalOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 6, 3),
    _NtcTsMuxAlmSignalOverflow_Type()
)
ntcTsMuxAlmSignalOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsMuxAlmSignalOverflow.setStatus("current")
_NtcTsMuxAlmBufferOverflow_Type = NtcAlarmState
_NtcTsMuxAlmBufferOverflow_Object = MibScalar
ntcTsMuxAlmBufferOverflow = _NtcTsMuxAlmBufferOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 6, 4),
    _NtcTsMuxAlmBufferOverflow_Type()
)
ntcTsMuxAlmBufferOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsMuxAlmBufferOverflow.setStatus("current")
_NtcTsMuxNpRateOutRange_Type = NtcAlarmState
_NtcTsMuxNpRateOutRange_Object = MibScalar
ntcTsMuxNpRateOutRange = _NtcTsMuxNpRateOutRange_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 6, 5),
    _NtcTsMuxNpRateOutRange_Type()
)
ntcTsMuxNpRateOutRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsMuxNpRateOutRange.setStatus("current")
_NtcTsMuxNpRangeThr_ObjectIdentity = ObjectIdentity
ntcTsMuxNpRangeThr = _NtcTsMuxNpRangeThr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 7)
)
if mibBuilder.loadTexts:
    ntcTsMuxNpRangeThr.setStatus("current")


class _NtcTsMuxNpRangeThrEnable_Type(NtcEnable):
    """Custom type ntcTsMuxNpRangeThrEnable based on NtcEnable"""
    defaultValue = 0


_NtcTsMuxNpRangeThrEnable_Type.__name__ = "NtcEnable"
_NtcTsMuxNpRangeThrEnable_Object = MibScalar
ntcTsMuxNpRangeThrEnable = _NtcTsMuxNpRangeThrEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 7, 1),
    _NtcTsMuxNpRangeThrEnable_Type()
)
ntcTsMuxNpRangeThrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxNpRangeThrEnable.setStatus("current")


class _NtcTsMuxNpRangeThrMinRate_Type(Unsigned32):
    """Custom type ntcTsMuxNpRangeThrMinRate based on Unsigned32"""
    defaultValue = 0


_NtcTsMuxNpRangeThrMinRate_Type.__name__ = "Unsigned32"
_NtcTsMuxNpRangeThrMinRate_Object = MibScalar
ntcTsMuxNpRangeThrMinRate = _NtcTsMuxNpRangeThrMinRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 7, 2),
    _NtcTsMuxNpRangeThrMinRate_Type()
)
ntcTsMuxNpRangeThrMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxNpRangeThrMinRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsMuxNpRangeThrMinRate.setUnits("bps")


class _NtcTsMuxNpRangeThrMaxRate_Type(Unsigned32):
    """Custom type ntcTsMuxNpRangeThrMaxRate based on Unsigned32"""
    defaultValue = 0


_NtcTsMuxNpRangeThrMaxRate_Type.__name__ = "Unsigned32"
_NtcTsMuxNpRangeThrMaxRate_Object = MibScalar
ntcTsMuxNpRangeThrMaxRate = _NtcTsMuxNpRangeThrMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 7, 3),
    _NtcTsMuxNpRangeThrMaxRate_Type()
)
ntcTsMuxNpRangeThrMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxNpRangeThrMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsMuxNpRangeThrMaxRate.setUnits("bps")


class _NtcTsMuxNpRangeTimeWindow_Type(Integer32):
    """Custom type ntcTsMuxNpRangeTimeWindow based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_NtcTsMuxNpRangeTimeWindow_Type.__name__ = "Integer32"
_NtcTsMuxNpRangeTimeWindow_Object = MibScalar
ntcTsMuxNpRangeTimeWindow = _NtcTsMuxNpRangeTimeWindow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 1, 7, 4),
    _NtcTsMuxNpRangeTimeWindow_Type()
)
ntcTsMuxNpRangeTimeWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsMuxNpRangeTimeWindow.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsMuxNpRangeTimeWindow.setUnits("s")
_NtcTsMuxConformance_ObjectIdentity = ObjectIdentity
ntcTsMuxConformance = _NtcTsMuxConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 2)
)
if mibBuilder.loadTexts:
    ntcTsMuxConformance.setStatus("current")
_NtcTsMuxConfCompliance_ObjectIdentity = ObjectIdentity
ntcTsMuxConfCompliance = _NtcTsMuxConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 2, 1)
)
if mibBuilder.loadTexts:
    ntcTsMuxConfCompliance.setStatus("current")
_NtcTsMuxConfGroup_ObjectIdentity = ObjectIdentity
ntcTsMuxConfGroup = _NtcTsMuxConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 2, 2)
)
if mibBuilder.loadTexts:
    ntcTsMuxConfGroup.setStatus("current")

# Managed Objects groups

ntcTsMuxConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 2, 2, 1)
)
ntcTsMuxConfGrpV1Standard.setObjects(
      *(("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxRaEnable"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxRaNullPktDrop"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxRaPcrRestamp"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxMonResetCounters"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxMonPacketCount"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxMonPacketRate"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxMonBitRatet"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxMonBWOccopation"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxCarIdEnable"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxCarIdDescriptorTag"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxCarIdModMfg"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxCarIdModSerialNr"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxCarIdCarrierIdentifier"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxCarIdTelephoneNr"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxCarIdLongitude"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxCarIdLatitude"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxCarIdUserInfo"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxCarIdLongitudeString"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxCarIdLatitudeString"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxSigNetworkId"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxSigTransportStreamId"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxSigPatRepetitionRate"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxSigSdtRepetitionRate"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxSigPmtRepetitionRate"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxAlmLocalPidOnInput"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxAlmSignalTableProcError"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxAlmSignalOverflow"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxAlmBufferOverflow"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxNpRateOutRange"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxNpRangeThrEnable"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxNpRangeThrMinRate"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxNpRangeThrMaxRate"),
        ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxNpRangeTimeWindow"))
)
if mibBuilder.loadTexts:
    ntcTsMuxConfGrpV1Standard.setStatus("current")

ntcTsMuxConfGrpObsolete = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 2, 2, 2)
)
ntcTsMuxConfGrpObsolete.setObjects(
    ("NEWTEC-TSMULTIPLEXING-MIB", "ntcInputSelectionEnable")
)
if mibBuilder.loadTexts:
    ntcTsMuxConfGrpObsolete.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcTsMuxConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1600, 2, 1, 1)
)
ntcTsMuxConfCompV1Standard.setObjects(
    ("NEWTEC-TSMULTIPLEXING-MIB", "ntcTsMuxConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcTsMuxConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-TSMULTIPLEXING-MIB",
    **{"ntcTsMultiplexing": ntcTsMultiplexing,
       "ntcTsMuxObjects": ntcTsMuxObjects,
       "ntcInputSelectionTable": ntcInputSelectionTable,
       "ntcInputSelectionEntry": ntcInputSelectionEntry,
       "ntcInputSelectionInputType": ntcInputSelectionInputType,
       "ntcInputSelectionEnable": ntcInputSelectionEnable,
       "ntcTsMuxRateAdapter": ntcTsMuxRateAdapter,
       "ntcTsMuxRaEnable": ntcTsMuxRaEnable,
       "ntcTsMuxRaNullPktDrop": ntcTsMuxRaNullPktDrop,
       "ntcTsMuxRaPcrRestamp": ntcTsMuxRaPcrRestamp,
       "ntcTsMuxMonitor": ntcTsMuxMonitor,
       "ntcTsMuxMonResetCounters": ntcTsMuxMonResetCounters,
       "ntcTsMuxMonStatisticsTable": ntcTsMuxMonStatisticsTable,
       "ntcTsMuxMonStatisticsEntry": ntcTsMuxMonStatisticsEntry,
       "ntcTsMuxMonStatisticsType": ntcTsMuxMonStatisticsType,
       "ntcTsMuxMonPacketCount": ntcTsMuxMonPacketCount,
       "ntcTsMuxMonPacketRate": ntcTsMuxMonPacketRate,
       "ntcTsMuxMonBitRatet": ntcTsMuxMonBitRatet,
       "ntcTsMuxMonBWOccopation": ntcTsMuxMonBWOccopation,
       "ntcTsMuxCarrierId": ntcTsMuxCarrierId,
       "ntcTsMuxCarIdEnable": ntcTsMuxCarIdEnable,
       "ntcTsMuxCarIdDescriptorTag": ntcTsMuxCarIdDescriptorTag,
       "ntcTsMuxCarIdModMfg": ntcTsMuxCarIdModMfg,
       "ntcTsMuxCarIdModSerialNr": ntcTsMuxCarIdModSerialNr,
       "ntcTsMuxCarIdCarrierIdentifier": ntcTsMuxCarIdCarrierIdentifier,
       "ntcTsMuxCarIdTelephoneNr": ntcTsMuxCarIdTelephoneNr,
       "ntcTsMuxCarIdLongitude": ntcTsMuxCarIdLongitude,
       "ntcTsMuxCarIdLatitude": ntcTsMuxCarIdLatitude,
       "ntcTsMuxCarIdUserInfo": ntcTsMuxCarIdUserInfo,
       "ntcTsMuxCarIdLongitudeString": ntcTsMuxCarIdLongitudeString,
       "ntcTsMuxCarIdLatitudeString": ntcTsMuxCarIdLatitudeString,
       "ntcTsMuxSignalling": ntcTsMuxSignalling,
       "ntcTsMuxSigNetworkId": ntcTsMuxSigNetworkId,
       "ntcTsMuxSigTransportStreamId": ntcTsMuxSigTransportStreamId,
       "ntcTsMuxSigPatRepetitionRate": ntcTsMuxSigPatRepetitionRate,
       "ntcTsMuxSigSdtRepetitionRate": ntcTsMuxSigSdtRepetitionRate,
       "ntcTsMuxSigPmtRepetitionRate": ntcTsMuxSigPmtRepetitionRate,
       "ntcTsMuxAlarm": ntcTsMuxAlarm,
       "ntcTsMuxAlmLocalPidOnInput": ntcTsMuxAlmLocalPidOnInput,
       "ntcTsMuxAlmSignalTableProcError": ntcTsMuxAlmSignalTableProcError,
       "ntcTsMuxAlmSignalOverflow": ntcTsMuxAlmSignalOverflow,
       "ntcTsMuxAlmBufferOverflow": ntcTsMuxAlmBufferOverflow,
       "ntcTsMuxNpRateOutRange": ntcTsMuxNpRateOutRange,
       "ntcTsMuxNpRangeThr": ntcTsMuxNpRangeThr,
       "ntcTsMuxNpRangeThrEnable": ntcTsMuxNpRangeThrEnable,
       "ntcTsMuxNpRangeThrMinRate": ntcTsMuxNpRangeThrMinRate,
       "ntcTsMuxNpRangeThrMaxRate": ntcTsMuxNpRangeThrMaxRate,
       "ntcTsMuxNpRangeTimeWindow": ntcTsMuxNpRangeTimeWindow,
       "ntcTsMuxConformance": ntcTsMuxConformance,
       "ntcTsMuxConfCompliance": ntcTsMuxConfCompliance,
       "ntcTsMuxConfCompV1Standard": ntcTsMuxConfCompV1Standard,
       "ntcTsMuxConfGroup": ntcTsMuxConfGroup,
       "ntcTsMuxConfGrpV1Standard": ntcTsMuxConfGrpV1Standard,
       "ntcTsMuxConfGrpObsolete": ntcTsMuxConfGrpObsolete}
)
