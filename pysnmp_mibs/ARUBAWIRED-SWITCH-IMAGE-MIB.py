_Q='arubaWiredSwitchBootGroup'
_P='arubaWiredSwitchFlashImagesGroup'
_O='arubaWiredBootProfileTimeout'
_N='arubaWiredDefaultBootEnum'
_M='arubaWiredDefaultBoot'
_L='arubaWiredSwitchImageSha'
_K='arubaWiredSwitchImageBuildDate'
_J='arubaWiredSwitchImageSize'
_I='arubaWiredSwitchImageVersion'
_H='arubaWiredSwitchImageType'
_G='arubaWiredSwitchImageTypeEnum'
_F='secondary'
_E='primary'
_D='Integer32'
_C='read-only'
_B='ARUBAWIRED-SWITCH-IMAGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wndFeatures,=mibBuilder.importSymbols('ARUBAWIRED-NETWORKING-OID','wndFeatures')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
arubaWiredSwitchImage=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,26))
if mibBuilder.loadTexts:arubaWiredSwitchImage.setRevisions(('2023-05-25 00:00',))
_ArubaWiredSwitchImageObject_ObjectIdentity=ObjectIdentity
arubaWiredSwitchImageObject=_ArubaWiredSwitchImageObject_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,26,1))
_ArubaWiredSwitchImageGeneral_ObjectIdentity=ObjectIdentity
arubaWiredSwitchImageGeneral=_ArubaWiredSwitchImageGeneral_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,26,1,0))
_ArubaWiredDefaultBoot_Type=DisplayString
_ArubaWiredDefaultBoot_Object=MibScalar
arubaWiredDefaultBoot=_ArubaWiredDefaultBoot_Object((1,3,6,1,4,1,47196,4,1,1,3,26,1,0,1),_ArubaWiredDefaultBoot_Type())
arubaWiredDefaultBoot.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDefaultBoot.setStatus(_A)
class _ArubaWiredDefaultBootEnum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_ArubaWiredDefaultBootEnum_Type.__name__=_D
_ArubaWiredDefaultBootEnum_Object=MibScalar
arubaWiredDefaultBootEnum=_ArubaWiredDefaultBootEnum_Object((1,3,6,1,4,1,47196,4,1,1,3,26,1,0,2),_ArubaWiredDefaultBootEnum_Type())
arubaWiredDefaultBootEnum.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredDefaultBootEnum.setStatus(_A)
class _ArubaWiredBootProfileTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_ArubaWiredBootProfileTimeout_Type.__name__=_D
_ArubaWiredBootProfileTimeout_Object=MibScalar
arubaWiredBootProfileTimeout=_ArubaWiredBootProfileTimeout_Object((1,3,6,1,4,1,47196,4,1,1,3,26,1,0,3),_ArubaWiredBootProfileTimeout_Type())
arubaWiredBootProfileTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredBootProfileTimeout.setStatus(_A)
_ArubaWiredSwitchImageDetails_ObjectIdentity=ObjectIdentity
arubaWiredSwitchImageDetails=_ArubaWiredSwitchImageDetails_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,26,1,1))
_ArubaWiredSwitchImageTable_Object=MibTable
arubaWiredSwitchImageTable=_ArubaWiredSwitchImageTable_Object((1,3,6,1,4,1,47196,4,1,1,3,26,1,1,1))
if mibBuilder.loadTexts:arubaWiredSwitchImageTable.setStatus(_A)
_ArubaWiredSwitchImageEntry_Object=MibTableRow
arubaWiredSwitchImageEntry=_ArubaWiredSwitchImageEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,26,1,1,1,1))
arubaWiredSwitchImageEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:arubaWiredSwitchImageEntry.setStatus(_A)
class _ArubaWiredSwitchImageTypeEnum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_ArubaWiredSwitchImageTypeEnum_Type.__name__=_D
_ArubaWiredSwitchImageTypeEnum_Object=MibTableColumn
arubaWiredSwitchImageTypeEnum=_ArubaWiredSwitchImageTypeEnum_Object((1,3,6,1,4,1,47196,4,1,1,3,26,1,1,1,1,1),_ArubaWiredSwitchImageTypeEnum_Type())
arubaWiredSwitchImageTypeEnum.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:arubaWiredSwitchImageTypeEnum.setStatus(_A)
_ArubaWiredSwitchImageType_Type=DisplayString
_ArubaWiredSwitchImageType_Object=MibTableColumn
arubaWiredSwitchImageType=_ArubaWiredSwitchImageType_Object((1,3,6,1,4,1,47196,4,1,1,3,26,1,1,1,1,2),_ArubaWiredSwitchImageType_Type())
arubaWiredSwitchImageType.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredSwitchImageType.setStatus(_A)
_ArubaWiredSwitchImageVersion_Type=DisplayString
_ArubaWiredSwitchImageVersion_Object=MibTableColumn
arubaWiredSwitchImageVersion=_ArubaWiredSwitchImageVersion_Object((1,3,6,1,4,1,47196,4,1,1,3,26,1,1,1,1,3),_ArubaWiredSwitchImageVersion_Type())
arubaWiredSwitchImageVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredSwitchImageVersion.setStatus(_A)
_ArubaWiredSwitchImageSize_Type=DisplayString
_ArubaWiredSwitchImageSize_Object=MibTableColumn
arubaWiredSwitchImageSize=_ArubaWiredSwitchImageSize_Object((1,3,6,1,4,1,47196,4,1,1,3,26,1,1,1,1,4),_ArubaWiredSwitchImageSize_Type())
arubaWiredSwitchImageSize.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredSwitchImageSize.setStatus(_A)
_ArubaWiredSwitchImageBuildDate_Type=DisplayString
_ArubaWiredSwitchImageBuildDate_Object=MibTableColumn
arubaWiredSwitchImageBuildDate=_ArubaWiredSwitchImageBuildDate_Object((1,3,6,1,4,1,47196,4,1,1,3,26,1,1,1,1,5),_ArubaWiredSwitchImageBuildDate_Type())
arubaWiredSwitchImageBuildDate.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredSwitchImageBuildDate.setStatus(_A)
_ArubaWiredSwitchImageSha_Type=DisplayString
_ArubaWiredSwitchImageSha_Object=MibTableColumn
arubaWiredSwitchImageSha=_ArubaWiredSwitchImageSha_Object((1,3,6,1,4,1,47196,4,1,1,3,26,1,1,1,1,6),_ArubaWiredSwitchImageSha_Type())
arubaWiredSwitchImageSha.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredSwitchImageSha.setStatus(_A)
_ArubaWiredSwitchImageConformance_ObjectIdentity=ObjectIdentity
arubaWiredSwitchImageConformance=_ArubaWiredSwitchImageConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,26,2))
_ArubaWiredSwitchImageGroups_ObjectIdentity=ObjectIdentity
arubaWiredSwitchImageGroups=_ArubaWiredSwitchImageGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,26,2,1))
_ArubaWiredSwitchImageCompliances_ObjectIdentity=ObjectIdentity
arubaWiredSwitchImageCompliances=_ArubaWiredSwitchImageCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,26,2,2))
arubaWiredSwitchFlashImagesGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,26,2,1,1))
arubaWiredSwitchFlashImagesGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:arubaWiredSwitchFlashImagesGroup.setStatus(_A)
arubaWiredSwitchBootGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,26,2,1,2))
arubaWiredSwitchBootGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:arubaWiredSwitchBootGroup.setStatus(_A)
arubaWiredSwitchImageCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,26,2,2,1))
arubaWiredSwitchImageCompliance.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:arubaWiredSwitchImageCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'arubaWiredSwitchImage':arubaWiredSwitchImage,'arubaWiredSwitchImageObject':arubaWiredSwitchImageObject,'arubaWiredSwitchImageGeneral':arubaWiredSwitchImageGeneral,_M:arubaWiredDefaultBoot,_N:arubaWiredDefaultBootEnum,_O:arubaWiredBootProfileTimeout,'arubaWiredSwitchImageDetails':arubaWiredSwitchImageDetails,'arubaWiredSwitchImageTable':arubaWiredSwitchImageTable,'arubaWiredSwitchImageEntry':arubaWiredSwitchImageEntry,_G:arubaWiredSwitchImageTypeEnum,_H:arubaWiredSwitchImageType,_I:arubaWiredSwitchImageVersion,_J:arubaWiredSwitchImageSize,_K:arubaWiredSwitchImageBuildDate,_L:arubaWiredSwitchImageSha,'arubaWiredSwitchImageConformance':arubaWiredSwitchImageConformance,'arubaWiredSwitchImageGroups':arubaWiredSwitchImageGroups,_P:arubaWiredSwitchFlashImagesGroup,_Q:arubaWiredSwitchBootGroup,'arubaWiredSwitchImageCompliances':arubaWiredSwitchImageCompliances,'arubaWiredSwitchImageCompliance':arubaWiredSwitchImageCompliance})