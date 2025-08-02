_X='fddimibPORTIndex'
_W='fddimibPORTSMTIndex'
_V='fddimibPATHConfigTokenOrder'
_U='fddimibPATHConfigPATHIndex'
_T='fddimibPATHConfigSMTIndex'
_S='fddimibPATHIndex'
_R='fddimibPATHSMTIndex'
_Q='primary'
_P='secondary'
_O='isolated'
_N='fddimibSMTIndex'
_M='fddimibMACIndex'
_L='fddimibMACSMTIndex'
_K='thru'
_J='concatenated'
_I='OctetString'
_H='none'
_G='FDDI-SMT73-MIB'
_F='false'
_E='true'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class FddiTimeNano(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class FddiTimeMilli(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class FddiResourceId(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class FddiSMTStationIdType(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class FddiMACLongAddressType(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_Fddi_ObjectIdentity=ObjectIdentity
fddi=_Fddi_ObjectIdentity((1,3,6,1,2,1,10,15))
_Fddimib_ObjectIdentity=ObjectIdentity
fddimib=_Fddimib_ObjectIdentity((1,3,6,1,2,1,10,15,73))
_FddimibSMT_ObjectIdentity=ObjectIdentity
fddimibSMT=_FddimibSMT_ObjectIdentity((1,3,6,1,2,1,10,15,73,1))
class _FddimibSMTNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FddimibSMTNumber_Type.__name__=_C
_FddimibSMTNumber_Object=MibScalar
fddimibSMTNumber=_FddimibSMTNumber_Object((1,3,6,1,2,1,10,15,73,1,1),_FddimibSMTNumber_Type())
fddimibSMTNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibSMTNumber.setStatus(_A)
_FddimibSMTTable_Object=MibTable
fddimibSMTTable=_FddimibSMTTable_Object((1,3,6,1,2,1,10,15,73,1,2))
if mibBuilder.loadTexts:fddimibSMTTable.setStatus(_A)
_FddimibSMTEntry_Object=MibTableRow
fddimibSMTEntry=_FddimibSMTEntry_Object((1,3,6,1,2,1,10,15,73,1,2,1))
fddimibSMTEntry.setIndexNames((0,_G,_N))
if mibBuilder.loadTexts:fddimibSMTEntry.setStatus(_A)
class _FddimibSMTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FddimibSMTIndex_Type.__name__=_C
_FddimibSMTIndex_Object=MibTableColumn
fddimibSMTIndex=_FddimibSMTIndex_Object((1,3,6,1,2,1,10,15,73,1,2,1,1),_FddimibSMTIndex_Type())
fddimibSMTIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibSMTIndex.setStatus(_A)
_FddimibSMTStationId_Type=FddiSMTStationIdType
_FddimibSMTStationId_Object=MibTableColumn
fddimibSMTStationId=_FddimibSMTStationId_Object((1,3,6,1,2,1,10,15,73,1,2,1,2),_FddimibSMTStationId_Type())
fddimibSMTStationId.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibSMTStationId.setStatus(_A)
class _FddimibSMTOpVersionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FddimibSMTOpVersionId_Type.__name__=_C
_FddimibSMTOpVersionId_Object=MibTableColumn
fddimibSMTOpVersionId=_FddimibSMTOpVersionId_Object((1,3,6,1,2,1,10,15,73,1,2,1,3),_FddimibSMTOpVersionId_Type())
fddimibSMTOpVersionId.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibSMTOpVersionId.setStatus(_A)
class _FddimibSMTHiVersionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FddimibSMTHiVersionId_Type.__name__=_C
_FddimibSMTHiVersionId_Object=MibTableColumn
fddimibSMTHiVersionId=_FddimibSMTHiVersionId_Object((1,3,6,1,2,1,10,15,73,1,2,1,4),_FddimibSMTHiVersionId_Type())
fddimibSMTHiVersionId.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibSMTHiVersionId.setStatus(_A)
class _FddimibSMTLoVersionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FddimibSMTLoVersionId_Type.__name__=_C
_FddimibSMTLoVersionId_Object=MibTableColumn
fddimibSMTLoVersionId=_FddimibSMTLoVersionId_Object((1,3,6,1,2,1,10,15,73,1,2,1,5),_FddimibSMTLoVersionId_Type())
fddimibSMTLoVersionId.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibSMTLoVersionId.setStatus(_A)
class _FddimibSMTUserData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_FddimibSMTUserData_Type.__name__=_I
_FddimibSMTUserData_Object=MibTableColumn
fddimibSMTUserData=_FddimibSMTUserData_Object((1,3,6,1,2,1,10,15,73,1,2,1,6),_FddimibSMTUserData_Type())
fddimibSMTUserData.setMaxAccess(_D)
if mibBuilder.loadTexts:fddimibSMTUserData.setStatus(_A)
class _FddimibSMTMIBVersionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FddimibSMTMIBVersionId_Type.__name__=_C
_FddimibSMTMIBVersionId_Object=MibTableColumn
fddimibSMTMIBVersionId=_FddimibSMTMIBVersionId_Object((1,3,6,1,2,1,10,15,73,1,2,1,7),_FddimibSMTMIBVersionId_Type())
fddimibSMTMIBVersionId.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibSMTMIBVersionId.setStatus(_A)
class _FddimibSMTMACCts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FddimibSMTMACCts_Type.__name__=_C
_FddimibSMTMACCts_Object=MibTableColumn
fddimibSMTMACCts=_FddimibSMTMACCts_Object((1,3,6,1,2,1,10,15,73,1,2,1,8),_FddimibSMTMACCts_Type())
fddimibSMTMACCts.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibSMTMACCts.setStatus(_A)
class _FddimibSMTNonMasterCts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_FddimibSMTNonMasterCts_Type.__name__=_C
_FddimibSMTNonMasterCts_Object=MibTableColumn
fddimibSMTNonMasterCts=_FddimibSMTNonMasterCts_Object((1,3,6,1,2,1,10,15,73,1,2,1,9),_FddimibSMTNonMasterCts_Type())
fddimibSMTNonMasterCts.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibSMTNonMasterCts.setStatus(_A)
class _FddimibSMTMasterCts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FddimibSMTMasterCts_Type.__name__=_C
_FddimibSMTMasterCts_Object=MibTableColumn
fddimibSMTMasterCts=_FddimibSMTMasterCts_Object((1,3,6,1,2,1,10,15,73,1,2,1,10),_FddimibSMTMasterCts_Type())
fddimibSMTMasterCts.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibSMTMasterCts.setStatus(_A)
class _FddimibSMTAvailablePaths_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FddimibSMTAvailablePaths_Type.__name__=_C
_FddimibSMTAvailablePaths_Object=MibTableColumn
fddimibSMTAvailablePaths=_FddimibSMTAvailablePaths_Object((1,3,6,1,2,1,10,15,73,1,2,1,11),_FddimibSMTAvailablePaths_Type())
fddimibSMTAvailablePaths.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibSMTAvailablePaths.setStatus(_A)
class _FddimibSMTConfigCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_FddimibSMTConfigCapabilities_Type.__name__=_C
_FddimibSMTConfigCapabilities_Object=MibTableColumn
fddimibSMTConfigCapabilities=_FddimibSMTConfigCapabilities_Object((1,3,6,1,2,1,10,15,73,1,2,1,12),_FddimibSMTConfigCapabilities_Type())
fddimibSMTConfigCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibSMTConfigCapabilities.setStatus(_A)
class _FddimibSMTConfigPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FddimibSMTConfigPolicy_Type.__name__=_C
_FddimibSMTConfigPolicy_Object=MibTableColumn
fddimibSMTConfigPolicy=_FddimibSMTConfigPolicy_Object((1,3,6,1,2,1,10,15,73,1,2,1,13),_FddimibSMTConfigPolicy_Type())
fddimibSMTConfigPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:fddimibSMTConfigPolicy.setStatus(_A)
class _FddimibSMTConnectionPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32768,65535))
_FddimibSMTConnectionPolicy_Type.__name__=_C
_FddimibSMTConnectionPolicy_Object=MibTableColumn
fddimibSMTConnectionPolicy=_FddimibSMTConnectionPolicy_Object((1,3,6,1,2,1,10,15,73,1,2,1,14),_FddimibSMTConnectionPolicy_Type())
fddimibSMTConnectionPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:fddimibSMTConnectionPolicy.setStatus(_A)
class _FddimibSMTTNotify_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,30))
_FddimibSMTTNotify_Type.__name__=_C
_FddimibSMTTNotify_Object=MibTableColumn
fddimibSMTTNotify=_FddimibSMTTNotify_Object((1,3,6,1,2,1,10,15,73,1,2,1,15),_FddimibSMTTNotify_Type())
fddimibSMTTNotify.setMaxAccess(_D)
if mibBuilder.loadTexts:fddimibSMTTNotify.setStatus(_A)
class _FddimibSMTStatRptPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FddimibSMTStatRptPolicy_Type.__name__=_C
_FddimibSMTStatRptPolicy_Object=MibTableColumn
fddimibSMTStatRptPolicy=_FddimibSMTStatRptPolicy_Object((1,3,6,1,2,1,10,15,73,1,2,1,16),_FddimibSMTStatRptPolicy_Type())
fddimibSMTStatRptPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:fddimibSMTStatRptPolicy.setStatus(_A)
_FddimibSMTTraceMaxExpiration_Type=FddiTimeMilli
_FddimibSMTTraceMaxExpiration_Object=MibTableColumn
fddimibSMTTraceMaxExpiration=_FddimibSMTTraceMaxExpiration_Object((1,3,6,1,2,1,10,15,73,1,2,1,17),_FddimibSMTTraceMaxExpiration_Type())
fddimibSMTTraceMaxExpiration.setMaxAccess(_D)
if mibBuilder.loadTexts:fddimibSMTTraceMaxExpiration.setStatus(_A)
class _FddimibSMTBypassPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FddimibSMTBypassPresent_Type.__name__=_C
_FddimibSMTBypassPresent_Object=MibTableColumn
fddimibSMTBypassPresent=_FddimibSMTBypassPresent_Object((1,3,6,1,2,1,10,15,73,1,2,1,18),_FddimibSMTBypassPresent_Type())
fddimibSMTBypassPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibSMTBypassPresent.setStatus(_A)
class _FddimibSMTECMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('ec0',1),('ec1',2),('ec2',3),('ec3',4),('ec4',5),('ec5',6),('ec6',7),('ec7',8)))
_FddimibSMTECMState_Type.__name__=_C
_FddimibSMTECMState_Object=MibTableColumn
fddimibSMTECMState=_FddimibSMTECMState_Object((1,3,6,1,2,1,10,15,73,1,2,1,19),_FddimibSMTECMState_Type())
fddimibSMTECMState.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibSMTECMState.setStatus(_A)
class _FddimibSMTCFState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('cf0',1),('cf1',2),('cf2',3),('cf3',4),('cf4',5),('cf5',6),('cf6',7),('cf7',8),('cf8',9),('cf9',10),('cf10',11),('cf11',12),('cf12',13)))
_FddimibSMTCFState_Type.__name__=_C
_FddimibSMTCFState_Object=MibTableColumn
fddimibSMTCFState=_FddimibSMTCFState_Object((1,3,6,1,2,1,10,15,73,1,2,1,20),_FddimibSMTCFState_Type())
fddimibSMTCFState.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibSMTCFState.setStatus(_A)
class _FddimibSMTRemoteDisconnectFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FddimibSMTRemoteDisconnectFlag_Type.__name__=_C
_FddimibSMTRemoteDisconnectFlag_Object=MibTableColumn
fddimibSMTRemoteDisconnectFlag=_FddimibSMTRemoteDisconnectFlag_Object((1,3,6,1,2,1,10,15,73,1,2,1,21),_FddimibSMTRemoteDisconnectFlag_Type())
fddimibSMTRemoteDisconnectFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibSMTRemoteDisconnectFlag.setStatus(_A)
class _FddimibSMTStationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('separated',2),(_K,3)))
_FddimibSMTStationStatus_Type.__name__=_C
_FddimibSMTStationStatus_Object=MibTableColumn
fddimibSMTStationStatus=_FddimibSMTStationStatus_Object((1,3,6,1,2,1,10,15,73,1,2,1,22),_FddimibSMTStationStatus_Type())
fddimibSMTStationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibSMTStationStatus.setStatus(_A)
class _FddimibSMTPeerWrapFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FddimibSMTPeerWrapFlag_Type.__name__=_C
_FddimibSMTPeerWrapFlag_Object=MibTableColumn
fddimibSMTPeerWrapFlag=_FddimibSMTPeerWrapFlag_Object((1,3,6,1,2,1,10,15,73,1,2,1,23),_FddimibSMTPeerWrapFlag_Type())
fddimibSMTPeerWrapFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibSMTPeerWrapFlag.setStatus(_A)
_FddimibSMTTimeStamp_Type=FddiTimeMilli
_FddimibSMTTimeStamp_Object=MibTableColumn
fddimibSMTTimeStamp=_FddimibSMTTimeStamp_Object((1,3,6,1,2,1,10,15,73,1,2,1,24),_FddimibSMTTimeStamp_Type())
fddimibSMTTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibSMTTimeStamp.setStatus(_A)
_FddimibSMTTransitionTimeStamp_Type=FddiTimeMilli
_FddimibSMTTransitionTimeStamp_Object=MibTableColumn
fddimibSMTTransitionTimeStamp=_FddimibSMTTransitionTimeStamp_Object((1,3,6,1,2,1,10,15,73,1,2,1,25),_FddimibSMTTransitionTimeStamp_Type())
fddimibSMTTransitionTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibSMTTransitionTimeStamp.setStatus(_A)
class _FddimibSMTStationAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('other',1),('connect',2),('disconnect',3),('path-Test',4),('self-Test',5),('disable-a',6),('disable-b',7),('disable-m',8)))
_FddimibSMTStationAction_Type.__name__=_C
_FddimibSMTStationAction_Object=MibTableColumn
fddimibSMTStationAction=_FddimibSMTStationAction_Object((1,3,6,1,2,1,10,15,73,1,2,1,26),_FddimibSMTStationAction_Type())
fddimibSMTStationAction.setMaxAccess(_D)
if mibBuilder.loadTexts:fddimibSMTStationAction.setStatus(_A)
_FddimibMAC_ObjectIdentity=ObjectIdentity
fddimibMAC=_FddimibMAC_ObjectIdentity((1,3,6,1,2,1,10,15,73,2))
class _FddimibMACNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FddimibMACNumber_Type.__name__=_C
_FddimibMACNumber_Object=MibScalar
fddimibMACNumber=_FddimibMACNumber_Object((1,3,6,1,2,1,10,15,73,2,1),_FddimibMACNumber_Type())
fddimibMACNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACNumber.setStatus(_A)
_FddimibMACTable_Object=MibTable
fddimibMACTable=_FddimibMACTable_Object((1,3,6,1,2,1,10,15,73,2,2))
if mibBuilder.loadTexts:fddimibMACTable.setStatus(_A)
_FddimibMACEntry_Object=MibTableRow
fddimibMACEntry=_FddimibMACEntry_Object((1,3,6,1,2,1,10,15,73,2,2,1))
fddimibMACEntry.setIndexNames((0,_G,_L),(0,_G,_M))
if mibBuilder.loadTexts:fddimibMACEntry.setStatus(_A)
class _FddimibMACSMTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FddimibMACSMTIndex_Type.__name__=_C
_FddimibMACSMTIndex_Object=MibTableColumn
fddimibMACSMTIndex=_FddimibMACSMTIndex_Object((1,3,6,1,2,1,10,15,73,2,2,1,1),_FddimibMACSMTIndex_Type())
fddimibMACSMTIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACSMTIndex.setStatus(_A)
class _FddimibMACIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FddimibMACIndex_Type.__name__=_C
_FddimibMACIndex_Object=MibTableColumn
fddimibMACIndex=_FddimibMACIndex_Object((1,3,6,1,2,1,10,15,73,2,2,1,2),_FddimibMACIndex_Type())
fddimibMACIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACIndex.setStatus(_A)
class _FddimibMACIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FddimibMACIfIndex_Type.__name__=_C
_FddimibMACIfIndex_Object=MibTableColumn
fddimibMACIfIndex=_FddimibMACIfIndex_Object((1,3,6,1,2,1,10,15,73,2,2,1,3),_FddimibMACIfIndex_Type())
fddimibMACIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACIfIndex.setStatus(_A)
class _FddimibMACFrameStatusFunctions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FddimibMACFrameStatusFunctions_Type.__name__=_C
_FddimibMACFrameStatusFunctions_Object=MibTableColumn
fddimibMACFrameStatusFunctions=_FddimibMACFrameStatusFunctions_Object((1,3,6,1,2,1,10,15,73,2,2,1,4),_FddimibMACFrameStatusFunctions_Type())
fddimibMACFrameStatusFunctions.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACFrameStatusFunctions.setStatus(_A)
_FddimibMACTMaxCapability_Type=FddiTimeNano
_FddimibMACTMaxCapability_Object=MibTableColumn
fddimibMACTMaxCapability=_FddimibMACTMaxCapability_Object((1,3,6,1,2,1,10,15,73,2,2,1,5),_FddimibMACTMaxCapability_Type())
fddimibMACTMaxCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACTMaxCapability.setStatus(_A)
_FddimibMACTVXCapability_Type=FddiTimeNano
_FddimibMACTVXCapability_Object=MibTableColumn
fddimibMACTVXCapability=_FddimibMACTVXCapability_Object((1,3,6,1,2,1,10,15,73,2,2,1,6),_FddimibMACTVXCapability_Type())
fddimibMACTVXCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACTVXCapability.setStatus(_A)
class _FddimibMACAvailablePaths_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FddimibMACAvailablePaths_Type.__name__=_C
_FddimibMACAvailablePaths_Object=MibTableColumn
fddimibMACAvailablePaths=_FddimibMACAvailablePaths_Object((1,3,6,1,2,1,10,15,73,2,2,1,7),_FddimibMACAvailablePaths_Type())
fddimibMACAvailablePaths.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACAvailablePaths.setStatus(_A)
class _FddimibMACCurrentPath_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),('local',2),(_P,3),(_Q,4),(_J,5),(_K,6)))
_FddimibMACCurrentPath_Type.__name__=_C
_FddimibMACCurrentPath_Object=MibTableColumn
fddimibMACCurrentPath=_FddimibMACCurrentPath_Object((1,3,6,1,2,1,10,15,73,2,2,1,8),_FddimibMACCurrentPath_Type())
fddimibMACCurrentPath.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACCurrentPath.setStatus(_A)
_FddimibMACUpstreamNbr_Type=FddiMACLongAddressType
_FddimibMACUpstreamNbr_Object=MibTableColumn
fddimibMACUpstreamNbr=_FddimibMACUpstreamNbr_Object((1,3,6,1,2,1,10,15,73,2,2,1,9),_FddimibMACUpstreamNbr_Type())
fddimibMACUpstreamNbr.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACUpstreamNbr.setStatus(_A)
_FddimibMACDownstreamNbr_Type=FddiMACLongAddressType
_FddimibMACDownstreamNbr_Object=MibTableColumn
fddimibMACDownstreamNbr=_FddimibMACDownstreamNbr_Object((1,3,6,1,2,1,10,15,73,2,2,1,10),_FddimibMACDownstreamNbr_Type())
fddimibMACDownstreamNbr.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACDownstreamNbr.setStatus(_A)
_FddimibMACOldUpstreamNbr_Type=FddiMACLongAddressType
_FddimibMACOldUpstreamNbr_Object=MibTableColumn
fddimibMACOldUpstreamNbr=_FddimibMACOldUpstreamNbr_Object((1,3,6,1,2,1,10,15,73,2,2,1,11),_FddimibMACOldUpstreamNbr_Type())
fddimibMACOldUpstreamNbr.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACOldUpstreamNbr.setStatus(_A)
_FddimibMACOldDownstreamNbr_Type=FddiMACLongAddressType
_FddimibMACOldDownstreamNbr_Object=MibTableColumn
fddimibMACOldDownstreamNbr=_FddimibMACOldDownstreamNbr_Object((1,3,6,1,2,1,10,15,73,2,2,1,12),_FddimibMACOldDownstreamNbr_Type())
fddimibMACOldDownstreamNbr.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACOldDownstreamNbr.setStatus(_A)
class _FddimibMACDupAddressTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('pass',2),('fail',3)))
_FddimibMACDupAddressTest_Type.__name__=_C
_FddimibMACDupAddressTest_Object=MibTableColumn
fddimibMACDupAddressTest=_FddimibMACDupAddressTest_Object((1,3,6,1,2,1,10,15,73,2,2,1,13),_FddimibMACDupAddressTest_Type())
fddimibMACDupAddressTest.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACDupAddressTest.setStatus(_A)
class _FddimibMACRequestedPaths_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FddimibMACRequestedPaths_Type.__name__=_C
_FddimibMACRequestedPaths_Object=MibTableColumn
fddimibMACRequestedPaths=_FddimibMACRequestedPaths_Object((1,3,6,1,2,1,10,15,73,2,2,1,14),_FddimibMACRequestedPaths_Type())
fddimibMACRequestedPaths.setMaxAccess(_D)
if mibBuilder.loadTexts:fddimibMACRequestedPaths.setStatus(_A)
class _FddimibMACDownstreamPORTType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('a',1),('b',2),('s',3),('m',4),(_H,5)))
_FddimibMACDownstreamPORTType_Type.__name__=_C
_FddimibMACDownstreamPORTType_Object=MibTableColumn
fddimibMACDownstreamPORTType=_FddimibMACDownstreamPORTType_Object((1,3,6,1,2,1,10,15,73,2,2,1,15),_FddimibMACDownstreamPORTType_Type())
fddimibMACDownstreamPORTType.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACDownstreamPORTType.setStatus(_A)
_FddimibMACSMTAddress_Type=FddiMACLongAddressType
_FddimibMACSMTAddress_Object=MibTableColumn
fddimibMACSMTAddress=_FddimibMACSMTAddress_Object((1,3,6,1,2,1,10,15,73,2,2,1,16),_FddimibMACSMTAddress_Type())
fddimibMACSMTAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACSMTAddress.setStatus(_A)
_FddimibMACTReq_Type=FddiTimeNano
_FddimibMACTReq_Object=MibTableColumn
fddimibMACTReq=_FddimibMACTReq_Object((1,3,6,1,2,1,10,15,73,2,2,1,17),_FddimibMACTReq_Type())
fddimibMACTReq.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACTReq.setStatus(_A)
_FddimibMACTNeg_Type=FddiTimeNano
_FddimibMACTNeg_Object=MibTableColumn
fddimibMACTNeg=_FddimibMACTNeg_Object((1,3,6,1,2,1,10,15,73,2,2,1,18),_FddimibMACTNeg_Type())
fddimibMACTNeg.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACTNeg.setStatus(_A)
_FddimibMACTMax_Type=FddiTimeNano
_FddimibMACTMax_Object=MibTableColumn
fddimibMACTMax=_FddimibMACTMax_Object((1,3,6,1,2,1,10,15,73,2,2,1,19),_FddimibMACTMax_Type())
fddimibMACTMax.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACTMax.setStatus(_A)
_FddimibMACTvxValue_Type=FddiTimeNano
_FddimibMACTvxValue_Object=MibTableColumn
fddimibMACTvxValue=_FddimibMACTvxValue_Object((1,3,6,1,2,1,10,15,73,2,2,1,20),_FddimibMACTvxValue_Type())
fddimibMACTvxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACTvxValue.setStatus(_A)
_FddimibMACFrameCts_Type=Counter32
_FddimibMACFrameCts_Object=MibTableColumn
fddimibMACFrameCts=_FddimibMACFrameCts_Object((1,3,6,1,2,1,10,15,73,2,2,1,21),_FddimibMACFrameCts_Type())
fddimibMACFrameCts.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACFrameCts.setStatus(_A)
_FddimibMACCopiedCts_Type=Counter32
_FddimibMACCopiedCts_Object=MibTableColumn
fddimibMACCopiedCts=_FddimibMACCopiedCts_Object((1,3,6,1,2,1,10,15,73,2,2,1,22),_FddimibMACCopiedCts_Type())
fddimibMACCopiedCts.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACCopiedCts.setStatus(_A)
_FddimibMACTransmitCts_Type=Counter32
_FddimibMACTransmitCts_Object=MibTableColumn
fddimibMACTransmitCts=_FddimibMACTransmitCts_Object((1,3,6,1,2,1,10,15,73,2,2,1,23),_FddimibMACTransmitCts_Type())
fddimibMACTransmitCts.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACTransmitCts.setStatus(_A)
_FddimibMACErrorCts_Type=Counter32
_FddimibMACErrorCts_Object=MibTableColumn
fddimibMACErrorCts=_FddimibMACErrorCts_Object((1,3,6,1,2,1,10,15,73,2,2,1,24),_FddimibMACErrorCts_Type())
fddimibMACErrorCts.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACErrorCts.setStatus(_A)
_FddimibMACLostCts_Type=Counter32
_FddimibMACLostCts_Object=MibTableColumn
fddimibMACLostCts=_FddimibMACLostCts_Object((1,3,6,1,2,1,10,15,73,2,2,1,25),_FddimibMACLostCts_Type())
fddimibMACLostCts.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACLostCts.setStatus(_A)
class _FddimibMACFrameErrorThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FddimibMACFrameErrorThreshold_Type.__name__=_C
_FddimibMACFrameErrorThreshold_Object=MibTableColumn
fddimibMACFrameErrorThreshold=_FddimibMACFrameErrorThreshold_Object((1,3,6,1,2,1,10,15,73,2,2,1,26),_FddimibMACFrameErrorThreshold_Type())
fddimibMACFrameErrorThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:fddimibMACFrameErrorThreshold.setStatus(_A)
class _FddimibMACFrameErrorRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FddimibMACFrameErrorRatio_Type.__name__=_C
_FddimibMACFrameErrorRatio_Object=MibTableColumn
fddimibMACFrameErrorRatio=_FddimibMACFrameErrorRatio_Object((1,3,6,1,2,1,10,15,73,2,2,1,27),_FddimibMACFrameErrorRatio_Type())
fddimibMACFrameErrorRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACFrameErrorRatio.setStatus(_A)
class _FddimibMACRMTState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('rm0',1),('rm1',2),('rm2',3),('rm3',4),('rm4',5),('rm5',6),('rm6',7),('rm7',8)))
_FddimibMACRMTState_Type.__name__=_C
_FddimibMACRMTState_Object=MibTableColumn
fddimibMACRMTState=_FddimibMACRMTState_Object((1,3,6,1,2,1,10,15,73,2,2,1,28),_FddimibMACRMTState_Type())
fddimibMACRMTState.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACRMTState.setStatus(_A)
class _FddimibMACDaFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FddimibMACDaFlag_Type.__name__=_C
_FddimibMACDaFlag_Object=MibTableColumn
fddimibMACDaFlag=_FddimibMACDaFlag_Object((1,3,6,1,2,1,10,15,73,2,2,1,29),_FddimibMACDaFlag_Type())
fddimibMACDaFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACDaFlag.setStatus(_A)
class _FddimibMACUnaDaFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FddimibMACUnaDaFlag_Type.__name__=_C
_FddimibMACUnaDaFlag_Object=MibTableColumn
fddimibMACUnaDaFlag=_FddimibMACUnaDaFlag_Object((1,3,6,1,2,1,10,15,73,2,2,1,30),_FddimibMACUnaDaFlag_Type())
fddimibMACUnaDaFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACUnaDaFlag.setStatus(_A)
class _FddimibMACFrameErrorFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FddimibMACFrameErrorFlag_Type.__name__=_C
_FddimibMACFrameErrorFlag_Object=MibTableColumn
fddimibMACFrameErrorFlag=_FddimibMACFrameErrorFlag_Object((1,3,6,1,2,1,10,15,73,2,2,1,31),_FddimibMACFrameErrorFlag_Type())
fddimibMACFrameErrorFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACFrameErrorFlag.setStatus(_A)
class _FddimibMACMAUnitdataAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FddimibMACMAUnitdataAvailable_Type.__name__=_C
_FddimibMACMAUnitdataAvailable_Object=MibTableColumn
fddimibMACMAUnitdataAvailable=_FddimibMACMAUnitdataAvailable_Object((1,3,6,1,2,1,10,15,73,2,2,1,32),_FddimibMACMAUnitdataAvailable_Type())
fddimibMACMAUnitdataAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACMAUnitdataAvailable.setStatus(_A)
class _FddimibMACHardwarePresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FddimibMACHardwarePresent_Type.__name__=_C
_FddimibMACHardwarePresent_Object=MibTableColumn
fddimibMACHardwarePresent=_FddimibMACHardwarePresent_Object((1,3,6,1,2,1,10,15,73,2,2,1,33),_FddimibMACHardwarePresent_Type())
fddimibMACHardwarePresent.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACHardwarePresent.setStatus(_A)
class _FddimibMACMAUnitdataEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FddimibMACMAUnitdataEnable_Type.__name__=_C
_FddimibMACMAUnitdataEnable_Object=MibTableColumn
fddimibMACMAUnitdataEnable=_FddimibMACMAUnitdataEnable_Object((1,3,6,1,2,1,10,15,73,2,2,1,34),_FddimibMACMAUnitdataEnable_Type())
fddimibMACMAUnitdataEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:fddimibMACMAUnitdataEnable.setStatus(_A)
_FddimibMACCounters_ObjectIdentity=ObjectIdentity
fddimibMACCounters=_FddimibMACCounters_ObjectIdentity((1,3,6,1,2,1,10,15,73,3))
_FddimibMACCountersTable_Object=MibTable
fddimibMACCountersTable=_FddimibMACCountersTable_Object((1,3,6,1,2,1,10,15,73,3,1))
if mibBuilder.loadTexts:fddimibMACCountersTable.setStatus(_A)
_FddimibMACCountersEntry_Object=MibTableRow
fddimibMACCountersEntry=_FddimibMACCountersEntry_Object((1,3,6,1,2,1,10,15,73,3,1,1))
fddimibMACCountersEntry.setIndexNames((0,_G,_L),(0,_G,_M))
if mibBuilder.loadTexts:fddimibMACCountersEntry.setStatus(_A)
_FddimibMACTokenCts_Type=Counter32
_FddimibMACTokenCts_Object=MibTableColumn
fddimibMACTokenCts=_FddimibMACTokenCts_Object((1,3,6,1,2,1,10,15,73,3,1,1,1),_FddimibMACTokenCts_Type())
fddimibMACTokenCts.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACTokenCts.setStatus(_A)
_FddimibMACTvxExpiredCts_Type=Counter32
_FddimibMACTvxExpiredCts_Object=MibTableColumn
fddimibMACTvxExpiredCts=_FddimibMACTvxExpiredCts_Object((1,3,6,1,2,1,10,15,73,3,1,1,2),_FddimibMACTvxExpiredCts_Type())
fddimibMACTvxExpiredCts.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACTvxExpiredCts.setStatus(_A)
_FddimibMACNotCopiedCts_Type=Counter32
_FddimibMACNotCopiedCts_Object=MibTableColumn
fddimibMACNotCopiedCts=_FddimibMACNotCopiedCts_Object((1,3,6,1,2,1,10,15,73,3,1,1,3),_FddimibMACNotCopiedCts_Type())
fddimibMACNotCopiedCts.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACNotCopiedCts.setStatus(_A)
_FddimibMACLateCts_Type=Counter32
_FddimibMACLateCts_Object=MibTableColumn
fddimibMACLateCts=_FddimibMACLateCts_Object((1,3,6,1,2,1,10,15,73,3,1,1,4),_FddimibMACLateCts_Type())
fddimibMACLateCts.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACLateCts.setStatus(_A)
_FddimibMACRingOpCts_Type=Counter32
_FddimibMACRingOpCts_Object=MibTableColumn
fddimibMACRingOpCts=_FddimibMACRingOpCts_Object((1,3,6,1,2,1,10,15,73,3,1,1,5),_FddimibMACRingOpCts_Type())
fddimibMACRingOpCts.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACRingOpCts.setStatus(_A)
class _FddimibMACNotCopiedRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FddimibMACNotCopiedRatio_Type.__name__=_C
_FddimibMACNotCopiedRatio_Object=MibTableColumn
fddimibMACNotCopiedRatio=_FddimibMACNotCopiedRatio_Object((1,3,6,1,2,1,10,15,73,3,1,1,6),_FddimibMACNotCopiedRatio_Type())
fddimibMACNotCopiedRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACNotCopiedRatio.setStatus(_A)
class _FddimibMACNotCopiedFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FddimibMACNotCopiedFlag_Type.__name__=_C
_FddimibMACNotCopiedFlag_Object=MibTableColumn
fddimibMACNotCopiedFlag=_FddimibMACNotCopiedFlag_Object((1,3,6,1,2,1,10,15,73,3,1,1,7),_FddimibMACNotCopiedFlag_Type())
fddimibMACNotCopiedFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibMACNotCopiedFlag.setStatus(_A)
class _FddimibMACNotCopiedThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FddimibMACNotCopiedThreshold_Type.__name__=_C
_FddimibMACNotCopiedThreshold_Object=MibTableColumn
fddimibMACNotCopiedThreshold=_FddimibMACNotCopiedThreshold_Object((1,3,6,1,2,1,10,15,73,3,1,1,8),_FddimibMACNotCopiedThreshold_Type())
fddimibMACNotCopiedThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:fddimibMACNotCopiedThreshold.setStatus(_A)
_FddimibPATH_ObjectIdentity=ObjectIdentity
fddimibPATH=_FddimibPATH_ObjectIdentity((1,3,6,1,2,1,10,15,73,4))
class _FddimibPATHNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FddimibPATHNumber_Type.__name__=_C
_FddimibPATHNumber_Object=MibScalar
fddimibPATHNumber=_FddimibPATHNumber_Object((1,3,6,1,2,1,10,15,73,4,1),_FddimibPATHNumber_Type())
fddimibPATHNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPATHNumber.setStatus(_A)
_FddimibPATHTable_Object=MibTable
fddimibPATHTable=_FddimibPATHTable_Object((1,3,6,1,2,1,10,15,73,4,2))
if mibBuilder.loadTexts:fddimibPATHTable.setStatus(_A)
_FddimibPATHEntry_Object=MibTableRow
fddimibPATHEntry=_FddimibPATHEntry_Object((1,3,6,1,2,1,10,15,73,4,2,1))
fddimibPATHEntry.setIndexNames((0,_G,_R),(0,_G,_S))
if mibBuilder.loadTexts:fddimibPATHEntry.setStatus(_A)
class _FddimibPATHSMTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FddimibPATHSMTIndex_Type.__name__=_C
_FddimibPATHSMTIndex_Object=MibTableColumn
fddimibPATHSMTIndex=_FddimibPATHSMTIndex_Object((1,3,6,1,2,1,10,15,73,4,2,1,1),_FddimibPATHSMTIndex_Type())
fddimibPATHSMTIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPATHSMTIndex.setStatus(_A)
class _FddimibPATHIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FddimibPATHIndex_Type.__name__=_C
_FddimibPATHIndex_Object=MibTableColumn
fddimibPATHIndex=_FddimibPATHIndex_Object((1,3,6,1,2,1,10,15,73,4,2,1,2),_FddimibPATHIndex_Type())
fddimibPATHIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPATHIndex.setStatus(_A)
_FddimibPATHTVXLowerBound_Type=FddiTimeNano
_FddimibPATHTVXLowerBound_Object=MibTableColumn
fddimibPATHTVXLowerBound=_FddimibPATHTVXLowerBound_Object((1,3,6,1,2,1,10,15,73,4,2,1,3),_FddimibPATHTVXLowerBound_Type())
fddimibPATHTVXLowerBound.setMaxAccess(_D)
if mibBuilder.loadTexts:fddimibPATHTVXLowerBound.setStatus(_A)
_FddimibPATHTMaxLowerBound_Type=FddiTimeNano
_FddimibPATHTMaxLowerBound_Object=MibTableColumn
fddimibPATHTMaxLowerBound=_FddimibPATHTMaxLowerBound_Object((1,3,6,1,2,1,10,15,73,4,2,1,4),_FddimibPATHTMaxLowerBound_Type())
fddimibPATHTMaxLowerBound.setMaxAccess(_D)
if mibBuilder.loadTexts:fddimibPATHTMaxLowerBound.setStatus(_A)
_FddimibPATHMaxTReq_Type=FddiTimeNano
_FddimibPATHMaxTReq_Object=MibTableColumn
fddimibPATHMaxTReq=_FddimibPATHMaxTReq_Object((1,3,6,1,2,1,10,15,73,4,2,1,5),_FddimibPATHMaxTReq_Type())
fddimibPATHMaxTReq.setMaxAccess(_D)
if mibBuilder.loadTexts:fddimibPATHMaxTReq.setStatus(_A)
_FddimibPATHConfigTable_Object=MibTable
fddimibPATHConfigTable=_FddimibPATHConfigTable_Object((1,3,6,1,2,1,10,15,73,4,3))
if mibBuilder.loadTexts:fddimibPATHConfigTable.setStatus(_A)
_FddimibPATHConfigEntry_Object=MibTableRow
fddimibPATHConfigEntry=_FddimibPATHConfigEntry_Object((1,3,6,1,2,1,10,15,73,4,3,1))
fddimibPATHConfigEntry.setIndexNames((0,_G,_T),(0,_G,_U),(0,_G,_V))
if mibBuilder.loadTexts:fddimibPATHConfigEntry.setStatus(_A)
class _FddimibPATHConfigSMTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FddimibPATHConfigSMTIndex_Type.__name__=_C
_FddimibPATHConfigSMTIndex_Object=MibTableColumn
fddimibPATHConfigSMTIndex=_FddimibPATHConfigSMTIndex_Object((1,3,6,1,2,1,10,15,73,4,3,1,1),_FddimibPATHConfigSMTIndex_Type())
fddimibPATHConfigSMTIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPATHConfigSMTIndex.setStatus(_A)
class _FddimibPATHConfigPATHIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FddimibPATHConfigPATHIndex_Type.__name__=_C
_FddimibPATHConfigPATHIndex_Object=MibTableColumn
fddimibPATHConfigPATHIndex=_FddimibPATHConfigPATHIndex_Object((1,3,6,1,2,1,10,15,73,4,3,1,2),_FddimibPATHConfigPATHIndex_Type())
fddimibPATHConfigPATHIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPATHConfigPATHIndex.setStatus(_A)
class _FddimibPATHConfigTokenOrder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FddimibPATHConfigTokenOrder_Type.__name__=_C
_FddimibPATHConfigTokenOrder_Object=MibTableColumn
fddimibPATHConfigTokenOrder=_FddimibPATHConfigTokenOrder_Object((1,3,6,1,2,1,10,15,73,4,3,1,3),_FddimibPATHConfigTokenOrder_Type())
fddimibPATHConfigTokenOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPATHConfigTokenOrder.setStatus(_A)
class _FddimibPATHConfigResourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4)));namedValues=NamedValues(*(('mac',2),('port',4)))
_FddimibPATHConfigResourceType_Type.__name__=_C
_FddimibPATHConfigResourceType_Object=MibTableColumn
fddimibPATHConfigResourceType=_FddimibPATHConfigResourceType_Object((1,3,6,1,2,1,10,15,73,4,3,1,4),_FddimibPATHConfigResourceType_Type())
fddimibPATHConfigResourceType.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPATHConfigResourceType.setStatus(_A)
class _FddimibPATHConfigResourceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FddimibPATHConfigResourceIndex_Type.__name__=_C
_FddimibPATHConfigResourceIndex_Object=MibTableColumn
fddimibPATHConfigResourceIndex=_FddimibPATHConfigResourceIndex_Object((1,3,6,1,2,1,10,15,73,4,3,1,5),_FddimibPATHConfigResourceIndex_Type())
fddimibPATHConfigResourceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPATHConfigResourceIndex.setStatus(_A)
class _FddimibPATHConfigCurrentPath_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_O,1),('local',2),(_P,3),(_Q,4),(_J,5),(_K,6)))
_FddimibPATHConfigCurrentPath_Type.__name__=_C
_FddimibPATHConfigCurrentPath_Object=MibTableColumn
fddimibPATHConfigCurrentPath=_FddimibPATHConfigCurrentPath_Object((1,3,6,1,2,1,10,15,73,4,3,1,6),_FddimibPATHConfigCurrentPath_Type())
fddimibPATHConfigCurrentPath.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPATHConfigCurrentPath.setStatus(_A)
_FddimibPORT_ObjectIdentity=ObjectIdentity
fddimibPORT=_FddimibPORT_ObjectIdentity((1,3,6,1,2,1,10,15,73,5))
class _FddimibPORTNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FddimibPORTNumber_Type.__name__=_C
_FddimibPORTNumber_Object=MibScalar
fddimibPORTNumber=_FddimibPORTNumber_Object((1,3,6,1,2,1,10,15,73,5,1),_FddimibPORTNumber_Type())
fddimibPORTNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTNumber.setStatus(_A)
_FddimibPORTTable_Object=MibTable
fddimibPORTTable=_FddimibPORTTable_Object((1,3,6,1,2,1,10,15,73,5,2))
if mibBuilder.loadTexts:fddimibPORTTable.setStatus(_A)
_FddimibPORTEntry_Object=MibTableRow
fddimibPORTEntry=_FddimibPORTEntry_Object((1,3,6,1,2,1,10,15,73,5,2,1))
fddimibPORTEntry.setIndexNames((0,_G,_W),(0,_G,_X))
if mibBuilder.loadTexts:fddimibPORTEntry.setStatus(_A)
class _FddimibPORTSMTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FddimibPORTSMTIndex_Type.__name__=_C
_FddimibPORTSMTIndex_Object=MibTableColumn
fddimibPORTSMTIndex=_FddimibPORTSMTIndex_Object((1,3,6,1,2,1,10,15,73,5,2,1,1),_FddimibPORTSMTIndex_Type())
fddimibPORTSMTIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTSMTIndex.setStatus(_A)
class _FddimibPORTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FddimibPORTIndex_Type.__name__=_C
_FddimibPORTIndex_Object=MibTableColumn
fddimibPORTIndex=_FddimibPORTIndex_Object((1,3,6,1,2,1,10,15,73,5,2,1,2),_FddimibPORTIndex_Type())
fddimibPORTIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTIndex.setStatus(_A)
class _FddimibPORTMyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('a',1),('b',2),('s',3),('m',4),(_H,5)))
_FddimibPORTMyType_Type.__name__=_C
_FddimibPORTMyType_Object=MibTableColumn
fddimibPORTMyType=_FddimibPORTMyType_Object((1,3,6,1,2,1,10,15,73,5,2,1,3),_FddimibPORTMyType_Type())
fddimibPORTMyType.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTMyType.setStatus(_A)
class _FddimibPORTNeighborType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('a',1),('b',2),('s',3),('m',4),(_H,5)))
_FddimibPORTNeighborType_Type.__name__=_C
_FddimibPORTNeighborType_Object=MibTableColumn
fddimibPORTNeighborType=_FddimibPORTNeighborType_Object((1,3,6,1,2,1,10,15,73,5,2,1,4),_FddimibPORTNeighborType_Type())
fddimibPORTNeighborType.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTNeighborType.setStatus(_A)
class _FddimibPORTConnectionPolicies_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_FddimibPORTConnectionPolicies_Type.__name__=_C
_FddimibPORTConnectionPolicies_Object=MibTableColumn
fddimibPORTConnectionPolicies=_FddimibPORTConnectionPolicies_Object((1,3,6,1,2,1,10,15,73,5,2,1,5),_FddimibPORTConnectionPolicies_Type())
fddimibPORTConnectionPolicies.setMaxAccess(_D)
if mibBuilder.loadTexts:fddimibPORTConnectionPolicies.setStatus(_A)
class _FddimibPORTMACIndicated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('tVal9FalseRVal9False',1),('tVal9FalseRVal9True',2),('tVal9TrueRVal9False',3),('tVal9TrueRVal9True',4)))
_FddimibPORTMACIndicated_Type.__name__=_C
_FddimibPORTMACIndicated_Object=MibTableColumn
fddimibPORTMACIndicated=_FddimibPORTMACIndicated_Object((1,3,6,1,2,1,10,15,73,5,2,1,6),_FddimibPORTMACIndicated_Type())
fddimibPORTMACIndicated.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTMACIndicated.setStatus(_A)
class _FddimibPORTCurrentPath_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ce0',1),('ce1',2),('ce2',3),('ce3',4),('ce4',5),('ce5',6)))
_FddimibPORTCurrentPath_Type.__name__=_C
_FddimibPORTCurrentPath_Object=MibTableColumn
fddimibPORTCurrentPath=_FddimibPORTCurrentPath_Object((1,3,6,1,2,1,10,15,73,5,2,1,7),_FddimibPORTCurrentPath_Type())
fddimibPORTCurrentPath.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTCurrentPath.setStatus(_A)
class _FddimibPORTRequestedPaths_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_FddimibPORTRequestedPaths_Type.__name__=_I
_FddimibPORTRequestedPaths_Object=MibTableColumn
fddimibPORTRequestedPaths=_FddimibPORTRequestedPaths_Object((1,3,6,1,2,1,10,15,73,5,2,1,8),_FddimibPORTRequestedPaths_Type())
fddimibPORTRequestedPaths.setMaxAccess(_D)
if mibBuilder.loadTexts:fddimibPORTRequestedPaths.setStatus(_A)
_FddimibPORTMACPlacement_Type=FddiResourceId
_FddimibPORTMACPlacement_Object=MibTableColumn
fddimibPORTMACPlacement=_FddimibPORTMACPlacement_Object((1,3,6,1,2,1,10,15,73,5,2,1,9),_FddimibPORTMACPlacement_Type())
fddimibPORTMACPlacement.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTMACPlacement.setStatus(_A)
class _FddimibPORTAvailablePaths_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FddimibPORTAvailablePaths_Type.__name__=_C
_FddimibPORTAvailablePaths_Object=MibTableColumn
fddimibPORTAvailablePaths=_FddimibPORTAvailablePaths_Object((1,3,6,1,2,1,10,15,73,5,2,1,10),_FddimibPORTAvailablePaths_Type())
fddimibPORTAvailablePaths.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTAvailablePaths.setStatus(_A)
class _FddimibPORTPMDClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('multimode',1),('single-mode1',2),('single-mode2',3),('sonet',4),('low-cost-fiber',5),('twisted-pair',6),('unknown',7),('unspecified',8)))
_FddimibPORTPMDClass_Type.__name__=_C
_FddimibPORTPMDClass_Object=MibTableColumn
fddimibPORTPMDClass=_FddimibPORTPMDClass_Object((1,3,6,1,2,1,10,15,73,5,2,1,11),_FddimibPORTPMDClass_Type())
fddimibPORTPMDClass.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTPMDClass.setStatus(_A)
class _FddimibPORTConnectionCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_FddimibPORTConnectionCapabilities_Type.__name__=_C
_FddimibPORTConnectionCapabilities_Object=MibTableColumn
fddimibPORTConnectionCapabilities=_FddimibPORTConnectionCapabilities_Object((1,3,6,1,2,1,10,15,73,5,2,1,12),_FddimibPORTConnectionCapabilities_Type())
fddimibPORTConnectionCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTConnectionCapabilities.setStatus(_A)
class _FddimibPORTBSFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FddimibPORTBSFlag_Type.__name__=_C
_FddimibPORTBSFlag_Object=MibTableColumn
fddimibPORTBSFlag=_FddimibPORTBSFlag_Object((1,3,6,1,2,1,10,15,73,5,2,1,13),_FddimibPORTBSFlag_Type())
fddimibPORTBSFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTBSFlag.setStatus(_A)
_FddimibPORTLCTFailCts_Type=Counter32
_FddimibPORTLCTFailCts_Object=MibTableColumn
fddimibPORTLCTFailCts=_FddimibPORTLCTFailCts_Object((1,3,6,1,2,1,10,15,73,5,2,1,14),_FddimibPORTLCTFailCts_Type())
fddimibPORTLCTFailCts.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTLCTFailCts.setStatus(_A)
class _FddimibPORTLerEstimate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,15))
_FddimibPORTLerEstimate_Type.__name__=_C
_FddimibPORTLerEstimate_Object=MibTableColumn
fddimibPORTLerEstimate=_FddimibPORTLerEstimate_Object((1,3,6,1,2,1,10,15,73,5,2,1,15),_FddimibPORTLerEstimate_Type())
fddimibPORTLerEstimate.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTLerEstimate.setStatus(_A)
_FddimibPORTLemRejectCts_Type=Counter32
_FddimibPORTLemRejectCts_Object=MibTableColumn
fddimibPORTLemRejectCts=_FddimibPORTLemRejectCts_Object((1,3,6,1,2,1,10,15,73,5,2,1,16),_FddimibPORTLemRejectCts_Type())
fddimibPORTLemRejectCts.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTLemRejectCts.setStatus(_A)
_FddimibPORTLemCts_Type=Counter32
_FddimibPORTLemCts_Object=MibTableColumn
fddimibPORTLemCts=_FddimibPORTLemCts_Object((1,3,6,1,2,1,10,15,73,5,2,1,17),_FddimibPORTLemCts_Type())
fddimibPORTLemCts.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTLemCts.setStatus(_A)
class _FddimibPORTLerCutoff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,15))
_FddimibPORTLerCutoff_Type.__name__=_C
_FddimibPORTLerCutoff_Object=MibTableColumn
fddimibPORTLerCutoff=_FddimibPORTLerCutoff_Object((1,3,6,1,2,1,10,15,73,5,2,1,18),_FddimibPORTLerCutoff_Type())
fddimibPORTLerCutoff.setMaxAccess(_D)
if mibBuilder.loadTexts:fddimibPORTLerCutoff.setStatus(_A)
class _FddimibPORTLerAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,15))
_FddimibPORTLerAlarm_Type.__name__=_C
_FddimibPORTLerAlarm_Object=MibTableColumn
fddimibPORTLerAlarm=_FddimibPORTLerAlarm_Object((1,3,6,1,2,1,10,15,73,5,2,1,19),_FddimibPORTLerAlarm_Type())
fddimibPORTLerAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:fddimibPORTLerAlarm.setStatus(_A)
class _FddimibPORTConnectState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disabled',1),('connecting',2),('standby',3),('active',4)))
_FddimibPORTConnectState_Type.__name__=_C
_FddimibPORTConnectState_Object=MibTableColumn
fddimibPORTConnectState=_FddimibPORTConnectState_Object((1,3,6,1,2,1,10,15,73,5,2,1,20),_FddimibPORTConnectState_Type())
fddimibPORTConnectState.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTConnectState.setStatus(_A)
class _FddimibPORTPCMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('pc0',1),('pc1',2),('pc2',3),('pc3',4),('pc4',5),('pc5',6),('pc6',7),('pc7',8),('pc8',9),('pc9',10)))
_FddimibPORTPCMState_Type.__name__=_C
_FddimibPORTPCMState_Object=MibTableColumn
fddimibPORTPCMState=_FddimibPORTPCMState_Object((1,3,6,1,2,1,10,15,73,5,2,1,21),_FddimibPORTPCMState_Type())
fddimibPORTPCMState.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTPCMState.setStatus(_A)
class _FddimibPORTPCWithhold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('m-m',2),('otherincompatible',3),('pathnotavailable',4)))
_FddimibPORTPCWithhold_Type.__name__=_C
_FddimibPORTPCWithhold_Object=MibTableColumn
fddimibPORTPCWithhold=_FddimibPORTPCWithhold_Object((1,3,6,1,2,1,10,15,73,5,2,1,22),_FddimibPORTPCWithhold_Type())
fddimibPORTPCWithhold.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTPCWithhold.setStatus(_A)
class _FddimibPORTLerFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FddimibPORTLerFlag_Type.__name__=_C
_FddimibPORTLerFlag_Object=MibTableColumn
fddimibPORTLerFlag=_FddimibPORTLerFlag_Object((1,3,6,1,2,1,10,15,73,5,2,1,23),_FddimibPORTLerFlag_Type())
fddimibPORTLerFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTLerFlag.setStatus(_A)
class _FddimibPORTHardwarePresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FddimibPORTHardwarePresent_Type.__name__=_C
_FddimibPORTHardwarePresent_Object=MibTableColumn
fddimibPORTHardwarePresent=_FddimibPORTHardwarePresent_Object((1,3,6,1,2,1,10,15,73,5,2,1,24),_FddimibPORTHardwarePresent_Type())
fddimibPORTHardwarePresent.setMaxAccess(_B)
if mibBuilder.loadTexts:fddimibPORTHardwarePresent.setStatus(_A)
class _FddimibPORTAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('maintPORT',2),('enablePORT',3),('disablePORT',4),('startPORT',5),('stopPORT',6)))
_FddimibPORTAction_Type.__name__=_C
_FddimibPORTAction_Object=MibTableColumn
fddimibPORTAction=_FddimibPORTAction_Object((1,3,6,1,2,1,10,15,73,5,2,1,25),_FddimibPORTAction_Type())
fddimibPORTAction.setMaxAccess(_D)
if mibBuilder.loadTexts:fddimibPORTAction.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'FddiTimeNano':FddiTimeNano,'FddiTimeMilli':FddiTimeMilli,'FddiResourceId':FddiResourceId,'FddiSMTStationIdType':FddiSMTStationIdType,'FddiMACLongAddressType':FddiMACLongAddressType,'fddi':fddi,'fddimib':fddimib,'fddimibSMT':fddimibSMT,'fddimibSMTNumber':fddimibSMTNumber,'fddimibSMTTable':fddimibSMTTable,'fddimibSMTEntry':fddimibSMTEntry,_N:fddimibSMTIndex,'fddimibSMTStationId':fddimibSMTStationId,'fddimibSMTOpVersionId':fddimibSMTOpVersionId,'fddimibSMTHiVersionId':fddimibSMTHiVersionId,'fddimibSMTLoVersionId':fddimibSMTLoVersionId,'fddimibSMTUserData':fddimibSMTUserData,'fddimibSMTMIBVersionId':fddimibSMTMIBVersionId,'fddimibSMTMACCts':fddimibSMTMACCts,'fddimibSMTNonMasterCts':fddimibSMTNonMasterCts,'fddimibSMTMasterCts':fddimibSMTMasterCts,'fddimibSMTAvailablePaths':fddimibSMTAvailablePaths,'fddimibSMTConfigCapabilities':fddimibSMTConfigCapabilities,'fddimibSMTConfigPolicy':fddimibSMTConfigPolicy,'fddimibSMTConnectionPolicy':fddimibSMTConnectionPolicy,'fddimibSMTTNotify':fddimibSMTTNotify,'fddimibSMTStatRptPolicy':fddimibSMTStatRptPolicy,'fddimibSMTTraceMaxExpiration':fddimibSMTTraceMaxExpiration,'fddimibSMTBypassPresent':fddimibSMTBypassPresent,'fddimibSMTECMState':fddimibSMTECMState,'fddimibSMTCFState':fddimibSMTCFState,'fddimibSMTRemoteDisconnectFlag':fddimibSMTRemoteDisconnectFlag,'fddimibSMTStationStatus':fddimibSMTStationStatus,'fddimibSMTPeerWrapFlag':fddimibSMTPeerWrapFlag,'fddimibSMTTimeStamp':fddimibSMTTimeStamp,'fddimibSMTTransitionTimeStamp':fddimibSMTTransitionTimeStamp,'fddimibSMTStationAction':fddimibSMTStationAction,'fddimibMAC':fddimibMAC,'fddimibMACNumber':fddimibMACNumber,'fddimibMACTable':fddimibMACTable,'fddimibMACEntry':fddimibMACEntry,_L:fddimibMACSMTIndex,_M:fddimibMACIndex,'fddimibMACIfIndex':fddimibMACIfIndex,'fddimibMACFrameStatusFunctions':fddimibMACFrameStatusFunctions,'fddimibMACTMaxCapability':fddimibMACTMaxCapability,'fddimibMACTVXCapability':fddimibMACTVXCapability,'fddimibMACAvailablePaths':fddimibMACAvailablePaths,'fddimibMACCurrentPath':fddimibMACCurrentPath,'fddimibMACUpstreamNbr':fddimibMACUpstreamNbr,'fddimibMACDownstreamNbr':fddimibMACDownstreamNbr,'fddimibMACOldUpstreamNbr':fddimibMACOldUpstreamNbr,'fddimibMACOldDownstreamNbr':fddimibMACOldDownstreamNbr,'fddimibMACDupAddressTest':fddimibMACDupAddressTest,'fddimibMACRequestedPaths':fddimibMACRequestedPaths,'fddimibMACDownstreamPORTType':fddimibMACDownstreamPORTType,'fddimibMACSMTAddress':fddimibMACSMTAddress,'fddimibMACTReq':fddimibMACTReq,'fddimibMACTNeg':fddimibMACTNeg,'fddimibMACTMax':fddimibMACTMax,'fddimibMACTvxValue':fddimibMACTvxValue,'fddimibMACFrameCts':fddimibMACFrameCts,'fddimibMACCopiedCts':fddimibMACCopiedCts,'fddimibMACTransmitCts':fddimibMACTransmitCts,'fddimibMACErrorCts':fddimibMACErrorCts,'fddimibMACLostCts':fddimibMACLostCts,'fddimibMACFrameErrorThreshold':fddimibMACFrameErrorThreshold,'fddimibMACFrameErrorRatio':fddimibMACFrameErrorRatio,'fddimibMACRMTState':fddimibMACRMTState,'fddimibMACDaFlag':fddimibMACDaFlag,'fddimibMACUnaDaFlag':fddimibMACUnaDaFlag,'fddimibMACFrameErrorFlag':fddimibMACFrameErrorFlag,'fddimibMACMAUnitdataAvailable':fddimibMACMAUnitdataAvailable,'fddimibMACHardwarePresent':fddimibMACHardwarePresent,'fddimibMACMAUnitdataEnable':fddimibMACMAUnitdataEnable,'fddimibMACCounters':fddimibMACCounters,'fddimibMACCountersTable':fddimibMACCountersTable,'fddimibMACCountersEntry':fddimibMACCountersEntry,'fddimibMACTokenCts':fddimibMACTokenCts,'fddimibMACTvxExpiredCts':fddimibMACTvxExpiredCts,'fddimibMACNotCopiedCts':fddimibMACNotCopiedCts,'fddimibMACLateCts':fddimibMACLateCts,'fddimibMACRingOpCts':fddimibMACRingOpCts,'fddimibMACNotCopiedRatio':fddimibMACNotCopiedRatio,'fddimibMACNotCopiedFlag':fddimibMACNotCopiedFlag,'fddimibMACNotCopiedThreshold':fddimibMACNotCopiedThreshold,'fddimibPATH':fddimibPATH,'fddimibPATHNumber':fddimibPATHNumber,'fddimibPATHTable':fddimibPATHTable,'fddimibPATHEntry':fddimibPATHEntry,_R:fddimibPATHSMTIndex,_S:fddimibPATHIndex,'fddimibPATHTVXLowerBound':fddimibPATHTVXLowerBound,'fddimibPATHTMaxLowerBound':fddimibPATHTMaxLowerBound,'fddimibPATHMaxTReq':fddimibPATHMaxTReq,'fddimibPATHConfigTable':fddimibPATHConfigTable,'fddimibPATHConfigEntry':fddimibPATHConfigEntry,_T:fddimibPATHConfigSMTIndex,_U:fddimibPATHConfigPATHIndex,_V:fddimibPATHConfigTokenOrder,'fddimibPATHConfigResourceType':fddimibPATHConfigResourceType,'fddimibPATHConfigResourceIndex':fddimibPATHConfigResourceIndex,'fddimibPATHConfigCurrentPath':fddimibPATHConfigCurrentPath,'fddimibPORT':fddimibPORT,'fddimibPORTNumber':fddimibPORTNumber,'fddimibPORTTable':fddimibPORTTable,'fddimibPORTEntry':fddimibPORTEntry,_W:fddimibPORTSMTIndex,_X:fddimibPORTIndex,'fddimibPORTMyType':fddimibPORTMyType,'fddimibPORTNeighborType':fddimibPORTNeighborType,'fddimibPORTConnectionPolicies':fddimibPORTConnectionPolicies,'fddimibPORTMACIndicated':fddimibPORTMACIndicated,'fddimibPORTCurrentPath':fddimibPORTCurrentPath,'fddimibPORTRequestedPaths':fddimibPORTRequestedPaths,'fddimibPORTMACPlacement':fddimibPORTMACPlacement,'fddimibPORTAvailablePaths':fddimibPORTAvailablePaths,'fddimibPORTPMDClass':fddimibPORTPMDClass,'fddimibPORTConnectionCapabilities':fddimibPORTConnectionCapabilities,'fddimibPORTBSFlag':fddimibPORTBSFlag,'fddimibPORTLCTFailCts':fddimibPORTLCTFailCts,'fddimibPORTLerEstimate':fddimibPORTLerEstimate,'fddimibPORTLemRejectCts':fddimibPORTLemRejectCts,'fddimibPORTLemCts':fddimibPORTLemCts,'fddimibPORTLerCutoff':fddimibPORTLerCutoff,'fddimibPORTLerAlarm':fddimibPORTLerAlarm,'fddimibPORTConnectState':fddimibPORTConnectState,'fddimibPORTPCMState':fddimibPORTPCMState,'fddimibPORTPCWithhold':fddimibPORTPCWithhold,'fddimibPORTLerFlag':fddimibPORTLerFlag,'fddimibPORTHardwarePresent':fddimibPORTHardwarePresent,'fddimibPORTAction':fddimibPORTAction})