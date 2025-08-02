_M='h3cStackTopology'
_L='h3cStackPortStatus'
_K='enabled'
_J='h3cStackPortIndex'
_I='h3cStackMemberID'
_H='disabled'
_G='entPhysicalIndex'
_F='ENTITY-MIB'
_E='read-write'
_D='A3COM-HUAWEI-STACK-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
entPhysicalIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cStack=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,91))
if mibBuilder.loadTexts:h3cStack.setRevisions(('2008-04-30 16:50',))
_H3cStackGlobalConfig_ObjectIdentity=ObjectIdentity
h3cStackGlobalConfig=_H3cStackGlobalConfig_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,91,1))
_H3cStackMaxMember_Type=Integer32
_H3cStackMaxMember_Object=MibScalar
h3cStackMaxMember=_H3cStackMaxMember_Object((1,3,6,1,4,1,43,45,1,10,2,91,1,1),_H3cStackMaxMember_Type())
h3cStackMaxMember.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackMaxMember.setStatus(_A)
_H3cStackMemberNum_Type=Integer32
_H3cStackMemberNum_Object=MibScalar
h3cStackMemberNum=_H3cStackMemberNum_Object((1,3,6,1,4,1,43,45,1,10,2,91,1,2),_H3cStackMemberNum_Type())
h3cStackMemberNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackMemberNum.setStatus(_A)
_H3cStackMaxConfigPriority_Type=Integer32
_H3cStackMaxConfigPriority_Object=MibScalar
h3cStackMaxConfigPriority=_H3cStackMaxConfigPriority_Object((1,3,6,1,4,1,43,45,1,10,2,91,1,3),_H3cStackMaxConfigPriority_Type())
h3cStackMaxConfigPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackMaxConfigPriority.setStatus(_A)
class _H3cStackAutoUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_K,2)))
_H3cStackAutoUpdate_Type.__name__=_C
_H3cStackAutoUpdate_Object=MibScalar
h3cStackAutoUpdate=_H3cStackAutoUpdate_Object((1,3,6,1,4,1,43,45,1,10,2,91,1,4),_H3cStackAutoUpdate_Type())
h3cStackAutoUpdate.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cStackAutoUpdate.setStatus(_A)
class _H3cStackMacPersistence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notPersist',1),('persistForSixMin',2),('persistForever',3)))
_H3cStackMacPersistence_Type.__name__=_C
_H3cStackMacPersistence_Object=MibScalar
h3cStackMacPersistence=_H3cStackMacPersistence_Object((1,3,6,1,4,1,43,45,1,10,2,91,1,5),_H3cStackMacPersistence_Type())
h3cStackMacPersistence.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cStackMacPersistence.setStatus(_A)
class _H3cStackLinkDelayInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_H3cStackLinkDelayInterval_Type.__name__=_C
_H3cStackLinkDelayInterval_Object=MibScalar
h3cStackLinkDelayInterval=_H3cStackLinkDelayInterval_Object((1,3,6,1,4,1,43,45,1,10,2,91,1,6),_H3cStackLinkDelayInterval_Type())
h3cStackLinkDelayInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cStackLinkDelayInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cStackLinkDelayInterval.setUnits('millisecond')
class _H3cStackTopology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('chainConn',1),('ringConn',2)))
_H3cStackTopology_Type.__name__=_C
_H3cStackTopology_Object=MibScalar
h3cStackTopology=_H3cStackTopology_Object((1,3,6,1,4,1,43,45,1,10,2,91,1,7),_H3cStackTopology_Type())
h3cStackTopology.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackTopology.setStatus(_A)
_H3cStackDeviceConfigTable_Object=MibTable
h3cStackDeviceConfigTable=_H3cStackDeviceConfigTable_Object((1,3,6,1,4,1,43,45,1,10,2,91,2))
if mibBuilder.loadTexts:h3cStackDeviceConfigTable.setStatus(_A)
_H3cStackDeviceConfigEntry_Object=MibTableRow
h3cStackDeviceConfigEntry=_H3cStackDeviceConfigEntry_Object((1,3,6,1,4,1,43,45,1,10,2,91,2,1))
h3cStackDeviceConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:h3cStackDeviceConfigEntry.setStatus(_A)
_H3cStackMemberID_Type=Integer32
_H3cStackMemberID_Object=MibTableColumn
h3cStackMemberID=_H3cStackMemberID_Object((1,3,6,1,4,1,43,45,1,10,2,91,2,1,1),_H3cStackMemberID_Type())
h3cStackMemberID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackMemberID.setStatus(_A)
_H3cStackConfigMemberID_Type=Integer32
_H3cStackConfigMemberID_Object=MibTableColumn
h3cStackConfigMemberID=_H3cStackConfigMemberID_Object((1,3,6,1,4,1,43,45,1,10,2,91,2,1,2),_H3cStackConfigMemberID_Type())
h3cStackConfigMemberID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cStackConfigMemberID.setStatus(_A)
_H3cStackPriority_Type=Integer32
_H3cStackPriority_Object=MibTableColumn
h3cStackPriority=_H3cStackPriority_Object((1,3,6,1,4,1,43,45,1,10,2,91,2,1,3),_H3cStackPriority_Type())
h3cStackPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cStackPriority.setStatus(_A)
_H3cStackPortNum_Type=Integer32
_H3cStackPortNum_Object=MibTableColumn
h3cStackPortNum=_H3cStackPortNum_Object((1,3,6,1,4,1,43,45,1,10,2,91,2,1,4),_H3cStackPortNum_Type())
h3cStackPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackPortNum.setStatus(_A)
_H3cStackPortMaxNum_Type=Integer32
_H3cStackPortMaxNum_Object=MibTableColumn
h3cStackPortMaxNum=_H3cStackPortMaxNum_Object((1,3,6,1,4,1,43,45,1,10,2,91,2,1,5),_H3cStackPortMaxNum_Type())
h3cStackPortMaxNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackPortMaxNum.setStatus(_A)
_H3cStackBoardConfigTable_Object=MibTable
h3cStackBoardConfigTable=_H3cStackBoardConfigTable_Object((1,3,6,1,4,1,43,45,1,10,2,91,3))
if mibBuilder.loadTexts:h3cStackBoardConfigTable.setStatus(_A)
_H3cStackBoardConfigEntry_Object=MibTableRow
h3cStackBoardConfigEntry=_H3cStackBoardConfigEntry_Object((1,3,6,1,4,1,43,45,1,10,2,91,3,1))
h3cStackBoardConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:h3cStackBoardConfigEntry.setStatus(_A)
class _H3cStackBoardRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('slave',1),('master',2),('loading',3),('other',4)))
_H3cStackBoardRole_Type.__name__=_C
_H3cStackBoardRole_Object=MibTableColumn
h3cStackBoardRole=_H3cStackBoardRole_Object((1,3,6,1,4,1,43,45,1,10,2,91,3,1,1),_H3cStackBoardRole_Type())
h3cStackBoardRole.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackBoardRole.setStatus(_A)
_H3cStackBoardBelongtoMember_Type=Integer32
_H3cStackBoardBelongtoMember_Object=MibTableColumn
h3cStackBoardBelongtoMember=_H3cStackBoardBelongtoMember_Object((1,3,6,1,4,1,43,45,1,10,2,91,3,1,2),_H3cStackBoardBelongtoMember_Type())
h3cStackBoardBelongtoMember.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackBoardBelongtoMember.setStatus(_A)
_H3cStackPortInfoTable_Object=MibTable
h3cStackPortInfoTable=_H3cStackPortInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,91,4))
if mibBuilder.loadTexts:h3cStackPortInfoTable.setStatus(_A)
_H3cStackPortInfoEntry_Object=MibTableRow
h3cStackPortInfoEntry=_H3cStackPortInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,91,4,1))
h3cStackPortInfoEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:h3cStackPortInfoEntry.setStatus(_A)
_H3cStackPortIndex_Type=Integer32
_H3cStackPortIndex_Object=MibTableColumn
h3cStackPortIndex=_H3cStackPortIndex_Object((1,3,6,1,4,1,43,45,1,10,2,91,4,1,1),_H3cStackPortIndex_Type())
h3cStackPortIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:h3cStackPortIndex.setStatus(_A)
class _H3cStackPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_K,2)))
_H3cStackPortEnable_Type.__name__=_C
_H3cStackPortEnable_Object=MibTableColumn
h3cStackPortEnable=_H3cStackPortEnable_Object((1,3,6,1,4,1,43,45,1,10,2,91,4,1,2),_H3cStackPortEnable_Type())
h3cStackPortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackPortEnable.setStatus(_A)
class _H3cStackPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('down',2),('silent',3),(_H,4)))
_H3cStackPortStatus_Type.__name__=_C
_H3cStackPortStatus_Object=MibTableColumn
h3cStackPortStatus=_H3cStackPortStatus_Object((1,3,6,1,4,1,43,45,1,10,2,91,4,1,3),_H3cStackPortStatus_Type())
h3cStackPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackPortStatus.setStatus(_A)
_H3cStackNeighbor_Type=Integer32
_H3cStackNeighbor_Object=MibTableColumn
h3cStackNeighbor=_H3cStackNeighbor_Object((1,3,6,1,4,1,43,45,1,10,2,91,4,1,4),_H3cStackNeighbor_Type())
h3cStackNeighbor.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackNeighbor.setStatus(_A)
_H3cStackPhyPortInfoTable_Object=MibTable
h3cStackPhyPortInfoTable=_H3cStackPhyPortInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,91,5))
if mibBuilder.loadTexts:h3cStackPhyPortInfoTable.setStatus(_A)
_H3cStackPhyPortInfoEntry_Object=MibTableRow
h3cStackPhyPortInfoEntry=_H3cStackPhyPortInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,91,5,1))
h3cStackPhyPortInfoEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:h3cStackPhyPortInfoEntry.setStatus(_A)
_H3cStackBelongtoPort_Type=Integer32
_H3cStackBelongtoPort_Object=MibTableColumn
h3cStackBelongtoPort=_H3cStackBelongtoPort_Object((1,3,6,1,4,1,43,45,1,10,2,91,5,1,1),_H3cStackBelongtoPort_Type())
h3cStackBelongtoPort.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cStackBelongtoPort.setStatus(_A)
_H3cStackTrap_ObjectIdentity=ObjectIdentity
h3cStackTrap=_H3cStackTrap_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,91,6))
_H3cStackTrapOjbects_ObjectIdentity=ObjectIdentity
h3cStackTrapOjbects=_H3cStackTrapOjbects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,91,6,0))
h3cStackPortLinkStatusChange=NotificationType((1,3,6,1,4,1,43,45,1,10,2,91,6,0,1))
h3cStackPortLinkStatusChange.setObjects(*((_D,_I),(_D,_J),(_D,_L)))
if mibBuilder.loadTexts:h3cStackPortLinkStatusChange.setStatus(_A)
h3cStackTopologyChange=NotificationType((1,3,6,1,4,1,43,45,1,10,2,91,6,0,2))
h3cStackTopologyChange.setObjects((_D,_M))
if mibBuilder.loadTexts:h3cStackTopologyChange.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cStack':h3cStack,'h3cStackGlobalConfig':h3cStackGlobalConfig,'h3cStackMaxMember':h3cStackMaxMember,'h3cStackMemberNum':h3cStackMemberNum,'h3cStackMaxConfigPriority':h3cStackMaxConfigPriority,'h3cStackAutoUpdate':h3cStackAutoUpdate,'h3cStackMacPersistence':h3cStackMacPersistence,'h3cStackLinkDelayInterval':h3cStackLinkDelayInterval,_M:h3cStackTopology,'h3cStackDeviceConfigTable':h3cStackDeviceConfigTable,'h3cStackDeviceConfigEntry':h3cStackDeviceConfigEntry,_I:h3cStackMemberID,'h3cStackConfigMemberID':h3cStackConfigMemberID,'h3cStackPriority':h3cStackPriority,'h3cStackPortNum':h3cStackPortNum,'h3cStackPortMaxNum':h3cStackPortMaxNum,'h3cStackBoardConfigTable':h3cStackBoardConfigTable,'h3cStackBoardConfigEntry':h3cStackBoardConfigEntry,'h3cStackBoardRole':h3cStackBoardRole,'h3cStackBoardBelongtoMember':h3cStackBoardBelongtoMember,'h3cStackPortInfoTable':h3cStackPortInfoTable,'h3cStackPortInfoEntry':h3cStackPortInfoEntry,_J:h3cStackPortIndex,'h3cStackPortEnable':h3cStackPortEnable,_L:h3cStackPortStatus,'h3cStackNeighbor':h3cStackNeighbor,'h3cStackPhyPortInfoTable':h3cStackPhyPortInfoTable,'h3cStackPhyPortInfoEntry':h3cStackPhyPortInfoEntry,'h3cStackBelongtoPort':h3cStackBelongtoPort,'h3cStackTrap':h3cStackTrap,'h3cStackTrapOjbects':h3cStackTrapOjbects,'h3cStackPortLinkStatusChange':h3cStackPortLinkStatusChange,'h3cStackTopologyChange':h3cStackTopologyChange})