_X='wwpLeosSwXgradeStatus'
_W='wwpLeosSwXgradeOpStatus'
_V='wwpLeosSwXgradePackage'
_U='wwpLeosSwDownloadNotificationInfo'
_T='wwpLeosSwDownloadFailCause'
_S='wwpLeosSwDownloadPackageName'
_R='unknown'
_Q='success'
_P='processing'
_O='download'
_N='install'
_M='wwpLeosSwXgradeOp'
_L='none'
_K='TruthValue'
_J='AddressFamilyNumbers'
_I='wwpLeosSwXgradeBladeId'
_H='deprecated'
_G='Integer32'
_F='OctetString'
_E='DisplayString'
_D='read-only'
_C='WWP-LEOS-SW-XGRADE-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AddressFamilyNumbers,=mibBuilder.importSymbols('IANA-ADDRESS-FAMILY-NUMBERS-MIB',_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention',_K)
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosSwXgradeMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,10))
if mibBuilder.loadTexts:wwpLeosSwXgradeMIB.setRevisions(('2012-06-27 00:00','2011-08-01 00:00','2011-07-07 00:01','2011-07-07 00:00','2003-04-21 17:00'))
class SwDownloadState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('idle',1),('downloading',2),('downloadComplete',3),('downloadFailed',4)))
class SwDownloadFailCause(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('downloadSuccess',0),('invalidPkgFile',1),('couldNotGetFile',2),('tftpServerNotFound',3),('cmdFileParseError',4),('internalFilesystemError',5),('flashOffline',6),('noStatus',7),('badFileCrc',8),('alreadyUpgradeMode',9),('unknownError',10)))
class SwXgradeOp(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_L,0),(_N,1),('inServiceActivate',2),('serviceAffectingActivate',3),('inServiceXgrade',4),('serviceAffectingXgrade',5),('servAffectingXgradeReport',6),('servNonAffectingXgradeReport',7),(_O,8),('cancelDownload',9)))
_WwpLeosSwXgradeMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosSwXgradeMIBObjects=_WwpLeosSwXgradeMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,10,1))
_WwpLeosSwXgrade_ObjectIdentity=ObjectIdentity
wwpLeosSwXgrade=_WwpLeosSwXgrade_ObjectIdentity((1,3,6,1,4,1,6141,2,60,10,1,1))
_WwpLeosSwDownload_ObjectIdentity=ObjectIdentity
wwpLeosSwDownload=_WwpLeosSwDownload_ObjectIdentity((1,3,6,1,4,1,6141,2,60,10,1,1,1))
class _WwpLeosSwDownloadServerAddrType_Type(AddressFamilyNumbers):defaultValue=0
_WwpLeosSwDownloadServerAddrType_Type.__name__=_J
_WwpLeosSwDownloadServerAddrType_Object=MibScalar
wwpLeosSwDownloadServerAddrType=_WwpLeosSwDownloadServerAddrType_Object((1,3,6,1,4,1,6141,2,60,10,1,1,1,1),_WwpLeosSwDownloadServerAddrType_Type())
wwpLeosSwDownloadServerAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwDownloadServerAddrType.setStatus(_H)
class _WwpLeosSwDownloadServerAddr_Type(DisplayString):defaultValue=OctetString('')
_WwpLeosSwDownloadServerAddr_Type.__name__=_E
_WwpLeosSwDownloadServerAddr_Object=MibScalar
wwpLeosSwDownloadServerAddr=_WwpLeosSwDownloadServerAddr_Object((1,3,6,1,4,1,6141,2,60,10,1,1,1,2),_WwpLeosSwDownloadServerAddr_Type())
wwpLeosSwDownloadServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwDownloadServerAddr.setStatus(_H)
class _WwpLeosSwDownloadPackageName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_WwpLeosSwDownloadPackageName_Type.__name__=_E
_WwpLeosSwDownloadPackageName_Object=MibScalar
wwpLeosSwDownloadPackageName=_WwpLeosSwDownloadPackageName_Object((1,3,6,1,4,1,6141,2,60,10,1,1,1,3),_WwpLeosSwDownloadPackageName_Type())
wwpLeosSwDownloadPackageName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwDownloadPackageName.setStatus(_H)
class _WwpLeosSwDownLoadActivate_Type(TruthValue):defaultValue=2
_WwpLeosSwDownLoadActivate_Type.__name__=_K
_WwpLeosSwDownLoadActivate_Object=MibScalar
wwpLeosSwDownLoadActivate=_WwpLeosSwDownLoadActivate_Object((1,3,6,1,4,1,6141,2,60,10,1,1,1,4),_WwpLeosSwDownLoadActivate_Type())
wwpLeosSwDownLoadActivate.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwDownLoadActivate.setStatus(_H)
class _WwpLeosSwDownloadNotifOnCompletion_Type(TruthValue):defaultValue=1
_WwpLeosSwDownloadNotifOnCompletion_Type.__name__=_K
_WwpLeosSwDownloadNotifOnCompletion_Object=MibScalar
wwpLeosSwDownloadNotifOnCompletion=_WwpLeosSwDownloadNotifOnCompletion_Object((1,3,6,1,4,1,6141,2,60,10,1,1,1,5),_WwpLeosSwDownloadNotifOnCompletion_Type())
wwpLeosSwDownloadNotifOnCompletion.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwDownloadNotifOnCompletion.setStatus(_H)
_WwpLeosSwDownloadStatus_Type=SwDownloadState
_WwpLeosSwDownloadStatus_Object=MibScalar
wwpLeosSwDownloadStatus=_WwpLeosSwDownloadStatus_Object((1,3,6,1,4,1,6141,2,60,10,1,1,1,6),_WwpLeosSwDownloadStatus_Type())
wwpLeosSwDownloadStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosSwDownloadStatus.setStatus(_H)
_WwpLeosSwDownloadFailCause_Type=SwDownloadFailCause
_WwpLeosSwDownloadFailCause_Object=MibScalar
wwpLeosSwDownloadFailCause=_WwpLeosSwDownloadFailCause_Object((1,3,6,1,4,1,6141,2,60,10,1,1,1,7),_WwpLeosSwDownloadFailCause_Type())
wwpLeosSwDownloadFailCause.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosSwDownloadFailCause.setStatus(_H)
class _WwpLeosSwDownloadNotificationInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_WwpLeosSwDownloadNotificationInfo_Type.__name__=_E
_WwpLeosSwDownloadNotificationInfo_Object=MibScalar
wwpLeosSwDownloadNotificationInfo=_WwpLeosSwDownloadNotificationInfo_Object((1,3,6,1,4,1,6141,2,60,10,1,1,1,8),_WwpLeosSwDownloadNotificationInfo_Type())
wwpLeosSwDownloadNotificationInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosSwDownloadNotificationInfo.setStatus(_H)
_WwpLeosSwXgradeBladeTable_Object=MibTable
wwpLeosSwXgradeBladeTable=_WwpLeosSwXgradeBladeTable_Object((1,3,6,1,4,1,6141,2,60,10,1,1,2))
if mibBuilder.loadTexts:wwpLeosSwXgradeBladeTable.setStatus(_A)
_WwpLeosSwXgradeBladeEntry_Object=MibTableRow
wwpLeosSwXgradeBladeEntry=_WwpLeosSwXgradeBladeEntry_Object((1,3,6,1,4,1,6141,2,60,10,1,1,2,1))
wwpLeosSwXgradeBladeEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wwpLeosSwXgradeBladeEntry.setStatus(_A)
class _WwpLeosSwXgradeBladeId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosSwXgradeBladeId_Type.__name__=_G
_WwpLeosSwXgradeBladeId_Object=MibTableColumn
wwpLeosSwXgradeBladeId=_WwpLeosSwXgradeBladeId_Object((1,3,6,1,4,1,6141,2,60,10,1,1,2,1,1),_WwpLeosSwXgradeBladeId_Type())
wwpLeosSwXgradeBladeId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosSwXgradeBladeId.setStatus(_A)
class _WwpLeosSwXgradePackage_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_WwpLeosSwXgradePackage_Type.__name__=_E
_WwpLeosSwXgradePackage_Object=MibTableColumn
wwpLeosSwXgradePackage=_WwpLeosSwXgradePackage_Object((1,3,6,1,4,1,6141,2,60,10,1,1,2,1,2),_WwpLeosSwXgradePackage_Type())
wwpLeosSwXgradePackage.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwXgradePackage.setStatus(_A)
_WwpLeosSwXgradeOp_Type=SwXgradeOp
_WwpLeosSwXgradeOp_Object=MibTableColumn
wwpLeosSwXgradeOp=_WwpLeosSwXgradeOp_Object((1,3,6,1,4,1,6141,2,60,10,1,1,2,1,3),_WwpLeosSwXgradeOp_Type())
wwpLeosSwXgradeOp.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwXgradeOp.setStatus(_A)
class _WwpLeosSwXgradeTftpAddrType_Type(AddressFamilyNumbers):defaultValue=0
_WwpLeosSwXgradeTftpAddrType_Type.__name__=_J
_WwpLeosSwXgradeTftpAddrType_Object=MibTableColumn
wwpLeosSwXgradeTftpAddrType=_WwpLeosSwXgradeTftpAddrType_Object((1,3,6,1,4,1,6141,2,60,10,1,1,2,1,4),_WwpLeosSwXgradeTftpAddrType_Type())
wwpLeosSwXgradeTftpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwXgradeTftpAddrType.setStatus(_A)
class _WwpLeosSwXgradeTftpAddr_Type(DisplayString):defaultValue=OctetString('')
_WwpLeosSwXgradeTftpAddr_Type.__name__=_E
_WwpLeosSwXgradeTftpAddr_Object=MibTableColumn
wwpLeosSwXgradeTftpAddr=_WwpLeosSwXgradeTftpAddr_Object((1,3,6,1,4,1,6141,2,60,10,1,1,2,1,5),_WwpLeosSwXgradeTftpAddr_Type())
wwpLeosSwXgradeTftpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwXgradeTftpAddr.setStatus(_A)
_WwpLeosSwXgradeOpActivate_Type=TruthValue
_WwpLeosSwXgradeOpActivate_Object=MibTableColumn
wwpLeosSwXgradeOpActivate=_WwpLeosSwXgradeOpActivate_Object((1,3,6,1,4,1,6141,2,60,10,1,1,2,1,6),_WwpLeosSwXgradeOpActivate_Type())
wwpLeosSwXgradeOpActivate.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwXgradeOpActivate.setStatus(_A)
class _WwpLeosSwXgradeOpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_P,2),(_Q,3),('failure',4)))
_WwpLeosSwXgradeOpStatus_Type.__name__=_G
_WwpLeosSwXgradeOpStatus_Object=MibTableColumn
wwpLeosSwXgradeOpStatus=_WwpLeosSwXgradeOpStatus_Object((1,3,6,1,4,1,6141,2,60,10,1,1,2,1,7),_WwpLeosSwXgradeOpStatus_Type())
wwpLeosSwXgradeOpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosSwXgradeOpStatus.setStatus(_A)
_WwpLeosSwXgradePackagePath_Type=DisplayString
_WwpLeosSwXgradePackagePath_Object=MibTableColumn
wwpLeosSwXgradePackagePath=_WwpLeosSwXgradePackagePath_Object((1,3,6,1,4,1,6141,2,60,10,1,1,2,1,8),_WwpLeosSwXgradePackagePath_Type())
wwpLeosSwXgradePackagePath.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwXgradePackagePath.setStatus(_A)
class _WwpLeosSwXgradeTransferMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('tftp',1),('ftp',2),('sftp',3),('defaultTftp',4),('defaultFtp',5),('defaultSftp',6),('default',7)))
_WwpLeosSwXgradeTransferMode_Type.__name__=_G
_WwpLeosSwXgradeTransferMode_Object=MibTableColumn
wwpLeosSwXgradeTransferMode=_WwpLeosSwXgradeTransferMode_Object((1,3,6,1,4,1,6141,2,60,10,1,1,2,1,9),_WwpLeosSwXgradeTransferMode_Type())
wwpLeosSwXgradeTransferMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwXgradeTransferMode.setStatus(_A)
class _WwpLeosSwXgradeLoginId_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WwpLeosSwXgradeLoginId_Type.__name__=_E
_WwpLeosSwXgradeLoginId_Object=MibTableColumn
wwpLeosSwXgradeLoginId=_WwpLeosSwXgradeLoginId_Object((1,3,6,1,4,1,6141,2,60,10,1,1,2,1,10),_WwpLeosSwXgradeLoginId_Type())
wwpLeosSwXgradeLoginId.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwXgradeLoginId.setStatus(_A)
class _WwpLeosSwXgradePassword_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_WwpLeosSwXgradePassword_Type.__name__=_E
_WwpLeosSwXgradePassword_Object=MibTableColumn
wwpLeosSwXgradePassword=_WwpLeosSwXgradePassword_Object((1,3,6,1,4,1,6141,2,60,10,1,1,2,1,11),_WwpLeosSwXgradePassword_Type())
wwpLeosSwXgradePassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwXgradePassword.setStatus(_A)
class _WwpLeosSwXgradeSecret_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_WwpLeosSwXgradeSecret_Type.__name__=_E
_WwpLeosSwXgradeSecret_Object=MibTableColumn
wwpLeosSwXgradeSecret=_WwpLeosSwXgradeSecret_Object((1,3,6,1,4,1,6141,2,60,10,1,1,2,1,12),_WwpLeosSwXgradeSecret_Type())
wwpLeosSwXgradeSecret.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwXgradeSecret.setStatus(_A)
_WwpLeosBladePackageInfoTable_Object=MibTable
wwpLeosBladePackageInfoTable=_WwpLeosBladePackageInfoTable_Object((1,3,6,1,4,1,6141,2,60,10,1,1,3))
if mibBuilder.loadTexts:wwpLeosBladePackageInfoTable.setStatus(_A)
_WwpLeosBladePackageInfoEntry_Object=MibTableRow
wwpLeosBladePackageInfoEntry=_WwpLeosBladePackageInfoEntry_Object((1,3,6,1,4,1,6141,2,60,10,1,1,3,1))
wwpLeosBladePackageInfoEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wwpLeosBladePackageInfoEntry.setStatus(_A)
class _WwpLeosBladeInstPackageVer_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_WwpLeosBladeInstPackageVer_Type.__name__=_F
_WwpLeosBladeInstPackageVer_Object=MibTableColumn
wwpLeosBladeInstPackageVer=_WwpLeosBladeInstPackageVer_Object((1,3,6,1,4,1,6141,2,60,10,1,1,3,1,1),_WwpLeosBladeInstPackageVer_Type())
wwpLeosBladeInstPackageVer.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBladeInstPackageVer.setStatus(_A)
class _WwpLeosBladeRunPackageVer_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_WwpLeosBladeRunPackageVer_Type.__name__=_F
_WwpLeosBladeRunPackageVer_Object=MibTableColumn
wwpLeosBladeRunPackageVer=_WwpLeosBladeRunPackageVer_Object((1,3,6,1,4,1,6141,2,60,10,1,1,3,1,2),_WwpLeosBladeRunPackageVer_Type())
wwpLeosBladeRunPackageVer.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBladeRunPackageVer.setStatus(_A)
class _WwpLeosBladeDnldPackageVer_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_WwpLeosBladeDnldPackageVer_Type.__name__=_F
_WwpLeosBladeDnldPackageVer_Object=MibTableColumn
wwpLeosBladeDnldPackageVer=_WwpLeosBladeDnldPackageVer_Object((1,3,6,1,4,1,6141,2,60,10,1,1,3,1,3),_WwpLeosBladeDnldPackageVer_Type())
wwpLeosBladeDnldPackageVer.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBladeDnldPackageVer.setStatus(_A)
class _WwpLeosBladeInstPackageRlsStatus_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_WwpLeosBladeInstPackageRlsStatus_Type.__name__=_F
_WwpLeosBladeInstPackageRlsStatus_Object=MibTableColumn
wwpLeosBladeInstPackageRlsStatus=_WwpLeosBladeInstPackageRlsStatus_Object((1,3,6,1,4,1,6141,2,60,10,1,1,3,1,4),_WwpLeosBladeInstPackageRlsStatus_Type())
wwpLeosBladeInstPackageRlsStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosBladeInstPackageRlsStatus.setStatus(_A)
_WwpLeosSwXgradeGlobalAttrs_ObjectIdentity=ObjectIdentity
wwpLeosSwXgradeGlobalAttrs=_WwpLeosSwXgradeGlobalAttrs_ObjectIdentity((1,3,6,1,4,1,6141,2,60,10,1,1,4))
_WwpLeosSwMIBVersion_Type=DisplayString
_WwpLeosSwMIBVersion_Object=MibScalar
wwpLeosSwMIBVersion=_WwpLeosSwMIBVersion_Object((1,3,6,1,4,1,6141,2,60,10,1,1,4,1),_WwpLeosSwMIBVersion_Type())
wwpLeosSwMIBVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosSwMIBVersion.setStatus(_A)
class _WwpLeosSwXgradeDestPath_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_WwpLeosSwXgradeDestPath_Type.__name__=_F
_WwpLeosSwXgradeDestPath_Object=MibScalar
wwpLeosSwXgradeDestPath=_WwpLeosSwXgradeDestPath_Object((1,3,6,1,4,1,6141,2,60,10,1,1,4,2),_WwpLeosSwXgradeDestPath_Type())
wwpLeosSwXgradeDestPath.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwXgradeDestPath.setStatus(_A)
class _WwpLeosSwXgradePackagePathName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_WwpLeosSwXgradePackagePathName_Type.__name__=_F
_WwpLeosSwXgradePackagePathName_Object=MibScalar
wwpLeosSwXgradePackagePathName=_WwpLeosSwXgradePackagePathName_Object((1,3,6,1,4,1,6141,2,60,10,1,1,4,3),_WwpLeosSwXgradePackagePathName_Type())
wwpLeosSwXgradePackagePathName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwXgradePackagePathName.setStatus(_A)
class _WwpLeosSwXgradeTftpServer_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_WwpLeosSwXgradeTftpServer_Type.__name__=_F
_WwpLeosSwXgradeTftpServer_Object=MibScalar
wwpLeosSwXgradeTftpServer=_WwpLeosSwXgradeTftpServer_Object((1,3,6,1,4,1,6141,2,60,10,1,1,4,4),_WwpLeosSwXgradeTftpServer_Type())
wwpLeosSwXgradeTftpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwXgradeTftpServer.setStatus(_A)
class _WwpLeosSwXgradeRevertTimeout_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosSwXgradeRevertTimeout_Type.__name__=_G
_WwpLeosSwXgradeRevertTimeout_Object=MibScalar
wwpLeosSwXgradeRevertTimeout=_WwpLeosSwXgradeRevertTimeout_Object((1,3,6,1,4,1,6141,2,60,10,1,1,4,5),_WwpLeosSwXgradeRevertTimeout_Type())
wwpLeosSwXgradeRevertTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwXgradeRevertTimeout.setStatus(_A)
class _WwpLeosSwXgradeBootOrder_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('localFlash',1),('localFlashThenCompactFlash',2),('compactFlashThenLocalFlash',3),(_R,4)))
_WwpLeosSwXgradeBootOrder_Type.__name__=_G
_WwpLeosSwXgradeBootOrder_Object=MibScalar
wwpLeosSwXgradeBootOrder=_WwpLeosSwXgradeBootOrder_Object((1,3,6,1,4,1,6141,2,60,10,1,1,4,6),_WwpLeosSwXgradeBootOrder_Type())
wwpLeosSwXgradeBootOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwXgradeBootOrder.setStatus(_A)
class _WwpLeosSwXgradeOptype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_L,0),(_O,1),(_N,2),('activate',3),('protect',4),('revert',5),('validate',6),('run',7)))
_WwpLeosSwXgradeOptype_Type.__name__=_G
_WwpLeosSwXgradeOptype_Object=MibScalar
wwpLeosSwXgradeOptype=_WwpLeosSwXgradeOptype_Object((1,3,6,1,4,1,6141,2,60,10,1,1,25),_WwpLeosSwXgradeOptype_Type())
wwpLeosSwXgradeOptype.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosSwXgradeOptype.setStatus(_A)
class _WwpLeosSwXgradeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)));namedValues=NamedValues(*((_Q,1),('failed',2),(_R,3),(_P,4),('invalidCfgRule',5),('invalidFileName',6),('fileSystemError',7),('cannotResolveHostName',8),('tftpClientTimeout',9),('tftpServerError',10),('tftpBadTag',11),('tftpBadValue',12),('networkError',13),('platformTypeNotSupported',14),('swMgrBusy',15),('needBackupSw',16),('internalError',17),('fileNotExist',18),('missingAttribute',19),('invalidXgradeOp',20),('noDefaultTftpConfigured',21)))
_WwpLeosSwXgradeStatus_Type.__name__=_G
_WwpLeosSwXgradeStatus_Object=MibScalar
wwpLeosSwXgradeStatus=_WwpLeosSwXgradeStatus_Object((1,3,6,1,4,1,6141,2,60,10,1,1,30),_WwpLeosSwXgradeStatus_Type())
wwpLeosSwXgradeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosSwXgradeStatus.setStatus(_A)
_WwpLeosSwXgradeMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosSwXgradeMIBNotificationPrefix=_WwpLeosSwXgradeMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,10,2))
_WwpLeosSwXgradeMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosSwXgradeMIBNotifications=_WwpLeosSwXgradeMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,10,2,0))
_WwpLeosSwXgradeMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosSwXgradeMIBConformance=_WwpLeosSwXgradeMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,10,3))
_WwpLeosSwXgradeMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosSwXgradeMIBCompliances=_WwpLeosSwXgradeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,10,3,1))
_WwpLeosSwXgradeMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosSwXgradeMIBGroups=_WwpLeosSwXgradeMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,10,3,2))
wwpLeosSwDownloadCompletion=NotificationType((1,3,6,1,4,1,6141,2,60,10,2,0,1))
wwpLeosSwDownloadCompletion.setObjects(*((_C,_S),(_C,_T),(_C,_U)))
if mibBuilder.loadTexts:wwpLeosSwDownloadCompletion.setStatus(_A)
wwpLeosSwXgradeOpCompletion=NotificationType((1,3,6,1,4,1,6141,2,60,10,2,0,2))
wwpLeosSwXgradeOpCompletion.setObjects(*((_C,_I),(_C,_V),(_C,_M),(_C,_W)))
if mibBuilder.loadTexts:wwpLeosSwXgradeOpCompletion.setStatus(_A)
wwpLeosSwXgradeBladePkgIncorrect=NotificationType((1,3,6,1,4,1,6141,2,60,10,2,0,3))
wwpLeosSwXgradeBladePkgIncorrect.setObjects((_C,_I))
if mibBuilder.loadTexts:wwpLeosSwXgradeBladePkgIncorrect.setStatus(_A)
wwpLeosSwXgradeCompletion=NotificationType((1,3,6,1,4,1,6141,2,60,10,2,0,4))
wwpLeosSwXgradeCompletion.setObjects(*((_C,_M),(_C,_X)))
if mibBuilder.loadTexts:wwpLeosSwXgradeCompletion.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'SwDownloadState':SwDownloadState,'SwDownloadFailCause':SwDownloadFailCause,'SwXgradeOp':SwXgradeOp,'wwpLeosSwXgradeMIB':wwpLeosSwXgradeMIB,'wwpLeosSwXgradeMIBObjects':wwpLeosSwXgradeMIBObjects,'wwpLeosSwXgrade':wwpLeosSwXgrade,'wwpLeosSwDownload':wwpLeosSwDownload,'wwpLeosSwDownloadServerAddrType':wwpLeosSwDownloadServerAddrType,'wwpLeosSwDownloadServerAddr':wwpLeosSwDownloadServerAddr,_S:wwpLeosSwDownloadPackageName,'wwpLeosSwDownLoadActivate':wwpLeosSwDownLoadActivate,'wwpLeosSwDownloadNotifOnCompletion':wwpLeosSwDownloadNotifOnCompletion,'wwpLeosSwDownloadStatus':wwpLeosSwDownloadStatus,_T:wwpLeosSwDownloadFailCause,_U:wwpLeosSwDownloadNotificationInfo,'wwpLeosSwXgradeBladeTable':wwpLeosSwXgradeBladeTable,'wwpLeosSwXgradeBladeEntry':wwpLeosSwXgradeBladeEntry,_I:wwpLeosSwXgradeBladeId,_V:wwpLeosSwXgradePackage,_M:wwpLeosSwXgradeOp,'wwpLeosSwXgradeTftpAddrType':wwpLeosSwXgradeTftpAddrType,'wwpLeosSwXgradeTftpAddr':wwpLeosSwXgradeTftpAddr,'wwpLeosSwXgradeOpActivate':wwpLeosSwXgradeOpActivate,_W:wwpLeosSwXgradeOpStatus,'wwpLeosSwXgradePackagePath':wwpLeosSwXgradePackagePath,'wwpLeosSwXgradeTransferMode':wwpLeosSwXgradeTransferMode,'wwpLeosSwXgradeLoginId':wwpLeosSwXgradeLoginId,'wwpLeosSwXgradePassword':wwpLeosSwXgradePassword,'wwpLeosSwXgradeSecret':wwpLeosSwXgradeSecret,'wwpLeosBladePackageInfoTable':wwpLeosBladePackageInfoTable,'wwpLeosBladePackageInfoEntry':wwpLeosBladePackageInfoEntry,'wwpLeosBladeInstPackageVer':wwpLeosBladeInstPackageVer,'wwpLeosBladeRunPackageVer':wwpLeosBladeRunPackageVer,'wwpLeosBladeDnldPackageVer':wwpLeosBladeDnldPackageVer,'wwpLeosBladeInstPackageRlsStatus':wwpLeosBladeInstPackageRlsStatus,'wwpLeosSwXgradeGlobalAttrs':wwpLeosSwXgradeGlobalAttrs,'wwpLeosSwMIBVersion':wwpLeosSwMIBVersion,'wwpLeosSwXgradeDestPath':wwpLeosSwXgradeDestPath,'wwpLeosSwXgradePackagePathName':wwpLeosSwXgradePackagePathName,'wwpLeosSwXgradeTftpServer':wwpLeosSwXgradeTftpServer,'wwpLeosSwXgradeRevertTimeout':wwpLeosSwXgradeRevertTimeout,'wwpLeosSwXgradeBootOrder':wwpLeosSwXgradeBootOrder,'wwpLeosSwXgradeOptype':wwpLeosSwXgradeOptype,_X:wwpLeosSwXgradeStatus,'wwpLeosSwXgradeMIBNotificationPrefix':wwpLeosSwXgradeMIBNotificationPrefix,'wwpLeosSwXgradeMIBNotifications':wwpLeosSwXgradeMIBNotifications,'wwpLeosSwDownloadCompletion':wwpLeosSwDownloadCompletion,'wwpLeosSwXgradeOpCompletion':wwpLeosSwXgradeOpCompletion,'wwpLeosSwXgradeBladePkgIncorrect':wwpLeosSwXgradeBladePkgIncorrect,'wwpLeosSwXgradeCompletion':wwpLeosSwXgradeCompletion,'wwpLeosSwXgradeMIBConformance':wwpLeosSwXgradeMIBConformance,'wwpLeosSwXgradeMIBCompliances':wwpLeosSwXgradeMIBCompliances,'wwpLeosSwXgradeMIBGroups':wwpLeosSwXgradeMIBGroups})