_Y='cigDhcpServersNotificationPoolNetwork'
_X='cigDhcpServersNotificationConflictDetectionMethod'
_W='cigDhcpServersNotificationClientHostName'
_V='cigDhcpServersVendorSpecificOptionIndex'
_U='cigDhcpServersVendorSpecificOptionPoolIndex'
_T='cigDhcpServersOptionIndex'
_S='cigDhcpServersOptionPoolIndex'
_R='cigDhcpServersPoolIndex'
_Q='cigDhcpServersNotificationIpAddr'
_P='cigTftpServersNotificationErrorString'
_O='cigTftpServersNotificationFilename'
_N='cigTftpServersNotificationClientIpAddr'
_M='cigDhcpServersNotificationClientIdentifier'
_L='TruthValue'
_K='00000000'
_J='Integer32'
_I='OctetString'
_H='accessible-for-notify'
_G='IpAddress'
_F='DisplayString'
_E='CIG-SERVERS-MIB'
_D='Unsigned32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,_G,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'PhysAddress','RowStatus','TextualConvention','TimeInterval',_L)
cigServers=ModuleIdentity((1,3,6,1,4,1,6889,2,1,16))
_Avaya_ObjectIdentity=ObjectIdentity
avaya=_Avaya_ObjectIdentity((1,3,6,1,4,1,6889))
_Mibs_ObjectIdentity=ObjectIdentity
mibs=_Mibs_ObjectIdentity((1,3,6,1,4,1,6889,2))
_Lsg_ObjectIdentity=ObjectIdentity
lsg=_Lsg_ObjectIdentity((1,3,6,1,4,1,6889,2,1))
_CigTftpServers_ObjectIdentity=ObjectIdentity
cigTftpServers=_CigTftpServers_ObjectIdentity((1,3,6,1,4,1,6889,2,1,16,1))
_CigTftpServersNotification_ObjectIdentity=ObjectIdentity
cigTftpServersNotification=_CigTftpServersNotification_ObjectIdentity((1,3,6,1,4,1,6889,2,1,16,1,0))
_CigTftpServersGenConfig_ObjectIdentity=ObjectIdentity
cigTftpServersGenConfig=_CigTftpServersGenConfig_ObjectIdentity((1,3,6,1,4,1,6889,2,1,16,1,1))
class _CigTftpServersMode_Type(TruthValue):defaultValue=2
_CigTftpServersMode_Type.__name__=_L
_CigTftpServersMode_Object=MibScalar
cigTftpServersMode=_CigTftpServersMode_Object((1,3,6,1,4,1,6889,2,1,16,1,1,1),_CigTftpServersMode_Type())
cigTftpServersMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cigTftpServersMode.setStatus(_A)
class _CigTftpServersResetStatCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_CigTftpServersResetStatCounters_Type.__name__=_J
_CigTftpServersResetStatCounters_Object=MibScalar
cigTftpServersResetStatCounters=_CigTftpServersResetStatCounters_Object((1,3,6,1,4,1,6889,2,1,16,1,1,2),_CigTftpServersResetStatCounters_Type())
cigTftpServersResetStatCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:cigTftpServersResetStatCounters.setStatus(_A)
_CigTftpServersMemoryAllocation_ObjectIdentity=ObjectIdentity
cigTftpServersMemoryAllocation=_CigTftpServersMemoryAllocation_ObjectIdentity((1,3,6,1,4,1,6889,2,1,16,1,2))
class _CigTftpServersTotalBytesUsedInNvram_Type(Unsigned32):defaultValue=0
_CigTftpServersTotalBytesUsedInNvram_Type.__name__=_D
_CigTftpServersTotalBytesUsedInNvram_Object=MibScalar
cigTftpServersTotalBytesUsedInNvram=_CigTftpServersTotalBytesUsedInNvram_Object((1,3,6,1,4,1,6889,2,1,16,1,2,1),_CigTftpServersTotalBytesUsedInNvram_Type())
cigTftpServersTotalBytesUsedInNvram.setMaxAccess(_C)
if mibBuilder.loadTexts:cigTftpServersTotalBytesUsedInNvram.setStatus(_A)
class _CigTftpServersTotalBytesCapacityInNvram_Type(Unsigned32):defaultValue=131072
_CigTftpServersTotalBytesCapacityInNvram_Type.__name__=_D
_CigTftpServersTotalBytesCapacityInNvram_Object=MibScalar
cigTftpServersTotalBytesCapacityInNvram=_CigTftpServersTotalBytesCapacityInNvram_Object((1,3,6,1,4,1,6889,2,1,16,1,2,2),_CigTftpServersTotalBytesCapacityInNvram_Type())
cigTftpServersTotalBytesCapacityInNvram.setMaxAccess(_C)
if mibBuilder.loadTexts:cigTftpServersTotalBytesCapacityInNvram.setStatus(_A)
class _CigTftpServersTotalBytesUsedInRam_Type(Unsigned32):defaultValue=0
_CigTftpServersTotalBytesUsedInRam_Type.__name__=_D
_CigTftpServersTotalBytesUsedInRam_Object=MibScalar
cigTftpServersTotalBytesUsedInRam=_CigTftpServersTotalBytesUsedInRam_Object((1,3,6,1,4,1,6889,2,1,16,1,2,3),_CigTftpServersTotalBytesUsedInRam_Type())
cigTftpServersTotalBytesUsedInRam.setMaxAccess(_C)
if mibBuilder.loadTexts:cigTftpServersTotalBytesUsedInRam.setStatus(_A)
class _CigTftpServersTotalBytesCapacityInRam_Type(Unsigned32):defaultValue=20971520
_CigTftpServersTotalBytesCapacityInRam_Type.__name__=_D
_CigTftpServersTotalBytesCapacityInRam_Object=MibScalar
cigTftpServersTotalBytesCapacityInRam=_CigTftpServersTotalBytesCapacityInRam_Object((1,3,6,1,4,1,6889,2,1,16,1,2,4),_CigTftpServersTotalBytesCapacityInRam_Type())
cigTftpServersTotalBytesCapacityInRam.setMaxAccess(_C)
if mibBuilder.loadTexts:cigTftpServersTotalBytesCapacityInRam.setStatus(_A)
_CigTftpServersGenStats_ObjectIdentity=ObjectIdentity
cigTftpServersGenStats=_CigTftpServersGenStats_ObjectIdentity((1,3,6,1,4,1,6889,2,1,16,1,3))
class _CigTftpServersSuccessfulDownloads_Type(Unsigned32):defaultValue=0
_CigTftpServersSuccessfulDownloads_Type.__name__=_D
_CigTftpServersSuccessfulDownloads_Object=MibScalar
cigTftpServersSuccessfulDownloads=_CigTftpServersSuccessfulDownloads_Object((1,3,6,1,4,1,6889,2,1,16,1,3,1),_CigTftpServersSuccessfulDownloads_Type())
cigTftpServersSuccessfulDownloads.setMaxAccess(_C)
if mibBuilder.loadTexts:cigTftpServersSuccessfulDownloads.setStatus(_A)
class _CigTftpServersNotDefinedErrors_Type(Unsigned32):defaultValue=0
_CigTftpServersNotDefinedErrors_Type.__name__=_D
_CigTftpServersNotDefinedErrors_Object=MibScalar
cigTftpServersNotDefinedErrors=_CigTftpServersNotDefinedErrors_Object((1,3,6,1,4,1,6889,2,1,16,1,3,2),_CigTftpServersNotDefinedErrors_Type())
cigTftpServersNotDefinedErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cigTftpServersNotDefinedErrors.setStatus(_A)
class _CigTftpServersFileNotFoundErrors_Type(Unsigned32):defaultValue=0
_CigTftpServersFileNotFoundErrors_Type.__name__=_D
_CigTftpServersFileNotFoundErrors_Object=MibScalar
cigTftpServersFileNotFoundErrors=_CigTftpServersFileNotFoundErrors_Object((1,3,6,1,4,1,6889,2,1,16,1,3,3),_CigTftpServersFileNotFoundErrors_Type())
cigTftpServersFileNotFoundErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cigTftpServersFileNotFoundErrors.setStatus(_A)
class _CigTftpServersAccessViolationErrors_Type(Unsigned32):defaultValue=0
_CigTftpServersAccessViolationErrors_Type.__name__=_D
_CigTftpServersAccessViolationErrors_Object=MibScalar
cigTftpServersAccessViolationErrors=_CigTftpServersAccessViolationErrors_Object((1,3,6,1,4,1,6889,2,1,16,1,3,4),_CigTftpServersAccessViolationErrors_Type())
cigTftpServersAccessViolationErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cigTftpServersAccessViolationErrors.setStatus(_A)
class _CigTftpServersDiskFullErrors_Type(Unsigned32):defaultValue=0
_CigTftpServersDiskFullErrors_Type.__name__=_D
_CigTftpServersDiskFullErrors_Object=MibScalar
cigTftpServersDiskFullErrors=_CigTftpServersDiskFullErrors_Object((1,3,6,1,4,1,6889,2,1,16,1,3,5),_CigTftpServersDiskFullErrors_Type())
cigTftpServersDiskFullErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cigTftpServersDiskFullErrors.setStatus(_A)
class _CigTftpServersIllegalTFTPOperationErrors_Type(Unsigned32):defaultValue=0
_CigTftpServersIllegalTFTPOperationErrors_Type.__name__=_D
_CigTftpServersIllegalTFTPOperationErrors_Object=MibScalar
cigTftpServersIllegalTFTPOperationErrors=_CigTftpServersIllegalTFTPOperationErrors_Object((1,3,6,1,4,1,6889,2,1,16,1,3,6),_CigTftpServersIllegalTFTPOperationErrors_Type())
cigTftpServersIllegalTFTPOperationErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cigTftpServersIllegalTFTPOperationErrors.setStatus(_A)
class _CigTftpServersUnknownTransferIdErrors_Type(Unsigned32):defaultValue=0
_CigTftpServersUnknownTransferIdErrors_Type.__name__=_D
_CigTftpServersUnknownTransferIdErrors_Object=MibScalar
cigTftpServersUnknownTransferIdErrors=_CigTftpServersUnknownTransferIdErrors_Object((1,3,6,1,4,1,6889,2,1,16,1,3,7),_CigTftpServersUnknownTransferIdErrors_Type())
cigTftpServersUnknownTransferIdErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cigTftpServersUnknownTransferIdErrors.setStatus(_A)
class _CigTftpServersFileAlreadyExistsErrors_Type(Unsigned32):defaultValue=0
_CigTftpServersFileAlreadyExistsErrors_Type.__name__=_D
_CigTftpServersFileAlreadyExistsErrors_Object=MibScalar
cigTftpServersFileAlreadyExistsErrors=_CigTftpServersFileAlreadyExistsErrors_Object((1,3,6,1,4,1,6889,2,1,16,1,3,8),_CigTftpServersFileAlreadyExistsErrors_Type())
cigTftpServersFileAlreadyExistsErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cigTftpServersFileAlreadyExistsErrors.setStatus(_A)
class _CigTftpServersNoSuchUserErrors_Type(Unsigned32):defaultValue=0
_CigTftpServersNoSuchUserErrors_Type.__name__=_D
_CigTftpServersNoSuchUserErrors_Object=MibScalar
cigTftpServersNoSuchUserErrors=_CigTftpServersNoSuchUserErrors_Object((1,3,6,1,4,1,6889,2,1,16,1,3,9),_CigTftpServersNoSuchUserErrors_Type())
cigTftpServersNoSuchUserErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cigTftpServersNoSuchUserErrors.setStatus(_A)
class _CigTftpServersDownloadTimeouts_Type(Unsigned32):defaultValue=0
_CigTftpServersDownloadTimeouts_Type.__name__=_D
_CigTftpServersDownloadTimeouts_Object=MibScalar
cigTftpServersDownloadTimeouts=_CigTftpServersDownloadTimeouts_Object((1,3,6,1,4,1,6889,2,1,16,1,3,10),_CigTftpServersDownloadTimeouts_Type())
cigTftpServersDownloadTimeouts.setMaxAccess(_C)
if mibBuilder.loadTexts:cigTftpServersDownloadTimeouts.setStatus(_A)
_CigTftpServersNotificationPacket_ObjectIdentity=ObjectIdentity
cigTftpServersNotificationPacket=_CigTftpServersNotificationPacket_ObjectIdentity((1,3,6,1,4,1,6889,2,1,16,1,4))
class _CigTftpServersNotificationClientIpAddr_Type(IpAddress):defaultHexValue=_K
_CigTftpServersNotificationClientIpAddr_Type.__name__=_G
_CigTftpServersNotificationClientIpAddr_Object=MibScalar
cigTftpServersNotificationClientIpAddr=_CigTftpServersNotificationClientIpAddr_Object((1,3,6,1,4,1,6889,2,1,16,1,4,1),_CigTftpServersNotificationClientIpAddr_Type())
cigTftpServersNotificationClientIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:cigTftpServersNotificationClientIpAddr.setStatus(_A)
class _CigTftpServersNotificationFilename_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_CigTftpServersNotificationFilename_Type.__name__=_F
_CigTftpServersNotificationFilename_Object=MibScalar
cigTftpServersNotificationFilename=_CigTftpServersNotificationFilename_Object((1,3,6,1,4,1,6889,2,1,16,1,4,2),_CigTftpServersNotificationFilename_Type())
cigTftpServersNotificationFilename.setMaxAccess(_H)
if mibBuilder.loadTexts:cigTftpServersNotificationFilename.setStatus(_A)
class _CigTftpServersNotificationErrorString_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_CigTftpServersNotificationErrorString_Type.__name__=_F
_CigTftpServersNotificationErrorString_Object=MibScalar
cigTftpServersNotificationErrorString=_CigTftpServersNotificationErrorString_Object((1,3,6,1,4,1,6889,2,1,16,1,4,3),_CigTftpServersNotificationErrorString_Type())
cigTftpServersNotificationErrorString.setMaxAccess(_H)
if mibBuilder.loadTexts:cigTftpServersNotificationErrorString.setStatus(_A)
_CigDhcpServers_ObjectIdentity=ObjectIdentity
cigDhcpServers=_CigDhcpServers_ObjectIdentity((1,3,6,1,4,1,6889,2,1,16,2))
_CigDhcpServersNotification_ObjectIdentity=ObjectIdentity
cigDhcpServersNotification=_CigDhcpServersNotification_ObjectIdentity((1,3,6,1,4,1,6889,2,1,16,2,0))
_CigDhcpServersGenConfig_ObjectIdentity=ObjectIdentity
cigDhcpServersGenConfig=_CigDhcpServersGenConfig_ObjectIdentity((1,3,6,1,4,1,6889,2,1,16,2,1))
class _CigDhcpServersMode_Type(TruthValue):defaultValue=2
_CigDhcpServersMode_Type.__name__=_L
_CigDhcpServersMode_Object=MibScalar
cigDhcpServersMode=_CigDhcpServersMode_Object((1,3,6,1,4,1,6889,2,1,16,2,1,1),_CigDhcpServersMode_Type())
cigDhcpServersMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersMode.setStatus(_A)
class _CigDhcpServersResetStatCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_CigDhcpServersResetStatCounters_Type.__name__=_J
_CigDhcpServersResetStatCounters_Object=MibScalar
cigDhcpServersResetStatCounters=_CigDhcpServersResetStatCounters_Object((1,3,6,1,4,1,6889,2,1,16,2,1,2),_CigDhcpServersResetStatCounters_Type())
cigDhcpServersResetStatCounters.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersResetStatCounters.setStatus(_A)
class _CigDhcpServersPingDetectionMode_Type(TruthValue):defaultValue=2
_CigDhcpServersPingDetectionMode_Type.__name__=_L
_CigDhcpServersPingDetectionMode_Object=MibScalar
cigDhcpServersPingDetectionMode=_CigDhcpServersPingDetectionMode_Object((1,3,6,1,4,1,6889,2,1,16,2,1,3),_CigDhcpServersPingDetectionMode_Type())
cigDhcpServersPingDetectionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersPingDetectionMode.setStatus(_A)
class _CigDhcpServersPingDetectionTimeout_Type(Unsigned32):defaultValue=500
_CigDhcpServersPingDetectionTimeout_Type.__name__=_D
_CigDhcpServersPingDetectionTimeout_Object=MibScalar
cigDhcpServersPingDetectionTimeout=_CigDhcpServersPingDetectionTimeout_Object((1,3,6,1,4,1,6889,2,1,16,2,1,4),_CigDhcpServersPingDetectionTimeout_Type())
cigDhcpServersPingDetectionTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersPingDetectionTimeout.setStatus(_A)
_CigDhcpServersPool_ObjectIdentity=ObjectIdentity
cigDhcpServersPool=_CigDhcpServersPool_ObjectIdentity((1,3,6,1,4,1,6889,2,1,16,2,2))
_CigDhcpServersPoolTable_Object=MibTable
cigDhcpServersPoolTable=_CigDhcpServersPoolTable_Object((1,3,6,1,4,1,6889,2,1,16,2,2,1))
if mibBuilder.loadTexts:cigDhcpServersPoolTable.setStatus(_A)
_CigDhcpServersPoolEntry_Object=MibTableRow
cigDhcpServersPoolEntry=_CigDhcpServersPoolEntry_Object((1,3,6,1,4,1,6889,2,1,16,2,2,1,1))
cigDhcpServersPoolEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:cigDhcpServersPoolEntry.setStatus(_A)
_CigDhcpServersPoolIndex_Type=Integer32
_CigDhcpServersPoolIndex_Object=MibTableColumn
cigDhcpServersPoolIndex=_CigDhcpServersPoolIndex_Object((1,3,6,1,4,1,6889,2,1,16,2,2,1,1,1),_CigDhcpServersPoolIndex_Type())
cigDhcpServersPoolIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpServersPoolIndex.setStatus(_A)
class _CigDhcpServersPoolStartIPAddr_Type(IpAddress):defaultHexValue=_K
_CigDhcpServersPoolStartIPAddr_Type.__name__=_G
_CigDhcpServersPoolStartIPAddr_Object=MibTableColumn
cigDhcpServersPoolStartIPAddr=_CigDhcpServersPoolStartIPAddr_Object((1,3,6,1,4,1,6889,2,1,16,2,2,1,1,2),_CigDhcpServersPoolStartIPAddr_Type())
cigDhcpServersPoolStartIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersPoolStartIPAddr.setStatus(_A)
class _CigDhcpServersPoolEndIPAddr_Type(IpAddress):defaultHexValue=_K
_CigDhcpServersPoolEndIPAddr_Type.__name__=_G
_CigDhcpServersPoolEndIPAddr_Object=MibTableColumn
cigDhcpServersPoolEndIPAddr=_CigDhcpServersPoolEndIPAddr_Object((1,3,6,1,4,1,6889,2,1,16,2,2,1,1,3),_CigDhcpServersPoolEndIPAddr_Type())
cigDhcpServersPoolEndIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersPoolEndIPAddr.setStatus(_A)
class _CigDhcpServersPoolMode_Type(TruthValue):defaultValue=2
_CigDhcpServersPoolMode_Type.__name__=_L
_CigDhcpServersPoolMode_Object=MibTableColumn
cigDhcpServersPoolMode=_CigDhcpServersPoolMode_Object((1,3,6,1,4,1,6889,2,1,16,2,2,1,1,4),_CigDhcpServersPoolMode_Type())
cigDhcpServersPoolMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersPoolMode.setStatus(_A)
class _CigDhcpServersPoolName_Type(DisplayString):defaultValue=OctetString('Dhcp Pool #');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CigDhcpServersPoolName_Type.__name__=_F
_CigDhcpServersPoolName_Object=MibTableColumn
cigDhcpServersPoolName=_CigDhcpServersPoolName_Object((1,3,6,1,4,1,6889,2,1,16,2,2,1,1,5),_CigDhcpServersPoolName_Type())
cigDhcpServersPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersPoolName.setStatus(_A)
class _CigDhcpServersPoolClientID_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CigDhcpServersPoolClientID_Type.__name__=_I
_CigDhcpServersPoolClientID_Object=MibTableColumn
cigDhcpServersPoolClientID=_CigDhcpServersPoolClientID_Object((1,3,6,1,4,1,6889,2,1,16,2,2,1,1,6),_CigDhcpServersPoolClientID_Type())
cigDhcpServersPoolClientID.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersPoolClientID.setStatus(_A)
class _CigDhcpServersPoolLeaseTime_Type(Unsigned32):defaultValue=691200
_CigDhcpServersPoolLeaseTime_Type.__name__=_D
_CigDhcpServersPoolLeaseTime_Object=MibTableColumn
cigDhcpServersPoolLeaseTime=_CigDhcpServersPoolLeaseTime_Object((1,3,6,1,4,1,6889,2,1,16,2,2,1,1,7),_CigDhcpServersPoolLeaseTime_Type())
cigDhcpServersPoolLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersPoolLeaseTime.setStatus(_A)
class _CigDhcpServersPoolBootFile_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CigDhcpServersPoolBootFile_Type.__name__=_F
_CigDhcpServersPoolBootFile_Object=MibTableColumn
cigDhcpServersPoolBootFile=_CigDhcpServersPoolBootFile_Object((1,3,6,1,4,1,6889,2,1,16,2,2,1,1,8),_CigDhcpServersPoolBootFile_Type())
cigDhcpServersPoolBootFile.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersPoolBootFile.setStatus(_A)
class _CigDhcpServersPoolNextServer_Type(IpAddress):defaultHexValue=_K
_CigDhcpServersPoolNextServer_Type.__name__=_G
_CigDhcpServersPoolNextServer_Object=MibTableColumn
cigDhcpServersPoolNextServer=_CigDhcpServersPoolNextServer_Object((1,3,6,1,4,1,6889,2,1,16,2,2,1,1,9),_CigDhcpServersPoolNextServer_Type())
cigDhcpServersPoolNextServer.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersPoolNextServer.setStatus(_A)
class _CigDhcpServersPoolSubnetMask_Type(IpAddress):defaultHexValue='ffffff00'
_CigDhcpServersPoolSubnetMask_Type.__name__=_G
_CigDhcpServersPoolSubnetMask_Object=MibTableColumn
cigDhcpServersPoolSubnetMask=_CigDhcpServersPoolSubnetMask_Object((1,3,6,1,4,1,6889,2,1,16,2,2,1,1,10),_CigDhcpServersPoolSubnetMask_Type())
cigDhcpServersPoolSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersPoolSubnetMask.setStatus(_A)
class _CigDhcpServersPoolDefaultGateway_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,145))
_CigDhcpServersPoolDefaultGateway_Type.__name__=_F
_CigDhcpServersPoolDefaultGateway_Object=MibTableColumn
cigDhcpServersPoolDefaultGateway=_CigDhcpServersPoolDefaultGateway_Object((1,3,6,1,4,1,6889,2,1,16,2,2,1,1,11),_CigDhcpServersPoolDefaultGateway_Type())
cigDhcpServersPoolDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersPoolDefaultGateway.setStatus(_A)
class _CigDhcpServersPoolDnsServer_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,145))
_CigDhcpServersPoolDnsServer_Type.__name__=_F
_CigDhcpServersPoolDnsServer_Object=MibTableColumn
cigDhcpServersPoolDnsServer=_CigDhcpServersPoolDnsServer_Object((1,3,6,1,4,1,6889,2,1,16,2,2,1,1,12),_CigDhcpServersPoolDnsServer_Type())
cigDhcpServersPoolDnsServer.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersPoolDnsServer.setStatus(_A)
class _CigDhcpServersPoolDomainName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CigDhcpServersPoolDomainName_Type.__name__=_F
_CigDhcpServersPoolDomainName_Object=MibTableColumn
cigDhcpServersPoolDomainName=_CigDhcpServersPoolDomainName_Object((1,3,6,1,4,1,6889,2,1,16,2,2,1,1,13),_CigDhcpServersPoolDomainName_Type())
cigDhcpServersPoolDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersPoolDomainName.setStatus(_A)
class _CigDhcpServersPoolServerName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CigDhcpServersPoolServerName_Type.__name__=_F
_CigDhcpServersPoolServerName_Object=MibTableColumn
cigDhcpServersPoolServerName=_CigDhcpServersPoolServerName_Object((1,3,6,1,4,1,6889,2,1,16,2,2,1,1,14),_CigDhcpServersPoolServerName_Type())
cigDhcpServersPoolServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersPoolServerName.setStatus(_A)
_CigDhcpServersPoolRowStatus_Type=RowStatus
_CigDhcpServersPoolRowStatus_Object=MibTableColumn
cigDhcpServersPoolRowStatus=_CigDhcpServersPoolRowStatus_Object((1,3,6,1,4,1,6889,2,1,16,2,2,1,1,15),_CigDhcpServersPoolRowStatus_Type())
cigDhcpServersPoolRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersPoolRowStatus.setStatus(_A)
_CigDhcpServersPoolGenOptionTable_Object=MibTable
cigDhcpServersPoolGenOptionTable=_CigDhcpServersPoolGenOptionTable_Object((1,3,6,1,4,1,6889,2,1,16,2,2,2))
if mibBuilder.loadTexts:cigDhcpServersPoolGenOptionTable.setStatus(_A)
_CigDhcpServersPoolGenOptionEntry_Object=MibTableRow
cigDhcpServersPoolGenOptionEntry=_CigDhcpServersPoolGenOptionEntry_Object((1,3,6,1,4,1,6889,2,1,16,2,2,2,1))
cigDhcpServersPoolGenOptionEntry.setIndexNames((0,_E,_S),(0,_E,_T))
if mibBuilder.loadTexts:cigDhcpServersPoolGenOptionEntry.setStatus(_A)
_CigDhcpServersOptionPoolIndex_Type=Integer32
_CigDhcpServersOptionPoolIndex_Object=MibTableColumn
cigDhcpServersOptionPoolIndex=_CigDhcpServersOptionPoolIndex_Object((1,3,6,1,4,1,6889,2,1,16,2,2,2,1,1),_CigDhcpServersOptionPoolIndex_Type())
cigDhcpServersOptionPoolIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpServersOptionPoolIndex.setStatus(_A)
_CigDhcpServersOptionIndex_Type=Integer32
_CigDhcpServersOptionIndex_Object=MibTableColumn
cigDhcpServersOptionIndex=_CigDhcpServersOptionIndex_Object((1,3,6,1,4,1,6889,2,1,16,2,2,2,1,2),_CigDhcpServersOptionIndex_Type())
cigDhcpServersOptionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpServersOptionIndex.setStatus(_A)
class _CigDhcpServersOptionName_Type(DisplayString):defaultValue=OctetString('Option #');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_CigDhcpServersOptionName_Type.__name__=_F
_CigDhcpServersOptionName_Object=MibTableColumn
cigDhcpServersOptionName=_CigDhcpServersOptionName_Object((1,3,6,1,4,1,6889,2,1,16,2,2,2,1,3),_CigDhcpServersOptionName_Type())
cigDhcpServersOptionName.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersOptionName.setStatus(_A)
class _CigDhcpServersOptionType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ascii',1),('hex',2),('ipAddresses',3),('integer',4),('word',5)))
_CigDhcpServersOptionType_Type.__name__=_J
_CigDhcpServersOptionType_Object=MibTableColumn
cigDhcpServersOptionType=_CigDhcpServersOptionType_Object((1,3,6,1,4,1,6889,2,1,16,2,2,2,1,4),_CigDhcpServersOptionType_Type())
cigDhcpServersOptionType.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersOptionType.setStatus(_A)
class _CigDhcpServersOptionValue_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CigDhcpServersOptionValue_Type.__name__=_I
_CigDhcpServersOptionValue_Object=MibTableColumn
cigDhcpServersOptionValue=_CigDhcpServersOptionValue_Object((1,3,6,1,4,1,6889,2,1,16,2,2,2,1,5),_CigDhcpServersOptionValue_Type())
cigDhcpServersOptionValue.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersOptionValue.setStatus(_A)
_CigDhcpServersOptionRowStatus_Type=RowStatus
_CigDhcpServersOptionRowStatus_Object=MibTableColumn
cigDhcpServersOptionRowStatus=_CigDhcpServersOptionRowStatus_Object((1,3,6,1,4,1,6889,2,1,16,2,2,2,1,6),_CigDhcpServersOptionRowStatus_Type())
cigDhcpServersOptionRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersOptionRowStatus.setStatus(_A)
_CigDhcpServersPoolVendorSpecificOptionTable_Object=MibTable
cigDhcpServersPoolVendorSpecificOptionTable=_CigDhcpServersPoolVendorSpecificOptionTable_Object((1,3,6,1,4,1,6889,2,1,16,2,2,3))
if mibBuilder.loadTexts:cigDhcpServersPoolVendorSpecificOptionTable.setStatus(_A)
_CigDhcpServersPoolVendorSpecificOptionEntry_Object=MibTableRow
cigDhcpServersPoolVendorSpecificOptionEntry=_CigDhcpServersPoolVendorSpecificOptionEntry_Object((1,3,6,1,4,1,6889,2,1,16,2,2,3,1))
cigDhcpServersPoolVendorSpecificOptionEntry.setIndexNames((0,_E,_U),(0,_E,_V))
if mibBuilder.loadTexts:cigDhcpServersPoolVendorSpecificOptionEntry.setStatus(_A)
_CigDhcpServersVendorSpecificOptionPoolIndex_Type=Integer32
_CigDhcpServersVendorSpecificOptionPoolIndex_Object=MibTableColumn
cigDhcpServersVendorSpecificOptionPoolIndex=_CigDhcpServersVendorSpecificOptionPoolIndex_Object((1,3,6,1,4,1,6889,2,1,16,2,2,3,1,1),_CigDhcpServersVendorSpecificOptionPoolIndex_Type())
cigDhcpServersVendorSpecificOptionPoolIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpServersVendorSpecificOptionPoolIndex.setStatus(_A)
_CigDhcpServersVendorSpecificOptionIndex_Type=Integer32
_CigDhcpServersVendorSpecificOptionIndex_Object=MibTableColumn
cigDhcpServersVendorSpecificOptionIndex=_CigDhcpServersVendorSpecificOptionIndex_Object((1,3,6,1,4,1,6889,2,1,16,2,2,3,1,2),_CigDhcpServersVendorSpecificOptionIndex_Type())
cigDhcpServersVendorSpecificOptionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpServersVendorSpecificOptionIndex.setStatus(_A)
class _CigDhcpServersVendorSpecificOptionName_Type(DisplayString):defaultValue=OctetString('Vendor Specific Option #');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_CigDhcpServersVendorSpecificOptionName_Type.__name__=_F
_CigDhcpServersVendorSpecificOptionName_Object=MibTableColumn
cigDhcpServersVendorSpecificOptionName=_CigDhcpServersVendorSpecificOptionName_Object((1,3,6,1,4,1,6889,2,1,16,2,2,3,1,3),_CigDhcpServersVendorSpecificOptionName_Type())
cigDhcpServersVendorSpecificOptionName.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersVendorSpecificOptionName.setStatus(_A)
class _CigDhcpServersVendorSpecificClassIdentifier_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CigDhcpServersVendorSpecificClassIdentifier_Type.__name__=_F
_CigDhcpServersVendorSpecificClassIdentifier_Object=MibTableColumn
cigDhcpServersVendorSpecificClassIdentifier=_CigDhcpServersVendorSpecificClassIdentifier_Object((1,3,6,1,4,1,6889,2,1,16,2,2,3,1,4),_CigDhcpServersVendorSpecificClassIdentifier_Type())
cigDhcpServersVendorSpecificClassIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersVendorSpecificClassIdentifier.setStatus(_A)
class _CigDhcpServersVendorSpecificOptionType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ascii',1),('hex',2)))
_CigDhcpServersVendorSpecificOptionType_Type.__name__=_J
_CigDhcpServersVendorSpecificOptionType_Object=MibTableColumn
cigDhcpServersVendorSpecificOptionType=_CigDhcpServersVendorSpecificOptionType_Object((1,3,6,1,4,1,6889,2,1,16,2,2,3,1,5),_CigDhcpServersVendorSpecificOptionType_Type())
cigDhcpServersVendorSpecificOptionType.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersVendorSpecificOptionType.setStatus(_A)
class _CigDhcpServersVendorSpecificOptionValue_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CigDhcpServersVendorSpecificOptionValue_Type.__name__=_I
_CigDhcpServersVendorSpecificOptionValue_Object=MibTableColumn
cigDhcpServersVendorSpecificOptionValue=_CigDhcpServersVendorSpecificOptionValue_Object((1,3,6,1,4,1,6889,2,1,16,2,2,3,1,6),_CigDhcpServersVendorSpecificOptionValue_Type())
cigDhcpServersVendorSpecificOptionValue.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersVendorSpecificOptionValue.setStatus(_A)
_CigDhcpServersVendorSpecificOptionRowStatus_Type=RowStatus
_CigDhcpServersVendorSpecificOptionRowStatus_Object=MibTableColumn
cigDhcpServersVendorSpecificOptionRowStatus=_CigDhcpServersVendorSpecificOptionRowStatus_Object((1,3,6,1,4,1,6889,2,1,16,2,2,3,1,7),_CigDhcpServersVendorSpecificOptionRowStatus_Type())
cigDhcpServersVendorSpecificOptionRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpServersVendorSpecificOptionRowStatus.setStatus(_A)
_CigDhcpServersGenStats_ObjectIdentity=ObjectIdentity
cigDhcpServersGenStats=_CigDhcpServersGenStats_ObjectIdentity((1,3,6,1,4,1,6889,2,1,16,2,3))
class _CigDhcpServersBootRequests_Type(Unsigned32):defaultValue=0
_CigDhcpServersBootRequests_Type.__name__=_D
_CigDhcpServersBootRequests_Object=MibScalar
cigDhcpServersBootRequests=_CigDhcpServersBootRequests_Object((1,3,6,1,4,1,6889,2,1,16,2,3,1),_CigDhcpServersBootRequests_Type())
cigDhcpServersBootRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpServersBootRequests.setStatus(_A)
class _CigDhcpServersDhcpDiscovers_Type(Unsigned32):defaultValue=0
_CigDhcpServersDhcpDiscovers_Type.__name__=_D
_CigDhcpServersDhcpDiscovers_Object=MibScalar
cigDhcpServersDhcpDiscovers=_CigDhcpServersDhcpDiscovers_Object((1,3,6,1,4,1,6889,2,1,16,2,3,2),_CigDhcpServersDhcpDiscovers_Type())
cigDhcpServersDhcpDiscovers.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpServersDhcpDiscovers.setStatus(_A)
class _CigDhcpServersDhcpRequests_Type(Unsigned32):defaultValue=0
_CigDhcpServersDhcpRequests_Type.__name__=_D
_CigDhcpServersDhcpRequests_Object=MibScalar
cigDhcpServersDhcpRequests=_CigDhcpServersDhcpRequests_Object((1,3,6,1,4,1,6889,2,1,16,2,3,3),_CigDhcpServersDhcpRequests_Type())
cigDhcpServersDhcpRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpServersDhcpRequests.setStatus(_A)
class _CigDhcpServersDhcpDeclines_Type(Unsigned32):defaultValue=0
_CigDhcpServersDhcpDeclines_Type.__name__=_D
_CigDhcpServersDhcpDeclines_Object=MibScalar
cigDhcpServersDhcpDeclines=_CigDhcpServersDhcpDeclines_Object((1,3,6,1,4,1,6889,2,1,16,2,3,4),_CigDhcpServersDhcpDeclines_Type())
cigDhcpServersDhcpDeclines.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpServersDhcpDeclines.setStatus(_A)
class _CigDhcpServersDhcpReleases_Type(Unsigned32):defaultValue=0
_CigDhcpServersDhcpReleases_Type.__name__=_D
_CigDhcpServersDhcpReleases_Object=MibScalar
cigDhcpServersDhcpReleases=_CigDhcpServersDhcpReleases_Object((1,3,6,1,4,1,6889,2,1,16,2,3,5),_CigDhcpServersDhcpReleases_Type())
cigDhcpServersDhcpReleases.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpServersDhcpReleases.setStatus(_A)
class _CigDhcpServersDhcpInforms_Type(Unsigned32):defaultValue=0
_CigDhcpServersDhcpInforms_Type.__name__=_D
_CigDhcpServersDhcpInforms_Object=MibScalar
cigDhcpServersDhcpInforms=_CigDhcpServersDhcpInforms_Object((1,3,6,1,4,1,6889,2,1,16,2,3,6),_CigDhcpServersDhcpInforms_Type())
cigDhcpServersDhcpInforms.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpServersDhcpInforms.setStatus(_A)
class _CigDhcpServersBootReplies_Type(Unsigned32):defaultValue=0
_CigDhcpServersBootReplies_Type.__name__=_D
_CigDhcpServersBootReplies_Object=MibScalar
cigDhcpServersBootReplies=_CigDhcpServersBootReplies_Object((1,3,6,1,4,1,6889,2,1,16,2,3,7),_CigDhcpServersBootReplies_Type())
cigDhcpServersBootReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpServersBootReplies.setStatus(_A)
class _CigDhcpServersDhcpOffers_Type(Unsigned32):defaultValue=0
_CigDhcpServersDhcpOffers_Type.__name__=_D
_CigDhcpServersDhcpOffers_Object=MibScalar
cigDhcpServersDhcpOffers=_CigDhcpServersDhcpOffers_Object((1,3,6,1,4,1,6889,2,1,16,2,3,8),_CigDhcpServersDhcpOffers_Type())
cigDhcpServersDhcpOffers.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpServersDhcpOffers.setStatus(_A)
class _CigDhcpServersDhcpAcks_Type(Unsigned32):defaultValue=0
_CigDhcpServersDhcpAcks_Type.__name__=_D
_CigDhcpServersDhcpAcks_Object=MibScalar
cigDhcpServersDhcpAcks=_CigDhcpServersDhcpAcks_Object((1,3,6,1,4,1,6889,2,1,16,2,3,9),_CigDhcpServersDhcpAcks_Type())
cigDhcpServersDhcpAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpServersDhcpAcks.setStatus(_A)
class _CigDhcpServersDhcpNacks_Type(Unsigned32):defaultValue=0
_CigDhcpServersDhcpNacks_Type.__name__=_D
_CigDhcpServersDhcpNacks_Object=MibScalar
cigDhcpServersDhcpNacks=_CigDhcpServersDhcpNacks_Object((1,3,6,1,4,1,6889,2,1,16,2,3,10),_CigDhcpServersDhcpNacks_Type())
cigDhcpServersDhcpNacks.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpServersDhcpNacks.setStatus(_A)
_CigDhcpServersNotificationPacket_ObjectIdentity=ObjectIdentity
cigDhcpServersNotificationPacket=_CigDhcpServersNotificationPacket_ObjectIdentity((1,3,6,1,4,1,6889,2,1,16,2,4))
class _CigDhcpServersNotificationIpAddr_Type(IpAddress):defaultHexValue=_K
_CigDhcpServersNotificationIpAddr_Type.__name__=_G
_CigDhcpServersNotificationIpAddr_Object=MibScalar
cigDhcpServersNotificationIpAddr=_CigDhcpServersNotificationIpAddr_Object((1,3,6,1,4,1,6889,2,1,16,2,4,1),_CigDhcpServersNotificationIpAddr_Type())
cigDhcpServersNotificationIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:cigDhcpServersNotificationIpAddr.setStatus(_A)
class _CigDhcpServersNotificationClientIdentifier_Type(OctetString):defaultHexValue='01000000000000';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CigDhcpServersNotificationClientIdentifier_Type.__name__=_I
_CigDhcpServersNotificationClientIdentifier_Object=MibScalar
cigDhcpServersNotificationClientIdentifier=_CigDhcpServersNotificationClientIdentifier_Object((1,3,6,1,4,1,6889,2,1,16,2,4,2),_CigDhcpServersNotificationClientIdentifier_Type())
cigDhcpServersNotificationClientIdentifier.setMaxAccess(_H)
if mibBuilder.loadTexts:cigDhcpServersNotificationClientIdentifier.setStatus(_A)
class _CigDhcpServersNotificationClientHostName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CigDhcpServersNotificationClientHostName_Type.__name__=_I
_CigDhcpServersNotificationClientHostName_Object=MibScalar
cigDhcpServersNotificationClientHostName=_CigDhcpServersNotificationClientHostName_Object((1,3,6,1,4,1,6889,2,1,16,2,4,3),_CigDhcpServersNotificationClientHostName_Type())
cigDhcpServersNotificationClientHostName.setMaxAccess(_H)
if mibBuilder.loadTexts:cigDhcpServersNotificationClientHostName.setStatus(_A)
class _CigDhcpServersNotificationConflictDetectionMethod_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('ping',1),('gratuitousArp',2),('notSupported',255)))
_CigDhcpServersNotificationConflictDetectionMethod_Type.__name__=_J
_CigDhcpServersNotificationConflictDetectionMethod_Object=MibScalar
cigDhcpServersNotificationConflictDetectionMethod=_CigDhcpServersNotificationConflictDetectionMethod_Object((1,3,6,1,4,1,6889,2,1,16,2,4,4),_CigDhcpServersNotificationConflictDetectionMethod_Type())
cigDhcpServersNotificationConflictDetectionMethod.setMaxAccess(_H)
if mibBuilder.loadTexts:cigDhcpServersNotificationConflictDetectionMethod.setStatus(_A)
class _CigDhcpServersNotificationPoolNetwork_Type(IpAddress):defaultHexValue=_K
_CigDhcpServersNotificationPoolNetwork_Type.__name__=_G
_CigDhcpServersNotificationPoolNetwork_Object=MibScalar
cigDhcpServersNotificationPoolNetwork=_CigDhcpServersNotificationPoolNetwork_Object((1,3,6,1,4,1,6889,2,1,16,2,4,5),_CigDhcpServersNotificationPoolNetwork_Type())
cigDhcpServersNotificationPoolNetwork.setMaxAccess(_H)
if mibBuilder.loadTexts:cigDhcpServersNotificationPoolNetwork.setStatus(_A)
cigTftpServersDownloadFailureTrap=NotificationType((1,3,6,1,4,1,6889,2,1,16,1,0,1))
cigTftpServersDownloadFailureTrap.setObjects(*((_E,_N),(_E,_O),(_E,_P)))
if mibBuilder.loadTexts:cigTftpServersDownloadFailureTrap.setStatus(_A)
cigTftpServersUploadFailureTrap=NotificationType((1,3,6,1,4,1,6889,2,1,16,1,0,2))
cigTftpServersUploadFailureTrap.setObjects(*((_E,_N),(_E,_O),(_E,_P)))
if mibBuilder.loadTexts:cigTftpServersUploadFailureTrap.setStatus(_A)
cigDhcpServersClientConflictDetectionTrap=NotificationType((1,3,6,1,4,1,6889,2,1,16,2,0,1))
cigDhcpServersClientConflictDetectionTrap.setObjects(*((_E,_Q),(_E,_W),(_E,_M),(_E,_X)))
if mibBuilder.loadTexts:cigDhcpServersClientConflictDetectionTrap.setStatus(_A)
cigDhcpServersServerNacksTrap=NotificationType((1,3,6,1,4,1,6889,2,1,16,2,0,2))
cigDhcpServersServerNacksTrap.setObjects(*((_E,_Q),(_E,_M)))
if mibBuilder.loadTexts:cigDhcpServersServerNacksTrap.setStatus(_A)
cigDhcpServersNoIpAddressLeft=NotificationType((1,3,6,1,4,1,6889,2,1,16,2,0,3))
cigDhcpServersNoIpAddressLeft.setObjects(*((_E,_M),(_E,_Y)))
if mibBuilder.loadTexts:cigDhcpServersNoIpAddressLeft.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'avaya':avaya,'mibs':mibs,'lsg':lsg,'cigServers':cigServers,'cigTftpServers':cigTftpServers,'cigTftpServersNotification':cigTftpServersNotification,'cigTftpServersDownloadFailureTrap':cigTftpServersDownloadFailureTrap,'cigTftpServersUploadFailureTrap':cigTftpServersUploadFailureTrap,'cigTftpServersGenConfig':cigTftpServersGenConfig,'cigTftpServersMode':cigTftpServersMode,'cigTftpServersResetStatCounters':cigTftpServersResetStatCounters,'cigTftpServersMemoryAllocation':cigTftpServersMemoryAllocation,'cigTftpServersTotalBytesUsedInNvram':cigTftpServersTotalBytesUsedInNvram,'cigTftpServersTotalBytesCapacityInNvram':cigTftpServersTotalBytesCapacityInNvram,'cigTftpServersTotalBytesUsedInRam':cigTftpServersTotalBytesUsedInRam,'cigTftpServersTotalBytesCapacityInRam':cigTftpServersTotalBytesCapacityInRam,'cigTftpServersGenStats':cigTftpServersGenStats,'cigTftpServersSuccessfulDownloads':cigTftpServersSuccessfulDownloads,'cigTftpServersNotDefinedErrors':cigTftpServersNotDefinedErrors,'cigTftpServersFileNotFoundErrors':cigTftpServersFileNotFoundErrors,'cigTftpServersAccessViolationErrors':cigTftpServersAccessViolationErrors,'cigTftpServersDiskFullErrors':cigTftpServersDiskFullErrors,'cigTftpServersIllegalTFTPOperationErrors':cigTftpServersIllegalTFTPOperationErrors,'cigTftpServersUnknownTransferIdErrors':cigTftpServersUnknownTransferIdErrors,'cigTftpServersFileAlreadyExistsErrors':cigTftpServersFileAlreadyExistsErrors,'cigTftpServersNoSuchUserErrors':cigTftpServersNoSuchUserErrors,'cigTftpServersDownloadTimeouts':cigTftpServersDownloadTimeouts,'cigTftpServersNotificationPacket':cigTftpServersNotificationPacket,_N:cigTftpServersNotificationClientIpAddr,_O:cigTftpServersNotificationFilename,_P:cigTftpServersNotificationErrorString,'cigDhcpServers':cigDhcpServers,'cigDhcpServersNotification':cigDhcpServersNotification,'cigDhcpServersClientConflictDetectionTrap':cigDhcpServersClientConflictDetectionTrap,'cigDhcpServersServerNacksTrap':cigDhcpServersServerNacksTrap,'cigDhcpServersNoIpAddressLeft':cigDhcpServersNoIpAddressLeft,'cigDhcpServersGenConfig':cigDhcpServersGenConfig,'cigDhcpServersMode':cigDhcpServersMode,'cigDhcpServersResetStatCounters':cigDhcpServersResetStatCounters,'cigDhcpServersPingDetectionMode':cigDhcpServersPingDetectionMode,'cigDhcpServersPingDetectionTimeout':cigDhcpServersPingDetectionTimeout,'cigDhcpServersPool':cigDhcpServersPool,'cigDhcpServersPoolTable':cigDhcpServersPoolTable,'cigDhcpServersPoolEntry':cigDhcpServersPoolEntry,_R:cigDhcpServersPoolIndex,'cigDhcpServersPoolStartIPAddr':cigDhcpServersPoolStartIPAddr,'cigDhcpServersPoolEndIPAddr':cigDhcpServersPoolEndIPAddr,'cigDhcpServersPoolMode':cigDhcpServersPoolMode,'cigDhcpServersPoolName':cigDhcpServersPoolName,'cigDhcpServersPoolClientID':cigDhcpServersPoolClientID,'cigDhcpServersPoolLeaseTime':cigDhcpServersPoolLeaseTime,'cigDhcpServersPoolBootFile':cigDhcpServersPoolBootFile,'cigDhcpServersPoolNextServer':cigDhcpServersPoolNextServer,'cigDhcpServersPoolSubnetMask':cigDhcpServersPoolSubnetMask,'cigDhcpServersPoolDefaultGateway':cigDhcpServersPoolDefaultGateway,'cigDhcpServersPoolDnsServer':cigDhcpServersPoolDnsServer,'cigDhcpServersPoolDomainName':cigDhcpServersPoolDomainName,'cigDhcpServersPoolServerName':cigDhcpServersPoolServerName,'cigDhcpServersPoolRowStatus':cigDhcpServersPoolRowStatus,'cigDhcpServersPoolGenOptionTable':cigDhcpServersPoolGenOptionTable,'cigDhcpServersPoolGenOptionEntry':cigDhcpServersPoolGenOptionEntry,_S:cigDhcpServersOptionPoolIndex,_T:cigDhcpServersOptionIndex,'cigDhcpServersOptionName':cigDhcpServersOptionName,'cigDhcpServersOptionType':cigDhcpServersOptionType,'cigDhcpServersOptionValue':cigDhcpServersOptionValue,'cigDhcpServersOptionRowStatus':cigDhcpServersOptionRowStatus,'cigDhcpServersPoolVendorSpecificOptionTable':cigDhcpServersPoolVendorSpecificOptionTable,'cigDhcpServersPoolVendorSpecificOptionEntry':cigDhcpServersPoolVendorSpecificOptionEntry,_U:cigDhcpServersVendorSpecificOptionPoolIndex,_V:cigDhcpServersVendorSpecificOptionIndex,'cigDhcpServersVendorSpecificOptionName':cigDhcpServersVendorSpecificOptionName,'cigDhcpServersVendorSpecificClassIdentifier':cigDhcpServersVendorSpecificClassIdentifier,'cigDhcpServersVendorSpecificOptionType':cigDhcpServersVendorSpecificOptionType,'cigDhcpServersVendorSpecificOptionValue':cigDhcpServersVendorSpecificOptionValue,'cigDhcpServersVendorSpecificOptionRowStatus':cigDhcpServersVendorSpecificOptionRowStatus,'cigDhcpServersGenStats':cigDhcpServersGenStats,'cigDhcpServersBootRequests':cigDhcpServersBootRequests,'cigDhcpServersDhcpDiscovers':cigDhcpServersDhcpDiscovers,'cigDhcpServersDhcpRequests':cigDhcpServersDhcpRequests,'cigDhcpServersDhcpDeclines':cigDhcpServersDhcpDeclines,'cigDhcpServersDhcpReleases':cigDhcpServersDhcpReleases,'cigDhcpServersDhcpInforms':cigDhcpServersDhcpInforms,'cigDhcpServersBootReplies':cigDhcpServersBootReplies,'cigDhcpServersDhcpOffers':cigDhcpServersDhcpOffers,'cigDhcpServersDhcpAcks':cigDhcpServersDhcpAcks,'cigDhcpServersDhcpNacks':cigDhcpServersDhcpNacks,'cigDhcpServersNotificationPacket':cigDhcpServersNotificationPacket,_Q:cigDhcpServersNotificationIpAddr,_M:cigDhcpServersNotificationClientIdentifier,_W:cigDhcpServersNotificationClientHostName,_X:cigDhcpServersNotificationConflictDetectionMethod,_Y:cigDhcpServersNotificationPoolNetwork})