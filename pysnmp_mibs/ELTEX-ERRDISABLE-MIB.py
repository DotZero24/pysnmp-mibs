_I='eltexErrdisableIfStatusCause'
_H='read-only'
_G='eltexErrdisableConfigCause'
_F='Integer32'
_E='ELTEX-ERRDISABLE-MIB'
_D='ifIndex'
_C='IF-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltexLtd,=mibBuilder.importSymbols('ELTEX-SMI-ACTUAL','eltexLtd')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_C,'InterfaceIndexOrZero',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
eltexErrdisableMIB=ModuleIdentity((1,3,6,1,4,1,35265,53))
if mibBuilder.loadTexts:eltexErrdisableMIB.setRevisions(('2023-03-06 00:00',))
class EltexErrdisableCauseType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('storm-control',1),('loopback-detection',2),('udld',3),('port-security',4)))
_EltexErrdisableObjects_ObjectIdentity=ObjectIdentity
eltexErrdisableObjects=_EltexErrdisableObjects_ObjectIdentity((1,3,6,1,4,1,35265,53,1))
_EltexErrdisableGlobals_ObjectIdentity=ObjectIdentity
eltexErrdisableGlobals=_EltexErrdisableGlobals_ObjectIdentity((1,3,6,1,4,1,35265,53,1,1))
_EltexErrdisableReactivateInterface_Type=InterfaceIndexOrZero
_EltexErrdisableReactivateInterface_Object=MibScalar
eltexErrdisableReactivateInterface=_EltexErrdisableReactivateInterface_Object((1,3,6,1,4,1,35265,53,1,1,1),_EltexErrdisableReactivateInterface_Type())
eltexErrdisableReactivateInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErrdisableReactivateInterface.setStatus(_A)
class _EltexErrdisableGlobalRecoveryInterval_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,86400))
_EltexErrdisableGlobalRecoveryInterval_Type.__name__=_F
_EltexErrdisableGlobalRecoveryInterval_Object=MibScalar
eltexErrdisableGlobalRecoveryInterval=_EltexErrdisableGlobalRecoveryInterval_Object((1,3,6,1,4,1,35265,53,1,1,2),_EltexErrdisableGlobalRecoveryInterval_Type())
eltexErrdisableGlobalRecoveryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErrdisableGlobalRecoveryInterval.setStatus(_A)
if mibBuilder.loadTexts:eltexErrdisableGlobalRecoveryInterval.setUnits('seconds')
_EltexErrdisableConfigs_ObjectIdentity=ObjectIdentity
eltexErrdisableConfigs=_EltexErrdisableConfigs_ObjectIdentity((1,3,6,1,4,1,35265,53,1,2))
_EltexErrdisableConfigTable_Object=MibTable
eltexErrdisableConfigTable=_EltexErrdisableConfigTable_Object((1,3,6,1,4,1,35265,53,1,2,1))
if mibBuilder.loadTexts:eltexErrdisableConfigTable.setStatus(_A)
_EltexErrdisableConfigEntry_Object=MibTableRow
eltexErrdisableConfigEntry=_EltexErrdisableConfigEntry_Object((1,3,6,1,4,1,35265,53,1,2,1,1))
eltexErrdisableConfigEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:eltexErrdisableConfigEntry.setStatus(_A)
_EltexErrdisableConfigCause_Type=EltexErrdisableCauseType
_EltexErrdisableConfigCause_Object=MibTableColumn
eltexErrdisableConfigCause=_EltexErrdisableConfigCause_Object((1,3,6,1,4,1,35265,53,1,2,1,1,1),_EltexErrdisableConfigCause_Type())
eltexErrdisableConfigCause.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:eltexErrdisableConfigCause.setStatus(_A)
_EltexErrdisableConfigRecoveryEnable_Type=TruthValue
_EltexErrdisableConfigRecoveryEnable_Object=MibTableColumn
eltexErrdisableConfigRecoveryEnable=_EltexErrdisableConfigRecoveryEnable_Object((1,3,6,1,4,1,35265,53,1,2,1,1,2),_EltexErrdisableConfigRecoveryEnable_Type())
eltexErrdisableConfigRecoveryEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErrdisableConfigRecoveryEnable.setStatus(_A)
_EltexErrdisableConfigTrapEnable_Type=TruthValue
_EltexErrdisableConfigTrapEnable_Object=MibTableColumn
eltexErrdisableConfigTrapEnable=_EltexErrdisableConfigTrapEnable_Object((1,3,6,1,4,1,35265,53,1,2,1,1,3),_EltexErrdisableConfigTrapEnable_Type())
eltexErrdisableConfigTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexErrdisableConfigTrapEnable.setStatus(_A)
_EltexErrdisableStatistics_ObjectIdentity=ObjectIdentity
eltexErrdisableStatistics=_EltexErrdisableStatistics_ObjectIdentity((1,3,6,1,4,1,35265,53,1,3))
_EltexErrdisableIfStatusTable_Object=MibTable
eltexErrdisableIfStatusTable=_EltexErrdisableIfStatusTable_Object((1,3,6,1,4,1,35265,53,1,3,1))
if mibBuilder.loadTexts:eltexErrdisableIfStatusTable.setStatus(_A)
_EltexErrdisableIfStatusEntry_Object=MibTableRow
eltexErrdisableIfStatusEntry=_EltexErrdisableIfStatusEntry_Object((1,3,6,1,4,1,35265,53,1,3,1,1))
eltexErrdisableIfStatusEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:eltexErrdisableIfStatusEntry.setStatus(_A)
_EltexErrdisableIfStatusCause_Type=EltexErrdisableCauseType
_EltexErrdisableIfStatusCause_Object=MibTableColumn
eltexErrdisableIfStatusCause=_EltexErrdisableIfStatusCause_Object((1,3,6,1,4,1,35265,53,1,3,1,1,1),_EltexErrdisableIfStatusCause_Type())
eltexErrdisableIfStatusCause.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexErrdisableIfStatusCause.setStatus(_A)
_EltexErrdisableIfStatusRecoveryEnable_Type=TruthValue
_EltexErrdisableIfStatusRecoveryEnable_Object=MibTableColumn
eltexErrdisableIfStatusRecoveryEnable=_EltexErrdisableIfStatusRecoveryEnable_Object((1,3,6,1,4,1,35265,53,1,3,1,1,2),_EltexErrdisableIfStatusRecoveryEnable_Type())
eltexErrdisableIfStatusRecoveryEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexErrdisableIfStatusRecoveryEnable.setStatus(_A)
_EltexErrdisableNotifications_ObjectIdentity=ObjectIdentity
eltexErrdisableNotifications=_EltexErrdisableNotifications_ObjectIdentity((1,3,6,1,4,1,35265,53,2))
_EltexErrdisableNotificationsPrefix_ObjectIdentity=ObjectIdentity
eltexErrdisableNotificationsPrefix=_EltexErrdisableNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,35265,53,2,0))
eltexErrdisableIfSuspendedTrap=NotificationType((1,3,6,1,4,1,35265,53,2,0,1))
eltexErrdisableIfSuspendedTrap.setObjects(*((_C,_D),(_E,_I)))
if mibBuilder.loadTexts:eltexErrdisableIfSuspendedTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'EltexErrdisableCauseType':EltexErrdisableCauseType,'eltexErrdisableMIB':eltexErrdisableMIB,'eltexErrdisableObjects':eltexErrdisableObjects,'eltexErrdisableGlobals':eltexErrdisableGlobals,'eltexErrdisableReactivateInterface':eltexErrdisableReactivateInterface,'eltexErrdisableGlobalRecoveryInterval':eltexErrdisableGlobalRecoveryInterval,'eltexErrdisableConfigs':eltexErrdisableConfigs,'eltexErrdisableConfigTable':eltexErrdisableConfigTable,'eltexErrdisableConfigEntry':eltexErrdisableConfigEntry,_G:eltexErrdisableConfigCause,'eltexErrdisableConfigRecoveryEnable':eltexErrdisableConfigRecoveryEnable,'eltexErrdisableConfigTrapEnable':eltexErrdisableConfigTrapEnable,'eltexErrdisableStatistics':eltexErrdisableStatistics,'eltexErrdisableIfStatusTable':eltexErrdisableIfStatusTable,'eltexErrdisableIfStatusEntry':eltexErrdisableIfStatusEntry,_I:eltexErrdisableIfStatusCause,'eltexErrdisableIfStatusRecoveryEnable':eltexErrdisableIfStatusRecoveryEnable,'eltexErrdisableNotifications':eltexErrdisableNotifications,'eltexErrdisableNotificationsPrefix':eltexErrdisableNotificationsPrefix,'eltexErrdisableIfSuspendedTrap':eltexErrdisableIfSuspendedTrap})