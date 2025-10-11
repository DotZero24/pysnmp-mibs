# SNMP MIB module (CPDU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/apc/CPDU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:55 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Apc_ObjectIdentity = ObjectIdentity
apc = _Apc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 1)
)
_CPDU_ObjectIdentity = ObjectIdentity
cPDU = _CPDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32)
)
_PduNamePlate_ObjectIdentity = ObjectIdentity
pduNamePlate = _PduNamePlate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 1)
)


class _PduNamePlateTableSize_Type(Integer32):
    """Custom type pduNamePlateTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduNamePlateTableSize_Type.__name__ = "Integer32"
_PduNamePlateTableSize_Object = MibScalar
pduNamePlateTableSize = _PduNamePlateTableSize_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 1, 1),
    _PduNamePlateTableSize_Type()
)
pduNamePlateTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateTableSize.setStatus("current")
_PduNamePlateTable_Object = MibTable
pduNamePlateTable = _PduNamePlateTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 1, 2)
)
if mibBuilder.loadTexts:
    pduNamePlateTable.setStatus("current")
_PduNamePlateEntry_Object = MibTableRow
pduNamePlateEntry = _PduNamePlateEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 1, 2, 1)
)
pduNamePlateEntry.setIndexNames(
    (0, "CPDU-MIB", "pduNamePlateIndex"),
)
if mibBuilder.loadTexts:
    pduNamePlateEntry.setStatus("current")


class _PduNamePlateIndex_Type(Integer32):
    """Custom type pduNamePlateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduNamePlateIndex_Type.__name__ = "Integer32"
_PduNamePlateIndex_Object = MibTableColumn
pduNamePlateIndex = _PduNamePlateIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 1, 2, 1, 1),
    _PduNamePlateIndex_Type()
)
pduNamePlateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduNamePlateIndex.setStatus("current")
_PduNamePlateName_Type = DisplayString
_PduNamePlateName_Object = MibTableColumn
pduNamePlateName = _PduNamePlateName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 1, 2, 1, 2),
    _PduNamePlateName_Type()
)
pduNamePlateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateName.setStatus("current")
_PduNamePlateLocation_Type = DisplayString
_PduNamePlateLocation_Object = MibTableColumn
pduNamePlateLocation = _PduNamePlateLocation_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 1, 2, 1, 3),
    _PduNamePlateLocation_Type()
)
pduNamePlateLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateLocation.setStatus("current")
_PduNamePlateInetAddressType_Type = Integer32
_PduNamePlateInetAddressType_Object = MibTableColumn
pduNamePlateInetAddressType = _PduNamePlateInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 1, 2, 1, 4),
    _PduNamePlateInetAddressType_Type()
)
pduNamePlateInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateInetAddressType.setStatus("current")
_PduNamePlateIPAddress_Type = InetAddress
_PduNamePlateIPAddress_Object = MibTableColumn
pduNamePlateIPAddress = _PduNamePlateIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 1, 2, 1, 5),
    _PduNamePlateIPAddress_Type()
)
pduNamePlateIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateIPAddress.setStatus("current")
_PduNamePlateInetNetMask_Type = InetAddress
_PduNamePlateInetNetMask_Object = MibTableColumn
pduNamePlateInetNetMask = _PduNamePlateInetNetMask_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 1, 2, 1, 6),
    _PduNamePlateInetNetMask_Type()
)
pduNamePlateInetNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateInetNetMask.setStatus("current")
_PduNamePlateInetGateway_Type = InetAddress
_PduNamePlateInetGateway_Object = MibTableColumn
pduNamePlateInetGateway = _PduNamePlateInetGateway_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 1, 2, 1, 7),
    _PduNamePlateInetGateway_Type()
)
pduNamePlateInetGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateInetGateway.setStatus("current")
_PduNamePlateMACAddress_Type = MacAddress
_PduNamePlateMACAddress_Object = MibTableColumn
pduNamePlateMACAddress = _PduNamePlateMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 1, 2, 1, 8),
    _PduNamePlateMACAddress_Type()
)
pduNamePlateMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateMACAddress.setStatus("current")
_PduNamePlateUTCTimeOffset_Type = DisplayString
_PduNamePlateUTCTimeOffset_Object = MibTableColumn
pduNamePlateUTCTimeOffset = _PduNamePlateUTCTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 1, 2, 1, 9),
    _PduNamePlateUTCTimeOffset_Type()
)
pduNamePlateUTCTimeOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateUTCTimeOffset.setStatus("current")
_PduNamePlateModelNumber_Type = DisplayString
_PduNamePlateModelNumber_Object = MibTableColumn
pduNamePlateModelNumber = _PduNamePlateModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 1, 2, 1, 10),
    _PduNamePlateModelNumber_Type()
)
pduNamePlateModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateModelNumber.setStatus("current")
_PduNamePlatePartNumber_Type = DisplayString
_PduNamePlatePartNumber_Object = MibTableColumn
pduNamePlatePartNumber = _PduNamePlatePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 1, 2, 1, 11),
    _PduNamePlatePartNumber_Type()
)
pduNamePlatePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlatePartNumber.setStatus("current")
_PduNamePlateSerialNumber_Type = DisplayString
_PduNamePlateSerialNumber_Object = MibTableColumn
pduNamePlateSerialNumber = _PduNamePlateSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 1, 2, 1, 12),
    _PduNamePlateSerialNumber_Type()
)
pduNamePlateSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateSerialNumber.setStatus("current")
_PduNamePlateDateofManufacture_Type = DisplayString
_PduNamePlateDateofManufacture_Object = MibTableColumn
pduNamePlateDateofManufacture = _PduNamePlateDateofManufacture_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 1, 2, 1, 13),
    _PduNamePlateDateofManufacture_Type()
)
pduNamePlateDateofManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateDateofManufacture.setStatus("current")
_PduNamePlateFirmwareVersion_Type = DisplayString
_PduNamePlateFirmwareVersion_Object = MibTableColumn
pduNamePlateFirmwareVersion = _PduNamePlateFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 1, 2, 1, 14),
    _PduNamePlateFirmwareVersion_Type()
)
pduNamePlateFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateFirmwareVersion.setStatus("current")
_PduNamePlateFirmwareVersionTimeStamp_Type = DisplayString
_PduNamePlateFirmwareVersionTimeStamp_Object = MibTableColumn
pduNamePlateFirmwareVersionTimeStamp = _PduNamePlateFirmwareVersionTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 1, 2, 1, 15),
    _PduNamePlateFirmwareVersionTimeStamp_Type()
)
pduNamePlateFirmwareVersionTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateFirmwareVersionTimeStamp.setStatus("current")


class _PduNamePlateType_Type(Integer32):
    """Custom type pduNamePlateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("singlePhase", 1),
          ("delta", 2),
          ("wye", 3))
    )


_PduNamePlateType_Type.__name__ = "Integer32"
_PduNamePlateType_Object = MibTableColumn
pduNamePlateType = _PduNamePlateType_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 1, 2, 1, 16),
    _PduNamePlateType_Type()
)
pduNamePlateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateType.setStatus("current")
_PduUnit_ObjectIdentity = ObjectIdentity
pduUnit = _PduUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2)
)


class _PduUnitTableSize_Type(Integer32):
    """Custom type pduUnitTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduUnitTableSize_Type.__name__ = "Integer32"
_PduUnitTableSize_Object = MibScalar
pduUnitTableSize = _PduUnitTableSize_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 1),
    _PduUnitTableSize_Type()
)
pduUnitTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitTableSize.setStatus("current")
_PduUnitConfigTable_Object = MibTable
pduUnitConfigTable = _PduUnitConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2)
)
if mibBuilder.loadTexts:
    pduUnitConfigTable.setStatus("current")
_PduUnitConfigEntry_Object = MibTableRow
pduUnitConfigEntry = _PduUnitConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1)
)
pduUnitConfigEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitConfigIndex"),
)
if mibBuilder.loadTexts:
    pduUnitConfigEntry.setStatus("current")


class _PduUnitConfigIndex_Type(Integer32):
    """Custom type pduUnitConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduUnitConfigIndex_Type.__name__ = "Integer32"
_PduUnitConfigIndex_Object = MibTableColumn
pduUnitConfigIndex = _PduUnitConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1, 1),
    _PduUnitConfigIndex_Type()
)
pduUnitConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduUnitConfigIndex.setStatus("current")
_PduUnitConfigName_Type = DisplayString
_PduUnitConfigName_Object = MibTableColumn
pduUnitConfigName = _PduUnitConfigName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1, 2),
    _PduUnitConfigName_Type()
)
pduUnitConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigName.setStatus("current")
_PduUnitConfigLocation_Type = DisplayString
_PduUnitConfigLocation_Object = MibTableColumn
pduUnitConfigLocation = _PduUnitConfigLocation_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1, 3),
    _PduUnitConfigLocation_Type()
)
pduUnitConfigLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigLocation.setStatus("current")


class _PduUnitConfigDisplayOrientation_Type(Integer32):
    """Custom type pduUnitConfigDisplayOrientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("displayNormal", 1),
          ("displayReverse", 2))
    )


_PduUnitConfigDisplayOrientation_Type.__name__ = "Integer32"
_PduUnitConfigDisplayOrientation_Object = MibTableColumn
pduUnitConfigDisplayOrientation = _PduUnitConfigDisplayOrientation_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1, 4),
    _PduUnitConfigDisplayOrientation_Type()
)
pduUnitConfigDisplayOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigDisplayOrientation.setStatus("current")


class _PduUnitConfigOledDisplayControl_Type(Integer32):
    """Custom type pduUnitConfigOledDisplayControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("displayOff", 1),
          ("displayOn", 2))
    )


_PduUnitConfigOledDisplayControl_Type.__name__ = "Integer32"
_PduUnitConfigOledDisplayControl_Object = MibTableColumn
pduUnitConfigOledDisplayControl = _PduUnitConfigOledDisplayControl_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1, 5),
    _PduUnitConfigOledDisplayControl_Type()
)
pduUnitConfigOledDisplayControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigOledDisplayControl.setStatus("current")


class _PduUnitConfigColdstartDelay_Type(Unsigned32):
    """Custom type pduUnitConfigColdstartDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_PduUnitConfigColdstartDelay_Type.__name__ = "Unsigned32"
_PduUnitConfigColdstartDelay_Object = MibTableColumn
pduUnitConfigColdstartDelay = _PduUnitConfigColdstartDelay_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1, 6),
    _PduUnitConfigColdstartDelay_Type()
)
pduUnitConfigColdstartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigColdstartDelay.setStatus("current")


class _PduUnitConfigGlobalOutletStateOnStartup_Type(Integer32):
    """Custom type pduUnitConfigGlobalOutletStateOnStartup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("lastKnownState", 2))
    )


_PduUnitConfigGlobalOutletStateOnStartup_Type.__name__ = "Integer32"
_PduUnitConfigGlobalOutletStateOnStartup_Object = MibTableColumn
pduUnitConfigGlobalOutletStateOnStartup = _PduUnitConfigGlobalOutletStateOnStartup_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1, 7),
    _PduUnitConfigGlobalOutletStateOnStartup_Type()
)
pduUnitConfigGlobalOutletStateOnStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigGlobalOutletStateOnStartup.setStatus("current")
_PduUnitConfigLowerCriticalThreshold_Type = Unsigned32
_PduUnitConfigLowerCriticalThreshold_Object = MibTableColumn
pduUnitConfigLowerCriticalThreshold = _PduUnitConfigLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1, 8),
    _PduUnitConfigLowerCriticalThreshold_Type()
)
pduUnitConfigLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigLowerCriticalThreshold.setStatus("current")
_PduUnitConfigLowerWarningThreshold_Type = Unsigned32
_PduUnitConfigLowerWarningThreshold_Object = MibTableColumn
pduUnitConfigLowerWarningThreshold = _PduUnitConfigLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1, 9),
    _PduUnitConfigLowerWarningThreshold_Type()
)
pduUnitConfigLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigLowerWarningThreshold.setStatus("current")
_PduUnitConfigUpperCriticalThreshold_Type = Unsigned32
_PduUnitConfigUpperCriticalThreshold_Object = MibTableColumn
pduUnitConfigUpperCriticalThreshold = _PduUnitConfigUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1, 10),
    _PduUnitConfigUpperCriticalThreshold_Type()
)
pduUnitConfigUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigUpperCriticalThreshold.setStatus("current")
_PduUnitConfigUpperWarningThreshold_Type = Unsigned32
_PduUnitConfigUpperWarningThreshold_Object = MibTableColumn
pduUnitConfigUpperWarningThreshold = _PduUnitConfigUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1, 11),
    _PduUnitConfigUpperWarningThreshold_Type()
)
pduUnitConfigUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigUpperWarningThreshold.setStatus("current")
_PduUnitConfigAlarmResetThreshold_Type = Unsigned32
_PduUnitConfigAlarmResetThreshold_Object = MibTableColumn
pduUnitConfigAlarmResetThreshold = _PduUnitConfigAlarmResetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1, 12),
    _PduUnitConfigAlarmResetThreshold_Type()
)
pduUnitConfigAlarmResetThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigAlarmResetThreshold.setStatus("current")
_PduUnitConfigAlarmStateChangeDelay_Type = Unsigned32
_PduUnitConfigAlarmStateChangeDelay_Object = MibTableColumn
pduUnitConfigAlarmStateChangeDelay = _PduUnitConfigAlarmStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1, 13),
    _PduUnitConfigAlarmStateChangeDelay_Type()
)
pduUnitConfigAlarmStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigAlarmStateChangeDelay.setStatus("current")


class _PduUnitConfigEnabledThresholds_Type(Bits):
    """Custom type pduUnitConfigEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperWarning", 2),
          ("upperCritical", 3))
    )

_PduUnitConfigEnabledThresholds_Type.__name__ = "Bits"
_PduUnitConfigEnabledThresholds_Object = MibTableColumn
pduUnitConfigEnabledThresholds = _PduUnitConfigEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1, 14),
    _PduUnitConfigEnabledThresholds_Type()
)
pduUnitConfigEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigEnabledThresholds.setStatus("current")


class _PduUnitConfigPeakPowerReset_Type(Integer32):
    """Custom type pduUnitConfigPeakPowerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("reset", 2))
    )


_PduUnitConfigPeakPowerReset_Type.__name__ = "Integer32"
_PduUnitConfigPeakPowerReset_Object = MibTableColumn
pduUnitConfigPeakPowerReset = _PduUnitConfigPeakPowerReset_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1, 15),
    _PduUnitConfigPeakPowerReset_Type()
)
pduUnitConfigPeakPowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigPeakPowerReset.setStatus("current")


class _PduUnitConfigEnergyReset_Type(Integer32):
    """Custom type pduUnitConfigEnergyReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("reset", 2),
          ("notSupported", 3))
    )


_PduUnitConfigEnergyReset_Type.__name__ = "Integer32"
_PduUnitConfigEnergyReset_Object = MibTableColumn
pduUnitConfigEnergyReset = _PduUnitConfigEnergyReset_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1, 16),
    _PduUnitConfigEnergyReset_Type()
)
pduUnitConfigEnergyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigEnergyReset.setStatus("current")


class _PduUnitConfigOutletPeakPowerReset_Type(Integer32):
    """Custom type pduUnitConfigOutletPeakPowerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("reset", 2),
          ("notSupported", 3))
    )


_PduUnitConfigOutletPeakPowerReset_Type.__name__ = "Integer32"
_PduUnitConfigOutletPeakPowerReset_Object = MibTableColumn
pduUnitConfigOutletPeakPowerReset = _PduUnitConfigOutletPeakPowerReset_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1, 17),
    _PduUnitConfigOutletPeakPowerReset_Type()
)
pduUnitConfigOutletPeakPowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigOutletPeakPowerReset.setStatus("current")


class _PduUnitConfigOutletEnergyReset_Type(Integer32):
    """Custom type pduUnitConfigOutletEnergyReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("reset", 2),
          ("notSupported", 3))
    )


_PduUnitConfigOutletEnergyReset_Type.__name__ = "Integer32"
_PduUnitConfigOutletEnergyReset_Object = MibTableColumn
pduUnitConfigOutletEnergyReset = _PduUnitConfigOutletEnergyReset_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1, 18),
    _PduUnitConfigOutletEnergyReset_Type()
)
pduUnitConfigOutletEnergyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigOutletEnergyReset.setStatus("current")


class _PduUnitConfigSsh_Type(Integer32):
    """Custom type pduUnitConfigSsh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_PduUnitConfigSsh_Type.__name__ = "Integer32"
_PduUnitConfigSsh_Object = MibTableColumn
pduUnitConfigSsh = _PduUnitConfigSsh_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1, 19),
    _PduUnitConfigSsh_Type()
)
pduUnitConfigSsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigSsh.setStatus("current")


class _PduUnitConfigResetNetworkManagementCard_Type(Integer32):
    """Custom type pduUnitConfigResetNetworkManagementCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 0),
          ("reset", 1))
    )


_PduUnitConfigResetNetworkManagementCard_Type.__name__ = "Integer32"
_PduUnitConfigResetNetworkManagementCard_Object = MibTableColumn
pduUnitConfigResetNetworkManagementCard = _PduUnitConfigResetNetworkManagementCard_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 2, 1, 20),
    _PduUnitConfigResetNetworkManagementCard_Type()
)
pduUnitConfigResetNetworkManagementCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigResetNetworkManagementCard.setStatus("current")
_PduUnitPropertiesTable_Object = MibTable
pduUnitPropertiesTable = _PduUnitPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 3)
)
if mibBuilder.loadTexts:
    pduUnitPropertiesTable.setStatus("current")
_PduUnitPropertiesEntry_Object = MibTableRow
pduUnitPropertiesEntry = _PduUnitPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 3, 1)
)
pduUnitPropertiesEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitPropertiesIndex"),
)
if mibBuilder.loadTexts:
    pduUnitPropertiesEntry.setStatus("current")


class _PduUnitPropertiesIndex_Type(Integer32):
    """Custom type pduUnitPropertiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduUnitPropertiesIndex_Type.__name__ = "Integer32"
_PduUnitPropertiesIndex_Object = MibTableColumn
pduUnitPropertiesIndex = _PduUnitPropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 3, 1, 1),
    _PduUnitPropertiesIndex_Type()
)
pduUnitPropertiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduUnitPropertiesIndex.setStatus("current")
_PduUnitPropertiesName_Type = DisplayString
_PduUnitPropertiesName_Object = MibTableColumn
pduUnitPropertiesName = _PduUnitPropertiesName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 3, 1, 2),
    _PduUnitPropertiesName_Type()
)
pduUnitPropertiesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesName.setStatus("current")


class _PduUnitPropertiesOutletCount_Type(Integer32):
    """Custom type pduUnitPropertiesOutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduUnitPropertiesOutletCount_Type.__name__ = "Integer32"
_PduUnitPropertiesOutletCount_Object = MibTableColumn
pduUnitPropertiesOutletCount = _PduUnitPropertiesOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 3, 1, 3),
    _PduUnitPropertiesOutletCount_Type()
)
pduUnitPropertiesOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesOutletCount.setStatus("current")


class _PduUnitPropertiesSwitchedOutletCount_Type(Integer32):
    """Custom type pduUnitPropertiesSwitchedOutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduUnitPropertiesSwitchedOutletCount_Type.__name__ = "Integer32"
_PduUnitPropertiesSwitchedOutletCount_Object = MibTableColumn
pduUnitPropertiesSwitchedOutletCount = _PduUnitPropertiesSwitchedOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 3, 1, 4),
    _PduUnitPropertiesSwitchedOutletCount_Type()
)
pduUnitPropertiesSwitchedOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesSwitchedOutletCount.setStatus("current")


class _PduUnitPropertiesMeteredOutletCount_Type(Integer32):
    """Custom type pduUnitPropertiesMeteredOutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduUnitPropertiesMeteredOutletCount_Type.__name__ = "Integer32"
_PduUnitPropertiesMeteredOutletCount_Object = MibTableColumn
pduUnitPropertiesMeteredOutletCount = _PduUnitPropertiesMeteredOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 3, 1, 5),
    _PduUnitPropertiesMeteredOutletCount_Type()
)
pduUnitPropertiesMeteredOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesMeteredOutletCount.setStatus("current")


class _PduUnitPropertiesInputPhaseCount_Type(Integer32):
    """Custom type pduUnitPropertiesInputPhaseCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduUnitPropertiesInputPhaseCount_Type.__name__ = "Integer32"
_PduUnitPropertiesInputPhaseCount_Object = MibTableColumn
pduUnitPropertiesInputPhaseCount = _PduUnitPropertiesInputPhaseCount_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 3, 1, 6),
    _PduUnitPropertiesInputPhaseCount_Type()
)
pduUnitPropertiesInputPhaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesInputPhaseCount.setStatus("current")


class _PduUnitPropertiesCircuitBreakerCount_Type(Integer32):
    """Custom type pduUnitPropertiesCircuitBreakerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduUnitPropertiesCircuitBreakerCount_Type.__name__ = "Integer32"
_PduUnitPropertiesCircuitBreakerCount_Object = MibTableColumn
pduUnitPropertiesCircuitBreakerCount = _PduUnitPropertiesCircuitBreakerCount_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 3, 1, 7),
    _PduUnitPropertiesCircuitBreakerCount_Type()
)
pduUnitPropertiesCircuitBreakerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesCircuitBreakerCount.setStatus("current")


class _PduUnitPropertiesMaxExternalSensorCount_Type(Integer32):
    """Custom type pduUnitPropertiesMaxExternalSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduUnitPropertiesMaxExternalSensorCount_Type.__name__ = "Integer32"
_PduUnitPropertiesMaxExternalSensorCount_Object = MibTableColumn
pduUnitPropertiesMaxExternalSensorCount = _PduUnitPropertiesMaxExternalSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 3, 1, 8),
    _PduUnitPropertiesMaxExternalSensorCount_Type()
)
pduUnitPropertiesMaxExternalSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesMaxExternalSensorCount.setStatus("current")


class _PduUnitPropertiesConnExternalSensorCount_Type(Integer32):
    """Custom type pduUnitPropertiesConnExternalSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduUnitPropertiesConnExternalSensorCount_Type.__name__ = "Integer32"
_PduUnitPropertiesConnExternalSensorCount_Object = MibTableColumn
pduUnitPropertiesConnExternalSensorCount = _PduUnitPropertiesConnExternalSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 3, 1, 9),
    _PduUnitPropertiesConnExternalSensorCount_Type()
)
pduUnitPropertiesConnExternalSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesConnExternalSensorCount.setStatus("current")
_PduUnitPropertiesRatedVoltage_Type = DisplayString
_PduUnitPropertiesRatedVoltage_Object = MibTableColumn
pduUnitPropertiesRatedVoltage = _PduUnitPropertiesRatedVoltage_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 3, 1, 10),
    _PduUnitPropertiesRatedVoltage_Type()
)
pduUnitPropertiesRatedVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesRatedVoltage.setStatus("current")
_PduUnitPropertiesRatedMaxCurrent_Type = DisplayString
_PduUnitPropertiesRatedMaxCurrent_Object = MibTableColumn
pduUnitPropertiesRatedMaxCurrent = _PduUnitPropertiesRatedMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 3, 1, 11),
    _PduUnitPropertiesRatedMaxCurrent_Type()
)
pduUnitPropertiesRatedMaxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesRatedMaxCurrent.setStatus("current")
_PduUnitPropertiesRatedFrequency_Type = DisplayString
_PduUnitPropertiesRatedFrequency_Object = MibTableColumn
pduUnitPropertiesRatedFrequency = _PduUnitPropertiesRatedFrequency_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 3, 1, 12),
    _PduUnitPropertiesRatedFrequency_Type()
)
pduUnitPropertiesRatedFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesRatedFrequency.setStatus("current")
_PduUnitPropertiesRatedPower_Type = DisplayString
_PduUnitPropertiesRatedPower_Object = MibTableColumn
pduUnitPropertiesRatedPower = _PduUnitPropertiesRatedPower_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 3, 1, 13),
    _PduUnitPropertiesRatedPower_Type()
)
pduUnitPropertiesRatedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesRatedPower.setStatus("current")


class _PduUnitPropertiesOrientation_Type(Integer32):
    """Custom type pduUnitPropertiesOrientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("horizontal", 1),
          ("vertical", 2))
    )


_PduUnitPropertiesOrientation_Type.__name__ = "Integer32"
_PduUnitPropertiesOrientation_Object = MibTableColumn
pduUnitPropertiesOrientation = _PduUnitPropertiesOrientation_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 3, 1, 14),
    _PduUnitPropertiesOrientation_Type()
)
pduUnitPropertiesOrientation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesOrientation.setStatus("current")


class _PduUnitPropertiesOutletLayout_Type(Integer32):
    """Custom type pduUnitPropertiesOutletLayout based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("seqPhaseToNuetral", 1),
          ("seqPhaseToPhase", 2),
          ("seqPhToNeu21PhToPh", 3),
          ("seqPhToPhGrouped", 4),
          ("seqPhToNGrouped", 5),
          ("seqPToN1516PToPGrouped", 6),
          ("seqPhToPh2xGrouped", 7),
          ("seqPhToN2xGrouped", 8),
          ("seqNotApplicable", 9))
    )


_PduUnitPropertiesOutletLayout_Type.__name__ = "Integer32"
_PduUnitPropertiesOutletLayout_Object = MibTableColumn
pduUnitPropertiesOutletLayout = _PduUnitPropertiesOutletLayout_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 3, 1, 15),
    _PduUnitPropertiesOutletLayout_Type()
)
pduUnitPropertiesOutletLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesOutletLayout.setStatus("current")


class _PduUnitPropertiesCascadeMemberType_Type(Integer32):
    """Custom type pduUnitPropertiesCascadeMemberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 1),
          ("parent", 2),
          ("child", 3))
    )


_PduUnitPropertiesCascadeMemberType_Type.__name__ = "Integer32"
_PduUnitPropertiesCascadeMemberType_Object = MibTableColumn
pduUnitPropertiesCascadeMemberType = _PduUnitPropertiesCascadeMemberType_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 3, 1, 16),
    _PduUnitPropertiesCascadeMemberType_Type()
)
pduUnitPropertiesCascadeMemberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesCascadeMemberType.setStatus("current")
_PduUnitStatusTable_Object = MibTable
pduUnitStatusTable = _PduUnitStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 4)
)
if mibBuilder.loadTexts:
    pduUnitStatusTable.setStatus("current")
_PduUnitStatusEntry_Object = MibTableRow
pduUnitStatusEntry = _PduUnitStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 4, 1)
)
pduUnitStatusEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitStatusIndex"),
)
if mibBuilder.loadTexts:
    pduUnitStatusEntry.setStatus("current")


class _PduUnitStatusIndex_Type(Integer32):
    """Custom type pduUnitStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduUnitStatusIndex_Type.__name__ = "Integer32"
_PduUnitStatusIndex_Object = MibTableColumn
pduUnitStatusIndex = _PduUnitStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 4, 1, 1),
    _PduUnitStatusIndex_Type()
)
pduUnitStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduUnitStatusIndex.setStatus("current")
_PduUnitStatusName_Type = DisplayString
_PduUnitStatusName_Object = MibTableColumn
pduUnitStatusName = _PduUnitStatusName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 4, 1, 2),
    _PduUnitStatusName_Type()
)
pduUnitStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusName.setStatus("current")


class _PduUnitStatusLoadState_Type(Integer32):
    """Custom type pduUnitStatusLoadState based on Integer32"""
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
        *(("upperCritical", 1),
          ("upperWarning", 2),
          ("lowerWarning", 3),
          ("lowerCritical", 4),
          ("normal", 5))
    )


_PduUnitStatusLoadState_Type.__name__ = "Integer32"
_PduUnitStatusLoadState_Object = MibTableColumn
pduUnitStatusLoadState = _PduUnitStatusLoadState_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 4, 1, 3),
    _PduUnitStatusLoadState_Type()
)
pduUnitStatusLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusLoadState.setStatus("current")
_PduUnitStatusActivePower_Type = Integer32
_PduUnitStatusActivePower_Object = MibTableColumn
pduUnitStatusActivePower = _PduUnitStatusActivePower_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 4, 1, 4),
    _PduUnitStatusActivePower_Type()
)
pduUnitStatusActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusActivePower.setStatus("current")
_PduUnitStatusApparentPower_Type = Integer32
_PduUnitStatusApparentPower_Object = MibTableColumn
pduUnitStatusApparentPower = _PduUnitStatusApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 4, 1, 5),
    _PduUnitStatusApparentPower_Type()
)
pduUnitStatusApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusApparentPower.setStatus("current")
_PduUnitStatusPeakPower_Type = Integer32
_PduUnitStatusPeakPower_Object = MibTableColumn
pduUnitStatusPeakPower = _PduUnitStatusPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 4, 1, 6),
    _PduUnitStatusPeakPower_Type()
)
pduUnitStatusPeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusPeakPower.setStatus("current")
_PduUnitStatusPeakPowerTimestamp_Type = DisplayString
_PduUnitStatusPeakPowerTimestamp_Object = MibTableColumn
pduUnitStatusPeakPowerTimestamp = _PduUnitStatusPeakPowerTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 4, 1, 7),
    _PduUnitStatusPeakPowerTimestamp_Type()
)
pduUnitStatusPeakPowerTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusPeakPowerTimestamp.setStatus("current")
_PduUnitStatusPeakPowerStartTime_Type = DisplayString
_PduUnitStatusPeakPowerStartTime_Object = MibTableColumn
pduUnitStatusPeakPowerStartTime = _PduUnitStatusPeakPowerStartTime_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 4, 1, 8),
    _PduUnitStatusPeakPowerStartTime_Type()
)
pduUnitStatusPeakPowerStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusPeakPowerStartTime.setStatus("current")
_PduUnitStatusEnergy_Type = Integer32
_PduUnitStatusEnergy_Object = MibTableColumn
pduUnitStatusEnergy = _PduUnitStatusEnergy_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 4, 1, 9),
    _PduUnitStatusEnergy_Type()
)
pduUnitStatusEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusEnergy.setStatus("current")
_PduUnitStatusResettableEnergy_Type = Integer32
_PduUnitStatusResettableEnergy_Object = MibTableColumn
pduUnitStatusResettableEnergy = _PduUnitStatusResettableEnergy_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 4, 1, 10),
    _PduUnitStatusResettableEnergy_Type()
)
pduUnitStatusResettableEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusResettableEnergy.setStatus("current")
_PduUnitStatusEnergyStartTime_Type = DisplayString
_PduUnitStatusEnergyStartTime_Object = MibTableColumn
pduUnitStatusEnergyStartTime = _PduUnitStatusEnergyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 4, 1, 11),
    _PduUnitStatusEnergyStartTime_Type()
)
pduUnitStatusEnergyStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusEnergyStartTime.setStatus("current")
_PduUnitStatusOutletsEnergyStartTime_Type = DisplayString
_PduUnitStatusOutletsEnergyStartTime_Object = MibTableColumn
pduUnitStatusOutletsEnergyStartTime = _PduUnitStatusOutletsEnergyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 4, 1, 12),
    _PduUnitStatusOutletsEnergyStartTime_Type()
)
pduUnitStatusOutletsEnergyStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusOutletsEnergyStartTime.setStatus("current")
_PduUnitPsTable_Object = MibTable
pduUnitPsTable = _PduUnitPsTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 5)
)
if mibBuilder.loadTexts:
    pduUnitPsTable.setStatus("current")
_PduUnitPsEntry_Object = MibTableRow
pduUnitPsEntry = _PduUnitPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 5, 1)
)
pduUnitPsEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitPsIndex"),
)
if mibBuilder.loadTexts:
    pduUnitPsEntry.setStatus("current")


class _PduUnitPsIndex_Type(Integer32):
    """Custom type pduUnitPsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_PduUnitPsIndex_Type.__name__ = "Integer32"
_PduUnitPsIndex_Object = MibTableColumn
pduUnitPsIndex = _PduUnitPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 5, 1, 1),
    _PduUnitPsIndex_Type()
)
pduUnitPsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPsIndex.setStatus("current")


class _PduUnitPsSupportUpstreamStatus_Type(Integer32):
    """Custom type pduUnitPsSupportUpstreamStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("available", 1))
    )


_PduUnitPsSupportUpstreamStatus_Type.__name__ = "Integer32"
_PduUnitPsSupportUpstreamStatus_Object = MibTableColumn
pduUnitPsSupportUpstreamStatus = _PduUnitPsSupportUpstreamStatus_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 5, 1, 2),
    _PduUnitPsSupportUpstreamStatus_Type()
)
pduUnitPsSupportUpstreamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPsSupportUpstreamStatus.setStatus("current")


class _PduUnitPsSupportDownstreamStatus_Type(Integer32):
    """Custom type pduUnitPsSupportDownstreamStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("available", 1))
    )


_PduUnitPsSupportDownstreamStatus_Type.__name__ = "Integer32"
_PduUnitPsSupportDownstreamStatus_Object = MibTableColumn
pduUnitPsSupportDownstreamStatus = _PduUnitPsSupportDownstreamStatus_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 5, 1, 3),
    _PduUnitPsSupportDownstreamStatus_Type()
)
pduUnitPsSupportDownstreamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPsSupportDownstreamStatus.setStatus("current")


class _PduUnitPsOptMode_Type(Integer32):
    """Custom type pduUnitPsOptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("backupPower", 0),
          ("mainPower", 1))
    )


_PduUnitPsOptMode_Type.__name__ = "Integer32"
_PduUnitPsOptMode_Object = MibTableColumn
pduUnitPsOptMode = _PduUnitPsOptMode_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 2, 5, 1, 4),
    _PduUnitPsOptMode_Type()
)
pduUnitPsOptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPsOptMode.setStatus("current")
_PduInputPhase_ObjectIdentity = ObjectIdentity
pduInputPhase = _PduInputPhase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3)
)


class _PduInputPhaseTableSize_Type(Integer32):
    """Custom type pduInputPhaseTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduInputPhaseTableSize_Type.__name__ = "Integer32"
_PduInputPhaseTableSize_Object = MibScalar
pduInputPhaseTableSize = _PduInputPhaseTableSize_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 1),
    _PduInputPhaseTableSize_Type()
)
pduInputPhaseTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseTableSize.setStatus("current")
_PduInputPhaseConfigTable_Object = MibTable
pduInputPhaseConfigTable = _PduInputPhaseConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 2)
)
if mibBuilder.loadTexts:
    pduInputPhaseConfigTable.setStatus("current")
_PduInputPhaseConfigEntry_Object = MibTableRow
pduInputPhaseConfigEntry = _PduInputPhaseConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 2, 1)
)
pduInputPhaseConfigEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitConfigIndex"),
    (0, "CPDU-MIB", "pduInputPhaseConfigIndex"),
)
if mibBuilder.loadTexts:
    pduInputPhaseConfigEntry.setStatus("current")


class _PduInputPhaseConfigIndex_Type(Integer32):
    """Custom type pduInputPhaseConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduInputPhaseConfigIndex_Type.__name__ = "Integer32"
_PduInputPhaseConfigIndex_Object = MibTableColumn
pduInputPhaseConfigIndex = _PduInputPhaseConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 2, 1, 1),
    _PduInputPhaseConfigIndex_Type()
)
pduInputPhaseConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduInputPhaseConfigIndex.setStatus("current")


class _PduInputPhaseConfigCount_Type(Integer32):
    """Custom type pduInputPhaseConfigCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduInputPhaseConfigCount_Type.__name__ = "Integer32"
_PduInputPhaseConfigCount_Object = MibTableColumn
pduInputPhaseConfigCount = _PduInputPhaseConfigCount_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 2, 1, 2),
    _PduInputPhaseConfigCount_Type()
)
pduInputPhaseConfigCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseConfigCount.setStatus("current")


class _PduInputPhaseConfigOverloadRestriction_Type(Integer32):
    """Custom type pduInputPhaseConfigOverloadRestriction based on Integer32"""
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
        *(("alwaysAllowTurnOn", 1),
          ("restrictOnUpperWarning", 2),
          ("restrictOnUpperCritical", 3),
          ("notSupported", 4))
    )


_PduInputPhaseConfigOverloadRestriction_Type.__name__ = "Integer32"
_PduInputPhaseConfigOverloadRestriction_Object = MibTableColumn
pduInputPhaseConfigOverloadRestriction = _PduInputPhaseConfigOverloadRestriction_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 2, 1, 3),
    _PduInputPhaseConfigOverloadRestriction_Type()
)
pduInputPhaseConfigOverloadRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigOverloadRestriction.setStatus("current")
_PduInputPhaseConfigCurrentLowerCriticalThreshold_Type = Unsigned32
_PduInputPhaseConfigCurrentLowerCriticalThreshold_Object = MibTableColumn
pduInputPhaseConfigCurrentLowerCriticalThreshold = _PduInputPhaseConfigCurrentLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 2, 1, 4),
    _PduInputPhaseConfigCurrentLowerCriticalThreshold_Type()
)
pduInputPhaseConfigCurrentLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigCurrentLowerCriticalThreshold.setStatus("current")
_PduInputPhaseConfigCurrentLowerWarningThreshold_Type = Unsigned32
_PduInputPhaseConfigCurrentLowerWarningThreshold_Object = MibTableColumn
pduInputPhaseConfigCurrentLowerWarningThreshold = _PduInputPhaseConfigCurrentLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 2, 1, 5),
    _PduInputPhaseConfigCurrentLowerWarningThreshold_Type()
)
pduInputPhaseConfigCurrentLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigCurrentLowerWarningThreshold.setStatus("current")
_PduInputPhaseConfigCurrentUpperCriticalThreshold_Type = Unsigned32
_PduInputPhaseConfigCurrentUpperCriticalThreshold_Object = MibTableColumn
pduInputPhaseConfigCurrentUpperCriticalThreshold = _PduInputPhaseConfigCurrentUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 2, 1, 6),
    _PduInputPhaseConfigCurrentUpperCriticalThreshold_Type()
)
pduInputPhaseConfigCurrentUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigCurrentUpperCriticalThreshold.setStatus("current")
_PduInputPhaseConfigCurrentUpperWarningThreshold_Type = Unsigned32
_PduInputPhaseConfigCurrentUpperWarningThreshold_Object = MibTableColumn
pduInputPhaseConfigCurrentUpperWarningThreshold = _PduInputPhaseConfigCurrentUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 2, 1, 7),
    _PduInputPhaseConfigCurrentUpperWarningThreshold_Type()
)
pduInputPhaseConfigCurrentUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigCurrentUpperWarningThreshold.setStatus("current")
_PduInputPhaseConfigVoltageLowerCriticalThreshold_Type = Unsigned32
_PduInputPhaseConfigVoltageLowerCriticalThreshold_Object = MibTableColumn
pduInputPhaseConfigVoltageLowerCriticalThreshold = _PduInputPhaseConfigVoltageLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 2, 1, 8),
    _PduInputPhaseConfigVoltageLowerCriticalThreshold_Type()
)
pduInputPhaseConfigVoltageLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigVoltageLowerCriticalThreshold.setStatus("current")
_PduInputPhaseConfigVoltageLowerWarningThreshold_Type = Unsigned32
_PduInputPhaseConfigVoltageLowerWarningThreshold_Object = MibTableColumn
pduInputPhaseConfigVoltageLowerWarningThreshold = _PduInputPhaseConfigVoltageLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 2, 1, 9),
    _PduInputPhaseConfigVoltageLowerWarningThreshold_Type()
)
pduInputPhaseConfigVoltageLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigVoltageLowerWarningThreshold.setStatus("current")
_PduInputPhaseConfigVoltageUpperCriticalThreshold_Type = Unsigned32
_PduInputPhaseConfigVoltageUpperCriticalThreshold_Object = MibTableColumn
pduInputPhaseConfigVoltageUpperCriticalThreshold = _PduInputPhaseConfigVoltageUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 2, 1, 10),
    _PduInputPhaseConfigVoltageUpperCriticalThreshold_Type()
)
pduInputPhaseConfigVoltageUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigVoltageUpperCriticalThreshold.setStatus("current")
_PduInputPhaseConfigVoltageUpperWarningThreshold_Type = Unsigned32
_PduInputPhaseConfigVoltageUpperWarningThreshold_Object = MibTableColumn
pduInputPhaseConfigVoltageUpperWarningThreshold = _PduInputPhaseConfigVoltageUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 2, 1, 11),
    _PduInputPhaseConfigVoltageUpperWarningThreshold_Type()
)
pduInputPhaseConfigVoltageUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigVoltageUpperWarningThreshold.setStatus("current")
_PduInputPhaseConfigCurrentAlarmResetThreshold_Type = Unsigned32
_PduInputPhaseConfigCurrentAlarmResetThreshold_Object = MibTableColumn
pduInputPhaseConfigCurrentAlarmResetThreshold = _PduInputPhaseConfigCurrentAlarmResetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 2, 1, 12),
    _PduInputPhaseConfigCurrentAlarmResetThreshold_Type()
)
pduInputPhaseConfigCurrentAlarmResetThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigCurrentAlarmResetThreshold.setStatus("current")
_PduInputPhaseConfigCurrentAlarmStateChangeDelay_Type = Integer32
_PduInputPhaseConfigCurrentAlarmStateChangeDelay_Object = MibTableColumn
pduInputPhaseConfigCurrentAlarmStateChangeDelay = _PduInputPhaseConfigCurrentAlarmStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 2, 1, 13),
    _PduInputPhaseConfigCurrentAlarmStateChangeDelay_Type()
)
pduInputPhaseConfigCurrentAlarmStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigCurrentAlarmStateChangeDelay.setStatus("current")


class _PduInputPhaseConfigCurrentEnabledThresholds_Type(Bits):
    """Custom type pduInputPhaseConfigCurrentEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperWarning", 2),
          ("upperCritical", 3))
    )

_PduInputPhaseConfigCurrentEnabledThresholds_Type.__name__ = "Bits"
_PduInputPhaseConfigCurrentEnabledThresholds_Object = MibTableColumn
pduInputPhaseConfigCurrentEnabledThresholds = _PduInputPhaseConfigCurrentEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 2, 1, 14),
    _PduInputPhaseConfigCurrentEnabledThresholds_Type()
)
pduInputPhaseConfigCurrentEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigCurrentEnabledThresholds.setStatus("current")
_PduInputPhaseConfigVoltageAlarmResetThreshold_Type = Unsigned32
_PduInputPhaseConfigVoltageAlarmResetThreshold_Object = MibTableColumn
pduInputPhaseConfigVoltageAlarmResetThreshold = _PduInputPhaseConfigVoltageAlarmResetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 2, 1, 15),
    _PduInputPhaseConfigVoltageAlarmResetThreshold_Type()
)
pduInputPhaseConfigVoltageAlarmResetThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigVoltageAlarmResetThreshold.setStatus("current")
_PduInputPhaseConfigVoltageAlarmStateChangeDelay_Type = Integer32
_PduInputPhaseConfigVoltageAlarmStateChangeDelay_Object = MibTableColumn
pduInputPhaseConfigVoltageAlarmStateChangeDelay = _PduInputPhaseConfigVoltageAlarmStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 2, 1, 16),
    _PduInputPhaseConfigVoltageAlarmStateChangeDelay_Type()
)
pduInputPhaseConfigVoltageAlarmStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigVoltageAlarmStateChangeDelay.setStatus("current")


class _PduInputPhaseConfigVoltageEnabledThresholds_Type(Bits):
    """Custom type pduInputPhaseConfigVoltageEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperWarning", 2),
          ("upperCritical", 3))
    )

_PduInputPhaseConfigVoltageEnabledThresholds_Type.__name__ = "Bits"
_PduInputPhaseConfigVoltageEnabledThresholds_Object = MibTableColumn
pduInputPhaseConfigVoltageEnabledThresholds = _PduInputPhaseConfigVoltageEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 2, 1, 17),
    _PduInputPhaseConfigVoltageEnabledThresholds_Type()
)
pduInputPhaseConfigVoltageEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigVoltageEnabledThresholds.setStatus("current")
_PduInputPhasePropertiesTable_Object = MibTable
pduInputPhasePropertiesTable = _PduInputPhasePropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 3)
)
if mibBuilder.loadTexts:
    pduInputPhasePropertiesTable.setStatus("current")
_PduInputPhasePropertiesEntry_Object = MibTableRow
pduInputPhasePropertiesEntry = _PduInputPhasePropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 3, 1)
)
pduInputPhasePropertiesEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitPropertiesIndex"),
    (0, "CPDU-MIB", "pduInputPhasePropertiesIndex"),
)
if mibBuilder.loadTexts:
    pduInputPhasePropertiesEntry.setStatus("current")


class _PduInputPhasePropertiesIndex_Type(Integer32):
    """Custom type pduInputPhasePropertiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduInputPhasePropertiesIndex_Type.__name__ = "Integer32"
_PduInputPhasePropertiesIndex_Object = MibTableColumn
pduInputPhasePropertiesIndex = _PduInputPhasePropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 3, 1, 1),
    _PduInputPhasePropertiesIndex_Type()
)
pduInputPhasePropertiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduInputPhasePropertiesIndex.setStatus("current")


class _PduInputPhasePropertiesCount_Type(Integer32):
    """Custom type pduInputPhasePropertiesCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduInputPhasePropertiesCount_Type.__name__ = "Integer32"
_PduInputPhasePropertiesCount_Object = MibTableColumn
pduInputPhasePropertiesCount = _PduInputPhasePropertiesCount_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 3, 1, 2),
    _PduInputPhasePropertiesCount_Type()
)
pduInputPhasePropertiesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhasePropertiesCount.setStatus("current")
_PduInputPhaseStatusTable_Object = MibTable
pduInputPhaseStatusTable = _PduInputPhaseStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 4)
)
if mibBuilder.loadTexts:
    pduInputPhaseStatusTable.setStatus("current")
_PduInputPhaseStatusEntry_Object = MibTableRow
pduInputPhaseStatusEntry = _PduInputPhaseStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 4, 1)
)
pduInputPhaseStatusEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitStatusIndex"),
    (0, "CPDU-MIB", "pduInputPhaseStatusIndex"),
)
if mibBuilder.loadTexts:
    pduInputPhaseStatusEntry.setStatus("current")


class _PduInputPhaseStatusIndex_Type(Integer32):
    """Custom type pduInputPhaseStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduInputPhaseStatusIndex_Type.__name__ = "Integer32"
_PduInputPhaseStatusIndex_Object = MibTableColumn
pduInputPhaseStatusIndex = _PduInputPhaseStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 4, 1, 1),
    _PduInputPhaseStatusIndex_Type()
)
pduInputPhaseStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduInputPhaseStatusIndex.setStatus("current")


class _PduInputPhaseStatusCount_Type(Integer32):
    """Custom type pduInputPhaseStatusCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduInputPhaseStatusCount_Type.__name__ = "Integer32"
_PduInputPhaseStatusCount_Object = MibTableColumn
pduInputPhaseStatusCount = _PduInputPhaseStatusCount_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 4, 1, 2),
    _PduInputPhaseStatusCount_Type()
)
pduInputPhaseStatusCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseStatusCount.setStatus("current")


class _PduInputPhaseStatusCurrentState_Type(Integer32):
    """Custom type pduInputPhaseStatusCurrentState based on Integer32"""
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
        *(("upperCritical", 1),
          ("upperWarning", 2),
          ("lowerWarning", 3),
          ("lowerCritical", 4),
          ("normal", 5))
    )


_PduInputPhaseStatusCurrentState_Type.__name__ = "Integer32"
_PduInputPhaseStatusCurrentState_Object = MibTableColumn
pduInputPhaseStatusCurrentState = _PduInputPhaseStatusCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 4, 1, 3),
    _PduInputPhaseStatusCurrentState_Type()
)
pduInputPhaseStatusCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseStatusCurrentState.setStatus("current")


class _PduInputPhaseStatusVoltageState_Type(Integer32):
    """Custom type pduInputPhaseStatusVoltageState based on Integer32"""
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
        *(("upperCritical", 1),
          ("upperWarning", 2),
          ("lowerWarning", 3),
          ("lowerCritical", 4),
          ("normal", 5))
    )


_PduInputPhaseStatusVoltageState_Type.__name__ = "Integer32"
_PduInputPhaseStatusVoltageState_Object = MibTableColumn
pduInputPhaseStatusVoltageState = _PduInputPhaseStatusVoltageState_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 4, 1, 4),
    _PduInputPhaseStatusVoltageState_Type()
)
pduInputPhaseStatusVoltageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseStatusVoltageState.setStatus("current")
_PduInputPhaseStatusCurrent_Type = Integer32
_PduInputPhaseStatusCurrent_Object = MibTableColumn
pduInputPhaseStatusCurrent = _PduInputPhaseStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 4, 1, 5),
    _PduInputPhaseStatusCurrent_Type()
)
pduInputPhaseStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseStatusCurrent.setStatus("current")
_PduInputPhaseStatusVoltage_Type = Integer32
_PduInputPhaseStatusVoltage_Object = MibTableColumn
pduInputPhaseStatusVoltage = _PduInputPhaseStatusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 4, 1, 6),
    _PduInputPhaseStatusVoltage_Type()
)
pduInputPhaseStatusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseStatusVoltage.setStatus("current")
_PduInputPhaseStatusActivePower_Type = Integer32
_PduInputPhaseStatusActivePower_Object = MibTableColumn
pduInputPhaseStatusActivePower = _PduInputPhaseStatusActivePower_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 4, 1, 7),
    _PduInputPhaseStatusActivePower_Type()
)
pduInputPhaseStatusActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseStatusActivePower.setStatus("current")
_PduInputPhaseStatusApparentPower_Type = Integer32
_PduInputPhaseStatusApparentPower_Object = MibTableColumn
pduInputPhaseStatusApparentPower = _PduInputPhaseStatusApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 4, 1, 8),
    _PduInputPhaseStatusApparentPower_Type()
)
pduInputPhaseStatusApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseStatusApparentPower.setStatus("current")
_PduInputPhaseStatusPowerFactor_Type = Integer32
_PduInputPhaseStatusPowerFactor_Object = MibTableColumn
pduInputPhaseStatusPowerFactor = _PduInputPhaseStatusPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 3, 4, 1, 9),
    _PduInputPhaseStatusPowerFactor_Type()
)
pduInputPhaseStatusPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseStatusPowerFactor.setStatus("current")
_PduCircuitBreaker_ObjectIdentity = ObjectIdentity
pduCircuitBreaker = _PduCircuitBreaker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4)
)


class _PduCircuitBreakerTableSize_Type(Integer32):
    """Custom type pduCircuitBreakerTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduCircuitBreakerTableSize_Type.__name__ = "Integer32"
_PduCircuitBreakerTableSize_Object = MibScalar
pduCircuitBreakerTableSize = _PduCircuitBreakerTableSize_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 1),
    _PduCircuitBreakerTableSize_Type()
)
pduCircuitBreakerTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCircuitBreakerTableSize.setStatus("current")
_PduCircuitBreakerConfigTable_Object = MibTable
pduCircuitBreakerConfigTable = _PduCircuitBreakerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 2)
)
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigTable.setStatus("current")
_PduCircuitBreakerConfigEntry_Object = MibTableRow
pduCircuitBreakerConfigEntry = _PduCircuitBreakerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 2, 1)
)
pduCircuitBreakerConfigEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitConfigIndex"),
    (0, "CPDU-MIB", "pduCircuitBreakerConfigIndex"),
)
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigEntry.setStatus("current")


class _PduCircuitBreakerConfigIndex_Type(Integer32):
    """Custom type pduCircuitBreakerConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduCircuitBreakerConfigIndex_Type.__name__ = "Integer32"
_PduCircuitBreakerConfigIndex_Object = MibTableColumn
pduCircuitBreakerConfigIndex = _PduCircuitBreakerConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 2, 1, 1),
    _PduCircuitBreakerConfigIndex_Type()
)
pduCircuitBreakerConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigIndex.setStatus("current")


class _PduCircuitBreakerConfigCount_Type(Integer32):
    """Custom type pduCircuitBreakerConfigCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduCircuitBreakerConfigCount_Type.__name__ = "Integer32"
_PduCircuitBreakerConfigCount_Object = MibTableColumn
pduCircuitBreakerConfigCount = _PduCircuitBreakerConfigCount_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 2, 1, 2),
    _PduCircuitBreakerConfigCount_Type()
)
pduCircuitBreakerConfigCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigCount.setStatus("current")
_PduCircuitBreakerName_Type = DisplayString
_PduCircuitBreakerName_Object = MibTableColumn
pduCircuitBreakerName = _PduCircuitBreakerName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 2, 1, 3),
    _PduCircuitBreakerName_Type()
)
pduCircuitBreakerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCircuitBreakerName.setStatus("current")


class _PduCircuitBreakerConfigOverloadRestriction_Type(Integer32):
    """Custom type pduCircuitBreakerConfigOverloadRestriction based on Integer32"""
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
        *(("alwaysAllowTurnOn", 1),
          ("restrictOnUpperWarning", 2),
          ("restrictOnUpperCritical", 3),
          ("notSupported", 4))
    )


_PduCircuitBreakerConfigOverloadRestriction_Type.__name__ = "Integer32"
_PduCircuitBreakerConfigOverloadRestriction_Object = MibTableColumn
pduCircuitBreakerConfigOverloadRestriction = _PduCircuitBreakerConfigOverloadRestriction_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 2, 1, 4),
    _PduCircuitBreakerConfigOverloadRestriction_Type()
)
pduCircuitBreakerConfigOverloadRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigOverloadRestriction.setStatus("current")
_PduCircuitBreakerConfigLowerCriticalThreshold_Type = Unsigned32
_PduCircuitBreakerConfigLowerCriticalThreshold_Object = MibTableColumn
pduCircuitBreakerConfigLowerCriticalThreshold = _PduCircuitBreakerConfigLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 2, 1, 5),
    _PduCircuitBreakerConfigLowerCriticalThreshold_Type()
)
pduCircuitBreakerConfigLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigLowerCriticalThreshold.setStatus("current")
_PduCircuitBreakerConfigLowerWarningThreshold_Type = Unsigned32
_PduCircuitBreakerConfigLowerWarningThreshold_Object = MibTableColumn
pduCircuitBreakerConfigLowerWarningThreshold = _PduCircuitBreakerConfigLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 2, 1, 6),
    _PduCircuitBreakerConfigLowerWarningThreshold_Type()
)
pduCircuitBreakerConfigLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigLowerWarningThreshold.setStatus("current")
_PduCircuitBreakerConfigUpperCriticalThreshold_Type = Unsigned32
_PduCircuitBreakerConfigUpperCriticalThreshold_Object = MibTableColumn
pduCircuitBreakerConfigUpperCriticalThreshold = _PduCircuitBreakerConfigUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 2, 1, 7),
    _PduCircuitBreakerConfigUpperCriticalThreshold_Type()
)
pduCircuitBreakerConfigUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigUpperCriticalThreshold.setStatus("current")
_PduCircuitBreakerConfigUpperWarningThreshold_Type = Unsigned32
_PduCircuitBreakerConfigUpperWarningThreshold_Object = MibTableColumn
pduCircuitBreakerConfigUpperWarningThreshold = _PduCircuitBreakerConfigUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 2, 1, 8),
    _PduCircuitBreakerConfigUpperWarningThreshold_Type()
)
pduCircuitBreakerConfigUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigUpperWarningThreshold.setStatus("current")
_PduCircuitBreakerConfigAlarmResetThreshold_Type = Unsigned32
_PduCircuitBreakerConfigAlarmResetThreshold_Object = MibTableColumn
pduCircuitBreakerConfigAlarmResetThreshold = _PduCircuitBreakerConfigAlarmResetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 2, 1, 9),
    _PduCircuitBreakerConfigAlarmResetThreshold_Type()
)
pduCircuitBreakerConfigAlarmResetThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigAlarmResetThreshold.setStatus("current")
_PduCircuitBreakerConfigAlarmStateChangeDelay_Type = Unsigned32
_PduCircuitBreakerConfigAlarmStateChangeDelay_Object = MibTableColumn
pduCircuitBreakerConfigAlarmStateChangeDelay = _PduCircuitBreakerConfigAlarmStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 2, 1, 10),
    _PduCircuitBreakerConfigAlarmStateChangeDelay_Type()
)
pduCircuitBreakerConfigAlarmStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigAlarmStateChangeDelay.setStatus("current")


class _PduCircuitBreakerConfigEnabledThresholds_Type(Bits):
    """Custom type pduCircuitBreakerConfigEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperWarning", 2),
          ("upperCritical", 3))
    )

_PduCircuitBreakerConfigEnabledThresholds_Type.__name__ = "Bits"
_PduCircuitBreakerConfigEnabledThresholds_Object = MibTableColumn
pduCircuitBreakerConfigEnabledThresholds = _PduCircuitBreakerConfigEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 2, 1, 11),
    _PduCircuitBreakerConfigEnabledThresholds_Type()
)
pduCircuitBreakerConfigEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigEnabledThresholds.setStatus("current")
_PduCircuitBreakerPropertiesTable_Object = MibTable
pduCircuitBreakerPropertiesTable = _PduCircuitBreakerPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 3)
)
if mibBuilder.loadTexts:
    pduCircuitBreakerPropertiesTable.setStatus("current")
_PduCircuitBreakerPropertiesEntry_Object = MibTableRow
pduCircuitBreakerPropertiesEntry = _PduCircuitBreakerPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 3, 1)
)
pduCircuitBreakerPropertiesEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitPropertiesIndex"),
    (0, "CPDU-MIB", "pduCircuitBreakerPropertiesIndex"),
)
if mibBuilder.loadTexts:
    pduCircuitBreakerPropertiesEntry.setStatus("current")


class _PduCircuitBreakerPropertiesIndex_Type(Integer32):
    """Custom type pduCircuitBreakerPropertiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduCircuitBreakerPropertiesIndex_Type.__name__ = "Integer32"
_PduCircuitBreakerPropertiesIndex_Object = MibTableColumn
pduCircuitBreakerPropertiesIndex = _PduCircuitBreakerPropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 3, 1, 1),
    _PduCircuitBreakerPropertiesIndex_Type()
)
pduCircuitBreakerPropertiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduCircuitBreakerPropertiesIndex.setStatus("current")


class _PduCircuitBreakerPropertiesCount_Type(Integer32):
    """Custom type pduCircuitBreakerPropertiesCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduCircuitBreakerPropertiesCount_Type.__name__ = "Integer32"
_PduCircuitBreakerPropertiesCount_Object = MibTableColumn
pduCircuitBreakerPropertiesCount = _PduCircuitBreakerPropertiesCount_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 3, 1, 2),
    _PduCircuitBreakerPropertiesCount_Type()
)
pduCircuitBreakerPropertiesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCircuitBreakerPropertiesCount.setStatus("current")


class _PduCircuitBreakerPropertiesInputLayout_Type(Integer32):
    """Custom type pduCircuitBreakerPropertiesInputLayout based on Integer32"""
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
        *(("seqPhase1ToNeutral", 1),
          ("seqPhase2ToNeutral", 2),
          ("seqPhase3ToNeutral", 3),
          ("seqPhase1ToPhase2", 4),
          ("seqPhase2ToPhase3", 5),
          ("seqPhase3ToPhase1", 6))
    )


_PduCircuitBreakerPropertiesInputLayout_Type.__name__ = "Integer32"
_PduCircuitBreakerPropertiesInputLayout_Object = MibTableColumn
pduCircuitBreakerPropertiesInputLayout = _PduCircuitBreakerPropertiesInputLayout_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 3, 1, 3),
    _PduCircuitBreakerPropertiesInputLayout_Type()
)
pduCircuitBreakerPropertiesInputLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCircuitBreakerPropertiesInputLayout.setStatus("current")


class _PduCircuitBreakerPropertiesCurrentRating_Type(Integer32):
    """Custom type pduCircuitBreakerPropertiesCurrentRating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduCircuitBreakerPropertiesCurrentRating_Type.__name__ = "Integer32"
_PduCircuitBreakerPropertiesCurrentRating_Object = MibTableColumn
pduCircuitBreakerPropertiesCurrentRating = _PduCircuitBreakerPropertiesCurrentRating_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 3, 1, 4),
    _PduCircuitBreakerPropertiesCurrentRating_Type()
)
pduCircuitBreakerPropertiesCurrentRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCircuitBreakerPropertiesCurrentRating.setStatus("current")
_PduCircuitBreakerStatusTable_Object = MibTable
pduCircuitBreakerStatusTable = _PduCircuitBreakerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 4)
)
if mibBuilder.loadTexts:
    pduCircuitBreakerStatusTable.setStatus("current")
_PduCircuitBreakerStatusEntry_Object = MibTableRow
pduCircuitBreakerStatusEntry = _PduCircuitBreakerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 4, 1)
)
pduCircuitBreakerStatusEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitStatusIndex"),
    (0, "CPDU-MIB", "pduCircuitBreakerStatusIndex"),
)
if mibBuilder.loadTexts:
    pduCircuitBreakerStatusEntry.setStatus("current")


class _PduCircuitBreakerStatusIndex_Type(Integer32):
    """Custom type pduCircuitBreakerStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduCircuitBreakerStatusIndex_Type.__name__ = "Integer32"
_PduCircuitBreakerStatusIndex_Object = MibTableColumn
pduCircuitBreakerStatusIndex = _PduCircuitBreakerStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 4, 1, 1),
    _PduCircuitBreakerStatusIndex_Type()
)
pduCircuitBreakerStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduCircuitBreakerStatusIndex.setStatus("current")


class _PduCircuitBreakerStatusCount_Type(Integer32):
    """Custom type pduCircuitBreakerStatusCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduCircuitBreakerStatusCount_Type.__name__ = "Integer32"
_PduCircuitBreakerStatusCount_Object = MibTableColumn
pduCircuitBreakerStatusCount = _PduCircuitBreakerStatusCount_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 4, 1, 2),
    _PduCircuitBreakerStatusCount_Type()
)
pduCircuitBreakerStatusCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCircuitBreakerStatusCount.setStatus("current")
_PduCircuitBreakerLabel_Type = DisplayString
_PduCircuitBreakerLabel_Object = MibTableColumn
pduCircuitBreakerLabel = _PduCircuitBreakerLabel_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 4, 1, 3),
    _PduCircuitBreakerLabel_Type()
)
pduCircuitBreakerLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCircuitBreakerLabel.setStatus("current")


class _PduCircuitBreakerStatusLoadState_Type(Integer32):
    """Custom type pduCircuitBreakerStatusLoadState based on Integer32"""
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
        *(("upperCritical", 1),
          ("upperWarning", 2),
          ("lowerWarning", 3),
          ("lowerCritical", 4),
          ("normal", 5),
          ("off", 6))
    )


_PduCircuitBreakerStatusLoadState_Type.__name__ = "Integer32"
_PduCircuitBreakerStatusLoadState_Object = MibTableColumn
pduCircuitBreakerStatusLoadState = _PduCircuitBreakerStatusLoadState_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 4, 1, 4),
    _PduCircuitBreakerStatusLoadState_Type()
)
pduCircuitBreakerStatusLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCircuitBreakerStatusLoadState.setStatus("current")
_PduCircuitBreakerStatusCurrent_Type = Integer32
_PduCircuitBreakerStatusCurrent_Object = MibTableColumn
pduCircuitBreakerStatusCurrent = _PduCircuitBreakerStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 4, 4, 1, 5),
    _PduCircuitBreakerStatusCurrent_Type()
)
pduCircuitBreakerStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCircuitBreakerStatusCurrent.setStatus("current")
_PduOutlet_ObjectIdentity = ObjectIdentity
pduOutlet = _PduOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5)
)


class _PduOutletSwitchedTableSize_Type(Integer32):
    """Custom type pduOutletSwitchedTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletSwitchedTableSize_Type.__name__ = "Integer32"
_PduOutletSwitchedTableSize_Object = MibScalar
pduOutletSwitchedTableSize = _PduOutletSwitchedTableSize_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 1),
    _PduOutletSwitchedTableSize_Type()
)
pduOutletSwitchedTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedTableSize.setStatus("current")
_PduOutletSwitchedConfigTable_Object = MibTable
pduOutletSwitchedConfigTable = _PduOutletSwitchedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 2)
)
if mibBuilder.loadTexts:
    pduOutletSwitchedConfigTable.setStatus("current")
_PduOutletSwitchedConfigEntry_Object = MibTableRow
pduOutletSwitchedConfigEntry = _PduOutletSwitchedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 2, 1)
)
pduOutletSwitchedConfigEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitConfigIndex"),
    (0, "CPDU-MIB", "pduOutletSwitchedConfigIndex"),
)
if mibBuilder.loadTexts:
    pduOutletSwitchedConfigEntry.setStatus("current")


class _PduOutletSwitchedConfigIndex_Type(Integer32):
    """Custom type pduOutletSwitchedConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletSwitchedConfigIndex_Type.__name__ = "Integer32"
_PduOutletSwitchedConfigIndex_Object = MibTableColumn
pduOutletSwitchedConfigIndex = _PduOutletSwitchedConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 2, 1, 1),
    _PduOutletSwitchedConfigIndex_Type()
)
pduOutletSwitchedConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutletSwitchedConfigIndex.setStatus("current")
_PduOutletSwitchedName_Type = DisplayString
_PduOutletSwitchedName_Object = MibTableColumn
pduOutletSwitchedName = _PduOutletSwitchedName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 2, 1, 2),
    _PduOutletSwitchedName_Type()
)
pduOutletSwitchedName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchedName.setStatus("current")


class _PduOutletSwitchedStateOnStartup_Type(Integer32):
    """Custom type pduOutletSwitchedStateOnStartup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("lastKnownState", 2))
    )


_PduOutletSwitchedStateOnStartup_Type.__name__ = "Integer32"
_PduOutletSwitchedStateOnStartup_Object = MibTableColumn
pduOutletSwitchedStateOnStartup = _PduOutletSwitchedStateOnStartup_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 2, 1, 3),
    _PduOutletSwitchedStateOnStartup_Type()
)
pduOutletSwitchedStateOnStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchedStateOnStartup.setStatus("current")
_PduOutletSwitchedConfigPowerOnTime_Type = Integer32
_PduOutletSwitchedConfigPowerOnTime_Object = MibTableColumn
pduOutletSwitchedConfigPowerOnTime = _PduOutletSwitchedConfigPowerOnTime_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 2, 1, 4),
    _PduOutletSwitchedConfigPowerOnTime_Type()
)
pduOutletSwitchedConfigPowerOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchedConfigPowerOnTime.setStatus("current")
_PduOutletSwitchedConfigPowerOffTime_Type = Integer32
_PduOutletSwitchedConfigPowerOffTime_Object = MibTableColumn
pduOutletSwitchedConfigPowerOffTime = _PduOutletSwitchedConfigPowerOffTime_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 2, 1, 5),
    _PduOutletSwitchedConfigPowerOffTime_Type()
)
pduOutletSwitchedConfigPowerOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchedConfigPowerOffTime.setStatus("current")
_PduOutletSwitchedConfigRebootDuration_Type = Integer32
_PduOutletSwitchedConfigRebootDuration_Object = MibTableColumn
pduOutletSwitchedConfigRebootDuration = _PduOutletSwitchedConfigRebootDuration_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 2, 1, 6),
    _PduOutletSwitchedConfigRebootDuration_Type()
)
pduOutletSwitchedConfigRebootDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchedConfigRebootDuration.setStatus("current")
_PduOutletSwitchedPropertiesTable_Object = MibTable
pduOutletSwitchedPropertiesTable = _PduOutletSwitchedPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 3)
)
if mibBuilder.loadTexts:
    pduOutletSwitchedPropertiesTable.setStatus("current")
_PduOutletSwitchedPropertiesEntry_Object = MibTableRow
pduOutletSwitchedPropertiesEntry = _PduOutletSwitchedPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 3, 1)
)
pduOutletSwitchedPropertiesEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitPropertiesIndex"),
    (0, "CPDU-MIB", "pduOutletSwitchedPropertiesIndex"),
)
if mibBuilder.loadTexts:
    pduOutletSwitchedPropertiesEntry.setStatus("current")


class _PduOutletSwitchedPropertiesIndex_Type(Integer32):
    """Custom type pduOutletSwitchedPropertiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletSwitchedPropertiesIndex_Type.__name__ = "Integer32"
_PduOutletSwitchedPropertiesIndex_Object = MibTableColumn
pduOutletSwitchedPropertiesIndex = _PduOutletSwitchedPropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 3, 1, 1),
    _PduOutletSwitchedPropertiesIndex_Type()
)
pduOutletSwitchedPropertiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutletSwitchedPropertiesIndex.setStatus("current")


class _PduOutletSwitchedPropertiesNumber_Type(Integer32):
    """Custom type pduOutletSwitchedPropertiesNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletSwitchedPropertiesNumber_Type.__name__ = "Integer32"
_PduOutletSwitchedPropertiesNumber_Object = MibTableColumn
pduOutletSwitchedPropertiesNumber = _PduOutletSwitchedPropertiesNumber_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 3, 1, 2),
    _PduOutletSwitchedPropertiesNumber_Type()
)
pduOutletSwitchedPropertiesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedPropertiesNumber.setStatus("current")
_PduOutletSwitchedPropertiesName_Type = DisplayString
_PduOutletSwitchedPropertiesName_Object = MibTableColumn
pduOutletSwitchedPropertiesName = _PduOutletSwitchedPropertiesName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 3, 1, 3),
    _PduOutletSwitchedPropertiesName_Type()
)
pduOutletSwitchedPropertiesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedPropertiesName.setStatus("current")


class _PduOutletSwitchedPropertiesInputPhaseLayout_Type(Integer32):
    """Custom type pduOutletSwitchedPropertiesInputPhaseLayout based on Integer32"""
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
        *(("seqPhase1ToNeutral", 1),
          ("seqPhase2ToNeutral", 2),
          ("seqPhase3ToNeutral", 3),
          ("seqPhase1ToPhase2", 4),
          ("seqPhase2ToPhase3", 5),
          ("seqPhase3ToPhase1", 6))
    )


_PduOutletSwitchedPropertiesInputPhaseLayout_Type.__name__ = "Integer32"
_PduOutletSwitchedPropertiesInputPhaseLayout_Object = MibTableColumn
pduOutletSwitchedPropertiesInputPhaseLayout = _PduOutletSwitchedPropertiesInputPhaseLayout_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 3, 1, 4),
    _PduOutletSwitchedPropertiesInputPhaseLayout_Type()
)
pduOutletSwitchedPropertiesInputPhaseLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedPropertiesInputPhaseLayout.setStatus("current")


class _PduOutletSwitchedPropertiesCircuitBreaker_Type(Integer32):
    """Custom type pduOutletSwitchedPropertiesCircuitBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletSwitchedPropertiesCircuitBreaker_Type.__name__ = "Integer32"
_PduOutletSwitchedPropertiesCircuitBreaker_Object = MibTableColumn
pduOutletSwitchedPropertiesCircuitBreaker = _PduOutletSwitchedPropertiesCircuitBreaker_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 3, 1, 5),
    _PduOutletSwitchedPropertiesCircuitBreaker_Type()
)
pduOutletSwitchedPropertiesCircuitBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedPropertiesCircuitBreaker.setStatus("current")


class _PduOutletSwitchedPropertiesCurrentRating_Type(Integer32):
    """Custom type pduOutletSwitchedPropertiesCurrentRating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletSwitchedPropertiesCurrentRating_Type.__name__ = "Integer32"
_PduOutletSwitchedPropertiesCurrentRating_Object = MibTableColumn
pduOutletSwitchedPropertiesCurrentRating = _PduOutletSwitchedPropertiesCurrentRating_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 3, 1, 6),
    _PduOutletSwitchedPropertiesCurrentRating_Type()
)
pduOutletSwitchedPropertiesCurrentRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedPropertiesCurrentRating.setStatus("current")
_PduOutletSwitchedStatusTable_Object = MibTable
pduOutletSwitchedStatusTable = _PduOutletSwitchedStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 4)
)
if mibBuilder.loadTexts:
    pduOutletSwitchedStatusTable.setStatus("current")
_PduOutletSwitchedStatusEntry_Object = MibTableRow
pduOutletSwitchedStatusEntry = _PduOutletSwitchedStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 4, 1)
)
pduOutletSwitchedStatusEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitStatusIndex"),
    (0, "CPDU-MIB", "pduOutletSwitchedStatusIndex"),
)
if mibBuilder.loadTexts:
    pduOutletSwitchedStatusEntry.setStatus("current")


class _PduOutletSwitchedStatusIndex_Type(Integer32):
    """Custom type pduOutletSwitchedStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletSwitchedStatusIndex_Type.__name__ = "Integer32"
_PduOutletSwitchedStatusIndex_Object = MibTableColumn
pduOutletSwitchedStatusIndex = _PduOutletSwitchedStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 4, 1, 1),
    _PduOutletSwitchedStatusIndex_Type()
)
pduOutletSwitchedStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutletSwitchedStatusIndex.setStatus("current")


class _PduOutletSwitchedStatusNumber_Type(Integer32):
    """Custom type pduOutletSwitchedStatusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletSwitchedStatusNumber_Type.__name__ = "Integer32"
_PduOutletSwitchedStatusNumber_Object = MibTableColumn
pduOutletSwitchedStatusNumber = _PduOutletSwitchedStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 4, 1, 2),
    _PduOutletSwitchedStatusNumber_Type()
)
pduOutletSwitchedStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedStatusNumber.setStatus("current")
_PduOutletSwitchedStatusName_Type = DisplayString
_PduOutletSwitchedStatusName_Object = MibTableColumn
pduOutletSwitchedStatusName = _PduOutletSwitchedStatusName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 4, 1, 3),
    _PduOutletSwitchedStatusName_Type()
)
pduOutletSwitchedStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedStatusName.setStatus("current")


class _PduOutletSwitchedStatusState_Type(Integer32):
    """Custom type pduOutletSwitchedStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_PduOutletSwitchedStatusState_Type.__name__ = "Integer32"
_PduOutletSwitchedStatusState_Object = MibTableColumn
pduOutletSwitchedStatusState = _PduOutletSwitchedStatusState_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 4, 1, 4),
    _PduOutletSwitchedStatusState_Type()
)
pduOutletSwitchedStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedStatusState.setStatus("current")
_PduOutletSwitchedControlTable_Object = MibTable
pduOutletSwitchedControlTable = _PduOutletSwitchedControlTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 5)
)
if mibBuilder.loadTexts:
    pduOutletSwitchedControlTable.setStatus("current")
_PduOutletSwitchedControlEntry_Object = MibTableRow
pduOutletSwitchedControlEntry = _PduOutletSwitchedControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 5, 1)
)
pduOutletSwitchedControlEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitConfigIndex"),
    (0, "CPDU-MIB", "pduOutletSwitchedControlIndex"),
)
if mibBuilder.loadTexts:
    pduOutletSwitchedControlEntry.setStatus("current")


class _PduOutletSwitchedControlIndex_Type(Integer32):
    """Custom type pduOutletSwitchedControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletSwitchedControlIndex_Type.__name__ = "Integer32"
_PduOutletSwitchedControlIndex_Object = MibTableColumn
pduOutletSwitchedControlIndex = _PduOutletSwitchedControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 5, 1, 1),
    _PduOutletSwitchedControlIndex_Type()
)
pduOutletSwitchedControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutletSwitchedControlIndex.setStatus("current")


class _PduOutletSwitchedControlNumber_Type(Integer32):
    """Custom type pduOutletSwitchedControlNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletSwitchedControlNumber_Type.__name__ = "Integer32"
_PduOutletSwitchedControlNumber_Object = MibTableColumn
pduOutletSwitchedControlNumber = _PduOutletSwitchedControlNumber_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 5, 1, 2),
    _PduOutletSwitchedControlNumber_Type()
)
pduOutletSwitchedControlNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedControlNumber.setStatus("current")
_PduOutletSwitchedControlName_Type = DisplayString
_PduOutletSwitchedControlName_Object = MibTableColumn
pduOutletSwitchedControlName = _PduOutletSwitchedControlName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 5, 1, 3),
    _PduOutletSwitchedControlName_Type()
)
pduOutletSwitchedControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedControlName.setStatus("current")


class _PduOutletSwitchedControlCommand_Type(Integer32):
    """Custom type pduOutletSwitchedControlCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("immediateOff", 1),
          ("immediateOn", 2),
          ("delayedOff", 3),
          ("delayedOn", 4),
          ("immediateReboot", 5),
          ("delayedReboot", 6),
          ("outletUnknown", 7))
    )


_PduOutletSwitchedControlCommand_Type.__name__ = "Integer32"
_PduOutletSwitchedControlCommand_Object = MibTableColumn
pduOutletSwitchedControlCommand = _PduOutletSwitchedControlCommand_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 5, 1, 4),
    _PduOutletSwitchedControlCommand_Type()
)
pduOutletSwitchedControlCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchedControlCommand.setStatus("current")


class _PduOutletMeteredTableSize_Type(Integer32):
    """Custom type pduOutletMeteredTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletMeteredTableSize_Type.__name__ = "Integer32"
_PduOutletMeteredTableSize_Object = MibScalar
pduOutletMeteredTableSize = _PduOutletMeteredTableSize_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 6),
    _PduOutletMeteredTableSize_Type()
)
pduOutletMeteredTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredTableSize.setStatus("current")
_PduOutletMeteredConfigTable_Object = MibTable
pduOutletMeteredConfigTable = _PduOutletMeteredConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 7)
)
if mibBuilder.loadTexts:
    pduOutletMeteredConfigTable.setStatus("current")
_PduOutletMeteredConfigEntry_Object = MibTableRow
pduOutletMeteredConfigEntry = _PduOutletMeteredConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 7, 1)
)
pduOutletMeteredConfigEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitConfigIndex"),
    (0, "CPDU-MIB", "pduOutletMeteredConfigIndex"),
)
if mibBuilder.loadTexts:
    pduOutletMeteredConfigEntry.setStatus("current")


class _PduOutletMeteredConfigIndex_Type(Integer32):
    """Custom type pduOutletMeteredConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletMeteredConfigIndex_Type.__name__ = "Integer32"
_PduOutletMeteredConfigIndex_Object = MibTableColumn
pduOutletMeteredConfigIndex = _PduOutletMeteredConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 7, 1, 1),
    _PduOutletMeteredConfigIndex_Type()
)
pduOutletMeteredConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutletMeteredConfigIndex.setStatus("current")
_PduOutletMeteredName_Type = DisplayString
_PduOutletMeteredName_Object = MibTableColumn
pduOutletMeteredName = _PduOutletMeteredName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 7, 1, 2),
    _PduOutletMeteredName_Type()
)
pduOutletMeteredName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletMeteredName.setStatus("current")
_PduOutletMeteredConfigLowerCriticalThreshold_Type = Unsigned32
_PduOutletMeteredConfigLowerCriticalThreshold_Object = MibTableColumn
pduOutletMeteredConfigLowerCriticalThreshold = _PduOutletMeteredConfigLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 7, 1, 3),
    _PduOutletMeteredConfigLowerCriticalThreshold_Type()
)
pduOutletMeteredConfigLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletMeteredConfigLowerCriticalThreshold.setStatus("current")
_PduOutletMeteredConfigLowerWarningThreshold_Type = Unsigned32
_PduOutletMeteredConfigLowerWarningThreshold_Object = MibTableColumn
pduOutletMeteredConfigLowerWarningThreshold = _PduOutletMeteredConfigLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 7, 1, 4),
    _PduOutletMeteredConfigLowerWarningThreshold_Type()
)
pduOutletMeteredConfigLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletMeteredConfigLowerWarningThreshold.setStatus("current")
_PduOutletMeteredConfigUpperCriticalThreshold_Type = Unsigned32
_PduOutletMeteredConfigUpperCriticalThreshold_Object = MibTableColumn
pduOutletMeteredConfigUpperCriticalThreshold = _PduOutletMeteredConfigUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 7, 1, 5),
    _PduOutletMeteredConfigUpperCriticalThreshold_Type()
)
pduOutletMeteredConfigUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletMeteredConfigUpperCriticalThreshold.setStatus("current")
_PduOutletMeteredConfigUpperWarningThreshold_Type = Unsigned32
_PduOutletMeteredConfigUpperWarningThreshold_Object = MibTableColumn
pduOutletMeteredConfigUpperWarningThreshold = _PduOutletMeteredConfigUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 7, 1, 6),
    _PduOutletMeteredConfigUpperWarningThreshold_Type()
)
pduOutletMeteredConfigUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletMeteredConfigUpperWarningThreshold.setStatus("current")
_PduOutletMeteredConfigAlarmResetThreshold_Type = Unsigned32
_PduOutletMeteredConfigAlarmResetThreshold_Object = MibTableColumn
pduOutletMeteredConfigAlarmResetThreshold = _PduOutletMeteredConfigAlarmResetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 7, 1, 7),
    _PduOutletMeteredConfigAlarmResetThreshold_Type()
)
pduOutletMeteredConfigAlarmResetThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletMeteredConfigAlarmResetThreshold.setStatus("current")
_PduOutletMeteredConfigAlarmStateChangeDelay_Type = Unsigned32
_PduOutletMeteredConfigAlarmStateChangeDelay_Object = MibTableColumn
pduOutletMeteredConfigAlarmStateChangeDelay = _PduOutletMeteredConfigAlarmStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 7, 1, 8),
    _PduOutletMeteredConfigAlarmStateChangeDelay_Type()
)
pduOutletMeteredConfigAlarmStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletMeteredConfigAlarmStateChangeDelay.setStatus("current")


class _PduOutletMeteredConfigEnabledThresholds_Type(Bits):
    """Custom type pduOutletMeteredConfigEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperWarning", 2),
          ("upperCritical", 3))
    )

_PduOutletMeteredConfigEnabledThresholds_Type.__name__ = "Bits"
_PduOutletMeteredConfigEnabledThresholds_Object = MibTableColumn
pduOutletMeteredConfigEnabledThresholds = _PduOutletMeteredConfigEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 7, 1, 9),
    _PduOutletMeteredConfigEnabledThresholds_Type()
)
pduOutletMeteredConfigEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletMeteredConfigEnabledThresholds.setStatus("current")
_PduOutletMeteredPropertiesTable_Object = MibTable
pduOutletMeteredPropertiesTable = _PduOutletMeteredPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 8)
)
if mibBuilder.loadTexts:
    pduOutletMeteredPropertiesTable.setStatus("current")
_PduOutletMeteredPropertiesEntry_Object = MibTableRow
pduOutletMeteredPropertiesEntry = _PduOutletMeteredPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 8, 1)
)
pduOutletMeteredPropertiesEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitPropertiesIndex"),
    (0, "CPDU-MIB", "pduOutletMeteredPropertiesIndex"),
)
if mibBuilder.loadTexts:
    pduOutletMeteredPropertiesEntry.setStatus("current")


class _PduOutletMeteredPropertiesIndex_Type(Integer32):
    """Custom type pduOutletMeteredPropertiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletMeteredPropertiesIndex_Type.__name__ = "Integer32"
_PduOutletMeteredPropertiesIndex_Object = MibTableColumn
pduOutletMeteredPropertiesIndex = _PduOutletMeteredPropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 8, 1, 1),
    _PduOutletMeteredPropertiesIndex_Type()
)
pduOutletMeteredPropertiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutletMeteredPropertiesIndex.setStatus("current")


class _PduOutletMeteredPropertiesNumber_Type(Integer32):
    """Custom type pduOutletMeteredPropertiesNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletMeteredPropertiesNumber_Type.__name__ = "Integer32"
_PduOutletMeteredPropertiesNumber_Object = MibTableColumn
pduOutletMeteredPropertiesNumber = _PduOutletMeteredPropertiesNumber_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 8, 1, 2),
    _PduOutletMeteredPropertiesNumber_Type()
)
pduOutletMeteredPropertiesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredPropertiesNumber.setStatus("current")
_PduOutletMeteredPropertiesName_Type = DisplayString
_PduOutletMeteredPropertiesName_Object = MibTableColumn
pduOutletMeteredPropertiesName = _PduOutletMeteredPropertiesName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 8, 1, 3),
    _PduOutletMeteredPropertiesName_Type()
)
pduOutletMeteredPropertiesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredPropertiesName.setStatus("current")


class _PduOutletMeteredPropertiesInputPhaseLayout_Type(Integer32):
    """Custom type pduOutletMeteredPropertiesInputPhaseLayout based on Integer32"""
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
        *(("seqPhase1ToNeutral", 1),
          ("seqPhase2ToNeutral", 2),
          ("seqPhase3ToNeutral", 3),
          ("seqPhase1ToPhase2", 4),
          ("seqPhase2ToPhase3", 5),
          ("seqPhase3ToPhase1", 6))
    )


_PduOutletMeteredPropertiesInputPhaseLayout_Type.__name__ = "Integer32"
_PduOutletMeteredPropertiesInputPhaseLayout_Object = MibTableColumn
pduOutletMeteredPropertiesInputPhaseLayout = _PduOutletMeteredPropertiesInputPhaseLayout_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 8, 1, 4),
    _PduOutletMeteredPropertiesInputPhaseLayout_Type()
)
pduOutletMeteredPropertiesInputPhaseLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredPropertiesInputPhaseLayout.setStatus("current")


class _PduOutletMeteredPropertiesCircuitBreaker_Type(Integer32):
    """Custom type pduOutletMeteredPropertiesCircuitBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletMeteredPropertiesCircuitBreaker_Type.__name__ = "Integer32"
_PduOutletMeteredPropertiesCircuitBreaker_Object = MibTableColumn
pduOutletMeteredPropertiesCircuitBreaker = _PduOutletMeteredPropertiesCircuitBreaker_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 8, 1, 5),
    _PduOutletMeteredPropertiesCircuitBreaker_Type()
)
pduOutletMeteredPropertiesCircuitBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredPropertiesCircuitBreaker.setStatus("current")
_PduOutletMeteredPropertiesPowerRating_Type = Integer32
_PduOutletMeteredPropertiesPowerRating_Object = MibTableColumn
pduOutletMeteredPropertiesPowerRating = _PduOutletMeteredPropertiesPowerRating_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 8, 1, 6),
    _PduOutletMeteredPropertiesPowerRating_Type()
)
pduOutletMeteredPropertiesPowerRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredPropertiesPowerRating.setStatus("current")
_PduOutletMeteredPropertiesCurrentRating_Type = Integer32
_PduOutletMeteredPropertiesCurrentRating_Object = MibTableColumn
pduOutletMeteredPropertiesCurrentRating = _PduOutletMeteredPropertiesCurrentRating_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 8, 1, 7),
    _PduOutletMeteredPropertiesCurrentRating_Type()
)
pduOutletMeteredPropertiesCurrentRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredPropertiesCurrentRating.setStatus("current")
_PduOutletMeteredStatusTable_Object = MibTable
pduOutletMeteredStatusTable = _PduOutletMeteredStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 9)
)
if mibBuilder.loadTexts:
    pduOutletMeteredStatusTable.setStatus("current")
_PduOutletMeteredStatusEntry_Object = MibTableRow
pduOutletMeteredStatusEntry = _PduOutletMeteredStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 9, 1)
)
pduOutletMeteredStatusEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitStatusIndex"),
    (0, "CPDU-MIB", "pduOutletMeteredStatusIndex"),
)
if mibBuilder.loadTexts:
    pduOutletMeteredStatusEntry.setStatus("current")


class _PduOutletMeteredStatusIndex_Type(Integer32):
    """Custom type pduOutletMeteredStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletMeteredStatusIndex_Type.__name__ = "Integer32"
_PduOutletMeteredStatusIndex_Object = MibTableColumn
pduOutletMeteredStatusIndex = _PduOutletMeteredStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 9, 1, 1),
    _PduOutletMeteredStatusIndex_Type()
)
pduOutletMeteredStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusIndex.setStatus("current")


class _PduOutletMeteredStatusNumber_Type(Integer32):
    """Custom type pduOutletMeteredStatusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletMeteredStatusNumber_Type.__name__ = "Integer32"
_PduOutletMeteredStatusNumber_Object = MibTableColumn
pduOutletMeteredStatusNumber = _PduOutletMeteredStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 9, 1, 2),
    _PduOutletMeteredStatusNumber_Type()
)
pduOutletMeteredStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusNumber.setStatus("current")
_PduOutletMeteredStatusName_Type = DisplayString
_PduOutletMeteredStatusName_Object = MibTableColumn
pduOutletMeteredStatusName = _PduOutletMeteredStatusName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 9, 1, 3),
    _PduOutletMeteredStatusName_Type()
)
pduOutletMeteredStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusName.setStatus("current")


class _PduOutletMeteredStatusLoadState_Type(Integer32):
    """Custom type pduOutletMeteredStatusLoadState based on Integer32"""
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
        *(("upperCritical", 1),
          ("upperWarning", 2),
          ("lowerWarning", 3),
          ("lowerCritical", 4),
          ("normal", 5))
    )


_PduOutletMeteredStatusLoadState_Type.__name__ = "Integer32"
_PduOutletMeteredStatusLoadState_Object = MibTableColumn
pduOutletMeteredStatusLoadState = _PduOutletMeteredStatusLoadState_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 9, 1, 4),
    _PduOutletMeteredStatusLoadState_Type()
)
pduOutletMeteredStatusLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusLoadState.setStatus("current")
_PduOutletMeteredStatusCurrent_Type = Integer32
_PduOutletMeteredStatusCurrent_Object = MibTableColumn
pduOutletMeteredStatusCurrent = _PduOutletMeteredStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 9, 1, 5),
    _PduOutletMeteredStatusCurrent_Type()
)
pduOutletMeteredStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusCurrent.setStatus("current")
_PduOutletMeteredStatusActivePower_Type = Integer32
_PduOutletMeteredStatusActivePower_Object = MibTableColumn
pduOutletMeteredStatusActivePower = _PduOutletMeteredStatusActivePower_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 9, 1, 6),
    _PduOutletMeteredStatusActivePower_Type()
)
pduOutletMeteredStatusActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusActivePower.setStatus("current")
_PduOutletMeteredStatusPowerFactor_Type = Integer32
_PduOutletMeteredStatusPowerFactor_Object = MibTableColumn
pduOutletMeteredStatusPowerFactor = _PduOutletMeteredStatusPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 9, 1, 7),
    _PduOutletMeteredStatusPowerFactor_Type()
)
pduOutletMeteredStatusPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusPowerFactor.setStatus("current")
_PduOutletMeteredStatusPeakPower_Type = Integer32
_PduOutletMeteredStatusPeakPower_Object = MibTableColumn
pduOutletMeteredStatusPeakPower = _PduOutletMeteredStatusPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 9, 1, 8),
    _PduOutletMeteredStatusPeakPower_Type()
)
pduOutletMeteredStatusPeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusPeakPower.setStatus("current")
_PduOutletMeteredStatusPeakPowerTimeStamp_Type = DisplayString
_PduOutletMeteredStatusPeakPowerTimeStamp_Object = MibTableColumn
pduOutletMeteredStatusPeakPowerTimeStamp = _PduOutletMeteredStatusPeakPowerTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 9, 1, 9),
    _PduOutletMeteredStatusPeakPowerTimeStamp_Type()
)
pduOutletMeteredStatusPeakPowerTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusPeakPowerTimeStamp.setStatus("current")
_PduOutletMeteredStatusPeakPowerStartTime_Type = DisplayString
_PduOutletMeteredStatusPeakPowerStartTime_Object = MibTableColumn
pduOutletMeteredStatusPeakPowerStartTime = _PduOutletMeteredStatusPeakPowerStartTime_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 9, 1, 10),
    _PduOutletMeteredStatusPeakPowerStartTime_Type()
)
pduOutletMeteredStatusPeakPowerStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusPeakPowerStartTime.setStatus("current")
_PduOutletMeteredStatusResettableEnergy_Type = Integer32
_PduOutletMeteredStatusResettableEnergy_Object = MibTableColumn
pduOutletMeteredStatusResettableEnergy = _PduOutletMeteredStatusResettableEnergy_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 5, 9, 1, 11),
    _PduOutletMeteredStatusResettableEnergy_Type()
)
pduOutletMeteredStatusResettableEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusResettableEnergy.setStatus("current")
_PduExternalSensor_ObjectIdentity = ObjectIdentity
pduExternalSensor = _PduExternalSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6)
)


class _PduExternalSensorTableSize_Type(Integer32):
    """Custom type pduExternalSensorTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduExternalSensorTableSize_Type.__name__ = "Integer32"
_PduExternalSensorTableSize_Object = MibScalar
pduExternalSensorTableSize = _PduExternalSensorTableSize_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 1),
    _PduExternalSensorTableSize_Type()
)
pduExternalSensorTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorTableSize.setStatus("current")
_PduExternalSensorNamePlateTable_Object = MibTable
pduExternalSensorNamePlateTable = _PduExternalSensorNamePlateTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 2)
)
if mibBuilder.loadTexts:
    pduExternalSensorNamePlateTable.setStatus("current")
_PduExternalSensorNamePlateEntry_Object = MibTableRow
pduExternalSensorNamePlateEntry = _PduExternalSensorNamePlateEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 2, 1)
)
pduExternalSensorNamePlateEntry.setIndexNames(
    (0, "CPDU-MIB", "pduNamePlateIndex"),
    (0, "CPDU-MIB", "pduExternalSensorNamePlateIndex"),
)
if mibBuilder.loadTexts:
    pduExternalSensorNamePlateEntry.setStatus("current")


class _PduExternalSensorNamePlateIndex_Type(Integer32):
    """Custom type pduExternalSensorNamePlateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduExternalSensorNamePlateIndex_Type.__name__ = "Integer32"
_PduExternalSensorNamePlateIndex_Object = MibTableColumn
pduExternalSensorNamePlateIndex = _PduExternalSensorNamePlateIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 2, 1, 1),
    _PduExternalSensorNamePlateIndex_Type()
)
pduExternalSensorNamePlateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduExternalSensorNamePlateIndex.setStatus("current")
_PduExternalSensorNamePlateName_Type = DisplayString
_PduExternalSensorNamePlateName_Object = MibTableColumn
pduExternalSensorNamePlateName = _PduExternalSensorNamePlateName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 2, 1, 2),
    _PduExternalSensorNamePlateName_Type()
)
pduExternalSensorNamePlateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorNamePlateName.setStatus("current")
_PduExternalSensorNamePlateDescription_Type = DisplayString
_PduExternalSensorNamePlateDescription_Object = MibTableColumn
pduExternalSensorNamePlateDescription = _PduExternalSensorNamePlateDescription_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 2, 1, 3),
    _PduExternalSensorNamePlateDescription_Type()
)
pduExternalSensorNamePlateDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorNamePlateDescription.setStatus("current")
_PduExternalSensorNamePlateLocation_Type = DisplayString
_PduExternalSensorNamePlateLocation_Object = MibTableColumn
pduExternalSensorNamePlateLocation = _PduExternalSensorNamePlateLocation_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 2, 1, 4),
    _PduExternalSensorNamePlateLocation_Type()
)
pduExternalSensorNamePlateLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorNamePlateLocation.setStatus("current")
_PduExternalSensorNamePlateSerialNumber_Type = DisplayString
_PduExternalSensorNamePlateSerialNumber_Object = MibTableColumn
pduExternalSensorNamePlateSerialNumber = _PduExternalSensorNamePlateSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 2, 1, 5),
    _PduExternalSensorNamePlateSerialNumber_Type()
)
pduExternalSensorNamePlateSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorNamePlateSerialNumber.setStatus("current")


class _PduExternalSensorNamePlateType_Type(Integer32):
    """Custom type pduExternalSensorNamePlateType based on Integer32"""
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
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("temperature", 1),
          ("humidity", 2),
          ("doorSwitch", 3),
          ("dryContact", 4),
          ("spotFluid", 5),
          ("ropeFluid", 6),
          ("smoke", 7),
          ("beacon", 8),
          ("airVelocity", 9),
          ("modbusAdapter", 17),
          ("hidAdapter", 18))
    )


_PduExternalSensorNamePlateType_Type.__name__ = "Integer32"
_PduExternalSensorNamePlateType_Object = MibTableColumn
pduExternalSensorNamePlateType = _PduExternalSensorNamePlateType_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 2, 1, 6),
    _PduExternalSensorNamePlateType_Type()
)
pduExternalSensorNamePlateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorNamePlateType.setStatus("current")


class _PduExternalSensorNamePlateUnits_Type(Integer32):
    """Custom type pduExternalSensorNamePlateUnits based on Integer32"""
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
        *(("logic", 0),
          ("degreeC", 1),
          ("degreeF", 2),
          ("percent", 3),
          ("mps", 4))
    )


_PduExternalSensorNamePlateUnits_Type.__name__ = "Integer32"
_PduExternalSensorNamePlateUnits_Object = MibTableColumn
pduExternalSensorNamePlateUnits = _PduExternalSensorNamePlateUnits_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 2, 1, 7),
    _PduExternalSensorNamePlateUnits_Type()
)
pduExternalSensorNamePlateUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorNamePlateUnits.setStatus("current")
_PduExternalSensorNamePlateIdentifier_Type = Integer32
_PduExternalSensorNamePlateIdentifier_Object = MibTableColumn
pduExternalSensorNamePlateIdentifier = _PduExternalSensorNamePlateIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 2, 1, 8),
    _PduExternalSensorNamePlateIdentifier_Type()
)
pduExternalSensorNamePlateIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorNamePlateIdentifier.setStatus("current")
_PduExternalSensorConfigTable_Object = MibTable
pduExternalSensorConfigTable = _PduExternalSensorConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 3)
)
if mibBuilder.loadTexts:
    pduExternalSensorConfigTable.setStatus("current")
_PduExternalSensorConfigEntry_Object = MibTableRow
pduExternalSensorConfigEntry = _PduExternalSensorConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 3, 1)
)
pduExternalSensorConfigEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitConfigIndex"),
    (0, "CPDU-MIB", "pduExternalSensorConfigIndex"),
)
if mibBuilder.loadTexts:
    pduExternalSensorConfigEntry.setStatus("current")


class _PduExternalSensorConfigIndex_Type(Integer32):
    """Custom type pduExternalSensorConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduExternalSensorConfigIndex_Type.__name__ = "Integer32"
_PduExternalSensorConfigIndex_Object = MibTableColumn
pduExternalSensorConfigIndex = _PduExternalSensorConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 3, 1, 1),
    _PduExternalSensorConfigIndex_Type()
)
pduExternalSensorConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduExternalSensorConfigIndex.setStatus("current")
_PduExternalSensorConfigLowerCriticalThreshold_Type = Unsigned32
_PduExternalSensorConfigLowerCriticalThreshold_Object = MibTableColumn
pduExternalSensorConfigLowerCriticalThreshold = _PduExternalSensorConfigLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 3, 1, 2),
    _PduExternalSensorConfigLowerCriticalThreshold_Type()
)
pduExternalSensorConfigLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorConfigLowerCriticalThreshold.setStatus("current")
_PduExternalSensorConfigLowerWarningThreshold_Type = Unsigned32
_PduExternalSensorConfigLowerWarningThreshold_Object = MibTableColumn
pduExternalSensorConfigLowerWarningThreshold = _PduExternalSensorConfigLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 3, 1, 3),
    _PduExternalSensorConfigLowerWarningThreshold_Type()
)
pduExternalSensorConfigLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorConfigLowerWarningThreshold.setStatus("current")
_PduExternalSensorConfigUpperCriticalThreshold_Type = Unsigned32
_PduExternalSensorConfigUpperCriticalThreshold_Object = MibTableColumn
pduExternalSensorConfigUpperCriticalThreshold = _PduExternalSensorConfigUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 3, 1, 4),
    _PduExternalSensorConfigUpperCriticalThreshold_Type()
)
pduExternalSensorConfigUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorConfigUpperCriticalThreshold.setStatus("current")
_PduExternalSensorConfigUpperWarningThreshold_Type = Unsigned32
_PduExternalSensorConfigUpperWarningThreshold_Object = MibTableColumn
pduExternalSensorConfigUpperWarningThreshold = _PduExternalSensorConfigUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 3, 1, 5),
    _PduExternalSensorConfigUpperWarningThreshold_Type()
)
pduExternalSensorConfigUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorConfigUpperWarningThreshold.setStatus("current")


class _PduExternalSensorConfigEnabledThresholds_Type(Bits):
    """Custom type pduExternalSensorConfigEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperWarning", 2),
          ("upperCritical", 3),
          ("binarySensorAlarm", 4))
    )

_PduExternalSensorConfigEnabledThresholds_Type.__name__ = "Bits"
_PduExternalSensorConfigEnabledThresholds_Object = MibTableColumn
pduExternalSensorConfigEnabledThresholds = _PduExternalSensorConfigEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 3, 1, 6),
    _PduExternalSensorConfigEnabledThresholds_Type()
)
pduExternalSensorConfigEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorConfigEnabledThresholds.setStatus("current")


class _PduExternalSensorConfigAlarmState_Type(Integer32):
    """Custom type pduExternalSensorConfigAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_PduExternalSensorConfigAlarmState_Type.__name__ = "Integer32"
_PduExternalSensorConfigAlarmState_Object = MibTableColumn
pduExternalSensorConfigAlarmState = _PduExternalSensorConfigAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 3, 1, 7),
    _PduExternalSensorConfigAlarmState_Type()
)
pduExternalSensorConfigAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorConfigAlarmState.setStatus("current")
_PduExternalSensorStatusTable_Object = MibTable
pduExternalSensorStatusTable = _PduExternalSensorStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 4)
)
if mibBuilder.loadTexts:
    pduExternalSensorStatusTable.setStatus("current")
_PduExternalSensorStatusEntry_Object = MibTableRow
pduExternalSensorStatusEntry = _PduExternalSensorStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 4, 1)
)
pduExternalSensorStatusEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitStatusIndex"),
    (0, "CPDU-MIB", "pduExternalSensorStatusIndex"),
)
if mibBuilder.loadTexts:
    pduExternalSensorStatusEntry.setStatus("current")


class _PduExternalSensorStatusIndex_Type(Integer32):
    """Custom type pduExternalSensorStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduExternalSensorStatusIndex_Type.__name__ = "Integer32"
_PduExternalSensorStatusIndex_Object = MibTableColumn
pduExternalSensorStatusIndex = _PduExternalSensorStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 4, 1, 1),
    _PduExternalSensorStatusIndex_Type()
)
pduExternalSensorStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduExternalSensorStatusIndex.setStatus("current")
_PduExternalSensorStatusName_Type = DisplayString
_PduExternalSensorStatusName_Object = MibTableColumn
pduExternalSensorStatusName = _PduExternalSensorStatusName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 4, 1, 2),
    _PduExternalSensorStatusName_Type()
)
pduExternalSensorStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorStatusName.setStatus("current")


class _PduExternalSensorStatusCommStatus_Type(Integer32):
    """Custom type pduExternalSensorStatusCommStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("commsOk", 2),
          ("commsLost", 3))
    )


_PduExternalSensorStatusCommStatus_Type.__name__ = "Integer32"
_PduExternalSensorStatusCommStatus_Object = MibTableColumn
pduExternalSensorStatusCommStatus = _PduExternalSensorStatusCommStatus_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 4, 1, 3),
    _PduExternalSensorStatusCommStatus_Type()
)
pduExternalSensorStatusCommStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorStatusCommStatus.setStatus("current")


class _PduExternalSensorStatusState_Type(Integer32):
    """Custom type pduExternalSensorStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 0),
          ("alarmed", 1),
          ("normal", 2),
          ("belowLowerCritical", 3),
          ("belowLowerWarning", 4),
          ("aboveUpperWarning", 5),
          ("aboveUpperCritical", 6))
    )


_PduExternalSensorStatusState_Type.__name__ = "Integer32"
_PduExternalSensorStatusState_Object = MibTableColumn
pduExternalSensorStatusState = _PduExternalSensorStatusState_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 4, 1, 4),
    _PduExternalSensorStatusState_Type()
)
pduExternalSensorStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorStatusState.setStatus("current")
_PduExternalSensorStatusValue_Type = Integer32
_PduExternalSensorStatusValue_Object = MibTableColumn
pduExternalSensorStatusValue = _PduExternalSensorStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 4, 1, 5),
    _PduExternalSensorStatusValue_Type()
)
pduExternalSensorStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorStatusValue.setStatus("current")
_PduExternalSensorStatusTimeStamp_Type = DisplayString
_PduExternalSensorStatusTimeStamp_Object = MibTableColumn
pduExternalSensorStatusTimeStamp = _PduExternalSensorStatusTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 4, 1, 6),
    _PduExternalSensorStatusTimeStamp_Type()
)
pduExternalSensorStatusTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorStatusTimeStamp.setStatus("current")
_PduExternalSensorStatusHighPrecisionValue_Type = Integer32
_PduExternalSensorStatusHighPrecisionValue_Object = MibTableColumn
pduExternalSensorStatusHighPrecisionValue = _PduExternalSensorStatusHighPrecisionValue_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 6, 4, 1, 7),
    _PduExternalSensorStatusHighPrecisionValue_Type()
)
pduExternalSensorStatusHighPrecisionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorStatusHighPrecisionValue.setStatus("current")
_PduSmartCabinet_ObjectIdentity = ObjectIdentity
pduSmartCabinet = _PduSmartCabinet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7)
)


class _PduUnitSmartCabinetTableSize_Type(Integer32):
    """Custom type pduUnitSmartCabinetTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduUnitSmartCabinetTableSize_Type.__name__ = "Integer32"
_PduUnitSmartCabinetTableSize_Object = MibScalar
pduUnitSmartCabinetTableSize = _PduUnitSmartCabinetTableSize_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 1),
    _PduUnitSmartCabinetTableSize_Type()
)
pduUnitSmartCabinetTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetTableSize.setStatus("current")
_PduUnitSmartCabinetTable_Object = MibTable
pduUnitSmartCabinetTable = _PduUnitSmartCabinetTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 2)
)
if mibBuilder.loadTexts:
    pduUnitSmartCabinetTable.setStatus("current")
_PduUnitSmartCabinetEntry_Object = MibTableRow
pduUnitSmartCabinetEntry = _PduUnitSmartCabinetEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 2, 1)
)
pduUnitSmartCabinetEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitSmartCabinetIndex"),
)
if mibBuilder.loadTexts:
    pduUnitSmartCabinetEntry.setStatus("current")


class _PduUnitSmartCabinetIndex_Type(Integer32):
    """Custom type pduUnitSmartCabinetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduUnitSmartCabinetIndex_Type.__name__ = "Integer32"
_PduUnitSmartCabinetIndex_Object = MibTableColumn
pduUnitSmartCabinetIndex = _PduUnitSmartCabinetIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 2, 1, 1),
    _PduUnitSmartCabinetIndex_Type()
)
pduUnitSmartCabinetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetIndex.setStatus("current")
_PduUnitSmartCabinetCardUserName_Type = DisplayString
_PduUnitSmartCabinetCardUserName_Object = MibTableColumn
pduUnitSmartCabinetCardUserName = _PduUnitSmartCabinetCardUserName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 2, 1, 2),
    _PduUnitSmartCabinetCardUserName_Type()
)
pduUnitSmartCabinetCardUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetCardUserName.setStatus("current")
_PduUnitSmartCabinetCardID_Type = Integer32
_PduUnitSmartCabinetCardID_Object = MibTableColumn
pduUnitSmartCabinetCardID = _PduUnitSmartCabinetCardID_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 2, 1, 3),
    _PduUnitSmartCabinetCardID_Type()
)
pduUnitSmartCabinetCardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetCardID.setStatus("current")
_PduUnitSmartCabinetTimestamp_Type = DisplayString
_PduUnitSmartCabinetTimestamp_Object = MibTableColumn
pduUnitSmartCabinetTimestamp = _PduUnitSmartCabinetTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 2, 1, 4),
    _PduUnitSmartCabinetTimestamp_Type()
)
pduUnitSmartCabinetTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetTimestamp.setStatus("current")


class _PduUnitSmartCabinetDoor_Type(Integer32):
    """Custom type pduUnitSmartCabinetDoor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hotAisle", 1),
          ("coldAisle", 2))
    )


_PduUnitSmartCabinetDoor_Type.__name__ = "Integer32"
_PduUnitSmartCabinetDoor_Object = MibTableColumn
pduUnitSmartCabinetDoor = _PduUnitSmartCabinetDoor_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 2, 1, 5),
    _PduUnitSmartCabinetDoor_Type()
)
pduUnitSmartCabinetDoor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetDoor.setStatus("current")
_PduUnitSmartCabinetControl_ObjectIdentity = ObjectIdentity
pduUnitSmartCabinetControl = _PduUnitSmartCabinetControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 3)
)
_PduUnitSmartCabinetControlUserName_Type = DisplayString
_PduUnitSmartCabinetControlUserName_Object = MibScalar
pduUnitSmartCabinetControlUserName = _PduUnitSmartCabinetControlUserName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 3, 1),
    _PduUnitSmartCabinetControlUserName_Type()
)
pduUnitSmartCabinetControlUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetControlUserName.setStatus("current")
_PduUnitSmartCabinetControlCardID_Type = Integer32
_PduUnitSmartCabinetControlCardID_Object = MibScalar
pduUnitSmartCabinetControlCardID = _PduUnitSmartCabinetControlCardID_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 3, 2),
    _PduUnitSmartCabinetControlCardID_Type()
)
pduUnitSmartCabinetControlCardID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetControlCardID.setStatus("current")
_PduUnitSmartCabinetControlTimestamp_Type = DisplayString
_PduUnitSmartCabinetControlTimestamp_Object = MibScalar
pduUnitSmartCabinetControlTimestamp = _PduUnitSmartCabinetControlTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 3, 3),
    _PduUnitSmartCabinetControlTimestamp_Type()
)
pduUnitSmartCabinetControlTimestamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetControlTimestamp.setStatus("current")


class _PduUnitSmartCabinetControlDoor_Type(Integer32):
    """Custom type pduUnitSmartCabinetControlDoor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hotAisle", 1),
          ("coldAisle", 2))
    )


_PduUnitSmartCabinetControlDoor_Type.__name__ = "Integer32"
_PduUnitSmartCabinetControlDoor_Object = MibScalar
pduUnitSmartCabinetControlDoor = _PduUnitSmartCabinetControlDoor_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 3, 4),
    _PduUnitSmartCabinetControlDoor_Type()
)
pduUnitSmartCabinetControlDoor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetControlDoor.setStatus("current")


class _PduUnitSmartCabinetCardIDEdit_Type(Integer32):
    """Custom type pduUnitSmartCabinetCardIDEdit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("grant", 0),
          ("remove", 1))
    )


_PduUnitSmartCabinetCardIDEdit_Type.__name__ = "Integer32"
_PduUnitSmartCabinetCardIDEdit_Object = MibScalar
pduUnitSmartCabinetCardIDEdit = _PduUnitSmartCabinetCardIDEdit_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 3, 5),
    _PduUnitSmartCabinetCardIDEdit_Type()
)
pduUnitSmartCabinetCardIDEdit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetCardIDEdit.setStatus("current")


class _PduUnitSmartCabinetColdAisleLockStatus_Type(Integer32):
    """Custom type pduUnitSmartCabinetColdAisleLockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlock", 0),
          ("lock", 1),
          ("notPresent", 2))
    )


_PduUnitSmartCabinetColdAisleLockStatus_Type.__name__ = "Integer32"
_PduUnitSmartCabinetColdAisleLockStatus_Object = MibScalar
pduUnitSmartCabinetColdAisleLockStatus = _PduUnitSmartCabinetColdAisleLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 3, 6),
    _PduUnitSmartCabinetColdAisleLockStatus_Type()
)
pduUnitSmartCabinetColdAisleLockStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetColdAisleLockStatus.setStatus("current")


class _PduUnitSmartCabinetHotAisleLockStatus_Type(Integer32):
    """Custom type pduUnitSmartCabinetHotAisleLockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlock", 0),
          ("lock", 1),
          ("notPresent", 2))
    )


_PduUnitSmartCabinetHotAisleLockStatus_Type.__name__ = "Integer32"
_PduUnitSmartCabinetHotAisleLockStatus_Object = MibScalar
pduUnitSmartCabinetHotAisleLockStatus = _PduUnitSmartCabinetHotAisleLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 3, 7),
    _PduUnitSmartCabinetHotAisleLockStatus_Type()
)
pduUnitSmartCabinetHotAisleLockStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetHotAisleLockStatus.setStatus("current")
_PduUnitSmartCabinetLockStateTable_Object = MibTable
pduUnitSmartCabinetLockStateTable = _PduUnitSmartCabinetLockStateTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 4)
)
if mibBuilder.loadTexts:
    pduUnitSmartCabinetLockStateTable.setStatus("current")
_PduUnitSmartCabinetLockStateEntry_Object = MibTableRow
pduUnitSmartCabinetLockStateEntry = _PduUnitSmartCabinetLockStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 4, 1)
)
pduUnitSmartCabinetLockStateEntry.setIndexNames(
    (0, "CPDU-MIB", "pduUnitSmartCabinetLockStateIndex"),
)
if mibBuilder.loadTexts:
    pduUnitSmartCabinetLockStateEntry.setStatus("current")


class _PduUnitSmartCabinetLockStateIndex_Type(Integer32):
    """Custom type pduUnitSmartCabinetLockStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduUnitSmartCabinetLockStateIndex_Type.__name__ = "Integer32"
_PduUnitSmartCabinetLockStateIndex_Object = MibTableColumn
pduUnitSmartCabinetLockStateIndex = _PduUnitSmartCabinetLockStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 4, 1, 1),
    _PduUnitSmartCabinetLockStateIndex_Type()
)
pduUnitSmartCabinetLockStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetLockStateIndex.setStatus("current")


class _PduUnitSmartCabinetColdAisleLockState_Type(Integer32):
    """Custom type pduUnitSmartCabinetColdAisleLockState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlock", 0),
          ("lock", 1),
          ("notPresent", 2))
    )


_PduUnitSmartCabinetColdAisleLockState_Type.__name__ = "Integer32"
_PduUnitSmartCabinetColdAisleLockState_Object = MibTableColumn
pduUnitSmartCabinetColdAisleLockState = _PduUnitSmartCabinetColdAisleLockState_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 4, 1, 2),
    _PduUnitSmartCabinetColdAisleLockState_Type()
)
pduUnitSmartCabinetColdAisleLockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetColdAisleLockState.setStatus("current")


class _PduUnitSmartCabinetHotAisleLockState_Type(Integer32):
    """Custom type pduUnitSmartCabinetHotAisleLockState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlock", 0),
          ("lock", 1),
          ("notPresent", 2))
    )


_PduUnitSmartCabinetHotAisleLockState_Type.__name__ = "Integer32"
_PduUnitSmartCabinetHotAisleLockState_Object = MibTableColumn
pduUnitSmartCabinetHotAisleLockState = _PduUnitSmartCabinetHotAisleLockState_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 4, 1, 3),
    _PduUnitSmartCabinetHotAisleLockState_Type()
)
pduUnitSmartCabinetHotAisleLockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetHotAisleLockState.setStatus("current")
_PduUnitSmartCabinetColdAisleLockLabel_Type = DisplayString
_PduUnitSmartCabinetColdAisleLockLabel_Object = MibTableColumn
pduUnitSmartCabinetColdAisleLockLabel = _PduUnitSmartCabinetColdAisleLockLabel_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 4, 1, 4),
    _PduUnitSmartCabinetColdAisleLockLabel_Type()
)
pduUnitSmartCabinetColdAisleLockLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetColdAisleLockLabel.setStatus("current")
_PduUnitSmartCabinetHotAisleLockLabel_Type = DisplayString
_PduUnitSmartCabinetHotAisleLockLabel_Object = MibTableColumn
pduUnitSmartCabinetHotAisleLockLabel = _PduUnitSmartCabinetHotAisleLockLabel_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 7, 4, 1, 5),
    _PduUnitSmartCabinetHotAisleLockLabel_Type()
)
pduUnitSmartCabinetHotAisleLockLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetHotAisleLockLabel.setStatus("current")
_PduTraps_ObjectIdentity = ObjectIdentity
pduTraps = _PduTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8)
)
_TrapsInfo_ObjectIdentity = ObjectIdentity
trapsInfo = _TrapsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 1)
)
_TrapsInfoTable_Object = MibTable
trapsInfoTable = _TrapsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 1, 1)
)
if mibBuilder.loadTexts:
    trapsInfoTable.setStatus("current")
_TrapsInfoEntry_Object = MibTableRow
trapsInfoEntry = _TrapsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 1, 1, 1)
)
trapsInfoEntry.setIndexNames(
    (0, "CPDU-MIB", "trapsInfoIndex"),
)
if mibBuilder.loadTexts:
    trapsInfoEntry.setStatus("current")


class _TrapsInfoIndex_Type(Integer32):
    """Custom type trapsInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_TrapsInfoIndex_Type.__name__ = "Integer32"
_TrapsInfoIndex_Object = MibTableColumn
trapsInfoIndex = _TrapsInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 1, 1, 1, 1),
    _TrapsInfoIndex_Type()
)
trapsInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapsInfoIndex.setStatus("current")
_UserName_Type = DisplayString
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 1, 1, 1, 2),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("current")
_UserUpdated_Type = DisplayString
_UserUpdated_Object = MibTableColumn
userUpdated = _UserUpdated_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 1, 1, 1, 3),
    _UserUpdated_Type()
)
userUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userUpdated.setStatus("current")
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibTableColumn
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 1, 1, 1, 4),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_RoleUpdated_Type = DisplayString
_RoleUpdated_Object = MibTableColumn
roleUpdated = _RoleUpdated_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 1, 1, 1, 5),
    _RoleUpdated_Type()
)
roleUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roleUpdated.setStatus("current")
_SmtpRecipients_Type = DisplayString
_SmtpRecipients_Object = MibTableColumn
smtpRecipients = _SmtpRecipients_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 1, 1, 1, 6),
    _SmtpRecipients_Type()
)
smtpRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpRecipients.setStatus("current")
_SmtpServer_Type = DisplayString
_SmtpServer_Object = MibTableColumn
smtpServer = _SmtpServer_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 1, 1, 1, 7),
    _SmtpServer_Type()
)
smtpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpServer.setStatus("current")
_PduIndex_Type = Integer32
_PduIndex_Object = MibScalar
pduIndex = _PduIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 1, 2),
    _PduIndex_Type()
)
pduIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pduIndex.setStatus("current")
_ExternalSensorIndex_Type = Integer32
_ExternalSensorIndex_Object = MibScalar
externalSensorIndex = _ExternalSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 1, 3),
    _ExternalSensorIndex_Type()
)
externalSensorIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    externalSensorIndex.setStatus("current")


class _ServerPing_Type(Integer32):
    """Custom type serverPing based on Integer32"""
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
        *(("pingEnable", 1),
          ("pingDisable", 2),
          ("serverReachable", 3),
          ("serverNotReachable", 4))
    )


_ServerPing_Type.__name__ = "Integer32"
_ServerPing_Object = MibScalar
serverPing = _ServerPing_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 1, 4),
    _ServerPing_Type()
)
serverPing.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    serverPing.setStatus("current")


class _UsbDevice_Type(Integer32):
    """Custom type usbDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_UsbDevice_Type.__name__ = "Integer32"
_UsbDevice_Object = MibScalar
usbDevice = _UsbDevice_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 1, 5),
    _UsbDevice_Type()
)
usbDevice.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    usbDevice.setStatus("current")
_ErrorDescription_Type = DisplayString
_ErrorDescription_Object = MibScalar
errorDescription = _ErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 1, 6),
    _ErrorDescription_Type()
)
errorDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    errorDescription.setStatus("current")


class _Cascading_Type(Integer32):
    """Custom type cascading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_Cascading_Type.__name__ = "Integer32"
_Cascading_Object = MibScalar
cascading = _Cascading_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 1, 7),
    _Cascading_Type()
)
cascading.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cascading.setStatus("current")


class _SystemCommunication_Type(Integer32):
    """Custom type systemCommunication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("lost", 2))
    )


_SystemCommunication_Type.__name__ = "Integer32"
_SystemCommunication_Object = MibScalar
systemCommunication = _SystemCommunication_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 1, 8),
    _SystemCommunication_Type()
)
systemCommunication.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    systemCommunication.setStatus("current")
_TrapCode_Type = Integer32
_TrapCode_Object = MibScalar
trapCode = _TrapCode_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 1, 9),
    _TrapCode_Type()
)
trapCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCode.setStatus("mandatory")


class _TrapDescription_Type(DisplayString):
    """Custom type trapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapDescription_Type.__name__ = "DisplayString"
_TrapDescription_Object = MibScalar
trapDescription = _TrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 1, 10),
    _TrapDescription_Type()
)
trapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDescription.setStatus("mandatory")
_PduEhandle_ObjectIdentity = ObjectIdentity
pduEhandle = _PduEhandle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9)
)
_PduEhandleTable_Object = MibTable
pduEhandleTable = _PduEhandleTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 1)
)
if mibBuilder.loadTexts:
    pduEhandleTable.setStatus("mandatory")
_PduEhandleEntry_Object = MibTableRow
pduEhandleEntry = _PduEhandleEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 1, 1)
)
pduEhandleEntry.setIndexNames(
    (0, "CPDU-MIB", "pduEhandleIndex"),
)
if mibBuilder.loadTexts:
    pduEhandleEntry.setStatus("mandatory")


class _PduEhandleIndex_Type(Integer32):
    """Custom type pduEhandleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_PduEhandleIndex_Type.__name__ = "Integer32"
_PduEhandleIndex_Object = MibTableColumn
pduEhandleIndex = _PduEhandleIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 1, 1, 1),
    _PduEhandleIndex_Type()
)
pduEhandleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEhandleIndex.setStatus("mandatory")


class _PduEhandleAisle_Type(Integer32):
    """Custom type pduEhandleAisle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hot", 1),
          ("cold", 2))
    )


_PduEhandleAisle_Type.__name__ = "Integer32"
_PduEhandleAisle_Object = MibTableColumn
pduEhandleAisle = _PduEhandleAisle_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 1, 1, 2),
    _PduEhandleAisle_Type()
)
pduEhandleAisle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEhandleAisle.setStatus("mandatory")


class _PduEhandleHandleOperation_Type(Integer32):
    """Custom type pduEhandleHandleOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlock", 1),
          ("lock", 2))
    )


_PduEhandleHandleOperation_Type.__name__ = "Integer32"
_PduEhandleHandleOperation_Object = MibTableColumn
pduEhandleHandleOperation = _PduEhandleHandleOperation_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 1, 1, 3),
    _PduEhandleHandleOperation_Type()
)
pduEhandleHandleOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEhandleHandleOperation.setStatus("mandatory")
_PduEhandleFwVer_Type = DisplayString
_PduEhandleFwVer_Object = MibTableColumn
pduEhandleFwVer = _PduEhandleFwVer_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 1, 1, 4),
    _PduEhandleFwVer_Type()
)
pduEhandleFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEhandleFwVer.setStatus("mandatory")


class _PduEhandleMechanicalLock_Type(Integer32):
    """Custom type pduEhandleMechanicalLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlock", 1),
          ("lock", 2))
    )


_PduEhandleMechanicalLock_Type.__name__ = "Integer32"
_PduEhandleMechanicalLock_Object = MibTableColumn
pduEhandleMechanicalLock = _PduEhandleMechanicalLock_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 1, 1, 5),
    _PduEhandleMechanicalLock_Type()
)
pduEhandleMechanicalLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEhandleMechanicalLock.setStatus("mandatory")
_PduEhandleSerial_Type = DisplayString
_PduEhandleSerial_Object = MibTableColumn
pduEhandleSerial = _PduEhandleSerial_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 1, 1, 6),
    _PduEhandleSerial_Type()
)
pduEhandleSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEhandleSerial.setStatus("mandatory")
_PduEhandleHwVer_Type = DisplayString
_PduEhandleHwVer_Object = MibTableColumn
pduEhandleHwVer = _PduEhandleHwVer_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 1, 1, 7),
    _PduEhandleHwVer_Type()
)
pduEhandleHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEhandleHwVer.setStatus("mandatory")
_PduEhandleAutoLockTime_Type = Integer32
_PduEhandleAutoLockTime_Object = MibTableColumn
pduEhandleAutoLockTime = _PduEhandleAutoLockTime_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 1, 1, 8),
    _PduEhandleAutoLockTime_Type()
)
pduEhandleAutoLockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEhandleAutoLockTime.setStatus("mandatory")
_PduEhandleDoorOpenTime_Type = Integer32
_PduEhandleDoorOpenTime_Object = MibTableColumn
pduEhandleDoorOpenTime = _PduEhandleDoorOpenTime_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 1, 1, 9),
    _PduEhandleDoorOpenTime_Type()
)
pduEhandleDoorOpenTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEhandleDoorOpenTime.setStatus("mandatory")
_PduEhandleMaxDoorOpenTime_Type = Integer32
_PduEhandleMaxDoorOpenTime_Object = MibTableColumn
pduEhandleMaxDoorOpenTime = _PduEhandleMaxDoorOpenTime_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 1, 1, 10),
    _PduEhandleMaxDoorOpenTime_Type()
)
pduEhandleMaxDoorOpenTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEhandleMaxDoorOpenTime.setStatus("mandatory")
_PduEhandleUserPinLength_Type = Integer32
_PduEhandleUserPinLength_Object = MibTableColumn
pduEhandleUserPinLength = _PduEhandleUserPinLength_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 1, 1, 11),
    _PduEhandleUserPinLength_Type()
)
pduEhandleUserPinLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEhandleUserPinLength.setStatus("mandatory")


class _PduEhandleUserPinMode_Type(Integer32):
    """Custom type pduEhandleUserPinMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("visible", 1),
          ("hidden", 2))
    )


_PduEhandleUserPinMode_Type.__name__ = "Integer32"
_PduEhandleUserPinMode_Object = MibTableColumn
pduEhandleUserPinMode = _PduEhandleUserPinMode_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 1, 1, 12),
    _PduEhandleUserPinMode_Type()
)
pduEhandleUserPinMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEhandleUserPinMode.setStatus("mandatory")


class _PduEhandleAisleControl_Type(Integer32):
    """Custom type pduEhandleAisleControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("combined", 1),
          ("standalone", 2))
    )


_PduEhandleAisleControl_Type.__name__ = "Integer32"
_PduEhandleAisleControl_Object = MibTableColumn
pduEhandleAisleControl = _PduEhandleAisleControl_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 1, 1, 13),
    _PduEhandleAisleControl_Type()
)
pduEhandleAisleControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEhandleAisleControl.setStatus("mandatory")
_PduEhandleControlTable_Object = MibTable
pduEhandleControlTable = _PduEhandleControlTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 2)
)
if mibBuilder.loadTexts:
    pduEhandleControlTable.setStatus("mandatory")
_PduEhandleControlEntry_Object = MibTableRow
pduEhandleControlEntry = _PduEhandleControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 2, 1)
)
pduEhandleControlEntry.setIndexNames(
    (0, "CPDU-MIB", "pduEhandleControlIndex"),
)
if mibBuilder.loadTexts:
    pduEhandleControlEntry.setStatus("mandatory")


class _PduEhandleControlIndex_Type(Integer32):
    """Custom type pduEhandleControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_PduEhandleControlIndex_Type.__name__ = "Integer32"
_PduEhandleControlIndex_Object = MibTableColumn
pduEhandleControlIndex = _PduEhandleControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 2, 1, 1),
    _PduEhandleControlIndex_Type()
)
pduEhandleControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEhandleControlIndex.setStatus("mandatory")
_PduEhandleControlUserName_Type = DisplayString
_PduEhandleControlUserName_Object = MibTableColumn
pduEhandleControlUserName = _PduEhandleControlUserName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 2, 1, 2),
    _PduEhandleControlUserName_Type()
)
pduEhandleControlUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEhandleControlUserName.setStatus("mandatory")
_PduEhandleControlCardIdStr_Type = DisplayString
_PduEhandleControlCardIdStr_Object = MibTableColumn
pduEhandleControlCardIdStr = _PduEhandleControlCardIdStr_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 2, 1, 3),
    _PduEhandleControlCardIdStr_Type()
)
pduEhandleControlCardIdStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEhandleControlCardIdStr.setStatus("mandatory")
_PduEhandleControlTimestamp_Type = DisplayString
_PduEhandleControlTimestamp_Object = MibTableColumn
pduEhandleControlTimestamp = _PduEhandleControlTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 2, 1, 4),
    _PduEhandleControlTimestamp_Type()
)
pduEhandleControlTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduEhandleControlTimestamp.setStatus("mandatory")


class _PduEhandleControlCardAisle_Type(Integer32):
    """Custom type pduEhandleControlCardAisle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hot", 1),
          ("cold", 2),
          ("both", 3))
    )


_PduEhandleControlCardAisle_Type.__name__ = "Integer32"
_PduEhandleControlCardAisle_Object = MibTableColumn
pduEhandleControlCardAisle = _PduEhandleControlCardAisle_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 2, 1, 5),
    _PduEhandleControlCardAisle_Type()
)
pduEhandleControlCardAisle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEhandleControlCardAisle.setStatus("mandatory")
_PduEhandleControlStartTime_Type = DisplayString
_PduEhandleControlStartTime_Object = MibTableColumn
pduEhandleControlStartTime = _PduEhandleControlStartTime_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 2, 1, 6),
    _PduEhandleControlStartTime_Type()
)
pduEhandleControlStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEhandleControlStartTime.setStatus("mandatory")
_PduEhandleControlExpireTime_Type = DisplayString
_PduEhandleControlExpireTime_Object = MibTableColumn
pduEhandleControlExpireTime = _PduEhandleControlExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 2, 1, 7),
    _PduEhandleControlExpireTime_Type()
)
pduEhandleControlExpireTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEhandleControlExpireTime.setStatus("mandatory")


class _PduEhandleControlTempUser_Type(Integer32):
    """Custom type pduEhandleControlTempUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_PduEhandleControlTempUser_Type.__name__ = "Integer32"
_PduEhandleControlTempUser_Object = MibTableColumn
pduEhandleControlTempUser = _PduEhandleControlTempUser_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 2, 1, 8),
    _PduEhandleControlTempUser_Type()
)
pduEhandleControlTempUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEhandleControlTempUser.setStatus("mandatory")
_PduEhandleControlPin_Type = DisplayString
_PduEhandleControlPin_Object = MibTableColumn
pduEhandleControlPin = _PduEhandleControlPin_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 9, 2, 1, 9),
    _PduEhandleControlPin_Type()
)
pduEhandleControlPin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduEhandleControlPin.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 1)
)
trapCritical.setObjects(
      *(("CPDU-MIB", "trapCode"),
        ("CPDU-MIB", "trapDescription"),
        ("CPDU-MIB", "sysDescr"),
        ("CPDU-MIB", "pduNamePlateIPAddress"))
)
if mibBuilder.loadTexts:
    trapCritical.setStatus(
        "current"
    )

trapWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 2)
)
trapWarning.setObjects(
      *(("CPDU-MIB", "trapCode"),
        ("CPDU-MIB", "trapDescription"),
        ("CPDU-MIB", "sysDescr"),
        ("CPDU-MIB", "pduNamePlateIPAddress"))
)
if mibBuilder.loadTexts:
    trapWarning.setStatus(
        "current"
    )

trapInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 3)
)
trapInformation.setObjects(
      *(("CPDU-MIB", "trapCode"),
        ("CPDU-MIB", "trapDescription"),
        ("CPDU-MIB", "sysDescr"),
        ("CPDU-MIB", "pdug5IPv4Address"))
)
if mibBuilder.loadTexts:
    trapInformation.setStatus(
        "current"
    )

trapCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 4)
)
trapCleared.setObjects(
      *(("CPDU-MIB", "trapCode"),
        ("CPDU-MIB", "trapDescription"),
        ("CPDU-MIB", "sysDescr"),
        ("CPDU-MIB", "pduNamePlateIPAddress"))
)
if mibBuilder.loadTexts:
    trapCleared.setStatus(
        "current"
    )

trapTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 318, 1, 1, 32, 8, 5)
)
trapTest.setObjects(
      *(("CPDU-MIB", "trapCode"),
        ("CPDU-MIB", "trapDescription"),
        ("CPDU-MIB", "sysDescr"),
        ("CPDU-MIB", "pduNamePlateIPAddress"))
)
if mibBuilder.loadTexts:
    trapTest.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPDU-MIB",
    **{"apc": apc,
       "products": products,
       "hardware": hardware,
       "cPDU": cPDU,
       "pduNamePlate": pduNamePlate,
       "pduNamePlateTableSize": pduNamePlateTableSize,
       "pduNamePlateTable": pduNamePlateTable,
       "pduNamePlateEntry": pduNamePlateEntry,
       "pduNamePlateIndex": pduNamePlateIndex,
       "pduNamePlateName": pduNamePlateName,
       "pduNamePlateLocation": pduNamePlateLocation,
       "pduNamePlateInetAddressType": pduNamePlateInetAddressType,
       "pduNamePlateIPAddress": pduNamePlateIPAddress,
       "pduNamePlateInetNetMask": pduNamePlateInetNetMask,
       "pduNamePlateInetGateway": pduNamePlateInetGateway,
       "pduNamePlateMACAddress": pduNamePlateMACAddress,
       "pduNamePlateUTCTimeOffset": pduNamePlateUTCTimeOffset,
       "pduNamePlateModelNumber": pduNamePlateModelNumber,
       "pduNamePlatePartNumber": pduNamePlatePartNumber,
       "pduNamePlateSerialNumber": pduNamePlateSerialNumber,
       "pduNamePlateDateofManufacture": pduNamePlateDateofManufacture,
       "pduNamePlateFirmwareVersion": pduNamePlateFirmwareVersion,
       "pduNamePlateFirmwareVersionTimeStamp": pduNamePlateFirmwareVersionTimeStamp,
       "pduNamePlateType": pduNamePlateType,
       "pduUnit": pduUnit,
       "pduUnitTableSize": pduUnitTableSize,
       "pduUnitConfigTable": pduUnitConfigTable,
       "pduUnitConfigEntry": pduUnitConfigEntry,
       "pduUnitConfigIndex": pduUnitConfigIndex,
       "pduUnitConfigName": pduUnitConfigName,
       "pduUnitConfigLocation": pduUnitConfigLocation,
       "pduUnitConfigDisplayOrientation": pduUnitConfigDisplayOrientation,
       "pduUnitConfigOledDisplayControl": pduUnitConfigOledDisplayControl,
       "pduUnitConfigColdstartDelay": pduUnitConfigColdstartDelay,
       "pduUnitConfigGlobalOutletStateOnStartup": pduUnitConfigGlobalOutletStateOnStartup,
       "pduUnitConfigLowerCriticalThreshold": pduUnitConfigLowerCriticalThreshold,
       "pduUnitConfigLowerWarningThreshold": pduUnitConfigLowerWarningThreshold,
       "pduUnitConfigUpperCriticalThreshold": pduUnitConfigUpperCriticalThreshold,
       "pduUnitConfigUpperWarningThreshold": pduUnitConfigUpperWarningThreshold,
       "pduUnitConfigAlarmResetThreshold": pduUnitConfigAlarmResetThreshold,
       "pduUnitConfigAlarmStateChangeDelay": pduUnitConfigAlarmStateChangeDelay,
       "pduUnitConfigEnabledThresholds": pduUnitConfigEnabledThresholds,
       "pduUnitConfigPeakPowerReset": pduUnitConfigPeakPowerReset,
       "pduUnitConfigEnergyReset": pduUnitConfigEnergyReset,
       "pduUnitConfigOutletPeakPowerReset": pduUnitConfigOutletPeakPowerReset,
       "pduUnitConfigOutletEnergyReset": pduUnitConfigOutletEnergyReset,
       "pduUnitConfigSsh": pduUnitConfigSsh,
       "pduUnitConfigResetNetworkManagementCard": pduUnitConfigResetNetworkManagementCard,
       "pduUnitPropertiesTable": pduUnitPropertiesTable,
       "pduUnitPropertiesEntry": pduUnitPropertiesEntry,
       "pduUnitPropertiesIndex": pduUnitPropertiesIndex,
       "pduUnitPropertiesName": pduUnitPropertiesName,
       "pduUnitPropertiesOutletCount": pduUnitPropertiesOutletCount,
       "pduUnitPropertiesSwitchedOutletCount": pduUnitPropertiesSwitchedOutletCount,
       "pduUnitPropertiesMeteredOutletCount": pduUnitPropertiesMeteredOutletCount,
       "pduUnitPropertiesInputPhaseCount": pduUnitPropertiesInputPhaseCount,
       "pduUnitPropertiesCircuitBreakerCount": pduUnitPropertiesCircuitBreakerCount,
       "pduUnitPropertiesMaxExternalSensorCount": pduUnitPropertiesMaxExternalSensorCount,
       "pduUnitPropertiesConnExternalSensorCount": pduUnitPropertiesConnExternalSensorCount,
       "pduUnitPropertiesRatedVoltage": pduUnitPropertiesRatedVoltage,
       "pduUnitPropertiesRatedMaxCurrent": pduUnitPropertiesRatedMaxCurrent,
       "pduUnitPropertiesRatedFrequency": pduUnitPropertiesRatedFrequency,
       "pduUnitPropertiesRatedPower": pduUnitPropertiesRatedPower,
       "pduUnitPropertiesOrientation": pduUnitPropertiesOrientation,
       "pduUnitPropertiesOutletLayout": pduUnitPropertiesOutletLayout,
       "pduUnitPropertiesCascadeMemberType": pduUnitPropertiesCascadeMemberType,
       "pduUnitStatusTable": pduUnitStatusTable,
       "pduUnitStatusEntry": pduUnitStatusEntry,
       "pduUnitStatusIndex": pduUnitStatusIndex,
       "pduUnitStatusName": pduUnitStatusName,
       "pduUnitStatusLoadState": pduUnitStatusLoadState,
       "pduUnitStatusActivePower": pduUnitStatusActivePower,
       "pduUnitStatusApparentPower": pduUnitStatusApparentPower,
       "pduUnitStatusPeakPower": pduUnitStatusPeakPower,
       "pduUnitStatusPeakPowerTimestamp": pduUnitStatusPeakPowerTimestamp,
       "pduUnitStatusPeakPowerStartTime": pduUnitStatusPeakPowerStartTime,
       "pduUnitStatusEnergy": pduUnitStatusEnergy,
       "pduUnitStatusResettableEnergy": pduUnitStatusResettableEnergy,
       "pduUnitStatusEnergyStartTime": pduUnitStatusEnergyStartTime,
       "pduUnitStatusOutletsEnergyStartTime": pduUnitStatusOutletsEnergyStartTime,
       "pduUnitPsTable": pduUnitPsTable,
       "pduUnitPsEntry": pduUnitPsEntry,
       "pduUnitPsIndex": pduUnitPsIndex,
       "pduUnitPsSupportUpstreamStatus": pduUnitPsSupportUpstreamStatus,
       "pduUnitPsSupportDownstreamStatus": pduUnitPsSupportDownstreamStatus,
       "pduUnitPsOptMode": pduUnitPsOptMode,
       "pduInputPhase": pduInputPhase,
       "pduInputPhaseTableSize": pduInputPhaseTableSize,
       "pduInputPhaseConfigTable": pduInputPhaseConfigTable,
       "pduInputPhaseConfigEntry": pduInputPhaseConfigEntry,
       "pduInputPhaseConfigIndex": pduInputPhaseConfigIndex,
       "pduInputPhaseConfigCount": pduInputPhaseConfigCount,
       "pduInputPhaseConfigOverloadRestriction": pduInputPhaseConfigOverloadRestriction,
       "pduInputPhaseConfigCurrentLowerCriticalThreshold": pduInputPhaseConfigCurrentLowerCriticalThreshold,
       "pduInputPhaseConfigCurrentLowerWarningThreshold": pduInputPhaseConfigCurrentLowerWarningThreshold,
       "pduInputPhaseConfigCurrentUpperCriticalThreshold": pduInputPhaseConfigCurrentUpperCriticalThreshold,
       "pduInputPhaseConfigCurrentUpperWarningThreshold": pduInputPhaseConfigCurrentUpperWarningThreshold,
       "pduInputPhaseConfigVoltageLowerCriticalThreshold": pduInputPhaseConfigVoltageLowerCriticalThreshold,
       "pduInputPhaseConfigVoltageLowerWarningThreshold": pduInputPhaseConfigVoltageLowerWarningThreshold,
       "pduInputPhaseConfigVoltageUpperCriticalThreshold": pduInputPhaseConfigVoltageUpperCriticalThreshold,
       "pduInputPhaseConfigVoltageUpperWarningThreshold": pduInputPhaseConfigVoltageUpperWarningThreshold,
       "pduInputPhaseConfigCurrentAlarmResetThreshold": pduInputPhaseConfigCurrentAlarmResetThreshold,
       "pduInputPhaseConfigCurrentAlarmStateChangeDelay": pduInputPhaseConfigCurrentAlarmStateChangeDelay,
       "pduInputPhaseConfigCurrentEnabledThresholds": pduInputPhaseConfigCurrentEnabledThresholds,
       "pduInputPhaseConfigVoltageAlarmResetThreshold": pduInputPhaseConfigVoltageAlarmResetThreshold,
       "pduInputPhaseConfigVoltageAlarmStateChangeDelay": pduInputPhaseConfigVoltageAlarmStateChangeDelay,
       "pduInputPhaseConfigVoltageEnabledThresholds": pduInputPhaseConfigVoltageEnabledThresholds,
       "pduInputPhasePropertiesTable": pduInputPhasePropertiesTable,
       "pduInputPhasePropertiesEntry": pduInputPhasePropertiesEntry,
       "pduInputPhasePropertiesIndex": pduInputPhasePropertiesIndex,
       "pduInputPhasePropertiesCount": pduInputPhasePropertiesCount,
       "pduInputPhaseStatusTable": pduInputPhaseStatusTable,
       "pduInputPhaseStatusEntry": pduInputPhaseStatusEntry,
       "pduInputPhaseStatusIndex": pduInputPhaseStatusIndex,
       "pduInputPhaseStatusCount": pduInputPhaseStatusCount,
       "pduInputPhaseStatusCurrentState": pduInputPhaseStatusCurrentState,
       "pduInputPhaseStatusVoltageState": pduInputPhaseStatusVoltageState,
       "pduInputPhaseStatusCurrent": pduInputPhaseStatusCurrent,
       "pduInputPhaseStatusVoltage": pduInputPhaseStatusVoltage,
       "pduInputPhaseStatusActivePower": pduInputPhaseStatusActivePower,
       "pduInputPhaseStatusApparentPower": pduInputPhaseStatusApparentPower,
       "pduInputPhaseStatusPowerFactor": pduInputPhaseStatusPowerFactor,
       "pduCircuitBreaker": pduCircuitBreaker,
       "pduCircuitBreakerTableSize": pduCircuitBreakerTableSize,
       "pduCircuitBreakerConfigTable": pduCircuitBreakerConfigTable,
       "pduCircuitBreakerConfigEntry": pduCircuitBreakerConfigEntry,
       "pduCircuitBreakerConfigIndex": pduCircuitBreakerConfigIndex,
       "pduCircuitBreakerConfigCount": pduCircuitBreakerConfigCount,
       "pduCircuitBreakerName": pduCircuitBreakerName,
       "pduCircuitBreakerConfigOverloadRestriction": pduCircuitBreakerConfigOverloadRestriction,
       "pduCircuitBreakerConfigLowerCriticalThreshold": pduCircuitBreakerConfigLowerCriticalThreshold,
       "pduCircuitBreakerConfigLowerWarningThreshold": pduCircuitBreakerConfigLowerWarningThreshold,
       "pduCircuitBreakerConfigUpperCriticalThreshold": pduCircuitBreakerConfigUpperCriticalThreshold,
       "pduCircuitBreakerConfigUpperWarningThreshold": pduCircuitBreakerConfigUpperWarningThreshold,
       "pduCircuitBreakerConfigAlarmResetThreshold": pduCircuitBreakerConfigAlarmResetThreshold,
       "pduCircuitBreakerConfigAlarmStateChangeDelay": pduCircuitBreakerConfigAlarmStateChangeDelay,
       "pduCircuitBreakerConfigEnabledThresholds": pduCircuitBreakerConfigEnabledThresholds,
       "pduCircuitBreakerPropertiesTable": pduCircuitBreakerPropertiesTable,
       "pduCircuitBreakerPropertiesEntry": pduCircuitBreakerPropertiesEntry,
       "pduCircuitBreakerPropertiesIndex": pduCircuitBreakerPropertiesIndex,
       "pduCircuitBreakerPropertiesCount": pduCircuitBreakerPropertiesCount,
       "pduCircuitBreakerPropertiesInputLayout": pduCircuitBreakerPropertiesInputLayout,
       "pduCircuitBreakerPropertiesCurrentRating": pduCircuitBreakerPropertiesCurrentRating,
       "pduCircuitBreakerStatusTable": pduCircuitBreakerStatusTable,
       "pduCircuitBreakerStatusEntry": pduCircuitBreakerStatusEntry,
       "pduCircuitBreakerStatusIndex": pduCircuitBreakerStatusIndex,
       "pduCircuitBreakerStatusCount": pduCircuitBreakerStatusCount,
       "pduCircuitBreakerLabel": pduCircuitBreakerLabel,
       "pduCircuitBreakerStatusLoadState": pduCircuitBreakerStatusLoadState,
       "pduCircuitBreakerStatusCurrent": pduCircuitBreakerStatusCurrent,
       "pduOutlet": pduOutlet,
       "pduOutletSwitchedTableSize": pduOutletSwitchedTableSize,
       "pduOutletSwitchedConfigTable": pduOutletSwitchedConfigTable,
       "pduOutletSwitchedConfigEntry": pduOutletSwitchedConfigEntry,
       "pduOutletSwitchedConfigIndex": pduOutletSwitchedConfigIndex,
       "pduOutletSwitchedName": pduOutletSwitchedName,
       "pduOutletSwitchedStateOnStartup": pduOutletSwitchedStateOnStartup,
       "pduOutletSwitchedConfigPowerOnTime": pduOutletSwitchedConfigPowerOnTime,
       "pduOutletSwitchedConfigPowerOffTime": pduOutletSwitchedConfigPowerOffTime,
       "pduOutletSwitchedConfigRebootDuration": pduOutletSwitchedConfigRebootDuration,
       "pduOutletSwitchedPropertiesTable": pduOutletSwitchedPropertiesTable,
       "pduOutletSwitchedPropertiesEntry": pduOutletSwitchedPropertiesEntry,
       "pduOutletSwitchedPropertiesIndex": pduOutletSwitchedPropertiesIndex,
       "pduOutletSwitchedPropertiesNumber": pduOutletSwitchedPropertiesNumber,
       "pduOutletSwitchedPropertiesName": pduOutletSwitchedPropertiesName,
       "pduOutletSwitchedPropertiesInputPhaseLayout": pduOutletSwitchedPropertiesInputPhaseLayout,
       "pduOutletSwitchedPropertiesCircuitBreaker": pduOutletSwitchedPropertiesCircuitBreaker,
       "pduOutletSwitchedPropertiesCurrentRating": pduOutletSwitchedPropertiesCurrentRating,
       "pduOutletSwitchedStatusTable": pduOutletSwitchedStatusTable,
       "pduOutletSwitchedStatusEntry": pduOutletSwitchedStatusEntry,
       "pduOutletSwitchedStatusIndex": pduOutletSwitchedStatusIndex,
       "pduOutletSwitchedStatusNumber": pduOutletSwitchedStatusNumber,
       "pduOutletSwitchedStatusName": pduOutletSwitchedStatusName,
       "pduOutletSwitchedStatusState": pduOutletSwitchedStatusState,
       "pduOutletSwitchedControlTable": pduOutletSwitchedControlTable,
       "pduOutletSwitchedControlEntry": pduOutletSwitchedControlEntry,
       "pduOutletSwitchedControlIndex": pduOutletSwitchedControlIndex,
       "pduOutletSwitchedControlNumber": pduOutletSwitchedControlNumber,
       "pduOutletSwitchedControlName": pduOutletSwitchedControlName,
       "pduOutletSwitchedControlCommand": pduOutletSwitchedControlCommand,
       "pduOutletMeteredTableSize": pduOutletMeteredTableSize,
       "pduOutletMeteredConfigTable": pduOutletMeteredConfigTable,
       "pduOutletMeteredConfigEntry": pduOutletMeteredConfigEntry,
       "pduOutletMeteredConfigIndex": pduOutletMeteredConfigIndex,
       "pduOutletMeteredName": pduOutletMeteredName,
       "pduOutletMeteredConfigLowerCriticalThreshold": pduOutletMeteredConfigLowerCriticalThreshold,
       "pduOutletMeteredConfigLowerWarningThreshold": pduOutletMeteredConfigLowerWarningThreshold,
       "pduOutletMeteredConfigUpperCriticalThreshold": pduOutletMeteredConfigUpperCriticalThreshold,
       "pduOutletMeteredConfigUpperWarningThreshold": pduOutletMeteredConfigUpperWarningThreshold,
       "pduOutletMeteredConfigAlarmResetThreshold": pduOutletMeteredConfigAlarmResetThreshold,
       "pduOutletMeteredConfigAlarmStateChangeDelay": pduOutletMeteredConfigAlarmStateChangeDelay,
       "pduOutletMeteredConfigEnabledThresholds": pduOutletMeteredConfigEnabledThresholds,
       "pduOutletMeteredPropertiesTable": pduOutletMeteredPropertiesTable,
       "pduOutletMeteredPropertiesEntry": pduOutletMeteredPropertiesEntry,
       "pduOutletMeteredPropertiesIndex": pduOutletMeteredPropertiesIndex,
       "pduOutletMeteredPropertiesNumber": pduOutletMeteredPropertiesNumber,
       "pduOutletMeteredPropertiesName": pduOutletMeteredPropertiesName,
       "pduOutletMeteredPropertiesInputPhaseLayout": pduOutletMeteredPropertiesInputPhaseLayout,
       "pduOutletMeteredPropertiesCircuitBreaker": pduOutletMeteredPropertiesCircuitBreaker,
       "pduOutletMeteredPropertiesPowerRating": pduOutletMeteredPropertiesPowerRating,
       "pduOutletMeteredPropertiesCurrentRating": pduOutletMeteredPropertiesCurrentRating,
       "pduOutletMeteredStatusTable": pduOutletMeteredStatusTable,
       "pduOutletMeteredStatusEntry": pduOutletMeteredStatusEntry,
       "pduOutletMeteredStatusIndex": pduOutletMeteredStatusIndex,
       "pduOutletMeteredStatusNumber": pduOutletMeteredStatusNumber,
       "pduOutletMeteredStatusName": pduOutletMeteredStatusName,
       "pduOutletMeteredStatusLoadState": pduOutletMeteredStatusLoadState,
       "pduOutletMeteredStatusCurrent": pduOutletMeteredStatusCurrent,
       "pduOutletMeteredStatusActivePower": pduOutletMeteredStatusActivePower,
       "pduOutletMeteredStatusPowerFactor": pduOutletMeteredStatusPowerFactor,
       "pduOutletMeteredStatusPeakPower": pduOutletMeteredStatusPeakPower,
       "pduOutletMeteredStatusPeakPowerTimeStamp": pduOutletMeteredStatusPeakPowerTimeStamp,
       "pduOutletMeteredStatusPeakPowerStartTime": pduOutletMeteredStatusPeakPowerStartTime,
       "pduOutletMeteredStatusResettableEnergy": pduOutletMeteredStatusResettableEnergy,
       "pduExternalSensor": pduExternalSensor,
       "pduExternalSensorTableSize": pduExternalSensorTableSize,
       "pduExternalSensorNamePlateTable": pduExternalSensorNamePlateTable,
       "pduExternalSensorNamePlateEntry": pduExternalSensorNamePlateEntry,
       "pduExternalSensorNamePlateIndex": pduExternalSensorNamePlateIndex,
       "pduExternalSensorNamePlateName": pduExternalSensorNamePlateName,
       "pduExternalSensorNamePlateDescription": pduExternalSensorNamePlateDescription,
       "pduExternalSensorNamePlateLocation": pduExternalSensorNamePlateLocation,
       "pduExternalSensorNamePlateSerialNumber": pduExternalSensorNamePlateSerialNumber,
       "pduExternalSensorNamePlateType": pduExternalSensorNamePlateType,
       "pduExternalSensorNamePlateUnits": pduExternalSensorNamePlateUnits,
       "pduExternalSensorNamePlateIdentifier": pduExternalSensorNamePlateIdentifier,
       "pduExternalSensorConfigTable": pduExternalSensorConfigTable,
       "pduExternalSensorConfigEntry": pduExternalSensorConfigEntry,
       "pduExternalSensorConfigIndex": pduExternalSensorConfigIndex,
       "pduExternalSensorConfigLowerCriticalThreshold": pduExternalSensorConfigLowerCriticalThreshold,
       "pduExternalSensorConfigLowerWarningThreshold": pduExternalSensorConfigLowerWarningThreshold,
       "pduExternalSensorConfigUpperCriticalThreshold": pduExternalSensorConfigUpperCriticalThreshold,
       "pduExternalSensorConfigUpperWarningThreshold": pduExternalSensorConfigUpperWarningThreshold,
       "pduExternalSensorConfigEnabledThresholds": pduExternalSensorConfigEnabledThresholds,
       "pduExternalSensorConfigAlarmState": pduExternalSensorConfigAlarmState,
       "pduExternalSensorStatusTable": pduExternalSensorStatusTable,
       "pduExternalSensorStatusEntry": pduExternalSensorStatusEntry,
       "pduExternalSensorStatusIndex": pduExternalSensorStatusIndex,
       "pduExternalSensorStatusName": pduExternalSensorStatusName,
       "pduExternalSensorStatusCommStatus": pduExternalSensorStatusCommStatus,
       "pduExternalSensorStatusState": pduExternalSensorStatusState,
       "pduExternalSensorStatusValue": pduExternalSensorStatusValue,
       "pduExternalSensorStatusTimeStamp": pduExternalSensorStatusTimeStamp,
       "pduExternalSensorStatusHighPrecisionValue": pduExternalSensorStatusHighPrecisionValue,
       "pduSmartCabinet": pduSmartCabinet,
       "pduUnitSmartCabinetTableSize": pduUnitSmartCabinetTableSize,
       "pduUnitSmartCabinetTable": pduUnitSmartCabinetTable,
       "pduUnitSmartCabinetEntry": pduUnitSmartCabinetEntry,
       "pduUnitSmartCabinetIndex": pduUnitSmartCabinetIndex,
       "pduUnitSmartCabinetCardUserName": pduUnitSmartCabinetCardUserName,
       "pduUnitSmartCabinetCardID": pduUnitSmartCabinetCardID,
       "pduUnitSmartCabinetTimestamp": pduUnitSmartCabinetTimestamp,
       "pduUnitSmartCabinetDoor": pduUnitSmartCabinetDoor,
       "pduUnitSmartCabinetControl": pduUnitSmartCabinetControl,
       "pduUnitSmartCabinetControlUserName": pduUnitSmartCabinetControlUserName,
       "pduUnitSmartCabinetControlCardID": pduUnitSmartCabinetControlCardID,
       "pduUnitSmartCabinetControlTimestamp": pduUnitSmartCabinetControlTimestamp,
       "pduUnitSmartCabinetControlDoor": pduUnitSmartCabinetControlDoor,
       "pduUnitSmartCabinetCardIDEdit": pduUnitSmartCabinetCardIDEdit,
       "pduUnitSmartCabinetColdAisleLockStatus": pduUnitSmartCabinetColdAisleLockStatus,
       "pduUnitSmartCabinetHotAisleLockStatus": pduUnitSmartCabinetHotAisleLockStatus,
       "pduUnitSmartCabinetLockStateTable": pduUnitSmartCabinetLockStateTable,
       "pduUnitSmartCabinetLockStateEntry": pduUnitSmartCabinetLockStateEntry,
       "pduUnitSmartCabinetLockStateIndex": pduUnitSmartCabinetLockStateIndex,
       "pduUnitSmartCabinetColdAisleLockState": pduUnitSmartCabinetColdAisleLockState,
       "pduUnitSmartCabinetHotAisleLockState": pduUnitSmartCabinetHotAisleLockState,
       "pduUnitSmartCabinetColdAisleLockLabel": pduUnitSmartCabinetColdAisleLockLabel,
       "pduUnitSmartCabinetHotAisleLockLabel": pduUnitSmartCabinetHotAisleLockLabel,
       "pduTraps": pduTraps,
       "trapsInfo": trapsInfo,
       "trapCritical": trapCritical,
       "trapsInfoTable": trapsInfoTable,
       "trapsInfoEntry": trapsInfoEntry,
       "trapsInfoIndex": trapsInfoIndex,
       "userName": userName,
       "userUpdated": userUpdated,
       "firmwareVersion": firmwareVersion,
       "roleUpdated": roleUpdated,
       "smtpRecipients": smtpRecipients,
       "smtpServer": smtpServer,
       "pduIndex": pduIndex,
       "externalSensorIndex": externalSensorIndex,
       "serverPing": serverPing,
       "usbDevice": usbDevice,
       "errorDescription": errorDescription,
       "cascading": cascading,
       "systemCommunication": systemCommunication,
       "trapCode": trapCode,
       "trapDescription": trapDescription,
       "trapWarning": trapWarning,
       "trapInformation": trapInformation,
       "trapCleared": trapCleared,
       "trapTest": trapTest,
       "pduEhandle": pduEhandle,
       "pduEhandleTable": pduEhandleTable,
       "pduEhandleEntry": pduEhandleEntry,
       "pduEhandleIndex": pduEhandleIndex,
       "pduEhandleAisle": pduEhandleAisle,
       "pduEhandleHandleOperation": pduEhandleHandleOperation,
       "pduEhandleFwVer": pduEhandleFwVer,
       "pduEhandleMechanicalLock": pduEhandleMechanicalLock,
       "pduEhandleSerial": pduEhandleSerial,
       "pduEhandleHwVer": pduEhandleHwVer,
       "pduEhandleAutoLockTime": pduEhandleAutoLockTime,
       "pduEhandleDoorOpenTime": pduEhandleDoorOpenTime,
       "pduEhandleMaxDoorOpenTime": pduEhandleMaxDoorOpenTime,
       "pduEhandleUserPinLength": pduEhandleUserPinLength,
       "pduEhandleUserPinMode": pduEhandleUserPinMode,
       "pduEhandleAisleControl": pduEhandleAisleControl,
       "pduEhandleControlTable": pduEhandleControlTable,
       "pduEhandleControlEntry": pduEhandleControlEntry,
       "pduEhandleControlIndex": pduEhandleControlIndex,
       "pduEhandleControlUserName": pduEhandleControlUserName,
       "pduEhandleControlCardIdStr": pduEhandleControlCardIdStr,
       "pduEhandleControlTimestamp": pduEhandleControlTimestamp,
       "pduEhandleControlCardAisle": pduEhandleControlCardAisle,
       "pduEhandleControlStartTime": pduEhandleControlStartTime,
       "pduEhandleControlExpireTime": pduEhandleControlExpireTime,
       "pduEhandleControlTempUser": pduEhandleControlTempUser,
       "pduEhandleControlPin": pduEhandleControlPin}
)
