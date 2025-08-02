_w='imageAutomaticUpdateGroupVer1'
_v='imageTransferGroupVer1'
_u='imageBasicNotificationGroupVer1'
_t='imageBasicNotificationParamsGroupVer1'
_s='imageBasicNotificationControlGroupVer1'
_r='imageBasicGroupVer1'
_q='imageCompletion'
_p='imageAutoUpdateTimeRange'
_o='imageAutoUpdateTimeOfDay'
_n='imageAutoUpdatePeriod'
_m='imageAutoUpdateTimeUnit'
_l='imageAutoUpdatePeriodicEnable'
_k='imageAutoUpdateOnRestartEnable'
_j='imageTransferPassword'
_i='imageTransferUsername'
_h='imageTransferProtocol'
_g='imageCompletionControl'
_f='imageDhcpSecondarySiteSpecificCode'
_e='imageDhcpPrimarySiteSpecificCode'
_d='imageStaticSecondaryPort'
_c='imageStaticSecondaryHost'
_b='imageStaticPrimaryPort'
_a='imageStaticPrimaryHost'
_Z='imageSelectConfigSource'
_Y='imageSecondaryPort'
_X='imageSecondaryHost'
_W='imagePrimaryPort'
_V='imagePrimaryHost'
_U='imageConfigSource'
_T='imageLocation'
_S='accessible-for-notify'
_R='Unsigned32'
_Q='MxIpSelectConfigSource'
_P='MxIpConfigSource'
_O='sysAdminLastDownloadSoftware'
_N='MX-SYSTEM-ADMIN-MIB'
_M='imageServerAddress'
_L='imageLocationUsed'
_K='MxIpDhcpSiteSpecificCode'
_J='MxEnableState'
_I='192.168.0.10'
_H='MxIpPort'
_G='MxIpHostName'
_F='read-only'
_E='Integer32'
_D='OctetString'
_C='read-write'
_B='MX-IMAGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ipAddressConfig,ipAddressStatus,mediatrixConfig,mediatrixMgmt=mibBuilder.importSymbols('MX-SMI','ipAddressConfig','ipAddressStatus','mediatrixConfig','mediatrixMgmt')
sysAdminLastDownloadSoftware,=mibBuilder.importSymbols(_N,_O)
MxEnableState,MxIpConfigSource,MxIpDhcpSiteSpecificCode,MxIpHostName,MxIpPort,MxIpSelectConfigSource=mibBuilder.importSymbols('MX-TC',_J,_P,_K,_G,_H,_Q)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_R,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
imageMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,6))
if mibBuilder.loadTexts:imageMIB.setRevisions(('2010-12-15 00:00','2006-03-06 00:00','2005-04-25 00:00','2004-03-27 00:00','2004-02-10 00:00','2001-09-06 00:00'))
_IpAddressStatusImage_ObjectIdentity=ObjectIdentity
ipAddressStatusImage=_IpAddressStatusImage_ObjectIdentity((1,3,6,1,4,1,4935,10,1,8))
class _ImageConfigSource_Type(MxIpConfigSource):defaultValue=1
_ImageConfigSource_Type.__name__=_P
_ImageConfigSource_Object=MibScalar
imageConfigSource=_ImageConfigSource_Object((1,3,6,1,4,1,4935,10,1,8,1),_ImageConfigSource_Type())
imageConfigSource.setMaxAccess(_F)
if mibBuilder.loadTexts:imageConfigSource.setStatus(_A)
class _ImagePrimaryHost_Type(MxIpHostName):defaultValue=OctetString(_I)
_ImagePrimaryHost_Type.__name__=_G
_ImagePrimaryHost_Object=MibScalar
imagePrimaryHost=_ImagePrimaryHost_Object((1,3,6,1,4,1,4935,10,1,8,2),_ImagePrimaryHost_Type())
imagePrimaryHost.setMaxAccess(_F)
if mibBuilder.loadTexts:imagePrimaryHost.setStatus(_A)
class _ImagePrimaryPort_Type(MxIpPort):defaultValue=69
_ImagePrimaryPort_Type.__name__=_H
_ImagePrimaryPort_Object=MibScalar
imagePrimaryPort=_ImagePrimaryPort_Object((1,3,6,1,4,1,4935,10,1,8,3),_ImagePrimaryPort_Type())
imagePrimaryPort.setMaxAccess(_F)
if mibBuilder.loadTexts:imagePrimaryPort.setStatus(_A)
class _ImageSecondaryHost_Type(MxIpHostName):defaultValue=OctetString(_I)
_ImageSecondaryHost_Type.__name__=_G
_ImageSecondaryHost_Object=MibScalar
imageSecondaryHost=_ImageSecondaryHost_Object((1,3,6,1,4,1,4935,10,1,8,4),_ImageSecondaryHost_Type())
imageSecondaryHost.setMaxAccess(_F)
if mibBuilder.loadTexts:imageSecondaryHost.setStatus(_A)
class _ImageSecondaryPort_Type(MxIpPort):defaultValue=69
_ImageSecondaryPort_Type.__name__=_H
_ImageSecondaryPort_Object=MibScalar
imageSecondaryPort=_ImageSecondaryPort_Object((1,3,6,1,4,1,4935,10,1,8,5),_ImageSecondaryPort_Type())
imageSecondaryPort.setMaxAccess(_F)
if mibBuilder.loadTexts:imageSecondaryPort.setStatus(_A)
_ImageStatus_ObjectIdentity=ObjectIdentity
imageStatus=_ImageStatus_ObjectIdentity((1,3,6,1,4,1,4935,10,75))
class _ImageLocationStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_ImageLocationStatus_Type.__name__=_D
_ImageLocationStatus_Object=MibScalar
imageLocationStatus=_ImageLocationStatus_Object((1,3,6,1,4,1,4935,10,75,10),_ImageLocationStatus_Type())
imageLocationStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:imageLocationStatus.setStatus(_A)
_IpAddressConfigImage_ObjectIdentity=ObjectIdentity
ipAddressConfigImage=_IpAddressConfigImage_ObjectIdentity((1,3,6,1,4,1,4935,15,1,8))
class _ImageSelectConfigSource_Type(MxIpSelectConfigSource):defaultValue=1
_ImageSelectConfigSource_Type.__name__=_Q
_ImageSelectConfigSource_Object=MibScalar
imageSelectConfigSource=_ImageSelectConfigSource_Object((1,3,6,1,4,1,4935,15,1,8,1),_ImageSelectConfigSource_Type())
imageSelectConfigSource.setMaxAccess(_C)
if mibBuilder.loadTexts:imageSelectConfigSource.setStatus(_A)
_IpAddressConfigImageStatic_ObjectIdentity=ObjectIdentity
ipAddressConfigImageStatic=_IpAddressConfigImageStatic_ObjectIdentity((1,3,6,1,4,1,4935,15,1,8,5))
class _ImageStaticPrimaryHost_Type(MxIpHostName):defaultValue=OctetString(_I)
_ImageStaticPrimaryHost_Type.__name__=_G
_ImageStaticPrimaryHost_Object=MibScalar
imageStaticPrimaryHost=_ImageStaticPrimaryHost_Object((1,3,6,1,4,1,4935,15,1,8,5,1),_ImageStaticPrimaryHost_Type())
imageStaticPrimaryHost.setMaxAccess(_C)
if mibBuilder.loadTexts:imageStaticPrimaryHost.setStatus(_A)
class _ImageStaticPrimaryPort_Type(MxIpPort):defaultValue=69
_ImageStaticPrimaryPort_Type.__name__=_H
_ImageStaticPrimaryPort_Object=MibScalar
imageStaticPrimaryPort=_ImageStaticPrimaryPort_Object((1,3,6,1,4,1,4935,15,1,8,5,2),_ImageStaticPrimaryPort_Type())
imageStaticPrimaryPort.setMaxAccess(_C)
if mibBuilder.loadTexts:imageStaticPrimaryPort.setStatus(_A)
class _ImageStaticSecondaryHost_Type(MxIpHostName):defaultValue=OctetString(_I)
_ImageStaticSecondaryHost_Type.__name__=_G
_ImageStaticSecondaryHost_Object=MibScalar
imageStaticSecondaryHost=_ImageStaticSecondaryHost_Object((1,3,6,1,4,1,4935,15,1,8,5,3),_ImageStaticSecondaryHost_Type())
imageStaticSecondaryHost.setMaxAccess(_C)
if mibBuilder.loadTexts:imageStaticSecondaryHost.setStatus(_A)
class _ImageStaticSecondaryPort_Type(MxIpPort):defaultValue=69
_ImageStaticSecondaryPort_Type.__name__=_H
_ImageStaticSecondaryPort_Object=MibScalar
imageStaticSecondaryPort=_ImageStaticSecondaryPort_Object((1,3,6,1,4,1,4935,15,1,8,5,4),_ImageStaticSecondaryPort_Type())
imageStaticSecondaryPort.setMaxAccess(_C)
if mibBuilder.loadTexts:imageStaticSecondaryPort.setStatus(_A)
_IpAddressConfigImageDhcp_ObjectIdentity=ObjectIdentity
ipAddressConfigImageDhcp=_IpAddressConfigImageDhcp_ObjectIdentity((1,3,6,1,4,1,4935,15,1,8,6))
class _ImageDhcpPrimarySiteSpecificCode_Type(MxIpDhcpSiteSpecificCode):defaultValue=0
_ImageDhcpPrimarySiteSpecificCode_Type.__name__=_K
_ImageDhcpPrimarySiteSpecificCode_Object=MibScalar
imageDhcpPrimarySiteSpecificCode=_ImageDhcpPrimarySiteSpecificCode_Object((1,3,6,1,4,1,4935,15,1,8,6,1),_ImageDhcpPrimarySiteSpecificCode_Type())
imageDhcpPrimarySiteSpecificCode.setMaxAccess(_C)
if mibBuilder.loadTexts:imageDhcpPrimarySiteSpecificCode.setStatus(_A)
class _ImageDhcpSecondarySiteSpecificCode_Type(MxIpDhcpSiteSpecificCode):defaultValue=0
_ImageDhcpSecondarySiteSpecificCode_Type.__name__=_K
_ImageDhcpSecondarySiteSpecificCode_Object=MibScalar
imageDhcpSecondarySiteSpecificCode=_ImageDhcpSecondarySiteSpecificCode_Object((1,3,6,1,4,1,4935,15,1,8,6,2),_ImageDhcpSecondarySiteSpecificCode_Type())
imageDhcpSecondarySiteSpecificCode.setMaxAccess(_C)
if mibBuilder.loadTexts:imageDhcpSecondarySiteSpecificCode.setStatus(_A)
_ImageMIBObjects_ObjectIdentity=ObjectIdentity
imageMIBObjects=_ImageMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,6,1))
class _ImageLocation_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_ImageLocation_Type.__name__=_D
_ImageLocation_Object=MibScalar
imageLocation=_ImageLocation_Object((1,3,6,1,4,1,4935,15,6,1,1),_ImageLocation_Type())
imageLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:imageLocation.setStatus(_A)
class _ImageSelectionFileLocation_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_ImageSelectionFileLocation_Type.__name__=_D
_ImageSelectionFileLocation_Object=MibScalar
imageSelectionFileLocation=_ImageSelectionFileLocation_Object((1,3,6,1,4,1,4935,15,6,1,50),_ImageSelectionFileLocation_Type())
imageSelectionFileLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:imageSelectionFileLocation.setStatus(_A)
class _ImageLocationProvisionSource_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('static',0),('remoteFile',1)))
_ImageLocationProvisionSource_Type.__name__=_E
_ImageLocationProvisionSource_Object=MibScalar
imageLocationProvisionSource=_ImageLocationProvisionSource_Object((1,3,6,1,4,1,4935,15,6,1,100),_ImageLocationProvisionSource_Type())
imageLocationProvisionSource.setMaxAccess(_C)
if mibBuilder.loadTexts:imageLocationProvisionSource.setStatus(_A)
_ImageTransfer_ObjectIdentity=ObjectIdentity
imageTransfer=_ImageTransfer_ObjectIdentity((1,3,6,1,4,1,4935,15,6,1,150))
class _ImageTransferProtocol_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('tftp',0),('http',1),('https',2)))
_ImageTransferProtocol_Type.__name__=_E
_ImageTransferProtocol_Object=MibScalar
imageTransferProtocol=_ImageTransferProtocol_Object((1,3,6,1,4,1,4935,15,6,1,150,50),_ImageTransferProtocol_Type())
imageTransferProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:imageTransferProtocol.setStatus(_A)
class _ImageTransferUsername_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_ImageTransferUsername_Type.__name__=_D
_ImageTransferUsername_Object=MibScalar
imageTransferUsername=_ImageTransferUsername_Object((1,3,6,1,4,1,4935,15,6,1,150,100),_ImageTransferUsername_Type())
imageTransferUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:imageTransferUsername.setStatus(_A)
class _ImageTransferPassword_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_ImageTransferPassword_Type.__name__=_D
_ImageTransferPassword_Object=MibScalar
imageTransferPassword=_ImageTransferPassword_Object((1,3,6,1,4,1,4935,15,6,1,150,150),_ImageTransferPassword_Type())
imageTransferPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:imageTransferPassword.setStatus(_A)
_ImageAutomaticUpdate_ObjectIdentity=ObjectIdentity
imageAutomaticUpdate=_ImageAutomaticUpdate_ObjectIdentity((1,3,6,1,4,1,4935,15,6,1,200))
class _ImageAutoUpdateOnRestartEnable_Type(MxEnableState):defaultValue=0
_ImageAutoUpdateOnRestartEnable_Type.__name__=_J
_ImageAutoUpdateOnRestartEnable_Object=MibScalar
imageAutoUpdateOnRestartEnable=_ImageAutoUpdateOnRestartEnable_Object((1,3,6,1,4,1,4935,15,6,1,200,50),_ImageAutoUpdateOnRestartEnable_Type())
imageAutoUpdateOnRestartEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:imageAutoUpdateOnRestartEnable.setStatus(_A)
class _ImageAutoUpdatePeriodicEnable_Type(MxEnableState):defaultValue=0
_ImageAutoUpdatePeriodicEnable_Type.__name__=_J
_ImageAutoUpdatePeriodicEnable_Object=MibScalar
imageAutoUpdatePeriodicEnable=_ImageAutoUpdatePeriodicEnable_Object((1,3,6,1,4,1,4935,15,6,1,200,100),_ImageAutoUpdatePeriodicEnable_Type())
imageAutoUpdatePeriodicEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:imageAutoUpdatePeriodicEnable.setStatus(_A)
class _ImageAutoUpdateTimeUnit_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,20)));namedValues=NamedValues(*(('hours',0),('days',1),('minutes',20)))
_ImageAutoUpdateTimeUnit_Type.__name__=_E
_ImageAutoUpdateTimeUnit_Object=MibScalar
imageAutoUpdateTimeUnit=_ImageAutoUpdateTimeUnit_Object((1,3,6,1,4,1,4935,15,6,1,200,150),_ImageAutoUpdateTimeUnit_Type())
imageAutoUpdateTimeUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:imageAutoUpdateTimeUnit.setStatus(_A)
class _ImageAutoUpdatePeriod_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_ImageAutoUpdatePeriod_Type.__name__=_R
_ImageAutoUpdatePeriod_Object=MibScalar
imageAutoUpdatePeriod=_ImageAutoUpdatePeriod_Object((1,3,6,1,4,1,4935,15,6,1,200,200),_ImageAutoUpdatePeriod_Type())
imageAutoUpdatePeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:imageAutoUpdatePeriod.setStatus(_A)
class _ImageAutoUpdateTimeOfDay_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,23))
_ImageAutoUpdateTimeOfDay_Type.__name__=_E
_ImageAutoUpdateTimeOfDay_Object=MibScalar
imageAutoUpdateTimeOfDay=_ImageAutoUpdateTimeOfDay_Object((1,3,6,1,4,1,4935,15,6,1,200,250),_ImageAutoUpdateTimeOfDay_Type())
imageAutoUpdateTimeOfDay.setMaxAccess(_C)
if mibBuilder.loadTexts:imageAutoUpdateTimeOfDay.setStatus('deprecated')
class _ImageAutoUpdateTimeRange_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_ImageAutoUpdateTimeRange_Type.__name__=_D
_ImageAutoUpdateTimeRange_Object=MibScalar
imageAutoUpdateTimeRange=_ImageAutoUpdateTimeRange_Object((1,3,6,1,4,1,4935,15,6,1,200,300),_ImageAutoUpdateTimeRange_Type())
imageAutoUpdateTimeRange.setMaxAccess(_C)
if mibBuilder.loadTexts:imageAutoUpdateTimeRange.setStatus(_A)
_ImageConformance_ObjectIdentity=ObjectIdentity
imageConformance=_ImageConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,6,2))
_ImageCompliances_ObjectIdentity=ObjectIdentity
imageCompliances=_ImageCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,6,2,1))
_ImageGroups_ObjectIdentity=ObjectIdentity
imageGroups=_ImageGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,6,2,2))
_ImageEvents_ObjectIdentity=ObjectIdentity
imageEvents=_ImageEvents_ObjectIdentity((1,3,6,1,4,1,4935,15,6,3))
_ImageNotificationsControl_ObjectIdentity=ObjectIdentity
imageNotificationsControl=_ImageNotificationsControl_ObjectIdentity((1,3,6,1,4,1,4935,15,6,3,1))
class _ImageCompletionControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_ImageCompletionControl_Type.__name__=_E
_ImageCompletionControl_Object=MibScalar
imageCompletionControl=_ImageCompletionControl_Object((1,3,6,1,4,1,4935,15,6,3,1,1),_ImageCompletionControl_Type())
imageCompletionControl.setMaxAccess(_C)
if mibBuilder.loadTexts:imageCompletionControl.setStatus(_A)
_ImageNotifications_ObjectIdentity=ObjectIdentity
imageNotifications=_ImageNotifications_ObjectIdentity((1,3,6,1,4,1,4935,15,6,3,2))
_ImageNotificationsParams_ObjectIdentity=ObjectIdentity
imageNotificationsParams=_ImageNotificationsParams_ObjectIdentity((1,3,6,1,4,1,4935,15,6,3,4))
class _ImageLocationUsed_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_ImageLocationUsed_Type.__name__=_D
_ImageLocationUsed_Object=MibScalar
imageLocationUsed=_ImageLocationUsed_Object((1,3,6,1,4,1,4935,15,6,3,4,1),_ImageLocationUsed_Type())
imageLocationUsed.setMaxAccess(_S)
if mibBuilder.loadTexts:imageLocationUsed.setStatus(_A)
_ImageServerAddress_Type=MxIpHostName
_ImageServerAddress_Object=MibScalar
imageServerAddress=_ImageServerAddress_Object((1,3,6,1,4,1,4935,15,6,3,4,2),_ImageServerAddress_Type())
imageServerAddress.setMaxAccess(_S)
if mibBuilder.loadTexts:imageServerAddress.setStatus(_A)
imageBasicGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,6,2,2,1))
imageBasicGroupVer1.setObjects((_B,_T))
if mibBuilder.loadTexts:imageBasicGroupVer1.setStatus(_A)
imageTFTPGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,6,2,2,2))
imageTFTPGroupVer1.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:imageTFTPGroupVer1.setStatus(_A)
imageBasicNotificationControlGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,6,2,2,3))
imageBasicNotificationControlGroupVer1.setObjects((_B,_g))
if mibBuilder.loadTexts:imageBasicNotificationControlGroupVer1.setStatus(_A)
imageBasicNotificationParamsGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,6,2,2,4))
imageBasicNotificationParamsGroupVer1.setObjects(*((_B,_L),(_B,_M)))
if mibBuilder.loadTexts:imageBasicNotificationParamsGroupVer1.setStatus(_A)
imageTransferGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,6,2,2,50))
imageTransferGroupVer1.setObjects(*((_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:imageTransferGroupVer1.setStatus(_A)
imageAutomaticUpdateGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,15,6,2,2,100))
imageAutomaticUpdateGroupVer1.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:imageAutomaticUpdateGroupVer1.setStatus(_A)
imageCompletion=NotificationType((1,3,6,1,4,1,4935,15,6,3,2,1))
imageCompletion.setObjects(*((_B,_L),(_B,_M),(_N,_O)))
if mibBuilder.loadTexts:imageCompletion.setStatus(_A)
imageBasicNotificationGroupVer1=NotificationGroup((1,3,6,1,4,1,4935,15,6,2,2,5))
imageBasicNotificationGroupVer1.setObjects((_B,_q))
if mibBuilder.loadTexts:imageBasicNotificationGroupVer1.setStatus(_A)
imageBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,6,2,1,1))
imageBasicComplVer1.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:imageBasicComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ipAddressStatusImage':ipAddressStatusImage,_U:imageConfigSource,_V:imagePrimaryHost,_W:imagePrimaryPort,_X:imageSecondaryHost,_Y:imageSecondaryPort,'imageStatus':imageStatus,'imageLocationStatus':imageLocationStatus,'ipAddressConfigImage':ipAddressConfigImage,_Z:imageSelectConfigSource,'ipAddressConfigImageStatic':ipAddressConfigImageStatic,_a:imageStaticPrimaryHost,_b:imageStaticPrimaryPort,_c:imageStaticSecondaryHost,_d:imageStaticSecondaryPort,'ipAddressConfigImageDhcp':ipAddressConfigImageDhcp,_e:imageDhcpPrimarySiteSpecificCode,_f:imageDhcpSecondarySiteSpecificCode,'imageMIB':imageMIB,'imageMIBObjects':imageMIBObjects,_T:imageLocation,'imageSelectionFileLocation':imageSelectionFileLocation,'imageLocationProvisionSource':imageLocationProvisionSource,'imageTransfer':imageTransfer,_h:imageTransferProtocol,_i:imageTransferUsername,_j:imageTransferPassword,'imageAutomaticUpdate':imageAutomaticUpdate,_k:imageAutoUpdateOnRestartEnable,_l:imageAutoUpdatePeriodicEnable,_m:imageAutoUpdateTimeUnit,_n:imageAutoUpdatePeriod,_o:imageAutoUpdateTimeOfDay,_p:imageAutoUpdateTimeRange,'imageConformance':imageConformance,'imageCompliances':imageCompliances,'imageBasicComplVer1':imageBasicComplVer1,'imageGroups':imageGroups,_r:imageBasicGroupVer1,'imageTFTPGroupVer1':imageTFTPGroupVer1,_s:imageBasicNotificationControlGroupVer1,_t:imageBasicNotificationParamsGroupVer1,_u:imageBasicNotificationGroupVer1,_v:imageTransferGroupVer1,_w:imageAutomaticUpdateGroupVer1,'imageEvents':imageEvents,'imageNotificationsControl':imageNotificationsControl,_g:imageCompletionControl,'imageNotifications':imageNotifications,_q:imageCompletion,'imageNotificationsParams':imageNotificationsParams,_L:imageLocationUsed,_M:imageServerAddress})