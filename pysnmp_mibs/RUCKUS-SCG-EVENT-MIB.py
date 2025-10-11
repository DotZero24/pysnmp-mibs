# SNMP MIB module (RUCKUS-SCG-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruckus/RUCKUS-SCG-EVENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:13:55 2025
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

(ruckusEvents,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusEvents")

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

ruckusSCGEventMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusSCGEventTraps_ObjectIdentity = ObjectIdentity
ruckusSCGEventTraps = _RuckusSCGEventTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1)
)
_RuckusSCGEventObjects_ObjectIdentity = ObjectIdentity
ruckusSCGEventObjects = _RuckusSCGEventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2)
)
_RuckusSCGEventDescription_Type = OctetString
_RuckusSCGEventDescription_Object = MibScalar
ruckusSCGEventDescription = _RuckusSCGEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 1),
    _RuckusSCGEventDescription_Type()
)
ruckusSCGEventDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventDescription.setStatus("current")
_RuckusSCGClusterName_Type = OctetString
_RuckusSCGClusterName_Object = MibScalar
ruckusSCGClusterName = _RuckusSCGClusterName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 2),
    _RuckusSCGClusterName_Type()
)
ruckusSCGClusterName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGClusterName.setStatus("current")
_RuckusSCGEventCode_Type = OctetString
_RuckusSCGEventCode_Object = MibScalar
ruckusSCGEventCode = _RuckusSCGEventCode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 10),
    _RuckusSCGEventCode_Type()
)
ruckusSCGEventCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventCode.setStatus("current")
_RuckusSCGProcessName_Type = OctetString
_RuckusSCGProcessName_Object = MibScalar
ruckusSCGProcessName = _RuckusSCGProcessName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 11),
    _RuckusSCGProcessName_Type()
)
ruckusSCGProcessName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGProcessName.setStatus("current")
_RuckusSCGEventCtrlIP_Type = OctetString
_RuckusSCGEventCtrlIP_Object = MibScalar
ruckusSCGEventCtrlIP = _RuckusSCGEventCtrlIP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 12),
    _RuckusSCGEventCtrlIP_Type()
)
ruckusSCGEventCtrlIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventCtrlIP.setStatus("current")
_RuckusSCGEventSeverity_Type = OctetString
_RuckusSCGEventSeverity_Object = MibScalar
ruckusSCGEventSeverity = _RuckusSCGEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 13),
    _RuckusSCGEventSeverity_Type()
)
ruckusSCGEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventSeverity.setStatus("current")
_RuckusSCGEventType_Type = OctetString
_RuckusSCGEventType_Object = MibScalar
ruckusSCGEventType = _RuckusSCGEventType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 14),
    _RuckusSCGEventType_Type()
)
ruckusSCGEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventType.setStatus("current")
_RuckusSCGEventNodeMgmtIp_Type = OctetString
_RuckusSCGEventNodeMgmtIp_Object = MibScalar
ruckusSCGEventNodeMgmtIp = _RuckusSCGEventNodeMgmtIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 15),
    _RuckusSCGEventNodeMgmtIp_Type()
)
ruckusSCGEventNodeMgmtIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventNodeMgmtIp.setStatus("current")
_RuckusSCGEventNodeName_Type = OctetString
_RuckusSCGEventNodeName_Object = MibScalar
ruckusSCGEventNodeName = _RuckusSCGEventNodeName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 16),
    _RuckusSCGEventNodeName_Type()
)
ruckusSCGEventNodeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventNodeName.setStatus("current")
_RuckusSCGCPUPerc_Type = OctetString
_RuckusSCGCPUPerc_Object = MibScalar
ruckusSCGCPUPerc = _RuckusSCGCPUPerc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 17),
    _RuckusSCGCPUPerc_Type()
)
ruckusSCGCPUPerc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGCPUPerc.setStatus("current")
_RuckusSCGMemoryPerc_Type = OctetString
_RuckusSCGMemoryPerc_Object = MibScalar
ruckusSCGMemoryPerc = _RuckusSCGMemoryPerc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 18),
    _RuckusSCGMemoryPerc_Type()
)
ruckusSCGMemoryPerc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGMemoryPerc.setStatus("current")
_RuckusSCGDiskPerc_Type = OctetString
_RuckusSCGDiskPerc_Object = MibScalar
ruckusSCGDiskPerc = _RuckusSCGDiskPerc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 19),
    _RuckusSCGDiskPerc_Type()
)
ruckusSCGDiskPerc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGDiskPerc.setStatus("current")
_RuckusSCGEventMacAddr_Type = OctetString
_RuckusSCGEventMacAddr_Object = MibScalar
ruckusSCGEventMacAddr = _RuckusSCGEventMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 20),
    _RuckusSCGEventMacAddr_Type()
)
ruckusSCGEventMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventMacAddr.setStatus("current")
_RuckusSCGEventFirmwareVersion_Type = OctetString
_RuckusSCGEventFirmwareVersion_Object = MibScalar
ruckusSCGEventFirmwareVersion = _RuckusSCGEventFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 21),
    _RuckusSCGEventFirmwareVersion_Type()
)
ruckusSCGEventFirmwareVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventFirmwareVersion.setStatus("current")
_RuckusSCGEventUpgradedFirmwareVersion_Type = OctetString
_RuckusSCGEventUpgradedFirmwareVersion_Object = MibScalar
ruckusSCGEventUpgradedFirmwareVersion = _RuckusSCGEventUpgradedFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 22),
    _RuckusSCGEventUpgradedFirmwareVersion_Type()
)
ruckusSCGEventUpgradedFirmwareVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventUpgradedFirmwareVersion.setStatus("current")
_RuckusSCGEventAPMacAddr_Type = OctetString
_RuckusSCGEventAPMacAddr_Object = MibScalar
ruckusSCGEventAPMacAddr = _RuckusSCGEventAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 23),
    _RuckusSCGEventAPMacAddr_Type()
)
ruckusSCGEventAPMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventAPMacAddr.setStatus("current")
_RuckusSCGEventReason_Type = OctetString
_RuckusSCGEventReason_Object = MibScalar
ruckusSCGEventReason = _RuckusSCGEventReason_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 24),
    _RuckusSCGEventReason_Type()
)
ruckusSCGEventReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventReason.setStatus("current")
_RuckusSCGEventAPName_Type = OctetString
_RuckusSCGEventAPName_Object = MibScalar
ruckusSCGEventAPName = _RuckusSCGEventAPName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 25),
    _RuckusSCGEventAPName_Type()
)
ruckusSCGEventAPName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventAPName.setStatus("current")
_RuckusSCGEventAPIP_Type = OctetString
_RuckusSCGEventAPIP_Object = MibScalar
ruckusSCGEventAPIP = _RuckusSCGEventAPIP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 26),
    _RuckusSCGEventAPIP_Type()
)
ruckusSCGEventAPIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventAPIP.setStatus("current")
_RuckusSCGEventAPLocation_Type = OctetString
_RuckusSCGEventAPLocation_Object = MibScalar
ruckusSCGEventAPLocation = _RuckusSCGEventAPLocation_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 27),
    _RuckusSCGEventAPLocation_Type()
)
ruckusSCGEventAPLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventAPLocation.setStatus("current")
_RuckusSCGEventAPGPSCoordinates_Type = OctetString
_RuckusSCGEventAPGPSCoordinates_Object = MibScalar
ruckusSCGEventAPGPSCoordinates = _RuckusSCGEventAPGPSCoordinates_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 28),
    _RuckusSCGEventAPGPSCoordinates_Type()
)
ruckusSCGEventAPGPSCoordinates.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventAPGPSCoordinates.setStatus("current")
_RuckusSCGEventAPDescription_Type = OctetString
_RuckusSCGEventAPDescription_Object = MibScalar
ruckusSCGEventAPDescription = _RuckusSCGEventAPDescription_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 29),
    _RuckusSCGEventAPDescription_Type()
)
ruckusSCGEventAPDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventAPDescription.setStatus("current")
_RuckusSCGEventZoneName_Type = OctetString
_RuckusSCGEventZoneName_Object = MibScalar
ruckusSCGEventZoneName = _RuckusSCGEventZoneName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 30),
    _RuckusSCGEventZoneName_Type()
)
ruckusSCGEventZoneName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventZoneName.setStatus("current")
_RuckusSCGAPModel_Type = OctetString
_RuckusSCGAPModel_Object = MibScalar
ruckusSCGAPModel = _RuckusSCGAPModel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 31),
    _RuckusSCGAPModel_Type()
)
ruckusSCGAPModel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGAPModel.setStatus("current")
_RuckusSCGConfigAPModel_Type = OctetString
_RuckusSCGConfigAPModel_Object = MibScalar
ruckusSCGConfigAPModel = _RuckusSCGConfigAPModel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 32),
    _RuckusSCGConfigAPModel_Type()
)
ruckusSCGConfigAPModel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGConfigAPModel.setStatus("current")
_RuckusSCGAPConfigID_Type = OctetString
_RuckusSCGAPConfigID_Object = MibScalar
ruckusSCGAPConfigID = _RuckusSCGAPConfigID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 33),
    _RuckusSCGAPConfigID_Type()
)
ruckusSCGAPConfigID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGAPConfigID.setStatus("current")
_RuckusSCGEventTargetZoneName_Type = OctetString
_RuckusSCGEventTargetZoneName_Object = MibScalar
ruckusSCGEventTargetZoneName = _RuckusSCGEventTargetZoneName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 34),
    _RuckusSCGEventTargetZoneName_Type()
)
ruckusSCGEventTargetZoneName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventTargetZoneName.setStatus("current")
_RuckusSCGEventAPIPv6_Type = OctetString
_RuckusSCGEventAPIPv6_Object = MibScalar
ruckusSCGEventAPIPv6 = _RuckusSCGEventAPIPv6_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 35),
    _RuckusSCGEventAPIPv6_Type()
)
ruckusSCGEventAPIPv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventAPIPv6.setStatus("current")
_RuckusSCGLBSURL_Type = OctetString
_RuckusSCGLBSURL_Object = MibScalar
ruckusSCGLBSURL = _RuckusSCGLBSURL_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 38),
    _RuckusSCGLBSURL_Type()
)
ruckusSCGLBSURL.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGLBSURL.setStatus("current")
_RuckusSCGLBSPort_Type = OctetString
_RuckusSCGLBSPort_Object = MibScalar
ruckusSCGLBSPort = _RuckusSCGLBSPort_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 39),
    _RuckusSCGLBSPort_Type()
)
ruckusSCGLBSPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGLBSPort.setStatus("current")
_RuckusSCGEventSSID_Type = OctetString
_RuckusSCGEventSSID_Object = MibScalar
ruckusSCGEventSSID = _RuckusSCGEventSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 40),
    _RuckusSCGEventSSID_Type()
)
ruckusSCGEventSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventSSID.setStatus("current")
_RuckusSCGEventRogueMac_Type = OctetString
_RuckusSCGEventRogueMac_Object = MibScalar
ruckusSCGEventRogueMac = _RuckusSCGEventRogueMac_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 45),
    _RuckusSCGEventRogueMac_Type()
)
ruckusSCGEventRogueMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventRogueMac.setStatus("current")
_RuckusPrimaryGRE_Type = OctetString
_RuckusPrimaryGRE_Object = MibScalar
ruckusPrimaryGRE = _RuckusPrimaryGRE_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 46),
    _RuckusPrimaryGRE_Type()
)
ruckusPrimaryGRE.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusPrimaryGRE.setStatus("current")
_RuckusSecondaryGRE_Type = OctetString
_RuckusSecondaryGRE_Object = MibScalar
ruckusSecondaryGRE = _RuckusSecondaryGRE_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 47),
    _RuckusSecondaryGRE_Type()
)
ruckusSecondaryGRE.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSecondaryGRE.setStatus("current")
_RuckusSoftGREGatewayList_Type = OctetString
_RuckusSoftGREGatewayList_Object = MibScalar
ruckusSoftGREGatewayList = _RuckusSoftGREGatewayList_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 48),
    _RuckusSoftGREGatewayList_Type()
)
ruckusSoftGREGatewayList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSoftGREGatewayList.setStatus("current")
_RuckusSCGSoftGREGWAddress_Type = OctetString
_RuckusSCGSoftGREGWAddress_Object = MibScalar
ruckusSCGSoftGREGWAddress = _RuckusSCGSoftGREGWAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 49),
    _RuckusSCGSoftGREGWAddress_Type()
)
ruckusSCGSoftGREGWAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGSoftGREGWAddress.setStatus("current")
_RuckusSCGEventClientMacAddr_Type = OctetString
_RuckusSCGEventClientMacAddr_Object = MibScalar
ruckusSCGEventClientMacAddr = _RuckusSCGEventClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 50),
    _RuckusSCGEventClientMacAddr_Type()
)
ruckusSCGEventClientMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventClientMacAddr.setStatus("current")
_RuckusSCGDPKey_Type = OctetString
_RuckusSCGDPKey_Object = MibScalar
ruckusSCGDPKey = _RuckusSCGDPKey_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 80),
    _RuckusSCGDPKey_Type()
)
ruckusSCGDPKey.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGDPKey.setStatus("current")
_RuckusSCGDPConfigID_Type = OctetString
_RuckusSCGDPConfigID_Object = MibScalar
ruckusSCGDPConfigID = _RuckusSCGDPConfigID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 81),
    _RuckusSCGDPConfigID_Type()
)
ruckusSCGDPConfigID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGDPConfigID.setStatus("current")
_RuckusSCGDPIP_Type = OctetString
_RuckusSCGDPIP_Object = MibScalar
ruckusSCGDPIP = _RuckusSCGDPIP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 82),
    _RuckusSCGDPIP_Type()
)
ruckusSCGDPIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGDPIP.setStatus("current")
_RuckusSCGDPPacketPoolID_Type = OctetString
_RuckusSCGDPPacketPoolID_Object = MibScalar
ruckusSCGDPPacketPoolID = _RuckusSCGDPPacketPoolID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 83),
    _RuckusSCGDPPacketPoolID_Type()
)
ruckusSCGDPPacketPoolID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGDPPacketPoolID.setStatus("current")
_RuckusSCGNetworkPortID_Type = OctetString
_RuckusSCGNetworkPortID_Object = MibScalar
ruckusSCGNetworkPortID = _RuckusSCGNetworkPortID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 100),
    _RuckusSCGNetworkPortID_Type()
)
ruckusSCGNetworkPortID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGNetworkPortID.setStatus("current")
_RuckusSCGNetworkInterface_Type = OctetString
_RuckusSCGNetworkInterface_Object = MibScalar
ruckusSCGNetworkInterface = _RuckusSCGNetworkInterface_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 101),
    _RuckusSCGNetworkInterface_Type()
)
ruckusSCGNetworkInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGNetworkInterface.setStatus("current")
_RuckusSCGSwitchStatus_Type = OctetString
_RuckusSCGSwitchStatus_Object = MibScalar
ruckusSCGSwitchStatus = _RuckusSCGSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 102),
    _RuckusSCGSwitchStatus_Type()
)
ruckusSCGSwitchStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGSwitchStatus.setStatus("current")
_RuckusSCGTemperatureStatus_Type = OctetString
_RuckusSCGTemperatureStatus_Object = MibScalar
ruckusSCGTemperatureStatus = _RuckusSCGTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 120),
    _RuckusSCGTemperatureStatus_Type()
)
ruckusSCGTemperatureStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGTemperatureStatus.setStatus("current")
_RuckusSCGProcessorId_Type = OctetString
_RuckusSCGProcessorId_Object = MibScalar
ruckusSCGProcessorId = _RuckusSCGProcessorId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 121),
    _RuckusSCGProcessorId_Type()
)
ruckusSCGProcessorId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGProcessorId.setStatus("current")
_RuckusSCGFanId_Type = OctetString
_RuckusSCGFanId_Object = MibScalar
ruckusSCGFanId = _RuckusSCGFanId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 122),
    _RuckusSCGFanId_Type()
)
ruckusSCGFanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGFanId.setStatus("current")
_RuckusSCGFanStatus_Type = OctetString
_RuckusSCGFanStatus_Object = MibScalar
ruckusSCGFanStatus = _RuckusSCGFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 123),
    _RuckusSCGFanStatus_Type()
)
ruckusSCGFanStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGFanStatus.setStatus("current")
_RuckusSCGPsId_Type = OctetString
_RuckusSCGPsId_Object = MibScalar
ruckusSCGPsId = _RuckusSCGPsId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 124),
    _RuckusSCGPsId_Type()
)
ruckusSCGPsId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGPsId.setStatus("current")
_RuckusSCGPsStatus_Type = OctetString
_RuckusSCGPsStatus_Object = MibScalar
ruckusSCGPsStatus = _RuckusSCGPsStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 125),
    _RuckusSCGPsStatus_Type()
)
ruckusSCGPsStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGPsStatus.setStatus("current")
_RuckusSCGDrvId_Type = OctetString
_RuckusSCGDrvId_Object = MibScalar
ruckusSCGDrvId = _RuckusSCGDrvId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 126),
    _RuckusSCGDrvId_Type()
)
ruckusSCGDrvId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGDrvId.setStatus("current")
_RuckusSCGDrvStatus_Type = OctetString
_RuckusSCGDrvStatus_Object = MibScalar
ruckusSCGDrvStatus = _RuckusSCGDrvStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 127),
    _RuckusSCGDrvStatus_Type()
)
ruckusSCGDrvStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGDrvStatus.setStatus("current")
_RuckusSCGLicenseType_Type = OctetString
_RuckusSCGLicenseType_Object = MibScalar
ruckusSCGLicenseType = _RuckusSCGLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 150),
    _RuckusSCGLicenseType_Type()
)
ruckusSCGLicenseType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGLicenseType.setStatus("current")
_RuckusSCGLicenseUsagePerc_Type = OctetString
_RuckusSCGLicenseUsagePerc_Object = MibScalar
ruckusSCGLicenseUsagePerc = _RuckusSCGLicenseUsagePerc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 151),
    _RuckusSCGLicenseUsagePerc_Type()
)
ruckusSCGLicenseUsagePerc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGLicenseUsagePerc.setStatus("current")
_RuckusSCGLicenseServerName_Type = OctetString
_RuckusSCGLicenseServerName_Object = MibScalar
ruckusSCGLicenseServerName = _RuckusSCGLicenseServerName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 152),
    _RuckusSCGLicenseServerName_Type()
)
ruckusSCGLicenseServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGLicenseServerName.setStatus("current")
_RuckusSCGIPSecGWAddress_Type = OctetString
_RuckusSCGIPSecGWAddress_Object = MibScalar
ruckusSCGIPSecGWAddress = _RuckusSCGIPSecGWAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 153),
    _RuckusSCGIPSecGWAddress_Type()
)
ruckusSCGIPSecGWAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGIPSecGWAddress.setStatus("current")
_RuckusSCGSyslogServerAddress_Type = OctetString
_RuckusSCGSyslogServerAddress_Object = MibScalar
ruckusSCGSyslogServerAddress = _RuckusSCGSyslogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 154),
    _RuckusSCGSyslogServerAddress_Type()
)
ruckusSCGSyslogServerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGSyslogServerAddress.setStatus("current")
_RuckusSCGSrcSyslogServerAddress_Type = OctetString
_RuckusSCGSrcSyslogServerAddress_Object = MibScalar
ruckusSCGSrcSyslogServerAddress = _RuckusSCGSrcSyslogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 155),
    _RuckusSCGSrcSyslogServerAddress_Type()
)
ruckusSCGSrcSyslogServerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGSrcSyslogServerAddress.setStatus("current")
_RuckusSCGDestSyslogServerAddress_Type = OctetString
_RuckusSCGDestSyslogServerAddress_Object = MibScalar
ruckusSCGDestSyslogServerAddress = _RuckusSCGDestSyslogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 156),
    _RuckusSCGDestSyslogServerAddress_Type()
)
ruckusSCGDestSyslogServerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGDestSyslogServerAddress.setStatus("current")
_RuckusSCGFtpIp_Type = OctetString
_RuckusSCGFtpIp_Object = MibScalar
ruckusSCGFtpIp = _RuckusSCGFtpIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 200),
    _RuckusSCGFtpIp_Type()
)
ruckusSCGFtpIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGFtpIp.setStatus("current")
_RuckusSCGFtpPort_Type = OctetString
_RuckusSCGFtpPort_Object = MibScalar
ruckusSCGFtpPort = _RuckusSCGFtpPort_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 201),
    _RuckusSCGFtpPort_Type()
)
ruckusSCGFtpPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGFtpPort.setStatus("current")
_RuckusSCGSrcProcess_Type = OctetString
_RuckusSCGSrcProcess_Object = MibScalar
ruckusSCGSrcProcess = _RuckusSCGSrcProcess_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 301),
    _RuckusSCGSrcProcess_Type()
)
ruckusSCGSrcProcess.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGSrcProcess.setStatus("current")
_RuckusSCGGgsnIp_Type = OctetString
_RuckusSCGGgsnIp_Object = MibScalar
ruckusSCGGgsnIp = _RuckusSCGGgsnIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 302),
    _RuckusSCGGgsnIp_Type()
)
ruckusSCGGgsnIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGGgsnIp.setStatus("current")
_RuckusSCGGtpcIp_Type = OctetString
_RuckusSCGGtpcIp_Object = MibScalar
ruckusSCGGtpcIp = _RuckusSCGGtpcIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 303),
    _RuckusSCGGtpcIp_Type()
)
ruckusSCGGtpcIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGGtpcIp.setStatus("current")
_RuckusSCGApn_Type = OctetString
_RuckusSCGApn_Object = MibScalar
ruckusSCGApn = _RuckusSCGApn_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 304),
    _RuckusSCGApn_Type()
)
ruckusSCGApn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGApn.setStatus("current")
_RuckusSCGUEImsi_Type = OctetString
_RuckusSCGUEImsi_Object = MibScalar
ruckusSCGUEImsi = _RuckusSCGUEImsi_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 305),
    _RuckusSCGUEImsi_Type()
)
ruckusSCGUEImsi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGUEImsi.setStatus("current")
_RuckusSCGUEMsisdn_Type = OctetString
_RuckusSCGUEMsisdn_Object = MibScalar
ruckusSCGUEMsisdn = _RuckusSCGUEMsisdn_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 306),
    _RuckusSCGUEMsisdn_Type()
)
ruckusSCGUEMsisdn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGUEMsisdn.setStatus("current")
_RuckusSCGAuthSrvrIp_Type = OctetString
_RuckusSCGAuthSrvrIp_Object = MibScalar
ruckusSCGAuthSrvrIp = _RuckusSCGAuthSrvrIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 307),
    _RuckusSCGAuthSrvrIp_Type()
)
ruckusSCGAuthSrvrIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGAuthSrvrIp.setStatus("current")
_RuckusSCGRadProxyIp_Type = OctetString
_RuckusSCGRadProxyIp_Object = MibScalar
ruckusSCGRadProxyIp = _RuckusSCGRadProxyIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 308),
    _RuckusSCGRadProxyIp_Type()
)
ruckusSCGRadProxyIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGRadProxyIp.setStatus("current")
_RuckusSCGAccSrvrIp_Type = OctetString
_RuckusSCGAccSrvrIp_Object = MibScalar
ruckusSCGAccSrvrIp = _RuckusSCGAccSrvrIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 309),
    _RuckusSCGAccSrvrIp_Type()
)
ruckusSCGAccSrvrIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGAccSrvrIp.setStatus("current")
_RuckusSCGRealm_Type = OctetString
_RuckusSCGRealm_Object = MibScalar
ruckusSCGRealm = _RuckusSCGRealm_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 310),
    _RuckusSCGRealm_Type()
)
ruckusSCGRealm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGRealm.setStatus("current")
_RuckusSCGCgfSrvrIp_Type = OctetString
_RuckusSCGCgfSrvrIp_Object = MibScalar
ruckusSCGCgfSrvrIp = _RuckusSCGCgfSrvrIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 311),
    _RuckusSCGCgfSrvrIp_Type()
)
ruckusSCGCgfSrvrIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGCgfSrvrIp.setStatus("current")
_RuckusSCGRadSrvrIp_Type = OctetString
_RuckusSCGRadSrvrIp_Object = MibScalar
ruckusSCGRadSrvrIp = _RuckusSCGRadSrvrIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 312),
    _RuckusSCGRadSrvrIp_Type()
)
ruckusSCGRadSrvrIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGRadSrvrIp.setStatus("current")
_RuckusSCGCipIp_Type = OctetString
_RuckusSCGCipIp_Object = MibScalar
ruckusSCGCipIp = _RuckusSCGCipIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 313),
    _RuckusSCGCipIp_Type()
)
ruckusSCGCipIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGCipIp.setStatus("current")
_RuckusSCGPointCode_Type = OctetString
_RuckusSCGPointCode_Object = MibScalar
ruckusSCGPointCode = _RuckusSCGPointCode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 314),
    _RuckusSCGPointCode_Type()
)
ruckusSCGPointCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGPointCode.setStatus("current")
_RuckusSCGCongLevel_Type = OctetString
_RuckusSCGCongLevel_Object = MibScalar
ruckusSCGCongLevel = _RuckusSCGCongLevel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 315),
    _RuckusSCGCongLevel_Type()
)
ruckusSCGCongLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGCongLevel.setStatus("current")
_RuckusSCGSSN_Type = OctetString
_RuckusSCGSSN_Object = MibScalar
ruckusSCGSSN = _RuckusSCGSSN_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 316),
    _RuckusSCGSSN_Type()
)
ruckusSCGSSN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGSSN.setStatus("current")
_RuckusSCGRoutingContext_Type = OctetString
_RuckusSCGRoutingContext_Object = MibScalar
ruckusSCGRoutingContext = _RuckusSCGRoutingContext_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 317),
    _RuckusSCGRoutingContext_Type()
)
ruckusSCGRoutingContext.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGRoutingContext.setStatus("current")
_RuckusSCGSrcIP_Type = OctetString
_RuckusSCGSrcIP_Object = MibScalar
ruckusSCGSrcIP = _RuckusSCGSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 318),
    _RuckusSCGSrcIP_Type()
)
ruckusSCGSrcIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGSrcIP.setStatus("current")
_RuckusSCGSrcPort_Type = OctetString
_RuckusSCGSrcPort_Object = MibScalar
ruckusSCGSrcPort = _RuckusSCGSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 319),
    _RuckusSCGSrcPort_Type()
)
ruckusSCGSrcPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGSrcPort.setStatus("current")
_RuckusSCGDestIP_Type = OctetString
_RuckusSCGDestIP_Object = MibScalar
ruckusSCGDestIP = _RuckusSCGDestIP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 320),
    _RuckusSCGDestIP_Type()
)
ruckusSCGDestIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGDestIP.setStatus("current")
_RuckusSCGDestPort_Type = OctetString
_RuckusSCGDestPort_Object = MibScalar
ruckusSCGDestPort = _RuckusSCGDestPort_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 321),
    _RuckusSCGDestPort_Type()
)
ruckusSCGDestPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGDestPort.setStatus("current")
_RuckusSCGOperation_Type = OctetString
_RuckusSCGOperation_Object = MibScalar
ruckusSCGOperation = _RuckusSCGOperation_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 322),
    _RuckusSCGOperation_Type()
)
ruckusSCGOperation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGOperation.setStatus("current")
_RuckusSCGHlrInstance_Type = OctetString
_RuckusSCGHlrInstance_Object = MibScalar
ruckusSCGHlrInstance = _RuckusSCGHlrInstance_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 323),
    _RuckusSCGHlrInstance_Type()
)
ruckusSCGHlrInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGHlrInstance.setStatus("current")
_RuckusSCGUserName_Type = OctetString
_RuckusSCGUserName_Object = MibScalar
ruckusSCGUserName = _RuckusSCGUserName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 324),
    _RuckusSCGUserName_Type()
)
ruckusSCGUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGUserName.setStatus("current")
_RuckusSCGPgwIp_Type = OctetString
_RuckusSCGPgwIp_Object = MibScalar
ruckusSCGPgwIp = _RuckusSCGPgwIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 325),
    _RuckusSCGPgwIp_Type()
)
ruckusSCGPgwIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGPgwIp.setStatus("current")
_RuckusSCGFileName_Type = OctetString
_RuckusSCGFileName_Object = MibScalar
ruckusSCGFileName = _RuckusSCGFileName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 326),
    _RuckusSCGFileName_Type()
)
ruckusSCGFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGFileName.setStatus("current")
_RuckusSCGLDAPSrvrIp_Type = OctetString
_RuckusSCGLDAPSrvrIp_Object = MibScalar
ruckusSCGLDAPSrvrIp = _RuckusSCGLDAPSrvrIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 327),
    _RuckusSCGLDAPSrvrIp_Type()
)
ruckusSCGLDAPSrvrIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGLDAPSrvrIp.setStatus("current")
_RuckusSCGADSrvrIp_Type = OctetString
_RuckusSCGADSrvrIp_Object = MibScalar
ruckusSCGADSrvrIp = _RuckusSCGADSrvrIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 328),
    _RuckusSCGADSrvrIp_Type()
)
ruckusSCGADSrvrIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGADSrvrIp.setStatus("current")
_RuckusSCGSoftwareName_Type = OctetString
_RuckusSCGSoftwareName_Object = MibScalar
ruckusSCGSoftwareName = _RuckusSCGSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 329),
    _RuckusSCGSoftwareName_Type()
)
ruckusSCGSoftwareName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGSoftwareName.setStatus("current")
_RuckusSCGDomainName_Type = OctetString
_RuckusSCGDomainName_Object = MibScalar
ruckusSCGDomainName = _RuckusSCGDomainName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 330),
    _RuckusSCGDomainName_Type()
)
ruckusSCGDomainName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGDomainName.setStatus("current")
_RuckusSCGDNATIp_Type = OctetString
_RuckusSCGDNATIp_Object = MibScalar
ruckusSCGDNATIp = _RuckusSCGDNATIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 331),
    _RuckusSCGDNATIp_Type()
)
ruckusSCGDNATIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGDNATIp.setStatus("current")
_RuckusSCGLMAIp_Type = OctetString
_RuckusSCGLMAIp_Object = MibScalar
ruckusSCGLMAIp = _RuckusSCGLMAIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 400),
    _RuckusSCGLMAIp_Type()
)
ruckusSCGLMAIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGLMAIp.setStatus("current")
_RuckusSCGEventRoguePolicyName_Type = OctetString
_RuckusSCGEventRoguePolicyName_Object = MibScalar
ruckusSCGEventRoguePolicyName = _RuckusSCGEventRoguePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 401),
    _RuckusSCGEventRoguePolicyName_Type()
)
ruckusSCGEventRoguePolicyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventRoguePolicyName.setStatus("current")
_RuckusSCGEventRogueRuleName_Type = OctetString
_RuckusSCGEventRogueRuleName_Object = MibScalar
ruckusSCGEventRogueRuleName = _RuckusSCGEventRogueRuleName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 402),
    _RuckusSCGEventRogueRuleName_Type()
)
ruckusSCGEventRogueRuleName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventRogueRuleName.setStatus("current")
_RuckusSCGEventRogueType_Type = OctetString
_RuckusSCGEventRogueType_Object = MibScalar
ruckusSCGEventRogueType = _RuckusSCGEventRogueType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 2, 403),
    _RuckusSCGEventRogueType_Type()
)
ruckusSCGEventRogueType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruckusSCGEventRogueType.setStatus("current")

# Managed Objects groups


# Notification objects

ruckusSCGSystemMiscEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 1)
)
ruckusSCGSystemMiscEventTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGSystemMiscEventTrap.setStatus(
        "current"
    )

ruckusSCGUpgradeSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 2)
)
ruckusSCGUpgradeSuccessTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventFirmwareVersion"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventUpgradedFirmwareVersion"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGUpgradeSuccessTrap.setStatus(
        "current"
    )

ruckusSCGUpgradeFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 3)
)
ruckusSCGUpgradeFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventFirmwareVersion"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventUpgradedFirmwareVersion"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGUpgradeFailedTrap.setStatus(
        "current"
    )

ruckusSCGNodeRestartedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 4)
)
ruckusSCGNodeRestartedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGNodeRestartedTrap.setStatus(
        "current"
    )

ruckusSCGNodeShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 5)
)
ruckusSCGNodeShutdownTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGNodeShutdownTrap.setStatus(
        "current"
    )

ruckusSCGCPUUsageThresholdExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 6)
)
ruckusSCGCPUUsageThresholdExceededTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGCPUPerc"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGCPUUsageThresholdExceededTrap.setStatus(
        "current"
    )

ruckusSCGMemoryUsageThresholdExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 7)
)
ruckusSCGMemoryUsageThresholdExceededTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGMemoryPerc"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGMemoryUsageThresholdExceededTrap.setStatus(
        "current"
    )

ruckusSCGDiskUsageThresholdExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 8)
)
ruckusSCGDiskUsageThresholdExceededTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDiskPerc"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDiskUsageThresholdExceededTrap.setStatus(
        "current"
    )

ruckusSCGLicenseUsageThresholdExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 19)
)
ruckusSCGLicenseUsageThresholdExceededTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLicenseType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLicenseUsagePerc"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGLicenseUsageThresholdExceededTrap.setStatus(
        "current"
    )

ruckusSCGAPMiscEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 20)
)
ruckusSCGAPMiscEventTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPMiscEventTrap.setStatus(
        "current"
    )

ruckusSCGAPConnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 21)
)
ruckusSCGAPConnectedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPConnectedTrap.setStatus(
        "current"
    )

ruckusSCGAPDeletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 22)
)
ruckusSCGAPDeletedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPDeletedTrap.setStatus(
        "current"
    )

ruckusSCGAPDisconnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 23)
)
ruckusSCGAPDisconnectedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPDisconnectedTrap.setStatus(
        "current"
    )

ruckusSCGAPLostHeartbeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 24)
)
ruckusSCGAPLostHeartbeatTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPLostHeartbeatTrap.setStatus(
        "current"
    )

ruckusSCGAPRebootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 25)
)
ruckusSCGAPRebootTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPRebootTrap.setStatus(
        "current"
    )

ruckusSCGCriticalAPConnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 26)
)
ruckusSCGCriticalAPConnectedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGCriticalAPConnectedTrap.setStatus(
        "current"
    )

ruckusSCGCriticalAPDisconnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 27)
)
ruckusSCGCriticalAPDisconnectedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGCriticalAPDisconnectedTrap.setStatus(
        "current"
    )

ruckusSCGAPRejectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 28)
)
ruckusSCGAPRejectedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCtrlIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPRejectedTrap.setStatus(
        "current"
    )

ruckusSCGAPConfUpdateFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 29)
)
ruckusSCGAPConfUpdateFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGAPConfigID"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPConfUpdateFailedTrap.setStatus(
        "current"
    )

ruckusSCGAPConfUpdatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 30)
)
ruckusSCGAPConfUpdatedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGAPConfigID"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPConfUpdatedTrap.setStatus(
        "current"
    )

ruckusSCGAPSwapOutModelDiffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 31)
)
ruckusSCGAPSwapOutModelDiffTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGAPModel"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGConfigAPModel"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPSwapOutModelDiffTrap.setStatus(
        "current"
    )

ruckusSCGAPPreProvisionModelDiffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 32)
)
ruckusSCGAPPreProvisionModelDiffTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGAPModel"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGConfigAPModel"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPPreProvisionModelDiffTrap.setStatus(
        "current"
    )

ruckusSCGAPDiscoveryFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 33)
)
ruckusSCGAPDiscoveryFailTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCtrlIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPDiscoveryFailTrap.setStatus(
        "current"
    )

ruckusSCGAPFirmwareUpdateFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 34)
)
ruckusSCGAPFirmwareUpdateFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPFirmwareUpdateFailedTrap.setStatus(
        "current"
    )

ruckusSCGAPFirmwareUpdatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 35)
)
ruckusSCGAPFirmwareUpdatedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPFirmwareUpdatedTrap.setStatus(
        "current"
    )

ruckusSCGAPWlanOversubscribedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 36)
)
ruckusSCGAPWlanOversubscribedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPWlanOversubscribedTrap.setStatus(
        "current"
    )

ruckusSCGAPFactoryResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 37)
)
ruckusSCGAPFactoryResetTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPFactoryResetTrap.setStatus(
        "current"
    )

ruckusSCGCableModemDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 38)
)
ruckusSCGCableModemDownTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGCableModemDownTrap.setStatus(
        "current"
    )

ruckusSCGCableModemRebootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 39)
)
ruckusSCGCableModemRebootTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGCableModemRebootTrap.setStatus(
        "current"
    )

ruckusSCGAPJoinZoneFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 40)
)
ruckusSCGAPJoinZoneFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventTargetZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPJoinZoneFailedTrap.setStatus(
        "current"
    )

ruckusSCGAPManagedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 41)
)
ruckusSCGAPManagedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCtrlIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPManagedTrap.setStatus(
        "current"
    )

ruckusSCGCPUUsageThresholdBackToNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 42)
)
ruckusSCGCPUUsageThresholdBackToNormalTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGCPUPerc"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGCPUUsageThresholdBackToNormalTrap.setStatus(
        "current"
    )

ruckusSCGMemoryUsageThresholdBackToNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 43)
)
ruckusSCGMemoryUsageThresholdBackToNormalTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGMemoryPerc"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGMemoryUsageThresholdBackToNormalTrap.setStatus(
        "current"
    )

ruckusSCGDiskUsageThresholdBackToNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 44)
)
ruckusSCGDiskUsageThresholdBackToNormalTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDiskPerc"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDiskUsageThresholdBackToNormalTrap.setStatus(
        "current"
    )

ruckusSCGCableModemUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 45)
)
ruckusSCGCableModemUpTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGCableModemUpTrap.setStatus(
        "current"
    )

ruckusSCGAPDiscoverySuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 46)
)
ruckusSCGAPDiscoverySuccessTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCtrlIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPDiscoverySuccessTrap.setStatus(
        "current"
    )

ruckusSCGCMResetByUserTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 47)
)
ruckusSCGCMResetByUserTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGCMResetByUserTrap.setStatus(
        "current"
    )

ruckusSCGCMResetFactoryByUserTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 48)
)
ruckusSCGCMResetFactoryByUserTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGCMResetFactoryByUserTrap.setStatus(
        "current"
    )

ruckusSCGSSIDSpoofingRogueAPDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 50)
)
ruckusSCGSSIDSpoofingRogueAPDetectedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventRogueMac"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSSID"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGSSIDSpoofingRogueAPDetectedTrap.setStatus(
        "current"
    )

ruckusSCGMacSpoofingRogueAPDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 51)
)
ruckusSCGMacSpoofingRogueAPDetectedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventRogueMac"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSSID"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGMacSpoofingRogueAPDetectedTrap.setStatus(
        "current"
    )

ruckusSCGSameNetworkRogueAPDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 52)
)
ruckusSCGSameNetworkRogueAPDetectedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventRogueMac"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSSID"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGSameNetworkRogueAPDetectedTrap.setStatus(
        "current"
    )

ruckusSCGADHocNetworkRogueAPDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 53)
)
ruckusSCGADHocNetworkRogueAPDetectedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventRogueMac"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSSID"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGADHocNetworkRogueAPDetectedTrap.setStatus(
        "current"
    )

ruckusSCGMaliciousRogueAPTimeoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 54)
)
ruckusSCGMaliciousRogueAPTimeoutTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventRogueMac"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGMaliciousRogueAPTimeoutTrap.setStatus(
        "current"
    )

ruckusSCGAPLBSConnectSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 55)
)
ruckusSCGAPLBSConnectSuccessTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLBSURL"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLBSPort"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPLBSConnectSuccessTrap.setStatus(
        "current"
    )

ruckusSCGAPLBSNoResponsesTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 56)
)
ruckusSCGAPLBSNoResponsesTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLBSURL"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLBSPort"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPLBSNoResponsesTrap.setStatus(
        "current"
    )

ruckusSCGAPLBSAuthFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 57)
)
ruckusSCGAPLBSAuthFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLBSURL"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLBSPort"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPLBSAuthFailedTrap.setStatus(
        "current"
    )

ruckusSCGAPLBSConnectFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 58)
)
ruckusSCGAPLBSConnectFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLBSURL"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLBSPort"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPLBSConnectFailedTrap.setStatus(
        "current"
    )

ruckusSCGGeneralRogueAPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 59)
)
ruckusSCGGeneralRogueAPTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventRogueMac"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSSID"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventRoguePolicyName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventRogueRuleName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventRogueType"))
)
if mibBuilder.loadTexts:
    ruckusSCGGeneralRogueAPTrap.setStatus(
        "current"
    )

ruckusSCGAPTunnelBuildFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 60)
)
ruckusSCGAPTunnelBuildFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPTunnelBuildFailedTrap.setStatus(
        "current"
    )

ruckusSCGAPTunnelBuildSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 61)
)
ruckusSCGAPTunnelBuildSuccessTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPTunnelBuildSuccessTrap.setStatus(
        "current"
    )

ruckusSCGAPTunnelDisconnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 62)
)
ruckusSCGAPTunnelDisconnectedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPTunnelDisconnectedTrap.setStatus(
        "current"
    )

ruckusSCGAPSoftGRETunnelFailoverPtoSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 65)
)
ruckusSCGAPSoftGRETunnelFailoverPtoSTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusPrimaryGRE"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSecondaryGRE"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPSoftGRETunnelFailoverPtoSTrap.setStatus(
        "current"
    )

ruckusSCGAPSoftGRETunnelFailoverStoPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 66)
)
ruckusSCGAPSoftGRETunnelFailoverStoPTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusPrimaryGRE"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSecondaryGRE"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPSoftGRETunnelFailoverStoPTrap.setStatus(
        "current"
    )

ruckusSCGAPSoftGREGatewayNotReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 67)
)
ruckusSCGAPSoftGREGatewayNotReachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSoftGREGatewayList"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPSoftGREGatewayNotReachableTrap.setStatus(
        "current"
    )

ruckusSCGAPSoftGREGatewayReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 68)
)
ruckusSCGAPSoftGREGatewayReachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSoftGREGWAddress"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPSoftGREGatewayReachableTrap.setStatus(
        "current"
    )

ruckusSCGDPConfUpdateFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 70)
)
ruckusSCGDPConfUpdateFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPConfigID"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPConfUpdateFailedTrap.setStatus(
        "current"
    )

ruckusSCGDPLostHeartbeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 71)
)
ruckusSCGDPLostHeartbeatTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPLostHeartbeatTrap.setStatus(
        "current"
    )

ruckusSCGDPDisconnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 72)
)
ruckusSCGDPDisconnectedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCtrlIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPDisconnectedTrap.setStatus(
        "current"
    )

ruckusSCGDPPhyInterfaceDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 73)
)
ruckusSCGDPPhyInterfaceDownTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGNetworkPortID"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPPhyInterfaceDownTrap.setStatus(
        "current"
    )

ruckusSCGDPStatusUpdateFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 74)
)
ruckusSCGDPStatusUpdateFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPStatusUpdateFailedTrap.setStatus(
        "current"
    )

ruckusSCGDPStatisticUpdateFaliedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 75)
)
ruckusSCGDPStatisticUpdateFaliedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPStatisticUpdateFaliedTrap.setStatus(
        "current"
    )

ruckusSCGDPConnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 76)
)
ruckusSCGDPConnectedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCtrlIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPConnectedTrap.setStatus(
        "current"
    )

ruckusSCGDPPhyInterfaceUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 77)
)
ruckusSCGDPPhyInterfaceUpTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGNetworkPortID"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPPhyInterfaceUpTrap.setStatus(
        "current"
    )

ruckusSCGDPConfUpdatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 78)
)
ruckusSCGDPConfUpdatedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPConfigID"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPConfUpdatedTrap.setStatus(
        "current"
    )

ruckusSCGDPTunnelTearDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 79)
)
ruckusSCGDPTunnelTearDownTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPTunnelTearDownTrap.setStatus(
        "current"
    )

ruckusSCGDPRebootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 80)
)
ruckusSCGDPRebootTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPRebootTrap.setStatus(
        "current"
    )

ruckusSCGDPAcceptTunnelRequestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 81)
)
ruckusSCGDPAcceptTunnelRequestTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPAcceptTunnelRequestTrap.setStatus(
        "current"
    )

ruckusSCGDPRejectTunnelRequestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 82)
)
ruckusSCGDPRejectTunnelRequestTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPRejectTunnelRequestTrap.setStatus(
        "current"
    )

ruckusSCGDPSgreGWUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 83)
)
ruckusSCGDPSgreGWUnreachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSoftGREGWAddress"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPSgreGWUnreachableTrap.setStatus(
        "current"
    )

ruckusSCGDPSgreGWReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 84)
)
ruckusSCGDPSgreGWReachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSoftGREGWAddress"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPSgreGWReachableTrap.setStatus(
        "current"
    )

ruckusSCGDPTunnelSetUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 85)
)
ruckusSCGDPTunnelSetUpTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPTunnelSetUpTrap.setStatus(
        "current"
    )

ruckusSCGDPDiscoverySuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 86)
)
ruckusSCGDPDiscoverySuccessTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCtrlIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPDiscoverySuccessTrap.setStatus(
        "current"
    )

ruckusSCGDPDiscoveryFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 87)
)
ruckusSCGDPDiscoveryFailTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCtrlIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPDiscoveryFailTrap.setStatus(
        "current"
    )

ruckusSCGDPSgreGWInactTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 88)
)
ruckusSCGDPSgreGWInactTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSoftGREGWAddress"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPSgreGWInactTrap.setStatus(
        "current"
    )

ruckusSCGDPSgreGWActTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 89)
)
ruckusSCGDPSgreGWActTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSoftGREGWAddress"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPSgreGWActTrap.setStatus(
        "current"
    )

ruckusSCGDPPktPoolLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 90)
)
ruckusSCGDPPktPoolLowTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPPacketPoolID"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPPktPoolLowTrap.setStatus(
        "current"
    )

ruckusSCGDPPktPoolCriticalLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 91)
)
ruckusSCGDPPktPoolCriticalLowTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPPacketPoolID"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPPktPoolCriticalLowTrap.setStatus(
        "current"
    )

ruckusSCGDPPktPoolRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 92)
)
ruckusSCGDPPktPoolRecoverTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPPacketPoolID"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPPktPoolRecoverTrap.setStatus(
        "current"
    )

ruckusSCGDPCoreDeadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 93)
)
ruckusSCGDPCoreDeadTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPCoreDeadTrap.setStatus(
        "current"
    )

ruckusSCGDPDeletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 94)
)
ruckusSCGDPDeletedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPDeletedTrap.setStatus(
        "current"
    )

ruckusSCGDPUpgradeStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 95)
)
ruckusSCGDPUpgradeStartTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPUpgradeStartTrap.setStatus(
        "current"
    )

ruckusSCGDPUpgradingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 96)
)
ruckusSCGDPUpgradingTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPUpgradingTrap.setStatus(
        "current"
    )

ruckusSCGDPUpgradeSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 97)
)
ruckusSCGDPUpgradeSuccessTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPUpgradeSuccessTrap.setStatus(
        "current"
    )

ruckusSCGDPUpgradeFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 98)
)
ruckusSCGDPUpgradeFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPKey"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDPUpgradeFailedTrap.setStatus(
        "current"
    )

ruckusSCGClientMiscEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 100)
)
ruckusSCGClientMiscEventTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventClientMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClientMiscEventTrap.setStatus(
        "current"
    )

ruckusSCGNodeJoinFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 200)
)
ruckusSCGNodeJoinFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGNodeJoinFailedTrap.setStatus(
        "current"
    )

ruckusSCGNodeRemoveFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 201)
)
ruckusSCGNodeRemoveFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGNodeRemoveFailedTrap.setStatus(
        "current"
    )

ruckusSCGNodeOutOfServiceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 202)
)
ruckusSCGNodeOutOfServiceTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGNodeOutOfServiceTrap.setStatus(
        "current"
    )

ruckusSCGClusterInMaintenanceStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 203)
)
ruckusSCGClusterInMaintenanceStateTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClusterInMaintenanceStateTrap.setStatus(
        "current"
    )

ruckusSCGClusterBackupFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 204)
)
ruckusSCGClusterBackupFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClusterBackupFailedTrap.setStatus(
        "current"
    )

ruckusSCGClusterRestoreFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 205)
)
ruckusSCGClusterRestoreFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClusterRestoreFailedTrap.setStatus(
        "current"
    )

ruckusSCGClusterAppStoppedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 206)
)
ruckusSCGClusterAppStoppedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGProcessName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClusterAppStoppedTrap.setStatus(
        "current"
    )

ruckusSCGNodeBondInterfaceDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 207)
)
ruckusSCGNodeBondInterfaceDownTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGNetworkInterface"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGNodeBondInterfaceDownTrap.setStatus(
        "current"
    )

ruckusSCGNodePhyInterfaceDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 208)
)
ruckusSCGNodePhyInterfaceDownTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGNetworkInterface"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGNodePhyInterfaceDownTrap.setStatus(
        "current"
    )

ruckusSCGClusterLeaderChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 209)
)
ruckusSCGClusterLeaderChangedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClusterLeaderChangedTrap.setStatus(
        "current"
    )

ruckusSCGClusterUpgradeSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 210)
)
ruckusSCGClusterUpgradeSuccessTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventFirmwareVersion"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventUpgradedFirmwareVersion"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClusterUpgradeSuccessTrap.setStatus(
        "current"
    )

ruckusSCGNodeBondInterfaceUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 211)
)
ruckusSCGNodeBondInterfaceUpTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGNetworkInterface"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGNodeBondInterfaceUpTrap.setStatus(
        "current"
    )

ruckusSCGNodePhyInterfaceUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 212)
)
ruckusSCGNodePhyInterfaceUpTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGNetworkInterface"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGNodePhyInterfaceUpTrap.setStatus(
        "current"
    )

ruckusSCGClusterBackToInServiceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 216)
)
ruckusSCGClusterBackToInServiceTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClusterBackToInServiceTrap.setStatus(
        "current"
    )

ruckusSCGBackupClusterSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 217)
)
ruckusSCGBackupClusterSuccessTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGBackupClusterSuccessTrap.setStatus(
        "current"
    )

ruckusSCGNodeJoinSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 218)
)
ruckusSCGNodeJoinSuccessTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGNodeJoinSuccessTrap.setStatus(
        "current"
    )

ruckusSCGClusterAppStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 219)
)
ruckusSCGClusterAppStartTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGProcessName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClusterAppStartTrap.setStatus(
        "current"
    )

ruckusSCGNodeRemoveSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 220)
)
ruckusSCGNodeRemoveSuccessTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGNodeRemoveSuccessTrap.setStatus(
        "current"
    )

ruckusSCGClusterRestoreSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 221)
)
ruckusSCGClusterRestoreSuccessTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClusterRestoreSuccessTrap.setStatus(
        "current"
    )

ruckusSCGNodeBackToInServiceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 222)
)
ruckusSCGNodeBackToInServiceTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGNodeBackToInServiceTrap.setStatus(
        "current"
    )

ruckusSCGSshTunnelSwitchedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 223)
)
ruckusSCGSshTunnelSwitchedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSwitchStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGSshTunnelSwitchedTrap.setStatus(
        "current"
    )

ruckusSCGClusterCfgBackupStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 224)
)
ruckusSCGClusterCfgBackupStartTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClusterCfgBackupStartTrap.setStatus(
        "current"
    )

ruckusSCGClusterCfgBackupSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 225)
)
ruckusSCGClusterCfgBackupSuccessTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClusterCfgBackupSuccessTrap.setStatus(
        "current"
    )

ruckusSCGClusterCfgBackupFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 226)
)
ruckusSCGClusterCfgBackupFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClusterCfgBackupFailedTrap.setStatus(
        "current"
    )

ruckusSCGClusterCfgRestoreSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 227)
)
ruckusSCGClusterCfgRestoreSuccessTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClusterCfgRestoreSuccessTrap.setStatus(
        "current"
    )

ruckusSCGClusterCfgRestoreFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 228)
)
ruckusSCGClusterCfgRestoreFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClusterCfgRestoreFailedTrap.setStatus(
        "current"
    )

ruckusSCGClusterUploadSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 229)
)
ruckusSCGClusterUploadSuccessTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClusterUploadSuccessTrap.setStatus(
        "current"
    )

ruckusSCGClusterUploadFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 230)
)
ruckusSCGClusterUploadFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClusterUploadFailedTrap.setStatus(
        "current"
    )

ruckusSCGClusterOutOfServiceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 231)
)
ruckusSCGClusterOutOfServiceTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClusterOutOfServiceTrap.setStatus(
        "current"
    )

ruckusSCGClusterUploadVDPFirmwareStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 232)
)
ruckusSCGClusterUploadVDPFirmwareStartTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClusterUploadVDPFirmwareStartTrap.setStatus(
        "current"
    )

ruckusSCGClusterUploadVDPFirmwareSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 233)
)
ruckusSCGClusterUploadVDPFirmwareSuccessTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClusterUploadVDPFirmwareSuccessTrap.setStatus(
        "current"
    )

ruckusSCGClusterUploadVDPFirmwareFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 234)
)
ruckusSCGClusterUploadVDPFirmwareFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGClusterName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGClusterUploadVDPFirmwareFailedTrap.setStatus(
        "current"
    )

ruckusSCGIpmiVotageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 250)
)
ruckusSCGIpmiVotageTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGTemperatureStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiVotageTrap.setStatus(
        "current"
    )

ruckusSCGIpmiTempBBTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 251)
)
ruckusSCGIpmiTempBBTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGTemperatureStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiTempBBTrap.setStatus(
        "current"
    )

ruckusSCGIpmiTempFPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 252)
)
ruckusSCGIpmiTempFPTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGTemperatureStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiTempFPTrap.setStatus(
        "current"
    )

ruckusSCGIpmiTempIOHTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 253)
)
ruckusSCGIpmiTempIOHTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGTemperatureStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiTempIOHTrap.setStatus(
        "current"
    )

ruckusSCGIpmiTempMemPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 254)
)
ruckusSCGIpmiTempMemPTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGProcessorId"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGTemperatureStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiTempMemPTrap.setStatus(
        "current"
    )

ruckusSCGIpmiTempPSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 255)
)
ruckusSCGIpmiTempPSTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPsId"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGTemperatureStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiTempPSTrap.setStatus(
        "current"
    )

ruckusSCGIpmiTempPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 256)
)
ruckusSCGIpmiTempPTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGProcessorId"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGTemperatureStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiTempPTrap.setStatus(
        "current"
    )

ruckusSCGIpmiTempHSBPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 257)
)
ruckusSCGIpmiTempHSBPTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGTemperatureStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiTempHSBPTrap.setStatus(
        "current"
    )

ruckusSCGIpmiFanTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 258)
)
ruckusSCGIpmiFanTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGFanId"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGFanStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiFanTrap.setStatus(
        "current"
    )

ruckusSCGIpmiPowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 259)
)
ruckusSCGIpmiPowerTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPsId"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPsStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiPowerTrap.setStatus(
        "current"
    )

ruckusSCGIpmiCurrentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 260)
)
ruckusSCGIpmiCurrentTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPsId"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPsStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiCurrentTrap.setStatus(
        "current"
    )

ruckusSCGIpmiFanStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 261)
)
ruckusSCGIpmiFanStatusTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGFanId"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGFanStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiFanStatusTrap.setStatus(
        "current"
    )

ruckusSCGIpmiPsStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 262)
)
ruckusSCGIpmiPsStatusTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPsId"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPsStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiPsStatusTrap.setStatus(
        "current"
    )

ruckusSCGIpmiDrvStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 263)
)
ruckusSCGIpmiDrvStatusTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDrvId"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDrvStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiDrvStatusTrap.setStatus(
        "current"
    )

ruckusSCGIpmiREVotageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 264)
)
ruckusSCGIpmiREVotageTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGTemperatureStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiREVotageTrap.setStatus(
        "current"
    )

ruckusSCGIpmiRETempBBTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 265)
)
ruckusSCGIpmiRETempBBTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGTemperatureStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiRETempBBTrap.setStatus(
        "current"
    )

ruckusSCGIpmiRETempFPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 266)
)
ruckusSCGIpmiRETempFPTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGTemperatureStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiRETempFPTrap.setStatus(
        "current"
    )

ruckusSCGIpmiRETempIOHTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 267)
)
ruckusSCGIpmiRETempIOHTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGTemperatureStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiRETempIOHTrap.setStatus(
        "current"
    )

ruckusSCGIpmiRETempMemPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 268)
)
ruckusSCGIpmiRETempMemPTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGProcessorId"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGTemperatureStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiRETempMemPTrap.setStatus(
        "current"
    )

ruckusSCGIpmiRETempPSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 269)
)
ruckusSCGIpmiRETempPSTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPsId"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGTemperatureStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiRETempPSTrap.setStatus(
        "current"
    )

ruckusSCGIpmiRETempPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 270)
)
ruckusSCGIpmiRETempPTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGProcessorId"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGTemperatureStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiRETempPTrap.setStatus(
        "current"
    )

ruckusSCGIpmiRETempHSBPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 271)
)
ruckusSCGIpmiRETempHSBPTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGTemperatureStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiRETempHSBPTrap.setStatus(
        "current"
    )

ruckusSCGIpmiREFanTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 272)
)
ruckusSCGIpmiREFanTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGFanId"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGFanStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiREFanTrap.setStatus(
        "current"
    )

ruckusSCGIpmiREPowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 273)
)
ruckusSCGIpmiREPowerTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPsId"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPsStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiREPowerTrap.setStatus(
        "current"
    )

ruckusSCGIpmiRECurrentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 274)
)
ruckusSCGIpmiRECurrentTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPsId"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPsStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiRECurrentTrap.setStatus(
        "current"
    )

ruckusSCGIpmiREFanStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 275)
)
ruckusSCGIpmiREFanStatusTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGFanId"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGFanStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiREFanStatusTrap.setStatus(
        "current"
    )

ruckusSCGIpmiREPsStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 276)
)
ruckusSCGIpmiREPsStatusTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPsId"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPsStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiREPsStatusTrap.setStatus(
        "current"
    )

ruckusSCGIpmiREDrvStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 277)
)
ruckusSCGIpmiREDrvStatusTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDrvId"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDrvStatus"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGIpmiREDrvStatusTrap.setStatus(
        "current"
    )

ruckusSCGFtpTransferErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 280)
)
ruckusSCGFtpTransferErrorTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGFtpIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGFtpPort"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGFileName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGFtpTransferErrorTrap.setStatus(
        "current"
    )

ruckusSCGSystemLBSConnectSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 290)
)
ruckusSCGSystemLBSConnectSuccessTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLBSURL"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLBSPort"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGSystemLBSConnectSuccessTrap.setStatus(
        "current"
    )

ruckusSCGSystemLBSNoResponseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 291)
)
ruckusSCGSystemLBSNoResponseTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLBSURL"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLBSPort"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGSystemLBSNoResponseTrap.setStatus(
        "current"
    )

ruckusSCGSystemLBSAuthFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 292)
)
ruckusSCGSystemLBSAuthFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLBSURL"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLBSPort"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGSystemLBSAuthFailedTrap.setStatus(
        "current"
    )

ruckusSCGSystemLBSConnectFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 293)
)
ruckusSCGSystemLBSConnectFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLBSURL"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLBSPort"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGSystemLBSConnectFailedTrap.setStatus(
        "current"
    )

ruckusSCGProcessRestartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 300)
)
ruckusSCGProcessRestartTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGProcessName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGProcessRestartTrap.setStatus(
        "current"
    )

ruckusSCGServiceUnavailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 301)
)
ruckusSCGServiceUnavailableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGProcessName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGServiceUnavailableTrap.setStatus(
        "current"
    )

ruckusSCGKeepAliveFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 302)
)
ruckusSCGKeepAliveFailureTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcProcess"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGProcessName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGKeepAliveFailureTrap.setStatus(
        "current"
    )

ruckusSCGResourceUnavailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 304)
)
ruckusSCGResourceUnavailableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcProcess"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGResourceUnavailableTrap.setStatus(
        "current"
    )

ruckusSCGSmfRegFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 305)
)
ruckusSCGSmfRegFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcProcess"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGSmfRegFailedTrap.setStatus(
        "current"
    )

ruckusSCGHipFailoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 306)
)
ruckusSCGHipFailoverTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcProcess"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGHipFailoverTrap.setStatus(
        "current"
    )

ruckusSCGConfUpdFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 307)
)
ruckusSCGConfUpdFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGProcessName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGConfUpdFailedTrap.setStatus(
        "current"
    )

ruckusSCGConfRcvFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 308)
)
ruckusSCGConfRcvFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGConfRcvFailedTrap.setStatus(
        "current"
    )

ruckusSCGLostCnxnToDbladeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 309)
)
ruckusSCGLostCnxnToDbladeTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCtrlIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGLostCnxnToDbladeTrap.setStatus(
        "current"
    )

ruckusSCGGgsnRestartedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 310)
)
ruckusSCGGgsnRestartedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGGgsnIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGGtpcIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGGgsnRestartedTrap.setStatus(
        "current"
    )

ruckusSCGGgsnNotReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 311)
)
ruckusSCGGgsnNotReachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGGgsnIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGGtpcIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGGgsnNotReachableTrap.setStatus(
        "current"
    )

ruckusSCGGgsnNotResolvedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 312)
)
ruckusSCGGgsnNotResolvedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGApn"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUEImsi"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUEMsisdn"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGGgsnNotResolvedTrap.setStatus(
        "current"
    )

ruckusSCGUnknownUETrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 313)
)
ruckusSCGUnknownUETrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventClientMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUEMsisdn"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGUnknownUETrap.setStatus(
        "current"
    )

ruckusSCGAuthSrvrNotReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 314)
)
ruckusSCGAuthSrvrNotReachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGAuthSrvrIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGRadProxyIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGAuthSrvrNotReachableTrap.setStatus(
        "current"
    )

ruckusSCGAccSrvrNotReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 315)
)
ruckusSCGAccSrvrNotReachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGAccSrvrIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGRadProxyIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGAccSrvrNotReachableTrap.setStatus(
        "current"
    )

ruckusSCGUnknownRealmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 316)
)
ruckusSCGUnknownRealmTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGRealm"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGUnknownRealmTrap.setStatus(
        "current"
    )

ruckusSCGAuthFailedNonPermanentIDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 317)
)
ruckusSCGAuthFailedNonPermanentIDTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUEImsi"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUEMsisdn"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGAuthFailedNonPermanentIDTrap.setStatus(
        "current"
    )

ruckusSCGCnxnToCgfFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 318)
)
ruckusSCGCnxnToCgfFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGCgfSrvrIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGRadSrvrIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGCnxnToCgfFailedTrap.setStatus(
        "current"
    )

ruckusSCGCdrTransferFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 319)
)
ruckusSCGCdrTransferFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGCgfSrvrIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGRadSrvrIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGCdrTransferFailedTrap.setStatus(
        "current"
    )

ruckusSCGCdrGenerateFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 320)
)
ruckusSCGCdrGenerateFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGRadSrvrIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGCdrGenerateFailedTrap.setStatus(
        "current"
    )

ruckusSCGDestNotRecheableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 321)
)
ruckusSCGDestNotRecheableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPointCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDestNotRecheableTrap.setStatus(
        "current"
    )

ruckusSCGAppServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 324)
)
ruckusSCGAppServerDownTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGRoutingContext"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPointCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSSN"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGAppServerDownTrap.setStatus(
        "current"
    )

ruckusSCGAppServerInactiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 325)
)
ruckusSCGAppServerInactiveTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGRoutingContext"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPointCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSSN"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGAppServerInactiveTrap.setStatus(
        "current"
    )

ruckusSCGAssocCantStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 326)
)
ruckusSCGAssocCantStartTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcPort"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDestIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDestPort"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGAssocCantStartTrap.setStatus(
        "current"
    )

ruckusSCGAssocDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 327)
)
ruckusSCGAssocDownTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcPort"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDestIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDestPort"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGAssocDownTrap.setStatus(
        "current"
    )

ruckusSCGOutboundRoutingFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 328)
)
ruckusSCGOutboundRoutingFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGOperation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUEImsi"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGHlrInstance"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGOutboundRoutingFailedTrap.setStatus(
        "current"
    )

ruckusSCGDidAllocationFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 329)
)
ruckusSCGDidAllocationFailureTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDidAllocationFailureTrap.setStatus(
        "current"
    )

ruckusSCGPdnGwUnresolvedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 331)
)
ruckusSCGPdnGwUnresolvedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcProcess"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGApn"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUEImsi"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUEMsisdn"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGPdnGwUnresolvedTrap.setStatus(
        "current"
    )

ruckusSCGPdnGwVersionUnsupportedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 332)
)
ruckusSCGPdnGwVersionUnsupportedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcProcess"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPgwIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGPdnGwVersionUnsupportedTrap.setStatus(
        "current"
    )

ruckusSCGPdnGwAssociationDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 333)
)
ruckusSCGPdnGwAssociationDownTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcProcess"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPgwIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGPdnGwAssociationDownTrap.setStatus(
        "current"
    )

ruckusSCGCreateSessionResponseFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 334)
)
ruckusSCGCreateSessionResponseFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcProcess"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPgwIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUEImsi"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGRealm"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGCreateSessionResponseFailedTrap.setStatus(
        "current"
    )

ruckusSCGDecodeFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 335)
)
ruckusSCGDecodeFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcProcess"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPgwIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDecodeFailedTrap.setStatus(
        "current"
    )

ruckusSCGModifyBearerResponseFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 336)
)
ruckusSCGModifyBearerResponseFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcProcess"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPgwIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUEImsi"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGRealm"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGModifyBearerResponseFailedTrap.setStatus(
        "current"
    )

ruckusSCGDeleteSessionResponseFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 337)
)
ruckusSCGDeleteSessionResponseFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcProcess"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPgwIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUEImsi"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGRealm"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDeleteSessionResponseFailedTrap.setStatus(
        "current"
    )

ruckusSCGDeleteBearerRequestFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 338)
)
ruckusSCGDeleteBearerRequestFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcProcess"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPgwIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGRealm"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDeleteBearerRequestFailedTrap.setStatus(
        "current"
    )

ruckusSCGUpdateBearerRequestFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 339)
)
ruckusSCGUpdateBearerRequestFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcProcess"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPgwIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGRealm"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventReason"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGUpdateBearerRequestFailedTrap.setStatus(
        "current"
    )

ruckusSCGCgfServerNotConfiguredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 340)
)
ruckusSCGCgfServerNotConfiguredTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGCgfSrvrIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGGgsnIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGCgfServerNotConfiguredTrap.setStatus(
        "current"
    )

ruckusSCGTtgSessionCriticalThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 342)
)
ruckusSCGTtgSessionCriticalThresholdTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGTtgSessionCriticalThresholdTrap.setStatus(
        "current"
    )

ruckusSCGTtgSessionLicenseInsufficientTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 343)
)
ruckusSCGTtgSessionLicenseInsufficientTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGTtgSessionLicenseInsufficientTrap.setStatus(
        "current"
    )

ruckusSCGAPAcctMsgMandatoryPrmMissingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 344)
)
ruckusSCGAPAcctMsgMandatoryPrmMissingTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcProcess"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUserName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPAcctMsgMandatoryPrmMissingTrap.setStatus(
        "current"
    )

ruckusSCGAcctUnknownRealmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 345)
)
ruckusSCGAcctUnknownRealmTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcProcess"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUserName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAcctUnknownRealmTrap.setStatus(
        "current"
    )

ruckusSCGAPAcctMsgDecodeFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 346)
)
ruckusSCGAPAcctMsgDecodeFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcProcess"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPAcctMsgDecodeFailedTrap.setStatus(
        "current"
    )

ruckusSCGAPAcctRespWhileInvalidConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 347)
)
ruckusSCGAPAcctRespWhileInvalidConfigTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcProcess"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUserName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPAcctRespWhileInvalidConfigTrap.setStatus(
        "current"
    )

ruckusSCGAPAcctMsgDropNoAcctStartMsgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 348)
)
ruckusSCGAPAcctMsgDropNoAcctStartMsgTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcProcess"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUserName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPAcctMsgDropNoAcctStartMsgTrap.setStatus(
        "current"
    )

ruckusSCGUnauthorizedCoaDmMessageDroppedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 349)
)
ruckusSCGUnauthorizedCoaDmMessageDroppedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcProcess"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGRadSrvrIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGUnauthorizedCoaDmMessageDroppedTrap.setStatus(
        "current"
    )

ruckusSCGConnectedToDbladeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 350)
)
ruckusSCGConnectedToDbladeTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCtrlIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGConnectedToDbladeTrap.setStatus(
        "current"
    )

ruckusSCGDestAvailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 351)
)
ruckusSCGDestAvailableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPointCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGDestAvailableTrap.setStatus(
        "current"
    )

ruckusSCGAppServerActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 352)
)
ruckusSCGAppServerActiveTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGRoutingContext"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGPointCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSSN"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGAppServerActiveTrap.setStatus(
        "current"
    )

ruckusSCGAssocUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 353)
)
ruckusSCGAssocUpTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcPort"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDestIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDestPort"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGAssocUpTrap.setStatus(
        "current"
    )

ruckusSCGSessUpdatedAtDbladeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 354)
)
ruckusSCGSessUpdatedAtDbladeTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCtrlIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUEImsi"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUEMsisdn"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGSessUpdatedAtDbladeTrap.setStatus(
        "current"
    )

ruckusSCGSessUpdateErrAtDbladeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 355)
)
ruckusSCGSessUpdateErrAtDbladeTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCtrlIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUEImsi"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUEMsisdn"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGSessUpdateErrAtDbladeTrap.setStatus(
        "current"
    )

ruckusSCGSessDeletedAtDbladeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 356)
)
ruckusSCGSessDeletedAtDbladeTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCtrlIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUEImsi"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUEMsisdn"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGSessDeletedAtDbladeTrap.setStatus(
        "current"
    )

ruckusSCGSessDeleteErrAtDbladeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 357)
)
ruckusSCGSessDeleteErrAtDbladeTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCtrlIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUEImsi"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGUEMsisdn"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGSessDeleteErrAtDbladeTrap.setStatus(
        "current"
    )

ruckusSCGLicenseSyncSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 358)
)
ruckusSCGLicenseSyncSuccessTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLicenseServerName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGLicenseSyncSuccessTrap.setStatus(
        "current"
    )

ruckusSCGLicenseSyncFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 359)
)
ruckusSCGLicenseSyncFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLicenseServerName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGLicenseSyncFailedTrap.setStatus(
        "current"
    )

ruckusSCGLicenseImportSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 360)
)
ruckusSCGLicenseImportSuccessTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGLicenseImportSuccessTrap.setStatus(
        "current"
    )

ruckusSCGLicenseImportFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 361)
)
ruckusSCGLicenseImportFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGLicenseImportFailedTrap.setStatus(
        "current"
    )

ruckusSCGSyslogServerReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 370)
)
ruckusSCGSyslogServerReachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSyslogServerAddress"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGSyslogServerReachableTrap.setStatus(
        "current"
    )

ruckusSCGSyslogServerUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 371)
)
ruckusSCGSyslogServerUnreachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSyslogServerAddress"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGSyslogServerUnreachableTrap.setStatus(
        "current"
    )

ruckusSCGSyslogServerSwitchedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 372)
)
ruckusSCGSyslogServerSwitchedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSrcSyslogServerAddress"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDestSyslogServerAddress"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGSyslogServerSwitchedTrap.setStatus(
        "current"
    )

ruckusSCGAPRadiusServerReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 400)
)
ruckusSCGAPRadiusServerReachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGRadSrvrIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPRadiusServerReachableTrap.setStatus(
        "current"
    )

ruckusSCGAPRadiusServerUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 401)
)
ruckusSCGAPRadiusServerUnreachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGRadSrvrIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPRadiusServerUnreachableTrap.setStatus(
        "current"
    )

ruckusSCGAPLDAPServerReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 402)
)
ruckusSCGAPLDAPServerReachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLDAPSrvrIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPLDAPServerReachableTrap.setStatus(
        "current"
    )

ruckusSCGAPLDAPServerUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 403)
)
ruckusSCGAPLDAPServerUnreachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLDAPSrvrIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPLDAPServerUnreachableTrap.setStatus(
        "current"
    )

ruckusSCGAPADServerReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 404)
)
ruckusSCGAPADServerReachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGADSrvrIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPADServerReachableTrap.setStatus(
        "current"
    )

ruckusSCGAPADServerUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 405)
)
ruckusSCGAPADServerUnreachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGADSrvrIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPADServerUnreachableTrap.setStatus(
        "current"
    )

ruckusSCGAPUsbSoftwarePackageDownloadedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 406)
)
ruckusSCGAPUsbSoftwarePackageDownloadedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSoftwareName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPUsbSoftwarePackageDownloadedTrap.setStatus(
        "current"
    )

ruckusSCGAPUsbSoftwarePackageDownloadFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 407)
)
ruckusSCGAPUsbSoftwarePackageDownloadFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGSoftwareName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGAPUsbSoftwarePackageDownloadFailedTrap.setStatus(
        "current"
    )

ruckusSCGEspAuthServerReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 408)
)
ruckusSCGEspAuthServerReachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGAuthSrvrIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGEspAuthServerReachableTrap.setStatus(
        "current"
    )

ruckusSCGEspAuthServerUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 409)
)
ruckusSCGEspAuthServerUnreachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGAuthSrvrIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGEspAuthServerUnreachableTrap.setStatus(
        "current"
    )

ruckusSCGEspAuthServerResolvableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 410)
)
ruckusSCGEspAuthServerResolvableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDomainName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGEspAuthServerResolvableTrap.setStatus(
        "current"
    )

ruckusSCGEspAuthServerUnResolvableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 411)
)
ruckusSCGEspAuthServerUnResolvableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDomainName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGEspAuthServerUnResolvableTrap.setStatus(
        "current"
    )

ruckusSCGEspDNATServerReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 412)
)
ruckusSCGEspDNATServerReachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDNATIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGEspDNATServerReachableTrap.setStatus(
        "current"
    )

ruckusSCGEspDNATServerUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 413)
)
ruckusSCGEspDNATServerUnreachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDNATIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGEspDNATServerUnreachableTrap.setStatus(
        "current"
    )

ruckusSCGEspDNATServerResolvableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 414)
)
ruckusSCGEspDNATServerResolvableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDomainName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGEspDNATServerResolvableTrap.setStatus(
        "current"
    )

ruckusSCGEspDNATServerUnresolvableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 415)
)
ruckusSCGEspDNATServerUnresolvableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGDomainName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGEspDNATServerUnresolvableTrap.setStatus(
        "current"
    )

ruckusRateLimitTORSurpassedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 500)
)
ruckusRateLimitTORSurpassedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGRadSrvrIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusRateLimitTORSurpassedTrap.setStatus(
        "current"
    )

ruckusSCGIPSecTunnelAssociatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 600)
)
ruckusSCGIPSecTunnelAssociatedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGIPSecGWAddress"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGIPSecTunnelAssociatedTrap.setStatus(
        "current"
    )

ruckusSCGIPSecTunnelDisassociatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 601)
)
ruckusSCGIPSecTunnelDisassociatedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGIPSecGWAddress"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGIPSecTunnelDisassociatedTrap.setStatus(
        "current"
    )

ruckusSCGIPSecTunnelAssociateFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 602)
)
ruckusSCGIPSecTunnelAssociateFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIP"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPLocation"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPDescription"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPGPSCoordinates"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventZoneName"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGIPSecGWAddress"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventAPIPv6"))
)
if mibBuilder.loadTexts:
    ruckusSCGIPSecTunnelAssociateFailedTrap.setStatus(
        "current"
    )

ruckusSCGPmipProcessInitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 700)
)
ruckusSCGPmipProcessInitTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGPmipProcessInitTrap.setStatus(
        "current"
    )

ruckusSCGPmipUnavailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 701)
)
ruckusSCGPmipUnavailableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGPmipUnavailableTrap.setStatus(
        "current"
    )

ruckusSCGPmipUnallocatedMemoryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 702)
)
ruckusSCGPmipUnallocatedMemoryTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGPmipUnallocatedMemoryTrap.setStatus(
        "current"
    )

ruckusSCGPmipUpdateCgfFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 703)
)
ruckusSCGPmipUpdateCgfFailedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGPmipUpdateCgfFailedTrap.setStatus(
        "current"
    )

ruckusSCGPmipLMAIcmpUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 704)
)
ruckusSCGPmipLMAIcmpUnreachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLMAIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGPmipLMAIcmpUnreachableTrap.setStatus(
        "current"
    )

ruckusSCGPmipLMAFailOverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 705)
)
ruckusSCGPmipLMAFailOverTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLMAIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGPmipLMAFailOverTrap.setStatus(
        "current"
    )

ruckusSCGPmipBindingFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 706)
)
ruckusSCGPmipBindingFailureTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGPmipBindingFailureTrap.setStatus(
        "current"
    )

ruckusSCGPmiplostCnxnToDHCPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 707)
)
ruckusSCGPmiplostCnxnToDHCPTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGPmiplostCnxnToDHCPTrap.setStatus(
        "current"
    )

ruckusSCGPmipLMAIcmpReachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 708)
)
ruckusSCGPmipLMAIcmpReachableTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGLMAIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGPmipLMAIcmpReachableTrap.setStatus(
        "current"
    )

ruckusSCGPmipBindingSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 709)
)
ruckusSCGPmipBindingSuccessTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGPmipBindingSuccessTrap.setStatus(
        "current"
    )

ruckusSCGPmipConnectedToDHCPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 710)
)
ruckusSCGPmipConnectedToDHCPTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGPmipConnectedToDHCPTrap.setStatus(
        "current"
    )

ruckusSCGPmipProcessStoppedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25053, 2, 10, 1, 711)
)
ruckusSCGPmipProcessStoppedTrap.setObjects(
      *(("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventSeverity"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventType"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventMacAddr"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventNodeMgmtIp"),
        ("RUCKUS-SCG-EVENT-MIB", "ruckusSCGEventCode"))
)
if mibBuilder.loadTexts:
    ruckusSCGPmipProcessStoppedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-SCG-EVENT-MIB",
    **{"ruckusSCGEventMIB": ruckusSCGEventMIB,
       "ruckusSCGEventTraps": ruckusSCGEventTraps,
       "ruckusSCGSystemMiscEventTrap": ruckusSCGSystemMiscEventTrap,
       "ruckusSCGUpgradeSuccessTrap": ruckusSCGUpgradeSuccessTrap,
       "ruckusSCGUpgradeFailedTrap": ruckusSCGUpgradeFailedTrap,
       "ruckusSCGNodeRestartedTrap": ruckusSCGNodeRestartedTrap,
       "ruckusSCGNodeShutdownTrap": ruckusSCGNodeShutdownTrap,
       "ruckusSCGCPUUsageThresholdExceededTrap": ruckusSCGCPUUsageThresholdExceededTrap,
       "ruckusSCGMemoryUsageThresholdExceededTrap": ruckusSCGMemoryUsageThresholdExceededTrap,
       "ruckusSCGDiskUsageThresholdExceededTrap": ruckusSCGDiskUsageThresholdExceededTrap,
       "ruckusSCGLicenseUsageThresholdExceededTrap": ruckusSCGLicenseUsageThresholdExceededTrap,
       "ruckusSCGAPMiscEventTrap": ruckusSCGAPMiscEventTrap,
       "ruckusSCGAPConnectedTrap": ruckusSCGAPConnectedTrap,
       "ruckusSCGAPDeletedTrap": ruckusSCGAPDeletedTrap,
       "ruckusSCGAPDisconnectedTrap": ruckusSCGAPDisconnectedTrap,
       "ruckusSCGAPLostHeartbeatTrap": ruckusSCGAPLostHeartbeatTrap,
       "ruckusSCGAPRebootTrap": ruckusSCGAPRebootTrap,
       "ruckusSCGCriticalAPConnectedTrap": ruckusSCGCriticalAPConnectedTrap,
       "ruckusSCGCriticalAPDisconnectedTrap": ruckusSCGCriticalAPDisconnectedTrap,
       "ruckusSCGAPRejectedTrap": ruckusSCGAPRejectedTrap,
       "ruckusSCGAPConfUpdateFailedTrap": ruckusSCGAPConfUpdateFailedTrap,
       "ruckusSCGAPConfUpdatedTrap": ruckusSCGAPConfUpdatedTrap,
       "ruckusSCGAPSwapOutModelDiffTrap": ruckusSCGAPSwapOutModelDiffTrap,
       "ruckusSCGAPPreProvisionModelDiffTrap": ruckusSCGAPPreProvisionModelDiffTrap,
       "ruckusSCGAPDiscoveryFailTrap": ruckusSCGAPDiscoveryFailTrap,
       "ruckusSCGAPFirmwareUpdateFailedTrap": ruckusSCGAPFirmwareUpdateFailedTrap,
       "ruckusSCGAPFirmwareUpdatedTrap": ruckusSCGAPFirmwareUpdatedTrap,
       "ruckusSCGAPWlanOversubscribedTrap": ruckusSCGAPWlanOversubscribedTrap,
       "ruckusSCGAPFactoryResetTrap": ruckusSCGAPFactoryResetTrap,
       "ruckusSCGCableModemDownTrap": ruckusSCGCableModemDownTrap,
       "ruckusSCGCableModemRebootTrap": ruckusSCGCableModemRebootTrap,
       "ruckusSCGAPJoinZoneFailedTrap": ruckusSCGAPJoinZoneFailedTrap,
       "ruckusSCGAPManagedTrap": ruckusSCGAPManagedTrap,
       "ruckusSCGCPUUsageThresholdBackToNormalTrap": ruckusSCGCPUUsageThresholdBackToNormalTrap,
       "ruckusSCGMemoryUsageThresholdBackToNormalTrap": ruckusSCGMemoryUsageThresholdBackToNormalTrap,
       "ruckusSCGDiskUsageThresholdBackToNormalTrap": ruckusSCGDiskUsageThresholdBackToNormalTrap,
       "ruckusSCGCableModemUpTrap": ruckusSCGCableModemUpTrap,
       "ruckusSCGAPDiscoverySuccessTrap": ruckusSCGAPDiscoverySuccessTrap,
       "ruckusSCGCMResetByUserTrap": ruckusSCGCMResetByUserTrap,
       "ruckusSCGCMResetFactoryByUserTrap": ruckusSCGCMResetFactoryByUserTrap,
       "ruckusSCGSSIDSpoofingRogueAPDetectedTrap": ruckusSCGSSIDSpoofingRogueAPDetectedTrap,
       "ruckusSCGMacSpoofingRogueAPDetectedTrap": ruckusSCGMacSpoofingRogueAPDetectedTrap,
       "ruckusSCGSameNetworkRogueAPDetectedTrap": ruckusSCGSameNetworkRogueAPDetectedTrap,
       "ruckusSCGADHocNetworkRogueAPDetectedTrap": ruckusSCGADHocNetworkRogueAPDetectedTrap,
       "ruckusSCGMaliciousRogueAPTimeoutTrap": ruckusSCGMaliciousRogueAPTimeoutTrap,
       "ruckusSCGAPLBSConnectSuccessTrap": ruckusSCGAPLBSConnectSuccessTrap,
       "ruckusSCGAPLBSNoResponsesTrap": ruckusSCGAPLBSNoResponsesTrap,
       "ruckusSCGAPLBSAuthFailedTrap": ruckusSCGAPLBSAuthFailedTrap,
       "ruckusSCGAPLBSConnectFailedTrap": ruckusSCGAPLBSConnectFailedTrap,
       "ruckusSCGGeneralRogueAPTrap": ruckusSCGGeneralRogueAPTrap,
       "ruckusSCGAPTunnelBuildFailedTrap": ruckusSCGAPTunnelBuildFailedTrap,
       "ruckusSCGAPTunnelBuildSuccessTrap": ruckusSCGAPTunnelBuildSuccessTrap,
       "ruckusSCGAPTunnelDisconnectedTrap": ruckusSCGAPTunnelDisconnectedTrap,
       "ruckusSCGAPSoftGRETunnelFailoverPtoSTrap": ruckusSCGAPSoftGRETunnelFailoverPtoSTrap,
       "ruckusSCGAPSoftGRETunnelFailoverStoPTrap": ruckusSCGAPSoftGRETunnelFailoverStoPTrap,
       "ruckusSCGAPSoftGREGatewayNotReachableTrap": ruckusSCGAPSoftGREGatewayNotReachableTrap,
       "ruckusSCGAPSoftGREGatewayReachableTrap": ruckusSCGAPSoftGREGatewayReachableTrap,
       "ruckusSCGDPConfUpdateFailedTrap": ruckusSCGDPConfUpdateFailedTrap,
       "ruckusSCGDPLostHeartbeatTrap": ruckusSCGDPLostHeartbeatTrap,
       "ruckusSCGDPDisconnectedTrap": ruckusSCGDPDisconnectedTrap,
       "ruckusSCGDPPhyInterfaceDownTrap": ruckusSCGDPPhyInterfaceDownTrap,
       "ruckusSCGDPStatusUpdateFailedTrap": ruckusSCGDPStatusUpdateFailedTrap,
       "ruckusSCGDPStatisticUpdateFaliedTrap": ruckusSCGDPStatisticUpdateFaliedTrap,
       "ruckusSCGDPConnectedTrap": ruckusSCGDPConnectedTrap,
       "ruckusSCGDPPhyInterfaceUpTrap": ruckusSCGDPPhyInterfaceUpTrap,
       "ruckusSCGDPConfUpdatedTrap": ruckusSCGDPConfUpdatedTrap,
       "ruckusSCGDPTunnelTearDownTrap": ruckusSCGDPTunnelTearDownTrap,
       "ruckusSCGDPRebootTrap": ruckusSCGDPRebootTrap,
       "ruckusSCGDPAcceptTunnelRequestTrap": ruckusSCGDPAcceptTunnelRequestTrap,
       "ruckusSCGDPRejectTunnelRequestTrap": ruckusSCGDPRejectTunnelRequestTrap,
       "ruckusSCGDPSgreGWUnreachableTrap": ruckusSCGDPSgreGWUnreachableTrap,
       "ruckusSCGDPSgreGWReachableTrap": ruckusSCGDPSgreGWReachableTrap,
       "ruckusSCGDPTunnelSetUpTrap": ruckusSCGDPTunnelSetUpTrap,
       "ruckusSCGDPDiscoverySuccessTrap": ruckusSCGDPDiscoverySuccessTrap,
       "ruckusSCGDPDiscoveryFailTrap": ruckusSCGDPDiscoveryFailTrap,
       "ruckusSCGDPSgreGWInactTrap": ruckusSCGDPSgreGWInactTrap,
       "ruckusSCGDPSgreGWActTrap": ruckusSCGDPSgreGWActTrap,
       "ruckusSCGDPPktPoolLowTrap": ruckusSCGDPPktPoolLowTrap,
       "ruckusSCGDPPktPoolCriticalLowTrap": ruckusSCGDPPktPoolCriticalLowTrap,
       "ruckusSCGDPPktPoolRecoverTrap": ruckusSCGDPPktPoolRecoverTrap,
       "ruckusSCGDPCoreDeadTrap": ruckusSCGDPCoreDeadTrap,
       "ruckusSCGDPDeletedTrap": ruckusSCGDPDeletedTrap,
       "ruckusSCGDPUpgradeStartTrap": ruckusSCGDPUpgradeStartTrap,
       "ruckusSCGDPUpgradingTrap": ruckusSCGDPUpgradingTrap,
       "ruckusSCGDPUpgradeSuccessTrap": ruckusSCGDPUpgradeSuccessTrap,
       "ruckusSCGDPUpgradeFailedTrap": ruckusSCGDPUpgradeFailedTrap,
       "ruckusSCGClientMiscEventTrap": ruckusSCGClientMiscEventTrap,
       "ruckusSCGNodeJoinFailedTrap": ruckusSCGNodeJoinFailedTrap,
       "ruckusSCGNodeRemoveFailedTrap": ruckusSCGNodeRemoveFailedTrap,
       "ruckusSCGNodeOutOfServiceTrap": ruckusSCGNodeOutOfServiceTrap,
       "ruckusSCGClusterInMaintenanceStateTrap": ruckusSCGClusterInMaintenanceStateTrap,
       "ruckusSCGClusterBackupFailedTrap": ruckusSCGClusterBackupFailedTrap,
       "ruckusSCGClusterRestoreFailedTrap": ruckusSCGClusterRestoreFailedTrap,
       "ruckusSCGClusterAppStoppedTrap": ruckusSCGClusterAppStoppedTrap,
       "ruckusSCGNodeBondInterfaceDownTrap": ruckusSCGNodeBondInterfaceDownTrap,
       "ruckusSCGNodePhyInterfaceDownTrap": ruckusSCGNodePhyInterfaceDownTrap,
       "ruckusSCGClusterLeaderChangedTrap": ruckusSCGClusterLeaderChangedTrap,
       "ruckusSCGClusterUpgradeSuccessTrap": ruckusSCGClusterUpgradeSuccessTrap,
       "ruckusSCGNodeBondInterfaceUpTrap": ruckusSCGNodeBondInterfaceUpTrap,
       "ruckusSCGNodePhyInterfaceUpTrap": ruckusSCGNodePhyInterfaceUpTrap,
       "ruckusSCGClusterBackToInServiceTrap": ruckusSCGClusterBackToInServiceTrap,
       "ruckusSCGBackupClusterSuccessTrap": ruckusSCGBackupClusterSuccessTrap,
       "ruckusSCGNodeJoinSuccessTrap": ruckusSCGNodeJoinSuccessTrap,
       "ruckusSCGClusterAppStartTrap": ruckusSCGClusterAppStartTrap,
       "ruckusSCGNodeRemoveSuccessTrap": ruckusSCGNodeRemoveSuccessTrap,
       "ruckusSCGClusterRestoreSuccessTrap": ruckusSCGClusterRestoreSuccessTrap,
       "ruckusSCGNodeBackToInServiceTrap": ruckusSCGNodeBackToInServiceTrap,
       "ruckusSCGSshTunnelSwitchedTrap": ruckusSCGSshTunnelSwitchedTrap,
       "ruckusSCGClusterCfgBackupStartTrap": ruckusSCGClusterCfgBackupStartTrap,
       "ruckusSCGClusterCfgBackupSuccessTrap": ruckusSCGClusterCfgBackupSuccessTrap,
       "ruckusSCGClusterCfgBackupFailedTrap": ruckusSCGClusterCfgBackupFailedTrap,
       "ruckusSCGClusterCfgRestoreSuccessTrap": ruckusSCGClusterCfgRestoreSuccessTrap,
       "ruckusSCGClusterCfgRestoreFailedTrap": ruckusSCGClusterCfgRestoreFailedTrap,
       "ruckusSCGClusterUploadSuccessTrap": ruckusSCGClusterUploadSuccessTrap,
       "ruckusSCGClusterUploadFailedTrap": ruckusSCGClusterUploadFailedTrap,
       "ruckusSCGClusterOutOfServiceTrap": ruckusSCGClusterOutOfServiceTrap,
       "ruckusSCGClusterUploadVDPFirmwareStartTrap": ruckusSCGClusterUploadVDPFirmwareStartTrap,
       "ruckusSCGClusterUploadVDPFirmwareSuccessTrap": ruckusSCGClusterUploadVDPFirmwareSuccessTrap,
       "ruckusSCGClusterUploadVDPFirmwareFailedTrap": ruckusSCGClusterUploadVDPFirmwareFailedTrap,
       "ruckusSCGIpmiVotageTrap": ruckusSCGIpmiVotageTrap,
       "ruckusSCGIpmiTempBBTrap": ruckusSCGIpmiTempBBTrap,
       "ruckusSCGIpmiTempFPTrap": ruckusSCGIpmiTempFPTrap,
       "ruckusSCGIpmiTempIOHTrap": ruckusSCGIpmiTempIOHTrap,
       "ruckusSCGIpmiTempMemPTrap": ruckusSCGIpmiTempMemPTrap,
       "ruckusSCGIpmiTempPSTrap": ruckusSCGIpmiTempPSTrap,
       "ruckusSCGIpmiTempPTrap": ruckusSCGIpmiTempPTrap,
       "ruckusSCGIpmiTempHSBPTrap": ruckusSCGIpmiTempHSBPTrap,
       "ruckusSCGIpmiFanTrap": ruckusSCGIpmiFanTrap,
       "ruckusSCGIpmiPowerTrap": ruckusSCGIpmiPowerTrap,
       "ruckusSCGIpmiCurrentTrap": ruckusSCGIpmiCurrentTrap,
       "ruckusSCGIpmiFanStatusTrap": ruckusSCGIpmiFanStatusTrap,
       "ruckusSCGIpmiPsStatusTrap": ruckusSCGIpmiPsStatusTrap,
       "ruckusSCGIpmiDrvStatusTrap": ruckusSCGIpmiDrvStatusTrap,
       "ruckusSCGIpmiREVotageTrap": ruckusSCGIpmiREVotageTrap,
       "ruckusSCGIpmiRETempBBTrap": ruckusSCGIpmiRETempBBTrap,
       "ruckusSCGIpmiRETempFPTrap": ruckusSCGIpmiRETempFPTrap,
       "ruckusSCGIpmiRETempIOHTrap": ruckusSCGIpmiRETempIOHTrap,
       "ruckusSCGIpmiRETempMemPTrap": ruckusSCGIpmiRETempMemPTrap,
       "ruckusSCGIpmiRETempPSTrap": ruckusSCGIpmiRETempPSTrap,
       "ruckusSCGIpmiRETempPTrap": ruckusSCGIpmiRETempPTrap,
       "ruckusSCGIpmiRETempHSBPTrap": ruckusSCGIpmiRETempHSBPTrap,
       "ruckusSCGIpmiREFanTrap": ruckusSCGIpmiREFanTrap,
       "ruckusSCGIpmiREPowerTrap": ruckusSCGIpmiREPowerTrap,
       "ruckusSCGIpmiRECurrentTrap": ruckusSCGIpmiRECurrentTrap,
       "ruckusSCGIpmiREFanStatusTrap": ruckusSCGIpmiREFanStatusTrap,
       "ruckusSCGIpmiREPsStatusTrap": ruckusSCGIpmiREPsStatusTrap,
       "ruckusSCGIpmiREDrvStatusTrap": ruckusSCGIpmiREDrvStatusTrap,
       "ruckusSCGFtpTransferErrorTrap": ruckusSCGFtpTransferErrorTrap,
       "ruckusSCGSystemLBSConnectSuccessTrap": ruckusSCGSystemLBSConnectSuccessTrap,
       "ruckusSCGSystemLBSNoResponseTrap": ruckusSCGSystemLBSNoResponseTrap,
       "ruckusSCGSystemLBSAuthFailedTrap": ruckusSCGSystemLBSAuthFailedTrap,
       "ruckusSCGSystemLBSConnectFailedTrap": ruckusSCGSystemLBSConnectFailedTrap,
       "ruckusSCGProcessRestartTrap": ruckusSCGProcessRestartTrap,
       "ruckusSCGServiceUnavailableTrap": ruckusSCGServiceUnavailableTrap,
       "ruckusSCGKeepAliveFailureTrap": ruckusSCGKeepAliveFailureTrap,
       "ruckusSCGResourceUnavailableTrap": ruckusSCGResourceUnavailableTrap,
       "ruckusSCGSmfRegFailedTrap": ruckusSCGSmfRegFailedTrap,
       "ruckusSCGHipFailoverTrap": ruckusSCGHipFailoverTrap,
       "ruckusSCGConfUpdFailedTrap": ruckusSCGConfUpdFailedTrap,
       "ruckusSCGConfRcvFailedTrap": ruckusSCGConfRcvFailedTrap,
       "ruckusSCGLostCnxnToDbladeTrap": ruckusSCGLostCnxnToDbladeTrap,
       "ruckusSCGGgsnRestartedTrap": ruckusSCGGgsnRestartedTrap,
       "ruckusSCGGgsnNotReachableTrap": ruckusSCGGgsnNotReachableTrap,
       "ruckusSCGGgsnNotResolvedTrap": ruckusSCGGgsnNotResolvedTrap,
       "ruckusSCGUnknownUETrap": ruckusSCGUnknownUETrap,
       "ruckusSCGAuthSrvrNotReachableTrap": ruckusSCGAuthSrvrNotReachableTrap,
       "ruckusSCGAccSrvrNotReachableTrap": ruckusSCGAccSrvrNotReachableTrap,
       "ruckusSCGUnknownRealmTrap": ruckusSCGUnknownRealmTrap,
       "ruckusSCGAuthFailedNonPermanentIDTrap": ruckusSCGAuthFailedNonPermanentIDTrap,
       "ruckusSCGCnxnToCgfFailedTrap": ruckusSCGCnxnToCgfFailedTrap,
       "ruckusSCGCdrTransferFailedTrap": ruckusSCGCdrTransferFailedTrap,
       "ruckusSCGCdrGenerateFailedTrap": ruckusSCGCdrGenerateFailedTrap,
       "ruckusSCGDestNotRecheableTrap": ruckusSCGDestNotRecheableTrap,
       "ruckusSCGAppServerDownTrap": ruckusSCGAppServerDownTrap,
       "ruckusSCGAppServerInactiveTrap": ruckusSCGAppServerInactiveTrap,
       "ruckusSCGAssocCantStartTrap": ruckusSCGAssocCantStartTrap,
       "ruckusSCGAssocDownTrap": ruckusSCGAssocDownTrap,
       "ruckusSCGOutboundRoutingFailedTrap": ruckusSCGOutboundRoutingFailedTrap,
       "ruckusSCGDidAllocationFailureTrap": ruckusSCGDidAllocationFailureTrap,
       "ruckusSCGPdnGwUnresolvedTrap": ruckusSCGPdnGwUnresolvedTrap,
       "ruckusSCGPdnGwVersionUnsupportedTrap": ruckusSCGPdnGwVersionUnsupportedTrap,
       "ruckusSCGPdnGwAssociationDownTrap": ruckusSCGPdnGwAssociationDownTrap,
       "ruckusSCGCreateSessionResponseFailedTrap": ruckusSCGCreateSessionResponseFailedTrap,
       "ruckusSCGDecodeFailedTrap": ruckusSCGDecodeFailedTrap,
       "ruckusSCGModifyBearerResponseFailedTrap": ruckusSCGModifyBearerResponseFailedTrap,
       "ruckusSCGDeleteSessionResponseFailedTrap": ruckusSCGDeleteSessionResponseFailedTrap,
       "ruckusSCGDeleteBearerRequestFailedTrap": ruckusSCGDeleteBearerRequestFailedTrap,
       "ruckusSCGUpdateBearerRequestFailedTrap": ruckusSCGUpdateBearerRequestFailedTrap,
       "ruckusSCGCgfServerNotConfiguredTrap": ruckusSCGCgfServerNotConfiguredTrap,
       "ruckusSCGTtgSessionCriticalThresholdTrap": ruckusSCGTtgSessionCriticalThresholdTrap,
       "ruckusSCGTtgSessionLicenseInsufficientTrap": ruckusSCGTtgSessionLicenseInsufficientTrap,
       "ruckusSCGAPAcctMsgMandatoryPrmMissingTrap": ruckusSCGAPAcctMsgMandatoryPrmMissingTrap,
       "ruckusSCGAcctUnknownRealmTrap": ruckusSCGAcctUnknownRealmTrap,
       "ruckusSCGAPAcctMsgDecodeFailedTrap": ruckusSCGAPAcctMsgDecodeFailedTrap,
       "ruckusSCGAPAcctRespWhileInvalidConfigTrap": ruckusSCGAPAcctRespWhileInvalidConfigTrap,
       "ruckusSCGAPAcctMsgDropNoAcctStartMsgTrap": ruckusSCGAPAcctMsgDropNoAcctStartMsgTrap,
       "ruckusSCGUnauthorizedCoaDmMessageDroppedTrap": ruckusSCGUnauthorizedCoaDmMessageDroppedTrap,
       "ruckusSCGConnectedToDbladeTrap": ruckusSCGConnectedToDbladeTrap,
       "ruckusSCGDestAvailableTrap": ruckusSCGDestAvailableTrap,
       "ruckusSCGAppServerActiveTrap": ruckusSCGAppServerActiveTrap,
       "ruckusSCGAssocUpTrap": ruckusSCGAssocUpTrap,
       "ruckusSCGSessUpdatedAtDbladeTrap": ruckusSCGSessUpdatedAtDbladeTrap,
       "ruckusSCGSessUpdateErrAtDbladeTrap": ruckusSCGSessUpdateErrAtDbladeTrap,
       "ruckusSCGSessDeletedAtDbladeTrap": ruckusSCGSessDeletedAtDbladeTrap,
       "ruckusSCGSessDeleteErrAtDbladeTrap": ruckusSCGSessDeleteErrAtDbladeTrap,
       "ruckusSCGLicenseSyncSuccessTrap": ruckusSCGLicenseSyncSuccessTrap,
       "ruckusSCGLicenseSyncFailedTrap": ruckusSCGLicenseSyncFailedTrap,
       "ruckusSCGLicenseImportSuccessTrap": ruckusSCGLicenseImportSuccessTrap,
       "ruckusSCGLicenseImportFailedTrap": ruckusSCGLicenseImportFailedTrap,
       "ruckusSCGSyslogServerReachableTrap": ruckusSCGSyslogServerReachableTrap,
       "ruckusSCGSyslogServerUnreachableTrap": ruckusSCGSyslogServerUnreachableTrap,
       "ruckusSCGSyslogServerSwitchedTrap": ruckusSCGSyslogServerSwitchedTrap,
       "ruckusSCGAPRadiusServerReachableTrap": ruckusSCGAPRadiusServerReachableTrap,
       "ruckusSCGAPRadiusServerUnreachableTrap": ruckusSCGAPRadiusServerUnreachableTrap,
       "ruckusSCGAPLDAPServerReachableTrap": ruckusSCGAPLDAPServerReachableTrap,
       "ruckusSCGAPLDAPServerUnreachableTrap": ruckusSCGAPLDAPServerUnreachableTrap,
       "ruckusSCGAPADServerReachableTrap": ruckusSCGAPADServerReachableTrap,
       "ruckusSCGAPADServerUnreachableTrap": ruckusSCGAPADServerUnreachableTrap,
       "ruckusSCGAPUsbSoftwarePackageDownloadedTrap": ruckusSCGAPUsbSoftwarePackageDownloadedTrap,
       "ruckusSCGAPUsbSoftwarePackageDownloadFailedTrap": ruckusSCGAPUsbSoftwarePackageDownloadFailedTrap,
       "ruckusSCGEspAuthServerReachableTrap": ruckusSCGEspAuthServerReachableTrap,
       "ruckusSCGEspAuthServerUnreachableTrap": ruckusSCGEspAuthServerUnreachableTrap,
       "ruckusSCGEspAuthServerResolvableTrap": ruckusSCGEspAuthServerResolvableTrap,
       "ruckusSCGEspAuthServerUnResolvableTrap": ruckusSCGEspAuthServerUnResolvableTrap,
       "ruckusSCGEspDNATServerReachableTrap": ruckusSCGEspDNATServerReachableTrap,
       "ruckusSCGEspDNATServerUnreachableTrap": ruckusSCGEspDNATServerUnreachableTrap,
       "ruckusSCGEspDNATServerResolvableTrap": ruckusSCGEspDNATServerResolvableTrap,
       "ruckusSCGEspDNATServerUnresolvableTrap": ruckusSCGEspDNATServerUnresolvableTrap,
       "ruckusRateLimitTORSurpassedTrap": ruckusRateLimitTORSurpassedTrap,
       "ruckusSCGIPSecTunnelAssociatedTrap": ruckusSCGIPSecTunnelAssociatedTrap,
       "ruckusSCGIPSecTunnelDisassociatedTrap": ruckusSCGIPSecTunnelDisassociatedTrap,
       "ruckusSCGIPSecTunnelAssociateFailedTrap": ruckusSCGIPSecTunnelAssociateFailedTrap,
       "ruckusSCGPmipProcessInitTrap": ruckusSCGPmipProcessInitTrap,
       "ruckusSCGPmipUnavailableTrap": ruckusSCGPmipUnavailableTrap,
       "ruckusSCGPmipUnallocatedMemoryTrap": ruckusSCGPmipUnallocatedMemoryTrap,
       "ruckusSCGPmipUpdateCgfFailedTrap": ruckusSCGPmipUpdateCgfFailedTrap,
       "ruckusSCGPmipLMAIcmpUnreachableTrap": ruckusSCGPmipLMAIcmpUnreachableTrap,
       "ruckusSCGPmipLMAFailOverTrap": ruckusSCGPmipLMAFailOverTrap,
       "ruckusSCGPmipBindingFailureTrap": ruckusSCGPmipBindingFailureTrap,
       "ruckusSCGPmiplostCnxnToDHCPTrap": ruckusSCGPmiplostCnxnToDHCPTrap,
       "ruckusSCGPmipLMAIcmpReachableTrap": ruckusSCGPmipLMAIcmpReachableTrap,
       "ruckusSCGPmipBindingSuccessTrap": ruckusSCGPmipBindingSuccessTrap,
       "ruckusSCGPmipConnectedToDHCPTrap": ruckusSCGPmipConnectedToDHCPTrap,
       "ruckusSCGPmipProcessStoppedTrap": ruckusSCGPmipProcessStoppedTrap,
       "ruckusSCGEventObjects": ruckusSCGEventObjects,
       "ruckusSCGEventDescription": ruckusSCGEventDescription,
       "ruckusSCGClusterName": ruckusSCGClusterName,
       "ruckusSCGEventCode": ruckusSCGEventCode,
       "ruckusSCGProcessName": ruckusSCGProcessName,
       "ruckusSCGEventCtrlIP": ruckusSCGEventCtrlIP,
       "ruckusSCGEventSeverity": ruckusSCGEventSeverity,
       "ruckusSCGEventType": ruckusSCGEventType,
       "ruckusSCGEventNodeMgmtIp": ruckusSCGEventNodeMgmtIp,
       "ruckusSCGEventNodeName": ruckusSCGEventNodeName,
       "ruckusSCGCPUPerc": ruckusSCGCPUPerc,
       "ruckusSCGMemoryPerc": ruckusSCGMemoryPerc,
       "ruckusSCGDiskPerc": ruckusSCGDiskPerc,
       "ruckusSCGEventMacAddr": ruckusSCGEventMacAddr,
       "ruckusSCGEventFirmwareVersion": ruckusSCGEventFirmwareVersion,
       "ruckusSCGEventUpgradedFirmwareVersion": ruckusSCGEventUpgradedFirmwareVersion,
       "ruckusSCGEventAPMacAddr": ruckusSCGEventAPMacAddr,
       "ruckusSCGEventReason": ruckusSCGEventReason,
       "ruckusSCGEventAPName": ruckusSCGEventAPName,
       "ruckusSCGEventAPIP": ruckusSCGEventAPIP,
       "ruckusSCGEventAPLocation": ruckusSCGEventAPLocation,
       "ruckusSCGEventAPGPSCoordinates": ruckusSCGEventAPGPSCoordinates,
       "ruckusSCGEventAPDescription": ruckusSCGEventAPDescription,
       "ruckusSCGEventZoneName": ruckusSCGEventZoneName,
       "ruckusSCGAPModel": ruckusSCGAPModel,
       "ruckusSCGConfigAPModel": ruckusSCGConfigAPModel,
       "ruckusSCGAPConfigID": ruckusSCGAPConfigID,
       "ruckusSCGEventTargetZoneName": ruckusSCGEventTargetZoneName,
       "ruckusSCGEventAPIPv6": ruckusSCGEventAPIPv6,
       "ruckusSCGLBSURL": ruckusSCGLBSURL,
       "ruckusSCGLBSPort": ruckusSCGLBSPort,
       "ruckusSCGEventSSID": ruckusSCGEventSSID,
       "ruckusSCGEventRogueMac": ruckusSCGEventRogueMac,
       "ruckusPrimaryGRE": ruckusPrimaryGRE,
       "ruckusSecondaryGRE": ruckusSecondaryGRE,
       "ruckusSoftGREGatewayList": ruckusSoftGREGatewayList,
       "ruckusSCGSoftGREGWAddress": ruckusSCGSoftGREGWAddress,
       "ruckusSCGEventClientMacAddr": ruckusSCGEventClientMacAddr,
       "ruckusSCGDPKey": ruckusSCGDPKey,
       "ruckusSCGDPConfigID": ruckusSCGDPConfigID,
       "ruckusSCGDPIP": ruckusSCGDPIP,
       "ruckusSCGDPPacketPoolID": ruckusSCGDPPacketPoolID,
       "ruckusSCGNetworkPortID": ruckusSCGNetworkPortID,
       "ruckusSCGNetworkInterface": ruckusSCGNetworkInterface,
       "ruckusSCGSwitchStatus": ruckusSCGSwitchStatus,
       "ruckusSCGTemperatureStatus": ruckusSCGTemperatureStatus,
       "ruckusSCGProcessorId": ruckusSCGProcessorId,
       "ruckusSCGFanId": ruckusSCGFanId,
       "ruckusSCGFanStatus": ruckusSCGFanStatus,
       "ruckusSCGPsId": ruckusSCGPsId,
       "ruckusSCGPsStatus": ruckusSCGPsStatus,
       "ruckusSCGDrvId": ruckusSCGDrvId,
       "ruckusSCGDrvStatus": ruckusSCGDrvStatus,
       "ruckusSCGLicenseType": ruckusSCGLicenseType,
       "ruckusSCGLicenseUsagePerc": ruckusSCGLicenseUsagePerc,
       "ruckusSCGLicenseServerName": ruckusSCGLicenseServerName,
       "ruckusSCGIPSecGWAddress": ruckusSCGIPSecGWAddress,
       "ruckusSCGSyslogServerAddress": ruckusSCGSyslogServerAddress,
       "ruckusSCGSrcSyslogServerAddress": ruckusSCGSrcSyslogServerAddress,
       "ruckusSCGDestSyslogServerAddress": ruckusSCGDestSyslogServerAddress,
       "ruckusSCGFtpIp": ruckusSCGFtpIp,
       "ruckusSCGFtpPort": ruckusSCGFtpPort,
       "ruckusSCGSrcProcess": ruckusSCGSrcProcess,
       "ruckusSCGGgsnIp": ruckusSCGGgsnIp,
       "ruckusSCGGtpcIp": ruckusSCGGtpcIp,
       "ruckusSCGApn": ruckusSCGApn,
       "ruckusSCGUEImsi": ruckusSCGUEImsi,
       "ruckusSCGUEMsisdn": ruckusSCGUEMsisdn,
       "ruckusSCGAuthSrvrIp": ruckusSCGAuthSrvrIp,
       "ruckusSCGRadProxyIp": ruckusSCGRadProxyIp,
       "ruckusSCGAccSrvrIp": ruckusSCGAccSrvrIp,
       "ruckusSCGRealm": ruckusSCGRealm,
       "ruckusSCGCgfSrvrIp": ruckusSCGCgfSrvrIp,
       "ruckusSCGRadSrvrIp": ruckusSCGRadSrvrIp,
       "ruckusSCGCipIp": ruckusSCGCipIp,
       "ruckusSCGPointCode": ruckusSCGPointCode,
       "ruckusSCGCongLevel": ruckusSCGCongLevel,
       "ruckusSCGSSN": ruckusSCGSSN,
       "ruckusSCGRoutingContext": ruckusSCGRoutingContext,
       "ruckusSCGSrcIP": ruckusSCGSrcIP,
       "ruckusSCGSrcPort": ruckusSCGSrcPort,
       "ruckusSCGDestIP": ruckusSCGDestIP,
       "ruckusSCGDestPort": ruckusSCGDestPort,
       "ruckusSCGOperation": ruckusSCGOperation,
       "ruckusSCGHlrInstance": ruckusSCGHlrInstance,
       "ruckusSCGUserName": ruckusSCGUserName,
       "ruckusSCGPgwIp": ruckusSCGPgwIp,
       "ruckusSCGFileName": ruckusSCGFileName,
       "ruckusSCGLDAPSrvrIp": ruckusSCGLDAPSrvrIp,
       "ruckusSCGADSrvrIp": ruckusSCGADSrvrIp,
       "ruckusSCGSoftwareName": ruckusSCGSoftwareName,
       "ruckusSCGDomainName": ruckusSCGDomainName,
       "ruckusSCGDNATIp": ruckusSCGDNATIp,
       "ruckusSCGLMAIp": ruckusSCGLMAIp,
       "ruckusSCGEventRoguePolicyName": ruckusSCGEventRoguePolicyName,
       "ruckusSCGEventRogueRuleName": ruckusSCGEventRogueRuleName,
       "ruckusSCGEventRogueType": ruckusSCGEventRogueType}
)
