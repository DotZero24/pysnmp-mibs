_V='wwpLeosTwampServerCtrlSessionId'
_U='wwpLeosTwampClientStatsRecordIndex'
_T='wwpLeosTwampClientSessionStatsIndex'
_S='wwpLeosTwampClientSessionId'
_R='accept'
_Q='listen'
_P='wwpLeosTwampServerSessionId'
_O='wwpLeosTwampPortId'
_N='off'
_M='not-accessible'
_L='inactive'
_K='error'
_J='stop'
_I='DisplayString'
_H='active'
_G='enable'
_F='disable'
_E='WWP-LEOS-TWAMP-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_I,'PhysAddress','TextualConvention','TruthValue')
wwpModules,wwpModulesLeos=mibBuilder.importSymbols('WWP-SMI','wwpModules','wwpModulesLeos')
wwpLeosTwampMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,40))
if mibBuilder.loadTexts:wwpLeosTwampMIB.setRevisions(('2008-08-08 08:00','2008-02-15 08:00'))
_WwpLeosTwampMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosTwampMIBObjects=_WwpLeosTwampMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,40,1))
_WwpLeosTwamp_ObjectIdentity=ObjectIdentity
wwpLeosTwamp=_WwpLeosTwamp_ObjectIdentity((1,3,6,1,4,1,6141,2,60,40,1,1))
_WwpLeosTwampModule_ObjectIdentity=ObjectIdentity
wwpLeosTwampModule=_WwpLeosTwampModule_ObjectIdentity((1,3,6,1,4,1,6141,2,60,40,1,1,1))
class _WwpLeosTwampPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,65535))
_WwpLeosTwampPort_Type.__name__=_C
_WwpLeosTwampPort_Object=MibScalar
wwpLeosTwampPort=_WwpLeosTwampPort_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,1),_WwpLeosTwampPort_Type())
wwpLeosTwampPort.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampPort.setStatus(_A)
class _WwpLeosTwampEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_WwpLeosTwampEnable_Type.__name__=_C
_WwpLeosTwampEnable_Object=MibScalar
wwpLeosTwampEnable=_WwpLeosTwampEnable_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,2),_WwpLeosTwampEnable_Type())
wwpLeosTwampEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampEnable.setStatus(_A)
_WwpLeosTwampPortEnableTable_Object=MibTable
wwpLeosTwampPortEnableTable=_WwpLeosTwampPortEnableTable_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,3))
if mibBuilder.loadTexts:wwpLeosTwampPortEnableTable.setStatus(_A)
_WwpLeosTwampPortEnableEntry_Object=MibTableRow
wwpLeosTwampPortEnableEntry=_WwpLeosTwampPortEnableEntry_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,3,1))
wwpLeosTwampPortEnableEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:wwpLeosTwampPortEnableEntry.setStatus(_A)
class _WwpLeosTwampPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,28))
_WwpLeosTwampPortId_Type.__name__=_C
_WwpLeosTwampPortId_Object=MibTableColumn
wwpLeosTwampPortId=_WwpLeosTwampPortId_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,3,1,1),_WwpLeosTwampPortId_Type())
wwpLeosTwampPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampPortId.setStatus(_A)
class _WwpLeosTwampPortEnableState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_WwpLeosTwampPortEnableState_Type.__name__=_C
_WwpLeosTwampPortEnableState_Object=MibTableColumn
wwpLeosTwampPortEnableState=_WwpLeosTwampPortEnableState_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,3,1,2),_WwpLeosTwampPortEnableState_Type())
wwpLeosTwampPortEnableState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampPortEnableState.setStatus(_A)
class _WwpLeosTwampClientEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_WwpLeosTwampClientEnable_Type.__name__=_C
_WwpLeosTwampClientEnable_Object=MibScalar
wwpLeosTwampClientEnable=_WwpLeosTwampClientEnable_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,4),_WwpLeosTwampClientEnable_Type())
wwpLeosTwampClientEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampClientEnable.setStatus(_A)
class _WwpLeosTwampServerEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_WwpLeosTwampServerEnable_Type.__name__=_C
_WwpLeosTwampServerEnable_Object=MibScalar
wwpLeosTwampServerEnable=_WwpLeosTwampServerEnable_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,5),_WwpLeosTwampServerEnable_Type())
wwpLeosTwampServerEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampServerEnable.setStatus(_A)
class _WwpLeosTwampLightEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_WwpLeosTwampLightEnable_Type.__name__=_C
_WwpLeosTwampLightEnable_Object=MibScalar
wwpLeosTwampLightEnable=_WwpLeosTwampLightEnable_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,6),_WwpLeosTwampLightEnable_Type())
wwpLeosTwampLightEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampLightEnable.setStatus(_A)
_WwpLeosTwampServerSessionsTable_Object=MibTable
wwpLeosTwampServerSessionsTable=_WwpLeosTwampServerSessionsTable_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,7))
if mibBuilder.loadTexts:wwpLeosTwampServerSessionsTable.setStatus(_A)
_WwpLeosTwampServerSessionEntry_Object=MibTableRow
wwpLeosTwampServerSessionEntry=_WwpLeosTwampServerSessionEntry_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,7,1))
wwpLeosTwampServerSessionEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:wwpLeosTwampServerSessionEntry.setStatus(_A)
class _WwpLeosTwampServerSessionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_WwpLeosTwampServerSessionId_Type.__name__=_C
_WwpLeosTwampServerSessionId_Object=MibTableColumn
wwpLeosTwampServerSessionId=_WwpLeosTwampServerSessionId_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,7,1,1),_WwpLeosTwampServerSessionId_Type())
wwpLeosTwampServerSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampServerSessionId.setStatus(_A)
class _WwpLeosTwampServerSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_Q,0),('greet',1),('start',2),(_R,3),('test',4),(_J,5),(_K,6)))
_WwpLeosTwampServerSessionState_Type.__name__=_C
_WwpLeosTwampServerSessionState_Object=MibTableColumn
wwpLeosTwampServerSessionState=_WwpLeosTwampServerSessionState_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,7,1,2),_WwpLeosTwampServerSessionState_Type())
wwpLeosTwampServerSessionState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampServerSessionState.setStatus(_A)
class _WwpLeosTwampServerSessionPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosTwampServerSessionPort_Type.__name__=_C
_WwpLeosTwampServerSessionPort_Object=MibTableColumn
wwpLeosTwampServerSessionPort=_WwpLeosTwampServerSessionPort_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,7,1,3),_WwpLeosTwampServerSessionPort_Type())
wwpLeosTwampServerSessionPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampServerSessionPort.setStatus(_A)
_WwpLeosTwampServerSessionHost_Type=IpAddress
_WwpLeosTwampServerSessionHost_Object=MibTableColumn
wwpLeosTwampServerSessionHost=_WwpLeosTwampServerSessionHost_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,7,1,4),_WwpLeosTwampServerSessionHost_Type())
wwpLeosTwampServerSessionHost.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampServerSessionHost.setStatus(_A)
_WwpLeosTwampServerSessionNumPkts_Type=Integer32
_WwpLeosTwampServerSessionNumPkts_Object=MibTableColumn
wwpLeosTwampServerSessionNumPkts=_WwpLeosTwampServerSessionNumPkts_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,7,1,5),_WwpLeosTwampServerSessionNumPkts_Type())
wwpLeosTwampServerSessionNumPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampServerSessionNumPkts.setStatus(_A)
_WwpLeosTwampServerSessionSeqNum_Type=Integer32
_WwpLeosTwampServerSessionSeqNum_Object=MibTableColumn
wwpLeosTwampServerSessionSeqNum=_WwpLeosTwampServerSessionSeqNum_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,7,1,6),_WwpLeosTwampServerSessionSeqNum_Type())
wwpLeosTwampServerSessionSeqNum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampServerSessionSeqNum.setStatus(_A)
class _WwpLeosTwampServerSessionHwAssist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_H,1)))
_WwpLeosTwampServerSessionHwAssist_Type.__name__=_C
_WwpLeosTwampServerSessionHwAssist_Object=MibTableColumn
wwpLeosTwampServerSessionHwAssist=_WwpLeosTwampServerSessionHwAssist_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,7,1,7),_WwpLeosTwampServerSessionHwAssist_Type())
wwpLeosTwampServerSessionHwAssist.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampServerSessionHwAssist.setStatus(_A)
class _WwpLeosTwampTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_WwpLeosTwampTimeout_Type.__name__=_C
_WwpLeosTwampTimeout_Object=MibScalar
wwpLeosTwampTimeout=_WwpLeosTwampTimeout_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,8),_WwpLeosTwampTimeout_Type())
wwpLeosTwampTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampTimeout.setStatus(_A)
_WwpLeosTwampClientSessionsTable_Object=MibTable
wwpLeosTwampClientSessionsTable=_WwpLeosTwampClientSessionsTable_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,9))
if mibBuilder.loadTexts:wwpLeosTwampClientSessionsTable.setStatus(_A)
_WwpLeosTwampClientSessionEntry_Object=MibTableRow
wwpLeosTwampClientSessionEntry=_WwpLeosTwampClientSessionEntry_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,9,1))
wwpLeosTwampClientSessionEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:wwpLeosTwampClientSessionEntry.setStatus(_A)
class _WwpLeosTwampClientSessionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_WwpLeosTwampClientSessionId_Type.__name__=_C
_WwpLeosTwampClientSessionId_Object=MibTableColumn
wwpLeosTwampClientSessionId=_WwpLeosTwampClientSessionId_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,9,1,1),_WwpLeosTwampClientSessionId_Type())
wwpLeosTwampClientSessionId.setMaxAccess(_M)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionId.setStatus(_A)
class _WwpLeosTwampClientSessionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),('createAndGo',2),('clear',3),('startTest',4),('stopTest',5),('clearStats',6)))
_WwpLeosTwampClientSessionStatus_Type.__name__=_C
_WwpLeosTwampClientSessionStatus_Object=MibTableColumn
wwpLeosTwampClientSessionStatus=_WwpLeosTwampClientSessionStatus_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,9,1,2),_WwpLeosTwampClientSessionStatus_Type())
wwpLeosTwampClientSessionStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatus.setStatus(_A)
class _WwpLeosTwampClientSessionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_WwpLeosTwampClientSessionName_Type.__name__=_I
_WwpLeosTwampClientSessionName_Object=MibTableColumn
wwpLeosTwampClientSessionName=_WwpLeosTwampClientSessionName_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,9,1,3),_WwpLeosTwampClientSessionName_Type())
wwpLeosTwampClientSessionName.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionName.setStatus(_A)
_WwpLeosTwampClientSessionHost_Type=IpAddress
_WwpLeosTwampClientSessionHost_Object=MibTableColumn
wwpLeosTwampClientSessionHost=_WwpLeosTwampClientSessionHost_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,9,1,4),_WwpLeosTwampClientSessionHost_Type())
wwpLeosTwampClientSessionHost.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionHost.setStatus(_A)
class _WwpLeosTwampClientSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('idle',0),('greeting',1),('serverStart',2),('sessionSetup',3),('sessionStart',4),('testing',5),(_J,6),(_K,7)))
_WwpLeosTwampClientSessionState_Type.__name__=_C
_WwpLeosTwampClientSessionState_Object=MibTableColumn
wwpLeosTwampClientSessionState=_WwpLeosTwampClientSessionState_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,9,1,5),_WwpLeosTwampClientSessionState_Type())
wwpLeosTwampClientSessionState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionState.setStatus(_A)
class _WwpLeosTwampClientSessionCommPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosTwampClientSessionCommPort_Type.__name__=_C
_WwpLeosTwampClientSessionCommPort_Object=MibTableColumn
wwpLeosTwampClientSessionCommPort=_WwpLeosTwampClientSessionCommPort_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,9,1,6),_WwpLeosTwampClientSessionCommPort_Type())
wwpLeosTwampClientSessionCommPort.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionCommPort.setStatus(_A)
class _WwpLeosTwampClientSessionCosPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dscp',1),('ipPrec',2)))
_WwpLeosTwampClientSessionCosPolicy_Type.__name__=_C
_WwpLeosTwampClientSessionCosPolicy_Object=MibTableColumn
wwpLeosTwampClientSessionCosPolicy=_WwpLeosTwampClientSessionCosPolicy_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,9,1,7),_WwpLeosTwampClientSessionCosPolicy_Type())
wwpLeosTwampClientSessionCosPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionCosPolicy.setStatus(_A)
class _WwpLeosTwampClientSessionDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_WwpLeosTwampClientSessionDscp_Type.__name__=_C
_WwpLeosTwampClientSessionDscp_Object=MibTableColumn
wwpLeosTwampClientSessionDscp=_WwpLeosTwampClientSessionDscp_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,9,1,8),_WwpLeosTwampClientSessionDscp_Type())
wwpLeosTwampClientSessionDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionDscp.setStatus(_A)
class _WwpLeosTwampClientSessionIpPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosTwampClientSessionIpPrec_Type.__name__=_C
_WwpLeosTwampClientSessionIpPrec_Object=MibTableColumn
wwpLeosTwampClientSessionIpPrec=_WwpLeosTwampClientSessionIpPrec_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,9,1,9),_WwpLeosTwampClientSessionIpPrec_Type())
wwpLeosTwampClientSessionIpPrec.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionIpPrec.setStatus(_A)
class _WwpLeosTwampClientSessionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fixed',1),('poisson',2)))
_WwpLeosTwampClientSessionType_Type.__name__=_C
_WwpLeosTwampClientSessionType_Object=MibTableColumn
wwpLeosTwampClientSessionType=_WwpLeosTwampClientSessionType_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,9,1,10),_WwpLeosTwampClientSessionType_Type())
wwpLeosTwampClientSessionType.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionType.setStatus(_A)
class _WwpLeosTwampClientSessionPktSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1500))
_WwpLeosTwampClientSessionPktSize_Type.__name__=_C
_WwpLeosTwampClientSessionPktSize_Object=MibTableColumn
wwpLeosTwampClientSessionPktSize=_WwpLeosTwampClientSessionPktSize_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,9,1,11),_WwpLeosTwampClientSessionPktSize_Type())
wwpLeosTwampClientSessionPktSize.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionPktSize.setStatus(_A)
class _WwpLeosTwampClientSessionRepeat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_N,2)))
_WwpLeosTwampClientSessionRepeat_Type.__name__=_C
_WwpLeosTwampClientSessionRepeat_Object=MibTableColumn
wwpLeosTwampClientSessionRepeat=_WwpLeosTwampClientSessionRepeat_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,9,1,12),_WwpLeosTwampClientSessionRepeat_Type())
wwpLeosTwampClientSessionRepeat.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionRepeat.setStatus(_A)
_WwpLeosTwampClientSessionSeqNum_Type=Integer32
_WwpLeosTwampClientSessionSeqNum_Object=MibTableColumn
wwpLeosTwampClientSessionSeqNum=_WwpLeosTwampClientSessionSeqNum_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,9,1,13),_WwpLeosTwampClientSessionSeqNum_Type())
wwpLeosTwampClientSessionSeqNum.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionSeqNum.setStatus(_A)
_WwpLeosTwampClientSessionNumPkts_Type=Integer32
_WwpLeosTwampClientSessionNumPkts_Object=MibTableColumn
wwpLeosTwampClientSessionNumPkts=_WwpLeosTwampClientSessionNumPkts_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,9,1,14),_WwpLeosTwampClientSessionNumPkts_Type())
wwpLeosTwampClientSessionNumPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionNumPkts.setStatus(_A)
class _WwpLeosTwampClientSessionRxHw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_H,1)))
_WwpLeosTwampClientSessionRxHw_Type.__name__=_C
_WwpLeosTwampClientSessionRxHw_Object=MibTableColumn
wwpLeosTwampClientSessionRxHw=_WwpLeosTwampClientSessionRxHw_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,9,1,15),_WwpLeosTwampClientSessionRxHw_Type())
wwpLeosTwampClientSessionRxHw.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionRxHw.setStatus(_A)
class _WwpLeosTwampClientSessionTxHw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_H,1)))
_WwpLeosTwampClientSessionTxHw_Type.__name__=_C
_WwpLeosTwampClientSessionTxHw_Object=MibTableColumn
wwpLeosTwampClientSessionTxHw=_WwpLeosTwampClientSessionTxHw_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,9,1,16),_WwpLeosTwampClientSessionTxHw_Type())
wwpLeosTwampClientSessionTxHw.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionTxHw.setStatus(_A)
class _WwpLeosTwampClientSessionDot1dpri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_WwpLeosTwampClientSessionDot1dpri_Type.__name__=_C
_WwpLeosTwampClientSessionDot1dpri_Object=MibTableColumn
wwpLeosTwampClientSessionDot1dpri=_WwpLeosTwampClientSessionDot1dpri_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,9,1,17),_WwpLeosTwampClientSessionDot1dpri_Type())
wwpLeosTwampClientSessionDot1dpri.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionDot1dpri.setStatus(_A)
_WwpLeosTwampClientSessionsStatisticsTable_Object=MibTable
wwpLeosTwampClientSessionsStatisticsTable=_WwpLeosTwampClientSessionsStatisticsTable_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11))
if mibBuilder.loadTexts:wwpLeosTwampClientSessionsStatisticsTable.setStatus(_A)
_WwpLeosTwampClientSessionStatisticsEntry_Object=MibTableRow
wwpLeosTwampClientSessionStatisticsEntry=_WwpLeosTwampClientSessionStatisticsEntry_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1))
wwpLeosTwampClientSessionStatisticsEntry.setIndexNames((0,_E,_T),(0,_E,_U))
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatisticsEntry.setStatus(_A)
class _WwpLeosTwampClientSessionStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_WwpLeosTwampClientSessionStatsIndex_Type.__name__=_C
_WwpLeosTwampClientSessionStatsIndex_Object=MibTableColumn
wwpLeosTwampClientSessionStatsIndex=_WwpLeosTwampClientSessionStatsIndex_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,1),_WwpLeosTwampClientSessionStatsIndex_Type())
wwpLeosTwampClientSessionStatsIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsIndex.setStatus(_A)
class _WwpLeosTwampClientStatsRecordIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_WwpLeosTwampClientStatsRecordIndex_Type.__name__=_C
_WwpLeosTwampClientStatsRecordIndex_Object=MibTableColumn
wwpLeosTwampClientStatsRecordIndex=_WwpLeosTwampClientStatsRecordIndex_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,2),_WwpLeosTwampClientStatsRecordIndex_Type())
wwpLeosTwampClientStatsRecordIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:wwpLeosTwampClientStatsRecordIndex.setStatus(_A)
class _WwpLeosTwampClientSessionStatsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_WwpLeosTwampClientSessionStatsName_Type.__name__=_I
_WwpLeosTwampClientSessionStatsName_Object=MibTableColumn
wwpLeosTwampClientSessionStatsName=_WwpLeosTwampClientSessionStatsName_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,3),_WwpLeosTwampClientSessionStatsName_Type())
wwpLeosTwampClientSessionStatsName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsName.setStatus(_A)
_WwpLeosTwampClientSessionTimestamp_Type=Unsigned32
_WwpLeosTwampClientSessionTimestamp_Object=MibTableColumn
wwpLeosTwampClientSessionTimestamp=_WwpLeosTwampClientSessionTimestamp_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,4),_WwpLeosTwampClientSessionTimestamp_Type())
wwpLeosTwampClientSessionTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionTimestamp.setStatus(_A)
_WwpLeosTwampClientSessionStatsPktTx_Type=Unsigned32
_WwpLeosTwampClientSessionStatsPktTx_Object=MibTableColumn
wwpLeosTwampClientSessionStatsPktTx=_WwpLeosTwampClientSessionStatsPktTx_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,5),_WwpLeosTwampClientSessionStatsPktTx_Type())
wwpLeosTwampClientSessionStatsPktTx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsPktTx.setStatus(_A)
_WwpLeosTwampClientSessionStatsPktRx_Type=Unsigned32
_WwpLeosTwampClientSessionStatsPktRx_Object=MibTableColumn
wwpLeosTwampClientSessionStatsPktRx=_WwpLeosTwampClientSessionStatsPktRx_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,6),_WwpLeosTwampClientSessionStatsPktRx_Type())
wwpLeosTwampClientSessionStatsPktRx.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsPktRx.setStatus(_A)
_WwpLeosTwampClientSessionStatsPktOL_Type=Unsigned32
_WwpLeosTwampClientSessionStatsPktOL_Object=MibTableColumn
wwpLeosTwampClientSessionStatsPktOL=_WwpLeosTwampClientSessionStatsPktOL_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,7),_WwpLeosTwampClientSessionStatsPktOL_Type())
wwpLeosTwampClientSessionStatsPktOL.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsPktOL.setStatus(_A)
_WwpLeosTwampClientSessionStatsPktRL_Type=Unsigned32
_WwpLeosTwampClientSessionStatsPktRL_Object=MibTableColumn
wwpLeosTwampClientSessionStatsPktRL=_WwpLeosTwampClientSessionStatsPktRL_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,8),_WwpLeosTwampClientSessionStatsPktRL_Type())
wwpLeosTwampClientSessionStatsPktRL.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsPktRL.setStatus(_A)
_WwpLeosTwampClientSessionStatsRTMin_Type=Unsigned32
_WwpLeosTwampClientSessionStatsRTMin_Object=MibTableColumn
wwpLeosTwampClientSessionStatsRTMin=_WwpLeosTwampClientSessionStatsRTMin_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,9),_WwpLeosTwampClientSessionStatsRTMin_Type())
wwpLeosTwampClientSessionStatsRTMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsRTMin.setStatus(_A)
_WwpLeosTwampClientSessionStatsRTMax_Type=Unsigned32
_WwpLeosTwampClientSessionStatsRTMax_Object=MibTableColumn
wwpLeosTwampClientSessionStatsRTMax=_WwpLeosTwampClientSessionStatsRTMax_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,10),_WwpLeosTwampClientSessionStatsRTMax_Type())
wwpLeosTwampClientSessionStatsRTMax.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsRTMax.setStatus(_A)
_WwpLeosTwampClientSessionStatsRTMean_Type=Unsigned32
_WwpLeosTwampClientSessionStatsRTMean_Object=MibTableColumn
wwpLeosTwampClientSessionStatsRTMean=_WwpLeosTwampClientSessionStatsRTMean_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,11),_WwpLeosTwampClientSessionStatsRTMean_Type())
wwpLeosTwampClientSessionStatsRTMean.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsRTMean.setStatus(_A)
_WwpLeosTwampClientSessionStatsRTStdDev_Type=Unsigned32
_WwpLeosTwampClientSessionStatsRTStdDev_Object=MibTableColumn
wwpLeosTwampClientSessionStatsRTStdDev=_WwpLeosTwampClientSessionStatsRTStdDev_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,12),_WwpLeosTwampClientSessionStatsRTStdDev_Type())
wwpLeosTwampClientSessionStatsRTStdDev.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsRTStdDev.setStatus(_A)
_WwpLeosTwampClientSessionStatsRT95th_Type=Unsigned32
_WwpLeosTwampClientSessionStatsRT95th_Object=MibTableColumn
wwpLeosTwampClientSessionStatsRT95th=_WwpLeosTwampClientSessionStatsRT95th_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,13),_WwpLeosTwampClientSessionStatsRT95th_Type())
wwpLeosTwampClientSessionStatsRT95th.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsRT95th.setStatus(_A)
_WwpLeosTwampClientSessionStatsRT99pt9th_Type=Unsigned32
_WwpLeosTwampClientSessionStatsRT99pt9th_Object=MibTableColumn
wwpLeosTwampClientSessionStatsRT99pt9th=_WwpLeosTwampClientSessionStatsRT99pt9th_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,14),_WwpLeosTwampClientSessionStatsRT99pt9th_Type())
wwpLeosTwampClientSessionStatsRT99pt9th.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsRT99pt9th.setStatus(_A)
_WwpLeosTwampClientSessionStatsOWOMin_Type=Unsigned32
_WwpLeosTwampClientSessionStatsOWOMin_Object=MibTableColumn
wwpLeosTwampClientSessionStatsOWOMin=_WwpLeosTwampClientSessionStatsOWOMin_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,15),_WwpLeosTwampClientSessionStatsOWOMin_Type())
wwpLeosTwampClientSessionStatsOWOMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsOWOMin.setStatus(_A)
_WwpLeosTwampClientSessionStatsOWOMax_Type=Unsigned32
_WwpLeosTwampClientSessionStatsOWOMax_Object=MibTableColumn
wwpLeosTwampClientSessionStatsOWOMax=_WwpLeosTwampClientSessionStatsOWOMax_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,16),_WwpLeosTwampClientSessionStatsOWOMax_Type())
wwpLeosTwampClientSessionStatsOWOMax.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsOWOMax.setStatus(_A)
_WwpLeosTwampClientSessionStatsOWOMean_Type=Unsigned32
_WwpLeosTwampClientSessionStatsOWOMean_Object=MibTableColumn
wwpLeosTwampClientSessionStatsOWOMean=_WwpLeosTwampClientSessionStatsOWOMean_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,17),_WwpLeosTwampClientSessionStatsOWOMean_Type())
wwpLeosTwampClientSessionStatsOWOMean.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsOWOMean.setStatus(_A)
_WwpLeosTwampClientSessionStatsOWOStdDev_Type=Unsigned32
_WwpLeosTwampClientSessionStatsOWOStdDev_Object=MibTableColumn
wwpLeosTwampClientSessionStatsOWOStdDev=_WwpLeosTwampClientSessionStatsOWOStdDev_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,18),_WwpLeosTwampClientSessionStatsOWOStdDev_Type())
wwpLeosTwampClientSessionStatsOWOStdDev.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsOWOStdDev.setStatus(_A)
_WwpLeosTwampClientSessionStatsOWO95th_Type=Unsigned32
_WwpLeosTwampClientSessionStatsOWO95th_Object=MibTableColumn
wwpLeosTwampClientSessionStatsOWO95th=_WwpLeosTwampClientSessionStatsOWO95th_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,19),_WwpLeosTwampClientSessionStatsOWO95th_Type())
wwpLeosTwampClientSessionStatsOWO95th.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsOWO95th.setStatus(_A)
_WwpLeosTwampClientSessionStatsOWO99pt9th_Type=Unsigned32
_WwpLeosTwampClientSessionStatsOWO99pt9th_Object=MibTableColumn
wwpLeosTwampClientSessionStatsOWO99pt9th=_WwpLeosTwampClientSessionStatsOWO99pt9th_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,20),_WwpLeosTwampClientSessionStatsOWO99pt9th_Type())
wwpLeosTwampClientSessionStatsOWO99pt9th.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsOWO99pt9th.setStatus(_A)
_WwpLeosTwampClientSessionStatsOWBMin_Type=Unsigned32
_WwpLeosTwampClientSessionStatsOWBMin_Object=MibTableColumn
wwpLeosTwampClientSessionStatsOWBMin=_WwpLeosTwampClientSessionStatsOWBMin_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,21),_WwpLeosTwampClientSessionStatsOWBMin_Type())
wwpLeosTwampClientSessionStatsOWBMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsOWBMin.setStatus(_A)
_WwpLeosTwampClientSessionStatsOWBMax_Type=Unsigned32
_WwpLeosTwampClientSessionStatsOWBMax_Object=MibTableColumn
wwpLeosTwampClientSessionStatsOWBMax=_WwpLeosTwampClientSessionStatsOWBMax_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,22),_WwpLeosTwampClientSessionStatsOWBMax_Type())
wwpLeosTwampClientSessionStatsOWBMax.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsOWBMax.setStatus(_A)
_WwpLeosTwampClientSessionStatsOWBMean_Type=Unsigned32
_WwpLeosTwampClientSessionStatsOWBMean_Object=MibTableColumn
wwpLeosTwampClientSessionStatsOWBMean=_WwpLeosTwampClientSessionStatsOWBMean_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,23),_WwpLeosTwampClientSessionStatsOWBMean_Type())
wwpLeosTwampClientSessionStatsOWBMean.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsOWBMean.setStatus(_A)
_WwpLeosTwampClientSessionStatsOWBStdDev_Type=Unsigned32
_WwpLeosTwampClientSessionStatsOWBStdDev_Object=MibTableColumn
wwpLeosTwampClientSessionStatsOWBStdDev=_WwpLeosTwampClientSessionStatsOWBStdDev_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,24),_WwpLeosTwampClientSessionStatsOWBStdDev_Type())
wwpLeosTwampClientSessionStatsOWBStdDev.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsOWBStdDev.setStatus(_A)
_WwpLeosTwampClientSessionStatsOWB95th_Type=Unsigned32
_WwpLeosTwampClientSessionStatsOWB95th_Object=MibTableColumn
wwpLeosTwampClientSessionStatsOWB95th=_WwpLeosTwampClientSessionStatsOWB95th_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,25),_WwpLeosTwampClientSessionStatsOWB95th_Type())
wwpLeosTwampClientSessionStatsOWB95th.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsOWB95th.setStatus(_A)
_WwpLeosTwampClientSessionStatsOWB99pt9th_Type=Unsigned32
_WwpLeosTwampClientSessionStatsOWB99pt9th_Object=MibTableColumn
wwpLeosTwampClientSessionStatsOWB99pt9th=_WwpLeosTwampClientSessionStatsOWB99pt9th_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,26),_WwpLeosTwampClientSessionStatsOWB99pt9th_Type())
wwpLeosTwampClientSessionStatsOWB99pt9th.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsOWB99pt9th.setStatus(_A)
_WwpLeosTwampClientSessionStatsTPMin_Type=Unsigned32
_WwpLeosTwampClientSessionStatsTPMin_Object=MibTableColumn
wwpLeosTwampClientSessionStatsTPMin=_WwpLeosTwampClientSessionStatsTPMin_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,27),_WwpLeosTwampClientSessionStatsTPMin_Type())
wwpLeosTwampClientSessionStatsTPMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsTPMin.setStatus(_A)
_WwpLeosTwampClientSessionStatsTPMax_Type=Unsigned32
_WwpLeosTwampClientSessionStatsTPMax_Object=MibTableColumn
wwpLeosTwampClientSessionStatsTPMax=_WwpLeosTwampClientSessionStatsTPMax_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,28),_WwpLeosTwampClientSessionStatsTPMax_Type())
wwpLeosTwampClientSessionStatsTPMax.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsTPMax.setStatus(_A)
_WwpLeosTwampClientSessionStatsTPMean_Type=Unsigned32
_WwpLeosTwampClientSessionStatsTPMean_Object=MibTableColumn
wwpLeosTwampClientSessionStatsTPMean=_WwpLeosTwampClientSessionStatsTPMean_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,29),_WwpLeosTwampClientSessionStatsTPMean_Type())
wwpLeosTwampClientSessionStatsTPMean.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsTPMean.setStatus(_A)
_WwpLeosTwampClientSessionStatsTPStdDev_Type=Unsigned32
_WwpLeosTwampClientSessionStatsTPStdDev_Object=MibTableColumn
wwpLeosTwampClientSessionStatsTPStdDev=_WwpLeosTwampClientSessionStatsTPStdDev_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,30),_WwpLeosTwampClientSessionStatsTPStdDev_Type())
wwpLeosTwampClientSessionStatsTPStdDev.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsTPStdDev.setStatus(_A)
_WwpLeosTwampClientSessionStatsTP95th_Type=Unsigned32
_WwpLeosTwampClientSessionStatsTP95th_Object=MibTableColumn
wwpLeosTwampClientSessionStatsTP95th=_WwpLeosTwampClientSessionStatsTP95th_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,31),_WwpLeosTwampClientSessionStatsTP95th_Type())
wwpLeosTwampClientSessionStatsTP95th.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsTP95th.setStatus(_A)
_WwpLeosTwampClientSessionStatsTP99pt9th_Type=Unsigned32
_WwpLeosTwampClientSessionStatsTP99pt9th_Object=MibTableColumn
wwpLeosTwampClientSessionStatsTP99pt9th=_WwpLeosTwampClientSessionStatsTP99pt9th_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,11,1,32),_WwpLeosTwampClientSessionStatsTP99pt9th_Type())
wwpLeosTwampClientSessionStatsTP99pt9th.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampClientSessionStatsTP99pt9th.setStatus(_A)
class _WwpLeosTwampClientDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_WwpLeosTwampClientDscp_Type.__name__=_C
_WwpLeosTwampClientDscp_Object=MibScalar
wwpLeosTwampClientDscp=_WwpLeosTwampClientDscp_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,12),_WwpLeosTwampClientDscp_Type())
wwpLeosTwampClientDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampClientDscp.setStatus(_A)
class _WwpLeosTwampServerDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_WwpLeosTwampServerDscp_Type.__name__=_C
_WwpLeosTwampServerDscp_Object=MibScalar
wwpLeosTwampServerDscp=_WwpLeosTwampServerDscp_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,13),_WwpLeosTwampServerDscp_Type())
wwpLeosTwampServerDscp.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampServerDscp.setStatus(_A)
class _WwpLeosTwampClientHwAssist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_N,2)))
_WwpLeosTwampClientHwAssist_Type.__name__=_C
_WwpLeosTwampClientHwAssist_Object=MibScalar
wwpLeosTwampClientHwAssist=_WwpLeosTwampClientHwAssist_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,14),_WwpLeosTwampClientHwAssist_Type())
wwpLeosTwampClientHwAssist.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampClientHwAssist.setStatus(_A)
class _WwpLeosTwampServerHwAssist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_N,2)))
_WwpLeosTwampServerHwAssist_Type.__name__=_C
_WwpLeosTwampServerHwAssist_Object=MibScalar
wwpLeosTwampServerHwAssist=_WwpLeosTwampServerHwAssist_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,15),_WwpLeosTwampServerHwAssist_Type())
wwpLeosTwampServerHwAssist.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosTwampServerHwAssist.setStatus(_A)
_WwpLeosTwampServerCtrlSessionsTable_Object=MibTable
wwpLeosTwampServerCtrlSessionsTable=_WwpLeosTwampServerCtrlSessionsTable_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,16))
if mibBuilder.loadTexts:wwpLeosTwampServerCtrlSessionsTable.setStatus(_A)
_WwpLeosTwampServerCtrlSessionEntry_Object=MibTableRow
wwpLeosTwampServerCtrlSessionEntry=_WwpLeosTwampServerCtrlSessionEntry_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,16,1))
wwpLeosTwampServerCtrlSessionEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:wwpLeosTwampServerCtrlSessionEntry.setStatus(_A)
class _WwpLeosTwampServerCtrlSessionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_WwpLeosTwampServerCtrlSessionId_Type.__name__=_C
_WwpLeosTwampServerCtrlSessionId_Object=MibTableColumn
wwpLeosTwampServerCtrlSessionId=_WwpLeosTwampServerCtrlSessionId_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,16,1,1),_WwpLeosTwampServerCtrlSessionId_Type())
wwpLeosTwampServerCtrlSessionId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampServerCtrlSessionId.setStatus(_A)
class _WwpLeosTwampServerCtrlSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_Q,0),('greet',1),('start',2),(_R,3),('test',4),(_J,5),(_K,6)))
_WwpLeosTwampServerCtrlSessionState_Type.__name__=_C
_WwpLeosTwampServerCtrlSessionState_Object=MibTableColumn
wwpLeosTwampServerCtrlSessionState=_WwpLeosTwampServerCtrlSessionState_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,16,1,2),_WwpLeosTwampServerCtrlSessionState_Type())
wwpLeosTwampServerCtrlSessionState.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampServerCtrlSessionState.setStatus(_A)
class _WwpLeosTwampServerCtrlSessionPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosTwampServerCtrlSessionPort_Type.__name__=_C
_WwpLeosTwampServerCtrlSessionPort_Object=MibTableColumn
wwpLeosTwampServerCtrlSessionPort=_WwpLeosTwampServerCtrlSessionPort_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,16,1,3),_WwpLeosTwampServerCtrlSessionPort_Type())
wwpLeosTwampServerCtrlSessionPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampServerCtrlSessionPort.setStatus(_A)
_WwpLeosTwampServerCtrlSessionHost_Type=IpAddress
_WwpLeosTwampServerCtrlSessionHost_Object=MibTableColumn
wwpLeosTwampServerCtrlSessionHost=_WwpLeosTwampServerCtrlSessionHost_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,16,1,4),_WwpLeosTwampServerCtrlSessionHost_Type())
wwpLeosTwampServerCtrlSessionHost.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampServerCtrlSessionHost.setStatus(_A)
_WwpLeosTwampServerCtrlSessionTestMap_Type=Unsigned32
_WwpLeosTwampServerCtrlSessionTestMap_Object=MibTableColumn
wwpLeosTwampServerCtrlSessionTestMap=_WwpLeosTwampServerCtrlSessionTestMap_Object((1,3,6,1,4,1,6141,2,60,40,1,1,1,16,1,5),_WwpLeosTwampServerCtrlSessionTestMap_Type())
wwpLeosTwampServerCtrlSessionTestMap.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosTwampServerCtrlSessionTestMap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'wwpLeosTwampMIB':wwpLeosTwampMIB,'wwpLeosTwampMIBObjects':wwpLeosTwampMIBObjects,'wwpLeosTwamp':wwpLeosTwamp,'wwpLeosTwampModule':wwpLeosTwampModule,'wwpLeosTwampPort':wwpLeosTwampPort,'wwpLeosTwampEnable':wwpLeosTwampEnable,'wwpLeosTwampPortEnableTable':wwpLeosTwampPortEnableTable,'wwpLeosTwampPortEnableEntry':wwpLeosTwampPortEnableEntry,_O:wwpLeosTwampPortId,'wwpLeosTwampPortEnableState':wwpLeosTwampPortEnableState,'wwpLeosTwampClientEnable':wwpLeosTwampClientEnable,'wwpLeosTwampServerEnable':wwpLeosTwampServerEnable,'wwpLeosTwampLightEnable':wwpLeosTwampLightEnable,'wwpLeosTwampServerSessionsTable':wwpLeosTwampServerSessionsTable,'wwpLeosTwampServerSessionEntry':wwpLeosTwampServerSessionEntry,_P:wwpLeosTwampServerSessionId,'wwpLeosTwampServerSessionState':wwpLeosTwampServerSessionState,'wwpLeosTwampServerSessionPort':wwpLeosTwampServerSessionPort,'wwpLeosTwampServerSessionHost':wwpLeosTwampServerSessionHost,'wwpLeosTwampServerSessionNumPkts':wwpLeosTwampServerSessionNumPkts,'wwpLeosTwampServerSessionSeqNum':wwpLeosTwampServerSessionSeqNum,'wwpLeosTwampServerSessionHwAssist':wwpLeosTwampServerSessionHwAssist,'wwpLeosTwampTimeout':wwpLeosTwampTimeout,'wwpLeosTwampClientSessionsTable':wwpLeosTwampClientSessionsTable,'wwpLeosTwampClientSessionEntry':wwpLeosTwampClientSessionEntry,_S:wwpLeosTwampClientSessionId,'wwpLeosTwampClientSessionStatus':wwpLeosTwampClientSessionStatus,'wwpLeosTwampClientSessionName':wwpLeosTwampClientSessionName,'wwpLeosTwampClientSessionHost':wwpLeosTwampClientSessionHost,'wwpLeosTwampClientSessionState':wwpLeosTwampClientSessionState,'wwpLeosTwampClientSessionCommPort':wwpLeosTwampClientSessionCommPort,'wwpLeosTwampClientSessionCosPolicy':wwpLeosTwampClientSessionCosPolicy,'wwpLeosTwampClientSessionDscp':wwpLeosTwampClientSessionDscp,'wwpLeosTwampClientSessionIpPrec':wwpLeosTwampClientSessionIpPrec,'wwpLeosTwampClientSessionType':wwpLeosTwampClientSessionType,'wwpLeosTwampClientSessionPktSize':wwpLeosTwampClientSessionPktSize,'wwpLeosTwampClientSessionRepeat':wwpLeosTwampClientSessionRepeat,'wwpLeosTwampClientSessionSeqNum':wwpLeosTwampClientSessionSeqNum,'wwpLeosTwampClientSessionNumPkts':wwpLeosTwampClientSessionNumPkts,'wwpLeosTwampClientSessionRxHw':wwpLeosTwampClientSessionRxHw,'wwpLeosTwampClientSessionTxHw':wwpLeosTwampClientSessionTxHw,'wwpLeosTwampClientSessionDot1dpri':wwpLeosTwampClientSessionDot1dpri,'wwpLeosTwampClientSessionsStatisticsTable':wwpLeosTwampClientSessionsStatisticsTable,'wwpLeosTwampClientSessionStatisticsEntry':wwpLeosTwampClientSessionStatisticsEntry,_T:wwpLeosTwampClientSessionStatsIndex,_U:wwpLeosTwampClientStatsRecordIndex,'wwpLeosTwampClientSessionStatsName':wwpLeosTwampClientSessionStatsName,'wwpLeosTwampClientSessionTimestamp':wwpLeosTwampClientSessionTimestamp,'wwpLeosTwampClientSessionStatsPktTx':wwpLeosTwampClientSessionStatsPktTx,'wwpLeosTwampClientSessionStatsPktRx':wwpLeosTwampClientSessionStatsPktRx,'wwpLeosTwampClientSessionStatsPktOL':wwpLeosTwampClientSessionStatsPktOL,'wwpLeosTwampClientSessionStatsPktRL':wwpLeosTwampClientSessionStatsPktRL,'wwpLeosTwampClientSessionStatsRTMin':wwpLeosTwampClientSessionStatsRTMin,'wwpLeosTwampClientSessionStatsRTMax':wwpLeosTwampClientSessionStatsRTMax,'wwpLeosTwampClientSessionStatsRTMean':wwpLeosTwampClientSessionStatsRTMean,'wwpLeosTwampClientSessionStatsRTStdDev':wwpLeosTwampClientSessionStatsRTStdDev,'wwpLeosTwampClientSessionStatsRT95th':wwpLeosTwampClientSessionStatsRT95th,'wwpLeosTwampClientSessionStatsRT99pt9th':wwpLeosTwampClientSessionStatsRT99pt9th,'wwpLeosTwampClientSessionStatsOWOMin':wwpLeosTwampClientSessionStatsOWOMin,'wwpLeosTwampClientSessionStatsOWOMax':wwpLeosTwampClientSessionStatsOWOMax,'wwpLeosTwampClientSessionStatsOWOMean':wwpLeosTwampClientSessionStatsOWOMean,'wwpLeosTwampClientSessionStatsOWOStdDev':wwpLeosTwampClientSessionStatsOWOStdDev,'wwpLeosTwampClientSessionStatsOWO95th':wwpLeosTwampClientSessionStatsOWO95th,'wwpLeosTwampClientSessionStatsOWO99pt9th':wwpLeosTwampClientSessionStatsOWO99pt9th,'wwpLeosTwampClientSessionStatsOWBMin':wwpLeosTwampClientSessionStatsOWBMin,'wwpLeosTwampClientSessionStatsOWBMax':wwpLeosTwampClientSessionStatsOWBMax,'wwpLeosTwampClientSessionStatsOWBMean':wwpLeosTwampClientSessionStatsOWBMean,'wwpLeosTwampClientSessionStatsOWBStdDev':wwpLeosTwampClientSessionStatsOWBStdDev,'wwpLeosTwampClientSessionStatsOWB95th':wwpLeosTwampClientSessionStatsOWB95th,'wwpLeosTwampClientSessionStatsOWB99pt9th':wwpLeosTwampClientSessionStatsOWB99pt9th,'wwpLeosTwampClientSessionStatsTPMin':wwpLeosTwampClientSessionStatsTPMin,'wwpLeosTwampClientSessionStatsTPMax':wwpLeosTwampClientSessionStatsTPMax,'wwpLeosTwampClientSessionStatsTPMean':wwpLeosTwampClientSessionStatsTPMean,'wwpLeosTwampClientSessionStatsTPStdDev':wwpLeosTwampClientSessionStatsTPStdDev,'wwpLeosTwampClientSessionStatsTP95th':wwpLeosTwampClientSessionStatsTP95th,'wwpLeosTwampClientSessionStatsTP99pt9th':wwpLeosTwampClientSessionStatsTP99pt9th,'wwpLeosTwampClientDscp':wwpLeosTwampClientDscp,'wwpLeosTwampServerDscp':wwpLeosTwampServerDscp,'wwpLeosTwampClientHwAssist':wwpLeosTwampClientHwAssist,'wwpLeosTwampServerHwAssist':wwpLeosTwampServerHwAssist,'wwpLeosTwampServerCtrlSessionsTable':wwpLeosTwampServerCtrlSessionsTable,'wwpLeosTwampServerCtrlSessionEntry':wwpLeosTwampServerCtrlSessionEntry,_V:wwpLeosTwampServerCtrlSessionId,'wwpLeosTwampServerCtrlSessionState':wwpLeosTwampServerCtrlSessionState,'wwpLeosTwampServerCtrlSessionPort':wwpLeosTwampServerCtrlSessionPort,'wwpLeosTwampServerCtrlSessionHost':wwpLeosTwampServerCtrlSessionHost,'wwpLeosTwampServerCtrlSessionTestMap':wwpLeosTwampServerCtrlSessionTestMap})