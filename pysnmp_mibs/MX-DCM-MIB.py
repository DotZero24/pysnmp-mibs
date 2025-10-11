# SNMP MIB module (MX-DCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-DCM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:53 2025
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

(mediatrixServices,) = mibBuilder.importSymbols(
    "MX-SMI2",
    "mediatrixServices")

(MxActivationState,
 MxAdvancedIpPort,
 MxDigitMap,
 MxEnableState,
 MxIpAddress,
 MxIpHostName,
 MxIpPort,
 MxIpSubnetMask) = mibBuilder.importSymbols(
    "MX-TC",
    "MxActivationState",
    "MxAdvancedIpPort",
    "MxDigitMap",
    "MxEnableState",
    "MxIpAddress",
    "MxIpHostName",
    "MxIpPort",
    "MxIpSubnetMask")

(MxFloat32,
 MxIpAddr,
 MxIpAddrMask,
 MxIpAddrPort,
 MxIpHostNamePort,
 MxUInt64,
 MxUri,
 MxUrl) = mibBuilder.importSymbols(
    "MX-TC2",
    "MxFloat32",
    "MxIpAddr",
    "MxIpAddrMask",
    "MxIpAddrPort",
    "MxIpHostNamePort",
    "MxUInt64",
    "MxUri",
    "MxUrl")

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

dcmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DcmMIBObjects_ObjectIdentity = ObjectIdentity
dcmMIBObjects = _DcmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1)
)
_UnitInfoGroup_ObjectIdentity = ObjectIdentity
unitInfoGroup = _UnitInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 100)
)
_UnitInfoProductName_Type = OctetString
_UnitInfoProductName_Object = MibScalar
unitInfoProductName = _UnitInfoProductName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 100, 100),
    _UnitInfoProductName_Type()
)
unitInfoProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitInfoProductName.setStatus("current")
_UnitInfoSerialNumber_Type = OctetString
_UnitInfoSerialNumber_Object = MibScalar
unitInfoSerialNumber = _UnitInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 100, 200),
    _UnitInfoSerialNumber_Type()
)
unitInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitInfoSerialNumber.setStatus("current")
_UnitInfoMacAddress_Type = OctetString
_UnitInfoMacAddress_Object = MibScalar
unitInfoMacAddress = _UnitInfoMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 100, 300),
    _UnitInfoMacAddress_Type()
)
unitInfoMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitInfoMacAddress.setStatus("current")
_UnitInfoHardwareRevision_Type = OctetString
_UnitInfoHardwareRevision_Object = MibScalar
unitInfoHardwareRevision = _UnitInfoHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 100, 400),
    _UnitInfoHardwareRevision_Type()
)
unitInfoHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitInfoHardwareRevision.setStatus("current")
_TotalNumberOfDsp_Type = Unsigned32
_TotalNumberOfDsp_Object = MibScalar
totalNumberOfDsp = _TotalNumberOfDsp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 100, 500),
    _TotalNumberOfDsp_Type()
)
totalNumberOfDsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalNumberOfDsp.setStatus("current")
_HwExtInfoGroup_ObjectIdentity = ObjectIdentity
hwExtInfoGroup = _HwExtInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 300)
)
_HardwareExtInfoTable_Object = MibTable
hardwareExtInfoTable = _HardwareExtInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 300, 100)
)
if mibBuilder.loadTexts:
    hardwareExtInfoTable.setStatus("current")
_HardwareExtInfoEntry_Object = MibTableRow
hardwareExtInfoEntry = _HardwareExtInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 300, 100, 1)
)
hardwareExtInfoEntry.setIndexNames(
    (0, "MX-DCM-MIB", "hardwareExtInfoIndex"),
)
if mibBuilder.loadTexts:
    hardwareExtInfoEntry.setStatus("current")
_HardwareExtInfoIndex_Type = Unsigned32
_HardwareExtInfoIndex_Object = MibTableColumn
hardwareExtInfoIndex = _HardwareExtInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 300, 100, 1, 100),
    _HardwareExtInfoIndex_Type()
)
hardwareExtInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareExtInfoIndex.setStatus("current")
_HardwareExtInfoProductName_Type = OctetString
_HardwareExtInfoProductName_Object = MibTableColumn
hardwareExtInfoProductName = _HardwareExtInfoProductName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 300, 100, 1, 200),
    _HardwareExtInfoProductName_Type()
)
hardwareExtInfoProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareExtInfoProductName.setStatus("current")
_HardwareExtInfoSerialNumber_Type = OctetString
_HardwareExtInfoSerialNumber_Object = MibTableColumn
hardwareExtInfoSerialNumber = _HardwareExtInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 300, 100, 1, 300),
    _HardwareExtInfoSerialNumber_Type()
)
hardwareExtInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareExtInfoSerialNumber.setStatus("current")
_HardwareExtInfoLocation_Type = OctetString
_HardwareExtInfoLocation_Object = MibTableColumn
hardwareExtInfoLocation = _HardwareExtInfoLocation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 300, 100, 1, 400),
    _HardwareExtInfoLocation_Type()
)
hardwareExtInfoLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareExtInfoLocation.setStatus("current")
_LicenseGroup_ObjectIdentity = ObjectIdentity
licenseGroup = _LicenseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 500)
)
_ActiveFeatureTable_Object = MibTable
activeFeatureTable = _ActiveFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 500, 100)
)
if mibBuilder.loadTexts:
    activeFeatureTable.setStatus("current")
_ActiveFeatureEntry_Object = MibTableRow
activeFeatureEntry = _ActiveFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 500, 100, 1)
)
activeFeatureEntry.setIndexNames(
    (0, "MX-DCM-MIB", "activeFeatureID"),
)
if mibBuilder.loadTexts:
    activeFeatureEntry.setStatus("current")
_ActiveFeatureID_Type = Unsigned32
_ActiveFeatureID_Object = MibTableColumn
activeFeatureID = _ActiveFeatureID_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 500, 100, 1, 100),
    _ActiveFeatureID_Type()
)
activeFeatureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeFeatureID.setStatus("current")
_ActiveFeatureDescription_Type = OctetString
_ActiveFeatureDescription_Object = MibTableColumn
activeFeatureDescription = _ActiveFeatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 500, 100, 1, 200),
    _ActiveFeatureDescription_Type()
)
activeFeatureDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeFeatureDescription.setStatus("current")


class _ActiveFeatureDelete_Type(Integer32):
    """Custom type activeFeatureDelete based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("delete", 10))
    )


_ActiveFeatureDelete_Type.__name__ = "Integer32"
_ActiveFeatureDelete_Object = MibTableColumn
activeFeatureDelete = _ActiveFeatureDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 500, 100, 1, 500),
    _ActiveFeatureDelete_Type()
)
activeFeatureDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeFeatureDelete.setStatus("current")
_StatisticsGroup_ObjectIdentity = ObjectIdentity
statisticsGroup = _StatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 10000)
)
_MemoryGroup_ObjectIdentity = ObjectIdentity
memoryGroup = _MemoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 10000, 100)
)
_PersistentMemoryTotal_Type = Unsigned32
_PersistentMemoryTotal_Object = MibScalar
persistentMemoryTotal = _PersistentMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 10000, 100, 100),
    _PersistentMemoryTotal_Type()
)
persistentMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    persistentMemoryTotal.setStatus("current")
_PersistentMemoryInUse_Type = Unsigned32
_PersistentMemoryInUse_Object = MibScalar
persistentMemoryInUse = _PersistentMemoryInUse_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 10000, 100, 200),
    _PersistentMemoryInUse_Type()
)
persistentMemoryInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    persistentMemoryInUse.setStatus("current")


class _PersistentWearPercentage_Type(Integer32):
    """Custom type persistentWearPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_PersistentWearPercentage_Type.__name__ = "Integer32"
_PersistentWearPercentage_Object = MibScalar
persistentWearPercentage = _PersistentWearPercentage_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 10000, 100, 250),
    _PersistentWearPercentage_Type()
)
persistentWearPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    persistentWearPercentage.setStatus("current")
_VolatileMemoryTotal_Type = MxUInt64
_VolatileMemoryTotal_Object = MibScalar
volatileMemoryTotal = _VolatileMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 10000, 100, 300),
    _VolatileMemoryTotal_Type()
)
volatileMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volatileMemoryTotal.setStatus("current")
_VolatileMemoryInUse_Type = MxUInt64
_VolatileMemoryInUse_Object = MibScalar
volatileMemoryInUse = _VolatileMemoryInUse_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 10000, 100, 400),
    _VolatileMemoryInUse_Type()
)
volatileMemoryInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volatileMemoryInUse.setStatus("current")
_InteropGroup_ObjectIdentity = ObjectIdentity
interopGroup = _InteropGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 50000)
)


class _InteropEthernetControllerRevA0_Type(MxEnableState):
    """Custom type interopEthernetControllerRevA0 based on MxEnableState"""
    defaultValue = 1


_InteropEthernetControllerRevA0_Type.__name__ = "MxEnableState"
_InteropEthernetControllerRevA0_Object = MibScalar
interopEthernetControllerRevA0 = _InteropEthernetControllerRevA0_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 50000, 100),
    _InteropEthernetControllerRevA0_Type()
)
interopEthernetControllerRevA0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopEthernetControllerRevA0.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 60010)
)


class _MinSeverity_Type(Integer32):
    """Custom type minSeverity based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("debug", 100),
          ("info", 200),
          ("warning", 300),
          ("error", 400),
          ("critical", 500))
    )


_MinSeverity_Type.__name__ = "Integer32"
_MinSeverity_Object = MibScalar
minSeverity = _MinSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 60020)
)


class _NeedRestartInfo_Type(Integer32):
    """Custom type needRestartInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 100))
    )


_NeedRestartInfo_Type.__name__ = "Integer32"
_NeedRestartInfo_Object = MibScalar
needRestartInfo = _NeedRestartInfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2000, 1, 60020, 100),
    _NeedRestartInfo_Type()
)
needRestartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    needRestartInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-DCM-MIB",
    **{"dcmMIB": dcmMIB,
       "dcmMIBObjects": dcmMIBObjects,
       "unitInfoGroup": unitInfoGroup,
       "unitInfoProductName": unitInfoProductName,
       "unitInfoSerialNumber": unitInfoSerialNumber,
       "unitInfoMacAddress": unitInfoMacAddress,
       "unitInfoHardwareRevision": unitInfoHardwareRevision,
       "totalNumberOfDsp": totalNumberOfDsp,
       "hwExtInfoGroup": hwExtInfoGroup,
       "hardwareExtInfoTable": hardwareExtInfoTable,
       "hardwareExtInfoEntry": hardwareExtInfoEntry,
       "hardwareExtInfoIndex": hardwareExtInfoIndex,
       "hardwareExtInfoProductName": hardwareExtInfoProductName,
       "hardwareExtInfoSerialNumber": hardwareExtInfoSerialNumber,
       "hardwareExtInfoLocation": hardwareExtInfoLocation,
       "licenseGroup": licenseGroup,
       "activeFeatureTable": activeFeatureTable,
       "activeFeatureEntry": activeFeatureEntry,
       "activeFeatureID": activeFeatureID,
       "activeFeatureDescription": activeFeatureDescription,
       "activeFeatureDelete": activeFeatureDelete,
       "statisticsGroup": statisticsGroup,
       "memoryGroup": memoryGroup,
       "persistentMemoryTotal": persistentMemoryTotal,
       "persistentMemoryInUse": persistentMemoryInUse,
       "persistentWearPercentage": persistentWearPercentage,
       "volatileMemoryTotal": volatileMemoryTotal,
       "volatileMemoryInUse": volatileMemoryInUse,
       "interopGroup": interopGroup,
       "interopEthernetControllerRevA0": interopEthernetControllerRevA0,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
