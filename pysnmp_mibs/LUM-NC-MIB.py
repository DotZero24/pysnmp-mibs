_O='ncStatusGroupV2'
_N='ncStatusGroup'
_M='ncStatusDown'
_L='ncStatusDegraded'
_K='ncGeneralStatusTableSize'
_J='ncGeneralStateLastChangeTime'
_I='ncGeneralConfigLastChangeTime'
_H='Unsigned32'
_G='ncGeneralGroup'
_F='ncStatusIncomplete'
_E='deprecated'
_D='ncStatusIndex'
_C='read-only'
_B='current'
_A='LUM-NC-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumModules,lumNcMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumNcMIB')
FaultStatus,=mibBuilder.importSymbols('LUM-TC','FaultStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
lumNcMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,39))
if mibBuilder.loadTexts:lumNcMIBModule.setRevisions(('2017-06-15 00:00','2011-04-13 00:00'))
_LumNcConfs_ObjectIdentity=ObjectIdentity
lumNcConfs=_LumNcConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,39,1))
_LumNcGroups_ObjectIdentity=ObjectIdentity
lumNcGroups=_LumNcGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,39,1,1))
_LumNcCompl_ObjectIdentity=ObjectIdentity
lumNcCompl=_LumNcCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,39,1,2))
_LumNcMIBObjects_ObjectIdentity=ObjectIdentity
lumNcMIBObjects=_LumNcMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,39,2))
_NcGeneral_ObjectIdentity=ObjectIdentity
ncGeneral=_NcGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,39,2,1))
_NcGeneralConfigLastChangeTime_Type=DateAndTime
_NcGeneralConfigLastChangeTime_Object=MibScalar
ncGeneralConfigLastChangeTime=_NcGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,39,2,1,1),_NcGeneralConfigLastChangeTime_Type())
ncGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ncGeneralConfigLastChangeTime.setStatus(_B)
_NcGeneralStateLastChangeTime_Type=DateAndTime
_NcGeneralStateLastChangeTime_Object=MibScalar
ncGeneralStateLastChangeTime=_NcGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,39,2,1,2),_NcGeneralStateLastChangeTime_Type())
ncGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ncGeneralStateLastChangeTime.setStatus(_B)
_NcGeneralStatusTableSize_Type=Unsigned32
_NcGeneralStatusTableSize_Object=MibScalar
ncGeneralStatusTableSize=_NcGeneralStatusTableSize_Object((1,3,6,1,4,1,8708,2,39,2,1,3),_NcGeneralStatusTableSize_Type())
ncGeneralStatusTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ncGeneralStatusTableSize.setStatus(_B)
_NcStatusList_ObjectIdentity=ObjectIdentity
ncStatusList=_NcStatusList_ObjectIdentity((1,3,6,1,4,1,8708,2,39,2,2))
_NcStatusTable_Object=MibTable
ncStatusTable=_NcStatusTable_Object((1,3,6,1,4,1,8708,2,39,2,2,1))
if mibBuilder.loadTexts:ncStatusTable.setStatus(_B)
_NcStatusEntry_Object=MibTableRow
ncStatusEntry=_NcStatusEntry_Object((1,3,6,1,4,1,8708,2,39,2,2,1,1))
ncStatusEntry.setIndexNames((0,_A,_D))
if mibBuilder.loadTexts:ncStatusEntry.setStatus(_B)
class _NcStatusIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NcStatusIndex_Type.__name__=_H
_NcStatusIndex_Object=MibTableColumn
ncStatusIndex=_NcStatusIndex_Object((1,3,6,1,4,1,8708,2,39,2,2,1,1,1),_NcStatusIndex_Type())
ncStatusIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ncStatusIndex.setStatus(_B)
_NcStatusIncomplete_Type=FaultStatus
_NcStatusIncomplete_Object=MibTableColumn
ncStatusIncomplete=_NcStatusIncomplete_Object((1,3,6,1,4,1,8708,2,39,2,2,1,1,2),_NcStatusIncomplete_Type())
ncStatusIncomplete.setMaxAccess(_C)
if mibBuilder.loadTexts:ncStatusIncomplete.setStatus(_B)
_NcStatusDegraded_Type=FaultStatus
_NcStatusDegraded_Object=MibTableColumn
ncStatusDegraded=_NcStatusDegraded_Object((1,3,6,1,4,1,8708,2,39,2,2,1,1,3),_NcStatusDegraded_Type())
ncStatusDegraded.setMaxAccess(_C)
if mibBuilder.loadTexts:ncStatusDegraded.setStatus(_E)
_NcStatusDown_Type=FaultStatus
_NcStatusDown_Object=MibTableColumn
ncStatusDown=_NcStatusDown_Object((1,3,6,1,4,1,8708,2,39,2,2,1,1,4),_NcStatusDown_Type())
ncStatusDown.setMaxAccess(_C)
if mibBuilder.loadTexts:ncStatusDown.setStatus(_E)
ncGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,39,1,1,1))
ncGeneralGroup.setObjects(*((_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:ncGeneralGroup.setStatus(_B)
ncStatusGroup=ObjectGroup((1,3,6,1,4,1,8708,2,39,1,1,2))
ncStatusGroup.setObjects(*((_A,_D),(_A,_L),(_A,_M),(_A,_F)))
if mibBuilder.loadTexts:ncStatusGroup.setStatus(_E)
ncStatusGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,39,1,1,3))
ncStatusGroupV2.setObjects(*((_A,_D),(_A,_F)))
if mibBuilder.loadTexts:ncStatusGroupV2.setStatus(_B)
lumNcBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,39,1,2,1))
lumNcBasicComplV1.setObjects(*((_A,_G),(_A,_N)))
if mibBuilder.loadTexts:lumNcBasicComplV1.setStatus(_E)
lumNcBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,39,1,2,2))
lumNcBasicComplV2.setObjects(*((_A,_G),(_A,_O)))
if mibBuilder.loadTexts:lumNcBasicComplV2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumNcMIBModule':lumNcMIBModule,'lumNcConfs':lumNcConfs,'lumNcGroups':lumNcGroups,_G:ncGeneralGroup,_N:ncStatusGroup,_O:ncStatusGroupV2,'lumNcCompl':lumNcCompl,'lumNcBasicComplV1':lumNcBasicComplV1,'lumNcBasicComplV2':lumNcBasicComplV2,'lumNcMIBObjects':lumNcMIBObjects,'ncGeneral':ncGeneral,_I:ncGeneralConfigLastChangeTime,_J:ncGeneralStateLastChangeTime,_K:ncGeneralStatusTableSize,'ncStatusList':ncStatusList,'ncStatusTable':ncStatusTable,'ncStatusEntry':ncStatusEntry,_D:ncStatusIndex,_F:ncStatusIncomplete,_L:ncStatusDegraded,_M:ncStatusDown})