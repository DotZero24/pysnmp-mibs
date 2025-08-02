_O='hpnicfQinQPrioritySwapOld'
_N='hpnicfQinQVidSwapOld'
_M='hpnicfQinQPriorityValue'
_L='hpnicfQinQProtocolIndex'
_K='OctetString'
_J='hpnicfQinQVlanID'
_I='read-write'
_H='not-accessible'
_G='HpnicfQinQSwitchState'
_F='ifIndex'
_E='IF-MIB'
_D='HPN-ICF-QINQ-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfQINQ=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,69))
if mibBuilder.loadTexts:hpnicfQINQ.setRevisions(('2006-03-10 00:00',))
class HpnicfQinQSwitchState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpnicfQinQMibObject_ObjectIdentity=ObjectIdentity
hpnicfQinQMibObject=_HpnicfQinQMibObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,69,1))
_HpnicfQinQGlobalConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfQinQGlobalConfigGroup=_HpnicfQinQGlobalConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,69,1,1))
class _HpnicfQinQBpduTunnelSwitch_Type(HpnicfQinQSwitchState):defaultValue=1
_HpnicfQinQBpduTunnelSwitch_Type.__name__=_G
_HpnicfQinQBpduTunnelSwitch_Object=MibScalar
hpnicfQinQBpduTunnelSwitch=_HpnicfQinQBpduTunnelSwitch_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,1,1),_HpnicfQinQBpduTunnelSwitch_Type())
hpnicfQinQBpduTunnelSwitch.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfQinQBpduTunnelSwitch.setStatus(_A)
class _HpnicfQinQEthernetTypeValue_Type(Integer32):defaultValue=33024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfQinQEthernetTypeValue_Type.__name__=_C
_HpnicfQinQEthernetTypeValue_Object=MibScalar
hpnicfQinQEthernetTypeValue=_HpnicfQinQEthernetTypeValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,1,2),_HpnicfQinQEthernetTypeValue_Type())
hpnicfQinQEthernetTypeValue.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfQinQEthernetTypeValue.setStatus(_A)
class _HpnicfQinQServiceTPIDValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfQinQServiceTPIDValue_Type.__name__=_C
_HpnicfQinQServiceTPIDValue_Object=MibScalar
hpnicfQinQServiceTPIDValue=_HpnicfQinQServiceTPIDValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,1,3),_HpnicfQinQServiceTPIDValue_Type())
hpnicfQinQServiceTPIDValue.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfQinQServiceTPIDValue.setStatus(_A)
class _HpnicfQinQCustomerTPIDValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfQinQCustomerTPIDValue_Type.__name__=_C
_HpnicfQinQCustomerTPIDValue_Object=MibScalar
hpnicfQinQCustomerTPIDValue=_HpnicfQinQCustomerTPIDValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,1,4),_HpnicfQinQCustomerTPIDValue_Type())
hpnicfQinQCustomerTPIDValue.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfQinQCustomerTPIDValue.setStatus(_A)
_HpnicfQinQBpduTunnelTable_Object=MibTable
hpnicfQinQBpduTunnelTable=_HpnicfQinQBpduTunnelTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,2))
if mibBuilder.loadTexts:hpnicfQinQBpduTunnelTable.setStatus(_A)
_HpnicfQinQBpduTunnelEntry_Object=MibTableRow
hpnicfQinQBpduTunnelEntry=_HpnicfQinQBpduTunnelEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,2,1))
hpnicfQinQBpduTunnelEntry.setIndexNames((0,_E,_F),(0,_D,_L))
if mibBuilder.loadTexts:hpnicfQinQBpduTunnelEntry.setStatus(_A)
class _HpnicfQinQProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('bpdu',1),('stp',2),('gmosaic',3),('igmp',4)))
_HpnicfQinQProtocolIndex_Type.__name__=_C
_HpnicfQinQProtocolIndex_Object=MibTableColumn
hpnicfQinQProtocolIndex=_HpnicfQinQProtocolIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,2,1,1),_HpnicfQinQProtocolIndex_Type())
hpnicfQinQProtocolIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfQinQProtocolIndex.setStatus(_A)
_HpnicfQinQBpduRowStatus_Type=RowStatus
_HpnicfQinQBpduRowStatus_Object=MibTableColumn
hpnicfQinQBpduRowStatus=_HpnicfQinQBpduRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,2,1,2),_HpnicfQinQBpduRowStatus_Type())
hpnicfQinQBpduRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQBpduRowStatus.setStatus(_A)
_HpnicfQinQPriorityRemarkTable_Object=MibTable
hpnicfQinQPriorityRemarkTable=_HpnicfQinQPriorityRemarkTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,3))
if mibBuilder.loadTexts:hpnicfQinQPriorityRemarkTable.setStatus(_A)
_HpnicfQinQPriorityRemarkEntry_Object=MibTableRow
hpnicfQinQPriorityRemarkEntry=_HpnicfQinQPriorityRemarkEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,3,1))
hpnicfQinQPriorityRemarkEntry.setIndexNames((0,_E,_F),(0,_D,_M))
if mibBuilder.loadTexts:hpnicfQinQPriorityRemarkEntry.setStatus(_A)
class _HpnicfQinQPriorityValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_HpnicfQinQPriorityValue_Type.__name__=_C
_HpnicfQinQPriorityValue_Object=MibTableColumn
hpnicfQinQPriorityValue=_HpnicfQinQPriorityValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,3,1,1),_HpnicfQinQPriorityValue_Type())
hpnicfQinQPriorityValue.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfQinQPriorityValue.setStatus(_A)
class _HpnicfQinQPriorityRemarkValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfQinQPriorityRemarkValue_Type.__name__=_C
_HpnicfQinQPriorityRemarkValue_Object=MibTableColumn
hpnicfQinQPriorityRemarkValue=_HpnicfQinQPriorityRemarkValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,3,1,2),_HpnicfQinQPriorityRemarkValue_Type())
hpnicfQinQPriorityRemarkValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQPriorityRemarkValue.setStatus(_A)
_HpnicfQinQPriorityRowStatus_Type=RowStatus
_HpnicfQinQPriorityRowStatus_Object=MibTableColumn
hpnicfQinQPriorityRowStatus=_HpnicfQinQPriorityRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,3,1,3),_HpnicfQinQPriorityRowStatus_Type())
hpnicfQinQPriorityRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQPriorityRowStatus.setStatus(_A)
_HpnicfQinQVidTable_Object=MibTable
hpnicfQinQVidTable=_HpnicfQinQVidTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,4))
if mibBuilder.loadTexts:hpnicfQinQVidTable.setStatus(_A)
_HpnicfQinQVidEntry_Object=MibTableRow
hpnicfQinQVidEntry=_HpnicfQinQVidEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,4,1))
hpnicfQinQVidEntry.setIndexNames((0,_E,_F),(0,_D,_J))
if mibBuilder.loadTexts:hpnicfQinQVidEntry.setStatus(_A)
class _HpnicfQinQVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfQinQVlanID_Type.__name__=_C
_HpnicfQinQVlanID_Object=MibTableColumn
hpnicfQinQVlanID=_HpnicfQinQVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,4,1,1),_HpnicfQinQVlanID_Type())
hpnicfQinQVlanID.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfQinQVlanID.setStatus(_A)
class _HpnicfQinQInboundVidListLow_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_HpnicfQinQInboundVidListLow_Type.__name__=_K
_HpnicfQinQInboundVidListLow_Object=MibTableColumn
hpnicfQinQInboundVidListLow=_HpnicfQinQInboundVidListLow_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,4,1,2),_HpnicfQinQInboundVidListLow_Type())
hpnicfQinQInboundVidListLow.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQInboundVidListLow.setStatus(_A)
class _HpnicfQinQInboundVidListHigh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_HpnicfQinQInboundVidListHigh_Type.__name__=_K
_HpnicfQinQInboundVidListHigh_Object=MibTableColumn
hpnicfQinQInboundVidListHigh=_HpnicfQinQInboundVidListHigh_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,4,1,3),_HpnicfQinQInboundVidListHigh_Type())
hpnicfQinQInboundVidListHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQInboundVidListHigh.setStatus(_A)
class _HpnicfQinQVidEthernetType_Type(Integer32):defaultValue=33024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfQinQVidEthernetType_Type.__name__=_C
_HpnicfQinQVidEthernetType_Object=MibTableColumn
hpnicfQinQVidEthernetType=_HpnicfQinQVidEthernetType_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,4,1,4),_HpnicfQinQVidEthernetType_Type())
hpnicfQinQVidEthernetType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQVidEthernetType.setStatus(_A)
_HpnicfQinQVidRowStatus_Type=RowStatus
_HpnicfQinQVidRowStatus_Object=MibTableColumn
hpnicfQinQVidRowStatus=_HpnicfQinQVidRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,4,1,5),_HpnicfQinQVidRowStatus_Type())
hpnicfQinQVidRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQVidRowStatus.setStatus(_A)
_HpnicfQinQVidSwapTable_Object=MibTable
hpnicfQinQVidSwapTable=_HpnicfQinQVidSwapTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,5))
if mibBuilder.loadTexts:hpnicfQinQVidSwapTable.setStatus(_A)
_HpnicfQinQVidSwapEntry_Object=MibTableRow
hpnicfQinQVidSwapEntry=_HpnicfQinQVidSwapEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,5,1))
hpnicfQinQVidSwapEntry.setIndexNames((0,_E,_F),(0,_D,_J),(0,_D,_N))
if mibBuilder.loadTexts:hpnicfQinQVidSwapEntry.setStatus(_A)
class _HpnicfQinQVidSwapOld_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfQinQVidSwapOld_Type.__name__=_C
_HpnicfQinQVidSwapOld_Object=MibTableColumn
hpnicfQinQVidSwapOld=_HpnicfQinQVidSwapOld_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,5,1,1),_HpnicfQinQVidSwapOld_Type())
hpnicfQinQVidSwapOld.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfQinQVidSwapOld.setStatus(_A)
class _HpnicfQinQVidSwapNew_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfQinQVidSwapNew_Type.__name__=_C
_HpnicfQinQVidSwapNew_Object=MibTableColumn
hpnicfQinQVidSwapNew=_HpnicfQinQVidSwapNew_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,5,1,2),_HpnicfQinQVidSwapNew_Type())
hpnicfQinQVidSwapNew.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQVidSwapNew.setStatus(_A)
_HpnicfQinQVidSwapRowStatus_Type=RowStatus
_HpnicfQinQVidSwapRowStatus_Object=MibTableColumn
hpnicfQinQVidSwapRowStatus=_HpnicfQinQVidSwapRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,5,1,3),_HpnicfQinQVidSwapRowStatus_Type())
hpnicfQinQVidSwapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQVidSwapRowStatus.setStatus(_A)
_HpnicfQinQPrioritySwapTable_Object=MibTable
hpnicfQinQPrioritySwapTable=_HpnicfQinQPrioritySwapTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,6))
if mibBuilder.loadTexts:hpnicfQinQPrioritySwapTable.setStatus(_A)
_HpnicfQinQPrioritySwapEntry_Object=MibTableRow
hpnicfQinQPrioritySwapEntry=_HpnicfQinQPrioritySwapEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,6,1))
hpnicfQinQPrioritySwapEntry.setIndexNames((0,_E,_F),(0,_D,_J),(0,_D,_O))
if mibBuilder.loadTexts:hpnicfQinQPrioritySwapEntry.setStatus(_A)
class _HpnicfQinQPrioritySwapOld_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_HpnicfQinQPrioritySwapOld_Type.__name__=_C
_HpnicfQinQPrioritySwapOld_Object=MibTableColumn
hpnicfQinQPrioritySwapOld=_HpnicfQinQPrioritySwapOld_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,6,1,1),_HpnicfQinQPrioritySwapOld_Type())
hpnicfQinQPrioritySwapOld.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfQinQPrioritySwapOld.setStatus(_A)
class _HpnicfQinQPrioritySwapNew_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfQinQPrioritySwapNew_Type.__name__=_C
_HpnicfQinQPrioritySwapNew_Object=MibTableColumn
hpnicfQinQPrioritySwapNew=_HpnicfQinQPrioritySwapNew_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,6,1,2),_HpnicfQinQPrioritySwapNew_Type())
hpnicfQinQPrioritySwapNew.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQPrioritySwapNew.setStatus(_A)
_HpnicfQinQPrioritySwapRowStatus_Type=RowStatus
_HpnicfQinQPrioritySwapRowStatus_Object=MibTableColumn
hpnicfQinQPrioritySwapRowStatus=_HpnicfQinQPrioritySwapRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,6,1,3),_HpnicfQinQPrioritySwapRowStatus_Type())
hpnicfQinQPrioritySwapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQPrioritySwapRowStatus.setStatus(_A)
_HpnicfQinQIfConfigTable_Object=MibTable
hpnicfQinQIfConfigTable=_HpnicfQinQIfConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,7))
if mibBuilder.loadTexts:hpnicfQinQIfConfigTable.setStatus(_A)
_HpnicfQinQIfConfigEntry_Object=MibTableRow
hpnicfQinQIfConfigEntry=_HpnicfQinQIfConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,7,1))
hpnicfQinQIfConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hpnicfQinQIfConfigEntry.setStatus(_A)
class _HpnicfQinQIfEthernetType_Type(Integer32):defaultValue=33024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfQinQIfEthernetType_Type.__name__=_C
_HpnicfQinQIfEthernetType_Object=MibTableColumn
hpnicfQinQIfEthernetType=_HpnicfQinQIfEthernetType_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,7,1,1),_HpnicfQinQIfEthernetType_Type())
hpnicfQinQIfEthernetType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQIfEthernetType.setStatus(_A)
class _HpnicfQinQIfSwitch_Type(HpnicfQinQSwitchState):defaultValue=2
_HpnicfQinQIfSwitch_Type.__name__=_G
_HpnicfQinQIfSwitch_Object=MibTableColumn
hpnicfQinQIfSwitch=_HpnicfQinQIfSwitch_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,7,1,2),_HpnicfQinQIfSwitch_Type())
hpnicfQinQIfSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQIfSwitch.setStatus(_A)
_HpnicfQinQIfRowStatus_Type=RowStatus
_HpnicfQinQIfRowStatus_Object=MibTableColumn
hpnicfQinQIfRowStatus=_HpnicfQinQIfRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,7,1,3),_HpnicfQinQIfRowStatus_Type())
hpnicfQinQIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQIfRowStatus.setStatus(_A)
class _HpnicfQinQIfServiceTPIDValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfQinQIfServiceTPIDValue_Type.__name__=_C
_HpnicfQinQIfServiceTPIDValue_Object=MibTableColumn
hpnicfQinQIfServiceTPIDValue=_HpnicfQinQIfServiceTPIDValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,7,1,4),_HpnicfQinQIfServiceTPIDValue_Type())
hpnicfQinQIfServiceTPIDValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQIfServiceTPIDValue.setStatus(_A)
class _HpnicfQinQIfCustomerTPIDValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfQinQIfCustomerTPIDValue_Type.__name__=_C
_HpnicfQinQIfCustomerTPIDValue_Object=MibTableColumn
hpnicfQinQIfCustomerTPIDValue=_HpnicfQinQIfCustomerTPIDValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,7,1,5),_HpnicfQinQIfCustomerTPIDValue_Type())
hpnicfQinQIfCustomerTPIDValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQIfCustomerTPIDValue.setStatus(_A)
class _HpnicfQinQIfUplinkSwitch_Type(HpnicfQinQSwitchState):defaultValue=2
_HpnicfQinQIfUplinkSwitch_Type.__name__=_G
_HpnicfQinQIfUplinkSwitch_Object=MibTableColumn
hpnicfQinQIfUplinkSwitch=_HpnicfQinQIfUplinkSwitch_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,7,1,6),_HpnicfQinQIfUplinkSwitch_Type())
hpnicfQinQIfUplinkSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQIfUplinkSwitch.setStatus(_A)
class _HpnicfQinQIfDownlinkSwitch_Type(HpnicfQinQSwitchState):defaultValue=2
_HpnicfQinQIfDownlinkSwitch_Type.__name__=_G
_HpnicfQinQIfDownlinkSwitch_Object=MibTableColumn
hpnicfQinQIfDownlinkSwitch=_HpnicfQinQIfDownlinkSwitch_Object((1,3,6,1,4,1,11,2,14,11,15,2,69,1,7,1,7),_HpnicfQinQIfDownlinkSwitch_Type())
hpnicfQinQIfDownlinkSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQinQIfDownlinkSwitch.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_G:HpnicfQinQSwitchState,'hpnicfQINQ':hpnicfQINQ,'hpnicfQinQMibObject':hpnicfQinQMibObject,'hpnicfQinQGlobalConfigGroup':hpnicfQinQGlobalConfigGroup,'hpnicfQinQBpduTunnelSwitch':hpnicfQinQBpduTunnelSwitch,'hpnicfQinQEthernetTypeValue':hpnicfQinQEthernetTypeValue,'hpnicfQinQServiceTPIDValue':hpnicfQinQServiceTPIDValue,'hpnicfQinQCustomerTPIDValue':hpnicfQinQCustomerTPIDValue,'hpnicfQinQBpduTunnelTable':hpnicfQinQBpduTunnelTable,'hpnicfQinQBpduTunnelEntry':hpnicfQinQBpduTunnelEntry,_L:hpnicfQinQProtocolIndex,'hpnicfQinQBpduRowStatus':hpnicfQinQBpduRowStatus,'hpnicfQinQPriorityRemarkTable':hpnicfQinQPriorityRemarkTable,'hpnicfQinQPriorityRemarkEntry':hpnicfQinQPriorityRemarkEntry,_M:hpnicfQinQPriorityValue,'hpnicfQinQPriorityRemarkValue':hpnicfQinQPriorityRemarkValue,'hpnicfQinQPriorityRowStatus':hpnicfQinQPriorityRowStatus,'hpnicfQinQVidTable':hpnicfQinQVidTable,'hpnicfQinQVidEntry':hpnicfQinQVidEntry,_J:hpnicfQinQVlanID,'hpnicfQinQInboundVidListLow':hpnicfQinQInboundVidListLow,'hpnicfQinQInboundVidListHigh':hpnicfQinQInboundVidListHigh,'hpnicfQinQVidEthernetType':hpnicfQinQVidEthernetType,'hpnicfQinQVidRowStatus':hpnicfQinQVidRowStatus,'hpnicfQinQVidSwapTable':hpnicfQinQVidSwapTable,'hpnicfQinQVidSwapEntry':hpnicfQinQVidSwapEntry,_N:hpnicfQinQVidSwapOld,'hpnicfQinQVidSwapNew':hpnicfQinQVidSwapNew,'hpnicfQinQVidSwapRowStatus':hpnicfQinQVidSwapRowStatus,'hpnicfQinQPrioritySwapTable':hpnicfQinQPrioritySwapTable,'hpnicfQinQPrioritySwapEntry':hpnicfQinQPrioritySwapEntry,_O:hpnicfQinQPrioritySwapOld,'hpnicfQinQPrioritySwapNew':hpnicfQinQPrioritySwapNew,'hpnicfQinQPrioritySwapRowStatus':hpnicfQinQPrioritySwapRowStatus,'hpnicfQinQIfConfigTable':hpnicfQinQIfConfigTable,'hpnicfQinQIfConfigEntry':hpnicfQinQIfConfigEntry,'hpnicfQinQIfEthernetType':hpnicfQinQIfEthernetType,'hpnicfQinQIfSwitch':hpnicfQinQIfSwitch,'hpnicfQinQIfRowStatus':hpnicfQinQIfRowStatus,'hpnicfQinQIfServiceTPIDValue':hpnicfQinQIfServiceTPIDValue,'hpnicfQinQIfCustomerTPIDValue':hpnicfQinQIfCustomerTPIDValue,'hpnicfQinQIfUplinkSwitch':hpnicfQinQIfUplinkSwitch,'hpnicfQinQIfDownlinkSwitch':hpnicfQinQIfDownlinkSwitch})