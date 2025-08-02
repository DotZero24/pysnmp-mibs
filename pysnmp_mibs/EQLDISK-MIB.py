_O='eqlDiskSlot'
_N='eqlDiskStatus'
_M='eqlDiskSmartInfoEntry'
_L='eqlDiskErrorEntry'
_K='eqlDiskStatusEntry'
_J='eqlDiskIndex'
_I='eqlMemberIndex'
_H='EQLMEMBER-MIB'
_G='eqlGroupId'
_F='EQLGROUP-MIB'
_E='DisplayString'
_D='EQLDISK-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eqlGroupId,=mibBuilder.importSymbols(_F,_G)
eqlMemberIndex,=mibBuilder.importSymbols(_H,_I)
equalLogic,=mibBuilder.importSymbols('EQUALLOGIC-SMI','equalLogic')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
eqldiskModule=ModuleIdentity((1,3,6,1,4,1,12740,3))
if mibBuilder.loadTexts:eqldiskModule.setRevisions(('2002-09-06 00:00',))
_EqldiskObjects_ObjectIdentity=ObjectIdentity
eqldiskObjects=_EqldiskObjects_ObjectIdentity((1,3,6,1,4,1,12740,3,1))
_EqlDiskTable_Object=MibTable
eqlDiskTable=_EqlDiskTable_Object((1,3,6,1,4,1,12740,3,1,1))
if mibBuilder.loadTexts:eqlDiskTable.setStatus(_A)
_EqlDiskEntry_Object=MibTableRow
eqlDiskEntry=_EqlDiskEntry_Object((1,3,6,1,4,1,12740,3,1,1,1))
eqlDiskEntry.setIndexNames((0,_F,_G),(0,_H,_I),(0,_D,_J))
if mibBuilder.loadTexts:eqlDiskEntry.setStatus(_A)
_EqlDiskIndex_Type=Integer32
_EqlDiskIndex_Object=MibTableColumn
eqlDiskIndex=_EqlDiskIndex_Object((1,3,6,1,4,1,12740,3,1,1,1,1),_EqlDiskIndex_Type())
eqlDiskIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:eqlDiskIndex.setStatus(_A)
class _EqlDiskType_Type(DisplayString):defaultValue=OctetString('unknown disk type');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EqlDiskType_Type.__name__=_E
_EqlDiskType_Object=MibTableColumn
eqlDiskType=_EqlDiskType_Object((1,3,6,1,4,1,12740,3,1,1,1,2),_EqlDiskType_Type())
eqlDiskType.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskType.setStatus(_A)
class _EqlDiskModelNumber_Type(DisplayString):defaultValue=OctetString('unknown disk model');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_EqlDiskModelNumber_Type.__name__=_E
_EqlDiskModelNumber_Object=MibTableColumn
eqlDiskModelNumber=_EqlDiskModelNumber_Object((1,3,6,1,4,1,12740,3,1,1,1,3),_EqlDiskModelNumber_Type())
eqlDiskModelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskModelNumber.setStatus(_A)
class _EqlDiskRevisionNumber_Type(DisplayString):defaultValue=OctetString('?firmrev');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_EqlDiskRevisionNumber_Type.__name__=_E
_EqlDiskRevisionNumber_Object=MibTableColumn
eqlDiskRevisionNumber=_EqlDiskRevisionNumber_Object((1,3,6,1,4,1,12740,3,1,1,1,4),_EqlDiskRevisionNumber_Type())
eqlDiskRevisionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskRevisionNumber.setStatus(_A)
class _EqlDiskSerialNumber_Type(DisplayString):defaultValue=OctetString('unknown serial#');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_EqlDiskSerialNumber_Type.__name__=_E
_EqlDiskSerialNumber_Object=MibTableColumn
eqlDiskSerialNumber=_EqlDiskSerialNumber_Object((1,3,6,1,4,1,12740,3,1,1,1,5),_EqlDiskSerialNumber_Type())
eqlDiskSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSerialNumber.setStatus(_A)
_EqlDiskSize_Type=Integer32
_EqlDiskSize_Object=MibTableColumn
eqlDiskSize=_EqlDiskSize_Object((1,3,6,1,4,1,12740,3,1,1,1,6),_EqlDiskSize_Type())
eqlDiskSize.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSize.setStatus(_A)
class _EqlDiskAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('set-disk-on-line',1),('set-disk-off-line',2),('set-disk-spare',3)))
_EqlDiskAdminStatus_Type.__name__=_C
_EqlDiskAdminStatus_Object=MibTableColumn
eqlDiskAdminStatus=_EqlDiskAdminStatus_Object((1,3,6,1,4,1,12740,3,1,1,1,7),_EqlDiskAdminStatus_Type())
eqlDiskAdminStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:eqlDiskAdminStatus.setStatus(_A)
class _EqlDiskStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('on-line',1),('spare',2),('failed',3),('off-line',4),('alt-sig',5),('too-small',6),('history-of-failures',7),('unsupported-version',8),('unhealthy',9),('replacement',10),('encrypted',11),('notApproved',12),('preempt-failed',13)))
_EqlDiskStatus_Type.__name__=_C
_EqlDiskStatus_Object=MibTableColumn
eqlDiskStatus=_EqlDiskStatus_Object((1,3,6,1,4,1,12740,3,1,1,1,8),_EqlDiskStatus_Type())
eqlDiskStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskStatus.setStatus(_A)
_EqlDiskErrors_Type=Counter32
_EqlDiskErrors_Object=MibTableColumn
eqlDiskErrors=_EqlDiskErrors_Object((1,3,6,1,4,1,12740,3,1,1,1,9),_EqlDiskErrors_Type())
eqlDiskErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskErrors.setStatus(_A)
_EqlDiskId_Type=Integer32
_EqlDiskId_Object=MibTableColumn
eqlDiskId=_EqlDiskId_Object((1,3,6,1,4,1,12740,3,1,1,1,10),_EqlDiskId_Type())
eqlDiskId.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskId.setStatus(_A)
class _EqlDiskSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,13))
_EqlDiskSlot_Type.__name__=_C
_EqlDiskSlot_Object=MibTableColumn
eqlDiskSlot=_EqlDiskSlot_Object((1,3,6,1,4,1,12740,3,1,1,1,11),_EqlDiskSlot_Type())
eqlDiskSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSlot.setStatus(_A)
class _EqlDiskTypeEnum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',0),('sata',1),('sas',2),('sata-ssd',3),('sas-ssd',4),('sas-sed-hdd',5),('sas-sed-ssd',6)))
_EqlDiskTypeEnum_Type.__name__=_C
_EqlDiskTypeEnum_Object=MibTableColumn
eqlDiskTypeEnum=_EqlDiskTypeEnum_Object((1,3,6,1,4,1,12740,3,1,1,1,12),_EqlDiskTypeEnum_Type())
eqlDiskTypeEnum.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskTypeEnum.setStatus(_A)
_EqlDiskRPM_Type=Integer32
_EqlDiskRPM_Object=MibTableColumn
eqlDiskRPM=_EqlDiskRPM_Object((1,3,6,1,4,1,12740,3,1,1,1,13),_EqlDiskRPM_Type())
eqlDiskRPM.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskRPM.setStatus(_A)
class _EqlDiskSectorSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('sector-size-512-bytes',0),('sector-size-4096-bytes',1),('sector-size-unknown',2)))
_EqlDiskSectorSize_Type.__name__=_C
_EqlDiskSectorSize_Object=MibTableColumn
eqlDiskSectorSize=_EqlDiskSectorSize_Object((1,3,6,1,4,1,12740,3,1,1,1,14),_EqlDiskSectorSize_Type())
eqlDiskSectorSize.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSectorSize.setStatus(_A)
class _EqlDiskManufacturingInfo_Type(DisplayString):defaultValue=OctetString('mfginfo?');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_EqlDiskManufacturingInfo_Type.__name__=_E
_EqlDiskManufacturingInfo_Object=MibTableColumn
eqlDiskManufacturingInfo=_EqlDiskManufacturingInfo_Object((1,3,6,1,4,1,12740,3,1,1,1,15),_EqlDiskManufacturingInfo_Type())
eqlDiskManufacturingInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskManufacturingInfo.setStatus(_A)
class _EqlDiskPI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('pi-disabled',0),('pi-enabled',1)))
_EqlDiskPI_Type.__name__=_C
_EqlDiskPI_Object=MibTableColumn
eqlDiskPI=_EqlDiskPI_Object((1,3,6,1,4,1,12740,3,1,1,1,16),_EqlDiskPI_Type())
eqlDiskPI.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskPI.setStatus(_A)
class _EqlDiskHealth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('smart-status-not-available',0),('smart-ok',1),('smart-tripped',2)))
_EqlDiskHealth_Type.__name__=_C
_EqlDiskHealth_Object=MibTableColumn
eqlDiskHealth=_EqlDiskHealth_Object((1,3,6,1,4,1,12740,3,1,1,1,17),_EqlDiskHealth_Type())
eqlDiskHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskHealth.setStatus(_A)
_EqlDiskStatusTable_Object=MibTable
eqlDiskStatusTable=_EqlDiskStatusTable_Object((1,3,6,1,4,1,12740,3,1,2))
if mibBuilder.loadTexts:eqlDiskStatusTable.setStatus(_A)
_EqlDiskStatusEntry_Object=MibTableRow
eqlDiskStatusEntry=_EqlDiskStatusEntry_Object((1,3,6,1,4,1,12740,3,1,2,1))
if mibBuilder.loadTexts:eqlDiskStatusEntry.setStatus(_A)
_EqlDiskStatusXfers_Type=Counter64
_EqlDiskStatusXfers_Object=MibTableColumn
eqlDiskStatusXfers=_EqlDiskStatusXfers_Object((1,3,6,1,4,1,12740,3,1,2,1,1),_EqlDiskStatusXfers_Type())
eqlDiskStatusXfers.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskStatusXfers.setStatus(_A)
_EqlDiskStatusBytesRead_Type=Counter64
_EqlDiskStatusBytesRead_Object=MibTableColumn
eqlDiskStatusBytesRead=_EqlDiskStatusBytesRead_Object((1,3,6,1,4,1,12740,3,1,2,1,2),_EqlDiskStatusBytesRead_Type())
eqlDiskStatusBytesRead.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskStatusBytesRead.setStatus(_A)
_EqlDiskStatusBytesWritten_Type=Counter64
_EqlDiskStatusBytesWritten_Object=MibTableColumn
eqlDiskStatusBytesWritten=_EqlDiskStatusBytesWritten_Object((1,3,6,1,4,1,12740,3,1,2,1,3),_EqlDiskStatusBytesWritten_Type())
eqlDiskStatusBytesWritten.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskStatusBytesWritten.setStatus(_A)
_EqlDiskStatusBusyTime_Type=Counter64
_EqlDiskStatusBusyTime_Object=MibTableColumn
eqlDiskStatusBusyTime=_EqlDiskStatusBusyTime_Object((1,3,6,1,4,1,12740,3,1,2,1,4),_EqlDiskStatusBusyTime_Type())
eqlDiskStatusBusyTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskStatusBusyTime.setStatus(_A)
_EqlDiskStatusNumIOs_Type=Counter32
_EqlDiskStatusNumIOs_Object=MibTableColumn
eqlDiskStatusNumIOs=_EqlDiskStatusNumIOs_Object((1,3,6,1,4,1,12740,3,1,2,1,5),_EqlDiskStatusNumIOs_Type())
eqlDiskStatusNumIOs.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskStatusNumIOs.setStatus(_A)
_EqlDiskStatusFailXfers_Type=Counter32
_EqlDiskStatusFailXfers_Object=MibTableColumn
eqlDiskStatusFailXfers=_EqlDiskStatusFailXfers_Object((1,3,6,1,4,1,12740,3,1,2,1,6),_EqlDiskStatusFailXfers_Type())
eqlDiskStatusFailXfers.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskStatusFailXfers.setStatus(_A)
_EqlDiskStatusNumResets_Type=Counter32
_EqlDiskStatusNumResets_Object=MibTableColumn
eqlDiskStatusNumResets=_EqlDiskStatusNumResets_Object((1,3,6,1,4,1,12740,3,1,2,1,7),_EqlDiskStatusNumResets_Type())
eqlDiskStatusNumResets.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskStatusNumResets.setStatus(_A)
_EqlDiskStatusTotalQD_Type=Counter64
_EqlDiskStatusTotalQD_Object=MibTableColumn
eqlDiskStatusTotalQD=_EqlDiskStatusTotalQD_Object((1,3,6,1,4,1,12740,3,1,2,1,8),_EqlDiskStatusTotalQD_Type())
eqlDiskStatusTotalQD.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskStatusTotalQD.setStatus(_A)
_EqlDiskStatusLifetime_Type=Integer32
_EqlDiskStatusLifetime_Object=MibTableColumn
eqlDiskStatusLifetime=_EqlDiskStatusLifetime_Object((1,3,6,1,4,1,12740,3,1,2,1,9),_EqlDiskStatusLifetime_Type())
eqlDiskStatusLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskStatusLifetime.setStatus(_A)
_EqlDiskErrorTable_Object=MibTable
eqlDiskErrorTable=_EqlDiskErrorTable_Object((1,3,6,1,4,1,12740,3,1,3))
if mibBuilder.loadTexts:eqlDiskErrorTable.setStatus(_A)
_EqlDiskErrorEntry_Object=MibTableRow
eqlDiskErrorEntry=_EqlDiskErrorEntry_Object((1,3,6,1,4,1,12740,3,1,3,1))
if mibBuilder.loadTexts:eqlDiskErrorEntry.setStatus(_A)
_EqlDiskErrorPhyReady_Type=Counter32
_EqlDiskErrorPhyReady_Object=MibTableColumn
eqlDiskErrorPhyReady=_EqlDiskErrorPhyReady_Object((1,3,6,1,4,1,12740,3,1,3,1,1),_EqlDiskErrorPhyReady_Type())
eqlDiskErrorPhyReady.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskErrorPhyReady.setStatus(_A)
_EqlDiskErrorPhyInternal_Type=Counter32
_EqlDiskErrorPhyInternal_Object=MibTableColumn
eqlDiskErrorPhyInternal=_EqlDiskErrorPhyInternal_Object((1,3,6,1,4,1,12740,3,1,3,1,2),_EqlDiskErrorPhyInternal_Type())
eqlDiskErrorPhyInternal.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskErrorPhyInternal.setStatus(_A)
_EqlDiskErrorCommWake_Type=Counter32
_EqlDiskErrorCommWake_Object=MibTableColumn
eqlDiskErrorCommWake=_EqlDiskErrorCommWake_Object((1,3,6,1,4,1,12740,3,1,3,1,3),_EqlDiskErrorCommWake_Type())
eqlDiskErrorCommWake.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskErrorCommWake.setStatus(_A)
_EqlDiskErrorDecode10b8b_Type=Counter32
_EqlDiskErrorDecode10b8b_Object=MibTableColumn
eqlDiskErrorDecode10b8b=_EqlDiskErrorDecode10b8b_Object((1,3,6,1,4,1,12740,3,1,3,1,4),_EqlDiskErrorDecode10b8b_Type())
eqlDiskErrorDecode10b8b.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskErrorDecode10b8b.setStatus(_A)
_EqlDiskErrorDisparity_Type=Counter32
_EqlDiskErrorDisparity_Object=MibTableColumn
eqlDiskErrorDisparity=_EqlDiskErrorDisparity_Object((1,3,6,1,4,1,12740,3,1,3,1,5),_EqlDiskErrorDisparity_Type())
eqlDiskErrorDisparity.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskErrorDisparity.setStatus(_A)
_EqlDiskErrorCRC_Type=Counter32
_EqlDiskErrorCRC_Object=MibTableColumn
eqlDiskErrorCRC=_EqlDiskErrorCRC_Object((1,3,6,1,4,1,12740,3,1,3,1,6),_EqlDiskErrorCRC_Type())
eqlDiskErrorCRC.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskErrorCRC.setStatus(_A)
_EqlDiskErrorHandShake_Type=Counter32
_EqlDiskErrorHandShake_Object=MibTableColumn
eqlDiskErrorHandShake=_EqlDiskErrorHandShake_Object((1,3,6,1,4,1,12740,3,1,3,1,7),_EqlDiskErrorHandShake_Type())
eqlDiskErrorHandShake.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskErrorHandShake.setStatus(_A)
_EqlDiskErrorLinkSeq_Type=Counter32
_EqlDiskErrorLinkSeq_Object=MibTableColumn
eqlDiskErrorLinkSeq=_EqlDiskErrorLinkSeq_Object((1,3,6,1,4,1,12740,3,1,3,1,8),_EqlDiskErrorLinkSeq_Type())
eqlDiskErrorLinkSeq.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskErrorLinkSeq.setStatus(_A)
_EqlDiskErrorTransportState_Type=Counter32
_EqlDiskErrorTransportState_Object=MibTableColumn
eqlDiskErrorTransportState=_EqlDiskErrorTransportState_Object((1,3,6,1,4,1,12740,3,1,3,1,9),_EqlDiskErrorTransportState_Type())
eqlDiskErrorTransportState.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskErrorTransportState.setStatus(_A)
_EqlDiskErrorUnrecFIS_Type=Counter32
_EqlDiskErrorUnrecFIS_Object=MibTableColumn
eqlDiskErrorUnrecFIS=_EqlDiskErrorUnrecFIS_Object((1,3,6,1,4,1,12740,3,1,3,1,10),_EqlDiskErrorUnrecFIS_Type())
eqlDiskErrorUnrecFIS.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskErrorUnrecFIS.setStatus(_A)
_EqlDiskSmartInfoTable_Object=MibTable
eqlDiskSmartInfoTable=_EqlDiskSmartInfoTable_Object((1,3,6,1,4,1,12740,3,1,4))
if mibBuilder.loadTexts:eqlDiskSmartInfoTable.setStatus(_A)
_EqlDiskSmartInfoEntry_Object=MibTableRow
eqlDiskSmartInfoEntry=_EqlDiskSmartInfoEntry_Object((1,3,6,1,4,1,12740,3,1,4,1))
if mibBuilder.loadTexts:eqlDiskSmartInfoEntry.setStatus(_A)
_EqlDiskSmartInfoRawReadErrorRate_Type=Integer32
_EqlDiskSmartInfoRawReadErrorRate_Object=MibTableColumn
eqlDiskSmartInfoRawReadErrorRate=_EqlDiskSmartInfoRawReadErrorRate_Object((1,3,6,1,4,1,12740,3,1,4,1,1),_EqlDiskSmartInfoRawReadErrorRate_Type())
eqlDiskSmartInfoRawReadErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoRawReadErrorRate.setStatus(_A)
_EqlDiskSmartInfoRawReadErrorRateWorst_Type=Integer32
_EqlDiskSmartInfoRawReadErrorRateWorst_Object=MibTableColumn
eqlDiskSmartInfoRawReadErrorRateWorst=_EqlDiskSmartInfoRawReadErrorRateWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,2),_EqlDiskSmartInfoRawReadErrorRateWorst_Type())
eqlDiskSmartInfoRawReadErrorRateWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoRawReadErrorRateWorst.setStatus(_A)
_EqlDiskSmartInfoThroughputPerformance_Type=Integer32
_EqlDiskSmartInfoThroughputPerformance_Object=MibTableColumn
eqlDiskSmartInfoThroughputPerformance=_EqlDiskSmartInfoThroughputPerformance_Object((1,3,6,1,4,1,12740,3,1,4,1,3),_EqlDiskSmartInfoThroughputPerformance_Type())
eqlDiskSmartInfoThroughputPerformance.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoThroughputPerformance.setStatus(_A)
_EqlDiskSmartInfoThroughputPerformanceWorst_Type=Integer32
_EqlDiskSmartInfoThroughputPerformanceWorst_Object=MibTableColumn
eqlDiskSmartInfoThroughputPerformanceWorst=_EqlDiskSmartInfoThroughputPerformanceWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,4),_EqlDiskSmartInfoThroughputPerformanceWorst_Type())
eqlDiskSmartInfoThroughputPerformanceWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoThroughputPerformanceWorst.setStatus(_A)
_EqlDiskSmartInfoSpinUpTime_Type=Integer32
_EqlDiskSmartInfoSpinUpTime_Object=MibTableColumn
eqlDiskSmartInfoSpinUpTime=_EqlDiskSmartInfoSpinUpTime_Object((1,3,6,1,4,1,12740,3,1,4,1,5),_EqlDiskSmartInfoSpinUpTime_Type())
eqlDiskSmartInfoSpinUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoSpinUpTime.setStatus(_A)
_EqlDiskSmartInfoSpinUpTimeWorst_Type=Integer32
_EqlDiskSmartInfoSpinUpTimeWorst_Object=MibTableColumn
eqlDiskSmartInfoSpinUpTimeWorst=_EqlDiskSmartInfoSpinUpTimeWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,6),_EqlDiskSmartInfoSpinUpTimeWorst_Type())
eqlDiskSmartInfoSpinUpTimeWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoSpinUpTimeWorst.setStatus(_A)
_EqlDiskSmartInfoStartStopCount_Type=Integer32
_EqlDiskSmartInfoStartStopCount_Object=MibTableColumn
eqlDiskSmartInfoStartStopCount=_EqlDiskSmartInfoStartStopCount_Object((1,3,6,1,4,1,12740,3,1,4,1,7),_EqlDiskSmartInfoStartStopCount_Type())
eqlDiskSmartInfoStartStopCount.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoStartStopCount.setStatus(_A)
_EqlDiskSmartInfoStartStopCountWorst_Type=Integer32
_EqlDiskSmartInfoStartStopCountWorst_Object=MibTableColumn
eqlDiskSmartInfoStartStopCountWorst=_EqlDiskSmartInfoStartStopCountWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,8),_EqlDiskSmartInfoStartStopCountWorst_Type())
eqlDiskSmartInfoStartStopCountWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoStartStopCountWorst.setStatus(_A)
_EqlDiskSmartInfoReallocatedSectorCount_Type=Integer32
_EqlDiskSmartInfoReallocatedSectorCount_Object=MibTableColumn
eqlDiskSmartInfoReallocatedSectorCount=_EqlDiskSmartInfoReallocatedSectorCount_Object((1,3,6,1,4,1,12740,3,1,4,1,9),_EqlDiskSmartInfoReallocatedSectorCount_Type())
eqlDiskSmartInfoReallocatedSectorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoReallocatedSectorCount.setStatus(_A)
_EqlDiskSmartInfoReallocatedSectorCountWorst_Type=Integer32
_EqlDiskSmartInfoReallocatedSectorCountWorst_Object=MibTableColumn
eqlDiskSmartInfoReallocatedSectorCountWorst=_EqlDiskSmartInfoReallocatedSectorCountWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,10),_EqlDiskSmartInfoReallocatedSectorCountWorst_Type())
eqlDiskSmartInfoReallocatedSectorCountWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoReallocatedSectorCountWorst.setStatus(_A)
_EqlDiskSmartInfoReadChannelMargin_Type=Integer32
_EqlDiskSmartInfoReadChannelMargin_Object=MibTableColumn
eqlDiskSmartInfoReadChannelMargin=_EqlDiskSmartInfoReadChannelMargin_Object((1,3,6,1,4,1,12740,3,1,4,1,11),_EqlDiskSmartInfoReadChannelMargin_Type())
eqlDiskSmartInfoReadChannelMargin.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoReadChannelMargin.setStatus(_A)
_EqlDiskSmartInfoReadChannelMarginWorst_Type=Integer32
_EqlDiskSmartInfoReadChannelMarginWorst_Object=MibTableColumn
eqlDiskSmartInfoReadChannelMarginWorst=_EqlDiskSmartInfoReadChannelMarginWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,12),_EqlDiskSmartInfoReadChannelMarginWorst_Type())
eqlDiskSmartInfoReadChannelMarginWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoReadChannelMarginWorst.setStatus(_A)
_EqlDiskSmartInfoSeekErrorRate_Type=Integer32
_EqlDiskSmartInfoSeekErrorRate_Object=MibTableColumn
eqlDiskSmartInfoSeekErrorRate=_EqlDiskSmartInfoSeekErrorRate_Object((1,3,6,1,4,1,12740,3,1,4,1,13),_EqlDiskSmartInfoSeekErrorRate_Type())
eqlDiskSmartInfoSeekErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoSeekErrorRate.setStatus(_A)
_EqlDiskSmartInfoSeekErrorRateWorst_Type=Integer32
_EqlDiskSmartInfoSeekErrorRateWorst_Object=MibTableColumn
eqlDiskSmartInfoSeekErrorRateWorst=_EqlDiskSmartInfoSeekErrorRateWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,14),_EqlDiskSmartInfoSeekErrorRateWorst_Type())
eqlDiskSmartInfoSeekErrorRateWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoSeekErrorRateWorst.setStatus(_A)
_EqlDiskSmartInfoSeekPerformance_Type=Integer32
_EqlDiskSmartInfoSeekPerformance_Object=MibTableColumn
eqlDiskSmartInfoSeekPerformance=_EqlDiskSmartInfoSeekPerformance_Object((1,3,6,1,4,1,12740,3,1,4,1,15),_EqlDiskSmartInfoSeekPerformance_Type())
eqlDiskSmartInfoSeekPerformance.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoSeekPerformance.setStatus(_A)
_EqlDiskSmartInfoSeekPerformanceWorst_Type=Integer32
_EqlDiskSmartInfoSeekPerformanceWorst_Object=MibTableColumn
eqlDiskSmartInfoSeekPerformanceWorst=_EqlDiskSmartInfoSeekPerformanceWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,16),_EqlDiskSmartInfoSeekPerformanceWorst_Type())
eqlDiskSmartInfoSeekPerformanceWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoSeekPerformanceWorst.setStatus(_A)
_EqlDiskSmartInfoPowerOnHours_Type=Integer32
_EqlDiskSmartInfoPowerOnHours_Object=MibTableColumn
eqlDiskSmartInfoPowerOnHours=_EqlDiskSmartInfoPowerOnHours_Object((1,3,6,1,4,1,12740,3,1,4,1,17),_EqlDiskSmartInfoPowerOnHours_Type())
eqlDiskSmartInfoPowerOnHours.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoPowerOnHours.setStatus(_A)
_EqlDiskSmartInfoPowerOnHoursWorst_Type=Integer32
_EqlDiskSmartInfoPowerOnHoursWorst_Object=MibTableColumn
eqlDiskSmartInfoPowerOnHoursWorst=_EqlDiskSmartInfoPowerOnHoursWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,18),_EqlDiskSmartInfoPowerOnHoursWorst_Type())
eqlDiskSmartInfoPowerOnHoursWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoPowerOnHoursWorst.setStatus(_A)
_EqlDiskSmartInfoSpinupRetries_Type=Integer32
_EqlDiskSmartInfoSpinupRetries_Object=MibTableColumn
eqlDiskSmartInfoSpinupRetries=_EqlDiskSmartInfoSpinupRetries_Object((1,3,6,1,4,1,12740,3,1,4,1,19),_EqlDiskSmartInfoSpinupRetries_Type())
eqlDiskSmartInfoSpinupRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoSpinupRetries.setStatus(_A)
_EqlDiskSmartInfoSpinupRetriesWorst_Type=Integer32
_EqlDiskSmartInfoSpinupRetriesWorst_Object=MibTableColumn
eqlDiskSmartInfoSpinupRetriesWorst=_EqlDiskSmartInfoSpinupRetriesWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,20),_EqlDiskSmartInfoSpinupRetriesWorst_Type())
eqlDiskSmartInfoSpinupRetriesWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoSpinupRetriesWorst.setStatus(_A)
_EqlDiskSmartInfoDriveRecalibRetryCount_Type=Integer32
_EqlDiskSmartInfoDriveRecalibRetryCount_Object=MibTableColumn
eqlDiskSmartInfoDriveRecalibRetryCount=_EqlDiskSmartInfoDriveRecalibRetryCount_Object((1,3,6,1,4,1,12740,3,1,4,1,21),_EqlDiskSmartInfoDriveRecalibRetryCount_Type())
eqlDiskSmartInfoDriveRecalibRetryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoDriveRecalibRetryCount.setStatus(_A)
_EqlDiskSmartInfoDriveRecalibRetryCountWorst_Type=Integer32
_EqlDiskSmartInfoDriveRecalibRetryCountWorst_Object=MibTableColumn
eqlDiskSmartInfoDriveRecalibRetryCountWorst=_EqlDiskSmartInfoDriveRecalibRetryCountWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,22),_EqlDiskSmartInfoDriveRecalibRetryCountWorst_Type())
eqlDiskSmartInfoDriveRecalibRetryCountWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoDriveRecalibRetryCountWorst.setStatus(_A)
_EqlDiskSmartInfoPowerCycleCount_Type=Integer32
_EqlDiskSmartInfoPowerCycleCount_Object=MibTableColumn
eqlDiskSmartInfoPowerCycleCount=_EqlDiskSmartInfoPowerCycleCount_Object((1,3,6,1,4,1,12740,3,1,4,1,23),_EqlDiskSmartInfoPowerCycleCount_Type())
eqlDiskSmartInfoPowerCycleCount.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoPowerCycleCount.setStatus(_A)
_EqlDiskSmartInfoPowerCycleCountWorst_Type=Integer32
_EqlDiskSmartInfoPowerCycleCountWorst_Object=MibTableColumn
eqlDiskSmartInfoPowerCycleCountWorst=_EqlDiskSmartInfoPowerCycleCountWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,24),_EqlDiskSmartInfoPowerCycleCountWorst_Type())
eqlDiskSmartInfoPowerCycleCountWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoPowerCycleCountWorst.setStatus(_A)
_EqlDiskSmartInfoReadSoftErrorRate_Type=Integer32
_EqlDiskSmartInfoReadSoftErrorRate_Object=MibTableColumn
eqlDiskSmartInfoReadSoftErrorRate=_EqlDiskSmartInfoReadSoftErrorRate_Object((1,3,6,1,4,1,12740,3,1,4,1,25),_EqlDiskSmartInfoReadSoftErrorRate_Type())
eqlDiskSmartInfoReadSoftErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoReadSoftErrorRate.setStatus(_A)
_EqlDiskSmartInfoReadSoftErrorRateWorst_Type=Integer32
_EqlDiskSmartInfoReadSoftErrorRateWorst_Object=MibTableColumn
eqlDiskSmartInfoReadSoftErrorRateWorst=_EqlDiskSmartInfoReadSoftErrorRateWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,26),_EqlDiskSmartInfoReadSoftErrorRateWorst_Type())
eqlDiskSmartInfoReadSoftErrorRateWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoReadSoftErrorRateWorst.setStatus(_A)
_EqlDiskSmartInfoEmergencyRetractCycles_Type=Integer32
_EqlDiskSmartInfoEmergencyRetractCycles_Object=MibTableColumn
eqlDiskSmartInfoEmergencyRetractCycles=_EqlDiskSmartInfoEmergencyRetractCycles_Object((1,3,6,1,4,1,12740,3,1,4,1,27),_EqlDiskSmartInfoEmergencyRetractCycles_Type())
eqlDiskSmartInfoEmergencyRetractCycles.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoEmergencyRetractCycles.setStatus(_A)
_EqlDiskSmartInfoEmergencyRetractCyclesWorst_Type=Integer32
_EqlDiskSmartInfoEmergencyRetractCyclesWorst_Object=MibTableColumn
eqlDiskSmartInfoEmergencyRetractCyclesWorst=_EqlDiskSmartInfoEmergencyRetractCyclesWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,28),_EqlDiskSmartInfoEmergencyRetractCyclesWorst_Type())
eqlDiskSmartInfoEmergencyRetractCyclesWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoEmergencyRetractCyclesWorst.setStatus(_A)
_EqlDiskSmartInfoLoadUnloadCycles_Type=Integer32
_EqlDiskSmartInfoLoadUnloadCycles_Object=MibTableColumn
eqlDiskSmartInfoLoadUnloadCycles=_EqlDiskSmartInfoLoadUnloadCycles_Object((1,3,6,1,4,1,12740,3,1,4,1,29),_EqlDiskSmartInfoLoadUnloadCycles_Type())
eqlDiskSmartInfoLoadUnloadCycles.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoLoadUnloadCycles.setStatus(_A)
_EqlDiskSmartInfoLoadUnloadCyclesWorst_Type=Integer32
_EqlDiskSmartInfoLoadUnloadCyclesWorst_Object=MibTableColumn
eqlDiskSmartInfoLoadUnloadCyclesWorst=_EqlDiskSmartInfoLoadUnloadCyclesWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,30),_EqlDiskSmartInfoLoadUnloadCyclesWorst_Type())
eqlDiskSmartInfoLoadUnloadCyclesWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoLoadUnloadCyclesWorst.setStatus(_A)
_EqlDiskSmartInfoHDDTemp_Type=Integer32
_EqlDiskSmartInfoHDDTemp_Object=MibTableColumn
eqlDiskSmartInfoHDDTemp=_EqlDiskSmartInfoHDDTemp_Object((1,3,6,1,4,1,12740,3,1,4,1,31),_EqlDiskSmartInfoHDDTemp_Type())
eqlDiskSmartInfoHDDTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoHDDTemp.setStatus(_A)
_EqlDiskSmartInfoHDDTempWorst_Type=Integer32
_EqlDiskSmartInfoHDDTempWorst_Object=MibTableColumn
eqlDiskSmartInfoHDDTempWorst=_EqlDiskSmartInfoHDDTempWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,32),_EqlDiskSmartInfoHDDTempWorst_Type())
eqlDiskSmartInfoHDDTempWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoHDDTempWorst.setStatus(_A)
_EqlDiskSmartInfoOnTheFlyErrorRate_Type=Integer32
_EqlDiskSmartInfoOnTheFlyErrorRate_Object=MibTableColumn
eqlDiskSmartInfoOnTheFlyErrorRate=_EqlDiskSmartInfoOnTheFlyErrorRate_Object((1,3,6,1,4,1,12740,3,1,4,1,33),_EqlDiskSmartInfoOnTheFlyErrorRate_Type())
eqlDiskSmartInfoOnTheFlyErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoOnTheFlyErrorRate.setStatus(_A)
_EqlDiskSmartInfoOnTheFlyErrorRateWorst_Type=Integer32
_EqlDiskSmartInfoOnTheFlyErrorRateWorst_Object=MibTableColumn
eqlDiskSmartInfoOnTheFlyErrorRateWorst=_EqlDiskSmartInfoOnTheFlyErrorRateWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,34),_EqlDiskSmartInfoOnTheFlyErrorRateWorst_Type())
eqlDiskSmartInfoOnTheFlyErrorRateWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoOnTheFlyErrorRateWorst.setStatus(_A)
_EqlDiskSmartInfoSelfTestReallocSectors_Type=Integer32
_EqlDiskSmartInfoSelfTestReallocSectors_Object=MibTableColumn
eqlDiskSmartInfoSelfTestReallocSectors=_EqlDiskSmartInfoSelfTestReallocSectors_Object((1,3,6,1,4,1,12740,3,1,4,1,35),_EqlDiskSmartInfoSelfTestReallocSectors_Type())
eqlDiskSmartInfoSelfTestReallocSectors.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoSelfTestReallocSectors.setStatus(_A)
_EqlDiskSmartInfoSelfTestReallocSectorsWorst_Type=Integer32
_EqlDiskSmartInfoSelfTestReallocSectorsWorst_Object=MibTableColumn
eqlDiskSmartInfoSelfTestReallocSectorsWorst=_EqlDiskSmartInfoSelfTestReallocSectorsWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,36),_EqlDiskSmartInfoSelfTestReallocSectorsWorst_Type())
eqlDiskSmartInfoSelfTestReallocSectorsWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoSelfTestReallocSectorsWorst.setStatus(_A)
_EqlDiskSmartInfoPendingDefects_Type=Integer32
_EqlDiskSmartInfoPendingDefects_Object=MibTableColumn
eqlDiskSmartInfoPendingDefects=_EqlDiskSmartInfoPendingDefects_Object((1,3,6,1,4,1,12740,3,1,4,1,37),_EqlDiskSmartInfoPendingDefects_Type())
eqlDiskSmartInfoPendingDefects.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoPendingDefects.setStatus(_A)
_EqlDiskSmartInfoPendingDefectsWorst_Type=Integer32
_EqlDiskSmartInfoPendingDefectsWorst_Object=MibTableColumn
eqlDiskSmartInfoPendingDefectsWorst=_EqlDiskSmartInfoPendingDefectsWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,38),_EqlDiskSmartInfoPendingDefectsWorst_Type())
eqlDiskSmartInfoPendingDefectsWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoPendingDefectsWorst.setStatus(_A)
_EqlDiskSmartInfoOfflineSurfaceScan_Type=Integer32
_EqlDiskSmartInfoOfflineSurfaceScan_Object=MibTableColumn
eqlDiskSmartInfoOfflineSurfaceScan=_EqlDiskSmartInfoOfflineSurfaceScan_Object((1,3,6,1,4,1,12740,3,1,4,1,39),_EqlDiskSmartInfoOfflineSurfaceScan_Type())
eqlDiskSmartInfoOfflineSurfaceScan.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoOfflineSurfaceScan.setStatus(_A)
_EqlDiskSmartInfoOfflineSurfaceScanWorst_Type=Integer32
_EqlDiskSmartInfoOfflineSurfaceScanWorst_Object=MibTableColumn
eqlDiskSmartInfoOfflineSurfaceScanWorst=_EqlDiskSmartInfoOfflineSurfaceScanWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,40),_EqlDiskSmartInfoOfflineSurfaceScanWorst_Type())
eqlDiskSmartInfoOfflineSurfaceScanWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoOfflineSurfaceScanWorst.setStatus(_A)
_EqlDiskSmartInfoUltraDMACRCErrorRate_Type=Integer32
_EqlDiskSmartInfoUltraDMACRCErrorRate_Object=MibTableColumn
eqlDiskSmartInfoUltraDMACRCErrorRate=_EqlDiskSmartInfoUltraDMACRCErrorRate_Object((1,3,6,1,4,1,12740,3,1,4,1,41),_EqlDiskSmartInfoUltraDMACRCErrorRate_Type())
eqlDiskSmartInfoUltraDMACRCErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoUltraDMACRCErrorRate.setStatus(_A)
_EqlDiskSmartInfoUltraDMACRCErrorRateWorst_Type=Integer32
_EqlDiskSmartInfoUltraDMACRCErrorRateWorst_Object=MibTableColumn
eqlDiskSmartInfoUltraDMACRCErrorRateWorst=_EqlDiskSmartInfoUltraDMACRCErrorRateWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,42),_EqlDiskSmartInfoUltraDMACRCErrorRateWorst_Type())
eqlDiskSmartInfoUltraDMACRCErrorRateWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoUltraDMACRCErrorRateWorst.setStatus(_A)
_EqlDiskSmartInfoWritePreampErrors_Type=Integer32
_EqlDiskSmartInfoWritePreampErrors_Object=MibTableColumn
eqlDiskSmartInfoWritePreampErrors=_EqlDiskSmartInfoWritePreampErrors_Object((1,3,6,1,4,1,12740,3,1,4,1,43),_EqlDiskSmartInfoWritePreampErrors_Type())
eqlDiskSmartInfoWritePreampErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoWritePreampErrors.setStatus(_A)
_EqlDiskSmartInfoWritePreampErrorsWorst_Type=Integer32
_EqlDiskSmartInfoWritePreampErrorsWorst_Object=MibTableColumn
eqlDiskSmartInfoWritePreampErrorsWorst=_EqlDiskSmartInfoWritePreampErrorsWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,44),_EqlDiskSmartInfoWritePreampErrorsWorst_Type())
eqlDiskSmartInfoWritePreampErrorsWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoWritePreampErrorsWorst.setStatus(_A)
_EqlDiskSmartInfoOffTrackErrors_Type=Integer32
_EqlDiskSmartInfoOffTrackErrors_Object=MibTableColumn
eqlDiskSmartInfoOffTrackErrors=_EqlDiskSmartInfoOffTrackErrors_Object((1,3,6,1,4,1,12740,3,1,4,1,45),_EqlDiskSmartInfoOffTrackErrors_Type())
eqlDiskSmartInfoOffTrackErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoOffTrackErrors.setStatus(_A)
_EqlDiskSmartInfoOffTrackErrorsWorst_Type=Integer32
_EqlDiskSmartInfoOffTrackErrorsWorst_Object=MibTableColumn
eqlDiskSmartInfoOffTrackErrorsWorst=_EqlDiskSmartInfoOffTrackErrorsWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,46),_EqlDiskSmartInfoOffTrackErrorsWorst_Type())
eqlDiskSmartInfoOffTrackErrorsWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoOffTrackErrorsWorst.setStatus(_A)
_EqlDiskSmartInfoDAMErrorRate_Type=Integer32
_EqlDiskSmartInfoDAMErrorRate_Object=MibTableColumn
eqlDiskSmartInfoDAMErrorRate=_EqlDiskSmartInfoDAMErrorRate_Object((1,3,6,1,4,1,12740,3,1,4,1,47),_EqlDiskSmartInfoDAMErrorRate_Type())
eqlDiskSmartInfoDAMErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoDAMErrorRate.setStatus(_A)
_EqlDiskSmartInfoDAMErrorRateWorst_Type=Integer32
_EqlDiskSmartInfoDAMErrorRateWorst_Object=MibTableColumn
eqlDiskSmartInfoDAMErrorRateWorst=_EqlDiskSmartInfoDAMErrorRateWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,48),_EqlDiskSmartInfoDAMErrorRateWorst_Type())
eqlDiskSmartInfoDAMErrorRateWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoDAMErrorRateWorst.setStatus(_A)
_EqlDiskSmartInfoECCErrors_Type=Integer32
_EqlDiskSmartInfoECCErrors_Object=MibTableColumn
eqlDiskSmartInfoECCErrors=_EqlDiskSmartInfoECCErrors_Object((1,3,6,1,4,1,12740,3,1,4,1,49),_EqlDiskSmartInfoECCErrors_Type())
eqlDiskSmartInfoECCErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoECCErrors.setStatus(_A)
_EqlDiskSmartInfoECCErrorsWorst_Type=Integer32
_EqlDiskSmartInfoECCErrorsWorst_Object=MibTableColumn
eqlDiskSmartInfoECCErrorsWorst=_EqlDiskSmartInfoECCErrorsWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,50),_EqlDiskSmartInfoECCErrorsWorst_Type())
eqlDiskSmartInfoECCErrorsWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoECCErrorsWorst.setStatus(_A)
_EqlDiskSmartInfoSoftECCCorrection_Type=Integer32
_EqlDiskSmartInfoSoftECCCorrection_Object=MibTableColumn
eqlDiskSmartInfoSoftECCCorrection=_EqlDiskSmartInfoSoftECCCorrection_Object((1,3,6,1,4,1,12740,3,1,4,1,51),_EqlDiskSmartInfoSoftECCCorrection_Type())
eqlDiskSmartInfoSoftECCCorrection.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoSoftECCCorrection.setStatus(_A)
_EqlDiskSmartInfoSoftECCCorrectionWorst_Type=Integer32
_EqlDiskSmartInfoSoftECCCorrectionWorst_Object=MibTableColumn
eqlDiskSmartInfoSoftECCCorrectionWorst=_EqlDiskSmartInfoSoftECCCorrectionWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,52),_EqlDiskSmartInfoSoftECCCorrectionWorst_Type())
eqlDiskSmartInfoSoftECCCorrectionWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoSoftECCCorrectionWorst.setStatus(_A)
_EqlDiskSmartInfoThermalAsperityRate_Type=Integer32
_EqlDiskSmartInfoThermalAsperityRate_Object=MibTableColumn
eqlDiskSmartInfoThermalAsperityRate=_EqlDiskSmartInfoThermalAsperityRate_Object((1,3,6,1,4,1,12740,3,1,4,1,53),_EqlDiskSmartInfoThermalAsperityRate_Type())
eqlDiskSmartInfoThermalAsperityRate.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoThermalAsperityRate.setStatus(_A)
_EqlDiskSmartInfoThermalAsperityRateWorst_Type=Integer32
_EqlDiskSmartInfoThermalAsperityRateWorst_Object=MibTableColumn
eqlDiskSmartInfoThermalAsperityRateWorst=_EqlDiskSmartInfoThermalAsperityRateWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,54),_EqlDiskSmartInfoThermalAsperityRateWorst_Type())
eqlDiskSmartInfoThermalAsperityRateWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoThermalAsperityRateWorst.setStatus(_A)
_EqlDiskSmartInfoSpinHighCount_Type=Integer32
_EqlDiskSmartInfoSpinHighCount_Object=MibTableColumn
eqlDiskSmartInfoSpinHighCount=_EqlDiskSmartInfoSpinHighCount_Object((1,3,6,1,4,1,12740,3,1,4,1,55),_EqlDiskSmartInfoSpinHighCount_Type())
eqlDiskSmartInfoSpinHighCount.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoSpinHighCount.setStatus(_A)
_EqlDiskSmartInfoSpinHighCountWorst_Type=Integer32
_EqlDiskSmartInfoSpinHighCountWorst_Object=MibTableColumn
eqlDiskSmartInfoSpinHighCountWorst=_EqlDiskSmartInfoSpinHighCountWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,56),_EqlDiskSmartInfoSpinHighCountWorst_Type())
eqlDiskSmartInfoSpinHighCountWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoSpinHighCountWorst.setStatus(_A)
_EqlDiskSmartInfoSpinBuzz_Type=Integer32
_EqlDiskSmartInfoSpinBuzz_Object=MibTableColumn
eqlDiskSmartInfoSpinBuzz=_EqlDiskSmartInfoSpinBuzz_Object((1,3,6,1,4,1,12740,3,1,4,1,57),_EqlDiskSmartInfoSpinBuzz_Type())
eqlDiskSmartInfoSpinBuzz.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoSpinBuzz.setStatus(_A)
_EqlDiskSmartInfoSpinBuzzWorst_Type=Integer32
_EqlDiskSmartInfoSpinBuzzWorst_Object=MibTableColumn
eqlDiskSmartInfoSpinBuzzWorst=_EqlDiskSmartInfoSpinBuzzWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,58),_EqlDiskSmartInfoSpinBuzzWorst_Type())
eqlDiskSmartInfoSpinBuzzWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoSpinBuzzWorst.setStatus(_A)
_EqlDiskSmartInfoOfflineSeekPerformance_Type=Integer32
_EqlDiskSmartInfoOfflineSeekPerformance_Object=MibTableColumn
eqlDiskSmartInfoOfflineSeekPerformance=_EqlDiskSmartInfoOfflineSeekPerformance_Object((1,3,6,1,4,1,12740,3,1,4,1,59),_EqlDiskSmartInfoOfflineSeekPerformance_Type())
eqlDiskSmartInfoOfflineSeekPerformance.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoOfflineSeekPerformance.setStatus(_A)
_EqlDiskSmartInfoOfflineSeekPerformanceWorst_Type=Integer32
_EqlDiskSmartInfoOfflineSeekPerformanceWorst_Object=MibTableColumn
eqlDiskSmartInfoOfflineSeekPerformanceWorst=_EqlDiskSmartInfoOfflineSeekPerformanceWorst_Object((1,3,6,1,4,1,12740,3,1,4,1,60),_EqlDiskSmartInfoOfflineSeekPerformanceWorst_Type())
eqlDiskSmartInfoOfflineSeekPerformanceWorst.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoOfflineSeekPerformanceWorst.setStatus(_A)
_EqlDiskSmartInfoThresholdExceeded_Type=Integer32
_EqlDiskSmartInfoThresholdExceeded_Object=MibTableColumn
eqlDiskSmartInfoThresholdExceeded=_EqlDiskSmartInfoThresholdExceeded_Object((1,3,6,1,4,1,12740,3,1,4,1,61),_EqlDiskSmartInfoThresholdExceeded_Type())
eqlDiskSmartInfoThresholdExceeded.setMaxAccess(_B)
if mibBuilder.loadTexts:eqlDiskSmartInfoThresholdExceeded.setStatus(_A)
_EqldiskNotifications_ObjectIdentity=ObjectIdentity
eqldiskNotifications=_EqldiskNotifications_ObjectIdentity((1,3,6,1,4,1,12740,3,2))
_EqldiskMgmtNotifications_ObjectIdentity=ObjectIdentity
eqldiskMgmtNotifications=_EqldiskMgmtNotifications_ObjectIdentity((1,3,6,1,4,1,12740,3,2,1))
_EqldiskConformance_ObjectIdentity=ObjectIdentity
eqldiskConformance=_EqldiskConformance_ObjectIdentity((1,3,6,1,4,1,12740,3,3))
eqlDiskEntry.registerAugmentions((_D,_K))
eqlDiskStatusEntry.setIndexNames(*eqlDiskEntry.getIndexNames())
eqlDiskEntry.registerAugmentions((_D,_L))
eqlDiskErrorEntry.setIndexNames(*eqlDiskEntry.getIndexNames())
eqlDiskEntry.registerAugmentions((_D,_M))
eqlDiskSmartInfoEntry.setIndexNames(*eqlDiskEntry.getIndexNames())
eqlDiskStatusChange=NotificationType((1,3,6,1,4,1,12740,3,2,1,1))
eqlDiskStatusChange.setObjects(*((_D,_N),(_D,_O)))
if mibBuilder.loadTexts:eqlDiskStatusChange.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'eqldiskModule':eqldiskModule,'eqldiskObjects':eqldiskObjects,'eqlDiskTable':eqlDiskTable,'eqlDiskEntry':eqlDiskEntry,_J:eqlDiskIndex,'eqlDiskType':eqlDiskType,'eqlDiskModelNumber':eqlDiskModelNumber,'eqlDiskRevisionNumber':eqlDiskRevisionNumber,'eqlDiskSerialNumber':eqlDiskSerialNumber,'eqlDiskSize':eqlDiskSize,'eqlDiskAdminStatus':eqlDiskAdminStatus,_N:eqlDiskStatus,'eqlDiskErrors':eqlDiskErrors,'eqlDiskId':eqlDiskId,_O:eqlDiskSlot,'eqlDiskTypeEnum':eqlDiskTypeEnum,'eqlDiskRPM':eqlDiskRPM,'eqlDiskSectorSize':eqlDiskSectorSize,'eqlDiskManufacturingInfo':eqlDiskManufacturingInfo,'eqlDiskPI':eqlDiskPI,'eqlDiskHealth':eqlDiskHealth,'eqlDiskStatusTable':eqlDiskStatusTable,_K:eqlDiskStatusEntry,'eqlDiskStatusXfers':eqlDiskStatusXfers,'eqlDiskStatusBytesRead':eqlDiskStatusBytesRead,'eqlDiskStatusBytesWritten':eqlDiskStatusBytesWritten,'eqlDiskStatusBusyTime':eqlDiskStatusBusyTime,'eqlDiskStatusNumIOs':eqlDiskStatusNumIOs,'eqlDiskStatusFailXfers':eqlDiskStatusFailXfers,'eqlDiskStatusNumResets':eqlDiskStatusNumResets,'eqlDiskStatusTotalQD':eqlDiskStatusTotalQD,'eqlDiskStatusLifetime':eqlDiskStatusLifetime,'eqlDiskErrorTable':eqlDiskErrorTable,_L:eqlDiskErrorEntry,'eqlDiskErrorPhyReady':eqlDiskErrorPhyReady,'eqlDiskErrorPhyInternal':eqlDiskErrorPhyInternal,'eqlDiskErrorCommWake':eqlDiskErrorCommWake,'eqlDiskErrorDecode10b8b':eqlDiskErrorDecode10b8b,'eqlDiskErrorDisparity':eqlDiskErrorDisparity,'eqlDiskErrorCRC':eqlDiskErrorCRC,'eqlDiskErrorHandShake':eqlDiskErrorHandShake,'eqlDiskErrorLinkSeq':eqlDiskErrorLinkSeq,'eqlDiskErrorTransportState':eqlDiskErrorTransportState,'eqlDiskErrorUnrecFIS':eqlDiskErrorUnrecFIS,'eqlDiskSmartInfoTable':eqlDiskSmartInfoTable,_M:eqlDiskSmartInfoEntry,'eqlDiskSmartInfoRawReadErrorRate':eqlDiskSmartInfoRawReadErrorRate,'eqlDiskSmartInfoRawReadErrorRateWorst':eqlDiskSmartInfoRawReadErrorRateWorst,'eqlDiskSmartInfoThroughputPerformance':eqlDiskSmartInfoThroughputPerformance,'eqlDiskSmartInfoThroughputPerformanceWorst':eqlDiskSmartInfoThroughputPerformanceWorst,'eqlDiskSmartInfoSpinUpTime':eqlDiskSmartInfoSpinUpTime,'eqlDiskSmartInfoSpinUpTimeWorst':eqlDiskSmartInfoSpinUpTimeWorst,'eqlDiskSmartInfoStartStopCount':eqlDiskSmartInfoStartStopCount,'eqlDiskSmartInfoStartStopCountWorst':eqlDiskSmartInfoStartStopCountWorst,'eqlDiskSmartInfoReallocatedSectorCount':eqlDiskSmartInfoReallocatedSectorCount,'eqlDiskSmartInfoReallocatedSectorCountWorst':eqlDiskSmartInfoReallocatedSectorCountWorst,'eqlDiskSmartInfoReadChannelMargin':eqlDiskSmartInfoReadChannelMargin,'eqlDiskSmartInfoReadChannelMarginWorst':eqlDiskSmartInfoReadChannelMarginWorst,'eqlDiskSmartInfoSeekErrorRate':eqlDiskSmartInfoSeekErrorRate,'eqlDiskSmartInfoSeekErrorRateWorst':eqlDiskSmartInfoSeekErrorRateWorst,'eqlDiskSmartInfoSeekPerformance':eqlDiskSmartInfoSeekPerformance,'eqlDiskSmartInfoSeekPerformanceWorst':eqlDiskSmartInfoSeekPerformanceWorst,'eqlDiskSmartInfoPowerOnHours':eqlDiskSmartInfoPowerOnHours,'eqlDiskSmartInfoPowerOnHoursWorst':eqlDiskSmartInfoPowerOnHoursWorst,'eqlDiskSmartInfoSpinupRetries':eqlDiskSmartInfoSpinupRetries,'eqlDiskSmartInfoSpinupRetriesWorst':eqlDiskSmartInfoSpinupRetriesWorst,'eqlDiskSmartInfoDriveRecalibRetryCount':eqlDiskSmartInfoDriveRecalibRetryCount,'eqlDiskSmartInfoDriveRecalibRetryCountWorst':eqlDiskSmartInfoDriveRecalibRetryCountWorst,'eqlDiskSmartInfoPowerCycleCount':eqlDiskSmartInfoPowerCycleCount,'eqlDiskSmartInfoPowerCycleCountWorst':eqlDiskSmartInfoPowerCycleCountWorst,'eqlDiskSmartInfoReadSoftErrorRate':eqlDiskSmartInfoReadSoftErrorRate,'eqlDiskSmartInfoReadSoftErrorRateWorst':eqlDiskSmartInfoReadSoftErrorRateWorst,'eqlDiskSmartInfoEmergencyRetractCycles':eqlDiskSmartInfoEmergencyRetractCycles,'eqlDiskSmartInfoEmergencyRetractCyclesWorst':eqlDiskSmartInfoEmergencyRetractCyclesWorst,'eqlDiskSmartInfoLoadUnloadCycles':eqlDiskSmartInfoLoadUnloadCycles,'eqlDiskSmartInfoLoadUnloadCyclesWorst':eqlDiskSmartInfoLoadUnloadCyclesWorst,'eqlDiskSmartInfoHDDTemp':eqlDiskSmartInfoHDDTemp,'eqlDiskSmartInfoHDDTempWorst':eqlDiskSmartInfoHDDTempWorst,'eqlDiskSmartInfoOnTheFlyErrorRate':eqlDiskSmartInfoOnTheFlyErrorRate,'eqlDiskSmartInfoOnTheFlyErrorRateWorst':eqlDiskSmartInfoOnTheFlyErrorRateWorst,'eqlDiskSmartInfoSelfTestReallocSectors':eqlDiskSmartInfoSelfTestReallocSectors,'eqlDiskSmartInfoSelfTestReallocSectorsWorst':eqlDiskSmartInfoSelfTestReallocSectorsWorst,'eqlDiskSmartInfoPendingDefects':eqlDiskSmartInfoPendingDefects,'eqlDiskSmartInfoPendingDefectsWorst':eqlDiskSmartInfoPendingDefectsWorst,'eqlDiskSmartInfoOfflineSurfaceScan':eqlDiskSmartInfoOfflineSurfaceScan,'eqlDiskSmartInfoOfflineSurfaceScanWorst':eqlDiskSmartInfoOfflineSurfaceScanWorst,'eqlDiskSmartInfoUltraDMACRCErrorRate':eqlDiskSmartInfoUltraDMACRCErrorRate,'eqlDiskSmartInfoUltraDMACRCErrorRateWorst':eqlDiskSmartInfoUltraDMACRCErrorRateWorst,'eqlDiskSmartInfoWritePreampErrors':eqlDiskSmartInfoWritePreampErrors,'eqlDiskSmartInfoWritePreampErrorsWorst':eqlDiskSmartInfoWritePreampErrorsWorst,'eqlDiskSmartInfoOffTrackErrors':eqlDiskSmartInfoOffTrackErrors,'eqlDiskSmartInfoOffTrackErrorsWorst':eqlDiskSmartInfoOffTrackErrorsWorst,'eqlDiskSmartInfoDAMErrorRate':eqlDiskSmartInfoDAMErrorRate,'eqlDiskSmartInfoDAMErrorRateWorst':eqlDiskSmartInfoDAMErrorRateWorst,'eqlDiskSmartInfoECCErrors':eqlDiskSmartInfoECCErrors,'eqlDiskSmartInfoECCErrorsWorst':eqlDiskSmartInfoECCErrorsWorst,'eqlDiskSmartInfoSoftECCCorrection':eqlDiskSmartInfoSoftECCCorrection,'eqlDiskSmartInfoSoftECCCorrectionWorst':eqlDiskSmartInfoSoftECCCorrectionWorst,'eqlDiskSmartInfoThermalAsperityRate':eqlDiskSmartInfoThermalAsperityRate,'eqlDiskSmartInfoThermalAsperityRateWorst':eqlDiskSmartInfoThermalAsperityRateWorst,'eqlDiskSmartInfoSpinHighCount':eqlDiskSmartInfoSpinHighCount,'eqlDiskSmartInfoSpinHighCountWorst':eqlDiskSmartInfoSpinHighCountWorst,'eqlDiskSmartInfoSpinBuzz':eqlDiskSmartInfoSpinBuzz,'eqlDiskSmartInfoSpinBuzzWorst':eqlDiskSmartInfoSpinBuzzWorst,'eqlDiskSmartInfoOfflineSeekPerformance':eqlDiskSmartInfoOfflineSeekPerformance,'eqlDiskSmartInfoOfflineSeekPerformanceWorst':eqlDiskSmartInfoOfflineSeekPerformanceWorst,'eqlDiskSmartInfoThresholdExceeded':eqlDiskSmartInfoThresholdExceeded,'eqldiskNotifications':eqldiskNotifications,'eqldiskMgmtNotifications':eqldiskMgmtNotifications,'eqlDiskStatusChange':eqlDiskStatusChange,'eqldiskConformance':eqldiskConformance})