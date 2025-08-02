_AB='physicalLinkInterfaceName'
_AA='physicalLinkInfoInterfaceName'
_A9='bearerChannelInfoIndex'
_A8='r2ToneVariantsInterfaceName'
_A7='r2LinkTimerVariantsInterfaceName'
_A6='r2DigitTimerVariantsInterfaceName'
_A5='r2TimerVariantsInterfaceName'
_A4='r2SignalingVariantsInterfaceName'
_A3='OctetString'
_A2='resetSpecific'
_A1='noOp'
_A0='c15'
_z='c14'
_y='c13'
_x='c12'
_w='c11'
_v='c10'
_u='c9'
_t='c8'
_s='c7'
_r='c6'
_q='c5'
_p='c4'
_o='c3'
_n='c2'
_m='c1'
_l='Unsigned32'
_k='b15'
_j='b14'
_i='b13'
_h='b12'
_g='b11'
_f='b10'
_e='b9'
_d='b8'
_c='b7'
_b='b6'
_a='b5'
_Z='b4'
_Y='b3'
_X='b2'
_W='b1'
_V='MX-R2-MIB'
_U='MxEnableState'
_T='a15'
_S='a14'
_R='a13'
_Q='a12'
_P='a11'
_O='a10'
_N='a9'
_M='a8'
_L='a7'
_K='a6'
_J='a5'
_I='a4'
_H='a3'
_G='a2'
_F='a1'
_E='read-only'
_D='none'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_A3,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_U,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_l,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
r2MIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1875))
_R2MIBObjects_ObjectIdentity=ObjectIdentity
r2MIBObjects=_R2MIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1875,1))
_R2Group_ObjectIdentity=ObjectIdentity
r2Group=_R2Group_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100))
_R2Table_Object=MibTable
r2Table=_R2Table_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,100))
if mibBuilder.loadTexts:r2Table.setStatus(_A)
_R2Entry_Object=MibTableRow
r2Entry=_R2Entry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,100,1))
r2Entry.setIndexNames((0,_V,'r2Name'))
if mibBuilder.loadTexts:r2Entry.setStatus(_A)
_R2Name_Type=OctetString
_R2Name_Object=MibTableColumn
r2Name=_R2Name_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,100,1,100),_R2Name_Type())
r2Name.setMaxAccess(_E)
if mibBuilder.loadTexts:r2Name.setStatus(_A)
class _R2ChannelRange_Type(OctetString):defaultValue=OctetString('1-30');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_R2ChannelRange_Type.__name__=_A3
_R2ChannelRange_Object=MibTableColumn
r2ChannelRange=_R2ChannelRange_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,100,1,200),_R2ChannelRange_Type())
r2ChannelRange.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ChannelRange.setStatus(_A)
class _R2ChannelAllocationStrategy_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('ascending',100),('descending',200),('roundRobinAscending',300),('roundRobinDescending',400)))
_R2ChannelAllocationStrategy_Type.__name__=_C
_R2ChannelAllocationStrategy_Object=MibTableColumn
r2ChannelAllocationStrategy=_R2ChannelAllocationStrategy_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,100,1,300),_R2ChannelAllocationStrategy_Type())
r2ChannelAllocationStrategy.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ChannelAllocationStrategy.setStatus(_A)
class _R2MaxActiveCalls_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_R2MaxActiveCalls_Type.__name__=_l
_R2MaxActiveCalls_Object=MibTableColumn
r2MaxActiveCalls=_R2MaxActiveCalls_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,100,1,400),_R2MaxActiveCalls_Type())
r2MaxActiveCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:r2MaxActiveCalls.setStatus(_A)
class _R2EncodingScheme_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('g711alaw',100),('g711ulaw',200)))
_R2EncodingScheme_Type.__name__=_C
_R2EncodingScheme_Object=MibTableColumn
r2EncodingScheme=_R2EncodingScheme_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,100,1,500),_R2EncodingScheme_Type())
r2EncodingScheme.setMaxAccess(_B)
if mibBuilder.loadTexts:r2EncodingScheme.setStatus(_A)
class _R2LineSignaling_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(100));namedValues=NamedValues(('q4212BitsSignaling',100))
_R2LineSignaling_Type.__name__=_C
_R2LineSignaling_Object=MibTableColumn
r2LineSignaling=_R2LineSignaling_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,100,1,600),_R2LineSignaling_Type())
r2LineSignaling.setMaxAccess(_B)
if mibBuilder.loadTexts:r2LineSignaling.setStatus(_A)
class _R2IncomingDigitSignaling_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('mfcR2',100),('dtmfR2',200)))
_R2IncomingDigitSignaling_Type.__name__=_C
_R2IncomingDigitSignaling_Object=MibTableColumn
r2IncomingDigitSignaling=_R2IncomingDigitSignaling_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,100,1,750),_R2IncomingDigitSignaling_Type())
r2IncomingDigitSignaling.setMaxAccess(_B)
if mibBuilder.loadTexts:r2IncomingDigitSignaling.setStatus(_A)
class _R2OutgoingDigitSignaling_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('mfcR2',100),('dtmfR2',200)))
_R2OutgoingDigitSignaling_Type.__name__=_C
_R2OutgoingDigitSignaling_Object=MibTableColumn
r2OutgoingDigitSignaling=_R2OutgoingDigitSignaling_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,100,1,760),_R2OutgoingDigitSignaling_Type())
r2OutgoingDigitSignaling.setMaxAccess(_B)
if mibBuilder.loadTexts:r2OutgoingDigitSignaling.setStatus(_A)
class _R2CountrySelection_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700)));namedValues=NamedValues(*(('brazilR2',100),('mexicoR2',200),('argentinaR2',300),('saudiArabiaR2',400),('venezuelaR2',500),('philippinesR2',600),('iTUTR2',700)))
_R2CountrySelection_Type.__name__=_C
_R2CountrySelection_Object=MibTableColumn
r2CountrySelection=_R2CountrySelection_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,100,1,800),_R2CountrySelection_Type())
r2CountrySelection.setMaxAccess(_B)
if mibBuilder.loadTexts:r2CountrySelection.setStatus(_A)
class _R2DigitAttenuation_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_R2DigitAttenuation_Type.__name__=_l
_R2DigitAttenuation_Object=MibTableColumn
r2DigitAttenuation=_R2DigitAttenuation_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,100,1,900),_R2DigitAttenuation_Type())
r2DigitAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:r2DigitAttenuation.setStatus(_A)
_R2SignalingVariantsTable_Object=MibTable
r2SignalingVariantsTable=_R2SignalingVariantsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,200))
if mibBuilder.loadTexts:r2SignalingVariantsTable.setStatus(_A)
_R2SignalingVariantsEntry_Object=MibTableRow
r2SignalingVariantsEntry=_R2SignalingVariantsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,200,1))
r2SignalingVariantsEntry.setIndexNames((0,_V,_A4))
if mibBuilder.loadTexts:r2SignalingVariantsEntry.setStatus(_A)
_R2SignalingVariantsInterfaceName_Type=OctetString
_R2SignalingVariantsInterfaceName_Object=MibTableColumn
r2SignalingVariantsInterfaceName=_R2SignalingVariantsInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,200,1,100),_R2SignalingVariantsInterfaceName_Type())
r2SignalingVariantsInterfaceName.setMaxAccess(_E)
if mibBuilder.loadTexts:r2SignalingVariantsInterfaceName.setStatus(_A)
class _R2SignalingVariantsOverrideDefault_Type(MxEnableState):defaultValue=0
_R2SignalingVariantsOverrideDefault_Type.__name__=_U
_R2SignalingVariantsOverrideDefault_Object=MibTableColumn
r2SignalingVariantsOverrideDefault=_R2SignalingVariantsOverrideDefault_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,200,1,300),_R2SignalingVariantsOverrideDefault_Type())
r2SignalingVariantsOverrideDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:r2SignalingVariantsOverrideDefault.setStatus(_A)
class _R2SignalingVariantsBitsCD_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_R2SignalingVariantsBitsCD_Type.__name__=_C
_R2SignalingVariantsBitsCD_Object=MibTableColumn
r2SignalingVariantsBitsCD=_R2SignalingVariantsBitsCD_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,200,1,400),_R2SignalingVariantsBitsCD_Type())
r2SignalingVariantsBitsCD.setMaxAccess(_B)
if mibBuilder.loadTexts:r2SignalingVariantsBitsCD.setStatus(_A)
class _R2SignalingVariantsDnisLength_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_R2SignalingVariantsDnisLength_Type.__name__=_l
_R2SignalingVariantsDnisLength_Object=MibTableColumn
r2SignalingVariantsDnisLength=_R2SignalingVariantsDnisLength_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,200,1,500),_R2SignalingVariantsDnisLength_Type())
r2SignalingVariantsDnisLength.setMaxAccess(_B)
if mibBuilder.loadTexts:r2SignalingVariantsDnisLength.setStatus(_A)
class _R2SignalingVariantsAniLength_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_R2SignalingVariantsAniLength_Type.__name__=_l
_R2SignalingVariantsAniLength_Object=MibTableColumn
r2SignalingVariantsAniLength=_R2SignalingVariantsAniLength_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,200,1,600),_R2SignalingVariantsAniLength_Type())
r2SignalingVariantsAniLength.setMaxAccess(_B)
if mibBuilder.loadTexts:r2SignalingVariantsAniLength.setStatus(_A)
class _R2SignalingVariantsAniRequestEnable_Type(MxEnableState):defaultValue=1
_R2SignalingVariantsAniRequestEnable_Type.__name__=_U
_R2SignalingVariantsAniRequestEnable_Object=MibTableColumn
r2SignalingVariantsAniRequestEnable=_R2SignalingVariantsAniRequestEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,200,1,700),_R2SignalingVariantsAniRequestEnable_Type())
r2SignalingVariantsAniRequestEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:r2SignalingVariantsAniRequestEnable.setStatus(_A)
class _R2SignalingVariantsSendAniRequestAfterDnisDigits_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_R2SignalingVariantsSendAniRequestAfterDnisDigits_Type.__name__=_l
_R2SignalingVariantsSendAniRequestAfterDnisDigits_Object=MibTableColumn
r2SignalingVariantsSendAniRequestAfterDnisDigits=_R2SignalingVariantsSendAniRequestAfterDnisDigits_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,200,1,800),_R2SignalingVariantsSendAniRequestAfterDnisDigits_Type())
r2SignalingVariantsSendAniRequestAfterDnisDigits.setMaxAccess(_B)
if mibBuilder.loadTexts:r2SignalingVariantsSendAniRequestAfterDnisDigits.setStatus(_A)
class _R2SignalingVariantsCollectCallBlocked_Type(MxEnableState):defaultValue=1
_R2SignalingVariantsCollectCallBlocked_Type.__name__=_U
_R2SignalingVariantsCollectCallBlocked_Object=MibTableColumn
r2SignalingVariantsCollectCallBlocked=_R2SignalingVariantsCollectCallBlocked_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,200,1,900),_R2SignalingVariantsCollectCallBlocked_Type())
r2SignalingVariantsCollectCallBlocked.setMaxAccess(_B)
if mibBuilder.loadTexts:r2SignalingVariantsCollectCallBlocked.setStatus(_A)
class _R2SignalingVariantsAniCategory_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100)));namedValues=NamedValues(*(('natSubscriberNoPrio',100),('natSubscriberPrio',200),('natMaintenance',300),('natSpare',400),('natOperator',500),('natData',600),('intSubscriberNoPrio',700),('intData',800),('intSubscriberPrio',900),('intOperator',1000),('collectCall',1100)))
_R2SignalingVariantsAniCategory_Type.__name__=_C
_R2SignalingVariantsAniCategory_Object=MibTableColumn
r2SignalingVariantsAniCategory=_R2SignalingVariantsAniCategory_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,200,1,920),_R2SignalingVariantsAniCategory_Type())
r2SignalingVariantsAniCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:r2SignalingVariantsAniCategory.setStatus(_A)
class _R2SignalingVariantsLineFreeCategory_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('lineFreeCharge',100),('lineFreeNoCharge',200)))
_R2SignalingVariantsLineFreeCategory_Type.__name__=_C
_R2SignalingVariantsLineFreeCategory_Object=MibTableColumn
r2SignalingVariantsLineFreeCategory=_R2SignalingVariantsLineFreeCategory_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,200,1,930),_R2SignalingVariantsLineFreeCategory_Type())
r2SignalingVariantsLineFreeCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:r2SignalingVariantsLineFreeCategory.setStatus(_A)
class _R2SignalingVariantsAniRestrictedEnable_Type(MxEnableState):defaultValue=1
_R2SignalingVariantsAniRestrictedEnable_Type.__name__=_U
_R2SignalingVariantsAniRestrictedEnable_Object=MibTableColumn
r2SignalingVariantsAniRestrictedEnable=_R2SignalingVariantsAniRestrictedEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,200,1,950),_R2SignalingVariantsAniRestrictedEnable_Type())
r2SignalingVariantsAniRestrictedEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:r2SignalingVariantsAniRestrictedEnable.setStatus(_A)
class _R2SignalingVariantsIncomingDeclineMethod_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('release',100),('clearBack',200)))
_R2SignalingVariantsIncomingDeclineMethod_Type.__name__=_C
_R2SignalingVariantsIncomingDeclineMethod_Object=MibTableColumn
r2SignalingVariantsIncomingDeclineMethod=_R2SignalingVariantsIncomingDeclineMethod_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,200,1,970),_R2SignalingVariantsIncomingDeclineMethod_Type())
r2SignalingVariantsIncomingDeclineMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:r2SignalingVariantsIncomingDeclineMethod.setStatus(_A)
class _R2SignalingVariantsResetSpecific_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_A1,0),(_A2,10)))
_R2SignalingVariantsResetSpecific_Type.__name__=_C
_R2SignalingVariantsResetSpecific_Object=MibTableColumn
r2SignalingVariantsResetSpecific=_R2SignalingVariantsResetSpecific_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,200,1,1000),_R2SignalingVariantsResetSpecific_Type())
r2SignalingVariantsResetSpecific.setMaxAccess(_B)
if mibBuilder.loadTexts:r2SignalingVariantsResetSpecific.setStatus(_A)
_R2TimerVariantsTable_Object=MibTable
r2TimerVariantsTable=_R2TimerVariantsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300))
if mibBuilder.loadTexts:r2TimerVariantsTable.setStatus(_A)
_R2TimerVariantsEntry_Object=MibTableRow
r2TimerVariantsEntry=_R2TimerVariantsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1))
r2TimerVariantsEntry.setIndexNames((0,_V,_A5))
if mibBuilder.loadTexts:r2TimerVariantsEntry.setStatus(_A)
_R2TimerVariantsInterfaceName_Type=OctetString
_R2TimerVariantsInterfaceName_Object=MibTableColumn
r2TimerVariantsInterfaceName=_R2TimerVariantsInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,100),_R2TimerVariantsInterfaceName_Type())
r2TimerVariantsInterfaceName.setMaxAccess(_E)
if mibBuilder.loadTexts:r2TimerVariantsInterfaceName.setStatus(_A)
class _R2TimerVariantsOverrideDefault_Type(MxEnableState):defaultValue=0
_R2TimerVariantsOverrideDefault_Type.__name__=_U
_R2TimerVariantsOverrideDefault_Object=MibTableColumn
r2TimerVariantsOverrideDefault=_R2TimerVariantsOverrideDefault_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,300),_R2TimerVariantsOverrideDefault_Type())
r2TimerVariantsOverrideDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsOverrideDefault.setStatus(_A)
class _R2TimerVariantsSeizureAckTimeout_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_R2TimerVariantsSeizureAckTimeout_Type.__name__=_C
_R2TimerVariantsSeizureAckTimeout_Object=MibTableColumn
r2TimerVariantsSeizureAckTimeout=_R2TimerVariantsSeizureAckTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,400),_R2TimerVariantsSeizureAckTimeout_Type())
r2TimerVariantsSeizureAckTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsSeizureAckTimeout.setStatus(_A)
class _R2TimerVariantsFaultSeizureAckTimeout_Type(Integer32):defaultValue=60000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_R2TimerVariantsFaultSeizureAckTimeout_Type.__name__=_C
_R2TimerVariantsFaultSeizureAckTimeout_Object=MibTableColumn
r2TimerVariantsFaultSeizureAckTimeout=_R2TimerVariantsFaultSeizureAckTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,500),_R2TimerVariantsFaultSeizureAckTimeout_Type())
r2TimerVariantsFaultSeizureAckTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsFaultSeizureAckTimeout.setStatus(_A)
class _R2TimerVariantsDoubleSeizureTimeout_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_R2TimerVariantsDoubleSeizureTimeout_Type.__name__=_C
_R2TimerVariantsDoubleSeizureTimeout_Object=MibTableColumn
r2TimerVariantsDoubleSeizureTimeout=_R2TimerVariantsDoubleSeizureTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,600),_R2TimerVariantsDoubleSeizureTimeout_Type())
r2TimerVariantsDoubleSeizureTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsDoubleSeizureTimeout.setStatus(_A)
class _R2TimerVariantsDoubleAnswerTimeout_Type(Integer32):defaultValue=1500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,90000))
_R2TimerVariantsDoubleAnswerTimeout_Type.__name__=_C
_R2TimerVariantsDoubleAnswerTimeout_Object=MibTableColumn
r2TimerVariantsDoubleAnswerTimeout=_R2TimerVariantsDoubleAnswerTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,700),_R2TimerVariantsDoubleAnswerTimeout_Type())
r2TimerVariantsDoubleAnswerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsDoubleAnswerTimeout.setStatus(_A)
class _R2TimerVariantsAnswerTimeout_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8000))
_R2TimerVariantsAnswerTimeout_Type.__name__=_C
_R2TimerVariantsAnswerTimeout_Object=MibTableColumn
r2TimerVariantsAnswerTimeout=_R2TimerVariantsAnswerTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,710),_R2TimerVariantsAnswerTimeout_Type())
r2TimerVariantsAnswerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsAnswerTimeout.setStatus(_A)
class _R2TimerVariantsReAnswerTimeout_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8000))
_R2TimerVariantsReAnswerTimeout_Type.__name__=_C
_R2TimerVariantsReAnswerTimeout_Object=MibTableColumn
r2TimerVariantsReAnswerTimeout=_R2TimerVariantsReAnswerTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,720),_R2TimerVariantsReAnswerTimeout_Type())
r2TimerVariantsReAnswerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsReAnswerTimeout.setStatus(_A)
class _R2TimerVariantsReleaseGuardTimeout_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4000))
_R2TimerVariantsReleaseGuardTimeout_Type.__name__=_C
_R2TimerVariantsReleaseGuardTimeout_Object=MibTableColumn
r2TimerVariantsReleaseGuardTimeout=_R2TimerVariantsReleaseGuardTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,800),_R2TimerVariantsReleaseGuardTimeout_Type())
r2TimerVariantsReleaseGuardTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsReleaseGuardTimeout.setStatus(_A)
class _R2TimerVariantsInterCallGuardTimeout_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15000))
_R2TimerVariantsInterCallGuardTimeout_Type.__name__=_C
_R2TimerVariantsInterCallGuardTimeout_Object=MibTableColumn
r2TimerVariantsInterCallGuardTimeout=_R2TimerVariantsInterCallGuardTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,820),_R2TimerVariantsInterCallGuardTimeout_Type())
r2TimerVariantsInterCallGuardTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsInterCallGuardTimeout.setStatus(_A)
class _R2TimerVariantsNoDigitTimeout_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120000))
_R2TimerVariantsNoDigitTimeout_Type.__name__=_C
_R2TimerVariantsNoDigitTimeout_Object=MibTableColumn
r2TimerVariantsNoDigitTimeout=_R2TimerVariantsNoDigitTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,830),_R2TimerVariantsNoDigitTimeout_Type())
r2TimerVariantsNoDigitTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsNoDigitTimeout.setStatus(_A)
class _R2TimerVariantsCongestionToneGuardTimeout_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000))
_R2TimerVariantsCongestionToneGuardTimeout_Type.__name__=_C
_R2TimerVariantsCongestionToneGuardTimeout_Object=MibTableColumn
r2TimerVariantsCongestionToneGuardTimeout=_R2TimerVariantsCongestionToneGuardTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,850),_R2TimerVariantsCongestionToneGuardTimeout_Type())
r2TimerVariantsCongestionToneGuardTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsCongestionToneGuardTimeout.setStatus(_A)
class _R2TimerVariantsUnblockingTimeout_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4000))
_R2TimerVariantsUnblockingTimeout_Type.__name__=_C
_R2TimerVariantsUnblockingTimeout_Object=MibTableColumn
r2TimerVariantsUnblockingTimeout=_R2TimerVariantsUnblockingTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,900),_R2TimerVariantsUnblockingTimeout_Type())
r2TimerVariantsUnblockingTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsUnblockingTimeout.setStatus(_A)
class _R2TimerVariantsAddressCompleteTimeout_Type(Integer32):defaultValue=8000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20000))
_R2TimerVariantsAddressCompleteTimeout_Type.__name__=_C
_R2TimerVariantsAddressCompleteTimeout_Object=MibTableColumn
r2TimerVariantsAddressCompleteTimeout=_R2TimerVariantsAddressCompleteTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,1000),_R2TimerVariantsAddressCompleteTimeout_Type())
r2TimerVariantsAddressCompleteTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsAddressCompleteTimeout.setStatus(_A)
class _R2TimerVariantsWaitAnswerTimeout_Type(Integer32):defaultValue=60000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600000))
_R2TimerVariantsWaitAnswerTimeout_Type.__name__=_C
_R2TimerVariantsWaitAnswerTimeout_Object=MibTableColumn
r2TimerVariantsWaitAnswerTimeout=_R2TimerVariantsWaitAnswerTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,1100),_R2TimerVariantsWaitAnswerTimeout_Type())
r2TimerVariantsWaitAnswerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsWaitAnswerTimeout.setStatus(_A)
class _R2TimerVariantsDigitCompleteTimeout_Type(Integer32):defaultValue=4000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_R2TimerVariantsDigitCompleteTimeout_Type.__name__=_C
_R2TimerVariantsDigitCompleteTimeout_Object=MibTableColumn
r2TimerVariantsDigitCompleteTimeout=_R2TimerVariantsDigitCompleteTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,1200),_R2TimerVariantsDigitCompleteTimeout_Type())
r2TimerVariantsDigitCompleteTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsDigitCompleteTimeout.setStatus(_A)
class _R2TimerVariantsWaitGroupBResponseCompleteTimeout_Type(Integer32):defaultValue=3000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_R2TimerVariantsWaitGroupBResponseCompleteTimeout_Type.__name__=_C
_R2TimerVariantsWaitGroupBResponseCompleteTimeout_Object=MibTableColumn
r2TimerVariantsWaitGroupBResponseCompleteTimeout=_R2TimerVariantsWaitGroupBResponseCompleteTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,1300),_R2TimerVariantsWaitGroupBResponseCompleteTimeout_Type())
r2TimerVariantsWaitGroupBResponseCompleteTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsWaitGroupBResponseCompleteTimeout.setStatus(_A)
class _R2TimerVariantsWaitImmediateResponseCompleteTimeout_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_R2TimerVariantsWaitImmediateResponseCompleteTimeout_Type.__name__=_C
_R2TimerVariantsWaitImmediateResponseCompleteTimeout_Object=MibTableColumn
r2TimerVariantsWaitImmediateResponseCompleteTimeout=_R2TimerVariantsWaitImmediateResponseCompleteTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,1400),_R2TimerVariantsWaitImmediateResponseCompleteTimeout_Type())
r2TimerVariantsWaitImmediateResponseCompleteTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsWaitImmediateResponseCompleteTimeout.setStatus(_A)
class _R2TimerVariantsPlayToneGuardTimeout_Type(Integer32):defaultValue=70;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_R2TimerVariantsPlayToneGuardTimeout_Type.__name__=_C
_R2TimerVariantsPlayToneGuardTimeout_Object=MibTableColumn
r2TimerVariantsPlayToneGuardTimeout=_R2TimerVariantsPlayToneGuardTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,1500),_R2TimerVariantsPlayToneGuardTimeout_Type())
r2TimerVariantsPlayToneGuardTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsPlayToneGuardTimeout.setStatus(_A)
class _R2TimerVariantsAcceptCallTimeout_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_R2TimerVariantsAcceptCallTimeout_Type.__name__=_C
_R2TimerVariantsAcceptCallTimeout_Object=MibTableColumn
r2TimerVariantsAcceptCallTimeout=_R2TimerVariantsAcceptCallTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,1600),_R2TimerVariantsAcceptCallTimeout_Type())
r2TimerVariantsAcceptCallTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsAcceptCallTimeout.setStatus(_A)
class _R2TimerVariantsClearForwardGuardTimeout_Type(Integer32):defaultValue=1500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600000))
_R2TimerVariantsClearForwardGuardTimeout_Type.__name__=_C
_R2TimerVariantsClearForwardGuardTimeout_Object=MibTableColumn
r2TimerVariantsClearForwardGuardTimeout=_R2TimerVariantsClearForwardGuardTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,1700),_R2TimerVariantsClearForwardGuardTimeout_Type())
r2TimerVariantsClearForwardGuardTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsClearForwardGuardTimeout.setStatus(_A)
class _R2TimerVariantsClearBackwardGuardTimeout_Type(Integer32):defaultValue=1500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600000))
_R2TimerVariantsClearBackwardGuardTimeout_Type.__name__=_C
_R2TimerVariantsClearBackwardGuardTimeout_Object=MibTableColumn
r2TimerVariantsClearBackwardGuardTimeout=_R2TimerVariantsClearBackwardGuardTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,1800),_R2TimerVariantsClearBackwardGuardTimeout_Type())
r2TimerVariantsClearBackwardGuardTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsClearBackwardGuardTimeout.setStatus(_A)
class _R2TimerVariantsFaultOnAnsweredGuardTimeout_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400000))
_R2TimerVariantsFaultOnAnsweredGuardTimeout_Type.__name__=_C
_R2TimerVariantsFaultOnAnsweredGuardTimeout_Object=MibTableColumn
r2TimerVariantsFaultOnAnsweredGuardTimeout=_R2TimerVariantsFaultOnAnsweredGuardTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,1900),_R2TimerVariantsFaultOnAnsweredGuardTimeout_Type())
r2TimerVariantsFaultOnAnsweredGuardTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsFaultOnAnsweredGuardTimeout.setStatus(_A)
class _R2TimerVariantsFaultOnClearBackwardGuardTimeout_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400000))
_R2TimerVariantsFaultOnClearBackwardGuardTimeout_Type.__name__=_C
_R2TimerVariantsFaultOnClearBackwardGuardTimeout_Object=MibTableColumn
r2TimerVariantsFaultOnClearBackwardGuardTimeout=_R2TimerVariantsFaultOnClearBackwardGuardTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,2000),_R2TimerVariantsFaultOnClearBackwardGuardTimeout_Type())
r2TimerVariantsFaultOnClearBackwardGuardTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsFaultOnClearBackwardGuardTimeout.setStatus(_A)
class _R2TimerVariantsFaultOnSeizeAckGuardTimeout_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400000))
_R2TimerVariantsFaultOnSeizeAckGuardTimeout_Type.__name__=_C
_R2TimerVariantsFaultOnSeizeAckGuardTimeout_Object=MibTableColumn
r2TimerVariantsFaultOnSeizeAckGuardTimeout=_R2TimerVariantsFaultOnSeizeAckGuardTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,2100),_R2TimerVariantsFaultOnSeizeAckGuardTimeout_Type())
r2TimerVariantsFaultOnSeizeAckGuardTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsFaultOnSeizeAckGuardTimeout.setStatus(_A)
class _R2TimerVariantsFaultOnSeizeGuardTimeout_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400000))
_R2TimerVariantsFaultOnSeizeGuardTimeout_Type.__name__=_C
_R2TimerVariantsFaultOnSeizeGuardTimeout_Object=MibTableColumn
r2TimerVariantsFaultOnSeizeGuardTimeout=_R2TimerVariantsFaultOnSeizeGuardTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,2200),_R2TimerVariantsFaultOnSeizeGuardTimeout_Type())
r2TimerVariantsFaultOnSeizeGuardTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsFaultOnSeizeGuardTimeout.setStatus(_A)
class _R2TimerVariantsDeclineGuardTimeout_Type(Integer32):defaultValue=1500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,2000))
_R2TimerVariantsDeclineGuardTimeout_Type.__name__=_C
_R2TimerVariantsDeclineGuardTimeout_Object=MibTableColumn
r2TimerVariantsDeclineGuardTimeout=_R2TimerVariantsDeclineGuardTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,2250),_R2TimerVariantsDeclineGuardTimeout_Type())
r2TimerVariantsDeclineGuardTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsDeclineGuardTimeout.setStatus(_A)
class _R2TimerVariantsResetSpecific_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_A1,0),(_A2,10)))
_R2TimerVariantsResetSpecific_Type.__name__=_C
_R2TimerVariantsResetSpecific_Object=MibTableColumn
r2TimerVariantsResetSpecific=_R2TimerVariantsResetSpecific_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,300,1,2300),_R2TimerVariantsResetSpecific_Type())
r2TimerVariantsResetSpecific.setMaxAccess(_B)
if mibBuilder.loadTexts:r2TimerVariantsResetSpecific.setStatus(_A)
_R2DigitTimerVariantsTable_Object=MibTable
r2DigitTimerVariantsTable=_R2DigitTimerVariantsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,400))
if mibBuilder.loadTexts:r2DigitTimerVariantsTable.setStatus(_A)
_R2DigitTimerVariantsEntry_Object=MibTableRow
r2DigitTimerVariantsEntry=_R2DigitTimerVariantsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,400,1))
r2DigitTimerVariantsEntry.setIndexNames((0,_V,_A6))
if mibBuilder.loadTexts:r2DigitTimerVariantsEntry.setStatus(_A)
_R2DigitTimerVariantsInterfaceName_Type=OctetString
_R2DigitTimerVariantsInterfaceName_Object=MibTableColumn
r2DigitTimerVariantsInterfaceName=_R2DigitTimerVariantsInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,400,1,100),_R2DigitTimerVariantsInterfaceName_Type())
r2DigitTimerVariantsInterfaceName.setMaxAccess(_E)
if mibBuilder.loadTexts:r2DigitTimerVariantsInterfaceName.setStatus(_A)
class _R2DigitTimerVariantsOverrideDefault_Type(MxEnableState):defaultValue=0
_R2DigitTimerVariantsOverrideDefault_Type.__name__=_U
_R2DigitTimerVariantsOverrideDefault_Object=MibTableColumn
r2DigitTimerVariantsOverrideDefault=_R2DigitTimerVariantsOverrideDefault_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,400,1,300),_R2DigitTimerVariantsOverrideDefault_Type())
r2DigitTimerVariantsOverrideDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:r2DigitTimerVariantsOverrideDefault.setStatus(_A)
class _R2DigitTimerVariantsMfCongestionToneDuration_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120000))
_R2DigitTimerVariantsMfCongestionToneDuration_Type.__name__=_C
_R2DigitTimerVariantsMfCongestionToneDuration_Object=MibTableColumn
r2DigitTimerVariantsMfCongestionToneDuration=_R2DigitTimerVariantsMfCongestionToneDuration_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,400,1,350),_R2DigitTimerVariantsMfCongestionToneDuration_Type())
r2DigitTimerVariantsMfCongestionToneDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:r2DigitTimerVariantsMfCongestionToneDuration.setStatus(_A)
class _R2DigitTimerVariantsMfcPulseInterDigitTimeout_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_R2DigitTimerVariantsMfcPulseInterDigitTimeout_Type.__name__=_C
_R2DigitTimerVariantsMfcPulseInterDigitTimeout_Object=MibTableColumn
r2DigitTimerVariantsMfcPulseInterDigitTimeout=_R2DigitTimerVariantsMfcPulseInterDigitTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,400,1,400),_R2DigitTimerVariantsMfcPulseInterDigitTimeout_Type())
r2DigitTimerVariantsMfcPulseInterDigitTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2DigitTimerVariantsMfcPulseInterDigitTimeout.setStatus(_A)
class _R2DigitTimerVariantsMfcPulseMinOnTimeout_Type(Integer32):defaultValue=150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_R2DigitTimerVariantsMfcPulseMinOnTimeout_Type.__name__=_C
_R2DigitTimerVariantsMfcPulseMinOnTimeout_Object=MibTableColumn
r2DigitTimerVariantsMfcPulseMinOnTimeout=_R2DigitTimerVariantsMfcPulseMinOnTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,400,1,500),_R2DigitTimerVariantsMfcPulseMinOnTimeout_Type())
r2DigitTimerVariantsMfcPulseMinOnTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2DigitTimerVariantsMfcPulseMinOnTimeout.setStatus(_A)
class _R2DigitTimerVariantsMfcMaxSequenceTimeout_Type(Integer32):defaultValue=10000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,70000))
_R2DigitTimerVariantsMfcMaxSequenceTimeout_Type.__name__=_C
_R2DigitTimerVariantsMfcMaxSequenceTimeout_Object=MibTableColumn
r2DigitTimerVariantsMfcMaxSequenceTimeout=_R2DigitTimerVariantsMfcMaxSequenceTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,400,1,600),_R2DigitTimerVariantsMfcMaxSequenceTimeout_Type())
r2DigitTimerVariantsMfcMaxSequenceTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2DigitTimerVariantsMfcMaxSequenceTimeout.setStatus(_A)
class _R2DigitTimerVariantsMfcMaxOnTimeout_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,35000))
_R2DigitTimerVariantsMfcMaxOnTimeout_Type.__name__=_C
_R2DigitTimerVariantsMfcMaxOnTimeout_Object=MibTableColumn
r2DigitTimerVariantsMfcMaxOnTimeout=_R2DigitTimerVariantsMfcMaxOnTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,400,1,700),_R2DigitTimerVariantsMfcMaxOnTimeout_Type())
r2DigitTimerVariantsMfcMaxOnTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2DigitTimerVariantsMfcMaxOnTimeout.setStatus(_A)
class _R2DigitTimerVariantsMfcMaxOffTimeout_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,35000))
_R2DigitTimerVariantsMfcMaxOffTimeout_Type.__name__=_C
_R2DigitTimerVariantsMfcMaxOffTimeout_Object=MibTableColumn
r2DigitTimerVariantsMfcMaxOffTimeout=_R2DigitTimerVariantsMfcMaxOffTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,400,1,800),_R2DigitTimerVariantsMfcMaxOffTimeout_Type())
r2DigitTimerVariantsMfcMaxOffTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2DigitTimerVariantsMfcMaxOffTimeout.setStatus(_A)
class _R2DigitTimerVariantsResetSpecific_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_A1,0),(_A2,10)))
_R2DigitTimerVariantsResetSpecific_Type.__name__=_C
_R2DigitTimerVariantsResetSpecific_Object=MibTableColumn
r2DigitTimerVariantsResetSpecific=_R2DigitTimerVariantsResetSpecific_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,400,1,900),_R2DigitTimerVariantsResetSpecific_Type())
r2DigitTimerVariantsResetSpecific.setMaxAccess(_B)
if mibBuilder.loadTexts:r2DigitTimerVariantsResetSpecific.setStatus(_A)
_R2LinkTimerVariantsTable_Object=MibTable
r2LinkTimerVariantsTable=_R2LinkTimerVariantsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,500))
if mibBuilder.loadTexts:r2LinkTimerVariantsTable.setStatus(_A)
_R2LinkTimerVariantsEntry_Object=MibTableRow
r2LinkTimerVariantsEntry=_R2LinkTimerVariantsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,500,1))
r2LinkTimerVariantsEntry.setIndexNames((0,_V,_A7))
if mibBuilder.loadTexts:r2LinkTimerVariantsEntry.setStatus(_A)
_R2LinkTimerVariantsInterfaceName_Type=OctetString
_R2LinkTimerVariantsInterfaceName_Object=MibTableColumn
r2LinkTimerVariantsInterfaceName=_R2LinkTimerVariantsInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,500,1,100),_R2LinkTimerVariantsInterfaceName_Type())
r2LinkTimerVariantsInterfaceName.setMaxAccess(_E)
if mibBuilder.loadTexts:r2LinkTimerVariantsInterfaceName.setStatus(_A)
class _R2LinkTimerVariantsOverrideDefault_Type(MxEnableState):defaultValue=0
_R2LinkTimerVariantsOverrideDefault_Type.__name__=_U
_R2LinkTimerVariantsOverrideDefault_Object=MibTableColumn
r2LinkTimerVariantsOverrideDefault=_R2LinkTimerVariantsOverrideDefault_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,500,1,300),_R2LinkTimerVariantsOverrideDefault_Type())
r2LinkTimerVariantsOverrideDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:r2LinkTimerVariantsOverrideDefault.setStatus(_A)
class _R2LinkTimerVariantsLinkActivationTimeout_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_R2LinkTimerVariantsLinkActivationTimeout_Type.__name__=_C
_R2LinkTimerVariantsLinkActivationTimeout_Object=MibTableColumn
r2LinkTimerVariantsLinkActivationTimeout=_R2LinkTimerVariantsLinkActivationTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,500,1,400),_R2LinkTimerVariantsLinkActivationTimeout_Type())
r2LinkTimerVariantsLinkActivationTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2LinkTimerVariantsLinkActivationTimeout.setStatus(_A)
class _R2LinkTimerVariantsLinkActivationRetryTimeout_Type(Integer32):defaultValue=3000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_R2LinkTimerVariantsLinkActivationRetryTimeout_Type.__name__=_C
_R2LinkTimerVariantsLinkActivationRetryTimeout_Object=MibTableColumn
r2LinkTimerVariantsLinkActivationRetryTimeout=_R2LinkTimerVariantsLinkActivationRetryTimeout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,500,1,500),_R2LinkTimerVariantsLinkActivationRetryTimeout_Type())
r2LinkTimerVariantsLinkActivationRetryTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:r2LinkTimerVariantsLinkActivationRetryTimeout.setStatus(_A)
class _R2LinkTimerVariantsResetSpecific_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_A1,0),(_A2,10)))
_R2LinkTimerVariantsResetSpecific_Type.__name__=_C
_R2LinkTimerVariantsResetSpecific_Object=MibTableColumn
r2LinkTimerVariantsResetSpecific=_R2LinkTimerVariantsResetSpecific_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,500,1,600),_R2LinkTimerVariantsResetSpecific_Type())
r2LinkTimerVariantsResetSpecific.setMaxAccess(_B)
if mibBuilder.loadTexts:r2LinkTimerVariantsResetSpecific.setStatus(_A)
_R2ToneVariantsTable_Object=MibTable
r2ToneVariantsTable=_R2ToneVariantsTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600))
if mibBuilder.loadTexts:r2ToneVariantsTable.setStatus(_A)
_R2ToneVariantsEntry_Object=MibTableRow
r2ToneVariantsEntry=_R2ToneVariantsEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1))
r2ToneVariantsEntry.setIndexNames((0,_V,_A8))
if mibBuilder.loadTexts:r2ToneVariantsEntry.setStatus(_A)
_R2ToneVariantsInterfaceName_Type=OctetString
_R2ToneVariantsInterfaceName_Object=MibTableColumn
r2ToneVariantsInterfaceName=_R2ToneVariantsInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,100),_R2ToneVariantsInterfaceName_Type())
r2ToneVariantsInterfaceName.setMaxAccess(_E)
if mibBuilder.loadTexts:r2ToneVariantsInterfaceName.setStatus(_A)
class _R2ToneVariantsOverrideDefault_Type(MxEnableState):defaultValue=0
_R2ToneVariantsOverrideDefault_Type.__name__=_U
_R2ToneVariantsOverrideDefault_Object=MibTableColumn
r2ToneVariantsOverrideDefault=_R2ToneVariantsOverrideDefault_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,300),_R2ToneVariantsOverrideDefault_Type())
r2ToneVariantsOverrideDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsOverrideDefault.setStatus(_A)
class _R2ToneVariantsFwdGroup1EndOfDnis_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),('i1',200),('i2',300),('i3',400),('i4',500),('i5',600),('i6',700),('i7',800),('i8',900),('i9',1000),('i10',1100),('i11',1200),('i12',1300),('i13',1400),('i14',1500),('i15',1600)))
_R2ToneVariantsFwdGroup1EndOfDnis_Type.__name__=_C
_R2ToneVariantsFwdGroup1EndOfDnis_Object=MibTableColumn
r2ToneVariantsFwdGroup1EndOfDnis=_R2ToneVariantsFwdGroup1EndOfDnis_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,400),_R2ToneVariantsFwdGroup1EndOfDnis_Type())
r2ToneVariantsFwdGroup1EndOfDnis.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsFwdGroup1EndOfDnis.setStatus(_A)
class _R2ToneVariantsFwdGroup1EndOfAni_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),('i1',200),('i2',300),('i3',400),('i4',500),('i5',600),('i6',700),('i7',800),('i8',900),('i9',1000),('i10',1100),('i11',1200),('i12',1300),('i13',1400),('i14',1500),('i15',1600)))
_R2ToneVariantsFwdGroup1EndOfAni_Type.__name__=_C
_R2ToneVariantsFwdGroup1EndOfAni_Object=MibTableColumn
r2ToneVariantsFwdGroup1EndOfAni=_R2ToneVariantsFwdGroup1EndOfAni_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,500),_R2ToneVariantsFwdGroup1EndOfAni_Type())
r2ToneVariantsFwdGroup1EndOfAni.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsFwdGroup1EndOfAni.setStatus(_A)
class _R2ToneVariantsFwdGroup1RestrictedAni_Type(Integer32):defaultValue=1300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),('i1',200),('i2',300),('i3',400),('i4',500),('i5',600),('i6',700),('i7',800),('i8',900),('i9',1000),('i10',1100),('i11',1200),('i12',1300),('i13',1400),('i14',1500),('i15',1600)))
_R2ToneVariantsFwdGroup1RestrictedAni_Type.__name__=_C
_R2ToneVariantsFwdGroup1RestrictedAni_Object=MibTableColumn
r2ToneVariantsFwdGroup1RestrictedAni=_R2ToneVariantsFwdGroup1RestrictedAni_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,520),_R2ToneVariantsFwdGroup1RestrictedAni_Type())
r2ToneVariantsFwdGroup1RestrictedAni.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsFwdGroup1RestrictedAni.setStatus(_A)
class _R2ToneVariantsBwdGroupASendNextDnisDigit_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_F,200),(_G,300),(_H,400),(_I,500),(_J,600),(_K,700),(_L,800),(_M,900),(_N,1000),(_O,1100),(_P,1200),(_Q,1300),(_R,1400),(_S,1500),(_T,1600)))
_R2ToneVariantsBwdGroupASendNextDnisDigit_Type.__name__=_C
_R2ToneVariantsBwdGroupASendNextDnisDigit_Object=MibTableColumn
r2ToneVariantsBwdGroupASendNextDnisDigit=_R2ToneVariantsBwdGroupASendNextDnisDigit_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,600),_R2ToneVariantsBwdGroupASendNextDnisDigit_Type())
r2ToneVariantsBwdGroupASendNextDnisDigit.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupASendNextDnisDigit.setStatus(_A)
class _R2ToneVariantsBwdGroupASendPreviousDnisDigit_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_F,200),(_G,300),(_H,400),(_I,500),(_J,600),(_K,700),(_L,800),(_M,900),(_N,1000),(_O,1100),(_P,1200),(_Q,1300),(_R,1400),(_S,1500),(_T,1600)))
_R2ToneVariantsBwdGroupASendPreviousDnisDigit_Type.__name__=_C
_R2ToneVariantsBwdGroupASendPreviousDnisDigit_Object=MibTableColumn
r2ToneVariantsBwdGroupASendPreviousDnisDigit=_R2ToneVariantsBwdGroupASendPreviousDnisDigit_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,700),_R2ToneVariantsBwdGroupASendPreviousDnisDigit_Type())
r2ToneVariantsBwdGroupASendPreviousDnisDigit.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupASendPreviousDnisDigit.setStatus(_A)
class _R2ToneVariantsBwdGroupASwitchToGroupII_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_F,200),(_G,300),(_H,400),(_I,500),(_J,600),(_K,700),(_L,800),(_M,900),(_N,1000),(_O,1100),(_P,1200),(_Q,1300),(_R,1400),(_S,1500),(_T,1600)))
_R2ToneVariantsBwdGroupASwitchToGroupII_Type.__name__=_C
_R2ToneVariantsBwdGroupASwitchToGroupII_Object=MibTableColumn
r2ToneVariantsBwdGroupASwitchToGroupII=_R2ToneVariantsBwdGroupASwitchToGroupII_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,800),_R2ToneVariantsBwdGroupASwitchToGroupII_Type())
r2ToneVariantsBwdGroupASwitchToGroupII.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupASwitchToGroupII.setStatus(_A)
class _R2ToneVariantsBwdGroupANetworkCongestion_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_F,200),(_G,300),(_H,400),(_I,500),(_J,600),(_K,700),(_L,800),(_M,900),(_N,1000),(_O,1100),(_P,1200),(_Q,1300),(_R,1400),(_S,1500),(_T,1600)))
_R2ToneVariantsBwdGroupANetworkCongestion_Type.__name__=_C
_R2ToneVariantsBwdGroupANetworkCongestion_Object=MibTableColumn
r2ToneVariantsBwdGroupANetworkCongestion=_R2ToneVariantsBwdGroupANetworkCongestion_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,900),_R2ToneVariantsBwdGroupANetworkCongestion_Type())
r2ToneVariantsBwdGroupANetworkCongestion.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupANetworkCongestion.setStatus(_A)
class _R2ToneVariantsBwdGroupASendCallingPartyCategory_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_F,200),(_G,300),(_H,400),(_I,500),(_J,600),(_K,700),(_L,800),(_M,900),(_N,1000),(_O,1100),(_P,1200),(_Q,1300),(_R,1400),(_S,1500),(_T,1600)))
_R2ToneVariantsBwdGroupASendCallingPartyCategory_Type.__name__=_C
_R2ToneVariantsBwdGroupASendCallingPartyCategory_Object=MibTableColumn
r2ToneVariantsBwdGroupASendCallingPartyCategory=_R2ToneVariantsBwdGroupASendCallingPartyCategory_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,1000),_R2ToneVariantsBwdGroupASendCallingPartyCategory_Type())
r2ToneVariantsBwdGroupASendCallingPartyCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupASendCallingPartyCategory.setStatus(_A)
class _R2ToneVariantsBwdGroupAImmediateAccept_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_F,200),(_G,300),(_H,400),(_I,500),(_J,600),(_K,700),(_L,800),(_M,900),(_N,1000),(_O,1100),(_P,1200),(_Q,1300),(_R,1400),(_S,1500),(_T,1600)))
_R2ToneVariantsBwdGroupAImmediateAccept_Type.__name__=_C
_R2ToneVariantsBwdGroupAImmediateAccept_Object=MibTableColumn
r2ToneVariantsBwdGroupAImmediateAccept=_R2ToneVariantsBwdGroupAImmediateAccept_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,1100),_R2ToneVariantsBwdGroupAImmediateAccept_Type())
r2ToneVariantsBwdGroupAImmediateAccept.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupAImmediateAccept.setStatus(_A)
class _R2ToneVariantsBwdGroupASendDnisDigitNMinus2_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_F,200),(_G,300),(_H,400),(_I,500),(_J,600),(_K,700),(_L,800),(_M,900),(_N,1000),(_O,1100),(_P,1200),(_Q,1300),(_R,1400),(_S,1500),(_T,1600)))
_R2ToneVariantsBwdGroupASendDnisDigitNMinus2_Type.__name__=_C
_R2ToneVariantsBwdGroupASendDnisDigitNMinus2_Object=MibTableColumn
r2ToneVariantsBwdGroupASendDnisDigitNMinus2=_R2ToneVariantsBwdGroupASendDnisDigitNMinus2_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,1200),_R2ToneVariantsBwdGroupASendDnisDigitNMinus2_Type())
r2ToneVariantsBwdGroupASendDnisDigitNMinus2.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupASendDnisDigitNMinus2.setStatus(_A)
class _R2ToneVariantsBwdGroupASendDnisDigitNMinus3_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_F,200),(_G,300),(_H,400),(_I,500),(_J,600),(_K,700),(_L,800),(_M,900),(_N,1000),(_O,1100),(_P,1200),(_Q,1300),(_R,1400),(_S,1500),(_T,1600)))
_R2ToneVariantsBwdGroupASendDnisDigitNMinus3_Type.__name__=_C
_R2ToneVariantsBwdGroupASendDnisDigitNMinus3_Object=MibTableColumn
r2ToneVariantsBwdGroupASendDnisDigitNMinus3=_R2ToneVariantsBwdGroupASendDnisDigitNMinus3_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,1300),_R2ToneVariantsBwdGroupASendDnisDigitNMinus3_Type())
r2ToneVariantsBwdGroupASendDnisDigitNMinus3.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupASendDnisDigitNMinus3.setStatus(_A)
class _R2ToneVariantsBwdGroupARepeatAllDnis_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_F,200),(_G,300),(_H,400),(_I,500),(_J,600),(_K,700),(_L,800),(_M,900),(_N,1000),(_O,1100),(_P,1200),(_Q,1300),(_R,1400),(_S,1500),(_T,1600)))
_R2ToneVariantsBwdGroupARepeatAllDnis_Type.__name__=_C
_R2ToneVariantsBwdGroupARepeatAllDnis_Object=MibTableColumn
r2ToneVariantsBwdGroupARepeatAllDnis=_R2ToneVariantsBwdGroupARepeatAllDnis_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,1400),_R2ToneVariantsBwdGroupARepeatAllDnis_Type())
r2ToneVariantsBwdGroupARepeatAllDnis.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupARepeatAllDnis.setStatus(_A)
class _R2ToneVariantsBwdGroupASendNextAniDigit_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_F,200),(_G,300),(_H,400),(_I,500),(_J,600),(_K,700),(_L,800),(_M,900),(_N,1000),(_O,1100),(_P,1200),(_Q,1300),(_R,1400),(_S,1500),(_T,1600)))
_R2ToneVariantsBwdGroupASendNextAniDigit_Type.__name__=_C
_R2ToneVariantsBwdGroupASendNextAniDigit_Object=MibTableColumn
r2ToneVariantsBwdGroupASendNextAniDigit=_R2ToneVariantsBwdGroupASendNextAniDigit_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,1500),_R2ToneVariantsBwdGroupASendNextAniDigit_Type())
r2ToneVariantsBwdGroupASendNextAniDigit.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupASendNextAniDigit.setStatus(_A)
class _R2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_F,200),(_G,300),(_H,400),(_I,500),(_J,600),(_K,700),(_L,800),(_M,900),(_N,1000),(_O,1100),(_P,1200),(_Q,1300),(_R,1400),(_S,1500),(_T,1600)))
_R2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC_Type.__name__=_C
_R2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC_Object=MibTableColumn
r2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC=_R2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,1550),_R2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC_Type())
r2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC.setStatus(_A)
class _R2ToneVariantsBwdGroupBSendSit_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_W,200),(_X,300),(_Y,400),(_Z,500),(_a,600),(_b,700),(_c,800),(_d,900),(_e,1000),(_f,1100),(_g,1200),(_h,1300),(_i,1400),(_j,1500),(_k,1600)))
_R2ToneVariantsBwdGroupBSendSit_Type.__name__=_C
_R2ToneVariantsBwdGroupBSendSit_Object=MibTableColumn
r2ToneVariantsBwdGroupBSendSit=_R2ToneVariantsBwdGroupBSendSit_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,1600),_R2ToneVariantsBwdGroupBSendSit_Type())
r2ToneVariantsBwdGroupBSendSit.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupBSendSit.setStatus(_A)
class _R2ToneVariantsBwdGroupBUserBusy_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_W,200),(_X,300),(_Y,400),(_Z,500),(_a,600),(_b,700),(_c,800),(_d,900),(_e,1000),(_f,1100),(_g,1200),(_h,1300),(_i,1400),(_j,1500),(_k,1600)))
_R2ToneVariantsBwdGroupBUserBusy_Type.__name__=_C
_R2ToneVariantsBwdGroupBUserBusy_Object=MibTableColumn
r2ToneVariantsBwdGroupBUserBusy=_R2ToneVariantsBwdGroupBUserBusy_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,1700),_R2ToneVariantsBwdGroupBUserBusy_Type())
r2ToneVariantsBwdGroupBUserBusy.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupBUserBusy.setStatus(_A)
class _R2ToneVariantsBwdGroupBNetworkCongestion_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_W,200),(_X,300),(_Y,400),(_Z,500),(_a,600),(_b,700),(_c,800),(_d,900),(_e,1000),(_f,1100),(_g,1200),(_h,1300),(_i,1400),(_j,1500),(_k,1600)))
_R2ToneVariantsBwdGroupBNetworkCongestion_Type.__name__=_C
_R2ToneVariantsBwdGroupBNetworkCongestion_Object=MibTableColumn
r2ToneVariantsBwdGroupBNetworkCongestion=_R2ToneVariantsBwdGroupBNetworkCongestion_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,1800),_R2ToneVariantsBwdGroupBNetworkCongestion_Type())
r2ToneVariantsBwdGroupBNetworkCongestion.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupBNetworkCongestion.setStatus(_A)
class _R2ToneVariantsBwdGroupBUnassignedNumber_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_W,200),(_X,300),(_Y,400),(_Z,500),(_a,600),(_b,700),(_c,800),(_d,900),(_e,1000),(_f,1100),(_g,1200),(_h,1300),(_i,1400),(_j,1500),(_k,1600)))
_R2ToneVariantsBwdGroupBUnassignedNumber_Type.__name__=_C
_R2ToneVariantsBwdGroupBUnassignedNumber_Object=MibTableColumn
r2ToneVariantsBwdGroupBUnassignedNumber=_R2ToneVariantsBwdGroupBUnassignedNumber_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,1900),_R2ToneVariantsBwdGroupBUnassignedNumber_Type())
r2ToneVariantsBwdGroupBUnassignedNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupBUnassignedNumber.setStatus(_A)
class _R2ToneVariantsBwdGroupBLineFreeCharge_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_W,200),(_X,300),(_Y,400),(_Z,500),(_a,600),(_b,700),(_c,800),(_d,900),(_e,1000),(_f,1100),(_g,1200),(_h,1300),(_i,1400),(_j,1500),(_k,1600)))
_R2ToneVariantsBwdGroupBLineFreeCharge_Type.__name__=_C
_R2ToneVariantsBwdGroupBLineFreeCharge_Object=MibTableColumn
r2ToneVariantsBwdGroupBLineFreeCharge=_R2ToneVariantsBwdGroupBLineFreeCharge_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,2000),_R2ToneVariantsBwdGroupBLineFreeCharge_Type())
r2ToneVariantsBwdGroupBLineFreeCharge.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupBLineFreeCharge.setStatus(_A)
class _R2ToneVariantsBwdGroupBSupplementaryLineFreeCharge_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_W,200),(_X,300),(_Y,400),(_Z,500),(_a,600),(_b,700),(_c,800),(_d,900),(_e,1000),(_f,1100),(_g,1200),(_h,1300),(_i,1400),(_j,1500),(_k,1600)))
_R2ToneVariantsBwdGroupBSupplementaryLineFreeCharge_Type.__name__=_C
_R2ToneVariantsBwdGroupBSupplementaryLineFreeCharge_Object=MibTableColumn
r2ToneVariantsBwdGroupBSupplementaryLineFreeCharge=_R2ToneVariantsBwdGroupBSupplementaryLineFreeCharge_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,2100),_R2ToneVariantsBwdGroupBSupplementaryLineFreeCharge_Type())
r2ToneVariantsBwdGroupBSupplementaryLineFreeCharge.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupBSupplementaryLineFreeCharge.setStatus(_A)
class _R2ToneVariantsBwdGroupBLineFreeNoCharge_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_W,200),(_X,300),(_Y,400),(_Z,500),(_a,600),(_b,700),(_c,800),(_d,900),(_e,1000),(_f,1100),(_g,1200),(_h,1300),(_i,1400),(_j,1500),(_k,1600)))
_R2ToneVariantsBwdGroupBLineFreeNoCharge_Type.__name__=_C
_R2ToneVariantsBwdGroupBLineFreeNoCharge_Object=MibTableColumn
r2ToneVariantsBwdGroupBLineFreeNoCharge=_R2ToneVariantsBwdGroupBLineFreeNoCharge_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,2200),_R2ToneVariantsBwdGroupBLineFreeNoCharge_Type())
r2ToneVariantsBwdGroupBLineFreeNoCharge.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupBLineFreeNoCharge.setStatus(_A)
class _R2ToneVariantsBwdGroupBLineOutOfOrder_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_W,200),(_X,300),(_Y,400),(_Z,500),(_a,600),(_b,700),(_c,800),(_d,900),(_e,1000),(_f,1100),(_g,1200),(_h,1300),(_i,1400),(_j,1500),(_k,1600)))
_R2ToneVariantsBwdGroupBLineOutOfOrder_Type.__name__=_C
_R2ToneVariantsBwdGroupBLineOutOfOrder_Object=MibTableColumn
r2ToneVariantsBwdGroupBLineOutOfOrder=_R2ToneVariantsBwdGroupBLineOutOfOrder_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,2300),_R2ToneVariantsBwdGroupBLineOutOfOrder_Type())
r2ToneVariantsBwdGroupBLineOutOfOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupBLineOutOfOrder.setStatus(_A)
class _R2ToneVariantsBwdGroupBChangedNumber_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_W,200),(_X,300),(_Y,400),(_Z,500),(_a,600),(_b,700),(_c,800),(_d,900),(_e,1000),(_f,1100),(_g,1200),(_h,1300),(_i,1400),(_j,1500),(_k,1600)))
_R2ToneVariantsBwdGroupBChangedNumber_Type.__name__=_C
_R2ToneVariantsBwdGroupBChangedNumber_Object=MibTableColumn
r2ToneVariantsBwdGroupBChangedNumber=_R2ToneVariantsBwdGroupBChangedNumber_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,2350),_R2ToneVariantsBwdGroupBChangedNumber_Type())
r2ToneVariantsBwdGroupBChangedNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupBChangedNumber.setStatus(_A)
class _R2ToneVariantsBwdGroupCSendNextAniDigit_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_m,200),(_n,300),(_o,400),(_p,500),(_q,600),(_r,700),(_s,800),(_t,900),(_u,1000),(_v,1100),(_w,1200),(_x,1300),(_y,1400),(_z,1500),(_A0,1600)))
_R2ToneVariantsBwdGroupCSendNextAniDigit_Type.__name__=_C
_R2ToneVariantsBwdGroupCSendNextAniDigit_Object=MibTableColumn
r2ToneVariantsBwdGroupCSendNextAniDigit=_R2ToneVariantsBwdGroupCSendNextAniDigit_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,2355),_R2ToneVariantsBwdGroupCSendNextAniDigit_Type())
r2ToneVariantsBwdGroupCSendNextAniDigit.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupCSendNextAniDigit.setStatus(_A)
class _R2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_m,200),(_n,300),(_o,400),(_p,500),(_q,600),(_r,700),(_s,800),(_t,900),(_u,1000),(_v,1100),(_w,1200),(_x,1300),(_y,1400),(_z,1500),(_A0,1600)))
_R2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA_Type.__name__=_C
_R2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA_Object=MibTableColumn
r2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA=_R2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,2360),_R2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA_Type())
r2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA.setStatus(_A)
class _R2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_m,200),(_n,300),(_o,400),(_p,500),(_q,600),(_r,700),(_s,800),(_t,900),(_u,1000),(_v,1100),(_w,1200),(_x,1300),(_y,1400),(_z,1500),(_A0,1600)))
_R2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA_Type.__name__=_C
_R2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA_Object=MibTableColumn
r2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA=_R2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,2365),_R2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA_Type())
r2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA.setStatus(_A)
class _R2ToneVariantsBwdGroupCNetworkCongestion_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_m,200),(_n,300),(_o,400),(_p,500),(_q,600),(_r,700),(_s,800),(_t,900),(_u,1000),(_v,1100),(_w,1200),(_x,1300),(_y,1400),(_z,1500),(_A0,1600)))
_R2ToneVariantsBwdGroupCNetworkCongestion_Type.__name__=_C
_R2ToneVariantsBwdGroupCNetworkCongestion_Object=MibTableColumn
r2ToneVariantsBwdGroupCNetworkCongestion=_R2ToneVariantsBwdGroupCNetworkCongestion_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,2370),_R2ToneVariantsBwdGroupCNetworkCongestion_Type())
r2ToneVariantsBwdGroupCNetworkCongestion.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupCNetworkCongestion.setStatus(_A)
class _R2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_m,200),(_n,300),(_o,400),(_p,500),(_q,600),(_r,700),(_s,800),(_t,900),(_u,1000),(_v,1100),(_w,1200),(_x,1300),(_y,1400),(_z,1500),(_A0,1600)))
_R2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA_Type.__name__=_C
_R2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA_Object=MibTableColumn
r2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA=_R2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,2375),_R2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA_Type())
r2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA.setStatus(_A)
class _R2ToneVariantsBwdGroupCSwitchGroupII_Type(Integer32):defaultValue=1600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600)));namedValues=NamedValues(*((_D,100),(_m,200),(_n,300),(_o,400),(_p,500),(_q,600),(_r,700),(_s,800),(_t,900),(_u,1000),(_v,1100),(_w,1200),(_x,1300),(_y,1400),(_z,1500),(_A0,1600)))
_R2ToneVariantsBwdGroupCSwitchGroupII_Type.__name__=_C
_R2ToneVariantsBwdGroupCSwitchGroupII_Object=MibTableColumn
r2ToneVariantsBwdGroupCSwitchGroupII=_R2ToneVariantsBwdGroupCSwitchGroupII_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,2380),_R2ToneVariantsBwdGroupCSwitchGroupII_Type())
r2ToneVariantsBwdGroupCSwitchGroupII.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsBwdGroupCSwitchGroupII.setStatus(_A)
class _R2ToneVariantsResetSpecific_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10)));namedValues=NamedValues(*((_A1,0),(_A2,10)))
_R2ToneVariantsResetSpecific_Type.__name__=_C
_R2ToneVariantsResetSpecific_Object=MibTableColumn
r2ToneVariantsResetSpecific=_R2ToneVariantsResetSpecific_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,100,600,1,2400),_R2ToneVariantsResetSpecific_Type())
r2ToneVariantsResetSpecific.setMaxAccess(_B)
if mibBuilder.loadTexts:r2ToneVariantsResetSpecific.setStatus(_A)
_BearerChannelGroup_ObjectIdentity=ObjectIdentity
bearerChannelGroup=_BearerChannelGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,200))
_BearerChannelInfoTable_Object=MibTable
bearerChannelInfoTable=_BearerChannelInfoTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,200,100))
if mibBuilder.loadTexts:bearerChannelInfoTable.setStatus(_A)
_BearerChannelInfoEntry_Object=MibTableRow
bearerChannelInfoEntry=_BearerChannelInfoEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,200,100,1))
bearerChannelInfoEntry.setIndexNames((0,_V,_A9))
if mibBuilder.loadTexts:bearerChannelInfoEntry.setStatus(_A)
_BearerChannelInfoIndex_Type=OctetString
_BearerChannelInfoIndex_Object=MibTableColumn
bearerChannelInfoIndex=_BearerChannelInfoIndex_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,200,100,1,100),_BearerChannelInfoIndex_Type())
bearerChannelInfoIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:bearerChannelInfoIndex.setStatus(_A)
class _BearerChannelInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400,500)));namedValues=NamedValues(*(('idle',100),('inUse',200),('maintenance',300),('error',400),('disabled',500)))
_BearerChannelInfoState_Type.__name__=_C
_BearerChannelInfoState_Object=MibTableColumn
bearerChannelInfoState=_BearerChannelInfoState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,200,100,1,200),_BearerChannelInfoState_Type())
bearerChannelInfoState.setMaxAccess(_E)
if mibBuilder.loadTexts:bearerChannelInfoState.setStatus(_A)
_PhysicalGroup_ObjectIdentity=ObjectIdentity
physicalGroup=_PhysicalGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,300))
_PhysicalLinkInfoTable_Object=MibTable
physicalLinkInfoTable=_PhysicalLinkInfoTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,300,100))
if mibBuilder.loadTexts:physicalLinkInfoTable.setStatus(_A)
_PhysicalLinkInfoEntry_Object=MibTableRow
physicalLinkInfoEntry=_PhysicalLinkInfoEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,300,100,1))
physicalLinkInfoEntry.setIndexNames((0,_V,_AA))
if mibBuilder.loadTexts:physicalLinkInfoEntry.setStatus(_A)
_PhysicalLinkInfoInterfaceName_Type=OctetString
_PhysicalLinkInfoInterfaceName_Object=MibTableColumn
physicalLinkInfoInterfaceName=_PhysicalLinkInfoInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,300,100,1,100),_PhysicalLinkInfoInterfaceName_Type())
physicalLinkInfoInterfaceName.setMaxAccess(_E)
if mibBuilder.loadTexts:physicalLinkInfoInterfaceName.setStatus(_A)
class _PhysicalLinkInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('up',100),('down',200)))
_PhysicalLinkInfoState_Type.__name__=_C
_PhysicalLinkInfoState_Object=MibTableColumn
physicalLinkInfoState=_PhysicalLinkInfoState_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,300,100,1,200),_PhysicalLinkInfoState_Type())
physicalLinkInfoState.setMaxAccess(_E)
if mibBuilder.loadTexts:physicalLinkInfoState.setStatus(_A)
_PhysicalLinkTable_Object=MibTable
physicalLinkTable=_PhysicalLinkTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,300,200))
if mibBuilder.loadTexts:physicalLinkTable.setStatus(_A)
_PhysicalLinkEntry_Object=MibTableRow
physicalLinkEntry=_PhysicalLinkEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,300,200,1))
physicalLinkEntry.setIndexNames((0,_V,_AB))
if mibBuilder.loadTexts:physicalLinkEntry.setStatus(_A)
_PhysicalLinkInterfaceName_Type=OctetString
_PhysicalLinkInterfaceName_Object=MibTableColumn
physicalLinkInterfaceName=_PhysicalLinkInterfaceName_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,300,200,1,100),_PhysicalLinkInterfaceName_Type())
physicalLinkInterfaceName.setMaxAccess(_E)
if mibBuilder.loadTexts:physicalLinkInterfaceName.setStatus(_A)
class _PhysicalLinkLineCoding_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('b8zs',100),('hdb3',200),('ami',300)))
_PhysicalLinkLineCoding_Type.__name__=_C
_PhysicalLinkLineCoding_Object=MibTableColumn
physicalLinkLineCoding=_PhysicalLinkLineCoding_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,300,200,1,200),_PhysicalLinkLineCoding_Type())
physicalLinkLineCoding.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalLinkLineCoding.setStatus(_A)
class _PhysicalLinkLineFraming_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*(('sf',100),('esf',200),('crc4',300),('noCrc4',400)))
_PhysicalLinkLineFraming_Type.__name__=_C
_PhysicalLinkLineFraming_Object=MibTableColumn
physicalLinkLineFraming=_PhysicalLinkLineFraming_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,300,200,1,300),_PhysicalLinkLineFraming_Type())
physicalLinkLineFraming.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalLinkLineFraming.setStatus(_A)
class _PhysicalLinkClockMode_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('master',100),('slave',200)))
_PhysicalLinkClockMode_Type.__name__=_C
_PhysicalLinkClockMode_Object=MibTableColumn
physicalLinkClockMode=_PhysicalLinkClockMode_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,300,200,1,400),_PhysicalLinkClockMode_Type())
physicalLinkClockMode.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalLinkClockMode.setStatus(_A)
class _PhysicalLinkMonitorLinkStateEnable_Type(MxEnableState):defaultValue=1
_PhysicalLinkMonitorLinkStateEnable_Type.__name__=_U
_PhysicalLinkMonitorLinkStateEnable_Object=MibTableColumn
physicalLinkMonitorLinkStateEnable=_PhysicalLinkMonitorLinkStateEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,300,200,1,500),_PhysicalLinkMonitorLinkStateEnable_Type())
physicalLinkMonitorLinkStateEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalLinkMonitorLinkStateEnable.setStatus(_A)
class _PhysicalLinkPortPinout_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300)));namedValues=NamedValues(*(('auto',100),('master',200),('slave',300)))
_PhysicalLinkPortPinout_Type.__name__=_C
_PhysicalLinkPortPinout_Object=MibTableColumn
physicalLinkPortPinout=_PhysicalLinkPortPinout_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,300,200,1,600),_PhysicalLinkPortPinout_Type())
physicalLinkPortPinout.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalLinkPortPinout.setStatus(_A)
_AutoConfigure_ObjectIdentity=ObjectIdentity
autoConfigure=_AutoConfigure_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,400))
class _AutoConfigureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('idle',100),('sensing',200)))
_AutoConfigureStatus_Type.__name__=_C
_AutoConfigureStatus_Object=MibScalar
autoConfigureStatus=_AutoConfigureStatus_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,400,100),_AutoConfigureStatus_Type())
autoConfigureStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:autoConfigureStatus.setStatus(_A)
class _LastAutoConfigureResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200,300,400)));namedValues=NamedValues(*((_D,100),('success',200),('fail',300),('aborted',400)))
_LastAutoConfigureResult_Type.__name__=_C
_LastAutoConfigureResult_Object=MibScalar
lastAutoConfigureResult=_LastAutoConfigureResult_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,400,200),_LastAutoConfigureResult_Type())
lastAutoConfigureResult.setMaxAccess(_E)
if mibBuilder.loadTexts:lastAutoConfigureResult.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*(('disable',0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_C
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_C
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,1875,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_E)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_V,**{'r2MIB':r2MIB,'r2MIBObjects':r2MIBObjects,'r2Group':r2Group,'r2Table':r2Table,'r2Entry':r2Entry,'r2Name':r2Name,'r2ChannelRange':r2ChannelRange,'r2ChannelAllocationStrategy':r2ChannelAllocationStrategy,'r2MaxActiveCalls':r2MaxActiveCalls,'r2EncodingScheme':r2EncodingScheme,'r2LineSignaling':r2LineSignaling,'r2IncomingDigitSignaling':r2IncomingDigitSignaling,'r2OutgoingDigitSignaling':r2OutgoingDigitSignaling,'r2CountrySelection':r2CountrySelection,'r2DigitAttenuation':r2DigitAttenuation,'r2SignalingVariantsTable':r2SignalingVariantsTable,'r2SignalingVariantsEntry':r2SignalingVariantsEntry,_A4:r2SignalingVariantsInterfaceName,'r2SignalingVariantsOverrideDefault':r2SignalingVariantsOverrideDefault,'r2SignalingVariantsBitsCD':r2SignalingVariantsBitsCD,'r2SignalingVariantsDnisLength':r2SignalingVariantsDnisLength,'r2SignalingVariantsAniLength':r2SignalingVariantsAniLength,'r2SignalingVariantsAniRequestEnable':r2SignalingVariantsAniRequestEnable,'r2SignalingVariantsSendAniRequestAfterDnisDigits':r2SignalingVariantsSendAniRequestAfterDnisDigits,'r2SignalingVariantsCollectCallBlocked':r2SignalingVariantsCollectCallBlocked,'r2SignalingVariantsAniCategory':r2SignalingVariantsAniCategory,'r2SignalingVariantsLineFreeCategory':r2SignalingVariantsLineFreeCategory,'r2SignalingVariantsAniRestrictedEnable':r2SignalingVariantsAniRestrictedEnable,'r2SignalingVariantsIncomingDeclineMethod':r2SignalingVariantsIncomingDeclineMethod,'r2SignalingVariantsResetSpecific':r2SignalingVariantsResetSpecific,'r2TimerVariantsTable':r2TimerVariantsTable,'r2TimerVariantsEntry':r2TimerVariantsEntry,_A5:r2TimerVariantsInterfaceName,'r2TimerVariantsOverrideDefault':r2TimerVariantsOverrideDefault,'r2TimerVariantsSeizureAckTimeout':r2TimerVariantsSeizureAckTimeout,'r2TimerVariantsFaultSeizureAckTimeout':r2TimerVariantsFaultSeizureAckTimeout,'r2TimerVariantsDoubleSeizureTimeout':r2TimerVariantsDoubleSeizureTimeout,'r2TimerVariantsDoubleAnswerTimeout':r2TimerVariantsDoubleAnswerTimeout,'r2TimerVariantsAnswerTimeout':r2TimerVariantsAnswerTimeout,'r2TimerVariantsReAnswerTimeout':r2TimerVariantsReAnswerTimeout,'r2TimerVariantsReleaseGuardTimeout':r2TimerVariantsReleaseGuardTimeout,'r2TimerVariantsInterCallGuardTimeout':r2TimerVariantsInterCallGuardTimeout,'r2TimerVariantsNoDigitTimeout':r2TimerVariantsNoDigitTimeout,'r2TimerVariantsCongestionToneGuardTimeout':r2TimerVariantsCongestionToneGuardTimeout,'r2TimerVariantsUnblockingTimeout':r2TimerVariantsUnblockingTimeout,'r2TimerVariantsAddressCompleteTimeout':r2TimerVariantsAddressCompleteTimeout,'r2TimerVariantsWaitAnswerTimeout':r2TimerVariantsWaitAnswerTimeout,'r2TimerVariantsDigitCompleteTimeout':r2TimerVariantsDigitCompleteTimeout,'r2TimerVariantsWaitGroupBResponseCompleteTimeout':r2TimerVariantsWaitGroupBResponseCompleteTimeout,'r2TimerVariantsWaitImmediateResponseCompleteTimeout':r2TimerVariantsWaitImmediateResponseCompleteTimeout,'r2TimerVariantsPlayToneGuardTimeout':r2TimerVariantsPlayToneGuardTimeout,'r2TimerVariantsAcceptCallTimeout':r2TimerVariantsAcceptCallTimeout,'r2TimerVariantsClearForwardGuardTimeout':r2TimerVariantsClearForwardGuardTimeout,'r2TimerVariantsClearBackwardGuardTimeout':r2TimerVariantsClearBackwardGuardTimeout,'r2TimerVariantsFaultOnAnsweredGuardTimeout':r2TimerVariantsFaultOnAnsweredGuardTimeout,'r2TimerVariantsFaultOnClearBackwardGuardTimeout':r2TimerVariantsFaultOnClearBackwardGuardTimeout,'r2TimerVariantsFaultOnSeizeAckGuardTimeout':r2TimerVariantsFaultOnSeizeAckGuardTimeout,'r2TimerVariantsFaultOnSeizeGuardTimeout':r2TimerVariantsFaultOnSeizeGuardTimeout,'r2TimerVariantsDeclineGuardTimeout':r2TimerVariantsDeclineGuardTimeout,'r2TimerVariantsResetSpecific':r2TimerVariantsResetSpecific,'r2DigitTimerVariantsTable':r2DigitTimerVariantsTable,'r2DigitTimerVariantsEntry':r2DigitTimerVariantsEntry,_A6:r2DigitTimerVariantsInterfaceName,'r2DigitTimerVariantsOverrideDefault':r2DigitTimerVariantsOverrideDefault,'r2DigitTimerVariantsMfCongestionToneDuration':r2DigitTimerVariantsMfCongestionToneDuration,'r2DigitTimerVariantsMfcPulseInterDigitTimeout':r2DigitTimerVariantsMfcPulseInterDigitTimeout,'r2DigitTimerVariantsMfcPulseMinOnTimeout':r2DigitTimerVariantsMfcPulseMinOnTimeout,'r2DigitTimerVariantsMfcMaxSequenceTimeout':r2DigitTimerVariantsMfcMaxSequenceTimeout,'r2DigitTimerVariantsMfcMaxOnTimeout':r2DigitTimerVariantsMfcMaxOnTimeout,'r2DigitTimerVariantsMfcMaxOffTimeout':r2DigitTimerVariantsMfcMaxOffTimeout,'r2DigitTimerVariantsResetSpecific':r2DigitTimerVariantsResetSpecific,'r2LinkTimerVariantsTable':r2LinkTimerVariantsTable,'r2LinkTimerVariantsEntry':r2LinkTimerVariantsEntry,_A7:r2LinkTimerVariantsInterfaceName,'r2LinkTimerVariantsOverrideDefault':r2LinkTimerVariantsOverrideDefault,'r2LinkTimerVariantsLinkActivationTimeout':r2LinkTimerVariantsLinkActivationTimeout,'r2LinkTimerVariantsLinkActivationRetryTimeout':r2LinkTimerVariantsLinkActivationRetryTimeout,'r2LinkTimerVariantsResetSpecific':r2LinkTimerVariantsResetSpecific,'r2ToneVariantsTable':r2ToneVariantsTable,'r2ToneVariantsEntry':r2ToneVariantsEntry,_A8:r2ToneVariantsInterfaceName,'r2ToneVariantsOverrideDefault':r2ToneVariantsOverrideDefault,'r2ToneVariantsFwdGroup1EndOfDnis':r2ToneVariantsFwdGroup1EndOfDnis,'r2ToneVariantsFwdGroup1EndOfAni':r2ToneVariantsFwdGroup1EndOfAni,'r2ToneVariantsFwdGroup1RestrictedAni':r2ToneVariantsFwdGroup1RestrictedAni,'r2ToneVariantsBwdGroupASendNextDnisDigit':r2ToneVariantsBwdGroupASendNextDnisDigit,'r2ToneVariantsBwdGroupASendPreviousDnisDigit':r2ToneVariantsBwdGroupASendPreviousDnisDigit,'r2ToneVariantsBwdGroupASwitchToGroupII':r2ToneVariantsBwdGroupASwitchToGroupII,'r2ToneVariantsBwdGroupANetworkCongestion':r2ToneVariantsBwdGroupANetworkCongestion,'r2ToneVariantsBwdGroupASendCallingPartyCategory':r2ToneVariantsBwdGroupASendCallingPartyCategory,'r2ToneVariantsBwdGroupAImmediateAccept':r2ToneVariantsBwdGroupAImmediateAccept,'r2ToneVariantsBwdGroupASendDnisDigitNMinus2':r2ToneVariantsBwdGroupASendDnisDigitNMinus2,'r2ToneVariantsBwdGroupASendDnisDigitNMinus3':r2ToneVariantsBwdGroupASendDnisDigitNMinus3,'r2ToneVariantsBwdGroupARepeatAllDnis':r2ToneVariantsBwdGroupARepeatAllDnis,'r2ToneVariantsBwdGroupASendNextAniDigit':r2ToneVariantsBwdGroupASendNextAniDigit,'r2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC':r2ToneVariantsBwdGroupASendCallingPartyCategorySwitchGroupC,'r2ToneVariantsBwdGroupBSendSit':r2ToneVariantsBwdGroupBSendSit,'r2ToneVariantsBwdGroupBUserBusy':r2ToneVariantsBwdGroupBUserBusy,'r2ToneVariantsBwdGroupBNetworkCongestion':r2ToneVariantsBwdGroupBNetworkCongestion,'r2ToneVariantsBwdGroupBUnassignedNumber':r2ToneVariantsBwdGroupBUnassignedNumber,'r2ToneVariantsBwdGroupBLineFreeCharge':r2ToneVariantsBwdGroupBLineFreeCharge,'r2ToneVariantsBwdGroupBSupplementaryLineFreeCharge':r2ToneVariantsBwdGroupBSupplementaryLineFreeCharge,'r2ToneVariantsBwdGroupBLineFreeNoCharge':r2ToneVariantsBwdGroupBLineFreeNoCharge,'r2ToneVariantsBwdGroupBLineOutOfOrder':r2ToneVariantsBwdGroupBLineOutOfOrder,'r2ToneVariantsBwdGroupBChangedNumber':r2ToneVariantsBwdGroupBChangedNumber,'r2ToneVariantsBwdGroupCSendNextAniDigit':r2ToneVariantsBwdGroupCSendNextAniDigit,'r2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA':r2ToneVariantsBwdGroupCRepeatAllDnisSwitchGroupA,'r2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA':r2ToneVariantsBwdGroupCSendNextDnisDigitSwitchGroupA,'r2ToneVariantsBwdGroupCNetworkCongestion':r2ToneVariantsBwdGroupCNetworkCongestion,'r2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA':r2ToneVariantsBwdGroupCSendPreviousDnisDigitSwitchGroupA,'r2ToneVariantsBwdGroupCSwitchGroupII':r2ToneVariantsBwdGroupCSwitchGroupII,'r2ToneVariantsResetSpecific':r2ToneVariantsResetSpecific,'bearerChannelGroup':bearerChannelGroup,'bearerChannelInfoTable':bearerChannelInfoTable,'bearerChannelInfoEntry':bearerChannelInfoEntry,_A9:bearerChannelInfoIndex,'bearerChannelInfoState':bearerChannelInfoState,'physicalGroup':physicalGroup,'physicalLinkInfoTable':physicalLinkInfoTable,'physicalLinkInfoEntry':physicalLinkInfoEntry,_AA:physicalLinkInfoInterfaceName,'physicalLinkInfoState':physicalLinkInfoState,'physicalLinkTable':physicalLinkTable,'physicalLinkEntry':physicalLinkEntry,_AB:physicalLinkInterfaceName,'physicalLinkLineCoding':physicalLinkLineCoding,'physicalLinkLineFraming':physicalLinkLineFraming,'physicalLinkClockMode':physicalLinkClockMode,'physicalLinkMonitorLinkStateEnable':physicalLinkMonitorLinkStateEnable,'physicalLinkPortPinout':physicalLinkPortPinout,'autoConfigure':autoConfigure,'autoConfigureStatus':autoConfigureStatus,'lastAutoConfigureResult':lastAutoConfigureResult,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})