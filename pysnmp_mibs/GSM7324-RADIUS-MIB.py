_M='agentRadiusServerIndex'
_L='not-accessible'
_K='agentRadiusAccountingServerIndex'
_J='GSM7324-RADIUS-MIB'
_I='read-only'
_H='DisplayString'
_G='read-create'
_F='disable'
_E='enable'
_D='Unsigned32'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
gsm7324,=mibBuilder.importSymbols('GSM7324-REF-MIB','gsm7324')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention')
gsm7324Radius=ModuleIdentity((1,3,6,1,4,1,4526,1,7,8))
if mibBuilder.loadTexts:gsm7324Radius.setRevisions(('2003-05-07 00:00',))
_AgentRadiusConfigGroup_ObjectIdentity=ObjectIdentity
agentRadiusConfigGroup=_AgentRadiusConfigGroup_ObjectIdentity((1,3,6,1,4,1,4526,1,7,8,1))
class _AgentRadiusMaxTransmit_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_AgentRadiusMaxTransmit_Type.__name__=_D
_AgentRadiusMaxTransmit_Object=MibScalar
agentRadiusMaxTransmit=_AgentRadiusMaxTransmit_Object((1,3,6,1,4,1,4526,1,7,8,1,1),_AgentRadiusMaxTransmit_Type())
agentRadiusMaxTransmit.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRadiusMaxTransmit.setStatus(_A)
class _AgentRadiusTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_AgentRadiusTimeout_Type.__name__=_D
_AgentRadiusTimeout_Object=MibScalar
agentRadiusTimeout=_AgentRadiusTimeout_Object((1,3,6,1,4,1,4526,1,7,8,1,2),_AgentRadiusTimeout_Type())
agentRadiusTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRadiusTimeout.setStatus(_A)
class _AgentRadiusAccountingMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentRadiusAccountingMode_Type.__name__=_B
_AgentRadiusAccountingMode_Object=MibScalar
agentRadiusAccountingMode=_AgentRadiusAccountingMode_Object((1,3,6,1,4,1,4526,1,7,8,1,3),_AgentRadiusAccountingMode_Type())
agentRadiusAccountingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRadiusAccountingMode.setStatus(_A)
class _AgentRadiusStatsClear_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentRadiusStatsClear_Type.__name__=_B
_AgentRadiusStatsClear_Object=MibScalar
agentRadiusStatsClear=_AgentRadiusStatsClear_Object((1,3,6,1,4,1,4526,1,7,8,1,4),_AgentRadiusStatsClear_Type())
agentRadiusStatsClear.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRadiusStatsClear.setStatus(_A)
class _AgentRadiusAccountingIndexNextValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentRadiusAccountingIndexNextValid_Type.__name__=_B
_AgentRadiusAccountingIndexNextValid_Object=MibScalar
agentRadiusAccountingIndexNextValid=_AgentRadiusAccountingIndexNextValid_Object((1,3,6,1,4,1,4526,1,7,8,1,5),_AgentRadiusAccountingIndexNextValid_Type())
agentRadiusAccountingIndexNextValid.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRadiusAccountingIndexNextValid.setStatus(_A)
_AgentRadiusAccountingConfigTable_Object=MibTable
agentRadiusAccountingConfigTable=_AgentRadiusAccountingConfigTable_Object((1,3,6,1,4,1,4526,1,7,8,1,6))
if mibBuilder.loadTexts:agentRadiusAccountingConfigTable.setStatus(_A)
_AgentRadiusAccountingConfigEntry_Object=MibTableRow
agentRadiusAccountingConfigEntry=_AgentRadiusAccountingConfigEntry_Object((1,3,6,1,4,1,4526,1,7,8,1,6,1))
agentRadiusAccountingConfigEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:agentRadiusAccountingConfigEntry.setStatus(_A)
class _AgentRadiusAccountingServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AgentRadiusAccountingServerIndex_Type.__name__=_B
_AgentRadiusAccountingServerIndex_Object=MibTableColumn
agentRadiusAccountingServerIndex=_AgentRadiusAccountingServerIndex_Object((1,3,6,1,4,1,4526,1,7,8,1,6,1,1),_AgentRadiusAccountingServerIndex_Type())
agentRadiusAccountingServerIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:agentRadiusAccountingServerIndex.setStatus(_A)
_AgentRadiusAccountingServerAddress_Type=IpAddress
_AgentRadiusAccountingServerAddress_Object=MibTableColumn
agentRadiusAccountingServerAddress=_AgentRadiusAccountingServerAddress_Object((1,3,6,1,4,1,4526,1,7,8,1,6,1,2),_AgentRadiusAccountingServerAddress_Type())
agentRadiusAccountingServerAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:agentRadiusAccountingServerAddress.setStatus(_A)
class _AgentRadiusAccountingPort_Type(Unsigned32):defaultValue=1813;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentRadiusAccountingPort_Type.__name__=_D
_AgentRadiusAccountingPort_Object=MibTableColumn
agentRadiusAccountingPort=_AgentRadiusAccountingPort_Object((1,3,6,1,4,1,4526,1,7,8,1,6,1,3),_AgentRadiusAccountingPort_Type())
agentRadiusAccountingPort.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRadiusAccountingPort.setStatus(_A)
class _AgentRadiusAccountingSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_AgentRadiusAccountingSecret_Type.__name__=_H
_AgentRadiusAccountingSecret_Object=MibTableColumn
agentRadiusAccountingSecret=_AgentRadiusAccountingSecret_Object((1,3,6,1,4,1,4526,1,7,8,1,6,1,4),_AgentRadiusAccountingSecret_Type())
agentRadiusAccountingSecret.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRadiusAccountingSecret.setStatus(_A)
_AgentRadiusAccountingStatus_Type=RowStatus
_AgentRadiusAccountingStatus_Object=MibTableColumn
agentRadiusAccountingStatus=_AgentRadiusAccountingStatus_Object((1,3,6,1,4,1,4526,1,7,8,1,6,1,5),_AgentRadiusAccountingStatus_Type())
agentRadiusAccountingStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:agentRadiusAccountingStatus.setStatus(_A)
class _AgentRadiusServerIndexNextValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentRadiusServerIndexNextValid_Type.__name__=_B
_AgentRadiusServerIndexNextValid_Object=MibScalar
agentRadiusServerIndexNextValid=_AgentRadiusServerIndexNextValid_Object((1,3,6,1,4,1,4526,1,7,8,1,7),_AgentRadiusServerIndexNextValid_Type())
agentRadiusServerIndexNextValid.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRadiusServerIndexNextValid.setStatus(_A)
_AgentRadiusServerConfigTable_Object=MibTable
agentRadiusServerConfigTable=_AgentRadiusServerConfigTable_Object((1,3,6,1,4,1,4526,1,7,8,1,8))
if mibBuilder.loadTexts:agentRadiusServerConfigTable.setStatus(_A)
_AgentRadiusServerConfigEntry_Object=MibTableRow
agentRadiusServerConfigEntry=_AgentRadiusServerConfigEntry_Object((1,3,6,1,4,1,4526,1,7,8,1,8,1))
agentRadiusServerConfigEntry.setIndexNames((0,_J,_M))
if mibBuilder.loadTexts:agentRadiusServerConfigEntry.setStatus(_A)
class _AgentRadiusServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AgentRadiusServerIndex_Type.__name__=_B
_AgentRadiusServerIndex_Object=MibTableColumn
agentRadiusServerIndex=_AgentRadiusServerIndex_Object((1,3,6,1,4,1,4526,1,7,8,1,8,1,1),_AgentRadiusServerIndex_Type())
agentRadiusServerIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:agentRadiusServerIndex.setStatus(_A)
_AgentRadiusServerAddress_Type=IpAddress
_AgentRadiusServerAddress_Object=MibTableColumn
agentRadiusServerAddress=_AgentRadiusServerAddress_Object((1,3,6,1,4,1,4526,1,7,8,1,8,1,2),_AgentRadiusServerAddress_Type())
agentRadiusServerAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:agentRadiusServerAddress.setStatus(_A)
class _AgentRadiusServerPort_Type(Unsigned32):defaultValue=1812;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AgentRadiusServerPort_Type.__name__=_D
_AgentRadiusServerPort_Object=MibTableColumn
agentRadiusServerPort=_AgentRadiusServerPort_Object((1,3,6,1,4,1,4526,1,7,8,1,8,1,3),_AgentRadiusServerPort_Type())
agentRadiusServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRadiusServerPort.setStatus(_A)
class _AgentRadiusServerSecret_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_AgentRadiusServerSecret_Type.__name__=_H
_AgentRadiusServerSecret_Object=MibTableColumn
agentRadiusServerSecret=_AgentRadiusServerSecret_Object((1,3,6,1,4,1,4526,1,7,8,1,8,1,4),_AgentRadiusServerSecret_Type())
agentRadiusServerSecret.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRadiusServerSecret.setStatus(_A)
class _AgentRadiusServerPrimaryMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentRadiusServerPrimaryMode_Type.__name__=_B
_AgentRadiusServerPrimaryMode_Object=MibTableColumn
agentRadiusServerPrimaryMode=_AgentRadiusServerPrimaryMode_Object((1,3,6,1,4,1,4526,1,7,8,1,8,1,5),_AgentRadiusServerPrimaryMode_Type())
agentRadiusServerPrimaryMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRadiusServerPrimaryMode.setStatus(_A)
class _AgentRadiusServerCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_AgentRadiusServerCurrentMode_Type.__name__=_B
_AgentRadiusServerCurrentMode_Object=MibTableColumn
agentRadiusServerCurrentMode=_AgentRadiusServerCurrentMode_Object((1,3,6,1,4,1,4526,1,7,8,1,8,1,6),_AgentRadiusServerCurrentMode_Type())
agentRadiusServerCurrentMode.setMaxAccess(_I)
if mibBuilder.loadTexts:agentRadiusServerCurrentMode.setStatus(_A)
class _AgentRadiusServerMsgAuth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AgentRadiusServerMsgAuth_Type.__name__=_B
_AgentRadiusServerMsgAuth_Object=MibTableColumn
agentRadiusServerMsgAuth=_AgentRadiusServerMsgAuth_Object((1,3,6,1,4,1,4526,1,7,8,1,8,1,7),_AgentRadiusServerMsgAuth_Type())
agentRadiusServerMsgAuth.setMaxAccess(_C)
if mibBuilder.loadTexts:agentRadiusServerMsgAuth.setStatus(_A)
_AgentRadiusServerStatus_Type=RowStatus
_AgentRadiusServerStatus_Object=MibTableColumn
agentRadiusServerStatus=_AgentRadiusServerStatus_Object((1,3,6,1,4,1,4526,1,7,8,1,8,1,8),_AgentRadiusServerStatus_Type())
agentRadiusServerStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:agentRadiusServerStatus.setStatus(_A)
mibBuilder.exportSymbols(_J,**{'gsm7324Radius':gsm7324Radius,'agentRadiusConfigGroup':agentRadiusConfigGroup,'agentRadiusMaxTransmit':agentRadiusMaxTransmit,'agentRadiusTimeout':agentRadiusTimeout,'agentRadiusAccountingMode':agentRadiusAccountingMode,'agentRadiusStatsClear':agentRadiusStatsClear,'agentRadiusAccountingIndexNextValid':agentRadiusAccountingIndexNextValid,'agentRadiusAccountingConfigTable':agentRadiusAccountingConfigTable,'agentRadiusAccountingConfigEntry':agentRadiusAccountingConfigEntry,_K:agentRadiusAccountingServerIndex,'agentRadiusAccountingServerAddress':agentRadiusAccountingServerAddress,'agentRadiusAccountingPort':agentRadiusAccountingPort,'agentRadiusAccountingSecret':agentRadiusAccountingSecret,'agentRadiusAccountingStatus':agentRadiusAccountingStatus,'agentRadiusServerIndexNextValid':agentRadiusServerIndexNextValid,'agentRadiusServerConfigTable':agentRadiusServerConfigTable,'agentRadiusServerConfigEntry':agentRadiusServerConfigEntry,_M:agentRadiusServerIndex,'agentRadiusServerAddress':agentRadiusServerAddress,'agentRadiusServerPort':agentRadiusServerPort,'agentRadiusServerSecret':agentRadiusServerSecret,'agentRadiusServerPrimaryMode':agentRadiusServerPrimaryMode,'agentRadiusServerCurrentMode':agentRadiusServerCurrentMode,'agentRadiusServerMsgAuth':agentRadiusServerMsgAuth,'agentRadiusServerStatus':agentRadiusServerStatus})