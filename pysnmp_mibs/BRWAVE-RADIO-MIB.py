_Q='brwaveRadioRSLVoltage'
_P='brwaveRadioTxBand'
_O='brwaveTrapCount'
_N='brwaveUnitModel'
_M='brwaveRadioSn'
_L='accessible-for-notify'
_K='ifIndex'
_J='IF-MIB'
_I='OctetString'
_H='brwaveRadioInVoltage'
_G='Integer32'
_F='brwaveRadioTxTemperature'
_E='brwaveRadioUnitTemperature'
_D='brwaveRadioRSL'
_C='read-only'
_B='BRWAVE-RADIO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_J,_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
brwaveRadioMibModule=ModuleIdentity((1,3,6,1,4,1,6080,1,1,3))
if mibBuilder.loadTexts:brwaveRadioMibModule.setRevisions(('2006-07-06 11:00','2005-05-26 11:30'))
_BridgeWave_ObjectIdentity=ObjectIdentity
bridgeWave=_BridgeWave_ObjectIdentity((1,3,6,1,4,1,6080))
if mibBuilder.loadTexts:bridgeWave.setStatus(_A)
_BrwaveReg_ObjectIdentity=ObjectIdentity
brwaveReg=_BrwaveReg_ObjectIdentity((1,3,6,1,4,1,6080,1))
if mibBuilder.loadTexts:brwaveReg.setStatus(_A)
_BrwaveMibs_ObjectIdentity=ObjectIdentity
brwaveMibs=_BrwaveMibs_ObjectIdentity((1,3,6,1,4,1,6080,1,1))
if mibBuilder.loadTexts:brwaveMibs.setStatus(_A)
_BrwaveModules_ObjectIdentity=ObjectIdentity
brwaveModules=_BrwaveModules_ObjectIdentity((1,3,6,1,4,1,6080,1,2))
if mibBuilder.loadTexts:brwaveModules.setStatus(_A)
_BrwaveRadioFE60_ObjectIdentity=ObjectIdentity
brwaveRadioFE60=_BrwaveRadioFE60_ObjectIdentity((1,3,6,1,4,1,6080,1,2,1))
if mibBuilder.loadTexts:brwaveRadioFE60.setStatus(_A)
_BrwaveRadioGE60_ObjectIdentity=ObjectIdentity
brwaveRadioGE60=_BrwaveRadioGE60_ObjectIdentity((1,3,6,1,4,1,6080,1,2,2))
if mibBuilder.loadTexts:brwaveRadioGE60.setStatus(_A)
_BrwaveRadioAR60_ObjectIdentity=ObjectIdentity
brwaveRadioAR60=_BrwaveRadioAR60_ObjectIdentity((1,3,6,1,4,1,6080,1,2,3))
if mibBuilder.loadTexts:brwaveRadioAR60.setStatus(_A)
_BrwaveCommon_ObjectIdentity=ObjectIdentity
brwaveCommon=_BrwaveCommon_ObjectIdentity((1,3,6,1,4,1,6080,2))
if mibBuilder.loadTexts:brwaveCommon.setStatus(_A)
_BrwaveRadioSn_Type=DisplayString
_BrwaveRadioSn_Object=MibScalar
brwaveRadioSn=_BrwaveRadioSn_Object((1,3,6,1,4,1,6080,2,1),_BrwaveRadioSn_Type())
brwaveRadioSn.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveRadioSn.setStatus(_A)
_BrwaveUnitModel_Type=DisplayString
_BrwaveUnitModel_Object=MibScalar
brwaveUnitModel=_BrwaveUnitModel_Object((1,3,6,1,4,1,6080,2,2),_BrwaveUnitModel_Type())
brwaveUnitModel.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveUnitModel.setStatus(_A)
_BrwaveBbSn_Type=DisplayString
_BrwaveBbSn_Object=MibScalar
brwaveBbSn=_BrwaveBbSn_Object((1,3,6,1,4,1,6080,2,3),_BrwaveBbSn_Type())
brwaveBbSn.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveBbSn.setStatus(_A)
_BrwaveIfSn_Type=DisplayString
_BrwaveIfSn_Object=MibScalar
brwaveIfSn=_BrwaveIfSn_Object((1,3,6,1,4,1,6080,2,4),_BrwaveIfSn_Type())
brwaveIfSn.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveIfSn.setStatus(_A)
_BrwaveMmwSn_Type=DisplayString
_BrwaveMmwSn_Object=MibScalar
brwaveMmwSn=_BrwaveMmwSn_Object((1,3,6,1,4,1,6080,2,5),_BrwaveMmwSn_Type())
brwaveMmwSn.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveMmwSn.setStatus(_A)
_BrwaveTrapCount_Type=Unsigned32
_BrwaveTrapCount_Object=MibScalar
brwaveTrapCount=_BrwaveTrapCount_Object((1,3,6,1,4,1,6080,2,6),_BrwaveTrapCount_Type())
brwaveTrapCount.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveTrapCount.setStatus(_A)
_BrwaveProducts_ObjectIdentity=ObjectIdentity
brwaveProducts=_BrwaveProducts_ObjectIdentity((1,3,6,1,4,1,6080,3))
if mibBuilder.loadTexts:brwaveProducts.setStatus(_A)
_BrwaveRadio_ObjectIdentity=ObjectIdentity
brwaveRadio=_BrwaveRadio_ObjectIdentity((1,3,6,1,4,1,6080,3,1))
if mibBuilder.loadTexts:brwaveRadio.setStatus(_A)
_BrwaveRadioFactorySetup_ObjectIdentity=ObjectIdentity
brwaveRadioFactorySetup=_BrwaveRadioFactorySetup_ObjectIdentity((1,3,6,1,4,1,6080,3,1,2))
if mibBuilder.loadTexts:brwaveRadioFactorySetup.setStatus(_A)
class _BrwaveRadioTxBand_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('low',1),('high',2)))
_BrwaveRadioTxBand_Type.__name__=_G
_BrwaveRadioTxBand_Object=MibScalar
brwaveRadioTxBand=_BrwaveRadioTxBand_Object((1,3,6,1,4,1,6080,3,1,2,1),_BrwaveRadioTxBand_Type())
brwaveRadioTxBand.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveRadioTxBand.setStatus(_A)
class _BrwaveRadioFactoryRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('adaptRate',1),('mbps1000',2),('mbps100',3)))
_BrwaveRadioFactoryRate_Type.__name__=_G
_BrwaveRadioFactoryRate_Object=MibScalar
brwaveRadioFactoryRate=_BrwaveRadioFactoryRate_Object((1,3,6,1,4,1,6080,3,1,2,3),_BrwaveRadioFactoryRate_Type())
brwaveRadioFactoryRate.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveRadioFactoryRate.setStatus(_A)
_BrwaveRadioClearStats_Type=Integer32
_BrwaveRadioClearStats_Object=MibScalar
brwaveRadioClearStats=_BrwaveRadioClearStats_Object((1,3,6,1,4,1,6080,3,1,2,4),_BrwaveRadioClearStats_Type())
brwaveRadioClearStats.setMaxAccess('read-write')
if mibBuilder.loadTexts:brwaveRadioClearStats.setStatus(_A)
_BrwaveRadioStatus_ObjectIdentity=ObjectIdentity
brwaveRadioStatus=_BrwaveRadioStatus_ObjectIdentity((1,3,6,1,4,1,6080,3,1,3))
if mibBuilder.loadTexts:brwaveRadioStatus.setStatus(_A)
_BrwaveRadioInVoltage_Type=Integer32
_BrwaveRadioInVoltage_Object=MibScalar
brwaveRadioInVoltage=_BrwaveRadioInVoltage_Object((1,3,6,1,4,1,6080,3,1,3,1),_BrwaveRadioInVoltage_Type())
brwaveRadioInVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveRadioInVoltage.setStatus(_A)
_BrwaveRadioUnitTemperature_Type=Integer32
_BrwaveRadioUnitTemperature_Object=MibScalar
brwaveRadioUnitTemperature=_BrwaveRadioUnitTemperature_Object((1,3,6,1,4,1,6080,3,1,3,2),_BrwaveRadioUnitTemperature_Type())
brwaveRadioUnitTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveRadioUnitTemperature.setStatus(_A)
_BrwaveRadioTxTemperature_Type=Integer32
_BrwaveRadioTxTemperature_Object=MibScalar
brwaveRadioTxTemperature=_BrwaveRadioTxTemperature_Object((1,3,6,1,4,1,6080,3,1,3,3),_BrwaveRadioTxTemperature_Type())
brwaveRadioTxTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveRadioTxTemperature.setStatus(_A)
_BrwaveRadioRSL_Type=Integer32
_BrwaveRadioRSL_Object=MibScalar
brwaveRadioRSL=_BrwaveRadioRSL_Object((1,3,6,1,4,1,6080,3,1,3,4),_BrwaveRadioRSL_Type())
brwaveRadioRSL.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveRadioRSL.setStatus(_A)
_BrwaveRadioRSLVoltage_Type=DisplayString
_BrwaveRadioRSLVoltage_Object=MibScalar
brwaveRadioRSLVoltage=_BrwaveRadioRSLVoltage_Object((1,3,6,1,4,1,6080,3,1,3,5),_BrwaveRadioRSLVoltage_Type())
brwaveRadioRSLVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveRadioRSLVoltage.setStatus(_A)
_BrwaveRadioAbsRSL_Type=Integer32
_BrwaveRadioAbsRSL_Object=MibScalar
brwaveRadioAbsRSL=_BrwaveRadioAbsRSL_Object((1,3,6,1,4,1,6080,3,1,3,6),_BrwaveRadioAbsRSL_Type())
brwaveRadioAbsRSL.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveRadioAbsRSL.setStatus(_A)
_BrwaveRadioRSLVoltageInt_Type=Integer32
_BrwaveRadioRSLVoltageInt_Object=MibScalar
brwaveRadioRSLVoltageInt=_BrwaveRadioRSLVoltageInt_Object((1,3,6,1,4,1,6080,3,1,3,7),_BrwaveRadioRSLVoltageInt_Type())
brwaveRadioRSLVoltageInt.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveRadioRSLVoltageInt.setStatus(_A)
_BrwaveCopperUtilization_Type=Integer32
_BrwaveCopperUtilization_Object=MibScalar
brwaveCopperUtilization=_BrwaveCopperUtilization_Object((1,3,6,1,4,1,6080,3,1,3,8),_BrwaveCopperUtilization_Type())
brwaveCopperUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveCopperUtilization.setStatus(_A)
_BrwaveFiberUtilization_Type=Integer32
_BrwaveFiberUtilization_Object=MibScalar
brwaveFiberUtilization=_BrwaveFiberUtilization_Object((1,3,6,1,4,1,6080,3,1,3,9),_BrwaveFiberUtilization_Type())
brwaveFiberUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveFiberUtilization.setStatus(_A)
_BrwaveRadioUtilization_Type=Integer32
_BrwaveRadioUtilization_Object=MibScalar
brwaveRadioUtilization=_BrwaveRadioUtilization_Object((1,3,6,1,4,1,6080,3,1,3,10),_BrwaveRadioUtilization_Type())
brwaveRadioUtilization.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveRadioUtilization.setStatus(_A)
class _BrwaveRadioFecError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noError',0),('preFec',1),('postFec',2)))
_BrwaveRadioFecError_Type.__name__=_G
_BrwaveRadioFecError_Object=MibScalar
brwaveRadioFecError=_BrwaveRadioFecError_Object((1,3,6,1,4,1,6080,3,1,3,11),_BrwaveRadioFecError_Type())
brwaveRadioFecError.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveRadioFecError.setStatus(_A)
_BrwaveRadioPreFecFlag_Type=Integer32
_BrwaveRadioPreFecFlag_Object=MibScalar
brwaveRadioPreFecFlag=_BrwaveRadioPreFecFlag_Object((1,3,6,1,4,1,6080,3,1,3,12),_BrwaveRadioPreFecFlag_Type())
brwaveRadioPreFecFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveRadioPreFecFlag.setStatus(_A)
_BrwaveRadioPostFecFlag_Type=Integer32
_BrwaveRadioPostFecFlag_Object=MibScalar
brwaveRadioPostFecFlag=_BrwaveRadioPostFecFlag_Object((1,3,6,1,4,1,6080,3,1,3,13),_BrwaveRadioPostFecFlag_Type())
brwaveRadioPostFecFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveRadioPostFecFlag.setStatus(_A)
_BrwaveRadioLinkRate_Type=Integer32
_BrwaveRadioLinkRate_Object=MibScalar
brwaveRadioLinkRate=_BrwaveRadioLinkRate_Object((1,3,6,1,4,1,6080,3,1,3,14),_BrwaveRadioLinkRate_Type())
brwaveRadioLinkRate.setMaxAccess(_C)
if mibBuilder.loadTexts:brwaveRadioLinkRate.setStatus(_A)
_BrwaveRadioEvents_ObjectIdentity=ObjectIdentity
brwaveRadioEvents=_BrwaveRadioEvents_ObjectIdentity((1,3,6,1,4,1,6080,3,1,9))
_BrwaveRadioEventsV2_ObjectIdentity=ObjectIdentity
brwaveRadioEventsV2=_BrwaveRadioEventsV2_ObjectIdentity((1,3,6,1,4,1,6080,3,1,9,0))
_BrwaveRadioTrapObjs_ObjectIdentity=ObjectIdentity
brwaveRadioTrapObjs=_BrwaveRadioTrapObjs_ObjectIdentity((1,3,6,1,4,1,6080,3,1,9,1))
class _ManagerIP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ManagerIP_Type.__name__=_I
_ManagerIP_Object=MibScalar
managerIP=_ManagerIP_Object((1,3,6,1,4,1,6080,3,1,9,1,1),_ManagerIP_Type())
managerIP.setMaxAccess(_L)
if mibBuilder.loadTexts:managerIP.setStatus(_A)
class _UserName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_UserName_Type.__name__=_I
_UserName_Object=MibScalar
userName=_UserName_Object((1,3,6,1,4,1,6080,3,1,9,1,2),_UserName_Type())
userName.setMaxAccess(_L)
if mibBuilder.loadTexts:userName.setStatus(_A)
_BrwaveConformance_ObjectIdentity=ObjectIdentity
brwaveConformance=_BrwaveConformance_ObjectIdentity((1,3,6,1,4,1,6080,3,1,10))
_BrwaveRadioGroups_ObjectIdentity=ObjectIdentity
brwaveRadioGroups=_BrwaveRadioGroups_ObjectIdentity((1,3,6,1,4,1,6080,3,1,10,1))
_BrwaveCompliances_ObjectIdentity=ObjectIdentity
brwaveCompliances=_BrwaveCompliances_ObjectIdentity((1,3,6,1,4,1,6080,3,1,10,2))
brwaveCommonGroup=ObjectGroup((1,3,6,1,4,1,6080,3,1,10,1,1))
brwaveCommonGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:brwaveCommonGroup.setStatus(_A)
brwaveFactoryGroup=ObjectGroup((1,3,6,1,4,1,6080,3,1,10,1,2))
brwaveFactoryGroup.setObjects((_B,_P))
if mibBuilder.loadTexts:brwaveFactoryGroup.setStatus(_A)
brwaveStatusGroup=ObjectGroup((1,3,6,1,4,1,6080,3,1,10,1,3))
brwaveStatusGroup.setObjects(*((_B,_H),(_B,_E),(_B,_F),(_B,_D),(_B,_Q)))
if mibBuilder.loadTexts:brwaveStatusGroup.setStatus(_A)
brwaveErrorsOverThreshold=NotificationType((1,3,6,1,4,1,6080,3,1,9,0,1))
brwaveErrorsOverThreshold.setObjects(*((_J,_K),(_B,_E),(_B,_F),(_B,_D)))
if mibBuilder.loadTexts:brwaveErrorsOverThreshold.setStatus(_A)
brwaveErrorsUnderThreshold=NotificationType((1,3,6,1,4,1,6080,3,1,9,0,2))
brwaveErrorsUnderThreshold.setObjects(*((_J,_K),(_B,_E),(_B,_F),(_B,_D)))
if mibBuilder.loadTexts:brwaveErrorsUnderThreshold.setStatus(_A)
brwaveUnitTemperatureAbnormal=NotificationType((1,3,6,1,4,1,6080,3,1,9,0,3))
brwaveUnitTemperatureAbnormal.setObjects((_B,_E))
if mibBuilder.loadTexts:brwaveUnitTemperatureAbnormal.setStatus(_A)
brwaveUnitTemperatureNormal=NotificationType((1,3,6,1,4,1,6080,3,1,9,0,4))
brwaveUnitTemperatureNormal.setObjects((_B,_E))
if mibBuilder.loadTexts:brwaveUnitTemperatureNormal.setStatus(_A)
brwaveTxTemperatureAbnormal=NotificationType((1,3,6,1,4,1,6080,3,1,9,0,5))
brwaveTxTemperatureAbnormal.setObjects((_B,_F))
if mibBuilder.loadTexts:brwaveTxTemperatureAbnormal.setStatus(_A)
brwaveTxTemperatureNormal=NotificationType((1,3,6,1,4,1,6080,3,1,9,0,6))
brwaveTxTemperatureNormal.setObjects((_B,_F))
if mibBuilder.loadTexts:brwaveTxTemperatureNormal.setStatus(_A)
brwaveInputVoltageAbnormal=NotificationType((1,3,6,1,4,1,6080,3,1,9,0,7))
brwaveInputVoltageAbnormal.setObjects((_B,_H))
if mibBuilder.loadTexts:brwaveInputVoltageAbnormal.setStatus(_A)
brwaveInputVoltageNormal=NotificationType((1,3,6,1,4,1,6080,3,1,9,0,8))
brwaveInputVoltageNormal.setObjects((_B,_H))
if mibBuilder.loadTexts:brwaveInputVoltageNormal.setStatus(_A)
brwaveRslNormal=NotificationType((1,3,6,1,4,1,6080,3,1,9,0,10))
brwaveRslNormal.setObjects((_B,_D))
if mibBuilder.loadTexts:brwaveRslNormal.setStatus(_A)
brwaveRslMinor=NotificationType((1,3,6,1,4,1,6080,3,1,9,0,11))
brwaveRslMinor.setObjects((_B,_D))
if mibBuilder.loadTexts:brwaveRslMinor.setStatus(_A)
brwaveRslMajor=NotificationType((1,3,6,1,4,1,6080,3,1,9,0,13))
brwaveRslMajor.setObjects((_B,_D))
if mibBuilder.loadTexts:brwaveRslMajor.setStatus(_A)
brwaveConfigChange=NotificationType((1,3,6,1,4,1,6080,3,1,9,0,26))
if mibBuilder.loadTexts:brwaveConfigChange.setStatus(_A)
brwaveLoginSuccessfull=NotificationType((1,3,6,1,4,1,6080,3,1,9,0,27))
if mibBuilder.loadTexts:brwaveLoginSuccessfull.setStatus(_A)
brwaveGeToFeSwitch=NotificationType((1,3,6,1,4,1,6080,3,1,9,0,28))
brwaveGeToFeSwitch.setObjects((_B,_D))
if mibBuilder.loadTexts:brwaveGeToFeSwitch.setStatus(_A)
brwaveFeToGeSwitch=NotificationType((1,3,6,1,4,1,6080,3,1,9,0,29))
brwaveFeToGeSwitch.setObjects((_B,_D))
if mibBuilder.loadTexts:brwaveFeToGeSwitch.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bridgeWave':bridgeWave,'brwaveReg':brwaveReg,'brwaveMibs':brwaveMibs,'brwaveRadioMibModule':brwaveRadioMibModule,'brwaveModules':brwaveModules,'brwaveRadioFE60':brwaveRadioFE60,'brwaveRadioGE60':brwaveRadioGE60,'brwaveRadioAR60':brwaveRadioAR60,'brwaveCommon':brwaveCommon,_M:brwaveRadioSn,_N:brwaveUnitModel,'brwaveBbSn':brwaveBbSn,'brwaveIfSn':brwaveIfSn,'brwaveMmwSn':brwaveMmwSn,_O:brwaveTrapCount,'brwaveProducts':brwaveProducts,'brwaveRadio':brwaveRadio,'brwaveRadioFactorySetup':brwaveRadioFactorySetup,_P:brwaveRadioTxBand,'brwaveRadioFactoryRate':brwaveRadioFactoryRate,'brwaveRadioClearStats':brwaveRadioClearStats,'brwaveRadioStatus':brwaveRadioStatus,_H:brwaveRadioInVoltage,_E:brwaveRadioUnitTemperature,_F:brwaveRadioTxTemperature,_D:brwaveRadioRSL,_Q:brwaveRadioRSLVoltage,'brwaveRadioAbsRSL':brwaveRadioAbsRSL,'brwaveRadioRSLVoltageInt':brwaveRadioRSLVoltageInt,'brwaveCopperUtilization':brwaveCopperUtilization,'brwaveFiberUtilization':brwaveFiberUtilization,'brwaveRadioUtilization':brwaveRadioUtilization,'brwaveRadioFecError':brwaveRadioFecError,'brwaveRadioPreFecFlag':brwaveRadioPreFecFlag,'brwaveRadioPostFecFlag':brwaveRadioPostFecFlag,'brwaveRadioLinkRate':brwaveRadioLinkRate,'brwaveRadioEvents':brwaveRadioEvents,'brwaveRadioEventsV2':brwaveRadioEventsV2,'brwaveErrorsOverThreshold':brwaveErrorsOverThreshold,'brwaveErrorsUnderThreshold':brwaveErrorsUnderThreshold,'brwaveUnitTemperatureAbnormal':brwaveUnitTemperatureAbnormal,'brwaveUnitTemperatureNormal':brwaveUnitTemperatureNormal,'brwaveTxTemperatureAbnormal':brwaveTxTemperatureAbnormal,'brwaveTxTemperatureNormal':brwaveTxTemperatureNormal,'brwaveInputVoltageAbnormal':brwaveInputVoltageAbnormal,'brwaveInputVoltageNormal':brwaveInputVoltageNormal,'brwaveRslNormal':brwaveRslNormal,'brwaveRslMinor':brwaveRslMinor,'brwaveRslMajor':brwaveRslMajor,'brwaveConfigChange':brwaveConfigChange,'brwaveLoginSuccessfull':brwaveLoginSuccessfull,'brwaveGeToFeSwitch':brwaveGeToFeSwitch,'brwaveFeToGeSwitch':brwaveFeToGeSwitch,'brwaveRadioTrapObjs':brwaveRadioTrapObjs,'managerIP':managerIP,'userName':userName,'brwaveConformance':brwaveConformance,'brwaveRadioGroups':brwaveRadioGroups,'brwaveCommonGroup':brwaveCommonGroup,'brwaveFactoryGroup':brwaveFactoryGroup,'brwaveStatusGroup':brwaveStatusGroup,'brwaveCompliances':brwaveCompliances})