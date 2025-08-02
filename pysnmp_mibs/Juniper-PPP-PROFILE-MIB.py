_A1='juniPppProfileGroup11'
_A0='juniPppProfileGroup10'
_z='juniPppProfileGroup8'
_y='juniPppProfileGroup7'
_x='juniPppProfileGroup6'
_w='juniPppProfileGroup5'
_v='juniPppProfileGroup4'
_u='juniPppProfileGroup3'
_t='juniPppProfileGroup2'
_s='juniPppProfileGroup'
_r='juniPppProfileMulticlassReassembly'
_q='juniPppProfileMulticlassFragmentation'
_p='juniPppProfileMulticlassTcName'
_o='juniPppProfileMultilinkMaxMultiClasses'
_n='juniPppProfileMultilinkMulticlass'
_m='juniPppProfileIpcpLockout'
_l='juniPppProfileIpcpPromptDnsOption'
_k='juniPppProfileMulticlassIndex'
_j='read-create'
_i='JuniNibbleConfig'
_h='JuniPppAuthentication'
_g='not-accessible'
_f='juniPppProfileId'
_e='juniPppProfileIgnoreMagicNumberMismatch'
_d='juniPppProfileLcpAuthentication2'
_c='juniPppProfileHashLinkSelection'
_b='juniPppProfileFragmentSize'
_a='juniPppProfileMaxReceiveReconstructedUnit'
_Z='juniPppProfileReassembly'
_Y='juniPppProfileFragmentation'
_X='juniPppProfileInitiateIpv6'
_W='juniPppProfileInitiateIp'
_V='juniPppProfileAaaProfile'
_U='juniPppProfileAuthenticatorVirtualRouter'
_T='Integer32'
_S='juniPppProfileIpcpNetmask'
_R='juniPppProfileMlppp'
_Q='juniPppProfilePassiveMode'
_P='juniPppProfileChapMaxChallengeLength'
_O='juniPppProfileChapMinChallengeLength'
_N='juniPppProfileStateLog'
_M='juniPppProfilePacketLog'
_L='juniPppProfileLcpInitialMRU'
_K='juniPppProfileIpPeerWinsPriority'
_J='juniPppProfileIpPeerDnsPriority'
_I='juniPppProfileLcpAuthentication'
_H='juniPppProfileLcpKeepalive'
_G='juniPppProfileLcpMagicNumber'
_F='juniPppProfileSetMap'
_E='obsolete'
_D='JuniEnable'
_C='read-write'
_B='current'
_A='Juniper-PPP-PROFILE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniPppAuthentication,=mibBuilder.importSymbols('Juniper-PPP-MIB',_h)
JuniEnable,JuniName,JuniNibbleConfig,JuniSetMap=mibBuilder.importSymbols('Juniper-TC',_D,'JuniName',_i,'JuniSetMap')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_T,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
juniPppProfileMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,45))
if mibBuilder.loadTexts:juniPppProfileMIB.setRevisions(('2009-09-18 07:24','2009-08-10 14:23','2007-07-12 12:15','2005-10-19 16:26','2003-11-03 21:10','2003-09-29 18:58','2003-03-11 21:59','2002-09-16 21:44','2002-09-03 22:38','2002-01-25 14:00','2002-01-16 17:58','2002-01-08 19:43','2001-10-02 12:41'))
class JuniPppProfileMulticlassTcName(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_JuniPppProfileObjects_ObjectIdentity=ObjectIdentity
juniPppProfileObjects=_JuniPppProfileObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,45,1))
_JuniPppProfile_ObjectIdentity=ObjectIdentity
juniPppProfile=_JuniPppProfile_ObjectIdentity((1,3,6,1,4,1,4874,2,2,45,1,1))
_JuniPppProfileTable_Object=MibTable
juniPppProfileTable=_JuniPppProfileTable_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1))
if mibBuilder.loadTexts:juniPppProfileTable.setStatus(_B)
_JuniPppProfileEntry_Object=MibTableRow
juniPppProfileEntry=_JuniPppProfileEntry_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1))
juniPppProfileEntry.setIndexNames((0,_A,_f))
if mibBuilder.loadTexts:juniPppProfileEntry.setStatus(_B)
_JuniPppProfileId_Type=Unsigned32
_JuniPppProfileId_Object=MibTableColumn
juniPppProfileId=_JuniPppProfileId_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,1),_JuniPppProfileId_Type())
juniPppProfileId.setMaxAccess(_g)
if mibBuilder.loadTexts:juniPppProfileId.setStatus(_B)
_JuniPppProfileSetMap_Type=JuniSetMap
_JuniPppProfileSetMap_Object=MibTableColumn
juniPppProfileSetMap=_JuniPppProfileSetMap_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,2),_JuniPppProfileSetMap_Type())
juniPppProfileSetMap.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileSetMap.setStatus(_B)
class _JuniPppProfileLcpMagicNumber_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_JuniPppProfileLcpMagicNumber_Type.__name__=_T
_JuniPppProfileLcpMagicNumber_Object=MibTableColumn
juniPppProfileLcpMagicNumber=_JuniPppProfileLcpMagicNumber_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,3),_JuniPppProfileLcpMagicNumber_Type())
juniPppProfileLcpMagicNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileLcpMagicNumber.setStatus(_B)
class _JuniPppProfileLcpKeepalive_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(30,64800))
_JuniPppProfileLcpKeepalive_Type.__name__=_T
_JuniPppProfileLcpKeepalive_Object=MibTableColumn
juniPppProfileLcpKeepalive=_JuniPppProfileLcpKeepalive_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,4),_JuniPppProfileLcpKeepalive_Type())
juniPppProfileLcpKeepalive.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileLcpKeepalive.setStatus(_B)
if mibBuilder.loadTexts:juniPppProfileLcpKeepalive.setUnits('seconds')
class _JuniPppProfileLcpAuthentication_Type(JuniPppAuthentication):defaultValue=0
_JuniPppProfileLcpAuthentication_Type.__name__=_h
_JuniPppProfileLcpAuthentication_Object=MibTableColumn
juniPppProfileLcpAuthentication=_JuniPppProfileLcpAuthentication_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,5),_JuniPppProfileLcpAuthentication_Type())
juniPppProfileLcpAuthentication.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileLcpAuthentication.setStatus('deprecated')
class _JuniPppProfileIpPeerDnsPriority_Type(JuniEnable):defaultValue=0
_JuniPppProfileIpPeerDnsPriority_Type.__name__=_D
_JuniPppProfileIpPeerDnsPriority_Object=MibTableColumn
juniPppProfileIpPeerDnsPriority=_JuniPppProfileIpPeerDnsPriority_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,6),_JuniPppProfileIpPeerDnsPriority_Type())
juniPppProfileIpPeerDnsPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileIpPeerDnsPriority.setStatus(_B)
class _JuniPppProfileIpPeerWinsPriority_Type(JuniEnable):defaultValue=0
_JuniPppProfileIpPeerWinsPriority_Type.__name__=_D
_JuniPppProfileIpPeerWinsPriority_Object=MibTableColumn
juniPppProfileIpPeerWinsPriority=_JuniPppProfileIpPeerWinsPriority_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,7),_JuniPppProfileIpPeerWinsPriority_Type())
juniPppProfileIpPeerWinsPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileIpPeerWinsPriority.setStatus(_B)
class _JuniPppProfileLcpInitialMRU_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(64,65535))
_JuniPppProfileLcpInitialMRU_Type.__name__=_T
_JuniPppProfileLcpInitialMRU_Object=MibTableColumn
juniPppProfileLcpInitialMRU=_JuniPppProfileLcpInitialMRU_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,8),_JuniPppProfileLcpInitialMRU_Type())
juniPppProfileLcpInitialMRU.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileLcpInitialMRU.setStatus(_B)
class _JuniPppProfilePacketLog_Type(JuniEnable):defaultValue=0
_JuniPppProfilePacketLog_Type.__name__=_D
_JuniPppProfilePacketLog_Object=MibTableColumn
juniPppProfilePacketLog=_JuniPppProfilePacketLog_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,9),_JuniPppProfilePacketLog_Type())
juniPppProfilePacketLog.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfilePacketLog.setStatus(_B)
class _JuniPppProfileStateLog_Type(JuniEnable):defaultValue=0
_JuniPppProfileStateLog_Type.__name__=_D
_JuniPppProfileStateLog_Object=MibTableColumn
juniPppProfileStateLog=_JuniPppProfileStateLog_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,10),_JuniPppProfileStateLog_Type())
juniPppProfileStateLog.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileStateLog.setStatus(_B)
class _JuniPppProfileChapMinChallengeLength_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,63))
_JuniPppProfileChapMinChallengeLength_Type.__name__=_T
_JuniPppProfileChapMinChallengeLength_Object=MibTableColumn
juniPppProfileChapMinChallengeLength=_JuniPppProfileChapMinChallengeLength_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,11),_JuniPppProfileChapMinChallengeLength_Type())
juniPppProfileChapMinChallengeLength.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileChapMinChallengeLength.setStatus(_B)
class _JuniPppProfileChapMaxChallengeLength_Type(Integer32):defaultValue=32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,63))
_JuniPppProfileChapMaxChallengeLength_Type.__name__=_T
_JuniPppProfileChapMaxChallengeLength_Object=MibTableColumn
juniPppProfileChapMaxChallengeLength=_JuniPppProfileChapMaxChallengeLength_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,12),_JuniPppProfileChapMaxChallengeLength_Type())
juniPppProfileChapMaxChallengeLength.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileChapMaxChallengeLength.setStatus(_B)
class _JuniPppProfilePassiveMode_Type(JuniEnable):defaultValue=0
_JuniPppProfilePassiveMode_Type.__name__=_D
_JuniPppProfilePassiveMode_Object=MibTableColumn
juniPppProfilePassiveMode=_JuniPppProfilePassiveMode_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,13),_JuniPppProfilePassiveMode_Type())
juniPppProfilePassiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfilePassiveMode.setStatus(_B)
class _JuniPppProfileMlppp_Type(JuniEnable):defaultValue=0
_JuniPppProfileMlppp_Type.__name__=_D
_JuniPppProfileMlppp_Object=MibTableColumn
juniPppProfileMlppp=_JuniPppProfileMlppp_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,14),_JuniPppProfileMlppp_Type())
juniPppProfileMlppp.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileMlppp.setStatus(_B)
class _JuniPppProfileIpcpNetmask_Type(JuniEnable):defaultValue=0
_JuniPppProfileIpcpNetmask_Type.__name__=_D
_JuniPppProfileIpcpNetmask_Object=MibTableColumn
juniPppProfileIpcpNetmask=_JuniPppProfileIpcpNetmask_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,15),_JuniPppProfileIpcpNetmask_Type())
juniPppProfileIpcpNetmask.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileIpcpNetmask.setStatus(_B)
_JuniPppProfileAuthenticatorVirtualRouter_Type=JuniName
_JuniPppProfileAuthenticatorVirtualRouter_Object=MibTableColumn
juniPppProfileAuthenticatorVirtualRouter=_JuniPppProfileAuthenticatorVirtualRouter_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,16),_JuniPppProfileAuthenticatorVirtualRouter_Type())
juniPppProfileAuthenticatorVirtualRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileAuthenticatorVirtualRouter.setStatus(_B)
_JuniPppProfileAaaProfile_Type=JuniName
_JuniPppProfileAaaProfile_Object=MibTableColumn
juniPppProfileAaaProfile=_JuniPppProfileAaaProfile_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,17),_JuniPppProfileAaaProfile_Type())
juniPppProfileAaaProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileAaaProfile.setStatus(_B)
class _JuniPppProfileInitiateIp_Type(JuniEnable):defaultValue=0
_JuniPppProfileInitiateIp_Type.__name__=_D
_JuniPppProfileInitiateIp_Object=MibTableColumn
juniPppProfileInitiateIp=_JuniPppProfileInitiateIp_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,18),_JuniPppProfileInitiateIp_Type())
juniPppProfileInitiateIp.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileInitiateIp.setStatus(_B)
class _JuniPppProfileInitiateIpv6_Type(JuniEnable):defaultValue=0
_JuniPppProfileInitiateIpv6_Type.__name__=_D
_JuniPppProfileInitiateIpv6_Object=MibTableColumn
juniPppProfileInitiateIpv6=_JuniPppProfileInitiateIpv6_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,19),_JuniPppProfileInitiateIpv6_Type())
juniPppProfileInitiateIpv6.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileInitiateIpv6.setStatus(_B)
class _JuniPppProfileFragmentation_Type(JuniEnable):defaultValue=0
_JuniPppProfileFragmentation_Type.__name__=_D
_JuniPppProfileFragmentation_Object=MibTableColumn
juniPppProfileFragmentation=_JuniPppProfileFragmentation_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,20),_JuniPppProfileFragmentation_Type())
juniPppProfileFragmentation.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileFragmentation.setStatus(_B)
class _JuniPppProfileReassembly_Type(JuniEnable):defaultValue=0
_JuniPppProfileReassembly_Type.__name__=_D
_JuniPppProfileReassembly_Object=MibTableColumn
juniPppProfileReassembly=_JuniPppProfileReassembly_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,21),_JuniPppProfileReassembly_Type())
juniPppProfileReassembly.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileReassembly.setStatus(_B)
class _JuniPppProfileMaxReceiveReconstructedUnit_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(64,65535))
_JuniPppProfileMaxReceiveReconstructedUnit_Type.__name__=_T
_JuniPppProfileMaxReceiveReconstructedUnit_Object=MibTableColumn
juniPppProfileMaxReceiveReconstructedUnit=_JuniPppProfileMaxReceiveReconstructedUnit_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,22),_JuniPppProfileMaxReceiveReconstructedUnit_Type())
juniPppProfileMaxReceiveReconstructedUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileMaxReceiveReconstructedUnit.setStatus(_B)
class _JuniPppProfileFragmentSize_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(128,65535))
_JuniPppProfileFragmentSize_Type.__name__=_T
_JuniPppProfileFragmentSize_Object=MibTableColumn
juniPppProfileFragmentSize=_JuniPppProfileFragmentSize_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,23),_JuniPppProfileFragmentSize_Type())
juniPppProfileFragmentSize.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileFragmentSize.setStatus(_B)
class _JuniPppProfileHashLinkSelection_Type(JuniEnable):defaultValue=0
_JuniPppProfileHashLinkSelection_Type.__name__=_D
_JuniPppProfileHashLinkSelection_Object=MibTableColumn
juniPppProfileHashLinkSelection=_JuniPppProfileHashLinkSelection_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,24),_JuniPppProfileHashLinkSelection_Type())
juniPppProfileHashLinkSelection.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileHashLinkSelection.setStatus(_B)
class _JuniPppProfileLcpAuthentication2_Type(JuniNibbleConfig):defaultValue=0
_JuniPppProfileLcpAuthentication2_Type.__name__=_i
_JuniPppProfileLcpAuthentication2_Object=MibTableColumn
juniPppProfileLcpAuthentication2=_JuniPppProfileLcpAuthentication2_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,25),_JuniPppProfileLcpAuthentication2_Type())
juniPppProfileLcpAuthentication2.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileLcpAuthentication2.setStatus(_B)
class _JuniPppProfileIgnoreMagicNumberMismatch_Type(JuniEnable):defaultValue=0
_JuniPppProfileIgnoreMagicNumberMismatch_Type.__name__=_D
_JuniPppProfileIgnoreMagicNumberMismatch_Object=MibTableColumn
juniPppProfileIgnoreMagicNumberMismatch=_JuniPppProfileIgnoreMagicNumberMismatch_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,26),_JuniPppProfileIgnoreMagicNumberMismatch_Type())
juniPppProfileIgnoreMagicNumberMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileIgnoreMagicNumberMismatch.setStatus(_B)
class _JuniPppProfileIpcpPromptDnsOption_Type(JuniEnable):defaultValue=0
_JuniPppProfileIpcpPromptDnsOption_Type.__name__=_D
_JuniPppProfileIpcpPromptDnsOption_Object=MibTableColumn
juniPppProfileIpcpPromptDnsOption=_JuniPppProfileIpcpPromptDnsOption_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,27),_JuniPppProfileIpcpPromptDnsOption_Type())
juniPppProfileIpcpPromptDnsOption.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileIpcpPromptDnsOption.setStatus(_B)
class _JuniPppProfileIpcpLockout_Type(JuniEnable):defaultValue=0
_JuniPppProfileIpcpLockout_Type.__name__=_D
_JuniPppProfileIpcpLockout_Object=MibTableColumn
juniPppProfileIpcpLockout=_JuniPppProfileIpcpLockout_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,28),_JuniPppProfileIpcpLockout_Type())
juniPppProfileIpcpLockout.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileIpcpLockout.setStatus(_B)
class _JuniPppProfileMultilinkMulticlass_Type(JuniEnable):defaultValue=0
_JuniPppProfileMultilinkMulticlass_Type.__name__=_D
_JuniPppProfileMultilinkMulticlass_Object=MibTableColumn
juniPppProfileMultilinkMulticlass=_JuniPppProfileMultilinkMulticlass_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,29),_JuniPppProfileMultilinkMulticlass_Type())
juniPppProfileMultilinkMulticlass.setMaxAccess(_j)
if mibBuilder.loadTexts:juniPppProfileMultilinkMulticlass.setStatus(_B)
class _JuniPppProfileMultilinkMaxMultiClasses_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_JuniPppProfileMultilinkMaxMultiClasses_Type.__name__=_T
_JuniPppProfileMultilinkMaxMultiClasses_Object=MibTableColumn
juniPppProfileMultilinkMaxMultiClasses=_JuniPppProfileMultilinkMaxMultiClasses_Object((1,3,6,1,4,1,4874,2,2,45,1,1,1,1,30),_JuniPppProfileMultilinkMaxMultiClasses_Type())
juniPppProfileMultilinkMaxMultiClasses.setMaxAccess(_j)
if mibBuilder.loadTexts:juniPppProfileMultilinkMaxMultiClasses.setStatus(_B)
_JuniPppProfileMulticlassTraffiClassTable_Object=MibTable
juniPppProfileMulticlassTraffiClassTable=_JuniPppProfileMulticlassTraffiClassTable_Object((1,3,6,1,4,1,4874,2,2,45,1,1,2))
if mibBuilder.loadTexts:juniPppProfileMulticlassTraffiClassTable.setStatus(_B)
_JuniPppProfileMulticlassTrafficClassEntry_Object=MibTableRow
juniPppProfileMulticlassTrafficClassEntry=_JuniPppProfileMulticlassTrafficClassEntry_Object((1,3,6,1,4,1,4874,2,2,45,1,1,2,1))
juniPppProfileMulticlassTrafficClassEntry.setIndexNames((0,_A,_f),(0,_A,_k))
if mibBuilder.loadTexts:juniPppProfileMulticlassTrafficClassEntry.setStatus(_B)
_JuniPppProfileMulticlassId_Type=Unsigned32
_JuniPppProfileMulticlassId_Object=MibTableColumn
juniPppProfileMulticlassId=_JuniPppProfileMulticlassId_Object((1,3,6,1,4,1,4874,2,2,45,1,1,2,1,1),_JuniPppProfileMulticlassId_Type())
juniPppProfileMulticlassId.setMaxAccess(_g)
if mibBuilder.loadTexts:juniPppProfileMulticlassId.setStatus(_B)
class _JuniPppProfileMulticlassIndex_Type(Integer32):defaultValue=15
_JuniPppProfileMulticlassIndex_Type.__name__=_T
_JuniPppProfileMulticlassIndex_Object=MibTableColumn
juniPppProfileMulticlassIndex=_JuniPppProfileMulticlassIndex_Object((1,3,6,1,4,1,4874,2,2,45,1,1,2,1,2),_JuniPppProfileMulticlassIndex_Type())
juniPppProfileMulticlassIndex.setMaxAccess(_g)
if mibBuilder.loadTexts:juniPppProfileMulticlassIndex.setStatus(_B)
_JuniPppProfileMulticlassTcName_Type=JuniPppProfileMulticlassTcName
_JuniPppProfileMulticlassTcName_Object=MibTableColumn
juniPppProfileMulticlassTcName=_JuniPppProfileMulticlassTcName_Object((1,3,6,1,4,1,4874,2,2,45,1,1,2,1,3),_JuniPppProfileMulticlassTcName_Type())
juniPppProfileMulticlassTcName.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileMulticlassTcName.setStatus(_B)
class _JuniPppProfileMulticlassFragmentation_Type(JuniEnable):defaultValue=0
_JuniPppProfileMulticlassFragmentation_Type.__name__=_D
_JuniPppProfileMulticlassFragmentation_Object=MibTableColumn
juniPppProfileMulticlassFragmentation=_JuniPppProfileMulticlassFragmentation_Object((1,3,6,1,4,1,4874,2,2,45,1,1,2,1,4),_JuniPppProfileMulticlassFragmentation_Type())
juniPppProfileMulticlassFragmentation.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileMulticlassFragmentation.setStatus(_B)
class _JuniPppProfileMulticlassReassembly_Type(JuniEnable):defaultValue=0
_JuniPppProfileMulticlassReassembly_Type.__name__=_D
_JuniPppProfileMulticlassReassembly_Object=MibTableColumn
juniPppProfileMulticlassReassembly=_JuniPppProfileMulticlassReassembly_Object((1,3,6,1,4,1,4874,2,2,45,1,1,2,1,5),_JuniPppProfileMulticlassReassembly_Type())
juniPppProfileMulticlassReassembly.setMaxAccess(_C)
if mibBuilder.loadTexts:juniPppProfileMulticlassReassembly.setStatus(_B)
_JuniPppProfileConformance_ObjectIdentity=ObjectIdentity
juniPppProfileConformance=_JuniPppProfileConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,45,4))
_JuniPppProfileCompliances_ObjectIdentity=ObjectIdentity
juniPppProfileCompliances=_JuniPppProfileCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,45,4,1))
_JuniPppProfileGroups_ObjectIdentity=ObjectIdentity
juniPppProfileGroups=_JuniPppProfileGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,45,4,2))
juniPppProfileGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,45,4,2,1))
juniPppProfileGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:juniPppProfileGroup.setStatus(_E)
juniPppProfileGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,45,4,2,2))
juniPppProfileGroup2.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:juniPppProfileGroup2.setStatus(_E)
juniPppProfileGroup3=ObjectGroup((1,3,6,1,4,1,4874,2,2,45,4,2,3))
juniPppProfileGroup3.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:juniPppProfileGroup3.setStatus(_E)
juniPppProfileGroup4=ObjectGroup((1,3,6,1,4,1,4874,2,2,45,4,2,4))
juniPppProfileGroup4.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_U)))
if mibBuilder.loadTexts:juniPppProfileGroup4.setStatus(_E)
juniPppProfileGroup5=ObjectGroup((1,3,6,1,4,1,4874,2,2,45,4,2,5))
juniPppProfileGroup5.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:juniPppProfileGroup5.setStatus(_E)
juniPppProfileGroup6=ObjectGroup((1,3,6,1,4,1,4874,2,2,45,4,2,6))
juniPppProfileGroup6.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:juniPppProfileGroup6.setStatus(_E)
juniPppProfileGroup7=ObjectGroup((1,3,6,1,4,1,4874,2,2,45,4,2,7))
juniPppProfileGroup7.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:juniPppProfileGroup7.setStatus(_E)
juniPppProfileGroup8=ObjectGroup((1,3,6,1,4,1,4874,2,2,45,4,2,8))
juniPppProfileGroup8.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:juniPppProfileGroup8.setStatus(_E)
juniPppProfileGroup9=ObjectGroup((1,3,6,1,4,1,4874,2,2,45,4,2,9))
juniPppProfileGroup9.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:juniPppProfileGroup9.setStatus(_E)
juniPppProfileGroup10=ObjectGroup((1,3,6,1,4,1,4874,2,2,45,4,2,10))
juniPppProfileGroup10.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:juniPppProfileGroup10.setStatus(_E)
juniPppProfileGroup11=ObjectGroup((1,3,6,1,4,1,4874,2,2,45,4,2,11))
juniPppProfileGroup11.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:juniPppProfileGroup11.setStatus(_B)
juniPppProfileGroup12=ObjectGroup((1,3,6,1,4,1,4874,2,2,45,4,2,12))
juniPppProfileGroup12.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:juniPppProfileGroup12.setStatus(_B)
juniPppProfileMulticlassTrafficClassGroup1=ObjectGroup((1,3,6,1,4,1,4874,2,2,45,4,2,13))
juniPppProfileMulticlassTrafficClassGroup1.setObjects(*((_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:juniPppProfileMulticlassTrafficClassGroup1.setStatus(_B)
juniPppProfileCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,45,4,1,1))
juniPppProfileCompliance.setObjects((_A,_s))
if mibBuilder.loadTexts:juniPppProfileCompliance.setStatus(_E)
juniPppProfileCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,45,4,1,2))
juniPppProfileCompliance2.setObjects((_A,_t))
if mibBuilder.loadTexts:juniPppProfileCompliance2.setStatus(_E)
juniPppProfileCompliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,45,4,1,3))
juniPppProfileCompliance3.setObjects((_A,_u))
if mibBuilder.loadTexts:juniPppProfileCompliance3.setStatus(_E)
juniPppProfileCompliance4=ModuleCompliance((1,3,6,1,4,1,4874,2,2,45,4,1,4))
juniPppProfileCompliance4.setObjects((_A,_v))
if mibBuilder.loadTexts:juniPppProfileCompliance4.setStatus(_E)
juniPppProfileCompliance5=ModuleCompliance((1,3,6,1,4,1,4874,2,2,45,4,1,5))
juniPppProfileCompliance5.setObjects((_A,_w))
if mibBuilder.loadTexts:juniPppProfileCompliance5.setStatus(_E)
juniPppProfileCompliance6=ModuleCompliance((1,3,6,1,4,1,4874,2,2,45,4,1,6))
juniPppProfileCompliance6.setObjects((_A,_x))
if mibBuilder.loadTexts:juniPppProfileCompliance6.setStatus(_E)
juniPppProfileCompliance7=ModuleCompliance((1,3,6,1,4,1,4874,2,2,45,4,1,7))
juniPppProfileCompliance7.setObjects((_A,_y))
if mibBuilder.loadTexts:juniPppProfileCompliance7.setStatus(_E)
juniPppProfileCompliance8=ModuleCompliance((1,3,6,1,4,1,4874,2,2,45,4,1,8))
juniPppProfileCompliance8.setObjects((_A,_z))
if mibBuilder.loadTexts:juniPppProfileCompliance8.setStatus(_E)
juniPppProfileCompliance9=ModuleCompliance((1,3,6,1,4,1,4874,2,2,45,4,1,9))
juniPppProfileCompliance9.setObjects((_A,_A0))
if mibBuilder.loadTexts:juniPppProfileCompliance9.setStatus(_E)
juniPppProfileCompliance10=ModuleCompliance((1,3,6,1,4,1,4874,2,2,45,4,1,10))
juniPppProfileCompliance10.setObjects((_A,_A1))
if mibBuilder.loadTexts:juniPppProfileCompliance10.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'JuniPppProfileMulticlassTcName':JuniPppProfileMulticlassTcName,'juniPppProfileMIB':juniPppProfileMIB,'juniPppProfileObjects':juniPppProfileObjects,'juniPppProfile':juniPppProfile,'juniPppProfileTable':juniPppProfileTable,'juniPppProfileEntry':juniPppProfileEntry,_f:juniPppProfileId,_F:juniPppProfileSetMap,_G:juniPppProfileLcpMagicNumber,_H:juniPppProfileLcpKeepalive,_I:juniPppProfileLcpAuthentication,_J:juniPppProfileIpPeerDnsPriority,_K:juniPppProfileIpPeerWinsPriority,_L:juniPppProfileLcpInitialMRU,_M:juniPppProfilePacketLog,_N:juniPppProfileStateLog,_O:juniPppProfileChapMinChallengeLength,_P:juniPppProfileChapMaxChallengeLength,_Q:juniPppProfilePassiveMode,_R:juniPppProfileMlppp,_S:juniPppProfileIpcpNetmask,_U:juniPppProfileAuthenticatorVirtualRouter,_V:juniPppProfileAaaProfile,_W:juniPppProfileInitiateIp,_X:juniPppProfileInitiateIpv6,_Y:juniPppProfileFragmentation,_Z:juniPppProfileReassembly,_a:juniPppProfileMaxReceiveReconstructedUnit,_b:juniPppProfileFragmentSize,_c:juniPppProfileHashLinkSelection,_d:juniPppProfileLcpAuthentication2,_e:juniPppProfileIgnoreMagicNumberMismatch,_l:juniPppProfileIpcpPromptDnsOption,_m:juniPppProfileIpcpLockout,_n:juniPppProfileMultilinkMulticlass,_o:juniPppProfileMultilinkMaxMultiClasses,'juniPppProfileMulticlassTraffiClassTable':juniPppProfileMulticlassTraffiClassTable,'juniPppProfileMulticlassTrafficClassEntry':juniPppProfileMulticlassTrafficClassEntry,'juniPppProfileMulticlassId':juniPppProfileMulticlassId,_k:juniPppProfileMulticlassIndex,_p:juniPppProfileMulticlassTcName,_q:juniPppProfileMulticlassFragmentation,_r:juniPppProfileMulticlassReassembly,'juniPppProfileConformance':juniPppProfileConformance,'juniPppProfileCompliances':juniPppProfileCompliances,'juniPppProfileCompliance':juniPppProfileCompliance,'juniPppProfileCompliance2':juniPppProfileCompliance2,'juniPppProfileCompliance3':juniPppProfileCompliance3,'juniPppProfileCompliance4':juniPppProfileCompliance4,'juniPppProfileCompliance5':juniPppProfileCompliance5,'juniPppProfileCompliance6':juniPppProfileCompliance6,'juniPppProfileCompliance7':juniPppProfileCompliance7,'juniPppProfileCompliance8':juniPppProfileCompliance8,'juniPppProfileCompliance9':juniPppProfileCompliance9,'juniPppProfileCompliance10':juniPppProfileCompliance10,'juniPppProfileGroups':juniPppProfileGroups,_s:juniPppProfileGroup,_t:juniPppProfileGroup2,_u:juniPppProfileGroup3,_v:juniPppProfileGroup4,_w:juniPppProfileGroup5,_x:juniPppProfileGroup6,_y:juniPppProfileGroup7,_z:juniPppProfileGroup8,'juniPppProfileGroup9':juniPppProfileGroup9,_A0:juniPppProfileGroup10,_A1:juniPppProfileGroup11,'juniPppProfileGroup12':juniPppProfileGroup12,'juniPppProfileMulticlassTrafficClassGroup1':juniPppProfileMulticlassTrafficClassGroup1})