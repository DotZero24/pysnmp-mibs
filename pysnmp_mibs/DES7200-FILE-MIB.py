_S='myFileTransMeansMIBGroup'
_R='myFileMIBGroup'
_Q='myFileTransMeans'
_P='myFileSystemAvailableRoom'
_O='myFileSystemMaxRoom'
_N='myFileTransEntryStatus'
_M='myFileTransDataLength'
_L='myFileTransComplete'
_K='myFileTransResult'
_J='myFileTransServerAddr'
_I='myFileTransDescFileName'
_H='myFileTransSrcFileName'
_G='myFileTransOperType'
_F='myFileTransIndex'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='DES7200-FILE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('DES7200-SMI','myMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
myFileMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,2,11))
if mibBuilder.loadTexts:myFileMIB.setRevisions(('2002-03-20 00:00',))
_MyFileMIBObjects_ObjectIdentity=ObjectIdentity
myFileMIBObjects=_MyFileMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,11,1))
_MyFileTransTable_Object=MibTable
myFileTransTable=_MyFileTransTable_Object((1,3,6,1,4,1,171,10,97,2,11,1,1))
if mibBuilder.loadTexts:myFileTransTable.setStatus(_A)
_MyFileTransEntry_Object=MibTableRow
myFileTransEntry=_MyFileTransEntry_Object((1,3,6,1,4,1,171,10,97,2,11,1,1,1))
myFileTransEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:myFileTransEntry.setStatus(_A)
_MyFileTransIndex_Type=Integer32
_MyFileTransIndex_Object=MibTableColumn
myFileTransIndex=_MyFileTransIndex_Object((1,3,6,1,4,1,171,10,97,2,11,1,1,1,1),_MyFileTransIndex_Type())
myFileTransIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myFileTransIndex.setStatus(_A)
class _MyFileTransMeans_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tftp',1),('xmodem',2),('other',3)))
_MyFileTransMeans_Type.__name__=_E
_MyFileTransMeans_Object=MibTableColumn
myFileTransMeans=_MyFileTransMeans_Object((1,3,6,1,4,1,171,10,97,2,11,1,1,1,2),_MyFileTransMeans_Type())
myFileTransMeans.setMaxAccess(_D)
if mibBuilder.loadTexts:myFileTransMeans.setStatus(_A)
class _MyFileTransOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('upload',1),('download',2),('synchronize',3)))
_MyFileTransOperType_Type.__name__=_E
_MyFileTransOperType_Object=MibTableColumn
myFileTransOperType=_MyFileTransOperType_Object((1,3,6,1,4,1,171,10,97,2,11,1,1,1,3),_MyFileTransOperType_Type())
myFileTransOperType.setMaxAccess(_D)
if mibBuilder.loadTexts:myFileTransOperType.setStatus(_A)
_MyFileTransSrcFileName_Type=DisplayString
_MyFileTransSrcFileName_Object=MibTableColumn
myFileTransSrcFileName=_MyFileTransSrcFileName_Object((1,3,6,1,4,1,171,10,97,2,11,1,1,1,4),_MyFileTransSrcFileName_Type())
myFileTransSrcFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:myFileTransSrcFileName.setStatus(_A)
_MyFileTransDescFileName_Type=DisplayString
_MyFileTransDescFileName_Object=MibTableColumn
myFileTransDescFileName=_MyFileTransDescFileName_Object((1,3,6,1,4,1,171,10,97,2,11,1,1,1,5),_MyFileTransDescFileName_Type())
myFileTransDescFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:myFileTransDescFileName.setStatus(_A)
_MyFileTransServerAddr_Type=IpAddress
_MyFileTransServerAddr_Object=MibTableColumn
myFileTransServerAddr=_MyFileTransServerAddr_Object((1,3,6,1,4,1,171,10,97,2,11,1,1,1,6),_MyFileTransServerAddr_Type())
myFileTransServerAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:myFileTransServerAddr.setStatus(_A)
class _MyFileTransResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('success',1),('failure',2),('parametersIllegel',3),('timeout',4)))
_MyFileTransResult_Type.__name__=_E
_MyFileTransResult_Object=MibTableColumn
myFileTransResult=_MyFileTransResult_Object((1,3,6,1,4,1,171,10,97,2,11,1,1,1,7),_MyFileTransResult_Type())
myFileTransResult.setMaxAccess(_C)
if mibBuilder.loadTexts:myFileTransResult.setStatus(_A)
_MyFileTransComplete_Type=TruthValue
_MyFileTransComplete_Object=MibTableColumn
myFileTransComplete=_MyFileTransComplete_Object((1,3,6,1,4,1,171,10,97,2,11,1,1,1,8),_MyFileTransComplete_Type())
myFileTransComplete.setMaxAccess(_C)
if mibBuilder.loadTexts:myFileTransComplete.setStatus(_A)
_MyFileTransDataLength_Type=Gauge32
_MyFileTransDataLength_Object=MibTableColumn
myFileTransDataLength=_MyFileTransDataLength_Object((1,3,6,1,4,1,171,10,97,2,11,1,1,1,9),_MyFileTransDataLength_Type())
myFileTransDataLength.setMaxAccess(_C)
if mibBuilder.loadTexts:myFileTransDataLength.setStatus(_A)
_MyFileTransEntryStatus_Type=RowStatus
_MyFileTransEntryStatus_Object=MibTableColumn
myFileTransEntryStatus=_MyFileTransEntryStatus_Object((1,3,6,1,4,1,171,10,97,2,11,1,1,1,10),_MyFileTransEntryStatus_Type())
myFileTransEntryStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:myFileTransEntryStatus.setStatus(_A)
_MyFileSystemMaxRoom_Type=Integer32
_MyFileSystemMaxRoom_Object=MibScalar
myFileSystemMaxRoom=_MyFileSystemMaxRoom_Object((1,3,6,1,4,1,171,10,97,2,11,1,2),_MyFileSystemMaxRoom_Type())
myFileSystemMaxRoom.setMaxAccess(_C)
if mibBuilder.loadTexts:myFileSystemMaxRoom.setStatus(_A)
_MyFileSystemAvailableRoom_Type=Integer32
_MyFileSystemAvailableRoom_Object=MibScalar
myFileSystemAvailableRoom=_MyFileSystemAvailableRoom_Object((1,3,6,1,4,1,171,10,97,2,11,1,3),_MyFileSystemAvailableRoom_Type())
myFileSystemAvailableRoom.setMaxAccess(_C)
if mibBuilder.loadTexts:myFileSystemAvailableRoom.setStatus(_A)
_MyFileMIBConformance_ObjectIdentity=ObjectIdentity
myFileMIBConformance=_MyFileMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,11,2))
_MyFileMIBCompliances_ObjectIdentity=ObjectIdentity
myFileMIBCompliances=_MyFileMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,11,2,1))
_MyFileMIBGroups_ObjectIdentity=ObjectIdentity
myFileMIBGroups=_MyFileMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,11,2,2))
myFileMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,11,2,2,1))
myFileMIBGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:myFileMIBGroup.setStatus(_A)
myFileTransMeansMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,11,2,2,2))
myFileTransMeansMIBGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:myFileTransMeansMIBGroup.setStatus(_A)
myFileMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,11,2,1,1))
myFileMIBCompliance.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:myFileMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'myFileMIB':myFileMIB,'myFileMIBObjects':myFileMIBObjects,'myFileTransTable':myFileTransTable,'myFileTransEntry':myFileTransEntry,_F:myFileTransIndex,_Q:myFileTransMeans,_G:myFileTransOperType,_H:myFileTransSrcFileName,_I:myFileTransDescFileName,_J:myFileTransServerAddr,_K:myFileTransResult,_L:myFileTransComplete,_M:myFileTransDataLength,_N:myFileTransEntryStatus,_O:myFileSystemMaxRoom,_P:myFileSystemAvailableRoom,'myFileMIBConformance':myFileMIBConformance,'myFileMIBCompliances':myFileMIBCompliances,'myFileMIBCompliance':myFileMIBCompliance,'myFileMIBGroups':myFileMIBGroups,_R:myFileMIBGroup,_S:myFileTransMeansMIBGroup})