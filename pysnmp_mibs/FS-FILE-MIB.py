_b='fsFileTransMeansMIBGroup'
_a='fsFileMIBGroup'
_Z='fsFileTransMeans'
_Y='fsFileSystemAvailableRoom'
_X='fsFileSystemMaxRoom'
_W='fsFileTransPortType'
_V='fsFileTransServerPort'
_U='fsFileTransFileType'
_T='fsFileTransPassWord'
_S='fsFileTransUserName'
_R='fsFileTransServerAddr6'
_Q='fsFileTransEntryStatus'
_P='fsFileTransDataLength'
_O='fsFileTransComplete'
_N='fsFileTransResult'
_M='fsFileTransServerAddr'
_L='fsFileTransDescFileName'
_K='fsFileTransSrcFileName'
_J='fsFileTransOperType'
_I='OctetString'
_H='fsFileTransFailedReason'
_G='read-write'
_F='fsFileTransIndex'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='FS-FILE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsFileMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,11))
if mibBuilder.loadTexts:fsFileMIB.setRevisions(('2002-03-20 00:00',))
_FsFileMIBTraps_ObjectIdentity=ObjectIdentity
fsFileMIBTraps=_FsFileMIBTraps_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,11,0))
_FsFileMIBObjects_ObjectIdentity=ObjectIdentity
fsFileMIBObjects=_FsFileMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,11,1))
_FsFileTransTable_Object=MibTable
fsFileTransTable=_FsFileTransTable_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,1))
if mibBuilder.loadTexts:fsFileTransTable.setStatus(_A)
_FsFileTransEntry_Object=MibTableRow
fsFileTransEntry=_FsFileTransEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,1,1))
fsFileTransEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:fsFileTransEntry.setStatus(_A)
_FsFileTransIndex_Type=Integer32
_FsFileTransIndex_Object=MibTableColumn
fsFileTransIndex=_FsFileTransIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,1,1,1),_FsFileTransIndex_Type())
fsFileTransIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsFileTransIndex.setStatus(_A)
class _FsFileTransMeans_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tftp',1),('xmodem',2),('other',3)))
_FsFileTransMeans_Type.__name__=_E
_FsFileTransMeans_Object=MibTableColumn
fsFileTransMeans=_FsFileTransMeans_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,1,1,2),_FsFileTransMeans_Type())
fsFileTransMeans.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFileTransMeans.setStatus(_A)
class _FsFileTransOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('upload',1),('download',2),('synchronize',3)))
_FsFileTransOperType_Type.__name__=_E
_FsFileTransOperType_Object=MibTableColumn
fsFileTransOperType=_FsFileTransOperType_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,1,1,3),_FsFileTransOperType_Type())
fsFileTransOperType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFileTransOperType.setStatus(_A)
_FsFileTransSrcFileName_Type=DisplayString
_FsFileTransSrcFileName_Object=MibTableColumn
fsFileTransSrcFileName=_FsFileTransSrcFileName_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,1,1,4),_FsFileTransSrcFileName_Type())
fsFileTransSrcFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFileTransSrcFileName.setStatus(_A)
_FsFileTransDescFileName_Type=DisplayString
_FsFileTransDescFileName_Object=MibTableColumn
fsFileTransDescFileName=_FsFileTransDescFileName_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,1,1,5),_FsFileTransDescFileName_Type())
fsFileTransDescFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFileTransDescFileName.setStatus(_A)
_FsFileTransServerAddr_Type=IpAddress
_FsFileTransServerAddr_Object=MibTableColumn
fsFileTransServerAddr=_FsFileTransServerAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,1,1,6),_FsFileTransServerAddr_Type())
fsFileTransServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFileTransServerAddr.setStatus(_A)
class _FsFileTransResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('success',1),('failure',2),('parametersIllegel',3),('timeout',4)))
_FsFileTransResult_Type.__name__=_E
_FsFileTransResult_Object=MibTableColumn
fsFileTransResult=_FsFileTransResult_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,1,1,7),_FsFileTransResult_Type())
fsFileTransResult.setMaxAccess(_D)
if mibBuilder.loadTexts:fsFileTransResult.setStatus(_A)
_FsFileTransComplete_Type=TruthValue
_FsFileTransComplete_Object=MibTableColumn
fsFileTransComplete=_FsFileTransComplete_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,1,1,8),_FsFileTransComplete_Type())
fsFileTransComplete.setMaxAccess(_D)
if mibBuilder.loadTexts:fsFileTransComplete.setStatus(_A)
_FsFileTransDataLength_Type=Gauge32
_FsFileTransDataLength_Object=MibTableColumn
fsFileTransDataLength=_FsFileTransDataLength_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,1,1,9),_FsFileTransDataLength_Type())
fsFileTransDataLength.setMaxAccess(_D)
if mibBuilder.loadTexts:fsFileTransDataLength.setStatus(_A)
_FsFileTransEntryStatus_Type=RowStatus
_FsFileTransEntryStatus_Object=MibTableColumn
fsFileTransEntryStatus=_FsFileTransEntryStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,1,1,10),_FsFileTransEntryStatus_Type())
fsFileTransEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFileTransEntryStatus.setStatus(_A)
class _FsFileTransServerAddr6_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsFileTransServerAddr6_Type.__name__=_I
_FsFileTransServerAddr6_Object=MibTableColumn
fsFileTransServerAddr6=_FsFileTransServerAddr6_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,1,1,11),_FsFileTransServerAddr6_Type())
fsFileTransServerAddr6.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFileTransServerAddr6.setStatus(_A)
_FsFileTransUserName_Type=DisplayString
_FsFileTransUserName_Object=MibTableColumn
fsFileTransUserName=_FsFileTransUserName_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,1,1,12),_FsFileTransUserName_Type())
fsFileTransUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFileTransUserName.setStatus(_A)
_FsFileTransPassWord_Type=DisplayString
_FsFileTransPassWord_Object=MibTableColumn
fsFileTransPassWord=_FsFileTransPassWord_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,1,1,13),_FsFileTransPassWord_Type())
fsFileTransPassWord.setMaxAccess(_C)
if mibBuilder.loadTexts:fsFileTransPassWord.setStatus(_A)
_FsFileTransFailedReason_Type=DisplayString
_FsFileTransFailedReason_Object=MibTableColumn
fsFileTransFailedReason=_FsFileTransFailedReason_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,1,1,14),_FsFileTransFailedReason_Type())
fsFileTransFailedReason.setMaxAccess(_D)
if mibBuilder.loadTexts:fsFileTransFailedReason.setStatus(_A)
class _FsFileTransFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('software-version-file',1),('config-file',2),('log-file',3)))
_FsFileTransFileType_Type.__name__=_E
_FsFileTransFileType_Object=MibTableColumn
fsFileTransFileType=_FsFileTransFileType_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,1,1,15),_FsFileTransFileType_Type())
fsFileTransFileType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsFileTransFileType.setStatus(_A)
_FsFileTransServerPort_Type=Integer32
_FsFileTransServerPort_Object=MibTableColumn
fsFileTransServerPort=_FsFileTransServerPort_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,1,1,16),_FsFileTransServerPort_Type())
fsFileTransServerPort.setMaxAccess(_G)
if mibBuilder.loadTexts:fsFileTransServerPort.setStatus(_A)
class _FsFileTransPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('byInterfacePort',1),('byMgmtPort',2)))
_FsFileTransPortType_Type.__name__=_E
_FsFileTransPortType_Object=MibTableColumn
fsFileTransPortType=_FsFileTransPortType_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,1,1,17),_FsFileTransPortType_Type())
fsFileTransPortType.setMaxAccess(_G)
if mibBuilder.loadTexts:fsFileTransPortType.setStatus(_A)
_FsFileSystemMaxRoom_Type=Integer32
_FsFileSystemMaxRoom_Object=MibScalar
fsFileSystemMaxRoom=_FsFileSystemMaxRoom_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,2),_FsFileSystemMaxRoom_Type())
fsFileSystemMaxRoom.setMaxAccess(_D)
if mibBuilder.loadTexts:fsFileSystemMaxRoom.setStatus(_A)
_FsFileSystemAvailableRoom_Type=Integer32
_FsFileSystemAvailableRoom_Object=MibScalar
fsFileSystemAvailableRoom=_FsFileSystemAvailableRoom_Object((1,3,6,1,4,1,52642,1,1,10,2,11,1,3),_FsFileSystemAvailableRoom_Type())
fsFileSystemAvailableRoom.setMaxAccess(_D)
if mibBuilder.loadTexts:fsFileSystemAvailableRoom.setStatus(_A)
_FsFileMIBConformance_ObjectIdentity=ObjectIdentity
fsFileMIBConformance=_FsFileMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,11,2))
_FsFileMIBCompliances_ObjectIdentity=ObjectIdentity
fsFileMIBCompliances=_FsFileMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,11,2,1))
_FsFileMIBGroups_ObjectIdentity=ObjectIdentity
fsFileMIBGroups=_FsFileMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,11,2,2))
fsFileMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,11,2,2,1))
fsFileMIBGroup.setObjects(*((_B,_F),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_H),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:fsFileMIBGroup.setStatus(_A)
fsFileTransMeansMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,11,2,2,2))
fsFileTransMeansMIBGroup.setObjects((_B,_Z))
if mibBuilder.loadTexts:fsFileTransMeansMIBGroup.setStatus(_A)
fsFileSystemUpdateFailTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,11,0,1))
fsFileSystemUpdateFailTrap.setObjects((_B,_H))
if mibBuilder.loadTexts:fsFileSystemUpdateFailTrap.setStatus(_A)
fsFileMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,11,2,1,1))
fsFileMIBCompliance.setObjects(*((_B,_a),(_B,_b)))
if mibBuilder.loadTexts:fsFileMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsFileMIB':fsFileMIB,'fsFileMIBTraps':fsFileMIBTraps,'fsFileSystemUpdateFailTrap':fsFileSystemUpdateFailTrap,'fsFileMIBObjects':fsFileMIBObjects,'fsFileTransTable':fsFileTransTable,'fsFileTransEntry':fsFileTransEntry,_F:fsFileTransIndex,_Z:fsFileTransMeans,_J:fsFileTransOperType,_K:fsFileTransSrcFileName,_L:fsFileTransDescFileName,_M:fsFileTransServerAddr,_N:fsFileTransResult,_O:fsFileTransComplete,_P:fsFileTransDataLength,_Q:fsFileTransEntryStatus,_R:fsFileTransServerAddr6,_S:fsFileTransUserName,_T:fsFileTransPassWord,_H:fsFileTransFailedReason,_U:fsFileTransFileType,_V:fsFileTransServerPort,_W:fsFileTransPortType,_X:fsFileSystemMaxRoom,_Y:fsFileSystemAvailableRoom,'fsFileMIBConformance':fsFileMIBConformance,'fsFileMIBCompliances':fsFileMIBCompliances,'fsFileMIBCompliance':fsFileMIBCompliance,'fsFileMIBGroups':fsFileMIBGroups,_a:fsFileMIBGroup,_b:fsFileTransMeansMIBGroup})