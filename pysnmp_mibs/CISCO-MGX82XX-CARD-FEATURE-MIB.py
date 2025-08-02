_N='cmCoreCardFeatureGroup'
_M='cmAscCardFeatureGroup'
_L='cmPxmCardFeatureGroup'
_K='switchCoreCard'
_J='redundancyAllowed'
_I='pxmCardCacMode'
_H='trkCACEnable'
_G='apsCardAttributes'
_F='vsiControllersAllowed'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='CISCO-MGX82XX-CARD-FEATURE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cardSpecific,=mibBuilder.importSymbols('BASIS-MIB','cardSpecific')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoMgx82xxCardFeatureMIB=ModuleIdentity((1,3,6,1,4,1,351,150,74))
if mibBuilder.loadTexts:ciscoMgx82xxCardFeatureMIB.setRevisions(('2003-05-05 00:00',))
_AscFeatures_ObjectIdentity=ObjectIdentity
ascFeatures=_AscFeatures_ObjectIdentity((1,3,6,1,4,1,351,110,3,5))
class _RedundancyAllowed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('redNotAllowed',1),('redAllowed',2)))
_RedundancyAllowed_Type.__name__=_C
_RedundancyAllowed_Object=MibScalar
redundancyAllowed=_RedundancyAllowed_Object((1,3,6,1,4,1,351,110,3,5,1),_RedundancyAllowed_Type())
redundancyAllowed.setMaxAccess(_D)
if mibBuilder.loadTexts:redundancyAllowed.setStatus(_A)
_PxmFeatures_ObjectIdentity=ObjectIdentity
pxmFeatures=_PxmFeatures_ObjectIdentity((1,3,6,1,4,1,351,110,3,15))
class _VsiControllersAllowed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_VsiControllersAllowed_Type.__name__=_C
_VsiControllersAllowed_Object=MibScalar
vsiControllersAllowed=_VsiControllersAllowed_Object((1,3,6,1,4,1,351,110,3,15,1),_VsiControllersAllowed_Type())
vsiControllersAllowed.setMaxAccess(_D)
if mibBuilder.loadTexts:vsiControllersAllowed.setStatus(_A)
class _ApsCardAttributes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ApsCardAttributes_Type.__name__=_C
_ApsCardAttributes_Object=MibScalar
apsCardAttributes=_ApsCardAttributes_Object((1,3,6,1,4,1,351,110,3,15,2),_ApsCardAttributes_Type())
apsCardAttributes.setMaxAccess(_D)
if mibBuilder.loadTexts:apsCardAttributes.setStatus(_A)
class _TrkCACEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_TrkCACEnable_Type.__name__=_C
_TrkCACEnable_Object=MibScalar
trkCACEnable=_TrkCACEnable_Object((1,3,6,1,4,1,351,110,3,15,3),_TrkCACEnable_Type())
trkCACEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:trkCACEnable.setStatus(_A)
class _PxmCardCacMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pcrBasedCac',1),('scrBasedCac',2)))
_PxmCardCacMode_Type.__name__=_C
_PxmCardCacMode_Object=MibScalar
pxmCardCacMode=_PxmCardCacMode_Object((1,3,6,1,4,1,351,110,3,15,4),_PxmCardCacMode_Type())
pxmCardCacMode.setMaxAccess(_E)
if mibBuilder.loadTexts:pxmCardCacMode.setStatus(_A)
_CoreCardCommands_ObjectIdentity=ObjectIdentity
coreCardCommands=_CoreCardCommands_ObjectIdentity((1,3,6,1,4,1,351,110,3,20))
class _SwitchCoreCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noAction',1),('doswitchcc',2),('instswitchcc',3),('fallbackswitchcc',4)))
_SwitchCoreCard_Type.__name__=_C
_SwitchCoreCard_Object=MibScalar
switchCoreCard=_SwitchCoreCard_Object((1,3,6,1,4,1,351,110,3,20,1),_SwitchCoreCard_Type())
switchCoreCard.setMaxAccess(_E)
if mibBuilder.loadTexts:switchCoreCard.setStatus(_A)
_CmCardFeatureMIBConformance_ObjectIdentity=ObjectIdentity
cmCardFeatureMIBConformance=_CmCardFeatureMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,74,2))
_CmCardFeatureMIBGroups_ObjectIdentity=ObjectIdentity
cmCardFeatureMIBGroups=_CmCardFeatureMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,74,2,1))
_CmCardFeatureMIBCompliances_ObjectIdentity=ObjectIdentity
cmCardFeatureMIBCompliances=_CmCardFeatureMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,74,2,2))
cmPxmCardFeatureGroup=ObjectGroup((1,3,6,1,4,1,351,150,74,2,1,1))
cmPxmCardFeatureGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:cmPxmCardFeatureGroup.setStatus(_A)
cmAscCardFeatureGroup=ObjectGroup((1,3,6,1,4,1,351,150,74,2,1,2))
cmAscCardFeatureGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:cmAscCardFeatureGroup.setStatus(_A)
cmCoreCardFeatureGroup=ObjectGroup((1,3,6,1,4,1,351,150,74,2,1,3))
cmCoreCardFeatureGroup.setObjects((_B,_K))
if mibBuilder.loadTexts:cmCoreCardFeatureGroup.setStatus(_A)
cmCardFeatureCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,74,2,2,1))
cmCardFeatureCompliance.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:cmCardFeatureCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ascFeatures':ascFeatures,_J:redundancyAllowed,'pxmFeatures':pxmFeatures,_F:vsiControllersAllowed,_G:apsCardAttributes,_H:trkCACEnable,_I:pxmCardCacMode,'coreCardCommands':coreCardCommands,_K:switchCoreCard,'ciscoMgx82xxCardFeatureMIB':ciscoMgx82xxCardFeatureMIB,'cmCardFeatureMIBConformance':cmCardFeatureMIBConformance,'cmCardFeatureMIBGroups':cmCardFeatureMIBGroups,_L:cmPxmCardFeatureGroup,_M:cmAscCardFeatureGroup,_N:cmCoreCardFeatureGroup,'cmCardFeatureMIBCompliances':cmCardFeatureMIBCompliances,'cmCardFeatureCompliance':cmCardFeatureCompliance})