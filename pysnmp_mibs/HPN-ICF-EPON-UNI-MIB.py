_e='hpnicfEponUniMultActAddress'
_d='hpnicfEponUniMultActVlan'
_c='hpnicfEponUniMirrorGroupID'
_b='hpnicfEponUniQosRuleIndex'
_a='preview'
_Z='permit'
_Y='hpnicfEponUniMulticastIndex'
_X='hpnicfEponUniMacIndex'
_W='notSupport'
_V='accessible-for-notify'
_U='TruthValue'
_T='hpnicfEponUniVlan'
_S='hpnicfEponUniAdminStatus'
_R='hpnicfEponUniQosConfIndex'
_Q='false'
_P='true'
_O='disable'
_N='enable'
_M='hpnicfEponUniDescr'
_L='ifDescr'
_K='not-accessible'
_J='OctetString'
_I='hpnicfEponUniIndex'
_H='ifIndex'
_G='read-create'
_F='IF-MIB'
_E='HPN-ICF-EPON-UNI-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfEpon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfEpon')
ifDescr,ifIndex=mibBuilder.importSymbols(_F,_L,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_U)
hpnicfEponUni=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,5))
_HpnicfEponUniSysMan_ObjectIdentity=ObjectIdentity
hpnicfEponUniSysMan=_HpnicfEponUniSysMan_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1))
_HpnicfEponUniSysManTable_Object=MibTable
hpnicfEponUniSysManTable=_HpnicfEponUniSysManTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1))
if mibBuilder.loadTexts:hpnicfEponUniSysManTable.setStatus(_A)
_HpnicfEponUniSysManEntry_Object=MibTableRow
hpnicfEponUniSysManEntry=_HpnicfEponUniSysManEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1))
hpnicfEponUniSysManEntry.setIndexNames((0,_F,_H),(0,_E,_I))
if mibBuilder.loadTexts:hpnicfEponUniSysManEntry.setStatus(_A)
_HpnicfEponUniIndex_Type=Integer32
_HpnicfEponUniIndex_Object=MibTableColumn
hpnicfEponUniIndex=_HpnicfEponUniIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,1),_HpnicfEponUniIndex_Type())
hpnicfEponUniIndex.setMaxAccess(_V)
if mibBuilder.loadTexts:hpnicfEponUniIndex.setStatus(_A)
_HpnicfEponUniDescr_Type=OctetString
_HpnicfEponUniDescr_Object=MibTableColumn
hpnicfEponUniDescr=_HpnicfEponUniDescr_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,2),_HpnicfEponUniDescr_Type())
hpnicfEponUniDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniDescr.setStatus(_A)
class _HpnicfEponUniAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_HpnicfEponUniAdminStatus_Type.__name__=_C
_HpnicfEponUniAdminStatus_Object=MibTableColumn
hpnicfEponUniAdminStatus=_HpnicfEponUniAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,3),_HpnicfEponUniAdminStatus_Type())
hpnicfEponUniAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniAdminStatus.setStatus(_A)
class _HpnicfEponUniMdi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mdi-ii',1),('mdi-x',2),('mdi-auto',3)))
_HpnicfEponUniMdi_Type.__name__=_C
_HpnicfEponUniMdi_Object=MibTableColumn
hpnicfEponUniMdi=_HpnicfEponUniMdi_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,4),_HpnicfEponUniMdi_Type())
hpnicfEponUniMdi.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniMdi.setStatus(_A)
class _HpnicfEponUniPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfEponUniPriority_Type.__name__=_C
_HpnicfEponUniPriority_Object=MibTableColumn
hpnicfEponUniPriority=_HpnicfEponUniPriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,5),_HpnicfEponUniPriority_Type())
hpnicfEponUniPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniPriority.setStatus(_A)
class _HpnicfEponUniVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('vlantrunk',1),('access',2),('hybrid',3),('untagged',4),('transparent',5),('doubletagged',6),('tag',7),('translation',8)))
_HpnicfEponUniVlanType_Type.__name__=_C
_HpnicfEponUniVlanType_Object=MibTableColumn
hpnicfEponUniVlanType=_HpnicfEponUniVlanType_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,6),_HpnicfEponUniVlanType_Type())
hpnicfEponUniVlanType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniVlanType.setStatus(_A)
class _HpnicfEponUniAccessVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfEponUniAccessVlan_Type.__name__=_C
_HpnicfEponUniAccessVlan_Object=MibTableColumn
hpnicfEponUniAccessVlan=_HpnicfEponUniAccessVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,7),_HpnicfEponUniAccessVlan_Type())
hpnicfEponUniAccessVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniAccessVlan.setStatus(_A)
class _HpnicfEponUniTrunkPvid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfEponUniTrunkPvid_Type.__name__=_C
_HpnicfEponUniTrunkPvid_Object=MibTableColumn
hpnicfEponUniTrunkPvid=_HpnicfEponUniTrunkPvid_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,8),_HpnicfEponUniTrunkPvid_Type())
hpnicfEponUniTrunkPvid.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniTrunkPvid.setStatus(_A)
_HpnicfEponUniVLANTrunkAllowListLow_Type=OctetString
_HpnicfEponUniVLANTrunkAllowListLow_Object=MibTableColumn
hpnicfEponUniVLANTrunkAllowListLow=_HpnicfEponUniVLANTrunkAllowListLow_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,9),_HpnicfEponUniVLANTrunkAllowListLow_Type())
hpnicfEponUniVLANTrunkAllowListLow.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniVLANTrunkAllowListLow.setStatus(_A)
_HpnicfEponUniVLANTrunkAllowListHigh_Type=OctetString
_HpnicfEponUniVLANTrunkAllowListHigh_Object=MibTableColumn
hpnicfEponUniVLANTrunkAllowListHigh=_HpnicfEponUniVLANTrunkAllowListHigh_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,10),_HpnicfEponUniVLANTrunkAllowListHigh_Type())
hpnicfEponUniVLANTrunkAllowListHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniVLANTrunkAllowListHigh.setStatus(_A)
_HpnicfEponUniInboundLineRate_Type=Integer32
_HpnicfEponUniInboundLineRate_Object=MibTableColumn
hpnicfEponUniInboundLineRate=_HpnicfEponUniInboundLineRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,11),_HpnicfEponUniInboundLineRate_Type())
hpnicfEponUniInboundLineRate.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniInboundLineRate.setStatus(_A)
_HpnicfEponUniOutboundLineRate_Type=Integer32
_HpnicfEponUniOutboundLineRate_Object=MibTableColumn
hpnicfEponUniOutboundLineRate=_HpnicfEponUniOutboundLineRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,12),_HpnicfEponUniOutboundLineRate_Type())
hpnicfEponUniOutboundLineRate.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniOutboundLineRate.setStatus(_A)
_HpnicfEponUniFlowControl_Type=TruthValue
_HpnicfEponUniFlowControl_Object=MibTableColumn
hpnicfEponUniFlowControl=_HpnicfEponUniFlowControl_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,13),_HpnicfEponUniFlowControl_Type())
hpnicfEponUniFlowControl.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniFlowControl.setStatus(_A)
class _HpnicfEponUniSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10,100,1000,10000,24000)));namedValues=NamedValues(*(('auto',0),('s10M',10),('s100M',100),('s1000M',1000),('s10000M',10000),('s24000M',24000)))
_HpnicfEponUniSpeed_Type.__name__=_C
_HpnicfEponUniSpeed_Object=MibTableColumn
hpnicfEponUniSpeed=_HpnicfEponUniSpeed_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,14),_HpnicfEponUniSpeed_Type())
hpnicfEponUniSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniSpeed.setStatus(_A)
class _HpnicfEponUniDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('full',1),('half',2),('auto',3)))
_HpnicfEponUniDuplex_Type.__name__=_C
_HpnicfEponUniDuplex_Object=MibTableColumn
hpnicfEponUniDuplex=_HpnicfEponUniDuplex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,15),_HpnicfEponUniDuplex_Type())
hpnicfEponUniDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniDuplex.setStatus(_A)
_HpnicfEponUniVlanVPNStatus_Type=TruthValue
_HpnicfEponUniVlanVPNStatus_Object=MibTableColumn
hpnicfEponUniVlanVPNStatus=_HpnicfEponUniVlanVPNStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,16),_HpnicfEponUniVlanVPNStatus_Type())
hpnicfEponUniVlanVPNStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniVlanVPNStatus.setStatus(_A)
class _HpnicfEponUniCountReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_HpnicfEponUniCountReset_Type.__name__=_C
_HpnicfEponUniCountReset_Object=MibTableColumn
hpnicfEponUniCountReset=_HpnicfEponUniCountReset_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,17),_HpnicfEponUniCountReset_Type())
hpnicfEponUniCountReset.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniCountReset.setStatus(_A)
class _HpnicfEponUniPortIsolate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_HpnicfEponUniPortIsolate_Type.__name__=_C
_HpnicfEponUniPortIsolate_Object=MibTableColumn
hpnicfEponUniPortIsolate=_HpnicfEponUniPortIsolate_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,18),_HpnicfEponUniPortIsolate_Type())
hpnicfEponUniPortIsolate.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniPortIsolate.setStatus(_A)
class _HpnicfEponUniVlanConfiguration_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfEponUniVlanConfiguration_Type.__name__=_J
_HpnicfEponUniVlanConfiguration_Object=MibTableColumn
hpnicfEponUniVlanConfiguration=_HpnicfEponUniVlanConfiguration_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,23),_HpnicfEponUniVlanConfiguration_Type())
hpnicfEponUniVlanConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniVlanConfiguration.setStatus(_A)
class _HpnicfEponUniAutoNegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_HpnicfEponUniAutoNegotiation_Type.__name__=_C
_HpnicfEponUniAutoNegotiation_Object=MibTableColumn
hpnicfEponUniAutoNegotiation=_HpnicfEponUniAutoNegotiation_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,25),_HpnicfEponUniAutoNegotiation_Type())
hpnicfEponUniAutoNegotiation.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniAutoNegotiation.setStatus(_A)
class _HpnicfEponUniRestartAutoNeg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('autoNegotiation',1))
_HpnicfEponUniRestartAutoNeg_Type.__name__=_C
_HpnicfEponUniRestartAutoNeg_Object=MibTableColumn
hpnicfEponUniRestartAutoNeg=_HpnicfEponUniRestartAutoNeg_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,26),_HpnicfEponUniRestartAutoNeg_Type())
hpnicfEponUniRestartAutoNeg.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniRestartAutoNeg.setStatus(_A)
class _HpnicfEponUniLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_HpnicfEponUniLinkStatus_Type.__name__=_C
_HpnicfEponUniLinkStatus_Object=MibTableColumn
hpnicfEponUniLinkStatus=_HpnicfEponUniLinkStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,29),_HpnicfEponUniLinkStatus_Type())
hpnicfEponUniLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniLinkStatus.setStatus(_A)
class _HpnicfEponUniInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('gigabitethernetport',1),('fastethernetport',2),('voipport',3),('e1port',4)))
_HpnicfEponUniInterfaceType_Type.__name__=_C
_HpnicfEponUniInterfaceType_Object=MibTableColumn
hpnicfEponUniInterfaceType=_HpnicfEponUniInterfaceType_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,30),_HpnicfEponUniInterfaceType_Type())
hpnicfEponUniInterfaceType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniInterfaceType.setStatus(_A)
class _HpnicfEponUniVitualCableTest_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_HpnicfEponUniVitualCableTest_Type.__name__=_C
_HpnicfEponUniVitualCableTest_Object=MibTableColumn
hpnicfEponUniVitualCableTest=_HpnicfEponUniVitualCableTest_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,31),_HpnicfEponUniVitualCableTest_Type())
hpnicfEponUniVitualCableTest.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniVitualCableTest.setStatus(_A)
class _HpnicfEponUniVCTCableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('normal',1),('abnormal',2),('abnormalOpen',3),('abnormalShort',4),('failure',5)))
_HpnicfEponUniVCTCableStatus_Type.__name__=_C
_HpnicfEponUniVCTCableStatus_Object=MibTableColumn
hpnicfEponUniVCTCableStatus=_HpnicfEponUniVCTCableStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,32),_HpnicfEponUniVCTCableStatus_Type())
hpnicfEponUniVCTCableStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniVCTCableStatus.setStatus(_A)
_HpnicfEponUniVCTCableLength_Type=Integer32
_HpnicfEponUniVCTCableLength_Object=MibTableColumn
hpnicfEponUniVCTCableLength=_HpnicfEponUniVCTCableLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,33),_HpnicfEponUniVCTCableLength_Type())
hpnicfEponUniVCTCableLength.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniVCTCableLength.setStatus(_A)
class _HpnicfEponUniVCTImpedanceMismatch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('not-support',1),(_P,2),(_Q,3)))
_HpnicfEponUniVCTImpedanceMismatch_Type.__name__=_C
_HpnicfEponUniVCTImpedanceMismatch_Object=MibTableColumn
hpnicfEponUniVCTImpedanceMismatch=_HpnicfEponUniVCTImpedanceMismatch_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,34),_HpnicfEponUniVCTImpedanceMismatch_Type())
hpnicfEponUniVCTImpedanceMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniVCTImpedanceMismatch.setStatus(_A)
_HpnicfEponUniVCTPairSkew_Type=Integer32
_HpnicfEponUniVCTPairSkew_Object=MibTableColumn
hpnicfEponUniVCTPairSkew=_HpnicfEponUniVCTPairSkew_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,35),_HpnicfEponUniVCTPairSkew_Type())
hpnicfEponUniVCTPairSkew.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniVCTPairSkew.setStatus(_A)
class _HpnicfEponUniVCTPairSwap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),(_P,2),(_Q,3)))
_HpnicfEponUniVCTPairSwap_Type.__name__=_C
_HpnicfEponUniVCTPairSwap_Object=MibTableColumn
hpnicfEponUniVCTPairSwap=_HpnicfEponUniVCTPairSwap_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,36),_HpnicfEponUniVCTPairSwap_Type())
hpnicfEponUniVCTPairSwap.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniVCTPairSwap.setStatus(_A)
class _HpnicfEponUniVCTPolaritySwap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),(_P,2),(_Q,3)))
_HpnicfEponUniVCTPolaritySwap_Type.__name__=_C
_HpnicfEponUniVCTPolaritySwap_Object=MibTableColumn
hpnicfEponUniVCTPolaritySwap=_HpnicfEponUniVCTPolaritySwap_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,37),_HpnicfEponUniVCTPolaritySwap_Type())
hpnicfEponUniVCTPolaritySwap.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniVCTPolaritySwap.setStatus(_A)
_HpnicfEponUniVCTInsertionLoss_Type=Integer32
_HpnicfEponUniVCTInsertionLoss_Object=MibTableColumn
hpnicfEponUniVCTInsertionLoss=_HpnicfEponUniVCTInsertionLoss_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,38),_HpnicfEponUniVCTInsertionLoss_Type())
hpnicfEponUniVCTInsertionLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniVCTInsertionLoss.setStatus(_A)
_HpnicfEponUniVCTReturnLoss_Type=Integer32
_HpnicfEponUniVCTReturnLoss_Object=MibTableColumn
hpnicfEponUniVCTReturnLoss=_HpnicfEponUniVCTReturnLoss_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,39),_HpnicfEponUniVCTReturnLoss_Type())
hpnicfEponUniVCTReturnLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniVCTReturnLoss.setStatus(_A)
_HpnicfEponUniVCTNearendCrosstalk_Type=Integer32
_HpnicfEponUniVCTNearendCrosstalk_Object=MibTableColumn
hpnicfEponUniVCTNearendCrosstalk=_HpnicfEponUniVCTNearendCrosstalk_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,40),_HpnicfEponUniVCTNearendCrosstalk_Type())
hpnicfEponUniVCTNearendCrosstalk.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniVCTNearendCrosstalk.setStatus(_A)
_HpnicfEponUniVlan_Type=Integer32
_HpnicfEponUniVlan_Object=MibTableColumn
hpnicfEponUniVlan=_HpnicfEponUniVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,1,1,41),_HpnicfEponUniVlan_Type())
hpnicfEponUniVlan.setMaxAccess(_V)
if mibBuilder.loadTexts:hpnicfEponUniVlan.setStatus(_A)
_HpnicfEponUniCountTable_Object=MibTable
hpnicfEponUniCountTable=_HpnicfEponUniCountTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2))
if mibBuilder.loadTexts:hpnicfEponUniCountTable.setStatus(_A)
_HpnicfEponUniCountEntry_Object=MibTableRow
hpnicfEponUniCountEntry=_HpnicfEponUniCountEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1))
hpnicfEponUniCountEntry.setIndexNames((0,_F,_H),(0,_E,_I))
if mibBuilder.loadTexts:hpnicfEponUniCountEntry.setStatus(_A)
_HpnicfEponUniInStatsPkts_Type=Unsigned32
_HpnicfEponUniInStatsPkts_Object=MibTableColumn
hpnicfEponUniInStatsPkts=_HpnicfEponUniInStatsPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1,1),_HpnicfEponUniInStatsPkts_Type())
hpnicfEponUniInStatsPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniInStatsPkts.setStatus(_A)
_HpnicfEponUniInStatsUnicastPkts_Type=Unsigned32
_HpnicfEponUniInStatsUnicastPkts_Object=MibTableColumn
hpnicfEponUniInStatsUnicastPkts=_HpnicfEponUniInStatsUnicastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1,2),_HpnicfEponUniInStatsUnicastPkts_Type())
hpnicfEponUniInStatsUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniInStatsUnicastPkts.setStatus(_A)
_HpnicfEponUniInStatsBroadcastPkts_Type=Unsigned32
_HpnicfEponUniInStatsBroadcastPkts_Object=MibTableColumn
hpnicfEponUniInStatsBroadcastPkts=_HpnicfEponUniInStatsBroadcastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1,3),_HpnicfEponUniInStatsBroadcastPkts_Type())
hpnicfEponUniInStatsBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniInStatsBroadcastPkts.setStatus(_A)
_HpnicfEponUniInStatsMulticastPkts_Type=Unsigned32
_HpnicfEponUniInStatsMulticastPkts_Object=MibTableColumn
hpnicfEponUniInStatsMulticastPkts=_HpnicfEponUniInStatsMulticastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1,4),_HpnicfEponUniInStatsMulticastPkts_Type())
hpnicfEponUniInStatsMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniInStatsMulticastPkts.setStatus(_A)
_HpnicfEponUniInPausePkts_Type=Unsigned32
_HpnicfEponUniInPausePkts_Object=MibTableColumn
hpnicfEponUniInPausePkts=_HpnicfEponUniInPausePkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1,5),_HpnicfEponUniInPausePkts_Type())
hpnicfEponUniInPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniInPausePkts.setStatus(_A)
_HpnicfEponUniInTotalErrors_Type=Unsigned32
_HpnicfEponUniInTotalErrors_Object=MibTableColumn
hpnicfEponUniInTotalErrors=_HpnicfEponUniInTotalErrors_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1,6),_HpnicfEponUniInTotalErrors_Type())
hpnicfEponUniInTotalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniInTotalErrors.setStatus(_A)
_HpnicfEponUniInStatsCRCAlignErrors_Type=Unsigned32
_HpnicfEponUniInStatsCRCAlignErrors_Object=MibTableColumn
hpnicfEponUniInStatsCRCAlignErrors=_HpnicfEponUniInStatsCRCAlignErrors_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1,7),_HpnicfEponUniInStatsCRCAlignErrors_Type())
hpnicfEponUniInStatsCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniInStatsCRCAlignErrors.setStatus(_A)
_HpnicfEponUniInStatsUndersizePkts_Type=Unsigned32
_HpnicfEponUniInStatsUndersizePkts_Object=MibTableColumn
hpnicfEponUniInStatsUndersizePkts=_HpnicfEponUniInStatsUndersizePkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1,8),_HpnicfEponUniInStatsUndersizePkts_Type())
hpnicfEponUniInStatsUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniInStatsUndersizePkts.setStatus(_A)
_HpnicfEponUniInStatsOversizePkts_Type=Unsigned32
_HpnicfEponUniInStatsOversizePkts_Object=MibTableColumn
hpnicfEponUniInStatsOversizePkts=_HpnicfEponUniInStatsOversizePkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1,9),_HpnicfEponUniInStatsOversizePkts_Type())
hpnicfEponUniInStatsOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniInStatsOversizePkts.setStatus(_A)
_HpnicfEponUniInErrorbyOther_Type=Unsigned32
_HpnicfEponUniInErrorbyOther_Object=MibTableColumn
hpnicfEponUniInErrorbyOther=_HpnicfEponUniInErrorbyOther_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1,10),_HpnicfEponUniInErrorbyOther_Type())
hpnicfEponUniInErrorbyOther.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniInErrorbyOther.setStatus(_A)
_HpnicfEponUniOutStatsPkts_Type=Unsigned32
_HpnicfEponUniOutStatsPkts_Object=MibTableColumn
hpnicfEponUniOutStatsPkts=_HpnicfEponUniOutStatsPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1,11),_HpnicfEponUniOutStatsPkts_Type())
hpnicfEponUniOutStatsPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniOutStatsPkts.setStatus(_A)
_HpnicfEponUniOutStatsUnicastPkts_Type=Unsigned32
_HpnicfEponUniOutStatsUnicastPkts_Object=MibTableColumn
hpnicfEponUniOutStatsUnicastPkts=_HpnicfEponUniOutStatsUnicastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1,12),_HpnicfEponUniOutStatsUnicastPkts_Type())
hpnicfEponUniOutStatsUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniOutStatsUnicastPkts.setStatus(_A)
_HpnicfEponUniOutStatsBroadcastPkts_Type=Unsigned32
_HpnicfEponUniOutStatsBroadcastPkts_Object=MibTableColumn
hpnicfEponUniOutStatsBroadcastPkts=_HpnicfEponUniOutStatsBroadcastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1,13),_HpnicfEponUniOutStatsBroadcastPkts_Type())
hpnicfEponUniOutStatsBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniOutStatsBroadcastPkts.setStatus(_A)
_HpnicfEponUniOutStatsMulticastPkts_Type=Unsigned32
_HpnicfEponUniOutStatsMulticastPkts_Object=MibTableColumn
hpnicfEponUniOutStatsMulticastPkts=_HpnicfEponUniOutStatsMulticastPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1,14),_HpnicfEponUniOutStatsMulticastPkts_Type())
hpnicfEponUniOutStatsMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniOutStatsMulticastPkts.setStatus(_A)
_HpnicfEponUniOutStatsPausePkts_Type=Unsigned32
_HpnicfEponUniOutStatsPausePkts_Object=MibTableColumn
hpnicfEponUniOutStatsPausePkts=_HpnicfEponUniOutStatsPausePkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1,15),_HpnicfEponUniOutStatsPausePkts_Type())
hpnicfEponUniOutStatsPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniOutStatsPausePkts.setStatus(_A)
_HpnicfEponUniOutTotalErrors_Type=Unsigned32
_HpnicfEponUniOutTotalErrors_Object=MibTableColumn
hpnicfEponUniOutTotalErrors=_HpnicfEponUniOutTotalErrors_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1,16),_HpnicfEponUniOutTotalErrors_Type())
hpnicfEponUniOutTotalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniOutTotalErrors.setStatus(_A)
_HpnicfEponUniOutStatsCollisions_Type=Unsigned32
_HpnicfEponUniOutStatsCollisions_Object=MibTableColumn
hpnicfEponUniOutStatsCollisions=_HpnicfEponUniOutStatsCollisions_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1,17),_HpnicfEponUniOutStatsCollisions_Type())
hpnicfEponUniOutStatsCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniOutStatsCollisions.setStatus(_A)
_HpnicfEponUniOutDelayExceededDiscards_Type=Unsigned32
_HpnicfEponUniOutDelayExceededDiscards_Object=MibTableColumn
hpnicfEponUniOutDelayExceededDiscards=_HpnicfEponUniOutDelayExceededDiscards_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1,18),_HpnicfEponUniOutDelayExceededDiscards_Type())
hpnicfEponUniOutDelayExceededDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniOutDelayExceededDiscards.setStatus(_A)
_HpnicfEponUniOutErrorbyOther_Type=Unsigned32
_HpnicfEponUniOutErrorbyOther_Object=MibTableColumn
hpnicfEponUniOutErrorbyOther=_HpnicfEponUniOutErrorbyOther_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1,19),_HpnicfEponUniOutErrorbyOther_Type())
hpnicfEponUniOutErrorbyOther.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniOutErrorbyOther.setStatus(_A)
_HpnicfEponUniOutDroppedFrames_Type=Unsigned32
_HpnicfEponUniOutDroppedFrames_Object=MibTableColumn
hpnicfEponUniOutDroppedFrames=_HpnicfEponUniOutDroppedFrames_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,2,1,20),_HpnicfEponUniOutDroppedFrames_Type())
hpnicfEponUniOutDroppedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniOutDroppedFrames.setStatus(_A)
_HpnicfEponUniIgmpInfoTable_Object=MibTable
hpnicfEponUniIgmpInfoTable=_HpnicfEponUniIgmpInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,3))
if mibBuilder.loadTexts:hpnicfEponUniIgmpInfoTable.setStatus(_A)
_HpnicfEponUniIgmpInfoEntry_Object=MibTableRow
hpnicfEponUniIgmpInfoEntry=_HpnicfEponUniIgmpInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,3,1))
hpnicfEponUniIgmpInfoEntry.setIndexNames((0,_F,_H),(0,_E,_I),(0,_E,_X))
if mibBuilder.loadTexts:hpnicfEponUniIgmpInfoEntry.setStatus(_A)
_HpnicfEponUniMacIndex_Type=Integer32
_HpnicfEponUniMacIndex_Object=MibTableColumn
hpnicfEponUniMacIndex=_HpnicfEponUniMacIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,3,1,1),_HpnicfEponUniMacIndex_Type())
hpnicfEponUniMacIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfEponUniMacIndex.setStatus(_A)
_HpnicfEponUniIgmpMacAddress_Type=MacAddress
_HpnicfEponUniIgmpMacAddress_Object=MibTableColumn
hpnicfEponUniIgmpMacAddress=_HpnicfEponUniIgmpMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,3,1,2),_HpnicfEponUniIgmpMacAddress_Type())
hpnicfEponUniIgmpMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniIgmpMacAddress.setStatus(_A)
class _HpnicfEponUniIgmpVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfEponUniIgmpVlanId_Type.__name__=_C
_HpnicfEponUniIgmpVlanId_Object=MibTableColumn
hpnicfEponUniIgmpVlanId=_HpnicfEponUniIgmpVlanId_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,3,1,3),_HpnicfEponUniIgmpVlanId_Type())
hpnicfEponUniIgmpVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniIgmpVlanId.setStatus(_A)
_HpnicfEponUniParaMan_ObjectIdentity=ObjectIdentity
hpnicfEponUniParaMan=_HpnicfEponUniParaMan_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,4))
_HpnicfEponUniLineRateMax_Type=Integer32
_HpnicfEponUniLineRateMax_Object=MibScalar
hpnicfEponUniLineRateMax=_HpnicfEponUniLineRateMax_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,4,1),_HpnicfEponUniLineRateMax_Type())
hpnicfEponUniLineRateMax.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniLineRateMax.setStatus(_A)
_HpnicfEponUniLineRateStep_Type=Integer32
_HpnicfEponUniLineRateStep_Object=MibScalar
hpnicfEponUniLineRateStep=_HpnicfEponUniLineRateStep_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,4,2),_HpnicfEponUniLineRateStep_Type())
hpnicfEponUniLineRateStep.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniLineRateStep.setStatus(_A)
_HpnicfEponUniNumberOnOnu_Type=Integer32
_HpnicfEponUniNumberOnOnu_Object=MibScalar
hpnicfEponUniNumberOnOnu=_HpnicfEponUniNumberOnOnu_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,4,3),_HpnicfEponUniNumberOnOnu_Type())
hpnicfEponUniNumberOnOnu.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniNumberOnOnu.setStatus(_A)
_HpnicfEponUniScalarGroup_ObjectIdentity=ObjectIdentity
hpnicfEponUniScalarGroup=_HpnicfEponUniScalarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,5))
_HpnicfEponUniPortPolicyTable_Object=MibTable
hpnicfEponUniPortPolicyTable=_HpnicfEponUniPortPolicyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,6))
if mibBuilder.loadTexts:hpnicfEponUniPortPolicyTable.setStatus(_A)
_HpnicfEponUniPortPolicyEntry_Object=MibTableRow
hpnicfEponUniPortPolicyEntry=_HpnicfEponUniPortPolicyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,6,1))
hpnicfEponUniPortPolicyEntry.setIndexNames((0,_F,_H),(0,_E,_I))
if mibBuilder.loadTexts:hpnicfEponUniPortPolicyEntry.setStatus(_A)
class _HpnicfEponUniPortPolicyStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_HpnicfEponUniPortPolicyStatus_Type.__name__=_C
_HpnicfEponUniPortPolicyStatus_Object=MibTableColumn
hpnicfEponUniPortPolicyStatus=_HpnicfEponUniPortPolicyStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,6,1,1),_HpnicfEponUniPortPolicyStatus_Type())
hpnicfEponUniPortPolicyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniPortPolicyStatus.setStatus(_A)
class _HpnicfEponUniPortPolicyCir_Type(Integer32):defaultValue=102400
_HpnicfEponUniPortPolicyCir_Type.__name__=_C
_HpnicfEponUniPortPolicyCir_Object=MibTableColumn
hpnicfEponUniPortPolicyCir=_HpnicfEponUniPortPolicyCir_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,6,1,2),_HpnicfEponUniPortPolicyCir_Type())
hpnicfEponUniPortPolicyCir.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniPortPolicyCir.setStatus(_A)
class _HpnicfEponUniPortPolicyBucketDepth_Type(Integer32):defaultValue=0
_HpnicfEponUniPortPolicyBucketDepth_Type.__name__=_C
_HpnicfEponUniPortPolicyBucketDepth_Object=MibTableColumn
hpnicfEponUniPortPolicyBucketDepth=_HpnicfEponUniPortPolicyBucketDepth_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,6,1,3),_HpnicfEponUniPortPolicyBucketDepth_Type())
hpnicfEponUniPortPolicyBucketDepth.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniPortPolicyBucketDepth.setStatus(_A)
class _HpnicfEponUniPortPolicyExtraBurst_Type(Integer32):defaultValue=0
_HpnicfEponUniPortPolicyExtraBurst_Type.__name__=_C
_HpnicfEponUniPortPolicyExtraBurst_Object=MibTableColumn
hpnicfEponUniPortPolicyExtraBurst=_HpnicfEponUniPortPolicyExtraBurst_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,6,1,4),_HpnicfEponUniPortPolicyExtraBurst_Type())
hpnicfEponUniPortPolicyExtraBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniPortPolicyExtraBurst.setStatus(_A)
_HpnicfEponUniPortPolicyInboundCir_Type=Integer32
_HpnicfEponUniPortPolicyInboundCir_Object=MibTableColumn
hpnicfEponUniPortPolicyInboundCir=_HpnicfEponUniPortPolicyInboundCir_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,6,1,5),_HpnicfEponUniPortPolicyInboundCir_Type())
hpnicfEponUniPortPolicyInboundCir.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniPortPolicyInboundCir.setStatus(_A)
class _HpnicfEponUniPortPolicyInboundBucketDepth_Type(Integer32):defaultValue=0
_HpnicfEponUniPortPolicyInboundBucketDepth_Type.__name__=_C
_HpnicfEponUniPortPolicyInboundBucketDepth_Object=MibTableColumn
hpnicfEponUniPortPolicyInboundBucketDepth=_HpnicfEponUniPortPolicyInboundBucketDepth_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,6,1,6),_HpnicfEponUniPortPolicyInboundBucketDepth_Type())
hpnicfEponUniPortPolicyInboundBucketDepth.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniPortPolicyInboundBucketDepth.setStatus(_A)
class _HpnicfEponUniPortPolicyInboundExtraBurst_Type(Integer32):defaultValue=0
_HpnicfEponUniPortPolicyInboundExtraBurst_Type.__name__=_C
_HpnicfEponUniPortPolicyInboundExtraBurst_Object=MibTableColumn
hpnicfEponUniPortPolicyInboundExtraBurst=_HpnicfEponUniPortPolicyInboundExtraBurst_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,6,1,7),_HpnicfEponUniPortPolicyInboundExtraBurst_Type())
hpnicfEponUniPortPolicyInboundExtraBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniPortPolicyInboundExtraBurst.setStatus(_A)
_HpnicfEponUniPortPolicyOutboundCir_Type=Integer32
_HpnicfEponUniPortPolicyOutboundCir_Object=MibTableColumn
hpnicfEponUniPortPolicyOutboundCir=_HpnicfEponUniPortPolicyOutboundCir_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,6,1,8),_HpnicfEponUniPortPolicyOutboundCir_Type())
hpnicfEponUniPortPolicyOutboundCir.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniPortPolicyOutboundCir.setStatus(_A)
_HpnicfEponUniPortPolicyOutboundPir_Type=Integer32
_HpnicfEponUniPortPolicyOutboundPir_Object=MibTableColumn
hpnicfEponUniPortPolicyOutboundPir=_HpnicfEponUniPortPolicyOutboundPir_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,6,1,9),_HpnicfEponUniPortPolicyOutboundPir_Type())
hpnicfEponUniPortPolicyOutboundPir.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniPortPolicyOutboundPir.setStatus(_A)
_HpnicfEponUniMulticastTable_Object=MibTable
hpnicfEponUniMulticastTable=_HpnicfEponUniMulticastTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,7))
if mibBuilder.loadTexts:hpnicfEponUniMulticastTable.setStatus(_A)
_HpnicfEponUniMulticastEntry_Object=MibTableRow
hpnicfEponUniMulticastEntry=_HpnicfEponUniMulticastEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,7,1))
hpnicfEponUniMulticastEntry.setIndexNames((0,_F,_H),(0,_E,_I))
if mibBuilder.loadTexts:hpnicfEponUniMulticastEntry.setStatus(_A)
class _HpnicfEponUniMulticastGroupNumber_Type(Integer32):defaultValue=64
_HpnicfEponUniMulticastGroupNumber_Type.__name__=_C
_HpnicfEponUniMulticastGroupNumber_Object=MibTableColumn
hpnicfEponUniMulticastGroupNumber=_HpnicfEponUniMulticastGroupNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,7,1,1),_HpnicfEponUniMulticastGroupNumber_Type())
hpnicfEponUniMulticastGroupNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniMulticastGroupNumber.setStatus(_A)
class _HpnicfEponUniMulticastVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfEponUniMulticastVlanList_Type.__name__=_J
_HpnicfEponUniMulticastVlanList_Object=MibTableColumn
hpnicfEponUniMulticastVlanList=_HpnicfEponUniMulticastVlanList_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,7,1,2),_HpnicfEponUniMulticastVlanList_Type())
hpnicfEponUniMulticastVlanList.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniMulticastVlanList.setStatus(_A)
class _HpnicfEponUniMulticastStripStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_HpnicfEponUniMulticastStripStatus_Type.__name__=_C
_HpnicfEponUniMulticastStripStatus_Object=MibTableColumn
hpnicfEponUniMulticastStripStatus=_HpnicfEponUniMulticastStripStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,7,1,3),_HpnicfEponUniMulticastStripStatus_Type())
hpnicfEponUniMulticastStripStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniMulticastStripStatus.setStatus(_A)
class _HpnicfEponUniMulticastFastleave_Type(TruthValue):defaultValue=2
_HpnicfEponUniMulticastFastleave_Type.__name__=_U
_HpnicfEponUniMulticastFastleave_Object=MibTableColumn
hpnicfEponUniMulticastFastleave=_HpnicfEponUniMulticastFastleave_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,7,1,4),_HpnicfEponUniMulticastFastleave_Type())
hpnicfEponUniMulticastFastleave.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniMulticastFastleave.setStatus(_A)
_HpnicfEponUniTechAbilityTable_Object=MibTable
hpnicfEponUniTechAbilityTable=_HpnicfEponUniTechAbilityTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,8))
if mibBuilder.loadTexts:hpnicfEponUniTechAbilityTable.setStatus(_A)
_HpnicfEponUniTechAbilityEntry_Object=MibTableRow
hpnicfEponUniTechAbilityEntry=_HpnicfEponUniTechAbilityEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,8,1))
hpnicfEponUniTechAbilityEntry.setIndexNames((0,_F,_H),(0,_E,_I))
if mibBuilder.loadTexts:hpnicfEponUniTechAbilityEntry.setStatus(_A)
class _HpnicfEponUniLocalTechAbility_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfEponUniLocalTechAbility_Type.__name__=_J
_HpnicfEponUniLocalTechAbility_Object=MibTableColumn
hpnicfEponUniLocalTechAbility=_HpnicfEponUniLocalTechAbility_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,8,1,1),_HpnicfEponUniLocalTechAbility_Type())
hpnicfEponUniLocalTechAbility.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniLocalTechAbility.setStatus(_A)
class _HpnicfEponUniAdvertisedTechAbility_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfEponUniAdvertisedTechAbility_Type.__name__=_J
_HpnicfEponUniAdvertisedTechAbility_Object=MibTableColumn
hpnicfEponUniAdvertisedTechAbility=_HpnicfEponUniAdvertisedTechAbility_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,8,1,2),_HpnicfEponUniAdvertisedTechAbility_Type())
hpnicfEponUniAdvertisedTechAbility.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniAdvertisedTechAbility.setStatus(_A)
_HpnicfEponUniMulticastControlTable_Object=MibTable
hpnicfEponUniMulticastControlTable=_HpnicfEponUniMulticastControlTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,9))
if mibBuilder.loadTexts:hpnicfEponUniMulticastControlTable.setStatus(_A)
_HpnicfEponUniMulticastControlEntry_Object=MibTableRow
hpnicfEponUniMulticastControlEntry=_HpnicfEponUniMulticastControlEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,9,1))
hpnicfEponUniMulticastControlEntry.setIndexNames((0,_F,_H),(0,_E,_I),(0,_E,_Y))
if mibBuilder.loadTexts:hpnicfEponUniMulticastControlEntry.setStatus(_A)
_HpnicfEponUniMulticastVlanIndex_Type=Integer32
_HpnicfEponUniMulticastVlanIndex_Object=MibTableColumn
hpnicfEponUniMulticastVlanIndex=_HpnicfEponUniMulticastVlanIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,9,1,1),_HpnicfEponUniMulticastVlanIndex_Type())
hpnicfEponUniMulticastVlanIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniMulticastVlanIndex.setStatus(_A)
class _HpnicfEponUniMulticastAddressList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfEponUniMulticastAddressList_Type.__name__=_J
_HpnicfEponUniMulticastAddressList_Object=MibTableColumn
hpnicfEponUniMulticastAddressList=_HpnicfEponUniMulticastAddressList_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,9,1,2),_HpnicfEponUniMulticastAddressList_Type())
hpnicfEponUniMulticastAddressList.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniMulticastAddressList.setStatus(_A)
class _HpnicfEponUniMulticastAccessRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('deny',1),(_Z,2),(_a,3)))
_HpnicfEponUniMulticastAccessRule_Type.__name__=_C
_HpnicfEponUniMulticastAccessRule_Object=MibTableColumn
hpnicfEponUniMulticastAccessRule=_HpnicfEponUniMulticastAccessRule_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,9,1,3),_HpnicfEponUniMulticastAccessRule_Type())
hpnicfEponUniMulticastAccessRule.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniMulticastAccessRule.setStatus(_A)
_HpnicfEponUniMulticastChannelLimit_Type=Integer32
_HpnicfEponUniMulticastChannelLimit_Object=MibTableColumn
hpnicfEponUniMulticastChannelLimit=_HpnicfEponUniMulticastChannelLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,9,1,4),_HpnicfEponUniMulticastChannelLimit_Type())
hpnicfEponUniMulticastChannelLimit.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniMulticastChannelLimit.setStatus(_A)
_HpnicfEponUniMulticastPreTimeSlice_Type=Integer32
_HpnicfEponUniMulticastPreTimeSlice_Object=MibTableColumn
hpnicfEponUniMulticastPreTimeSlice=_HpnicfEponUniMulticastPreTimeSlice_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,9,1,5),_HpnicfEponUniMulticastPreTimeSlice_Type())
hpnicfEponUniMulticastPreTimeSlice.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniMulticastPreTimeSlice.setStatus(_A)
_HpnicfEponUniMulticastPreTimes_Type=Integer32
_HpnicfEponUniMulticastPreTimes_Object=MibTableColumn
hpnicfEponUniMulticastPreTimes=_HpnicfEponUniMulticastPreTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,9,1,6),_HpnicfEponUniMulticastPreTimes_Type())
hpnicfEponUniMulticastPreTimes.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniMulticastPreTimes.setStatus(_A)
_HpnicfEponUniMulticastPreInterval_Type=Integer32
_HpnicfEponUniMulticastPreInterval_Object=MibTableColumn
hpnicfEponUniMulticastPreInterval=_HpnicfEponUniMulticastPreInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,9,1,7),_HpnicfEponUniMulticastPreInterval_Type())
hpnicfEponUniMulticastPreInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniMulticastPreInterval.setStatus(_A)
_HpnicfEponUniMulticastRowStatus_Type=RowStatus
_HpnicfEponUniMulticastRowStatus_Object=MibTableColumn
hpnicfEponUniMulticastRowStatus=_HpnicfEponUniMulticastRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,9,1,8),_HpnicfEponUniMulticastRowStatus_Type())
hpnicfEponUniMulticastRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniMulticastRowStatus.setStatus(_A)
_HpnicfEponUniMulticastIndex_Type=Integer32
_HpnicfEponUniMulticastIndex_Object=MibTableColumn
hpnicfEponUniMulticastIndex=_HpnicfEponUniMulticastIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,9,1,9),_HpnicfEponUniMulticastIndex_Type())
hpnicfEponUniMulticastIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfEponUniMulticastIndex.setStatus(_A)
class _HpnicfEponUniMulticastSourceIpList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfEponUniMulticastSourceIpList_Type.__name__=_J
_HpnicfEponUniMulticastSourceIpList_Object=MibTableColumn
hpnicfEponUniMulticastSourceIpList=_HpnicfEponUniMulticastSourceIpList_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,9,1,10),_HpnicfEponUniMulticastSourceIpList_Type())
hpnicfEponUniMulticastSourceIpList.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniMulticastSourceIpList.setStatus(_A)
_HpnicfEponUniMulticastResetInterval_Type=Integer32
_HpnicfEponUniMulticastResetInterval_Object=MibTableColumn
hpnicfEponUniMulticastResetInterval=_HpnicfEponUniMulticastResetInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,9,1,11),_HpnicfEponUniMulticastResetInterval_Type())
hpnicfEponUniMulticastResetInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniMulticastResetInterval.setStatus(_A)
_HpnicfEponUniQosIndexNextTable_Object=MibTable
hpnicfEponUniQosIndexNextTable=_HpnicfEponUniQosIndexNextTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,10))
if mibBuilder.loadTexts:hpnicfEponUniQosIndexNextTable.setStatus(_A)
_HpnicfEponUniQosIndexNextEntry_Object=MibTableRow
hpnicfEponUniQosIndexNextEntry=_HpnicfEponUniQosIndexNextEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,10,1))
hpnicfEponUniQosIndexNextEntry.setIndexNames((0,_F,_H),(0,_E,_I))
if mibBuilder.loadTexts:hpnicfEponUniQosIndexNextEntry.setStatus(_A)
_HpnicfEponUniQosConfIndexNext_Type=Integer32
_HpnicfEponUniQosConfIndexNext_Object=MibTableColumn
hpnicfEponUniQosConfIndexNext=_HpnicfEponUniQosConfIndexNext_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,10,1,1),_HpnicfEponUniQosConfIndexNext_Type())
hpnicfEponUniQosConfIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniQosConfIndexNext.setStatus(_A)
_HpnicfEponUniQosConfTable_Object=MibTable
hpnicfEponUniQosConfTable=_HpnicfEponUniQosConfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,11))
if mibBuilder.loadTexts:hpnicfEponUniQosConfTable.setStatus(_A)
_HpnicfEponUniQosConfEntry_Object=MibTableRow
hpnicfEponUniQosConfEntry=_HpnicfEponUniQosConfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,11,1))
hpnicfEponUniQosConfEntry.setIndexNames((0,_F,_H),(0,_E,_I),(0,_E,_R))
if mibBuilder.loadTexts:hpnicfEponUniQosConfEntry.setStatus(_A)
_HpnicfEponUniQosConfIndex_Type=Integer32
_HpnicfEponUniQosConfIndex_Object=MibTableColumn
hpnicfEponUniQosConfIndex=_HpnicfEponUniQosConfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,11,1,1),_HpnicfEponUniQosConfIndex_Type())
hpnicfEponUniQosConfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfEponUniQosConfIndex.setStatus(_A)
_HpnicfEponUniQosConfRuleIndexNext_Type=Integer32
_HpnicfEponUniQosConfRuleIndexNext_Object=MibTableColumn
hpnicfEponUniQosConfRuleIndexNext=_HpnicfEponUniQosConfRuleIndexNext_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,11,1,2),_HpnicfEponUniQosConfRuleIndexNext_Type())
hpnicfEponUniQosConfRuleIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniQosConfRuleIndexNext.setStatus(_A)
_HpnicfEponUniQosConfMappedQueue_Type=Integer32
_HpnicfEponUniQosConfMappedQueue_Object=MibTableColumn
hpnicfEponUniQosConfMappedQueue=_HpnicfEponUniQosConfMappedQueue_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,11,1,3),_HpnicfEponUniQosConfMappedQueue_Type())
hpnicfEponUniQosConfMappedQueue.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniQosConfMappedQueue.setStatus(_A)
_HpnicfEponUniQosConfMarkedPriority_Type=Integer32
_HpnicfEponUniQosConfMarkedPriority_Object=MibTableColumn
hpnicfEponUniQosConfMarkedPriority=_HpnicfEponUniQosConfMarkedPriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,11,1,4),_HpnicfEponUniQosConfMarkedPriority_Type())
hpnicfEponUniQosConfMarkedPriority.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniQosConfMarkedPriority.setStatus(_A)
_HpnicfEponUniQosConfRowStatus_Type=RowStatus
_HpnicfEponUniQosConfRowStatus_Object=MibTableColumn
hpnicfEponUniQosConfRowStatus=_HpnicfEponUniQosConfRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,11,1,5),_HpnicfEponUniQosConfRowStatus_Type())
hpnicfEponUniQosConfRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniQosConfRowStatus.setStatus(_A)
_HpnicfEponUniQosRuleTable_Object=MibTable
hpnicfEponUniQosRuleTable=_HpnicfEponUniQosRuleTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,12))
if mibBuilder.loadTexts:hpnicfEponUniQosRuleTable.setStatus(_A)
_HpnicfEponUniQosRuleEntry_Object=MibTableRow
hpnicfEponUniQosRuleEntry=_HpnicfEponUniQosRuleEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,12,1))
hpnicfEponUniQosRuleEntry.setIndexNames((0,_F,_H),(0,_E,_I),(0,_E,_R),(0,_E,_b))
if mibBuilder.loadTexts:hpnicfEponUniQosRuleEntry.setStatus(_A)
class _HpnicfEponUniQosRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfEponUniQosRuleIndex_Type.__name__=_C
_HpnicfEponUniQosRuleIndex_Object=MibTableColumn
hpnicfEponUniQosRuleIndex=_HpnicfEponUniQosRuleIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,12,1,1),_HpnicfEponUniQosRuleIndex_Type())
hpnicfEponUniQosRuleIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfEponUniQosRuleIndex.setStatus(_A)
class _HpnicfEponUniQosRuleSelector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('dstmac',1),('srcmac',2),('ethernetpriority',3),('vlanid',4),('ethernettype',5),('dstip',6),('srcip',7),('ipprototype',8),('ipv4tosdscp',9),('ipv6precedence',10),('srcport',11),('dstport',12)))
_HpnicfEponUniQosRuleSelector_Type.__name__=_C
_HpnicfEponUniQosRuleSelector_Object=MibTableColumn
hpnicfEponUniQosRuleSelector=_HpnicfEponUniQosRuleSelector_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,12,1,2),_HpnicfEponUniQosRuleSelector_Type())
hpnicfEponUniQosRuleSelector.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniQosRuleSelector.setStatus(_A)
_HpnicfEponUniQosRuleValue_Type=Integer32
_HpnicfEponUniQosRuleValue_Object=MibTableColumn
hpnicfEponUniQosRuleValue=_HpnicfEponUniQosRuleValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,12,1,3),_HpnicfEponUniQosRuleValue_Type())
hpnicfEponUniQosRuleValue.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniQosRuleValue.setStatus(_A)
_HpnicfEponUniQosRuleMacAddress_Type=MacAddress
_HpnicfEponUniQosRuleMacAddress_Object=MibTableColumn
hpnicfEponUniQosRuleMacAddress=_HpnicfEponUniQosRuleMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,12,1,4),_HpnicfEponUniQosRuleMacAddress_Type())
hpnicfEponUniQosRuleMacAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniQosRuleMacAddress.setStatus(_A)
class _HpnicfEponUniQosRuleOperator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('nevermatch',1),('equal',2),('notequal',3),('lessthanequal',4),('greaterthanequal',5),('fieldexist',6),('fieldnotexist',7),('alwaysmatch',8)))
_HpnicfEponUniQosRuleOperator_Type.__name__=_C
_HpnicfEponUniQosRuleOperator_Object=MibTableColumn
hpnicfEponUniQosRuleOperator=_HpnicfEponUniQosRuleOperator_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,12,1,5),_HpnicfEponUniQosRuleOperator_Type())
hpnicfEponUniQosRuleOperator.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniQosRuleOperator.setStatus(_A)
_HpnicfEponUniQosRuleRowStatus_Type=RowStatus
_HpnicfEponUniQosRuleRowStatus_Object=MibTableColumn
hpnicfEponUniQosRuleRowStatus=_HpnicfEponUniQosRuleRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,12,1,6),_HpnicfEponUniQosRuleRowStatus_Type())
hpnicfEponUniQosRuleRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniQosRuleRowStatus.setStatus(_A)
_HpnicfEponUniMirrorGroupTable_Object=MibTable
hpnicfEponUniMirrorGroupTable=_HpnicfEponUniMirrorGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,13))
if mibBuilder.loadTexts:hpnicfEponUniMirrorGroupTable.setStatus(_A)
_HpnicfEponUniMirrorGroupEntry_Object=MibTableRow
hpnicfEponUniMirrorGroupEntry=_HpnicfEponUniMirrorGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,13,1))
hpnicfEponUniMirrorGroupEntry.setIndexNames((0,_F,_H),(0,_E,_c))
if mibBuilder.loadTexts:hpnicfEponUniMirrorGroupEntry.setStatus(_A)
_HpnicfEponUniMirrorGroupID_Type=Integer32
_HpnicfEponUniMirrorGroupID_Object=MibTableColumn
hpnicfEponUniMirrorGroupID=_HpnicfEponUniMirrorGroupID_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,13,1,1),_HpnicfEponUniMirrorGroupID_Type())
hpnicfEponUniMirrorGroupID.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfEponUniMirrorGroupID.setStatus(_A)
_HpnicfEponUniMirrorInboundPortList_Type=OctetString
_HpnicfEponUniMirrorInboundPortList_Object=MibTableColumn
hpnicfEponUniMirrorInboundPortList=_HpnicfEponUniMirrorInboundPortList_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,13,1,2),_HpnicfEponUniMirrorInboundPortList_Type())
hpnicfEponUniMirrorInboundPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEponUniMirrorInboundPortList.setStatus(_A)
_HpnicfEponUniMirrorOutboundPortList_Type=OctetString
_HpnicfEponUniMirrorOutboundPortList_Object=MibTableColumn
hpnicfEponUniMirrorOutboundPortList=_HpnicfEponUniMirrorOutboundPortList_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,13,1,3),_HpnicfEponUniMirrorOutboundPortList_Type())
hpnicfEponUniMirrorOutboundPortList.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniMirrorOutboundPortList.setStatus(_A)
_HpnicfEponUniMonitorPort_Type=Integer32
_HpnicfEponUniMonitorPort_Object=MibTableColumn
hpnicfEponUniMonitorPort=_HpnicfEponUniMonitorPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,13,1,4),_HpnicfEponUniMonitorPort_Type())
hpnicfEponUniMonitorPort.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniMonitorPort.setStatus(_A)
_HpnicfEponUniMirrorRowStatus_Type=RowStatus
_HpnicfEponUniMirrorRowStatus_Object=MibTableColumn
hpnicfEponUniMirrorRowStatus=_HpnicfEponUniMirrorRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,13,1,5),_HpnicfEponUniMirrorRowStatus_Type())
hpnicfEponUniMirrorRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfEponUniMirrorRowStatus.setStatus(_A)
_HpnicfEponUniMirrorGroupIdNextTable_Object=MibTable
hpnicfEponUniMirrorGroupIdNextTable=_HpnicfEponUniMirrorGroupIdNextTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,14))
if mibBuilder.loadTexts:hpnicfEponUniMirrorGroupIdNextTable.setStatus(_A)
_HpnicfEponUniMirrorGroupIdNextEntry_Object=MibTableRow
hpnicfEponUniMirrorGroupIdNextEntry=_HpnicfEponUniMirrorGroupIdNextEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,14,1))
hpnicfEponUniMirrorGroupIdNextEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:hpnicfEponUniMirrorGroupIdNextEntry.setStatus(_A)
_HpnicfEponUniMirrorGroupIDNext_Type=Integer32
_HpnicfEponUniMirrorGroupIDNext_Object=MibTableColumn
hpnicfEponUniMirrorGroupIDNext=_HpnicfEponUniMirrorGroupIDNext_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,14,1,1),_HpnicfEponUniMirrorGroupIDNext_Type())
hpnicfEponUniMirrorGroupIDNext.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniMirrorGroupIDNext.setStatus(_A)
_HpnicfEponUniMulticastCtrlInfoTable_Object=MibTable
hpnicfEponUniMulticastCtrlInfoTable=_HpnicfEponUniMulticastCtrlInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,15))
if mibBuilder.loadTexts:hpnicfEponUniMulticastCtrlInfoTable.setStatus(_A)
_HpnicfEponUniMulticastCtrlInfoEntry_Object=MibTableRow
hpnicfEponUniMulticastCtrlInfoEntry=_HpnicfEponUniMulticastCtrlInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,15,1))
hpnicfEponUniMulticastCtrlInfoEntry.setIndexNames((0,_F,_H),(0,_E,_I),(0,_E,_d),(0,_E,_e))
if mibBuilder.loadTexts:hpnicfEponUniMulticastCtrlInfoEntry.setStatus(_A)
_HpnicfEponUniMultActVlan_Type=Integer32
_HpnicfEponUniMultActVlan_Object=MibTableColumn
hpnicfEponUniMultActVlan=_HpnicfEponUniMultActVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,15,1,1),_HpnicfEponUniMultActVlan_Type())
hpnicfEponUniMultActVlan.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfEponUniMultActVlan.setStatus(_A)
_HpnicfEponUniMultActAddress_Type=IpAddress
_HpnicfEponUniMultActAddress_Object=MibTableColumn
hpnicfEponUniMultActAddress=_HpnicfEponUniMultActAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,15,1,2),_HpnicfEponUniMultActAddress_Type())
hpnicfEponUniMultActAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfEponUniMultActAddress.setStatus(_A)
class _HpnicfEponUniMultActAccessRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('deny',1),(_Z,2),(_a,3)))
_HpnicfEponUniMultActAccessRule_Type.__name__=_C
_HpnicfEponUniMultActAccessRule_Object=MibTableColumn
hpnicfEponUniMultActAccessRule=_HpnicfEponUniMultActAccessRule_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,15,1,3),_HpnicfEponUniMultActAccessRule_Type())
hpnicfEponUniMultActAccessRule.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniMultActAccessRule.setStatus(_A)
_HpnicfEponUniMultActPreTimes_Type=Integer32
_HpnicfEponUniMultActPreTimes_Object=MibTableColumn
hpnicfEponUniMultActPreTimes=_HpnicfEponUniMultActPreTimes_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,15,1,4),_HpnicfEponUniMultActPreTimes_Type())
hpnicfEponUniMultActPreTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniMultActPreTimes.setStatus(_A)
_HpnicfEponUniMultActPreRemain_Type=Integer32
_HpnicfEponUniMultActPreRemain_Object=MibTableColumn
hpnicfEponUniMultActPreRemain=_HpnicfEponUniMultActPreRemain_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,15,1,5),_HpnicfEponUniMultActPreRemain_Type())
hpnicfEponUniMultActPreRemain.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniMultActPreRemain.setStatus(_A)
_HpnicfEponUniMulticastIndexNextTable_Object=MibTable
hpnicfEponUniMulticastIndexNextTable=_HpnicfEponUniMulticastIndexNextTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,16))
if mibBuilder.loadTexts:hpnicfEponUniMulticastIndexNextTable.setStatus(_A)
_HpnicfEponUniMulticastIndexNextEntry_Object=MibTableRow
hpnicfEponUniMulticastIndexNextEntry=_HpnicfEponUniMulticastIndexNextEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,16,1))
hpnicfEponUniMulticastIndexNextEntry.setIndexNames((0,_F,_H),(0,_E,_I))
if mibBuilder.loadTexts:hpnicfEponUniMulticastIndexNextEntry.setStatus(_A)
_HpnicfEponUniMulticastConfIndexNext_Type=Integer32
_HpnicfEponUniMulticastConfIndexNext_Object=MibTableColumn
hpnicfEponUniMulticastConfIndexNext=_HpnicfEponUniMulticastConfIndexNext_Object((1,3,6,1,4,1,11,2,14,11,15,2,42,5,1,16,1,1),_HpnicfEponUniMulticastConfIndexNext_Type())
hpnicfEponUniMulticastConfIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfEponUniMulticastConfIndexNext.setStatus(_A)
_HpnicfEponUniTrap_ObjectIdentity=ObjectIdentity
hpnicfEponUniTrap=_HpnicfEponUniTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,5,2))
_HpnicfEponUniTrapPrefix_ObjectIdentity=ObjectIdentity
hpnicfEponUniTrapPrefix=_HpnicfEponUniTrapPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,42,5,2,0))
hpnicfEponUniLinkUpTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,5,2,0,1))
hpnicfEponUniLinkUpTrap.setObjects(*((_F,_H),(_F,_L),(_E,_I),(_E,_M),(_E,_S)))
if mibBuilder.loadTexts:hpnicfEponUniLinkUpTrap.setStatus(_A)
hpnicfEponUniLinkDownTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,5,2,0,2))
hpnicfEponUniLinkDownTrap.setObjects(*((_F,_H),(_F,_L),(_E,_I),(_E,_M),(_E,_S)))
if mibBuilder.loadTexts:hpnicfEponUniLinkDownTrap.setStatus(_A)
hpnicfEponUniLoopBackDetectedTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,5,2,0,3))
hpnicfEponUniLoopBackDetectedTrap.setObjects(*((_F,_H),(_F,_L),(_E,_I),(_E,_M),(_E,_T)))
if mibBuilder.loadTexts:hpnicfEponUniLoopBackDetectedTrap.setStatus(_A)
hpnicfEponUniLoopBackRecoveredTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,42,5,2,0,4))
hpnicfEponUniLoopBackRecoveredTrap.setObjects(*((_F,_H),(_F,_L),(_E,_I),(_E,_M),(_E,_T)))
if mibBuilder.loadTexts:hpnicfEponUniLoopBackRecoveredTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hpnicfEponUni':hpnicfEponUni,'hpnicfEponUniSysMan':hpnicfEponUniSysMan,'hpnicfEponUniSysManTable':hpnicfEponUniSysManTable,'hpnicfEponUniSysManEntry':hpnicfEponUniSysManEntry,_I:hpnicfEponUniIndex,_M:hpnicfEponUniDescr,_S:hpnicfEponUniAdminStatus,'hpnicfEponUniMdi':hpnicfEponUniMdi,'hpnicfEponUniPriority':hpnicfEponUniPriority,'hpnicfEponUniVlanType':hpnicfEponUniVlanType,'hpnicfEponUniAccessVlan':hpnicfEponUniAccessVlan,'hpnicfEponUniTrunkPvid':hpnicfEponUniTrunkPvid,'hpnicfEponUniVLANTrunkAllowListLow':hpnicfEponUniVLANTrunkAllowListLow,'hpnicfEponUniVLANTrunkAllowListHigh':hpnicfEponUniVLANTrunkAllowListHigh,'hpnicfEponUniInboundLineRate':hpnicfEponUniInboundLineRate,'hpnicfEponUniOutboundLineRate':hpnicfEponUniOutboundLineRate,'hpnicfEponUniFlowControl':hpnicfEponUniFlowControl,'hpnicfEponUniSpeed':hpnicfEponUniSpeed,'hpnicfEponUniDuplex':hpnicfEponUniDuplex,'hpnicfEponUniVlanVPNStatus':hpnicfEponUniVlanVPNStatus,'hpnicfEponUniCountReset':hpnicfEponUniCountReset,'hpnicfEponUniPortIsolate':hpnicfEponUniPortIsolate,'hpnicfEponUniVlanConfiguration':hpnicfEponUniVlanConfiguration,'hpnicfEponUniAutoNegotiation':hpnicfEponUniAutoNegotiation,'hpnicfEponUniRestartAutoNeg':hpnicfEponUniRestartAutoNeg,'hpnicfEponUniLinkStatus':hpnicfEponUniLinkStatus,'hpnicfEponUniInterfaceType':hpnicfEponUniInterfaceType,'hpnicfEponUniVitualCableTest':hpnicfEponUniVitualCableTest,'hpnicfEponUniVCTCableStatus':hpnicfEponUniVCTCableStatus,'hpnicfEponUniVCTCableLength':hpnicfEponUniVCTCableLength,'hpnicfEponUniVCTImpedanceMismatch':hpnicfEponUniVCTImpedanceMismatch,'hpnicfEponUniVCTPairSkew':hpnicfEponUniVCTPairSkew,'hpnicfEponUniVCTPairSwap':hpnicfEponUniVCTPairSwap,'hpnicfEponUniVCTPolaritySwap':hpnicfEponUniVCTPolaritySwap,'hpnicfEponUniVCTInsertionLoss':hpnicfEponUniVCTInsertionLoss,'hpnicfEponUniVCTReturnLoss':hpnicfEponUniVCTReturnLoss,'hpnicfEponUniVCTNearendCrosstalk':hpnicfEponUniVCTNearendCrosstalk,_T:hpnicfEponUniVlan,'hpnicfEponUniCountTable':hpnicfEponUniCountTable,'hpnicfEponUniCountEntry':hpnicfEponUniCountEntry,'hpnicfEponUniInStatsPkts':hpnicfEponUniInStatsPkts,'hpnicfEponUniInStatsUnicastPkts':hpnicfEponUniInStatsUnicastPkts,'hpnicfEponUniInStatsBroadcastPkts':hpnicfEponUniInStatsBroadcastPkts,'hpnicfEponUniInStatsMulticastPkts':hpnicfEponUniInStatsMulticastPkts,'hpnicfEponUniInPausePkts':hpnicfEponUniInPausePkts,'hpnicfEponUniInTotalErrors':hpnicfEponUniInTotalErrors,'hpnicfEponUniInStatsCRCAlignErrors':hpnicfEponUniInStatsCRCAlignErrors,'hpnicfEponUniInStatsUndersizePkts':hpnicfEponUniInStatsUndersizePkts,'hpnicfEponUniInStatsOversizePkts':hpnicfEponUniInStatsOversizePkts,'hpnicfEponUniInErrorbyOther':hpnicfEponUniInErrorbyOther,'hpnicfEponUniOutStatsPkts':hpnicfEponUniOutStatsPkts,'hpnicfEponUniOutStatsUnicastPkts':hpnicfEponUniOutStatsUnicastPkts,'hpnicfEponUniOutStatsBroadcastPkts':hpnicfEponUniOutStatsBroadcastPkts,'hpnicfEponUniOutStatsMulticastPkts':hpnicfEponUniOutStatsMulticastPkts,'hpnicfEponUniOutStatsPausePkts':hpnicfEponUniOutStatsPausePkts,'hpnicfEponUniOutTotalErrors':hpnicfEponUniOutTotalErrors,'hpnicfEponUniOutStatsCollisions':hpnicfEponUniOutStatsCollisions,'hpnicfEponUniOutDelayExceededDiscards':hpnicfEponUniOutDelayExceededDiscards,'hpnicfEponUniOutErrorbyOther':hpnicfEponUniOutErrorbyOther,'hpnicfEponUniOutDroppedFrames':hpnicfEponUniOutDroppedFrames,'hpnicfEponUniIgmpInfoTable':hpnicfEponUniIgmpInfoTable,'hpnicfEponUniIgmpInfoEntry':hpnicfEponUniIgmpInfoEntry,_X:hpnicfEponUniMacIndex,'hpnicfEponUniIgmpMacAddress':hpnicfEponUniIgmpMacAddress,'hpnicfEponUniIgmpVlanId':hpnicfEponUniIgmpVlanId,'hpnicfEponUniParaMan':hpnicfEponUniParaMan,'hpnicfEponUniLineRateMax':hpnicfEponUniLineRateMax,'hpnicfEponUniLineRateStep':hpnicfEponUniLineRateStep,'hpnicfEponUniNumberOnOnu':hpnicfEponUniNumberOnOnu,'hpnicfEponUniScalarGroup':hpnicfEponUniScalarGroup,'hpnicfEponUniPortPolicyTable':hpnicfEponUniPortPolicyTable,'hpnicfEponUniPortPolicyEntry':hpnicfEponUniPortPolicyEntry,'hpnicfEponUniPortPolicyStatus':hpnicfEponUniPortPolicyStatus,'hpnicfEponUniPortPolicyCir':hpnicfEponUniPortPolicyCir,'hpnicfEponUniPortPolicyBucketDepth':hpnicfEponUniPortPolicyBucketDepth,'hpnicfEponUniPortPolicyExtraBurst':hpnicfEponUniPortPolicyExtraBurst,'hpnicfEponUniPortPolicyInboundCir':hpnicfEponUniPortPolicyInboundCir,'hpnicfEponUniPortPolicyInboundBucketDepth':hpnicfEponUniPortPolicyInboundBucketDepth,'hpnicfEponUniPortPolicyInboundExtraBurst':hpnicfEponUniPortPolicyInboundExtraBurst,'hpnicfEponUniPortPolicyOutboundCir':hpnicfEponUniPortPolicyOutboundCir,'hpnicfEponUniPortPolicyOutboundPir':hpnicfEponUniPortPolicyOutboundPir,'hpnicfEponUniMulticastTable':hpnicfEponUniMulticastTable,'hpnicfEponUniMulticastEntry':hpnicfEponUniMulticastEntry,'hpnicfEponUniMulticastGroupNumber':hpnicfEponUniMulticastGroupNumber,'hpnicfEponUniMulticastVlanList':hpnicfEponUniMulticastVlanList,'hpnicfEponUniMulticastStripStatus':hpnicfEponUniMulticastStripStatus,'hpnicfEponUniMulticastFastleave':hpnicfEponUniMulticastFastleave,'hpnicfEponUniTechAbilityTable':hpnicfEponUniTechAbilityTable,'hpnicfEponUniTechAbilityEntry':hpnicfEponUniTechAbilityEntry,'hpnicfEponUniLocalTechAbility':hpnicfEponUniLocalTechAbility,'hpnicfEponUniAdvertisedTechAbility':hpnicfEponUniAdvertisedTechAbility,'hpnicfEponUniMulticastControlTable':hpnicfEponUniMulticastControlTable,'hpnicfEponUniMulticastControlEntry':hpnicfEponUniMulticastControlEntry,'hpnicfEponUniMulticastVlanIndex':hpnicfEponUniMulticastVlanIndex,'hpnicfEponUniMulticastAddressList':hpnicfEponUniMulticastAddressList,'hpnicfEponUniMulticastAccessRule':hpnicfEponUniMulticastAccessRule,'hpnicfEponUniMulticastChannelLimit':hpnicfEponUniMulticastChannelLimit,'hpnicfEponUniMulticastPreTimeSlice':hpnicfEponUniMulticastPreTimeSlice,'hpnicfEponUniMulticastPreTimes':hpnicfEponUniMulticastPreTimes,'hpnicfEponUniMulticastPreInterval':hpnicfEponUniMulticastPreInterval,'hpnicfEponUniMulticastRowStatus':hpnicfEponUniMulticastRowStatus,_Y:hpnicfEponUniMulticastIndex,'hpnicfEponUniMulticastSourceIpList':hpnicfEponUniMulticastSourceIpList,'hpnicfEponUniMulticastResetInterval':hpnicfEponUniMulticastResetInterval,'hpnicfEponUniQosIndexNextTable':hpnicfEponUniQosIndexNextTable,'hpnicfEponUniQosIndexNextEntry':hpnicfEponUniQosIndexNextEntry,'hpnicfEponUniQosConfIndexNext':hpnicfEponUniQosConfIndexNext,'hpnicfEponUniQosConfTable':hpnicfEponUniQosConfTable,'hpnicfEponUniQosConfEntry':hpnicfEponUniQosConfEntry,_R:hpnicfEponUniQosConfIndex,'hpnicfEponUniQosConfRuleIndexNext':hpnicfEponUniQosConfRuleIndexNext,'hpnicfEponUniQosConfMappedQueue':hpnicfEponUniQosConfMappedQueue,'hpnicfEponUniQosConfMarkedPriority':hpnicfEponUniQosConfMarkedPriority,'hpnicfEponUniQosConfRowStatus':hpnicfEponUniQosConfRowStatus,'hpnicfEponUniQosRuleTable':hpnicfEponUniQosRuleTable,'hpnicfEponUniQosRuleEntry':hpnicfEponUniQosRuleEntry,_b:hpnicfEponUniQosRuleIndex,'hpnicfEponUniQosRuleSelector':hpnicfEponUniQosRuleSelector,'hpnicfEponUniQosRuleValue':hpnicfEponUniQosRuleValue,'hpnicfEponUniQosRuleMacAddress':hpnicfEponUniQosRuleMacAddress,'hpnicfEponUniQosRuleOperator':hpnicfEponUniQosRuleOperator,'hpnicfEponUniQosRuleRowStatus':hpnicfEponUniQosRuleRowStatus,'hpnicfEponUniMirrorGroupTable':hpnicfEponUniMirrorGroupTable,'hpnicfEponUniMirrorGroupEntry':hpnicfEponUniMirrorGroupEntry,_c:hpnicfEponUniMirrorGroupID,'hpnicfEponUniMirrorInboundPortList':hpnicfEponUniMirrorInboundPortList,'hpnicfEponUniMirrorOutboundPortList':hpnicfEponUniMirrorOutboundPortList,'hpnicfEponUniMonitorPort':hpnicfEponUniMonitorPort,'hpnicfEponUniMirrorRowStatus':hpnicfEponUniMirrorRowStatus,'hpnicfEponUniMirrorGroupIdNextTable':hpnicfEponUniMirrorGroupIdNextTable,'hpnicfEponUniMirrorGroupIdNextEntry':hpnicfEponUniMirrorGroupIdNextEntry,'hpnicfEponUniMirrorGroupIDNext':hpnicfEponUniMirrorGroupIDNext,'hpnicfEponUniMulticastCtrlInfoTable':hpnicfEponUniMulticastCtrlInfoTable,'hpnicfEponUniMulticastCtrlInfoEntry':hpnicfEponUniMulticastCtrlInfoEntry,_d:hpnicfEponUniMultActVlan,_e:hpnicfEponUniMultActAddress,'hpnicfEponUniMultActAccessRule':hpnicfEponUniMultActAccessRule,'hpnicfEponUniMultActPreTimes':hpnicfEponUniMultActPreTimes,'hpnicfEponUniMultActPreRemain':hpnicfEponUniMultActPreRemain,'hpnicfEponUniMulticastIndexNextTable':hpnicfEponUniMulticastIndexNextTable,'hpnicfEponUniMulticastIndexNextEntry':hpnicfEponUniMulticastIndexNextEntry,'hpnicfEponUniMulticastConfIndexNext':hpnicfEponUniMulticastConfIndexNext,'hpnicfEponUniTrap':hpnicfEponUniTrap,'hpnicfEponUniTrapPrefix':hpnicfEponUniTrapPrefix,'hpnicfEponUniLinkUpTrap':hpnicfEponUniLinkUpTrap,'hpnicfEponUniLinkDownTrap':hpnicfEponUniLinkDownTrap,'hpnicfEponUniLoopBackDetectedTrap':hpnicfEponUniLoopBackDetectedTrap,'hpnicfEponUniLoopBackRecoveredTrap':hpnicfEponUniLoopBackRecoveredTrap})