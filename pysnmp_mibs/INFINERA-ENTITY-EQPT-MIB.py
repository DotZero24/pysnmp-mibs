_n='eqptGroup'
_m='eqptRedundancyStatus'
_l='eqptFruInsertionDate'
_k='eqptUniversalSlotUsage'
_j='eqptPON'
_i='eqptFirmwareVersion'
_h='eqptHardwareVersion'
_g='eqptVendorId'
_f='eqptManufacturedDate'
_e='eqptSerialNumber'
_d='eqptPartNumber'
_c='eqptOutletTemp'
_b='eqptInletTemp'
_a='eqptLastRebootReason'
_Z='eqptLastRebootTime'
_Y='eqptEqptMaxPowerDraw'
_X='eqptSAFpgaUpgradeFlag'
_W='eqptSAFpgaUpgradePending'
_V='eqptCLEI'
_U='eqptBaseCircuitPackType'
_T='eqptInstalledEqptType'
_S='eqptProvEqptType'
_R='eqptAlarmInhibitState'
_Q='eqptOpStateQualifierList'
_P='eqptAlarmReportControl'
_O='eqptAvailabilityState'
_N='eqptOperationalState'
_M='eqptAdministrativeState'
_L='eqptLabel'
_K='eqptMoId'
_J='degrees Celcius'
_I='InfnArc'
_H='InfnAdminState'
_G='entPhysicalIndex'
_F='ENTITY-MIB'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='INFINERA-ENTITY-EQPT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_F,_G)
commonEquipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','commonEquipment')
FloatArbitraryPrecision,FloatHundredths,FloatTenths,InfnAdminState,InfnArc,InfnAvailabilityState,InfnCircuitPackType,InfnCorrelatedRedunStatus,InfnEqptType,InfnLastRebootReason,InfnOperationalState,InfnOpsQualifierList=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatArbitraryPrecision','FloatHundredths','FloatTenths',_H,_I,'InfnAvailabilityState','InfnCircuitPackType','InfnCorrelatedRedunStatus','InfnEqptType','InfnLastRebootReason','InfnOperationalState','InfnOpsQualifierList')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
eqptMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,1,9,1))
_EqptTable_Object=MibTable
eqptTable=_EqptTable_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1))
if mibBuilder.loadTexts:eqptTable.setStatus(_A)
_EqptEntry_Object=MibTableRow
eqptEntry=_EqptEntry_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1))
eqptEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:eqptEntry.setStatus(_A)
_EqptMoId_Type=DisplayString
_EqptMoId_Object=MibTableColumn
eqptMoId=_EqptMoId_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,1),_EqptMoId_Type())
eqptMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptMoId.setStatus(_A)
_EqptLabel_Type=DisplayString
_EqptLabel_Object=MibTableColumn
eqptLabel=_EqptLabel_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,2),_EqptLabel_Type())
eqptLabel.setMaxAccess(_E)
if mibBuilder.loadTexts:eqptLabel.setStatus(_A)
class _EqptAdministrativeState_Type(InfnAdminState):defaultValue=3
_EqptAdministrativeState_Type.__name__=_H
_EqptAdministrativeState_Object=MibTableColumn
eqptAdministrativeState=_EqptAdministrativeState_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,3),_EqptAdministrativeState_Type())
eqptAdministrativeState.setMaxAccess(_E)
if mibBuilder.loadTexts:eqptAdministrativeState.setStatus(_A)
_EqptOperationalState_Type=InfnOperationalState
_EqptOperationalState_Object=MibTableColumn
eqptOperationalState=_EqptOperationalState_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,4),_EqptOperationalState_Type())
eqptOperationalState.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptOperationalState.setStatus(_A)
_EqptAvailabilityState_Type=InfnAvailabilityState
_EqptAvailabilityState_Object=MibTableColumn
eqptAvailabilityState=_EqptAvailabilityState_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,5),_EqptAvailabilityState_Type())
eqptAvailabilityState.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptAvailabilityState.setStatus(_A)
class _EqptAlarmReportControl_Type(InfnArc):defaultValue=1
_EqptAlarmReportControl_Type.__name__=_I
_EqptAlarmReportControl_Object=MibTableColumn
eqptAlarmReportControl=_EqptAlarmReportControl_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,6),_EqptAlarmReportControl_Type())
eqptAlarmReportControl.setMaxAccess(_E)
if mibBuilder.loadTexts:eqptAlarmReportControl.setStatus(_A)
_EqptOpStateQualifierList_Type=InfnOpsQualifierList
_EqptOpStateQualifierList_Object=MibTableColumn
eqptOpStateQualifierList=_EqptOpStateQualifierList_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,7),_EqptOpStateQualifierList_Type())
eqptOpStateQualifierList.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptOpStateQualifierList.setStatus(_A)
_EqptAlarmInhibitState_Type=InfnArc
_EqptAlarmInhibitState_Object=MibTableColumn
eqptAlarmInhibitState=_EqptAlarmInhibitState_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,8),_EqptAlarmInhibitState_Type())
eqptAlarmInhibitState.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptAlarmInhibitState.setStatus(_A)
_EqptProvEqptType_Type=InfnEqptType
_EqptProvEqptType_Object=MibTableColumn
eqptProvEqptType=_EqptProvEqptType_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,9),_EqptProvEqptType_Type())
eqptProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptProvEqptType.setStatus(_A)
_EqptInstalledEqptType_Type=InfnEqptType
_EqptInstalledEqptType_Object=MibTableColumn
eqptInstalledEqptType=_EqptInstalledEqptType_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,10),_EqptInstalledEqptType_Type())
eqptInstalledEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptInstalledEqptType.setStatus(_A)
_EqptBaseCircuitPackType_Type=InfnCircuitPackType
_EqptBaseCircuitPackType_Object=MibTableColumn
eqptBaseCircuitPackType=_EqptBaseCircuitPackType_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,11),_EqptBaseCircuitPackType_Type())
eqptBaseCircuitPackType.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptBaseCircuitPackType.setStatus(_A)
_EqptCLEI_Type=DisplayString
_EqptCLEI_Object=MibTableColumn
eqptCLEI=_EqptCLEI_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,12),_EqptCLEI_Type())
eqptCLEI.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptCLEI.setStatus(_A)
class _EqptSAFpgaUpgradePending_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('sa',2)))
_EqptSAFpgaUpgradePending_Type.__name__=_D
_EqptSAFpgaUpgradePending_Object=MibTableColumn
eqptSAFpgaUpgradePending=_EqptSAFpgaUpgradePending_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,13),_EqptSAFpgaUpgradePending_Type())
eqptSAFpgaUpgradePending.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptSAFpgaUpgradePending.setStatus(_A)
class _EqptSAFpgaUpgradeFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('upgradeOnNextColdBoot',1),('doNotUpgrade',2),('upgradeOnNextWarmBoot',3)))
_EqptSAFpgaUpgradeFlag_Type.__name__=_D
_EqptSAFpgaUpgradeFlag_Object=MibTableColumn
eqptSAFpgaUpgradeFlag=_EqptSAFpgaUpgradeFlag_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,14),_EqptSAFpgaUpgradeFlag_Type())
eqptSAFpgaUpgradeFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptSAFpgaUpgradeFlag.setStatus(_A)
_EqptEqptMaxPowerDraw_Type=FloatHundredths
_EqptEqptMaxPowerDraw_Object=MibTableColumn
eqptEqptMaxPowerDraw=_EqptEqptMaxPowerDraw_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,15),_EqptEqptMaxPowerDraw_Type())
eqptEqptMaxPowerDraw.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptEqptMaxPowerDraw.setStatus(_A)
_EqptLastRebootTime_Type=DisplayString
_EqptLastRebootTime_Object=MibTableColumn
eqptLastRebootTime=_EqptLastRebootTime_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,16),_EqptLastRebootTime_Type())
eqptLastRebootTime.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptLastRebootTime.setStatus(_A)
_EqptLastRebootReason_Type=InfnLastRebootReason
_EqptLastRebootReason_Object=MibTableColumn
eqptLastRebootReason=_EqptLastRebootReason_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,17),_EqptLastRebootReason_Type())
eqptLastRebootReason.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptLastRebootReason.setStatus(_A)
_EqptInletTemp_Type=FloatArbitraryPrecision
_EqptInletTemp_Object=MibTableColumn
eqptInletTemp=_EqptInletTemp_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,18),_EqptInletTemp_Type())
eqptInletTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptInletTemp.setStatus(_A)
if mibBuilder.loadTexts:eqptInletTemp.setUnits(_J)
_EqptOutletTemp_Type=FloatArbitraryPrecision
_EqptOutletTemp_Object=MibTableColumn
eqptOutletTemp=_EqptOutletTemp_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,19),_EqptOutletTemp_Type())
eqptOutletTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptOutletTemp.setStatus(_A)
if mibBuilder.loadTexts:eqptOutletTemp.setUnits(_J)
_EqptPartNumber_Type=DisplayString
_EqptPartNumber_Object=MibTableColumn
eqptPartNumber=_EqptPartNumber_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,20),_EqptPartNumber_Type())
eqptPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptPartNumber.setStatus(_A)
_EqptSerialNumber_Type=DisplayString
_EqptSerialNumber_Object=MibTableColumn
eqptSerialNumber=_EqptSerialNumber_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,21),_EqptSerialNumber_Type())
eqptSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptSerialNumber.setStatus(_A)
_EqptManufacturedDate_Type=DisplayString
_EqptManufacturedDate_Object=MibTableColumn
eqptManufacturedDate=_EqptManufacturedDate_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,22),_EqptManufacturedDate_Type())
eqptManufacturedDate.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptManufacturedDate.setStatus(_A)
_EqptVendorId_Type=DisplayString
_EqptVendorId_Object=MibTableColumn
eqptVendorId=_EqptVendorId_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,23),_EqptVendorId_Type())
eqptVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptVendorId.setStatus(_A)
_EqptHardwareVersion_Type=DisplayString
_EqptHardwareVersion_Object=MibTableColumn
eqptHardwareVersion=_EqptHardwareVersion_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,24),_EqptHardwareVersion_Type())
eqptHardwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptHardwareVersion.setStatus(_A)
_EqptFirmwareVersion_Type=DisplayString
_EqptFirmwareVersion_Object=MibTableColumn
eqptFirmwareVersion=_EqptFirmwareVersion_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,25),_EqptFirmwareVersion_Type())
eqptFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptFirmwareVersion.setStatus(_A)
_EqptPON_Type=DisplayString
_EqptPON_Object=MibTableColumn
eqptPON=_EqptPON_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,26),_EqptPON_Type())
eqptPON.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptPON.setStatus(_A)
_EqptUniversalSlotUsage_Type=Integer32
_EqptUniversalSlotUsage_Object=MibTableColumn
eqptUniversalSlotUsage=_EqptUniversalSlotUsage_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,27),_EqptUniversalSlotUsage_Type())
eqptUniversalSlotUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptUniversalSlotUsage.setStatus(_A)
_EqptFruInsertionDate_Type=DisplayString
_EqptFruInsertionDate_Object=MibTableColumn
eqptFruInsertionDate=_EqptFruInsertionDate_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,28),_EqptFruInsertionDate_Type())
eqptFruInsertionDate.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptFruInsertionDate.setStatus(_A)
_EqptRedundancyStatus_Type=InfnCorrelatedRedunStatus
_EqptRedundancyStatus_Object=MibTableColumn
eqptRedundancyStatus=_EqptRedundancyStatus_Object((1,3,6,1,4,1,21296,2,2,1,9,1,1,1,29),_EqptRedundancyStatus_Type())
eqptRedundancyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:eqptRedundancyStatus.setStatus(_A)
_EqptConformance_ObjectIdentity=ObjectIdentity
eqptConformance=_EqptConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,9,1,3))
_EqptCompliances_ObjectIdentity=ObjectIdentity
eqptCompliances=_EqptCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,9,1,3,1))
_EqptGroups_ObjectIdentity=ObjectIdentity
eqptGroups=_EqptGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,1,9,1,3,2))
eqptGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,1,9,1,3,2,1))
eqptGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:eqptGroup.setStatus(_A)
eqptCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,1,9,1,3,1,1))
eqptCompliance.setObjects((_B,_n))
if mibBuilder.loadTexts:eqptCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'eqptMIB':eqptMIB,'eqptTable':eqptTable,'eqptEntry':eqptEntry,_K:eqptMoId,_L:eqptLabel,_M:eqptAdministrativeState,_N:eqptOperationalState,_O:eqptAvailabilityState,_P:eqptAlarmReportControl,_Q:eqptOpStateQualifierList,_R:eqptAlarmInhibitState,_S:eqptProvEqptType,_T:eqptInstalledEqptType,_U:eqptBaseCircuitPackType,_V:eqptCLEI,_W:eqptSAFpgaUpgradePending,_X:eqptSAFpgaUpgradeFlag,_Y:eqptEqptMaxPowerDraw,_Z:eqptLastRebootTime,_a:eqptLastRebootReason,_b:eqptInletTemp,_c:eqptOutletTemp,_d:eqptPartNumber,_e:eqptSerialNumber,_f:eqptManufacturedDate,_g:eqptVendorId,_h:eqptHardwareVersion,_i:eqptFirmwareVersion,_j:eqptPON,_k:eqptUniversalSlotUsage,_l:eqptFruInsertionDate,_m:eqptRedundancyStatus,'eqptConformance':eqptConformance,'eqptCompliances':eqptCompliances,'eqptCompliance':eqptCompliance,'eqptGroups':eqptGroups,_n:eqptGroup})