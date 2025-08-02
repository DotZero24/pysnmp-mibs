_q='ifCfgE1PortIndex'
_p='ifCfgE1SlotIndex'
_o='ifCfgT1PortIndex'
_n='ifCfgT1SlotIndex'
_m='ifCfgSdslPortIndex'
_l='ifCfgSdslSlotIndex'
_k='ifCfgIdslPortIndex'
_j='ifCfgIdslSlotIndex'
_i='delay64ms'
_h='delay32ms'
_g='delay16ms'
_f='delay8ms'
_e='delay4ms'
_d='delay2ms'
_c='delay1ms'
_b='corr4ms'
_a='corr2ms'
_Z='corr1ms'
_Y='corr500us'
_X='corr250us'
_W='corr125us'
_V='stdMdeNoLink'
_U='gDMT-BIS-Annex-M'
_T='gDMT-BIS-Annex-L'
_S='gDMT-BISplus'
_R='gDMT-BIS'
_Q='aLCATEL'
_P='multiMode'
_O='ifCfgAdslPortIndex'
_N='ifCfgAdslSlotIndex'
_M='ifCfgVLANIndex'
_L='ifCfgIfPortIndex'
_K='ifCfgIfSlotIndex'
_J='ifCfgPortIndex'
_I='ifCfgSlotIndex'
_H='OctetString'
_G='off'
_F='Kbps'
_E='NTNTECH-INTERFACE-MODULE-CONFIGURATION-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
NtnDisplayString,ntntechInterfaceModule=mibBuilder.importSymbols('NTNTECH-ROOT-MIB','NtnDisplayString','ntntechInterfaceModule')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntntechInterfaceModuleConfigurationMIB=ModuleIdentity((1,3,6,1,4,1,8059,1,2,1))
if mibBuilder.loadTexts:ntntechInterfaceModuleConfigurationMIB.setRevisions(('1902-08-06 11:50','1902-08-28 10:23','1902-10-11 09:40','1902-10-22 02:00','1903-09-30 10:59','1904-10-11 09:32','1904-11-17 10:59'))
_IfModCfgMIBObjects_ObjectIdentity=ObjectIdentity
ifModCfgMIBObjects=_IfModCfgMIBObjects_ObjectIdentity((1,3,6,1,4,1,8059,1,2,1,1))
_IfModCfgParameterConfiguration_ObjectIdentity=ObjectIdentity
ifModCfgParameterConfiguration=_IfModCfgParameterConfiguration_ObjectIdentity((1,3,6,1,4,1,8059,1,2,1,1,1))
_PrmCfgInterface_ObjectIdentity=ObjectIdentity
prmCfgInterface=_PrmCfgInterface_ObjectIdentity((1,3,6,1,4,1,8059,1,2,1,1,1,1))
_PrmCfgInterfacePort_ObjectIdentity=ObjectIdentity
prmCfgInterfacePort=_PrmCfgInterfacePort_ObjectIdentity((1,3,6,1,4,1,8059,1,2,1,1,1,2))
_IfCfgPortTable_Object=MibTable
ifCfgPortTable=_IfCfgPortTable_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,1))
if mibBuilder.loadTexts:ifCfgPortTable.setStatus(_A)
_IfCfgPortEntry_Object=MibTableRow
ifCfgPortEntry=_IfCfgPortEntry_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,1,1))
ifCfgPortEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:ifCfgPortEntry.setStatus(_A)
class _IfCfgSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_IfCfgSlotIndex_Type.__name__=_B
_IfCfgSlotIndex_Object=MibTableColumn
ifCfgSlotIndex=_IfCfgSlotIndex_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,1,1,1),_IfCfgSlotIndex_Type())
ifCfgSlotIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifCfgSlotIndex.setStatus(_A)
class _IfCfgPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_IfCfgPortIndex_Type.__name__=_B
_IfCfgPortIndex_Object=MibTableColumn
ifCfgPortIndex=_IfCfgPortIndex_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,1,1,2),_IfCfgPortIndex_Type())
ifCfgPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifCfgPortIndex.setStatus(_A)
class _IfCfgPortCircuitID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_IfCfgPortCircuitID_Type.__name__=_H
_IfCfgPortCircuitID_Object=MibTableColumn
ifCfgPortCircuitID=_IfCfgPortCircuitID_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,1,1,3),_IfCfgPortCircuitID_Type())
ifCfgPortCircuitID.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortCircuitID.setStatus(_A)
_IfCfgPortFltrIp1Start_Type=IpAddress
_IfCfgPortFltrIp1Start_Object=MibTableColumn
ifCfgPortFltrIp1Start=_IfCfgPortFltrIp1Start_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,1,1,4),_IfCfgPortFltrIp1Start_Type())
ifCfgPortFltrIp1Start.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortFltrIp1Start.setStatus(_A)
_IfCfgPortFltrIp1End_Type=IpAddress
_IfCfgPortFltrIp1End_Object=MibTableColumn
ifCfgPortFltrIp1End=_IfCfgPortFltrIp1End_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,1,1,5),_IfCfgPortFltrIp1End_Type())
ifCfgPortFltrIp1End.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortFltrIp1End.setStatus(_A)
_IfCfgPortFltrIp2Start_Type=IpAddress
_IfCfgPortFltrIp2Start_Object=MibTableColumn
ifCfgPortFltrIp2Start=_IfCfgPortFltrIp2Start_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,1,1,6),_IfCfgPortFltrIp2Start_Type())
ifCfgPortFltrIp2Start.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortFltrIp2Start.setStatus(_A)
_IfCfgPortFltrIp2End_Type=IpAddress
_IfCfgPortFltrIp2End_Object=MibTableColumn
ifCfgPortFltrIp2End=_IfCfgPortFltrIp2End_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,1,1,7),_IfCfgPortFltrIp2End_Type())
ifCfgPortFltrIp2End.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortFltrIp2End.setStatus(_A)
class _IfCfgPortBackboneVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4085))
_IfCfgPortBackboneVlan_Type.__name__=_B
_IfCfgPortBackboneVlan_Object=MibTableColumn
ifCfgPortBackboneVlan=_IfCfgPortBackboneVlan_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,1,1,8),_IfCfgPortBackboneVlan_Type())
ifCfgPortBackboneVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortBackboneVlan.setStatus(_A)
class _IfCfgPortVlanPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_IfCfgPortVlanPriority_Type.__name__=_B
_IfCfgPortVlanPriority_Object=MibTableColumn
ifCfgPortVlanPriority=_IfCfgPortVlanPriority_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,1,1,9),_IfCfgPortVlanPriority_Type())
ifCfgPortVlanPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortVlanPriority.setStatus(_A)
class _IfCfgPortFloodMde_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uplFlood',1),('vlnFlood',2)))
_IfCfgPortFloodMde_Type.__name__=_B
_IfCfgPortFloodMde_Object=MibTableColumn
ifCfgPortFloodMde=_IfCfgPortFloodMde_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,1,1,10),_IfCfgPortFloodMde_Type())
ifCfgPortFloodMde.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortFloodMde.setStatus(_A)
class _IfCfgPortIpFltProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('protocolALL',1),('protocolIP',2)))
_IfCfgPortIpFltProtocol_Type.__name__=_B
_IfCfgPortIpFltProtocol_Object=MibTableColumn
ifCfgPortIpFltProtocol=_IfCfgPortIpFltProtocol_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,1,1,11),_IfCfgPortIpFltProtocol_Type())
ifCfgPortIpFltProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortIpFltProtocol.setStatus(_A)
class _IfCfgPortReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('reset',1),('noReset',2)))
_IfCfgPortReset_Type.__name__=_B
_IfCfgPortReset_Object=MibTableColumn
ifCfgPortReset=_IfCfgPortReset_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,1,1,12),_IfCfgPortReset_Type())
ifCfgPortReset.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortReset.setStatus(_A)
class _IfCfgPortBkBoneEthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ethtype8100',1),('ethtype9100',2)))
_IfCfgPortBkBoneEthType_Type.__name__=_B
_IfCfgPortBkBoneEthType_Object=MibTableColumn
ifCfgPortBkBoneEthType=_IfCfgPortBkBoneEthType_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,1,1,13),_IfCfgPortBkBoneEthType_Type())
ifCfgPortBkBoneEthType.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortBkBoneEthType.setStatus(_A)
_IfCfgPortVLANTable_Object=MibTable
ifCfgPortVLANTable=_IfCfgPortVLANTable_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,2))
if mibBuilder.loadTexts:ifCfgPortVLANTable.setStatus(_A)
_IfCfgPortVLANEntry_Object=MibTableRow
ifCfgPortVLANEntry=_IfCfgPortVLANEntry_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,2,1))
ifCfgPortVLANEntry.setIndexNames((0,_E,_K),(0,_E,_L),(0,_E,_M))
if mibBuilder.loadTexts:ifCfgPortVLANEntry.setStatus(_A)
class _IfCfgIfSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_IfCfgIfSlotIndex_Type.__name__=_B
_IfCfgIfSlotIndex_Object=MibTableColumn
ifCfgIfSlotIndex=_IfCfgIfSlotIndex_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,2,1,1),_IfCfgIfSlotIndex_Type())
ifCfgIfSlotIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifCfgIfSlotIndex.setStatus(_A)
class _IfCfgIfPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_IfCfgIfPortIndex_Type.__name__=_B
_IfCfgIfPortIndex_Object=MibTableColumn
ifCfgIfPortIndex=_IfCfgIfPortIndex_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,2,1,2),_IfCfgIfPortIndex_Type())
ifCfgIfPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifCfgIfPortIndex.setStatus(_A)
class _IfCfgVLANIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_IfCfgVLANIndex_Type.__name__=_B
_IfCfgVLANIndex_Object=MibTableColumn
ifCfgVLANIndex=_IfCfgVLANIndex_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,2,1,3),_IfCfgVLANIndex_Type())
ifCfgVLANIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifCfgVLANIndex.setStatus(_A)
class _IfCfgVLANIdStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4085))
_IfCfgVLANIdStart_Type.__name__=_B
_IfCfgVLANIdStart_Object=MibTableColumn
ifCfgVLANIdStart=_IfCfgVLANIdStart_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,2,1,4),_IfCfgVLANIdStart_Type())
ifCfgVLANIdStart.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgVLANIdStart.setStatus(_A)
class _IfCfgVLANIdEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4085))
_IfCfgVLANIdEnd_Type.__name__=_B
_IfCfgVLANIdEnd_Object=MibTableColumn
ifCfgVLANIdEnd=_IfCfgVLANIdEnd_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,2,1,5),_IfCfgVLANIdEnd_Type())
ifCfgVLANIdEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgVLANIdEnd.setStatus(_A)
_IfCfgPortAdslTable_Object=MibTable
ifCfgPortAdslTable=_IfCfgPortAdslTable_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3))
if mibBuilder.loadTexts:ifCfgPortAdslTable.setStatus(_A)
_IfCfgPortAdslEntry_Object=MibTableRow
ifCfgPortAdslEntry=_IfCfgPortAdslEntry_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1))
ifCfgPortAdslEntry.setIndexNames((0,_E,_N),(0,_E,_O))
if mibBuilder.loadTexts:ifCfgPortAdslEntry.setStatus(_A)
class _IfCfgAdslSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_IfCfgAdslSlotIndex_Type.__name__=_B
_IfCfgAdslSlotIndex_Object=MibTableColumn
ifCfgAdslSlotIndex=_IfCfgAdslSlotIndex_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,1),_IfCfgAdslSlotIndex_Type())
ifCfgAdslSlotIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifCfgAdslSlotIndex.setStatus(_A)
class _IfCfgAdslPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_IfCfgAdslPortIndex_Type.__name__=_B
_IfCfgAdslPortIndex_Object=MibTableColumn
ifCfgAdslPortIndex=_IfCfgAdslPortIndex_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,2),_IfCfgAdslPortIndex_Type())
ifCfgAdslPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifCfgAdslPortIndex.setStatus(_A)
class _IfCfgPortAdslPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('on',1),(_G,2),('adaptive',3),('fixedadaptive',4)))
_IfCfgPortAdslPortMode_Type.__name__=_B
_IfCfgPortAdslPortMode_Object=MibTableColumn
ifCfgPortAdslPortMode=_IfCfgPortAdslPortMode_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,3),_IfCfgPortAdslPortMode_Type())
ifCfgPortAdslPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortAdslPortMode.setStatus(_A)
class _IfCfgPortAdslVpiVciDetect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_G,2)))
_IfCfgPortAdslVpiVciDetect_Type.__name__=_B
_IfCfgPortAdslVpiVciDetect_Object=MibTableColumn
ifCfgPortAdslVpiVciDetect=_IfCfgPortAdslVpiVciDetect_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,4),_IfCfgPortAdslVpiVciDetect_Type())
ifCfgPortAdslVpiVciDetect.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortAdslVpiVciDetect.setStatus(_A)
class _IfCfgPortAdslRxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_IfCfgPortAdslRxRate_Type.__name__=_B
_IfCfgPortAdslRxRate_Object=MibTableColumn
ifCfgPortAdslRxRate=_IfCfgPortAdslRxRate_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,5),_IfCfgPortAdslRxRate_Type())
ifCfgPortAdslRxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortAdslRxRate.setStatus(_A)
if mibBuilder.loadTexts:ifCfgPortAdslRxRate.setUnits(_F)
class _IfCfgPortAdslTxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,252))
_IfCfgPortAdslTxRate_Type.__name__=_B
_IfCfgPortAdslTxRate_Object=MibTableColumn
ifCfgPortAdslTxRate=_IfCfgPortAdslTxRate_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,6),_IfCfgPortAdslTxRate_Type())
ifCfgPortAdslTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortAdslTxRate.setStatus(_A)
if mibBuilder.loadTexts:ifCfgPortAdslTxRate.setUnits(_F)
class _IfCfgPortAdslFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('frameType1483LLC',1),('frameType1483VCM',2)))
_IfCfgPortAdslFrameType_Type.__name__=_B
_IfCfgPortAdslFrameType_Object=MibTableColumn
ifCfgPortAdslFrameType=_IfCfgPortAdslFrameType_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,7),_IfCfgPortAdslFrameType_Type())
ifCfgPortAdslFrameType.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortAdslFrameType.setStatus(_A)
class _IfCfgPortAdslVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IfCfgPortAdslVpi_Type.__name__=_B
_IfCfgPortAdslVpi_Object=MibTableColumn
ifCfgPortAdslVpi=_IfCfgPortAdslVpi_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,8),_IfCfgPortAdslVpi_Type())
ifCfgPortAdslVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortAdslVpi.setStatus(_A)
class _IfCfgPortAdslVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IfCfgPortAdslVci_Type.__name__=_B
_IfCfgPortAdslVci_Object=MibTableColumn
ifCfgPortAdslVci=_IfCfgPortAdslVci_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,9),_IfCfgPortAdslVci_Type())
ifCfgPortAdslVci.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortAdslVci.setStatus(_A)
class _IfCfgPortAdslStandardMde_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,255)));namedValues=NamedValues(*(('t1413',1),('gLite',2),('gDMT',3),(_P,4),(_Q,5),(_R,6),(_S,7),(_T,8),(_U,9),(_V,255)))
_IfCfgPortAdslStandardMde_Type.__name__=_B
_IfCfgPortAdslStandardMde_Object=MibTableColumn
ifCfgPortAdslStandardMde=_IfCfgPortAdslStandardMde_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,10),_IfCfgPortAdslStandardMde_Type())
ifCfgPortAdslStandardMde.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortAdslStandardMde.setStatus(_A)
class _IfCfgPortAdslCorrectionUp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6)))
_IfCfgPortAdslCorrectionUp_Type.__name__=_B
_IfCfgPortAdslCorrectionUp_Object=MibTableColumn
ifCfgPortAdslCorrectionUp=_IfCfgPortAdslCorrectionUp_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,11),_IfCfgPortAdslCorrectionUp_Type())
ifCfgPortAdslCorrectionUp.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortAdslCorrectionUp.setStatus(_A)
class _IfCfgPortAdslCorrectionDn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6)))
_IfCfgPortAdslCorrectionDn_Type.__name__=_B
_IfCfgPortAdslCorrectionDn_Object=MibTableColumn
ifCfgPortAdslCorrectionDn=_IfCfgPortAdslCorrectionDn_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,12),_IfCfgPortAdslCorrectionDn_Type())
ifCfgPortAdslCorrectionDn.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortAdslCorrectionDn.setStatus(_A)
class _IfCfgPortAdslDelayUp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3),(_f,4),(_g,5),(_h,6),(_i,7)))
_IfCfgPortAdslDelayUp_Type.__name__=_B
_IfCfgPortAdslDelayUp_Object=MibTableColumn
ifCfgPortAdslDelayUp=_IfCfgPortAdslDelayUp_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,13),_IfCfgPortAdslDelayUp_Type())
ifCfgPortAdslDelayUp.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortAdslDelayUp.setStatus(_A)
class _IfCfgPortAdslDelayDn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_c,1),(_d,2),(_e,3),(_f,4),(_g,5),(_h,6),(_i,7)))
_IfCfgPortAdslDelayDn_Type.__name__=_B
_IfCfgPortAdslDelayDn_Object=MibTableColumn
ifCfgPortAdslDelayDn=_IfCfgPortAdslDelayDn_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,14),_IfCfgPortAdslDelayDn_Type())
ifCfgPortAdslDelayDn.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortAdslDelayDn.setStatus(_A)
class _IfCfgPortAdslEcFdm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ec',1),('fdm',2)))
_IfCfgPortAdslEcFdm_Type.__name__=_B
_IfCfgPortAdslEcFdm_Object=MibTableColumn
ifCfgPortAdslEcFdm=_IfCfgPortAdslEcFdm_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,15),_IfCfgPortAdslEcFdm_Type())
ifCfgPortAdslEcFdm.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortAdslEcFdm.setStatus(_A)
class _IfCfgPortAdslFastBuffer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_G,2)))
_IfCfgPortAdslFastBuffer_Type.__name__=_B
_IfCfgPortAdslFastBuffer_Object=MibTableColumn
ifCfgPortAdslFastBuffer=_IfCfgPortAdslFastBuffer_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,16),_IfCfgPortAdslFastBuffer_Type())
ifCfgPortAdslFastBuffer.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortAdslFastBuffer.setStatus(_A)
class _IfCfgPortAdslSnrUp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_IfCfgPortAdslSnrUp_Type.__name__=_B
_IfCfgPortAdslSnrUp_Object=MibTableColumn
ifCfgPortAdslSnrUp=_IfCfgPortAdslSnrUp_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,17),_IfCfgPortAdslSnrUp_Type())
ifCfgPortAdslSnrUp.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortAdslSnrUp.setStatus(_A)
class _IfCfgPortAdslSnrDn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_IfCfgPortAdslSnrDn_Type.__name__=_B
_IfCfgPortAdslSnrDn_Object=MibTableColumn
ifCfgPortAdslSnrDn=_IfCfgPortAdslSnrDn_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,18),_IfCfgPortAdslSnrDn_Type())
ifCfgPortAdslSnrDn.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortAdslSnrDn.setStatus(_A)
class _IfCfgPortAdslActualRxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_IfCfgPortAdslActualRxRate_Type.__name__=_B
_IfCfgPortAdslActualRxRate_Object=MibTableColumn
ifCfgPortAdslActualRxRate=_IfCfgPortAdslActualRxRate_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,19),_IfCfgPortAdslActualRxRate_Type())
ifCfgPortAdslActualRxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ifCfgPortAdslActualRxRate.setStatus(_A)
if mibBuilder.loadTexts:ifCfgPortAdslActualRxRate.setUnits(_F)
class _IfCfgPortAdslActualTxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_IfCfgPortAdslActualTxRate_Type.__name__=_B
_IfCfgPortAdslActualTxRate_Object=MibTableColumn
ifCfgPortAdslActualTxRate=_IfCfgPortAdslActualTxRate_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,20),_IfCfgPortAdslActualTxRate_Type())
ifCfgPortAdslActualTxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:ifCfgPortAdslActualTxRate.setStatus(_A)
if mibBuilder.loadTexts:ifCfgPortAdslActualTxRate.setUnits(_F)
class _IfCfgPortAdslActualStandardMde_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,255)));namedValues=NamedValues(*(('t1413',1),('gLite',2),('gDMT',3),(_P,4),(_Q,5),(_R,6),(_S,7),(_T,8),(_U,9),(_V,255)))
_IfCfgPortAdslActualStandardMde_Type.__name__=_B
_IfCfgPortAdslActualStandardMde_Object=MibTableColumn
ifCfgPortAdslActualStandardMde=_IfCfgPortAdslActualStandardMde_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,21),_IfCfgPortAdslActualStandardMde_Type())
ifCfgPortAdslActualStandardMde.setMaxAccess(_D)
if mibBuilder.loadTexts:ifCfgPortAdslActualStandardMde.setStatus(_A)
class _IfCfgPortAdslActualDepthUp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_IfCfgPortAdslActualDepthUp_Type.__name__=_B
_IfCfgPortAdslActualDepthUp_Object=MibTableColumn
ifCfgPortAdslActualDepthUp=_IfCfgPortAdslActualDepthUp_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,22),_IfCfgPortAdslActualDepthUp_Type())
ifCfgPortAdslActualDepthUp.setMaxAccess(_D)
if mibBuilder.loadTexts:ifCfgPortAdslActualDepthUp.setStatus(_A)
class _IfCfgPortAdslActualDepthDn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_IfCfgPortAdslActualDepthDn_Type.__name__=_B
_IfCfgPortAdslActualDepthDn_Object=MibTableColumn
ifCfgPortAdslActualDepthDn=_IfCfgPortAdslActualDepthDn_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,3,1,23),_IfCfgPortAdslActualDepthDn_Type())
ifCfgPortAdslActualDepthDn.setMaxAccess(_D)
if mibBuilder.loadTexts:ifCfgPortAdslActualDepthDn.setStatus(_A)
_IfCfgPortIdslTable_Object=MibTable
ifCfgPortIdslTable=_IfCfgPortIdslTable_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,4))
if mibBuilder.loadTexts:ifCfgPortIdslTable.setStatus(_A)
_IfCfgPortIdslEntry_Object=MibTableRow
ifCfgPortIdslEntry=_IfCfgPortIdslEntry_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,4,1))
ifCfgPortIdslEntry.setIndexNames((0,_E,_j),(0,_E,_k))
if mibBuilder.loadTexts:ifCfgPortIdslEntry.setStatus(_A)
class _IfCfgIdslSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_IfCfgIdslSlotIndex_Type.__name__=_B
_IfCfgIdslSlotIndex_Object=MibTableColumn
ifCfgIdslSlotIndex=_IfCfgIdslSlotIndex_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,4,1,1),_IfCfgIdslSlotIndex_Type())
ifCfgIdslSlotIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifCfgIdslSlotIndex.setStatus(_A)
class _IfCfgIdslPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_IfCfgIdslPortIndex_Type.__name__=_B
_IfCfgIdslPortIndex_Object=MibTableColumn
ifCfgIdslPortIndex=_IfCfgIdslPortIndex_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,4,1,2),_IfCfgIdslPortIndex_Type())
ifCfgIdslPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifCfgIdslPortIndex.setStatus(_A)
class _IfCfgPortIdslRxTxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,255)));namedValues=NamedValues(*(('idslRxTxRateDefect',0),('idslRxTxRate128',1),('idslRxTxRate144',2),('idslRxTxRateOff',255)))
_IfCfgPortIdslRxTxRate_Type.__name__=_B
_IfCfgPortIdslRxTxRate_Object=MibTableColumn
ifCfgPortIdslRxTxRate=_IfCfgPortIdslRxTxRate_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,4,1,3),_IfCfgPortIdslRxTxRate_Type())
ifCfgPortIdslRxTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortIdslRxTxRate.setStatus(_A)
if mibBuilder.loadTexts:ifCfgPortIdslRxTxRate.setUnits(_F)
_IfCfgPortSdslTable_Object=MibTable
ifCfgPortSdslTable=_IfCfgPortSdslTable_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,5))
if mibBuilder.loadTexts:ifCfgPortSdslTable.setStatus(_A)
_IfCfgPortSdslEntry_Object=MibTableRow
ifCfgPortSdslEntry=_IfCfgPortSdslEntry_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,5,1))
ifCfgPortSdslEntry.setIndexNames((0,_E,_l),(0,_E,_m))
if mibBuilder.loadTexts:ifCfgPortSdslEntry.setStatus(_A)
class _IfCfgSdslSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_IfCfgSdslSlotIndex_Type.__name__=_B
_IfCfgSdslSlotIndex_Object=MibTableColumn
ifCfgSdslSlotIndex=_IfCfgSdslSlotIndex_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,5,1,1),_IfCfgSdslSlotIndex_Type())
ifCfgSdslSlotIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifCfgSdslSlotIndex.setStatus(_A)
class _IfCfgSdslPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_IfCfgSdslPortIndex_Type.__name__=_B
_IfCfgSdslPortIndex_Object=MibTableColumn
ifCfgSdslPortIndex=_IfCfgSdslPortIndex_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,5,1,2),_IfCfgSdslPortIndex_Type())
ifCfgSdslPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifCfgSdslPortIndex.setStatus(_A)
class _IfCfgPortSdslRxTxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,255)));namedValues=NamedValues(*(('sdslRxTxRateDefect',0),('sdslRxTxRate144',1),('sdslRxTxRate272',2),('sdslRxTxRate400',3),('sdslRxTxRate528',4),('sdslRxTxRate784',5),('sdslRxTxRate1040',6),('sdslRxTxRate1168',7),('sdslRxTxRate1552',8),('sdslRxTxRate2064',9),('sdslRxTxRate2320',10),('sdslRxTxRateOff',255)))
_IfCfgPortSdslRxTxRate_Type.__name__=_B
_IfCfgPortSdslRxTxRate_Object=MibTableColumn
ifCfgPortSdslRxTxRate=_IfCfgPortSdslRxTxRate_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,5,1,3),_IfCfgPortSdslRxTxRate_Type())
ifCfgPortSdslRxTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortSdslRxTxRate.setStatus(_A)
if mibBuilder.loadTexts:ifCfgPortSdslRxTxRate.setUnits(_F)
class _IfCfgPortSdslLineCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('lineCodeCap',1),('lineCode2B1Q',2),('lineCodeGSHDSL',3)))
_IfCfgPortSdslLineCode_Type.__name__=_B
_IfCfgPortSdslLineCode_Object=MibTableColumn
ifCfgPortSdslLineCode=_IfCfgPortSdslLineCode_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,5,1,4),_IfCfgPortSdslLineCode_Type())
ifCfgPortSdslLineCode.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortSdslLineCode.setStatus(_A)
_IfCfgPortT1Table_Object=MibTable
ifCfgPortT1Table=_IfCfgPortT1Table_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,6))
if mibBuilder.loadTexts:ifCfgPortT1Table.setStatus(_A)
_IfCfgPortT1Entry_Object=MibTableRow
ifCfgPortT1Entry=_IfCfgPortT1Entry_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,6,1))
ifCfgPortT1Entry.setIndexNames((0,_E,_n),(0,_E,_o))
if mibBuilder.loadTexts:ifCfgPortT1Entry.setStatus(_A)
class _IfCfgT1SlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_IfCfgT1SlotIndex_Type.__name__=_B
_IfCfgT1SlotIndex_Object=MibTableColumn
ifCfgT1SlotIndex=_IfCfgT1SlotIndex_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,6,1,1),_IfCfgT1SlotIndex_Type())
ifCfgT1SlotIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifCfgT1SlotIndex.setStatus(_A)
class _IfCfgT1PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_IfCfgT1PortIndex_Type.__name__=_B
_IfCfgT1PortIndex_Object=MibTableColumn
ifCfgT1PortIndex=_IfCfgT1PortIndex_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,6,1,2),_IfCfgT1PortIndex_Type())
ifCfgT1PortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifCfgT1PortIndex.setStatus(_A)
class _IfCfgPortT1RxTxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,255)));namedValues=NamedValues(*(('t1RxTxRateDefect',0),('t1RxTxRate192',1),('t1RxTxRate384',2),('t1RxTxRate576',3),('t1RxTxRate768',4),('t1RxTxRate960',5),('t1RxTxRate1152',6),('t1RxTxRate1344',7),('t1RxTxRate1536',8),('t1RxTxRateOff',255)))
_IfCfgPortT1RxTxRate_Type.__name__=_B
_IfCfgPortT1RxTxRate_Object=MibTableColumn
ifCfgPortT1RxTxRate=_IfCfgPortT1RxTxRate_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,6,1,3),_IfCfgPortT1RxTxRate_Type())
ifCfgPortT1RxTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortT1RxTxRate.setStatus(_A)
if mibBuilder.loadTexts:ifCfgPortT1RxTxRate.setUnits(_F)
class _IfCfgPortT1FrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('t1frameTypeESF',1),('t1frameTypeSFD4',2)))
_IfCfgPortT1FrameType_Type.__name__=_B
_IfCfgPortT1FrameType_Object=MibTableColumn
ifCfgPortT1FrameType=_IfCfgPortT1FrameType_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,6,1,4),_IfCfgPortT1FrameType_Type())
ifCfgPortT1FrameType.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortT1FrameType.setStatus(_A)
class _IfCfgPortT1LineCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('t1lineCodeB8ZS',1),('t1lineCodeAMI',2)))
_IfCfgPortT1LineCode_Type.__name__=_B
_IfCfgPortT1LineCode_Object=MibTableColumn
ifCfgPortT1LineCode=_IfCfgPortT1LineCode_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,6,1,5),_IfCfgPortT1LineCode_Type())
ifCfgPortT1LineCode.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortT1LineCode.setStatus(_A)
class _IfCfgPortT1TxBuildOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('t1TxBuildOut0db',1),('t1TxBuildOutN7p5db',2),('t1TxBuildOutN15db',3),('t1TxBuildOutN22db',4)))
_IfCfgPortT1TxBuildOut_Type.__name__=_B
_IfCfgPortT1TxBuildOut_Object=MibTableColumn
ifCfgPortT1TxBuildOut=_IfCfgPortT1TxBuildOut_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,6,1,6),_IfCfgPortT1TxBuildOut_Type())
ifCfgPortT1TxBuildOut.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortT1TxBuildOut.setStatus(_A)
class _IfCfgPortT1ClockSrc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('t1ClockSrcLocal',1),('t1ClockSrcLoop',2)))
_IfCfgPortT1ClockSrc_Type.__name__=_B
_IfCfgPortT1ClockSrc_Object=MibTableColumn
ifCfgPortT1ClockSrc=_IfCfgPortT1ClockSrc_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,6,1,7),_IfCfgPortT1ClockSrc_Type())
ifCfgPortT1ClockSrc.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortT1ClockSrc.setStatus(_A)
_IfCfgPortE1Table_Object=MibTable
ifCfgPortE1Table=_IfCfgPortE1Table_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,7))
if mibBuilder.loadTexts:ifCfgPortE1Table.setStatus(_A)
_IfCfgPortE1Entry_Object=MibTableRow
ifCfgPortE1Entry=_IfCfgPortE1Entry_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,7,1))
ifCfgPortE1Entry.setIndexNames((0,_E,_p),(0,_E,_q))
if mibBuilder.loadTexts:ifCfgPortE1Entry.setStatus(_A)
class _IfCfgE1SlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_IfCfgE1SlotIndex_Type.__name__=_B
_IfCfgE1SlotIndex_Object=MibTableColumn
ifCfgE1SlotIndex=_IfCfgE1SlotIndex_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,7,1,1),_IfCfgE1SlotIndex_Type())
ifCfgE1SlotIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifCfgE1SlotIndex.setStatus(_A)
class _IfCfgE1PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_IfCfgE1PortIndex_Type.__name__=_B
_IfCfgE1PortIndex_Object=MibTableColumn
ifCfgE1PortIndex=_IfCfgE1PortIndex_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,7,1,2),_IfCfgE1PortIndex_Type())
ifCfgE1PortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ifCfgE1PortIndex.setStatus(_A)
class _IfCfgPortE1RxTxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,255)));namedValues=NamedValues(*(('e1RxTxRateDefect',0),('e1RxTxRate256',1),('e1RxTxRate512',2),('e1RxTxRate768',3),('e1RxTxRate1024',4),('e1RxTxRate1280',5),('e1RxTxRate1536',6),('e1RxTxRate1792',7),('e1RxTxRate1984',8),('e1RxTxRateOff',255)))
_IfCfgPortE1RxTxRate_Type.__name__=_B
_IfCfgPortE1RxTxRate_Object=MibTableColumn
ifCfgPortE1RxTxRate=_IfCfgPortE1RxTxRate_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,7,1,3),_IfCfgPortE1RxTxRate_Type())
ifCfgPortE1RxTxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortE1RxTxRate.setStatus(_A)
if mibBuilder.loadTexts:ifCfgPortE1RxTxRate.setUnits(_F)
class _IfCfgPortE1FrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('e1frameTypeCRC',1),('e1frameTypeNoCRC',2)))
_IfCfgPortE1FrameType_Type.__name__=_B
_IfCfgPortE1FrameType_Object=MibTableColumn
ifCfgPortE1FrameType=_IfCfgPortE1FrameType_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,7,1,4),_IfCfgPortE1FrameType_Type())
ifCfgPortE1FrameType.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortE1FrameType.setStatus(_A)
class _IfCfgPortE1LineCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('e1lineCodeHDB3',1),('e1lineCodeAMI',2)))
_IfCfgPortE1LineCode_Type.__name__=_B
_IfCfgPortE1LineCode_Object=MibTableColumn
ifCfgPortE1LineCode=_IfCfgPortE1LineCode_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,7,1,5),_IfCfgPortE1LineCode_Type())
ifCfgPortE1LineCode.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortE1LineCode.setStatus(_A)
class _IfCfgPortE1ClockSrc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('e1ClockSrcLocal',1),('e1ClockSrcLoop',2)))
_IfCfgPortE1ClockSrc_Type.__name__=_B
_IfCfgPortE1ClockSrc_Object=MibTableColumn
ifCfgPortE1ClockSrc=_IfCfgPortE1ClockSrc_Object((1,3,6,1,4,1,8059,1,2,1,1,1,2,7,1,6),_IfCfgPortE1ClockSrc_Type())
ifCfgPortE1ClockSrc.setMaxAccess(_C)
if mibBuilder.loadTexts:ifCfgPortE1ClockSrc.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ntntechInterfaceModuleConfigurationMIB':ntntechInterfaceModuleConfigurationMIB,'ifModCfgMIBObjects':ifModCfgMIBObjects,'ifModCfgParameterConfiguration':ifModCfgParameterConfiguration,'prmCfgInterface':prmCfgInterface,'prmCfgInterfacePort':prmCfgInterfacePort,'ifCfgPortTable':ifCfgPortTable,'ifCfgPortEntry':ifCfgPortEntry,_I:ifCfgSlotIndex,_J:ifCfgPortIndex,'ifCfgPortCircuitID':ifCfgPortCircuitID,'ifCfgPortFltrIp1Start':ifCfgPortFltrIp1Start,'ifCfgPortFltrIp1End':ifCfgPortFltrIp1End,'ifCfgPortFltrIp2Start':ifCfgPortFltrIp2Start,'ifCfgPortFltrIp2End':ifCfgPortFltrIp2End,'ifCfgPortBackboneVlan':ifCfgPortBackboneVlan,'ifCfgPortVlanPriority':ifCfgPortVlanPriority,'ifCfgPortFloodMde':ifCfgPortFloodMde,'ifCfgPortIpFltProtocol':ifCfgPortIpFltProtocol,'ifCfgPortReset':ifCfgPortReset,'ifCfgPortBkBoneEthType':ifCfgPortBkBoneEthType,'ifCfgPortVLANTable':ifCfgPortVLANTable,'ifCfgPortVLANEntry':ifCfgPortVLANEntry,_K:ifCfgIfSlotIndex,_L:ifCfgIfPortIndex,_M:ifCfgVLANIndex,'ifCfgVLANIdStart':ifCfgVLANIdStart,'ifCfgVLANIdEnd':ifCfgVLANIdEnd,'ifCfgPortAdslTable':ifCfgPortAdslTable,'ifCfgPortAdslEntry':ifCfgPortAdslEntry,_N:ifCfgAdslSlotIndex,_O:ifCfgAdslPortIndex,'ifCfgPortAdslPortMode':ifCfgPortAdslPortMode,'ifCfgPortAdslVpiVciDetect':ifCfgPortAdslVpiVciDetect,'ifCfgPortAdslRxRate':ifCfgPortAdslRxRate,'ifCfgPortAdslTxRate':ifCfgPortAdslTxRate,'ifCfgPortAdslFrameType':ifCfgPortAdslFrameType,'ifCfgPortAdslVpi':ifCfgPortAdslVpi,'ifCfgPortAdslVci':ifCfgPortAdslVci,'ifCfgPortAdslStandardMde':ifCfgPortAdslStandardMde,'ifCfgPortAdslCorrectionUp':ifCfgPortAdslCorrectionUp,'ifCfgPortAdslCorrectionDn':ifCfgPortAdslCorrectionDn,'ifCfgPortAdslDelayUp':ifCfgPortAdslDelayUp,'ifCfgPortAdslDelayDn':ifCfgPortAdslDelayDn,'ifCfgPortAdslEcFdm':ifCfgPortAdslEcFdm,'ifCfgPortAdslFastBuffer':ifCfgPortAdslFastBuffer,'ifCfgPortAdslSnrUp':ifCfgPortAdslSnrUp,'ifCfgPortAdslSnrDn':ifCfgPortAdslSnrDn,'ifCfgPortAdslActualRxRate':ifCfgPortAdslActualRxRate,'ifCfgPortAdslActualTxRate':ifCfgPortAdslActualTxRate,'ifCfgPortAdslActualStandardMde':ifCfgPortAdslActualStandardMde,'ifCfgPortAdslActualDepthUp':ifCfgPortAdslActualDepthUp,'ifCfgPortAdslActualDepthDn':ifCfgPortAdslActualDepthDn,'ifCfgPortIdslTable':ifCfgPortIdslTable,'ifCfgPortIdslEntry':ifCfgPortIdslEntry,_j:ifCfgIdslSlotIndex,_k:ifCfgIdslPortIndex,'ifCfgPortIdslRxTxRate':ifCfgPortIdslRxTxRate,'ifCfgPortSdslTable':ifCfgPortSdslTable,'ifCfgPortSdslEntry':ifCfgPortSdslEntry,_l:ifCfgSdslSlotIndex,_m:ifCfgSdslPortIndex,'ifCfgPortSdslRxTxRate':ifCfgPortSdslRxTxRate,'ifCfgPortSdslLineCode':ifCfgPortSdslLineCode,'ifCfgPortT1Table':ifCfgPortT1Table,'ifCfgPortT1Entry':ifCfgPortT1Entry,_n:ifCfgT1SlotIndex,_o:ifCfgT1PortIndex,'ifCfgPortT1RxTxRate':ifCfgPortT1RxTxRate,'ifCfgPortT1FrameType':ifCfgPortT1FrameType,'ifCfgPortT1LineCode':ifCfgPortT1LineCode,'ifCfgPortT1TxBuildOut':ifCfgPortT1TxBuildOut,'ifCfgPortT1ClockSrc':ifCfgPortT1ClockSrc,'ifCfgPortE1Table':ifCfgPortE1Table,'ifCfgPortE1Entry':ifCfgPortE1Entry,_p:ifCfgE1SlotIndex,_q:ifCfgE1PortIndex,'ifCfgPortE1RxTxRate':ifCfgPortE1RxTxRate,'ifCfgPortE1FrameType':ifCfgPortE1FrameType,'ifCfgPortE1LineCode':ifCfgPortE1LineCode,'ifCfgPortE1ClockSrc':ifCfgPortE1ClockSrc})