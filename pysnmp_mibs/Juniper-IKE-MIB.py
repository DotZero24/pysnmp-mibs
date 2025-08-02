_AH='juniIkePolicyRuleV2Group'
_AG='juniIkeSaGroup'
_AF='juniIkePolicyRuleV2RowStatus'
_AE='juniIkePolicyRuleV2RouterIndex'
_AD='juniIkePolicyRuleV2IpAddress'
_AC='juniIkePolicyRuleV2NegotiationMode'
_AB='juniIkePolicyRuleV2Lifetime'
_AA='juniIkePolicyRuleV2HashMethod'
_A9='juniIkePolicyRuleV2PfsGroup'
_A8='juniIkePolicyRuleV2EncryptMethod'
_A7='juniIkePolicyRuleV2AuthMethod'
_A6='juniLocalCookie'
_A5='juniRemoteCookie'
_A4='juniIkeSa2Remaining'
_A3='juniIkeSa2State'
_A2='juniIkeSaRemaining'
_A1='juniIkeSaState'
_A0='juniIkeFqdnPresharedKeyRowStatus'
_z='juniIkeFqdnPresharedMaskedKeyStr'
_y='juniIkeFqdnPresharedKeyStr'
_x='juniIkeIpv4PresharedKeyRowStatus'
_w='juniIkeIpv4PresharedMaskedKeyStr'
_v='juniIkeIpv4PresharedKeyStr'
_u='juniIkePolicyRuleRowStatus'
_t='juniIkePolicyRuleNegotiationMode'
_s='juniIkePolicyRuleLifetime'
_r='juniIkePolicyRuleHashMethod'
_q='juniIkePolicyRulePfsGroup'
_p='juniIkePolicyRuleEncryptMethod'
_o='juniIkePolicyRuleAuthMethod'
_n='JuniIkeNegotiationV2Mode'
_m='juniIkePolicyRuleV2Priority'
_l='juniIkeSaNegotiationDone'
_k='juniIkeSa2Direction'
_j='juniIkeSa2RouterIndex'
_i='juniIkeSaLocalPort'
_h='juniIkeSa2LocalIpAddr'
_g='juniIkeSaRemotePort'
_f='juniIkeSa2RemoteIpAddr'
_e='seconds'
_d='juniIkeSaDirection'
_c='juniIkeSaRouterIndex'
_b='juniIkeSaLocalIpAddr'
_a='juniIkeSaRemoteIpAddr'
_Z='juniIkeFqdnPresharedRouterIndex'
_Y='juniIkeFqdnPresharedRemote'
_X='juniIkeIpv4PresharedRouterIdx'
_W='juniIkeIpv4PresharedRemoteIpAddr'
_V='JuniIkeNegotiationMode'
_U='juniIkePolicyRulePriority'
_T='responder'
_S='initiator'
_R='juniIkeSa2Group'
_Q='juniIkePolicyRuleGroup'
_P='JuniIkeHashMethod'
_O='JuniIkeGroup'
_N='JuniIkeEncryptionMethod'
_M='JuniIkeAuthenticationMethod'
_L='Unsigned32'
_K='juniIkeFqdnPreSharedKeyGroup'
_J='juniIkeIpv4PreSharedKeyGroup'
_I='DisplayString'
_H='OctetString'
_G='read-only'
_F='Integer32'
_E='not-accessible'
_D='read-create'
_C='obsolete'
_B='current'
_A='Juniper-IKE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention')
juniIkeMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,71))
if mibBuilder.loadTexts:juniIkeMIB.setRevisions(('2005-11-22 16:15','2004-01-23 15:12','2004-04-06 22:26'))
class JuniIkeAuthenticationMethod(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,3)));namedValues=NamedValues(*(('rsaSignature',0),('preSharedKeys',3)))
class JuniIkeEncryptionMethod(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('des',0),('tripleDes',1)))
class JuniIkeGroup(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4)));namedValues=NamedValues(*(('group1',0),('group2',1),('group5',4)))
class JuniIkeHashMethod(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('md5',0),('sha',1)))
class JuniIkeNegotiationMode(TextualConvention,Integer32):status=_C;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('aggressive',0),('main',1)))
class JuniIkeNegotiationV2Mode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('aggressiveAccepted',0),('aggressiveRequested',1),('aggressiveRequired',2),('aggressiveNotAllowed',3)))
class JuniIpsecPhase1SaState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)));namedValues=NamedValues(*(('reserved',0),('startSaNegotiationI',1),('startSaNegotiationR',2),('mmSaI',3),('mmSaR',4),('mmKeI',5),('mmKeR',6),('mmFinalI',7),('mmFinalR',8),('mmDoneI',9),('amSaI',10),('amSaR',11),('amFinalI',12),('amDoneR',13),('startQmI',14),('startQmR',15),('qmHashSaI',16),('qmHashSaR',17),('qmHashI',18),('qmDoneR',19),('startNgmI',20),('startNgmR',21),('ngmHashSaI',22),('ngmHashSaR',23),('ngmDoneI',24),('done',25),('deleted',26)))
class JuniIpsecPhase1SaDirection(TextualConvention,Integer32):status=_C;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_S,0),(_T,1)))
_JuniIkeObjects_ObjectIdentity=ObjectIdentity
juniIkeObjects=_JuniIkeObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,71,1))
_JuniIke_ObjectIdentity=ObjectIdentity
juniIke=_JuniIke_ObjectIdentity((1,3,6,1,4,1,4874,2,2,71,1,1))
_JuniIkePolicyRuleTable_Object=MibTable
juniIkePolicyRuleTable=_JuniIkePolicyRuleTable_Object((1,3,6,1,4,1,4874,2,2,71,1,1,1))
if mibBuilder.loadTexts:juniIkePolicyRuleTable.setStatus(_C)
_JuniIkePolicyRuleEntry_Object=MibTableRow
juniIkePolicyRuleEntry=_JuniIkePolicyRuleEntry_Object((1,3,6,1,4,1,4874,2,2,71,1,1,1,1))
juniIkePolicyRuleEntry.setIndexNames((0,_A,_U))
if mibBuilder.loadTexts:juniIkePolicyRuleEntry.setStatus(_C)
class _JuniIkePolicyRulePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_JuniIkePolicyRulePriority_Type.__name__=_F
_JuniIkePolicyRulePriority_Object=MibTableColumn
juniIkePolicyRulePriority=_JuniIkePolicyRulePriority_Object((1,3,6,1,4,1,4874,2,2,71,1,1,1,1,1),_JuniIkePolicyRulePriority_Type())
juniIkePolicyRulePriority.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIkePolicyRulePriority.setStatus(_C)
class _JuniIkePolicyRuleAuthMethod_Type(JuniIkeAuthenticationMethod):defaultValue=3
_JuniIkePolicyRuleAuthMethod_Type.__name__=_M
_JuniIkePolicyRuleAuthMethod_Object=MibTableColumn
juniIkePolicyRuleAuthMethod=_JuniIkePolicyRuleAuthMethod_Object((1,3,6,1,4,1,4874,2,2,71,1,1,1,1,2),_JuniIkePolicyRuleAuthMethod_Type())
juniIkePolicyRuleAuthMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkePolicyRuleAuthMethod.setStatus(_C)
class _JuniIkePolicyRuleEncryptMethod_Type(JuniIkeEncryptionMethod):defaultValue=1
_JuniIkePolicyRuleEncryptMethod_Type.__name__=_N
_JuniIkePolicyRuleEncryptMethod_Object=MibTableColumn
juniIkePolicyRuleEncryptMethod=_JuniIkePolicyRuleEncryptMethod_Object((1,3,6,1,4,1,4874,2,2,71,1,1,1,1,3),_JuniIkePolicyRuleEncryptMethod_Type())
juniIkePolicyRuleEncryptMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkePolicyRuleEncryptMethod.setStatus(_C)
class _JuniIkePolicyRulePfsGroup_Type(JuniIkeGroup):defaultValue=1
_JuniIkePolicyRulePfsGroup_Type.__name__=_O
_JuniIkePolicyRulePfsGroup_Object=MibTableColumn
juniIkePolicyRulePfsGroup=_JuniIkePolicyRulePfsGroup_Object((1,3,6,1,4,1,4874,2,2,71,1,1,1,1,4),_JuniIkePolicyRulePfsGroup_Type())
juniIkePolicyRulePfsGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkePolicyRulePfsGroup.setStatus(_C)
class _JuniIkePolicyRuleHashMethod_Type(JuniIkeHashMethod):defaultValue=1
_JuniIkePolicyRuleHashMethod_Type.__name__=_P
_JuniIkePolicyRuleHashMethod_Object=MibTableColumn
juniIkePolicyRuleHashMethod=_JuniIkePolicyRuleHashMethod_Object((1,3,6,1,4,1,4874,2,2,71,1,1,1,1,5),_JuniIkePolicyRuleHashMethod_Type())
juniIkePolicyRuleHashMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkePolicyRuleHashMethod.setStatus(_C)
class _JuniIkePolicyRuleLifetime_Type(Integer32):defaultValue=28800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_JuniIkePolicyRuleLifetime_Type.__name__=_F
_JuniIkePolicyRuleLifetime_Object=MibTableColumn
juniIkePolicyRuleLifetime=_JuniIkePolicyRuleLifetime_Object((1,3,6,1,4,1,4874,2,2,71,1,1,1,1,6),_JuniIkePolicyRuleLifetime_Type())
juniIkePolicyRuleLifetime.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkePolicyRuleLifetime.setStatus(_C)
class _JuniIkePolicyRuleNegotiationMode_Type(JuniIkeNegotiationMode):defaultValue=0
_JuniIkePolicyRuleNegotiationMode_Type.__name__=_V
_JuniIkePolicyRuleNegotiationMode_Object=MibTableColumn
juniIkePolicyRuleNegotiationMode=_JuniIkePolicyRuleNegotiationMode_Object((1,3,6,1,4,1,4874,2,2,71,1,1,1,1,7),_JuniIkePolicyRuleNegotiationMode_Type())
juniIkePolicyRuleNegotiationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkePolicyRuleNegotiationMode.setStatus(_C)
_JuniIkePolicyRuleRowStatus_Type=RowStatus
_JuniIkePolicyRuleRowStatus_Object=MibTableColumn
juniIkePolicyRuleRowStatus=_JuniIkePolicyRuleRowStatus_Object((1,3,6,1,4,1,4874,2,2,71,1,1,1,1,8),_JuniIkePolicyRuleRowStatus_Type())
juniIkePolicyRuleRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkePolicyRuleRowStatus.setStatus(_C)
_JuniIkeIpv4PresharedKeyTable_Object=MibTable
juniIkeIpv4PresharedKeyTable=_JuniIkeIpv4PresharedKeyTable_Object((1,3,6,1,4,1,4874,2,2,71,1,1,2))
if mibBuilder.loadTexts:juniIkeIpv4PresharedKeyTable.setStatus(_B)
_JuniIkeIpv4PresharedKeyEntry_Object=MibTableRow
juniIkeIpv4PresharedKeyEntry=_JuniIkeIpv4PresharedKeyEntry_Object((1,3,6,1,4,1,4874,2,2,71,1,1,2,1))
juniIkeIpv4PresharedKeyEntry.setIndexNames((0,_A,_W),(0,_A,_X))
if mibBuilder.loadTexts:juniIkeIpv4PresharedKeyEntry.setStatus(_B)
_JuniIkeIpv4PresharedRemoteIpAddr_Type=IpAddress
_JuniIkeIpv4PresharedRemoteIpAddr_Object=MibTableColumn
juniIkeIpv4PresharedRemoteIpAddr=_JuniIkeIpv4PresharedRemoteIpAddr_Object((1,3,6,1,4,1,4874,2,2,71,1,1,2,1,1),_JuniIkeIpv4PresharedRemoteIpAddr_Type())
juniIkeIpv4PresharedRemoteIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIkeIpv4PresharedRemoteIpAddr.setStatus(_B)
_JuniIkeIpv4PresharedRouterIdx_Type=Unsigned32
_JuniIkeIpv4PresharedRouterIdx_Object=MibTableColumn
juniIkeIpv4PresharedRouterIdx=_JuniIkeIpv4PresharedRouterIdx_Object((1,3,6,1,4,1,4874,2,2,71,1,1,2,1,2),_JuniIkeIpv4PresharedRouterIdx_Type())
juniIkeIpv4PresharedRouterIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIkeIpv4PresharedRouterIdx.setStatus(_B)
class _JuniIkeIpv4PresharedKeyStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,200))
_JuniIkeIpv4PresharedKeyStr_Type.__name__=_I
_JuniIkeIpv4PresharedKeyStr_Object=MibTableColumn
juniIkeIpv4PresharedKeyStr=_JuniIkeIpv4PresharedKeyStr_Object((1,3,6,1,4,1,4874,2,2,71,1,1,2,1,3),_JuniIkeIpv4PresharedKeyStr_Type())
juniIkeIpv4PresharedKeyStr.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkeIpv4PresharedKeyStr.setStatus(_B)
class _JuniIkeIpv4PresharedMaskedKeyStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,300))
_JuniIkeIpv4PresharedMaskedKeyStr_Type.__name__=_H
_JuniIkeIpv4PresharedMaskedKeyStr_Object=MibTableColumn
juniIkeIpv4PresharedMaskedKeyStr=_JuniIkeIpv4PresharedMaskedKeyStr_Object((1,3,6,1,4,1,4874,2,2,71,1,1,2,1,4),_JuniIkeIpv4PresharedMaskedKeyStr_Type())
juniIkeIpv4PresharedMaskedKeyStr.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkeIpv4PresharedMaskedKeyStr.setStatus(_B)
_JuniIkeIpv4PresharedKeyRowStatus_Type=RowStatus
_JuniIkeIpv4PresharedKeyRowStatus_Object=MibTableColumn
juniIkeIpv4PresharedKeyRowStatus=_JuniIkeIpv4PresharedKeyRowStatus_Object((1,3,6,1,4,1,4874,2,2,71,1,1,2,1,5),_JuniIkeIpv4PresharedKeyRowStatus_Type())
juniIkeIpv4PresharedKeyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkeIpv4PresharedKeyRowStatus.setStatus(_B)
_JuniIkeFqdnPresharedKeyTable_Object=MibTable
juniIkeFqdnPresharedKeyTable=_JuniIkeFqdnPresharedKeyTable_Object((1,3,6,1,4,1,4874,2,2,71,1,1,3))
if mibBuilder.loadTexts:juniIkeFqdnPresharedKeyTable.setStatus(_B)
_JuniIkeFqdnPresharedKeyEntry_Object=MibTableRow
juniIkeFqdnPresharedKeyEntry=_JuniIkeFqdnPresharedKeyEntry_Object((1,3,6,1,4,1,4874,2,2,71,1,1,3,1))
juniIkeFqdnPresharedKeyEntry.setIndexNames((0,_A,_Y),(0,_A,_Z))
if mibBuilder.loadTexts:juniIkeFqdnPresharedKeyEntry.setStatus(_B)
class _JuniIkeFqdnPresharedRemote_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_JuniIkeFqdnPresharedRemote_Type.__name__=_I
_JuniIkeFqdnPresharedRemote_Object=MibTableColumn
juniIkeFqdnPresharedRemote=_JuniIkeFqdnPresharedRemote_Object((1,3,6,1,4,1,4874,2,2,71,1,1,3,1,1),_JuniIkeFqdnPresharedRemote_Type())
juniIkeFqdnPresharedRemote.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIkeFqdnPresharedRemote.setStatus(_B)
_JuniIkeFqdnPresharedRouterIndex_Type=Unsigned32
_JuniIkeFqdnPresharedRouterIndex_Object=MibTableColumn
juniIkeFqdnPresharedRouterIndex=_JuniIkeFqdnPresharedRouterIndex_Object((1,3,6,1,4,1,4874,2,2,71,1,1,3,1,2),_JuniIkeFqdnPresharedRouterIndex_Type())
juniIkeFqdnPresharedRouterIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIkeFqdnPresharedRouterIndex.setStatus(_B)
class _JuniIkeFqdnPresharedKeyStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,200))
_JuniIkeFqdnPresharedKeyStr_Type.__name__=_I
_JuniIkeFqdnPresharedKeyStr_Object=MibTableColumn
juniIkeFqdnPresharedKeyStr=_JuniIkeFqdnPresharedKeyStr_Object((1,3,6,1,4,1,4874,2,2,71,1,1,3,1,3),_JuniIkeFqdnPresharedKeyStr_Type())
juniIkeFqdnPresharedKeyStr.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkeFqdnPresharedKeyStr.setStatus(_B)
class _JuniIkeFqdnPresharedMaskedKeyStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,300))
_JuniIkeFqdnPresharedMaskedKeyStr_Type.__name__=_H
_JuniIkeFqdnPresharedMaskedKeyStr_Object=MibTableColumn
juniIkeFqdnPresharedMaskedKeyStr=_JuniIkeFqdnPresharedMaskedKeyStr_Object((1,3,6,1,4,1,4874,2,2,71,1,1,3,1,4),_JuniIkeFqdnPresharedMaskedKeyStr_Type())
juniIkeFqdnPresharedMaskedKeyStr.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkeFqdnPresharedMaskedKeyStr.setStatus(_B)
_JuniIkeFqdnPresharedKeyRowStatus_Type=RowStatus
_JuniIkeFqdnPresharedKeyRowStatus_Object=MibTableColumn
juniIkeFqdnPresharedKeyRowStatus=_JuniIkeFqdnPresharedKeyRowStatus_Object((1,3,6,1,4,1,4874,2,2,71,1,1,3,1,5),_JuniIkeFqdnPresharedKeyRowStatus_Type())
juniIkeFqdnPresharedKeyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkeFqdnPresharedKeyRowStatus.setStatus(_B)
_JuniIkeSaTable_Object=MibTable
juniIkeSaTable=_JuniIkeSaTable_Object((1,3,6,1,4,1,4874,2,2,71,1,1,4))
if mibBuilder.loadTexts:juniIkeSaTable.setStatus(_C)
_JuniIkeSaEntry_Object=MibTableRow
juniIkeSaEntry=_JuniIkeSaEntry_Object((1,3,6,1,4,1,4874,2,2,71,1,1,4,1))
juniIkeSaEntry.setIndexNames((0,_A,_a),(0,_A,_b),(0,_A,_c),(0,_A,_d))
if mibBuilder.loadTexts:juniIkeSaEntry.setStatus(_C)
_JuniIkeSaRemoteIpAddr_Type=IpAddress
_JuniIkeSaRemoteIpAddr_Object=MibTableColumn
juniIkeSaRemoteIpAddr=_JuniIkeSaRemoteIpAddr_Object((1,3,6,1,4,1,4874,2,2,71,1,1,4,1,1),_JuniIkeSaRemoteIpAddr_Type())
juniIkeSaRemoteIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIkeSaRemoteIpAddr.setStatus(_C)
_JuniIkeSaLocalIpAddr_Type=IpAddress
_JuniIkeSaLocalIpAddr_Object=MibTableColumn
juniIkeSaLocalIpAddr=_JuniIkeSaLocalIpAddr_Object((1,3,6,1,4,1,4874,2,2,71,1,1,4,1,2),_JuniIkeSaLocalIpAddr_Type())
juniIkeSaLocalIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIkeSaLocalIpAddr.setStatus(_C)
_JuniIkeSaRouterIndex_Type=Unsigned32
_JuniIkeSaRouterIndex_Object=MibTableColumn
juniIkeSaRouterIndex=_JuniIkeSaRouterIndex_Object((1,3,6,1,4,1,4874,2,2,71,1,1,4,1,3),_JuniIkeSaRouterIndex_Type())
juniIkeSaRouterIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIkeSaRouterIndex.setStatus(_C)
_JuniIkeSaDirection_Type=JuniIpsecPhase1SaDirection
_JuniIkeSaDirection_Object=MibTableColumn
juniIkeSaDirection=_JuniIkeSaDirection_Object((1,3,6,1,4,1,4874,2,2,71,1,1,4,1,4),_JuniIkeSaDirection_Type())
juniIkeSaDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIkeSaDirection.setStatus(_C)
_JuniIkeSaState_Type=JuniIpsecPhase1SaState
_JuniIkeSaState_Object=MibTableColumn
juniIkeSaState=_JuniIkeSaState_Object((1,3,6,1,4,1,4874,2,2,71,1,1,4,1,5),_JuniIkeSaState_Type())
juniIkeSaState.setMaxAccess(_G)
if mibBuilder.loadTexts:juniIkeSaState.setStatus(_C)
class _JuniIkeSaRemaining_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_JuniIkeSaRemaining_Type.__name__=_L
_JuniIkeSaRemaining_Object=MibTableColumn
juniIkeSaRemaining=_JuniIkeSaRemaining_Object((1,3,6,1,4,1,4874,2,2,71,1,1,4,1,6),_JuniIkeSaRemaining_Type())
juniIkeSaRemaining.setMaxAccess(_G)
if mibBuilder.loadTexts:juniIkeSaRemaining.setStatus(_C)
if mibBuilder.loadTexts:juniIkeSaRemaining.setUnits(_e)
_JuniIkeSa2Table_Object=MibTable
juniIkeSa2Table=_JuniIkeSa2Table_Object((1,3,6,1,4,1,4874,2,2,71,1,1,5))
if mibBuilder.loadTexts:juniIkeSa2Table.setStatus(_B)
_JuniIkeSa2Entry_Object=MibTableRow
juniIkeSa2Entry=_JuniIkeSa2Entry_Object((1,3,6,1,4,1,4874,2,2,71,1,1,5,1))
juniIkeSa2Entry.setIndexNames((0,_A,_f),(0,_A,_g),(0,_A,_h),(0,_A,_i),(0,_A,_j),(0,_A,_k),(0,_A,_l))
if mibBuilder.loadTexts:juniIkeSa2Entry.setStatus(_B)
_JuniIkeSa2RemoteIpAddr_Type=IpAddress
_JuniIkeSa2RemoteIpAddr_Object=MibTableColumn
juniIkeSa2RemoteIpAddr=_JuniIkeSa2RemoteIpAddr_Object((1,3,6,1,4,1,4874,2,2,71,1,1,5,1,1),_JuniIkeSa2RemoteIpAddr_Type())
juniIkeSa2RemoteIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIkeSa2RemoteIpAddr.setStatus(_B)
_JuniIkeSaRemotePort_Type=Unsigned32
_JuniIkeSaRemotePort_Object=MibTableColumn
juniIkeSaRemotePort=_JuniIkeSaRemotePort_Object((1,3,6,1,4,1,4874,2,2,71,1,1,5,1,2),_JuniIkeSaRemotePort_Type())
juniIkeSaRemotePort.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIkeSaRemotePort.setStatus(_B)
_JuniIkeSa2LocalIpAddr_Type=IpAddress
_JuniIkeSa2LocalIpAddr_Object=MibTableColumn
juniIkeSa2LocalIpAddr=_JuniIkeSa2LocalIpAddr_Object((1,3,6,1,4,1,4874,2,2,71,1,1,5,1,3),_JuniIkeSa2LocalIpAddr_Type())
juniIkeSa2LocalIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIkeSa2LocalIpAddr.setStatus(_B)
_JuniIkeSaLocalPort_Type=Unsigned32
_JuniIkeSaLocalPort_Object=MibTableColumn
juniIkeSaLocalPort=_JuniIkeSaLocalPort_Object((1,3,6,1,4,1,4874,2,2,71,1,1,5,1,4),_JuniIkeSaLocalPort_Type())
juniIkeSaLocalPort.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIkeSaLocalPort.setStatus(_B)
_JuniIkeSa2RouterIndex_Type=Unsigned32
_JuniIkeSa2RouterIndex_Object=MibTableColumn
juniIkeSa2RouterIndex=_JuniIkeSa2RouterIndex_Object((1,3,6,1,4,1,4874,2,2,71,1,1,5,1,5),_JuniIkeSa2RouterIndex_Type())
juniIkeSa2RouterIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIkeSa2RouterIndex.setStatus(_B)
class _JuniIkeSa2Direction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_S,1)))
_JuniIkeSa2Direction_Type.__name__=_F
_JuniIkeSa2Direction_Object=MibTableColumn
juniIkeSa2Direction=_JuniIkeSa2Direction_Object((1,3,6,1,4,1,4874,2,2,71,1,1,5,1,6),_JuniIkeSa2Direction_Type())
juniIkeSa2Direction.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIkeSa2Direction.setStatus(_B)
class _JuniIkeSaNegotiationDone_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('negotiationNotDone',0),('negotiationDone',1)))
_JuniIkeSaNegotiationDone_Type.__name__=_F
_JuniIkeSaNegotiationDone_Object=MibTableColumn
juniIkeSaNegotiationDone=_JuniIkeSaNegotiationDone_Object((1,3,6,1,4,1,4874,2,2,71,1,1,5,1,7),_JuniIkeSaNegotiationDone_Type())
juniIkeSaNegotiationDone.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIkeSaNegotiationDone.setStatus(_B)
_JuniIkeSa2State_Type=JuniIpsecPhase1SaState
_JuniIkeSa2State_Object=MibTableColumn
juniIkeSa2State=_JuniIkeSa2State_Object((1,3,6,1,4,1,4874,2,2,71,1,1,5,1,8),_JuniIkeSa2State_Type())
juniIkeSa2State.setMaxAccess(_G)
if mibBuilder.loadTexts:juniIkeSa2State.setStatus(_B)
class _JuniIkeSa2Remaining_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_JuniIkeSa2Remaining_Type.__name__=_L
_JuniIkeSa2Remaining_Object=MibTableColumn
juniIkeSa2Remaining=_JuniIkeSa2Remaining_Object((1,3,6,1,4,1,4874,2,2,71,1,1,5,1,9),_JuniIkeSa2Remaining_Type())
juniIkeSa2Remaining.setMaxAccess(_G)
if mibBuilder.loadTexts:juniIkeSa2Remaining.setStatus(_B)
if mibBuilder.loadTexts:juniIkeSa2Remaining.setUnits(_e)
class _JuniRemoteCookie_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_JuniRemoteCookie_Type.__name__=_H
_JuniRemoteCookie_Object=MibTableColumn
juniRemoteCookie=_JuniRemoteCookie_Object((1,3,6,1,4,1,4874,2,2,71,1,1,5,1,10),_JuniRemoteCookie_Type())
juniRemoteCookie.setMaxAccess(_G)
if mibBuilder.loadTexts:juniRemoteCookie.setStatus(_B)
class _JuniLocalCookie_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_JuniLocalCookie_Type.__name__=_H
_JuniLocalCookie_Object=MibTableColumn
juniLocalCookie=_JuniLocalCookie_Object((1,3,6,1,4,1,4874,2,2,71,1,1,5,1,11),_JuniLocalCookie_Type())
juniLocalCookie.setMaxAccess(_G)
if mibBuilder.loadTexts:juniLocalCookie.setStatus(_B)
_JuniIkePolicyRuleV2Table_Object=MibTable
juniIkePolicyRuleV2Table=_JuniIkePolicyRuleV2Table_Object((1,3,6,1,4,1,4874,2,2,71,1,1,6))
if mibBuilder.loadTexts:juniIkePolicyRuleV2Table.setStatus(_B)
_JuniIkePolicyRuleV2Entry_Object=MibTableRow
juniIkePolicyRuleV2Entry=_JuniIkePolicyRuleV2Entry_Object((1,3,6,1,4,1,4874,2,2,71,1,1,6,1))
juniIkePolicyRuleV2Entry.setIndexNames((0,_A,_m))
if mibBuilder.loadTexts:juniIkePolicyRuleV2Entry.setStatus(_B)
class _JuniIkePolicyRuleV2Priority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_JuniIkePolicyRuleV2Priority_Type.__name__=_F
_JuniIkePolicyRuleV2Priority_Object=MibTableColumn
juniIkePolicyRuleV2Priority=_JuniIkePolicyRuleV2Priority_Object((1,3,6,1,4,1,4874,2,2,71,1,1,6,1,1),_JuniIkePolicyRuleV2Priority_Type())
juniIkePolicyRuleV2Priority.setMaxAccess(_E)
if mibBuilder.loadTexts:juniIkePolicyRuleV2Priority.setStatus(_B)
class _JuniIkePolicyRuleV2AuthMethod_Type(JuniIkeAuthenticationMethod):defaultValue=3
_JuniIkePolicyRuleV2AuthMethod_Type.__name__=_M
_JuniIkePolicyRuleV2AuthMethod_Object=MibTableColumn
juniIkePolicyRuleV2AuthMethod=_JuniIkePolicyRuleV2AuthMethod_Object((1,3,6,1,4,1,4874,2,2,71,1,1,6,1,2),_JuniIkePolicyRuleV2AuthMethod_Type())
juniIkePolicyRuleV2AuthMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkePolicyRuleV2AuthMethod.setStatus(_B)
class _JuniIkePolicyRuleV2EncryptMethod_Type(JuniIkeEncryptionMethod):defaultValue=1
_JuniIkePolicyRuleV2EncryptMethod_Type.__name__=_N
_JuniIkePolicyRuleV2EncryptMethod_Object=MibTableColumn
juniIkePolicyRuleV2EncryptMethod=_JuniIkePolicyRuleV2EncryptMethod_Object((1,3,6,1,4,1,4874,2,2,71,1,1,6,1,3),_JuniIkePolicyRuleV2EncryptMethod_Type())
juniIkePolicyRuleV2EncryptMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkePolicyRuleV2EncryptMethod.setStatus(_B)
class _JuniIkePolicyRuleV2PfsGroup_Type(JuniIkeGroup):defaultValue=1
_JuniIkePolicyRuleV2PfsGroup_Type.__name__=_O
_JuniIkePolicyRuleV2PfsGroup_Object=MibTableColumn
juniIkePolicyRuleV2PfsGroup=_JuniIkePolicyRuleV2PfsGroup_Object((1,3,6,1,4,1,4874,2,2,71,1,1,6,1,4),_JuniIkePolicyRuleV2PfsGroup_Type())
juniIkePolicyRuleV2PfsGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkePolicyRuleV2PfsGroup.setStatus(_B)
class _JuniIkePolicyRuleV2HashMethod_Type(JuniIkeHashMethod):defaultValue=1
_JuniIkePolicyRuleV2HashMethod_Type.__name__=_P
_JuniIkePolicyRuleV2HashMethod_Object=MibTableColumn
juniIkePolicyRuleV2HashMethod=_JuniIkePolicyRuleV2HashMethod_Object((1,3,6,1,4,1,4874,2,2,71,1,1,6,1,5),_JuniIkePolicyRuleV2HashMethod_Type())
juniIkePolicyRuleV2HashMethod.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkePolicyRuleV2HashMethod.setStatus(_B)
class _JuniIkePolicyRuleV2Lifetime_Type(Integer32):defaultValue=28800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,86400))
_JuniIkePolicyRuleV2Lifetime_Type.__name__=_F
_JuniIkePolicyRuleV2Lifetime_Object=MibTableColumn
juniIkePolicyRuleV2Lifetime=_JuniIkePolicyRuleV2Lifetime_Object((1,3,6,1,4,1,4874,2,2,71,1,1,6,1,6),_JuniIkePolicyRuleV2Lifetime_Type())
juniIkePolicyRuleV2Lifetime.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkePolicyRuleV2Lifetime.setStatus(_B)
class _JuniIkePolicyRuleV2NegotiationMode_Type(JuniIkeNegotiationV2Mode):defaultValue=3
_JuniIkePolicyRuleV2NegotiationMode_Type.__name__=_n
_JuniIkePolicyRuleV2NegotiationMode_Object=MibTableColumn
juniIkePolicyRuleV2NegotiationMode=_JuniIkePolicyRuleV2NegotiationMode_Object((1,3,6,1,4,1,4874,2,2,71,1,1,6,1,7),_JuniIkePolicyRuleV2NegotiationMode_Type())
juniIkePolicyRuleV2NegotiationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkePolicyRuleV2NegotiationMode.setStatus(_B)
_JuniIkePolicyRuleV2IpAddress_Type=IpAddress
_JuniIkePolicyRuleV2IpAddress_Object=MibTableColumn
juniIkePolicyRuleV2IpAddress=_JuniIkePolicyRuleV2IpAddress_Object((1,3,6,1,4,1,4874,2,2,71,1,1,6,1,8),_JuniIkePolicyRuleV2IpAddress_Type())
juniIkePolicyRuleV2IpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkePolicyRuleV2IpAddress.setStatus(_B)
_JuniIkePolicyRuleV2RouterIndex_Type=Unsigned32
_JuniIkePolicyRuleV2RouterIndex_Object=MibTableColumn
juniIkePolicyRuleV2RouterIndex=_JuniIkePolicyRuleV2RouterIndex_Object((1,3,6,1,4,1,4874,2,2,71,1,1,6,1,9),_JuniIkePolicyRuleV2RouterIndex_Type())
juniIkePolicyRuleV2RouterIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkePolicyRuleV2RouterIndex.setStatus(_B)
_JuniIkePolicyRuleV2RowStatus_Type=RowStatus
_JuniIkePolicyRuleV2RowStatus_Object=MibTableColumn
juniIkePolicyRuleV2RowStatus=_JuniIkePolicyRuleV2RowStatus_Object((1,3,6,1,4,1,4874,2,2,71,1,1,6,1,10),_JuniIkePolicyRuleV2RowStatus_Type())
juniIkePolicyRuleV2RowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:juniIkePolicyRuleV2RowStatus.setStatus(_B)
_JuniIkeMIBConformance_ObjectIdentity=ObjectIdentity
juniIkeMIBConformance=_JuniIkeMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,71,2))
_JuniIkeMIBCompliances_ObjectIdentity=ObjectIdentity
juniIkeMIBCompliances=_JuniIkeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,71,2,1))
_JuniIkeMIBGroups_ObjectIdentity=ObjectIdentity
juniIkeMIBGroups=_JuniIkeMIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,71,2,2))
juniIkePolicyRuleGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,71,2,2,1))
juniIkePolicyRuleGroup.setObjects(*((_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:juniIkePolicyRuleGroup.setStatus(_C)
juniIkeIpv4PreSharedKeyGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,71,2,2,2))
juniIkeIpv4PreSharedKeyGroup.setObjects(*((_A,_v),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:juniIkeIpv4PreSharedKeyGroup.setStatus(_B)
juniIkeFqdnPreSharedKeyGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,71,2,2,3))
juniIkeFqdnPreSharedKeyGroup.setObjects(*((_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:juniIkeFqdnPreSharedKeyGroup.setStatus(_B)
juniIkeSaGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,71,2,2,4))
juniIkeSaGroup.setObjects(*((_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:juniIkeSaGroup.setStatus(_C)
juniIkeSa2Group=ObjectGroup((1,3,6,1,4,1,4874,2,2,71,2,2,5))
juniIkeSa2Group.setObjects(*((_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:juniIkeSa2Group.setStatus(_B)
juniIkePolicyRuleV2Group=ObjectGroup((1,3,6,1,4,1,4874,2,2,71,2,2,6))
juniIkePolicyRuleV2Group.setObjects(*((_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:juniIkePolicyRuleV2Group.setStatus(_B)
juniIkeCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,71,2,1,1))
juniIkeCompliance.setObjects(*((_A,_Q),(_A,_J),(_A,_K),(_A,_AG)))
if mibBuilder.loadTexts:juniIkeCompliance.setStatus(_C)
juniIkeCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,71,2,1,2))
juniIkeCompliance2.setObjects(*((_A,_Q),(_A,_J),(_A,_K),(_A,_R)))
if mibBuilder.loadTexts:juniIkeCompliance2.setStatus(_C)
juniIkeCompliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,71,2,1,3))
juniIkeCompliance3.setObjects(*((_A,_AH),(_A,_J),(_A,_K),(_A,_R)))
if mibBuilder.loadTexts:juniIkeCompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_M:JuniIkeAuthenticationMethod,_N:JuniIkeEncryptionMethod,_O:JuniIkeGroup,_P:JuniIkeHashMethod,_V:JuniIkeNegotiationMode,_n:JuniIkeNegotiationV2Mode,'JuniIpsecPhase1SaState':JuniIpsecPhase1SaState,'JuniIpsecPhase1SaDirection':JuniIpsecPhase1SaDirection,'juniIkeMIB':juniIkeMIB,'juniIkeObjects':juniIkeObjects,'juniIke':juniIke,'juniIkePolicyRuleTable':juniIkePolicyRuleTable,'juniIkePolicyRuleEntry':juniIkePolicyRuleEntry,_U:juniIkePolicyRulePriority,_o:juniIkePolicyRuleAuthMethod,_p:juniIkePolicyRuleEncryptMethod,_q:juniIkePolicyRulePfsGroup,_r:juniIkePolicyRuleHashMethod,_s:juniIkePolicyRuleLifetime,_t:juniIkePolicyRuleNegotiationMode,_u:juniIkePolicyRuleRowStatus,'juniIkeIpv4PresharedKeyTable':juniIkeIpv4PresharedKeyTable,'juniIkeIpv4PresharedKeyEntry':juniIkeIpv4PresharedKeyEntry,_W:juniIkeIpv4PresharedRemoteIpAddr,_X:juniIkeIpv4PresharedRouterIdx,_v:juniIkeIpv4PresharedKeyStr,_w:juniIkeIpv4PresharedMaskedKeyStr,_x:juniIkeIpv4PresharedKeyRowStatus,'juniIkeFqdnPresharedKeyTable':juniIkeFqdnPresharedKeyTable,'juniIkeFqdnPresharedKeyEntry':juniIkeFqdnPresharedKeyEntry,_Y:juniIkeFqdnPresharedRemote,_Z:juniIkeFqdnPresharedRouterIndex,_y:juniIkeFqdnPresharedKeyStr,_z:juniIkeFqdnPresharedMaskedKeyStr,_A0:juniIkeFqdnPresharedKeyRowStatus,'juniIkeSaTable':juniIkeSaTable,'juniIkeSaEntry':juniIkeSaEntry,_a:juniIkeSaRemoteIpAddr,_b:juniIkeSaLocalIpAddr,_c:juniIkeSaRouterIndex,_d:juniIkeSaDirection,_A1:juniIkeSaState,_A2:juniIkeSaRemaining,'juniIkeSa2Table':juniIkeSa2Table,'juniIkeSa2Entry':juniIkeSa2Entry,_f:juniIkeSa2RemoteIpAddr,_g:juniIkeSaRemotePort,_h:juniIkeSa2LocalIpAddr,_i:juniIkeSaLocalPort,_j:juniIkeSa2RouterIndex,_k:juniIkeSa2Direction,_l:juniIkeSaNegotiationDone,_A3:juniIkeSa2State,_A4:juniIkeSa2Remaining,_A5:juniRemoteCookie,_A6:juniLocalCookie,'juniIkePolicyRuleV2Table':juniIkePolicyRuleV2Table,'juniIkePolicyRuleV2Entry':juniIkePolicyRuleV2Entry,_m:juniIkePolicyRuleV2Priority,_A7:juniIkePolicyRuleV2AuthMethod,_A8:juniIkePolicyRuleV2EncryptMethod,_A9:juniIkePolicyRuleV2PfsGroup,_AA:juniIkePolicyRuleV2HashMethod,_AB:juniIkePolicyRuleV2Lifetime,_AC:juniIkePolicyRuleV2NegotiationMode,_AD:juniIkePolicyRuleV2IpAddress,_AE:juniIkePolicyRuleV2RouterIndex,_AF:juniIkePolicyRuleV2RowStatus,'juniIkeMIBConformance':juniIkeMIBConformance,'juniIkeMIBCompliances':juniIkeMIBCompliances,'juniIkeCompliance':juniIkeCompliance,'juniIkeCompliance2':juniIkeCompliance2,'juniIkeCompliance3':juniIkeCompliance3,'juniIkeMIBGroups':juniIkeMIBGroups,_Q:juniIkePolicyRuleGroup,_J:juniIkeIpv4PreSharedKeyGroup,_K:juniIkeFqdnPreSharedKeyGroup,_AG:juniIkeSaGroup,_R:juniIkeSa2Group,_AH:juniIkePolicyRuleV2Group})