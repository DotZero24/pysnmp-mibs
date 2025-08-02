_y='ccacSysProtocolResGroup'
_x='ccacSysGatewayResGroup'
_w='ccacSysStatGroup'
_v='ccacSysDialCtrlConfigGroup'
_u='ccacSysResPolicyGroup'
_t='ccacSysConfigGroup'
_s='ccacSysProResPolicyIndex'
_r='ccacSysProResType'
_q='ccacSysGwResPolicyIndex'
_p='ccacSysGwResType'
_o='ccacSysCallsInSWindow'
_n='ccacSysCallRejections'
_m='ccacSysRsCallsWhenExceed'
_l='ccacSysRsExceedCount'
_k='ccacSysRsPrevDuration'
_j='ccacSysRsDuration'
_i='ccacSysRsState'
_h='ccacSysRpAvailable'
_g='ccacSysRpCurReading'
_f='ccacSysRpAction'
_e='ccacSysRpInterval'
_d='ccacSysRpLowThreshold'
_c='ccacSysRpMedThreshold'
_b='ccacSysRpHighThreshold'
_a='ccacSysRpPercentOrAbsNum'
_Z='ccacSysRpAvgUtilization'
_Y='ccacSysRpUserTunable'
_X='ccacSysRpResType'
_W='ccacSysCallSpike'
_V='ccacSysSlidingWindowSize'
_U='ccacSysSlidingWindowSteps'
_T='ccacSysPlayMessageFile'
_S='ccacSysIsdnRejectCode'
_R='ccacSysRejectCode'
_Q='ccacSysTreatment'
_P='ccacSysNotifyEnable'
_O='ccacSysCacEnable'
_N='ccacSysStatEntry'
_M='ccacSysProResIndex'
_L='ccacSysGwResIndex'
_K='cmgwSignalProtocolIndex'
_J='ccacSysRpIndex'
_I='not-accessible'
_H='TruthValue'
_G='cmgwIndex'
_F='CISCO-MEDIA-GATEWAY-MIB'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='CISCO-CAC-SYSTEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cmgwIndex,cmgwSignalProtocolIndex=mibBuilder.importSymbols(_F,_G,_K)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeInterval',_H)
ccacSysMIB=ModuleIdentity((1,3,6,1,4,1,9,9,322))
if mibBuilder.loadTexts:ccacSysMIB.setRevisions(('2003-04-24 00:00',))
class CcacResourceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*(('cpu5Sec',1),('cpuAvg',2),('ioMem',3),('procMem',4),('totMem',5),('totCalls',6),('staMem',7),('dynMem',8),('commBuf',9),('msgQueue',10),('dspQueue',11),('svc',12),('ds0',13),('dspChannel',14),('h248Mem',15)))
_CcacSysObjects_ObjectIdentity=ObjectIdentity
ccacSysObjects=_CcacSysObjects_ObjectIdentity((1,3,6,1,4,1,9,9,322,1))
_CcacSysConfig_ObjectIdentity=ObjectIdentity
ccacSysConfig=_CcacSysConfig_ObjectIdentity((1,3,6,1,4,1,9,9,322,1,1))
_CcacSysConfigTable_Object=MibTable
ccacSysConfigTable=_CcacSysConfigTable_Object((1,3,6,1,4,1,9,9,322,1,1,1))
if mibBuilder.loadTexts:ccacSysConfigTable.setStatus(_A)
_CcacSysConfigEntry_Object=MibTableRow
ccacSysConfigEntry=_CcacSysConfigEntry_Object((1,3,6,1,4,1,9,9,322,1,1,1,1))
ccacSysConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ccacSysConfigEntry.setStatus(_A)
class _CcacSysCacEnable_Type(TruthValue):defaultValue=1
_CcacSysCacEnable_Type.__name__=_H
_CcacSysCacEnable_Object=MibTableColumn
ccacSysCacEnable=_CcacSysCacEnable_Object((1,3,6,1,4,1,9,9,322,1,1,1,1,1),_CcacSysCacEnable_Type())
ccacSysCacEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ccacSysCacEnable.setStatus(_A)
class _CcacSysNotifyEnable_Type(TruthValue):defaultValue=1
_CcacSysNotifyEnable_Type.__name__=_H
_CcacSysNotifyEnable_Object=MibTableColumn
ccacSysNotifyEnable=_CcacSysNotifyEnable_Object((1,3,6,1,4,1,9,9,322,1,1,1,1,2),_CcacSysNotifyEnable_Type())
ccacSysNotifyEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ccacSysNotifyEnable.setStatus(_A)
class _CcacSysTreatment_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hairpin',1),('reject',2),('playMessage',3)))
_CcacSysTreatment_Type.__name__=_C
_CcacSysTreatment_Object=MibTableColumn
ccacSysTreatment=_CcacSysTreatment_Object((1,3,6,1,4,1,9,9,322,1,1,1,1,3),_CcacSysTreatment_Type())
ccacSysTreatment.setMaxAccess(_E)
if mibBuilder.loadTexts:ccacSysTreatment.setStatus(_A)
class _CcacSysRejectCode_Type(Integer32):defaultValue=44;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CcacSysRejectCode_Type.__name__=_C
_CcacSysRejectCode_Object=MibTableColumn
ccacSysRejectCode=_CcacSysRejectCode_Object((1,3,6,1,4,1,9,9,322,1,1,1,1,4),_CcacSysRejectCode_Type())
ccacSysRejectCode.setMaxAccess(_E)
if mibBuilder.loadTexts:ccacSysRejectCode.setStatus(_A)
class _CcacSysIsdnRejectCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(34,47))
_CcacSysIsdnRejectCode_Type.__name__=_C
_CcacSysIsdnRejectCode_Object=MibTableColumn
ccacSysIsdnRejectCode=_CcacSysIsdnRejectCode_Object((1,3,6,1,4,1,9,9,322,1,1,1,1,5),_CcacSysIsdnRejectCode_Type())
ccacSysIsdnRejectCode.setMaxAccess(_E)
if mibBuilder.loadTexts:ccacSysIsdnRejectCode.setStatus(_A)
_CcacSysPlayMessageFile_Type=SnmpAdminString
_CcacSysPlayMessageFile_Object=MibTableColumn
ccacSysPlayMessageFile=_CcacSysPlayMessageFile_Object((1,3,6,1,4,1,9,9,322,1,1,1,1,6),_CcacSysPlayMessageFile_Type())
ccacSysPlayMessageFile.setMaxAccess(_E)
if mibBuilder.loadTexts:ccacSysPlayMessageFile.setStatus(_A)
class _CcacSysSlidingWindowSteps_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,10))
_CcacSysSlidingWindowSteps_Type.__name__=_C
_CcacSysSlidingWindowSteps_Object=MibTableColumn
ccacSysSlidingWindowSteps=_CcacSysSlidingWindowSteps_Object((1,3,6,1,4,1,9,9,322,1,1,1,1,7),_CcacSysSlidingWindowSteps_Type())
ccacSysSlidingWindowSteps.setMaxAccess(_E)
if mibBuilder.loadTexts:ccacSysSlidingWindowSteps.setStatus(_A)
class _CcacSysSlidingWindowSize_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,2000))
_CcacSysSlidingWindowSize_Type.__name__=_C
_CcacSysSlidingWindowSize_Object=MibTableColumn
ccacSysSlidingWindowSize=_CcacSysSlidingWindowSize_Object((1,3,6,1,4,1,9,9,322,1,1,1,1,8),_CcacSysSlidingWindowSize_Type())
ccacSysSlidingWindowSize.setMaxAccess(_E)
if mibBuilder.loadTexts:ccacSysSlidingWindowSize.setStatus(_A)
if mibBuilder.loadTexts:ccacSysSlidingWindowSize.setUnits('millisecond')
class _CcacSysCallSpike_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CcacSysCallSpike_Type.__name__=_C
_CcacSysCallSpike_Object=MibTableColumn
ccacSysCallSpike=_CcacSysCallSpike_Object((1,3,6,1,4,1,9,9,322,1,1,1,1,9),_CcacSysCallSpike_Type())
ccacSysCallSpike.setMaxAccess(_E)
if mibBuilder.loadTexts:ccacSysCallSpike.setStatus(_A)
if mibBuilder.loadTexts:ccacSysCallSpike.setUnits('calls')
_CcacSysResPolicy_ObjectIdentity=ObjectIdentity
ccacSysResPolicy=_CcacSysResPolicy_ObjectIdentity((1,3,6,1,4,1,9,9,322,1,2))
_CcacSysGatewayResTable_Object=MibTable
ccacSysGatewayResTable=_CcacSysGatewayResTable_Object((1,3,6,1,4,1,9,9,322,1,2,1))
if mibBuilder.loadTexts:ccacSysGatewayResTable.setStatus(_A)
_CcacSysGatewayResEntry_Object=MibTableRow
ccacSysGatewayResEntry=_CcacSysGatewayResEntry_Object((1,3,6,1,4,1,9,9,322,1,2,1,1))
ccacSysGatewayResEntry.setIndexNames((0,_F,_G),(0,_B,_L))
if mibBuilder.loadTexts:ccacSysGatewayResEntry.setStatus(_A)
class _CcacSysGwResIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_CcacSysGwResIndex_Type.__name__=_C
_CcacSysGwResIndex_Object=MibTableColumn
ccacSysGwResIndex=_CcacSysGwResIndex_Object((1,3,6,1,4,1,9,9,322,1,2,1,1,1),_CcacSysGwResIndex_Type())
ccacSysGwResIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ccacSysGwResIndex.setStatus(_A)
_CcacSysGwResType_Type=CcacResourceType
_CcacSysGwResType_Object=MibTableColumn
ccacSysGwResType=_CcacSysGwResType_Object((1,3,6,1,4,1,9,9,322,1,2,1,1,2),_CcacSysGwResType_Type())
ccacSysGwResType.setMaxAccess(_D)
if mibBuilder.loadTexts:ccacSysGwResType.setStatus(_A)
class _CcacSysGwResPolicyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CcacSysGwResPolicyIndex_Type.__name__=_C
_CcacSysGwResPolicyIndex_Object=MibTableColumn
ccacSysGwResPolicyIndex=_CcacSysGwResPolicyIndex_Object((1,3,6,1,4,1,9,9,322,1,2,1,1,3),_CcacSysGwResPolicyIndex_Type())
ccacSysGwResPolicyIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ccacSysGwResPolicyIndex.setStatus(_A)
_CcacSysProtocolResTable_Object=MibTable
ccacSysProtocolResTable=_CcacSysProtocolResTable_Object((1,3,6,1,4,1,9,9,322,1,2,2))
if mibBuilder.loadTexts:ccacSysProtocolResTable.setStatus(_A)
_CcacSysProtocolResEntry_Object=MibTableRow
ccacSysProtocolResEntry=_CcacSysProtocolResEntry_Object((1,3,6,1,4,1,9,9,322,1,2,2,1))
ccacSysProtocolResEntry.setIndexNames((0,_F,_G),(0,_F,_K),(0,_B,_M))
if mibBuilder.loadTexts:ccacSysProtocolResEntry.setStatus(_A)
class _CcacSysProResIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_CcacSysProResIndex_Type.__name__=_C
_CcacSysProResIndex_Object=MibTableColumn
ccacSysProResIndex=_CcacSysProResIndex_Object((1,3,6,1,4,1,9,9,322,1,2,2,1,1),_CcacSysProResIndex_Type())
ccacSysProResIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ccacSysProResIndex.setStatus(_A)
_CcacSysProResType_Type=CcacResourceType
_CcacSysProResType_Object=MibTableColumn
ccacSysProResType=_CcacSysProResType_Object((1,3,6,1,4,1,9,9,322,1,2,2,1,2),_CcacSysProResType_Type())
ccacSysProResType.setMaxAccess(_D)
if mibBuilder.loadTexts:ccacSysProResType.setStatus(_A)
class _CcacSysProResPolicyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CcacSysProResPolicyIndex_Type.__name__=_C
_CcacSysProResPolicyIndex_Object=MibTableColumn
ccacSysProResPolicyIndex=_CcacSysProResPolicyIndex_Object((1,3,6,1,4,1,9,9,322,1,2,2,1,3),_CcacSysProResPolicyIndex_Type())
ccacSysProResPolicyIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ccacSysProResPolicyIndex.setStatus(_A)
_CcacSysResPolicyTable_Object=MibTable
ccacSysResPolicyTable=_CcacSysResPolicyTable_Object((1,3,6,1,4,1,9,9,322,1,2,3))
if mibBuilder.loadTexts:ccacSysResPolicyTable.setStatus(_A)
_CcacSysResPolicyEntry_Object=MibTableRow
ccacSysResPolicyEntry=_CcacSysResPolicyEntry_Object((1,3,6,1,4,1,9,9,322,1,2,3,1))
ccacSysResPolicyEntry.setIndexNames((0,_F,_G),(0,_B,_J))
if mibBuilder.loadTexts:ccacSysResPolicyEntry.setStatus(_A)
class _CcacSysRpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CcacSysRpIndex_Type.__name__=_C
_CcacSysRpIndex_Object=MibTableColumn
ccacSysRpIndex=_CcacSysRpIndex_Object((1,3,6,1,4,1,9,9,322,1,2,3,1,1),_CcacSysRpIndex_Type())
ccacSysRpIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ccacSysRpIndex.setStatus(_A)
_CcacSysRpResType_Type=CcacResourceType
_CcacSysRpResType_Object=MibTableColumn
ccacSysRpResType=_CcacSysRpResType_Object((1,3,6,1,4,1,9,9,322,1,2,3,1,2),_CcacSysRpResType_Type())
ccacSysRpResType.setMaxAccess(_D)
if mibBuilder.loadTexts:ccacSysRpResType.setStatus(_A)
_CcacSysRpUserTunable_Type=TruthValue
_CcacSysRpUserTunable_Object=MibTableColumn
ccacSysRpUserTunable=_CcacSysRpUserTunable_Object((1,3,6,1,4,1,9,9,322,1,2,3,1,3),_CcacSysRpUserTunable_Type())
ccacSysRpUserTunable.setMaxAccess(_D)
if mibBuilder.loadTexts:ccacSysRpUserTunable.setStatus(_A)
_CcacSysRpAvgUtilization_Type=TruthValue
_CcacSysRpAvgUtilization_Object=MibTableColumn
ccacSysRpAvgUtilization=_CcacSysRpAvgUtilization_Object((1,3,6,1,4,1,9,9,322,1,2,3,1,4),_CcacSysRpAvgUtilization_Type())
ccacSysRpAvgUtilization.setMaxAccess(_D)
if mibBuilder.loadTexts:ccacSysRpAvgUtilization.setStatus(_A)
class _CcacSysRpPercentOrAbsNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unitPercent',1),('unitAbsoluteNum',2)))
_CcacSysRpPercentOrAbsNum_Type.__name__=_C
_CcacSysRpPercentOrAbsNum_Object=MibTableColumn
ccacSysRpPercentOrAbsNum=_CcacSysRpPercentOrAbsNum_Object((1,3,6,1,4,1,9,9,322,1,2,3,1,5),_CcacSysRpPercentOrAbsNum_Type())
ccacSysRpPercentOrAbsNum.setMaxAccess(_D)
if mibBuilder.loadTexts:ccacSysRpPercentOrAbsNum.setStatus(_A)
class _CcacSysRpHighThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_CcacSysRpHighThreshold_Type.__name__=_C
_CcacSysRpHighThreshold_Object=MibTableColumn
ccacSysRpHighThreshold=_CcacSysRpHighThreshold_Object((1,3,6,1,4,1,9,9,322,1,2,3,1,6),_CcacSysRpHighThreshold_Type())
ccacSysRpHighThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:ccacSysRpHighThreshold.setStatus(_A)
class _CcacSysRpMedThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_CcacSysRpMedThreshold_Type.__name__=_C
_CcacSysRpMedThreshold_Object=MibTableColumn
ccacSysRpMedThreshold=_CcacSysRpMedThreshold_Object((1,3,6,1,4,1,9,9,322,1,2,3,1,7),_CcacSysRpMedThreshold_Type())
ccacSysRpMedThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:ccacSysRpMedThreshold.setStatus(_A)
class _CcacSysRpLowThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_CcacSysRpLowThreshold_Type.__name__=_C
_CcacSysRpLowThreshold_Object=MibTableColumn
ccacSysRpLowThreshold=_CcacSysRpLowThreshold_Object((1,3,6,1,4,1,9,9,322,1,2,3,1,8),_CcacSysRpLowThreshold_Type())
ccacSysRpLowThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:ccacSysRpLowThreshold.setStatus(_A)
class _CcacSysRpInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_CcacSysRpInterval_Type.__name__=_C
_CcacSysRpInterval_Object=MibTableColumn
ccacSysRpInterval=_CcacSysRpInterval_Object((1,3,6,1,4,1,9,9,322,1,2,3,1,9),_CcacSysRpInterval_Type())
ccacSysRpInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:ccacSysRpInterval.setStatus(_A)
if mibBuilder.loadTexts:ccacSysRpInterval.setUnits('seconds')
class _CcacSysRpAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('busyout',2),('treatment',3),('busyoutAndTreatment',4)))
_CcacSysRpAction_Type.__name__=_C
_CcacSysRpAction_Object=MibTableColumn
ccacSysRpAction=_CcacSysRpAction_Object((1,3,6,1,4,1,9,9,322,1,2,3,1,10),_CcacSysRpAction_Type())
ccacSysRpAction.setMaxAccess(_E)
if mibBuilder.loadTexts:ccacSysRpAction.setStatus(_A)
class _CcacSysRpCurReading_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_CcacSysRpCurReading_Type.__name__=_C
_CcacSysRpCurReading_Object=MibTableColumn
ccacSysRpCurReading=_CcacSysRpCurReading_Object((1,3,6,1,4,1,9,9,322,1,2,3,1,11),_CcacSysRpCurReading_Type())
ccacSysRpCurReading.setMaxAccess(_D)
if mibBuilder.loadTexts:ccacSysRpCurReading.setStatus(_A)
_CcacSysRpAvailable_Type=TruthValue
_CcacSysRpAvailable_Object=MibTableColumn
ccacSysRpAvailable=_CcacSysRpAvailable_Object((1,3,6,1,4,1,9,9,322,1,2,3,1,12),_CcacSysRpAvailable_Type())
ccacSysRpAvailable.setMaxAccess(_D)
if mibBuilder.loadTexts:ccacSysRpAvailable.setStatus(_A)
_CcacSysStat_ObjectIdentity=ObjectIdentity
ccacSysStat=_CcacSysStat_ObjectIdentity((1,3,6,1,4,1,9,9,322,1,3))
_CcacSysResStatTable_Object=MibTable
ccacSysResStatTable=_CcacSysResStatTable_Object((1,3,6,1,4,1,9,9,322,1,3,1))
if mibBuilder.loadTexts:ccacSysResStatTable.setStatus(_A)
_CcacSysResStatEntry_Object=MibTableRow
ccacSysResStatEntry=_CcacSysResStatEntry_Object((1,3,6,1,4,1,9,9,322,1,3,1,1))
ccacSysResStatEntry.setIndexNames((0,_F,_G),(0,_B,_J))
if mibBuilder.loadTexts:ccacSysResStatEntry.setStatus(_A)
class _CcacSysRsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('thresholdClear',1),('thresholdExceed',2),('thresholdWarn',3)))
_CcacSysRsState_Type.__name__=_C
_CcacSysRsState_Object=MibTableColumn
ccacSysRsState=_CcacSysRsState_Object((1,3,6,1,4,1,9,9,322,1,3,1,1,1),_CcacSysRsState_Type())
ccacSysRsState.setMaxAccess(_D)
if mibBuilder.loadTexts:ccacSysRsState.setStatus(_A)
_CcacSysRsDuration_Type=TimeInterval
_CcacSysRsDuration_Object=MibTableColumn
ccacSysRsDuration=_CcacSysRsDuration_Object((1,3,6,1,4,1,9,9,322,1,3,1,1,2),_CcacSysRsDuration_Type())
ccacSysRsDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:ccacSysRsDuration.setStatus(_A)
_CcacSysRsPrevDuration_Type=TimeInterval
_CcacSysRsPrevDuration_Object=MibTableColumn
ccacSysRsPrevDuration=_CcacSysRsPrevDuration_Object((1,3,6,1,4,1,9,9,322,1,3,1,1,3),_CcacSysRsPrevDuration_Type())
ccacSysRsPrevDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:ccacSysRsPrevDuration.setStatus(_A)
_CcacSysRsExceedCount_Type=Counter32
_CcacSysRsExceedCount_Object=MibTableColumn
ccacSysRsExceedCount=_CcacSysRsExceedCount_Object((1,3,6,1,4,1,9,9,322,1,3,1,1,4),_CcacSysRsExceedCount_Type())
ccacSysRsExceedCount.setMaxAccess(_D)
if mibBuilder.loadTexts:ccacSysRsExceedCount.setStatus(_A)
_CcacSysRsCallsWhenExceed_Type=Counter32
_CcacSysRsCallsWhenExceed_Object=MibTableColumn
ccacSysRsCallsWhenExceed=_CcacSysRsCallsWhenExceed_Object((1,3,6,1,4,1,9,9,322,1,3,1,1,5),_CcacSysRsCallsWhenExceed_Type())
ccacSysRsCallsWhenExceed.setMaxAccess(_D)
if mibBuilder.loadTexts:ccacSysRsCallsWhenExceed.setStatus(_A)
_CcacSysStatTable_Object=MibTable
ccacSysStatTable=_CcacSysStatTable_Object((1,3,6,1,4,1,9,9,322,1,3,2))
if mibBuilder.loadTexts:ccacSysStatTable.setStatus(_A)
_CcacSysStatEntry_Object=MibTableRow
ccacSysStatEntry=_CcacSysStatEntry_Object((1,3,6,1,4,1,9,9,322,1,3,2,1))
if mibBuilder.loadTexts:ccacSysStatEntry.setStatus(_A)
_CcacSysCallRejections_Type=Counter32
_CcacSysCallRejections_Object=MibTableColumn
ccacSysCallRejections=_CcacSysCallRejections_Object((1,3,6,1,4,1,9,9,322,1,3,2,1,1),_CcacSysCallRejections_Type())
ccacSysCallRejections.setMaxAccess(_D)
if mibBuilder.loadTexts:ccacSysCallRejections.setStatus(_A)
_CcacSysCallsInSWindow_Type=Counter32
_CcacSysCallsInSWindow_Object=MibTableColumn
ccacSysCallsInSWindow=_CcacSysCallsInSWindow_Object((1,3,6,1,4,1,9,9,322,1,3,2,1,2),_CcacSysCallsInSWindow_Type())
ccacSysCallsInSWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:ccacSysCallsInSWindow.setStatus(_A)
_CcacSysConformance_ObjectIdentity=ObjectIdentity
ccacSysConformance=_CcacSysConformance_ObjectIdentity((1,3,6,1,4,1,9,9,322,2))
_CcacSysCompliances_ObjectIdentity=ObjectIdentity
ccacSysCompliances=_CcacSysCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,322,2,1))
_CcacSysGroups_ObjectIdentity=ObjectIdentity
ccacSysGroups=_CcacSysGroups_ObjectIdentity((1,3,6,1,4,1,9,9,322,2,2))
ccacSysConfigEntry.registerAugmentions((_B,_N))
ccacSysStatEntry.setIndexNames(*ccacSysConfigEntry.getIndexNames())
ccacSysConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,322,2,2,1))
ccacSysConfigGroup.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ccacSysConfigGroup.setStatus(_A)
ccacSysDialCtrlConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,322,2,2,2))
ccacSysDialCtrlConfigGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:ccacSysDialCtrlConfigGroup.setStatus(_A)
ccacSysResPolicyGroup=ObjectGroup((1,3,6,1,4,1,9,9,322,2,2,3))
ccacSysResPolicyGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:ccacSysResPolicyGroup.setStatus(_A)
ccacSysStatGroup=ObjectGroup((1,3,6,1,4,1,9,9,322,2,2,4))
ccacSysStatGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o)))
if mibBuilder.loadTexts:ccacSysStatGroup.setStatus(_A)
ccacSysGatewayResGroup=ObjectGroup((1,3,6,1,4,1,9,9,322,2,2,5))
ccacSysGatewayResGroup.setObjects(*((_B,_p),(_B,_q)))
if mibBuilder.loadTexts:ccacSysGatewayResGroup.setStatus(_A)
ccacSysProtocolResGroup=ObjectGroup((1,3,6,1,4,1,9,9,322,2,2,6))
ccacSysProtocolResGroup.setObjects(*((_B,_r),(_B,_s)))
if mibBuilder.loadTexts:ccacSysProtocolResGroup.setStatus(_A)
ccacSysCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,322,2,1,1))
ccacSysCompliance.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:ccacSysCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CcacResourceType':CcacResourceType,'ccacSysMIB':ccacSysMIB,'ccacSysObjects':ccacSysObjects,'ccacSysConfig':ccacSysConfig,'ccacSysConfigTable':ccacSysConfigTable,'ccacSysConfigEntry':ccacSysConfigEntry,_O:ccacSysCacEnable,_P:ccacSysNotifyEnable,_Q:ccacSysTreatment,_R:ccacSysRejectCode,_S:ccacSysIsdnRejectCode,_T:ccacSysPlayMessageFile,_U:ccacSysSlidingWindowSteps,_V:ccacSysSlidingWindowSize,_W:ccacSysCallSpike,'ccacSysResPolicy':ccacSysResPolicy,'ccacSysGatewayResTable':ccacSysGatewayResTable,'ccacSysGatewayResEntry':ccacSysGatewayResEntry,_L:ccacSysGwResIndex,_p:ccacSysGwResType,_q:ccacSysGwResPolicyIndex,'ccacSysProtocolResTable':ccacSysProtocolResTable,'ccacSysProtocolResEntry':ccacSysProtocolResEntry,_M:ccacSysProResIndex,_r:ccacSysProResType,_s:ccacSysProResPolicyIndex,'ccacSysResPolicyTable':ccacSysResPolicyTable,'ccacSysResPolicyEntry':ccacSysResPolicyEntry,_J:ccacSysRpIndex,_X:ccacSysRpResType,_Y:ccacSysRpUserTunable,_Z:ccacSysRpAvgUtilization,_a:ccacSysRpPercentOrAbsNum,_b:ccacSysRpHighThreshold,_c:ccacSysRpMedThreshold,_d:ccacSysRpLowThreshold,_e:ccacSysRpInterval,_f:ccacSysRpAction,_g:ccacSysRpCurReading,_h:ccacSysRpAvailable,'ccacSysStat':ccacSysStat,'ccacSysResStatTable':ccacSysResStatTable,'ccacSysResStatEntry':ccacSysResStatEntry,_i:ccacSysRsState,_j:ccacSysRsDuration,_k:ccacSysRsPrevDuration,_l:ccacSysRsExceedCount,_m:ccacSysRsCallsWhenExceed,'ccacSysStatTable':ccacSysStatTable,_N:ccacSysStatEntry,_n:ccacSysCallRejections,_o:ccacSysCallsInSWindow,'ccacSysConformance':ccacSysConformance,'ccacSysCompliances':ccacSysCompliances,'ccacSysCompliance':ccacSysCompliance,'ccacSysGroups':ccacSysGroups,_t:ccacSysConfigGroup,_v:ccacSysDialCtrlConfigGroup,_u:ccacSysResPolicyGroup,_w:ccacSysStatGroup,_x:ccacSysGatewayResGroup,_y:ccacSysProtocolResGroup})