_a='hwLapdIsdnLinkStatus'
_Z='hwQ931IsdnCallTimeClose'
_Y='hwQ931IsdnLastCauseDisc'
_X='hwChanbIsdnCallFreeCode'
_W='hwChanbIsdnCallFreeReason'
_V='hwChanbIsdnLastKeepTime'
_U='hwChanbIsdnInfoType'
_T='hwChanbIsdnCallerAddr'
_S='hwChanbIsdnCallType'
_R='hwChanbIsdnAddr'
_Q='accessible-for-notify'
_P='milliseconds'
_O='unknown'
_N='hwQ931IsdnCallTimeOpen'
_M='hwQ931IsdnCallDirection'
_L='hwQ931IsdnLastCalling'
_K='hwQ931IsdnLastCalled'
_J='hwLapdIsdnIf'
_I='hwChanbIsdnIf'
_H='hwQ931IsdnOpIndex'
_G='disabled'
_F='enabled'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='A3COM-HUAWEI-ISDN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mlsr,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','mlsr')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
hwIsdnMib=ModuleIdentity((1,3,6,1,4,1,43,45,1,2,33,9))
_HwIsdnMibObjects_ObjectIdentity=ObjectIdentity
hwIsdnMibObjects=_HwIsdnMibObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,33,9,1))
_IsdnChannelB_ObjectIdentity=ObjectIdentity
isdnChannelB=_IsdnChannelB_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,33,9,1,1))
_HwChanbIsdnTable_Object=MibTable
hwChanbIsdnTable=_HwChanbIsdnTable_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,1,1))
if mibBuilder.loadTexts:hwChanbIsdnTable.setStatus(_A)
_HwChanbIsdnEntry_Object=MibTableRow
hwChanbIsdnEntry=_HwChanbIsdnEntry_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,1,1,1))
hwChanbIsdnEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hwChanbIsdnEntry.setStatus(_A)
_HwChanbIsdnIf_Type=Integer32
_HwChanbIsdnIf_Object=MibTableColumn
hwChanbIsdnIf=_HwChanbIsdnIf_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,1,1,1,1),_HwChanbIsdnIf_Type())
hwChanbIsdnIf.setMaxAccess(_C)
if mibBuilder.loadTexts:hwChanbIsdnIf.setStatus(_A)
class _HwChanbIsdnPermit_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('callOut',1),('callIn',2),('callBidirection',3)))
_HwChanbIsdnPermit_Type.__name__=_D
_HwChanbIsdnPermit_Object=MibTableColumn
hwChanbIsdnPermit=_HwChanbIsdnPermit_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,1,1,1,2),_HwChanbIsdnPermit_Type())
hwChanbIsdnPermit.setMaxAccess(_C)
if mibBuilder.loadTexts:hwChanbIsdnPermit.setStatus(_A)
_HwChanbIsdnAddr_Type=DisplayString
_HwChanbIsdnAddr_Object=MibTableColumn
hwChanbIsdnAddr=_HwChanbIsdnAddr_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,1,1,1,3),_HwChanbIsdnAddr_Type())
hwChanbIsdnAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hwChanbIsdnAddr.setStatus(_A)
_HwChanbIsdnCallerAddr_Type=DisplayString
_HwChanbIsdnCallerAddr_Object=MibTableColumn
hwChanbIsdnCallerAddr=_HwChanbIsdnCallerAddr_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,1,1,1,4),_HwChanbIsdnCallerAddr_Type())
hwChanbIsdnCallerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hwChanbIsdnCallerAddr.setStatus(_A)
class _HwChanbIsdnCallType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('nocall',0),('call',1),('answer',2)))
_HwChanbIsdnCallType_Type.__name__=_D
_HwChanbIsdnCallType_Object=MibTableColumn
hwChanbIsdnCallType=_HwChanbIsdnCallType_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,1,1,1,5),_HwChanbIsdnCallType_Type())
hwChanbIsdnCallType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwChanbIsdnCallType.setStatus(_A)
class _HwChanbIsdnInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_O,1),('speech',2),('unrestrDigit',3),('unrestrDigit56',4),('restrictDigit',5),('audio31',6),('audio7',7),('video',8),('swithchedPacket',9)))
_HwChanbIsdnInfoType_Type.__name__=_D
_HwChanbIsdnInfoType_Object=MibTableColumn
hwChanbIsdnInfoType=_HwChanbIsdnInfoType_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,1,1,1,6),_HwChanbIsdnInfoType_Type())
hwChanbIsdnInfoType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwChanbIsdnInfoType.setStatus(_A)
class _HwChanbIsdnState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('idle',1),('connecting',2),('active',3)))
_HwChanbIsdnState_Type.__name__=_D
_HwChanbIsdnState_Object=MibTableColumn
hwChanbIsdnState=_HwChanbIsdnState_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,1,1,1,7),_HwChanbIsdnState_Type())
hwChanbIsdnState.setMaxAccess(_C)
if mibBuilder.loadTexts:hwChanbIsdnState.setStatus(_A)
_HwChanbIsdnCallFreeReason_Type=DisplayString
_HwChanbIsdnCallFreeReason_Object=MibTableColumn
hwChanbIsdnCallFreeReason=_HwChanbIsdnCallFreeReason_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,1,1,1,8),_HwChanbIsdnCallFreeReason_Type())
hwChanbIsdnCallFreeReason.setMaxAccess(_C)
if mibBuilder.loadTexts:hwChanbIsdnCallFreeReason.setStatus(_A)
_HwChanbIsdnCallFreeCode_Type=Integer32
_HwChanbIsdnCallFreeCode_Object=MibTableColumn
hwChanbIsdnCallFreeCode=_HwChanbIsdnCallFreeCode_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,1,1,1,9),_HwChanbIsdnCallFreeCode_Type())
hwChanbIsdnCallFreeCode.setMaxAccess(_C)
if mibBuilder.loadTexts:hwChanbIsdnCallFreeCode.setStatus(_A)
_HwChanbIsdnCallAccept_Type=Counter32
_HwChanbIsdnCallAccept_Object=MibTableColumn
hwChanbIsdnCallAccept=_HwChanbIsdnCallAccept_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,1,1,1,10),_HwChanbIsdnCallAccept_Type())
hwChanbIsdnCallAccept.setMaxAccess(_C)
if mibBuilder.loadTexts:hwChanbIsdnCallAccept.setStatus(_A)
_HwChanbIsdnCallReject_Type=Counter32
_HwChanbIsdnCallReject_Object=MibTableColumn
hwChanbIsdnCallReject=_HwChanbIsdnCallReject_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,1,1,1,11),_HwChanbIsdnCallReject_Type())
hwChanbIsdnCallReject.setMaxAccess(_C)
if mibBuilder.loadTexts:hwChanbIsdnCallReject.setStatus(_A)
_HwChanbIsdnCallSuccess_Type=Counter32
_HwChanbIsdnCallSuccess_Object=MibTableColumn
hwChanbIsdnCallSuccess=_HwChanbIsdnCallSuccess_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,1,1,1,12),_HwChanbIsdnCallSuccess_Type())
hwChanbIsdnCallSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:hwChanbIsdnCallSuccess.setStatus(_A)
_HwChanbIsdnCallFailure_Type=Counter32
_HwChanbIsdnCallFailure_Object=MibTableColumn
hwChanbIsdnCallFailure=_HwChanbIsdnCallFailure_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,1,1,1,13),_HwChanbIsdnCallFailure_Type())
hwChanbIsdnCallFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:hwChanbIsdnCallFailure.setStatus(_A)
class _HwChanbIsdnMaxKeepTime_Type(Integer32):defaultValue=2147483647
_HwChanbIsdnMaxKeepTime_Type.__name__=_D
_HwChanbIsdnMaxKeepTime_Object=MibTableColumn
hwChanbIsdnMaxKeepTime=_HwChanbIsdnMaxKeepTime_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,1,1,1,14),_HwChanbIsdnMaxKeepTime_Type())
hwChanbIsdnMaxKeepTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwChanbIsdnMaxKeepTime.setStatus(_A)
if mibBuilder.loadTexts:hwChanbIsdnMaxKeepTime.setUnits(_P)
_HwChanbIsdnLastKeepTime_Type=Integer32
_HwChanbIsdnLastKeepTime_Object=MibTableColumn
hwChanbIsdnLastKeepTime=_HwChanbIsdnLastKeepTime_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,1,1,1,15),_HwChanbIsdnLastKeepTime_Type())
hwChanbIsdnLastKeepTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwChanbIsdnLastKeepTime.setStatus(_A)
if mibBuilder.loadTexts:hwChanbIsdnLastKeepTime.setUnits(_P)
_HwChanbIsdnLastCallTime_Type=TimeStamp
_HwChanbIsdnLastCallTime_Object=MibTableColumn
hwChanbIsdnLastCallTime=_HwChanbIsdnLastCallTime_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,1,1,1,16),_HwChanbIsdnLastCallTime_Type())
hwChanbIsdnLastCallTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hwChanbIsdnLastCallTime.setStatus(_A)
class _HwChanbTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HwChanbTrapEnable_Type.__name__=_D
_HwChanbTrapEnable_Object=MibScalar
hwChanbTrapEnable=_HwChanbTrapEnable_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,1,2),_HwChanbTrapEnable_Type())
hwChanbTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hwChanbTrapEnable.setStatus(_A)
_IsdnQ931_ObjectIdentity=ObjectIdentity
isdnQ931=_IsdnQ931_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,33,9,1,2))
_HwQ931IsdnControl_ObjectIdentity=ObjectIdentity
hwQ931IsdnControl=_HwQ931IsdnControl_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,33,9,1,2,1))
class _HwQ931CallSetupTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HwQ931CallSetupTrapEnable_Type.__name__=_D
_HwQ931CallSetupTrapEnable_Object=MibScalar
hwQ931CallSetupTrapEnable=_HwQ931CallSetupTrapEnable_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,2,1,1),_HwQ931CallSetupTrapEnable_Type())
hwQ931CallSetupTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hwQ931CallSetupTrapEnable.setStatus(_A)
class _HwQ931CallClearTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HwQ931CallClearTrapEnable_Type.__name__=_D
_HwQ931CallClearTrapEnable_Object=MibScalar
hwQ931CallClearTrapEnable=_HwQ931CallClearTrapEnable_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,2,1,2),_HwQ931CallClearTrapEnable_Type())
hwQ931CallClearTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hwQ931CallClearTrapEnable.setStatus(_A)
_HwQ931IsdnTable_Object=MibTable
hwQ931IsdnTable=_HwQ931IsdnTable_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,2,2))
if mibBuilder.loadTexts:hwQ931IsdnTable.setStatus(_A)
_HwQ931IsdnEntry_Object=MibTableRow
hwQ931IsdnEntry=_HwQ931IsdnEntry_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,2,2,1))
hwQ931IsdnEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hwQ931IsdnEntry.setStatus(_A)
_HwQ931IsdnOpIndex_Type=Integer32
_HwQ931IsdnOpIndex_Object=MibTableColumn
hwQ931IsdnOpIndex=_HwQ931IsdnOpIndex_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,2,2,1,1),_HwQ931IsdnOpIndex_Type())
hwQ931IsdnOpIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:hwQ931IsdnOpIndex.setStatus(_A)
_HwQ931IsdnLastCalled_Type=DisplayString
_HwQ931IsdnLastCalled_Object=MibTableColumn
hwQ931IsdnLastCalled=_HwQ931IsdnLastCalled_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,2,2,1,2),_HwQ931IsdnLastCalled_Type())
hwQ931IsdnLastCalled.setMaxAccess(_C)
if mibBuilder.loadTexts:hwQ931IsdnLastCalled.setStatus(_A)
_HwQ931IsdnLastCalling_Type=DisplayString
_HwQ931IsdnLastCalling_Object=MibTableColumn
hwQ931IsdnLastCalling=_HwQ931IsdnLastCalling_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,2,2,1,3),_HwQ931IsdnLastCalling_Type())
hwQ931IsdnLastCalling.setMaxAccess(_C)
if mibBuilder.loadTexts:hwQ931IsdnLastCalling.setStatus(_A)
class _HwQ931IsdnLastCauseDisc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),('normCallClr',2),('noRouteToTransNet',3),('noRouteToDest',4),('switchEquCongest',5),('netOutofOrder',6)))
_HwQ931IsdnLastCauseDisc_Type.__name__=_D
_HwQ931IsdnLastCauseDisc_Object=MibTableColumn
hwQ931IsdnLastCauseDisc=_HwQ931IsdnLastCauseDisc_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,2,2,1,4),_HwQ931IsdnLastCauseDisc_Type())
hwQ931IsdnLastCauseDisc.setMaxAccess(_C)
if mibBuilder.loadTexts:hwQ931IsdnLastCauseDisc.setStatus(_A)
class _HwQ931IsdnCallDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('incoming',1),('outgoing',2)))
_HwQ931IsdnCallDirection_Type.__name__=_D
_HwQ931IsdnCallDirection_Object=MibTableColumn
hwQ931IsdnCallDirection=_HwQ931IsdnCallDirection_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,2,2,1,5),_HwQ931IsdnCallDirection_Type())
hwQ931IsdnCallDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hwQ931IsdnCallDirection.setStatus(_A)
_HwQ931IsdnCallTimeOpen_Type=DateAndTime
_HwQ931IsdnCallTimeOpen_Object=MibTableColumn
hwQ931IsdnCallTimeOpen=_HwQ931IsdnCallTimeOpen_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,2,2,1,6),_HwQ931IsdnCallTimeOpen_Type())
hwQ931IsdnCallTimeOpen.setMaxAccess(_C)
if mibBuilder.loadTexts:hwQ931IsdnCallTimeOpen.setStatus(_A)
_HwQ931IsdnCallTimeClose_Type=DateAndTime
_HwQ931IsdnCallTimeClose_Object=MibTableColumn
hwQ931IsdnCallTimeClose=_HwQ931IsdnCallTimeClose_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,2,2,1,7),_HwQ931IsdnCallTimeClose_Type())
hwQ931IsdnCallTimeClose.setMaxAccess(_C)
if mibBuilder.loadTexts:hwQ931IsdnCallTimeClose.setStatus(_A)
_HwIsdnLapd_ObjectIdentity=ObjectIdentity
hwIsdnLapd=_HwIsdnLapd_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,33,9,1,3))
_HwLapdIsdnTable_Object=MibTable
hwLapdIsdnTable=_HwLapdIsdnTable_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,3,1))
if mibBuilder.loadTexts:hwLapdIsdnTable.setStatus(_A)
_HwLapdIsdnEntry_Object=MibTableRow
hwLapdIsdnEntry=_HwLapdIsdnEntry_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,3,1,1))
hwLapdIsdnEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:hwLapdIsdnEntry.setStatus(_A)
_HwLapdIsdnIf_Type=Integer32
_HwLapdIsdnIf_Object=MibTableColumn
hwLapdIsdnIf=_HwLapdIsdnIf_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,3,1,1,1),_HwLapdIsdnIf_Type())
hwLapdIsdnIf.setMaxAccess(_Q)
if mibBuilder.loadTexts:hwLapdIsdnIf.setStatus(_A)
class _HwLapdIsdnProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('dss1',1),('qsig',2),('etsi',3),('ess5',4),('ansi',5),('ni2',6),('ntt',7),('att',8),('ni',9)))
_HwLapdIsdnProtocol_Type.__name__=_D
_HwLapdIsdnProtocol_Object=MibTableColumn
hwLapdIsdnProtocol=_HwLapdIsdnProtocol_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,3,1,1,2),_HwLapdIsdnProtocol_Type())
hwLapdIsdnProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:hwLapdIsdnProtocol.setStatus(_A)
class _HwLapdIsdnIfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('userSide',1),('networkSide',2)))
_HwLapdIsdnIfMode_Type.__name__=_D
_HwLapdIsdnIfMode_Object=MibTableColumn
hwLapdIsdnIfMode=_HwLapdIsdnIfMode_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,3,1,1,3),_HwLapdIsdnIfMode_Type())
hwLapdIsdnIfMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hwLapdIsdnIfMode.setStatus(_A)
class _HwLapdIsdnLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inactive',1),('l1Active',2),('l2Active',3)))
_HwLapdIsdnLinkStatus_Type.__name__=_D
_HwLapdIsdnLinkStatus_Object=MibTableColumn
hwLapdIsdnLinkStatus=_HwLapdIsdnLinkStatus_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,3,1,1,4),_HwLapdIsdnLinkStatus_Type())
hwLapdIsdnLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwLapdIsdnLinkStatus.setStatus(_A)
_HwLapdIsdnControl_ObjectIdentity=ObjectIdentity
hwLapdIsdnControl=_HwLapdIsdnControl_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,33,9,1,3,2))
class _HwLapdStatusTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HwLapdStatusTrapEnable_Type.__name__=_D
_HwLapdStatusTrapEnable_Object=MibScalar
hwLapdStatusTrapEnable=_HwLapdStatusTrapEnable_Object((1,3,6,1,4,1,43,45,1,2,33,9,1,3,2,1),_HwLapdStatusTrapEnable_Type())
hwLapdStatusTrapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hwLapdStatusTrapEnable.setStatus(_A)
_HwIsdnMibTraps_ObjectIdentity=ObjectIdentity
hwIsdnMibTraps=_HwIsdnMibTraps_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,33,9,2))
hwChanbIsdnCall=NotificationType((1,3,6,1,4,1,43,45,1,2,33,9,2,1))
hwChanbIsdnCall.setObjects(*((_B,_I),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:hwChanbIsdnCall.setStatus(_A)
hwQ931IsdnCallSetup=NotificationType((1,3,6,1,4,1,43,45,1,2,33,9,2,2))
hwQ931IsdnCallSetup.setObjects(*((_B,_H),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:hwQ931IsdnCallSetup.setStatus(_A)
hwQ931IsdnCallClear=NotificationType((1,3,6,1,4,1,43,45,1,2,33,9,2,3))
hwQ931IsdnCallClear.setObjects(*((_B,_H),(_B,_K),(_B,_L),(_B,_Y),(_B,_M),(_B,_N),(_B,_Z)))
if mibBuilder.loadTexts:hwQ931IsdnCallClear.setStatus(_A)
hwLapdIsdnStatusChange=NotificationType((1,3,6,1,4,1,43,45,1,2,33,9,2,4))
hwLapdIsdnStatusChange.setObjects(*((_B,_J),(_B,_a)))
if mibBuilder.loadTexts:hwLapdIsdnStatusChange.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hwIsdnMib':hwIsdnMib,'hwIsdnMibObjects':hwIsdnMibObjects,'isdnChannelB':isdnChannelB,'hwChanbIsdnTable':hwChanbIsdnTable,'hwChanbIsdnEntry':hwChanbIsdnEntry,_I:hwChanbIsdnIf,'hwChanbIsdnPermit':hwChanbIsdnPermit,_R:hwChanbIsdnAddr,_T:hwChanbIsdnCallerAddr,_S:hwChanbIsdnCallType,_U:hwChanbIsdnInfoType,'hwChanbIsdnState':hwChanbIsdnState,_W:hwChanbIsdnCallFreeReason,_X:hwChanbIsdnCallFreeCode,'hwChanbIsdnCallAccept':hwChanbIsdnCallAccept,'hwChanbIsdnCallReject':hwChanbIsdnCallReject,'hwChanbIsdnCallSuccess':hwChanbIsdnCallSuccess,'hwChanbIsdnCallFailure':hwChanbIsdnCallFailure,'hwChanbIsdnMaxKeepTime':hwChanbIsdnMaxKeepTime,_V:hwChanbIsdnLastKeepTime,'hwChanbIsdnLastCallTime':hwChanbIsdnLastCallTime,'hwChanbTrapEnable':hwChanbTrapEnable,'isdnQ931':isdnQ931,'hwQ931IsdnControl':hwQ931IsdnControl,'hwQ931CallSetupTrapEnable':hwQ931CallSetupTrapEnable,'hwQ931CallClearTrapEnable':hwQ931CallClearTrapEnable,'hwQ931IsdnTable':hwQ931IsdnTable,'hwQ931IsdnEntry':hwQ931IsdnEntry,_H:hwQ931IsdnOpIndex,_K:hwQ931IsdnLastCalled,_L:hwQ931IsdnLastCalling,_Y:hwQ931IsdnLastCauseDisc,_M:hwQ931IsdnCallDirection,_N:hwQ931IsdnCallTimeOpen,_Z:hwQ931IsdnCallTimeClose,'hwIsdnLapd':hwIsdnLapd,'hwLapdIsdnTable':hwLapdIsdnTable,'hwLapdIsdnEntry':hwLapdIsdnEntry,_J:hwLapdIsdnIf,'hwLapdIsdnProtocol':hwLapdIsdnProtocol,'hwLapdIsdnIfMode':hwLapdIsdnIfMode,_a:hwLapdIsdnLinkStatus,'hwLapdIsdnControl':hwLapdIsdnControl,'hwLapdStatusTrapEnable':hwLapdStatusTrapEnable,'hwIsdnMibTraps':hwIsdnMibTraps,'hwChanbIsdnCall':hwChanbIsdnCall,'hwQ931IsdnCallSetup':hwQ931IsdnCallSetup,'hwQ931IsdnCallClear':hwQ931IsdnCallClear,'hwLapdIsdnStatusChange':hwLapdIsdnStatusChange})