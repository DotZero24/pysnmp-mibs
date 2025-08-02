_m='oaPortLosGroup'
_l='oaPortLosTrapParamsGroup'
_k='oaDevLosNotificationsGroup'
_j='oaDevLosMandatoryGroup'
_i='oaDevLosActivePortChanged'
_h='oaDevLosGrAgVid'
_g='oaDevLosGrAgAdminStatus'
_f='oaDevLosGrAgRMepStatus'
_e='oaDevLosGrToPrimaryTrapTimer'
_d='oaDevLosGrToBackupTrapTimer'
_c='oaDevLosGrPollDelayTimer'
_b='oaDevLosGrHoldOffTimer'
_a='oaDevLosGrWtrTimer'
_Z='oaDevLosGrMmuEnabled'
_Y='oaDevLosGrEnableMode'
_X='oaDevLosGrProtectionMode'
_W='oaDevLosAgSupport'
_V='oaDevLosGenSupport'
_U='oaDevLosGrAgRemoteMep'
_T='oaDevLosGrAgAssociationId'
_S='oaDevLosGrAgDomainId'
_R='supported'
_Q='notSupported'
_P='TruthValue'
_O='DisplayString'
_N='oaDevLosGrConnectionId'
_M='oaDevLosGrActionCause'
_L='oaDevLosGrActivePortNumber'
_K='oaDevLosGrSecondaryPort'
_J='oaDevLosGrPrimaryPort'
_I='not-accessible'
_H='oaDevLosGrId'
_G='seconds'
_F='Unsigned32'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='current'
_A='OA-DEV-LINK-PROTECTION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nbSwitchG1Il,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','nbSwitchG1Il')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_O,'PhysAddress','TextualConvention',_P)
oaDeviceLinkProtection=ModuleIdentity((1,3,6,1,4,1,629,1,50,11,1,24))
if mibBuilder.loadTexts:oaDeviceLinkProtection.setRevisions(('2020-06-16 00:00','2018-12-24 00:00','2016-07-13 00:00','2007-12-11 00:00','2007-08-02 00:00'))
_NbDeviceConfig_ObjectIdentity=ObjectIdentity
nbDeviceConfig=_NbDeviceConfig_ObjectIdentity((1,3,6,1,4,1,629,1,50,11))
_NbDevGen_ObjectIdentity=ObjectIdentity
nbDevGen=_NbDevGen_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1))
_OaDevLosNotifications_ObjectIdentity=ObjectIdentity
oaDevLosNotifications=_OaDevLosNotifications_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,24,0))
_OaDevLosGen_ObjectIdentity=ObjectIdentity
oaDevLosGen=_OaDevLosGen_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,24,1))
class _OaDevLosGenSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_OaDevLosGenSupport_Type.__name__=_C
_OaDevLosGenSupport_Object=MibScalar
oaDevLosGenSupport=_OaDevLosGenSupport_Object((1,3,6,1,4,1,629,1,50,11,1,24,1,1),_OaDevLosGenSupport_Type())
oaDevLosGenSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:oaDevLosGenSupport.setStatus(_B)
class _OaDevLosAgSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_OaDevLosAgSupport_Type.__name__=_C
_OaDevLosAgSupport_Object=MibScalar
oaDevLosAgSupport=_OaDevLosAgSupport_Object((1,3,6,1,4,1,629,1,50,11,1,24,1,2),_OaDevLosAgSupport_Type())
oaDevLosAgSupport.setMaxAccess(_E)
if mibBuilder.loadTexts:oaDevLosAgSupport.setStatus(_B)
_OaDevLosGrp_ObjectIdentity=ObjectIdentity
oaDevLosGrp=_OaDevLosGrp_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,24,2))
_OaDevLosGrTable_Object=MibTable
oaDevLosGrTable=_OaDevLosGrTable_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,5))
if mibBuilder.loadTexts:oaDevLosGrTable.setStatus(_B)
_OaDevLosGrEntry_Object=MibTableRow
oaDevLosGrEntry=_OaDevLosGrEntry_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,5,1))
oaDevLosGrEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:oaDevLosGrEntry.setStatus(_B)
class _OaDevLosGrId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OaDevLosGrId_Type.__name__=_C
_OaDevLosGrId_Object=MibTableColumn
oaDevLosGrId=_OaDevLosGrId_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,5,1,1),_OaDevLosGrId_Type())
oaDevLosGrId.setMaxAccess(_I)
if mibBuilder.loadTexts:oaDevLosGrId.setStatus(_B)
class _OaDevLosGrPrimaryPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_OaDevLosGrPrimaryPort_Type.__name__=_C
_OaDevLosGrPrimaryPort_Object=MibTableColumn
oaDevLosGrPrimaryPort=_OaDevLosGrPrimaryPort_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,5,1,2),_OaDevLosGrPrimaryPort_Type())
oaDevLosGrPrimaryPort.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevLosGrPrimaryPort.setStatus(_B)
class _OaDevLosGrSecondaryPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_OaDevLosGrSecondaryPort_Type.__name__=_C
_OaDevLosGrSecondaryPort_Object=MibTableColumn
oaDevLosGrSecondaryPort=_OaDevLosGrSecondaryPort_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,5,1,3),_OaDevLosGrSecondaryPort_Type())
oaDevLosGrSecondaryPort.setMaxAccess(_E)
if mibBuilder.loadTexts:oaDevLosGrSecondaryPort.setStatus(_B)
class _OaDevLosGrProtectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('preemption',2),('notPreemption',3)))
_OaDevLosGrProtectionMode_Type.__name__=_C
_OaDevLosGrProtectionMode_Object=MibTableColumn
oaDevLosGrProtectionMode=_OaDevLosGrProtectionMode_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,5,1,4),_OaDevLosGrProtectionMode_Type())
oaDevLosGrProtectionMode.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevLosGrProtectionMode.setStatus(_B)
class _OaDevLosGrEnableMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('enable',2),('disable',3)))
_OaDevLosGrEnableMode_Type.__name__=_C
_OaDevLosGrEnableMode_Object=MibTableColumn
oaDevLosGrEnableMode=_OaDevLosGrEnableMode_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,5,1,5),_OaDevLosGrEnableMode_Type())
oaDevLosGrEnableMode.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevLosGrEnableMode.setStatus(_B)
_OaDevLosGrActivePortNumber_Type=Integer32
_OaDevLosGrActivePortNumber_Object=MibTableColumn
oaDevLosGrActivePortNumber=_OaDevLosGrActivePortNumber_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,5,1,6),_OaDevLosGrActivePortNumber_Type())
oaDevLosGrActivePortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevLosGrActivePortNumber.setStatus(_B)
class _OaDevLosGrActionCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('noAction',1),('portLinkUp',2),('portLinkDown',3),('agRMepDiscardEvent',4),('agRMepNoConnEvent',5),('agRMepAliveEvent',6),('activePortAdminSet',7)))
_OaDevLosGrActionCause_Type.__name__=_C
_OaDevLosGrActionCause_Object=MibTableColumn
oaDevLosGrActionCause=_OaDevLosGrActionCause_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,5,1,7),_OaDevLosGrActionCause_Type())
oaDevLosGrActionCause.setMaxAccess(_E)
if mibBuilder.loadTexts:oaDevLosGrActionCause.setStatus(_B)
class _OaDevLosGrWtrTimer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_OaDevLosGrWtrTimer_Type.__name__=_C
_OaDevLosGrWtrTimer_Object=MibTableColumn
oaDevLosGrWtrTimer=_OaDevLosGrWtrTimer_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,5,1,8),_OaDevLosGrWtrTimer_Type())
oaDevLosGrWtrTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevLosGrWtrTimer.setStatus(_B)
if mibBuilder.loadTexts:oaDevLosGrWtrTimer.setUnits(_G)
class _OaDevLosGrConnectionId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_OaDevLosGrConnectionId_Type.__name__=_O
_OaDevLosGrConnectionId_Object=MibTableColumn
oaDevLosGrConnectionId=_OaDevLosGrConnectionId_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,5,1,9),_OaDevLosGrConnectionId_Type())
oaDevLosGrConnectionId.setMaxAccess(_E)
if mibBuilder.loadTexts:oaDevLosGrConnectionId.setStatus(_B)
class _OaDevLosGrHoldOffTimer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_OaDevLosGrHoldOffTimer_Type.__name__=_C
_OaDevLosGrHoldOffTimer_Object=MibTableColumn
oaDevLosGrHoldOffTimer=_OaDevLosGrHoldOffTimer_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,5,1,10),_OaDevLosGrHoldOffTimer_Type())
oaDevLosGrHoldOffTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevLosGrHoldOffTimer.setStatus(_B)
if mibBuilder.loadTexts:oaDevLosGrHoldOffTimer.setUnits(_G)
class _OaDevLosGrPollDelayTimer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_OaDevLosGrPollDelayTimer_Type.__name__=_C
_OaDevLosGrPollDelayTimer_Object=MibTableColumn
oaDevLosGrPollDelayTimer=_OaDevLosGrPollDelayTimer_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,5,1,11),_OaDevLosGrPollDelayTimer_Type())
oaDevLosGrPollDelayTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevLosGrPollDelayTimer.setStatus(_B)
if mibBuilder.loadTexts:oaDevLosGrPollDelayTimer.setUnits(_G)
class _OaDevLosGrToBackupTrapTimer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_OaDevLosGrToBackupTrapTimer_Type.__name__=_C
_OaDevLosGrToBackupTrapTimer_Object=MibTableColumn
oaDevLosGrToBackupTrapTimer=_OaDevLosGrToBackupTrapTimer_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,5,1,12),_OaDevLosGrToBackupTrapTimer_Type())
oaDevLosGrToBackupTrapTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevLosGrToBackupTrapTimer.setStatus(_B)
if mibBuilder.loadTexts:oaDevLosGrToBackupTrapTimer.setUnits(_G)
class _OaDevLosGrToPrimaryTrapTimer_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_OaDevLosGrToPrimaryTrapTimer_Type.__name__=_C
_OaDevLosGrToPrimaryTrapTimer_Object=MibTableColumn
oaDevLosGrToPrimaryTrapTimer=_OaDevLosGrToPrimaryTrapTimer_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,5,1,13),_OaDevLosGrToPrimaryTrapTimer_Type())
oaDevLosGrToPrimaryTrapTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevLosGrToPrimaryTrapTimer.setStatus(_B)
if mibBuilder.loadTexts:oaDevLosGrToPrimaryTrapTimer.setUnits(_G)
_OaDevLosGrAgTable_Object=MibTable
oaDevLosGrAgTable=_OaDevLosGrAgTable_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,7))
if mibBuilder.loadTexts:oaDevLosGrAgTable.setStatus(_B)
_OaDevLosGrAgEntry_Object=MibTableRow
oaDevLosGrAgEntry=_OaDevLosGrAgEntry_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,7,1))
oaDevLosGrAgEntry.setIndexNames((0,_A,_H),(0,_A,_S),(0,_A,_T),(0,_A,_U))
if mibBuilder.loadTexts:oaDevLosGrAgEntry.setStatus(_B)
class _OaDevLosGrAgDomainId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_OaDevLosGrAgDomainId_Type.__name__=_F
_OaDevLosGrAgDomainId_Object=MibTableColumn
oaDevLosGrAgDomainId=_OaDevLosGrAgDomainId_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,7,1,2),_OaDevLosGrAgDomainId_Type())
oaDevLosGrAgDomainId.setMaxAccess(_I)
if mibBuilder.loadTexts:oaDevLosGrAgDomainId.setStatus(_B)
class _OaDevLosGrAgAssociationId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_OaDevLosGrAgAssociationId_Type.__name__=_F
_OaDevLosGrAgAssociationId_Object=MibTableColumn
oaDevLosGrAgAssociationId=_OaDevLosGrAgAssociationId_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,7,1,3),_OaDevLosGrAgAssociationId_Type())
oaDevLosGrAgAssociationId.setMaxAccess(_I)
if mibBuilder.loadTexts:oaDevLosGrAgAssociationId.setStatus(_B)
class _OaDevLosGrAgRemoteMep_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8192))
_OaDevLosGrAgRemoteMep_Type.__name__=_F
_OaDevLosGrAgRemoteMep_Object=MibTableColumn
oaDevLosGrAgRemoteMep=_OaDevLosGrAgRemoteMep_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,7,1,4),_OaDevLosGrAgRemoteMep_Type())
oaDevLosGrAgRemoteMep.setMaxAccess(_I)
if mibBuilder.loadTexts:oaDevLosGrAgRemoteMep.setStatus(_B)
class _OaDevLosGrAgRMepStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('discard',2),('noConnection',3)))
_OaDevLosGrAgRMepStatus_Type.__name__=_C
_OaDevLosGrAgRMepStatus_Object=MibTableColumn
oaDevLosGrAgRMepStatus=_OaDevLosGrAgRMepStatus_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,7,1,8),_OaDevLosGrAgRMepStatus_Type())
oaDevLosGrAgRMepStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:oaDevLosGrAgRMepStatus.setStatus(_B)
class _OaDevLosGrAgAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_OaDevLosGrAgAdminStatus_Type.__name__=_C
_OaDevLosGrAgAdminStatus_Object=MibTableColumn
oaDevLosGrAgAdminStatus=_OaDevLosGrAgAdminStatus_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,7,1,10),_OaDevLosGrAgAdminStatus_Type())
oaDevLosGrAgAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevLosGrAgAdminStatus.setStatus(_B)
class _OaDevLosGrAgVid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8192))
_OaDevLosGrAgVid_Type.__name__=_F
_OaDevLosGrAgVid_Object=MibTableColumn
oaDevLosGrAgVid=_OaDevLosGrAgVid_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,7,1,11),_OaDevLosGrAgVid_Type())
oaDevLosGrAgVid.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevLosGrAgVid.setStatus(_B)
_OaDevLosGrMmuTable_Object=MibTable
oaDevLosGrMmuTable=_OaDevLosGrMmuTable_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,8))
if mibBuilder.loadTexts:oaDevLosGrMmuTable.setStatus(_B)
_OaDevLosGrMmuEntry_Object=MibTableRow
oaDevLosGrMmuEntry=_OaDevLosGrMmuEntry_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,8,1))
oaDevLosGrMmuEntry.setIndexNames((0,_A,_H))
if mibBuilder.loadTexts:oaDevLosGrMmuEntry.setStatus(_B)
class _OaDevLosGrMmuEnabled_Type(TruthValue):defaultValue=2
_OaDevLosGrMmuEnabled_Type.__name__=_P
_OaDevLosGrMmuEnabled_Object=MibTableColumn
oaDevLosGrMmuEnabled=_OaDevLosGrMmuEnabled_Object((1,3,6,1,4,1,629,1,50,11,1,24,2,8,1,2),_OaDevLosGrMmuEnabled_Type())
oaDevLosGrMmuEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDevLosGrMmuEnabled.setStatus(_B)
_OaDevLosConformance_ObjectIdentity=ObjectIdentity
oaDevLosConformance=_OaDevLosConformance_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,24,101))
_OaDevLosMIBCompliances_ObjectIdentity=ObjectIdentity
oaDevLosMIBCompliances=_OaDevLosMIBCompliances_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,24,101,1))
_OaDevLosMIBGroups_ObjectIdentity=ObjectIdentity
oaDevLosMIBGroups=_OaDevLosMIBGroups_ObjectIdentity((1,3,6,1,4,1,629,1,50,11,1,24,101,2))
oaDevLosMandatoryGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,11,1,24,101,2,1))
oaDevLosMandatoryGroup.setObjects(*((_A,_V),(_A,_W),(_A,_J),(_A,_K),(_A,_X),(_A,_Y),(_A,_L),(_A,_Z)))
if mibBuilder.loadTexts:oaDevLosMandatoryGroup.setStatus(_B)
oaPortLosTrapParamsGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,11,1,24,101,2,2))
oaPortLosTrapParamsGroup.setObjects(*((_A,_M),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_N)))
if mibBuilder.loadTexts:oaPortLosTrapParamsGroup.setStatus(_B)
oaPortLosGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,11,1,24,101,2,3))
oaPortLosGroup.setObjects(*((_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:oaPortLosGroup.setStatus(_B)
oaDevLosActivePortChanged=NotificationType((1,3,6,1,4,1,629,1,50,11,1,24,0,37))
oaDevLosActivePortChanged.setObjects(*((_A,_L),(_A,_J),(_A,_K),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:oaDevLosActivePortChanged.setStatus(_B)
oaDevLosNotificationsGroup=NotificationGroup((1,3,6,1,4,1,629,1,50,11,1,24,101,2,4))
oaDevLosNotificationsGroup.setObjects((_A,_i))
if mibBuilder.loadTexts:oaDevLosNotificationsGroup.setStatus(_B)
oaDevLosMIBCompliance=ModuleCompliance((1,3,6,1,4,1,629,1,50,11,1,24,101,1,1))
oaDevLosMIBCompliance.setObjects(*((_A,_j),(_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:oaDevLosMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'nbDeviceConfig':nbDeviceConfig,'nbDevGen':nbDevGen,'oaDeviceLinkProtection':oaDeviceLinkProtection,'oaDevLosNotifications':oaDevLosNotifications,_i:oaDevLosActivePortChanged,'oaDevLosGen':oaDevLosGen,_V:oaDevLosGenSupport,_W:oaDevLosAgSupport,'oaDevLosGrp':oaDevLosGrp,'oaDevLosGrTable':oaDevLosGrTable,'oaDevLosGrEntry':oaDevLosGrEntry,_H:oaDevLosGrId,_J:oaDevLosGrPrimaryPort,_K:oaDevLosGrSecondaryPort,_X:oaDevLosGrProtectionMode,_Y:oaDevLosGrEnableMode,_L:oaDevLosGrActivePortNumber,_M:oaDevLosGrActionCause,_a:oaDevLosGrWtrTimer,_N:oaDevLosGrConnectionId,_b:oaDevLosGrHoldOffTimer,_c:oaDevLosGrPollDelayTimer,_d:oaDevLosGrToBackupTrapTimer,_e:oaDevLosGrToPrimaryTrapTimer,'oaDevLosGrAgTable':oaDevLosGrAgTable,'oaDevLosGrAgEntry':oaDevLosGrAgEntry,_S:oaDevLosGrAgDomainId,_T:oaDevLosGrAgAssociationId,_U:oaDevLosGrAgRemoteMep,_f:oaDevLosGrAgRMepStatus,_g:oaDevLosGrAgAdminStatus,_h:oaDevLosGrAgVid,'oaDevLosGrMmuTable':oaDevLosGrMmuTable,'oaDevLosGrMmuEntry':oaDevLosGrMmuEntry,_Z:oaDevLosGrMmuEnabled,'oaDevLosConformance':oaDevLosConformance,'oaDevLosMIBCompliances':oaDevLosMIBCompliances,'oaDevLosMIBCompliance':oaDevLosMIBCompliance,'oaDevLosMIBGroups':oaDevLosMIBGroups,_j:oaDevLosMandatoryGroup,_l:oaPortLosTrapParamsGroup,_m:oaPortLosGroup,_k:oaDevLosNotificationsGroup})