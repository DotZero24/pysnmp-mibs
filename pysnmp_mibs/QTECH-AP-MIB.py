_x='qtechApMIBGroup'
_w='qtechApProfMplsSrcPort'
_v='qtechApProfMplsVlan'
_u='qtechApProfMplsDestIp'
_t='qtechApProfMplsSrcIp'
_s='qtechApProfMpls2ndLabel'
_r='qtechApProfMplsTopLabel'
_q='qtechApProfIpv6SrcPort'
_p='qtechApProfIpv6Vlan'
_o='qtechApProfIpv6L4DestPort'
_n='qtechApProfIpv6L4SrcPort'
_m='qtechApProfIpv6Pro'
_l='qtechApProfIpv6DestIp'
_k='qtechApProfIpv6SrcIp'
_j='qtechApProfIpv4SrcPort'
_i='qtechApProfIpv4Vlan'
_h='qtechApProfIpv4L4DestPort'
_g='qtechApProfIpv4L4SrcPort'
_f='qtechApProfIpv4Pro'
_e='qtechApProfIpv4DestIp'
_d='qtechApProfIpv4SrcIp'
_c='qtechApProfL2SrcPort'
_b='qtechApProfL2Vlan'
_a='qtechApProfL2Pro'
_Z='qtechApProfL2DestMac'
_Y='qtechApProfL2SrcMac'
_X='qtechApPortMemberAction'
_W='qtechApPortMemberApNumber'
_V='qtechApConfigAction'
_U='qtechApConfigPortMember'
_T='qtechApConfigCurrentPtNumber'
_S='qtechApConfigMaxPtNumber'
_R='qtechApConfigIndex'
_Q='qtechApFlowBalance'
_P='qtechApMaxPtNumber'
_O='qtechApMemberAction'
_N='qtechApPortConfigApIndex'
_M='qtechApCurrentNumber'
_L='qtechApMaxNumber'
_K='qtechApProfIdx'
_J='qtechApPortConfigPortIndex'
_I='Integer32'
_H='qtechApPortMemberPortIndex'
_G='qtechApConfigNumber'
_F='qtechApIndex'
_E='obsolete'
_D='read-only'
_C='read-write'
_B='QTECH-AP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
IfIndex,MemberMap=mibBuilder.importSymbols('QTECH-TC','IfIndex','MemberMap')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
qtechApMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,7))
if mibBuilder.loadTexts:qtechApMIB.setRevisions(('2002-03-20 00:00',))
_QtechApMIBObjects_ObjectIdentity=ObjectIdentity
qtechApMIBObjects=_QtechApMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,7,1))
_QtechApMaxNumber_Type=Integer32
_QtechApMaxNumber_Object=MibScalar
qtechApMaxNumber=_QtechApMaxNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,1),_QtechApMaxNumber_Type())
qtechApMaxNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechApMaxNumber.setStatus(_A)
_QtechApCurrentNumber_Type=Integer32
_QtechApCurrentNumber_Object=MibScalar
qtechApCurrentNumber=_QtechApCurrentNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,2),_QtechApCurrentNumber_Type())
qtechApCurrentNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechApCurrentNumber.setStatus(_A)
_QtechApPortConfigTable_Object=MibTable
qtechApPortConfigTable=_QtechApPortConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,3))
if mibBuilder.loadTexts:qtechApPortConfigTable.setStatus(_E)
_QtechApPortConfigEntry_Object=MibTableRow
qtechApPortConfigEntry=_QtechApPortConfigEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,3,1))
qtechApPortConfigEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:qtechApPortConfigEntry.setStatus(_E)
_QtechApPortConfigPortIndex_Type=IfIndex
_QtechApPortConfigPortIndex_Object=MibTableColumn
qtechApPortConfigPortIndex=_QtechApPortConfigPortIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,3,1,1),_QtechApPortConfigPortIndex_Type())
qtechApPortConfigPortIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:qtechApPortConfigPortIndex.setStatus(_E)
_QtechApPortConfigApIndex_Type=IfIndex
_QtechApPortConfigApIndex_Object=MibTableColumn
qtechApPortConfigApIndex=_QtechApPortConfigApIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,3,1,2),_QtechApPortConfigApIndex_Type())
qtechApPortConfigApIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApPortConfigApIndex.setStatus(_E)
_QtechApTable_Object=MibTable
qtechApTable=_QtechApTable_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,4))
if mibBuilder.loadTexts:qtechApTable.setStatus(_E)
_QtechApEntry_Object=MibTableRow
qtechApEntry=_QtechApEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,4,1))
qtechApEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:qtechApEntry.setStatus(_E)
_QtechApIndex_Type=IfIndex
_QtechApIndex_Object=MibTableColumn
qtechApIndex=_QtechApIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,4,1,1),_QtechApIndex_Type())
qtechApIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechApIndex.setStatus(_E)
_QtechApMemberAction_Type=MemberMap
_QtechApMemberAction_Object=MibTableColumn
qtechApMemberAction=_QtechApMemberAction_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,4,1,2),_QtechApMemberAction_Type())
qtechApMemberAction.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechApMemberAction.setStatus(_E)
_QtechApPossibleMember_Type=MemberMap
_QtechApPossibleMember_Object=MibTableColumn
qtechApPossibleMember=_QtechApPossibleMember_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,4,1,3),_QtechApPossibleMember_Type())
qtechApPossibleMember.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechApPossibleMember.setStatus(_E)
_QtechApMaxPtNumber_Type=Integer32
_QtechApMaxPtNumber_Object=MibTableColumn
qtechApMaxPtNumber=_QtechApMaxPtNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,4,1,4),_QtechApMaxPtNumber_Type())
qtechApMaxPtNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechApMaxPtNumber.setStatus(_E)
class _QtechApFlowBalance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*(('unknown',0),('source-mac',1),('destination-mac',2),('src-dest-mac',3),('source-ip',4),('destination-ip',5),('src-dest-ip',6),('src-dest-port',7),('src-dst-ip-l4port',8),('enhanced-profile',9),('src-l4port',10),('dest-l4port',11),('src-dest-l4port',12),('src-ip-l4port',13),('dest-ip-l4port',14),('src-ip-dest-l4port',15),('dest-ip-src-l4port',16),('src-dest-ip-src-l4port',17),('src-dest-ip-dest-l4port',18),('src-ip-src-dest-l4port',19),('dest-ip-src-dest-l4port',20)))
_QtechApFlowBalance_Type.__name__=_I
_QtechApFlowBalance_Object=MibScalar
qtechApFlowBalance=_QtechApFlowBalance_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,5),_QtechApFlowBalance_Type())
qtechApFlowBalance.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApFlowBalance.setStatus(_A)
_QtechApConfigTable_Object=MibTable
qtechApConfigTable=_QtechApConfigTable_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,6))
if mibBuilder.loadTexts:qtechApConfigTable.setStatus(_A)
_QtechApConfigEntry_Object=MibTableRow
qtechApConfigEntry=_QtechApConfigEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,6,1))
qtechApConfigEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:qtechApConfigEntry.setStatus(_A)
_QtechApConfigNumber_Type=Integer32
_QtechApConfigNumber_Object=MibTableColumn
qtechApConfigNumber=_QtechApConfigNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,6,1,1),_QtechApConfigNumber_Type())
qtechApConfigNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApConfigNumber.setStatus(_A)
_QtechApConfigIndex_Type=IfIndex
_QtechApConfigIndex_Object=MibTableColumn
qtechApConfigIndex=_QtechApConfigIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,6,1,2),_QtechApConfigIndex_Type())
qtechApConfigIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechApConfigIndex.setStatus(_A)
_QtechApConfigMaxPtNumber_Type=Integer32
_QtechApConfigMaxPtNumber_Object=MibTableColumn
qtechApConfigMaxPtNumber=_QtechApConfigMaxPtNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,6,1,3),_QtechApConfigMaxPtNumber_Type())
qtechApConfigMaxPtNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechApConfigMaxPtNumber.setStatus(_A)
_QtechApConfigCurrentPtNumber_Type=Integer32
_QtechApConfigCurrentPtNumber_Object=MibTableColumn
qtechApConfigCurrentPtNumber=_QtechApConfigCurrentPtNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,6,1,4),_QtechApConfigCurrentPtNumber_Type())
qtechApConfigCurrentPtNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechApConfigCurrentPtNumber.setStatus(_A)
_QtechApConfigPortMember_Type=PortList
_QtechApConfigPortMember_Object=MibTableColumn
qtechApConfigPortMember=_QtechApConfigPortMember_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,6,1,5),_QtechApConfigPortMember_Type())
qtechApConfigPortMember.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechApConfigPortMember.setStatus(_A)
_QtechApConfigAction_Type=Integer32
_QtechApConfigAction_Object=MibTableColumn
qtechApConfigAction=_QtechApConfigAction_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,6,1,6),_QtechApConfigAction_Type())
qtechApConfigAction.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApConfigAction.setStatus(_A)
_QtechApPortMemberTable_Object=MibTable
qtechApPortMemberTable=_QtechApPortMemberTable_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,7))
if mibBuilder.loadTexts:qtechApPortMemberTable.setStatus(_A)
_QtechApPortMemberEntry_Object=MibTableRow
qtechApPortMemberEntry=_QtechApPortMemberEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,7,1))
qtechApPortMemberEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:qtechApPortMemberEntry.setStatus(_A)
_QtechApPortMemberPortIndex_Type=IfIndex
_QtechApPortMemberPortIndex_Object=MibTableColumn
qtechApPortMemberPortIndex=_QtechApPortMemberPortIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,7,1,1),_QtechApPortMemberPortIndex_Type())
qtechApPortMemberPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechApPortMemberPortIndex.setStatus(_A)
_QtechApPortMemberApNumber_Type=Integer32
_QtechApPortMemberApNumber_Object=MibTableColumn
qtechApPortMemberApNumber=_QtechApPortMemberApNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,7,1,2),_QtechApPortMemberApNumber_Type())
qtechApPortMemberApNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApPortMemberApNumber.setStatus(_A)
_QtechApPortMemberAction_Type=Integer32
_QtechApPortMemberAction_Object=MibTableColumn
qtechApPortMemberAction=_QtechApPortMemberAction_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,7,1,3),_QtechApPortMemberAction_Type())
qtechApPortMemberAction.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApPortMemberAction.setStatus(_A)
_QtechApBalcProfName_Type=DisplayString
_QtechApBalcProfName_Object=MibScalar
qtechApBalcProfName=_QtechApBalcProfName_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,8),_QtechApBalcProfName_Type())
qtechApBalcProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApBalcProfName.setStatus(_A)
_QtechApProfTable_Object=MibTable
qtechApProfTable=_QtechApProfTable_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9))
if mibBuilder.loadTexts:qtechApProfTable.setStatus(_A)
_QtechApProfEntry_Object=MibTableRow
qtechApProfEntry=_QtechApProfEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1))
qtechApProfEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:qtechApProfEntry.setStatus(_A)
_QtechApProfIdx_Type=Integer32
_QtechApProfIdx_Object=MibTableColumn
qtechApProfIdx=_QtechApProfIdx_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,1),_QtechApProfIdx_Type())
qtechApProfIdx.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechApProfIdx.setStatus(_A)
_QtechApProfName_Type=DisplayString
_QtechApProfName_Object=MibTableColumn
qtechApProfName=_QtechApProfName_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,2),_QtechApProfName_Type())
qtechApProfName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechApProfName.setStatus(_A)
_QtechApProfL2SrcMac_Type=TruthValue
_QtechApProfL2SrcMac_Object=MibTableColumn
qtechApProfL2SrcMac=_QtechApProfL2SrcMac_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,3),_QtechApProfL2SrcMac_Type())
qtechApProfL2SrcMac.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfL2SrcMac.setStatus(_A)
_QtechApProfL2DestMac_Type=TruthValue
_QtechApProfL2DestMac_Object=MibTableColumn
qtechApProfL2DestMac=_QtechApProfL2DestMac_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,4),_QtechApProfL2DestMac_Type())
qtechApProfL2DestMac.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfL2DestMac.setStatus(_A)
_QtechApProfL2Pro_Type=TruthValue
_QtechApProfL2Pro_Object=MibTableColumn
qtechApProfL2Pro=_QtechApProfL2Pro_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,5),_QtechApProfL2Pro_Type())
qtechApProfL2Pro.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfL2Pro.setStatus(_A)
_QtechApProfL2Vlan_Type=TruthValue
_QtechApProfL2Vlan_Object=MibTableColumn
qtechApProfL2Vlan=_QtechApProfL2Vlan_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,6),_QtechApProfL2Vlan_Type())
qtechApProfL2Vlan.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfL2Vlan.setStatus(_A)
_QtechApProfL2SrcPort_Type=TruthValue
_QtechApProfL2SrcPort_Object=MibTableColumn
qtechApProfL2SrcPort=_QtechApProfL2SrcPort_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,7),_QtechApProfL2SrcPort_Type())
qtechApProfL2SrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfL2SrcPort.setStatus(_A)
_QtechApProfIpv4SrcIp_Type=TruthValue
_QtechApProfIpv4SrcIp_Object=MibTableColumn
qtechApProfIpv4SrcIp=_QtechApProfIpv4SrcIp_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,8),_QtechApProfIpv4SrcIp_Type())
qtechApProfIpv4SrcIp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfIpv4SrcIp.setStatus(_A)
_QtechApProfIpv4DestIp_Type=TruthValue
_QtechApProfIpv4DestIp_Object=MibTableColumn
qtechApProfIpv4DestIp=_QtechApProfIpv4DestIp_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,9),_QtechApProfIpv4DestIp_Type())
qtechApProfIpv4DestIp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfIpv4DestIp.setStatus(_A)
_QtechApProfIpv4Pro_Type=TruthValue
_QtechApProfIpv4Pro_Object=MibTableColumn
qtechApProfIpv4Pro=_QtechApProfIpv4Pro_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,10),_QtechApProfIpv4Pro_Type())
qtechApProfIpv4Pro.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfIpv4Pro.setStatus(_A)
_QtechApProfIpv4L4SrcPort_Type=TruthValue
_QtechApProfIpv4L4SrcPort_Object=MibTableColumn
qtechApProfIpv4L4SrcPort=_QtechApProfIpv4L4SrcPort_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,11),_QtechApProfIpv4L4SrcPort_Type())
qtechApProfIpv4L4SrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfIpv4L4SrcPort.setStatus(_A)
_QtechApProfIpv4L4DestPort_Type=TruthValue
_QtechApProfIpv4L4DestPort_Object=MibTableColumn
qtechApProfIpv4L4DestPort=_QtechApProfIpv4L4DestPort_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,12),_QtechApProfIpv4L4DestPort_Type())
qtechApProfIpv4L4DestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfIpv4L4DestPort.setStatus(_A)
_QtechApProfIpv4Vlan_Type=TruthValue
_QtechApProfIpv4Vlan_Object=MibTableColumn
qtechApProfIpv4Vlan=_QtechApProfIpv4Vlan_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,13),_QtechApProfIpv4Vlan_Type())
qtechApProfIpv4Vlan.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfIpv4Vlan.setStatus(_A)
_QtechApProfIpv4SrcPort_Type=TruthValue
_QtechApProfIpv4SrcPort_Object=MibTableColumn
qtechApProfIpv4SrcPort=_QtechApProfIpv4SrcPort_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,14),_QtechApProfIpv4SrcPort_Type())
qtechApProfIpv4SrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfIpv4SrcPort.setStatus(_A)
_QtechApProfIpv6SrcIp_Type=TruthValue
_QtechApProfIpv6SrcIp_Object=MibTableColumn
qtechApProfIpv6SrcIp=_QtechApProfIpv6SrcIp_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,15),_QtechApProfIpv6SrcIp_Type())
qtechApProfIpv6SrcIp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfIpv6SrcIp.setStatus(_A)
_QtechApProfIpv6DestIp_Type=TruthValue
_QtechApProfIpv6DestIp_Object=MibTableColumn
qtechApProfIpv6DestIp=_QtechApProfIpv6DestIp_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,16),_QtechApProfIpv6DestIp_Type())
qtechApProfIpv6DestIp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfIpv6DestIp.setStatus(_A)
_QtechApProfIpv6Pro_Type=TruthValue
_QtechApProfIpv6Pro_Object=MibTableColumn
qtechApProfIpv6Pro=_QtechApProfIpv6Pro_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,17),_QtechApProfIpv6Pro_Type())
qtechApProfIpv6Pro.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfIpv6Pro.setStatus(_A)
_QtechApProfIpv6L4SrcPort_Type=TruthValue
_QtechApProfIpv6L4SrcPort_Object=MibTableColumn
qtechApProfIpv6L4SrcPort=_QtechApProfIpv6L4SrcPort_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,18),_QtechApProfIpv6L4SrcPort_Type())
qtechApProfIpv6L4SrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfIpv6L4SrcPort.setStatus(_A)
_QtechApProfIpv6L4DestPort_Type=TruthValue
_QtechApProfIpv6L4DestPort_Object=MibTableColumn
qtechApProfIpv6L4DestPort=_QtechApProfIpv6L4DestPort_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,19),_QtechApProfIpv6L4DestPort_Type())
qtechApProfIpv6L4DestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfIpv6L4DestPort.setStatus(_A)
_QtechApProfIpv6Vlan_Type=TruthValue
_QtechApProfIpv6Vlan_Object=MibTableColumn
qtechApProfIpv6Vlan=_QtechApProfIpv6Vlan_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,20),_QtechApProfIpv6Vlan_Type())
qtechApProfIpv6Vlan.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfIpv6Vlan.setStatus(_A)
_QtechApProfIpv6SrcPort_Type=TruthValue
_QtechApProfIpv6SrcPort_Object=MibTableColumn
qtechApProfIpv6SrcPort=_QtechApProfIpv6SrcPort_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,21),_QtechApProfIpv6SrcPort_Type())
qtechApProfIpv6SrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfIpv6SrcPort.setStatus(_A)
_QtechApProfMplsTopLabel_Type=TruthValue
_QtechApProfMplsTopLabel_Object=MibTableColumn
qtechApProfMplsTopLabel=_QtechApProfMplsTopLabel_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,22),_QtechApProfMplsTopLabel_Type())
qtechApProfMplsTopLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfMplsTopLabel.setStatus(_A)
_QtechApProfMpls2ndLabel_Type=TruthValue
_QtechApProfMpls2ndLabel_Object=MibTableColumn
qtechApProfMpls2ndLabel=_QtechApProfMpls2ndLabel_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,23),_QtechApProfMpls2ndLabel_Type())
qtechApProfMpls2ndLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfMpls2ndLabel.setStatus(_A)
_QtechApProfMplsSrcIp_Type=TruthValue
_QtechApProfMplsSrcIp_Object=MibTableColumn
qtechApProfMplsSrcIp=_QtechApProfMplsSrcIp_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,24),_QtechApProfMplsSrcIp_Type())
qtechApProfMplsSrcIp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfMplsSrcIp.setStatus(_A)
_QtechApProfMplsDestIp_Type=TruthValue
_QtechApProfMplsDestIp_Object=MibTableColumn
qtechApProfMplsDestIp=_QtechApProfMplsDestIp_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,25),_QtechApProfMplsDestIp_Type())
qtechApProfMplsDestIp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfMplsDestIp.setStatus(_A)
_QtechApProfMplsVlan_Type=TruthValue
_QtechApProfMplsVlan_Object=MibTableColumn
qtechApProfMplsVlan=_QtechApProfMplsVlan_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,26),_QtechApProfMplsVlan_Type())
qtechApProfMplsVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfMplsVlan.setStatus(_A)
_QtechApProfMplsSrcPort_Type=TruthValue
_QtechApProfMplsSrcPort_Object=MibTableColumn
qtechApProfMplsSrcPort=_QtechApProfMplsSrcPort_Object((1,3,6,1,4,1,27514,1,1,10,2,7,1,9,1,27),_QtechApProfMplsSrcPort_Type())
qtechApProfMplsSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechApProfMplsSrcPort.setStatus(_A)
_QtechApMIBConformance_ObjectIdentity=ObjectIdentity
qtechApMIBConformance=_QtechApMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,7,2))
_QtechApMIBCompliances_ObjectIdentity=ObjectIdentity
qtechApMIBCompliances=_QtechApMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,7,2,1))
_QtechApMIBGroups_ObjectIdentity=ObjectIdentity
qtechApMIBGroups=_QtechApMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,7,2,2))
qtechApMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,7,2,2,1))
qtechApMIBGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_F),(_B,_O),(_B,_P),(_B,_Q),(_B,_G),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_H),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:qtechApMIBGroup.setStatus(_A)
qtechApMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,7,2,1,1))
qtechApMIBCompliance.setObjects((_B,_x))
if mibBuilder.loadTexts:qtechApMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechApMIB':qtechApMIB,'qtechApMIBObjects':qtechApMIBObjects,_L:qtechApMaxNumber,_M:qtechApCurrentNumber,'qtechApPortConfigTable':qtechApPortConfigTable,'qtechApPortConfigEntry':qtechApPortConfigEntry,_J:qtechApPortConfigPortIndex,_N:qtechApPortConfigApIndex,'qtechApTable':qtechApTable,'qtechApEntry':qtechApEntry,_F:qtechApIndex,_O:qtechApMemberAction,'qtechApPossibleMember':qtechApPossibleMember,_P:qtechApMaxPtNumber,_Q:qtechApFlowBalance,'qtechApConfigTable':qtechApConfigTable,'qtechApConfigEntry':qtechApConfigEntry,_G:qtechApConfigNumber,_R:qtechApConfigIndex,_S:qtechApConfigMaxPtNumber,_T:qtechApConfigCurrentPtNumber,_U:qtechApConfigPortMember,_V:qtechApConfigAction,'qtechApPortMemberTable':qtechApPortMemberTable,'qtechApPortMemberEntry':qtechApPortMemberEntry,_H:qtechApPortMemberPortIndex,_W:qtechApPortMemberApNumber,_X:qtechApPortMemberAction,'qtechApBalcProfName':qtechApBalcProfName,'qtechApProfTable':qtechApProfTable,'qtechApProfEntry':qtechApProfEntry,_K:qtechApProfIdx,'qtechApProfName':qtechApProfName,_Y:qtechApProfL2SrcMac,_Z:qtechApProfL2DestMac,_a:qtechApProfL2Pro,_b:qtechApProfL2Vlan,_c:qtechApProfL2SrcPort,_d:qtechApProfIpv4SrcIp,_e:qtechApProfIpv4DestIp,_f:qtechApProfIpv4Pro,_g:qtechApProfIpv4L4SrcPort,_h:qtechApProfIpv4L4DestPort,_i:qtechApProfIpv4Vlan,_j:qtechApProfIpv4SrcPort,_k:qtechApProfIpv6SrcIp,_l:qtechApProfIpv6DestIp,_m:qtechApProfIpv6Pro,_n:qtechApProfIpv6L4SrcPort,_o:qtechApProfIpv6L4DestPort,_p:qtechApProfIpv6Vlan,_q:qtechApProfIpv6SrcPort,_r:qtechApProfMplsTopLabel,_s:qtechApProfMpls2ndLabel,_t:qtechApProfMplsSrcIp,_u:qtechApProfMplsDestIp,_v:qtechApProfMplsVlan,_w:qtechApProfMplsSrcPort,'qtechApMIBConformance':qtechApMIBConformance,'qtechApMIBCompliances':qtechApMIBCompliances,'qtechApMIBCompliance':qtechApMIBCompliance,'qtechApMIBGroups':qtechApMIBGroups,_x:qtechApMIBGroup})