_H='slOSChannelIndex'
_G='slOSChannelLineIndex'
_F='slOSPRConfigLineIndex'
_E='slOCMConfigLineIndex'
_D='SL-OSA-MIB'
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
slOSA=ModuleIdentity((1,3,6,1,4,1,4515,1,1,18))
_SlOSAConfig_ObjectIdentity=ObjectIdentity
slOSAConfig=_SlOSAConfig_ObjectIdentity((1,3,6,1,4,1,4515,1,1,18,1))
_SlOCMConfigTable_Object=MibTable
slOCMConfigTable=_SlOCMConfigTable_Object((1,3,6,1,4,1,4515,1,1,18,1,1))
if mibBuilder.loadTexts:slOCMConfigTable.setStatus(_A)
_SlOCMConfigEntry_Object=MibTableRow
slOCMConfigEntry=_SlOCMConfigEntry_Object((1,3,6,1,4,1,4515,1,1,18,1,1,1))
slOCMConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:slOCMConfigEntry.setStatus(_A)
_SlOCMConfigLineIndex_Type=InterfaceIndex
_SlOCMConfigLineIndex_Object=MibTableColumn
slOCMConfigLineIndex=_SlOCMConfigLineIndex_Object((1,3,6,1,4,1,4515,1,1,18,1,1,1,1),_SlOCMConfigLineIndex_Type())
slOCMConfigLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slOCMConfigLineIndex.setStatus(_A)
_SlOCMConfigOperStatus_Type=Integer32
_SlOCMConfigOperStatus_Object=MibTableColumn
slOCMConfigOperStatus=_SlOCMConfigOperStatus_Object((1,3,6,1,4,1,4515,1,1,18,1,1,1,2),_SlOCMConfigOperStatus_Type())
slOCMConfigOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:slOCMConfigOperStatus.setStatus(_A)
_SlOCMConfigTemp_Type=Integer32
_SlOCMConfigTemp_Object=MibTableColumn
slOCMConfigTemp=_SlOCMConfigTemp_Object((1,3,6,1,4,1,4515,1,1,18,1,1,1,3),_SlOCMConfigTemp_Type())
slOCMConfigTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:slOCMConfigTemp.setStatus(_A)
_SlOCMConfigSNO_Type=DisplayString
_SlOCMConfigSNO_Object=MibTableColumn
slOCMConfigSNO=_SlOCMConfigSNO_Object((1,3,6,1,4,1,4515,1,1,18,1,1,1,4),_SlOCMConfigSNO_Type())
slOCMConfigSNO.setMaxAccess(_B)
if mibBuilder.loadTexts:slOCMConfigSNO.setStatus(_A)
_SlOCMConfigMFD_Type=DisplayString
_SlOCMConfigMFD_Object=MibTableColumn
slOCMConfigMFD=_SlOCMConfigMFD_Object((1,3,6,1,4,1,4515,1,1,18,1,1,1,5),_SlOCMConfigMFD_Type())
slOCMConfigMFD.setMaxAccess(_B)
if mibBuilder.loadTexts:slOCMConfigMFD.setStatus(_A)
_SlOCMConfigHWR_Type=DisplayString
_SlOCMConfigHWR_Object=MibTableColumn
slOCMConfigHWR=_SlOCMConfigHWR_Object((1,3,6,1,4,1,4515,1,1,18,1,1,1,6),_SlOCMConfigHWR_Type())
slOCMConfigHWR.setMaxAccess(_B)
if mibBuilder.loadTexts:slOCMConfigHWR.setStatus(_A)
_SlOCMConfigFWR_Type=DisplayString
_SlOCMConfigFWR_Object=MibTableColumn
slOCMConfigFWR=_SlOCMConfigFWR_Object((1,3,6,1,4,1,4515,1,1,18,1,1,1,7),_SlOCMConfigFWR_Type())
slOCMConfigFWR.setMaxAccess(_B)
if mibBuilder.loadTexts:slOCMConfigFWR.setStatus(_A)
_SlOCMConfigPortLock_Type=Integer32
_SlOCMConfigPortLock_Object=MibTableColumn
slOCMConfigPortLock=_SlOCMConfigPortLock_Object((1,3,6,1,4,1,4515,1,1,18,1,1,1,8),_SlOCMConfigPortLock_Type())
slOCMConfigPortLock.setMaxAccess(_C)
if mibBuilder.loadTexts:slOCMConfigPortLock.setStatus(_A)
_SlOCMConfigCycles_Type=Integer32
_SlOCMConfigCycles_Object=MibTableColumn
slOCMConfigCycles=_SlOCMConfigCycles_Object((1,3,6,1,4,1,4515,1,1,18,1,1,1,9),_SlOCMConfigCycles_Type())
slOCMConfigCycles.setMaxAccess(_B)
if mibBuilder.loadTexts:slOCMConfigCycles.setStatus(_A)
_SlOCMConfigPN_Type=DisplayString
_SlOCMConfigPN_Object=MibTableColumn
slOCMConfigPN=_SlOCMConfigPN_Object((1,3,6,1,4,1,4515,1,1,18,1,1,1,10),_SlOCMConfigPN_Type())
slOCMConfigPN.setMaxAccess(_B)
if mibBuilder.loadTexts:slOCMConfigPN.setStatus(_A)
_SlOSPRConfigTable_Object=MibTable
slOSPRConfigTable=_SlOSPRConfigTable_Object((1,3,6,1,4,1,4515,1,1,18,1,2))
if mibBuilder.loadTexts:slOSPRConfigTable.setStatus(_A)
_SlOSPRConfigEntry_Object=MibTableRow
slOSPRConfigEntry=_SlOSPRConfigEntry_Object((1,3,6,1,4,1,4515,1,1,18,1,2,1))
slOSPRConfigEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:slOSPRConfigEntry.setStatus(_A)
_SlOSPRConfigLineIndex_Type=InterfaceIndex
_SlOSPRConfigLineIndex_Object=MibTableColumn
slOSPRConfigLineIndex=_SlOSPRConfigLineIndex_Object((1,3,6,1,4,1,4515,1,1,18,1,2,1,1),_SlOSPRConfigLineIndex_Type())
slOSPRConfigLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slOSPRConfigLineIndex.setStatus(_A)
_SlOSPRConfigAdmin_Type=Integer32
_SlOSPRConfigAdmin_Object=MibTableColumn
slOSPRConfigAdmin=_SlOSPRConfigAdmin_Object((1,3,6,1,4,1,4515,1,1,18,1,2,1,2),_SlOSPRConfigAdmin_Type())
slOSPRConfigAdmin.setMaxAccess(_C)
if mibBuilder.loadTexts:slOSPRConfigAdmin.setStatus(_A)
_SlOSPRConfigOper_Type=Integer32
_SlOSPRConfigOper_Object=MibTableColumn
slOSPRConfigOper=_SlOSPRConfigOper_Object((1,3,6,1,4,1,4515,1,1,18,1,2,1,3),_SlOSPRConfigOper_Type())
slOSPRConfigOper.setMaxAccess(_B)
if mibBuilder.loadTexts:slOSPRConfigOper.setStatus(_A)
_SlOSPRConfigAlias_Type=DisplayString
_SlOSPRConfigAlias_Object=MibTableColumn
slOSPRConfigAlias=_SlOSPRConfigAlias_Object((1,3,6,1,4,1,4515,1,1,18,1,2,1,4),_SlOSPRConfigAlias_Type())
slOSPRConfigAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:slOSPRConfigAlias.setStatus(_A)
_SlOSPRConfigGrid_Type=Integer32
_SlOSPRConfigGrid_Object=MibTableColumn
slOSPRConfigGrid=_SlOSPRConfigGrid_Object((1,3,6,1,4,1,4515,1,1,18,1,2,1,5),_SlOSPRConfigGrid_Type())
slOSPRConfigGrid.setMaxAccess(_C)
if mibBuilder.loadTexts:slOSPRConfigGrid.setStatus(_A)
_SlOSPRConfigLossDetectThresh_Type=Integer32
_SlOSPRConfigLossDetectThresh_Object=MibTableColumn
slOSPRConfigLossDetectThresh=_SlOSPRConfigLossDetectThresh_Object((1,3,6,1,4,1,4515,1,1,18,1,2,1,6),_SlOSPRConfigLossDetectThresh_Type())
slOSPRConfigLossDetectThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:slOSPRConfigLossDetectThresh.setStatus(_A)
_SlOSPRConfigRefreshTime_Type=Integer32
_SlOSPRConfigRefreshTime_Object=MibTableColumn
slOSPRConfigRefreshTime=_SlOSPRConfigRefreshTime_Object((1,3,6,1,4,1,4515,1,1,18,1,2,1,7),_SlOSPRConfigRefreshTime_Type())
slOSPRConfigRefreshTime.setMaxAccess(_C)
if mibBuilder.loadTexts:slOSPRConfigRefreshTime.setStatus(_A)
_SlOSPRConfigRestoreDefaults_Type=Integer32
_SlOSPRConfigRestoreDefaults_Object=MibTableColumn
slOSPRConfigRestoreDefaults=_SlOSPRConfigRestoreDefaults_Object((1,3,6,1,4,1,4515,1,1,18,1,2,1,8),_SlOSPRConfigRestoreDefaults_Type())
slOSPRConfigRestoreDefaults.setMaxAccess(_C)
if mibBuilder.loadTexts:slOSPRConfigRestoreDefaults.setStatus(_A)
_SlOSPRConfigTR_Type=Integer32
_SlOSPRConfigTR_Object=MibTableColumn
slOSPRConfigTR=_SlOSPRConfigTR_Object((1,3,6,1,4,1,4515,1,1,18,1,2,1,9),_SlOSPRConfigTR_Type())
slOSPRConfigTR.setMaxAccess(_C)
if mibBuilder.loadTexts:slOSPRConfigTR.setStatus(_A)
_SlOSPRConfigDL_Type=Integer32
_SlOSPRConfigDL_Object=MibTableColumn
slOSPRConfigDL=_SlOSPRConfigDL_Object((1,3,6,1,4,1,4515,1,1,18,1,2,1,10),_SlOSPRConfigDL_Type())
slOSPRConfigDL.setMaxAccess(_B)
if mibBuilder.loadTexts:slOSPRConfigDL.setStatus(_A)
_SlOSPRConfigDU_Type=Integer32
_SlOSPRConfigDU_Object=MibTableColumn
slOSPRConfigDU=_SlOSPRConfigDU_Object((1,3,6,1,4,1,4515,1,1,18,1,2,1,11),_SlOSPRConfigDU_Type())
slOSPRConfigDU.setMaxAccess(_B)
if mibBuilder.loadTexts:slOSPRConfigDU.setStatus(_A)
_SlOSPRConfigNL_Type=Integer32
_SlOSPRConfigNL_Object=MibTableColumn
slOSPRConfigNL=_SlOSPRConfigNL_Object((1,3,6,1,4,1,4515,1,1,18,1,2,1,12),_SlOSPRConfigNL_Type())
slOSPRConfigNL.setMaxAccess(_B)
if mibBuilder.loadTexts:slOSPRConfigNL.setStatus(_A)
_SlOSPRConfigNU_Type=Integer32
_SlOSPRConfigNU_Object=MibTableColumn
slOSPRConfigNU=_SlOSPRConfigNU_Object((1,3,6,1,4,1,4515,1,1,18,1,2,1,13),_SlOSPRConfigNU_Type())
slOSPRConfigNU.setMaxAccess(_B)
if mibBuilder.loadTexts:slOSPRConfigNU.setStatus(_A)
_SlOSPRConfigBWX_Type=Integer32
_SlOSPRConfigBWX_Object=MibTableColumn
slOSPRConfigBWX=_SlOSPRConfigBWX_Object((1,3,6,1,4,1,4515,1,1,18,1,2,1,14),_SlOSPRConfigBWX_Type())
slOSPRConfigBWX.setMaxAccess(_B)
if mibBuilder.loadTexts:slOSPRConfigBWX.setStatus(_A)
_SlOSPRConfigNTR_Type=Integer32
_SlOSPRConfigNTR_Object=MibTableColumn
slOSPRConfigNTR=_SlOSPRConfigNTR_Object((1,3,6,1,4,1,4515,1,1,18,1,2,1,15),_SlOSPRConfigNTR_Type())
slOSPRConfigNTR.setMaxAccess(_B)
if mibBuilder.loadTexts:slOSPRConfigNTR.setStatus(_A)
_SlOSPRConfigRBW_Type=Integer32
_SlOSPRConfigRBW_Object=MibTableColumn
slOSPRConfigRBW=_SlOSPRConfigRBW_Object((1,3,6,1,4,1,4515,1,1,18,1,2,1,16),_SlOSPRConfigRBW_Type())
slOSPRConfigRBW.setMaxAccess(_B)
if mibBuilder.loadTexts:slOSPRConfigRBW.setStatus(_A)
_SlOSPRConfigBWT_Type=Integer32
_SlOSPRConfigBWT_Object=MibTableColumn
slOSPRConfigBWT=_SlOSPRConfigBWT_Object((1,3,6,1,4,1,4515,1,1,18,1,2,1,17),_SlOSPRConfigBWT_Type())
slOSPRConfigBWT.setMaxAccess(_B)
if mibBuilder.loadTexts:slOSPRConfigBWT.setStatus(_A)
_SlOSChannelTable_Object=MibTable
slOSChannelTable=_SlOSChannelTable_Object((1,3,6,1,4,1,4515,1,1,18,1,3))
if mibBuilder.loadTexts:slOSChannelTable.setStatus(_A)
_SlOSChannelEntry_Object=MibTableRow
slOSChannelEntry=_SlOSChannelEntry_Object((1,3,6,1,4,1,4515,1,1,18,1,3,1))
slOSChannelEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:slOSChannelEntry.setStatus(_A)
_SlOSChannelLineIndex_Type=InterfaceIndex
_SlOSChannelLineIndex_Object=MibTableColumn
slOSChannelLineIndex=_SlOSChannelLineIndex_Object((1,3,6,1,4,1,4515,1,1,18,1,3,1,1),_SlOSChannelLineIndex_Type())
slOSChannelLineIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slOSChannelLineIndex.setStatus(_A)
_SlOSChannelIndex_Type=Integer32
_SlOSChannelIndex_Object=MibTableColumn
slOSChannelIndex=_SlOSChannelIndex_Object((1,3,6,1,4,1,4515,1,1,18,1,3,1,2),_SlOSChannelIndex_Type())
slOSChannelIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:slOSChannelIndex.setStatus(_A)
_SlOSChannelFR_Type=Integer32
_SlOSChannelFR_Object=MibTableColumn
slOSChannelFR=_SlOSChannelFR_Object((1,3,6,1,4,1,4515,1,1,18,1,3,1,3),_SlOSChannelFR_Type())
slOSChannelFR.setMaxAccess(_B)
if mibBuilder.loadTexts:slOSChannelFR.setStatus(_A)
_SlOSChannelPO_Type=Integer32
_SlOSChannelPO_Object=MibTableColumn
slOSChannelPO=_SlOSChannelPO_Object((1,3,6,1,4,1,4515,1,1,18,1,3,1,4),_SlOSChannelPO_Type())
slOSChannelPO.setMaxAccess(_B)
if mibBuilder.loadTexts:slOSChannelPO.setStatus(_A)
_SlOSChannelBW_Type=Integer32
_SlOSChannelBW_Object=MibTableColumn
slOSChannelBW=_SlOSChannelBW_Object((1,3,6,1,4,1,4515,1,1,18,1,3,1,5),_SlOSChannelBW_Type())
slOSChannelBW.setMaxAccess(_B)
if mibBuilder.loadTexts:slOSChannelBW.setStatus(_A)
_SlOSChannelOSNR_Type=Integer32
_SlOSChannelOSNR_Object=MibTableColumn
slOSChannelOSNR=_SlOSChannelOSNR_Object((1,3,6,1,4,1,4515,1,1,18,1,3,1,6),_SlOSChannelOSNR_Type())
slOSChannelOSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:slOSChannelOSNR.setStatus(_A)
_SlOSAPm_ObjectIdentity=ObjectIdentity
slOSAPm=_SlOSAPm_ObjectIdentity((1,3,6,1,4,1,4515,1,1,18,2))
_SlOSATraps_ObjectIdentity=ObjectIdentity
slOSATraps=_SlOSATraps_ObjectIdentity((1,3,6,1,4,1,4515,1,1,18,3))
mibBuilder.exportSymbols(_D,**{'slOSA':slOSA,'slOSAConfig':slOSAConfig,'slOCMConfigTable':slOCMConfigTable,'slOCMConfigEntry':slOCMConfigEntry,_E:slOCMConfigLineIndex,'slOCMConfigOperStatus':slOCMConfigOperStatus,'slOCMConfigTemp':slOCMConfigTemp,'slOCMConfigSNO':slOCMConfigSNO,'slOCMConfigMFD':slOCMConfigMFD,'slOCMConfigHWR':slOCMConfigHWR,'slOCMConfigFWR':slOCMConfigFWR,'slOCMConfigPortLock':slOCMConfigPortLock,'slOCMConfigCycles':slOCMConfigCycles,'slOCMConfigPN':slOCMConfigPN,'slOSPRConfigTable':slOSPRConfigTable,'slOSPRConfigEntry':slOSPRConfigEntry,_F:slOSPRConfigLineIndex,'slOSPRConfigAdmin':slOSPRConfigAdmin,'slOSPRConfigOper':slOSPRConfigOper,'slOSPRConfigAlias':slOSPRConfigAlias,'slOSPRConfigGrid':slOSPRConfigGrid,'slOSPRConfigLossDetectThresh':slOSPRConfigLossDetectThresh,'slOSPRConfigRefreshTime':slOSPRConfigRefreshTime,'slOSPRConfigRestoreDefaults':slOSPRConfigRestoreDefaults,'slOSPRConfigTR':slOSPRConfigTR,'slOSPRConfigDL':slOSPRConfigDL,'slOSPRConfigDU':slOSPRConfigDU,'slOSPRConfigNL':slOSPRConfigNL,'slOSPRConfigNU':slOSPRConfigNU,'slOSPRConfigBWX':slOSPRConfigBWX,'slOSPRConfigNTR':slOSPRConfigNTR,'slOSPRConfigRBW':slOSPRConfigRBW,'slOSPRConfigBWT':slOSPRConfigBWT,'slOSChannelTable':slOSChannelTable,'slOSChannelEntry':slOSChannelEntry,_G:slOSChannelLineIndex,_H:slOSChannelIndex,'slOSChannelFR':slOSChannelFR,'slOSChannelPO':slOSChannelPO,'slOSChannelBW':slOSChannelBW,'slOSChannelOSNR':slOSChannelOSNR,'slOSAPm':slOSAPm,'slOSATraps':slOSATraps})