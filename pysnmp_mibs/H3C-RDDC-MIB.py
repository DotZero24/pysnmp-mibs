_U='h3cRddcSwitchReason'
_T='h3cRddcNodeInfo'
_S='invalid'
_R='not-accessible'
_Q='h3cRddcNodeId'
_P='h3cRddcNodeGroupIdx'
_O='seconds'
_N='minutes'
_M='Unsigned32'
_L='OctetString'
_K='accessible-for-notify'
_J='DisplayString'
_I='Integer32'
_H='ifIndex'
_G='ifDescr'
_F='h3cRddcGroupName'
_E='h3cRddcGroupIdx'
_D='IF-MIB'
_C='read-only'
_B='H3C-RDDC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifDescr,ifIndex=mibBuilder.importSymbols(_D,_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
h3cRddc=ModuleIdentity((1,3,6,1,4,1,2011,10,2,151))
if mibBuilder.loadTexts:h3cRddc.setRevisions(('2014-01-03 00:00',))
_H3cRddcNotifications_ObjectIdentity=ObjectIdentity
h3cRddcNotifications=_H3cRddcNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,151,0))
_H3cRddcObjects_ObjectIdentity=ObjectIdentity
h3cRddcObjects=_H3cRddcObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,151,1))
_H3cRddcInfo_ObjectIdentity=ObjectIdentity
h3cRddcInfo=_H3cRddcInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,2,151,1,1))
_H3cRddcTable_Object=MibTable
h3cRddcTable=_H3cRddcTable_Object((1,3,6,1,4,1,2011,10,2,151,1,1,1))
if mibBuilder.loadTexts:h3cRddcTable.setStatus(_A)
_H3cRddcEntry_Object=MibTableRow
h3cRddcEntry=_H3cRddcEntry_Object((1,3,6,1,4,1,2011,10,2,151,1,1,1,1))
h3cRddcEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:h3cRddcEntry.setStatus(_A)
_H3cRddcGroupIdx_Type=Unsigned32
_H3cRddcGroupIdx_Object=MibTableColumn
h3cRddcGroupIdx=_H3cRddcGroupIdx_Object((1,3,6,1,4,1,2011,10,2,151,1,1,1,1,1),_H3cRddcGroupIdx_Type())
h3cRddcGroupIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cRddcGroupIdx.setStatus(_A)
class _H3cRddcGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_H3cRddcGroupName_Type.__name__=_L
_H3cRddcGroupName_Object=MibTableColumn
h3cRddcGroupName=_H3cRddcGroupName_Object((1,3,6,1,4,1,2011,10,2,151,1,1,1,1,2),_H3cRddcGroupName_Type())
h3cRddcGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRddcGroupName.setStatus(_A)
_H3cRddcPreempTimeRemain_Type=Unsigned32
_H3cRddcPreempTimeRemain_Object=MibTableColumn
h3cRddcPreempTimeRemain=_H3cRddcPreempTimeRemain_Object((1,3,6,1,4,1,2011,10,2,151,1,1,1,1,3),_H3cRddcPreempTimeRemain_Type())
h3cRddcPreempTimeRemain.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRddcPreempTimeRemain.setStatus(_A)
if mibBuilder.loadTexts:h3cRddcPreempTimeRemain.setUnits(_N)
_H3cRddcPreempTimeConfig_Type=Unsigned32
_H3cRddcPreempTimeConfig_Object=MibTableColumn
h3cRddcPreempTimeConfig=_H3cRddcPreempTimeConfig_Object((1,3,6,1,4,1,2011,10,2,151,1,1,1,1,4),_H3cRddcPreempTimeConfig_Type())
h3cRddcPreempTimeConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRddcPreempTimeConfig.setStatus(_A)
if mibBuilder.loadTexts:h3cRddcPreempTimeConfig.setUnits(_N)
_H3cRddcHoldTimeRemain_Type=Unsigned32
_H3cRddcHoldTimeRemain_Object=MibTableColumn
h3cRddcHoldTimeRemain=_H3cRddcHoldTimeRemain_Object((1,3,6,1,4,1,2011,10,2,151,1,1,1,1,5),_H3cRddcHoldTimeRemain_Type())
h3cRddcHoldTimeRemain.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRddcHoldTimeRemain.setStatus(_A)
if mibBuilder.loadTexts:h3cRddcHoldTimeRemain.setUnits(_O)
_H3cRddcHoldTimeConfig_Type=Unsigned32
_H3cRddcHoldTimeConfig_Object=MibTableColumn
h3cRddcHoldTimeConfig=_H3cRddcHoldTimeConfig_Object((1,3,6,1,4,1,2011,10,2,151,1,1,1,1,6),_H3cRddcHoldTimeConfig_Type())
h3cRddcHoldTimeConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRddcHoldTimeConfig.setStatus(_A)
if mibBuilder.loadTexts:h3cRddcHoldTimeConfig.setUnits(_O)
_H3cRddcNodeTable_Object=MibTable
h3cRddcNodeTable=_H3cRddcNodeTable_Object((1,3,6,1,4,1,2011,10,2,151,1,1,2))
if mibBuilder.loadTexts:h3cRddcNodeTable.setStatus(_A)
_H3cRddcNodeEntry_Object=MibTableRow
h3cRddcNodeEntry=_H3cRddcNodeEntry_Object((1,3,6,1,4,1,2011,10,2,151,1,1,2,1))
h3cRddcNodeEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:h3cRddcNodeEntry.setStatus(_A)
_H3cRddcNodeGroupIdx_Type=Unsigned32
_H3cRddcNodeGroupIdx_Object=MibTableColumn
h3cRddcNodeGroupIdx=_H3cRddcNodeGroupIdx_Object((1,3,6,1,4,1,2011,10,2,151,1,1,2,1,1),_H3cRddcNodeGroupIdx_Type())
h3cRddcNodeGroupIdx.setMaxAccess(_R)
if mibBuilder.loadTexts:h3cRddcNodeGroupIdx.setStatus(_A)
_H3cRddcNodeId_Type=Unsigned32
_H3cRddcNodeId_Object=MibTableColumn
h3cRddcNodeId=_H3cRddcNodeId_Object((1,3,6,1,4,1,2011,10,2,151,1,1,2,1,2),_H3cRddcNodeId_Type())
h3cRddcNodeId.setMaxAccess(_R)
if mibBuilder.loadTexts:h3cRddcNodeId.setStatus(_A)
class _H3cRddcNodeBindType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),('chassis',2)))
_H3cRddcNodeBindType_Type.__name__=_I
_H3cRddcNodeBindType_Object=MibTableColumn
h3cRddcNodeBindType=_H3cRddcNodeBindType_Object((1,3,6,1,4,1,2011,10,2,151,1,1,2,1,3),_H3cRddcNodeBindType_Type())
h3cRddcNodeBindType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRddcNodeBindType.setStatus(_A)
_H3cRddcNodeBindInfo_Type=Unsigned32
_H3cRddcNodeBindInfo_Object=MibTableColumn
h3cRddcNodeBindInfo=_H3cRddcNodeBindInfo_Object((1,3,6,1,4,1,2011,10,2,151,1,1,2,1,4),_H3cRddcNodeBindInfo_Type())
h3cRddcNodeBindInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRddcNodeBindInfo.setStatus(_A)
class _H3cRddcNodePriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_H3cRddcNodePriority_Type.__name__=_M
_H3cRddcNodePriority_Object=MibTableColumn
h3cRddcNodePriority=_H3cRddcNodePriority_Object((1,3,6,1,4,1,2011,10,2,151,1,1,2,1,5),_H3cRddcNodePriority_Type())
h3cRddcNodePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRddcNodePriority.setStatus(_A)
_H3cRddcNodeWeight_Type=Integer32
_H3cRddcNodeWeight_Object=MibTableColumn
h3cRddcNodeWeight=_H3cRddcNodeWeight_Object((1,3,6,1,4,1,2011,10,2,151,1,1,2,1,6),_H3cRddcNodeWeight_Type())
h3cRddcNodeWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRddcNodeWeight.setStatus(_A)
class _H3cRddcNodeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('master',2),('standby',3)))
_H3cRddcNodeStatus_Type.__name__=_I
_H3cRddcNodeStatus_Object=MibTableColumn
h3cRddcNodeStatus=_H3cRddcNodeStatus_Object((1,3,6,1,4,1,2011,10,2,151,1,1,2,1,7),_H3cRddcNodeStatus_Type())
h3cRddcNodeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cRddcNodeStatus.setStatus(_A)
_H3cRddcTrapObjects_ObjectIdentity=ObjectIdentity
h3cRddcTrapObjects=_H3cRddcTrapObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,151,1,2))
class _H3cRddcNodeInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cRddcNodeInfo_Type.__name__=_J
_H3cRddcNodeInfo_Object=MibScalar
h3cRddcNodeInfo=_H3cRddcNodeInfo_Object((1,3,6,1,4,1,2011,10,2,151,1,2,1),_H3cRddcNodeInfo_Type())
h3cRddcNodeInfo.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cRddcNodeInfo.setStatus(_A)
class _H3cRddcSwitchReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cRddcSwitchReason_Type.__name__=_J
_H3cRddcSwitchReason_Object=MibScalar
h3cRddcSwitchReason=_H3cRddcSwitchReason_Object((1,3,6,1,4,1,2011,10,2,151,1,2,2),_H3cRddcSwitchReason_Type())
h3cRddcSwitchReason.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cRddcSwitchReason.setStatus(_A)
h3cRddcSwitchoverTrap=NotificationType((1,3,6,1,4,1,2011,10,2,151,0,1))
h3cRddcSwitchoverTrap.setObjects(*((_B,_E),(_B,_F),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:h3cRddcSwitchoverTrap.setStatus(_A)
h3cRddcFailIfRecoverTrap=NotificationType((1,3,6,1,4,1,2011,10,2,151,0,2))
h3cRddcFailIfRecoverTrap.setObjects(*((_B,_E),(_B,_F),(_D,_H),(_D,_G)))
if mibBuilder.loadTexts:h3cRddcFailIfRecoverTrap.setStatus(_A)
h3cRddcFailIfGenerateTrap=NotificationType((1,3,6,1,4,1,2011,10,2,151,0,3))
h3cRddcFailIfGenerateTrap.setObjects(*((_B,_E),(_B,_F),(_D,_H),(_D,_G)))
if mibBuilder.loadTexts:h3cRddcFailIfGenerateTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cRddc':h3cRddc,'h3cRddcNotifications':h3cRddcNotifications,'h3cRddcSwitchoverTrap':h3cRddcSwitchoverTrap,'h3cRddcFailIfRecoverTrap':h3cRddcFailIfRecoverTrap,'h3cRddcFailIfGenerateTrap':h3cRddcFailIfGenerateTrap,'h3cRddcObjects':h3cRddcObjects,'h3cRddcInfo':h3cRddcInfo,'h3cRddcTable':h3cRddcTable,'h3cRddcEntry':h3cRddcEntry,_E:h3cRddcGroupIdx,_F:h3cRddcGroupName,'h3cRddcPreempTimeRemain':h3cRddcPreempTimeRemain,'h3cRddcPreempTimeConfig':h3cRddcPreempTimeConfig,'h3cRddcHoldTimeRemain':h3cRddcHoldTimeRemain,'h3cRddcHoldTimeConfig':h3cRddcHoldTimeConfig,'h3cRddcNodeTable':h3cRddcNodeTable,'h3cRddcNodeEntry':h3cRddcNodeEntry,_P:h3cRddcNodeGroupIdx,_Q:h3cRddcNodeId,'h3cRddcNodeBindType':h3cRddcNodeBindType,'h3cRddcNodeBindInfo':h3cRddcNodeBindInfo,'h3cRddcNodePriority':h3cRddcNodePriority,'h3cRddcNodeWeight':h3cRddcNodeWeight,'h3cRddcNodeStatus':h3cRddcNodeStatus,'h3cRddcTrapObjects':h3cRddcTrapObjects,_T:h3cRddcNodeInfo,_U:h3cRddcSwitchReason})