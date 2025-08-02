_G='agentSwitchLlpfProtocolType'
_F='DNOS-LLPF-PRIVATE-MIB'
_E='Unsigned32'
_D='Integer32'
_C='ifIndex'
_B='IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dnOS,=mibBuilder.importSymbols('DELL-REF-MIB','dnOS')
ifIndex,=mibBuilder.importSymbols(_B,_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
fastPathLlpf=ModuleIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,48))
if mibBuilder.loadTexts:fastPathLlpf.setRevisions(('2011-01-26 00:00','2009-10-26 00:00'))
_AgentSwitchLlpfGroup_ObjectIdentity=ObjectIdentity
agentSwitchLlpfGroup=_AgentSwitchLlpfGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,48,1))
_AgentSwitchLlpfPortConfigTable_Object=MibTable
agentSwitchLlpfPortConfigTable=_AgentSwitchLlpfPortConfigTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,48,1,1))
if mibBuilder.loadTexts:agentSwitchLlpfPortConfigTable.setStatus(_A)
_AgentSwitchLlpfPortConfigEntry_Object=MibTableRow
agentSwitchLlpfPortConfigEntry=_AgentSwitchLlpfPortConfigEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,48,1,1,1))
agentSwitchLlpfPortConfigEntry.setIndexNames((0,_B,_C),(0,_F,_G))
if mibBuilder.loadTexts:agentSwitchLlpfPortConfigEntry.setStatus(_A)
class _AgentSwitchLlpfProtocolType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_AgentSwitchLlpfProtocolType_Type.__name__=_E
_AgentSwitchLlpfProtocolType_Object=MibTableColumn
agentSwitchLlpfProtocolType=_AgentSwitchLlpfProtocolType_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,48,1,1,1,1),_AgentSwitchLlpfProtocolType_Type())
agentSwitchLlpfProtocolType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:agentSwitchLlpfProtocolType.setStatus(_A)
class _AgentSwitchLlpfPortBlockMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AgentSwitchLlpfPortBlockMode_Type.__name__=_D
_AgentSwitchLlpfPortBlockMode_Object=MibTableColumn
agentSwitchLlpfPortBlockMode=_AgentSwitchLlpfPortBlockMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,48,1,1,1,2),_AgentSwitchLlpfPortBlockMode_Type())
agentSwitchLlpfPortBlockMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:agentSwitchLlpfPortBlockMode.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'fastPathLlpf':fastPathLlpf,'agentSwitchLlpfGroup':agentSwitchLlpfGroup,'agentSwitchLlpfPortConfigTable':agentSwitchLlpfPortConfigTable,'agentSwitchLlpfPortConfigEntry':agentSwitchLlpfPortConfigEntry,_G:agentSwitchLlpfProtocolType,'agentSwitchLlpfPortBlockMode':agentSwitchLlpfPortBlockMode})