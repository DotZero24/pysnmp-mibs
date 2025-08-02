_J='cfprDcxVifEpInstanceId'
_I='cfprDcxVcInstanceId'
_H='cfprDcxVIfInstanceId'
_G='cfprDcxUniverseInstanceId'
_F='cfprDcxNsInstanceId'
_E='cfprDcxFcoeVifEpInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-DCX-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprAdaptorLinkState,CfprAdaptorServiceState,CfprDcxAdminState,CfprDcxNsAllocStatus,CfprDcxOperState,CfprDcxProtState,CfprDcxState,CfprDcxVIfProtRole,CfprDpsecForgedTransmit,CfprFabricTrafficDirection,CfprFsmLifecycle,CfprNetworkConnectionType,CfprNetworkLocale,CfprNetworkPortRole,CfprNetworkPortType,CfprNetworkSide,CfprNetworkSwitchId,CfprNetworkTransport,CfprNwctrlAdminState,CfprNwctrlLinkFailAction,CfprNwctrlRegistrationMode,CfprQosHostControl,CfprVnicInstantiation=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprAdaptorLinkState','CfprAdaptorServiceState','CfprDcxAdminState','CfprDcxNsAllocStatus','CfprDcxOperState','CfprDcxProtState','CfprDcxState','CfprDcxVIfProtRole','CfprDpsecForgedTransmit','CfprFabricTrafficDirection','CfprFsmLifecycle','CfprNetworkConnectionType','CfprNetworkLocale','CfprNetworkPortRole','CfprNetworkPortType','CfprNetworkSide','CfprNetworkSwitchId','CfprNetworkTransport','CfprNwctrlAdminState','CfprNwctrlLinkFailAction','CfprNwctrlRegistrationMode','CfprQosHostControl','CfprVnicInstantiation')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprDcxObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,14))
_CfprDcxFcoeVifEpTable_Object=MibTable
cfprDcxFcoeVifEpTable=_CfprDcxFcoeVifEpTable_Object((1,3,6,1,4,1,9,9,826,1,14,1))
if mibBuilder.loadTexts:cfprDcxFcoeVifEpTable.setStatus(_A)
_CfprDcxFcoeVifEpEntry_Object=MibTableRow
cfprDcxFcoeVifEpEntry=_CfprDcxFcoeVifEpEntry_Object((1,3,6,1,4,1,9,9,826,1,14,1,1))
cfprDcxFcoeVifEpEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprDcxFcoeVifEpEntry.setStatus(_A)
_CfprDcxFcoeVifEpInstanceId_Type=CfprManagedObjectId
_CfprDcxFcoeVifEpInstanceId_Object=MibTableColumn
cfprDcxFcoeVifEpInstanceId=_CfprDcxFcoeVifEpInstanceId_Object((1,3,6,1,4,1,9,9,826,1,14,1,1,1),_CfprDcxFcoeVifEpInstanceId_Type())
cfprDcxFcoeVifEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprDcxFcoeVifEpInstanceId.setStatus(_A)
_CfprDcxFcoeVifEpDn_Type=CfprManagedObjectDn
_CfprDcxFcoeVifEpDn_Object=MibTableColumn
cfprDcxFcoeVifEpDn=_CfprDcxFcoeVifEpDn_Object((1,3,6,1,4,1,9,9,826,1,14,1,1,2),_CfprDcxFcoeVifEpDn_Type())
cfprDcxFcoeVifEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxFcoeVifEpDn.setStatus(_A)
_CfprDcxFcoeVifEpRn_Type=SnmpAdminString
_CfprDcxFcoeVifEpRn_Object=MibTableColumn
cfprDcxFcoeVifEpRn=_CfprDcxFcoeVifEpRn_Object((1,3,6,1,4,1,9,9,826,1,14,1,1,3),_CfprDcxFcoeVifEpRn_Type())
cfprDcxFcoeVifEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxFcoeVifEpRn.setStatus(_A)
_CfprDcxFcoeVifEpId_Type=Gauge32
_CfprDcxFcoeVifEpId_Object=MibTableColumn
cfprDcxFcoeVifEpId=_CfprDcxFcoeVifEpId_Object((1,3,6,1,4,1,9,9,826,1,14,1,1,4),_CfprDcxFcoeVifEpId_Type())
cfprDcxFcoeVifEpId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxFcoeVifEpId.setStatus(_A)
_CfprDcxNsTable_Object=MibTable
cfprDcxNsTable=_CfprDcxNsTable_Object((1,3,6,1,4,1,9,9,826,1,14,2))
if mibBuilder.loadTexts:cfprDcxNsTable.setStatus(_A)
_CfprDcxNsEntry_Object=MibTableRow
cfprDcxNsEntry=_CfprDcxNsEntry_Object((1,3,6,1,4,1,9,9,826,1,14,2,1))
cfprDcxNsEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprDcxNsEntry.setStatus(_A)
_CfprDcxNsInstanceId_Type=CfprManagedObjectId
_CfprDcxNsInstanceId_Object=MibTableColumn
cfprDcxNsInstanceId=_CfprDcxNsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,14,2,1,1),_CfprDcxNsInstanceId_Type())
cfprDcxNsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprDcxNsInstanceId.setStatus(_A)
_CfprDcxNsDn_Type=CfprManagedObjectDn
_CfprDcxNsDn_Object=MibTableColumn
cfprDcxNsDn=_CfprDcxNsDn_Object((1,3,6,1,4,1,9,9,826,1,14,2,1,2),_CfprDcxNsDn_Type())
cfprDcxNsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxNsDn.setStatus(_A)
_CfprDcxNsRn_Type=SnmpAdminString
_CfprDcxNsRn_Object=MibTableColumn
cfprDcxNsRn=_CfprDcxNsRn_Object((1,3,6,1,4,1,9,9,826,1,14,2,1,3),_CfprDcxNsRn_Type())
cfprDcxNsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxNsRn.setStatus(_A)
_CfprDcxNsAllocStatus_Type=CfprDcxNsAllocStatus
_CfprDcxNsAllocStatus_Object=MibTableColumn
cfprDcxNsAllocStatus=_CfprDcxNsAllocStatus_Object((1,3,6,1,4,1,9,9,826,1,14,2,1,4),_CfprDcxNsAllocStatus_Type())
cfprDcxNsAllocStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxNsAllocStatus.setStatus(_A)
_CfprDcxNsSide_Type=CfprNetworkSide
_CfprDcxNsSide_Object=MibTableColumn
cfprDcxNsSide=_CfprDcxNsSide_Object((1,3,6,1,4,1,9,9,826,1,14,2,1,5),_CfprDcxNsSide_Type())
cfprDcxNsSide.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxNsSide.setStatus(_A)
_CfprDcxNsSize_Type=Gauge32
_CfprDcxNsSize_Object=MibTableColumn
cfprDcxNsSize=_CfprDcxNsSize_Object((1,3,6,1,4,1,9,9,826,1,14,2,1,6),_CfprDcxNsSize_Type())
cfprDcxNsSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxNsSize.setStatus(_A)
_CfprDcxNsSwitchId_Type=CfprNetworkSwitchId
_CfprDcxNsSwitchId_Object=MibTableColumn
cfprDcxNsSwitchId=_CfprDcxNsSwitchId_Object((1,3,6,1,4,1,9,9,826,1,14,2,1,7),_CfprDcxNsSwitchId_Type())
cfprDcxNsSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxNsSwitchId.setStatus(_A)
_CfprDcxNsUsed_Type=Gauge32
_CfprDcxNsUsed_Object=MibTableColumn
cfprDcxNsUsed=_CfprDcxNsUsed_Object((1,3,6,1,4,1,9,9,826,1,14,2,1,8),_CfprDcxNsUsed_Type())
cfprDcxNsUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxNsUsed.setStatus(_A)
_CfprDcxUniverseTable_Object=MibTable
cfprDcxUniverseTable=_CfprDcxUniverseTable_Object((1,3,6,1,4,1,9,9,826,1,14,3))
if mibBuilder.loadTexts:cfprDcxUniverseTable.setStatus(_A)
_CfprDcxUniverseEntry_Object=MibTableRow
cfprDcxUniverseEntry=_CfprDcxUniverseEntry_Object((1,3,6,1,4,1,9,9,826,1,14,3,1))
cfprDcxUniverseEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprDcxUniverseEntry.setStatus(_A)
_CfprDcxUniverseInstanceId_Type=CfprManagedObjectId
_CfprDcxUniverseInstanceId_Object=MibTableColumn
cfprDcxUniverseInstanceId=_CfprDcxUniverseInstanceId_Object((1,3,6,1,4,1,9,9,826,1,14,3,1,1),_CfprDcxUniverseInstanceId_Type())
cfprDcxUniverseInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprDcxUniverseInstanceId.setStatus(_A)
_CfprDcxUniverseDn_Type=CfprManagedObjectDn
_CfprDcxUniverseDn_Object=MibTableColumn
cfprDcxUniverseDn=_CfprDcxUniverseDn_Object((1,3,6,1,4,1,9,9,826,1,14,3,1,2),_CfprDcxUniverseDn_Type())
cfprDcxUniverseDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxUniverseDn.setStatus(_A)
_CfprDcxUniverseRn_Type=SnmpAdminString
_CfprDcxUniverseRn_Object=MibTableColumn
cfprDcxUniverseRn=_CfprDcxUniverseRn_Object((1,3,6,1,4,1,9,9,826,1,14,3,1,3),_CfprDcxUniverseRn_Type())
cfprDcxUniverseRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxUniverseRn.setStatus(_A)
_CfprDcxVIfTable_Object=MibTable
cfprDcxVIfTable=_CfprDcxVIfTable_Object((1,3,6,1,4,1,9,9,826,1,14,4))
if mibBuilder.loadTexts:cfprDcxVIfTable.setStatus(_A)
_CfprDcxVIfEntry_Object=MibTableRow
cfprDcxVIfEntry=_CfprDcxVIfEntry_Object((1,3,6,1,4,1,9,9,826,1,14,4,1))
cfprDcxVIfEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprDcxVIfEntry.setStatus(_A)
_CfprDcxVIfInstanceId_Type=CfprManagedObjectId
_CfprDcxVIfInstanceId_Object=MibTableColumn
cfprDcxVIfInstanceId=_CfprDcxVIfInstanceId_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,1),_CfprDcxVIfInstanceId_Type())
cfprDcxVIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprDcxVIfInstanceId.setStatus(_A)
_CfprDcxVIfDn_Type=CfprManagedObjectDn
_CfprDcxVIfDn_Object=MibTableColumn
cfprDcxVIfDn=_CfprDcxVIfDn_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,2),_CfprDcxVIfDn_Type())
cfprDcxVIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfDn.setStatus(_A)
_CfprDcxVIfRn_Type=SnmpAdminString
_CfprDcxVIfRn_Object=MibTableColumn
cfprDcxVIfRn=_CfprDcxVIfRn_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,3),_CfprDcxVIfRn_Type())
cfprDcxVIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfRn.setStatus(_A)
_CfprDcxVIfAdminState_Type=CfprDcxAdminState
_CfprDcxVIfAdminState_Object=MibTableColumn
cfprDcxVIfAdminState=_CfprDcxVIfAdminState_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,4),_CfprDcxVIfAdminState_Type())
cfprDcxVIfAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfAdminState.setStatus(_A)
_CfprDcxVIfCookie_Type=Unsigned64
_CfprDcxVIfCookie_Object=MibTableColumn
cfprDcxVIfCookie=_CfprDcxVIfCookie_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,5),_CfprDcxVIfCookie_Type())
cfprDcxVIfCookie.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfCookie.setStatus(_A)
_CfprDcxVIfEpDn_Type=SnmpAdminString
_CfprDcxVIfEpDn_Object=MibTableColumn
cfprDcxVIfEpDn=_CfprDcxVIfEpDn_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,6),_CfprDcxVIfEpDn_Type())
cfprDcxVIfEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfEpDn.setStatus(_A)
_CfprDcxVIfId_Type=Gauge32
_CfprDcxVIfId_Object=MibTableColumn
cfprDcxVIfId=_CfprDcxVIfId_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,7),_CfprDcxVIfId_Type())
cfprDcxVIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfId.setStatus(_A)
_CfprDcxVIfIfRole_Type=CfprNetworkPortRole
_CfprDcxVIfIfRole_Object=MibTableColumn
cfprDcxVIfIfRole=_CfprDcxVIfIfRole_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,8),_CfprDcxVIfIfRole_Type())
cfprDcxVIfIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfIfRole.setStatus(_A)
_CfprDcxVIfIfType_Type=CfprNetworkPortType
_CfprDcxVIfIfType_Object=MibTableColumn
cfprDcxVIfIfType=_CfprDcxVIfIfType_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,9),_CfprDcxVIfIfType_Type())
cfprDcxVIfIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfIfType.setStatus(_A)
_CfprDcxVIfInstType_Type=CfprVnicInstantiation
_CfprDcxVIfInstType_Object=MibTableColumn
cfprDcxVIfInstType=_CfprDcxVIfInstType_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,10),_CfprDcxVIfInstType_Type())
cfprDcxVIfInstType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfInstType.setStatus(_A)
_CfprDcxVIfLc_Type=CfprFsmLifecycle
_CfprDcxVIfLc_Object=MibTableColumn
cfprDcxVIfLc=_CfprDcxVIfLc_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,11),_CfprDcxVIfLc_Type())
cfprDcxVIfLc.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfLc.setStatus(_A)
_CfprDcxVIfLinkState_Type=CfprAdaptorLinkState
_CfprDcxVIfLinkState_Object=MibTableColumn
cfprDcxVIfLinkState=_CfprDcxVIfLinkState_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,12),_CfprDcxVIfLinkState_Type())
cfprDcxVIfLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfLinkState.setStatus(_A)
_CfprDcxVIfLocale_Type=CfprNetworkLocale
_CfprDcxVIfLocale_Object=MibTableColumn
cfprDcxVIfLocale=_CfprDcxVIfLocale_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,13),_CfprDcxVIfLocale_Type())
cfprDcxVIfLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfLocale.setStatus(_A)
_CfprDcxVIfName_Type=SnmpAdminString
_CfprDcxVIfName_Object=MibTableColumn
cfprDcxVIfName=_CfprDcxVIfName_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,14),_CfprDcxVIfName_Type())
cfprDcxVIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfName.setStatus(_A)
_CfprDcxVIfOperState_Type=CfprDcxOperState
_CfprDcxVIfOperState_Object=MibTableColumn
cfprDcxVIfOperState=_CfprDcxVIfOperState_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,15),_CfprDcxVIfOperState_Type())
cfprDcxVIfOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfOperState.setStatus(_A)
_CfprDcxVIfPeerDn_Type=SnmpAdminString
_CfprDcxVIfPeerDn_Object=MibTableColumn
cfprDcxVIfPeerDn=_CfprDcxVIfPeerDn_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,16),_CfprDcxVIfPeerDn_Type())
cfprDcxVIfPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfPeerDn.setStatus(_A)
_CfprDcxVIfProtPeerId_Type=Gauge32
_CfprDcxVIfProtPeerId_Object=MibTableColumn
cfprDcxVIfProtPeerId=_CfprDcxVIfProtPeerId_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,17),_CfprDcxVIfProtPeerId_Type())
cfprDcxVIfProtPeerId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfProtPeerId.setStatus(_A)
_CfprDcxVIfProtRole_Type=CfprDcxVIfProtRole
_CfprDcxVIfProtRole_Object=MibTableColumn
cfprDcxVIfProtRole=_CfprDcxVIfProtRole_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,18),_CfprDcxVIfProtRole_Type())
cfprDcxVIfProtRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfProtRole.setStatus(_A)
_CfprDcxVIfProtState_Type=CfprDcxProtState
_CfprDcxVIfProtState_Object=MibTableColumn
cfprDcxVIfProtState=_CfprDcxVIfProtState_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,19),_CfprDcxVIfProtState_Type())
cfprDcxVIfProtState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfProtState.setStatus(_A)
_CfprDcxVIfQosControl_Type=CfprQosHostControl
_CfprDcxVIfQosControl_Object=MibTableColumn
cfprDcxVIfQosControl=_CfprDcxVIfQosControl_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,20),_CfprDcxVIfQosControl_Type())
cfprDcxVIfQosControl.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfQosControl.setStatus(_A)
_CfprDcxVIfState_Type=CfprDcxState
_CfprDcxVIfState_Object=MibTableColumn
cfprDcxVIfState=_CfprDcxVIfState_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,21),_CfprDcxVIfState_Type())
cfprDcxVIfState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfState.setStatus(_A)
_CfprDcxVIfSwitchId_Type=CfprNetworkSwitchId
_CfprDcxVIfSwitchId_Object=MibTableColumn
cfprDcxVIfSwitchId=_CfprDcxVIfSwitchId_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,22),_CfprDcxVIfSwitchId_Type())
cfprDcxVIfSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfSwitchId.setStatus(_A)
_CfprDcxVIfTag_Type=Gauge32
_CfprDcxVIfTag_Object=MibTableColumn
cfprDcxVIfTag=_CfprDcxVIfTag_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,23),_CfprDcxVIfTag_Type())
cfprDcxVIfTag.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfTag.setStatus(_A)
_CfprDcxVIfTransport_Type=CfprNetworkTransport
_CfprDcxVIfTransport_Object=MibTableColumn
cfprDcxVIfTransport=_CfprDcxVIfTransport_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,24),_CfprDcxVIfTransport_Type())
cfprDcxVIfTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfTransport.setStatus(_A)
_CfprDcxVIfType_Type=CfprNetworkConnectionType
_CfprDcxVIfType_Object=MibTableColumn
cfprDcxVIfType=_CfprDcxVIfType_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,25),_CfprDcxVIfType_Type())
cfprDcxVIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfType.setStatus(_A)
_CfprDcxVIfServiceState_Type=CfprAdaptorServiceState
_CfprDcxVIfServiceState_Object=MibTableColumn
cfprDcxVIfServiceState=_CfprDcxVIfServiceState_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,26),_CfprDcxVIfServiceState_Type())
cfprDcxVIfServiceState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfServiceState.setStatus(_A)
_CfprDcxVIfVcAdminState_Type=CfprDcxAdminState
_CfprDcxVIfVcAdminState_Object=MibTableColumn
cfprDcxVIfVcAdminState=_CfprDcxVIfVcAdminState_Object((1,3,6,1,4,1,9,9,826,1,14,4,1,27),_CfprDcxVIfVcAdminState_Type())
cfprDcxVIfVcAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVIfVcAdminState.setStatus(_A)
_CfprDcxVcTable_Object=MibTable
cfprDcxVcTable=_CfprDcxVcTable_Object((1,3,6,1,4,1,9,9,826,1,14,5))
if mibBuilder.loadTexts:cfprDcxVcTable.setStatus(_A)
_CfprDcxVcEntry_Object=MibTableRow
cfprDcxVcEntry=_CfprDcxVcEntry_Object((1,3,6,1,4,1,9,9,826,1,14,5,1))
cfprDcxVcEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprDcxVcEntry.setStatus(_A)
_CfprDcxVcInstanceId_Type=CfprManagedObjectId
_CfprDcxVcInstanceId_Object=MibTableColumn
cfprDcxVcInstanceId=_CfprDcxVcInstanceId_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,1),_CfprDcxVcInstanceId_Type())
cfprDcxVcInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprDcxVcInstanceId.setStatus(_A)
_CfprDcxVcDn_Type=CfprManagedObjectDn
_CfprDcxVcDn_Object=MibTableColumn
cfprDcxVcDn=_CfprDcxVcDn_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,2),_CfprDcxVcDn_Type())
cfprDcxVcDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcDn.setStatus(_A)
_CfprDcxVcRn_Type=SnmpAdminString
_CfprDcxVcRn_Object=MibTableColumn
cfprDcxVcRn=_CfprDcxVcRn_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,3),_CfprDcxVcRn_Type())
cfprDcxVcRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcRn.setStatus(_A)
_CfprDcxVcAdminState_Type=CfprDcxAdminState
_CfprDcxVcAdminState_Object=MibTableColumn
cfprDcxVcAdminState=_CfprDcxVcAdminState_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,4),_CfprDcxVcAdminState_Type())
cfprDcxVcAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcAdminState.setStatus(_A)
_CfprDcxVcAllowDtagVlan_Type=TruthValue
_CfprDcxVcAllowDtagVlan_Object=MibTableColumn
cfprDcxVcAllowDtagVlan=_CfprDcxVcAllowDtagVlan_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,5),_CfprDcxVcAllowDtagVlan_Type())
cfprDcxVcAllowDtagVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcAllowDtagVlan.setStatus(_A)
_CfprDcxVcBorderAggrPortId_Type=Gauge32
_CfprDcxVcBorderAggrPortId_Object=MibTableColumn
cfprDcxVcBorderAggrPortId=_CfprDcxVcBorderAggrPortId_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,6),_CfprDcxVcBorderAggrPortId_Type())
cfprDcxVcBorderAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcBorderAggrPortId.setStatus(_A)
_CfprDcxVcBorderPortId_Type=Gauge32
_CfprDcxVcBorderPortId_Object=MibTableColumn
cfprDcxVcBorderPortId=_CfprDcxVcBorderPortId_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,7),_CfprDcxVcBorderPortId_Type())
cfprDcxVcBorderPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcBorderPortId.setStatus(_A)
_CfprDcxVcBorderSlotId_Type=Gauge32
_CfprDcxVcBorderSlotId_Object=MibTableColumn
cfprDcxVcBorderSlotId=_CfprDcxVcBorderSlotId_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,8),_CfprDcxVcBorderSlotId_Type())
cfprDcxVcBorderSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcBorderSlotId.setStatus(_A)
_CfprDcxVcBorderVfcId_Type=Gauge32
_CfprDcxVcBorderVfcId_Object=MibTableColumn
cfprDcxVcBorderVfcId=_CfprDcxVcBorderVfcId_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,9),_CfprDcxVcBorderVfcId_Type())
cfprDcxVcBorderVfcId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcBorderVfcId.setStatus(_A)
_CfprDcxVcCdp_Type=CfprNwctrlAdminState
_CfprDcxVcCdp_Object=MibTableColumn
cfprDcxVcCdp=_CfprDcxVcCdp_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,10),_CfprDcxVcCdp_Type())
cfprDcxVcCdp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcCdp.setStatus(_A)
_CfprDcxVcCookie_Type=Unsigned64
_CfprDcxVcCookie_Object=MibTableColumn
cfprDcxVcCookie=_CfprDcxVcCookie_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,11),_CfprDcxVcCookie_Type())
cfprDcxVcCookie.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcCookie.setStatus(_A)
_CfprDcxVcCos_Type=Gauge32
_CfprDcxVcCos_Object=MibTableColumn
cfprDcxVcCos=_CfprDcxVcCos_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,12),_CfprDcxVcCos_Type())
cfprDcxVcCos.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcCos.setStatus(_A)
_CfprDcxVcDerivedFromId_Type=Gauge32
_CfprDcxVcDerivedFromId_Object=MibTableColumn
cfprDcxVcDerivedFromId=_CfprDcxVcDerivedFromId_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,13),_CfprDcxVcDerivedFromId_Type())
cfprDcxVcDerivedFromId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcDerivedFromId.setStatus(_A)
_CfprDcxVcEncap_Type=Gauge32
_CfprDcxVcEncap_Object=MibTableColumn
cfprDcxVcEncap=_CfprDcxVcEncap_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,14),_CfprDcxVcEncap_Type())
cfprDcxVcEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcEncap.setStatus(_A)
_CfprDcxVcFcoeId_Type=Gauge32
_CfprDcxVcFcoeId_Object=MibTableColumn
cfprDcxVcFcoeId=_CfprDcxVcFcoeId_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,15),_CfprDcxVcFcoeId_Type())
cfprDcxVcFcoeId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcFcoeId.setStatus(_A)
_CfprDcxVcFltAggr_Type=Unsigned64
_CfprDcxVcFltAggr_Object=MibTableColumn
cfprDcxVcFltAggr=_CfprDcxVcFltAggr_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,16),_CfprDcxVcFltAggr_Type())
cfprDcxVcFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcFltAggr.setStatus(_A)
_CfprDcxVcForgeMac_Type=CfprDpsecForgedTransmit
_CfprDcxVcForgeMac_Object=MibTableColumn
cfprDcxVcForgeMac=_CfprDcxVcForgeMac_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,17),_CfprDcxVcForgeMac_Type())
cfprDcxVcForgeMac.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcForgeMac.setStatus(_A)
_CfprDcxVcId_Type=Gauge32
_CfprDcxVcId_Object=MibTableColumn
cfprDcxVcId=_CfprDcxVcId_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,18),_CfprDcxVcId_Type())
cfprDcxVcId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcId.setStatus(_A)
_CfprDcxVcInstType_Type=CfprVnicInstantiation
_CfprDcxVcInstType_Object=MibTableColumn
cfprDcxVcInstType=_CfprDcxVcInstType_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,19),_CfprDcxVcInstType_Type())
cfprDcxVcInstType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcInstType.setStatus(_A)
_CfprDcxVcLc_Type=CfprFsmLifecycle
_CfprDcxVcLc_Object=MibTableColumn
cfprDcxVcLc=_CfprDcxVcLc_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,20),_CfprDcxVcLc_Type())
cfprDcxVcLc.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcLc.setStatus(_A)
_CfprDcxVcLinkState_Type=CfprAdaptorLinkState
_CfprDcxVcLinkState_Object=MibTableColumn
cfprDcxVcLinkState=_CfprDcxVcLinkState_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,21),_CfprDcxVcLinkState_Type())
cfprDcxVcLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcLinkState.setStatus(_A)
_CfprDcxVcLocale_Type=CfprNetworkLocale
_CfprDcxVcLocale_Object=MibTableColumn
cfprDcxVcLocale=_CfprDcxVcLocale_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,22),_CfprDcxVcLocale_Type())
cfprDcxVcLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcLocale.setStatus(_A)
_CfprDcxVcMacRegisterMode_Type=CfprNwctrlRegistrationMode
_CfprDcxVcMacRegisterMode_Object=MibTableColumn
cfprDcxVcMacRegisterMode=_CfprDcxVcMacRegisterMode_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,23),_CfprDcxVcMacRegisterMode_Type())
cfprDcxVcMacRegisterMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcMacRegisterMode.setStatus(_A)
_CfprDcxVcMonTrafDir_Type=CfprFabricTrafficDirection
_CfprDcxVcMonTrafDir_Object=MibTableColumn
cfprDcxVcMonTrafDir=_CfprDcxVcMonTrafDir_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,24),_CfprDcxVcMonTrafDir_Type())
cfprDcxVcMonTrafDir.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcMonTrafDir.setStatus(_A)
_CfprDcxVcName_Type=SnmpAdminString
_CfprDcxVcName_Object=MibTableColumn
cfprDcxVcName=_CfprDcxVcName_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,25),_CfprDcxVcName_Type())
cfprDcxVcName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcName.setStatus(_A)
_CfprDcxVcOperBorderAggrPortId_Type=Gauge32
_CfprDcxVcOperBorderAggrPortId_Object=MibTableColumn
cfprDcxVcOperBorderAggrPortId=_CfprDcxVcOperBorderAggrPortId_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,26),_CfprDcxVcOperBorderAggrPortId_Type())
cfprDcxVcOperBorderAggrPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcOperBorderAggrPortId.setStatus(_A)
_CfprDcxVcOperBorderPortId_Type=Gauge32
_CfprDcxVcOperBorderPortId_Object=MibTableColumn
cfprDcxVcOperBorderPortId=_CfprDcxVcOperBorderPortId_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,27),_CfprDcxVcOperBorderPortId_Type())
cfprDcxVcOperBorderPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcOperBorderPortId.setStatus(_A)
_CfprDcxVcOperBorderSlotId_Type=Gauge32
_CfprDcxVcOperBorderSlotId_Object=MibTableColumn
cfprDcxVcOperBorderSlotId=_CfprDcxVcOperBorderSlotId_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,28),_CfprDcxVcOperBorderSlotId_Type())
cfprDcxVcOperBorderSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcOperBorderSlotId.setStatus(_A)
_CfprDcxVcOperState_Type=CfprDcxOperState
_CfprDcxVcOperState_Object=MibTableColumn
cfprDcxVcOperState=_CfprDcxVcOperState_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,29),_CfprDcxVcOperState_Type())
cfprDcxVcOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcOperState.setStatus(_A)
_CfprDcxVcPeerId_Type=Gauge32
_CfprDcxVcPeerId_Object=MibTableColumn
cfprDcxVcPeerId=_CfprDcxVcPeerId_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,30),_CfprDcxVcPeerId_Type())
cfprDcxVcPeerId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcPeerId.setStatus(_A)
_CfprDcxVcProtState_Type=CfprDcxProtState
_CfprDcxVcProtState_Object=MibTableColumn
cfprDcxVcProtState=_CfprDcxVcProtState_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,31),_CfprDcxVcProtState_Type())
cfprDcxVcProtState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcProtState.setStatus(_A)
_CfprDcxVcQosPolicyDn_Type=SnmpAdminString
_CfprDcxVcQosPolicyDn_Object=MibTableColumn
cfprDcxVcQosPolicyDn=_CfprDcxVcQosPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,32),_CfprDcxVcQosPolicyDn_Type())
cfprDcxVcQosPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcQosPolicyDn.setStatus(_A)
_CfprDcxVcQosPolicyId_Type=SnmpAdminString
_CfprDcxVcQosPolicyId_Object=MibTableColumn
cfprDcxVcQosPolicyId=_CfprDcxVcQosPolicyId_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,33),_CfprDcxVcQosPolicyId_Type())
cfprDcxVcQosPolicyId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcQosPolicyId.setStatus(_A)
_CfprDcxVcRole_Type=CfprNetworkPortRole
_CfprDcxVcRole_Object=MibTableColumn
cfprDcxVcRole=_CfprDcxVcRole_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,34),_CfprDcxVcRole_Type())
cfprDcxVcRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcRole.setStatus(_A)
_CfprDcxVcState_Type=CfprDcxState
_CfprDcxVcState_Object=MibTableColumn
cfprDcxVcState=_CfprDcxVcState_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,35),_CfprDcxVcState_Type())
cfprDcxVcState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcState.setStatus(_A)
_CfprDcxVcStateQual_Type=SnmpAdminString
_CfprDcxVcStateQual_Object=MibTableColumn
cfprDcxVcStateQual=_CfprDcxVcStateQual_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,36),_CfprDcxVcStateQual_Type())
cfprDcxVcStateQual.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcStateQual.setStatus(_A)
_CfprDcxVcSwitchId_Type=CfprNetworkSwitchId
_CfprDcxVcSwitchId_Object=MibTableColumn
cfprDcxVcSwitchId=_CfprDcxVcSwitchId_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,37),_CfprDcxVcSwitchId_Type())
cfprDcxVcSwitchId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcSwitchId.setStatus(_A)
_CfprDcxVcTag_Type=Gauge32
_CfprDcxVcTag_Object=MibTableColumn
cfprDcxVcTag=_CfprDcxVcTag_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,38),_CfprDcxVcTag_Type())
cfprDcxVcTag.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcTag.setStatus(_A)
_CfprDcxVcTransport_Type=CfprNetworkTransport
_CfprDcxVcTransport_Object=MibTableColumn
cfprDcxVcTransport=_CfprDcxVcTransport_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,39),_CfprDcxVcTransport_Type())
cfprDcxVcTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcTransport.setStatus(_A)
_CfprDcxVcType_Type=CfprNetworkConnectionType
_CfprDcxVcType_Object=MibTableColumn
cfprDcxVcType=_CfprDcxVcType_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,40),_CfprDcxVcType_Type())
cfprDcxVcType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcType.setStatus(_A)
_CfprDcxVcUplinkFailAction_Type=CfprNwctrlLinkFailAction
_CfprDcxVcUplinkFailAction_Object=MibTableColumn
cfprDcxVcUplinkFailAction=_CfprDcxVcUplinkFailAction_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,41),_CfprDcxVcUplinkFailAction_Type())
cfprDcxVcUplinkFailAction.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcUplinkFailAction.setStatus(_A)
_CfprDcxVcVnic_Type=SnmpAdminString
_CfprDcxVcVnic_Object=MibTableColumn
cfprDcxVcVnic=_CfprDcxVcVnic_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,42),_CfprDcxVcVnic_Type())
cfprDcxVcVnic.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcVnic.setStatus(_A)
_CfprDcxVcServiceState_Type=CfprAdaptorServiceState
_CfprDcxVcServiceState_Object=MibTableColumn
cfprDcxVcServiceState=_CfprDcxVcServiceState_Object((1,3,6,1,4,1,9,9,826,1,14,5,1,43),_CfprDcxVcServiceState_Type())
cfprDcxVcServiceState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVcServiceState.setStatus(_A)
_CfprDcxVifEpTable_Object=MibTable
cfprDcxVifEpTable=_CfprDcxVifEpTable_Object((1,3,6,1,4,1,9,9,826,1,14,6))
if mibBuilder.loadTexts:cfprDcxVifEpTable.setStatus(_A)
_CfprDcxVifEpEntry_Object=MibTableRow
cfprDcxVifEpEntry=_CfprDcxVifEpEntry_Object((1,3,6,1,4,1,9,9,826,1,14,6,1))
cfprDcxVifEpEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprDcxVifEpEntry.setStatus(_A)
_CfprDcxVifEpInstanceId_Type=CfprManagedObjectId
_CfprDcxVifEpInstanceId_Object=MibTableColumn
cfprDcxVifEpInstanceId=_CfprDcxVifEpInstanceId_Object((1,3,6,1,4,1,9,9,826,1,14,6,1,1),_CfprDcxVifEpInstanceId_Type())
cfprDcxVifEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprDcxVifEpInstanceId.setStatus(_A)
_CfprDcxVifEpDn_Type=CfprManagedObjectDn
_CfprDcxVifEpDn_Object=MibTableColumn
cfprDcxVifEpDn=_CfprDcxVifEpDn_Object((1,3,6,1,4,1,9,9,826,1,14,6,1,2),_CfprDcxVifEpDn_Type())
cfprDcxVifEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVifEpDn.setStatus(_A)
_CfprDcxVifEpRn_Type=SnmpAdminString
_CfprDcxVifEpRn_Object=MibTableColumn
cfprDcxVifEpRn=_CfprDcxVifEpRn_Object((1,3,6,1,4,1,9,9,826,1,14,6,1,3),_CfprDcxVifEpRn_Type())
cfprDcxVifEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVifEpRn.setStatus(_A)
_CfprDcxVifEpId_Type=Gauge32
_CfprDcxVifEpId_Object=MibTableColumn
cfprDcxVifEpId=_CfprDcxVifEpId_Object((1,3,6,1,4,1,9,9,826,1,14,6,1,4),_CfprDcxVifEpId_Type())
cfprDcxVifEpId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprDcxVifEpId.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprDcxObjects':cfprDcxObjects,'cfprDcxFcoeVifEpTable':cfprDcxFcoeVifEpTable,'cfprDcxFcoeVifEpEntry':cfprDcxFcoeVifEpEntry,_E:cfprDcxFcoeVifEpInstanceId,'cfprDcxFcoeVifEpDn':cfprDcxFcoeVifEpDn,'cfprDcxFcoeVifEpRn':cfprDcxFcoeVifEpRn,'cfprDcxFcoeVifEpId':cfprDcxFcoeVifEpId,'cfprDcxNsTable':cfprDcxNsTable,'cfprDcxNsEntry':cfprDcxNsEntry,_F:cfprDcxNsInstanceId,'cfprDcxNsDn':cfprDcxNsDn,'cfprDcxNsRn':cfprDcxNsRn,'cfprDcxNsAllocStatus':cfprDcxNsAllocStatus,'cfprDcxNsSide':cfprDcxNsSide,'cfprDcxNsSize':cfprDcxNsSize,'cfprDcxNsSwitchId':cfprDcxNsSwitchId,'cfprDcxNsUsed':cfprDcxNsUsed,'cfprDcxUniverseTable':cfprDcxUniverseTable,'cfprDcxUniverseEntry':cfprDcxUniverseEntry,_G:cfprDcxUniverseInstanceId,'cfprDcxUniverseDn':cfprDcxUniverseDn,'cfprDcxUniverseRn':cfprDcxUniverseRn,'cfprDcxVIfTable':cfprDcxVIfTable,'cfprDcxVIfEntry':cfprDcxVIfEntry,_H:cfprDcxVIfInstanceId,'cfprDcxVIfDn':cfprDcxVIfDn,'cfprDcxVIfRn':cfprDcxVIfRn,'cfprDcxVIfAdminState':cfprDcxVIfAdminState,'cfprDcxVIfCookie':cfprDcxVIfCookie,'cfprDcxVIfEpDn':cfprDcxVIfEpDn,'cfprDcxVIfId':cfprDcxVIfId,'cfprDcxVIfIfRole':cfprDcxVIfIfRole,'cfprDcxVIfIfType':cfprDcxVIfIfType,'cfprDcxVIfInstType':cfprDcxVIfInstType,'cfprDcxVIfLc':cfprDcxVIfLc,'cfprDcxVIfLinkState':cfprDcxVIfLinkState,'cfprDcxVIfLocale':cfprDcxVIfLocale,'cfprDcxVIfName':cfprDcxVIfName,'cfprDcxVIfOperState':cfprDcxVIfOperState,'cfprDcxVIfPeerDn':cfprDcxVIfPeerDn,'cfprDcxVIfProtPeerId':cfprDcxVIfProtPeerId,'cfprDcxVIfProtRole':cfprDcxVIfProtRole,'cfprDcxVIfProtState':cfprDcxVIfProtState,'cfprDcxVIfQosControl':cfprDcxVIfQosControl,'cfprDcxVIfState':cfprDcxVIfState,'cfprDcxVIfSwitchId':cfprDcxVIfSwitchId,'cfprDcxVIfTag':cfprDcxVIfTag,'cfprDcxVIfTransport':cfprDcxVIfTransport,'cfprDcxVIfType':cfprDcxVIfType,'cfprDcxVIfServiceState':cfprDcxVIfServiceState,'cfprDcxVIfVcAdminState':cfprDcxVIfVcAdminState,'cfprDcxVcTable':cfprDcxVcTable,'cfprDcxVcEntry':cfprDcxVcEntry,_I:cfprDcxVcInstanceId,'cfprDcxVcDn':cfprDcxVcDn,'cfprDcxVcRn':cfprDcxVcRn,'cfprDcxVcAdminState':cfprDcxVcAdminState,'cfprDcxVcAllowDtagVlan':cfprDcxVcAllowDtagVlan,'cfprDcxVcBorderAggrPortId':cfprDcxVcBorderAggrPortId,'cfprDcxVcBorderPortId':cfprDcxVcBorderPortId,'cfprDcxVcBorderSlotId':cfprDcxVcBorderSlotId,'cfprDcxVcBorderVfcId':cfprDcxVcBorderVfcId,'cfprDcxVcCdp':cfprDcxVcCdp,'cfprDcxVcCookie':cfprDcxVcCookie,'cfprDcxVcCos':cfprDcxVcCos,'cfprDcxVcDerivedFromId':cfprDcxVcDerivedFromId,'cfprDcxVcEncap':cfprDcxVcEncap,'cfprDcxVcFcoeId':cfprDcxVcFcoeId,'cfprDcxVcFltAggr':cfprDcxVcFltAggr,'cfprDcxVcForgeMac':cfprDcxVcForgeMac,'cfprDcxVcId':cfprDcxVcId,'cfprDcxVcInstType':cfprDcxVcInstType,'cfprDcxVcLc':cfprDcxVcLc,'cfprDcxVcLinkState':cfprDcxVcLinkState,'cfprDcxVcLocale':cfprDcxVcLocale,'cfprDcxVcMacRegisterMode':cfprDcxVcMacRegisterMode,'cfprDcxVcMonTrafDir':cfprDcxVcMonTrafDir,'cfprDcxVcName':cfprDcxVcName,'cfprDcxVcOperBorderAggrPortId':cfprDcxVcOperBorderAggrPortId,'cfprDcxVcOperBorderPortId':cfprDcxVcOperBorderPortId,'cfprDcxVcOperBorderSlotId':cfprDcxVcOperBorderSlotId,'cfprDcxVcOperState':cfprDcxVcOperState,'cfprDcxVcPeerId':cfprDcxVcPeerId,'cfprDcxVcProtState':cfprDcxVcProtState,'cfprDcxVcQosPolicyDn':cfprDcxVcQosPolicyDn,'cfprDcxVcQosPolicyId':cfprDcxVcQosPolicyId,'cfprDcxVcRole':cfprDcxVcRole,'cfprDcxVcState':cfprDcxVcState,'cfprDcxVcStateQual':cfprDcxVcStateQual,'cfprDcxVcSwitchId':cfprDcxVcSwitchId,'cfprDcxVcTag':cfprDcxVcTag,'cfprDcxVcTransport':cfprDcxVcTransport,'cfprDcxVcType':cfprDcxVcType,'cfprDcxVcUplinkFailAction':cfprDcxVcUplinkFailAction,'cfprDcxVcVnic':cfprDcxVcVnic,'cfprDcxVcServiceState':cfprDcxVcServiceState,'cfprDcxVifEpTable':cfprDcxVifEpTable,'cfprDcxVifEpEntry':cfprDcxVifEpEntry,_J:cfprDcxVifEpInstanceId,'cfprDcxVifEpDn':cfprDcxVifEpDn,'cfprDcxVifEpRn':cfprDcxVifEpRn,'cfprDcxVifEpId':cfprDcxVifEpId})