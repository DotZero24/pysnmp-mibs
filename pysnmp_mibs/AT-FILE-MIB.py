_E='fileIndex'
_D='AT-FILE-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,modules=mibBuilder.importSymbols('AT-SMI-MIB','DisplayStringUnsized','modules')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
file=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,56))
if mibBuilder.loadTexts:file.setRevisions(('2006-06-28 12:22',))
_FileTable_Object=MibTable
fileTable=_FileTable_Object((1,3,6,1,4,1,207,8,4,4,4,56,1))
if mibBuilder.loadTexts:fileTable.setStatus(_A)
_FileEntry_Object=MibTableRow
fileEntry=_FileEntry_Object((1,3,6,1,4,1,207,8,4,4,4,56,1,1))
fileEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:fileEntry.setStatus(_A)
_FileIndex_Type=Integer32
_FileIndex_Object=MibTableColumn
fileIndex=_FileIndex_Object((1,3,6,1,4,1,207,8,4,4,4,56,1,1,1),_FileIndex_Type())
fileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fileIndex.setStatus(_A)
_FileName_Type=DisplayString
_FileName_Object=MibTableColumn
fileName=_FileName_Object((1,3,6,1,4,1,207,8,4,4,4,56,1,1,2),_FileName_Type())
fileName.setMaxAccess(_B)
if mibBuilder.loadTexts:fileName.setStatus(_A)
class _FileDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('flash',1),('nvs',2)))
_FileDevice_Type.__name__=_C
_FileDevice_Object=MibTableColumn
fileDevice=_FileDevice_Object((1,3,6,1,4,1,207,8,4,4,4,56,1,1,3),_FileDevice_Type())
fileDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:fileDevice.setStatus(_A)
_FileCreationTime_Type=DisplayString
_FileCreationTime_Object=MibTableColumn
fileCreationTime=_FileCreationTime_Object((1,3,6,1,4,1,207,8,4,4,4,56,1,1,4),_FileCreationTime_Type())
fileCreationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fileCreationTime.setStatus(_A)
class _FileStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('deleting',2)))
_FileStatus_Type.__name__=_C
_FileStatus_Object=MibTableColumn
fileStatus=_FileStatus_Object((1,3,6,1,4,1,207,8,4,4,4,56,1,1,5),_FileStatus_Type())
fileStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:fileStatus.setStatus(_A)
_FileSize_Type=Integer32
_FileSize_Object=MibTableColumn
fileSize=_FileSize_Object((1,3,6,1,4,1,207,8,4,4,4,56,1,1,6),_FileSize_Type())
fileSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fileSize.setStatus(_A)
_FileNumbers_Type=Integer32
_FileNumbers_Object=MibScalar
fileNumbers=_FileNumbers_Object((1,3,6,1,4,1,207,8,4,4,4,56,2),_FileNumbers_Type())
fileNumbers.setMaxAccess(_B)
if mibBuilder.loadTexts:fileNumbers.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'file':file,'fileTable':fileTable,'fileEntry':fileEntry,_E:fileIndex,'fileName':fileName,'fileDevice':fileDevice,'fileCreationTime':fileCreationTime,'fileStatus':fileStatus,'fileSize':fileSize,'fileNumbers':fileNumbers})