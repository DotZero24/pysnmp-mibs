# SNMP MIB module (LEFTHAND-NETWORKS-NSM-NETWORK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/LEFTHAND-NETWORKS-NSM-NETWORK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:41:03 2025
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

(lhnNsmNetwork,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-NSM-MIB",
    "lhnNsmNetwork")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

lhnNsmNetworkModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 3)
)
if mibBuilder.loadTexts:
    lhnNsmNetworkModule.setRevisions(
        ("2013-11-15 00:00",
         "2013-06-25 00:00",
         "2012-09-04 00:00",
         "2011-04-19 00:00",
         "2010-09-07 00:00",
         "2010-07-19 00:00",
         "2009-11-20 00:00",
         "2009-03-10 00:00",
         "2008-01-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LhnNsmNetworkModuleConformance_ObjectIdentity = ObjectIdentity
lhnNsmNetworkModuleConformance = _LhnNsmNetworkModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 3, 1)
)
_LhnNsmNetworkModuleCompliances_ObjectIdentity = ObjectIdentity
lhnNsmNetworkModuleCompliances = _LhnNsmNetworkModuleCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 3, 1, 1)
)
_LhnNsmNetworkModuleGroups_ObjectIdentity = ObjectIdentity
lhnNsmNetworkModuleGroups = _LhnNsmNetworkModuleGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 3, 1, 2)
)
_NetworkDeviceCount_Type = Integer32
_NetworkDeviceCount_Object = MibScalar
networkDeviceCount = _NetworkDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 1),
    _NetworkDeviceCount_Type()
)
networkDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceCount.setStatus("current")
_NetworkDeviceTable_Object = MibTable
networkDeviceTable = _NetworkDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    networkDeviceTable.setStatus("current")
_NetworkDeviceEntry_Object = MibTableRow
networkDeviceEntry = _NetworkDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 2, 1)
)
networkDeviceEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "networkDeviceIndex"),
)
if mibBuilder.loadTexts:
    networkDeviceEntry.setStatus("current")
_NetworkDeviceIndex_Type = Unsigned32
_NetworkDeviceIndex_Object = MibTableColumn
networkDeviceIndex = _NetworkDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 2, 1, 1),
    _NetworkDeviceIndex_Type()
)
networkDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkDeviceIndex.setStatus("current")
_NetworkDeviceName_Type = DisplayString
_NetworkDeviceName_Object = MibTableColumn
networkDeviceName = _NetworkDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 2, 1, 6),
    _NetworkDeviceName_Type()
)
networkDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceName.setStatus("current")
_NetworkDeviceIpAddress_Type = IpAddress
_NetworkDeviceIpAddress_Object = MibTableColumn
networkDeviceIpAddress = _NetworkDeviceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 2, 1, 7),
    _NetworkDeviceIpAddress_Type()
)
networkDeviceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceIpAddress.setStatus("current")
_NetworkDeviceMask_Type = IpAddress
_NetworkDeviceMask_Object = MibTableColumn
networkDeviceMask = _NetworkDeviceMask_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 2, 1, 8),
    _NetworkDeviceMask_Type()
)
networkDeviceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceMask.setStatus("current")
_NetworkDeviceDefaultGateway_Type = IpAddress
_NetworkDeviceDefaultGateway_Object = MibTableColumn
networkDeviceDefaultGateway = _NetworkDeviceDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 2, 1, 9),
    _NetworkDeviceDefaultGateway_Type()
)
networkDeviceDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceDefaultGateway.setStatus("current")


class _NetworkDeviceMode_Type(Integer32):
    """Custom type networkDeviceMode based on Integer32"""
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
        *(("disabled", 1),
          ("auto", 2),
          ("static", 3),
          ("slave", 4))
    )


_NetworkDeviceMode_Type.__name__ = "Integer32"
_NetworkDeviceMode_Object = MibTableColumn
networkDeviceMode = _NetworkDeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 2, 1, 10),
    _NetworkDeviceMode_Type()
)
networkDeviceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceMode.setStatus("current")
_NetworkDeviceStatus_Type = DisplayString
_NetworkDeviceStatus_Object = MibTableColumn
networkDeviceStatus = _NetworkDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 2, 1, 11),
    _NetworkDeviceStatus_Type()
)
networkDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceStatus.setStatus("current")
_NetworkDeviceRowStatus_Type = RowStatus
_NetworkDeviceRowStatus_Object = MibTableColumn
networkDeviceRowStatus = _NetworkDeviceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 2, 1, 99),
    _NetworkDeviceRowStatus_Type()
)
networkDeviceRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkDeviceRowStatus.setStatus("obsolete")
_FibreChannelDeviceCount_Type = Integer32
_FibreChannelDeviceCount_Object = MibScalar
fibreChannelDeviceCount = _FibreChannelDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 3),
    _FibreChannelDeviceCount_Type()
)
fibreChannelDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibreChannelDeviceCount.setStatus("current")
_FibreChannelDeviceTable_Object = MibTable
fibreChannelDeviceTable = _FibreChannelDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    fibreChannelDeviceTable.setStatus("current")
_FibreChannelDeviceEntry_Object = MibTableRow
fibreChannelDeviceEntry = _FibreChannelDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 4, 1)
)
fibreChannelDeviceEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "fibreChannelDeviceIndex"),
)
if mibBuilder.loadTexts:
    fibreChannelDeviceEntry.setStatus("current")
_FibreChannelDeviceIndex_Type = Unsigned32
_FibreChannelDeviceIndex_Object = MibTableColumn
fibreChannelDeviceIndex = _FibreChannelDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 4, 1, 1),
    _FibreChannelDeviceIndex_Type()
)
fibreChannelDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fibreChannelDeviceIndex.setStatus("current")
_FibreChannelDeviceName_Type = DisplayString
_FibreChannelDeviceName_Object = MibTableColumn
fibreChannelDeviceName = _FibreChannelDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 4, 1, 2),
    _FibreChannelDeviceName_Type()
)
fibreChannelDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibreChannelDeviceName.setStatus("current")
_FibreChannelDeviceDriverVersion_Type = DisplayString
_FibreChannelDeviceDriverVersion_Object = MibTableColumn
fibreChannelDeviceDriverVersion = _FibreChannelDeviceDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 4, 1, 3),
    _FibreChannelDeviceDriverVersion_Type()
)
fibreChannelDeviceDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibreChannelDeviceDriverVersion.setStatus("current")
_FibreChannelDeviceFirmwareVersion_Type = DisplayString
_FibreChannelDeviceFirmwareVersion_Object = MibTableColumn
fibreChannelDeviceFirmwareVersion = _FibreChannelDeviceFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 4, 1, 4),
    _FibreChannelDeviceFirmwareVersion_Type()
)
fibreChannelDeviceFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibreChannelDeviceFirmwareVersion.setStatus("current")
_FibreChannelDeviceNodeName_Type = DisplayString
_FibreChannelDeviceNodeName_Object = MibTableColumn
fibreChannelDeviceNodeName = _FibreChannelDeviceNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 4, 1, 5),
    _FibreChannelDeviceNodeName_Type()
)
fibreChannelDeviceNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibreChannelDeviceNodeName.setStatus("current")
_FibreChannelDevicePortName_Type = DisplayString
_FibreChannelDevicePortName_Object = MibTableColumn
fibreChannelDevicePortName = _FibreChannelDevicePortName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 4, 1, 6),
    _FibreChannelDevicePortName_Type()
)
fibreChannelDevicePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibreChannelDevicePortName.setStatus("current")
_FibreChannelDevicePortId_Type = DisplayString
_FibreChannelDevicePortId_Object = MibTableColumn
fibreChannelDevicePortId = _FibreChannelDevicePortId_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 4, 1, 7),
    _FibreChannelDevicePortId_Type()
)
fibreChannelDevicePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibreChannelDevicePortId.setStatus("current")
_FibreChannelDevicePortType_Type = DisplayString
_FibreChannelDevicePortType_Object = MibTableColumn
fibreChannelDevicePortType = _FibreChannelDevicePortType_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 4, 1, 8),
    _FibreChannelDevicePortType_Type()
)
fibreChannelDevicePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibreChannelDevicePortType.setStatus("current")
_FibreChannelDeviceCurrentSpeed_Type = DisplayString
_FibreChannelDeviceCurrentSpeed_Object = MibTableColumn
fibreChannelDeviceCurrentSpeed = _FibreChannelDeviceCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 4, 1, 9),
    _FibreChannelDeviceCurrentSpeed_Type()
)
fibreChannelDeviceCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibreChannelDeviceCurrentSpeed.setStatus("current")
_FibreChannelDeviceLinkStatus_Type = DisplayString
_FibreChannelDeviceLinkStatus_Object = MibTableColumn
fibreChannelDeviceLinkStatus = _FibreChannelDeviceLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 4, 1, 10),
    _FibreChannelDeviceLinkStatus_Type()
)
fibreChannelDeviceLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibreChannelDeviceLinkStatus.setStatus("current")
_FibreChannelDeviceRxFrames_Type = Counter64
_FibreChannelDeviceRxFrames_Object = MibTableColumn
fibreChannelDeviceRxFrames = _FibreChannelDeviceRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 4, 1, 11),
    _FibreChannelDeviceRxFrames_Type()
)
fibreChannelDeviceRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibreChannelDeviceRxFrames.setStatus("current")
_FibreChannelDeviceTxFrames_Type = Counter64
_FibreChannelDeviceTxFrames_Object = MibTableColumn
fibreChannelDeviceTxFrames = _FibreChannelDeviceTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 4, 1, 12),
    _FibreChannelDeviceTxFrames_Type()
)
fibreChannelDeviceTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibreChannelDeviceTxFrames.setStatus("current")
_FibreChannelDeviceRxWords_Type = Counter64
_FibreChannelDeviceRxWords_Object = MibTableColumn
fibreChannelDeviceRxWords = _FibreChannelDeviceRxWords_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 4, 1, 13),
    _FibreChannelDeviceRxWords_Type()
)
fibreChannelDeviceRxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibreChannelDeviceRxWords.setStatus("current")
_FibreChannelDeviceTxWords_Type = Counter64
_FibreChannelDeviceTxWords_Object = MibTableColumn
fibreChannelDeviceTxWords = _FibreChannelDeviceTxWords_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 4, 1, 14),
    _FibreChannelDeviceTxWords_Type()
)
fibreChannelDeviceTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibreChannelDeviceTxWords.setStatus("current")
_FibreChannelDeviceBiosVersion_Type = DisplayString
_FibreChannelDeviceBiosVersion_Object = MibTableColumn
fibreChannelDeviceBiosVersion = _FibreChannelDeviceBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 4, 1, 15),
    _FibreChannelDeviceBiosVersion_Type()
)
fibreChannelDeviceBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibreChannelDeviceBiosVersion.setStatus("current")
_FibreChannelDeviceSerialNumber_Type = DisplayString
_FibreChannelDeviceSerialNumber_Object = MibTableColumn
fibreChannelDeviceSerialNumber = _FibreChannelDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 2, 4, 1, 16),
    _FibreChannelDeviceSerialNumber_Type()
)
fibreChannelDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fibreChannelDeviceSerialNumber.setStatus("current")

# Managed Objects groups

lefthandNetworksNsmNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 3, 1, 2, 1)
)
lefthandNetworksNsmNetworkGroup.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "networkDeviceCount"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "networkDeviceName"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "networkDeviceIpAddress"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "networkDeviceMask"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "networkDeviceDefaultGateway"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "networkDeviceMode"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "networkDeviceStatus"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "fibreChannelDeviceCount"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "fibreChannelDeviceName"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "fibreChannelDeviceDriverVersion"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "fibreChannelDeviceFirmwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "fibreChannelDeviceNodeName"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "fibreChannelDevicePortName"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "fibreChannelDevicePortId"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "fibreChannelDevicePortType"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "fibreChannelDeviceCurrentSpeed"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "fibreChannelDeviceLinkStatus"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "fibreChannelDeviceRxFrames"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "fibreChannelDeviceTxFrames"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "fibreChannelDeviceRxWords"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "fibreChannelDeviceTxWords"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "fibreChannelDeviceBiosVersion"),
        ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "fibreChannelDeviceSerialNumber"))
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmNetworkGroup.setStatus("current")

lefthandNetworksNsmNetworkGroupObsolete = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 3, 1, 2, 2)
)
lefthandNetworksNsmNetworkGroupObsolete.setObjects(
    ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "networkDeviceRowStatus")
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmNetworkGroupObsolete.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lefthandNetworksNsmNetworkMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 3, 1, 1, 1)
)
lefthandNetworksNsmNetworkMibCompliance.setObjects(
    ("LEFTHAND-NETWORKS-NSM-NETWORK-MIB", "lefthandNetworksNsmNetworkGroup")
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmNetworkMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-NSM-NETWORK-MIB",
    **{"lhnNsmNetworkModule": lhnNsmNetworkModule,
       "lhnNsmNetworkModuleConformance": lhnNsmNetworkModuleConformance,
       "lhnNsmNetworkModuleCompliances": lhnNsmNetworkModuleCompliances,
       "lefthandNetworksNsmNetworkMibCompliance": lefthandNetworksNsmNetworkMibCompliance,
       "lhnNsmNetworkModuleGroups": lhnNsmNetworkModuleGroups,
       "lefthandNetworksNsmNetworkGroup": lefthandNetworksNsmNetworkGroup,
       "lefthandNetworksNsmNetworkGroupObsolete": lefthandNetworksNsmNetworkGroupObsolete,
       "networkDeviceCount": networkDeviceCount,
       "networkDeviceTable": networkDeviceTable,
       "networkDeviceEntry": networkDeviceEntry,
       "networkDeviceIndex": networkDeviceIndex,
       "networkDeviceName": networkDeviceName,
       "networkDeviceIpAddress": networkDeviceIpAddress,
       "networkDeviceMask": networkDeviceMask,
       "networkDeviceDefaultGateway": networkDeviceDefaultGateway,
       "networkDeviceMode": networkDeviceMode,
       "networkDeviceStatus": networkDeviceStatus,
       "networkDeviceRowStatus": networkDeviceRowStatus,
       "fibreChannelDeviceCount": fibreChannelDeviceCount,
       "fibreChannelDeviceTable": fibreChannelDeviceTable,
       "fibreChannelDeviceEntry": fibreChannelDeviceEntry,
       "fibreChannelDeviceIndex": fibreChannelDeviceIndex,
       "fibreChannelDeviceName": fibreChannelDeviceName,
       "fibreChannelDeviceDriverVersion": fibreChannelDeviceDriverVersion,
       "fibreChannelDeviceFirmwareVersion": fibreChannelDeviceFirmwareVersion,
       "fibreChannelDeviceNodeName": fibreChannelDeviceNodeName,
       "fibreChannelDevicePortName": fibreChannelDevicePortName,
       "fibreChannelDevicePortId": fibreChannelDevicePortId,
       "fibreChannelDevicePortType": fibreChannelDevicePortType,
       "fibreChannelDeviceCurrentSpeed": fibreChannelDeviceCurrentSpeed,
       "fibreChannelDeviceLinkStatus": fibreChannelDeviceLinkStatus,
       "fibreChannelDeviceRxFrames": fibreChannelDeviceRxFrames,
       "fibreChannelDeviceTxFrames": fibreChannelDeviceTxFrames,
       "fibreChannelDeviceRxWords": fibreChannelDeviceRxWords,
       "fibreChannelDeviceTxWords": fibreChannelDeviceTxWords,
       "fibreChannelDeviceBiosVersion": fibreChannelDeviceBiosVersion,
       "fibreChannelDeviceSerialNumber": fibreChannelDeviceSerialNumber}
)
