_F='agentAutoVoIPIntfIndex'
_E='FASTPATH-QOS-AUTOVOIP-MIB'
_D='2007-11-23 00:00'
_C='Unsigned32'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPathQOS,=mibBuilder.importSymbols('FASTPATH-QOS-MIB','fastPathQOS')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fastPathQOSAUTOVOIP=ModuleIdentity((1,3,6,1,4,1,4413,1,1,3,4))
if mibBuilder.loadTexts:fastPathQOSAUTOVOIP.setRevisions((_D,_D))
class PercentByFives(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5,5),ValueRangeConstraint(10,10),ValueRangeConstraint(15,15),ValueRangeConstraint(20,20),ValueRangeConstraint(25,25),ValueRangeConstraint(30,30),ValueRangeConstraint(35,35),ValueRangeConstraint(40,40),ValueRangeConstraint(45,45),ValueRangeConstraint(50,50),ValueRangeConstraint(55,55),ValueRangeConstraint(60,60),ValueRangeConstraint(65,65),ValueRangeConstraint(70,70),ValueRangeConstraint(75,75),ValueRangeConstraint(80,80),ValueRangeConstraint(85,85),ValueRangeConstraint(90,90),ValueRangeConstraint(95,95),ValueRangeConstraint(100,100))
class Sixteenths(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_AgentAutoVoIPCfgGroup_ObjectIdentity=ObjectIdentity
agentAutoVoIPCfgGroup=_AgentAutoVoIPCfgGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,3,4,1))
_AgentAutoVoIPTable_Object=MibTable
agentAutoVoIPTable=_AgentAutoVoIPTable_Object((1,3,6,1,4,1,4413,1,1,3,4,1,1))
if mibBuilder.loadTexts:agentAutoVoIPTable.setStatus(_A)
_AgentAutoVoIPEntry_Object=MibTableRow
agentAutoVoIPEntry=_AgentAutoVoIPEntry_Object((1,3,6,1,4,1,4413,1,1,3,4,1,1,1))
agentAutoVoIPEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:agentAutoVoIPEntry.setStatus(_A)
_AgentAutoVoIPIntfIndex_Type=InterfaceIndexOrZero
_AgentAutoVoIPIntfIndex_Object=MibTableColumn
agentAutoVoIPIntfIndex=_AgentAutoVoIPIntfIndex_Object((1,3,6,1,4,1,4413,1,1,3,4,1,1,1,1),_AgentAutoVoIPIntfIndex_Type())
agentAutoVoIPIntfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:agentAutoVoIPIntfIndex.setStatus(_A)
class _AgentAutoVoIPMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AgentAutoVoIPMode_Type.__name__=_B
_AgentAutoVoIPMode_Object=MibTableColumn
agentAutoVoIPMode=_AgentAutoVoIPMode_Object((1,3,6,1,4,1,4413,1,1,3,4,1,1,1,2),_AgentAutoVoIPMode_Type())
agentAutoVoIPMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:agentAutoVoIPMode.setStatus(_A)
class _AgentAutoVoIPCosQueue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AgentAutoVoIPCosQueue_Type.__name__=_C
_AgentAutoVoIPCosQueue_Object=MibTableColumn
agentAutoVoIPCosQueue=_AgentAutoVoIPCosQueue_Object((1,3,6,1,4,1,4413,1,1,3,4,1,1,1,3),_AgentAutoVoIPCosQueue_Type())
agentAutoVoIPCosQueue.setMaxAccess('read-only')
if mibBuilder.loadTexts:agentAutoVoIPCosQueue.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'PercentByFives':PercentByFives,'Sixteenths':Sixteenths,'fastPathQOSAUTOVOIP':fastPathQOSAUTOVOIP,'agentAutoVoIPCfgGroup':agentAutoVoIPCfgGroup,'agentAutoVoIPTable':agentAutoVoIPTable,'agentAutoVoIPEntry':agentAutoVoIPEntry,_F:agentAutoVoIPIntfIndex,'agentAutoVoIPMode':agentAutoVoIPMode,'agentAutoVoIPCosQueue':agentAutoVoIPCosQueue})