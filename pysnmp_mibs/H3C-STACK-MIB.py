_R='h3cStackTopology'
_Q='h3cStackPortStatus'
_P='enabled'
_O='Unsigned32'
_N='OctetString'
_M='h3cStackPortIndex'
_L='h3cStackMemberID'
_K='disabled'
_J='entPhysicalIndex'
_I='ENTITY-MIB'
_H='ifIndex'
_G='ifDescr'
_F='H3C-STACK-MIB'
_E='read-write'
_D='Integer32'
_C='IF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_I,_J)
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifDescr,ifIndex=mibBuilder.importSymbols(_C,_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_O,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cStack=ModuleIdentity((1,3,6,1,4,1,2011,10,2,91))
if mibBuilder.loadTexts:h3cStack.setRevisions(('2014-11-20 08:50','2014-08-11 06:41','2013-10-23 00:00','2013-08-16 00:00','2012-02-24 00:00','2008-04-30 16:50'))
_H3cStackGlobalConfig_ObjectIdentity=ObjectIdentity
h3cStackGlobalConfig=_H3cStackGlobalConfig_ObjectIdentity((1,3,6,1,4,1,2011,10,2,91,1))
_H3cStackMaxMember_Type=Integer32
_H3cStackMaxMember_Object=MibScalar
h3cStackMaxMember=_H3cStackMaxMember_Object((1,3,6,1,4,1,2011,10,2,91,1,1),_H3cStackMaxMember_Type())
h3cStackMaxMember.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackMaxMember.setStatus(_A)
_H3cStackMemberNum_Type=Integer32
_H3cStackMemberNum_Object=MibScalar
h3cStackMemberNum=_H3cStackMemberNum_Object((1,3,6,1,4,1,2011,10,2,91,1,2),_H3cStackMemberNum_Type())
h3cStackMemberNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackMemberNum.setStatus(_A)
_H3cStackMaxConfigPriority_Type=Integer32
_H3cStackMaxConfigPriority_Object=MibScalar
h3cStackMaxConfigPriority=_H3cStackMaxConfigPriority_Object((1,3,6,1,4,1,2011,10,2,91,1,3),_H3cStackMaxConfigPriority_Type())
h3cStackMaxConfigPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackMaxConfigPriority.setStatus(_A)
class _H3cStackAutoUpdate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_P,2)))
_H3cStackAutoUpdate_Type.__name__=_D
_H3cStackAutoUpdate_Object=MibScalar
h3cStackAutoUpdate=_H3cStackAutoUpdate_Object((1,3,6,1,4,1,2011,10,2,91,1,4),_H3cStackAutoUpdate_Type())
h3cStackAutoUpdate.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cStackAutoUpdate.setStatus(_A)
class _H3cStackMacPersistence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notPersist',1),('persistForSixMin',2),('persistForever',3)))
_H3cStackMacPersistence_Type.__name__=_D
_H3cStackMacPersistence_Object=MibScalar
h3cStackMacPersistence=_H3cStackMacPersistence_Object((1,3,6,1,4,1,2011,10,2,91,1,5),_H3cStackMacPersistence_Type())
h3cStackMacPersistence.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cStackMacPersistence.setStatus(_A)
class _H3cStackLinkDelayInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cStackLinkDelayInterval_Type.__name__=_D
_H3cStackLinkDelayInterval_Object=MibScalar
h3cStackLinkDelayInterval=_H3cStackLinkDelayInterval_Object((1,3,6,1,4,1,2011,10,2,91,1,6),_H3cStackLinkDelayInterval_Type())
h3cStackLinkDelayInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cStackLinkDelayInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cStackLinkDelayInterval.setUnits('millisecond')
class _H3cStackTopology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('chainConn',1),('ringConn',2)))
_H3cStackTopology_Type.__name__=_D
_H3cStackTopology_Object=MibScalar
h3cStackTopology=_H3cStackTopology_Object((1,3,6,1,4,1,2011,10,2,91,1,7),_H3cStackTopology_Type())
h3cStackTopology.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackTopology.setStatus(_A)
class _H3cStackDomainId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_H3cStackDomainId_Type.__name__=_O
_H3cStackDomainId_Object=MibScalar
h3cStackDomainId=_H3cStackDomainId_Object((1,3,6,1,4,1,2011,10,2,91,1,8),_H3cStackDomainId_Type())
h3cStackDomainId.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cStackDomainId.setStatus(_A)
class _H3cStackPortConfigActivate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('set',2)))
_H3cStackPortConfigActivate_Type.__name__=_D
_H3cStackPortConfigActivate_Object=MibScalar
h3cStackPortConfigActivate=_H3cStackPortConfigActivate_Object((1,3,6,1,4,1,2011,10,2,91,1,9),_H3cStackPortConfigActivate_Type())
h3cStackPortConfigActivate.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cStackPortConfigActivate.setStatus(_A)
_H3cStackDeviceConfigTable_Object=MibTable
h3cStackDeviceConfigTable=_H3cStackDeviceConfigTable_Object((1,3,6,1,4,1,2011,10,2,91,2))
if mibBuilder.loadTexts:h3cStackDeviceConfigTable.setStatus(_A)
_H3cStackDeviceConfigEntry_Object=MibTableRow
h3cStackDeviceConfigEntry=_H3cStackDeviceConfigEntry_Object((1,3,6,1,4,1,2011,10,2,91,2,1))
h3cStackDeviceConfigEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:h3cStackDeviceConfigEntry.setStatus(_A)
_H3cStackMemberID_Type=Integer32
_H3cStackMemberID_Object=MibTableColumn
h3cStackMemberID=_H3cStackMemberID_Object((1,3,6,1,4,1,2011,10,2,91,2,1,1),_H3cStackMemberID_Type())
h3cStackMemberID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackMemberID.setStatus(_A)
_H3cStackConfigMemberID_Type=Integer32
_H3cStackConfigMemberID_Object=MibTableColumn
h3cStackConfigMemberID=_H3cStackConfigMemberID_Object((1,3,6,1,4,1,2011,10,2,91,2,1,2),_H3cStackConfigMemberID_Type())
h3cStackConfigMemberID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cStackConfigMemberID.setStatus(_A)
_H3cStackPriority_Type=Integer32
_H3cStackPriority_Object=MibTableColumn
h3cStackPriority=_H3cStackPriority_Object((1,3,6,1,4,1,2011,10,2,91,2,1,3),_H3cStackPriority_Type())
h3cStackPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cStackPriority.setStatus(_A)
_H3cStackPortNum_Type=Integer32
_H3cStackPortNum_Object=MibTableColumn
h3cStackPortNum=_H3cStackPortNum_Object((1,3,6,1,4,1,2011,10,2,91,2,1,4),_H3cStackPortNum_Type())
h3cStackPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackPortNum.setStatus(_A)
_H3cStackPortMaxNum_Type=Integer32
_H3cStackPortMaxNum_Object=MibTableColumn
h3cStackPortMaxNum=_H3cStackPortMaxNum_Object((1,3,6,1,4,1,2011,10,2,91,2,1,5),_H3cStackPortMaxNum_Type())
h3cStackPortMaxNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackPortMaxNum.setStatus(_A)
_H3cStackBoardConfigTable_Object=MibTable
h3cStackBoardConfigTable=_H3cStackBoardConfigTable_Object((1,3,6,1,4,1,2011,10,2,91,3))
if mibBuilder.loadTexts:h3cStackBoardConfigTable.setStatus(_A)
_H3cStackBoardConfigEntry_Object=MibTableRow
h3cStackBoardConfigEntry=_H3cStackBoardConfigEntry_Object((1,3,6,1,4,1,2011,10,2,91,3,1))
h3cStackBoardConfigEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:h3cStackBoardConfigEntry.setStatus(_A)
class _H3cStackBoardRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('slave',1),('master',2),('loading',3),('other',4)))
_H3cStackBoardRole_Type.__name__=_D
_H3cStackBoardRole_Object=MibTableColumn
h3cStackBoardRole=_H3cStackBoardRole_Object((1,3,6,1,4,1,2011,10,2,91,3,1,1),_H3cStackBoardRole_Type())
h3cStackBoardRole.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackBoardRole.setStatus(_A)
_H3cStackBoardBelongtoMember_Type=Integer32
_H3cStackBoardBelongtoMember_Object=MibTableColumn
h3cStackBoardBelongtoMember=_H3cStackBoardBelongtoMember_Object((1,3,6,1,4,1,2011,10,2,91,3,1,2),_H3cStackBoardBelongtoMember_Type())
h3cStackBoardBelongtoMember.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackBoardBelongtoMember.setStatus(_A)
_H3cStackPortInfoTable_Object=MibTable
h3cStackPortInfoTable=_H3cStackPortInfoTable_Object((1,3,6,1,4,1,2011,10,2,91,4))
if mibBuilder.loadTexts:h3cStackPortInfoTable.setStatus(_A)
_H3cStackPortInfoEntry_Object=MibTableRow
h3cStackPortInfoEntry=_H3cStackPortInfoEntry_Object((1,3,6,1,4,1,2011,10,2,91,4,1))
h3cStackPortInfoEntry.setIndexNames((0,_F,_L),(0,_F,_M))
if mibBuilder.loadTexts:h3cStackPortInfoEntry.setStatus(_A)
_H3cStackPortIndex_Type=Integer32
_H3cStackPortIndex_Object=MibTableColumn
h3cStackPortIndex=_H3cStackPortIndex_Object((1,3,6,1,4,1,2011,10,2,91,4,1,1),_H3cStackPortIndex_Type())
h3cStackPortIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:h3cStackPortIndex.setStatus(_A)
class _H3cStackPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_P,2)))
_H3cStackPortEnable_Type.__name__=_D
_H3cStackPortEnable_Object=MibTableColumn
h3cStackPortEnable=_H3cStackPortEnable_Object((1,3,6,1,4,1,2011,10,2,91,4,1,2),_H3cStackPortEnable_Type())
h3cStackPortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackPortEnable.setStatus(_A)
class _H3cStackPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('up',1),('down',2),('silent',3),(_K,4)))
_H3cStackPortStatus_Type.__name__=_D
_H3cStackPortStatus_Object=MibTableColumn
h3cStackPortStatus=_H3cStackPortStatus_Object((1,3,6,1,4,1,2011,10,2,91,4,1,3),_H3cStackPortStatus_Type())
h3cStackPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackPortStatus.setStatus(_A)
_H3cStackNeighbor_Type=Integer32
_H3cStackNeighbor_Object=MibTableColumn
h3cStackNeighbor=_H3cStackNeighbor_Object((1,3,6,1,4,1,2011,10,2,91,4,1,4),_H3cStackNeighbor_Type())
h3cStackNeighbor.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackNeighbor.setStatus(_A)
class _H3cStackPortForwardingPath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,511))
_H3cStackPortForwardingPath_Type.__name__=_N
_H3cStackPortForwardingPath_Object=MibTableColumn
h3cStackPortForwardingPath=_H3cStackPortForwardingPath_Object((1,3,6,1,4,1,2011,10,2,91,4,1,5),_H3cStackPortForwardingPath_Type())
h3cStackPortForwardingPath.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cStackPortForwardingPath.setStatus(_A)
_H3cStackPhyPortInfoTable_Object=MibTable
h3cStackPhyPortInfoTable=_H3cStackPhyPortInfoTable_Object((1,3,6,1,4,1,2011,10,2,91,5))
if mibBuilder.loadTexts:h3cStackPhyPortInfoTable.setStatus(_A)
_H3cStackPhyPortInfoEntry_Object=MibTableRow
h3cStackPhyPortInfoEntry=_H3cStackPhyPortInfoEntry_Object((1,3,6,1,4,1,2011,10,2,91,5,1))
h3cStackPhyPortInfoEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:h3cStackPhyPortInfoEntry.setStatus(_A)
_H3cStackBelongtoPort_Type=Integer32
_H3cStackBelongtoPort_Object=MibTableColumn
h3cStackBelongtoPort=_H3cStackBelongtoPort_Object((1,3,6,1,4,1,2011,10,2,91,5,1,1),_H3cStackBelongtoPort_Type())
h3cStackBelongtoPort.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cStackBelongtoPort.setStatus(_A)
_H3cStackTrap_ObjectIdentity=ObjectIdentity
h3cStackTrap=_H3cStackTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,91,6))
_H3cStackTrapOjbects_ObjectIdentity=ObjectIdentity
h3cStackTrapOjbects=_H3cStackTrapOjbects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,91,6,0))
h3cStackPortLinkStatusChange=NotificationType((1,3,6,1,4,1,2011,10,2,91,6,0,1))
h3cStackPortLinkStatusChange.setObjects(*((_F,_L),(_F,_M),(_F,_Q)))
if mibBuilder.loadTexts:h3cStackPortLinkStatusChange.setStatus(_A)
h3cStackTopologyChange=NotificationType((1,3,6,1,4,1,2011,10,2,91,6,0,2))
h3cStackTopologyChange.setObjects((_F,_R))
if mibBuilder.loadTexts:h3cStackTopologyChange.setStatus(_A)
h3cStackMadBfdChangeNormal=NotificationType((1,3,6,1,4,1,2011,10,2,91,6,0,3))
h3cStackMadBfdChangeNormal.setObjects(*((_C,_H),(_C,_G)))
if mibBuilder.loadTexts:h3cStackMadBfdChangeNormal.setStatus(_A)
h3cStackMadBfdChangeFailure=NotificationType((1,3,6,1,4,1,2011,10,2,91,6,0,4))
h3cStackMadBfdChangeFailure.setObjects(*((_C,_H),(_C,_G)))
if mibBuilder.loadTexts:h3cStackMadBfdChangeFailure.setStatus(_A)
h3cStackMadLacpChangeNormal=NotificationType((1,3,6,1,4,1,2011,10,2,91,6,0,5))
h3cStackMadLacpChangeNormal.setObjects(*((_C,_H),(_C,_G)))
if mibBuilder.loadTexts:h3cStackMadLacpChangeNormal.setStatus(_A)
h3cStackMadLacpChangeFailure=NotificationType((1,3,6,1,4,1,2011,10,2,91,6,0,6))
h3cStackMadLacpChangeFailure.setObjects(*((_C,_H),(_C,_G)))
if mibBuilder.loadTexts:h3cStackMadLacpChangeFailure.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'h3cStack':h3cStack,'h3cStackGlobalConfig':h3cStackGlobalConfig,'h3cStackMaxMember':h3cStackMaxMember,'h3cStackMemberNum':h3cStackMemberNum,'h3cStackMaxConfigPriority':h3cStackMaxConfigPriority,'h3cStackAutoUpdate':h3cStackAutoUpdate,'h3cStackMacPersistence':h3cStackMacPersistence,'h3cStackLinkDelayInterval':h3cStackLinkDelayInterval,_R:h3cStackTopology,'h3cStackDomainId':h3cStackDomainId,'h3cStackPortConfigActivate':h3cStackPortConfigActivate,'h3cStackDeviceConfigTable':h3cStackDeviceConfigTable,'h3cStackDeviceConfigEntry':h3cStackDeviceConfigEntry,_L:h3cStackMemberID,'h3cStackConfigMemberID':h3cStackConfigMemberID,'h3cStackPriority':h3cStackPriority,'h3cStackPortNum':h3cStackPortNum,'h3cStackPortMaxNum':h3cStackPortMaxNum,'h3cStackBoardConfigTable':h3cStackBoardConfigTable,'h3cStackBoardConfigEntry':h3cStackBoardConfigEntry,'h3cStackBoardRole':h3cStackBoardRole,'h3cStackBoardBelongtoMember':h3cStackBoardBelongtoMember,'h3cStackPortInfoTable':h3cStackPortInfoTable,'h3cStackPortInfoEntry':h3cStackPortInfoEntry,_M:h3cStackPortIndex,'h3cStackPortEnable':h3cStackPortEnable,_Q:h3cStackPortStatus,'h3cStackNeighbor':h3cStackNeighbor,'h3cStackPortForwardingPath':h3cStackPortForwardingPath,'h3cStackPhyPortInfoTable':h3cStackPhyPortInfoTable,'h3cStackPhyPortInfoEntry':h3cStackPhyPortInfoEntry,'h3cStackBelongtoPort':h3cStackBelongtoPort,'h3cStackTrap':h3cStackTrap,'h3cStackTrapOjbects':h3cStackTrapOjbects,'h3cStackPortLinkStatusChange':h3cStackPortLinkStatusChange,'h3cStackTopologyChange':h3cStackTopologyChange,'h3cStackMadBfdChangeNormal':h3cStackMadBfdChangeNormal,'h3cStackMadBfdChangeFailure':h3cStackMadBfdChangeFailure,'h3cStackMadLacpChangeNormal':h3cStackMadLacpChangeNormal,'h3cStackMadLacpChangeFailure':h3cStackMadLacpChangeFailure})