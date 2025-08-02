_M='swFSDirectoryName'
_L='swFSDriveInfoStackIndex'
_K='swFSDriveInfoStackUnitID'
_J='not-accessible'
_I='swFSDriveInfoIndex'
_H='FILE-SYSTEM-MIB'
_G='start'
_F='none'
_E='read-only'
_D='Integer32'
_C='DisplayString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
swFileSystemMIB=ModuleIdentity((1,3,6,1,4,1,171,12,14))
_SwFSBasicInfo_ObjectIdentity=ObjectIdentity
swFSBasicInfo=_SwFSBasicInfo_ObjectIdentity((1,3,6,1,4,1,171,12,14,1))
class _SwFSBasicInfoCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*(('other',0),(_G,1),('finish',2),('in-process',3),('fail',4),('invalid-drive-name',5),('same-file-name',6),('root-area-full',7),('insufficient-disk',8),('invalid-directory',9),('file-readonly',10),('exist-same-directory',11),('exist-file-in-directory',12),('no-file-or-dir',13),('no-format',14),('no-storage-media',15),('fs-no-match-media',16),('error-input',17),('error-char',18),('error-filename',19),('access-media-error',20)))
_SwFSBasicInfoCtrlStatus_Type.__name__=_D
_SwFSBasicInfoCtrlStatus_Object=MibScalar
swFSBasicInfoCtrlStatus=_SwFSBasicInfoCtrlStatus_Object((1,3,6,1,4,1,171,12,14,1,1),_SwFSBasicInfoCtrlStatus_Type())
swFSBasicInfoCtrlStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:swFSBasicInfoCtrlStatus.setStatus(_A)
class _SwFSBasicInfoCtrlProcess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SwFSBasicInfoCtrlProcess_Type.__name__=_D
_SwFSBasicInfoCtrlProcess_Object=MibScalar
swFSBasicInfoCtrlProcess=_SwFSBasicInfoCtrlProcess_Object((1,3,6,1,4,1,171,12,14,1,2),_SwFSBasicInfoCtrlProcess_Type())
swFSBasicInfoCtrlProcess.setMaxAccess(_E)
if mibBuilder.loadTexts:swFSBasicInfoCtrlProcess.setStatus(_A)
if mibBuilder.loadTexts:swFSBasicInfoCtrlProcess.setUnits('%')
_SwFSDriveCtrl_ObjectIdentity=ObjectIdentity
swFSDriveCtrl=_SwFSDriveCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,14,2))
_SwFSDriveInfoTable_Object=MibTable
swFSDriveInfoTable=_SwFSDriveInfoTable_Object((1,3,6,1,4,1,171,12,14,2,1))
if mibBuilder.loadTexts:swFSDriveInfoTable.setStatus(_A)
_SwFSDriveInfoEntry_Object=MibTableRow
swFSDriveInfoEntry=_SwFSDriveInfoEntry_Object((1,3,6,1,4,1,171,12,14,2,1,1))
swFSDriveInfoEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:swFSDriveInfoEntry.setStatus(_A)
_SwFSDriveInfoIndex_Type=Integer32
_SwFSDriveInfoIndex_Object=MibTableColumn
swFSDriveInfoIndex=_SwFSDriveInfoIndex_Object((1,3,6,1,4,1,171,12,14,2,1,1,1),_SwFSDriveInfoIndex_Type())
swFSDriveInfoIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:swFSDriveInfoIndex.setStatus(_A)
class _SwFSDriveInfoDriveID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)));namedValues=NamedValues(*(('a',0),('b',1),('c',2),('d',3),('e',4),('f',5),('g',6),('h',7),('i',8),('j',9),('k',10),('l',11),('m',12),('n',13),('o',14),('p',15),('q',16),('r',17),('s',18),('t',19),('u',20),('v',21),('w',22),('x',23),('y',24),('z',25)))
_SwFSDriveInfoDriveID_Type.__name__=_D
_SwFSDriveInfoDriveID_Object=MibTableColumn
swFSDriveInfoDriveID=_SwFSDriveInfoDriveID_Object((1,3,6,1,4,1,171,12,14,2,1,1,2),_SwFSDriveInfoDriveID_Type())
swFSDriveInfoDriveID.setMaxAccess(_E)
if mibBuilder.loadTexts:swFSDriveInfoDriveID.setStatus(_A)
class _SwFSDriveInfoType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwFSDriveInfoType_Type.__name__=_C
_SwFSDriveInfoType_Object=MibTableColumn
swFSDriveInfoType=_SwFSDriveInfoType_Object((1,3,6,1,4,1,171,12,14,2,1,1,3),_SwFSDriveInfoType_Type())
swFSDriveInfoType.setMaxAccess(_E)
if mibBuilder.loadTexts:swFSDriveInfoType.setStatus(_A)
_SwFSDriveInfoSize_Type=Integer32
_SwFSDriveInfoSize_Object=MibTableColumn
swFSDriveInfoSize=_SwFSDriveInfoSize_Object((1,3,6,1,4,1,171,12,14,2,1,1,4),_SwFSDriveInfoSize_Type())
swFSDriveInfoSize.setMaxAccess(_E)
if mibBuilder.loadTexts:swFSDriveInfoSize.setStatus(_A)
class _SwFSDriveInfoPartition_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwFSDriveInfoPartition_Type.__name__=_C
_SwFSDriveInfoPartition_Object=MibTableColumn
swFSDriveInfoPartition=_SwFSDriveInfoPartition_Object((1,3,6,1,4,1,171,12,14,2,1,1,5),_SwFSDriveInfoPartition_Type())
swFSDriveInfoPartition.setMaxAccess(_E)
if mibBuilder.loadTexts:swFSDriveInfoPartition.setStatus(_A)
class _SwFSDriveInfoFStype_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwFSDriveInfoFStype_Type.__name__=_C
_SwFSDriveInfoFStype_Object=MibTableColumn
swFSDriveInfoFStype=_SwFSDriveInfoFStype_Object((1,3,6,1,4,1,171,12,14,2,1,1,6),_SwFSDriveInfoFStype_Type())
swFSDriveInfoFStype.setMaxAccess(_E)
if mibBuilder.loadTexts:swFSDriveInfoFStype.setStatus(_A)
_SwFSDriveFormatCtrl_ObjectIdentity=ObjectIdentity
swFSDriveFormatCtrl=_SwFSDriveFormatCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,14,2,2))
class _SwFSDriveFormatDriveID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)));namedValues=NamedValues(*((_F,0),('a',1),('b',2),('c',3),('d',4),('e',5),('f',6),('g',7),('h',8),('i',9),('j',10),('k',11),('l',12),('m',13),('n',14),('o',15),('p',16),('q',17),('r',18),('s',19),('t',20),('u',21),('v',22),('w',23),('x',24),('y',25),('z',26)))
_SwFSDriveFormatDriveID_Type.__name__=_D
_SwFSDriveFormatDriveID_Object=MibScalar
swFSDriveFormatDriveID=_SwFSDriveFormatDriveID_Object((1,3,6,1,4,1,171,12,14,2,2,1),_SwFSDriveFormatDriveID_Type())
swFSDriveFormatDriveID.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSDriveFormatDriveID.setStatus(_A)
class _SwFSDriveFormatFat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fat16',1),('fat32',2)))
_SwFSDriveFormatFat_Type.__name__=_D
_SwFSDriveFormatFat_Object=MibScalar
swFSDriveFormatFat=_SwFSDriveFormatFat_Object((1,3,6,1,4,1,171,12,14,2,2,2),_SwFSDriveFormatFat_Type())
swFSDriveFormatFat.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSDriveFormatFat.setStatus(_A)
class _SwFSDriveFormatLabelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_SwFSDriveFormatLabelName_Type.__name__=_C
_SwFSDriveFormatLabelName_Object=MibScalar
swFSDriveFormatLabelName=_SwFSDriveFormatLabelName_Object((1,3,6,1,4,1,171,12,14,2,2,3),_SwFSDriveFormatLabelName_Type())
swFSDriveFormatLabelName.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSDriveFormatLabelName.setStatus(_A)
class _SwFSDriveFormatType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fast',1),('full',2),('full-with-mbr',3)))
_SwFSDriveFormatType_Type.__name__=_D
_SwFSDriveFormatType_Object=MibScalar
swFSDriveFormatType=_SwFSDriveFormatType_Object((1,3,6,1,4,1,171,12,14,2,2,4),_SwFSDriveFormatType_Type())
swFSDriveFormatType.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSDriveFormatType.setStatus(_A)
class _SwFSDriveFormatActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwFSDriveFormatActivity_Type.__name__=_D
_SwFSDriveFormatActivity_Object=MibScalar
swFSDriveFormatActivity=_SwFSDriveFormatActivity_Object((1,3,6,1,4,1,171,12,14,2,2,5),_SwFSDriveFormatActivity_Type())
swFSDriveFormatActivity.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSDriveFormatActivity.setStatus(_A)
_SwFSDriveChangeCtrl_ObjectIdentity=ObjectIdentity
swFSDriveChangeCtrl=_SwFSDriveChangeCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,14,2,3))
_SwFSDriveChangeUnitID_Type=Integer32
_SwFSDriveChangeUnitID_Object=MibScalar
swFSDriveChangeUnitID=_SwFSDriveChangeUnitID_Object((1,3,6,1,4,1,171,12,14,2,3,1),_SwFSDriveChangeUnitID_Type())
swFSDriveChangeUnitID.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSDriveChangeUnitID.setStatus(_A)
class _SwFSDriveChangeDriveID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)));namedValues=NamedValues(*((_F,1),('a',2),('b',3),('c',4),('d',5),('e',6),('f',7),('g',8),('h',9),('i',10),('j',11),('k',12),('l',13),('m',14),('n',15),('o',16),('p',17),('q',18),('r',19),('s',20),('t',21),('u',22),('v',23),('w',24),('x',25),('y',26),('z',27)))
_SwFSDriveChangeDriveID_Type.__name__=_D
_SwFSDriveChangeDriveID_Object=MibScalar
swFSDriveChangeDriveID=_SwFSDriveChangeDriveID_Object((1,3,6,1,4,1,171,12,14,2,3,2),_SwFSDriveChangeDriveID_Type())
swFSDriveChangeDriveID.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSDriveChangeDriveID.setStatus(_A)
class _SwFSDriveCurrentDirectory_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwFSDriveCurrentDirectory_Type.__name__=_C
_SwFSDriveCurrentDirectory_Object=MibScalar
swFSDriveCurrentDirectory=_SwFSDriveCurrentDirectory_Object((1,3,6,1,4,1,171,12,14,2,3,3),_SwFSDriveCurrentDirectory_Type())
swFSDriveCurrentDirectory.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSDriveCurrentDirectory.setStatus(_A)
_SwFSDriveInfoStackTable_Object=MibTable
swFSDriveInfoStackTable=_SwFSDriveInfoStackTable_Object((1,3,6,1,4,1,171,12,14,2,4))
if mibBuilder.loadTexts:swFSDriveInfoStackTable.setStatus(_A)
_SwFSDriveInfoStackEntry_Object=MibTableRow
swFSDriveInfoStackEntry=_SwFSDriveInfoStackEntry_Object((1,3,6,1,4,1,171,12,14,2,4,1))
swFSDriveInfoStackEntry.setIndexNames((0,_H,_K),(0,_H,_L))
if mibBuilder.loadTexts:swFSDriveInfoStackEntry.setStatus(_A)
_SwFSDriveInfoStackUnitID_Type=Integer32
_SwFSDriveInfoStackUnitID_Object=MibTableColumn
swFSDriveInfoStackUnitID=_SwFSDriveInfoStackUnitID_Object((1,3,6,1,4,1,171,12,14,2,4,1,1),_SwFSDriveInfoStackUnitID_Type())
swFSDriveInfoStackUnitID.setMaxAccess(_E)
if mibBuilder.loadTexts:swFSDriveInfoStackUnitID.setStatus(_A)
_SwFSDriveInfoStackIndex_Type=Integer32
_SwFSDriveInfoStackIndex_Object=MibTableColumn
swFSDriveInfoStackIndex=_SwFSDriveInfoStackIndex_Object((1,3,6,1,4,1,171,12,14,2,4,1,2),_SwFSDriveInfoStackIndex_Type())
swFSDriveInfoStackIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:swFSDriveInfoStackIndex.setStatus(_A)
class _SwFSDriveInfoStackDriveID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)));namedValues=NamedValues(*(('a',1),('b',2),('c',3),('d',4),('e',5),('f',6),('g',7),('h',8),('i',9),('j',10),('k',11),('l',12),('m',13),('n',14),('o',15),('p',16),('q',17),('r',18),('s',19),('t',20),('u',21),('v',22),('w',23),('x',24),('y',25),('z',26)))
_SwFSDriveInfoStackDriveID_Type.__name__=_D
_SwFSDriveInfoStackDriveID_Object=MibTableColumn
swFSDriveInfoStackDriveID=_SwFSDriveInfoStackDriveID_Object((1,3,6,1,4,1,171,12,14,2,4,1,3),_SwFSDriveInfoStackDriveID_Type())
swFSDriveInfoStackDriveID.setMaxAccess(_E)
if mibBuilder.loadTexts:swFSDriveInfoStackDriveID.setStatus(_A)
class _SwFSDriveInfoStackType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwFSDriveInfoStackType_Type.__name__=_C
_SwFSDriveInfoStackType_Object=MibTableColumn
swFSDriveInfoStackType=_SwFSDriveInfoStackType_Object((1,3,6,1,4,1,171,12,14,2,4,1,4),_SwFSDriveInfoStackType_Type())
swFSDriveInfoStackType.setMaxAccess(_E)
if mibBuilder.loadTexts:swFSDriveInfoStackType.setStatus(_A)
_SwFSDriveInfoStackSize_Type=Integer32
_SwFSDriveInfoStackSize_Object=MibTableColumn
swFSDriveInfoStackSize=_SwFSDriveInfoStackSize_Object((1,3,6,1,4,1,171,12,14,2,4,1,5),_SwFSDriveInfoStackSize_Type())
swFSDriveInfoStackSize.setMaxAccess(_E)
if mibBuilder.loadTexts:swFSDriveInfoStackSize.setStatus(_A)
class _SwFSDriveInfoStackPartition_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwFSDriveInfoStackPartition_Type.__name__=_C
_SwFSDriveInfoStackPartition_Object=MibTableColumn
swFSDriveInfoStackPartition=_SwFSDriveInfoStackPartition_Object((1,3,6,1,4,1,171,12,14,2,4,1,6),_SwFSDriveInfoStackPartition_Type())
swFSDriveInfoStackPartition.setMaxAccess(_E)
if mibBuilder.loadTexts:swFSDriveInfoStackPartition.setStatus(_A)
class _SwFSDriveInfoStackFStype_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwFSDriveInfoStackFStype_Type.__name__=_C
_SwFSDriveInfoStackFStype_Object=MibTableColumn
swFSDriveInfoStackFStype=_SwFSDriveInfoStackFStype_Object((1,3,6,1,4,1,171,12,14,2,4,1,7),_SwFSDriveInfoStackFStype_Type())
swFSDriveInfoStackFStype.setMaxAccess(_E)
if mibBuilder.loadTexts:swFSDriveInfoStackFStype.setStatus(_A)
_SwFSDirectoryCtrl_ObjectIdentity=ObjectIdentity
swFSDirectoryCtrl=_SwFSDirectoryCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,14,3))
class _SwFSDirectoryMake_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwFSDirectoryMake_Type.__name__=_C
_SwFSDirectoryMake_Object=MibScalar
swFSDirectoryMake=_SwFSDirectoryMake_Object((1,3,6,1,4,1,171,12,14,3,1),_SwFSDirectoryMake_Type())
swFSDirectoryMake.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSDirectoryMake.setStatus(_A)
class _SwFSDirectoryDel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwFSDirectoryDel_Type.__name__=_C
_SwFSDirectoryDel_Object=MibScalar
swFSDirectoryDel=_SwFSDirectoryDel_Object((1,3,6,1,4,1,171,12,14,3,2),_SwFSDirectoryDel_Type())
swFSDirectoryDel.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSDirectoryDel.setStatus(_A)
_SwFSctrlDirectoryDir_ObjectIdentity=ObjectIdentity
swFSctrlDirectoryDir=_SwFSctrlDirectoryDir_ObjectIdentity((1,3,6,1,4,1,171,12,14,3,3))
class _SwFSDirectoryPath_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwFSDirectoryPath_Type.__name__=_C
_SwFSDirectoryPath_Object=MibScalar
swFSDirectoryPath=_SwFSDirectoryPath_Object((1,3,6,1,4,1,171,12,14,3,3,1),_SwFSDirectoryPath_Type())
swFSDirectoryPath.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSDirectoryPath.setStatus(_A)
_SwFSDirectoryTable_Object=MibTable
swFSDirectoryTable=_SwFSDirectoryTable_Object((1,3,6,1,4,1,171,12,14,3,3,2))
if mibBuilder.loadTexts:swFSDirectoryTable.setStatus(_A)
_SwFSDirectoryEntry_Object=MibTableRow
swFSDirectoryEntry=_SwFSDirectoryEntry_Object((1,3,6,1,4,1,171,12,14,3,3,2,1))
swFSDirectoryEntry.setIndexNames((0,_H,_M))
if mibBuilder.loadTexts:swFSDirectoryEntry.setStatus(_A)
class _SwFSDirectoryName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwFSDirectoryName_Type.__name__=_C
_SwFSDirectoryName_Object=MibTableColumn
swFSDirectoryName=_SwFSDirectoryName_Object((1,3,6,1,4,1,171,12,14,3,3,2,1,1),_SwFSDirectoryName_Type())
swFSDirectoryName.setMaxAccess(_E)
if mibBuilder.loadTexts:swFSDirectoryName.setStatus(_A)
class _SwFSDirectoryAttr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dir',1),('file',2)))
_SwFSDirectoryAttr_Type.__name__=_D
_SwFSDirectoryAttr_Object=MibTableColumn
swFSDirectoryAttr=_SwFSDirectoryAttr_Object((1,3,6,1,4,1,171,12,14,3,3,2,1,2),_SwFSDirectoryAttr_Type())
swFSDirectoryAttr.setMaxAccess(_E)
if mibBuilder.loadTexts:swFSDirectoryAttr.setStatus(_A)
class _SwFSDirectoryTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwFSDirectoryTime_Type.__name__=_C
_SwFSDirectoryTime_Object=MibTableColumn
swFSDirectoryTime=_SwFSDirectoryTime_Object((1,3,6,1,4,1,171,12,14,3,3,2,1,3),_SwFSDirectoryTime_Type())
swFSDirectoryTime.setMaxAccess(_E)
if mibBuilder.loadTexts:swFSDirectoryTime.setStatus(_A)
_SwFSDirectorySize_Type=Integer32
_SwFSDirectorySize_Object=MibTableColumn
swFSDirectorySize=_SwFSDirectorySize_Object((1,3,6,1,4,1,171,12,14,3,3,2,1,4),_SwFSDirectorySize_Type())
swFSDirectorySize.setMaxAccess(_E)
if mibBuilder.loadTexts:swFSDirectorySize.setStatus(_A)
if mibBuilder.loadTexts:swFSDirectorySize.setUnits('bytes')
_SwFSFileCtrl_ObjectIdentity=ObjectIdentity
swFSFileCtrl=_SwFSFileCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,14,4))
_SwFSFileRename_ObjectIdentity=ObjectIdentity
swFSFileRename=_SwFSFileRename_ObjectIdentity((1,3,6,1,4,1,171,12,14,4,1))
class _SwFSFileSourceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwFSFileSourceName_Type.__name__=_C
_SwFSFileSourceName_Object=MibScalar
swFSFileSourceName=_SwFSFileSourceName_Object((1,3,6,1,4,1,171,12,14,4,1,1),_SwFSFileSourceName_Type())
swFSFileSourceName.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSFileSourceName.setStatus(_A)
class _SwFSFileTargetName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwFSFileTargetName_Type.__name__=_C
_SwFSFileTargetName_Object=MibScalar
swFSFileTargetName=_SwFSFileTargetName_Object((1,3,6,1,4,1,171,12,14,4,1,2),_SwFSFileTargetName_Type())
swFSFileTargetName.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSFileTargetName.setStatus(_A)
class _SwFSFileRenameActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwFSFileRenameActivity_Type.__name__=_D
_SwFSFileRenameActivity_Object=MibScalar
swFSFileRenameActivity=_SwFSFileRenameActivity_Object((1,3,6,1,4,1,171,12,14,4,1,3),_SwFSFileRenameActivity_Type())
swFSFileRenameActivity.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSFileRenameActivity.setStatus(_A)
_SwFSFileDel_ObjectIdentity=ObjectIdentity
swFSFileDel=_SwFSFileDel_ObjectIdentity((1,3,6,1,4,1,171,12,14,4,2))
class _SwFSFileDelName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwFSFileDelName_Type.__name__=_C
_SwFSFileDelName_Object=MibScalar
swFSFileDelName=_SwFSFileDelName_Object((1,3,6,1,4,1,171,12,14,4,2,1),_SwFSFileDelName_Type())
swFSFileDelName.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSFileDelName.setStatus(_A)
class _SwFSFileDelOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('recursive',2)))
_SwFSFileDelOption_Type.__name__=_D
_SwFSFileDelOption_Object=MibScalar
swFSFileDelOption=_SwFSFileDelOption_Object((1,3,6,1,4,1,171,12,14,4,2,2),_SwFSFileDelOption_Type())
swFSFileDelOption.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSFileDelOption.setStatus(_A)
class _SwFSFileDelActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwFSFileDelActivity_Type.__name__=_D
_SwFSFileDelActivity_Object=MibScalar
swFSFileDelActivity=_SwFSFileDelActivity_Object((1,3,6,1,4,1,171,12,14,4,2,3),_SwFSFileDelActivity_Type())
swFSFileDelActivity.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSFileDelActivity.setStatus(_A)
_SwFSCopyCtrl_ObjectIdentity=ObjectIdentity
swFSCopyCtrl=_SwFSCopyCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,14,5))
class _SwFSCopySourceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwFSCopySourceName_Type.__name__=_C
_SwFSCopySourceName_Object=MibScalar
swFSCopySourceName=_SwFSCopySourceName_Object((1,3,6,1,4,1,171,12,14,5,1),_SwFSCopySourceName_Type())
swFSCopySourceName.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSCopySourceName.setStatus(_A)
class _SwFSCopyDestinationName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwFSCopyDestinationName_Type.__name__=_C
_SwFSCopyDestinationName_Object=MibScalar
swFSCopyDestinationName=_SwFSCopyDestinationName_Object((1,3,6,1,4,1,171,12,14,5,2),_SwFSCopyDestinationName_Type())
swFSCopyDestinationName.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSCopyDestinationName.setStatus(_A)
class _SwFSCopyActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_F,1),(_G,2),('file-to-file',3),('file-to-image',4),('file-to-config',5),('file-to-prom',6),('image-to-file',7),('config-to-file',8),('log-to-file',9),('prom-to-file',10)))
_SwFSCopyActivity_Type.__name__=_D
_SwFSCopyActivity_Object=MibScalar
swFSCopyActivity=_SwFSCopyActivity_Object((1,3,6,1,4,1,171,12,14,5,3),_SwFSCopyActivity_Type())
swFSCopyActivity.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSCopyActivity.setStatus(_A)
_SwFSCopyDestinationUnitID_Type=Integer32
_SwFSCopyDestinationUnitID_Object=MibScalar
swFSCopyDestinationUnitID=_SwFSCopyDestinationUnitID_Object((1,3,6,1,4,1,171,12,14,5,4),_SwFSCopyDestinationUnitID_Type())
swFSCopyDestinationUnitID.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSCopyDestinationUnitID.setStatus(_A)
class _SwFSCopyDestinationDriveID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)));namedValues=NamedValues(*((_F,1),('a',2),('b',3),('c',4),('d',5),('e',6),('f',7),('g',8),('h',9),('i',10),('j',11),('k',12),('l',13),('m',14),('n',15),('o',16),('p',17),('q',18),('r',19),('s',20),('t',21),('u',22),('v',23),('w',24),('x',25),('y',26),('z',27)))
_SwFSCopyDestinationDriveID_Type.__name__=_D
_SwFSCopyDestinationDriveID_Object=MibScalar
swFSCopyDestinationDriveID=_SwFSCopyDestinationDriveID_Object((1,3,6,1,4,1,171,12,14,5,5),_SwFSCopyDestinationDriveID_Type())
swFSCopyDestinationDriveID.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSCopyDestinationDriveID.setStatus(_A)
_SwFSCopyConfigID_Type=Integer32
_SwFSCopyConfigID_Object=MibScalar
swFSCopyConfigID=_SwFSCopyConfigID_Object((1,3,6,1,4,1,171,12,14,5,6),_SwFSCopyConfigID_Type())
swFSCopyConfigID.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSCopyConfigID.setStatus(_A)
_SwFSCopyImageID_Type=Integer32
_SwFSCopyImageID_Object=MibScalar
swFSCopyImageID=_SwFSCopyImageID_Object((1,3,6,1,4,1,171,12,14,5,7),_SwFSCopyImageID_Type())
swFSCopyImageID.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSCopyImageID.setStatus(_A)
_SwFSMoveCtrl_ObjectIdentity=ObjectIdentity
swFSMoveCtrl=_SwFSMoveCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,14,6))
class _SwFSMoveSourceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwFSMoveSourceName_Type.__name__=_C
_SwFSMoveSourceName_Object=MibScalar
swFSMoveSourceName=_SwFSMoveSourceName_Object((1,3,6,1,4,1,171,12,14,6,1),_SwFSMoveSourceName_Type())
swFSMoveSourceName.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSMoveSourceName.setStatus(_A)
_SwFSMoveDestinationUnitID_Type=Integer32
_SwFSMoveDestinationUnitID_Object=MibScalar
swFSMoveDestinationUnitID=_SwFSMoveDestinationUnitID_Object((1,3,6,1,4,1,171,12,14,6,2),_SwFSMoveDestinationUnitID_Type())
swFSMoveDestinationUnitID.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSMoveDestinationUnitID.setStatus(_A)
class _SwFSMoveDestinationDriveID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)));namedValues=NamedValues(*((_F,1),('a',2),('b',3),('c',4),('d',5),('e',6),('f',7),('g',8),('h',9),('i',10),('j',11),('k',12),('l',13),('m',14),('n',15),('o',16),('p',17),('q',18),('r',19),('s',20),('t',21),('u',22),('v',23),('w',24),('x',25),('y',26),('z',27)))
_SwFSMoveDestinationDriveID_Type.__name__=_D
_SwFSMoveDestinationDriveID_Object=MibScalar
swFSMoveDestinationDriveID=_SwFSMoveDestinationDriveID_Object((1,3,6,1,4,1,171,12,14,6,3),_SwFSMoveDestinationDriveID_Type())
swFSMoveDestinationDriveID.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSMoveDestinationDriveID.setStatus(_A)
class _SwFSMoveDestinationName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwFSMoveDestinationName_Type.__name__=_C
_SwFSMoveDestinationName_Object=MibScalar
swFSMoveDestinationName=_SwFSMoveDestinationName_Object((1,3,6,1,4,1,171,12,14,6,4),_SwFSMoveDestinationName_Type())
swFSMoveDestinationName.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSMoveDestinationName.setStatus(_A)
class _SwFSMoveActivity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwFSMoveActivity_Type.__name__=_D
_SwFSMoveActivity_Object=MibScalar
swFSMoveActivity=_SwFSMoveActivity_Object((1,3,6,1,4,1,171,12,14,6,5),_SwFSMoveActivity_Type())
swFSMoveActivity.setMaxAccess(_B)
if mibBuilder.loadTexts:swFSMoveActivity.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'swFileSystemMIB':swFileSystemMIB,'swFSBasicInfo':swFSBasicInfo,'swFSBasicInfoCtrlStatus':swFSBasicInfoCtrlStatus,'swFSBasicInfoCtrlProcess':swFSBasicInfoCtrlProcess,'swFSDriveCtrl':swFSDriveCtrl,'swFSDriveInfoTable':swFSDriveInfoTable,'swFSDriveInfoEntry':swFSDriveInfoEntry,_I:swFSDriveInfoIndex,'swFSDriveInfoDriveID':swFSDriveInfoDriveID,'swFSDriveInfoType':swFSDriveInfoType,'swFSDriveInfoSize':swFSDriveInfoSize,'swFSDriveInfoPartition':swFSDriveInfoPartition,'swFSDriveInfoFStype':swFSDriveInfoFStype,'swFSDriveFormatCtrl':swFSDriveFormatCtrl,'swFSDriveFormatDriveID':swFSDriveFormatDriveID,'swFSDriveFormatFat':swFSDriveFormatFat,'swFSDriveFormatLabelName':swFSDriveFormatLabelName,'swFSDriveFormatType':swFSDriveFormatType,'swFSDriveFormatActivity':swFSDriveFormatActivity,'swFSDriveChangeCtrl':swFSDriveChangeCtrl,'swFSDriveChangeUnitID':swFSDriveChangeUnitID,'swFSDriveChangeDriveID':swFSDriveChangeDriveID,'swFSDriveCurrentDirectory':swFSDriveCurrentDirectory,'swFSDriveInfoStackTable':swFSDriveInfoStackTable,'swFSDriveInfoStackEntry':swFSDriveInfoStackEntry,_K:swFSDriveInfoStackUnitID,_L:swFSDriveInfoStackIndex,'swFSDriveInfoStackDriveID':swFSDriveInfoStackDriveID,'swFSDriveInfoStackType':swFSDriveInfoStackType,'swFSDriveInfoStackSize':swFSDriveInfoStackSize,'swFSDriveInfoStackPartition':swFSDriveInfoStackPartition,'swFSDriveInfoStackFStype':swFSDriveInfoStackFStype,'swFSDirectoryCtrl':swFSDirectoryCtrl,'swFSDirectoryMake':swFSDirectoryMake,'swFSDirectoryDel':swFSDirectoryDel,'swFSctrlDirectoryDir':swFSctrlDirectoryDir,'swFSDirectoryPath':swFSDirectoryPath,'swFSDirectoryTable':swFSDirectoryTable,'swFSDirectoryEntry':swFSDirectoryEntry,_M:swFSDirectoryName,'swFSDirectoryAttr':swFSDirectoryAttr,'swFSDirectoryTime':swFSDirectoryTime,'swFSDirectorySize':swFSDirectorySize,'swFSFileCtrl':swFSFileCtrl,'swFSFileRename':swFSFileRename,'swFSFileSourceName':swFSFileSourceName,'swFSFileTargetName':swFSFileTargetName,'swFSFileRenameActivity':swFSFileRenameActivity,'swFSFileDel':swFSFileDel,'swFSFileDelName':swFSFileDelName,'swFSFileDelOption':swFSFileDelOption,'swFSFileDelActivity':swFSFileDelActivity,'swFSCopyCtrl':swFSCopyCtrl,'swFSCopySourceName':swFSCopySourceName,'swFSCopyDestinationName':swFSCopyDestinationName,'swFSCopyActivity':swFSCopyActivity,'swFSCopyDestinationUnitID':swFSCopyDestinationUnitID,'swFSCopyDestinationDriveID':swFSCopyDestinationDriveID,'swFSCopyConfigID':swFSCopyConfigID,'swFSCopyImageID':swFSCopyImageID,'swFSMoveCtrl':swFSMoveCtrl,'swFSMoveSourceName':swFSMoveSourceName,'swFSMoveDestinationUnitID':swFSMoveDestinationUnitID,'swFSMoveDestinationDriveID':swFSMoveDestinationDriveID,'swFSMoveDestinationName':swFSMoveDestinationName,'swFSMoveActivity':swFSMoveActivity})