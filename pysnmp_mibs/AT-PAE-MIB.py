_o='failure'
_n='forcedAuthed'
_m='serverAuthed'
_l='forcedUnauth'
_k='conflictingVlan'
_j='invalidVlan'
_i='noActiveServers'
_h='serverTimeout'
_g='serverReject'
_f='authTimeout'
_e='logoff'
_d='adminReset'
_c='timeout'
_b='request'
_a='forceUnauth'
_Z='forceAuth'
_Y='aborting'
_X='authenticated'
_W='authenticating'
_V='connecting'
_U='disconnected'
_T='both'
_S='TruthValue'
_R='atrMacBasedAuthLastAuthReason'
_Q='atrMacBasedAuthPostAuthVlan'
_P='atrMacBasedAuthPreAuthVlan'
_O='atrDot1xAuthLastAuthReason'
_N='atrDot1xAuthPostAuthVlan'
_M='atrDot1xAuthPreAuthVlan'
_L='success'
_K='initialise'
_J='atrMacBasedAuthPaePortSuppMacAddress'
_I='atrMacBasedAuthPaePortNumber'
_H='atrDot1xPaePortSuppMacAddress'
_G='atrDot1xPaePortNumber'
_F='Unsigned32'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='AT-PAE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
modules,=mibBuilder.importSymbols('AT-SMI-MIB','modules')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_S)
portAuth=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,118))
if mibBuilder.loadTexts:portAuth.setRevisions(('2007-01-15 11:00','2004-12-21 00:00'))
class AtrPaeControlledDirections(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),('in',1)))
class AtrPaeControlledPortStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('authorised',1),('unauthorised',2)))
class AtrPaeControlledPortControl(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forceUnauthorised',1),('auto',2),('forceAuthorised',3)))
_AtrPaeMib_ObjectIdentity=ObjectIdentity
atrPaeMib=_AtrPaeMib_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,118,1))
_AtrPaeMIBObjects_ObjectIdentity=ObjectIdentity
atrPaeMIBObjects=_AtrPaeMIBObjects_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,118,1,1))
_AtrDot1xPaeSystem_ObjectIdentity=ObjectIdentity
atrDot1xPaeSystem=_AtrDot1xPaeSystem_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,118,1,1,1))
_AtrDot1xPaePortTable_Object=MibTable
atrDot1xPaePortTable=_AtrDot1xPaePortTable_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,1,2))
if mibBuilder.loadTexts:atrDot1xPaePortTable.setStatus(_A)
_AtrDot1xPaePortEntry_Object=MibTableRow
atrDot1xPaePortEntry=_AtrDot1xPaePortEntry_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,1,2,1))
atrDot1xPaePortEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:atrDot1xPaePortEntry.setStatus(_A)
_AtrDot1xPaePortNumber_Type=InterfaceIndex
_AtrDot1xPaePortNumber_Object=MibTableColumn
atrDot1xPaePortNumber=_AtrDot1xPaePortNumber_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,1,2,1,1),_AtrDot1xPaePortNumber_Type())
atrDot1xPaePortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xPaePortNumber.setStatus(_A)
_AtrDot1xPaePortProtocolVersion_Type=Unsigned32
_AtrDot1xPaePortProtocolVersion_Object=MibTableColumn
atrDot1xPaePortProtocolVersion=_AtrDot1xPaePortProtocolVersion_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,1,2,1,2),_AtrDot1xPaePortProtocolVersion_Type())
atrDot1xPaePortProtocolVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xPaePortProtocolVersion.setStatus(_A)
class _AtrDot1xPaePortCapabilities_Type(Bits):namedValues=NamedValues(*(('atrDot1xPaePortAuthCapable',0),('atrDot1xPaePortSuppCapable',1)))
_AtrDot1xPaePortCapabilities_Type.__name__='Bits'
_AtrDot1xPaePortCapabilities_Object=MibTableColumn
atrDot1xPaePortCapabilities=_AtrDot1xPaePortCapabilities_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,1,2,1,3),_AtrDot1xPaePortCapabilities_Type())
atrDot1xPaePortCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xPaePortCapabilities.setStatus(_A)
_AtrDot1xPaePortInitialise_Type=TruthValue
_AtrDot1xPaePortInitialise_Object=MibTableColumn
atrDot1xPaePortInitialise=_AtrDot1xPaePortInitialise_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,1,2,1,4),_AtrDot1xPaePortInitialise_Type())
atrDot1xPaePortInitialise.setMaxAccess(_D)
if mibBuilder.loadTexts:atrDot1xPaePortInitialise.setStatus(_A)
_AtrDot1xPaePortReauthenticate_Type=TruthValue
_AtrDot1xPaePortReauthenticate_Object=MibTableColumn
atrDot1xPaePortReauthenticate=_AtrDot1xPaePortReauthenticate_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,1,2,1,5),_AtrDot1xPaePortReauthenticate_Type())
atrDot1xPaePortReauthenticate.setMaxAccess(_D)
if mibBuilder.loadTexts:atrDot1xPaePortReauthenticate.setStatus(_A)
_AtrDot1xPaePortSuppMacAddress_Type=MacAddress
_AtrDot1xPaePortSuppMacAddress_Object=MibTableColumn
atrDot1xPaePortSuppMacAddress=_AtrDot1xPaePortSuppMacAddress_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,1,2,1,6),_AtrDot1xPaePortSuppMacAddress_Type())
atrDot1xPaePortSuppMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xPaePortSuppMacAddress.setStatus(_A)
_AtrDot1xPaeAuthenticator_ObjectIdentity=ObjectIdentity
atrDot1xPaeAuthenticator=_AtrDot1xPaeAuthenticator_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2))
_AtrDot1xAuthConfigTable_Object=MibTable
atrDot1xAuthConfigTable=_AtrDot1xAuthConfigTable_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1))
if mibBuilder.loadTexts:atrDot1xAuthConfigTable.setStatus(_A)
_AtrDot1xAuthConfigEntry_Object=MibTableRow
atrDot1xAuthConfigEntry=_AtrDot1xAuthConfigEntry_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1))
atrDot1xAuthConfigEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:atrDot1xAuthConfigEntry.setStatus(_A)
class _AtrDot1xAuthPaeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_K,1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),('held',7),(_Z,8),(_a,9)))
_AtrDot1xAuthPaeState_Type.__name__=_E
_AtrDot1xAuthPaeState_Object=MibTableColumn
atrDot1xAuthPaeState=_AtrDot1xAuthPaeState_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,1),_AtrDot1xAuthPaeState_Type())
atrDot1xAuthPaeState.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xAuthPaeState.setStatus(_A)
class _AtrDot1xAuthBackendAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_b,1),('response',2),(_L,3),('fail',4),(_c,5),('idle',6),(_K,7)))
_AtrDot1xAuthBackendAuthState_Type.__name__=_E
_AtrDot1xAuthBackendAuthState_Object=MibTableColumn
atrDot1xAuthBackendAuthState=_AtrDot1xAuthBackendAuthState_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,2),_AtrDot1xAuthBackendAuthState_Type())
atrDot1xAuthBackendAuthState.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xAuthBackendAuthState.setStatus(_A)
_AtrDot1xAuthAdminControlledDirections_Type=AtrPaeControlledDirections
_AtrDot1xAuthAdminControlledDirections_Object=MibTableColumn
atrDot1xAuthAdminControlledDirections=_AtrDot1xAuthAdminControlledDirections_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,3),_AtrDot1xAuthAdminControlledDirections_Type())
atrDot1xAuthAdminControlledDirections.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xAuthAdminControlledDirections.setStatus(_A)
_AtrDot1xAuthOperControlledDirections_Type=AtrPaeControlledDirections
_AtrDot1xAuthOperControlledDirections_Object=MibTableColumn
atrDot1xAuthOperControlledDirections=_AtrDot1xAuthOperControlledDirections_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,4),_AtrDot1xAuthOperControlledDirections_Type())
atrDot1xAuthOperControlledDirections.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xAuthOperControlledDirections.setStatus(_A)
_AtrDot1xAuthAuthControlledPortStatus_Type=AtrPaeControlledPortStatus
_AtrDot1xAuthAuthControlledPortStatus_Object=MibTableColumn
atrDot1xAuthAuthControlledPortStatus=_AtrDot1xAuthAuthControlledPortStatus_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,5),_AtrDot1xAuthAuthControlledPortStatus_Type())
atrDot1xAuthAuthControlledPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xAuthAuthControlledPortStatus.setStatus(_A)
_AtrDot1xAuthAuthControlledPortControl_Type=AtrPaeControlledPortControl
_AtrDot1xAuthAuthControlledPortControl_Object=MibTableColumn
atrDot1xAuthAuthControlledPortControl=_AtrDot1xAuthAuthControlledPortControl_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,6),_AtrDot1xAuthAuthControlledPortControl_Type())
atrDot1xAuthAuthControlledPortControl.setMaxAccess(_D)
if mibBuilder.loadTexts:atrDot1xAuthAuthControlledPortControl.setStatus(_A)
class _AtrDot1xAuthQuietPeriod_Type(Unsigned32):defaultValue=60
_AtrDot1xAuthQuietPeriod_Type.__name__=_F
_AtrDot1xAuthQuietPeriod_Object=MibTableColumn
atrDot1xAuthQuietPeriod=_AtrDot1xAuthQuietPeriod_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,7),_AtrDot1xAuthQuietPeriod_Type())
atrDot1xAuthQuietPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:atrDot1xAuthQuietPeriod.setStatus(_A)
class _AtrDot1xAuthTxPeriod_Type(Unsigned32):defaultValue=30
_AtrDot1xAuthTxPeriod_Type.__name__=_F
_AtrDot1xAuthTxPeriod_Object=MibTableColumn
atrDot1xAuthTxPeriod=_AtrDot1xAuthTxPeriod_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,8),_AtrDot1xAuthTxPeriod_Type())
atrDot1xAuthTxPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:atrDot1xAuthTxPeriod.setStatus(_A)
class _AtrDot1xAuthSuppTimeout_Type(Unsigned32):defaultValue=30
_AtrDot1xAuthSuppTimeout_Type.__name__=_F
_AtrDot1xAuthSuppTimeout_Object=MibTableColumn
atrDot1xAuthSuppTimeout=_AtrDot1xAuthSuppTimeout_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,9),_AtrDot1xAuthSuppTimeout_Type())
atrDot1xAuthSuppTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:atrDot1xAuthSuppTimeout.setStatus(_A)
class _AtrDot1xAuthServerTimeout_Type(Unsigned32):defaultValue=30
_AtrDot1xAuthServerTimeout_Type.__name__=_F
_AtrDot1xAuthServerTimeout_Object=MibTableColumn
atrDot1xAuthServerTimeout=_AtrDot1xAuthServerTimeout_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,10),_AtrDot1xAuthServerTimeout_Type())
atrDot1xAuthServerTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:atrDot1xAuthServerTimeout.setStatus(_A)
class _AtrDot1xAuthMaxReq_Type(Unsigned32):defaultValue=2
_AtrDot1xAuthMaxReq_Type.__name__=_F
_AtrDot1xAuthMaxReq_Object=MibTableColumn
atrDot1xAuthMaxReq=_AtrDot1xAuthMaxReq_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,11),_AtrDot1xAuthMaxReq_Type())
atrDot1xAuthMaxReq.setMaxAccess(_D)
if mibBuilder.loadTexts:atrDot1xAuthMaxReq.setStatus(_A)
class _AtrDot1xAuthReAuthPeriod_Type(Unsigned32):defaultValue=3600
_AtrDot1xAuthReAuthPeriod_Type.__name__=_F
_AtrDot1xAuthReAuthPeriod_Object=MibTableColumn
atrDot1xAuthReAuthPeriod=_AtrDot1xAuthReAuthPeriod_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,12),_AtrDot1xAuthReAuthPeriod_Type())
atrDot1xAuthReAuthPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:atrDot1xAuthReAuthPeriod.setStatus(_A)
class _AtrDot1xAuthReAuthEnabled_Type(TruthValue):defaultValue=2
_AtrDot1xAuthReAuthEnabled_Type.__name__=_S
_AtrDot1xAuthReAuthEnabled_Object=MibTableColumn
atrDot1xAuthReAuthEnabled=_AtrDot1xAuthReAuthEnabled_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,13),_AtrDot1xAuthReAuthEnabled_Type())
atrDot1xAuthReAuthEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:atrDot1xAuthReAuthEnabled.setStatus(_A)
_AtrDot1xAuthKeyTxEnabled_Type=TruthValue
_AtrDot1xAuthKeyTxEnabled_Object=MibTableColumn
atrDot1xAuthKeyTxEnabled=_AtrDot1xAuthKeyTxEnabled_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,14),_AtrDot1xAuthKeyTxEnabled_Type())
atrDot1xAuthKeyTxEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xAuthKeyTxEnabled.setStatus(_A)
_AtrDot1xAuthPreAuthVlan_Type=DisplayString
_AtrDot1xAuthPreAuthVlan_Object=MibTableColumn
atrDot1xAuthPreAuthVlan=_AtrDot1xAuthPreAuthVlan_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,15),_AtrDot1xAuthPreAuthVlan_Type())
atrDot1xAuthPreAuthVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xAuthPreAuthVlan.setStatus(_A)
_AtrDot1xAuthPostAuthVlan_Type=DisplayString
_AtrDot1xAuthPostAuthVlan_Object=MibTableColumn
atrDot1xAuthPostAuthVlan=_AtrDot1xAuthPostAuthVlan_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,16),_AtrDot1xAuthPostAuthVlan_Type())
atrDot1xAuthPostAuthVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xAuthPostAuthVlan.setStatus(_A)
class _AtrDot1xAuthLastAuthReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('never',1),(_d,2),(_e,3),(_f,4),(_g,5),(_h,6),(_i,7),(_j,8),(_k,9),(_l,10),(_m,11),(_n,12)))
_AtrDot1xAuthLastAuthReason_Type.__name__=_E
_AtrDot1xAuthLastAuthReason_Object=MibTableColumn
atrDot1xAuthLastAuthReason=_AtrDot1xAuthLastAuthReason_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,17),_AtrDot1xAuthLastAuthReason_Type())
atrDot1xAuthLastAuthReason.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xAuthLastAuthReason.setStatus(_A)
_AtrDot1XAuthVlanAssignment_Type=TruthValue
_AtrDot1XAuthVlanAssignment_Object=MibTableColumn
atrDot1XAuthVlanAssignment=_AtrDot1XAuthVlanAssignment_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,18),_AtrDot1XAuthVlanAssignment_Type())
atrDot1XAuthVlanAssignment.setMaxAccess(_D)
if mibBuilder.loadTexts:atrDot1XAuthVlanAssignment.setStatus(_A)
_AtrDot1XAuthSecureVlan_Type=TruthValue
_AtrDot1XAuthSecureVlan_Object=MibTableColumn
atrDot1XAuthSecureVlan=_AtrDot1XAuthSecureVlan_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,19),_AtrDot1XAuthSecureVlan_Type())
atrDot1XAuthSecureVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:atrDot1XAuthSecureVlan.setStatus(_A)
_AtrDot1xAuthGuestVlan_Type=DisplayString
_AtrDot1xAuthGuestVlan_Object=MibTableColumn
atrDot1xAuthGuestVlan=_AtrDot1xAuthGuestVlan_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,20),_AtrDot1xAuthGuestVlan_Type())
atrDot1xAuthGuestVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:atrDot1xAuthGuestVlan.setStatus(_A)
_AtrDot1XAuthMibReset_Type=TruthValue
_AtrDot1XAuthMibReset_Object=MibTableColumn
atrDot1XAuthMibReset=_AtrDot1XAuthMibReset_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,21),_AtrDot1XAuthMibReset_Type())
atrDot1XAuthMibReset.setMaxAccess(_D)
if mibBuilder.loadTexts:atrDot1XAuthMibReset.setStatus(_A)
class _AtrDot1xAuthTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_o,2),(_T,3),('none',4)))
_AtrDot1xAuthTrap_Type.__name__=_E
_AtrDot1xAuthTrap_Object=MibTableColumn
atrDot1xAuthTrap=_AtrDot1xAuthTrap_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,1,1,22),_AtrDot1xAuthTrap_Type())
atrDot1xAuthTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:atrDot1xAuthTrap.setStatus(_A)
_AtrDot1xAuthStatsTable_Object=MibTable
atrDot1xAuthStatsTable=_AtrDot1xAuthStatsTable_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,2))
if mibBuilder.loadTexts:atrDot1xAuthStatsTable.setStatus(_A)
_AtrDot1xAuthStatsEntry_Object=MibTableRow
atrDot1xAuthStatsEntry=_AtrDot1xAuthStatsEntry_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,2,1))
atrDot1xAuthStatsEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:atrDot1xAuthStatsEntry.setStatus(_A)
_AtrDot1xAuthEapolFramesRx_Type=Counter32
_AtrDot1xAuthEapolFramesRx_Object=MibTableColumn
atrDot1xAuthEapolFramesRx=_AtrDot1xAuthEapolFramesRx_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,2,1,1),_AtrDot1xAuthEapolFramesRx_Type())
atrDot1xAuthEapolFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xAuthEapolFramesRx.setStatus(_A)
_AtrDot1xAuthEapolFramesTx_Type=Counter32
_AtrDot1xAuthEapolFramesTx_Object=MibTableColumn
atrDot1xAuthEapolFramesTx=_AtrDot1xAuthEapolFramesTx_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,2,1,2),_AtrDot1xAuthEapolFramesTx_Type())
atrDot1xAuthEapolFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xAuthEapolFramesTx.setStatus(_A)
_AtrDot1xAuthEapolStartFramesRx_Type=Counter32
_AtrDot1xAuthEapolStartFramesRx_Object=MibTableColumn
atrDot1xAuthEapolStartFramesRx=_AtrDot1xAuthEapolStartFramesRx_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,2,1,3),_AtrDot1xAuthEapolStartFramesRx_Type())
atrDot1xAuthEapolStartFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xAuthEapolStartFramesRx.setStatus(_A)
_AtrDot1xAuthEapolLogoffFramesRx_Type=Counter32
_AtrDot1xAuthEapolLogoffFramesRx_Object=MibTableColumn
atrDot1xAuthEapolLogoffFramesRx=_AtrDot1xAuthEapolLogoffFramesRx_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,2,1,4),_AtrDot1xAuthEapolLogoffFramesRx_Type())
atrDot1xAuthEapolLogoffFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xAuthEapolLogoffFramesRx.setStatus(_A)
_AtrDot1xAuthEapolRespIdFramesRx_Type=Counter32
_AtrDot1xAuthEapolRespIdFramesRx_Object=MibTableColumn
atrDot1xAuthEapolRespIdFramesRx=_AtrDot1xAuthEapolRespIdFramesRx_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,2,1,5),_AtrDot1xAuthEapolRespIdFramesRx_Type())
atrDot1xAuthEapolRespIdFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xAuthEapolRespIdFramesRx.setStatus(_A)
_AtrDot1xAuthEapolRespFramesRx_Type=Counter32
_AtrDot1xAuthEapolRespFramesRx_Object=MibTableColumn
atrDot1xAuthEapolRespFramesRx=_AtrDot1xAuthEapolRespFramesRx_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,2,1,6),_AtrDot1xAuthEapolRespFramesRx_Type())
atrDot1xAuthEapolRespFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xAuthEapolRespFramesRx.setStatus(_A)
_AtrDot1xAuthEapolReqIdFramesTx_Type=Counter32
_AtrDot1xAuthEapolReqIdFramesTx_Object=MibTableColumn
atrDot1xAuthEapolReqIdFramesTx=_AtrDot1xAuthEapolReqIdFramesTx_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,2,1,7),_AtrDot1xAuthEapolReqIdFramesTx_Type())
atrDot1xAuthEapolReqIdFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xAuthEapolReqIdFramesTx.setStatus(_A)
_AtrDot1xAuthEapolReqFramesTx_Type=Counter32
_AtrDot1xAuthEapolReqFramesTx_Object=MibTableColumn
atrDot1xAuthEapolReqFramesTx=_AtrDot1xAuthEapolReqFramesTx_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,2,1,8),_AtrDot1xAuthEapolReqFramesTx_Type())
atrDot1xAuthEapolReqFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xAuthEapolReqFramesTx.setStatus(_A)
_AtrDot1xAuthInvalidEapolFramesRx_Type=Counter32
_AtrDot1xAuthInvalidEapolFramesRx_Object=MibTableColumn
atrDot1xAuthInvalidEapolFramesRx=_AtrDot1xAuthInvalidEapolFramesRx_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,2,1,9),_AtrDot1xAuthInvalidEapolFramesRx_Type())
atrDot1xAuthInvalidEapolFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xAuthInvalidEapolFramesRx.setStatus(_A)
_AtrDot1xAuthEapLengthErrorFramesRx_Type=Counter32
_AtrDot1xAuthEapLengthErrorFramesRx_Object=MibTableColumn
atrDot1xAuthEapLengthErrorFramesRx=_AtrDot1xAuthEapLengthErrorFramesRx_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,2,1,10),_AtrDot1xAuthEapLengthErrorFramesRx_Type())
atrDot1xAuthEapLengthErrorFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xAuthEapLengthErrorFramesRx.setStatus(_A)
_AtrDot1xAuthLastEapolFrameVersion_Type=Unsigned32
_AtrDot1xAuthLastEapolFrameVersion_Object=MibTableColumn
atrDot1xAuthLastEapolFrameVersion=_AtrDot1xAuthLastEapolFrameVersion_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,2,2,1,11),_AtrDot1xAuthLastEapolFrameVersion_Type())
atrDot1xAuthLastEapolFrameVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:atrDot1xAuthLastEapolFrameVersion.setStatus(_A)
_AtrDot1xTraps_ObjectIdentity=ObjectIdentity
atrDot1xTraps=_AtrDot1xTraps_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,118,1,1,3))
_AtrMacBasedAuthPaeSystem_ObjectIdentity=ObjectIdentity
atrMacBasedAuthPaeSystem=_AtrMacBasedAuthPaeSystem_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,118,1,1,4))
_AtrMacBasedAuthPaePortTable_Object=MibTable
atrMacBasedAuthPaePortTable=_AtrMacBasedAuthPaePortTable_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,4,1))
if mibBuilder.loadTexts:atrMacBasedAuthPaePortTable.setStatus(_A)
_AtrMacBasedAuthPaePortEntry_Object=MibTableRow
atrMacBasedAuthPaePortEntry=_AtrMacBasedAuthPaePortEntry_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,4,1,1))
atrMacBasedAuthPaePortEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:atrMacBasedAuthPaePortEntry.setStatus(_A)
_AtrMacBasedAuthPaePortNumber_Type=InterfaceIndex
_AtrMacBasedAuthPaePortNumber_Object=MibTableColumn
atrMacBasedAuthPaePortNumber=_AtrMacBasedAuthPaePortNumber_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,4,1,1,1),_AtrMacBasedAuthPaePortNumber_Type())
atrMacBasedAuthPaePortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:atrMacBasedAuthPaePortNumber.setStatus(_A)
_AtrMacBasedAuthPaePortInitialise_Type=TruthValue
_AtrMacBasedAuthPaePortInitialise_Object=MibTableColumn
atrMacBasedAuthPaePortInitialise=_AtrMacBasedAuthPaePortInitialise_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,4,1,1,2),_AtrMacBasedAuthPaePortInitialise_Type())
atrMacBasedAuthPaePortInitialise.setMaxAccess(_D)
if mibBuilder.loadTexts:atrMacBasedAuthPaePortInitialise.setStatus(_A)
_AtrMacBasedAuthPaePortReauthenticate_Type=TruthValue
_AtrMacBasedAuthPaePortReauthenticate_Object=MibTableColumn
atrMacBasedAuthPaePortReauthenticate=_AtrMacBasedAuthPaePortReauthenticate_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,4,1,1,3),_AtrMacBasedAuthPaePortReauthenticate_Type())
atrMacBasedAuthPaePortReauthenticate.setMaxAccess(_D)
if mibBuilder.loadTexts:atrMacBasedAuthPaePortReauthenticate.setStatus(_A)
_AtrMacBasedAuthPaePortSuppMacAddress_Type=MacAddress
_AtrMacBasedAuthPaePortSuppMacAddress_Object=MibTableColumn
atrMacBasedAuthPaePortSuppMacAddress=_AtrMacBasedAuthPaePortSuppMacAddress_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,4,1,1,4),_AtrMacBasedAuthPaePortSuppMacAddress_Type())
atrMacBasedAuthPaePortSuppMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:atrMacBasedAuthPaePortSuppMacAddress.setStatus(_A)
_AtrMacBasedAuthPaeAuthenticator_ObjectIdentity=ObjectIdentity
atrMacBasedAuthPaeAuthenticator=_AtrMacBasedAuthPaeAuthenticator_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,118,1,1,5))
_AtrMacBasedAuthConfigTable_Object=MibTable
atrMacBasedAuthConfigTable=_AtrMacBasedAuthConfigTable_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,5,1))
if mibBuilder.loadTexts:atrMacBasedAuthConfigTable.setStatus(_A)
_AtrMacBasedAuthConfigEntry_Object=MibTableRow
atrMacBasedAuthConfigEntry=_AtrMacBasedAuthConfigEntry_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,5,1,1))
atrMacBasedAuthConfigEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:atrMacBasedAuthConfigEntry.setStatus(_A)
class _AtrMacBasedAuthPaeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_K,1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),('held',7),(_Z,8),(_a,9)))
_AtrMacBasedAuthPaeState_Type.__name__=_E
_AtrMacBasedAuthPaeState_Object=MibTableColumn
atrMacBasedAuthPaeState=_AtrMacBasedAuthPaeState_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,5,1,1,1),_AtrMacBasedAuthPaeState_Type())
atrMacBasedAuthPaeState.setMaxAccess(_C)
if mibBuilder.loadTexts:atrMacBasedAuthPaeState.setStatus(_A)
class _AtrMacBasedAuthBackendAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_b,1),(_L,2),('fail',3),(_c,4),('idle',5),(_K,6)))
_AtrMacBasedAuthBackendAuthState_Type.__name__=_E
_AtrMacBasedAuthBackendAuthState_Object=MibTableColumn
atrMacBasedAuthBackendAuthState=_AtrMacBasedAuthBackendAuthState_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,5,1,1,2),_AtrMacBasedAuthBackendAuthState_Type())
atrMacBasedAuthBackendAuthState.setMaxAccess(_C)
if mibBuilder.loadTexts:atrMacBasedAuthBackendAuthState.setStatus(_A)
_AtrMacBasedAuthControlledPortStatus_Type=AtrPaeControlledPortStatus
_AtrMacBasedAuthControlledPortStatus_Object=MibTableColumn
atrMacBasedAuthControlledPortStatus=_AtrMacBasedAuthControlledPortStatus_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,5,1,1,3),_AtrMacBasedAuthControlledPortStatus_Type())
atrMacBasedAuthControlledPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:atrMacBasedAuthControlledPortStatus.setStatus(_A)
_AtrMacBasedAuthControlledPortControl_Type=AtrPaeControlledPortControl
_AtrMacBasedAuthControlledPortControl_Object=MibTableColumn
atrMacBasedAuthControlledPortControl=_AtrMacBasedAuthControlledPortControl_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,5,1,1,4),_AtrMacBasedAuthControlledPortControl_Type())
atrMacBasedAuthControlledPortControl.setMaxAccess(_D)
if mibBuilder.loadTexts:atrMacBasedAuthControlledPortControl.setStatus(_A)
class _AtrMacBasedAuthQuietPeriod_Type(Unsigned32):defaultValue=60
_AtrMacBasedAuthQuietPeriod_Type.__name__=_F
_AtrMacBasedAuthQuietPeriod_Object=MibTableColumn
atrMacBasedAuthQuietPeriod=_AtrMacBasedAuthQuietPeriod_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,5,1,1,5),_AtrMacBasedAuthQuietPeriod_Type())
atrMacBasedAuthQuietPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:atrMacBasedAuthQuietPeriod.setStatus(_A)
class _AtrMacBasedAuthReAuthPeriod_Type(Unsigned32):defaultValue=3600
_AtrMacBasedAuthReAuthPeriod_Type.__name__=_F
_AtrMacBasedAuthReAuthPeriod_Object=MibTableColumn
atrMacBasedAuthReAuthPeriod=_AtrMacBasedAuthReAuthPeriod_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,5,1,1,6),_AtrMacBasedAuthReAuthPeriod_Type())
atrMacBasedAuthReAuthPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:atrMacBasedAuthReAuthPeriod.setStatus(_A)
class _AtrMacBasedAuthReAuthEnabled_Type(TruthValue):defaultValue=2
_AtrMacBasedAuthReAuthEnabled_Type.__name__=_S
_AtrMacBasedAuthReAuthEnabled_Object=MibTableColumn
atrMacBasedAuthReAuthEnabled=_AtrMacBasedAuthReAuthEnabled_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,5,1,1,7),_AtrMacBasedAuthReAuthEnabled_Type())
atrMacBasedAuthReAuthEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:atrMacBasedAuthReAuthEnabled.setStatus(_A)
_AtrMacBasedAuthPreAuthVlan_Type=DisplayString
_AtrMacBasedAuthPreAuthVlan_Object=MibTableColumn
atrMacBasedAuthPreAuthVlan=_AtrMacBasedAuthPreAuthVlan_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,5,1,1,8),_AtrMacBasedAuthPreAuthVlan_Type())
atrMacBasedAuthPreAuthVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:atrMacBasedAuthPreAuthVlan.setStatus(_A)
_AtrMacBasedAuthPostAuthVlan_Type=DisplayString
_AtrMacBasedAuthPostAuthVlan_Object=MibTableColumn
atrMacBasedAuthPostAuthVlan=_AtrMacBasedAuthPostAuthVlan_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,5,1,1,9),_AtrMacBasedAuthPostAuthVlan_Type())
atrMacBasedAuthPostAuthVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:atrMacBasedAuthPostAuthVlan.setStatus(_A)
class _AtrMacBasedAuthLastAuthReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('never',1),(_d,2),(_e,3),(_f,4),(_g,5),(_h,6),(_i,7),(_j,8),(_k,9),(_l,10),(_m,11),(_n,12)))
_AtrMacBasedAuthLastAuthReason_Type.__name__=_E
_AtrMacBasedAuthLastAuthReason_Object=MibTableColumn
atrMacBasedAuthLastAuthReason=_AtrMacBasedAuthLastAuthReason_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,5,1,1,10),_AtrMacBasedAuthLastAuthReason_Type())
atrMacBasedAuthLastAuthReason.setMaxAccess(_C)
if mibBuilder.loadTexts:atrMacBasedAuthLastAuthReason.setStatus(_A)
_AtrMacBasedAuthVlanAssignment_Type=TruthValue
_AtrMacBasedAuthVlanAssignment_Object=MibTableColumn
atrMacBasedAuthVlanAssignment=_AtrMacBasedAuthVlanAssignment_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,5,1,1,11),_AtrMacBasedAuthVlanAssignment_Type())
atrMacBasedAuthVlanAssignment.setMaxAccess(_D)
if mibBuilder.loadTexts:atrMacBasedAuthVlanAssignment.setStatus(_A)
_AtrMacBasedAuthSecureVlan_Type=TruthValue
_AtrMacBasedAuthSecureVlan_Object=MibTableColumn
atrMacBasedAuthSecureVlan=_AtrMacBasedAuthSecureVlan_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,5,1,1,12),_AtrMacBasedAuthSecureVlan_Type())
atrMacBasedAuthSecureVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:atrMacBasedAuthSecureVlan.setStatus(_A)
_AtrMacBasedAuthMibReset_Type=TruthValue
_AtrMacBasedAuthMibReset_Object=MibTableColumn
atrMacBasedAuthMibReset=_AtrMacBasedAuthMibReset_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,5,1,1,13),_AtrMacBasedAuthMibReset_Type())
atrMacBasedAuthMibReset.setMaxAccess(_D)
if mibBuilder.loadTexts:atrMacBasedAuthMibReset.setStatus(_A)
class _AtrMacBasedAuthTrap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_o,2),(_T,3),('none',4)))
_AtrMacBasedAuthTrap_Type.__name__=_E
_AtrMacBasedAuthTrap_Object=MibTableColumn
atrMacBasedAuthTrap=_AtrMacBasedAuthTrap_Object((1,3,6,1,4,1,207,8,4,4,4,118,1,1,5,1,1,14),_AtrMacBasedAuthTrap_Type())
atrMacBasedAuthTrap.setMaxAccess(_D)
if mibBuilder.loadTexts:atrMacBasedAuthTrap.setStatus(_A)
_AtrMacBasedAuthTraps_ObjectIdentity=ObjectIdentity
atrMacBasedAuthTraps=_AtrMacBasedAuthTraps_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,118,1,1,6))
atrDot1xAuthenticated=NotificationType((1,3,6,1,4,1,207,8,4,4,4,118,1,1,3,1))
atrDot1xAuthenticated.setObjects(*((_B,_G),(_B,_H),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:atrDot1xAuthenticated.setStatus(_A)
atrDot1xUnauthenticated=NotificationType((1,3,6,1,4,1,207,8,4,4,4,118,1,1,3,2))
atrDot1xUnauthenticated.setObjects(*((_B,_G),(_B,_H),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:atrDot1xUnauthenticated.setStatus(_A)
atrDot1xFailedAuth=NotificationType((1,3,6,1,4,1,207,8,4,4,4,118,1,1,3,3))
atrDot1xFailedAuth.setObjects(*((_B,_G),(_B,_H),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:atrDot1xFailedAuth.setStatus(_A)
atrMacBasedAuthAuthenticated=NotificationType((1,3,6,1,4,1,207,8,4,4,4,118,1,1,6,1))
atrMacBasedAuthAuthenticated.setObjects(*((_B,_I),(_B,_J),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:atrMacBasedAuthAuthenticated.setStatus(_A)
atrMacBasedAuthUnauthenticated=NotificationType((1,3,6,1,4,1,207,8,4,4,4,118,1,1,6,2))
atrMacBasedAuthUnauthenticated.setObjects(*((_B,_I),(_B,_J),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:atrMacBasedAuthUnauthenticated.setStatus(_A)
atrMacBasedAuthFailedAuth=NotificationType((1,3,6,1,4,1,207,8,4,4,4,118,1,1,6,3))
atrMacBasedAuthFailedAuth.setObjects(*((_B,_I),(_B,_J),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:atrMacBasedAuthFailedAuth.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AtrPaeControlledDirections':AtrPaeControlledDirections,'AtrPaeControlledPortStatus':AtrPaeControlledPortStatus,'AtrPaeControlledPortControl':AtrPaeControlledPortControl,'portAuth':portAuth,'atrPaeMib':atrPaeMib,'atrPaeMIBObjects':atrPaeMIBObjects,'atrDot1xPaeSystem':atrDot1xPaeSystem,'atrDot1xPaePortTable':atrDot1xPaePortTable,'atrDot1xPaePortEntry':atrDot1xPaePortEntry,_G:atrDot1xPaePortNumber,'atrDot1xPaePortProtocolVersion':atrDot1xPaePortProtocolVersion,'atrDot1xPaePortCapabilities':atrDot1xPaePortCapabilities,'atrDot1xPaePortInitialise':atrDot1xPaePortInitialise,'atrDot1xPaePortReauthenticate':atrDot1xPaePortReauthenticate,_H:atrDot1xPaePortSuppMacAddress,'atrDot1xPaeAuthenticator':atrDot1xPaeAuthenticator,'atrDot1xAuthConfigTable':atrDot1xAuthConfigTable,'atrDot1xAuthConfigEntry':atrDot1xAuthConfigEntry,'atrDot1xAuthPaeState':atrDot1xAuthPaeState,'atrDot1xAuthBackendAuthState':atrDot1xAuthBackendAuthState,'atrDot1xAuthAdminControlledDirections':atrDot1xAuthAdminControlledDirections,'atrDot1xAuthOperControlledDirections':atrDot1xAuthOperControlledDirections,'atrDot1xAuthAuthControlledPortStatus':atrDot1xAuthAuthControlledPortStatus,'atrDot1xAuthAuthControlledPortControl':atrDot1xAuthAuthControlledPortControl,'atrDot1xAuthQuietPeriod':atrDot1xAuthQuietPeriod,'atrDot1xAuthTxPeriod':atrDot1xAuthTxPeriod,'atrDot1xAuthSuppTimeout':atrDot1xAuthSuppTimeout,'atrDot1xAuthServerTimeout':atrDot1xAuthServerTimeout,'atrDot1xAuthMaxReq':atrDot1xAuthMaxReq,'atrDot1xAuthReAuthPeriod':atrDot1xAuthReAuthPeriod,'atrDot1xAuthReAuthEnabled':atrDot1xAuthReAuthEnabled,'atrDot1xAuthKeyTxEnabled':atrDot1xAuthKeyTxEnabled,_M:atrDot1xAuthPreAuthVlan,_N:atrDot1xAuthPostAuthVlan,_O:atrDot1xAuthLastAuthReason,'atrDot1XAuthVlanAssignment':atrDot1XAuthVlanAssignment,'atrDot1XAuthSecureVlan':atrDot1XAuthSecureVlan,'atrDot1xAuthGuestVlan':atrDot1xAuthGuestVlan,'atrDot1XAuthMibReset':atrDot1XAuthMibReset,'atrDot1xAuthTrap':atrDot1xAuthTrap,'atrDot1xAuthStatsTable':atrDot1xAuthStatsTable,'atrDot1xAuthStatsEntry':atrDot1xAuthStatsEntry,'atrDot1xAuthEapolFramesRx':atrDot1xAuthEapolFramesRx,'atrDot1xAuthEapolFramesTx':atrDot1xAuthEapolFramesTx,'atrDot1xAuthEapolStartFramesRx':atrDot1xAuthEapolStartFramesRx,'atrDot1xAuthEapolLogoffFramesRx':atrDot1xAuthEapolLogoffFramesRx,'atrDot1xAuthEapolRespIdFramesRx':atrDot1xAuthEapolRespIdFramesRx,'atrDot1xAuthEapolRespFramesRx':atrDot1xAuthEapolRespFramesRx,'atrDot1xAuthEapolReqIdFramesTx':atrDot1xAuthEapolReqIdFramesTx,'atrDot1xAuthEapolReqFramesTx':atrDot1xAuthEapolReqFramesTx,'atrDot1xAuthInvalidEapolFramesRx':atrDot1xAuthInvalidEapolFramesRx,'atrDot1xAuthEapLengthErrorFramesRx':atrDot1xAuthEapLengthErrorFramesRx,'atrDot1xAuthLastEapolFrameVersion':atrDot1xAuthLastEapolFrameVersion,'atrDot1xTraps':atrDot1xTraps,'atrDot1xAuthenticated':atrDot1xAuthenticated,'atrDot1xUnauthenticated':atrDot1xUnauthenticated,'atrDot1xFailedAuth':atrDot1xFailedAuth,'atrMacBasedAuthPaeSystem':atrMacBasedAuthPaeSystem,'atrMacBasedAuthPaePortTable':atrMacBasedAuthPaePortTable,'atrMacBasedAuthPaePortEntry':atrMacBasedAuthPaePortEntry,_I:atrMacBasedAuthPaePortNumber,'atrMacBasedAuthPaePortInitialise':atrMacBasedAuthPaePortInitialise,'atrMacBasedAuthPaePortReauthenticate':atrMacBasedAuthPaePortReauthenticate,_J:atrMacBasedAuthPaePortSuppMacAddress,'atrMacBasedAuthPaeAuthenticator':atrMacBasedAuthPaeAuthenticator,'atrMacBasedAuthConfigTable':atrMacBasedAuthConfigTable,'atrMacBasedAuthConfigEntry':atrMacBasedAuthConfigEntry,'atrMacBasedAuthPaeState':atrMacBasedAuthPaeState,'atrMacBasedAuthBackendAuthState':atrMacBasedAuthBackendAuthState,'atrMacBasedAuthControlledPortStatus':atrMacBasedAuthControlledPortStatus,'atrMacBasedAuthControlledPortControl':atrMacBasedAuthControlledPortControl,'atrMacBasedAuthQuietPeriod':atrMacBasedAuthQuietPeriod,'atrMacBasedAuthReAuthPeriod':atrMacBasedAuthReAuthPeriod,'atrMacBasedAuthReAuthEnabled':atrMacBasedAuthReAuthEnabled,_P:atrMacBasedAuthPreAuthVlan,_Q:atrMacBasedAuthPostAuthVlan,_R:atrMacBasedAuthLastAuthReason,'atrMacBasedAuthVlanAssignment':atrMacBasedAuthVlanAssignment,'atrMacBasedAuthSecureVlan':atrMacBasedAuthSecureVlan,'atrMacBasedAuthMibReset':atrMacBasedAuthMibReset,'atrMacBasedAuthTrap':atrMacBasedAuthTrap,'atrMacBasedAuthTraps':atrMacBasedAuthTraps,'atrMacBasedAuthAuthenticated':atrMacBasedAuthAuthenticated,'atrMacBasedAuthUnauthenticated':atrMacBasedAuthUnauthenticated,'atrMacBasedAuthFailedAuth':atrMacBasedAuthFailedAuth})