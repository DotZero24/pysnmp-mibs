# SNMP MIB module (ELTEX-MES-HARDWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-HARDWARE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:49:41 2025
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

(eltMes,
 eltMesHardwareMib) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes",
    "eltMesHardwareMib")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class EltHardwareLedUnitIdModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stack", 1),
          ("poe", 2))
    )



class EltBreakoutMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("mode-4x10", 2))
    )



# MIB Managed Objects in the order of their OIDs

_EltMesHardwareMibMIBObjects_ObjectIdentity = ObjectIdentity
eltMesHardwareMibMIBObjects = _EltMesHardwareMibMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1)
)
_EltMesHardwareConfig_ObjectIdentity = ObjectIdentity
eltMesHardwareConfig = _EltMesHardwareConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1)
)
_EltMesHardwareSerdesConfig_ObjectIdentity = ObjectIdentity
eltMesHardwareSerdesConfig = _EltMesHardwareSerdesConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1)
)
_EltHardwareSerdesRxConfigTable_Object = MibTable
eltHardwareSerdesRxConfigTable = _EltHardwareSerdesRxConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltHardwareSerdesRxConfigTable.setStatus("current")
_EltHardwareSerdesRxConfigEntry_Object = MibTableRow
eltHardwareSerdesRxConfigEntry = _EltHardwareSerdesRxConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 1, 1)
)
eltHardwareSerdesRxConfigEntry.setIndexNames(
    (0, "ELTEX-MES-HARDWARE-MIB", "eltHardwareSerdesRxConfigIfIndex"),
    (0, "ELTEX-MES-HARDWARE-MIB", "eltHardwareSerdesRxConfigLaneNumber"),
)
if mibBuilder.loadTexts:
    eltHardwareSerdesRxConfigEntry.setStatus("current")
_EltHardwareSerdesRxConfigIfIndex_Type = Integer32
_EltHardwareSerdesRxConfigIfIndex_Object = MibTableColumn
eltHardwareSerdesRxConfigIfIndex = _EltHardwareSerdesRxConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 1, 1, 1),
    _EltHardwareSerdesRxConfigIfIndex_Type()
)
eltHardwareSerdesRxConfigIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltHardwareSerdesRxConfigIfIndex.setStatus("current")
_EltHardwareSerdesRxConfigLaneNumber_Type = Integer32
_EltHardwareSerdesRxConfigLaneNumber_Object = MibTableColumn
eltHardwareSerdesRxConfigLaneNumber = _EltHardwareSerdesRxConfigLaneNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 1, 1, 2),
    _EltHardwareSerdesRxConfigLaneNumber_Type()
)
eltHardwareSerdesRxConfigLaneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltHardwareSerdesRxConfigLaneNumber.setStatus("current")


class _EltHardwareSerdesRxConfigUserParamsEnable_Type(TruthValue):
    """Custom type eltHardwareSerdesRxConfigUserParamsEnable based on TruthValue"""
    defaultValue = 2


_EltHardwareSerdesRxConfigUserParamsEnable_Type.__name__ = "TruthValue"
_EltHardwareSerdesRxConfigUserParamsEnable_Object = MibTableColumn
eltHardwareSerdesRxConfigUserParamsEnable = _EltHardwareSerdesRxConfigUserParamsEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 1, 1, 3),
    _EltHardwareSerdesRxConfigUserParamsEnable_Type()
)
eltHardwareSerdesRxConfigUserParamsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltHardwareSerdesRxConfigUserParamsEnable.setStatus("current")


class _EltHardwareSerdesRxConfigSquelch_Type(Integer32):
    """Custom type eltHardwareSerdesRxConfigSquelch based on Integer32"""
    defaultValue = 0


_EltHardwareSerdesRxConfigSquelch_Type.__name__ = "Integer32"
_EltHardwareSerdesRxConfigSquelch_Object = MibTableColumn
eltHardwareSerdesRxConfigSquelch = _EltHardwareSerdesRxConfigSquelch_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 1, 1, 4),
    _EltHardwareSerdesRxConfigSquelch_Type()
)
eltHardwareSerdesRxConfigSquelch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltHardwareSerdesRxConfigSquelch.setStatus("current")


class _EltHardwareSerdesRxConfigFFEResistor_Type(Integer32):
    """Custom type eltHardwareSerdesRxConfigFFEResistor based on Integer32"""
    defaultValue = 0


_EltHardwareSerdesRxConfigFFEResistor_Type.__name__ = "Integer32"
_EltHardwareSerdesRxConfigFFEResistor_Object = MibTableColumn
eltHardwareSerdesRxConfigFFEResistor = _EltHardwareSerdesRxConfigFFEResistor_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 1, 1, 5),
    _EltHardwareSerdesRxConfigFFEResistor_Type()
)
eltHardwareSerdesRxConfigFFEResistor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltHardwareSerdesRxConfigFFEResistor.setStatus("current")


class _EltHardwareSerdesRxConfigFFECapacitor_Type(Integer32):
    """Custom type eltHardwareSerdesRxConfigFFECapacitor based on Integer32"""
    defaultValue = 0


_EltHardwareSerdesRxConfigFFECapacitor_Type.__name__ = "Integer32"
_EltHardwareSerdesRxConfigFFECapacitor_Object = MibTableColumn
eltHardwareSerdesRxConfigFFECapacitor = _EltHardwareSerdesRxConfigFFECapacitor_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 1, 1, 6),
    _EltHardwareSerdesRxConfigFFECapacitor_Type()
)
eltHardwareSerdesRxConfigFFECapacitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltHardwareSerdesRxConfigFFECapacitor.setStatus("current")


class _EltHardwareSerdesRxConfigAlign90_Type(Integer32):
    """Custom type eltHardwareSerdesRxConfigAlign90 based on Integer32"""
    defaultValue = 0


_EltHardwareSerdesRxConfigAlign90_Type.__name__ = "Integer32"
_EltHardwareSerdesRxConfigAlign90_Object = MibTableColumn
eltHardwareSerdesRxConfigAlign90 = _EltHardwareSerdesRxConfigAlign90_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 1, 1, 7),
    _EltHardwareSerdesRxConfigAlign90_Type()
)
eltHardwareSerdesRxConfigAlign90.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltHardwareSerdesRxConfigAlign90.setStatus("current")
_EltHardwareSerdesTxConfigTable_Object = MibTable
eltHardwareSerdesTxConfigTable = _EltHardwareSerdesTxConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eltHardwareSerdesTxConfigTable.setStatus("current")
_EltHardwareSerdesTxConfigEntry_Object = MibTableRow
eltHardwareSerdesTxConfigEntry = _EltHardwareSerdesTxConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 2, 1)
)
eltHardwareSerdesTxConfigEntry.setIndexNames(
    (0, "ELTEX-MES-HARDWARE-MIB", "eltHardwareSerdesTxConfigIfIndex"),
    (0, "ELTEX-MES-HARDWARE-MIB", "eltHardwareSerdesTxConfigLaneNumber"),
)
if mibBuilder.loadTexts:
    eltHardwareSerdesTxConfigEntry.setStatus("current")
_EltHardwareSerdesTxConfigIfIndex_Type = Integer32
_EltHardwareSerdesTxConfigIfIndex_Object = MibTableColumn
eltHardwareSerdesTxConfigIfIndex = _EltHardwareSerdesTxConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 2, 1, 1),
    _EltHardwareSerdesTxConfigIfIndex_Type()
)
eltHardwareSerdesTxConfigIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltHardwareSerdesTxConfigIfIndex.setStatus("current")
_EltHardwareSerdesTxConfigLaneNumber_Type = Integer32
_EltHardwareSerdesTxConfigLaneNumber_Object = MibTableColumn
eltHardwareSerdesTxConfigLaneNumber = _EltHardwareSerdesTxConfigLaneNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 2, 1, 2),
    _EltHardwareSerdesTxConfigLaneNumber_Type()
)
eltHardwareSerdesTxConfigLaneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltHardwareSerdesTxConfigLaneNumber.setStatus("current")


class _EltHardwareSerdesTxConfigUserParamsEnable_Type(TruthValue):
    """Custom type eltHardwareSerdesTxConfigUserParamsEnable based on TruthValue"""
    defaultValue = 2


_EltHardwareSerdesTxConfigUserParamsEnable_Type.__name__ = "TruthValue"
_EltHardwareSerdesTxConfigUserParamsEnable_Object = MibTableColumn
eltHardwareSerdesTxConfigUserParamsEnable = _EltHardwareSerdesTxConfigUserParamsEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 2, 1, 3),
    _EltHardwareSerdesTxConfigUserParamsEnable_Type()
)
eltHardwareSerdesTxConfigUserParamsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltHardwareSerdesTxConfigUserParamsEnable.setStatus("current")


class _EltHardwareSerdesTxConfigAmplitude_Type(Integer32):
    """Custom type eltHardwareSerdesTxConfigAmplitude based on Integer32"""
    defaultValue = 0


_EltHardwareSerdesTxConfigAmplitude_Type.__name__ = "Integer32"
_EltHardwareSerdesTxConfigAmplitude_Object = MibTableColumn
eltHardwareSerdesTxConfigAmplitude = _EltHardwareSerdesTxConfigAmplitude_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 2, 1, 4),
    _EltHardwareSerdesTxConfigAmplitude_Type()
)
eltHardwareSerdesTxConfigAmplitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltHardwareSerdesTxConfigAmplitude.setStatus("current")


class _EltHardwareSerdesTxConfigAmplitudeAdjustEnable_Type(TruthValue):
    """Custom type eltHardwareSerdesTxConfigAmplitudeAdjustEnable based on TruthValue"""
    defaultValue = 2


_EltHardwareSerdesTxConfigAmplitudeAdjustEnable_Type.__name__ = "TruthValue"
_EltHardwareSerdesTxConfigAmplitudeAdjustEnable_Object = MibTableColumn
eltHardwareSerdesTxConfigAmplitudeAdjustEnable = _EltHardwareSerdesTxConfigAmplitudeAdjustEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 2, 1, 5),
    _EltHardwareSerdesTxConfigAmplitudeAdjustEnable_Type()
)
eltHardwareSerdesTxConfigAmplitudeAdjustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltHardwareSerdesTxConfigAmplitudeAdjustEnable.setStatus("current")


class _EltHardwareSerdesTxConfigEmphasisAmplitudeGen0_Type(Integer32):
    """Custom type eltHardwareSerdesTxConfigEmphasisAmplitudeGen0 based on Integer32"""
    defaultValue = 0


_EltHardwareSerdesTxConfigEmphasisAmplitudeGen0_Type.__name__ = "Integer32"
_EltHardwareSerdesTxConfigEmphasisAmplitudeGen0_Object = MibTableColumn
eltHardwareSerdesTxConfigEmphasisAmplitudeGen0 = _EltHardwareSerdesTxConfigEmphasisAmplitudeGen0_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 2, 1, 6),
    _EltHardwareSerdesTxConfigEmphasisAmplitudeGen0_Type()
)
eltHardwareSerdesTxConfigEmphasisAmplitudeGen0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltHardwareSerdesTxConfigEmphasisAmplitudeGen0.setStatus("current")


class _EltHardwareSerdesTxConfigEmphasisAmplitudeGen1_Type(Integer32):
    """Custom type eltHardwareSerdesTxConfigEmphasisAmplitudeGen1 based on Integer32"""
    defaultValue = 0


_EltHardwareSerdesTxConfigEmphasisAmplitudeGen1_Type.__name__ = "Integer32"
_EltHardwareSerdesTxConfigEmphasisAmplitudeGen1_Object = MibTableColumn
eltHardwareSerdesTxConfigEmphasisAmplitudeGen1 = _EltHardwareSerdesTxConfigEmphasisAmplitudeGen1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 2, 1, 7),
    _EltHardwareSerdesTxConfigEmphasisAmplitudeGen1_Type()
)
eltHardwareSerdesTxConfigEmphasisAmplitudeGen1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltHardwareSerdesTxConfigEmphasisAmplitudeGen1.setStatus("current")


class _EltHardwareSerdesTxConfigAmplitudeShiftEnable_Type(TruthValue):
    """Custom type eltHardwareSerdesTxConfigAmplitudeShiftEnable based on TruthValue"""
    defaultValue = 2


_EltHardwareSerdesTxConfigAmplitudeShiftEnable_Type.__name__ = "TruthValue"
_EltHardwareSerdesTxConfigAmplitudeShiftEnable_Object = MibTableColumn
eltHardwareSerdesTxConfigAmplitudeShiftEnable = _EltHardwareSerdesTxConfigAmplitudeShiftEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 2, 1, 8),
    _EltHardwareSerdesTxConfigAmplitudeShiftEnable_Type()
)
eltHardwareSerdesTxConfigAmplitudeShiftEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltHardwareSerdesTxConfigAmplitudeShiftEnable.setStatus("current")
_EltHardwareInterfaceTable_Object = MibTable
eltHardwareInterfaceTable = _EltHardwareInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    eltHardwareInterfaceTable.setStatus("current")
_EltHardwareInterfaceEntry_Object = MibTableRow
eltHardwareInterfaceEntry = _EltHardwareInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 3, 1)
)
eltHardwareInterfaceEntry.setIndexNames(
    (0, "ELTEX-MES-HARDWARE-MIB", "eltHardwareInterfaceIndex"),
)
if mibBuilder.loadTexts:
    eltHardwareInterfaceEntry.setStatus("current")
_EltHardwareInterfaceIndex_Type = InterfaceIndex
_EltHardwareInterfaceIndex_Object = MibTableColumn
eltHardwareInterfaceIndex = _EltHardwareInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 3, 1, 1),
    _EltHardwareInterfaceIndex_Type()
)
eltHardwareInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltHardwareInterfaceIndex.setStatus("current")
_EltHardwareInterfaceBreakoutModeAfterReset_Type = EltBreakoutMode
_EltHardwareInterfaceBreakoutModeAfterReset_Object = MibTableColumn
eltHardwareInterfaceBreakoutModeAfterReset = _EltHardwareInterfaceBreakoutModeAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 3, 1, 2),
    _EltHardwareInterfaceBreakoutModeAfterReset_Type()
)
eltHardwareInterfaceBreakoutModeAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltHardwareInterfaceBreakoutModeAfterReset.setStatus("current")
_EltHardwareInterfaceBreakoutMode_Type = EltBreakoutMode
_EltHardwareInterfaceBreakoutMode_Object = MibTableColumn
eltHardwareInterfaceBreakoutMode = _EltHardwareInterfaceBreakoutMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 3, 1, 3),
    _EltHardwareInterfaceBreakoutMode_Type()
)
eltHardwareInterfaceBreakoutMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltHardwareInterfaceBreakoutMode.setStatus("current")
_EltHardwareInterfaceBreakoutPortList_Type = PortList
_EltHardwareInterfaceBreakoutPortList_Object = MibTableColumn
eltHardwareInterfaceBreakoutPortList = _EltHardwareInterfaceBreakoutPortList_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 1, 3, 1, 4),
    _EltHardwareInterfaceBreakoutPortList_Type()
)
eltHardwareInterfaceBreakoutPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltHardwareInterfaceBreakoutPortList.setStatus("current")
_EltMesHardwareLedConfig_ObjectIdentity = ObjectIdentity
eltMesHardwareLedConfig = _EltMesHardwareLedConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 2)
)


class _EltHardwareLedConfigUnitIdMode_Type(EltHardwareLedUnitIdModeType):
    """Custom type eltHardwareLedConfigUnitIdMode based on EltHardwareLedUnitIdModeType"""
    defaultValue = 1


_EltHardwareLedConfigUnitIdMode_Type.__name__ = "EltHardwareLedUnitIdModeType"
_EltHardwareLedConfigUnitIdMode_Object = MibScalar
eltHardwareLedConfigUnitIdMode = _EltHardwareLedConfigUnitIdMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 1, 2, 1),
    _EltHardwareLedConfigUnitIdMode_Type()
)
eltHardwareLedConfigUnitIdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltHardwareLedConfigUnitIdMode.setStatus("current")
_EltMesHardwareStatus_ObjectIdentity = ObjectIdentity
eltMesHardwareStatus = _EltMesHardwareStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 2)
)
_EltMesHardwareSerdesStatus_ObjectIdentity = ObjectIdentity
eltMesHardwareSerdesStatus = _EltMesHardwareSerdesStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 14, 1, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-HARDWARE-MIB",
    **{"EltHardwareLedUnitIdModeType": EltHardwareLedUnitIdModeType,
       "EltBreakoutMode": EltBreakoutMode,
       "eltMesHardwareMibMIBObjects": eltMesHardwareMibMIBObjects,
       "eltMesHardwareConfig": eltMesHardwareConfig,
       "eltMesHardwareSerdesConfig": eltMesHardwareSerdesConfig,
       "eltHardwareSerdesRxConfigTable": eltHardwareSerdesRxConfigTable,
       "eltHardwareSerdesRxConfigEntry": eltHardwareSerdesRxConfigEntry,
       "eltHardwareSerdesRxConfigIfIndex": eltHardwareSerdesRxConfigIfIndex,
       "eltHardwareSerdesRxConfigLaneNumber": eltHardwareSerdesRxConfigLaneNumber,
       "eltHardwareSerdesRxConfigUserParamsEnable": eltHardwareSerdesRxConfigUserParamsEnable,
       "eltHardwareSerdesRxConfigSquelch": eltHardwareSerdesRxConfigSquelch,
       "eltHardwareSerdesRxConfigFFEResistor": eltHardwareSerdesRxConfigFFEResistor,
       "eltHardwareSerdesRxConfigFFECapacitor": eltHardwareSerdesRxConfigFFECapacitor,
       "eltHardwareSerdesRxConfigAlign90": eltHardwareSerdesRxConfigAlign90,
       "eltHardwareSerdesTxConfigTable": eltHardwareSerdesTxConfigTable,
       "eltHardwareSerdesTxConfigEntry": eltHardwareSerdesTxConfigEntry,
       "eltHardwareSerdesTxConfigIfIndex": eltHardwareSerdesTxConfigIfIndex,
       "eltHardwareSerdesTxConfigLaneNumber": eltHardwareSerdesTxConfigLaneNumber,
       "eltHardwareSerdesTxConfigUserParamsEnable": eltHardwareSerdesTxConfigUserParamsEnable,
       "eltHardwareSerdesTxConfigAmplitude": eltHardwareSerdesTxConfigAmplitude,
       "eltHardwareSerdesTxConfigAmplitudeAdjustEnable": eltHardwareSerdesTxConfigAmplitudeAdjustEnable,
       "eltHardwareSerdesTxConfigEmphasisAmplitudeGen0": eltHardwareSerdesTxConfigEmphasisAmplitudeGen0,
       "eltHardwareSerdesTxConfigEmphasisAmplitudeGen1": eltHardwareSerdesTxConfigEmphasisAmplitudeGen1,
       "eltHardwareSerdesTxConfigAmplitudeShiftEnable": eltHardwareSerdesTxConfigAmplitudeShiftEnable,
       "eltHardwareInterfaceTable": eltHardwareInterfaceTable,
       "eltHardwareInterfaceEntry": eltHardwareInterfaceEntry,
       "eltHardwareInterfaceIndex": eltHardwareInterfaceIndex,
       "eltHardwareInterfaceBreakoutModeAfterReset": eltHardwareInterfaceBreakoutModeAfterReset,
       "eltHardwareInterfaceBreakoutMode": eltHardwareInterfaceBreakoutMode,
       "eltHardwareInterfaceBreakoutPortList": eltHardwareInterfaceBreakoutPortList,
       "eltMesHardwareLedConfig": eltMesHardwareLedConfig,
       "eltHardwareLedConfigUnitIdMode": eltHardwareLedConfigUnitIdMode,
       "eltMesHardwareStatus": eltMesHardwareStatus,
       "eltMesHardwareSerdesStatus": eltMesHardwareSerdesStatus}
)
