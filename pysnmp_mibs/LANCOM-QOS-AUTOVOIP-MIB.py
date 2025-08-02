_M='agentAutoVoIPSessionIndex'
_L='agentAutoVoIPOUIIndex'
_K='disable'
_J='enable'
_I='agentAutoVoIPIntfIndex'
_H='2007-11-23 00:00'
_G='Unsigned32'
_F='OctetString'
_E='LANCOM-QOS-AUTOVOIP-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
fastPathQOS,=mibBuilder.importSymbols('LANCOM-QOS-MIB','fastPathQOS')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fastPathQOSAUTOVOIP=ModuleIdentity((1,3,6,1,4,1,2356,16,1,3,4))
if mibBuilder.loadTexts:fastPathQOSAUTOVOIP.setRevisions(('2017-12-15 00:00','2012-02-18 00:00','2011-01-26 00:00',_H,_H))
_AgentAutoVoIPCfgGroup_ObjectIdentity=ObjectIdentity
agentAutoVoIPCfgGroup=_AgentAutoVoIPCfgGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,3,4,1))
_AgentAutoVoIPVLAN_Type=Integer32
_AgentAutoVoIPVLAN_Object=MibScalar
agentAutoVoIPVLAN=_AgentAutoVoIPVLAN_Object((1,3,6,1,4,1,2356,16,1,3,4,1,1),_AgentAutoVoIPVLAN_Type())
agentAutoVoIPVLAN.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAutoVoIPVLAN.setStatus(_A)
_AgentAutoVoIPOUIPriority_Type=Integer32
_AgentAutoVoIPOUIPriority_Object=MibScalar
agentAutoVoIPOUIPriority=_AgentAutoVoIPOUIPriority_Object((1,3,6,1,4,1,2356,16,1,3,4,1,2),_AgentAutoVoIPOUIPriority_Type())
agentAutoVoIPOUIPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAutoVoIPOUIPriority.setStatus(_A)
class _AgentAutoVoIPProtocolPriScheme_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trafficClass',1),('remark',2)))
_AgentAutoVoIPProtocolPriScheme_Type.__name__=_C
_AgentAutoVoIPProtocolPriScheme_Object=MibScalar
agentAutoVoIPProtocolPriScheme=_AgentAutoVoIPProtocolPriScheme_Object((1,3,6,1,4,1,2356,16,1,3,4,1,3),_AgentAutoVoIPProtocolPriScheme_Type())
agentAutoVoIPProtocolPriScheme.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAutoVoIPProtocolPriScheme.setStatus(_A)
class _AgentAutoVoIPProtocolTcOrRemarkValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AgentAutoVoIPProtocolTcOrRemarkValue_Type.__name__=_G
_AgentAutoVoIPProtocolTcOrRemarkValue_Object=MibScalar
agentAutoVoIPProtocolTcOrRemarkValue=_AgentAutoVoIPProtocolTcOrRemarkValue_Object((1,3,6,1,4,1,2356,16,1,3,4,1,4),_AgentAutoVoIPProtocolTcOrRemarkValue_Type())
agentAutoVoIPProtocolTcOrRemarkValue.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAutoVoIPProtocolTcOrRemarkValue.setStatus(_A)
_AgentAutoVoIPTable_Object=MibTable
agentAutoVoIPTable=_AgentAutoVoIPTable_Object((1,3,6,1,4,1,2356,16,1,3,4,1,5))
if mibBuilder.loadTexts:agentAutoVoIPTable.setStatus(_A)
_AgentAutoVoIPEntry_Object=MibTableRow
agentAutoVoIPEntry=_AgentAutoVoIPEntry_Object((1,3,6,1,4,1,2356,16,1,3,4,1,5,1))
agentAutoVoIPEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:agentAutoVoIPEntry.setStatus(_A)
_AgentAutoVoIPIntfIndex_Type=InterfaceIndex
_AgentAutoVoIPIntfIndex_Object=MibTableColumn
agentAutoVoIPIntfIndex=_AgentAutoVoIPIntfIndex_Object((1,3,6,1,4,1,2356,16,1,3,4,1,5,1,1),_AgentAutoVoIPIntfIndex_Type())
agentAutoVoIPIntfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:agentAutoVoIPIntfIndex.setStatus(_A)
class _AgentAutoVoIPProtocolMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AgentAutoVoIPProtocolMode_Type.__name__=_C
_AgentAutoVoIPProtocolMode_Object=MibTableColumn
agentAutoVoIPProtocolMode=_AgentAutoVoIPProtocolMode_Object((1,3,6,1,4,1,2356,16,1,3,4,1,5,1,2),_AgentAutoVoIPProtocolMode_Type())
agentAutoVoIPProtocolMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAutoVoIPProtocolMode.setStatus(_A)
class _AgentAutoVoIPOUIMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_AgentAutoVoIPOUIMode_Type.__name__=_C
_AgentAutoVoIPOUIMode_Object=MibTableColumn
agentAutoVoIPOUIMode=_AgentAutoVoIPOUIMode_Object((1,3,6,1,4,1,2356,16,1,3,4,1,5,1,3),_AgentAutoVoIPOUIMode_Type())
agentAutoVoIPOUIMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAutoVoIPOUIMode.setStatus(_A)
class _AgentAutoVoIPProtocolPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_AgentAutoVoIPProtocolPortStatus_Type.__name__=_C
_AgentAutoVoIPProtocolPortStatus_Object=MibTableColumn
agentAutoVoIPProtocolPortStatus=_AgentAutoVoIPProtocolPortStatus_Object((1,3,6,1,4,1,2356,16,1,3,4,1,5,1,4),_AgentAutoVoIPProtocolPortStatus_Type())
agentAutoVoIPProtocolPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAutoVoIPProtocolPortStatus.setStatus(_A)
class _AgentAutoVoIPOUIPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_AgentAutoVoIPOUIPortStatus_Type.__name__=_C
_AgentAutoVoIPOUIPortStatus_Object=MibTableColumn
agentAutoVoIPOUIPortStatus=_AgentAutoVoIPOUIPortStatus_Object((1,3,6,1,4,1,2356,16,1,3,4,1,5,1,5),_AgentAutoVoIPOUIPortStatus_Type())
agentAutoVoIPOUIPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAutoVoIPOUIPortStatus.setStatus(_A)
_AgentAutoVoIPOUITable_Object=MibTable
agentAutoVoIPOUITable=_AgentAutoVoIPOUITable_Object((1,3,6,1,4,1,2356,16,1,3,4,1,6))
if mibBuilder.loadTexts:agentAutoVoIPOUITable.setStatus(_A)
_AgentAutoVoIPOUIEntry_Object=MibTableRow
agentAutoVoIPOUIEntry=_AgentAutoVoIPOUIEntry_Object((1,3,6,1,4,1,2356,16,1,3,4,1,6,1))
agentAutoVoIPOUIEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:agentAutoVoIPOUIEntry.setStatus(_A)
class _AgentAutoVoIPOUIIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_AgentAutoVoIPOUIIndex_Type.__name__=_C
_AgentAutoVoIPOUIIndex_Object=MibTableColumn
agentAutoVoIPOUIIndex=_AgentAutoVoIPOUIIndex_Object((1,3,6,1,4,1,2356,16,1,3,4,1,6,1,1),_AgentAutoVoIPOUIIndex_Type())
agentAutoVoIPOUIIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAutoVoIPOUIIndex.setStatus(_A)
class _AgentAutoVoIPOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_AgentAutoVoIPOUI_Type.__name__=_F
_AgentAutoVoIPOUI_Object=MibTableColumn
agentAutoVoIPOUI=_AgentAutoVoIPOUI_Object((1,3,6,1,4,1,2356,16,1,3,4,1,6,1,2),_AgentAutoVoIPOUI_Type())
agentAutoVoIPOUI.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAutoVoIPOUI.setStatus(_A)
class _AgentAutoVoIPOUIDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AgentAutoVoIPOUIDesc_Type.__name__=_F
_AgentAutoVoIPOUIDesc_Object=MibTableColumn
agentAutoVoIPOUIDesc=_AgentAutoVoIPOUIDesc_Object((1,3,6,1,4,1,2356,16,1,3,4,1,6,1,3),_AgentAutoVoIPOUIDesc_Type())
agentAutoVoIPOUIDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:agentAutoVoIPOUIDesc.setStatus(_A)
_AgentAutoVoIPOUIRowStatus_Type=RowStatus
_AgentAutoVoIPOUIRowStatus_Object=MibTableColumn
agentAutoVoIPOUIRowStatus=_AgentAutoVoIPOUIRowStatus_Object((1,3,6,1,4,1,2356,16,1,3,4,1,6,1,4),_AgentAutoVoIPOUIRowStatus_Type())
agentAutoVoIPOUIRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:agentAutoVoIPOUIRowStatus.setStatus(_A)
_AgentAutoVoIPSessionTable_Object=MibTable
agentAutoVoIPSessionTable=_AgentAutoVoIPSessionTable_Object((1,3,6,1,4,1,2356,16,1,3,4,1,7))
if mibBuilder.loadTexts:agentAutoVoIPSessionTable.setStatus(_A)
_AgentAutoVoIPSessionEntry_Object=MibTableRow
agentAutoVoIPSessionEntry=_AgentAutoVoIPSessionEntry_Object((1,3,6,1,4,1,2356,16,1,3,4,1,7,1))
agentAutoVoIPSessionEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:agentAutoVoIPSessionEntry.setStatus(_A)
class _AgentAutoVoIPSessionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_AgentAutoVoIPSessionIndex_Type.__name__=_C
_AgentAutoVoIPSessionIndex_Object=MibTableColumn
agentAutoVoIPSessionIndex=_AgentAutoVoIPSessionIndex_Object((1,3,6,1,4,1,2356,16,1,3,4,1,7,1,1),_AgentAutoVoIPSessionIndex_Type())
agentAutoVoIPSessionIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAutoVoIPSessionIndex.setStatus(_A)
_AgentAutoVoIPSourceIP_Type=IpAddress
_AgentAutoVoIPSourceIP_Object=MibTableColumn
agentAutoVoIPSourceIP=_AgentAutoVoIPSourceIP_Object((1,3,6,1,4,1,2356,16,1,3,4,1,7,1,2),_AgentAutoVoIPSourceIP_Type())
agentAutoVoIPSourceIP.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAutoVoIPSourceIP.setStatus(_A)
_AgentAutoVoIPDestinationIP_Type=IpAddress
_AgentAutoVoIPDestinationIP_Object=MibTableColumn
agentAutoVoIPDestinationIP=_AgentAutoVoIPDestinationIP_Object((1,3,6,1,4,1,2356,16,1,3,4,1,7,1,3),_AgentAutoVoIPDestinationIP_Type())
agentAutoVoIPDestinationIP.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAutoVoIPDestinationIP.setStatus(_A)
_AgentAutoVoIPSourceL4Port_Type=Integer32
_AgentAutoVoIPSourceL4Port_Object=MibTableColumn
agentAutoVoIPSourceL4Port=_AgentAutoVoIPSourceL4Port_Object((1,3,6,1,4,1,2356,16,1,3,4,1,7,1,4),_AgentAutoVoIPSourceL4Port_Type())
agentAutoVoIPSourceL4Port.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAutoVoIPSourceL4Port.setStatus(_A)
_AgentAutoVoIPDestinationL4Port_Type=Integer32
_AgentAutoVoIPDestinationL4Port_Object=MibTableColumn
agentAutoVoIPDestinationL4Port=_AgentAutoVoIPDestinationL4Port_Object((1,3,6,1,4,1,2356,16,1,3,4,1,7,1,5),_AgentAutoVoIPDestinationL4Port_Type())
agentAutoVoIPDestinationL4Port.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAutoVoIPDestinationL4Port.setStatus(_A)
_AgentAutoVoIPProtocol_Type=Integer32
_AgentAutoVoIPProtocol_Object=MibTableColumn
agentAutoVoIPProtocol=_AgentAutoVoIPProtocol_Object((1,3,6,1,4,1,2356,16,1,3,4,1,7,1,6),_AgentAutoVoIPProtocol_Type())
agentAutoVoIPProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:agentAutoVoIPProtocol.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fastPathQOSAUTOVOIP':fastPathQOSAUTOVOIP,'agentAutoVoIPCfgGroup':agentAutoVoIPCfgGroup,'agentAutoVoIPVLAN':agentAutoVoIPVLAN,'agentAutoVoIPOUIPriority':agentAutoVoIPOUIPriority,'agentAutoVoIPProtocolPriScheme':agentAutoVoIPProtocolPriScheme,'agentAutoVoIPProtocolTcOrRemarkValue':agentAutoVoIPProtocolTcOrRemarkValue,'agentAutoVoIPTable':agentAutoVoIPTable,'agentAutoVoIPEntry':agentAutoVoIPEntry,_I:agentAutoVoIPIntfIndex,'agentAutoVoIPProtocolMode':agentAutoVoIPProtocolMode,'agentAutoVoIPOUIMode':agentAutoVoIPOUIMode,'agentAutoVoIPProtocolPortStatus':agentAutoVoIPProtocolPortStatus,'agentAutoVoIPOUIPortStatus':agentAutoVoIPOUIPortStatus,'agentAutoVoIPOUITable':agentAutoVoIPOUITable,'agentAutoVoIPOUIEntry':agentAutoVoIPOUIEntry,_L:agentAutoVoIPOUIIndex,'agentAutoVoIPOUI':agentAutoVoIPOUI,'agentAutoVoIPOUIDesc':agentAutoVoIPOUIDesc,'agentAutoVoIPOUIRowStatus':agentAutoVoIPOUIRowStatus,'agentAutoVoIPSessionTable':agentAutoVoIPSessionTable,'agentAutoVoIPSessionEntry':agentAutoVoIPSessionEntry,_M:agentAutoVoIPSessionIndex,'agentAutoVoIPSourceIP':agentAutoVoIPSourceIP,'agentAutoVoIPDestinationIP':agentAutoVoIPDestinationIP,'agentAutoVoIPSourceL4Port':agentAutoVoIPSourceL4Port,'agentAutoVoIPDestinationL4Port':agentAutoVoIPDestinationL4Port,'agentAutoVoIPProtocol':agentAutoVoIPProtocol})