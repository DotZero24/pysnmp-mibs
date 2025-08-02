_L='swGenExpansionModuleMgmtSlotID'
_K='swGenFileSystemMgmtIndex'
_J='swGenMgmtUnitID'
_I='not-accessible'
_H='other'
_G='OctetString'
_F='read-only'
_E='GENERAL-MGMT-MIB'
_D='Integer32'
_C='DisplayString'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_C,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
dXS_3600_32S,=mibBuilder.importSymbols('SW3600PRIMGMT-MIB','dXS-3600-32S')
swGeneralMgmtMIB=ModuleIdentity((1,3,6,1,4,1,171,10,127,1,20))
class UnitList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
class Ipv6Address(TextualConvention,OctetString):status=_A;displayHint='2x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_SwGenMgmtNotifications_ObjectIdentity=ObjectIdentity
swGenMgmtNotifications=_SwGenMgmtNotifications_ObjectIdentity((1,3,6,1,4,1,171,10,127,1,20,0))
_SwGenMgmtMIBObjects_ObjectIdentity=ObjectIdentity
swGenMgmtMIBObjects=_SwGenMgmtMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,127,1,20,1))
_SwGenMgmtGroup_ObjectIdentity=ObjectIdentity
swGenMgmtGroup=_SwGenMgmtGroup_ObjectIdentity((1,3,6,1,4,1,171,10,127,1,20,1,1))
_SwGenFileSystemMgmt_ObjectIdentity=ObjectIdentity
swGenFileSystemMgmt=_SwGenFileSystemMgmt_ObjectIdentity((1,3,6,1,4,1,171,10,127,1,20,1,1,1))
_SwGenFileSystemMgmtTable_Object=MibTable
swGenFileSystemMgmtTable=_SwGenFileSystemMgmtTable_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,1,1))
if mibBuilder.loadTexts:swGenFileSystemMgmtTable.setStatus(_A)
_SwGenFileSystemMgmtEntry_Object=MibTableRow
swGenFileSystemMgmtEntry=_SwGenFileSystemMgmtEntry_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,1,1,1))
swGenFileSystemMgmtEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:swGenFileSystemMgmtEntry.setStatus(_A)
_SwGenFileSystemMgmtIndex_Type=Integer32
_SwGenFileSystemMgmtIndex_Object=MibTableColumn
swGenFileSystemMgmtIndex=_SwGenFileSystemMgmtIndex_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,1,1,1,1),_SwGenFileSystemMgmtIndex_Type())
swGenFileSystemMgmtIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:swGenFileSystemMgmtIndex.setStatus(_A)
class _SwGenFileSystemMgmtDscr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwGenFileSystemMgmtDscr_Type.__name__=_C
_SwGenFileSystemMgmtDscr_Object=MibTableColumn
swGenFileSystemMgmtDscr=_SwGenFileSystemMgmtDscr_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,1,1,1,2),_SwGenFileSystemMgmtDscr_Type())
swGenFileSystemMgmtDscr.setMaxAccess(_F)
if mibBuilder.loadTexts:swGenFileSystemMgmtDscr.setStatus(_A)
_SwGenFileSystemMgmtServerAddrType_Type=InetAddressType
_SwGenFileSystemMgmtServerAddrType_Object=MibTableColumn
swGenFileSystemMgmtServerAddrType=_SwGenFileSystemMgmtServerAddrType_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,1,1,1,3),_SwGenFileSystemMgmtServerAddrType_Type())
swGenFileSystemMgmtServerAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:swGenFileSystemMgmtServerAddrType.setStatus(_A)
_SwGenFileSystemMgmtServerAddr_Type=InetAddress
_SwGenFileSystemMgmtServerAddr_Object=MibTableColumn
swGenFileSystemMgmtServerAddr=_SwGenFileSystemMgmtServerAddr_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,1,1,1,4),_SwGenFileSystemMgmtServerAddr_Type())
swGenFileSystemMgmtServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swGenFileSystemMgmtServerAddr.setStatus(_A)
class _SwGenFileSystemMgmtInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SwGenFileSystemMgmtInterfaceName_Type.__name__=_C
_SwGenFileSystemMgmtInterfaceName_Object=MibTableColumn
swGenFileSystemMgmtInterfaceName=_SwGenFileSystemMgmtInterfaceName_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,1,1,1,5),_SwGenFileSystemMgmtInterfaceName_Type())
swGenFileSystemMgmtInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:swGenFileSystemMgmtInterfaceName.setStatus(_A)
class _SwGenFileSystemMgmtTranserProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tftp',1),('ftp',2)))
_SwGenFileSystemMgmtTranserProtocol_Type.__name__=_D
_SwGenFileSystemMgmtTranserProtocol_Object=MibTableColumn
swGenFileSystemMgmtTranserProtocol=_SwGenFileSystemMgmtTranserProtocol_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,1,1,1,10),_SwGenFileSystemMgmtTranserProtocol_Type())
swGenFileSystemMgmtTranserProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:swGenFileSystemMgmtTranserProtocol.setStatus(_A)
_SwGenFileSystemMgmtUserName_Type=DisplayString
_SwGenFileSystemMgmtUserName_Object=MibTableColumn
swGenFileSystemMgmtUserName=_SwGenFileSystemMgmtUserName_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,1,1,1,11),_SwGenFileSystemMgmtUserName_Type())
swGenFileSystemMgmtUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:swGenFileSystemMgmtUserName.setStatus(_A)
_SwGenFileSystemMgmtPassword_Type=DisplayString
_SwGenFileSystemMgmtPassword_Object=MibTableColumn
swGenFileSystemMgmtPassword=_SwGenFileSystemMgmtPassword_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,1,1,1,12),_SwGenFileSystemMgmtPassword_Type())
swGenFileSystemMgmtPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:swGenFileSystemMgmtPassword.setStatus(_A)
class _SwGenFileSystemMgmtServerFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwGenFileSystemMgmtServerFileName_Type.__name__=_C
_SwGenFileSystemMgmtServerFileName_Object=MibTableColumn
swGenFileSystemMgmtServerFileName=_SwGenFileSystemMgmtServerFileName_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,1,1,1,20),_SwGenFileSystemMgmtServerFileName_Type())
swGenFileSystemMgmtServerFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:swGenFileSystemMgmtServerFileName.setStatus(_A)
class _SwGenFileSystemMgmtDeviceFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwGenFileSystemMgmtDeviceFileName_Type.__name__=_C
_SwGenFileSystemMgmtDeviceFileName_Object=MibTableColumn
swGenFileSystemMgmtDeviceFileName=_SwGenFileSystemMgmtDeviceFileName_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,1,1,1,21),_SwGenFileSystemMgmtDeviceFileName_Type())
swGenFileSystemMgmtDeviceFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:swGenFileSystemMgmtDeviceFileName.setStatus(_A)
class _SwGenFileSystemMgmtLoadType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('upload',2),('download',3)))
_SwGenFileSystemMgmtLoadType_Type.__name__=_D
_SwGenFileSystemMgmtLoadType_Object=MibTableColumn
swGenFileSystemMgmtLoadType=_SwGenFileSystemMgmtLoadType_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,1,1,1,30),_SwGenFileSystemMgmtLoadType_Type())
swGenFileSystemMgmtLoadType.setMaxAccess(_B)
if mibBuilder.loadTexts:swGenFileSystemMgmtLoadType.setStatus(_A)
class _SwGenFileSystemMgmtCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('inactive',2),('start',3)))
_SwGenFileSystemMgmtCtrl_Type.__name__=_D
_SwGenFileSystemMgmtCtrl_Object=MibTableColumn
swGenFileSystemMgmtCtrl=_SwGenFileSystemMgmtCtrl_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,1,1,1,100),_SwGenFileSystemMgmtCtrl_Type())
swGenFileSystemMgmtCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:swGenFileSystemMgmtCtrl.setStatus(_A)
_SwGenFileSystemBootupFileMgmtTable_Object=MibTable
swGenFileSystemBootupFileMgmtTable=_SwGenFileSystemBootupFileMgmtTable_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,5))
if mibBuilder.loadTexts:swGenFileSystemBootupFileMgmtTable.setStatus(_A)
_SwGenFileSystemBootupFileMgmtEntry_Object=MibTableRow
swGenFileSystemBootupFileMgmtEntry=_SwGenFileSystemBootupFileMgmtEntry_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,5,1))
swGenFileSystemBootupFileMgmtEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:swGenFileSystemBootupFileMgmtEntry.setStatus(_A)
_SwGenMgmtUnitID_Type=Integer32
_SwGenMgmtUnitID_Object=MibTableColumn
swGenMgmtUnitID=_SwGenMgmtUnitID_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,5,1,1),_SwGenMgmtUnitID_Type())
swGenMgmtUnitID.setMaxAccess(_I)
if mibBuilder.loadTexts:swGenMgmtUnitID.setStatus(_A)
class _SwGenFileSystemBootImage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwGenFileSystemBootImage_Type.__name__=_C
_SwGenFileSystemBootImage_Object=MibTableColumn
swGenFileSystemBootImage=_SwGenFileSystemBootImage_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,5,1,3),_SwGenFileSystemBootImage_Type())
swGenFileSystemBootImage.setMaxAccess(_B)
if mibBuilder.loadTexts:swGenFileSystemBootImage.setStatus(_A)
class _SwGenFileSystemBootConfig_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwGenFileSystemBootConfig_Type.__name__=_C
_SwGenFileSystemBootConfig_Object=MibTableColumn
swGenFileSystemBootConfig=_SwGenFileSystemBootConfig_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,5,1,5),_SwGenFileSystemBootConfig_Type())
swGenFileSystemBootConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:swGenFileSystemBootConfig.setStatus(_A)
_SwGenFileSystemActiveConfigIncrement_Type=TruthValue
_SwGenFileSystemActiveConfigIncrement_Object=MibTableColumn
swGenFileSystemActiveConfigIncrement=_SwGenFileSystemActiveConfigIncrement_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,5,1,10),_SwGenFileSystemActiveConfigIncrement_Type())
swGenFileSystemActiveConfigIncrement.setMaxAccess(_B)
if mibBuilder.loadTexts:swGenFileSystemActiveConfigIncrement.setStatus(_A)
class _SwGenFileSystemActiveConfig_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwGenFileSystemActiveConfig_Type.__name__=_C
_SwGenFileSystemActiveConfig_Object=MibTableColumn
swGenFileSystemActiveConfig=_SwGenFileSystemActiveConfig_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,5,1,11),_SwGenFileSystemActiveConfig_Type())
swGenFileSystemActiveConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:swGenFileSystemActiveConfig.setStatus(_A)
_SwGenExpansionModuleMgmtTable_Object=MibTable
swGenExpansionModuleMgmtTable=_SwGenExpansionModuleMgmtTable_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,8))
if mibBuilder.loadTexts:swGenExpansionModuleMgmtTable.setStatus(_A)
_SwGenExpansionModuleMgmtEntry_Object=MibTableRow
swGenExpansionModuleMgmtEntry=_SwGenExpansionModuleMgmtEntry_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,8,1))
swGenExpansionModuleMgmtEntry.setIndexNames((0,_E,_J),(0,_E,_L))
if mibBuilder.loadTexts:swGenExpansionModuleMgmtEntry.setStatus(_A)
_SwGenExpansionModuleMgmtSlotID_Type=Integer32
_SwGenExpansionModuleMgmtSlotID_Object=MibTableColumn
swGenExpansionModuleMgmtSlotID=_SwGenExpansionModuleMgmtSlotID_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,8,1,2),_SwGenExpansionModuleMgmtSlotID_Type())
swGenExpansionModuleMgmtSlotID.setMaxAccess(_I)
if mibBuilder.loadTexts:swGenExpansionModuleMgmtSlotID.setStatus(_A)
class _SwGenExpansionModuleMgmtBootup_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwGenExpansionModuleMgmtBootup_Type.__name__=_C
_SwGenExpansionModuleMgmtBootup_Object=MibTableColumn
swGenExpansionModuleMgmtBootup=_SwGenExpansionModuleMgmtBootup_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,8,1,3),_SwGenExpansionModuleMgmtBootup_Type())
swGenExpansionModuleMgmtBootup.setMaxAccess(_F)
if mibBuilder.loadTexts:swGenExpansionModuleMgmtBootup.setStatus(_A)
class _SwGenExpansionModuleMgmtCurrent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwGenExpansionModuleMgmtCurrent_Type.__name__=_C
_SwGenExpansionModuleMgmtCurrent_Object=MibTableColumn
swGenExpansionModuleMgmtCurrent=_SwGenExpansionModuleMgmtCurrent_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,8,1,4),_SwGenExpansionModuleMgmtCurrent_Type())
swGenExpansionModuleMgmtCurrent.setMaxAccess(_F)
if mibBuilder.loadTexts:swGenExpansionModuleMgmtCurrent.setStatus(_A)
class _SwGenExpansionModuleBootupPortModeInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwGenExpansionModuleBootupPortModeInfo_Type.__name__=_G
_SwGenExpansionModuleBootupPortModeInfo_Object=MibTableColumn
swGenExpansionModuleBootupPortModeInfo=_SwGenExpansionModuleBootupPortModeInfo_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,8,1,5),_SwGenExpansionModuleBootupPortModeInfo_Type())
swGenExpansionModuleBootupPortModeInfo.setMaxAccess(_F)
if mibBuilder.loadTexts:swGenExpansionModuleBootupPortModeInfo.setStatus(_A)
class _SwGenExpansionModuleCurrentPortModeMGT_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwGenExpansionModuleCurrentPortModeMGT_Type.__name__=_G
_SwGenExpansionModuleCurrentPortModeMGT_Object=MibTableColumn
swGenExpansionModuleCurrentPortModeMGT=_SwGenExpansionModuleCurrentPortModeMGT_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,8,1,6),_SwGenExpansionModuleCurrentPortModeMGT_Type())
swGenExpansionModuleCurrentPortModeMGT.setMaxAccess(_B)
if mibBuilder.loadTexts:swGenExpansionModuleCurrentPortModeMGT.setStatus(_A)
class _SwGenExpansionModuleEquippedModulePortMode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwGenExpansionModuleEquippedModulePortMode_Type.__name__=_G
_SwGenExpansionModuleEquippedModulePortMode_Object=MibTableColumn
swGenExpansionModuleEquippedModulePortMode=_SwGenExpansionModuleEquippedModulePortMode_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,8,1,7),_SwGenExpansionModuleEquippedModulePortMode_Type())
swGenExpansionModuleEquippedModulePortMode.setMaxAccess(_F)
if mibBuilder.loadTexts:swGenExpansionModuleEquippedModulePortMode.setStatus(_A)
class _SwGenMgmtReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('start',2)))
_SwGenMgmtReboot_Type.__name__=_D
_SwGenMgmtReboot_Object=MibScalar
swGenMgmtReboot=_SwGenMgmtReboot_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,10),_SwGenMgmtReboot_Type())
swGenMgmtReboot.setMaxAccess(_B)
if mibBuilder.loadTexts:swGenMgmtReboot.setStatus(_A)
class _SwGenMgmtSaveConfigFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwGenMgmtSaveConfigFileName_Type.__name__=_C
_SwGenMgmtSaveConfigFileName_Object=MibScalar
swGenMgmtSaveConfigFileName=_SwGenMgmtSaveConfigFileName_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,11),_SwGenMgmtSaveConfigFileName_Type())
swGenMgmtSaveConfigFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:swGenMgmtSaveConfigFileName.setStatus(_A)
class _SwGenMgmtSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('configuration',2),('log',3),('all',4)))
_SwGenMgmtSave_Type.__name__=_D
_SwGenMgmtSave_Object=MibScalar
swGenMgmtSave=_SwGenMgmtSave_Object((1,3,6,1,4,1,171,10,127,1,20,1,1,12),_SwGenMgmtSave_Type())
swGenMgmtSave.setMaxAccess(_B)
if mibBuilder.loadTexts:swGenMgmtSave.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'Ipv6Address':Ipv6Address,'UnitList':UnitList,'swGeneralMgmtMIB':swGeneralMgmtMIB,'swGenMgmtNotifications':swGenMgmtNotifications,'swGenMgmtMIBObjects':swGenMgmtMIBObjects,'swGenMgmtGroup':swGenMgmtGroup,'swGenFileSystemMgmt':swGenFileSystemMgmt,'swGenFileSystemMgmtTable':swGenFileSystemMgmtTable,'swGenFileSystemMgmtEntry':swGenFileSystemMgmtEntry,_K:swGenFileSystemMgmtIndex,'swGenFileSystemMgmtDscr':swGenFileSystemMgmtDscr,'swGenFileSystemMgmtServerAddrType':swGenFileSystemMgmtServerAddrType,'swGenFileSystemMgmtServerAddr':swGenFileSystemMgmtServerAddr,'swGenFileSystemMgmtInterfaceName':swGenFileSystemMgmtInterfaceName,'swGenFileSystemMgmtTranserProtocol':swGenFileSystemMgmtTranserProtocol,'swGenFileSystemMgmtUserName':swGenFileSystemMgmtUserName,'swGenFileSystemMgmtPassword':swGenFileSystemMgmtPassword,'swGenFileSystemMgmtServerFileName':swGenFileSystemMgmtServerFileName,'swGenFileSystemMgmtDeviceFileName':swGenFileSystemMgmtDeviceFileName,'swGenFileSystemMgmtLoadType':swGenFileSystemMgmtLoadType,'swGenFileSystemMgmtCtrl':swGenFileSystemMgmtCtrl,'swGenFileSystemBootupFileMgmtTable':swGenFileSystemBootupFileMgmtTable,'swGenFileSystemBootupFileMgmtEntry':swGenFileSystemBootupFileMgmtEntry,_J:swGenMgmtUnitID,'swGenFileSystemBootImage':swGenFileSystemBootImage,'swGenFileSystemBootConfig':swGenFileSystemBootConfig,'swGenFileSystemActiveConfigIncrement':swGenFileSystemActiveConfigIncrement,'swGenFileSystemActiveConfig':swGenFileSystemActiveConfig,'swGenExpansionModuleMgmtTable':swGenExpansionModuleMgmtTable,'swGenExpansionModuleMgmtEntry':swGenExpansionModuleMgmtEntry,_L:swGenExpansionModuleMgmtSlotID,'swGenExpansionModuleMgmtBootup':swGenExpansionModuleMgmtBootup,'swGenExpansionModuleMgmtCurrent':swGenExpansionModuleMgmtCurrent,'swGenExpansionModuleBootupPortModeInfo':swGenExpansionModuleBootupPortModeInfo,'swGenExpansionModuleCurrentPortModeMGT':swGenExpansionModuleCurrentPortModeMGT,'swGenExpansionModuleEquippedModulePortMode':swGenExpansionModuleEquippedModulePortMode,'swGenMgmtReboot':swGenMgmtReboot,'swGenMgmtSaveConfigFileName':swGenMgmtSaveConfigFileName,'swGenMgmtSave':swGenMgmtSave})