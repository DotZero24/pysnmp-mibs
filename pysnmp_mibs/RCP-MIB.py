_M='swRCPServerConfigIndex'
_L='swRCPFileSystemIndex'
_K='read-only'
_J='download'
_I='upload'
_H='swRCPFileIndex'
_G='not-accessible'
_F='other'
_E='RCP-MIB'
_D='Integer32'
_C='DisplayString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention','TruthValue')
swRCPMIB=ModuleIdentity((1,3,6,1,4,1,171,12,82))
class UnitList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_SwRCPMgmt_ObjectIdentity=ObjectIdentity
swRCPMgmt=_SwRCPMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,82,1))
_SwRCPFileTable_Object=MibTable
swRCPFileTable=_SwRCPFileTable_Object((1,3,6,1,4,1,171,12,82,1,1))
if mibBuilder.loadTexts:swRCPFileTable.setStatus(_A)
_SwRCPFileEntry_Object=MibTableRow
swRCPFileEntry=_SwRCPFileEntry_Object((1,3,6,1,4,1,171,12,82,1,1,1))
swRCPFileEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:swRCPFileEntry.setStatus(_A)
_SwRCPFileIndex_Type=Integer32
_SwRCPFileIndex_Object=MibTableColumn
swRCPFileIndex=_SwRCPFileIndex_Object((1,3,6,1,4,1,171,12,82,1,1,1,1),_SwRCPFileIndex_Type())
swRCPFileIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:swRCPFileIndex.setStatus(_A)
class _SwRCPFileLoadType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3)))
_SwRCPFileLoadType_Type.__name__=_D
_SwRCPFileLoadType_Object=MibTableColumn
swRCPFileLoadType=_SwRCPFileLoadType_Object((1,3,6,1,4,1,171,12,82,1,1,1,2),_SwRCPFileLoadType_Type())
swRCPFileLoadType.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPFileLoadType.setStatus(_A)
class _SwRCPFileType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwRCPFileType_Type.__name__=_C
_SwRCPFileType_Object=MibTableColumn
swRCPFileType=_SwRCPFileType_Object((1,3,6,1,4,1,171,12,82,1,1,1,3),_SwRCPFileType_Type())
swRCPFileType.setMaxAccess(_K)
if mibBuilder.loadTexts:swRCPFileType.setStatus(_A)
class _SwRCPFileServerUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_SwRCPFileServerUserName_Type.__name__=_C
_SwRCPFileServerUserName_Object=MibTableColumn
swRCPFileServerUserName=_SwRCPFileServerUserName_Object((1,3,6,1,4,1,171,12,82,1,1,1,4),_SwRCPFileServerUserName_Type())
swRCPFileServerUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPFileServerUserName.setStatus(_A)
_SwRCPFileServerAddrType_Type=InetAddressType
_SwRCPFileServerAddrType_Object=MibTableColumn
swRCPFileServerAddrType=_SwRCPFileServerAddrType_Object((1,3,6,1,4,1,171,12,82,1,1,1,5),_SwRCPFileServerAddrType_Type())
swRCPFileServerAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPFileServerAddrType.setStatus(_A)
_SwRCPFileServerAddr_Type=InetAddress
_SwRCPFileServerAddr_Object=MibTableColumn
swRCPFileServerAddr=_SwRCPFileServerAddr_Object((1,3,6,1,4,1,171,12,82,1,1,1,6),_SwRCPFileServerAddr_Type())
swRCPFileServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPFileServerAddr.setStatus(_A)
class _SwRCPFileServerPathFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwRCPFileServerPathFileName_Type.__name__=_C
_SwRCPFileServerPathFileName_Object=MibTableColumn
swRCPFileServerPathFileName=_SwRCPFileServerPathFileName_Object((1,3,6,1,4,1,171,12,82,1,1,1,7),_SwRCPFileServerPathFileName_Type())
swRCPFileServerPathFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPFileServerPathFileName.setStatus(_A)
_SwRCPFileUnitID_Type=UnitList
_SwRCPFileUnitID_Object=MibTableColumn
swRCPFileUnitID=_SwRCPFileUnitID_Object((1,3,6,1,4,1,171,12,82,1,1,1,8),_SwRCPFileUnitID_Type())
swRCPFileUnitID.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPFileUnitID.setStatus(_A)
_SwRCPFileCtrlID_Type=Integer32
_SwRCPFileCtrlID_Object=MibTableColumn
swRCPFileCtrlID=_SwRCPFileCtrlID_Object((1,3,6,1,4,1,171,12,82,1,1,1,9),_SwRCPFileCtrlID_Type())
swRCPFileCtrlID.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPFileCtrlID.setStatus(_A)
_SwRCPFileBootUpImage_Type=TruthValue
_SwRCPFileBootUpImage_Object=MibTableColumn
swRCPFileBootUpImage=_SwRCPFileBootUpImage_Object((1,3,6,1,4,1,171,12,82,1,1,1,10),_SwRCPFileBootUpImage_Type())
swRCPFileBootUpImage.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPFileBootUpImage.setStatus(_A)
_SwRCPFileForceAgree_Type=TruthValue
_SwRCPFileForceAgree_Object=MibTableColumn
swRCPFileForceAgree=_SwRCPFileForceAgree_Object((1,3,6,1,4,1,171,12,82,1,1,1,11),_SwRCPFileForceAgree_Type())
swRCPFileForceAgree.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPFileForceAgree.setStatus(_A)
class _SwRCPFileCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('start',2)))
_SwRCPFileCtrl_Type.__name__=_D
_SwRCPFileCtrl_Object=MibTableColumn
swRCPFileCtrl=_SwRCPFileCtrl_Object((1,3,6,1,4,1,171,12,82,1,1,1,12),_SwRCPFileCtrl_Type())
swRCPFileCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPFileCtrl.setStatus(_A)
_SwRCPFileSystemTable_Object=MibTable
swRCPFileSystemTable=_SwRCPFileSystemTable_Object((1,3,6,1,4,1,171,12,82,1,2))
if mibBuilder.loadTexts:swRCPFileSystemTable.setStatus(_A)
_SwRCPFileSystemEntry_Object=MibTableRow
swRCPFileSystemEntry=_SwRCPFileSystemEntry_Object((1,3,6,1,4,1,171,12,82,1,2,1))
swRCPFileSystemEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:swRCPFileSystemEntry.setStatus(_A)
_SwRCPFileSystemIndex_Type=Integer32
_SwRCPFileSystemIndex_Object=MibTableColumn
swRCPFileSystemIndex=_SwRCPFileSystemIndex_Object((1,3,6,1,4,1,171,12,82,1,2,1,1),_SwRCPFileSystemIndex_Type())
swRCPFileSystemIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:swRCPFileSystemIndex.setStatus(_A)
class _SwRCPFileSystemLoadType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_I,2),(_J,3)))
_SwRCPFileSystemLoadType_Type.__name__=_D
_SwRCPFileSystemLoadType_Object=MibTableColumn
swRCPFileSystemLoadType=_SwRCPFileSystemLoadType_Object((1,3,6,1,4,1,171,12,82,1,2,1,2),_SwRCPFileSystemLoadType_Type())
swRCPFileSystemLoadType.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPFileSystemLoadType.setStatus(_A)
class _SwRCPFileSystemFileType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwRCPFileSystemFileType_Type.__name__=_C
_SwRCPFileSystemFileType_Object=MibTableColumn
swRCPFileSystemFileType=_SwRCPFileSystemFileType_Object((1,3,6,1,4,1,171,12,82,1,2,1,3),_SwRCPFileSystemFileType_Type())
swRCPFileSystemFileType.setMaxAccess(_K)
if mibBuilder.loadTexts:swRCPFileSystemFileType.setStatus(_A)
class _SwRCPFileSystemServerUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_SwRCPFileSystemServerUserName_Type.__name__=_C
_SwRCPFileSystemServerUserName_Object=MibTableColumn
swRCPFileSystemServerUserName=_SwRCPFileSystemServerUserName_Object((1,3,6,1,4,1,171,12,82,1,2,1,4),_SwRCPFileSystemServerUserName_Type())
swRCPFileSystemServerUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPFileSystemServerUserName.setStatus(_A)
_SwRCPFileSystemServerAddrType_Type=InetAddressType
_SwRCPFileSystemServerAddrType_Object=MibTableColumn
swRCPFileSystemServerAddrType=_SwRCPFileSystemServerAddrType_Object((1,3,6,1,4,1,171,12,82,1,2,1,5),_SwRCPFileSystemServerAddrType_Type())
swRCPFileSystemServerAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPFileSystemServerAddrType.setStatus(_A)
_SwRCPFileSystemServerAddr_Type=InetAddress
_SwRCPFileSystemServerAddr_Object=MibTableColumn
swRCPFileSystemServerAddr=_SwRCPFileSystemServerAddr_Object((1,3,6,1,4,1,171,12,82,1,2,1,6),_SwRCPFileSystemServerAddr_Type())
swRCPFileSystemServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPFileSystemServerAddr.setStatus(_A)
class _SwRCPFileSystemServerPathFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwRCPFileSystemServerPathFileName_Type.__name__=_C
_SwRCPFileSystemServerPathFileName_Object=MibTableColumn
swRCPFileSystemServerPathFileName=_SwRCPFileSystemServerPathFileName_Object((1,3,6,1,4,1,171,12,82,1,2,1,7),_SwRCPFileSystemServerPathFileName_Type())
swRCPFileSystemServerPathFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPFileSystemServerPathFileName.setStatus(_A)
class _SwRCPFileSystemDevicePathFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SwRCPFileSystemDevicePathFileName_Type.__name__=_C
_SwRCPFileSystemDevicePathFileName_Object=MibTableColumn
swRCPFileSystemDevicePathFileName=_SwRCPFileSystemDevicePathFileName_Object((1,3,6,1,4,1,171,12,82,1,2,1,8),_SwRCPFileSystemDevicePathFileName_Type())
swRCPFileSystemDevicePathFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPFileSystemDevicePathFileName.setStatus(_A)
_SwRCPFileSystemUnitID_Type=UnitList
_SwRCPFileSystemUnitID_Object=MibTableColumn
swRCPFileSystemUnitID=_SwRCPFileSystemUnitID_Object((1,3,6,1,4,1,171,12,82,1,2,1,9),_SwRCPFileSystemUnitID_Type())
swRCPFileSystemUnitID.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPFileSystemUnitID.setStatus(_A)
_SwRCPFileSystemBootUpImage_Type=TruthValue
_SwRCPFileSystemBootUpImage_Object=MibTableColumn
swRCPFileSystemBootUpImage=_SwRCPFileSystemBootUpImage_Object((1,3,6,1,4,1,171,12,82,1,2,1,10),_SwRCPFileSystemBootUpImage_Type())
swRCPFileSystemBootUpImage.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPFileSystemBootUpImage.setStatus(_A)
_SwRCPFileSystemForceAgree_Type=TruthValue
_SwRCPFileSystemForceAgree_Object=MibTableColumn
swRCPFileSystemForceAgree=_SwRCPFileSystemForceAgree_Object((1,3,6,1,4,1,171,12,82,1,2,1,11),_SwRCPFileSystemForceAgree_Type())
swRCPFileSystemForceAgree.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPFileSystemForceAgree.setStatus(_A)
class _SwRCPFileSystemCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('start',2)))
_SwRCPFileSystemCtrl_Type.__name__=_D
_SwRCPFileSystemCtrl_Object=MibTableColumn
swRCPFileSystemCtrl=_SwRCPFileSystemCtrl_Object((1,3,6,1,4,1,171,12,82,1,2,1,12),_SwRCPFileSystemCtrl_Type())
swRCPFileSystemCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPFileSystemCtrl.setStatus(_A)
_SwRCPServerConfigTable_Object=MibTable
swRCPServerConfigTable=_SwRCPServerConfigTable_Object((1,3,6,1,4,1,171,12,82,1,3))
if mibBuilder.loadTexts:swRCPServerConfigTable.setStatus(_A)
_SwRCPServerConfigEntry_Object=MibTableRow
swRCPServerConfigEntry=_SwRCPServerConfigEntry_Object((1,3,6,1,4,1,171,12,82,1,3,1))
swRCPServerConfigEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:swRCPServerConfigEntry.setStatus(_A)
_SwRCPServerConfigIndex_Type=Integer32
_SwRCPServerConfigIndex_Object=MibTableColumn
swRCPServerConfigIndex=_SwRCPServerConfigIndex_Object((1,3,6,1,4,1,171,12,82,1,3,1,1),_SwRCPServerConfigIndex_Type())
swRCPServerConfigIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:swRCPServerConfigIndex.setStatus(_A)
_SwRCPServerConfigAddrType_Type=InetAddressType
_SwRCPServerConfigAddrType_Object=MibTableColumn
swRCPServerConfigAddrType=_SwRCPServerConfigAddrType_Object((1,3,6,1,4,1,171,12,82,1,3,1,2),_SwRCPServerConfigAddrType_Type())
swRCPServerConfigAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPServerConfigAddrType.setStatus(_A)
_SwRCPServerConfigAddr_Type=InetAddress
_SwRCPServerConfigAddr_Object=MibTableColumn
swRCPServerConfigAddr=_SwRCPServerConfigAddr_Object((1,3,6,1,4,1,171,12,82,1,3,1,3),_SwRCPServerConfigAddr_Type())
swRCPServerConfigAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPServerConfigAddr.setStatus(_A)
class _SwRCPServerConfigUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_SwRCPServerConfigUserName_Type.__name__=_C
_SwRCPServerConfigUserName_Object=MibTableColumn
swRCPServerConfigUserName=_SwRCPServerConfigUserName_Object((1,3,6,1,4,1,171,12,82,1,3,1,4),_SwRCPServerConfigUserName_Type())
swRCPServerConfigUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:swRCPServerConfigUserName.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'UnitList':UnitList,'swRCPMIB':swRCPMIB,'swRCPMgmt':swRCPMgmt,'swRCPFileTable':swRCPFileTable,'swRCPFileEntry':swRCPFileEntry,_H:swRCPFileIndex,'swRCPFileLoadType':swRCPFileLoadType,'swRCPFileType':swRCPFileType,'swRCPFileServerUserName':swRCPFileServerUserName,'swRCPFileServerAddrType':swRCPFileServerAddrType,'swRCPFileServerAddr':swRCPFileServerAddr,'swRCPFileServerPathFileName':swRCPFileServerPathFileName,'swRCPFileUnitID':swRCPFileUnitID,'swRCPFileCtrlID':swRCPFileCtrlID,'swRCPFileBootUpImage':swRCPFileBootUpImage,'swRCPFileForceAgree':swRCPFileForceAgree,'swRCPFileCtrl':swRCPFileCtrl,'swRCPFileSystemTable':swRCPFileSystemTable,'swRCPFileSystemEntry':swRCPFileSystemEntry,_L:swRCPFileSystemIndex,'swRCPFileSystemLoadType':swRCPFileSystemLoadType,'swRCPFileSystemFileType':swRCPFileSystemFileType,'swRCPFileSystemServerUserName':swRCPFileSystemServerUserName,'swRCPFileSystemServerAddrType':swRCPFileSystemServerAddrType,'swRCPFileSystemServerAddr':swRCPFileSystemServerAddr,'swRCPFileSystemServerPathFileName':swRCPFileSystemServerPathFileName,'swRCPFileSystemDevicePathFileName':swRCPFileSystemDevicePathFileName,'swRCPFileSystemUnitID':swRCPFileSystemUnitID,'swRCPFileSystemBootUpImage':swRCPFileSystemBootUpImage,'swRCPFileSystemForceAgree':swRCPFileSystemForceAgree,'swRCPFileSystemCtrl':swRCPFileSystemCtrl,'swRCPServerConfigTable':swRCPServerConfigTable,'swRCPServerConfigEntry':swRCPServerConfigEntry,_M:swRCPServerConfigIndex,'swRCPServerConfigAddrType':swRCPServerConfigAddrType,'swRCPServerConfigAddr':swRCPServerConfigAddr,'swRCPServerConfigUserName':swRCPServerConfigUserName})