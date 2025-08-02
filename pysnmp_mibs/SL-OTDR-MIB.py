_I='slOTDREventIndex'
_H='slOTDREventTableIndex'
_G='slOTDREventLineIndex'
_F='slOTDRPRConfigLineIndex'
_E='slOTDRMDConfigLineIndex'
_D='SL-OTDR-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
slService,=mibBuilder.importSymbols('SL-NE-MIB','slService')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
slOTDR=ModuleIdentity((1,3,6,1,4,1,4515,1,1,19))
_SlOTDRConfig_ObjectIdentity=ObjectIdentity
slOTDRConfig=_SlOTDRConfig_ObjectIdentity((1,3,6,1,4,1,4515,1,1,19,1))
_SlOTDRMDConfigTable_Object=MibTable
slOTDRMDConfigTable=_SlOTDRMDConfigTable_Object((1,3,6,1,4,1,4515,1,1,19,1,1))
if mibBuilder.loadTexts:slOTDRMDConfigTable.setStatus(_A)
_SlOTDRMDConfigEntry_Object=MibTableRow
slOTDRMDConfigEntry=_SlOTDRMDConfigEntry_Object((1,3,6,1,4,1,4515,1,1,19,1,1,1))
slOTDRMDConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:slOTDRMDConfigEntry.setStatus(_A)
_SlOTDRMDConfigLineIndex_Type=InterfaceIndex
_SlOTDRMDConfigLineIndex_Object=MibTableColumn
slOTDRMDConfigLineIndex=_SlOTDRMDConfigLineIndex_Object((1,3,6,1,4,1,4515,1,1,19,1,1,1,1),_SlOTDRMDConfigLineIndex_Type())
slOTDRMDConfigLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTDRMDConfigLineIndex.setStatus(_A)
_SlOTDRMDConfigAdminStatus_Type=Integer32
_SlOTDRMDConfigAdminStatus_Object=MibTableColumn
slOTDRMDConfigAdminStatus=_SlOTDRMDConfigAdminStatus_Object((1,3,6,1,4,1,4515,1,1,19,1,1,1,2),_SlOTDRMDConfigAdminStatus_Type())
slOTDRMDConfigAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTDRMDConfigAdminStatus.setStatus(_A)
_SlOTDRMDConfigOperStatus_Type=Integer32
_SlOTDRMDConfigOperStatus_Object=MibTableColumn
slOTDRMDConfigOperStatus=_SlOTDRMDConfigOperStatus_Object((1,3,6,1,4,1,4515,1,1,19,1,1,1,3),_SlOTDRMDConfigOperStatus_Type())
slOTDRMDConfigOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTDRMDConfigOperStatus.setStatus(_A)
_SlOTDRMDConfigPN_Type=DisplayString
_SlOTDRMDConfigPN_Object=MibTableColumn
slOTDRMDConfigPN=_SlOTDRMDConfigPN_Object((1,3,6,1,4,1,4515,1,1,19,1,1,1,4),_SlOTDRMDConfigPN_Type())
slOTDRMDConfigPN.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTDRMDConfigPN.setStatus(_A)
_SlOTDRMDConfigSNO_Type=DisplayString
_SlOTDRMDConfigSNO_Object=MibTableColumn
slOTDRMDConfigSNO=_SlOTDRMDConfigSNO_Object((1,3,6,1,4,1,4515,1,1,19,1,1,1,5),_SlOTDRMDConfigSNO_Type())
slOTDRMDConfigSNO.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTDRMDConfigSNO.setStatus(_A)
_SlOTDRMDConfigMF_Type=DisplayString
_SlOTDRMDConfigMF_Object=MibTableColumn
slOTDRMDConfigMF=_SlOTDRMDConfigMF_Object((1,3,6,1,4,1,4515,1,1,19,1,1,1,6),_SlOTDRMDConfigMF_Type())
slOTDRMDConfigMF.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTDRMDConfigMF.setStatus(_A)
_SlOTDRMDConfigHWR_Type=DisplayString
_SlOTDRMDConfigHWR_Object=MibTableColumn
slOTDRMDConfigHWR=_SlOTDRMDConfigHWR_Object((1,3,6,1,4,1,4515,1,1,19,1,1,1,7),_SlOTDRMDConfigHWR_Type())
slOTDRMDConfigHWR.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTDRMDConfigHWR.setStatus(_A)
_SlOTDRMDConfigFWR_Type=DisplayString
_SlOTDRMDConfigFWR_Object=MibTableColumn
slOTDRMDConfigFWR=_SlOTDRMDConfigFWR_Object((1,3,6,1,4,1,4515,1,1,19,1,1,1,8),_SlOTDRMDConfigFWR_Type())
slOTDRMDConfigFWR.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTDRMDConfigFWR.setStatus(_A)
_SlOTDRMDConfigPortLock_Type=Integer32
_SlOTDRMDConfigPortLock_Object=MibTableColumn
slOTDRMDConfigPortLock=_SlOTDRMDConfigPortLock_Object((1,3,6,1,4,1,4515,1,1,19,1,1,1,9),_SlOTDRMDConfigPortLock_Type())
slOTDRMDConfigPortLock.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTDRMDConfigPortLock.setStatus(_A)
_SlOTDRMDConfigCycles_Type=Integer32
_SlOTDRMDConfigCycles_Object=MibTableColumn
slOTDRMDConfigCycles=_SlOTDRMDConfigCycles_Object((1,3,6,1,4,1,4515,1,1,19,1,1,1,10),_SlOTDRMDConfigCycles_Type())
slOTDRMDConfigCycles.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTDRMDConfigCycles.setStatus(_A)
_SlOTDRMDConfigDynamicRange_Type=Integer32
_SlOTDRMDConfigDynamicRange_Object=MibTableColumn
slOTDRMDConfigDynamicRange=_SlOTDRMDConfigDynamicRange_Object((1,3,6,1,4,1,4515,1,1,19,1,1,1,11),_SlOTDRMDConfigDynamicRange_Type())
slOTDRMDConfigDynamicRange.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTDRMDConfigDynamicRange.setStatus(_A)
_SlOTDRPRConfigTable_Object=MibTable
slOTDRPRConfigTable=_SlOTDRPRConfigTable_Object((1,3,6,1,4,1,4515,1,1,19,1,2))
if mibBuilder.loadTexts:slOTDRPRConfigTable.setStatus(_A)
_SlOTDRPRConfigEntry_Object=MibTableRow
slOTDRPRConfigEntry=_SlOTDRPRConfigEntry_Object((1,3,6,1,4,1,4515,1,1,19,1,2,1))
slOTDRPRConfigEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:slOTDRPRConfigEntry.setStatus(_A)
_SlOTDRPRConfigLineIndex_Type=InterfaceIndex
_SlOTDRPRConfigLineIndex_Object=MibTableColumn
slOTDRPRConfigLineIndex=_SlOTDRPRConfigLineIndex_Object((1,3,6,1,4,1,4515,1,1,19,1,2,1,1),_SlOTDRPRConfigLineIndex_Type())
slOTDRPRConfigLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTDRPRConfigLineIndex.setStatus(_A)
_SlOTDRPRConfigAdmin_Type=Integer32
_SlOTDRPRConfigAdmin_Object=MibTableColumn
slOTDRPRConfigAdmin=_SlOTDRPRConfigAdmin_Object((1,3,6,1,4,1,4515,1,1,19,1,2,1,2),_SlOTDRPRConfigAdmin_Type())
slOTDRPRConfigAdmin.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTDRPRConfigAdmin.setStatus(_A)
_SlOTDRPRConfigOper_Type=Integer32
_SlOTDRPRConfigOper_Object=MibTableColumn
slOTDRPRConfigOper=_SlOTDRPRConfigOper_Object((1,3,6,1,4,1,4515,1,1,19,1,2,1,3),_SlOTDRPRConfigOper_Type())
slOTDRPRConfigOper.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTDRPRConfigOper.setStatus(_A)
_SlOTDRPRConfigAlias_Type=DisplayString
_SlOTDRPRConfigAlias_Object=MibTableColumn
slOTDRPRConfigAlias=_SlOTDRPRConfigAlias_Object((1,3,6,1,4,1,4515,1,1,19,1,2,1,4),_SlOTDRPRConfigAlias_Type())
slOTDRPRConfigAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTDRPRConfigAlias.setStatus(_A)
_SlOTDRPRConfigUIOR_Type=Integer32
_SlOTDRPRConfigUIOR_Object=MibTableColumn
slOTDRPRConfigUIOR=_SlOTDRPRConfigUIOR_Object((1,3,6,1,4,1,4515,1,1,19,1,2,1,5),_SlOTDRPRConfigUIOR_Type())
slOTDRPRConfigUIOR.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTDRPRConfigUIOR.setStatus(_A)
_SlOTDRPRConfigTLOS_Type=Integer32
_SlOTDRPRConfigTLOS_Object=MibTableColumn
slOTDRPRConfigTLOS=_SlOTDRPRConfigTLOS_Object((1,3,6,1,4,1,4515,1,1,19,1,2,1,6),_SlOTDRPRConfigTLOS_Type())
slOTDRPRConfigTLOS.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTDRPRConfigTLOS.setStatus(_A)
_SlOTDRPRConfigTREF_Type=Integer32
_SlOTDRPRConfigTREF_Object=MibTableColumn
slOTDRPRConfigTREF=_SlOTDRPRConfigTREF_Object((1,3,6,1,4,1,4515,1,1,19,1,2,1,7),_SlOTDRPRConfigTREF_Type())
slOTDRPRConfigTREF.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTDRPRConfigTREF.setStatus(_A)
_SlOTDRPRConfigMTIM_Type=Integer32
_SlOTDRPRConfigMTIM_Object=MibTableColumn
slOTDRPRConfigMTIM=_SlOTDRPRConfigMTIM_Object((1,3,6,1,4,1,4515,1,1,19,1,2,1,8),_SlOTDRPRConfigMTIM_Type())
slOTDRPRConfigMTIM.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTDRPRConfigMTIM.setStatus(_A)
_SlOTDRPRConfigDIST_Type=Integer32
_SlOTDRPRConfigDIST_Object=MibTableColumn
slOTDRPRConfigDIST=_SlOTDRPRConfigDIST_Object((1,3,6,1,4,1,4515,1,1,19,1,2,1,9),_SlOTDRPRConfigDIST_Type())
slOTDRPRConfigDIST.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTDRPRConfigDIST.setStatus(_A)
_SlOTDRPRConfigPWIDTH_Type=Integer32
_SlOTDRPRConfigPWIDTH_Object=MibTableColumn
slOTDRPRConfigPWIDTH=_SlOTDRPRConfigPWIDTH_Object((1,3,6,1,4,1,4515,1,1,19,1,2,1,10),_SlOTDRPRConfigPWIDTH_Type())
slOTDRPRConfigPWIDTH.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTDRPRConfigPWIDTH.setStatus(_A)
_SlOTDRPRConfigRESOL_Type=Integer32
_SlOTDRPRConfigRESOL_Object=MibTableColumn
slOTDRPRConfigRESOL=_SlOTDRPRConfigRESOL_Object((1,3,6,1,4,1,4515,1,1,19,1,2,1,11),_SlOTDRPRConfigRESOL_Type())
slOTDRPRConfigRESOL.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTDRPRConfigRESOL.setStatus(_A)
_SlOTDRPRConfigTEOF_Type=Integer32
_SlOTDRPRConfigTEOF_Object=MibTableColumn
slOTDRPRConfigTEOF=_SlOTDRPRConfigTEOF_Object((1,3,6,1,4,1,4515,1,1,19,1,2,1,12),_SlOTDRPRConfigTEOF_Type())
slOTDRPRConfigTEOF.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTDRPRConfigTEOF.setStatus(_A)
_SlOTDRPRConfigRefSavRmv_Type=Integer32
_SlOTDRPRConfigRefSavRmv_Object=MibTableColumn
slOTDRPRConfigRefSavRmv=_SlOTDRPRConfigRefSavRmv_Object((1,3,6,1,4,1,4515,1,1,19,1,2,1,13),_SlOTDRPRConfigRefSavRmv_Type())
slOTDRPRConfigRefSavRmv.setMaxAccess(_C)
if mibBuilder.loadTexts:slOTDRPRConfigRefSavRmv.setStatus(_A)
_SlOTDREventTable_Object=MibTable
slOTDREventTable=_SlOTDREventTable_Object((1,3,6,1,4,1,4515,1,1,19,1,3))
if mibBuilder.loadTexts:slOTDREventTable.setStatus(_A)
_SlOTDREventEntry_Object=MibTableRow
slOTDREventEntry=_SlOTDREventEntry_Object((1,3,6,1,4,1,4515,1,1,19,1,3,1))
slOTDREventEntry.setIndexNames((0,_D,_G),(0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:slOTDREventEntry.setStatus(_A)
_SlOTDREventLineIndex_Type=InterfaceIndex
_SlOTDREventLineIndex_Object=MibTableColumn
slOTDREventLineIndex=_SlOTDREventLineIndex_Object((1,3,6,1,4,1,4515,1,1,19,1,3,1,1),_SlOTDREventLineIndex_Type())
slOTDREventLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTDREventLineIndex.setStatus(_A)
_SlOTDREventTableIndex_Type=Integer32
_SlOTDREventTableIndex_Object=MibTableColumn
slOTDREventTableIndex=_SlOTDREventTableIndex_Object((1,3,6,1,4,1,4515,1,1,19,1,3,1,2),_SlOTDREventTableIndex_Type())
slOTDREventTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTDREventTableIndex.setStatus(_A)
_SlOTDREventIndex_Type=Integer32
_SlOTDREventIndex_Object=MibTableColumn
slOTDREventIndex=_SlOTDREventIndex_Object((1,3,6,1,4,1,4515,1,1,19,1,3,1,3),_SlOTDREventIndex_Type())
slOTDREventIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTDREventIndex.setStatus(_A)
_SlOTDREventType_Type=Integer32
_SlOTDREventType_Object=MibTableColumn
slOTDREventType=_SlOTDREventType_Object((1,3,6,1,4,1,4515,1,1,19,1,3,1,4),_SlOTDREventType_Type())
slOTDREventType.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTDREventType.setStatus(_A)
_SlOTDREventDistance_Type=Integer32
_SlOTDREventDistance_Object=MibTableColumn
slOTDREventDistance=_SlOTDREventDistance_Object((1,3,6,1,4,1,4515,1,1,19,1,3,1,5),_SlOTDREventDistance_Type())
slOTDREventDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTDREventDistance.setStatus(_A)
_SlOTDREventReflectance_Type=Integer32
_SlOTDREventReflectance_Object=MibTableColumn
slOTDREventReflectance=_SlOTDREventReflectance_Object((1,3,6,1,4,1,4515,1,1,19,1,3,1,6),_SlOTDREventReflectance_Type())
slOTDREventReflectance.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTDREventReflectance.setStatus(_A)
_SlOTDREventLoss_Type=Integer32
_SlOTDREventLoss_Object=MibTableColumn
slOTDREventLoss=_SlOTDREventLoss_Object((1,3,6,1,4,1,4515,1,1,19,1,3,1,7),_SlOTDREventLoss_Type())
slOTDREventLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTDREventLoss.setStatus(_A)
_SlOTDREventTLoss_Type=Integer32
_SlOTDREventTLoss_Object=MibTableColumn
slOTDREventTLoss=_SlOTDREventTLoss_Object((1,3,6,1,4,1,4515,1,1,19,1,3,1,8),_SlOTDREventTLoss_Type())
slOTDREventTLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:slOTDREventTLoss.setStatus(_A)
_SlOTDRPm_ObjectIdentity=ObjectIdentity
slOTDRPm=_SlOTDRPm_ObjectIdentity((1,3,6,1,4,1,4515,1,1,19,2))
_SlOTDRTraps_ObjectIdentity=ObjectIdentity
slOTDRTraps=_SlOTDRTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,1,19,3))
mibBuilder.exportSymbols(_D,**{'slOTDR':slOTDR,'slOTDRConfig':slOTDRConfig,'slOTDRMDConfigTable':slOTDRMDConfigTable,'slOTDRMDConfigEntry':slOTDRMDConfigEntry,_E:slOTDRMDConfigLineIndex,'slOTDRMDConfigAdminStatus':slOTDRMDConfigAdminStatus,'slOTDRMDConfigOperStatus':slOTDRMDConfigOperStatus,'slOTDRMDConfigPN':slOTDRMDConfigPN,'slOTDRMDConfigSNO':slOTDRMDConfigSNO,'slOTDRMDConfigMF':slOTDRMDConfigMF,'slOTDRMDConfigHWR':slOTDRMDConfigHWR,'slOTDRMDConfigFWR':slOTDRMDConfigFWR,'slOTDRMDConfigPortLock':slOTDRMDConfigPortLock,'slOTDRMDConfigCycles':slOTDRMDConfigCycles,'slOTDRMDConfigDynamicRange':slOTDRMDConfigDynamicRange,'slOTDRPRConfigTable':slOTDRPRConfigTable,'slOTDRPRConfigEntry':slOTDRPRConfigEntry,_F:slOTDRPRConfigLineIndex,'slOTDRPRConfigAdmin':slOTDRPRConfigAdmin,'slOTDRPRConfigOper':slOTDRPRConfigOper,'slOTDRPRConfigAlias':slOTDRPRConfigAlias,'slOTDRPRConfigUIOR':slOTDRPRConfigUIOR,'slOTDRPRConfigTLOS':slOTDRPRConfigTLOS,'slOTDRPRConfigTREF':slOTDRPRConfigTREF,'slOTDRPRConfigMTIM':slOTDRPRConfigMTIM,'slOTDRPRConfigDIST':slOTDRPRConfigDIST,'slOTDRPRConfigPWIDTH':slOTDRPRConfigPWIDTH,'slOTDRPRConfigRESOL':slOTDRPRConfigRESOL,'slOTDRPRConfigTEOF':slOTDRPRConfigTEOF,'slOTDRPRConfigRefSavRmv':slOTDRPRConfigRefSavRmv,'slOTDREventTable':slOTDREventTable,'slOTDREventEntry':slOTDREventEntry,_G:slOTDREventLineIndex,_H:slOTDREventTableIndex,_I:slOTDREventIndex,'slOTDREventType':slOTDREventType,'slOTDREventDistance':slOTDREventDistance,'slOTDREventReflectance':slOTDREventReflectance,'slOTDREventLoss':slOTDREventLoss,'slOTDREventTLoss':slOTDREventTLoss,'slOTDRPm':slOTDRPm,'slOTDRTraps':slOTDRTraps})