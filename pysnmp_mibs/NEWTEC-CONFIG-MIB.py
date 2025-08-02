_Q='ntcCfgConfGrpV1Standard'
_P='ntcCfgLoadConfigNotForced'
_O='ntcCfgDeleteConfig'
_N='ntcCfgSaveConfig'
_M='ntcCfgLoadConfig'
_L='ntcCfgBootConfig'
_K='ntcCfgUnsavedChanges'
_J='ntcCfgActiveConfig'
_I='ntcCfgConfigName'
_H='ntcCfgConfigIndex'
_G='Unsigned32'
_F='read-only'
_E='read-write'
_D='unknown'
_C='DisplayString'
_B='NEWTEC-CONFIG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention','TruthValue')
ntcConfig=ModuleIdentity((1,3,6,1,4,1,5835,5,2,1500))
if mibBuilder.loadTexts:ntcConfig.setRevisions(('2013-03-27 10:00','2012-06-28 12:00'))
_NtcCfgObjects_ObjectIdentity=ObjectIdentity
ntcCfgObjects=_NtcCfgObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1500,1))
if mibBuilder.loadTexts:ntcCfgObjects.setStatus(_A)
_NtcCfgConfigTable_Object=MibTable
ntcCfgConfigTable=_NtcCfgConfigTable_Object((1,3,6,1,4,1,5835,5,2,1500,1,1))
if mibBuilder.loadTexts:ntcCfgConfigTable.setStatus(_A)
_NtcCfgConfigEntry_Object=MibTableRow
ntcCfgConfigEntry=_NtcCfgConfigEntry_Object((1,3,6,1,4,1,5835,5,2,1500,1,1,1))
ntcCfgConfigEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:ntcCfgConfigEntry.setStatus(_A)
class _NtcCfgConfigIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NtcCfgConfigIndex_Type.__name__=_G
_NtcCfgConfigIndex_Object=MibTableColumn
ntcCfgConfigIndex=_NtcCfgConfigIndex_Object((1,3,6,1,4,1,5835,5,2,1500,1,1,1,1),_NtcCfgConfigIndex_Type())
ntcCfgConfigIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ntcCfgConfigIndex.setStatus(_A)
class _NtcCfgConfigName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,240))
_NtcCfgConfigName_Type.__name__=_C
_NtcCfgConfigName_Object=MibTableColumn
ntcCfgConfigName=_NtcCfgConfigName_Object((1,3,6,1,4,1,5835,5,2,1500,1,1,1,2),_NtcCfgConfigName_Type())
ntcCfgConfigName.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcCfgConfigName.setStatus(_A)
class _NtcCfgActiveConfig_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,240))
_NtcCfgActiveConfig_Type.__name__=_C
_NtcCfgActiveConfig_Object=MibScalar
ntcCfgActiveConfig=_NtcCfgActiveConfig_Object((1,3,6,1,4,1,5835,5,2,1500,1,2),_NtcCfgActiveConfig_Type())
ntcCfgActiveConfig.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcCfgActiveConfig.setStatus(_A)
_NtcCfgUnsavedChanges_Type=TruthValue
_NtcCfgUnsavedChanges_Object=MibScalar
ntcCfgUnsavedChanges=_NtcCfgUnsavedChanges_Object((1,3,6,1,4,1,5835,5,2,1500,1,3),_NtcCfgUnsavedChanges_Type())
ntcCfgUnsavedChanges.setMaxAccess(_F)
if mibBuilder.loadTexts:ntcCfgUnsavedChanges.setStatus(_A)
class _NtcCfgBootConfig_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,240))
_NtcCfgBootConfig_Type.__name__=_C
_NtcCfgBootConfig_Object=MibScalar
ntcCfgBootConfig=_NtcCfgBootConfig_Object((1,3,6,1,4,1,5835,5,2,1500,1,4),_NtcCfgBootConfig_Type())
ntcCfgBootConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcCfgBootConfig.setStatus(_A)
class _NtcCfgLoadConfig_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,240))
_NtcCfgLoadConfig_Type.__name__=_C
_NtcCfgLoadConfig_Object=MibScalar
ntcCfgLoadConfig=_NtcCfgLoadConfig_Object((1,3,6,1,4,1,5835,5,2,1500,1,5),_NtcCfgLoadConfig_Type())
ntcCfgLoadConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcCfgLoadConfig.setStatus(_A)
class _NtcCfgSaveConfig_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,240))
_NtcCfgSaveConfig_Type.__name__=_C
_NtcCfgSaveConfig_Object=MibScalar
ntcCfgSaveConfig=_NtcCfgSaveConfig_Object((1,3,6,1,4,1,5835,5,2,1500,1,6),_NtcCfgSaveConfig_Type())
ntcCfgSaveConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcCfgSaveConfig.setStatus(_A)
class _NtcCfgDeleteConfig_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,240))
_NtcCfgDeleteConfig_Type.__name__=_C
_NtcCfgDeleteConfig_Object=MibScalar
ntcCfgDeleteConfig=_NtcCfgDeleteConfig_Object((1,3,6,1,4,1,5835,5,2,1500,1,7),_NtcCfgDeleteConfig_Type())
ntcCfgDeleteConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcCfgDeleteConfig.setStatus(_A)
class _NtcCfgLoadConfigNotForced_Type(DisplayString):defaultValue=OctetString(_D);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,240))
_NtcCfgLoadConfigNotForced_Type.__name__=_C
_NtcCfgLoadConfigNotForced_Object=MibScalar
ntcCfgLoadConfigNotForced=_NtcCfgLoadConfigNotForced_Object((1,3,6,1,4,1,5835,5,2,1500,1,8),_NtcCfgLoadConfigNotForced_Type())
ntcCfgLoadConfigNotForced.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcCfgLoadConfigNotForced.setStatus(_A)
_NtcCfgConformance_ObjectIdentity=ObjectIdentity
ntcCfgConformance=_NtcCfgConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1500,2))
if mibBuilder.loadTexts:ntcCfgConformance.setStatus(_A)
_NtcCfgConfCompliance_ObjectIdentity=ObjectIdentity
ntcCfgConfCompliance=_NtcCfgConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1500,2,1))
if mibBuilder.loadTexts:ntcCfgConfCompliance.setStatus(_A)
_NtcCfgConfGroup_ObjectIdentity=ObjectIdentity
ntcCfgConfGroup=_NtcCfgConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1500,2,2))
if mibBuilder.loadTexts:ntcCfgConfGroup.setStatus(_A)
ntcCfgConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,1500,2,2,1))
ntcCfgConfGrpV1Standard.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ntcCfgConfGrpV1Standard.setStatus(_A)
ntcCfgConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,1500,2,1,1))
ntcCfgConfCompV1Standard.setObjects((_B,_Q))
if mibBuilder.loadTexts:ntcCfgConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcConfig':ntcConfig,'ntcCfgObjects':ntcCfgObjects,'ntcCfgConfigTable':ntcCfgConfigTable,'ntcCfgConfigEntry':ntcCfgConfigEntry,_H:ntcCfgConfigIndex,_I:ntcCfgConfigName,_J:ntcCfgActiveConfig,_K:ntcCfgUnsavedChanges,_L:ntcCfgBootConfig,_M:ntcCfgLoadConfig,_N:ntcCfgSaveConfig,_O:ntcCfgDeleteConfig,_P:ntcCfgLoadConfigNotForced,'ntcCfgConformance':ntcCfgConformance,'ntcCfgConfCompliance':ntcCfgConfCompliance,'ntcCfgConfCompV1Standard':ntcCfgConfCompV1Standard,'ntcCfgConfGroup':ntcCfgConfGroup,_Q:ntcCfgConfGrpV1Standard})