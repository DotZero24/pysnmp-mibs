_A1='zhonePingTestCompleted'
_A0='zhonePingResultsLastGoodProbe'
_z='zhonePingResultsRttSumOfSquares'
_y='zhonePingResultsIpTargetAddressType'
_x='zhonePingResultsOperStatus'
_w='zhonePingCtlRowStatus'
_v='zhonePingCtlDSField'
_u='zhonePingCtlIfIndex'
_t='zhonePingCtlSourceAddress'
_s='zhonePingCtlSourceAddressType'
_r='zhonePingCtlByPassRouteTable'
_q='zhonePingCtlDescr'
_p='zhonePingCtlType'
_o='zhonePingCtlTrapTestFailureFilter'
_n='zhonePingCtlTrapProbeFailureFilter'
_m='zhonePingCtlTrapGeneration'
_l='zhonePingCtlStorageType'
_k='zhonePingCtlMaxRows'
_j='zhonePingCtlFrequency'
_i='zhonePingCtlDataFill'
_h='zhonePingCtlAdminStatus'
_g='zhonePingCtlProbeCount'
_f='zhonePingCtlTimeOut'
_e='zhonePingCtlDataSize'
_d='zhonePingCtlTargetAddress'
_c='zhonePingCtlTargetAddressType'
_b='zhonePingMaxConcurrentRequests'
_a='disabled'
_Z='enabled'
_Y='probes'
_X='seconds'
_W='TruthValue'
_V='StorageType'
_U='SnmpAdminString'
_T='InterfaceIndexOrZero'
_S='ObjectIdentifier'
_R='OctetString'
_Q='zhonePingResultsSentProbes'
_P='zhonePingResultsProbeResponses'
_O='zhonePingResultsAverageRtt'
_N='zhonePingResultsMaxRtt'
_M='zhonePingResultsMinRtt'
_L='zhonePingResultsIpTargetAddress'
_K='zhonePingCtlIndex'
_J='milliseconds'
_I='InetAddressType'
_H='InetAddress'
_G='00'
_F='Integer32'
_E='Unsigned32'
_D='read-only'
_C='read-create'
_B='ZHONE-DISMAN-PING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_R,_S)
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_T)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_H,_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_U)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso','mib-2')
DateAndTime,DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus',_V,'TextualConvention',_W)
zhoneIp,=mibBuilder.importSymbols('Zhone','zhoneIp')
zhonePingMIB=ModuleIdentity((1,3,6,1,4,1,5504,4,1,19))
if mibBuilder.loadTexts:zhonePingMIB.setRevisions(('2003-01-27 00:00',))
class OperationResponseStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('responseReceived',1),('unknown',2),('internalError',3),('requestTimedOut',4),('unknownDestinationAddress',5),('noRouteToTarget',6),('interfaceInactiveToTarget',7),('arpFailure',8),('maxConcurrentLimitReached',9),('unableToResolveDnsName',10),('invalidHostAddress',11)))
_ZhonePingNotifications_ObjectIdentity=ObjectIdentity
zhonePingNotifications=_ZhonePingNotifications_ObjectIdentity((1,3,6,1,4,1,5504,4,1,19,0))
_ZhonePingObjects_ObjectIdentity=ObjectIdentity
zhonePingObjects=_ZhonePingObjects_ObjectIdentity((1,3,6,1,4,1,5504,4,1,19,1))
class _ZhonePingMaxConcurrentRequests_Type(Unsigned32):defaultValue=10
_ZhonePingMaxConcurrentRequests_Type.__name__=_E
_ZhonePingMaxConcurrentRequests_Object=MibScalar
zhonePingMaxConcurrentRequests=_ZhonePingMaxConcurrentRequests_Object((1,3,6,1,4,1,5504,4,1,19,1,1),_ZhonePingMaxConcurrentRequests_Type())
zhonePingMaxConcurrentRequests.setMaxAccess('read-write')
if mibBuilder.loadTexts:zhonePingMaxConcurrentRequests.setStatus(_A)
if mibBuilder.loadTexts:zhonePingMaxConcurrentRequests.setUnits('requests')
class _ZhonePingCtlIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZhonePingCtlIndexNext_Type.__name__=_F
_ZhonePingCtlIndexNext_Object=MibScalar
zhonePingCtlIndexNext=_ZhonePingCtlIndexNext_Object((1,3,6,1,4,1,5504,4,1,19,1,2),_ZhonePingCtlIndexNext_Type())
zhonePingCtlIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:zhonePingCtlIndexNext.setStatus(_A)
_ZhonePingCtlTable_Object=MibTable
zhonePingCtlTable=_ZhonePingCtlTable_Object((1,3,6,1,4,1,5504,4,1,19,1,3))
if mibBuilder.loadTexts:zhonePingCtlTable.setStatus(_A)
_ZhonePingCtlEntry_Object=MibTableRow
zhonePingCtlEntry=_ZhonePingCtlEntry_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1))
zhonePingCtlEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:zhonePingCtlEntry.setStatus(_A)
class _ZhonePingCtlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZhonePingCtlIndex_Type.__name__=_F
_ZhonePingCtlIndex_Object=MibTableColumn
zhonePingCtlIndex=_ZhonePingCtlIndex_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,1),_ZhonePingCtlIndex_Type())
zhonePingCtlIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:zhonePingCtlIndex.setStatus(_A)
class _ZhonePingCtlTargetAddressType_Type(InetAddressType):defaultValue=0
_ZhonePingCtlTargetAddressType_Type.__name__=_I
_ZhonePingCtlTargetAddressType_Object=MibTableColumn
zhonePingCtlTargetAddressType=_ZhonePingCtlTargetAddressType_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,2),_ZhonePingCtlTargetAddressType_Type())
zhonePingCtlTargetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlTargetAddressType.setStatus(_A)
class _ZhonePingCtlTargetAddress_Type(InetAddress):defaultHexValue=_G
_ZhonePingCtlTargetAddress_Type.__name__=_H
_ZhonePingCtlTargetAddress_Object=MibTableColumn
zhonePingCtlTargetAddress=_ZhonePingCtlTargetAddress_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,3),_ZhonePingCtlTargetAddress_Type())
zhonePingCtlTargetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlTargetAddress.setStatus(_A)
class _ZhonePingCtlDataSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65507))
_ZhonePingCtlDataSize_Type.__name__=_E
_ZhonePingCtlDataSize_Object=MibTableColumn
zhonePingCtlDataSize=_ZhonePingCtlDataSize_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,4),_ZhonePingCtlDataSize_Type())
zhonePingCtlDataSize.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlDataSize.setStatus(_A)
if mibBuilder.loadTexts:zhonePingCtlDataSize.setUnits('octets')
class _ZhonePingCtlTimeOut_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_ZhonePingCtlTimeOut_Type.__name__=_E
_ZhonePingCtlTimeOut_Object=MibTableColumn
zhonePingCtlTimeOut=_ZhonePingCtlTimeOut_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,5),_ZhonePingCtlTimeOut_Type())
zhonePingCtlTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlTimeOut.setStatus(_A)
if mibBuilder.loadTexts:zhonePingCtlTimeOut.setUnits(_X)
class _ZhonePingCtlProbeCount_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_ZhonePingCtlProbeCount_Type.__name__=_E
_ZhonePingCtlProbeCount_Object=MibTableColumn
zhonePingCtlProbeCount=_ZhonePingCtlProbeCount_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,6),_ZhonePingCtlProbeCount_Type())
zhonePingCtlProbeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlProbeCount.setStatus(_A)
if mibBuilder.loadTexts:zhonePingCtlProbeCount.setUnits(_Y)
class _ZhonePingCtlAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_ZhonePingCtlAdminStatus_Type.__name__=_F
_ZhonePingCtlAdminStatus_Object=MibTableColumn
zhonePingCtlAdminStatus=_ZhonePingCtlAdminStatus_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,7),_ZhonePingCtlAdminStatus_Type())
zhonePingCtlAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlAdminStatus.setStatus(_A)
class _ZhonePingCtlDataFill_Type(OctetString):defaultHexValue=_G;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_ZhonePingCtlDataFill_Type.__name__=_R
_ZhonePingCtlDataFill_Object=MibTableColumn
zhonePingCtlDataFill=_ZhonePingCtlDataFill_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,8),_ZhonePingCtlDataFill_Type())
zhonePingCtlDataFill.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlDataFill.setStatus(_A)
class _ZhonePingCtlFrequency_Type(Unsigned32):defaultValue=0
_ZhonePingCtlFrequency_Type.__name__=_E
_ZhonePingCtlFrequency_Object=MibTableColumn
zhonePingCtlFrequency=_ZhonePingCtlFrequency_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,9),_ZhonePingCtlFrequency_Type())
zhonePingCtlFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlFrequency.setStatus(_A)
if mibBuilder.loadTexts:zhonePingCtlFrequency.setUnits(_X)
class _ZhonePingCtlMaxRows_Type(Unsigned32):defaultValue=50
_ZhonePingCtlMaxRows_Type.__name__=_E
_ZhonePingCtlMaxRows_Object=MibTableColumn
zhonePingCtlMaxRows=_ZhonePingCtlMaxRows_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,10),_ZhonePingCtlMaxRows_Type())
zhonePingCtlMaxRows.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlMaxRows.setStatus(_A)
if mibBuilder.loadTexts:zhonePingCtlMaxRows.setUnits('rows')
class _ZhonePingCtlStorageType_Type(StorageType):defaultValue=3
_ZhonePingCtlStorageType_Type.__name__=_V
_ZhonePingCtlStorageType_Object=MibTableColumn
zhonePingCtlStorageType=_ZhonePingCtlStorageType_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,11),_ZhonePingCtlStorageType_Type())
zhonePingCtlStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlStorageType.setStatus(_A)
class _ZhonePingCtlTrapGeneration_Type(Bits):namedValues=NamedValues(*(('probeFailure',0),('testFailure',1),('testCompletion',2)))
_ZhonePingCtlTrapGeneration_Type.__name__='Bits'
_ZhonePingCtlTrapGeneration_Object=MibTableColumn
zhonePingCtlTrapGeneration=_ZhonePingCtlTrapGeneration_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,12),_ZhonePingCtlTrapGeneration_Type())
zhonePingCtlTrapGeneration.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlTrapGeneration.setStatus(_A)
class _ZhonePingCtlTrapProbeFailureFilter_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_ZhonePingCtlTrapProbeFailureFilter_Type.__name__=_E
_ZhonePingCtlTrapProbeFailureFilter_Object=MibTableColumn
zhonePingCtlTrapProbeFailureFilter=_ZhonePingCtlTrapProbeFailureFilter_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,13),_ZhonePingCtlTrapProbeFailureFilter_Type())
zhonePingCtlTrapProbeFailureFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlTrapProbeFailureFilter.setStatus(_A)
class _ZhonePingCtlTrapTestFailureFilter_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_ZhonePingCtlTrapTestFailureFilter_Type.__name__=_E
_ZhonePingCtlTrapTestFailureFilter_Object=MibTableColumn
zhonePingCtlTrapTestFailureFilter=_ZhonePingCtlTrapTestFailureFilter_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,14),_ZhonePingCtlTrapTestFailureFilter_Type())
zhonePingCtlTrapTestFailureFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlTrapTestFailureFilter.setStatus(_A)
class _ZhonePingCtlType_Type(ObjectIdentifier):defaultValue=1,3,6,1,4,1,5504,4,1,19,3,1
_ZhonePingCtlType_Type.__name__=_S
_ZhonePingCtlType_Object=MibTableColumn
zhonePingCtlType=_ZhonePingCtlType_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,15),_ZhonePingCtlType_Type())
zhonePingCtlType.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlType.setStatus(_A)
class _ZhonePingCtlDescr_Type(SnmpAdminString):defaultHexValue=_G
_ZhonePingCtlDescr_Type.__name__=_U
_ZhonePingCtlDescr_Object=MibTableColumn
zhonePingCtlDescr=_ZhonePingCtlDescr_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,16),_ZhonePingCtlDescr_Type())
zhonePingCtlDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlDescr.setStatus(_A)
class _ZhonePingCtlSourceAddressType_Type(InetAddressType):defaultValue=1
_ZhonePingCtlSourceAddressType_Type.__name__=_I
_ZhonePingCtlSourceAddressType_Object=MibTableColumn
zhonePingCtlSourceAddressType=_ZhonePingCtlSourceAddressType_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,17),_ZhonePingCtlSourceAddressType_Type())
zhonePingCtlSourceAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlSourceAddressType.setStatus(_A)
class _ZhonePingCtlSourceAddress_Type(InetAddress):defaultHexValue=_G
_ZhonePingCtlSourceAddress_Type.__name__=_H
_ZhonePingCtlSourceAddress_Object=MibTableColumn
zhonePingCtlSourceAddress=_ZhonePingCtlSourceAddress_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,18),_ZhonePingCtlSourceAddress_Type())
zhonePingCtlSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlSourceAddress.setStatus(_A)
class _ZhonePingCtlIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_ZhonePingCtlIfIndex_Type.__name__=_T
_ZhonePingCtlIfIndex_Object=MibTableColumn
zhonePingCtlIfIndex=_ZhonePingCtlIfIndex_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,19),_ZhonePingCtlIfIndex_Type())
zhonePingCtlIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlIfIndex.setStatus(_A)
class _ZhonePingCtlByPassRouteTable_Type(TruthValue):defaultValue=2
_ZhonePingCtlByPassRouteTable_Type.__name__=_W
_ZhonePingCtlByPassRouteTable_Object=MibTableColumn
zhonePingCtlByPassRouteTable=_ZhonePingCtlByPassRouteTable_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,20),_ZhonePingCtlByPassRouteTable_Type())
zhonePingCtlByPassRouteTable.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlByPassRouteTable.setStatus(_A)
class _ZhonePingCtlDSField_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZhonePingCtlDSField_Type.__name__=_E
_ZhonePingCtlDSField_Object=MibTableColumn
zhonePingCtlDSField=_ZhonePingCtlDSField_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,21),_ZhonePingCtlDSField_Type())
zhonePingCtlDSField.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlDSField.setStatus(_A)
_ZhonePingCtlRowStatus_Type=RowStatus
_ZhonePingCtlRowStatus_Object=MibTableColumn
zhonePingCtlRowStatus=_ZhonePingCtlRowStatus_Object((1,3,6,1,4,1,5504,4,1,19,1,3,1,22),_ZhonePingCtlRowStatus_Type())
zhonePingCtlRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zhonePingCtlRowStatus.setStatus(_A)
_ZhonePingResultsTable_Object=MibTable
zhonePingResultsTable=_ZhonePingResultsTable_Object((1,3,6,1,4,1,5504,4,1,19,1,4))
if mibBuilder.loadTexts:zhonePingResultsTable.setStatus(_A)
_ZhonePingResultsEntry_Object=MibTableRow
zhonePingResultsEntry=_ZhonePingResultsEntry_Object((1,3,6,1,4,1,5504,4,1,19,1,4,1))
zhonePingResultsEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:zhonePingResultsEntry.setStatus(_A)
class _ZhonePingResultsOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),(_a,2)))
_ZhonePingResultsOperStatus_Type.__name__=_F
_ZhonePingResultsOperStatus_Object=MibTableColumn
zhonePingResultsOperStatus=_ZhonePingResultsOperStatus_Object((1,3,6,1,4,1,5504,4,1,19,1,4,1,1),_ZhonePingResultsOperStatus_Type())
zhonePingResultsOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zhonePingResultsOperStatus.setStatus(_A)
class _ZhonePingResultsIpTargetAddressType_Type(InetAddressType):defaultValue=0
_ZhonePingResultsIpTargetAddressType_Type.__name__=_I
_ZhonePingResultsIpTargetAddressType_Object=MibTableColumn
zhonePingResultsIpTargetAddressType=_ZhonePingResultsIpTargetAddressType_Object((1,3,6,1,4,1,5504,4,1,19,1,4,1,2),_ZhonePingResultsIpTargetAddressType_Type())
zhonePingResultsIpTargetAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:zhonePingResultsIpTargetAddressType.setStatus(_A)
class _ZhonePingResultsIpTargetAddress_Type(InetAddress):defaultHexValue=_G
_ZhonePingResultsIpTargetAddress_Type.__name__=_H
_ZhonePingResultsIpTargetAddress_Object=MibTableColumn
zhonePingResultsIpTargetAddress=_ZhonePingResultsIpTargetAddress_Object((1,3,6,1,4,1,5504,4,1,19,1,4,1,3),_ZhonePingResultsIpTargetAddress_Type())
zhonePingResultsIpTargetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:zhonePingResultsIpTargetAddress.setStatus(_A)
_ZhonePingResultsMinRtt_Type=Unsigned32
_ZhonePingResultsMinRtt_Object=MibTableColumn
zhonePingResultsMinRtt=_ZhonePingResultsMinRtt_Object((1,3,6,1,4,1,5504,4,1,19,1,4,1,4),_ZhonePingResultsMinRtt_Type())
zhonePingResultsMinRtt.setMaxAccess(_D)
if mibBuilder.loadTexts:zhonePingResultsMinRtt.setStatus(_A)
if mibBuilder.loadTexts:zhonePingResultsMinRtt.setUnits(_J)
_ZhonePingResultsMaxRtt_Type=Unsigned32
_ZhonePingResultsMaxRtt_Object=MibTableColumn
zhonePingResultsMaxRtt=_ZhonePingResultsMaxRtt_Object((1,3,6,1,4,1,5504,4,1,19,1,4,1,5),_ZhonePingResultsMaxRtt_Type())
zhonePingResultsMaxRtt.setMaxAccess(_D)
if mibBuilder.loadTexts:zhonePingResultsMaxRtt.setStatus(_A)
if mibBuilder.loadTexts:zhonePingResultsMaxRtt.setUnits(_J)
_ZhonePingResultsAverageRtt_Type=Unsigned32
_ZhonePingResultsAverageRtt_Object=MibTableColumn
zhonePingResultsAverageRtt=_ZhonePingResultsAverageRtt_Object((1,3,6,1,4,1,5504,4,1,19,1,4,1,6),_ZhonePingResultsAverageRtt_Type())
zhonePingResultsAverageRtt.setMaxAccess(_D)
if mibBuilder.loadTexts:zhonePingResultsAverageRtt.setStatus(_A)
if mibBuilder.loadTexts:zhonePingResultsAverageRtt.setUnits(_J)
_ZhonePingResultsProbeResponses_Type=Unsigned32
_ZhonePingResultsProbeResponses_Object=MibTableColumn
zhonePingResultsProbeResponses=_ZhonePingResultsProbeResponses_Object((1,3,6,1,4,1,5504,4,1,19,1,4,1,7),_ZhonePingResultsProbeResponses_Type())
zhonePingResultsProbeResponses.setMaxAccess(_D)
if mibBuilder.loadTexts:zhonePingResultsProbeResponses.setStatus(_A)
if mibBuilder.loadTexts:zhonePingResultsProbeResponses.setUnits('responses')
_ZhonePingResultsSentProbes_Type=Unsigned32
_ZhonePingResultsSentProbes_Object=MibTableColumn
zhonePingResultsSentProbes=_ZhonePingResultsSentProbes_Object((1,3,6,1,4,1,5504,4,1,19,1,4,1,8),_ZhonePingResultsSentProbes_Type())
zhonePingResultsSentProbes.setMaxAccess(_D)
if mibBuilder.loadTexts:zhonePingResultsSentProbes.setStatus(_A)
if mibBuilder.loadTexts:zhonePingResultsSentProbes.setUnits(_Y)
_ZhonePingResultsRttSumOfSquares_Type=Unsigned32
_ZhonePingResultsRttSumOfSquares_Object=MibTableColumn
zhonePingResultsRttSumOfSquares=_ZhonePingResultsRttSumOfSquares_Object((1,3,6,1,4,1,5504,4,1,19,1,4,1,9),_ZhonePingResultsRttSumOfSquares_Type())
zhonePingResultsRttSumOfSquares.setMaxAccess(_D)
if mibBuilder.loadTexts:zhonePingResultsRttSumOfSquares.setStatus(_A)
if mibBuilder.loadTexts:zhonePingResultsRttSumOfSquares.setUnits(_J)
_ZhonePingResultsLastGoodProbe_Type=DateAndTime
_ZhonePingResultsLastGoodProbe_Object=MibTableColumn
zhonePingResultsLastGoodProbe=_ZhonePingResultsLastGoodProbe_Object((1,3,6,1,4,1,5504,4,1,19,1,4,1,10),_ZhonePingResultsLastGoodProbe_Type())
zhonePingResultsLastGoodProbe.setMaxAccess(_D)
if mibBuilder.loadTexts:zhonePingResultsLastGoodProbe.setStatus(_A)
_ZhonePingConformance_ObjectIdentity=ObjectIdentity
zhonePingConformance=_ZhonePingConformance_ObjectIdentity((1,3,6,1,4,1,5504,4,1,19,2))
_ZhonePingGroups_ObjectIdentity=ObjectIdentity
zhonePingGroups=_ZhonePingGroups_ObjectIdentity((1,3,6,1,4,1,5504,4,1,19,2,2))
_ZhonePingImplementationTypeDomains_ObjectIdentity=ObjectIdentity
zhonePingImplementationTypeDomains=_ZhonePingImplementationTypeDomains_ObjectIdentity((1,3,6,1,4,1,5504,4,1,19,3))
_ZhonePingIcmpEcho_ObjectIdentity=ObjectIdentity
zhonePingIcmpEcho=_ZhonePingIcmpEcho_ObjectIdentity((1,3,6,1,4,1,5504,4,1,19,3,1))
if mibBuilder.loadTexts:zhonePingIcmpEcho.setStatus(_A)
_ZhonePingUdpEcho_ObjectIdentity=ObjectIdentity
zhonePingUdpEcho=_ZhonePingUdpEcho_ObjectIdentity((1,3,6,1,4,1,5504,4,1,19,3,2))
if mibBuilder.loadTexts:zhonePingUdpEcho.setStatus(_A)
_ZhonePingSnmpQuery_ObjectIdentity=ObjectIdentity
zhonePingSnmpQuery=_ZhonePingSnmpQuery_ObjectIdentity((1,3,6,1,4,1,5504,4,1,19,3,3))
if mibBuilder.loadTexts:zhonePingSnmpQuery.setStatus(_A)
_ZhonePingTcpConnectionAttempt_ObjectIdentity=ObjectIdentity
zhonePingTcpConnectionAttempt=_ZhonePingTcpConnectionAttempt_ObjectIdentity((1,3,6,1,4,1,5504,4,1,19,3,4))
if mibBuilder.loadTexts:zhonePingTcpConnectionAttempt.setStatus(_A)
zhonePingGroup=ObjectGroup((1,3,6,1,4,1,5504,4,1,19,2,2,1))
zhonePingGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_z)))
if mibBuilder.loadTexts:zhonePingGroup.setStatus(_A)
zhonePingTimeStampGroup=ObjectGroup((1,3,6,1,4,1,5504,4,1,19,2,2,2))
zhonePingTimeStampGroup.setObjects((_B,_A0))
if mibBuilder.loadTexts:zhonePingTimeStampGroup.setStatus(_A)
zhonePingTestCompleted=NotificationType((1,3,6,1,4,1,5504,4,1,19,0,1))
zhonePingTestCompleted.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:zhonePingTestCompleted.setStatus(_A)
zhonePingNotificationsGroup=NotificationGroup((1,3,6,1,4,1,5504,4,1,19,2,2,3))
zhonePingNotificationsGroup.setObjects((_B,_A1))
if mibBuilder.loadTexts:zhonePingNotificationsGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'OperationResponseStatus':OperationResponseStatus,'zhonePingMIB':zhonePingMIB,'zhonePingNotifications':zhonePingNotifications,_A1:zhonePingTestCompleted,'zhonePingObjects':zhonePingObjects,_b:zhonePingMaxConcurrentRequests,'zhonePingCtlIndexNext':zhonePingCtlIndexNext,'zhonePingCtlTable':zhonePingCtlTable,'zhonePingCtlEntry':zhonePingCtlEntry,_K:zhonePingCtlIndex,_c:zhonePingCtlTargetAddressType,_d:zhonePingCtlTargetAddress,_e:zhonePingCtlDataSize,_f:zhonePingCtlTimeOut,_g:zhonePingCtlProbeCount,_h:zhonePingCtlAdminStatus,_i:zhonePingCtlDataFill,_j:zhonePingCtlFrequency,_k:zhonePingCtlMaxRows,_l:zhonePingCtlStorageType,_m:zhonePingCtlTrapGeneration,_n:zhonePingCtlTrapProbeFailureFilter,_o:zhonePingCtlTrapTestFailureFilter,_p:zhonePingCtlType,_q:zhonePingCtlDescr,_s:zhonePingCtlSourceAddressType,_t:zhonePingCtlSourceAddress,_u:zhonePingCtlIfIndex,_r:zhonePingCtlByPassRouteTable,_v:zhonePingCtlDSField,_w:zhonePingCtlRowStatus,'zhonePingResultsTable':zhonePingResultsTable,'zhonePingResultsEntry':zhonePingResultsEntry,_x:zhonePingResultsOperStatus,_y:zhonePingResultsIpTargetAddressType,_L:zhonePingResultsIpTargetAddress,_M:zhonePingResultsMinRtt,_N:zhonePingResultsMaxRtt,_O:zhonePingResultsAverageRtt,_P:zhonePingResultsProbeResponses,_Q:zhonePingResultsSentProbes,_z:zhonePingResultsRttSumOfSquares,_A0:zhonePingResultsLastGoodProbe,'zhonePingConformance':zhonePingConformance,'zhonePingGroups':zhonePingGroups,'zhonePingGroup':zhonePingGroup,'zhonePingTimeStampGroup':zhonePingTimeStampGroup,'zhonePingNotificationsGroup':zhonePingNotificationsGroup,'zhonePingImplementationTypeDomains':zhonePingImplementationTypeDomains,'zhonePingIcmpEcho':zhonePingIcmpEcho,'zhonePingUdpEcho':zhonePingUdpEcho,'zhonePingSnmpQuery':zhonePingSnmpQuery,'zhonePingTcpConnectionAttempt':zhonePingTcpConnectionAttempt})