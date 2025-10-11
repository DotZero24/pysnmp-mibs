# SNMP MIB module (QTECH-ENTITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-ENTITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:48 2025
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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

qtechEntityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21)
)
if mibBuilder.loadTexts:
    qtechEntityMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechDeviceMIBObjects_ObjectIdentity = ObjectIdentity
qtechDeviceMIBObjects = _QtechDeviceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1)
)
_QtechDeviceMaxNumber_Type = Integer32
_QtechDeviceMaxNumber_Object = MibScalar
qtechDeviceMaxNumber = _QtechDeviceMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 1),
    _QtechDeviceMaxNumber_Type()
)
qtechDeviceMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDeviceMaxNumber.setStatus("current")
_QtechDeviceInfoTable_Object = MibTable
qtechDeviceInfoTable = _QtechDeviceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 2)
)
if mibBuilder.loadTexts:
    qtechDeviceInfoTable.setStatus("current")
_QtechDeviceInfoEntry_Object = MibTableRow
qtechDeviceInfoEntry = _QtechDeviceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 2, 1)
)
qtechDeviceInfoEntry.setIndexNames(
    (0, "QTECH-ENTITY-MIB", "qtechDeviceInfoIndex"),
)
if mibBuilder.loadTexts:
    qtechDeviceInfoEntry.setStatus("current")
_QtechDeviceInfoIndex_Type = Integer32
_QtechDeviceInfoIndex_Object = MibTableColumn
qtechDeviceInfoIndex = _QtechDeviceInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 2, 1, 1),
    _QtechDeviceInfoIndex_Type()
)
qtechDeviceInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDeviceInfoIndex.setStatus("current")


class _QtechDeviceInfoDescr_Type(DisplayString):
    """Custom type qtechDeviceInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechDeviceInfoDescr_Type.__name__ = "DisplayString"
_QtechDeviceInfoDescr_Object = MibTableColumn
qtechDeviceInfoDescr = _QtechDeviceInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 2, 1, 2),
    _QtechDeviceInfoDescr_Type()
)
qtechDeviceInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDeviceInfoDescr.setStatus("current")
_QtechDeviceInfoSlotNumber_Type = Integer32
_QtechDeviceInfoSlotNumber_Object = MibTableColumn
qtechDeviceInfoSlotNumber = _QtechDeviceInfoSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 2, 1, 3),
    _QtechDeviceInfoSlotNumber_Type()
)
qtechDeviceInfoSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDeviceInfoSlotNumber.setStatus("current")


class _QtechDevicePowerStatus_Type(Integer32):
    """Custom type qtechDevicePowerStatus based on Integer32"""
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
        *(("rpsNoLink", 1),
          ("rpsLinkAndNoPower", 2),
          ("rpsLinkAndReadyForPower", 3),
          ("rpsLinkAndPower", 4))
    )


_QtechDevicePowerStatus_Type.__name__ = "Integer32"
_QtechDevicePowerStatus_Object = MibTableColumn
qtechDevicePowerStatus = _QtechDevicePowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 2, 1, 4),
    _QtechDevicePowerStatus_Type()
)
qtechDevicePowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDevicePowerStatus.setStatus("current")
_QtechDeviceMacAddress_Type = MacAddress
_QtechDeviceMacAddress_Object = MibTableColumn
qtechDeviceMacAddress = _QtechDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 2, 1, 5),
    _QtechDeviceMacAddress_Type()
)
qtechDeviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDeviceMacAddress.setStatus("current")


class _QtechDevicePriority_Type(Integer32):
    """Custom type qtechDevicePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_QtechDevicePriority_Type.__name__ = "Integer32"
_QtechDevicePriority_Object = MibTableColumn
qtechDevicePriority = _QtechDevicePriority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 2, 1, 6),
    _QtechDevicePriority_Type()
)
qtechDevicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDevicePriority.setStatus("current")


class _QtechDeviceAlias_Type(DisplayString):
    """Custom type qtechDeviceAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechDeviceAlias_Type.__name__ = "DisplayString"
_QtechDeviceAlias_Object = MibTableColumn
qtechDeviceAlias = _QtechDeviceAlias_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 2, 1, 7),
    _QtechDeviceAlias_Type()
)
qtechDeviceAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDeviceAlias.setStatus("current")


class _QtechDeviceSWVersion_Type(DisplayString):
    """Custom type qtechDeviceSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechDeviceSWVersion_Type.__name__ = "DisplayString"
_QtechDeviceSWVersion_Object = MibTableColumn
qtechDeviceSWVersion = _QtechDeviceSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 2, 1, 8),
    _QtechDeviceSWVersion_Type()
)
qtechDeviceSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDeviceSWVersion.setStatus("current")


class _QtechDeviceHWVersion_Type(DisplayString):
    """Custom type qtechDeviceHWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechDeviceHWVersion_Type.__name__ = "DisplayString"
_QtechDeviceHWVersion_Object = MibTableColumn
qtechDeviceHWVersion = _QtechDeviceHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 2, 1, 9),
    _QtechDeviceHWVersion_Type()
)
qtechDeviceHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDeviceHWVersion.setStatus("current")


class _QtechDeviceSerialNumber_Type(DisplayString):
    """Custom type qtechDeviceSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechDeviceSerialNumber_Type.__name__ = "DisplayString"
_QtechDeviceSerialNumber_Object = MibTableColumn
qtechDeviceSerialNumber = _QtechDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 2, 1, 10),
    _QtechDeviceSerialNumber_Type()
)
qtechDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDeviceSerialNumber.setStatus("current")
_QtechDeviceOid_Type = ObjectIdentifier
_QtechDeviceOid_Object = MibTableColumn
qtechDeviceOid = _QtechDeviceOid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 2, 1, 11),
    _QtechDeviceOid_Type()
)
qtechDeviceOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDeviceOid.setStatus("current")
_QtechSlotInfoTable_Object = MibTable
qtechSlotInfoTable = _QtechSlotInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 3)
)
if mibBuilder.loadTexts:
    qtechSlotInfoTable.setStatus("current")
_QtechSlotInfoEntry_Object = MibTableRow
qtechSlotInfoEntry = _QtechSlotInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 3, 1)
)
qtechSlotInfoEntry.setIndexNames(
    (0, "QTECH-ENTITY-MIB", "qtechSlotInfoDeviceIndex"),
    (0, "QTECH-ENTITY-MIB", "qtechSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    qtechSlotInfoEntry.setStatus("current")
_QtechSlotInfoDeviceIndex_Type = Integer32
_QtechSlotInfoDeviceIndex_Object = MibTableColumn
qtechSlotInfoDeviceIndex = _QtechSlotInfoDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 3, 1, 1),
    _QtechSlotInfoDeviceIndex_Type()
)
qtechSlotInfoDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSlotInfoDeviceIndex.setStatus("current")
_QtechSlotInfoIndex_Type = Integer32
_QtechSlotInfoIndex_Object = MibTableColumn
qtechSlotInfoIndex = _QtechSlotInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 3, 1, 2),
    _QtechSlotInfoIndex_Type()
)
qtechSlotInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSlotInfoIndex.setStatus("current")
_QtechSlotModuleInfoDescr_Type = DisplayString
_QtechSlotModuleInfoDescr_Object = MibTableColumn
qtechSlotModuleInfoDescr = _QtechSlotModuleInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 3, 1, 3),
    _QtechSlotModuleInfoDescr_Type()
)
qtechSlotModuleInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSlotModuleInfoDescr.setStatus("current")
_QtechSlotInfoPortNumber_Type = Integer32
_QtechSlotInfoPortNumber_Object = MibTableColumn
qtechSlotInfoPortNumber = _QtechSlotInfoPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 3, 1, 4),
    _QtechSlotInfoPortNumber_Type()
)
qtechSlotInfoPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSlotInfoPortNumber.setStatus("current")
_QtechSlotInfoPortMaxNumber_Type = Integer32
_QtechSlotInfoPortMaxNumber_Object = MibTableColumn
qtechSlotInfoPortMaxNumber = _QtechSlotInfoPortMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 3, 1, 5),
    _QtechSlotInfoPortMaxNumber_Type()
)
qtechSlotInfoPortMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSlotInfoPortMaxNumber.setStatus("current")


class _QtechSlotInfoDesc_Type(DisplayString):
    """Custom type qtechSlotInfoDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechSlotInfoDesc_Type.__name__ = "DisplayString"
_QtechSlotInfoDesc_Object = MibTableColumn
qtechSlotInfoDesc = _QtechSlotInfoDesc_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 3, 1, 6),
    _QtechSlotInfoDesc_Type()
)
qtechSlotInfoDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSlotInfoDesc.setStatus("current")


class _QtechSlotConfigModuleInfoDescr_Type(DisplayString):
    """Custom type qtechSlotConfigModuleInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechSlotConfigModuleInfoDescr_Type.__name__ = "DisplayString"
_QtechSlotConfigModuleInfoDescr_Object = MibTableColumn
qtechSlotConfigModuleInfoDescr = _QtechSlotConfigModuleInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 3, 1, 7),
    _QtechSlotConfigModuleInfoDescr_Type()
)
qtechSlotConfigModuleInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSlotConfigModuleInfoDescr.setStatus("current")
_QtechSlotUserStatus_Type = Integer32
_QtechSlotUserStatus_Object = MibTableColumn
qtechSlotUserStatus = _QtechSlotUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 3, 1, 8),
    _QtechSlotUserStatus_Type()
)
qtechSlotUserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSlotUserStatus.setStatus("current")
_QtechSlotSoftwareStatus_Type = Integer32
_QtechSlotSoftwareStatus_Object = MibTableColumn
qtechSlotSoftwareStatus = _QtechSlotSoftwareStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 3, 1, 9),
    _QtechSlotSoftwareStatus_Type()
)
qtechSlotSoftwareStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSlotSoftwareStatus.setStatus("current")


class _QtechSlotSerialNumber_Type(DisplayString):
    """Custom type qtechSlotSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechSlotSerialNumber_Type.__name__ = "DisplayString"
_QtechSlotSerialNumber_Object = MibTableColumn
qtechSlotSerialNumber = _QtechSlotSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 3, 1, 10),
    _QtechSlotSerialNumber_Type()
)
qtechSlotSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSlotSerialNumber.setStatus("current")


class _QtechSlotHWVersion_Type(DisplayString):
    """Custom type qtechSlotHWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechSlotHWVersion_Type.__name__ = "DisplayString"
_QtechSlotHWVersion_Object = MibTableColumn
qtechSlotHWVersion = _QtechSlotHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 3, 1, 11),
    _QtechSlotHWVersion_Type()
)
qtechSlotHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSlotHWVersion.setStatus("current")
_QtechModuleTempStateTable_Object = MibTable
qtechModuleTempStateTable = _QtechModuleTempStateTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 4)
)
if mibBuilder.loadTexts:
    qtechModuleTempStateTable.setStatus("current")
_QtechModuleTempStateEntry_Object = MibTableRow
qtechModuleTempStateEntry = _QtechModuleTempStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 4, 1)
)
qtechModuleTempStateEntry.setIndexNames(
    (0, "QTECH-ENTITY-MIB", "qtechModuleTempStateDeviceIndex"),
    (0, "QTECH-ENTITY-MIB", "qtechModuleTempStateIndex"),
)
if mibBuilder.loadTexts:
    qtechModuleTempStateEntry.setStatus("current")
_QtechModuleTempStateDeviceIndex_Type = Integer32
_QtechModuleTempStateDeviceIndex_Object = MibTableColumn
qtechModuleTempStateDeviceIndex = _QtechModuleTempStateDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 4, 1, 1),
    _QtechModuleTempStateDeviceIndex_Type()
)
qtechModuleTempStateDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechModuleTempStateDeviceIndex.setStatus("current")
_QtechModuleTempStateIndex_Type = Integer32
_QtechModuleTempStateIndex_Object = MibTableColumn
qtechModuleTempStateIndex = _QtechModuleTempStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 4, 1, 2),
    _QtechModuleTempStateIndex_Type()
)
qtechModuleTempStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechModuleTempStateIndex.setStatus("current")


class _QtechModuleTempState_Type(Integer32):
    """Custom type qtechModuleTempState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tempNormal", 1),
          ("tempWarning", 2))
    )


_QtechModuleTempState_Type.__name__ = "Integer32"
_QtechModuleTempState_Object = MibTableColumn
qtechModuleTempState = _QtechModuleTempState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 4, 1, 3),
    _QtechModuleTempState_Type()
)
qtechModuleTempState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechModuleTempState.setStatus("current")
_QtechPowerStateTable_Object = MibTable
qtechPowerStateTable = _QtechPowerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 5)
)
if mibBuilder.loadTexts:
    qtechPowerStateTable.setStatus("current")
_QtechPowerStateEntry_Object = MibTableRow
qtechPowerStateEntry = _QtechPowerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 5, 1)
)
qtechPowerStateEntry.setIndexNames(
    (0, "QTECH-ENTITY-MIB", "qtechPowerStateDeviceIndex"),
    (0, "QTECH-ENTITY-MIB", "qtechPowerStateIndex"),
)
if mibBuilder.loadTexts:
    qtechPowerStateEntry.setStatus("current")
_QtechPowerStateDeviceIndex_Type = Integer32
_QtechPowerStateDeviceIndex_Object = MibTableColumn
qtechPowerStateDeviceIndex = _QtechPowerStateDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 5, 1, 1),
    _QtechPowerStateDeviceIndex_Type()
)
qtechPowerStateDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPowerStateDeviceIndex.setStatus("current")
_QtechPowerStateIndex_Type = Integer32
_QtechPowerStateIndex_Object = MibTableColumn
qtechPowerStateIndex = _QtechPowerStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 5, 1, 2),
    _QtechPowerStateIndex_Type()
)
qtechPowerStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPowerStateIndex.setStatus("current")


class _QtechPowerState_Type(Integer32):
    """Custom type qtechPowerState based on Integer32"""
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
        *(("noLink", 1),
          ("linkAndNoPower", 2),
          ("linkAndReadyForPower", 3),
          ("linkAndPower", 4),
          ("linkAndPowerAbnormal", 5))
    )


_QtechPowerState_Type.__name__ = "Integer32"
_QtechPowerState_Object = MibTableColumn
qtechPowerState = _QtechPowerState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 5, 1, 3),
    _QtechPowerState_Type()
)
qtechPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPowerState.setStatus("current")


class _QtechPowerStatePowerDescr_Type(DisplayString):
    """Custom type qtechPowerStatePowerDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechPowerStatePowerDescr_Type.__name__ = "DisplayString"
_QtechPowerStatePowerDescr_Object = MibTableColumn
qtechPowerStatePowerDescr = _QtechPowerStatePowerDescr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 5, 1, 4),
    _QtechPowerStatePowerDescr_Type()
)
qtechPowerStatePowerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPowerStatePowerDescr.setStatus("current")
_QtechFanStateTable_Object = MibTable
qtechFanStateTable = _QtechFanStateTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 6)
)
if mibBuilder.loadTexts:
    qtechFanStateTable.setStatus("current")
_QtechFanStateEntry_Object = MibTableRow
qtechFanStateEntry = _QtechFanStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 6, 1)
)
qtechFanStateEntry.setIndexNames(
    (0, "QTECH-ENTITY-MIB", "qtechFanStateDeviceIndex"),
    (0, "QTECH-ENTITY-MIB", "qtechFanStateIndex"),
)
if mibBuilder.loadTexts:
    qtechFanStateEntry.setStatus("current")
_QtechFanStateDeviceIndex_Type = Integer32
_QtechFanStateDeviceIndex_Object = MibTableColumn
qtechFanStateDeviceIndex = _QtechFanStateDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 6, 1, 1),
    _QtechFanStateDeviceIndex_Type()
)
qtechFanStateDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFanStateDeviceIndex.setStatus("current")
_QtechFanStateIndex_Type = Integer32
_QtechFanStateIndex_Object = MibTableColumn
qtechFanStateIndex = _QtechFanStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 6, 1, 2),
    _QtechFanStateIndex_Type()
)
qtechFanStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFanStateIndex.setStatus("current")


class _QtechFanState_Type(Integer32):
    """Custom type qtechFanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("work", 1),
          ("stop", 2))
    )


_QtechFanState_Type.__name__ = "Integer32"
_QtechFanState_Object = MibTableColumn
qtechFanState = _QtechFanState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 6, 1, 3),
    _QtechFanState_Type()
)
qtechFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFanState.setStatus("current")


class _QtechFanStateFanDescr_Type(DisplayString):
    """Custom type qtechFanStateFanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechFanStateFanDescr_Type.__name__ = "DisplayString"
_QtechFanStateFanDescr_Object = MibTableColumn
qtechFanStateFanDescr = _QtechFanStateFanDescr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 1, 6, 1, 4),
    _QtechFanStateFanDescr_Type()
)
qtechFanStateFanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFanStateFanDescr.setStatus("current")
_QtechEntityMIBTraps_ObjectIdentity = ObjectIdentity
qtechEntityMIBTraps = _QtechEntityMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 2)
)
_QtechEntityStateChgDesc_Type = DisplayString
_QtechEntityStateChgDesc_Object = MibScalar
qtechEntityStateChgDesc = _QtechEntityStateChgDesc_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 2, 1),
    _QtechEntityStateChgDesc_Type()
)
qtechEntityStateChgDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechEntityStateChgDesc.setStatus("current")


class _QtechTemperatureWarningDesc_Type(DisplayString):
    """Custom type qtechTemperatureWarningDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechTemperatureWarningDesc_Type.__name__ = "DisplayString"
_QtechTemperatureWarningDesc_Object = MibScalar
qtechTemperatureWarningDesc = _QtechTemperatureWarningDesc_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 2, 3),
    _QtechTemperatureWarningDesc_Type()
)
qtechTemperatureWarningDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechTemperatureWarningDesc.setStatus("current")
_QtechDeviceMIBConformance_ObjectIdentity = ObjectIdentity
qtechDeviceMIBConformance = _QtechDeviceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 3)
)
_QtechDeviceMIBCompliances_ObjectIdentity = ObjectIdentity
qtechDeviceMIBCompliances = _QtechDeviceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 3, 1)
)
_QtechDeviceMIBGroups_ObjectIdentity = ObjectIdentity
qtechDeviceMIBGroups = _QtechDeviceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 3, 2)
)

# Managed Objects groups

qtechDeviceInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 3, 2, 1)
)
qtechDeviceInfoMIBGroup.setObjects(
      *(("QTECH-ENTITY-MIB", "qtechDeviceMaxNumber"),
        ("QTECH-ENTITY-MIB", "qtechDeviceInfoIndex"),
        ("QTECH-ENTITY-MIB", "qtechDeviceInfoDescr"),
        ("QTECH-ENTITY-MIB", "qtechDeviceInfoSlotNumber"),
        ("QTECH-ENTITY-MIB", "qtechDevicePowerStatus"))
)
if mibBuilder.loadTexts:
    qtechDeviceInfoMIBGroup.setStatus("current")

qtechOptionalDevInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 3, 2, 2)
)
qtechOptionalDevInfoMIBGroup.setObjects(
      *(("QTECH-ENTITY-MIB", "qtechDeviceMacAddress"),
        ("QTECH-ENTITY-MIB", "qtechDevicePriority"),
        ("QTECH-ENTITY-MIB", "qtechDeviceAlias"),
        ("QTECH-ENTITY-MIB", "qtechDeviceSWVersion"),
        ("QTECH-ENTITY-MIB", "qtechDeviceHWVersion"),
        ("QTECH-ENTITY-MIB", "qtechDeviceSerialNumber"),
        ("QTECH-ENTITY-MIB", "qtechDeviceOid"))
)
if mibBuilder.loadTexts:
    qtechOptionalDevInfoMIBGroup.setStatus("current")

qtechModuleInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 3, 2, 3)
)
qtechModuleInfoMIBGroup.setObjects(
      *(("QTECH-ENTITY-MIB", "qtechSlotInfoDeviceIndex"),
        ("QTECH-ENTITY-MIB", "qtechSlotInfoIndex"),
        ("QTECH-ENTITY-MIB", "qtechSlotModuleInfoDescr"),
        ("QTECH-ENTITY-MIB", "qtechSlotInfoPortNumber"),
        ("QTECH-ENTITY-MIB", "qtechSlotInfoPortMaxNumber"),
        ("QTECH-ENTITY-MIB", "qtechSlotInfoDesc"),
        ("QTECH-ENTITY-MIB", "qtechSlotConfigModuleInfoDescr"),
        ("QTECH-ENTITY-MIB", "qtechSlotUserStatus"),
        ("QTECH-ENTITY-MIB", "qtechSlotSoftwareStatus"),
        ("QTECH-ENTITY-MIB", "qtechSlotSerialNumber"),
        ("QTECH-ENTITY-MIB", "qtechSlotHWVersion"))
)
if mibBuilder.loadTexts:
    qtechModuleInfoMIBGroup.setStatus("current")

qtechEntityChgDescGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 3, 2, 4)
)
qtechEntityChgDescGroup.setObjects(
    ("QTECH-ENTITY-MIB", "qtechEntityStateChgDesc")
)
if mibBuilder.loadTexts:
    qtechEntityChgDescGroup.setStatus("current")

qtechModuleTempStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 3, 2, 6)
)
qtechModuleTempStateGroup.setObjects(
      *(("QTECH-ENTITY-MIB", "qtechModuleTempStateDeviceIndex"),
        ("QTECH-ENTITY-MIB", "qtechModuleTempStateIndex"),
        ("QTECH-ENTITY-MIB", "qtechModuleTempState"))
)
if mibBuilder.loadTexts:
    qtechModuleTempStateGroup.setStatus("current")

qtechPowerStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 3, 2, 7)
)
qtechPowerStateGroup.setObjects(
      *(("QTECH-ENTITY-MIB", "qtechPowerStateDeviceIndex"),
        ("QTECH-ENTITY-MIB", "qtechPowerStateIndex"),
        ("QTECH-ENTITY-MIB", "qtechPowerState"),
        ("QTECH-ENTITY-MIB", "qtechPowerStatePowerDescr"))
)
if mibBuilder.loadTexts:
    qtechPowerStateGroup.setStatus("current")

qtechFanStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 3, 2, 8)
)
qtechFanStateGroup.setObjects(
      *(("QTECH-ENTITY-MIB", "qtechFanStateDeviceIndex"),
        ("QTECH-ENTITY-MIB", "qtechFanStateIndex"),
        ("QTECH-ENTITY-MIB", "qtechFanState"),
        ("QTECH-ENTITY-MIB", "qtechFanStateFanDescr"))
)
if mibBuilder.loadTexts:
    qtechFanStateGroup.setStatus("current")

qtechTemperatureWarningDescGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 3, 2, 9)
)
qtechTemperatureWarningDescGroup.setObjects(
    ("QTECH-ENTITY-MIB", "qtechTemperatureWarningDesc")
)
if mibBuilder.loadTexts:
    qtechTemperatureWarningDescGroup.setStatus("current")


# Notification objects

qtechEntityStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 2, 2)
)
qtechEntityStatusChange.setObjects(
    ("QTECH-ENTITY-MIB", "qtechEntityStateChgDesc")
)
if mibBuilder.loadTexts:
    qtechEntityStatusChange.setStatus(
        "current"
    )

qtechTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 2, 4)
)
qtechTemperatureWarning.setObjects(
    ("QTECH-ENTITY-MIB", "qtechTemperatureWarningDesc")
)
if mibBuilder.loadTexts:
    qtechTemperatureWarning.setStatus(
        "current"
    )


# Notifications groups

qtechDeviceMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 3, 2, 5)
)
qtechDeviceMIBNotificationGroup.setObjects(
    ("QTECH-ENTITY-MIB", "qtechEntityStatusChange")
)
if mibBuilder.loadTexts:
    qtechDeviceMIBNotificationGroup.setStatus(
        "current"
    )

qtechTemperatureWarningGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 3, 2, 10)
)
qtechTemperatureWarningGroup.setObjects(
    ("QTECH-ENTITY-MIB", "qtechTemperatureWarning")
)
if mibBuilder.loadTexts:
    qtechTemperatureWarningGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

qtechDeviceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 21, 3, 1, 1)
)
qtechDeviceMIBCompliance.setObjects(
      *(("QTECH-ENTITY-MIB", "qtechDeviceInfoMIBGroup"),
        ("QTECH-ENTITY-MIB", "qtechModuleInfoMIBGroup"),
        ("QTECH-ENTITY-MIB", "qtechOptionalDevInfoMIBGroup"),
        ("QTECH-ENTITY-MIB", "qtechEntityChgDescGroup"),
        ("QTECH-ENTITY-MIB", "qtechDeviceMIBNotificationGroup"),
        ("QTECH-ENTITY-MIB", "qtechModuleTempStateGroup"),
        ("QTECH-ENTITY-MIB", "qtechPowerStateGroup"),
        ("QTECH-ENTITY-MIB", "qtechFanStateGroup"),
        ("QTECH-ENTITY-MIB", "qtechTemperatureWarningDescGroup"),
        ("QTECH-ENTITY-MIB", "qtechTemperatureWarningGroup"))
)
if mibBuilder.loadTexts:
    qtechDeviceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-ENTITY-MIB",
    **{"qtechEntityMIB": qtechEntityMIB,
       "qtechDeviceMIBObjects": qtechDeviceMIBObjects,
       "qtechDeviceMaxNumber": qtechDeviceMaxNumber,
       "qtechDeviceInfoTable": qtechDeviceInfoTable,
       "qtechDeviceInfoEntry": qtechDeviceInfoEntry,
       "qtechDeviceInfoIndex": qtechDeviceInfoIndex,
       "qtechDeviceInfoDescr": qtechDeviceInfoDescr,
       "qtechDeviceInfoSlotNumber": qtechDeviceInfoSlotNumber,
       "qtechDevicePowerStatus": qtechDevicePowerStatus,
       "qtechDeviceMacAddress": qtechDeviceMacAddress,
       "qtechDevicePriority": qtechDevicePriority,
       "qtechDeviceAlias": qtechDeviceAlias,
       "qtechDeviceSWVersion": qtechDeviceSWVersion,
       "qtechDeviceHWVersion": qtechDeviceHWVersion,
       "qtechDeviceSerialNumber": qtechDeviceSerialNumber,
       "qtechDeviceOid": qtechDeviceOid,
       "qtechSlotInfoTable": qtechSlotInfoTable,
       "qtechSlotInfoEntry": qtechSlotInfoEntry,
       "qtechSlotInfoDeviceIndex": qtechSlotInfoDeviceIndex,
       "qtechSlotInfoIndex": qtechSlotInfoIndex,
       "qtechSlotModuleInfoDescr": qtechSlotModuleInfoDescr,
       "qtechSlotInfoPortNumber": qtechSlotInfoPortNumber,
       "qtechSlotInfoPortMaxNumber": qtechSlotInfoPortMaxNumber,
       "qtechSlotInfoDesc": qtechSlotInfoDesc,
       "qtechSlotConfigModuleInfoDescr": qtechSlotConfigModuleInfoDescr,
       "qtechSlotUserStatus": qtechSlotUserStatus,
       "qtechSlotSoftwareStatus": qtechSlotSoftwareStatus,
       "qtechSlotSerialNumber": qtechSlotSerialNumber,
       "qtechSlotHWVersion": qtechSlotHWVersion,
       "qtechModuleTempStateTable": qtechModuleTempStateTable,
       "qtechModuleTempStateEntry": qtechModuleTempStateEntry,
       "qtechModuleTempStateDeviceIndex": qtechModuleTempStateDeviceIndex,
       "qtechModuleTempStateIndex": qtechModuleTempStateIndex,
       "qtechModuleTempState": qtechModuleTempState,
       "qtechPowerStateTable": qtechPowerStateTable,
       "qtechPowerStateEntry": qtechPowerStateEntry,
       "qtechPowerStateDeviceIndex": qtechPowerStateDeviceIndex,
       "qtechPowerStateIndex": qtechPowerStateIndex,
       "qtechPowerState": qtechPowerState,
       "qtechPowerStatePowerDescr": qtechPowerStatePowerDescr,
       "qtechFanStateTable": qtechFanStateTable,
       "qtechFanStateEntry": qtechFanStateEntry,
       "qtechFanStateDeviceIndex": qtechFanStateDeviceIndex,
       "qtechFanStateIndex": qtechFanStateIndex,
       "qtechFanState": qtechFanState,
       "qtechFanStateFanDescr": qtechFanStateFanDescr,
       "qtechEntityMIBTraps": qtechEntityMIBTraps,
       "qtechEntityStateChgDesc": qtechEntityStateChgDesc,
       "qtechEntityStatusChange": qtechEntityStatusChange,
       "qtechTemperatureWarningDesc": qtechTemperatureWarningDesc,
       "qtechTemperatureWarning": qtechTemperatureWarning,
       "qtechDeviceMIBConformance": qtechDeviceMIBConformance,
       "qtechDeviceMIBCompliances": qtechDeviceMIBCompliances,
       "qtechDeviceMIBCompliance": qtechDeviceMIBCompliance,
       "qtechDeviceMIBGroups": qtechDeviceMIBGroups,
       "qtechDeviceInfoMIBGroup": qtechDeviceInfoMIBGroup,
       "qtechOptionalDevInfoMIBGroup": qtechOptionalDevInfoMIBGroup,
       "qtechModuleInfoMIBGroup": qtechModuleInfoMIBGroup,
       "qtechEntityChgDescGroup": qtechEntityChgDescGroup,
       "qtechDeviceMIBNotificationGroup": qtechDeviceMIBNotificationGroup,
       "qtechModuleTempStateGroup": qtechModuleTempStateGroup,
       "qtechPowerStateGroup": qtechPowerStateGroup,
       "qtechFanStateGroup": qtechFanStateGroup,
       "qtechTemperatureWarningDescGroup": qtechTemperatureWarningDescGroup,
       "qtechTemperatureWarningGroup": qtechTemperatureWarningGroup}
)
