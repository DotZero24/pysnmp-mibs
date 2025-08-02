_W='hpnicfdeTConnTcpConfigEntry'
_V='hpnicfdeTConnOperEntry'
_U='hpnicfdeTConnConfigEntry'
_T='hpnicfdeEBMacMapIndex'
_S='hpnicfdeRchCacheIndex'
_R='hpnicfdeBridgeNumIndex'
_Q='disabled'
_P='enabled'
_O='packets'
_N='InetAddress'
_M='not-accessible'
_L='MacAddressNC'
_K='OctetString'
_J='HPN-ICF-SNA-DLSW-EXT-MIB'
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
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_H,_I)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_N,'InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfDlswExt=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,62))
if mibBuilder.loadTexts:hpnicfDlswExt.setRevisions(('2005-07-20 19:00',))
_HpnicfDlswExtMIBObjects_ObjectIdentity=ObjectIdentity
hpnicfDlswExtMIBObjects=_HpnicfDlswExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,62,1))
_HpnicfdeNode_ObjectIdentity=ObjectIdentity
hpnicfdeNode=_HpnicfdeNode_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1))
class _HpnicfdeNodeVendorID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_HpnicfdeNodeVendorID_Type.__name__=_K
_HpnicfdeNodeVendorID_Object=MibScalar
hpnicfdeNodeVendorID=_HpnicfdeNodeVendorID_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,1),_HpnicfdeNodeVendorID_Type())
hpnicfdeNodeVendorID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodeVendorID.setStatus(_A)
_HpnicfdeNodeIpAddrType_Type=InetAddressType
_HpnicfdeNodeIpAddrType_Object=MibScalar
hpnicfdeNodeIpAddrType=_HpnicfdeNodeIpAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,2),_HpnicfdeNodeIpAddrType_Type())
hpnicfdeNodeIpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodeIpAddrType.setStatus(_A)
class _HpnicfdeNodeLocalAddr_Type(InetAddress):defaultHexValue=''
_HpnicfdeNodeLocalAddr_Type.__name__=_N
_HpnicfdeNodeLocalAddr_Object=MibScalar
hpnicfdeNodeLocalAddr=_HpnicfdeNodeLocalAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,3),_HpnicfdeNodeLocalAddr_Type())
hpnicfdeNodeLocalAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodeLocalAddr.setStatus(_A)
class _HpnicfdeNodePriority_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5),ValueRangeConstraint(65535,65535))
_HpnicfdeNodePriority_Type.__name__=_C
_HpnicfdeNodePriority_Object=MibScalar
hpnicfdeNodePriority=_HpnicfdeNodePriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,4),_HpnicfdeNodePriority_Type())
hpnicfdeNodePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodePriority.setStatus(_A)
class _HpnicfdeNodeInitPacingWindow_Type(Integer32):defaultValue=40;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000),ValueRangeConstraint(65535,65535))
_HpnicfdeNodeInitPacingWindow_Type.__name__=_C
_HpnicfdeNodeInitPacingWindow_Object=MibScalar
hpnicfdeNodeInitPacingWindow=_HpnicfdeNodeInitPacingWindow_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,5),_HpnicfdeNodeInitPacingWindow_Type())
hpnicfdeNodeInitPacingWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodeInitPacingWindow.setStatus(_A)
if mibBuilder.loadTexts:hpnicfdeNodeInitPacingWindow.setUnits(_O)
class _HpnicfdeNodeMaxPacingWindow_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2000),ValueRangeConstraint(65535,65535))
_HpnicfdeNodeMaxPacingWindow_Type.__name__=_C
_HpnicfdeNodeMaxPacingWindow_Object=MibScalar
hpnicfdeNodeMaxPacingWindow=_HpnicfdeNodeMaxPacingWindow_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,6),_HpnicfdeNodeMaxPacingWindow_Type())
hpnicfdeNodeMaxPacingWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodeMaxPacingWindow.setStatus(_A)
if mibBuilder.loadTexts:hpnicfdeNodeMaxPacingWindow.setUnits(_O)
class _HpnicfdeNodeKeepAliveInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000),ValueRangeConstraint(65535,65535))
_HpnicfdeNodeKeepAliveInterval_Type.__name__=_C
_HpnicfdeNodeKeepAliveInterval_Object=MibScalar
hpnicfdeNodeKeepAliveInterval=_HpnicfdeNodeKeepAliveInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,7),_HpnicfdeNodeKeepAliveInterval_Type())
hpnicfdeNodeKeepAliveInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodeKeepAliveInterval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfdeNodeKeepAliveInterval.setUnits(_G)
class _HpnicfdeNodePermitDynamic_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,65535)));namedValues=NamedValues(*(('permitDynamic',1),('forbidDynamic',2),('unknown',65535)))
_HpnicfdeNodePermitDynamic_Type.__name__=_C
_HpnicfdeNodePermitDynamic_Object=MibScalar
hpnicfdeNodePermitDynamic=_HpnicfdeNodePermitDynamic_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,8),_HpnicfdeNodePermitDynamic_Type())
hpnicfdeNodePermitDynamic.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodePermitDynamic.setStatus(_A)
class _HpnicfdeNodeConnTimeout_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfdeNodeConnTimeout_Type.__name__=_C
_HpnicfdeNodeConnTimeout_Object=MibScalar
hpnicfdeNodeConnTimeout=_HpnicfdeNodeConnTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,9),_HpnicfdeNodeConnTimeout_Type())
hpnicfdeNodeConnTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodeConnTimeout.setStatus(_A)
if mibBuilder.loadTexts:hpnicfdeNodeConnTimeout.setUnits(_G)
class _HpnicfdeNodeLocalPendTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfdeNodeLocalPendTimeout_Type.__name__=_C
_HpnicfdeNodeLocalPendTimeout_Object=MibScalar
hpnicfdeNodeLocalPendTimeout=_HpnicfdeNodeLocalPendTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,10),_HpnicfdeNodeLocalPendTimeout_Type())
hpnicfdeNodeLocalPendTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodeLocalPendTimeout.setStatus(_A)
if mibBuilder.loadTexts:hpnicfdeNodeLocalPendTimeout.setUnits(_G)
class _HpnicfdeNodeRemotePendTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfdeNodeRemotePendTimeout_Type.__name__=_C
_HpnicfdeNodeRemotePendTimeout_Object=MibScalar
hpnicfdeNodeRemotePendTimeout=_HpnicfdeNodeRemotePendTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,11),_HpnicfdeNodeRemotePendTimeout_Type())
hpnicfdeNodeRemotePendTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodeRemotePendTimeout.setStatus(_A)
if mibBuilder.loadTexts:hpnicfdeNodeRemotePendTimeout.setUnits(_G)
class _HpnicfdeNodeSnaCacheTimeout_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfdeNodeSnaCacheTimeout_Type.__name__=_C
_HpnicfdeNodeSnaCacheTimeout_Object=MibScalar
hpnicfdeNodeSnaCacheTimeout=_HpnicfdeNodeSnaCacheTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,12),_HpnicfdeNodeSnaCacheTimeout_Type())
hpnicfdeNodeSnaCacheTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodeSnaCacheTimeout.setStatus(_A)
if mibBuilder.loadTexts:hpnicfdeNodeSnaCacheTimeout.setUnits(_G)
class _HpnicfdeNodeExplorerTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfdeNodeExplorerTimeout_Type.__name__=_C
_HpnicfdeNodeExplorerTimeout_Object=MibScalar
hpnicfdeNodeExplorerTimeout=_HpnicfdeNodeExplorerTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,13),_HpnicfdeNodeExplorerTimeout_Type())
hpnicfdeNodeExplorerTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodeExplorerTimeout.setStatus(_A)
if mibBuilder.loadTexts:hpnicfdeNodeExplorerTimeout.setUnits(_G)
class _HpnicfdeNodeExplorerWaitTimeout_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfdeNodeExplorerWaitTimeout_Type.__name__=_C
_HpnicfdeNodeExplorerWaitTimeout_Object=MibScalar
hpnicfdeNodeExplorerWaitTimeout=_HpnicfdeNodeExplorerWaitTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,14),_HpnicfdeNodeExplorerWaitTimeout_Type())
hpnicfdeNodeExplorerWaitTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodeExplorerWaitTimeout.setStatus(_A)
if mibBuilder.loadTexts:hpnicfdeNodeExplorerWaitTimeout.setUnits(_G)
class _HpnicfdeNodeConfigSapList_Type(OctetString):defaultHexValue='FF000000000000000000000000000000';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_HpnicfdeNodeConfigSapList_Type.__name__=_K
_HpnicfdeNodeConfigSapList_Object=MibScalar
hpnicfdeNodeConfigSapList=_HpnicfdeNodeConfigSapList_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,15),_HpnicfdeNodeConfigSapList_Type())
hpnicfdeNodeConfigSapList.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodeConfigSapList.setStatus(_A)
class _HpnicfdeNodeMaxTransmission_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HpnicfdeNodeMaxTransmission_Type.__name__=_C
_HpnicfdeNodeMaxTransmission_Object=MibScalar
hpnicfdeNodeMaxTransmission=_HpnicfdeNodeMaxTransmission_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,16),_HpnicfdeNodeMaxTransmission_Type())
hpnicfdeNodeMaxTransmission.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodeMaxTransmission.setStatus(_A)
class _HpnicfdeNodeMulticastStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_HpnicfdeNodeMulticastStatus_Type.__name__=_C
_HpnicfdeNodeMulticastStatus_Object=MibScalar
hpnicfdeNodeMulticastStatus=_HpnicfdeNodeMulticastStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,17),_HpnicfdeNodeMulticastStatus_Type())
hpnicfdeNodeMulticastStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodeMulticastStatus.setStatus(_A)
_HpnicfdeNodeMulticastAddress_Type=InetAddress
_HpnicfdeNodeMulticastAddress_Object=MibScalar
hpnicfdeNodeMulticastAddress=_HpnicfdeNodeMulticastAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,18),_HpnicfdeNodeMulticastAddress_Type())
hpnicfdeNodeMulticastAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodeMulticastAddress.setStatus(_A)
class _HpnicfdeNodeResetTcpAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_HpnicfdeNodeResetTcpAll_Type.__name__=_C
_HpnicfdeNodeResetTcpAll_Object=MibScalar
hpnicfdeNodeResetTcpAll=_HpnicfdeNodeResetTcpAll_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,19),_HpnicfdeNodeResetTcpAll_Type())
hpnicfdeNodeResetTcpAll.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodeResetTcpAll.setStatus(_A)
class _HpnicfdeNodeStCapTcpNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfdeNodeStCapTcpNum_Type.__name__=_C
_HpnicfdeNodeStCapTcpNum_Object=MibScalar
hpnicfdeNodeStCapTcpNum=_HpnicfdeNodeStCapTcpNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,20),_HpnicfdeNodeStCapTcpNum_Type())
hpnicfdeNodeStCapTcpNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodeStCapTcpNum.setStatus(_A)
class _HpnicfdeNodeTcpQueueMax_Type(Integer32):defaultValue=200
_HpnicfdeNodeTcpQueueMax_Type.__name__=_C
_HpnicfdeNodeTcpQueueMax_Object=MibScalar
hpnicfdeNodeTcpQueueMax=_HpnicfdeNodeTcpQueueMax_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,1,21),_HpnicfdeNodeTcpQueueMax_Type())
hpnicfdeNodeTcpQueueMax.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdeNodeTcpQueueMax.setStatus(_A)
_HpnicfdeTConn_ObjectIdentity=ObjectIdentity
hpnicfdeTConn=_HpnicfdeTConn_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2))
_HpnicfdeTConnConfigTable_Object=MibTable
hpnicfdeTConnConfigTable=_HpnicfdeTConnConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,1))
if mibBuilder.loadTexts:hpnicfdeTConnConfigTable.setStatus(_A)
_HpnicfdeTConnConfigEntry_Object=MibTableRow
hpnicfdeTConnConfigEntry=_HpnicfdeTConnConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,1,1))
if mibBuilder.loadTexts:hpnicfdeTConnConfigEntry.setStatus(_A)
class _HpnicfdeTConnConfigVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_HpnicfdeTConnConfigVersion_Type.__name__=_K
_HpnicfdeTConnConfigVersion_Object=MibTableColumn
hpnicfdeTConnConfigVersion=_HpnicfdeTConnConfigVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,1,1,1),_HpnicfdeTConnConfigVersion_Type())
hpnicfdeTConnConfigVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeTConnConfigVersion.setStatus(_A)
class _HpnicfdeTConnConfigPriority_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_HpnicfdeTConnConfigPriority_Type.__name__=_C
_HpnicfdeTConnConfigPriority_Object=MibTableColumn
hpnicfdeTConnConfigPriority=_HpnicfdeTConnConfigPriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,1,1,2),_HpnicfdeTConnConfigPriority_Type())
hpnicfdeTConnConfigPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeTConnConfigPriority.setStatus(_A)
_HpnicfdeTConnConfigLfSize_Type=LFSize
_HpnicfdeTConnConfigLfSize_Object=MibTableColumn
hpnicfdeTConnConfigLfSize=_HpnicfdeTConnConfigLfSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,1,1,3),_HpnicfdeTConnConfigLfSize_Type())
hpnicfdeTConnConfigLfSize.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeTConnConfigLfSize.setStatus(_A)
class _HpnicfdeTConnConfigKeepaliveIntval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1200))
_HpnicfdeTConnConfigKeepaliveIntval_Type.__name__=_C
_HpnicfdeTConnConfigKeepaliveIntval_Object=MibTableColumn
hpnicfdeTConnConfigKeepaliveIntval=_HpnicfdeTConnConfigKeepaliveIntval_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,1,1,4),_HpnicfdeTConnConfigKeepaliveIntval_Type())
hpnicfdeTConnConfigKeepaliveIntval.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeTConnConfigKeepaliveIntval.setStatus(_A)
if mibBuilder.loadTexts:hpnicfdeTConnConfigKeepaliveIntval.setUnits(_G)
class _HpnicfdeTConnConfigBackup_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_HpnicfdeTConnConfigBackup_Type.__name__=_C
_HpnicfdeTConnConfigBackup_Object=MibTableColumn
hpnicfdeTConnConfigBackup=_HpnicfdeTConnConfigBackup_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,1,1,5),_HpnicfdeTConnConfigBackup_Type())
hpnicfdeTConnConfigBackup.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeTConnConfigBackup.setStatus(_A)
_HpnicfdeTConnConfigBackupTAddr_Type=TAddress
_HpnicfdeTConnConfigBackupTAddr_Object=MibTableColumn
hpnicfdeTConnConfigBackupTAddr=_HpnicfdeTConnConfigBackupTAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,1,1,6),_HpnicfdeTConnConfigBackupTAddr_Type())
hpnicfdeTConnConfigBackupTAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeTConnConfigBackupTAddr.setStatus(_A)
class _HpnicfdeTConnConfigBackupLinger_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_HpnicfdeTConnConfigBackupLinger_Type.__name__=_C
_HpnicfdeTConnConfigBackupLinger_Object=MibTableColumn
hpnicfdeTConnConfigBackupLinger=_HpnicfdeTConnConfigBackupLinger_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,1,1,7),_HpnicfdeTConnConfigBackupLinger_Type())
hpnicfdeTConnConfigBackupLinger.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeTConnConfigBackupLinger.setStatus(_A)
if mibBuilder.loadTexts:hpnicfdeTConnConfigBackupLinger.setUnits('minutes')
_HpnicfdeTConnOperTable_Object=MibTable
hpnicfdeTConnOperTable=_HpnicfdeTConnOperTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,2))
if mibBuilder.loadTexts:hpnicfdeTConnOperTable.setStatus(_A)
_HpnicfdeTConnOperEntry_Object=MibTableRow
hpnicfdeTConnOperEntry=_HpnicfdeTConnOperEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,2,1))
if mibBuilder.loadTexts:hpnicfdeTConnOperEntry.setStatus(_A)
class _HpnicfdeTConnOperPeerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('configured',1),('learningDynamic',2),('other',3)))
_HpnicfdeTConnOperPeerType_Type.__name__=_C
_HpnicfdeTConnOperPeerType_Object=MibTableColumn
hpnicfdeTConnOperPeerType=_HpnicfdeTConnOperPeerType_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,2,1,1),_HpnicfdeTConnOperPeerType_Type())
hpnicfdeTConnOperPeerType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfdeTConnOperPeerType.setStatus(_A)
_HpnicfdeTConnOperVendorID_Type=OctetString
_HpnicfdeTConnOperVendorID_Object=MibTableColumn
hpnicfdeTConnOperVendorID=_HpnicfdeTConnOperVendorID_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,2,1,2),_HpnicfdeTConnOperVendorID_Type())
hpnicfdeTConnOperVendorID.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfdeTConnOperVendorID.setStatus(_A)
_HpnicfdeTConnOperVersionString_Type=OctetString
_HpnicfdeTConnOperVersionString_Object=MibTableColumn
hpnicfdeTConnOperVersionString=_HpnicfdeTConnOperVersionString_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,2,1,3),_HpnicfdeTConnOperVersionString_Type())
hpnicfdeTConnOperVersionString.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfdeTConnOperVersionString.setStatus(_A)
_HpnicfdeTConnOperUpTime_Type=TimeTicks
_HpnicfdeTConnOperUpTime_Object=MibTableColumn
hpnicfdeTConnOperUpTime=_HpnicfdeTConnOperUpTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,2,1,4),_HpnicfdeTConnOperUpTime_Type())
hpnicfdeTConnOperUpTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfdeTConnOperUpTime.setStatus(_A)
_HpnicfdeTConnOperMulticastAddress_Type=TAddress
_HpnicfdeTConnOperMulticastAddress_Object=MibTableColumn
hpnicfdeTConnOperMulticastAddress=_HpnicfdeTConnOperMulticastAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,2,1,5),_HpnicfdeTConnOperMulticastAddress_Type())
hpnicfdeTConnOperMulticastAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfdeTConnOperMulticastAddress.setStatus(_A)
_HpnicfdeTConnOperStCapTcpNumber_Type=Integer32
_HpnicfdeTConnOperStCapTcpNumber_Object=MibTableColumn
hpnicfdeTConnOperStCapTcpNumber=_HpnicfdeTConnOperStCapTcpNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,2,1,6),_HpnicfdeTConnOperStCapTcpNumber_Type())
hpnicfdeTConnOperStCapTcpNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfdeTConnOperStCapTcpNumber.setStatus(_A)
_HpnicfdeTConnOperRecvPkts_Type=Counter32
_HpnicfdeTConnOperRecvPkts_Object=MibTableColumn
hpnicfdeTConnOperRecvPkts=_HpnicfdeTConnOperRecvPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,2,1,7),_HpnicfdeTConnOperRecvPkts_Type())
hpnicfdeTConnOperRecvPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfdeTConnOperRecvPkts.setStatus(_A)
_HpnicfdeTConnOperSendPkts_Type=Counter32
_HpnicfdeTConnOperSendPkts_Object=MibTableColumn
hpnicfdeTConnOperSendPkts=_HpnicfdeTConnOperSendPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,2,1,8),_HpnicfdeTConnOperSendPkts_Type())
hpnicfdeTConnOperSendPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfdeTConnOperSendPkts.setStatus(_A)
_HpnicfdeTConnOperDropPkts_Type=Counter32
_HpnicfdeTConnOperDropPkts_Object=MibTableColumn
hpnicfdeTConnOperDropPkts=_HpnicfdeTConnOperDropPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,2,1,9),_HpnicfdeTConnOperDropPkts_Type())
hpnicfdeTConnOperDropPkts.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfdeTConnOperDropPkts.setStatus(_A)
_HpnicfdeTConnTcpConfigTable_Object=MibTable
hpnicfdeTConnTcpConfigTable=_HpnicfdeTConnTcpConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,3))
if mibBuilder.loadTexts:hpnicfdeTConnTcpConfigTable.setStatus(_A)
_HpnicfdeTConnTcpConfigEntry_Object=MibTableRow
hpnicfdeTConnTcpConfigEntry=_HpnicfdeTConnTcpConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,3,1))
if mibBuilder.loadTexts:hpnicfdeTConnTcpConfigEntry.setStatus(_A)
class _HpnicfdeTConnTcpConfigQueueMax_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,2000))
_HpnicfdeTConnTcpConfigQueueMax_Type.__name__=_C
_HpnicfdeTConnTcpConfigQueueMax_Object=MibTableColumn
hpnicfdeTConnTcpConfigQueueMax=_HpnicfdeTConnTcpConfigQueueMax_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,2,3,1,1),_HpnicfdeTConnTcpConfigQueueMax_Type())
hpnicfdeTConnTcpConfigQueueMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeTConnTcpConfigQueueMax.setStatus(_A)
_HpnicfdeBridge_ObjectIdentity=ObjectIdentity
hpnicfdeBridge=_HpnicfdeBridge_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,62,1,3))
_HpnicfdeBridgeTable_Object=MibTable
hpnicfdeBridgeTable=_HpnicfdeBridgeTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,3,1))
if mibBuilder.loadTexts:hpnicfdeBridgeTable.setStatus(_A)
_HpnicfdeBridgeEntry_Object=MibTableRow
hpnicfdeBridgeEntry=_HpnicfdeBridgeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,3,1,1))
hpnicfdeBridgeEntry.setIndexNames((0,_J,_R))
if mibBuilder.loadTexts:hpnicfdeBridgeEntry.setStatus(_A)
class _HpnicfdeBridgeNumIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfdeBridgeNumIndex_Type.__name__=_C
_HpnicfdeBridgeNumIndex_Object=MibTableColumn
hpnicfdeBridgeNumIndex=_HpnicfdeBridgeNumIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,3,1,1,1),_HpnicfdeBridgeNumIndex_Type())
hpnicfdeBridgeNumIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfdeBridgeNumIndex.setStatus(_A)
_HpnicfdeBridgeRowStatus_Type=RowStatus
_HpnicfdeBridgeRowStatus_Object=MibTableColumn
hpnicfdeBridgeRowStatus=_HpnicfdeBridgeRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,3,1,1,2),_HpnicfdeBridgeRowStatus_Type())
hpnicfdeBridgeRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeBridgeRowStatus.setStatus(_A)
_HpnicfdeBridgeIfTable_Object=MibTable
hpnicfdeBridgeIfTable=_HpnicfdeBridgeIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,3,2))
if mibBuilder.loadTexts:hpnicfdeBridgeIfTable.setStatus(_A)
_HpnicfdeBridgeIfEntry_Object=MibTableRow
hpnicfdeBridgeIfEntry=_HpnicfdeBridgeIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,3,2,1))
hpnicfdeBridgeIfEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:hpnicfdeBridgeIfEntry.setStatus(_A)
class _HpnicfdeBridgeIfBrgGrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfdeBridgeIfBrgGrp_Type.__name__=_C
_HpnicfdeBridgeIfBrgGrp_Object=MibTableColumn
hpnicfdeBridgeIfBrgGrp=_HpnicfdeBridgeIfBrgGrp_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,3,2,1,1),_HpnicfdeBridgeIfBrgGrp_Type())
hpnicfdeBridgeIfBrgGrp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeBridgeIfBrgGrp.setStatus(_A)
_HpnicfdeBridgeIfRowStatus_Type=RowStatus
_HpnicfdeBridgeIfRowStatus_Object=MibTableColumn
hpnicfdeBridgeIfRowStatus=_HpnicfdeBridgeIfRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,3,2,1,2),_HpnicfdeBridgeIfRowStatus_Type())
hpnicfdeBridgeIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeBridgeIfRowStatus.setStatus(_A)
_HpnicfdeQllc_ObjectIdentity=ObjectIdentity
hpnicfdeQllc=_HpnicfdeQllc_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,62,1,4))
_HpnicfdeQllcTable_Object=MibTable
hpnicfdeQllcTable=_HpnicfdeQllcTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,4,1))
if mibBuilder.loadTexts:hpnicfdeQllcTable.setStatus(_A)
_HpnicfdeQllcEntry_Object=MibTableRow
hpnicfdeQllcEntry=_HpnicfdeQllcEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,4,1,1))
hpnicfdeQllcEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:hpnicfdeQllcEntry.setStatus(_A)
_HpnicfQllcX121Address_Type=Integer32
_HpnicfQllcX121Address_Object=MibTableColumn
hpnicfQllcX121Address=_HpnicfQllcX121Address_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,4,1,1,1),_HpnicfQllcX121Address_Type())
hpnicfQllcX121Address.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQllcX121Address.setStatus(_A)
_HpnicfQllcLocalMac_Type=MacAddressNC
_HpnicfQllcLocalMac_Object=MibTableColumn
hpnicfQllcLocalMac=_HpnicfQllcLocalMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,4,1,1,2),_HpnicfQllcLocalMac_Type())
hpnicfQllcLocalMac.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQllcLocalMac.setStatus(_A)
class _HpnicfQllcLocalSap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_HpnicfQllcLocalSap_Type.__name__=_K
_HpnicfQllcLocalSap_Object=MibTableColumn
hpnicfQllcLocalSap=_HpnicfQllcLocalSap_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,4,1,1,3),_HpnicfQllcLocalSap_Type())
hpnicfQllcLocalSap.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQllcLocalSap.setStatus(_A)
class _HpnicfQllcRemoteMac_Type(MacAddressNC):defaultHexValue=''
_HpnicfQllcRemoteMac_Type.__name__=_L
_HpnicfQllcRemoteMac_Object=MibTableColumn
hpnicfQllcRemoteMac=_HpnicfQllcRemoteMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,4,1,1,4),_HpnicfQllcRemoteMac_Type())
hpnicfQllcRemoteMac.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQllcRemoteMac.setStatus(_A)
class _HpnicfQllcRemoteSap_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,1))
_HpnicfQllcRemoteSap_Type.__name__=_K
_HpnicfQllcRemoteSap_Object=MibTableColumn
hpnicfQllcRemoteSap=_HpnicfQllcRemoteSap_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,4,1,1,5),_HpnicfQllcRemoteSap_Type())
hpnicfQllcRemoteSap.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQllcRemoteSap.setStatus(_A)
_HpnicfQllcRowStatus_Type=RowStatus
_HpnicfQllcRowStatus_Object=MibTableColumn
hpnicfQllcRowStatus=_HpnicfQllcRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,4,1,1,6),_HpnicfQllcRowStatus_Type())
hpnicfQllcRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQllcRowStatus.setStatus(_A)
_HpnicfdeSdlc_ObjectIdentity=ObjectIdentity
hpnicfdeSdlc=_HpnicfdeSdlc_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,62,1,5))
_HpnicfdeSdlcPortTable_Object=MibTable
hpnicfdeSdlcPortTable=_HpnicfdeSdlcPortTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,5,1))
if mibBuilder.loadTexts:hpnicfdeSdlcPortTable.setStatus(_A)
_HpnicfdeSdlcPortEntry_Object=MibTableRow
hpnicfdeSdlcPortEntry=_HpnicfdeSdlcPortEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,5,1,1))
hpnicfdeSdlcPortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:hpnicfdeSdlcPortEntry.setStatus(_A)
class _HpnicfdeSdlcPortRole_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('seconday',2),('norole',3)))
_HpnicfdeSdlcPortRole_Type.__name__=_C
_HpnicfdeSdlcPortRole_Object=MibTableColumn
hpnicfdeSdlcPortRole=_HpnicfdeSdlcPortRole_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,5,1,1,1),_HpnicfdeSdlcPortRole_Type())
hpnicfdeSdlcPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeSdlcPortRole.setStatus(_A)
class _HpnicfdeSdlcPortSendWindow_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_HpnicfdeSdlcPortSendWindow_Type.__name__=_C
_HpnicfdeSdlcPortSendWindow_Object=MibTableColumn
hpnicfdeSdlcPortSendWindow=_HpnicfdeSdlcPortSendWindow_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,5,1,1,2),_HpnicfdeSdlcPortSendWindow_Type())
hpnicfdeSdlcPortSendWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeSdlcPortSendWindow.setStatus(_A)
class _HpnicfdeSdlcPortModulo_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(8,128)));namedValues=NamedValues(*(('m8',8),('m128',128)))
_HpnicfdeSdlcPortModulo_Type.__name__=_C
_HpnicfdeSdlcPortModulo_Object=MibTableColumn
hpnicfdeSdlcPortModulo=_HpnicfdeSdlcPortModulo_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,5,1,1,3),_HpnicfdeSdlcPortModulo_Type())
hpnicfdeSdlcPortModulo.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeSdlcPortModulo.setStatus(_A)
class _HpnicfdeSdlcPortMaxPdu_Type(Integer32):defaultValue=265;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,17600))
_HpnicfdeSdlcPortMaxPdu_Type.__name__=_C
_HpnicfdeSdlcPortMaxPdu_Object=MibTableColumn
hpnicfdeSdlcPortMaxPdu=_HpnicfdeSdlcPortMaxPdu_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,5,1,1,4),_HpnicfdeSdlcPortMaxPdu_Type())
hpnicfdeSdlcPortMaxPdu.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeSdlcPortMaxPdu.setStatus(_A)
class _HpnicfdeSdlcPortMaxSendQueue_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,255))
_HpnicfdeSdlcPortMaxSendQueue_Type.__name__=_C
_HpnicfdeSdlcPortMaxSendQueue_Object=MibTableColumn
hpnicfdeSdlcPortMaxSendQueue=_HpnicfdeSdlcPortMaxSendQueue_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,5,1,1,5),_HpnicfdeSdlcPortMaxSendQueue_Type())
hpnicfdeSdlcPortMaxSendQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeSdlcPortMaxSendQueue.setStatus(_A)
class _HpnicfdeSdlcPortMaxTransmission_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfdeSdlcPortMaxTransmission_Type.__name__=_C
_HpnicfdeSdlcPortMaxTransmission_Object=MibTableColumn
hpnicfdeSdlcPortMaxTransmission=_HpnicfdeSdlcPortMaxTransmission_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,5,1,1,6),_HpnicfdeSdlcPortMaxTransmission_Type())
hpnicfdeSdlcPortMaxTransmission.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeSdlcPortMaxTransmission.setStatus(_A)
class _HpnicfdeSdlcPortSimultaneousEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_HpnicfdeSdlcPortSimultaneousEnable_Type.__name__=_C
_HpnicfdeSdlcPortSimultaneousEnable_Object=MibTableColumn
hpnicfdeSdlcPortSimultaneousEnable=_HpnicfdeSdlcPortSimultaneousEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,5,1,1,7),_HpnicfdeSdlcPortSimultaneousEnable_Type())
hpnicfdeSdlcPortSimultaneousEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeSdlcPortSimultaneousEnable.setStatus(_A)
class _HpnicfdeSdlcPortTimerACK_Type(Integer32):defaultValue=3000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_HpnicfdeSdlcPortTimerACK_Type.__name__=_C
_HpnicfdeSdlcPortTimerACK_Object=MibTableColumn
hpnicfdeSdlcPortTimerACK=_HpnicfdeSdlcPortTimerACK_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,5,1,1,8),_HpnicfdeSdlcPortTimerACK_Type())
hpnicfdeSdlcPortTimerACK.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeSdlcPortTimerACK.setStatus(_A)
if mibBuilder.loadTexts:hpnicfdeSdlcPortTimerACK.setUnits(_F)
class _HpnicfdeSdlcPortTimerLifeTime_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_HpnicfdeSdlcPortTimerLifeTime_Type.__name__=_C
_HpnicfdeSdlcPortTimerLifeTime_Object=MibTableColumn
hpnicfdeSdlcPortTimerLifeTime=_HpnicfdeSdlcPortTimerLifeTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,5,1,1,9),_HpnicfdeSdlcPortTimerLifeTime_Type())
hpnicfdeSdlcPortTimerLifeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeSdlcPortTimerLifeTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfdeSdlcPortTimerLifeTime.setUnits(_F)
class _HpnicfdeSdlcPortTimerPollPause_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_HpnicfdeSdlcPortTimerPollPause_Type.__name__=_C
_HpnicfdeSdlcPortTimerPollPause_Object=MibTableColumn
hpnicfdeSdlcPortTimerPollPause=_HpnicfdeSdlcPortTimerPollPause_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,5,1,1,10),_HpnicfdeSdlcPortTimerPollPause_Type())
hpnicfdeSdlcPortTimerPollPause.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeSdlcPortTimerPollPause.setStatus(_A)
if mibBuilder.loadTexts:hpnicfdeSdlcPortTimerPollPause.setUnits(_F)
_HpnicfdeSdlcPortRowStatus_Type=RowStatus
_HpnicfdeSdlcPortRowStatus_Object=MibTableColumn
hpnicfdeSdlcPortRowStatus=_HpnicfdeSdlcPortRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,5,1,1,11),_HpnicfdeSdlcPortRowStatus_Type())
hpnicfdeSdlcPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeSdlcPortRowStatus.setStatus(_A)
_HpnicfdeLlc2_ObjectIdentity=ObjectIdentity
hpnicfdeLlc2=_HpnicfdeLlc2_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,62,1,6))
_HpnicfdeLlc2PortTable_Object=MibTable
hpnicfdeLlc2PortTable=_HpnicfdeLlc2PortTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,6,1))
if mibBuilder.loadTexts:hpnicfdeLlc2PortTable.setStatus(_A)
_HpnicfdeLlc2PortEntry_Object=MibTableRow
hpnicfdeLlc2PortEntry=_HpnicfdeLlc2PortEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,6,1,1))
hpnicfdeLlc2PortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:hpnicfdeLlc2PortEntry.setStatus(_A)
class _HpnicfdeLlc2PortMaxAck_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_HpnicfdeLlc2PortMaxAck_Type.__name__=_C
_HpnicfdeLlc2PortMaxAck_Object=MibTableColumn
hpnicfdeLlc2PortMaxAck=_HpnicfdeLlc2PortMaxAck_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,6,1,1,1),_HpnicfdeLlc2PortMaxAck_Type())
hpnicfdeLlc2PortMaxAck.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeLlc2PortMaxAck.setStatus(_A)
class _HpnicfdeLlc2PortMaxPdu_Type(Integer32):defaultValue=1493;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1700))
_HpnicfdeLlc2PortMaxPdu_Type.__name__=_C
_HpnicfdeLlc2PortMaxPdu_Object=MibTableColumn
hpnicfdeLlc2PortMaxPdu=_HpnicfdeLlc2PortMaxPdu_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,6,1,1,2),_HpnicfdeLlc2PortMaxPdu_Type())
hpnicfdeLlc2PortMaxPdu.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeLlc2PortMaxPdu.setStatus(_A)
class _HpnicfdeLlc2PortMaxSendQueue_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,200))
_HpnicfdeLlc2PortMaxSendQueue_Type.__name__=_C
_HpnicfdeLlc2PortMaxSendQueue_Object=MibTableColumn
hpnicfdeLlc2PortMaxSendQueue=_HpnicfdeLlc2PortMaxSendQueue_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,6,1,1,3),_HpnicfdeLlc2PortMaxSendQueue_Type())
hpnicfdeLlc2PortMaxSendQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeLlc2PortMaxSendQueue.setStatus(_A)
class _HpnicfdeLlc2PortMaxTransmission_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfdeLlc2PortMaxTransmission_Type.__name__=_C
_HpnicfdeLlc2PortMaxTransmission_Object=MibTableColumn
hpnicfdeLlc2PortMaxTransmission=_HpnicfdeLlc2PortMaxTransmission_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,6,1,1,4),_HpnicfdeLlc2PortMaxTransmission_Type())
hpnicfdeLlc2PortMaxTransmission.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeLlc2PortMaxTransmission.setStatus(_A)
class _HpnicfdeLlc2PortModulo_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(8,128)));namedValues=NamedValues(*(('m8',8),('m128',128)))
_HpnicfdeLlc2PortModulo_Type.__name__=_C
_HpnicfdeLlc2PortModulo_Object=MibTableColumn
hpnicfdeLlc2PortModulo=_HpnicfdeLlc2PortModulo_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,6,1,1,5),_HpnicfdeLlc2PortModulo_Type())
hpnicfdeLlc2PortModulo.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeLlc2PortModulo.setStatus(_A)
class _HpnicfdeLlc2PortReceiveWindow_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_HpnicfdeLlc2PortReceiveWindow_Type.__name__=_C
_HpnicfdeLlc2PortReceiveWindow_Object=MibTableColumn
hpnicfdeLlc2PortReceiveWindow=_HpnicfdeLlc2PortReceiveWindow_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,6,1,1,6),_HpnicfdeLlc2PortReceiveWindow_Type())
hpnicfdeLlc2PortReceiveWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeLlc2PortReceiveWindow.setStatus(_A)
class _HpnicfdeLlc2PortTimerAck_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_HpnicfdeLlc2PortTimerAck_Type.__name__=_C
_HpnicfdeLlc2PortTimerAck_Object=MibTableColumn
hpnicfdeLlc2PortTimerAck=_HpnicfdeLlc2PortTimerAck_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,6,1,1,7),_HpnicfdeLlc2PortTimerAck_Type())
hpnicfdeLlc2PortTimerAck.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeLlc2PortTimerAck.setStatus(_A)
if mibBuilder.loadTexts:hpnicfdeLlc2PortTimerAck.setUnits(_F)
class _HpnicfdeLlc2PortTimerAckDelay_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_HpnicfdeLlc2PortTimerAckDelay_Type.__name__=_C
_HpnicfdeLlc2PortTimerAckDelay_Object=MibTableColumn
hpnicfdeLlc2PortTimerAckDelay=_HpnicfdeLlc2PortTimerAckDelay_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,6,1,1,8),_HpnicfdeLlc2PortTimerAckDelay_Type())
hpnicfdeLlc2PortTimerAckDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeLlc2PortTimerAckDelay.setStatus(_A)
if mibBuilder.loadTexts:hpnicfdeLlc2PortTimerAckDelay.setUnits(_F)
class _HpnicfdeLlc2PortTimerDetect_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_HpnicfdeLlc2PortTimerDetect_Type.__name__=_C
_HpnicfdeLlc2PortTimerDetect_Object=MibTableColumn
hpnicfdeLlc2PortTimerDetect=_HpnicfdeLlc2PortTimerDetect_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,6,1,1,9),_HpnicfdeLlc2PortTimerDetect_Type())
hpnicfdeLlc2PortTimerDetect.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeLlc2PortTimerDetect.setStatus(_A)
if mibBuilder.loadTexts:hpnicfdeLlc2PortTimerDetect.setUnits(_F)
class _HpnicfdeLlc2PortTimerBusy_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_HpnicfdeLlc2PortTimerBusy_Type.__name__=_C
_HpnicfdeLlc2PortTimerBusy_Object=MibTableColumn
hpnicfdeLlc2PortTimerBusy=_HpnicfdeLlc2PortTimerBusy_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,6,1,1,10),_HpnicfdeLlc2PortTimerBusy_Type())
hpnicfdeLlc2PortTimerBusy.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeLlc2PortTimerBusy.setStatus(_A)
if mibBuilder.loadTexts:hpnicfdeLlc2PortTimerBusy.setUnits(_F)
class _HpnicfdeLlc2PortTimerPoll_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_HpnicfdeLlc2PortTimerPoll_Type.__name__=_C
_HpnicfdeLlc2PortTimerPoll_Object=MibTableColumn
hpnicfdeLlc2PortTimerPoll=_HpnicfdeLlc2PortTimerPoll_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,6,1,1,11),_HpnicfdeLlc2PortTimerPoll_Type())
hpnicfdeLlc2PortTimerPoll.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeLlc2PortTimerPoll.setStatus(_A)
if mibBuilder.loadTexts:hpnicfdeLlc2PortTimerPoll.setUnits(_F)
class _HpnicfdeLlc2PortTimerReject_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_HpnicfdeLlc2PortTimerReject_Type.__name__=_C
_HpnicfdeLlc2PortTimerReject_Object=MibTableColumn
hpnicfdeLlc2PortTimerReject=_HpnicfdeLlc2PortTimerReject_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,6,1,1,12),_HpnicfdeLlc2PortTimerReject_Type())
hpnicfdeLlc2PortTimerReject.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeLlc2PortTimerReject.setStatus(_A)
if mibBuilder.loadTexts:hpnicfdeLlc2PortTimerReject.setUnits(_F)
_HpnicfdeLlc2PortRowStatus_Type=RowStatus
_HpnicfdeLlc2PortRowStatus_Object=MibTableColumn
hpnicfdeLlc2PortRowStatus=_HpnicfdeLlc2PortRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,6,1,1,13),_HpnicfdeLlc2PortRowStatus_Type())
hpnicfdeLlc2PortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeLlc2PortRowStatus.setStatus(_A)
_HpnicfdeReachableCache_ObjectIdentity=ObjectIdentity
hpnicfdeReachableCache=_HpnicfdeReachableCache_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,62,1,7))
_HpnicfdeRchCacheStat_ObjectIdentity=ObjectIdentity
hpnicfdeRchCacheStat=_HpnicfdeRchCacheStat_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,62,1,7,1))
_HpnicfdeRchCacheMaxIndex_Type=Integer32
_HpnicfdeRchCacheMaxIndex_Object=MibScalar
hpnicfdeRchCacheMaxIndex=_HpnicfdeRchCacheMaxIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,7,1,1),_HpnicfdeRchCacheMaxIndex_Type())
hpnicfdeRchCacheMaxIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfdeRchCacheMaxIndex.setStatus(_A)
_HpnicfdeRchCacheNextIndex_Type=Integer32
_HpnicfdeRchCacheNextIndex_Object=MibScalar
hpnicfdeRchCacheNextIndex=_HpnicfdeRchCacheNextIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,7,1,2),_HpnicfdeRchCacheNextIndex_Type())
hpnicfdeRchCacheNextIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfdeRchCacheNextIndex.setStatus(_A)
_HpnicfdeRchCacheTable_Object=MibTable
hpnicfdeRchCacheTable=_HpnicfdeRchCacheTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,7,3))
if mibBuilder.loadTexts:hpnicfdeRchCacheTable.setStatus(_A)
_HpnicfdeRchCacheEntry_Object=MibTableRow
hpnicfdeRchCacheEntry=_HpnicfdeRchCacheEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,7,3,1))
hpnicfdeRchCacheEntry.setIndexNames((0,_J,_S))
if mibBuilder.loadTexts:hpnicfdeRchCacheEntry.setStatus(_A)
_HpnicfdeRchCacheIndex_Type=Integer32
_HpnicfdeRchCacheIndex_Object=MibTableColumn
hpnicfdeRchCacheIndex=_HpnicfdeRchCacheIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,7,3,1,1),_HpnicfdeRchCacheIndex_Type())
hpnicfdeRchCacheIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfdeRchCacheIndex.setStatus(_A)
class _HpnicfdeRchCacheStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('found',1),('verify',2),('noCacheInfo',3),('exploring',4),('waiting',5)))
_HpnicfdeRchCacheStatus_Type.__name__=_C
_HpnicfdeRchCacheStatus_Object=MibTableColumn
hpnicfdeRchCacheStatus=_HpnicfdeRchCacheStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,7,3,1,2),_HpnicfdeRchCacheStatus_Type())
hpnicfdeRchCacheStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfdeRchCacheStatus.setStatus(_A)
_HpnicfdeRchCacheRemainTime_Type=TimeTicks
_HpnicfdeRchCacheRemainTime_Object=MibTableColumn
hpnicfdeRchCacheRemainTime=_HpnicfdeRchCacheRemainTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,7,3,1,3),_HpnicfdeRchCacheRemainTime_Type())
hpnicfdeRchCacheRemainTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfdeRchCacheRemainTime.setStatus(_A)
_HpnicfdeRchCacheMac_Type=MacAddressNC
_HpnicfdeRchCacheMac_Object=MibTableColumn
hpnicfdeRchCacheMac=_HpnicfdeRchCacheMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,7,3,1,4),_HpnicfdeRchCacheMac_Type())
hpnicfdeRchCacheMac.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeRchCacheMac.setStatus(_A)
_HpnicfdeRchCacheRemoteIpAddrType_Type=InetAddressType
_HpnicfdeRchCacheRemoteIpAddrType_Object=MibTableColumn
hpnicfdeRchCacheRemoteIpAddrType=_HpnicfdeRchCacheRemoteIpAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,7,3,1,5),_HpnicfdeRchCacheRemoteIpAddrType_Type())
hpnicfdeRchCacheRemoteIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeRchCacheRemoteIpAddrType.setStatus(_A)
_HpnicfdeRchCacheRemoteIp_Type=InetAddress
_HpnicfdeRchCacheRemoteIp_Object=MibTableColumn
hpnicfdeRchCacheRemoteIp=_HpnicfdeRchCacheRemoteIp_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,7,3,1,6),_HpnicfdeRchCacheRemoteIp_Type())
hpnicfdeRchCacheRemoteIp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeRchCacheRemoteIp.setStatus(_A)
_HpnicfdeRchCacheRowStatus_Type=RowStatus
_HpnicfdeRchCacheRowStatus_Object=MibTableColumn
hpnicfdeRchCacheRowStatus=_HpnicfdeRchCacheRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,7,3,1,7),_HpnicfdeRchCacheRowStatus_Type())
hpnicfdeRchCacheRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeRchCacheRowStatus.setStatus(_A)
_HpnicfdeEthernetBackup_ObjectIdentity=ObjectIdentity
hpnicfdeEthernetBackup=_HpnicfdeEthernetBackup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,62,1,8))
_HpnicfdeEBMacMapStat_ObjectIdentity=ObjectIdentity
hpnicfdeEBMacMapStat=_HpnicfdeEBMacMapStat_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,62,1,8,1))
_HpnicfdeEBMacMapMaxIndex_Type=Integer32
_HpnicfdeEBMacMapMaxIndex_Object=MibScalar
hpnicfdeEBMacMapMaxIndex=_HpnicfdeEBMacMapMaxIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,8,1,1),_HpnicfdeEBMacMapMaxIndex_Type())
hpnicfdeEBMacMapMaxIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfdeEBMacMapMaxIndex.setStatus(_A)
_HpnicfdeEBMacMapNextIndex_Type=Integer32
_HpnicfdeEBMacMapNextIndex_Object=MibScalar
hpnicfdeEBMacMapNextIndex=_HpnicfdeEBMacMapNextIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,8,1,2),_HpnicfdeEBMacMapNextIndex_Type())
hpnicfdeEBMacMapNextIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfdeEBMacMapNextIndex.setStatus(_A)
_HpnicfdeEBIfTable_Object=MibTable
hpnicfdeEBIfTable=_HpnicfdeEBIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,8,3))
if mibBuilder.loadTexts:hpnicfdeEBIfTable.setStatus(_A)
_HpnicfdeEBIfEntry_Object=MibTableRow
hpnicfdeEBIfEntry=_HpnicfdeEBIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,8,3,1))
hpnicfdeEBIfEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:hpnicfdeEBIfEntry.setStatus(_A)
class _HpnicfdeEBMulticastMac_Type(MacAddressNC):defaultHexValue='000000000000'
_HpnicfdeEBMulticastMac_Type.__name__=_L
_HpnicfdeEBMulticastMac_Object=MibTableColumn
hpnicfdeEBMulticastMac=_HpnicfdeEBMulticastMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,8,3,1,1),_HpnicfdeEBMulticastMac_Type())
hpnicfdeEBMulticastMac.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeEBMulticastMac.setStatus(_A)
class _HpnicfdeEBPriority_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_HpnicfdeEBPriority_Type.__name__=_C
_HpnicfdeEBPriority_Object=MibTableColumn
hpnicfdeEBPriority=_HpnicfdeEBPriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,8,3,1,2),_HpnicfdeEBPriority_Type())
hpnicfdeEBPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeEBPriority.setStatus(_A)
class _HpnicfdeEBtimer_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_HpnicfdeEBtimer_Type.__name__=_C
_HpnicfdeEBtimer_Object=MibTableColumn
hpnicfdeEBtimer=_HpnicfdeEBtimer_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,8,3,1,3),_HpnicfdeEBtimer_Type())
hpnicfdeEBtimer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeEBtimer.setStatus(_A)
_HpnicfdeEBRowStatus_Type=RowStatus
_HpnicfdeEBRowStatus_Object=MibTableColumn
hpnicfdeEBRowStatus=_HpnicfdeEBRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,8,3,1,4),_HpnicfdeEBRowStatus_Type())
hpnicfdeEBRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeEBRowStatus.setStatus(_A)
_HpnicfdeEBMacMapTable_Object=MibTable
hpnicfdeEBMacMapTable=_HpnicfdeEBMacMapTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,8,4))
if mibBuilder.loadTexts:hpnicfdeEBMacMapTable.setStatus(_A)
_HpnicfdeEBMacMapEntry_Object=MibTableRow
hpnicfdeEBMacMapEntry=_HpnicfdeEBMacMapEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,8,4,1))
hpnicfdeEBMacMapEntry.setIndexNames((0,_H,_I),(0,_J,_T))
if mibBuilder.loadTexts:hpnicfdeEBMacMapEntry.setStatus(_A)
_HpnicfdeEBMacMapIndex_Type=Integer32
_HpnicfdeEBMacMapIndex_Object=MibTableColumn
hpnicfdeEBMacMapIndex=_HpnicfdeEBMacMapIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,8,4,1,1),_HpnicfdeEBMacMapIndex_Type())
hpnicfdeEBMacMapIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:hpnicfdeEBMacMapIndex.setStatus(_A)
_HpnicfdeEBMacMapLocalMac_Type=MacAddressNC
_HpnicfdeEBMacMapLocalMac_Object=MibTableColumn
hpnicfdeEBMacMapLocalMac=_HpnicfdeEBMacMapLocalMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,8,4,1,2),_HpnicfdeEBMacMapLocalMac_Type())
hpnicfdeEBMacMapLocalMac.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeEBMacMapLocalMac.setStatus(_A)
_HpnicfdeEBMacMapRemoteMac_Type=MacAddressNC
_HpnicfdeEBMacMapRemoteMac_Object=MibTableColumn
hpnicfdeEBMacMapRemoteMac=_HpnicfdeEBMacMapRemoteMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,8,4,1,3),_HpnicfdeEBMacMapRemoteMac_Type())
hpnicfdeEBMacMapRemoteMac.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeEBMacMapRemoteMac.setStatus(_A)
_HpnicfdeEBMacMapNeighbour_Type=MacAddressNC
_HpnicfdeEBMacMapNeighbour_Object=MibTableColumn
hpnicfdeEBMacMapNeighbour=_HpnicfdeEBMacMapNeighbour_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,8,4,1,4),_HpnicfdeEBMacMapNeighbour_Type())
hpnicfdeEBMacMapNeighbour.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeEBMacMapNeighbour.setStatus(_A)
_HpnicfdeEBMacMapRowStatus_Type=RowStatus
_HpnicfdeEBMacMapRowStatus_Object=MibTableColumn
hpnicfdeEBMacMapRowStatus=_HpnicfdeEBMacMapRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,62,1,8,4,1,5),_HpnicfdeEBMacMapRowStatus_Type())
hpnicfdeEBMacMapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdeEBMacMapRowStatus.setStatus(_A)
dlswTConnConfigEntry.registerAugmentions((_J,_U))
hpnicfdeTConnConfigEntry.setIndexNames(*dlswTConnConfigEntry.getIndexNames())
dlswTConnOperEntry.registerAugmentions((_J,_V))
hpnicfdeTConnOperEntry.setIndexNames(*dlswTConnOperEntry.getIndexNames())
dlswTConnTcpConfigEntry.registerAugmentions((_J,_W))
hpnicfdeTConnTcpConfigEntry.setIndexNames(*dlswTConnTcpConfigEntry.getIndexNames())
mibBuilder.exportSymbols(_J,**{'hpnicfDlswExt':hpnicfDlswExt,'hpnicfDlswExtMIBObjects':hpnicfDlswExtMIBObjects,'hpnicfdeNode':hpnicfdeNode,'hpnicfdeNodeVendorID':hpnicfdeNodeVendorID,'hpnicfdeNodeIpAddrType':hpnicfdeNodeIpAddrType,'hpnicfdeNodeLocalAddr':hpnicfdeNodeLocalAddr,'hpnicfdeNodePriority':hpnicfdeNodePriority,'hpnicfdeNodeInitPacingWindow':hpnicfdeNodeInitPacingWindow,'hpnicfdeNodeMaxPacingWindow':hpnicfdeNodeMaxPacingWindow,'hpnicfdeNodeKeepAliveInterval':hpnicfdeNodeKeepAliveInterval,'hpnicfdeNodePermitDynamic':hpnicfdeNodePermitDynamic,'hpnicfdeNodeConnTimeout':hpnicfdeNodeConnTimeout,'hpnicfdeNodeLocalPendTimeout':hpnicfdeNodeLocalPendTimeout,'hpnicfdeNodeRemotePendTimeout':hpnicfdeNodeRemotePendTimeout,'hpnicfdeNodeSnaCacheTimeout':hpnicfdeNodeSnaCacheTimeout,'hpnicfdeNodeExplorerTimeout':hpnicfdeNodeExplorerTimeout,'hpnicfdeNodeExplorerWaitTimeout':hpnicfdeNodeExplorerWaitTimeout,'hpnicfdeNodeConfigSapList':hpnicfdeNodeConfigSapList,'hpnicfdeNodeMaxTransmission':hpnicfdeNodeMaxTransmission,'hpnicfdeNodeMulticastStatus':hpnicfdeNodeMulticastStatus,'hpnicfdeNodeMulticastAddress':hpnicfdeNodeMulticastAddress,'hpnicfdeNodeResetTcpAll':hpnicfdeNodeResetTcpAll,'hpnicfdeNodeStCapTcpNum':hpnicfdeNodeStCapTcpNum,'hpnicfdeNodeTcpQueueMax':hpnicfdeNodeTcpQueueMax,'hpnicfdeTConn':hpnicfdeTConn,'hpnicfdeTConnConfigTable':hpnicfdeTConnConfigTable,_U:hpnicfdeTConnConfigEntry,'hpnicfdeTConnConfigVersion':hpnicfdeTConnConfigVersion,'hpnicfdeTConnConfigPriority':hpnicfdeTConnConfigPriority,'hpnicfdeTConnConfigLfSize':hpnicfdeTConnConfigLfSize,'hpnicfdeTConnConfigKeepaliveIntval':hpnicfdeTConnConfigKeepaliveIntval,'hpnicfdeTConnConfigBackup':hpnicfdeTConnConfigBackup,'hpnicfdeTConnConfigBackupTAddr':hpnicfdeTConnConfigBackupTAddr,'hpnicfdeTConnConfigBackupLinger':hpnicfdeTConnConfigBackupLinger,'hpnicfdeTConnOperTable':hpnicfdeTConnOperTable,_V:hpnicfdeTConnOperEntry,'hpnicfdeTConnOperPeerType':hpnicfdeTConnOperPeerType,'hpnicfdeTConnOperVendorID':hpnicfdeTConnOperVendorID,'hpnicfdeTConnOperVersionString':hpnicfdeTConnOperVersionString,'hpnicfdeTConnOperUpTime':hpnicfdeTConnOperUpTime,'hpnicfdeTConnOperMulticastAddress':hpnicfdeTConnOperMulticastAddress,'hpnicfdeTConnOperStCapTcpNumber':hpnicfdeTConnOperStCapTcpNumber,'hpnicfdeTConnOperRecvPkts':hpnicfdeTConnOperRecvPkts,'hpnicfdeTConnOperSendPkts':hpnicfdeTConnOperSendPkts,'hpnicfdeTConnOperDropPkts':hpnicfdeTConnOperDropPkts,'hpnicfdeTConnTcpConfigTable':hpnicfdeTConnTcpConfigTable,_W:hpnicfdeTConnTcpConfigEntry,'hpnicfdeTConnTcpConfigQueueMax':hpnicfdeTConnTcpConfigQueueMax,'hpnicfdeBridge':hpnicfdeBridge,'hpnicfdeBridgeTable':hpnicfdeBridgeTable,'hpnicfdeBridgeEntry':hpnicfdeBridgeEntry,_R:hpnicfdeBridgeNumIndex,'hpnicfdeBridgeRowStatus':hpnicfdeBridgeRowStatus,'hpnicfdeBridgeIfTable':hpnicfdeBridgeIfTable,'hpnicfdeBridgeIfEntry':hpnicfdeBridgeIfEntry,'hpnicfdeBridgeIfBrgGrp':hpnicfdeBridgeIfBrgGrp,'hpnicfdeBridgeIfRowStatus':hpnicfdeBridgeIfRowStatus,'hpnicfdeQllc':hpnicfdeQllc,'hpnicfdeQllcTable':hpnicfdeQllcTable,'hpnicfdeQllcEntry':hpnicfdeQllcEntry,'hpnicfQllcX121Address':hpnicfQllcX121Address,'hpnicfQllcLocalMac':hpnicfQllcLocalMac,'hpnicfQllcLocalSap':hpnicfQllcLocalSap,'hpnicfQllcRemoteMac':hpnicfQllcRemoteMac,'hpnicfQllcRemoteSap':hpnicfQllcRemoteSap,'hpnicfQllcRowStatus':hpnicfQllcRowStatus,'hpnicfdeSdlc':hpnicfdeSdlc,'hpnicfdeSdlcPortTable':hpnicfdeSdlcPortTable,'hpnicfdeSdlcPortEntry':hpnicfdeSdlcPortEntry,'hpnicfdeSdlcPortRole':hpnicfdeSdlcPortRole,'hpnicfdeSdlcPortSendWindow':hpnicfdeSdlcPortSendWindow,'hpnicfdeSdlcPortModulo':hpnicfdeSdlcPortModulo,'hpnicfdeSdlcPortMaxPdu':hpnicfdeSdlcPortMaxPdu,'hpnicfdeSdlcPortMaxSendQueue':hpnicfdeSdlcPortMaxSendQueue,'hpnicfdeSdlcPortMaxTransmission':hpnicfdeSdlcPortMaxTransmission,'hpnicfdeSdlcPortSimultaneousEnable':hpnicfdeSdlcPortSimultaneousEnable,'hpnicfdeSdlcPortTimerACK':hpnicfdeSdlcPortTimerACK,'hpnicfdeSdlcPortTimerLifeTime':hpnicfdeSdlcPortTimerLifeTime,'hpnicfdeSdlcPortTimerPollPause':hpnicfdeSdlcPortTimerPollPause,'hpnicfdeSdlcPortRowStatus':hpnicfdeSdlcPortRowStatus,'hpnicfdeLlc2':hpnicfdeLlc2,'hpnicfdeLlc2PortTable':hpnicfdeLlc2PortTable,'hpnicfdeLlc2PortEntry':hpnicfdeLlc2PortEntry,'hpnicfdeLlc2PortMaxAck':hpnicfdeLlc2PortMaxAck,'hpnicfdeLlc2PortMaxPdu':hpnicfdeLlc2PortMaxPdu,'hpnicfdeLlc2PortMaxSendQueue':hpnicfdeLlc2PortMaxSendQueue,'hpnicfdeLlc2PortMaxTransmission':hpnicfdeLlc2PortMaxTransmission,'hpnicfdeLlc2PortModulo':hpnicfdeLlc2PortModulo,'hpnicfdeLlc2PortReceiveWindow':hpnicfdeLlc2PortReceiveWindow,'hpnicfdeLlc2PortTimerAck':hpnicfdeLlc2PortTimerAck,'hpnicfdeLlc2PortTimerAckDelay':hpnicfdeLlc2PortTimerAckDelay,'hpnicfdeLlc2PortTimerDetect':hpnicfdeLlc2PortTimerDetect,'hpnicfdeLlc2PortTimerBusy':hpnicfdeLlc2PortTimerBusy,'hpnicfdeLlc2PortTimerPoll':hpnicfdeLlc2PortTimerPoll,'hpnicfdeLlc2PortTimerReject':hpnicfdeLlc2PortTimerReject,'hpnicfdeLlc2PortRowStatus':hpnicfdeLlc2PortRowStatus,'hpnicfdeReachableCache':hpnicfdeReachableCache,'hpnicfdeRchCacheStat':hpnicfdeRchCacheStat,'hpnicfdeRchCacheMaxIndex':hpnicfdeRchCacheMaxIndex,'hpnicfdeRchCacheNextIndex':hpnicfdeRchCacheNextIndex,'hpnicfdeRchCacheTable':hpnicfdeRchCacheTable,'hpnicfdeRchCacheEntry':hpnicfdeRchCacheEntry,_S:hpnicfdeRchCacheIndex,'hpnicfdeRchCacheStatus':hpnicfdeRchCacheStatus,'hpnicfdeRchCacheRemainTime':hpnicfdeRchCacheRemainTime,'hpnicfdeRchCacheMac':hpnicfdeRchCacheMac,'hpnicfdeRchCacheRemoteIpAddrType':hpnicfdeRchCacheRemoteIpAddrType,'hpnicfdeRchCacheRemoteIp':hpnicfdeRchCacheRemoteIp,'hpnicfdeRchCacheRowStatus':hpnicfdeRchCacheRowStatus,'hpnicfdeEthernetBackup':hpnicfdeEthernetBackup,'hpnicfdeEBMacMapStat':hpnicfdeEBMacMapStat,'hpnicfdeEBMacMapMaxIndex':hpnicfdeEBMacMapMaxIndex,'hpnicfdeEBMacMapNextIndex':hpnicfdeEBMacMapNextIndex,'hpnicfdeEBIfTable':hpnicfdeEBIfTable,'hpnicfdeEBIfEntry':hpnicfdeEBIfEntry,'hpnicfdeEBMulticastMac':hpnicfdeEBMulticastMac,'hpnicfdeEBPriority':hpnicfdeEBPriority,'hpnicfdeEBtimer':hpnicfdeEBtimer,'hpnicfdeEBRowStatus':hpnicfdeEBRowStatus,'hpnicfdeEBMacMapTable':hpnicfdeEBMacMapTable,'hpnicfdeEBMacMapEntry':hpnicfdeEBMacMapEntry,_T:hpnicfdeEBMacMapIndex,'hpnicfdeEBMacMapLocalMac':hpnicfdeEBMacMapLocalMac,'hpnicfdeEBMacMapRemoteMac':hpnicfdeEBMacMapRemoteMac,'hpnicfdeEBMacMapNeighbour':hpnicfdeEBMacMapNeighbour,'hpnicfdeEBMacMapRowStatus':hpnicfdeEBMacMapRowStatus})