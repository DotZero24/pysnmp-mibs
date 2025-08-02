_AE='qtechClusterCandidateStatusGroup'
_AD='qtechClusterBlackListGroup'
_AC='qtechClusterMemberAddGroup'
_AB='qtechClusterCandidateGroup'
_AA='qtechClusterMemberGroup'
_A9='qtechClusterMemberStatusGroup'
_A8='qtechClusterStatusGroup'
_A7='qtechClusterDevicePassword'
_A6='qtechClusterPassword'
_A5='qtechClusterMemberAddRowStatus'
_A4='qtechClusterMemberAddMacAddress'
_A3='qtechClusterCandidateState'
_A2='qtechClusterCandidateUpSn'
_A1='qtechClusterCandidateHops'
_A0='qtechClusterCandidateUpPort'
_z='qtechClusterCandidateLcPort'
_y='qtechClusterMemberReload'
_x='qtechClusterMemberNoRecvUdpRspCount'
_w='qtechClusterMemberNoRecvTopoRspCount'
_v='qtechClusterMemberLastUdpUpdateTime'
_u='qtechClusterMemberLastTopoUpdateTime'
_t='qtechClusterMemberUpSn'
_s='qtechClusterMemberHops'
_r='qtechClusterMemberIp'
_q='qtechClusterMemberName'
_p='qtechClusterMemberUpPort'
_o='qtechClusterMemberLcPort'
_n='qtechClusterMemberMacAddress'
_m='qtechClusterDeviceSn'
_l='qtechClusterDeviceIP'
_k='qtechClusterDevMaxCapicity'
_j='qtechClusterMaxNumberOfMembers'
_i='qtechClusterNumberOfMembers'
_h='qtechClusterTftpServer'
_g='qtechClusterTimerHold'
_f='qtechClusterTimerHello'
_e='qtechClusterTimerTopo'
_d='qtechClusterVlan'
_c='qtechClusterCmdMacAddress'
_b='Unsigned32'
_a='qtechClusterMemberState'
_Z='qtechClusterDeviceRole'
_Y='qtechClusterDeviceEnable'
_X='qtechClusterHopsLimit'
_W='qtechClusterDeviceMacAddress'
_V='qtechClusterPasswordSn'
_U='qtechClusterBlacklistMacAddress'
_T='qtechClusterCandidateUpIfx'
_S='qtechClusterCandidateLcIfx'
_R='qtechClusterCandidateUpMAC'
_Q='qtechClusterMemberUpIfx'
_P='qtechClusterMemberLcIfx'
_O='qtechClusterMemberUpMAC'
_N='qtechClusterMemberAddSn'
_M='qtechClusterIpMask'
_L='qtechClusterIpPool'
_K='qtechClusterName'
_J='qtechClusterCandidateMacAddress'
_I='qtechClusterMemberSn'
_H='EnabledStatus'
_G='DisplayString'
_F='read-create'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='QTECH-CLUSTER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_H)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_b,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp')
qtechClusterMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,31))
if mibBuilder.loadTexts:qtechClusterMIB.setRevisions(('2012-07-01 00:00',))
_QtechClusterMIBObjects_ObjectIdentity=ObjectIdentity
qtechClusterMIBObjects=_QtechClusterMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,31,1))
class _QtechClusterName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QtechClusterName_Type.__name__=_G
_QtechClusterName_Object=MibScalar
qtechClusterName=_QtechClusterName_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,1),_QtechClusterName_Type())
qtechClusterName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechClusterName.setStatus(_A)
class _QtechClusterStatus_Type(EnabledStatus):defaultValue=1
_QtechClusterStatus_Type.__name__=_H
_QtechClusterStatus_Object=MibScalar
qtechClusterStatus=_QtechClusterStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,2),_QtechClusterStatus_Type())
qtechClusterStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechClusterStatus.setStatus(_A)
_QtechClusterCmdMacAddress_Type=MacAddress
_QtechClusterCmdMacAddress_Object=MibScalar
qtechClusterCmdMacAddress=_QtechClusterCmdMacAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,3),_QtechClusterCmdMacAddress_Type())
qtechClusterCmdMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterCmdMacAddress.setStatus(_A)
_QtechClusterCmdName_Type=DisplayString
_QtechClusterCmdName_Object=MibScalar
qtechClusterCmdName=_QtechClusterCmdName_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,4),_QtechClusterCmdName_Type())
qtechClusterCmdName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterCmdName.setStatus(_A)
class _QtechClusterVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_QtechClusterVlan_Type.__name__=_E
_QtechClusterVlan_Object=MibScalar
qtechClusterVlan=_QtechClusterVlan_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,5),_QtechClusterVlan_Type())
qtechClusterVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechClusterVlan.setStatus(_A)
class _QtechClusterHopsLimit_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_QtechClusterHopsLimit_Type.__name__=_E
_QtechClusterHopsLimit_Object=MibScalar
qtechClusterHopsLimit=_QtechClusterHopsLimit_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,6),_QtechClusterHopsLimit_Type())
qtechClusterHopsLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechClusterHopsLimit.setStatus(_A)
class _QtechClusterTimerTopo_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_QtechClusterTimerTopo_Type.__name__=_E
_QtechClusterTimerTopo_Object=MibScalar
qtechClusterTimerTopo=_QtechClusterTimerTopo_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,7),_QtechClusterTimerTopo_Type())
qtechClusterTimerTopo.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechClusterTimerTopo.setStatus(_A)
class _QtechClusterTimerHello_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_QtechClusterTimerHello_Type.__name__=_E
_QtechClusterTimerHello_Object=MibScalar
qtechClusterTimerHello=_QtechClusterTimerHello_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,8),_QtechClusterTimerHello_Type())
qtechClusterTimerHello.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechClusterTimerHello.setStatus(_A)
class _QtechClusterTimerHold_Type(Integer32):defaultValue=90;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_QtechClusterTimerHold_Type.__name__=_E
_QtechClusterTimerHold_Object=MibScalar
qtechClusterTimerHold=_QtechClusterTimerHold_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,9),_QtechClusterTimerHold_Type())
qtechClusterTimerHold.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechClusterTimerHold.setStatus(_A)
_QtechClusterTftpServer_Type=IpAddress
_QtechClusterTftpServer_Object=MibScalar
qtechClusterTftpServer=_QtechClusterTftpServer_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,10),_QtechClusterTftpServer_Type())
qtechClusterTftpServer.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechClusterTftpServer.setStatus(_A)
class _QtechClusterNumberOfMembers_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_QtechClusterNumberOfMembers_Type.__name__=_E
_QtechClusterNumberOfMembers_Object=MibScalar
qtechClusterNumberOfMembers=_QtechClusterNumberOfMembers_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,11),_QtechClusterNumberOfMembers_Type())
qtechClusterNumberOfMembers.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterNumberOfMembers.setStatus(_A)
class _QtechClusterMaxNumberOfMembers_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_QtechClusterMaxNumberOfMembers_Type.__name__=_E
_QtechClusterMaxNumberOfMembers_Object=MibScalar
qtechClusterMaxNumberOfMembers=_QtechClusterMaxNumberOfMembers_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,12),_QtechClusterMaxNumberOfMembers_Type())
qtechClusterMaxNumberOfMembers.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterMaxNumberOfMembers.setStatus(_A)
class _QtechClusterDevMaxCapicity_Type(Unsigned32):defaultValue=0
_QtechClusterDevMaxCapicity_Type.__name__=_b
_QtechClusterDevMaxCapicity_Object=MibScalar
qtechClusterDevMaxCapicity=_QtechClusterDevMaxCapicity_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,13),_QtechClusterDevMaxCapicity_Type())
qtechClusterDevMaxCapicity.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterDevMaxCapicity.setStatus(_A)
class _QtechClusterAutoAdd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('disable-with-def',0),('enable',1),('disabled-with-static',2),('disabled-with-del',3)))
_QtechClusterAutoAdd_Type.__name__=_E
_QtechClusterAutoAdd_Object=MibScalar
qtechClusterAutoAdd=_QtechClusterAutoAdd_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,14),_QtechClusterAutoAdd_Type())
qtechClusterAutoAdd.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechClusterAutoAdd.setStatus(_A)
class _QtechClusterExplore_Type(EnabledStatus):defaultValue=2
_QtechClusterExplore_Type.__name__=_H
_QtechClusterExplore_Object=MibScalar
qtechClusterExplore=_QtechClusterExplore_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,15),_QtechClusterExplore_Type())
qtechClusterExplore.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechClusterExplore.setStatus(_A)
_QtechClusterSpecifyAdmin_ObjectIdentity=ObjectIdentity
qtechClusterSpecifyAdmin=_QtechClusterSpecifyAdmin_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,31,1,16))
_QtechClusterSpecifyAdminAddress_Type=MacAddress
_QtechClusterSpecifyAdminAddress_Object=MibScalar
qtechClusterSpecifyAdminAddress=_QtechClusterSpecifyAdminAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,16,1),_QtechClusterSpecifyAdminAddress_Type())
qtechClusterSpecifyAdminAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechClusterSpecifyAdminAddress.setStatus(_A)
class _QtechClusterSpecifyAdminName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_QtechClusterSpecifyAdminName_Type.__name__=_G
_QtechClusterSpecifyAdminName_Object=MibScalar
qtechClusterSpecifyAdminName=_QtechClusterSpecifyAdminName_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,16,2),_QtechClusterSpecifyAdminName_Type())
qtechClusterSpecifyAdminName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechClusterSpecifyAdminName.setStatus(_A)
_QtechClusterDeviceInfo_ObjectIdentity=ObjectIdentity
qtechClusterDeviceInfo=_QtechClusterDeviceInfo_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,31,1,17))
class _QtechClusterDeviceEnable_Type(EnabledStatus):defaultValue=1
_QtechClusterDeviceEnable_Type.__name__=_H
_QtechClusterDeviceEnable_Object=MibScalar
qtechClusterDeviceEnable=_QtechClusterDeviceEnable_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,17,1),_QtechClusterDeviceEnable_Type())
qtechClusterDeviceEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechClusterDeviceEnable.setStatus(_A)
class _QtechClusterDeviceRole_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('candidateDevice',1),('managerDevice',2),('memberDevice',3)))
_QtechClusterDeviceRole_Type.__name__=_E
_QtechClusterDeviceRole_Object=MibScalar
qtechClusterDeviceRole=_QtechClusterDeviceRole_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,17,2),_QtechClusterDeviceRole_Type())
qtechClusterDeviceRole.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterDeviceRole.setStatus(_A)
_QtechClusterDeviceIP_Type=IpAddress
_QtechClusterDeviceIP_Object=MibScalar
qtechClusterDeviceIP=_QtechClusterDeviceIP_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,17,3),_QtechClusterDeviceIP_Type())
qtechClusterDeviceIP.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterDeviceIP.setStatus(_A)
class _QtechClusterDeviceSn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,240))
_QtechClusterDeviceSn_Type.__name__=_E
_QtechClusterDeviceSn_Object=MibScalar
qtechClusterDeviceSn=_QtechClusterDeviceSn_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,17,4),_QtechClusterDeviceSn_Type())
qtechClusterDeviceSn.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterDeviceSn.setStatus(_A)
_QtechClusterIpPoolTable_Object=MibTable
qtechClusterIpPoolTable=_QtechClusterIpPoolTable_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,18))
if mibBuilder.loadTexts:qtechClusterIpPoolTable.setStatus(_A)
_QtechClusterIpPoolEntry_Object=MibTableRow
qtechClusterIpPoolEntry=_QtechClusterIpPoolEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,18,1))
qtechClusterIpPoolEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:qtechClusterIpPoolEntry.setStatus(_A)
_QtechClusterIpPool_Type=IpAddress
_QtechClusterIpPool_Object=MibTableColumn
qtechClusterIpPool=_QtechClusterIpPool_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,18,1,1),_QtechClusterIpPool_Type())
qtechClusterIpPool.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterIpPool.setStatus(_A)
_QtechClusterIpMask_Type=IpAddress
_QtechClusterIpMask_Object=MibTableColumn
qtechClusterIpMask=_QtechClusterIpMask_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,18,1,2),_QtechClusterIpMask_Type())
qtechClusterIpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterIpMask.setStatus(_A)
_QtechClusterIpPoolRowStatus_Type=RowStatus
_QtechClusterIpPoolRowStatus_Object=MibTableColumn
qtechClusterIpPoolRowStatus=_QtechClusterIpPoolRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,18,1,3),_QtechClusterIpPoolRowStatus_Type())
qtechClusterIpPoolRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechClusterIpPoolRowStatus.setStatus(_A)
_QtechClusterMemberAddTable_Object=MibTable
qtechClusterMemberAddTable=_QtechClusterMemberAddTable_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,19))
if mibBuilder.loadTexts:qtechClusterMemberAddTable.setStatus(_A)
_QtechClusterMemberAddEntry_Object=MibTableRow
qtechClusterMemberAddEntry=_QtechClusterMemberAddEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,19,1))
qtechClusterMemberAddEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:qtechClusterMemberAddEntry.setStatus(_A)
class _QtechClusterMemberAddSn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_QtechClusterMemberAddSn_Type.__name__=_E
_QtechClusterMemberAddSn_Object=MibTableColumn
qtechClusterMemberAddSn=_QtechClusterMemberAddSn_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,19,1,1),_QtechClusterMemberAddSn_Type())
qtechClusterMemberAddSn.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterMemberAddSn.setStatus(_A)
_QtechClusterMemberAddMacAddress_Type=MacAddress
_QtechClusterMemberAddMacAddress_Object=MibTableColumn
qtechClusterMemberAddMacAddress=_QtechClusterMemberAddMacAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,19,1,2),_QtechClusterMemberAddMacAddress_Type())
qtechClusterMemberAddMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechClusterMemberAddMacAddress.setStatus(_A)
_QtechClusterMemberAddRowStatus_Type=RowStatus
_QtechClusterMemberAddRowStatus_Object=MibTableColumn
qtechClusterMemberAddRowStatus=_QtechClusterMemberAddRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,19,1,3),_QtechClusterMemberAddRowStatus_Type())
qtechClusterMemberAddRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechClusterMemberAddRowStatus.setStatus(_A)
_QtechClusterMemberTable_Object=MibTable
qtechClusterMemberTable=_QtechClusterMemberTable_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,20))
if mibBuilder.loadTexts:qtechClusterMemberTable.setStatus(_A)
_QtechClusterMemberEntry_Object=MibTableRow
qtechClusterMemberEntry=_QtechClusterMemberEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,20,1))
qtechClusterMemberEntry.setIndexNames((0,_B,_I),(0,_B,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:qtechClusterMemberEntry.setStatus(_A)
_QtechClusterMemberSn_Type=Unsigned32
_QtechClusterMemberSn_Object=MibTableColumn
qtechClusterMemberSn=_QtechClusterMemberSn_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,20,1,1),_QtechClusterMemberSn_Type())
qtechClusterMemberSn.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterMemberSn.setStatus(_A)
_QtechClusterMemberUpMAC_Type=MacAddress
_QtechClusterMemberUpMAC_Object=MibTableColumn
qtechClusterMemberUpMAC=_QtechClusterMemberUpMAC_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,20,1,2),_QtechClusterMemberUpMAC_Type())
qtechClusterMemberUpMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterMemberUpMAC.setStatus(_A)
_QtechClusterMemberLcIfx_Type=Unsigned32
_QtechClusterMemberLcIfx_Object=MibTableColumn
qtechClusterMemberLcIfx=_QtechClusterMemberLcIfx_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,20,1,3),_QtechClusterMemberLcIfx_Type())
qtechClusterMemberLcIfx.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterMemberLcIfx.setStatus(_A)
_QtechClusterMemberUpIfx_Type=Unsigned32
_QtechClusterMemberUpIfx_Object=MibTableColumn
qtechClusterMemberUpIfx=_QtechClusterMemberUpIfx_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,20,1,4),_QtechClusterMemberUpIfx_Type())
qtechClusterMemberUpIfx.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterMemberUpIfx.setStatus(_A)
_QtechClusterMemberLcPort_Type=DisplayString
_QtechClusterMemberLcPort_Object=MibTableColumn
qtechClusterMemberLcPort=_QtechClusterMemberLcPort_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,20,1,5),_QtechClusterMemberLcPort_Type())
qtechClusterMemberLcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterMemberLcPort.setStatus(_A)
_QtechClusterMemberUpPort_Type=DisplayString
_QtechClusterMemberUpPort_Object=MibTableColumn
qtechClusterMemberUpPort=_QtechClusterMemberUpPort_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,20,1,6),_QtechClusterMemberUpPort_Type())
qtechClusterMemberUpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterMemberUpPort.setStatus(_A)
_QtechClusterMemberMacAddress_Type=MacAddress
_QtechClusterMemberMacAddress_Object=MibTableColumn
qtechClusterMemberMacAddress=_QtechClusterMemberMacAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,20,1,7),_QtechClusterMemberMacAddress_Type())
qtechClusterMemberMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterMemberMacAddress.setStatus(_A)
_QtechClusterMemberName_Type=DisplayString
_QtechClusterMemberName_Object=MibTableColumn
qtechClusterMemberName=_QtechClusterMemberName_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,20,1,8),_QtechClusterMemberName_Type())
qtechClusterMemberName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterMemberName.setStatus(_A)
_QtechClusterMemberIp_Type=IpAddress
_QtechClusterMemberIp_Object=MibTableColumn
qtechClusterMemberIp=_QtechClusterMemberIp_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,20,1,9),_QtechClusterMemberIp_Type())
qtechClusterMemberIp.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterMemberIp.setStatus(_A)
_QtechClusterMemberHops_Type=Unsigned32
_QtechClusterMemberHops_Object=MibTableColumn
qtechClusterMemberHops=_QtechClusterMemberHops_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,20,1,10),_QtechClusterMemberHops_Type())
qtechClusterMemberHops.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterMemberHops.setStatus(_A)
_QtechClusterMemberState_Type=DisplayString
_QtechClusterMemberState_Object=MibTableColumn
qtechClusterMemberState=_QtechClusterMemberState_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,20,1,11),_QtechClusterMemberState_Type())
qtechClusterMemberState.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterMemberState.setStatus(_A)
_QtechClusterMemberUpSn_Type=Unsigned32
_QtechClusterMemberUpSn_Object=MibTableColumn
qtechClusterMemberUpSn=_QtechClusterMemberUpSn_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,20,1,12),_QtechClusterMemberUpSn_Type())
qtechClusterMemberUpSn.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterMemberUpSn.setStatus(_A)
_QtechClusterMemberLastTopoUpdateTime_Type=Unsigned32
_QtechClusterMemberLastTopoUpdateTime_Object=MibTableColumn
qtechClusterMemberLastTopoUpdateTime=_QtechClusterMemberLastTopoUpdateTime_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,20,1,13),_QtechClusterMemberLastTopoUpdateTime_Type())
qtechClusterMemberLastTopoUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterMemberLastTopoUpdateTime.setStatus(_A)
_QtechClusterMemberLastUdpUpdateTime_Type=Unsigned32
_QtechClusterMemberLastUdpUpdateTime_Object=MibTableColumn
qtechClusterMemberLastUdpUpdateTime=_QtechClusterMemberLastUdpUpdateTime_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,20,1,14),_QtechClusterMemberLastUdpUpdateTime_Type())
qtechClusterMemberLastUdpUpdateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterMemberLastUdpUpdateTime.setStatus(_A)
_QtechClusterMemberNoRecvTopoRspCount_Type=Unsigned32
_QtechClusterMemberNoRecvTopoRspCount_Object=MibTableColumn
qtechClusterMemberNoRecvTopoRspCount=_QtechClusterMemberNoRecvTopoRspCount_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,20,1,15),_QtechClusterMemberNoRecvTopoRspCount_Type())
qtechClusterMemberNoRecvTopoRspCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterMemberNoRecvTopoRspCount.setStatus(_A)
_QtechClusterMemberNoRecvUdpRspCount_Type=Unsigned32
_QtechClusterMemberNoRecvUdpRspCount_Object=MibTableColumn
qtechClusterMemberNoRecvUdpRspCount=_QtechClusterMemberNoRecvUdpRspCount_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,20,1,16),_QtechClusterMemberNoRecvUdpRspCount_Type())
qtechClusterMemberNoRecvUdpRspCount.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterMemberNoRecvUdpRspCount.setStatus(_A)
_QtechClusterMemberReload_Type=EnabledStatus
_QtechClusterMemberReload_Object=MibTableColumn
qtechClusterMemberReload=_QtechClusterMemberReload_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,20,1,17),_QtechClusterMemberReload_Type())
qtechClusterMemberReload.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechClusterMemberReload.setStatus(_A)
_QtechClusterCandidateTable_Object=MibTable
qtechClusterCandidateTable=_QtechClusterCandidateTable_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,21))
if mibBuilder.loadTexts:qtechClusterCandidateTable.setStatus(_A)
_QtechClusterCandidateEntry_Object=MibTableRow
qtechClusterCandidateEntry=_QtechClusterCandidateEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,21,1))
qtechClusterCandidateEntry.setIndexNames((0,_B,_J),(0,_B,_R),(0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:qtechClusterCandidateEntry.setStatus(_A)
_QtechClusterCandidateMacAddress_Type=MacAddress
_QtechClusterCandidateMacAddress_Object=MibTableColumn
qtechClusterCandidateMacAddress=_QtechClusterCandidateMacAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,21,1,1),_QtechClusterCandidateMacAddress_Type())
qtechClusterCandidateMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterCandidateMacAddress.setStatus(_A)
_QtechClusterCandidateUpMAC_Type=MacAddress
_QtechClusterCandidateUpMAC_Object=MibTableColumn
qtechClusterCandidateUpMAC=_QtechClusterCandidateUpMAC_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,21,1,2),_QtechClusterCandidateUpMAC_Type())
qtechClusterCandidateUpMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterCandidateUpMAC.setStatus(_A)
_QtechClusterCandidateLcIfx_Type=Unsigned32
_QtechClusterCandidateLcIfx_Object=MibTableColumn
qtechClusterCandidateLcIfx=_QtechClusterCandidateLcIfx_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,21,1,3),_QtechClusterCandidateLcIfx_Type())
qtechClusterCandidateLcIfx.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterCandidateLcIfx.setStatus(_A)
_QtechClusterCandidateUpIfx_Type=Unsigned32
_QtechClusterCandidateUpIfx_Object=MibTableColumn
qtechClusterCandidateUpIfx=_QtechClusterCandidateUpIfx_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,21,1,4),_QtechClusterCandidateUpIfx_Type())
qtechClusterCandidateUpIfx.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterCandidateUpIfx.setStatus(_A)
_QtechClusterCandidateLcPort_Type=DisplayString
_QtechClusterCandidateLcPort_Object=MibTableColumn
qtechClusterCandidateLcPort=_QtechClusterCandidateLcPort_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,21,1,5),_QtechClusterCandidateLcPort_Type())
qtechClusterCandidateLcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterCandidateLcPort.setStatus(_A)
_QtechClusterCandidateUpPort_Type=DisplayString
_QtechClusterCandidateUpPort_Object=MibTableColumn
qtechClusterCandidateUpPort=_QtechClusterCandidateUpPort_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,21,1,6),_QtechClusterCandidateUpPort_Type())
qtechClusterCandidateUpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterCandidateUpPort.setStatus(_A)
_QtechClusterCandidateUpSn_Type=Unsigned32
_QtechClusterCandidateUpSn_Object=MibTableColumn
qtechClusterCandidateUpSn=_QtechClusterCandidateUpSn_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,21,1,7),_QtechClusterCandidateUpSn_Type())
qtechClusterCandidateUpSn.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterCandidateUpSn.setStatus(_A)
_QtechClusterCandidateHops_Type=Unsigned32
_QtechClusterCandidateHops_Object=MibTableColumn
qtechClusterCandidateHops=_QtechClusterCandidateHops_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,21,1,8),_QtechClusterCandidateHops_Type())
qtechClusterCandidateHops.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterCandidateHops.setStatus(_A)
_QtechClusterCandidateState_Type=DisplayString
_QtechClusterCandidateState_Object=MibTableColumn
qtechClusterCandidateState=_QtechClusterCandidateState_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,21,1,9),_QtechClusterCandidateState_Type())
qtechClusterCandidateState.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterCandidateState.setStatus(_A)
_QtechClusterBlacklistTable_Object=MibTable
qtechClusterBlacklistTable=_QtechClusterBlacklistTable_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,22))
if mibBuilder.loadTexts:qtechClusterBlacklistTable.setStatus(_A)
_QtechClusterBlacklistEntry_Object=MibTableRow
qtechClusterBlacklistEntry=_QtechClusterBlacklistEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,22,1))
qtechClusterBlacklistEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:qtechClusterBlacklistEntry.setStatus(_A)
_QtechClusterBlacklistMacAddress_Type=MacAddress
_QtechClusterBlacklistMacAddress_Object=MibTableColumn
qtechClusterBlacklistMacAddress=_QtechClusterBlacklistMacAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,22,1,1),_QtechClusterBlacklistMacAddress_Type())
qtechClusterBlacklistMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterBlacklistMacAddress.setStatus(_A)
_QtechClusterBlackListRowStatus_Type=RowStatus
_QtechClusterBlackListRowStatus_Object=MibTableColumn
qtechClusterBlackListRowStatus=_QtechClusterBlackListRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,22,1,2),_QtechClusterBlackListRowStatus_Type())
qtechClusterBlackListRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechClusterBlackListRowStatus.setStatus(_A)
_QtechClusterPasswordAuth_ObjectIdentity=ObjectIdentity
qtechClusterPasswordAuth=_QtechClusterPasswordAuth_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,31,1,23))
_QtechClusterPasswordAuthPoolTable_Object=MibTable
qtechClusterPasswordAuthPoolTable=_QtechClusterPasswordAuthPoolTable_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,23,1))
if mibBuilder.loadTexts:qtechClusterPasswordAuthPoolTable.setStatus(_A)
_QtechClusterPasswordAuthPoolEntry_Object=MibTableRow
qtechClusterPasswordAuthPoolEntry=_QtechClusterPasswordAuthPoolEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,23,1,1))
qtechClusterPasswordAuthPoolEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:qtechClusterPasswordAuthPoolEntry.setStatus(_A)
class _QtechClusterPasswordSn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_QtechClusterPasswordSn_Type.__name__=_E
_QtechClusterPasswordSn_Object=MibTableColumn
qtechClusterPasswordSn=_QtechClusterPasswordSn_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,23,1,1,1),_QtechClusterPasswordSn_Type())
qtechClusterPasswordSn.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterPasswordSn.setStatus(_A)
class _QtechClusterPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,126))
_QtechClusterPassword_Type.__name__=_G
_QtechClusterPassword_Object=MibTableColumn
qtechClusterPassword=_QtechClusterPassword_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,23,1,1,2),_QtechClusterPassword_Type())
qtechClusterPassword.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechClusterPassword.setStatus(_A)
_QtechClusterPasswordAuthRowStatus_Type=RowStatus
_QtechClusterPasswordAuthRowStatus_Object=MibTableColumn
qtechClusterPasswordAuthRowStatus=_QtechClusterPasswordAuthRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,23,1,1,3),_QtechClusterPasswordAuthRowStatus_Type())
qtechClusterPasswordAuthRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechClusterPasswordAuthRowStatus.setStatus(_A)
_QtechClusterDeviceAuthPasswordTable_Object=MibTable
qtechClusterDeviceAuthPasswordTable=_QtechClusterDeviceAuthPasswordTable_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,23,2))
if mibBuilder.loadTexts:qtechClusterDeviceAuthPasswordTable.setStatus(_A)
_QtechClusterDeviceAuthPasswordEntry_Object=MibTableRow
qtechClusterDeviceAuthPasswordEntry=_QtechClusterDeviceAuthPasswordEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,23,2,1))
qtechClusterDeviceAuthPasswordEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:qtechClusterDeviceAuthPasswordEntry.setStatus(_A)
_QtechClusterDeviceMacAddress_Type=MacAddress
_QtechClusterDeviceMacAddress_Object=MibTableColumn
qtechClusterDeviceMacAddress=_QtechClusterDeviceMacAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,23,2,1,1),_QtechClusterDeviceMacAddress_Type())
qtechClusterDeviceMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechClusterDeviceMacAddress.setStatus(_A)
class _QtechClusterDevicePassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,126))
_QtechClusterDevicePassword_Type.__name__=_G
_QtechClusterDevicePassword_Object=MibTableColumn
qtechClusterDevicePassword=_QtechClusterDevicePassword_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,23,2,1,2),_QtechClusterDevicePassword_Type())
qtechClusterDevicePassword.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechClusterDevicePassword.setStatus(_A)
_QtechClusterDevicePasswordRowStatus_Type=RowStatus
_QtechClusterDevicePasswordRowStatus_Object=MibTableColumn
qtechClusterDevicePasswordRowStatus=_QtechClusterDevicePasswordRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,31,1,23,2,1,3),_QtechClusterDevicePasswordRowStatus_Type())
qtechClusterDevicePasswordRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechClusterDevicePasswordRowStatus.setStatus(_A)
_QtechClusterTraps_ObjectIdentity=ObjectIdentity
qtechClusterTraps=_QtechClusterTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,31,2))
_QtechClusterMIBConformance_ObjectIdentity=ObjectIdentity
qtechClusterMIBConformance=_QtechClusterMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,31,3))
_QtechClusterMIBCompliances_ObjectIdentity=ObjectIdentity
qtechClusterMIBCompliances=_QtechClusterMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,31,3,1))
_QtechClusterMIBGroups_ObjectIdentity=ObjectIdentity
qtechClusterMIBGroups=_QtechClusterMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,31,3,2))
qtechClusterStatusGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,31,3,2,1))
qtechClusterStatusGroup.setObjects(*((_B,_K),(_B,_c),(_B,_L),(_B,_M),(_B,_d),(_B,_X),(_B,_X),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:qtechClusterStatusGroup.setStatus(_A)
qtechClusterMemberStatusGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,31,3,2,2))
qtechClusterMemberStatusGroup.setObjects(*((_B,_K),(_B,_Y),(_B,_Z),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:qtechClusterMemberStatusGroup.setStatus(_A)
qtechClusterCandidateStatusGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,31,3,2,3))
qtechClusterCandidateStatusGroup.setObjects(*((_B,_K),(_B,_Z),(_B,_Y)))
if mibBuilder.loadTexts:qtechClusterCandidateStatusGroup.setStatus(_A)
qtechClusterMemberGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,31,3,2,4))
qtechClusterMemberGroup.setObjects(*((_B,_I),(_B,_n),(_B,_P),(_B,_Q),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_a),(_B,_t),(_B,_O),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:qtechClusterMemberGroup.setStatus(_A)
qtechClusterCandidateGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,31,3,2,5))
qtechClusterCandidateGroup.setObjects(*((_B,_J),(_B,_R),(_B,_S),(_B,_T),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:qtechClusterCandidateGroup.setStatus(_A)
qtechClusterMemberAddGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,31,3,2,6))
qtechClusterMemberAddGroup.setObjects(*((_B,_A4),(_B,_N),(_B,_A5)))
if mibBuilder.loadTexts:qtechClusterMemberAddGroup.setStatus(_A)
qtechClusterBlackListGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,31,3,2,7))
qtechClusterBlackListGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:qtechClusterBlackListGroup.setStatus(_A)
qtechClusterPasswordAuthPoolGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,31,3,2,8))
qtechClusterPasswordAuthPoolGroup.setObjects(*((_B,_V),(_B,_A6)))
if mibBuilder.loadTexts:qtechClusterPasswordAuthPoolGroup.setStatus(_A)
qtechClsuterDeviceAuthPasswordGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,31,3,2,9))
qtechClsuterDeviceAuthPasswordGroup.setObjects(*((_B,_W),(_B,_A7)))
if mibBuilder.loadTexts:qtechClsuterDeviceAuthPasswordGroup.setStatus(_A)
qtechClusterMemberStateChangeTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,31,2,1))
qtechClusterMemberStateChangeTrap.setObjects(*((_B,_I),(_B,_a)))
if mibBuilder.loadTexts:qtechClusterMemberStateChangeTrap.setStatus(_A)
qtechClusterMemberFailureTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,31,2,2))
qtechClusterMemberFailureTrap.setObjects((_B,_J))
if mibBuilder.loadTexts:qtechClusterMemberFailureTrap.setStatus(_A)
qtechClusterDevMaximumAllowedTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,31,2,3))
if mibBuilder.loadTexts:qtechClusterDevMaximumAllowedTrap.setStatus(_A)
qtechClusterMemberMaximumAllowedTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,31,2,4))
if mibBuilder.loadTexts:qtechClusterMemberMaximumAllowedTrap.setStatus(_A)
qtechClusterCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,31,3,1,1))
qtechClusterCompliance.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,'uijieClusterPasswordAuthPoolGroup'),(_B,'qtechDeviceAuthPasswordGroup'),(_B,_AE)))
if mibBuilder.loadTexts:qtechClusterCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechClusterMIB':qtechClusterMIB,'qtechClusterMIBObjects':qtechClusterMIBObjects,_K:qtechClusterName,'qtechClusterStatus':qtechClusterStatus,_c:qtechClusterCmdMacAddress,'qtechClusterCmdName':qtechClusterCmdName,_d:qtechClusterVlan,_X:qtechClusterHopsLimit,_e:qtechClusterTimerTopo,_f:qtechClusterTimerHello,_g:qtechClusterTimerHold,_h:qtechClusterTftpServer,_i:qtechClusterNumberOfMembers,_j:qtechClusterMaxNumberOfMembers,_k:qtechClusterDevMaxCapicity,'qtechClusterAutoAdd':qtechClusterAutoAdd,'qtechClusterExplore':qtechClusterExplore,'qtechClusterSpecifyAdmin':qtechClusterSpecifyAdmin,'qtechClusterSpecifyAdminAddress':qtechClusterSpecifyAdminAddress,'qtechClusterSpecifyAdminName':qtechClusterSpecifyAdminName,'qtechClusterDeviceInfo':qtechClusterDeviceInfo,_Y:qtechClusterDeviceEnable,_Z:qtechClusterDeviceRole,_l:qtechClusterDeviceIP,_m:qtechClusterDeviceSn,'qtechClusterIpPoolTable':qtechClusterIpPoolTable,'qtechClusterIpPoolEntry':qtechClusterIpPoolEntry,_L:qtechClusterIpPool,_M:qtechClusterIpMask,'qtechClusterIpPoolRowStatus':qtechClusterIpPoolRowStatus,'qtechClusterMemberAddTable':qtechClusterMemberAddTable,'qtechClusterMemberAddEntry':qtechClusterMemberAddEntry,_N:qtechClusterMemberAddSn,_A4:qtechClusterMemberAddMacAddress,_A5:qtechClusterMemberAddRowStatus,'qtechClusterMemberTable':qtechClusterMemberTable,'qtechClusterMemberEntry':qtechClusterMemberEntry,_I:qtechClusterMemberSn,_O:qtechClusterMemberUpMAC,_P:qtechClusterMemberLcIfx,_Q:qtechClusterMemberUpIfx,_o:qtechClusterMemberLcPort,_p:qtechClusterMemberUpPort,_n:qtechClusterMemberMacAddress,_q:qtechClusterMemberName,_r:qtechClusterMemberIp,_s:qtechClusterMemberHops,_a:qtechClusterMemberState,_t:qtechClusterMemberUpSn,_u:qtechClusterMemberLastTopoUpdateTime,_v:qtechClusterMemberLastUdpUpdateTime,_w:qtechClusterMemberNoRecvTopoRspCount,_x:qtechClusterMemberNoRecvUdpRspCount,_y:qtechClusterMemberReload,'qtechClusterCandidateTable':qtechClusterCandidateTable,'qtechClusterCandidateEntry':qtechClusterCandidateEntry,_J:qtechClusterCandidateMacAddress,_R:qtechClusterCandidateUpMAC,_S:qtechClusterCandidateLcIfx,_T:qtechClusterCandidateUpIfx,_z:qtechClusterCandidateLcPort,_A0:qtechClusterCandidateUpPort,_A2:qtechClusterCandidateUpSn,_A1:qtechClusterCandidateHops,_A3:qtechClusterCandidateState,'qtechClusterBlacklistTable':qtechClusterBlacklistTable,'qtechClusterBlacklistEntry':qtechClusterBlacklistEntry,_U:qtechClusterBlacklistMacAddress,'qtechClusterBlackListRowStatus':qtechClusterBlackListRowStatus,'qtechClusterPasswordAuth':qtechClusterPasswordAuth,'qtechClusterPasswordAuthPoolTable':qtechClusterPasswordAuthPoolTable,'qtechClusterPasswordAuthPoolEntry':qtechClusterPasswordAuthPoolEntry,_V:qtechClusterPasswordSn,_A6:qtechClusterPassword,'qtechClusterPasswordAuthRowStatus':qtechClusterPasswordAuthRowStatus,'qtechClusterDeviceAuthPasswordTable':qtechClusterDeviceAuthPasswordTable,'qtechClusterDeviceAuthPasswordEntry':qtechClusterDeviceAuthPasswordEntry,_W:qtechClusterDeviceMacAddress,_A7:qtechClusterDevicePassword,'qtechClusterDevicePasswordRowStatus':qtechClusterDevicePasswordRowStatus,'qtechClusterTraps':qtechClusterTraps,'qtechClusterMemberStateChangeTrap':qtechClusterMemberStateChangeTrap,'qtechClusterMemberFailureTrap':qtechClusterMemberFailureTrap,'qtechClusterDevMaximumAllowedTrap':qtechClusterDevMaximumAllowedTrap,'qtechClusterMemberMaximumAllowedTrap':qtechClusterMemberMaximumAllowedTrap,'qtechClusterMIBConformance':qtechClusterMIBConformance,'qtechClusterMIBCompliances':qtechClusterMIBCompliances,'qtechClusterCompliance':qtechClusterCompliance,'qtechClusterMIBGroups':qtechClusterMIBGroups,_A8:qtechClusterStatusGroup,_A9:qtechClusterMemberStatusGroup,_AE:qtechClusterCandidateStatusGroup,_AA:qtechClusterMemberGroup,_AB:qtechClusterCandidateGroup,_AC:qtechClusterMemberAddGroup,_AD:qtechClusterBlackListGroup,'qtechClusterPasswordAuthPoolGroup':qtechClusterPasswordAuthPoolGroup,'qtechClsuterDeviceAuthPasswordGroup':qtechClsuterDeviceAuthPasswordGroup})