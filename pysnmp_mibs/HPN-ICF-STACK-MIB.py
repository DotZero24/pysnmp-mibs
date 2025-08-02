_Q='hpnicfStackTopology'
_P='hpnicfStackPortStatus'
_O='enabled'
_N='OctetString'
_M='hpnicfStackPortIndex'
_L='hpnicfStackMemberID'
_K='disabled'
_J='entPhysicalIndex'
_I='ENTITY-MIB'
_H='ifIndex'
_G='ifDescr'
_F='read-write'
_E='HPN-ICF-STACK-MIB'
_D='Integer32'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_I,_J)
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifDescr,ifIndex=mibBuilder.importSymbols(_C,_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfStack=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,91))
if mibBuilder.loadTexts:hpnicfStack.setRevisions(('2008-04-30 16:50',))
_HpnicfStackGlobalConfig_ObjectIdentity=ObjectIdentity
hpnicfStackGlobalConfig=_HpnicfStackGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,91,1))
_HpnicfStackMaxMember_Type=Integer32
_HpnicfStackMaxMember_Object=MibScalar
hpnicfStackMaxMember=_HpnicfStackMaxMember_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,1,1),_HpnicfStackMaxMember_Type())
hpnicfStackMaxMember.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStackMaxMember.setStatus(_A)
_HpnicfStackMemberNum_Type=Integer32
_HpnicfStackMemberNum_Object=MibScalar
hpnicfStackMemberNum=_HpnicfStackMemberNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,1,2),_HpnicfStackMemberNum_Type())
hpnicfStackMemberNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStackMemberNum.setStatus(_A)
_HpnicfStackMaxConfigPriority_Type=Integer32
_HpnicfStackMaxConfigPriority_Object=MibScalar
hpnicfStackMaxConfigPriority=_HpnicfStackMaxConfigPriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,1,3),_HpnicfStackMaxConfigPriority_Type())
hpnicfStackMaxConfigPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStackMaxConfigPriority.setStatus(_A)
class _HpnicfStackAutoUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_O,2)))
_HpnicfStackAutoUpdate_Type.__name__=_D
_HpnicfStackAutoUpdate_Object=MibScalar
hpnicfStackAutoUpdate=_HpnicfStackAutoUpdate_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,1,4),_HpnicfStackAutoUpdate_Type())
hpnicfStackAutoUpdate.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfStackAutoUpdate.setStatus(_A)
class _HpnicfStackMacPersistence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notPersist',1),('persistForSixMin',2),('persistForever',3)))
_HpnicfStackMacPersistence_Type.__name__=_D
_HpnicfStackMacPersistence_Object=MibScalar
hpnicfStackMacPersistence=_HpnicfStackMacPersistence_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,1,5),_HpnicfStackMacPersistence_Type())
hpnicfStackMacPersistence.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfStackMacPersistence.setStatus(_A)
class _HpnicfStackLinkDelayInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_HpnicfStackLinkDelayInterval_Type.__name__=_D
_HpnicfStackLinkDelayInterval_Object=MibScalar
hpnicfStackLinkDelayInterval=_HpnicfStackLinkDelayInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,1,6),_HpnicfStackLinkDelayInterval_Type())
hpnicfStackLinkDelayInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfStackLinkDelayInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfStackLinkDelayInterval.setUnits('millisecond')
class _HpnicfStackTopology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('chainConn',1),('ringConn',2)))
_HpnicfStackTopology_Type.__name__=_D
_HpnicfStackTopology_Object=MibScalar
hpnicfStackTopology=_HpnicfStackTopology_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,1,7),_HpnicfStackTopology_Type())
hpnicfStackTopology.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStackTopology.setStatus(_A)
_HpnicfStackDeviceConfigTable_Object=MibTable
hpnicfStackDeviceConfigTable=_HpnicfStackDeviceConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,2))
if mibBuilder.loadTexts:hpnicfStackDeviceConfigTable.setStatus(_A)
_HpnicfStackDeviceConfigEntry_Object=MibTableRow
hpnicfStackDeviceConfigEntry=_HpnicfStackDeviceConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,2,1))
hpnicfStackDeviceConfigEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:hpnicfStackDeviceConfigEntry.setStatus(_A)
_HpnicfStackMemberID_Type=Integer32
_HpnicfStackMemberID_Object=MibTableColumn
hpnicfStackMemberID=_HpnicfStackMemberID_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,2,1,1),_HpnicfStackMemberID_Type())
hpnicfStackMemberID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStackMemberID.setStatus(_A)
_HpnicfStackConfigMemberID_Type=Integer32
_HpnicfStackConfigMemberID_Object=MibTableColumn
hpnicfStackConfigMemberID=_HpnicfStackConfigMemberID_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,2,1,2),_HpnicfStackConfigMemberID_Type())
hpnicfStackConfigMemberID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfStackConfigMemberID.setStatus(_A)
_HpnicfStackPriority_Type=Integer32
_HpnicfStackPriority_Object=MibTableColumn
hpnicfStackPriority=_HpnicfStackPriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,2,1,3),_HpnicfStackPriority_Type())
hpnicfStackPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfStackPriority.setStatus(_A)
_HpnicfStackPortNum_Type=Integer32
_HpnicfStackPortNum_Object=MibTableColumn
hpnicfStackPortNum=_HpnicfStackPortNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,2,1,4),_HpnicfStackPortNum_Type())
hpnicfStackPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStackPortNum.setStatus(_A)
_HpnicfStackPortMaxNum_Type=Integer32
_HpnicfStackPortMaxNum_Object=MibTableColumn
hpnicfStackPortMaxNum=_HpnicfStackPortMaxNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,2,1,5),_HpnicfStackPortMaxNum_Type())
hpnicfStackPortMaxNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStackPortMaxNum.setStatus(_A)
_HpnicfStackBoardConfigTable_Object=MibTable
hpnicfStackBoardConfigTable=_HpnicfStackBoardConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,3))
if mibBuilder.loadTexts:hpnicfStackBoardConfigTable.setStatus(_A)
_HpnicfStackBoardConfigEntry_Object=MibTableRow
hpnicfStackBoardConfigEntry=_HpnicfStackBoardConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,3,1))
hpnicfStackBoardConfigEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:hpnicfStackBoardConfigEntry.setStatus(_A)
class _HpnicfStackBoardRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('slave',1),('master',2),('loading',3),('other',4)))
_HpnicfStackBoardRole_Type.__name__=_D
_HpnicfStackBoardRole_Object=MibTableColumn
hpnicfStackBoardRole=_HpnicfStackBoardRole_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,3,1,1),_HpnicfStackBoardRole_Type())
hpnicfStackBoardRole.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStackBoardRole.setStatus(_A)
_HpnicfStackBoardBelongtoMember_Type=Integer32
_HpnicfStackBoardBelongtoMember_Object=MibTableColumn
hpnicfStackBoardBelongtoMember=_HpnicfStackBoardBelongtoMember_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,3,1,2),_HpnicfStackBoardBelongtoMember_Type())
hpnicfStackBoardBelongtoMember.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStackBoardBelongtoMember.setStatus(_A)
_HpnicfStackPortInfoTable_Object=MibTable
hpnicfStackPortInfoTable=_HpnicfStackPortInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,4))
if mibBuilder.loadTexts:hpnicfStackPortInfoTable.setStatus(_A)
_HpnicfStackPortInfoEntry_Object=MibTableRow
hpnicfStackPortInfoEntry=_HpnicfStackPortInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,4,1))
hpnicfStackPortInfoEntry.setIndexNames((0,_E,_L),(0,_E,_M))
if mibBuilder.loadTexts:hpnicfStackPortInfoEntry.setStatus(_A)
_HpnicfStackPortIndex_Type=Integer32
_HpnicfStackPortIndex_Object=MibTableColumn
hpnicfStackPortIndex=_HpnicfStackPortIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,4,1,1),_HpnicfStackPortIndex_Type())
hpnicfStackPortIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hpnicfStackPortIndex.setStatus(_A)
class _HpnicfStackPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_O,2)))
_HpnicfStackPortEnable_Type.__name__=_D
_HpnicfStackPortEnable_Object=MibTableColumn
hpnicfStackPortEnable=_HpnicfStackPortEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,4,1,2),_HpnicfStackPortEnable_Type())
hpnicfStackPortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStackPortEnable.setStatus(_A)
class _HpnicfStackPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('down',2),('silent',3),(_K,4)))
_HpnicfStackPortStatus_Type.__name__=_D
_HpnicfStackPortStatus_Object=MibTableColumn
hpnicfStackPortStatus=_HpnicfStackPortStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,4,1,3),_HpnicfStackPortStatus_Type())
hpnicfStackPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStackPortStatus.setStatus(_A)
_HpnicfStackNeighbor_Type=Integer32
_HpnicfStackNeighbor_Object=MibTableColumn
hpnicfStackNeighbor=_HpnicfStackNeighbor_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,4,1,4),_HpnicfStackNeighbor_Type())
hpnicfStackNeighbor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStackNeighbor.setStatus(_A)
class _HpnicfStackPortForwardingPath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,511))
_HpnicfStackPortForwardingPath_Type.__name__=_N
_HpnicfStackPortForwardingPath_Object=MibTableColumn
hpnicfStackPortForwardingPath=_HpnicfStackPortForwardingPath_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,4,1,5),_HpnicfStackPortForwardingPath_Type())
hpnicfStackPortForwardingPath.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfStackPortForwardingPath.setStatus(_A)
_HpnicfStackPhyPortInfoTable_Object=MibTable
hpnicfStackPhyPortInfoTable=_HpnicfStackPhyPortInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,5))
if mibBuilder.loadTexts:hpnicfStackPhyPortInfoTable.setStatus(_A)
_HpnicfStackPhyPortInfoEntry_Object=MibTableRow
hpnicfStackPhyPortInfoEntry=_HpnicfStackPhyPortInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,5,1))
hpnicfStackPhyPortInfoEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:hpnicfStackPhyPortInfoEntry.setStatus(_A)
_HpnicfStackBelongtoPort_Type=Integer32
_HpnicfStackBelongtoPort_Object=MibTableColumn
hpnicfStackBelongtoPort=_HpnicfStackBelongtoPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,91,5,1,1),_HpnicfStackBelongtoPort_Type())
hpnicfStackBelongtoPort.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfStackBelongtoPort.setStatus(_A)
_HpnicfStackTrap_ObjectIdentity=ObjectIdentity
hpnicfStackTrap=_HpnicfStackTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,91,6))
_HpnicfStackTrapOjbects_ObjectIdentity=ObjectIdentity
hpnicfStackTrapOjbects=_HpnicfStackTrapOjbects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,91,6,0))
hpnicfStackPortLinkStatusChange=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,91,6,0,1))
hpnicfStackPortLinkStatusChange.setObjects(*((_E,_L),(_E,_M),(_E,_P)))
if mibBuilder.loadTexts:hpnicfStackPortLinkStatusChange.setStatus(_A)
hpnicfStackTopologyChange=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,91,6,0,2))
hpnicfStackTopologyChange.setObjects((_E,_Q))
if mibBuilder.loadTexts:hpnicfStackTopologyChange.setStatus(_A)
hpnicfStackMadBfdChangeNormal=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,91,6,0,3))
hpnicfStackMadBfdChangeNormal.setObjects(*((_C,_H),(_C,_G)))
if mibBuilder.loadTexts:hpnicfStackMadBfdChangeNormal.setStatus(_A)
hpnicfStackMadBfdChangeFailure=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,91,6,0,4))
hpnicfStackMadBfdChangeFailure.setObjects(*((_C,_H),(_C,_G)))
if mibBuilder.loadTexts:hpnicfStackMadBfdChangeFailure.setStatus(_A)
hpnicfStackMadLacpChangeNormal=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,91,6,0,5))
hpnicfStackMadLacpChangeNormal.setObjects(*((_C,_H),(_C,_G)))
if mibBuilder.loadTexts:hpnicfStackMadLacpChangeNormal.setStatus(_A)
hpnicfStackMadLacpChangeFailure=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,91,6,0,6))
hpnicfStackMadLacpChangeFailure.setObjects(*((_C,_H),(_C,_G)))
if mibBuilder.loadTexts:hpnicfStackMadLacpChangeFailure.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hpnicfStack':hpnicfStack,'hpnicfStackGlobalConfig':hpnicfStackGlobalConfig,'hpnicfStackMaxMember':hpnicfStackMaxMember,'hpnicfStackMemberNum':hpnicfStackMemberNum,'hpnicfStackMaxConfigPriority':hpnicfStackMaxConfigPriority,'hpnicfStackAutoUpdate':hpnicfStackAutoUpdate,'hpnicfStackMacPersistence':hpnicfStackMacPersistence,'hpnicfStackLinkDelayInterval':hpnicfStackLinkDelayInterval,_Q:hpnicfStackTopology,'hpnicfStackDeviceConfigTable':hpnicfStackDeviceConfigTable,'hpnicfStackDeviceConfigEntry':hpnicfStackDeviceConfigEntry,_L:hpnicfStackMemberID,'hpnicfStackConfigMemberID':hpnicfStackConfigMemberID,'hpnicfStackPriority':hpnicfStackPriority,'hpnicfStackPortNum':hpnicfStackPortNum,'hpnicfStackPortMaxNum':hpnicfStackPortMaxNum,'hpnicfStackBoardConfigTable':hpnicfStackBoardConfigTable,'hpnicfStackBoardConfigEntry':hpnicfStackBoardConfigEntry,'hpnicfStackBoardRole':hpnicfStackBoardRole,'hpnicfStackBoardBelongtoMember':hpnicfStackBoardBelongtoMember,'hpnicfStackPortInfoTable':hpnicfStackPortInfoTable,'hpnicfStackPortInfoEntry':hpnicfStackPortInfoEntry,_M:hpnicfStackPortIndex,'hpnicfStackPortEnable':hpnicfStackPortEnable,_P:hpnicfStackPortStatus,'hpnicfStackNeighbor':hpnicfStackNeighbor,'hpnicfStackPortForwardingPath':hpnicfStackPortForwardingPath,'hpnicfStackPhyPortInfoTable':hpnicfStackPhyPortInfoTable,'hpnicfStackPhyPortInfoEntry':hpnicfStackPhyPortInfoEntry,'hpnicfStackBelongtoPort':hpnicfStackBelongtoPort,'hpnicfStackTrap':hpnicfStackTrap,'hpnicfStackTrapOjbects':hpnicfStackTrapOjbects,'hpnicfStackPortLinkStatusChange':hpnicfStackPortLinkStatusChange,'hpnicfStackTopologyChange':hpnicfStackTopologyChange,'hpnicfStackMadBfdChangeNormal':hpnicfStackMadBfdChangeNormal,'hpnicfStackMadBfdChangeFailure':hpnicfStackMadBfdChangeFailure,'hpnicfStackMadLacpChangeNormal':hpnicfStackMadLacpChangeNormal,'hpnicfStackMadLacpChangeFailure':hpnicfStackMadLacpChangeFailure})