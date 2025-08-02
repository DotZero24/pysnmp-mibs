_X='zxr10DiffServClsMatchSequence'
_W='zxr10DiffServClsMapName'
_V='zxr10DiffServVPNName'
_U='zxr10DiffServVPNMode'
_T='zxr10DiffServCIPNo'
_S='zxr10DiffServPWName'
_R='zxr10DiffServTunnelNo'
_Q='zxr10DiffServFlowServiceClass'
_P='zxr10DiffServFlowPatternName'
_O='zxr10DiffServDropPatternColor'
_N='zxr10DiffServDropPatternName'
_M='zxr10DiffServDomainOutToSType'
_L='zxr10DiffServDomainOutColor'
_K='zxr10DiffServDomainOutServClass'
_J='zxr10DiffServDomainOutName'
_I='zxr10DiffServDomainInToSValue'
_H='zxr10DiffServDomainInToSType'
_G='zxr10DiffServDomainInName'
_F='DisplayString'
_E='ifIndex'
_D='IF-MIB'
_C='ZXR10-DIFFSERV-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
zxr10DiffServ=ModuleIdentity((1,3,6,1,4,1,3902,3,101,8))
class DisplayString(OctetString):0
class DiffServPacketTos(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ip-dscp',1),('vlan-8021p',2),('mpls-exp',3)))
class DiffServClass(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('cs7',0),('cs6',1),('ef',2),('af4',3),('af3',4),('af2',5),('af1',6),('be',7)))
class DiffServColor(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('green',0),('yellow',1),('red',2)))
class DiffServScheuldingMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('pq',1),('wfq',2),('wrr',3),('dwrr',4)))
class DiffServDroppingMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wred',1),('tail-drop',2)))
class DiffServTunnelingMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('uniform',1),('pipe',2),('short-pipe',3)))
class DiffServPolicingAction(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('discard',1),('pass',2),('remark-pass',3)))
class DiffServTosTrustType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('trust-8021p',1),('trust-dscp',2),('trust-exp',3)))
class DiffServPolicingMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('blind',1),('aware',2)))
class DiffServVPNMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('vpls',1),('vll',2),('vls',3),('vlan-vll',4)))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_Zxr10_ObjectIdentity=ObjectIdentity
zxr10=_Zxr10_ObjectIdentity((1,3,6,1,4,1,3902,3))
_Zxr10protocol_ObjectIdentity=ObjectIdentity
zxr10protocol=_Zxr10protocol_ObjectIdentity((1,3,6,1,4,1,3902,3,101))
_Zxr10DiffServDomainInTable_Object=MibTable
zxr10DiffServDomainInTable=_Zxr10DiffServDomainInTable_Object((1,3,6,1,4,1,3902,3,101,8,1))
if mibBuilder.loadTexts:zxr10DiffServDomainInTable.setStatus(_A)
_Zxr10DiffServDomainInEntry_Object=MibTableRow
zxr10DiffServDomainInEntry=_Zxr10DiffServDomainInEntry_Object((1,3,6,1,4,1,3902,3,101,8,1,1))
zxr10DiffServDomainInEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:zxr10DiffServDomainInEntry.setStatus(_A)
_Zxr10DiffServDomainInName_Type=DisplayString
_Zxr10DiffServDomainInName_Object=MibTableColumn
zxr10DiffServDomainInName=_Zxr10DiffServDomainInName_Object((1,3,6,1,4,1,3902,3,101,8,1,1,1),_Zxr10DiffServDomainInName_Type())
zxr10DiffServDomainInName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServDomainInName.setStatus(_A)
_Zxr10DiffServDomainInToSType_Type=DiffServPacketTos
_Zxr10DiffServDomainInToSType_Object=MibTableColumn
zxr10DiffServDomainInToSType=_Zxr10DiffServDomainInToSType_Object((1,3,6,1,4,1,3902,3,101,8,1,1,2),_Zxr10DiffServDomainInToSType_Type())
zxr10DiffServDomainInToSType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServDomainInToSType.setStatus(_A)
_Zxr10DiffServDomainInToSValue_Type=Integer32
_Zxr10DiffServDomainInToSValue_Object=MibTableColumn
zxr10DiffServDomainInToSValue=_Zxr10DiffServDomainInToSValue_Object((1,3,6,1,4,1,3902,3,101,8,1,1,3),_Zxr10DiffServDomainInToSValue_Type())
zxr10DiffServDomainInToSValue.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServDomainInToSValue.setStatus(_A)
_Zxr10DiffServDomainInServClass_Type=DiffServClass
_Zxr10DiffServDomainInServClass_Object=MibTableColumn
zxr10DiffServDomainInServClass=_Zxr10DiffServDomainInServClass_Object((1,3,6,1,4,1,3902,3,101,8,1,1,4),_Zxr10DiffServDomainInServClass_Type())
zxr10DiffServDomainInServClass.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServDomainInServClass.setStatus(_A)
_Zxr10DiffServDomainInColor_Type=DiffServColor
_Zxr10DiffServDomainInColor_Object=MibTableColumn
zxr10DiffServDomainInColor=_Zxr10DiffServDomainInColor_Object((1,3,6,1,4,1,3902,3,101,8,1,1,5),_Zxr10DiffServDomainInColor_Type())
zxr10DiffServDomainInColor.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServDomainInColor.setStatus(_A)
_Zxr10DiffServDomainOutTable_Object=MibTable
zxr10DiffServDomainOutTable=_Zxr10DiffServDomainOutTable_Object((1,3,6,1,4,1,3902,3,101,8,2))
if mibBuilder.loadTexts:zxr10DiffServDomainOutTable.setStatus(_A)
_Zxr10DiffServDomainOutEntry_Object=MibTableRow
zxr10DiffServDomainOutEntry=_Zxr10DiffServDomainOutEntry_Object((1,3,6,1,4,1,3902,3,101,8,2,1))
zxr10DiffServDomainOutEntry.setIndexNames((0,_C,_J),(0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:zxr10DiffServDomainOutEntry.setStatus(_A)
_Zxr10DiffServDomainOutName_Type=DisplayString
_Zxr10DiffServDomainOutName_Object=MibTableColumn
zxr10DiffServDomainOutName=_Zxr10DiffServDomainOutName_Object((1,3,6,1,4,1,3902,3,101,8,2,1,1),_Zxr10DiffServDomainOutName_Type())
zxr10DiffServDomainOutName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServDomainOutName.setStatus(_A)
_Zxr10DiffServDomainOutServClass_Type=DiffServClass
_Zxr10DiffServDomainOutServClass_Object=MibTableColumn
zxr10DiffServDomainOutServClass=_Zxr10DiffServDomainOutServClass_Object((1,3,6,1,4,1,3902,3,101,8,2,1,2),_Zxr10DiffServDomainOutServClass_Type())
zxr10DiffServDomainOutServClass.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServDomainOutServClass.setStatus(_A)
_Zxr10DiffServDomainOutColor_Type=DiffServColor
_Zxr10DiffServDomainOutColor_Object=MibTableColumn
zxr10DiffServDomainOutColor=_Zxr10DiffServDomainOutColor_Object((1,3,6,1,4,1,3902,3,101,8,2,1,3),_Zxr10DiffServDomainOutColor_Type())
zxr10DiffServDomainOutColor.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServDomainOutColor.setStatus(_A)
_Zxr10DiffServDomainOutToSType_Type=DiffServPacketTos
_Zxr10DiffServDomainOutToSType_Object=MibTableColumn
zxr10DiffServDomainOutToSType=_Zxr10DiffServDomainOutToSType_Object((1,3,6,1,4,1,3902,3,101,8,2,1,4),_Zxr10DiffServDomainOutToSType_Type())
zxr10DiffServDomainOutToSType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServDomainOutToSType.setStatus(_A)
_Zxr10DiffServDomainOutToSValue_Type=Integer32
_Zxr10DiffServDomainOutToSValue_Object=MibTableColumn
zxr10DiffServDomainOutToSValue=_Zxr10DiffServDomainOutToSValue_Object((1,3,6,1,4,1,3902,3,101,8,2,1,5),_Zxr10DiffServDomainOutToSValue_Type())
zxr10DiffServDomainOutToSValue.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServDomainOutToSValue.setStatus(_A)
_Zxr10DiffServDropPatternTable_Object=MibTable
zxr10DiffServDropPatternTable=_Zxr10DiffServDropPatternTable_Object((1,3,6,1,4,1,3902,3,101,8,3))
if mibBuilder.loadTexts:zxr10DiffServDropPatternTable.setStatus(_A)
_Zxr10DiffServDropPatternEntry_Object=MibTableRow
zxr10DiffServDropPatternEntry=_Zxr10DiffServDropPatternEntry_Object((1,3,6,1,4,1,3902,3,101,8,3,1))
zxr10DiffServDropPatternEntry.setIndexNames((0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:zxr10DiffServDropPatternEntry.setStatus(_A)
_Zxr10DiffServDropPatternName_Type=DisplayString
_Zxr10DiffServDropPatternName_Object=MibTableColumn
zxr10DiffServDropPatternName=_Zxr10DiffServDropPatternName_Object((1,3,6,1,4,1,3902,3,101,8,3,1,1),_Zxr10DiffServDropPatternName_Type())
zxr10DiffServDropPatternName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServDropPatternName.setStatus(_A)
_Zxr10DiffServDropPatternColor_Type=DiffServColor
_Zxr10DiffServDropPatternColor_Object=MibTableColumn
zxr10DiffServDropPatternColor=_Zxr10DiffServDropPatternColor_Object((1,3,6,1,4,1,3902,3,101,8,3,1,2),_Zxr10DiffServDropPatternColor_Type())
zxr10DiffServDropPatternColor.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServDropPatternColor.setStatus(_A)
_Zxr10DiffServDropPatternMode_Type=DiffServDroppingMode
_Zxr10DiffServDropPatternMode_Object=MibTableColumn
zxr10DiffServDropPatternMode=_Zxr10DiffServDropPatternMode_Object((1,3,6,1,4,1,3902,3,101,8,3,1,3),_Zxr10DiffServDropPatternMode_Type())
zxr10DiffServDropPatternMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServDropPatternMode.setStatus(_A)
_Zxr10DiffServDropLowThreshold_Type=Integer32
_Zxr10DiffServDropLowThreshold_Object=MibTableColumn
zxr10DiffServDropLowThreshold=_Zxr10DiffServDropLowThreshold_Object((1,3,6,1,4,1,3902,3,101,8,3,1,4),_Zxr10DiffServDropLowThreshold_Type())
zxr10DiffServDropLowThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServDropLowThreshold.setStatus(_A)
_Zxr10DiffServDropHighThreshold_Type=Integer32
_Zxr10DiffServDropHighThreshold_Object=MibTableColumn
zxr10DiffServDropHighThreshold=_Zxr10DiffServDropHighThreshold_Object((1,3,6,1,4,1,3902,3,101,8,3,1,5),_Zxr10DiffServDropHighThreshold_Type())
zxr10DiffServDropHighThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServDropHighThreshold.setStatus(_A)
_Zxr10DiffServDropProbability_Type=Integer32
_Zxr10DiffServDropProbability_Object=MibTableColumn
zxr10DiffServDropProbability=_Zxr10DiffServDropProbability_Object((1,3,6,1,4,1,3902,3,101,8,3,1,6),_Zxr10DiffServDropProbability_Type())
zxr10DiffServDropProbability.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServDropProbability.setStatus(_A)
_Zxr10DiffServFlowPatternTable_Object=MibTable
zxr10DiffServFlowPatternTable=_Zxr10DiffServFlowPatternTable_Object((1,3,6,1,4,1,3902,3,101,8,4))
if mibBuilder.loadTexts:zxr10DiffServFlowPatternTable.setStatus(_A)
_Zxr10DiffServFlowPatternEntry_Object=MibTableRow
zxr10DiffServFlowPatternEntry=_Zxr10DiffServFlowPatternEntry_Object((1,3,6,1,4,1,3902,3,101,8,4,1))
zxr10DiffServFlowPatternEntry.setIndexNames((0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:zxr10DiffServFlowPatternEntry.setStatus(_A)
_Zxr10DiffServFlowPatternName_Type=DisplayString
_Zxr10DiffServFlowPatternName_Object=MibTableColumn
zxr10DiffServFlowPatternName=_Zxr10DiffServFlowPatternName_Object((1,3,6,1,4,1,3902,3,101,8,4,1,1),_Zxr10DiffServFlowPatternName_Type())
zxr10DiffServFlowPatternName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServFlowPatternName.setStatus(_A)
_Zxr10DiffServFlowServiceClass_Type=DiffServClass
_Zxr10DiffServFlowServiceClass_Object=MibTableColumn
zxr10DiffServFlowServiceClass=_Zxr10DiffServFlowServiceClass_Object((1,3,6,1,4,1,3902,3,101,8,4,1,2),_Zxr10DiffServFlowServiceClass_Type())
zxr10DiffServFlowServiceClass.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServFlowServiceClass.setStatus(_A)
_Zxr10DiffServFlowSchedulingMode_Type=DiffServScheuldingMode
_Zxr10DiffServFlowSchedulingMode_Object=MibTableColumn
zxr10DiffServFlowSchedulingMode=_Zxr10DiffServFlowSchedulingMode_Object((1,3,6,1,4,1,3902,3,101,8,4,1,3),_Zxr10DiffServFlowSchedulingMode_Type())
zxr10DiffServFlowSchedulingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServFlowSchedulingMode.setStatus(_A)
_Zxr10DiffServSchedulingWeight_Type=Integer32
_Zxr10DiffServSchedulingWeight_Object=MibTableColumn
zxr10DiffServSchedulingWeight=_Zxr10DiffServSchedulingWeight_Object((1,3,6,1,4,1,3902,3,101,8,4,1,4),_Zxr10DiffServSchedulingWeight_Type())
zxr10DiffServSchedulingWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServSchedulingWeight.setStatus(_A)
_Zxr10DiffServFlowShapingCir_Type=Integer32
_Zxr10DiffServFlowShapingCir_Object=MibTableColumn
zxr10DiffServFlowShapingCir=_Zxr10DiffServFlowShapingCir_Object((1,3,6,1,4,1,3902,3,101,8,4,1,5),_Zxr10DiffServFlowShapingCir_Type())
zxr10DiffServFlowShapingCir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServFlowShapingCir.setStatus(_A)
_Zxr10DiffServFlowShapingCbs_Type=Integer32
_Zxr10DiffServFlowShapingCbs_Object=MibTableColumn
zxr10DiffServFlowShapingCbs=_Zxr10DiffServFlowShapingCbs_Object((1,3,6,1,4,1,3902,3,101,8,4,1,6),_Zxr10DiffServFlowShapingCbs_Type())
zxr10DiffServFlowShapingCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServFlowShapingCbs.setStatus(_A)
_Zxr10DiffServFlowShapingPir_Type=Integer32
_Zxr10DiffServFlowShapingPir_Object=MibTableColumn
zxr10DiffServFlowShapingPir=_Zxr10DiffServFlowShapingPir_Object((1,3,6,1,4,1,3902,3,101,8,4,1,7),_Zxr10DiffServFlowShapingPir_Type())
zxr10DiffServFlowShapingPir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServFlowShapingPir.setStatus(_A)
_Zxr10DiffServFlowShapingPbs_Type=Integer32
_Zxr10DiffServFlowShapingPbs_Object=MibTableColumn
zxr10DiffServFlowShapingPbs=_Zxr10DiffServFlowShapingPbs_Object((1,3,6,1,4,1,3902,3,101,8,4,1,8),_Zxr10DiffServFlowShapingPbs_Type())
zxr10DiffServFlowShapingPbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServFlowShapingPbs.setStatus(_A)
_Zxr10DiffServFlowDropPatternName_Type=DisplayString
_Zxr10DiffServFlowDropPatternName_Object=MibTableColumn
zxr10DiffServFlowDropPatternName=_Zxr10DiffServFlowDropPatternName_Object((1,3,6,1,4,1,3902,3,101,8,4,1,9),_Zxr10DiffServFlowDropPatternName_Type())
zxr10DiffServFlowDropPatternName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServFlowDropPatternName.setStatus(_A)
_Zxr10DiffServIntfTable_Object=MibTable
zxr10DiffServIntfTable=_Zxr10DiffServIntfTable_Object((1,3,6,1,4,1,3902,3,101,8,5))
if mibBuilder.loadTexts:zxr10DiffServIntfTable.setStatus(_A)
_Zxr10DiffServIntfEntry_Object=MibTableRow
zxr10DiffServIntfEntry=_Zxr10DiffServIntfEntry_Object((1,3,6,1,4,1,3902,3,101,8,5,1))
zxr10DiffServIntfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zxr10DiffServIntfEntry.setStatus(_A)
_Zxr10DiffServIntfName_Type=DisplayString
_Zxr10DiffServIntfName_Object=MibTableColumn
zxr10DiffServIntfName=_Zxr10DiffServIntfName_Object((1,3,6,1,4,1,3902,3,101,8,5,1,1),_Zxr10DiffServIntfName_Type())
zxr10DiffServIntfName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfName.setStatus(_A)
_Zxr10DiffServIntfFlowPatternName_Type=DisplayString
_Zxr10DiffServIntfFlowPatternName_Object=MibTableColumn
zxr10DiffServIntfFlowPatternName=_Zxr10DiffServIntfFlowPatternName_Object((1,3,6,1,4,1,3902,3,101,8,5,1,2),_Zxr10DiffServIntfFlowPatternName_Type())
zxr10DiffServIntfFlowPatternName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfFlowPatternName.setStatus(_A)
_Zxr10DiffServIntfDomainName_Type=DisplayString
_Zxr10DiffServIntfDomainName_Object=MibTableColumn
zxr10DiffServIntfDomainName=_Zxr10DiffServIntfDomainName_Object((1,3,6,1,4,1,3902,3,101,8,5,1,3),_Zxr10DiffServIntfDomainName_Type())
zxr10DiffServIntfDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfDomainName.setStatus(_A)
_Zxr10DiffServIntfDomainAppVlanRange_Type=DisplayString
_Zxr10DiffServIntfDomainAppVlanRange_Object=MibTableColumn
zxr10DiffServIntfDomainAppVlanRange=_Zxr10DiffServIntfDomainAppVlanRange_Object((1,3,6,1,4,1,3902,3,101,8,5,1,4),_Zxr10DiffServIntfDomainAppVlanRange_Type())
zxr10DiffServIntfDomainAppVlanRange.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfDomainAppVlanRange.setStatus(_A)
_Zxr10DiffServIntfTrustType_Type=DiffServTosTrustType
_Zxr10DiffServIntfTrustType_Object=MibTableColumn
zxr10DiffServIntfTrustType=_Zxr10DiffServIntfTrustType_Object((1,3,6,1,4,1,3902,3,101,8,5,1,5),_Zxr10DiffServIntfTrustType_Type())
zxr10DiffServIntfTrustType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfTrustType.setStatus(_A)
_Zxr10DiffServIntfTrustAppVlanRange_Type=DisplayString
_Zxr10DiffServIntfTrustAppVlanRange_Object=MibTableColumn
zxr10DiffServIntfTrustAppVlanRange=_Zxr10DiffServIntfTrustAppVlanRange_Object((1,3,6,1,4,1,3902,3,101,8,5,1,6),_Zxr10DiffServIntfTrustAppVlanRange_Type())
zxr10DiffServIntfTrustAppVlanRange.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfTrustAppVlanRange.setStatus(_A)
_Zxr10DiffServIntfTunnelingMode_Type=DiffServTunnelingMode
_Zxr10DiffServIntfTunnelingMode_Object=MibTableColumn
zxr10DiffServIntfTunnelingMode=_Zxr10DiffServIntfTunnelingMode_Object((1,3,6,1,4,1,3902,3,101,8,5,1,7),_Zxr10DiffServIntfTunnelingMode_Type())
zxr10DiffServIntfTunnelingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfTunnelingMode.setStatus(_A)
_Zxr10DiffServIntfInPolicingMode_Type=DiffServPolicingMode
_Zxr10DiffServIntfInPolicingMode_Object=MibTableColumn
zxr10DiffServIntfInPolicingMode=_Zxr10DiffServIntfInPolicingMode_Object((1,3,6,1,4,1,3902,3,101,8,5,1,8),_Zxr10DiffServIntfInPolicingMode_Type())
zxr10DiffServIntfInPolicingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfInPolicingMode.setStatus(_A)
_Zxr10DiffServIntfInPolicingCir_Type=Integer32
_Zxr10DiffServIntfInPolicingCir_Object=MibTableColumn
zxr10DiffServIntfInPolicingCir=_Zxr10DiffServIntfInPolicingCir_Object((1,3,6,1,4,1,3902,3,101,8,5,1,9),_Zxr10DiffServIntfInPolicingCir_Type())
zxr10DiffServIntfInPolicingCir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfInPolicingCir.setStatus(_A)
_Zxr10DiffServIntfInPolicingCbs_Type=Integer32
_Zxr10DiffServIntfInPolicingCbs_Object=MibTableColumn
zxr10DiffServIntfInPolicingCbs=_Zxr10DiffServIntfInPolicingCbs_Object((1,3,6,1,4,1,3902,3,101,8,5,1,10),_Zxr10DiffServIntfInPolicingCbs_Type())
zxr10DiffServIntfInPolicingCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfInPolicingCbs.setStatus(_A)
_Zxr10DiffServIntfInPolicingPir_Type=Integer32
_Zxr10DiffServIntfInPolicingPir_Object=MibTableColumn
zxr10DiffServIntfInPolicingPir=_Zxr10DiffServIntfInPolicingPir_Object((1,3,6,1,4,1,3902,3,101,8,5,1,11),_Zxr10DiffServIntfInPolicingPir_Type())
zxr10DiffServIntfInPolicingPir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfInPolicingPir.setStatus(_A)
_Zxr10DiffServIntfInPolicingPbs_Type=Integer32
_Zxr10DiffServIntfInPolicingPbs_Object=MibTableColumn
zxr10DiffServIntfInPolicingPbs=_Zxr10DiffServIntfInPolicingPbs_Object((1,3,6,1,4,1,3902,3,101,8,5,1,12),_Zxr10DiffServIntfInPolicingPbs_Type())
zxr10DiffServIntfInPolicingPbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfInPolicingPbs.setStatus(_A)
_Zxr10DiffServIntfInPolicingGreenAction_Type=DiffServPolicingAction
_Zxr10DiffServIntfInPolicingGreenAction_Object=MibTableColumn
zxr10DiffServIntfInPolicingGreenAction=_Zxr10DiffServIntfInPolicingGreenAction_Object((1,3,6,1,4,1,3902,3,101,8,5,1,13),_Zxr10DiffServIntfInPolicingGreenAction_Type())
zxr10DiffServIntfInPolicingGreenAction.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfInPolicingGreenAction.setStatus(_A)
_Zxr10DiffServIntfInPolicingGreenRemarkClass_Type=DiffServClass
_Zxr10DiffServIntfInPolicingGreenRemarkClass_Object=MibTableColumn
zxr10DiffServIntfInPolicingGreenRemarkClass=_Zxr10DiffServIntfInPolicingGreenRemarkClass_Object((1,3,6,1,4,1,3902,3,101,8,5,1,14),_Zxr10DiffServIntfInPolicingGreenRemarkClass_Type())
zxr10DiffServIntfInPolicingGreenRemarkClass.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfInPolicingGreenRemarkClass.setStatus(_A)
_Zxr10DiffServIntfInPolicingGreenRemarkColor_Type=DiffServColor
_Zxr10DiffServIntfInPolicingGreenRemarkColor_Object=MibTableColumn
zxr10DiffServIntfInPolicingGreenRemarkColor=_Zxr10DiffServIntfInPolicingGreenRemarkColor_Object((1,3,6,1,4,1,3902,3,101,8,5,1,15),_Zxr10DiffServIntfInPolicingGreenRemarkColor_Type())
zxr10DiffServIntfInPolicingGreenRemarkColor.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfInPolicingGreenRemarkColor.setStatus(_A)
_Zxr10DiffServIntfInPolicingYellowAction_Type=DiffServPolicingAction
_Zxr10DiffServIntfInPolicingYellowAction_Object=MibTableColumn
zxr10DiffServIntfInPolicingYellowAction=_Zxr10DiffServIntfInPolicingYellowAction_Object((1,3,6,1,4,1,3902,3,101,8,5,1,16),_Zxr10DiffServIntfInPolicingYellowAction_Type())
zxr10DiffServIntfInPolicingYellowAction.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfInPolicingYellowAction.setStatus(_A)
_Zxr10DiffServIntfInPolicingYellowRemarkClass_Type=DiffServClass
_Zxr10DiffServIntfInPolicingYellowRemarkClass_Object=MibTableColumn
zxr10DiffServIntfInPolicingYellowRemarkClass=_Zxr10DiffServIntfInPolicingYellowRemarkClass_Object((1,3,6,1,4,1,3902,3,101,8,5,1,17),_Zxr10DiffServIntfInPolicingYellowRemarkClass_Type())
zxr10DiffServIntfInPolicingYellowRemarkClass.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfInPolicingYellowRemarkClass.setStatus(_A)
_Zxr10DiffServIntfInPolicingYellowRemarkColor_Type=DiffServColor
_Zxr10DiffServIntfInPolicingYellowRemarkColor_Object=MibTableColumn
zxr10DiffServIntfInPolicingYellowRemarkColor=_Zxr10DiffServIntfInPolicingYellowRemarkColor_Object((1,3,6,1,4,1,3902,3,101,8,5,1,18),_Zxr10DiffServIntfInPolicingYellowRemarkColor_Type())
zxr10DiffServIntfInPolicingYellowRemarkColor.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfInPolicingYellowRemarkColor.setStatus(_A)
_Zxr10DiffServIntfInPolicingRedAction_Type=DiffServPolicingAction
_Zxr10DiffServIntfInPolicingRedAction_Object=MibTableColumn
zxr10DiffServIntfInPolicingRedAction=_Zxr10DiffServIntfInPolicingRedAction_Object((1,3,6,1,4,1,3902,3,101,8,5,1,19),_Zxr10DiffServIntfInPolicingRedAction_Type())
zxr10DiffServIntfInPolicingRedAction.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfInPolicingRedAction.setStatus(_A)
_Zxr10DiffServIntfInPolicingRedRemarkClass_Type=DiffServClass
_Zxr10DiffServIntfInPolicingRedRemarkClass_Object=MibTableColumn
zxr10DiffServIntfInPolicingRedRemarkClass=_Zxr10DiffServIntfInPolicingRedRemarkClass_Object((1,3,6,1,4,1,3902,3,101,8,5,1,20),_Zxr10DiffServIntfInPolicingRedRemarkClass_Type())
zxr10DiffServIntfInPolicingRedRemarkClass.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfInPolicingRedRemarkClass.setStatus(_A)
_Zxr10DiffServIntfInPolicingRedRemarkColor_Type=DiffServColor
_Zxr10DiffServIntfInPolicingRedRemarkColor_Object=MibTableColumn
zxr10DiffServIntfInPolicingRedRemarkColor=_Zxr10DiffServIntfInPolicingRedRemarkColor_Object((1,3,6,1,4,1,3902,3,101,8,5,1,21),_Zxr10DiffServIntfInPolicingRedRemarkColor_Type())
zxr10DiffServIntfInPolicingRedRemarkColor.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfInPolicingRedRemarkColor.setStatus(_A)
_Zxr10DiffServIntfOutPolicingMode_Type=DiffServPolicingMode
_Zxr10DiffServIntfOutPolicingMode_Object=MibTableColumn
zxr10DiffServIntfOutPolicingMode=_Zxr10DiffServIntfOutPolicingMode_Object((1,3,6,1,4,1,3902,3,101,8,5,1,22),_Zxr10DiffServIntfOutPolicingMode_Type())
zxr10DiffServIntfOutPolicingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfOutPolicingMode.setStatus(_A)
_Zxr10DiffServIntfOutPolicingCir_Type=Integer32
_Zxr10DiffServIntfOutPolicingCir_Object=MibTableColumn
zxr10DiffServIntfOutPolicingCir=_Zxr10DiffServIntfOutPolicingCir_Object((1,3,6,1,4,1,3902,3,101,8,5,1,23),_Zxr10DiffServIntfOutPolicingCir_Type())
zxr10DiffServIntfOutPolicingCir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfOutPolicingCir.setStatus(_A)
_Zxr10DiffServIntfOutPolicingCbs_Type=Integer32
_Zxr10DiffServIntfOutPolicingCbs_Object=MibTableColumn
zxr10DiffServIntfOutPolicingCbs=_Zxr10DiffServIntfOutPolicingCbs_Object((1,3,6,1,4,1,3902,3,101,8,5,1,24),_Zxr10DiffServIntfOutPolicingCbs_Type())
zxr10DiffServIntfOutPolicingCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfOutPolicingCbs.setStatus(_A)
_Zxr10DiffServIntfOutPolicingPir_Type=Integer32
_Zxr10DiffServIntfOutPolicingPir_Object=MibTableColumn
zxr10DiffServIntfOutPolicingPir=_Zxr10DiffServIntfOutPolicingPir_Object((1,3,6,1,4,1,3902,3,101,8,5,1,25),_Zxr10DiffServIntfOutPolicingPir_Type())
zxr10DiffServIntfOutPolicingPir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfOutPolicingPir.setStatus(_A)
_Zxr10DiffServIntfOutPolicingPbs_Type=Integer32
_Zxr10DiffServIntfOutPolicingPbs_Object=MibTableColumn
zxr10DiffServIntfOutPolicingPbs=_Zxr10DiffServIntfOutPolicingPbs_Object((1,3,6,1,4,1,3902,3,101,8,5,1,26),_Zxr10DiffServIntfOutPolicingPbs_Type())
zxr10DiffServIntfOutPolicingPbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfOutPolicingPbs.setStatus(_A)
_Zxr10DiffServIntfOutPolicingGreenAction_Type=DiffServPolicingAction
_Zxr10DiffServIntfOutPolicingGreenAction_Object=MibTableColumn
zxr10DiffServIntfOutPolicingGreenAction=_Zxr10DiffServIntfOutPolicingGreenAction_Object((1,3,6,1,4,1,3902,3,101,8,5,1,27),_Zxr10DiffServIntfOutPolicingGreenAction_Type())
zxr10DiffServIntfOutPolicingGreenAction.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfOutPolicingGreenAction.setStatus(_A)
_Zxr10DiffServIntfOutPolicingGreenRemarkClass_Type=DiffServClass
_Zxr10DiffServIntfOutPolicingGreenRemarkClass_Object=MibTableColumn
zxr10DiffServIntfOutPolicingGreenRemarkClass=_Zxr10DiffServIntfOutPolicingGreenRemarkClass_Object((1,3,6,1,4,1,3902,3,101,8,5,1,28),_Zxr10DiffServIntfOutPolicingGreenRemarkClass_Type())
zxr10DiffServIntfOutPolicingGreenRemarkClass.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfOutPolicingGreenRemarkClass.setStatus(_A)
_Zxr10DiffServIntfOutPolicingGreenRemarkColor_Type=DiffServColor
_Zxr10DiffServIntfOutPolicingGreenRemarkColor_Object=MibTableColumn
zxr10DiffServIntfOutPolicingGreenRemarkColor=_Zxr10DiffServIntfOutPolicingGreenRemarkColor_Object((1,3,6,1,4,1,3902,3,101,8,5,1,29),_Zxr10DiffServIntfOutPolicingGreenRemarkColor_Type())
zxr10DiffServIntfOutPolicingGreenRemarkColor.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfOutPolicingGreenRemarkColor.setStatus(_A)
_Zxr10DiffServIntfOutPolicingYellowAction_Type=DiffServPolicingAction
_Zxr10DiffServIntfOutPolicingYellowAction_Object=MibTableColumn
zxr10DiffServIntfOutPolicingYellowAction=_Zxr10DiffServIntfOutPolicingYellowAction_Object((1,3,6,1,4,1,3902,3,101,8,5,1,30),_Zxr10DiffServIntfOutPolicingYellowAction_Type())
zxr10DiffServIntfOutPolicingYellowAction.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfOutPolicingYellowAction.setStatus(_A)
_Zxr10DiffServIntfOutPolicingYellowRemarkClass_Type=DiffServClass
_Zxr10DiffServIntfOutPolicingYellowRemarkClass_Object=MibTableColumn
zxr10DiffServIntfOutPolicingYellowRemarkClass=_Zxr10DiffServIntfOutPolicingYellowRemarkClass_Object((1,3,6,1,4,1,3902,3,101,8,5,1,31),_Zxr10DiffServIntfOutPolicingYellowRemarkClass_Type())
zxr10DiffServIntfOutPolicingYellowRemarkClass.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfOutPolicingYellowRemarkClass.setStatus(_A)
_Zxr10DiffServIntfOutPolicingYellowRemarkColor_Type=DiffServColor
_Zxr10DiffServIntfOutPolicingYellowRemarkColor_Object=MibTableColumn
zxr10DiffServIntfOutPolicingYellowRemarkColor=_Zxr10DiffServIntfOutPolicingYellowRemarkColor_Object((1,3,6,1,4,1,3902,3,101,8,5,1,32),_Zxr10DiffServIntfOutPolicingYellowRemarkColor_Type())
zxr10DiffServIntfOutPolicingYellowRemarkColor.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfOutPolicingYellowRemarkColor.setStatus(_A)
_Zxr10DiffServIntfOutPolicingRedAction_Type=DiffServPolicingAction
_Zxr10DiffServIntfOutPolicingRedAction_Object=MibTableColumn
zxr10DiffServIntfOutPolicingRedAction=_Zxr10DiffServIntfOutPolicingRedAction_Object((1,3,6,1,4,1,3902,3,101,8,5,1,33),_Zxr10DiffServIntfOutPolicingRedAction_Type())
zxr10DiffServIntfOutPolicingRedAction.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfOutPolicingRedAction.setStatus(_A)
_Zxr10DiffServIntfOutPolicingRedRemarkClass_Type=DiffServClass
_Zxr10DiffServIntfOutPolicingRedRemarkClass_Object=MibTableColumn
zxr10DiffServIntfOutPolicingRedRemarkClass=_Zxr10DiffServIntfOutPolicingRedRemarkClass_Object((1,3,6,1,4,1,3902,3,101,8,5,1,34),_Zxr10DiffServIntfOutPolicingRedRemarkClass_Type())
zxr10DiffServIntfOutPolicingRedRemarkClass.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfOutPolicingRedRemarkClass.setStatus(_A)
_Zxr10DiffServIntfOutPolicingRedRemarkColor_Type=DiffServColor
_Zxr10DiffServIntfOutPolicingRedRemarkColor_Object=MibTableColumn
zxr10DiffServIntfOutPolicingRedRemarkColor=_Zxr10DiffServIntfOutPolicingRedRemarkColor_Object((1,3,6,1,4,1,3902,3,101,8,5,1,35),_Zxr10DiffServIntfOutPolicingRedRemarkColor_Type())
zxr10DiffServIntfOutPolicingRedRemarkColor.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfOutPolicingRedRemarkColor.setStatus(_A)
_Zxr10DiffServIntfOutShapingCir_Type=Integer32
_Zxr10DiffServIntfOutShapingCir_Object=MibTableColumn
zxr10DiffServIntfOutShapingCir=_Zxr10DiffServIntfOutShapingCir_Object((1,3,6,1,4,1,3902,3,101,8,5,1,36),_Zxr10DiffServIntfOutShapingCir_Type())
zxr10DiffServIntfOutShapingCir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfOutShapingCir.setStatus(_A)
_Zxr10DiffServIntfOutShapingCbs_Type=Integer32
_Zxr10DiffServIntfOutShapingCbs_Object=MibTableColumn
zxr10DiffServIntfOutShapingCbs=_Zxr10DiffServIntfOutShapingCbs_Object((1,3,6,1,4,1,3902,3,101,8,5,1,37),_Zxr10DiffServIntfOutShapingCbs_Type())
zxr10DiffServIntfOutShapingCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfOutShapingCbs.setStatus(_A)
_Zxr10DiffServIntfOutShapingPir_Type=Integer32
_Zxr10DiffServIntfOutShapingPir_Object=MibTableColumn
zxr10DiffServIntfOutShapingPir=_Zxr10DiffServIntfOutShapingPir_Object((1,3,6,1,4,1,3902,3,101,8,5,1,38),_Zxr10DiffServIntfOutShapingPir_Type())
zxr10DiffServIntfOutShapingPir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfOutShapingPir.setStatus(_A)
_Zxr10DiffServIntfOutShapingPbs_Type=Integer32
_Zxr10DiffServIntfOutShapingPbs_Object=MibTableColumn
zxr10DiffServIntfOutShapingPbs=_Zxr10DiffServIntfOutShapingPbs_Object((1,3,6,1,4,1,3902,3,101,8,5,1,39),_Zxr10DiffServIntfOutShapingPbs_Type())
zxr10DiffServIntfOutShapingPbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfOutShapingPbs.setStatus(_A)
_Zxr10DiffServIntfTunnelingServClass_Type=DiffServClass
_Zxr10DiffServIntfTunnelingServClass_Object=MibTableColumn
zxr10DiffServIntfTunnelingServClass=_Zxr10DiffServIntfTunnelingServClass_Object((1,3,6,1,4,1,3902,3,101,8,5,1,40),_Zxr10DiffServIntfTunnelingServClass_Type())
zxr10DiffServIntfTunnelingServClass.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfTunnelingServClass.setStatus(_A)
_Zxr10DiffServIntfTunnelingColor_Type=DiffServColor
_Zxr10DiffServIntfTunnelingColor_Object=MibTableColumn
zxr10DiffServIntfTunnelingColor=_Zxr10DiffServIntfTunnelingColor_Object((1,3,6,1,4,1,3902,3,101,8,5,1,41),_Zxr10DiffServIntfTunnelingColor_Type())
zxr10DiffServIntfTunnelingColor.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServIntfTunnelingColor.setStatus(_A)
_Zxr10DiffServTunnelTable_Object=MibTable
zxr10DiffServTunnelTable=_Zxr10DiffServTunnelTable_Object((1,3,6,1,4,1,3902,3,101,8,6))
if mibBuilder.loadTexts:zxr10DiffServTunnelTable.setStatus(_A)
_Zxr10DiffServTunnelEntry_Object=MibTableRow
zxr10DiffServTunnelEntry=_Zxr10DiffServTunnelEntry_Object((1,3,6,1,4,1,3902,3,101,8,6,1))
zxr10DiffServTunnelEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:zxr10DiffServTunnelEntry.setStatus(_A)
_Zxr10DiffServTunnelNo_Type=Integer32
_Zxr10DiffServTunnelNo_Object=MibTableColumn
zxr10DiffServTunnelNo=_Zxr10DiffServTunnelNo_Object((1,3,6,1,4,1,3902,3,101,8,6,1,1),_Zxr10DiffServTunnelNo_Type())
zxr10DiffServTunnelNo.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServTunnelNo.setStatus(_A)
_Zxr10DiffServTunnelFlowPatternName_Type=DisplayString
_Zxr10DiffServTunnelFlowPatternName_Object=MibTableColumn
zxr10DiffServTunnelFlowPatternName=_Zxr10DiffServTunnelFlowPatternName_Object((1,3,6,1,4,1,3902,3,101,8,6,1,2),_Zxr10DiffServTunnelFlowPatternName_Type())
zxr10DiffServTunnelFlowPatternName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServTunnelFlowPatternName.setStatus(_A)
_Zxr10DiffServTunnelTunnelingMode_Type=DiffServTunnelingMode
_Zxr10DiffServTunnelTunnelingMode_Object=MibTableColumn
zxr10DiffServTunnelTunnelingMode=_Zxr10DiffServTunnelTunnelingMode_Object((1,3,6,1,4,1,3902,3,101,8,6,1,3),_Zxr10DiffServTunnelTunnelingMode_Type())
zxr10DiffServTunnelTunnelingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServTunnelTunnelingMode.setStatus(_A)
_Zxr10DiffServTunnelPolicingMode_Type=DiffServPolicingMode
_Zxr10DiffServTunnelPolicingMode_Object=MibTableColumn
zxr10DiffServTunnelPolicingMode=_Zxr10DiffServTunnelPolicingMode_Object((1,3,6,1,4,1,3902,3,101,8,6,1,4),_Zxr10DiffServTunnelPolicingMode_Type())
zxr10DiffServTunnelPolicingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServTunnelPolicingMode.setStatus(_A)
_Zxr10DiffServTunnelPolicingCir_Type=Integer32
_Zxr10DiffServTunnelPolicingCir_Object=MibTableColumn
zxr10DiffServTunnelPolicingCir=_Zxr10DiffServTunnelPolicingCir_Object((1,3,6,1,4,1,3902,3,101,8,6,1,5),_Zxr10DiffServTunnelPolicingCir_Type())
zxr10DiffServTunnelPolicingCir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServTunnelPolicingCir.setStatus(_A)
_Zxr10DiffServTunnelPolicingCbs_Type=Integer32
_Zxr10DiffServTunnelPolicingCbs_Object=MibTableColumn
zxr10DiffServTunnelPolicingCbs=_Zxr10DiffServTunnelPolicingCbs_Object((1,3,6,1,4,1,3902,3,101,8,6,1,6),_Zxr10DiffServTunnelPolicingCbs_Type())
zxr10DiffServTunnelPolicingCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServTunnelPolicingCbs.setStatus(_A)
_Zxr10DiffServTunnelPolicingPir_Type=Integer32
_Zxr10DiffServTunnelPolicingPir_Object=MibTableColumn
zxr10DiffServTunnelPolicingPir=_Zxr10DiffServTunnelPolicingPir_Object((1,3,6,1,4,1,3902,3,101,8,6,1,7),_Zxr10DiffServTunnelPolicingPir_Type())
zxr10DiffServTunnelPolicingPir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServTunnelPolicingPir.setStatus(_A)
_Zxr10DiffServTunnelPolicingPbs_Type=Integer32
_Zxr10DiffServTunnelPolicingPbs_Object=MibTableColumn
zxr10DiffServTunnelPolicingPbs=_Zxr10DiffServTunnelPolicingPbs_Object((1,3,6,1,4,1,3902,3,101,8,6,1,8),_Zxr10DiffServTunnelPolicingPbs_Type())
zxr10DiffServTunnelPolicingPbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServTunnelPolicingPbs.setStatus(_A)
_Zxr10DiffServTunnelShapingCir_Type=Integer32
_Zxr10DiffServTunnelShapingCir_Object=MibTableColumn
zxr10DiffServTunnelShapingCir=_Zxr10DiffServTunnelShapingCir_Object((1,3,6,1,4,1,3902,3,101,8,6,1,9),_Zxr10DiffServTunnelShapingCir_Type())
zxr10DiffServTunnelShapingCir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServTunnelShapingCir.setStatus(_A)
_Zxr10DiffServTunnelShapingCbs_Type=Integer32
_Zxr10DiffServTunnelShapingCbs_Object=MibTableColumn
zxr10DiffServTunnelShapingCbs=_Zxr10DiffServTunnelShapingCbs_Object((1,3,6,1,4,1,3902,3,101,8,6,1,10),_Zxr10DiffServTunnelShapingCbs_Type())
zxr10DiffServTunnelShapingCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServTunnelShapingCbs.setStatus(_A)
_Zxr10DiffServTunnelShapingPir_Type=Integer32
_Zxr10DiffServTunnelShapingPir_Object=MibTableColumn
zxr10DiffServTunnelShapingPir=_Zxr10DiffServTunnelShapingPir_Object((1,3,6,1,4,1,3902,3,101,8,6,1,11),_Zxr10DiffServTunnelShapingPir_Type())
zxr10DiffServTunnelShapingPir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServTunnelShapingPir.setStatus(_A)
_Zxr10DiffServTunnelShapingPbs_Type=Integer32
_Zxr10DiffServTunnelShapingPbs_Object=MibTableColumn
zxr10DiffServTunnelShapingPbs=_Zxr10DiffServTunnelShapingPbs_Object((1,3,6,1,4,1,3902,3,101,8,6,1,12),_Zxr10DiffServTunnelShapingPbs_Type())
zxr10DiffServTunnelShapingPbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServTunnelShapingPbs.setStatus(_A)
_Zxr10DiffServTunnelIntfName1_Type=DisplayString
_Zxr10DiffServTunnelIntfName1_Object=MibTableColumn
zxr10DiffServTunnelIntfName1=_Zxr10DiffServTunnelIntfName1_Object((1,3,6,1,4,1,3902,3,101,8,6,1,13),_Zxr10DiffServTunnelIntfName1_Type())
zxr10DiffServTunnelIntfName1.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServTunnelIntfName1.setStatus(_A)
_Zxr10DiffServTunnelDomainName1_Type=DisplayString
_Zxr10DiffServTunnelDomainName1_Object=MibTableColumn
zxr10DiffServTunnelDomainName1=_Zxr10DiffServTunnelDomainName1_Object((1,3,6,1,4,1,3902,3,101,8,6,1,14),_Zxr10DiffServTunnelDomainName1_Type())
zxr10DiffServTunnelDomainName1.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServTunnelDomainName1.setStatus(_A)
_Zxr10DiffServTunnelIntfName2_Type=DisplayString
_Zxr10DiffServTunnelIntfName2_Object=MibTableColumn
zxr10DiffServTunnelIntfName2=_Zxr10DiffServTunnelIntfName2_Object((1,3,6,1,4,1,3902,3,101,8,6,1,15),_Zxr10DiffServTunnelIntfName2_Type())
zxr10DiffServTunnelIntfName2.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServTunnelIntfName2.setStatus(_A)
_Zxr10DiffServTunnelDomainName2_Type=DisplayString
_Zxr10DiffServTunnelDomainName2_Object=MibTableColumn
zxr10DiffServTunnelDomainName2=_Zxr10DiffServTunnelDomainName2_Object((1,3,6,1,4,1,3902,3,101,8,6,1,16),_Zxr10DiffServTunnelDomainName2_Type())
zxr10DiffServTunnelDomainName2.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServTunnelDomainName2.setStatus(_A)
_Zxr10DiffServTunnelTunnelingServClass_Type=DiffServClass
_Zxr10DiffServTunnelTunnelingServClass_Object=MibTableColumn
zxr10DiffServTunnelTunnelingServClass=_Zxr10DiffServTunnelTunnelingServClass_Object((1,3,6,1,4,1,3902,3,101,8,6,1,17),_Zxr10DiffServTunnelTunnelingServClass_Type())
zxr10DiffServTunnelTunnelingServClass.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServTunnelTunnelingServClass.setStatus(_A)
_Zxr10DiffServTunnelTunnelingColor_Type=DiffServColor
_Zxr10DiffServTunnelTunnelingColor_Object=MibTableColumn
zxr10DiffServTunnelTunnelingColor=_Zxr10DiffServTunnelTunnelingColor_Object((1,3,6,1,4,1,3902,3,101,8,6,1,18),_Zxr10DiffServTunnelTunnelingColor_Type())
zxr10DiffServTunnelTunnelingColor.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServTunnelTunnelingColor.setStatus(_A)
_Zxr10DiffServPWTable_Object=MibTable
zxr10DiffServPWTable=_Zxr10DiffServPWTable_Object((1,3,6,1,4,1,3902,3,101,8,7))
if mibBuilder.loadTexts:zxr10DiffServPWTable.setStatus(_A)
_Zxr10DiffServPWEntry_Object=MibTableRow
zxr10DiffServPWEntry=_Zxr10DiffServPWEntry_Object((1,3,6,1,4,1,3902,3,101,8,7,1))
zxr10DiffServPWEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:zxr10DiffServPWEntry.setStatus(_A)
_Zxr10DiffServPWName_Type=DisplayString
_Zxr10DiffServPWName_Object=MibTableColumn
zxr10DiffServPWName=_Zxr10DiffServPWName_Object((1,3,6,1,4,1,3902,3,101,8,7,1,1),_Zxr10DiffServPWName_Type())
zxr10DiffServPWName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServPWName.setStatus(_A)
_Zxr10DiffServPWFlowPatternName_Type=DisplayString
_Zxr10DiffServPWFlowPatternName_Object=MibTableColumn
zxr10DiffServPWFlowPatternName=_Zxr10DiffServPWFlowPatternName_Object((1,3,6,1,4,1,3902,3,101,8,7,1,2),_Zxr10DiffServPWFlowPatternName_Type())
zxr10DiffServPWFlowPatternName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServPWFlowPatternName.setStatus(_A)
_Zxr10DiffServPWPolicingMode_Type=DiffServPolicingMode
_Zxr10DiffServPWPolicingMode_Object=MibTableColumn
zxr10DiffServPWPolicingMode=_Zxr10DiffServPWPolicingMode_Object((1,3,6,1,4,1,3902,3,101,8,7,1,3),_Zxr10DiffServPWPolicingMode_Type())
zxr10DiffServPWPolicingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServPWPolicingMode.setStatus(_A)
_Zxr10DiffServPWPolicingCir_Type=Integer32
_Zxr10DiffServPWPolicingCir_Object=MibTableColumn
zxr10DiffServPWPolicingCir=_Zxr10DiffServPWPolicingCir_Object((1,3,6,1,4,1,3902,3,101,8,7,1,4),_Zxr10DiffServPWPolicingCir_Type())
zxr10DiffServPWPolicingCir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServPWPolicingCir.setStatus(_A)
_Zxr10DiffServPWPolicingCbs_Type=Integer32
_Zxr10DiffServPWPolicingCbs_Object=MibTableColumn
zxr10DiffServPWPolicingCbs=_Zxr10DiffServPWPolicingCbs_Object((1,3,6,1,4,1,3902,3,101,8,7,1,5),_Zxr10DiffServPWPolicingCbs_Type())
zxr10DiffServPWPolicingCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServPWPolicingCbs.setStatus(_A)
_Zxr10DiffServPWPolicingPir_Type=Integer32
_Zxr10DiffServPWPolicingPir_Object=MibTableColumn
zxr10DiffServPWPolicingPir=_Zxr10DiffServPWPolicingPir_Object((1,3,6,1,4,1,3902,3,101,8,7,1,6),_Zxr10DiffServPWPolicingPir_Type())
zxr10DiffServPWPolicingPir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServPWPolicingPir.setStatus(_A)
_Zxr10DiffServPWPolicingPbs_Type=Integer32
_Zxr10DiffServPWPolicingPbs_Object=MibTableColumn
zxr10DiffServPWPolicingPbs=_Zxr10DiffServPWPolicingPbs_Object((1,3,6,1,4,1,3902,3,101,8,7,1,7),_Zxr10DiffServPWPolicingPbs_Type())
zxr10DiffServPWPolicingPbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServPWPolicingPbs.setStatus(_A)
_Zxr10DiffServPWShapingCir_Type=Integer32
_Zxr10DiffServPWShapingCir_Object=MibTableColumn
zxr10DiffServPWShapingCir=_Zxr10DiffServPWShapingCir_Object((1,3,6,1,4,1,3902,3,101,8,7,1,8),_Zxr10DiffServPWShapingCir_Type())
zxr10DiffServPWShapingCir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServPWShapingCir.setStatus(_A)
_Zxr10DiffServPWShapingCbs_Type=Integer32
_Zxr10DiffServPWShapingCbs_Object=MibTableColumn
zxr10DiffServPWShapingCbs=_Zxr10DiffServPWShapingCbs_Object((1,3,6,1,4,1,3902,3,101,8,7,1,9),_Zxr10DiffServPWShapingCbs_Type())
zxr10DiffServPWShapingCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServPWShapingCbs.setStatus(_A)
_Zxr10DiffServPWShapingPir_Type=Integer32
_Zxr10DiffServPWShapingPir_Object=MibTableColumn
zxr10DiffServPWShapingPir=_Zxr10DiffServPWShapingPir_Object((1,3,6,1,4,1,3902,3,101,8,7,1,10),_Zxr10DiffServPWShapingPir_Type())
zxr10DiffServPWShapingPir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServPWShapingPir.setStatus(_A)
_Zxr10DiffServPWShapingPbs_Type=Integer32
_Zxr10DiffServPWShapingPbs_Object=MibTableColumn
zxr10DiffServPWShapingPbs=_Zxr10DiffServPWShapingPbs_Object((1,3,6,1,4,1,3902,3,101,8,7,1,11),_Zxr10DiffServPWShapingPbs_Type())
zxr10DiffServPWShapingPbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServPWShapingPbs.setStatus(_A)
_Zxr10DiffServPWDomainName_Type=DisplayString
_Zxr10DiffServPWDomainName_Object=MibTableColumn
zxr10DiffServPWDomainName=_Zxr10DiffServPWDomainName_Object((1,3,6,1,4,1,3902,3,101,8,7,1,12),_Zxr10DiffServPWDomainName_Type())
zxr10DiffServPWDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServPWDomainName.setStatus(_A)
_Zxr10DiffServCIPTable_Object=MibTable
zxr10DiffServCIPTable=_Zxr10DiffServCIPTable_Object((1,3,6,1,4,1,3902,3,101,8,8))
if mibBuilder.loadTexts:zxr10DiffServCIPTable.setStatus(_A)
_Zxr10DiffServCIPEntry_Object=MibTableRow
zxr10DiffServCIPEntry=_Zxr10DiffServCIPEntry_Object((1,3,6,1,4,1,3902,3,101,8,8,1))
zxr10DiffServCIPEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:zxr10DiffServCIPEntry.setStatus(_A)
_Zxr10DiffServCIPNo_Type=Integer32
_Zxr10DiffServCIPNo_Object=MibTableColumn
zxr10DiffServCIPNo=_Zxr10DiffServCIPNo_Object((1,3,6,1,4,1,3902,3,101,8,8,1,1),_Zxr10DiffServCIPNo_Type())
zxr10DiffServCIPNo.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServCIPNo.setStatus(_A)
_Zxr10DiffServCIPPolicingMode_Type=DiffServPolicingMode
_Zxr10DiffServCIPPolicingMode_Object=MibTableColumn
zxr10DiffServCIPPolicingMode=_Zxr10DiffServCIPPolicingMode_Object((1,3,6,1,4,1,3902,3,101,8,8,1,2),_Zxr10DiffServCIPPolicingMode_Type())
zxr10DiffServCIPPolicingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServCIPPolicingMode.setStatus(_A)
_Zxr10DiffServCIPPolicingCir_Type=Integer32
_Zxr10DiffServCIPPolicingCir_Object=MibTableColumn
zxr10DiffServCIPPolicingCir=_Zxr10DiffServCIPPolicingCir_Object((1,3,6,1,4,1,3902,3,101,8,8,1,3),_Zxr10DiffServCIPPolicingCir_Type())
zxr10DiffServCIPPolicingCir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServCIPPolicingCir.setStatus(_A)
_Zxr10DiffServCIPPolicingCbs_Type=Integer32
_Zxr10DiffServCIPPolicingCbs_Object=MibTableColumn
zxr10DiffServCIPPolicingCbs=_Zxr10DiffServCIPPolicingCbs_Object((1,3,6,1,4,1,3902,3,101,8,8,1,4),_Zxr10DiffServCIPPolicingCbs_Type())
zxr10DiffServCIPPolicingCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServCIPPolicingCbs.setStatus(_A)
_Zxr10DiffServCIPPolicingPir_Type=Integer32
_Zxr10DiffServCIPPolicingPir_Object=MibTableColumn
zxr10DiffServCIPPolicingPir=_Zxr10DiffServCIPPolicingPir_Object((1,3,6,1,4,1,3902,3,101,8,8,1,5),_Zxr10DiffServCIPPolicingPir_Type())
zxr10DiffServCIPPolicingPir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServCIPPolicingPir.setStatus(_A)
_Zxr10DiffServCIPPolicingPbs_Type=Integer32
_Zxr10DiffServCIPPolicingPbs_Object=MibTableColumn
zxr10DiffServCIPPolicingPbs=_Zxr10DiffServCIPPolicingPbs_Object((1,3,6,1,4,1,3902,3,101,8,8,1,6),_Zxr10DiffServCIPPolicingPbs_Type())
zxr10DiffServCIPPolicingPbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServCIPPolicingPbs.setStatus(_A)
_Zxr10DiffServVPNTable_Object=MibTable
zxr10DiffServVPNTable=_Zxr10DiffServVPNTable_Object((1,3,6,1,4,1,3902,3,101,8,9))
if mibBuilder.loadTexts:zxr10DiffServVPNTable.setStatus(_A)
_Zxr10DiffServVPNEntry_Object=MibTableRow
zxr10DiffServVPNEntry=_Zxr10DiffServVPNEntry_Object((1,3,6,1,4,1,3902,3,101,8,9,1))
zxr10DiffServVPNEntry.setIndexNames((0,_C,_U),(0,_C,_V))
if mibBuilder.loadTexts:zxr10DiffServVPNEntry.setStatus(_A)
_Zxr10DiffServVPNMode_Type=DiffServVPNMode
_Zxr10DiffServVPNMode_Object=MibTableColumn
zxr10DiffServVPNMode=_Zxr10DiffServVPNMode_Object((1,3,6,1,4,1,3902,3,101,8,9,1,1),_Zxr10DiffServVPNMode_Type())
zxr10DiffServVPNMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServVPNMode.setStatus(_A)
_Zxr10DiffServVPNName_Type=DisplayString
_Zxr10DiffServVPNName_Object=MibTableColumn
zxr10DiffServVPNName=_Zxr10DiffServVPNName_Object((1,3,6,1,4,1,3902,3,101,8,9,1,2),_Zxr10DiffServVPNName_Type())
zxr10DiffServVPNName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServVPNName.setStatus(_A)
_Zxr10DiffServVPNTunnelingMode_Type=DiffServTunnelingMode
_Zxr10DiffServVPNTunnelingMode_Object=MibTableColumn
zxr10DiffServVPNTunnelingMode=_Zxr10DiffServVPNTunnelingMode_Object((1,3,6,1,4,1,3902,3,101,8,9,1,3),_Zxr10DiffServVPNTunnelingMode_Type())
zxr10DiffServVPNTunnelingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServVPNTunnelingMode.setStatus(_A)
_Zxr10DiffServVPNPolicingMode_Type=DiffServPolicingMode
_Zxr10DiffServVPNPolicingMode_Object=MibTableColumn
zxr10DiffServVPNPolicingMode=_Zxr10DiffServVPNPolicingMode_Object((1,3,6,1,4,1,3902,3,101,8,9,1,4),_Zxr10DiffServVPNPolicingMode_Type())
zxr10DiffServVPNPolicingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServVPNPolicingMode.setStatus(_A)
_Zxr10DiffServVPNPolicingCir_Type=Integer32
_Zxr10DiffServVPNPolicingCir_Object=MibTableColumn
zxr10DiffServVPNPolicingCir=_Zxr10DiffServVPNPolicingCir_Object((1,3,6,1,4,1,3902,3,101,8,9,1,5),_Zxr10DiffServVPNPolicingCir_Type())
zxr10DiffServVPNPolicingCir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServVPNPolicingCir.setStatus(_A)
_Zxr10DiffServVPNPolicingCbs_Type=Integer32
_Zxr10DiffServVPNPolicingCbs_Object=MibTableColumn
zxr10DiffServVPNPolicingCbs=_Zxr10DiffServVPNPolicingCbs_Object((1,3,6,1,4,1,3902,3,101,8,9,1,6),_Zxr10DiffServVPNPolicingCbs_Type())
zxr10DiffServVPNPolicingCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServVPNPolicingCbs.setStatus(_A)
_Zxr10DiffServVPNPolicingPir_Type=Integer32
_Zxr10DiffServVPNPolicingPir_Object=MibTableColumn
zxr10DiffServVPNPolicingPir=_Zxr10DiffServVPNPolicingPir_Object((1,3,6,1,4,1,3902,3,101,8,9,1,7),_Zxr10DiffServVPNPolicingPir_Type())
zxr10DiffServVPNPolicingPir.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServVPNPolicingPir.setStatus(_A)
_Zxr10DiffServVPNPolicingPbs_Type=Integer32
_Zxr10DiffServVPNPolicingPbs_Object=MibTableColumn
zxr10DiffServVPNPolicingPbs=_Zxr10DiffServVPNPolicingPbs_Object((1,3,6,1,4,1,3902,3,101,8,9,1,8),_Zxr10DiffServVPNPolicingPbs_Type())
zxr10DiffServVPNPolicingPbs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServVPNPolicingPbs.setStatus(_A)
_Zxr10DiffServClsMapTable_Object=MibTable
zxr10DiffServClsMapTable=_Zxr10DiffServClsMapTable_Object((1,3,6,1,4,1,3902,3,101,8,10))
if mibBuilder.loadTexts:zxr10DiffServClsMapTable.setStatus(_A)
_Zxr10DiffServClsMapEntry_Object=MibTableRow
zxr10DiffServClsMapEntry=_Zxr10DiffServClsMapEntry_Object((1,3,6,1,4,1,3902,3,101,8,10,1))
zxr10DiffServClsMapEntry.setIndexNames((0,_C,_W),(0,_C,_X))
if mibBuilder.loadTexts:zxr10DiffServClsMapEntry.setStatus(_A)
_Zxr10DiffServClsMapName_Type=DisplayString
_Zxr10DiffServClsMapName_Object=MibTableColumn
zxr10DiffServClsMapName=_Zxr10DiffServClsMapName_Object((1,3,6,1,4,1,3902,3,101,8,10,1,1),_Zxr10DiffServClsMapName_Type())
zxr10DiffServClsMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServClsMapName.setStatus(_A)
_Zxr10DiffServClsMatchSequence_Type=Integer32
_Zxr10DiffServClsMatchSequence_Object=MibTableColumn
zxr10DiffServClsMatchSequence=_Zxr10DiffServClsMatchSequence_Object((1,3,6,1,4,1,3902,3,101,8,10,1,2),_Zxr10DiffServClsMatchSequence_Type())
zxr10DiffServClsMatchSequence.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zxr10DiffServClsMatchSequence.setStatus(_A)
_Zxr10DiffServClsMatchSvlanID_Type=DisplayString
_Zxr10DiffServClsMatchSvlanID_Object=MibTableColumn
zxr10DiffServClsMatchSvlanID=_Zxr10DiffServClsMatchSvlanID_Object((1,3,6,1,4,1,3902,3,101,8,10,1,3),_Zxr10DiffServClsMatchSvlanID_Type())
zxr10DiffServClsMatchSvlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServClsMatchSvlanID.setStatus(_A)
_Zxr10DiffServClsMatchCvlanID_Type=DisplayString
_Zxr10DiffServClsMatchCvlanID_Object=MibTableColumn
zxr10DiffServClsMatchCvlanID=_Zxr10DiffServClsMatchCvlanID_Object((1,3,6,1,4,1,3902,3,101,8,10,1,4),_Zxr10DiffServClsMatchCvlanID_Type())
zxr10DiffServClsMatchCvlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServClsMatchCvlanID.setStatus(_A)
_Zxr10DiffServClsMatchSVlanPri_Type=DisplayString
_Zxr10DiffServClsMatchSVlanPri_Object=MibTableColumn
zxr10DiffServClsMatchSVlanPri=_Zxr10DiffServClsMatchSVlanPri_Object((1,3,6,1,4,1,3902,3,101,8,10,1,5),_Zxr10DiffServClsMatchSVlanPri_Type())
zxr10DiffServClsMatchSVlanPri.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServClsMatchSVlanPri.setStatus(_A)
_Zxr10DiffServClsMatchVpi_Type=DisplayString
_Zxr10DiffServClsMatchVpi_Object=MibTableColumn
zxr10DiffServClsMatchVpi=_Zxr10DiffServClsMatchVpi_Object((1,3,6,1,4,1,3902,3,101,8,10,1,6),_Zxr10DiffServClsMatchVpi_Type())
zxr10DiffServClsMatchVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServClsMatchVpi.setStatus(_A)
_Zxr10DiffServClsMatchVci_Type=DisplayString
_Zxr10DiffServClsMatchVci_Object=MibTableColumn
zxr10DiffServClsMatchVci=_Zxr10DiffServClsMatchVci_Object((1,3,6,1,4,1,3902,3,101,8,10,1,7),_Zxr10DiffServClsMatchVci_Type())
zxr10DiffServClsMatchVci.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10DiffServClsMatchVci.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_F:DisplayString,'DiffServPacketTos':DiffServPacketTos,'DiffServClass':DiffServClass,'DiffServColor':DiffServColor,'DiffServScheuldingMode':DiffServScheuldingMode,'DiffServDroppingMode':DiffServDroppingMode,'DiffServTunnelingMode':DiffServTunnelingMode,'DiffServPolicingAction':DiffServPolicingAction,'DiffServTosTrustType':DiffServTosTrustType,'DiffServPolicingMode':DiffServPolicingMode,'DiffServVPNMode':DiffServVPNMode,'zte':zte,'zxr10':zxr10,'zxr10protocol':zxr10protocol,'zxr10DiffServ':zxr10DiffServ,'zxr10DiffServDomainInTable':zxr10DiffServDomainInTable,'zxr10DiffServDomainInEntry':zxr10DiffServDomainInEntry,_G:zxr10DiffServDomainInName,_H:zxr10DiffServDomainInToSType,_I:zxr10DiffServDomainInToSValue,'zxr10DiffServDomainInServClass':zxr10DiffServDomainInServClass,'zxr10DiffServDomainInColor':zxr10DiffServDomainInColor,'zxr10DiffServDomainOutTable':zxr10DiffServDomainOutTable,'zxr10DiffServDomainOutEntry':zxr10DiffServDomainOutEntry,_J:zxr10DiffServDomainOutName,_K:zxr10DiffServDomainOutServClass,_L:zxr10DiffServDomainOutColor,_M:zxr10DiffServDomainOutToSType,'zxr10DiffServDomainOutToSValue':zxr10DiffServDomainOutToSValue,'zxr10DiffServDropPatternTable':zxr10DiffServDropPatternTable,'zxr10DiffServDropPatternEntry':zxr10DiffServDropPatternEntry,_N:zxr10DiffServDropPatternName,_O:zxr10DiffServDropPatternColor,'zxr10DiffServDropPatternMode':zxr10DiffServDropPatternMode,'zxr10DiffServDropLowThreshold':zxr10DiffServDropLowThreshold,'zxr10DiffServDropHighThreshold':zxr10DiffServDropHighThreshold,'zxr10DiffServDropProbability':zxr10DiffServDropProbability,'zxr10DiffServFlowPatternTable':zxr10DiffServFlowPatternTable,'zxr10DiffServFlowPatternEntry':zxr10DiffServFlowPatternEntry,_P:zxr10DiffServFlowPatternName,_Q:zxr10DiffServFlowServiceClass,'zxr10DiffServFlowSchedulingMode':zxr10DiffServFlowSchedulingMode,'zxr10DiffServSchedulingWeight':zxr10DiffServSchedulingWeight,'zxr10DiffServFlowShapingCir':zxr10DiffServFlowShapingCir,'zxr10DiffServFlowShapingCbs':zxr10DiffServFlowShapingCbs,'zxr10DiffServFlowShapingPir':zxr10DiffServFlowShapingPir,'zxr10DiffServFlowShapingPbs':zxr10DiffServFlowShapingPbs,'zxr10DiffServFlowDropPatternName':zxr10DiffServFlowDropPatternName,'zxr10DiffServIntfTable':zxr10DiffServIntfTable,'zxr10DiffServIntfEntry':zxr10DiffServIntfEntry,'zxr10DiffServIntfName':zxr10DiffServIntfName,'zxr10DiffServIntfFlowPatternName':zxr10DiffServIntfFlowPatternName,'zxr10DiffServIntfDomainName':zxr10DiffServIntfDomainName,'zxr10DiffServIntfDomainAppVlanRange':zxr10DiffServIntfDomainAppVlanRange,'zxr10DiffServIntfTrustType':zxr10DiffServIntfTrustType,'zxr10DiffServIntfTrustAppVlanRange':zxr10DiffServIntfTrustAppVlanRange,'zxr10DiffServIntfTunnelingMode':zxr10DiffServIntfTunnelingMode,'zxr10DiffServIntfInPolicingMode':zxr10DiffServIntfInPolicingMode,'zxr10DiffServIntfInPolicingCir':zxr10DiffServIntfInPolicingCir,'zxr10DiffServIntfInPolicingCbs':zxr10DiffServIntfInPolicingCbs,'zxr10DiffServIntfInPolicingPir':zxr10DiffServIntfInPolicingPir,'zxr10DiffServIntfInPolicingPbs':zxr10DiffServIntfInPolicingPbs,'zxr10DiffServIntfInPolicingGreenAction':zxr10DiffServIntfInPolicingGreenAction,'zxr10DiffServIntfInPolicingGreenRemarkClass':zxr10DiffServIntfInPolicingGreenRemarkClass,'zxr10DiffServIntfInPolicingGreenRemarkColor':zxr10DiffServIntfInPolicingGreenRemarkColor,'zxr10DiffServIntfInPolicingYellowAction':zxr10DiffServIntfInPolicingYellowAction,'zxr10DiffServIntfInPolicingYellowRemarkClass':zxr10DiffServIntfInPolicingYellowRemarkClass,'zxr10DiffServIntfInPolicingYellowRemarkColor':zxr10DiffServIntfInPolicingYellowRemarkColor,'zxr10DiffServIntfInPolicingRedAction':zxr10DiffServIntfInPolicingRedAction,'zxr10DiffServIntfInPolicingRedRemarkClass':zxr10DiffServIntfInPolicingRedRemarkClass,'zxr10DiffServIntfInPolicingRedRemarkColor':zxr10DiffServIntfInPolicingRedRemarkColor,'zxr10DiffServIntfOutPolicingMode':zxr10DiffServIntfOutPolicingMode,'zxr10DiffServIntfOutPolicingCir':zxr10DiffServIntfOutPolicingCir,'zxr10DiffServIntfOutPolicingCbs':zxr10DiffServIntfOutPolicingCbs,'zxr10DiffServIntfOutPolicingPir':zxr10DiffServIntfOutPolicingPir,'zxr10DiffServIntfOutPolicingPbs':zxr10DiffServIntfOutPolicingPbs,'zxr10DiffServIntfOutPolicingGreenAction':zxr10DiffServIntfOutPolicingGreenAction,'zxr10DiffServIntfOutPolicingGreenRemarkClass':zxr10DiffServIntfOutPolicingGreenRemarkClass,'zxr10DiffServIntfOutPolicingGreenRemarkColor':zxr10DiffServIntfOutPolicingGreenRemarkColor,'zxr10DiffServIntfOutPolicingYellowAction':zxr10DiffServIntfOutPolicingYellowAction,'zxr10DiffServIntfOutPolicingYellowRemarkClass':zxr10DiffServIntfOutPolicingYellowRemarkClass,'zxr10DiffServIntfOutPolicingYellowRemarkColor':zxr10DiffServIntfOutPolicingYellowRemarkColor,'zxr10DiffServIntfOutPolicingRedAction':zxr10DiffServIntfOutPolicingRedAction,'zxr10DiffServIntfOutPolicingRedRemarkClass':zxr10DiffServIntfOutPolicingRedRemarkClass,'zxr10DiffServIntfOutPolicingRedRemarkColor':zxr10DiffServIntfOutPolicingRedRemarkColor,'zxr10DiffServIntfOutShapingCir':zxr10DiffServIntfOutShapingCir,'zxr10DiffServIntfOutShapingCbs':zxr10DiffServIntfOutShapingCbs,'zxr10DiffServIntfOutShapingPir':zxr10DiffServIntfOutShapingPir,'zxr10DiffServIntfOutShapingPbs':zxr10DiffServIntfOutShapingPbs,'zxr10DiffServIntfTunnelingServClass':zxr10DiffServIntfTunnelingServClass,'zxr10DiffServIntfTunnelingColor':zxr10DiffServIntfTunnelingColor,'zxr10DiffServTunnelTable':zxr10DiffServTunnelTable,'zxr10DiffServTunnelEntry':zxr10DiffServTunnelEntry,_R:zxr10DiffServTunnelNo,'zxr10DiffServTunnelFlowPatternName':zxr10DiffServTunnelFlowPatternName,'zxr10DiffServTunnelTunnelingMode':zxr10DiffServTunnelTunnelingMode,'zxr10DiffServTunnelPolicingMode':zxr10DiffServTunnelPolicingMode,'zxr10DiffServTunnelPolicingCir':zxr10DiffServTunnelPolicingCir,'zxr10DiffServTunnelPolicingCbs':zxr10DiffServTunnelPolicingCbs,'zxr10DiffServTunnelPolicingPir':zxr10DiffServTunnelPolicingPir,'zxr10DiffServTunnelPolicingPbs':zxr10DiffServTunnelPolicingPbs,'zxr10DiffServTunnelShapingCir':zxr10DiffServTunnelShapingCir,'zxr10DiffServTunnelShapingCbs':zxr10DiffServTunnelShapingCbs,'zxr10DiffServTunnelShapingPir':zxr10DiffServTunnelShapingPir,'zxr10DiffServTunnelShapingPbs':zxr10DiffServTunnelShapingPbs,'zxr10DiffServTunnelIntfName1':zxr10DiffServTunnelIntfName1,'zxr10DiffServTunnelDomainName1':zxr10DiffServTunnelDomainName1,'zxr10DiffServTunnelIntfName2':zxr10DiffServTunnelIntfName2,'zxr10DiffServTunnelDomainName2':zxr10DiffServTunnelDomainName2,'zxr10DiffServTunnelTunnelingServClass':zxr10DiffServTunnelTunnelingServClass,'zxr10DiffServTunnelTunnelingColor':zxr10DiffServTunnelTunnelingColor,'zxr10DiffServPWTable':zxr10DiffServPWTable,'zxr10DiffServPWEntry':zxr10DiffServPWEntry,_S:zxr10DiffServPWName,'zxr10DiffServPWFlowPatternName':zxr10DiffServPWFlowPatternName,'zxr10DiffServPWPolicingMode':zxr10DiffServPWPolicingMode,'zxr10DiffServPWPolicingCir':zxr10DiffServPWPolicingCir,'zxr10DiffServPWPolicingCbs':zxr10DiffServPWPolicingCbs,'zxr10DiffServPWPolicingPir':zxr10DiffServPWPolicingPir,'zxr10DiffServPWPolicingPbs':zxr10DiffServPWPolicingPbs,'zxr10DiffServPWShapingCir':zxr10DiffServPWShapingCir,'zxr10DiffServPWShapingCbs':zxr10DiffServPWShapingCbs,'zxr10DiffServPWShapingPir':zxr10DiffServPWShapingPir,'zxr10DiffServPWShapingPbs':zxr10DiffServPWShapingPbs,'zxr10DiffServPWDomainName':zxr10DiffServPWDomainName,'zxr10DiffServCIPTable':zxr10DiffServCIPTable,'zxr10DiffServCIPEntry':zxr10DiffServCIPEntry,_T:zxr10DiffServCIPNo,'zxr10DiffServCIPPolicingMode':zxr10DiffServCIPPolicingMode,'zxr10DiffServCIPPolicingCir':zxr10DiffServCIPPolicingCir,'zxr10DiffServCIPPolicingCbs':zxr10DiffServCIPPolicingCbs,'zxr10DiffServCIPPolicingPir':zxr10DiffServCIPPolicingPir,'zxr10DiffServCIPPolicingPbs':zxr10DiffServCIPPolicingPbs,'zxr10DiffServVPNTable':zxr10DiffServVPNTable,'zxr10DiffServVPNEntry':zxr10DiffServVPNEntry,_U:zxr10DiffServVPNMode,_V:zxr10DiffServVPNName,'zxr10DiffServVPNTunnelingMode':zxr10DiffServVPNTunnelingMode,'zxr10DiffServVPNPolicingMode':zxr10DiffServVPNPolicingMode,'zxr10DiffServVPNPolicingCir':zxr10DiffServVPNPolicingCir,'zxr10DiffServVPNPolicingCbs':zxr10DiffServVPNPolicingCbs,'zxr10DiffServVPNPolicingPir':zxr10DiffServVPNPolicingPir,'zxr10DiffServVPNPolicingPbs':zxr10DiffServVPNPolicingPbs,'zxr10DiffServClsMapTable':zxr10DiffServClsMapTable,'zxr10DiffServClsMapEntry':zxr10DiffServClsMapEntry,_W:zxr10DiffServClsMapName,_X:zxr10DiffServClsMatchSequence,'zxr10DiffServClsMatchSvlanID':zxr10DiffServClsMatchSvlanID,'zxr10DiffServClsMatchCvlanID':zxr10DiffServClsMatchCvlanID,'zxr10DiffServClsMatchSVlanPri':zxr10DiffServClsMatchSVlanPri,'zxr10DiffServClsMatchVpi':zxr10DiffServClsMatchVpi,'zxr10DiffServClsMatchVci':zxr10DiffServClsMatchVci})