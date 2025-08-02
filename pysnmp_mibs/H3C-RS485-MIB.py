_J='InetAddressType'
_I='h3cRS485SessionIndex'
_H='H3C-RS485-MIB'
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
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_E,_F)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cRS485=ModuleIdentity((1,3,6,1,4,1,2011,10,2,109))
_H3cRS485Properties_ObjectIdentity=ObjectIdentity
h3cRS485Properties=_H3cRS485Properties_ObjectIdentity((1,3,6,1,4,1,2011,10,2,109,1))
_H3cRS485PropertiesTable_Object=MibTable
h3cRS485PropertiesTable=_H3cRS485PropertiesTable_Object((1,3,6,1,4,1,2011,10,2,109,1,1))
if mibBuilder.loadTexts:h3cRS485PropertiesTable.setStatus(_A)
_H3cRS485PropertiesEntry_Object=MibTableRow
h3cRS485PropertiesEntry=_H3cRS485PropertiesEntry_Object((1,3,6,1,4,1,2011,10,2,109,1,1,1))
h3cRS485PropertiesEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:h3cRS485PropertiesEntry.setStatus(_A)
class _H3cRS485RawSessionNextIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_H3cRS485RawSessionNextIndex_Type.__name__=_B
_H3cRS485RawSessionNextIndex_Object=MibTableColumn
h3cRS485RawSessionNextIndex=_H3cRS485RawSessionNextIndex_Object((1,3,6,1,4,1,2011,10,2,109,1,1,1,1),_H3cRS485RawSessionNextIndex_Type())
h3cRS485RawSessionNextIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRS485RawSessionNextIndex.setStatus(_A)
class _H3cRS485BaudRate_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('bautRate300',1),('bautRate600',2),('bautRate1200',3),('bautRate2400',4),('bautRate4800',5),('bautRate9600',6),('bautRate19200',7),('bautRate38400',8),('bautRate57600',9),('bautRate115200',10)))
_H3cRS485BaudRate_Type.__name__=_B
_H3cRS485BaudRate_Object=MibTableColumn
h3cRS485BaudRate=_H3cRS485BaudRate_Object((1,3,6,1,4,1,2011,10,2,109,1,1,1,2),_H3cRS485BaudRate_Type())
h3cRS485BaudRate.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRS485BaudRate.setStatus(_A)
class _H3cRS485DataBits_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('five',1),('six',2),('seven',3),('eight',4)))
_H3cRS485DataBits_Type.__name__=_B
_H3cRS485DataBits_Object=MibTableColumn
h3cRS485DataBits=_H3cRS485DataBits_Object((1,3,6,1,4,1,2011,10,2,109,1,1,1,3),_H3cRS485DataBits_Type())
h3cRS485DataBits.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRS485DataBits.setStatus(_A)
if mibBuilder.loadTexts:h3cRS485DataBits.setUnits('bit')
class _H3cRS485Parity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('odd',2),('even',3),('mark',4),('space',5)))
_H3cRS485Parity_Type.__name__=_B
_H3cRS485Parity_Object=MibTableColumn
h3cRS485Parity=_H3cRS485Parity_Object((1,3,6,1,4,1,2011,10,2,109,1,1,1,4),_H3cRS485Parity_Type())
h3cRS485Parity.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRS485Parity.setStatus(_A)
class _H3cRS485StopBits_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('one',1),('two',2),('oneAndHalf',3)))
_H3cRS485StopBits_Type.__name__=_B
_H3cRS485StopBits_Object=MibTableColumn
h3cRS485StopBits=_H3cRS485StopBits_Object((1,3,6,1,4,1,2011,10,2,109,1,1,1,5),_H3cRS485StopBits_Type())
h3cRS485StopBits.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRS485StopBits.setStatus(_A)
if mibBuilder.loadTexts:h3cRS485StopBits.setUnits('bit')
class _H3cRS485FlowControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('hardware',2),('xonOrxoff',3)))
_H3cRS485FlowControl_Type.__name__=_B
_H3cRS485FlowControl_Object=MibTableColumn
h3cRS485FlowControl=_H3cRS485FlowControl_Object((1,3,6,1,4,1,2011,10,2,109,1,1,1,6),_H3cRS485FlowControl_Type())
h3cRS485FlowControl.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRS485FlowControl.setStatus(_A)
_H3cRS485TXCharacters_Type=Integer32
_H3cRS485TXCharacters_Object=MibTableColumn
h3cRS485TXCharacters=_H3cRS485TXCharacters_Object((1,3,6,1,4,1,2011,10,2,109,1,1,1,7),_H3cRS485TXCharacters_Type())
h3cRS485TXCharacters.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRS485TXCharacters.setStatus(_A)
_H3cRS485RXCharacters_Type=Integer32
_H3cRS485RXCharacters_Object=MibTableColumn
h3cRS485RXCharacters=_H3cRS485RXCharacters_Object((1,3,6,1,4,1,2011,10,2,109,1,1,1,8),_H3cRS485RXCharacters_Type())
h3cRS485RXCharacters.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRS485RXCharacters.setStatus(_A)
_H3cRS485TXErrCharacters_Type=Integer32
_H3cRS485TXErrCharacters_Object=MibTableColumn
h3cRS485TXErrCharacters=_H3cRS485TXErrCharacters_Object((1,3,6,1,4,1,2011,10,2,109,1,1,1,9),_H3cRS485TXErrCharacters_Type())
h3cRS485TXErrCharacters.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRS485TXErrCharacters.setStatus(_A)
_H3cRS485RXErrCharacters_Type=Integer32
_H3cRS485RXErrCharacters_Object=MibTableColumn
h3cRS485RXErrCharacters=_H3cRS485RXErrCharacters_Object((1,3,6,1,4,1,2011,10,2,109,1,1,1,10),_H3cRS485RXErrCharacters_Type())
h3cRS485RXErrCharacters.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRS485RXErrCharacters.setStatus(_A)
class _H3cRS485ResetCharacters_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('counting',1),('clear',2)))
_H3cRS485ResetCharacters_Type.__name__=_B
_H3cRS485ResetCharacters_Object=MibTableColumn
h3cRS485ResetCharacters=_H3cRS485ResetCharacters_Object((1,3,6,1,4,1,2011,10,2,109,1,1,1,11),_H3cRS485ResetCharacters_Type())
h3cRS485ResetCharacters.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRS485ResetCharacters.setStatus(_A)
_H3cRS485RawSessions_ObjectIdentity=ObjectIdentity
h3cRS485RawSessions=_H3cRS485RawSessions_ObjectIdentity((1,3,6,1,4,1,2011,10,2,109,2))
_H3cRS485RawSessionSummary_ObjectIdentity=ObjectIdentity
h3cRS485RawSessionSummary=_H3cRS485RawSessionSummary_ObjectIdentity((1,3,6,1,4,1,2011,10,2,109,2,1))
class _H3cRS485RawSessionMaxNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_H3cRS485RawSessionMaxNum_Type.__name__=_B
_H3cRS485RawSessionMaxNum_Object=MibScalar
h3cRS485RawSessionMaxNum=_H3cRS485RawSessionMaxNum_Object((1,3,6,1,4,1,2011,10,2,109,2,1,1),_H3cRS485RawSessionMaxNum_Type())
h3cRS485RawSessionMaxNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRS485RawSessionMaxNum.setStatus(_A)
_H3cRS485RawSessionTable_Object=MibTable
h3cRS485RawSessionTable=_H3cRS485RawSessionTable_Object((1,3,6,1,4,1,2011,10,2,109,2,2))
if mibBuilder.loadTexts:h3cRS485RawSessionTable.setStatus(_A)
_H3cRS485RawSessionEntry_Object=MibTableRow
h3cRS485RawSessionEntry=_H3cRS485RawSessionEntry_Object((1,3,6,1,4,1,2011,10,2,109,2,2,1))
h3cRS485RawSessionEntry.setIndexNames((0,_E,_F),(0,_H,_I))
if mibBuilder.loadTexts:h3cRS485RawSessionEntry.setStatus(_A)
class _H3cRS485SessionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_H3cRS485SessionIndex_Type.__name__=_B
_H3cRS485SessionIndex_Object=MibTableColumn
h3cRS485SessionIndex=_H3cRS485SessionIndex_Object((1,3,6,1,4,1,2011,10,2,109,2,2,1,1),_H3cRS485SessionIndex_Type())
h3cRS485SessionIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cRS485SessionIndex.setStatus(_A)
class _H3cRS485SessionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('udp',1),('tcpClient',2),('tcpServer',3)))
_H3cRS485SessionType_Type.__name__=_B
_H3cRS485SessionType_Object=MibTableColumn
h3cRS485SessionType=_H3cRS485SessionType_Object((1,3,6,1,4,1,2011,10,2,109,2,2,1,2),_H3cRS485SessionType_Type())
h3cRS485SessionType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRS485SessionType.setStatus(_A)
class _H3cRS485SessionAddType_Type(InetAddressType):defaultValue=1
_H3cRS485SessionAddType_Type.__name__=_J
_H3cRS485SessionAddType_Object=MibTableColumn
h3cRS485SessionAddType=_H3cRS485SessionAddType_Object((1,3,6,1,4,1,2011,10,2,109,2,2,1,3),_H3cRS485SessionAddType_Type())
h3cRS485SessionAddType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRS485SessionAddType.setStatus(_A)
_H3cRS485SessionRemoteIP_Type=InetAddress
_H3cRS485SessionRemoteIP_Object=MibTableColumn
h3cRS485SessionRemoteIP=_H3cRS485SessionRemoteIP_Object((1,3,6,1,4,1,2011,10,2,109,2,2,1,4),_H3cRS485SessionRemoteIP_Type())
h3cRS485SessionRemoteIP.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cRS485SessionRemoteIP.setStatus(_A)
class _H3cRS485SessionRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_H3cRS485SessionRemotePort_Type.__name__=_B
_H3cRS485SessionRemotePort_Object=MibTableColumn
h3cRS485SessionRemotePort=_H3cRS485SessionRemotePort_Object((1,3,6,1,4,1,2011,10,2,109,2,2,1,5),_H3cRS485SessionRemotePort_Type())
h3cRS485SessionRemotePort.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cRS485SessionRemotePort.setStatus(_A)
class _H3cRS485SessionLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,65535))
_H3cRS485SessionLocalPort_Type.__name__=_B
_H3cRS485SessionLocalPort_Object=MibTableColumn
h3cRS485SessionLocalPort=_H3cRS485SessionLocalPort_Object((1,3,6,1,4,1,2011,10,2,109,2,2,1,6),_H3cRS485SessionLocalPort_Type())
h3cRS485SessionLocalPort.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cRS485SessionLocalPort.setStatus(_A)
_H3cRS485SessionStatus_Type=RowStatus
_H3cRS485SessionStatus_Object=MibTableColumn
h3cRS485SessionStatus=_H3cRS485SessionStatus_Object((1,3,6,1,4,1,2011,10,2,109,2,2,1,7),_H3cRS485SessionStatus_Type())
h3cRS485SessionStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cRS485SessionStatus.setStatus(_A)
_H3cRS485RawSessionErrInfoTable_Object=MibTable
h3cRS485RawSessionErrInfoTable=_H3cRS485RawSessionErrInfoTable_Object((1,3,6,1,4,1,2011,10,2,109,2,3))
if mibBuilder.loadTexts:h3cRS485RawSessionErrInfoTable.setStatus(_A)
_H3cRS485RawSessionErrInfoEntry_Object=MibTableRow
h3cRS485RawSessionErrInfoEntry=_H3cRS485RawSessionErrInfoEntry_Object((1,3,6,1,4,1,2011,10,2,109,2,3,1))
h3cRS485RawSessionErrInfoEntry.setIndexNames((0,_E,_F),(0,_H,_I))
if mibBuilder.loadTexts:h3cRS485RawSessionErrInfoEntry.setStatus(_A)
_H3cRS485RawSessionErrInfo_Type=DisplayString
_H3cRS485RawSessionErrInfo_Object=MibTableColumn
h3cRS485RawSessionErrInfo=_H3cRS485RawSessionErrInfo_Object((1,3,6,1,4,1,2011,10,2,109,2,3,1,1),_H3cRS485RawSessionErrInfo_Type())
h3cRS485RawSessionErrInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRS485RawSessionErrInfo.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'h3cRS485':h3cRS485,'h3cRS485Properties':h3cRS485Properties,'h3cRS485PropertiesTable':h3cRS485PropertiesTable,'h3cRS485PropertiesEntry':h3cRS485PropertiesEntry,'h3cRS485RawSessionNextIndex':h3cRS485RawSessionNextIndex,'h3cRS485BaudRate':h3cRS485BaudRate,'h3cRS485DataBits':h3cRS485DataBits,'h3cRS485Parity':h3cRS485Parity,'h3cRS485StopBits':h3cRS485StopBits,'h3cRS485FlowControl':h3cRS485FlowControl,'h3cRS485TXCharacters':h3cRS485TXCharacters,'h3cRS485RXCharacters':h3cRS485RXCharacters,'h3cRS485TXErrCharacters':h3cRS485TXErrCharacters,'h3cRS485RXErrCharacters':h3cRS485RXErrCharacters,'h3cRS485ResetCharacters':h3cRS485ResetCharacters,'h3cRS485RawSessions':h3cRS485RawSessions,'h3cRS485RawSessionSummary':h3cRS485RawSessionSummary,'h3cRS485RawSessionMaxNum':h3cRS485RawSessionMaxNum,'h3cRS485RawSessionTable':h3cRS485RawSessionTable,'h3cRS485RawSessionEntry':h3cRS485RawSessionEntry,_I:h3cRS485SessionIndex,'h3cRS485SessionType':h3cRS485SessionType,'h3cRS485SessionAddType':h3cRS485SessionAddType,'h3cRS485SessionRemoteIP':h3cRS485SessionRemoteIP,'h3cRS485SessionRemotePort':h3cRS485SessionRemotePort,'h3cRS485SessionLocalPort':h3cRS485SessionLocalPort,'h3cRS485SessionStatus':h3cRS485SessionStatus,'h3cRS485RawSessionErrInfoTable':h3cRS485RawSessionErrInfoTable,'h3cRS485RawSessionErrInfoEntry':h3cRS485RawSessionErrInfoEntry,'h3cRS485RawSessionErrInfo':h3cRS485RawSessionErrInfo})