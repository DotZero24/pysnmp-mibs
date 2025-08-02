_O='h3cQinQPrioritySwapOld'
_N='h3cQinQVidSwapOld'
_M='h3cQinQPriorityValue'
_L='h3cQinQProtocolIndex'
_K='OctetString'
_J='h3cQinQVlanID'
_I='read-write'
_H='not-accessible'
_G='H3cQinQSwitchState'
_F='ifIndex'
_E='IF-MIB'
_D='A3COM-HUAWEI-QINQ-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cQINQ=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,69))
if mibBuilder.loadTexts:h3cQINQ.setRevisions(('2006-03-10 00:00',))
class H3cQinQSwitchState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_H3cQinQMibObject_ObjectIdentity=ObjectIdentity
h3cQinQMibObject=_H3cQinQMibObject_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,69,1))
_H3cQinQGlobalConfigGroup_ObjectIdentity=ObjectIdentity
h3cQinQGlobalConfigGroup=_H3cQinQGlobalConfigGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,69,1,1))
class _H3cQinQBpduTunnelSwitch_Type(H3cQinQSwitchState):defaultValue=1
_H3cQinQBpduTunnelSwitch_Type.__name__=_G
_H3cQinQBpduTunnelSwitch_Object=MibScalar
h3cQinQBpduTunnelSwitch=_H3cQinQBpduTunnelSwitch_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,1,1),_H3cQinQBpduTunnelSwitch_Type())
h3cQinQBpduTunnelSwitch.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cQinQBpduTunnelSwitch.setStatus(_A)
class _H3cQinQEthernetTypeValue_Type(Integer32):defaultValue=33024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cQinQEthernetTypeValue_Type.__name__=_C
_H3cQinQEthernetTypeValue_Object=MibScalar
h3cQinQEthernetTypeValue=_H3cQinQEthernetTypeValue_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,1,2),_H3cQinQEthernetTypeValue_Type())
h3cQinQEthernetTypeValue.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cQinQEthernetTypeValue.setStatus(_A)
class _H3cQinQServiceTPIDValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cQinQServiceTPIDValue_Type.__name__=_C
_H3cQinQServiceTPIDValue_Object=MibScalar
h3cQinQServiceTPIDValue=_H3cQinQServiceTPIDValue_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,1,3),_H3cQinQServiceTPIDValue_Type())
h3cQinQServiceTPIDValue.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cQinQServiceTPIDValue.setStatus(_A)
class _H3cQinQCustomerTPIDValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cQinQCustomerTPIDValue_Type.__name__=_C
_H3cQinQCustomerTPIDValue_Object=MibScalar
h3cQinQCustomerTPIDValue=_H3cQinQCustomerTPIDValue_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,1,4),_H3cQinQCustomerTPIDValue_Type())
h3cQinQCustomerTPIDValue.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cQinQCustomerTPIDValue.setStatus(_A)
_H3cQinQBpduTunnelTable_Object=MibTable
h3cQinQBpduTunnelTable=_H3cQinQBpduTunnelTable_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,2))
if mibBuilder.loadTexts:h3cQinQBpduTunnelTable.setStatus(_A)
_H3cQinQBpduTunnelEntry_Object=MibTableRow
h3cQinQBpduTunnelEntry=_H3cQinQBpduTunnelEntry_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,2,1))
h3cQinQBpduTunnelEntry.setIndexNames((0,_E,_F),(0,_D,_L))
if mibBuilder.loadTexts:h3cQinQBpduTunnelEntry.setStatus(_A)
class _H3cQinQProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('bpdu',1),('stp',2),('gvrp',3),('igmp',4)))
_H3cQinQProtocolIndex_Type.__name__=_C
_H3cQinQProtocolIndex_Object=MibTableColumn
h3cQinQProtocolIndex=_H3cQinQProtocolIndex_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,2,1,1),_H3cQinQProtocolIndex_Type())
h3cQinQProtocolIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cQinQProtocolIndex.setStatus(_A)
_H3cQinQBpduRowStatus_Type=RowStatus
_H3cQinQBpduRowStatus_Object=MibTableColumn
h3cQinQBpduRowStatus=_H3cQinQBpduRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,2,1,2),_H3cQinQBpduRowStatus_Type())
h3cQinQBpduRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQBpduRowStatus.setStatus(_A)
_H3cQinQPriorityRemarkTable_Object=MibTable
h3cQinQPriorityRemarkTable=_H3cQinQPriorityRemarkTable_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,3))
if mibBuilder.loadTexts:h3cQinQPriorityRemarkTable.setStatus(_A)
_H3cQinQPriorityRemarkEntry_Object=MibTableRow
h3cQinQPriorityRemarkEntry=_H3cQinQPriorityRemarkEntry_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,3,1))
h3cQinQPriorityRemarkEntry.setIndexNames((0,_E,_F),(0,_D,_M))
if mibBuilder.loadTexts:h3cQinQPriorityRemarkEntry.setStatus(_A)
class _H3cQinQPriorityValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_H3cQinQPriorityValue_Type.__name__=_C
_H3cQinQPriorityValue_Object=MibTableColumn
h3cQinQPriorityValue=_H3cQinQPriorityValue_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,3,1,1),_H3cQinQPriorityValue_Type())
h3cQinQPriorityValue.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cQinQPriorityValue.setStatus(_A)
class _H3cQinQPriorityRemarkValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_H3cQinQPriorityRemarkValue_Type.__name__=_C
_H3cQinQPriorityRemarkValue_Object=MibTableColumn
h3cQinQPriorityRemarkValue=_H3cQinQPriorityRemarkValue_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,3,1,2),_H3cQinQPriorityRemarkValue_Type())
h3cQinQPriorityRemarkValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQPriorityRemarkValue.setStatus(_A)
_H3cQinQPriorityRowStatus_Type=RowStatus
_H3cQinQPriorityRowStatus_Object=MibTableColumn
h3cQinQPriorityRowStatus=_H3cQinQPriorityRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,3,1,3),_H3cQinQPriorityRowStatus_Type())
h3cQinQPriorityRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQPriorityRowStatus.setStatus(_A)
_H3cQinQVidTable_Object=MibTable
h3cQinQVidTable=_H3cQinQVidTable_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,4))
if mibBuilder.loadTexts:h3cQinQVidTable.setStatus(_A)
_H3cQinQVidEntry_Object=MibTableRow
h3cQinQVidEntry=_H3cQinQVidEntry_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,4,1))
h3cQinQVidEntry.setIndexNames((0,_E,_F),(0,_D,_J))
if mibBuilder.loadTexts:h3cQinQVidEntry.setStatus(_A)
class _H3cQinQVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_H3cQinQVlanID_Type.__name__=_C
_H3cQinQVlanID_Object=MibTableColumn
h3cQinQVlanID=_H3cQinQVlanID_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,4,1,1),_H3cQinQVlanID_Type())
h3cQinQVlanID.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cQinQVlanID.setStatus(_A)
class _H3cQinQInboundVidListLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_H3cQinQInboundVidListLow_Type.__name__=_K
_H3cQinQInboundVidListLow_Object=MibTableColumn
h3cQinQInboundVidListLow=_H3cQinQInboundVidListLow_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,4,1,2),_H3cQinQInboundVidListLow_Type())
h3cQinQInboundVidListLow.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQInboundVidListLow.setStatus(_A)
class _H3cQinQInboundVidListHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_H3cQinQInboundVidListHigh_Type.__name__=_K
_H3cQinQInboundVidListHigh_Object=MibTableColumn
h3cQinQInboundVidListHigh=_H3cQinQInboundVidListHigh_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,4,1,3),_H3cQinQInboundVidListHigh_Type())
h3cQinQInboundVidListHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQInboundVidListHigh.setStatus(_A)
class _H3cQinQVidEthernetType_Type(Integer32):defaultValue=33024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cQinQVidEthernetType_Type.__name__=_C
_H3cQinQVidEthernetType_Object=MibTableColumn
h3cQinQVidEthernetType=_H3cQinQVidEthernetType_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,4,1,4),_H3cQinQVidEthernetType_Type())
h3cQinQVidEthernetType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQVidEthernetType.setStatus(_A)
_H3cQinQVidRowStatus_Type=RowStatus
_H3cQinQVidRowStatus_Object=MibTableColumn
h3cQinQVidRowStatus=_H3cQinQVidRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,4,1,5),_H3cQinQVidRowStatus_Type())
h3cQinQVidRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQVidRowStatus.setStatus(_A)
_H3cQinQVidSwapTable_Object=MibTable
h3cQinQVidSwapTable=_H3cQinQVidSwapTable_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,5))
if mibBuilder.loadTexts:h3cQinQVidSwapTable.setStatus(_A)
_H3cQinQVidSwapEntry_Object=MibTableRow
h3cQinQVidSwapEntry=_H3cQinQVidSwapEntry_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,5,1))
h3cQinQVidSwapEntry.setIndexNames((0,_E,_F),(0,_D,_J),(0,_D,_N))
if mibBuilder.loadTexts:h3cQinQVidSwapEntry.setStatus(_A)
class _H3cQinQVidSwapOld_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_H3cQinQVidSwapOld_Type.__name__=_C
_H3cQinQVidSwapOld_Object=MibTableColumn
h3cQinQVidSwapOld=_H3cQinQVidSwapOld_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,5,1,1),_H3cQinQVidSwapOld_Type())
h3cQinQVidSwapOld.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cQinQVidSwapOld.setStatus(_A)
class _H3cQinQVidSwapNew_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_H3cQinQVidSwapNew_Type.__name__=_C
_H3cQinQVidSwapNew_Object=MibTableColumn
h3cQinQVidSwapNew=_H3cQinQVidSwapNew_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,5,1,2),_H3cQinQVidSwapNew_Type())
h3cQinQVidSwapNew.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQVidSwapNew.setStatus(_A)
_H3cQinQVidSwapRowStatus_Type=RowStatus
_H3cQinQVidSwapRowStatus_Object=MibTableColumn
h3cQinQVidSwapRowStatus=_H3cQinQVidSwapRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,5,1,3),_H3cQinQVidSwapRowStatus_Type())
h3cQinQVidSwapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQVidSwapRowStatus.setStatus(_A)
_H3cQinQPrioritySwapTable_Object=MibTable
h3cQinQPrioritySwapTable=_H3cQinQPrioritySwapTable_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,6))
if mibBuilder.loadTexts:h3cQinQPrioritySwapTable.setStatus(_A)
_H3cQinQPrioritySwapEntry_Object=MibTableRow
h3cQinQPrioritySwapEntry=_H3cQinQPrioritySwapEntry_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,6,1))
h3cQinQPrioritySwapEntry.setIndexNames((0,_E,_F),(0,_D,_J),(0,_D,_O))
if mibBuilder.loadTexts:h3cQinQPrioritySwapEntry.setStatus(_A)
class _H3cQinQPrioritySwapOld_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_H3cQinQPrioritySwapOld_Type.__name__=_C
_H3cQinQPrioritySwapOld_Object=MibTableColumn
h3cQinQPrioritySwapOld=_H3cQinQPrioritySwapOld_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,6,1,1),_H3cQinQPrioritySwapOld_Type())
h3cQinQPrioritySwapOld.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cQinQPrioritySwapOld.setStatus(_A)
class _H3cQinQPrioritySwapNew_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_H3cQinQPrioritySwapNew_Type.__name__=_C
_H3cQinQPrioritySwapNew_Object=MibTableColumn
h3cQinQPrioritySwapNew=_H3cQinQPrioritySwapNew_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,6,1,2),_H3cQinQPrioritySwapNew_Type())
h3cQinQPrioritySwapNew.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQPrioritySwapNew.setStatus(_A)
_H3cQinQPrioritySwapRowStatus_Type=RowStatus
_H3cQinQPrioritySwapRowStatus_Object=MibTableColumn
h3cQinQPrioritySwapRowStatus=_H3cQinQPrioritySwapRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,6,1,3),_H3cQinQPrioritySwapRowStatus_Type())
h3cQinQPrioritySwapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQPrioritySwapRowStatus.setStatus(_A)
_H3cQinQIfConfigTable_Object=MibTable
h3cQinQIfConfigTable=_H3cQinQIfConfigTable_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,7))
if mibBuilder.loadTexts:h3cQinQIfConfigTable.setStatus(_A)
_H3cQinQIfConfigEntry_Object=MibTableRow
h3cQinQIfConfigEntry=_H3cQinQIfConfigEntry_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,7,1))
h3cQinQIfConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:h3cQinQIfConfigEntry.setStatus(_A)
class _H3cQinQIfEthernetType_Type(Integer32):defaultValue=33024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cQinQIfEthernetType_Type.__name__=_C
_H3cQinQIfEthernetType_Object=MibTableColumn
h3cQinQIfEthernetType=_H3cQinQIfEthernetType_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,7,1,1),_H3cQinQIfEthernetType_Type())
h3cQinQIfEthernetType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQIfEthernetType.setStatus(_A)
class _H3cQinQIfSwitch_Type(H3cQinQSwitchState):defaultValue=2
_H3cQinQIfSwitch_Type.__name__=_G
_H3cQinQIfSwitch_Object=MibTableColumn
h3cQinQIfSwitch=_H3cQinQIfSwitch_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,7,1,2),_H3cQinQIfSwitch_Type())
h3cQinQIfSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQIfSwitch.setStatus(_A)
_H3cQinQIfRowStatus_Type=RowStatus
_H3cQinQIfRowStatus_Object=MibTableColumn
h3cQinQIfRowStatus=_H3cQinQIfRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,7,1,3),_H3cQinQIfRowStatus_Type())
h3cQinQIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQIfRowStatus.setStatus(_A)
class _H3cQinQIfServiceTPIDValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cQinQIfServiceTPIDValue_Type.__name__=_C
_H3cQinQIfServiceTPIDValue_Object=MibTableColumn
h3cQinQIfServiceTPIDValue=_H3cQinQIfServiceTPIDValue_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,7,1,4),_H3cQinQIfServiceTPIDValue_Type())
h3cQinQIfServiceTPIDValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQIfServiceTPIDValue.setStatus(_A)
class _H3cQinQIfCustomerTPIDValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cQinQIfCustomerTPIDValue_Type.__name__=_C
_H3cQinQIfCustomerTPIDValue_Object=MibTableColumn
h3cQinQIfCustomerTPIDValue=_H3cQinQIfCustomerTPIDValue_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,7,1,5),_H3cQinQIfCustomerTPIDValue_Type())
h3cQinQIfCustomerTPIDValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQIfCustomerTPIDValue.setStatus(_A)
class _H3cQinQIfUplinkSwitch_Type(H3cQinQSwitchState):defaultValue=2
_H3cQinQIfUplinkSwitch_Type.__name__=_G
_H3cQinQIfUplinkSwitch_Object=MibTableColumn
h3cQinQIfUplinkSwitch=_H3cQinQIfUplinkSwitch_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,7,1,6),_H3cQinQIfUplinkSwitch_Type())
h3cQinQIfUplinkSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQIfUplinkSwitch.setStatus(_A)
class _H3cQinQIfDownlinkSwitch_Type(H3cQinQSwitchState):defaultValue=2
_H3cQinQIfDownlinkSwitch_Type.__name__=_G
_H3cQinQIfDownlinkSwitch_Object=MibTableColumn
h3cQinQIfDownlinkSwitch=_H3cQinQIfDownlinkSwitch_Object((1,3,6,1,4,1,43,45,1,10,2,69,1,7,1,7),_H3cQinQIfDownlinkSwitch_Type())
h3cQinQIfDownlinkSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQinQIfDownlinkSwitch.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_G:H3cQinQSwitchState,'h3cQINQ':h3cQINQ,'h3cQinQMibObject':h3cQinQMibObject,'h3cQinQGlobalConfigGroup':h3cQinQGlobalConfigGroup,'h3cQinQBpduTunnelSwitch':h3cQinQBpduTunnelSwitch,'h3cQinQEthernetTypeValue':h3cQinQEthernetTypeValue,'h3cQinQServiceTPIDValue':h3cQinQServiceTPIDValue,'h3cQinQCustomerTPIDValue':h3cQinQCustomerTPIDValue,'h3cQinQBpduTunnelTable':h3cQinQBpduTunnelTable,'h3cQinQBpduTunnelEntry':h3cQinQBpduTunnelEntry,_L:h3cQinQProtocolIndex,'h3cQinQBpduRowStatus':h3cQinQBpduRowStatus,'h3cQinQPriorityRemarkTable':h3cQinQPriorityRemarkTable,'h3cQinQPriorityRemarkEntry':h3cQinQPriorityRemarkEntry,_M:h3cQinQPriorityValue,'h3cQinQPriorityRemarkValue':h3cQinQPriorityRemarkValue,'h3cQinQPriorityRowStatus':h3cQinQPriorityRowStatus,'h3cQinQVidTable':h3cQinQVidTable,'h3cQinQVidEntry':h3cQinQVidEntry,_J:h3cQinQVlanID,'h3cQinQInboundVidListLow':h3cQinQInboundVidListLow,'h3cQinQInboundVidListHigh':h3cQinQInboundVidListHigh,'h3cQinQVidEthernetType':h3cQinQVidEthernetType,'h3cQinQVidRowStatus':h3cQinQVidRowStatus,'h3cQinQVidSwapTable':h3cQinQVidSwapTable,'h3cQinQVidSwapEntry':h3cQinQVidSwapEntry,_N:h3cQinQVidSwapOld,'h3cQinQVidSwapNew':h3cQinQVidSwapNew,'h3cQinQVidSwapRowStatus':h3cQinQVidSwapRowStatus,'h3cQinQPrioritySwapTable':h3cQinQPrioritySwapTable,'h3cQinQPrioritySwapEntry':h3cQinQPrioritySwapEntry,_O:h3cQinQPrioritySwapOld,'h3cQinQPrioritySwapNew':h3cQinQPrioritySwapNew,'h3cQinQPrioritySwapRowStatus':h3cQinQPrioritySwapRowStatus,'h3cQinQIfConfigTable':h3cQinQIfConfigTable,'h3cQinQIfConfigEntry':h3cQinQIfConfigEntry,'h3cQinQIfEthernetType':h3cQinQIfEthernetType,'h3cQinQIfSwitch':h3cQinQIfSwitch,'h3cQinQIfRowStatus':h3cQinQIfRowStatus,'h3cQinQIfServiceTPIDValue':h3cQinQIfServiceTPIDValue,'h3cQinQIfCustomerTPIDValue':h3cQinQIfCustomerTPIDValue,'h3cQinQIfUplinkSwitch':h3cQinQIfUplinkSwitch,'h3cQinQIfDownlinkSwitch':h3cQinQIfDownlinkSwitch})