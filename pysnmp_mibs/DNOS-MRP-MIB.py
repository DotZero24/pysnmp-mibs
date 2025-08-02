_F='agentDot1qMrpPort'
_E='DNOS-MRP-MIB'
_D='Unsigned32'
_C='read-write'
_B='TimeInterval'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dnOS,=mibBuilder.importSymbols('DELL-REF-MIB','dnOS')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_B,'TruthValue')
fastPathMRP=ModuleIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,60))
if mibBuilder.loadTexts:fastPathMRP.setRevisions(('2011-04-29 00:00','2011-01-26 00:00','2010-10-31 00:00'))
_AgentDot1qMrp_ObjectIdentity=ObjectIdentity
agentDot1qMrp=_AgentDot1qMrp_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,60,1))
_AgentDot1qPortMrpTable_Object=MibTable
agentDot1qPortMrpTable=_AgentDot1qPortMrpTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,60,1,1))
if mibBuilder.loadTexts:agentDot1qPortMrpTable.setStatus(_A)
_AgentDot1qPortMrpEntry_Object=MibTableRow
agentDot1qPortMrpEntry=_AgentDot1qPortMrpEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,60,1,1,1))
agentDot1qPortMrpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:agentDot1qPortMrpEntry.setStatus(_A)
class _AgentDot1qMrpPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentDot1qMrpPort_Type.__name__=_D
_AgentDot1qMrpPort_Object=MibTableColumn
agentDot1qMrpPort=_AgentDot1qMrpPort_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,60,1,1,1,1),_AgentDot1qMrpPort_Type())
agentDot1qMrpPort.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:agentDot1qMrpPort.setStatus(_A)
class _AgentDot1qPortMrpJoinTime_Type(TimeInterval):defaultValue=20
_AgentDot1qPortMrpJoinTime_Type.__name__=_B
_AgentDot1qPortMrpJoinTime_Object=MibTableColumn
agentDot1qPortMrpJoinTime=_AgentDot1qPortMrpJoinTime_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,60,1,1,1,2),_AgentDot1qPortMrpJoinTime_Type())
agentDot1qPortMrpJoinTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1qPortMrpJoinTime.setStatus(_A)
class _AgentDot1qPortMrpLeaveTime_Type(TimeInterval):defaultValue=60
_AgentDot1qPortMrpLeaveTime_Type.__name__=_B
_AgentDot1qPortMrpLeaveTime_Object=MibTableColumn
agentDot1qPortMrpLeaveTime=_AgentDot1qPortMrpLeaveTime_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,60,1,1,1,3),_AgentDot1qPortMrpLeaveTime_Type())
agentDot1qPortMrpLeaveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1qPortMrpLeaveTime.setStatus(_A)
class _AgentDot1qPortMrpLeaveAllTime_Type(TimeInterval):defaultValue=1000
_AgentDot1qPortMrpLeaveAllTime_Type.__name__=_B
_AgentDot1qPortMrpLeaveAllTime_Object=MibTableColumn
agentDot1qPortMrpLeaveAllTime=_AgentDot1qPortMrpLeaveAllTime_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,60,1,1,1,4),_AgentDot1qPortMrpLeaveAllTime_Type())
agentDot1qPortMrpLeaveAllTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDot1qPortMrpLeaveAllTime.setStatus(_A)
_AgentDot1qMrpMxrp_ObjectIdentity=ObjectIdentity
agentDot1qMrpMxrp=_AgentDot1qMrpMxrp_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,60,2))
mibBuilder.exportSymbols(_E,**{'fastPathMRP':fastPathMRP,'agentDot1qMrp':agentDot1qMrp,'agentDot1qPortMrpTable':agentDot1qPortMrpTable,'agentDot1qPortMrpEntry':agentDot1qPortMrpEntry,_F:agentDot1qMrpPort,'agentDot1qPortMrpJoinTime':agentDot1qPortMrpJoinTime,'agentDot1qPortMrpLeaveTime':agentDot1qPortMrpLeaveTime,'agentDot1qPortMrpLeaveAllTime':agentDot1qPortMrpLeaveAllTime,'agentDot1qMrpMxrp':agentDot1qMrpMxrp})