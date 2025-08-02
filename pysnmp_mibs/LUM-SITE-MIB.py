_e='siteExtAlarmOutGroupV1'
_d='siteGeneralGroupV2'
_c='siteExtAlarmGroupV1'
_b='siteGeneralExtAlarmOutTableSize'
_a='siteExtAlarmOutIndex'
_Z='activeLow'
_Y='activeHigh'
_X='AdminStatusWithNA'
_W='siteExtAlarmGroupV2'
_V='siteGeneralGroupV1'
_U='siteExtAlarmOperStatus'
_T='siteExtAlarmId'
_S='siteGeneralExtAlarmTableSize'
_R='siteGeneralStateLastChangeTime'
_Q='siteGeneralLastChangeTime'
_P='AlarmPerceivedSeverity'
_O='siteExtAlarmActive'
_N='siteExtAlarmText'
_M='siteExtAlarmSeverity'
_L='siteExtAlarmLevel'
_K='siteExtAlarmAdminStatus'
_J='siteExtAlarmName'
_I='deprecated'
_H='Integer32'
_G='siteExtAlarmIndex'
_F='DisplayString'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='current'
_A='LUM-SITE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AlarmPerceivedSeverity,=mibBuilder.importSymbols('LUM-ALARM-MIB',_P)
lumModules,lumSiteMIB=mibBuilder.importSymbols('LUM-REG','lumModules','lumSiteMIB')
AdminStatusWithNA,BoardOrInterfaceOperStatus,FaultStatus,OperStatusWithNA=mibBuilder.importSymbols('LUM-TC',_X,'BoardOrInterfaceOperStatus','FaultStatus','OperStatusWithNA')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'PhysAddress','TextualConvention')
lumSiteMIBModule=ModuleIdentity((1,3,6,1,4,1,8708,1,1,42))
if mibBuilder.loadTexts:lumSiteMIBModule.setRevisions(('2017-06-15 00:00','2016-12-01 00:00','2011-12-20 00:00'))
_LumSiteConfs_ObjectIdentity=ObjectIdentity
lumSiteConfs=_LumSiteConfs_ObjectIdentity((1,3,6,1,4,1,8708,2,42,1))
_LumSiteGroups_ObjectIdentity=ObjectIdentity
lumSiteGroups=_LumSiteGroups_ObjectIdentity((1,3,6,1,4,1,8708,2,42,1,1))
_LumSiteCompl_ObjectIdentity=ObjectIdentity
lumSiteCompl=_LumSiteCompl_ObjectIdentity((1,3,6,1,4,1,8708,2,42,1,2))
_LumSiteMIBObjects_ObjectIdentity=ObjectIdentity
lumSiteMIBObjects=_LumSiteMIBObjects_ObjectIdentity((1,3,6,1,4,1,8708,2,42,2))
_SiteGeneral_ObjectIdentity=ObjectIdentity
siteGeneral=_SiteGeneral_ObjectIdentity((1,3,6,1,4,1,8708,2,42,2,1))
_SiteGeneralLastChangeTime_Type=DateAndTime
_SiteGeneralLastChangeTime_Object=MibScalar
siteGeneralLastChangeTime=_SiteGeneralLastChangeTime_Object((1,3,6,1,4,1,8708,2,42,2,1,1),_SiteGeneralLastChangeTime_Type())
siteGeneralLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:siteGeneralLastChangeTime.setStatus(_B)
_SiteGeneralStateLastChangeTime_Type=DateAndTime
_SiteGeneralStateLastChangeTime_Object=MibScalar
siteGeneralStateLastChangeTime=_SiteGeneralStateLastChangeTime_Object((1,3,6,1,4,1,8708,2,42,2,1,2),_SiteGeneralStateLastChangeTime_Type())
siteGeneralStateLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:siteGeneralStateLastChangeTime.setStatus(_B)
_SiteGeneralExtAlarmTableSize_Type=Unsigned32
_SiteGeneralExtAlarmTableSize_Object=MibScalar
siteGeneralExtAlarmTableSize=_SiteGeneralExtAlarmTableSize_Object((1,3,6,1,4,1,8708,2,42,2,1,3),_SiteGeneralExtAlarmTableSize_Type())
siteGeneralExtAlarmTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:siteGeneralExtAlarmTableSize.setStatus(_B)
_SiteGeneralExtAlarmOutTableSize_Type=Unsigned32
_SiteGeneralExtAlarmOutTableSize_Object=MibScalar
siteGeneralExtAlarmOutTableSize=_SiteGeneralExtAlarmOutTableSize_Object((1,3,6,1,4,1,8708,2,42,2,1,4),_SiteGeneralExtAlarmOutTableSize_Type())
siteGeneralExtAlarmOutTableSize.setMaxAccess(_C)
if mibBuilder.loadTexts:siteGeneralExtAlarmOutTableSize.setStatus(_B)
_SiteExtAlarmList_ObjectIdentity=ObjectIdentity
siteExtAlarmList=_SiteExtAlarmList_ObjectIdentity((1,3,6,1,4,1,8708,2,42,2,2))
_SiteExtAlarmTable_Object=MibTable
siteExtAlarmTable=_SiteExtAlarmTable_Object((1,3,6,1,4,1,8708,2,42,2,2,1))
if mibBuilder.loadTexts:siteExtAlarmTable.setStatus(_B)
_SiteExtAlarmEntry_Object=MibTableRow
siteExtAlarmEntry=_SiteExtAlarmEntry_Object((1,3,6,1,4,1,8708,2,42,2,2,1,1))
siteExtAlarmEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:siteExtAlarmEntry.setStatus(_B)
class _SiteExtAlarmIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SiteExtAlarmIndex_Type.__name__=_E
_SiteExtAlarmIndex_Object=MibTableColumn
siteExtAlarmIndex=_SiteExtAlarmIndex_Object((1,3,6,1,4,1,8708,2,42,2,2,1,1,1),_SiteExtAlarmIndex_Type())
siteExtAlarmIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:siteExtAlarmIndex.setStatus(_B)
class _SiteExtAlarmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SiteExtAlarmName_Type.__name__=_F
_SiteExtAlarmName_Object=MibTableColumn
siteExtAlarmName=_SiteExtAlarmName_Object((1,3,6,1,4,1,8708,2,42,2,2,1,1,2),_SiteExtAlarmName_Type())
siteExtAlarmName.setMaxAccess(_C)
if mibBuilder.loadTexts:siteExtAlarmName.setStatus(_B)
class _SiteExtAlarmAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_SiteExtAlarmAdminStatus_Type.__name__=_H
_SiteExtAlarmAdminStatus_Object=MibTableColumn
siteExtAlarmAdminStatus=_SiteExtAlarmAdminStatus_Object((1,3,6,1,4,1,8708,2,42,2,2,1,1,3),_SiteExtAlarmAdminStatus_Type())
siteExtAlarmAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:siteExtAlarmAdminStatus.setStatus(_B)
class _SiteExtAlarmLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_SiteExtAlarmLevel_Type.__name__=_H
_SiteExtAlarmLevel_Object=MibTableColumn
siteExtAlarmLevel=_SiteExtAlarmLevel_Object((1,3,6,1,4,1,8708,2,42,2,2,1,1,4),_SiteExtAlarmLevel_Type())
siteExtAlarmLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:siteExtAlarmLevel.setStatus(_B)
class _SiteExtAlarmSeverity_Type(AlarmPerceivedSeverity):defaultValue=3
_SiteExtAlarmSeverity_Type.__name__=_P
_SiteExtAlarmSeverity_Object=MibTableColumn
siteExtAlarmSeverity=_SiteExtAlarmSeverity_Object((1,3,6,1,4,1,8708,2,42,2,2,1,1,5),_SiteExtAlarmSeverity_Type())
siteExtAlarmSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:siteExtAlarmSeverity.setStatus(_B)
class _SiteExtAlarmText_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SiteExtAlarmText_Type.__name__=_F
_SiteExtAlarmText_Object=MibTableColumn
siteExtAlarmText=_SiteExtAlarmText_Object((1,3,6,1,4,1,8708,2,42,2,2,1,1,6),_SiteExtAlarmText_Type())
siteExtAlarmText.setMaxAccess(_D)
if mibBuilder.loadTexts:siteExtAlarmText.setStatus(_B)
_SiteExtAlarmActive_Type=FaultStatus
_SiteExtAlarmActive_Object=MibTableColumn
siteExtAlarmActive=_SiteExtAlarmActive_Object((1,3,6,1,4,1,8708,2,42,2,2,1,1,7),_SiteExtAlarmActive_Type())
siteExtAlarmActive.setMaxAccess(_C)
if mibBuilder.loadTexts:siteExtAlarmActive.setStatus(_B)
class _SiteExtAlarmId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SiteExtAlarmId_Type.__name__=_E
_SiteExtAlarmId_Object=MibTableColumn
siteExtAlarmId=_SiteExtAlarmId_Object((1,3,6,1,4,1,8708,2,42,2,2,1,1,8),_SiteExtAlarmId_Type())
siteExtAlarmId.setMaxAccess(_C)
if mibBuilder.loadTexts:siteExtAlarmId.setStatus(_B)
_SiteExtAlarmOperStatus_Type=BoardOrInterfaceOperStatus
_SiteExtAlarmOperStatus_Object=MibTableColumn
siteExtAlarmOperStatus=_SiteExtAlarmOperStatus_Object((1,3,6,1,4,1,8708,2,42,2,2,1,1,9),_SiteExtAlarmOperStatus_Type())
siteExtAlarmOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:siteExtAlarmOperStatus.setStatus(_B)
_SiteExtAlarmOutList_ObjectIdentity=ObjectIdentity
siteExtAlarmOutList=_SiteExtAlarmOutList_ObjectIdentity((1,3,6,1,4,1,8708,2,42,2,3))
_SiteExtAlarmOutTable_Object=MibTable
siteExtAlarmOutTable=_SiteExtAlarmOutTable_Object((1,3,6,1,4,1,8708,2,42,2,3,1))
if mibBuilder.loadTexts:siteExtAlarmOutTable.setStatus(_B)
_SiteExtAlarmOutEntry_Object=MibTableRow
siteExtAlarmOutEntry=_SiteExtAlarmOutEntry_Object((1,3,6,1,4,1,8708,2,42,2,3,1,1))
siteExtAlarmOutEntry.setIndexNames((0,_A,_a))
if mibBuilder.loadTexts:siteExtAlarmOutEntry.setStatus(_B)
class _SiteExtAlarmOutIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SiteExtAlarmOutIndex_Type.__name__=_E
_SiteExtAlarmOutIndex_Object=MibTableColumn
siteExtAlarmOutIndex=_SiteExtAlarmOutIndex_Object((1,3,6,1,4,1,8708,2,42,2,3,1,1,1),_SiteExtAlarmOutIndex_Type())
siteExtAlarmOutIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:siteExtAlarmOutIndex.setStatus(_B)
class _SiteExtAlarmOutName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SiteExtAlarmOutName_Type.__name__=_F
_SiteExtAlarmOutName_Object=MibTableColumn
siteExtAlarmOutName=_SiteExtAlarmOutName_Object((1,3,6,1,4,1,8708,2,42,2,3,1,1,2),_SiteExtAlarmOutName_Type())
siteExtAlarmOutName.setMaxAccess(_C)
if mibBuilder.loadTexts:siteExtAlarmOutName.setStatus(_B)
class _SiteExtAlarmOutAdminStatus_Type(AdminStatusWithNA):defaultValue=3
_SiteExtAlarmOutAdminStatus_Type.__name__=_X
_SiteExtAlarmOutAdminStatus_Object=MibTableColumn
siteExtAlarmOutAdminStatus=_SiteExtAlarmOutAdminStatus_Object((1,3,6,1,4,1,8708,2,42,2,3,1,1,3),_SiteExtAlarmOutAdminStatus_Type())
siteExtAlarmOutAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:siteExtAlarmOutAdminStatus.setStatus(_B)
_SiteExtAlarmOutOperStatus_Type=OperStatusWithNA
_SiteExtAlarmOutOperStatus_Object=MibTableColumn
siteExtAlarmOutOperStatus=_SiteExtAlarmOutOperStatus_Object((1,3,6,1,4,1,8708,2,42,2,3,1,1,4),_SiteExtAlarmOutOperStatus_Type())
siteExtAlarmOutOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:siteExtAlarmOutOperStatus.setStatus(_B)
class _SiteExtAlarmOutLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_Z,2)))
_SiteExtAlarmOutLevel_Type.__name__=_H
_SiteExtAlarmOutLevel_Object=MibTableColumn
siteExtAlarmOutLevel=_SiteExtAlarmOutLevel_Object((1,3,6,1,4,1,8708,2,42,2,3,1,1,5),_SiteExtAlarmOutLevel_Type())
siteExtAlarmOutLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:siteExtAlarmOutLevel.setStatus(_B)
class _SiteExtAlarmOutSeverity_Type(AlarmPerceivedSeverity):defaultValue=3
_SiteExtAlarmOutSeverity_Type.__name__=_P
_SiteExtAlarmOutSeverity_Object=MibTableColumn
siteExtAlarmOutSeverity=_SiteExtAlarmOutSeverity_Object((1,3,6,1,4,1,8708,2,42,2,3,1,1,6),_SiteExtAlarmOutSeverity_Type())
siteExtAlarmOutSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:siteExtAlarmOutSeverity.setStatus(_B)
class _SiteExtAlarmOutText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_SiteExtAlarmOutText_Type.__name__=_F
_SiteExtAlarmOutText_Object=MibTableColumn
siteExtAlarmOutText=_SiteExtAlarmOutText_Object((1,3,6,1,4,1,8708,2,42,2,3,1,1,7),_SiteExtAlarmOutText_Type())
siteExtAlarmOutText.setMaxAccess(_D)
if mibBuilder.loadTexts:siteExtAlarmOutText.setStatus(_B)
_SiteExtAlarmOutActive_Type=FaultStatus
_SiteExtAlarmOutActive_Object=MibTableColumn
siteExtAlarmOutActive=_SiteExtAlarmOutActive_Object((1,3,6,1,4,1,8708,2,42,2,3,1,1,8),_SiteExtAlarmOutActive_Type())
siteExtAlarmOutActive.setMaxAccess(_C)
if mibBuilder.loadTexts:siteExtAlarmOutActive.setStatus(_B)
class _SiteExtAlarmOutId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SiteExtAlarmOutId_Type.__name__=_E
_SiteExtAlarmOutId_Object=MibTableColumn
siteExtAlarmOutId=_SiteExtAlarmOutId_Object((1,3,6,1,4,1,8708,2,42,2,3,1,1,9),_SiteExtAlarmOutId_Type())
siteExtAlarmOutId.setMaxAccess(_C)
if mibBuilder.loadTexts:siteExtAlarmOutId.setStatus(_B)
siteGeneralGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,42,1,1,1))
siteGeneralGroupV1.setObjects(*((_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:siteGeneralGroupV1.setStatus(_I)
siteGeneralGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,42,1,1,2))
siteGeneralGroupV2.setObjects(*((_A,_Q),(_A,_R),(_A,_S),(_A,_b)))
if mibBuilder.loadTexts:siteGeneralGroupV2.setStatus(_B)
siteExtAlarmGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,42,1,1,3))
siteExtAlarmGroupV1.setObjects(*((_A,_G),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:siteExtAlarmGroupV1.setStatus(_I)
siteExtAlarmGroupV2=ObjectGroup((1,3,6,1,4,1,8708,2,42,1,1,4))
siteExtAlarmGroupV2.setObjects(*((_A,_G),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:siteExtAlarmGroupV2.setStatus(_B)
siteExtAlarmOutGroupV1=ObjectGroup((1,3,6,1,4,1,8708,2,42,1,1,5))
siteExtAlarmOutGroupV1.setObjects(*((_A,_G),(_A,_J),(_A,_K),(_A,_U),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_T)))
if mibBuilder.loadTexts:siteExtAlarmOutGroupV1.setStatus(_B)
lumSiteBasicComplV1=ModuleCompliance((1,3,6,1,4,1,8708,2,42,1,2,1))
lumSiteBasicComplV1.setObjects(*((_A,_V),(_A,_c)))
if mibBuilder.loadTexts:lumSiteBasicComplV1.setStatus(_I)
lumSiteBasicComplV2=ModuleCompliance((1,3,6,1,4,1,8708,2,42,1,2,2))
lumSiteBasicComplV2.setObjects(*((_A,_V),(_A,_W)))
if mibBuilder.loadTexts:lumSiteBasicComplV2.setStatus(_I)
lumSiteBasicComplV3=ModuleCompliance((1,3,6,1,4,1,8708,2,42,1,2,3))
lumSiteBasicComplV3.setObjects(*((_A,_d),(_A,_W),(_A,_e)))
if mibBuilder.loadTexts:lumSiteBasicComplV3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lumSiteMIBModule':lumSiteMIBModule,'lumSiteConfs':lumSiteConfs,'lumSiteGroups':lumSiteGroups,_V:siteGeneralGroupV1,_d:siteGeneralGroupV2,_c:siteExtAlarmGroupV1,_W:siteExtAlarmGroupV2,_e:siteExtAlarmOutGroupV1,'lumSiteCompl':lumSiteCompl,'lumSiteBasicComplV1':lumSiteBasicComplV1,'lumSiteBasicComplV2':lumSiteBasicComplV2,'lumSiteBasicComplV3':lumSiteBasicComplV3,'lumSiteMIBObjects':lumSiteMIBObjects,'siteGeneral':siteGeneral,_Q:siteGeneralLastChangeTime,_R:siteGeneralStateLastChangeTime,_S:siteGeneralExtAlarmTableSize,_b:siteGeneralExtAlarmOutTableSize,'siteExtAlarmList':siteExtAlarmList,'siteExtAlarmTable':siteExtAlarmTable,'siteExtAlarmEntry':siteExtAlarmEntry,_G:siteExtAlarmIndex,_J:siteExtAlarmName,_K:siteExtAlarmAdminStatus,_L:siteExtAlarmLevel,_M:siteExtAlarmSeverity,_N:siteExtAlarmText,_O:siteExtAlarmActive,_T:siteExtAlarmId,_U:siteExtAlarmOperStatus,'siteExtAlarmOutList':siteExtAlarmOutList,'siteExtAlarmOutTable':siteExtAlarmOutTable,'siteExtAlarmOutEntry':siteExtAlarmOutEntry,_a:siteExtAlarmOutIndex,'siteExtAlarmOutName':siteExtAlarmOutName,'siteExtAlarmOutAdminStatus':siteExtAlarmOutAdminStatus,'siteExtAlarmOutOperStatus':siteExtAlarmOutOperStatus,'siteExtAlarmOutLevel':siteExtAlarmOutLevel,'siteExtAlarmOutSeverity':siteExtAlarmOutSeverity,'siteExtAlarmOutText':siteExtAlarmOutText,'siteExtAlarmOutActive':siteExtAlarmOutActive,'siteExtAlarmOutId':siteExtAlarmOutId})