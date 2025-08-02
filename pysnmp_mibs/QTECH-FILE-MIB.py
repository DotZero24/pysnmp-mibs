_b='qtechFileTransMeansMIBGroup'
_a='qtechFileMIBGroup'
_Z='qtechFileTransMeans'
_Y='qtechFileSystemAvailableRoom'
_X='qtechFileSystemMaxRoom'
_W='qtechFileTransPortType'
_V='qtechFileTransServerPort'
_U='qtechFileTransFileType'
_T='qtechFileTransPassWord'
_S='qtechFileTransUserName'
_R='qtechFileTransServerAddr6'
_Q='qtechFileTransEntryStatus'
_P='qtechFileTransDataLength'
_O='qtechFileTransComplete'
_N='qtechFileTransResult'
_M='qtechFileTransServerAddr'
_L='qtechFileTransDescFileName'
_K='qtechFileTransSrcFileName'
_J='qtechFileTransOperType'
_I='OctetString'
_H='qtechFileTransFailedReason'
_G='read-write'
_F='qtechFileTransIndex'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='QTECH-FILE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
qtechFileMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,11))
if mibBuilder.loadTexts:qtechFileMIB.setRevisions(('2002-03-20 00:00',))
_QtechFileMIBTraps_ObjectIdentity=ObjectIdentity
qtechFileMIBTraps=_QtechFileMIBTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,11,0))
_QtechFileMIBObjects_ObjectIdentity=ObjectIdentity
qtechFileMIBObjects=_QtechFileMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,11,1))
_QtechFileTransTable_Object=MibTable
qtechFileTransTable=_QtechFileTransTable_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,1))
if mibBuilder.loadTexts:qtechFileTransTable.setStatus(_A)
_QtechFileTransEntry_Object=MibTableRow
qtechFileTransEntry=_QtechFileTransEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,1,1))
qtechFileTransEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:qtechFileTransEntry.setStatus(_A)
_QtechFileTransIndex_Type=Integer32
_QtechFileTransIndex_Object=MibTableColumn
qtechFileTransIndex=_QtechFileTransIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,1,1,1),_QtechFileTransIndex_Type())
qtechFileTransIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechFileTransIndex.setStatus(_A)
class _QtechFileTransMeans_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tftp',1),('xmodem',2),('other',3)))
_QtechFileTransMeans_Type.__name__=_E
_QtechFileTransMeans_Object=MibTableColumn
qtechFileTransMeans=_QtechFileTransMeans_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,1,1,2),_QtechFileTransMeans_Type())
qtechFileTransMeans.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFileTransMeans.setStatus(_A)
class _QtechFileTransOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('upload',1),('download',2),('synchronize',3)))
_QtechFileTransOperType_Type.__name__=_E
_QtechFileTransOperType_Object=MibTableColumn
qtechFileTransOperType=_QtechFileTransOperType_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,1,1,3),_QtechFileTransOperType_Type())
qtechFileTransOperType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFileTransOperType.setStatus(_A)
_QtechFileTransSrcFileName_Type=DisplayString
_QtechFileTransSrcFileName_Object=MibTableColumn
qtechFileTransSrcFileName=_QtechFileTransSrcFileName_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,1,1,4),_QtechFileTransSrcFileName_Type())
qtechFileTransSrcFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFileTransSrcFileName.setStatus(_A)
_QtechFileTransDescFileName_Type=DisplayString
_QtechFileTransDescFileName_Object=MibTableColumn
qtechFileTransDescFileName=_QtechFileTransDescFileName_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,1,1,5),_QtechFileTransDescFileName_Type())
qtechFileTransDescFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFileTransDescFileName.setStatus(_A)
_QtechFileTransServerAddr_Type=IpAddress
_QtechFileTransServerAddr_Object=MibTableColumn
qtechFileTransServerAddr=_QtechFileTransServerAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,1,1,6),_QtechFileTransServerAddr_Type())
qtechFileTransServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFileTransServerAddr.setStatus(_A)
class _QtechFileTransResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('success',1),('failure',2),('parametersIllegel',3),('timeout',4)))
_QtechFileTransResult_Type.__name__=_E
_QtechFileTransResult_Object=MibTableColumn
qtechFileTransResult=_QtechFileTransResult_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,1,1,7),_QtechFileTransResult_Type())
qtechFileTransResult.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechFileTransResult.setStatus(_A)
_QtechFileTransComplete_Type=TruthValue
_QtechFileTransComplete_Object=MibTableColumn
qtechFileTransComplete=_QtechFileTransComplete_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,1,1,8),_QtechFileTransComplete_Type())
qtechFileTransComplete.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechFileTransComplete.setStatus(_A)
_QtechFileTransDataLength_Type=Gauge32
_QtechFileTransDataLength_Object=MibTableColumn
qtechFileTransDataLength=_QtechFileTransDataLength_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,1,1,9),_QtechFileTransDataLength_Type())
qtechFileTransDataLength.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechFileTransDataLength.setStatus(_A)
_QtechFileTransEntryStatus_Type=RowStatus
_QtechFileTransEntryStatus_Object=MibTableColumn
qtechFileTransEntryStatus=_QtechFileTransEntryStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,1,1,10),_QtechFileTransEntryStatus_Type())
qtechFileTransEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFileTransEntryStatus.setStatus(_A)
class _QtechFileTransServerAddr6_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_QtechFileTransServerAddr6_Type.__name__=_I
_QtechFileTransServerAddr6_Object=MibTableColumn
qtechFileTransServerAddr6=_QtechFileTransServerAddr6_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,1,1,11),_QtechFileTransServerAddr6_Type())
qtechFileTransServerAddr6.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFileTransServerAddr6.setStatus(_A)
_QtechFileTransUserName_Type=DisplayString
_QtechFileTransUserName_Object=MibTableColumn
qtechFileTransUserName=_QtechFileTransUserName_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,1,1,12),_QtechFileTransUserName_Type())
qtechFileTransUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFileTransUserName.setStatus(_A)
_QtechFileTransPassWord_Type=DisplayString
_QtechFileTransPassWord_Object=MibTableColumn
qtechFileTransPassWord=_QtechFileTransPassWord_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,1,1,13),_QtechFileTransPassWord_Type())
qtechFileTransPassWord.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechFileTransPassWord.setStatus(_A)
_QtechFileTransFailedReason_Type=DisplayString
_QtechFileTransFailedReason_Object=MibTableColumn
qtechFileTransFailedReason=_QtechFileTransFailedReason_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,1,1,14),_QtechFileTransFailedReason_Type())
qtechFileTransFailedReason.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechFileTransFailedReason.setStatus(_A)
class _QtechFileTransFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('software-version-file',1),('config-file',2),('log-file',3)))
_QtechFileTransFileType_Type.__name__=_E
_QtechFileTransFileType_Object=MibTableColumn
qtechFileTransFileType=_QtechFileTransFileType_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,1,1,15),_QtechFileTransFileType_Type())
qtechFileTransFileType.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechFileTransFileType.setStatus(_A)
_QtechFileTransServerPort_Type=Integer32
_QtechFileTransServerPort_Object=MibTableColumn
qtechFileTransServerPort=_QtechFileTransServerPort_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,1,1,16),_QtechFileTransServerPort_Type())
qtechFileTransServerPort.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechFileTransServerPort.setStatus(_A)
class _QtechFileTransPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('byInterfacePort',1),('byMgmtPort',2)))
_QtechFileTransPortType_Type.__name__=_E
_QtechFileTransPortType_Object=MibTableColumn
qtechFileTransPortType=_QtechFileTransPortType_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,1,1,17),_QtechFileTransPortType_Type())
qtechFileTransPortType.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechFileTransPortType.setStatus(_A)
_QtechFileSystemMaxRoom_Type=Integer32
_QtechFileSystemMaxRoom_Object=MibScalar
qtechFileSystemMaxRoom=_QtechFileSystemMaxRoom_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,2),_QtechFileSystemMaxRoom_Type())
qtechFileSystemMaxRoom.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechFileSystemMaxRoom.setStatus(_A)
_QtechFileSystemAvailableRoom_Type=Integer32
_QtechFileSystemAvailableRoom_Object=MibScalar
qtechFileSystemAvailableRoom=_QtechFileSystemAvailableRoom_Object((1,3,6,1,4,1,27514,1,1,10,2,11,1,3),_QtechFileSystemAvailableRoom_Type())
qtechFileSystemAvailableRoom.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechFileSystemAvailableRoom.setStatus(_A)
_QtechFileMIBConformance_ObjectIdentity=ObjectIdentity
qtechFileMIBConformance=_QtechFileMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,11,2))
_QtechFileMIBCompliances_ObjectIdentity=ObjectIdentity
qtechFileMIBCompliances=_QtechFileMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,11,2,1))
_QtechFileMIBGroups_ObjectIdentity=ObjectIdentity
qtechFileMIBGroups=_QtechFileMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,11,2,2))
qtechFileMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,11,2,2,1))
qtechFileMIBGroup.setObjects(*((_B,_F),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_H),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:qtechFileMIBGroup.setStatus(_A)
qtechFileTransMeansMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,11,2,2,2))
qtechFileTransMeansMIBGroup.setObjects((_B,_Z))
if mibBuilder.loadTexts:qtechFileTransMeansMIBGroup.setStatus(_A)
qtechFileSystemUpdateFailTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,11,0,1))
qtechFileSystemUpdateFailTrap.setObjects((_B,_H))
if mibBuilder.loadTexts:qtechFileSystemUpdateFailTrap.setStatus(_A)
qtechFileMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,11,2,1,1))
qtechFileMIBCompliance.setObjects(*((_B,_a),(_B,_b)))
if mibBuilder.loadTexts:qtechFileMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechFileMIB':qtechFileMIB,'qtechFileMIBTraps':qtechFileMIBTraps,'qtechFileSystemUpdateFailTrap':qtechFileSystemUpdateFailTrap,'qtechFileMIBObjects':qtechFileMIBObjects,'qtechFileTransTable':qtechFileTransTable,'qtechFileTransEntry':qtechFileTransEntry,_F:qtechFileTransIndex,_Z:qtechFileTransMeans,_J:qtechFileTransOperType,_K:qtechFileTransSrcFileName,_L:qtechFileTransDescFileName,_M:qtechFileTransServerAddr,_N:qtechFileTransResult,_O:qtechFileTransComplete,_P:qtechFileTransDataLength,_Q:qtechFileTransEntryStatus,_R:qtechFileTransServerAddr6,_S:qtechFileTransUserName,_T:qtechFileTransPassWord,_H:qtechFileTransFailedReason,_U:qtechFileTransFileType,_V:qtechFileTransServerPort,_W:qtechFileTransPortType,_X:qtechFileSystemMaxRoom,_Y:qtechFileSystemAvailableRoom,'qtechFileMIBConformance':qtechFileMIBConformance,'qtechFileMIBCompliances':qtechFileMIBCompliances,'qtechFileMIBCompliance':qtechFileMIBCompliance,'qtechFileMIBGroups':qtechFileMIBGroups,_a:qtechFileMIBGroup,_b:qtechFileTransMeansMIBGroup})