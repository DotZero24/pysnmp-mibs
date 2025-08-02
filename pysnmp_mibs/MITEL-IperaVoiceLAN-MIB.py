_T='mitelIpera3000AlmResetCauseBITS'
_S='mitelIpera3000AlmResetCause'
_R='mitelIpera3000TrapAlmShutdownDetailedCause'
_Q='mitelIpera3000TrapAlmShutdownCause'
_P='mitelIpera3000AlmNbrCategories'
_O='mitelIpera3000AlmDetectDate'
_N='mitelIpera3000AlmLevel'
_M='mitelIpera3000CatTblIndex'
_L='NotificationType'
_K='Integer32'
_J='mitelIpera3000ResTblDetectDate'
_I='mitelIpera3000ResTblClusterName'
_H='mitelIpera3000ResTblPriCEID'
_G='mitelIpera3000ResTblPriSysName'
_F='sysName'
_E='SNMPv2-MIB'
_D='DisplayString'
_C='MITEL-IperaVoiceLAN-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mitelAppCallServer,mitelConfAgents,mitelConfCompliances,mitelGrpIpera3000,mitelIdCsIpera3000=mibBuilder.importSymbols('MITEL-MIB','mitelAppCallServer','mitelConfAgents','mitelConfCompliances','mitelGrpIpera3000','mitelIdCsIpera3000')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_E,_F)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier',_L,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_L,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
class DateAndTime(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8),ValueSizeConstraint(11,11))
class MitelIpera3000AlarmLevelType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('almClear',1),('almMinor',2),('almMajor',3),('almCritical',4)))
class MitelIpera3000ShutdownCause(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('resourcesLowReboot',1),('softwareFailureReboot',2),('hardwareFailureReboot',3),('softwareUpgradedReboot',4),('databaseRestoreReboot',5),('intermediateReboot',6),('l2SwitchFailureReboot',7),('remoteAlarmButtonReboot',8),('programmedReboot',9),('maintenanceCommandReboot',10),('maintenanceCommandShutdown',11),('shutdownCauseNotReported',12)))
class MitelIpera3000ResetCause(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('pushButtonReset',1),('softwareInitiatedReset',2),('powerOnReset',3),('systemFaultReset',4),('uknownReset',5)))
_MitelAppCsIpera3000_ObjectIdentity=ObjectIdentity
mitelAppCsIpera3000=_MitelAppCsIpera3000_ObjectIdentity((1,3,6,1,4,1,1027,4,1,1,2))
_MitelIpera3000System_ObjectIdentity=ObjectIdentity
mitelIpera3000System=_MitelIpera3000System_ObjectIdentity((1,3,6,1,4,1,1027,4,1,1,2,1))
_MitelIpera3000SysCapDisplay_ObjectIdentity=ObjectIdentity
mitelIpera3000SysCapDisplay=_MitelIpera3000SysCapDisplay_ObjectIdentity((1,3,6,1,4,1,1027,4,1,1,2,1,2))
_MitelIpera3000IPUsrLicPurchased_Type=Integer32
_MitelIpera3000IPUsrLicPurchased_Object=MibScalar
mitelIpera3000IPUsrLicPurchased=_MitelIpera3000IPUsrLicPurchased_Object((1,3,6,1,4,1,1027,4,1,1,2,1,2,1),_MitelIpera3000IPUsrLicPurchased_Type())
mitelIpera3000IPUsrLicPurchased.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000IPUsrLicPurchased.setStatus(_A)
_MitelIpera3000IPUsrLicUsed_Type=Integer32
_MitelIpera3000IPUsrLicUsed_Object=MibScalar
mitelIpera3000IPUsrLicUsed=_MitelIpera3000IPUsrLicUsed_Object((1,3,6,1,4,1,1027,4,1,1,2,1,2,2),_MitelIpera3000IPUsrLicUsed_Type())
mitelIpera3000IPUsrLicUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000IPUsrLicUsed.setStatus(_A)
_MitelIpera3000IPDevLicPurchased_Type=Integer32
_MitelIpera3000IPDevLicPurchased_Object=MibScalar
mitelIpera3000IPDevLicPurchased=_MitelIpera3000IPDevLicPurchased_Object((1,3,6,1,4,1,1027,4,1,1,2,1,2,3),_MitelIpera3000IPDevLicPurchased_Type())
mitelIpera3000IPDevLicPurchased.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000IPDevLicPurchased.setStatus(_A)
_MitelIpera3000IPDevLicUsed_Type=Integer32
_MitelIpera3000IPDevLicUsed_Object=MibScalar
mitelIpera3000IPDevLicUsed=_MitelIpera3000IPDevLicUsed_Object((1,3,6,1,4,1,1027,4,1,1,2,1,2,4),_MitelIpera3000IPDevLicUsed_Type())
mitelIpera3000IPDevLicUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000IPDevLicUsed.setStatus(_A)
class _MitelIpera3000CEID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MitelIpera3000CEID_Type.__name__=_D
_MitelIpera3000CEID_Object=MibScalar
mitelIpera3000CEID=_MitelIpera3000CEID_Object((1,3,6,1,4,1,1027,4,1,1,2,1,3),_MitelIpera3000CEID_Type())
mitelIpera3000CEID.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000CEID.setStatus(_A)
class _MitelIpera3000PNI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MitelIpera3000PNI_Type.__name__=_D
_MitelIpera3000PNI_Object=MibScalar
mitelIpera3000PNI=_MitelIpera3000PNI_Object((1,3,6,1,4,1,1027,4,1,1,2,1,4),_MitelIpera3000PNI_Type())
mitelIpera3000PNI.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000PNI.setStatus(_A)
class _MitelIpera3000ClusterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MitelIpera3000ClusterName_Type.__name__=_D
_MitelIpera3000ClusterName_Object=MibScalar
mitelIpera3000ClusterName=_MitelIpera3000ClusterName_Object((1,3,6,1,4,1,1027,4,1,1,2,1,5),_MitelIpera3000ClusterName_Type())
mitelIpera3000ClusterName.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000ClusterName.setStatus(_A)
_MitelIpera3000Alarms_ObjectIdentity=ObjectIdentity
mitelIpera3000Alarms=_MitelIpera3000Alarms_ObjectIdentity((1,3,6,1,4,1,1027,4,1,1,2,2))
_MitelIpera3000AlmLevel_Type=MitelIpera3000AlarmLevelType
_MitelIpera3000AlmLevel_Object=MibScalar
mitelIpera3000AlmLevel=_MitelIpera3000AlmLevel_Object((1,3,6,1,4,1,1027,4,1,1,2,2,1),_MitelIpera3000AlmLevel_Type())
mitelIpera3000AlmLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000AlmLevel.setStatus(_A)
_MitelIpera3000AlmDetectDate_Type=DateAndTime
_MitelIpera3000AlmDetectDate_Object=MibScalar
mitelIpera3000AlmDetectDate=_MitelIpera3000AlmDetectDate_Object((1,3,6,1,4,1,1027,4,1,1,2,2,2),_MitelIpera3000AlmDetectDate_Type())
mitelIpera3000AlmDetectDate.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000AlmDetectDate.setStatus(_A)
_MitelIpera3000AlmNbrCategories_Type=Integer32
_MitelIpera3000AlmNbrCategories_Object=MibScalar
mitelIpera3000AlmNbrCategories=_MitelIpera3000AlmNbrCategories_Object((1,3,6,1,4,1,1027,4,1,1,2,2,3),_MitelIpera3000AlmNbrCategories_Type())
mitelIpera3000AlmNbrCategories.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000AlmNbrCategories.setStatus(_A)
_MitelIpera3000CategoryTable_Object=MibTable
mitelIpera3000CategoryTable=_MitelIpera3000CategoryTable_Object((1,3,6,1,4,1,1027,4,1,1,2,2,4))
if mibBuilder.loadTexts:mitelIpera3000CategoryTable.setStatus(_A)
_MitelIpera3000CategoryTableEntry_Object=MibTableRow
mitelIpera3000CategoryTableEntry=_MitelIpera3000CategoryTableEntry_Object((1,3,6,1,4,1,1027,4,1,1,2,2,4,1))
mitelIpera3000CategoryTableEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:mitelIpera3000CategoryTableEntry.setStatus(_A)
class _MitelIpera3000CatTblIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MitelIpera3000CatTblIndex_Type.__name__=_K
_MitelIpera3000CatTblIndex_Object=MibTableColumn
mitelIpera3000CatTblIndex=_MitelIpera3000CatTblIndex_Object((1,3,6,1,4,1,1027,4,1,1,2,2,4,1,1),_MitelIpera3000CatTblIndex_Type())
mitelIpera3000CatTblIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000CatTblIndex.setStatus(_A)
_MitelIpera3000CatTblAvailable_Type=Integer32
_MitelIpera3000CatTblAvailable_Object=MibTableColumn
mitelIpera3000CatTblAvailable=_MitelIpera3000CatTblAvailable_Object((1,3,6,1,4,1,1027,4,1,1,2,2,4,1,2),_MitelIpera3000CatTblAvailable_Type())
mitelIpera3000CatTblAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000CatTblAvailable.setStatus(_A)
_MitelIpera3000CatTblUnavailable_Type=Integer32
_MitelIpera3000CatTblUnavailable_Object=MibTableColumn
mitelIpera3000CatTblUnavailable=_MitelIpera3000CatTblUnavailable_Object((1,3,6,1,4,1,1027,4,1,1,2,2,4,1,3),_MitelIpera3000CatTblUnavailable_Type())
mitelIpera3000CatTblUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000CatTblUnavailable.setStatus(_A)
_MitelIpera3000CatTblLevel_Type=MitelIpera3000AlarmLevelType
_MitelIpera3000CatTblLevel_Object=MibTableColumn
mitelIpera3000CatTblLevel=_MitelIpera3000CatTblLevel_Object((1,3,6,1,4,1,1027,4,1,1,2,2,4,1,4),_MitelIpera3000CatTblLevel_Type())
mitelIpera3000CatTblLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000CatTblLevel.setStatus(_A)
_MitelIpera3000CatTblMinorThresh_Type=Integer32
_MitelIpera3000CatTblMinorThresh_Object=MibTableColumn
mitelIpera3000CatTblMinorThresh=_MitelIpera3000CatTblMinorThresh_Object((1,3,6,1,4,1,1027,4,1,1,2,2,4,1,5),_MitelIpera3000CatTblMinorThresh_Type())
mitelIpera3000CatTblMinorThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000CatTblMinorThresh.setStatus(_A)
_MitelIpera3000CatTblMajorThresh_Type=Integer32
_MitelIpera3000CatTblMajorThresh_Object=MibTableColumn
mitelIpera3000CatTblMajorThresh=_MitelIpera3000CatTblMajorThresh_Object((1,3,6,1,4,1,1027,4,1,1,2,2,4,1,6),_MitelIpera3000CatTblMajorThresh_Type())
mitelIpera3000CatTblMajorThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000CatTblMajorThresh.setStatus(_A)
_MitelIpera3000CatTblCriticalThresh_Type=Integer32
_MitelIpera3000CatTblCriticalThresh_Object=MibTableColumn
mitelIpera3000CatTblCriticalThresh=_MitelIpera3000CatTblCriticalThresh_Object((1,3,6,1,4,1,1027,4,1,1,2,2,4,1,7),_MitelIpera3000CatTblCriticalThresh_Type())
mitelIpera3000CatTblCriticalThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000CatTblCriticalThresh.setStatus(_A)
class _MitelIpera3000CatTblName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MitelIpera3000CatTblName_Type.__name__=_D
_MitelIpera3000CatTblName_Object=MibTableColumn
mitelIpera3000CatTblName=_MitelIpera3000CatTblName_Object((1,3,6,1,4,1,1027,4,1,1,2,2,4,1,8),_MitelIpera3000CatTblName_Type())
mitelIpera3000CatTblName.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000CatTblName.setStatus(_A)
_MitelIpera3000TrapAlmShutdownCause_Type=MitelIpera3000ShutdownCause
_MitelIpera3000TrapAlmShutdownCause_Object=MibScalar
mitelIpera3000TrapAlmShutdownCause=_MitelIpera3000TrapAlmShutdownCause_Object((1,3,6,1,4,1,1027,4,1,1,2,2,5),_MitelIpera3000TrapAlmShutdownCause_Type())
mitelIpera3000TrapAlmShutdownCause.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000TrapAlmShutdownCause.setStatus(_A)
_MitelIpera3000TrapAlmShutdownDetailedCause_Type=Integer32
_MitelIpera3000TrapAlmShutdownDetailedCause_Object=MibScalar
mitelIpera3000TrapAlmShutdownDetailedCause=_MitelIpera3000TrapAlmShutdownDetailedCause_Object((1,3,6,1,4,1,1027,4,1,1,2,2,6),_MitelIpera3000TrapAlmShutdownDetailedCause_Type())
mitelIpera3000TrapAlmShutdownDetailedCause.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000TrapAlmShutdownDetailedCause.setStatus(_A)
_MitelIpera3000AlmResetCause_Type=MitelIpera3000ResetCause
_MitelIpera3000AlmResetCause_Object=MibScalar
mitelIpera3000AlmResetCause=_MitelIpera3000AlmResetCause_Object((1,3,6,1,4,1,1027,4,1,1,2,2,7),_MitelIpera3000AlmResetCause_Type())
mitelIpera3000AlmResetCause.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000AlmResetCause.setStatus(_A)
_MitelIpera3000AlmResetCauseBITS_Type=Integer32
_MitelIpera3000AlmResetCauseBITS_Object=MibScalar
mitelIpera3000AlmResetCauseBITS=_MitelIpera3000AlmResetCauseBITS_Object((1,3,6,1,4,1,1027,4,1,1,2,2,8),_MitelIpera3000AlmResetCauseBITS_Type())
mitelIpera3000AlmResetCauseBITS.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000AlmResetCauseBITS.setStatus(_A)
_MitelIpera3000Notifications_ObjectIdentity=ObjectIdentity
mitelIpera3000Notifications=_MitelIpera3000Notifications_ObjectIdentity((1,3,6,1,4,1,1027,4,1,1,2,3))
_MitelIpera3000Resilience_ObjectIdentity=ObjectIdentity
mitelIpera3000Resilience=_MitelIpera3000Resilience_ObjectIdentity((1,3,6,1,4,1,1027,4,1,1,2,4))
_MitelIpera3000ResTable_Object=MibTable
mitelIpera3000ResTable=_MitelIpera3000ResTable_Object((1,3,6,1,4,1,1027,4,1,1,2,4,1))
if mibBuilder.loadTexts:mitelIpera3000ResTable.setStatus(_A)
_MitelIpera3000ResTableEntry_Object=MibTableRow
mitelIpera3000ResTableEntry=_MitelIpera3000ResTableEntry_Object((1,3,6,1,4,1,1027,4,1,1,2,4,1,1))
mitelIpera3000ResTableEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:mitelIpera3000ResTableEntry.setStatus(_A)
class _MitelIpera3000ResTblPriSysName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MitelIpera3000ResTblPriSysName_Type.__name__=_D
_MitelIpera3000ResTblPriSysName_Object=MibTableColumn
mitelIpera3000ResTblPriSysName=_MitelIpera3000ResTblPriSysName_Object((1,3,6,1,4,1,1027,4,1,1,2,4,1,1,1),_MitelIpera3000ResTblPriSysName_Type())
mitelIpera3000ResTblPriSysName.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000ResTblPriSysName.setStatus(_A)
class _MitelIpera3000ResTblPriCEID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MitelIpera3000ResTblPriCEID_Type.__name__=_D
_MitelIpera3000ResTblPriCEID_Object=MibTableColumn
mitelIpera3000ResTblPriCEID=_MitelIpera3000ResTblPriCEID_Object((1,3,6,1,4,1,1027,4,1,1,2,4,1,1,2),_MitelIpera3000ResTblPriCEID_Type())
mitelIpera3000ResTblPriCEID.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000ResTblPriCEID.setStatus(_A)
class _MitelIpera3000ResTblClusterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MitelIpera3000ResTblClusterName_Type.__name__=_D
_MitelIpera3000ResTblClusterName_Object=MibTableColumn
mitelIpera3000ResTblClusterName=_MitelIpera3000ResTblClusterName_Object((1,3,6,1,4,1,1027,4,1,1,2,4,1,1,3),_MitelIpera3000ResTblClusterName_Type())
mitelIpera3000ResTblClusterName.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000ResTblClusterName.setStatus(_A)
_MitelIpera3000ResTblDetectDate_Type=DateAndTime
_MitelIpera3000ResTblDetectDate_Object=MibTableColumn
mitelIpera3000ResTblDetectDate=_MitelIpera3000ResTblDetectDate_Object((1,3,6,1,4,1,1027,4,1,1,2,4,1,1,4),_MitelIpera3000ResTblDetectDate_Type())
mitelIpera3000ResTblDetectDate.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000ResTblDetectDate.setStatus(_A)
class _MitelIpera3000ResTblStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('firstSetFailover',1),('healthCheckComplete',2),('handOffComplete',3)))
_MitelIpera3000ResTblStatus_Type.__name__=_K
_MitelIpera3000ResTblStatus_Object=MibTableColumn
mitelIpera3000ResTblStatus=_MitelIpera3000ResTblStatus_Object((1,3,6,1,4,1,1027,4,1,1,2,4,1,1,5),_MitelIpera3000ResTblStatus_Type())
mitelIpera3000ResTblStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelIpera3000ResTblStatus.setStatus(_A)
_MitelIpera3000Applications_ObjectIdentity=ObjectIdentity
mitelIpera3000Applications=_MitelIpera3000Applications_ObjectIdentity((1,3,6,1,4,1,1027,4,1,1,2,5))
_MitelComplIpera3000_ObjectIdentity=ObjectIdentity
mitelComplIpera3000=_MitelComplIpera3000_ObjectIdentity((1,3,6,1,4,1,1027,5,1,4))
_MitelGrpIpera3000System_ObjectIdentity=ObjectIdentity
mitelGrpIpera3000System=_MitelGrpIpera3000System_ObjectIdentity((1,3,6,1,4,1,1027,5,2,4,1))
_MitelGrpIpera3000Alarms_ObjectIdentity=ObjectIdentity
mitelGrpIpera3000Alarms=_MitelGrpIpera3000Alarms_ObjectIdentity((1,3,6,1,4,1,1027,5,2,4,2))
_MitelAgentIpera3000_ObjectIdentity=ObjectIdentity
mitelAgentIpera3000=_MitelAgentIpera3000_ObjectIdentity((1,3,6,1,4,1,1027,5,3,3))
mitelIpera3000NotifAlarm=NotificationType((1,3,6,1,4,1,1027,1,2,3,0,301))
mitelIpera3000NotifAlarm.setObjects(*((_E,_F),(_C,_N),(_C,_O),(_C,_P)))
if mibBuilder.loadTexts:mitelIpera3000NotifAlarm.setStatus('')
mitelIpera3000ShutdownAlarm=NotificationType((1,3,6,1,4,1,1027,1,2,3,0,302))
mitelIpera3000ShutdownAlarm.setObjects(*((_E,_F),(_C,_Q),(_C,_R)))
if mibBuilder.loadTexts:mitelIpera3000ShutdownAlarm.setStatus('')
mitelIpera3000RestartCompleteAlarm=NotificationType((1,3,6,1,4,1,1027,1,2,3,0,303))
mitelIpera3000RestartCompleteAlarm.setObjects(*((_E,_F),(_C,_S),(_C,_T)))
if mibBuilder.loadTexts:mitelIpera3000RestartCompleteAlarm.setStatus('')
mitelIpera3000NotifResiltFirstSetFailover=NotificationType((1,3,6,1,4,1,1027,1,2,3,0,501))
mitelIpera3000NotifResiltFirstSetFailover.setObjects(*((_E,_F),(_C,_H),(_C,_G),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:mitelIpera3000NotifResiltFirstSetFailover.setStatus('')
mitelIpera3000NotifResiltHealthCheckComplete=NotificationType((1,3,6,1,4,1,1027,1,2,3,0,502))
mitelIpera3000NotifResiltHealthCheckComplete.setObjects(*((_E,_F),(_C,_H),(_C,_G),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:mitelIpera3000NotifResiltHealthCheckComplete.setStatus('')
mitelIpera3000NotifResiltHandoffComplete=NotificationType((1,3,6,1,4,1,1027,1,2,3,0,503))
mitelIpera3000NotifResiltHandoffComplete.setObjects(*((_E,_F),(_C,_H),(_C,_G),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:mitelIpera3000NotifResiltHandoffComplete.setStatus('')
mibBuilder.exportSymbols(_C,**{'DateAndTime':DateAndTime,'MitelIpera3000AlarmLevelType':MitelIpera3000AlarmLevelType,'MitelIpera3000ShutdownCause':MitelIpera3000ShutdownCause,'MitelIpera3000ResetCause':MitelIpera3000ResetCause,'mitelIpera3000NotifAlarm':mitelIpera3000NotifAlarm,'mitelIpera3000ShutdownAlarm':mitelIpera3000ShutdownAlarm,'mitelIpera3000RestartCompleteAlarm':mitelIpera3000RestartCompleteAlarm,'mitelIpera3000NotifResiltFirstSetFailover':mitelIpera3000NotifResiltFirstSetFailover,'mitelIpera3000NotifResiltHealthCheckComplete':mitelIpera3000NotifResiltHealthCheckComplete,'mitelIpera3000NotifResiltHandoffComplete':mitelIpera3000NotifResiltHandoffComplete,'mitelAppCsIpera3000':mitelAppCsIpera3000,'mitelIpera3000System':mitelIpera3000System,'mitelIpera3000SysCapDisplay':mitelIpera3000SysCapDisplay,'mitelIpera3000IPUsrLicPurchased':mitelIpera3000IPUsrLicPurchased,'mitelIpera3000IPUsrLicUsed':mitelIpera3000IPUsrLicUsed,'mitelIpera3000IPDevLicPurchased':mitelIpera3000IPDevLicPurchased,'mitelIpera3000IPDevLicUsed':mitelIpera3000IPDevLicUsed,'mitelIpera3000CEID':mitelIpera3000CEID,'mitelIpera3000PNI':mitelIpera3000PNI,'mitelIpera3000ClusterName':mitelIpera3000ClusterName,'mitelIpera3000Alarms':mitelIpera3000Alarms,_N:mitelIpera3000AlmLevel,_O:mitelIpera3000AlmDetectDate,_P:mitelIpera3000AlmNbrCategories,'mitelIpera3000CategoryTable':mitelIpera3000CategoryTable,'mitelIpera3000CategoryTableEntry':mitelIpera3000CategoryTableEntry,_M:mitelIpera3000CatTblIndex,'mitelIpera3000CatTblAvailable':mitelIpera3000CatTblAvailable,'mitelIpera3000CatTblUnavailable':mitelIpera3000CatTblUnavailable,'mitelIpera3000CatTblLevel':mitelIpera3000CatTblLevel,'mitelIpera3000CatTblMinorThresh':mitelIpera3000CatTblMinorThresh,'mitelIpera3000CatTblMajorThresh':mitelIpera3000CatTblMajorThresh,'mitelIpera3000CatTblCriticalThresh':mitelIpera3000CatTblCriticalThresh,'mitelIpera3000CatTblName':mitelIpera3000CatTblName,_Q:mitelIpera3000TrapAlmShutdownCause,_R:mitelIpera3000TrapAlmShutdownDetailedCause,_S:mitelIpera3000AlmResetCause,_T:mitelIpera3000AlmResetCauseBITS,'mitelIpera3000Notifications':mitelIpera3000Notifications,'mitelIpera3000Resilience':mitelIpera3000Resilience,'mitelIpera3000ResTable':mitelIpera3000ResTable,'mitelIpera3000ResTableEntry':mitelIpera3000ResTableEntry,_G:mitelIpera3000ResTblPriSysName,_H:mitelIpera3000ResTblPriCEID,_I:mitelIpera3000ResTblClusterName,_J:mitelIpera3000ResTblDetectDate,'mitelIpera3000ResTblStatus':mitelIpera3000ResTblStatus,'mitelIpera3000Applications':mitelIpera3000Applications,'mitelComplIpera3000':mitelComplIpera3000,'mitelGrpIpera3000System':mitelGrpIpera3000System,'mitelGrpIpera3000Alarms':mitelGrpIpera3000Alarms,'mitelAgentIpera3000':mitelAgentIpera3000})