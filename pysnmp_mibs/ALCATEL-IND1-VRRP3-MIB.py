_A0='alaVrrp3NotificationsGroup'
_z='alaVrrp3TrapInfoGroup'
_y='alaVrrp3StatsGroup'
_x='alaVrrp3OperGroup'
_w='alaVrrp3TrapProtoError'
_v='alaVrrp3TrapNewMaster'
_u='alaVrrp3StatsPacketLengthErrors'
_t='alaVrrp3StatsAddressListErrors'
_s='alaVrrp3StatsIpTtlErrors'
_r='alaVrrp3StatsInvldAuthType'
_q='alaVrrp3StatsInvldTypePktsRcvd'
_p='alaVrrp3StatsPriZeroPktsSent'
_o='alaVrrp3StatsPriZeroPktsRcvd'
_n='alaVrrp3StatsAdvIntervalErrors'
_m='alaVrrp3StatsAdvertiseRcvd'
_l='alaVrrp3StatsBecomeMaster'
_k='alaVrrp3RouterVrIdErrors'
_j='alaVrrp3RouterVersionErrors'
_i='alaVrrp3RouterChecksumErrors'
_h='alaVrrp3AssoIpAddrRowStatus'
_g='alaVrrp3OperRowStatus'
_f='alaVrrp3OperUpTime'
_e='alaVrrp3OperAcceptMode'
_d='alaVrrp3OperPreemptMode'
_c='alaVrrp3OperAdvInterval'
_b='alaVrrp3OperPrimaryIpAddr'
_a='alaVrrp3OperPrimaryIpAddrType'
_Z='alaVrrp3OperIpAddrCount'
_Y='alaVrrp3OperVersion'
_X='alaVrrp3OperPriority'
_W='alaVrrp3OperAdminState'
_V='alaVrrp3OperState'
_U='alaVrrp3OperVirtualMacAddr'
_T='alaVrrp3NotificationCntl'
_S='accessible-for-notify'
_R='alaVrrp3AssoIpAddr'
_Q='alaVrrp3AssoIpAddrType'
_P='alaVrrp3TrapProtoErrReason'
_O='alaVrrp3TrapNewMasterReason'
_N='alaVrrp3OperMasterIpAddr'
_M='alaVrrp3OperMasterIpAddrType'
_L='TruthValue'
_K='InetAddress'
_J='not-accessible'
_I='alaVrrp3OperVrId'
_H='alaVrrp3OperIpVersion'
_G='ifIndex'
_F='IF-MIB'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='current'
_A='ALCATEL-IND1-VRRP3-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1Vrrp,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1Vrrp')
ifIndex,=mibBuilder.importSymbols(_F,_G)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_K,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp',_L)
VrId,=mibBuilder.importSymbols('VRRP-MIB','VrId')
alcatelIND1VRRP3MIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,28,2))
if mibBuilder.loadTexts:alcatelIND1VRRP3MIB.setRevisions(('2007-04-03 00:00',))
_AlaVrrp3Notifications_ObjectIdentity=ObjectIdentity
alaVrrp3Notifications=_AlaVrrp3Notifications_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,28,2,0))
_AlaVrrp3Operations_ObjectIdentity=ObjectIdentity
alaVrrp3Operations=_AlaVrrp3Operations_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,28,2,1))
class _AlaVrrp3NotificationCntl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_AlaVrrp3NotificationCntl_Type.__name__=_D
_AlaVrrp3NotificationCntl_Object=MibScalar
alaVrrp3NotificationCntl=_AlaVrrp3NotificationCntl_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,1),_AlaVrrp3NotificationCntl_Type())
alaVrrp3NotificationCntl.setMaxAccess('read-write')
if mibBuilder.loadTexts:alaVrrp3NotificationCntl.setStatus(_B)
_AlaVrrp3OperTable_Object=MibTable
alaVrrp3OperTable=_AlaVrrp3OperTable_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,2))
if mibBuilder.loadTexts:alaVrrp3OperTable.setStatus(_B)
_AlaVrrp3OperEntry_Object=MibTableRow
alaVrrp3OperEntry=_AlaVrrp3OperEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,2,1))
alaVrrp3OperEntry.setIndexNames((0,_A,_H),(0,_A,_I),(0,_F,_G))
if mibBuilder.loadTexts:alaVrrp3OperEntry.setStatus(_B)
class _AlaVrrp3OperIpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_AlaVrrp3OperIpVersion_Type.__name__=_D
_AlaVrrp3OperIpVersion_Object=MibTableColumn
alaVrrp3OperIpVersion=_AlaVrrp3OperIpVersion_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,2,1,1),_AlaVrrp3OperIpVersion_Type())
alaVrrp3OperIpVersion.setMaxAccess(_J)
if mibBuilder.loadTexts:alaVrrp3OperIpVersion.setStatus(_B)
_AlaVrrp3OperVrId_Type=VrId
_AlaVrrp3OperVrId_Object=MibTableColumn
alaVrrp3OperVrId=_AlaVrrp3OperVrId_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,2,1,2),_AlaVrrp3OperVrId_Type())
alaVrrp3OperVrId.setMaxAccess(_J)
if mibBuilder.loadTexts:alaVrrp3OperVrId.setStatus(_B)
_AlaVrrp3OperVirtualMacAddr_Type=MacAddress
_AlaVrrp3OperVirtualMacAddr_Object=MibTableColumn
alaVrrp3OperVirtualMacAddr=_AlaVrrp3OperVirtualMacAddr_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,2,1,3),_AlaVrrp3OperVirtualMacAddr_Type())
alaVrrp3OperVirtualMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3OperVirtualMacAddr.setStatus(_B)
class _AlaVrrp3OperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('initialize',1),('backup',2),('master',3)))
_AlaVrrp3OperState_Type.__name__=_D
_AlaVrrp3OperState_Object=MibTableColumn
alaVrrp3OperState=_AlaVrrp3OperState_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,2,1,4),_AlaVrrp3OperState_Type())
alaVrrp3OperState.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3OperState.setStatus(_B)
class _AlaVrrp3OperAdminState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_AlaVrrp3OperAdminState_Type.__name__=_D
_AlaVrrp3OperAdminState_Object=MibTableColumn
alaVrrp3OperAdminState=_AlaVrrp3OperAdminState_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,2,1,5),_AlaVrrp3OperAdminState_Type())
alaVrrp3OperAdminState.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVrrp3OperAdminState.setStatus(_B)
class _AlaVrrp3OperPriority_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaVrrp3OperPriority_Type.__name__=_D
_AlaVrrp3OperPriority_Object=MibTableColumn
alaVrrp3OperPriority=_AlaVrrp3OperPriority_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,2,1,6),_AlaVrrp3OperPriority_Type())
alaVrrp3OperPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVrrp3OperPriority.setStatus(_B)
class _AlaVrrp3OperVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vrrpv2',1),('vrrpv3',2)))
_AlaVrrp3OperVersion_Type.__name__=_D
_AlaVrrp3OperVersion_Object=MibTableColumn
alaVrrp3OperVersion=_AlaVrrp3OperVersion_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,2,1,7),_AlaVrrp3OperVersion_Type())
alaVrrp3OperVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3OperVersion.setStatus(_B)
class _AlaVrrp3OperIpAddrCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaVrrp3OperIpAddrCount_Type.__name__=_D
_AlaVrrp3OperIpAddrCount_Object=MibTableColumn
alaVrrp3OperIpAddrCount=_AlaVrrp3OperIpAddrCount_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,2,1,8),_AlaVrrp3OperIpAddrCount_Type())
alaVrrp3OperIpAddrCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3OperIpAddrCount.setStatus(_B)
_AlaVrrp3OperMasterIpAddrType_Type=InetAddressType
_AlaVrrp3OperMasterIpAddrType_Object=MibTableColumn
alaVrrp3OperMasterIpAddrType=_AlaVrrp3OperMasterIpAddrType_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,2,1,9),_AlaVrrp3OperMasterIpAddrType_Type())
alaVrrp3OperMasterIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3OperMasterIpAddrType.setStatus(_B)
_AlaVrrp3OperMasterIpAddr_Type=InetAddress
_AlaVrrp3OperMasterIpAddr_Object=MibTableColumn
alaVrrp3OperMasterIpAddr=_AlaVrrp3OperMasterIpAddr_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,2,1,10),_AlaVrrp3OperMasterIpAddr_Type())
alaVrrp3OperMasterIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3OperMasterIpAddr.setStatus(_B)
_AlaVrrp3OperPrimaryIpAddrType_Type=InetAddressType
_AlaVrrp3OperPrimaryIpAddrType_Object=MibTableColumn
alaVrrp3OperPrimaryIpAddrType=_AlaVrrp3OperPrimaryIpAddrType_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,2,1,11),_AlaVrrp3OperPrimaryIpAddrType_Type())
alaVrrp3OperPrimaryIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3OperPrimaryIpAddrType.setStatus(_B)
class _AlaVrrp3OperPrimaryIpAddr_Type(InetAddress):defaultHexValue='00000000'
_AlaVrrp3OperPrimaryIpAddr_Type.__name__=_K
_AlaVrrp3OperPrimaryIpAddr_Object=MibTableColumn
alaVrrp3OperPrimaryIpAddr=_AlaVrrp3OperPrimaryIpAddr_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,2,1,12),_AlaVrrp3OperPrimaryIpAddr_Type())
alaVrrp3OperPrimaryIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3OperPrimaryIpAddr.setStatus(_B)
class _AlaVrrp3OperAdvInterval_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_AlaVrrp3OperAdvInterval_Type.__name__=_D
_AlaVrrp3OperAdvInterval_Object=MibTableColumn
alaVrrp3OperAdvInterval=_AlaVrrp3OperAdvInterval_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,2,1,13),_AlaVrrp3OperAdvInterval_Type())
alaVrrp3OperAdvInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVrrp3OperAdvInterval.setStatus(_B)
if mibBuilder.loadTexts:alaVrrp3OperAdvInterval.setUnits('centiseconds')
class _AlaVrrp3OperPreemptMode_Type(TruthValue):defaultValue=1
_AlaVrrp3OperPreemptMode_Type.__name__=_L
_AlaVrrp3OperPreemptMode_Object=MibTableColumn
alaVrrp3OperPreemptMode=_AlaVrrp3OperPreemptMode_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,2,1,14),_AlaVrrp3OperPreemptMode_Type())
alaVrrp3OperPreemptMode.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVrrp3OperPreemptMode.setStatus(_B)
class _AlaVrrp3OperAcceptMode_Type(TruthValue):defaultValue=1
_AlaVrrp3OperAcceptMode_Type.__name__=_L
_AlaVrrp3OperAcceptMode_Object=MibTableColumn
alaVrrp3OperAcceptMode=_AlaVrrp3OperAcceptMode_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,2,1,15),_AlaVrrp3OperAcceptMode_Type())
alaVrrp3OperAcceptMode.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVrrp3OperAcceptMode.setStatus(_B)
_AlaVrrp3OperUpTime_Type=TimeStamp
_AlaVrrp3OperUpTime_Object=MibTableColumn
alaVrrp3OperUpTime=_AlaVrrp3OperUpTime_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,2,1,16),_AlaVrrp3OperUpTime_Type())
alaVrrp3OperUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3OperUpTime.setStatus(_B)
_AlaVrrp3OperRowStatus_Type=RowStatus
_AlaVrrp3OperRowStatus_Object=MibTableColumn
alaVrrp3OperRowStatus=_AlaVrrp3OperRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,2,1,17),_AlaVrrp3OperRowStatus_Type())
alaVrrp3OperRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVrrp3OperRowStatus.setStatus(_B)
_AlaVrrp3AssoIpAddrTable_Object=MibTable
alaVrrp3AssoIpAddrTable=_AlaVrrp3AssoIpAddrTable_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,3))
if mibBuilder.loadTexts:alaVrrp3AssoIpAddrTable.setStatus(_B)
_AlaVrrp3AssoIpAddrEntry_Object=MibTableRow
alaVrrp3AssoIpAddrEntry=_AlaVrrp3AssoIpAddrEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,3,1))
alaVrrp3AssoIpAddrEntry.setIndexNames((0,_A,_H),(0,_A,_I),(0,_F,_G),(0,_A,_Q),(0,_A,_R))
if mibBuilder.loadTexts:alaVrrp3AssoIpAddrEntry.setStatus(_B)
_AlaVrrp3AssoIpAddrType_Type=InetAddressType
_AlaVrrp3AssoIpAddrType_Object=MibTableColumn
alaVrrp3AssoIpAddrType=_AlaVrrp3AssoIpAddrType_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,3,1,1),_AlaVrrp3AssoIpAddrType_Type())
alaVrrp3AssoIpAddrType.setMaxAccess(_J)
if mibBuilder.loadTexts:alaVrrp3AssoIpAddrType.setStatus(_B)
class _AlaVrrp3AssoIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_AlaVrrp3AssoIpAddr_Type.__name__=_K
_AlaVrrp3AssoIpAddr_Object=MibTableColumn
alaVrrp3AssoIpAddr=_AlaVrrp3AssoIpAddr_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,3,1,2),_AlaVrrp3AssoIpAddr_Type())
alaVrrp3AssoIpAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:alaVrrp3AssoIpAddr.setStatus(_B)
_AlaVrrp3AssoIpAddrRowStatus_Type=RowStatus
_AlaVrrp3AssoIpAddrRowStatus_Object=MibTableColumn
alaVrrp3AssoIpAddrRowStatus=_AlaVrrp3AssoIpAddrRowStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,3,1,3),_AlaVrrp3AssoIpAddrRowStatus_Type())
alaVrrp3AssoIpAddrRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:alaVrrp3AssoIpAddrRowStatus.setStatus(_B)
class _AlaVrrp3TrapNewMasterReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('priority',0),('preempted',1),('masterNoResponse',2)))
_AlaVrrp3TrapNewMasterReason_Type.__name__=_D
_AlaVrrp3TrapNewMasterReason_Object=MibScalar
alaVrrp3TrapNewMasterReason=_AlaVrrp3TrapNewMasterReason_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,4),_AlaVrrp3TrapNewMasterReason_Type())
alaVrrp3TrapNewMasterReason.setMaxAccess(_S)
if mibBuilder.loadTexts:alaVrrp3TrapNewMasterReason.setStatus(_B)
class _AlaVrrp3TrapProtoErrReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('hopLimitError',0),('versionError',1),('checksumError',2),('vridError',3)))
_AlaVrrp3TrapProtoErrReason_Type.__name__=_D
_AlaVrrp3TrapProtoErrReason_Object=MibScalar
alaVrrp3TrapProtoErrReason=_AlaVrrp3TrapProtoErrReason_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,1,5),_AlaVrrp3TrapProtoErrReason_Type())
alaVrrp3TrapProtoErrReason.setMaxAccess(_S)
if mibBuilder.loadTexts:alaVrrp3TrapProtoErrReason.setStatus(_B)
_AlaVrrp3Statistics_ObjectIdentity=ObjectIdentity
alaVrrp3Statistics=_AlaVrrp3Statistics_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,28,2,2))
_AlaVrrp3RouterChecksumErrors_Type=Counter32
_AlaVrrp3RouterChecksumErrors_Object=MibScalar
alaVrrp3RouterChecksumErrors=_AlaVrrp3RouterChecksumErrors_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,2,1),_AlaVrrp3RouterChecksumErrors_Type())
alaVrrp3RouterChecksumErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3RouterChecksumErrors.setStatus(_B)
_AlaVrrp3RouterVersionErrors_Type=Counter32
_AlaVrrp3RouterVersionErrors_Object=MibScalar
alaVrrp3RouterVersionErrors=_AlaVrrp3RouterVersionErrors_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,2,2),_AlaVrrp3RouterVersionErrors_Type())
alaVrrp3RouterVersionErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3RouterVersionErrors.setStatus(_B)
_AlaVrrp3RouterVrIdErrors_Type=Counter32
_AlaVrrp3RouterVrIdErrors_Object=MibScalar
alaVrrp3RouterVrIdErrors=_AlaVrrp3RouterVrIdErrors_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,2,3),_AlaVrrp3RouterVrIdErrors_Type())
alaVrrp3RouterVrIdErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3RouterVrIdErrors.setStatus(_B)
_AlaVrrp3RouterStatsTable_Object=MibTable
alaVrrp3RouterStatsTable=_AlaVrrp3RouterStatsTable_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,2,4))
if mibBuilder.loadTexts:alaVrrp3RouterStatsTable.setStatus(_B)
_AlaVrrp3RouterStatsEntry_Object=MibTableRow
alaVrrp3RouterStatsEntry=_AlaVrrp3RouterStatsEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,2,4,1))
alaVrrp3RouterStatsEntry.setIndexNames((0,_A,_H),(0,_A,_I),(0,_F,_G))
if mibBuilder.loadTexts:alaVrrp3RouterStatsEntry.setStatus(_B)
_AlaVrrp3StatsBecomeMaster_Type=Counter32
_AlaVrrp3StatsBecomeMaster_Object=MibTableColumn
alaVrrp3StatsBecomeMaster=_AlaVrrp3StatsBecomeMaster_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,2,4,1,1),_AlaVrrp3StatsBecomeMaster_Type())
alaVrrp3StatsBecomeMaster.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3StatsBecomeMaster.setStatus(_B)
_AlaVrrp3StatsAdvertiseRcvd_Type=Counter32
_AlaVrrp3StatsAdvertiseRcvd_Object=MibTableColumn
alaVrrp3StatsAdvertiseRcvd=_AlaVrrp3StatsAdvertiseRcvd_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,2,4,1,2),_AlaVrrp3StatsAdvertiseRcvd_Type())
alaVrrp3StatsAdvertiseRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3StatsAdvertiseRcvd.setStatus(_B)
_AlaVrrp3StatsAdvIntervalErrors_Type=Counter32
_AlaVrrp3StatsAdvIntervalErrors_Object=MibTableColumn
alaVrrp3StatsAdvIntervalErrors=_AlaVrrp3StatsAdvIntervalErrors_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,2,4,1,3),_AlaVrrp3StatsAdvIntervalErrors_Type())
alaVrrp3StatsAdvIntervalErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3StatsAdvIntervalErrors.setStatus(_B)
_AlaVrrp3StatsIpTtlErrors_Type=Counter32
_AlaVrrp3StatsIpTtlErrors_Object=MibTableColumn
alaVrrp3StatsIpTtlErrors=_AlaVrrp3StatsIpTtlErrors_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,2,4,1,4),_AlaVrrp3StatsIpTtlErrors_Type())
alaVrrp3StatsIpTtlErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3StatsIpTtlErrors.setStatus(_B)
_AlaVrrp3StatsPriZeroPktsRcvd_Type=Counter32
_AlaVrrp3StatsPriZeroPktsRcvd_Object=MibTableColumn
alaVrrp3StatsPriZeroPktsRcvd=_AlaVrrp3StatsPriZeroPktsRcvd_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,2,4,1,5),_AlaVrrp3StatsPriZeroPktsRcvd_Type())
alaVrrp3StatsPriZeroPktsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3StatsPriZeroPktsRcvd.setStatus(_B)
_AlaVrrp3StatsPriZeroPktsSent_Type=Counter32
_AlaVrrp3StatsPriZeroPktsSent_Object=MibTableColumn
alaVrrp3StatsPriZeroPktsSent=_AlaVrrp3StatsPriZeroPktsSent_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,2,4,1,6),_AlaVrrp3StatsPriZeroPktsSent_Type())
alaVrrp3StatsPriZeroPktsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3StatsPriZeroPktsSent.setStatus(_B)
_AlaVrrp3StatsInvldTypePktsRcvd_Type=Counter32
_AlaVrrp3StatsInvldTypePktsRcvd_Object=MibTableColumn
alaVrrp3StatsInvldTypePktsRcvd=_AlaVrrp3StatsInvldTypePktsRcvd_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,2,4,1,7),_AlaVrrp3StatsInvldTypePktsRcvd_Type())
alaVrrp3StatsInvldTypePktsRcvd.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3StatsInvldTypePktsRcvd.setStatus(_B)
_AlaVrrp3StatsAddressListErrors_Type=Counter32
_AlaVrrp3StatsAddressListErrors_Object=MibTableColumn
alaVrrp3StatsAddressListErrors=_AlaVrrp3StatsAddressListErrors_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,2,4,1,8),_AlaVrrp3StatsAddressListErrors_Type())
alaVrrp3StatsAddressListErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3StatsAddressListErrors.setStatus(_B)
_AlaVrrp3StatsInvldAuthType_Type=Counter32
_AlaVrrp3StatsInvldAuthType_Object=MibTableColumn
alaVrrp3StatsInvldAuthType=_AlaVrrp3StatsInvldAuthType_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,2,4,1,9),_AlaVrrp3StatsInvldAuthType_Type())
alaVrrp3StatsInvldAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3StatsInvldAuthType.setStatus(_B)
_AlaVrrp3StatsPacketLengthErrors_Type=Counter32
_AlaVrrp3StatsPacketLengthErrors_Object=MibTableColumn
alaVrrp3StatsPacketLengthErrors=_AlaVrrp3StatsPacketLengthErrors_Object((1,3,6,1,4,1,6486,800,1,2,1,28,2,2,4,1,10),_AlaVrrp3StatsPacketLengthErrors_Type())
alaVrrp3StatsPacketLengthErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVrrp3StatsPacketLengthErrors.setStatus(_B)
_AlaVrrp3Conformance_ObjectIdentity=ObjectIdentity
alaVrrp3Conformance=_AlaVrrp3Conformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,28,2,3))
_AlaVrrp3MIBCompliances_ObjectIdentity=ObjectIdentity
alaVrrp3MIBCompliances=_AlaVrrp3MIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,28,2,3,1))
_AlaVrrp3MIBGroups_ObjectIdentity=ObjectIdentity
alaVrrp3MIBGroups=_AlaVrrp3MIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,28,2,3,2))
alaVrrp3OperGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,28,2,3,2,1))
alaVrrp3OperGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_M),(_A,_N),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:alaVrrp3OperGroup.setStatus(_B)
alaVrrp3StatsGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,28,2,3,2,2))
alaVrrp3StatsGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:alaVrrp3StatsGroup.setStatus(_B)
alaVrrp3TrapInfoGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,28,2,3,2,3))
alaVrrp3TrapInfoGroup.setObjects(*((_A,_O),(_A,_P)))
if mibBuilder.loadTexts:alaVrrp3TrapInfoGroup.setStatus(_B)
alaVrrp3TrapNewMaster=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,28,2,0,1))
alaVrrp3TrapNewMaster.setObjects(*((_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:alaVrrp3TrapNewMaster.setStatus(_B)
alaVrrp3TrapProtoError=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,28,2,0,2))
alaVrrp3TrapProtoError.setObjects((_A,_P))
if mibBuilder.loadTexts:alaVrrp3TrapProtoError.setStatus(_B)
alaVrrp3NotificationsGroup=NotificationGroup((1,3,6,1,4,1,6486,800,1,2,1,28,2,3,2,4))
alaVrrp3NotificationsGroup.setObjects(*((_A,_v),(_A,_w)))
if mibBuilder.loadTexts:alaVrrp3NotificationsGroup.setStatus(_B)
alaVrrp3MIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,28,2,3,1,1))
alaVrrp3MIBCompliance.setObjects(*((_A,_x),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:alaVrrp3MIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'alcatelIND1VRRP3MIB':alcatelIND1VRRP3MIB,'alaVrrp3Notifications':alaVrrp3Notifications,_v:alaVrrp3TrapNewMaster,_w:alaVrrp3TrapProtoError,'alaVrrp3Operations':alaVrrp3Operations,_T:alaVrrp3NotificationCntl,'alaVrrp3OperTable':alaVrrp3OperTable,'alaVrrp3OperEntry':alaVrrp3OperEntry,_H:alaVrrp3OperIpVersion,_I:alaVrrp3OperVrId,_U:alaVrrp3OperVirtualMacAddr,_V:alaVrrp3OperState,_W:alaVrrp3OperAdminState,_X:alaVrrp3OperPriority,_Y:alaVrrp3OperVersion,_Z:alaVrrp3OperIpAddrCount,_M:alaVrrp3OperMasterIpAddrType,_N:alaVrrp3OperMasterIpAddr,_a:alaVrrp3OperPrimaryIpAddrType,_b:alaVrrp3OperPrimaryIpAddr,_c:alaVrrp3OperAdvInterval,_d:alaVrrp3OperPreemptMode,_e:alaVrrp3OperAcceptMode,_f:alaVrrp3OperUpTime,_g:alaVrrp3OperRowStatus,'alaVrrp3AssoIpAddrTable':alaVrrp3AssoIpAddrTable,'alaVrrp3AssoIpAddrEntry':alaVrrp3AssoIpAddrEntry,_Q:alaVrrp3AssoIpAddrType,_R:alaVrrp3AssoIpAddr,_h:alaVrrp3AssoIpAddrRowStatus,_O:alaVrrp3TrapNewMasterReason,_P:alaVrrp3TrapProtoErrReason,'alaVrrp3Statistics':alaVrrp3Statistics,_i:alaVrrp3RouterChecksumErrors,_j:alaVrrp3RouterVersionErrors,_k:alaVrrp3RouterVrIdErrors,'alaVrrp3RouterStatsTable':alaVrrp3RouterStatsTable,'alaVrrp3RouterStatsEntry':alaVrrp3RouterStatsEntry,_l:alaVrrp3StatsBecomeMaster,_m:alaVrrp3StatsAdvertiseRcvd,_n:alaVrrp3StatsAdvIntervalErrors,_s:alaVrrp3StatsIpTtlErrors,_o:alaVrrp3StatsPriZeroPktsRcvd,_p:alaVrrp3StatsPriZeroPktsSent,_q:alaVrrp3StatsInvldTypePktsRcvd,_t:alaVrrp3StatsAddressListErrors,_r:alaVrrp3StatsInvldAuthType,_u:alaVrrp3StatsPacketLengthErrors,'alaVrrp3Conformance':alaVrrp3Conformance,'alaVrrp3MIBCompliances':alaVrrp3MIBCompliances,'alaVrrp3MIBCompliance':alaVrrp3MIBCompliance,'alaVrrp3MIBGroups':alaVrrp3MIBGroups,_x:alaVrrp3OperGroup,_y:alaVrrp3StatsGroup,_z:alaVrrp3TrapInfoGroup,_A0:alaVrrp3NotificationsGroup})