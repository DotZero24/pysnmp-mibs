_E='rlSocketId'
_D='RADLAN-SOCKET-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rlSocket=ModuleIdentity((1,3,6,1,4,1,89,85))
if mibBuilder.loadTexts:rlSocket.setRevisions(('2007-01-02 00:00',))
_RlSocketMibVersion_Type=Integer32
_RlSocketMibVersion_Object=MibScalar
rlSocketMibVersion=_RlSocketMibVersion_Object((1,3,6,1,4,1,89,85,1),_RlSocketMibVersion_Type())
rlSocketMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSocketMibVersion.setStatus(_A)
_RlSocketTable_Object=MibTable
rlSocketTable=_RlSocketTable_Object((1,3,6,1,4,1,89,85,2))
if mibBuilder.loadTexts:rlSocketTable.setStatus(_A)
_RlSocketEntry_Object=MibTableRow
rlSocketEntry=_RlSocketEntry_Object((1,3,6,1,4,1,89,85,2,1))
rlSocketEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rlSocketEntry.setStatus(_A)
_RlSocketId_Type=Integer32
_RlSocketId_Object=MibTableColumn
rlSocketId=_RlSocketId_Object((1,3,6,1,4,1,89,85,2,1,1),_RlSocketId_Type())
rlSocketId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSocketId.setStatus(_A)
class _RlSocketType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stream',1),('dgram',2),('raw',3)))
_RlSocketType_Type.__name__=_C
_RlSocketType_Object=MibTableColumn
rlSocketType=_RlSocketType_Object((1,3,6,1,4,1,89,85,2,1,2),_RlSocketType_Type())
rlSocketType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSocketType.setStatus(_A)
class _RlSocketState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('connected',1),('notConnected',2),('recvClosed',3),('sendClosed',4),('closed',5),('peerClosed',6),('sendRecvClosed',7)))
_RlSocketState_Type.__name__=_C
_RlSocketState_Object=MibTableColumn
rlSocketState=_RlSocketState_Object((1,3,6,1,4,1,89,85,2,1,3),_RlSocketState_Type())
rlSocketState.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSocketState.setStatus(_A)
class _RlSocketBlockMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('blocking',1),('nonBlocking',2)))
_RlSocketBlockMode_Type.__name__=_C
_RlSocketBlockMode_Object=MibTableColumn
rlSocketBlockMode=_RlSocketBlockMode_Object((1,3,6,1,4,1,89,85,2,1,4),_RlSocketBlockMode_Type())
rlSocketBlockMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSocketBlockMode.setStatus(_A)
_RlSocketUpTime_Type=TimeTicks
_RlSocketUpTime_Object=MibTableColumn
rlSocketUpTime=_RlSocketUpTime_Object((1,3,6,1,4,1,89,85,2,1,5),_RlSocketUpTime_Type())
rlSocketUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlSocketUpTime.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'rlSocket':rlSocket,'rlSocketMibVersion':rlSocketMibVersion,'rlSocketTable':rlSocketTable,'rlSocketEntry':rlSocketEntry,_E:rlSocketId,'rlSocketType':rlSocketType,'rlSocketState':rlSocketState,'rlSocketBlockMode':rlSocketBlockMode,'rlSocketUpTime':rlSocketUpTime})