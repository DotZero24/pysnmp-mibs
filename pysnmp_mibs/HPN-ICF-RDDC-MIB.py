_U='hpnicfRddcSwitchReason'
_T='hpnicfRddcNodeInfo'
_S='invalid'
_R='not-accessible'
_Q='hpnicfRddcNodeId'
_P='hpnicfRddcNodeGroupIdx'
_O='seconds'
_N='minutes'
_M='Unsigned32'
_L='OctetString'
_K='accessible-for-notify'
_J='DisplayString'
_I='Integer32'
_H='ifIndex'
_G='ifDescr'
_F='hpnicfRddcGroupName'
_E='hpnicfRddcGroupIdx'
_D='IF-MIB'
_C='read-only'
_B='HPN-ICF-RDDC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifDescr,ifIndex=mibBuilder.importSymbols(_D,_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
hpnicfRddc=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,151))
if mibBuilder.loadTexts:hpnicfRddc.setRevisions(('2014-01-03 00:00',))
_HpnicfRddcNotifications_ObjectIdentity=ObjectIdentity
hpnicfRddcNotifications=_HpnicfRddcNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,151,0))
_HpnicfRddcObjects_ObjectIdentity=ObjectIdentity
hpnicfRddcObjects=_HpnicfRddcObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,151,1))
_HpnicfRddcInfo_ObjectIdentity=ObjectIdentity
hpnicfRddcInfo=_HpnicfRddcInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,151,1,1))
_HpnicfRddcTable_Object=MibTable
hpnicfRddcTable=_HpnicfRddcTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,151,1,1,1))
if mibBuilder.loadTexts:hpnicfRddcTable.setStatus(_A)
_HpnicfRddcEntry_Object=MibTableRow
hpnicfRddcEntry=_HpnicfRddcEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,151,1,1,1,1))
hpnicfRddcEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:hpnicfRddcEntry.setStatus(_A)
_HpnicfRddcGroupIdx_Type=Unsigned32
_HpnicfRddcGroupIdx_Object=MibTableColumn
hpnicfRddcGroupIdx=_HpnicfRddcGroupIdx_Object((1,3,6,1,4,1,11,2,14,11,15,2,151,1,1,1,1,1),_HpnicfRddcGroupIdx_Type())
hpnicfRddcGroupIdx.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfRddcGroupIdx.setStatus(_A)
class _HpnicfRddcGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_HpnicfRddcGroupName_Type.__name__=_L
_HpnicfRddcGroupName_Object=MibTableColumn
hpnicfRddcGroupName=_HpnicfRddcGroupName_Object((1,3,6,1,4,1,11,2,14,11,15,2,151,1,1,1,1,2),_HpnicfRddcGroupName_Type())
hpnicfRddcGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRddcGroupName.setStatus(_A)
_HpnicfRddcPreempTimeRemain_Type=Unsigned32
_HpnicfRddcPreempTimeRemain_Object=MibTableColumn
hpnicfRddcPreempTimeRemain=_HpnicfRddcPreempTimeRemain_Object((1,3,6,1,4,1,11,2,14,11,15,2,151,1,1,1,1,3),_HpnicfRddcPreempTimeRemain_Type())
hpnicfRddcPreempTimeRemain.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRddcPreempTimeRemain.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRddcPreempTimeRemain.setUnits(_N)
_HpnicfRddcPreempTimeConfig_Type=Unsigned32
_HpnicfRddcPreempTimeConfig_Object=MibTableColumn
hpnicfRddcPreempTimeConfig=_HpnicfRddcPreempTimeConfig_Object((1,3,6,1,4,1,11,2,14,11,15,2,151,1,1,1,1,4),_HpnicfRddcPreempTimeConfig_Type())
hpnicfRddcPreempTimeConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRddcPreempTimeConfig.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRddcPreempTimeConfig.setUnits(_N)
_HpnicfRddcHoldTimeRemain_Type=Unsigned32
_HpnicfRddcHoldTimeRemain_Object=MibTableColumn
hpnicfRddcHoldTimeRemain=_HpnicfRddcHoldTimeRemain_Object((1,3,6,1,4,1,11,2,14,11,15,2,151,1,1,1,1,5),_HpnicfRddcHoldTimeRemain_Type())
hpnicfRddcHoldTimeRemain.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRddcHoldTimeRemain.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRddcHoldTimeRemain.setUnits(_O)
_HpnicfRddcHoldTimeConfig_Type=Unsigned32
_HpnicfRddcHoldTimeConfig_Object=MibTableColumn
hpnicfRddcHoldTimeConfig=_HpnicfRddcHoldTimeConfig_Object((1,3,6,1,4,1,11,2,14,11,15,2,151,1,1,1,1,6),_HpnicfRddcHoldTimeConfig_Type())
hpnicfRddcHoldTimeConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRddcHoldTimeConfig.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRddcHoldTimeConfig.setUnits(_O)
_HpnicfRddcNodeTable_Object=MibTable
hpnicfRddcNodeTable=_HpnicfRddcNodeTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,151,1,1,2))
if mibBuilder.loadTexts:hpnicfRddcNodeTable.setStatus(_A)
_HpnicfRddcNodeEntry_Object=MibTableRow
hpnicfRddcNodeEntry=_HpnicfRddcNodeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,151,1,1,2,1))
hpnicfRddcNodeEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:hpnicfRddcNodeEntry.setStatus(_A)
_HpnicfRddcNodeGroupIdx_Type=Unsigned32
_HpnicfRddcNodeGroupIdx_Object=MibTableColumn
hpnicfRddcNodeGroupIdx=_HpnicfRddcNodeGroupIdx_Object((1,3,6,1,4,1,11,2,14,11,15,2,151,1,1,2,1,1),_HpnicfRddcNodeGroupIdx_Type())
hpnicfRddcNodeGroupIdx.setMaxAccess(_R)
if mibBuilder.loadTexts:hpnicfRddcNodeGroupIdx.setStatus(_A)
_HpnicfRddcNodeId_Type=Unsigned32
_HpnicfRddcNodeId_Object=MibTableColumn
hpnicfRddcNodeId=_HpnicfRddcNodeId_Object((1,3,6,1,4,1,11,2,14,11,15,2,151,1,1,2,1,2),_HpnicfRddcNodeId_Type())
hpnicfRddcNodeId.setMaxAccess(_R)
if mibBuilder.loadTexts:hpnicfRddcNodeId.setStatus(_A)
class _HpnicfRddcNodeBindType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),('chassis',2)))
_HpnicfRddcNodeBindType_Type.__name__=_I
_HpnicfRddcNodeBindType_Object=MibTableColumn
hpnicfRddcNodeBindType=_HpnicfRddcNodeBindType_Object((1,3,6,1,4,1,11,2,14,11,15,2,151,1,1,2,1,3),_HpnicfRddcNodeBindType_Type())
hpnicfRddcNodeBindType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRddcNodeBindType.setStatus(_A)
_HpnicfRddcNodeBindInfo_Type=Unsigned32
_HpnicfRddcNodeBindInfo_Object=MibTableColumn
hpnicfRddcNodeBindInfo=_HpnicfRddcNodeBindInfo_Object((1,3,6,1,4,1,11,2,14,11,15,2,151,1,1,2,1,4),_HpnicfRddcNodeBindInfo_Type())
hpnicfRddcNodeBindInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRddcNodeBindInfo.setStatus(_A)
class _HpnicfRddcNodePriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfRddcNodePriority_Type.__name__=_M
_HpnicfRddcNodePriority_Object=MibTableColumn
hpnicfRddcNodePriority=_HpnicfRddcNodePriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,151,1,1,2,1,5),_HpnicfRddcNodePriority_Type())
hpnicfRddcNodePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRddcNodePriority.setStatus(_A)
_HpnicfRddcNodeWeight_Type=Integer32
_HpnicfRddcNodeWeight_Object=MibTableColumn
hpnicfRddcNodeWeight=_HpnicfRddcNodeWeight_Object((1,3,6,1,4,1,11,2,14,11,15,2,151,1,1,2,1,6),_HpnicfRddcNodeWeight_Type())
hpnicfRddcNodeWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRddcNodeWeight.setStatus(_A)
class _HpnicfRddcNodeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('master',2),('standby',3)))
_HpnicfRddcNodeStatus_Type.__name__=_I
_HpnicfRddcNodeStatus_Object=MibTableColumn
hpnicfRddcNodeStatus=_HpnicfRddcNodeStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,151,1,1,2,1,7),_HpnicfRddcNodeStatus_Type())
hpnicfRddcNodeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRddcNodeStatus.setStatus(_A)
_HpnicfRddcTrapObjects_ObjectIdentity=ObjectIdentity
hpnicfRddcTrapObjects=_HpnicfRddcTrapObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,151,1,2))
class _HpnicfRddcNodeInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfRddcNodeInfo_Type.__name__=_J
_HpnicfRddcNodeInfo_Object=MibScalar
hpnicfRddcNodeInfo=_HpnicfRddcNodeInfo_Object((1,3,6,1,4,1,11,2,14,11,15,2,151,1,2,1),_HpnicfRddcNodeInfo_Type())
hpnicfRddcNodeInfo.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfRddcNodeInfo.setStatus(_A)
class _HpnicfRddcSwitchReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfRddcSwitchReason_Type.__name__=_J
_HpnicfRddcSwitchReason_Object=MibScalar
hpnicfRddcSwitchReason=_HpnicfRddcSwitchReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,151,1,2,2),_HpnicfRddcSwitchReason_Type())
hpnicfRddcSwitchReason.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfRddcSwitchReason.setStatus(_A)
hpnicfRddcSwitchoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,151,0,1))
hpnicfRddcSwitchoverTrap.setObjects(*((_B,_E),(_B,_F),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:hpnicfRddcSwitchoverTrap.setStatus(_A)
hpnicfRddcFailIfRecoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,151,0,2))
hpnicfRddcFailIfRecoverTrap.setObjects(*((_B,_E),(_B,_F),(_D,_H),(_D,_G)))
if mibBuilder.loadTexts:hpnicfRddcFailIfRecoverTrap.setStatus(_A)
hpnicfRddcFailIfGenerateTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,151,0,3))
hpnicfRddcFailIfGenerateTrap.setObjects(*((_B,_E),(_B,_F),(_D,_H),(_D,_G)))
if mibBuilder.loadTexts:hpnicfRddcFailIfGenerateTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfRddc':hpnicfRddc,'hpnicfRddcNotifications':hpnicfRddcNotifications,'hpnicfRddcSwitchoverTrap':hpnicfRddcSwitchoverTrap,'hpnicfRddcFailIfRecoverTrap':hpnicfRddcFailIfRecoverTrap,'hpnicfRddcFailIfGenerateTrap':hpnicfRddcFailIfGenerateTrap,'hpnicfRddcObjects':hpnicfRddcObjects,'hpnicfRddcInfo':hpnicfRddcInfo,'hpnicfRddcTable':hpnicfRddcTable,'hpnicfRddcEntry':hpnicfRddcEntry,_E:hpnicfRddcGroupIdx,_F:hpnicfRddcGroupName,'hpnicfRddcPreempTimeRemain':hpnicfRddcPreempTimeRemain,'hpnicfRddcPreempTimeConfig':hpnicfRddcPreempTimeConfig,'hpnicfRddcHoldTimeRemain':hpnicfRddcHoldTimeRemain,'hpnicfRddcHoldTimeConfig':hpnicfRddcHoldTimeConfig,'hpnicfRddcNodeTable':hpnicfRddcNodeTable,'hpnicfRddcNodeEntry':hpnicfRddcNodeEntry,_P:hpnicfRddcNodeGroupIdx,_Q:hpnicfRddcNodeId,'hpnicfRddcNodeBindType':hpnicfRddcNodeBindType,'hpnicfRddcNodeBindInfo':hpnicfRddcNodeBindInfo,'hpnicfRddcNodePriority':hpnicfRddcNodePriority,'hpnicfRddcNodeWeight':hpnicfRddcNodeWeight,'hpnicfRddcNodeStatus':hpnicfRddcNodeStatus,'hpnicfRddcTrapObjects':hpnicfRddcTrapObjects,_T:hpnicfRddcNodeInfo,_U:hpnicfRddcSwitchReason})