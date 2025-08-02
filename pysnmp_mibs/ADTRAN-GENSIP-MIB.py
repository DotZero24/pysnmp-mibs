_T='adGenSipRegistrationIdentityIndex'
_S='adGenSipRegistrationTrunkIndex'
_R='read-write'
_Q='adGenSipMgmntIdentityIndex'
_P='adGenSipMgmntTrunkIndex'
_O='adGenSipIdentityEntryIndex'
_N='adGenSipIdentityTrunkIndex'
_M='adGenSipIdentityUserIndex'
_L='outboundProxy'
_K='adGenSipTrunkEntryIndex'
_J='ifIndex'
_I='IF-MIB'
_H='domain'
_G='not-accessible'
_F='DisplayString'
_E='ADTRAN-GENSIP-MIB'
_D='read-only'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AdGenVoipTrunkName,AdGenVoipUserNumber=mibBuilder.importSymbols('ADTRAN-GENVOIP-MIB','AdGenVoipTrunkName','AdGenVoipUserNumber')
adGenSip,adGenSipID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenSip','adGenSipID')
ifIndex,=mibBuilder.importSymbols(_I,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention','TruthValue')
adGenSipIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,21,1))
if mibBuilder.loadTexts:adGenSipIdentity.setRevisions(('2018-04-11 00:00','2011-05-04 00:00','2010-12-22 00:00','2009-10-06 00:00'))
_AdGenSipProvisioning_ObjectIdentity=ObjectIdentity
adGenSipProvisioning=_AdGenSipProvisioning_ObjectIdentity((1,3,6,1,4,1,664,5,70,21,1))
_AdGenSipTrunkProv_ObjectIdentity=ObjectIdentity
adGenSipTrunkProv=_AdGenSipTrunkProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,21,1,1))
_AdGenSipTrunkProvCurrentNumber_Type=Integer32
_AdGenSipTrunkProvCurrentNumber_Object=MibScalar
adGenSipTrunkProvCurrentNumber=_AdGenSipTrunkProvCurrentNumber_Object((1,3,6,1,4,1,664,5,70,21,1,1,1),_AdGenSipTrunkProvCurrentNumber_Type())
adGenSipTrunkProvCurrentNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSipTrunkProvCurrentNumber.setStatus(_A)
_AdGenSipTrunkProvLastCreateError_Type=DisplayString
_AdGenSipTrunkProvLastCreateError_Object=MibScalar
adGenSipTrunkProvLastCreateError=_AdGenSipTrunkProvLastCreateError_Object((1,3,6,1,4,1,664,5,70,21,1,1,2),_AdGenSipTrunkProvLastCreateError_Type())
adGenSipTrunkProvLastCreateError.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSipTrunkProvLastCreateError.setStatus(_A)
_AdGenSipTrunkProvTable_Object=MibTable
adGenSipTrunkProvTable=_AdGenSipTrunkProvTable_Object((1,3,6,1,4,1,664,5,70,21,1,1,3))
if mibBuilder.loadTexts:adGenSipTrunkProvTable.setStatus(_A)
_AdGenSipTrunkProvEntry_Object=MibTableRow
adGenSipTrunkProvEntry=_AdGenSipTrunkProvEntry_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1))
adGenSipTrunkProvEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:adGenSipTrunkProvEntry.setStatus(_A)
_AdGenSipTrunkEntryIndex_Type=AdGenVoipTrunkName
_AdGenSipTrunkEntryIndex_Object=MibTableColumn
adGenSipTrunkEntryIndex=_AdGenSipTrunkEntryIndex_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,1),_AdGenSipTrunkEntryIndex_Type())
adGenSipTrunkEntryIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenSipTrunkEntryIndex.setStatus(_A)
_AdGenSipTrunkRowStatus_Type=RowStatus
_AdGenSipTrunkRowStatus_Object=MibTableColumn
adGenSipTrunkRowStatus=_AdGenSipTrunkRowStatus_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,2),_AdGenSipTrunkRowStatus_Type())
adGenSipTrunkRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkRowStatus.setStatus(_A)
_AdGenSipTrunkLastErrorString_Type=DisplayString
_AdGenSipTrunkLastErrorString_Object=MibTableColumn
adGenSipTrunkLastErrorString=_AdGenSipTrunkLastErrorString_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,3),_AdGenSipTrunkLastErrorString_Type())
adGenSipTrunkLastErrorString.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSipTrunkLastErrorString.setStatus(_A)
_AdGenSipTrunkSipProxyPrimary_Type=DisplayString
_AdGenSipTrunkSipProxyPrimary_Object=MibTableColumn
adGenSipTrunkSipProxyPrimary=_AdGenSipTrunkSipProxyPrimary_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,4),_AdGenSipTrunkSipProxyPrimary_Type())
adGenSipTrunkSipProxyPrimary.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipProxyPrimary.setStatus(_A)
class _AdGenSipTrunkSipProxyPrimaryUdp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdGenSipTrunkSipProxyPrimaryUdp_Type.__name__=_C
_AdGenSipTrunkSipProxyPrimaryUdp_Object=MibTableColumn
adGenSipTrunkSipProxyPrimaryUdp=_AdGenSipTrunkSipProxyPrimaryUdp_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,5),_AdGenSipTrunkSipProxyPrimaryUdp_Type())
adGenSipTrunkSipProxyPrimaryUdp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipProxyPrimaryUdp.setStatus(_A)
_AdGenSipTrunkSipProxySecondary_Type=DisplayString
_AdGenSipTrunkSipProxySecondary_Object=MibTableColumn
adGenSipTrunkSipProxySecondary=_AdGenSipTrunkSipProxySecondary_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,6),_AdGenSipTrunkSipProxySecondary_Type())
adGenSipTrunkSipProxySecondary.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipProxySecondary.setStatus(_A)
class _AdGenSipTrunkSipProxySecondaryUdp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdGenSipTrunkSipProxySecondaryUdp_Type.__name__=_C
_AdGenSipTrunkSipProxySecondaryUdp_Object=MibTableColumn
adGenSipTrunkSipProxySecondaryUdp=_AdGenSipTrunkSipProxySecondaryUdp_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,7),_AdGenSipTrunkSipProxySecondaryUdp_Type())
adGenSipTrunkSipProxySecondaryUdp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipProxySecondaryUdp.setStatus(_A)
_AdGenSipTrunkSipOutboundProxyPrimary_Type=DisplayString
_AdGenSipTrunkSipOutboundProxyPrimary_Object=MibTableColumn
adGenSipTrunkSipOutboundProxyPrimary=_AdGenSipTrunkSipOutboundProxyPrimary_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,8),_AdGenSipTrunkSipOutboundProxyPrimary_Type())
adGenSipTrunkSipOutboundProxyPrimary.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipOutboundProxyPrimary.setStatus(_A)
class _AdGenSipTrunkSipOutboundProxyPrimaryUdp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdGenSipTrunkSipOutboundProxyPrimaryUdp_Type.__name__=_C
_AdGenSipTrunkSipOutboundProxyPrimaryUdp_Object=MibTableColumn
adGenSipTrunkSipOutboundProxyPrimaryUdp=_AdGenSipTrunkSipOutboundProxyPrimaryUdp_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,9),_AdGenSipTrunkSipOutboundProxyPrimaryUdp_Type())
adGenSipTrunkSipOutboundProxyPrimaryUdp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipOutboundProxyPrimaryUdp.setStatus(_A)
_AdGenSipTrunkSipOutboundProxySecondary_Type=DisplayString
_AdGenSipTrunkSipOutboundProxySecondary_Object=MibTableColumn
adGenSipTrunkSipOutboundProxySecondary=_AdGenSipTrunkSipOutboundProxySecondary_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,10),_AdGenSipTrunkSipOutboundProxySecondary_Type())
adGenSipTrunkSipOutboundProxySecondary.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipOutboundProxySecondary.setStatus(_A)
class _AdGenSipTrunkSipOutboundProxySecondaryUdp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdGenSipTrunkSipOutboundProxySecondaryUdp_Type.__name__=_C
_AdGenSipTrunkSipOutboundProxySecondaryUdp_Object=MibTableColumn
adGenSipTrunkSipOutboundProxySecondaryUdp=_AdGenSipTrunkSipOutboundProxySecondaryUdp_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,11),_AdGenSipTrunkSipOutboundProxySecondaryUdp_Type())
adGenSipTrunkSipOutboundProxySecondaryUdp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipOutboundProxySecondaryUdp.setStatus(_A)
class _AdGenSipTrunkSipDomain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_AdGenSipTrunkSipDomain_Type.__name__=_F
_AdGenSipTrunkSipDomain_Object=MibTableColumn
adGenSipTrunkSipDomain=_AdGenSipTrunkSipDomain_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,12),_AdGenSipTrunkSipDomain_Type())
adGenSipTrunkSipDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipDomain.setStatus(_A)
_AdGenSipTrunkSipTrustDomain_Type=TruthValue
_AdGenSipTrunkSipTrustDomain_Object=MibTableColumn
adGenSipTrunkSipTrustDomain=_AdGenSipTrunkSipTrustDomain_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,13),_AdGenSipTrunkSipTrustDomain_Type())
adGenSipTrunkSipTrustDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipTrustDomain.setStatus(_A)
_AdGenSipTrunkSipTrustDomainPAssertedIdReq_Type=TruthValue
_AdGenSipTrunkSipTrustDomainPAssertedIdReq_Object=MibTableColumn
adGenSipTrunkSipTrustDomainPAssertedIdReq=_AdGenSipTrunkSipTrustDomainPAssertedIdReq_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,14),_AdGenSipTrunkSipTrustDomainPAssertedIdReq_Type())
adGenSipTrunkSipTrustDomainPAssertedIdReq.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipTrustDomainPAssertedIdReq.setStatus(_A)
_AdGenSipTrunkSipAuthenticate_Type=TruthValue
_AdGenSipTrunkSipAuthenticate_Object=MibTableColumn
adGenSipTrunkSipAuthenticate=_AdGenSipTrunkSipAuthenticate_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,15),_AdGenSipTrunkSipAuthenticate_Type())
adGenSipTrunkSipAuthenticate.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipAuthenticate.setStatus(_A)
class _AdGenSipTrunkSipDialStringSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('requestUri',1),('to',2)))
_AdGenSipTrunkSipDialStringSource_Type.__name__=_C
_AdGenSipTrunkSipDialStringSource_Object=MibTableColumn
adGenSipTrunkSipDialStringSource=_AdGenSipTrunkSipDialStringSource_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,16),_AdGenSipTrunkSipDialStringSource_Type())
adGenSipTrunkSipDialStringSource.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipDialStringSource.setStatus(_A)
class _AdGenSipTrunkSipKeepAliveMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('info',2),('options',3)))
_AdGenSipTrunkSipKeepAliveMethod_Type.__name__=_C
_AdGenSipTrunkSipKeepAliveMethod_Object=MibTableColumn
adGenSipTrunkSipKeepAliveMethod=_AdGenSipTrunkSipKeepAliveMethod_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,17),_AdGenSipTrunkSipKeepAliveMethod_Type())
adGenSipTrunkSipKeepAliveMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipKeepAliveMethod.setStatus(_A)
class _AdGenSipTrunkSipKeepAliveInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,3600))
_AdGenSipTrunkSipKeepAliveInterval_Type.__name__=_C
_AdGenSipTrunkSipKeepAliveInterval_Object=MibTableColumn
adGenSipTrunkSipKeepAliveInterval=_AdGenSipTrunkSipKeepAliveInterval_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,18),_AdGenSipTrunkSipKeepAliveInterval_Type())
adGenSipTrunkSipKeepAliveInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipKeepAliveInterval.setStatus(_A)
class _AdGenSipTrunkTimerRegFailRetry_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,604800))
_AdGenSipTrunkTimerRegFailRetry_Type.__name__=_C
_AdGenSipTrunkTimerRegFailRetry_Object=MibTableColumn
adGenSipTrunkTimerRegFailRetry=_AdGenSipTrunkTimerRegFailRetry_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,19),_AdGenSipTrunkTimerRegFailRetry_Type())
adGenSipTrunkTimerRegFailRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkTimerRegFailRetry.setStatus(_A)
class _AdGenSipTrunkTimerRollover_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_AdGenSipTrunkTimerRollover_Type.__name__=_C
_AdGenSipTrunkTimerRollover_Object=MibTableColumn
adGenSipTrunkTimerRollover=_AdGenSipTrunkTimerRollover_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,20),_AdGenSipTrunkTimerRollover_Type())
adGenSipTrunkTimerRollover.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkTimerRollover.setStatus(_A)
_AdGenSipTrunkPrivacy_Type=TruthValue
_AdGenSipTrunkPrivacy_Object=MibTableColumn
adGenSipTrunkPrivacy=_AdGenSipTrunkPrivacy_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,21),_AdGenSipTrunkPrivacy_Type())
adGenSipTrunkPrivacy.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkPrivacy.setStatus(_A)
_AdGenSipTrunkGrammarRequestUriResolve_Type=TruthValue
_AdGenSipTrunkGrammarRequestUriResolve_Object=MibTableColumn
adGenSipTrunkGrammarRequestUriResolve=_AdGenSipTrunkGrammarRequestUriResolve_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,22),_AdGenSipTrunkGrammarRequestUriResolve_Type())
adGenSipTrunkGrammarRequestUriResolve.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkGrammarRequestUriResolve.setStatus(_A)
class _AdGenSipTrunkGrammarRequestUriHost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sipOutboundProxy',1),('sipProxy',2),(_H,3)))
_AdGenSipTrunkGrammarRequestUriHost_Type.__name__=_C
_AdGenSipTrunkGrammarRequestUriHost_Object=MibTableColumn
adGenSipTrunkGrammarRequestUriHost=_AdGenSipTrunkGrammarRequestUriHost_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,23),_AdGenSipTrunkGrammarRequestUriHost_Type())
adGenSipTrunkGrammarRequestUriHost.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkGrammarRequestUriHost.setStatus(_A)
class _AdGenSipTrunkGrammarFromHost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),('proxy',2),(_H,3),('local',4)))
_AdGenSipTrunkGrammarFromHost_Type.__name__=_C
_AdGenSipTrunkGrammarFromHost_Object=MibTableColumn
adGenSipTrunkGrammarFromHost=_AdGenSipTrunkGrammarFromHost_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,24),_AdGenSipTrunkGrammarFromHost_Type())
adGenSipTrunkGrammarFromHost.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkGrammarFromHost.setStatus(_A)
class _AdGenSipTrunkGrammarFromUser_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('domestic',1),('international',2)))
_AdGenSipTrunkGrammarFromUser_Type.__name__=_C
_AdGenSipTrunkGrammarFromUser_Object=MibTableColumn
adGenSipTrunkGrammarFromUser=_AdGenSipTrunkGrammarFromUser_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,25),_AdGenSipTrunkGrammarFromUser_Type())
adGenSipTrunkGrammarFromUser.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkGrammarFromUser.setStatus(_A)
class _AdGenSipTrunkGrammarPAssertedIdHost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),('proxy',2),(_H,3),('local',4)))
_AdGenSipTrunkGrammarPAssertedIdHost_Type.__name__=_C
_AdGenSipTrunkGrammarPAssertedIdHost_Object=MibTableColumn
adGenSipTrunkGrammarPAssertedIdHost=_AdGenSipTrunkGrammarPAssertedIdHost_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,26),_AdGenSipTrunkGrammarPAssertedIdHost_Type())
adGenSipTrunkGrammarPAssertedIdHost.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkGrammarPAssertedIdHost.setStatus(_A)
class _AdGenSipTrunkGrammarToHost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('server',1),(_H,2)))
_AdGenSipTrunkGrammarToHost_Type.__name__=_C
_AdGenSipTrunkGrammarToHost_Object=MibTableColumn
adGenSipTrunkGrammarToHost=_AdGenSipTrunkGrammarToHost_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,27),_AdGenSipTrunkGrammarToHost_Type())
adGenSipTrunkGrammarToHost.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkGrammarToHost.setStatus(_A)
_AdGenSipTrunkGrammarAlertInfoUrl_Type=DisplayString
_AdGenSipTrunkGrammarAlertInfoUrl_Object=MibTableColumn
adGenSipTrunkGrammarAlertInfoUrl=_AdGenSipTrunkGrammarAlertInfoUrl_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,28),_AdGenSipTrunkGrammarAlertInfoUrl_Type())
adGenSipTrunkGrammarAlertInfoUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkGrammarAlertInfoUrl.setStatus(_A)
_AdGenSipTrunkGrammarSupported100Rel_Type=TruthValue
_AdGenSipTrunkGrammarSupported100Rel_Object=MibTableColumn
adGenSipTrunkGrammarSupported100Rel=_AdGenSipTrunkGrammarSupported100Rel_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,29),_AdGenSipTrunkGrammarSupported100Rel_Type())
adGenSipTrunkGrammarSupported100Rel.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkGrammarSupported100Rel.setStatus(_A)
_AdGenSipTrunkGrammarProxyRequirePrivacy_Type=TruthValue
_AdGenSipTrunkGrammarProxyRequirePrivacy_Object=MibTableColumn
adGenSipTrunkGrammarProxyRequirePrivacy=_AdGenSipTrunkGrammarProxyRequirePrivacy_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,30),_AdGenSipTrunkGrammarProxyRequirePrivacy_Type())
adGenSipTrunkGrammarProxyRequirePrivacy.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkGrammarProxyRequirePrivacy.setStatus(_A)
_AdGenSipTrunkGrammarRequire100rel_Type=TruthValue
_AdGenSipTrunkGrammarRequire100rel_Object=MibTableColumn
adGenSipTrunkGrammarRequire100rel=_AdGenSipTrunkGrammarRequire100rel_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,31),_AdGenSipTrunkGrammarRequire100rel_Type())
adGenSipTrunkGrammarRequire100rel.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkGrammarRequire100rel.setStatus(_A)
class _AdGenSipTrunkGrammarUserAgent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_AdGenSipTrunkGrammarUserAgent_Type.__name__=_F
_AdGenSipTrunkGrammarUserAgent_Object=MibTableColumn
adGenSipTrunkGrammarUserAgent=_AdGenSipTrunkGrammarUserAgent_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,32),_AdGenSipTrunkGrammarUserAgent_Type())
adGenSipTrunkGrammarUserAgent.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkGrammarUserAgent.setStatus(_A)
class _AdGenSipTrunkGrammarSdpHold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rfc2543',1),('rfc3264',2)))
_AdGenSipTrunkGrammarSdpHold_Type.__name__=_C
_AdGenSipTrunkGrammarSdpHold_Object=MibTableColumn
adGenSipTrunkGrammarSdpHold=_AdGenSipTrunkGrammarSdpHold_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,33),_AdGenSipTrunkGrammarSdpHold_Type())
adGenSipTrunkGrammarSdpHold.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkGrammarSdpHold.setStatus(_A)
_AdGenSipTrunkSipRegistrarPrimary_Type=DisplayString
_AdGenSipTrunkSipRegistrarPrimary_Object=MibTableColumn
adGenSipTrunkSipRegistrarPrimary=_AdGenSipTrunkSipRegistrarPrimary_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,34),_AdGenSipTrunkSipRegistrarPrimary_Type())
adGenSipTrunkSipRegistrarPrimary.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipRegistrarPrimary.setStatus(_A)
class _AdGenSipTrunkSipRegistrarPrimaryUdp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdGenSipTrunkSipRegistrarPrimaryUdp_Type.__name__=_C
_AdGenSipTrunkSipRegistrarPrimaryUdp_Object=MibTableColumn
adGenSipTrunkSipRegistrarPrimaryUdp=_AdGenSipTrunkSipRegistrarPrimaryUdp_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,35),_AdGenSipTrunkSipRegistrarPrimaryUdp_Type())
adGenSipTrunkSipRegistrarPrimaryUdp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipRegistrarPrimaryUdp.setStatus(_A)
_AdGenSipTrunkSipRegistrarSecondary_Type=DisplayString
_AdGenSipTrunkSipRegistrarSecondary_Object=MibTableColumn
adGenSipTrunkSipRegistrarSecondary=_AdGenSipTrunkSipRegistrarSecondary_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,36),_AdGenSipTrunkSipRegistrarSecondary_Type())
adGenSipTrunkSipRegistrarSecondary.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipRegistrarSecondary.setStatus(_A)
class _AdGenSipTrunkSipRegistrarSecondaryUdp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AdGenSipTrunkSipRegistrarSecondaryUdp_Type.__name__=_C
_AdGenSipTrunkSipRegistrarSecondaryUdp_Object=MibTableColumn
adGenSipTrunkSipRegistrarSecondaryUdp=_AdGenSipTrunkSipRegistrarSecondaryUdp_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,37),_AdGenSipTrunkSipRegistrarSecondaryUdp_Type())
adGenSipTrunkSipRegistrarSecondaryUdp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipRegistrarSecondaryUdp.setStatus(_A)
class _AdGenSipTrunkSipRegistrarThresholdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('percentage',1),('absolute',2)))
_AdGenSipTrunkSipRegistrarThresholdType_Type.__name__=_C
_AdGenSipTrunkSipRegistrarThresholdType_Object=MibTableColumn
adGenSipTrunkSipRegistrarThresholdType=_AdGenSipTrunkSipRegistrarThresholdType_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,38),_AdGenSipTrunkSipRegistrarThresholdType_Type())
adGenSipTrunkSipRegistrarThresholdType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipRegistrarThresholdType.setStatus(_A)
class _AdGenSipTrunkSipRegistrarThresholdValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,604800))
_AdGenSipTrunkSipRegistrarThresholdValue_Type.__name__=_C
_AdGenSipTrunkSipRegistrarThresholdValue_Object=MibTableColumn
adGenSipTrunkSipRegistrarThresholdValue=_AdGenSipTrunkSipRegistrarThresholdValue_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,39),_AdGenSipTrunkSipRegistrarThresholdValue_Type())
adGenSipTrunkSipRegistrarThresholdValue.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipRegistrarThresholdValue.setStatus(_A)
class _AdGenSipTrunkSipRegistrarMaxConcurrentReg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_AdGenSipTrunkSipRegistrarMaxConcurrentReg_Type.__name__=_C
_AdGenSipTrunkSipRegistrarMaxConcurrentReg_Object=MibTableColumn
adGenSipTrunkSipRegistrarMaxConcurrentReg=_AdGenSipTrunkSipRegistrarMaxConcurrentReg_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,40),_AdGenSipTrunkSipRegistrarMaxConcurrentReg_Type())
adGenSipTrunkSipRegistrarMaxConcurrentReg.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipRegistrarMaxConcurrentReg.setStatus(_A)
class _AdGenSipTrunkSipRegistrarExpireTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AdGenSipTrunkSipRegistrarExpireTime_Type.__name__=_C
_AdGenSipTrunkSipRegistrarExpireTime_Object=MibTableColumn
adGenSipTrunkSipRegistrarExpireTime=_AdGenSipTrunkSipRegistrarExpireTime_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,41),_AdGenSipTrunkSipRegistrarExpireTime_Type())
adGenSipTrunkSipRegistrarExpireTime.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipRegistrarExpireTime.setStatus(_A)
_AdGenSipTrunkSipRegistrarRequireExpires_Type=TruthValue
_AdGenSipTrunkSipRegistrarRequireExpires_Object=MibTableColumn
adGenSipTrunkSipRegistrarRequireExpires=_AdGenSipTrunkSipRegistrarRequireExpires_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,42),_AdGenSipTrunkSipRegistrarRequireExpires_Type())
adGenSipTrunkSipRegistrarRequireExpires.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipRegistrarRequireExpires.setStatus(_A)
class _AdGenSipTrunkSipDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AdGenSipTrunkSipDscp_Type.__name__=_C
_AdGenSipTrunkSipDscp_Object=MibTableColumn
adGenSipTrunkSipDscp=_AdGenSipTrunkSipDscp_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,43),_AdGenSipTrunkSipDscp_Type())
adGenSipTrunkSipDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkSipDscp.setStatus(_A)
class _AdGenSipTrunkRtpDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AdGenSipTrunkRtpDscp_Type.__name__=_C
_AdGenSipTrunkRtpDscp_Object=MibTableColumn
adGenSipTrunkRtpDscp=_AdGenSipTrunkRtpDscp_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,44),_AdGenSipTrunkRtpDscp_Type())
adGenSipTrunkRtpDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkRtpDscp.setStatus(_A)
class _AdGenSipTrunkGrammarAddressScheme_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sipUri',1),('telUri',2)))
_AdGenSipTrunkGrammarAddressScheme_Type.__name__=_C
_AdGenSipTrunkGrammarAddressScheme_Object=MibTableColumn
adGenSipTrunkGrammarAddressScheme=_AdGenSipTrunkGrammarAddressScheme_Object((1,3,6,1,4,1,664,5,70,21,1,1,3,1,45),_AdGenSipTrunkGrammarAddressScheme_Type())
adGenSipTrunkGrammarAddressScheme.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipTrunkGrammarAddressScheme.setStatus(_A)
_AdGenSipIdentityProv_ObjectIdentity=ObjectIdentity
adGenSipIdentityProv=_AdGenSipIdentityProv_ObjectIdentity((1,3,6,1,4,1,664,5,70,21,1,2))
_AdGenSipIdentityProvCurrentNumber_Type=Integer32
_AdGenSipIdentityProvCurrentNumber_Object=MibScalar
adGenSipIdentityProvCurrentNumber=_AdGenSipIdentityProvCurrentNumber_Object((1,3,6,1,4,1,664,5,70,21,1,2,1),_AdGenSipIdentityProvCurrentNumber_Type())
adGenSipIdentityProvCurrentNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSipIdentityProvCurrentNumber.setStatus(_A)
_AdGenSipIdentityProvLastCreateError_Type=DisplayString
_AdGenSipIdentityProvLastCreateError_Object=MibScalar
adGenSipIdentityProvLastCreateError=_AdGenSipIdentityProvLastCreateError_Object((1,3,6,1,4,1,664,5,70,21,1,2,2),_AdGenSipIdentityProvLastCreateError_Type())
adGenSipIdentityProvLastCreateError.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSipIdentityProvLastCreateError.setStatus(_A)
_AdGenSipIdentityProvTable_Object=MibTable
adGenSipIdentityProvTable=_AdGenSipIdentityProvTable_Object((1,3,6,1,4,1,664,5,70,21,1,2,3))
if mibBuilder.loadTexts:adGenSipIdentityProvTable.setStatus(_A)
_AdGenSipIdentityProvEntry_Object=MibTableRow
adGenSipIdentityProvEntry=_AdGenSipIdentityProvEntry_Object((1,3,6,1,4,1,664,5,70,21,1,2,3,1))
adGenSipIdentityProvEntry.setIndexNames((0,_E,_M),(0,_E,_N),(1,_E,_O))
if mibBuilder.loadTexts:adGenSipIdentityProvEntry.setStatus(_A)
_AdGenSipIdentityUserIndex_Type=AdGenVoipUserNumber
_AdGenSipIdentityUserIndex_Object=MibTableColumn
adGenSipIdentityUserIndex=_AdGenSipIdentityUserIndex_Object((1,3,6,1,4,1,664,5,70,21,1,2,3,1,1),_AdGenSipIdentityUserIndex_Type())
adGenSipIdentityUserIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenSipIdentityUserIndex.setStatus(_A)
_AdGenSipIdentityTrunkIndex_Type=AdGenVoipTrunkName
_AdGenSipIdentityTrunkIndex_Object=MibTableColumn
adGenSipIdentityTrunkIndex=_AdGenSipIdentityTrunkIndex_Object((1,3,6,1,4,1,664,5,70,21,1,2,3,1,2),_AdGenSipIdentityTrunkIndex_Type())
adGenSipIdentityTrunkIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenSipIdentityTrunkIndex.setStatus(_A)
class _AdGenSipIdentityEntryIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_AdGenSipIdentityEntryIndex_Type.__name__=_F
_AdGenSipIdentityEntryIndex_Object=MibTableColumn
adGenSipIdentityEntryIndex=_AdGenSipIdentityEntryIndex_Object((1,3,6,1,4,1,664,5,70,21,1,2,3,1,3),_AdGenSipIdentityEntryIndex_Type())
adGenSipIdentityEntryIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenSipIdentityEntryIndex.setStatus(_A)
_AdGenSipIdentityRowStatus_Type=RowStatus
_AdGenSipIdentityRowStatus_Object=MibTableColumn
adGenSipIdentityRowStatus=_AdGenSipIdentityRowStatus_Object((1,3,6,1,4,1,664,5,70,21,1,2,3,1,4),_AdGenSipIdentityRowStatus_Type())
adGenSipIdentityRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipIdentityRowStatus.setStatus(_A)
_AdGenSipIdentityLastErrorString_Type=DisplayString
_AdGenSipIdentityLastErrorString_Object=MibTableColumn
adGenSipIdentityLastErrorString=_AdGenSipIdentityLastErrorString_Object((1,3,6,1,4,1,664,5,70,21,1,2,3,1,5),_AdGenSipIdentityLastErrorString_Type())
adGenSipIdentityLastErrorString.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSipIdentityLastErrorString.setStatus(_A)
_AdGenSipIdentityRegister_Type=TruthValue
_AdGenSipIdentityRegister_Object=MibTableColumn
adGenSipIdentityRegister=_AdGenSipIdentityRegister_Object((1,3,6,1,4,1,664,5,70,21,1,2,3,1,6),_AdGenSipIdentityRegister_Type())
adGenSipIdentityRegister.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipIdentityRegister.setStatus(_A)
class _AdGenSipIdentityAuthName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_AdGenSipIdentityAuthName_Type.__name__=_F
_AdGenSipIdentityAuthName_Object=MibTableColumn
adGenSipIdentityAuthName=_AdGenSipIdentityAuthName_Object((1,3,6,1,4,1,664,5,70,21,1,2,3,1,7),_AdGenSipIdentityAuthName_Type())
adGenSipIdentityAuthName.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipIdentityAuthName.setStatus(_A)
class _AdGenSipIdentityPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_AdGenSipIdentityPassword_Type.__name__=_F
_AdGenSipIdentityPassword_Object=MibTableColumn
adGenSipIdentityPassword=_AdGenSipIdentityPassword_Object((1,3,6,1,4,1,664,5,70,21,1,2,3,1,8),_AdGenSipIdentityPassword_Type())
adGenSipIdentityPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenSipIdentityPassword.setStatus(_A)
_AdGenSipMgmnt_ObjectIdentity=ObjectIdentity
adGenSipMgmnt=_AdGenSipMgmnt_ObjectIdentity((1,3,6,1,4,1,664,5,70,21,2))
_AdGenSipMgmntActions_ObjectIdentity=ObjectIdentity
adGenSipMgmntActions=_AdGenSipMgmntActions_ObjectIdentity((1,3,6,1,4,1,664,5,70,21,2,1))
_AdGenSipMgmntTable_Object=MibTable
adGenSipMgmntTable=_AdGenSipMgmntTable_Object((1,3,6,1,4,1,664,5,70,21,2,1,1))
if mibBuilder.loadTexts:adGenSipMgmntTable.setStatus(_A)
_AdGenSipMgmntEntry_Object=MibTableRow
adGenSipMgmntEntry=_AdGenSipMgmntEntry_Object((1,3,6,1,4,1,664,5,70,21,2,1,1,1))
adGenSipMgmntEntry.setIndexNames((0,_I,_J),(0,_E,_P),(1,_E,_Q))
if mibBuilder.loadTexts:adGenSipMgmntEntry.setStatus(_A)
_AdGenSipMgmntTrunkIndex_Type=AdGenVoipTrunkName
_AdGenSipMgmntTrunkIndex_Object=MibTableColumn
adGenSipMgmntTrunkIndex=_AdGenSipMgmntTrunkIndex_Object((1,3,6,1,4,1,664,5,70,21,2,1,1,1,1),_AdGenSipMgmntTrunkIndex_Type())
adGenSipMgmntTrunkIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenSipMgmntTrunkIndex.setStatus(_A)
class _AdGenSipMgmntIdentityIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_AdGenSipMgmntIdentityIndex_Type.__name__=_F
_AdGenSipMgmntIdentityIndex_Object=MibTableColumn
adGenSipMgmntIdentityIndex=_AdGenSipMgmntIdentityIndex_Object((1,3,6,1,4,1,664,5,70,21,2,1,1,1,2),_AdGenSipMgmntIdentityIndex_Type())
adGenSipMgmntIdentityIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenSipMgmntIdentityIndex.setStatus(_A)
class _AdGenSipMgmntForceReg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('force',1))
_AdGenSipMgmntForceReg_Type.__name__=_C
_AdGenSipMgmntForceReg_Object=MibTableColumn
adGenSipMgmntForceReg=_AdGenSipMgmntForceReg_Object((1,3,6,1,4,1,664,5,70,21,2,1,1,1,3),_AdGenSipMgmntForceReg_Type())
adGenSipMgmntForceReg.setMaxAccess(_R)
if mibBuilder.loadTexts:adGenSipMgmntForceReg.setStatus(_A)
class _AdGenSipMgmntClearReg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_AdGenSipMgmntClearReg_Type.__name__=_C
_AdGenSipMgmntClearReg_Object=MibTableColumn
adGenSipMgmntClearReg=_AdGenSipMgmntClearReg_Object((1,3,6,1,4,1,664,5,70,21,2,1,1,1,4),_AdGenSipMgmntClearReg_Type())
adGenSipMgmntClearReg.setMaxAccess(_R)
if mibBuilder.loadTexts:adGenSipMgmntClearReg.setStatus(_A)
_AdGenSipStatus_ObjectIdentity=ObjectIdentity
adGenSipStatus=_AdGenSipStatus_ObjectIdentity((1,3,6,1,4,1,664,5,70,21,3))
_AdGenSipStatusRegistration_ObjectIdentity=ObjectIdentity
adGenSipStatusRegistration=_AdGenSipStatusRegistration_ObjectIdentity((1,3,6,1,4,1,664,5,70,21,3,1))
_AdGenSipStatusRegistrationTable_Object=MibTable
adGenSipStatusRegistrationTable=_AdGenSipStatusRegistrationTable_Object((1,3,6,1,4,1,664,5,70,21,3,1,1))
if mibBuilder.loadTexts:adGenSipStatusRegistrationTable.setStatus(_A)
_AdGenSipStatusRegistrationEntry_Object=MibTableRow
adGenSipStatusRegistrationEntry=_AdGenSipStatusRegistrationEntry_Object((1,3,6,1,4,1,664,5,70,21,3,1,1,1))
adGenSipStatusRegistrationEntry.setIndexNames((0,_I,_J),(0,_E,_S),(1,_E,_T))
if mibBuilder.loadTexts:adGenSipStatusRegistrationEntry.setStatus(_A)
_AdGenSipRegistrationTrunkIndex_Type=AdGenVoipTrunkName
_AdGenSipRegistrationTrunkIndex_Object=MibTableColumn
adGenSipRegistrationTrunkIndex=_AdGenSipRegistrationTrunkIndex_Object((1,3,6,1,4,1,664,5,70,21,3,1,1,1,1),_AdGenSipRegistrationTrunkIndex_Type())
adGenSipRegistrationTrunkIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenSipRegistrationTrunkIndex.setStatus(_A)
class _AdGenSipRegistrationIdentityIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_AdGenSipRegistrationIdentityIndex_Type.__name__=_F
_AdGenSipRegistrationIdentityIndex_Object=MibTableColumn
adGenSipRegistrationIdentityIndex=_AdGenSipRegistrationIdentityIndex_Object((1,3,6,1,4,1,664,5,70,21,3,1,1,1,2),_AdGenSipRegistrationIdentityIndex_Type())
adGenSipRegistrationIdentityIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenSipRegistrationIdentityIndex.setStatus(_A)
class _AdGenSipStatusRegistrationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_AdGenSipStatusRegistrationStatus_Type.__name__=_C
_AdGenSipStatusRegistrationStatus_Object=MibTableColumn
adGenSipStatusRegistrationStatus=_AdGenSipStatusRegistrationStatus_Object((1,3,6,1,4,1,664,5,70,21,3,1,1,1,3),_AdGenSipStatusRegistrationStatus_Type())
adGenSipStatusRegistrationStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSipStatusRegistrationStatus.setStatus(_A)
_AdGenSipStatusRegistrationGrant_Type=Unsigned32
_AdGenSipStatusRegistrationGrant_Object=MibTableColumn
adGenSipStatusRegistrationGrant=_AdGenSipStatusRegistrationGrant_Object((1,3,6,1,4,1,664,5,70,21,3,1,1,1,4),_AdGenSipStatusRegistrationGrant_Type())
adGenSipStatusRegistrationGrant.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSipStatusRegistrationGrant.setStatus(_A)
_AdGenSipStatusRegistrationExpires_Type=Unsigned32
_AdGenSipStatusRegistrationExpires_Object=MibTableColumn
adGenSipStatusRegistrationExpires=_AdGenSipStatusRegistrationExpires_Object((1,3,6,1,4,1,664,5,70,21,3,1,1,1,5),_AdGenSipStatusRegistrationExpires_Type())
adGenSipStatusRegistrationExpires.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSipStatusRegistrationExpires.setStatus(_A)
_AdGenSipStatusRegistrationSuccess_Type=Unsigned32
_AdGenSipStatusRegistrationSuccess_Object=MibTableColumn
adGenSipStatusRegistrationSuccess=_AdGenSipStatusRegistrationSuccess_Object((1,3,6,1,4,1,664,5,70,21,3,1,1,1,6),_AdGenSipStatusRegistrationSuccess_Type())
adGenSipStatusRegistrationSuccess.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSipStatusRegistrationSuccess.setStatus(_A)
_AdGenSipStatusRegistrationFail_Type=Unsigned32
_AdGenSipStatusRegistrationFail_Object=MibTableColumn
adGenSipStatusRegistrationFail=_AdGenSipStatusRegistrationFail_Object((1,3,6,1,4,1,664,5,70,21,3,1,1,1,7),_AdGenSipStatusRegistrationFail_Type())
adGenSipStatusRegistrationFail.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSipStatusRegistrationFail.setStatus(_A)
_AdGenSipStatusRegistrationRequests_Type=Unsigned32
_AdGenSipStatusRegistrationRequests_Object=MibTableColumn
adGenSipStatusRegistrationRequests=_AdGenSipStatusRegistrationRequests_Object((1,3,6,1,4,1,664,5,70,21,3,1,1,1,8),_AdGenSipStatusRegistrationRequests_Type())
adGenSipStatusRegistrationRequests.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSipStatusRegistrationRequests.setStatus(_A)
_AdGenSipStatusRegistrationChallenges_Type=Unsigned32
_AdGenSipStatusRegistrationChallenges_Object=MibTableColumn
adGenSipStatusRegistrationChallenges=_AdGenSipStatusRegistrationChallenges_Object((1,3,6,1,4,1,664,5,70,21,3,1,1,1,9),_AdGenSipStatusRegistrationChallenges_Type())
adGenSipStatusRegistrationChallenges.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSipStatusRegistrationChallenges.setStatus(_A)
_AdGenSipStatusRegistrationRollovers_Type=Unsigned32
_AdGenSipStatusRegistrationRollovers_Object=MibTableColumn
adGenSipStatusRegistrationRollovers=_AdGenSipStatusRegistrationRollovers_Object((1,3,6,1,4,1,664,5,70,21,3,1,1,1,10),_AdGenSipStatusRegistrationRollovers_Type())
adGenSipStatusRegistrationRollovers.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenSipStatusRegistrationRollovers.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'adGenSipProvisioning':adGenSipProvisioning,'adGenSipTrunkProv':adGenSipTrunkProv,'adGenSipTrunkProvCurrentNumber':adGenSipTrunkProvCurrentNumber,'adGenSipTrunkProvLastCreateError':adGenSipTrunkProvLastCreateError,'adGenSipTrunkProvTable':adGenSipTrunkProvTable,'adGenSipTrunkProvEntry':adGenSipTrunkProvEntry,_K:adGenSipTrunkEntryIndex,'adGenSipTrunkRowStatus':adGenSipTrunkRowStatus,'adGenSipTrunkLastErrorString':adGenSipTrunkLastErrorString,'adGenSipTrunkSipProxyPrimary':adGenSipTrunkSipProxyPrimary,'adGenSipTrunkSipProxyPrimaryUdp':adGenSipTrunkSipProxyPrimaryUdp,'adGenSipTrunkSipProxySecondary':adGenSipTrunkSipProxySecondary,'adGenSipTrunkSipProxySecondaryUdp':adGenSipTrunkSipProxySecondaryUdp,'adGenSipTrunkSipOutboundProxyPrimary':adGenSipTrunkSipOutboundProxyPrimary,'adGenSipTrunkSipOutboundProxyPrimaryUdp':adGenSipTrunkSipOutboundProxyPrimaryUdp,'adGenSipTrunkSipOutboundProxySecondary':adGenSipTrunkSipOutboundProxySecondary,'adGenSipTrunkSipOutboundProxySecondaryUdp':adGenSipTrunkSipOutboundProxySecondaryUdp,'adGenSipTrunkSipDomain':adGenSipTrunkSipDomain,'adGenSipTrunkSipTrustDomain':adGenSipTrunkSipTrustDomain,'adGenSipTrunkSipTrustDomainPAssertedIdReq':adGenSipTrunkSipTrustDomainPAssertedIdReq,'adGenSipTrunkSipAuthenticate':adGenSipTrunkSipAuthenticate,'adGenSipTrunkSipDialStringSource':adGenSipTrunkSipDialStringSource,'adGenSipTrunkSipKeepAliveMethod':adGenSipTrunkSipKeepAliveMethod,'adGenSipTrunkSipKeepAliveInterval':adGenSipTrunkSipKeepAliveInterval,'adGenSipTrunkTimerRegFailRetry':adGenSipTrunkTimerRegFailRetry,'adGenSipTrunkTimerRollover':adGenSipTrunkTimerRollover,'adGenSipTrunkPrivacy':adGenSipTrunkPrivacy,'adGenSipTrunkGrammarRequestUriResolve':adGenSipTrunkGrammarRequestUriResolve,'adGenSipTrunkGrammarRequestUriHost':adGenSipTrunkGrammarRequestUriHost,'adGenSipTrunkGrammarFromHost':adGenSipTrunkGrammarFromHost,'adGenSipTrunkGrammarFromUser':adGenSipTrunkGrammarFromUser,'adGenSipTrunkGrammarPAssertedIdHost':adGenSipTrunkGrammarPAssertedIdHost,'adGenSipTrunkGrammarToHost':adGenSipTrunkGrammarToHost,'adGenSipTrunkGrammarAlertInfoUrl':adGenSipTrunkGrammarAlertInfoUrl,'adGenSipTrunkGrammarSupported100Rel':adGenSipTrunkGrammarSupported100Rel,'adGenSipTrunkGrammarProxyRequirePrivacy':adGenSipTrunkGrammarProxyRequirePrivacy,'adGenSipTrunkGrammarRequire100rel':adGenSipTrunkGrammarRequire100rel,'adGenSipTrunkGrammarUserAgent':adGenSipTrunkGrammarUserAgent,'adGenSipTrunkGrammarSdpHold':adGenSipTrunkGrammarSdpHold,'adGenSipTrunkSipRegistrarPrimary':adGenSipTrunkSipRegistrarPrimary,'adGenSipTrunkSipRegistrarPrimaryUdp':adGenSipTrunkSipRegistrarPrimaryUdp,'adGenSipTrunkSipRegistrarSecondary':adGenSipTrunkSipRegistrarSecondary,'adGenSipTrunkSipRegistrarSecondaryUdp':adGenSipTrunkSipRegistrarSecondaryUdp,'adGenSipTrunkSipRegistrarThresholdType':adGenSipTrunkSipRegistrarThresholdType,'adGenSipTrunkSipRegistrarThresholdValue':adGenSipTrunkSipRegistrarThresholdValue,'adGenSipTrunkSipRegistrarMaxConcurrentReg':adGenSipTrunkSipRegistrarMaxConcurrentReg,'adGenSipTrunkSipRegistrarExpireTime':adGenSipTrunkSipRegistrarExpireTime,'adGenSipTrunkSipRegistrarRequireExpires':adGenSipTrunkSipRegistrarRequireExpires,'adGenSipTrunkSipDscp':adGenSipTrunkSipDscp,'adGenSipTrunkRtpDscp':adGenSipTrunkRtpDscp,'adGenSipTrunkGrammarAddressScheme':adGenSipTrunkGrammarAddressScheme,'adGenSipIdentityProv':adGenSipIdentityProv,'adGenSipIdentityProvCurrentNumber':adGenSipIdentityProvCurrentNumber,'adGenSipIdentityProvLastCreateError':adGenSipIdentityProvLastCreateError,'adGenSipIdentityProvTable':adGenSipIdentityProvTable,'adGenSipIdentityProvEntry':adGenSipIdentityProvEntry,_M:adGenSipIdentityUserIndex,_N:adGenSipIdentityTrunkIndex,_O:adGenSipIdentityEntryIndex,'adGenSipIdentityRowStatus':adGenSipIdentityRowStatus,'adGenSipIdentityLastErrorString':adGenSipIdentityLastErrorString,'adGenSipIdentityRegister':adGenSipIdentityRegister,'adGenSipIdentityAuthName':adGenSipIdentityAuthName,'adGenSipIdentityPassword':adGenSipIdentityPassword,'adGenSipMgmnt':adGenSipMgmnt,'adGenSipMgmntActions':adGenSipMgmntActions,'adGenSipMgmntTable':adGenSipMgmntTable,'adGenSipMgmntEntry':adGenSipMgmntEntry,_P:adGenSipMgmntTrunkIndex,_Q:adGenSipMgmntIdentityIndex,'adGenSipMgmntForceReg':adGenSipMgmntForceReg,'adGenSipMgmntClearReg':adGenSipMgmntClearReg,'adGenSipStatus':adGenSipStatus,'adGenSipStatusRegistration':adGenSipStatusRegistration,'adGenSipStatusRegistrationTable':adGenSipStatusRegistrationTable,'adGenSipStatusRegistrationEntry':adGenSipStatusRegistrationEntry,_S:adGenSipRegistrationTrunkIndex,_T:adGenSipRegistrationIdentityIndex,'adGenSipStatusRegistrationStatus':adGenSipStatusRegistrationStatus,'adGenSipStatusRegistrationGrant':adGenSipStatusRegistrationGrant,'adGenSipStatusRegistrationExpires':adGenSipStatusRegistrationExpires,'adGenSipStatusRegistrationSuccess':adGenSipStatusRegistrationSuccess,'adGenSipStatusRegistrationFail':adGenSipStatusRegistrationFail,'adGenSipStatusRegistrationRequests':adGenSipStatusRegistrationRequests,'adGenSipStatusRegistrationChallenges':adGenSipStatusRegistrationChallenges,'adGenSipStatusRegistrationRollovers':adGenSipStatusRegistrationRollovers,'adGenSipIdentity':adGenSipIdentity})