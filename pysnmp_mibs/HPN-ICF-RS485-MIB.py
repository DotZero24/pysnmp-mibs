_J='InetAddressType'
_I='hpnicfRS485SessionIndex'
_H='HPN-ICF-RS485-MIB'
_G='read-create'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_E,_F)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfRS485=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,109))
_HpnicfRS485Properties_ObjectIdentity=ObjectIdentity
hpnicfRS485Properties=_HpnicfRS485Properties_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,109,1))
_HpnicfRS485PropertiesTable_Object=MibTable
hpnicfRS485PropertiesTable=_HpnicfRS485PropertiesTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,1,1))
if mibBuilder.loadTexts:hpnicfRS485PropertiesTable.setStatus(_A)
_HpnicfRS485PropertiesEntry_Object=MibTableRow
hpnicfRS485PropertiesEntry=_HpnicfRS485PropertiesEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,1,1,1))
hpnicfRS485PropertiesEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hpnicfRS485PropertiesEntry.setStatus(_A)
class _HpnicfRS485RawSessionNextIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfRS485RawSessionNextIndex_Type.__name__=_B
_HpnicfRS485RawSessionNextIndex_Object=MibTableColumn
hpnicfRS485RawSessionNextIndex=_HpnicfRS485RawSessionNextIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,1,1,1,1),_HpnicfRS485RawSessionNextIndex_Type())
hpnicfRS485RawSessionNextIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfRS485RawSessionNextIndex.setStatus(_A)
class _HpnicfRS485BaudRate_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('bautRate300',1),('bautRate600',2),('bautRate1200',3),('bautRate2400',4),('bautRate4800',5),('bautRate9600',6),('bautRate19200',7),('bautRate38400',8),('bautRate57600',9),('bautRate115200',10)))
_HpnicfRS485BaudRate_Type.__name__=_B
_HpnicfRS485BaudRate_Object=MibTableColumn
hpnicfRS485BaudRate=_HpnicfRS485BaudRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,1,1,1,2),_HpnicfRS485BaudRate_Type())
hpnicfRS485BaudRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRS485BaudRate.setStatus(_A)
class _HpnicfRS485DataBits_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('five',1),('six',2),('seven',3),('eight',4)))
_HpnicfRS485DataBits_Type.__name__=_B
_HpnicfRS485DataBits_Object=MibTableColumn
hpnicfRS485DataBits=_HpnicfRS485DataBits_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,1,1,1,3),_HpnicfRS485DataBits_Type())
hpnicfRS485DataBits.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRS485DataBits.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRS485DataBits.setUnits('bit')
class _HpnicfRS485Parity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('odd',2),('even',3),('mark',4),('space',5)))
_HpnicfRS485Parity_Type.__name__=_B
_HpnicfRS485Parity_Object=MibTableColumn
hpnicfRS485Parity=_HpnicfRS485Parity_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,1,1,1,4),_HpnicfRS485Parity_Type())
hpnicfRS485Parity.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRS485Parity.setStatus(_A)
class _HpnicfRS485StopBits_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('one',1),('two',2),('oneAndHalf',3)))
_HpnicfRS485StopBits_Type.__name__=_B
_HpnicfRS485StopBits_Object=MibTableColumn
hpnicfRS485StopBits=_HpnicfRS485StopBits_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,1,1,1,5),_HpnicfRS485StopBits_Type())
hpnicfRS485StopBits.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRS485StopBits.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRS485StopBits.setUnits('bit')
class _HpnicfRS485FlowControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('hardware',2),('xonOrxoff',3)))
_HpnicfRS485FlowControl_Type.__name__=_B
_HpnicfRS485FlowControl_Object=MibTableColumn
hpnicfRS485FlowControl=_HpnicfRS485FlowControl_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,1,1,1,6),_HpnicfRS485FlowControl_Type())
hpnicfRS485FlowControl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRS485FlowControl.setStatus(_A)
_HpnicfRS485TXCharacters_Type=Integer32
_HpnicfRS485TXCharacters_Object=MibTableColumn
hpnicfRS485TXCharacters=_HpnicfRS485TXCharacters_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,1,1,1,7),_HpnicfRS485TXCharacters_Type())
hpnicfRS485TXCharacters.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfRS485TXCharacters.setStatus(_A)
_HpnicfRS485RXCharacters_Type=Integer32
_HpnicfRS485RXCharacters_Object=MibTableColumn
hpnicfRS485RXCharacters=_HpnicfRS485RXCharacters_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,1,1,1,8),_HpnicfRS485RXCharacters_Type())
hpnicfRS485RXCharacters.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfRS485RXCharacters.setStatus(_A)
_HpnicfRS485TXErrCharacters_Type=Integer32
_HpnicfRS485TXErrCharacters_Object=MibTableColumn
hpnicfRS485TXErrCharacters=_HpnicfRS485TXErrCharacters_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,1,1,1,9),_HpnicfRS485TXErrCharacters_Type())
hpnicfRS485TXErrCharacters.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfRS485TXErrCharacters.setStatus(_A)
_HpnicfRS485RXErrCharacters_Type=Integer32
_HpnicfRS485RXErrCharacters_Object=MibTableColumn
hpnicfRS485RXErrCharacters=_HpnicfRS485RXErrCharacters_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,1,1,1,10),_HpnicfRS485RXErrCharacters_Type())
hpnicfRS485RXErrCharacters.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfRS485RXErrCharacters.setStatus(_A)
class _HpnicfRS485ResetCharacters_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('counting',1),('clear',2)))
_HpnicfRS485ResetCharacters_Type.__name__=_B
_HpnicfRS485ResetCharacters_Object=MibTableColumn
hpnicfRS485ResetCharacters=_HpnicfRS485ResetCharacters_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,1,1,1,11),_HpnicfRS485ResetCharacters_Type())
hpnicfRS485ResetCharacters.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRS485ResetCharacters.setStatus(_A)
_HpnicfRS485RawSessions_ObjectIdentity=ObjectIdentity
hpnicfRS485RawSessions=_HpnicfRS485RawSessions_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,109,2))
_HpnicfRS485RawSessionSummary_ObjectIdentity=ObjectIdentity
hpnicfRS485RawSessionSummary=_HpnicfRS485RawSessionSummary_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,109,2,1))
class _HpnicfRS485RawSessionMaxNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfRS485RawSessionMaxNum_Type.__name__=_B
_HpnicfRS485RawSessionMaxNum_Object=MibScalar
hpnicfRS485RawSessionMaxNum=_HpnicfRS485RawSessionMaxNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,2,1,1),_HpnicfRS485RawSessionMaxNum_Type())
hpnicfRS485RawSessionMaxNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfRS485RawSessionMaxNum.setStatus(_A)
_HpnicfRS485RawSessionTable_Object=MibTable
hpnicfRS485RawSessionTable=_HpnicfRS485RawSessionTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,2,2))
if mibBuilder.loadTexts:hpnicfRS485RawSessionTable.setStatus(_A)
_HpnicfRS485RawSessionEntry_Object=MibTableRow
hpnicfRS485RawSessionEntry=_HpnicfRS485RawSessionEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,2,2,1))
hpnicfRS485RawSessionEntry.setIndexNames((0,_E,_F),(0,_H,_I))
if mibBuilder.loadTexts:hpnicfRS485RawSessionEntry.setStatus(_A)
class _HpnicfRS485SessionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfRS485SessionIndex_Type.__name__=_B
_HpnicfRS485SessionIndex_Object=MibTableColumn
hpnicfRS485SessionIndex=_HpnicfRS485SessionIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,2,2,1,1),_HpnicfRS485SessionIndex_Type())
hpnicfRS485SessionIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfRS485SessionIndex.setStatus(_A)
class _HpnicfRS485SessionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('udp',1),('tcpClient',2),('tcpServer',3)))
_HpnicfRS485SessionType_Type.__name__=_B
_HpnicfRS485SessionType_Object=MibTableColumn
hpnicfRS485SessionType=_HpnicfRS485SessionType_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,2,2,1,2),_HpnicfRS485SessionType_Type())
hpnicfRS485SessionType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRS485SessionType.setStatus(_A)
class _HpnicfRS485SessionAddType_Type(InetAddressType):defaultValue=1
_HpnicfRS485SessionAddType_Type.__name__=_J
_HpnicfRS485SessionAddType_Object=MibTableColumn
hpnicfRS485SessionAddType=_HpnicfRS485SessionAddType_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,2,2,1,3),_HpnicfRS485SessionAddType_Type())
hpnicfRS485SessionAddType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRS485SessionAddType.setStatus(_A)
_HpnicfRS485SessionRemoteIP_Type=InetAddress
_HpnicfRS485SessionRemoteIP_Object=MibTableColumn
hpnicfRS485SessionRemoteIP=_HpnicfRS485SessionRemoteIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,2,2,1,4),_HpnicfRS485SessionRemoteIP_Type())
hpnicfRS485SessionRemoteIP.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfRS485SessionRemoteIP.setStatus(_A)
class _HpnicfRS485SessionRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_HpnicfRS485SessionRemotePort_Type.__name__=_B
_HpnicfRS485SessionRemotePort_Object=MibTableColumn
hpnicfRS485SessionRemotePort=_HpnicfRS485SessionRemotePort_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,2,2,1,5),_HpnicfRS485SessionRemotePort_Type())
hpnicfRS485SessionRemotePort.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfRS485SessionRemotePort.setStatus(_A)
class _HpnicfRS485SessionLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_HpnicfRS485SessionLocalPort_Type.__name__=_B
_HpnicfRS485SessionLocalPort_Object=MibTableColumn
hpnicfRS485SessionLocalPort=_HpnicfRS485SessionLocalPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,2,2,1,6),_HpnicfRS485SessionLocalPort_Type())
hpnicfRS485SessionLocalPort.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfRS485SessionLocalPort.setStatus(_A)
_HpnicfRS485SessionStatus_Type=RowStatus
_HpnicfRS485SessionStatus_Object=MibTableColumn
hpnicfRS485SessionStatus=_HpnicfRS485SessionStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,2,2,1,7),_HpnicfRS485SessionStatus_Type())
hpnicfRS485SessionStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfRS485SessionStatus.setStatus(_A)
_HpnicfRS485RawSessionErrInfoTable_Object=MibTable
hpnicfRS485RawSessionErrInfoTable=_HpnicfRS485RawSessionErrInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,2,3))
if mibBuilder.loadTexts:hpnicfRS485RawSessionErrInfoTable.setStatus(_A)
_HpnicfRS485RawSessionErrInfoEntry_Object=MibTableRow
hpnicfRS485RawSessionErrInfoEntry=_HpnicfRS485RawSessionErrInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,2,3,1))
hpnicfRS485RawSessionErrInfoEntry.setIndexNames((0,_E,_F),(0,_H,_I))
if mibBuilder.loadTexts:hpnicfRS485RawSessionErrInfoEntry.setStatus(_A)
_HpnicfRS485RawSessionErrInfo_Type=DisplayString
_HpnicfRS485RawSessionErrInfo_Object=MibTableColumn
hpnicfRS485RawSessionErrInfo=_HpnicfRS485RawSessionErrInfo_Object((1,3,6,1,4,1,11,2,14,11,15,2,109,2,3,1,1),_HpnicfRS485RawSessionErrInfo_Type())
hpnicfRS485RawSessionErrInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfRS485RawSessionErrInfo.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'hpnicfRS485':hpnicfRS485,'hpnicfRS485Properties':hpnicfRS485Properties,'hpnicfRS485PropertiesTable':hpnicfRS485PropertiesTable,'hpnicfRS485PropertiesEntry':hpnicfRS485PropertiesEntry,'hpnicfRS485RawSessionNextIndex':hpnicfRS485RawSessionNextIndex,'hpnicfRS485BaudRate':hpnicfRS485BaudRate,'hpnicfRS485DataBits':hpnicfRS485DataBits,'hpnicfRS485Parity':hpnicfRS485Parity,'hpnicfRS485StopBits':hpnicfRS485StopBits,'hpnicfRS485FlowControl':hpnicfRS485FlowControl,'hpnicfRS485TXCharacters':hpnicfRS485TXCharacters,'hpnicfRS485RXCharacters':hpnicfRS485RXCharacters,'hpnicfRS485TXErrCharacters':hpnicfRS485TXErrCharacters,'hpnicfRS485RXErrCharacters':hpnicfRS485RXErrCharacters,'hpnicfRS485ResetCharacters':hpnicfRS485ResetCharacters,'hpnicfRS485RawSessions':hpnicfRS485RawSessions,'hpnicfRS485RawSessionSummary':hpnicfRS485RawSessionSummary,'hpnicfRS485RawSessionMaxNum':hpnicfRS485RawSessionMaxNum,'hpnicfRS485RawSessionTable':hpnicfRS485RawSessionTable,'hpnicfRS485RawSessionEntry':hpnicfRS485RawSessionEntry,_I:hpnicfRS485SessionIndex,'hpnicfRS485SessionType':hpnicfRS485SessionType,'hpnicfRS485SessionAddType':hpnicfRS485SessionAddType,'hpnicfRS485SessionRemoteIP':hpnicfRS485SessionRemoteIP,'hpnicfRS485SessionRemotePort':hpnicfRS485SessionRemotePort,'hpnicfRS485SessionLocalPort':hpnicfRS485SessionLocalPort,'hpnicfRS485SessionStatus':hpnicfRS485SessionStatus,'hpnicfRS485RawSessionErrInfoTable':hpnicfRS485RawSessionErrInfoTable,'hpnicfRS485RawSessionErrInfoEntry':hpnicfRS485RawSessionErrInfoEntry,'hpnicfRS485RawSessionErrInfo':hpnicfRS485RawSessionErrInfo})