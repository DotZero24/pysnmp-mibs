_j='cHsrpGrpGroupSup'
_i='deprecated'
_h='cHsrpStateChange'
_g='cHsrpGrpIpNone'
_f='cHsrpGrpEntryRowStatus'
_e='cHsrpGrpVirtualMacAddr'
_d='cHsrpGrpStandbyRouter'
_c='cHsrpGrpActiveRouter'
_b='cHsrpGrpUseConfigVirtualIpAddr'
_a='cHsrpGrpVirtualIpAddr'
_Z='cHsrpGrpLearnedHoldTime'
_Y='cHsrpGrpLearnedHelloTime'
_X='cHsrpGrpConfiguredHoldTime'
_W='cHsrpGrpConfiguredHelloTime'
_V='cHsrpGrpUseConfiguredTimers'
_U='cHsrpGrpPreemptDelay'
_T='cHsrpGrpPreempt'
_S='cHsrpGrpPriority'
_R='cHsrpGrpAuth'
_Q='cHsrpConfigTimeout'
_P='cHsrpGrpNumber'
_O='DisplayString'
_N='IpAddress'
_M='ifIndex'
_L='IF-MIB'
_K='cHsrpNotificationsGroup'
_J='cHsrpGrpStandbyState'
_I='TruthValue'
_H='cHsrpGrpGroup'
_G='cHsrpConfigGroup'
_F='milliseconds'
_E='read-only'
_D='read-create'
_C='Unsigned32'
_B='current'
_A='CISCO-HSRP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_L,_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32',_N,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_O,'MacAddress','PhysAddress','RowStatus','TextualConvention',_I)
ciscoHsrpMIB=ModuleIdentity((1,3,6,1,4,1,9,9,106))
if mibBuilder.loadTexts:ciscoHsrpMIB.setRevisions(('2010-09-06 00:00','2005-12-20 00:00','1998-08-03 00:00'))
class HsrpState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('initial',1),('learn',2),('listen',3),('speak',4),('standby',5),('active',6)))
_CiscoHsrpMIBObjects_ObjectIdentity=ObjectIdentity
ciscoHsrpMIBObjects=_CiscoHsrpMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,106,1))
_CHsrpGlobalConfig_ObjectIdentity=ObjectIdentity
cHsrpGlobalConfig=_CHsrpGlobalConfig_ObjectIdentity((1,3,6,1,4,1,9,9,106,1,1))
class _CHsrpConfigTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_CHsrpConfigTimeout_Type.__name__=_C
_CHsrpConfigTimeout_Object=MibScalar
cHsrpConfigTimeout=_CHsrpConfigTimeout_Object((1,3,6,1,4,1,9,9,106,1,1,1),_CHsrpConfigTimeout_Type())
cHsrpConfigTimeout.setMaxAccess('read-write')
if mibBuilder.loadTexts:cHsrpConfigTimeout.setStatus(_B)
if mibBuilder.loadTexts:cHsrpConfigTimeout.setUnits('minutes')
_CHsrpGroup_ObjectIdentity=ObjectIdentity
cHsrpGroup=_CHsrpGroup_ObjectIdentity((1,3,6,1,4,1,9,9,106,1,2))
_CHsrpGrpTable_Object=MibTable
cHsrpGrpTable=_CHsrpGrpTable_Object((1,3,6,1,4,1,9,9,106,1,2,1))
if mibBuilder.loadTexts:cHsrpGrpTable.setStatus(_B)
_CHsrpGrpEntry_Object=MibTableRow
cHsrpGrpEntry=_CHsrpGrpEntry_Object((1,3,6,1,4,1,9,9,106,1,2,1,1))
cHsrpGrpEntry.setIndexNames((0,_L,_M),(0,_A,_P))
if mibBuilder.loadTexts:cHsrpGrpEntry.setStatus(_B)
class _CHsrpGrpNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CHsrpGrpNumber_Type.__name__=_C
_CHsrpGrpNumber_Object=MibTableColumn
cHsrpGrpNumber=_CHsrpGrpNumber_Object((1,3,6,1,4,1,9,9,106,1,2,1,1,1),_CHsrpGrpNumber_Type())
cHsrpGrpNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cHsrpGrpNumber.setStatus(_B)
class _CHsrpGrpAuth_Type(DisplayString):defaultValue=OctetString('cisco');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_CHsrpGrpAuth_Type.__name__=_O
_CHsrpGrpAuth_Object=MibTableColumn
cHsrpGrpAuth=_CHsrpGrpAuth_Object((1,3,6,1,4,1,9,9,106,1,2,1,1,2),_CHsrpGrpAuth_Type())
cHsrpGrpAuth.setMaxAccess(_D)
if mibBuilder.loadTexts:cHsrpGrpAuth.setStatus(_B)
class _CHsrpGrpPriority_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CHsrpGrpPriority_Type.__name__=_C
_CHsrpGrpPriority_Object=MibTableColumn
cHsrpGrpPriority=_CHsrpGrpPriority_Object((1,3,6,1,4,1,9,9,106,1,2,1,1,3),_CHsrpGrpPriority_Type())
cHsrpGrpPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:cHsrpGrpPriority.setStatus(_B)
class _CHsrpGrpPreempt_Type(TruthValue):defaultValue=2
_CHsrpGrpPreempt_Type.__name__=_I
_CHsrpGrpPreempt_Object=MibTableColumn
cHsrpGrpPreempt=_CHsrpGrpPreempt_Object((1,3,6,1,4,1,9,9,106,1,2,1,1,4),_CHsrpGrpPreempt_Type())
cHsrpGrpPreempt.setMaxAccess(_D)
if mibBuilder.loadTexts:cHsrpGrpPreempt.setStatus(_B)
class _CHsrpGrpPreemptDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_CHsrpGrpPreemptDelay_Type.__name__=_C
_CHsrpGrpPreemptDelay_Object=MibTableColumn
cHsrpGrpPreemptDelay=_CHsrpGrpPreemptDelay_Object((1,3,6,1,4,1,9,9,106,1,2,1,1,5),_CHsrpGrpPreemptDelay_Type())
cHsrpGrpPreemptDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:cHsrpGrpPreemptDelay.setStatus(_B)
if mibBuilder.loadTexts:cHsrpGrpPreemptDelay.setUnits('seconds')
_CHsrpGrpUseConfiguredTimers_Type=TruthValue
_CHsrpGrpUseConfiguredTimers_Object=MibTableColumn
cHsrpGrpUseConfiguredTimers=_CHsrpGrpUseConfiguredTimers_Object((1,3,6,1,4,1,9,9,106,1,2,1,1,6),_CHsrpGrpUseConfiguredTimers_Type())
cHsrpGrpUseConfiguredTimers.setMaxAccess(_E)
if mibBuilder.loadTexts:cHsrpGrpUseConfiguredTimers.setStatus(_B)
class _CHsrpGrpConfiguredHelloTime_Type(Unsigned32):defaultValue=3000
_CHsrpGrpConfiguredHelloTime_Type.__name__=_C
_CHsrpGrpConfiguredHelloTime_Object=MibTableColumn
cHsrpGrpConfiguredHelloTime=_CHsrpGrpConfiguredHelloTime_Object((1,3,6,1,4,1,9,9,106,1,2,1,1,7),_CHsrpGrpConfiguredHelloTime_Type())
cHsrpGrpConfiguredHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cHsrpGrpConfiguredHelloTime.setStatus(_B)
if mibBuilder.loadTexts:cHsrpGrpConfiguredHelloTime.setUnits(_F)
class _CHsrpGrpConfiguredHoldTime_Type(Unsigned32):defaultValue=10000
_CHsrpGrpConfiguredHoldTime_Type.__name__=_C
_CHsrpGrpConfiguredHoldTime_Object=MibTableColumn
cHsrpGrpConfiguredHoldTime=_CHsrpGrpConfiguredHoldTime_Object((1,3,6,1,4,1,9,9,106,1,2,1,1,8),_CHsrpGrpConfiguredHoldTime_Type())
cHsrpGrpConfiguredHoldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cHsrpGrpConfiguredHoldTime.setStatus(_B)
if mibBuilder.loadTexts:cHsrpGrpConfiguredHoldTime.setUnits(_F)
class _CHsrpGrpLearnedHelloTime_Type(Unsigned32):defaultValue=3000
_CHsrpGrpLearnedHelloTime_Type.__name__=_C
_CHsrpGrpLearnedHelloTime_Object=MibTableColumn
cHsrpGrpLearnedHelloTime=_CHsrpGrpLearnedHelloTime_Object((1,3,6,1,4,1,9,9,106,1,2,1,1,9),_CHsrpGrpLearnedHelloTime_Type())
cHsrpGrpLearnedHelloTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cHsrpGrpLearnedHelloTime.setStatus(_B)
if mibBuilder.loadTexts:cHsrpGrpLearnedHelloTime.setUnits(_F)
class _CHsrpGrpLearnedHoldTime_Type(Unsigned32):defaultValue=10000
_CHsrpGrpLearnedHoldTime_Type.__name__=_C
_CHsrpGrpLearnedHoldTime_Object=MibTableColumn
cHsrpGrpLearnedHoldTime=_CHsrpGrpLearnedHoldTime_Object((1,3,6,1,4,1,9,9,106,1,2,1,1,10),_CHsrpGrpLearnedHoldTime_Type())
cHsrpGrpLearnedHoldTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cHsrpGrpLearnedHoldTime.setStatus(_B)
if mibBuilder.loadTexts:cHsrpGrpLearnedHoldTime.setUnits(_F)
class _CHsrpGrpVirtualIpAddr_Type(IpAddress):defaultHexValue='00000000'
_CHsrpGrpVirtualIpAddr_Type.__name__=_N
_CHsrpGrpVirtualIpAddr_Object=MibTableColumn
cHsrpGrpVirtualIpAddr=_CHsrpGrpVirtualIpAddr_Object((1,3,6,1,4,1,9,9,106,1,2,1,1,11),_CHsrpGrpVirtualIpAddr_Type())
cHsrpGrpVirtualIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cHsrpGrpVirtualIpAddr.setStatus(_B)
_CHsrpGrpUseConfigVirtualIpAddr_Type=TruthValue
_CHsrpGrpUseConfigVirtualIpAddr_Object=MibTableColumn
cHsrpGrpUseConfigVirtualIpAddr=_CHsrpGrpUseConfigVirtualIpAddr_Object((1,3,6,1,4,1,9,9,106,1,2,1,1,12),_CHsrpGrpUseConfigVirtualIpAddr_Type())
cHsrpGrpUseConfigVirtualIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cHsrpGrpUseConfigVirtualIpAddr.setStatus(_B)
_CHsrpGrpActiveRouter_Type=IpAddress
_CHsrpGrpActiveRouter_Object=MibTableColumn
cHsrpGrpActiveRouter=_CHsrpGrpActiveRouter_Object((1,3,6,1,4,1,9,9,106,1,2,1,1,13),_CHsrpGrpActiveRouter_Type())
cHsrpGrpActiveRouter.setMaxAccess(_E)
if mibBuilder.loadTexts:cHsrpGrpActiveRouter.setStatus(_B)
_CHsrpGrpStandbyRouter_Type=IpAddress
_CHsrpGrpStandbyRouter_Object=MibTableColumn
cHsrpGrpStandbyRouter=_CHsrpGrpStandbyRouter_Object((1,3,6,1,4,1,9,9,106,1,2,1,1,14),_CHsrpGrpStandbyRouter_Type())
cHsrpGrpStandbyRouter.setMaxAccess(_E)
if mibBuilder.loadTexts:cHsrpGrpStandbyRouter.setStatus(_B)
_CHsrpGrpStandbyState_Type=HsrpState
_CHsrpGrpStandbyState_Object=MibTableColumn
cHsrpGrpStandbyState=_CHsrpGrpStandbyState_Object((1,3,6,1,4,1,9,9,106,1,2,1,1,15),_CHsrpGrpStandbyState_Type())
cHsrpGrpStandbyState.setMaxAccess(_E)
if mibBuilder.loadTexts:cHsrpGrpStandbyState.setStatus(_B)
_CHsrpGrpVirtualMacAddr_Type=MacAddress
_CHsrpGrpVirtualMacAddr_Object=MibTableColumn
cHsrpGrpVirtualMacAddr=_CHsrpGrpVirtualMacAddr_Object((1,3,6,1,4,1,9,9,106,1,2,1,1,16),_CHsrpGrpVirtualMacAddr_Type())
cHsrpGrpVirtualMacAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cHsrpGrpVirtualMacAddr.setStatus(_B)
_CHsrpGrpEntryRowStatus_Type=RowStatus
_CHsrpGrpEntryRowStatus_Object=MibTableColumn
cHsrpGrpEntryRowStatus=_CHsrpGrpEntryRowStatus_Object((1,3,6,1,4,1,9,9,106,1,2,1,1,17),_CHsrpGrpEntryRowStatus_Type())
cHsrpGrpEntryRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cHsrpGrpEntryRowStatus.setStatus(_B)
class _CHsrpGrpIpNone_Type(TruthValue):defaultValue=2
_CHsrpGrpIpNone_Type.__name__=_I
_CHsrpGrpIpNone_Object=MibTableColumn
cHsrpGrpIpNone=_CHsrpGrpIpNone_Object((1,3,6,1,4,1,9,9,106,1,2,1,1,18),_CHsrpGrpIpNone_Type())
cHsrpGrpIpNone.setMaxAccess(_D)
if mibBuilder.loadTexts:cHsrpGrpIpNone.setStatus(_B)
_CHsrpMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cHsrpMIBNotificationPrefix=_CHsrpMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,106,2))
_CHsrpMIBNotifications_ObjectIdentity=ObjectIdentity
cHsrpMIBNotifications=_CHsrpMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,106,2,0))
_CHsrpConformance_ObjectIdentity=ObjectIdentity
cHsrpConformance=_CHsrpConformance_ObjectIdentity((1,3,6,1,4,1,9,9,106,3))
_CHsrpCompliances_ObjectIdentity=ObjectIdentity
cHsrpCompliances=_CHsrpCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,106,3,1))
_CHsrpComplianceGroups_ObjectIdentity=ObjectIdentity
cHsrpComplianceGroups=_CHsrpComplianceGroups_ObjectIdentity((1,3,6,1,4,1,9,9,106,3,2))
cHsrpConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,106,3,2,1))
cHsrpConfigGroup.setObjects((_A,_Q))
if mibBuilder.loadTexts:cHsrpConfigGroup.setStatus(_B)
cHsrpGrpGroup=ObjectGroup((1,3,6,1,4,1,9,9,106,3,2,2))
cHsrpGrpGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_J),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:cHsrpGrpGroup.setStatus(_B)
cHsrpGrpGroupSup=ObjectGroup((1,3,6,1,4,1,9,9,106,3,2,4))
cHsrpGrpGroupSup.setObjects((_A,_g))
if mibBuilder.loadTexts:cHsrpGrpGroupSup.setStatus(_B)
cHsrpStateChange=NotificationType((1,3,6,1,4,1,9,9,106,2,0,1))
cHsrpStateChange.setObjects((_A,_J))
if mibBuilder.loadTexts:cHsrpStateChange.setStatus(_B)
cHsrpNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,106,3,2,3))
cHsrpNotificationsGroup.setObjects((_A,_h))
if mibBuilder.loadTexts:cHsrpNotificationsGroup.setStatus(_B)
cHsrpCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,106,3,1,1))
cHsrpCompliance.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:cHsrpCompliance.setStatus(_i)
cHsrpComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,106,3,1,2))
cHsrpComplianceRev1.setObjects(*((_A,_G),(_A,_H),(_A,_K)))
if mibBuilder.loadTexts:cHsrpComplianceRev1.setStatus(_i)
cHsrpComplianceRev2=ModuleCompliance((1,3,6,1,4,1,9,9,106,3,1,3))
cHsrpComplianceRev2.setObjects(*((_A,_G),(_A,_H),(_A,_j),(_A,_K)))
if mibBuilder.loadTexts:cHsrpComplianceRev2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'HsrpState':HsrpState,'ciscoHsrpMIB':ciscoHsrpMIB,'ciscoHsrpMIBObjects':ciscoHsrpMIBObjects,'cHsrpGlobalConfig':cHsrpGlobalConfig,_Q:cHsrpConfigTimeout,'cHsrpGroup':cHsrpGroup,'cHsrpGrpTable':cHsrpGrpTable,'cHsrpGrpEntry':cHsrpGrpEntry,_P:cHsrpGrpNumber,_R:cHsrpGrpAuth,_S:cHsrpGrpPriority,_T:cHsrpGrpPreempt,_U:cHsrpGrpPreemptDelay,_V:cHsrpGrpUseConfiguredTimers,_W:cHsrpGrpConfiguredHelloTime,_X:cHsrpGrpConfiguredHoldTime,_Y:cHsrpGrpLearnedHelloTime,_Z:cHsrpGrpLearnedHoldTime,_a:cHsrpGrpVirtualIpAddr,_b:cHsrpGrpUseConfigVirtualIpAddr,_c:cHsrpGrpActiveRouter,_d:cHsrpGrpStandbyRouter,_J:cHsrpGrpStandbyState,_e:cHsrpGrpVirtualMacAddr,_f:cHsrpGrpEntryRowStatus,_g:cHsrpGrpIpNone,'cHsrpMIBNotificationPrefix':cHsrpMIBNotificationPrefix,'cHsrpMIBNotifications':cHsrpMIBNotifications,_h:cHsrpStateChange,'cHsrpConformance':cHsrpConformance,'cHsrpCompliances':cHsrpCompliances,'cHsrpCompliance':cHsrpCompliance,'cHsrpComplianceRev1':cHsrpComplianceRev1,'cHsrpComplianceRev2':cHsrpComplianceRev2,'cHsrpComplianceGroups':cHsrpComplianceGroups,_G:cHsrpConfigGroup,_H:cHsrpGrpGroup,_K:cHsrpNotificationsGroup,_j:cHsrpGrpGroupSup})