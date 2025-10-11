# SNMP MIB module (ADTRAN-TA5K-SM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TA5K-SM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:05 2025
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

(adGenPortTrapIdentifier,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortTrapIdentifier")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adIdentity,
 adMgmt,
 adProducts) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity",
    "adMgmt",
    "adProducts")

(adTAeSCUTrapAlarmLevel,) = mibBuilder.importSymbols(
    "ADTRAN-TAeSCUEXT1-MIB",
    "adTAeSCUTrapAlarmLevel")

(InterfaceIndexOrZero,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifDescr",
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

adTa5kSmModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 750)
)
if mibBuilder.loadTexts:
    adTa5kSmModuleIdentity.setRevisions(
        ("2021-10-26 00:00",
         "2019-05-07 00:00",
         "2017-08-24 10:50",
         "2014-10-29 11:00",
         "2014-09-17 15:55",
         "2014-04-24 10:00",
         "2011-10-26 11:00",
         "2011-10-11 14:00",
         "2011-04-12 21:07")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EthernetDefaultInterfaceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("gigabitEthernet", 2),
          ("tenGigabitEthernet", 3),
          ("lagGroup", 4),
          ("accessModule", 5),
          ("efmGroup", 6),
          ("efmPort", 7),
          ("erps", 8),
          ("atmPort", 9),
          ("rpr", 10),
          ("atmGroup", 11),
          ("muxponderSlot", 12),
          ("xGigabitEthernet", 13))
    )



# MIB Managed Objects in the order of their OIDs

_AdTa5kSmTraps_ObjectIdentity = ObjectIdentity
adTa5kSmTraps = _AdTa5kSmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1, 750)
)
_AdTa5kSmAlarms_ObjectIdentity = ObjectIdentity
adTa5kSmAlarms = _AdTa5kSmAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0)
)
_AdTa5kSm_ObjectIdentity = ObjectIdentity
adTa5kSm = _AdTa5kSm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 750)
)
_AdTa5kSmConfig_ObjectIdentity = ObjectIdentity
adTa5kSmConfig = _AdTa5kSmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1)
)
_AdTa5kSmSystemTable_Object = MibTable
adTa5kSmSystemTable = _AdTa5kSmSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1)
)
if mibBuilder.loadTexts:
    adTa5kSmSystemTable.setStatus("current")
_AdTa5kSmSystemEntry_Object = MibTableRow
adTa5kSmSystemEntry = _AdTa5kSmSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1)
)
adTa5kSmSystemEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTa5kSmSystemEntry.setStatus("current")
_AdTa5kSmMaxNodes_Type = Integer32
_AdTa5kSmMaxNodes_Object = MibTableColumn
adTa5kSmMaxNodes = _AdTa5kSmMaxNodes_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 1),
    _AdTa5kSmMaxNodes_Type()
)
adTa5kSmMaxNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmMaxNodes.setStatus("current")


class _AdTa5kSmMaxShelves_Type(Integer32):
    """Custom type adTa5kSmMaxShelves based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AdTa5kSmMaxShelves_Type.__name__ = "Integer32"
_AdTa5kSmMaxShelves_Object = MibTableColumn
adTa5kSmMaxShelves = _AdTa5kSmMaxShelves_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 2),
    _AdTa5kSmMaxShelves_Type()
)
adTa5kSmMaxShelves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmMaxShelves.setStatus("current")


class _AdTa5kSmBootRev_Type(DisplayString):
    """Custom type adTa5kSmBootRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdTa5kSmBootRev_Type.__name__ = "DisplayString"
_AdTa5kSmBootRev_Object = MibTableColumn
adTa5kSmBootRev = _AdTa5kSmBootRev_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 3),
    _AdTa5kSmBootRev_Type()
)
adTa5kSmBootRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmBootRev.setStatus("current")


class _AdTa5kSmNet1SFPDescription_Type(DisplayString):
    """Custom type adTa5kSmNet1SFPDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdTa5kSmNet1SFPDescription_Type.__name__ = "DisplayString"
_AdTa5kSmNet1SFPDescription_Object = MibTableColumn
adTa5kSmNet1SFPDescription = _AdTa5kSmNet1SFPDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 4),
    _AdTa5kSmNet1SFPDescription_Type()
)
adTa5kSmNet1SFPDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmNet1SFPDescription.setStatus("deprecated")


class _AdTa5kSmNet2SFPDescription_Type(DisplayString):
    """Custom type adTa5kSmNet2SFPDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdTa5kSmNet2SFPDescription_Type.__name__ = "DisplayString"
_AdTa5kSmNet2SFPDescription_Object = MibTableColumn
adTa5kSmNet2SFPDescription = _AdTa5kSmNet2SFPDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 5),
    _AdTa5kSmNet2SFPDescription_Type()
)
adTa5kSmNet2SFPDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmNet2SFPDescription.setStatus("deprecated")


class _AdTa5kSmRingGenType_Type(Integer32):
    """Custom type adTa5kSmRingGenType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal40REN", 1),
          ("external", 2))
    )


_AdTa5kSmRingGenType_Type.__name__ = "Integer32"
_AdTa5kSmRingGenType_Object = MibTableColumn
adTa5kSmRingGenType = _AdTa5kSmRingGenType_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 6),
    _AdTa5kSmRingGenType_Type()
)
adTa5kSmRingGenType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmRingGenType.setStatus("current")


class _AdTa5kSmSMIOType_Type(Integer32):
    """Custom type adTa5kSmSMIOType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdTa5kSmSMIOType_Type.__name__ = "Integer32"
_AdTa5kSmSMIOType_Object = MibTableColumn
adTa5kSmSMIOType = _AdTa5kSmSMIOType_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 7),
    _AdTa5kSmSMIOType_Type()
)
adTa5kSmSMIOType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmSMIOType.setStatus("current")


class _AdTa5kSmNet1AutoNegoAdmnStat_Type(Integer32):
    """Custom type adTa5kSmNet1AutoNegoAdmnStat based on Integer32"""
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


_AdTa5kSmNet1AutoNegoAdmnStat_Type.__name__ = "Integer32"
_AdTa5kSmNet1AutoNegoAdmnStat_Object = MibTableColumn
adTa5kSmNet1AutoNegoAdmnStat = _AdTa5kSmNet1AutoNegoAdmnStat_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 8),
    _AdTa5kSmNet1AutoNegoAdmnStat_Type()
)
adTa5kSmNet1AutoNegoAdmnStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmNet1AutoNegoAdmnStat.setStatus("deprecated")


class _AdTa5kSmNet2AutoNegoAdmnStat_Type(Integer32):
    """Custom type adTa5kSmNet2AutoNegoAdmnStat based on Integer32"""
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


_AdTa5kSmNet2AutoNegoAdmnStat_Type.__name__ = "Integer32"
_AdTa5kSmNet2AutoNegoAdmnStat_Object = MibTableColumn
adTa5kSmNet2AutoNegoAdmnStat = _AdTa5kSmNet2AutoNegoAdmnStat_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 9),
    _AdTa5kSmNet2AutoNegoAdmnStat_Type()
)
adTa5kSmNet2AutoNegoAdmnStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmNet2AutoNegoAdmnStat.setStatus("deprecated")


class _AdTa5kSmNet1SFPVendorPartNumber_Type(DisplayString):
    """Custom type adTa5kSmNet1SFPVendorPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdTa5kSmNet1SFPVendorPartNumber_Type.__name__ = "DisplayString"
_AdTa5kSmNet1SFPVendorPartNumber_Object = MibTableColumn
adTa5kSmNet1SFPVendorPartNumber = _AdTa5kSmNet1SFPVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 10),
    _AdTa5kSmNet1SFPVendorPartNumber_Type()
)
adTa5kSmNet1SFPVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmNet1SFPVendorPartNumber.setStatus("current")


class _AdTa5kSmNet1SFPVendorSerialNumber_Type(DisplayString):
    """Custom type adTa5kSmNet1SFPVendorSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdTa5kSmNet1SFPVendorSerialNumber_Type.__name__ = "DisplayString"
_AdTa5kSmNet1SFPVendorSerialNumber_Object = MibTableColumn
adTa5kSmNet1SFPVendorSerialNumber = _AdTa5kSmNet1SFPVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 11),
    _AdTa5kSmNet1SFPVendorSerialNumber_Type()
)
adTa5kSmNet1SFPVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmNet1SFPVendorSerialNumber.setStatus("deprecated")


class _AdTa5kSmNet1SFPRxPowerLevel_Type(Integer32):
    """Custom type adTa5kSmNet1SFPRxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7000, 7000),
    )


_AdTa5kSmNet1SFPRxPowerLevel_Type.__name__ = "Integer32"
_AdTa5kSmNet1SFPRxPowerLevel_Object = MibTableColumn
adTa5kSmNet1SFPRxPowerLevel = _AdTa5kSmNet1SFPRxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 12),
    _AdTa5kSmNet1SFPRxPowerLevel_Type()
)
adTa5kSmNet1SFPRxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmNet1SFPRxPowerLevel.setStatus("deprecated")


class _AdTa5kSmNet1SFPTxPowerLevel_Type(Integer32):
    """Custom type adTa5kSmNet1SFPTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7000, 7000),
    )


_AdTa5kSmNet1SFPTxPowerLevel_Type.__name__ = "Integer32"
_AdTa5kSmNet1SFPTxPowerLevel_Object = MibTableColumn
adTa5kSmNet1SFPTxPowerLevel = _AdTa5kSmNet1SFPTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 13),
    _AdTa5kSmNet1SFPTxPowerLevel_Type()
)
adTa5kSmNet1SFPTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmNet1SFPTxPowerLevel.setStatus("deprecated")


class _AdTa5kSmNet1SFPTxBias_Type(Integer32):
    """Custom type adTa5kSmNet1SFPTxBias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdTa5kSmNet1SFPTxBias_Type.__name__ = "Integer32"
_AdTa5kSmNet1SFPTxBias_Object = MibTableColumn
adTa5kSmNet1SFPTxBias = _AdTa5kSmNet1SFPTxBias_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 14),
    _AdTa5kSmNet1SFPTxBias_Type()
)
adTa5kSmNet1SFPTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmNet1SFPTxBias.setStatus("deprecated")


class _AdTa5kSmNet1SFPTemperature_Type(Integer32):
    """Custom type adTa5kSmNet1SFPTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, 140),
    )


_AdTa5kSmNet1SFPTemperature_Type.__name__ = "Integer32"
_AdTa5kSmNet1SFPTemperature_Object = MibTableColumn
adTa5kSmNet1SFPTemperature = _AdTa5kSmNet1SFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 15),
    _AdTa5kSmNet1SFPTemperature_Type()
)
adTa5kSmNet1SFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmNet1SFPTemperature.setStatus("deprecated")
_AdTa5kSmNet1SFPSupplyVoltage_Type = Integer32
_AdTa5kSmNet1SFPSupplyVoltage_Object = MibTableColumn
adTa5kSmNet1SFPSupplyVoltage = _AdTa5kSmNet1SFPSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 16),
    _AdTa5kSmNet1SFPSupplyVoltage_Type()
)
adTa5kSmNet1SFPSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmNet1SFPSupplyVoltage.setStatus("deprecated")


class _AdTa5kSmNet2SFPVendorPartNumber_Type(DisplayString):
    """Custom type adTa5kSmNet2SFPVendorPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdTa5kSmNet2SFPVendorPartNumber_Type.__name__ = "DisplayString"
_AdTa5kSmNet2SFPVendorPartNumber_Object = MibTableColumn
adTa5kSmNet2SFPVendorPartNumber = _AdTa5kSmNet2SFPVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 17),
    _AdTa5kSmNet2SFPVendorPartNumber_Type()
)
adTa5kSmNet2SFPVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmNet2SFPVendorPartNumber.setStatus("deprecated")


class _AdTa5kSmNet2SFPVendorSerialNumber_Type(DisplayString):
    """Custom type adTa5kSmNet2SFPVendorSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdTa5kSmNet2SFPVendorSerialNumber_Type.__name__ = "DisplayString"
_AdTa5kSmNet2SFPVendorSerialNumber_Object = MibTableColumn
adTa5kSmNet2SFPVendorSerialNumber = _AdTa5kSmNet2SFPVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 18),
    _AdTa5kSmNet2SFPVendorSerialNumber_Type()
)
adTa5kSmNet2SFPVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmNet2SFPVendorSerialNumber.setStatus("deprecated")


class _AdTa5kSmNet2SFPRxPowerLevel_Type(Integer32):
    """Custom type adTa5kSmNet2SFPRxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7000, 7000),
    )


_AdTa5kSmNet2SFPRxPowerLevel_Type.__name__ = "Integer32"
_AdTa5kSmNet2SFPRxPowerLevel_Object = MibTableColumn
adTa5kSmNet2SFPRxPowerLevel = _AdTa5kSmNet2SFPRxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 19),
    _AdTa5kSmNet2SFPRxPowerLevel_Type()
)
adTa5kSmNet2SFPRxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmNet2SFPRxPowerLevel.setStatus("deprecated")


class _AdTa5kSmNet2SFPTxPowerLevel_Type(Integer32):
    """Custom type adTa5kSmNet2SFPTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7000, 7000),
    )


_AdTa5kSmNet2SFPTxPowerLevel_Type.__name__ = "Integer32"
_AdTa5kSmNet2SFPTxPowerLevel_Object = MibTableColumn
adTa5kSmNet2SFPTxPowerLevel = _AdTa5kSmNet2SFPTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 20),
    _AdTa5kSmNet2SFPTxPowerLevel_Type()
)
adTa5kSmNet2SFPTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmNet2SFPTxPowerLevel.setStatus("deprecated")


class _AdTa5kSmNet2SFPTxBias_Type(Integer32):
    """Custom type adTa5kSmNet2SFPTxBias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdTa5kSmNet2SFPTxBias_Type.__name__ = "Integer32"
_AdTa5kSmNet2SFPTxBias_Object = MibTableColumn
adTa5kSmNet2SFPTxBias = _AdTa5kSmNet2SFPTxBias_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 21),
    _AdTa5kSmNet2SFPTxBias_Type()
)
adTa5kSmNet2SFPTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmNet2SFPTxBias.setStatus("deprecated")


class _AdTa5kSmNet2SFPTemperature_Type(Integer32):
    """Custom type adTa5kSmNet2SFPTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, 140),
    )


_AdTa5kSmNet2SFPTemperature_Type.__name__ = "Integer32"
_AdTa5kSmNet2SFPTemperature_Object = MibTableColumn
adTa5kSmNet2SFPTemperature = _AdTa5kSmNet2SFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 22),
    _AdTa5kSmNet2SFPTemperature_Type()
)
adTa5kSmNet2SFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmNet2SFPTemperature.setStatus("deprecated")
_AdTa5kSmNet2SFPSupplyVoltage_Type = Integer32
_AdTa5kSmNet2SFPSupplyVoltage_Object = MibTableColumn
adTa5kSmNet2SFPSupplyVoltage = _AdTa5kSmNet2SFPSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 1, 1, 1, 23),
    _AdTa5kSmNet2SFPSupplyVoltage_Type()
)
adTa5kSmNet2SFPSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmNet2SFPSupplyVoltage.setStatus("deprecated")
_AdTa5kSmProv_ObjectIdentity = ObjectIdentity
adTa5kSmProv = _AdTa5kSmProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2)
)
_AdTa5kSmProvTable_Object = MibTable
adTa5kSmProvTable = _AdTa5kSmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1)
)
if mibBuilder.loadTexts:
    adTa5kSmProvTable.setStatus("current")
_AdTa5kSmProvEntry_Object = MibTableRow
adTa5kSmProvEntry = _AdTa5kSmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1)
)
adTa5kSmProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTa5kSmProvEntry.setStatus("current")
_AdTa5kSmNode_Type = Integer32
_AdTa5kSmNode_Object = MibTableColumn
adTa5kSmNode = _AdTa5kSmNode_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 1),
    _AdTa5kSmNode_Type()
)
adTa5kSmNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmNode.setStatus("current")
_AdTa5kSmUplink_Type = Integer32
_AdTa5kSmUplink_Object = MibTableColumn
adTa5kSmUplink = _AdTa5kSmUplink_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 2),
    _AdTa5kSmUplink_Type()
)
adTa5kSmUplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmUplink.setStatus("deprecated")


class _AdTa5kSmAggregation_Type(Integer32):
    """Custom type adTa5kSmAggregation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdTa5kSmAggregation_Type.__name__ = "Integer32"
_AdTa5kSmAggregation_Object = MibTableColumn
adTa5kSmAggregation = _AdTa5kSmAggregation_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 3),
    _AdTa5kSmAggregation_Type()
)
adTa5kSmAggregation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmAggregation.setStatus("current")


class _AdTa5kSmPrimaryClock_Type(Integer32):
    """Custom type adTa5kSmPrimaryClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("net1", 2),
          ("net2", 3),
          ("loopA", 4),
          ("loopB", 5),
          ("extA", 7),
          ("extB", 8))
    )


_AdTa5kSmPrimaryClock_Type.__name__ = "Integer32"
_AdTa5kSmPrimaryClock_Object = MibTableColumn
adTa5kSmPrimaryClock = _AdTa5kSmPrimaryClock_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 4),
    _AdTa5kSmPrimaryClock_Type()
)
adTa5kSmPrimaryClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmPrimaryClock.setStatus("deprecated")


class _AdTa5kSmSecondaryClock_Type(Integer32):
    """Custom type adTa5kSmSecondaryClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("net1", 2),
          ("net2", 3),
          ("loopA", 4),
          ("loopB", 5),
          ("extA", 7),
          ("extB", 8))
    )


_AdTa5kSmSecondaryClock_Type.__name__ = "Integer32"
_AdTa5kSmSecondaryClock_Object = MibTableColumn
adTa5kSmSecondaryClock = _AdTa5kSmSecondaryClock_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 5),
    _AdTa5kSmSecondaryClock_Type()
)
adTa5kSmSecondaryClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmSecondaryClock.setStatus("deprecated")


class _AdTa5kSmCurrentClock_Type(Integer32):
    """Custom type adTa5kSmCurrentClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("fallback", 3),
          ("standby", 4))
    )


_AdTa5kSmCurrentClock_Type.__name__ = "Integer32"
_AdTa5kSmCurrentClock_Object = MibTableColumn
adTa5kSmCurrentClock = _AdTa5kSmCurrentClock_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 6),
    _AdTa5kSmCurrentClock_Type()
)
adTa5kSmCurrentClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmCurrentClock.setStatus("deprecated")


class _AdTa5kSmClockModeRevertive_Type(Integer32):
    """Custom type adTa5kSmClockModeRevertive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AdTa5kSmClockModeRevertive_Type.__name__ = "Integer32"
_AdTa5kSmClockModeRevertive_Object = MibTableColumn
adTa5kSmClockModeRevertive = _AdTa5kSmClockModeRevertive_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 7),
    _AdTa5kSmClockModeRevertive_Type()
)
adTa5kSmClockModeRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmClockModeRevertive.setStatus("deprecated")


class _AdTa5kSmForceClockFailover_Type(Integer32):
    """Custom type adTa5kSmForceClockFailover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failover", 1),
          ("notavailable", 2))
    )


_AdTa5kSmForceClockFailover_Type.__name__ = "Integer32"
_AdTa5kSmForceClockFailover_Object = MibTableColumn
adTa5kSmForceClockFailover = _AdTa5kSmForceClockFailover_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 8),
    _AdTa5kSmForceClockFailover_Type()
)
adTa5kSmForceClockFailover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmForceClockFailover.setStatus("deprecated")


class _AdTa5kSmNetworkName_Type(DisplayString):
    """Custom type adTa5kSmNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdTa5kSmNetworkName_Type.__name__ = "DisplayString"
_AdTa5kSmNetworkName_Object = MibTableColumn
adTa5kSmNetworkName = _AdTa5kSmNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 10),
    _AdTa5kSmNetworkName_Type()
)
adTa5kSmNetworkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmNetworkName.setStatus("current")
_AdTa5kSmTopologyChangeCount_Type = Integer32
_AdTa5kSmTopologyChangeCount_Object = MibTableColumn
adTa5kSmTopologyChangeCount = _AdTa5kSmTopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 11),
    _AdTa5kSmTopologyChangeCount_Type()
)
adTa5kSmTopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmTopologyChangeCount.setStatus("current")
_AdTa5kSmTopologyInstance_Type = Integer32
_AdTa5kSmTopologyInstance_Object = MibTableColumn
adTa5kSmTopologyInstance = _AdTa5kSmTopologyInstance_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 12),
    _AdTa5kSmTopologyInstance_Type()
)
adTa5kSmTopologyInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmTopologyInstance.setStatus("current")
_AdTa5kSmLoopASource_Type = Integer32
_AdTa5kSmLoopASource_Object = MibTableColumn
adTa5kSmLoopASource = _AdTa5kSmLoopASource_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 13),
    _AdTa5kSmLoopASource_Type()
)
adTa5kSmLoopASource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmLoopASource.setStatus("deprecated")
_AdTa5kSmLoopBSource_Type = Integer32
_AdTa5kSmLoopBSource_Object = MibTableColumn
adTa5kSmLoopBSource = _AdTa5kSmLoopBSource_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 14),
    _AdTa5kSmLoopBSource_Type()
)
adTa5kSmLoopBSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmLoopBSource.setStatus("deprecated")


class _AdTa5kSmExtAType_Type(Integer32):
    """Custom type adTa5kSmExtAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bitsD4", 1),
          ("bitsOD", 2),
          ("composite", 3),
          ("composite8kHz", 4))
    )


_AdTa5kSmExtAType_Type.__name__ = "Integer32"
_AdTa5kSmExtAType_Object = MibTableColumn
adTa5kSmExtAType = _AdTa5kSmExtAType_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 15),
    _AdTa5kSmExtAType_Type()
)
adTa5kSmExtAType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmExtAType.setStatus("deprecated")


class _AdTa5kSmExtBType_Type(Integer32):
    """Custom type adTa5kSmExtBType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bitsD4", 1),
          ("bitsOD", 2),
          ("composite", 3),
          ("composite8kHz", 4))
    )


_AdTa5kSmExtBType_Type.__name__ = "Integer32"
_AdTa5kSmExtBType_Object = MibTableColumn
adTa5kSmExtBType = _AdTa5kSmExtBType_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 16),
    _AdTa5kSmExtBType_Type()
)
adTa5kSmExtBType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmExtBType.setStatus("deprecated")


class _AdTa5kSmUpstreamChaining_Type(Integer32):
    """Custom type adTa5kSmUpstreamChaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdTa5kSmUpstreamChaining_Type.__name__ = "Integer32"
_AdTa5kSmUpstreamChaining_Object = MibTableColumn
adTa5kSmUpstreamChaining = _AdTa5kSmUpstreamChaining_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 17),
    _AdTa5kSmUpstreamChaining_Type()
)
adTa5kSmUpstreamChaining.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmUpstreamChaining.setStatus("deprecated")


class _AdTa5kSmDownstreamChaining_Type(Integer32):
    """Custom type adTa5kSmDownstreamChaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdTa5kSmDownstreamChaining_Type.__name__ = "Integer32"
_AdTa5kSmDownstreamChaining_Object = MibTableColumn
adTa5kSmDownstreamChaining = _AdTa5kSmDownstreamChaining_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 18),
    _AdTa5kSmDownstreamChaining_Type()
)
adTa5kSmDownstreamChaining.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmDownstreamChaining.setStatus("deprecated")


class _AdTa5kSmFallbackClock_Type(Integer32):
    """Custom type adTa5kSmFallbackClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("local", 1),
          ("net1", 2),
          ("net2", 3),
          ("loopA", 4),
          ("loopB", 5),
          ("none", 6),
          ("extA", 7),
          ("extB", 8))
    )


_AdTa5kSmFallbackClock_Type.__name__ = "Integer32"
_AdTa5kSmFallbackClock_Object = MibTableColumn
adTa5kSmFallbackClock = _AdTa5kSmFallbackClock_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 19),
    _AdTa5kSmFallbackClock_Type()
)
adTa5kSmFallbackClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmFallbackClock.setStatus("deprecated")


class _AdTa5kSmExtAQuality_Type(Integer32):
    """Custom type adTa5kSmExtAQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              15)
        )
    )
    namedValues = NamedValues(
        *(("stratum1", 1),
          ("synchronized", 2),
          ("stratum2", 3),
          ("transmitModeClock", 4),
          ("stratum3e", 5),
          ("stratum3", 6),
          ("sonetClock", 7),
          ("stratum4or4e", 8),
          ("doNotUseForSync", 15))
    )


_AdTa5kSmExtAQuality_Type.__name__ = "Integer32"
_AdTa5kSmExtAQuality_Object = MibTableColumn
adTa5kSmExtAQuality = _AdTa5kSmExtAQuality_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 20),
    _AdTa5kSmExtAQuality_Type()
)
adTa5kSmExtAQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmExtAQuality.setStatus("deprecated")


class _AdTa5kSmExtBQuality_Type(Integer32):
    """Custom type adTa5kSmExtBQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              15)
        )
    )
    namedValues = NamedValues(
        *(("stratum1", 1),
          ("synchronized", 2),
          ("stratum2", 3),
          ("transmitModeClock", 4),
          ("stratum3e", 5),
          ("stratum3", 6),
          ("sonetClock", 7),
          ("stratum4or4e", 8),
          ("doNotUseForSync", 15))
    )


_AdTa5kSmExtBQuality_Type.__name__ = "Integer32"
_AdTa5kSmExtBQuality_Object = MibTableColumn
adTa5kSmExtBQuality = _AdTa5kSmExtBQuality_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 21),
    _AdTa5kSmExtBQuality_Type()
)
adTa5kSmExtBQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmExtBQuality.setStatus("deprecated")


class _AdTa5kSmExtAPreference_Type(Integer32):
    """Custom type adTa5kSmExtAPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AdTa5kSmExtAPreference_Type.__name__ = "Integer32"
_AdTa5kSmExtAPreference_Object = MibTableColumn
adTa5kSmExtAPreference = _AdTa5kSmExtAPreference_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 22),
    _AdTa5kSmExtAPreference_Type()
)
adTa5kSmExtAPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmExtAPreference.setStatus("deprecated")


class _AdTa5kSmExtBPreference_Type(Integer32):
    """Custom type adTa5kSmExtBPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AdTa5kSmExtBPreference_Type.__name__ = "Integer32"
_AdTa5kSmExtBPreference_Object = MibTableColumn
adTa5kSmExtBPreference = _AdTa5kSmExtBPreference_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 23),
    _AdTa5kSmExtBPreference_Type()
)
adTa5kSmExtBPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmExtBPreference.setStatus("deprecated")


class _AdTa5kSmUseHopCount_Type(Integer32):
    """Custom type adTa5kSmUseHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AdTa5kSmUseHopCount_Type.__name__ = "Integer32"
_AdTa5kSmUseHopCount_Object = MibTableColumn
adTa5kSmUseHopCount = _AdTa5kSmUseHopCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 24),
    _AdTa5kSmUseHopCount_Type()
)
adTa5kSmUseHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmUseHopCount.setStatus("deprecated")


class _AdTa5kSmIGMPInterfaceMode_Type(Integer32):
    """Custom type adTa5kSmIGMPInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("diable", 1),
          ("proxy", 2),
          ("snooping", 4))
    )


_AdTa5kSmIGMPInterfaceMode_Type.__name__ = "Integer32"
_AdTa5kSmIGMPInterfaceMode_Object = MibTableColumn
adTa5kSmIGMPInterfaceMode = _AdTa5kSmIGMPInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 25),
    _AdTa5kSmIGMPInterfaceMode_Type()
)
adTa5kSmIGMPInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmIGMPInterfaceMode.setStatus("current")


class _AdTa5kSmSTagTPID_Type(Integer32):
    """Custom type adTa5kSmSTagTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdTa5kSmSTagTPID_Type.__name__ = "Integer32"
_AdTa5kSmSTagTPID_Object = MibTableColumn
adTa5kSmSTagTPID = _AdTa5kSmSTagTPID_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 26),
    _AdTa5kSmSTagTPID_Type()
)
adTa5kSmSTagTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmSTagTPID.setStatus("current")


class _AdTa5kSmExtAPriority_Type(Integer32):
    """Custom type adTa5kSmExtAPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdTa5kSmExtAPriority_Type.__name__ = "Integer32"
_AdTa5kSmExtAPriority_Object = MibTableColumn
adTa5kSmExtAPriority = _AdTa5kSmExtAPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 27),
    _AdTa5kSmExtAPriority_Type()
)
adTa5kSmExtAPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmExtAPriority.setStatus("deprecated")


class _AdTa5kSmExtBPriority_Type(Integer32):
    """Custom type adTa5kSmExtBPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdTa5kSmExtBPriority_Type.__name__ = "Integer32"
_AdTa5kSmExtBPriority_Object = MibTableColumn
adTa5kSmExtBPriority = _AdTa5kSmExtBPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 28),
    _AdTa5kSmExtBPriority_Type()
)
adTa5kSmExtBPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmExtBPriority.setStatus("deprecated")


class _AdTa5kSmInternalSTag_Type(Integer32):
    """Custom type adTa5kSmInternalSTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_AdTa5kSmInternalSTag_Type.__name__ = "Integer32"
_AdTa5kSmInternalSTag_Object = MibTableColumn
adTa5kSmInternalSTag = _AdTa5kSmInternalSTag_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 29),
    _AdTa5kSmInternalSTag_Type()
)
adTa5kSmInternalSTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmInternalSTag.setStatus("current")


class _AdTa5kSmBpRateAlarmSeverityLevel_Type(Integer32):
    """Custom type adTa5kSmBpRateAlarmSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdTa5kSmBpRateAlarmSeverityLevel_Type.__name__ = "Integer32"
_AdTa5kSmBpRateAlarmSeverityLevel_Object = MibTableColumn
adTa5kSmBpRateAlarmSeverityLevel = _AdTa5kSmBpRateAlarmSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 1, 1, 30),
    _AdTa5kSmBpRateAlarmSeverityLevel_Type()
)
adTa5kSmBpRateAlarmSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmBpRateAlarmSeverityLevel.setStatus("current")
_AdTa5kSmNetworkPortProvTable_Object = MibTable
adTa5kSmNetworkPortProvTable = _AdTa5kSmNetworkPortProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 2)
)
if mibBuilder.loadTexts:
    adTa5kSmNetworkPortProvTable.setStatus("current")
_AdTa5kSmNetworkPortProvEntry_Object = MibTableRow
adTa5kSmNetworkPortProvEntry = _AdTa5kSmNetworkPortProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 2, 1)
)
adTa5kSmNetworkPortProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTa5kSmNetworkPortProvEntry.setStatus("current")


class _AdTa5kSmPortMode_Type(Integer32):
    """Custom type adTa5kSmPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unused", 1),
          ("networkInterface", 2),
          ("uplink", 3),
          ("downlink", 4),
          ("erps", 5))
    )


_AdTa5kSmPortMode_Type.__name__ = "Integer32"
_AdTa5kSmPortMode_Object = MibTableColumn
adTa5kSmPortMode = _AdTa5kSmPortMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 2, 1, 1),
    _AdTa5kSmPortMode_Type()
)
adTa5kSmPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmPortMode.setStatus("deprecated")


class _AdTa5kSmLACPMode_Type(Integer32):
    """Custom type adTa5kSmLACPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("active", 2),
          ("passive", 3))
    )


_AdTa5kSmLACPMode_Type.__name__ = "Integer32"
_AdTa5kSmLACPMode_Object = MibTableColumn
adTa5kSmLACPMode = _AdTa5kSmLACPMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 2, 1, 2),
    _AdTa5kSmLACPMode_Type()
)
adTa5kSmLACPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmLACPMode.setStatus("deprecated")
_AdTa5kSmEthernetDefaultInterface_ObjectIdentity = ObjectIdentity
adTa5kSmEthernetDefaultInterface = _AdTa5kSmEthernetDefaultInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 3)
)
_AdTa5kSmEthDefaultInterfaceIndex_Type = InterfaceIndexOrZero
_AdTa5kSmEthDefaultInterfaceIndex_Object = MibScalar
adTa5kSmEthDefaultInterfaceIndex = _AdTa5kSmEthDefaultInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 3, 1),
    _AdTa5kSmEthDefaultInterfaceIndex_Type()
)
adTa5kSmEthDefaultInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmEthDefaultInterfaceIndex.setStatus("current")
_AdTa5kSmEthernetDefaultIfcType_Type = EthernetDefaultInterfaceType
_AdTa5kSmEthernetDefaultIfcType_Object = MibScalar
adTa5kSmEthernetDefaultIfcType = _AdTa5kSmEthernetDefaultIfcType_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 3, 2),
    _AdTa5kSmEthernetDefaultIfcType_Type()
)
adTa5kSmEthernetDefaultIfcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmEthernetDefaultIfcType.setStatus("current")


class _AdTa5kSmEthernetDefaultIfcSlot_Type(Integer32):
    """Custom type adTa5kSmEthernetDefaultIfcSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdTa5kSmEthernetDefaultIfcSlot_Type.__name__ = "Integer32"
_AdTa5kSmEthernetDefaultIfcSlot_Object = MibScalar
adTa5kSmEthernetDefaultIfcSlot = _AdTa5kSmEthernetDefaultIfcSlot_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 3, 3),
    _AdTa5kSmEthernetDefaultIfcSlot_Type()
)
adTa5kSmEthernetDefaultIfcSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmEthernetDefaultIfcSlot.setStatus("current")


class _AdTa5kSmEthernetDefaultIfcPort_Type(Integer32):
    """Custom type adTa5kSmEthernetDefaultIfcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdTa5kSmEthernetDefaultIfcPort_Type.__name__ = "Integer32"
_AdTa5kSmEthernetDefaultIfcPort_Object = MibScalar
adTa5kSmEthernetDefaultIfcPort = _AdTa5kSmEthernetDefaultIfcPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 3, 4),
    _AdTa5kSmEthernetDefaultIfcPort_Type()
)
adTa5kSmEthernetDefaultIfcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmEthernetDefaultIfcPort.setStatus("current")
_AdTa5kSmAlarmProvTable_Object = MibTable
adTa5kSmAlarmProvTable = _AdTa5kSmAlarmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 4)
)
if mibBuilder.loadTexts:
    adTa5kSmAlarmProvTable.setStatus("current")
_AdTa5kSmAlarmProvEntry_Object = MibTableRow
adTa5kSmAlarmProvEntry = _AdTa5kSmAlarmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 4, 1)
)
adTa5kSmAlarmProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTa5kSmAlarmProvEntry.setStatus("current")


class _AdTa5kSmRingGenFailAlarmEnable_Type(TruthValue):
    """Custom type adTa5kSmRingGenFailAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kSmRingGenFailAlarmEnable_Type.__name__ = "TruthValue"
_AdTa5kSmRingGenFailAlarmEnable_Object = MibTableColumn
adTa5kSmRingGenFailAlarmEnable = _AdTa5kSmRingGenFailAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 4, 1, 1),
    _AdTa5kSmRingGenFailAlarmEnable_Type()
)
adTa5kSmRingGenFailAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmRingGenFailAlarmEnable.setStatus("current")


class _AdTa5kSmPowerLimitExceededAlarmEnable_Type(TruthValue):
    """Custom type adTa5kSmPowerLimitExceededAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kSmPowerLimitExceededAlarmEnable_Type.__name__ = "TruthValue"
_AdTa5kSmPowerLimitExceededAlarmEnable_Object = MibTableColumn
adTa5kSmPowerLimitExceededAlarmEnable = _AdTa5kSmPowerLimitExceededAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 4, 1, 2),
    _AdTa5kSmPowerLimitExceededAlarmEnable_Type()
)
adTa5kSmPowerLimitExceededAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmPowerLimitExceededAlarmEnable.setStatus("current")


class _AdTa5kSmDuplicateNodeAlarmEnable_Type(TruthValue):
    """Custom type adTa5kSmDuplicateNodeAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kSmDuplicateNodeAlarmEnable_Type.__name__ = "TruthValue"
_AdTa5kSmDuplicateNodeAlarmEnable_Object = MibTableColumn
adTa5kSmDuplicateNodeAlarmEnable = _AdTa5kSmDuplicateNodeAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 4, 1, 3),
    _AdTa5kSmDuplicateNodeAlarmEnable_Type()
)
adTa5kSmDuplicateNodeAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmDuplicateNodeAlarmEnable.setStatus("current")


class _AdTa5kSmDuplicateScmIpAlarmEnable_Type(TruthValue):
    """Custom type adTa5kSmDuplicateScmIpAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kSmDuplicateScmIpAlarmEnable_Type.__name__ = "TruthValue"
_AdTa5kSmDuplicateScmIpAlarmEnable_Object = MibTableColumn
adTa5kSmDuplicateScmIpAlarmEnable = _AdTa5kSmDuplicateScmIpAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 4, 1, 4),
    _AdTa5kSmDuplicateScmIpAlarmEnable_Type()
)
adTa5kSmDuplicateScmIpAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmDuplicateScmIpAlarmEnable.setStatus("current")


class _AdTa5kSmNodeNumberProvAlarmEnable_Type(TruthValue):
    """Custom type adTa5kSmNodeNumberProvAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kSmNodeNumberProvAlarmEnable_Type.__name__ = "TruthValue"
_AdTa5kSmNodeNumberProvAlarmEnable_Object = MibTableColumn
adTa5kSmNodeNumberProvAlarmEnable = _AdTa5kSmNodeNumberProvAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 4, 1, 5),
    _AdTa5kSmNodeNumberProvAlarmEnable_Type()
)
adTa5kSmNodeNumberProvAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmNodeNumberProvAlarmEnable.setStatus("current")


class _AdTa5kSmMgmtVlanFailAlarmEnable_Type(TruthValue):
    """Custom type adTa5kSmMgmtVlanFailAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kSmMgmtVlanFailAlarmEnable_Type.__name__ = "TruthValue"
_AdTa5kSmMgmtVlanFailAlarmEnable_Object = MibTableColumn
adTa5kSmMgmtVlanFailAlarmEnable = _AdTa5kSmMgmtVlanFailAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 4, 1, 6),
    _AdTa5kSmMgmtVlanFailAlarmEnable_Type()
)
adTa5kSmMgmtVlanFailAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmMgmtVlanFailAlarmEnable.setStatus("current")


class _AdTa5kSmioMismatchAlarmEnable_Type(TruthValue):
    """Custom type adTa5kSmioMismatchAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kSmioMismatchAlarmEnable_Type.__name__ = "TruthValue"
_AdTa5kSmioMismatchAlarmEnable_Object = MibTableColumn
adTa5kSmioMismatchAlarmEnable = _AdTa5kSmioMismatchAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 4, 1, 7),
    _AdTa5kSmioMismatchAlarmEnable_Type()
)
adTa5kSmioMismatchAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmioMismatchAlarmEnable.setStatus("current")


class _AdTa5kSmBPRateFallbackAlarmEnable_Type(TruthValue):
    """Custom type adTa5kSmBPRateFallbackAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kSmBPRateFallbackAlarmEnable_Type.__name__ = "TruthValue"
_AdTa5kSmBPRateFallbackAlarmEnable_Object = MibTableColumn
adTa5kSmBPRateFallbackAlarmEnable = _AdTa5kSmBPRateFallbackAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 4, 1, 8),
    _AdTa5kSmBPRateFallbackAlarmEnable_Type()
)
adTa5kSmBPRateFallbackAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmBPRateFallbackAlarmEnable.setStatus("current")


class _AdTa5kSmPeerLinksDownAlarmEnable_Type(TruthValue):
    """Custom type adTa5kSmPeerLinksDownAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kSmPeerLinksDownAlarmEnable_Type.__name__ = "TruthValue"
_AdTa5kSmPeerLinksDownAlarmEnable_Object = MibTableColumn
adTa5kSmPeerLinksDownAlarmEnable = _AdTa5kSmPeerLinksDownAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 2, 4, 1, 9),
    _AdTa5kSmPeerLinksDownAlarmEnable_Type()
)
adTa5kSmPeerLinksDownAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmPeerLinksDownAlarmEnable.setStatus("current")
_AdTa5kSmStatus_ObjectIdentity = ObjectIdentity
adTa5kSmStatus = _AdTa5kSmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 3)
)
_AdTa5kSmClockStatusTable_Object = MibTable
adTa5kSmClockStatusTable = _AdTa5kSmClockStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 3, 1)
)
if mibBuilder.loadTexts:
    adTa5kSmClockStatusTable.setStatus("current")
_AdTa5kSmClockStatusEntry_Object = MibTableRow
adTa5kSmClockStatusEntry = _AdTa5kSmClockStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 3, 1, 1)
)
adTa5kSmClockStatusEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTa5kSmClockStatusEntry.setStatus("current")


class _AdTa5kSmLoopAClockHealth_Type(Integer32):
    """Custom type adTa5kSmLoopAClockHealth based on Integer32"""
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


_AdTa5kSmLoopAClockHealth_Type.__name__ = "Integer32"
_AdTa5kSmLoopAClockHealth_Object = MibTableColumn
adTa5kSmLoopAClockHealth = _AdTa5kSmLoopAClockHealth_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 3, 1, 1, 1),
    _AdTa5kSmLoopAClockHealth_Type()
)
adTa5kSmLoopAClockHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmLoopAClockHealth.setStatus("deprecated")


class _AdTa5kSmLoopBClockHealth_Type(Integer32):
    """Custom type adTa5kSmLoopBClockHealth based on Integer32"""
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


_AdTa5kSmLoopBClockHealth_Type.__name__ = "Integer32"
_AdTa5kSmLoopBClockHealth_Object = MibTableColumn
adTa5kSmLoopBClockHealth = _AdTa5kSmLoopBClockHealth_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 3, 1, 1, 2),
    _AdTa5kSmLoopBClockHealth_Type()
)
adTa5kSmLoopBClockHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmLoopBClockHealth.setStatus("deprecated")


class _AdTa5kSmBitsAClockHealth_Type(Integer32):
    """Custom type adTa5kSmBitsAClockHealth based on Integer32"""
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


_AdTa5kSmBitsAClockHealth_Type.__name__ = "Integer32"
_AdTa5kSmBitsAClockHealth_Object = MibTableColumn
adTa5kSmBitsAClockHealth = _AdTa5kSmBitsAClockHealth_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 3, 1, 1, 3),
    _AdTa5kSmBitsAClockHealth_Type()
)
adTa5kSmBitsAClockHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmBitsAClockHealth.setStatus("deprecated")


class _AdTa5kSmBitsBClockHealth_Type(Integer32):
    """Custom type adTa5kSmBitsBClockHealth based on Integer32"""
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


_AdTa5kSmBitsBClockHealth_Type.__name__ = "Integer32"
_AdTa5kSmBitsBClockHealth_Object = MibTableColumn
adTa5kSmBitsBClockHealth = _AdTa5kSmBitsBClockHealth_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 3, 1, 1, 4),
    _AdTa5kSmBitsBClockHealth_Type()
)
adTa5kSmBitsBClockHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmBitsBClockHealth.setStatus("deprecated")


class _AdTa5kSmPrimaryClockHealth_Type(Integer32):
    """Custom type adTa5kSmPrimaryClockHealth based on Integer32"""
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


_AdTa5kSmPrimaryClockHealth_Type.__name__ = "Integer32"
_AdTa5kSmPrimaryClockHealth_Object = MibTableColumn
adTa5kSmPrimaryClockHealth = _AdTa5kSmPrimaryClockHealth_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 3, 1, 1, 5),
    _AdTa5kSmPrimaryClockHealth_Type()
)
adTa5kSmPrimaryClockHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmPrimaryClockHealth.setStatus("deprecated")


class _AdTa5kSmSecondaryClockHealth_Type(Integer32):
    """Custom type adTa5kSmSecondaryClockHealth based on Integer32"""
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


_AdTa5kSmSecondaryClockHealth_Type.__name__ = "Integer32"
_AdTa5kSmSecondaryClockHealth_Object = MibTableColumn
adTa5kSmSecondaryClockHealth = _AdTa5kSmSecondaryClockHealth_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 3, 1, 1, 6),
    _AdTa5kSmSecondaryClockHealth_Type()
)
adTa5kSmSecondaryClockHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmSecondaryClockHealth.setStatus("deprecated")
_AdTa5kSmRingVoltagePresent_Type = Integer32
_AdTa5kSmRingVoltagePresent_Object = MibTableColumn
adTa5kSmRingVoltagePresent = _AdTa5kSmRingVoltagePresent_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 3, 1, 1, 7),
    _AdTa5kSmRingVoltagePresent_Type()
)
adTa5kSmRingVoltagePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmRingVoltagePresent.setStatus("deprecated")
_AdTa5kSmRingFail_Type = Integer32
_AdTa5kSmRingFail_Object = MibTableColumn
adTa5kSmRingFail = _AdTa5kSmRingFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 3, 1, 1, 8),
    _AdTa5kSmRingFail_Type()
)
adTa5kSmRingFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmRingFail.setStatus("current")
_AdTa5kSmPeerRingFail_Type = Integer32
_AdTa5kSmPeerRingFail_Object = MibTableColumn
adTa5kSmPeerRingFail = _AdTa5kSmPeerRingFail_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 3, 1, 1, 9),
    _AdTa5kSmPeerRingFail_Type()
)
adTa5kSmPeerRingFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmPeerRingFail.setStatus("current")


class _AdTa5kSmCurrentHopCount_Type(Integer32):
    """Custom type adTa5kSmCurrentHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdTa5kSmCurrentHopCount_Type.__name__ = "Integer32"
_AdTa5kSmCurrentHopCount_Object = MibTableColumn
adTa5kSmCurrentHopCount = _AdTa5kSmCurrentHopCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 3, 1, 1, 10),
    _AdTa5kSmCurrentHopCount_Type()
)
adTa5kSmCurrentHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmCurrentHopCount.setStatus("deprecated")


class _AdTa5kSmCurrentTimingSourcePriority_Type(Integer32):
    """Custom type adTa5kSmCurrentTimingSourcePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdTa5kSmCurrentTimingSourcePriority_Type.__name__ = "Integer32"
_AdTa5kSmCurrentTimingSourcePriority_Object = MibTableColumn
adTa5kSmCurrentTimingSourcePriority = _AdTa5kSmCurrentTimingSourcePriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 3, 1, 1, 11),
    _AdTa5kSmCurrentTimingSourcePriority_Type()
)
adTa5kSmCurrentTimingSourcePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmCurrentTimingSourcePriority.setStatus("deprecated")


class _AdTa5kSmCurrentTimingSourceQuality_Type(Integer32):
    """Custom type adTa5kSmCurrentTimingSourceQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              15)
        )
    )
    namedValues = NamedValues(
        *(("stratum1", 1),
          ("synchronized", 2),
          ("stratum2", 3),
          ("transmitModeClock", 4),
          ("stratum3e", 5),
          ("stratum3", 6),
          ("sonetClock", 7),
          ("stratum4or4e", 8),
          ("doNotUseForSync", 15))
    )


_AdTa5kSmCurrentTimingSourceQuality_Type.__name__ = "Integer32"
_AdTa5kSmCurrentTimingSourceQuality_Object = MibTableColumn
adTa5kSmCurrentTimingSourceQuality = _AdTa5kSmCurrentTimingSourceQuality_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 3, 1, 1, 12),
    _AdTa5kSmCurrentTimingSourceQuality_Type()
)
adTa5kSmCurrentTimingSourceQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmCurrentTimingSourceQuality.setStatus("deprecated")
_AdTa5kSmTest_ObjectIdentity = ObjectIdentity
adTa5kSmTest = _AdTa5kSmTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 4)
)
_AdTa5kSmMetalicTestAccessTable_Object = MibTable
adTa5kSmMetalicTestAccessTable = _AdTa5kSmMetalicTestAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 4, 1)
)
if mibBuilder.loadTexts:
    adTa5kSmMetalicTestAccessTable.setStatus("current")
_AdTa5kSmMetalicTestAccessEntry_Object = MibTableRow
adTa5kSmMetalicTestAccessEntry = _AdTa5kSmMetalicTestAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 4, 1, 1)
)
adTa5kSmMetalicTestAccessEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTa5kSmMetalicTestAccessEntry.setStatus("current")


class _AdTa5kSmFacilityTR_Type(Integer32):
    """Custom type adTa5kSmFacilityTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdTa5kSmFacilityTR_Type.__name__ = "Integer32"
_AdTa5kSmFacilityTR_Object = MibTableColumn
adTa5kSmFacilityTR = _AdTa5kSmFacilityTR_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 4, 1, 1, 1),
    _AdTa5kSmFacilityTR_Type()
)
adTa5kSmFacilityTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmFacilityTR.setStatus("current")


class _AdTa5kSmFacilityT1R1_Type(Integer32):
    """Custom type adTa5kSmFacilityT1R1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdTa5kSmFacilityT1R1_Type.__name__ = "Integer32"
_AdTa5kSmFacilityT1R1_Object = MibTableColumn
adTa5kSmFacilityT1R1 = _AdTa5kSmFacilityT1R1_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 4, 1, 1, 2),
    _AdTa5kSmFacilityT1R1_Type()
)
adTa5kSmFacilityT1R1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmFacilityT1R1.setStatus("current")


class _AdTa5kSmEquipmentTR_Type(Integer32):
    """Custom type adTa5kSmEquipmentTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdTa5kSmEquipmentTR_Type.__name__ = "Integer32"
_AdTa5kSmEquipmentTR_Object = MibTableColumn
adTa5kSmEquipmentTR = _AdTa5kSmEquipmentTR_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 4, 1, 1, 3),
    _AdTa5kSmEquipmentTR_Type()
)
adTa5kSmEquipmentTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmEquipmentTR.setStatus("current")


class _AdTa5kSmEquipmentT1R1_Type(Integer32):
    """Custom type adTa5kSmEquipmentT1R1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdTa5kSmEquipmentT1R1_Type.__name__ = "Integer32"
_AdTa5kSmEquipmentT1R1_Object = MibTableColumn
adTa5kSmEquipmentT1R1 = _AdTa5kSmEquipmentT1R1_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 4, 1, 1, 4),
    _AdTa5kSmEquipmentT1R1_Type()
)
adTa5kSmEquipmentT1R1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmEquipmentT1R1.setStatus("current")


class _AdTa5kSmLoopTR_Type(Integer32):
    """Custom type adTa5kSmLoopTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdTa5kSmLoopTR_Type.__name__ = "Integer32"
_AdTa5kSmLoopTR_Object = MibTableColumn
adTa5kSmLoopTR = _AdTa5kSmLoopTR_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 4, 1, 1, 5),
    _AdTa5kSmLoopTR_Type()
)
adTa5kSmLoopTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmLoopTR.setStatus("current")


class _AdTa5kSmLoopT1R1_Type(Integer32):
    """Custom type adTa5kSmLoopT1R1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdTa5kSmLoopT1R1_Type.__name__ = "Integer32"
_AdTa5kSmLoopT1R1_Object = MibTableColumn
adTa5kSmLoopT1R1 = _AdTa5kSmLoopT1R1_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 4, 1, 1, 6),
    _AdTa5kSmLoopT1R1_Type()
)
adTa5kSmLoopT1R1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmLoopT1R1.setStatus("current")
_AdTa5kSmPerfMon_ObjectIdentity = ObjectIdentity
adTa5kSmPerfMon = _AdTa5kSmPerfMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 5)
)
_AdTa5kSmAtpMfg_ObjectIdentity = ObjectIdentity
adTa5kSmAtpMfg = _AdTa5kSmAtpMfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 6)
)
_AdTa5kSmAtpTable_Object = MibTable
adTa5kSmAtpTable = _AdTa5kSmAtpTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 6, 1)
)
if mibBuilder.loadTexts:
    adTa5kSmAtpTable.setStatus("current")
_AdTa5kSmAtpEntry_Object = MibTableRow
adTa5kSmAtpEntry = _AdTa5kSmAtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 6, 1, 1)
)
adTa5kSmAtpEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTa5kSmAtpEntry.setStatus("current")


class _AdTa5kSmTemp1_Type(Integer32):
    """Custom type adTa5kSmTemp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AdTa5kSmTemp1_Type.__name__ = "Integer32"
_AdTa5kSmTemp1_Object = MibTableColumn
adTa5kSmTemp1 = _AdTa5kSmTemp1_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 6, 1, 1, 1),
    _AdTa5kSmTemp1_Type()
)
adTa5kSmTemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmTemp1.setStatus("current")


class _AdTa5kSmTemp2_Type(Integer32):
    """Custom type adTa5kSmTemp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AdTa5kSmTemp2_Type.__name__ = "Integer32"
_AdTa5kSmTemp2_Object = MibTableColumn
adTa5kSmTemp2 = _AdTa5kSmTemp2_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 6, 1, 1, 2),
    _AdTa5kSmTemp2_Type()
)
adTa5kSmTemp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmTemp2.setStatus("current")
_AdTa5kSmExpMac_Type = OctetString
_AdTa5kSmExpMac_Object = MibTableColumn
adTa5kSmExpMac = _AdTa5kSmExpMac_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 6, 1, 1, 3),
    _AdTa5kSmExpMac_Type()
)
adTa5kSmExpMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmExpMac.setStatus("current")
_AdTa5kSmPeerMac_Type = OctetString
_AdTa5kSmPeerMac_Object = MibTableColumn
adTa5kSmPeerMac = _AdTa5kSmPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 750, 6, 1, 1, 4),
    _AdTa5kSmPeerMac_Type()
)
adTa5kSmPeerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kSmPeerMac.setStatus("current")

# Managed Objects groups


# Notification objects

adTa5kSmTimingSrcClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 2)
)
adTa5kSmTimingSrcClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTa5kSmTimingSrcClear.setStatus(
        "deprecated"
    )

adTa5kSmTimingSrcFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 3)
)
adTa5kSmTimingSrcFail.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTa5kSmTimingSrcFail.setStatus(
        "deprecated"
    )

adTa5kSmRingGenClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 4)
)
adTa5kSmRingGenClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTa5kSmRingGenClear.setStatus(
        "current"
    )

adTa5kSmRingGenFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 5)
)
adTa5kSmRingGenFail.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTa5kSmRingGenFail.setStatus(
        "current"
    )

adTa5kSmPowerLimitAlmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 6)
)
adTa5kSmPowerLimitAlmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTa5kSmPowerLimitAlmClear.setStatus(
        "current"
    )

adTa5kSmPowerLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 7)
)
adTa5kSmPowerLimitExceeded.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTa5kSmPowerLimitExceeded.setStatus(
        "current"
    )

adTa5kSmUnknownSfpClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 8)
)
adTa5kSmUnknownSfpClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTa5kSmUnknownSfpClear.setStatus(
        "current"
    )

adTa5kSmUnknownSfpAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 9)
)
adTa5kSmUnknownSfpAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTa5kSmUnknownSfpAlarm.setStatus(
        "current"
    )

adTa5kSmSfpFaultClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 10)
)
adTa5kSmSfpFaultClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTa5kSmSfpFaultClear.setStatus(
        "current"
    )

adTa5kSmSfpFaultActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 11)
)
adTa5kSmSfpFaultActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTa5kSmSfpFaultActive.setStatus(
        "current"
    )

adTa5kSmMultipleUplinksClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 12)
)
adTa5kSmMultipleUplinksClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kSmMultipleUplinksClear.setStatus(
        "deprecated"
    )

adTa5kSmMultipleUplinksDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 13)
)
adTa5kSmMultipleUplinksDetected.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kSmMultipleUplinksDetected.setStatus(
        "deprecated"
    )

adTa5kSmExtAFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 14)
)
adTa5kSmExtAFailureClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kSmExtAFailureClear.setStatus(
        "current"
    )

adTa5kSmExtAFailureActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 15)
)
adTa5kSmExtAFailureActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kSmExtAFailureActive.setStatus(
        "current"
    )

adTa5kSmExtBFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 16)
)
adTa5kSmExtBFailureClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kSmExtBFailureClear.setStatus(
        "current"
    )

adTa5kSmExtBFailureActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 17)
)
adTa5kSmExtBFailureActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kSmExtBFailureActive.setStatus(
        "current"
    )

adTa5kSmLossOfHeartbeatClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 18)
)
adTa5kSmLossOfHeartbeatClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTa5kSmLossOfHeartbeatClear.setStatus(
        "current"
    )

adTa5kSmLossOfHeartbeatActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 19)
)
adTa5kSmLossOfHeartbeatActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTa5kSmLossOfHeartbeatActive.setStatus(
        "current"
    )

adTa5kSmLossOfNetworkStpClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 20)
)
adTa5kSmLossOfNetworkStpClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTa5kSmLossOfNetworkStpClear.setStatus(
        "deprecated"
    )

adTa5kSmLossOfNetworkStpActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 21)
)
adTa5kSmLossOfNetworkStpActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTa5kSmLossOfNetworkStpActive.setStatus(
        "deprecated"
    )

adTa5kSmDuplicateNodeClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 22)
)
adTa5kSmDuplicateNodeClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TA5K-SM-MIB", "adTa5kSmNode"))
)
if mibBuilder.loadTexts:
    adTa5kSmDuplicateNodeClear.setStatus(
        "current"
    )

adTa5kSmDuplicateNodeActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 23)
)
adTa5kSmDuplicateNodeActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TA5K-SM-MIB", "adTa5kSmNode"))
)
if mibBuilder.loadTexts:
    adTa5kSmDuplicateNodeActive.setStatus(
        "current"
    )

adTa5kSmDuplicateScmIpClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 24)
)
adTa5kSmDuplicateScmIpClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kSmDuplicateScmIpClear.setStatus(
        "current"
    )

adTa5kSmDuplicateScmIpActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 25)
)
adTa5kSmDuplicateScmIpActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kSmDuplicateScmIpActive.setStatus(
        "current"
    )

adTa5kSmBandwidthFullClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 26)
)
adTa5kSmBandwidthFullClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTa5kSmBandwidthFullClear.setStatus(
        "current"
    )

adTa5kSmBandwidthFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 27)
)
adTa5kSmBandwidthFull.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTa5kSmBandwidthFull.setStatus(
        "current"
    )

adTa5kSmPriTimingSrcClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 28)
)
adTa5kSmPriTimingSrcClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTa5kSmPriTimingSrcClear.setStatus(
        "deprecated"
    )

adTa5kSmPriTimingSrcFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 29)
)
adTa5kSmPriTimingSrcFail.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTa5kSmPriTimingSrcFail.setStatus(
        "deprecated"
    )

adTa5kSmSecTimingSrcClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 30)
)
adTa5kSmSecTimingSrcClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTa5kSmSecTimingSrcClear.setStatus(
        "deprecated"
    )

adTa5kSmSecTimingSrcFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 31)
)
adTa5kSmSecTimingSrcFail.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTa5kSmSecTimingSrcFail.setStatus(
        "deprecated"
    )

adTa5kSmNodeNumberProvClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 32)
)
adTa5kSmNodeNumberProvClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTa5kSmNodeNumberProvClear.setStatus(
        "current"
    )

adTa5kSmNodeNumberDefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 33)
)
adTa5kSmNodeNumberDefault.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTa5kSmNodeNumberDefault.setStatus(
        "current"
    )

adTa5kSmMgmtVlanFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 34)
)
adTa5kSmMgmtVlanFailClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kSmMgmtVlanFailClear.setStatus(
        "current"
    )

adTa5kSmMgmtVlanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 35)
)
adTa5kSmMgmtVlanFail.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kSmMgmtVlanFail.setStatus(
        "current"
    )

adTa5kSmioMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 36)
)
adTa5kSmioMismatchClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kSmioMismatchClear.setStatus(
        "current"
    )

adTa5kSmioMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 37)
)
adTa5kSmioMismatch.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kSmioMismatch.setStatus(
        "current"
    )

adTa5kSmBackPlaneRateFallbackClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 38)
)
adTa5kSmBackPlaneRateFallbackClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTa5kSmBackPlaneRateFallbackClear.setStatus(
        "current"
    )

adTa5kSmBackPlaneRateFallback = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 39)
)
adTa5kSmBackPlaneRateFallback.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTa5kSmBackPlaneRateFallback.setStatus(
        "current"
    )

adTa5kSmPeerLinkDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 40)
)
adTa5kSmPeerLinkDownClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    adTa5kSmPeerLinkDownClear.setStatus(
        "current"
    )

adTa5kSmPeerLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 41)
)
adTa5kSmPeerLinkDown.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    adTa5kSmPeerLinkDown.setStatus(
        "current"
    )

adTa5kSmBackPlaneIncompatibleClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 42)
)
adTa5kSmBackPlaneIncompatibleClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kSmBackPlaneIncompatibleClear.setStatus(
        "current"
    )

adTa5kSmBackPlaneIncompatibleActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 750, 0, 43)
)
adTa5kSmBackPlaneIncompatibleActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kSmBackPlaneIncompatibleActive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TA5K-SM-MIB",
    **{"EthernetDefaultInterfaceType": EthernetDefaultInterfaceType,
       "adTa5kSmTraps": adTa5kSmTraps,
       "adTa5kSmAlarms": adTa5kSmAlarms,
       "adTa5kSmTimingSrcClear": adTa5kSmTimingSrcClear,
       "adTa5kSmTimingSrcFail": adTa5kSmTimingSrcFail,
       "adTa5kSmRingGenClear": adTa5kSmRingGenClear,
       "adTa5kSmRingGenFail": adTa5kSmRingGenFail,
       "adTa5kSmPowerLimitAlmClear": adTa5kSmPowerLimitAlmClear,
       "adTa5kSmPowerLimitExceeded": adTa5kSmPowerLimitExceeded,
       "adTa5kSmUnknownSfpClear": adTa5kSmUnknownSfpClear,
       "adTa5kSmUnknownSfpAlarm": adTa5kSmUnknownSfpAlarm,
       "adTa5kSmSfpFaultClear": adTa5kSmSfpFaultClear,
       "adTa5kSmSfpFaultActive": adTa5kSmSfpFaultActive,
       "adTa5kSmMultipleUplinksClear": adTa5kSmMultipleUplinksClear,
       "adTa5kSmMultipleUplinksDetected": adTa5kSmMultipleUplinksDetected,
       "adTa5kSmExtAFailureClear": adTa5kSmExtAFailureClear,
       "adTa5kSmExtAFailureActive": adTa5kSmExtAFailureActive,
       "adTa5kSmExtBFailureClear": adTa5kSmExtBFailureClear,
       "adTa5kSmExtBFailureActive": adTa5kSmExtBFailureActive,
       "adTa5kSmLossOfHeartbeatClear": adTa5kSmLossOfHeartbeatClear,
       "adTa5kSmLossOfHeartbeatActive": adTa5kSmLossOfHeartbeatActive,
       "adTa5kSmLossOfNetworkStpClear": adTa5kSmLossOfNetworkStpClear,
       "adTa5kSmLossOfNetworkStpActive": adTa5kSmLossOfNetworkStpActive,
       "adTa5kSmDuplicateNodeClear": adTa5kSmDuplicateNodeClear,
       "adTa5kSmDuplicateNodeActive": adTa5kSmDuplicateNodeActive,
       "adTa5kSmDuplicateScmIpClear": adTa5kSmDuplicateScmIpClear,
       "adTa5kSmDuplicateScmIpActive": adTa5kSmDuplicateScmIpActive,
       "adTa5kSmBandwidthFullClear": adTa5kSmBandwidthFullClear,
       "adTa5kSmBandwidthFull": adTa5kSmBandwidthFull,
       "adTa5kSmPriTimingSrcClear": adTa5kSmPriTimingSrcClear,
       "adTa5kSmPriTimingSrcFail": adTa5kSmPriTimingSrcFail,
       "adTa5kSmSecTimingSrcClear": adTa5kSmSecTimingSrcClear,
       "adTa5kSmSecTimingSrcFail": adTa5kSmSecTimingSrcFail,
       "adTa5kSmNodeNumberProvClear": adTa5kSmNodeNumberProvClear,
       "adTa5kSmNodeNumberDefault": adTa5kSmNodeNumberDefault,
       "adTa5kSmMgmtVlanFailClear": adTa5kSmMgmtVlanFailClear,
       "adTa5kSmMgmtVlanFail": adTa5kSmMgmtVlanFail,
       "adTa5kSmioMismatchClear": adTa5kSmioMismatchClear,
       "adTa5kSmioMismatch": adTa5kSmioMismatch,
       "adTa5kSmBackPlaneRateFallbackClear": adTa5kSmBackPlaneRateFallbackClear,
       "adTa5kSmBackPlaneRateFallback": adTa5kSmBackPlaneRateFallback,
       "adTa5kSmPeerLinkDownClear": adTa5kSmPeerLinkDownClear,
       "adTa5kSmPeerLinkDown": adTa5kSmPeerLinkDown,
       "adTa5kSmBackPlaneIncompatibleClear": adTa5kSmBackPlaneIncompatibleClear,
       "adTa5kSmBackPlaneIncompatibleActive": adTa5kSmBackPlaneIncompatibleActive,
       "adTa5kSm": adTa5kSm,
       "adTa5kSmConfig": adTa5kSmConfig,
       "adTa5kSmSystemTable": adTa5kSmSystemTable,
       "adTa5kSmSystemEntry": adTa5kSmSystemEntry,
       "adTa5kSmMaxNodes": adTa5kSmMaxNodes,
       "adTa5kSmMaxShelves": adTa5kSmMaxShelves,
       "adTa5kSmBootRev": adTa5kSmBootRev,
       "adTa5kSmNet1SFPDescription": adTa5kSmNet1SFPDescription,
       "adTa5kSmNet2SFPDescription": adTa5kSmNet2SFPDescription,
       "adTa5kSmRingGenType": adTa5kSmRingGenType,
       "adTa5kSmSMIOType": adTa5kSmSMIOType,
       "adTa5kSmNet1AutoNegoAdmnStat": adTa5kSmNet1AutoNegoAdmnStat,
       "adTa5kSmNet2AutoNegoAdmnStat": adTa5kSmNet2AutoNegoAdmnStat,
       "adTa5kSmNet1SFPVendorPartNumber": adTa5kSmNet1SFPVendorPartNumber,
       "adTa5kSmNet1SFPVendorSerialNumber": adTa5kSmNet1SFPVendorSerialNumber,
       "adTa5kSmNet1SFPRxPowerLevel": adTa5kSmNet1SFPRxPowerLevel,
       "adTa5kSmNet1SFPTxPowerLevel": adTa5kSmNet1SFPTxPowerLevel,
       "adTa5kSmNet1SFPTxBias": adTa5kSmNet1SFPTxBias,
       "adTa5kSmNet1SFPTemperature": adTa5kSmNet1SFPTemperature,
       "adTa5kSmNet1SFPSupplyVoltage": adTa5kSmNet1SFPSupplyVoltage,
       "adTa5kSmNet2SFPVendorPartNumber": adTa5kSmNet2SFPVendorPartNumber,
       "adTa5kSmNet2SFPVendorSerialNumber": adTa5kSmNet2SFPVendorSerialNumber,
       "adTa5kSmNet2SFPRxPowerLevel": adTa5kSmNet2SFPRxPowerLevel,
       "adTa5kSmNet2SFPTxPowerLevel": adTa5kSmNet2SFPTxPowerLevel,
       "adTa5kSmNet2SFPTxBias": adTa5kSmNet2SFPTxBias,
       "adTa5kSmNet2SFPTemperature": adTa5kSmNet2SFPTemperature,
       "adTa5kSmNet2SFPSupplyVoltage": adTa5kSmNet2SFPSupplyVoltage,
       "adTa5kSmProv": adTa5kSmProv,
       "adTa5kSmProvTable": adTa5kSmProvTable,
       "adTa5kSmProvEntry": adTa5kSmProvEntry,
       "adTa5kSmNode": adTa5kSmNode,
       "adTa5kSmUplink": adTa5kSmUplink,
       "adTa5kSmAggregation": adTa5kSmAggregation,
       "adTa5kSmPrimaryClock": adTa5kSmPrimaryClock,
       "adTa5kSmSecondaryClock": adTa5kSmSecondaryClock,
       "adTa5kSmCurrentClock": adTa5kSmCurrentClock,
       "adTa5kSmClockModeRevertive": adTa5kSmClockModeRevertive,
       "adTa5kSmForceClockFailover": adTa5kSmForceClockFailover,
       "adTa5kSmNetworkName": adTa5kSmNetworkName,
       "adTa5kSmTopologyChangeCount": adTa5kSmTopologyChangeCount,
       "adTa5kSmTopologyInstance": adTa5kSmTopologyInstance,
       "adTa5kSmLoopASource": adTa5kSmLoopASource,
       "adTa5kSmLoopBSource": adTa5kSmLoopBSource,
       "adTa5kSmExtAType": adTa5kSmExtAType,
       "adTa5kSmExtBType": adTa5kSmExtBType,
       "adTa5kSmUpstreamChaining": adTa5kSmUpstreamChaining,
       "adTa5kSmDownstreamChaining": adTa5kSmDownstreamChaining,
       "adTa5kSmFallbackClock": adTa5kSmFallbackClock,
       "adTa5kSmExtAQuality": adTa5kSmExtAQuality,
       "adTa5kSmExtBQuality": adTa5kSmExtBQuality,
       "adTa5kSmExtAPreference": adTa5kSmExtAPreference,
       "adTa5kSmExtBPreference": adTa5kSmExtBPreference,
       "adTa5kSmUseHopCount": adTa5kSmUseHopCount,
       "adTa5kSmIGMPInterfaceMode": adTa5kSmIGMPInterfaceMode,
       "adTa5kSmSTagTPID": adTa5kSmSTagTPID,
       "adTa5kSmExtAPriority": adTa5kSmExtAPriority,
       "adTa5kSmExtBPriority": adTa5kSmExtBPriority,
       "adTa5kSmInternalSTag": adTa5kSmInternalSTag,
       "adTa5kSmBpRateAlarmSeverityLevel": adTa5kSmBpRateAlarmSeverityLevel,
       "adTa5kSmNetworkPortProvTable": adTa5kSmNetworkPortProvTable,
       "adTa5kSmNetworkPortProvEntry": adTa5kSmNetworkPortProvEntry,
       "adTa5kSmPortMode": adTa5kSmPortMode,
       "adTa5kSmLACPMode": adTa5kSmLACPMode,
       "adTa5kSmEthernetDefaultInterface": adTa5kSmEthernetDefaultInterface,
       "adTa5kSmEthDefaultInterfaceIndex": adTa5kSmEthDefaultInterfaceIndex,
       "adTa5kSmEthernetDefaultIfcType": adTa5kSmEthernetDefaultIfcType,
       "adTa5kSmEthernetDefaultIfcSlot": adTa5kSmEthernetDefaultIfcSlot,
       "adTa5kSmEthernetDefaultIfcPort": adTa5kSmEthernetDefaultIfcPort,
       "adTa5kSmAlarmProvTable": adTa5kSmAlarmProvTable,
       "adTa5kSmAlarmProvEntry": adTa5kSmAlarmProvEntry,
       "adTa5kSmRingGenFailAlarmEnable": adTa5kSmRingGenFailAlarmEnable,
       "adTa5kSmPowerLimitExceededAlarmEnable": adTa5kSmPowerLimitExceededAlarmEnable,
       "adTa5kSmDuplicateNodeAlarmEnable": adTa5kSmDuplicateNodeAlarmEnable,
       "adTa5kSmDuplicateScmIpAlarmEnable": adTa5kSmDuplicateScmIpAlarmEnable,
       "adTa5kSmNodeNumberProvAlarmEnable": adTa5kSmNodeNumberProvAlarmEnable,
       "adTa5kSmMgmtVlanFailAlarmEnable": adTa5kSmMgmtVlanFailAlarmEnable,
       "adTa5kSmioMismatchAlarmEnable": adTa5kSmioMismatchAlarmEnable,
       "adTa5kSmBPRateFallbackAlarmEnable": adTa5kSmBPRateFallbackAlarmEnable,
       "adTa5kSmPeerLinksDownAlarmEnable": adTa5kSmPeerLinksDownAlarmEnable,
       "adTa5kSmStatus": adTa5kSmStatus,
       "adTa5kSmClockStatusTable": adTa5kSmClockStatusTable,
       "adTa5kSmClockStatusEntry": adTa5kSmClockStatusEntry,
       "adTa5kSmLoopAClockHealth": adTa5kSmLoopAClockHealth,
       "adTa5kSmLoopBClockHealth": adTa5kSmLoopBClockHealth,
       "adTa5kSmBitsAClockHealth": adTa5kSmBitsAClockHealth,
       "adTa5kSmBitsBClockHealth": adTa5kSmBitsBClockHealth,
       "adTa5kSmPrimaryClockHealth": adTa5kSmPrimaryClockHealth,
       "adTa5kSmSecondaryClockHealth": adTa5kSmSecondaryClockHealth,
       "adTa5kSmRingVoltagePresent": adTa5kSmRingVoltagePresent,
       "adTa5kSmRingFail": adTa5kSmRingFail,
       "adTa5kSmPeerRingFail": adTa5kSmPeerRingFail,
       "adTa5kSmCurrentHopCount": adTa5kSmCurrentHopCount,
       "adTa5kSmCurrentTimingSourcePriority": adTa5kSmCurrentTimingSourcePriority,
       "adTa5kSmCurrentTimingSourceQuality": adTa5kSmCurrentTimingSourceQuality,
       "adTa5kSmTest": adTa5kSmTest,
       "adTa5kSmMetalicTestAccessTable": adTa5kSmMetalicTestAccessTable,
       "adTa5kSmMetalicTestAccessEntry": adTa5kSmMetalicTestAccessEntry,
       "adTa5kSmFacilityTR": adTa5kSmFacilityTR,
       "adTa5kSmFacilityT1R1": adTa5kSmFacilityT1R1,
       "adTa5kSmEquipmentTR": adTa5kSmEquipmentTR,
       "adTa5kSmEquipmentT1R1": adTa5kSmEquipmentT1R1,
       "adTa5kSmLoopTR": adTa5kSmLoopTR,
       "adTa5kSmLoopT1R1": adTa5kSmLoopT1R1,
       "adTa5kSmPerfMon": adTa5kSmPerfMon,
       "adTa5kSmAtpMfg": adTa5kSmAtpMfg,
       "adTa5kSmAtpTable": adTa5kSmAtpTable,
       "adTa5kSmAtpEntry": adTa5kSmAtpEntry,
       "adTa5kSmTemp1": adTa5kSmTemp1,
       "adTa5kSmTemp2": adTa5kSmTemp2,
       "adTa5kSmExpMac": adTa5kSmExpMac,
       "adTa5kSmPeerMac": adTa5kSmPeerMac,
       "adTa5kSmModuleIdentity": adTa5kSmModuleIdentity}
)
