_b='cwmStatConfigGroup'
_a='cwmUploadGroup'
_Z='deprecated'
_Y='cwmUploadCounter'
_X='cwmSCTFileVerOpr'
_W='cwmSCTFileVerCfg'
_V='cwmStatMaximumConnections'
_U='cwmStatCollectionInterval'
_T='cwmStatCollectionStatus'
_S='cwmStatLevelConfigured'
_R='cwmStatCurrentLevel'
_Q='cwmStatBucketInterval'
_P='cwmAutoLineDiagEnable'
_O='cwmIngressSCTFileName'
_N='cwmIngressSCTFileId'
_M='StatisticsLevel'
_L='minutes'
_K='disable'
_J='enable'
_I='cwmConfigGroup2'
_H='cwmIndex'
_G='cwmConfigGroup'
_F='read-only'
_E='Integer32'
_D='Unsigned32'
_C='read-write'
_B='CISCO-WAN-MODULE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoWanModuleMIB=ModuleIdentity((1,3,6,1,4,1,9,9,145))
if mibBuilder.loadTexts:ciscoWanModuleMIB.setRevisions(('2002-09-11 00:00','2001-07-20 00:00','1999-10-22 00:00'))
class StatisticsLevel(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('notApplicable',0),('levelOne',1),('levelTwo',2),('levelThree',3)))
_CwmMIBObjects_ObjectIdentity=ObjectIdentity
cwmMIBObjects=_CwmMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,145,1))
_CwmConfig_ObjectIdentity=ObjectIdentity
cwmConfig=_CwmConfig_ObjectIdentity((1,3,6,1,4,1,9,9,145,1,1))
_CwmConfigTable_Object=MibTable
cwmConfigTable=_CwmConfigTable_Object((1,3,6,1,4,1,9,9,145,1,1,1))
if mibBuilder.loadTexts:cwmConfigTable.setStatus(_A)
_CwmConfigEntry_Object=MibTableRow
cwmConfigEntry=_CwmConfigEntry_Object((1,3,6,1,4,1,9,9,145,1,1,1,1))
cwmConfigEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cwmConfigEntry.setStatus(_A)
class _CwmIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CwmIndex_Type.__name__=_D
_CwmIndex_Object=MibTableColumn
cwmIndex=_CwmIndex_Object((1,3,6,1,4,1,9,9,145,1,1,1,1,1),_CwmIndex_Type())
cwmIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cwmIndex.setStatus(_A)
class _CwmIngressSCTFileId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CwmIngressSCTFileId_Type.__name__=_D
_CwmIngressSCTFileId_Object=MibTableColumn
cwmIngressSCTFileId=_CwmIngressSCTFileId_Object((1,3,6,1,4,1,9,9,145,1,1,1,1,2),_CwmIngressSCTFileId_Type())
cwmIngressSCTFileId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwmIngressSCTFileId.setStatus(_A)
_CwmIngressSCTFileName_Type=DisplayString
_CwmIngressSCTFileName_Object=MibTableColumn
cwmIngressSCTFileName=_CwmIngressSCTFileName_Object((1,3,6,1,4,1,9,9,145,1,1,1,1,3),_CwmIngressSCTFileName_Type())
cwmIngressSCTFileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cwmIngressSCTFileName.setStatus(_A)
class _CwmAutoLineDiagEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_CwmAutoLineDiagEnable_Type.__name__=_E
_CwmAutoLineDiagEnable_Object=MibTableColumn
cwmAutoLineDiagEnable=_CwmAutoLineDiagEnable_Object((1,3,6,1,4,1,9,9,145,1,1,1,1,4),_CwmAutoLineDiagEnable_Type())
cwmAutoLineDiagEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cwmAutoLineDiagEnable.setStatus(_A)
class _CwmSCTFileVerCfg_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwmSCTFileVerCfg_Type.__name__=_D
_CwmSCTFileVerCfg_Object=MibTableColumn
cwmSCTFileVerCfg=_CwmSCTFileVerCfg_Object((1,3,6,1,4,1,9,9,145,1,1,1,1,5),_CwmSCTFileVerCfg_Type())
cwmSCTFileVerCfg.setMaxAccess(_C)
if mibBuilder.loadTexts:cwmSCTFileVerCfg.setStatus(_A)
class _CwmSCTFileVerOpr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwmSCTFileVerOpr_Type.__name__=_D
_CwmSCTFileVerOpr_Object=MibTableColumn
cwmSCTFileVerOpr=_CwmSCTFileVerOpr_Object((1,3,6,1,4,1,9,9,145,1,1,1,1,6),_CwmSCTFileVerOpr_Type())
cwmSCTFileVerOpr.setMaxAccess(_F)
if mibBuilder.loadTexts:cwmSCTFileVerOpr.setStatus(_A)
class _CwmUploadCounter_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwmUploadCounter_Type.__name__=_D
_CwmUploadCounter_Object=MibTableColumn
cwmUploadCounter=_CwmUploadCounter_Object((1,3,6,1,4,1,9,9,145,1,1,1,1,7),_CwmUploadCounter_Type())
cwmUploadCounter.setMaxAccess(_F)
if mibBuilder.loadTexts:cwmUploadCounter.setStatus(_A)
_CwmStatsConfig_ObjectIdentity=ObjectIdentity
cwmStatsConfig=_CwmStatsConfig_ObjectIdentity((1,3,6,1,4,1,9,9,145,1,2))
_CwmStatConfigTable_Object=MibTable
cwmStatConfigTable=_CwmStatConfigTable_Object((1,3,6,1,4,1,9,9,145,1,2,1))
if mibBuilder.loadTexts:cwmStatConfigTable.setStatus(_A)
_CwmStatConfigEntry_Object=MibTableRow
cwmStatConfigEntry=_CwmStatConfigEntry_Object((1,3,6,1,4,1,9,9,145,1,2,1,1))
cwmStatConfigEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cwmStatConfigEntry.setStatus(_A)
class _CwmStatBucketInterval_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,10,15,20,30,60)));namedValues=NamedValues(*(('five',5),('ten',10),('fifteen',15),('twenty',20),('thirty',30),('sixty',60)))
_CwmStatBucketInterval_Type.__name__=_E
_CwmStatBucketInterval_Object=MibTableColumn
cwmStatBucketInterval=_CwmStatBucketInterval_Object((1,3,6,1,4,1,9,9,145,1,2,1,1,1),_CwmStatBucketInterval_Type())
cwmStatBucketInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cwmStatBucketInterval.setStatus(_A)
if mibBuilder.loadTexts:cwmStatBucketInterval.setUnits(_L)
class _CwmStatCollectionInterval_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,5)));namedValues=NamedValues(*(('default',0),('one',1),('five',5)))
_CwmStatCollectionInterval_Type.__name__=_E
_CwmStatCollectionInterval_Object=MibTableColumn
cwmStatCollectionInterval=_CwmStatCollectionInterval_Object((1,3,6,1,4,1,9,9,145,1,2,1,1,2),_CwmStatCollectionInterval_Type())
cwmStatCollectionInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cwmStatCollectionInterval.setStatus(_A)
if mibBuilder.loadTexts:cwmStatCollectionInterval.setUnits(_L)
class _CwmStatCollectionStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_CwmStatCollectionStatus_Type.__name__=_E
_CwmStatCollectionStatus_Object=MibTableColumn
cwmStatCollectionStatus=_CwmStatCollectionStatus_Object((1,3,6,1,4,1,9,9,145,1,2,1,1,3),_CwmStatCollectionStatus_Type())
cwmStatCollectionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwmStatCollectionStatus.setStatus(_A)
_CwmStatCurrentLevel_Type=StatisticsLevel
_CwmStatCurrentLevel_Object=MibTableColumn
cwmStatCurrentLevel=_CwmStatCurrentLevel_Object((1,3,6,1,4,1,9,9,145,1,2,1,1,4),_CwmStatCurrentLevel_Type())
cwmStatCurrentLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:cwmStatCurrentLevel.setStatus(_A)
class _CwmStatLevelConfigured_Type(StatisticsLevel):defaultValue=1
_CwmStatLevelConfigured_Type.__name__=_M
_CwmStatLevelConfigured_Object=MibTableColumn
cwmStatLevelConfigured=_CwmStatLevelConfigured_Object((1,3,6,1,4,1,9,9,145,1,2,1,1,5),_CwmStatLevelConfigured_Type())
cwmStatLevelConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:cwmStatLevelConfigured.setStatus(_A)
_CwmStatMaximumConnections_Type=Unsigned32
_CwmStatMaximumConnections_Object=MibTableColumn
cwmStatMaximumConnections=_CwmStatMaximumConnections_Object((1,3,6,1,4,1,9,9,145,1,2,1,1,6),_CwmStatMaximumConnections_Type())
cwmStatMaximumConnections.setMaxAccess(_F)
if mibBuilder.loadTexts:cwmStatMaximumConnections.setStatus(_A)
_CiscoWanModuleMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoWanModuleMIBNotificationPrefix=_CiscoWanModuleMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,145,2))
_CiscoWanModuleMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoWanModuleMIBNotifications=_CiscoWanModuleMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,145,2,0))
_CiscoWanModuleMIBConformance_ObjectIdentity=ObjectIdentity
ciscoWanModuleMIBConformance=_CiscoWanModuleMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,145,3))
_CiscoWanModuleMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWanModuleMIBCompliances=_CiscoWanModuleMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,145,3,1))
_CiscoWanModuleMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWanModuleMIBGroups=_CiscoWanModuleMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,145,3,2))
cwmConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,145,3,2,1))
cwmConfigGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:cwmConfigGroup.setStatus(_A)
cwmStatConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,145,3,2,2))
cwmStatConfigGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:cwmStatConfigGroup.setStatus(_A)
cwmConfigGroup2=ObjectGroup((1,3,6,1,4,1,9,9,145,3,2,3))
cwmConfigGroup2.setObjects(*((_B,_W),(_B,_X)))
if mibBuilder.loadTexts:cwmConfigGroup2.setStatus(_A)
cwmUploadGroup=ObjectGroup((1,3,6,1,4,1,9,9,145,3,2,4))
cwmUploadGroup.setObjects((_B,_Y))
if mibBuilder.loadTexts:cwmUploadGroup.setStatus(_A)
ciscoWanModuleMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,145,3,1,1))
ciscoWanModuleMIBCompliance.setObjects((_B,_G))
if mibBuilder.loadTexts:ciscoWanModuleMIBCompliance.setStatus(_Z)
ciscoWanModuleMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,145,3,1,2))
ciscoWanModuleMIBComplianceRev1.setObjects(*((_B,_G),(_B,_I)))
if mibBuilder.loadTexts:ciscoWanModuleMIBComplianceRev1.setStatus(_Z)
ciscoWanModuleMIBComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,145,3,1,3))
ciscoWanModuleMIBComplianceRev2.setObjects(*((_B,_G),(_B,_I),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:ciscoWanModuleMIBComplianceRev2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_M:StatisticsLevel,'ciscoWanModuleMIB':ciscoWanModuleMIB,'cwmMIBObjects':cwmMIBObjects,'cwmConfig':cwmConfig,'cwmConfigTable':cwmConfigTable,'cwmConfigEntry':cwmConfigEntry,_H:cwmIndex,_N:cwmIngressSCTFileId,_O:cwmIngressSCTFileName,_P:cwmAutoLineDiagEnable,_W:cwmSCTFileVerCfg,_X:cwmSCTFileVerOpr,_Y:cwmUploadCounter,'cwmStatsConfig':cwmStatsConfig,'cwmStatConfigTable':cwmStatConfigTable,'cwmStatConfigEntry':cwmStatConfigEntry,_Q:cwmStatBucketInterval,_U:cwmStatCollectionInterval,_T:cwmStatCollectionStatus,_R:cwmStatCurrentLevel,_S:cwmStatLevelConfigured,_V:cwmStatMaximumConnections,'ciscoWanModuleMIBNotificationPrefix':ciscoWanModuleMIBNotificationPrefix,'ciscoWanModuleMIBNotifications':ciscoWanModuleMIBNotifications,'ciscoWanModuleMIBConformance':ciscoWanModuleMIBConformance,'ciscoWanModuleMIBCompliances':ciscoWanModuleMIBCompliances,'ciscoWanModuleMIBCompliance':ciscoWanModuleMIBCompliance,'ciscoWanModuleMIBComplianceRev1':ciscoWanModuleMIBComplianceRev1,'ciscoWanModuleMIBComplianceRev2':ciscoWanModuleMIBComplianceRev2,'ciscoWanModuleMIBGroups':ciscoWanModuleMIBGroups,_G:cwmConfigGroup,_b:cwmStatConfigGroup,_I:cwmConfigGroup2,_a:cwmUploadGroup})