_Ao='alaIPsecCountersGroup'
_An='alaIPsecKeyGroup'
_Am='alaIPsecSAConfigGroup'
_Al='alaIPsecSecurityPolicyGroup'
_Ak='alaIPsecConfigGroup'
_Aj='alaIPsecStatisticsOutDiscarded'
_Ai='alaIPsecStatisticsInDiscarded'
_Ah='alaIPsecStatisticsOutNoMemory'
_Ag='alaIPsecStatisticsOutBadPacket'
_Af='alaIPsecStatisticsOutNoSA'
_Ae='alaIPsecStatisticsOutPolicyViolation'
_Ad='alaIPsecStatisticsOutSuccessful'
_Ac='alaIPsecStatisticsInNoMemory'
_Ab='alaIPsecStatisticsInBadPacket'
_Aa='alaIPsecStatisticsInESPAuthenticationFail'
_AZ='alaIPsecStatisticsInESPAuthenticationSuccess'
_AY='alaIPsecStatisticsInAHAuthenticationFail'
_AX='alaIPsecStatisticsInAHAuthenticationSuccess'
_AW='alaIPsecStatisticsInESPReplay'
_AV='alaIPsecStatisticsInAHReplay'
_AU='alaIPsecStatisticsInUnknownSPI'
_AT='alaIPsecStatisticsInNoSA'
_AS='alaIPsecStatisticsInPolicyViolation'
_AR='alaIPsecStatisticsInSuccessful'
_AQ='alaIPsecErrorsOutOther'
_AP='alaIPsecErrorsOutDiscarded'
_AO='alaIPsecErrorsOutNoSA'
_AN='alaIPsecErrorsInOther'
_AM='alaIPsecErrorsInDiscarded'
_AL='alaIPsecErrorsInAuthenticationFail'
_AK='alaIPsecErrorsInReplay'
_AJ='alaIPsecErrorsInNoSA'
_AI='alaIPsecErrorsInPolicyViolation'
_AH='alaIPsecKeyRowStatus'
_AG='alaIPsecKeyEncrypted'
_AF='alaIPsecKey'
_AE='alaIPsecKeyName'
_AD='alaIPsecKeyType'
_AC='alaIPsecSAConfigRowStatus'
_AB='alaIPsecSAConfigOperationalState'
_AA='alaIPsecSAConfigAdminState'
_A9='alaIPsecSAConfigAuthenticationAlgorithm'
_A8='alaIPsecSAConfigEncryptionKeyLength'
_A7='alaIPsecSAConfigEncryptionAlgorithm'
_A6='alaIPsecSAConfigDescription'
_A5='alaIPsecSAConfigName'
_A4='alaIPsecSAConfigSPI'
_A3='alaIPsecSAConfigDestinationType'
_A2='alaIPsecSAConfigDestination'
_A1='alaIPsecSAConfigSourceType'
_A0='alaIPsecSAConfigSource'
_z='alaIPsecSAConfigType'
_y='alaIPsecSecurityPolicyRuleRowStatus'
_x='alaIPsecSecurityPolicyRuleMode'
_w='alaIPsecSecurityPolicyRuleProtocol'
_v='alaIPsecSecurityPolicyRowStatus'
_u='alaIPsecSecurityPolicyPriority'
_t='alaIPsecSecurityPolicyOperationalState'
_s='alaIPsecSecurityPolicyAdminState'
_r='alaIPsecSecurityPolicyAction'
_q='alaIPsecSecurityPolicyDescription'
_p='alaIPsecSecurityPolicyName'
_o='alaIPsecSecurityPolicyDirection'
_n='alaIPsecSecurityPolicyICMPv6Type'
_m='alaIPsecSecurityPolicyULProtocol'
_l='alaIPsecSecurityPolicyDestinationPort'
_k='alaIPsecSecurityPolicyDestinationPrefixLength'
_j='alaIPsecSecurityPolicyDestinationType'
_i='alaIPsecSecurityPolicyDestination'
_h='alaIPsecSecurityPolicySourcePort'
_g='alaIPsecSecurityPolicySourcePrefixLength'
_f='alaIPsecSecurityPolicySourceType'
_e='alaIPsecSecurityPolicySource'
_d='alaIPsecSecurityKeyNew'
_c='alaIPsecSecurityKeyCurrent'
_b='alaIPsecErrorsProtocol'
_a='alaIPsecKeyID'
_Z='IPsecAHAlgorithm'
_Y='IPsecESPAlgorithm'
_X='alaIPsecSAConfigID'
_W='alaIPsecSecurityPolicyRuleIndex'
_V='IPsecULProtocol'
_U='alaIPsecStatisticsProtocol'
_T='read-write'
_S='alaIPsecSecurityKeyID'
_R='disabled'
_Q='enabled'
_P='TruthValue'
_O='IPsecAdminState'
_N='IPsecDescription'
_M='IPsecPortNumber'
_L='alaIPsecSecurityPolicyID'
_K='none'
_J='Unsigned32'
_I='SnmpAdminString'
_H='OctetString'
_G='not-accessible'
_F='Integer32'
_E='deprecated'
_D='read-only'
_C='read-create'
_B='ALCATEL-ENT1-IPSEC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1IPsec,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','softentIND1IPsec')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_P)
alcatelIND1IPsecMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,43,1))
if mibBuilder.loadTexts:alcatelIND1IPsecMIB.setRevisions(('2010-07-20 00:00',))
class IPsecDescription(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,200))
class IPsecPortNumber(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class IPsecPrefixLength(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
class IPsecULProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class IPsecAdminState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
class IPsecSAType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('ah',2),('esp',3)))
class IPsecESPAlgorithm(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,11,12,13)));namedValues=NamedValues(*((_K,0),('descbc',2),('des3cbc',3),('null',11),('aescbc',12),('aesctr',13)))
class IPsecAHAlgorithm(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,9)));namedValues=NamedValues(*((_K,0),('hmacmd5',2),('hmacsha1',3),('aesxcbcmac',9)))
class IPsecOperationalState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),('dnspending',3)))
_AlcatelIND1IPsecMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1IPsecMIBObjects=_AlcatelIND1IPsecMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,43,1,1))
_AlaIPsecConfig_ObjectIdentity=ObjectIdentity
alaIPsecConfig=_AlaIPsecConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1))
_AlaIPsecSecurityKeyTable_Object=MibTable
alaIPsecSecurityKeyTable=_AlaIPsecSecurityKeyTable_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,1))
if mibBuilder.loadTexts:alaIPsecSecurityKeyTable.setStatus(_A)
_AlaIPsecSecurityKeyEntry_Object=MibTableRow
alaIPsecSecurityKeyEntry=_AlaIPsecSecurityKeyEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,1,1))
alaIPsecSecurityKeyEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:alaIPsecSecurityKeyEntry.setStatus(_A)
_AlaIPsecSecurityKeyID_Type=Unsigned32
_AlaIPsecSecurityKeyID_Object=MibTableColumn
alaIPsecSecurityKeyID=_AlaIPsecSecurityKeyID_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,1,1,1),_AlaIPsecSecurityKeyID_Type())
alaIPsecSecurityKeyID.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIPsecSecurityKeyID.setStatus(_A)
class _AlaIPsecSecurityKeyCurrent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AlaIPsecSecurityKeyCurrent_Type.__name__=_H
_AlaIPsecSecurityKeyCurrent_Object=MibTableColumn
alaIPsecSecurityKeyCurrent=_AlaIPsecSecurityKeyCurrent_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,1,1,2),_AlaIPsecSecurityKeyCurrent_Type())
alaIPsecSecurityKeyCurrent.setMaxAccess(_T)
if mibBuilder.loadTexts:alaIPsecSecurityKeyCurrent.setStatus(_A)
class _AlaIPsecSecurityKeyNew_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_AlaIPsecSecurityKeyNew_Type.__name__=_H
_AlaIPsecSecurityKeyNew_Object=MibTableColumn
alaIPsecSecurityKeyNew=_AlaIPsecSecurityKeyNew_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,1,1,3),_AlaIPsecSecurityKeyNew_Type())
alaIPsecSecurityKeyNew.setMaxAccess(_T)
if mibBuilder.loadTexts:alaIPsecSecurityKeyNew.setStatus(_A)
_AlaIPsecStatisticsTable_Object=MibTable
alaIPsecStatisticsTable=_AlaIPsecStatisticsTable_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2))
if mibBuilder.loadTexts:alaIPsecStatisticsTable.setStatus(_E)
_AlaIPsecStatisticsEntry_Object=MibTableRow
alaIPsecStatisticsEntry=_AlaIPsecStatisticsEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1))
alaIPsecStatisticsEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:alaIPsecStatisticsEntry.setStatus(_E)
class _AlaIPsecStatisticsProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(6));namedValues=NamedValues(('ipv6',6))
_AlaIPsecStatisticsProtocol_Type.__name__=_F
_AlaIPsecStatisticsProtocol_Object=MibTableColumn
alaIPsecStatisticsProtocol=_AlaIPsecStatisticsProtocol_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1,1),_AlaIPsecStatisticsProtocol_Type())
alaIPsecStatisticsProtocol.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIPsecStatisticsProtocol.setStatus(_E)
_AlaIPsecStatisticsInSuccessful_Type=Counter32
_AlaIPsecStatisticsInSuccessful_Object=MibTableColumn
alaIPsecStatisticsInSuccessful=_AlaIPsecStatisticsInSuccessful_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1,2),_AlaIPsecStatisticsInSuccessful_Type())
alaIPsecStatisticsInSuccessful.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecStatisticsInSuccessful.setStatus(_E)
_AlaIPsecStatisticsInPolicyViolation_Type=Counter32
_AlaIPsecStatisticsInPolicyViolation_Object=MibTableColumn
alaIPsecStatisticsInPolicyViolation=_AlaIPsecStatisticsInPolicyViolation_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1,3),_AlaIPsecStatisticsInPolicyViolation_Type())
alaIPsecStatisticsInPolicyViolation.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecStatisticsInPolicyViolation.setStatus(_E)
_AlaIPsecStatisticsInNoSA_Type=Counter32
_AlaIPsecStatisticsInNoSA_Object=MibTableColumn
alaIPsecStatisticsInNoSA=_AlaIPsecStatisticsInNoSA_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1,4),_AlaIPsecStatisticsInNoSA_Type())
alaIPsecStatisticsInNoSA.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecStatisticsInNoSA.setStatus(_E)
_AlaIPsecStatisticsInUnknownSPI_Type=Counter32
_AlaIPsecStatisticsInUnknownSPI_Object=MibTableColumn
alaIPsecStatisticsInUnknownSPI=_AlaIPsecStatisticsInUnknownSPI_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1,5),_AlaIPsecStatisticsInUnknownSPI_Type())
alaIPsecStatisticsInUnknownSPI.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecStatisticsInUnknownSPI.setStatus(_E)
_AlaIPsecStatisticsInAHReplay_Type=Counter32
_AlaIPsecStatisticsInAHReplay_Object=MibTableColumn
alaIPsecStatisticsInAHReplay=_AlaIPsecStatisticsInAHReplay_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1,6),_AlaIPsecStatisticsInAHReplay_Type())
alaIPsecStatisticsInAHReplay.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecStatisticsInAHReplay.setStatus(_E)
_AlaIPsecStatisticsInESPReplay_Type=Counter32
_AlaIPsecStatisticsInESPReplay_Object=MibTableColumn
alaIPsecStatisticsInESPReplay=_AlaIPsecStatisticsInESPReplay_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1,7),_AlaIPsecStatisticsInESPReplay_Type())
alaIPsecStatisticsInESPReplay.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecStatisticsInESPReplay.setStatus(_E)
_AlaIPsecStatisticsInAHAuthenticationSuccess_Type=Counter32
_AlaIPsecStatisticsInAHAuthenticationSuccess_Object=MibTableColumn
alaIPsecStatisticsInAHAuthenticationSuccess=_AlaIPsecStatisticsInAHAuthenticationSuccess_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1,8),_AlaIPsecStatisticsInAHAuthenticationSuccess_Type())
alaIPsecStatisticsInAHAuthenticationSuccess.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecStatisticsInAHAuthenticationSuccess.setStatus(_E)
_AlaIPsecStatisticsInAHAuthenticationFail_Type=Counter32
_AlaIPsecStatisticsInAHAuthenticationFail_Object=MibTableColumn
alaIPsecStatisticsInAHAuthenticationFail=_AlaIPsecStatisticsInAHAuthenticationFail_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1,9),_AlaIPsecStatisticsInAHAuthenticationFail_Type())
alaIPsecStatisticsInAHAuthenticationFail.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecStatisticsInAHAuthenticationFail.setStatus(_E)
_AlaIPsecStatisticsInESPAuthenticationSuccess_Type=Counter32
_AlaIPsecStatisticsInESPAuthenticationSuccess_Object=MibTableColumn
alaIPsecStatisticsInESPAuthenticationSuccess=_AlaIPsecStatisticsInESPAuthenticationSuccess_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1,10),_AlaIPsecStatisticsInESPAuthenticationSuccess_Type())
alaIPsecStatisticsInESPAuthenticationSuccess.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecStatisticsInESPAuthenticationSuccess.setStatus(_E)
_AlaIPsecStatisticsInESPAuthenticationFail_Type=Counter32
_AlaIPsecStatisticsInESPAuthenticationFail_Object=MibTableColumn
alaIPsecStatisticsInESPAuthenticationFail=_AlaIPsecStatisticsInESPAuthenticationFail_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1,11),_AlaIPsecStatisticsInESPAuthenticationFail_Type())
alaIPsecStatisticsInESPAuthenticationFail.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecStatisticsInESPAuthenticationFail.setStatus(_E)
_AlaIPsecStatisticsInBadPacket_Type=Counter32
_AlaIPsecStatisticsInBadPacket_Object=MibTableColumn
alaIPsecStatisticsInBadPacket=_AlaIPsecStatisticsInBadPacket_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1,12),_AlaIPsecStatisticsInBadPacket_Type())
alaIPsecStatisticsInBadPacket.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecStatisticsInBadPacket.setStatus(_E)
_AlaIPsecStatisticsInNoMemory_Type=Counter32
_AlaIPsecStatisticsInNoMemory_Object=MibTableColumn
alaIPsecStatisticsInNoMemory=_AlaIPsecStatisticsInNoMemory_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1,13),_AlaIPsecStatisticsInNoMemory_Type())
alaIPsecStatisticsInNoMemory.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecStatisticsInNoMemory.setStatus(_E)
_AlaIPsecStatisticsOutSuccessful_Type=Counter32
_AlaIPsecStatisticsOutSuccessful_Object=MibTableColumn
alaIPsecStatisticsOutSuccessful=_AlaIPsecStatisticsOutSuccessful_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1,14),_AlaIPsecStatisticsOutSuccessful_Type())
alaIPsecStatisticsOutSuccessful.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecStatisticsOutSuccessful.setStatus(_E)
_AlaIPsecStatisticsOutPolicyViolation_Type=Counter32
_AlaIPsecStatisticsOutPolicyViolation_Object=MibTableColumn
alaIPsecStatisticsOutPolicyViolation=_AlaIPsecStatisticsOutPolicyViolation_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1,15),_AlaIPsecStatisticsOutPolicyViolation_Type())
alaIPsecStatisticsOutPolicyViolation.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecStatisticsOutPolicyViolation.setStatus(_E)
_AlaIPsecStatisticsOutNoSA_Type=Counter32
_AlaIPsecStatisticsOutNoSA_Object=MibTableColumn
alaIPsecStatisticsOutNoSA=_AlaIPsecStatisticsOutNoSA_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1,16),_AlaIPsecStatisticsOutNoSA_Type())
alaIPsecStatisticsOutNoSA.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecStatisticsOutNoSA.setStatus(_E)
_AlaIPsecStatisticsOutBadPacket_Type=Counter32
_AlaIPsecStatisticsOutBadPacket_Object=MibTableColumn
alaIPsecStatisticsOutBadPacket=_AlaIPsecStatisticsOutBadPacket_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1,17),_AlaIPsecStatisticsOutBadPacket_Type())
alaIPsecStatisticsOutBadPacket.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecStatisticsOutBadPacket.setStatus(_E)
_AlaIPsecStatisticsOutNoMemory_Type=Counter32
_AlaIPsecStatisticsOutNoMemory_Object=MibTableColumn
alaIPsecStatisticsOutNoMemory=_AlaIPsecStatisticsOutNoMemory_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1,18),_AlaIPsecStatisticsOutNoMemory_Type())
alaIPsecStatisticsOutNoMemory.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecStatisticsOutNoMemory.setStatus(_E)
_AlaIPsecStatisticsInDiscarded_Type=Counter32
_AlaIPsecStatisticsInDiscarded_Object=MibTableColumn
alaIPsecStatisticsInDiscarded=_AlaIPsecStatisticsInDiscarded_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1,19),_AlaIPsecStatisticsInDiscarded_Type())
alaIPsecStatisticsInDiscarded.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecStatisticsInDiscarded.setStatus(_E)
_AlaIPsecStatisticsOutDiscarded_Type=Counter32
_AlaIPsecStatisticsOutDiscarded_Object=MibTableColumn
alaIPsecStatisticsOutDiscarded=_AlaIPsecStatisticsOutDiscarded_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,1,2,1,20),_AlaIPsecStatisticsOutDiscarded_Type())
alaIPsecStatisticsOutDiscarded.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecStatisticsOutDiscarded.setStatus(_E)
_AlaIPsecSecurityPolicyTable_Object=MibTable
alaIPsecSecurityPolicyTable=_AlaIPsecSecurityPolicyTable_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2))
if mibBuilder.loadTexts:alaIPsecSecurityPolicyTable.setStatus(_A)
_AlaIPsecSecurityPolicyEntry_Object=MibTableRow
alaIPsecSecurityPolicyEntry=_AlaIPsecSecurityPolicyEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2,1))
alaIPsecSecurityPolicyEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:alaIPsecSecurityPolicyEntry.setStatus(_A)
_AlaIPsecSecurityPolicyID_Type=Unsigned32
_AlaIPsecSecurityPolicyID_Object=MibTableColumn
alaIPsecSecurityPolicyID=_AlaIPsecSecurityPolicyID_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2,1,1),_AlaIPsecSecurityPolicyID_Type())
alaIPsecSecurityPolicyID.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIPsecSecurityPolicyID.setStatus(_A)
_AlaIPsecSecurityPolicySourceType_Type=InetAddressType
_AlaIPsecSecurityPolicySourceType_Object=MibTableColumn
alaIPsecSecurityPolicySourceType=_AlaIPsecSecurityPolicySourceType_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2,1,2),_AlaIPsecSecurityPolicySourceType_Type())
alaIPsecSecurityPolicySourceType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSecurityPolicySourceType.setStatus(_A)
_AlaIPsecSecurityPolicySource_Type=InetAddress
_AlaIPsecSecurityPolicySource_Object=MibTableColumn
alaIPsecSecurityPolicySource=_AlaIPsecSecurityPolicySource_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2,1,3),_AlaIPsecSecurityPolicySource_Type())
alaIPsecSecurityPolicySource.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSecurityPolicySource.setStatus(_A)
_AlaIPsecSecurityPolicySourcePrefixLength_Type=IPsecPrefixLength
_AlaIPsecSecurityPolicySourcePrefixLength_Object=MibTableColumn
alaIPsecSecurityPolicySourcePrefixLength=_AlaIPsecSecurityPolicySourcePrefixLength_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2,1,4),_AlaIPsecSecurityPolicySourcePrefixLength_Type())
alaIPsecSecurityPolicySourcePrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSecurityPolicySourcePrefixLength.setStatus(_A)
class _AlaIPsecSecurityPolicySourcePort_Type(IPsecPortNumber):defaultValue=0
_AlaIPsecSecurityPolicySourcePort_Type.__name__=_M
_AlaIPsecSecurityPolicySourcePort_Object=MibTableColumn
alaIPsecSecurityPolicySourcePort=_AlaIPsecSecurityPolicySourcePort_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2,1,5),_AlaIPsecSecurityPolicySourcePort_Type())
alaIPsecSecurityPolicySourcePort.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSecurityPolicySourcePort.setStatus(_A)
_AlaIPsecSecurityPolicyDestinationType_Type=InetAddressType
_AlaIPsecSecurityPolicyDestinationType_Object=MibTableColumn
alaIPsecSecurityPolicyDestinationType=_AlaIPsecSecurityPolicyDestinationType_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2,1,6),_AlaIPsecSecurityPolicyDestinationType_Type())
alaIPsecSecurityPolicyDestinationType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSecurityPolicyDestinationType.setStatus(_A)
_AlaIPsecSecurityPolicyDestination_Type=InetAddress
_AlaIPsecSecurityPolicyDestination_Object=MibTableColumn
alaIPsecSecurityPolicyDestination=_AlaIPsecSecurityPolicyDestination_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2,1,7),_AlaIPsecSecurityPolicyDestination_Type())
alaIPsecSecurityPolicyDestination.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSecurityPolicyDestination.setStatus(_A)
_AlaIPsecSecurityPolicyDestinationPrefixLength_Type=IPsecPrefixLength
_AlaIPsecSecurityPolicyDestinationPrefixLength_Object=MibTableColumn
alaIPsecSecurityPolicyDestinationPrefixLength=_AlaIPsecSecurityPolicyDestinationPrefixLength_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2,1,8),_AlaIPsecSecurityPolicyDestinationPrefixLength_Type())
alaIPsecSecurityPolicyDestinationPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSecurityPolicyDestinationPrefixLength.setStatus(_A)
class _AlaIPsecSecurityPolicyDestinationPort_Type(IPsecPortNumber):defaultValue=0
_AlaIPsecSecurityPolicyDestinationPort_Type.__name__=_M
_AlaIPsecSecurityPolicyDestinationPort_Object=MibTableColumn
alaIPsecSecurityPolicyDestinationPort=_AlaIPsecSecurityPolicyDestinationPort_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2,1,9),_AlaIPsecSecurityPolicyDestinationPort_Type())
alaIPsecSecurityPolicyDestinationPort.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSecurityPolicyDestinationPort.setStatus(_A)
class _AlaIPsecSecurityPolicyULProtocol_Type(IPsecULProtocol):defaultValue=255
_AlaIPsecSecurityPolicyULProtocol_Type.__name__=_V
_AlaIPsecSecurityPolicyULProtocol_Object=MibTableColumn
alaIPsecSecurityPolicyULProtocol=_AlaIPsecSecurityPolicyULProtocol_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2,1,10),_AlaIPsecSecurityPolicyULProtocol_Type())
alaIPsecSecurityPolicyULProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSecurityPolicyULProtocol.setStatus(_A)
class _AlaIPsecSecurityPolicyICMPv6Type_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AlaIPsecSecurityPolicyICMPv6Type_Type.__name__=_F
_AlaIPsecSecurityPolicyICMPv6Type_Object=MibTableColumn
alaIPsecSecurityPolicyICMPv6Type=_AlaIPsecSecurityPolicyICMPv6Type_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2,1,11),_AlaIPsecSecurityPolicyICMPv6Type_Type())
alaIPsecSecurityPolicyICMPv6Type.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSecurityPolicyICMPv6Type.setStatus(_A)
class _AlaIPsecSecurityPolicyDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_AlaIPsecSecurityPolicyDirection_Type.__name__=_F
_AlaIPsecSecurityPolicyDirection_Object=MibTableColumn
alaIPsecSecurityPolicyDirection=_AlaIPsecSecurityPolicyDirection_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2,1,12),_AlaIPsecSecurityPolicyDirection_Type())
alaIPsecSecurityPolicyDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSecurityPolicyDirection.setStatus(_A)
class _AlaIPsecSecurityPolicyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_AlaIPsecSecurityPolicyName_Type.__name__=_I
_AlaIPsecSecurityPolicyName_Object=MibTableColumn
alaIPsecSecurityPolicyName=_AlaIPsecSecurityPolicyName_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2,1,13),_AlaIPsecSecurityPolicyName_Type())
alaIPsecSecurityPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSecurityPolicyName.setStatus(_A)
class _AlaIPsecSecurityPolicyDescription_Type(IPsecDescription):defaultValue=OctetString('')
_AlaIPsecSecurityPolicyDescription_Type.__name__=_N
_AlaIPsecSecurityPolicyDescription_Object=MibTableColumn
alaIPsecSecurityPolicyDescription=_AlaIPsecSecurityPolicyDescription_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2,1,14),_AlaIPsecSecurityPolicyDescription_Type())
alaIPsecSecurityPolicyDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSecurityPolicyDescription.setStatus(_A)
class _AlaIPsecSecurityPolicyAction_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('discard',0),(_K,1),('ipsec',2)))
_AlaIPsecSecurityPolicyAction_Type.__name__=_F
_AlaIPsecSecurityPolicyAction_Object=MibTableColumn
alaIPsecSecurityPolicyAction=_AlaIPsecSecurityPolicyAction_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2,1,15),_AlaIPsecSecurityPolicyAction_Type())
alaIPsecSecurityPolicyAction.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSecurityPolicyAction.setStatus(_A)
class _AlaIPsecSecurityPolicyAdminState_Type(IPsecAdminState):defaultValue=1
_AlaIPsecSecurityPolicyAdminState_Type.__name__=_O
_AlaIPsecSecurityPolicyAdminState_Object=MibTableColumn
alaIPsecSecurityPolicyAdminState=_AlaIPsecSecurityPolicyAdminState_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2,1,16),_AlaIPsecSecurityPolicyAdminState_Type())
alaIPsecSecurityPolicyAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSecurityPolicyAdminState.setStatus(_A)
_AlaIPsecSecurityPolicyOperationalState_Type=IPsecOperationalState
_AlaIPsecSecurityPolicyOperationalState_Object=MibTableColumn
alaIPsecSecurityPolicyOperationalState=_AlaIPsecSecurityPolicyOperationalState_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2,1,17),_AlaIPsecSecurityPolicyOperationalState_Type())
alaIPsecSecurityPolicyOperationalState.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecSecurityPolicyOperationalState.setStatus(_A)
class _AlaIPsecSecurityPolicyPriority_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_AlaIPsecSecurityPolicyPriority_Type.__name__=_F
_AlaIPsecSecurityPolicyPriority_Object=MibTableColumn
alaIPsecSecurityPolicyPriority=_AlaIPsecSecurityPolicyPriority_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2,1,18),_AlaIPsecSecurityPolicyPriority_Type())
alaIPsecSecurityPolicyPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSecurityPolicyPriority.setStatus(_A)
_AlaIPsecSecurityPolicyRowStatus_Type=RowStatus
_AlaIPsecSecurityPolicyRowStatus_Object=MibTableColumn
alaIPsecSecurityPolicyRowStatus=_AlaIPsecSecurityPolicyRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,2,1,19),_AlaIPsecSecurityPolicyRowStatus_Type())
alaIPsecSecurityPolicyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSecurityPolicyRowStatus.setStatus(_A)
_AlaIPsecSecurityPolicyRuleTable_Object=MibTable
alaIPsecSecurityPolicyRuleTable=_AlaIPsecSecurityPolicyRuleTable_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,3))
if mibBuilder.loadTexts:alaIPsecSecurityPolicyRuleTable.setStatus(_A)
_AlaIPsecSecurityPolicyRuleEntry_Object=MibTableRow
alaIPsecSecurityPolicyRuleEntry=_AlaIPsecSecurityPolicyRuleEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,3,1))
alaIPsecSecurityPolicyRuleEntry.setIndexNames((0,_B,_L),(0,_B,_W))
if mibBuilder.loadTexts:alaIPsecSecurityPolicyRuleEntry.setStatus(_A)
class _AlaIPsecSecurityPolicyRuleIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AlaIPsecSecurityPolicyRuleIndex_Type.__name__=_J
_AlaIPsecSecurityPolicyRuleIndex_Object=MibTableColumn
alaIPsecSecurityPolicyRuleIndex=_AlaIPsecSecurityPolicyRuleIndex_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,3,1,1),_AlaIPsecSecurityPolicyRuleIndex_Type())
alaIPsecSecurityPolicyRuleIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIPsecSecurityPolicyRuleIndex.setStatus(_A)
class _AlaIPsecSecurityPolicyRuleProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ah',1),('esp',2)))
_AlaIPsecSecurityPolicyRuleProtocol_Type.__name__=_F
_AlaIPsecSecurityPolicyRuleProtocol_Object=MibTableColumn
alaIPsecSecurityPolicyRuleProtocol=_AlaIPsecSecurityPolicyRuleProtocol_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,3,1,2),_AlaIPsecSecurityPolicyRuleProtocol_Type())
alaIPsecSecurityPolicyRuleProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSecurityPolicyRuleProtocol.setStatus(_A)
class _AlaIPsecSecurityPolicyRuleMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('transport',1))
_AlaIPsecSecurityPolicyRuleMode_Type.__name__=_F
_AlaIPsecSecurityPolicyRuleMode_Object=MibTableColumn
alaIPsecSecurityPolicyRuleMode=_AlaIPsecSecurityPolicyRuleMode_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,3,1,3),_AlaIPsecSecurityPolicyRuleMode_Type())
alaIPsecSecurityPolicyRuleMode.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSecurityPolicyRuleMode.setStatus(_A)
_AlaIPsecSecurityPolicyRuleRowStatus_Type=RowStatus
_AlaIPsecSecurityPolicyRuleRowStatus_Object=MibTableColumn
alaIPsecSecurityPolicyRuleRowStatus=_AlaIPsecSecurityPolicyRuleRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,3,1,4),_AlaIPsecSecurityPolicyRuleRowStatus_Type())
alaIPsecSecurityPolicyRuleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSecurityPolicyRuleRowStatus.setStatus(_A)
_AlaIPsecSAConfigTable_Object=MibTable
alaIPsecSAConfigTable=_AlaIPsecSAConfigTable_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,4))
if mibBuilder.loadTexts:alaIPsecSAConfigTable.setStatus(_A)
_AlaIPsecSAConfigEntry_Object=MibTableRow
alaIPsecSAConfigEntry=_AlaIPsecSAConfigEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,4,1))
alaIPsecSAConfigEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:alaIPsecSAConfigEntry.setStatus(_A)
_AlaIPsecSAConfigID_Type=Unsigned32
_AlaIPsecSAConfigID_Object=MibTableColumn
alaIPsecSAConfigID=_AlaIPsecSAConfigID_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,4,1,1),_AlaIPsecSAConfigID_Type())
alaIPsecSAConfigID.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIPsecSAConfigID.setStatus(_A)
_AlaIPsecSAConfigType_Type=IPsecSAType
_AlaIPsecSAConfigType_Object=MibTableColumn
alaIPsecSAConfigType=_AlaIPsecSAConfigType_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,4,1,2),_AlaIPsecSAConfigType_Type())
alaIPsecSAConfigType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSAConfigType.setStatus(_A)
_AlaIPsecSAConfigSourceType_Type=InetAddressType
_AlaIPsecSAConfigSourceType_Object=MibTableColumn
alaIPsecSAConfigSourceType=_AlaIPsecSAConfigSourceType_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,4,1,3),_AlaIPsecSAConfigSourceType_Type())
alaIPsecSAConfigSourceType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSAConfigSourceType.setStatus(_A)
_AlaIPsecSAConfigSource_Type=InetAddress
_AlaIPsecSAConfigSource_Object=MibTableColumn
alaIPsecSAConfigSource=_AlaIPsecSAConfigSource_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,4,1,4),_AlaIPsecSAConfigSource_Type())
alaIPsecSAConfigSource.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSAConfigSource.setStatus(_A)
_AlaIPsecSAConfigDestinationType_Type=InetAddressType
_AlaIPsecSAConfigDestinationType_Object=MibTableColumn
alaIPsecSAConfigDestinationType=_AlaIPsecSAConfigDestinationType_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,4,1,5),_AlaIPsecSAConfigDestinationType_Type())
alaIPsecSAConfigDestinationType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSAConfigDestinationType.setStatus(_A)
_AlaIPsecSAConfigDestination_Type=InetAddress
_AlaIPsecSAConfigDestination_Object=MibTableColumn
alaIPsecSAConfigDestination=_AlaIPsecSAConfigDestination_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,4,1,6),_AlaIPsecSAConfigDestination_Type())
alaIPsecSAConfigDestination.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSAConfigDestination.setStatus(_A)
_AlaIPsecSAConfigSPI_Type=Unsigned32
_AlaIPsecSAConfigSPI_Object=MibTableColumn
alaIPsecSAConfigSPI=_AlaIPsecSAConfigSPI_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,4,1,7),_AlaIPsecSAConfigSPI_Type())
alaIPsecSAConfigSPI.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSAConfigSPI.setStatus(_A)
class _AlaIPsecSAConfigName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_AlaIPsecSAConfigName_Type.__name__=_I
_AlaIPsecSAConfigName_Object=MibTableColumn
alaIPsecSAConfigName=_AlaIPsecSAConfigName_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,4,1,8),_AlaIPsecSAConfigName_Type())
alaIPsecSAConfigName.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSAConfigName.setStatus(_A)
class _AlaIPsecSAConfigDescription_Type(IPsecDescription):defaultValue=OctetString('')
_AlaIPsecSAConfigDescription_Type.__name__=_N
_AlaIPsecSAConfigDescription_Object=MibTableColumn
alaIPsecSAConfigDescription=_AlaIPsecSAConfigDescription_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,4,1,9),_AlaIPsecSAConfigDescription_Type())
alaIPsecSAConfigDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSAConfigDescription.setStatus(_A)
class _AlaIPsecSAConfigEncryptionAlgorithm_Type(IPsecESPAlgorithm):defaultValue=0
_AlaIPsecSAConfigEncryptionAlgorithm_Type.__name__=_Y
_AlaIPsecSAConfigEncryptionAlgorithm_Object=MibTableColumn
alaIPsecSAConfigEncryptionAlgorithm=_AlaIPsecSAConfigEncryptionAlgorithm_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,4,1,10),_AlaIPsecSAConfigEncryptionAlgorithm_Type())
alaIPsecSAConfigEncryptionAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSAConfigEncryptionAlgorithm.setStatus(_A)
class _AlaIPsecSAConfigEncryptionKeyLength_Type(Unsigned32):defaultValue=0
_AlaIPsecSAConfigEncryptionKeyLength_Type.__name__=_J
_AlaIPsecSAConfigEncryptionKeyLength_Object=MibTableColumn
alaIPsecSAConfigEncryptionKeyLength=_AlaIPsecSAConfigEncryptionKeyLength_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,4,1,11),_AlaIPsecSAConfigEncryptionKeyLength_Type())
alaIPsecSAConfigEncryptionKeyLength.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSAConfigEncryptionKeyLength.setStatus(_A)
if mibBuilder.loadTexts:alaIPsecSAConfigEncryptionKeyLength.setUnits('bits')
class _AlaIPsecSAConfigAuthenticationAlgorithm_Type(IPsecAHAlgorithm):defaultValue=0
_AlaIPsecSAConfigAuthenticationAlgorithm_Type.__name__=_Z
_AlaIPsecSAConfigAuthenticationAlgorithm_Object=MibTableColumn
alaIPsecSAConfigAuthenticationAlgorithm=_AlaIPsecSAConfigAuthenticationAlgorithm_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,4,1,12),_AlaIPsecSAConfigAuthenticationAlgorithm_Type())
alaIPsecSAConfigAuthenticationAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSAConfigAuthenticationAlgorithm.setStatus(_A)
class _AlaIPsecSAConfigAdminState_Type(IPsecAdminState):defaultValue=1
_AlaIPsecSAConfigAdminState_Type.__name__=_O
_AlaIPsecSAConfigAdminState_Object=MibTableColumn
alaIPsecSAConfigAdminState=_AlaIPsecSAConfigAdminState_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,4,1,13),_AlaIPsecSAConfigAdminState_Type())
alaIPsecSAConfigAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSAConfigAdminState.setStatus(_A)
_AlaIPsecSAConfigOperationalState_Type=IPsecOperationalState
_AlaIPsecSAConfigOperationalState_Object=MibTableColumn
alaIPsecSAConfigOperationalState=_AlaIPsecSAConfigOperationalState_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,4,1,14),_AlaIPsecSAConfigOperationalState_Type())
alaIPsecSAConfigOperationalState.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecSAConfigOperationalState.setStatus(_A)
_AlaIPsecSAConfigRowStatus_Type=RowStatus
_AlaIPsecSAConfigRowStatus_Object=MibTableColumn
alaIPsecSAConfigRowStatus=_AlaIPsecSAConfigRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,4,1,15),_AlaIPsecSAConfigRowStatus_Type())
alaIPsecSAConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecSAConfigRowStatus.setStatus(_A)
_AlaIPsecKeyTable_Object=MibTable
alaIPsecKeyTable=_AlaIPsecKeyTable_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,5))
if mibBuilder.loadTexts:alaIPsecKeyTable.setStatus(_A)
_AlaIPsecKeyEntry_Object=MibTableRow
alaIPsecKeyEntry=_AlaIPsecKeyEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,5,1))
alaIPsecKeyEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:alaIPsecKeyEntry.setStatus(_A)
_AlaIPsecKeyID_Type=Unsigned32
_AlaIPsecKeyID_Object=MibTableColumn
alaIPsecKeyID=_AlaIPsecKeyID_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,5,1,1),_AlaIPsecKeyID_Type())
alaIPsecKeyID.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIPsecKeyID.setStatus(_A)
class _AlaIPsecKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('saAuthentication',1),('saEncryption',2)))
_AlaIPsecKeyType_Type.__name__=_F
_AlaIPsecKeyType_Object=MibTableColumn
alaIPsecKeyType=_AlaIPsecKeyType_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,5,1,2),_AlaIPsecKeyType_Type())
alaIPsecKeyType.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecKeyType.setStatus(_A)
class _AlaIPsecKeyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AlaIPsecKeyName_Type.__name__=_H
_AlaIPsecKeyName_Object=MibTableColumn
alaIPsecKeyName=_AlaIPsecKeyName_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,5,1,3),_AlaIPsecKeyName_Type())
alaIPsecKeyName.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecKeyName.setStatus(_A)
_AlaIPsecKey_Type=OctetString
_AlaIPsecKey_Object=MibTableColumn
alaIPsecKey=_AlaIPsecKey_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,5,1,4),_AlaIPsecKey_Type())
alaIPsecKey.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecKey.setStatus(_A)
class _AlaIPsecKeyEncrypted_Type(TruthValue):defaultValue=2
_AlaIPsecKeyEncrypted_Type.__name__=_P
_AlaIPsecKeyEncrypted_Object=MibTableColumn
alaIPsecKeyEncrypted=_AlaIPsecKeyEncrypted_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,5,1,5),_AlaIPsecKeyEncrypted_Type())
alaIPsecKeyEncrypted.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecKeyEncrypted.setStatus(_A)
_AlaIPsecKeyRowStatus_Type=RowStatus
_AlaIPsecKeyRowStatus_Object=MibTableColumn
alaIPsecKeyRowStatus=_AlaIPsecKeyRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,5,1,6),_AlaIPsecKeyRowStatus_Type())
alaIPsecKeyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alaIPsecKeyRowStatus.setStatus(_A)
_AlaIPsecErrorsTable_Object=MibTable
alaIPsecErrorsTable=_AlaIPsecErrorsTable_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,6))
if mibBuilder.loadTexts:alaIPsecErrorsTable.setStatus(_A)
_AlaIPsecErrorsEntry_Object=MibTableRow
alaIPsecErrorsEntry=_AlaIPsecErrorsEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,6,1))
alaIPsecErrorsEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:alaIPsecErrorsEntry.setStatus(_A)
class _AlaIPsecErrorsProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(6));namedValues=NamedValues(('ipv6',6))
_AlaIPsecErrorsProtocol_Type.__name__=_F
_AlaIPsecErrorsProtocol_Object=MibTableColumn
alaIPsecErrorsProtocol=_AlaIPsecErrorsProtocol_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,6,1,1),_AlaIPsecErrorsProtocol_Type())
alaIPsecErrorsProtocol.setMaxAccess(_G)
if mibBuilder.loadTexts:alaIPsecErrorsProtocol.setStatus(_A)
_AlaIPsecErrorsInPolicyViolation_Type=Counter32
_AlaIPsecErrorsInPolicyViolation_Object=MibTableColumn
alaIPsecErrorsInPolicyViolation=_AlaIPsecErrorsInPolicyViolation_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,6,1,2),_AlaIPsecErrorsInPolicyViolation_Type())
alaIPsecErrorsInPolicyViolation.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecErrorsInPolicyViolation.setStatus(_A)
_AlaIPsecErrorsInNoSA_Type=Counter32
_AlaIPsecErrorsInNoSA_Object=MibTableColumn
alaIPsecErrorsInNoSA=_AlaIPsecErrorsInNoSA_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,6,1,3),_AlaIPsecErrorsInNoSA_Type())
alaIPsecErrorsInNoSA.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecErrorsInNoSA.setStatus(_A)
_AlaIPsecErrorsInReplay_Type=Counter32
_AlaIPsecErrorsInReplay_Object=MibTableColumn
alaIPsecErrorsInReplay=_AlaIPsecErrorsInReplay_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,6,1,4),_AlaIPsecErrorsInReplay_Type())
alaIPsecErrorsInReplay.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecErrorsInReplay.setStatus(_A)
_AlaIPsecErrorsInAuthenticationFail_Type=Counter32
_AlaIPsecErrorsInAuthenticationFail_Object=MibTableColumn
alaIPsecErrorsInAuthenticationFail=_AlaIPsecErrorsInAuthenticationFail_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,6,1,5),_AlaIPsecErrorsInAuthenticationFail_Type())
alaIPsecErrorsInAuthenticationFail.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecErrorsInAuthenticationFail.setStatus(_A)
_AlaIPsecErrorsInDiscarded_Type=Counter32
_AlaIPsecErrorsInDiscarded_Object=MibTableColumn
alaIPsecErrorsInDiscarded=_AlaIPsecErrorsInDiscarded_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,6,1,6),_AlaIPsecErrorsInDiscarded_Type())
alaIPsecErrorsInDiscarded.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecErrorsInDiscarded.setStatus(_A)
_AlaIPsecErrorsInOther_Type=Counter32
_AlaIPsecErrorsInOther_Object=MibTableColumn
alaIPsecErrorsInOther=_AlaIPsecErrorsInOther_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,6,1,7),_AlaIPsecErrorsInOther_Type())
alaIPsecErrorsInOther.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecErrorsInOther.setStatus(_A)
_AlaIPsecErrorsOutNoSA_Type=Counter32
_AlaIPsecErrorsOutNoSA_Object=MibTableColumn
alaIPsecErrorsOutNoSA=_AlaIPsecErrorsOutNoSA_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,6,1,8),_AlaIPsecErrorsOutNoSA_Type())
alaIPsecErrorsOutNoSA.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecErrorsOutNoSA.setStatus(_A)
_AlaIPsecErrorsOutDiscarded_Type=Counter32
_AlaIPsecErrorsOutDiscarded_Object=MibTableColumn
alaIPsecErrorsOutDiscarded=_AlaIPsecErrorsOutDiscarded_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,6,1,9),_AlaIPsecErrorsOutDiscarded_Type())
alaIPsecErrorsOutDiscarded.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecErrorsOutDiscarded.setStatus(_A)
_AlaIPsecErrorsOutOther_Type=Counter32
_AlaIPsecErrorsOutOther_Object=MibTableColumn
alaIPsecErrorsOutOther=_AlaIPsecErrorsOutOther_Object((1,3,6,1,4,1,6486,801,1,2,1,43,1,1,6,1,10),_AlaIPsecErrorsOutOther_Type())
alaIPsecErrorsOutOther.setMaxAccess(_D)
if mibBuilder.loadTexts:alaIPsecErrorsOutOther.setStatus(_A)
_AlcatelIND1IPsecMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1IPsecMIBConformance=_AlcatelIND1IPsecMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,43,1,2))
_AlcatelIND1IPsecMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1IPsecMIBCompliances=_AlcatelIND1IPsecMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,43,1,2,1))
_AlcatelIND1IPsecMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1IPsecMIBGroups=_AlcatelIND1IPsecMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,43,1,2,2))
alaIPsecConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,43,1,2,2,1))
alaIPsecConfigGroup.setObjects(*((_B,_c),(_B,_d)))
if mibBuilder.loadTexts:alaIPsecConfigGroup.setStatus(_A)
alaIPsecSecurityPolicyGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,43,1,2,2,2))
alaIPsecSecurityPolicyGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:alaIPsecSecurityPolicyGroup.setStatus(_A)
alaIPsecSAConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,43,1,2,2,3))
alaIPsecSAConfigGroup.setObjects(*((_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:alaIPsecSAConfigGroup.setStatus(_A)
alaIPsecKeyGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,43,1,2,2,4))
alaIPsecKeyGroup.setObjects(*((_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:alaIPsecKeyGroup.setStatus(_A)
alaIPsecCountersGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,43,1,2,2,5))
alaIPsecCountersGroup.setObjects(*((_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ)))
if mibBuilder.loadTexts:alaIPsecCountersGroup.setStatus(_A)
alaIPsecStatisticsGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,43,1,2,2,6))
alaIPsecStatisticsGroup.setObjects(*((_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj)))
if mibBuilder.loadTexts:alaIPsecStatisticsGroup.setStatus(_E)
alaIPsecCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,43,1,2,1,1))
alaIPsecCompliance.setObjects(*((_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao)))
if mibBuilder.loadTexts:alaIPsecCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_N:IPsecDescription,_M:IPsecPortNumber,'IPsecPrefixLength':IPsecPrefixLength,_V:IPsecULProtocol,_O:IPsecAdminState,'IPsecSAType':IPsecSAType,_Y:IPsecESPAlgorithm,_Z:IPsecAHAlgorithm,'IPsecOperationalState':IPsecOperationalState,'alcatelIND1IPsecMIB':alcatelIND1IPsecMIB,'alcatelIND1IPsecMIBObjects':alcatelIND1IPsecMIBObjects,'alaIPsecConfig':alaIPsecConfig,'alaIPsecSecurityKeyTable':alaIPsecSecurityKeyTable,'alaIPsecSecurityKeyEntry':alaIPsecSecurityKeyEntry,_S:alaIPsecSecurityKeyID,_c:alaIPsecSecurityKeyCurrent,_d:alaIPsecSecurityKeyNew,'alaIPsecStatisticsTable':alaIPsecStatisticsTable,'alaIPsecStatisticsEntry':alaIPsecStatisticsEntry,_U:alaIPsecStatisticsProtocol,_AR:alaIPsecStatisticsInSuccessful,_AS:alaIPsecStatisticsInPolicyViolation,_AT:alaIPsecStatisticsInNoSA,_AU:alaIPsecStatisticsInUnknownSPI,_AV:alaIPsecStatisticsInAHReplay,_AW:alaIPsecStatisticsInESPReplay,_AX:alaIPsecStatisticsInAHAuthenticationSuccess,_AY:alaIPsecStatisticsInAHAuthenticationFail,_AZ:alaIPsecStatisticsInESPAuthenticationSuccess,_Aa:alaIPsecStatisticsInESPAuthenticationFail,_Ab:alaIPsecStatisticsInBadPacket,_Ac:alaIPsecStatisticsInNoMemory,_Ad:alaIPsecStatisticsOutSuccessful,_Ae:alaIPsecStatisticsOutPolicyViolation,_Af:alaIPsecStatisticsOutNoSA,_Ag:alaIPsecStatisticsOutBadPacket,_Ah:alaIPsecStatisticsOutNoMemory,_Ai:alaIPsecStatisticsInDiscarded,_Aj:alaIPsecStatisticsOutDiscarded,'alaIPsecSecurityPolicyTable':alaIPsecSecurityPolicyTable,'alaIPsecSecurityPolicyEntry':alaIPsecSecurityPolicyEntry,_L:alaIPsecSecurityPolicyID,_f:alaIPsecSecurityPolicySourceType,_e:alaIPsecSecurityPolicySource,_g:alaIPsecSecurityPolicySourcePrefixLength,_h:alaIPsecSecurityPolicySourcePort,_j:alaIPsecSecurityPolicyDestinationType,_i:alaIPsecSecurityPolicyDestination,_k:alaIPsecSecurityPolicyDestinationPrefixLength,_l:alaIPsecSecurityPolicyDestinationPort,_m:alaIPsecSecurityPolicyULProtocol,_n:alaIPsecSecurityPolicyICMPv6Type,_o:alaIPsecSecurityPolicyDirection,_p:alaIPsecSecurityPolicyName,_q:alaIPsecSecurityPolicyDescription,_r:alaIPsecSecurityPolicyAction,_s:alaIPsecSecurityPolicyAdminState,_t:alaIPsecSecurityPolicyOperationalState,_u:alaIPsecSecurityPolicyPriority,_v:alaIPsecSecurityPolicyRowStatus,'alaIPsecSecurityPolicyRuleTable':alaIPsecSecurityPolicyRuleTable,'alaIPsecSecurityPolicyRuleEntry':alaIPsecSecurityPolicyRuleEntry,_W:alaIPsecSecurityPolicyRuleIndex,_w:alaIPsecSecurityPolicyRuleProtocol,_x:alaIPsecSecurityPolicyRuleMode,_y:alaIPsecSecurityPolicyRuleRowStatus,'alaIPsecSAConfigTable':alaIPsecSAConfigTable,'alaIPsecSAConfigEntry':alaIPsecSAConfigEntry,_X:alaIPsecSAConfigID,_z:alaIPsecSAConfigType,_A1:alaIPsecSAConfigSourceType,_A0:alaIPsecSAConfigSource,_A3:alaIPsecSAConfigDestinationType,_A2:alaIPsecSAConfigDestination,_A4:alaIPsecSAConfigSPI,_A5:alaIPsecSAConfigName,_A6:alaIPsecSAConfigDescription,_A7:alaIPsecSAConfigEncryptionAlgorithm,_A8:alaIPsecSAConfigEncryptionKeyLength,_A9:alaIPsecSAConfigAuthenticationAlgorithm,_AA:alaIPsecSAConfigAdminState,_AB:alaIPsecSAConfigOperationalState,_AC:alaIPsecSAConfigRowStatus,'alaIPsecKeyTable':alaIPsecKeyTable,'alaIPsecKeyEntry':alaIPsecKeyEntry,_a:alaIPsecKeyID,_AD:alaIPsecKeyType,_AE:alaIPsecKeyName,_AF:alaIPsecKey,_AG:alaIPsecKeyEncrypted,_AH:alaIPsecKeyRowStatus,'alaIPsecErrorsTable':alaIPsecErrorsTable,'alaIPsecErrorsEntry':alaIPsecErrorsEntry,_b:alaIPsecErrorsProtocol,_AI:alaIPsecErrorsInPolicyViolation,_AJ:alaIPsecErrorsInNoSA,_AK:alaIPsecErrorsInReplay,_AL:alaIPsecErrorsInAuthenticationFail,_AM:alaIPsecErrorsInDiscarded,_AN:alaIPsecErrorsInOther,_AO:alaIPsecErrorsOutNoSA,_AP:alaIPsecErrorsOutDiscarded,_AQ:alaIPsecErrorsOutOther,'alcatelIND1IPsecMIBConformance':alcatelIND1IPsecMIBConformance,'alcatelIND1IPsecMIBCompliances':alcatelIND1IPsecMIBCompliances,'alaIPsecCompliance':alaIPsecCompliance,'alcatelIND1IPsecMIBGroups':alcatelIND1IPsecMIBGroups,_Ak:alaIPsecConfigGroup,_Al:alaIPsecSecurityPolicyGroup,_Am:alaIPsecSAConfigGroup,_An:alaIPsecKeyGroup,_Ao:alaIPsecCountersGroup,'alaIPsecStatisticsGroup':alaIPsecStatisticsGroup})