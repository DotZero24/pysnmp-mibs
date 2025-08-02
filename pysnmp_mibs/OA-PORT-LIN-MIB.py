_f='oaPortLinGroup'
_e='oaPortLinTrapParamsGroup'
_d='oaPortLinNotificationsGroup'
_c='oaPortLinMandatoryGroup'
_b='oaPortLinStateDown'
_a='oaPortLinStateUp'
_Z='oaPortLinAgAdminStatus'
_Y='oaPortLinAgRMepStatus'
_X='oaPortLinLastError'
_W='oaPortLinSymmetricStatus'
_V='oaPortLinAdminStatus'
_U='oaPortLinOperStatus'
_T='oaPortLinAgSupport'
_S='oaPortLinGenSupport'
_R='oaPortLinAgRemoteMep'
_Q='oaPortLinAgAssociationId'
_P='oaPortLinAgDomainId'
_O='invalid'
_N='supported'
_M='notSupported'
_L='DisplayString'
_K='OctetString'
_J='oaPortLinId'
_I='oaPortLinActionCause'
_H='oaPortLinSlavePorts'
_G='read-write'
_F='not-accessible'
_E='Unsigned32'
_D='read-only'
_C='Integer32'
_B='current'
_A='OA-PORT-LIN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nbSwitchG1Il,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','nbSwitchG1Il')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','TextualConvention')
nbPortLinkReflection=ModuleIdentity((1,3,6,1,4,1,629,1,50,10,11))
if mibBuilder.loadTexts:nbPortLinkReflection.setRevisions(('2011-03-16 00:00','2010-11-02 00:00','2007-12-11 00:00','2007-08-02 00:00'))
_NbPortParams_ObjectIdentity=ObjectIdentity
nbPortParams=_NbPortParams_ObjectIdentity((1,3,6,1,4,1,629,1,50,10))
_OaPortLinNotifications_ObjectIdentity=ObjectIdentity
oaPortLinNotifications=_OaPortLinNotifications_ObjectIdentity((1,3,6,1,4,1,629,1,50,10,11,0))
_OaPortLinGen_ObjectIdentity=ObjectIdentity
oaPortLinGen=_OaPortLinGen_ObjectIdentity((1,3,6,1,4,1,629,1,50,10,11,1))
class _OaPortLinGenSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_OaPortLinGenSupport_Type.__name__=_C
_OaPortLinGenSupport_Object=MibScalar
oaPortLinGenSupport=_OaPortLinGenSupport_Object((1,3,6,1,4,1,629,1,50,10,11,1,1),_OaPortLinGenSupport_Type())
oaPortLinGenSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:oaPortLinGenSupport.setStatus(_B)
class _OaPortLinAgSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_OaPortLinAgSupport_Type.__name__=_C
_OaPortLinAgSupport_Object=MibScalar
oaPortLinAgSupport=_OaPortLinAgSupport_Object((1,3,6,1,4,1,629,1,50,10,11,1,2),_OaPortLinAgSupport_Type())
oaPortLinAgSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:oaPortLinAgSupport.setStatus(_B)
class _OaPortLinLastError_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,160))
_OaPortLinLastError_Type.__name__=_L
_OaPortLinLastError_Object=MibScalar
oaPortLinLastError=_OaPortLinLastError_Object((1,3,6,1,4,1,629,1,50,10,11,1,3),_OaPortLinLastError_Type())
oaPortLinLastError.setMaxAccess(_D)
if mibBuilder.loadTexts:oaPortLinLastError.setStatus(_B)
_OaPortLinGrp_ObjectIdentity=ObjectIdentity
oaPortLinGrp=_OaPortLinGrp_ObjectIdentity((1,3,6,1,4,1,629,1,50,10,11,2))
_OaPortLinTable_Object=MibTable
oaPortLinTable=_OaPortLinTable_Object((1,3,6,1,4,1,629,1,50,10,11,2,1))
if mibBuilder.loadTexts:oaPortLinTable.setStatus(_B)
_OaPortLinEntry_Object=MibTableRow
oaPortLinEntry=_OaPortLinEntry_Object((1,3,6,1,4,1,629,1,50,10,11,2,1,1))
oaPortLinEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:oaPortLinEntry.setStatus(_B)
class _OaPortLinId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OaPortLinId_Type.__name__=_C
_OaPortLinId_Object=MibTableColumn
oaPortLinId=_OaPortLinId_Object((1,3,6,1,4,1,629,1,50,10,11,2,1,1,1),_OaPortLinId_Type())
oaPortLinId.setMaxAccess(_F)
if mibBuilder.loadTexts:oaPortLinId.setStatus(_B)
class _OaPortLinOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('master',2),('slave',3)))
_OaPortLinOperStatus_Type.__name__=_C
_OaPortLinOperStatus_Object=MibTableColumn
oaPortLinOperStatus=_OaPortLinOperStatus_Object((1,3,6,1,4,1,629,1,50,10,11,2,1,1,2),_OaPortLinOperStatus_Type())
oaPortLinOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:oaPortLinOperStatus.setStatus(_B)
class _OaPortLinAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_O,2)))
_OaPortLinAdminStatus_Type.__name__=_C
_OaPortLinAdminStatus_Object=MibTableColumn
oaPortLinAdminStatus=_OaPortLinAdminStatus_Object((1,3,6,1,4,1,629,1,50,10,11,2,1,1,3),_OaPortLinAdminStatus_Type())
oaPortLinAdminStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:oaPortLinAdminStatus.setStatus(_B)
class _OaPortLinSlavePorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_OaPortLinSlavePorts_Type.__name__=_K
_OaPortLinSlavePorts_Object=MibTableColumn
oaPortLinSlavePorts=_OaPortLinSlavePorts_Object((1,3,6,1,4,1,629,1,50,10,11,2,1,1,4),_OaPortLinSlavePorts_Type())
oaPortLinSlavePorts.setMaxAccess(_G)
if mibBuilder.loadTexts:oaPortLinSlavePorts.setStatus(_B)
class _OaPortLinSymmetricStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('symmetric',2),('nonSymmetric',3)))
_OaPortLinSymmetricStatus_Type.__name__=_C
_OaPortLinSymmetricStatus_Object=MibTableColumn
oaPortLinSymmetricStatus=_OaPortLinSymmetricStatus_Object((1,3,6,1,4,1,629,1,50,10,11,2,1,1,5),_OaPortLinSymmetricStatus_Type())
oaPortLinSymmetricStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:oaPortLinSymmetricStatus.setStatus(_B)
class _OaPortLinActionCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noAction',1),('portLinkUp',2),('portLinkDown',3),('agRMepDiscardEvent',4),('agRMepNoConnEvent',5),('agRMepAliveEvent',6)))
_OaPortLinActionCause_Type.__name__=_C
_OaPortLinActionCause_Object=MibTableColumn
oaPortLinActionCause=_OaPortLinActionCause_Object((1,3,6,1,4,1,629,1,50,10,11,2,1,1,6),_OaPortLinActionCause_Type())
oaPortLinActionCause.setMaxAccess(_D)
if mibBuilder.loadTexts:oaPortLinActionCause.setStatus(_B)
_OaPortLinAgTable_Object=MibTable
oaPortLinAgTable=_OaPortLinAgTable_Object((1,3,6,1,4,1,629,1,50,10,11,2,5))
if mibBuilder.loadTexts:oaPortLinAgTable.setStatus(_B)
_OaPortLinAgEntry_Object=MibTableRow
oaPortLinAgEntry=_OaPortLinAgEntry_Object((1,3,6,1,4,1,629,1,50,10,11,2,5,1))
oaPortLinAgEntry.setIndexNames((0,_A,_J),(0,_A,_P),(0,_A,_Q),(0,_A,_R))
if mibBuilder.loadTexts:oaPortLinAgEntry.setStatus(_B)
class _OaPortLinAgDomainId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_OaPortLinAgDomainId_Type.__name__=_E
_OaPortLinAgDomainId_Object=MibTableColumn
oaPortLinAgDomainId=_OaPortLinAgDomainId_Object((1,3,6,1,4,1,629,1,50,10,11,2,5,1,2),_OaPortLinAgDomainId_Type())
oaPortLinAgDomainId.setMaxAccess(_F)
if mibBuilder.loadTexts:oaPortLinAgDomainId.setStatus(_B)
class _OaPortLinAgAssociationId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_OaPortLinAgAssociationId_Type.__name__=_E
_OaPortLinAgAssociationId_Object=MibTableColumn
oaPortLinAgAssociationId=_OaPortLinAgAssociationId_Object((1,3,6,1,4,1,629,1,50,10,11,2,5,1,3),_OaPortLinAgAssociationId_Type())
oaPortLinAgAssociationId.setMaxAccess(_F)
if mibBuilder.loadTexts:oaPortLinAgAssociationId.setStatus(_B)
class _OaPortLinAgRemoteMep_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8192))
_OaPortLinAgRemoteMep_Type.__name__=_E
_OaPortLinAgRemoteMep_Object=MibTableColumn
oaPortLinAgRemoteMep=_OaPortLinAgRemoteMep_Object((1,3,6,1,4,1,629,1,50,10,11,2,5,1,4),_OaPortLinAgRemoteMep_Type())
oaPortLinAgRemoteMep.setMaxAccess(_F)
if mibBuilder.loadTexts:oaPortLinAgRemoteMep.setStatus(_B)
class _OaPortLinAgRMepStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('discard',2),('noConnection',3)))
_OaPortLinAgRMepStatus_Type.__name__=_C
_OaPortLinAgRMepStatus_Object=MibTableColumn
oaPortLinAgRMepStatus=_OaPortLinAgRMepStatus_Object((1,3,6,1,4,1,629,1,50,10,11,2,5,1,8),_OaPortLinAgRMepStatus_Type())
oaPortLinAgRMepStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:oaPortLinAgRMepStatus.setStatus(_B)
class _OaPortLinAgAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_O,2)))
_OaPortLinAgAdminStatus_Type.__name__=_C
_OaPortLinAgAdminStatus_Object=MibTableColumn
oaPortLinAgAdminStatus=_OaPortLinAgAdminStatus_Object((1,3,6,1,4,1,629,1,50,10,11,2,5,1,10),_OaPortLinAgAdminStatus_Type())
oaPortLinAgAdminStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:oaPortLinAgAdminStatus.setStatus(_B)
_OaPortLinConformance_ObjectIdentity=ObjectIdentity
oaPortLinConformance=_OaPortLinConformance_ObjectIdentity((1,3,6,1,4,1,629,1,50,10,11,101))
_OaPortLinCompliances_ObjectIdentity=ObjectIdentity
oaPortLinCompliances=_OaPortLinCompliances_ObjectIdentity((1,3,6,1,4,1,629,1,50,10,11,101,1))
_OaPortLinGroups_ObjectIdentity=ObjectIdentity
oaPortLinGroups=_OaPortLinGroups_ObjectIdentity((1,3,6,1,4,1,629,1,50,10,11,101,2))
oaPortLinMandatoryGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,10,11,101,2,1))
oaPortLinMandatoryGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_H),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:oaPortLinMandatoryGroup.setStatus(_B)
oaPortLinTrapParamsGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,10,11,101,2,2))
oaPortLinTrapParamsGroup.setObjects((_A,_I))
if mibBuilder.loadTexts:oaPortLinTrapParamsGroup.setStatus(_B)
oaPortLinGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,10,11,101,2,3))
oaPortLinGroup.setObjects(*((_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:oaPortLinGroup.setStatus(_B)
oaPortLinStateUp=NotificationType((1,3,6,1,4,1,629,1,50,10,11,0,33))
oaPortLinStateUp.setObjects(*((_A,_H),(_A,_I)))
if mibBuilder.loadTexts:oaPortLinStateUp.setStatus(_B)
oaPortLinStateDown=NotificationType((1,3,6,1,4,1,629,1,50,10,11,0,35))
oaPortLinStateDown.setObjects(*((_A,_H),(_A,_I)))
if mibBuilder.loadTexts:oaPortLinStateDown.setStatus(_B)
oaPortLinNotificationsGroup=NotificationGroup((1,3,6,1,4,1,629,1,50,10,11,101,2,4))
oaPortLinNotificationsGroup.setObjects(*((_A,_a),(_A,_b)))
if mibBuilder.loadTexts:oaPortLinNotificationsGroup.setStatus(_B)
oaPortLinCompliance=ModuleCompliance((1,3,6,1,4,1,629,1,50,10,11,101,1,1))
oaPortLinCompliance.setObjects(*((_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:oaPortLinCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'nbPortParams':nbPortParams,'nbPortLinkReflection':nbPortLinkReflection,'oaPortLinNotifications':oaPortLinNotifications,_a:oaPortLinStateUp,_b:oaPortLinStateDown,'oaPortLinGen':oaPortLinGen,_S:oaPortLinGenSupport,_T:oaPortLinAgSupport,_X:oaPortLinLastError,'oaPortLinGrp':oaPortLinGrp,'oaPortLinTable':oaPortLinTable,'oaPortLinEntry':oaPortLinEntry,_J:oaPortLinId,_U:oaPortLinOperStatus,_V:oaPortLinAdminStatus,_H:oaPortLinSlavePorts,_W:oaPortLinSymmetricStatus,_I:oaPortLinActionCause,'oaPortLinAgTable':oaPortLinAgTable,'oaPortLinAgEntry':oaPortLinAgEntry,_P:oaPortLinAgDomainId,_Q:oaPortLinAgAssociationId,_R:oaPortLinAgRemoteMep,_Y:oaPortLinAgRMepStatus,_Z:oaPortLinAgAdminStatus,'oaPortLinConformance':oaPortLinConformance,'oaPortLinCompliances':oaPortLinCompliances,'oaPortLinCompliance':oaPortLinCompliance,'oaPortLinGroups':oaPortLinGroups,_c:oaPortLinMandatoryGroup,_e:oaPortLinTrapParamsGroup,_f:oaPortLinGroup,_d:oaPortLinNotificationsGroup})