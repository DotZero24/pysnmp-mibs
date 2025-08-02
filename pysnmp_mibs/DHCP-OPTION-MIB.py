_Q='rcDhcp6OptionPortCode'
_P='rcDhcp6OptionPortIndex'
_O='rcDhcpOptionPortCode'
_N='rcDhcpOptionPortIndex'
_M='rcDhcp6OptionCode'
_L='rcDhcpOptionCode'
_K='rcDhcpOption82PortIndex'
_J='ipAddress'
_I='hexString'
_H='asciiString'
_G='read-write'
_F='OctetString'
_E='Integer32'
_D='not-accessible'
_C='DHCP-OPTION-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
rcPortIndex,=mibBuilder.importSymbols('SWITCH-SYSTEM-MIB','rcPortIndex')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC','EnableVar')
rcDhcpOption=ModuleIdentity((1,3,6,1,4,1,8886,6,1,41))
if mibBuilder.loadTexts:rcDhcpOption.setRevisions(('2008-11-06 00:00',))
_RcDhcpOptionMibObjects_ObjectIdentity=ObjectIdentity
rcDhcpOptionMibObjects=_RcDhcpOptionMibObjects_ObjectIdentity((1,3,6,1,4,1,8886,6,1,41,1))
_RcDhcpOption82PortGroup_ObjectIdentity=ObjectIdentity
rcDhcpOption82PortGroup=_RcDhcpOption82PortGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,41,1,1))
_RcDhcpOption82PortTable_Object=MibTable
rcDhcpOption82PortTable=_RcDhcpOption82PortTable_Object((1,3,6,1,4,1,8886,6,1,41,1,1,1))
if mibBuilder.loadTexts:rcDhcpOption82PortTable.setStatus(_A)
_RcDhcpOption82PortEntry_Object=MibTableRow
rcDhcpOption82PortEntry=_RcDhcpOption82PortEntry_Object((1,3,6,1,4,1,8886,6,1,41,1,1,1,1))
rcDhcpOption82PortEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:rcDhcpOption82PortEntry.setStatus(_A)
_RcDhcpOption82PortIndex_Type=Integer32
_RcDhcpOption82PortIndex_Object=MibTableColumn
rcDhcpOption82PortIndex=_RcDhcpOption82PortIndex_Object((1,3,6,1,4,1,8886,6,1,41,1,1,1,1,1),_RcDhcpOption82PortIndex_Type())
rcDhcpOption82PortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rcDhcpOption82PortIndex.setStatus(_A)
class _RcDhcpOption82CircuitID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RcDhcpOption82CircuitID_Type.__name__=_F
_RcDhcpOption82CircuitID_Object=MibTableColumn
rcDhcpOption82CircuitID=_RcDhcpOption82CircuitID_Object((1,3,6,1,4,1,8886,6,1,41,1,1,1,1,2),_RcDhcpOption82CircuitID_Type())
rcDhcpOption82CircuitID.setMaxAccess(_G)
if mibBuilder.loadTexts:rcDhcpOption82CircuitID.setStatus(_A)
_RcDhcpOption82ConfigGroup_ObjectIdentity=ObjectIdentity
rcDhcpOption82ConfigGroup=_RcDhcpOption82ConfigGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,41,1,2))
class _RcDhcpOption82AttachString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RcDhcpOption82AttachString_Type.__name__=_F
_RcDhcpOption82AttachString_Object=MibScalar
rcDhcpOption82AttachString=_RcDhcpOption82AttachString_Object((1,3,6,1,4,1,8886,6,1,41,1,2,1),_RcDhcpOption82AttachString_Type())
rcDhcpOption82AttachString.setMaxAccess(_G)
if mibBuilder.loadTexts:rcDhcpOption82AttachString.setStatus(_A)
class _RcDhcpOption82RemoteIDMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('switchmac',1),('clientmac',2),('switchmac-string',3),('clientmac-string',4),('hostname',5),('user-defined',6)))
_RcDhcpOption82RemoteIDMode_Type.__name__=_E
_RcDhcpOption82RemoteIDMode_Object=MibScalar
rcDhcpOption82RemoteIDMode=_RcDhcpOption82RemoteIDMode_Object((1,3,6,1,4,1,8886,6,1,41,1,2,2),_RcDhcpOption82RemoteIDMode_Type())
rcDhcpOption82RemoteIDMode.setMaxAccess(_G)
if mibBuilder.loadTexts:rcDhcpOption82RemoteIDMode.setStatus(_A)
class _RcDhcpOption82RemoteIDString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_RcDhcpOption82RemoteIDString_Type.__name__=_F
_RcDhcpOption82RemoteIDString_Object=MibScalar
rcDhcpOption82RemoteIDString=_RcDhcpOption82RemoteIDString_Object((1,3,6,1,4,1,8886,6,1,41,1,2,3),_RcDhcpOption82RemoteIDString_Type())
rcDhcpOption82RemoteIDString.setMaxAccess(_G)
if mibBuilder.loadTexts:rcDhcpOption82RemoteIDString.setStatus(_A)
_RcDhcpOptionGlobalGroup_ObjectIdentity=ObjectIdentity
rcDhcpOptionGlobalGroup=_RcDhcpOptionGlobalGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,41,1,3))
_RcDhcpOptionGlobalTable_Object=MibTable
rcDhcpOptionGlobalTable=_RcDhcpOptionGlobalTable_Object((1,3,6,1,4,1,8886,6,1,41,1,3,1))
if mibBuilder.loadTexts:rcDhcpOptionGlobalTable.setStatus(_A)
_RcDhcpOptionGlobalEntry_Object=MibTableRow
rcDhcpOptionGlobalEntry=_RcDhcpOptionGlobalEntry_Object((1,3,6,1,4,1,8886,6,1,41,1,3,1,1))
rcDhcpOptionGlobalEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:rcDhcpOptionGlobalEntry.setStatus(_A)
_RcDhcpOptionCode_Type=OctetString
_RcDhcpOptionCode_Object=MibTableColumn
rcDhcpOptionCode=_RcDhcpOptionCode_Object((1,3,6,1,4,1,8886,6,1,41,1,3,1,1,1),_RcDhcpOptionCode_Type())
rcDhcpOptionCode.setMaxAccess(_D)
if mibBuilder.loadTexts:rcDhcpOptionCode.setStatus(_A)
_RcDhcpOptionContent_Type=OctetString
_RcDhcpOptionContent_Object=MibTableColumn
rcDhcpOptionContent=_RcDhcpOptionContent_Object((1,3,6,1,4,1,8886,6,1,41,1,3,1,1,2),_RcDhcpOptionContent_Type())
rcDhcpOptionContent.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpOptionContent.setStatus(_A)
_RcDhcpOptionLength_Type=OctetString
_RcDhcpOptionLength_Object=MibTableColumn
rcDhcpOptionLength=_RcDhcpOptionLength_Object((1,3,6,1,4,1,8886,6,1,41,1,3,1,1,3),_RcDhcpOptionLength_Type())
rcDhcpOptionLength.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpOptionLength.setStatus(_A)
class _RcDhcpOptionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3)))
_RcDhcpOptionType_Type.__name__=_E
_RcDhcpOptionType_Object=MibTableColumn
rcDhcpOptionType=_RcDhcpOptionType_Object((1,3,6,1,4,1,8886,6,1,41,1,3,1,1,4),_RcDhcpOptionType_Type())
rcDhcpOptionType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpOptionType.setStatus(_A)
_RcDhcpOptionRowStatus_Type=RowStatus
_RcDhcpOptionRowStatus_Object=MibTableColumn
rcDhcpOptionRowStatus=_RcDhcpOptionRowStatus_Object((1,3,6,1,4,1,8886,6,1,41,1,3,1,1,5),_RcDhcpOptionRowStatus_Type())
rcDhcpOptionRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpOptionRowStatus.setStatus(_A)
_RcDhcp6OptionGlobalTable_Object=MibTable
rcDhcp6OptionGlobalTable=_RcDhcp6OptionGlobalTable_Object((1,3,6,1,4,1,8886,6,1,41,1,3,2))
if mibBuilder.loadTexts:rcDhcp6OptionGlobalTable.setStatus(_A)
_RcDhcp6OptionGlobalEntry_Object=MibTableRow
rcDhcp6OptionGlobalEntry=_RcDhcp6OptionGlobalEntry_Object((1,3,6,1,4,1,8886,6,1,41,1,3,2,1))
rcDhcp6OptionGlobalEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:rcDhcp6OptionGlobalEntry.setStatus(_A)
_RcDhcp6OptionCode_Type=OctetString
_RcDhcp6OptionCode_Object=MibTableColumn
rcDhcp6OptionCode=_RcDhcp6OptionCode_Object((1,3,6,1,4,1,8886,6,1,41,1,3,2,1,1),_RcDhcp6OptionCode_Type())
rcDhcp6OptionCode.setMaxAccess(_D)
if mibBuilder.loadTexts:rcDhcp6OptionCode.setStatus(_A)
_RcDhcp6OptionContent_Type=OctetString
_RcDhcp6OptionContent_Object=MibTableColumn
rcDhcp6OptionContent=_RcDhcp6OptionContent_Object((1,3,6,1,4,1,8886,6,1,41,1,3,2,1,2),_RcDhcp6OptionContent_Type())
rcDhcp6OptionContent.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcp6OptionContent.setStatus(_A)
_RcDhcp6OptionLength_Type=OctetString
_RcDhcp6OptionLength_Object=MibTableColumn
rcDhcp6OptionLength=_RcDhcp6OptionLength_Object((1,3,6,1,4,1,8886,6,1,41,1,3,2,1,3),_RcDhcp6OptionLength_Type())
rcDhcp6OptionLength.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcp6OptionLength.setStatus(_A)
class _RcDhcp6OptionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3)))
_RcDhcp6OptionType_Type.__name__=_E
_RcDhcp6OptionType_Object=MibTableColumn
rcDhcp6OptionType=_RcDhcp6OptionType_Object((1,3,6,1,4,1,8886,6,1,41,1,3,2,1,4),_RcDhcp6OptionType_Type())
rcDhcp6OptionType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcp6OptionType.setStatus(_A)
_RcDhcp6OptionRowStatus_Type=RowStatus
_RcDhcp6OptionRowStatus_Object=MibTableColumn
rcDhcp6OptionRowStatus=_RcDhcp6OptionRowStatus_Object((1,3,6,1,4,1,8886,6,1,41,1,3,2,1,5),_RcDhcp6OptionRowStatus_Type())
rcDhcp6OptionRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcp6OptionRowStatus.setStatus(_A)
_RcDhcpOptionPortGroup_ObjectIdentity=ObjectIdentity
rcDhcpOptionPortGroup=_RcDhcpOptionPortGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,41,1,4))
_RcDhcpOptionPortTable_Object=MibTable
rcDhcpOptionPortTable=_RcDhcpOptionPortTable_Object((1,3,6,1,4,1,8886,6,1,41,1,4,1))
if mibBuilder.loadTexts:rcDhcpOptionPortTable.setStatus(_A)
_RcDhcpOptionPortEntry_Object=MibTableRow
rcDhcpOptionPortEntry=_RcDhcpOptionPortEntry_Object((1,3,6,1,4,1,8886,6,1,41,1,4,1,1))
rcDhcpOptionPortEntry.setIndexNames((0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:rcDhcpOptionPortEntry.setStatus(_A)
_RcDhcpOptionPortIndex_Type=Integer32
_RcDhcpOptionPortIndex_Object=MibTableColumn
rcDhcpOptionPortIndex=_RcDhcpOptionPortIndex_Object((1,3,6,1,4,1,8886,6,1,41,1,4,1,1,1),_RcDhcpOptionPortIndex_Type())
rcDhcpOptionPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rcDhcpOptionPortIndex.setStatus(_A)
_RcDhcpOptionPortCode_Type=OctetString
_RcDhcpOptionPortCode_Object=MibTableColumn
rcDhcpOptionPortCode=_RcDhcpOptionPortCode_Object((1,3,6,1,4,1,8886,6,1,41,1,4,1,1,2),_RcDhcpOptionPortCode_Type())
rcDhcpOptionPortCode.setMaxAccess(_D)
if mibBuilder.loadTexts:rcDhcpOptionPortCode.setStatus(_A)
_RcDhcpOptionPortContent_Type=OctetString
_RcDhcpOptionPortContent_Object=MibTableColumn
rcDhcpOptionPortContent=_RcDhcpOptionPortContent_Object((1,3,6,1,4,1,8886,6,1,41,1,4,1,1,3),_RcDhcpOptionPortContent_Type())
rcDhcpOptionPortContent.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpOptionPortContent.setStatus(_A)
_RcDhcpOptionPortLength_Type=OctetString
_RcDhcpOptionPortLength_Object=MibTableColumn
rcDhcpOptionPortLength=_RcDhcpOptionPortLength_Object((1,3,6,1,4,1,8886,6,1,41,1,4,1,1,4),_RcDhcpOptionPortLength_Type())
rcDhcpOptionPortLength.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpOptionPortLength.setStatus(_A)
class _RcDhcpOptionPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3)))
_RcDhcpOptionPortType_Type.__name__=_E
_RcDhcpOptionPortType_Object=MibTableColumn
rcDhcpOptionPortType=_RcDhcpOptionPortType_Object((1,3,6,1,4,1,8886,6,1,41,1,4,1,1,5),_RcDhcpOptionPortType_Type())
rcDhcpOptionPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpOptionPortType.setStatus(_A)
_RcDhcpOptionPortRowStatus_Type=RowStatus
_RcDhcpOptionPortRowStatus_Object=MibTableColumn
rcDhcpOptionPortRowStatus=_RcDhcpOptionPortRowStatus_Object((1,3,6,1,4,1,8886,6,1,41,1,4,1,1,6),_RcDhcpOptionPortRowStatus_Type())
rcDhcpOptionPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpOptionPortRowStatus.setStatus(_A)
_RcDhcp6OptionPortTable_Object=MibTable
rcDhcp6OptionPortTable=_RcDhcp6OptionPortTable_Object((1,3,6,1,4,1,8886,6,1,41,1,4,2))
if mibBuilder.loadTexts:rcDhcp6OptionPortTable.setStatus(_A)
_RcDhcp6OptionPortEntry_Object=MibTableRow
rcDhcp6OptionPortEntry=_RcDhcp6OptionPortEntry_Object((1,3,6,1,4,1,8886,6,1,41,1,4,2,1))
rcDhcp6OptionPortEntry.setIndexNames((0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:rcDhcp6OptionPortEntry.setStatus(_A)
_RcDhcp6OptionPortIndex_Type=Integer32
_RcDhcp6OptionPortIndex_Object=MibTableColumn
rcDhcp6OptionPortIndex=_RcDhcp6OptionPortIndex_Object((1,3,6,1,4,1,8886,6,1,41,1,4,2,1,1),_RcDhcp6OptionPortIndex_Type())
rcDhcp6OptionPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rcDhcp6OptionPortIndex.setStatus(_A)
_RcDhcp6OptionPortCode_Type=OctetString
_RcDhcp6OptionPortCode_Object=MibTableColumn
rcDhcp6OptionPortCode=_RcDhcp6OptionPortCode_Object((1,3,6,1,4,1,8886,6,1,41,1,4,2,1,2),_RcDhcp6OptionPortCode_Type())
rcDhcp6OptionPortCode.setMaxAccess(_D)
if mibBuilder.loadTexts:rcDhcp6OptionPortCode.setStatus(_A)
_RcDhcp6OptionPortContent_Type=OctetString
_RcDhcp6OptionPortContent_Object=MibTableColumn
rcDhcp6OptionPortContent=_RcDhcp6OptionPortContent_Object((1,3,6,1,4,1,8886,6,1,41,1,4,2,1,3),_RcDhcp6OptionPortContent_Type())
rcDhcp6OptionPortContent.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcp6OptionPortContent.setStatus(_A)
_RcDhcp6OptionPortLength_Type=OctetString
_RcDhcp6OptionPortLength_Object=MibTableColumn
rcDhcp6OptionPortLength=_RcDhcp6OptionPortLength_Object((1,3,6,1,4,1,8886,6,1,41,1,4,2,1,4),_RcDhcp6OptionPortLength_Type())
rcDhcp6OptionPortLength.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcp6OptionPortLength.setStatus(_A)
class _RcDhcp6OptionPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3)))
_RcDhcp6OptionPortType_Type.__name__=_E
_RcDhcp6OptionPortType_Object=MibTableColumn
rcDhcp6OptionPortType=_RcDhcp6OptionPortType_Object((1,3,6,1,4,1,8886,6,1,41,1,4,2,1,5),_RcDhcp6OptionPortType_Type())
rcDhcp6OptionPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcp6OptionPortType.setStatus(_A)
_RcDhcp6OptionPortRowStatus_Type=RowStatus
_RcDhcp6OptionPortRowStatus_Object=MibTableColumn
rcDhcp6OptionPortRowStatus=_RcDhcp6OptionPortRowStatus_Object((1,3,6,1,4,1,8886,6,1,41,1,4,2,1,6),_RcDhcp6OptionPortRowStatus_Type())
rcDhcp6OptionPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcp6OptionPortRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'rcDhcpOption':rcDhcpOption,'rcDhcpOptionMibObjects':rcDhcpOptionMibObjects,'rcDhcpOption82PortGroup':rcDhcpOption82PortGroup,'rcDhcpOption82PortTable':rcDhcpOption82PortTable,'rcDhcpOption82PortEntry':rcDhcpOption82PortEntry,_K:rcDhcpOption82PortIndex,'rcDhcpOption82CircuitID':rcDhcpOption82CircuitID,'rcDhcpOption82ConfigGroup':rcDhcpOption82ConfigGroup,'rcDhcpOption82AttachString':rcDhcpOption82AttachString,'rcDhcpOption82RemoteIDMode':rcDhcpOption82RemoteIDMode,'rcDhcpOption82RemoteIDString':rcDhcpOption82RemoteIDString,'rcDhcpOptionGlobalGroup':rcDhcpOptionGlobalGroup,'rcDhcpOptionGlobalTable':rcDhcpOptionGlobalTable,'rcDhcpOptionGlobalEntry':rcDhcpOptionGlobalEntry,_L:rcDhcpOptionCode,'rcDhcpOptionContent':rcDhcpOptionContent,'rcDhcpOptionLength':rcDhcpOptionLength,'rcDhcpOptionType':rcDhcpOptionType,'rcDhcpOptionRowStatus':rcDhcpOptionRowStatus,'rcDhcp6OptionGlobalTable':rcDhcp6OptionGlobalTable,'rcDhcp6OptionGlobalEntry':rcDhcp6OptionGlobalEntry,_M:rcDhcp6OptionCode,'rcDhcp6OptionContent':rcDhcp6OptionContent,'rcDhcp6OptionLength':rcDhcp6OptionLength,'rcDhcp6OptionType':rcDhcp6OptionType,'rcDhcp6OptionRowStatus':rcDhcp6OptionRowStatus,'rcDhcpOptionPortGroup':rcDhcpOptionPortGroup,'rcDhcpOptionPortTable':rcDhcpOptionPortTable,'rcDhcpOptionPortEntry':rcDhcpOptionPortEntry,_N:rcDhcpOptionPortIndex,_O:rcDhcpOptionPortCode,'rcDhcpOptionPortContent':rcDhcpOptionPortContent,'rcDhcpOptionPortLength':rcDhcpOptionPortLength,'rcDhcpOptionPortType':rcDhcpOptionPortType,'rcDhcpOptionPortRowStatus':rcDhcpOptionPortRowStatus,'rcDhcp6OptionPortTable':rcDhcp6OptionPortTable,'rcDhcp6OptionPortEntry':rcDhcp6OptionPortEntry,_P:rcDhcp6OptionPortIndex,_Q:rcDhcp6OptionPortCode,'rcDhcp6OptionPortContent':rcDhcp6OptionPortContent,'rcDhcp6OptionPortLength':rcDhcp6OptionPortLength,'rcDhcp6OptionPortType':rcDhcp6OptionPortType,'rcDhcp6OptionPortRowStatus':rcDhcp6OptionPortRowStatus})