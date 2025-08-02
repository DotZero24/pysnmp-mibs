_t='ciscoCdstvServerMIBCachingObjectGroup'
_s='ciscoCdstvServerMIBStorageObjectGroup'
_r='ciscoCdstvServerMIBStreamingObjectGroup'
_q='ciscoCdstvServerMIBMainObjectGroup'
_p='cdstvServerCacheGroupID'
_o='cdstvServerCacheGroupName'
_n='cdstvServerVaultGroupID'
_m='cdstvServerVaultGroupName'
_l='cdstvServerFTPOutSessions'
_k='cdstvServerFTPOutBandwidth'
_j='cdstvServerFTPOutInterface'
_i='cdstvVaultLocalCopies'
_h='cdstvVaultMirrorCopies'
_g='cdstvServerStreamerIsCache'
_f='cdstvServerStreamGroupID'
_e='cdstvServerStreamGroupName'
_d='cdstvStreamJumboFramesEnable'
_c='cdstvServerEndingTransportPort'
_b='cdstvServerStartingTransportPort'
_a='cdstvServerNullStreamingEnable'
_Z='cdstvServerSourceAddressType'
_Y='cdstvServerCacheECN'
_X='cdstvServerCacheDSCP'
_W='cdstvServerTransportECN'
_V='cdstvServerTransportDSCP'
_U='cdstvServerOffloadEnable'
_T='cdstvCacheJumboFramesEnable'
_S='cdstvServerCachePort'
_R='cdstvServerSourceAddress'
_Q='cdstvServerTTL'
_P='cdstvServerHostname'
_O='cdstvServerGroupID'
_N='cdstvServerID'
_M='cdstvServerPartNo'
_L='cdstvServerRole'
_K='copies'
_J='SnmpAdminString'
_I='InetAddressType'
_H='InetAddress'
_G='Integer32'
_F='InetPortNumber'
_E='Unsigned32'
_D='read-only'
_C='read-write'
_B='CISCO-CDSTV-SERVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
Dscp,=mibBuilder.importSymbols('DIFFSERV-DSCP-TC','Dscp')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_H,_I,_F)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoCdstvServerMIB=ModuleIdentity((1,3,6,1,4,1,9,9,754))
if mibBuilder.loadTexts:ciscoCdstvServerMIB.setRevisions(('2012-12-12 00:00','2010-07-13 00:00'))
class CiscoCdstvEcn(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ect1',1),('ect0',2),('congestion',3),('disabled',4)))
_CiscoCdstvServerMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoCdstvServerMIBNotifs=_CiscoCdstvServerMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,754,0))
_CiscoCdstvServerMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCdstvServerMIBObjects=_CiscoCdstvServerMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,754,1))
_CdstvServerCommonObjects_ObjectIdentity=ObjectIdentity
cdstvServerCommonObjects=_CdstvServerCommonObjects_ObjectIdentity((1,3,6,1,4,1,9,9,754,1,1))
class _CdstvServerRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('isv',1),('vault',2),('streamer',3),('controller',4),('cachingserver',5),('recorder',6)))
_CdstvServerRole_Type.__name__=_G
_CdstvServerRole_Object=MibScalar
cdstvServerRole=_CdstvServerRole_Object((1,3,6,1,4,1,9,9,754,1,1,1),_CdstvServerRole_Type())
cdstvServerRole.setMaxAccess(_D)
if mibBuilder.loadTexts:cdstvServerRole.setStatus(_A)
_CdstvServerPartNo_Type=SnmpAdminString
_CdstvServerPartNo_Object=MibScalar
cdstvServerPartNo=_CdstvServerPartNo_Object((1,3,6,1,4,1,9,9,754,1,1,2),_CdstvServerPartNo_Type())
cdstvServerPartNo.setMaxAccess(_D)
if mibBuilder.loadTexts:cdstvServerPartNo.setStatus(_A)
_CdstvServerID_Type=Unsigned32
_CdstvServerID_Object=MibScalar
cdstvServerID=_CdstvServerID_Object((1,3,6,1,4,1,9,9,754,1,1,3),_CdstvServerID_Type())
cdstvServerID.setMaxAccess(_D)
if mibBuilder.loadTexts:cdstvServerID.setStatus(_A)
_CdstvServerGroupID_Type=Unsigned32
_CdstvServerGroupID_Object=MibScalar
cdstvServerGroupID=_CdstvServerGroupID_Object((1,3,6,1,4,1,9,9,754,1,1,4),_CdstvServerGroupID_Type())
cdstvServerGroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:cdstvServerGroupID.setStatus(_A)
class _CdstvServerHostname_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CdstvServerHostname_Type.__name__=_J
_CdstvServerHostname_Object=MibScalar
cdstvServerHostname=_CdstvServerHostname_Object((1,3,6,1,4,1,9,9,754,1,1,5),_CdstvServerHostname_Type())
cdstvServerHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvServerHostname.setStatus(_A)
class _CdstvServerTTL_Type(Unsigned32):defaultValue=16;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CdstvServerTTL_Type.__name__=_E
_CdstvServerTTL_Object=MibScalar
cdstvServerTTL=_CdstvServerTTL_Object((1,3,6,1,4,1,9,9,754,1,1,6),_CdstvServerTTL_Type())
cdstvServerTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvServerTTL.setStatus(_A)
if mibBuilder.loadTexts:cdstvServerTTL.setUnits('hops')
_CdstvServerDefaultStreamCacheSettings_ObjectIdentity=ObjectIdentity
cdstvServerDefaultStreamCacheSettings=_CdstvServerDefaultStreamCacheSettings_ObjectIdentity((1,3,6,1,4,1,9,9,754,1,1,7))
class _CdstvServerSourceAddressType_Type(InetAddressType):defaultValue=1
_CdstvServerSourceAddressType_Type.__name__=_I
_CdstvServerSourceAddressType_Object=MibScalar
cdstvServerSourceAddressType=_CdstvServerSourceAddressType_Object((1,3,6,1,4,1,9,9,754,1,1,7,1),_CdstvServerSourceAddressType_Type())
cdstvServerSourceAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvServerSourceAddressType.setStatus(_A)
class _CdstvServerSourceAddress_Type(InetAddress):defaultValue=OctetString('192.168.207.65')
_CdstvServerSourceAddress_Type.__name__=_H
_CdstvServerSourceAddress_Object=MibScalar
cdstvServerSourceAddress=_CdstvServerSourceAddress_Object((1,3,6,1,4,1,9,9,754,1,1,7,2),_CdstvServerSourceAddress_Type())
cdstvServerSourceAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvServerSourceAddress.setStatus(_A)
class _CdstvServerCachePort_Type(InetPortNumber):defaultValue=48879
_CdstvServerCachePort_Type.__name__=_F
_CdstvServerCachePort_Object=MibScalar
cdstvServerCachePort=_CdstvServerCachePort_Object((1,3,6,1,4,1,9,9,754,1,1,7,3),_CdstvServerCachePort_Type())
cdstvServerCachePort.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvServerCachePort.setStatus(_A)
_CdstvCacheJumboFramesEnable_Type=TruthValue
_CdstvCacheJumboFramesEnable_Object=MibScalar
cdstvCacheJumboFramesEnable=_CdstvCacheJumboFramesEnable_Object((1,3,6,1,4,1,9,9,754,1,1,8),_CdstvCacheJumboFramesEnable_Type())
cdstvCacheJumboFramesEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvCacheJumboFramesEnable.setStatus(_A)
_CdstvServerOffloadEnable_Type=TruthValue
_CdstvServerOffloadEnable_Object=MibScalar
cdstvServerOffloadEnable=_CdstvServerOffloadEnable_Object((1,3,6,1,4,1,9,9,754,1,1,9),_CdstvServerOffloadEnable_Type())
cdstvServerOffloadEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvServerOffloadEnable.setStatus(_A)
_CdstvServerTransportCacheIPPkts_ObjectIdentity=ObjectIdentity
cdstvServerTransportCacheIPPkts=_CdstvServerTransportCacheIPPkts_ObjectIdentity((1,3,6,1,4,1,9,9,754,1,1,10))
_CdstvServerTransportDSCP_Type=Dscp
_CdstvServerTransportDSCP_Object=MibScalar
cdstvServerTransportDSCP=_CdstvServerTransportDSCP_Object((1,3,6,1,4,1,9,9,754,1,1,10,1),_CdstvServerTransportDSCP_Type())
cdstvServerTransportDSCP.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvServerTransportDSCP.setStatus(_A)
_CdstvServerTransportECN_Type=CiscoCdstvEcn
_CdstvServerTransportECN_Object=MibScalar
cdstvServerTransportECN=_CdstvServerTransportECN_Object((1,3,6,1,4,1,9,9,754,1,1,10,2),_CdstvServerTransportECN_Type())
cdstvServerTransportECN.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvServerTransportECN.setStatus(_A)
_CdstvServerCacheDSCP_Type=Dscp
_CdstvServerCacheDSCP_Object=MibScalar
cdstvServerCacheDSCP=_CdstvServerCacheDSCP_Object((1,3,6,1,4,1,9,9,754,1,1,10,3),_CdstvServerCacheDSCP_Type())
cdstvServerCacheDSCP.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvServerCacheDSCP.setStatus(_A)
_CdstvServerCacheECN_Type=CiscoCdstvEcn
_CdstvServerCacheECN_Object=MibScalar
cdstvServerCacheECN=_CdstvServerCacheECN_Object((1,3,6,1,4,1,9,9,754,1,1,10,4),_CdstvServerCacheECN_Type())
cdstvServerCacheECN.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvServerCacheECN.setStatus(_A)
_CdstvServerNullStreamingEnable_Type=TruthValue
_CdstvServerNullStreamingEnable_Object=MibScalar
cdstvServerNullStreamingEnable=_CdstvServerNullStreamingEnable_Object((1,3,6,1,4,1,9,9,754,1,1,11),_CdstvServerNullStreamingEnable_Type())
cdstvServerNullStreamingEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvServerNullStreamingEnable.setStatus(_A)
_CdstvServerStreamingObjects_ObjectIdentity=ObjectIdentity
cdstvServerStreamingObjects=_CdstvServerStreamingObjects_ObjectIdentity((1,3,6,1,4,1,9,9,754,1,2))
class _CdstvServerStartingTransportPort_Type(InetPortNumber):defaultValue=48879
_CdstvServerStartingTransportPort_Type.__name__=_F
_CdstvServerStartingTransportPort_Object=MibScalar
cdstvServerStartingTransportPort=_CdstvServerStartingTransportPort_Object((1,3,6,1,4,1,9,9,754,1,2,1),_CdstvServerStartingTransportPort_Type())
cdstvServerStartingTransportPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvServerStartingTransportPort.setStatus(_A)
_CdstvServerEndingTransportPort_Type=InetPortNumber
_CdstvServerEndingTransportPort_Object=MibScalar
cdstvServerEndingTransportPort=_CdstvServerEndingTransportPort_Object((1,3,6,1,4,1,9,9,754,1,2,2),_CdstvServerEndingTransportPort_Type())
cdstvServerEndingTransportPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvServerEndingTransportPort.setStatus(_A)
_CdstvStreamJumboFramesEnable_Type=TruthValue
_CdstvStreamJumboFramesEnable_Object=MibScalar
cdstvStreamJumboFramesEnable=_CdstvStreamJumboFramesEnable_Object((1,3,6,1,4,1,9,9,754,1,2,3),_CdstvStreamJumboFramesEnable_Type())
cdstvStreamJumboFramesEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvStreamJumboFramesEnable.setStatus(_A)
_CdstvServerStreamGroupInfo_ObjectIdentity=ObjectIdentity
cdstvServerStreamGroupInfo=_CdstvServerStreamGroupInfo_ObjectIdentity((1,3,6,1,4,1,9,9,754,1,2,4))
_CdstvServerStreamGroupName_Type=SnmpAdminString
_CdstvServerStreamGroupName_Object=MibScalar
cdstvServerStreamGroupName=_CdstvServerStreamGroupName_Object((1,3,6,1,4,1,9,9,754,1,2,4,1),_CdstvServerStreamGroupName_Type())
cdstvServerStreamGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:cdstvServerStreamGroupName.setStatus(_A)
_CdstvServerStreamGroupID_Type=Unsigned32
_CdstvServerStreamGroupID_Object=MibScalar
cdstvServerStreamGroupID=_CdstvServerStreamGroupID_Object((1,3,6,1,4,1,9,9,754,1,2,4,2),_CdstvServerStreamGroupID_Type())
cdstvServerStreamGroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:cdstvServerStreamGroupID.setStatus(_A)
_CdstvServerStreamerIsCache_Type=TruthValue
_CdstvServerStreamerIsCache_Object=MibScalar
cdstvServerStreamerIsCache=_CdstvServerStreamerIsCache_Object((1,3,6,1,4,1,9,9,754,1,2,4,3),_CdstvServerStreamerIsCache_Type())
cdstvServerStreamerIsCache.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvServerStreamerIsCache.setStatus(_A)
_CdstvServerStorageObjects_ObjectIdentity=ObjectIdentity
cdstvServerStorageObjects=_CdstvServerStorageObjects_ObjectIdentity((1,3,6,1,4,1,9,9,754,1,3))
class _CdstvVaultMirrorCopies_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_CdstvVaultMirrorCopies_Type.__name__=_E
_CdstvVaultMirrorCopies_Object=MibScalar
cdstvVaultMirrorCopies=_CdstvVaultMirrorCopies_Object((1,3,6,1,4,1,9,9,754,1,3,1),_CdstvVaultMirrorCopies_Type())
cdstvVaultMirrorCopies.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvVaultMirrorCopies.setStatus(_A)
if mibBuilder.loadTexts:cdstvVaultMirrorCopies.setUnits(_K)
class _CdstvVaultLocalCopies_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_CdstvVaultLocalCopies_Type.__name__=_E
_CdstvVaultLocalCopies_Object=MibScalar
cdstvVaultLocalCopies=_CdstvVaultLocalCopies_Object((1,3,6,1,4,1,9,9,754,1,3,2),_CdstvVaultLocalCopies_Type())
cdstvVaultLocalCopies.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvVaultLocalCopies.setStatus(_A)
if mibBuilder.loadTexts:cdstvVaultLocalCopies.setUnits(_K)
_CdstvServerFTPOutSettings_ObjectIdentity=ObjectIdentity
cdstvServerFTPOutSettings=_CdstvServerFTPOutSettings_ObjectIdentity((1,3,6,1,4,1,9,9,754,1,3,3))
class _CdstvServerFTPOutInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('management',1),('ingest',2)))
_CdstvServerFTPOutInterface_Type.__name__=_G
_CdstvServerFTPOutInterface_Object=MibScalar
cdstvServerFTPOutInterface=_CdstvServerFTPOutInterface_Object((1,3,6,1,4,1,9,9,754,1,3,3,1),_CdstvServerFTPOutInterface_Type())
cdstvServerFTPOutInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvServerFTPOutInterface.setStatus(_A)
class _CdstvServerFTPOutBandwidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_CdstvServerFTPOutBandwidth_Type.__name__=_E
_CdstvServerFTPOutBandwidth_Object=MibScalar
cdstvServerFTPOutBandwidth=_CdstvServerFTPOutBandwidth_Object((1,3,6,1,4,1,9,9,754,1,3,3,2),_CdstvServerFTPOutBandwidth_Type())
cdstvServerFTPOutBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvServerFTPOutBandwidth.setStatus(_A)
if mibBuilder.loadTexts:cdstvServerFTPOutBandwidth.setUnits('Mbps')
class _CdstvServerFTPOutSessions_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CdstvServerFTPOutSessions_Type.__name__=_E
_CdstvServerFTPOutSessions_Object=MibScalar
cdstvServerFTPOutSessions=_CdstvServerFTPOutSessions_Object((1,3,6,1,4,1,9,9,754,1,3,3,3),_CdstvServerFTPOutSessions_Type())
cdstvServerFTPOutSessions.setMaxAccess(_C)
if mibBuilder.loadTexts:cdstvServerFTPOutSessions.setStatus(_A)
if mibBuilder.loadTexts:cdstvServerFTPOutSessions.setUnits('sessions')
_CdstvServerVaultGroupInformation_ObjectIdentity=ObjectIdentity
cdstvServerVaultGroupInformation=_CdstvServerVaultGroupInformation_ObjectIdentity((1,3,6,1,4,1,9,9,754,1,3,4))
_CdstvServerVaultGroupName_Type=SnmpAdminString
_CdstvServerVaultGroupName_Object=MibScalar
cdstvServerVaultGroupName=_CdstvServerVaultGroupName_Object((1,3,6,1,4,1,9,9,754,1,3,4,1),_CdstvServerVaultGroupName_Type())
cdstvServerVaultGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:cdstvServerVaultGroupName.setStatus(_A)
_CdstvServerVaultGroupID_Type=Unsigned32
_CdstvServerVaultGroupID_Object=MibScalar
cdstvServerVaultGroupID=_CdstvServerVaultGroupID_Object((1,3,6,1,4,1,9,9,754,1,3,4,2),_CdstvServerVaultGroupID_Type())
cdstvServerVaultGroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:cdstvServerVaultGroupID.setStatus(_A)
_CdstvServerCachingObjects_ObjectIdentity=ObjectIdentity
cdstvServerCachingObjects=_CdstvServerCachingObjects_ObjectIdentity((1,3,6,1,4,1,9,9,754,1,4))
_CdstvServerCacheGroupInformation_ObjectIdentity=ObjectIdentity
cdstvServerCacheGroupInformation=_CdstvServerCacheGroupInformation_ObjectIdentity((1,3,6,1,4,1,9,9,754,1,4,1))
_CdstvServerCacheGroupName_Type=SnmpAdminString
_CdstvServerCacheGroupName_Object=MibScalar
cdstvServerCacheGroupName=_CdstvServerCacheGroupName_Object((1,3,6,1,4,1,9,9,754,1,4,1,1),_CdstvServerCacheGroupName_Type())
cdstvServerCacheGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:cdstvServerCacheGroupName.setStatus(_A)
_CdstvServerCacheGroupID_Type=Unsigned32
_CdstvServerCacheGroupID_Object=MibScalar
cdstvServerCacheGroupID=_CdstvServerCacheGroupID_Object((1,3,6,1,4,1,9,9,754,1,4,1,2),_CdstvServerCacheGroupID_Type())
cdstvServerCacheGroupID.setMaxAccess(_D)
if mibBuilder.loadTexts:cdstvServerCacheGroupID.setStatus(_A)
_CiscoCdstvServerMIBConform_ObjectIdentity=ObjectIdentity
ciscoCdstvServerMIBConform=_CiscoCdstvServerMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,754,2))
_CiscoCdstvServerMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCdstvServerMIBCompliances=_CiscoCdstvServerMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,754,2,1))
_CiscoCdstvServerMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCdstvServerMIBGroups=_CiscoCdstvServerMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,754,2,2))
ciscoCdstvServerMIBMainObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,754,2,2,1))
ciscoCdstvServerMIBMainObjectGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:ciscoCdstvServerMIBMainObjectGroup.setStatus(_A)
ciscoCdstvServerMIBStreamingObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,754,2,2,2))
ciscoCdstvServerMIBStreamingObjectGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:ciscoCdstvServerMIBStreamingObjectGroup.setStatus(_A)
ciscoCdstvServerMIBStorageObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,754,2,2,3))
ciscoCdstvServerMIBStorageObjectGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:ciscoCdstvServerMIBStorageObjectGroup.setStatus(_A)
ciscoCdstvServerMIBCachingObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,754,2,2,4))
ciscoCdstvServerMIBCachingObjectGroup.setObjects(*((_B,_o),(_B,_p)))
if mibBuilder.loadTexts:ciscoCdstvServerMIBCachingObjectGroup.setStatus(_A)
ciscoCdstvServerMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,754,2,1,1))
ciscoCdstvServerMIBCompliance.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:ciscoCdstvServerMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CiscoCdstvEcn':CiscoCdstvEcn,'ciscoCdstvServerMIB':ciscoCdstvServerMIB,'ciscoCdstvServerMIBNotifs':ciscoCdstvServerMIBNotifs,'ciscoCdstvServerMIBObjects':ciscoCdstvServerMIBObjects,'cdstvServerCommonObjects':cdstvServerCommonObjects,_L:cdstvServerRole,_M:cdstvServerPartNo,_N:cdstvServerID,_O:cdstvServerGroupID,_P:cdstvServerHostname,_Q:cdstvServerTTL,'cdstvServerDefaultStreamCacheSettings':cdstvServerDefaultStreamCacheSettings,_Z:cdstvServerSourceAddressType,_R:cdstvServerSourceAddress,_S:cdstvServerCachePort,_T:cdstvCacheJumboFramesEnable,_U:cdstvServerOffloadEnable,'cdstvServerTransportCacheIPPkts':cdstvServerTransportCacheIPPkts,_V:cdstvServerTransportDSCP,_W:cdstvServerTransportECN,_X:cdstvServerCacheDSCP,_Y:cdstvServerCacheECN,_a:cdstvServerNullStreamingEnable,'cdstvServerStreamingObjects':cdstvServerStreamingObjects,_b:cdstvServerStartingTransportPort,_c:cdstvServerEndingTransportPort,_d:cdstvStreamJumboFramesEnable,'cdstvServerStreamGroupInfo':cdstvServerStreamGroupInfo,_e:cdstvServerStreamGroupName,_f:cdstvServerStreamGroupID,_g:cdstvServerStreamerIsCache,'cdstvServerStorageObjects':cdstvServerStorageObjects,_h:cdstvVaultMirrorCopies,_i:cdstvVaultLocalCopies,'cdstvServerFTPOutSettings':cdstvServerFTPOutSettings,_j:cdstvServerFTPOutInterface,_k:cdstvServerFTPOutBandwidth,_l:cdstvServerFTPOutSessions,'cdstvServerVaultGroupInformation':cdstvServerVaultGroupInformation,_m:cdstvServerVaultGroupName,_n:cdstvServerVaultGroupID,'cdstvServerCachingObjects':cdstvServerCachingObjects,'cdstvServerCacheGroupInformation':cdstvServerCacheGroupInformation,_o:cdstvServerCacheGroupName,_p:cdstvServerCacheGroupID,'ciscoCdstvServerMIBConform':ciscoCdstvServerMIBConform,'ciscoCdstvServerMIBCompliances':ciscoCdstvServerMIBCompliances,'ciscoCdstvServerMIBCompliance':ciscoCdstvServerMIBCompliance,'ciscoCdstvServerMIBGroups':ciscoCdstvServerMIBGroups,_q:ciscoCdstvServerMIBMainObjectGroup,_r:ciscoCdstvServerMIBStreamingObjectGroup,_s:ciscoCdstvServerMIBStorageObjectGroup,_t:ciscoCdstvServerMIBCachingObjectGroup})