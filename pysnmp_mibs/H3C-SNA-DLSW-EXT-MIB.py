_W='h3cdeTConnTcpConfigEntry'
_V='h3cdeTConnOperEntry'
_U='h3cdeTConnConfigEntry'
_T='h3cdeEBMacMapIndex'
_S='h3cdeRchCacheIndex'
_R='h3cdeBridgeNumIndex'
_Q='disabled'
_P='enabled'
_O='packets'
_N='InetAddress'
_M='not-accessible'
_L='MacAddressNC'
_K='OctetString'
_J='H3C-SNA-DLSW-EXT-MIB'
_I='ifIndex'
_H='IF-MIB'
_G='seconds'
_F='milliseconds'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
LFSize,MacAddressNC,TAddress,dlswTConnConfigEntry,dlswTConnOperEntry,dlswTConnTcpConfigEntry=mibBuilder.importSymbols('DLSW-MIB','LFSize',_L,'TAddress','dlswTConnConfigEntry','dlswTConnOperEntry','dlswTConnTcpConfigEntry')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_H,_I)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_N,'InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cDlswExt=ModuleIdentity((1,3,6,1,4,1,2011,10,2,62))
if mibBuilder.loadTexts:h3cDlswExt.setRevisions(('2005-07-20 19:00',))
_H3cDlswExtMIBObjects_ObjectIdentity=ObjectIdentity
h3cDlswExtMIBObjects=_H3cDlswExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,62,1))
_H3cdeNode_ObjectIdentity=ObjectIdentity
h3cdeNode=_H3cdeNode_ObjectIdentity((1,3,6,1,4,1,2011,10,2,62,1,1))
class _H3cdeNodeVendorID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_H3cdeNodeVendorID_Type.__name__=_K
_H3cdeNodeVendorID_Object=MibScalar
h3cdeNodeVendorID=_H3cdeNodeVendorID_Object((1,3,6,1,4,1,2011,10,2,62,1,1,1),_H3cdeNodeVendorID_Type())
h3cdeNodeVendorID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodeVendorID.setStatus(_A)
_H3cdeNodeIpAddrType_Type=InetAddressType
_H3cdeNodeIpAddrType_Object=MibScalar
h3cdeNodeIpAddrType=_H3cdeNodeIpAddrType_Object((1,3,6,1,4,1,2011,10,2,62,1,1,2),_H3cdeNodeIpAddrType_Type())
h3cdeNodeIpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodeIpAddrType.setStatus(_A)
class _H3cdeNodeLocalAddr_Type(InetAddress):defaultHexValue=''
_H3cdeNodeLocalAddr_Type.__name__=_N
_H3cdeNodeLocalAddr_Object=MibScalar
h3cdeNodeLocalAddr=_H3cdeNodeLocalAddr_Object((1,3,6,1,4,1,2011,10,2,62,1,1,3),_H3cdeNodeLocalAddr_Type())
h3cdeNodeLocalAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodeLocalAddr.setStatus(_A)
class _H3cdeNodePriority_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5),ValueRangeConstraint(65535,65535))
_H3cdeNodePriority_Type.__name__=_C
_H3cdeNodePriority_Object=MibScalar
h3cdeNodePriority=_H3cdeNodePriority_Object((1,3,6,1,4,1,2011,10,2,62,1,1,4),_H3cdeNodePriority_Type())
h3cdeNodePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodePriority.setStatus(_A)
class _H3cdeNodeInitPacingWindow_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000),ValueRangeConstraint(65535,65535))
_H3cdeNodeInitPacingWindow_Type.__name__=_C
_H3cdeNodeInitPacingWindow_Object=MibScalar
h3cdeNodeInitPacingWindow=_H3cdeNodeInitPacingWindow_Object((1,3,6,1,4,1,2011,10,2,62,1,1,5),_H3cdeNodeInitPacingWindow_Type())
h3cdeNodeInitPacingWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodeInitPacingWindow.setStatus(_A)
if mibBuilder.loadTexts:h3cdeNodeInitPacingWindow.setUnits(_O)
class _H3cdeNodeMaxPacingWindow_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000),ValueRangeConstraint(65535,65535))
_H3cdeNodeMaxPacingWindow_Type.__name__=_C
_H3cdeNodeMaxPacingWindow_Object=MibScalar
h3cdeNodeMaxPacingWindow=_H3cdeNodeMaxPacingWindow_Object((1,3,6,1,4,1,2011,10,2,62,1,1,6),_H3cdeNodeMaxPacingWindow_Type())
h3cdeNodeMaxPacingWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodeMaxPacingWindow.setStatus(_A)
if mibBuilder.loadTexts:h3cdeNodeMaxPacingWindow.setUnits(_O)
class _H3cdeNodeKeepAliveInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000),ValueRangeConstraint(65535,65535))
_H3cdeNodeKeepAliveInterval_Type.__name__=_C
_H3cdeNodeKeepAliveInterval_Object=MibScalar
h3cdeNodeKeepAliveInterval=_H3cdeNodeKeepAliveInterval_Object((1,3,6,1,4,1,2011,10,2,62,1,1,7),_H3cdeNodeKeepAliveInterval_Type())
h3cdeNodeKeepAliveInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodeKeepAliveInterval.setStatus(_A)
if mibBuilder.loadTexts:h3cdeNodeKeepAliveInterval.setUnits(_G)
class _H3cdeNodePermitDynamic_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,65535)));namedValues=NamedValues(*(('permitDynamic',1),('forbidDynamic',2),('unknown',65535)))
_H3cdeNodePermitDynamic_Type.__name__=_C
_H3cdeNodePermitDynamic_Object=MibScalar
h3cdeNodePermitDynamic=_H3cdeNodePermitDynamic_Object((1,3,6,1,4,1,2011,10,2,62,1,1,8),_H3cdeNodePermitDynamic_Type())
h3cdeNodePermitDynamic.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodePermitDynamic.setStatus(_A)
class _H3cdeNodeConnTimeout_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cdeNodeConnTimeout_Type.__name__=_C
_H3cdeNodeConnTimeout_Object=MibScalar
h3cdeNodeConnTimeout=_H3cdeNodeConnTimeout_Object((1,3,6,1,4,1,2011,10,2,62,1,1,9),_H3cdeNodeConnTimeout_Type())
h3cdeNodeConnTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodeConnTimeout.setStatus(_A)
if mibBuilder.loadTexts:h3cdeNodeConnTimeout.setUnits(_G)
class _H3cdeNodeLocalPendTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cdeNodeLocalPendTimeout_Type.__name__=_C
_H3cdeNodeLocalPendTimeout_Object=MibScalar
h3cdeNodeLocalPendTimeout=_H3cdeNodeLocalPendTimeout_Object((1,3,6,1,4,1,2011,10,2,62,1,1,10),_H3cdeNodeLocalPendTimeout_Type())
h3cdeNodeLocalPendTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodeLocalPendTimeout.setStatus(_A)
if mibBuilder.loadTexts:h3cdeNodeLocalPendTimeout.setUnits(_G)
class _H3cdeNodeRemotePendTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cdeNodeRemotePendTimeout_Type.__name__=_C
_H3cdeNodeRemotePendTimeout_Object=MibScalar
h3cdeNodeRemotePendTimeout=_H3cdeNodeRemotePendTimeout_Object((1,3,6,1,4,1,2011,10,2,62,1,1,11),_H3cdeNodeRemotePendTimeout_Type())
h3cdeNodeRemotePendTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodeRemotePendTimeout.setStatus(_A)
if mibBuilder.loadTexts:h3cdeNodeRemotePendTimeout.setUnits(_G)
class _H3cdeNodeSnaCacheTimeout_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cdeNodeSnaCacheTimeout_Type.__name__=_C
_H3cdeNodeSnaCacheTimeout_Object=MibScalar
h3cdeNodeSnaCacheTimeout=_H3cdeNodeSnaCacheTimeout_Object((1,3,6,1,4,1,2011,10,2,62,1,1,12),_H3cdeNodeSnaCacheTimeout_Type())
h3cdeNodeSnaCacheTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodeSnaCacheTimeout.setStatus(_A)
if mibBuilder.loadTexts:h3cdeNodeSnaCacheTimeout.setUnits(_G)
class _H3cdeNodeExplorerTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cdeNodeExplorerTimeout_Type.__name__=_C
_H3cdeNodeExplorerTimeout_Object=MibScalar
h3cdeNodeExplorerTimeout=_H3cdeNodeExplorerTimeout_Object((1,3,6,1,4,1,2011,10,2,62,1,1,13),_H3cdeNodeExplorerTimeout_Type())
h3cdeNodeExplorerTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodeExplorerTimeout.setStatus(_A)
if mibBuilder.loadTexts:h3cdeNodeExplorerTimeout.setUnits(_G)
class _H3cdeNodeExplorerWaitTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cdeNodeExplorerWaitTimeout_Type.__name__=_C
_H3cdeNodeExplorerWaitTimeout_Object=MibScalar
h3cdeNodeExplorerWaitTimeout=_H3cdeNodeExplorerWaitTimeout_Object((1,3,6,1,4,1,2011,10,2,62,1,1,14),_H3cdeNodeExplorerWaitTimeout_Type())
h3cdeNodeExplorerWaitTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodeExplorerWaitTimeout.setStatus(_A)
if mibBuilder.loadTexts:h3cdeNodeExplorerWaitTimeout.setUnits(_G)
class _H3cdeNodeConfigSapList_Type(OctetString):defaultHexValue='FF000000000000000000000000000000';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_H3cdeNodeConfigSapList_Type.__name__=_K
_H3cdeNodeConfigSapList_Object=MibScalar
h3cdeNodeConfigSapList=_H3cdeNodeConfigSapList_Object((1,3,6,1,4,1,2011,10,2,62,1,1,15),_H3cdeNodeConfigSapList_Type())
h3cdeNodeConfigSapList.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodeConfigSapList.setStatus(_A)
class _H3cdeNodeMaxTransmission_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_H3cdeNodeMaxTransmission_Type.__name__=_C
_H3cdeNodeMaxTransmission_Object=MibScalar
h3cdeNodeMaxTransmission=_H3cdeNodeMaxTransmission_Object((1,3,6,1,4,1,2011,10,2,62,1,1,16),_H3cdeNodeMaxTransmission_Type())
h3cdeNodeMaxTransmission.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodeMaxTransmission.setStatus(_A)
class _H3cdeNodeMulticastStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_H3cdeNodeMulticastStatus_Type.__name__=_C
_H3cdeNodeMulticastStatus_Object=MibScalar
h3cdeNodeMulticastStatus=_H3cdeNodeMulticastStatus_Object((1,3,6,1,4,1,2011,10,2,62,1,1,17),_H3cdeNodeMulticastStatus_Type())
h3cdeNodeMulticastStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodeMulticastStatus.setStatus(_A)
_H3cdeNodeMulticastAddress_Type=InetAddress
_H3cdeNodeMulticastAddress_Object=MibScalar
h3cdeNodeMulticastAddress=_H3cdeNodeMulticastAddress_Object((1,3,6,1,4,1,2011,10,2,62,1,1,18),_H3cdeNodeMulticastAddress_Type())
h3cdeNodeMulticastAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodeMulticastAddress.setStatus(_A)
class _H3cdeNodeResetTcpAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_H3cdeNodeResetTcpAll_Type.__name__=_C
_H3cdeNodeResetTcpAll_Object=MibScalar
h3cdeNodeResetTcpAll=_H3cdeNodeResetTcpAll_Object((1,3,6,1,4,1,2011,10,2,62,1,1,19),_H3cdeNodeResetTcpAll_Type())
h3cdeNodeResetTcpAll.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodeResetTcpAll.setStatus(_A)
class _H3cdeNodeStCapTcpNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cdeNodeStCapTcpNum_Type.__name__=_C
_H3cdeNodeStCapTcpNum_Object=MibScalar
h3cdeNodeStCapTcpNum=_H3cdeNodeStCapTcpNum_Object((1,3,6,1,4,1,2011,10,2,62,1,1,20),_H3cdeNodeStCapTcpNum_Type())
h3cdeNodeStCapTcpNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodeStCapTcpNum.setStatus(_A)
class _H3cdeNodeTcpQueueMax_Type(Integer32):defaultValue=200
_H3cdeNodeTcpQueueMax_Type.__name__=_C
_H3cdeNodeTcpQueueMax_Object=MibScalar
h3cdeNodeTcpQueueMax=_H3cdeNodeTcpQueueMax_Object((1,3,6,1,4,1,2011,10,2,62,1,1,21),_H3cdeNodeTcpQueueMax_Type())
h3cdeNodeTcpQueueMax.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cdeNodeTcpQueueMax.setStatus(_A)
_H3cdeTConn_ObjectIdentity=ObjectIdentity
h3cdeTConn=_H3cdeTConn_ObjectIdentity((1,3,6,1,4,1,2011,10,2,62,1,2))
_H3cdeTConnConfigTable_Object=MibTable
h3cdeTConnConfigTable=_H3cdeTConnConfigTable_Object((1,3,6,1,4,1,2011,10,2,62,1,2,1))
if mibBuilder.loadTexts:h3cdeTConnConfigTable.setStatus(_A)
_H3cdeTConnConfigEntry_Object=MibTableRow
h3cdeTConnConfigEntry=_H3cdeTConnConfigEntry_Object((1,3,6,1,4,1,2011,10,2,62,1,2,1,1))
if mibBuilder.loadTexts:h3cdeTConnConfigEntry.setStatus(_A)
class _H3cdeTConnConfigVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_H3cdeTConnConfigVersion_Type.__name__=_K
_H3cdeTConnConfigVersion_Object=MibTableColumn
h3cdeTConnConfigVersion=_H3cdeTConnConfigVersion_Object((1,3,6,1,4,1,2011,10,2,62,1,2,1,1,1),_H3cdeTConnConfigVersion_Type())
h3cdeTConnConfigVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeTConnConfigVersion.setStatus(_A)
class _H3cdeTConnConfigPriority_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_H3cdeTConnConfigPriority_Type.__name__=_C
_H3cdeTConnConfigPriority_Object=MibTableColumn
h3cdeTConnConfigPriority=_H3cdeTConnConfigPriority_Object((1,3,6,1,4,1,2011,10,2,62,1,2,1,1,2),_H3cdeTConnConfigPriority_Type())
h3cdeTConnConfigPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeTConnConfigPriority.setStatus(_A)
_H3cdeTConnConfigLfSize_Type=LFSize
_H3cdeTConnConfigLfSize_Object=MibTableColumn
h3cdeTConnConfigLfSize=_H3cdeTConnConfigLfSize_Object((1,3,6,1,4,1,2011,10,2,62,1,2,1,1,3),_H3cdeTConnConfigLfSize_Type())
h3cdeTConnConfigLfSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeTConnConfigLfSize.setStatus(_A)
class _H3cdeTConnConfigKeepaliveIntval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1200))
_H3cdeTConnConfigKeepaliveIntval_Type.__name__=_C
_H3cdeTConnConfigKeepaliveIntval_Object=MibTableColumn
h3cdeTConnConfigKeepaliveIntval=_H3cdeTConnConfigKeepaliveIntval_Object((1,3,6,1,4,1,2011,10,2,62,1,2,1,1,4),_H3cdeTConnConfigKeepaliveIntval_Type())
h3cdeTConnConfigKeepaliveIntval.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeTConnConfigKeepaliveIntval.setStatus(_A)
if mibBuilder.loadTexts:h3cdeTConnConfigKeepaliveIntval.setUnits(_G)
class _H3cdeTConnConfigBackup_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_H3cdeTConnConfigBackup_Type.__name__=_C
_H3cdeTConnConfigBackup_Object=MibTableColumn
h3cdeTConnConfigBackup=_H3cdeTConnConfigBackup_Object((1,3,6,1,4,1,2011,10,2,62,1,2,1,1,5),_H3cdeTConnConfigBackup_Type())
h3cdeTConnConfigBackup.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeTConnConfigBackup.setStatus(_A)
_H3cdeTConnConfigBackupTAddr_Type=TAddress
_H3cdeTConnConfigBackupTAddr_Object=MibTableColumn
h3cdeTConnConfigBackupTAddr=_H3cdeTConnConfigBackupTAddr_Object((1,3,6,1,4,1,2011,10,2,62,1,2,1,1,6),_H3cdeTConnConfigBackupTAddr_Type())
h3cdeTConnConfigBackupTAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeTConnConfigBackupTAddr.setStatus(_A)
class _H3cdeTConnConfigBackupLinger_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_H3cdeTConnConfigBackupLinger_Type.__name__=_C
_H3cdeTConnConfigBackupLinger_Object=MibTableColumn
h3cdeTConnConfigBackupLinger=_H3cdeTConnConfigBackupLinger_Object((1,3,6,1,4,1,2011,10,2,62,1,2,1,1,7),_H3cdeTConnConfigBackupLinger_Type())
h3cdeTConnConfigBackupLinger.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeTConnConfigBackupLinger.setStatus(_A)
if mibBuilder.loadTexts:h3cdeTConnConfigBackupLinger.setUnits('minutes')
_H3cdeTConnOperTable_Object=MibTable
h3cdeTConnOperTable=_H3cdeTConnOperTable_Object((1,3,6,1,4,1,2011,10,2,62,1,2,2))
if mibBuilder.loadTexts:h3cdeTConnOperTable.setStatus(_A)
_H3cdeTConnOperEntry_Object=MibTableRow
h3cdeTConnOperEntry=_H3cdeTConnOperEntry_Object((1,3,6,1,4,1,2011,10,2,62,1,2,2,1))
if mibBuilder.loadTexts:h3cdeTConnOperEntry.setStatus(_A)
class _H3cdeTConnOperPeerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('configured',1),('learningDynamic',2),('other',3)))
_H3cdeTConnOperPeerType_Type.__name__=_C
_H3cdeTConnOperPeerType_Object=MibTableColumn
h3cdeTConnOperPeerType=_H3cdeTConnOperPeerType_Object((1,3,6,1,4,1,2011,10,2,62,1,2,2,1,1),_H3cdeTConnOperPeerType_Type())
h3cdeTConnOperPeerType.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cdeTConnOperPeerType.setStatus(_A)
_H3cdeTConnOperVendorID_Type=OctetString
_H3cdeTConnOperVendorID_Object=MibTableColumn
h3cdeTConnOperVendorID=_H3cdeTConnOperVendorID_Object((1,3,6,1,4,1,2011,10,2,62,1,2,2,1,2),_H3cdeTConnOperVendorID_Type())
h3cdeTConnOperVendorID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cdeTConnOperVendorID.setStatus(_A)
_H3cdeTConnOperVersionString_Type=OctetString
_H3cdeTConnOperVersionString_Object=MibTableColumn
h3cdeTConnOperVersionString=_H3cdeTConnOperVersionString_Object((1,3,6,1,4,1,2011,10,2,62,1,2,2,1,3),_H3cdeTConnOperVersionString_Type())
h3cdeTConnOperVersionString.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cdeTConnOperVersionString.setStatus(_A)
_H3cdeTConnOperUpTime_Type=TimeTicks
_H3cdeTConnOperUpTime_Object=MibTableColumn
h3cdeTConnOperUpTime=_H3cdeTConnOperUpTime_Object((1,3,6,1,4,1,2011,10,2,62,1,2,2,1,4),_H3cdeTConnOperUpTime_Type())
h3cdeTConnOperUpTime.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cdeTConnOperUpTime.setStatus(_A)
_H3cdeTConnOperMulticastAddress_Type=TAddress
_H3cdeTConnOperMulticastAddress_Object=MibTableColumn
h3cdeTConnOperMulticastAddress=_H3cdeTConnOperMulticastAddress_Object((1,3,6,1,4,1,2011,10,2,62,1,2,2,1,5),_H3cdeTConnOperMulticastAddress_Type())
h3cdeTConnOperMulticastAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cdeTConnOperMulticastAddress.setStatus(_A)
_H3cdeTConnOperStCapTcpNumber_Type=Integer32
_H3cdeTConnOperStCapTcpNumber_Object=MibTableColumn
h3cdeTConnOperStCapTcpNumber=_H3cdeTConnOperStCapTcpNumber_Object((1,3,6,1,4,1,2011,10,2,62,1,2,2,1,6),_H3cdeTConnOperStCapTcpNumber_Type())
h3cdeTConnOperStCapTcpNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cdeTConnOperStCapTcpNumber.setStatus(_A)
_H3cdeTConnOperRecvPkts_Type=Counter32
_H3cdeTConnOperRecvPkts_Object=MibTableColumn
h3cdeTConnOperRecvPkts=_H3cdeTConnOperRecvPkts_Object((1,3,6,1,4,1,2011,10,2,62,1,2,2,1,7),_H3cdeTConnOperRecvPkts_Type())
h3cdeTConnOperRecvPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cdeTConnOperRecvPkts.setStatus(_A)
_H3cdeTConnOperSendPkts_Type=Counter32
_H3cdeTConnOperSendPkts_Object=MibTableColumn
h3cdeTConnOperSendPkts=_H3cdeTConnOperSendPkts_Object((1,3,6,1,4,1,2011,10,2,62,1,2,2,1,8),_H3cdeTConnOperSendPkts_Type())
h3cdeTConnOperSendPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cdeTConnOperSendPkts.setStatus(_A)
_H3cdeTConnOperDropPkts_Type=Counter32
_H3cdeTConnOperDropPkts_Object=MibTableColumn
h3cdeTConnOperDropPkts=_H3cdeTConnOperDropPkts_Object((1,3,6,1,4,1,2011,10,2,62,1,2,2,1,9),_H3cdeTConnOperDropPkts_Type())
h3cdeTConnOperDropPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cdeTConnOperDropPkts.setStatus(_A)
_H3cdeTConnTcpConfigTable_Object=MibTable
h3cdeTConnTcpConfigTable=_H3cdeTConnTcpConfigTable_Object((1,3,6,1,4,1,2011,10,2,62,1,2,3))
if mibBuilder.loadTexts:h3cdeTConnTcpConfigTable.setStatus(_A)
_H3cdeTConnTcpConfigEntry_Object=MibTableRow
h3cdeTConnTcpConfigEntry=_H3cdeTConnTcpConfigEntry_Object((1,3,6,1,4,1,2011,10,2,62,1,2,3,1))
if mibBuilder.loadTexts:h3cdeTConnTcpConfigEntry.setStatus(_A)
class _H3cdeTConnTcpConfigQueueMax_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,2000))
_H3cdeTConnTcpConfigQueueMax_Type.__name__=_C
_H3cdeTConnTcpConfigQueueMax_Object=MibTableColumn
h3cdeTConnTcpConfigQueueMax=_H3cdeTConnTcpConfigQueueMax_Object((1,3,6,1,4,1,2011,10,2,62,1,2,3,1,1),_H3cdeTConnTcpConfigQueueMax_Type())
h3cdeTConnTcpConfigQueueMax.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeTConnTcpConfigQueueMax.setStatus(_A)
_H3cdeBridge_ObjectIdentity=ObjectIdentity
h3cdeBridge=_H3cdeBridge_ObjectIdentity((1,3,6,1,4,1,2011,10,2,62,1,3))
_H3cdeBridgeTable_Object=MibTable
h3cdeBridgeTable=_H3cdeBridgeTable_Object((1,3,6,1,4,1,2011,10,2,62,1,3,1))
if mibBuilder.loadTexts:h3cdeBridgeTable.setStatus(_A)
_H3cdeBridgeEntry_Object=MibTableRow
h3cdeBridgeEntry=_H3cdeBridgeEntry_Object((1,3,6,1,4,1,2011,10,2,62,1,3,1,1))
h3cdeBridgeEntry.setIndexNames((0,_J,_R))
if mibBuilder.loadTexts:h3cdeBridgeEntry.setStatus(_A)
class _H3cdeBridgeNumIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_H3cdeBridgeNumIndex_Type.__name__=_C
_H3cdeBridgeNumIndex_Object=MibTableColumn
h3cdeBridgeNumIndex=_H3cdeBridgeNumIndex_Object((1,3,6,1,4,1,2011,10,2,62,1,3,1,1,1),_H3cdeBridgeNumIndex_Type())
h3cdeBridgeNumIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cdeBridgeNumIndex.setStatus(_A)
_H3cdeBridgeRowStatus_Type=RowStatus
_H3cdeBridgeRowStatus_Object=MibTableColumn
h3cdeBridgeRowStatus=_H3cdeBridgeRowStatus_Object((1,3,6,1,4,1,2011,10,2,62,1,3,1,1,2),_H3cdeBridgeRowStatus_Type())
h3cdeBridgeRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeBridgeRowStatus.setStatus(_A)
_H3cdeBridgeIfTable_Object=MibTable
h3cdeBridgeIfTable=_H3cdeBridgeIfTable_Object((1,3,6,1,4,1,2011,10,2,62,1,3,2))
if mibBuilder.loadTexts:h3cdeBridgeIfTable.setStatus(_A)
_H3cdeBridgeIfEntry_Object=MibTableRow
h3cdeBridgeIfEntry=_H3cdeBridgeIfEntry_Object((1,3,6,1,4,1,2011,10,2,62,1,3,2,1))
h3cdeBridgeIfEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:h3cdeBridgeIfEntry.setStatus(_A)
class _H3cdeBridgeIfBrgGrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_H3cdeBridgeIfBrgGrp_Type.__name__=_C
_H3cdeBridgeIfBrgGrp_Object=MibTableColumn
h3cdeBridgeIfBrgGrp=_H3cdeBridgeIfBrgGrp_Object((1,3,6,1,4,1,2011,10,2,62,1,3,2,1,1),_H3cdeBridgeIfBrgGrp_Type())
h3cdeBridgeIfBrgGrp.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeBridgeIfBrgGrp.setStatus(_A)
_H3cdeBridgeIfRowStatus_Type=RowStatus
_H3cdeBridgeIfRowStatus_Object=MibTableColumn
h3cdeBridgeIfRowStatus=_H3cdeBridgeIfRowStatus_Object((1,3,6,1,4,1,2011,10,2,62,1,3,2,1,2),_H3cdeBridgeIfRowStatus_Type())
h3cdeBridgeIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeBridgeIfRowStatus.setStatus(_A)
_H3cdeQllc_ObjectIdentity=ObjectIdentity
h3cdeQllc=_H3cdeQllc_ObjectIdentity((1,3,6,1,4,1,2011,10,2,62,1,4))
_H3cdeQllcTable_Object=MibTable
h3cdeQllcTable=_H3cdeQllcTable_Object((1,3,6,1,4,1,2011,10,2,62,1,4,1))
if mibBuilder.loadTexts:h3cdeQllcTable.setStatus(_A)
_H3cdeQllcEntry_Object=MibTableRow
h3cdeQllcEntry=_H3cdeQllcEntry_Object((1,3,6,1,4,1,2011,10,2,62,1,4,1,1))
h3cdeQllcEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:h3cdeQllcEntry.setStatus(_A)
_H3cQllcX121Address_Type=Integer32
_H3cQllcX121Address_Object=MibTableColumn
h3cQllcX121Address=_H3cQllcX121Address_Object((1,3,6,1,4,1,2011,10,2,62,1,4,1,1,1),_H3cQllcX121Address_Type())
h3cQllcX121Address.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQllcX121Address.setStatus(_A)
_H3cQllcLocalMac_Type=MacAddressNC
_H3cQllcLocalMac_Object=MibTableColumn
h3cQllcLocalMac=_H3cQllcLocalMac_Object((1,3,6,1,4,1,2011,10,2,62,1,4,1,1,2),_H3cQllcLocalMac_Type())
h3cQllcLocalMac.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQllcLocalMac.setStatus(_A)
class _H3cQllcLocalSap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_H3cQllcLocalSap_Type.__name__=_K
_H3cQllcLocalSap_Object=MibTableColumn
h3cQllcLocalSap=_H3cQllcLocalSap_Object((1,3,6,1,4,1,2011,10,2,62,1,4,1,1,3),_H3cQllcLocalSap_Type())
h3cQllcLocalSap.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQllcLocalSap.setStatus(_A)
class _H3cQllcRemoteMac_Type(MacAddressNC):defaultHexValue=''
_H3cQllcRemoteMac_Type.__name__=_L
_H3cQllcRemoteMac_Object=MibTableColumn
h3cQllcRemoteMac=_H3cQllcRemoteMac_Object((1,3,6,1,4,1,2011,10,2,62,1,4,1,1,4),_H3cQllcRemoteMac_Type())
h3cQllcRemoteMac.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQllcRemoteMac.setStatus(_A)
class _H3cQllcRemoteSap_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,1))
_H3cQllcRemoteSap_Type.__name__=_K
_H3cQllcRemoteSap_Object=MibTableColumn
h3cQllcRemoteSap=_H3cQllcRemoteSap_Object((1,3,6,1,4,1,2011,10,2,62,1,4,1,1,5),_H3cQllcRemoteSap_Type())
h3cQllcRemoteSap.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQllcRemoteSap.setStatus(_A)
_H3cQllcRowStatus_Type=RowStatus
_H3cQllcRowStatus_Object=MibTableColumn
h3cQllcRowStatus=_H3cQllcRowStatus_Object((1,3,6,1,4,1,2011,10,2,62,1,4,1,1,6),_H3cQllcRowStatus_Type())
h3cQllcRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQllcRowStatus.setStatus(_A)
_H3cdeSdlc_ObjectIdentity=ObjectIdentity
h3cdeSdlc=_H3cdeSdlc_ObjectIdentity((1,3,6,1,4,1,2011,10,2,62,1,5))
_H3cdeSdlcPortTable_Object=MibTable
h3cdeSdlcPortTable=_H3cdeSdlcPortTable_Object((1,3,6,1,4,1,2011,10,2,62,1,5,1))
if mibBuilder.loadTexts:h3cdeSdlcPortTable.setStatus(_A)
_H3cdeSdlcPortEntry_Object=MibTableRow
h3cdeSdlcPortEntry=_H3cdeSdlcPortEntry_Object((1,3,6,1,4,1,2011,10,2,62,1,5,1,1))
h3cdeSdlcPortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:h3cdeSdlcPortEntry.setStatus(_A)
class _H3cdeSdlcPortRole_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('seconday',2),('norole',3)))
_H3cdeSdlcPortRole_Type.__name__=_C
_H3cdeSdlcPortRole_Object=MibTableColumn
h3cdeSdlcPortRole=_H3cdeSdlcPortRole_Object((1,3,6,1,4,1,2011,10,2,62,1,5,1,1,1),_H3cdeSdlcPortRole_Type())
h3cdeSdlcPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeSdlcPortRole.setStatus(_A)
class _H3cdeSdlcPortSendWindow_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_H3cdeSdlcPortSendWindow_Type.__name__=_C
_H3cdeSdlcPortSendWindow_Object=MibTableColumn
h3cdeSdlcPortSendWindow=_H3cdeSdlcPortSendWindow_Object((1,3,6,1,4,1,2011,10,2,62,1,5,1,1,2),_H3cdeSdlcPortSendWindow_Type())
h3cdeSdlcPortSendWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeSdlcPortSendWindow.setStatus(_A)
class _H3cdeSdlcPortModulo_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(8,128)));namedValues=NamedValues(*(('m8',8),('m128',128)))
_H3cdeSdlcPortModulo_Type.__name__=_C
_H3cdeSdlcPortModulo_Object=MibTableColumn
h3cdeSdlcPortModulo=_H3cdeSdlcPortModulo_Object((1,3,6,1,4,1,2011,10,2,62,1,5,1,1,3),_H3cdeSdlcPortModulo_Type())
h3cdeSdlcPortModulo.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeSdlcPortModulo.setStatus(_A)
class _H3cdeSdlcPortMaxPdu_Type(Integer32):defaultValue=265;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,17600))
_H3cdeSdlcPortMaxPdu_Type.__name__=_C
_H3cdeSdlcPortMaxPdu_Object=MibTableColumn
h3cdeSdlcPortMaxPdu=_H3cdeSdlcPortMaxPdu_Object((1,3,6,1,4,1,2011,10,2,62,1,5,1,1,4),_H3cdeSdlcPortMaxPdu_Type())
h3cdeSdlcPortMaxPdu.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeSdlcPortMaxPdu.setStatus(_A)
class _H3cdeSdlcPortMaxSendQueue_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,255))
_H3cdeSdlcPortMaxSendQueue_Type.__name__=_C
_H3cdeSdlcPortMaxSendQueue_Object=MibTableColumn
h3cdeSdlcPortMaxSendQueue=_H3cdeSdlcPortMaxSendQueue_Object((1,3,6,1,4,1,2011,10,2,62,1,5,1,1,5),_H3cdeSdlcPortMaxSendQueue_Type())
h3cdeSdlcPortMaxSendQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeSdlcPortMaxSendQueue.setStatus(_A)
class _H3cdeSdlcPortMaxTransmission_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_H3cdeSdlcPortMaxTransmission_Type.__name__=_C
_H3cdeSdlcPortMaxTransmission_Object=MibTableColumn
h3cdeSdlcPortMaxTransmission=_H3cdeSdlcPortMaxTransmission_Object((1,3,6,1,4,1,2011,10,2,62,1,5,1,1,6),_H3cdeSdlcPortMaxTransmission_Type())
h3cdeSdlcPortMaxTransmission.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeSdlcPortMaxTransmission.setStatus(_A)
class _H3cdeSdlcPortSimultaneousEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_H3cdeSdlcPortSimultaneousEnable_Type.__name__=_C
_H3cdeSdlcPortSimultaneousEnable_Object=MibTableColumn
h3cdeSdlcPortSimultaneousEnable=_H3cdeSdlcPortSimultaneousEnable_Object((1,3,6,1,4,1,2011,10,2,62,1,5,1,1,7),_H3cdeSdlcPortSimultaneousEnable_Type())
h3cdeSdlcPortSimultaneousEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeSdlcPortSimultaneousEnable.setStatus(_A)
class _H3cdeSdlcPortTimerACK_Type(Integer32):defaultValue=3000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_H3cdeSdlcPortTimerACK_Type.__name__=_C
_H3cdeSdlcPortTimerACK_Object=MibTableColumn
h3cdeSdlcPortTimerACK=_H3cdeSdlcPortTimerACK_Object((1,3,6,1,4,1,2011,10,2,62,1,5,1,1,8),_H3cdeSdlcPortTimerACK_Type())
h3cdeSdlcPortTimerACK.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeSdlcPortTimerACK.setStatus(_A)
if mibBuilder.loadTexts:h3cdeSdlcPortTimerACK.setUnits(_F)
class _H3cdeSdlcPortTimerLifeTime_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_H3cdeSdlcPortTimerLifeTime_Type.__name__=_C
_H3cdeSdlcPortTimerLifeTime_Object=MibTableColumn
h3cdeSdlcPortTimerLifeTime=_H3cdeSdlcPortTimerLifeTime_Object((1,3,6,1,4,1,2011,10,2,62,1,5,1,1,9),_H3cdeSdlcPortTimerLifeTime_Type())
h3cdeSdlcPortTimerLifeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeSdlcPortTimerLifeTime.setStatus(_A)
if mibBuilder.loadTexts:h3cdeSdlcPortTimerLifeTime.setUnits(_F)
class _H3cdeSdlcPortTimerPollPause_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_H3cdeSdlcPortTimerPollPause_Type.__name__=_C
_H3cdeSdlcPortTimerPollPause_Object=MibTableColumn
h3cdeSdlcPortTimerPollPause=_H3cdeSdlcPortTimerPollPause_Object((1,3,6,1,4,1,2011,10,2,62,1,5,1,1,10),_H3cdeSdlcPortTimerPollPause_Type())
h3cdeSdlcPortTimerPollPause.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeSdlcPortTimerPollPause.setStatus(_A)
if mibBuilder.loadTexts:h3cdeSdlcPortTimerPollPause.setUnits(_F)
_H3cdeSdlcPortRowStatus_Type=RowStatus
_H3cdeSdlcPortRowStatus_Object=MibTableColumn
h3cdeSdlcPortRowStatus=_H3cdeSdlcPortRowStatus_Object((1,3,6,1,4,1,2011,10,2,62,1,5,1,1,11),_H3cdeSdlcPortRowStatus_Type())
h3cdeSdlcPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeSdlcPortRowStatus.setStatus(_A)
_H3cdeLlc2_ObjectIdentity=ObjectIdentity
h3cdeLlc2=_H3cdeLlc2_ObjectIdentity((1,3,6,1,4,1,2011,10,2,62,1,6))
_H3cdeLlc2PortTable_Object=MibTable
h3cdeLlc2PortTable=_H3cdeLlc2PortTable_Object((1,3,6,1,4,1,2011,10,2,62,1,6,1))
if mibBuilder.loadTexts:h3cdeLlc2PortTable.setStatus(_A)
_H3cdeLlc2PortEntry_Object=MibTableRow
h3cdeLlc2PortEntry=_H3cdeLlc2PortEntry_Object((1,3,6,1,4,1,2011,10,2,62,1,6,1,1))
h3cdeLlc2PortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:h3cdeLlc2PortEntry.setStatus(_A)
class _H3cdeLlc2PortMaxAck_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_H3cdeLlc2PortMaxAck_Type.__name__=_C
_H3cdeLlc2PortMaxAck_Object=MibTableColumn
h3cdeLlc2PortMaxAck=_H3cdeLlc2PortMaxAck_Object((1,3,6,1,4,1,2011,10,2,62,1,6,1,1,1),_H3cdeLlc2PortMaxAck_Type())
h3cdeLlc2PortMaxAck.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeLlc2PortMaxAck.setStatus(_A)
class _H3cdeLlc2PortMaxPdu_Type(Integer32):defaultValue=1493;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1700))
_H3cdeLlc2PortMaxPdu_Type.__name__=_C
_H3cdeLlc2PortMaxPdu_Object=MibTableColumn
h3cdeLlc2PortMaxPdu=_H3cdeLlc2PortMaxPdu_Object((1,3,6,1,4,1,2011,10,2,62,1,6,1,1,2),_H3cdeLlc2PortMaxPdu_Type())
h3cdeLlc2PortMaxPdu.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeLlc2PortMaxPdu.setStatus(_A)
class _H3cdeLlc2PortMaxSendQueue_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,200))
_H3cdeLlc2PortMaxSendQueue_Type.__name__=_C
_H3cdeLlc2PortMaxSendQueue_Object=MibTableColumn
h3cdeLlc2PortMaxSendQueue=_H3cdeLlc2PortMaxSendQueue_Object((1,3,6,1,4,1,2011,10,2,62,1,6,1,1,3),_H3cdeLlc2PortMaxSendQueue_Type())
h3cdeLlc2PortMaxSendQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeLlc2PortMaxSendQueue.setStatus(_A)
class _H3cdeLlc2PortMaxTransmission_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_H3cdeLlc2PortMaxTransmission_Type.__name__=_C
_H3cdeLlc2PortMaxTransmission_Object=MibTableColumn
h3cdeLlc2PortMaxTransmission=_H3cdeLlc2PortMaxTransmission_Object((1,3,6,1,4,1,2011,10,2,62,1,6,1,1,4),_H3cdeLlc2PortMaxTransmission_Type())
h3cdeLlc2PortMaxTransmission.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeLlc2PortMaxTransmission.setStatus(_A)
class _H3cdeLlc2PortModulo_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(8,128)));namedValues=NamedValues(*(('m8',8),('m128',128)))
_H3cdeLlc2PortModulo_Type.__name__=_C
_H3cdeLlc2PortModulo_Object=MibTableColumn
h3cdeLlc2PortModulo=_H3cdeLlc2PortModulo_Object((1,3,6,1,4,1,2011,10,2,62,1,6,1,1,5),_H3cdeLlc2PortModulo_Type())
h3cdeLlc2PortModulo.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeLlc2PortModulo.setStatus(_A)
class _H3cdeLlc2PortReceiveWindow_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_H3cdeLlc2PortReceiveWindow_Type.__name__=_C
_H3cdeLlc2PortReceiveWindow_Object=MibTableColumn
h3cdeLlc2PortReceiveWindow=_H3cdeLlc2PortReceiveWindow_Object((1,3,6,1,4,1,2011,10,2,62,1,6,1,1,6),_H3cdeLlc2PortReceiveWindow_Type())
h3cdeLlc2PortReceiveWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeLlc2PortReceiveWindow.setStatus(_A)
class _H3cdeLlc2PortTimerAck_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_H3cdeLlc2PortTimerAck_Type.__name__=_C
_H3cdeLlc2PortTimerAck_Object=MibTableColumn
h3cdeLlc2PortTimerAck=_H3cdeLlc2PortTimerAck_Object((1,3,6,1,4,1,2011,10,2,62,1,6,1,1,7),_H3cdeLlc2PortTimerAck_Type())
h3cdeLlc2PortTimerAck.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeLlc2PortTimerAck.setStatus(_A)
if mibBuilder.loadTexts:h3cdeLlc2PortTimerAck.setUnits(_F)
class _H3cdeLlc2PortTimerAckDelay_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_H3cdeLlc2PortTimerAckDelay_Type.__name__=_C
_H3cdeLlc2PortTimerAckDelay_Object=MibTableColumn
h3cdeLlc2PortTimerAckDelay=_H3cdeLlc2PortTimerAckDelay_Object((1,3,6,1,4,1,2011,10,2,62,1,6,1,1,8),_H3cdeLlc2PortTimerAckDelay_Type())
h3cdeLlc2PortTimerAckDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeLlc2PortTimerAckDelay.setStatus(_A)
if mibBuilder.loadTexts:h3cdeLlc2PortTimerAckDelay.setUnits(_F)
class _H3cdeLlc2PortTimerDetect_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_H3cdeLlc2PortTimerDetect_Type.__name__=_C
_H3cdeLlc2PortTimerDetect_Object=MibTableColumn
h3cdeLlc2PortTimerDetect=_H3cdeLlc2PortTimerDetect_Object((1,3,6,1,4,1,2011,10,2,62,1,6,1,1,9),_H3cdeLlc2PortTimerDetect_Type())
h3cdeLlc2PortTimerDetect.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeLlc2PortTimerDetect.setStatus(_A)
if mibBuilder.loadTexts:h3cdeLlc2PortTimerDetect.setUnits(_F)
class _H3cdeLlc2PortTimerBusy_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_H3cdeLlc2PortTimerBusy_Type.__name__=_C
_H3cdeLlc2PortTimerBusy_Object=MibTableColumn
h3cdeLlc2PortTimerBusy=_H3cdeLlc2PortTimerBusy_Object((1,3,6,1,4,1,2011,10,2,62,1,6,1,1,10),_H3cdeLlc2PortTimerBusy_Type())
h3cdeLlc2PortTimerBusy.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeLlc2PortTimerBusy.setStatus(_A)
if mibBuilder.loadTexts:h3cdeLlc2PortTimerBusy.setUnits(_F)
class _H3cdeLlc2PortTimerPoll_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_H3cdeLlc2PortTimerPoll_Type.__name__=_C
_H3cdeLlc2PortTimerPoll_Object=MibTableColumn
h3cdeLlc2PortTimerPoll=_H3cdeLlc2PortTimerPoll_Object((1,3,6,1,4,1,2011,10,2,62,1,6,1,1,11),_H3cdeLlc2PortTimerPoll_Type())
h3cdeLlc2PortTimerPoll.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeLlc2PortTimerPoll.setStatus(_A)
if mibBuilder.loadTexts:h3cdeLlc2PortTimerPoll.setUnits(_F)
class _H3cdeLlc2PortTimerReject_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_H3cdeLlc2PortTimerReject_Type.__name__=_C
_H3cdeLlc2PortTimerReject_Object=MibTableColumn
h3cdeLlc2PortTimerReject=_H3cdeLlc2PortTimerReject_Object((1,3,6,1,4,1,2011,10,2,62,1,6,1,1,12),_H3cdeLlc2PortTimerReject_Type())
h3cdeLlc2PortTimerReject.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeLlc2PortTimerReject.setStatus(_A)
if mibBuilder.loadTexts:h3cdeLlc2PortTimerReject.setUnits(_F)
_H3cdeLlc2PortRowStatus_Type=RowStatus
_H3cdeLlc2PortRowStatus_Object=MibTableColumn
h3cdeLlc2PortRowStatus=_H3cdeLlc2PortRowStatus_Object((1,3,6,1,4,1,2011,10,2,62,1,6,1,1,13),_H3cdeLlc2PortRowStatus_Type())
h3cdeLlc2PortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeLlc2PortRowStatus.setStatus(_A)
_H3cdeReachableCache_ObjectIdentity=ObjectIdentity
h3cdeReachableCache=_H3cdeReachableCache_ObjectIdentity((1,3,6,1,4,1,2011,10,2,62,1,7))
_H3cdeRchCacheStat_ObjectIdentity=ObjectIdentity
h3cdeRchCacheStat=_H3cdeRchCacheStat_ObjectIdentity((1,3,6,1,4,1,2011,10,2,62,1,7,1))
_H3cdeRchCacheMaxIndex_Type=Integer32
_H3cdeRchCacheMaxIndex_Object=MibScalar
h3cdeRchCacheMaxIndex=_H3cdeRchCacheMaxIndex_Object((1,3,6,1,4,1,2011,10,2,62,1,7,1,1),_H3cdeRchCacheMaxIndex_Type())
h3cdeRchCacheMaxIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cdeRchCacheMaxIndex.setStatus(_A)
_H3cdeRchCacheNextIndex_Type=Integer32
_H3cdeRchCacheNextIndex_Object=MibScalar
h3cdeRchCacheNextIndex=_H3cdeRchCacheNextIndex_Object((1,3,6,1,4,1,2011,10,2,62,1,7,1,2),_H3cdeRchCacheNextIndex_Type())
h3cdeRchCacheNextIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cdeRchCacheNextIndex.setStatus(_A)
_H3cdeRchCacheTable_Object=MibTable
h3cdeRchCacheTable=_H3cdeRchCacheTable_Object((1,3,6,1,4,1,2011,10,2,62,1,7,3))
if mibBuilder.loadTexts:h3cdeRchCacheTable.setStatus(_A)
_H3cdeRchCacheEntry_Object=MibTableRow
h3cdeRchCacheEntry=_H3cdeRchCacheEntry_Object((1,3,6,1,4,1,2011,10,2,62,1,7,3,1))
h3cdeRchCacheEntry.setIndexNames((0,_J,_S))
if mibBuilder.loadTexts:h3cdeRchCacheEntry.setStatus(_A)
_H3cdeRchCacheIndex_Type=Integer32
_H3cdeRchCacheIndex_Object=MibTableColumn
h3cdeRchCacheIndex=_H3cdeRchCacheIndex_Object((1,3,6,1,4,1,2011,10,2,62,1,7,3,1,1),_H3cdeRchCacheIndex_Type())
h3cdeRchCacheIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cdeRchCacheIndex.setStatus(_A)
class _H3cdeRchCacheStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('found',1),('verify',2),('noCacheInfo',3),('exploring',4),('waiting',5)))
_H3cdeRchCacheStatus_Type.__name__=_C
_H3cdeRchCacheStatus_Object=MibTableColumn
h3cdeRchCacheStatus=_H3cdeRchCacheStatus_Object((1,3,6,1,4,1,2011,10,2,62,1,7,3,1,2),_H3cdeRchCacheStatus_Type())
h3cdeRchCacheStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cdeRchCacheStatus.setStatus(_A)
_H3cdeRchCacheRemainTime_Type=TimeTicks
_H3cdeRchCacheRemainTime_Object=MibTableColumn
h3cdeRchCacheRemainTime=_H3cdeRchCacheRemainTime_Object((1,3,6,1,4,1,2011,10,2,62,1,7,3,1,3),_H3cdeRchCacheRemainTime_Type())
h3cdeRchCacheRemainTime.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cdeRchCacheRemainTime.setStatus(_A)
_H3cdeRchCacheMac_Type=MacAddressNC
_H3cdeRchCacheMac_Object=MibTableColumn
h3cdeRchCacheMac=_H3cdeRchCacheMac_Object((1,3,6,1,4,1,2011,10,2,62,1,7,3,1,4),_H3cdeRchCacheMac_Type())
h3cdeRchCacheMac.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeRchCacheMac.setStatus(_A)
_H3cdeRchCacheRemoteIpAddrType_Type=InetAddressType
_H3cdeRchCacheRemoteIpAddrType_Object=MibTableColumn
h3cdeRchCacheRemoteIpAddrType=_H3cdeRchCacheRemoteIpAddrType_Object((1,3,6,1,4,1,2011,10,2,62,1,7,3,1,5),_H3cdeRchCacheRemoteIpAddrType_Type())
h3cdeRchCacheRemoteIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeRchCacheRemoteIpAddrType.setStatus(_A)
_H3cdeRchCacheRemoteIp_Type=InetAddress
_H3cdeRchCacheRemoteIp_Object=MibTableColumn
h3cdeRchCacheRemoteIp=_H3cdeRchCacheRemoteIp_Object((1,3,6,1,4,1,2011,10,2,62,1,7,3,1,6),_H3cdeRchCacheRemoteIp_Type())
h3cdeRchCacheRemoteIp.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeRchCacheRemoteIp.setStatus(_A)
_H3cdeRchCacheRowStatus_Type=RowStatus
_H3cdeRchCacheRowStatus_Object=MibTableColumn
h3cdeRchCacheRowStatus=_H3cdeRchCacheRowStatus_Object((1,3,6,1,4,1,2011,10,2,62,1,7,3,1,7),_H3cdeRchCacheRowStatus_Type())
h3cdeRchCacheRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeRchCacheRowStatus.setStatus(_A)
_H3cdeEthernetBackup_ObjectIdentity=ObjectIdentity
h3cdeEthernetBackup=_H3cdeEthernetBackup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,62,1,8))
_H3cdeEBMacMapStat_ObjectIdentity=ObjectIdentity
h3cdeEBMacMapStat=_H3cdeEBMacMapStat_ObjectIdentity((1,3,6,1,4,1,2011,10,2,62,1,8,1))
_H3cdeEBMacMapMaxIndex_Type=Integer32
_H3cdeEBMacMapMaxIndex_Object=MibScalar
h3cdeEBMacMapMaxIndex=_H3cdeEBMacMapMaxIndex_Object((1,3,6,1,4,1,2011,10,2,62,1,8,1,1),_H3cdeEBMacMapMaxIndex_Type())
h3cdeEBMacMapMaxIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cdeEBMacMapMaxIndex.setStatus(_A)
_H3cdeEBMacMapNextIndex_Type=Integer32
_H3cdeEBMacMapNextIndex_Object=MibScalar
h3cdeEBMacMapNextIndex=_H3cdeEBMacMapNextIndex_Object((1,3,6,1,4,1,2011,10,2,62,1,8,1,2),_H3cdeEBMacMapNextIndex_Type())
h3cdeEBMacMapNextIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cdeEBMacMapNextIndex.setStatus(_A)
_H3cdeEBIfTable_Object=MibTable
h3cdeEBIfTable=_H3cdeEBIfTable_Object((1,3,6,1,4,1,2011,10,2,62,1,8,3))
if mibBuilder.loadTexts:h3cdeEBIfTable.setStatus(_A)
_H3cdeEBIfEntry_Object=MibTableRow
h3cdeEBIfEntry=_H3cdeEBIfEntry_Object((1,3,6,1,4,1,2011,10,2,62,1,8,3,1))
h3cdeEBIfEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:h3cdeEBIfEntry.setStatus(_A)
class _H3cdeEBMulticastMac_Type(MacAddressNC):defaultHexValue='000000000000'
_H3cdeEBMulticastMac_Type.__name__=_L
_H3cdeEBMulticastMac_Object=MibTableColumn
h3cdeEBMulticastMac=_H3cdeEBMulticastMac_Object((1,3,6,1,4,1,2011,10,2,62,1,8,3,1,1),_H3cdeEBMulticastMac_Type())
h3cdeEBMulticastMac.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeEBMulticastMac.setStatus(_A)
class _H3cdeEBPriority_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_H3cdeEBPriority_Type.__name__=_C
_H3cdeEBPriority_Object=MibTableColumn
h3cdeEBPriority=_H3cdeEBPriority_Object((1,3,6,1,4,1,2011,10,2,62,1,8,3,1,2),_H3cdeEBPriority_Type())
h3cdeEBPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeEBPriority.setStatus(_A)
class _H3cdeEBtimer_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_H3cdeEBtimer_Type.__name__=_C
_H3cdeEBtimer_Object=MibTableColumn
h3cdeEBtimer=_H3cdeEBtimer_Object((1,3,6,1,4,1,2011,10,2,62,1,8,3,1,3),_H3cdeEBtimer_Type())
h3cdeEBtimer.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeEBtimer.setStatus(_A)
_H3cdeEBRowStatus_Type=RowStatus
_H3cdeEBRowStatus_Object=MibTableColumn
h3cdeEBRowStatus=_H3cdeEBRowStatus_Object((1,3,6,1,4,1,2011,10,2,62,1,8,3,1,4),_H3cdeEBRowStatus_Type())
h3cdeEBRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeEBRowStatus.setStatus(_A)
_H3cdeEBMacMapTable_Object=MibTable
h3cdeEBMacMapTable=_H3cdeEBMacMapTable_Object((1,3,6,1,4,1,2011,10,2,62,1,8,4))
if mibBuilder.loadTexts:h3cdeEBMacMapTable.setStatus(_A)
_H3cdeEBMacMapEntry_Object=MibTableRow
h3cdeEBMacMapEntry=_H3cdeEBMacMapEntry_Object((1,3,6,1,4,1,2011,10,2,62,1,8,4,1))
h3cdeEBMacMapEntry.setIndexNames((0,_H,_I),(0,_J,_T))
if mibBuilder.loadTexts:h3cdeEBMacMapEntry.setStatus(_A)
_H3cdeEBMacMapIndex_Type=Integer32
_H3cdeEBMacMapIndex_Object=MibTableColumn
h3cdeEBMacMapIndex=_H3cdeEBMacMapIndex_Object((1,3,6,1,4,1,2011,10,2,62,1,8,4,1,1),_H3cdeEBMacMapIndex_Type())
h3cdeEBMacMapIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cdeEBMacMapIndex.setStatus(_A)
_H3cdeEBMacMapLocalMac_Type=MacAddressNC
_H3cdeEBMacMapLocalMac_Object=MibTableColumn
h3cdeEBMacMapLocalMac=_H3cdeEBMacMapLocalMac_Object((1,3,6,1,4,1,2011,10,2,62,1,8,4,1,2),_H3cdeEBMacMapLocalMac_Type())
h3cdeEBMacMapLocalMac.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeEBMacMapLocalMac.setStatus(_A)
_H3cdeEBMacMapRemoteMac_Type=MacAddressNC
_H3cdeEBMacMapRemoteMac_Object=MibTableColumn
h3cdeEBMacMapRemoteMac=_H3cdeEBMacMapRemoteMac_Object((1,3,6,1,4,1,2011,10,2,62,1,8,4,1,3),_H3cdeEBMacMapRemoteMac_Type())
h3cdeEBMacMapRemoteMac.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeEBMacMapRemoteMac.setStatus(_A)
_H3cdeEBMacMapNeighbour_Type=MacAddressNC
_H3cdeEBMacMapNeighbour_Object=MibTableColumn
h3cdeEBMacMapNeighbour=_H3cdeEBMacMapNeighbour_Object((1,3,6,1,4,1,2011,10,2,62,1,8,4,1,4),_H3cdeEBMacMapNeighbour_Type())
h3cdeEBMacMapNeighbour.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeEBMacMapNeighbour.setStatus(_A)
_H3cdeEBMacMapRowStatus_Type=RowStatus
_H3cdeEBMacMapRowStatus_Object=MibTableColumn
h3cdeEBMacMapRowStatus=_H3cdeEBMacMapRowStatus_Object((1,3,6,1,4,1,2011,10,2,62,1,8,4,1,5),_H3cdeEBMacMapRowStatus_Type())
h3cdeEBMacMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cdeEBMacMapRowStatus.setStatus(_A)
dlswTConnConfigEntry.registerAugmentions((_J,_U))
h3cdeTConnConfigEntry.setIndexNames(*dlswTConnConfigEntry.getIndexNames())
dlswTConnOperEntry.registerAugmentions((_J,_V))
h3cdeTConnOperEntry.setIndexNames(*dlswTConnOperEntry.getIndexNames())
dlswTConnTcpConfigEntry.registerAugmentions((_J,_W))
h3cdeTConnTcpConfigEntry.setIndexNames(*dlswTConnTcpConfigEntry.getIndexNames())
mibBuilder.exportSymbols(_J,**{'h3cDlswExt':h3cDlswExt,'h3cDlswExtMIBObjects':h3cDlswExtMIBObjects,'h3cdeNode':h3cdeNode,'h3cdeNodeVendorID':h3cdeNodeVendorID,'h3cdeNodeIpAddrType':h3cdeNodeIpAddrType,'h3cdeNodeLocalAddr':h3cdeNodeLocalAddr,'h3cdeNodePriority':h3cdeNodePriority,'h3cdeNodeInitPacingWindow':h3cdeNodeInitPacingWindow,'h3cdeNodeMaxPacingWindow':h3cdeNodeMaxPacingWindow,'h3cdeNodeKeepAliveInterval':h3cdeNodeKeepAliveInterval,'h3cdeNodePermitDynamic':h3cdeNodePermitDynamic,'h3cdeNodeConnTimeout':h3cdeNodeConnTimeout,'h3cdeNodeLocalPendTimeout':h3cdeNodeLocalPendTimeout,'h3cdeNodeRemotePendTimeout':h3cdeNodeRemotePendTimeout,'h3cdeNodeSnaCacheTimeout':h3cdeNodeSnaCacheTimeout,'h3cdeNodeExplorerTimeout':h3cdeNodeExplorerTimeout,'h3cdeNodeExplorerWaitTimeout':h3cdeNodeExplorerWaitTimeout,'h3cdeNodeConfigSapList':h3cdeNodeConfigSapList,'h3cdeNodeMaxTransmission':h3cdeNodeMaxTransmission,'h3cdeNodeMulticastStatus':h3cdeNodeMulticastStatus,'h3cdeNodeMulticastAddress':h3cdeNodeMulticastAddress,'h3cdeNodeResetTcpAll':h3cdeNodeResetTcpAll,'h3cdeNodeStCapTcpNum':h3cdeNodeStCapTcpNum,'h3cdeNodeTcpQueueMax':h3cdeNodeTcpQueueMax,'h3cdeTConn':h3cdeTConn,'h3cdeTConnConfigTable':h3cdeTConnConfigTable,_U:h3cdeTConnConfigEntry,'h3cdeTConnConfigVersion':h3cdeTConnConfigVersion,'h3cdeTConnConfigPriority':h3cdeTConnConfigPriority,'h3cdeTConnConfigLfSize':h3cdeTConnConfigLfSize,'h3cdeTConnConfigKeepaliveIntval':h3cdeTConnConfigKeepaliveIntval,'h3cdeTConnConfigBackup':h3cdeTConnConfigBackup,'h3cdeTConnConfigBackupTAddr':h3cdeTConnConfigBackupTAddr,'h3cdeTConnConfigBackupLinger':h3cdeTConnConfigBackupLinger,'h3cdeTConnOperTable':h3cdeTConnOperTable,_V:h3cdeTConnOperEntry,'h3cdeTConnOperPeerType':h3cdeTConnOperPeerType,'h3cdeTConnOperVendorID':h3cdeTConnOperVendorID,'h3cdeTConnOperVersionString':h3cdeTConnOperVersionString,'h3cdeTConnOperUpTime':h3cdeTConnOperUpTime,'h3cdeTConnOperMulticastAddress':h3cdeTConnOperMulticastAddress,'h3cdeTConnOperStCapTcpNumber':h3cdeTConnOperStCapTcpNumber,'h3cdeTConnOperRecvPkts':h3cdeTConnOperRecvPkts,'h3cdeTConnOperSendPkts':h3cdeTConnOperSendPkts,'h3cdeTConnOperDropPkts':h3cdeTConnOperDropPkts,'h3cdeTConnTcpConfigTable':h3cdeTConnTcpConfigTable,_W:h3cdeTConnTcpConfigEntry,'h3cdeTConnTcpConfigQueueMax':h3cdeTConnTcpConfigQueueMax,'h3cdeBridge':h3cdeBridge,'h3cdeBridgeTable':h3cdeBridgeTable,'h3cdeBridgeEntry':h3cdeBridgeEntry,_R:h3cdeBridgeNumIndex,'h3cdeBridgeRowStatus':h3cdeBridgeRowStatus,'h3cdeBridgeIfTable':h3cdeBridgeIfTable,'h3cdeBridgeIfEntry':h3cdeBridgeIfEntry,'h3cdeBridgeIfBrgGrp':h3cdeBridgeIfBrgGrp,'h3cdeBridgeIfRowStatus':h3cdeBridgeIfRowStatus,'h3cdeQllc':h3cdeQllc,'h3cdeQllcTable':h3cdeQllcTable,'h3cdeQllcEntry':h3cdeQllcEntry,'h3cQllcX121Address':h3cQllcX121Address,'h3cQllcLocalMac':h3cQllcLocalMac,'h3cQllcLocalSap':h3cQllcLocalSap,'h3cQllcRemoteMac':h3cQllcRemoteMac,'h3cQllcRemoteSap':h3cQllcRemoteSap,'h3cQllcRowStatus':h3cQllcRowStatus,'h3cdeSdlc':h3cdeSdlc,'h3cdeSdlcPortTable':h3cdeSdlcPortTable,'h3cdeSdlcPortEntry':h3cdeSdlcPortEntry,'h3cdeSdlcPortRole':h3cdeSdlcPortRole,'h3cdeSdlcPortSendWindow':h3cdeSdlcPortSendWindow,'h3cdeSdlcPortModulo':h3cdeSdlcPortModulo,'h3cdeSdlcPortMaxPdu':h3cdeSdlcPortMaxPdu,'h3cdeSdlcPortMaxSendQueue':h3cdeSdlcPortMaxSendQueue,'h3cdeSdlcPortMaxTransmission':h3cdeSdlcPortMaxTransmission,'h3cdeSdlcPortSimultaneousEnable':h3cdeSdlcPortSimultaneousEnable,'h3cdeSdlcPortTimerACK':h3cdeSdlcPortTimerACK,'h3cdeSdlcPortTimerLifeTime':h3cdeSdlcPortTimerLifeTime,'h3cdeSdlcPortTimerPollPause':h3cdeSdlcPortTimerPollPause,'h3cdeSdlcPortRowStatus':h3cdeSdlcPortRowStatus,'h3cdeLlc2':h3cdeLlc2,'h3cdeLlc2PortTable':h3cdeLlc2PortTable,'h3cdeLlc2PortEntry':h3cdeLlc2PortEntry,'h3cdeLlc2PortMaxAck':h3cdeLlc2PortMaxAck,'h3cdeLlc2PortMaxPdu':h3cdeLlc2PortMaxPdu,'h3cdeLlc2PortMaxSendQueue':h3cdeLlc2PortMaxSendQueue,'h3cdeLlc2PortMaxTransmission':h3cdeLlc2PortMaxTransmission,'h3cdeLlc2PortModulo':h3cdeLlc2PortModulo,'h3cdeLlc2PortReceiveWindow':h3cdeLlc2PortReceiveWindow,'h3cdeLlc2PortTimerAck':h3cdeLlc2PortTimerAck,'h3cdeLlc2PortTimerAckDelay':h3cdeLlc2PortTimerAckDelay,'h3cdeLlc2PortTimerDetect':h3cdeLlc2PortTimerDetect,'h3cdeLlc2PortTimerBusy':h3cdeLlc2PortTimerBusy,'h3cdeLlc2PortTimerPoll':h3cdeLlc2PortTimerPoll,'h3cdeLlc2PortTimerReject':h3cdeLlc2PortTimerReject,'h3cdeLlc2PortRowStatus':h3cdeLlc2PortRowStatus,'h3cdeReachableCache':h3cdeReachableCache,'h3cdeRchCacheStat':h3cdeRchCacheStat,'h3cdeRchCacheMaxIndex':h3cdeRchCacheMaxIndex,'h3cdeRchCacheNextIndex':h3cdeRchCacheNextIndex,'h3cdeRchCacheTable':h3cdeRchCacheTable,'h3cdeRchCacheEntry':h3cdeRchCacheEntry,_S:h3cdeRchCacheIndex,'h3cdeRchCacheStatus':h3cdeRchCacheStatus,'h3cdeRchCacheRemainTime':h3cdeRchCacheRemainTime,'h3cdeRchCacheMac':h3cdeRchCacheMac,'h3cdeRchCacheRemoteIpAddrType':h3cdeRchCacheRemoteIpAddrType,'h3cdeRchCacheRemoteIp':h3cdeRchCacheRemoteIp,'h3cdeRchCacheRowStatus':h3cdeRchCacheRowStatus,'h3cdeEthernetBackup':h3cdeEthernetBackup,'h3cdeEBMacMapStat':h3cdeEBMacMapStat,'h3cdeEBMacMapMaxIndex':h3cdeEBMacMapMaxIndex,'h3cdeEBMacMapNextIndex':h3cdeEBMacMapNextIndex,'h3cdeEBIfTable':h3cdeEBIfTable,'h3cdeEBIfEntry':h3cdeEBIfEntry,'h3cdeEBMulticastMac':h3cdeEBMulticastMac,'h3cdeEBPriority':h3cdeEBPriority,'h3cdeEBtimer':h3cdeEBtimer,'h3cdeEBRowStatus':h3cdeEBRowStatus,'h3cdeEBMacMapTable':h3cdeEBMacMapTable,'h3cdeEBMacMapEntry':h3cdeEBMacMapEntry,_T:h3cdeEBMacMapIndex,'h3cdeEBMacMapLocalMac':h3cdeEBMacMapLocalMac,'h3cdeEBMacMapRemoteMac':h3cdeEBMacMapRemoteMac,'h3cdeEBMacMapNeighbour':h3cdeEBMacMapNeighbour,'h3cdeEBMacMapRowStatus':h3cdeEBMacMapRowStatus})