_a='hpSwitchBuildGroup'
_Z='hpSwitchMgmtModuleGroup'
_Y='hpSwitchFlashImagesGroup'
_X='hpSwitchMgmtModuleWatchDog'
_W='hpSwitchMgmtModuleBuildOptions'
_V='hpSwitchFlashImageBuildNumber'
_U='hpSwitchMgmtModuleBuildNumber'
_T='hpSwitchMgmtModuleBootImage'
_S='hpSwitchMgmtModuleVersion'
_R='hpSwitchMgmtModuleDate'
_Q='hpSwitchMgmtModuleDirectory'
_P='hpSwitchMgmtModuleStatus'
_O='hpSwitchDefaultBoot'
_N='hpSwitchBootRomVersion'
_M='hpSwitchFlashImageVersion'
_L='hpSwitchFlashImageBuildDate'
_K='hpSwitchFlashImageSize'
_J='hpSwitchMgmtModuleID'
_I='not-accessible'
_H='hpSwitchFlashImageType'
_G='secondary'
_F='primary'
_E='unknown'
_D='Integer32'
_C='read-only'
_B='HP-SWITCH-IMAGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpSwitchImage=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,59))
if mibBuilder.loadTexts:hpSwitchImage.setRevisions(('2013-04-01 00:00','2008-12-15 00:00'))
_HpSwitchImageObject_ObjectIdentity=ObjectIdentity
hpSwitchImageObject=_HpSwitchImageObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,59,1))
class _HpSwitchDefaultBoot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HpSwitchDefaultBoot_Type.__name__=_D
_HpSwitchDefaultBoot_Object=MibScalar
hpSwitchDefaultBoot=_HpSwitchDefaultBoot_Object((1,3,6,1,4,1,11,2,14,11,5,1,59,1,1),_HpSwitchDefaultBoot_Type())
hpSwitchDefaultBoot.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchDefaultBoot.setStatus(_A)
_HpSwitchBootRomVersion_Type=DisplayString
_HpSwitchBootRomVersion_Object=MibScalar
hpSwitchBootRomVersion=_HpSwitchBootRomVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,59,1,2),_HpSwitchBootRomVersion_Type())
hpSwitchBootRomVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchBootRomVersion.setStatus(_A)
_HpSwitchFlashImageTable_Object=MibTable
hpSwitchFlashImageTable=_HpSwitchFlashImageTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,59,1,3))
if mibBuilder.loadTexts:hpSwitchFlashImageTable.setStatus(_A)
_HpSwitchFlashImageEntry_Object=MibTableRow
hpSwitchFlashImageEntry=_HpSwitchFlashImageEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,59,1,3,1))
hpSwitchFlashImageEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpSwitchFlashImageEntry.setStatus(_A)
class _HpSwitchFlashImageType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HpSwitchFlashImageType_Type.__name__=_D
_HpSwitchFlashImageType_Object=MibTableColumn
hpSwitchFlashImageType=_HpSwitchFlashImageType_Object((1,3,6,1,4,1,11,2,14,11,5,1,59,1,3,1,1),_HpSwitchFlashImageType_Type())
hpSwitchFlashImageType.setMaxAccess(_I)
if mibBuilder.loadTexts:hpSwitchFlashImageType.setStatus(_A)
_HpSwitchFlashImageSize_Type=Unsigned32
_HpSwitchFlashImageSize_Object=MibTableColumn
hpSwitchFlashImageSize=_HpSwitchFlashImageSize_Object((1,3,6,1,4,1,11,2,14,11,5,1,59,1,3,1,2),_HpSwitchFlashImageSize_Type())
hpSwitchFlashImageSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFlashImageSize.setStatus(_A)
if mibBuilder.loadTexts:hpSwitchFlashImageSize.setUnits('Bytes')
_HpSwitchFlashImageBuildDate_Type=DisplayString
_HpSwitchFlashImageBuildDate_Object=MibTableColumn
hpSwitchFlashImageBuildDate=_HpSwitchFlashImageBuildDate_Object((1,3,6,1,4,1,11,2,14,11,5,1,59,1,3,1,3),_HpSwitchFlashImageBuildDate_Type())
hpSwitchFlashImageBuildDate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFlashImageBuildDate.setStatus(_A)
_HpSwitchFlashImageVersion_Type=DisplayString
_HpSwitchFlashImageVersion_Object=MibTableColumn
hpSwitchFlashImageVersion=_HpSwitchFlashImageVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,59,1,3,1,4),_HpSwitchFlashImageVersion_Type())
hpSwitchFlashImageVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFlashImageVersion.setStatus(_A)
_HpSwitchFlashImageBuildNumber_Type=DisplayString
_HpSwitchFlashImageBuildNumber_Object=MibTableColumn
hpSwitchFlashImageBuildNumber=_HpSwitchFlashImageBuildNumber_Object((1,3,6,1,4,1,11,2,14,11,5,1,59,1,3,1,5),_HpSwitchFlashImageBuildNumber_Type())
hpSwitchFlashImageBuildNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchFlashImageBuildNumber.setStatus(_A)
_HpSwitchMgmtModuleVersionTable_Object=MibTable
hpSwitchMgmtModuleVersionTable=_HpSwitchMgmtModuleVersionTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,59,1,4))
if mibBuilder.loadTexts:hpSwitchMgmtModuleVersionTable.setStatus(_A)
_HpSwitchMgmtModuleVersionEntry_Object=MibTableRow
hpSwitchMgmtModuleVersionEntry=_HpSwitchMgmtModuleVersionEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,59,1,4,1))
hpSwitchMgmtModuleVersionEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:hpSwitchMgmtModuleVersionEntry.setStatus(_A)
class _HpSwitchMgmtModuleID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mgmtModule1',1),('mgmtModule2',2)))
_HpSwitchMgmtModuleID_Type.__name__=_D
_HpSwitchMgmtModuleID_Object=MibTableColumn
hpSwitchMgmtModuleID=_HpSwitchMgmtModuleID_Object((1,3,6,1,4,1,11,2,14,11,5,1,59,1,4,1,1),_HpSwitchMgmtModuleID_Type())
hpSwitchMgmtModuleID.setMaxAccess(_I)
if mibBuilder.loadTexts:hpSwitchMgmtModuleID.setStatus(_A)
class _HpSwitchMgmtModuleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),('active',2),('redundancyDisabled',3),('standby',4),('offline',5),('failed',6),('syncing',7)))
_HpSwitchMgmtModuleStatus_Type.__name__=_D
_HpSwitchMgmtModuleStatus_Object=MibTableColumn
hpSwitchMgmtModuleStatus=_HpSwitchMgmtModuleStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,59,1,4,1,2),_HpSwitchMgmtModuleStatus_Type())
hpSwitchMgmtModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchMgmtModuleStatus.setStatus(_A)
_HpSwitchMgmtModuleDirectory_Type=DisplayString
_HpSwitchMgmtModuleDirectory_Object=MibTableColumn
hpSwitchMgmtModuleDirectory=_HpSwitchMgmtModuleDirectory_Object((1,3,6,1,4,1,11,2,14,11,5,1,59,1,4,1,3),_HpSwitchMgmtModuleDirectory_Type())
hpSwitchMgmtModuleDirectory.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchMgmtModuleDirectory.setStatus(_A)
_HpSwitchMgmtModuleDate_Type=DisplayString
_HpSwitchMgmtModuleDate_Object=MibTableColumn
hpSwitchMgmtModuleDate=_HpSwitchMgmtModuleDate_Object((1,3,6,1,4,1,11,2,14,11,5,1,59,1,4,1,4),_HpSwitchMgmtModuleDate_Type())
hpSwitchMgmtModuleDate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchMgmtModuleDate.setStatus(_A)
_HpSwitchMgmtModuleVersion_Type=DisplayString
_HpSwitchMgmtModuleVersion_Object=MibTableColumn
hpSwitchMgmtModuleVersion=_HpSwitchMgmtModuleVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,59,1,4,1,5),_HpSwitchMgmtModuleVersion_Type())
hpSwitchMgmtModuleVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchMgmtModuleVersion.setStatus(_A)
_HpSwitchMgmtModuleBuildNumber_Type=DisplayString
_HpSwitchMgmtModuleBuildNumber_Object=MibTableColumn
hpSwitchMgmtModuleBuildNumber=_HpSwitchMgmtModuleBuildNumber_Object((1,3,6,1,4,1,11,2,14,11,5,1,59,1,4,1,6),_HpSwitchMgmtModuleBuildNumber_Type())
hpSwitchMgmtModuleBuildNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchMgmtModuleBuildNumber.setStatus(_A)
class _HpSwitchMgmtModuleBootImage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_HpSwitchMgmtModuleBootImage_Type.__name__=_D
_HpSwitchMgmtModuleBootImage_Object=MibTableColumn
hpSwitchMgmtModuleBootImage=_HpSwitchMgmtModuleBootImage_Object((1,3,6,1,4,1,11,2,14,11,5,1,59,1,4,1,7),_HpSwitchMgmtModuleBootImage_Type())
hpSwitchMgmtModuleBootImage.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchMgmtModuleBootImage.setStatus(_A)
class _HpSwitchMgmtModuleBuildOptions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('qa',2),('hubmode',3),('debug',4),('asicLogging',5)))
_HpSwitchMgmtModuleBuildOptions_Type.__name__=_D
_HpSwitchMgmtModuleBuildOptions_Object=MibTableColumn
hpSwitchMgmtModuleBuildOptions=_HpSwitchMgmtModuleBuildOptions_Object((1,3,6,1,4,1,11,2,14,11,5,1,59,1,4,1,8),_HpSwitchMgmtModuleBuildOptions_Type())
hpSwitchMgmtModuleBuildOptions.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchMgmtModuleBuildOptions.setStatus(_A)
class _HpSwitchMgmtModuleWatchDog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('enabled',2),('disabled',3)))
_HpSwitchMgmtModuleWatchDog_Type.__name__=_D
_HpSwitchMgmtModuleWatchDog_Object=MibTableColumn
hpSwitchMgmtModuleWatchDog=_HpSwitchMgmtModuleWatchDog_Object((1,3,6,1,4,1,11,2,14,11,5,1,59,1,4,1,9),_HpSwitchMgmtModuleWatchDog_Type())
hpSwitchMgmtModuleWatchDog.setMaxAccess(_C)
if mibBuilder.loadTexts:hpSwitchMgmtModuleWatchDog.setStatus(_A)
_HpSwitchImageConformance_ObjectIdentity=ObjectIdentity
hpSwitchImageConformance=_HpSwitchImageConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,59,2))
_HpSwitchImageGroups_ObjectIdentity=ObjectIdentity
hpSwitchImageGroups=_HpSwitchImageGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,59,2,1))
_HpSwitchImageCompliances_ObjectIdentity=ObjectIdentity
hpSwitchImageCompliances=_HpSwitchImageCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,59,2,2))
hpSwitchFlashImagesGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,59,2,1,1))
hpSwitchFlashImagesGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:hpSwitchFlashImagesGroup.setStatus(_A)
hpSwitchMgmtModuleGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,59,2,1,2))
hpSwitchMgmtModuleGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:hpSwitchMgmtModuleGroup.setStatus(_A)
hpSwitchBuildGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,59,2,1,3))
hpSwitchBuildGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:hpSwitchBuildGroup.setStatus(_A)
hpSwitchImageCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,59,2,2,1))
hpSwitchImageCompliance.setObjects(*((_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:hpSwitchImageCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpSwitchImage':hpSwitchImage,'hpSwitchImageObject':hpSwitchImageObject,_O:hpSwitchDefaultBoot,_N:hpSwitchBootRomVersion,'hpSwitchFlashImageTable':hpSwitchFlashImageTable,'hpSwitchFlashImageEntry':hpSwitchFlashImageEntry,_H:hpSwitchFlashImageType,_K:hpSwitchFlashImageSize,_L:hpSwitchFlashImageBuildDate,_M:hpSwitchFlashImageVersion,_V:hpSwitchFlashImageBuildNumber,'hpSwitchMgmtModuleVersionTable':hpSwitchMgmtModuleVersionTable,'hpSwitchMgmtModuleVersionEntry':hpSwitchMgmtModuleVersionEntry,_J:hpSwitchMgmtModuleID,_P:hpSwitchMgmtModuleStatus,_Q:hpSwitchMgmtModuleDirectory,_R:hpSwitchMgmtModuleDate,_S:hpSwitchMgmtModuleVersion,_U:hpSwitchMgmtModuleBuildNumber,_T:hpSwitchMgmtModuleBootImage,_W:hpSwitchMgmtModuleBuildOptions,_X:hpSwitchMgmtModuleWatchDog,'hpSwitchImageConformance':hpSwitchImageConformance,'hpSwitchImageGroups':hpSwitchImageGroups,_Y:hpSwitchFlashImagesGroup,_Z:hpSwitchMgmtModuleGroup,_a:hpSwitchBuildGroup,'hpSwitchImageCompliances':hpSwitchImageCompliances,'hpSwitchImageCompliance':hpSwitchImageCompliance})