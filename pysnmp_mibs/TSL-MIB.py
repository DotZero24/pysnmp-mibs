_U='mduTotalCurrent'
_T='mduVoltage'
_S='mduPowerStatus'
_R='alarmData'
_Q='alarmPolarity'
_P='alarmState'
_O='alarmText'
_N='alarmIndex'
_M='alarmType'
_L='mduOutputIndex'
_K='DisplayString'
_J='NotificationType'
_I='alarmEqptTemp'
_H='off'
_G='optional'
_F='alarmTableIndex'
_E='Integer32'
_D='TSL-MIB'
_C='read-only'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_J,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','Opaque',_J,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_TslMIB_ObjectIdentity=ObjectIdentity
tslMIB=_TslMIB_ObjectIdentity((1,3,6,1,4,1,6853))
_Alarm_ObjectIdentity=ObjectIdentity
alarm=_Alarm_ObjectIdentity((1,3,6,1,4,1,6853,2))
_AlarmIdent_Type=DisplayString
_AlarmIdent_Object=MibScalar
alarmIdent=_AlarmIdent_Object((1,3,6,1,4,1,6853,2,1),_AlarmIdent_Type())
alarmIdent.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmIdent.setStatus(_A)
_AlarmTable_Object=MibTable
alarmTable=_AlarmTable_Object((1,3,6,1,4,1,6853,2,2))
if mibBuilder.loadTexts:alarmTable.setStatus(_A)
_AlarmEntry_Object=MibTableRow
alarmEntry=_AlarmEntry_Object((1,3,6,1,4,1,6853,2,2,1))
alarmEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:alarmEntry.setStatus(_A)
class _AlarmTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,28))
_AlarmTableIndex_Type.__name__=_E
_AlarmTableIndex_Object=MibTableColumn
alarmTableIndex=_AlarmTableIndex_Object((1,3,6,1,4,1,6853,2,2,1,1),_AlarmTableIndex_Type())
alarmTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmTableIndex.setStatus(_A)
class _AlarmType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('internal',1),('gpi',2),('outputFail',3),('psuFail',4),('currentAlarm',5)))
_AlarmType_Type.__name__=_E
_AlarmType_Object=MibTableColumn
alarmType=_AlarmType_Object((1,3,6,1,4,1,6853,2,2,1,2),_AlarmType_Type())
alarmType.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmType.setStatus(_A)
_AlarmIndex_Type=Integer32
_AlarmIndex_Object=MibTableColumn
alarmIndex=_AlarmIndex_Object((1,3,6,1,4,1,6853,2,2,1,3),_AlarmIndex_Type())
alarmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmIndex.setStatus(_A)
_AlarmText_Type=DisplayString
_AlarmText_Object=MibTableColumn
alarmText=_AlarmText_Object((1,3,6,1,4,1,6853,2,2,1,4),_AlarmText_Type())
alarmText.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmText.setStatus(_A)
class _AlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inactive',1),('active',2)))
_AlarmState_Type.__name__=_E
_AlarmState_Object=MibTableColumn
alarmState=_AlarmState_Object((1,3,6,1,4,1,6853,2,2,1,5),_AlarmState_Type())
alarmState.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmState.setStatus(_A)
class _AlarmPolarity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notApplicable',1),('normallyOpen',2),('normallyClosed',3)))
_AlarmPolarity_Type.__name__=_E
_AlarmPolarity_Object=MibTableColumn
alarmPolarity=_AlarmPolarity_Object((1,3,6,1,4,1,6853,2,2,1,6),_AlarmPolarity_Type())
alarmPolarity.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmPolarity.setStatus(_A)
_AlarmData_Type=Opaque
_AlarmData_Object=MibTableColumn
alarmData=_AlarmData_Object((1,3,6,1,4,1,6853,2,2,1,7),_AlarmData_Type())
alarmData.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmData.setStatus(_G)
_AlarmTotal_Type=Integer32
_AlarmTotal_Object=MibScalar
alarmTotal=_AlarmTotal_Object((1,3,6,1,4,1,6853,2,3),_AlarmTotal_Type())
alarmTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmTotal.setStatus(_A)
_AlarmLocation_Type=DisplayString
_AlarmLocation_Object=MibScalar
alarmLocation=_AlarmLocation_Object((1,3,6,1,4,1,6853,2,4),_AlarmLocation_Type())
alarmLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmLocation.setStatus(_A)
_AlarmEqptTemp_Type=Integer32
_AlarmEqptTemp_Object=MibScalar
alarmEqptTemp=_AlarmEqptTemp_Object((1,3,6,1,4,1,6853,2,5),_AlarmEqptTemp_Type())
alarmEqptTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmEqptTemp.setStatus(_G)
_AlarmEqptTempHi_Type=Integer32
_AlarmEqptTempHi_Object=MibScalar
alarmEqptTempHi=_AlarmEqptTempHi_Object((1,3,6,1,4,1,6853,2,6),_AlarmEqptTempHi_Type())
alarmEqptTempHi.setMaxAccess(_B)
if mibBuilder.loadTexts:alarmEqptTempHi.setStatus(_G)
_Mdu12_ObjectIdentity=ObjectIdentity
mdu12=_Mdu12_ObjectIdentity((1,3,6,1,4,1,6853,3))
_Mdu12Ident_Type=DisplayString
_Mdu12Ident_Object=MibScalar
mdu12Ident=_Mdu12Ident_Object((1,3,6,1,4,1,6853,3,1),_Mdu12Ident_Type())
mdu12Ident.setMaxAccess(_C)
if mibBuilder.loadTexts:mdu12Ident.setStatus(_A)
class _MduPowerOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('simultaneous',1),('sequential',2),('delayed',3)))
_MduPowerOn_Type.__name__=_E
_MduPowerOn_Object=MibScalar
mduPowerOn=_MduPowerOn_Object((1,3,6,1,4,1,6853,3,2),_MduPowerOn_Type())
mduPowerOn.setMaxAccess(_B)
if mibBuilder.loadTexts:mduPowerOn.setStatus(_A)
_MduSeqDelay_Type=Integer32
_MduSeqDelay_Object=MibScalar
mduSeqDelay=_MduSeqDelay_Object((1,3,6,1,4,1,6853,3,3),_MduSeqDelay_Type())
mduSeqDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:mduSeqDelay.setStatus(_A)
_MduOutputTable_Object=MibTable
mduOutputTable=_MduOutputTable_Object((1,3,6,1,4,1,6853,3,4))
if mibBuilder.loadTexts:mduOutputTable.setStatus(_A)
_MduOutputEntry_Object=MibTableRow
mduOutputEntry=_MduOutputEntry_Object((1,3,6,1,4,1,6853,3,4,1))
mduOutputEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:mduOutputEntry.setStatus(_A)
class _MduOutputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_MduOutputIndex_Type.__name__=_E
_MduOutputIndex_Object=MibTableColumn
mduOutputIndex=_MduOutputIndex_Object((1,3,6,1,4,1,6853,3,4,1,1),_MduOutputIndex_Type())
mduOutputIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mduOutputIndex.setStatus(_A)
class _MduOutputState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('on',2),('locked-Off',3),('locked-On',4)))
_MduOutputState_Type.__name__=_E
_MduOutputState_Object=MibTableColumn
mduOutputState=_MduOutputState_Object((1,3,6,1,4,1,6853,3,4,1,2),_MduOutputState_Type())
mduOutputState.setMaxAccess(_B)
if mibBuilder.loadTexts:mduOutputState.setStatus(_A)
_MduOutputDelay_Type=Integer32
_MduOutputDelay_Object=MibTableColumn
mduOutputDelay=_MduOutputDelay_Object((1,3,6,1,4,1,6853,3,4,1,3),_MduOutputDelay_Type())
mduOutputDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:mduOutputDelay.setStatus(_A)
_MduOutputlowerCurrent_Type=Integer32
_MduOutputlowerCurrent_Object=MibTableColumn
mduOutputlowerCurrent=_MduOutputlowerCurrent_Object((1,3,6,1,4,1,6853,3,4,1,4),_MduOutputlowerCurrent_Type())
mduOutputlowerCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:mduOutputlowerCurrent.setStatus(_A)
_MduOutputupperCurrent_Type=Integer32
_MduOutputupperCurrent_Object=MibTableColumn
mduOutputupperCurrent=_MduOutputupperCurrent_Object((1,3,6,1,4,1,6853,3,4,1,5),_MduOutputupperCurrent_Type())
mduOutputupperCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:mduOutputupperCurrent.setStatus(_A)
_MduOutputCurrent_Type=Integer32
_MduOutputCurrent_Object=MibTableColumn
mduOutputCurrent=_MduOutputCurrent_Object((1,3,6,1,4,1,6853,3,4,1,6),_MduOutputCurrent_Type())
mduOutputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:mduOutputCurrent.setStatus(_A)
_MduOutputpowerFactor_Type=Integer32
_MduOutputpowerFactor_Object=MibTableColumn
mduOutputpowerFactor=_MduOutputpowerFactor_Object((1,3,6,1,4,1,6853,3,4,1,7),_MduOutputpowerFactor_Type())
mduOutputpowerFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:mduOutputpowerFactor.setStatus(_A)
_MduOutputVA_Type=Integer32
_MduOutputVA_Object=MibTableColumn
mduOutputVA=_MduOutputVA_Object((1,3,6,1,4,1,6853,3,4,1,8),_MduOutputVA_Type())
mduOutputVA.setMaxAccess(_C)
if mibBuilder.loadTexts:mduOutputVA.setStatus(_A)
_MduOutputWatts_Type=Integer32
_MduOutputWatts_Object=MibTableColumn
mduOutputWatts=_MduOutputWatts_Object((1,3,6,1,4,1,6853,3,4,1,9),_MduOutputWatts_Type())
mduOutputWatts.setMaxAccess(_C)
if mibBuilder.loadTexts:mduOutputWatts.setStatus(_A)
_MduOutputCal_Type=Integer32
_MduOutputCal_Object=MibTableColumn
mduOutputCal=_MduOutputCal_Object((1,3,6,1,4,1,6853,3,4,1,10),_MduOutputCal_Type())
mduOutputCal.setMaxAccess(_B)
if mibBuilder.loadTexts:mduOutputCal.setStatus(_A)
class _MduPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('totalLoss',1),('input1OK',2),('input2OK',3),('allOk',4)))
_MduPowerStatus_Type.__name__=_E
_MduPowerStatus_Object=MibScalar
mduPowerStatus=_MduPowerStatus_Object((1,3,6,1,4,1,6853,3,5),_MduPowerStatus_Type())
mduPowerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mduPowerStatus.setStatus(_A)
_MduVoltageCal_Type=Integer32
_MduVoltageCal_Object=MibScalar
mduVoltageCal=_MduVoltageCal_Object((1,3,6,1,4,1,6853,3,6),_MduVoltageCal_Type())
mduVoltageCal.setMaxAccess(_B)
if mibBuilder.loadTexts:mduVoltageCal.setStatus(_A)
_MduVoltage_Type=Integer32
_MduVoltage_Object=MibScalar
mduVoltage=_MduVoltage_Object((1,3,6,1,4,1,6853,3,7),_MduVoltage_Type())
mduVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:mduVoltage.setStatus(_A)
_MduVoltageFloor_Type=Integer32
_MduVoltageFloor_Object=MibScalar
mduVoltageFloor=_MduVoltageFloor_Object((1,3,6,1,4,1,6853,3,8),_MduVoltageFloor_Type())
mduVoltageFloor.setMaxAccess(_B)
if mibBuilder.loadTexts:mduVoltageFloor.setStatus(_A)
_MduVoltageLimit_Type=Integer32
_MduVoltageLimit_Object=MibScalar
mduVoltageLimit=_MduVoltageLimit_Object((1,3,6,1,4,1,6853,3,9),_MduVoltageLimit_Type())
mduVoltageLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:mduVoltageLimit.setStatus(_A)
_MduTotalCurrent_Type=Integer32
_MduTotalCurrent_Object=MibScalar
mduTotalCurrent=_MduTotalCurrent_Object((1,3,6,1,4,1,6853,3,10),_MduTotalCurrent_Type())
mduTotalCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:mduTotalCurrent.setStatus(_A)
_MduCurrentLimit_Type=Integer32
_MduCurrentLimit_Object=MibScalar
mduCurrentLimit=_MduCurrentLimit_Object((1,3,6,1,4,1,6853,3,11),_MduCurrentLimit_Type())
mduCurrentLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:mduCurrentLimit.setStatus(_A)
class _MduAuxRly1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('on',2)))
_MduAuxRly1_Type.__name__=_E
_MduAuxRly1_Object=MibScalar
mduAuxRly1=_MduAuxRly1_Object((1,3,6,1,4,1,6853,3,12),_MduAuxRly1_Type())
mduAuxRly1.setMaxAccess(_B)
if mibBuilder.loadTexts:mduAuxRly1.setStatus(_A)
class _MduAuxRly2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('on',2)))
_MduAuxRly2_Type.__name__=_E
_MduAuxRly2_Object=MibScalar
mduAuxRly2=_MduAuxRly2_Object((1,3,6,1,4,1,6853,3,13),_MduAuxRly2_Type())
mduAuxRly2.setMaxAccess(_B)
if mibBuilder.loadTexts:mduAuxRly2.setStatus(_A)
alarmTrap=NotificationType((1,3,6,1,4,1,6853,0,4))
alarmTrap.setObjects(*((_D,_F),(_D,_M),(_D,_N),(_D,_O),(_D,_P),(_D,_Q),(_D,_R)))
if mibBuilder.loadTexts:alarmTrap.setStatus('')
alarmEqptTempHiTrap=NotificationType((1,3,6,1,4,1,6853,0,5))
alarmEqptTempHiTrap.setObjects((_D,_I))
if mibBuilder.loadTexts:alarmEqptTempHiTrap.setStatus('')
alarmEqptTempOkTrap=NotificationType((1,3,6,1,4,1,6853,0,6))
alarmEqptTempOkTrap.setObjects((_D,_I))
if mibBuilder.loadTexts:alarmEqptTempOkTrap.setStatus('')
mduPowerStatusTrap=NotificationType((1,3,6,1,4,1,6853,0,7))
mduPowerStatusTrap.setObjects((_D,_S))
if mibBuilder.loadTexts:mduPowerStatusTrap.setStatus('')
mduVoltageStatusTrap=NotificationType((1,3,6,1,4,1,6853,0,8))
mduVoltageStatusTrap.setObjects((_D,_T))
if mibBuilder.loadTexts:mduVoltageStatusTrap.setStatus('')
mduTotalCurrentStatusTrap=NotificationType((1,3,6,1,4,1,6853,0,9))
mduTotalCurrentStatusTrap.setObjects((_D,_U))
if mibBuilder.loadTexts:mduTotalCurrentStatusTrap.setStatus('')
mibBuilder.exportSymbols(_D,**{_K:DisplayString,'tslMIB':tslMIB,'alarmTrap':alarmTrap,'alarmEqptTempHiTrap':alarmEqptTempHiTrap,'alarmEqptTempOkTrap':alarmEqptTempOkTrap,'mduPowerStatusTrap':mduPowerStatusTrap,'mduVoltageStatusTrap':mduVoltageStatusTrap,'mduTotalCurrentStatusTrap':mduTotalCurrentStatusTrap,'alarm':alarm,'alarmIdent':alarmIdent,'alarmTable':alarmTable,'alarmEntry':alarmEntry,_F:alarmTableIndex,_M:alarmType,_N:alarmIndex,_O:alarmText,_P:alarmState,_Q:alarmPolarity,_R:alarmData,'alarmTotal':alarmTotal,'alarmLocation':alarmLocation,_I:alarmEqptTemp,'alarmEqptTempHi':alarmEqptTempHi,'mdu12':mdu12,'mdu12Ident':mdu12Ident,'mduPowerOn':mduPowerOn,'mduSeqDelay':mduSeqDelay,'mduOutputTable':mduOutputTable,'mduOutputEntry':mduOutputEntry,_L:mduOutputIndex,'mduOutputState':mduOutputState,'mduOutputDelay':mduOutputDelay,'mduOutputlowerCurrent':mduOutputlowerCurrent,'mduOutputupperCurrent':mduOutputupperCurrent,'mduOutputCurrent':mduOutputCurrent,'mduOutputpowerFactor':mduOutputpowerFactor,'mduOutputVA':mduOutputVA,'mduOutputWatts':mduOutputWatts,'mduOutputCal':mduOutputCal,_S:mduPowerStatus,'mduVoltageCal':mduVoltageCal,_T:mduVoltage,'mduVoltageFloor':mduVoltageFloor,'mduVoltageLimit':mduVoltageLimit,_U:mduTotalCurrent,'mduCurrentLimit':mduCurrentLimit,'mduAuxRly1':mduAuxRly1,'mduAuxRly2':mduAuxRly2})