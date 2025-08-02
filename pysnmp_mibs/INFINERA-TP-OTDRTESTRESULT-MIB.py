_e='otdrTestResultGroup'
_d='otdrTestResultUploadStatus'
_c='otdrTestResultEndOfFiberThreshold'
_b='otdrTestResultReflectanceThreshold'
_a='otdrTestResultEventLossThreshold'
_Z='otdrTestResultAcquisitionRangeDistance'
_Y='otdrTestResultAcquisitionRange'
_X='otdrTestResultTestAcquisitionTime'
_W='otdrTestResultBackScatterCoefficient'
_V='otdrTestResultDataSpacing'
_U='otdrTestResultPulseWidth'
_T='otdrTestResultUnitsOfDistance'
_S='otdrTestResultOpticalReturnLoss'
_R='otdrTestResultEndToEndLoss'
_Q='otdrTestResultKeyEventsCount'
_P='otdrTestResultDataPointsCount'
_O='otdrTestResultTestFiberType'
_N='otdrTestResultTestFiberID'
_M='otdrTestResultTestCableID'
_L='otdrTestResultConnectivityState'
_K='otdrTestResultProvisionedNeighborPtp'
_J='otdrTestResultAcquisitionMode'
_I='otdrTestResultTestExecutionType'
_H='otdrTestResultOtdmPortId'
_G='otdrTestResultOtdmSerialNumber'
_F='otdrTestResultTimeStamp'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-TP-OTDRTESTRESULT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatHundredths,InfnFiberType,InfnOtdrFileUploadStatus,InfnOtdrPtpConnState,InfnOtdrTestAcquisitionMode,InfnOtdrTestExecutionType,InfnOtdrTestPulseWidth=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','InfnFiberType','InfnOtdrFileUploadStatus','InfnOtdrPtpConnState','InfnOtdrTestAcquisitionMode','InfnOtdrTestExecutionType','InfnOtdrTestPulseWidth')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
otdrTestResultMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,62))
_OtdrTestResultTable_Object=MibTable
otdrTestResultTable=_OtdrTestResultTable_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1))
if mibBuilder.loadTexts:otdrTestResultTable.setStatus(_A)
_OtdrTestResultEntry_Object=MibTableRow
otdrTestResultEntry=_OtdrTestResultEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1))
otdrTestResultEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:otdrTestResultEntry.setStatus(_A)
_OtdrTestResultTimeStamp_Type=Integer32
_OtdrTestResultTimeStamp_Object=MibTableColumn
otdrTestResultTimeStamp=_OtdrTestResultTimeStamp_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,1),_OtdrTestResultTimeStamp_Type())
otdrTestResultTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultTimeStamp.setStatus(_A)
_OtdrTestResultOtdmSerialNumber_Type=DisplayString
_OtdrTestResultOtdmSerialNumber_Object=MibTableColumn
otdrTestResultOtdmSerialNumber=_OtdrTestResultOtdmSerialNumber_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,2),_OtdrTestResultOtdmSerialNumber_Type())
otdrTestResultOtdmSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultOtdmSerialNumber.setStatus(_A)
_OtdrTestResultOtdmPortId_Type=DisplayString
_OtdrTestResultOtdmPortId_Object=MibTableColumn
otdrTestResultOtdmPortId=_OtdrTestResultOtdmPortId_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,3),_OtdrTestResultOtdmPortId_Type())
otdrTestResultOtdmPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultOtdmPortId.setStatus(_A)
_OtdrTestResultTestExecutionType_Type=InfnOtdrTestExecutionType
_OtdrTestResultTestExecutionType_Object=MibTableColumn
otdrTestResultTestExecutionType=_OtdrTestResultTestExecutionType_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,4),_OtdrTestResultTestExecutionType_Type())
otdrTestResultTestExecutionType.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultTestExecutionType.setStatus(_A)
_OtdrTestResultAcquisitionMode_Type=InfnOtdrTestAcquisitionMode
_OtdrTestResultAcquisitionMode_Object=MibTableColumn
otdrTestResultAcquisitionMode=_OtdrTestResultAcquisitionMode_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,5),_OtdrTestResultAcquisitionMode_Type())
otdrTestResultAcquisitionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultAcquisitionMode.setStatus(_A)
_OtdrTestResultProvisionedNeighborPtp_Type=DisplayString
_OtdrTestResultProvisionedNeighborPtp_Object=MibTableColumn
otdrTestResultProvisionedNeighborPtp=_OtdrTestResultProvisionedNeighborPtp_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,6),_OtdrTestResultProvisionedNeighborPtp_Type())
otdrTestResultProvisionedNeighborPtp.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultProvisionedNeighborPtp.setStatus(_A)
_OtdrTestResultConnectivityState_Type=InfnOtdrPtpConnState
_OtdrTestResultConnectivityState_Object=MibTableColumn
otdrTestResultConnectivityState=_OtdrTestResultConnectivityState_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,7),_OtdrTestResultConnectivityState_Type())
otdrTestResultConnectivityState.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultConnectivityState.setStatus(_A)
_OtdrTestResultTestCableID_Type=DisplayString
_OtdrTestResultTestCableID_Object=MibTableColumn
otdrTestResultTestCableID=_OtdrTestResultTestCableID_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,8),_OtdrTestResultTestCableID_Type())
otdrTestResultTestCableID.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultTestCableID.setStatus(_A)
_OtdrTestResultTestFiberID_Type=DisplayString
_OtdrTestResultTestFiberID_Object=MibTableColumn
otdrTestResultTestFiberID=_OtdrTestResultTestFiberID_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,9),_OtdrTestResultTestFiberID_Type())
otdrTestResultTestFiberID.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultTestFiberID.setStatus(_A)
_OtdrTestResultTestFiberType_Type=InfnFiberType
_OtdrTestResultTestFiberType_Object=MibTableColumn
otdrTestResultTestFiberType=_OtdrTestResultTestFiberType_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,10),_OtdrTestResultTestFiberType_Type())
otdrTestResultTestFiberType.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultTestFiberType.setStatus(_A)
_OtdrTestResultDataPointsCount_Type=Integer32
_OtdrTestResultDataPointsCount_Object=MibTableColumn
otdrTestResultDataPointsCount=_OtdrTestResultDataPointsCount_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,11),_OtdrTestResultDataPointsCount_Type())
otdrTestResultDataPointsCount.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultDataPointsCount.setStatus(_A)
_OtdrTestResultKeyEventsCount_Type=Integer32
_OtdrTestResultKeyEventsCount_Object=MibTableColumn
otdrTestResultKeyEventsCount=_OtdrTestResultKeyEventsCount_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,12),_OtdrTestResultKeyEventsCount_Type())
otdrTestResultKeyEventsCount.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultKeyEventsCount.setStatus(_A)
_OtdrTestResultEndToEndLoss_Type=FloatHundredths
_OtdrTestResultEndToEndLoss_Object=MibTableColumn
otdrTestResultEndToEndLoss=_OtdrTestResultEndToEndLoss_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,13),_OtdrTestResultEndToEndLoss_Type())
otdrTestResultEndToEndLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultEndToEndLoss.setStatus(_A)
_OtdrTestResultOpticalReturnLoss_Type=FloatHundredths
_OtdrTestResultOpticalReturnLoss_Object=MibTableColumn
otdrTestResultOpticalReturnLoss=_OtdrTestResultOpticalReturnLoss_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,14),_OtdrTestResultOpticalReturnLoss_Type())
otdrTestResultOpticalReturnLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultOpticalReturnLoss.setStatus(_A)
_OtdrTestResultUnitsOfDistance_Type=DisplayString
_OtdrTestResultUnitsOfDistance_Object=MibTableColumn
otdrTestResultUnitsOfDistance=_OtdrTestResultUnitsOfDistance_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,15),_OtdrTestResultUnitsOfDistance_Type())
otdrTestResultUnitsOfDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultUnitsOfDistance.setStatus(_A)
_OtdrTestResultPulseWidth_Type=InfnOtdrTestPulseWidth
_OtdrTestResultPulseWidth_Object=MibTableColumn
otdrTestResultPulseWidth=_OtdrTestResultPulseWidth_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,16),_OtdrTestResultPulseWidth_Type())
otdrTestResultPulseWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultPulseWidth.setStatus(_A)
_OtdrTestResultDataSpacing_Type=FloatHundredths
_OtdrTestResultDataSpacing_Object=MibTableColumn
otdrTestResultDataSpacing=_OtdrTestResultDataSpacing_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,17),_OtdrTestResultDataSpacing_Type())
otdrTestResultDataSpacing.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultDataSpacing.setStatus(_A)
_OtdrTestResultBackScatterCoefficient_Type=Integer32
_OtdrTestResultBackScatterCoefficient_Object=MibTableColumn
otdrTestResultBackScatterCoefficient=_OtdrTestResultBackScatterCoefficient_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,18),_OtdrTestResultBackScatterCoefficient_Type())
otdrTestResultBackScatterCoefficient.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultBackScatterCoefficient.setStatus(_A)
_OtdrTestResultTestAcquisitionTime_Type=Integer32
_OtdrTestResultTestAcquisitionTime_Object=MibTableColumn
otdrTestResultTestAcquisitionTime=_OtdrTestResultTestAcquisitionTime_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,19),_OtdrTestResultTestAcquisitionTime_Type())
otdrTestResultTestAcquisitionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultTestAcquisitionTime.setStatus(_A)
_OtdrTestResultAcquisitionRange_Type=Integer32
_OtdrTestResultAcquisitionRange_Object=MibTableColumn
otdrTestResultAcquisitionRange=_OtdrTestResultAcquisitionRange_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,20),_OtdrTestResultAcquisitionRange_Type())
otdrTestResultAcquisitionRange.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultAcquisitionRange.setStatus(_A)
_OtdrTestResultAcquisitionRangeDistance_Type=Integer32
_OtdrTestResultAcquisitionRangeDistance_Object=MibTableColumn
otdrTestResultAcquisitionRangeDistance=_OtdrTestResultAcquisitionRangeDistance_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,21),_OtdrTestResultAcquisitionRangeDistance_Type())
otdrTestResultAcquisitionRangeDistance.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultAcquisitionRangeDistance.setStatus(_A)
_OtdrTestResultEventLossThreshold_Type=FloatHundredths
_OtdrTestResultEventLossThreshold_Object=MibTableColumn
otdrTestResultEventLossThreshold=_OtdrTestResultEventLossThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,22),_OtdrTestResultEventLossThreshold_Type())
otdrTestResultEventLossThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultEventLossThreshold.setStatus(_A)
_OtdrTestResultReflectanceThreshold_Type=Integer32
_OtdrTestResultReflectanceThreshold_Object=MibTableColumn
otdrTestResultReflectanceThreshold=_OtdrTestResultReflectanceThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,23),_OtdrTestResultReflectanceThreshold_Type())
otdrTestResultReflectanceThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultReflectanceThreshold.setStatus(_A)
_OtdrTestResultEndOfFiberThreshold_Type=Integer32
_OtdrTestResultEndOfFiberThreshold_Object=MibTableColumn
otdrTestResultEndOfFiberThreshold=_OtdrTestResultEndOfFiberThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,24),_OtdrTestResultEndOfFiberThreshold_Type())
otdrTestResultEndOfFiberThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultEndOfFiberThreshold.setStatus(_A)
_OtdrTestResultUploadStatus_Type=InfnOtdrFileUploadStatus
_OtdrTestResultUploadStatus_Object=MibTableColumn
otdrTestResultUploadStatus=_OtdrTestResultUploadStatus_Object((1,3,6,1,4,1,21296,2,2,2,2,62,1,1,25),_OtdrTestResultUploadStatus_Type())
otdrTestResultUploadStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:otdrTestResultUploadStatus.setStatus(_A)
_OtdrTestResultConformance_ObjectIdentity=ObjectIdentity
otdrTestResultConformance=_OtdrTestResultConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,62,3))
_OtdrTestResultCompliances_ObjectIdentity=ObjectIdentity
otdrTestResultCompliances=_OtdrTestResultCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,62,3,1))
_OtdrTestResultGroups_ObjectIdentity=ObjectIdentity
otdrTestResultGroups=_OtdrTestResultGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,62,3,2))
otdrTestResultGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,62,3,2,1))
otdrTestResultGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:otdrTestResultGroup.setStatus(_A)
otdrTestResultCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,62,3,1,1))
otdrTestResultCompliance.setObjects((_B,_e))
if mibBuilder.loadTexts:otdrTestResultCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'otdrTestResultMIB':otdrTestResultMIB,'otdrTestResultTable':otdrTestResultTable,'otdrTestResultEntry':otdrTestResultEntry,_F:otdrTestResultTimeStamp,_G:otdrTestResultOtdmSerialNumber,_H:otdrTestResultOtdmPortId,_I:otdrTestResultTestExecutionType,_J:otdrTestResultAcquisitionMode,_K:otdrTestResultProvisionedNeighborPtp,_L:otdrTestResultConnectivityState,_M:otdrTestResultTestCableID,_N:otdrTestResultTestFiberID,_O:otdrTestResultTestFiberType,_P:otdrTestResultDataPointsCount,_Q:otdrTestResultKeyEventsCount,_R:otdrTestResultEndToEndLoss,_S:otdrTestResultOpticalReturnLoss,_T:otdrTestResultUnitsOfDistance,_U:otdrTestResultPulseWidth,_V:otdrTestResultDataSpacing,_W:otdrTestResultBackScatterCoefficient,_X:otdrTestResultTestAcquisitionTime,_Y:otdrTestResultAcquisitionRange,_Z:otdrTestResultAcquisitionRangeDistance,_a:otdrTestResultEventLossThreshold,_b:otdrTestResultReflectanceThreshold,_c:otdrTestResultEndOfFiberThreshold,_d:otdrTestResultUploadStatus,'otdrTestResultConformance':otdrTestResultConformance,'otdrTestResultCompliances':otdrTestResultCompliances,'otdrTestResultCompliance':otdrTestResultCompliance,'otdrTestResultGroups':otdrTestResultGroups,_e:otdrTestResultGroup})