_T='v2FwIndex'
_S='cmpLZMA'
_R='cmpNRV2D99'
_Q='cmpReserved'
_P='cmpMiniLZ'
_O='cmpLZRLE'
_N='not-accessible'
_M='v2NonVolIndex'
_L='OctetString'
_K='BRCM-V2-FACTORY-MIB'
_J='Bits'
_I='other'
_H='inProgress'
_G='success'
_F='failure'
_E='TruthValue'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cableDataFactory,=mibBuilder.importSymbols('BRCM-CABLEDATA-FACTORY-MIB','cableDataFactory')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_J,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention',_E)
v2Factory=ModuleIdentity((1,3,6,1,4,1,4413,2,99,1,1,2,4))
if mibBuilder.loadTexts:v2Factory.setRevisions(('2007-02-05 00:00','2004-04-09 00:00','2003-07-11 00:00','2003-04-16 00:00','2002-09-12 00:00'))
_V2FactoryNonVol_ObjectIdentity=ObjectIdentity
v2FactoryNonVol=_V2FactoryNonVol_ObjectIdentity((1,3,6,1,4,1,4413,2,99,1,1,2,4,1))
_V2FactNonVolTable_Object=MibTable
v2FactNonVolTable=_V2FactNonVolTable_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,1))
if mibBuilder.loadTexts:v2FactNonVolTable.setStatus(_A)
_V2FactNonVolEntry_Object=MibTableRow
v2FactNonVolEntry=_V2FactNonVolEntry_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,1,1))
v2FactNonVolEntry.setIndexNames((0,_K,_M))
if mibBuilder.loadTexts:v2FactNonVolEntry.setStatus(_A)
class _V2NonVolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_V2NonVolIndex_Type.__name__=_D
_V2NonVolIndex_Object=MibTableColumn
v2NonVolIndex=_V2NonVolIndex_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,1,1,1),_V2NonVolIndex_Type())
v2NonVolIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:v2NonVolIndex.setStatus(_A)
_V2NonVolName_Type=DisplayString
_V2NonVolName_Object=MibTableColumn
v2NonVolName=_V2NonVolName_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,1,1,2),_V2NonVolName_Type())
v2NonVolName.setMaxAccess(_B)
if mibBuilder.loadTexts:v2NonVolName.setStatus(_A)
class _V2NonVolMagicNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_V2NonVolMagicNumber_Type.__name__=_L
_V2NonVolMagicNumber_Object=MibTableColumn
v2NonVolMagicNumber=_V2NonVolMagicNumber_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,1,1,3),_V2NonVolMagicNumber_Type())
v2NonVolMagicNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:v2NonVolMagicNumber.setStatus(_A)
_V2NonVolVersionPermanent_Type=DisplayString
_V2NonVolVersionPermanent_Object=MibTableColumn
v2NonVolVersionPermanent=_V2NonVolVersionPermanent_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,1,1,4),_V2NonVolVersionPermanent_Type())
v2NonVolVersionPermanent.setMaxAccess(_B)
if mibBuilder.loadTexts:v2NonVolVersionPermanent.setStatus(_A)
_V2NonVolVersionDynamic_Type=DisplayString
_V2NonVolVersionDynamic_Object=MibTableColumn
v2NonVolVersionDynamic=_V2NonVolVersionDynamic_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,1,1,5),_V2NonVolVersionDynamic_Type())
v2NonVolVersionDynamic.setMaxAccess(_B)
if mibBuilder.loadTexts:v2NonVolVersionDynamic.setStatus(_A)
_V2NonVolIsDefaultPermanent_Type=TruthValue
_V2NonVolIsDefaultPermanent_Object=MibTableColumn
v2NonVolIsDefaultPermanent=_V2NonVolIsDefaultPermanent_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,1,1,6),_V2NonVolIsDefaultPermanent_Type())
v2NonVolIsDefaultPermanent.setMaxAccess(_B)
if mibBuilder.loadTexts:v2NonVolIsDefaultPermanent.setStatus(_A)
_V2NonVolIsDefaultDynamic_Type=TruthValue
_V2NonVolIsDefaultDynamic_Object=MibTableColumn
v2NonVolIsDefaultDynamic=_V2NonVolIsDefaultDynamic_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,1,1,7),_V2NonVolIsDefaultDynamic_Type())
v2NonVolIsDefaultDynamic.setMaxAccess(_B)
if mibBuilder.loadTexts:v2NonVolIsDefaultDynamic.setStatus(_A)
_V2NonVolRawData_Type=OctetString
_V2NonVolRawData_Object=MibTableColumn
v2NonVolRawData=_V2NonVolRawData_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,1,1,8),_V2NonVolRawData_Type())
v2NonVolRawData.setMaxAccess(_B)
if mibBuilder.loadTexts:v2NonVolRawData.setStatus(_A)
_V2NonVolIsManufacturedPermanent_Type=TruthValue
_V2NonVolIsManufacturedPermanent_Object=MibTableColumn
v2NonVolIsManufacturedPermanent=_V2NonVolIsManufacturedPermanent_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,1,1,9),_V2NonVolIsManufacturedPermanent_Type())
v2NonVolIsManufacturedPermanent.setMaxAccess(_B)
if mibBuilder.loadTexts:v2NonVolIsManufacturedPermanent.setStatus(_A)
_V2NonVolMfgHintPermanent_Type=DisplayString
_V2NonVolMfgHintPermanent_Object=MibTableColumn
v2NonVolMfgHintPermanent=_V2NonVolMfgHintPermanent_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,1,1,10),_V2NonVolMfgHintPermanent_Type())
v2NonVolMfgHintPermanent.setMaxAccess(_B)
if mibBuilder.loadTexts:v2NonVolMfgHintPermanent.setStatus(_A)
_V2NonVolIsManufacturedDynamic_Type=TruthValue
_V2NonVolIsManufacturedDynamic_Object=MibTableColumn
v2NonVolIsManufacturedDynamic=_V2NonVolIsManufacturedDynamic_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,1,1,11),_V2NonVolIsManufacturedDynamic_Type())
v2NonVolIsManufacturedDynamic.setMaxAccess(_B)
if mibBuilder.loadTexts:v2NonVolIsManufacturedDynamic.setStatus(_A)
_V2NonVolMfgHintDynamic_Type=DisplayString
_V2NonVolMfgHintDynamic_Object=MibTableColumn
v2NonVolMfgHintDynamic=_V2NonVolMfgHintDynamic_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,1,1,12),_V2NonVolMfgHintDynamic_Type())
v2NonVolMfgHintDynamic.setMaxAccess(_B)
if mibBuilder.loadTexts:v2NonVolMfgHintDynamic.setStatus(_A)
_V2NonVolControl_ObjectIdentity=ObjectIdentity
v2NonVolControl=_V2NonVolControl_ObjectIdentity((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,2))
class _V2NonVolControlGroup_Type(Integer32):defaultValue=0
_V2NonVolControlGroup_Type.__name__=_D
_V2NonVolControlGroup_Object=MibScalar
v2NonVolControlGroup=_V2NonVolControlGroup_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,2,1),_V2NonVolControlGroup_Type())
v2NonVolControlGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:v2NonVolControlGroup.setStatus(_A)
class _V2NonVolControlSection_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('permanent',1),('dynamic',2),('both',3)))
_V2NonVolControlSection_Type.__name__=_D
_V2NonVolControlSection_Object=MibScalar
v2NonVolControlSection=_V2NonVolControlSection_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,2,2),_V2NonVolControlSection_Type())
v2NonVolControlSection.setMaxAccess(_C)
if mibBuilder.loadTexts:v2NonVolControlSection.setStatus(_A)
_V2NonVolRestoreDefaults_Type=TruthValue
_V2NonVolRestoreDefaults_Object=MibScalar
v2NonVolRestoreDefaults=_V2NonVolRestoreDefaults_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,2,3),_V2NonVolRestoreDefaults_Type())
v2NonVolRestoreDefaults.setMaxAccess(_C)
if mibBuilder.loadTexts:v2NonVolRestoreDefaults.setStatus(_A)
_V2NonVolTftpServer_Type=IpAddress
_V2NonVolTftpServer_Object=MibScalar
v2NonVolTftpServer=_V2NonVolTftpServer_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,2,4),_V2NonVolTftpServer_Type())
v2NonVolTftpServer.setMaxAccess(_C)
if mibBuilder.loadTexts:v2NonVolTftpServer.setStatus(_A)
_V2NonVolTftpPath_Type=SnmpAdminString
_V2NonVolTftpPath_Object=MibScalar
v2NonVolTftpPath=_V2NonVolTftpPath_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,2,5),_V2NonVolTftpPath_Type())
v2NonVolTftpPath.setMaxAccess(_C)
if mibBuilder.loadTexts:v2NonVolTftpPath.setStatus(_A)
_V2NonVolDloadNow_Type=TruthValue
_V2NonVolDloadNow_Object=MibScalar
v2NonVolDloadNow=_V2NonVolDloadNow_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,2,6),_V2NonVolDloadNow_Type())
v2NonVolDloadNow.setMaxAccess(_C)
if mibBuilder.loadTexts:v2NonVolDloadNow.setStatus(_A)
class _V2NonVolDloadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3)))
_V2NonVolDloadStatus_Type.__name__=_D
_V2NonVolDloadStatus_Object=MibScalar
v2NonVolDloadStatus=_V2NonVolDloadStatus_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,2,7),_V2NonVolDloadStatus_Type())
v2NonVolDloadStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:v2NonVolDloadStatus.setStatus(_A)
_V2NonVolDelExtraData_Type=TruthValue
_V2NonVolDelExtraData_Object=MibScalar
v2NonVolDelExtraData=_V2NonVolDelExtraData_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,2,8),_V2NonVolDelExtraData_Type())
v2NonVolDelExtraData.setMaxAccess(_C)
if mibBuilder.loadTexts:v2NonVolDelExtraData.setStatus(_A)
_V2NonVolFlush_Type=TruthValue
_V2NonVolFlush_Object=MibScalar
v2NonVolFlush=_V2NonVolFlush_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,2,9),_V2NonVolFlush_Type())
v2NonVolFlush.setMaxAccess(_C)
if mibBuilder.loadTexts:v2NonVolFlush.setStatus(_A)
_V2NonVolClearDevice_Type=TruthValue
_V2NonVolClearDevice_Object=MibScalar
v2NonVolClearDevice=_V2NonVolClearDevice_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,1,2,10),_V2NonVolClearDevice_Type())
v2NonVolClearDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:v2NonVolClearDevice.setStatus(_A)
_V2FactoryImages_ObjectIdentity=ObjectIdentity
v2FactoryImages=_V2FactoryImages_ObjectIdentity((1,3,6,1,4,1,4413,2,99,1,1,2,4,2))
_V2ImagesBootloader_ObjectIdentity=ObjectIdentity
v2ImagesBootloader=_V2ImagesBootloader_ObjectIdentity((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,1))
_V2BootloaderVersion_Type=Unsigned32
_V2BootloaderVersion_Object=MibScalar
v2BootloaderVersion=_V2BootloaderVersion_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,1,1),_V2BootloaderVersion_Type())
v2BootloaderVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:v2BootloaderVersion.setStatus(_A)
_V2BootloaderSignature_Type=Unsigned32
_V2BootloaderSignature_Object=MibScalar
v2BootloaderSignature=_V2BootloaderSignature_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,1,2),_V2BootloaderSignature_Type())
v2BootloaderSignature.setMaxAccess(_B)
if mibBuilder.loadTexts:v2BootloaderSignature.setStatus(_A)
_V2BootloaderBoardInfo_Type=Unsigned32
_V2BootloaderBoardInfo_Object=MibScalar
v2BootloaderBoardInfo=_V2BootloaderBoardInfo_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,1,3),_V2BootloaderBoardInfo_Type())
v2BootloaderBoardInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:v2BootloaderBoardInfo.setStatus(_A)
class _V2BootloaderCompressionSupport_Type(Bits):namedValues=NamedValues(*((_O,0),(_P,1),(_Q,2),(_R,3),(_S,4)))
_V2BootloaderCompressionSupport_Type.__name__=_J
_V2BootloaderCompressionSupport_Object=MibScalar
v2BootloaderCompressionSupport=_V2BootloaderCompressionSupport_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,1,4),_V2BootloaderCompressionSupport_Type())
v2BootloaderCompressionSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:v2BootloaderCompressionSupport.setStatus(_A)
class _V2BootloaderIncompatibleImageCheckEnabled_Type(TruthValue):defaultValue=1
_V2BootloaderIncompatibleImageCheckEnabled_Type.__name__=_E
_V2BootloaderIncompatibleImageCheckEnabled_Object=MibScalar
v2BootloaderIncompatibleImageCheckEnabled=_V2BootloaderIncompatibleImageCheckEnabled_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,1,5),_V2BootloaderIncompatibleImageCheckEnabled_Type())
v2BootloaderIncompatibleImageCheckEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:v2BootloaderIncompatibleImageCheckEnabled.setStatus(_A)
_V2BootloaderDloadTftpServer_Type=IpAddress
_V2BootloaderDloadTftpServer_Object=MibScalar
v2BootloaderDloadTftpServer=_V2BootloaderDloadTftpServer_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,1,6),_V2BootloaderDloadTftpServer_Type())
v2BootloaderDloadTftpServer.setMaxAccess(_C)
if mibBuilder.loadTexts:v2BootloaderDloadTftpServer.setStatus(_A)
_V2BootloaderDloadTftpPath_Type=SnmpAdminString
_V2BootloaderDloadTftpPath_Object=MibScalar
v2BootloaderDloadTftpPath=_V2BootloaderDloadTftpPath_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,1,7),_V2BootloaderDloadTftpPath_Type())
v2BootloaderDloadTftpPath.setMaxAccess(_C)
if mibBuilder.loadTexts:v2BootloaderDloadTftpPath.setStatus(_A)
_V2BootloaderDloadNow_Type=TruthValue
_V2BootloaderDloadNow_Object=MibScalar
v2BootloaderDloadNow=_V2BootloaderDloadNow_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,1,8),_V2BootloaderDloadNow_Type())
v2BootloaderDloadNow.setMaxAccess(_C)
if mibBuilder.loadTexts:v2BootloaderDloadNow.setStatus(_A)
class _V2BootloaderDloadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3)))
_V2BootloaderDloadStatus_Type.__name__=_D
_V2BootloaderDloadStatus_Object=MibScalar
v2BootloaderDloadStatus=_V2BootloaderDloadStatus_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,1,9),_V2BootloaderDloadStatus_Type())
v2BootloaderDloadStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:v2BootloaderDloadStatus.setStatus(_A)
_V2ImagesFirmware_ObjectIdentity=ObjectIdentity
v2ImagesFirmware=_V2ImagesFirmware_ObjectIdentity((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2))
_V2FirmwareTable_Object=MibTable
v2FirmwareTable=_V2FirmwareTable_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,1))
if mibBuilder.loadTexts:v2FirmwareTable.setStatus(_A)
_V2FirmwareEntry_Object=MibTableRow
v2FirmwareEntry=_V2FirmwareEntry_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,1,1))
v2FirmwareEntry.setIndexNames((0,_K,_T))
if mibBuilder.loadTexts:v2FirmwareEntry.setStatus(_A)
class _V2FwIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_V2FwIndex_Type.__name__=_D
_V2FwIndex_Object=MibTableColumn
v2FwIndex=_V2FwIndex_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,1,1,1),_V2FwIndex_Type())
v2FwIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:v2FwIndex.setStatus(_A)
_V2FwSignature_Type=Unsigned32
_V2FwSignature_Object=MibTableColumn
v2FwSignature=_V2FwSignature_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,1,1,2),_V2FwSignature_Type())
v2FwSignature.setMaxAccess(_B)
if mibBuilder.loadTexts:v2FwSignature.setStatus(_A)
class _V2FwControl_Type(Bits):namedValues=NamedValues(*((_O,0),(_P,1),(_Q,2),(_R,3),(_S,4)))
_V2FwControl_Type.__name__=_J
_V2FwControl_Object=MibTableColumn
v2FwControl=_V2FwControl_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,1,1,3),_V2FwControl_Type())
v2FwControl.setMaxAccess(_B)
if mibBuilder.loadTexts:v2FwControl.setStatus(_A)
_V2FwRevision_Type=DisplayString
_V2FwRevision_Object=MibTableColumn
v2FwRevision=_V2FwRevision_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,1,1,4),_V2FwRevision_Type())
v2FwRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:v2FwRevision.setStatus(_A)
_V2FwBuildTime_Type=DateAndTime
_V2FwBuildTime_Object=MibTableColumn
v2FwBuildTime=_V2FwBuildTime_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,1,1,5),_V2FwBuildTime_Type())
v2FwBuildTime.setMaxAccess(_B)
if mibBuilder.loadTexts:v2FwBuildTime.setStatus(_A)
_V2FwFileSize_Type=Unsigned32
_V2FwFileSize_Object=MibTableColumn
v2FwFileSize=_V2FwFileSize_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,1,1,6),_V2FwFileSize_Type())
v2FwFileSize.setMaxAccess(_B)
if mibBuilder.loadTexts:v2FwFileSize.setStatus(_A)
_V2FwMaxImageSize_Type=Unsigned32
_V2FwMaxImageSize_Object=MibTableColumn
v2FwMaxImageSize=_V2FwMaxImageSize_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,1,1,7),_V2FwMaxImageSize_Type())
v2FwMaxImageSize.setMaxAccess(_B)
if mibBuilder.loadTexts:v2FwMaxImageSize.setStatus(_A)
_V2FwFileName_Type=DisplayString
_V2FwFileName_Object=MibTableColumn
v2FwFileName=_V2FwFileName_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,1,1,8),_V2FwFileName_Type())
v2FwFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:v2FwFileName.setStatus(_A)
_V2FwHCS_Type=Unsigned32
_V2FwHCS_Object=MibTableColumn
v2FwHCS=_V2FwHCS_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,1,1,9),_V2FwHCS_Type())
v2FwHCS.setMaxAccess(_B)
if mibBuilder.loadTexts:v2FwHCS.setStatus(_A)
_V2FwCRC_Type=Unsigned32
_V2FwCRC_Object=MibTableColumn
v2FwCRC=_V2FwCRC_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,1,1,10),_V2FwCRC_Type())
v2FwCRC.setMaxAccess(_B)
if mibBuilder.loadTexts:v2FwCRC.setStatus(_A)
_V2FirmwareControl_ObjectIdentity=ObjectIdentity
v2FirmwareControl=_V2FirmwareControl_ObjectIdentity((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,2))
_V2FwControlImageNumber_Type=Integer32
_V2FwControlImageNumber_Object=MibScalar
v2FwControlImageNumber=_V2FwControlImageNumber_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,2,1),_V2FwControlImageNumber_Type())
v2FwControlImageNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:v2FwControlImageNumber.setStatus(_A)
_V2FwDloadTftpServer_Type=IpAddress
_V2FwDloadTftpServer_Object=MibScalar
v2FwDloadTftpServer=_V2FwDloadTftpServer_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,2,2),_V2FwDloadTftpServer_Type())
v2FwDloadTftpServer.setMaxAccess(_C)
if mibBuilder.loadTexts:v2FwDloadTftpServer.setStatus(_A)
_V2FwDloadTftpPath_Type=SnmpAdminString
_V2FwDloadTftpPath_Object=MibScalar
v2FwDloadTftpPath=_V2FwDloadTftpPath_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,2,3),_V2FwDloadTftpPath_Type())
v2FwDloadTftpPath.setMaxAccess(_C)
if mibBuilder.loadTexts:v2FwDloadTftpPath.setStatus(_A)
class _V2FwDloadLarge_Type(TruthValue):defaultValue=2
_V2FwDloadLarge_Type.__name__=_E
_V2FwDloadLarge_Object=MibScalar
v2FwDloadLarge=_V2FwDloadLarge_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,2,4),_V2FwDloadLarge_Type())
v2FwDloadLarge.setMaxAccess(_C)
if mibBuilder.loadTexts:v2FwDloadLarge.setStatus(_A)
class _V2FwDloadForce_Type(TruthValue):defaultValue=2
_V2FwDloadForce_Type.__name__=_E
_V2FwDloadForce_Object=MibScalar
v2FwDloadForce=_V2FwDloadForce_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,2,5),_V2FwDloadForce_Type())
v2FwDloadForce.setMaxAccess(_C)
if mibBuilder.loadTexts:v2FwDloadForce.setStatus(_A)
_V2FwDloadNow_Type=TruthValue
_V2FwDloadNow_Object=MibScalar
v2FwDloadNow=_V2FwDloadNow_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,2,6),_V2FwDloadNow_Type())
v2FwDloadNow.setMaxAccess(_C)
if mibBuilder.loadTexts:v2FwDloadNow.setStatus(_A)
class _V2FwDloadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3)))
_V2FwDloadStatus_Type.__name__=_D
_V2FwDloadStatus_Object=MibScalar
v2FwDloadStatus=_V2FwDloadStatus_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,2,7),_V2FwDloadStatus_Type())
v2FwDloadStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:v2FwDloadStatus.setStatus(_A)
_V2FwDeleteImage_Type=TruthValue
_V2FwDeleteImage_Object=MibScalar
v2FwDeleteImage=_V2FwDeleteImage_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,2,8),_V2FwDeleteImage_Type())
v2FwDeleteImage.setMaxAccess(_C)
if mibBuilder.loadTexts:v2FwDeleteImage.setStatus(_A)
_V2FwCopyImageFrom_Type=Integer32
_V2FwCopyImageFrom_Object=MibScalar
v2FwCopyImageFrom=_V2FwCopyImageFrom_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,2,9),_V2FwCopyImageFrom_Type())
v2FwCopyImageFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:v2FwCopyImageFrom.setStatus(_A)
class _V2FwCopyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3)))
_V2FwCopyStatus_Type.__name__=_D
_V2FwCopyStatus_Object=MibScalar
v2FwCopyStatus=_V2FwCopyStatus_Object((1,3,6,1,4,1,4413,2,99,1,1,2,4,2,2,2,10),_V2FwCopyStatus_Type())
v2FwCopyStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:v2FwCopyStatus.setStatus(_A)
mibBuilder.exportSymbols(_K,**{'v2Factory':v2Factory,'v2FactoryNonVol':v2FactoryNonVol,'v2FactNonVolTable':v2FactNonVolTable,'v2FactNonVolEntry':v2FactNonVolEntry,_M:v2NonVolIndex,'v2NonVolName':v2NonVolName,'v2NonVolMagicNumber':v2NonVolMagicNumber,'v2NonVolVersionPermanent':v2NonVolVersionPermanent,'v2NonVolVersionDynamic':v2NonVolVersionDynamic,'v2NonVolIsDefaultPermanent':v2NonVolIsDefaultPermanent,'v2NonVolIsDefaultDynamic':v2NonVolIsDefaultDynamic,'v2NonVolRawData':v2NonVolRawData,'v2NonVolIsManufacturedPermanent':v2NonVolIsManufacturedPermanent,'v2NonVolMfgHintPermanent':v2NonVolMfgHintPermanent,'v2NonVolIsManufacturedDynamic':v2NonVolIsManufacturedDynamic,'v2NonVolMfgHintDynamic':v2NonVolMfgHintDynamic,'v2NonVolControl':v2NonVolControl,'v2NonVolControlGroup':v2NonVolControlGroup,'v2NonVolControlSection':v2NonVolControlSection,'v2NonVolRestoreDefaults':v2NonVolRestoreDefaults,'v2NonVolTftpServer':v2NonVolTftpServer,'v2NonVolTftpPath':v2NonVolTftpPath,'v2NonVolDloadNow':v2NonVolDloadNow,'v2NonVolDloadStatus':v2NonVolDloadStatus,'v2NonVolDelExtraData':v2NonVolDelExtraData,'v2NonVolFlush':v2NonVolFlush,'v2NonVolClearDevice':v2NonVolClearDevice,'v2FactoryImages':v2FactoryImages,'v2ImagesBootloader':v2ImagesBootloader,'v2BootloaderVersion':v2BootloaderVersion,'v2BootloaderSignature':v2BootloaderSignature,'v2BootloaderBoardInfo':v2BootloaderBoardInfo,'v2BootloaderCompressionSupport':v2BootloaderCompressionSupport,'v2BootloaderIncompatibleImageCheckEnabled':v2BootloaderIncompatibleImageCheckEnabled,'v2BootloaderDloadTftpServer':v2BootloaderDloadTftpServer,'v2BootloaderDloadTftpPath':v2BootloaderDloadTftpPath,'v2BootloaderDloadNow':v2BootloaderDloadNow,'v2BootloaderDloadStatus':v2BootloaderDloadStatus,'v2ImagesFirmware':v2ImagesFirmware,'v2FirmwareTable':v2FirmwareTable,'v2FirmwareEntry':v2FirmwareEntry,_T:v2FwIndex,'v2FwSignature':v2FwSignature,'v2FwControl':v2FwControl,'v2FwRevision':v2FwRevision,'v2FwBuildTime':v2FwBuildTime,'v2FwFileSize':v2FwFileSize,'v2FwMaxImageSize':v2FwMaxImageSize,'v2FwFileName':v2FwFileName,'v2FwHCS':v2FwHCS,'v2FwCRC':v2FwCRC,'v2FirmwareControl':v2FirmwareControl,'v2FwControlImageNumber':v2FwControlImageNumber,'v2FwDloadTftpServer':v2FwDloadTftpServer,'v2FwDloadTftpPath':v2FwDloadTftpPath,'v2FwDloadLarge':v2FwDloadLarge,'v2FwDloadForce':v2FwDloadForce,'v2FwDloadNow':v2FwDloadNow,'v2FwDloadStatus':v2FwDloadStatus,'v2FwDeleteImage':v2FwDeleteImage,'v2FwCopyImageFrom':v2FwCopyImageFrom,'v2FwCopyStatus':v2FwCopyStatus})