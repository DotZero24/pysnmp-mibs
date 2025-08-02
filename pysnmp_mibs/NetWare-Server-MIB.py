_g='nwVolUsageUserID'
_f='nwVolUsageVolID'
_e='nwUserVolVolID'
_d='nwUserVolUserID'
_c='expired'
_b='nwUserID'
_a='nwSetDescrIndex'
_Z='nwSetDescrParamIndex'
_Y='nwSetDescrCategoryIndex'
_X='nwSetParamIndex'
_W='nwSetParamCategoryIndex'
_V='nwSetCategoryIndex'
_U='nwNLMIndex'
_T='nwSft3EngineType'
_S='nwQServerID'
_R='nwQServerQID'
_Q='nwQJobNumber'
_P='nwQJobQID'
_O='nwConnectionNumber'
_N='nwOfileConnection'
_M='nwOfileDirectoryNumber'
_L='nwOfileVolID'
_K='nwVolID'
_J='disabled'
_I='enabled'
_H='unknown'
_G='other'
_F='read-write'
_E='InternationalDisplayString'
_D='NetWare-Server-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InternationalDisplayString,KBytes=mibBuilder.importSymbols('HOST-RESOURCES-MIB',_E,'KBytes')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
class Seconds(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class IPXNetNumber(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class TransportDomain(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noAddress',1),('ipx',2),('ip',3),('appleTalkDDP',4)))
class TransportAddress(OctetString):0
class EngineType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('msEngine',1),('ioEnginePrimary',2),('ioEngineSecondary',3)))
class DSTType(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_Novell_ObjectIdentity=ObjectIdentity
novell=_Novell_ObjectIdentity((1,3,6,1,4,1,23))
_MibDoc_ObjectIdentity=ObjectIdentity
mibDoc=_MibDoc_ObjectIdentity((1,3,6,1,4,1,23,2))
_NwServer_ObjectIdentity=ObjectIdentity
nwServer=_NwServer_ObjectIdentity((1,3,6,1,4,1,23,2,28))
_NwSystem_ObjectIdentity=ObjectIdentity
nwSystem=_NwSystem_ObjectIdentity((1,3,6,1,4,1,23,2,28,1))
class _NwSysServerName_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_NwSysServerName_Type.__name__=_E
_NwSysServerName_Object=MibScalar
nwSysServerName=_NwSysServerName_Object((1,3,6,1,4,1,23,2,28,1,1),_NwSysServerName_Type())
nwSysServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSysServerName.setStatus(_A)
_NwSysSerialNumber_Type=InternationalDisplayString
_NwSysSerialNumber_Object=MibScalar
nwSysSerialNumber=_NwSysSerialNumber_Object((1,3,6,1,4,1,23,2,28,1,2),_NwSysSerialNumber_Type())
nwSysSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSysSerialNumber.setStatus(_A)
_NwSysInternalNetNum_Type=IPXNetNumber
_NwSysInternalNetNum_Object=MibScalar
nwSysInternalNetNum=_NwSysInternalNetNum_Object((1,3,6,1,4,1,23,2,28,1,3),_NwSysInternalNetNum_Type())
nwSysInternalNetNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSysInternalNetNum.setStatus(_A)
_NwSysServerUpTime_Type=TimeTicks
_NwSysServerUpTime_Object=MibScalar
nwSysServerUpTime=_NwSysServerUpTime_Object((1,3,6,1,4,1,23,2,28,1,4),_NwSysServerUpTime_Type())
nwSysServerUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSysServerUpTime.setStatus(_A)
class _NwSysOSSFTLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('sftI',2),('sftII',3),('sftIII',4)))
_NwSysOSSFTLevel_Type.__name__=_C
_NwSysOSSFTLevel_Object=MibScalar
nwSysOSSFTLevel=_NwSysOSSFTLevel_Object((1,3,6,1,4,1,23,2,28,1,5),_NwSysOSSFTLevel_Type())
nwSysOSSFTLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSysOSSFTLevel.setStatus(_A)
_NwSysOSMajorVer_Type=Integer32
_NwSysOSMajorVer_Object=MibScalar
nwSysOSMajorVer=_NwSysOSMajorVer_Object((1,3,6,1,4,1,23,2,28,1,6),_NwSysOSMajorVer_Type())
nwSysOSMajorVer.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSysOSMajorVer.setStatus(_A)
_NwSysOSMinorVer_Type=Integer32
_NwSysOSMinorVer_Object=MibScalar
nwSysOSMinorVer=_NwSysOSMinorVer_Object((1,3,6,1,4,1,23,2,28,1,7),_NwSysOSMinorVer_Type())
nwSysOSMinorVer.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSysOSMinorVer.setStatus(_A)
_NwSysOSReleaseDate_Type=DateAndTime
_NwSysOSReleaseDate_Object=MibScalar
nwSysOSReleaseDate=_NwSysOSReleaseDate_Object((1,3,6,1,4,1,23,2,28,1,8),_NwSysOSReleaseDate_Type())
nwSysOSReleaseDate.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSysOSReleaseDate.setStatus(_A)
class _NwSysOSDescription_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NwSysOSDescription_Type.__name__=_E
_NwSysOSDescription_Object=MibScalar
nwSysOSDescription=_NwSysOSDescription_Object((1,3,6,1,4,1,23,2,28,1,9),_NwSysOSDescription_Type())
nwSysOSDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSysOSDescription.setStatus(_A)
_NwSysOSCopyright_Type=InternationalDisplayString
_NwSysOSCopyright_Object=MibScalar
nwSysOSCopyright=_NwSysOSCopyright_Object((1,3,6,1,4,1,23,2,28,1,10),_NwSysOSCopyright_Type())
nwSysOSCopyright.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSysOSCopyright.setStatus(_A)
_NwSysTime_Type=DateAndTime
_NwSysTime_Object=MibScalar
nwSysTime=_NwSysTime_Object((1,3,6,1,4,1,23,2,28,1,11),_NwSysTime_Type())
nwSysTime.setMaxAccess(_F)
if mibBuilder.loadTexts:nwSysTime.setStatus(_A)
class _NwSysTimeZone_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_NwSysTimeZone_Type.__name__=_E
_NwSysTimeZone_Object=MibScalar
nwSysTimeZone=_NwSysTimeZone_Object((1,3,6,1,4,1,23,2,28,1,12),_NwSysTimeZone_Type())
nwSysTimeZone.setMaxAccess(_F)
if mibBuilder.loadTexts:nwSysTimeZone.setStatus(_A)
class _NwSysLoginState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notApplicable',1),(_I,2),(_J,3)))
_NwSysLoginState_Type.__name__=_C
_NwSysLoginState_Object=MibScalar
nwSysLoginState=_NwSysLoginState_Object((1,3,6,1,4,1,23,2,28,1,13),_NwSysLoginState_Type())
nwSysLoginState.setMaxAccess(_F)
if mibBuilder.loadTexts:nwSysLoginState.setStatus(_A)
class _NwSysLanguageID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,14,15,16,17)));namedValues=NamedValues(*((_G,1),('canadianFrench',2),('chinese',3),('danish',4),('dutch',5),('english',6),('finnish',7),('french',8),('german',9),('italian',10),('japanese',11),('portuguese',14),('russian',15),('spanish',16),('swedish',17)))
_NwSysLanguageID_Type.__name__=_C
_NwSysLanguageID_Object=MibScalar
nwSysLanguageID=_NwSysLanguageID_Object((1,3,6,1,4,1,23,2,28,1,14),_NwSysLanguageID_Type())
nwSysLanguageID.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSysLanguageID.setStatus(_A)
_NwSysNMASerialNumber_Type=InternationalDisplayString
_NwSysNMASerialNumber_Object=MibScalar
nwSysNMASerialNumber=_NwSysNMASerialNumber_Object((1,3,6,1,4,1,23,2,28,1,15),_NwSysNMASerialNumber_Type())
nwSysNMASerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSysNMASerialNumber.setStatus(_A)
_NwSysNMACopiesAllowed_Type=Integer32
_NwSysNMACopiesAllowed_Object=MibScalar
nwSysNMACopiesAllowed=_NwSysNMACopiesAllowed_Object((1,3,6,1,4,1,23,2,28,1,16),_NwSysNMACopiesAllowed_Type())
nwSysNMACopiesAllowed.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSysNMACopiesAllowed.setStatus(_A)
_NwSysDirectoryTree_Type=InternationalDisplayString
_NwSysDirectoryTree_Object=MibScalar
nwSysDirectoryTree=_NwSysDirectoryTree_Object((1,3,6,1,4,1,23,2,28,1,17),_NwSysDirectoryTree_Type())
nwSysDirectoryTree.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSysDirectoryTree.setStatus(_A)
_NwSysBinderyContext_Type=InternationalDisplayString
_NwSysBinderyContext_Object=MibScalar
nwSysBinderyContext=_NwSysBinderyContext_Object((1,3,6,1,4,1,23,2,28,1,18),_NwSysBinderyContext_Type())
nwSysBinderyContext.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSysBinderyContext.setStatus(_A)
_NwSysServerDSName_Type=InternationalDisplayString
_NwSysServerDSName_Object=MibScalar
nwSysServerDSName=_NwSysServerDSName_Object((1,3,6,1,4,1,23,2,28,1,19),_NwSysServerDSName_Type())
nwSysServerDSName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSysServerDSName.setStatus(_A)
_NwSysDaylightSavingsStart_Type=DSTType
_NwSysDaylightSavingsStart_Object=MibScalar
nwSysDaylightSavingsStart=_NwSysDaylightSavingsStart_Object((1,3,6,1,4,1,23,2,28,1,20),_NwSysDaylightSavingsStart_Type())
nwSysDaylightSavingsStart.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSysDaylightSavingsStart.setStatus(_A)
_NwSysDaylightSavingsEnd_Type=DSTType
_NwSysDaylightSavingsEnd_Object=MibScalar
nwSysDaylightSavingsEnd=_NwSysDaylightSavingsEnd_Object((1,3,6,1,4,1,23,2,28,1,21),_NwSysDaylightSavingsEnd_Type())
nwSysDaylightSavingsEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSysDaylightSavingsEnd.setStatus(_A)
_NwSysDaylightSavingsOffset_Type=Integer32
_NwSysDaylightSavingsOffset_Object=MibScalar
nwSysDaylightSavingsOffset=_NwSysDaylightSavingsOffset_Object((1,3,6,1,4,1,23,2,28,1,22),_NwSysDaylightSavingsOffset_Type())
nwSysDaylightSavingsOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSysDaylightSavingsOffset.setStatus(_A)
class _NwSysDaylightSavingsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_NwSysDaylightSavingsStatus_Type.__name__=_C
_NwSysDaylightSavingsStatus_Object=MibScalar
nwSysDaylightSavingsStatus=_NwSysDaylightSavingsStatus_Object((1,3,6,1,4,1,23,2,28,1,23),_NwSysDaylightSavingsStatus_Type())
nwSysDaylightSavingsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSysDaylightSavingsStatus.setStatus(_A)
_NwFileSystem_ObjectIdentity=ObjectIdentity
nwFileSystem=_NwFileSystem_ObjectIdentity((1,3,6,1,4,1,23,2,28,2))
_NwFSReads_Type=Counter32
_NwFSReads_Object=MibScalar
nwFSReads=_NwFSReads_Object((1,3,6,1,4,1,23,2,28,2,1),_NwFSReads_Type())
nwFSReads.setMaxAccess(_B)
if mibBuilder.loadTexts:nwFSReads.setStatus(_A)
_NwFSWrites_Type=Counter32
_NwFSWrites_Object=MibScalar
nwFSWrites=_NwFSWrites_Object((1,3,6,1,4,1,23,2,28,2,2),_NwFSWrites_Type())
nwFSWrites.setMaxAccess(_B)
if mibBuilder.loadTexts:nwFSWrites.setStatus(_A)
_NwFSReadKBytes_Type=Counter32
_NwFSReadKBytes_Object=MibScalar
nwFSReadKBytes=_NwFSReadKBytes_Object((1,3,6,1,4,1,23,2,28,2,3),_NwFSReadKBytes_Type())
nwFSReadKBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwFSReadKBytes.setStatus(_A)
_NwFSWrittenKBytes_Type=Counter32
_NwFSWrittenKBytes_Object=MibScalar
nwFSWrittenKBytes=_NwFSWrittenKBytes_Object((1,3,6,1,4,1,23,2,28,2,4),_NwFSWrittenKBytes_Type())
nwFSWrittenKBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwFSWrittenKBytes.setStatus(_A)
_NwFSCacheChecks_Type=Counter32
_NwFSCacheChecks_Object=MibScalar
nwFSCacheChecks=_NwFSCacheChecks_Object((1,3,6,1,4,1,23,2,28,2,5),_NwFSCacheChecks_Type())
nwFSCacheChecks.setMaxAccess(_B)
if mibBuilder.loadTexts:nwFSCacheChecks.setStatus(_A)
_NwFSCacheHits_Type=Counter32
_NwFSCacheHits_Object=MibScalar
nwFSCacheHits=_NwFSCacheHits_Object((1,3,6,1,4,1,23,2,28,2,6),_NwFSCacheHits_Type())
nwFSCacheHits.setMaxAccess(_B)
if mibBuilder.loadTexts:nwFSCacheHits.setStatus(_A)
_NwFSOpenFiles_Type=Integer32
_NwFSOpenFiles_Object=MibScalar
nwFSOpenFiles=_NwFSOpenFiles_Object((1,3,6,1,4,1,23,2,28,2,7),_NwFSOpenFiles_Type())
nwFSOpenFiles.setMaxAccess(_B)
if mibBuilder.loadTexts:nwFSOpenFiles.setStatus(_A)
_NwFSMaxOpenFiles_Type=Integer32
_NwFSMaxOpenFiles_Object=MibScalar
nwFSMaxOpenFiles=_NwFSMaxOpenFiles_Object((1,3,6,1,4,1,23,2,28,2,8),_NwFSMaxOpenFiles_Type())
nwFSMaxOpenFiles.setMaxAccess(_B)
if mibBuilder.loadTexts:nwFSMaxOpenFiles.setStatus(_A)
_NwFSRecordLocks_Type=Integer32
_NwFSRecordLocks_Object=MibScalar
nwFSRecordLocks=_NwFSRecordLocks_Object((1,3,6,1,4,1,23,2,28,2,9),_NwFSRecordLocks_Type())
nwFSRecordLocks.setMaxAccess(_B)
if mibBuilder.loadTexts:nwFSRecordLocks.setStatus(_A)
_NwFSMaxRecordLocks_Type=Integer32
_NwFSMaxRecordLocks_Object=MibScalar
nwFSMaxRecordLocks=_NwFSMaxRecordLocks_Object((1,3,6,1,4,1,23,2,28,2,10),_NwFSMaxRecordLocks_Type())
nwFSMaxRecordLocks.setMaxAccess(_B)
if mibBuilder.loadTexts:nwFSMaxRecordLocks.setStatus(_A)
_NwFSMaxSubdirectoryTreeDepth_Type=Integer32
_NwFSMaxSubdirectoryTreeDepth_Object=MibScalar
nwFSMaxSubdirectoryTreeDepth=_NwFSMaxSubdirectoryTreeDepth_Object((1,3,6,1,4,1,23,2,28,2,11),_NwFSMaxSubdirectoryTreeDepth_Type())
nwFSMaxSubdirectoryTreeDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:nwFSMaxSubdirectoryTreeDepth.setStatus(_A)
class _NwFSMaxPercentOfVolumeUsedByDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_NwFSMaxPercentOfVolumeUsedByDir_Type.__name__=_C
_NwFSMaxPercentOfVolumeUsedByDir_Object=MibScalar
nwFSMaxPercentOfVolumeUsedByDir=_NwFSMaxPercentOfVolumeUsedByDir_Object((1,3,6,1,4,1,23,2,28,2,12),_NwFSMaxPercentOfVolumeUsedByDir_Type())
nwFSMaxPercentOfVolumeUsedByDir.setMaxAccess(_B)
if mibBuilder.loadTexts:nwFSMaxPercentOfVolumeUsedByDir.setStatus(_A)
_NwFSVolCount_Type=Integer32
_NwFSVolCount_Object=MibScalar
nwFSVolCount=_NwFSVolCount_Object((1,3,6,1,4,1,23,2,28,2,13),_NwFSVolCount_Type())
nwFSVolCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nwFSVolCount.setStatus(_A)
_NwFSVolTable_Object=MibTable
nwFSVolTable=_NwFSVolTable_Object((1,3,6,1,4,1,23,2,28,2,14))
if mibBuilder.loadTexts:nwFSVolTable.setStatus(_A)
_NwFSVolEntry_Object=MibTableRow
nwFSVolEntry=_NwFSVolEntry_Object((1,3,6,1,4,1,23,2,28,2,14,1))
nwFSVolEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:nwFSVolEntry.setStatus(_A)
class _NwVolID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NwVolID_Type.__name__=_C
_NwVolID_Object=MibTableColumn
nwVolID=_NwVolID_Object((1,3,6,1,4,1,23,2,28,2,14,1,1),_NwVolID_Type())
nwVolID.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolID.setStatus(_A)
class _NwVolPhysicalName_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NwVolPhysicalName_Type.__name__=_E
_NwVolPhysicalName_Object=MibTableColumn
nwVolPhysicalName=_NwVolPhysicalName_Object((1,3,6,1,4,1,23,2,28,2,14,1,2),_NwVolPhysicalName_Type())
nwVolPhysicalName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolPhysicalName.setStatus(_A)
_NwVolSize_Type=KBytes
_NwVolSize_Object=MibTableColumn
nwVolSize=_NwVolSize_Object((1,3,6,1,4,1,23,2,28,2,14,1,3),_NwVolSize_Type())
nwVolSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolSize.setStatus(_A)
_NwVolFree_Type=KBytes
_NwVolFree_Object=MibTableColumn
nwVolFree=_NwVolFree_Object((1,3,6,1,4,1,23,2,28,2,14,1,4),_NwVolFree_Type())
nwVolFree.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolFree.setStatus(_A)
_NwVolFreeable_Type=KBytes
_NwVolFreeable_Object=MibTableColumn
nwVolFreeable=_NwVolFreeable_Object((1,3,6,1,4,1,23,2,28,2,14,1,5),_NwVolFreeable_Type())
nwVolFreeable.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolFreeable.setStatus(_A)
_NwVolNonFreeable_Type=KBytes
_NwVolNonFreeable_Object=MibTableColumn
nwVolNonFreeable=_NwVolNonFreeable_Object((1,3,6,1,4,1,23,2,28,2,14,1,6),_NwVolNonFreeable_Type())
nwVolNonFreeable.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolNonFreeable.setStatus(_A)
_NwVolBlockSize_Type=Integer32
_NwVolBlockSize_Object=MibTableColumn
nwVolBlockSize=_NwVolBlockSize_Object((1,3,6,1,4,1,23,2,28,2,14,1,7),_NwVolBlockSize_Type())
nwVolBlockSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolBlockSize.setStatus(_A)
class _NwVolMounted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mounted',1),('dismounted',2)))
_NwVolMounted_Type.__name__=_C
_NwVolMounted_Object=MibTableColumn
nwVolMounted=_NwVolMounted_Object((1,3,6,1,4,1,23,2,28,2,14,1,8),_NwVolMounted_Type())
nwVolMounted.setMaxAccess(_F)
if mibBuilder.loadTexts:nwVolMounted.setStatus(_A)
class _NwVolAttributes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_NwVolAttributes_Type.__name__=_C
_NwVolAttributes_Object=MibTableColumn
nwVolAttributes=_NwVolAttributes_Object((1,3,6,1,4,1,23,2,28,2,14,1,9),_NwVolAttributes_Type())
nwVolAttributes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolAttributes.setStatus(_A)
class _NwVolNameSpaces_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_NwVolNameSpaces_Type.__name__=_C
_NwVolNameSpaces_Object=MibTableColumn
nwVolNameSpaces=_NwVolNameSpaces_Object((1,3,6,1,4,1,23,2,28,2,14,1,10),_NwVolNameSpaces_Type())
nwVolNameSpaces.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolNameSpaces.setStatus(_A)
_NwVolTotalDirEntries_Type=Integer32
_NwVolTotalDirEntries_Object=MibTableColumn
nwVolTotalDirEntries=_NwVolTotalDirEntries_Object((1,3,6,1,4,1,23,2,28,2,14,1,11),_NwVolTotalDirEntries_Type())
nwVolTotalDirEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolTotalDirEntries.setStatus(_A)
_NwVolUsedDirEntries_Type=Integer32
_NwVolUsedDirEntries_Object=MibTableColumn
nwVolUsedDirEntries=_NwVolUsedDirEntries_Object((1,3,6,1,4,1,23,2,28,2,14,1,12),_NwVolUsedDirEntries_Type())
nwVolUsedDirEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolUsedDirEntries.setStatus(_A)
_NwVolSegmentCount_Type=Integer32
_NwVolSegmentCount_Object=MibTableColumn
nwVolSegmentCount=_NwVolSegmentCount_Object((1,3,6,1,4,1,23,2,28,2,14,1,13),_NwVolSegmentCount_Type())
nwVolSegmentCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolSegmentCount.setStatus(_A)
_NwVolDSName_Type=InternationalDisplayString
_NwVolDSName_Object=MibTableColumn
nwVolDSName=_NwVolDSName_Object((1,3,6,1,4,1,23,2,28,2,14,1,14),_NwVolDSName_Type())
nwVolDSName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolDSName.setStatus(_A)
class _NwVolFileSystemID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),('netWareVolume',3),('nfsVolume',4)))
_NwVolFileSystemID_Type.__name__=_C
_NwVolFileSystemID_Object=MibTableColumn
nwVolFileSystemID=_NwVolFileSystemID_Object((1,3,6,1,4,1,23,2,28,2,14,1,15),_NwVolFileSystemID_Type())
nwVolFileSystemID.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolFileSystemID.setStatus(_A)
_NwVolFileSystemName_Type=InternationalDisplayString
_NwVolFileSystemName_Object=MibTableColumn
nwVolFileSystemName=_NwVolFileSystemName_Object((1,3,6,1,4,1,23,2,28,2,14,1,16),_NwVolFileSystemName_Type())
nwVolFileSystemName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolFileSystemName.setStatus(_A)
_NwFSOpenFileTable_Object=MibTable
nwFSOpenFileTable=_NwFSOpenFileTable_Object((1,3,6,1,4,1,23,2,28,2,15))
if mibBuilder.loadTexts:nwFSOpenFileTable.setStatus(_A)
_NwFSOpenFileEntry_Object=MibTableRow
nwFSOpenFileEntry=_NwFSOpenFileEntry_Object((1,3,6,1,4,1,23,2,28,2,15,1))
nwFSOpenFileEntry.setIndexNames((0,_D,_L),(0,_D,_M),(0,_D,_N))
if mibBuilder.loadTexts:nwFSOpenFileEntry.setStatus(_A)
class _NwOfileVolID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NwOfileVolID_Type.__name__=_C
_NwOfileVolID_Object=MibTableColumn
nwOfileVolID=_NwOfileVolID_Object((1,3,6,1,4,1,23,2,28,2,15,1,1),_NwOfileVolID_Type())
nwOfileVolID.setMaxAccess(_B)
if mibBuilder.loadTexts:nwOfileVolID.setStatus(_A)
_NwOfileDirectoryNumber_Type=Integer32
_NwOfileDirectoryNumber_Object=MibTableColumn
nwOfileDirectoryNumber=_NwOfileDirectoryNumber_Object((1,3,6,1,4,1,23,2,28,2,15,1,2),_NwOfileDirectoryNumber_Type())
nwOfileDirectoryNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nwOfileDirectoryNumber.setStatus(_A)
_NwOfileConnection_Type=Integer32
_NwOfileConnection_Object=MibTableColumn
nwOfileConnection=_NwOfileConnection_Object((1,3,6,1,4,1,23,2,28,2,15,1,3),_NwOfileConnection_Type())
nwOfileConnection.setMaxAccess(_B)
if mibBuilder.loadTexts:nwOfileConnection.setStatus(_A)
class _NwOfileVolumeName_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NwOfileVolumeName_Type.__name__=_E
_NwOfileVolumeName_Object=MibTableColumn
nwOfileVolumeName=_NwOfileVolumeName_Object((1,3,6,1,4,1,23,2,28,2,15,1,4),_NwOfileVolumeName_Type())
nwOfileVolumeName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwOfileVolumeName.setStatus(_A)
class _NwOfileName_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_NwOfileName_Type.__name__=_E
_NwOfileName_Object=MibTableColumn
nwOfileName=_NwOfileName_Object((1,3,6,1,4,1,23,2,28,2,15,1,5),_NwOfileName_Type())
nwOfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwOfileName.setStatus(_A)
_NwOfileLoginName_Type=InternationalDisplayString
_NwOfileLoginName_Object=MibTableColumn
nwOfileLoginName=_NwOfileLoginName_Object((1,3,6,1,4,1,23,2,28,2,15,1,6),_NwOfileLoginName_Type())
nwOfileLoginName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwOfileLoginName.setStatus(_A)
_NwUsers_ObjectIdentity=ObjectIdentity
nwUsers=_NwUsers_ObjectIdentity((1,3,6,1,4,1,23,2,28,3))
_NwUserCount_Type=Integer32
_NwUserCount_Object=MibScalar
nwUserCount=_NwUserCount_Object((1,3,6,1,4,1,23,2,28,3,1),_NwUserCount_Type())
nwUserCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nwUserCount.setStatus(_A)
_NwLoginCount_Type=Integer32
_NwLoginCount_Object=MibScalar
nwLoginCount=_NwLoginCount_Object((1,3,6,1,4,1,23,2,28,3,2),_NwLoginCount_Type())
nwLoginCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nwLoginCount.setStatus(_A)
_NwMaxLogins_Type=Integer32
_NwMaxLogins_Object=MibScalar
nwMaxLogins=_NwMaxLogins_Object((1,3,6,1,4,1,23,2,28,3,3),_NwMaxLogins_Type())
nwMaxLogins.setMaxAccess(_B)
if mibBuilder.loadTexts:nwMaxLogins.setStatus(_A)
_NwConnectionCount_Type=Integer32
_NwConnectionCount_Object=MibScalar
nwConnectionCount=_NwConnectionCount_Object((1,3,6,1,4,1,23,2,28,3,4),_NwConnectionCount_Type())
nwConnectionCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nwConnectionCount.setStatus(_A)
_NwPeakRemoteConnections_Type=Integer32
_NwPeakRemoteConnections_Object=MibScalar
nwPeakRemoteConnections=_NwPeakRemoteConnections_Object((1,3,6,1,4,1,23,2,28,3,5),_NwPeakRemoteConnections_Type())
nwPeakRemoteConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:nwPeakRemoteConnections.setStatus(_A)
_NwMaxConnections_Type=Integer32
_NwMaxConnections_Object=MibScalar
nwMaxConnections=_NwMaxConnections_Object((1,3,6,1,4,1,23,2,28,3,6),_NwMaxConnections_Type())
nwMaxConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:nwMaxConnections.setStatus(_A)
_NwNLMConnections_Type=Integer32
_NwNLMConnections_Object=MibScalar
nwNLMConnections=_NwNLMConnections_Object((1,3,6,1,4,1,23,2,28,3,7),_NwNLMConnections_Type())
nwNLMConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNLMConnections.setStatus(_A)
_NwConnectionTable_Object=MibTable
nwConnectionTable=_NwConnectionTable_Object((1,3,6,1,4,1,23,2,28,3,8))
if mibBuilder.loadTexts:nwConnectionTable.setStatus(_A)
_NwConnectionEntry_Object=MibTableRow
nwConnectionEntry=_NwConnectionEntry_Object((1,3,6,1,4,1,23,2,28,3,8,1))
nwConnectionEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:nwConnectionEntry.setStatus(_A)
_NwConnectionNumber_Type=Integer32
_NwConnectionNumber_Object=MibTableColumn
nwConnectionNumber=_NwConnectionNumber_Object((1,3,6,1,4,1,23,2,28,3,8,1,1),_NwConnectionNumber_Type())
nwConnectionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nwConnectionNumber.setStatus(_A)
_NwConnectionLoginName_Type=InternationalDisplayString
_NwConnectionLoginName_Object=MibTableColumn
nwConnectionLoginName=_NwConnectionLoginName_Object((1,3,6,1,4,1,23,2,28,3,8,1,2),_NwConnectionLoginName_Type())
nwConnectionLoginName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwConnectionLoginName.setStatus(_A)
_NwConnectionTransportDomain_Type=TransportDomain
_NwConnectionTransportDomain_Object=MibTableColumn
nwConnectionTransportDomain=_NwConnectionTransportDomain_Object((1,3,6,1,4,1,23,2,28,3,8,1,3),_NwConnectionTransportDomain_Type())
nwConnectionTransportDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:nwConnectionTransportDomain.setStatus(_A)
_NwConnectionTransportAddress_Type=TransportAddress
_NwConnectionTransportAddress_Object=MibTableColumn
nwConnectionTransportAddress=_NwConnectionTransportAddress_Object((1,3,6,1,4,1,23,2,28,3,8,1,4),_NwConnectionTransportAddress_Type())
nwConnectionTransportAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nwConnectionTransportAddress.setStatus(_A)
_NwConnectionTime_Type=DateAndTime
_NwConnectionTime_Object=MibTableColumn
nwConnectionTime=_NwConnectionTime_Object((1,3,6,1,4,1,23,2,28,3,8,1,5),_NwConnectionTime_Type())
nwConnectionTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwConnectionTime.setStatus(_A)
_NwConnectionReadKBytes_Type=Counter32
_NwConnectionReadKBytes_Object=MibTableColumn
nwConnectionReadKBytes=_NwConnectionReadKBytes_Object((1,3,6,1,4,1,23,2,28,3,8,1,6),_NwConnectionReadKBytes_Type())
nwConnectionReadKBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwConnectionReadKBytes.setStatus(_A)
_NwConnectionWrittenKBytes_Type=Counter32
_NwConnectionWrittenKBytes_Object=MibTableColumn
nwConnectionWrittenKBytes=_NwConnectionWrittenKBytes_Object((1,3,6,1,4,1,23,2,28,3,8,1,7),_NwConnectionWrittenKBytes_Type())
nwConnectionWrittenKBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:nwConnectionWrittenKBytes.setStatus(_A)
_NwConnectionNcpRequests_Type=Counter32
_NwConnectionNcpRequests_Object=MibTableColumn
nwConnectionNcpRequests=_NwConnectionNcpRequests_Object((1,3,6,1,4,1,23,2,28,3,8,1,8),_NwConnectionNcpRequests_Type())
nwConnectionNcpRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:nwConnectionNcpRequests.setStatus(_A)
_NwConnectionFilesOpen_Type=Integer32
_NwConnectionFilesOpen_Object=MibTableColumn
nwConnectionFilesOpen=_NwConnectionFilesOpen_Object((1,3,6,1,4,1,23,2,28,3,8,1,9),_NwConnectionFilesOpen_Type())
nwConnectionFilesOpen.setMaxAccess(_B)
if mibBuilder.loadTexts:nwConnectionFilesOpen.setStatus(_A)
_NwConnectionRecordsLocked_Type=Integer32
_NwConnectionRecordsLocked_Object=MibTableColumn
nwConnectionRecordsLocked=_NwConnectionRecordsLocked_Object((1,3,6,1,4,1,23,2,28,3,8,1,10),_NwConnectionRecordsLocked_Type())
nwConnectionRecordsLocked.setMaxAccess(_B)
if mibBuilder.loadTexts:nwConnectionRecordsLocked.setStatus(_A)
class _NwConnectionPrivilege_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_NwConnectionPrivilege_Type.__name__=_C
_NwConnectionPrivilege_Object=MibTableColumn
nwConnectionPrivilege=_NwConnectionPrivilege_Object((1,3,6,1,4,1,23,2,28,3,8,1,11),_NwConnectionPrivilege_Type())
nwConnectionPrivilege.setMaxAccess(_B)
if mibBuilder.loadTexts:nwConnectionPrivilege.setStatus(_A)
class _NwConnectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_NwConnectionStatus_Type.__name__=_C
_NwConnectionStatus_Object=MibTableColumn
nwConnectionStatus=_NwConnectionStatus_Object((1,3,6,1,4,1,23,2,28,3,8,1,12),_NwConnectionStatus_Type())
nwConnectionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwConnectionStatus.setStatus(_A)
_NwQueue_ObjectIdentity=ObjectIdentity
nwQueue=_NwQueue_ObjectIdentity((1,3,6,1,4,1,23,2,28,4))
_NwQueueCount_Type=Integer32
_NwQueueCount_Object=MibScalar
nwQueueCount=_NwQueueCount_Object((1,3,6,1,4,1,23,2,28,4,1),_NwQueueCount_Type())
nwQueueCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQueueCount.setStatus(_A)
_NwQueueTable_Object=MibTable
nwQueueTable=_NwQueueTable_Object((1,3,6,1,4,1,23,2,28,4,2))
if mibBuilder.loadTexts:nwQueueTable.setStatus(_A)
_NwQueueEntry_Object=MibTableRow
nwQueueEntry=_NwQueueEntry_Object((1,3,6,1,4,1,23,2,28,4,2,1))
nwQueueEntry.setIndexNames((0,_D,'nwQID'))
if mibBuilder.loadTexts:nwQueueEntry.setStatus(_A)
class _NwQID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NwQID_Type.__name__=_C
_NwQID_Object=MibTableColumn
nwQID=_NwQID_Object((1,3,6,1,4,1,23,2,28,4,2,1,1),_NwQID_Type())
nwQID.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQID.setStatus(_A)
_NwQName_Type=InternationalDisplayString
_NwQName_Object=MibTableColumn
nwQName=_NwQName_Object((1,3,6,1,4,1,23,2,28,4,2,1,2),_NwQName_Type())
nwQName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQName.setStatus(_A)
class _NwQType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('printQueue',2),('archiveQueue',3),('jobQueue',4)))
_NwQType_Type.__name__=_C
_NwQType_Object=MibTableColumn
nwQType=_NwQType_Object((1,3,6,1,4,1,23,2,28,4,2,1,3),_NwQType_Type())
nwQType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQType.setStatus(_A)
class _NwQAddJobState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('canAddJobs',1),('cannotAddJobs',2)))
_NwQAddJobState_Type.__name__=_C
_NwQAddJobState_Object=MibTableColumn
nwQAddJobState=_NwQAddJobState_Object((1,3,6,1,4,1,23,2,28,4,2,1,4),_NwQAddJobState_Type())
nwQAddJobState.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQAddJobState.setStatus(_A)
class _NwQAttachState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('canAttach',1),('cannotAttach',2)))
_NwQAttachState_Type.__name__=_C
_NwQAttachState_Object=MibTableColumn
nwQAttachState=_NwQAttachState_Object((1,3,6,1,4,1,23,2,28,4,2,1,5),_NwQAttachState_Type())
nwQAttachState.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQAttachState.setStatus(_A)
class _NwQServiceJobState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('canService',1),('cannotService',2)))
_NwQServiceJobState_Type.__name__=_C
_NwQServiceJobState_Object=MibTableColumn
nwQServiceJobState=_NwQServiceJobState_Object((1,3,6,1,4,1,23,2,28,4,2,1,6),_NwQServiceJobState_Type())
nwQServiceJobState.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQServiceJobState.setStatus(_A)
class _NwQDirVolName_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NwQDirVolName_Type.__name__=_E
_NwQDirVolName_Object=MibTableColumn
nwQDirVolName=_NwQDirVolName_Object((1,3,6,1,4,1,23,2,28,4,2,1,7),_NwQDirVolName_Type())
nwQDirVolName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQDirVolName.setStatus(_A)
_NwQNumJobEntries_Type=Integer32
_NwQNumJobEntries_Object=MibTableColumn
nwQNumJobEntries=_NwQNumJobEntries_Object((1,3,6,1,4,1,23,2,28,4,2,1,8),_NwQNumJobEntries_Type())
nwQNumJobEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQNumJobEntries.setStatus(_A)
_NwQNumAssignedServers_Type=Integer32
_NwQNumAssignedServers_Object=MibTableColumn
nwQNumAssignedServers=_NwQNumAssignedServers_Object((1,3,6,1,4,1,23,2,28,4,2,1,9),_NwQNumAssignedServers_Type())
nwQNumAssignedServers.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQNumAssignedServers.setStatus(_A)
_NwQueueJobTable_Object=MibTable
nwQueueJobTable=_NwQueueJobTable_Object((1,3,6,1,4,1,23,2,28,4,3))
if mibBuilder.loadTexts:nwQueueJobTable.setStatus(_A)
_NwQueueJobEntry_Object=MibTableRow
nwQueueJobEntry=_NwQueueJobEntry_Object((1,3,6,1,4,1,23,2,28,4,3,1))
nwQueueJobEntry.setIndexNames((0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:nwQueueJobEntry.setStatus(_A)
class _NwQJobQID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NwQJobQID_Type.__name__=_C
_NwQJobQID_Object=MibTableColumn
nwQJobQID=_NwQJobQID_Object((1,3,6,1,4,1,23,2,28,4,3,1,1),_NwQJobQID_Type())
nwQJobQID.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQJobQID.setStatus(_A)
_NwQJobNumber_Type=Integer32
_NwQJobNumber_Object=MibTableColumn
nwQJobNumber=_NwQJobNumber_Object((1,3,6,1,4,1,23,2,28,4,3,1,2),_NwQJobNumber_Type())
nwQJobNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQJobNumber.setStatus(_A)
class _NwQJobDescription_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NwQJobDescription_Type.__name__=_E
_NwQJobDescription_Object=MibTableColumn
nwQJobDescription=_NwQJobDescription_Object((1,3,6,1,4,1,23,2,28,4,3,1,3),_NwQJobDescription_Type())
nwQJobDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQJobDescription.setStatus(_A)
_NwQJobEntryDateTime_Type=DateAndTime
_NwQJobEntryDateTime_Object=MibTableColumn
nwQJobEntryDateTime=_NwQJobEntryDateTime_Object((1,3,6,1,4,1,23,2,28,4,3,1,4),_NwQJobEntryDateTime_Type())
nwQJobEntryDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQJobEntryDateTime.setStatus(_A)
_NwQJobPosition_Type=Integer32
_NwQJobPosition_Object=MibTableColumn
nwQJobPosition=_NwQJobPosition_Object((1,3,6,1,4,1,23,2,28,4,3,1,5),_NwQJobPosition_Type())
nwQJobPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQJobPosition.setStatus(_A)
_NwQJobSize_Type=Integer32
_NwQJobSize_Object=MibTableColumn
nwQJobSize=_NwQJobSize_Object((1,3,6,1,4,1,23,2,28,4,3,1,6),_NwQJobSize_Type())
nwQJobSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQJobSize.setStatus(_A)
_NwQJobControlFlags_Type=Integer32
_NwQJobControlFlags_Object=MibTableColumn
nwQJobControlFlags=_NwQJobControlFlags_Object((1,3,6,1,4,1,23,2,28,4,3,1,7),_NwQJobControlFlags_Type())
nwQJobControlFlags.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQJobControlFlags.setStatus(_A)
_NwQJobUserName_Type=InternationalDisplayString
_NwQJobUserName_Object=MibTableColumn
nwQJobUserName=_NwQJobUserName_Object((1,3,6,1,4,1,23,2,28,4,3,1,8),_NwQJobUserName_Type())
nwQJobUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQJobUserName.setStatus(_A)
_NwQJobTargetServerName_Type=InternationalDisplayString
_NwQJobTargetServerName_Object=MibTableColumn
nwQJobTargetServerName=_NwQJobTargetServerName_Object((1,3,6,1,4,1,23,2,28,4,3,1,9),_NwQJobTargetServerName_Type())
nwQJobTargetServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQJobTargetServerName.setStatus(_A)
_NwQJobTargetDateTime_Type=DateAndTime
_NwQJobTargetDateTime_Object=MibTableColumn
nwQJobTargetDateTime=_NwQJobTargetDateTime_Object((1,3,6,1,4,1,23,2,28,4,3,1,10),_NwQJobTargetDateTime_Type())
nwQJobTargetDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQJobTargetDateTime.setStatus(_A)
_NwQJobServerName_Type=InternationalDisplayString
_NwQJobServerName_Object=MibTableColumn
nwQJobServerName=_NwQJobServerName_Object((1,3,6,1,4,1,23,2,28,4,3,1,11),_NwQJobServerName_Type())
nwQJobServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQJobServerName.setStatus(_A)
_NwQueueServerTable_Object=MibTable
nwQueueServerTable=_NwQueueServerTable_Object((1,3,6,1,4,1,23,2,28,4,4))
if mibBuilder.loadTexts:nwQueueServerTable.setStatus(_A)
_NwQueueServerEntry_Object=MibTableRow
nwQueueServerEntry=_NwQueueServerEntry_Object((1,3,6,1,4,1,23,2,28,4,4,1))
nwQueueServerEntry.setIndexNames((0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:nwQueueServerEntry.setStatus(_A)
class _NwQServerQID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NwQServerQID_Type.__name__=_C
_NwQServerQID_Object=MibTableColumn
nwQServerQID=_NwQServerQID_Object((1,3,6,1,4,1,23,2,28,4,4,1,1),_NwQServerQID_Type())
nwQServerQID.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQServerQID.setStatus(_A)
class _NwQServerID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NwQServerID_Type.__name__=_C
_NwQServerID_Object=MibTableColumn
nwQServerID=_NwQServerID_Object((1,3,6,1,4,1,23,2,28,4,4,1,2),_NwQServerID_Type())
nwQServerID.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQServerID.setStatus(_A)
_NwQServerName_Type=InternationalDisplayString
_NwQServerName_Object=MibTableColumn
nwQServerName=_NwQServerName_Object((1,3,6,1,4,1,23,2,28,4,4,1,3),_NwQServerName_Type())
nwQServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQServerName.setStatus(_A)
class _NwQServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('active',2),('inactive',3)))
_NwQServerStatus_Type.__name__=_C
_NwQServerStatus_Object=MibTableColumn
nwQServerStatus=_NwQServerStatus_Object((1,3,6,1,4,1,23,2,28,4,4,1,4),_NwQServerStatus_Type())
nwQServerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwQServerStatus.setStatus(_A)
_NwOdi_ObjectIdentity=ObjectIdentity
nwOdi=_NwOdi_ObjectIdentity((1,3,6,1,4,1,23,2,28,5))
_NwOdiLslEnqSendCount_Type=Integer32
_NwOdiLslEnqSendCount_Object=MibScalar
nwOdiLslEnqSendCount=_NwOdiLslEnqSendCount_Object((1,3,6,1,4,1,23,2,28,5,1),_NwOdiLslEnqSendCount_Type())
nwOdiLslEnqSendCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nwOdiLslEnqSendCount.setStatus(_A)
_NwOdiOsPktRcvBuffer_Type=Integer32
_NwOdiOsPktRcvBuffer_Object=MibScalar
nwOdiOsPktRcvBuffer=_NwOdiOsPktRcvBuffer_Object((1,3,6,1,4,1,23,2,28,5,2),_NwOdiOsPktRcvBuffer_Type())
nwOdiOsPktRcvBuffer.setMaxAccess(_B)
if mibBuilder.loadTexts:nwOdiOsPktRcvBuffer.setStatus(_A)
_NwOdiOsMaxPktRcvBuffers_Type=Integer32
_NwOdiOsMaxPktRcvBuffers_Object=MibScalar
nwOdiOsMaxPktRcvBuffers=_NwOdiOsMaxPktRcvBuffers_Object((1,3,6,1,4,1,23,2,28,5,3),_NwOdiOsMaxPktRcvBuffers_Type())
nwOdiOsMaxPktRcvBuffers.setMaxAccess(_F)
if mibBuilder.loadTexts:nwOdiOsMaxPktRcvBuffers.setStatus(_A)
_NwOdiOsMinPktRcvBuffers_Type=Integer32
_NwOdiOsMinPktRcvBuffers_Object=MibScalar
nwOdiOsMinPktRcvBuffers=_NwOdiOsMinPktRcvBuffers_Object((1,3,6,1,4,1,23,2,28,5,4),_NwOdiOsMinPktRcvBuffers_Type())
nwOdiOsMinPktRcvBuffers.setMaxAccess(_B)
if mibBuilder.loadTexts:nwOdiOsMinPktRcvBuffers.setStatus(_A)
_NwSft3_ObjectIdentity=ObjectIdentity
nwSft3=_NwSft3_ObjectIdentity((1,3,6,1,4,1,23,2,28,6))
_NwSft3Engine_Type=EngineType
_NwSft3Engine_Object=MibScalar
nwSft3Engine=_NwSft3Engine_Object((1,3,6,1,4,1,23,2,28,6,1),_NwSft3Engine_Type())
nwSft3Engine.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSft3Engine.setStatus(_A)
class _NwSft3EngineState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),('synchronizing',2),('mirrored',3),('noSecondary',4),('down',5)))
_NwSft3EngineState_Type.__name__=_C
_NwSft3EngineState_Object=MibScalar
nwSft3EngineState=_NwSft3EngineState_Object((1,3,6,1,4,1,23,2,28,6,2),_NwSft3EngineState_Type())
nwSft3EngineState.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSft3EngineState.setStatus(_A)
_NwSft3EngineTable_Object=MibTable
nwSft3EngineTable=_NwSft3EngineTable_Object((1,3,6,1,4,1,23,2,28,6,3))
if mibBuilder.loadTexts:nwSft3EngineTable.setStatus(_A)
_NwSft3EngineEntry_Object=MibTableRow
nwSft3EngineEntry=_NwSft3EngineEntry_Object((1,3,6,1,4,1,23,2,28,6,3,1))
nwSft3EngineEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:nwSft3EngineEntry.setStatus(_A)
_NwSft3EngineType_Type=EngineType
_NwSft3EngineType_Object=MibTableColumn
nwSft3EngineType=_NwSft3EngineType_Object((1,3,6,1,4,1,23,2,28,6,3,1,1),_NwSft3EngineType_Type())
nwSft3EngineType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSft3EngineType.setStatus(_A)
_NwSft3EngineName_Type=InternationalDisplayString
_NwSft3EngineName_Object=MibTableColumn
nwSft3EngineName=_NwSft3EngineName_Object((1,3,6,1,4,1,23,2,28,6,3,1,2),_NwSft3EngineName_Type())
nwSft3EngineName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSft3EngineName.setStatus(_A)
_NwSft3EngineInternalNetNum_Type=IPXNetNumber
_NwSft3EngineInternalNetNum_Object=MibTableColumn
nwSft3EngineInternalNetNum=_NwSft3EngineInternalNetNum_Object((1,3,6,1,4,1,23,2,28,6,3,1,3),_NwSft3EngineInternalNetNum_Type())
nwSft3EngineInternalNetNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSft3EngineInternalNetNum.setStatus(_A)
_NwNCP_ObjectIdentity=ObjectIdentity
nwNCP=_NwNCP_ObjectIdentity((1,3,6,1,4,1,23,2,28,7))
class _NwNCPIPXChecksums_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noChecksums',1),('checksumIfEnabledAtClient',2),('requireChecksums',3)))
_NwNCPIPXChecksums_Type.__name__=_C
_NwNCPIPXChecksums_Object=MibScalar
nwNCPIPXChecksums=_NwNCPIPXChecksums_Object((1,3,6,1,4,1,23,2,28,7,1),_NwNCPIPXChecksums_Type())
nwNCPIPXChecksums.setMaxAccess(_F)
if mibBuilder.loadTexts:nwNCPIPXChecksums.setStatus(_A)
class _NwNCPPacketSignatures_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('serverNeverSigns',1),('serverSignsOnClientRequest',2),('serverSignsIfClientCapable',3),('serverMandatesSigning',4)))
_NwNCPPacketSignatures_Type.__name__=_C
_NwNCPPacketSignatures_Object=MibScalar
nwNCPPacketSignatures=_NwNCPPacketSignatures_Object((1,3,6,1,4,1,23,2,28,7,2),_NwNCPPacketSignatures_Type())
nwNCPPacketSignatures.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNCPPacketSignatures.setStatus(_A)
_NwNCPNumNCPReqs_Type=Counter32
_NwNCPNumNCPReqs_Object=MibScalar
nwNCPNumNCPReqs=_NwNCPNumNCPReqs_Object((1,3,6,1,4,1,23,2,28,7,3),_NwNCPNumNCPReqs_Type())
nwNCPNumNCPReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNCPNumNCPReqs.setStatus(_A)
_NwNCPUseCount_Type=Integer32
_NwNCPUseCount_Object=MibScalar
nwNCPUseCount=_NwNCPUseCount_Object((1,3,6,1,4,1,23,2,28,7,4),_NwNCPUseCount_Type())
nwNCPUseCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNCPUseCount.setStatus(_A)
_NwNCPPeakUseCount_Type=Integer32
_NwNCPPeakUseCount_Object=MibScalar
nwNCPPeakUseCount=_NwNCPPeakUseCount_Object((1,3,6,1,4,1,23,2,28,7,5),_NwNCPPeakUseCount_Type())
nwNCPPeakUseCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNCPPeakUseCount.setStatus(_A)
_NwNCPForgedPkts_Type=Counter32
_NwNCPForgedPkts_Object=MibScalar
nwNCPForgedPkts=_NwNCPForgedPkts_Object((1,3,6,1,4,1,23,2,28,7,6),_NwNCPForgedPkts_Type())
nwNCPForgedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNCPForgedPkts.setStatus(_A)
_NwNCPBeingProcesseds_Type=Counter32
_NwNCPBeingProcesseds_Object=MibScalar
nwNCPBeingProcesseds=_NwNCPBeingProcesseds_Object((1,3,6,1,4,1,23,2,28,7,7),_NwNCPBeingProcesseds_Type())
nwNCPBeingProcesseds.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNCPBeingProcesseds.setStatus(_A)
_NwNCPNoAvailConns_Type=Counter32
_NwNCPNoAvailConns_Object=MibScalar
nwNCPNoAvailConns=_NwNCPNoAvailConns_Object((1,3,6,1,4,1,23,2,28,7,8),_NwNCPNoAvailConns_Type())
nwNCPNoAvailConns.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNCPNoAvailConns.setStatus(_A)
_NwNCPIPXChecksumErrs_Type=Counter32
_NwNCPIPXChecksumErrs_Object=MibScalar
nwNCPIPXChecksumErrs=_NwNCPIPXChecksumErrs_Object((1,3,6,1,4,1,23,2,28,7,9),_NwNCPIPXChecksumErrs_Type())
nwNCPIPXChecksumErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNCPIPXChecksumErrs.setStatus(_A)
_NwNCPInvalidPacketSigs_Type=Counter32
_NwNCPInvalidPacketSigs_Object=MibScalar
nwNCPInvalidPacketSigs=_NwNCPInvalidPacketSigs_Object((1,3,6,1,4,1,23,2,28,7,10),_NwNCPInvalidPacketSigs_Type())
nwNCPInvalidPacketSigs.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNCPInvalidPacketSigs.setStatus(_A)
_NwNCPExtNumReg_Type=Integer32
_NwNCPExtNumReg_Object=MibScalar
nwNCPExtNumReg=_NwNCPExtNumReg_Object((1,3,6,1,4,1,23,2,28,7,11),_NwNCPExtNumReg_Type())
nwNCPExtNumReg.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNCPExtNumReg.setStatus(_A)
_NwNCPExtInvalidReqs_Type=Counter32
_NwNCPExtInvalidReqs_Object=MibScalar
nwNCPExtInvalidReqs=_NwNCPExtInvalidReqs_Object((1,3,6,1,4,1,23,2,28,7,12),_NwNCPExtInvalidReqs_Type())
nwNCPExtInvalidReqs.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNCPExtInvalidReqs.setStatus(_A)
_NwWatchdog_ObjectIdentity=ObjectIdentity
nwWatchdog=_NwWatchdog_ObjectIdentity((1,3,6,1,4,1,23,2,28,8))
_NwWDTimeBeforeFirstPkt_Type=Integer32
_NwWDTimeBeforeFirstPkt_Object=MibScalar
nwWDTimeBeforeFirstPkt=_NwWDTimeBeforeFirstPkt_Object((1,3,6,1,4,1,23,2,28,8,1),_NwWDTimeBeforeFirstPkt_Type())
nwWDTimeBeforeFirstPkt.setMaxAccess(_F)
if mibBuilder.loadTexts:nwWDTimeBeforeFirstPkt.setStatus(_A)
_NwWDTimeBetweenPkts_Type=Seconds
_NwWDTimeBetweenPkts_Object=MibScalar
nwWDTimeBetweenPkts=_NwWDTimeBetweenPkts_Object((1,3,6,1,4,1,23,2,28,8,2),_NwWDTimeBetweenPkts_Type())
nwWDTimeBetweenPkts.setMaxAccess(_F)
if mibBuilder.loadTexts:nwWDTimeBetweenPkts.setStatus(_A)
_NwWDNumPktsToSend_Type=Integer32
_NwWDNumPktsToSend_Object=MibScalar
nwWDNumPktsToSend=_NwWDNumPktsToSend_Object((1,3,6,1,4,1,23,2,28,8,3),_NwWDNumPktsToSend_Type())
nwWDNumPktsToSend.setMaxAccess(_F)
if mibBuilder.loadTexts:nwWDNumPktsToSend.setStatus(_A)
class _NwWDCurrentState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('waiting',2),('sendingPackets',3),('clearingStations',4)))
_NwWDCurrentState_Type.__name__=_C
_NwWDCurrentState_Object=MibScalar
nwWDCurrentState=_NwWDCurrentState_Object((1,3,6,1,4,1,23,2,28,8,4),_NwWDCurrentState_Type())
nwWDCurrentState.setMaxAccess(_B)
if mibBuilder.loadTexts:nwWDCurrentState.setStatus(_A)
class _NwWDNotifyConsoleFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('doNotNotify',1),('notify',2)))
_NwWDNotifyConsoleFlag_Type.__name__=_C
_NwWDNotifyConsoleFlag_Object=MibScalar
nwWDNotifyConsoleFlag=_NwWDNotifyConsoleFlag_Object((1,3,6,1,4,1,23,2,28,8,5),_NwWDNotifyConsoleFlag_Type())
nwWDNotifyConsoleFlag.setMaxAccess(_F)
if mibBuilder.loadTexts:nwWDNotifyConsoleFlag.setStatus(_A)
_NwNLM_ObjectIdentity=ObjectIdentity
nwNLM=_NwNLM_ObjectIdentity((1,3,6,1,4,1,23,2,28,9))
_NwNLMTable_Object=MibTable
nwNLMTable=_NwNLMTable_Object((1,3,6,1,4,1,23,2,28,9,1))
if mibBuilder.loadTexts:nwNLMTable.setStatus(_A)
_NwNLMEntry_Object=MibTableRow
nwNLMEntry=_NwNLMEntry_Object((1,3,6,1,4,1,23,2,28,9,1,1))
nwNLMEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:nwNLMEntry.setStatus(_A)
class _NwNLMIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NwNLMIndex_Type.__name__=_C
_NwNLMIndex_Object=MibTableColumn
nwNLMIndex=_NwNLMIndex_Object((1,3,6,1,4,1,23,2,28,9,1,1,1),_NwNLMIndex_Type())
nwNLMIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNLMIndex.setStatus(_A)
class _NwNLMName_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_NwNLMName_Type.__name__=_E
_NwNLMName_Object=MibTableColumn
nwNLMName=_NwNLMName_Object((1,3,6,1,4,1,23,2,28,9,1,1,2),_NwNLMName_Type())
nwNLMName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNLMName.setStatus(_A)
class _NwNLMDescription_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_NwNLMDescription_Type.__name__=_E
_NwNLMDescription_Object=MibTableColumn
nwNLMDescription=_NwNLMDescription_Object((1,3,6,1,4,1,23,2,28,9,1,1,3),_NwNLMDescription_Type())
nwNLMDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNLMDescription.setStatus(_A)
_NwNLMTotalMemory_Type=Integer32
_NwNLMTotalMemory_Object=MibTableColumn
nwNLMTotalMemory=_NwNLMTotalMemory_Object((1,3,6,1,4,1,23,2,28,9,1,1,4),_NwNLMTotalMemory_Type())
nwNLMTotalMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNLMTotalMemory.setStatus(_A)
_NwNLMCopyright_Type=InternationalDisplayString
_NwNLMCopyright_Object=MibTableColumn
nwNLMCopyright=_NwNLMCopyright_Object((1,3,6,1,4,1,23,2,28,9,1,1,5),_NwNLMCopyright_Type())
nwNLMCopyright.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNLMCopyright.setStatus(_A)
class _NwNLMProtectionDomain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('osDomain',1),('protectedDomain',2)))
_NwNLMProtectionDomain_Type.__name__=_C
_NwNLMProtectionDomain_Object=MibTableColumn
nwNLMProtectionDomain=_NwNLMProtectionDomain_Object((1,3,6,1,4,1,23,2,28,9,1,1,6),_NwNLMProtectionDomain_Type())
nwNLMProtectionDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNLMProtectionDomain.setStatus(_A)
_NwNLMMajorVer_Type=Integer32
_NwNLMMajorVer_Object=MibTableColumn
nwNLMMajorVer=_NwNLMMajorVer_Object((1,3,6,1,4,1,23,2,28,9,1,1,7),_NwNLMMajorVer_Type())
nwNLMMajorVer.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNLMMajorVer.setStatus(_A)
_NwNLMMinorVer_Type=Integer32
_NwNLMMinorVer_Object=MibTableColumn
nwNLMMinorVer=_NwNLMMinorVer_Object((1,3,6,1,4,1,23,2,28,9,1,1,8),_NwNLMMinorVer_Type())
nwNLMMinorVer.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNLMMinorVer.setStatus(_A)
_NwNLMRevision_Type=Integer32
_NwNLMRevision_Object=MibTableColumn
nwNLMRevision=_NwNLMRevision_Object((1,3,6,1,4,1,23,2,28,9,1,1,9),_NwNLMRevision_Type())
nwNLMRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNLMRevision.setStatus(_A)
_NwNLMReleaseDate_Type=DateAndTime
_NwNLMReleaseDate_Object=MibTableColumn
nwNLMReleaseDate=_NwNLMReleaseDate_Object((1,3,6,1,4,1,23,2,28,9,1,1,10),_NwNLMReleaseDate_Type())
nwNLMReleaseDate.setMaxAccess(_B)
if mibBuilder.loadTexts:nwNLMReleaseDate.setStatus(_A)
_NwSetParams_ObjectIdentity=ObjectIdentity
nwSetParams=_NwSetParams_ObjectIdentity((1,3,6,1,4,1,23,2,28,10))
_NwSetCategoryTable_Object=MibTable
nwSetCategoryTable=_NwSetCategoryTable_Object((1,3,6,1,4,1,23,2,28,10,1))
if mibBuilder.loadTexts:nwSetCategoryTable.setStatus(_A)
_NwSetCategoryEntry_Object=MibTableRow
nwSetCategoryEntry=_NwSetCategoryEntry_Object((1,3,6,1,4,1,23,2,28,10,1,1))
nwSetCategoryEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:nwSetCategoryEntry.setStatus(_A)
class _NwSetCategoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NwSetCategoryIndex_Type.__name__=_C
_NwSetCategoryIndex_Object=MibTableColumn
nwSetCategoryIndex=_NwSetCategoryIndex_Object((1,3,6,1,4,1,23,2,28,10,1,1,1),_NwSetCategoryIndex_Type())
nwSetCategoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSetCategoryIndex.setStatus(_A)
_NwSetCategoryName_Type=InternationalDisplayString
_NwSetCategoryName_Object=MibTableColumn
nwSetCategoryName=_NwSetCategoryName_Object((1,3,6,1,4,1,23,2,28,10,1,1,2),_NwSetCategoryName_Type())
nwSetCategoryName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSetCategoryName.setStatus(_A)
_NwSetParamTable_Object=MibTable
nwSetParamTable=_NwSetParamTable_Object((1,3,6,1,4,1,23,2,28,10,2))
if mibBuilder.loadTexts:nwSetParamTable.setStatus(_A)
_NwSetParamEntry_Object=MibTableRow
nwSetParamEntry=_NwSetParamEntry_Object((1,3,6,1,4,1,23,2,28,10,2,1))
nwSetParamEntry.setIndexNames((0,_D,_W),(0,_D,_X))
if mibBuilder.loadTexts:nwSetParamEntry.setStatus(_A)
class _NwSetParamCategoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NwSetParamCategoryIndex_Type.__name__=_C
_NwSetParamCategoryIndex_Object=MibTableColumn
nwSetParamCategoryIndex=_NwSetParamCategoryIndex_Object((1,3,6,1,4,1,23,2,28,10,2,1,1),_NwSetParamCategoryIndex_Type())
nwSetParamCategoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSetParamCategoryIndex.setStatus(_A)
class _NwSetParamIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NwSetParamIndex_Type.__name__=_C
_NwSetParamIndex_Object=MibTableColumn
nwSetParamIndex=_NwSetParamIndex_Object((1,3,6,1,4,1,23,2,28,10,2,1,2),_NwSetParamIndex_Type())
nwSetParamIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSetParamIndex.setStatus(_A)
_NwSetParamName_Type=InternationalDisplayString
_NwSetParamName_Object=MibTableColumn
nwSetParamName=_NwSetParamName_Object((1,3,6,1,4,1,23,2,28,10,2,1,3),_NwSetParamName_Type())
nwSetParamName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSetParamName.setStatus(_A)
class _NwSetParamType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('number',1),('boolean',2),('ticks',3),('blockShift',4),('timeOffset',5),('string',6),('trigger',7)))
_NwSetParamType_Type.__name__=_C
_NwSetParamType_Object=MibTableColumn
nwSetParamType=_NwSetParamType_Object((1,3,6,1,4,1,23,2,28,10,2,1,4),_NwSetParamType_Type())
nwSetParamType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSetParamType.setStatus(_A)
_NwSetParamValueInteger_Type=Integer32
_NwSetParamValueInteger_Object=MibTableColumn
nwSetParamValueInteger=_NwSetParamValueInteger_Object((1,3,6,1,4,1,23,2,28,10,2,1,5),_NwSetParamValueInteger_Type())
nwSetParamValueInteger.setMaxAccess(_F)
if mibBuilder.loadTexts:nwSetParamValueInteger.setStatus(_A)
_NwSetParamValueString_Type=InternationalDisplayString
_NwSetParamValueString_Object=MibTableColumn
nwSetParamValueString=_NwSetParamValueString_Object((1,3,6,1,4,1,23,2,28,10,2,1,6),_NwSetParamValueString_Type())
nwSetParamValueString.setMaxAccess(_F)
if mibBuilder.loadTexts:nwSetParamValueString.setStatus(_A)
_NwSetParamLowerLimit_Type=Integer32
_NwSetParamLowerLimit_Object=MibTableColumn
nwSetParamLowerLimit=_NwSetParamLowerLimit_Object((1,3,6,1,4,1,23,2,28,10,2,1,7),_NwSetParamLowerLimit_Type())
nwSetParamLowerLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSetParamLowerLimit.setStatus(_A)
_NwSetParamUpperLimit_Type=Integer32
_NwSetParamUpperLimit_Object=MibTableColumn
nwSetParamUpperLimit=_NwSetParamUpperLimit_Object((1,3,6,1,4,1,23,2,28,10,2,1,8),_NwSetParamUpperLimit_Type())
nwSetParamUpperLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSetParamUpperLimit.setStatus(_A)
_NwSetParamDescrLength_Type=Integer32
_NwSetParamDescrLength_Object=MibTableColumn
nwSetParamDescrLength=_NwSetParamDescrLength_Object((1,3,6,1,4,1,23,2,28,10,2,1,9),_NwSetParamDescrLength_Type())
nwSetParamDescrLength.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSetParamDescrLength.setStatus(_A)
class _NwSetParamMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_NwSetParamMode_Type.__name__=_C
_NwSetParamMode_Object=MibTableColumn
nwSetParamMode=_NwSetParamMode_Object((1,3,6,1,4,1,23,2,28,10,2,1,10),_NwSetParamMode_Type())
nwSetParamMode.setMaxAccess(_F)
if mibBuilder.loadTexts:nwSetParamMode.setStatus(_A)
_NwSetDescrTable_Object=MibTable
nwSetDescrTable=_NwSetDescrTable_Object((1,3,6,1,4,1,23,2,28,10,3))
if mibBuilder.loadTexts:nwSetDescrTable.setStatus(_A)
_NwSetDescrEntry_Object=MibTableRow
nwSetDescrEntry=_NwSetDescrEntry_Object((1,3,6,1,4,1,23,2,28,10,3,1))
nwSetDescrEntry.setIndexNames((0,_D,_Y),(0,_D,_Z),(0,_D,_a))
if mibBuilder.loadTexts:nwSetDescrEntry.setStatus(_A)
class _NwSetDescrCategoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NwSetDescrCategoryIndex_Type.__name__=_C
_NwSetDescrCategoryIndex_Object=MibTableColumn
nwSetDescrCategoryIndex=_NwSetDescrCategoryIndex_Object((1,3,6,1,4,1,23,2,28,10,3,1,1),_NwSetDescrCategoryIndex_Type())
nwSetDescrCategoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSetDescrCategoryIndex.setStatus(_A)
class _NwSetDescrParamIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NwSetDescrParamIndex_Type.__name__=_C
_NwSetDescrParamIndex_Object=MibTableColumn
nwSetDescrParamIndex=_NwSetDescrParamIndex_Object((1,3,6,1,4,1,23,2,28,10,3,1,2),_NwSetDescrParamIndex_Type())
nwSetDescrParamIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSetDescrParamIndex.setStatus(_A)
class _NwSetDescrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NwSetDescrIndex_Type.__name__=_C
_NwSetDescrIndex_Object=MibTableColumn
nwSetDescrIndex=_NwSetDescrIndex_Object((1,3,6,1,4,1,23,2,28,10,3,1,3),_NwSetDescrIndex_Type())
nwSetDescrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSetDescrIndex.setStatus(_A)
_NwSetDescription_Type=InternationalDisplayString
_NwSetDescription_Object=MibTableColumn
nwSetDescription=_NwSetDescription_Object((1,3,6,1,4,1,23,2,28,10,3,1,4),_NwSetDescription_Type())
nwSetDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:nwSetDescription.setStatus(_A)
_NwUserAccounts_ObjectIdentity=ObjectIdentity
nwUserAccounts=_NwUserAccounts_ObjectIdentity((1,3,6,1,4,1,23,2,28,11))
_NwUserAcctTable_Object=MibTable
nwUserAcctTable=_NwUserAcctTable_Object((1,3,6,1,4,1,23,2,28,11,1))
if mibBuilder.loadTexts:nwUserAcctTable.setStatus(_A)
_NwUserAcctEntry_Object=MibTableRow
nwUserAcctEntry=_NwUserAcctEntry_Object((1,3,6,1,4,1,23,2,28,11,1,1))
nwUserAcctEntry.setIndexNames((0,_D,_b))
if mibBuilder.loadTexts:nwUserAcctEntry.setStatus(_A)
class _NwUserID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NwUserID_Type.__name__=_C
_NwUserID_Object=MibTableColumn
nwUserID=_NwUserID_Object((1,3,6,1,4,1,23,2,28,11,1,1,1),_NwUserID_Type())
nwUserID.setMaxAccess(_B)
if mibBuilder.loadTexts:nwUserID.setStatus(_A)
_NwUserName_Type=InternationalDisplayString
_NwUserName_Object=MibTableColumn
nwUserName=_NwUserName_Object((1,3,6,1,4,1,23,2,28,11,1,1,2),_NwUserName_Type())
nwUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwUserName.setStatus(_A)
_NwUserDiskUsage_Type=KBytes
_NwUserDiskUsage_Object=MibTableColumn
nwUserDiskUsage=_NwUserDiskUsage_Object((1,3,6,1,4,1,23,2,28,11,1,1,3),_NwUserDiskUsage_Type())
nwUserDiskUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:nwUserDiskUsage.setStatus(_A)
_NwUserLastLoginTime_Type=DateAndTime
_NwUserLastLoginTime_Object=MibTableColumn
nwUserLastLoginTime=_NwUserLastLoginTime_Object((1,3,6,1,4,1,23,2,28,11,1,1,4),_NwUserLastLoginTime_Type())
nwUserLastLoginTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nwUserLastLoginTime.setStatus(_A)
class _NwUserAccountStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_c,2)))
_NwUserAccountStatus_Type.__name__=_C
_NwUserAccountStatus_Object=MibTableColumn
nwUserAccountStatus=_NwUserAccountStatus_Object((1,3,6,1,4,1,23,2,28,11,1,1,5),_NwUserAccountStatus_Type())
nwUserAccountStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwUserAccountStatus.setStatus(_A)
class _NwUserPasswordStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_c,2)))
_NwUserPasswordStatus_Type.__name__=_C
_NwUserPasswordStatus_Object=MibTableColumn
nwUserPasswordStatus=_NwUserPasswordStatus_Object((1,3,6,1,4,1,23,2,28,11,1,1,6),_NwUserPasswordStatus_Type())
nwUserPasswordStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nwUserPasswordStatus.setStatus(_A)
_NwUserBadLoginTransport_Type=TransportDomain
_NwUserBadLoginTransport_Object=MibTableColumn
nwUserBadLoginTransport=_NwUserBadLoginTransport_Object((1,3,6,1,4,1,23,2,28,11,1,1,7),_NwUserBadLoginTransport_Type())
nwUserBadLoginTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:nwUserBadLoginTransport.setStatus(_A)
_NwUserBadLoginAddress_Type=TransportAddress
_NwUserBadLoginAddress_Object=MibTableColumn
nwUserBadLoginAddress=_NwUserBadLoginAddress_Object((1,3,6,1,4,1,23,2,28,11,1,1,8),_NwUserBadLoginAddress_Type())
nwUserBadLoginAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nwUserBadLoginAddress.setStatus(_A)
_NwUserBadLoginAttempts_Type=Integer32
_NwUserBadLoginAttempts_Object=MibTableColumn
nwUserBadLoginAttempts=_NwUserBadLoginAttempts_Object((1,3,6,1,4,1,23,2,28,11,1,1,9),_NwUserBadLoginAttempts_Type())
nwUserBadLoginAttempts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwUserBadLoginAttempts.setStatus(_A)
_NwUserFullName_Type=InternationalDisplayString
_NwUserFullName_Object=MibTableColumn
nwUserFullName=_NwUserFullName_Object((1,3,6,1,4,1,23,2,28,11,1,1,10),_NwUserFullName_Type())
nwUserFullName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwUserFullName.setStatus(_A)
_NwUserVolUsageTable_Object=MibTable
nwUserVolUsageTable=_NwUserVolUsageTable_Object((1,3,6,1,4,1,23,2,28,11,2))
if mibBuilder.loadTexts:nwUserVolUsageTable.setStatus(_A)
_NwUserVolUsageEntry_Object=MibTableRow
nwUserVolUsageEntry=_NwUserVolUsageEntry_Object((1,3,6,1,4,1,23,2,28,11,2,1))
nwUserVolUsageEntry.setIndexNames((0,_D,_d),(0,_D,_e))
if mibBuilder.loadTexts:nwUserVolUsageEntry.setStatus(_A)
class _NwUserVolUserID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NwUserVolUserID_Type.__name__=_C
_NwUserVolUserID_Object=MibTableColumn
nwUserVolUserID=_NwUserVolUserID_Object((1,3,6,1,4,1,23,2,28,11,2,1,1),_NwUserVolUserID_Type())
nwUserVolUserID.setMaxAccess(_B)
if mibBuilder.loadTexts:nwUserVolUserID.setStatus(_A)
class _NwUserVolVolID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NwUserVolVolID_Type.__name__=_C
_NwUserVolVolID_Object=MibTableColumn
nwUserVolVolID=_NwUserVolVolID_Object((1,3,6,1,4,1,23,2,28,11,2,1,2),_NwUserVolVolID_Type())
nwUserVolVolID.setMaxAccess(_B)
if mibBuilder.loadTexts:nwUserVolVolID.setStatus(_A)
_NwUserVolUsageUser_Type=InternationalDisplayString
_NwUserVolUsageUser_Object=MibTableColumn
nwUserVolUsageUser=_NwUserVolUsageUser_Object((1,3,6,1,4,1,23,2,28,11,2,1,3),_NwUserVolUsageUser_Type())
nwUserVolUsageUser.setMaxAccess(_B)
if mibBuilder.loadTexts:nwUserVolUsageUser.setStatus(_A)
class _NwUserVolUsageVolume_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NwUserVolUsageVolume_Type.__name__=_E
_NwUserVolUsageVolume_Object=MibTableColumn
nwUserVolUsageVolume=_NwUserVolUsageVolume_Object((1,3,6,1,4,1,23,2,28,11,2,1,4),_NwUserVolUsageVolume_Type())
nwUserVolUsageVolume.setMaxAccess(_B)
if mibBuilder.loadTexts:nwUserVolUsageVolume.setStatus(_A)
_NwUserVolUsageSpaceUsed_Type=KBytes
_NwUserVolUsageSpaceUsed_Object=MibTableColumn
nwUserVolUsageSpaceUsed=_NwUserVolUsageSpaceUsed_Object((1,3,6,1,4,1,23,2,28,11,2,1,5),_NwUserVolUsageSpaceUsed_Type())
nwUserVolUsageSpaceUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:nwUserVolUsageSpaceUsed.setStatus(_A)
_NwUserVolUsageLimit_Type=KBytes
_NwUserVolUsageLimit_Object=MibTableColumn
nwUserVolUsageLimit=_NwUserVolUsageLimit_Object((1,3,6,1,4,1,23,2,28,11,2,1,6),_NwUserVolUsageLimit_Type())
nwUserVolUsageLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:nwUserVolUsageLimit.setStatus(_A)
_NwVolUsageTable_Object=MibTable
nwVolUsageTable=_NwVolUsageTable_Object((1,3,6,1,4,1,23,2,28,11,3))
if mibBuilder.loadTexts:nwVolUsageTable.setStatus(_A)
_NwVolUsageEntry_Object=MibTableRow
nwVolUsageEntry=_NwVolUsageEntry_Object((1,3,6,1,4,1,23,2,28,11,3,1))
nwVolUsageEntry.setIndexNames((0,_D,_f),(0,_D,_g))
if mibBuilder.loadTexts:nwVolUsageEntry.setStatus(_A)
class _NwVolUsageVolID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NwVolUsageVolID_Type.__name__=_C
_NwVolUsageVolID_Object=MibTableColumn
nwVolUsageVolID=_NwVolUsageVolID_Object((1,3,6,1,4,1,23,2,28,11,3,1,1),_NwVolUsageVolID_Type())
nwVolUsageVolID.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolUsageVolID.setStatus(_A)
class _NwVolUsageUserID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NwVolUsageUserID_Type.__name__=_C
_NwVolUsageUserID_Object=MibTableColumn
nwVolUsageUserID=_NwVolUsageUserID_Object((1,3,6,1,4,1,23,2,28,11,3,1,2),_NwVolUsageUserID_Type())
nwVolUsageUserID.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolUsageUserID.setStatus(_A)
class _NwVolUsageVolume_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NwVolUsageVolume_Type.__name__=_E
_NwVolUsageVolume_Object=MibTableColumn
nwVolUsageVolume=_NwVolUsageVolume_Object((1,3,6,1,4,1,23,2,28,11,3,1,3),_NwVolUsageVolume_Type())
nwVolUsageVolume.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolUsageVolume.setStatus(_A)
_NwVolUsageUser_Type=InternationalDisplayString
_NwVolUsageUser_Object=MibTableColumn
nwVolUsageUser=_NwVolUsageUser_Object((1,3,6,1,4,1,23,2,28,11,3,1,4),_NwVolUsageUser_Type())
nwVolUsageUser.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolUsageUser.setStatus(_A)
_NwVolUsageSpaceUsed_Type=KBytes
_NwVolUsageSpaceUsed_Object=MibTableColumn
nwVolUsageSpaceUsed=_NwVolUsageSpaceUsed_Object((1,3,6,1,4,1,23,2,28,11,3,1,5),_NwVolUsageSpaceUsed_Type())
nwVolUsageSpaceUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolUsageSpaceUsed.setStatus(_A)
_NwVolUsageLimit_Type=KBytes
_NwVolUsageLimit_Object=MibTableColumn
nwVolUsageLimit=_NwVolUsageLimit_Object((1,3,6,1,4,1,23,2,28,11,3,1,6),_NwVolUsageLimit_Type())
nwVolUsageLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:nwVolUsageLimit.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'Seconds':Seconds,'IPXNetNumber':IPXNetNumber,'TransportDomain':TransportDomain,'TransportAddress':TransportAddress,'EngineType':EngineType,'DSTType':DSTType,'novell':novell,'mibDoc':mibDoc,'nwServer':nwServer,'nwSystem':nwSystem,'nwSysServerName':nwSysServerName,'nwSysSerialNumber':nwSysSerialNumber,'nwSysInternalNetNum':nwSysInternalNetNum,'nwSysServerUpTime':nwSysServerUpTime,'nwSysOSSFTLevel':nwSysOSSFTLevel,'nwSysOSMajorVer':nwSysOSMajorVer,'nwSysOSMinorVer':nwSysOSMinorVer,'nwSysOSReleaseDate':nwSysOSReleaseDate,'nwSysOSDescription':nwSysOSDescription,'nwSysOSCopyright':nwSysOSCopyright,'nwSysTime':nwSysTime,'nwSysTimeZone':nwSysTimeZone,'nwSysLoginState':nwSysLoginState,'nwSysLanguageID':nwSysLanguageID,'nwSysNMASerialNumber':nwSysNMASerialNumber,'nwSysNMACopiesAllowed':nwSysNMACopiesAllowed,'nwSysDirectoryTree':nwSysDirectoryTree,'nwSysBinderyContext':nwSysBinderyContext,'nwSysServerDSName':nwSysServerDSName,'nwSysDaylightSavingsStart':nwSysDaylightSavingsStart,'nwSysDaylightSavingsEnd':nwSysDaylightSavingsEnd,'nwSysDaylightSavingsOffset':nwSysDaylightSavingsOffset,'nwSysDaylightSavingsStatus':nwSysDaylightSavingsStatus,'nwFileSystem':nwFileSystem,'nwFSReads':nwFSReads,'nwFSWrites':nwFSWrites,'nwFSReadKBytes':nwFSReadKBytes,'nwFSWrittenKBytes':nwFSWrittenKBytes,'nwFSCacheChecks':nwFSCacheChecks,'nwFSCacheHits':nwFSCacheHits,'nwFSOpenFiles':nwFSOpenFiles,'nwFSMaxOpenFiles':nwFSMaxOpenFiles,'nwFSRecordLocks':nwFSRecordLocks,'nwFSMaxRecordLocks':nwFSMaxRecordLocks,'nwFSMaxSubdirectoryTreeDepth':nwFSMaxSubdirectoryTreeDepth,'nwFSMaxPercentOfVolumeUsedByDir':nwFSMaxPercentOfVolumeUsedByDir,'nwFSVolCount':nwFSVolCount,'nwFSVolTable':nwFSVolTable,'nwFSVolEntry':nwFSVolEntry,_K:nwVolID,'nwVolPhysicalName':nwVolPhysicalName,'nwVolSize':nwVolSize,'nwVolFree':nwVolFree,'nwVolFreeable':nwVolFreeable,'nwVolNonFreeable':nwVolNonFreeable,'nwVolBlockSize':nwVolBlockSize,'nwVolMounted':nwVolMounted,'nwVolAttributes':nwVolAttributes,'nwVolNameSpaces':nwVolNameSpaces,'nwVolTotalDirEntries':nwVolTotalDirEntries,'nwVolUsedDirEntries':nwVolUsedDirEntries,'nwVolSegmentCount':nwVolSegmentCount,'nwVolDSName':nwVolDSName,'nwVolFileSystemID':nwVolFileSystemID,'nwVolFileSystemName':nwVolFileSystemName,'nwFSOpenFileTable':nwFSOpenFileTable,'nwFSOpenFileEntry':nwFSOpenFileEntry,_L:nwOfileVolID,_M:nwOfileDirectoryNumber,_N:nwOfileConnection,'nwOfileVolumeName':nwOfileVolumeName,'nwOfileName':nwOfileName,'nwOfileLoginName':nwOfileLoginName,'nwUsers':nwUsers,'nwUserCount':nwUserCount,'nwLoginCount':nwLoginCount,'nwMaxLogins':nwMaxLogins,'nwConnectionCount':nwConnectionCount,'nwPeakRemoteConnections':nwPeakRemoteConnections,'nwMaxConnections':nwMaxConnections,'nwNLMConnections':nwNLMConnections,'nwConnectionTable':nwConnectionTable,'nwConnectionEntry':nwConnectionEntry,_O:nwConnectionNumber,'nwConnectionLoginName':nwConnectionLoginName,'nwConnectionTransportDomain':nwConnectionTransportDomain,'nwConnectionTransportAddress':nwConnectionTransportAddress,'nwConnectionTime':nwConnectionTime,'nwConnectionReadKBytes':nwConnectionReadKBytes,'nwConnectionWrittenKBytes':nwConnectionWrittenKBytes,'nwConnectionNcpRequests':nwConnectionNcpRequests,'nwConnectionFilesOpen':nwConnectionFilesOpen,'nwConnectionRecordsLocked':nwConnectionRecordsLocked,'nwConnectionPrivilege':nwConnectionPrivilege,'nwConnectionStatus':nwConnectionStatus,'nwQueue':nwQueue,'nwQueueCount':nwQueueCount,'nwQueueTable':nwQueueTable,'nwQueueEntry':nwQueueEntry,'nwQID':nwQID,'nwQName':nwQName,'nwQType':nwQType,'nwQAddJobState':nwQAddJobState,'nwQAttachState':nwQAttachState,'nwQServiceJobState':nwQServiceJobState,'nwQDirVolName':nwQDirVolName,'nwQNumJobEntries':nwQNumJobEntries,'nwQNumAssignedServers':nwQNumAssignedServers,'nwQueueJobTable':nwQueueJobTable,'nwQueueJobEntry':nwQueueJobEntry,_P:nwQJobQID,_Q:nwQJobNumber,'nwQJobDescription':nwQJobDescription,'nwQJobEntryDateTime':nwQJobEntryDateTime,'nwQJobPosition':nwQJobPosition,'nwQJobSize':nwQJobSize,'nwQJobControlFlags':nwQJobControlFlags,'nwQJobUserName':nwQJobUserName,'nwQJobTargetServerName':nwQJobTargetServerName,'nwQJobTargetDateTime':nwQJobTargetDateTime,'nwQJobServerName':nwQJobServerName,'nwQueueServerTable':nwQueueServerTable,'nwQueueServerEntry':nwQueueServerEntry,_R:nwQServerQID,_S:nwQServerID,'nwQServerName':nwQServerName,'nwQServerStatus':nwQServerStatus,'nwOdi':nwOdi,'nwOdiLslEnqSendCount':nwOdiLslEnqSendCount,'nwOdiOsPktRcvBuffer':nwOdiOsPktRcvBuffer,'nwOdiOsMaxPktRcvBuffers':nwOdiOsMaxPktRcvBuffers,'nwOdiOsMinPktRcvBuffers':nwOdiOsMinPktRcvBuffers,'nwSft3':nwSft3,'nwSft3Engine':nwSft3Engine,'nwSft3EngineState':nwSft3EngineState,'nwSft3EngineTable':nwSft3EngineTable,'nwSft3EngineEntry':nwSft3EngineEntry,_T:nwSft3EngineType,'nwSft3EngineName':nwSft3EngineName,'nwSft3EngineInternalNetNum':nwSft3EngineInternalNetNum,'nwNCP':nwNCP,'nwNCPIPXChecksums':nwNCPIPXChecksums,'nwNCPPacketSignatures':nwNCPPacketSignatures,'nwNCPNumNCPReqs':nwNCPNumNCPReqs,'nwNCPUseCount':nwNCPUseCount,'nwNCPPeakUseCount':nwNCPPeakUseCount,'nwNCPForgedPkts':nwNCPForgedPkts,'nwNCPBeingProcesseds':nwNCPBeingProcesseds,'nwNCPNoAvailConns':nwNCPNoAvailConns,'nwNCPIPXChecksumErrs':nwNCPIPXChecksumErrs,'nwNCPInvalidPacketSigs':nwNCPInvalidPacketSigs,'nwNCPExtNumReg':nwNCPExtNumReg,'nwNCPExtInvalidReqs':nwNCPExtInvalidReqs,'nwWatchdog':nwWatchdog,'nwWDTimeBeforeFirstPkt':nwWDTimeBeforeFirstPkt,'nwWDTimeBetweenPkts':nwWDTimeBetweenPkts,'nwWDNumPktsToSend':nwWDNumPktsToSend,'nwWDCurrentState':nwWDCurrentState,'nwWDNotifyConsoleFlag':nwWDNotifyConsoleFlag,'nwNLM':nwNLM,'nwNLMTable':nwNLMTable,'nwNLMEntry':nwNLMEntry,_U:nwNLMIndex,'nwNLMName':nwNLMName,'nwNLMDescription':nwNLMDescription,'nwNLMTotalMemory':nwNLMTotalMemory,'nwNLMCopyright':nwNLMCopyright,'nwNLMProtectionDomain':nwNLMProtectionDomain,'nwNLMMajorVer':nwNLMMajorVer,'nwNLMMinorVer':nwNLMMinorVer,'nwNLMRevision':nwNLMRevision,'nwNLMReleaseDate':nwNLMReleaseDate,'nwSetParams':nwSetParams,'nwSetCategoryTable':nwSetCategoryTable,'nwSetCategoryEntry':nwSetCategoryEntry,_V:nwSetCategoryIndex,'nwSetCategoryName':nwSetCategoryName,'nwSetParamTable':nwSetParamTable,'nwSetParamEntry':nwSetParamEntry,_W:nwSetParamCategoryIndex,_X:nwSetParamIndex,'nwSetParamName':nwSetParamName,'nwSetParamType':nwSetParamType,'nwSetParamValueInteger':nwSetParamValueInteger,'nwSetParamValueString':nwSetParamValueString,'nwSetParamLowerLimit':nwSetParamLowerLimit,'nwSetParamUpperLimit':nwSetParamUpperLimit,'nwSetParamDescrLength':nwSetParamDescrLength,'nwSetParamMode':nwSetParamMode,'nwSetDescrTable':nwSetDescrTable,'nwSetDescrEntry':nwSetDescrEntry,_Y:nwSetDescrCategoryIndex,_Z:nwSetDescrParamIndex,_a:nwSetDescrIndex,'nwSetDescription':nwSetDescription,'nwUserAccounts':nwUserAccounts,'nwUserAcctTable':nwUserAcctTable,'nwUserAcctEntry':nwUserAcctEntry,_b:nwUserID,'nwUserName':nwUserName,'nwUserDiskUsage':nwUserDiskUsage,'nwUserLastLoginTime':nwUserLastLoginTime,'nwUserAccountStatus':nwUserAccountStatus,'nwUserPasswordStatus':nwUserPasswordStatus,'nwUserBadLoginTransport':nwUserBadLoginTransport,'nwUserBadLoginAddress':nwUserBadLoginAddress,'nwUserBadLoginAttempts':nwUserBadLoginAttempts,'nwUserFullName':nwUserFullName,'nwUserVolUsageTable':nwUserVolUsageTable,'nwUserVolUsageEntry':nwUserVolUsageEntry,_d:nwUserVolUserID,_e:nwUserVolVolID,'nwUserVolUsageUser':nwUserVolUsageUser,'nwUserVolUsageVolume':nwUserVolUsageVolume,'nwUserVolUsageSpaceUsed':nwUserVolUsageSpaceUsed,'nwUserVolUsageLimit':nwUserVolUsageLimit,'nwVolUsageTable':nwVolUsageTable,'nwVolUsageEntry':nwVolUsageEntry,_f:nwVolUsageVolID,_g:nwVolUsageUserID,'nwVolUsageVolume':nwVolUsageVolume,'nwVolUsageUser':nwVolUsageUser,'nwVolUsageSpaceUsed':nwVolUsageSpaceUsed,'nwVolUsageLimit':nwVolUsageLimit})