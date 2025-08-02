_Y='ifXcFlexProcFuncMapGroupV1'
_X='ifXcFlexInterfaceConfigGroupV1'
_W='ifXcFlexGeneralGroupV1'
_V='ifXcFlexProcFuncMapProcFuncIndex'
_U='ifXcFlexProcFuncMapUId'
_T='ifXcFlexProcFuncMapType'
_S='ifXcFlexProcFuncMapName'
_R='ifXcFlexInterfaceConfigInterfaceType'
_Q='ifXcFlexInterfaceConfigProcFuncIndex'
_P='ifXcFlexInterfaceConfigUId'
_O='ifXcFlexInterfaceConfigName'
_N='ifXcFlexProcFuncMapStateLastChangeTime'
_M='ifXcFlexProcFuncMapConfigLastChangeTime'
_L='ifXcFlexProcFuncMapTableSize'
_K='ifXcFlexInterfaceConfigStateLastChangeTime'
_J='ifXcFlexInterfaceConfigConfigLastChangeTime'
_I='ifXcFlexInterfaceConfigTableSize'
_H='ifXcFlexGeneralStateLastChangeTime'
_G='ifXcFlexGeneralConfigLastChangeTime'
_F='ifXcFlexProcFuncMapIndex'
_E='ifXcFlexInterfaceConfigIndex'
_D='Integer32'
_C='read-only'
_B='LUM-IFXCFLEX-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumIfXcFlexMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumIfXcFlexMIB','lumModules')
MgmtNameString,Unsigned32WithNA=mibBuilder.importSymbols('LUM-TC','MgmtNameString','Unsigned32WithNA')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
lumIfXcFlexMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,70))
if mibBuilder.loadTexts:lumIfXcFlexMIBModule.setRevisions(('2017-06-15 00:00','2016-08-18 00:00'))
_LumIfXcFlexConfs_ObjectIdentity=ObjectIdentity
lumIfXcFlexConfs=_LumIfXcFlexConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,70,1))
_LumIfXcFlexGroups_ObjectIdentity=ObjectIdentity
lumIfXcFlexGroups=_LumIfXcFlexGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,70,1,1))
_LumIfXcFlexCompl_ObjectIdentity=ObjectIdentity
lumIfXcFlexCompl=_LumIfXcFlexCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,70,1,2))
_LumIfXcFlexMIBObjects_ObjectIdentity=ObjectIdentity
lumIfXcFlexMIBObjects=_LumIfXcFlexMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,70,2))
_IfXcFlexGeneral_ObjectIdentity=ObjectIdentity
ifXcFlexGeneral=_IfXcFlexGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,70,2,1))
_IfXcFlexGeneralConfigLastChangeTime_Type=DateAndTime
_IfXcFlexGeneralConfigLastChangeTime_Object=MibScalar
ifXcFlexGeneralConfigLastChangeTime=_IfXcFlexGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,70,2,1,1),_IfXcFlexGeneralConfigLastChangeTime_Type())
ifXcFlexGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcFlexGeneralConfigLastChangeTime.setStatus(_A)
_IfXcFlexGeneralStateLastChangeTime_Type=DateAndTime
_IfXcFlexGeneralStateLastChangeTime_Object=MibScalar
ifXcFlexGeneralStateLastChangeTime=_IfXcFlexGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,70,2,1,2),_IfXcFlexGeneralStateLastChangeTime_Type())
ifXcFlexGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcFlexGeneralStateLastChangeTime.setStatus(_A)
_IfXcFlexInterfaceConfigTableSize_Type=Unsigned32
_IfXcFlexInterfaceConfigTableSize_Object=MibScalar
ifXcFlexInterfaceConfigTableSize=_IfXcFlexInterfaceConfigTableSize_Object((1,3,6,1,4,1,8708,2,70,2,1,3),_IfXcFlexInterfaceConfigTableSize_Type())
ifXcFlexInterfaceConfigTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcFlexInterfaceConfigTableSize.setStatus(_A)
_IfXcFlexInterfaceConfigConfigLastChangeTime_Type=DateAndTime
_IfXcFlexInterfaceConfigConfigLastChangeTime_Object=MibScalar
ifXcFlexInterfaceConfigConfigLastChangeTime=_IfXcFlexInterfaceConfigConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,70,2,1,4),_IfXcFlexInterfaceConfigConfigLastChangeTime_Type())
ifXcFlexInterfaceConfigConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcFlexInterfaceConfigConfigLastChangeTime.setStatus(_A)
_IfXcFlexInterfaceConfigStateLastChangeTime_Type=DateAndTime
_IfXcFlexInterfaceConfigStateLastChangeTime_Object=MibScalar
ifXcFlexInterfaceConfigStateLastChangeTime=_IfXcFlexInterfaceConfigStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,70,2,1,5),_IfXcFlexInterfaceConfigStateLastChangeTime_Type())
ifXcFlexInterfaceConfigStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcFlexInterfaceConfigStateLastChangeTime.setStatus(_A)
_IfXcFlexProcFuncMapTableSize_Type=Unsigned32
_IfXcFlexProcFuncMapTableSize_Object=MibScalar
ifXcFlexProcFuncMapTableSize=_IfXcFlexProcFuncMapTableSize_Object((1,3,6,1,4,1,8708,2,70,2,1,6),_IfXcFlexProcFuncMapTableSize_Type())
ifXcFlexProcFuncMapTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcFlexProcFuncMapTableSize.setStatus(_A)
_IfXcFlexProcFuncMapConfigLastChangeTime_Type=DateAndTime
_IfXcFlexProcFuncMapConfigLastChangeTime_Object=MibScalar
ifXcFlexProcFuncMapConfigLastChangeTime=_IfXcFlexProcFuncMapConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,70,2,1,7),_IfXcFlexProcFuncMapConfigLastChangeTime_Type())
ifXcFlexProcFuncMapConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcFlexProcFuncMapConfigLastChangeTime.setStatus(_A)
_IfXcFlexProcFuncMapStateLastChangeTime_Type=DateAndTime
_IfXcFlexProcFuncMapStateLastChangeTime_Object=MibScalar
ifXcFlexProcFuncMapStateLastChangeTime=_IfXcFlexProcFuncMapStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,70,2,1,8),_IfXcFlexProcFuncMapStateLastChangeTime_Type())
ifXcFlexProcFuncMapStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcFlexProcFuncMapStateLastChangeTime.setStatus(_A)
_IfXcFlexInterfaceConfigList_ObjectIdentity=ObjectIdentity
ifXcFlexInterfaceConfigList=_IfXcFlexInterfaceConfigList_ObjectIdentity((1,3,6,1,4,1,8708,2,70,2,2))
_IfXcFlexInterfaceConfigTable_Object=MibTable
ifXcFlexInterfaceConfigTable=_IfXcFlexInterfaceConfigTable_Object((1,3,6,1,4,1,8708,2,70,2,2,1))
if mibBuilder.loadTexts:ifXcFlexInterfaceConfigTable.setStatus(_A)
_IfXcFlexInterfaceConfigEntry_Object=MibTableRow
ifXcFlexInterfaceConfigEntry=_IfXcFlexInterfaceConfigEntry_Object((1,3,6,1,4,1,8708,2,70,2,2,1,1))
ifXcFlexInterfaceConfigEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:ifXcFlexInterfaceConfigEntry.setStatus(_A)
_IfXcFlexInterfaceConfigIndex_Type=Unsigned32
_IfXcFlexInterfaceConfigIndex_Object=MibTableColumn
ifXcFlexInterfaceConfigIndex=_IfXcFlexInterfaceConfigIndex_Object((1,3,6,1,4,1,8708,2,70,2,2,1,1,1),_IfXcFlexInterfaceConfigIndex_Type())
ifXcFlexInterfaceConfigIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcFlexInterfaceConfigIndex.setStatus(_A)
_IfXcFlexInterfaceConfigName_Type=MgmtNameString
_IfXcFlexInterfaceConfigName_Object=MibTableColumn
ifXcFlexInterfaceConfigName=_IfXcFlexInterfaceConfigName_Object((1,3,6,1,4,1,8708,2,70,2,2,1,1,2),_IfXcFlexInterfaceConfigName_Type())
ifXcFlexInterfaceConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcFlexInterfaceConfigName.setStatus(_A)
_IfXcFlexInterfaceConfigUId_Type=Unsigned32
_IfXcFlexInterfaceConfigUId_Object=MibTableColumn
ifXcFlexInterfaceConfigUId=_IfXcFlexInterfaceConfigUId_Object((1,3,6,1,4,1,8708,2,70,2,2,1,1,3),_IfXcFlexInterfaceConfigUId_Type())
ifXcFlexInterfaceConfigUId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcFlexInterfaceConfigUId.setStatus(_A)
_IfXcFlexInterfaceConfigProcFuncIndex_Type=Unsigned32WithNA
_IfXcFlexInterfaceConfigProcFuncIndex_Object=MibTableColumn
ifXcFlexInterfaceConfigProcFuncIndex=_IfXcFlexInterfaceConfigProcFuncIndex_Object((1,3,6,1,4,1,8708,2,70,2,2,1,1,4),_IfXcFlexInterfaceConfigProcFuncIndex_Type())
ifXcFlexInterfaceConfigProcFuncIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcFlexInterfaceConfigProcFuncIndex.setStatus(_A)
class _IfXcFlexInterfaceConfigInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unused',1),('client',2),('line',3),('secondaryLine',4)))
_IfXcFlexInterfaceConfigInterfaceType_Type.__name__=_D
_IfXcFlexInterfaceConfigInterfaceType_Object=MibTableColumn
ifXcFlexInterfaceConfigInterfaceType=_IfXcFlexInterfaceConfigInterfaceType_Object((1,3,6,1,4,1,8708,2,70,2,2,1,1,5),_IfXcFlexInterfaceConfigInterfaceType_Type())
ifXcFlexInterfaceConfigInterfaceType.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcFlexInterfaceConfigInterfaceType.setStatus(_A)
_IfXcFlexProcFuncMapList_ObjectIdentity=ObjectIdentity
ifXcFlexProcFuncMapList=_IfXcFlexProcFuncMapList_ObjectIdentity((1,3,6,1,4,1,8708,2,70,2,3))
_IfXcFlexProcFuncMapTable_Object=MibTable
ifXcFlexProcFuncMapTable=_IfXcFlexProcFuncMapTable_Object((1,3,6,1,4,1,8708,2,70,2,3,1))
if mibBuilder.loadTexts:ifXcFlexProcFuncMapTable.setStatus(_A)
_IfXcFlexProcFuncMapEntry_Object=MibTableRow
ifXcFlexProcFuncMapEntry=_IfXcFlexProcFuncMapEntry_Object((1,3,6,1,4,1,8708,2,70,2,3,1,1))
ifXcFlexProcFuncMapEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:ifXcFlexProcFuncMapEntry.setStatus(_A)
_IfXcFlexProcFuncMapIndex_Type=Unsigned32
_IfXcFlexProcFuncMapIndex_Object=MibTableColumn
ifXcFlexProcFuncMapIndex=_IfXcFlexProcFuncMapIndex_Object((1,3,6,1,4,1,8708,2,70,2,3,1,1,1),_IfXcFlexProcFuncMapIndex_Type())
ifXcFlexProcFuncMapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcFlexProcFuncMapIndex.setStatus(_A)
_IfXcFlexProcFuncMapName_Type=MgmtNameString
_IfXcFlexProcFuncMapName_Object=MibTableColumn
ifXcFlexProcFuncMapName=_IfXcFlexProcFuncMapName_Object((1,3,6,1,4,1,8708,2,70,2,3,1,1,2),_IfXcFlexProcFuncMapName_Type())
ifXcFlexProcFuncMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcFlexProcFuncMapName.setStatus(_A)
class _IfXcFlexProcFuncMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('transponder',1),('muxponder',2)))
_IfXcFlexProcFuncMapType_Type.__name__=_D
_IfXcFlexProcFuncMapType_Object=MibTableColumn
ifXcFlexProcFuncMapType=_IfXcFlexProcFuncMapType_Object((1,3,6,1,4,1,8708,2,70,2,3,1,1,3),_IfXcFlexProcFuncMapType_Type())
ifXcFlexProcFuncMapType.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcFlexProcFuncMapType.setStatus(_A)
_IfXcFlexProcFuncMapUId_Type=Unsigned32
_IfXcFlexProcFuncMapUId_Object=MibTableColumn
ifXcFlexProcFuncMapUId=_IfXcFlexProcFuncMapUId_Object((1,3,6,1,4,1,8708,2,70,2,3,1,1,4),_IfXcFlexProcFuncMapUId_Type())
ifXcFlexProcFuncMapUId.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcFlexProcFuncMapUId.setStatus(_A)
_IfXcFlexProcFuncMapProcFuncIndex_Type=Unsigned32WithNA
_IfXcFlexProcFuncMapProcFuncIndex_Object=MibTableColumn
ifXcFlexProcFuncMapProcFuncIndex=_IfXcFlexProcFuncMapProcFuncIndex_Object((1,3,6,1,4,1,8708,2,70,2,3,1,1,5),_IfXcFlexProcFuncMapProcFuncIndex_Type())
ifXcFlexProcFuncMapProcFuncIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcFlexProcFuncMapProcFuncIndex.setStatus(_A)
ifXcFlexGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,70,1,1,1))
ifXcFlexGeneralGroupV1.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ifXcFlexGeneralGroupV1.setStatus(_A)
ifXcFlexInterfaceConfigGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,70,1,1,2))
ifXcFlexInterfaceConfigGroupV1.setObjects(*((_B,_E),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ifXcFlexInterfaceConfigGroupV1.setStatus(_A)
ifXcFlexProcFuncMapGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,70,1,1,3))
ifXcFlexProcFuncMapGroupV1.setObjects(*((_B,_F),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:ifXcFlexProcFuncMapGroupV1.setStatus(_A)
lumIfXcFlexComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,70,1,2,1))
lumIfXcFlexComplV1.setObjects(*((_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:lumIfXcFlexComplV1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lumIfXcFlexMIBModule':lumIfXcFlexMIBModule,'lumIfXcFlexConfs':lumIfXcFlexConfs,'lumIfXcFlexGroups':lumIfXcFlexGroups,_W:ifXcFlexGeneralGroupV1,_X:ifXcFlexInterfaceConfigGroupV1,_Y:ifXcFlexProcFuncMapGroupV1,'lumIfXcFlexCompl':lumIfXcFlexCompl,'lumIfXcFlexComplV1':lumIfXcFlexComplV1,'lumIfXcFlexMIBObjects':lumIfXcFlexMIBObjects,'ifXcFlexGeneral':ifXcFlexGeneral,_G:ifXcFlexGeneralConfigLastChangeTime,_H:ifXcFlexGeneralStateLastChangeTime,_I:ifXcFlexInterfaceConfigTableSize,_J:ifXcFlexInterfaceConfigConfigLastChangeTime,_K:ifXcFlexInterfaceConfigStateLastChangeTime,_L:ifXcFlexProcFuncMapTableSize,_M:ifXcFlexProcFuncMapConfigLastChangeTime,_N:ifXcFlexProcFuncMapStateLastChangeTime,'ifXcFlexInterfaceConfigList':ifXcFlexInterfaceConfigList,'ifXcFlexInterfaceConfigTable':ifXcFlexInterfaceConfigTable,'ifXcFlexInterfaceConfigEntry':ifXcFlexInterfaceConfigEntry,_E:ifXcFlexInterfaceConfigIndex,_O:ifXcFlexInterfaceConfigName,_P:ifXcFlexInterfaceConfigUId,_Q:ifXcFlexInterfaceConfigProcFuncIndex,_R:ifXcFlexInterfaceConfigInterfaceType,'ifXcFlexProcFuncMapList':ifXcFlexProcFuncMapList,'ifXcFlexProcFuncMapTable':ifXcFlexProcFuncMapTable,'ifXcFlexProcFuncMapEntry':ifXcFlexProcFuncMapEntry,_F:ifXcFlexProcFuncMapIndex,_S:ifXcFlexProcFuncMapName,_T:ifXcFlexProcFuncMapType,_U:ifXcFlexProcFuncMapUId,_V:ifXcFlexProcFuncMapProcFuncIndex})