_J='failed'
_I='success'
_H='vmImagesFilesIndex'
_G='filesIndex'
_F='read-write'
_E='MX-FILE-MIB'
_D='OctetString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap','MxEnableState','MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fileMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2600))
_FileMIBObjects_ObjectIdentity=ObjectIdentity
fileMIBObjects=_FileMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2600,1))
_FilesTable_Object=MibTable
filesTable=_FilesTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,100))
if mibBuilder.loadTexts:filesTable.setStatus(_A)
_FilesEntry_Object=MibTableRow
filesEntry=_FilesEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,100,1))
filesEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:filesEntry.setStatus(_A)
_FilesIndex_Type=Unsigned32
_FilesIndex_Object=MibTableColumn
filesIndex=_FilesIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,100,1,101),_FilesIndex_Type())
filesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:filesIndex.setStatus(_A)
class _FilesFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,510))
_FilesFileName_Type.__name__=_D
_FilesFileName_Object=MibTableColumn
filesFileName=_FilesFileName_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,100,1,201),_FilesFileName_Type())
filesFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:filesFileName.setStatus(_A)
class _FilesFileDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FilesFileDescription_Type.__name__=_D
_FilesFileDescription_Object=MibTableColumn
filesFileDescription=_FilesFileDescription_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,100,1,400),_FilesFileDescription_Type())
filesFileDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:filesFileDescription.setStatus(_A)
_FilesFileSize_Type=Unsigned32
_FilesFileSize_Object=MibTableColumn
filesFileSize=_FilesFileSize_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,100,1,500),_FilesFileSize_Type())
filesFileSize.setMaxAccess(_B)
if mibBuilder.loadTexts:filesFileSize.setStatus(_A)
_VmImagesFilesTable_Object=MibTable
vmImagesFilesTable=_VmImagesFilesTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,150))
if mibBuilder.loadTexts:vmImagesFilesTable.setStatus(_A)
_VmImagesFilesEntry_Object=MibTableRow
vmImagesFilesEntry=_VmImagesFilesEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,150,1))
vmImagesFilesEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:vmImagesFilesEntry.setStatus(_A)
_VmImagesFilesIndex_Type=Unsigned32
_VmImagesFilesIndex_Object=MibTableColumn
vmImagesFilesIndex=_VmImagesFilesIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,150,1,100),_VmImagesFilesIndex_Type())
vmImagesFilesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vmImagesFilesIndex.setStatus(_A)
class _VmImagesFilesFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,510))
_VmImagesFilesFileName_Type.__name__=_D
_VmImagesFilesFileName_Object=MibTableColumn
vmImagesFilesFileName=_VmImagesFilesFileName_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,150,1,200),_VmImagesFilesFileName_Type())
vmImagesFilesFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:vmImagesFilesFileName.setStatus(_A)
class _VmImagesFilesFileDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VmImagesFilesFileDescription_Type.__name__=_D
_VmImagesFilesFileDescription_Object=MibTableColumn
vmImagesFilesFileDescription=_VmImagesFilesFileDescription_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,150,1,300),_VmImagesFilesFileDescription_Type())
vmImagesFilesFileDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:vmImagesFilesFileDescription.setStatus(_A)
_VmImagesFilesFileSize_Type=Unsigned32
_VmImagesFilesFileSize_Object=MibTableColumn
vmImagesFilesFileSize=_VmImagesFilesFileSize_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,150,1,400),_VmImagesFilesFileSize_Type())
vmImagesFilesFileSize.setMaxAccess(_B)
if mibBuilder.loadTexts:vmImagesFilesFileSize.setStatus(_A)
_FileSystemQuotaSize_Type=Unsigned32
_FileSystemQuotaSize_Object=MibScalar
fileSystemQuotaSize=_FileSystemQuotaSize_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,200),_FileSystemQuotaSize_Type())
fileSystemQuotaSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fileSystemQuotaSize.setStatus(_A)
_FileSystemAvailableSize_Type=Unsigned32
_FileSystemAvailableSize_Object=MibScalar
fileSystemAvailableSize=_FileSystemAvailableSize_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,250),_FileSystemAvailableSize_Type())
fileSystemAvailableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fileSystemAvailableSize.setStatus(_A)
_VmImagesAvailableSize_Type=Unsigned32
_VmImagesAvailableSize_Object=MibScalar
vmImagesAvailableSize=_VmImagesAvailableSize_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,280),_VmImagesAvailableSize_Type())
vmImagesAvailableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:vmImagesAvailableSize.setStatus(_A)
_TransferGroup_ObjectIdentity=ObjectIdentity
transferGroup=_TransferGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,500))
class _TransferHttpsCipherSuite_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('cS1',100),('cS2',200),('cS3',300)))
_TransferHttpsCipherSuite_Type.__name__=_C
_TransferHttpsCipherSuite_Object=MibScalar
transferHttpsCipherSuite=_TransferHttpsCipherSuite_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,500,100),_TransferHttpsCipherSuite_Type())
transferHttpsCipherSuite.setMaxAccess(_F)
if mibBuilder.loadTexts:transferHttpsCipherSuite.setStatus(_A)
class _TransferHttpsTlsVersion_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('sSLv3',100),('tLSv1',200),('tLSv1-1',300),('tLSv1-2',400)))
_TransferHttpsTlsVersion_Type.__name__=_C
_TransferHttpsTlsVersion_Object=MibScalar
transferHttpsTlsVersion=_TransferHttpsTlsVersion_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,500,200),_TransferHttpsTlsVersion_Type())
transferHttpsTlsVersion.setMaxAccess(_F)
if mibBuilder.loadTexts:transferHttpsTlsVersion.setStatus(_A)
_Statistics_ObjectIdentity=ObjectIdentity
statistics=_Statistics_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,600))
class _StatLastDownloadFileResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('none',100),('downloading',200),(_I,300),(_J,400)))
_StatLastDownloadFileResult_Type.__name__=_C
_StatLastDownloadFileResult_Object=MibScalar
statLastDownloadFileResult=_StatLastDownloadFileResult_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,600,100),_StatLastDownloadFileResult_Type())
statLastDownloadFileResult.setMaxAccess(_B)
if mibBuilder.loadTexts:statLastDownloadFileResult.setStatus(_A)
class _StatLastUploadFileResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('none',100),('uploading',200),(_I,300),(_J,400)))
_StatLastUploadFileResult_Type.__name__=_C
_StatLastUploadFileResult_Object=MibScalar
statLastUploadFileResult=_StatLastUploadFileResult_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,600,200),_StatLastUploadFileResult_Type())
statLastUploadFileResult.setMaxAccess(_B)
if mibBuilder.loadTexts:statLastUploadFileResult.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_C
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_F)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_C
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,2600,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fileMIB':fileMIB,'fileMIBObjects':fileMIBObjects,'filesTable':filesTable,'filesEntry':filesEntry,_G:filesIndex,'filesFileName':filesFileName,'filesFileDescription':filesFileDescription,'filesFileSize':filesFileSize,'vmImagesFilesTable':vmImagesFilesTable,'vmImagesFilesEntry':vmImagesFilesEntry,_H:vmImagesFilesIndex,'vmImagesFilesFileName':vmImagesFilesFileName,'vmImagesFilesFileDescription':vmImagesFilesFileDescription,'vmImagesFilesFileSize':vmImagesFilesFileSize,'fileSystemQuotaSize':fileSystemQuotaSize,'fileSystemAvailableSize':fileSystemAvailableSize,'vmImagesAvailableSize':vmImagesAvailableSize,'transferGroup':transferGroup,'transferHttpsCipherSuite':transferHttpsCipherSuite,'transferHttpsTlsVersion':transferHttpsTlsVersion,'statistics':statistics,'statLastDownloadFileResult':statLastDownloadFileResult,'statLastUploadFileResult':statLastUploadFileResult,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})