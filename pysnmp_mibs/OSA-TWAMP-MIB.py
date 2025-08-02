_j='osaTwampNotificationGroup'
_i='osaTwampMandatoryGroup'
_h='osaTwampMaxSessionsExceeded'
_g='osaTwampResponderSessionState'
_f='osaTwampResponderSessionSequenceNumber'
_e='osaTwampResponderSessionRemoteClientUdpPort'
_d='osaTwampResponderSessionSourceUdpPort'
_c='osaTwampResponderSessionRemoteClientIpAddress'
_b='osaTwampResponderSessionSourceIpAddress'
_a='osaTwampResponderSessionVlanTag'
_Z='osaTwampResponderSessionAgingTimeout'
_Y='osaTwampResponderSessionIdleTimeout'
_X='osaTwampResponderRowStatus'
_W='osaTwampResponderState'
_V='osaTwampResponderSequenceAction'
_U='osaTwampResponderRemoteClientUdpPort'
_T='osaTwampResponderSourceUdpPort'
_S='osaTwampResponderRemoteClientIpAddress'
_R='osaTwampResponderSourceIpAddress'
_Q='osaTwampResponderVlanTag'
_P='osaTwampResponderAgingTimeout'
_O='osaTwampResponderIdleTimeout'
_N='osaTwampResponderControlMode'
_M='osaTwampResponderAlias'
_L='osaTwampResponderIgnoreEs'
_K='osaTwampResponderSessionIndex'
_J='osaTwampResponderServerIndex'
_I='osaTwampResponderIndex'
_H='not-accessible'
_G='DisplayString'
_F='Unsigned32'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='OSA-TWAMP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
advaMIB,=mibBuilder.importSymbols('ADVA-MIB','advaMIB')
VlanId,=mibBuilder.importSymbols('IEEE8021-CFM-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention')
osaTwamp=ModuleIdentity((1,3,6,1,4,1,2544,8))
if mibBuilder.loadTexts:osaTwamp.setRevisions(('2021-08-15 00:00',))
_OsaTwampNotifications_ObjectIdentity=ObjectIdentity
osaTwampNotifications=_OsaTwampNotifications_ObjectIdentity((1,3,6,1,4,1,2544,8,0))
_OsaTwampGlobals_ObjectIdentity=ObjectIdentity
osaTwampGlobals=_OsaTwampGlobals_ObjectIdentity((1,3,6,1,4,1,2544,8,1))
class _OsaTwampResponderIgnoreEs_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ignore',1),('notIgnore',2)))
_OsaTwampResponderIgnoreEs_Type.__name__=_E
_OsaTwampResponderIgnoreEs_Object=MibScalar
osaTwampResponderIgnoreEs=_OsaTwampResponderIgnoreEs_Object((1,3,6,1,4,1,2544,8,1,1),_OsaTwampResponderIgnoreEs_Type())
osaTwampResponderIgnoreEs.setMaxAccess('read-write')
if mibBuilder.loadTexts:osaTwampResponderIgnoreEs.setStatus(_A)
_OsaTwampResponderTable_Object=MibTable
osaTwampResponderTable=_OsaTwampResponderTable_Object((1,3,6,1,4,1,2544,8,2))
if mibBuilder.loadTexts:osaTwampResponderTable.setStatus(_A)
_OsaTwampResponderEntry_Object=MibTableRow
osaTwampResponderEntry=_OsaTwampResponderEntry_Object((1,3,6,1,4,1,2544,8,2,1))
osaTwampResponderEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:osaTwampResponderEntry.setStatus(_A)
class _OsaTwampResponderIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OsaTwampResponderIndex_Type.__name__=_E
_OsaTwampResponderIndex_Object=MibTableColumn
osaTwampResponderIndex=_OsaTwampResponderIndex_Object((1,3,6,1,4,1,2544,8,2,1,1),_OsaTwampResponderIndex_Type())
osaTwampResponderIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:osaTwampResponderIndex.setStatus(_A)
class _OsaTwampResponderAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_OsaTwampResponderAlias_Type.__name__=_G
_OsaTwampResponderAlias_Object=MibTableColumn
osaTwampResponderAlias=_OsaTwampResponderAlias_Object((1,3,6,1,4,1,2544,8,2,1,2),_OsaTwampResponderAlias_Type())
osaTwampResponderAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:osaTwampResponderAlias.setStatus(_A)
class _OsaTwampResponderControlMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('controlDisabled',1),('controlEnabled',2)))
_OsaTwampResponderControlMode_Type.__name__=_E
_OsaTwampResponderControlMode_Object=MibTableColumn
osaTwampResponderControlMode=_OsaTwampResponderControlMode_Object((1,3,6,1,4,1,2544,8,2,1,3),_OsaTwampResponderControlMode_Type())
osaTwampResponderControlMode.setMaxAccess(_C)
if mibBuilder.loadTexts:osaTwampResponderControlMode.setStatus(_A)
class _OsaTwampResponderIdleTimeout_Type(Unsigned32):defaultValue=5
_OsaTwampResponderIdleTimeout_Type.__name__=_F
_OsaTwampResponderIdleTimeout_Object=MibTableColumn
osaTwampResponderIdleTimeout=_OsaTwampResponderIdleTimeout_Object((1,3,6,1,4,1,2544,8,2,1,4),_OsaTwampResponderIdleTimeout_Type())
osaTwampResponderIdleTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:osaTwampResponderIdleTimeout.setStatus(_A)
class _OsaTwampResponderAgingTimeout_Type(Unsigned32):defaultValue=900;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9000))
_OsaTwampResponderAgingTimeout_Type.__name__=_F
_OsaTwampResponderAgingTimeout_Object=MibTableColumn
osaTwampResponderAgingTimeout=_OsaTwampResponderAgingTimeout_Object((1,3,6,1,4,1,2544,8,2,1,5),_OsaTwampResponderAgingTimeout_Type())
osaTwampResponderAgingTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:osaTwampResponderAgingTimeout.setStatus(_A)
_OsaTwampResponderVlanTag_Type=VlanId
_OsaTwampResponderVlanTag_Object=MibTableColumn
osaTwampResponderVlanTag=_OsaTwampResponderVlanTag_Object((1,3,6,1,4,1,2544,8,2,1,6),_OsaTwampResponderVlanTag_Type())
osaTwampResponderVlanTag.setMaxAccess(_C)
if mibBuilder.loadTexts:osaTwampResponderVlanTag.setStatus(_A)
class _OsaTwampResponderSourceIpAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,48))
_OsaTwampResponderSourceIpAddress_Type.__name__=_G
_OsaTwampResponderSourceIpAddress_Object=MibTableColumn
osaTwampResponderSourceIpAddress=_OsaTwampResponderSourceIpAddress_Object((1,3,6,1,4,1,2544,8,2,1,7),_OsaTwampResponderSourceIpAddress_Type())
osaTwampResponderSourceIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:osaTwampResponderSourceIpAddress.setStatus(_A)
class _OsaTwampResponderRemoteClientIpAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,48))
_OsaTwampResponderRemoteClientIpAddress_Type.__name__=_G
_OsaTwampResponderRemoteClientIpAddress_Object=MibTableColumn
osaTwampResponderRemoteClientIpAddress=_OsaTwampResponderRemoteClientIpAddress_Object((1,3,6,1,4,1,2544,8,2,1,8),_OsaTwampResponderRemoteClientIpAddress_Type())
osaTwampResponderRemoteClientIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:osaTwampResponderRemoteClientIpAddress.setStatus(_A)
class _OsaTwampResponderSourceUdpPort_Type(Unsigned32):defaultValue=862;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OsaTwampResponderSourceUdpPort_Type.__name__=_F
_OsaTwampResponderSourceUdpPort_Object=MibTableColumn
osaTwampResponderSourceUdpPort=_OsaTwampResponderSourceUdpPort_Object((1,3,6,1,4,1,2544,8,2,1,9),_OsaTwampResponderSourceUdpPort_Type())
osaTwampResponderSourceUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:osaTwampResponderSourceUdpPort.setStatus(_A)
class _OsaTwampResponderRemoteClientUdpPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OsaTwampResponderRemoteClientUdpPort_Type.__name__=_F
_OsaTwampResponderRemoteClientUdpPort_Object=MibTableColumn
osaTwampResponderRemoteClientUdpPort=_OsaTwampResponderRemoteClientUdpPort_Object((1,3,6,1,4,1,2544,8,2,1,10),_OsaTwampResponderRemoteClientUdpPort_Type())
osaTwampResponderRemoteClientUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:osaTwampResponderRemoteClientUdpPort.setStatus(_A)
class _OsaTwampResponderSequenceAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAction',1),('clearSequenceNumber',2)))
_OsaTwampResponderSequenceAction_Type.__name__=_E
_OsaTwampResponderSequenceAction_Object=MibTableColumn
osaTwampResponderSequenceAction=_OsaTwampResponderSequenceAction_Object((1,3,6,1,4,1,2544,8,2,1,11),_OsaTwampResponderSequenceAction_Type())
osaTwampResponderSequenceAction.setMaxAccess(_C)
if mibBuilder.loadTexts:osaTwampResponderSequenceAction.setStatus(_A)
class _OsaTwampResponderState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('init',1),('testReady',2),('waitingForTransitTimeout',3),('end',4)))
_OsaTwampResponderState_Type.__name__=_E
_OsaTwampResponderState_Object=MibTableColumn
osaTwampResponderState=_OsaTwampResponderState_Object((1,3,6,1,4,1,2544,8,2,1,12),_OsaTwampResponderState_Type())
osaTwampResponderState.setMaxAccess(_D)
if mibBuilder.loadTexts:osaTwampResponderState.setStatus(_A)
_OsaTwampResponderRowStatus_Type=RowStatus
_OsaTwampResponderRowStatus_Object=MibTableColumn
osaTwampResponderRowStatus=_OsaTwampResponderRowStatus_Object((1,3,6,1,4,1,2544,8,2,1,13),_OsaTwampResponderRowStatus_Type())
osaTwampResponderRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:osaTwampResponderRowStatus.setStatus(_A)
_OsaTwampResponderSessionTable_Object=MibTable
osaTwampResponderSessionTable=_OsaTwampResponderSessionTable_Object((1,3,6,1,4,1,2544,8,3))
if mibBuilder.loadTexts:osaTwampResponderSessionTable.setStatus(_A)
_OsaTwampResponderSessionEntry_Object=MibTableRow
osaTwampResponderSessionEntry=_OsaTwampResponderSessionEntry_Object((1,3,6,1,4,1,2544,8,3,1))
osaTwampResponderSessionEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:osaTwampResponderSessionEntry.setStatus(_A)
class _OsaTwampResponderServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OsaTwampResponderServerIndex_Type.__name__=_E
_OsaTwampResponderServerIndex_Object=MibTableColumn
osaTwampResponderServerIndex=_OsaTwampResponderServerIndex_Object((1,3,6,1,4,1,2544,8,3,1,1),_OsaTwampResponderServerIndex_Type())
osaTwampResponderServerIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:osaTwampResponderServerIndex.setStatus(_A)
class _OsaTwampResponderSessionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,500))
_OsaTwampResponderSessionIndex_Type.__name__=_E
_OsaTwampResponderSessionIndex_Object=MibTableColumn
osaTwampResponderSessionIndex=_OsaTwampResponderSessionIndex_Object((1,3,6,1,4,1,2544,8,3,1,2),_OsaTwampResponderSessionIndex_Type())
osaTwampResponderSessionIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:osaTwampResponderSessionIndex.setStatus(_A)
class _OsaTwampResponderSessionIdleTimeout_Type(Unsigned32):defaultValue=5
_OsaTwampResponderSessionIdleTimeout_Type.__name__=_F
_OsaTwampResponderSessionIdleTimeout_Object=MibTableColumn
osaTwampResponderSessionIdleTimeout=_OsaTwampResponderSessionIdleTimeout_Object((1,3,6,1,4,1,2544,8,3,1,3),_OsaTwampResponderSessionIdleTimeout_Type())
osaTwampResponderSessionIdleTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:osaTwampResponderSessionIdleTimeout.setStatus(_A)
class _OsaTwampResponderSessionAgingTimeout_Type(Unsigned32):defaultValue=900
_OsaTwampResponderSessionAgingTimeout_Type.__name__=_F
_OsaTwampResponderSessionAgingTimeout_Object=MibTableColumn
osaTwampResponderSessionAgingTimeout=_OsaTwampResponderSessionAgingTimeout_Object((1,3,6,1,4,1,2544,8,3,1,4),_OsaTwampResponderSessionAgingTimeout_Type())
osaTwampResponderSessionAgingTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:osaTwampResponderSessionAgingTimeout.setStatus(_A)
_OsaTwampResponderSessionVlanTag_Type=VlanId
_OsaTwampResponderSessionVlanTag_Object=MibTableColumn
osaTwampResponderSessionVlanTag=_OsaTwampResponderSessionVlanTag_Object((1,3,6,1,4,1,2544,8,3,1,5),_OsaTwampResponderSessionVlanTag_Type())
osaTwampResponderSessionVlanTag.setMaxAccess(_D)
if mibBuilder.loadTexts:osaTwampResponderSessionVlanTag.setStatus(_A)
class _OsaTwampResponderSessionSourceIpAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,48))
_OsaTwampResponderSessionSourceIpAddress_Type.__name__=_G
_OsaTwampResponderSessionSourceIpAddress_Object=MibTableColumn
osaTwampResponderSessionSourceIpAddress=_OsaTwampResponderSessionSourceIpAddress_Object((1,3,6,1,4,1,2544,8,3,1,6),_OsaTwampResponderSessionSourceIpAddress_Type())
osaTwampResponderSessionSourceIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:osaTwampResponderSessionSourceIpAddress.setStatus(_A)
class _OsaTwampResponderSessionRemoteClientIpAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,48))
_OsaTwampResponderSessionRemoteClientIpAddress_Type.__name__=_G
_OsaTwampResponderSessionRemoteClientIpAddress_Object=MibTableColumn
osaTwampResponderSessionRemoteClientIpAddress=_OsaTwampResponderSessionRemoteClientIpAddress_Object((1,3,6,1,4,1,2544,8,3,1,7),_OsaTwampResponderSessionRemoteClientIpAddress_Type())
osaTwampResponderSessionRemoteClientIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:osaTwampResponderSessionRemoteClientIpAddress.setStatus(_A)
class _OsaTwampResponderSessionSourceUdpPort_Type(Unsigned32):defaultValue=862;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OsaTwampResponderSessionSourceUdpPort_Type.__name__=_F
_OsaTwampResponderSessionSourceUdpPort_Object=MibTableColumn
osaTwampResponderSessionSourceUdpPort=_OsaTwampResponderSessionSourceUdpPort_Object((1,3,6,1,4,1,2544,8,3,1,8),_OsaTwampResponderSessionSourceUdpPort_Type())
osaTwampResponderSessionSourceUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:osaTwampResponderSessionSourceUdpPort.setStatus(_A)
class _OsaTwampResponderSessionRemoteClientUdpPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_OsaTwampResponderSessionRemoteClientUdpPort_Type.__name__=_F
_OsaTwampResponderSessionRemoteClientUdpPort_Object=MibTableColumn
osaTwampResponderSessionRemoteClientUdpPort=_OsaTwampResponderSessionRemoteClientUdpPort_Object((1,3,6,1,4,1,2544,8,3,1,9),_OsaTwampResponderSessionRemoteClientUdpPort_Type())
osaTwampResponderSessionRemoteClientUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:osaTwampResponderSessionRemoteClientUdpPort.setStatus(_A)
_OsaTwampResponderSessionSequenceNumber_Type=Unsigned32
_OsaTwampResponderSessionSequenceNumber_Object=MibTableColumn
osaTwampResponderSessionSequenceNumber=_OsaTwampResponderSessionSequenceNumber_Object((1,3,6,1,4,1,2544,8,3,1,10),_OsaTwampResponderSessionSequenceNumber_Type())
osaTwampResponderSessionSequenceNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:osaTwampResponderSessionSequenceNumber.setStatus(_A)
class _OsaTwampResponderSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('init',1),('testInProgress',2),('idle',3)))
_OsaTwampResponderSessionState_Type.__name__=_E
_OsaTwampResponderSessionState_Object=MibTableColumn
osaTwampResponderSessionState=_OsaTwampResponderSessionState_Object((1,3,6,1,4,1,2544,8,3,1,11),_OsaTwampResponderSessionState_Type())
osaTwampResponderSessionState.setMaxAccess(_D)
if mibBuilder.loadTexts:osaTwampResponderSessionState.setStatus(_A)
_OsaTwampConformance_ObjectIdentity=ObjectIdentity
osaTwampConformance=_OsaTwampConformance_ObjectIdentity((1,3,6,1,4,1,2544,8,100))
_OsaTwampMIBCompliances_ObjectIdentity=ObjectIdentity
osaTwampMIBCompliances=_OsaTwampMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2544,8,100,1))
_OsaTwampMIBGroups_ObjectIdentity=ObjectIdentity
osaTwampMIBGroups=_OsaTwampMIBGroups_ObjectIdentity((1,3,6,1,4,1,2544,8,100,2))
osaTwampMandatoryGroup=ObjectGroup((1,3,6,1,4,1,2544,8,100,2,1))
osaTwampMandatoryGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:osaTwampMandatoryGroup.setStatus(_A)
osaTwampMaxSessionsExceeded=NotificationType((1,3,6,1,4,1,2544,8,0,1))
if mibBuilder.loadTexts:osaTwampMaxSessionsExceeded.setStatus(_A)
osaTwampNotificationGroup=NotificationGroup((1,3,6,1,4,1,2544,8,100,2,2))
osaTwampNotificationGroup.setObjects((_B,_h))
if mibBuilder.loadTexts:osaTwampNotificationGroup.setStatus(_A)
osaTwampMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2544,8,100,1,1))
osaTwampMIBCompliance.setObjects(*((_B,_i),(_B,_j)))
if mibBuilder.loadTexts:osaTwampMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'osaTwamp':osaTwamp,'osaTwampNotifications':osaTwampNotifications,_h:osaTwampMaxSessionsExceeded,'osaTwampGlobals':osaTwampGlobals,_L:osaTwampResponderIgnoreEs,'osaTwampResponderTable':osaTwampResponderTable,'osaTwampResponderEntry':osaTwampResponderEntry,_I:osaTwampResponderIndex,_M:osaTwampResponderAlias,_N:osaTwampResponderControlMode,_O:osaTwampResponderIdleTimeout,_P:osaTwampResponderAgingTimeout,_Q:osaTwampResponderVlanTag,_R:osaTwampResponderSourceIpAddress,_S:osaTwampResponderRemoteClientIpAddress,_T:osaTwampResponderSourceUdpPort,_U:osaTwampResponderRemoteClientUdpPort,_V:osaTwampResponderSequenceAction,_W:osaTwampResponderState,_X:osaTwampResponderRowStatus,'osaTwampResponderSessionTable':osaTwampResponderSessionTable,'osaTwampResponderSessionEntry':osaTwampResponderSessionEntry,_J:osaTwampResponderServerIndex,_K:osaTwampResponderSessionIndex,_Y:osaTwampResponderSessionIdleTimeout,_Z:osaTwampResponderSessionAgingTimeout,_a:osaTwampResponderSessionVlanTag,_b:osaTwampResponderSessionSourceIpAddress,_c:osaTwampResponderSessionRemoteClientIpAddress,_d:osaTwampResponderSessionSourceUdpPort,_e:osaTwampResponderSessionRemoteClientUdpPort,_f:osaTwampResponderSessionSequenceNumber,_g:osaTwampResponderSessionState,'osaTwampConformance':osaTwampConformance,'osaTwampMIBCompliances':osaTwampMIBCompliances,'osaTwampMIBCompliance':osaTwampMIBCompliance,'osaTwampMIBGroups':osaTwampMIBGroups,_i:osaTwampMandatoryGroup,_j:osaTwampNotificationGroup})