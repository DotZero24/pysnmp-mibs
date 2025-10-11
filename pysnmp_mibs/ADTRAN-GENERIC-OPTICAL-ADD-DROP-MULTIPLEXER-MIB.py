# SNMP MIB module (ADTRAN-GENERIC-OPTICAL-ADD-DROP-MULTIPLEXER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENERIC-OPTICAL-ADD-DROP-MULTIPLEXER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:03 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adGenOpticalADM,
 adGenOpticalADMID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenOpticalADM",
    "adGenOpticalADMID")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenOpticalADMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 43, 1)
)
if mibBuilder.loadTexts:
    adGenOpticalADMMIB.setRevisions(
        ("2012-07-26 00:00",
         "2012-06-12 00:00",
         "2012-05-18 00:00",
         "2012-04-11 00:00",
         "2012-03-19 00:00",
         "2012-01-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenOpticalADMConfiguration_ObjectIdentity = ObjectIdentity
adGenOpticalADMConfiguration = _AdGenOpticalADMConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 1)
)
_AdGenOpticalADMConfigurationTable_Object = MibTable
adGenOpticalADMConfigurationTable = _AdGenOpticalADMConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 1, 1)
)
if mibBuilder.loadTexts:
    adGenOpticalADMConfigurationTable.setStatus("current")
_AdGenOpticalADMConfigurationEntry_Object = MibTableRow
adGenOpticalADMConfigurationEntry = _AdGenOpticalADMConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 1, 1, 1)
)
adGenOpticalADMConfigurationEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenOpticalADMConfigurationEntry.setStatus("current")


class _AdGenOpticalADMGridSpacingSupported_Type(Bits):
    """Custom type adGenOpticalADMGridSpacingSupported based on Bits"""
    namedValues = NamedValues(
        *(("fiftyGHz", 0),
          ("oneHundredGHz", 1))
    )

_AdGenOpticalADMGridSpacingSupported_Type.__name__ = "Bits"
_AdGenOpticalADMGridSpacingSupported_Object = MibTableColumn
adGenOpticalADMGridSpacingSupported = _AdGenOpticalADMGridSpacingSupported_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 1, 1, 1, 1),
    _AdGenOpticalADMGridSpacingSupported_Type()
)
adGenOpticalADMGridSpacingSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMGridSpacingSupported.setStatus("current")


class _AdGenOpticalADMRemoveAllCrossConnect_Type(Integer32):
    """Custom type adGenOpticalADMRemoveAllCrossConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("removeAllCrossConnect", 1)
    )


_AdGenOpticalADMRemoveAllCrossConnect_Type.__name__ = "Integer32"
_AdGenOpticalADMRemoveAllCrossConnect_Object = MibTableColumn
adGenOpticalADMRemoveAllCrossConnect = _AdGenOpticalADMRemoveAllCrossConnect_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 1, 1, 1, 2),
    _AdGenOpticalADMRemoveAllCrossConnect_Type()
)
adGenOpticalADMRemoveAllCrossConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOpticalADMRemoveAllCrossConnect.setStatus("current")
_AdGenOpticalADMProvInterface_ObjectIdentity = ObjectIdentity
adGenOpticalADMProvInterface = _AdGenOpticalADMProvInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2)
)
_AdGenOpticalADMProvInterfaceTable_Object = MibTable
adGenOpticalADMProvInterfaceTable = _AdGenOpticalADMProvInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 1)
)
if mibBuilder.loadTexts:
    adGenOpticalADMProvInterfaceTable.setStatus("current")
_AdGenOpticalADMProvInterfaceEntry_Object = MibTableRow
adGenOpticalADMProvInterfaceEntry = _AdGenOpticalADMProvInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 1, 1)
)
adGenOpticalADMProvInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenOpticalADMProvInterfaceEntry.setStatus("current")


class _AdGenOpticalADMProvInterfaceDescription_Type(OctetString):
    """Custom type adGenOpticalADMProvInterfaceDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenOpticalADMProvInterfaceDescription_Type.__name__ = "OctetString"
_AdGenOpticalADMProvInterfaceDescription_Object = MibTableColumn
adGenOpticalADMProvInterfaceDescription = _AdGenOpticalADMProvInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 1, 1, 1),
    _AdGenOpticalADMProvInterfaceDescription_Type()
)
adGenOpticalADMProvInterfaceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOpticalADMProvInterfaceDescription.setStatus("current")
_AdGenOpticalADMProvChannelPowerLevel_Type = Integer32
_AdGenOpticalADMProvChannelPowerLevel_Object = MibTableColumn
adGenOpticalADMProvChannelPowerLevel = _AdGenOpticalADMProvChannelPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 1, 1, 2),
    _AdGenOpticalADMProvChannelPowerLevel_Type()
)
adGenOpticalADMProvChannelPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelPowerLevel.setUnits("Tenth of a dBm")


class _AdGenOpticalADMProvAutoPowerBalancing_Type(Integer32):
    """Custom type adGenOpticalADMProvAutoPowerBalancing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AdGenOpticalADMProvAutoPowerBalancing_Type.__name__ = "Integer32"
_AdGenOpticalADMProvAutoPowerBalancing_Object = MibTableColumn
adGenOpticalADMProvAutoPowerBalancing = _AdGenOpticalADMProvAutoPowerBalancing_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 1, 1, 3),
    _AdGenOpticalADMProvAutoPowerBalancing_Type()
)
adGenOpticalADMProvAutoPowerBalancing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOpticalADMProvAutoPowerBalancing.setStatus("current")
_AdGenOpticalADMProvOcmTotalPowerThresholdHigh_Type = Integer32
_AdGenOpticalADMProvOcmTotalPowerThresholdHigh_Object = MibTableColumn
adGenOpticalADMProvOcmTotalPowerThresholdHigh = _AdGenOpticalADMProvOcmTotalPowerThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 1, 1, 4),
    _AdGenOpticalADMProvOcmTotalPowerThresholdHigh_Type()
)
adGenOpticalADMProvOcmTotalPowerThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOpticalADMProvOcmTotalPowerThresholdHigh.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvOcmTotalPowerThresholdHigh.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvOcmTotalPowerThresholdLow_Type = Integer32
_AdGenOpticalADMProvOcmTotalPowerThresholdLow_Object = MibTableColumn
adGenOpticalADMProvOcmTotalPowerThresholdLow = _AdGenOpticalADMProvOcmTotalPowerThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 1, 1, 5),
    _AdGenOpticalADMProvOcmTotalPowerThresholdLow_Type()
)
adGenOpticalADMProvOcmTotalPowerThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOpticalADMProvOcmTotalPowerThresholdLow.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvOcmTotalPowerThresholdLow.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvTotalPowerThresholdHigh_Type = Integer32
_AdGenOpticalADMProvTotalPowerThresholdHigh_Object = MibTableColumn
adGenOpticalADMProvTotalPowerThresholdHigh = _AdGenOpticalADMProvTotalPowerThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 1, 1, 6),
    _AdGenOpticalADMProvTotalPowerThresholdHigh_Type()
)
adGenOpticalADMProvTotalPowerThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOpticalADMProvTotalPowerThresholdHigh.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvTotalPowerThresholdHigh.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvTotalPowerThresholdLow_Type = Integer32
_AdGenOpticalADMProvTotalPowerThresholdLow_Object = MibTableColumn
adGenOpticalADMProvTotalPowerThresholdLow = _AdGenOpticalADMProvTotalPowerThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 1, 1, 7),
    _AdGenOpticalADMProvTotalPowerThresholdLow_Type()
)
adGenOpticalADMProvTotalPowerThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOpticalADMProvTotalPowerThresholdLow.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvTotalPowerThresholdLow.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvInsertionLoss_Type = Integer32
_AdGenOpticalADMProvInsertionLoss_Object = MibTableColumn
adGenOpticalADMProvInsertionLoss = _AdGenOpticalADMProvInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 1, 1, 8),
    _AdGenOpticalADMProvInsertionLoss_Type()
)
adGenOpticalADMProvInsertionLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOpticalADMProvInsertionLoss.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvInsertionLoss.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvGain_Type = Integer32
_AdGenOpticalADMProvGain_Object = MibTableColumn
adGenOpticalADMProvGain = _AdGenOpticalADMProvGain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 1, 1, 9),
    _AdGenOpticalADMProvGain_Type()
)
adGenOpticalADMProvGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenOpticalADMProvGain.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvGain.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvInterfaceSupportTable_Object = MibTable
adGenOpticalADMProvInterfaceSupportTable = _AdGenOpticalADMProvInterfaceSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 2)
)
if mibBuilder.loadTexts:
    adGenOpticalADMProvInterfaceSupportTable.setStatus("current")
_AdGenOpticalADMProvInterfaceSupportEntry_Object = MibTableRow
adGenOpticalADMProvInterfaceSupportEntry = _AdGenOpticalADMProvInterfaceSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 2, 1)
)
adGenOpticalADMProvInterfaceSupportEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenOpticalADMProvInterfaceSupportEntry.setStatus("current")
_AdGenOpticalADMProvOcmTotalPowerThresholdHighMin_Type = Integer32
_AdGenOpticalADMProvOcmTotalPowerThresholdHighMin_Object = MibTableColumn
adGenOpticalADMProvOcmTotalPowerThresholdHighMin = _AdGenOpticalADMProvOcmTotalPowerThresholdHighMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 2, 1, 1),
    _AdGenOpticalADMProvOcmTotalPowerThresholdHighMin_Type()
)
adGenOpticalADMProvOcmTotalPowerThresholdHighMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvOcmTotalPowerThresholdHighMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvOcmTotalPowerThresholdHighMin.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvOcmTotalPowerThresholdHighMax_Type = Integer32
_AdGenOpticalADMProvOcmTotalPowerThresholdHighMax_Object = MibTableColumn
adGenOpticalADMProvOcmTotalPowerThresholdHighMax = _AdGenOpticalADMProvOcmTotalPowerThresholdHighMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 2, 1, 2),
    _AdGenOpticalADMProvOcmTotalPowerThresholdHighMax_Type()
)
adGenOpticalADMProvOcmTotalPowerThresholdHighMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvOcmTotalPowerThresholdHighMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvOcmTotalPowerThresholdHighMax.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvOcmTotalPowerThresholdLowMin_Type = Integer32
_AdGenOpticalADMProvOcmTotalPowerThresholdLowMin_Object = MibTableColumn
adGenOpticalADMProvOcmTotalPowerThresholdLowMin = _AdGenOpticalADMProvOcmTotalPowerThresholdLowMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 2, 1, 3),
    _AdGenOpticalADMProvOcmTotalPowerThresholdLowMin_Type()
)
adGenOpticalADMProvOcmTotalPowerThresholdLowMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvOcmTotalPowerThresholdLowMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvOcmTotalPowerThresholdLowMin.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvOcmTotalPowerThresholdLowMax_Type = Integer32
_AdGenOpticalADMProvOcmTotalPowerThresholdLowMax_Object = MibTableColumn
adGenOpticalADMProvOcmTotalPowerThresholdLowMax = _AdGenOpticalADMProvOcmTotalPowerThresholdLowMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 2, 1, 4),
    _AdGenOpticalADMProvOcmTotalPowerThresholdLowMax_Type()
)
adGenOpticalADMProvOcmTotalPowerThresholdLowMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvOcmTotalPowerThresholdLowMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvOcmTotalPowerThresholdLowMax.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvTotalPowerThresholdHighMin_Type = Integer32
_AdGenOpticalADMProvTotalPowerThresholdHighMin_Object = MibTableColumn
adGenOpticalADMProvTotalPowerThresholdHighMin = _AdGenOpticalADMProvTotalPowerThresholdHighMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 2, 1, 5),
    _AdGenOpticalADMProvTotalPowerThresholdHighMin_Type()
)
adGenOpticalADMProvTotalPowerThresholdHighMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvTotalPowerThresholdHighMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvTotalPowerThresholdHighMin.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvTotalPowerThresholdHighMax_Type = Integer32
_AdGenOpticalADMProvTotalPowerThresholdHighMax_Object = MibTableColumn
adGenOpticalADMProvTotalPowerThresholdHighMax = _AdGenOpticalADMProvTotalPowerThresholdHighMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 2, 1, 6),
    _AdGenOpticalADMProvTotalPowerThresholdHighMax_Type()
)
adGenOpticalADMProvTotalPowerThresholdHighMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvTotalPowerThresholdHighMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvTotalPowerThresholdHighMax.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvTotalPowerThresholdLowMin_Type = Integer32
_AdGenOpticalADMProvTotalPowerThresholdLowMin_Object = MibTableColumn
adGenOpticalADMProvTotalPowerThresholdLowMin = _AdGenOpticalADMProvTotalPowerThresholdLowMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 2, 1, 7),
    _AdGenOpticalADMProvTotalPowerThresholdLowMin_Type()
)
adGenOpticalADMProvTotalPowerThresholdLowMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvTotalPowerThresholdLowMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvTotalPowerThresholdLowMin.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvTotalPowerThresholdLowMax_Type = Integer32
_AdGenOpticalADMProvTotalPowerThresholdLowMax_Object = MibTableColumn
adGenOpticalADMProvTotalPowerThresholdLowMax = _AdGenOpticalADMProvTotalPowerThresholdLowMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 2, 2, 1, 8),
    _AdGenOpticalADMProvTotalPowerThresholdLowMax_Type()
)
adGenOpticalADMProvTotalPowerThresholdLowMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvTotalPowerThresholdLowMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvTotalPowerThresholdLowMax.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvChannel_ObjectIdentity = ObjectIdentity
adGenOpticalADMProvChannel = _AdGenOpticalADMProvChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3)
)
_AdGenOpticalADMProvChannelTable_Object = MibTable
adGenOpticalADMProvChannelTable = _AdGenOpticalADMProvChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 1)
)
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelTable.setStatus("current")
_AdGenOpticalADMProvChannelEntry_Object = MibTableRow
adGenOpticalADMProvChannelEntry = _AdGenOpticalADMProvChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 1, 1)
)
adGenOpticalADMProvChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENERIC-OPTICAL-ADD-DROP-MULTIPLEXER-MIB", "adGenOpticalADMProvChannelGridSpacing"),
)
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelEntry.setStatus("current")


class _AdGenOpticalADMProvChannelGridSpacing_Type(Integer32):
    """Custom type adGenOpticalADMProvChannelGridSpacing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("fiftyGHz", 50),
          ("oneHundredGHz", 100))
    )


_AdGenOpticalADMProvChannelGridSpacing_Type.__name__ = "Integer32"
_AdGenOpticalADMProvChannelGridSpacing_Object = MibTableColumn
adGenOpticalADMProvChannelGridSpacing = _AdGenOpticalADMProvChannelGridSpacing_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 1, 1, 1),
    _AdGenOpticalADMProvChannelGridSpacing_Type()
)
adGenOpticalADMProvChannelGridSpacing.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelGridSpacing.setStatus("current")
_AdGenOpticalADMProvChannelRowStatus_Type = RowStatus
_AdGenOpticalADMProvChannelRowStatus_Object = MibTableColumn
adGenOpticalADMProvChannelRowStatus = _AdGenOpticalADMProvChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 1, 1, 2),
    _AdGenOpticalADMProvChannelRowStatus_Type()
)
adGenOpticalADMProvChannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelRowStatus.setStatus("current")


class _AdGenOpticalADMProvChannelDescription_Type(OctetString):
    """Custom type adGenOpticalADMProvChannelDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenOpticalADMProvChannelDescription_Type.__name__ = "OctetString"
_AdGenOpticalADMProvChannelDescription_Object = MibTableColumn
adGenOpticalADMProvChannelDescription = _AdGenOpticalADMProvChannelDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 1, 1, 3),
    _AdGenOpticalADMProvChannelDescription_Type()
)
adGenOpticalADMProvChannelDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelDescription.setStatus("current")
_AdGenOpticalADMProvChannelNumber_Type = Integer32
_AdGenOpticalADMProvChannelNumber_Object = MibTableColumn
adGenOpticalADMProvChannelNumber = _AdGenOpticalADMProvChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 1, 1, 4),
    _AdGenOpticalADMProvChannelNumber_Type()
)
adGenOpticalADMProvChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelNumber.setStatus("current")
_AdGenOpticalADMProvChannelFrequency_Type = Integer32
_AdGenOpticalADMProvChannelFrequency_Object = MibTableColumn
adGenOpticalADMProvChannelFrequency = _AdGenOpticalADMProvChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 1, 1, 5),
    _AdGenOpticalADMProvChannelFrequency_Type()
)
adGenOpticalADMProvChannelFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelFrequency.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelFrequency.setUnits("Tera Hz")
_AdGenOpticalADMProvChannelWaveLength_Type = Integer32
_AdGenOpticalADMProvChannelWaveLength_Object = MibTableColumn
adGenOpticalADMProvChannelWaveLength = _AdGenOpticalADMProvChannelWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 1, 1, 6),
    _AdGenOpticalADMProvChannelWaveLength_Type()
)
adGenOpticalADMProvChannelWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelWaveLength.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelWaveLength.setUnits("Pico Meters")


class _AdGenOpticalADMProvChannelPowerOverride_Type(Integer32):
    """Custom type adGenOpticalADMProvChannelPowerOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("power", 2),
          ("attenuation", 3))
    )


_AdGenOpticalADMProvChannelPowerOverride_Type.__name__ = "Integer32"
_AdGenOpticalADMProvChannelPowerOverride_Object = MibTableColumn
adGenOpticalADMProvChannelPowerOverride = _AdGenOpticalADMProvChannelPowerOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 1, 1, 7),
    _AdGenOpticalADMProvChannelPowerOverride_Type()
)
adGenOpticalADMProvChannelPowerOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelPowerOverride.setStatus("current")
_AdGenOpticalADMProvChannelPower_Type = Integer32
_AdGenOpticalADMProvChannelPower_Object = MibTableColumn
adGenOpticalADMProvChannelPower = _AdGenOpticalADMProvChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 1, 1, 8),
    _AdGenOpticalADMProvChannelPower_Type()
)
adGenOpticalADMProvChannelPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelPower.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelPower.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvChannelAttenuation_Type = Integer32
_AdGenOpticalADMProvChannelAttenuation_Object = MibTableColumn
adGenOpticalADMProvChannelAttenuation = _AdGenOpticalADMProvChannelAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 1, 1, 9),
    _AdGenOpticalADMProvChannelAttenuation_Type()
)
adGenOpticalADMProvChannelAttenuation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelAttenuation.setUnits("Tenth of a dB")
_AdGenOpticalADMProvChannelOcmThresholdHigh_Type = Integer32
_AdGenOpticalADMProvChannelOcmThresholdHigh_Object = MibTableColumn
adGenOpticalADMProvChannelOcmThresholdHigh = _AdGenOpticalADMProvChannelOcmThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 1, 1, 10),
    _AdGenOpticalADMProvChannelOcmThresholdHigh_Type()
)
adGenOpticalADMProvChannelOcmThresholdHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelOcmThresholdHigh.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelOcmThresholdHigh.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvChannelOcmThresholdLow_Type = Integer32
_AdGenOpticalADMProvChannelOcmThresholdLow_Object = MibTableColumn
adGenOpticalADMProvChannelOcmThresholdLow = _AdGenOpticalADMProvChannelOcmThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 1, 1, 11),
    _AdGenOpticalADMProvChannelOcmThresholdLow_Type()
)
adGenOpticalADMProvChannelOcmThresholdLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelOcmThresholdLow.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelOcmThresholdLow.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvChannelCrossConnect_Type = OctetString
_AdGenOpticalADMProvChannelCrossConnect_Object = MibTableColumn
adGenOpticalADMProvChannelCrossConnect = _AdGenOpticalADMProvChannelCrossConnect_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 1, 1, 12),
    _AdGenOpticalADMProvChannelCrossConnect_Type()
)
adGenOpticalADMProvChannelCrossConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelCrossConnect.setStatus("current")


class _AdGenOpticalADMProvChannelOperStatus_Type(Integer32):
    """Custom type adGenOpticalADMProvChannelOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_AdGenOpticalADMProvChannelOperStatus_Type.__name__ = "Integer32"
_AdGenOpticalADMProvChannelOperStatus_Object = MibTableColumn
adGenOpticalADMProvChannelOperStatus = _AdGenOpticalADMProvChannelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 1, 1, 13),
    _AdGenOpticalADMProvChannelOperStatus_Type()
)
adGenOpticalADMProvChannelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelOperStatus.setStatus("current")


class _AdGenOpticalADMProvChannelAdminStatus_Type(Integer32):
    """Custom type adGenOpticalADMProvChannelAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_AdGenOpticalADMProvChannelAdminStatus_Type.__name__ = "Integer32"
_AdGenOpticalADMProvChannelAdminStatus_Object = MibTableColumn
adGenOpticalADMProvChannelAdminStatus = _AdGenOpticalADMProvChannelAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 1, 1, 14),
    _AdGenOpticalADMProvChannelAdminStatus_Type()
)
adGenOpticalADMProvChannelAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelAdminStatus.setStatus("current")
_AdGenOpticalADMProvChannelSupportTable_Object = MibTable
adGenOpticalADMProvChannelSupportTable = _AdGenOpticalADMProvChannelSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 2)
)
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelSupportTable.setStatus("current")
_AdGenOpticalADMProvChannelSupportEntry_Object = MibTableRow
adGenOpticalADMProvChannelSupportEntry = _AdGenOpticalADMProvChannelSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 2, 1)
)
adGenOpticalADMProvChannelSupportEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENERIC-OPTICAL-ADD-DROP-MULTIPLEXER-MIB", "adGenOpticalADMProvChannelGridSpacing"),
)
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelSupportEntry.setStatus("current")
_AdGenOpticalADMProvChannelPowerMin_Type = Integer32
_AdGenOpticalADMProvChannelPowerMin_Object = MibTableColumn
adGenOpticalADMProvChannelPowerMin = _AdGenOpticalADMProvChannelPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 2, 1, 1),
    _AdGenOpticalADMProvChannelPowerMin_Type()
)
adGenOpticalADMProvChannelPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelPowerMin.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvChannelPowerMax_Type = Integer32
_AdGenOpticalADMProvChannelPowerMax_Object = MibTableColumn
adGenOpticalADMProvChannelPowerMax = _AdGenOpticalADMProvChannelPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 2, 1, 2),
    _AdGenOpticalADMProvChannelPowerMax_Type()
)
adGenOpticalADMProvChannelPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelPowerMax.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvChannelAttenuationMin_Type = Integer32
_AdGenOpticalADMProvChannelAttenuationMin_Object = MibTableColumn
adGenOpticalADMProvChannelAttenuationMin = _AdGenOpticalADMProvChannelAttenuationMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 2, 1, 3),
    _AdGenOpticalADMProvChannelAttenuationMin_Type()
)
adGenOpticalADMProvChannelAttenuationMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelAttenuationMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelAttenuationMin.setUnits("Tenth of a dB")
_AdGenOpticalADMProvChannelAttenuationMax_Type = Integer32
_AdGenOpticalADMProvChannelAttenuationMax_Object = MibTableColumn
adGenOpticalADMProvChannelAttenuationMax = _AdGenOpticalADMProvChannelAttenuationMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 2, 1, 4),
    _AdGenOpticalADMProvChannelAttenuationMax_Type()
)
adGenOpticalADMProvChannelAttenuationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelAttenuationMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelAttenuationMax.setUnits("Tenth of a dB")
_AdGenOpticalADMProvChannelOcmThresholdHighMin_Type = Integer32
_AdGenOpticalADMProvChannelOcmThresholdHighMin_Object = MibTableColumn
adGenOpticalADMProvChannelOcmThresholdHighMin = _AdGenOpticalADMProvChannelOcmThresholdHighMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 2, 1, 5),
    _AdGenOpticalADMProvChannelOcmThresholdHighMin_Type()
)
adGenOpticalADMProvChannelOcmThresholdHighMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelOcmThresholdHighMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelOcmThresholdHighMin.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvChannelOcmThresholdHighMax_Type = Integer32
_AdGenOpticalADMProvChannelOcmThresholdHighMax_Object = MibTableColumn
adGenOpticalADMProvChannelOcmThresholdHighMax = _AdGenOpticalADMProvChannelOcmThresholdHighMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 2, 1, 6),
    _AdGenOpticalADMProvChannelOcmThresholdHighMax_Type()
)
adGenOpticalADMProvChannelOcmThresholdHighMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelOcmThresholdHighMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelOcmThresholdHighMax.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvChannelOcmThresholdLowMin_Type = Integer32
_AdGenOpticalADMProvChannelOcmThresholdLowMin_Object = MibTableColumn
adGenOpticalADMProvChannelOcmThresholdLowMin = _AdGenOpticalADMProvChannelOcmThresholdLowMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 2, 1, 7),
    _AdGenOpticalADMProvChannelOcmThresholdLowMin_Type()
)
adGenOpticalADMProvChannelOcmThresholdLowMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelOcmThresholdLowMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelOcmThresholdLowMin.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvChannelOcmThresholdLowMax_Type = Integer32
_AdGenOpticalADMProvChannelOcmThresholdLowMax_Object = MibTableColumn
adGenOpticalADMProvChannelOcmThresholdLowMax = _AdGenOpticalADMProvChannelOcmThresholdLowMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 2, 1, 8),
    _AdGenOpticalADMProvChannelOcmThresholdLowMax_Type()
)
adGenOpticalADMProvChannelOcmThresholdLowMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelOcmThresholdLowMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelOcmThresholdLowMax.setUnits("Tenth of a dBm")
_AdGenOpticalADMProvChannelWaveLengthMin_Type = Integer32
_AdGenOpticalADMProvChannelWaveLengthMin_Object = MibTableColumn
adGenOpticalADMProvChannelWaveLengthMin = _AdGenOpticalADMProvChannelWaveLengthMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 2, 1, 9),
    _AdGenOpticalADMProvChannelWaveLengthMin_Type()
)
adGenOpticalADMProvChannelWaveLengthMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelWaveLengthMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelWaveLengthMin.setUnits("PicoMeter")
_AdGenOpticalADMProvChannelWaveLengthMax_Type = Integer32
_AdGenOpticalADMProvChannelWaveLengthMax_Object = MibTableColumn
adGenOpticalADMProvChannelWaveLengthMax = _AdGenOpticalADMProvChannelWaveLengthMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 3, 2, 1, 10),
    _AdGenOpticalADMProvChannelWaveLengthMax_Type()
)
adGenOpticalADMProvChannelWaveLengthMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelWaveLengthMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelWaveLengthMax.setUnits("PicoMeter")
_AdGenOpticalADMCrossConnect_ObjectIdentity = ObjectIdentity
adGenOpticalADMCrossConnect = _AdGenOpticalADMCrossConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 4)
)
_AdGenOpticalADMCrossConnectTable_Object = MibTable
adGenOpticalADMCrossConnectTable = _AdGenOpticalADMCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 4, 1)
)
if mibBuilder.loadTexts:
    adGenOpticalADMCrossConnectTable.setStatus("current")
_AdGenOpticalADMCrossConnectEntry_Object = MibTableRow
adGenOpticalADMCrossConnectEntry = _AdGenOpticalADMCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 4, 1, 1)
)
adGenOpticalADMCrossConnectEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (1, "ADTRAN-GENERIC-OPTICAL-ADD-DROP-MULTIPLEXER-MIB", "adGenOpticalADMCrossConnectName"),
)
if mibBuilder.loadTexts:
    adGenOpticalADMCrossConnectEntry.setStatus("current")


class _AdGenOpticalADMCrossConnectName_Type(DisplayString):
    """Custom type adGenOpticalADMCrossConnectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenOpticalADMCrossConnectName_Type.__name__ = "DisplayString"
_AdGenOpticalADMCrossConnectName_Object = MibTableColumn
adGenOpticalADMCrossConnectName = _AdGenOpticalADMCrossConnectName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 4, 1, 1, 1),
    _AdGenOpticalADMCrossConnectName_Type()
)
adGenOpticalADMCrossConnectName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenOpticalADMCrossConnectName.setStatus("current")
_AdGenOpticalADMCrossConnectRowStatus_Type = RowStatus
_AdGenOpticalADMCrossConnectRowStatus_Object = MibTableColumn
adGenOpticalADMCrossConnectRowStatus = _AdGenOpticalADMCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 4, 1, 1, 2),
    _AdGenOpticalADMCrossConnectRowStatus_Type()
)
adGenOpticalADMCrossConnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOpticalADMCrossConnectRowStatus.setStatus("current")
_AdGenOpticalADMCrossConnectSrcChannelIfIndex_Type = InterfaceIndex
_AdGenOpticalADMCrossConnectSrcChannelIfIndex_Object = MibTableColumn
adGenOpticalADMCrossConnectSrcChannelIfIndex = _AdGenOpticalADMCrossConnectSrcChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 4, 1, 1, 3),
    _AdGenOpticalADMCrossConnectSrcChannelIfIndex_Type()
)
adGenOpticalADMCrossConnectSrcChannelIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOpticalADMCrossConnectSrcChannelIfIndex.setStatus("current")


class _AdGenOpticalADMCrossConnectSrcChannelGridSpacing_Type(Integer32):
    """Custom type adGenOpticalADMCrossConnectSrcChannelGridSpacing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("fiftyGHz", 50),
          ("oneHundredGHz", 100))
    )


_AdGenOpticalADMCrossConnectSrcChannelGridSpacing_Type.__name__ = "Integer32"
_AdGenOpticalADMCrossConnectSrcChannelGridSpacing_Object = MibTableColumn
adGenOpticalADMCrossConnectSrcChannelGridSpacing = _AdGenOpticalADMCrossConnectSrcChannelGridSpacing_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 4, 1, 1, 4),
    _AdGenOpticalADMCrossConnectSrcChannelGridSpacing_Type()
)
adGenOpticalADMCrossConnectSrcChannelGridSpacing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOpticalADMCrossConnectSrcChannelGridSpacing.setStatus("current")
_AdGenOpticalADMCrossConnectDstInterfaceIfIndex_Type = InterfaceIndex
_AdGenOpticalADMCrossConnectDstInterfaceIfIndex_Object = MibTableColumn
adGenOpticalADMCrossConnectDstInterfaceIfIndex = _AdGenOpticalADMCrossConnectDstInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 4, 1, 1, 5),
    _AdGenOpticalADMCrossConnectDstInterfaceIfIndex_Type()
)
adGenOpticalADMCrossConnectDstInterfaceIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOpticalADMCrossConnectDstInterfaceIfIndex.setStatus("current")


class _AdGenOpticalADMCrossConnectOperationStatus_Type(Integer32):
    """Custom type adGenOpticalADMCrossConnectOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_AdGenOpticalADMCrossConnectOperationStatus_Type.__name__ = "Integer32"
_AdGenOpticalADMCrossConnectOperationStatus_Object = MibTableColumn
adGenOpticalADMCrossConnectOperationStatus = _AdGenOpticalADMCrossConnectOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 4, 1, 1, 6),
    _AdGenOpticalADMCrossConnectOperationStatus_Type()
)
adGenOpticalADMCrossConnectOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMCrossConnectOperationStatus.setStatus("current")
_AdGenOpticalADMCrossConnectError_Type = DisplayString
_AdGenOpticalADMCrossConnectError_Object = MibTableColumn
adGenOpticalADMCrossConnectError = _AdGenOpticalADMCrossConnectError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 4, 1, 1, 7),
    _AdGenOpticalADMCrossConnectError_Type()
)
adGenOpticalADMCrossConnectError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMCrossConnectError.setStatus("current")


class _AdGenOpticalADMCrossConnectAdminStatus_Type(Integer32):
    """Custom type adGenOpticalADMCrossConnectAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_AdGenOpticalADMCrossConnectAdminStatus_Type.__name__ = "Integer32"
_AdGenOpticalADMCrossConnectAdminStatus_Object = MibTableColumn
adGenOpticalADMCrossConnectAdminStatus = _AdGenOpticalADMCrossConnectAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 4, 1, 1, 8),
    _AdGenOpticalADMCrossConnectAdminStatus_Type()
)
adGenOpticalADMCrossConnectAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenOpticalADMCrossConnectAdminStatus.setStatus("current")
_AdGenOpticalADMProvError_ObjectIdentity = ObjectIdentity
adGenOpticalADMProvError = _AdGenOpticalADMProvError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 5)
)
_AdGenOpticalADMProvErrorTable_Object = MibTable
adGenOpticalADMProvErrorTable = _AdGenOpticalADMProvErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 5, 1)
)
if mibBuilder.loadTexts:
    adGenOpticalADMProvErrorTable.setStatus("current")
_AdGenOpticalADMProvErrorEntry_Object = MibTableRow
adGenOpticalADMProvErrorEntry = _AdGenOpticalADMProvErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 5, 1, 1)
)
adGenOpticalADMProvErrorEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenOpticalADMProvErrorEntry.setStatus("current")
_AdGenOpticalADMProvChannelError_Type = DisplayString
_AdGenOpticalADMProvChannelError_Object = MibTableColumn
adGenOpticalADMProvChannelError = _AdGenOpticalADMProvChannelError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 5, 1, 1, 1),
    _AdGenOpticalADMProvChannelError_Type()
)
adGenOpticalADMProvChannelError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvChannelError.setStatus("current")
_AdGenOpticalADMProvCrossConnectError_Type = DisplayString
_AdGenOpticalADMProvCrossConnectError_Object = MibTableColumn
adGenOpticalADMProvCrossConnectError = _AdGenOpticalADMProvCrossConnectError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 5, 1, 1, 2),
    _AdGenOpticalADMProvCrossConnectError_Type()
)
adGenOpticalADMProvCrossConnectError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMProvCrossConnectError.setStatus("current")
_AdGenOpticalADMStatus_ObjectIdentity = ObjectIdentity
adGenOpticalADMStatus = _AdGenOpticalADMStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 6)
)
_AdGenOpticalADMInterfaceStatusTable_Object = MibTable
adGenOpticalADMInterfaceStatusTable = _AdGenOpticalADMInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 6, 1)
)
if mibBuilder.loadTexts:
    adGenOpticalADMInterfaceStatusTable.setStatus("current")
_AdGenOpticalADMInterfaceStatusEntry_Object = MibTableRow
adGenOpticalADMInterfaceStatusEntry = _AdGenOpticalADMInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 6, 1, 1)
)
adGenOpticalADMInterfaceStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenOpticalADMInterfaceStatusEntry.setStatus("current")
_AdGenOpticalADMInterfaceStatOcmTotalPower_Type = Integer32
_AdGenOpticalADMInterfaceStatOcmTotalPower_Object = MibTableColumn
adGenOpticalADMInterfaceStatOcmTotalPower = _AdGenOpticalADMInterfaceStatOcmTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 6, 1, 1, 1),
    _AdGenOpticalADMInterfaceStatOcmTotalPower_Type()
)
adGenOpticalADMInterfaceStatOcmTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMInterfaceStatOcmTotalPower.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMInterfaceStatOcmTotalPower.setUnits("Tenth of a dBm")
_AdGenOpticalADMInterfaceStatTotalPower_Type = Integer32
_AdGenOpticalADMInterfaceStatTotalPower_Object = MibTableColumn
adGenOpticalADMInterfaceStatTotalPower = _AdGenOpticalADMInterfaceStatTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 6, 1, 1, 2),
    _AdGenOpticalADMInterfaceStatTotalPower_Type()
)
adGenOpticalADMInterfaceStatTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMInterfaceStatTotalPower.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMInterfaceStatTotalPower.setUnits("Tenth of a dBm")
_AdGenOpticalADMInterfaceStatActualGain_Type = Integer32
_AdGenOpticalADMInterfaceStatActualGain_Object = MibTableColumn
adGenOpticalADMInterfaceStatActualGain = _AdGenOpticalADMInterfaceStatActualGain_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 6, 1, 1, 3),
    _AdGenOpticalADMInterfaceStatActualGain_Type()
)
adGenOpticalADMInterfaceStatActualGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMInterfaceStatActualGain.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMInterfaceStatActualGain.setUnits("Tenth of a dBm")
_AdGenOpticalADMInterfaceStatInputPower_Type = Integer32
_AdGenOpticalADMInterfaceStatInputPower_Object = MibTableColumn
adGenOpticalADMInterfaceStatInputPower = _AdGenOpticalADMInterfaceStatInputPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 6, 1, 1, 4),
    _AdGenOpticalADMInterfaceStatInputPower_Type()
)
adGenOpticalADMInterfaceStatInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMInterfaceStatInputPower.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMInterfaceStatInputPower.setUnits("Tenth of a dBm")
_AdGenOpticalADMChannelStatusTable_Object = MibTable
adGenOpticalADMChannelStatusTable = _AdGenOpticalADMChannelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 6, 2)
)
if mibBuilder.loadTexts:
    adGenOpticalADMChannelStatusTable.setStatus("current")
_AdGenOpticalADMChannelStatusEntry_Object = MibTableRow
adGenOpticalADMChannelStatusEntry = _AdGenOpticalADMChannelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 6, 2, 1)
)
adGenOpticalADMChannelStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENERIC-OPTICAL-ADD-DROP-MULTIPLEXER-MIB", "adGenOpticalADMProvChannelGridSpacing"),
)
if mibBuilder.loadTexts:
    adGenOpticalADMChannelStatusEntry.setStatus("current")
_AdGenOpticalADMChannelStatOcmChannelPower_Type = Integer32
_AdGenOpticalADMChannelStatOcmChannelPower_Object = MibTableColumn
adGenOpticalADMChannelStatOcmChannelPower = _AdGenOpticalADMChannelStatOcmChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 6, 2, 1, 1),
    _AdGenOpticalADMChannelStatOcmChannelPower_Type()
)
adGenOpticalADMChannelStatOcmChannelPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMChannelStatOcmChannelPower.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMChannelStatOcmChannelPower.setUnits("Tenth of a dBm")
_AdGenOpticalADMChannelStatAttenuation_Type = Integer32
_AdGenOpticalADMChannelStatAttenuation_Object = MibTableColumn
adGenOpticalADMChannelStatAttenuation = _AdGenOpticalADMChannelStatAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 6, 2, 1, 2),
    _AdGenOpticalADMChannelStatAttenuation_Type()
)
adGenOpticalADMChannelStatAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenOpticalADMChannelStatAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    adGenOpticalADMChannelStatAttenuation.setUnits("Tenth of a dB")
_AdGenOpticalADMAlarm_ObjectIdentity = ObjectIdentity
adGenOpticalADMAlarm = _AdGenOpticalADMAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100)
)
_AdGenOpticalADMEvents_ObjectIdentity = ObjectIdentity
adGenOpticalADMEvents = _AdGenOpticalADMEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0)
)

# Managed Objects groups


# Notification objects

adGenOpticalADMAlmComInLOSActiveClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 1)
)
adGenOpticalADMAlmComInLOSActiveClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmComInLOSActiveClear.setStatus(
        "current"
    )

adGenOpticalADMAlmComInLOSActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 2)
)
adGenOpticalADMAlmComInLOSActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmComInLOSActive.setStatus(
        "current"
    )

adGenOpticalADMAlmComInTotalPwrTHHiActiveClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 3)
)
adGenOpticalADMAlmComInTotalPwrTHHiActiveClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmComInTotalPwrTHHiActiveClear.setStatus(
        "current"
    )

adGenOpticalADMAlmComInTotalPwrTHHiActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 4)
)
adGenOpticalADMAlmComInTotalPwrTHHiActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmComInTotalPwrTHHiActive.setStatus(
        "current"
    )

adGenOpticalADMAlmComInTotalPwrTHLowActiveClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 5)
)
adGenOpticalADMAlmComInTotalPwrTHLowActiveClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmComInTotalPwrTHLowActiveClear.setStatus(
        "current"
    )

adGenOpticalADMAlmComInTotalPwrTHLowActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 6)
)
adGenOpticalADMAlmComInTotalPwrTHLowActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmComInTotalPwrTHLowActive.setStatus(
        "current"
    )

adGenOpticalADMAlmComInOcmTotalPwrTHHiActiveClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 7)
)
adGenOpticalADMAlmComInOcmTotalPwrTHHiActiveClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmComInOcmTotalPwrTHHiActiveClear.setStatus(
        "current"
    )

adGenOpticalADMAlmComInOcmTotalPwrTHHiActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 8)
)
adGenOpticalADMAlmComInOcmTotalPwrTHHiActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmComInOcmTotalPwrTHHiActive.setStatus(
        "current"
    )

adGenOpticalADMAlmComInOcmTotalPwrTHLowActiveClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 9)
)
adGenOpticalADMAlmComInOcmTotalPwrTHLowActiveClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmComInOcmTotalPwrTHLowActiveClear.setStatus(
        "current"
    )

adGenOpticalADMAlmComInOcmTotalPwrTHLowActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 10)
)
adGenOpticalADMAlmComInOcmTotalPwrTHLowActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmComInOcmTotalPwrTHLowActive.setStatus(
        "current"
    )

adGenOpticalADMAlmComOutOcmTotalPwrTHHiActiveClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 11)
)
adGenOpticalADMAlmComOutOcmTotalPwrTHHiActiveClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmComOutOcmTotalPwrTHHiActiveClear.setStatus(
        "current"
    )

adGenOpticalADMAlmComOutOcmTotalPwrTHHiActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 12)
)
adGenOpticalADMAlmComOutOcmTotalPwrTHHiActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmComOutOcmTotalPwrTHHiActive.setStatus(
        "current"
    )

adGenOpticalADMAlmComOutOcmTotalPwrTHLowActiveClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 13)
)
adGenOpticalADMAlmComOutOcmTotalPwrTHLowActiveClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmComOutOcmTotalPwrTHLowActiveClear.setStatus(
        "current"
    )

adGenOpticalADMAlmComOutOcmTotalPwrTHLowActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 14)
)
adGenOpticalADMAlmComOutOcmTotalPwrTHLowActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmComOutOcmTotalPwrTHLowActive.setStatus(
        "current"
    )

adGenOpticalADMAlmChannelComInOcmPwrTHHiActiveClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 15)
)
adGenOpticalADMAlmChannelComInOcmPwrTHHiActiveClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmChannelComInOcmPwrTHHiActiveClear.setStatus(
        "current"
    )

adGenOpticalADMAlmChannelComInOcmPwrTHHiActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 16)
)
adGenOpticalADMAlmChannelComInOcmPwrTHHiActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmChannelComInOcmPwrTHHiActive.setStatus(
        "current"
    )

adGenOpticalADMAlmChannelComInOcmPwrTHLowActiveClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 17)
)
adGenOpticalADMAlmChannelComInOcmPwrTHLowActiveClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmChannelComInOcmPwrTHLowActiveClear.setStatus(
        "current"
    )

adGenOpticalADMAlmChannelComInOcmPwrTHLowActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 18)
)
adGenOpticalADMAlmChannelComInOcmPwrTHLowActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmChannelComInOcmPwrTHLowActive.setStatus(
        "current"
    )

adGenOpticalADMAlmChannelComOutOcmPwrTHHiActiveClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 19)
)
adGenOpticalADMAlmChannelComOutOcmPwrTHHiActiveClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmChannelComOutOcmPwrTHHiActiveClear.setStatus(
        "current"
    )

adGenOpticalADMAlmChannelComOutOcmPwrTHHiActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 20)
)
adGenOpticalADMAlmChannelComOutOcmPwrTHHiActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmChannelComOutOcmPwrTHHiActive.setStatus(
        "current"
    )

adGenOpticalADMAlmChannelComOutOcmPwrTHLowActiveClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 21)
)
adGenOpticalADMAlmChannelComOutOcmPwrTHLowActiveClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmChannelComOutOcmPwrTHLowActiveClear.setStatus(
        "current"
    )

adGenOpticalADMAlmChannelComOutOcmPwrTHLowActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 22)
)
adGenOpticalADMAlmChannelComOutOcmPwrTHLowActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmChannelComOutOcmPwrTHLowActive.setStatus(
        "current"
    )

adGenOpticalADMAlmChannelComOutAutoOORHiActiveClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 23)
)
adGenOpticalADMAlmChannelComOutAutoOORHiActiveClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmChannelComOutAutoOORHiActiveClear.setStatus(
        "current"
    )

adGenOpticalADMAlmChannelComOutAutoOORHiActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 24)
)
adGenOpticalADMAlmChannelComOutAutoOORHiActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmChannelComOutAutoOORHiActive.setStatus(
        "current"
    )

adGenOpticalADMAlmChannelComOutAutoOORLowActiveClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 25)
)
adGenOpticalADMAlmChannelComOutAutoOORLowActiveClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmChannelComOutAutoOORLowActiveClear.setStatus(
        "current"
    )

adGenOpticalADMAlmChannelComOutAutoOORLowActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 26)
)
adGenOpticalADMAlmChannelComOutAutoOORLowActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmChannelComOutAutoOORLowActive.setStatus(
        "current"
    )

adGenOpticalADMAlmLossOfMidStageInActiveClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 27)
)
adGenOpticalADMAlmLossOfMidStageInActiveClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmLossOfMidStageInActiveClear.setStatus(
        "current"
    )

adGenOpticalADMAlmLossOfMidStageInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 28)
)
adGenOpticalADMAlmLossOfMidStageInActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmLossOfMidStageInActive.setStatus(
        "current"
    )

adGenOpticalADMAlmComOutAmpShutOffClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 29)
)
adGenOpticalADMAlmComOutAmpShutOffClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmComOutAmpShutOffClear.setStatus(
        "current"
    )

adGenOpticalADMAlmComOutAmpShutOffActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 43, 100, 0, 30)
)
adGenOpticalADMAlmComOutAmpShutOffActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenOpticalADMAlmComOutAmpShutOffActive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENERIC-OPTICAL-ADD-DROP-MULTIPLEXER-MIB",
    **{"adGenOpticalADMConfiguration": adGenOpticalADMConfiguration,
       "adGenOpticalADMConfigurationTable": adGenOpticalADMConfigurationTable,
       "adGenOpticalADMConfigurationEntry": adGenOpticalADMConfigurationEntry,
       "adGenOpticalADMGridSpacingSupported": adGenOpticalADMGridSpacingSupported,
       "adGenOpticalADMRemoveAllCrossConnect": adGenOpticalADMRemoveAllCrossConnect,
       "adGenOpticalADMProvInterface": adGenOpticalADMProvInterface,
       "adGenOpticalADMProvInterfaceTable": adGenOpticalADMProvInterfaceTable,
       "adGenOpticalADMProvInterfaceEntry": adGenOpticalADMProvInterfaceEntry,
       "adGenOpticalADMProvInterfaceDescription": adGenOpticalADMProvInterfaceDescription,
       "adGenOpticalADMProvChannelPowerLevel": adGenOpticalADMProvChannelPowerLevel,
       "adGenOpticalADMProvAutoPowerBalancing": adGenOpticalADMProvAutoPowerBalancing,
       "adGenOpticalADMProvOcmTotalPowerThresholdHigh": adGenOpticalADMProvOcmTotalPowerThresholdHigh,
       "adGenOpticalADMProvOcmTotalPowerThresholdLow": adGenOpticalADMProvOcmTotalPowerThresholdLow,
       "adGenOpticalADMProvTotalPowerThresholdHigh": adGenOpticalADMProvTotalPowerThresholdHigh,
       "adGenOpticalADMProvTotalPowerThresholdLow": adGenOpticalADMProvTotalPowerThresholdLow,
       "adGenOpticalADMProvInsertionLoss": adGenOpticalADMProvInsertionLoss,
       "adGenOpticalADMProvGain": adGenOpticalADMProvGain,
       "adGenOpticalADMProvInterfaceSupportTable": adGenOpticalADMProvInterfaceSupportTable,
       "adGenOpticalADMProvInterfaceSupportEntry": adGenOpticalADMProvInterfaceSupportEntry,
       "adGenOpticalADMProvOcmTotalPowerThresholdHighMin": adGenOpticalADMProvOcmTotalPowerThresholdHighMin,
       "adGenOpticalADMProvOcmTotalPowerThresholdHighMax": adGenOpticalADMProvOcmTotalPowerThresholdHighMax,
       "adGenOpticalADMProvOcmTotalPowerThresholdLowMin": adGenOpticalADMProvOcmTotalPowerThresholdLowMin,
       "adGenOpticalADMProvOcmTotalPowerThresholdLowMax": adGenOpticalADMProvOcmTotalPowerThresholdLowMax,
       "adGenOpticalADMProvTotalPowerThresholdHighMin": adGenOpticalADMProvTotalPowerThresholdHighMin,
       "adGenOpticalADMProvTotalPowerThresholdHighMax": adGenOpticalADMProvTotalPowerThresholdHighMax,
       "adGenOpticalADMProvTotalPowerThresholdLowMin": adGenOpticalADMProvTotalPowerThresholdLowMin,
       "adGenOpticalADMProvTotalPowerThresholdLowMax": adGenOpticalADMProvTotalPowerThresholdLowMax,
       "adGenOpticalADMProvChannel": adGenOpticalADMProvChannel,
       "adGenOpticalADMProvChannelTable": adGenOpticalADMProvChannelTable,
       "adGenOpticalADMProvChannelEntry": adGenOpticalADMProvChannelEntry,
       "adGenOpticalADMProvChannelGridSpacing": adGenOpticalADMProvChannelGridSpacing,
       "adGenOpticalADMProvChannelRowStatus": adGenOpticalADMProvChannelRowStatus,
       "adGenOpticalADMProvChannelDescription": adGenOpticalADMProvChannelDescription,
       "adGenOpticalADMProvChannelNumber": adGenOpticalADMProvChannelNumber,
       "adGenOpticalADMProvChannelFrequency": adGenOpticalADMProvChannelFrequency,
       "adGenOpticalADMProvChannelWaveLength": adGenOpticalADMProvChannelWaveLength,
       "adGenOpticalADMProvChannelPowerOverride": adGenOpticalADMProvChannelPowerOverride,
       "adGenOpticalADMProvChannelPower": adGenOpticalADMProvChannelPower,
       "adGenOpticalADMProvChannelAttenuation": adGenOpticalADMProvChannelAttenuation,
       "adGenOpticalADMProvChannelOcmThresholdHigh": adGenOpticalADMProvChannelOcmThresholdHigh,
       "adGenOpticalADMProvChannelOcmThresholdLow": adGenOpticalADMProvChannelOcmThresholdLow,
       "adGenOpticalADMProvChannelCrossConnect": adGenOpticalADMProvChannelCrossConnect,
       "adGenOpticalADMProvChannelOperStatus": adGenOpticalADMProvChannelOperStatus,
       "adGenOpticalADMProvChannelAdminStatus": adGenOpticalADMProvChannelAdminStatus,
       "adGenOpticalADMProvChannelSupportTable": adGenOpticalADMProvChannelSupportTable,
       "adGenOpticalADMProvChannelSupportEntry": adGenOpticalADMProvChannelSupportEntry,
       "adGenOpticalADMProvChannelPowerMin": adGenOpticalADMProvChannelPowerMin,
       "adGenOpticalADMProvChannelPowerMax": adGenOpticalADMProvChannelPowerMax,
       "adGenOpticalADMProvChannelAttenuationMin": adGenOpticalADMProvChannelAttenuationMin,
       "adGenOpticalADMProvChannelAttenuationMax": adGenOpticalADMProvChannelAttenuationMax,
       "adGenOpticalADMProvChannelOcmThresholdHighMin": adGenOpticalADMProvChannelOcmThresholdHighMin,
       "adGenOpticalADMProvChannelOcmThresholdHighMax": adGenOpticalADMProvChannelOcmThresholdHighMax,
       "adGenOpticalADMProvChannelOcmThresholdLowMin": adGenOpticalADMProvChannelOcmThresholdLowMin,
       "adGenOpticalADMProvChannelOcmThresholdLowMax": adGenOpticalADMProvChannelOcmThresholdLowMax,
       "adGenOpticalADMProvChannelWaveLengthMin": adGenOpticalADMProvChannelWaveLengthMin,
       "adGenOpticalADMProvChannelWaveLengthMax": adGenOpticalADMProvChannelWaveLengthMax,
       "adGenOpticalADMCrossConnect": adGenOpticalADMCrossConnect,
       "adGenOpticalADMCrossConnectTable": adGenOpticalADMCrossConnectTable,
       "adGenOpticalADMCrossConnectEntry": adGenOpticalADMCrossConnectEntry,
       "adGenOpticalADMCrossConnectName": adGenOpticalADMCrossConnectName,
       "adGenOpticalADMCrossConnectRowStatus": adGenOpticalADMCrossConnectRowStatus,
       "adGenOpticalADMCrossConnectSrcChannelIfIndex": adGenOpticalADMCrossConnectSrcChannelIfIndex,
       "adGenOpticalADMCrossConnectSrcChannelGridSpacing": adGenOpticalADMCrossConnectSrcChannelGridSpacing,
       "adGenOpticalADMCrossConnectDstInterfaceIfIndex": adGenOpticalADMCrossConnectDstInterfaceIfIndex,
       "adGenOpticalADMCrossConnectOperationStatus": adGenOpticalADMCrossConnectOperationStatus,
       "adGenOpticalADMCrossConnectError": adGenOpticalADMCrossConnectError,
       "adGenOpticalADMCrossConnectAdminStatus": adGenOpticalADMCrossConnectAdminStatus,
       "adGenOpticalADMProvError": adGenOpticalADMProvError,
       "adGenOpticalADMProvErrorTable": adGenOpticalADMProvErrorTable,
       "adGenOpticalADMProvErrorEntry": adGenOpticalADMProvErrorEntry,
       "adGenOpticalADMProvChannelError": adGenOpticalADMProvChannelError,
       "adGenOpticalADMProvCrossConnectError": adGenOpticalADMProvCrossConnectError,
       "adGenOpticalADMStatus": adGenOpticalADMStatus,
       "adGenOpticalADMInterfaceStatusTable": adGenOpticalADMInterfaceStatusTable,
       "adGenOpticalADMInterfaceStatusEntry": adGenOpticalADMInterfaceStatusEntry,
       "adGenOpticalADMInterfaceStatOcmTotalPower": adGenOpticalADMInterfaceStatOcmTotalPower,
       "adGenOpticalADMInterfaceStatTotalPower": adGenOpticalADMInterfaceStatTotalPower,
       "adGenOpticalADMInterfaceStatActualGain": adGenOpticalADMInterfaceStatActualGain,
       "adGenOpticalADMInterfaceStatInputPower": adGenOpticalADMInterfaceStatInputPower,
       "adGenOpticalADMChannelStatusTable": adGenOpticalADMChannelStatusTable,
       "adGenOpticalADMChannelStatusEntry": adGenOpticalADMChannelStatusEntry,
       "adGenOpticalADMChannelStatOcmChannelPower": adGenOpticalADMChannelStatOcmChannelPower,
       "adGenOpticalADMChannelStatAttenuation": adGenOpticalADMChannelStatAttenuation,
       "adGenOpticalADMAlarm": adGenOpticalADMAlarm,
       "adGenOpticalADMEvents": adGenOpticalADMEvents,
       "adGenOpticalADMAlmComInLOSActiveClear": adGenOpticalADMAlmComInLOSActiveClear,
       "adGenOpticalADMAlmComInLOSActive": adGenOpticalADMAlmComInLOSActive,
       "adGenOpticalADMAlmComInTotalPwrTHHiActiveClear": adGenOpticalADMAlmComInTotalPwrTHHiActiveClear,
       "adGenOpticalADMAlmComInTotalPwrTHHiActive": adGenOpticalADMAlmComInTotalPwrTHHiActive,
       "adGenOpticalADMAlmComInTotalPwrTHLowActiveClear": adGenOpticalADMAlmComInTotalPwrTHLowActiveClear,
       "adGenOpticalADMAlmComInTotalPwrTHLowActive": adGenOpticalADMAlmComInTotalPwrTHLowActive,
       "adGenOpticalADMAlmComInOcmTotalPwrTHHiActiveClear": adGenOpticalADMAlmComInOcmTotalPwrTHHiActiveClear,
       "adGenOpticalADMAlmComInOcmTotalPwrTHHiActive": adGenOpticalADMAlmComInOcmTotalPwrTHHiActive,
       "adGenOpticalADMAlmComInOcmTotalPwrTHLowActiveClear": adGenOpticalADMAlmComInOcmTotalPwrTHLowActiveClear,
       "adGenOpticalADMAlmComInOcmTotalPwrTHLowActive": adGenOpticalADMAlmComInOcmTotalPwrTHLowActive,
       "adGenOpticalADMAlmComOutOcmTotalPwrTHHiActiveClear": adGenOpticalADMAlmComOutOcmTotalPwrTHHiActiveClear,
       "adGenOpticalADMAlmComOutOcmTotalPwrTHHiActive": adGenOpticalADMAlmComOutOcmTotalPwrTHHiActive,
       "adGenOpticalADMAlmComOutOcmTotalPwrTHLowActiveClear": adGenOpticalADMAlmComOutOcmTotalPwrTHLowActiveClear,
       "adGenOpticalADMAlmComOutOcmTotalPwrTHLowActive": adGenOpticalADMAlmComOutOcmTotalPwrTHLowActive,
       "adGenOpticalADMAlmChannelComInOcmPwrTHHiActiveClear": adGenOpticalADMAlmChannelComInOcmPwrTHHiActiveClear,
       "adGenOpticalADMAlmChannelComInOcmPwrTHHiActive": adGenOpticalADMAlmChannelComInOcmPwrTHHiActive,
       "adGenOpticalADMAlmChannelComInOcmPwrTHLowActiveClear": adGenOpticalADMAlmChannelComInOcmPwrTHLowActiveClear,
       "adGenOpticalADMAlmChannelComInOcmPwrTHLowActive": adGenOpticalADMAlmChannelComInOcmPwrTHLowActive,
       "adGenOpticalADMAlmChannelComOutOcmPwrTHHiActiveClear": adGenOpticalADMAlmChannelComOutOcmPwrTHHiActiveClear,
       "adGenOpticalADMAlmChannelComOutOcmPwrTHHiActive": adGenOpticalADMAlmChannelComOutOcmPwrTHHiActive,
       "adGenOpticalADMAlmChannelComOutOcmPwrTHLowActiveClear": adGenOpticalADMAlmChannelComOutOcmPwrTHLowActiveClear,
       "adGenOpticalADMAlmChannelComOutOcmPwrTHLowActive": adGenOpticalADMAlmChannelComOutOcmPwrTHLowActive,
       "adGenOpticalADMAlmChannelComOutAutoOORHiActiveClear": adGenOpticalADMAlmChannelComOutAutoOORHiActiveClear,
       "adGenOpticalADMAlmChannelComOutAutoOORHiActive": adGenOpticalADMAlmChannelComOutAutoOORHiActive,
       "adGenOpticalADMAlmChannelComOutAutoOORLowActiveClear": adGenOpticalADMAlmChannelComOutAutoOORLowActiveClear,
       "adGenOpticalADMAlmChannelComOutAutoOORLowActive": adGenOpticalADMAlmChannelComOutAutoOORLowActive,
       "adGenOpticalADMAlmLossOfMidStageInActiveClear": adGenOpticalADMAlmLossOfMidStageInActiveClear,
       "adGenOpticalADMAlmLossOfMidStageInActive": adGenOpticalADMAlmLossOfMidStageInActive,
       "adGenOpticalADMAlmComOutAmpShutOffClear": adGenOpticalADMAlmComOutAmpShutOffClear,
       "adGenOpticalADMAlmComOutAmpShutOffActive": adGenOpticalADMAlmComOutAmpShutOffActive,
       "adGenOpticalADMMIB": adGenOpticalADMMIB}
)
