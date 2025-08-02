_S='prevState'
_R='newState'
_Q='channelPort'
_P='channelDescr'
_O='channelIndex'
_N='pl2TrapValue64'
_M='pl2TrapThreshold64'
_L='pl2TrapValue'
_K='pl2TrapThreshold'
_J='fd-10000'
_I='fd-1000'
_H='fd-100'
_G='hd-100'
_F='pl2TrapOid'
_E='pl2TrapMessage'
_D='Integer32'
_C='read-only'
_B='PACKETLOGIC-TRAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
packetlogic2,=mibBuilder.importSymbols('PACKETLOGIC-MIB','packetlogic2')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
pl2Trap=ModuleIdentity((1,3,6,1,4,1,15397,2,8))
if mibBuilder.loadTexts:pl2Trap.setRevisions(('2012-12-13 13:22',))
_Pl2Traps_ObjectIdentity=ObjectIdentity
pl2Traps=_Pl2Traps_ObjectIdentity((1,3,6,1,4,1,15397,2,8,0))
_Pl2TrapVals_ObjectIdentity=ObjectIdentity
pl2TrapVals=_Pl2TrapVals_ObjectIdentity((1,3,6,1,4,1,15397,2,8,1))
_Pl2TrapMessage_Type=DisplayString
_Pl2TrapMessage_Object=MibScalar
pl2TrapMessage=_Pl2TrapMessage_Object((1,3,6,1,4,1,15397,2,8,1,1),_Pl2TrapMessage_Type())
pl2TrapMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:pl2TrapMessage.setStatus(_A)
_Pl2TrapOid_Type=ObjectIdentifier
_Pl2TrapOid_Object=MibScalar
pl2TrapOid=_Pl2TrapOid_Object((1,3,6,1,4,1,15397,2,8,1,2),_Pl2TrapOid_Type())
pl2TrapOid.setMaxAccess(_C)
if mibBuilder.loadTexts:pl2TrapOid.setStatus(_A)
_Pl2TrapValue_Type=Unsigned32
_Pl2TrapValue_Object=MibScalar
pl2TrapValue=_Pl2TrapValue_Object((1,3,6,1,4,1,15397,2,8,1,3),_Pl2TrapValue_Type())
pl2TrapValue.setMaxAccess(_C)
if mibBuilder.loadTexts:pl2TrapValue.setStatus(_A)
_Pl2TrapThreshold_Type=Unsigned32
_Pl2TrapThreshold_Object=MibScalar
pl2TrapThreshold=_Pl2TrapThreshold_Object((1,3,6,1,4,1,15397,2,8,1,4),_Pl2TrapThreshold_Type())
pl2TrapThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:pl2TrapThreshold.setStatus(_A)
_Pl2TrapValue64_Type=Counter64
_Pl2TrapValue64_Object=MibScalar
pl2TrapValue64=_Pl2TrapValue64_Object((1,3,6,1,4,1,15397,2,8,1,5),_Pl2TrapValue64_Type())
pl2TrapValue64.setMaxAccess(_C)
if mibBuilder.loadTexts:pl2TrapValue64.setStatus(_A)
_Pl2TrapThreshold64_Type=Counter64
_Pl2TrapThreshold64_Object=MibScalar
pl2TrapThreshold64=_Pl2TrapThreshold64_Object((1,3,6,1,4,1,15397,2,8,1,6),_Pl2TrapThreshold64_Type())
pl2TrapThreshold64.setMaxAccess(_C)
if mibBuilder.loadTexts:pl2TrapThreshold64.setStatus(_A)
_Pl2ChannelTraps_ObjectIdentity=ObjectIdentity
pl2ChannelTraps=_Pl2ChannelTraps_ObjectIdentity((1,3,6,1,4,1,15397,2,8,2))
_Pl2ChannelTrapVals_ObjectIdentity=ObjectIdentity
pl2ChannelTrapVals=_Pl2ChannelTrapVals_ObjectIdentity((1,3,6,1,4,1,15397,2,8,3))
_ChannelIndex_Type=Unsigned32
_ChannelIndex_Object=MibScalar
channelIndex=_ChannelIndex_Object((1,3,6,1,4,1,15397,2,8,3,1),_ChannelIndex_Type())
channelIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:channelIndex.setStatus(_A)
_ChannelDescr_Type=DisplayString
_ChannelDescr_Object=MibScalar
channelDescr=_ChannelDescr_Object((1,3,6,1,4,1,15397,2,8,3,2),_ChannelDescr_Type())
channelDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:channelDescr.setStatus(_A)
class _ChannelPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('external',0),('internal',1)))
_ChannelPort_Type.__name__=_D
_ChannelPort_Object=MibScalar
channelPort=_ChannelPort_Object((1,3,6,1,4,1,15397,2,8,3,3),_ChannelPort_Type())
channelPort.setMaxAccess(_C)
if mibBuilder.loadTexts:channelPort.setStatus(_A)
class _PrevState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('auto',0),('hd-10',1),('fd-10',2),(_G,3),(_H,4),(_I,5),(_J,6)))
_PrevState_Type.__name__=_D
_PrevState_Object=MibScalar
prevState=_PrevState_Object((1,3,6,1,4,1,15397,2,8,3,4),_PrevState_Type())
prevState.setMaxAccess(_C)
if mibBuilder.loadTexts:prevState.setStatus(_A)
class _NewState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('auto',0),('hd-10',1),('fd-10',2),(_G,3),(_H,4),(_I,5),(_J,6)))
_NewState_Type.__name__=_D
_NewState_Object=MibScalar
newState=_NewState_Object((1,3,6,1,4,1,15397,2,8,3,5),_NewState_Type())
newState.setMaxAccess(_C)
if mibBuilder.loadTexts:newState.setStatus(_A)
pl2TrapGenericMsg=NotificationType((1,3,6,1,4,1,15397,2,8,0,1))
pl2TrapGenericMsg.setObjects((_B,_E))
if mibBuilder.loadTexts:pl2TrapGenericMsg.setStatus(_A)
pl2TrapGeneric=NotificationType((1,3,6,1,4,1,15397,2,8,0,2))
if mibBuilder.loadTexts:pl2TrapGeneric.setStatus(_A)
pl2TrapSystemStatsAlert=NotificationType((1,3,6,1,4,1,15397,2,8,0,3))
pl2TrapSystemStatsAlert.setObjects(*((_B,_K),(_B,_E),(_B,_L),(_B,_F)))
if mibBuilder.loadTexts:pl2TrapSystemStatsAlert.setStatus(_A)
pl2TrapSystemStatsAlert64=NotificationType((1,3,6,1,4,1,15397,2,8,0,4))
pl2TrapSystemStatsAlert64.setObjects(*((_B,_M),(_B,_E),(_B,_N),(_B,_F)))
if mibBuilder.loadTexts:pl2TrapSystemStatsAlert64.setStatus(_A)
pl2TrapSystemStatsAlertClear=NotificationType((1,3,6,1,4,1,15397,2,8,0,5))
pl2TrapSystemStatsAlertClear.setObjects((_B,_F))
if mibBuilder.loadTexts:pl2TrapSystemStatsAlertClear.setStatus(_A)
pl2ChannelStateChanged=NotificationType((1,3,6,1,4,1,15397,2,8,2,1))
pl2ChannelStateChanged.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:pl2ChannelStateChanged.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pl2Trap':pl2Trap,'pl2Traps':pl2Traps,'pl2TrapGenericMsg':pl2TrapGenericMsg,'pl2TrapGeneric':pl2TrapGeneric,'pl2TrapSystemStatsAlert':pl2TrapSystemStatsAlert,'pl2TrapSystemStatsAlert64':pl2TrapSystemStatsAlert64,'pl2TrapSystemStatsAlertClear':pl2TrapSystemStatsAlertClear,'pl2TrapVals':pl2TrapVals,_E:pl2TrapMessage,_F:pl2TrapOid,_L:pl2TrapValue,_K:pl2TrapThreshold,_N:pl2TrapValue64,_M:pl2TrapThreshold64,'pl2ChannelTraps':pl2ChannelTraps,'pl2ChannelStateChanged':pl2ChannelStateChanged,'pl2ChannelTrapVals':pl2ChannelTrapVals,_O:channelIndex,_P:channelDescr,_Q:channelPort,_S:prevState,_R:newState})