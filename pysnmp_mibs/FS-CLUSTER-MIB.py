_X='fsClusterMemberState'
_W='fsClusterDeviceMacAddress'
_V='fsClusterPasswordSn'
_U='fsClusterBlacklistMacAddress'
_T='fsClusterCandidateUpIfx'
_S='fsClusterCandidateLcIfx'
_R='fsClusterCandidateUpMAC'
_Q='fsClusterMemberUpIfx'
_P='fsClusterMemberLcIfx'
_O='fsClusterMemberUpMAC'
_N='fsClusterMemberAddSn'
_M='fsClusterIpMask'
_L='fsClusterIpPool'
_K='Unsigned32'
_J='fsClusterCandidateMacAddress'
_I='fsClusterMemberSn'
_H='EnabledStatus'
_G='DisplayString'
_F='read-create'
_E='Integer32'
_D='read-write'
_C='FS-CLUSTER-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp')
fsClusterMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,31))
if mibBuilder.loadTexts:fsClusterMIB.setRevisions(('2012-07-01 00:00',))
_FsClusterMIBObjects_ObjectIdentity=ObjectIdentity
fsClusterMIBObjects=_FsClusterMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,31,1))
class _FsClusterName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_FsClusterName_Type.__name__=_G
_FsClusterName_Object=MibScalar
fsClusterName=_FsClusterName_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,1),_FsClusterName_Type())
fsClusterName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsClusterName.setStatus(_A)
class _FsClusterStatus_Type(EnabledStatus):defaultValue=1
_FsClusterStatus_Type.__name__=_H
_FsClusterStatus_Object=MibScalar
fsClusterStatus=_FsClusterStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,2),_FsClusterStatus_Type())
fsClusterStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsClusterStatus.setStatus(_A)
_FsClusterCmdMacAddress_Type=MacAddress
_FsClusterCmdMacAddress_Object=MibScalar
fsClusterCmdMacAddress=_FsClusterCmdMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,3),_FsClusterCmdMacAddress_Type())
fsClusterCmdMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterCmdMacAddress.setStatus(_A)
_FsClusterCmdName_Type=DisplayString
_FsClusterCmdName_Object=MibScalar
fsClusterCmdName=_FsClusterCmdName_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,4),_FsClusterCmdName_Type())
fsClusterCmdName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterCmdName.setStatus(_A)
class _FsClusterVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_FsClusterVlan_Type.__name__=_E
_FsClusterVlan_Object=MibScalar
fsClusterVlan=_FsClusterVlan_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,5),_FsClusterVlan_Type())
fsClusterVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:fsClusterVlan.setStatus(_A)
class _FsClusterHopsLimit_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_FsClusterHopsLimit_Type.__name__=_E
_FsClusterHopsLimit_Object=MibScalar
fsClusterHopsLimit=_FsClusterHopsLimit_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,6),_FsClusterHopsLimit_Type())
fsClusterHopsLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:fsClusterHopsLimit.setStatus(_A)
class _FsClusterTimerTopo_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_FsClusterTimerTopo_Type.__name__=_E
_FsClusterTimerTopo_Object=MibScalar
fsClusterTimerTopo=_FsClusterTimerTopo_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,7),_FsClusterTimerTopo_Type())
fsClusterTimerTopo.setMaxAccess(_D)
if mibBuilder.loadTexts:fsClusterTimerTopo.setStatus(_A)
class _FsClusterTimerHello_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_FsClusterTimerHello_Type.__name__=_E
_FsClusterTimerHello_Object=MibScalar
fsClusterTimerHello=_FsClusterTimerHello_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,8),_FsClusterTimerHello_Type())
fsClusterTimerHello.setMaxAccess(_D)
if mibBuilder.loadTexts:fsClusterTimerHello.setStatus(_A)
class _FsClusterTimerHold_Type(Integer32):defaultValue=90;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,300))
_FsClusterTimerHold_Type.__name__=_E
_FsClusterTimerHold_Object=MibScalar
fsClusterTimerHold=_FsClusterTimerHold_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,9),_FsClusterTimerHold_Type())
fsClusterTimerHold.setMaxAccess(_D)
if mibBuilder.loadTexts:fsClusterTimerHold.setStatus(_A)
_FsClusterTftpServer_Type=IpAddress
_FsClusterTftpServer_Object=MibScalar
fsClusterTftpServer=_FsClusterTftpServer_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,10),_FsClusterTftpServer_Type())
fsClusterTftpServer.setMaxAccess(_D)
if mibBuilder.loadTexts:fsClusterTftpServer.setStatus(_A)
class _FsClusterNumberOfMembers_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_FsClusterNumberOfMembers_Type.__name__=_E
_FsClusterNumberOfMembers_Object=MibScalar
fsClusterNumberOfMembers=_FsClusterNumberOfMembers_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,11),_FsClusterNumberOfMembers_Type())
fsClusterNumberOfMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterNumberOfMembers.setStatus(_A)
class _FsClusterMaxNumberOfMembers_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_FsClusterMaxNumberOfMembers_Type.__name__=_E
_FsClusterMaxNumberOfMembers_Object=MibScalar
fsClusterMaxNumberOfMembers=_FsClusterMaxNumberOfMembers_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,12),_FsClusterMaxNumberOfMembers_Type())
fsClusterMaxNumberOfMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterMaxNumberOfMembers.setStatus(_A)
class _FsClusterDevMaxCapicity_Type(Unsigned32):defaultValue=0
_FsClusterDevMaxCapicity_Type.__name__=_K
_FsClusterDevMaxCapicity_Object=MibScalar
fsClusterDevMaxCapicity=_FsClusterDevMaxCapicity_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,13),_FsClusterDevMaxCapicity_Type())
fsClusterDevMaxCapicity.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterDevMaxCapicity.setStatus(_A)
class _FsClusterAutoAdd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('disable-with-def',0),('enable',1),('disabled-with-static',2),('disabled-with-del',3)))
_FsClusterAutoAdd_Type.__name__=_E
_FsClusterAutoAdd_Object=MibScalar
fsClusterAutoAdd=_FsClusterAutoAdd_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,14),_FsClusterAutoAdd_Type())
fsClusterAutoAdd.setMaxAccess(_D)
if mibBuilder.loadTexts:fsClusterAutoAdd.setStatus(_A)
class _FsClusterExplore_Type(EnabledStatus):defaultValue=2
_FsClusterExplore_Type.__name__=_H
_FsClusterExplore_Object=MibScalar
fsClusterExplore=_FsClusterExplore_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,15),_FsClusterExplore_Type())
fsClusterExplore.setMaxAccess(_D)
if mibBuilder.loadTexts:fsClusterExplore.setStatus(_A)
_FsClusterSpecifyAdmin_ObjectIdentity=ObjectIdentity
fsClusterSpecifyAdmin=_FsClusterSpecifyAdmin_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,31,1,16))
_FsClusterSpecifyAdminAddress_Type=MacAddress
_FsClusterSpecifyAdminAddress_Object=MibScalar
fsClusterSpecifyAdminAddress=_FsClusterSpecifyAdminAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,16,1),_FsClusterSpecifyAdminAddress_Type())
fsClusterSpecifyAdminAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsClusterSpecifyAdminAddress.setStatus(_A)
class _FsClusterSpecifyAdminName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_FsClusterSpecifyAdminName_Type.__name__=_G
_FsClusterSpecifyAdminName_Object=MibScalar
fsClusterSpecifyAdminName=_FsClusterSpecifyAdminName_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,16,2),_FsClusterSpecifyAdminName_Type())
fsClusterSpecifyAdminName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsClusterSpecifyAdminName.setStatus(_A)
_FsClusterDeviceInfo_ObjectIdentity=ObjectIdentity
fsClusterDeviceInfo=_FsClusterDeviceInfo_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,31,1,17))
class _FsClusterDeviceEnable_Type(EnabledStatus):defaultValue=1
_FsClusterDeviceEnable_Type.__name__=_H
_FsClusterDeviceEnable_Object=MibScalar
fsClusterDeviceEnable=_FsClusterDeviceEnable_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,17,1),_FsClusterDeviceEnable_Type())
fsClusterDeviceEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:fsClusterDeviceEnable.setStatus(_A)
class _FsClusterDeviceRole_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('candidateDevice',1),('managerDevice',2),('memberDevice',3)))
_FsClusterDeviceRole_Type.__name__=_E
_FsClusterDeviceRole_Object=MibScalar
fsClusterDeviceRole=_FsClusterDeviceRole_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,17,2),_FsClusterDeviceRole_Type())
fsClusterDeviceRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterDeviceRole.setStatus(_A)
_FsClusterDeviceIP_Type=IpAddress
_FsClusterDeviceIP_Object=MibScalar
fsClusterDeviceIP=_FsClusterDeviceIP_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,17,3),_FsClusterDeviceIP_Type())
fsClusterDeviceIP.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterDeviceIP.setStatus(_A)
class _FsClusterDeviceSn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,240))
_FsClusterDeviceSn_Type.__name__=_E
_FsClusterDeviceSn_Object=MibScalar
fsClusterDeviceSn=_FsClusterDeviceSn_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,17,4),_FsClusterDeviceSn_Type())
fsClusterDeviceSn.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterDeviceSn.setStatus(_A)
_FsClusterIpPoolTable_Object=MibTable
fsClusterIpPoolTable=_FsClusterIpPoolTable_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,18))
if mibBuilder.loadTexts:fsClusterIpPoolTable.setStatus(_A)
_FsClusterIpPoolEntry_Object=MibTableRow
fsClusterIpPoolEntry=_FsClusterIpPoolEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,18,1))
fsClusterIpPoolEntry.setIndexNames((0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:fsClusterIpPoolEntry.setStatus(_A)
_FsClusterIpPool_Type=IpAddress
_FsClusterIpPool_Object=MibTableColumn
fsClusterIpPool=_FsClusterIpPool_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,18,1,1),_FsClusterIpPool_Type())
fsClusterIpPool.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterIpPool.setStatus(_A)
_FsClusterIpMask_Type=IpAddress
_FsClusterIpMask_Object=MibTableColumn
fsClusterIpMask=_FsClusterIpMask_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,18,1,2),_FsClusterIpMask_Type())
fsClusterIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterIpMask.setStatus(_A)
_FsClusterIpPoolRowStatus_Type=RowStatus
_FsClusterIpPoolRowStatus_Object=MibTableColumn
fsClusterIpPoolRowStatus=_FsClusterIpPoolRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,18,1,3),_FsClusterIpPoolRowStatus_Type())
fsClusterIpPoolRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsClusterIpPoolRowStatus.setStatus(_A)
_FsClusterMemberAddTable_Object=MibTable
fsClusterMemberAddTable=_FsClusterMemberAddTable_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,19))
if mibBuilder.loadTexts:fsClusterMemberAddTable.setStatus(_A)
_FsClusterMemberAddEntry_Object=MibTableRow
fsClusterMemberAddEntry=_FsClusterMemberAddEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,19,1))
fsClusterMemberAddEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:fsClusterMemberAddEntry.setStatus(_A)
class _FsClusterMemberAddSn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_FsClusterMemberAddSn_Type.__name__=_E
_FsClusterMemberAddSn_Object=MibTableColumn
fsClusterMemberAddSn=_FsClusterMemberAddSn_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,19,1,1),_FsClusterMemberAddSn_Type())
fsClusterMemberAddSn.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterMemberAddSn.setStatus(_A)
_FsClusterMemberAddMacAddress_Type=MacAddress
_FsClusterMemberAddMacAddress_Object=MibTableColumn
fsClusterMemberAddMacAddress=_FsClusterMemberAddMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,19,1,2),_FsClusterMemberAddMacAddress_Type())
fsClusterMemberAddMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsClusterMemberAddMacAddress.setStatus(_A)
_FsClusterMemberAddRowStatus_Type=RowStatus
_FsClusterMemberAddRowStatus_Object=MibTableColumn
fsClusterMemberAddRowStatus=_FsClusterMemberAddRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,19,1,3),_FsClusterMemberAddRowStatus_Type())
fsClusterMemberAddRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsClusterMemberAddRowStatus.setStatus(_A)
_FsClusterMemberTable_Object=MibTable
fsClusterMemberTable=_FsClusterMemberTable_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,20))
if mibBuilder.loadTexts:fsClusterMemberTable.setStatus(_A)
_FsClusterMemberEntry_Object=MibTableRow
fsClusterMemberEntry=_FsClusterMemberEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,20,1))
fsClusterMemberEntry.setIndexNames((0,_C,_I),(0,_C,_O),(0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:fsClusterMemberEntry.setStatus(_A)
_FsClusterMemberSn_Type=Unsigned32
_FsClusterMemberSn_Object=MibTableColumn
fsClusterMemberSn=_FsClusterMemberSn_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,20,1,1),_FsClusterMemberSn_Type())
fsClusterMemberSn.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterMemberSn.setStatus(_A)
_FsClusterMemberUpMAC_Type=MacAddress
_FsClusterMemberUpMAC_Object=MibTableColumn
fsClusterMemberUpMAC=_FsClusterMemberUpMAC_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,20,1,2),_FsClusterMemberUpMAC_Type())
fsClusterMemberUpMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterMemberUpMAC.setStatus(_A)
_FsClusterMemberLcIfx_Type=Unsigned32
_FsClusterMemberLcIfx_Object=MibTableColumn
fsClusterMemberLcIfx=_FsClusterMemberLcIfx_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,20,1,3),_FsClusterMemberLcIfx_Type())
fsClusterMemberLcIfx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterMemberLcIfx.setStatus(_A)
_FsClusterMemberUpIfx_Type=Unsigned32
_FsClusterMemberUpIfx_Object=MibTableColumn
fsClusterMemberUpIfx=_FsClusterMemberUpIfx_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,20,1,4),_FsClusterMemberUpIfx_Type())
fsClusterMemberUpIfx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterMemberUpIfx.setStatus(_A)
_FsClusterMemberLcPort_Type=DisplayString
_FsClusterMemberLcPort_Object=MibTableColumn
fsClusterMemberLcPort=_FsClusterMemberLcPort_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,20,1,5),_FsClusterMemberLcPort_Type())
fsClusterMemberLcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterMemberLcPort.setStatus(_A)
_FsClusterMemberUpPort_Type=DisplayString
_FsClusterMemberUpPort_Object=MibTableColumn
fsClusterMemberUpPort=_FsClusterMemberUpPort_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,20,1,6),_FsClusterMemberUpPort_Type())
fsClusterMemberUpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterMemberUpPort.setStatus(_A)
_FsClusterMemberMacAddress_Type=MacAddress
_FsClusterMemberMacAddress_Object=MibTableColumn
fsClusterMemberMacAddress=_FsClusterMemberMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,20,1,7),_FsClusterMemberMacAddress_Type())
fsClusterMemberMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterMemberMacAddress.setStatus(_A)
_FsClusterMemberName_Type=DisplayString
_FsClusterMemberName_Object=MibTableColumn
fsClusterMemberName=_FsClusterMemberName_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,20,1,8),_FsClusterMemberName_Type())
fsClusterMemberName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterMemberName.setStatus(_A)
_FsClusterMemberIp_Type=IpAddress
_FsClusterMemberIp_Object=MibTableColumn
fsClusterMemberIp=_FsClusterMemberIp_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,20,1,9),_FsClusterMemberIp_Type())
fsClusterMemberIp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterMemberIp.setStatus(_A)
_FsClusterMemberHops_Type=Unsigned32
_FsClusterMemberHops_Object=MibTableColumn
fsClusterMemberHops=_FsClusterMemberHops_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,20,1,10),_FsClusterMemberHops_Type())
fsClusterMemberHops.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterMemberHops.setStatus(_A)
_FsClusterMemberState_Type=DisplayString
_FsClusterMemberState_Object=MibTableColumn
fsClusterMemberState=_FsClusterMemberState_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,20,1,11),_FsClusterMemberState_Type())
fsClusterMemberState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterMemberState.setStatus(_A)
_FsClusterMemberUpSn_Type=Unsigned32
_FsClusterMemberUpSn_Object=MibTableColumn
fsClusterMemberUpSn=_FsClusterMemberUpSn_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,20,1,12),_FsClusterMemberUpSn_Type())
fsClusterMemberUpSn.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterMemberUpSn.setStatus(_A)
_FsClusterMemberLastTopoUpdateTime_Type=Unsigned32
_FsClusterMemberLastTopoUpdateTime_Object=MibTableColumn
fsClusterMemberLastTopoUpdateTime=_FsClusterMemberLastTopoUpdateTime_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,20,1,13),_FsClusterMemberLastTopoUpdateTime_Type())
fsClusterMemberLastTopoUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterMemberLastTopoUpdateTime.setStatus(_A)
_FsClusterMemberLastUdpUpdateTime_Type=Unsigned32
_FsClusterMemberLastUdpUpdateTime_Object=MibTableColumn
fsClusterMemberLastUdpUpdateTime=_FsClusterMemberLastUdpUpdateTime_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,20,1,14),_FsClusterMemberLastUdpUpdateTime_Type())
fsClusterMemberLastUdpUpdateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterMemberLastUdpUpdateTime.setStatus(_A)
_FsClusterMemberNoRecvTopoRspCount_Type=Unsigned32
_FsClusterMemberNoRecvTopoRspCount_Object=MibTableColumn
fsClusterMemberNoRecvTopoRspCount=_FsClusterMemberNoRecvTopoRspCount_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,20,1,15),_FsClusterMemberNoRecvTopoRspCount_Type())
fsClusterMemberNoRecvTopoRspCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterMemberNoRecvTopoRspCount.setStatus(_A)
_FsClusterMemberNoRecvUdpRspCount_Type=Unsigned32
_FsClusterMemberNoRecvUdpRspCount_Object=MibTableColumn
fsClusterMemberNoRecvUdpRspCount=_FsClusterMemberNoRecvUdpRspCount_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,20,1,16),_FsClusterMemberNoRecvUdpRspCount_Type())
fsClusterMemberNoRecvUdpRspCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterMemberNoRecvUdpRspCount.setStatus(_A)
_FsClusterMemberReload_Type=EnabledStatus
_FsClusterMemberReload_Object=MibTableColumn
fsClusterMemberReload=_FsClusterMemberReload_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,20,1,17),_FsClusterMemberReload_Type())
fsClusterMemberReload.setMaxAccess(_D)
if mibBuilder.loadTexts:fsClusterMemberReload.setStatus(_A)
_FsClusterCandidateTable_Object=MibTable
fsClusterCandidateTable=_FsClusterCandidateTable_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,21))
if mibBuilder.loadTexts:fsClusterCandidateTable.setStatus(_A)
_FsClusterCandidateEntry_Object=MibTableRow
fsClusterCandidateEntry=_FsClusterCandidateEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,21,1))
fsClusterCandidateEntry.setIndexNames((0,_C,_J),(0,_C,_R),(0,_C,_S),(0,_C,_T))
if mibBuilder.loadTexts:fsClusterCandidateEntry.setStatus(_A)
_FsClusterCandidateMacAddress_Type=MacAddress
_FsClusterCandidateMacAddress_Object=MibTableColumn
fsClusterCandidateMacAddress=_FsClusterCandidateMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,21,1,1),_FsClusterCandidateMacAddress_Type())
fsClusterCandidateMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterCandidateMacAddress.setStatus(_A)
_FsClusterCandidateUpMAC_Type=MacAddress
_FsClusterCandidateUpMAC_Object=MibTableColumn
fsClusterCandidateUpMAC=_FsClusterCandidateUpMAC_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,21,1,2),_FsClusterCandidateUpMAC_Type())
fsClusterCandidateUpMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterCandidateUpMAC.setStatus(_A)
_FsClusterCandidateLcIfx_Type=Unsigned32
_FsClusterCandidateLcIfx_Object=MibTableColumn
fsClusterCandidateLcIfx=_FsClusterCandidateLcIfx_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,21,1,3),_FsClusterCandidateLcIfx_Type())
fsClusterCandidateLcIfx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterCandidateLcIfx.setStatus(_A)
_FsClusterCandidateUpIfx_Type=Unsigned32
_FsClusterCandidateUpIfx_Object=MibTableColumn
fsClusterCandidateUpIfx=_FsClusterCandidateUpIfx_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,21,1,4),_FsClusterCandidateUpIfx_Type())
fsClusterCandidateUpIfx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterCandidateUpIfx.setStatus(_A)
_FsClusterCandidateLcPort_Type=DisplayString
_FsClusterCandidateLcPort_Object=MibTableColumn
fsClusterCandidateLcPort=_FsClusterCandidateLcPort_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,21,1,5),_FsClusterCandidateLcPort_Type())
fsClusterCandidateLcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterCandidateLcPort.setStatus(_A)
_FsClusterCandidateUpPort_Type=DisplayString
_FsClusterCandidateUpPort_Object=MibTableColumn
fsClusterCandidateUpPort=_FsClusterCandidateUpPort_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,21,1,6),_FsClusterCandidateUpPort_Type())
fsClusterCandidateUpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterCandidateUpPort.setStatus(_A)
_FsClusterCandidateUpSn_Type=Unsigned32
_FsClusterCandidateUpSn_Object=MibTableColumn
fsClusterCandidateUpSn=_FsClusterCandidateUpSn_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,21,1,7),_FsClusterCandidateUpSn_Type())
fsClusterCandidateUpSn.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterCandidateUpSn.setStatus(_A)
_FsClusterCandidateHops_Type=Unsigned32
_FsClusterCandidateHops_Object=MibTableColumn
fsClusterCandidateHops=_FsClusterCandidateHops_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,21,1,8),_FsClusterCandidateHops_Type())
fsClusterCandidateHops.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterCandidateHops.setStatus(_A)
_FsClusterCandidateState_Type=DisplayString
_FsClusterCandidateState_Object=MibTableColumn
fsClusterCandidateState=_FsClusterCandidateState_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,21,1,9),_FsClusterCandidateState_Type())
fsClusterCandidateState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterCandidateState.setStatus(_A)
_FsClusterBlacklistTable_Object=MibTable
fsClusterBlacklistTable=_FsClusterBlacklistTable_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,22))
if mibBuilder.loadTexts:fsClusterBlacklistTable.setStatus(_A)
_FsClusterBlacklistEntry_Object=MibTableRow
fsClusterBlacklistEntry=_FsClusterBlacklistEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,22,1))
fsClusterBlacklistEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:fsClusterBlacklistEntry.setStatus(_A)
_FsClusterBlacklistMacAddress_Type=MacAddress
_FsClusterBlacklistMacAddress_Object=MibTableColumn
fsClusterBlacklistMacAddress=_FsClusterBlacklistMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,22,1,1),_FsClusterBlacklistMacAddress_Type())
fsClusterBlacklistMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterBlacklistMacAddress.setStatus(_A)
_FsClusterBlackListRowStatus_Type=RowStatus
_FsClusterBlackListRowStatus_Object=MibTableColumn
fsClusterBlackListRowStatus=_FsClusterBlackListRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,22,1,2),_FsClusterBlackListRowStatus_Type())
fsClusterBlackListRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsClusterBlackListRowStatus.setStatus(_A)
_FsClusterPasswordAuth_ObjectIdentity=ObjectIdentity
fsClusterPasswordAuth=_FsClusterPasswordAuth_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,31,1,23))
_FsClusterPasswordAuthPoolTable_Object=MibTable
fsClusterPasswordAuthPoolTable=_FsClusterPasswordAuthPoolTable_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,23,1))
if mibBuilder.loadTexts:fsClusterPasswordAuthPoolTable.setStatus(_A)
_FsClusterPasswordAuthPoolEntry_Object=MibTableRow
fsClusterPasswordAuthPoolEntry=_FsClusterPasswordAuthPoolEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,23,1,1))
fsClusterPasswordAuthPoolEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:fsClusterPasswordAuthPoolEntry.setStatus(_A)
class _FsClusterPasswordSn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_FsClusterPasswordSn_Type.__name__=_E
_FsClusterPasswordSn_Object=MibTableColumn
fsClusterPasswordSn=_FsClusterPasswordSn_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,23,1,1,1),_FsClusterPasswordSn_Type())
fsClusterPasswordSn.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterPasswordSn.setStatus(_A)
class _FsClusterPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,126))
_FsClusterPassword_Type.__name__=_G
_FsClusterPassword_Object=MibTableColumn
fsClusterPassword=_FsClusterPassword_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,23,1,1,2),_FsClusterPassword_Type())
fsClusterPassword.setMaxAccess(_F)
if mibBuilder.loadTexts:fsClusterPassword.setStatus(_A)
_FsClusterPasswordAuthRowStatus_Type=RowStatus
_FsClusterPasswordAuthRowStatus_Object=MibTableColumn
fsClusterPasswordAuthRowStatus=_FsClusterPasswordAuthRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,23,1,1,3),_FsClusterPasswordAuthRowStatus_Type())
fsClusterPasswordAuthRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsClusterPasswordAuthRowStatus.setStatus(_A)
_FsClusterDeviceAuthPasswordTable_Object=MibTable
fsClusterDeviceAuthPasswordTable=_FsClusterDeviceAuthPasswordTable_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,23,2))
if mibBuilder.loadTexts:fsClusterDeviceAuthPasswordTable.setStatus(_A)
_FsClusterDeviceAuthPasswordEntry_Object=MibTableRow
fsClusterDeviceAuthPasswordEntry=_FsClusterDeviceAuthPasswordEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,23,2,1))
fsClusterDeviceAuthPasswordEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:fsClusterDeviceAuthPasswordEntry.setStatus(_A)
_FsClusterDeviceMacAddress_Type=MacAddress
_FsClusterDeviceMacAddress_Object=MibTableColumn
fsClusterDeviceMacAddress=_FsClusterDeviceMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,23,2,1,1),_FsClusterDeviceMacAddress_Type())
fsClusterDeviceMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsClusterDeviceMacAddress.setStatus(_A)
class _FsClusterDevicePassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,126))
_FsClusterDevicePassword_Type.__name__=_G
_FsClusterDevicePassword_Object=MibTableColumn
fsClusterDevicePassword=_FsClusterDevicePassword_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,23,2,1,2),_FsClusterDevicePassword_Type())
fsClusterDevicePassword.setMaxAccess(_F)
if mibBuilder.loadTexts:fsClusterDevicePassword.setStatus(_A)
_FsClusterDevicePasswordRowStatus_Type=RowStatus
_FsClusterDevicePasswordRowStatus_Object=MibTableColumn
fsClusterDevicePasswordRowStatus=_FsClusterDevicePasswordRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,31,1,23,2,1,3),_FsClusterDevicePasswordRowStatus_Type())
fsClusterDevicePasswordRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsClusterDevicePasswordRowStatus.setStatus(_A)
_FsClusterTraps_ObjectIdentity=ObjectIdentity
fsClusterTraps=_FsClusterTraps_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,31,2))
fsClusterMemberStateChangeTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,31,2,1))
fsClusterMemberStateChangeTrap.setObjects(*((_C,_I),(_C,_X)))
if mibBuilder.loadTexts:fsClusterMemberStateChangeTrap.setStatus(_A)
fsClusterMemberFailureTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,31,2,2))
fsClusterMemberFailureTrap.setObjects((_C,_J))
if mibBuilder.loadTexts:fsClusterMemberFailureTrap.setStatus(_A)
fsClusterDevMaximumAllowedTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,31,2,3))
if mibBuilder.loadTexts:fsClusterDevMaximumAllowedTrap.setStatus(_A)
fsClusterMemberMaximumAllowedTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,31,2,4))
if mibBuilder.loadTexts:fsClusterMemberMaximumAllowedTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fsClusterMIB':fsClusterMIB,'fsClusterMIBObjects':fsClusterMIBObjects,'fsClusterName':fsClusterName,'fsClusterStatus':fsClusterStatus,'fsClusterCmdMacAddress':fsClusterCmdMacAddress,'fsClusterCmdName':fsClusterCmdName,'fsClusterVlan':fsClusterVlan,'fsClusterHopsLimit':fsClusterHopsLimit,'fsClusterTimerTopo':fsClusterTimerTopo,'fsClusterTimerHello':fsClusterTimerHello,'fsClusterTimerHold':fsClusterTimerHold,'fsClusterTftpServer':fsClusterTftpServer,'fsClusterNumberOfMembers':fsClusterNumberOfMembers,'fsClusterMaxNumberOfMembers':fsClusterMaxNumberOfMembers,'fsClusterDevMaxCapicity':fsClusterDevMaxCapicity,'fsClusterAutoAdd':fsClusterAutoAdd,'fsClusterExplore':fsClusterExplore,'fsClusterSpecifyAdmin':fsClusterSpecifyAdmin,'fsClusterSpecifyAdminAddress':fsClusterSpecifyAdminAddress,'fsClusterSpecifyAdminName':fsClusterSpecifyAdminName,'fsClusterDeviceInfo':fsClusterDeviceInfo,'fsClusterDeviceEnable':fsClusterDeviceEnable,'fsClusterDeviceRole':fsClusterDeviceRole,'fsClusterDeviceIP':fsClusterDeviceIP,'fsClusterDeviceSn':fsClusterDeviceSn,'fsClusterIpPoolTable':fsClusterIpPoolTable,'fsClusterIpPoolEntry':fsClusterIpPoolEntry,_L:fsClusterIpPool,_M:fsClusterIpMask,'fsClusterIpPoolRowStatus':fsClusterIpPoolRowStatus,'fsClusterMemberAddTable':fsClusterMemberAddTable,'fsClusterMemberAddEntry':fsClusterMemberAddEntry,_N:fsClusterMemberAddSn,'fsClusterMemberAddMacAddress':fsClusterMemberAddMacAddress,'fsClusterMemberAddRowStatus':fsClusterMemberAddRowStatus,'fsClusterMemberTable':fsClusterMemberTable,'fsClusterMemberEntry':fsClusterMemberEntry,_I:fsClusterMemberSn,_O:fsClusterMemberUpMAC,_P:fsClusterMemberLcIfx,_Q:fsClusterMemberUpIfx,'fsClusterMemberLcPort':fsClusterMemberLcPort,'fsClusterMemberUpPort':fsClusterMemberUpPort,'fsClusterMemberMacAddress':fsClusterMemberMacAddress,'fsClusterMemberName':fsClusterMemberName,'fsClusterMemberIp':fsClusterMemberIp,'fsClusterMemberHops':fsClusterMemberHops,_X:fsClusterMemberState,'fsClusterMemberUpSn':fsClusterMemberUpSn,'fsClusterMemberLastTopoUpdateTime':fsClusterMemberLastTopoUpdateTime,'fsClusterMemberLastUdpUpdateTime':fsClusterMemberLastUdpUpdateTime,'fsClusterMemberNoRecvTopoRspCount':fsClusterMemberNoRecvTopoRspCount,'fsClusterMemberNoRecvUdpRspCount':fsClusterMemberNoRecvUdpRspCount,'fsClusterMemberReload':fsClusterMemberReload,'fsClusterCandidateTable':fsClusterCandidateTable,'fsClusterCandidateEntry':fsClusterCandidateEntry,_J:fsClusterCandidateMacAddress,_R:fsClusterCandidateUpMAC,_S:fsClusterCandidateLcIfx,_T:fsClusterCandidateUpIfx,'fsClusterCandidateLcPort':fsClusterCandidateLcPort,'fsClusterCandidateUpPort':fsClusterCandidateUpPort,'fsClusterCandidateUpSn':fsClusterCandidateUpSn,'fsClusterCandidateHops':fsClusterCandidateHops,'fsClusterCandidateState':fsClusterCandidateState,'fsClusterBlacklistTable':fsClusterBlacklistTable,'fsClusterBlacklistEntry':fsClusterBlacklistEntry,_U:fsClusterBlacklistMacAddress,'fsClusterBlackListRowStatus':fsClusterBlackListRowStatus,'fsClusterPasswordAuth':fsClusterPasswordAuth,'fsClusterPasswordAuthPoolTable':fsClusterPasswordAuthPoolTable,'fsClusterPasswordAuthPoolEntry':fsClusterPasswordAuthPoolEntry,_V:fsClusterPasswordSn,'fsClusterPassword':fsClusterPassword,'fsClusterPasswordAuthRowStatus':fsClusterPasswordAuthRowStatus,'fsClusterDeviceAuthPasswordTable':fsClusterDeviceAuthPasswordTable,'fsClusterDeviceAuthPasswordEntry':fsClusterDeviceAuthPasswordEntry,_W:fsClusterDeviceMacAddress,'fsClusterDevicePassword':fsClusterDevicePassword,'fsClusterDevicePasswordRowStatus':fsClusterDevicePasswordRowStatus,'fsClusterTraps':fsClusterTraps,'fsClusterMemberStateChangeTrap':fsClusterMemberStateChangeTrap,'fsClusterMemberFailureTrap':fsClusterMemberFailureTrap,'fsClusterDevMaximumAllowedTrap':fsClusterDevMaximumAllowedTrap,'fsClusterMemberMaximumAllowedTrap':fsClusterMemberMaximumAllowedTrap})