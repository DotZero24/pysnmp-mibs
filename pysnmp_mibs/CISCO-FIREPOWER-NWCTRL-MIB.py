_H='cfprNwctrlSubIfInstanceId'
_G='cfprNwctrlPortConfigInstanceId'
_F='cfprNwctrlCardConfigInstanceId'
_E='cfprNwctrlDefinitionInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-NWCTRL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprEquipmentCardAdminState,CfprEquipmentPowerState,CfprFabricAdminState,CfprFabricSSAPortType,CfprNwctrlAdminState,CfprNwctrlCardAction,CfprNwctrlConfigState,CfprNwctrlLinkFailAction,CfprNwctrlOirState,CfprNwctrlRegistrationMode,CfprPolicyPolicyOwner,CfprPortDuplex,CfprPortEthSpeed=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprEquipmentCardAdminState','CfprEquipmentPowerState','CfprFabricAdminState','CfprFabricSSAPortType','CfprNwctrlAdminState','CfprNwctrlCardAction','CfprNwctrlConfigState','CfprNwctrlLinkFailAction','CfprNwctrlOirState','CfprNwctrlRegistrationMode','CfprPolicyPolicyOwner','CfprPortDuplex','CfprPortEthSpeed')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprNwctrlObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,56))
_CfprNwctrlDefinitionTable_Object=MibTable
cfprNwctrlDefinitionTable=_CfprNwctrlDefinitionTable_Object((1,3,6,1,4,1,9,9,826,1,56,1))
if mibBuilder.loadTexts:cfprNwctrlDefinitionTable.setStatus(_A)
_CfprNwctrlDefinitionEntry_Object=MibTableRow
cfprNwctrlDefinitionEntry=_CfprNwctrlDefinitionEntry_Object((1,3,6,1,4,1,9,9,826,1,56,1,1))
cfprNwctrlDefinitionEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprNwctrlDefinitionEntry.setStatus(_A)
_CfprNwctrlDefinitionInstanceId_Type=CfprManagedObjectId
_CfprNwctrlDefinitionInstanceId_Object=MibTableColumn
cfprNwctrlDefinitionInstanceId=_CfprNwctrlDefinitionInstanceId_Object((1,3,6,1,4,1,9,9,826,1,56,1,1,1),_CfprNwctrlDefinitionInstanceId_Type())
cfprNwctrlDefinitionInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprNwctrlDefinitionInstanceId.setStatus(_A)
_CfprNwctrlDefinitionDn_Type=CfprManagedObjectDn
_CfprNwctrlDefinitionDn_Object=MibTableColumn
cfprNwctrlDefinitionDn=_CfprNwctrlDefinitionDn_Object((1,3,6,1,4,1,9,9,826,1,56,1,1,2),_CfprNwctrlDefinitionDn_Type())
cfprNwctrlDefinitionDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlDefinitionDn.setStatus(_A)
_CfprNwctrlDefinitionRn_Type=SnmpAdminString
_CfprNwctrlDefinitionRn_Object=MibTableColumn
cfprNwctrlDefinitionRn=_CfprNwctrlDefinitionRn_Object((1,3,6,1,4,1,9,9,826,1,56,1,1,3),_CfprNwctrlDefinitionRn_Type())
cfprNwctrlDefinitionRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlDefinitionRn.setStatus(_A)
_CfprNwctrlDefinitionCdp_Type=CfprNwctrlAdminState
_CfprNwctrlDefinitionCdp_Object=MibTableColumn
cfprNwctrlDefinitionCdp=_CfprNwctrlDefinitionCdp_Object((1,3,6,1,4,1,9,9,826,1,56,1,1,4),_CfprNwctrlDefinitionCdp_Type())
cfprNwctrlDefinitionCdp.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlDefinitionCdp.setStatus(_A)
_CfprNwctrlDefinitionDescr_Type=SnmpAdminString
_CfprNwctrlDefinitionDescr_Object=MibTableColumn
cfprNwctrlDefinitionDescr=_CfprNwctrlDefinitionDescr_Object((1,3,6,1,4,1,9,9,826,1,56,1,1,5),_CfprNwctrlDefinitionDescr_Type())
cfprNwctrlDefinitionDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlDefinitionDescr.setStatus(_A)
_CfprNwctrlDefinitionIntId_Type=SnmpAdminString
_CfprNwctrlDefinitionIntId_Object=MibTableColumn
cfprNwctrlDefinitionIntId=_CfprNwctrlDefinitionIntId_Object((1,3,6,1,4,1,9,9,826,1,56,1,1,6),_CfprNwctrlDefinitionIntId_Type())
cfprNwctrlDefinitionIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlDefinitionIntId.setStatus(_A)
_CfprNwctrlDefinitionMacRegisterMode_Type=CfprNwctrlRegistrationMode
_CfprNwctrlDefinitionMacRegisterMode_Object=MibTableColumn
cfprNwctrlDefinitionMacRegisterMode=_CfprNwctrlDefinitionMacRegisterMode_Object((1,3,6,1,4,1,9,9,826,1,56,1,1,7),_CfprNwctrlDefinitionMacRegisterMode_Type())
cfprNwctrlDefinitionMacRegisterMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlDefinitionMacRegisterMode.setStatus(_A)
_CfprNwctrlDefinitionName_Type=SnmpAdminString
_CfprNwctrlDefinitionName_Object=MibTableColumn
cfprNwctrlDefinitionName=_CfprNwctrlDefinitionName_Object((1,3,6,1,4,1,9,9,826,1,56,1,1,8),_CfprNwctrlDefinitionName_Type())
cfprNwctrlDefinitionName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlDefinitionName.setStatus(_A)
_CfprNwctrlDefinitionPolicyLevel_Type=Gauge32
_CfprNwctrlDefinitionPolicyLevel_Object=MibTableColumn
cfprNwctrlDefinitionPolicyLevel=_CfprNwctrlDefinitionPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,56,1,1,9),_CfprNwctrlDefinitionPolicyLevel_Type())
cfprNwctrlDefinitionPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlDefinitionPolicyLevel.setStatus(_A)
_CfprNwctrlDefinitionPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprNwctrlDefinitionPolicyOwner_Object=MibTableColumn
cfprNwctrlDefinitionPolicyOwner=_CfprNwctrlDefinitionPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,56,1,1,10),_CfprNwctrlDefinitionPolicyOwner_Type())
cfprNwctrlDefinitionPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlDefinitionPolicyOwner.setStatus(_A)
_CfprNwctrlDefinitionUplinkFailAction_Type=CfprNwctrlLinkFailAction
_CfprNwctrlDefinitionUplinkFailAction_Object=MibTableColumn
cfprNwctrlDefinitionUplinkFailAction=_CfprNwctrlDefinitionUplinkFailAction_Object((1,3,6,1,4,1,9,9,826,1,56,1,1,11),_CfprNwctrlDefinitionUplinkFailAction_Type())
cfprNwctrlDefinitionUplinkFailAction.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlDefinitionUplinkFailAction.setStatus(_A)
_CfprNwctrlDefinitionLldpReceive_Type=CfprNwctrlAdminState
_CfprNwctrlDefinitionLldpReceive_Object=MibTableColumn
cfprNwctrlDefinitionLldpReceive=_CfprNwctrlDefinitionLldpReceive_Object((1,3,6,1,4,1,9,9,826,1,56,1,1,12),_CfprNwctrlDefinitionLldpReceive_Type())
cfprNwctrlDefinitionLldpReceive.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlDefinitionLldpReceive.setStatus(_A)
_CfprNwctrlDefinitionLldpTransmit_Type=CfprNwctrlAdminState
_CfprNwctrlDefinitionLldpTransmit_Object=MibTableColumn
cfprNwctrlDefinitionLldpTransmit=_CfprNwctrlDefinitionLldpTransmit_Object((1,3,6,1,4,1,9,9,826,1,56,1,1,13),_CfprNwctrlDefinitionLldpTransmit_Type())
cfprNwctrlDefinitionLldpTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlDefinitionLldpTransmit.setStatus(_A)
_CfprNwctrlCardConfigTable_Object=MibTable
cfprNwctrlCardConfigTable=_CfprNwctrlCardConfigTable_Object((1,3,6,1,4,1,9,9,826,1,56,2))
if mibBuilder.loadTexts:cfprNwctrlCardConfigTable.setStatus(_A)
_CfprNwctrlCardConfigEntry_Object=MibTableRow
cfprNwctrlCardConfigEntry=_CfprNwctrlCardConfigEntry_Object((1,3,6,1,4,1,9,9,826,1,56,2,1))
cfprNwctrlCardConfigEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprNwctrlCardConfigEntry.setStatus(_A)
_CfprNwctrlCardConfigInstanceId_Type=CfprManagedObjectId
_CfprNwctrlCardConfigInstanceId_Object=MibTableColumn
cfprNwctrlCardConfigInstanceId=_CfprNwctrlCardConfigInstanceId_Object((1,3,6,1,4,1,9,9,826,1,56,2,1,1),_CfprNwctrlCardConfigInstanceId_Type())
cfprNwctrlCardConfigInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprNwctrlCardConfigInstanceId.setStatus(_A)
_CfprNwctrlCardConfigDn_Type=CfprManagedObjectDn
_CfprNwctrlCardConfigDn_Object=MibTableColumn
cfprNwctrlCardConfigDn=_CfprNwctrlCardConfigDn_Object((1,3,6,1,4,1,9,9,826,1,56,2,1,2),_CfprNwctrlCardConfigDn_Type())
cfprNwctrlCardConfigDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlCardConfigDn.setStatus(_A)
_CfprNwctrlCardConfigRn_Type=SnmpAdminString
_CfprNwctrlCardConfigRn_Object=MibTableColumn
cfprNwctrlCardConfigRn=_CfprNwctrlCardConfigRn_Object((1,3,6,1,4,1,9,9,826,1,56,2,1,3),_CfprNwctrlCardConfigRn_Type())
cfprNwctrlCardConfigRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlCardConfigRn.setStatus(_A)
_CfprNwctrlCardConfigAction_Type=CfprNwctrlCardAction
_CfprNwctrlCardConfigAction_Object=MibTableColumn
cfprNwctrlCardConfigAction=_CfprNwctrlCardConfigAction_Object((1,3,6,1,4,1,9,9,826,1,56,2,1,4),_CfprNwctrlCardConfigAction_Type())
cfprNwctrlCardConfigAction.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlCardConfigAction.setStatus(_A)
_CfprNwctrlCardConfigAdminState_Type=CfprEquipmentCardAdminState
_CfprNwctrlCardConfigAdminState_Object=MibTableColumn
cfprNwctrlCardConfigAdminState=_CfprNwctrlCardConfigAdminState_Object((1,3,6,1,4,1,9,9,826,1,56,2,1,5),_CfprNwctrlCardConfigAdminState_Type())
cfprNwctrlCardConfigAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlCardConfigAdminState.setStatus(_A)
_CfprNwctrlCardConfigConfigState_Type=CfprNwctrlConfigState
_CfprNwctrlCardConfigConfigState_Object=MibTableColumn
cfprNwctrlCardConfigConfigState=_CfprNwctrlCardConfigConfigState_Object((1,3,6,1,4,1,9,9,826,1,56,2,1,6),_CfprNwctrlCardConfigConfigState_Type())
cfprNwctrlCardConfigConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlCardConfigConfigState.setStatus(_A)
_CfprNwctrlCardConfigFltAggr_Type=Unsigned64
_CfprNwctrlCardConfigFltAggr_Object=MibTableColumn
cfprNwctrlCardConfigFltAggr=_CfprNwctrlCardConfigFltAggr_Object((1,3,6,1,4,1,9,9,826,1,56,2,1,7),_CfprNwctrlCardConfigFltAggr_Type())
cfprNwctrlCardConfigFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlCardConfigFltAggr.setStatus(_A)
_CfprNwctrlCardConfigModel_Type=SnmpAdminString
_CfprNwctrlCardConfigModel_Object=MibTableColumn
cfprNwctrlCardConfigModel=_CfprNwctrlCardConfigModel_Object((1,3,6,1,4,1,9,9,826,1,56,2,1,8),_CfprNwctrlCardConfigModel_Type())
cfprNwctrlCardConfigModel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlCardConfigModel.setStatus(_A)
_CfprNwctrlCardConfigOirState_Type=CfprNwctrlOirState
_CfprNwctrlCardConfigOirState_Object=MibTableColumn
cfprNwctrlCardConfigOirState=_CfprNwctrlCardConfigOirState_Object((1,3,6,1,4,1,9,9,826,1,56,2,1,9),_CfprNwctrlCardConfigOirState_Type())
cfprNwctrlCardConfigOirState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlCardConfigOirState.setStatus(_A)
_CfprNwctrlCardConfigOperState_Type=CfprEquipmentPowerState
_CfprNwctrlCardConfigOperState_Object=MibTableColumn
cfprNwctrlCardConfigOperState=_CfprNwctrlCardConfigOperState_Object((1,3,6,1,4,1,9,9,826,1,56,2,1,10),_CfprNwctrlCardConfigOperState_Type())
cfprNwctrlCardConfigOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlCardConfigOperState.setStatus(_A)
_CfprNwctrlCardConfigPresence_Type=TruthValue
_CfprNwctrlCardConfigPresence_Object=MibTableColumn
cfprNwctrlCardConfigPresence=_CfprNwctrlCardConfigPresence_Object((1,3,6,1,4,1,9,9,826,1,56,2,1,11),_CfprNwctrlCardConfigPresence_Type())
cfprNwctrlCardConfigPresence.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlCardConfigPresence.setStatus(_A)
_CfprNwctrlCardConfigRevision_Type=SnmpAdminString
_CfprNwctrlCardConfigRevision_Object=MibTableColumn
cfprNwctrlCardConfigRevision=_CfprNwctrlCardConfigRevision_Object((1,3,6,1,4,1,9,9,826,1,56,2,1,12),_CfprNwctrlCardConfigRevision_Type())
cfprNwctrlCardConfigRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlCardConfigRevision.setStatus(_A)
_CfprNwctrlCardConfigSlotId_Type=Gauge32
_CfprNwctrlCardConfigSlotId_Object=MibTableColumn
cfprNwctrlCardConfigSlotId=_CfprNwctrlCardConfigSlotId_Object((1,3,6,1,4,1,9,9,826,1,56,2,1,13),_CfprNwctrlCardConfigSlotId_Type())
cfprNwctrlCardConfigSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlCardConfigSlotId.setStatus(_A)
_CfprNwctrlCardConfigTs_Type=DateAndTime
_CfprNwctrlCardConfigTs_Object=MibTableColumn
cfprNwctrlCardConfigTs=_CfprNwctrlCardConfigTs_Object((1,3,6,1,4,1,9,9,826,1,56,2,1,14),_CfprNwctrlCardConfigTs_Type())
cfprNwctrlCardConfigTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlCardConfigTs.setStatus(_A)
_CfprNwctrlCardConfigVendor_Type=SnmpAdminString
_CfprNwctrlCardConfigVendor_Object=MibTableColumn
cfprNwctrlCardConfigVendor=_CfprNwctrlCardConfigVendor_Object((1,3,6,1,4,1,9,9,826,1,56,2,1,15),_CfprNwctrlCardConfigVendor_Type())
cfprNwctrlCardConfigVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlCardConfigVendor.setStatus(_A)
_CfprNwctrlPortConfigTable_Object=MibTable
cfprNwctrlPortConfigTable=_CfprNwctrlPortConfigTable_Object((1,3,6,1,4,1,9,9,826,1,56,3))
if mibBuilder.loadTexts:cfprNwctrlPortConfigTable.setStatus(_A)
_CfprNwctrlPortConfigEntry_Object=MibTableRow
cfprNwctrlPortConfigEntry=_CfprNwctrlPortConfigEntry_Object((1,3,6,1,4,1,9,9,826,1,56,3,1))
cfprNwctrlPortConfigEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprNwctrlPortConfigEntry.setStatus(_A)
_CfprNwctrlPortConfigInstanceId_Type=CfprManagedObjectId
_CfprNwctrlPortConfigInstanceId_Object=MibTableColumn
cfprNwctrlPortConfigInstanceId=_CfprNwctrlPortConfigInstanceId_Object((1,3,6,1,4,1,9,9,826,1,56,3,1,1),_CfprNwctrlPortConfigInstanceId_Type())
cfprNwctrlPortConfigInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprNwctrlPortConfigInstanceId.setStatus(_A)
_CfprNwctrlPortConfigDn_Type=CfprManagedObjectDn
_CfprNwctrlPortConfigDn_Object=MibTableColumn
cfprNwctrlPortConfigDn=_CfprNwctrlPortConfigDn_Object((1,3,6,1,4,1,9,9,826,1,56,3,1,2),_CfprNwctrlPortConfigDn_Type())
cfprNwctrlPortConfigDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlPortConfigDn.setStatus(_A)
_CfprNwctrlPortConfigRn_Type=SnmpAdminString
_CfprNwctrlPortConfigRn_Object=MibTableColumn
cfprNwctrlPortConfigRn=_CfprNwctrlPortConfigRn_Object((1,3,6,1,4,1,9,9,826,1,56,3,1,3),_CfprNwctrlPortConfigRn_Type())
cfprNwctrlPortConfigRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlPortConfigRn.setStatus(_A)
_CfprNwctrlPortConfigAdminDuplex_Type=CfprPortDuplex
_CfprNwctrlPortConfigAdminDuplex_Object=MibTableColumn
cfprNwctrlPortConfigAdminDuplex=_CfprNwctrlPortConfigAdminDuplex_Object((1,3,6,1,4,1,9,9,826,1,56,3,1,4),_CfprNwctrlPortConfigAdminDuplex_Type())
cfprNwctrlPortConfigAdminDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlPortConfigAdminDuplex.setStatus(_A)
_CfprNwctrlPortConfigAdminSpeed_Type=CfprPortEthSpeed
_CfprNwctrlPortConfigAdminSpeed_Object=MibTableColumn
cfprNwctrlPortConfigAdminSpeed=_CfprNwctrlPortConfigAdminSpeed_Object((1,3,6,1,4,1,9,9,826,1,56,3,1,5),_CfprNwctrlPortConfigAdminSpeed_Type())
cfprNwctrlPortConfigAdminSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlPortConfigAdminSpeed.setStatus(_A)
_CfprNwctrlPortConfigAdminState_Type=CfprFabricAdminState
_CfprNwctrlPortConfigAdminState_Object=MibTableColumn
cfprNwctrlPortConfigAdminState=_CfprNwctrlPortConfigAdminState_Object((1,3,6,1,4,1,9,9,826,1,56,3,1,6),_CfprNwctrlPortConfigAdminState_Type())
cfprNwctrlPortConfigAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlPortConfigAdminState.setStatus(_A)
_CfprNwctrlPortConfigAggrId_Type=Gauge32
_CfprNwctrlPortConfigAggrId_Object=MibTableColumn
cfprNwctrlPortConfigAggrId=_CfprNwctrlPortConfigAggrId_Object((1,3,6,1,4,1,9,9,826,1,56,3,1,7),_CfprNwctrlPortConfigAggrId_Type())
cfprNwctrlPortConfigAggrId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlPortConfigAggrId.setStatus(_A)
_CfprNwctrlPortConfigAllowSharing_Type=TruthValue
_CfprNwctrlPortConfigAllowSharing_Object=MibTableColumn
cfprNwctrlPortConfigAllowSharing=_CfprNwctrlPortConfigAllowSharing_Object((1,3,6,1,4,1,9,9,826,1,56,3,1,8),_CfprNwctrlPortConfigAllowSharing_Type())
cfprNwctrlPortConfigAllowSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlPortConfigAllowSharing.setStatus(_A)
_CfprNwctrlPortConfigAutoNeg_Type=TruthValue
_CfprNwctrlPortConfigAutoNeg_Object=MibTableColumn
cfprNwctrlPortConfigAutoNeg=_CfprNwctrlPortConfigAutoNeg_Object((1,3,6,1,4,1,9,9,826,1,56,3,1,9),_CfprNwctrlPortConfigAutoNeg_Type())
cfprNwctrlPortConfigAutoNeg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlPortConfigAutoNeg.setStatus(_A)
_CfprNwctrlPortConfigFlowCtrlPolicy_Type=SnmpAdminString
_CfprNwctrlPortConfigFlowCtrlPolicy_Object=MibTableColumn
cfprNwctrlPortConfigFlowCtrlPolicy=_CfprNwctrlPortConfigFlowCtrlPolicy_Object((1,3,6,1,4,1,9,9,826,1,56,3,1,10),_CfprNwctrlPortConfigFlowCtrlPolicy_Type())
cfprNwctrlPortConfigFlowCtrlPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlPortConfigFlowCtrlPolicy.setStatus(_A)
_CfprNwctrlPortConfigPcId_Type=Gauge32
_CfprNwctrlPortConfigPcId_Object=MibTableColumn
cfprNwctrlPortConfigPcId=_CfprNwctrlPortConfigPcId_Object((1,3,6,1,4,1,9,9,826,1,56,3,1,11),_CfprNwctrlPortConfigPcId_Type())
cfprNwctrlPortConfigPcId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlPortConfigPcId.setStatus(_A)
_CfprNwctrlPortConfigPortId_Type=Gauge32
_CfprNwctrlPortConfigPortId_Object=MibTableColumn
cfprNwctrlPortConfigPortId=_CfprNwctrlPortConfigPortId_Object((1,3,6,1,4,1,9,9,826,1,56,3,1,12),_CfprNwctrlPortConfigPortId_Type())
cfprNwctrlPortConfigPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlPortConfigPortId.setStatus(_A)
_CfprNwctrlPortConfigSlotId_Type=Gauge32
_CfprNwctrlPortConfigSlotId_Object=MibTableColumn
cfprNwctrlPortConfigSlotId=_CfprNwctrlPortConfigSlotId_Object((1,3,6,1,4,1,9,9,826,1,56,3,1,13),_CfprNwctrlPortConfigSlotId_Type())
cfprNwctrlPortConfigSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlPortConfigSlotId.setStatus(_A)
_CfprNwctrlPortConfigSsaPortType_Type=CfprFabricSSAPortType
_CfprNwctrlPortConfigSsaPortType_Object=MibTableColumn
cfprNwctrlPortConfigSsaPortType=_CfprNwctrlPortConfigSsaPortType_Object((1,3,6,1,4,1,9,9,826,1,56,3,1,14),_CfprNwctrlPortConfigSsaPortType_Type())
cfprNwctrlPortConfigSsaPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlPortConfigSsaPortType.setStatus(_A)
_CfprNwctrlPortConfigTs_Type=DateAndTime
_CfprNwctrlPortConfigTs_Object=MibTableColumn
cfprNwctrlPortConfigTs=_CfprNwctrlPortConfigTs_Object((1,3,6,1,4,1,9,9,826,1,56,3,1,15),_CfprNwctrlPortConfigTs_Type())
cfprNwctrlPortConfigTs.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlPortConfigTs.setStatus(_A)
_CfprNwctrlPortConfigNwCtrlPolicyName_Type=SnmpAdminString
_CfprNwctrlPortConfigNwCtrlPolicyName_Object=MibTableColumn
cfprNwctrlPortConfigNwCtrlPolicyName=_CfprNwctrlPortConfigNwCtrlPolicyName_Object((1,3,6,1,4,1,9,9,826,1,56,3,1,16),_CfprNwctrlPortConfigNwCtrlPolicyName_Type())
cfprNwctrlPortConfigNwCtrlPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlPortConfigNwCtrlPolicyName.setStatus(_A)
_CfprNwctrlPortConfigAllowAneg_Type=TruthValue
_CfprNwctrlPortConfigAllowAneg_Object=MibTableColumn
cfprNwctrlPortConfigAllowAneg=_CfprNwctrlPortConfigAllowAneg_Object((1,3,6,1,4,1,9,9,826,1,56,3,1,17),_CfprNwctrlPortConfigAllowAneg_Type())
cfprNwctrlPortConfigAllowAneg.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlPortConfigAllowAneg.setStatus(_A)
_CfprNwctrlSubIfTable_Object=MibTable
cfprNwctrlSubIfTable=_CfprNwctrlSubIfTable_Object((1,3,6,1,4,1,9,9,826,1,56,4))
if mibBuilder.loadTexts:cfprNwctrlSubIfTable.setStatus(_A)
_CfprNwctrlSubIfEntry_Object=MibTableRow
cfprNwctrlSubIfEntry=_CfprNwctrlSubIfEntry_Object((1,3,6,1,4,1,9,9,826,1,56,4,1))
cfprNwctrlSubIfEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprNwctrlSubIfEntry.setStatus(_A)
_CfprNwctrlSubIfInstanceId_Type=CfprManagedObjectId
_CfprNwctrlSubIfInstanceId_Object=MibTableColumn
cfprNwctrlSubIfInstanceId=_CfprNwctrlSubIfInstanceId_Object((1,3,6,1,4,1,9,9,826,1,56,4,1,1),_CfprNwctrlSubIfInstanceId_Type())
cfprNwctrlSubIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprNwctrlSubIfInstanceId.setStatus(_A)
_CfprNwctrlSubIfDn_Type=CfprManagedObjectDn
_CfprNwctrlSubIfDn_Object=MibTableColumn
cfprNwctrlSubIfDn=_CfprNwctrlSubIfDn_Object((1,3,6,1,4,1,9,9,826,1,56,4,1,2),_CfprNwctrlSubIfDn_Type())
cfprNwctrlSubIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlSubIfDn.setStatus(_A)
_CfprNwctrlSubIfRn_Type=SnmpAdminString
_CfprNwctrlSubIfRn_Object=MibTableColumn
cfprNwctrlSubIfRn=_CfprNwctrlSubIfRn_Object((1,3,6,1,4,1,9,9,826,1,56,4,1,3),_CfprNwctrlSubIfRn_Type())
cfprNwctrlSubIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlSubIfRn.setStatus(_A)
_CfprNwctrlSubIfAdminState_Type=CfprFabricAdminState
_CfprNwctrlSubIfAdminState_Object=MibTableColumn
cfprNwctrlSubIfAdminState=_CfprNwctrlSubIfAdminState_Object((1,3,6,1,4,1,9,9,826,1,56,4,1,4),_CfprNwctrlSubIfAdminState_Type())
cfprNwctrlSubIfAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlSubIfAdminState.setStatus(_A)
_CfprNwctrlSubIfAllowSharing_Type=TruthValue
_CfprNwctrlSubIfAllowSharing_Object=MibTableColumn
cfprNwctrlSubIfAllowSharing=_CfprNwctrlSubIfAllowSharing_Object((1,3,6,1,4,1,9,9,826,1,56,4,1,5),_CfprNwctrlSubIfAllowSharing_Type())
cfprNwctrlSubIfAllowSharing.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlSubIfAllowSharing.setStatus(_A)
_CfprNwctrlSubIfSsaPortType_Type=CfprFabricSSAPortType
_CfprNwctrlSubIfSsaPortType_Object=MibTableColumn
cfprNwctrlSubIfSsaPortType=_CfprNwctrlSubIfSsaPortType_Object((1,3,6,1,4,1,9,9,826,1,56,4,1,6),_CfprNwctrlSubIfSsaPortType_Type())
cfprNwctrlSubIfSsaPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlSubIfSsaPortType.setStatus(_A)
_CfprNwctrlSubIfSubId_Type=Gauge32
_CfprNwctrlSubIfSubId_Object=MibTableColumn
cfprNwctrlSubIfSubId=_CfprNwctrlSubIfSubId_Object((1,3,6,1,4,1,9,9,826,1,56,4,1,7),_CfprNwctrlSubIfSubId_Type())
cfprNwctrlSubIfSubId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlSubIfSubId.setStatus(_A)
_CfprNwctrlSubIfVlanId_Type=Integer32
_CfprNwctrlSubIfVlanId_Object=MibTableColumn
cfprNwctrlSubIfVlanId=_CfprNwctrlSubIfVlanId_Object((1,3,6,1,4,1,9,9,826,1,56,4,1,8),_CfprNwctrlSubIfVlanId_Type())
cfprNwctrlSubIfVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprNwctrlSubIfVlanId.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprNwctrlObjects':cfprNwctrlObjects,'cfprNwctrlDefinitionTable':cfprNwctrlDefinitionTable,'cfprNwctrlDefinitionEntry':cfprNwctrlDefinitionEntry,_E:cfprNwctrlDefinitionInstanceId,'cfprNwctrlDefinitionDn':cfprNwctrlDefinitionDn,'cfprNwctrlDefinitionRn':cfprNwctrlDefinitionRn,'cfprNwctrlDefinitionCdp':cfprNwctrlDefinitionCdp,'cfprNwctrlDefinitionDescr':cfprNwctrlDefinitionDescr,'cfprNwctrlDefinitionIntId':cfprNwctrlDefinitionIntId,'cfprNwctrlDefinitionMacRegisterMode':cfprNwctrlDefinitionMacRegisterMode,'cfprNwctrlDefinitionName':cfprNwctrlDefinitionName,'cfprNwctrlDefinitionPolicyLevel':cfprNwctrlDefinitionPolicyLevel,'cfprNwctrlDefinitionPolicyOwner':cfprNwctrlDefinitionPolicyOwner,'cfprNwctrlDefinitionUplinkFailAction':cfprNwctrlDefinitionUplinkFailAction,'cfprNwctrlDefinitionLldpReceive':cfprNwctrlDefinitionLldpReceive,'cfprNwctrlDefinitionLldpTransmit':cfprNwctrlDefinitionLldpTransmit,'cfprNwctrlCardConfigTable':cfprNwctrlCardConfigTable,'cfprNwctrlCardConfigEntry':cfprNwctrlCardConfigEntry,_F:cfprNwctrlCardConfigInstanceId,'cfprNwctrlCardConfigDn':cfprNwctrlCardConfigDn,'cfprNwctrlCardConfigRn':cfprNwctrlCardConfigRn,'cfprNwctrlCardConfigAction':cfprNwctrlCardConfigAction,'cfprNwctrlCardConfigAdminState':cfprNwctrlCardConfigAdminState,'cfprNwctrlCardConfigConfigState':cfprNwctrlCardConfigConfigState,'cfprNwctrlCardConfigFltAggr':cfprNwctrlCardConfigFltAggr,'cfprNwctrlCardConfigModel':cfprNwctrlCardConfigModel,'cfprNwctrlCardConfigOirState':cfprNwctrlCardConfigOirState,'cfprNwctrlCardConfigOperState':cfprNwctrlCardConfigOperState,'cfprNwctrlCardConfigPresence':cfprNwctrlCardConfigPresence,'cfprNwctrlCardConfigRevision':cfprNwctrlCardConfigRevision,'cfprNwctrlCardConfigSlotId':cfprNwctrlCardConfigSlotId,'cfprNwctrlCardConfigTs':cfprNwctrlCardConfigTs,'cfprNwctrlCardConfigVendor':cfprNwctrlCardConfigVendor,'cfprNwctrlPortConfigTable':cfprNwctrlPortConfigTable,'cfprNwctrlPortConfigEntry':cfprNwctrlPortConfigEntry,_G:cfprNwctrlPortConfigInstanceId,'cfprNwctrlPortConfigDn':cfprNwctrlPortConfigDn,'cfprNwctrlPortConfigRn':cfprNwctrlPortConfigRn,'cfprNwctrlPortConfigAdminDuplex':cfprNwctrlPortConfigAdminDuplex,'cfprNwctrlPortConfigAdminSpeed':cfprNwctrlPortConfigAdminSpeed,'cfprNwctrlPortConfigAdminState':cfprNwctrlPortConfigAdminState,'cfprNwctrlPortConfigAggrId':cfprNwctrlPortConfigAggrId,'cfprNwctrlPortConfigAllowSharing':cfprNwctrlPortConfigAllowSharing,'cfprNwctrlPortConfigAutoNeg':cfprNwctrlPortConfigAutoNeg,'cfprNwctrlPortConfigFlowCtrlPolicy':cfprNwctrlPortConfigFlowCtrlPolicy,'cfprNwctrlPortConfigPcId':cfprNwctrlPortConfigPcId,'cfprNwctrlPortConfigPortId':cfprNwctrlPortConfigPortId,'cfprNwctrlPortConfigSlotId':cfprNwctrlPortConfigSlotId,'cfprNwctrlPortConfigSsaPortType':cfprNwctrlPortConfigSsaPortType,'cfprNwctrlPortConfigTs':cfprNwctrlPortConfigTs,'cfprNwctrlPortConfigNwCtrlPolicyName':cfprNwctrlPortConfigNwCtrlPolicyName,'cfprNwctrlPortConfigAllowAneg':cfprNwctrlPortConfigAllowAneg,'cfprNwctrlSubIfTable':cfprNwctrlSubIfTable,'cfprNwctrlSubIfEntry':cfprNwctrlSubIfEntry,_H:cfprNwctrlSubIfInstanceId,'cfprNwctrlSubIfDn':cfprNwctrlSubIfDn,'cfprNwctrlSubIfRn':cfprNwctrlSubIfRn,'cfprNwctrlSubIfAdminState':cfprNwctrlSubIfAdminState,'cfprNwctrlSubIfAllowSharing':cfprNwctrlSubIfAllowSharing,'cfprNwctrlSubIfSsaPortType':cfprNwctrlSubIfSsaPortType,'cfprNwctrlSubIfSubId':cfprNwctrlSubIfSubId,'cfprNwctrlSubIfVlanId':cfprNwctrlSubIfVlanId})