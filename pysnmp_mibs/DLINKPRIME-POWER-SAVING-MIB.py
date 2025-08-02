_Q='dppsIfEeeCfgGroup'
_P='dppsShutdownCfgGroup'
_O='dppsDimLedCfgGroup'
_N='dppsIfEeeStatus'
_M='dppsPortShutdownTimeRange'
_L='dppsPortShutdownEnabled'
_K='dppsDimLedTimeRange'
_J='dppsLedAdminEnabled'
_I='dppsDimLedEnabled'
_H='Integer32'
_G='ifIndex'
_F='IF-MIB'
_E='DisplayString'
_D='TruthValue'
_C='read-write'
_B='DLINKPRIME-POWER-SAVING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention',_D)
dlinkPrimePowerSavingMIB=ModuleIdentity((1,3,6,1,4,1,171,15,12))
if mibBuilder.loadTexts:dlinkPrimePowerSavingMIB.setRevisions(('2013-01-31 00:00','2014-04-26 00:00'))
_DpPowerSavingMIBNotifications_ObjectIdentity=ObjectIdentity
dpPowerSavingMIBNotifications=_DpPowerSavingMIBNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,12,0))
_DpPowerSavingMIBObjects_ObjectIdentity=ObjectIdentity
dpPowerSavingMIBObjects=_DpPowerSavingMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,12,1))
_DpPowerSavingGeneral_ObjectIdentity=ObjectIdentity
dpPowerSavingGeneral=_DpPowerSavingGeneral_ObjectIdentity((1,3,6,1,4,1,171,15,12,1,1))
class _DppsLinkDetectionEnabled_Type(TruthValue):defaultValue=2
_DppsLinkDetectionEnabled_Type.__name__=_D
_DppsLinkDetectionEnabled_Object=MibScalar
dppsLinkDetectionEnabled=_DppsLinkDetectionEnabled_Object((1,3,6,1,4,1,171,15,12,1,1,1),_DppsLinkDetectionEnabled_Type())
dppsLinkDetectionEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dppsLinkDetectionEnabled.setStatus(_A)
class _DppsHibernationEnabled_Type(TruthValue):defaultValue=2
_DppsHibernationEnabled_Type.__name__=_D
_DppsHibernationEnabled_Object=MibScalar
dppsHibernationEnabled=_DppsHibernationEnabled_Object((1,3,6,1,4,1,171,15,12,1,1,2),_DppsHibernationEnabled_Type())
dppsHibernationEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dppsHibernationEnabled.setStatus(_A)
class _DppsDimLedEnabled_Type(TruthValue):defaultValue=2
_DppsDimLedEnabled_Type.__name__=_D
_DppsDimLedEnabled_Object=MibScalar
dppsDimLedEnabled=_DppsDimLedEnabled_Object((1,3,6,1,4,1,171,15,12,1,1,3),_DppsDimLedEnabled_Type())
dppsDimLedEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dppsDimLedEnabled.setStatus(_A)
class _DppsLedAdminEnabled_Type(TruthValue):defaultValue=1
_DppsLedAdminEnabled_Type.__name__=_D
_DppsLedAdminEnabled_Object=MibScalar
dppsLedAdminEnabled=_DppsLedAdminEnabled_Object((1,3,6,1,4,1,171,15,12,1,1,4),_DppsLedAdminEnabled_Type())
dppsLedAdminEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dppsLedAdminEnabled.setStatus(_A)
class _DppsPortShutdownEnabled_Type(TruthValue):defaultValue=2
_DppsPortShutdownEnabled_Type.__name__=_D
_DppsPortShutdownEnabled_Object=MibScalar
dppsPortShutdownEnabled=_DppsPortShutdownEnabled_Object((1,3,6,1,4,1,171,15,12,1,1,5),_DppsPortShutdownEnabled_Type())
dppsPortShutdownEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:dppsPortShutdownEnabled.setStatus(_A)
_DpPowerSavingIfObjects_ObjectIdentity=ObjectIdentity
dpPowerSavingIfObjects=_DpPowerSavingIfObjects_ObjectIdentity((1,3,6,1,4,1,171,15,12,1,2))
_DppsIfEeeTable_Object=MibTable
dppsIfEeeTable=_DppsIfEeeTable_Object((1,3,6,1,4,1,171,15,12,1,2,1))
if mibBuilder.loadTexts:dppsIfEeeTable.setStatus(_A)
_DppsIfEeeEntry_Object=MibTableRow
dppsIfEeeEntry=_DppsIfEeeEntry_Object((1,3,6,1,4,1,171,15,12,1,2,1,1))
dppsIfEeeEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dppsIfEeeEntry.setStatus(_A)
class _DppsIfEeeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_DppsIfEeeStatus_Type.__name__=_H
_DppsIfEeeStatus_Object=MibTableColumn
dppsIfEeeStatus=_DppsIfEeeStatus_Object((1,3,6,1,4,1,171,15,12,1,2,1,1,2),_DppsIfEeeStatus_Type())
dppsIfEeeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dppsIfEeeStatus.setStatus(_A)
_DppsScheduleCtrl_ObjectIdentity=ObjectIdentity
dppsScheduleCtrl=_DppsScheduleCtrl_ObjectIdentity((1,3,6,1,4,1,171,15,12,1,3))
class _DppsHibernationTimeRange_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_DppsHibernationTimeRange_Type.__name__=_E
_DppsHibernationTimeRange_Object=MibScalar
dppsHibernationTimeRange=_DppsHibernationTimeRange_Object((1,3,6,1,4,1,171,15,12,1,3,1),_DppsHibernationTimeRange_Type())
dppsHibernationTimeRange.setMaxAccess(_C)
if mibBuilder.loadTexts:dppsHibernationTimeRange.setStatus(_A)
class _DppsDimLedTimeRange_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_DppsDimLedTimeRange_Type.__name__=_E
_DppsDimLedTimeRange_Object=MibScalar
dppsDimLedTimeRange=_DppsDimLedTimeRange_Object((1,3,6,1,4,1,171,15,12,1,3,2),_DppsDimLedTimeRange_Type())
dppsDimLedTimeRange.setMaxAccess(_C)
if mibBuilder.loadTexts:dppsDimLedTimeRange.setStatus(_A)
_DppsPortShutdownScheduleTable_Object=MibTable
dppsPortShutdownScheduleTable=_DppsPortShutdownScheduleTable_Object((1,3,6,1,4,1,171,15,12,1,3,3))
if mibBuilder.loadTexts:dppsPortShutdownScheduleTable.setStatus(_A)
_DppsPortShutdownScheduleEntry_Object=MibTableRow
dppsPortShutdownScheduleEntry=_DppsPortShutdownScheduleEntry_Object((1,3,6,1,4,1,171,15,12,1,3,3,1))
dppsPortShutdownScheduleEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dppsPortShutdownScheduleEntry.setStatus(_A)
class _DppsPortShutdownTimeRange_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_DppsPortShutdownTimeRange_Type.__name__=_E
_DppsPortShutdownTimeRange_Object=MibTableColumn
dppsPortShutdownTimeRange=_DppsPortShutdownTimeRange_Object((1,3,6,1,4,1,171,15,12,1,3,3,1,1),_DppsPortShutdownTimeRange_Type())
dppsPortShutdownTimeRange.setMaxAccess(_C)
if mibBuilder.loadTexts:dppsPortShutdownTimeRange.setStatus(_A)
_DpPowerSavingMIBConformance_ObjectIdentity=ObjectIdentity
dpPowerSavingMIBConformance=_DpPowerSavingMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,12,2))
_DppsMIBCompliances_ObjectIdentity=ObjectIdentity
dppsMIBCompliances=_DppsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,12,2,1))
_DppsMIBGroups_ObjectIdentity=ObjectIdentity
dppsMIBGroups=_DppsMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,15,12,2,2))
dppsDimLedCfgGroup=ObjectGroup((1,3,6,1,4,1,171,15,12,2,2,1))
dppsDimLedCfgGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:dppsDimLedCfgGroup.setStatus(_A)
dppsShutdownCfgGroup=ObjectGroup((1,3,6,1,4,1,171,15,12,2,2,2))
dppsShutdownCfgGroup.setObjects(*((_B,_L),(_B,_M)))
if mibBuilder.loadTexts:dppsShutdownCfgGroup.setStatus(_A)
dppsIfEeeCfgGroup=ObjectGroup((1,3,6,1,4,1,171,15,12,2,2,3))
dppsIfEeeCfgGroup.setObjects((_B,_N))
if mibBuilder.loadTexts:dppsIfEeeCfgGroup.setStatus(_A)
dppsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,12,2,1,1))
dppsMIBCompliance.setObjects(*((_B,'dppsLinkCfgGroup'),(_B,'dppsLenCfgGroup'),(_B,'dppsHiberCfgGroup'),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:dppsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlinkPrimePowerSavingMIB':dlinkPrimePowerSavingMIB,'dpPowerSavingMIBNotifications':dpPowerSavingMIBNotifications,'dpPowerSavingMIBObjects':dpPowerSavingMIBObjects,'dpPowerSavingGeneral':dpPowerSavingGeneral,'dppsLinkDetectionEnabled':dppsLinkDetectionEnabled,'dppsHibernationEnabled':dppsHibernationEnabled,_I:dppsDimLedEnabled,_J:dppsLedAdminEnabled,_L:dppsPortShutdownEnabled,'dpPowerSavingIfObjects':dpPowerSavingIfObjects,'dppsIfEeeTable':dppsIfEeeTable,'dppsIfEeeEntry':dppsIfEeeEntry,_N:dppsIfEeeStatus,'dppsScheduleCtrl':dppsScheduleCtrl,'dppsHibernationTimeRange':dppsHibernationTimeRange,_K:dppsDimLedTimeRange,'dppsPortShutdownScheduleTable':dppsPortShutdownScheduleTable,'dppsPortShutdownScheduleEntry':dppsPortShutdownScheduleEntry,_M:dppsPortShutdownTimeRange,'dpPowerSavingMIBConformance':dpPowerSavingMIBConformance,'dppsMIBCompliances':dppsMIBCompliances,'dppsMIBCompliance':dppsMIBCompliance,'dppsMIBGroups':dppsMIBGroups,_O:dppsDimLedCfgGroup,_P:dppsShutdownCfgGroup,_Q:dppsIfEeeCfgGroup})