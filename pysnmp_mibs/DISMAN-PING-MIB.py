_AC='pingTimeStampGroup'
_AB='pingGroup'
_AA='pingTestCompleted'
_A9='pingTestFailed'
_A8='pingProbeFailed'
_A7='pingProbeHistoryIndex'
_A6='TruthValue'
_A5='StorageType'
_A4='InterfaceIndexOrZero'
_A3='ObjectIdentifier'
_A2='OctetString'
_A1='pingHistoryGroup'
_A0='pingCtlRowStatusGroup'
_z='pingMinimumGroup'
_y='pingProbeHistoryTime'
_x='deprecated'
_w='pingProbeHistoryLastRC'
_v='pingProbeHistoryStatus'
_u='pingProbeHistoryResponse'
_t='pingCtlRowStatus'
_s='pingCtlDSField'
_r='pingCtlIfIndex'
_q='pingCtlSourceAddress'
_p='pingCtlSourceAddressType'
_o='pingCtlByPassRouteTable'
_n='pingCtlDescr'
_m='pingCtlType'
_l='pingCtlTrapTestFailureFilter'
_k='pingCtlTrapProbeFailureFilter'
_j='pingCtlTrapGeneration'
_i='pingCtlStorageType'
_h='pingCtlMaxRows'
_g='pingCtlFrequency'
_f='pingCtlDataFill'
_e='pingCtlAdminStatus'
_d='pingCtlProbeCount'
_c='pingCtlTimeOut'
_b='pingCtlDataSize'
_a='pingMaxConcurrentRequests'
_Z='not-accessible'
_Y='Integer32'
_X='pingNotificationsGroup'
_W='pingCtlTestName'
_V='pingCtlOwnerIndex'
_U='SnmpAdminString'
_T='InetAddressType'
_S='InetAddress'
_R='milliseconds'
_Q='pingResultsLastGoodProbe'
_P='pingResultsRttSumOfSquares'
_O='pingResultsSentProbes'
_N='pingResultsProbeResponses'
_M='pingResultsAverageRtt'
_L='pingResultsMaxRtt'
_K='pingResultsMinRtt'
_J='pingResultsIpTargetAddress'
_I='pingResultsIpTargetAddressType'
_H='pingResultsOperStatus'
_G='pingCtlTargetAddress'
_F='pingCtlTargetAddressType'
_E='Unsigned32'
_D='read-only'
_C='read-create'
_B='current'
_A='DISMAN-PING-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_A2,_A3)
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_A4)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_S,_T)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_U)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_Y,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso','mib-2')
DateAndTime,DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus',_A5,'TextualConvention',_A6)
pingMIB=ModuleIdentity((1,3,6,1,2,1,80))
if mibBuilder.loadTexts:pingMIB.setRevisions(('2006-06-13 00:00','2000-09-21 00:00'))
class OperationResponseStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('responseReceived',1),('unknown',2),('internalError',3),('requestTimedOut',4),('unknownDestinationAddress',5),('noRouteToTarget',6),('interfaceInactiveToTarget',7),('arpFailure',8),('maxConcurrentLimitReached',9),('unableToResolveDnsName',10),('invalidHostAddress',11)))
_PingNotifications_ObjectIdentity=ObjectIdentity
pingNotifications=_PingNotifications_ObjectIdentity((1,3,6,1,2,1,80,0))
_PingObjects_ObjectIdentity=ObjectIdentity
pingObjects=_PingObjects_ObjectIdentity((1,3,6,1,2,1,80,1))
class _PingMaxConcurrentRequests_Type(Unsigned32):defaultValue=10
_PingMaxConcurrentRequests_Type.__name__=_E
_PingMaxConcurrentRequests_Object=MibScalar
pingMaxConcurrentRequests=_PingMaxConcurrentRequests_Object((1,3,6,1,2,1,80,1,1),_PingMaxConcurrentRequests_Type())
pingMaxConcurrentRequests.setMaxAccess('read-write')
if mibBuilder.loadTexts:pingMaxConcurrentRequests.setStatus(_B)
if mibBuilder.loadTexts:pingMaxConcurrentRequests.setUnits('requests')
_PingCtlTable_Object=MibTable
pingCtlTable=_PingCtlTable_Object((1,3,6,1,2,1,80,1,2))
if mibBuilder.loadTexts:pingCtlTable.setStatus(_B)
_PingCtlEntry_Object=MibTableRow
pingCtlEntry=_PingCtlEntry_Object((1,3,6,1,2,1,80,1,2,1))
pingCtlEntry.setIndexNames((0,_A,_V),(0,_A,_W))
if mibBuilder.loadTexts:pingCtlEntry.setStatus(_B)
class _PingCtlOwnerIndex_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PingCtlOwnerIndex_Type.__name__=_U
_PingCtlOwnerIndex_Object=MibTableColumn
pingCtlOwnerIndex=_PingCtlOwnerIndex_Object((1,3,6,1,2,1,80,1,2,1,1),_PingCtlOwnerIndex_Type())
pingCtlOwnerIndex.setMaxAccess(_Z)
if mibBuilder.loadTexts:pingCtlOwnerIndex.setStatus(_B)
class _PingCtlTestName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_PingCtlTestName_Type.__name__=_U
_PingCtlTestName_Object=MibTableColumn
pingCtlTestName=_PingCtlTestName_Object((1,3,6,1,2,1,80,1,2,1,2),_PingCtlTestName_Type())
pingCtlTestName.setMaxAccess(_Z)
if mibBuilder.loadTexts:pingCtlTestName.setStatus(_B)
class _PingCtlTargetAddressType_Type(InetAddressType):defaultValue=0
_PingCtlTargetAddressType_Type.__name__=_T
_PingCtlTargetAddressType_Object=MibTableColumn
pingCtlTargetAddressType=_PingCtlTargetAddressType_Object((1,3,6,1,2,1,80,1,2,1,3),_PingCtlTargetAddressType_Type())
pingCtlTargetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlTargetAddressType.setStatus(_B)
class _PingCtlTargetAddress_Type(InetAddress):defaultHexValue=''
_PingCtlTargetAddress_Type.__name__=_S
_PingCtlTargetAddress_Object=MibTableColumn
pingCtlTargetAddress=_PingCtlTargetAddress_Object((1,3,6,1,2,1,80,1,2,1,4),_PingCtlTargetAddress_Type())
pingCtlTargetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlTargetAddress.setStatus(_B)
class _PingCtlDataSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65507))
_PingCtlDataSize_Type.__name__=_E
_PingCtlDataSize_Object=MibTableColumn
pingCtlDataSize=_PingCtlDataSize_Object((1,3,6,1,2,1,80,1,2,1,5),_PingCtlDataSize_Type())
pingCtlDataSize.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlDataSize.setStatus(_B)
if mibBuilder.loadTexts:pingCtlDataSize.setUnits('octets')
class _PingCtlTimeOut_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_PingCtlTimeOut_Type.__name__=_E
_PingCtlTimeOut_Object=MibTableColumn
pingCtlTimeOut=_PingCtlTimeOut_Object((1,3,6,1,2,1,80,1,2,1,6),_PingCtlTimeOut_Type())
pingCtlTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlTimeOut.setStatus(_B)
if mibBuilder.loadTexts:pingCtlTimeOut.setUnits('seconds')
class _PingCtlProbeCount_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_PingCtlProbeCount_Type.__name__=_E
_PingCtlProbeCount_Object=MibTableColumn
pingCtlProbeCount=_PingCtlProbeCount_Object((1,3,6,1,2,1,80,1,2,1,7),_PingCtlProbeCount_Type())
pingCtlProbeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlProbeCount.setStatus(_B)
if mibBuilder.loadTexts:pingCtlProbeCount.setUnits('probes')
class _PingCtlAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_PingCtlAdminStatus_Type.__name__=_Y
_PingCtlAdminStatus_Object=MibTableColumn
pingCtlAdminStatus=_PingCtlAdminStatus_Object((1,3,6,1,2,1,80,1,2,1,8),_PingCtlAdminStatus_Type())
pingCtlAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlAdminStatus.setStatus(_B)
class _PingCtlDataFill_Type(OctetString):defaultHexValue='00';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_PingCtlDataFill_Type.__name__=_A2
_PingCtlDataFill_Object=MibTableColumn
pingCtlDataFill=_PingCtlDataFill_Object((1,3,6,1,2,1,80,1,2,1,9),_PingCtlDataFill_Type())
pingCtlDataFill.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlDataFill.setStatus(_B)
class _PingCtlFrequency_Type(Unsigned32):defaultValue=0
_PingCtlFrequency_Type.__name__=_E
_PingCtlFrequency_Object=MibTableColumn
pingCtlFrequency=_PingCtlFrequency_Object((1,3,6,1,2,1,80,1,2,1,10),_PingCtlFrequency_Type())
pingCtlFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlFrequency.setStatus(_B)
if mibBuilder.loadTexts:pingCtlFrequency.setUnits('seconds')
class _PingCtlMaxRows_Type(Unsigned32):defaultValue=50
_PingCtlMaxRows_Type.__name__=_E
_PingCtlMaxRows_Object=MibTableColumn
pingCtlMaxRows=_PingCtlMaxRows_Object((1,3,6,1,2,1,80,1,2,1,11),_PingCtlMaxRows_Type())
pingCtlMaxRows.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlMaxRows.setStatus(_B)
if mibBuilder.loadTexts:pingCtlMaxRows.setUnits('rows')
class _PingCtlStorageType_Type(StorageType):defaultValue=3
_PingCtlStorageType_Type.__name__=_A5
_PingCtlStorageType_Object=MibTableColumn
pingCtlStorageType=_PingCtlStorageType_Object((1,3,6,1,2,1,80,1,2,1,12),_PingCtlStorageType_Type())
pingCtlStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlStorageType.setStatus(_B)
class _PingCtlTrapGeneration_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('probeFailure',0),('testFailure',1),('testCompletion',2)))
_PingCtlTrapGeneration_Type.__name__='Bits'
_PingCtlTrapGeneration_Object=MibTableColumn
pingCtlTrapGeneration=_PingCtlTrapGeneration_Object((1,3,6,1,2,1,80,1,2,1,13),_PingCtlTrapGeneration_Type())
pingCtlTrapGeneration.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlTrapGeneration.setStatus(_B)
class _PingCtlTrapProbeFailureFilter_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_PingCtlTrapProbeFailureFilter_Type.__name__=_E
_PingCtlTrapProbeFailureFilter_Object=MibTableColumn
pingCtlTrapProbeFailureFilter=_PingCtlTrapProbeFailureFilter_Object((1,3,6,1,2,1,80,1,2,1,14),_PingCtlTrapProbeFailureFilter_Type())
pingCtlTrapProbeFailureFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlTrapProbeFailureFilter.setStatus(_B)
class _PingCtlTrapTestFailureFilter_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_PingCtlTrapTestFailureFilter_Type.__name__=_E
_PingCtlTrapTestFailureFilter_Object=MibTableColumn
pingCtlTrapTestFailureFilter=_PingCtlTrapTestFailureFilter_Object((1,3,6,1,2,1,80,1,2,1,15),_PingCtlTrapTestFailureFilter_Type())
pingCtlTrapTestFailureFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlTrapTestFailureFilter.setStatus(_B)
class _PingCtlType_Type(ObjectIdentifier):defaultValue=1,3,6,1,2,1,80,3,1
_PingCtlType_Type.__name__=_A3
_PingCtlType_Object=MibTableColumn
pingCtlType=_PingCtlType_Object((1,3,6,1,2,1,80,1,2,1,16),_PingCtlType_Type())
pingCtlType.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlType.setStatus(_B)
class _PingCtlDescr_Type(SnmpAdminString):defaultHexValue=''
_PingCtlDescr_Type.__name__=_U
_PingCtlDescr_Object=MibTableColumn
pingCtlDescr=_PingCtlDescr_Object((1,3,6,1,2,1,80,1,2,1,17),_PingCtlDescr_Type())
pingCtlDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlDescr.setStatus(_B)
class _PingCtlSourceAddressType_Type(InetAddressType):defaultValue=0
_PingCtlSourceAddressType_Type.__name__=_T
_PingCtlSourceAddressType_Object=MibTableColumn
pingCtlSourceAddressType=_PingCtlSourceAddressType_Object((1,3,6,1,2,1,80,1,2,1,18),_PingCtlSourceAddressType_Type())
pingCtlSourceAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlSourceAddressType.setStatus(_B)
class _PingCtlSourceAddress_Type(InetAddress):defaultHexValue=''
_PingCtlSourceAddress_Type.__name__=_S
_PingCtlSourceAddress_Object=MibTableColumn
pingCtlSourceAddress=_PingCtlSourceAddress_Object((1,3,6,1,2,1,80,1,2,1,19),_PingCtlSourceAddress_Type())
pingCtlSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlSourceAddress.setStatus(_B)
class _PingCtlIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_PingCtlIfIndex_Type.__name__=_A4
_PingCtlIfIndex_Object=MibTableColumn
pingCtlIfIndex=_PingCtlIfIndex_Object((1,3,6,1,2,1,80,1,2,1,20),_PingCtlIfIndex_Type())
pingCtlIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlIfIndex.setStatus(_B)
class _PingCtlByPassRouteTable_Type(TruthValue):defaultValue=2
_PingCtlByPassRouteTable_Type.__name__=_A6
_PingCtlByPassRouteTable_Object=MibTableColumn
pingCtlByPassRouteTable=_PingCtlByPassRouteTable_Object((1,3,6,1,2,1,80,1,2,1,21),_PingCtlByPassRouteTable_Type())
pingCtlByPassRouteTable.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlByPassRouteTable.setStatus(_B)
class _PingCtlDSField_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PingCtlDSField_Type.__name__=_E
_PingCtlDSField_Object=MibTableColumn
pingCtlDSField=_PingCtlDSField_Object((1,3,6,1,2,1,80,1,2,1,22),_PingCtlDSField_Type())
pingCtlDSField.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlDSField.setStatus(_B)
_PingCtlRowStatus_Type=RowStatus
_PingCtlRowStatus_Object=MibTableColumn
pingCtlRowStatus=_PingCtlRowStatus_Object((1,3,6,1,2,1,80,1,2,1,23),_PingCtlRowStatus_Type())
pingCtlRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pingCtlRowStatus.setStatus(_B)
_PingResultsTable_Object=MibTable
pingResultsTable=_PingResultsTable_Object((1,3,6,1,2,1,80,1,3))
if mibBuilder.loadTexts:pingResultsTable.setStatus(_B)
_PingResultsEntry_Object=MibTableRow
pingResultsEntry=_PingResultsEntry_Object((1,3,6,1,2,1,80,1,3,1))
pingResultsEntry.setIndexNames((0,_A,_V),(0,_A,_W))
if mibBuilder.loadTexts:pingResultsEntry.setStatus(_B)
class _PingResultsOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),('disabled',2),('completed',3)))
_PingResultsOperStatus_Type.__name__=_Y
_PingResultsOperStatus_Object=MibTableColumn
pingResultsOperStatus=_PingResultsOperStatus_Object((1,3,6,1,2,1,80,1,3,1,1),_PingResultsOperStatus_Type())
pingResultsOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pingResultsOperStatus.setStatus(_B)
class _PingResultsIpTargetAddressType_Type(InetAddressType):defaultValue=0
_PingResultsIpTargetAddressType_Type.__name__=_T
_PingResultsIpTargetAddressType_Object=MibTableColumn
pingResultsIpTargetAddressType=_PingResultsIpTargetAddressType_Object((1,3,6,1,2,1,80,1,3,1,2),_PingResultsIpTargetAddressType_Type())
pingResultsIpTargetAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:pingResultsIpTargetAddressType.setStatus(_B)
class _PingResultsIpTargetAddress_Type(InetAddress):defaultHexValue=''
_PingResultsIpTargetAddress_Type.__name__=_S
_PingResultsIpTargetAddress_Object=MibTableColumn
pingResultsIpTargetAddress=_PingResultsIpTargetAddress_Object((1,3,6,1,2,1,80,1,3,1,3),_PingResultsIpTargetAddress_Type())
pingResultsIpTargetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:pingResultsIpTargetAddress.setStatus(_B)
_PingResultsMinRtt_Type=Unsigned32
_PingResultsMinRtt_Object=MibTableColumn
pingResultsMinRtt=_PingResultsMinRtt_Object((1,3,6,1,2,1,80,1,3,1,4),_PingResultsMinRtt_Type())
pingResultsMinRtt.setMaxAccess(_D)
if mibBuilder.loadTexts:pingResultsMinRtt.setStatus(_B)
if mibBuilder.loadTexts:pingResultsMinRtt.setUnits(_R)
_PingResultsMaxRtt_Type=Unsigned32
_PingResultsMaxRtt_Object=MibTableColumn
pingResultsMaxRtt=_PingResultsMaxRtt_Object((1,3,6,1,2,1,80,1,3,1,5),_PingResultsMaxRtt_Type())
pingResultsMaxRtt.setMaxAccess(_D)
if mibBuilder.loadTexts:pingResultsMaxRtt.setStatus(_B)
if mibBuilder.loadTexts:pingResultsMaxRtt.setUnits(_R)
_PingResultsAverageRtt_Type=Unsigned32
_PingResultsAverageRtt_Object=MibTableColumn
pingResultsAverageRtt=_PingResultsAverageRtt_Object((1,3,6,1,2,1,80,1,3,1,6),_PingResultsAverageRtt_Type())
pingResultsAverageRtt.setMaxAccess(_D)
if mibBuilder.loadTexts:pingResultsAverageRtt.setStatus(_B)
if mibBuilder.loadTexts:pingResultsAverageRtt.setUnits(_R)
_PingResultsProbeResponses_Type=Gauge32
_PingResultsProbeResponses_Object=MibTableColumn
pingResultsProbeResponses=_PingResultsProbeResponses_Object((1,3,6,1,2,1,80,1,3,1,7),_PingResultsProbeResponses_Type())
pingResultsProbeResponses.setMaxAccess(_D)
if mibBuilder.loadTexts:pingResultsProbeResponses.setStatus(_B)
if mibBuilder.loadTexts:pingResultsProbeResponses.setUnits('responses')
_PingResultsSentProbes_Type=Gauge32
_PingResultsSentProbes_Object=MibTableColumn
pingResultsSentProbes=_PingResultsSentProbes_Object((1,3,6,1,2,1,80,1,3,1,8),_PingResultsSentProbes_Type())
pingResultsSentProbes.setMaxAccess(_D)
if mibBuilder.loadTexts:pingResultsSentProbes.setStatus(_B)
if mibBuilder.loadTexts:pingResultsSentProbes.setUnits('probes')
_PingResultsRttSumOfSquares_Type=Unsigned32
_PingResultsRttSumOfSquares_Object=MibTableColumn
pingResultsRttSumOfSquares=_PingResultsRttSumOfSquares_Object((1,3,6,1,2,1,80,1,3,1,9),_PingResultsRttSumOfSquares_Type())
pingResultsRttSumOfSquares.setMaxAccess(_D)
if mibBuilder.loadTexts:pingResultsRttSumOfSquares.setStatus(_B)
if mibBuilder.loadTexts:pingResultsRttSumOfSquares.setUnits(_R)
_PingResultsLastGoodProbe_Type=DateAndTime
_PingResultsLastGoodProbe_Object=MibTableColumn
pingResultsLastGoodProbe=_PingResultsLastGoodProbe_Object((1,3,6,1,2,1,80,1,3,1,10),_PingResultsLastGoodProbe_Type())
pingResultsLastGoodProbe.setMaxAccess(_D)
if mibBuilder.loadTexts:pingResultsLastGoodProbe.setStatus(_B)
_PingProbeHistoryTable_Object=MibTable
pingProbeHistoryTable=_PingProbeHistoryTable_Object((1,3,6,1,2,1,80,1,4))
if mibBuilder.loadTexts:pingProbeHistoryTable.setStatus(_B)
_PingProbeHistoryEntry_Object=MibTableRow
pingProbeHistoryEntry=_PingProbeHistoryEntry_Object((1,3,6,1,2,1,80,1,4,1))
pingProbeHistoryEntry.setIndexNames((0,_A,_V),(0,_A,_W),(0,_A,_A7))
if mibBuilder.loadTexts:pingProbeHistoryEntry.setStatus(_B)
class _PingProbeHistoryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_PingProbeHistoryIndex_Type.__name__=_E
_PingProbeHistoryIndex_Object=MibTableColumn
pingProbeHistoryIndex=_PingProbeHistoryIndex_Object((1,3,6,1,2,1,80,1,4,1,1),_PingProbeHistoryIndex_Type())
pingProbeHistoryIndex.setMaxAccess(_Z)
if mibBuilder.loadTexts:pingProbeHistoryIndex.setStatus(_B)
_PingProbeHistoryResponse_Type=Unsigned32
_PingProbeHistoryResponse_Object=MibTableColumn
pingProbeHistoryResponse=_PingProbeHistoryResponse_Object((1,3,6,1,2,1,80,1,4,1,2),_PingProbeHistoryResponse_Type())
pingProbeHistoryResponse.setMaxAccess(_D)
if mibBuilder.loadTexts:pingProbeHistoryResponse.setStatus(_B)
if mibBuilder.loadTexts:pingProbeHistoryResponse.setUnits(_R)
_PingProbeHistoryStatus_Type=OperationResponseStatus
_PingProbeHistoryStatus_Object=MibTableColumn
pingProbeHistoryStatus=_PingProbeHistoryStatus_Object((1,3,6,1,2,1,80,1,4,1,3),_PingProbeHistoryStatus_Type())
pingProbeHistoryStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pingProbeHistoryStatus.setStatus(_B)
_PingProbeHistoryLastRC_Type=Integer32
_PingProbeHistoryLastRC_Object=MibTableColumn
pingProbeHistoryLastRC=_PingProbeHistoryLastRC_Object((1,3,6,1,2,1,80,1,4,1,4),_PingProbeHistoryLastRC_Type())
pingProbeHistoryLastRC.setMaxAccess(_D)
if mibBuilder.loadTexts:pingProbeHistoryLastRC.setStatus(_B)
_PingProbeHistoryTime_Type=DateAndTime
_PingProbeHistoryTime_Object=MibTableColumn
pingProbeHistoryTime=_PingProbeHistoryTime_Object((1,3,6,1,2,1,80,1,4,1,5),_PingProbeHistoryTime_Type())
pingProbeHistoryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:pingProbeHistoryTime.setStatus(_B)
_PingConformance_ObjectIdentity=ObjectIdentity
pingConformance=_PingConformance_ObjectIdentity((1,3,6,1,2,1,80,2))
_PingCompliances_ObjectIdentity=ObjectIdentity
pingCompliances=_PingCompliances_ObjectIdentity((1,3,6,1,2,1,80,2,1))
_PingGroups_ObjectIdentity=ObjectIdentity
pingGroups=_PingGroups_ObjectIdentity((1,3,6,1,2,1,80,2,2))
_PingImplementationTypeDomains_ObjectIdentity=ObjectIdentity
pingImplementationTypeDomains=_PingImplementationTypeDomains_ObjectIdentity((1,3,6,1,2,1,80,3))
_PingIcmpEcho_ObjectIdentity=ObjectIdentity
pingIcmpEcho=_PingIcmpEcho_ObjectIdentity((1,3,6,1,2,1,80,3,1))
if mibBuilder.loadTexts:pingIcmpEcho.setStatus(_B)
_PingUdpEcho_ObjectIdentity=ObjectIdentity
pingUdpEcho=_PingUdpEcho_ObjectIdentity((1,3,6,1,2,1,80,3,2))
if mibBuilder.loadTexts:pingUdpEcho.setStatus(_B)
_PingSnmpQuery_ObjectIdentity=ObjectIdentity
pingSnmpQuery=_PingSnmpQuery_ObjectIdentity((1,3,6,1,2,1,80,3,3))
if mibBuilder.loadTexts:pingSnmpQuery.setStatus(_B)
_PingTcpConnectionAttempt_ObjectIdentity=ObjectIdentity
pingTcpConnectionAttempt=_PingTcpConnectionAttempt_ObjectIdentity((1,3,6,1,2,1,80,3,4))
if mibBuilder.loadTexts:pingTcpConnectionAttempt.setStatus(_B)
pingGroup=ObjectGroup((1,3,6,1,2,1,80,2,2,1))
pingGroup.setObjects(*((_A,_a),(_A,_F),(_A,_G),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:pingGroup.setStatus(_x)
pingTimeStampGroup=ObjectGroup((1,3,6,1,2,1,80,2,2,2))
pingTimeStampGroup.setObjects(*((_A,_Q),(_A,_y)))
if mibBuilder.loadTexts:pingTimeStampGroup.setStatus(_x)
pingMinimumGroup=ObjectGroup((1,3,6,1,2,1,80,2,2,4))
pingMinimumGroup.setObjects(*((_A,_a),(_A,_F),(_A,_G),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:pingMinimumGroup.setStatus(_B)
pingCtlRowStatusGroup=ObjectGroup((1,3,6,1,2,1,80,2,2,5))
pingCtlRowStatusGroup.setObjects((_A,_t))
if mibBuilder.loadTexts:pingCtlRowStatusGroup.setStatus(_B)
pingHistoryGroup=ObjectGroup((1,3,6,1,2,1,80,2,2,6))
pingHistoryGroup.setObjects(*((_A,_u),(_A,_v),(_A,_w),(_A,_y)))
if mibBuilder.loadTexts:pingHistoryGroup.setStatus(_B)
pingProbeFailed=NotificationType((1,3,6,1,2,1,80,0,1))
pingProbeFailed.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:pingProbeFailed.setStatus(_B)
pingTestFailed=NotificationType((1,3,6,1,2,1,80,0,2))
pingTestFailed.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:pingTestFailed.setStatus(_B)
pingTestCompleted=NotificationType((1,3,6,1,2,1,80,0,3))
pingTestCompleted.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:pingTestCompleted.setStatus(_B)
pingNotificationsGroup=NotificationGroup((1,3,6,1,2,1,80,2,2,3))
pingNotificationsGroup.setObjects(*((_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:pingNotificationsGroup.setStatus(_B)
pingCompliance=ModuleCompliance((1,3,6,1,2,1,80,2,1,1))
pingCompliance.setObjects(*((_A,_AB),(_A,_X),(_A,_AC)))
if mibBuilder.loadTexts:pingCompliance.setStatus(_x)
pingFullCompliance=ModuleCompliance((1,3,6,1,2,1,80,2,1,2))
pingFullCompliance.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_X)))
if mibBuilder.loadTexts:pingFullCompliance.setStatus(_B)
pingMinimumCompliance=ModuleCompliance((1,3,6,1,2,1,80,2,1,3))
pingMinimumCompliance.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_X)))
if mibBuilder.loadTexts:pingMinimumCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'OperationResponseStatus':OperationResponseStatus,'pingMIB':pingMIB,'pingNotifications':pingNotifications,_A8:pingProbeFailed,_A9:pingTestFailed,_AA:pingTestCompleted,'pingObjects':pingObjects,_a:pingMaxConcurrentRequests,'pingCtlTable':pingCtlTable,'pingCtlEntry':pingCtlEntry,_V:pingCtlOwnerIndex,_W:pingCtlTestName,_F:pingCtlTargetAddressType,_G:pingCtlTargetAddress,_b:pingCtlDataSize,_c:pingCtlTimeOut,_d:pingCtlProbeCount,_e:pingCtlAdminStatus,_f:pingCtlDataFill,_g:pingCtlFrequency,_h:pingCtlMaxRows,_i:pingCtlStorageType,_j:pingCtlTrapGeneration,_k:pingCtlTrapProbeFailureFilter,_l:pingCtlTrapTestFailureFilter,_m:pingCtlType,_n:pingCtlDescr,_p:pingCtlSourceAddressType,_q:pingCtlSourceAddress,_r:pingCtlIfIndex,_o:pingCtlByPassRouteTable,_s:pingCtlDSField,_t:pingCtlRowStatus,'pingResultsTable':pingResultsTable,'pingResultsEntry':pingResultsEntry,_H:pingResultsOperStatus,_I:pingResultsIpTargetAddressType,_J:pingResultsIpTargetAddress,_K:pingResultsMinRtt,_L:pingResultsMaxRtt,_M:pingResultsAverageRtt,_N:pingResultsProbeResponses,_O:pingResultsSentProbes,_P:pingResultsRttSumOfSquares,_Q:pingResultsLastGoodProbe,'pingProbeHistoryTable':pingProbeHistoryTable,'pingProbeHistoryEntry':pingProbeHistoryEntry,_A7:pingProbeHistoryIndex,_u:pingProbeHistoryResponse,_v:pingProbeHistoryStatus,_w:pingProbeHistoryLastRC,_y:pingProbeHistoryTime,'pingConformance':pingConformance,'pingCompliances':pingCompliances,'pingCompliance':pingCompliance,'pingFullCompliance':pingFullCompliance,'pingMinimumCompliance':pingMinimumCompliance,'pingGroups':pingGroups,_AB:pingGroup,_AC:pingTimeStampGroup,_X:pingNotificationsGroup,_z:pingMinimumGroup,_A0:pingCtlRowStatusGroup,_A1:pingHistoryGroup,'pingImplementationTypeDomains':pingImplementationTypeDomains,'pingIcmpEcho':pingIcmpEcho,'pingUdpEcho':pingUdpEcho,'pingSnmpQuery':pingSnmpQuery,'pingTcpConnectionAttempt':pingTcpConnectionAttempt})