_BN='ciscoVcClassGroup'
_BM='ciscoDslPVCGroup'
_BL='ciscoIpPoolGroup'
_BK='ciscoVirtualTemplateGroup'
_BJ='ciscoNrpSlotGroup'
_BI='cdslVcClassRowStatus'
_BH='cdslVcClassVirtualTemplate'
_BG='cdslVcClassVbrNrtInputMBS'
_BF='cdslVcClassVbrNrtInputSCR'
_BE='cdslVcClassVbrNrtInputPCR'
_BD='cdslVcClassVbrNrtInputBP'
_BC='cdslVcClassVbrNrtSCR'
_BB='cdslVcClassVbrNrtPCR'
_BA='cdslVcClassUbrPlusInputMCR'
_B9='cdslVcClassUbrPlusInputPCR'
_B8='cdslVcClassUbrPlusMCR'
_B7='cdslVcClassUbrPlusPCR'
_B6='cdslVcClassUbrInputPCR'
_B5='cdslVcClassUbrPCR'
_B4='cdslVcClassTransmitPriority'
_B3='cdslVcClassProtocolIpxBC'
_B2='cdslVcClassProtocolIpBC'
_B1='cdslVcClassOamSvcLF'
_B0='cdslVcClassOamSvcManaged'
_A_='cdslVcClassOamPvcLF'
_Az='cdslVcClassOamPvcManaged'
_Ay='cdslVcClassOamRetryDownCount'
_Ax='cdslVcClassOamRetryUpCount'
_Aw='cdslVcClassInarp'
_Av='cdslVcClassILMIManage'
_Au='cdslVcClassIdleMTR'
_At='cdslVcClassIdleTimeout'
_As='cdslVcClassMuxLinkType'
_Ar='cdslVcClassEncapsulation'
_Aq='cdslVcClassBroadcast'
_Ap='cdslVcClassAbrIORDF'
_Ao='cdslVcClassAbrIORIF'
_An='cdslVcClassAbrMcr'
_Am='cdslVcClassAbrPCR'
_Al='cdslVcClassQosType'
_Ak='cdslVcClassType'
_Aj='cdslMaxVcClasses'
_Ai='cdslVcClasses'
_Ah='cdslAtmPvcAbrMCR'
_Ag='cdslAtmPvcQosType'
_Af='cdslAtmPvcRowStatus'
_Ae='cdslAtmPvcVirtualTemplate'
_Ad='cdslAtmPvcVbrNrtSCR'
_Ac='cdslAtmPvcVbrNrtPCR'
_Ab='cdslAtmPvcUbrPlusMCR'
_Aa='cdslAtmPvcUbrPlusPCR'
_AZ='cdslAtmPvcUbrPCR'
_AY='cdslAtmPvcProtocolIpxBC'
_AX='cdslAtmPvcProtocolIpBC'
_AW='cdslAtmPvcOamPvcLF'
_AV='cdslAtmPvcOamPvcManaged'
_AU='cdslAtmPvcOamRetryDownCount'
_AT='cdslAtmPvcOamRetryUpCount'
_AS='cdslAtmPvcInarp'
_AR='cdslAtmPvcILMIManage'
_AQ='cdslAtmPvcMuxLinkType'
_AP='cdslAtmPvcEncapsulation'
_AO='cdslAtmPvcBroadcast'
_AN='cdslAtmPvcAbrIORDF'
_AM='cdslAtmPvcAbrIORIF'
_AL='cdslAtmPvcAbrPCR'
_AK='cdslAtmPvcClass'
_AJ='cdslAtmPvcSubIfNumber'
_AI='cdslAtmPvcName'
_AH='cdslPppOverAtmPvcs'
_AG='cdslLocalIpAddrRangeRowStatus'
_AF='cdslLocalIpAddrPoolInUseAddresses'
_AE='cdslLocalIpAddrPoolFreeAddresses'
_AD='cdslMaxLocalIpAddrPools'
_AC='cdslLocalIpAddrPools'
_AB='cdslVTRowStatus'
_AA='cdslVTPppUseTacacs'
_A9='cdslVTPppPapEncrypType'
_A8='cdslVTPppPapPassword'
_A7='cdslVTPppPapUserName'
_A6='cdslVTPppChapWaitPeer'
_A5='cdslVTPppChapRefuse'
_A4='cdslVTPppChapEncrypType'
_A3='cdslVTPppChapPassword'
_A2='cdslVTPppChapHost'
_A1='cdslVTPppAuthMSChap'
_A0='cdslVTPppAuthChap'
_z='cdslVTPppAuthPap'
_y='cdslVTPeerIpAddrPool'
_x='cdslVTPeerIpAddressMethod'
_w='cdslVTIpIfIndex'
_v='cdslVTIpAddressMask'
_u='cdslVTIpAddress'
_t='cdslVTIpAddressMethod'
_s='cdslVirtualTemplates'
_r='cdslMaxVirtualTemplates'
_q='cdslNrpIpAddress'
_p='cdslNrpNumber'
_o='cdslMaxNrps'
_n='seconds'
_m='cdslVcClassName'
_l='aal5ciscoppp'
_k='aal5qsaal'
_j='aal5ilmi'
_i='aal34smds'
_h='aal5nlpid'
_g='aal5mux'
_f='aal5snap'
_e='default'
_d='vbrNrt'
_c='ubrPlus'
_b='ubrDefault'
_a='cdslAtmPvcVci'
_Z='cdslAtmPvcVpi'
_Y='cdslLocalIpAddrRangeHighAddr'
_X='cdslLocalIpAddrRangeLowAddr'
_W='negotiate'
_V='cdslVTIndex'
_U='IpAddress'
_T='ifIndex'
_S='InterfaceIndexOrZero'
_R='IF-MIB'
_Q='cdslLocalIpAddrPoolName'
_P='TruthValue'
_O='RowStatus'
_N='Gauge32'
_M='unknown'
_L='true'
_K='false'
_J='not-accessible'
_I='DisplayString'
_H='cdslNrpSlotIndex'
_G='kbps'
_F='Unsigned32'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='CISCO-DSL-PROVISION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_R,_S,_T)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_N,_D,_U,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress',_O,'TextualConvention',_P)
ciscoDslProvisionMIB=ModuleIdentity((1,3,6,1,4,1,9,10,30))
if mibBuilder.loadTexts:ciscoDslProvisionMIB.setRevisions(('2005-12-14 00:00','1999-06-18 00:00'))
_CiscoDslProvMIBObjects_ObjectIdentity=ObjectIdentity
ciscoDslProvMIBObjects=_CiscoDslProvMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,30,1))
_CdslNrpSlot_ObjectIdentity=ObjectIdentity
cdslNrpSlot=_CdslNrpSlot_ObjectIdentity((1,3,6,1,4,1,9,10,30,1,1))
class _CdslMaxNrps_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdslMaxNrps_Type.__name__=_F
_CdslMaxNrps_Object=MibScalar
cdslMaxNrps=_CdslMaxNrps_Object((1,3,6,1,4,1,9,10,30,1,1,1),_CdslMaxNrps_Type())
cdslMaxNrps.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslMaxNrps.setStatus(_A)
class _CdslNrpNumber_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdslNrpNumber_Type.__name__=_N
_CdslNrpNumber_Object=MibScalar
cdslNrpNumber=_CdslNrpNumber_Object((1,3,6,1,4,1,9,10,30,1,1,2),_CdslNrpNumber_Type())
cdslNrpNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslNrpNumber.setStatus(_A)
_CdslNrpIpAddressTable_Object=MibTable
cdslNrpIpAddressTable=_CdslNrpIpAddressTable_Object((1,3,6,1,4,1,9,10,30,1,1,3))
if mibBuilder.loadTexts:cdslNrpIpAddressTable.setStatus(_A)
_CdslNrpIpAddressEntry_Object=MibTableRow
cdslNrpIpAddressEntry=_CdslNrpIpAddressEntry_Object((1,3,6,1,4,1,9,10,30,1,1,3,1))
cdslNrpIpAddressEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cdslNrpIpAddressEntry.setStatus(_A)
class _CdslNrpSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CdslNrpSlotIndex_Type.__name__=_D
_CdslNrpSlotIndex_Object=MibTableColumn
cdslNrpSlotIndex=_CdslNrpSlotIndex_Object((1,3,6,1,4,1,9,10,30,1,1,3,1,1),_CdslNrpSlotIndex_Type())
cdslNrpSlotIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cdslNrpSlotIndex.setStatus(_A)
_CdslNrpIpAddress_Type=IpAddress
_CdslNrpIpAddress_Object=MibTableColumn
cdslNrpIpAddress=_CdslNrpIpAddress_Object((1,3,6,1,4,1,9,10,30,1,1,3,1,2),_CdslNrpIpAddress_Type())
cdslNrpIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslNrpIpAddress.setStatus(_A)
_CdslVirtualTemplate_ObjectIdentity=ObjectIdentity
cdslVirtualTemplate=_CdslVirtualTemplate_ObjectIdentity((1,3,6,1,4,1,9,10,30,1,2))
_CdslVirtualTemplateNumberTable_Object=MibTable
cdslVirtualTemplateNumberTable=_CdslVirtualTemplateNumberTable_Object((1,3,6,1,4,1,9,10,30,1,2,1))
if mibBuilder.loadTexts:cdslVirtualTemplateNumberTable.setStatus(_A)
_CdslVirtualTemplateNumberEntry_Object=MibTableRow
cdslVirtualTemplateNumberEntry=_CdslVirtualTemplateNumberEntry_Object((1,3,6,1,4,1,9,10,30,1,2,1,1))
cdslVirtualTemplateNumberEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cdslVirtualTemplateNumberEntry.setStatus(_A)
class _CdslMaxVirtualTemplates_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdslMaxVirtualTemplates_Type.__name__=_F
_CdslMaxVirtualTemplates_Object=MibTableColumn
cdslMaxVirtualTemplates=_CdslMaxVirtualTemplates_Object((1,3,6,1,4,1,9,10,30,1,2,1,1,1),_CdslMaxVirtualTemplates_Type())
cdslMaxVirtualTemplates.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslMaxVirtualTemplates.setStatus(_A)
class _CdslVirtualTemplates_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdslVirtualTemplates_Type.__name__=_N
_CdslVirtualTemplates_Object=MibTableColumn
cdslVirtualTemplates=_CdslVirtualTemplates_Object((1,3,6,1,4,1,9,10,30,1,2,1,1,2),_CdslVirtualTemplates_Type())
cdslVirtualTemplates.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslVirtualTemplates.setStatus(_A)
_CdslVirtualTemplateTable_Object=MibTable
cdslVirtualTemplateTable=_CdslVirtualTemplateTable_Object((1,3,6,1,4,1,9,10,30,1,2,2))
if mibBuilder.loadTexts:cdslVirtualTemplateTable.setStatus(_A)
_CdslVirtualTemplateEntry_Object=MibTableRow
cdslVirtualTemplateEntry=_CdslVirtualTemplateEntry_Object((1,3,6,1,4,1,9,10,30,1,2,2,1))
cdslVirtualTemplateEntry.setIndexNames((0,_B,_H),(0,_B,_V))
if mibBuilder.loadTexts:cdslVirtualTemplateEntry.setStatus(_A)
class _CdslVTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CdslVTIndex_Type.__name__=_D
_CdslVTIndex_Object=MibTableColumn
cdslVTIndex=_CdslVTIndex_Object((1,3,6,1,4,1,9,10,30,1,2,2,1,1),_CdslVTIndex_Type())
cdslVTIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cdslVTIndex.setStatus(_A)
class _CdslVTIpAddressMethod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('ipAddress',1),('interfaceIp',2),(_W,3)))
_CdslVTIpAddressMethod_Type.__name__=_D
_CdslVTIpAddressMethod_Object=MibTableColumn
cdslVTIpAddressMethod=_CdslVTIpAddressMethod_Object((1,3,6,1,4,1,9,10,30,1,2,2,1,2),_CdslVTIpAddressMethod_Type())
cdslVTIpAddressMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVTIpAddressMethod.setStatus(_A)
_CdslVTIpAddress_Type=IpAddress
_CdslVTIpAddress_Object=MibTableColumn
cdslVTIpAddress=_CdslVTIpAddress_Object((1,3,6,1,4,1,9,10,30,1,2,2,1,3),_CdslVTIpAddress_Type())
cdslVTIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVTIpAddress.setStatus(_A)
class _CdslVTIpAddressMask_Type(IpAddress):defaultHexValue='ffffffff'
_CdslVTIpAddressMask_Type.__name__=_U
_CdslVTIpAddressMask_Object=MibTableColumn
cdslVTIpAddressMask=_CdslVTIpAddressMask_Object((1,3,6,1,4,1,9,10,30,1,2,2,1,4),_CdslVTIpAddressMask_Type())
cdslVTIpAddressMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVTIpAddressMask.setStatus(_A)
class _CdslVTIpIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_CdslVTIpIfIndex_Type.__name__=_S
_CdslVTIpIfIndex_Object=MibTableColumn
cdslVTIpIfIndex=_CdslVTIpIfIndex_Object((1,3,6,1,4,1,9,10,30,1,2,2,1,5),_CdslVTIpIfIndex_Type())
cdslVTIpIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVTIpIfIndex.setStatus(_A)
class _CdslVTPeerIpAddressMethod_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),(_W,1),('ipAddressPool',2)))
_CdslVTPeerIpAddressMethod_Type.__name__=_D
_CdslVTPeerIpAddressMethod_Object=MibTableColumn
cdslVTPeerIpAddressMethod=_CdslVTPeerIpAddressMethod_Object((1,3,6,1,4,1,9,10,30,1,2,2,1,6),_CdslVTPeerIpAddressMethod_Type())
cdslVTPeerIpAddressMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVTPeerIpAddressMethod.setStatus(_A)
class _CdslVTPeerIpAddrPool_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CdslVTPeerIpAddrPool_Type.__name__=_I
_CdslVTPeerIpAddrPool_Object=MibTableColumn
cdslVTPeerIpAddrPool=_CdslVTPeerIpAddrPool_Object((1,3,6,1,4,1,9,10,30,1,2,2,1,7),_CdslVTPeerIpAddrPool_Type())
cdslVTPeerIpAddrPool.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVTPeerIpAddrPool.setStatus(_A)
class _CdslVTPppAuthChap_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CdslVTPppAuthChap_Type.__name__=_D
_CdslVTPppAuthChap_Object=MibTableColumn
cdslVTPppAuthChap=_CdslVTPppAuthChap_Object((1,3,6,1,4,1,9,10,30,1,2,2,1,8),_CdslVTPppAuthChap_Type())
cdslVTPppAuthChap.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVTPppAuthChap.setStatus(_A)
class _CdslVTPppAuthMSChap_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CdslVTPppAuthMSChap_Type.__name__=_D
_CdslVTPppAuthMSChap_Object=MibTableColumn
cdslVTPppAuthMSChap=_CdslVTPppAuthMSChap_Object((1,3,6,1,4,1,9,10,30,1,2,2,1,9),_CdslVTPppAuthMSChap_Type())
cdslVTPppAuthMSChap.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVTPppAuthMSChap.setStatus(_A)
class _CdslVTPppAuthPap_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CdslVTPppAuthPap_Type.__name__=_D
_CdslVTPppAuthPap_Object=MibTableColumn
cdslVTPppAuthPap=_CdslVTPppAuthPap_Object((1,3,6,1,4,1,9,10,30,1,2,2,1,10),_CdslVTPppAuthPap_Type())
cdslVTPppAuthPap.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVTPppAuthPap.setStatus(_A)
class _CdslVTPppChapHost_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CdslVTPppChapHost_Type.__name__=_I
_CdslVTPppChapHost_Object=MibTableColumn
cdslVTPppChapHost=_CdslVTPppChapHost_Object((1,3,6,1,4,1,9,10,30,1,2,2,1,11),_CdslVTPppChapHost_Type())
cdslVTPppChapHost.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVTPppChapHost.setStatus(_A)
class _CdslVTPppChapPassword_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,25))
_CdslVTPppChapPassword_Type.__name__=_I
_CdslVTPppChapPassword_Object=MibTableColumn
cdslVTPppChapPassword=_CdslVTPppChapPassword_Object((1,3,6,1,4,1,9,10,30,1,2,2,1,12),_CdslVTPppChapPassword_Type())
cdslVTPppChapPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVTPppChapPassword.setStatus(_A)
class _CdslVTPppChapEncrypType_Type(TruthValue):defaultValue=2
_CdslVTPppChapEncrypType_Type.__name__=_P
_CdslVTPppChapEncrypType_Object=MibTableColumn
cdslVTPppChapEncrypType=_CdslVTPppChapEncrypType_Object((1,3,6,1,4,1,9,10,30,1,2,2,1,13),_CdslVTPppChapEncrypType_Type())
cdslVTPppChapEncrypType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVTPppChapEncrypType.setStatus(_A)
class _CdslVTPppChapRefuse_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('no',1),('refuse',2),('refuseCallinOnly',3)))
_CdslVTPppChapRefuse_Type.__name__=_D
_CdslVTPppChapRefuse_Object=MibTableColumn
cdslVTPppChapRefuse=_CdslVTPppChapRefuse_Object((1,3,6,1,4,1,9,10,30,1,2,2,1,14),_CdslVTPppChapRefuse_Type())
cdslVTPppChapRefuse.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVTPppChapRefuse.setStatus(_A)
class _CdslVTPppChapWaitPeer_Type(TruthValue):defaultValue=1
_CdslVTPppChapWaitPeer_Type.__name__=_P
_CdslVTPppChapWaitPeer_Object=MibTableColumn
cdslVTPppChapWaitPeer=_CdslVTPppChapWaitPeer_Object((1,3,6,1,4,1,9,10,30,1,2,2,1,15),_CdslVTPppChapWaitPeer_Type())
cdslVTPppChapWaitPeer.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVTPppChapWaitPeer.setStatus(_A)
class _CdslVTPppPapUserName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CdslVTPppPapUserName_Type.__name__=_I
_CdslVTPppPapUserName_Object=MibTableColumn
cdslVTPppPapUserName=_CdslVTPppPapUserName_Object((1,3,6,1,4,1,9,10,30,1,2,2,1,16),_CdslVTPppPapUserName_Type())
cdslVTPppPapUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVTPppPapUserName.setStatus(_A)
class _CdslVTPppPapPassword_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CdslVTPppPapPassword_Type.__name__=_I
_CdslVTPppPapPassword_Object=MibTableColumn
cdslVTPppPapPassword=_CdslVTPppPapPassword_Object((1,3,6,1,4,1,9,10,30,1,2,2,1,17),_CdslVTPppPapPassword_Type())
cdslVTPppPapPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVTPppPapPassword.setStatus(_A)
class _CdslVTPppPapEncrypType_Type(TruthValue):defaultValue=2
_CdslVTPppPapEncrypType_Type.__name__=_P
_CdslVTPppPapEncrypType_Object=MibTableColumn
cdslVTPppPapEncrypType=_CdslVTPppPapEncrypType_Object((1,3,6,1,4,1,9,10,30,1,2,2,1,18),_CdslVTPppPapEncrypType_Type())
cdslVTPppPapEncrypType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVTPppPapEncrypType.setStatus(_A)
class _CdslVTPppUseTacacs_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('no',1),('yes',2),('singleLine',3)))
_CdslVTPppUseTacacs_Type.__name__=_D
_CdslVTPppUseTacacs_Object=MibTableColumn
cdslVTPppUseTacacs=_CdslVTPppUseTacacs_Object((1,3,6,1,4,1,9,10,30,1,2,2,1,19),_CdslVTPppUseTacacs_Type())
cdslVTPppUseTacacs.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVTPppUseTacacs.setStatus(_A)
class _CdslVTRowStatus_Type(RowStatus):defaultValue=1
_CdslVTRowStatus_Type.__name__=_O
_CdslVTRowStatus_Object=MibTableColumn
cdslVTRowStatus=_CdslVTRowStatus_Object((1,3,6,1,4,1,9,10,30,1,2,2,1,20),_CdslVTRowStatus_Type())
cdslVTRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVTRowStatus.setStatus(_A)
_CdslLocalIpAddrPool_ObjectIdentity=ObjectIdentity
cdslLocalIpAddrPool=_CdslLocalIpAddrPool_ObjectIdentity((1,3,6,1,4,1,9,10,30,1,3))
_CdslLocalIpAddrPoolNumberTable_Object=MibTable
cdslLocalIpAddrPoolNumberTable=_CdslLocalIpAddrPoolNumberTable_Object((1,3,6,1,4,1,9,10,30,1,3,1))
if mibBuilder.loadTexts:cdslLocalIpAddrPoolNumberTable.setStatus(_A)
_CdslLocalIpAddrPoolNumberEntry_Object=MibTableRow
cdslLocalIpAddrPoolNumberEntry=_CdslLocalIpAddrPoolNumberEntry_Object((1,3,6,1,4,1,9,10,30,1,3,1,1))
cdslLocalIpAddrPoolNumberEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cdslLocalIpAddrPoolNumberEntry.setStatus(_A)
class _CdslMaxLocalIpAddrPools_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdslMaxLocalIpAddrPools_Type.__name__=_F
_CdslMaxLocalIpAddrPools_Object=MibTableColumn
cdslMaxLocalIpAddrPools=_CdslMaxLocalIpAddrPools_Object((1,3,6,1,4,1,9,10,30,1,3,1,1,1),_CdslMaxLocalIpAddrPools_Type())
cdslMaxLocalIpAddrPools.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslMaxLocalIpAddrPools.setStatus(_A)
class _CdslLocalIpAddrPools_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdslLocalIpAddrPools_Type.__name__=_N
_CdslLocalIpAddrPools_Object=MibTableColumn
cdslLocalIpAddrPools=_CdslLocalIpAddrPools_Object((1,3,6,1,4,1,9,10,30,1,3,1,1,2),_CdslLocalIpAddrPools_Type())
cdslLocalIpAddrPools.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslLocalIpAddrPools.setStatus(_A)
_CdslLocalIpAddrPoolTable_Object=MibTable
cdslLocalIpAddrPoolTable=_CdslLocalIpAddrPoolTable_Object((1,3,6,1,4,1,9,10,30,1,3,2))
if mibBuilder.loadTexts:cdslLocalIpAddrPoolTable.setStatus(_A)
_CdslLocalIpAddrPoolEntry_Object=MibTableRow
cdslLocalIpAddrPoolEntry=_CdslLocalIpAddrPoolEntry_Object((1,3,6,1,4,1,9,10,30,1,3,2,1))
cdslLocalIpAddrPoolEntry.setIndexNames((0,_B,_H),(0,_B,_Q))
if mibBuilder.loadTexts:cdslLocalIpAddrPoolEntry.setStatus(_A)
class _CdslLocalIpAddrPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CdslLocalIpAddrPoolName_Type.__name__=_I
_CdslLocalIpAddrPoolName_Object=MibTableColumn
cdslLocalIpAddrPoolName=_CdslLocalIpAddrPoolName_Object((1,3,6,1,4,1,9,10,30,1,3,2,1,1),_CdslLocalIpAddrPoolName_Type())
cdslLocalIpAddrPoolName.setMaxAccess(_J)
if mibBuilder.loadTexts:cdslLocalIpAddrPoolName.setStatus(_A)
class _CdslLocalIpAddrPoolFreeAddresses_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdslLocalIpAddrPoolFreeAddresses_Type.__name__=_F
_CdslLocalIpAddrPoolFreeAddresses_Object=MibTableColumn
cdslLocalIpAddrPoolFreeAddresses=_CdslLocalIpAddrPoolFreeAddresses_Object((1,3,6,1,4,1,9,10,30,1,3,2,1,2),_CdslLocalIpAddrPoolFreeAddresses_Type())
cdslLocalIpAddrPoolFreeAddresses.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslLocalIpAddrPoolFreeAddresses.setStatus(_A)
class _CdslLocalIpAddrPoolInUseAddresses_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdslLocalIpAddrPoolInUseAddresses_Type.__name__=_F
_CdslLocalIpAddrPoolInUseAddresses_Object=MibTableColumn
cdslLocalIpAddrPoolInUseAddresses=_CdslLocalIpAddrPoolInUseAddresses_Object((1,3,6,1,4,1,9,10,30,1,3,2,1,3),_CdslLocalIpAddrPoolInUseAddresses_Type())
cdslLocalIpAddrPoolInUseAddresses.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslLocalIpAddrPoolInUseAddresses.setStatus(_A)
_CdslLocalIpAddrRangeTable_Object=MibTable
cdslLocalIpAddrRangeTable=_CdslLocalIpAddrRangeTable_Object((1,3,6,1,4,1,9,10,30,1,3,3))
if mibBuilder.loadTexts:cdslLocalIpAddrRangeTable.setStatus(_A)
_CdslLocalIpAddrRangeEntry_Object=MibTableRow
cdslLocalIpAddrRangeEntry=_CdslLocalIpAddrRangeEntry_Object((1,3,6,1,4,1,9,10,30,1,3,3,1))
cdslLocalIpAddrRangeEntry.setIndexNames((0,_B,_H),(0,_B,_X),(0,_B,_Y),(0,_B,_Q))
if mibBuilder.loadTexts:cdslLocalIpAddrRangeEntry.setStatus(_A)
_CdslLocalIpAddrRangeLowAddr_Type=IpAddress
_CdslLocalIpAddrRangeLowAddr_Object=MibTableColumn
cdslLocalIpAddrRangeLowAddr=_CdslLocalIpAddrRangeLowAddr_Object((1,3,6,1,4,1,9,10,30,1,3,3,1,1),_CdslLocalIpAddrRangeLowAddr_Type())
cdslLocalIpAddrRangeLowAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:cdslLocalIpAddrRangeLowAddr.setStatus(_A)
_CdslLocalIpAddrRangeHighAddr_Type=IpAddress
_CdslLocalIpAddrRangeHighAddr_Object=MibTableColumn
cdslLocalIpAddrRangeHighAddr=_CdslLocalIpAddrRangeHighAddr_Object((1,3,6,1,4,1,9,10,30,1,3,3,1,2),_CdslLocalIpAddrRangeHighAddr_Type())
cdslLocalIpAddrRangeHighAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:cdslLocalIpAddrRangeHighAddr.setStatus(_A)
_CdslLocalIpAddrRangeRowStatus_Type=RowStatus
_CdslLocalIpAddrRangeRowStatus_Object=MibTableColumn
cdslLocalIpAddrRangeRowStatus=_CdslLocalIpAddrRangeRowStatus_Object((1,3,6,1,4,1,9,10,30,1,3,3,1,3),_CdslLocalIpAddrRangeRowStatus_Type())
cdslLocalIpAddrRangeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslLocalIpAddrRangeRowStatus.setStatus(_A)
_CdslAtmPvc_ObjectIdentity=ObjectIdentity
cdslAtmPvc=_CdslAtmPvc_ObjectIdentity((1,3,6,1,4,1,9,10,30,1,4))
_CdslPppOverAtmPvcNumberTable_Object=MibTable
cdslPppOverAtmPvcNumberTable=_CdslPppOverAtmPvcNumberTable_Object((1,3,6,1,4,1,9,10,30,1,4,1))
if mibBuilder.loadTexts:cdslPppOverAtmPvcNumberTable.setStatus(_A)
_CdslPppOverAtmPvcNumberEntry_Object=MibTableRow
cdslPppOverAtmPvcNumberEntry=_CdslPppOverAtmPvcNumberEntry_Object((1,3,6,1,4,1,9,10,30,1,4,1,1))
cdslPppOverAtmPvcNumberEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cdslPppOverAtmPvcNumberEntry.setStatus(_A)
class _CdslPppOverAtmPvcs_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdslPppOverAtmPvcs_Type.__name__=_N
_CdslPppOverAtmPvcs_Object=MibTableColumn
cdslPppOverAtmPvcs=_CdslPppOverAtmPvcs_Object((1,3,6,1,4,1,9,10,30,1,4,1,1,1),_CdslPppOverAtmPvcs_Type())
cdslPppOverAtmPvcs.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslPppOverAtmPvcs.setStatus(_A)
_CdslAtmPvcTable_Object=MibTable
cdslAtmPvcTable=_CdslAtmPvcTable_Object((1,3,6,1,4,1,9,10,30,1,4,2))
if mibBuilder.loadTexts:cdslAtmPvcTable.setStatus(_A)
_CdslAtmPvcEntry_Object=MibTableRow
cdslAtmPvcEntry=_CdslAtmPvcEntry_Object((1,3,6,1,4,1,9,10,30,1,4,2,1))
cdslAtmPvcEntry.setIndexNames((0,_B,_H),(0,_R,_T),(0,_B,_Z),(0,_B,_a))
if mibBuilder.loadTexts:cdslAtmPvcEntry.setStatus(_A)
class _CdslAtmPvcVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CdslAtmPvcVpi_Type.__name__=_D
_CdslAtmPvcVpi_Object=MibTableColumn
cdslAtmPvcVpi=_CdslAtmPvcVpi_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,1),_CdslAtmPvcVpi_Type())
cdslAtmPvcVpi.setMaxAccess(_J)
if mibBuilder.loadTexts:cdslAtmPvcVpi.setStatus(_A)
class _CdslAtmPvcVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CdslAtmPvcVci_Type.__name__=_D
_CdslAtmPvcVci_Object=MibTableColumn
cdslAtmPvcVci=_CdslAtmPvcVci_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,2),_CdslAtmPvcVci_Type())
cdslAtmPvcVci.setMaxAccess(_J)
if mibBuilder.loadTexts:cdslAtmPvcVci.setStatus(_A)
class _CdslAtmPvcName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CdslAtmPvcName_Type.__name__=_I
_CdslAtmPvcName_Object=MibTableColumn
cdslAtmPvcName=_CdslAtmPvcName_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,3),_CdslAtmPvcName_Type())
cdslAtmPvcName.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslAtmPvcName.setStatus(_A)
class _CdslAtmPvcSubIfNumber_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CdslAtmPvcSubIfNumber_Type.__name__=_D
_CdslAtmPvcSubIfNumber_Object=MibTableColumn
cdslAtmPvcSubIfNumber=_CdslAtmPvcSubIfNumber_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,4),_CdslAtmPvcSubIfNumber_Type())
cdslAtmPvcSubIfNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslAtmPvcSubIfNumber.setStatus(_A)
class _CdslAtmPvcClass_Type(DisplayString):defaultValue=OctetString('default-vc-class');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CdslAtmPvcClass_Type.__name__=_I
_CdslAtmPvcClass_Object=MibTableColumn
cdslAtmPvcClass=_CdslAtmPvcClass_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,5),_CdslAtmPvcClass_Type())
cdslAtmPvcClass.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslAtmPvcClass.setStatus(_A)
class _CdslAtmPvcQosType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_b,0),('cbr',1),('ubr',2),(_c,3),('vbrRt',4),(_d,5),('abr',6),('max',7)))
_CdslAtmPvcQosType_Type.__name__=_D
_CdslAtmPvcQosType_Object=MibTableColumn
cdslAtmPvcQosType=_CdslAtmPvcQosType_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,6),_CdslAtmPvcQosType_Type())
cdslAtmPvcQosType.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslAtmPvcQosType.setStatus(_A)
class _CdslAtmPvcAbrPCR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdslAtmPvcAbrPCR_Type.__name__=_F
_CdslAtmPvcAbrPCR_Object=MibTableColumn
cdslAtmPvcAbrPCR=_CdslAtmPvcAbrPCR_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,7),_CdslAtmPvcAbrPCR_Type())
cdslAtmPvcAbrPCR.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslAtmPvcAbrPCR.setStatus(_A)
if mibBuilder.loadTexts:cdslAtmPvcAbrPCR.setUnits(_G)
class _CdslAtmPvcAbrMCR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_CdslAtmPvcAbrMCR_Type.__name__=_F
_CdslAtmPvcAbrMCR_Object=MibTableColumn
cdslAtmPvcAbrMCR=_CdslAtmPvcAbrMCR_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,8),_CdslAtmPvcAbrMCR_Type())
cdslAtmPvcAbrMCR.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslAtmPvcAbrMCR.setStatus(_A)
if mibBuilder.loadTexts:cdslAtmPvcAbrMCR.setUnits(_G)
class _CdslAtmPvcAbrIORIF_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdslAtmPvcAbrIORIF_Type.__name__=_F
_CdslAtmPvcAbrIORIF_Object=MibTableColumn
cdslAtmPvcAbrIORIF=_CdslAtmPvcAbrIORIF_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,9),_CdslAtmPvcAbrIORIF_Type())
cdslAtmPvcAbrIORIF.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslAtmPvcAbrIORIF.setStatus(_A)
class _CdslAtmPvcAbrIORDF_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdslAtmPvcAbrIORDF_Type.__name__=_F
_CdslAtmPvcAbrIORDF_Object=MibTableColumn
cdslAtmPvcAbrIORDF=_CdslAtmPvcAbrIORDF_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,10),_CdslAtmPvcAbrIORDF_Type())
cdslAtmPvcAbrIORDF.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslAtmPvcAbrIORDF.setStatus(_A)
class _CdslAtmPvcBroadcast_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),(_L,1),(_M,2)))
_CdslAtmPvcBroadcast_Type.__name__=_D
_CdslAtmPvcBroadcast_Object=MibTableColumn
cdslAtmPvcBroadcast=_CdslAtmPvcBroadcast_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,11),_CdslAtmPvcBroadcast_Type())
cdslAtmPvcBroadcast.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslAtmPvcBroadcast.setStatus(_A)
class _CdslAtmPvcEncapsulation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_e,0),(_f,1),(_g,2),(_h,3),(_i,4),(_j,5),(_k,6),(_l,7)))
_CdslAtmPvcEncapsulation_Type.__name__=_D
_CdslAtmPvcEncapsulation_Object=MibTableColumn
cdslAtmPvcEncapsulation=_CdslAtmPvcEncapsulation_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,12),_CdslAtmPvcEncapsulation_Type())
cdslAtmPvcEncapsulation.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslAtmPvcEncapsulation.setStatus(_A)
class _CdslAtmPvcMuxLinkType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ip',1),('ppp',2)))
_CdslAtmPvcMuxLinkType_Type.__name__=_D
_CdslAtmPvcMuxLinkType_Object=MibTableColumn
cdslAtmPvcMuxLinkType=_CdslAtmPvcMuxLinkType_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,13),_CdslAtmPvcMuxLinkType_Type())
cdslAtmPvcMuxLinkType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslAtmPvcMuxLinkType.setStatus(_A)
class _CdslAtmPvcVirtualTemplate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CdslAtmPvcVirtualTemplate_Type.__name__=_D
_CdslAtmPvcVirtualTemplate_Object=MibTableColumn
cdslAtmPvcVirtualTemplate=_CdslAtmPvcVirtualTemplate_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,14),_CdslAtmPvcVirtualTemplate_Type())
cdslAtmPvcVirtualTemplate.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslAtmPvcVirtualTemplate.setStatus(_A)
class _CdslAtmPvcILMIManage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),(_L,1),(_M,2)))
_CdslAtmPvcILMIManage_Type.__name__=_D
_CdslAtmPvcILMIManage_Object=MibTableColumn
cdslAtmPvcILMIManage=_CdslAtmPvcILMIManage_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,15),_CdslAtmPvcILMIManage_Type())
cdslAtmPvcILMIManage.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslAtmPvcILMIManage.setStatus(_A)
class _CdslAtmPvcInarp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_CdslAtmPvcInarp_Type.__name__=_F
_CdslAtmPvcInarp_Object=MibTableColumn
cdslAtmPvcInarp=_CdslAtmPvcInarp_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,16),_CdslAtmPvcInarp_Type())
cdslAtmPvcInarp.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslAtmPvcInarp.setStatus(_A)
class _CdslAtmPvcOamRetryUpCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_CdslAtmPvcOamRetryUpCount_Type.__name__=_F
_CdslAtmPvcOamRetryUpCount_Object=MibTableColumn
cdslAtmPvcOamRetryUpCount=_CdslAtmPvcOamRetryUpCount_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,17),_CdslAtmPvcOamRetryUpCount_Type())
cdslAtmPvcOamRetryUpCount.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslAtmPvcOamRetryUpCount.setStatus(_A)
class _CdslAtmPvcOamRetryDownCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_CdslAtmPvcOamRetryDownCount_Type.__name__=_F
_CdslAtmPvcOamRetryDownCount_Object=MibTableColumn
cdslAtmPvcOamRetryDownCount=_CdslAtmPvcOamRetryDownCount_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,18),_CdslAtmPvcOamRetryDownCount_Type())
cdslAtmPvcOamRetryDownCount.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslAtmPvcOamRetryDownCount.setStatus(_A)
class _CdslAtmPvcOamPvcManaged_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),(_L,1),(_M,2)))
_CdslAtmPvcOamPvcManaged_Type.__name__=_D
_CdslAtmPvcOamPvcManaged_Object=MibTableColumn
cdslAtmPvcOamPvcManaged=_CdslAtmPvcOamPvcManaged_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,19),_CdslAtmPvcOamPvcManaged_Type())
cdslAtmPvcOamPvcManaged.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslAtmPvcOamPvcManaged.setStatus(_A)
class _CdslAtmPvcOamPvcLF_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_CdslAtmPvcOamPvcLF_Type.__name__=_F
_CdslAtmPvcOamPvcLF_Object=MibTableColumn
cdslAtmPvcOamPvcLF=_CdslAtmPvcOamPvcLF_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,20),_CdslAtmPvcOamPvcLF_Type())
cdslAtmPvcOamPvcLF.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslAtmPvcOamPvcLF.setStatus(_A)
_CdslAtmPvcProtocolIpBC_Type=TruthValue
_CdslAtmPvcProtocolIpBC_Object=MibTableColumn
cdslAtmPvcProtocolIpBC=_CdslAtmPvcProtocolIpBC_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,21),_CdslAtmPvcProtocolIpBC_Type())
cdslAtmPvcProtocolIpBC.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslAtmPvcProtocolIpBC.setStatus(_A)
_CdslAtmPvcProtocolIpxBC_Type=TruthValue
_CdslAtmPvcProtocolIpxBC_Object=MibTableColumn
cdslAtmPvcProtocolIpxBC=_CdslAtmPvcProtocolIpxBC_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,22),_CdslAtmPvcProtocolIpxBC_Type())
cdslAtmPvcProtocolIpxBC.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslAtmPvcProtocolIpxBC.setStatus(_A)
class _CdslAtmPvcUbrPCR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,155000))
_CdslAtmPvcUbrPCR_Type.__name__=_F
_CdslAtmPvcUbrPCR_Object=MibTableColumn
cdslAtmPvcUbrPCR=_CdslAtmPvcUbrPCR_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,23),_CdslAtmPvcUbrPCR_Type())
cdslAtmPvcUbrPCR.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslAtmPvcUbrPCR.setStatus(_A)
if mibBuilder.loadTexts:cdslAtmPvcUbrPCR.setUnits(_G)
class _CdslAtmPvcUbrPlusPCR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,155000))
_CdslAtmPvcUbrPlusPCR_Type.__name__=_F
_CdslAtmPvcUbrPlusPCR_Object=MibTableColumn
cdslAtmPvcUbrPlusPCR=_CdslAtmPvcUbrPlusPCR_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,24),_CdslAtmPvcUbrPlusPCR_Type())
cdslAtmPvcUbrPlusPCR.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslAtmPvcUbrPlusPCR.setStatus(_A)
if mibBuilder.loadTexts:cdslAtmPvcUbrPlusPCR.setUnits(_G)
class _CdslAtmPvcUbrPlusMCR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_CdslAtmPvcUbrPlusMCR_Type.__name__=_F
_CdslAtmPvcUbrPlusMCR_Object=MibTableColumn
cdslAtmPvcUbrPlusMCR=_CdslAtmPvcUbrPlusMCR_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,25),_CdslAtmPvcUbrPlusMCR_Type())
cdslAtmPvcUbrPlusMCR.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslAtmPvcUbrPlusMCR.setStatus(_A)
if mibBuilder.loadTexts:cdslAtmPvcUbrPlusMCR.setUnits(_G)
class _CdslAtmPvcVbrNrtPCR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,155000))
_CdslAtmPvcVbrNrtPCR_Type.__name__=_F
_CdslAtmPvcVbrNrtPCR_Object=MibTableColumn
cdslAtmPvcVbrNrtPCR=_CdslAtmPvcVbrNrtPCR_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,26),_CdslAtmPvcVbrNrtPCR_Type())
cdslAtmPvcVbrNrtPCR.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslAtmPvcVbrNrtPCR.setStatus(_A)
if mibBuilder.loadTexts:cdslAtmPvcVbrNrtPCR.setUnits(_G)
class _CdslAtmPvcVbrNrtSCR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_CdslAtmPvcVbrNrtSCR_Type.__name__=_F
_CdslAtmPvcVbrNrtSCR_Object=MibTableColumn
cdslAtmPvcVbrNrtSCR=_CdslAtmPvcVbrNrtSCR_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,27),_CdslAtmPvcVbrNrtSCR_Type())
cdslAtmPvcVbrNrtSCR.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslAtmPvcVbrNrtSCR.setStatus(_A)
if mibBuilder.loadTexts:cdslAtmPvcVbrNrtSCR.setUnits(_G)
class _CdslAtmPvcRowStatus_Type(RowStatus):defaultValue=1
_CdslAtmPvcRowStatus_Type.__name__=_O
_CdslAtmPvcRowStatus_Object=MibTableColumn
cdslAtmPvcRowStatus=_CdslAtmPvcRowStatus_Object((1,3,6,1,4,1,9,10,30,1,4,2,1,28),_CdslAtmPvcRowStatus_Type())
cdslAtmPvcRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslAtmPvcRowStatus.setStatus(_A)
_CdslVcClass_ObjectIdentity=ObjectIdentity
cdslVcClass=_CdslVcClass_ObjectIdentity((1,3,6,1,4,1,9,10,30,1,5))
_CdslVcClassNumberTable_Object=MibTable
cdslVcClassNumberTable=_CdslVcClassNumberTable_Object((1,3,6,1,4,1,9,10,30,1,5,1))
if mibBuilder.loadTexts:cdslVcClassNumberTable.setStatus(_A)
_CdslVcClassNumberEntry_Object=MibTableRow
cdslVcClassNumberEntry=_CdslVcClassNumberEntry_Object((1,3,6,1,4,1,9,10,30,1,5,1,1))
cdslVcClassNumberEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cdslVcClassNumberEntry.setStatus(_A)
class _CdslMaxVcClasses_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdslMaxVcClasses_Type.__name__=_F
_CdslMaxVcClasses_Object=MibTableColumn
cdslMaxVcClasses=_CdslMaxVcClasses_Object((1,3,6,1,4,1,9,10,30,1,5,1,1,1),_CdslMaxVcClasses_Type())
cdslMaxVcClasses.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslMaxVcClasses.setStatus(_A)
class _CdslVcClasses_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CdslVcClasses_Type.__name__=_N
_CdslVcClasses_Object=MibTableColumn
cdslVcClasses=_CdslVcClasses_Object((1,3,6,1,4,1,9,10,30,1,5,1,1,2),_CdslVcClasses_Type())
cdslVcClasses.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslVcClasses.setStatus(_A)
_CdslVcClassTable_Object=MibTable
cdslVcClassTable=_CdslVcClassTable_Object((1,3,6,1,4,1,9,10,30,1,5,2))
if mibBuilder.loadTexts:cdslVcClassTable.setStatus(_A)
_CdslVcClassEntry_Object=MibTableRow
cdslVcClassEntry=_CdslVcClassEntry_Object((1,3,6,1,4,1,9,10,30,1,5,2,1))
cdslVcClassEntry.setIndexNames((0,_B,_H),(0,_B,_m))
if mibBuilder.loadTexts:cdslVcClassEntry.setStatus(_A)
class _CdslVcClassName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CdslVcClassName_Type.__name__=_I
_CdslVcClassName_Object=MibTableColumn
cdslVcClassName=_CdslVcClassName_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,1),_CdslVcClassName_Type())
cdslVcClassName.setMaxAccess(_J)
if mibBuilder.loadTexts:cdslVcClassName.setStatus(_A)
class _CdslVcClassType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('atm',1),('funi',2)))
_CdslVcClassType_Type.__name__=_D
_CdslVcClassType_Object=MibTableColumn
cdslVcClassType=_CdslVcClassType_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,2),_CdslVcClassType_Type())
cdslVcClassType.setMaxAccess(_E)
if mibBuilder.loadTexts:cdslVcClassType.setStatus(_A)
class _CdslVcClassQosType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_b,0),('cbr',1),('ubr',2),(_c,3),('vbrRt',4),(_d,5),('abr',6),('max',7)))
_CdslVcClassQosType_Type.__name__=_D
_CdslVcClassQosType_Object=MibTableColumn
cdslVcClassQosType=_CdslVcClassQosType_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,3),_CdslVcClassQosType_Type())
cdslVcClassQosType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassQosType.setStatus(_A)
class _CdslVcClassAbrPCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(56,155000))
_CdslVcClassAbrPCR_Type.__name__=_D
_CdslVcClassAbrPCR_Object=MibTableColumn
cdslVcClassAbrPCR=_CdslVcClassAbrPCR_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,4),_CdslVcClassAbrPCR_Type())
cdslVcClassAbrPCR.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassAbrPCR.setStatus(_A)
if mibBuilder.loadTexts:cdslVcClassAbrPCR.setUnits(_G)
class _CdslVcClassAbrMcr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,155000))
_CdslVcClassAbrMcr_Type.__name__=_D
_CdslVcClassAbrMcr_Object=MibTableColumn
cdslVcClassAbrMcr=_CdslVcClassAbrMcr_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,5),_CdslVcClassAbrMcr_Type())
cdslVcClassAbrMcr.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassAbrMcr.setStatus(_A)
if mibBuilder.loadTexts:cdslVcClassAbrMcr.setUnits(_G)
class _CdslVcClassAbrIORIF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CdslVcClassAbrIORIF_Type.__name__=_D
_CdslVcClassAbrIORIF_Object=MibTableColumn
cdslVcClassAbrIORIF=_CdslVcClassAbrIORIF_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,6),_CdslVcClassAbrIORIF_Type())
cdslVcClassAbrIORIF.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassAbrIORIF.setStatus(_A)
class _CdslVcClassAbrIORDF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CdslVcClassAbrIORDF_Type.__name__=_D
_CdslVcClassAbrIORDF_Object=MibTableColumn
cdslVcClassAbrIORDF=_CdslVcClassAbrIORDF_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,7),_CdslVcClassAbrIORDF_Type())
cdslVcClassAbrIORDF.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassAbrIORDF.setStatus(_A)
class _CdslVcClassBroadcast_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),(_L,1),(_M,2)))
_CdslVcClassBroadcast_Type.__name__=_D
_CdslVcClassBroadcast_Object=MibTableColumn
cdslVcClassBroadcast=_CdslVcClassBroadcast_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,8),_CdslVcClassBroadcast_Type())
cdslVcClassBroadcast.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassBroadcast.setStatus(_A)
class _CdslVcClassEncapsulation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_e,0),(_f,1),(_g,2),(_h,3),(_i,4),(_j,5),(_k,6),(_l,7)))
_CdslVcClassEncapsulation_Type.__name__=_D
_CdslVcClassEncapsulation_Object=MibTableColumn
cdslVcClassEncapsulation=_CdslVcClassEncapsulation_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,9),_CdslVcClassEncapsulation_Type())
cdslVcClassEncapsulation.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassEncapsulation.setStatus(_A)
class _CdslVcClassMuxLinkType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ip',1),('ppp',2)))
_CdslVcClassMuxLinkType_Type.__name__=_D
_CdslVcClassMuxLinkType_Object=MibTableColumn
cdslVcClassMuxLinkType=_CdslVcClassMuxLinkType_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,10),_CdslVcClassMuxLinkType_Type())
cdslVcClassMuxLinkType.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassMuxLinkType.setStatus(_A)
class _CdslVcClassVirtualTemplate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CdslVcClassVirtualTemplate_Type.__name__=_D
_CdslVcClassVirtualTemplate_Object=MibTableColumn
cdslVcClassVirtualTemplate=_CdslVcClassVirtualTemplate_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,11),_CdslVcClassVirtualTemplate_Type())
cdslVcClassVirtualTemplate.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassVirtualTemplate.setStatus(_A)
class _CdslVcClassIdleTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000000))
_CdslVcClassIdleTimeout_Type.__name__=_D
_CdslVcClassIdleTimeout_Object=MibTableColumn
cdslVcClassIdleTimeout=_CdslVcClassIdleTimeout_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,12),_CdslVcClassIdleTimeout_Type())
cdslVcClassIdleTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassIdleTimeout.setStatus(_A)
class _CdslVcClassIdleMTR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,155000))
_CdslVcClassIdleMTR_Type.__name__=_D
_CdslVcClassIdleMTR_Object=MibTableColumn
cdslVcClassIdleMTR=_CdslVcClassIdleMTR_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,13),_CdslVcClassIdleMTR_Type())
cdslVcClassIdleMTR.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassIdleMTR.setStatus(_A)
if mibBuilder.loadTexts:cdslVcClassIdleMTR.setUnits(_G)
class _CdslVcClassILMIManage_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),(_L,1),(_M,2)))
_CdslVcClassILMIManage_Type.__name__=_D
_CdslVcClassILMIManage_Object=MibTableColumn
cdslVcClassILMIManage=_CdslVcClassILMIManage_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,14),_CdslVcClassILMIManage_Type())
cdslVcClassILMIManage.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassILMIManage.setStatus(_A)
class _CdslVcClassInarp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_CdslVcClassInarp_Type.__name__=_D
_CdslVcClassInarp_Object=MibTableColumn
cdslVcClassInarp=_CdslVcClassInarp_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,15),_CdslVcClassInarp_Type())
cdslVcClassInarp.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassInarp.setStatus(_A)
class _CdslVcClassOamRetryUpCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_CdslVcClassOamRetryUpCount_Type.__name__=_D
_CdslVcClassOamRetryUpCount_Object=MibTableColumn
cdslVcClassOamRetryUpCount=_CdslVcClassOamRetryUpCount_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,16),_CdslVcClassOamRetryUpCount_Type())
cdslVcClassOamRetryUpCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassOamRetryUpCount.setStatus(_A)
class _CdslVcClassOamRetryDownCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_CdslVcClassOamRetryDownCount_Type.__name__=_D
_CdslVcClassOamRetryDownCount_Object=MibTableColumn
cdslVcClassOamRetryDownCount=_CdslVcClassOamRetryDownCount_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,17),_CdslVcClassOamRetryDownCount_Type())
cdslVcClassOamRetryDownCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassOamRetryDownCount.setStatus(_A)
class _CdslVcClassOamPvcManaged_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),(_L,1),(_M,2)))
_CdslVcClassOamPvcManaged_Type.__name__=_D
_CdslVcClassOamPvcManaged_Object=MibTableColumn
cdslVcClassOamPvcManaged=_CdslVcClassOamPvcManaged_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,18),_CdslVcClassOamPvcManaged_Type())
cdslVcClassOamPvcManaged.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassOamPvcManaged.setStatus(_A)
class _CdslVcClassOamPvcLF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_CdslVcClassOamPvcLF_Type.__name__=_D
_CdslVcClassOamPvcLF_Object=MibTableColumn
cdslVcClassOamPvcLF=_CdslVcClassOamPvcLF_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,19),_CdslVcClassOamPvcLF_Type())
cdslVcClassOamPvcLF.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassOamPvcLF.setStatus(_A)
if mibBuilder.loadTexts:cdslVcClassOamPvcLF.setUnits(_n)
class _CdslVcClassOamSvcManaged_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),(_L,1),(_M,2)))
_CdslVcClassOamSvcManaged_Type.__name__=_D
_CdslVcClassOamSvcManaged_Object=MibTableColumn
cdslVcClassOamSvcManaged=_CdslVcClassOamSvcManaged_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,20),_CdslVcClassOamSvcManaged_Type())
cdslVcClassOamSvcManaged.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassOamSvcManaged.setStatus(_A)
class _CdslVcClassOamSvcLF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_CdslVcClassOamSvcLF_Type.__name__=_D
_CdslVcClassOamSvcLF_Object=MibTableColumn
cdslVcClassOamSvcLF=_CdslVcClassOamSvcLF_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,21),_CdslVcClassOamSvcLF_Type())
cdslVcClassOamSvcLF.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassOamSvcLF.setStatus(_A)
if mibBuilder.loadTexts:cdslVcClassOamSvcLF.setUnits(_n)
_CdslVcClassProtocolIpBC_Type=TruthValue
_CdslVcClassProtocolIpBC_Object=MibTableColumn
cdslVcClassProtocolIpBC=_CdslVcClassProtocolIpBC_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,22),_CdslVcClassProtocolIpBC_Type())
cdslVcClassProtocolIpBC.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassProtocolIpBC.setStatus(_A)
_CdslVcClassProtocolIpxBC_Type=TruthValue
_CdslVcClassProtocolIpxBC_Object=MibTableColumn
cdslVcClassProtocolIpxBC=_CdslVcClassProtocolIpxBC_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,23),_CdslVcClassProtocolIpxBC_Type())
cdslVcClassProtocolIpxBC.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassProtocolIpxBC.setStatus(_A)
class _CdslVcClassTransmitPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CdslVcClassTransmitPriority_Type.__name__=_D
_CdslVcClassTransmitPriority_Object=MibTableColumn
cdslVcClassTransmitPriority=_CdslVcClassTransmitPriority_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,24),_CdslVcClassTransmitPriority_Type())
cdslVcClassTransmitPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassTransmitPriority.setStatus(_A)
class _CdslVcClassUbrPCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,155000))
_CdslVcClassUbrPCR_Type.__name__=_D
_CdslVcClassUbrPCR_Object=MibTableColumn
cdslVcClassUbrPCR=_CdslVcClassUbrPCR_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,25),_CdslVcClassUbrPCR_Type())
cdslVcClassUbrPCR.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassUbrPCR.setStatus(_A)
if mibBuilder.loadTexts:cdslVcClassUbrPCR.setUnits(_G)
class _CdslVcClassUbrInputPCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,155000))
_CdslVcClassUbrInputPCR_Type.__name__=_D
_CdslVcClassUbrInputPCR_Object=MibTableColumn
cdslVcClassUbrInputPCR=_CdslVcClassUbrInputPCR_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,26),_CdslVcClassUbrInputPCR_Type())
cdslVcClassUbrInputPCR.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassUbrInputPCR.setStatus(_A)
if mibBuilder.loadTexts:cdslVcClassUbrInputPCR.setUnits(_G)
class _CdslVcClassUbrPlusPCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,155000))
_CdslVcClassUbrPlusPCR_Type.__name__=_D
_CdslVcClassUbrPlusPCR_Object=MibTableColumn
cdslVcClassUbrPlusPCR=_CdslVcClassUbrPlusPCR_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,27),_CdslVcClassUbrPlusPCR_Type())
cdslVcClassUbrPlusPCR.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassUbrPlusPCR.setStatus(_A)
if mibBuilder.loadTexts:cdslVcClassUbrPlusPCR.setUnits(_G)
class _CdslVcClassUbrPlusMCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,155000))
_CdslVcClassUbrPlusMCR_Type.__name__=_D
_CdslVcClassUbrPlusMCR_Object=MibTableColumn
cdslVcClassUbrPlusMCR=_CdslVcClassUbrPlusMCR_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,28),_CdslVcClassUbrPlusMCR_Type())
cdslVcClassUbrPlusMCR.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassUbrPlusMCR.setStatus(_A)
if mibBuilder.loadTexts:cdslVcClassUbrPlusMCR.setUnits(_G)
class _CdslVcClassUbrPlusInputPCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,155000))
_CdslVcClassUbrPlusInputPCR_Type.__name__=_D
_CdslVcClassUbrPlusInputPCR_Object=MibTableColumn
cdslVcClassUbrPlusInputPCR=_CdslVcClassUbrPlusInputPCR_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,29),_CdslVcClassUbrPlusInputPCR_Type())
cdslVcClassUbrPlusInputPCR.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassUbrPlusInputPCR.setStatus(_A)
if mibBuilder.loadTexts:cdslVcClassUbrPlusInputPCR.setUnits(_G)
class _CdslVcClassUbrPlusInputMCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,155000))
_CdslVcClassUbrPlusInputMCR_Type.__name__=_D
_CdslVcClassUbrPlusInputMCR_Object=MibTableColumn
cdslVcClassUbrPlusInputMCR=_CdslVcClassUbrPlusInputMCR_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,30),_CdslVcClassUbrPlusInputMCR_Type())
cdslVcClassUbrPlusInputMCR.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassUbrPlusInputMCR.setStatus(_A)
if mibBuilder.loadTexts:cdslVcClassUbrPlusInputMCR.setUnits(_G)
class _CdslVcClassVbrNrtPCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,155000))
_CdslVcClassVbrNrtPCR_Type.__name__=_D
_CdslVcClassVbrNrtPCR_Object=MibTableColumn
cdslVcClassVbrNrtPCR=_CdslVcClassVbrNrtPCR_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,31),_CdslVcClassVbrNrtPCR_Type())
cdslVcClassVbrNrtPCR.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassVbrNrtPCR.setStatus(_A)
if mibBuilder.loadTexts:cdslVcClassVbrNrtPCR.setUnits(_G)
class _CdslVcClassVbrNrtSCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_CdslVcClassVbrNrtSCR_Type.__name__=_D
_CdslVcClassVbrNrtSCR_Object=MibTableColumn
cdslVcClassVbrNrtSCR=_CdslVcClassVbrNrtSCR_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,32),_CdslVcClassVbrNrtSCR_Type())
cdslVcClassVbrNrtSCR.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassVbrNrtSCR.setStatus(_A)
if mibBuilder.loadTexts:cdslVcClassVbrNrtSCR.setUnits(_G)
class _CdslVcClassVbrNrtInputBP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_CdslVcClassVbrNrtInputBP_Type.__name__=_D
_CdslVcClassVbrNrtInputBP_Object=MibTableColumn
cdslVcClassVbrNrtInputBP=_CdslVcClassVbrNrtInputBP_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,33),_CdslVcClassVbrNrtInputBP_Type())
cdslVcClassVbrNrtInputBP.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassVbrNrtInputBP.setStatus(_A)
class _CdslVcClassVbrNrtInputPCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,155000))
_CdslVcClassVbrNrtInputPCR_Type.__name__=_D
_CdslVcClassVbrNrtInputPCR_Object=MibTableColumn
cdslVcClassVbrNrtInputPCR=_CdslVcClassVbrNrtInputPCR_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,34),_CdslVcClassVbrNrtInputPCR_Type())
cdslVcClassVbrNrtInputPCR.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassVbrNrtInputPCR.setStatus(_A)
if mibBuilder.loadTexts:cdslVcClassVbrNrtInputPCR.setUnits(_G)
class _CdslVcClassVbrNrtInputSCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_CdslVcClassVbrNrtInputSCR_Type.__name__=_D
_CdslVcClassVbrNrtInputSCR_Object=MibTableColumn
cdslVcClassVbrNrtInputSCR=_CdslVcClassVbrNrtInputSCR_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,35),_CdslVcClassVbrNrtInputSCR_Type())
cdslVcClassVbrNrtInputSCR.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassVbrNrtInputSCR.setStatus(_A)
if mibBuilder.loadTexts:cdslVcClassVbrNrtInputSCR.setUnits(_G)
class _CdslVcClassVbrNrtInputMBS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_CdslVcClassVbrNrtInputMBS_Type.__name__=_D
_CdslVcClassVbrNrtInputMBS_Object=MibTableColumn
cdslVcClassVbrNrtInputMBS=_CdslVcClassVbrNrtInputMBS_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,36),_CdslVcClassVbrNrtInputMBS_Type())
cdslVcClassVbrNrtInputMBS.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassVbrNrtInputMBS.setStatus(_A)
if mibBuilder.loadTexts:cdslVcClassVbrNrtInputMBS.setUnits('cells')
class _CdslVcClassRowStatus_Type(RowStatus):defaultValue=1
_CdslVcClassRowStatus_Type.__name__=_O
_CdslVcClassRowStatus_Object=MibTableColumn
cdslVcClassRowStatus=_CdslVcClassRowStatus_Object((1,3,6,1,4,1,9,10,30,1,5,2,1,37),_CdslVcClassRowStatus_Type())
cdslVcClassRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cdslVcClassRowStatus.setStatus(_A)
_CiscoDslProvMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoDslProvMIBNotificationPrefix=_CiscoDslProvMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,30,2))
_CiscoDslProvMIBConformance_ObjectIdentity=ObjectIdentity
ciscoDslProvMIBConformance=_CiscoDslProvMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,30,3))
_CiscoDslProvMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoDslProvMIBCompliances=_CiscoDslProvMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,30,3,1))
_CiscoDslProvMIBGroups_ObjectIdentity=ObjectIdentity
ciscoDslProvMIBGroups=_CiscoDslProvMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,30,3,2))
ciscoNrpSlotGroup=ObjectGroup((1,3,6,1,4,1,9,10,30,3,2,1))
ciscoNrpSlotGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:ciscoNrpSlotGroup.setStatus(_A)
ciscoVirtualTemplateGroup=ObjectGroup((1,3,6,1,4,1,9,10,30,3,2,2))
ciscoVirtualTemplateGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:ciscoVirtualTemplateGroup.setStatus(_A)
ciscoIpPoolGroup=ObjectGroup((1,3,6,1,4,1,9,10,30,3,2,3))
ciscoIpPoolGroup.setObjects(*((_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:ciscoIpPoolGroup.setStatus(_A)
ciscoDslPVCGroup=ObjectGroup((1,3,6,1,4,1,9,10,30,3,2,4))
ciscoDslPVCGroup.setObjects(*((_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah)))
if mibBuilder.loadTexts:ciscoDslPVCGroup.setStatus(_A)
ciscoVcClassGroup=ObjectGroup((1,3,6,1,4,1,9,10,30,3,2,5))
ciscoVcClassGroup.setObjects(*((_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2),(_B,_B3),(_B,_B4),(_B,_B5),(_B,_B6),(_B,_B7),(_B,_B8),(_B,_B9),(_B,_BA),(_B,_BB),(_B,_BC),(_B,_BD),(_B,_BE),(_B,_BF),(_B,_BG),(_B,_BH),(_B,_BI)))
if mibBuilder.loadTexts:ciscoVcClassGroup.setStatus(_A)
ciscoDslProvMIBBasicCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,30,3,1,1))
ciscoDslProvMIBBasicCompliance.setObjects(*((_B,_BJ),(_B,_BK),(_B,_BL),(_B,_BM),(_B,_BN)))
if mibBuilder.loadTexts:ciscoDslProvMIBBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoDslProvisionMIB':ciscoDslProvisionMIB,'ciscoDslProvMIBObjects':ciscoDslProvMIBObjects,'cdslNrpSlot':cdslNrpSlot,_o:cdslMaxNrps,_p:cdslNrpNumber,'cdslNrpIpAddressTable':cdslNrpIpAddressTable,'cdslNrpIpAddressEntry':cdslNrpIpAddressEntry,_H:cdslNrpSlotIndex,_q:cdslNrpIpAddress,'cdslVirtualTemplate':cdslVirtualTemplate,'cdslVirtualTemplateNumberTable':cdslVirtualTemplateNumberTable,'cdslVirtualTemplateNumberEntry':cdslVirtualTemplateNumberEntry,_r:cdslMaxVirtualTemplates,_s:cdslVirtualTemplates,'cdslVirtualTemplateTable':cdslVirtualTemplateTable,'cdslVirtualTemplateEntry':cdslVirtualTemplateEntry,_V:cdslVTIndex,_t:cdslVTIpAddressMethod,_u:cdslVTIpAddress,_v:cdslVTIpAddressMask,_w:cdslVTIpIfIndex,_x:cdslVTPeerIpAddressMethod,_y:cdslVTPeerIpAddrPool,_A0:cdslVTPppAuthChap,_A1:cdslVTPppAuthMSChap,_z:cdslVTPppAuthPap,_A2:cdslVTPppChapHost,_A3:cdslVTPppChapPassword,_A4:cdslVTPppChapEncrypType,_A5:cdslVTPppChapRefuse,_A6:cdslVTPppChapWaitPeer,_A7:cdslVTPppPapUserName,_A8:cdslVTPppPapPassword,_A9:cdslVTPppPapEncrypType,_AA:cdslVTPppUseTacacs,_AB:cdslVTRowStatus,'cdslLocalIpAddrPool':cdslLocalIpAddrPool,'cdslLocalIpAddrPoolNumberTable':cdslLocalIpAddrPoolNumberTable,'cdslLocalIpAddrPoolNumberEntry':cdslLocalIpAddrPoolNumberEntry,_AD:cdslMaxLocalIpAddrPools,_AC:cdslLocalIpAddrPools,'cdslLocalIpAddrPoolTable':cdslLocalIpAddrPoolTable,'cdslLocalIpAddrPoolEntry':cdslLocalIpAddrPoolEntry,_Q:cdslLocalIpAddrPoolName,_AE:cdslLocalIpAddrPoolFreeAddresses,_AF:cdslLocalIpAddrPoolInUseAddresses,'cdslLocalIpAddrRangeTable':cdslLocalIpAddrRangeTable,'cdslLocalIpAddrRangeEntry':cdslLocalIpAddrRangeEntry,_X:cdslLocalIpAddrRangeLowAddr,_Y:cdslLocalIpAddrRangeHighAddr,_AG:cdslLocalIpAddrRangeRowStatus,'cdslAtmPvc':cdslAtmPvc,'cdslPppOverAtmPvcNumberTable':cdslPppOverAtmPvcNumberTable,'cdslPppOverAtmPvcNumberEntry':cdslPppOverAtmPvcNumberEntry,_AH:cdslPppOverAtmPvcs,'cdslAtmPvcTable':cdslAtmPvcTable,'cdslAtmPvcEntry':cdslAtmPvcEntry,_Z:cdslAtmPvcVpi,_a:cdslAtmPvcVci,_AI:cdslAtmPvcName,_AJ:cdslAtmPvcSubIfNumber,_AK:cdslAtmPvcClass,_Ag:cdslAtmPvcQosType,_AL:cdslAtmPvcAbrPCR,_Ah:cdslAtmPvcAbrMCR,_AM:cdslAtmPvcAbrIORIF,_AN:cdslAtmPvcAbrIORDF,_AO:cdslAtmPvcBroadcast,_AP:cdslAtmPvcEncapsulation,_AQ:cdslAtmPvcMuxLinkType,_Ae:cdslAtmPvcVirtualTemplate,_AR:cdslAtmPvcILMIManage,_AS:cdslAtmPvcInarp,_AT:cdslAtmPvcOamRetryUpCount,_AU:cdslAtmPvcOamRetryDownCount,_AV:cdslAtmPvcOamPvcManaged,_AW:cdslAtmPvcOamPvcLF,_AX:cdslAtmPvcProtocolIpBC,_AY:cdslAtmPvcProtocolIpxBC,_AZ:cdslAtmPvcUbrPCR,_Aa:cdslAtmPvcUbrPlusPCR,_Ab:cdslAtmPvcUbrPlusMCR,_Ac:cdslAtmPvcVbrNrtPCR,_Ad:cdslAtmPvcVbrNrtSCR,_Af:cdslAtmPvcRowStatus,'cdslVcClass':cdslVcClass,'cdslVcClassNumberTable':cdslVcClassNumberTable,'cdslVcClassNumberEntry':cdslVcClassNumberEntry,_Aj:cdslMaxVcClasses,_Ai:cdslVcClasses,'cdslVcClassTable':cdslVcClassTable,'cdslVcClassEntry':cdslVcClassEntry,_m:cdslVcClassName,_Ak:cdslVcClassType,_Al:cdslVcClassQosType,_Am:cdslVcClassAbrPCR,_An:cdslVcClassAbrMcr,_Ao:cdslVcClassAbrIORIF,_Ap:cdslVcClassAbrIORDF,_Aq:cdslVcClassBroadcast,_Ar:cdslVcClassEncapsulation,_As:cdslVcClassMuxLinkType,_BH:cdslVcClassVirtualTemplate,_At:cdslVcClassIdleTimeout,_Au:cdslVcClassIdleMTR,_Av:cdslVcClassILMIManage,_Aw:cdslVcClassInarp,_Ax:cdslVcClassOamRetryUpCount,_Ay:cdslVcClassOamRetryDownCount,_Az:cdslVcClassOamPvcManaged,_A_:cdslVcClassOamPvcLF,_B0:cdslVcClassOamSvcManaged,_B1:cdslVcClassOamSvcLF,_B2:cdslVcClassProtocolIpBC,_B3:cdslVcClassProtocolIpxBC,_B4:cdslVcClassTransmitPriority,_B5:cdslVcClassUbrPCR,_B6:cdslVcClassUbrInputPCR,_B7:cdslVcClassUbrPlusPCR,_B8:cdslVcClassUbrPlusMCR,_B9:cdslVcClassUbrPlusInputPCR,_BA:cdslVcClassUbrPlusInputMCR,_BB:cdslVcClassVbrNrtPCR,_BC:cdslVcClassVbrNrtSCR,_BD:cdslVcClassVbrNrtInputBP,_BE:cdslVcClassVbrNrtInputPCR,_BF:cdslVcClassVbrNrtInputSCR,_BG:cdslVcClassVbrNrtInputMBS,_BI:cdslVcClassRowStatus,'ciscoDslProvMIBNotificationPrefix':ciscoDslProvMIBNotificationPrefix,'ciscoDslProvMIBConformance':ciscoDslProvMIBConformance,'ciscoDslProvMIBCompliances':ciscoDslProvMIBCompliances,'ciscoDslProvMIBBasicCompliance':ciscoDslProvMIBBasicCompliance,'ciscoDslProvMIBGroups':ciscoDslProvMIBGroups,_BJ:ciscoNrpSlotGroup,_BK:ciscoVirtualTemplateGroup,_BL:ciscoIpPoolGroup,_BM:ciscoDslPVCGroup,_BN:ciscoVcClassGroup})