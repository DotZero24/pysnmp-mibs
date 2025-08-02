_f='etsysLinkFlapInterfaceGroup'
_e='etsysLinkFlapSystemGroup'
_d='etsysLinkFlapViolation'
_c='etsysLinkFlapIntfLinkFlapViolations'
_b='etsysLinkFlapIntfCurrentElapsed'
_a='etsysLinkFlapIntfLinkdownCountTotal'
_Z='etsysLinkFlapIntfLinkdownCountCurrent'
_Y='etsysLinkFlapIntfDownTime'
_X='etsysLinkFlapIntfTimeInterval'
_W='etsysLinkFlapIntfCountThreshold'
_V='etsysLinkFlapIntfClearStats'
_U='etsysLinkFlapIntfAction'
_T='etsysLinkFlapIntfEnabledStatus'
_S='etsysLinkFlapSystemLinkFlapMaximum'
_R='etsysLinkFlapSystemSupportedActions'
_Q='etsysLinkFlapSystemState'
_P='disabled'
_O='TruthValue'
_N='EnabledStatus'
_M='ifName'
_L='ifIndex'
_K='etsysLinkFlapIntfOperStatus'
_J='seconds'
_I='link state transitions'
_H='LinkFlapIntfAction'
_G='Integer32'
_F='IF-MIB'
_E='Unsigned32'
_D='read-only'
_C='read-write'
_B='ENTERASYS-LINK-FLAP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ifIndex,ifName=mibBuilder.importSymbols(_F,_L,_M)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_O)
etsysLinkFlapMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,52))
if mibBuilder.loadTexts:etsysLinkFlapMIB.setRevisions(('2009-10-16 12:53','2004-08-20 14:47'))
class LinkFlapIntfAction(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('disableInterface',0),('generateSyslogEntry',1),('generateNotification',2)))
_EtsysLinkFlapObjects_ObjectIdentity=ObjectIdentity
etsysLinkFlapObjects=_EtsysLinkFlapObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,52,1))
_EtsysLinkFlapNotificationBranch_ObjectIdentity=ObjectIdentity
etsysLinkFlapNotificationBranch=_EtsysLinkFlapNotificationBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,52,1,0))
_EtsysLinkFlapSystemBranch_ObjectIdentity=ObjectIdentity
etsysLinkFlapSystemBranch=_EtsysLinkFlapSystemBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,52,1,1))
class _EtsysLinkFlapSystemState_Type(EnabledStatus):defaultValue=2
_EtsysLinkFlapSystemState_Type.__name__=_N
_EtsysLinkFlapSystemState_Object=MibScalar
etsysLinkFlapSystemState=_EtsysLinkFlapSystemState_Object((1,3,6,1,4,1,5624,1,2,52,1,1,1),_EtsysLinkFlapSystemState_Type())
etsysLinkFlapSystemState.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysLinkFlapSystemState.setStatus(_A)
class _EtsysLinkFlapSystemSupportedActions_Type(LinkFlapIntfAction):defaultBinValue='111'
_EtsysLinkFlapSystemSupportedActions_Type.__name__=_H
_EtsysLinkFlapSystemSupportedActions_Object=MibScalar
etsysLinkFlapSystemSupportedActions=_EtsysLinkFlapSystemSupportedActions_Object((1,3,6,1,4,1,5624,1,2,52,1,1,2),_EtsysLinkFlapSystemSupportedActions_Type())
etsysLinkFlapSystemSupportedActions.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysLinkFlapSystemSupportedActions.setStatus(_A)
_EtsysLinkFlapSystemLinkFlapMaximum_Type=Unsigned32
_EtsysLinkFlapSystemLinkFlapMaximum_Object=MibScalar
etsysLinkFlapSystemLinkFlapMaximum=_EtsysLinkFlapSystemLinkFlapMaximum_Object((1,3,6,1,4,1,5624,1,2,52,1,1,3),_EtsysLinkFlapSystemLinkFlapMaximum_Type())
etsysLinkFlapSystemLinkFlapMaximum.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysLinkFlapSystemLinkFlapMaximum.setStatus(_A)
_EtsysLinkFlapInterfaceBranch_ObjectIdentity=ObjectIdentity
etsysLinkFlapInterfaceBranch=_EtsysLinkFlapInterfaceBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,52,1,2))
_EtsysLinkFlapInterfaceTable_Object=MibTable
etsysLinkFlapInterfaceTable=_EtsysLinkFlapInterfaceTable_Object((1,3,6,1,4,1,5624,1,2,52,1,2,1))
if mibBuilder.loadTexts:etsysLinkFlapInterfaceTable.setStatus(_A)
_EtsysLinkFlapInterfaceEntry_Object=MibTableRow
etsysLinkFlapInterfaceEntry=_EtsysLinkFlapInterfaceEntry_Object((1,3,6,1,4,1,5624,1,2,52,1,2,1,1))
etsysLinkFlapInterfaceEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:etsysLinkFlapInterfaceEntry.setStatus(_A)
class _EtsysLinkFlapIntfEnabledStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_P,2)))
_EtsysLinkFlapIntfEnabledStatus_Type.__name__=_G
_EtsysLinkFlapIntfEnabledStatus_Object=MibTableColumn
etsysLinkFlapIntfEnabledStatus=_EtsysLinkFlapIntfEnabledStatus_Object((1,3,6,1,4,1,5624,1,2,52,1,2,1,1,1),_EtsysLinkFlapIntfEnabledStatus_Type())
etsysLinkFlapIntfEnabledStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysLinkFlapIntfEnabledStatus.setStatus(_A)
class _EtsysLinkFlapIntfAction_Type(LinkFlapIntfAction):defaultBinValue='011'
_EtsysLinkFlapIntfAction_Type.__name__=_H
_EtsysLinkFlapIntfAction_Object=MibTableColumn
etsysLinkFlapIntfAction=_EtsysLinkFlapIntfAction_Object((1,3,6,1,4,1,5624,1,2,52,1,2,1,1,2),_EtsysLinkFlapIntfAction_Type())
etsysLinkFlapIntfAction.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysLinkFlapIntfAction.setStatus(_A)
class _EtsysLinkFlapIntfOperStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('operational',1),(_P,2)))
_EtsysLinkFlapIntfOperStatus_Type.__name__=_G
_EtsysLinkFlapIntfOperStatus_Object=MibTableColumn
etsysLinkFlapIntfOperStatus=_EtsysLinkFlapIntfOperStatus_Object((1,3,6,1,4,1,5624,1,2,52,1,2,1,1,3),_EtsysLinkFlapIntfOperStatus_Type())
etsysLinkFlapIntfOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysLinkFlapIntfOperStatus.setStatus(_A)
class _EtsysLinkFlapIntfClearStats_Type(TruthValue):defaultValue=2
_EtsysLinkFlapIntfClearStats_Type.__name__=_O
_EtsysLinkFlapIntfClearStats_Object=MibTableColumn
etsysLinkFlapIntfClearStats=_EtsysLinkFlapIntfClearStats_Object((1,3,6,1,4,1,5624,1,2,52,1,2,1,1,4),_EtsysLinkFlapIntfClearStats_Type())
etsysLinkFlapIntfClearStats.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysLinkFlapIntfClearStats.setStatus(_A)
class _EtsysLinkFlapIntfCountThreshold_Type(Unsigned32):defaultValue=5
_EtsysLinkFlapIntfCountThreshold_Type.__name__=_E
_EtsysLinkFlapIntfCountThreshold_Object=MibTableColumn
etsysLinkFlapIntfCountThreshold=_EtsysLinkFlapIntfCountThreshold_Object((1,3,6,1,4,1,5624,1,2,52,1,2,1,1,5),_EtsysLinkFlapIntfCountThreshold_Type())
etsysLinkFlapIntfCountThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysLinkFlapIntfCountThreshold.setStatus(_A)
if mibBuilder.loadTexts:etsysLinkFlapIntfCountThreshold.setUnits(_I)
class _EtsysLinkFlapIntfTimeInterval_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
_EtsysLinkFlapIntfTimeInterval_Type.__name__=_E
_EtsysLinkFlapIntfTimeInterval_Object=MibTableColumn
etsysLinkFlapIntfTimeInterval=_EtsysLinkFlapIntfTimeInterval_Object((1,3,6,1,4,1,5624,1,2,52,1,2,1,1,6),_EtsysLinkFlapIntfTimeInterval_Type())
etsysLinkFlapIntfTimeInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysLinkFlapIntfTimeInterval.setStatus(_A)
if mibBuilder.loadTexts:etsysLinkFlapIntfTimeInterval.setUnits(_J)
class _EtsysLinkFlapIntfDownTime_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
_EtsysLinkFlapIntfDownTime_Type.__name__=_E
_EtsysLinkFlapIntfDownTime_Object=MibTableColumn
etsysLinkFlapIntfDownTime=_EtsysLinkFlapIntfDownTime_Object((1,3,6,1,4,1,5624,1,2,52,1,2,1,1,7),_EtsysLinkFlapIntfDownTime_Type())
etsysLinkFlapIntfDownTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysLinkFlapIntfDownTime.setStatus(_A)
if mibBuilder.loadTexts:etsysLinkFlapIntfDownTime.setUnits(_J)
_EtsysLinkFlapIntfLinkdownCountCurrent_Type=Gauge32
_EtsysLinkFlapIntfLinkdownCountCurrent_Object=MibTableColumn
etsysLinkFlapIntfLinkdownCountCurrent=_EtsysLinkFlapIntfLinkdownCountCurrent_Object((1,3,6,1,4,1,5624,1,2,52,1,2,1,1,8),_EtsysLinkFlapIntfLinkdownCountCurrent_Type())
etsysLinkFlapIntfLinkdownCountCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysLinkFlapIntfLinkdownCountCurrent.setStatus(_A)
if mibBuilder.loadTexts:etsysLinkFlapIntfLinkdownCountCurrent.setUnits(_I)
_EtsysLinkFlapIntfLinkdownCountTotal_Type=Gauge32
_EtsysLinkFlapIntfLinkdownCountTotal_Object=MibTableColumn
etsysLinkFlapIntfLinkdownCountTotal=_EtsysLinkFlapIntfLinkdownCountTotal_Object((1,3,6,1,4,1,5624,1,2,52,1,2,1,1,9),_EtsysLinkFlapIntfLinkdownCountTotal_Type())
etsysLinkFlapIntfLinkdownCountTotal.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysLinkFlapIntfLinkdownCountTotal.setStatus(_A)
if mibBuilder.loadTexts:etsysLinkFlapIntfLinkdownCountTotal.setUnits(_I)
_EtsysLinkFlapIntfCurrentElapsed_Type=Unsigned32
_EtsysLinkFlapIntfCurrentElapsed_Object=MibTableColumn
etsysLinkFlapIntfCurrentElapsed=_EtsysLinkFlapIntfCurrentElapsed_Object((1,3,6,1,4,1,5624,1,2,52,1,2,1,1,10),_EtsysLinkFlapIntfCurrentElapsed_Type())
etsysLinkFlapIntfCurrentElapsed.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysLinkFlapIntfCurrentElapsed.setStatus(_A)
if mibBuilder.loadTexts:etsysLinkFlapIntfCurrentElapsed.setUnits(_J)
_EtsysLinkFlapIntfLinkFlapViolations_Type=Gauge32
_EtsysLinkFlapIntfLinkFlapViolations_Object=MibTableColumn
etsysLinkFlapIntfLinkFlapViolations=_EtsysLinkFlapIntfLinkFlapViolations_Object((1,3,6,1,4,1,5624,1,2,52,1,2,1,1,11),_EtsysLinkFlapIntfLinkFlapViolations_Type())
etsysLinkFlapIntfLinkFlapViolations.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysLinkFlapIntfLinkFlapViolations.setStatus(_A)
if mibBuilder.loadTexts:etsysLinkFlapIntfLinkFlapViolations.setUnits('violations')
_EtsysLinkFlapConformance_ObjectIdentity=ObjectIdentity
etsysLinkFlapConformance=_EtsysLinkFlapConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,52,2))
_EtsysLinkFlapGroups_ObjectIdentity=ObjectIdentity
etsysLinkFlapGroups=_EtsysLinkFlapGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,52,2,1))
_EtsysLinkFlapCompliances_ObjectIdentity=ObjectIdentity
etsysLinkFlapCompliances=_EtsysLinkFlapCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,52,2,2))
etsysLinkFlapSystemGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,52,2,1,1))
etsysLinkFlapSystemGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:etsysLinkFlapSystemGroup.setStatus(_A)
etsysLinkFlapInterfaceGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,52,2,1,2))
etsysLinkFlapInterfaceGroup.setObjects(*((_B,_T),(_B,_U),(_B,_K),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:etsysLinkFlapInterfaceGroup.setStatus(_A)
etsysLinkFlapViolation=NotificationType((1,3,6,1,4,1,5624,1,2,52,1,0,1))
etsysLinkFlapViolation.setObjects(*((_F,_M),(_B,_K)))
if mibBuilder.loadTexts:etsysLinkFlapViolation.setStatus(_A)
etsysLinkFlapNotificationGroup=NotificationGroup((1,3,6,1,4,1,5624,1,2,52,2,1,3))
etsysLinkFlapNotificationGroup.setObjects((_B,_d))
if mibBuilder.loadTexts:etsysLinkFlapNotificationGroup.setStatus(_A)
etsysLinkFlapCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,52,2,2,1))
etsysLinkFlapCompliance.setObjects(*((_B,_e),(_B,_f)))
if mibBuilder.loadTexts:etsysLinkFlapCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_H:LinkFlapIntfAction,'etsysLinkFlapMIB':etsysLinkFlapMIB,'etsysLinkFlapObjects':etsysLinkFlapObjects,'etsysLinkFlapNotificationBranch':etsysLinkFlapNotificationBranch,_d:etsysLinkFlapViolation,'etsysLinkFlapSystemBranch':etsysLinkFlapSystemBranch,_Q:etsysLinkFlapSystemState,_R:etsysLinkFlapSystemSupportedActions,_S:etsysLinkFlapSystemLinkFlapMaximum,'etsysLinkFlapInterfaceBranch':etsysLinkFlapInterfaceBranch,'etsysLinkFlapInterfaceTable':etsysLinkFlapInterfaceTable,'etsysLinkFlapInterfaceEntry':etsysLinkFlapInterfaceEntry,_T:etsysLinkFlapIntfEnabledStatus,_U:etsysLinkFlapIntfAction,_K:etsysLinkFlapIntfOperStatus,_V:etsysLinkFlapIntfClearStats,_W:etsysLinkFlapIntfCountThreshold,_X:etsysLinkFlapIntfTimeInterval,_Y:etsysLinkFlapIntfDownTime,_Z:etsysLinkFlapIntfLinkdownCountCurrent,_a:etsysLinkFlapIntfLinkdownCountTotal,_b:etsysLinkFlapIntfCurrentElapsed,_c:etsysLinkFlapIntfLinkFlapViolations,'etsysLinkFlapConformance':etsysLinkFlapConformance,'etsysLinkFlapGroups':etsysLinkFlapGroups,_e:etsysLinkFlapSystemGroup,_f:etsysLinkFlapInterfaceGroup,'etsysLinkFlapNotificationGroup':etsysLinkFlapNotificationGroup,'etsysLinkFlapCompliances':etsysLinkFlapCompliances,'etsysLinkFlapCompliance':etsysLinkFlapCompliance})