# SNMP MIB module (LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:42:21 2025
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

(lhnNsmEvents,
 lhnNsmNotification,
 lhnNsmOldEvents,
 lhnNsmOldNotification) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-NSM-MIB",
    "lhnNsmEvents",
    "lhnNsmNotification",
    "lhnNsmOldEvents",
    "lhnNsmOldNotification")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lhnNsmNotificationModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 15)
)
if mibBuilder.loadTexts:
    lhnNsmNotificationModule.setRevisions(
        ("2013-11-22 00:00",
         "2013-06-25 00:00",
         "2012-10-12 00:00",
         "2012-09-18 00:00",
         "2012-09-04 00:00",
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

_LhnNsmNotificationModuleConformance_ObjectIdentity = ObjectIdentity
lhnNsmNotificationModuleConformance = _LhnNsmNotificationModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 15, 1)
)
_LhnNsmNotificationModuleCompliances_ObjectIdentity = ObjectIdentity
lhnNsmNotificationModuleCompliances = _LhnNsmNotificationModuleCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 15, 1, 1)
)
_LhnNsmNotificationModuleGroups_ObjectIdentity = ObjectIdentity
lhnNsmNotificationModuleGroups = _LhnNsmNotificationModuleGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 15, 1, 2)
)
_LhnNsmDevices_ObjectIdentity = ObjectIdentity
lhnNsmDevices = _LhnNsmDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1)
)
if mibBuilder.loadTexts:
    lhnNsmDevices.setStatus("current")
_LhnNsmEvents_ObjectIdentity = ObjectIdentity
lhnNsmEvents = _LhnNsmEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0)
)
if mibBuilder.loadTexts:
    lhnNsmEvents.setStatus("current")
_LhnNotificationOldMessageCount_Type = Integer32
_LhnNotificationOldMessageCount_Object = MibScalar
lhnNotificationOldMessageCount = _LhnNotificationOldMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 1),
    _LhnNotificationOldMessageCount_Type()
)
lhnNotificationOldMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnNotificationOldMessageCount.setStatus("current")
_LhnNotificationOldMessageTable_Object = MibTable
lhnNotificationOldMessageTable = _LhnNotificationOldMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2)
)
if mibBuilder.loadTexts:
    lhnNotificationOldMessageTable.setStatus("current")
_LhnNotificationOldMessageEntry_Object = MibTableRow
lhnNotificationOldMessageEntry = _LhnNotificationOldMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2, 1)
)
lhnNotificationOldMessageEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNotificationIndex"),
)
if mibBuilder.loadTexts:
    lhnNotificationOldMessageEntry.setStatus("current")
_LhnNotificationIndex_Type = Unsigned32
_LhnNotificationIndex_Object = MibTableColumn
lhnNotificationIndex = _LhnNotificationIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2, 1, 1),
    _LhnNotificationIndex_Type()
)
lhnNotificationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lhnNotificationIndex.setStatus("current")
_LhnNotificationMessage_Type = DisplayString
_LhnNotificationMessage_Object = MibTableColumn
lhnNotificationMessage = _LhnNotificationMessage_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2, 1, 2),
    _LhnNotificationMessage_Type()
)
lhnNotificationMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnNotificationMessage.setStatus("current")
_LhnNotificationTime_Type = DateAndTime
_LhnNotificationTime_Object = MibTableColumn
lhnNotificationTime = _LhnNotificationTime_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2, 1, 3),
    _LhnNotificationTime_Type()
)
lhnNotificationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnNotificationTime.setStatus("current")
_LhnNotificationMessageCount_Type = Integer32
_LhnNotificationMessageCount_Object = MibScalar
lhnNotificationMessageCount = _LhnNotificationMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 1),
    _LhnNotificationMessageCount_Type()
)
lhnNotificationMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnNotificationMessageCount.setStatus("current")
_LhnNotificationMessageTable_Object = MibTable
lhnNotificationMessageTable = _LhnNotificationMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2)
)
if mibBuilder.loadTexts:
    lhnNotificationMessageTable.setStatus("current")
_LhnNotificationMessageEntry_Object = MibTableRow
lhnNotificationMessageEntry = _LhnNotificationMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1)
)
lhnNotificationMessageEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNotificationMessageIndex"),
)
if mibBuilder.loadTexts:
    lhnNotificationMessageEntry.setStatus("current")
_LhnNotificationMessageIndex_Type = Unsigned32
_LhnNotificationMessageIndex_Object = MibTableColumn
lhnNotificationMessageIndex = _LhnNotificationMessageIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 1),
    _LhnNotificationMessageIndex_Type()
)
lhnNotificationMessageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lhnNotificationMessageIndex.setStatus("current")
_LhnMessage_Type = DisplayString
_LhnMessage_Object = MibTableColumn
lhnMessage = _LhnMessage_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 2),
    _LhnMessage_Type()
)
lhnMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnMessage.setStatus("current")
_LhnMessageTime_Type = DateAndTime
_LhnMessageTime_Object = MibTableColumn
lhnMessageTime = _LhnMessageTime_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 3),
    _LhnMessageTime_Type()
)
lhnMessageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnMessageTime.setStatus("current")
_LhnEventID_Type = DisplayString
_LhnEventID_Object = MibTableColumn
lhnEventID = _LhnEventID_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 4),
    _LhnEventID_Type()
)
lhnEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnEventID.setStatus("current")


class _LhnSeverity_Type(Integer32):
    """Custom type lhnSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 0),
          ("warning", 1),
          ("info", 2))
    )


_LhnSeverity_Type.__name__ = "Integer32"
_LhnSeverity_Object = MibTableColumn
lhnSeverity = _LhnSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 5),
    _LhnSeverity_Type()
)
lhnSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnSeverity.setStatus("current")
_LhnHostname_Type = DisplayString
_LhnHostname_Object = MibTableColumn
lhnHostname = _LhnHostname_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 6),
    _LhnHostname_Type()
)
lhnHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnHostname.setStatus("current")
_LhnPrimaryIP_Type = DisplayString
_LhnPrimaryIP_Object = MibTableColumn
lhnPrimaryIP = _LhnPrimaryIP_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 7),
    _LhnPrimaryIP_Type()
)
lhnPrimaryIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnPrimaryIP.setStatus("current")
_LhnMac_Type = DisplayString
_LhnMac_Object = MibTableColumn
lhnMac = _LhnMac_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 8),
    _LhnMac_Type()
)
lhnMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnMac.setStatus("current")
_LhnSerialNumber_Type = DisplayString
_LhnSerialNumber_Object = MibTableColumn
lhnSerialNumber = _LhnSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 9),
    _LhnSerialNumber_Type()
)
lhnSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnSerialNumber.setStatus("current")
_LhnModelName_Type = DisplayString
_LhnModelName_Object = MibTableColumn
lhnModelName = _LhnModelName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 10),
    _LhnModelName_Type()
)
lhnModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnModelName.setStatus("current")
_LhnProductName_Type = DisplayString
_LhnProductName_Object = MibTableColumn
lhnProductName = _LhnProductName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 11),
    _LhnProductName_Type()
)
lhnProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnProductName.setStatus("current")
_LhnProductID_Type = DisplayString
_LhnProductID_Object = MibTableColumn
lhnProductID = _LhnProductID_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 12),
    _LhnProductID_Type()
)
lhnProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnProductID.setStatus("current")
_LhnHpim_Type = TruthValue
_LhnHpim_Object = MibTableColumn
lhnHpim = _LhnHpim_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 13),
    _LhnHpim_Type()
)
lhnHpim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnHpim.setStatus("current")
_LhnSoftwareVersion_Type = DisplayString
_LhnSoftwareVersion_Object = MibTableColumn
lhnSoftwareVersion = _LhnSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 14),
    _LhnSoftwareVersion_Type()
)
lhnSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnSoftwareVersion.setStatus("current")
_LhnManagementGroupVersion_Type = DisplayString
_LhnManagementGroupVersion_Object = MibTableColumn
lhnManagementGroupVersion = _LhnManagementGroupVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 15),
    _LhnManagementGroupVersion_Type()
)
lhnManagementGroupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnManagementGroupVersion.setStatus("current")
_LhnManagementGroupSerialNumber_Type = DisplayString
_LhnManagementGroupSerialNumber_Object = MibTableColumn
lhnManagementGroupSerialNumber = _LhnManagementGroupSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 16),
    _LhnManagementGroupSerialNumber_Type()
)
lhnManagementGroupSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnManagementGroupSerialNumber.setStatus("current")
_LhnManagementGroup_Type = DisplayString
_LhnManagementGroup_Object = MibTableColumn
lhnManagementGroup = _LhnManagementGroup_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 17),
    _LhnManagementGroup_Type()
)
lhnManagementGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnManagementGroup.setStatus("current")
_LhnCluster_Type = DisplayString
_LhnCluster_Object = MibTableColumn
lhnCluster = _LhnCluster_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 18),
    _LhnCluster_Type()
)
lhnCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnCluster.setStatus("current")
_LhnSite_Type = DisplayString
_LhnSite_Object = MibTableColumn
lhnSite = _LhnSite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 19),
    _LhnSite_Type()
)
lhnSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnSite.setStatus("current")
_LhnComponentName_Type = DisplayString
_LhnComponentName_Object = MibTableColumn
lhnComponentName = _LhnComponentName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 20),
    _LhnComponentName_Type()
)
lhnComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnComponentName.setStatus("current")
_LhnSystemName_Type = DisplayString
_LhnSystemName_Object = MibTableColumn
lhnSystemName = _LhnSystemName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 21),
    _LhnSystemName_Type()
)
lhnSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnSystemName.setStatus("current")
_LhnLogicalName_Type = DisplayString
_LhnLogicalName_Object = MibTableColumn
lhnLogicalName = _LhnLogicalName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 22),
    _LhnLogicalName_Type()
)
lhnLogicalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnLogicalName.setStatus("current")
_LhnComponentState_Type = DisplayString
_LhnComponentState_Object = MibTableColumn
lhnComponentState = _LhnComponentState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 23),
    _LhnComponentState_Type()
)
lhnComponentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnComponentState.setStatus("current")
_LhnComponentModel_Type = DisplayString
_LhnComponentModel_Object = MibTableColumn
lhnComponentModel = _LhnComponentModel_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 24),
    _LhnComponentModel_Type()
)
lhnComponentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnComponentModel.setStatus("current")
_LhnComponentSerialNumber_Type = DisplayString
_LhnComponentSerialNumber_Object = MibTableColumn
lhnComponentSerialNumber = _LhnComponentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 25),
    _LhnComponentSerialNumber_Type()
)
lhnComponentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnComponentSerialNumber.setStatus("current")
_LhnComponentFirmwareVersion_Type = DisplayString
_LhnComponentFirmwareVersion_Object = MibTableColumn
lhnComponentFirmwareVersion = _LhnComponentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 26),
    _LhnComponentFirmwareVersion_Type()
)
lhnComponentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnComponentFirmwareVersion.setStatus("current")
_LhnComponentHardwareVersion_Type = DisplayString
_LhnComponentHardwareVersion_Object = MibTableColumn
lhnComponentHardwareVersion = _LhnComponentHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 27),
    _LhnComponentHardwareVersion_Type()
)
lhnComponentHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnComponentHardwareVersion.setStatus("current")
_LhnDriverVersion_Type = DisplayString
_LhnDriverVersion_Object = MibTableColumn
lhnDriverVersion = _LhnDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 28),
    _LhnDriverVersion_Type()
)
lhnDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnDriverVersion.setStatus("current")
_LhnBiosVersion_Type = DisplayString
_LhnBiosVersion_Object = MibTableColumn
lhnBiosVersion = _LhnBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 29),
    _LhnBiosVersion_Type()
)
lhnBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnBiosVersion.setStatus("current")
_LhnRaidConfiguration_Type = DisplayString
_LhnRaidConfiguration_Object = MibTableColumn
lhnRaidConfiguration = _LhnRaidConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 30),
    _LhnRaidConfiguration_Type()
)
lhnRaidConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnRaidConfiguration.setStatus("current")
_LhnDiskInterface_Type = DisplayString
_LhnDiskInterface_Object = MibTableColumn
lhnDiskInterface = _LhnDiskInterface_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 31),
    _LhnDiskInterface_Type()
)
lhnDiskInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnDiskInterface.setStatus("current")
_LhnDiskCapacity_Type = Integer32
_LhnDiskCapacity_Object = MibTableColumn
lhnDiskCapacity = _LhnDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 32),
    _LhnDiskCapacity_Type()
)
lhnDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnDiskCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lhnDiskCapacity.setUnits("MB")
_LhnRaidState_Type = DisplayString
_LhnRaidState_Object = MibTableColumn
lhnRaidState = _LhnRaidState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 33),
    _LhnRaidState_Type()
)
lhnRaidState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnRaidState.setStatus("current")
_LhnParityInitStatus_Type = DisplayString
_LhnParityInitStatus_Object = MibTableColumn
lhnParityInitStatus = _LhnParityInitStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 34),
    _LhnParityInitStatus_Type()
)
lhnParityInitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnParityInitStatus.setStatus("current")
_LhnHealthState_Type = DisplayString
_LhnHealthState_Object = MibTableColumn
lhnHealthState = _LhnHealthState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 35),
    _LhnHealthState_Type()
)
lhnHealthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnHealthState.setStatus("current")
_LhnBpsState_Type = DisplayString
_LhnBpsState_Object = MibTableColumn
lhnBpsState = _LhnBpsState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 36),
    _LhnBpsState_Type()
)
lhnBpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnBpsState.setStatus("current")
_LhnCacheState_Type = DisplayString
_LhnCacheState_Object = MibTableColumn
lhnCacheState = _LhnCacheState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 37),
    _LhnCacheState_Type()
)
lhnCacheState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnCacheState.setStatus("current")
_LhnLinkState_Type = DisplayString
_LhnLinkState_Object = MibTableColumn
lhnLinkState = _LhnLinkState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 38),
    _LhnLinkState_Type()
)
lhnLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnLinkState.setStatus("current")
_LhnVipState_Type = DisplayString
_LhnVipState_Object = MibTableColumn
lhnVipState = _LhnVipState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 39),
    _LhnVipState_Type()
)
lhnVipState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnVipState.setStatus("current")
_LhnMaintenanceMode_Type = DisplayString
_LhnMaintenanceMode_Object = MibTableColumn
lhnMaintenanceMode = _LhnMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 40),
    _LhnMaintenanceMode_Type()
)
lhnMaintenanceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnMaintenanceMode.setStatus("current")
_LhnMinFanSpeed_Type = Integer32
_LhnMinFanSpeed_Object = MibTableColumn
lhnMinFanSpeed = _LhnMinFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 41),
    _LhnMinFanSpeed_Type()
)
lhnMinFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnMinFanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    lhnMinFanSpeed.setUnits("RPM")
_LhnFanSpeed_Type = Gauge32
_LhnFanSpeed_Object = MibTableColumn
lhnFanSpeed = _LhnFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 42),
    _LhnFanSpeed_Type()
)
lhnFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnFanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    lhnFanSpeed.setUnits("RPM")
_LhnHighTemperatureLimit_Type = Integer32
_LhnHighTemperatureLimit_Object = MibTableColumn
lhnHighTemperatureLimit = _LhnHighTemperatureLimit_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 43),
    _LhnHighTemperatureLimit_Type()
)
lhnHighTemperatureLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnHighTemperatureLimit.setStatus("current")
if mibBuilder.loadTexts:
    lhnHighTemperatureLimit.setUnits("Celsius")
_LhnTemperatureState_Type = DisplayString
_LhnTemperatureState_Object = MibTableColumn
lhnTemperatureState = _LhnTemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 44),
    _LhnTemperatureState_Type()
)
lhnTemperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnTemperatureState.setStatus("current")
_LhnTemperature_Type = Gauge32
_LhnTemperature_Object = MibTableColumn
lhnTemperature = _LhnTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 45),
    _LhnTemperature_Type()
)
lhnTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnTemperature.setStatus("current")
if mibBuilder.loadTexts:
    lhnTemperature.setUnits("Celsius")
_LhnHighVoltageLimit_Type = Integer32
_LhnHighVoltageLimit_Object = MibTableColumn
lhnHighVoltageLimit = _LhnHighVoltageLimit_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 46),
    _LhnHighVoltageLimit_Type()
)
lhnHighVoltageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnHighVoltageLimit.setStatus("current")
if mibBuilder.loadTexts:
    lhnHighVoltageLimit.setUnits("Volts")
_LhnLowVoltageLimit_Type = Integer32
_LhnLowVoltageLimit_Object = MibTableColumn
lhnLowVoltageLimit = _LhnLowVoltageLimit_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 47),
    _LhnLowVoltageLimit_Type()
)
lhnLowVoltageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnLowVoltageLimit.setStatus("current")
if mibBuilder.loadTexts:
    lhnLowVoltageLimit.setUnits("Volts")
_LhnVoltage_Type = Gauge32
_LhnVoltage_Object = MibTableColumn
lhnVoltage = _LhnVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 48),
    _LhnVoltage_Type()
)
lhnVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnVoltage.setStatus("current")
if mibBuilder.loadTexts:
    lhnVoltage.setUnits("Volts")
_LhnUtilization_Type = Gauge32
_LhnUtilization_Object = MibTableColumn
lhnUtilization = _LhnUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 49),
    _LhnUtilization_Type()
)
lhnUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnUtilization.setStatus("current")
if mibBuilder.loadTexts:
    lhnUtilization.setUnits("%")
_LhnLatency_Type = Gauge32
_LhnLatency_Object = MibTableColumn
lhnLatency = _LhnLatency_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 50),
    _LhnLatency_Type()
)
lhnLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnLatency.setStatus("current")
if mibBuilder.loadTexts:
    lhnLatency.setUnits("ms")
_LhnMemoryUtilization_Type = Gauge32
_LhnMemoryUtilization_Object = MibTableColumn
lhnMemoryUtilization = _LhnMemoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 51),
    _LhnMemoryUtilization_Type()
)
lhnMemoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnMemoryUtilization.setStatus("current")
if mibBuilder.loadTexts:
    lhnMemoryUtilization.setUnits("%")
_LhnMemoryConfig_Type = Integer32
_LhnMemoryConfig_Object = MibTableColumn
lhnMemoryConfig = _LhnMemoryConfig_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 52),
    _LhnMemoryConfig_Type()
)
lhnMemoryConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnMemoryConfig.setStatus("current")
if mibBuilder.loadTexts:
    lhnMemoryConfig.setUnits("MB")
_LhnCpuUtilization_Type = Gauge32
_LhnCpuUtilization_Object = MibTableColumn
lhnCpuUtilization = _LhnCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 53),
    _LhnCpuUtilization_Type()
)
lhnCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnCpuUtilization.setStatus("current")
if mibBuilder.loadTexts:
    lhnCpuUtilization.setUnits("%")
_LhnCpuConfig_Type = Integer32
_LhnCpuConfig_Object = MibTableColumn
lhnCpuConfig = _LhnCpuConfig_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 54),
    _LhnCpuConfig_Type()
)
lhnCpuConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnCpuConfig.setStatus("current")
if mibBuilder.loadTexts:
    lhnCpuConfig.setUnits("cores")
_LhnDiskSpeed_Type = DisplayString
_LhnDiskSpeed_Object = MibTableColumn
lhnDiskSpeed = _LhnDiskSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 55),
    _LhnDiskSpeed_Type()
)
lhnDiskSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnDiskSpeed.setStatus("current")
_LhnLicenseState_Type = DisplayString
_LhnLicenseState_Object = MibTableColumn
lhnLicenseState = _LhnLicenseState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 56),
    _LhnLicenseState_Type()
)
lhnLicenseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnLicenseState.setStatus("current")
_LhnUtilizationState_Type = DisplayString
_LhnUtilizationState_Object = MibTableColumn
lhnUtilizationState = _LhnUtilizationState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 57),
    _LhnUtilizationState_Type()
)
lhnUtilizationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnUtilizationState.setStatus("current")
_LhnLatencyState_Type = DisplayString
_LhnLatencyState_Object = MibTableColumn
lhnLatencyState = _LhnLatencyState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 58),
    _LhnLatencyState_Type()
)
lhnLatencyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnLatencyState.setStatus("current")
_LhnServerVIPAddress_Type = DisplayString
_LhnServerVIPAddress_Object = MibTableColumn
lhnServerVIPAddress = _LhnServerVIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 59),
    _LhnServerVIPAddress_Type()
)
lhnServerVIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnServerVIPAddress.setStatus("current")
_LhnServerVIPState_Type = DisplayString
_LhnServerVIPState_Object = MibTableColumn
lhnServerVIPState = _LhnServerVIPState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 60),
    _LhnServerVIPState_Type()
)
lhnServerVIPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnServerVIPState.setStatus("current")
_LhnReplicationState_Type = DisplayString
_LhnReplicationState_Object = MibTableColumn
lhnReplicationState = _LhnReplicationState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 61),
    _LhnReplicationState_Type()
)
lhnReplicationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnReplicationState.setStatus("current")
_LhnSnapshotState_Type = DisplayString
_LhnSnapshotState_Object = MibTableColumn
lhnSnapshotState = _LhnSnapshotState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 62),
    _LhnSnapshotState_Type()
)
lhnSnapshotState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnSnapshotState.setStatus("current")
_LhnSnapshotSchedState_Type = DisplayString
_LhnSnapshotSchedState_Object = MibTableColumn
lhnSnapshotSchedState = _LhnSnapshotSchedState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 63),
    _LhnSnapshotSchedState_Type()
)
lhnSnapshotSchedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnSnapshotSchedState.setStatus("current")
_LhnWarrantyPartNumber_Type = DisplayString
_LhnWarrantyPartNumber_Object = MibTableColumn
lhnWarrantyPartNumber = _LhnWarrantyPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 64),
    _LhnWarrantyPartNumber_Type()
)
lhnWarrantyPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnWarrantyPartNumber.setStatus("current")
_LhnWarrantySerialNumber_Type = DisplayString
_LhnWarrantySerialNumber_Object = MibTableColumn
lhnWarrantySerialNumber = _LhnWarrantySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 65),
    _LhnWarrantySerialNumber_Type()
)
lhnWarrantySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnWarrantySerialNumber.setStatus("current")
_LhnWarrantyLicenseNumber_Type = DisplayString
_LhnWarrantyLicenseNumber_Object = MibTableColumn
lhnWarrantyLicenseNumber = _LhnWarrantyLicenseNumber_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 66),
    _LhnWarrantyLicenseNumber_Type()
)
lhnWarrantyLicenseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnWarrantyLicenseNumber.setStatus("current")
_LhnWearState_Type = DisplayString
_LhnWearState_Object = MibTableColumn
lhnWearState = _LhnWearState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 67),
    _LhnWearState_Type()
)
lhnWearState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnWearState.setStatus("current")
_LhnWearDays_Type = Integer32
_LhnWearDays_Object = MibTableColumn
lhnWearDays = _LhnWearDays_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 68),
    _LhnWearDays_Type()
)
lhnWearDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnWearDays.setStatus("current")
_LhnWearPercent_Type = Gauge32
_LhnWearPercent_Object = MibTableColumn
lhnWearPercent = _LhnWearPercent_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 15, 2, 1, 69),
    _LhnWearPercent_Type()
)
lhnWearPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lhnWearPercent.setStatus("current")
if mibBuilder.loadTexts:
    lhnWearPercent.setUnits("%")

# Managed Objects groups

lefthandNetworksNsmNotificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 15, 1, 2, 1)
)
lefthandNetworksNsmNotificationGroup.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNotificationOldMessageCount"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNotificationMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNotificationTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNotificationMessageCount"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSystemName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnLogicalName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentModel"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentFirmwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentHardwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnDriverVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnBiosVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnRaidConfiguration"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnDiskInterface"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnDiskCapacity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnRaidState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnParityInitStatus"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHealthState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnBpsState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCacheState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnLinkState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnVipState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMaintenanceMode"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMinFanSpeed"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnFanSpeed"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHighTemperatureLimit"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnTemperatureState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnTemperature"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHighVoltageLimit"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnLowVoltageLimit"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnVoltage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnUtilization"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnLatency"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMemoryUtilization"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMemoryConfig"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCpuUtilization"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCpuConfig"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnDiskSpeed"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnLicenseState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnUtilizationState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnLatencyState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnServerVIPAddress"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnServerVIPState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnReplicationState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSnapshotState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSnapshotSchedState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyPartNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantySerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyLicenseNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWearState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWearDays"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWearPercent"))
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmNotificationGroup.setStatus("current")


# Notification objects

lhnNsmNotificationGeneric = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 1)
)
lhnNsmNotificationGeneric.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyPartNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantySerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyLicenseNumber"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationGeneric.setStatus(
        "current"
    )

lhnNsmNotificationBackplane = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 2)
)
lhnNsmNotificationBackplane.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentFirmwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyPartNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantySerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyLicenseNumber"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationBackplane.setStatus(
        "current"
    )

lhnNsmNotificationController = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 3)
)
lhnNsmNotificationController.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentModel"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentHardwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentFirmwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnDriverVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnBiosVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCacheState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnBpsState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyPartNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantySerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyLicenseNumber"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationController.setStatus(
        "current"
    )

lhnNsmNotificationRAID = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 4)
)
lhnNsmNotificationRAID.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnRaidConfiguration"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnParityInitStatus"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyPartNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantySerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyLicenseNumber"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationRAID.setStatus(
        "current"
    )

lhnNsmNotificationDisk = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 5)
)
lhnNsmNotificationDisk.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentModel"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentFirmwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnDiskInterface"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnDiskCapacity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHealthState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnTemperatureState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnTemperature"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnDiskSpeed"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyPartNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantySerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyLicenseNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWearState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWearDays"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWearPercent"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationDisk.setStatus(
        "current"
    )

lhnNsmNotificationBootDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 6)
)
lhnNsmNotificationBootDevice.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyPartNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantySerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyLicenseNumber"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationBootDevice.setStatus(
        "current"
    )

lhnNsmNotificationFan = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 7)
)
lhnNsmNotificationFan.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMinFanSpeed"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnFanSpeed"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyPartNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantySerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyLicenseNumber"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationFan.setStatus(
        "current"
    )

lhnNsmNotificationTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 8)
)
lhnNsmNotificationTemperature.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHighTemperatureLimit"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnTemperature"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyPartNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantySerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyLicenseNumber"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationTemperature.setStatus(
        "current"
    )

lhnNsmNotificationPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 9)
)
lhnNsmNotificationPowerSupply.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyPartNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantySerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyLicenseNumber"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationPowerSupply.setStatus(
        "current"
    )

lhnNsmNotificationVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 10)
)
lhnNsmNotificationVoltage.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHighVoltageLimit"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnLowVoltageLimit"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnVoltage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyPartNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantySerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyLicenseNumber"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationVoltage.setStatus(
        "current"
    )

lhnNsmNotificationNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 11)
)
lhnNsmNotificationNetwork.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSystemName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnLogicalName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnLinkState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyPartNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantySerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyLicenseNumber"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationNetwork.setStatus(
        "current"
    )

lhnNsmNotificationMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 12)
)
lhnNsmNotificationMemory.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMemoryConfig"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMemoryUtilization"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyPartNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantySerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyLicenseNumber"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationMemory.setStatus(
        "current"
    )

lhnNsmNotificationCPU = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 13)
)
lhnNsmNotificationCPU.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCpuConfig"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCpuUtilization"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyPartNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantySerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnWarrantyLicenseNumber"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationCPU.setStatus(
        "current"
    )

lhnNsmNotificationLogging = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 14)
)
lhnNsmNotificationLogging.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnUtilization"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationLogging.setStatus(
        "current"
    )

lhnNsmNotificationManagementGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 15)
)
lhnNsmNotificationManagementGroup.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMaintenanceMode"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnLicenseState"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationManagementGroup.setStatus(
        "current"
    )

lhnNsmNotificationRemoteManagementGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 16)
)
lhnNsmNotificationRemoteManagementGroup.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentState"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationRemoteManagementGroup.setStatus(
        "current"
    )

lhnNsmNotificationCluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 17)
)
lhnNsmNotificationCluster.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnUtilization"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnVipState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnUtilizationState"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationCluster.setStatus(
        "current"
    )

lhnNsmNotificationStorageServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 18)
)
lhnNsmNotificationStorageServer.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnLatency"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnLatencyState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnServerVIPAddress"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnServerVIPState"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationStorageServer.setStatus(
        "current"
    )

lhnNsmNotificationRemoteCopy = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 19)
)
lhnNsmNotificationRemoteCopy.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnReplicationState"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationRemoteCopy.setStatus(
        "current"
    )

lhnNsmNotificationVolume = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 20)
)
lhnNsmNotificationVolume.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentState"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationVolume.setStatus(
        "current"
    )

lhnNsmNotificationSnapshot = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 21)
)
lhnNsmNotificationSnapshot.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSnapshotState"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationSnapshot.setStatus(
        "current"
    )

lhnNsmNotificationSnapshotSchedule = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 22)
)
lhnNsmNotificationSnapshotSchedule.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentState"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSnapshotSchedState"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationSnapshotSchedule.setStatus(
        "current"
    )

lhnNsmNotificationManager = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 23)
)
lhnNsmNotificationManager.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentState"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationManager.setStatus(
        "current"
    )

lhnNsmNotificationVirtualManager = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 24)
)
lhnNsmNotificationVirtualManager.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentState"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationVirtualManager.setStatus(
        "current"
    )

lhnNsmNotificationFailoverManager = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 25)
)
lhnNsmNotificationFailoverManager.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnComponentState"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationFailoverManager.setStatus(
        "current"
    )

lhnNsmNotificationConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 26)
)
lhnNsmNotificationConfiguration.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationConfiguration.setStatus(
        "current"
    )

lhnNsmNotificationResource = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 27)
)
lhnNsmNotificationResource.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationResource.setStatus(
        "current"
    )

lhnNsmNotificationService = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 28)
)
lhnNsmNotificationService.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationService.setStatus(
        "current"
    )

lhnNsmNotificationMountPoint = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 29)
)
lhnNsmNotificationMountPoint.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationMountPoint.setStatus(
        "current"
    )

lhnNsmNotificationPartition = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 0, 30)
)
lhnNsmNotificationPartition.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMessageTime"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnEventID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSeverity"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHostname"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnPrimaryIP"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnMac"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnModelName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductName"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnProductID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnHpim"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSoftwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupVersion"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroupSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnSite"))
)
if mibBuilder.loadTexts:
    lhnNsmNotificationPartition.setStatus(
        "current"
    )

lhnUserNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 3, 1)
)
lhnUserNotification.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNotificationMessage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNotificationTime"))
)
if mibBuilder.loadTexts:
    lhnUserNotification.setStatus(
        "current"
    )


# Notifications groups

lefthandNetworksNsmNotificationMibAllNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 15, 1, 2, 2)
)
lefthandNetworksNsmNotificationMibAllNotifications.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnUserNotification"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationGeneric"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationBackplane"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationController"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationRAID"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationDisk"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationBootDevice"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationFan"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationTemperature"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationPowerSupply"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationVoltage"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationNetwork"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationMemory"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationCPU"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationLogging"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationRemoteManagementGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationCluster"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationStorageServer"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationRemoteCopy"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationVolume"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationSnapshot"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationSnapshotSchedule"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationManager"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationVirtualManager"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationFailoverManager"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationConfiguration"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationResource"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationService"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationMountPoint"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lhnNsmNotificationPartition"))
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmNotificationMibAllNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lefthandNetworksNsmNotificationMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 15, 1, 1, 1)
)
lefthandNetworksNsmNotificationMibCompliance.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lefthandNetworksNsmNotificationGroup"),
        ("LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB", "lefthandNetworksNsmNotificationMibAllNotifications"))
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmNotificationMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-NSM-NOTIFICATION-MIB",
    **{"lhnNsmNotificationModule": lhnNsmNotificationModule,
       "lhnNsmNotificationModuleConformance": lhnNsmNotificationModuleConformance,
       "lhnNsmNotificationModuleCompliances": lhnNsmNotificationModuleCompliances,
       "lefthandNetworksNsmNotificationMibCompliance": lefthandNetworksNsmNotificationMibCompliance,
       "lhnNsmNotificationModuleGroups": lhnNsmNotificationModuleGroups,
       "lefthandNetworksNsmNotificationGroup": lefthandNetworksNsmNotificationGroup,
       "lefthandNetworksNsmNotificationMibAllNotifications": lefthandNetworksNsmNotificationMibAllNotifications,
       "lhnNsmDevices": lhnNsmDevices,
       "lhnNsmEvents": lhnNsmEvents,
       "lhnNsmNotificationGeneric": lhnNsmNotificationGeneric,
       "lhnNsmNotificationBackplane": lhnNsmNotificationBackplane,
       "lhnNsmNotificationController": lhnNsmNotificationController,
       "lhnNsmNotificationRAID": lhnNsmNotificationRAID,
       "lhnNsmNotificationDisk": lhnNsmNotificationDisk,
       "lhnNsmNotificationBootDevice": lhnNsmNotificationBootDevice,
       "lhnNsmNotificationFan": lhnNsmNotificationFan,
       "lhnNsmNotificationTemperature": lhnNsmNotificationTemperature,
       "lhnNsmNotificationPowerSupply": lhnNsmNotificationPowerSupply,
       "lhnNsmNotificationVoltage": lhnNsmNotificationVoltage,
       "lhnNsmNotificationNetwork": lhnNsmNotificationNetwork,
       "lhnNsmNotificationMemory": lhnNsmNotificationMemory,
       "lhnNsmNotificationCPU": lhnNsmNotificationCPU,
       "lhnNsmNotificationLogging": lhnNsmNotificationLogging,
       "lhnNsmNotificationManagementGroup": lhnNsmNotificationManagementGroup,
       "lhnNsmNotificationRemoteManagementGroup": lhnNsmNotificationRemoteManagementGroup,
       "lhnNsmNotificationCluster": lhnNsmNotificationCluster,
       "lhnNsmNotificationStorageServer": lhnNsmNotificationStorageServer,
       "lhnNsmNotificationRemoteCopy": lhnNsmNotificationRemoteCopy,
       "lhnNsmNotificationVolume": lhnNsmNotificationVolume,
       "lhnNsmNotificationSnapshot": lhnNsmNotificationSnapshot,
       "lhnNsmNotificationSnapshotSchedule": lhnNsmNotificationSnapshotSchedule,
       "lhnNsmNotificationManager": lhnNsmNotificationManager,
       "lhnNsmNotificationVirtualManager": lhnNsmNotificationVirtualManager,
       "lhnNsmNotificationFailoverManager": lhnNsmNotificationFailoverManager,
       "lhnNsmNotificationConfiguration": lhnNsmNotificationConfiguration,
       "lhnNsmNotificationResource": lhnNsmNotificationResource,
       "lhnNsmNotificationService": lhnNsmNotificationService,
       "lhnNsmNotificationMountPoint": lhnNsmNotificationMountPoint,
       "lhnNsmNotificationPartition": lhnNsmNotificationPartition,
       "lhnNotificationOldMessageCount": lhnNotificationOldMessageCount,
       "lhnNotificationOldMessageTable": lhnNotificationOldMessageTable,
       "lhnNotificationOldMessageEntry": lhnNotificationOldMessageEntry,
       "lhnNotificationIndex": lhnNotificationIndex,
       "lhnNotificationMessage": lhnNotificationMessage,
       "lhnNotificationTime": lhnNotificationTime,
       "lhnNotificationMessageCount": lhnNotificationMessageCount,
       "lhnNotificationMessageTable": lhnNotificationMessageTable,
       "lhnNotificationMessageEntry": lhnNotificationMessageEntry,
       "lhnNotificationMessageIndex": lhnNotificationMessageIndex,
       "lhnMessage": lhnMessage,
       "lhnMessageTime": lhnMessageTime,
       "lhnEventID": lhnEventID,
       "lhnSeverity": lhnSeverity,
       "lhnHostname": lhnHostname,
       "lhnPrimaryIP": lhnPrimaryIP,
       "lhnMac": lhnMac,
       "lhnSerialNumber": lhnSerialNumber,
       "lhnModelName": lhnModelName,
       "lhnProductName": lhnProductName,
       "lhnProductID": lhnProductID,
       "lhnHpim": lhnHpim,
       "lhnSoftwareVersion": lhnSoftwareVersion,
       "lhnManagementGroupVersion": lhnManagementGroupVersion,
       "lhnManagementGroupSerialNumber": lhnManagementGroupSerialNumber,
       "lhnManagementGroup": lhnManagementGroup,
       "lhnCluster": lhnCluster,
       "lhnSite": lhnSite,
       "lhnComponentName": lhnComponentName,
       "lhnSystemName": lhnSystemName,
       "lhnLogicalName": lhnLogicalName,
       "lhnComponentState": lhnComponentState,
       "lhnComponentModel": lhnComponentModel,
       "lhnComponentSerialNumber": lhnComponentSerialNumber,
       "lhnComponentFirmwareVersion": lhnComponentFirmwareVersion,
       "lhnComponentHardwareVersion": lhnComponentHardwareVersion,
       "lhnDriverVersion": lhnDriverVersion,
       "lhnBiosVersion": lhnBiosVersion,
       "lhnRaidConfiguration": lhnRaidConfiguration,
       "lhnDiskInterface": lhnDiskInterface,
       "lhnDiskCapacity": lhnDiskCapacity,
       "lhnRaidState": lhnRaidState,
       "lhnParityInitStatus": lhnParityInitStatus,
       "lhnHealthState": lhnHealthState,
       "lhnBpsState": lhnBpsState,
       "lhnCacheState": lhnCacheState,
       "lhnLinkState": lhnLinkState,
       "lhnVipState": lhnVipState,
       "lhnMaintenanceMode": lhnMaintenanceMode,
       "lhnMinFanSpeed": lhnMinFanSpeed,
       "lhnFanSpeed": lhnFanSpeed,
       "lhnHighTemperatureLimit": lhnHighTemperatureLimit,
       "lhnTemperatureState": lhnTemperatureState,
       "lhnTemperature": lhnTemperature,
       "lhnHighVoltageLimit": lhnHighVoltageLimit,
       "lhnLowVoltageLimit": lhnLowVoltageLimit,
       "lhnVoltage": lhnVoltage,
       "lhnUtilization": lhnUtilization,
       "lhnLatency": lhnLatency,
       "lhnMemoryUtilization": lhnMemoryUtilization,
       "lhnMemoryConfig": lhnMemoryConfig,
       "lhnCpuUtilization": lhnCpuUtilization,
       "lhnCpuConfig": lhnCpuConfig,
       "lhnDiskSpeed": lhnDiskSpeed,
       "lhnLicenseState": lhnLicenseState,
       "lhnUtilizationState": lhnUtilizationState,
       "lhnLatencyState": lhnLatencyState,
       "lhnServerVIPAddress": lhnServerVIPAddress,
       "lhnServerVIPState": lhnServerVIPState,
       "lhnReplicationState": lhnReplicationState,
       "lhnSnapshotState": lhnSnapshotState,
       "lhnSnapshotSchedState": lhnSnapshotSchedState,
       "lhnWarrantyPartNumber": lhnWarrantyPartNumber,
       "lhnWarrantySerialNumber": lhnWarrantySerialNumber,
       "lhnWarrantyLicenseNumber": lhnWarrantyLicenseNumber,
       "lhnWearState": lhnWearState,
       "lhnWearDays": lhnWearDays,
       "lhnWearPercent": lhnWearPercent,
       "lhnUserNotification": lhnUserNotification}
)
