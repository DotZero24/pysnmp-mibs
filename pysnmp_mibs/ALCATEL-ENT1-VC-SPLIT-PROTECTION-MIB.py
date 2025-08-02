_U='alaVCSPHelperGroup'
_T='alaVCSPConfigInfoGroup'
_S='alaVCSPNotificationGroup'
_R='alaVCSPRecoveryTrap'
_Q='alaVCSPProtectionTrap'
_P='alaVCSPHelperLinkaggRowStatus'
_O='alaVCSPHelperAdminState'
_N='alaVCSPAdminState'
_M='alaVCSPGuardTimer'
_L='alaVCSPUpTime'
_K='alaVCSPTableOperState'
_J='alaVCSPProtectionStateUpTime'
_I='alaVCSPLinkaggId'
_H='alaVCSPHelperLinkaggId'
_G='AlaVCSPState'
_F='read-write'
_E='Integer32'
_D='alaVCSPTableChassisID'
_C='read-only'
_B='ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alcatelIND1VirtualChassisMIBVCSP,=mibBuilder.importSymbols('ALCATEL-ENT1-VIRTUAL-CHASSIS-MIB','alcatelIND1VirtualChassisMIBVCSP')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
alaVCSPMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1))
if mibBuilder.loadTexts:alaVCSPMIB.setRevisions(('2013-10-14 00:00',))
class AlaVCSPChassisID(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
class AlaVCSPOpState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('protection',2),('inactive',3)))
class AlaVCSPState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AlaVCSPMIBNotifications_ObjectIdentity=ObjectIdentity
alaVCSPMIBNotifications=_AlaVCSPMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,0))
_AlaVCSPMIBObjects_ObjectIdentity=ObjectIdentity
alaVCSPMIBObjects=_AlaVCSPMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,1))
_AlaVCSPHelperGlobalConfig_ObjectIdentity=ObjectIdentity
alaVCSPHelperGlobalConfig=_AlaVCSPHelperGlobalConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,1,1))
class _AlaVCSPHelperAdminState_Type(AlaVCSPState):defaultValue=2
_AlaVCSPHelperAdminState_Type.__name__=_G
_AlaVCSPHelperAdminState_Object=MibScalar
alaVCSPHelperAdminState=_AlaVCSPHelperAdminState_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,1,1,1),_AlaVCSPHelperAdminState_Type())
alaVCSPHelperAdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVCSPHelperAdminState.setStatus(_A)
_AlaVCSPConfigInfo_ObjectIdentity=ObjectIdentity
alaVCSPConfigInfo=_AlaVCSPConfigInfo_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,1,2))
class _AlaVCSPAdminState_Type(AlaVCSPState):defaultValue=2
_AlaVCSPAdminState_Type.__name__=_G
_AlaVCSPAdminState_Object=MibScalar
alaVCSPAdminState=_AlaVCSPAdminState_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,1,2,1),_AlaVCSPAdminState_Type())
alaVCSPAdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVCSPAdminState.setStatus(_A)
class _AlaVCSPLinkaggId_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,128))
_AlaVCSPLinkaggId_Type.__name__=_E
_AlaVCSPLinkaggId_Object=MibScalar
alaVCSPLinkaggId=_AlaVCSPLinkaggId_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,1,2,2),_AlaVCSPLinkaggId_Type())
alaVCSPLinkaggId.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVCSPLinkaggId.setStatus(_A)
class _AlaVCSPGuardTimer_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,100))
_AlaVCSPGuardTimer_Type.__name__=_E
_AlaVCSPGuardTimer_Object=MibScalar
alaVCSPGuardTimer=_AlaVCSPGuardTimer_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,1,2,3),_AlaVCSPGuardTimer_Type())
alaVCSPGuardTimer.setMaxAccess(_F)
if mibBuilder.loadTexts:alaVCSPGuardTimer.setStatus(_A)
_AlaVCSPUpTime_Type=TimeTicks
_AlaVCSPUpTime_Object=MibScalar
alaVCSPUpTime=_AlaVCSPUpTime_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,1,2,4),_AlaVCSPUpTime_Type())
alaVCSPUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVCSPUpTime.setStatus(_A)
_AlaVCSPProtectionStateUpTime_Type=TimeTicks
_AlaVCSPProtectionStateUpTime_Object=MibScalar
alaVCSPProtectionStateUpTime=_AlaVCSPProtectionStateUpTime_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,1,2,5),_AlaVCSPProtectionStateUpTime_Type())
alaVCSPProtectionStateUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVCSPProtectionStateUpTime.setStatus(_A)
_AlaVCSPHelperLinkaggTable_Object=MibTable
alaVCSPHelperLinkaggTable=_AlaVCSPHelperLinkaggTable_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,1,3))
if mibBuilder.loadTexts:alaVCSPHelperLinkaggTable.setStatus(_A)
_AlaVCSPHelperLinkaggEntry_Object=MibTableRow
alaVCSPHelperLinkaggEntry=_AlaVCSPHelperLinkaggEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,1,3,1))
alaVCSPHelperLinkaggEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:alaVCSPHelperLinkaggEntry.setStatus(_A)
class _AlaVCSPHelperLinkaggId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AlaVCSPHelperLinkaggId_Type.__name__=_E
_AlaVCSPHelperLinkaggId_Object=MibTableColumn
alaVCSPHelperLinkaggId=_AlaVCSPHelperLinkaggId_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,1,3,1,1),_AlaVCSPHelperLinkaggId_Type())
alaVCSPHelperLinkaggId.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVCSPHelperLinkaggId.setStatus(_A)
_AlaVCSPHelperLinkaggRowStatus_Type=RowStatus
_AlaVCSPHelperLinkaggRowStatus_Object=MibTableColumn
alaVCSPHelperLinkaggRowStatus=_AlaVCSPHelperLinkaggRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,1,3,1,2),_AlaVCSPHelperLinkaggRowStatus_Type())
alaVCSPHelperLinkaggRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:alaVCSPHelperLinkaggRowStatus.setStatus(_A)
_AlaVCSPStateTable_Object=MibTable
alaVCSPStateTable=_AlaVCSPStateTable_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,1,4))
if mibBuilder.loadTexts:alaVCSPStateTable.setStatus(_A)
_AlaVCSPStateEntry_Object=MibTableRow
alaVCSPStateEntry=_AlaVCSPStateEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,1,4,1))
alaVCSPStateEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:alaVCSPStateEntry.setStatus(_A)
_AlaVCSPTableChassisID_Type=AlaVCSPChassisID
_AlaVCSPTableChassisID_Object=MibTableColumn
alaVCSPTableChassisID=_AlaVCSPTableChassisID_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,1,4,1,1),_AlaVCSPTableChassisID_Type())
alaVCSPTableChassisID.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVCSPTableChassisID.setStatus(_A)
_AlaVCSPTableOperState_Type=AlaVCSPOpState
_AlaVCSPTableOperState_Object=MibTableColumn
alaVCSPTableOperState=_AlaVCSPTableOperState_Object((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,1,4,1,2),_AlaVCSPTableOperState_Type())
alaVCSPTableOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:alaVCSPTableOperState.setStatus(_A)
_AlaVCSPMIBConformance_ObjectIdentity=ObjectIdentity
alaVCSPMIBConformance=_AlaVCSPMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,2))
_AlaVCSPMIBGroups_ObjectIdentity=ObjectIdentity
alaVCSPMIBGroups=_AlaVCSPMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,2,1))
_AlaVCSPMIBCompliances_ObjectIdentity=ObjectIdentity
alaVCSPMIBCompliances=_AlaVCSPMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,2,2))
alaVCSPConfigInfoGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,2,1,2))
alaVCSPConfigInfoGroup.setObjects(*((_B,_I),(_B,_J),(_B,_D),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:alaVCSPConfigInfoGroup.setStatus(_A)
alaVCSPHelperGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,2,1,3))
alaVCSPHelperGroup.setObjects(*((_B,_O),(_B,_H),(_B,_P)))
if mibBuilder.loadTexts:alaVCSPHelperGroup.setStatus(_A)
alaVCSPProtectionTrap=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,0,1))
alaVCSPProtectionTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:alaVCSPProtectionTrap.setStatus(_A)
alaVCSPRecoveryTrap=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,0,2))
alaVCSPRecoveryTrap.setObjects((_B,_D))
if mibBuilder.loadTexts:alaVCSPRecoveryTrap.setStatus(_A)
alaVCSPNotificationGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,2,1,1))
alaVCSPNotificationGroup.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:alaVCSPNotificationGroup.setStatus(_A)
alaVCSPMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,69,1,3,1,2,2,1))
alaVCSPMIBCompliance.setObjects(*((_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:alaVCSPMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AlaVCSPChassisID':AlaVCSPChassisID,'AlaVCSPOpState':AlaVCSPOpState,_G:AlaVCSPState,'alaVCSPMIB':alaVCSPMIB,'alaVCSPMIBNotifications':alaVCSPMIBNotifications,_Q:alaVCSPProtectionTrap,_R:alaVCSPRecoveryTrap,'alaVCSPMIBObjects':alaVCSPMIBObjects,'alaVCSPHelperGlobalConfig':alaVCSPHelperGlobalConfig,_O:alaVCSPHelperAdminState,'alaVCSPConfigInfo':alaVCSPConfigInfo,_N:alaVCSPAdminState,_I:alaVCSPLinkaggId,_M:alaVCSPGuardTimer,_L:alaVCSPUpTime,_J:alaVCSPProtectionStateUpTime,'alaVCSPHelperLinkaggTable':alaVCSPHelperLinkaggTable,'alaVCSPHelperLinkaggEntry':alaVCSPHelperLinkaggEntry,_H:alaVCSPHelperLinkaggId,_P:alaVCSPHelperLinkaggRowStatus,'alaVCSPStateTable':alaVCSPStateTable,'alaVCSPStateEntry':alaVCSPStateEntry,_D:alaVCSPTableChassisID,_K:alaVCSPTableOperState,'alaVCSPMIBConformance':alaVCSPMIBConformance,'alaVCSPMIBGroups':alaVCSPMIBGroups,_S:alaVCSPNotificationGroup,_T:alaVCSPConfigInfoGroup,_U:alaVCSPHelperGroup,'alaVCSPMIBCompliances':alaVCSPMIBCompliances,'alaVCSPMIBCompliance':alaVCSPMIBCompliance})