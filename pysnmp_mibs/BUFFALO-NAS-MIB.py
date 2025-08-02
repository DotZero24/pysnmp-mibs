_c='nasInformationDateAndTime'
_b='nasInformationDate'
_a='nasInformationMsg'
_Z='nasErrorDateAndTime'
_Y='nasErrorDate'
_X='nasErrorMsg'
_W='nasISCSIIndex'
_V='nasRPSUIndex'
_U='nasPVIndex'
_T='nasLVIndex'
_S='nasInformationIndex'
_R='nasErrorIndex'
_Q='nasArrayIndex'
_P='notSupport'
_O='nasDiskIndex'
_N='nasBackupIndex'
_M='nasVGIndex'
_L='fail'
_K='unavailable'
_J='normal'
_I='OctetString'
_H='not-accessible'
_G='BUFFALO-NAS-MIB'
_F='on'
_E='off'
_D='unknown'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
buffalo,=mibBuilder.importSymbols('BUFFALO-ROOT-MIB','buffalo')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
teraStation=ModuleIdentity((1,3,6,1,4,1,5227,27))
if mibBuilder.loadTexts:teraStation.setRevisions(('2020-03-09 00:00',))
class DayOfWeek(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('sun',1),('mon',2),('tue',3),('wed',4),('thu',5),('fri',6),('sat',7)))
class LongUTF8String(TextualConvention,OctetString):status=_A;displayHint='255t';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1024))
_TeraStationObjects_ObjectIdentity=ObjectIdentity
teraStationObjects=_TeraStationObjects_ObjectIdentity((1,3,6,1,4,1,5227,27,1))
_NasBackupTable_Object=MibTable
nasBackupTable=_NasBackupTable_Object((1,3,6,1,4,1,5227,27,1,1))
if mibBuilder.loadTexts:nasBackupTable.setStatus(_A)
_NasBackupEntry_Object=MibTableRow
nasBackupEntry=_NasBackupEntry_Object((1,3,6,1,4,1,5227,27,1,1,1))
nasBackupEntry.setIndexNames((0,_G,_N))
if mibBuilder.loadTexts:nasBackupEntry.setStatus(_A)
class _NasBackupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_NasBackupIndex_Type.__name__=_C
_NasBackupIndex_Object=MibTableColumn
nasBackupIndex=_NasBackupIndex_Object((1,3,6,1,4,1,5227,27,1,1,1,1),_NasBackupIndex_Type())
nasBackupIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:nasBackupIndex.setStatus(_A)
class _NasBackupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ready',1),('run',2),('done',3),('error',4)))
_NasBackupStatus_Type.__name__=_C
_NasBackupStatus_Object=MibTableColumn
nasBackupStatus=_NasBackupStatus_Object((1,3,6,1,4,1,5227,27,1,1,1,3),_NasBackupStatus_Type())
nasBackupStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nasBackupStatus.setStatus(_A)
_NasDiskTable_Object=MibTable
nasDiskTable=_NasDiskTable_Object((1,3,6,1,4,1,5227,27,1,2))
if mibBuilder.loadTexts:nasDiskTable.setStatus(_A)
_NasDiskEntry_Object=MibTableRow
nasDiskEntry=_NasDiskEntry_Object((1,3,6,1,4,1,5227,27,1,2,1))
nasDiskEntry.setIndexNames((0,_G,_O))
if mibBuilder.loadTexts:nasDiskEntry.setStatus(_A)
_NasDiskIndex_Type=Integer32
_NasDiskIndex_Object=MibTableColumn
nasDiskIndex=_NasDiskIndex_Object((1,3,6,1,4,1,5227,27,1,2,1,1),_NasDiskIndex_Type())
nasDiskIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:nasDiskIndex.setStatus(_A)
class _NasDiskStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_P,-1),(_J,1),('array1',2),('array2',3),('standby',4),('degrade',5),('remove',6),('standbyRemoved',7),('degradeRemoved',8),('removeRemoved',9),('array3',10),('array4',11),('mediaCartridge',12),('array5',13),('array6',14)))
_NasDiskStatus_Type.__name__=_C
_NasDiskStatus_Object=MibTableColumn
nasDiskStatus=_NasDiskStatus_Object((1,3,6,1,4,1,5227,27,1,2,1,2),_NasDiskStatus_Type())
nasDiskStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskStatus.setStatus(_A)
_NasDiskCapacity_Type=Integer32
_NasDiskCapacity_Object=MibTableColumn
nasDiskCapacity=_NasDiskCapacity_Object((1,3,6,1,4,1,5227,27,1,2,1,3),_NasDiskCapacity_Type())
nasDiskCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskCapacity.setStatus(_A)
class _NasDiskUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_NasDiskUsed_Type.__name__=_C
_NasDiskUsed_Object=MibTableColumn
nasDiskUsed=_NasDiskUsed_Object((1,3,6,1,4,1,5227,27,1,2,1,4),_NasDiskUsed_Type())
nasDiskUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskUsed.setStatus(_A)
if mibBuilder.loadTexts:nasDiskUsed.setUnits('%')
class _NasDiskSMARTStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-2,-1,1,2,3)));namedValues=NamedValues(*((_K,-2),(_D,-1),(_J,1),('caution',2),(_L,3)))
_NasDiskSMARTStatus_Type.__name__=_C
_NasDiskSMARTStatus_Object=MibTableColumn
nasDiskSMARTStatus=_NasDiskSMARTStatus_Object((1,3,6,1,4,1,5227,27,1,2,1,5),_NasDiskSMARTStatus_Type())
nasDiskSMARTStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTStatus.setStatus(_A)
_NasDiskSMARTReallocatedSectorCtValue_Type=Integer32
_NasDiskSMARTReallocatedSectorCtValue_Object=MibTableColumn
nasDiskSMARTReallocatedSectorCtValue=_NasDiskSMARTReallocatedSectorCtValue_Object((1,3,6,1,4,1,5227,27,1,2,1,6),_NasDiskSMARTReallocatedSectorCtValue_Type())
nasDiskSMARTReallocatedSectorCtValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTReallocatedSectorCtValue.setStatus(_A)
_NasDiskSMARTReallocatedSectorCtWorst_Type=Integer32
_NasDiskSMARTReallocatedSectorCtWorst_Object=MibTableColumn
nasDiskSMARTReallocatedSectorCtWorst=_NasDiskSMARTReallocatedSectorCtWorst_Object((1,3,6,1,4,1,5227,27,1,2,1,7),_NasDiskSMARTReallocatedSectorCtWorst_Type())
nasDiskSMARTReallocatedSectorCtWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTReallocatedSectorCtWorst.setStatus(_A)
_NasDiskSMARTReallocatedSectorCtThresh_Type=Integer32
_NasDiskSMARTReallocatedSectorCtThresh_Object=MibTableColumn
nasDiskSMARTReallocatedSectorCtThresh=_NasDiskSMARTReallocatedSectorCtThresh_Object((1,3,6,1,4,1,5227,27,1,2,1,8),_NasDiskSMARTReallocatedSectorCtThresh_Type())
nasDiskSMARTReallocatedSectorCtThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTReallocatedSectorCtThresh.setStatus(_A)
_NasDiskSMARTReallocatedSectorCtRAW_Type=DisplayString
_NasDiskSMARTReallocatedSectorCtRAW_Object=MibTableColumn
nasDiskSMARTReallocatedSectorCtRAW=_NasDiskSMARTReallocatedSectorCtRAW_Object((1,3,6,1,4,1,5227,27,1,2,1,9),_NasDiskSMARTReallocatedSectorCtRAW_Type())
nasDiskSMARTReallocatedSectorCtRAW.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTReallocatedSectorCtRAW.setStatus(_A)
_NasDiskSMARTCurrentPendingSectorValue_Type=Integer32
_NasDiskSMARTCurrentPendingSectorValue_Object=MibTableColumn
nasDiskSMARTCurrentPendingSectorValue=_NasDiskSMARTCurrentPendingSectorValue_Object((1,3,6,1,4,1,5227,27,1,2,1,10),_NasDiskSMARTCurrentPendingSectorValue_Type())
nasDiskSMARTCurrentPendingSectorValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTCurrentPendingSectorValue.setStatus(_A)
_NasDiskSMARTCurrentPendingSectorWorst_Type=Integer32
_NasDiskSMARTCurrentPendingSectorWorst_Object=MibTableColumn
nasDiskSMARTCurrentPendingSectorWorst=_NasDiskSMARTCurrentPendingSectorWorst_Object((1,3,6,1,4,1,5227,27,1,2,1,11),_NasDiskSMARTCurrentPendingSectorWorst_Type())
nasDiskSMARTCurrentPendingSectorWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTCurrentPendingSectorWorst.setStatus(_A)
_NasDiskSMARTCurrentPendingSectorThresh_Type=Integer32
_NasDiskSMARTCurrentPendingSectorThresh_Object=MibTableColumn
nasDiskSMARTCurrentPendingSectorThresh=_NasDiskSMARTCurrentPendingSectorThresh_Object((1,3,6,1,4,1,5227,27,1,2,1,12),_NasDiskSMARTCurrentPendingSectorThresh_Type())
nasDiskSMARTCurrentPendingSectorThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTCurrentPendingSectorThresh.setStatus(_A)
_NasDiskSMARTCurrentPendingSectorRAW_Type=DisplayString
_NasDiskSMARTCurrentPendingSectorRAW_Object=MibTableColumn
nasDiskSMARTCurrentPendingSectorRAW=_NasDiskSMARTCurrentPendingSectorRAW_Object((1,3,6,1,4,1,5227,27,1,2,1,13),_NasDiskSMARTCurrentPendingSectorRAW_Type())
nasDiskSMARTCurrentPendingSectorRAW.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTCurrentPendingSectorRAW.setStatus(_A)
_NasDiskSMARTOfflineUncorrectableValue_Type=Integer32
_NasDiskSMARTOfflineUncorrectableValue_Object=MibTableColumn
nasDiskSMARTOfflineUncorrectableValue=_NasDiskSMARTOfflineUncorrectableValue_Object((1,3,6,1,4,1,5227,27,1,2,1,14),_NasDiskSMARTOfflineUncorrectableValue_Type())
nasDiskSMARTOfflineUncorrectableValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTOfflineUncorrectableValue.setStatus(_A)
_NasDiskSMARTOfflineUncorrectableWorst_Type=Integer32
_NasDiskSMARTOfflineUncorrectableWorst_Object=MibTableColumn
nasDiskSMARTOfflineUncorrectableWorst=_NasDiskSMARTOfflineUncorrectableWorst_Object((1,3,6,1,4,1,5227,27,1,2,1,15),_NasDiskSMARTOfflineUncorrectableWorst_Type())
nasDiskSMARTOfflineUncorrectableWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTOfflineUncorrectableWorst.setStatus(_A)
_NasDiskSMARTOfflineUncorrectableThresh_Type=Integer32
_NasDiskSMARTOfflineUncorrectableThresh_Object=MibTableColumn
nasDiskSMARTOfflineUncorrectableThresh=_NasDiskSMARTOfflineUncorrectableThresh_Object((1,3,6,1,4,1,5227,27,1,2,1,16),_NasDiskSMARTOfflineUncorrectableThresh_Type())
nasDiskSMARTOfflineUncorrectableThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTOfflineUncorrectableThresh.setStatus(_A)
_NasDiskSMARTOfflineUncorrectableRAW_Type=DisplayString
_NasDiskSMARTOfflineUncorrectableRAW_Object=MibTableColumn
nasDiskSMARTOfflineUncorrectableRAW=_NasDiskSMARTOfflineUncorrectableRAW_Object((1,3,6,1,4,1,5227,27,1,2,1,17),_NasDiskSMARTOfflineUncorrectableRAW_Type())
nasDiskSMARTOfflineUncorrectableRAW.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTOfflineUncorrectableRAW.setStatus(_A)
_NasSSDSMARTRemainingLifeValue_Type=Integer32
_NasSSDSMARTRemainingLifeValue_Object=MibTableColumn
nasSSDSMARTRemainingLifeValue=_NasSSDSMARTRemainingLifeValue_Object((1,3,6,1,4,1,5227,27,1,2,1,18),_NasSSDSMARTRemainingLifeValue_Type())
nasSSDSMARTRemainingLifeValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nasSSDSMARTRemainingLifeValue.setStatus(_A)
_NasSSDSMARTRemainingLifeWorst_Type=Integer32
_NasSSDSMARTRemainingLifeWorst_Object=MibTableColumn
nasSSDSMARTRemainingLifeWorst=_NasSSDSMARTRemainingLifeWorst_Object((1,3,6,1,4,1,5227,27,1,2,1,19),_NasSSDSMARTRemainingLifeWorst_Type())
nasSSDSMARTRemainingLifeWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:nasSSDSMARTRemainingLifeWorst.setStatus(_A)
_NasSSDSMARTRemainingLifeThresh_Type=Integer32
_NasSSDSMARTRemainingLifeThresh_Object=MibTableColumn
nasSSDSMARTRemainingLifeThresh=_NasSSDSMARTRemainingLifeThresh_Object((1,3,6,1,4,1,5227,27,1,2,1,20),_NasSSDSMARTRemainingLifeThresh_Type())
nasSSDSMARTRemainingLifeThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:nasSSDSMARTRemainingLifeThresh.setStatus(_A)
_NasSSDSMARTBadBlockCountValue_Type=Integer32
_NasSSDSMARTBadBlockCountValue_Object=MibTableColumn
nasSSDSMARTBadBlockCountValue=_NasSSDSMARTBadBlockCountValue_Object((1,3,6,1,4,1,5227,27,1,2,1,21),_NasSSDSMARTBadBlockCountValue_Type())
nasSSDSMARTBadBlockCountValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nasSSDSMARTBadBlockCountValue.setStatus(_A)
_NasSSDSMARTBadBlockCountWorst_Type=Integer32
_NasSSDSMARTBadBlockCountWorst_Object=MibTableColumn
nasSSDSMARTBadBlockCountWorst=_NasSSDSMARTBadBlockCountWorst_Object((1,3,6,1,4,1,5227,27,1,2,1,22),_NasSSDSMARTBadBlockCountWorst_Type())
nasSSDSMARTBadBlockCountWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:nasSSDSMARTBadBlockCountWorst.setStatus(_A)
_NasSSDSMARTBadBlockCountThresh_Type=Integer32
_NasSSDSMARTBadBlockCountThresh_Object=MibTableColumn
nasSSDSMARTBadBlockCountThresh=_NasSSDSMARTBadBlockCountThresh_Object((1,3,6,1,4,1,5227,27,1,2,1,23),_NasSSDSMARTBadBlockCountThresh_Type())
nasSSDSMARTBadBlockCountThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:nasSSDSMARTBadBlockCountThresh.setStatus(_A)
_NasDiskCapacityGiB_Type=Integer32
_NasDiskCapacityGiB_Object=MibTableColumn
nasDiskCapacityGiB=_NasDiskCapacityGiB_Object((1,3,6,1,4,1,5227,27,1,2,1,24),_NasDiskCapacityGiB_Type())
nasDiskCapacityGiB.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskCapacityGiB.setStatus(_A)
_NasDiskCapacityLow_Type=Unsigned32
_NasDiskCapacityLow_Object=MibTableColumn
nasDiskCapacityLow=_NasDiskCapacityLow_Object((1,3,6,1,4,1,5227,27,1,2,1,25),_NasDiskCapacityLow_Type())
nasDiskCapacityLow.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskCapacityLow.setStatus(_A)
_NasDiskCapacityHigh_Type=Unsigned32
_NasDiskCapacityHigh_Object=MibTableColumn
nasDiskCapacityHigh=_NasDiskCapacityHigh_Object((1,3,6,1,4,1,5227,27,1,2,1,26),_NasDiskCapacityHigh_Type())
nasDiskCapacityHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskCapacityHigh.setStatus(_A)
_NasDiskUsedGiB_Type=Integer32
_NasDiskUsedGiB_Object=MibTableColumn
nasDiskUsedGiB=_NasDiskUsedGiB_Object((1,3,6,1,4,1,5227,27,1,2,1,27),_NasDiskUsedGiB_Type())
nasDiskUsedGiB.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskUsedGiB.setStatus(_A)
_NasDiskUsedLow_Type=Unsigned32
_NasDiskUsedLow_Object=MibTableColumn
nasDiskUsedLow=_NasDiskUsedLow_Object((1,3,6,1,4,1,5227,27,1,2,1,28),_NasDiskUsedLow_Type())
nasDiskUsedLow.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskUsedLow.setStatus(_A)
_NasDiskUsedHigh_Type=Unsigned32
_NasDiskUsedHigh_Object=MibTableColumn
nasDiskUsedHigh=_NasDiskUsedHigh_Object((1,3,6,1,4,1,5227,27,1,2,1,29),_NasDiskUsedHigh_Type())
nasDiskUsedHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskUsedHigh.setStatus(_A)
_NasDiskModelName_Type=DisplayString
_NasDiskModelName_Object=MibTableColumn
nasDiskModelName=_NasDiskModelName_Object((1,3,6,1,4,1,5227,27,1,2,1,30),_NasDiskModelName_Type())
nasDiskModelName.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskModelName.setStatus(_A)
class _NasDiskSMARTReallocatedSectorCtHealth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-2,1,3)));namedValues=NamedValues(*((_K,-2),(_J,1),(_L,3)))
_NasDiskSMARTReallocatedSectorCtHealth_Type.__name__=_C
_NasDiskSMARTReallocatedSectorCtHealth_Object=MibTableColumn
nasDiskSMARTReallocatedSectorCtHealth=_NasDiskSMARTReallocatedSectorCtHealth_Object((1,3,6,1,4,1,5227,27,1,2,1,31),_NasDiskSMARTReallocatedSectorCtHealth_Type())
nasDiskSMARTReallocatedSectorCtHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTReallocatedSectorCtHealth.setStatus(_A)
class _NasDiskSMARTCurrentPendingSectorHealth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-2,1,3)));namedValues=NamedValues(*((_K,-2),(_J,1),(_L,3)))
_NasDiskSMARTCurrentPendingSectorHealth_Type.__name__=_C
_NasDiskSMARTCurrentPendingSectorHealth_Object=MibTableColumn
nasDiskSMARTCurrentPendingSectorHealth=_NasDiskSMARTCurrentPendingSectorHealth_Object((1,3,6,1,4,1,5227,27,1,2,1,32),_NasDiskSMARTCurrentPendingSectorHealth_Type())
nasDiskSMARTCurrentPendingSectorHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTCurrentPendingSectorHealth.setStatus(_A)
class _NasDiskSMARTOfflineUncorrectableHealth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-2,1,3)));namedValues=NamedValues(*((_K,-2),(_J,1),(_L,3)))
_NasDiskSMARTOfflineUncorrectableHealth_Type.__name__=_C
_NasDiskSMARTOfflineUncorrectableHealth_Object=MibTableColumn
nasDiskSMARTOfflineUncorrectableHealth=_NasDiskSMARTOfflineUncorrectableHealth_Object((1,3,6,1,4,1,5227,27,1,2,1,33),_NasDiskSMARTOfflineUncorrectableHealth_Type())
nasDiskSMARTOfflineUncorrectableHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTOfflineUncorrectableHealth.setStatus(_A)
_NasDiskSMARTRawReadErrorRateValue_Type=Integer32
_NasDiskSMARTRawReadErrorRateValue_Object=MibTableColumn
nasDiskSMARTRawReadErrorRateValue=_NasDiskSMARTRawReadErrorRateValue_Object((1,3,6,1,4,1,5227,27,1,2,1,34),_NasDiskSMARTRawReadErrorRateValue_Type())
nasDiskSMARTRawReadErrorRateValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTRawReadErrorRateValue.setStatus(_A)
_NasDiskSMARTRawReadErrorRateWorst_Type=Integer32
_NasDiskSMARTRawReadErrorRateWorst_Object=MibTableColumn
nasDiskSMARTRawReadErrorRateWorst=_NasDiskSMARTRawReadErrorRateWorst_Object((1,3,6,1,4,1,5227,27,1,2,1,35),_NasDiskSMARTRawReadErrorRateWorst_Type())
nasDiskSMARTRawReadErrorRateWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTRawReadErrorRateWorst.setStatus(_A)
_NasDiskSMARTRawReadErrorRateThresh_Type=Integer32
_NasDiskSMARTRawReadErrorRateThresh_Object=MibTableColumn
nasDiskSMARTRawReadErrorRateThresh=_NasDiskSMARTRawReadErrorRateThresh_Object((1,3,6,1,4,1,5227,27,1,2,1,36),_NasDiskSMARTRawReadErrorRateThresh_Type())
nasDiskSMARTRawReadErrorRateThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTRawReadErrorRateThresh.setStatus(_A)
_NasDiskSMARTRawReadErrorRateRAW_Type=DisplayString
_NasDiskSMARTRawReadErrorRateRAW_Object=MibTableColumn
nasDiskSMARTRawReadErrorRateRAW=_NasDiskSMARTRawReadErrorRateRAW_Object((1,3,6,1,4,1,5227,27,1,2,1,37),_NasDiskSMARTRawReadErrorRateRAW_Type())
nasDiskSMARTRawReadErrorRateRAW.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTRawReadErrorRateRAW.setStatus(_A)
_NasDiskSMARTRawReadErrorRateHealth_Type=Integer32
_NasDiskSMARTRawReadErrorRateHealth_Object=MibTableColumn
nasDiskSMARTRawReadErrorRateHealth=_NasDiskSMARTRawReadErrorRateHealth_Object((1,3,6,1,4,1,5227,27,1,2,1,38),_NasDiskSMARTRawReadErrorRateHealth_Type())
nasDiskSMARTRawReadErrorRateHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTRawReadErrorRateHealth.setStatus(_A)
_NasDiskSMARTPowerOnHoursValue_Type=Integer32
_NasDiskSMARTPowerOnHoursValue_Object=MibTableColumn
nasDiskSMARTPowerOnHoursValue=_NasDiskSMARTPowerOnHoursValue_Object((1,3,6,1,4,1,5227,27,1,2,1,39),_NasDiskSMARTPowerOnHoursValue_Type())
nasDiskSMARTPowerOnHoursValue.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTPowerOnHoursValue.setStatus(_A)
_NasDiskSMARTPowerOnHoursWorst_Type=Integer32
_NasDiskSMARTPowerOnHoursWorst_Object=MibTableColumn
nasDiskSMARTPowerOnHoursWorst=_NasDiskSMARTPowerOnHoursWorst_Object((1,3,6,1,4,1,5227,27,1,2,1,40),_NasDiskSMARTPowerOnHoursWorst_Type())
nasDiskSMARTPowerOnHoursWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTPowerOnHoursWorst.setStatus(_A)
_NasDiskSMARTPowerOnHoursThresh_Type=Integer32
_NasDiskSMARTPowerOnHoursThresh_Object=MibTableColumn
nasDiskSMARTPowerOnHoursThresh=_NasDiskSMARTPowerOnHoursThresh_Object((1,3,6,1,4,1,5227,27,1,2,1,41),_NasDiskSMARTPowerOnHoursThresh_Type())
nasDiskSMARTPowerOnHoursThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTPowerOnHoursThresh.setStatus(_A)
_NasDiskSMARTPowerOnHoursRAW_Type=DisplayString
_NasDiskSMARTPowerOnHoursRAW_Object=MibTableColumn
nasDiskSMARTPowerOnHoursRAW=_NasDiskSMARTPowerOnHoursRAW_Object((1,3,6,1,4,1,5227,27,1,2,1,42),_NasDiskSMARTPowerOnHoursRAW_Type())
nasDiskSMARTPowerOnHoursRAW.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTPowerOnHoursRAW.setStatus(_A)
_NasDiskSMARTPowerOnHoursHealth_Type=Integer32
_NasDiskSMARTPowerOnHoursHealth_Object=MibTableColumn
nasDiskSMARTPowerOnHoursHealth=_NasDiskSMARTPowerOnHoursHealth_Object((1,3,6,1,4,1,5227,27,1,2,1,43),_NasDiskSMARTPowerOnHoursHealth_Type())
nasDiskSMARTPowerOnHoursHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:nasDiskSMARTPowerOnHoursHealth.setStatus(_A)
_NasArrayTable_Object=MibTable
nasArrayTable=_NasArrayTable_Object((1,3,6,1,4,1,5227,27,1,3))
if mibBuilder.loadTexts:nasArrayTable.setStatus(_A)
_NasArrayEntry_Object=MibTableRow
nasArrayEntry=_NasArrayEntry_Object((1,3,6,1,4,1,5227,27,1,3,1))
nasArrayEntry.setIndexNames((0,_G,_Q))
if mibBuilder.loadTexts:nasArrayEntry.setStatus(_A)
_NasArrayIndex_Type=Integer32
_NasArrayIndex_Object=MibTableColumn
nasArrayIndex=_NasArrayIndex_Object((1,3,6,1,4,1,5227,27,1,3,1,1),_NasArrayIndex_Type())
nasArrayIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:nasArrayIndex.setStatus(_A)
class _NasArrayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_P,-1),(_E,1),('raid0',2),('raid1',3),('raid5',4),('raid6',5),('raid10',6),('raid50',7),('raid51',8),('raid60',9),('raid61',10)))
_NasArrayStatus_Type.__name__=_C
_NasArrayStatus_Object=MibTableColumn
nasArrayStatus=_NasArrayStatus_Object((1,3,6,1,4,1,5227,27,1,3,1,2),_NasArrayStatus_Type())
nasArrayStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nasArrayStatus.setStatus(_A)
_NasArrayCapacity_Type=Integer32
_NasArrayCapacity_Object=MibTableColumn
nasArrayCapacity=_NasArrayCapacity_Object((1,3,6,1,4,1,5227,27,1,3,1,3),_NasArrayCapacity_Type())
nasArrayCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:nasArrayCapacity.setStatus(_A)
class _NasArrayUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_NasArrayUsed_Type.__name__=_C
_NasArrayUsed_Object=MibTableColumn
nasArrayUsed=_NasArrayUsed_Object((1,3,6,1,4,1,5227,27,1,3,1,4),_NasArrayUsed_Type())
nasArrayUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:nasArrayUsed.setStatus(_A)
if mibBuilder.loadTexts:nasArrayUsed.setUnits('%')
_NasArrayCapacityGiB_Type=Integer32
_NasArrayCapacityGiB_Object=MibTableColumn
nasArrayCapacityGiB=_NasArrayCapacityGiB_Object((1,3,6,1,4,1,5227,27,1,3,1,5),_NasArrayCapacityGiB_Type())
nasArrayCapacityGiB.setMaxAccess(_B)
if mibBuilder.loadTexts:nasArrayCapacityGiB.setStatus(_A)
_NasArrayCapacityLow_Type=Unsigned32
_NasArrayCapacityLow_Object=MibTableColumn
nasArrayCapacityLow=_NasArrayCapacityLow_Object((1,3,6,1,4,1,5227,27,1,3,1,6),_NasArrayCapacityLow_Type())
nasArrayCapacityLow.setMaxAccess(_B)
if mibBuilder.loadTexts:nasArrayCapacityLow.setStatus(_A)
_NasArrayCapacityHigh_Type=Unsigned32
_NasArrayCapacityHigh_Object=MibTableColumn
nasArrayCapacityHigh=_NasArrayCapacityHigh_Object((1,3,6,1,4,1,5227,27,1,3,1,7),_NasArrayCapacityHigh_Type())
nasArrayCapacityHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:nasArrayCapacityHigh.setStatus(_A)
_NasArrayUsedGiB_Type=Integer32
_NasArrayUsedGiB_Object=MibTableColumn
nasArrayUsedGiB=_NasArrayUsedGiB_Object((1,3,6,1,4,1,5227,27,1,3,1,8),_NasArrayUsedGiB_Type())
nasArrayUsedGiB.setMaxAccess(_B)
if mibBuilder.loadTexts:nasArrayUsedGiB.setStatus(_A)
_NasArrayUsedLow_Type=Unsigned32
_NasArrayUsedLow_Object=MibTableColumn
nasArrayUsedLow=_NasArrayUsedLow_Object((1,3,6,1,4,1,5227,27,1,3,1,9),_NasArrayUsedLow_Type())
nasArrayUsedLow.setMaxAccess(_B)
if mibBuilder.loadTexts:nasArrayUsedLow.setStatus(_A)
_NasArrayUsedHigh_Type=Unsigned32
_NasArrayUsedHigh_Object=MibTableColumn
nasArrayUsedHigh=_NasArrayUsedHigh_Object((1,3,6,1,4,1,5227,27,1,3,1,10),_NasArrayUsedHigh_Type())
nasArrayUsedHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:nasArrayUsedHigh.setStatus(_A)
_NasErrorTable_Object=MibTable
nasErrorTable=_NasErrorTable_Object((1,3,6,1,4,1,5227,27,1,4))
if mibBuilder.loadTexts:nasErrorTable.setStatus(_A)
_NasErrorEntry_Object=MibTableRow
nasErrorEntry=_NasErrorEntry_Object((1,3,6,1,4,1,5227,27,1,4,1))
nasErrorEntry.setIndexNames((0,_G,_R))
if mibBuilder.loadTexts:nasErrorEntry.setStatus(_A)
class _NasErrorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_NasErrorIndex_Type.__name__=_C
_NasErrorIndex_Object=MibTableColumn
nasErrorIndex=_NasErrorIndex_Object((1,3,6,1,4,1,5227,27,1,4,1,1),_NasErrorIndex_Type())
nasErrorIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:nasErrorIndex.setStatus(_A)
_NasErrorMsg_Type=DisplayString
_NasErrorMsg_Object=MibTableColumn
nasErrorMsg=_NasErrorMsg_Object((1,3,6,1,4,1,5227,27,1,4,1,2),_NasErrorMsg_Type())
nasErrorMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:nasErrorMsg.setStatus(_A)
_NasErrorDate_Type=DisplayString
_NasErrorDate_Object=MibTableColumn
nasErrorDate=_NasErrorDate_Object((1,3,6,1,4,1,5227,27,1,4,1,3),_NasErrorDate_Type())
nasErrorDate.setMaxAccess(_B)
if mibBuilder.loadTexts:nasErrorDate.setStatus(_A)
_NasErrorDateAndTime_Type=DateAndTime
_NasErrorDateAndTime_Object=MibTableColumn
nasErrorDateAndTime=_NasErrorDateAndTime_Object((1,3,6,1,4,1,5227,27,1,4,1,4),_NasErrorDateAndTime_Type())
nasErrorDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nasErrorDateAndTime.setStatus(_A)
_NasInformationTable_Object=MibTable
nasInformationTable=_NasInformationTable_Object((1,3,6,1,4,1,5227,27,1,5))
if mibBuilder.loadTexts:nasInformationTable.setStatus(_A)
_NasInformationEntry_Object=MibTableRow
nasInformationEntry=_NasInformationEntry_Object((1,3,6,1,4,1,5227,27,1,5,1))
nasInformationEntry.setIndexNames((0,_G,_S))
if mibBuilder.loadTexts:nasInformationEntry.setStatus(_A)
class _NasInformationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_NasInformationIndex_Type.__name__=_C
_NasInformationIndex_Object=MibTableColumn
nasInformationIndex=_NasInformationIndex_Object((1,3,6,1,4,1,5227,27,1,5,1,1),_NasInformationIndex_Type())
nasInformationIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:nasInformationIndex.setStatus(_A)
_NasInformationMsg_Type=DisplayString
_NasInformationMsg_Object=MibTableColumn
nasInformationMsg=_NasInformationMsg_Object((1,3,6,1,4,1,5227,27,1,5,1,2),_NasInformationMsg_Type())
nasInformationMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:nasInformationMsg.setStatus(_A)
_NasInformationDate_Type=DisplayString
_NasInformationDate_Object=MibTableColumn
nasInformationDate=_NasInformationDate_Object((1,3,6,1,4,1,5227,27,1,5,1,3),_NasInformationDate_Type())
nasInformationDate.setMaxAccess(_B)
if mibBuilder.loadTexts:nasInformationDate.setStatus(_A)
_NasInformationDateAndTime_Type=DateAndTime
_NasInformationDateAndTime_Object=MibTableColumn
nasInformationDateAndTime=_NasInformationDateAndTime_Object((1,3,6,1,4,1,5227,27,1,5,1,4),_NasInformationDateAndTime_Type())
nasInformationDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nasInformationDateAndTime.setStatus(_A)
_NasLVMParams_ObjectIdentity=ObjectIdentity
nasLVMParams=_NasLVMParams_ObjectIdentity((1,3,6,1,4,1,5227,27,1,6))
_NasVGTable_Object=MibTable
nasVGTable=_NasVGTable_Object((1,3,6,1,4,1,5227,27,1,6,1))
if mibBuilder.loadTexts:nasVGTable.setStatus(_A)
_NasVGEntry_Object=MibTableRow
nasVGEntry=_NasVGEntry_Object((1,3,6,1,4,1,5227,27,1,6,1,1))
nasVGEntry.setIndexNames((0,_G,_M))
if mibBuilder.loadTexts:nasVGEntry.setStatus(_A)
_NasVGIndex_Type=Integer32
_NasVGIndex_Object=MibTableColumn
nasVGIndex=_NasVGIndex_Object((1,3,6,1,4,1,5227,27,1,6,1,1,1),_NasVGIndex_Type())
nasVGIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:nasVGIndex.setStatus(_A)
_NasVGPESize_Type=Integer32
_NasVGPESize_Object=MibTableColumn
nasVGPESize=_NasVGPESize_Object((1,3,6,1,4,1,5227,27,1,6,1,1,2),_NasVGPESize_Type())
nasVGPESize.setMaxAccess(_B)
if mibBuilder.loadTexts:nasVGPESize.setStatus(_A)
if mibBuilder.loadTexts:nasVGPESize.setUnits('GB')
_NasVGPETotal_Type=Integer32
_NasVGPETotal_Object=MibTableColumn
nasVGPETotal=_NasVGPETotal_Object((1,3,6,1,4,1,5227,27,1,6,1,1,3),_NasVGPETotal_Type())
nasVGPETotal.setMaxAccess(_B)
if mibBuilder.loadTexts:nasVGPETotal.setStatus(_A)
_NasVGPEUsed_Type=Integer32
_NasVGPEUsed_Object=MibTableColumn
nasVGPEUsed=_NasVGPEUsed_Object((1,3,6,1,4,1,5227,27,1,6,1,1,4),_NasVGPEUsed_Type())
nasVGPEUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:nasVGPEUsed.setStatus(_A)
_NasLVTable_Object=MibTable
nasLVTable=_NasLVTable_Object((1,3,6,1,4,1,5227,27,1,6,1,1,5))
if mibBuilder.loadTexts:nasLVTable.setStatus(_A)
_NasLVEntry_Object=MibTableRow
nasLVEntry=_NasLVEntry_Object((1,3,6,1,4,1,5227,27,1,6,1,1,5,1))
nasLVEntry.setIndexNames((0,_G,_M),(0,_G,_T))
if mibBuilder.loadTexts:nasLVEntry.setStatus(_A)
class _NasLVIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_NasLVIndex_Type.__name__=_C
_NasLVIndex_Object=MibTableColumn
nasLVIndex=_NasLVIndex_Object((1,3,6,1,4,1,5227,27,1,6,1,1,5,1,1),_NasLVIndex_Type())
nasLVIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:nasLVIndex.setStatus(_A)
_NasLVName_Type=DisplayString
_NasLVName_Object=MibTableColumn
nasLVName=_NasLVName_Object((1,3,6,1,4,1,5227,27,1,6,1,1,5,1,2),_NasLVName_Type())
nasLVName.setMaxAccess(_B)
if mibBuilder.loadTexts:nasLVName.setStatus(_A)
_NasLVCapacity_Type=Integer32
_NasLVCapacity_Object=MibTableColumn
nasLVCapacity=_NasLVCapacity_Object((1,3,6,1,4,1,5227,27,1,6,1,1,5,1,3),_NasLVCapacity_Type())
nasLVCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:nasLVCapacity.setStatus(_A)
class _NasLVUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,100))
_NasLVUsed_Type.__name__=_C
_NasLVUsed_Object=MibTableColumn
nasLVUsed=_NasLVUsed_Object((1,3,6,1,4,1,5227,27,1,6,1,1,5,1,4),_NasLVUsed_Type())
nasLVUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:nasLVUsed.setStatus(_A)
if mibBuilder.loadTexts:nasLVUsed.setUnits('%')
_NasLVCapacityGiB_Type=Integer32
_NasLVCapacityGiB_Object=MibTableColumn
nasLVCapacityGiB=_NasLVCapacityGiB_Object((1,3,6,1,4,1,5227,27,1,6,1,1,5,1,5),_NasLVCapacityGiB_Type())
nasLVCapacityGiB.setMaxAccess(_B)
if mibBuilder.loadTexts:nasLVCapacityGiB.setStatus(_A)
_NasLVCapacityLow_Type=Unsigned32
_NasLVCapacityLow_Object=MibTableColumn
nasLVCapacityLow=_NasLVCapacityLow_Object((1,3,6,1,4,1,5227,27,1,6,1,1,5,1,6),_NasLVCapacityLow_Type())
nasLVCapacityLow.setMaxAccess(_B)
if mibBuilder.loadTexts:nasLVCapacityLow.setStatus(_A)
_NasLVCapacityHigh_Type=Unsigned32
_NasLVCapacityHigh_Object=MibTableColumn
nasLVCapacityHigh=_NasLVCapacityHigh_Object((1,3,6,1,4,1,5227,27,1,6,1,1,5,1,7),_NasLVCapacityHigh_Type())
nasLVCapacityHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:nasLVCapacityHigh.setStatus(_A)
_NasLVUsedGiB_Type=Integer32
_NasLVUsedGiB_Object=MibTableColumn
nasLVUsedGiB=_NasLVUsedGiB_Object((1,3,6,1,4,1,5227,27,1,6,1,1,5,1,8),_NasLVUsedGiB_Type())
nasLVUsedGiB.setMaxAccess(_B)
if mibBuilder.loadTexts:nasLVUsedGiB.setStatus(_A)
_NasLVUsedLow_Type=Unsigned32
_NasLVUsedLow_Object=MibTableColumn
nasLVUsedLow=_NasLVUsedLow_Object((1,3,6,1,4,1,5227,27,1,6,1,1,5,1,9),_NasLVUsedLow_Type())
nasLVUsedLow.setMaxAccess(_B)
if mibBuilder.loadTexts:nasLVUsedLow.setStatus(_A)
_NasLVUsedHigh_Type=Unsigned32
_NasLVUsedHigh_Object=MibTableColumn
nasLVUsedHigh=_NasLVUsedHigh_Object((1,3,6,1,4,1,5227,27,1,6,1,1,5,1,10),_NasLVUsedHigh_Type())
nasLVUsedHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:nasLVUsedHigh.setStatus(_A)
_NasPVTable_Object=MibTable
nasPVTable=_NasPVTable_Object((1,3,6,1,4,1,5227,27,1,6,1,1,6))
if mibBuilder.loadTexts:nasPVTable.setStatus(_A)
_NasPVEntry_Object=MibTableRow
nasPVEntry=_NasPVEntry_Object((1,3,6,1,4,1,5227,27,1,6,1,1,6,1))
nasPVEntry.setIndexNames((0,_G,_M),(0,_G,_U))
if mibBuilder.loadTexts:nasPVEntry.setStatus(_A)
_NasPVIndex_Type=Integer32
_NasPVIndex_Object=MibTableColumn
nasPVIndex=_NasPVIndex_Object((1,3,6,1,4,1,5227,27,1,6,1,1,6,1,1),_NasPVIndex_Type())
nasPVIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:nasPVIndex.setStatus(_A)
_NasPVName_Type=DisplayString
_NasPVName_Object=MibTableColumn
nasPVName=_NasPVName_Object((1,3,6,1,4,1,5227,27,1,6,1,1,6,1,2),_NasPVName_Type())
nasPVName.setMaxAccess(_B)
if mibBuilder.loadTexts:nasPVName.setStatus(_A)
_NasFailoverParams_ObjectIdentity=ObjectIdentity
nasFailoverParams=_NasFailoverParams_ObjectIdentity((1,3,6,1,4,1,5227,27,1,7))
class _NasFailoverRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32,64,128)));namedValues=NamedValues(*(('standalone',1),('main',2),('aloneMain',4),('backup',8),('aloneBackup',16),('maintenanceMain',32),('maintenanceBackup',64),('emMode',128)))
_NasFailoverRole_Type.__name__=_C
_NasFailoverRole_Object=MibScalar
nasFailoverRole=_NasFailoverRole_Object((1,3,6,1,4,1,5227,27,1,7,1),_NasFailoverRole_Type())
nasFailoverRole.setMaxAccess(_B)
if mibBuilder.loadTexts:nasFailoverRole.setStatus(_A)
class _NasFailoverStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,32)));namedValues=NamedValues(*(('idle',0),('busy',1),('startingMain',2),('startingBackup',3),('initializing',4),('stopping',32)))
_NasFailoverStatus_Type.__name__=_C
_NasFailoverStatus_Object=MibScalar
nasFailoverStatus=_NasFailoverStatus_Object((1,3,6,1,4,1,5227,27,1,7,2),_NasFailoverStatus_Type())
nasFailoverStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nasFailoverStatus.setStatus(_A)
_NasFailoverPartner_Type=IpAddress
_NasFailoverPartner_Object=MibScalar
nasFailoverPartner=_NasFailoverPartner_Object((1,3,6,1,4,1,5227,27,1,7,3),_NasFailoverPartner_Type())
nasFailoverPartner.setMaxAccess(_B)
if mibBuilder.loadTexts:nasFailoverPartner.setStatus(_A)
_NasRPSUTable_Object=MibTable
nasRPSUTable=_NasRPSUTable_Object((1,3,6,1,4,1,5227,27,1,8))
if mibBuilder.loadTexts:nasRPSUTable.setStatus(_A)
_NasRPSUEntry_Object=MibTableRow
nasRPSUEntry=_NasRPSUEntry_Object((1,3,6,1,4,1,5227,27,1,8,1))
nasRPSUEntry.setIndexNames((0,_G,_V))
if mibBuilder.loadTexts:nasRPSUEntry.setStatus(_A)
_NasRPSUIndex_Type=Integer32
_NasRPSUIndex_Object=MibTableColumn
nasRPSUIndex=_NasRPSUIndex_Object((1,3,6,1,4,1,5227,27,1,8,1,1),_NasRPSUIndex_Type())
nasRPSUIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:nasRPSUIndex.setStatus(_A)
class _NasRPSUStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),('fine',1),('broken',2)))
_NasRPSUStatus_Type.__name__=_C
_NasRPSUStatus_Object=MibTableColumn
nasRPSUStatus=_NasRPSUStatus_Object((1,3,6,1,4,1,5227,27,1,8,1,2),_NasRPSUStatus_Type())
nasRPSUStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nasRPSUStatus.setStatus(_A)
_NasISCSITable_Object=MibTable
nasISCSITable=_NasISCSITable_Object((1,3,6,1,4,1,5227,27,1,9))
if mibBuilder.loadTexts:nasISCSITable.setStatus(_A)
_NasISCSIEntry_Object=MibTableRow
nasISCSIEntry=_NasISCSIEntry_Object((1,3,6,1,4,1,5227,27,1,9,1))
nasISCSIEntry.setIndexNames((0,_G,_W))
if mibBuilder.loadTexts:nasISCSIEntry.setStatus(_A)
_NasISCSIIndex_Type=Integer32
_NasISCSIIndex_Object=MibTableColumn
nasISCSIIndex=_NasISCSIIndex_Object((1,3,6,1,4,1,5227,27,1,9,1,1),_NasISCSIIndex_Type())
nasISCSIIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:nasISCSIIndex.setStatus(_A)
_NasISCSIName_Type=DisplayString
_NasISCSIName_Object=MibTableColumn
nasISCSIName=_NasISCSIName_Object((1,3,6,1,4,1,5227,27,1,9,1,2),_NasISCSIName_Type())
nasISCSIName.setMaxAccess(_B)
if mibBuilder.loadTexts:nasISCSIName.setStatus(_A)
class _NasISCSIStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),('connected',1),('standing-by',2)))
_NasISCSIStatus_Type.__name__=_C
_NasISCSIStatus_Object=MibTableColumn
nasISCSIStatus=_NasISCSIStatus_Object((1,3,6,1,4,1,5227,27,1,9,1,3),_NasISCSIStatus_Type())
nasISCSIStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nasISCSIStatus.setStatus(_A)
_NasSystemInformation_ObjectIdentity=ObjectIdentity
nasSystemInformation=_NasSystemInformation_ObjectIdentity((1,3,6,1,4,1,5227,27,1,10))
class _NasProductName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NasProductName_Type.__name__=_I
_NasProductName_Object=MibScalar
nasProductName=_NasProductName_Object((1,3,6,1,4,1,5227,27,1,10,1),_NasProductName_Type())
nasProductName.setMaxAccess(_B)
if mibBuilder.loadTexts:nasProductName.setStatus(_A)
class _NasSerialNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NasSerialNumber_Type.__name__=_I
_NasSerialNumber_Object=MibScalar
nasSerialNumber=_NasSerialNumber_Object((1,3,6,1,4,1,5227,27,1,10,2),_NasSerialNumber_Type())
nasSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nasSerialNumber.setStatus(_A)
class _NasFWVersionMajor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NasFWVersionMajor_Type.__name__=_I
_NasFWVersionMajor_Object=MibScalar
nasFWVersionMajor=_NasFWVersionMajor_Object((1,3,6,1,4,1,5227,27,1,10,3),_NasFWVersionMajor_Type())
nasFWVersionMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:nasFWVersionMajor.setStatus(_A)
class _NasFWVersionMinor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NasFWVersionMinor_Type.__name__=_I
_NasFWVersionMinor_Object=MibScalar
nasFWVersionMinor=_NasFWVersionMinor_Object((1,3,6,1,4,1,5227,27,1,10,4),_NasFWVersionMinor_Type())
nasFWVersionMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:nasFWVersionMinor.setStatus(_A)
class _NasIsFWUpdateAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2,3)));namedValues=NamedValues(*((_D,-1),('available',1),(_K,2),('latest',3)))
_NasIsFWUpdateAvailable_Type.__name__=_C
_NasIsFWUpdateAvailable_Object=MibScalar
nasIsFWUpdateAvailable=_NasIsFWUpdateAvailable_Object((1,3,6,1,4,1,5227,27,1,10,5),_NasIsFWUpdateAvailable_Type())
nasIsFWUpdateAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:nasIsFWUpdateAvailable.setStatus(_A)
_NasSystemDateAndTime_Type=DateAndTime
_NasSystemDateAndTime_Object=MibScalar
nasSystemDateAndTime=_NasSystemDateAndTime_Object((1,3,6,1,4,1,5227,27,1,10,6),_NasSystemDateAndTime_Type())
nasSystemDateAndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nasSystemDateAndTime.setStatus(_A)
_NasServiceStatus_ObjectIdentity=ObjectIdentity
nasServiceStatus=_NasServiceStatus_ObjectIdentity((1,3,6,1,4,1,5227,27,1,11))
class _NasServiceStatusSMB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusSMB_Type.__name__=_C
_NasServiceStatusSMB_Object=MibScalar
nasServiceStatusSMB=_NasServiceStatusSMB_Object((1,3,6,1,4,1,5227,27,1,11,1),_NasServiceStatusSMB_Type())
nasServiceStatusSMB.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusSMB.setStatus(_A)
class _NasServiceStatusDFS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusDFS_Type.__name__=_C
_NasServiceStatusDFS_Object=MibScalar
nasServiceStatusDFS=_NasServiceStatusDFS_Object((1,3,6,1,4,1,5227,27,1,11,2),_NasServiceStatusDFS_Type())
nasServiceStatusDFS.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusDFS.setStatus(_A)
class _NasServiceStatusAFP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusAFP_Type.__name__=_C
_NasServiceStatusAFP_Object=MibScalar
nasServiceStatusAFP=_NasServiceStatusAFP_Object((1,3,6,1,4,1,5227,27,1,11,3),_NasServiceStatusAFP_Type())
nasServiceStatusAFP.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusAFP.setStatus(_A)
class _NasServiceStatusFTP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusFTP_Type.__name__=_C
_NasServiceStatusFTP_Object=MibScalar
nasServiceStatusFTP=_NasServiceStatusFTP_Object((1,3,6,1,4,1,5227,27,1,11,4),_NasServiceStatusFTP_Type())
nasServiceStatusFTP.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusFTP.setStatus(_A)
class _NasServiceStatusSFTP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusSFTP_Type.__name__=_C
_NasServiceStatusSFTP_Object=MibScalar
nasServiceStatusSFTP=_NasServiceStatusSFTP_Object((1,3,6,1,4,1,5227,27,1,11,5),_NasServiceStatusSFTP_Type())
nasServiceStatusSFTP.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusSFTP.setStatus(_A)
class _NasServiceStatusWebAxs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusWebAxs_Type.__name__=_C
_NasServiceStatusWebAxs_Object=MibScalar
nasServiceStatusWebAxs=_NasServiceStatusWebAxs_Object((1,3,6,1,4,1,5227,27,1,11,6),_NasServiceStatusWebAxs_Type())
nasServiceStatusWebAxs.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusWebAxs.setStatus(_A)
class _NasServiceStatusNFS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusNFS_Type.__name__=_C
_NasServiceStatusNFS_Object=MibScalar
nasServiceStatusNFS=_NasServiceStatusNFS_Object((1,3,6,1,4,1,5227,27,1,11,7),_NasServiceStatusNFS_Type())
nasServiceStatusNFS.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusNFS.setStatus(_A)
class _NasServiceStatusRAIDMaintenance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusRAIDMaintenance_Type.__name__=_C
_NasServiceStatusRAIDMaintenance_Object=MibScalar
nasServiceStatusRAIDMaintenance=_NasServiceStatusRAIDMaintenance_Object((1,3,6,1,4,1,5227,27,1,11,8),_NasServiceStatusRAIDMaintenance_Type())
nasServiceStatusRAIDMaintenance.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusRAIDMaintenance.setStatus(_A)
class _NasServiceStatusiSCSI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusiSCSI_Type.__name__=_C
_NasServiceStatusiSCSI_Object=MibScalar
nasServiceStatusiSCSI=_NasServiceStatusiSCSI_Object((1,3,6,1,4,1,5227,27,1,11,9),_NasServiceStatusiSCSI_Type())
nasServiceStatusiSCSI.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusiSCSI.setStatus(_A)
class _NasServiceStatusDLNAServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusDLNAServer_Type.__name__=_C
_NasServiceStatusDLNAServer_Object=MibScalar
nasServiceStatusDLNAServer=_NasServiceStatusDLNAServer_Object((1,3,6,1,4,1,5227,27,1,11,10),_NasServiceStatusDLNAServer_Type())
nasServiceStatusDLNAServer.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusDLNAServer.setStatus(_A)
class _NasServiceStatusiTunesServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusiTunesServer_Type.__name__=_C
_NasServiceStatusiTunesServer_Object=MibScalar
nasServiceStatusiTunesServer=_NasServiceStatusiTunesServer_Object((1,3,6,1,4,1,5227,27,1,11,11),_NasServiceStatusiTunesServer_Type())
nasServiceStatusiTunesServer.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusiTunesServer.setStatus(_A)
class _NasServiceStatusSqueezeboxServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusSqueezeboxServer_Type.__name__=_C
_NasServiceStatusSqueezeboxServer_Object=MibScalar
nasServiceStatusSqueezeboxServer=_NasServiceStatusSqueezeboxServer_Object((1,3,6,1,4,1,5227,27,1,11,12),_NasServiceStatusSqueezeboxServer_Type())
nasServiceStatusSqueezeboxServer.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusSqueezeboxServer.setStatus(_A)
class _NasServiceStatusPrintServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusPrintServer_Type.__name__=_C
_NasServiceStatusPrintServer_Object=MibScalar
nasServiceStatusPrintServer=_NasServiceStatusPrintServer_Object((1,3,6,1,4,1,5227,27,1,11,13),_NasServiceStatusPrintServer_Type())
nasServiceStatusPrintServer.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusPrintServer.setStatus(_A)
class _NasServiceStatusWebServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusWebServer_Type.__name__=_C
_NasServiceStatusWebServer_Object=MibScalar
nasServiceStatusWebServer=_NasServiceStatusWebServer_Object((1,3,6,1,4,1,5227,27,1,11,14),_NasServiceStatusWebServer_Type())
nasServiceStatusWebServer.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusWebServer.setStatus(_A)
class _NasServiceStatusMySQLServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusMySQLServer_Type.__name__=_C
_NasServiceStatusMySQLServer_Object=MibScalar
nasServiceStatusMySQLServer=_NasServiceStatusMySQLServer_Object((1,3,6,1,4,1,5227,27,1,11,15),_NasServiceStatusMySQLServer_Type())
nasServiceStatusMySQLServer.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusMySQLServer.setStatus(_A)
class _NasServiceStatusWebAxsSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusWebAxsSync_Type.__name__=_C
_NasServiceStatusWebAxsSync_Object=MibScalar
nasServiceStatusWebAxsSync=_NasServiceStatusWebAxsSync_Object((1,3,6,1,4,1,5227,27,1,11,16),_NasServiceStatusWebAxsSync_Type())
nasServiceStatusWebAxsSync.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusWebAxsSync.setStatus(_A)
class _NasServiceStatusCloudService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusCloudService_Type.__name__=_C
_NasServiceStatusCloudService_Object=MibScalar
nasServiceStatusCloudService=_NasServiceStatusCloudService_Object((1,3,6,1,4,1,5227,27,1,11,17),_NasServiceStatusCloudService_Type())
nasServiceStatusCloudService.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusCloudService.setStatus(_A)
class _NasServiceStatusBitTorrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusBitTorrent_Type.__name__=_C
_NasServiceStatusBitTorrent_Object=MibScalar
nasServiceStatusBitTorrent=_NasServiceStatusBitTorrent_Object((1,3,6,1,4,1,5227,27,1,11,18),_NasServiceStatusBitTorrent_Type())
nasServiceStatusBitTorrent.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusBitTorrent.setStatus(_A)
class _NasServiceStatusTeraSearch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusTeraSearch_Type.__name__=_C
_NasServiceStatusTeraSearch_Object=MibScalar
nasServiceStatusTeraSearch=_NasServiceStatusTeraSearch_Object((1,3,6,1,4,1,5227,27,1,11,19),_NasServiceStatusTeraSearch_Type())
nasServiceStatusTeraSearch.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusTeraSearch.setStatus(_A)
class _NasServiceStatusIpCamera_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusIpCamera_Type.__name__=_C
_NasServiceStatusIpCamera_Object=MibScalar
nasServiceStatusIpCamera=_NasServiceStatusIpCamera_Object((1,3,6,1,4,1,5227,27,1,11,20),_NasServiceStatusIpCamera_Type())
nasServiceStatusIpCamera.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusIpCamera.setStatus(_A)
class _NasServiceStatusVirusScan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusVirusScan_Type.__name__=_C
_NasServiceStatusVirusScan_Object=MibScalar
nasServiceStatusVirusScan=_NasServiceStatusVirusScan_Object((1,3,6,1,4,1,5227,27,1,11,21),_NasServiceStatusVirusScan_Type())
nasServiceStatusVirusScan.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusVirusScan.setStatus(_A)
class _NasServiceStatusSNMP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusSNMP_Type.__name__=_C
_NasServiceStatusSNMP_Object=MibScalar
nasServiceStatusSNMP=_NasServiceStatusSNMP_Object((1,3,6,1,4,1,5227,27,1,11,22),_NasServiceStatusSNMP_Type())
nasServiceStatusSNMP.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusSNMP.setStatus(_A)
class _NasServiceStatusTimeMachine_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusTimeMachine_Type.__name__=_C
_NasServiceStatusTimeMachine_Object=MibScalar
nasServiceStatusTimeMachine=_NasServiceStatusTimeMachine_Object((1,3,6,1,4,1,5227,27,1,11,23),_NasServiceStatusTimeMachine_Type())
nasServiceStatusTimeMachine.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusTimeMachine.setStatus(_A)
class _NasServiceStatusDirectCopy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusDirectCopy_Type.__name__=_C
_NasServiceStatusDirectCopy_Object=MibScalar
nasServiceStatusDirectCopy=_NasServiceStatusDirectCopy_Object((1,3,6,1,4,1,5227,27,1,11,24),_NasServiceStatusDirectCopy_Type())
nasServiceStatusDirectCopy.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusDirectCopy.setStatus(_A)
class _NasServiceStatusMailNotification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusMailNotification_Type.__name__=_C
_NasServiceStatusMailNotification_Object=MibScalar
nasServiceStatusMailNotification=_NasServiceStatusMailNotification_Object((1,3,6,1,4,1,5227,27,1,11,25),_NasServiceStatusMailNotification_Type())
nasServiceStatusMailNotification.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusMailNotification.setStatus(_A)
class _NasServiceStatusWorkingFolder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_D,-1),(_F,1),(_E,2)))
_NasServiceStatusWorkingFolder_Type.__name__=_C
_NasServiceStatusWorkingFolder_Object=MibScalar
nasServiceStatusWorkingFolder=_NasServiceStatusWorkingFolder_Object((1,3,6,1,4,1,5227,27,1,11,26),_NasServiceStatusWorkingFolder_Type())
nasServiceStatusWorkingFolder.setMaxAccess(_B)
if mibBuilder.loadTexts:nasServiceStatusWorkingFolder.setStatus(_A)
_TeraStationNotifications_ObjectIdentity=ObjectIdentity
teraStationNotifications=_TeraStationNotifications_ObjectIdentity((1,3,6,1,4,1,5227,27,2))
nasErrorOccur=NotificationType((1,3,6,1,4,1,5227,27,2,1))
nasErrorOccur.setObjects(*((_G,_X),(_G,_Y),(_G,_Z)))
if mibBuilder.loadTexts:nasErrorOccur.setStatus(_A)
nasInformationOccur=NotificationType((1,3,6,1,4,1,5227,27,2,2))
nasInformationOccur.setObjects(*((_G,_a),(_G,_b),(_G,_c)))
if mibBuilder.loadTexts:nasInformationOccur.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'DayOfWeek':DayOfWeek,'LongUTF8String':LongUTF8String,'teraStation':teraStation,'teraStationObjects':teraStationObjects,'nasBackupTable':nasBackupTable,'nasBackupEntry':nasBackupEntry,_N:nasBackupIndex,'nasBackupStatus':nasBackupStatus,'nasDiskTable':nasDiskTable,'nasDiskEntry':nasDiskEntry,_O:nasDiskIndex,'nasDiskStatus':nasDiskStatus,'nasDiskCapacity':nasDiskCapacity,'nasDiskUsed':nasDiskUsed,'nasDiskSMARTStatus':nasDiskSMARTStatus,'nasDiskSMARTReallocatedSectorCtValue':nasDiskSMARTReallocatedSectorCtValue,'nasDiskSMARTReallocatedSectorCtWorst':nasDiskSMARTReallocatedSectorCtWorst,'nasDiskSMARTReallocatedSectorCtThresh':nasDiskSMARTReallocatedSectorCtThresh,'nasDiskSMARTReallocatedSectorCtRAW':nasDiskSMARTReallocatedSectorCtRAW,'nasDiskSMARTCurrentPendingSectorValue':nasDiskSMARTCurrentPendingSectorValue,'nasDiskSMARTCurrentPendingSectorWorst':nasDiskSMARTCurrentPendingSectorWorst,'nasDiskSMARTCurrentPendingSectorThresh':nasDiskSMARTCurrentPendingSectorThresh,'nasDiskSMARTCurrentPendingSectorRAW':nasDiskSMARTCurrentPendingSectorRAW,'nasDiskSMARTOfflineUncorrectableValue':nasDiskSMARTOfflineUncorrectableValue,'nasDiskSMARTOfflineUncorrectableWorst':nasDiskSMARTOfflineUncorrectableWorst,'nasDiskSMARTOfflineUncorrectableThresh':nasDiskSMARTOfflineUncorrectableThresh,'nasDiskSMARTOfflineUncorrectableRAW':nasDiskSMARTOfflineUncorrectableRAW,'nasSSDSMARTRemainingLifeValue':nasSSDSMARTRemainingLifeValue,'nasSSDSMARTRemainingLifeWorst':nasSSDSMARTRemainingLifeWorst,'nasSSDSMARTRemainingLifeThresh':nasSSDSMARTRemainingLifeThresh,'nasSSDSMARTBadBlockCountValue':nasSSDSMARTBadBlockCountValue,'nasSSDSMARTBadBlockCountWorst':nasSSDSMARTBadBlockCountWorst,'nasSSDSMARTBadBlockCountThresh':nasSSDSMARTBadBlockCountThresh,'nasDiskCapacityGiB':nasDiskCapacityGiB,'nasDiskCapacityLow':nasDiskCapacityLow,'nasDiskCapacityHigh':nasDiskCapacityHigh,'nasDiskUsedGiB':nasDiskUsedGiB,'nasDiskUsedLow':nasDiskUsedLow,'nasDiskUsedHigh':nasDiskUsedHigh,'nasDiskModelName':nasDiskModelName,'nasDiskSMARTReallocatedSectorCtHealth':nasDiskSMARTReallocatedSectorCtHealth,'nasDiskSMARTCurrentPendingSectorHealth':nasDiskSMARTCurrentPendingSectorHealth,'nasDiskSMARTOfflineUncorrectableHealth':nasDiskSMARTOfflineUncorrectableHealth,'nasDiskSMARTRawReadErrorRateValue':nasDiskSMARTRawReadErrorRateValue,'nasDiskSMARTRawReadErrorRateWorst':nasDiskSMARTRawReadErrorRateWorst,'nasDiskSMARTRawReadErrorRateThresh':nasDiskSMARTRawReadErrorRateThresh,'nasDiskSMARTRawReadErrorRateRAW':nasDiskSMARTRawReadErrorRateRAW,'nasDiskSMARTRawReadErrorRateHealth':nasDiskSMARTRawReadErrorRateHealth,'nasDiskSMARTPowerOnHoursValue':nasDiskSMARTPowerOnHoursValue,'nasDiskSMARTPowerOnHoursWorst':nasDiskSMARTPowerOnHoursWorst,'nasDiskSMARTPowerOnHoursThresh':nasDiskSMARTPowerOnHoursThresh,'nasDiskSMARTPowerOnHoursRAW':nasDiskSMARTPowerOnHoursRAW,'nasDiskSMARTPowerOnHoursHealth':nasDiskSMARTPowerOnHoursHealth,'nasArrayTable':nasArrayTable,'nasArrayEntry':nasArrayEntry,_Q:nasArrayIndex,'nasArrayStatus':nasArrayStatus,'nasArrayCapacity':nasArrayCapacity,'nasArrayUsed':nasArrayUsed,'nasArrayCapacityGiB':nasArrayCapacityGiB,'nasArrayCapacityLow':nasArrayCapacityLow,'nasArrayCapacityHigh':nasArrayCapacityHigh,'nasArrayUsedGiB':nasArrayUsedGiB,'nasArrayUsedLow':nasArrayUsedLow,'nasArrayUsedHigh':nasArrayUsedHigh,'nasErrorTable':nasErrorTable,'nasErrorEntry':nasErrorEntry,_R:nasErrorIndex,_X:nasErrorMsg,_Y:nasErrorDate,_Z:nasErrorDateAndTime,'nasInformationTable':nasInformationTable,'nasInformationEntry':nasInformationEntry,_S:nasInformationIndex,_a:nasInformationMsg,_b:nasInformationDate,_c:nasInformationDateAndTime,'nasLVMParams':nasLVMParams,'nasVGTable':nasVGTable,'nasVGEntry':nasVGEntry,_M:nasVGIndex,'nasVGPESize':nasVGPESize,'nasVGPETotal':nasVGPETotal,'nasVGPEUsed':nasVGPEUsed,'nasLVTable':nasLVTable,'nasLVEntry':nasLVEntry,_T:nasLVIndex,'nasLVName':nasLVName,'nasLVCapacity':nasLVCapacity,'nasLVUsed':nasLVUsed,'nasLVCapacityGiB':nasLVCapacityGiB,'nasLVCapacityLow':nasLVCapacityLow,'nasLVCapacityHigh':nasLVCapacityHigh,'nasLVUsedGiB':nasLVUsedGiB,'nasLVUsedLow':nasLVUsedLow,'nasLVUsedHigh':nasLVUsedHigh,'nasPVTable':nasPVTable,'nasPVEntry':nasPVEntry,_U:nasPVIndex,'nasPVName':nasPVName,'nasFailoverParams':nasFailoverParams,'nasFailoverRole':nasFailoverRole,'nasFailoverStatus':nasFailoverStatus,'nasFailoverPartner':nasFailoverPartner,'nasRPSUTable':nasRPSUTable,'nasRPSUEntry':nasRPSUEntry,_V:nasRPSUIndex,'nasRPSUStatus':nasRPSUStatus,'nasISCSITable':nasISCSITable,'nasISCSIEntry':nasISCSIEntry,_W:nasISCSIIndex,'nasISCSIName':nasISCSIName,'nasISCSIStatus':nasISCSIStatus,'nasSystemInformation':nasSystemInformation,'nasProductName':nasProductName,'nasSerialNumber':nasSerialNumber,'nasFWVersionMajor':nasFWVersionMajor,'nasFWVersionMinor':nasFWVersionMinor,'nasIsFWUpdateAvailable':nasIsFWUpdateAvailable,'nasSystemDateAndTime':nasSystemDateAndTime,'nasServiceStatus':nasServiceStatus,'nasServiceStatusSMB':nasServiceStatusSMB,'nasServiceStatusDFS':nasServiceStatusDFS,'nasServiceStatusAFP':nasServiceStatusAFP,'nasServiceStatusFTP':nasServiceStatusFTP,'nasServiceStatusSFTP':nasServiceStatusSFTP,'nasServiceStatusWebAxs':nasServiceStatusWebAxs,'nasServiceStatusNFS':nasServiceStatusNFS,'nasServiceStatusRAIDMaintenance':nasServiceStatusRAIDMaintenance,'nasServiceStatusiSCSI':nasServiceStatusiSCSI,'nasServiceStatusDLNAServer':nasServiceStatusDLNAServer,'nasServiceStatusiTunesServer':nasServiceStatusiTunesServer,'nasServiceStatusSqueezeboxServer':nasServiceStatusSqueezeboxServer,'nasServiceStatusPrintServer':nasServiceStatusPrintServer,'nasServiceStatusWebServer':nasServiceStatusWebServer,'nasServiceStatusMySQLServer':nasServiceStatusMySQLServer,'nasServiceStatusWebAxsSync':nasServiceStatusWebAxsSync,'nasServiceStatusCloudService':nasServiceStatusCloudService,'nasServiceStatusBitTorrent':nasServiceStatusBitTorrent,'nasServiceStatusTeraSearch':nasServiceStatusTeraSearch,'nasServiceStatusIpCamera':nasServiceStatusIpCamera,'nasServiceStatusVirusScan':nasServiceStatusVirusScan,'nasServiceStatusSNMP':nasServiceStatusSNMP,'nasServiceStatusTimeMachine':nasServiceStatusTimeMachine,'nasServiceStatusDirectCopy':nasServiceStatusDirectCopy,'nasServiceStatusMailNotification':nasServiceStatusMailNotification,'nasServiceStatusWorkingFolder':nasServiceStatusWorkingFolder,'teraStationNotifications':teraStationNotifications,'nasErrorOccur':nasErrorOccur,'nasInformationOccur':nasInformationOccur})