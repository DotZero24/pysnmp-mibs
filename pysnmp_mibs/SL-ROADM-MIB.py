_H='slROCHConfigLineIndex'
_G='slWSSConfigLineIndex'
_F='SL-ROADM-MIB'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
slService,=mibBuilder.importSymbols('SL-NE-MIB','slService')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_E,'PhysAddress','TextualConvention','TruthValue')
slROADM=ModuleIdentity((1,3,6,1,4,1,4515,1,1,16))
class ROCHProvisioningType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('exp',2),('add',3)))
_SlROADMConfig_ObjectIdentity=ObjectIdentity
slROADMConfig=_SlROADMConfig_ObjectIdentity((1,3,6,1,4,1,4515,1,1,16,1))
_SlWSSConfigTable_Object=MibTable
slWSSConfigTable=_SlWSSConfigTable_Object((1,3,6,1,4,1,4515,1,1,16,1,1))
if mibBuilder.loadTexts:slWSSConfigTable.setStatus(_A)
_SlWSSConfigEntry_Object=MibTableRow
slWSSConfigEntry=_SlWSSConfigEntry_Object((1,3,6,1,4,1,4515,1,1,16,1,1,1))
slWSSConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:slWSSConfigEntry.setStatus(_A)
_SlWSSConfigLineIndex_Type=InterfaceIndex
_SlWSSConfigLineIndex_Object=MibTableColumn
slWSSConfigLineIndex=_SlWSSConfigLineIndex_Object((1,3,6,1,4,1,4515,1,1,16,1,1,1,1),_SlWSSConfigLineIndex_Type())
slWSSConfigLineIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:slWSSConfigLineIndex.setStatus(_A)
_SlWSSConfigOperStatus_Type=Integer32
_SlWSSConfigOperStatus_Object=MibTableColumn
slWSSConfigOperStatus=_SlWSSConfigOperStatus_Object((1,3,6,1,4,1,4515,1,1,16,1,1,1,2),_SlWSSConfigOperStatus_Type())
slWSSConfigOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:slWSSConfigOperStatus.setStatus(_A)
_SlWSSConfigSwitchTemp_Type=Integer32
_SlWSSConfigSwitchTemp_Object=MibTableColumn
slWSSConfigSwitchTemp=_SlWSSConfigSwitchTemp_Object((1,3,6,1,4,1,4515,1,1,16,1,1,1,3),_SlWSSConfigSwitchTemp_Type())
slWSSConfigSwitchTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:slWSSConfigSwitchTemp.setStatus(_A)
_SlWSSConfigBoardTemp_Type=Integer32
_SlWSSConfigBoardTemp_Object=MibTableColumn
slWSSConfigBoardTemp=_SlWSSConfigBoardTemp_Object((1,3,6,1,4,1,4515,1,1,16,1,1,1,4),_SlWSSConfigBoardTemp_Type())
slWSSConfigBoardTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:slWSSConfigBoardTemp.setStatus(_A)
_SlWSSConfigCaseTemp_Type=Integer32
_SlWSSConfigCaseTemp_Object=MibTableColumn
slWSSConfigCaseTemp=_SlWSSConfigCaseTemp_Object((1,3,6,1,4,1,4515,1,1,16,1,1,1,5),_SlWSSConfigCaseTemp_Type())
slWSSConfigCaseTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:slWSSConfigCaseTemp.setStatus(_A)
_SlWSSConfigUptime_Type=Integer32
_SlWSSConfigUptime_Object=MibTableColumn
slWSSConfigUptime=_SlWSSConfigUptime_Object((1,3,6,1,4,1,4515,1,1,16,1,1,1,6),_SlWSSConfigUptime_Type())
slWSSConfigUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:slWSSConfigUptime.setStatus(_A)
_SlWSSConfigComFirstWl_Type=Integer32
_SlWSSConfigComFirstWl_Object=MibTableColumn
slWSSConfigComFirstWl=_SlWSSConfigComFirstWl_Object((1,3,6,1,4,1,4515,1,1,16,1,1,1,7),_SlWSSConfigComFirstWl_Type())
slWSSConfigComFirstWl.setMaxAccess(_B)
if mibBuilder.loadTexts:slWSSConfigComFirstWl.setStatus(_A)
_SlWSSConfigComChCount_Type=Integer32
_SlWSSConfigComChCount_Object=MibTableColumn
slWSSConfigComChCount=_SlWSSConfigComChCount_Object((1,3,6,1,4,1,4515,1,1,16,1,1,1,8),_SlWSSConfigComChCount_Type())
slWSSConfigComChCount.setMaxAccess(_B)
if mibBuilder.loadTexts:slWSSConfigComChCount.setStatus(_A)
_SlWSSConfigPowerLevel_Type=Integer32
_SlWSSConfigPowerLevel_Object=MibTableColumn
slWSSConfigPowerLevel=_SlWSSConfigPowerLevel_Object((1,3,6,1,4,1,4515,1,1,16,1,1,1,9),_SlWSSConfigPowerLevel_Type())
slWSSConfigPowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:slWSSConfigPowerLevel.setStatus(_A)
_SlWSSConfigAttenLevel_Type=Integer32
_SlWSSConfigAttenLevel_Object=MibTableColumn
slWSSConfigAttenLevel=_SlWSSConfigAttenLevel_Object((1,3,6,1,4,1,4515,1,1,16,1,1,1,10),_SlWSSConfigAttenLevel_Type())
slWSSConfigAttenLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:slWSSConfigAttenLevel.setStatus(_A)
_SlWSSConfigEqualizationThreshLevel_Type=Integer32
_SlWSSConfigEqualizationThreshLevel_Object=MibTableColumn
slWSSConfigEqualizationThreshLevel=_SlWSSConfigEqualizationThreshLevel_Object((1,3,6,1,4,1,4515,1,1,16,1,1,1,11),_SlWSSConfigEqualizationThreshLevel_Type())
slWSSConfigEqualizationThreshLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:slWSSConfigEqualizationThreshLevel.setStatus(_A)
class _SlWSSConfigEqualizationMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('manual',1),('auto',2)))
_SlWSSConfigEqualizationMethod_Type.__name__=_D
_SlWSSConfigEqualizationMethod_Object=MibTableColumn
slWSSConfigEqualizationMethod=_SlWSSConfigEqualizationMethod_Object((1,3,6,1,4,1,4515,1,1,16,1,1,1,12),_SlWSSConfigEqualizationMethod_Type())
slWSSConfigEqualizationMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:slWSSConfigEqualizationMethod.setStatus(_A)
class _SlWSSConfigSpacing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('s100G',1),('s50G',2)))
_SlWSSConfigSpacing_Type.__name__=_D
_SlWSSConfigSpacing_Object=MibTableColumn
slWSSConfigSpacing=_SlWSSConfigSpacing_Object((1,3,6,1,4,1,4515,1,1,16,1,1,1,13),_SlWSSConfigSpacing_Type())
slWSSConfigSpacing.setMaxAccess(_C)
if mibBuilder.loadTexts:slWSSConfigSpacing.setStatus(_A)
_SlROCHConfigTable_Object=MibTable
slROCHConfigTable=_SlROCHConfigTable_Object((1,3,6,1,4,1,4515,1,1,16,1,2))
if mibBuilder.loadTexts:slROCHConfigTable.setStatus(_A)
_SlROCHConfigEntry_Object=MibTableRow
slROCHConfigEntry=_SlROCHConfigEntry_Object((1,3,6,1,4,1,4515,1,1,16,1,2,1))
slROCHConfigEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:slROCHConfigEntry.setStatus(_A)
_SlROCHConfigLineIndex_Type=InterfaceIndex
_SlROCHConfigLineIndex_Object=MibTableColumn
slROCHConfigLineIndex=_SlROCHConfigLineIndex_Object((1,3,6,1,4,1,4515,1,1,16,1,2,1,1),_SlROCHConfigLineIndex_Type())
slROCHConfigLineIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:slROCHConfigLineIndex.setStatus(_A)
_SlROCHConfigProvisioning_Type=ROCHProvisioningType
_SlROCHConfigProvisioning_Object=MibTableColumn
slROCHConfigProvisioning=_SlROCHConfigProvisioning_Object((1,3,6,1,4,1,4515,1,1,16,1,2,1,2),_SlROCHConfigProvisioning_Type())
slROCHConfigProvisioning.setMaxAccess(_B)
if mibBuilder.loadTexts:slROCHConfigProvisioning.setStatus(_A)
_SlROCHConfigInPowerLevel_Type=Integer32
_SlROCHConfigInPowerLevel_Object=MibTableColumn
slROCHConfigInPowerLevel=_SlROCHConfigInPowerLevel_Object((1,3,6,1,4,1,4515,1,1,16,1,2,1,3),_SlROCHConfigInPowerLevel_Type())
slROCHConfigInPowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:slROCHConfigInPowerLevel.setStatus(_A)
_SlROCHConfigOutPowerLevel_Type=Integer32
_SlROCHConfigOutPowerLevel_Object=MibTableColumn
slROCHConfigOutPowerLevel=_SlROCHConfigOutPowerLevel_Object((1,3,6,1,4,1,4515,1,1,16,1,2,1,4),_SlROCHConfigOutPowerLevel_Type())
slROCHConfigOutPowerLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:slROCHConfigOutPowerLevel.setStatus(_A)
_SlROCHConfigChannelDetect_Type=Integer32
_SlROCHConfigChannelDetect_Object=MibTableColumn
slROCHConfigChannelDetect=_SlROCHConfigChannelDetect_Object((1,3,6,1,4,1,4515,1,1,16,1,2,1,5),_SlROCHConfigChannelDetect_Type())
slROCHConfigChannelDetect.setMaxAccess(_C)
if mibBuilder.loadTexts:slROCHConfigChannelDetect.setStatus(_A)
_SlROCHConfigChPowerFailHighThresh_Type=Integer32
_SlROCHConfigChPowerFailHighThresh_Object=MibTableColumn
slROCHConfigChPowerFailHighThresh=_SlROCHConfigChPowerFailHighThresh_Object((1,3,6,1,4,1,4515,1,1,16,1,2,1,6),_SlROCHConfigChPowerFailHighThresh_Type())
slROCHConfigChPowerFailHighThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:slROCHConfigChPowerFailHighThresh.setStatus(_A)
_SlROCHConfigChPowerFailLowThresh_Type=Integer32
_SlROCHConfigChPowerFailLowThresh_Object=MibTableColumn
slROCHConfigChPowerFailLowThresh=_SlROCHConfigChPowerFailLowThresh_Object((1,3,6,1,4,1,4515,1,1,16,1,2,1,7),_SlROCHConfigChPowerFailLowThresh_Type())
slROCHConfigChPowerFailLowThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:slROCHConfigChPowerFailLowThresh.setStatus(_A)
_SlROCHConfigChPowerDegHighThresh_Type=Integer32
_SlROCHConfigChPowerDegHighThresh_Object=MibTableColumn
slROCHConfigChPowerDegHighThresh=_SlROCHConfigChPowerDegHighThresh_Object((1,3,6,1,4,1,4515,1,1,16,1,2,1,8),_SlROCHConfigChPowerDegHighThresh_Type())
slROCHConfigChPowerDegHighThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:slROCHConfigChPowerDegHighThresh.setStatus(_A)
_SlROCHConfigChPowerDegLowThresh_Type=Integer32
_SlROCHConfigChPowerDegLowThresh_Object=MibTableColumn
slROCHConfigChPowerDegLowThresh=_SlROCHConfigChPowerDegLowThresh_Object((1,3,6,1,4,1,4515,1,1,16,1,2,1,9),_SlROCHConfigChPowerDegLowThresh_Type())
slROCHConfigChPowerDegLowThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:slROCHConfigChPowerDegLowThresh.setStatus(_A)
_SlROCHConfigChPowerHystHighThresh_Type=Integer32
_SlROCHConfigChPowerHystHighThresh_Object=MibTableColumn
slROCHConfigChPowerHystHighThresh=_SlROCHConfigChPowerHystHighThresh_Object((1,3,6,1,4,1,4515,1,1,16,1,2,1,10),_SlROCHConfigChPowerHystHighThresh_Type())
slROCHConfigChPowerHystHighThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:slROCHConfigChPowerHystHighThresh.setStatus(_A)
_SlROCHConfigChPowerHystLowThresh_Type=Integer32
_SlROCHConfigChPowerHystLowThresh_Object=MibTableColumn
slROCHConfigChPowerHystLowThresh=_SlROCHConfigChPowerHystLowThresh_Object((1,3,6,1,4,1,4515,1,1,16,1,2,1,11),_SlROCHConfigChPowerHystLowThresh_Type())
slROCHConfigChPowerHystLowThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:slROCHConfigChPowerHystLowThresh.setStatus(_A)
class _SlROCHConfigChAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SlROCHConfigChAlias_Type.__name__=_E
_SlROCHConfigChAlias_Object=MibTableColumn
slROCHConfigChAlias=_SlROCHConfigChAlias_Object((1,3,6,1,4,1,4515,1,1,16,1,2,1,12),_SlROCHConfigChAlias_Type())
slROCHConfigChAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:slROCHConfigChAlias.setStatus(_A)
class _SlROCHConfigChAliasSmm_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SlROCHConfigChAliasSmm_Type.__name__=_E
_SlROCHConfigChAliasSmm_Object=MibTableColumn
slROCHConfigChAliasSmm=_SlROCHConfigChAliasSmm_Object((1,3,6,1,4,1,4515,1,1,16,1,2,1,13),_SlROCHConfigChAliasSmm_Type())
slROCHConfigChAliasSmm.setMaxAccess(_B)
if mibBuilder.loadTexts:slROCHConfigChAliasSmm.setStatus(_A)
_SlROCHConfigProvisioningNew_Type=Integer32
_SlROCHConfigProvisioningNew_Object=MibTableColumn
slROCHConfigProvisioningNew=_SlROCHConfigProvisioningNew_Object((1,3,6,1,4,1,4515,1,1,16,1,2,1,14),_SlROCHConfigProvisioningNew_Type())
slROCHConfigProvisioningNew.setMaxAccess(_B)
if mibBuilder.loadTexts:slROCHConfigProvisioningNew.setStatus(_A)
_SlROADMPm_ObjectIdentity=ObjectIdentity
slROADMPm=_SlROADMPm_ObjectIdentity((1,3,6,1,4,1,4515,1,1,16,2))
_SlROADMTraps_ObjectIdentity=ObjectIdentity
slROADMTraps=_SlROADMTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,1,16,3))
mibBuilder.exportSymbols(_F,**{'ROCHProvisioningType':ROCHProvisioningType,'slROADM':slROADM,'slROADMConfig':slROADMConfig,'slWSSConfigTable':slWSSConfigTable,'slWSSConfigEntry':slWSSConfigEntry,_G:slWSSConfigLineIndex,'slWSSConfigOperStatus':slWSSConfigOperStatus,'slWSSConfigSwitchTemp':slWSSConfigSwitchTemp,'slWSSConfigBoardTemp':slWSSConfigBoardTemp,'slWSSConfigCaseTemp':slWSSConfigCaseTemp,'slWSSConfigUptime':slWSSConfigUptime,'slWSSConfigComFirstWl':slWSSConfigComFirstWl,'slWSSConfigComChCount':slWSSConfigComChCount,'slWSSConfigPowerLevel':slWSSConfigPowerLevel,'slWSSConfigAttenLevel':slWSSConfigAttenLevel,'slWSSConfigEqualizationThreshLevel':slWSSConfigEqualizationThreshLevel,'slWSSConfigEqualizationMethod':slWSSConfigEqualizationMethod,'slWSSConfigSpacing':slWSSConfigSpacing,'slROCHConfigTable':slROCHConfigTable,'slROCHConfigEntry':slROCHConfigEntry,_H:slROCHConfigLineIndex,'slROCHConfigProvisioning':slROCHConfigProvisioning,'slROCHConfigInPowerLevel':slROCHConfigInPowerLevel,'slROCHConfigOutPowerLevel':slROCHConfigOutPowerLevel,'slROCHConfigChannelDetect':slROCHConfigChannelDetect,'slROCHConfigChPowerFailHighThresh':slROCHConfigChPowerFailHighThresh,'slROCHConfigChPowerFailLowThresh':slROCHConfigChPowerFailLowThresh,'slROCHConfigChPowerDegHighThresh':slROCHConfigChPowerDegHighThresh,'slROCHConfigChPowerDegLowThresh':slROCHConfigChPowerDegLowThresh,'slROCHConfigChPowerHystHighThresh':slROCHConfigChPowerHystHighThresh,'slROCHConfigChPowerHystLowThresh':slROCHConfigChPowerHystLowThresh,'slROCHConfigChAlias':slROCHConfigChAlias,'slROCHConfigChAliasSmm':slROCHConfigChAliasSmm,'slROCHConfigProvisioningNew':slROCHConfigProvisioningNew,'slROADMPm':slROADMPm,'slROADMTraps':slROADMTraps})