# SNMP MIB module (LEFTHAND-NETWORKS-NSM-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/LEFTHAND-NETWORKS-NSM-INFO-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:43:10 2025
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

(lhnModules,
 lhnNsm) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-GLOBAL-REG-MIB",
    "lhnModules",
    "lhnNsm")

(lhnNsmInfo,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-NSM-MIB",
    "lhnNsmInfo")

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

lhnNsmInfoModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 2)
)
if mibBuilder.loadTexts:
    lhnNsmInfoModule.setRevisions(
        ("2013-11-15 00:00",
         "2013-06-25 00:00",
         "2012-10-12 00:00",
         "2012-09-18 00:00",
         "2012-06-04 00:00",
         "2011-06-21 00:00",
         "2010-09-07 00:00",
         "2010-07-19 00:00",
         "2009-11-20 00:00",
         "2009-03-10 00:00",
         "2008-01-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LhnNsmInfoModuleConformance_ObjectIdentity = ObjectIdentity
lhnNsmInfoModuleConformance = _LhnNsmInfoModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 2, 1)
)
_LhnNsmInfoModuleCompliances_ObjectIdentity = ObjectIdentity
lhnNsmInfoModuleCompliances = _LhnNsmInfoModuleCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 2, 1, 1)
)
_LhnNsmInfoModuleGroups_ObjectIdentity = ObjectIdentity
lhnNsmInfoModuleGroups = _LhnNsmInfoModuleGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 2, 1, 2)
)
_InfoSerialNumberOld_Type = DisplayString
_InfoSerialNumberOld_Object = MibScalar
infoSerialNumberOld = _InfoSerialNumberOld_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 1),
    _InfoSerialNumberOld_Type()
)
infoSerialNumberOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSerialNumberOld.setStatus("obsolete")
_InfoModelOld_Type = DisplayString
_InfoModelOld_Object = MibScalar
infoModelOld = _InfoModelOld_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 2),
    _InfoModelOld_Type()
)
infoModelOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoModelOld.setStatus("obsolete")
_InfoSoftwareVersionOld_Type = DisplayString
_InfoSoftwareVersionOld_Object = MibScalar
infoSoftwareVersionOld = _InfoSoftwareVersionOld_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 3),
    _InfoSoftwareVersionOld_Type()
)
infoSoftwareVersionOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSoftwareVersionOld.setStatus("obsolete")
_InfoEnclosureFirmwareVersionOld_Type = DisplayString
_InfoEnclosureFirmwareVersionOld_Object = MibScalar
infoEnclosureFirmwareVersionOld = _InfoEnclosureFirmwareVersionOld_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 4),
    _InfoEnclosureFirmwareVersionOld_Type()
)
infoEnclosureFirmwareVersionOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoEnclosureFirmwareVersionOld.setStatus("obsolete")
_InfoMotherboardTemperature_Type = Gauge32
_InfoMotherboardTemperature_Object = MibScalar
infoMotherboardTemperature = _InfoMotherboardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 5),
    _InfoMotherboardTemperature_Type()
)
infoMotherboardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoMotherboardTemperature.setStatus("obsolete")
if mibBuilder.loadTexts:
    infoMotherboardTemperature.setUnits("Celsius")
_InfoCPUCount_Type = Integer32
_InfoCPUCount_Object = MibScalar
infoCPUCount = _InfoCPUCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 14),
    _InfoCPUCount_Type()
)
infoCPUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCPUCount.setStatus("obsolete")
_InfoCPUTable_Object = MibTable
infoCPUTable = _InfoCPUTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 15)
)
if mibBuilder.loadTexts:
    infoCPUTable.setStatus("obsolete")
_InfoCPUEntry_Object = MibTableRow
infoCPUEntry = _InfoCPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 15, 1)
)
infoCPUEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCPUIndex"),
)
if mibBuilder.loadTexts:
    infoCPUEntry.setStatus("obsolete")
_InfoCPUIndex_Type = Unsigned32
_InfoCPUIndex_Object = MibTableColumn
infoCPUIndex = _InfoCPUIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 15, 1, 1),
    _InfoCPUIndex_Type()
)
infoCPUIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    infoCPUIndex.setStatus("obsolete")
_InfoCPUTemperature_Type = Gauge32
_InfoCPUTemperature_Object = MibTableColumn
infoCPUTemperature = _InfoCPUTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 15, 1, 2),
    _InfoCPUTemperature_Type()
)
infoCPUTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCPUTemperature.setStatus("obsolete")
if mibBuilder.loadTexts:
    infoCPUTemperature.setUnits("Celsius")
_InfoCPUFanSpeed_Type = Gauge32
_InfoCPUFanSpeed_Object = MibTableColumn
infoCPUFanSpeed = _InfoCPUFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 15, 1, 3),
    _InfoCPUFanSpeed_Type()
)
infoCPUFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCPUFanSpeed.setStatus("obsolete")
if mibBuilder.loadTexts:
    infoCPUFanSpeed.setUnits("RPM")
_InfoObsoletePowerSupplyCount_Type = Integer32
_InfoObsoletePowerSupplyCount_Object = MibScalar
infoObsoletePowerSupplyCount = _InfoObsoletePowerSupplyCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 16),
    _InfoObsoletePowerSupplyCount_Type()
)
infoObsoletePowerSupplyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoObsoletePowerSupplyCount.setStatus("obsolete")
_InfoObsoletePowerSupplyTable_Object = MibTable
infoObsoletePowerSupplyTable = _InfoObsoletePowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 17)
)
if mibBuilder.loadTexts:
    infoObsoletePowerSupplyTable.setStatus("obsolete")
_InfoObsoletePowerSupplyEntry_Object = MibTableRow
infoObsoletePowerSupplyEntry = _InfoObsoletePowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 17, 1)
)
infoObsoletePowerSupplyEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoObsoletePowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    infoObsoletePowerSupplyEntry.setStatus("obsolete")
_InfoObsoletePowerSupplyIndex_Type = Unsigned32
_InfoObsoletePowerSupplyIndex_Object = MibTableColumn
infoObsoletePowerSupplyIndex = _InfoObsoletePowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 17, 1, 1),
    _InfoObsoletePowerSupplyIndex_Type()
)
infoObsoletePowerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    infoObsoletePowerSupplyIndex.setStatus("obsolete")
_InfoObsoletePowerSupplyState_Type = DisplayString
_InfoObsoletePowerSupplyState_Object = MibTableColumn
infoObsoletePowerSupplyState = _InfoObsoletePowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 17, 1, 3),
    _InfoObsoletePowerSupplyState_Type()
)
infoObsoletePowerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoObsoletePowerSupplyState.setStatus("obsolete")
_InfoObsoleteFanCount_Type = Integer32
_InfoObsoleteFanCount_Object = MibScalar
infoObsoleteFanCount = _InfoObsoleteFanCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 18),
    _InfoObsoleteFanCount_Type()
)
infoObsoleteFanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoObsoleteFanCount.setStatus("obsolete")
_InfoObsoleteFanTable_Object = MibTable
infoObsoleteFanTable = _InfoObsoleteFanTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 19)
)
if mibBuilder.loadTexts:
    infoObsoleteFanTable.setStatus("obsolete")
_InfoObsoleteFanEntry_Object = MibTableRow
infoObsoleteFanEntry = _InfoObsoleteFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 19, 1)
)
infoObsoleteFanEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoObsoleteFanIndex"),
)
if mibBuilder.loadTexts:
    infoObsoleteFanEntry.setStatus("obsolete")
_InfoObsoleteFanIndex_Type = Unsigned32
_InfoObsoleteFanIndex_Object = MibTableColumn
infoObsoleteFanIndex = _InfoObsoleteFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 19, 1, 1),
    _InfoObsoleteFanIndex_Type()
)
infoObsoleteFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    infoObsoleteFanIndex.setStatus("obsolete")
_InfoObsoleteFanState_Type = DisplayString
_InfoObsoleteFanState_Object = MibTableColumn
infoObsoleteFanState = _InfoObsoleteFanState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 19, 1, 3),
    _InfoObsoleteFanState_Type()
)
infoObsoleteFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoObsoleteFanState.setStatus("obsolete")
_InfoFlashCount_Type = Integer32
_InfoFlashCount_Object = MibScalar
infoFlashCount = _InfoFlashCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 20),
    _InfoFlashCount_Type()
)
infoFlashCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFlashCount.setStatus("obsolete")
_InfoFlashTable_Object = MibTable
infoFlashTable = _InfoFlashTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 21)
)
if mibBuilder.loadTexts:
    infoFlashTable.setStatus("obsolete")
_InfoFlashEntry_Object = MibTableRow
infoFlashEntry = _InfoFlashEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 21, 1)
)
infoFlashEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoFlashIndex"),
)
if mibBuilder.loadTexts:
    infoFlashEntry.setStatus("obsolete")
_InfoFlashIndex_Type = Unsigned32
_InfoFlashIndex_Object = MibTableColumn
infoFlashIndex = _InfoFlashIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 21, 1, 1),
    _InfoFlashIndex_Type()
)
infoFlashIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    infoFlashIndex.setStatus("obsolete")
_InfoFlashState_Type = DisplayString
_InfoFlashState_Object = MibTableColumn
infoFlashState = _InfoFlashState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 21, 1, 2),
    _InfoFlashState_Type()
)
infoFlashState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFlashState.setStatus("obsolete")
_InfoDriveCardCount_Type = Integer32
_InfoDriveCardCount_Object = MibScalar
infoDriveCardCount = _InfoDriveCardCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 24),
    _InfoDriveCardCount_Type()
)
infoDriveCardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoDriveCardCount.setStatus("obsolete")
_InfoDriveCardTable_Object = MibTable
infoDriveCardTable = _InfoDriveCardTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 25)
)
if mibBuilder.loadTexts:
    infoDriveCardTable.setStatus("obsolete")
_InfoDriveCardEntry_Object = MibTableRow
infoDriveCardEntry = _InfoDriveCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 25, 1)
)
infoDriveCardEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoDriveCardIndex"),
)
if mibBuilder.loadTexts:
    infoDriveCardEntry.setStatus("obsolete")
_InfoDriveCardIndex_Type = Unsigned32
_InfoDriveCardIndex_Object = MibTableColumn
infoDriveCardIndex = _InfoDriveCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 25, 1, 1),
    _InfoDriveCardIndex_Type()
)
infoDriveCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    infoDriveCardIndex.setStatus("obsolete")
_InfoDriveCardModel_Type = DisplayString
_InfoDriveCardModel_Object = MibTableColumn
infoDriveCardModel = _InfoDriveCardModel_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 25, 1, 2),
    _InfoDriveCardModel_Type()
)
infoDriveCardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoDriveCardModel.setStatus("obsolete")
_InfoDriveCardBiosVersion_Type = DisplayString
_InfoDriveCardBiosVersion_Object = MibTableColumn
infoDriveCardBiosVersion = _InfoDriveCardBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 25, 1, 3),
    _InfoDriveCardBiosVersion_Type()
)
infoDriveCardBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoDriveCardBiosVersion.setStatus("obsolete")
_InfoDriveCardFirmwareVersion_Type = DisplayString
_InfoDriveCardFirmwareVersion_Object = MibTableColumn
infoDriveCardFirmwareVersion = _InfoDriveCardFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 25, 1, 4),
    _InfoDriveCardFirmwareVersion_Type()
)
infoDriveCardFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoDriveCardFirmwareVersion.setStatus("obsolete")
_InfoCacheBatteryCount_Type = Integer32
_InfoCacheBatteryCount_Object = MibScalar
infoCacheBatteryCount = _InfoCacheBatteryCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 28),
    _InfoCacheBatteryCount_Type()
)
infoCacheBatteryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCacheBatteryCount.setStatus("obsolete")
_InfoCacheBatteryTable_Object = MibTable
infoCacheBatteryTable = _InfoCacheBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 29)
)
if mibBuilder.loadTexts:
    infoCacheBatteryTable.setStatus("obsolete")
_InfoCacheBatteryEntry_Object = MibTableRow
infoCacheBatteryEntry = _InfoCacheBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 29, 1)
)
infoCacheBatteryEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheBatteryIndex"),
)
if mibBuilder.loadTexts:
    infoCacheBatteryEntry.setStatus("obsolete")
_InfoCacheBatteryIndex_Type = Unsigned32
_InfoCacheBatteryIndex_Object = MibTableColumn
infoCacheBatteryIndex = _InfoCacheBatteryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 29, 1, 1),
    _InfoCacheBatteryIndex_Type()
)
infoCacheBatteryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    infoCacheBatteryIndex.setStatus("obsolete")
_InfoCacheBatteryState_Type = DisplayString
_InfoCacheBatteryState_Object = MibTableColumn
infoCacheBatteryState = _InfoCacheBatteryState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 29, 1, 2),
    _InfoCacheBatteryState_Type()
)
infoCacheBatteryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCacheBatteryState.setStatus("obsolete")
_InfoModel_Type = DisplayString
_InfoModel_Object = MibScalar
infoModel = _InfoModel_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 30),
    _InfoModel_Type()
)
infoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoModel.setStatus("current")
_InfoHostname_Type = DisplayString
_InfoHostname_Object = MibScalar
infoHostname = _InfoHostname_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 31),
    _InfoHostname_Type()
)
infoHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoHostname.setStatus("current")
_InfoIP_Type = DisplayString
_InfoIP_Object = MibScalar
infoIP = _InfoIP_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 32),
    _InfoIP_Type()
)
infoIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoIP.setStatus("current")
_InfoMAC_Type = DisplayString
_InfoMAC_Object = MibScalar
infoMAC = _InfoMAC_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 33),
    _InfoMAC_Type()
)
infoMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoMAC.setStatus("current")
_InfoSerialNumber_Type = DisplayString
_InfoSerialNumber_Object = MibScalar
infoSerialNumber = _InfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 34),
    _InfoSerialNumber_Type()
)
infoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSerialNumber.setStatus("current")
_InfoChassisUUID_Type = DisplayString
_InfoChassisUUID_Object = MibScalar
infoChassisUUID = _InfoChassisUUID_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 35),
    _InfoChassisUUID_Type()
)
infoChassisUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoChassisUUID.setStatus("current")
_InfoProductName_Type = DisplayString
_InfoProductName_Object = MibScalar
infoProductName = _InfoProductName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 36),
    _InfoProductName_Type()
)
infoProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoProductName.setStatus("current")
_InfoProductID_Type = DisplayString
_InfoProductID_Object = MibScalar
infoProductID = _InfoProductID_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 37),
    _InfoProductID_Type()
)
infoProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoProductID.setStatus("current")
_InfoSupportKey_Type = DisplayString
_InfoSupportKey_Object = MibScalar
infoSupportKey = _InfoSupportKey_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 38),
    _InfoSupportKey_Type()
)
infoSupportKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSupportKey.setStatus("current")
_InfoHardwareDescription_Type = DisplayString
_InfoHardwareDescription_Object = MibScalar
infoHardwareDescription = _InfoHardwareDescription_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 39),
    _InfoHardwareDescription_Type()
)
infoHardwareDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoHardwareDescription.setStatus("current")
_InfoSoftwareType_Type = DisplayString
_InfoSoftwareType_Object = MibScalar
infoSoftwareType = _InfoSoftwareType_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 50),
    _InfoSoftwareType_Type()
)
infoSoftwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSoftwareType.setStatus("current")
_InfoSoftwareVersion_Type = DisplayString
_InfoSoftwareVersion_Object = MibScalar
infoSoftwareVersion = _InfoSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 51),
    _InfoSoftwareVersion_Type()
)
infoSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoSoftwareVersion.setStatus("current")
_InfoHPsmhdVersion_Type = DisplayString
_InfoHPsmhdVersion_Object = MibScalar
infoHPsmhdVersion = _InfoHPsmhdVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 52),
    _InfoHPsmhdVersion_Type()
)
infoHPsmhdVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoHPsmhdVersion.setStatus("current")
_InfoHPSNMPAgent_Type = TruthValue
_InfoHPSNMPAgent_Object = MibScalar
infoHPSNMPAgent = _InfoHPSNMPAgent_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 53),
    _InfoHPSNMPAgent_Type()
)
infoHPSNMPAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoHPSNMPAgent.setStatus("current")
_InfoBIOSVersion_Type = DisplayString
_InfoBIOSVersion_Object = MibScalar
infoBIOSVersion = _InfoBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 70),
    _InfoBIOSVersion_Type()
)
infoBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoBIOSVersion.setStatus("current")
_InfoControllerCount_Type = Integer32
_InfoControllerCount_Object = MibScalar
infoControllerCount = _InfoControllerCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 80),
    _InfoControllerCount_Type()
)
infoControllerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoControllerCount.setStatus("current")
_InfoControllerTable_Object = MibTable
infoControllerTable = _InfoControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 81)
)
if mibBuilder.loadTexts:
    infoControllerTable.setStatus("current")
_InfoControllerEntry_Object = MibTableRow
infoControllerEntry = _InfoControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 81, 1)
)
infoControllerEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoControllerIndex"),
)
if mibBuilder.loadTexts:
    infoControllerEntry.setStatus("current")
_InfoControllerIndex_Type = Unsigned32
_InfoControllerIndex_Object = MibTableColumn
infoControllerIndex = _InfoControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 81, 1, 1),
    _InfoControllerIndex_Type()
)
infoControllerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    infoControllerIndex.setStatus("current")
_InfoControllerName_Type = DisplayString
_InfoControllerName_Object = MibTableColumn
infoControllerName = _InfoControllerName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 81, 1, 2),
    _InfoControllerName_Type()
)
infoControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoControllerName.setStatus("current")
_InfoControllerModelNumber_Type = DisplayString
_InfoControllerModelNumber_Object = MibTableColumn
infoControllerModelNumber = _InfoControllerModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 81, 1, 3),
    _InfoControllerModelNumber_Type()
)
infoControllerModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoControllerModelNumber.setStatus("current")
_InfoControllerSerialNumber_Type = DisplayString
_InfoControllerSerialNumber_Object = MibTableColumn
infoControllerSerialNumber = _InfoControllerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 81, 1, 4),
    _InfoControllerSerialNumber_Type()
)
infoControllerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoControllerSerialNumber.setStatus("current")
_InfoControllerFirmwareVersion_Type = DisplayString
_InfoControllerFirmwareVersion_Object = MibTableColumn
infoControllerFirmwareVersion = _InfoControllerFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 81, 1, 5),
    _InfoControllerFirmwareVersion_Type()
)
infoControllerFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoControllerFirmwareVersion.setStatus("current")
_InfoControllerBiosVersion_Type = DisplayString
_InfoControllerBiosVersion_Object = MibTableColumn
infoControllerBiosVersion = _InfoControllerBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 81, 1, 6),
    _InfoControllerBiosVersion_Type()
)
infoControllerBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoControllerBiosVersion.setStatus("current")
_InfoControllerDriverVersion_Type = DisplayString
_InfoControllerDriverVersion_Object = MibTableColumn
infoControllerDriverVersion = _InfoControllerDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 81, 1, 7),
    _InfoControllerDriverVersion_Type()
)
infoControllerDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoControllerDriverVersion.setStatus("current")
_InfoControllerRowStatus_Type = RowStatus
_InfoControllerRowStatus_Object = MibTableColumn
infoControllerRowStatus = _InfoControllerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 81, 1, 99),
    _InfoControllerRowStatus_Type()
)
infoControllerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoControllerRowStatus.setStatus("obsolete")
_InfoCacheCount_Type = Integer32
_InfoCacheCount_Object = MibScalar
infoCacheCount = _InfoCacheCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 90),
    _InfoCacheCount_Type()
)
infoCacheCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCacheCount.setStatus("current")
_InfoCacheTable_Object = MibTable
infoCacheTable = _InfoCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 91)
)
if mibBuilder.loadTexts:
    infoCacheTable.setStatus("current")
_InfoCacheEntry_Object = MibTableRow
infoCacheEntry = _InfoCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 91, 1)
)
infoCacheEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheIndex"),
)
if mibBuilder.loadTexts:
    infoCacheEntry.setStatus("current")
_InfoCacheIndex_Type = Unsigned32
_InfoCacheIndex_Object = MibTableColumn
infoCacheIndex = _InfoCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 91, 1, 1),
    _InfoCacheIndex_Type()
)
infoCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    infoCacheIndex.setStatus("current")
_InfoCacheName_Type = DisplayString
_InfoCacheName_Object = MibTableColumn
infoCacheName = _InfoCacheName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 91, 1, 2),
    _InfoCacheName_Type()
)
infoCacheName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCacheName.setStatus("current")
_InfoCacheModel_Type = DisplayString
_InfoCacheModel_Object = MibTableColumn
infoCacheModel = _InfoCacheModel_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 91, 1, 3),
    _InfoCacheModel_Type()
)
infoCacheModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCacheModel.setStatus("current")
_InfoCacheSize_Type = Integer32
_InfoCacheSize_Object = MibTableColumn
infoCacheSize = _InfoCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 91, 1, 4),
    _InfoCacheSize_Type()
)
infoCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCacheSize.setStatus("current")
if mibBuilder.loadTexts:
    infoCacheSize.setUnits("mB")
_InfoCacheSerialNumber_Type = DisplayString
_InfoCacheSerialNumber_Object = MibTableColumn
infoCacheSerialNumber = _InfoCacheSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 91, 1, 5),
    _InfoCacheSerialNumber_Type()
)
infoCacheSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCacheSerialNumber.setStatus("current")
_InfoCacheHardwareVersion_Type = DisplayString
_InfoCacheHardwareVersion_Object = MibTableColumn
infoCacheHardwareVersion = _InfoCacheHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 91, 1, 6),
    _InfoCacheHardwareVersion_Type()
)
infoCacheHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCacheHardwareVersion.setStatus("current")
_InfoCacheFirmwareVersion_Type = DisplayString
_InfoCacheFirmwareVersion_Object = MibTableColumn
infoCacheFirmwareVersion = _InfoCacheFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 91, 1, 7),
    _InfoCacheFirmwareVersion_Type()
)
infoCacheFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCacheFirmwareVersion.setStatus("current")
_InfoCacheDriverVersion_Type = DisplayString
_InfoCacheDriverVersion_Object = MibTableColumn
infoCacheDriverVersion = _InfoCacheDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 91, 1, 8),
    _InfoCacheDriverVersion_Type()
)
infoCacheDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCacheDriverVersion.setStatus("current")
_InfoCacheBpsVoltage_Type = DisplayString
_InfoCacheBpsVoltage_Object = MibTableColumn
infoCacheBpsVoltage = _InfoCacheBpsVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 91, 1, 20),
    _InfoCacheBpsVoltage_Type()
)
infoCacheBpsVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCacheBpsVoltage.setStatus("current")
if mibBuilder.loadTexts:
    infoCacheBpsVoltage.setUnits("Volts")
_InfoCacheBpsTestOverdue_Type = TruthValue
_InfoCacheBpsTestOverdue_Object = MibTableColumn
infoCacheBpsTestOverdue = _InfoCacheBpsTestOverdue_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 91, 1, 21),
    _InfoCacheBpsTestOverdue_Type()
)
infoCacheBpsTestOverdue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCacheBpsTestOverdue.setStatus("current")
_InfoCacheBpsState_Type = DisplayString
_InfoCacheBpsState_Object = MibTableColumn
infoCacheBpsState = _InfoCacheBpsState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 91, 1, 22),
    _InfoCacheBpsState_Type()
)
infoCacheBpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCacheBpsState.setStatus("current")


class _InfoCacheBpsStatus_Type(Integer32):
    """Custom type infoCacheBpsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2))
    )


_InfoCacheBpsStatus_Type.__name__ = "Integer32"
_InfoCacheBpsStatus_Object = MibTableColumn
infoCacheBpsStatus = _InfoCacheBpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 91, 1, 23),
    _InfoCacheBpsStatus_Type()
)
infoCacheBpsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCacheBpsStatus.setStatus("current")
_InfoCacheEnabled_Type = TruthValue
_InfoCacheEnabled_Object = MibTableColumn
infoCacheEnabled = _InfoCacheEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 91, 1, 50),
    _InfoCacheEnabled_Type()
)
infoCacheEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCacheEnabled.setStatus("current")
_InfoCacheMode_Type = DisplayString
_InfoCacheMode_Object = MibTableColumn
infoCacheMode = _InfoCacheMode_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 91, 1, 51),
    _InfoCacheMode_Type()
)
infoCacheMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCacheMode.setStatus("current")
_InfoCacheState_Type = DisplayString
_InfoCacheState_Object = MibTableColumn
infoCacheState = _InfoCacheState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 91, 1, 90),
    _InfoCacheState_Type()
)
infoCacheState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCacheState.setStatus("current")


class _InfoCacheStatus_Type(Integer32):
    """Custom type infoCacheStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2))
    )


_InfoCacheStatus_Type.__name__ = "Integer32"
_InfoCacheStatus_Object = MibTableColumn
infoCacheStatus = _InfoCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 91, 1, 91),
    _InfoCacheStatus_Type()
)
infoCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCacheStatus.setStatus("current")
_InfoCacheRowStatus_Type = RowStatus
_InfoCacheRowStatus_Object = MibTableColumn
infoCacheRowStatus = _InfoCacheRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 91, 1, 99),
    _InfoCacheRowStatus_Type()
)
infoCacheRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoCacheRowStatus.setStatus("obsolete")
_InfoBackplaneCount_Type = Integer32
_InfoBackplaneCount_Object = MibScalar
infoBackplaneCount = _InfoBackplaneCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 100),
    _InfoBackplaneCount_Type()
)
infoBackplaneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoBackplaneCount.setStatus("current")
_InfoBackplaneTable_Object = MibTable
infoBackplaneTable = _InfoBackplaneTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 101)
)
if mibBuilder.loadTexts:
    infoBackplaneTable.setStatus("current")
_InfoBackplaneEntry_Object = MibTableRow
infoBackplaneEntry = _InfoBackplaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 101, 1)
)
infoBackplaneEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoBackplaneIndex"),
)
if mibBuilder.loadTexts:
    infoBackplaneEntry.setStatus("current")
_InfoBackplaneIndex_Type = Unsigned32
_InfoBackplaneIndex_Object = MibTableColumn
infoBackplaneIndex = _InfoBackplaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 101, 1, 1),
    _InfoBackplaneIndex_Type()
)
infoBackplaneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    infoBackplaneIndex.setStatus("current")
_InfoBackplaneName_Type = DisplayString
_InfoBackplaneName_Object = MibTableColumn
infoBackplaneName = _InfoBackplaneName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 101, 1, 2),
    _InfoBackplaneName_Type()
)
infoBackplaneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoBackplaneName.setStatus("current")
_InfoBackplaneSerialNumber_Type = DisplayString
_InfoBackplaneSerialNumber_Object = MibTableColumn
infoBackplaneSerialNumber = _InfoBackplaneSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 101, 1, 3),
    _InfoBackplaneSerialNumber_Type()
)
infoBackplaneSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoBackplaneSerialNumber.setStatus("current")
_InfoBackplaneFirmwareVersion_Type = DisplayString
_InfoBackplaneFirmwareVersion_Object = MibTableColumn
infoBackplaneFirmwareVersion = _InfoBackplaneFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 101, 1, 4),
    _InfoBackplaneFirmwareVersion_Type()
)
infoBackplaneFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoBackplaneFirmwareVersion.setStatus("current")
_InfoBackplaneIDLed_Type = DisplayString
_InfoBackplaneIDLed_Object = MibTableColumn
infoBackplaneIDLed = _InfoBackplaneIDLed_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 101, 1, 5),
    _InfoBackplaneIDLed_Type()
)
infoBackplaneIDLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoBackplaneIDLed.setStatus("current")
_InfoBackplaneRowStatus_Type = RowStatus
_InfoBackplaneRowStatus_Object = MibTableColumn
infoBackplaneRowStatus = _InfoBackplaneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 101, 1, 99),
    _InfoBackplaneRowStatus_Type()
)
infoBackplaneRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoBackplaneRowStatus.setStatus("obsolete")
_InfoFanCount_Type = Integer32
_InfoFanCount_Object = MibScalar
infoFanCount = _InfoFanCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 110),
    _InfoFanCount_Type()
)
infoFanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFanCount.setStatus("current")
_InfoFanTable_Object = MibTable
infoFanTable = _InfoFanTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 111)
)
if mibBuilder.loadTexts:
    infoFanTable.setStatus("current")
_InfoFanEntry_Object = MibTableRow
infoFanEntry = _InfoFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 111, 1)
)
infoFanEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoFanIndex"),
)
if mibBuilder.loadTexts:
    infoFanEntry.setStatus("current")
_InfoFanIndex_Type = Unsigned32
_InfoFanIndex_Object = MibTableColumn
infoFanIndex = _InfoFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 111, 1, 1),
    _InfoFanIndex_Type()
)
infoFanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    infoFanIndex.setStatus("current")
_InfoFanName_Type = DisplayString
_InfoFanName_Object = MibTableColumn
infoFanName = _InfoFanName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 111, 1, 2),
    _InfoFanName_Type()
)
infoFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFanName.setStatus("current")
_InfoFanSpeed_Type = Gauge32
_InfoFanSpeed_Object = MibTableColumn
infoFanSpeed = _InfoFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 111, 1, 3),
    _InfoFanSpeed_Type()
)
infoFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    infoFanSpeed.setUnits("RPM")
_InfoFanMinSpeed_Type = Integer32
_InfoFanMinSpeed_Object = MibTableColumn
infoFanMinSpeed = _InfoFanMinSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 111, 1, 4),
    _InfoFanMinSpeed_Type()
)
infoFanMinSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFanMinSpeed.setStatus("current")
if mibBuilder.loadTexts:
    infoFanMinSpeed.setUnits("RPM")
_InfoFanState_Type = DisplayString
_InfoFanState_Object = MibTableColumn
infoFanState = _InfoFanState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 111, 1, 90),
    _InfoFanState_Type()
)
infoFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFanState.setStatus("current")


class _InfoFanStatus_Type(Integer32):
    """Custom type infoFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2))
    )


_InfoFanStatus_Type.__name__ = "Integer32"
_InfoFanStatus_Object = MibTableColumn
infoFanStatus = _InfoFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 111, 1, 91),
    _InfoFanStatus_Type()
)
infoFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFanStatus.setStatus("current")
_InfoFanRowStatus_Type = RowStatus
_InfoFanRowStatus_Object = MibTableColumn
infoFanRowStatus = _InfoFanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 111, 1, 99),
    _InfoFanRowStatus_Type()
)
infoFanRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFanRowStatus.setStatus("obsolete")
_InfoTemperatureSensorCount_Type = Integer32
_InfoTemperatureSensorCount_Object = MibScalar
infoTemperatureSensorCount = _InfoTemperatureSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 120),
    _InfoTemperatureSensorCount_Type()
)
infoTemperatureSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoTemperatureSensorCount.setStatus("current")
_InfoTemperatureSensorTable_Object = MibTable
infoTemperatureSensorTable = _InfoTemperatureSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 121)
)
if mibBuilder.loadTexts:
    infoTemperatureSensorTable.setStatus("current")
_InfoTemperatureSensorEntry_Object = MibTableRow
infoTemperatureSensorEntry = _InfoTemperatureSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 121, 1)
)
infoTemperatureSensorEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoTemperatureSensorIndex"),
)
if mibBuilder.loadTexts:
    infoTemperatureSensorEntry.setStatus("current")
_InfoTemperatureSensorIndex_Type = Unsigned32
_InfoTemperatureSensorIndex_Object = MibTableColumn
infoTemperatureSensorIndex = _InfoTemperatureSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 121, 1, 1),
    _InfoTemperatureSensorIndex_Type()
)
infoTemperatureSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    infoTemperatureSensorIndex.setStatus("current")
_InfoTemperatureSensorName_Type = DisplayString
_InfoTemperatureSensorName_Object = MibTableColumn
infoTemperatureSensorName = _InfoTemperatureSensorName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 121, 1, 2),
    _InfoTemperatureSensorName_Type()
)
infoTemperatureSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoTemperatureSensorName.setStatus("current")
_InfoTemperatureSensorValue_Type = Gauge32
_InfoTemperatureSensorValue_Object = MibTableColumn
infoTemperatureSensorValue = _InfoTemperatureSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 121, 1, 3),
    _InfoTemperatureSensorValue_Type()
)
infoTemperatureSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoTemperatureSensorValue.setStatus("current")
if mibBuilder.loadTexts:
    infoTemperatureSensorValue.setUnits("Celsius")
_InfoTemperatureSensorCritical_Type = Integer32
_InfoTemperatureSensorCritical_Object = MibTableColumn
infoTemperatureSensorCritical = _InfoTemperatureSensorCritical_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 121, 1, 4),
    _InfoTemperatureSensorCritical_Type()
)
infoTemperatureSensorCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoTemperatureSensorCritical.setStatus("current")
if mibBuilder.loadTexts:
    infoTemperatureSensorCritical.setUnits("Celsius")
_InfoTemperatureSensorLimit_Type = Integer32
_InfoTemperatureSensorLimit_Object = MibTableColumn
infoTemperatureSensorLimit = _InfoTemperatureSensorLimit_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 121, 1, 5),
    _InfoTemperatureSensorLimit_Type()
)
infoTemperatureSensorLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoTemperatureSensorLimit.setStatus("current")
if mibBuilder.loadTexts:
    infoTemperatureSensorLimit.setUnits("Celsius")
_InfoTemperatureSensorState_Type = DisplayString
_InfoTemperatureSensorState_Object = MibTableColumn
infoTemperatureSensorState = _InfoTemperatureSensorState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 121, 1, 90),
    _InfoTemperatureSensorState_Type()
)
infoTemperatureSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoTemperatureSensorState.setStatus("current")


class _InfoTemperatureSensorStatus_Type(Integer32):
    """Custom type infoTemperatureSensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2))
    )


_InfoTemperatureSensorStatus_Type.__name__ = "Integer32"
_InfoTemperatureSensorStatus_Object = MibTableColumn
infoTemperatureSensorStatus = _InfoTemperatureSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 121, 1, 91),
    _InfoTemperatureSensorStatus_Type()
)
infoTemperatureSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoTemperatureSensorStatus.setStatus("current")
_InfoTemperatureSensorRowStatus_Type = RowStatus
_InfoTemperatureSensorRowStatus_Object = MibTableColumn
infoTemperatureSensorRowStatus = _InfoTemperatureSensorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 121, 1, 99),
    _InfoTemperatureSensorRowStatus_Type()
)
infoTemperatureSensorRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoTemperatureSensorRowStatus.setStatus("obsolete")
_InfoPowerSupplyCount_Type = Integer32
_InfoPowerSupplyCount_Object = MibScalar
infoPowerSupplyCount = _InfoPowerSupplyCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 130),
    _InfoPowerSupplyCount_Type()
)
infoPowerSupplyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoPowerSupplyCount.setStatus("current")
_InfoPowerSupplyTable_Object = MibTable
infoPowerSupplyTable = _InfoPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 131)
)
if mibBuilder.loadTexts:
    infoPowerSupplyTable.setStatus("current")
_InfoPowerSupplyEntry_Object = MibTableRow
infoPowerSupplyEntry = _InfoPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 131, 1)
)
infoPowerSupplyEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    infoPowerSupplyEntry.setStatus("current")
_InfoPowerSupplyIndex_Type = Unsigned32
_InfoPowerSupplyIndex_Object = MibTableColumn
infoPowerSupplyIndex = _InfoPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 131, 1, 1),
    _InfoPowerSupplyIndex_Type()
)
infoPowerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    infoPowerSupplyIndex.setStatus("current")
_InfoPowerSupplyName_Type = DisplayString
_InfoPowerSupplyName_Object = MibTableColumn
infoPowerSupplyName = _InfoPowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 131, 1, 2),
    _InfoPowerSupplyName_Type()
)
infoPowerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoPowerSupplyName.setStatus("current")
_InfoPowerSupplyState_Type = DisplayString
_InfoPowerSupplyState_Object = MibTableColumn
infoPowerSupplyState = _InfoPowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 131, 1, 90),
    _InfoPowerSupplyState_Type()
)
infoPowerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoPowerSupplyState.setStatus("current")


class _InfoPowerSupplyStatus_Type(Integer32):
    """Custom type infoPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2))
    )


_InfoPowerSupplyStatus_Type.__name__ = "Integer32"
_InfoPowerSupplyStatus_Object = MibTableColumn
infoPowerSupplyStatus = _InfoPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 131, 1, 91),
    _InfoPowerSupplyStatus_Type()
)
infoPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoPowerSupplyStatus.setStatus("current")
_InfoPowerSupplyRowStatus_Type = RowStatus
_InfoPowerSupplyRowStatus_Object = MibTableColumn
infoPowerSupplyRowStatus = _InfoPowerSupplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 131, 1, 99),
    _InfoPowerSupplyRowStatus_Type()
)
infoPowerSupplyRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoPowerSupplyRowStatus.setStatus("obsolete")
_InfoPowerSupplyMode_Type = DisplayString
_InfoPowerSupplyMode_Object = MibScalar
infoPowerSupplyMode = _InfoPowerSupplyMode_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 132),
    _InfoPowerSupplyMode_Type()
)
infoPowerSupplyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoPowerSupplyMode.setStatus("current")
_InfoVoltageSensorCount_Type = Integer32
_InfoVoltageSensorCount_Object = MibScalar
infoVoltageSensorCount = _InfoVoltageSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 140),
    _InfoVoltageSensorCount_Type()
)
infoVoltageSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoVoltageSensorCount.setStatus("current")
_InfoVoltageSensorTable_Object = MibTable
infoVoltageSensorTable = _InfoVoltageSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 141)
)
if mibBuilder.loadTexts:
    infoVoltageSensorTable.setStatus("current")
_InfoVoltageSensorEntry_Object = MibTableRow
infoVoltageSensorEntry = _InfoVoltageSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 141, 1)
)
infoVoltageSensorEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoVoltageSensorIndex"),
)
if mibBuilder.loadTexts:
    infoVoltageSensorEntry.setStatus("current")
_InfoVoltageSensorIndex_Type = Unsigned32
_InfoVoltageSensorIndex_Object = MibTableColumn
infoVoltageSensorIndex = _InfoVoltageSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 141, 1, 1),
    _InfoVoltageSensorIndex_Type()
)
infoVoltageSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    infoVoltageSensorIndex.setStatus("current")
_InfoVoltageSensorName_Type = DisplayString
_InfoVoltageSensorName_Object = MibTableColumn
infoVoltageSensorName = _InfoVoltageSensorName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 141, 1, 2),
    _InfoVoltageSensorName_Type()
)
infoVoltageSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoVoltageSensorName.setStatus("current")
_InfoVoltageSensorValue_Type = DisplayString
_InfoVoltageSensorValue_Object = MibTableColumn
infoVoltageSensorValue = _InfoVoltageSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 141, 1, 3),
    _InfoVoltageSensorValue_Type()
)
infoVoltageSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoVoltageSensorValue.setStatus("current")
if mibBuilder.loadTexts:
    infoVoltageSensorValue.setUnits("Volts")
_InfoVoltageSensorLowLimit_Type = DisplayString
_InfoVoltageSensorLowLimit_Object = MibTableColumn
infoVoltageSensorLowLimit = _InfoVoltageSensorLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 141, 1, 4),
    _InfoVoltageSensorLowLimit_Type()
)
infoVoltageSensorLowLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoVoltageSensorLowLimit.setStatus("current")
if mibBuilder.loadTexts:
    infoVoltageSensorLowLimit.setUnits("Volts")
_InfoVoltageSensorHighLimit_Type = DisplayString
_InfoVoltageSensorHighLimit_Object = MibTableColumn
infoVoltageSensorHighLimit = _InfoVoltageSensorHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 141, 1, 5),
    _InfoVoltageSensorHighLimit_Type()
)
infoVoltageSensorHighLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoVoltageSensorHighLimit.setStatus("current")
if mibBuilder.loadTexts:
    infoVoltageSensorHighLimit.setUnits("Volts")
_InfoVoltageSensorState_Type = DisplayString
_InfoVoltageSensorState_Object = MibTableColumn
infoVoltageSensorState = _InfoVoltageSensorState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 141, 1, 90),
    _InfoVoltageSensorState_Type()
)
infoVoltageSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoVoltageSensorState.setStatus("current")


class _InfoVoltageSensorStatus_Type(Integer32):
    """Custom type infoVoltageSensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2))
    )


_InfoVoltageSensorStatus_Type.__name__ = "Integer32"
_InfoVoltageSensorStatus_Object = MibTableColumn
infoVoltageSensorStatus = _InfoVoltageSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 141, 1, 91),
    _InfoVoltageSensorStatus_Type()
)
infoVoltageSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoVoltageSensorStatus.setStatus("current")
_InfoVoltageSensorRowStatus_Type = RowStatus
_InfoVoltageSensorRowStatus_Object = MibTableColumn
infoVoltageSensorRowStatus = _InfoVoltageSensorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 141, 1, 99),
    _InfoVoltageSensorRowStatus_Type()
)
infoVoltageSensorRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoVoltageSensorRowStatus.setStatus("obsolete")
_InfoBootControllerName_Type = DisplayString
_InfoBootControllerName_Object = MibScalar
infoBootControllerName = _InfoBootControllerName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 150),
    _InfoBootControllerName_Type()
)
infoBootControllerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoBootControllerName.setStatus("current")
_InfoBootControllerModelNumber_Type = DisplayString
_InfoBootControllerModelNumber_Object = MibScalar
infoBootControllerModelNumber = _InfoBootControllerModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 151),
    _InfoBootControllerModelNumber_Type()
)
infoBootControllerModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoBootControllerModelNumber.setStatus("current")
_InfoBootControllerSerialNumber_Type = DisplayString
_InfoBootControllerSerialNumber_Object = MibScalar
infoBootControllerSerialNumber = _InfoBootControllerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 152),
    _InfoBootControllerSerialNumber_Type()
)
infoBootControllerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoBootControllerSerialNumber.setStatus("current")
_InfoBootControllerFirmwareVersion_Type = DisplayString
_InfoBootControllerFirmwareVersion_Object = MibScalar
infoBootControllerFirmwareVersion = _InfoBootControllerFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 153),
    _InfoBootControllerFirmwareVersion_Type()
)
infoBootControllerFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoBootControllerFirmwareVersion.setStatus("current")
_InfoBootControllerBiosVersion_Type = DisplayString
_InfoBootControllerBiosVersion_Object = MibScalar
infoBootControllerBiosVersion = _InfoBootControllerBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 154),
    _InfoBootControllerBiosVersion_Type()
)
infoBootControllerBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoBootControllerBiosVersion.setStatus("current")
_InfoBootControllerDriverVersion_Type = DisplayString
_InfoBootControllerDriverVersion_Object = MibScalar
infoBootControllerDriverVersion = _InfoBootControllerDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 155),
    _InfoBootControllerDriverVersion_Type()
)
infoBootControllerDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoBootControllerDriverVersion.setStatus("current")
_InfoWarrantyPartNumber_Type = DisplayString
_InfoWarrantyPartNumber_Object = MibScalar
infoWarrantyPartNumber = _InfoWarrantyPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 156),
    _InfoWarrantyPartNumber_Type()
)
infoWarrantyPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoWarrantyPartNumber.setStatus("current")
_InfoWarrantySerialNumber_Type = DisplayString
_InfoWarrantySerialNumber_Object = MibScalar
infoWarrantySerialNumber = _InfoWarrantySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 157),
    _InfoWarrantySerialNumber_Type()
)
infoWarrantySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoWarrantySerialNumber.setStatus("current")
_InfoWarrantyLicenseNumber_Type = DisplayString
_InfoWarrantyLicenseNumber_Object = MibScalar
infoWarrantyLicenseNumber = _InfoWarrantyLicenseNumber_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 1, 158),
    _InfoWarrantyLicenseNumber_Type()
)
infoWarrantyLicenseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoWarrantyLicenseNumber.setStatus("current")

# Managed Objects groups

lefthandNetworksNsmInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 2, 1, 2, 1)
)
lefthandNetworksNsmInfoGroup.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoModel"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoHostname"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoIP"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoMAC"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoChassisUUID"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoProductName"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoProductID"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoSupportKey"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoHardwareDescription"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoSoftwareType"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoHPsmhdVersion"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoHPSNMPAgent"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoBIOSVersion"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoControllerCount"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoControllerName"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoControllerModelNumber"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoControllerSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoControllerFirmwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoControllerBiosVersion"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoControllerDriverVersion"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheCount"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheName"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheModel"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheSize"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheHardwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheFirmwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheDriverVersion"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheBpsVoltage"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheBpsTestOverdue"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheBpsState"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheBpsStatus"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheEnabled"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheMode"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheState"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheStatus"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoBackplaneCount"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoBackplaneName"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoBackplaneSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoBackplaneFirmwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoBackplaneIDLed"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoFanCount"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoFanName"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoFanSpeed"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoFanMinSpeed"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoFanState"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoFanStatus"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoTemperatureSensorCount"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoTemperatureSensorName"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoTemperatureSensorValue"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoTemperatureSensorCritical"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoTemperatureSensorLimit"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoTemperatureSensorState"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoTemperatureSensorStatus"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoPowerSupplyCount"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoPowerSupplyName"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoPowerSupplyState"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoPowerSupplyStatus"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoPowerSupplyMode"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoVoltageSensorCount"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoVoltageSensorName"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoVoltageSensorValue"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoVoltageSensorLowLimit"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoVoltageSensorHighLimit"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoVoltageSensorState"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoVoltageSensorStatus"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoBootControllerName"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoBootControllerModelNumber"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoBootControllerSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoBootControllerFirmwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoBootControllerBiosVersion"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoBootControllerDriverVersion"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoWarrantyPartNumber"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoWarrantySerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoWarrantyLicenseNumber"))
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmInfoGroup.setStatus("current")

lefthandNetworksNsmInfoGroupObsolete = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 2, 1, 2, 2)
)
lefthandNetworksNsmInfoGroupObsolete.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoSerialNumberOld"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoModelOld"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoSoftwareVersionOld"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoEnclosureFirmwareVersionOld"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoMotherboardTemperature"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCPUCount"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoFlashCount"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoDriveCardCount"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheBatteryCount"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCPUTemperature"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCPUFanSpeed"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoObsoletePowerSupplyCount"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoObsoletePowerSupplyState"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoObsoleteFanCount"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoObsoleteFanState"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoFanStatus"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoFlashState"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoDriveCardModel"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoDriveCardBiosVersion"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoDriveCardFirmwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheBatteryState"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoControllerRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoCacheRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoBackplaneRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoFanRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoTemperatureSensorRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoPowerSupplyRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "infoVoltageSensorRowStatus"))
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmInfoGroupObsolete.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lefthandNetworksNsmInfoMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 2, 1, 1, 1)
)
lefthandNetworksNsmInfoMibCompliance.setObjects(
    ("LEFTHAND-NETWORKS-NSM-INFO-MIB", "lefthandNetworksNsmInfoGroup")
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmInfoMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-NSM-INFO-MIB",
    **{"lhnNsmInfoModule": lhnNsmInfoModule,
       "lhnNsmInfoModuleConformance": lhnNsmInfoModuleConformance,
       "lhnNsmInfoModuleCompliances": lhnNsmInfoModuleCompliances,
       "lefthandNetworksNsmInfoMibCompliance": lefthandNetworksNsmInfoMibCompliance,
       "lhnNsmInfoModuleGroups": lhnNsmInfoModuleGroups,
       "lefthandNetworksNsmInfoGroup": lefthandNetworksNsmInfoGroup,
       "lefthandNetworksNsmInfoGroupObsolete": lefthandNetworksNsmInfoGroupObsolete,
       "infoSerialNumberOld": infoSerialNumberOld,
       "infoModelOld": infoModelOld,
       "infoSoftwareVersionOld": infoSoftwareVersionOld,
       "infoEnclosureFirmwareVersionOld": infoEnclosureFirmwareVersionOld,
       "infoMotherboardTemperature": infoMotherboardTemperature,
       "infoCPUCount": infoCPUCount,
       "infoCPUTable": infoCPUTable,
       "infoCPUEntry": infoCPUEntry,
       "infoCPUIndex": infoCPUIndex,
       "infoCPUTemperature": infoCPUTemperature,
       "infoCPUFanSpeed": infoCPUFanSpeed,
       "infoObsoletePowerSupplyCount": infoObsoletePowerSupplyCount,
       "infoObsoletePowerSupplyTable": infoObsoletePowerSupplyTable,
       "infoObsoletePowerSupplyEntry": infoObsoletePowerSupplyEntry,
       "infoObsoletePowerSupplyIndex": infoObsoletePowerSupplyIndex,
       "infoObsoletePowerSupplyState": infoObsoletePowerSupplyState,
       "infoObsoleteFanCount": infoObsoleteFanCount,
       "infoObsoleteFanTable": infoObsoleteFanTable,
       "infoObsoleteFanEntry": infoObsoleteFanEntry,
       "infoObsoleteFanIndex": infoObsoleteFanIndex,
       "infoObsoleteFanState": infoObsoleteFanState,
       "infoFlashCount": infoFlashCount,
       "infoFlashTable": infoFlashTable,
       "infoFlashEntry": infoFlashEntry,
       "infoFlashIndex": infoFlashIndex,
       "infoFlashState": infoFlashState,
       "infoDriveCardCount": infoDriveCardCount,
       "infoDriveCardTable": infoDriveCardTable,
       "infoDriveCardEntry": infoDriveCardEntry,
       "infoDriveCardIndex": infoDriveCardIndex,
       "infoDriveCardModel": infoDriveCardModel,
       "infoDriveCardBiosVersion": infoDriveCardBiosVersion,
       "infoDriveCardFirmwareVersion": infoDriveCardFirmwareVersion,
       "infoCacheBatteryCount": infoCacheBatteryCount,
       "infoCacheBatteryTable": infoCacheBatteryTable,
       "infoCacheBatteryEntry": infoCacheBatteryEntry,
       "infoCacheBatteryIndex": infoCacheBatteryIndex,
       "infoCacheBatteryState": infoCacheBatteryState,
       "infoModel": infoModel,
       "infoHostname": infoHostname,
       "infoIP": infoIP,
       "infoMAC": infoMAC,
       "infoSerialNumber": infoSerialNumber,
       "infoChassisUUID": infoChassisUUID,
       "infoProductName": infoProductName,
       "infoProductID": infoProductID,
       "infoSupportKey": infoSupportKey,
       "infoHardwareDescription": infoHardwareDescription,
       "infoSoftwareType": infoSoftwareType,
       "infoSoftwareVersion": infoSoftwareVersion,
       "infoHPsmhdVersion": infoHPsmhdVersion,
       "infoHPSNMPAgent": infoHPSNMPAgent,
       "infoBIOSVersion": infoBIOSVersion,
       "infoControllerCount": infoControllerCount,
       "infoControllerTable": infoControllerTable,
       "infoControllerEntry": infoControllerEntry,
       "infoControllerIndex": infoControllerIndex,
       "infoControllerName": infoControllerName,
       "infoControllerModelNumber": infoControllerModelNumber,
       "infoControllerSerialNumber": infoControllerSerialNumber,
       "infoControllerFirmwareVersion": infoControllerFirmwareVersion,
       "infoControllerBiosVersion": infoControllerBiosVersion,
       "infoControllerDriverVersion": infoControllerDriverVersion,
       "infoControllerRowStatus": infoControllerRowStatus,
       "infoCacheCount": infoCacheCount,
       "infoCacheTable": infoCacheTable,
       "infoCacheEntry": infoCacheEntry,
       "infoCacheIndex": infoCacheIndex,
       "infoCacheName": infoCacheName,
       "infoCacheModel": infoCacheModel,
       "infoCacheSize": infoCacheSize,
       "infoCacheSerialNumber": infoCacheSerialNumber,
       "infoCacheHardwareVersion": infoCacheHardwareVersion,
       "infoCacheFirmwareVersion": infoCacheFirmwareVersion,
       "infoCacheDriverVersion": infoCacheDriverVersion,
       "infoCacheBpsVoltage": infoCacheBpsVoltage,
       "infoCacheBpsTestOverdue": infoCacheBpsTestOverdue,
       "infoCacheBpsState": infoCacheBpsState,
       "infoCacheBpsStatus": infoCacheBpsStatus,
       "infoCacheEnabled": infoCacheEnabled,
       "infoCacheMode": infoCacheMode,
       "infoCacheState": infoCacheState,
       "infoCacheStatus": infoCacheStatus,
       "infoCacheRowStatus": infoCacheRowStatus,
       "infoBackplaneCount": infoBackplaneCount,
       "infoBackplaneTable": infoBackplaneTable,
       "infoBackplaneEntry": infoBackplaneEntry,
       "infoBackplaneIndex": infoBackplaneIndex,
       "infoBackplaneName": infoBackplaneName,
       "infoBackplaneSerialNumber": infoBackplaneSerialNumber,
       "infoBackplaneFirmwareVersion": infoBackplaneFirmwareVersion,
       "infoBackplaneIDLed": infoBackplaneIDLed,
       "infoBackplaneRowStatus": infoBackplaneRowStatus,
       "infoFanCount": infoFanCount,
       "infoFanTable": infoFanTable,
       "infoFanEntry": infoFanEntry,
       "infoFanIndex": infoFanIndex,
       "infoFanName": infoFanName,
       "infoFanSpeed": infoFanSpeed,
       "infoFanMinSpeed": infoFanMinSpeed,
       "infoFanState": infoFanState,
       "infoFanStatus": infoFanStatus,
       "infoFanRowStatus": infoFanRowStatus,
       "infoTemperatureSensorCount": infoTemperatureSensorCount,
       "infoTemperatureSensorTable": infoTemperatureSensorTable,
       "infoTemperatureSensorEntry": infoTemperatureSensorEntry,
       "infoTemperatureSensorIndex": infoTemperatureSensorIndex,
       "infoTemperatureSensorName": infoTemperatureSensorName,
       "infoTemperatureSensorValue": infoTemperatureSensorValue,
       "infoTemperatureSensorCritical": infoTemperatureSensorCritical,
       "infoTemperatureSensorLimit": infoTemperatureSensorLimit,
       "infoTemperatureSensorState": infoTemperatureSensorState,
       "infoTemperatureSensorStatus": infoTemperatureSensorStatus,
       "infoTemperatureSensorRowStatus": infoTemperatureSensorRowStatus,
       "infoPowerSupplyCount": infoPowerSupplyCount,
       "infoPowerSupplyTable": infoPowerSupplyTable,
       "infoPowerSupplyEntry": infoPowerSupplyEntry,
       "infoPowerSupplyIndex": infoPowerSupplyIndex,
       "infoPowerSupplyName": infoPowerSupplyName,
       "infoPowerSupplyState": infoPowerSupplyState,
       "infoPowerSupplyStatus": infoPowerSupplyStatus,
       "infoPowerSupplyRowStatus": infoPowerSupplyRowStatus,
       "infoPowerSupplyMode": infoPowerSupplyMode,
       "infoVoltageSensorCount": infoVoltageSensorCount,
       "infoVoltageSensorTable": infoVoltageSensorTable,
       "infoVoltageSensorEntry": infoVoltageSensorEntry,
       "infoVoltageSensorIndex": infoVoltageSensorIndex,
       "infoVoltageSensorName": infoVoltageSensorName,
       "infoVoltageSensorValue": infoVoltageSensorValue,
       "infoVoltageSensorLowLimit": infoVoltageSensorLowLimit,
       "infoVoltageSensorHighLimit": infoVoltageSensorHighLimit,
       "infoVoltageSensorState": infoVoltageSensorState,
       "infoVoltageSensorStatus": infoVoltageSensorStatus,
       "infoVoltageSensorRowStatus": infoVoltageSensorRowStatus,
       "infoBootControllerName": infoBootControllerName,
       "infoBootControllerModelNumber": infoBootControllerModelNumber,
       "infoBootControllerSerialNumber": infoBootControllerSerialNumber,
       "infoBootControllerFirmwareVersion": infoBootControllerFirmwareVersion,
       "infoBootControllerBiosVersion": infoBootControllerBiosVersion,
       "infoBootControllerDriverVersion": infoBootControllerDriverVersion,
       "infoWarrantyPartNumber": infoWarrantyPartNumber,
       "infoWarrantySerialNumber": infoWarrantySerialNumber,
       "infoWarrantyLicenseNumber": infoWarrantyLicenseNumber}
)
