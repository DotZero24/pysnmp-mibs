_T='mapsDbCategory'
_S='mapsConfigAction'
_R='mapsConfigCondition'
_Q='mapsConfigSeverityLevel'
_P='mapsConfigMsList'
_O='mapsConfigNumOfMS'
_N='mapsConfigObjectKeyValue'
_M='mapsConfigObjectKeyType'
_L='mapsConfigObjectGroupType'
_K='mapsConfigRuleName'
_J='string'
_I='uint32'
_H='2015-01-13 14:00'
_G='swVfId'
_F='BROCADE-SYSTEM-MIB'
_E='Integer32'
_D='OctetString'
_C='BROCADE-MAPS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
swVfId,=mibBuilder.importSymbols(_F,_G)
bcsiModules,=mibBuilder.importSymbols('Brocade-REG-MIB','bcsiModules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
maps=ModuleIdentity((1,3,6,1,4,1,1588,3,1,4))
if mibBuilder.loadTexts:maps.setRevisions(('2013-03-01 14:00','2013-04-22 13:30',_H,_H))
_MapsTraps_ObjectIdentity=ObjectIdentity
mapsTraps=_MapsTraps_ObjectIdentity((1,3,6,1,4,1,1588,3,1,4,0))
if mibBuilder.loadTexts:mapsTraps.setStatus(_A)
_MapsConfig_ObjectIdentity=ObjectIdentity
mapsConfig=_MapsConfig_ObjectIdentity((1,3,6,1,4,1,1588,3,1,4,1))
if mibBuilder.loadTexts:mapsConfig.setStatus(_A)
class _MapsConfigRuleName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_MapsConfigRuleName_Type.__name__=_D
_MapsConfigRuleName_Object=MibScalar
mapsConfigRuleName=_MapsConfigRuleName_Object((1,3,6,1,4,1,1588,3,1,4,1,1),_MapsConfigRuleName_Type())
mapsConfigRuleName.setMaxAccess(_B)
if mibBuilder.loadTexts:mapsConfigRuleName.setStatus(_A)
class _MapsConfigCondition_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_MapsConfigCondition_Type.__name__=_D
_MapsConfigCondition_Object=MibScalar
mapsConfigCondition=_MapsConfigCondition_Object((1,3,6,1,4,1,1588,3,1,4,1,2),_MapsConfigCondition_Type())
mapsConfigCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:mapsConfigCondition.setStatus(_A)
_MapsConfigNumOfMS_Type=Integer32
_MapsConfigNumOfMS_Object=MibScalar
mapsConfigNumOfMS=_MapsConfigNumOfMS_Object((1,3,6,1,4,1,1588,3,1,4,1,3),_MapsConfigNumOfMS_Type())
mapsConfigNumOfMS.setMaxAccess(_B)
if mibBuilder.loadTexts:mapsConfigNumOfMS.setStatus(_A)
class _MapsConfigMsName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_MapsConfigMsName_Type.__name__=_D
_MapsConfigMsName_Object=MibScalar
mapsConfigMsName=_MapsConfigMsName_Object((1,3,6,1,4,1,1588,3,1,4,1,4),_MapsConfigMsName_Type())
mapsConfigMsName.setMaxAccess(_B)
if mibBuilder.loadTexts:mapsConfigMsName.setStatus(_A)
class _MapsConfigObjectGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('unknown',1),('ps',2),('fan',3),('port',4),('ve-port-cir',5),('ts',6),('slot',7),('gbic',8),('flash',9),('rule',10),('switch',11),('chassis',12),('cpu',13),('wwn',14),('flow',15),('eth-port',16)))
_MapsConfigObjectGroupType_Type.__name__=_E
_MapsConfigObjectGroupType_Object=MibScalar
mapsConfigObjectGroupType=_MapsConfigObjectGroupType_Object((1,3,6,1,4,1,1588,3,1,4,1,5),_MapsConfigObjectGroupType_Type())
mapsConfigObjectGroupType.setMaxAccess(_B)
if mibBuilder.loadTexts:mapsConfigObjectGroupType.setStatus(_A)
class _MapsConfigObjectKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('int32',1),(_I,2),('float',3),(_J,4)))
_MapsConfigObjectKeyType_Type.__name__=_E
_MapsConfigObjectKeyType_Object=MibScalar
mapsConfigObjectKeyType=_MapsConfigObjectKeyType_Object((1,3,6,1,4,1,1588,3,1,4,1,6),_MapsConfigObjectKeyType_Type())
mapsConfigObjectKeyType.setMaxAccess(_B)
if mibBuilder.loadTexts:mapsConfigObjectKeyType.setStatus(_A)
class _MapsConfigObjectKeyValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_MapsConfigObjectKeyValue_Type.__name__=_D
_MapsConfigObjectKeyValue_Object=MibScalar
mapsConfigObjectKeyValue=_MapsConfigObjectKeyValue_Object((1,3,6,1,4,1,1588,3,1,4,1,7),_MapsConfigObjectKeyValue_Type())
mapsConfigObjectKeyValue.setMaxAccess(_B)
if mibBuilder.loadTexts:mapsConfigObjectKeyValue.setStatus(_A)
class _MapsConfigValueType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('int32',1),(_I,2),('float',3),(_J,4)))
_MapsConfigValueType_Type.__name__=_E
_MapsConfigValueType_Object=MibScalar
mapsConfigValueType=_MapsConfigValueType_Object((1,3,6,1,4,1,1588,3,1,4,1,8),_MapsConfigValueType_Type())
mapsConfigValueType.setMaxAccess(_B)
if mibBuilder.loadTexts:mapsConfigValueType.setStatus(_A)
class _MapsConfigCurrentValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_MapsConfigCurrentValue_Type.__name__=_D
_MapsConfigCurrentValue_Object=MibScalar
mapsConfigCurrentValue=_MapsConfigCurrentValue_Object((1,3,6,1,4,1,1588,3,1,4,1,9),_MapsConfigCurrentValue_Type())
mapsConfigCurrentValue.setMaxAccess(_B)
if mibBuilder.loadTexts:mapsConfigCurrentValue.setStatus(_A)
class _MapsConfigTimeBase_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_MapsConfigTimeBase_Type.__name__=_D
_MapsConfigTimeBase_Object=MibScalar
mapsConfigTimeBase=_MapsConfigTimeBase_Object((1,3,6,1,4,1,1588,3,1,4,1,10),_MapsConfigTimeBase_Type())
mapsConfigTimeBase.setMaxAccess(_B)
if mibBuilder.loadTexts:mapsConfigTimeBase.setStatus(_A)
class _MapsConfigSeverityLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('critical',1),('error',2),('warning',3),('informational',4),('debug',5)))
_MapsConfigSeverityLevel_Type.__name__=_E
_MapsConfigSeverityLevel_Object=MibScalar
mapsConfigSeverityLevel=_MapsConfigSeverityLevel_Object((1,3,6,1,4,1,1588,3,1,4,1,11),_MapsConfigSeverityLevel_Type())
mapsConfigSeverityLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:mapsConfigSeverityLevel.setStatus(_A)
class _MapsConfigMsList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_MapsConfigMsList_Type.__name__=_D
_MapsConfigMsList_Object=MibScalar
mapsConfigMsList=_MapsConfigMsList_Object((1,3,6,1,4,1,1588,3,1,4,1,12),_MapsConfigMsList_Type())
mapsConfigMsList.setMaxAccess(_B)
if mibBuilder.loadTexts:mapsConfigMsList.setStatus(_A)
_MapsConfigAction_Type=Integer32
_MapsConfigAction_Object=MibScalar
mapsConfigAction=_MapsConfigAction_Object((1,3,6,1,4,1,1588,3,1,4,1,13),_MapsConfigAction_Type())
mapsConfigAction.setMaxAccess(_B)
if mibBuilder.loadTexts:mapsConfigAction.setStatus(_A)
class _MapsDbCategory_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(24,24));fixedLength=24
_MapsDbCategory_Type.__name__=_D
_MapsDbCategory_Object=MibScalar
mapsDbCategory=_MapsDbCategory_Object((1,3,6,1,4,1,1588,3,1,4,1,14),_MapsDbCategory_Type())
mapsDbCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:mapsDbCategory.setStatus(_A)
mapsTrapAM=NotificationType((1,3,6,1,4,1,1588,3,1,4,0,1))
mapsTrapAM.setObjects(*((_C,_K),(_C,_L),(_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q),(_C,_R),(_C,_S),(_F,_G),(_C,_T)))
if mibBuilder.loadTexts:mapsTrapAM.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'maps':maps,'mapsTraps':mapsTraps,'mapsTrapAM':mapsTrapAM,'mapsConfig':mapsConfig,_K:mapsConfigRuleName,_R:mapsConfigCondition,_O:mapsConfigNumOfMS,'mapsConfigMsName':mapsConfigMsName,_L:mapsConfigObjectGroupType,_M:mapsConfigObjectKeyType,_N:mapsConfigObjectKeyValue,'mapsConfigValueType':mapsConfigValueType,'mapsConfigCurrentValue':mapsConfigCurrentValue,'mapsConfigTimeBase':mapsConfigTimeBase,_Q:mapsConfigSeverityLevel,_P:mapsConfigMsList,_S:mapsConfigAction,_T:mapsDbCategory})