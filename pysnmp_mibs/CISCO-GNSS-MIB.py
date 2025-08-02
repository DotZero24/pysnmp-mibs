_P='ciscoGnssMIBNotificationGroup'
_O='ciscoGnssMIBMainObjectGroup'
_N='ciscoGnssModuleLockStatus'
_M='OpenCircuitAlarmStatus'
_L='ShortCircuitAlarmStatus'
_K='GnssSvVisibilityStatus'
_J='cGnssSatelliteVisibilityStatus'
_I='cGnssModuleOCAlarmStatus'
_H='cGnssModuleSCAlarmStatus'
_G='cGnssModulePresenceStatus'
_F='cGnssModuleLockStatus'
_E='read-only'
_D='cGnssModuleSlotState'
_C='cGnssModuleSlotInfo'
_B='current'
_A='CISCO-GNSS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoGnssMIB=ModuleIdentity((1,3,6,1,4,1,9,9,862))
if mibBuilder.loadTexts:ciscoGnssMIB.setRevisions(('2019-05-22 00:00',))
class OpenCircuitAlarmStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('raise',1),('clear',2)))
class ShortCircuitAlarmStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('raise',1),('clear',2)))
class SVCnt(TextualConvention,Integer32):status=_B
class GnssSvVisibilityStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bad',1),('good',2)))
class SlotState(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
class SlotInfo(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
class GnssModuleLockStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
class GnssModulePresenceStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('absent',1),('present',2)))
_CiscoGnssMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoGnssMIBNotifs=_CiscoGnssMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,862,0))
_CiscoGnssMIBObjects_ObjectIdentity=ObjectIdentity
ciscoGnssMIBObjects=_CiscoGnssMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,862,1))
_CGnssModuleLockStatus_Type=GnssModuleLockStatus
_CGnssModuleLockStatus_Object=MibScalar
cGnssModuleLockStatus=_CGnssModuleLockStatus_Object((1,3,6,1,4,1,9,9,862,1,1),_CGnssModuleLockStatus_Type())
cGnssModuleLockStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cGnssModuleLockStatus.setStatus(_B)
_CGnssModulePresenceStatus_Type=GnssModulePresenceStatus
_CGnssModulePresenceStatus_Object=MibScalar
cGnssModulePresenceStatus=_CGnssModulePresenceStatus_Object((1,3,6,1,4,1,9,9,862,1,2),_CGnssModulePresenceStatus_Type())
cGnssModulePresenceStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cGnssModulePresenceStatus.setStatus(_B)
_CGnssModuleSlotInfo_Type=SlotInfo
_CGnssModuleSlotInfo_Object=MibScalar
cGnssModuleSlotInfo=_CGnssModuleSlotInfo_Object((1,3,6,1,4,1,9,9,862,1,3),_CGnssModuleSlotInfo_Type())
cGnssModuleSlotInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:cGnssModuleSlotInfo.setStatus(_B)
_CGnssModuleSlotState_Type=SlotState
_CGnssModuleSlotState_Object=MibScalar
cGnssModuleSlotState=_CGnssModuleSlotState_Object((1,3,6,1,4,1,9,9,862,1,4),_CGnssModuleSlotState_Type())
cGnssModuleSlotState.setMaxAccess(_E)
if mibBuilder.loadTexts:cGnssModuleSlotState.setStatus(_B)
class _CGnssSatelliteVisibilityStatus_Type(GnssSvVisibilityStatus):defaultValue=2
_CGnssSatelliteVisibilityStatus_Type.__name__=_K
_CGnssSatelliteVisibilityStatus_Object=MibScalar
cGnssSatelliteVisibilityStatus=_CGnssSatelliteVisibilityStatus_Object((1,3,6,1,4,1,9,9,862,1,5),_CGnssSatelliteVisibilityStatus_Type())
cGnssSatelliteVisibilityStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cGnssSatelliteVisibilityStatus.setStatus(_B)
class _CGnssModuleSatelliteCount_Type(SVCnt):defaultValue=0
_CGnssModuleSatelliteCount_Type.__name__='SVCnt'
_CGnssModuleSatelliteCount_Object=MibScalar
cGnssModuleSatelliteCount=_CGnssModuleSatelliteCount_Object((1,3,6,1,4,1,9,9,862,1,6),_CGnssModuleSatelliteCount_Type())
cGnssModuleSatelliteCount.setMaxAccess(_E)
if mibBuilder.loadTexts:cGnssModuleSatelliteCount.setStatus(_B)
_CGnssModuleSvIdSNR_Type=DisplayString
_CGnssModuleSvIdSNR_Object=MibScalar
cGnssModuleSvIdSNR=_CGnssModuleSvIdSNR_Object((1,3,6,1,4,1,9,9,862,1,7),_CGnssModuleSvIdSNR_Type())
cGnssModuleSvIdSNR.setMaxAccess(_E)
if mibBuilder.loadTexts:cGnssModuleSvIdSNR.setStatus(_B)
class _CGnssModuleSCAlarmStatus_Type(ShortCircuitAlarmStatus):defaultValue=2
_CGnssModuleSCAlarmStatus_Type.__name__=_L
_CGnssModuleSCAlarmStatus_Object=MibScalar
cGnssModuleSCAlarmStatus=_CGnssModuleSCAlarmStatus_Object((1,3,6,1,4,1,9,9,862,1,8),_CGnssModuleSCAlarmStatus_Type())
cGnssModuleSCAlarmStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cGnssModuleSCAlarmStatus.setStatus(_B)
class _CGnssModuleOCAlarmStatus_Type(OpenCircuitAlarmStatus):defaultValue=2
_CGnssModuleOCAlarmStatus_Type.__name__=_M
_CGnssModuleOCAlarmStatus_Object=MibScalar
cGnssModuleOCAlarmStatus=_CGnssModuleOCAlarmStatus_Object((1,3,6,1,4,1,9,9,862,1,9),_CGnssModuleOCAlarmStatus_Type())
cGnssModuleOCAlarmStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cGnssModuleOCAlarmStatus.setStatus(_B)
_CiscoGnssMIBConform_ObjectIdentity=ObjectIdentity
ciscoGnssMIBConform=_CiscoGnssMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,862,2))
_CiscoGnssMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoGnssMIBCompliances=_CiscoGnssMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,862,2,1))
_CiscoGnssMIBGroups_ObjectIdentity=ObjectIdentity
ciscoGnssMIBGroups=_CiscoGnssMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,862,2,2))
ciscoGnssMIBMainObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,862,2,2,1))
ciscoGnssMIBMainObjectGroup.setObjects((_A,_F))
if mibBuilder.loadTexts:ciscoGnssMIBMainObjectGroup.setStatus(_B)
ciscoGnssModuleLockStatus=NotificationType((1,3,6,1,4,1,9,9,862,0,1))
ciscoGnssModuleLockStatus.setObjects(*((_A,_F),(_A,_C),(_A,_D)))
if mibBuilder.loadTexts:ciscoGnssModuleLockStatus.setStatus(_B)
ciscoGnssModuleLockClear=NotificationType((1,3,6,1,4,1,9,9,862,0,2))
ciscoGnssModuleLockClear.setObjects(*((_A,_F),(_A,_C),(_A,_D)))
if mibBuilder.loadTexts:ciscoGnssModuleLockClear.setStatus(_B)
ciscoGnssModulePresenceStatus=NotificationType((1,3,6,1,4,1,9,9,862,0,3))
ciscoGnssModulePresenceStatus.setObjects(*((_A,_G),(_A,_C),(_A,_D)))
if mibBuilder.loadTexts:ciscoGnssModulePresenceStatus.setStatus(_B)
ciscoGnssModulePresenceClear=NotificationType((1,3,6,1,4,1,9,9,862,0,4))
ciscoGnssModulePresenceClear.setObjects(*((_A,_G),(_A,_C),(_A,_D)))
if mibBuilder.loadTexts:ciscoGnssModulePresenceClear.setStatus(_B)
ciscoGnssAntennaSCAlarmStatus=NotificationType((1,3,6,1,4,1,9,9,862,0,5))
ciscoGnssAntennaSCAlarmStatus.setObjects(*((_A,_H),(_A,_C),(_A,_D)))
if mibBuilder.loadTexts:ciscoGnssAntennaSCAlarmStatus.setStatus(_B)
ciscoGnssAntennaSCAlarmClear=NotificationType((1,3,6,1,4,1,9,9,862,0,6))
ciscoGnssAntennaSCAlarmClear.setObjects(*((_A,_H),(_A,_C),(_A,_D)))
if mibBuilder.loadTexts:ciscoGnssAntennaSCAlarmClear.setStatus(_B)
ciscoGnssAntennaOCAlarmStatus=NotificationType((1,3,6,1,4,1,9,9,862,0,7))
ciscoGnssAntennaOCAlarmStatus.setObjects(*((_A,_C),(_A,_D),(_A,_I)))
if mibBuilder.loadTexts:ciscoGnssAntennaOCAlarmStatus.setStatus(_B)
ciscoGnssAntennaOCAlarmClear=NotificationType((1,3,6,1,4,1,9,9,862,0,8))
ciscoGnssAntennaOCAlarmClear.setObjects(*((_A,_C),(_A,_D),(_A,_I)))
if mibBuilder.loadTexts:ciscoGnssAntennaOCAlarmClear.setStatus(_B)
ciscoGnssSatelliteVisibilityStatus=NotificationType((1,3,6,1,4,1,9,9,862,0,9))
ciscoGnssSatelliteVisibilityStatus.setObjects(*((_A,_J),(_A,_C),(_A,_D)))
if mibBuilder.loadTexts:ciscoGnssSatelliteVisibilityStatus.setStatus(_B)
ciscoGnssSatelliteVisibilityClear=NotificationType((1,3,6,1,4,1,9,9,862,0,10))
ciscoGnssSatelliteVisibilityClear.setObjects(*((_A,_C),(_A,_D),(_A,_J)))
if mibBuilder.loadTexts:ciscoGnssSatelliteVisibilityClear.setStatus(_B)
ciscoGnssMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,862,2,2,2))
ciscoGnssMIBNotificationGroup.setObjects((_A,_N))
if mibBuilder.loadTexts:ciscoGnssMIBNotificationGroup.setStatus(_B)
ciscoGnssMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,862,2,1,1))
ciscoGnssMIBCompliance.setObjects(*((_A,_O),(_A,_P)))
if mibBuilder.loadTexts:ciscoGnssMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_M:OpenCircuitAlarmStatus,_L:ShortCircuitAlarmStatus,'SVCnt':SVCnt,_K:GnssSvVisibilityStatus,'SlotState':SlotState,'SlotInfo':SlotInfo,'GnssModuleLockStatus':GnssModuleLockStatus,'GnssModulePresenceStatus':GnssModulePresenceStatus,'ciscoGnssMIB':ciscoGnssMIB,'ciscoGnssMIBNotifs':ciscoGnssMIBNotifs,_N:ciscoGnssModuleLockStatus,'ciscoGnssModuleLockClear':ciscoGnssModuleLockClear,'ciscoGnssModulePresenceStatus':ciscoGnssModulePresenceStatus,'ciscoGnssModulePresenceClear':ciscoGnssModulePresenceClear,'ciscoGnssAntennaSCAlarmStatus':ciscoGnssAntennaSCAlarmStatus,'ciscoGnssAntennaSCAlarmClear':ciscoGnssAntennaSCAlarmClear,'ciscoGnssAntennaOCAlarmStatus':ciscoGnssAntennaOCAlarmStatus,'ciscoGnssAntennaOCAlarmClear':ciscoGnssAntennaOCAlarmClear,'ciscoGnssSatelliteVisibilityStatus':ciscoGnssSatelliteVisibilityStatus,'ciscoGnssSatelliteVisibilityClear':ciscoGnssSatelliteVisibilityClear,'ciscoGnssMIBObjects':ciscoGnssMIBObjects,_F:cGnssModuleLockStatus,_G:cGnssModulePresenceStatus,_C:cGnssModuleSlotInfo,_D:cGnssModuleSlotState,_J:cGnssSatelliteVisibilityStatus,'cGnssModuleSatelliteCount':cGnssModuleSatelliteCount,'cGnssModuleSvIdSNR':cGnssModuleSvIdSNR,_H:cGnssModuleSCAlarmStatus,_I:cGnssModuleOCAlarmStatus,'ciscoGnssMIBConform':ciscoGnssMIBConform,'ciscoGnssMIBCompliances':ciscoGnssMIBCompliances,'ciscoGnssMIBCompliance':ciscoGnssMIBCompliance,'ciscoGnssMIBGroups':ciscoGnssMIBGroups,_O:ciscoGnssMIBMainObjectGroup,_P:ciscoGnssMIBNotificationGroup})