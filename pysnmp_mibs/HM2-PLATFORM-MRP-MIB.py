_F='hm2AgentDot1qMrpPort'
_E='HM2-PLATFORM-MRP-MIB'
_D='Integer32'
_C='read-write'
_B='TimeInterval'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hm2PlatformMibs,=mibBuilder.importSymbols('HM2-TC-MIB','hm2PlatformMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeInterval=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_B)
hm2PlatformMRP=ModuleIdentity((1,3,6,1,4,1,248,12,60))
if mibBuilder.loadTexts:hm2PlatformMRP.setRevisions(('2013-04-10 00:00',))
_Hm2AgentDot1qMrp_ObjectIdentity=ObjectIdentity
hm2AgentDot1qMrp=_Hm2AgentDot1qMrp_ObjectIdentity((1,3,6,1,4,1,248,12,60,1))
_Hm2AgentDot1qPortMrpTable_Object=MibTable
hm2AgentDot1qPortMrpTable=_Hm2AgentDot1qPortMrpTable_Object((1,3,6,1,4,1,248,12,60,1,1))
if mibBuilder.loadTexts:hm2AgentDot1qPortMrpTable.setStatus(_A)
_Hm2AgentDot1qPortMrpEntry_Object=MibTableRow
hm2AgentDot1qPortMrpEntry=_Hm2AgentDot1qPortMrpEntry_Object((1,3,6,1,4,1,248,12,60,1,1,1))
hm2AgentDot1qPortMrpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hm2AgentDot1qPortMrpEntry.setStatus(_A)
class _Hm2AgentDot1qMrpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Hm2AgentDot1qMrpPort_Type.__name__=_D
_Hm2AgentDot1qMrpPort_Object=MibTableColumn
hm2AgentDot1qMrpPort=_Hm2AgentDot1qMrpPort_Object((1,3,6,1,4,1,248,12,60,1,1,1,1),_Hm2AgentDot1qMrpPort_Type())
hm2AgentDot1qMrpPort.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hm2AgentDot1qMrpPort.setStatus(_A)
class _Hm2AgentDot1qPortMrpJoinTime_Type(TimeInterval):defaultValue=20;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100))
_Hm2AgentDot1qPortMrpJoinTime_Type.__name__=_B
_Hm2AgentDot1qPortMrpJoinTime_Object=MibTableColumn
hm2AgentDot1qPortMrpJoinTime=_Hm2AgentDot1qPortMrpJoinTime_Object((1,3,6,1,4,1,248,12,60,1,1,1,2),_Hm2AgentDot1qPortMrpJoinTime_Type())
hm2AgentDot1qPortMrpJoinTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentDot1qPortMrpJoinTime.setStatus(_A)
class _Hm2AgentDot1qPortMrpLeaveTime_Type(TimeInterval):defaultValue=60;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,600))
_Hm2AgentDot1qPortMrpLeaveTime_Type.__name__=_B
_Hm2AgentDot1qPortMrpLeaveTime_Object=MibTableColumn
hm2AgentDot1qPortMrpLeaveTime=_Hm2AgentDot1qPortMrpLeaveTime_Object((1,3,6,1,4,1,248,12,60,1,1,1,3),_Hm2AgentDot1qPortMrpLeaveTime_Type())
hm2AgentDot1qPortMrpLeaveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentDot1qPortMrpLeaveTime.setStatus(_A)
class _Hm2AgentDot1qPortMrpLeaveAllTime_Type(TimeInterval):defaultValue=1000;subtypeSpec=TimeInterval.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,6000))
_Hm2AgentDot1qPortMrpLeaveAllTime_Type.__name__=_B
_Hm2AgentDot1qPortMrpLeaveAllTime_Object=MibTableColumn
hm2AgentDot1qPortMrpLeaveAllTime=_Hm2AgentDot1qPortMrpLeaveAllTime_Object((1,3,6,1,4,1,248,12,60,1,1,1,4),_Hm2AgentDot1qPortMrpLeaveAllTime_Type())
hm2AgentDot1qPortMrpLeaveAllTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2AgentDot1qPortMrpLeaveAllTime.setStatus(_A)
_Hm2AgentDot1qMrpMxrp_ObjectIdentity=ObjectIdentity
hm2AgentDot1qMrpMxrp=_Hm2AgentDot1qMrpMxrp_ObjectIdentity((1,3,6,1,4,1,248,12,60,2))
mibBuilder.exportSymbols(_E,**{'hm2PlatformMRP':hm2PlatformMRP,'hm2AgentDot1qMrp':hm2AgentDot1qMrp,'hm2AgentDot1qPortMrpTable':hm2AgentDot1qPortMrpTable,'hm2AgentDot1qPortMrpEntry':hm2AgentDot1qPortMrpEntry,_F:hm2AgentDot1qMrpPort,'hm2AgentDot1qPortMrpJoinTime':hm2AgentDot1qPortMrpJoinTime,'hm2AgentDot1qPortMrpLeaveTime':hm2AgentDot1qPortMrpLeaveTime,'hm2AgentDot1qPortMrpLeaveAllTime':hm2AgentDot1qPortMrpLeaveAllTime,'hm2AgentDot1qMrpMxrp':hm2AgentDot1qMrpMxrp})