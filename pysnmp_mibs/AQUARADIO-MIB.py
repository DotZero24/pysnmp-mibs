# SNMP MIB module (AQUARADIO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinet/AQUARADIO-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:01 2025
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

(sysSerialNumber,
 sysTrapSequence) = mibBuilder.importSymbols(
    "AQUASYSTEM-MIB",
    "sysSerialNumber",
    "sysTrapSequence")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(wanflex,) = mibBuilder.importSymbols(
    "INFINET-MIB",
    "wanflex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

aquaradioMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2)
)
if mibBuilder.loadTexts:
    aquaradioMIB.setRevisions(
        ("2014-09-22 05:56",
         "2013-07-26 04:27",
         "2013-04-08 11:40",
         "2013-04-08 10:59",
         "2009-11-10 11:56",
         "2009-10-30 08:38",
         "2009-05-12 11:22",
         "2007-11-08 13:09",
         "2004-10-11 16:28")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RadioSID(TextualConvention, Integer32):
    status = "current"
    displayHint = "x"


# MIB Managed Objects in the order of their OIDs

_RmPropertiesTable_Object = MibTable
rmPropertiesTable = _RmPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rmPropertiesTable.setStatus("current")
_RmPropertiesEntry_Object = MibTableRow
rmPropertiesEntry = _RmPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1)
)
rmPropertiesEntry.setIndexNames(
    (0, "AQUARADIO-MIB", "rmPropertiesIfIndex"),
)
if mibBuilder.loadTexts:
    rmPropertiesEntry.setStatus("current")


class _RmPropertiesIfIndex_Type(Integer32):
    """Custom type rmPropertiesIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RmPropertiesIfIndex_Type.__name__ = "Integer32"
_RmPropertiesIfIndex_Object = MibTableColumn
rmPropertiesIfIndex = _RmPropertiesIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 1),
    _RmPropertiesIfIndex_Type()
)
rmPropertiesIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmPropertiesIfIndex.setStatus("current")
_RmType_Type = OctetString
_RmType_Object = MibTableColumn
rmType = _RmType_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 2),
    _RmType_Type()
)
rmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmType.setStatus("current")
_RmFrequency_Type = Integer32
_RmFrequency_Object = MibTableColumn
rmFrequency = _RmFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 3),
    _RmFrequency_Type()
)
rmFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmFrequency.setStatus("current")
if mibBuilder.loadTexts:
    rmFrequency.setUnits("KHz")
_RmBitRate_Type = Integer32
_RmBitRate_Object = MibTableColumn
rmBitRate = _RmBitRate_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 4),
    _RmBitRate_Type()
)
rmBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmBitRate.setStatus("current")
_RmSid_Type = RadioSID
_RmSid_Object = MibTableColumn
rmSid = _RmSid_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 5),
    _RmSid_Type()
)
rmSid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmSid.setStatus("current")
_RmCurPowerLevel_Type = Integer32
_RmCurPowerLevel_Object = MibTableColumn
rmCurPowerLevel = _RmCurPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 6),
    _RmCurPowerLevel_Type()
)
rmCurPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmCurPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    rmCurPowerLevel.setUnits("tenth dBm.")


class _RmModulation_Type(Integer32):
    """Custom type rmModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("irrelevant", 0),
          ("cck", 1),
          ("mok", 2))
    )


_RmModulation_Type.__name__ = "Integer32"
_RmModulation_Object = MibTableColumn
rmModulation = _RmModulation_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 7),
    _RmModulation_Type()
)
rmModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmModulation.setStatus("current")


class _RmAntenna_Type(Integer32):
    """Custom type rmAntenna based on Integer32"""
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
        *(("right", 1),
          ("left", 2),
          ("div", 3),
          ("both", 4),
          ("txr", 5),
          ("txl", 6))
    )


_RmAntenna_Type.__name__ = "Integer32"
_RmAntenna_Object = MibTableColumn
rmAntenna = _RmAntenna_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 8),
    _RmAntenna_Type()
)
rmAntenna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmAntenna.setStatus("current")
_RmDistance_Type = Integer32
_RmDistance_Object = MibTableColumn
rmDistance = _RmDistance_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 9),
    _RmDistance_Type()
)
rmDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmDistance.setStatus("current")
if mibBuilder.loadTexts:
    rmDistance.setUnits("kilometers")


class _RmBurst_Type(Integer32):
    """Custom type rmBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_RmBurst_Type.__name__ = "Integer32"
_RmBurst_Object = MibTableColumn
rmBurst = _RmBurst_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 10),
    _RmBurst_Type()
)
rmBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmBurst.setStatus("current")


class _RmLongRange_Type(Integer32):
    """Custom type rmLongRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_RmLongRange_Type.__name__ = "Integer32"
_RmLongRange_Object = MibTableColumn
rmLongRange = _RmLongRange_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 11),
    _RmLongRange_Type()
)
rmLongRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmLongRange.setStatus("current")


class _RmPowerCtl_Type(Integer32):
    """Custom type rmPowerCtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_RmPowerCtl_Type.__name__ = "Integer32"
_RmPowerCtl_Object = MibTableColumn
rmPowerCtl = _RmPowerCtl_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 12),
    _RmPowerCtl_Type()
)
rmPowerCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmPowerCtl.setStatus("current")
_RmTXRT_Type = Integer32
_RmTXRT_Object = MibTableColumn
rmTXRT = _RmTXRT_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 13),
    _RmTXRT_Type()
)
rmTXRT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmTXRT.setStatus("current")
_RmTXVRT_Type = Integer32
_RmTXVRT_Object = MibTableColumn
rmTXVRT = _RmTXVRT_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 14),
    _RmTXVRT_Type()
)
rmTXVRT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmTXVRT.setStatus("current")


class _RmPTP_Type(Integer32):
    """Custom type rmPTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_RmPTP_Type.__name__ = "Integer32"
_RmPTP_Object = MibTableColumn
rmPTP = _RmPTP_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 15),
    _RmPTP_Type()
)
rmPTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmPTP.setStatus("current")


class _RmWOCD_Type(Integer32):
    """Custom type rmWOCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_RmWOCD_Type.__name__ = "Integer32"
_RmWOCD_Object = MibTableColumn
rmWOCD = _RmWOCD_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 16),
    _RmWOCD_Type()
)
rmWOCD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmWOCD.setStatus("current")


class _RmBCsid_Type(Integer32):
    """Custom type rmBCsid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_RmBCsid_Type.__name__ = "Integer32"
_RmBCsid_Object = MibTableColumn
rmBCsid = _RmBCsid_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 17),
    _RmBCsid_Type()
)
rmBCsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmBCsid.setStatus("current")


class _RmDistanceAuto_Type(Integer32):
    """Custom type rmDistanceAuto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_RmDistanceAuto_Type.__name__ = "Integer32"
_RmDistanceAuto_Object = MibTableColumn
rmDistanceAuto = _RmDistanceAuto_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 18),
    _RmDistanceAuto_Type()
)
rmDistanceAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmDistanceAuto.setStatus("current")
_RmNoiseFloor_Type = Integer32
_RmNoiseFloor_Object = MibTableColumn
rmNoiseFloor = _RmNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 19),
    _RmNoiseFloor_Type()
)
rmNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmNoiseFloor.setStatus("current")
_RmBandwidth_Type = Unsigned32
_RmBandwidth_Object = MibTableColumn
rmBandwidth = _RmBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 20),
    _RmBandwidth_Type()
)
rmBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    rmBandwidth.setUnits("KHz")


class _RmChainMode_Type(Integer32):
    """Custom type rmChainMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("miso", 1),
          ("mimo", 2))
    )


_RmChainMode_Type.__name__ = "Integer32"
_RmChainMode_Object = MibTableColumn
rmChainMode = _RmChainMode_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 21),
    _RmChainMode_Type()
)
rmChainMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmChainMode.setStatus("current")


class _RmSelectChannel_Type(Integer32):
    """Custom type rmSelectChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reading-stub", 0),
          ("new", 1),
          ("renew", 2))
    )


_RmSelectChannel_Type.__name__ = "Integer32"
_RmSelectChannel_Object = MibTableColumn
rmSelectChannel = _RmSelectChannel_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 1, 1, 22),
    _RmSelectChannel_Type()
)
rmSelectChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmSelectChannel.setStatus("current")
_RmPowerLevelsTable_Object = MibTable
rmPowerLevelsTable = _RmPowerLevelsTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    rmPowerLevelsTable.setStatus("current")
_RmPowerLevelsEntry_Object = MibTableRow
rmPowerLevelsEntry = _RmPowerLevelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 4, 1)
)
rmPowerLevelsEntry.setIndexNames(
    (0, "AQUARADIO-MIB", "rmPowerLevelsIfIndex"),
    (0, "AQUARADIO-MIB", "rmPowerLevelsValIndex"),
)
if mibBuilder.loadTexts:
    rmPowerLevelsEntry.setStatus("current")


class _RmPowerLevelsIfIndex_Type(Integer32):
    """Custom type rmPowerLevelsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RmPowerLevelsIfIndex_Type.__name__ = "Integer32"
_RmPowerLevelsIfIndex_Object = MibTableColumn
rmPowerLevelsIfIndex = _RmPowerLevelsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 4, 1, 1),
    _RmPowerLevelsIfIndex_Type()
)
rmPowerLevelsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmPowerLevelsIfIndex.setStatus("current")


class _RmPowerLevelsValIndex_Type(Integer32):
    """Custom type rmPowerLevelsValIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RmPowerLevelsValIndex_Type.__name__ = "Integer32"
_RmPowerLevelsValIndex_Object = MibTableColumn
rmPowerLevelsValIndex = _RmPowerLevelsValIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 4, 1, 2),
    _RmPowerLevelsValIndex_Type()
)
rmPowerLevelsValIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmPowerLevelsValIndex.setStatus("current")
_RmPowerLevelsPower_Type = Integer32
_RmPowerLevelsPower_Object = MibTableColumn
rmPowerLevelsPower = _RmPowerLevelsPower_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 4, 1, 3),
    _RmPowerLevelsPower_Type()
)
rmPowerLevelsPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmPowerLevelsPower.setStatus("current")
if mibBuilder.loadTexts:
    rmPowerLevelsPower.setUnits("tenth dBm.")
_RmFrequenciesTable_Object = MibTable
rmFrequenciesTable = _RmFrequenciesTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    rmFrequenciesTable.setStatus("current")
_RmFrequenciesEntry_Object = MibTableRow
rmFrequenciesEntry = _RmFrequenciesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 5, 1)
)
rmFrequenciesEntry.setIndexNames(
    (0, "AQUARADIO-MIB", "rmFrequenciesIfIndex"),
    (0, "AQUARADIO-MIB", "rmFrequenciesValIndex"),
)
if mibBuilder.loadTexts:
    rmFrequenciesEntry.setStatus("current")


class _RmFrequenciesIfIndex_Type(Integer32):
    """Custom type rmFrequenciesIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RmFrequenciesIfIndex_Type.__name__ = "Integer32"
_RmFrequenciesIfIndex_Object = MibTableColumn
rmFrequenciesIfIndex = _RmFrequenciesIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 5, 1, 1),
    _RmFrequenciesIfIndex_Type()
)
rmFrequenciesIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmFrequenciesIfIndex.setStatus("current")


class _RmFrequenciesValIndex_Type(Integer32):
    """Custom type rmFrequenciesValIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RmFrequenciesValIndex_Type.__name__ = "Integer32"
_RmFrequenciesValIndex_Object = MibTableColumn
rmFrequenciesValIndex = _RmFrequenciesValIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 5, 1, 2),
    _RmFrequenciesValIndex_Type()
)
rmFrequenciesValIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmFrequenciesValIndex.setStatus("current")
_RmFrequenciesFreq_Type = Integer32
_RmFrequenciesFreq_Object = MibTableColumn
rmFrequenciesFreq = _RmFrequenciesFreq_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 5, 1, 3),
    _RmFrequenciesFreq_Type()
)
rmFrequenciesFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmFrequenciesFreq.setStatus("current")
_RmBitratesTable_Object = MibTable
rmBitratesTable = _RmBitratesTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    rmBitratesTable.setStatus("current")
_RmBitratesEntry_Object = MibTableRow
rmBitratesEntry = _RmBitratesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 6, 1)
)
rmBitratesEntry.setIndexNames(
    (0, "AQUARADIO-MIB", "rmBitratesIfIndex"),
    (0, "AQUARADIO-MIB", "rmBitratesValIndex"),
)
if mibBuilder.loadTexts:
    rmBitratesEntry.setStatus("current")


class _RmBitratesIfIndex_Type(Integer32):
    """Custom type rmBitratesIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RmBitratesIfIndex_Type.__name__ = "Integer32"
_RmBitratesIfIndex_Object = MibTableColumn
rmBitratesIfIndex = _RmBitratesIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 6, 1, 1),
    _RmBitratesIfIndex_Type()
)
rmBitratesIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmBitratesIfIndex.setStatus("current")


class _RmBitratesValIndex_Type(Integer32):
    """Custom type rmBitratesValIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RmBitratesValIndex_Type.__name__ = "Integer32"
_RmBitratesValIndex_Object = MibTableColumn
rmBitratesValIndex = _RmBitratesValIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 6, 1, 2),
    _RmBitratesValIndex_Type()
)
rmBitratesValIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmBitratesValIndex.setStatus("current")
_RmBitratesBitrate_Type = Integer32
_RmBitratesBitrate_Object = MibTableColumn
rmBitratesBitrate = _RmBitratesBitrate_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 6, 1, 3),
    _RmBitratesBitrate_Type()
)
rmBitratesBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmBitratesBitrate.setStatus("current")
_RadioStatTable_Object = MibTable
radioStatTable = _RadioStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    radioStatTable.setStatus("current")
_RadioStatEntry_Object = MibTableRow
radioStatEntry = _RadioStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 7, 1)
)
radioStatEntry.setIndexNames(
    (0, "AQUARADIO-MIB", "radioStatMacAddress"),
)
if mibBuilder.loadTexts:
    radioStatEntry.setStatus("current")


class _RadioStatMacAddress_Type(OctetString):
    """Custom type radioStatMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RadioStatMacAddress_Type.__name__ = "OctetString"
_RadioStatMacAddress_Object = MibTableColumn
radioStatMacAddress = _RadioStatMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 7, 1, 1),
    _RadioStatMacAddress_Type()
)
radioStatMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioStatMacAddress.setStatus("current")
_RadioStatPackets_Type = Counter32
_RadioStatPackets_Object = MibTableColumn
radioStatPackets = _RadioStatPackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 7, 1, 2),
    _RadioStatPackets_Type()
)
radioStatPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioStatPackets.setStatus("current")
_RadioStatRepeats_Type = Counter32
_RadioStatRepeats_Object = MibTableColumn
radioStatRepeats = _RadioStatRepeats_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 7, 1, 3),
    _RadioStatRepeats_Type()
)
radioStatRepeats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioStatRepeats.setStatus("current")
_RadioStatRepeatPackets_Type = Counter32
_RadioStatRepeatPackets_Object = MibTableColumn
radioStatRepeatPackets = _RadioStatRepeatPackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 7, 1, 4),
    _RadioStatRepeatPackets_Type()
)
radioStatRepeatPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioStatRepeatPackets.setStatus("current")
_RadioStatBytes_Type = Counter32
_RadioStatBytes_Object = MibTableColumn
radioStatBytes = _RadioStatBytes_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 7, 1, 5),
    _RadioStatBytes_Type()
)
radioStatBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioStatBytes.setStatus("current")
_RadioStatRepeatBytes_Type = Counter32
_RadioStatRepeatBytes_Object = MibTableColumn
radioStatRepeatBytes = _RadioStatRepeatBytes_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 7, 1, 6),
    _RadioStatRepeatBytes_Type()
)
radioStatRepeatBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioStatRepeatBytes.setStatus("current")
_RadioStatErrors_Type = Counter32
_RadioStatErrors_Object = MibTableColumn
radioStatErrors = _RadioStatErrors_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 7, 1, 7),
    _RadioStatErrors_Type()
)
radioStatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioStatErrors.setStatus("current")
_RadioStatRecvPackets_Type = Counter32
_RadioStatRecvPackets_Object = MibTableColumn
radioStatRecvPackets = _RadioStatRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 7, 1, 8),
    _RadioStatRecvPackets_Type()
)
radioStatRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioStatRecvPackets.setStatus("current")
_RadioStatRecvBytes_Type = Counter32
_RadioStatRecvBytes_Object = MibTableColumn
radioStatRecvBytes = _RadioStatRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 7, 1, 9),
    _RadioStatRecvBytes_Type()
)
radioStatRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radioStatRecvBytes.setStatus("current")
_RmBandsTable_Object = MibTable
rmBandsTable = _RmBandsTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    rmBandsTable.setStatus("current")
_RmBandsEntry_Object = MibTableRow
rmBandsEntry = _RmBandsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 8, 1)
)
rmBandsEntry.setIndexNames(
    (0, "AQUARADIO-MIB", "rmBandsIfIndex"),
    (0, "AQUARADIO-MIB", "rmBandsValIndex"),
)
if mibBuilder.loadTexts:
    rmBandsEntry.setStatus("current")


class _RmBandsIfIndex_Type(Integer32):
    """Custom type rmBandsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RmBandsIfIndex_Type.__name__ = "Integer32"
_RmBandsIfIndex_Object = MibTableColumn
rmBandsIfIndex = _RmBandsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 8, 1, 1),
    _RmBandsIfIndex_Type()
)
rmBandsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmBandsIfIndex.setStatus("current")


class _RmBandsValIndex_Type(Integer32):
    """Custom type rmBandsValIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RmBandsValIndex_Type.__name__ = "Integer32"
_RmBandsValIndex_Object = MibTableColumn
rmBandsValIndex = _RmBandsValIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 8, 1, 2),
    _RmBandsValIndex_Type()
)
rmBandsValIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmBandsValIndex.setStatus("current")
_RmBandsBand_Type = Integer32
_RmBandsBand_Object = MibTableColumn
rmBandsBand = _RmBandsBand_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 8, 1, 3),
    _RmBandsBand_Type()
)
rmBandsBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmBandsBand.setStatus("current")
if mibBuilder.loadTexts:
    rmBandsBand.setUnits("Hz")
_AquaradioMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
aquaradioMIBNotificationsPrefix = _AquaradioMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 17)
)
_AquaradioMIBnotifications_ObjectIdentity = ObjectIdentity
aquaradioMIBnotifications = _AquaradioMIBnotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 17, 0)
)
_AquaradioMIBConformance_ObjectIdentity = ObjectIdentity
aquaradioMIBConformance = _AquaradioMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 18)
)
_AquaradioMIBCompliances_ObjectIdentity = ObjectIdentity
aquaradioMIBCompliances = _AquaradioMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 18, 1)
)
_AquaradioMIBGroups_ObjectIdentity = ObjectIdentity
aquaradioMIBGroups = _AquaradioMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 18, 2)
)

# Managed Objects groups

radioGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 18, 2, 1)
)
radioGroup.setObjects(
      *(("AQUARADIO-MIB", "rmPropertiesIfIndex"),
        ("AQUARADIO-MIB", "rmType"),
        ("AQUARADIO-MIB", "rmFrequency"),
        ("AQUARADIO-MIB", "rmBitRate"),
        ("AQUARADIO-MIB", "rmSid"),
        ("AQUARADIO-MIB", "rmCurPowerLevel"),
        ("AQUARADIO-MIB", "rmModulation"),
        ("AQUARADIO-MIB", "rmAntenna"),
        ("AQUARADIO-MIB", "rmDistance"),
        ("AQUARADIO-MIB", "rmBurst"),
        ("AQUARADIO-MIB", "rmLongRange"),
        ("AQUARADIO-MIB", "rmPowerCtl"),
        ("AQUARADIO-MIB", "rmTXRT"),
        ("AQUARADIO-MIB", "rmTXVRT"),
        ("AQUARADIO-MIB", "rmPTP"),
        ("AQUARADIO-MIB", "rmWOCD"),
        ("AQUARADIO-MIB", "rmBCsid"),
        ("AQUARADIO-MIB", "rmPowerLevelsIfIndex"),
        ("AQUARADIO-MIB", "rmPowerLevelsValIndex"),
        ("AQUARADIO-MIB", "rmPowerLevelsPower"),
        ("AQUARADIO-MIB", "rmFrequenciesIfIndex"),
        ("AQUARADIO-MIB", "rmFrequenciesValIndex"),
        ("AQUARADIO-MIB", "rmFrequenciesFreq"),
        ("AQUARADIO-MIB", "rmBitratesIfIndex"),
        ("AQUARADIO-MIB", "rmBitratesValIndex"),
        ("AQUARADIO-MIB", "rmBitratesBitrate"),
        ("AQUARADIO-MIB", "radioStatMacAddress"),
        ("AQUARADIO-MIB", "radioStatPackets"),
        ("AQUARADIO-MIB", "radioStatRepeats"),
        ("AQUARADIO-MIB", "radioStatRepeatPackets"),
        ("AQUARADIO-MIB", "radioStatBytes"),
        ("AQUARADIO-MIB", "radioStatRepeatBytes"),
        ("AQUARADIO-MIB", "radioStatErrors"),
        ("AQUARADIO-MIB", "radioStatRecvPackets"),
        ("AQUARADIO-MIB", "radioStatRecvBytes"),
        ("AQUARADIO-MIB", "rmDistanceAuto"),
        ("AQUARADIO-MIB", "rmNoiseFloor"),
        ("AQUARADIO-MIB", "rmBandwidth"),
        ("AQUARADIO-MIB", "rmChainMode"),
        ("AQUARADIO-MIB", "rmBandsIfIndex"),
        ("AQUARADIO-MIB", "rmBandsValIndex"),
        ("AQUARADIO-MIB", "rmBandsBand"),
        ("AQUARADIO-MIB", "rmSelectChannel"))
)
if mibBuilder.loadTexts:
    radioGroup.setStatus("current")


# Notification objects

radioFreqChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 17, 0, 1)
)
radioFreqChanged.setObjects(
      *(("AQUASYSTEM-MIB", "sysSerialNumber"),
        ("AQUASYSTEM-MIB", "sysTrapSequence"),
        ("AQUARADIO-MIB", "rmFrequency"),
        ("AQUARADIO-MIB", "rmPropertiesIfIndex"))
)
if mibBuilder.loadTexts:
    radioFreqChanged.setStatus(
        "current"
    )

radioBandChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 17, 0, 2)
)
radioBandChanged.setObjects(
      *(("AQUASYSTEM-MIB", "sysSerialNumber"),
        ("AQUASYSTEM-MIB", "sysTrapSequence"),
        ("AQUARADIO-MIB", "rmBandwidth"),
        ("AQUARADIO-MIB", "rmPropertiesIfIndex"))
)
if mibBuilder.loadTexts:
    radioBandChanged.setStatus(
        "current"
    )


# Notifications groups

aquaradioNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 18, 3)
)
aquaradioNotifications.setObjects(
      *(("AQUARADIO-MIB", "radioFreqChanged"),
        ("AQUARADIO-MIB", "radioBandChanged"))
)
if mibBuilder.loadTexts:
    aquaradioNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aquaradioMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 2, 18, 1, 1)
)
aquaradioMIBCompliance.setObjects(
    ("AQUARADIO-MIB", "radioGroup")
)
if mibBuilder.loadTexts:
    aquaradioMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AQUARADIO-MIB",
    **{"RadioSID": RadioSID,
       "aquaradioMIB": aquaradioMIB,
       "rmPropertiesTable": rmPropertiesTable,
       "rmPropertiesEntry": rmPropertiesEntry,
       "rmPropertiesIfIndex": rmPropertiesIfIndex,
       "rmType": rmType,
       "rmFrequency": rmFrequency,
       "rmBitRate": rmBitRate,
       "rmSid": rmSid,
       "rmCurPowerLevel": rmCurPowerLevel,
       "rmModulation": rmModulation,
       "rmAntenna": rmAntenna,
       "rmDistance": rmDistance,
       "rmBurst": rmBurst,
       "rmLongRange": rmLongRange,
       "rmPowerCtl": rmPowerCtl,
       "rmTXRT": rmTXRT,
       "rmTXVRT": rmTXVRT,
       "rmPTP": rmPTP,
       "rmWOCD": rmWOCD,
       "rmBCsid": rmBCsid,
       "rmDistanceAuto": rmDistanceAuto,
       "rmNoiseFloor": rmNoiseFloor,
       "rmBandwidth": rmBandwidth,
       "rmChainMode": rmChainMode,
       "rmSelectChannel": rmSelectChannel,
       "rmPowerLevelsTable": rmPowerLevelsTable,
       "rmPowerLevelsEntry": rmPowerLevelsEntry,
       "rmPowerLevelsIfIndex": rmPowerLevelsIfIndex,
       "rmPowerLevelsValIndex": rmPowerLevelsValIndex,
       "rmPowerLevelsPower": rmPowerLevelsPower,
       "rmFrequenciesTable": rmFrequenciesTable,
       "rmFrequenciesEntry": rmFrequenciesEntry,
       "rmFrequenciesIfIndex": rmFrequenciesIfIndex,
       "rmFrequenciesValIndex": rmFrequenciesValIndex,
       "rmFrequenciesFreq": rmFrequenciesFreq,
       "rmBitratesTable": rmBitratesTable,
       "rmBitratesEntry": rmBitratesEntry,
       "rmBitratesIfIndex": rmBitratesIfIndex,
       "rmBitratesValIndex": rmBitratesValIndex,
       "rmBitratesBitrate": rmBitratesBitrate,
       "radioStatTable": radioStatTable,
       "radioStatEntry": radioStatEntry,
       "radioStatMacAddress": radioStatMacAddress,
       "radioStatPackets": radioStatPackets,
       "radioStatRepeats": radioStatRepeats,
       "radioStatRepeatPackets": radioStatRepeatPackets,
       "radioStatBytes": radioStatBytes,
       "radioStatRepeatBytes": radioStatRepeatBytes,
       "radioStatErrors": radioStatErrors,
       "radioStatRecvPackets": radioStatRecvPackets,
       "radioStatRecvBytes": radioStatRecvBytes,
       "rmBandsTable": rmBandsTable,
       "rmBandsEntry": rmBandsEntry,
       "rmBandsIfIndex": rmBandsIfIndex,
       "rmBandsValIndex": rmBandsValIndex,
       "rmBandsBand": rmBandsBand,
       "aquaradioMIBNotificationsPrefix": aquaradioMIBNotificationsPrefix,
       "aquaradioMIBnotifications": aquaradioMIBnotifications,
       "radioFreqChanged": radioFreqChanged,
       "radioBandChanged": radioBandChanged,
       "aquaradioMIBConformance": aquaradioMIBConformance,
       "aquaradioMIBCompliances": aquaradioMIBCompliances,
       "aquaradioMIBCompliance": aquaradioMIBCompliance,
       "aquaradioMIBGroups": aquaradioMIBGroups,
       "radioGroup": radioGroup,
       "aquaradioNotifications": aquaradioNotifications}
)
