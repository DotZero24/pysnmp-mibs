_K='pmServerStatusGroup'
_J='pmServerGeneralGroup'
_I='pmServerStatusFaultyEduReportFilesExist'
_H='pmServerGeneralStatusTableSize'
_G='pmServerGeneralStateLastChangeTime'
_F='pmServerGeneralConfigLastChangeTime'
_E='Unsigned32'
_D='pmServerStatusIndex'
_C='read-only'
_B='LUM-PMSERVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lumModules,lumPmServerMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumPmServerMIB')
FaultStatus,=mibBuilder.importSymbols('LUM-TC','FaultStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
lumPmServerMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,49))
if mibBuilder.loadTexts:lumPmServerMIBModule.setRevisions(('2017-06-15 00:00','2012-07-18 00:00'))
_LumPmServerConfs_ObjectIdentity=ObjectIdentity
lumPmServerConfs=_LumPmServerConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,49,1))
_LumPmServerGroups_ObjectIdentity=ObjectIdentity
lumPmServerGroups=_LumPmServerGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,49,1,1))
_LumPmServerCompl_ObjectIdentity=ObjectIdentity
lumPmServerCompl=_LumPmServerCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,49,1,2))
_LumPmServerMIBObjects_ObjectIdentity=ObjectIdentity
lumPmServerMIBObjects=_LumPmServerMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,49,2))
_PmServerGeneral_ObjectIdentity=ObjectIdentity
pmServerGeneral=_PmServerGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,49,2,1))
_PmServerGeneralConfigLastChangeTime_Type=DateAndTime
_PmServerGeneralConfigLastChangeTime_Object=MibScalar
pmServerGeneralConfigLastChangeTime=_PmServerGeneralConfigLastChangeTime_Object((1,3,6,1,4,1,8708,2,49,2,1,1),_PmServerGeneralConfigLastChangeTime_Type())
pmServerGeneralConfigLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pmServerGeneralConfigLastChangeTime.setStatus(_A)
_PmServerGeneralStateLastChangeTime_Type=DateAndTime
_PmServerGeneralStateLastChangeTime_Object=MibScalar
pmServerGeneralStateLastChangeTime=_PmServerGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,49,2,1,2),_PmServerGeneralStateLastChangeTime_Type())
pmServerGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:pmServerGeneralStateLastChangeTime.setStatus(_A)
_PmServerGeneralStatusTableSize_Type=Unsigned32
_PmServerGeneralStatusTableSize_Object=MibScalar
pmServerGeneralStatusTableSize=_PmServerGeneralStatusTableSize_Object((1,3,6,1,4,1,8708,2,49,2,1,3),_PmServerGeneralStatusTableSize_Type())
pmServerGeneralStatusTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:pmServerGeneralStatusTableSize.setStatus(_A)
_PmServerStatusList_ObjectIdentity=ObjectIdentity
pmServerStatusList=_PmServerStatusList_ObjectIdentity((1,3,6,1,4,1,8708,2,49,2,2))
_PmServerStatusTable_Object=MibTable
pmServerStatusTable=_PmServerStatusTable_Object((1,3,6,1,4,1,8708,2,49,2,2,1))
if mibBuilder.loadTexts:pmServerStatusTable.setStatus(_A)
_PmServerStatusEntry_Object=MibTableRow
pmServerStatusEntry=_PmServerStatusEntry_Object((1,3,6,1,4,1,8708,2,49,2,2,1,1))
pmServerStatusEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:pmServerStatusEntry.setStatus(_A)
class _PmServerStatusIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PmServerStatusIndex_Type.__name__=_E
_PmServerStatusIndex_Object=MibTableColumn
pmServerStatusIndex=_PmServerStatusIndex_Object((1,3,6,1,4,1,8708,2,49,2,2,1,1,1),_PmServerStatusIndex_Type())
pmServerStatusIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pmServerStatusIndex.setStatus(_A)
_PmServerStatusFaultyEduReportFilesExist_Type=FaultStatus
_PmServerStatusFaultyEduReportFilesExist_Object=MibTableColumn
pmServerStatusFaultyEduReportFilesExist=_PmServerStatusFaultyEduReportFilesExist_Object((1,3,6,1,4,1,8708,2,49,2,2,1,1,2),_PmServerStatusFaultyEduReportFilesExist_Type())
pmServerStatusFaultyEduReportFilesExist.setMaxAccess(_C)
if mibBuilder.loadTexts:pmServerStatusFaultyEduReportFilesExist.setStatus(_A)
pmServerGeneralGroup=ObjectGroup((1,3,6,1,4,1,8708,2,49,1,1,1))
pmServerGeneralGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:pmServerGeneralGroup.setStatus(_A)
pmServerStatusGroup=ObjectGroup((1,3,6,1,4,1,8708,2,49,1,1,2))
pmServerStatusGroup.setObjects(*((_B,_D),(_B,_I)))
if mibBuilder.loadTexts:pmServerStatusGroup.setStatus(_A)
lumPmServerBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,49,1,2,1))
lumPmServerBasicComplV1.setObjects(*((_B,_J),(_B,_K)))
if mibBuilder.loadTexts:lumPmServerBasicComplV1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lumPmServerMIBModule':lumPmServerMIBModule,'lumPmServerConfs':lumPmServerConfs,'lumPmServerGroups':lumPmServerGroups,_J:pmServerGeneralGroup,_K:pmServerStatusGroup,'lumPmServerCompl':lumPmServerCompl,'lumPmServerBasicComplV1':lumPmServerBasicComplV1,'lumPmServerMIBObjects':lumPmServerMIBObjects,'pmServerGeneral':pmServerGeneral,_F:pmServerGeneralConfigLastChangeTime,_G:pmServerGeneralStateLastChangeTime,_H:pmServerGeneralStatusTableSize,'pmServerStatusList':pmServerStatusList,'pmServerStatusTable':pmServerStatusTable,'pmServerStatusEntry':pmServerStatusEntry,_D:pmServerStatusIndex,_I:pmServerStatusFaultyEduReportFilesExist})