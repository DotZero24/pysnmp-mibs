_n='adGenSlotOptionalGroup'
_m='adGenSlotBaseGroup'
_l='adGenSlotProdTransType'
_k='adGenSlotProdProductID'
_j='adGenSlotProdPhysAddress'
_i='adGenSlotProdSwVersion'
_h='adGenSlotProdRevision'
_g='adGenSlotProdSerialNumber'
_f='adGenSlotProdCLEIcode'
_e='adGenSlotProdPartNumber'
_d='adGenSlotProdName'
_c='adGenSlotUpTime'
_b='adGenSlotUpdateStatus'
_a='adGenSlotUpdateSoftware'
_Z='adGenSlotTFileName'
_Y='adGenSlotProvVersion'
_X='adGenSlotPortNumber'
_W='adGenSlotStatServiceState'
_V='adGenSlotFaceplate'
_U='adGenSlotAlarmStatus'
_T='adGenSlotTrapEnable'
_S='adGenSlotProduct'
_R='adGenSlotInfoState'
_Q='adGenSlotNumber'
_P='TruthValue'
_O='adGenSlotProvCpuRateLimitAlarmSlotSeverity'
_N='obsolete'
_M='ifIndex'
_L='ifDescr'
_K='IF-MIB'
_J='Integer32'
_I='read-write'
_H='sysName'
_G='SNMPv2-MIB'
_F='adTrapInformSeqNum'
_E='ADTRAN-GENTRAPINFORM-MIB'
_D='adGenSlotInfoIndex'
_C='read-only'
_B='ADTRAN-GENSLOT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenericShelves,=mibBuilder.importSymbols('ADTRAN-GENCHASSIS-MIB','adGenericShelves')
adTrapInformSeqNum,=mibBuilder.importSymbols(_E,_F)
AdPresence,AdProductIdentifier=mibBuilder.importSymbols('ADTRAN-TC','AdPresence','AdProductIdentifier')
ifDescr,ifIndex=mibBuilder.importSymbols(_K,_L,_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols(_G,_H)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_P)
adGenSlot=ModuleIdentity((1,3,6,1,4,1,664,5,13,2))
if mibBuilder.loadTexts:adGenSlot.setRevisions(('2017-03-29 00:00','2016-08-12 00:00','2016-03-14 00:00','2013-05-31 00:00','2012-12-06 00:00','2012-09-21 00:00','2011-10-13 00:00'))
_AdGenSlotNumber_Type=Integer32
_AdGenSlotNumber_Object=MibScalar
adGenSlotNumber=_AdGenSlotNumber_Object((1,3,6,1,4,1,664,5,13,2,1),_AdGenSlotNumber_Type())
adGenSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotNumber.setStatus(_A)
_AdGenSlotInfoTable_Object=MibTable
adGenSlotInfoTable=_AdGenSlotInfoTable_Object((1,3,6,1,4,1,664,5,13,2,3))
if mibBuilder.loadTexts:adGenSlotInfoTable.setStatus(_A)
_AdGenSlotInfoEntry_Object=MibTableRow
adGenSlotInfoEntry=_AdGenSlotInfoEntry_Object((1,3,6,1,4,1,664,5,13,2,3,1))
adGenSlotInfoEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:adGenSlotInfoEntry.setStatus(_A)
_AdGenSlotInfoIndex_Type=Integer32
_AdGenSlotInfoIndex_Object=MibTableColumn
adGenSlotInfoIndex=_AdGenSlotInfoIndex_Object((1,3,6,1,4,1,664,5,13,2,3,1,1),_AdGenSlotInfoIndex_Type())
adGenSlotInfoIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotInfoIndex.setStatus(_A)
_AdGenSlotInfoState_Type=AdPresence
_AdGenSlotInfoState_Object=MibTableColumn
adGenSlotInfoState=_AdGenSlotInfoState_Object((1,3,6,1,4,1,664,5,13,2,3,1,3),_AdGenSlotInfoState_Type())
adGenSlotInfoState.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotInfoState.setStatus(_A)
_AdGenSlotProduct_Type=AdProductIdentifier
_AdGenSlotProduct_Object=MibTableColumn
adGenSlotProduct=_AdGenSlotProduct_Object((1,3,6,1,4,1,664,5,13,2,3,1,4),_AdGenSlotProduct_Type())
adGenSlotProduct.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotProduct.setStatus(_A)
class _AdGenSlotTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enableTraps',1),('disableTraps',2)))
_AdGenSlotTrapEnable_Type.__name__=_J
_AdGenSlotTrapEnable_Object=MibTableColumn
adGenSlotTrapEnable=_AdGenSlotTrapEnable_Object((1,3,6,1,4,1,664,5,13,2,3,1,5),_AdGenSlotTrapEnable_Type())
adGenSlotTrapEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenSlotTrapEnable.setStatus(_A)
_AdGenSlotAlarmStatus_Type=OctetString
_AdGenSlotAlarmStatus_Object=MibTableColumn
adGenSlotAlarmStatus=_AdGenSlotAlarmStatus_Object((1,3,6,1,4,1,664,5,13,2,3,1,6),_AdGenSlotAlarmStatus_Type())
adGenSlotAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotAlarmStatus.setStatus(_A)
_AdGenSlotFaceplate_Type=OctetString
_AdGenSlotFaceplate_Object=MibTableColumn
adGenSlotFaceplate=_AdGenSlotFaceplate_Object((1,3,6,1,4,1,664,5,13,2,3,1,7),_AdGenSlotFaceplate_Type())
adGenSlotFaceplate.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotFaceplate.setStatus(_A)
class _AdGenSlotStatServiceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,8,9,10)));namedValues=NamedValues(*(('is',1),('oosUas',2),('oosMA',3),('fault',5),('isStbyHot',8),('isActLock',9),('isStbyLock',10)))
_AdGenSlotStatServiceState_Type.__name__=_J
_AdGenSlotStatServiceState_Object=MibTableColumn
adGenSlotStatServiceState=_AdGenSlotStatServiceState_Object((1,3,6,1,4,1,664,5,13,2,3,1,8),_AdGenSlotStatServiceState_Type())
adGenSlotStatServiceState.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenSlotStatServiceState.setStatus(_A)
_AdGenSlotPortNumber_Type=Integer32
_AdGenSlotPortNumber_Object=MibTableColumn
adGenSlotPortNumber=_AdGenSlotPortNumber_Object((1,3,6,1,4,1,664,5,13,2,3,1,9),_AdGenSlotPortNumber_Type())
adGenSlotPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotPortNumber.setStatus(_A)
_AdGenSlotProvVersion_Type=Integer32
_AdGenSlotProvVersion_Object=MibTableColumn
adGenSlotProvVersion=_AdGenSlotProvVersion_Object((1,3,6,1,4,1,664,5,13,2,3,1,10),_AdGenSlotProvVersion_Type())
adGenSlotProvVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotProvVersion.setStatus(_A)
_AdGenSlotTFileName_Type=DisplayString
_AdGenSlotTFileName_Object=MibTableColumn
adGenSlotTFileName=_AdGenSlotTFileName_Object((1,3,6,1,4,1,664,5,13,2,3,1,13),_AdGenSlotTFileName_Type())
adGenSlotTFileName.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenSlotTFileName.setStatus(_A)
class _AdGenSlotUpdateSoftware_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('initiate',1))
_AdGenSlotUpdateSoftware_Type.__name__=_J
_AdGenSlotUpdateSoftware_Object=MibTableColumn
adGenSlotUpdateSoftware=_AdGenSlotUpdateSoftware_Object((1,3,6,1,4,1,664,5,13,2,3,1,15),_AdGenSlotUpdateSoftware_Type())
adGenSlotUpdateSoftware.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenSlotUpdateSoftware.setStatus(_A)
_AdGenSlotUpdateStatus_Type=DisplayString
_AdGenSlotUpdateStatus_Object=MibTableColumn
adGenSlotUpdateStatus=_AdGenSlotUpdateStatus_Object((1,3,6,1,4,1,664,5,13,2,3,1,16),_AdGenSlotUpdateStatus_Type())
adGenSlotUpdateStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotUpdateStatus.setStatus(_A)
_AdGenSlotUpTime_Type=TimeTicks
_AdGenSlotUpTime_Object=MibTableColumn
adGenSlotUpTime=_AdGenSlotUpTime_Object((1,3,6,1,4,1,664,5,13,2,3,1,17),_AdGenSlotUpTime_Type())
adGenSlotUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotUpTime.setStatus(_A)
class _AdGenSlotServiceStateOOSMAAlarmEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AdGenSlotServiceStateOOSMAAlarmEnable_Type.__name__=_J
_AdGenSlotServiceStateOOSMAAlarmEnable_Object=MibTableColumn
adGenSlotServiceStateOOSMAAlarmEnable=_AdGenSlotServiceStateOOSMAAlarmEnable_Object((1,3,6,1,4,1,664,5,13,2,3,1,18),_AdGenSlotServiceStateOOSMAAlarmEnable_Type())
adGenSlotServiceStateOOSMAAlarmEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenSlotServiceStateOOSMAAlarmEnable.setStatus(_N)
_AdGenSlotPrimaryBuildDate_Type=DisplayString
_AdGenSlotPrimaryBuildDate_Object=MibTableColumn
adGenSlotPrimaryBuildDate=_AdGenSlotPrimaryBuildDate_Object((1,3,6,1,4,1,664,5,13,2,3,1,19),_AdGenSlotPrimaryBuildDate_Type())
adGenSlotPrimaryBuildDate.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotPrimaryBuildDate.setStatus(_A)
_AdGenSlotResetCause_Type=DisplayString
_AdGenSlotResetCause_Object=MibTableColumn
adGenSlotResetCause=_AdGenSlotResetCause_Object((1,3,6,1,4,1,664,5,13,2,3,1,20),_AdGenSlotResetCause_Type())
adGenSlotResetCause.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotResetCause.setStatus(_A)
_AdGenSlotWarmStartCauseIsValid_Type=TruthValue
_AdGenSlotWarmStartCauseIsValid_Object=MibTableColumn
adGenSlotWarmStartCauseIsValid=_AdGenSlotWarmStartCauseIsValid_Object((1,3,6,1,4,1,664,5,13,2,3,1,21),_AdGenSlotWarmStartCauseIsValid_Type())
adGenSlotWarmStartCauseIsValid.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotWarmStartCauseIsValid.setStatus(_A)
_AdGenSlotWarmStartCause_Type=DisplayString
_AdGenSlotWarmStartCause_Object=MibTableColumn
adGenSlotWarmStartCause=_AdGenSlotWarmStartCause_Object((1,3,6,1,4,1,664,5,13,2,3,1,22),_AdGenSlotWarmStartCause_Type())
adGenSlotWarmStartCause.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotWarmStartCause.setStatus(_A)
_AdGenSlotUpTimeSeconds_Type=Counter32
_AdGenSlotUpTimeSeconds_Object=MibTableColumn
adGenSlotUpTimeSeconds=_AdGenSlotUpTimeSeconds_Object((1,3,6,1,4,1,664,5,13,2,3,1,23),_AdGenSlotUpTimeSeconds_Type())
adGenSlotUpTimeSeconds.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotUpTimeSeconds.setStatus(_A)
_AdGenSlotProdTable_Object=MibTable
adGenSlotProdTable=_AdGenSlotProdTable_Object((1,3,6,1,4,1,664,5,13,2,4))
if mibBuilder.loadTexts:adGenSlotProdTable.setStatus(_A)
_AdGenSlotProdEntry_Object=MibTableRow
adGenSlotProdEntry=_AdGenSlotProdEntry_Object((1,3,6,1,4,1,664,5,13,2,4,1))
adGenSlotProdEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:adGenSlotProdEntry.setStatus(_A)
_AdGenSlotProdName_Type=DisplayString
_AdGenSlotProdName_Object=MibTableColumn
adGenSlotProdName=_AdGenSlotProdName_Object((1,3,6,1,4,1,664,5,13,2,4,1,1),_AdGenSlotProdName_Type())
adGenSlotProdName.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotProdName.setStatus(_A)
_AdGenSlotProdPartNumber_Type=DisplayString
_AdGenSlotProdPartNumber_Object=MibTableColumn
adGenSlotProdPartNumber=_AdGenSlotProdPartNumber_Object((1,3,6,1,4,1,664,5,13,2,4,1,2),_AdGenSlotProdPartNumber_Type())
adGenSlotProdPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotProdPartNumber.setStatus(_A)
_AdGenSlotProdCLEIcode_Type=DisplayString
_AdGenSlotProdCLEIcode_Object=MibTableColumn
adGenSlotProdCLEIcode=_AdGenSlotProdCLEIcode_Object((1,3,6,1,4,1,664,5,13,2,4,1,3),_AdGenSlotProdCLEIcode_Type())
adGenSlotProdCLEIcode.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotProdCLEIcode.setStatus(_A)
_AdGenSlotProdSerialNumber_Type=DisplayString
_AdGenSlotProdSerialNumber_Object=MibTableColumn
adGenSlotProdSerialNumber=_AdGenSlotProdSerialNumber_Object((1,3,6,1,4,1,664,5,13,2,4,1,4),_AdGenSlotProdSerialNumber_Type())
adGenSlotProdSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotProdSerialNumber.setStatus(_A)
_AdGenSlotProdRevision_Type=DisplayString
_AdGenSlotProdRevision_Object=MibTableColumn
adGenSlotProdRevision=_AdGenSlotProdRevision_Object((1,3,6,1,4,1,664,5,13,2,4,1,5),_AdGenSlotProdRevision_Type())
adGenSlotProdRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotProdRevision.setStatus(_A)
_AdGenSlotProdSwVersion_Type=DisplayString
_AdGenSlotProdSwVersion_Object=MibTableColumn
adGenSlotProdSwVersion=_AdGenSlotProdSwVersion_Object((1,3,6,1,4,1,664,5,13,2,4,1,6),_AdGenSlotProdSwVersion_Type())
adGenSlotProdSwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotProdSwVersion.setStatus(_A)
_AdGenSlotProdPhysAddress_Type=PhysAddress
_AdGenSlotProdPhysAddress_Object=MibTableColumn
adGenSlotProdPhysAddress=_AdGenSlotProdPhysAddress_Object((1,3,6,1,4,1,664,5,13,2,4,1,7),_AdGenSlotProdPhysAddress_Type())
adGenSlotProdPhysAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotProdPhysAddress.setStatus(_A)
_AdGenSlotProdProductID_Type=ObjectIdentifier
_AdGenSlotProdProductID_Object=MibTableColumn
adGenSlotProdProductID=_AdGenSlotProdProductID_Object((1,3,6,1,4,1,664,5,13,2,4,1,8),_AdGenSlotProdProductID_Type())
adGenSlotProdProductID.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotProdProductID.setStatus(_A)
_AdGenSlotProdTransType_Type=DisplayString
_AdGenSlotProdTransType_Object=MibTableColumn
adGenSlotProdTransType=_AdGenSlotProdTransType_Object((1,3,6,1,4,1,664,5,13,2,4,1,9),_AdGenSlotProdTransType_Type())
adGenSlotProdTransType.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenSlotProdTransType.setStatus(_A)
_AdGenSlotAlarmsPrefix_ObjectIdentity=ObjectIdentity
adGenSlotAlarmsPrefix=_AdGenSlotAlarmsPrefix_ObjectIdentity((1,3,6,1,4,1,664,5,13,2,5))
_AdGenSlotAlarms_ObjectIdentity=ObjectIdentity
adGenSlotAlarms=_AdGenSlotAlarms_ObjectIdentity((1,3,6,1,4,1,664,5,13,2,5,0))
_AdGenSlotProvCpuRateLimitAlarmSlotTable_Object=MibTable
adGenSlotProvCpuRateLimitAlarmSlotTable=_AdGenSlotProvCpuRateLimitAlarmSlotTable_Object((1,3,6,1,4,1,664,5,13,2,9))
if mibBuilder.loadTexts:adGenSlotProvCpuRateLimitAlarmSlotTable.setStatus(_A)
_AdGenSlotProvCpuRateLimitAlarmSlotEntry_Object=MibTableRow
adGenSlotProvCpuRateLimitAlarmSlotEntry=_AdGenSlotProvCpuRateLimitAlarmSlotEntry_Object((1,3,6,1,4,1,664,5,13,2,9,1))
adGenSlotProvCpuRateLimitAlarmSlotEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:adGenSlotProvCpuRateLimitAlarmSlotEntry.setStatus(_A)
class _AdGenSlotProvCpuRateLimitAlarmSlotSeverity_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,5,6)));namedValues=NamedValues(*(('minor',4),('major',5),('critical',6)))
_AdGenSlotProvCpuRateLimitAlarmSlotSeverity_Type.__name__=_J
_AdGenSlotProvCpuRateLimitAlarmSlotSeverity_Object=MibTableColumn
adGenSlotProvCpuRateLimitAlarmSlotSeverity=_AdGenSlotProvCpuRateLimitAlarmSlotSeverity_Object((1,3,6,1,4,1,664,5,13,2,9,1,1),_AdGenSlotProvCpuRateLimitAlarmSlotSeverity_Type())
adGenSlotProvCpuRateLimitAlarmSlotSeverity.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenSlotProvCpuRateLimitAlarmSlotSeverity.setStatus(_A)
class _AdGenSlotProvCpuRateLimitAlarmSlotEnable_Type(TruthValue):defaultValue=1
_AdGenSlotProvCpuRateLimitAlarmSlotEnable_Type.__name__=_P
_AdGenSlotProvCpuRateLimitAlarmSlotEnable_Object=MibTableColumn
adGenSlotProvCpuRateLimitAlarmSlotEnable=_AdGenSlotProvCpuRateLimitAlarmSlotEnable_Object((1,3,6,1,4,1,664,5,13,2,9,1,2),_AdGenSlotProvCpuRateLimitAlarmSlotEnable_Type())
adGenSlotProvCpuRateLimitAlarmSlotEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenSlotProvCpuRateLimitAlarmSlotEnable.setStatus(_A)
_AdGenSlotConformance_ObjectIdentity=ObjectIdentity
adGenSlotConformance=_AdGenSlotConformance_ObjectIdentity((1,3,6,1,4,1,664,5,13,2,99))
_AdGenSlotCompliances_ObjectIdentity=ObjectIdentity
adGenSlotCompliances=_AdGenSlotCompliances_ObjectIdentity((1,3,6,1,4,1,664,5,13,2,99,1))
_AdGenSlotMIBGroups_ObjectIdentity=ObjectIdentity
adGenSlotMIBGroups=_AdGenSlotMIBGroups_ObjectIdentity((1,3,6,1,4,1,664,5,13,2,99,2))
adGenSlotBaseGroup=ObjectGroup((1,3,6,1,4,1,664,5,13,2,99,2,1))
adGenSlotBaseGroup.setObjects(*((_B,_Q),(_B,_D),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:adGenSlotBaseGroup.setStatus(_A)
adGenSlotOptionalGroup=ObjectGroup((1,3,6,1,4,1,664,5,13,2,99,2,2))
adGenSlotOptionalGroup.setObjects(*((_B,_k),(_B,_l)))
if mibBuilder.loadTexts:adGenSlotOptionalGroup.setStatus(_A)
adGenSlotServiceStateOOSMAClear=NotificationType((1,3,6,1,4,1,664,5,13,2,5,0,1))
adGenSlotServiceStateOOSMAClear.setObjects(*((_E,_F),(_G,_H),(_B,_D)))
if mibBuilder.loadTexts:adGenSlotServiceStateOOSMAClear.setStatus(_N)
adGenSlotServiceStateOOSMAActive=NotificationType((1,3,6,1,4,1,664,5,13,2,5,0,2))
adGenSlotServiceStateOOSMAActive.setObjects(*((_E,_F),(_G,_H),(_B,_D)))
if mibBuilder.loadTexts:adGenSlotServiceStateOOSMAActive.setStatus(_N)
adGenSlotFpgaBistFailureClear=NotificationType((1,3,6,1,4,1,664,5,13,2,5,0,3))
adGenSlotFpgaBistFailureClear.setObjects(*((_E,_F),(_G,_H),(_B,_D)))
if mibBuilder.loadTexts:adGenSlotFpgaBistFailureClear.setStatus(_A)
adGenSlotFpgaBistFailureActive=NotificationType((1,3,6,1,4,1,664,5,13,2,5,0,4))
adGenSlotFpgaBistFailureActive.setObjects(*((_E,_F),(_G,_H),(_B,_D)))
if mibBuilder.loadTexts:adGenSlotFpgaBistFailureActive.setStatus(_A)
adGenSlotCpuRateLimitAlarmClear=NotificationType((1,3,6,1,4,1,664,5,13,2,5,0,5))
adGenSlotCpuRateLimitAlarmClear.setObjects(*((_E,_F),(_G,_H),(_K,_L),(_K,_M),(_B,_O)))
if mibBuilder.loadTexts:adGenSlotCpuRateLimitAlarmClear.setStatus(_A)
adGenSlotCpuRateLimitAlarmActive=NotificationType((1,3,6,1,4,1,664,5,13,2,5,0,6))
adGenSlotCpuRateLimitAlarmActive.setObjects(*((_E,_F),(_G,_H),(_K,_L),(_K,_M),(_B,_O)))
if mibBuilder.loadTexts:adGenSlotCpuRateLimitAlarmActive.setStatus(_A)
adGenSlotCompliance=ModuleCompliance((1,3,6,1,4,1,664,5,13,2,99,1,1))
adGenSlotCompliance.setObjects(*((_B,_m),(_B,_n)))
if mibBuilder.loadTexts:adGenSlotCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenSlot':adGenSlot,_Q:adGenSlotNumber,'adGenSlotInfoTable':adGenSlotInfoTable,'adGenSlotInfoEntry':adGenSlotInfoEntry,_D:adGenSlotInfoIndex,_R:adGenSlotInfoState,_S:adGenSlotProduct,_T:adGenSlotTrapEnable,_U:adGenSlotAlarmStatus,_V:adGenSlotFaceplate,_W:adGenSlotStatServiceState,_X:adGenSlotPortNumber,_Y:adGenSlotProvVersion,_Z:adGenSlotTFileName,_a:adGenSlotUpdateSoftware,_b:adGenSlotUpdateStatus,_c:adGenSlotUpTime,'adGenSlotServiceStateOOSMAAlarmEnable':adGenSlotServiceStateOOSMAAlarmEnable,'adGenSlotPrimaryBuildDate':adGenSlotPrimaryBuildDate,'adGenSlotResetCause':adGenSlotResetCause,'adGenSlotWarmStartCauseIsValid':adGenSlotWarmStartCauseIsValid,'adGenSlotWarmStartCause':adGenSlotWarmStartCause,'adGenSlotUpTimeSeconds':adGenSlotUpTimeSeconds,'adGenSlotProdTable':adGenSlotProdTable,'adGenSlotProdEntry':adGenSlotProdEntry,_d:adGenSlotProdName,_e:adGenSlotProdPartNumber,_f:adGenSlotProdCLEIcode,_g:adGenSlotProdSerialNumber,_h:adGenSlotProdRevision,_i:adGenSlotProdSwVersion,_j:adGenSlotProdPhysAddress,_k:adGenSlotProdProductID,_l:adGenSlotProdTransType,'adGenSlotAlarmsPrefix':adGenSlotAlarmsPrefix,'adGenSlotAlarms':adGenSlotAlarms,'adGenSlotServiceStateOOSMAClear':adGenSlotServiceStateOOSMAClear,'adGenSlotServiceStateOOSMAActive':adGenSlotServiceStateOOSMAActive,'adGenSlotFpgaBistFailureClear':adGenSlotFpgaBistFailureClear,'adGenSlotFpgaBistFailureActive':adGenSlotFpgaBistFailureActive,'adGenSlotCpuRateLimitAlarmClear':adGenSlotCpuRateLimitAlarmClear,'adGenSlotCpuRateLimitAlarmActive':adGenSlotCpuRateLimitAlarmActive,'adGenSlotProvCpuRateLimitAlarmSlotTable':adGenSlotProvCpuRateLimitAlarmSlotTable,'adGenSlotProvCpuRateLimitAlarmSlotEntry':adGenSlotProvCpuRateLimitAlarmSlotEntry,_O:adGenSlotProvCpuRateLimitAlarmSlotSeverity,'adGenSlotProvCpuRateLimitAlarmSlotEnable':adGenSlotProvCpuRateLimitAlarmSlotEnable,'adGenSlotConformance':adGenSlotConformance,'adGenSlotCompliances':adGenSlotCompliances,'adGenSlotCompliance':adGenSlotCompliance,'adGenSlotMIBGroups':adGenSlotMIBGroups,_m:adGenSlotBaseGroup,_n:adGenSlotOptionalGroup})