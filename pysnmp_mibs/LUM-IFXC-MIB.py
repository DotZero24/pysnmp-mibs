_Y='ifXcDynamicXcOduGroupV3'
_X='ifXcDynamicXcOduGroupV2'
_W='ifXcDynamicXcOduGroupV1'
_V='ifXcStaticXcOduToIndex'
_U='ifXcStaticXcOduFromIndex'
_T='ifXcStaticXcOduName'
_S='ifXcGeneralIfXcDynamicXcOduStateLastChangeTime'
_R='ifXcGeneralIfXcDynamicXcOduConfigLastChangeTime'
_Q='ifXcGeneralIfXcDynamicXcOduTableSize'
_P='ifXcGeneralIfXcStaticXcOduStateLastChangeTime'
_O='ifXcGeneralIfXcStaticXcOduConfigLastChangeTime'
_N='ifXcGeneralIfXcStaticXcOduTableSize'
_M='ifXcGeneralStateLastChangeTime'
_L='ifXcGeneralConfigLastChangeTime'
_K='ifXcStaticXcOduIndex'
_J='ifXcStaticXcOduGroupV1'
_I='ifXcGeneralGroupV1'
_H='deprecated'
_G='ifXcDynamicXcOduToIndex'
_F='ifXcDynamicXcOduFromIndex'
_E='ifXcDynamicXcOduName'
_D='ifXcDynamicXcOduIndex'
_C='read-only'
_B='current'
_A='LUM-IFXC-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumIfXcMIB,lumModules=mibBuilder.importSymbols('LUM-REG','lumIfXcMIB','lumModules')
CommandString,MgmtNameString,Unsigned32WithNA=mibBuilder.importSymbols('LUM-TC','CommandString','MgmtNameString','Unsigned32WithNA')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
lumIfXcMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,51))
if mibBuilder.loadTexts:lumIfXcMIBModule.setRevisions(('2017-06-15 00:00','2013-11-15 00:00','2012-11-20 00:00'))
_LumIfXcConfs_ObjectIdentity=ObjectIdentity
lumIfXcConfs=_LumIfXcConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,51,1))
_LumIfXcGroups_ObjectIdentity=ObjectIdentity
lumIfXcGroups=_LumIfXcGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,51,1,1))
_LumIfXcCompl_ObjectIdentity=ObjectIdentity
lumIfXcCompl=_LumIfXcCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,51,1,2))
_LumIfXcMIBObjects_ObjectIdentity=ObjectIdentity
lumIfXcMIBObjects=_LumIfXcMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,51,2))
_IfXcGeneral_ObjectIdentity=ObjectIdentity
ifXcGeneral=_IfXcGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,51,2,1))
_IfXcGeneralConfigLastChangeTime_Type=DateAndTime
_IfXcGeneralConfigLastChangeTime_Object=MibScalar
ifXcGeneralConfigLastChangeTime=_IfXcGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,51,2,1,1),_IfXcGeneralConfigLastChangeTime_Type())
ifXcGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcGeneralConfigLastChangeTime.setStatus(_B)
_IfXcGeneralStateLastChangeTime_Type=DateAndTime
_IfXcGeneralStateLastChangeTime_Object=MibScalar
ifXcGeneralStateLastChangeTime=_IfXcGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,51,2,1,2),_IfXcGeneralStateLastChangeTime_Type())
ifXcGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcGeneralStateLastChangeTime.setStatus(_B)
_IfXcGeneralIfXcStaticXcOduTableSize_Type=Unsigned32
_IfXcGeneralIfXcStaticXcOduTableSize_Object=MibScalar
ifXcGeneralIfXcStaticXcOduTableSize=_IfXcGeneralIfXcStaticXcOduTableSize_Object((1,3,6,1,4,1,8708,2,51,2,1,3),_IfXcGeneralIfXcStaticXcOduTableSize_Type())
ifXcGeneralIfXcStaticXcOduTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcGeneralIfXcStaticXcOduTableSize.setStatus(_B)
_IfXcGeneralIfXcStaticXcOduConfigLastChangeTime_Type=DateAndTime
_IfXcGeneralIfXcStaticXcOduConfigLastChangeTime_Object=MibScalar
ifXcGeneralIfXcStaticXcOduConfigLastChangeTime=_IfXcGeneralIfXcStaticXcOduConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,51,2,1,4),_IfXcGeneralIfXcStaticXcOduConfigLastChangeTime_Type())
ifXcGeneralIfXcStaticXcOduConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcGeneralIfXcStaticXcOduConfigLastChangeTime.setStatus(_B)
_IfXcGeneralIfXcStaticXcOduStateLastChangeTime_Type=DateAndTime
_IfXcGeneralIfXcStaticXcOduStateLastChangeTime_Object=MibScalar
ifXcGeneralIfXcStaticXcOduStateLastChangeTime=_IfXcGeneralIfXcStaticXcOduStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,51,2,1,5),_IfXcGeneralIfXcStaticXcOduStateLastChangeTime_Type())
ifXcGeneralIfXcStaticXcOduStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcGeneralIfXcStaticXcOduStateLastChangeTime.setStatus(_B)
_IfXcGeneralIfXcDynamicXcOduTableSize_Type=Unsigned32
_IfXcGeneralIfXcDynamicXcOduTableSize_Object=MibScalar
ifXcGeneralIfXcDynamicXcOduTableSize=_IfXcGeneralIfXcDynamicXcOduTableSize_Object((1,3,6,1,4,1,8708,2,51,2,1,6),_IfXcGeneralIfXcDynamicXcOduTableSize_Type())
ifXcGeneralIfXcDynamicXcOduTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcGeneralIfXcDynamicXcOduTableSize.setStatus(_B)
_IfXcGeneralIfXcDynamicXcOduConfigLastChangeTime_Type=DateAndTime
_IfXcGeneralIfXcDynamicXcOduConfigLastChangeTime_Object=MibScalar
ifXcGeneralIfXcDynamicXcOduConfigLastChangeTime=_IfXcGeneralIfXcDynamicXcOduConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,51,2,1,7),_IfXcGeneralIfXcDynamicXcOduConfigLastChangeTime_Type())
ifXcGeneralIfXcDynamicXcOduConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcGeneralIfXcDynamicXcOduConfigLastChangeTime.setStatus(_B)
_IfXcGeneralIfXcDynamicXcOduStateLastChangeTime_Type=DateAndTime
_IfXcGeneralIfXcDynamicXcOduStateLastChangeTime_Object=MibScalar
ifXcGeneralIfXcDynamicXcOduStateLastChangeTime=_IfXcGeneralIfXcDynamicXcOduStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,51,2,1,8),_IfXcGeneralIfXcDynamicXcOduStateLastChangeTime_Type())
ifXcGeneralIfXcDynamicXcOduStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcGeneralIfXcDynamicXcOduStateLastChangeTime.setStatus(_B)
_IfXcStaticXcOduList_ObjectIdentity=ObjectIdentity
ifXcStaticXcOduList=_IfXcStaticXcOduList_ObjectIdentity((1,3,6,1,4,1,8708,2,51,2,2))
_IfXcStaticXcOduTable_Object=MibTable
ifXcStaticXcOduTable=_IfXcStaticXcOduTable_Object((1,3,6,1,4,1,8708,2,51,2,2,1))
if mibBuilder.loadTexts:ifXcStaticXcOduTable.setStatus(_B)
_IfXcStaticXcOduEntry_Object=MibTableRow
ifXcStaticXcOduEntry=_IfXcStaticXcOduEntry_Object((1,3,6,1,4,1,8708,2,51,2,2,1,1))
ifXcStaticXcOduEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:ifXcStaticXcOduEntry.setStatus(_B)
_IfXcStaticXcOduIndex_Type=Unsigned32
_IfXcStaticXcOduIndex_Object=MibTableColumn
ifXcStaticXcOduIndex=_IfXcStaticXcOduIndex_Object((1,3,6,1,4,1,8708,2,51,2,2,1,1,1),_IfXcStaticXcOduIndex_Type())
ifXcStaticXcOduIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcStaticXcOduIndex.setStatus(_B)
_IfXcStaticXcOduName_Type=MgmtNameString
_IfXcStaticXcOduName_Object=MibTableColumn
ifXcStaticXcOduName=_IfXcStaticXcOduName_Object((1,3,6,1,4,1,8708,2,51,2,2,1,1,2),_IfXcStaticXcOduName_Type())
ifXcStaticXcOduName.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcStaticXcOduName.setStatus(_B)
_IfXcStaticXcOduFromIndex_Type=Unsigned32WithNA
_IfXcStaticXcOduFromIndex_Object=MibTableColumn
ifXcStaticXcOduFromIndex=_IfXcStaticXcOduFromIndex_Object((1,3,6,1,4,1,8708,2,51,2,2,1,1,3),_IfXcStaticXcOduFromIndex_Type())
ifXcStaticXcOduFromIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcStaticXcOduFromIndex.setStatus(_B)
_IfXcStaticXcOduToIndex_Type=Unsigned32WithNA
_IfXcStaticXcOduToIndex_Object=MibTableColumn
ifXcStaticXcOduToIndex=_IfXcStaticXcOduToIndex_Object((1,3,6,1,4,1,8708,2,51,2,2,1,1,4),_IfXcStaticXcOduToIndex_Type())
ifXcStaticXcOduToIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcStaticXcOduToIndex.setStatus(_B)
_IfXcDynamicXcOduList_ObjectIdentity=ObjectIdentity
ifXcDynamicXcOduList=_IfXcDynamicXcOduList_ObjectIdentity((1,3,6,1,4,1,8708,2,51,2,3))
_IfXcDynamicXcOduTable_Object=MibTable
ifXcDynamicXcOduTable=_IfXcDynamicXcOduTable_Object((1,3,6,1,4,1,8708,2,51,2,3,1))
if mibBuilder.loadTexts:ifXcDynamicXcOduTable.setStatus(_B)
_IfXcDynamicXcOduEntry_Object=MibTableRow
ifXcDynamicXcOduEntry=_IfXcDynamicXcOduEntry_Object((1,3,6,1,4,1,8708,2,51,2,3,1,1))
ifXcDynamicXcOduEntry.setIndexNames((0,_A,_D))
if mibBuilder.loadTexts:ifXcDynamicXcOduEntry.setStatus(_B)
_IfXcDynamicXcOduIndex_Type=Unsigned32
_IfXcDynamicXcOduIndex_Object=MibTableColumn
ifXcDynamicXcOduIndex=_IfXcDynamicXcOduIndex_Object((1,3,6,1,4,1,8708,2,51,2,3,1,1,1),_IfXcDynamicXcOduIndex_Type())
ifXcDynamicXcOduIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcDynamicXcOduIndex.setStatus(_B)
_IfXcDynamicXcOduName_Type=MgmtNameString
_IfXcDynamicXcOduName_Object=MibTableColumn
ifXcDynamicXcOduName=_IfXcDynamicXcOduName_Object((1,3,6,1,4,1,8708,2,51,2,3,1,1,2),_IfXcDynamicXcOduName_Type())
ifXcDynamicXcOduName.setMaxAccess('read-create')
if mibBuilder.loadTexts:ifXcDynamicXcOduName.setStatus(_B)
_IfXcDynamicXcOduFromIndex_Type=Unsigned32WithNA
_IfXcDynamicXcOduFromIndex_Object=MibTableColumn
ifXcDynamicXcOduFromIndex=_IfXcDynamicXcOduFromIndex_Object((1,3,6,1,4,1,8708,2,51,2,3,1,1,3),_IfXcDynamicXcOduFromIndex_Type())
ifXcDynamicXcOduFromIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ifXcDynamicXcOduFromIndex.setStatus(_B)
_IfXcDynamicXcOduToIndex_Type=Unsigned32WithNA
_IfXcDynamicXcOduToIndex_Object=MibTableColumn
ifXcDynamicXcOduToIndex=_IfXcDynamicXcOduToIndex_Object((1,3,6,1,4,1,8708,2,51,2,3,1,1,4),_IfXcDynamicXcOduToIndex_Type())
ifXcDynamicXcOduToIndex.setMaxAccess('read-write')
if mibBuilder.loadTexts:ifXcDynamicXcOduToIndex.setStatus(_B)
ifXcGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,51,1,1,1))
ifXcGeneralGroupV1.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:ifXcGeneralGroupV1.setStatus(_B)
ifXcStaticXcOduGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,51,1,1,2))
ifXcStaticXcOduGroupV1.setObjects(*((_A,_K),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:ifXcStaticXcOduGroupV1.setStatus(_B)
ifXcDynamicXcOduGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,51,1,1,3))
ifXcDynamicXcOduGroupV1.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:ifXcDynamicXcOduGroupV1.setStatus(_H)
ifXcDynamicXcOduGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,51,1,1,4))
ifXcDynamicXcOduGroupV2.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:ifXcDynamicXcOduGroupV2.setStatus(_H)
ifXcDynamicXcOduGroupV3=ObjectGroup((1,3,6,1,4,1,8708,2,51,1,1,5))
ifXcDynamicXcOduGroupV3.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:ifXcDynamicXcOduGroupV3.setStatus(_B)
lumIfXcComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,51,1,2,1))
lumIfXcComplV1.setObjects(*((_A,_I),(_A,_J),(_A,_W)))
if mibBuilder.loadTexts:lumIfXcComplV1.setStatus(_H)
lumIfXcComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,51,1,2,2))
lumIfXcComplV2.setObjects(*((_A,_I),(_A,_J),(_A,_X)))
if mibBuilder.loadTexts:lumIfXcComplV2.setStatus(_H)
lumIfXcComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,51,1,2,3))
lumIfXcComplV3.setObjects(*((_A,_I),(_A,_J),(_A,_Y)))
if mibBuilder.loadTexts:lumIfXcComplV3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumIfXcMIBModule':lumIfXcMIBModule,'lumIfXcConfs':lumIfXcConfs,'lumIfXcGroups':lumIfXcGroups,_I:ifXcGeneralGroupV1,_J:ifXcStaticXcOduGroupV1,_W:ifXcDynamicXcOduGroupV1,_X:ifXcDynamicXcOduGroupV2,_Y:ifXcDynamicXcOduGroupV3,'lumIfXcCompl':lumIfXcCompl,'lumIfXcComplV1':lumIfXcComplV1,'lumIfXcComplV2':lumIfXcComplV2,'lumIfXcComplV3':lumIfXcComplV3,'lumIfXcMIBObjects':lumIfXcMIBObjects,'ifXcGeneral':ifXcGeneral,_L:ifXcGeneralConfigLastChangeTime,_M:ifXcGeneralStateLastChangeTime,_N:ifXcGeneralIfXcStaticXcOduTableSize,_O:ifXcGeneralIfXcStaticXcOduConfigLastChangeTime,_P:ifXcGeneralIfXcStaticXcOduStateLastChangeTime,_Q:ifXcGeneralIfXcDynamicXcOduTableSize,_R:ifXcGeneralIfXcDynamicXcOduConfigLastChangeTime,_S:ifXcGeneralIfXcDynamicXcOduStateLastChangeTime,'ifXcStaticXcOduList':ifXcStaticXcOduList,'ifXcStaticXcOduTable':ifXcStaticXcOduTable,'ifXcStaticXcOduEntry':ifXcStaticXcOduEntry,_K:ifXcStaticXcOduIndex,_T:ifXcStaticXcOduName,_U:ifXcStaticXcOduFromIndex,_V:ifXcStaticXcOduToIndex,'ifXcDynamicXcOduList':ifXcDynamicXcOduList,'ifXcDynamicXcOduTable':ifXcDynamicXcOduTable,'ifXcDynamicXcOduEntry':ifXcDynamicXcOduEntry,_D:ifXcDynamicXcOduIndex,_E:ifXcDynamicXcOduName,_F:ifXcDynamicXcOduFromIndex,_G:ifXcDynamicXcOduToIndex})