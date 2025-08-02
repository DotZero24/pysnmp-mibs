_G='atFilev2SDcardStackMemberId'
_F='atFilev2Filename'
_E='AT-FILEv2-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
modules,=mibBuilder.importSymbols('AT-SMI-MIB','modules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
atFilev2=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,600))
if mibBuilder.loadTexts:atFilev2.setRevisions(('2008-09-24 00:00',))
_AtFilev2TableOptions_ObjectIdentity=ObjectIdentity
atFilev2TableOptions=_AtFilev2TableOptions_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,600,1))
class _AtFilev2Recursive_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AtFilev2Recursive_Type.__name__=_C
_AtFilev2Recursive_Object=MibScalar
atFilev2Recursive=_AtFilev2Recursive_Object((1,3,6,1,4,1,207,8,4,4,4,600,1,1),_AtFilev2Recursive_Type())
atFilev2Recursive.setMaxAccess(_B)
if mibBuilder.loadTexts:atFilev2Recursive.setStatus(_A)
class _AtFilev2AllFiles_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AtFilev2AllFiles_Type.__name__=_C
_AtFilev2AllFiles_Object=MibScalar
atFilev2AllFiles=_AtFilev2AllFiles_Object((1,3,6,1,4,1,207,8,4,4,4,600,1,2),_AtFilev2AllFiles_Type())
atFilev2AllFiles.setMaxAccess(_B)
if mibBuilder.loadTexts:atFilev2AllFiles.setStatus(_A)
class _AtFilev2Device_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_AtFilev2Device_Type.__name__=_C
_AtFilev2Device_Object=MibScalar
atFilev2Device=_AtFilev2Device_Object((1,3,6,1,4,1,207,8,4,4,4,600,1,3),_AtFilev2Device_Type())
atFilev2Device.setMaxAccess(_B)
if mibBuilder.loadTexts:atFilev2Device.setStatus(_A)
class _AtFilev2StackID_Type(Integer32):defaultValue=1
_AtFilev2StackID_Type.__name__=_C
_AtFilev2StackID_Object=MibScalar
atFilev2StackID=_AtFilev2StackID_Object((1,3,6,1,4,1,207,8,4,4,4,600,1,4),_AtFilev2StackID_Type())
atFilev2StackID.setMaxAccess(_B)
if mibBuilder.loadTexts:atFilev2StackID.setStatus(_A)
_AtFilev2Table_Object=MibTable
atFilev2Table=_AtFilev2Table_Object((1,3,6,1,4,1,207,8,4,4,4,600,2))
if mibBuilder.loadTexts:atFilev2Table.setStatus(_A)
_AtFilev2Entry_Object=MibTableRow
atFilev2Entry=_AtFilev2Entry_Object((1,3,6,1,4,1,207,8,4,4,4,600,2,1))
atFilev2Entry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:atFilev2Entry.setStatus(_A)
_AtFilev2Filename_Type=OctetString
_AtFilev2Filename_Object=MibTableColumn
atFilev2Filename=_AtFilev2Filename_Object((1,3,6,1,4,1,207,8,4,4,4,600,2,1,1),_AtFilev2Filename_Type())
atFilev2Filename.setMaxAccess(_D)
if mibBuilder.loadTexts:atFilev2Filename.setStatus(_A)
_AtFilev2FileSize_Type=Integer32
_AtFilev2FileSize_Object=MibTableColumn
atFilev2FileSize=_AtFilev2FileSize_Object((1,3,6,1,4,1,207,8,4,4,4,600,2,1,2),_AtFilev2FileSize_Type())
atFilev2FileSize.setMaxAccess(_D)
if mibBuilder.loadTexts:atFilev2FileSize.setStatus(_A)
_AtFilev2FileCreationTime_Type=OctetString
_AtFilev2FileCreationTime_Object=MibTableColumn
atFilev2FileCreationTime=_AtFilev2FileCreationTime_Object((1,3,6,1,4,1,207,8,4,4,4,600,2,1,3),_AtFilev2FileCreationTime_Type())
atFilev2FileCreationTime.setMaxAccess(_D)
if mibBuilder.loadTexts:atFilev2FileCreationTime.setStatus(_A)
_AtFilev2FileAttribs_Type=OctetString
_AtFilev2FileAttribs_Object=MibTableColumn
atFilev2FileAttribs=_AtFilev2FileAttribs_Object((1,3,6,1,4,1,207,8,4,4,4,600,2,1,4),_AtFilev2FileAttribs_Type())
atFilev2FileAttribs.setMaxAccess(_D)
if mibBuilder.loadTexts:atFilev2FileAttribs.setStatus(_A)
_AtFilev2FileOperation_ObjectIdentity=ObjectIdentity
atFilev2FileOperation=_AtFilev2FileOperation_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,600,3))
_AtFilev2SourceStackID_Type=Integer32
_AtFilev2SourceStackID_Object=MibScalar
atFilev2SourceStackID=_AtFilev2SourceStackID_Object((1,3,6,1,4,1,207,8,4,4,4,600,3,1),_AtFilev2SourceStackID_Type())
atFilev2SourceStackID.setMaxAccess(_B)
if mibBuilder.loadTexts:atFilev2SourceStackID.setStatus(_A)
class _AtFilev2SourceDevice_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_AtFilev2SourceDevice_Type.__name__=_C
_AtFilev2SourceDevice_Object=MibScalar
atFilev2SourceDevice=_AtFilev2SourceDevice_Object((1,3,6,1,4,1,207,8,4,4,4,600,3,2),_AtFilev2SourceDevice_Type())
atFilev2SourceDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:atFilev2SourceDevice.setStatus(_A)
_AtFilev2SourceFilename_Type=DisplayString
_AtFilev2SourceFilename_Object=MibScalar
atFilev2SourceFilename=_AtFilev2SourceFilename_Object((1,3,6,1,4,1,207,8,4,4,4,600,3,3),_AtFilev2SourceFilename_Type())
atFilev2SourceFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:atFilev2SourceFilename.setStatus(_A)
_AtFilev2DestinationStackID_Type=Integer32
_AtFilev2DestinationStackID_Object=MibScalar
atFilev2DestinationStackID=_AtFilev2DestinationStackID_Object((1,3,6,1,4,1,207,8,4,4,4,600,3,4),_AtFilev2DestinationStackID_Type())
atFilev2DestinationStackID.setMaxAccess(_B)
if mibBuilder.loadTexts:atFilev2DestinationStackID.setStatus(_A)
class _AtFilev2DestinationDevice_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_AtFilev2DestinationDevice_Type.__name__=_C
_AtFilev2DestinationDevice_Object=MibScalar
atFilev2DestinationDevice=_AtFilev2DestinationDevice_Object((1,3,6,1,4,1,207,8,4,4,4,600,3,5),_AtFilev2DestinationDevice_Type())
atFilev2DestinationDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:atFilev2DestinationDevice.setStatus(_A)
_AtFilev2DestinationFilename_Type=DisplayString
_AtFilev2DestinationFilename_Object=MibScalar
atFilev2DestinationFilename=_AtFilev2DestinationFilename_Object((1,3,6,1,4,1,207,8,4,4,4,600,3,6),_AtFilev2DestinationFilename_Type())
atFilev2DestinationFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:atFilev2DestinationFilename.setStatus(_A)
_AtFilev2CopyBegin_Type=OctetString
_AtFilev2CopyBegin_Object=MibScalar
atFilev2CopyBegin=_AtFilev2CopyBegin_Object((1,3,6,1,4,1,207,8,4,4,4,600,3,7),_AtFilev2CopyBegin_Type())
atFilev2CopyBegin.setMaxAccess(_B)
if mibBuilder.loadTexts:atFilev2CopyBegin.setStatus(_A)
_AtFilev2MoveBegin_Type=OctetString
_AtFilev2MoveBegin_Object=MibScalar
atFilev2MoveBegin=_AtFilev2MoveBegin_Object((1,3,6,1,4,1,207,8,4,4,4,600,3,8),_AtFilev2MoveBegin_Type())
atFilev2MoveBegin.setMaxAccess(_B)
if mibBuilder.loadTexts:atFilev2MoveBegin.setStatus(_A)
_AtFilev2DeleteBegin_Type=OctetString
_AtFilev2DeleteBegin_Object=MibScalar
atFilev2DeleteBegin=_AtFilev2DeleteBegin_Object((1,3,6,1,4,1,207,8,4,4,4,600,3,9),_AtFilev2DeleteBegin_Type())
atFilev2DeleteBegin.setMaxAccess(_B)
if mibBuilder.loadTexts:atFilev2DeleteBegin.setStatus(_A)
_AtFilev2Flash1_ObjectIdentity=ObjectIdentity
atFilev2Flash1=_AtFilev2Flash1_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,600,3,10))
_AtFilev2Card2_ObjectIdentity=ObjectIdentity
atFilev2Card2=_AtFilev2Card2_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,600,3,11))
_AtFilev2Nvs3_ObjectIdentity=ObjectIdentity
atFilev2Nvs3=_AtFilev2Nvs3_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,600,3,12))
_AtFilev2Tftp4_ObjectIdentity=ObjectIdentity
atFilev2Tftp4=_AtFilev2Tftp4_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,600,3,13))
_AtFilev2TftpIPAddr_Type=IpAddress
_AtFilev2TftpIPAddr_Object=MibScalar
atFilev2TftpIPAddr=_AtFilev2TftpIPAddr_Object((1,3,6,1,4,1,207,8,4,4,4,600,3,13,1),_AtFilev2TftpIPAddr_Type())
atFilev2TftpIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:atFilev2TftpIPAddr.setStatus(_A)
_AtFilev2SDcardTable_Object=MibTable
atFilev2SDcardTable=_AtFilev2SDcardTable_Object((1,3,6,1,4,1,207,8,4,4,4,600,4))
if mibBuilder.loadTexts:atFilev2SDcardTable.setStatus(_A)
_AtFilev2SDcardEntry_Object=MibTableRow
atFilev2SDcardEntry=_AtFilev2SDcardEntry_Object((1,3,6,1,4,1,207,8,4,4,4,600,4,1))
atFilev2SDcardEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:atFilev2SDcardEntry.setStatus(_A)
_AtFilev2SDcardStackMemberId_Type=Unsigned32
_AtFilev2SDcardStackMemberId_Object=MibTableColumn
atFilev2SDcardStackMemberId=_AtFilev2SDcardStackMemberId_Object((1,3,6,1,4,1,207,8,4,4,4,600,4,1,1),_AtFilev2SDcardStackMemberId_Type())
atFilev2SDcardStackMemberId.setMaxAccess(_D)
if mibBuilder.loadTexts:atFilev2SDcardStackMemberId.setStatus(_A)
class _AtFilev2SDcardPresence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notPresent',1),('present',2)))
_AtFilev2SDcardPresence_Type.__name__=_C
_AtFilev2SDcardPresence_Object=MibTableColumn
atFilev2SDcardPresence=_AtFilev2SDcardPresence_Object((1,3,6,1,4,1,207,8,4,4,4,600,4,1,2),_AtFilev2SDcardPresence_Type())
atFilev2SDcardPresence.setMaxAccess(_D)
if mibBuilder.loadTexts:atFilev2SDcardPresence.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'atFilev2':atFilev2,'atFilev2TableOptions':atFilev2TableOptions,'atFilev2Recursive':atFilev2Recursive,'atFilev2AllFiles':atFilev2AllFiles,'atFilev2Device':atFilev2Device,'atFilev2StackID':atFilev2StackID,'atFilev2Table':atFilev2Table,'atFilev2Entry':atFilev2Entry,_F:atFilev2Filename,'atFilev2FileSize':atFilev2FileSize,'atFilev2FileCreationTime':atFilev2FileCreationTime,'atFilev2FileAttribs':atFilev2FileAttribs,'atFilev2FileOperation':atFilev2FileOperation,'atFilev2SourceStackID':atFilev2SourceStackID,'atFilev2SourceDevice':atFilev2SourceDevice,'atFilev2SourceFilename':atFilev2SourceFilename,'atFilev2DestinationStackID':atFilev2DestinationStackID,'atFilev2DestinationDevice':atFilev2DestinationDevice,'atFilev2DestinationFilename':atFilev2DestinationFilename,'atFilev2CopyBegin':atFilev2CopyBegin,'atFilev2MoveBegin':atFilev2MoveBegin,'atFilev2DeleteBegin':atFilev2DeleteBegin,'atFilev2Flash1':atFilev2Flash1,'atFilev2Card2':atFilev2Card2,'atFilev2Nvs3':atFilev2Nvs3,'atFilev2Tftp4':atFilev2Tftp4,'atFilev2TftpIPAddr':atFilev2TftpIPAddr,'atFilev2SDcardTable':atFilev2SDcardTable,'atFilev2SDcardEntry':atFilev2SDcardEntry,_G:atFilev2SDcardStackMemberId,'atFilev2SDcardPresence':atFilev2SDcardPresence})