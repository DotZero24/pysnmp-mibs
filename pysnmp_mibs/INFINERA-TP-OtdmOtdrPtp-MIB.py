_X='otdmOtdrPtpGroup'
_W='otdmOtdrPtpTestResultUpload'
_V='otdmOtdrPtpTestResultFileName'
_U='otdmOtdrPtpTestEndOfFiberThreshold'
_T='otdmOtdrPtpTestReflectionThreshold'
_S='otdmOtdrPtpTestEventLossThreshold'
_R='otdmOtdrPtpTestFiberType'
_Q='otdmOtdrPtpTestFiberID'
_P='otdmOtdrPtpTestCableID'
_O='otdmOtdrPtpAcquistionTime'
_N='otdmOtdrPtpDetectionRange'
_M='otdmOtdrPtpTestPulseWidth'
_L='otdmOtdrPtpTestAquistionMode'
_K='otdmOtdrPtpTestControlStatus'
_J='otdmOtdrPtpProvisionedNeighborPtp'
_I='otdmOtdrPtpLstSuccConnValidationTime'
_H='otdmOtdrPtpConnectivityState'
_G='ifIndex'
_F='IF-MIB'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='INFINERA-TP-OtdmOtdrPtp-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatHundredths,InfnFiberType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','InfnFiberType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
otdmOtdrPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,48))
if mibBuilder.loadTexts:otdmOtdrPtpMIB.setRevisions(('2013-10-20 00:00',))
_OtdmOtdrPtpTable_Object=MibTable
otdmOtdrPtpTable=_OtdmOtdrPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,48,1))
if mibBuilder.loadTexts:otdmOtdrPtpTable.setStatus(_A)
_OtdmOtdrPtpEntry_Object=MibTableRow
otdmOtdrPtpEntry=_OtdmOtdrPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,48,1,1))
otdmOtdrPtpEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:otdmOtdrPtpEntry.setStatus(_A)
class _OtdmOtdrPtpConnectivityState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notVerified',1),('valid',2),('inValid',3)))
_OtdmOtdrPtpConnectivityState_Type.__name__=_D
_OtdmOtdrPtpConnectivityState_Object=MibTableColumn
otdmOtdrPtpConnectivityState=_OtdmOtdrPtpConnectivityState_Object((1,3,6,1,4,1,21296,2,2,2,2,48,1,1,1),_OtdmOtdrPtpConnectivityState_Type())
otdmOtdrPtpConnectivityState.setMaxAccess(_E)
if mibBuilder.loadTexts:otdmOtdrPtpConnectivityState.setStatus(_A)
_OtdmOtdrPtpLstSuccConnValidationTime_Type=Integer32
_OtdmOtdrPtpLstSuccConnValidationTime_Object=MibTableColumn
otdmOtdrPtpLstSuccConnValidationTime=_OtdmOtdrPtpLstSuccConnValidationTime_Object((1,3,6,1,4,1,21296,2,2,2,2,48,1,1,2),_OtdmOtdrPtpLstSuccConnValidationTime_Type())
otdmOtdrPtpLstSuccConnValidationTime.setMaxAccess(_E)
if mibBuilder.loadTexts:otdmOtdrPtpLstSuccConnValidationTime.setStatus(_A)
_OtdmOtdrPtpProvisionedNeighborPtp_Type=DisplayString
_OtdmOtdrPtpProvisionedNeighborPtp_Object=MibTableColumn
otdmOtdrPtpProvisionedNeighborPtp=_OtdmOtdrPtpProvisionedNeighborPtp_Object((1,3,6,1,4,1,21296,2,2,2,2,48,1,1,3),_OtdmOtdrPtpProvisionedNeighborPtp_Type())
otdmOtdrPtpProvisionedNeighborPtp.setMaxAccess(_C)
if mibBuilder.loadTexts:otdmOtdrPtpProvisionedNeighborPtp.setStatus(_A)
class _OtdmOtdrPtpTestControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('inProgress',1),('queuedUp',2),('scheduled',3),('idle',4)))
_OtdmOtdrPtpTestControlStatus_Type.__name__=_D
_OtdmOtdrPtpTestControlStatus_Object=MibTableColumn
otdmOtdrPtpTestControlStatus=_OtdmOtdrPtpTestControlStatus_Object((1,3,6,1,4,1,21296,2,2,2,2,48,1,1,4),_OtdmOtdrPtpTestControlStatus_Type())
otdmOtdrPtpTestControlStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:otdmOtdrPtpTestControlStatus.setStatus(_A)
class _OtdmOtdrPtpTestAquistionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('automatic',1),('manual',2)))
_OtdmOtdrPtpTestAquistionMode_Type.__name__=_D
_OtdmOtdrPtpTestAquistionMode_Object=MibTableColumn
otdmOtdrPtpTestAquistionMode=_OtdmOtdrPtpTestAquistionMode_Object((1,3,6,1,4,1,21296,2,2,2,2,48,1,1,5),_OtdmOtdrPtpTestAquistionMode_Type())
otdmOtdrPtpTestAquistionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:otdmOtdrPtpTestAquistionMode.setStatus(_A)
class _OtdmOtdrPtpTestPulseWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('ns5',1),('ns10',2),('ns30',3),('ns100',4),('ns300',5),('us1',6),('us3',7),('us10',8),('us20',9)))
_OtdmOtdrPtpTestPulseWidth_Type.__name__=_D
_OtdmOtdrPtpTestPulseWidth_Object=MibTableColumn
otdmOtdrPtpTestPulseWidth=_OtdmOtdrPtpTestPulseWidth_Object((1,3,6,1,4,1,21296,2,2,2,2,48,1,1,6),_OtdmOtdrPtpTestPulseWidth_Type())
otdmOtdrPtpTestPulseWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:otdmOtdrPtpTestPulseWidth.setStatus(_A)
class _OtdmOtdrPtpDetectionRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('km05',1),('km1',2),('km2',3),('km5',4),('km10',5),('km20',6),('km40',7),('km80',8),('km160',9),('km260',10)))
_OtdmOtdrPtpDetectionRange_Type.__name__=_D
_OtdmOtdrPtpDetectionRange_Object=MibTableColumn
otdmOtdrPtpDetectionRange=_OtdmOtdrPtpDetectionRange_Object((1,3,6,1,4,1,21296,2,2,2,2,48,1,1,7),_OtdmOtdrPtpDetectionRange_Type())
otdmOtdrPtpDetectionRange.setMaxAccess(_C)
if mibBuilder.loadTexts:otdmOtdrPtpDetectionRange.setStatus(_A)
class _OtdmOtdrPtpAcquistionTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('sec1',1),('sec5',2),('sec10',3),('sec20',4),('sec30',5),('sec60',6),('sec120',7),('sec180',8),('sec240',9),('sec300',10)))
_OtdmOtdrPtpAcquistionTime_Type.__name__=_D
_OtdmOtdrPtpAcquistionTime_Object=MibTableColumn
otdmOtdrPtpAcquistionTime=_OtdmOtdrPtpAcquistionTime_Object((1,3,6,1,4,1,21296,2,2,2,2,48,1,1,8),_OtdmOtdrPtpAcquistionTime_Type())
otdmOtdrPtpAcquistionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:otdmOtdrPtpAcquistionTime.setStatus(_A)
_OtdmOtdrPtpTestCableID_Type=DisplayString
_OtdmOtdrPtpTestCableID_Object=MibTableColumn
otdmOtdrPtpTestCableID=_OtdmOtdrPtpTestCableID_Object((1,3,6,1,4,1,21296,2,2,2,2,48,1,1,9),_OtdmOtdrPtpTestCableID_Type())
otdmOtdrPtpTestCableID.setMaxAccess(_C)
if mibBuilder.loadTexts:otdmOtdrPtpTestCableID.setStatus(_A)
_OtdmOtdrPtpTestFiberID_Type=DisplayString
_OtdmOtdrPtpTestFiberID_Object=MibTableColumn
otdmOtdrPtpTestFiberID=_OtdmOtdrPtpTestFiberID_Object((1,3,6,1,4,1,21296,2,2,2,2,48,1,1,10),_OtdmOtdrPtpTestFiberID_Type())
otdmOtdrPtpTestFiberID.setMaxAccess(_C)
if mibBuilder.loadTexts:otdmOtdrPtpTestFiberID.setStatus(_A)
_OtdmOtdrPtpTestFiberType_Type=InfnFiberType
_OtdmOtdrPtpTestFiberType_Object=MibTableColumn
otdmOtdrPtpTestFiberType=_OtdmOtdrPtpTestFiberType_Object((1,3,6,1,4,1,21296,2,2,2,2,48,1,1,11),_OtdmOtdrPtpTestFiberType_Type())
otdmOtdrPtpTestFiberType.setMaxAccess(_E)
if mibBuilder.loadTexts:otdmOtdrPtpTestFiberType.setStatus(_A)
_OtdmOtdrPtpTestEventLossThreshold_Type=FloatHundredths
_OtdmOtdrPtpTestEventLossThreshold_Object=MibTableColumn
otdmOtdrPtpTestEventLossThreshold=_OtdmOtdrPtpTestEventLossThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,48,1,1,12),_OtdmOtdrPtpTestEventLossThreshold_Type())
otdmOtdrPtpTestEventLossThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:otdmOtdrPtpTestEventLossThreshold.setStatus(_A)
_OtdmOtdrPtpTestReflectionThreshold_Type=FloatHundredths
_OtdmOtdrPtpTestReflectionThreshold_Object=MibTableColumn
otdmOtdrPtpTestReflectionThreshold=_OtdmOtdrPtpTestReflectionThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,48,1,1,13),_OtdmOtdrPtpTestReflectionThreshold_Type())
otdmOtdrPtpTestReflectionThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:otdmOtdrPtpTestReflectionThreshold.setStatus(_A)
_OtdmOtdrPtpTestEndOfFiberThreshold_Type=FloatHundredths
_OtdmOtdrPtpTestEndOfFiberThreshold_Object=MibTableColumn
otdmOtdrPtpTestEndOfFiberThreshold=_OtdmOtdrPtpTestEndOfFiberThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,48,1,1,15),_OtdmOtdrPtpTestEndOfFiberThreshold_Type())
otdmOtdrPtpTestEndOfFiberThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:otdmOtdrPtpTestEndOfFiberThreshold.setStatus(_A)
_OtdmOtdrPtpTestResultFileName_Type=DisplayString
_OtdmOtdrPtpTestResultFileName_Object=MibTableColumn
otdmOtdrPtpTestResultFileName=_OtdmOtdrPtpTestResultFileName_Object((1,3,6,1,4,1,21296,2,2,2,2,48,1,1,16),_OtdmOtdrPtpTestResultFileName_Type())
otdmOtdrPtpTestResultFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:otdmOtdrPtpTestResultFileName.setStatus(_A)
class _OtdmOtdrPtpTestResultUpload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_OtdmOtdrPtpTestResultUpload_Type.__name__=_D
_OtdmOtdrPtpTestResultUpload_Object=MibTableColumn
otdmOtdrPtpTestResultUpload=_OtdmOtdrPtpTestResultUpload_Object((1,3,6,1,4,1,21296,2,2,2,2,48,1,1,17),_OtdmOtdrPtpTestResultUpload_Type())
otdmOtdrPtpTestResultUpload.setMaxAccess(_C)
if mibBuilder.loadTexts:otdmOtdrPtpTestResultUpload.setStatus(_A)
_OtdmOtdrPtpConformance_ObjectIdentity=ObjectIdentity
otdmOtdrPtpConformance=_OtdmOtdrPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,48,3))
_OtdmOtdrPtpCompliances_ObjectIdentity=ObjectIdentity
otdmOtdrPtpCompliances=_OtdmOtdrPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,48,3,1))
_OtdmOtdrPtpGroups_ObjectIdentity=ObjectIdentity
otdmOtdrPtpGroups=_OtdmOtdrPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,48,3,2))
otdmOtdrPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,48,3,2,1))
otdmOtdrPtpGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:otdmOtdrPtpGroup.setStatus(_A)
otdmOtdrPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,48,3,1,1))
otdmOtdrPtpCompliance.setObjects((_B,_X))
if mibBuilder.loadTexts:otdmOtdrPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'otdmOtdrPtpMIB':otdmOtdrPtpMIB,'otdmOtdrPtpTable':otdmOtdrPtpTable,'otdmOtdrPtpEntry':otdmOtdrPtpEntry,_H:otdmOtdrPtpConnectivityState,_I:otdmOtdrPtpLstSuccConnValidationTime,_J:otdmOtdrPtpProvisionedNeighborPtp,_K:otdmOtdrPtpTestControlStatus,_L:otdmOtdrPtpTestAquistionMode,_M:otdmOtdrPtpTestPulseWidth,_N:otdmOtdrPtpDetectionRange,_O:otdmOtdrPtpAcquistionTime,_P:otdmOtdrPtpTestCableID,_Q:otdmOtdrPtpTestFiberID,_R:otdmOtdrPtpTestFiberType,_S:otdmOtdrPtpTestEventLossThreshold,_T:otdmOtdrPtpTestReflectionThreshold,_U:otdmOtdrPtpTestEndOfFiberThreshold,_V:otdmOtdrPtpTestResultFileName,_W:otdmOtdrPtpTestResultUpload,'otdmOtdrPtpConformance':otdmOtdrPtpConformance,'otdmOtdrPtpCompliances':otdmOtdrPtpCompliances,'otdmOtdrPtpCompliance':otdmOtdrPtpCompliance,'otdmOtdrPtpGroups':otdmOtdrPtpGroups,_X:otdmOtdrPtpGroup})