_O='package'
_N='taggedData'
_M='binaryCompressed'
_L='binary'
_K='iEEE695'
_J='intelHexCompressed'
_I='intelHex'
_H='flashFileID'
_G='flashVolume'
_F='CT-FLASH-MIB'
_E='DisplayString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctFlash,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctFlash')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_FlashStatus_ObjectIdentity=ObjectIdentity
flashStatus=_FlashStatus_ObjectIdentity((1,3,6,1,4,1,52,4,1,5,10,1))
_FlashVolumeStatusTable_Object=MibTable
flashVolumeStatusTable=_FlashVolumeStatusTable_Object((1,3,6,1,4,1,52,4,1,5,10,1,1))
if mibBuilder.loadTexts:flashVolumeStatusTable.setStatus(_A)
_FlashVolumeStatusEntry_Object=MibTableRow
flashVolumeStatusEntry=_FlashVolumeStatusEntry_Object((1,3,6,1,4,1,52,4,1,5,10,1,1,1))
flashVolumeStatusEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:flashVolumeStatusEntry.setStatus(_A)
_FlashVolume_Type=Integer32
_FlashVolume_Object=MibTableColumn
flashVolume=_FlashVolume_Object((1,3,6,1,4,1,52,4,1,5,10,1,1,1,1),_FlashVolume_Type())
flashVolume.setMaxAccess(_B)
if mibBuilder.loadTexts:flashVolume.setStatus(_A)
_FlashVolFiles_Type=Integer32
_FlashVolFiles_Object=MibTableColumn
flashVolFiles=_FlashVolFiles_Object((1,3,6,1,4,1,52,4,1,5,10,1,1,1,2),_FlashVolFiles_Type())
flashVolFiles.setMaxAccess(_B)
if mibBuilder.loadTexts:flashVolFiles.setStatus(_A)
_FlashVolSpace_Type=Integer32
_FlashVolSpace_Object=MibTableColumn
flashVolSpace=_FlashVolSpace_Object((1,3,6,1,4,1,52,4,1,5,10,1,1,1,3),_FlashVolSpace_Type())
flashVolSpace.setMaxAccess(_B)
if mibBuilder.loadTexts:flashVolSpace.setStatus(_A)
_FlashFile_ObjectIdentity=ObjectIdentity
flashFile=_FlashFile_ObjectIdentity((1,3,6,1,4,1,52,4,1,5,10,2))
_FlashFileTable_Object=MibTable
flashFileTable=_FlashFileTable_Object((1,3,6,1,4,1,52,4,1,5,10,2,1))
if mibBuilder.loadTexts:flashFileTable.setStatus(_A)
_FlashFileEntry_Object=MibTableRow
flashFileEntry=_FlashFileEntry_Object((1,3,6,1,4,1,52,4,1,5,10,2,1,1))
flashFileEntry.setIndexNames((0,_F,_G),(0,_F,_H))
if mibBuilder.loadTexts:flashFileEntry.setStatus(_A)
_FlashFileID_Type=Integer32
_FlashFileID_Object=MibTableColumn
flashFileID=_FlashFileID_Object((1,3,6,1,4,1,52,4,1,5,10,2,1,1,1),_FlashFileID_Type())
flashFileID.setMaxAccess(_B)
if mibBuilder.loadTexts:flashFileID.setStatus(_A)
class _FlashFilename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FlashFilename_Type.__name__=_E
_FlashFilename_Object=MibTableColumn
flashFilename=_FlashFilename_Object((1,3,6,1,4,1,52,4,1,5,10,2,1,1,2),_FlashFilename_Type())
flashFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:flashFilename.setStatus(_A)
class _FlashFileVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_FlashFileVersion_Type.__name__=_E
_FlashFileVersion_Object=MibTableColumn
flashFileVersion=_FlashFileVersion_Object((1,3,6,1,4,1,52,4,1,5,10,2,1,1,3),_FlashFileVersion_Type())
flashFileVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:flashFileVersion.setStatus(_A)
class _FlashFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),('eLF',4),('table',5),('dLL',6),('bOOT',7),(_L,8),(_M,9),(_N,10),(_O,11)))
_FlashFileType_Type.__name__=_D
_FlashFileType_Object=MibTableColumn
flashFileType=_FlashFileType_Object((1,3,6,1,4,1,52,4,1,5,10,2,1,1,4),_FlashFileType_Type())
flashFileType.setMaxAccess(_B)
if mibBuilder.loadTexts:flashFileType.setStatus(_A)
_FlashFileSize_Type=Integer32
_FlashFileSize_Object=MibTableColumn
flashFileSize=_FlashFileSize_Object((1,3,6,1,4,1,52,4,1,5,10,2,1,1,5),_FlashFileSize_Type())
flashFileSize.setMaxAccess(_B)
if mibBuilder.loadTexts:flashFileSize.setStatus(_A)
_FlashCmd_ObjectIdentity=ObjectIdentity
flashCmd=_FlashCmd_ObjectIdentity((1,3,6,1,4,1,52,4,1,5,10,3))
class _FlashCmdPath_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FlashCmdPath_Type.__name__=_E
_FlashCmdPath_Object=MibScalar
flashCmdPath=_FlashCmdPath_Object((1,3,6,1,4,1,52,4,1,5,10,3,1),_FlashCmdPath_Type())
flashCmdPath.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCmdPath.setStatus(_A)
_FlashCmdNetAddress_Type=IpAddress
_FlashCmdNetAddress_Object=MibScalar
flashCmdNetAddress=_FlashCmdNetAddress_Object((1,3,6,1,4,1,52,4,1,5,10,3,2),_FlashCmdNetAddress_Type())
flashCmdNetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCmdNetAddress.setStatus(_A)
_FlashCmdVolume_Type=Integer32
_FlashCmdVolume_Object=MibScalar
flashCmdVolume=_FlashCmdVolume_Object((1,3,6,1,4,1,52,4,1,5,10,3,3),_FlashCmdVolume_Type())
flashCmdVolume.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCmdVolume.setStatus(_A)
class _FlashCmdOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('install',1),('download',2),('upload',3),('cleanup',4),('delete',5),('none',6)))
_FlashCmdOperation_Type.__name__=_D
_FlashCmdOperation_Object=MibScalar
flashCmdOperation=_FlashCmdOperation_Object((1,3,6,1,4,1,52,4,1,5,10,3,4),_FlashCmdOperation_Type())
flashCmdOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCmdOperation.setStatus(_A)
class _FlashCmdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('idle',1),('other',2),('flashVerifyServer',3),('flashCleanup',4),('downLoadActive',5),('upLoadActive',6),('completeError',7)))
_FlashCmdStatus_Type.__name__=_D
_FlashCmdStatus_Object=MibScalar
flashCmdStatus=_FlashCmdStatus_Object((1,3,6,1,4,1,52,4,1,5,10,3,5),_FlashCmdStatus_Type())
flashCmdStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:flashCmdStatus.setStatus(_A)
class _FlashCmdError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*(('oK',1),('deleteFailed',2),('fileSystem',3),('tFTPerror',4),('corruptFile',5),('dupFlashName',6),('noFlashFile',7),('flashAlloc',8),('maxFiles',9),('invalidName',10),('protocolErr',11),('serverLost',12),('noNetFile',13),('noNetAccess',14),('netDiskFull',15),('dupNetFile',16),('parseError',17),('invalidType',18),('invalidCmd',19),('invalidModId',20),('noServerIP',21),('socketError',22),('blockSequence',23),('bufferError',24)))
_FlashCmdError_Type.__name__=_D
_FlashCmdError_Object=MibScalar
flashCmdError=_FlashCmdError_Object((1,3,6,1,4,1,52,4,1,5,10,3,6),_FlashCmdError_Type())
flashCmdError.setMaxAccess(_B)
if mibBuilder.loadTexts:flashCmdError.setStatus(_A)
class _FlashCmdFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FlashCmdFile_Type.__name__=_E
_FlashCmdFile_Object=MibScalar
flashCmdFile=_FlashCmdFile_Object((1,3,6,1,4,1,52,4,1,5,10,3,7),_FlashCmdFile_Type())
flashCmdFile.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCmdFile.setStatus(_A)
class _FlashCmdVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_FlashCmdVersion_Type.__name__=_E
_FlashCmdVersion_Object=MibScalar
flashCmdVersion=_FlashCmdVersion_Object((1,3,6,1,4,1,52,4,1,5,10,3,8),_FlashCmdVersion_Type())
flashCmdVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCmdVersion.setStatus(_A)
class _FlashCmdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_I,1),(_J,2),(_K,3),('eLF',4),('table',5),('dLL',6),('bOOT',7),(_L,8),(_M,9),(_N,10),(_O,11)))
_FlashCmdType_Type.__name__=_D
_FlashCmdType_Object=MibScalar
flashCmdType=_FlashCmdType_Object((1,3,6,1,4,1,52,4,1,5,10,3,9),_FlashCmdType_Type())
flashCmdType.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCmdType.setStatus(_A)
_FlashCmdSize_Type=Integer32
_FlashCmdSize_Object=MibScalar
flashCmdSize=_FlashCmdSize_Object((1,3,6,1,4,1,52,4,1,5,10,3,10),_FlashCmdSize_Type())
flashCmdSize.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCmdSize.setStatus(_A)
_FlashBlockCount_Type=Integer32
_FlashBlockCount_Object=MibScalar
flashBlockCount=_FlashBlockCount_Object((1,3,6,1,4,1,52,4,1,5,10,3,11),_FlashBlockCount_Type())
flashBlockCount.setMaxAccess(_B)
if mibBuilder.loadTexts:flashBlockCount.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'flashStatus':flashStatus,'flashVolumeStatusTable':flashVolumeStatusTable,'flashVolumeStatusEntry':flashVolumeStatusEntry,_G:flashVolume,'flashVolFiles':flashVolFiles,'flashVolSpace':flashVolSpace,'flashFile':flashFile,'flashFileTable':flashFileTable,'flashFileEntry':flashFileEntry,_H:flashFileID,'flashFilename':flashFilename,'flashFileVersion':flashFileVersion,'flashFileType':flashFileType,'flashFileSize':flashFileSize,'flashCmd':flashCmd,'flashCmdPath':flashCmdPath,'flashCmdNetAddress':flashCmdNetAddress,'flashCmdVolume':flashCmdVolume,'flashCmdOperation':flashCmdOperation,'flashCmdStatus':flashCmdStatus,'flashCmdError':flashCmdError,'flashCmdFile':flashCmdFile,'flashCmdVersion':flashCmdVersion,'flashCmdType':flashCmdType,'flashCmdSize':flashCmdSize,'flashBlockCount':flashBlockCount})