_F='Integer32'
_E='read-only'
_D='minutes'
_C='read-write'
_B='UPS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
clabCommonMibs,=mibBuilder.importSymbols('CLAB-DEF-MIB','clabCommonMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
clabUpsMib=ModuleIdentity((1,3,6,1,4,1,4491,4,1))
if mibBuilder.loadTexts:clabUpsMib.setRevisions(('2018-01-18 00:00','2010-04-28 00:00','2009-05-06 00:00','2007-01-19 17:00','2005-01-28 00:00'))
_ClabUpsNotifications_ObjectIdentity=ObjectIdentity
clabUpsNotifications=_ClabUpsNotifications_ObjectIdentity((1,3,6,1,4,1,4491,4,1,0))
_ClabUpsObjects_ObjectIdentity=ObjectIdentity
clabUpsObjects=_ClabUpsObjects_ObjectIdentity((1,3,6,1,4,1,4491,4,1,1))
_ClabSupplemtalGroup_ObjectIdentity=ObjectIdentity
clabSupplemtalGroup=_ClabSupplemtalGroup_ObjectIdentity((1,3,6,1,4,1,4491,4,1,1,1))
class _MtaDevPwrSupplyBatteryTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disableAutoTesting',1),('testScheduled',2),('testInProgress',3),('testPending',4)))
_MtaDevPwrSupplyBatteryTest_Type.__name__=_F
_MtaDevPwrSupplyBatteryTest_Object=MibScalar
mtaDevPwrSupplyBatteryTest=_MtaDevPwrSupplyBatteryTest_Object((1,3,6,1,4,1,4491,4,1,1,1,1),_MtaDevPwrSupplyBatteryTest_Type())
mtaDevPwrSupplyBatteryTest.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaDevPwrSupplyBatteryTest.setStatus(_A)
_MtaDevPwrSupplyConfigRunTime_Type=Integer32
_MtaDevPwrSupplyConfigRunTime_Object=MibScalar
mtaDevPwrSupplyConfigRunTime=_MtaDevPwrSupplyConfigRunTime_Object((1,3,6,1,4,1,4491,4,1,1,1,2),_MtaDevPwrSupplyConfigRunTime_Type())
mtaDevPwrSupplyConfigRunTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaDevPwrSupplyConfigRunTime.setStatus(_A)
if mibBuilder.loadTexts:mtaDevPwrSupplyConfigRunTime.setUnits(_D)
_MtaDevPwrSupplyRatedMinutes_Type=Integer32
_MtaDevPwrSupplyRatedMinutes_Object=MibScalar
mtaDevPwrSupplyRatedMinutes=_MtaDevPwrSupplyRatedMinutes_Object((1,3,6,1,4,1,4491,4,1,1,1,3),_MtaDevPwrSupplyRatedMinutes_Type())
mtaDevPwrSupplyRatedMinutes.setMaxAccess(_E)
if mibBuilder.loadTexts:mtaDevPwrSupplyRatedMinutes.setStatus(_A)
if mibBuilder.loadTexts:mtaDevPwrSupplyRatedMinutes.setUnits(_D)
_MtaDevPwrSupplyAvailableMinutes_Type=Integer32
_MtaDevPwrSupplyAvailableMinutes_Object=MibScalar
mtaDevPwrSupplyAvailableMinutes=_MtaDevPwrSupplyAvailableMinutes_Object((1,3,6,1,4,1,4491,4,1,1,1,4),_MtaDevPwrSupplyAvailableMinutes_Type())
mtaDevPwrSupplyAvailableMinutes.setMaxAccess(_E)
if mibBuilder.loadTexts:mtaDevPwrSupplyAvailableMinutes.setStatus(_A)
if mibBuilder.loadTexts:mtaDevPwrSupplyAvailableMinutes.setUnits(_D)
_MtaDevPwrSupplyConfigReplaceBatteryTime_Type=Integer32
_MtaDevPwrSupplyConfigReplaceBatteryTime_Object=MibScalar
mtaDevPwrSupplyConfigReplaceBatteryTime=_MtaDevPwrSupplyConfigReplaceBatteryTime_Object((1,3,6,1,4,1,4491,4,1,1,1,5),_MtaDevPwrSupplyConfigReplaceBatteryTime_Type())
mtaDevPwrSupplyConfigReplaceBatteryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaDevPwrSupplyConfigReplaceBatteryTime.setStatus(_A)
if mibBuilder.loadTexts:mtaDevPwrSupplyConfigReplaceBatteryTime.setUnits(_D)
_MtaDevPwrSupplyFullChargeTime_Type=Integer32
_MtaDevPwrSupplyFullChargeTime_Object=MibScalar
mtaDevPwrSupplyFullChargeTime=_MtaDevPwrSupplyFullChargeTime_Object((1,3,6,1,4,1,4491,4,1,1,1,6),_MtaDevPwrSupplyFullChargeTime_Type())
mtaDevPwrSupplyFullChargeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mtaDevPwrSupplyFullChargeTime.setStatus(_A)
_MtaDevPwrSupplyBatteryTestTime_Type=Integer32
_MtaDevPwrSupplyBatteryTestTime_Object=MibScalar
mtaDevPwrSupplyBatteryTestTime=_MtaDevPwrSupplyBatteryTestTime_Object((1,3,6,1,4,1,4491,4,1,1,1,7),_MtaDevPwrSupplyBatteryTestTime_Type())
mtaDevPwrSupplyBatteryTestTime.setMaxAccess(_E)
if mibBuilder.loadTexts:mtaDevPwrSupplyBatteryTestTime.setStatus(_A)
_ClabUpsConformance_ObjectIdentity=ObjectIdentity
clabUpsConformance=_ClabUpsConformance_ObjectIdentity((1,3,6,1,4,1,4491,4,1,2))
_ClabUpsCompliances_ObjectIdentity=ObjectIdentity
clabUpsCompliances=_ClabUpsCompliances_ObjectIdentity((1,3,6,1,4,1,4491,4,1,2,1))
_ClabUpsGroups_ObjectIdentity=ObjectIdentity
clabUpsGroups=_ClabUpsGroups_ObjectIdentity((1,3,6,1,4,1,4491,4,1,2,2))
clabUpsMibCompliance=ModuleCompliance((1,3,6,1,4,1,4491,4,1,2,2,1))
clabUpsMibCompliance.setObjects(*((_B,'upsSubsetIdentGroup'),(_B,'upsFullBatteryGroup'),(_B,'upsBasicInputGroup'),(_B,'upsBasicOutputGroup'),(_B,'upsBasicAlarmGroup'),(_B,'upsBasicControlGroup'),(_B,'upsBasicConfigGroup')))
if mibBuilder.loadTexts:clabUpsMibCompliance.setStatus(_A)
mibBuilder.exportSymbols('CLAB-UPS-MIB',**{'clabUpsMib':clabUpsMib,'clabUpsNotifications':clabUpsNotifications,'clabUpsObjects':clabUpsObjects,'clabSupplemtalGroup':clabSupplemtalGroup,'mtaDevPwrSupplyBatteryTest':mtaDevPwrSupplyBatteryTest,'mtaDevPwrSupplyConfigRunTime':mtaDevPwrSupplyConfigRunTime,'mtaDevPwrSupplyRatedMinutes':mtaDevPwrSupplyRatedMinutes,'mtaDevPwrSupplyAvailableMinutes':mtaDevPwrSupplyAvailableMinutes,'mtaDevPwrSupplyConfigReplaceBatteryTime':mtaDevPwrSupplyConfigReplaceBatteryTime,'mtaDevPwrSupplyFullChargeTime':mtaDevPwrSupplyFullChargeTime,'mtaDevPwrSupplyBatteryTestTime':mtaDevPwrSupplyBatteryTestTime,'clabUpsConformance':clabUpsConformance,'clabUpsCompliances':clabUpsCompliances,'clabUpsGroups':clabUpsGroups,'clabUpsMibCompliance':clabUpsMibCompliance})