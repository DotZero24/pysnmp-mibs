_c='h3cEponUniMultActAddress'
_b='h3cEponUniMultActVlan'
_a='h3cEponUniMirrorGroupID'
_Z='h3cEponUniQosRuleIndex'
_Y='preview'
_X='permit'
_W='h3cEponUniMulticastIndex'
_V='h3cEponUniMacIndex'
_U='notSupport'
_T='TruthValue'
_S='h3cEponUniAdminStatus'
_R='h3cEponUniDescr'
_Q='h3cEponUniQosConfIndex'
_P='ifDescr'
_O='false'
_N='true'
_M='disable'
_L='enable'
_K='not-accessible'
_J='OctetString'
_I='h3cEponUniIndex'
_H='ifIndex'
_G='IF-MIB'
_F='read-create'
_E='A3COM-HUAWEI-EPON-UNI-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cEpon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cEpon')
ifDescr,ifIndex=mibBuilder.importSymbols(_G,_P,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_T)
h3cEponUni=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,42,5))
_H3cEponUniSysMan_ObjectIdentity=ObjectIdentity
h3cEponUniSysMan=_H3cEponUniSysMan_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,42,5,1))
_H3cEponUniSysManTable_Object=MibTable
h3cEponUniSysManTable=_H3cEponUniSysManTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1))
if mibBuilder.loadTexts:h3cEponUniSysManTable.setStatus(_A)
_H3cEponUniSysManEntry_Object=MibTableRow
h3cEponUniSysManEntry=_H3cEponUniSysManEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1))
h3cEponUniSysManEntry.setIndexNames((0,_G,_H),(0,_E,_I))
if mibBuilder.loadTexts:h3cEponUniSysManEntry.setStatus(_A)
_H3cEponUniIndex_Type=Integer32
_H3cEponUniIndex_Object=MibTableColumn
h3cEponUniIndex=_H3cEponUniIndex_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,1),_H3cEponUniIndex_Type())
h3cEponUniIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:h3cEponUniIndex.setStatus(_A)
_H3cEponUniDescr_Type=OctetString
_H3cEponUniDescr_Object=MibTableColumn
h3cEponUniDescr=_H3cEponUniDescr_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,2),_H3cEponUniDescr_Type())
h3cEponUniDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniDescr.setStatus(_A)
class _H3cEponUniAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_H3cEponUniAdminStatus_Type.__name__=_C
_H3cEponUniAdminStatus_Object=MibTableColumn
h3cEponUniAdminStatus=_H3cEponUniAdminStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,3),_H3cEponUniAdminStatus_Type())
h3cEponUniAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniAdminStatus.setStatus(_A)
class _H3cEponUniMdi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mdi-ii',1),('mdi-x',2),('mdi-auto',3)))
_H3cEponUniMdi_Type.__name__=_C
_H3cEponUniMdi_Object=MibTableColumn
h3cEponUniMdi=_H3cEponUniMdi_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,4),_H3cEponUniMdi_Type())
h3cEponUniMdi.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniMdi.setStatus(_A)
class _H3cEponUniPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_H3cEponUniPriority_Type.__name__=_C
_H3cEponUniPriority_Object=MibTableColumn
h3cEponUniPriority=_H3cEponUniPriority_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,5),_H3cEponUniPriority_Type())
h3cEponUniPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniPriority.setStatus(_A)
class _H3cEponUniVlanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('vlantrunk',1),('access',2),('hybrid',3),('untagged',4),('transparent',5),('doubletagged',6),('tag',7),('translation',8)))
_H3cEponUniVlanType_Type.__name__=_C
_H3cEponUniVlanType_Object=MibTableColumn
h3cEponUniVlanType=_H3cEponUniVlanType_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,6),_H3cEponUniVlanType_Type())
h3cEponUniVlanType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniVlanType.setStatus(_A)
class _H3cEponUniAccessVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_H3cEponUniAccessVlan_Type.__name__=_C
_H3cEponUniAccessVlan_Object=MibTableColumn
h3cEponUniAccessVlan=_H3cEponUniAccessVlan_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,7),_H3cEponUniAccessVlan_Type())
h3cEponUniAccessVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniAccessVlan.setStatus(_A)
class _H3cEponUniTrunkPvid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_H3cEponUniTrunkPvid_Type.__name__=_C
_H3cEponUniTrunkPvid_Object=MibTableColumn
h3cEponUniTrunkPvid=_H3cEponUniTrunkPvid_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,8),_H3cEponUniTrunkPvid_Type())
h3cEponUniTrunkPvid.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniTrunkPvid.setStatus(_A)
_H3cEponUniVLANTrunkAllowListLow_Type=OctetString
_H3cEponUniVLANTrunkAllowListLow_Object=MibTableColumn
h3cEponUniVLANTrunkAllowListLow=_H3cEponUniVLANTrunkAllowListLow_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,9),_H3cEponUniVLANTrunkAllowListLow_Type())
h3cEponUniVLANTrunkAllowListLow.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniVLANTrunkAllowListLow.setStatus(_A)
_H3cEponUniVLANTrunkAllowListHigh_Type=OctetString
_H3cEponUniVLANTrunkAllowListHigh_Object=MibTableColumn
h3cEponUniVLANTrunkAllowListHigh=_H3cEponUniVLANTrunkAllowListHigh_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,10),_H3cEponUniVLANTrunkAllowListHigh_Type())
h3cEponUniVLANTrunkAllowListHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniVLANTrunkAllowListHigh.setStatus(_A)
_H3cEponUniInboundLineRate_Type=Integer32
_H3cEponUniInboundLineRate_Object=MibTableColumn
h3cEponUniInboundLineRate=_H3cEponUniInboundLineRate_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,11),_H3cEponUniInboundLineRate_Type())
h3cEponUniInboundLineRate.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniInboundLineRate.setStatus(_A)
_H3cEponUniOutboundLineRate_Type=Integer32
_H3cEponUniOutboundLineRate_Object=MibTableColumn
h3cEponUniOutboundLineRate=_H3cEponUniOutboundLineRate_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,12),_H3cEponUniOutboundLineRate_Type())
h3cEponUniOutboundLineRate.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniOutboundLineRate.setStatus(_A)
_H3cEponUniFlowControl_Type=TruthValue
_H3cEponUniFlowControl_Object=MibTableColumn
h3cEponUniFlowControl=_H3cEponUniFlowControl_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,13),_H3cEponUniFlowControl_Type())
h3cEponUniFlowControl.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniFlowControl.setStatus(_A)
class _H3cEponUniSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,10,100,1000,10000,24000)));namedValues=NamedValues(*(('auto',0),('s10M',10),('s100M',100),('s1000M',1000),('s10000M',10000),('s24000M',24000)))
_H3cEponUniSpeed_Type.__name__=_C
_H3cEponUniSpeed_Object=MibTableColumn
h3cEponUniSpeed=_H3cEponUniSpeed_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,14),_H3cEponUniSpeed_Type())
h3cEponUniSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniSpeed.setStatus(_A)
class _H3cEponUniDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('full',1),('half',2),('auto',3)))
_H3cEponUniDuplex_Type.__name__=_C
_H3cEponUniDuplex_Object=MibTableColumn
h3cEponUniDuplex=_H3cEponUniDuplex_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,15),_H3cEponUniDuplex_Type())
h3cEponUniDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniDuplex.setStatus(_A)
_H3cEponUniVlanVPNStatus_Type=TruthValue
_H3cEponUniVlanVPNStatus_Object=MibTableColumn
h3cEponUniVlanVPNStatus=_H3cEponUniVlanVPNStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,16),_H3cEponUniVlanVPNStatus_Type())
h3cEponUniVlanVPNStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniVlanVPNStatus.setStatus(_A)
class _H3cEponUniCountReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_H3cEponUniCountReset_Type.__name__=_C
_H3cEponUniCountReset_Object=MibTableColumn
h3cEponUniCountReset=_H3cEponUniCountReset_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,17),_H3cEponUniCountReset_Type())
h3cEponUniCountReset.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniCountReset.setStatus(_A)
class _H3cEponUniPortIsolate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_H3cEponUniPortIsolate_Type.__name__=_C
_H3cEponUniPortIsolate_Object=MibTableColumn
h3cEponUniPortIsolate=_H3cEponUniPortIsolate_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,18),_H3cEponUniPortIsolate_Type())
h3cEponUniPortIsolate.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniPortIsolate.setStatus(_A)
class _H3cEponUniVlanConfiguration_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cEponUniVlanConfiguration_Type.__name__=_J
_H3cEponUniVlanConfiguration_Object=MibTableColumn
h3cEponUniVlanConfiguration=_H3cEponUniVlanConfiguration_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,23),_H3cEponUniVlanConfiguration_Type())
h3cEponUniVlanConfiguration.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniVlanConfiguration.setStatus(_A)
class _H3cEponUniAutoNegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_H3cEponUniAutoNegotiation_Type.__name__=_C
_H3cEponUniAutoNegotiation_Object=MibTableColumn
h3cEponUniAutoNegotiation=_H3cEponUniAutoNegotiation_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,25),_H3cEponUniAutoNegotiation_Type())
h3cEponUniAutoNegotiation.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniAutoNegotiation.setStatus(_A)
class _H3cEponUniRestartAutoNeg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('autoNegotiation',1))
_H3cEponUniRestartAutoNeg_Type.__name__=_C
_H3cEponUniRestartAutoNeg_Object=MibTableColumn
h3cEponUniRestartAutoNeg=_H3cEponUniRestartAutoNeg_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,26),_H3cEponUniRestartAutoNeg_Type())
h3cEponUniRestartAutoNeg.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniRestartAutoNeg.setStatus(_A)
class _H3cEponUniLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_H3cEponUniLinkStatus_Type.__name__=_C
_H3cEponUniLinkStatus_Object=MibTableColumn
h3cEponUniLinkStatus=_H3cEponUniLinkStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,29),_H3cEponUniLinkStatus_Type())
h3cEponUniLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniLinkStatus.setStatus(_A)
class _H3cEponUniInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('gigabitethernetport',1),('fastethernetport',2),('voipport',3),('e1port',4)))
_H3cEponUniInterfaceType_Type.__name__=_C
_H3cEponUniInterfaceType_Object=MibTableColumn
h3cEponUniInterfaceType=_H3cEponUniInterfaceType_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,30),_H3cEponUniInterfaceType_Type())
h3cEponUniInterfaceType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniInterfaceType.setStatus(_A)
class _H3cEponUniVitualCableTest_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_H3cEponUniVitualCableTest_Type.__name__=_C
_H3cEponUniVitualCableTest_Object=MibTableColumn
h3cEponUniVitualCableTest=_H3cEponUniVitualCableTest_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,31),_H3cEponUniVitualCableTest_Type())
h3cEponUniVitualCableTest.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniVitualCableTest.setStatus(_A)
class _H3cEponUniVCTCableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('normal',1),('abnormal',2),('abnormalOpen',3),('abnormalShort',4),('failure',5)))
_H3cEponUniVCTCableStatus_Type.__name__=_C
_H3cEponUniVCTCableStatus_Object=MibTableColumn
h3cEponUniVCTCableStatus=_H3cEponUniVCTCableStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,32),_H3cEponUniVCTCableStatus_Type())
h3cEponUniVCTCableStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniVCTCableStatus.setStatus(_A)
_H3cEponUniVCTCableLength_Type=Integer32
_H3cEponUniVCTCableLength_Object=MibTableColumn
h3cEponUniVCTCableLength=_H3cEponUniVCTCableLength_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,33),_H3cEponUniVCTCableLength_Type())
h3cEponUniVCTCableLength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniVCTCableLength.setStatus(_A)
class _H3cEponUniVCTImpedanceMismatch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('not-support',1),(_N,2),(_O,3)))
_H3cEponUniVCTImpedanceMismatch_Type.__name__=_C
_H3cEponUniVCTImpedanceMismatch_Object=MibTableColumn
h3cEponUniVCTImpedanceMismatch=_H3cEponUniVCTImpedanceMismatch_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,34),_H3cEponUniVCTImpedanceMismatch_Type())
h3cEponUniVCTImpedanceMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniVCTImpedanceMismatch.setStatus(_A)
_H3cEponUniVCTPairSkew_Type=Integer32
_H3cEponUniVCTPairSkew_Object=MibTableColumn
h3cEponUniVCTPairSkew=_H3cEponUniVCTPairSkew_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,35),_H3cEponUniVCTPairSkew_Type())
h3cEponUniVCTPairSkew.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniVCTPairSkew.setStatus(_A)
class _H3cEponUniVCTPairSwap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),(_N,2),(_O,3)))
_H3cEponUniVCTPairSwap_Type.__name__=_C
_H3cEponUniVCTPairSwap_Object=MibTableColumn
h3cEponUniVCTPairSwap=_H3cEponUniVCTPairSwap_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,36),_H3cEponUniVCTPairSwap_Type())
h3cEponUniVCTPairSwap.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniVCTPairSwap.setStatus(_A)
class _H3cEponUniVCTPolaritySwap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),(_N,2),(_O,3)))
_H3cEponUniVCTPolaritySwap_Type.__name__=_C
_H3cEponUniVCTPolaritySwap_Object=MibTableColumn
h3cEponUniVCTPolaritySwap=_H3cEponUniVCTPolaritySwap_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,37),_H3cEponUniVCTPolaritySwap_Type())
h3cEponUniVCTPolaritySwap.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniVCTPolaritySwap.setStatus(_A)
_H3cEponUniVCTInsertionLoss_Type=Integer32
_H3cEponUniVCTInsertionLoss_Object=MibTableColumn
h3cEponUniVCTInsertionLoss=_H3cEponUniVCTInsertionLoss_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,38),_H3cEponUniVCTInsertionLoss_Type())
h3cEponUniVCTInsertionLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniVCTInsertionLoss.setStatus(_A)
_H3cEponUniVCTReturnLoss_Type=Integer32
_H3cEponUniVCTReturnLoss_Object=MibTableColumn
h3cEponUniVCTReturnLoss=_H3cEponUniVCTReturnLoss_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,39),_H3cEponUniVCTReturnLoss_Type())
h3cEponUniVCTReturnLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniVCTReturnLoss.setStatus(_A)
_H3cEponUniVCTNearendCrosstalk_Type=Integer32
_H3cEponUniVCTNearendCrosstalk_Object=MibTableColumn
h3cEponUniVCTNearendCrosstalk=_H3cEponUniVCTNearendCrosstalk_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,1,1,40),_H3cEponUniVCTNearendCrosstalk_Type())
h3cEponUniVCTNearendCrosstalk.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniVCTNearendCrosstalk.setStatus(_A)
_H3cEponUniCountTable_Object=MibTable
h3cEponUniCountTable=_H3cEponUniCountTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2))
if mibBuilder.loadTexts:h3cEponUniCountTable.setStatus(_A)
_H3cEponUniCountEntry_Object=MibTableRow
h3cEponUniCountEntry=_H3cEponUniCountEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1))
h3cEponUniCountEntry.setIndexNames((0,_G,_H),(0,_E,_I))
if mibBuilder.loadTexts:h3cEponUniCountEntry.setStatus(_A)
_H3cEponUniInStatsPkts_Type=Unsigned32
_H3cEponUniInStatsPkts_Object=MibTableColumn
h3cEponUniInStatsPkts=_H3cEponUniInStatsPkts_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1,1),_H3cEponUniInStatsPkts_Type())
h3cEponUniInStatsPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniInStatsPkts.setStatus(_A)
_H3cEponUniInStatsUnicastPkts_Type=Unsigned32
_H3cEponUniInStatsUnicastPkts_Object=MibTableColumn
h3cEponUniInStatsUnicastPkts=_H3cEponUniInStatsUnicastPkts_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1,2),_H3cEponUniInStatsUnicastPkts_Type())
h3cEponUniInStatsUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniInStatsUnicastPkts.setStatus(_A)
_H3cEponUniInStatsBroadcastPkts_Type=Unsigned32
_H3cEponUniInStatsBroadcastPkts_Object=MibTableColumn
h3cEponUniInStatsBroadcastPkts=_H3cEponUniInStatsBroadcastPkts_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1,3),_H3cEponUniInStatsBroadcastPkts_Type())
h3cEponUniInStatsBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniInStatsBroadcastPkts.setStatus(_A)
_H3cEponUniInStatsMulticastPkts_Type=Unsigned32
_H3cEponUniInStatsMulticastPkts_Object=MibTableColumn
h3cEponUniInStatsMulticastPkts=_H3cEponUniInStatsMulticastPkts_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1,4),_H3cEponUniInStatsMulticastPkts_Type())
h3cEponUniInStatsMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniInStatsMulticastPkts.setStatus(_A)
_H3cEponUniInPausePkts_Type=Unsigned32
_H3cEponUniInPausePkts_Object=MibTableColumn
h3cEponUniInPausePkts=_H3cEponUniInPausePkts_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1,5),_H3cEponUniInPausePkts_Type())
h3cEponUniInPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniInPausePkts.setStatus(_A)
_H3cEponUniInTotalErrors_Type=Unsigned32
_H3cEponUniInTotalErrors_Object=MibTableColumn
h3cEponUniInTotalErrors=_H3cEponUniInTotalErrors_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1,6),_H3cEponUniInTotalErrors_Type())
h3cEponUniInTotalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniInTotalErrors.setStatus(_A)
_H3cEponUniInStatsCRCAlignErrors_Type=Unsigned32
_H3cEponUniInStatsCRCAlignErrors_Object=MibTableColumn
h3cEponUniInStatsCRCAlignErrors=_H3cEponUniInStatsCRCAlignErrors_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1,7),_H3cEponUniInStatsCRCAlignErrors_Type())
h3cEponUniInStatsCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniInStatsCRCAlignErrors.setStatus(_A)
_H3cEponUniInStatsUndersizePkts_Type=Unsigned32
_H3cEponUniInStatsUndersizePkts_Object=MibTableColumn
h3cEponUniInStatsUndersizePkts=_H3cEponUniInStatsUndersizePkts_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1,8),_H3cEponUniInStatsUndersizePkts_Type())
h3cEponUniInStatsUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniInStatsUndersizePkts.setStatus(_A)
_H3cEponUniInStatsOversizePkts_Type=Unsigned32
_H3cEponUniInStatsOversizePkts_Object=MibTableColumn
h3cEponUniInStatsOversizePkts=_H3cEponUniInStatsOversizePkts_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1,9),_H3cEponUniInStatsOversizePkts_Type())
h3cEponUniInStatsOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniInStatsOversizePkts.setStatus(_A)
_H3cEponUniInErrorbyOther_Type=Unsigned32
_H3cEponUniInErrorbyOther_Object=MibTableColumn
h3cEponUniInErrorbyOther=_H3cEponUniInErrorbyOther_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1,10),_H3cEponUniInErrorbyOther_Type())
h3cEponUniInErrorbyOther.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniInErrorbyOther.setStatus(_A)
_H3cEponUniOutStatsPkts_Type=Unsigned32
_H3cEponUniOutStatsPkts_Object=MibTableColumn
h3cEponUniOutStatsPkts=_H3cEponUniOutStatsPkts_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1,11),_H3cEponUniOutStatsPkts_Type())
h3cEponUniOutStatsPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniOutStatsPkts.setStatus(_A)
_H3cEponUniOutStatsUnicastPkts_Type=Unsigned32
_H3cEponUniOutStatsUnicastPkts_Object=MibTableColumn
h3cEponUniOutStatsUnicastPkts=_H3cEponUniOutStatsUnicastPkts_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1,12),_H3cEponUniOutStatsUnicastPkts_Type())
h3cEponUniOutStatsUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniOutStatsUnicastPkts.setStatus(_A)
_H3cEponUniOutStatsBroadcastPkts_Type=Unsigned32
_H3cEponUniOutStatsBroadcastPkts_Object=MibTableColumn
h3cEponUniOutStatsBroadcastPkts=_H3cEponUniOutStatsBroadcastPkts_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1,13),_H3cEponUniOutStatsBroadcastPkts_Type())
h3cEponUniOutStatsBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniOutStatsBroadcastPkts.setStatus(_A)
_H3cEponUniOutStatsMulticastPkts_Type=Unsigned32
_H3cEponUniOutStatsMulticastPkts_Object=MibTableColumn
h3cEponUniOutStatsMulticastPkts=_H3cEponUniOutStatsMulticastPkts_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1,14),_H3cEponUniOutStatsMulticastPkts_Type())
h3cEponUniOutStatsMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniOutStatsMulticastPkts.setStatus(_A)
_H3cEponUniOutStatsPausePkts_Type=Unsigned32
_H3cEponUniOutStatsPausePkts_Object=MibTableColumn
h3cEponUniOutStatsPausePkts=_H3cEponUniOutStatsPausePkts_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1,15),_H3cEponUniOutStatsPausePkts_Type())
h3cEponUniOutStatsPausePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniOutStatsPausePkts.setStatus(_A)
_H3cEponUniOutTotalErrors_Type=Unsigned32
_H3cEponUniOutTotalErrors_Object=MibTableColumn
h3cEponUniOutTotalErrors=_H3cEponUniOutTotalErrors_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1,16),_H3cEponUniOutTotalErrors_Type())
h3cEponUniOutTotalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniOutTotalErrors.setStatus(_A)
_H3cEponUniOutStatsCollisions_Type=Unsigned32
_H3cEponUniOutStatsCollisions_Object=MibTableColumn
h3cEponUniOutStatsCollisions=_H3cEponUniOutStatsCollisions_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1,17),_H3cEponUniOutStatsCollisions_Type())
h3cEponUniOutStatsCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniOutStatsCollisions.setStatus(_A)
_H3cEponUniOutDelayExceededDiscards_Type=Unsigned32
_H3cEponUniOutDelayExceededDiscards_Object=MibTableColumn
h3cEponUniOutDelayExceededDiscards=_H3cEponUniOutDelayExceededDiscards_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1,18),_H3cEponUniOutDelayExceededDiscards_Type())
h3cEponUniOutDelayExceededDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniOutDelayExceededDiscards.setStatus(_A)
_H3cEponUniOutErrorbyOther_Type=Unsigned32
_H3cEponUniOutErrorbyOther_Object=MibTableColumn
h3cEponUniOutErrorbyOther=_H3cEponUniOutErrorbyOther_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1,19),_H3cEponUniOutErrorbyOther_Type())
h3cEponUniOutErrorbyOther.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniOutErrorbyOther.setStatus(_A)
_H3cEponUniOutDroppedFrames_Type=Unsigned32
_H3cEponUniOutDroppedFrames_Object=MibTableColumn
h3cEponUniOutDroppedFrames=_H3cEponUniOutDroppedFrames_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,2,1,20),_H3cEponUniOutDroppedFrames_Type())
h3cEponUniOutDroppedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniOutDroppedFrames.setStatus(_A)
_H3cEponUniIgmpInfoTable_Object=MibTable
h3cEponUniIgmpInfoTable=_H3cEponUniIgmpInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,3))
if mibBuilder.loadTexts:h3cEponUniIgmpInfoTable.setStatus(_A)
_H3cEponUniIgmpInfoEntry_Object=MibTableRow
h3cEponUniIgmpInfoEntry=_H3cEponUniIgmpInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,3,1))
h3cEponUniIgmpInfoEntry.setIndexNames((0,_G,_H),(0,_E,_I),(0,_E,_V))
if mibBuilder.loadTexts:h3cEponUniIgmpInfoEntry.setStatus(_A)
_H3cEponUniMacIndex_Type=Integer32
_H3cEponUniMacIndex_Object=MibTableColumn
h3cEponUniMacIndex=_H3cEponUniMacIndex_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,3,1,1),_H3cEponUniMacIndex_Type())
h3cEponUniMacIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cEponUniMacIndex.setStatus(_A)
_H3cEponUniIgmpMacAddress_Type=MacAddress
_H3cEponUniIgmpMacAddress_Object=MibTableColumn
h3cEponUniIgmpMacAddress=_H3cEponUniIgmpMacAddress_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,3,1,2),_H3cEponUniIgmpMacAddress_Type())
h3cEponUniIgmpMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniIgmpMacAddress.setStatus(_A)
class _H3cEponUniIgmpVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_H3cEponUniIgmpVlanId_Type.__name__=_C
_H3cEponUniIgmpVlanId_Object=MibTableColumn
h3cEponUniIgmpVlanId=_H3cEponUniIgmpVlanId_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,3,1,3),_H3cEponUniIgmpVlanId_Type())
h3cEponUniIgmpVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniIgmpVlanId.setStatus(_A)
_H3cEponUniParaMan_ObjectIdentity=ObjectIdentity
h3cEponUniParaMan=_H3cEponUniParaMan_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,42,5,1,4))
_H3cEponUniLineRateMax_Type=Integer32
_H3cEponUniLineRateMax_Object=MibScalar
h3cEponUniLineRateMax=_H3cEponUniLineRateMax_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,4,1),_H3cEponUniLineRateMax_Type())
h3cEponUniLineRateMax.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniLineRateMax.setStatus(_A)
_H3cEponUniLineRateStep_Type=Integer32
_H3cEponUniLineRateStep_Object=MibScalar
h3cEponUniLineRateStep=_H3cEponUniLineRateStep_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,4,2),_H3cEponUniLineRateStep_Type())
h3cEponUniLineRateStep.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniLineRateStep.setStatus(_A)
_H3cEponUniNumberOnOnu_Type=Integer32
_H3cEponUniNumberOnOnu_Object=MibScalar
h3cEponUniNumberOnOnu=_H3cEponUniNumberOnOnu_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,4,3),_H3cEponUniNumberOnOnu_Type())
h3cEponUniNumberOnOnu.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniNumberOnOnu.setStatus(_A)
_H3cEponUniScalarGroup_ObjectIdentity=ObjectIdentity
h3cEponUniScalarGroup=_H3cEponUniScalarGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,42,5,1,5))
_H3cEponUniPortPolicyTable_Object=MibTable
h3cEponUniPortPolicyTable=_H3cEponUniPortPolicyTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,6))
if mibBuilder.loadTexts:h3cEponUniPortPolicyTable.setStatus(_A)
_H3cEponUniPortPolicyEntry_Object=MibTableRow
h3cEponUniPortPolicyEntry=_H3cEponUniPortPolicyEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,6,1))
h3cEponUniPortPolicyEntry.setIndexNames((0,_G,_H),(0,_E,_I))
if mibBuilder.loadTexts:h3cEponUniPortPolicyEntry.setStatus(_A)
class _H3cEponUniPortPolicyStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_H3cEponUniPortPolicyStatus_Type.__name__=_C
_H3cEponUniPortPolicyStatus_Object=MibTableColumn
h3cEponUniPortPolicyStatus=_H3cEponUniPortPolicyStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,6,1,1),_H3cEponUniPortPolicyStatus_Type())
h3cEponUniPortPolicyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniPortPolicyStatus.setStatus(_A)
class _H3cEponUniPortPolicyCir_Type(Integer32):defaultValue=102400
_H3cEponUniPortPolicyCir_Type.__name__=_C
_H3cEponUniPortPolicyCir_Object=MibTableColumn
h3cEponUniPortPolicyCir=_H3cEponUniPortPolicyCir_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,6,1,2),_H3cEponUniPortPolicyCir_Type())
h3cEponUniPortPolicyCir.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniPortPolicyCir.setStatus(_A)
class _H3cEponUniPortPolicyBucketDepth_Type(Integer32):defaultValue=0
_H3cEponUniPortPolicyBucketDepth_Type.__name__=_C
_H3cEponUniPortPolicyBucketDepth_Object=MibTableColumn
h3cEponUniPortPolicyBucketDepth=_H3cEponUniPortPolicyBucketDepth_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,6,1,3),_H3cEponUniPortPolicyBucketDepth_Type())
h3cEponUniPortPolicyBucketDepth.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniPortPolicyBucketDepth.setStatus(_A)
class _H3cEponUniPortPolicyExtraBurst_Type(Integer32):defaultValue=0
_H3cEponUniPortPolicyExtraBurst_Type.__name__=_C
_H3cEponUniPortPolicyExtraBurst_Object=MibTableColumn
h3cEponUniPortPolicyExtraBurst=_H3cEponUniPortPolicyExtraBurst_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,6,1,4),_H3cEponUniPortPolicyExtraBurst_Type())
h3cEponUniPortPolicyExtraBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniPortPolicyExtraBurst.setStatus(_A)
_H3cEponUniPortPolicyInboundCir_Type=Integer32
_H3cEponUniPortPolicyInboundCir_Object=MibTableColumn
h3cEponUniPortPolicyInboundCir=_H3cEponUniPortPolicyInboundCir_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,6,1,5),_H3cEponUniPortPolicyInboundCir_Type())
h3cEponUniPortPolicyInboundCir.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniPortPolicyInboundCir.setStatus(_A)
class _H3cEponUniPortPolicyInboundBucketDepth_Type(Integer32):defaultValue=0
_H3cEponUniPortPolicyInboundBucketDepth_Type.__name__=_C
_H3cEponUniPortPolicyInboundBucketDepth_Object=MibTableColumn
h3cEponUniPortPolicyInboundBucketDepth=_H3cEponUniPortPolicyInboundBucketDepth_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,6,1,6),_H3cEponUniPortPolicyInboundBucketDepth_Type())
h3cEponUniPortPolicyInboundBucketDepth.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniPortPolicyInboundBucketDepth.setStatus(_A)
class _H3cEponUniPortPolicyInboundExtraBurst_Type(Integer32):defaultValue=0
_H3cEponUniPortPolicyInboundExtraBurst_Type.__name__=_C
_H3cEponUniPortPolicyInboundExtraBurst_Object=MibTableColumn
h3cEponUniPortPolicyInboundExtraBurst=_H3cEponUniPortPolicyInboundExtraBurst_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,6,1,7),_H3cEponUniPortPolicyInboundExtraBurst_Type())
h3cEponUniPortPolicyInboundExtraBurst.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniPortPolicyInboundExtraBurst.setStatus(_A)
_H3cEponUniPortPolicyOutboundCir_Type=Integer32
_H3cEponUniPortPolicyOutboundCir_Object=MibTableColumn
h3cEponUniPortPolicyOutboundCir=_H3cEponUniPortPolicyOutboundCir_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,6,1,8),_H3cEponUniPortPolicyOutboundCir_Type())
h3cEponUniPortPolicyOutboundCir.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniPortPolicyOutboundCir.setStatus(_A)
_H3cEponUniPortPolicyOutboundPir_Type=Integer32
_H3cEponUniPortPolicyOutboundPir_Object=MibTableColumn
h3cEponUniPortPolicyOutboundPir=_H3cEponUniPortPolicyOutboundPir_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,6,1,9),_H3cEponUniPortPolicyOutboundPir_Type())
h3cEponUniPortPolicyOutboundPir.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniPortPolicyOutboundPir.setStatus(_A)
_H3cEponUniMulticastTable_Object=MibTable
h3cEponUniMulticastTable=_H3cEponUniMulticastTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,7))
if mibBuilder.loadTexts:h3cEponUniMulticastTable.setStatus(_A)
_H3cEponUniMulticastEntry_Object=MibTableRow
h3cEponUniMulticastEntry=_H3cEponUniMulticastEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,7,1))
h3cEponUniMulticastEntry.setIndexNames((0,_G,_H),(0,_E,_I))
if mibBuilder.loadTexts:h3cEponUniMulticastEntry.setStatus(_A)
class _H3cEponUniMulticastGroupNumber_Type(Integer32):defaultValue=64
_H3cEponUniMulticastGroupNumber_Type.__name__=_C
_H3cEponUniMulticastGroupNumber_Object=MibTableColumn
h3cEponUniMulticastGroupNumber=_H3cEponUniMulticastGroupNumber_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,7,1,1),_H3cEponUniMulticastGroupNumber_Type())
h3cEponUniMulticastGroupNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniMulticastGroupNumber.setStatus(_A)
class _H3cEponUniMulticastVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cEponUniMulticastVlanList_Type.__name__=_J
_H3cEponUniMulticastVlanList_Object=MibTableColumn
h3cEponUniMulticastVlanList=_H3cEponUniMulticastVlanList_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,7,1,2),_H3cEponUniMulticastVlanList_Type())
h3cEponUniMulticastVlanList.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniMulticastVlanList.setStatus(_A)
class _H3cEponUniMulticastStripStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_H3cEponUniMulticastStripStatus_Type.__name__=_C
_H3cEponUniMulticastStripStatus_Object=MibTableColumn
h3cEponUniMulticastStripStatus=_H3cEponUniMulticastStripStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,7,1,3),_H3cEponUniMulticastStripStatus_Type())
h3cEponUniMulticastStripStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniMulticastStripStatus.setStatus(_A)
class _H3cEponUniMulticastFastleave_Type(TruthValue):defaultValue=2
_H3cEponUniMulticastFastleave_Type.__name__=_T
_H3cEponUniMulticastFastleave_Object=MibTableColumn
h3cEponUniMulticastFastleave=_H3cEponUniMulticastFastleave_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,7,1,4),_H3cEponUniMulticastFastleave_Type())
h3cEponUniMulticastFastleave.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniMulticastFastleave.setStatus(_A)
_H3cEponUniTechAbilityTable_Object=MibTable
h3cEponUniTechAbilityTable=_H3cEponUniTechAbilityTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,8))
if mibBuilder.loadTexts:h3cEponUniTechAbilityTable.setStatus(_A)
_H3cEponUniTechAbilityEntry_Object=MibTableRow
h3cEponUniTechAbilityEntry=_H3cEponUniTechAbilityEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,8,1))
h3cEponUniTechAbilityEntry.setIndexNames((0,_G,_H),(0,_E,_I))
if mibBuilder.loadTexts:h3cEponUniTechAbilityEntry.setStatus(_A)
class _H3cEponUniLocalTechAbility_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cEponUniLocalTechAbility_Type.__name__=_J
_H3cEponUniLocalTechAbility_Object=MibTableColumn
h3cEponUniLocalTechAbility=_H3cEponUniLocalTechAbility_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,8,1,1),_H3cEponUniLocalTechAbility_Type())
h3cEponUniLocalTechAbility.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniLocalTechAbility.setStatus(_A)
class _H3cEponUniAdvertisedTechAbility_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cEponUniAdvertisedTechAbility_Type.__name__=_J
_H3cEponUniAdvertisedTechAbility_Object=MibTableColumn
h3cEponUniAdvertisedTechAbility=_H3cEponUniAdvertisedTechAbility_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,8,1,2),_H3cEponUniAdvertisedTechAbility_Type())
h3cEponUniAdvertisedTechAbility.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniAdvertisedTechAbility.setStatus(_A)
_H3cEponUniMulticastControlTable_Object=MibTable
h3cEponUniMulticastControlTable=_H3cEponUniMulticastControlTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,9))
if mibBuilder.loadTexts:h3cEponUniMulticastControlTable.setStatus(_A)
_H3cEponUniMulticastControlEntry_Object=MibTableRow
h3cEponUniMulticastControlEntry=_H3cEponUniMulticastControlEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,9,1))
h3cEponUniMulticastControlEntry.setIndexNames((0,_G,_H),(0,_E,_I),(0,_E,_W))
if mibBuilder.loadTexts:h3cEponUniMulticastControlEntry.setStatus(_A)
_H3cEponUniMulticastVlanIndex_Type=Integer32
_H3cEponUniMulticastVlanIndex_Object=MibTableColumn
h3cEponUniMulticastVlanIndex=_H3cEponUniMulticastVlanIndex_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,9,1,1),_H3cEponUniMulticastVlanIndex_Type())
h3cEponUniMulticastVlanIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniMulticastVlanIndex.setStatus(_A)
class _H3cEponUniMulticastAddressList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cEponUniMulticastAddressList_Type.__name__=_J
_H3cEponUniMulticastAddressList_Object=MibTableColumn
h3cEponUniMulticastAddressList=_H3cEponUniMulticastAddressList_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,9,1,2),_H3cEponUniMulticastAddressList_Type())
h3cEponUniMulticastAddressList.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniMulticastAddressList.setStatus(_A)
class _H3cEponUniMulticastAccessRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('deny',1),(_X,2),(_Y,3)))
_H3cEponUniMulticastAccessRule_Type.__name__=_C
_H3cEponUniMulticastAccessRule_Object=MibTableColumn
h3cEponUniMulticastAccessRule=_H3cEponUniMulticastAccessRule_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,9,1,3),_H3cEponUniMulticastAccessRule_Type())
h3cEponUniMulticastAccessRule.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniMulticastAccessRule.setStatus(_A)
_H3cEponUniMulticastChannelLimit_Type=Integer32
_H3cEponUniMulticastChannelLimit_Object=MibTableColumn
h3cEponUniMulticastChannelLimit=_H3cEponUniMulticastChannelLimit_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,9,1,4),_H3cEponUniMulticastChannelLimit_Type())
h3cEponUniMulticastChannelLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniMulticastChannelLimit.setStatus(_A)
_H3cEponUniMulticastPreTimeSlice_Type=Integer32
_H3cEponUniMulticastPreTimeSlice_Object=MibTableColumn
h3cEponUniMulticastPreTimeSlice=_H3cEponUniMulticastPreTimeSlice_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,9,1,5),_H3cEponUniMulticastPreTimeSlice_Type())
h3cEponUniMulticastPreTimeSlice.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniMulticastPreTimeSlice.setStatus(_A)
_H3cEponUniMulticastPreTimes_Type=Integer32
_H3cEponUniMulticastPreTimes_Object=MibTableColumn
h3cEponUniMulticastPreTimes=_H3cEponUniMulticastPreTimes_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,9,1,6),_H3cEponUniMulticastPreTimes_Type())
h3cEponUniMulticastPreTimes.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniMulticastPreTimes.setStatus(_A)
_H3cEponUniMulticastPreInterval_Type=Integer32
_H3cEponUniMulticastPreInterval_Object=MibTableColumn
h3cEponUniMulticastPreInterval=_H3cEponUniMulticastPreInterval_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,9,1,7),_H3cEponUniMulticastPreInterval_Type())
h3cEponUniMulticastPreInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniMulticastPreInterval.setStatus(_A)
_H3cEponUniMulticastRowStatus_Type=RowStatus
_H3cEponUniMulticastRowStatus_Object=MibTableColumn
h3cEponUniMulticastRowStatus=_H3cEponUniMulticastRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,9,1,8),_H3cEponUniMulticastRowStatus_Type())
h3cEponUniMulticastRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniMulticastRowStatus.setStatus(_A)
_H3cEponUniMulticastIndex_Type=Integer32
_H3cEponUniMulticastIndex_Object=MibTableColumn
h3cEponUniMulticastIndex=_H3cEponUniMulticastIndex_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,9,1,9),_H3cEponUniMulticastIndex_Type())
h3cEponUniMulticastIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cEponUniMulticastIndex.setStatus(_A)
class _H3cEponUniMulticastSourceIpList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cEponUniMulticastSourceIpList_Type.__name__=_J
_H3cEponUniMulticastSourceIpList_Object=MibTableColumn
h3cEponUniMulticastSourceIpList=_H3cEponUniMulticastSourceIpList_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,9,1,10),_H3cEponUniMulticastSourceIpList_Type())
h3cEponUniMulticastSourceIpList.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniMulticastSourceIpList.setStatus(_A)
_H3cEponUniMulticastResetInterval_Type=Integer32
_H3cEponUniMulticastResetInterval_Object=MibTableColumn
h3cEponUniMulticastResetInterval=_H3cEponUniMulticastResetInterval_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,9,1,11),_H3cEponUniMulticastResetInterval_Type())
h3cEponUniMulticastResetInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniMulticastResetInterval.setStatus(_A)
_H3cEponUniQosIndexNextTable_Object=MibTable
h3cEponUniQosIndexNextTable=_H3cEponUniQosIndexNextTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,10))
if mibBuilder.loadTexts:h3cEponUniQosIndexNextTable.setStatus(_A)
_H3cEponUniQosIndexNextEntry_Object=MibTableRow
h3cEponUniQosIndexNextEntry=_H3cEponUniQosIndexNextEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,10,1))
h3cEponUniQosIndexNextEntry.setIndexNames((0,_G,_H),(0,_E,_I))
if mibBuilder.loadTexts:h3cEponUniQosIndexNextEntry.setStatus(_A)
_H3cEponUniQosConfIndexNext_Type=Integer32
_H3cEponUniQosConfIndexNext_Object=MibTableColumn
h3cEponUniQosConfIndexNext=_H3cEponUniQosConfIndexNext_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,10,1,1),_H3cEponUniQosConfIndexNext_Type())
h3cEponUniQosConfIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniQosConfIndexNext.setStatus(_A)
_H3cEponUniQosConfTable_Object=MibTable
h3cEponUniQosConfTable=_H3cEponUniQosConfTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,11))
if mibBuilder.loadTexts:h3cEponUniQosConfTable.setStatus(_A)
_H3cEponUniQosConfEntry_Object=MibTableRow
h3cEponUniQosConfEntry=_H3cEponUniQosConfEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,11,1))
h3cEponUniQosConfEntry.setIndexNames((0,_G,_H),(0,_E,_I),(0,_E,_Q))
if mibBuilder.loadTexts:h3cEponUniQosConfEntry.setStatus(_A)
_H3cEponUniQosConfIndex_Type=Integer32
_H3cEponUniQosConfIndex_Object=MibTableColumn
h3cEponUniQosConfIndex=_H3cEponUniQosConfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,11,1,1),_H3cEponUniQosConfIndex_Type())
h3cEponUniQosConfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cEponUniQosConfIndex.setStatus(_A)
_H3cEponUniQosConfRuleIndexNext_Type=Integer32
_H3cEponUniQosConfRuleIndexNext_Object=MibTableColumn
h3cEponUniQosConfRuleIndexNext=_H3cEponUniQosConfRuleIndexNext_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,11,1,2),_H3cEponUniQosConfRuleIndexNext_Type())
h3cEponUniQosConfRuleIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniQosConfRuleIndexNext.setStatus(_A)
_H3cEponUniQosConfMappedQueue_Type=Integer32
_H3cEponUniQosConfMappedQueue_Object=MibTableColumn
h3cEponUniQosConfMappedQueue=_H3cEponUniQosConfMappedQueue_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,11,1,3),_H3cEponUniQosConfMappedQueue_Type())
h3cEponUniQosConfMappedQueue.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniQosConfMappedQueue.setStatus(_A)
_H3cEponUniQosConfMarkedPriority_Type=Integer32
_H3cEponUniQosConfMarkedPriority_Object=MibTableColumn
h3cEponUniQosConfMarkedPriority=_H3cEponUniQosConfMarkedPriority_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,11,1,4),_H3cEponUniQosConfMarkedPriority_Type())
h3cEponUniQosConfMarkedPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniQosConfMarkedPriority.setStatus(_A)
_H3cEponUniQosConfRowStatus_Type=RowStatus
_H3cEponUniQosConfRowStatus_Object=MibTableColumn
h3cEponUniQosConfRowStatus=_H3cEponUniQosConfRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,11,1,5),_H3cEponUniQosConfRowStatus_Type())
h3cEponUniQosConfRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniQosConfRowStatus.setStatus(_A)
_H3cEponUniQosRuleTable_Object=MibTable
h3cEponUniQosRuleTable=_H3cEponUniQosRuleTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,12))
if mibBuilder.loadTexts:h3cEponUniQosRuleTable.setStatus(_A)
_H3cEponUniQosRuleEntry_Object=MibTableRow
h3cEponUniQosRuleEntry=_H3cEponUniQosRuleEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,12,1))
h3cEponUniQosRuleEntry.setIndexNames((0,_G,_H),(0,_E,_I),(0,_E,_Q),(0,_E,_Z))
if mibBuilder.loadTexts:h3cEponUniQosRuleEntry.setStatus(_A)
class _H3cEponUniQosRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_H3cEponUniQosRuleIndex_Type.__name__=_C
_H3cEponUniQosRuleIndex_Object=MibTableColumn
h3cEponUniQosRuleIndex=_H3cEponUniQosRuleIndex_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,12,1,1),_H3cEponUniQosRuleIndex_Type())
h3cEponUniQosRuleIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cEponUniQosRuleIndex.setStatus(_A)
class _H3cEponUniQosRuleSelector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('dstmac',1),('srcmac',2),('ethernetpriority',3),('vlanid',4),('ethernettype',5),('dstip',6),('srcip',7),('ipprototype',8),('ipv4tosdscp',9),('ipv6precedence',10),('srcport',11),('dstport',12)))
_H3cEponUniQosRuleSelector_Type.__name__=_C
_H3cEponUniQosRuleSelector_Object=MibTableColumn
h3cEponUniQosRuleSelector=_H3cEponUniQosRuleSelector_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,12,1,2),_H3cEponUniQosRuleSelector_Type())
h3cEponUniQosRuleSelector.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniQosRuleSelector.setStatus(_A)
_H3cEponUniQosRuleValue_Type=Integer32
_H3cEponUniQosRuleValue_Object=MibTableColumn
h3cEponUniQosRuleValue=_H3cEponUniQosRuleValue_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,12,1,3),_H3cEponUniQosRuleValue_Type())
h3cEponUniQosRuleValue.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniQosRuleValue.setStatus(_A)
_H3cEponUniQosRuleMacAddress_Type=MacAddress
_H3cEponUniQosRuleMacAddress_Object=MibTableColumn
h3cEponUniQosRuleMacAddress=_H3cEponUniQosRuleMacAddress_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,12,1,4),_H3cEponUniQosRuleMacAddress_Type())
h3cEponUniQosRuleMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniQosRuleMacAddress.setStatus(_A)
class _H3cEponUniQosRuleOperator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('nevermatch',1),('equal',2),('notequal',3),('lessthanequal',4),('greaterthanequal',5),('fieldexist',6),('fieldnotexist',7),('alwaysmatch',8)))
_H3cEponUniQosRuleOperator_Type.__name__=_C
_H3cEponUniQosRuleOperator_Object=MibTableColumn
h3cEponUniQosRuleOperator=_H3cEponUniQosRuleOperator_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,12,1,5),_H3cEponUniQosRuleOperator_Type())
h3cEponUniQosRuleOperator.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniQosRuleOperator.setStatus(_A)
_H3cEponUniQosRuleRowStatus_Type=RowStatus
_H3cEponUniQosRuleRowStatus_Object=MibTableColumn
h3cEponUniQosRuleRowStatus=_H3cEponUniQosRuleRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,12,1,6),_H3cEponUniQosRuleRowStatus_Type())
h3cEponUniQosRuleRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniQosRuleRowStatus.setStatus(_A)
_H3cEponUniMirrorGroupTable_Object=MibTable
h3cEponUniMirrorGroupTable=_H3cEponUniMirrorGroupTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,13))
if mibBuilder.loadTexts:h3cEponUniMirrorGroupTable.setStatus(_A)
_H3cEponUniMirrorGroupEntry_Object=MibTableRow
h3cEponUniMirrorGroupEntry=_H3cEponUniMirrorGroupEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,13,1))
h3cEponUniMirrorGroupEntry.setIndexNames((0,_G,_H),(0,_E,_a))
if mibBuilder.loadTexts:h3cEponUniMirrorGroupEntry.setStatus(_A)
_H3cEponUniMirrorGroupID_Type=Integer32
_H3cEponUniMirrorGroupID_Object=MibTableColumn
h3cEponUniMirrorGroupID=_H3cEponUniMirrorGroupID_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,13,1,1),_H3cEponUniMirrorGroupID_Type())
h3cEponUniMirrorGroupID.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cEponUniMirrorGroupID.setStatus(_A)
_H3cEponUniMirrorInboundPortList_Type=OctetString
_H3cEponUniMirrorInboundPortList_Object=MibTableColumn
h3cEponUniMirrorInboundPortList=_H3cEponUniMirrorInboundPortList_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,13,1,2),_H3cEponUniMirrorInboundPortList_Type())
h3cEponUniMirrorInboundPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEponUniMirrorInboundPortList.setStatus(_A)
_H3cEponUniMirrorOutboundPortList_Type=OctetString
_H3cEponUniMirrorOutboundPortList_Object=MibTableColumn
h3cEponUniMirrorOutboundPortList=_H3cEponUniMirrorOutboundPortList_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,13,1,3),_H3cEponUniMirrorOutboundPortList_Type())
h3cEponUniMirrorOutboundPortList.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniMirrorOutboundPortList.setStatus(_A)
_H3cEponUniMonitorPort_Type=Integer32
_H3cEponUniMonitorPort_Object=MibTableColumn
h3cEponUniMonitorPort=_H3cEponUniMonitorPort_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,13,1,4),_H3cEponUniMonitorPort_Type())
h3cEponUniMonitorPort.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniMonitorPort.setStatus(_A)
_H3cEponUniMirrorRowStatus_Type=RowStatus
_H3cEponUniMirrorRowStatus_Object=MibTableColumn
h3cEponUniMirrorRowStatus=_H3cEponUniMirrorRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,13,1,5),_H3cEponUniMirrorRowStatus_Type())
h3cEponUniMirrorRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cEponUniMirrorRowStatus.setStatus(_A)
_H3cEponUniMirrorGroupIdNextTable_Object=MibTable
h3cEponUniMirrorGroupIdNextTable=_H3cEponUniMirrorGroupIdNextTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,14))
if mibBuilder.loadTexts:h3cEponUniMirrorGroupIdNextTable.setStatus(_A)
_H3cEponUniMirrorGroupIdNextEntry_Object=MibTableRow
h3cEponUniMirrorGroupIdNextEntry=_H3cEponUniMirrorGroupIdNextEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,14,1))
h3cEponUniMirrorGroupIdNextEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cEponUniMirrorGroupIdNextEntry.setStatus(_A)
_H3cEponUniMirrorGroupIDNext_Type=Integer32
_H3cEponUniMirrorGroupIDNext_Object=MibTableColumn
h3cEponUniMirrorGroupIDNext=_H3cEponUniMirrorGroupIDNext_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,14,1,1),_H3cEponUniMirrorGroupIDNext_Type())
h3cEponUniMirrorGroupIDNext.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniMirrorGroupIDNext.setStatus(_A)
_H3cEponUniMulticastCtrlInfoTable_Object=MibTable
h3cEponUniMulticastCtrlInfoTable=_H3cEponUniMulticastCtrlInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,15))
if mibBuilder.loadTexts:h3cEponUniMulticastCtrlInfoTable.setStatus(_A)
_H3cEponUniMulticastCtrlInfoEntry_Object=MibTableRow
h3cEponUniMulticastCtrlInfoEntry=_H3cEponUniMulticastCtrlInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,15,1))
h3cEponUniMulticastCtrlInfoEntry.setIndexNames((0,_G,_H),(0,_E,_I),(0,_E,_b),(0,_E,_c))
if mibBuilder.loadTexts:h3cEponUniMulticastCtrlInfoEntry.setStatus(_A)
_H3cEponUniMultActVlan_Type=Integer32
_H3cEponUniMultActVlan_Object=MibTableColumn
h3cEponUniMultActVlan=_H3cEponUniMultActVlan_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,15,1,1),_H3cEponUniMultActVlan_Type())
h3cEponUniMultActVlan.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cEponUniMultActVlan.setStatus(_A)
_H3cEponUniMultActAddress_Type=IpAddress
_H3cEponUniMultActAddress_Object=MibTableColumn
h3cEponUniMultActAddress=_H3cEponUniMultActAddress_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,15,1,2),_H3cEponUniMultActAddress_Type())
h3cEponUniMultActAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cEponUniMultActAddress.setStatus(_A)
class _H3cEponUniMultActAccessRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('deny',1),(_X,2),(_Y,3)))
_H3cEponUniMultActAccessRule_Type.__name__=_C
_H3cEponUniMultActAccessRule_Object=MibTableColumn
h3cEponUniMultActAccessRule=_H3cEponUniMultActAccessRule_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,15,1,3),_H3cEponUniMultActAccessRule_Type())
h3cEponUniMultActAccessRule.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniMultActAccessRule.setStatus(_A)
_H3cEponUniMultActPreTimes_Type=Integer32
_H3cEponUniMultActPreTimes_Object=MibTableColumn
h3cEponUniMultActPreTimes=_H3cEponUniMultActPreTimes_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,15,1,4),_H3cEponUniMultActPreTimes_Type())
h3cEponUniMultActPreTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniMultActPreTimes.setStatus(_A)
_H3cEponUniMultActPreRemain_Type=Integer32
_H3cEponUniMultActPreRemain_Object=MibTableColumn
h3cEponUniMultActPreRemain=_H3cEponUniMultActPreRemain_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,15,1,5),_H3cEponUniMultActPreRemain_Type())
h3cEponUniMultActPreRemain.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniMultActPreRemain.setStatus(_A)
_H3cEponUniMulticastIndexNextTable_Object=MibTable
h3cEponUniMulticastIndexNextTable=_H3cEponUniMulticastIndexNextTable_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,16))
if mibBuilder.loadTexts:h3cEponUniMulticastIndexNextTable.setStatus(_A)
_H3cEponUniMulticastIndexNextEntry_Object=MibTableRow
h3cEponUniMulticastIndexNextEntry=_H3cEponUniMulticastIndexNextEntry_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,16,1))
h3cEponUniMulticastIndexNextEntry.setIndexNames((0,_G,_H),(0,_E,_I))
if mibBuilder.loadTexts:h3cEponUniMulticastIndexNextEntry.setStatus(_A)
_H3cEponUniMulticastConfIndexNext_Type=Integer32
_H3cEponUniMulticastConfIndexNext_Object=MibTableColumn
h3cEponUniMulticastConfIndexNext=_H3cEponUniMulticastConfIndexNext_Object((1,3,6,1,4,1,43,45,1,10,2,42,5,1,16,1,1),_H3cEponUniMulticastConfIndexNext_Type())
h3cEponUniMulticastConfIndexNext.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cEponUniMulticastConfIndexNext.setStatus(_A)
_H3cEponUniTrap_ObjectIdentity=ObjectIdentity
h3cEponUniTrap=_H3cEponUniTrap_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,42,5,2))
_H3cEponUniTrapPrefix_ObjectIdentity=ObjectIdentity
h3cEponUniTrapPrefix=_H3cEponUniTrapPrefix_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,42,5,2,0))
h3cEponUniLinkUpTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,5,2,0,1))
h3cEponUniLinkUpTrap.setObjects(*((_G,_H),(_G,_P),(_E,_I),(_E,_R),(_E,_S)))
if mibBuilder.loadTexts:h3cEponUniLinkUpTrap.setStatus(_A)
h3cEponUniLinkDownTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,42,5,2,0,2))
h3cEponUniLinkDownTrap.setObjects(*((_G,_H),(_G,_P),(_E,_I),(_E,_R),(_E,_S)))
if mibBuilder.loadTexts:h3cEponUniLinkDownTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'h3cEponUni':h3cEponUni,'h3cEponUniSysMan':h3cEponUniSysMan,'h3cEponUniSysManTable':h3cEponUniSysManTable,'h3cEponUniSysManEntry':h3cEponUniSysManEntry,_I:h3cEponUniIndex,_R:h3cEponUniDescr,_S:h3cEponUniAdminStatus,'h3cEponUniMdi':h3cEponUniMdi,'h3cEponUniPriority':h3cEponUniPriority,'h3cEponUniVlanType':h3cEponUniVlanType,'h3cEponUniAccessVlan':h3cEponUniAccessVlan,'h3cEponUniTrunkPvid':h3cEponUniTrunkPvid,'h3cEponUniVLANTrunkAllowListLow':h3cEponUniVLANTrunkAllowListLow,'h3cEponUniVLANTrunkAllowListHigh':h3cEponUniVLANTrunkAllowListHigh,'h3cEponUniInboundLineRate':h3cEponUniInboundLineRate,'h3cEponUniOutboundLineRate':h3cEponUniOutboundLineRate,'h3cEponUniFlowControl':h3cEponUniFlowControl,'h3cEponUniSpeed':h3cEponUniSpeed,'h3cEponUniDuplex':h3cEponUniDuplex,'h3cEponUniVlanVPNStatus':h3cEponUniVlanVPNStatus,'h3cEponUniCountReset':h3cEponUniCountReset,'h3cEponUniPortIsolate':h3cEponUniPortIsolate,'h3cEponUniVlanConfiguration':h3cEponUniVlanConfiguration,'h3cEponUniAutoNegotiation':h3cEponUniAutoNegotiation,'h3cEponUniRestartAutoNeg':h3cEponUniRestartAutoNeg,'h3cEponUniLinkStatus':h3cEponUniLinkStatus,'h3cEponUniInterfaceType':h3cEponUniInterfaceType,'h3cEponUniVitualCableTest':h3cEponUniVitualCableTest,'h3cEponUniVCTCableStatus':h3cEponUniVCTCableStatus,'h3cEponUniVCTCableLength':h3cEponUniVCTCableLength,'h3cEponUniVCTImpedanceMismatch':h3cEponUniVCTImpedanceMismatch,'h3cEponUniVCTPairSkew':h3cEponUniVCTPairSkew,'h3cEponUniVCTPairSwap':h3cEponUniVCTPairSwap,'h3cEponUniVCTPolaritySwap':h3cEponUniVCTPolaritySwap,'h3cEponUniVCTInsertionLoss':h3cEponUniVCTInsertionLoss,'h3cEponUniVCTReturnLoss':h3cEponUniVCTReturnLoss,'h3cEponUniVCTNearendCrosstalk':h3cEponUniVCTNearendCrosstalk,'h3cEponUniCountTable':h3cEponUniCountTable,'h3cEponUniCountEntry':h3cEponUniCountEntry,'h3cEponUniInStatsPkts':h3cEponUniInStatsPkts,'h3cEponUniInStatsUnicastPkts':h3cEponUniInStatsUnicastPkts,'h3cEponUniInStatsBroadcastPkts':h3cEponUniInStatsBroadcastPkts,'h3cEponUniInStatsMulticastPkts':h3cEponUniInStatsMulticastPkts,'h3cEponUniInPausePkts':h3cEponUniInPausePkts,'h3cEponUniInTotalErrors':h3cEponUniInTotalErrors,'h3cEponUniInStatsCRCAlignErrors':h3cEponUniInStatsCRCAlignErrors,'h3cEponUniInStatsUndersizePkts':h3cEponUniInStatsUndersizePkts,'h3cEponUniInStatsOversizePkts':h3cEponUniInStatsOversizePkts,'h3cEponUniInErrorbyOther':h3cEponUniInErrorbyOther,'h3cEponUniOutStatsPkts':h3cEponUniOutStatsPkts,'h3cEponUniOutStatsUnicastPkts':h3cEponUniOutStatsUnicastPkts,'h3cEponUniOutStatsBroadcastPkts':h3cEponUniOutStatsBroadcastPkts,'h3cEponUniOutStatsMulticastPkts':h3cEponUniOutStatsMulticastPkts,'h3cEponUniOutStatsPausePkts':h3cEponUniOutStatsPausePkts,'h3cEponUniOutTotalErrors':h3cEponUniOutTotalErrors,'h3cEponUniOutStatsCollisions':h3cEponUniOutStatsCollisions,'h3cEponUniOutDelayExceededDiscards':h3cEponUniOutDelayExceededDiscards,'h3cEponUniOutErrorbyOther':h3cEponUniOutErrorbyOther,'h3cEponUniOutDroppedFrames':h3cEponUniOutDroppedFrames,'h3cEponUniIgmpInfoTable':h3cEponUniIgmpInfoTable,'h3cEponUniIgmpInfoEntry':h3cEponUniIgmpInfoEntry,_V:h3cEponUniMacIndex,'h3cEponUniIgmpMacAddress':h3cEponUniIgmpMacAddress,'h3cEponUniIgmpVlanId':h3cEponUniIgmpVlanId,'h3cEponUniParaMan':h3cEponUniParaMan,'h3cEponUniLineRateMax':h3cEponUniLineRateMax,'h3cEponUniLineRateStep':h3cEponUniLineRateStep,'h3cEponUniNumberOnOnu':h3cEponUniNumberOnOnu,'h3cEponUniScalarGroup':h3cEponUniScalarGroup,'h3cEponUniPortPolicyTable':h3cEponUniPortPolicyTable,'h3cEponUniPortPolicyEntry':h3cEponUniPortPolicyEntry,'h3cEponUniPortPolicyStatus':h3cEponUniPortPolicyStatus,'h3cEponUniPortPolicyCir':h3cEponUniPortPolicyCir,'h3cEponUniPortPolicyBucketDepth':h3cEponUniPortPolicyBucketDepth,'h3cEponUniPortPolicyExtraBurst':h3cEponUniPortPolicyExtraBurst,'h3cEponUniPortPolicyInboundCir':h3cEponUniPortPolicyInboundCir,'h3cEponUniPortPolicyInboundBucketDepth':h3cEponUniPortPolicyInboundBucketDepth,'h3cEponUniPortPolicyInboundExtraBurst':h3cEponUniPortPolicyInboundExtraBurst,'h3cEponUniPortPolicyOutboundCir':h3cEponUniPortPolicyOutboundCir,'h3cEponUniPortPolicyOutboundPir':h3cEponUniPortPolicyOutboundPir,'h3cEponUniMulticastTable':h3cEponUniMulticastTable,'h3cEponUniMulticastEntry':h3cEponUniMulticastEntry,'h3cEponUniMulticastGroupNumber':h3cEponUniMulticastGroupNumber,'h3cEponUniMulticastVlanList':h3cEponUniMulticastVlanList,'h3cEponUniMulticastStripStatus':h3cEponUniMulticastStripStatus,'h3cEponUniMulticastFastleave':h3cEponUniMulticastFastleave,'h3cEponUniTechAbilityTable':h3cEponUniTechAbilityTable,'h3cEponUniTechAbilityEntry':h3cEponUniTechAbilityEntry,'h3cEponUniLocalTechAbility':h3cEponUniLocalTechAbility,'h3cEponUniAdvertisedTechAbility':h3cEponUniAdvertisedTechAbility,'h3cEponUniMulticastControlTable':h3cEponUniMulticastControlTable,'h3cEponUniMulticastControlEntry':h3cEponUniMulticastControlEntry,'h3cEponUniMulticastVlanIndex':h3cEponUniMulticastVlanIndex,'h3cEponUniMulticastAddressList':h3cEponUniMulticastAddressList,'h3cEponUniMulticastAccessRule':h3cEponUniMulticastAccessRule,'h3cEponUniMulticastChannelLimit':h3cEponUniMulticastChannelLimit,'h3cEponUniMulticastPreTimeSlice':h3cEponUniMulticastPreTimeSlice,'h3cEponUniMulticastPreTimes':h3cEponUniMulticastPreTimes,'h3cEponUniMulticastPreInterval':h3cEponUniMulticastPreInterval,'h3cEponUniMulticastRowStatus':h3cEponUniMulticastRowStatus,_W:h3cEponUniMulticastIndex,'h3cEponUniMulticastSourceIpList':h3cEponUniMulticastSourceIpList,'h3cEponUniMulticastResetInterval':h3cEponUniMulticastResetInterval,'h3cEponUniQosIndexNextTable':h3cEponUniQosIndexNextTable,'h3cEponUniQosIndexNextEntry':h3cEponUniQosIndexNextEntry,'h3cEponUniQosConfIndexNext':h3cEponUniQosConfIndexNext,'h3cEponUniQosConfTable':h3cEponUniQosConfTable,'h3cEponUniQosConfEntry':h3cEponUniQosConfEntry,_Q:h3cEponUniQosConfIndex,'h3cEponUniQosConfRuleIndexNext':h3cEponUniQosConfRuleIndexNext,'h3cEponUniQosConfMappedQueue':h3cEponUniQosConfMappedQueue,'h3cEponUniQosConfMarkedPriority':h3cEponUniQosConfMarkedPriority,'h3cEponUniQosConfRowStatus':h3cEponUniQosConfRowStatus,'h3cEponUniQosRuleTable':h3cEponUniQosRuleTable,'h3cEponUniQosRuleEntry':h3cEponUniQosRuleEntry,_Z:h3cEponUniQosRuleIndex,'h3cEponUniQosRuleSelector':h3cEponUniQosRuleSelector,'h3cEponUniQosRuleValue':h3cEponUniQosRuleValue,'h3cEponUniQosRuleMacAddress':h3cEponUniQosRuleMacAddress,'h3cEponUniQosRuleOperator':h3cEponUniQosRuleOperator,'h3cEponUniQosRuleRowStatus':h3cEponUniQosRuleRowStatus,'h3cEponUniMirrorGroupTable':h3cEponUniMirrorGroupTable,'h3cEponUniMirrorGroupEntry':h3cEponUniMirrorGroupEntry,_a:h3cEponUniMirrorGroupID,'h3cEponUniMirrorInboundPortList':h3cEponUniMirrorInboundPortList,'h3cEponUniMirrorOutboundPortList':h3cEponUniMirrorOutboundPortList,'h3cEponUniMonitorPort':h3cEponUniMonitorPort,'h3cEponUniMirrorRowStatus':h3cEponUniMirrorRowStatus,'h3cEponUniMirrorGroupIdNextTable':h3cEponUniMirrorGroupIdNextTable,'h3cEponUniMirrorGroupIdNextEntry':h3cEponUniMirrorGroupIdNextEntry,'h3cEponUniMirrorGroupIDNext':h3cEponUniMirrorGroupIDNext,'h3cEponUniMulticastCtrlInfoTable':h3cEponUniMulticastCtrlInfoTable,'h3cEponUniMulticastCtrlInfoEntry':h3cEponUniMulticastCtrlInfoEntry,_b:h3cEponUniMultActVlan,_c:h3cEponUniMultActAddress,'h3cEponUniMultActAccessRule':h3cEponUniMultActAccessRule,'h3cEponUniMultActPreTimes':h3cEponUniMultActPreTimes,'h3cEponUniMultActPreRemain':h3cEponUniMultActPreRemain,'h3cEponUniMulticastIndexNextTable':h3cEponUniMulticastIndexNextTable,'h3cEponUniMulticastIndexNextEntry':h3cEponUniMulticastIndexNextEntry,'h3cEponUniMulticastConfIndexNext':h3cEponUniMulticastConfIndexNext,'h3cEponUniTrap':h3cEponUniTrap,'h3cEponUniTrapPrefix':h3cEponUniTrapPrefix,'h3cEponUniLinkUpTrap':h3cEponUniLinkUpTrap,'h3cEponUniLinkDownTrap':h3cEponUniLinkDownTrap})