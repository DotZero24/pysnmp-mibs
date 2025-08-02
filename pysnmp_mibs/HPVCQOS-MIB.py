_R='vcQoSGroup'
_Q='vcQoSDscpMap'
_P='vcQoSDot1pMap'
_O='vcQoSClassificationMap'
_N='vcQoSTrafficClass'
_M='vcQoSTrafficClassConfig'
_L='vcQoSIfQoSConfig'
_K='vcQoSDscpMapDscpValue'
_J='vcQoSDot1pMapPrioValue'
_I='vcQoSTrafficClassId'
_H='ifIndex'
_G='IF-MIB'
_F='vcQoSTrafficClassConfigIndex'
_E='vcQoSClassificationMapIndex'
_D='Integer32'
_C='HPVCQOS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
virtualConnect,=mibBuilder.importSymbols('HPVCMODULE-MIB','virtualConnect')
ifIndex,=mibBuilder.importSymbols(_G,_H)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mib-2')
DisplayString,PhysAddress,RowPointer,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','TextualConvention','TruthValue')
vcQoSMIB=ModuleIdentity((1,3,6,1,4,1,11,5,7,5,2,5))
if mibBuilder.loadTexts:vcQoSMIB.setRevisions(('2016-03-21 00:00','2015-01-07 00:00','2012-04-25 00:00'))
class VcQoSConfigType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('passthrough',2),('customFCoE',3),('customNoFCoE',4)))
_VcQoSMIBObjects_ObjectIdentity=ObjectIdentity
vcQoSMIBObjects=_VcQoSMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,5,1))
_VcQoSConfigType_Type=VcQoSConfigType
_VcQoSConfigType_Object=MibScalar
vcQoSConfigType=_VcQoSConfigType_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,1),_VcQoSConfigType_Type())
vcQoSConfigType.setMaxAccess(_B)
if mibBuilder.loadTexts:vcQoSConfigType.setStatus(_A)
_VcQoSIfQoSConfig_ObjectIdentity=ObjectIdentity
vcQoSIfQoSConfig=_VcQoSIfQoSConfig_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,5,1,2))
_VcQoSIfQoSConfigTable_Object=MibTable
vcQoSIfQoSConfigTable=_VcQoSIfQoSConfigTable_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,2,1))
if mibBuilder.loadTexts:vcQoSIfQoSConfigTable.setStatus(_A)
_VcQoSIfQoSConfigEntry_Object=MibTableRow
vcQoSIfQoSConfigEntry=_VcQoSIfQoSConfigEntry_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,2,1,1))
vcQoSIfQoSConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:vcQoSIfQoSConfigEntry.setStatus(_A)
_VcQoSIfQoSTrafficClassConfigIndex_Type=Integer32
_VcQoSIfQoSTrafficClassConfigIndex_Object=MibTableColumn
vcQoSIfQoSTrafficClassConfigIndex=_VcQoSIfQoSTrafficClassConfigIndex_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,2,1,1,1),_VcQoSIfQoSTrafficClassConfigIndex_Type())
vcQoSIfQoSTrafficClassConfigIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vcQoSIfQoSTrafficClassConfigIndex.setStatus(_A)
_VcQoSIfQoSClassificationMapIndex_Type=Integer32
_VcQoSIfQoSClassificationMapIndex_Object=MibTableColumn
vcQoSIfQoSClassificationMapIndex=_VcQoSIfQoSClassificationMapIndex_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,2,1,1,2),_VcQoSIfQoSClassificationMapIndex_Type())
vcQoSIfQoSClassificationMapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vcQoSIfQoSClassificationMapIndex.setStatus(_A)
_VcQoSTrafficClassConfig_ObjectIdentity=ObjectIdentity
vcQoSTrafficClassConfig=_VcQoSTrafficClassConfig_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,5,1,3))
_VcQoSTrafficClassConfigTable_Object=MibTable
vcQoSTrafficClassConfigTable=_VcQoSTrafficClassConfigTable_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,3,1))
if mibBuilder.loadTexts:vcQoSTrafficClassConfigTable.setStatus(_A)
_VcQoSTrafficClassConfigEntry_Object=MibTableRow
vcQoSTrafficClassConfigEntry=_VcQoSTrafficClassConfigEntry_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,3,1,1))
vcQoSTrafficClassConfigEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:vcQoSTrafficClassConfigEntry.setStatus(_A)
_VcQoSTrafficClassConfigIndex_Type=Integer32
_VcQoSTrafficClassConfigIndex_Object=MibTableColumn
vcQoSTrafficClassConfigIndex=_VcQoSTrafficClassConfigIndex_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,3,1,1,1),_VcQoSTrafficClassConfigIndex_Type())
vcQoSTrafficClassConfigIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vcQoSTrafficClassConfigIndex.setStatus(_A)
_VcQoSTrafficClassConfigName_Type=SnmpAdminString
_VcQoSTrafficClassConfigName_Object=MibTableColumn
vcQoSTrafficClassConfigName=_VcQoSTrafficClassConfigName_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,3,1,1,2),_VcQoSTrafficClassConfigName_Type())
vcQoSTrafficClassConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:vcQoSTrafficClassConfigName.setStatus(_A)
_VcQoSTrafficClass_ObjectIdentity=ObjectIdentity
vcQoSTrafficClass=_VcQoSTrafficClass_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,5,1,4))
_VcQoSTrafficClassTable_Object=MibTable
vcQoSTrafficClassTable=_VcQoSTrafficClassTable_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,4,1))
if mibBuilder.loadTexts:vcQoSTrafficClassTable.setStatus(_A)
_VcQoSTrafficClassEntry_Object=MibTableRow
vcQoSTrafficClassEntry=_VcQoSTrafficClassEntry_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,4,1,1))
vcQoSTrafficClassEntry.setIndexNames((0,_C,_F),(0,_C,_I))
if mibBuilder.loadTexts:vcQoSTrafficClassEntry.setStatus(_A)
class _VcQoSTrafficClassId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_VcQoSTrafficClassId_Type.__name__=_D
_VcQoSTrafficClassId_Object=MibTableColumn
vcQoSTrafficClassId=_VcQoSTrafficClassId_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,4,1,1,1),_VcQoSTrafficClassId_Type())
vcQoSTrafficClassId.setMaxAccess(_B)
if mibBuilder.loadTexts:vcQoSTrafficClassId.setStatus(_A)
_VcQoSTrafficClassName_Type=SnmpAdminString
_VcQoSTrafficClassName_Object=MibTableColumn
vcQoSTrafficClassName=_VcQoSTrafficClassName_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,4,1,1,2),_VcQoSTrafficClassName_Type())
vcQoSTrafficClassName.setMaxAccess(_B)
if mibBuilder.loadTexts:vcQoSTrafficClassName.setStatus(_A)
_VcQoSTrafficClassRealTime_Type=TruthValue
_VcQoSTrafficClassRealTime_Object=MibTableColumn
vcQoSTrafficClassRealTime=_VcQoSTrafficClassRealTime_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,4,1,1,3),_VcQoSTrafficClassRealTime_Type())
vcQoSTrafficClassRealTime.setMaxAccess(_B)
if mibBuilder.loadTexts:vcQoSTrafficClassRealTime.setStatus(_A)
class _VcQoSTrafficClassShare_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_VcQoSTrafficClassShare_Type.__name__=_D
_VcQoSTrafficClassShare_Object=MibTableColumn
vcQoSTrafficClassShare=_VcQoSTrafficClassShare_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,4,1,1,4),_VcQoSTrafficClassShare_Type())
vcQoSTrafficClassShare.setMaxAccess(_B)
if mibBuilder.loadTexts:vcQoSTrafficClassShare.setStatus(_A)
class _VcQoSTrafficClassMaxShare_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_VcQoSTrafficClassMaxShare_Type.__name__=_D
_VcQoSTrafficClassMaxShare_Object=MibTableColumn
vcQoSTrafficClassMaxShare=_VcQoSTrafficClassMaxShare_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,4,1,1,5),_VcQoSTrafficClassMaxShare_Type())
vcQoSTrafficClassMaxShare.setMaxAccess(_B)
if mibBuilder.loadTexts:vcQoSTrafficClassMaxShare.setStatus(_A)
class _VcQoSTrafficClassEgressDot1pPrio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_VcQoSTrafficClassEgressDot1pPrio_Type.__name__=_D
_VcQoSTrafficClassEgressDot1pPrio_Object=MibTableColumn
vcQoSTrafficClassEgressDot1pPrio=_VcQoSTrafficClassEgressDot1pPrio_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,4,1,1,6),_VcQoSTrafficClassEgressDot1pPrio_Type())
vcQoSTrafficClassEgressDot1pPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:vcQoSTrafficClassEgressDot1pPrio.setStatus(_A)
_VcQoSTrafficClassEnabled_Type=TruthValue
_VcQoSTrafficClassEnabled_Object=MibTableColumn
vcQoSTrafficClassEnabled=_VcQoSTrafficClassEnabled_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,4,1,1,7),_VcQoSTrafficClassEnabled_Type())
vcQoSTrafficClassEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:vcQoSTrafficClassEnabled.setStatus(_A)
_VcQoSClassificationMap_ObjectIdentity=ObjectIdentity
vcQoSClassificationMap=_VcQoSClassificationMap_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,5,1,5))
_VcQoSClassificationMapTable_Object=MibTable
vcQoSClassificationMapTable=_VcQoSClassificationMapTable_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,5,1))
if mibBuilder.loadTexts:vcQoSClassificationMapTable.setStatus(_A)
_VcQoSClassificationMapEntry_Object=MibTableRow
vcQoSClassificationMapEntry=_VcQoSClassificationMapEntry_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,5,1,1))
vcQoSClassificationMapEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:vcQoSClassificationMapEntry.setStatus(_A)
_VcQoSClassificationMapIndex_Type=Integer32
_VcQoSClassificationMapIndex_Object=MibTableColumn
vcQoSClassificationMapIndex=_VcQoSClassificationMapIndex_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,5,1,1,1),_VcQoSClassificationMapIndex_Type())
vcQoSClassificationMapIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:vcQoSClassificationMapIndex.setStatus(_A)
_VcQoSClassificationMapName_Type=SnmpAdminString
_VcQoSClassificationMapName_Object=MibTableColumn
vcQoSClassificationMapName=_VcQoSClassificationMapName_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,5,1,1,2),_VcQoSClassificationMapName_Type())
vcQoSClassificationMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:vcQoSClassificationMapName.setStatus(_A)
_VcQoSDot1pMap_ObjectIdentity=ObjectIdentity
vcQoSDot1pMap=_VcQoSDot1pMap_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,5,1,6))
_VcQoSDot1pMapTable_Object=MibTable
vcQoSDot1pMapTable=_VcQoSDot1pMapTable_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,6,1))
if mibBuilder.loadTexts:vcQoSDot1pMapTable.setStatus(_A)
_VcQoSDot1pMapEntry_Object=MibTableRow
vcQoSDot1pMapEntry=_VcQoSDot1pMapEntry_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,6,1,1))
vcQoSDot1pMapEntry.setIndexNames((0,_C,_E),(0,_C,_J))
if mibBuilder.loadTexts:vcQoSDot1pMapEntry.setStatus(_A)
class _VcQoSDot1pMapPrioValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_VcQoSDot1pMapPrioValue_Type.__name__=_D
_VcQoSDot1pMapPrioValue_Object=MibTableColumn
vcQoSDot1pMapPrioValue=_VcQoSDot1pMapPrioValue_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,6,1,1,1),_VcQoSDot1pMapPrioValue_Type())
vcQoSDot1pMapPrioValue.setMaxAccess(_B)
if mibBuilder.loadTexts:vcQoSDot1pMapPrioValue.setStatus(_A)
class _VcQoSDot1pMapTrafficClassId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_VcQoSDot1pMapTrafficClassId_Type.__name__=_D
_VcQoSDot1pMapTrafficClassId_Object=MibTableColumn
vcQoSDot1pMapTrafficClassId=_VcQoSDot1pMapTrafficClassId_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,6,1,1,2),_VcQoSDot1pMapTrafficClassId_Type())
vcQoSDot1pMapTrafficClassId.setMaxAccess(_B)
if mibBuilder.loadTexts:vcQoSDot1pMapTrafficClassId.setStatus(_A)
_VcQoSDscpMap_ObjectIdentity=ObjectIdentity
vcQoSDscpMap=_VcQoSDscpMap_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,5,1,7))
_VcQoSDscpMapTable_Object=MibTable
vcQoSDscpMapTable=_VcQoSDscpMapTable_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,7,1))
if mibBuilder.loadTexts:vcQoSDscpMapTable.setStatus(_A)
_VcQoSDscpMapEntry_Object=MibTableRow
vcQoSDscpMapEntry=_VcQoSDscpMapEntry_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,7,1,1))
vcQoSDscpMapEntry.setIndexNames((0,_C,_E),(0,_C,_K))
if mibBuilder.loadTexts:vcQoSDscpMapEntry.setStatus(_A)
class _VcQoSDscpMapDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_VcQoSDscpMapDscpValue_Type.__name__=_D
_VcQoSDscpMapDscpValue_Object=MibTableColumn
vcQoSDscpMapDscpValue=_VcQoSDscpMapDscpValue_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,7,1,1,1),_VcQoSDscpMapDscpValue_Type())
vcQoSDscpMapDscpValue.setMaxAccess(_B)
if mibBuilder.loadTexts:vcQoSDscpMapDscpValue.setStatus(_A)
class _VcQoSDscpMapTrafficClassId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_VcQoSDscpMapTrafficClassId_Type.__name__=_D
_VcQoSDscpMapTrafficClassId_Object=MibTableColumn
vcQoSDscpMapTrafficClassId=_VcQoSDscpMapTrafficClassId_Object((1,3,6,1,4,1,11,5,7,5,2,5,1,7,1,1,2),_VcQoSDscpMapTrafficClassId_Type())
vcQoSDscpMapTrafficClassId.setMaxAccess(_B)
if mibBuilder.loadTexts:vcQoSDscpMapTrafficClassId.setStatus(_A)
_VcQoSMIBConformance_ObjectIdentity=ObjectIdentity
vcQoSMIBConformance=_VcQoSMIBConformance_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,5,2))
_VcQoSMIBCompliances_ObjectIdentity=ObjectIdentity
vcQoSMIBCompliances=_VcQoSMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,5,2,1))
_VcQoSMIBGroups_ObjectIdentity=ObjectIdentity
vcQoSMIBGroups=_VcQoSMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,5,2,2))
vcQoSGroup=ObjectGroup((1,3,6,1,4,1,11,5,7,5,2,5,2,2,1))
vcQoSGroup.setObjects(*((_C,_L),(_C,_M),(_C,_N),(_C,_O),(_C,_P),(_C,_Q)))
if mibBuilder.loadTexts:vcQoSGroup.setStatus(_A)
vcQoSMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,5,7,5,2,5,2,1,1))
vcQoSMIBCompliance.setObjects((_C,_R))
if mibBuilder.loadTexts:vcQoSMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'VcQoSConfigType':VcQoSConfigType,'vcQoSMIB':vcQoSMIB,'vcQoSMIBObjects':vcQoSMIBObjects,'vcQoSConfigType':vcQoSConfigType,_L:vcQoSIfQoSConfig,'vcQoSIfQoSConfigTable':vcQoSIfQoSConfigTable,'vcQoSIfQoSConfigEntry':vcQoSIfQoSConfigEntry,'vcQoSIfQoSTrafficClassConfigIndex':vcQoSIfQoSTrafficClassConfigIndex,'vcQoSIfQoSClassificationMapIndex':vcQoSIfQoSClassificationMapIndex,_M:vcQoSTrafficClassConfig,'vcQoSTrafficClassConfigTable':vcQoSTrafficClassConfigTable,'vcQoSTrafficClassConfigEntry':vcQoSTrafficClassConfigEntry,_F:vcQoSTrafficClassConfigIndex,'vcQoSTrafficClassConfigName':vcQoSTrafficClassConfigName,_N:vcQoSTrafficClass,'vcQoSTrafficClassTable':vcQoSTrafficClassTable,'vcQoSTrafficClassEntry':vcQoSTrafficClassEntry,_I:vcQoSTrafficClassId,'vcQoSTrafficClassName':vcQoSTrafficClassName,'vcQoSTrafficClassRealTime':vcQoSTrafficClassRealTime,'vcQoSTrafficClassShare':vcQoSTrafficClassShare,'vcQoSTrafficClassMaxShare':vcQoSTrafficClassMaxShare,'vcQoSTrafficClassEgressDot1pPrio':vcQoSTrafficClassEgressDot1pPrio,'vcQoSTrafficClassEnabled':vcQoSTrafficClassEnabled,_O:vcQoSClassificationMap,'vcQoSClassificationMapTable':vcQoSClassificationMapTable,'vcQoSClassificationMapEntry':vcQoSClassificationMapEntry,_E:vcQoSClassificationMapIndex,'vcQoSClassificationMapName':vcQoSClassificationMapName,_P:vcQoSDot1pMap,'vcQoSDot1pMapTable':vcQoSDot1pMapTable,'vcQoSDot1pMapEntry':vcQoSDot1pMapEntry,_J:vcQoSDot1pMapPrioValue,'vcQoSDot1pMapTrafficClassId':vcQoSDot1pMapTrafficClassId,_Q:vcQoSDscpMap,'vcQoSDscpMapTable':vcQoSDscpMapTable,'vcQoSDscpMapEntry':vcQoSDscpMapEntry,_K:vcQoSDscpMapDscpValue,'vcQoSDscpMapTrafficClassId':vcQoSDscpMapTrafficClassId,'vcQoSMIBConformance':vcQoSMIBConformance,'vcQoSMIBCompliances':vcQoSMIBCompliances,'vcQoSMIBCompliance':vcQoSMIBCompliance,'vcQoSMIBGroups':vcQoSMIBGroups,_R:vcQoSGroup})