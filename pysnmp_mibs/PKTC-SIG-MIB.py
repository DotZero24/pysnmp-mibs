_AQ='pktcNcsGroup'
_AP='pktcSigGroup'
_AO='pktcSigNcsServiceFlowState'
_AN='pktcSigServiceClassNameMask'
_AM='pktcSigServiceClassNameDS'
_AL='pktcSigServiceClassNameUS'
_AK='pktcNcsEndPntStatusError'
_AJ='pktcNcsEndPntStatusCallIpAddress'
_AI='pktcNcsEndPntConfigCallWaitingDelay'
_AH='pktcNcsEndPntConfigCallWaitingMaxRep'
_AG='pktcNcsEndPntConfigStatus'
_AF='pktcNcsEndPntConfigThist'
_AE='pktcNcsEndPntConfigLongDurationKeepAlive'
_AD='pktcNcsEndPntConfigRtoInit'
_AC='pktcNcsEndPntConfigRtoMax'
_AB='pktcNcsEndPntConfigTdmax'
_AA='pktcNcsEndPntConfigTdmin'
_A9='pktcNcsEndPntConfigTdinit'
_A8='pktcNcsEndPntConfigMWD'
_A7='pktcNcsEndPntConfigMax2QEnable'
_A6='pktcNcsEndPntConfigMax1QEnable'
_A5='pktcNcsEndPntConfigMax2'
_A4='pktcNcsEndPntConfigMax1'
_A3='pktcNcsEndPntConfigTSMax'
_A2='pktcNcsEndPntConfigStutterDialToneTO'
_A1='pktcNcsEndPntConfigReorderToneTO'
_A0='pktcNcsEndPntConfigRingBackTO'
_z='pktcNcsEndPntConfigRingingTO'
_y='pktcNcsEndPntConfigOffHookWarnToneTO'
_x='pktcNcsEndPntConfigMessageWaitingTO'
_w='pktcNcsEndPntConfigDialToneTO'
_v='pktcNcsEndPntConfigBusyToneTO'
_u='pktcNcsEndPntConfigCriticalDialTO'
_t='pktcNcsEndPntConfigPartialDialTO'
_s='pktcNcsEndPntConfigCallAgentUdpPort'
_r='pktcNcsEndPntConfigCallAgentId'
_q='pktcSigDevRtCadence'
_p='pktcSigDevRsCadence'
_o='pktcSigDevRgCadence'
_n='pktcSigDevR5Cadence'
_m='pktcSigDevR4Cadence'
_l='pktcSigDevR3Cadence'
_k='pktcSigDevR2Cadence'
_j='pktcSigDevR1Cadence'
_i='pktcSigDefNcsReceiveUdpPort'
_h='pktcSigEndPntCapabilityIndex'
_g='pktcSignalingVendorExtension'
_f='pktcSignalingVersion'
_e='pktcSignalingType'
_d='pktcSigTosFormatSelector'
_c='pktcSigDefMediaStreamTos'
_b='pktcSigDefCallSigTos'
_a='pktcSigDevR7Cadence'
_Z='pktcSigDevR6Cadence'
_Y='pktcSigDevR0Cadence'
_X='pktcSigDevConnectionMode'
_W='pktcSigDevSilenceSuppression'
_V='pktcSigDevEchoCancellation'
_U='pktcSigDevCodecMax'
_T='pktcSigDevCodecType'
_S='1111100000000000000000000000000000000000000000000000000000001'
_R='pktcSignalingIndex'
_Q='not-accessible'
_P='pktcSigDevCodecIndex'
_O='unknown'
_N='TruthValue'
_M='ifIndex'
_L='IF-MIB'
_K='SnmpAdminString'
_J='obsolete'
_I='11111111111111111111'
_H='read-only'
_G='PktcRingCadence'
_F='seconds'
_E='read-write'
_D='read-create'
_C='Integer32'
_B='PKTC-SIG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
clabProjPacketCable,=mibBuilder.importSymbols('CLAB-DEF-MIB','clabProjPacketCable')
ifIndex,=mibBuilder.importSymbols(_L,_M)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_N)
pktcSigMib=ModuleIdentity((1,3,6,1,4,1,4491,2,2,2))
if mibBuilder.loadTexts:pktcSigMib.setRevisions(('2005-01-28 00:00',))
class PktcCodecType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('other',1),(_O,2),('g729',3),('reserved',4),('g729E',5),('pcmu',6),('g726at32',7),('g728',8),('pcma',9),('g726at16',10),('g726at24',11),('g726at40',12),('ilbc',13),('bv16',14)))
class PktcRingCadence(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('interval1',0),('interval2',1),('interval3',2),('interval4',3),('interval5',4),('interval6',5),('interval7',6),('interval8',7),('interval9',8),('interval10',9),('interval11',10),('interval12',11),('interval13',12),('interval14',13),('interval15',14),('interval16',15),('interval17',16),('interval18',17),('interval19',18),('interval20',19),('interval21',20),('interval22',21),('interval23',22),('interval24',23),('interval25',24),('interval26',25),('interval27',26),('interval28',27),('interval29',28),('interval30',29),('interval31',30),('interval32',31),('interval33',32),('interval34',33),('interval35',34),('interval36',35),('interval37',36),('interval38',37),('interval39',38),('interval40',39),('interval41',40),('interval42',41),('interval43',42),('interval44',43),('interval45',44),('interval46',45),('interval47',46),('interval48',47),('interval49',48),('interval50',49),('interval51',50),('interval52',51),('interval53',52),('interval54',53),('interval55',54),('interval56',55),('interval57',56),('interval58',57),('interval59',58),('interval60',59),('interval61',60),('interval62',61),('interval63',62),('interval64',63)))
class PktcSigType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),(_O,2),('ncs',3),('dcs',4)))
_PktcSigMibObjects_ObjectIdentity=ObjectIdentity
pktcSigMibObjects=_PktcSigMibObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,2,2,1))
_PktcSigDevConfigObjects_ObjectIdentity=ObjectIdentity
pktcSigDevConfigObjects=_PktcSigDevConfigObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,2,2,1,1))
_PktcSigDevCodecTable_Object=MibTable
pktcSigDevCodecTable=_PktcSigDevCodecTable_Object((1,3,6,1,4,1,4491,2,2,2,1,1,1))
if mibBuilder.loadTexts:pktcSigDevCodecTable.setStatus(_A)
_PktcSigDevCodecEntry_Object=MibTableRow
pktcSigDevCodecEntry=_PktcSigDevCodecEntry_Object((1,3,6,1,4,1,4491,2,2,2,1,1,1,1))
pktcSigDevCodecEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:pktcSigDevCodecEntry.setStatus(_A)
class _PktcSigDevCodecIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16383))
_PktcSigDevCodecIndex_Type.__name__=_C
_PktcSigDevCodecIndex_Object=MibTableColumn
pktcSigDevCodecIndex=_PktcSigDevCodecIndex_Object((1,3,6,1,4,1,4491,2,2,2,1,1,1,1,1),_PktcSigDevCodecIndex_Type())
pktcSigDevCodecIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:pktcSigDevCodecIndex.setStatus(_A)
_PktcSigDevCodecType_Type=PktcCodecType
_PktcSigDevCodecType_Object=MibTableColumn
pktcSigDevCodecType=_PktcSigDevCodecType_Object((1,3,6,1,4,1,4491,2,2,2,1,1,1,1,2),_PktcSigDevCodecType_Type())
pktcSigDevCodecType.setMaxAccess(_H)
if mibBuilder.loadTexts:pktcSigDevCodecType.setStatus(_A)
class _PktcSigDevCodecMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16383))
_PktcSigDevCodecMax_Type.__name__=_C
_PktcSigDevCodecMax_Object=MibTableColumn
pktcSigDevCodecMax=_PktcSigDevCodecMax_Object((1,3,6,1,4,1,4491,2,2,2,1,1,1,1,3),_PktcSigDevCodecMax_Type())
pktcSigDevCodecMax.setMaxAccess(_H)
if mibBuilder.loadTexts:pktcSigDevCodecMax.setStatus(_A)
_PktcSigDevEchoCancellation_Type=TruthValue
_PktcSigDevEchoCancellation_Object=MibScalar
pktcSigDevEchoCancellation=_PktcSigDevEchoCancellation_Object((1,3,6,1,4,1,4491,2,2,2,1,1,2),_PktcSigDevEchoCancellation_Type())
pktcSigDevEchoCancellation.setMaxAccess(_H)
if mibBuilder.loadTexts:pktcSigDevEchoCancellation.setStatus(_A)
_PktcSigDevSilenceSuppression_Type=TruthValue
_PktcSigDevSilenceSuppression_Object=MibScalar
pktcSigDevSilenceSuppression=_PktcSigDevSilenceSuppression_Object((1,3,6,1,4,1,4491,2,2,2,1,1,3),_PktcSigDevSilenceSuppression_Type())
pktcSigDevSilenceSuppression.setMaxAccess(_H)
if mibBuilder.loadTexts:pktcSigDevSilenceSuppression.setStatus(_A)
class _PktcSigDevConnectionMode_Type(Bits):namedValues=NamedValues(*(('voice',0),('fax',1),('modem',2)))
_PktcSigDevConnectionMode_Type.__name__='Bits'
_PktcSigDevConnectionMode_Object=MibScalar
pktcSigDevConnectionMode=_PktcSigDevConnectionMode_Object((1,3,6,1,4,1,4491,2,2,2,1,1,4),_PktcSigDevConnectionMode_Type())
pktcSigDevConnectionMode.setMaxAccess(_H)
if mibBuilder.loadTexts:pktcSigDevConnectionMode.setStatus(_A)
class _PktcSigDevR0Cadence_Type(PktcRingCadence):defaultBinValue=_I
_PktcSigDevR0Cadence_Type.__name__=_G
_PktcSigDevR0Cadence_Object=MibScalar
pktcSigDevR0Cadence=_PktcSigDevR0Cadence_Object((1,3,6,1,4,1,4491,2,2,2,1,1,5),_PktcSigDevR0Cadence_Type())
pktcSigDevR0Cadence.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcSigDevR0Cadence.setStatus(_A)
class _PktcSigDevR6Cadence_Type(PktcRingCadence):defaultBinValue=_I
_PktcSigDevR6Cadence_Type.__name__=_G
_PktcSigDevR6Cadence_Object=MibScalar
pktcSigDevR6Cadence=_PktcSigDevR6Cadence_Object((1,3,6,1,4,1,4491,2,2,2,1,1,6),_PktcSigDevR6Cadence_Type())
pktcSigDevR6Cadence.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcSigDevR6Cadence.setStatus(_A)
class _PktcSigDevR7Cadence_Type(PktcRingCadence):defaultBinValue=_I
_PktcSigDevR7Cadence_Type.__name__=_G
_PktcSigDevR7Cadence_Object=MibScalar
pktcSigDevR7Cadence=_PktcSigDevR7Cadence_Object((1,3,6,1,4,1,4491,2,2,2,1,1,7),_PktcSigDevR7Cadence_Type())
pktcSigDevR7Cadence.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcSigDevR7Cadence.setStatus(_A)
class _PktcSigDefCallSigTos_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_PktcSigDefCallSigTos_Type.__name__=_C
_PktcSigDefCallSigTos_Object=MibScalar
pktcSigDefCallSigTos=_PktcSigDefCallSigTos_Object((1,3,6,1,4,1,4491,2,2,2,1,1,8),_PktcSigDefCallSigTos_Type())
pktcSigDefCallSigTos.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcSigDefCallSigTos.setStatus(_A)
class _PktcSigDefMediaStreamTos_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_PktcSigDefMediaStreamTos_Type.__name__=_C
_PktcSigDefMediaStreamTos_Object=MibScalar
pktcSigDefMediaStreamTos=_PktcSigDefMediaStreamTos_Object((1,3,6,1,4,1,4491,2,2,2,1,1,9),_PktcSigDefMediaStreamTos_Type())
pktcSigDefMediaStreamTos.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcSigDefMediaStreamTos.setStatus(_A)
class _PktcSigTosFormatSelector_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4TOSOctet',1),('dscpCodepoint',2)))
_PktcSigTosFormatSelector_Type.__name__=_C
_PktcSigTosFormatSelector_Object=MibScalar
pktcSigTosFormatSelector=_PktcSigTosFormatSelector_Object((1,3,6,1,4,1,4491,2,2,2,1,1,10),_PktcSigTosFormatSelector_Type())
pktcSigTosFormatSelector.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcSigTosFormatSelector.setStatus(_A)
_PktcSigCapabilityTable_Object=MibTable
pktcSigCapabilityTable=_PktcSigCapabilityTable_Object((1,3,6,1,4,1,4491,2,2,2,1,1,11))
if mibBuilder.loadTexts:pktcSigCapabilityTable.setStatus(_A)
_PktcSigCapabilityEntry_Object=MibTableRow
pktcSigCapabilityEntry=_PktcSigCapabilityEntry_Object((1,3,6,1,4,1,4491,2,2,2,1,1,11,1))
pktcSigCapabilityEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:pktcSigCapabilityEntry.setStatus(_A)
class _PktcSignalingIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16383))
_PktcSignalingIndex_Type.__name__=_C
_PktcSignalingIndex_Object=MibTableColumn
pktcSignalingIndex=_PktcSignalingIndex_Object((1,3,6,1,4,1,4491,2,2,2,1,1,11,1,1),_PktcSignalingIndex_Type())
pktcSignalingIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:pktcSignalingIndex.setStatus(_A)
_PktcSignalingType_Type=PktcSigType
_PktcSignalingType_Object=MibTableColumn
pktcSignalingType=_PktcSignalingType_Object((1,3,6,1,4,1,4491,2,2,2,1,1,11,1,2),_PktcSignalingType_Type())
pktcSignalingType.setMaxAccess(_H)
if mibBuilder.loadTexts:pktcSignalingType.setStatus(_A)
_PktcSignalingVersion_Type=SnmpAdminString
_PktcSignalingVersion_Object=MibTableColumn
pktcSignalingVersion=_PktcSignalingVersion_Object((1,3,6,1,4,1,4491,2,2,2,1,1,11,1,3),_PktcSignalingVersion_Type())
pktcSignalingVersion.setMaxAccess(_H)
if mibBuilder.loadTexts:pktcSignalingVersion.setStatus(_A)
_PktcSignalingVendorExtension_Type=SnmpAdminString
_PktcSignalingVendorExtension_Object=MibTableColumn
pktcSignalingVendorExtension=_PktcSignalingVendorExtension_Object((1,3,6,1,4,1,4491,2,2,2,1,1,11,1,4),_PktcSignalingVendorExtension_Type())
pktcSignalingVendorExtension.setMaxAccess(_H)
if mibBuilder.loadTexts:pktcSignalingVendorExtension.setStatus(_A)
class _PktcSigDefNcsReceiveUdpPort_Type(Integer32):defaultValue=2427;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_PktcSigDefNcsReceiveUdpPort_Type.__name__=_C
_PktcSigDefNcsReceiveUdpPort_Object=MibScalar
pktcSigDefNcsReceiveUdpPort=_PktcSigDefNcsReceiveUdpPort_Object((1,3,6,1,4,1,4491,2,2,2,1,1,12),_PktcSigDefNcsReceiveUdpPort_Type())
pktcSigDefNcsReceiveUdpPort.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcSigDefNcsReceiveUdpPort.setStatus(_A)
class _PktcSigServiceClassNameUS_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_PktcSigServiceClassNameUS_Type.__name__=_K
_PktcSigServiceClassNameUS_Object=MibScalar
pktcSigServiceClassNameUS=_PktcSigServiceClassNameUS_Object((1,3,6,1,4,1,4491,2,2,2,1,1,13),_PktcSigServiceClassNameUS_Type())
pktcSigServiceClassNameUS.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcSigServiceClassNameUS.setStatus(_J)
class _PktcSigServiceClassNameDS_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_PktcSigServiceClassNameDS_Type.__name__=_K
_PktcSigServiceClassNameDS_Object=MibScalar
pktcSigServiceClassNameDS=_PktcSigServiceClassNameDS_Object((1,3,6,1,4,1,4491,2,2,2,1,1,14),_PktcSigServiceClassNameDS_Type())
pktcSigServiceClassNameDS.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcSigServiceClassNameDS.setStatus(_J)
class _PktcSigServiceClassNameMask_Type(Integer32):defaultValue=0
_PktcSigServiceClassNameMask_Type.__name__=_C
_PktcSigServiceClassNameMask_Object=MibScalar
pktcSigServiceClassNameMask=_PktcSigServiceClassNameMask_Object((1,3,6,1,4,1,4491,2,2,2,1,1,15),_PktcSigServiceClassNameMask_Type())
pktcSigServiceClassNameMask.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcSigServiceClassNameMask.setStatus(_J)
class _PktcSigNcsServiceFlowState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notactive',1),('active',2),('error',3)))
_PktcSigNcsServiceFlowState_Type.__name__=_C
_PktcSigNcsServiceFlowState_Object=MibScalar
pktcSigNcsServiceFlowState=_PktcSigNcsServiceFlowState_Object((1,3,6,1,4,1,4491,2,2,2,1,1,16),_PktcSigNcsServiceFlowState_Type())
pktcSigNcsServiceFlowState.setMaxAccess(_H)
if mibBuilder.loadTexts:pktcSigNcsServiceFlowState.setStatus(_J)
class _PktcSigDevR1Cadence_Type(PktcRingCadence):defaultBinValue=_I
_PktcSigDevR1Cadence_Type.__name__=_G
_PktcSigDevR1Cadence_Object=MibScalar
pktcSigDevR1Cadence=_PktcSigDevR1Cadence_Object((1,3,6,1,4,1,4491,2,2,2,1,1,17),_PktcSigDevR1Cadence_Type())
pktcSigDevR1Cadence.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcSigDevR1Cadence.setStatus(_A)
class _PktcSigDevR2Cadence_Type(PktcRingCadence):defaultBinValue='11111111000011111111'
_PktcSigDevR2Cadence_Type.__name__=_G
_PktcSigDevR2Cadence_Object=MibScalar
pktcSigDevR2Cadence=_PktcSigDevR2Cadence_Object((1,3,6,1,4,1,4491,2,2,2,1,1,18),_PktcSigDevR2Cadence_Type())
pktcSigDevR2Cadence.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcSigDevR2Cadence.setStatus(_A)
class _PktcSigDevR3Cadence_Type(PktcRingCadence):defaultBinValue='11110011110011111111'
_PktcSigDevR3Cadence_Type.__name__=_G
_PktcSigDevR3Cadence_Object=MibScalar
pktcSigDevR3Cadence=_PktcSigDevR3Cadence_Object((1,3,6,1,4,1,4491,2,2,2,1,1,19),_PktcSigDevR3Cadence_Type())
pktcSigDevR3Cadence.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcSigDevR3Cadence.setStatus(_A)
class _PktcSigDevR4Cadence_Type(PktcRingCadence):defaultBinValue='11100111111111100111'
_PktcSigDevR4Cadence_Type.__name__=_G
_PktcSigDevR4Cadence_Object=MibScalar
pktcSigDevR4Cadence=_PktcSigDevR4Cadence_Object((1,3,6,1,4,1,4491,2,2,2,1,1,20),_PktcSigDevR4Cadence_Type())
pktcSigDevR4Cadence.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcSigDevR4Cadence.setStatus(_A)
class _PktcSigDevR5Cadence_Type(PktcRingCadence):defaultBinValue=_S
_PktcSigDevR5Cadence_Type.__name__=_G
_PktcSigDevR5Cadence_Object=MibScalar
pktcSigDevR5Cadence=_PktcSigDevR5Cadence_Object((1,3,6,1,4,1,4491,2,2,2,1,1,21),_PktcSigDevR5Cadence_Type())
pktcSigDevR5Cadence.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcSigDevR5Cadence.setStatus(_A)
class _PktcSigDevRgCadence_Type(PktcRingCadence):defaultBinValue=_I
_PktcSigDevRgCadence_Type.__name__=_G
_PktcSigDevRgCadence_Object=MibScalar
pktcSigDevRgCadence=_PktcSigDevRgCadence_Object((1,3,6,1,4,1,4491,2,2,2,1,1,22),_PktcSigDevRgCadence_Type())
pktcSigDevRgCadence.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcSigDevRgCadence.setStatus(_A)
class _PktcSigDevRsCadence_Type(PktcRingCadence):defaultBinValue=_S
_PktcSigDevRsCadence_Type.__name__=_G
_PktcSigDevRsCadence_Object=MibScalar
pktcSigDevRsCadence=_PktcSigDevRsCadence_Object((1,3,6,1,4,1,4491,2,2,2,1,1,23),_PktcSigDevRsCadence_Type())
pktcSigDevRsCadence.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcSigDevRsCadence.setStatus(_A)
class _PktcSigDevRtCadence_Type(PktcRingCadence):defaultBinValue=_I
_PktcSigDevRtCadence_Type.__name__=_G
_PktcSigDevRtCadence_Object=MibScalar
pktcSigDevRtCadence=_PktcSigDevRtCadence_Object((1,3,6,1,4,1,4491,2,2,2,1,1,24),_PktcSigDevRtCadence_Type())
pktcSigDevRtCadence.setMaxAccess(_E)
if mibBuilder.loadTexts:pktcSigDevRtCadence.setStatus(_A)
_PktcNcsEndPntConfigObjects_ObjectIdentity=ObjectIdentity
pktcNcsEndPntConfigObjects=_PktcNcsEndPntConfigObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,2,2,1,2))
_PktcNcsEndPntConfigTable_Object=MibTable
pktcNcsEndPntConfigTable=_PktcNcsEndPntConfigTable_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1))
if mibBuilder.loadTexts:pktcNcsEndPntConfigTable.setStatus(_A)
_PktcNcsEndPntConfigEntry_Object=MibTableRow
pktcNcsEndPntConfigEntry=_PktcNcsEndPntConfigEntry_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1))
pktcNcsEndPntConfigEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:pktcNcsEndPntConfigEntry.setStatus(_A)
class _PktcNcsEndPntConfigCallAgentId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,255))
_PktcNcsEndPntConfigCallAgentId_Type.__name__=_K
_PktcNcsEndPntConfigCallAgentId_Object=MibTableColumn
pktcNcsEndPntConfigCallAgentId=_PktcNcsEndPntConfigCallAgentId_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,1),_PktcNcsEndPntConfigCallAgentId_Type())
pktcNcsEndPntConfigCallAgentId.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigCallAgentId.setStatus(_A)
class _PktcNcsEndPntConfigCallAgentUdpPort_Type(Integer32):defaultValue=2727;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1025,65535))
_PktcNcsEndPntConfigCallAgentUdpPort_Type.__name__=_C
_PktcNcsEndPntConfigCallAgentUdpPort_Object=MibTableColumn
pktcNcsEndPntConfigCallAgentUdpPort=_PktcNcsEndPntConfigCallAgentUdpPort_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,2),_PktcNcsEndPntConfigCallAgentUdpPort_Type())
pktcNcsEndPntConfigCallAgentUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigCallAgentUdpPort.setStatus(_A)
class _PktcNcsEndPntConfigPartialDialTO_Type(Integer32):defaultValue=16
_PktcNcsEndPntConfigPartialDialTO_Type.__name__=_C
_PktcNcsEndPntConfigPartialDialTO_Object=MibTableColumn
pktcNcsEndPntConfigPartialDialTO=_PktcNcsEndPntConfigPartialDialTO_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,3),_PktcNcsEndPntConfigPartialDialTO_Type())
pktcNcsEndPntConfigPartialDialTO.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigPartialDialTO.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigPartialDialTO.setUnits(_F)
class _PktcNcsEndPntConfigCriticalDialTO_Type(Integer32):defaultValue=4
_PktcNcsEndPntConfigCriticalDialTO_Type.__name__=_C
_PktcNcsEndPntConfigCriticalDialTO_Object=MibTableColumn
pktcNcsEndPntConfigCriticalDialTO=_PktcNcsEndPntConfigCriticalDialTO_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,4),_PktcNcsEndPntConfigCriticalDialTO_Type())
pktcNcsEndPntConfigCriticalDialTO.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigCriticalDialTO.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigCriticalDialTO.setUnits(_F)
class _PktcNcsEndPntConfigBusyToneTO_Type(Integer32):defaultValue=30
_PktcNcsEndPntConfigBusyToneTO_Type.__name__=_C
_PktcNcsEndPntConfigBusyToneTO_Object=MibTableColumn
pktcNcsEndPntConfigBusyToneTO=_PktcNcsEndPntConfigBusyToneTO_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,5),_PktcNcsEndPntConfigBusyToneTO_Type())
pktcNcsEndPntConfigBusyToneTO.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigBusyToneTO.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigBusyToneTO.setUnits(_F)
class _PktcNcsEndPntConfigDialToneTO_Type(Integer32):defaultValue=16
_PktcNcsEndPntConfigDialToneTO_Type.__name__=_C
_PktcNcsEndPntConfigDialToneTO_Object=MibTableColumn
pktcNcsEndPntConfigDialToneTO=_PktcNcsEndPntConfigDialToneTO_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,6),_PktcNcsEndPntConfigDialToneTO_Type())
pktcNcsEndPntConfigDialToneTO.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigDialToneTO.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigDialToneTO.setUnits(_F)
class _PktcNcsEndPntConfigMessageWaitingTO_Type(Integer32):defaultValue=16
_PktcNcsEndPntConfigMessageWaitingTO_Type.__name__=_C
_PktcNcsEndPntConfigMessageWaitingTO_Object=MibTableColumn
pktcNcsEndPntConfigMessageWaitingTO=_PktcNcsEndPntConfigMessageWaitingTO_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,7),_PktcNcsEndPntConfigMessageWaitingTO_Type())
pktcNcsEndPntConfigMessageWaitingTO.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigMessageWaitingTO.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigMessageWaitingTO.setUnits(_F)
class _PktcNcsEndPntConfigOffHookWarnToneTO_Type(Integer32):defaultValue=0
_PktcNcsEndPntConfigOffHookWarnToneTO_Type.__name__=_C
_PktcNcsEndPntConfigOffHookWarnToneTO_Object=MibTableColumn
pktcNcsEndPntConfigOffHookWarnToneTO=_PktcNcsEndPntConfigOffHookWarnToneTO_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,8),_PktcNcsEndPntConfigOffHookWarnToneTO_Type())
pktcNcsEndPntConfigOffHookWarnToneTO.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigOffHookWarnToneTO.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigOffHookWarnToneTO.setUnits(_F)
class _PktcNcsEndPntConfigRingingTO_Type(Integer32):defaultValue=180
_PktcNcsEndPntConfigRingingTO_Type.__name__=_C
_PktcNcsEndPntConfigRingingTO_Object=MibTableColumn
pktcNcsEndPntConfigRingingTO=_PktcNcsEndPntConfigRingingTO_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,9),_PktcNcsEndPntConfigRingingTO_Type())
pktcNcsEndPntConfigRingingTO.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigRingingTO.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigRingingTO.setUnits(_F)
class _PktcNcsEndPntConfigRingBackTO_Type(Integer32):defaultValue=180
_PktcNcsEndPntConfigRingBackTO_Type.__name__=_C
_PktcNcsEndPntConfigRingBackTO_Object=MibTableColumn
pktcNcsEndPntConfigRingBackTO=_PktcNcsEndPntConfigRingBackTO_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,10),_PktcNcsEndPntConfigRingBackTO_Type())
pktcNcsEndPntConfigRingBackTO.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigRingBackTO.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigRingBackTO.setUnits(_F)
class _PktcNcsEndPntConfigReorderToneTO_Type(Integer32):defaultValue=30
_PktcNcsEndPntConfigReorderToneTO_Type.__name__=_C
_PktcNcsEndPntConfigReorderToneTO_Object=MibTableColumn
pktcNcsEndPntConfigReorderToneTO=_PktcNcsEndPntConfigReorderToneTO_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,11),_PktcNcsEndPntConfigReorderToneTO_Type())
pktcNcsEndPntConfigReorderToneTO.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigReorderToneTO.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigReorderToneTO.setUnits(_F)
class _PktcNcsEndPntConfigStutterDialToneTO_Type(Integer32):defaultValue=16
_PktcNcsEndPntConfigStutterDialToneTO_Type.__name__=_C
_PktcNcsEndPntConfigStutterDialToneTO_Object=MibTableColumn
pktcNcsEndPntConfigStutterDialToneTO=_PktcNcsEndPntConfigStutterDialToneTO_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,12),_PktcNcsEndPntConfigStutterDialToneTO_Type())
pktcNcsEndPntConfigStutterDialToneTO.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigStutterDialToneTO.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigStutterDialToneTO.setUnits(_F)
class _PktcNcsEndPntConfigTSMax_Type(Integer32):defaultValue=20
_PktcNcsEndPntConfigTSMax_Type.__name__=_C
_PktcNcsEndPntConfigTSMax_Object=MibTableColumn
pktcNcsEndPntConfigTSMax=_PktcNcsEndPntConfigTSMax_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,13),_PktcNcsEndPntConfigTSMax_Type())
pktcNcsEndPntConfigTSMax.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigTSMax.setStatus(_A)
class _PktcNcsEndPntConfigMax1_Type(Integer32):defaultValue=5
_PktcNcsEndPntConfigMax1_Type.__name__=_C
_PktcNcsEndPntConfigMax1_Object=MibTableColumn
pktcNcsEndPntConfigMax1=_PktcNcsEndPntConfigMax1_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,14),_PktcNcsEndPntConfigMax1_Type())
pktcNcsEndPntConfigMax1.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigMax1.setStatus(_A)
class _PktcNcsEndPntConfigMax2_Type(Integer32):defaultValue=7
_PktcNcsEndPntConfigMax2_Type.__name__=_C
_PktcNcsEndPntConfigMax2_Object=MibTableColumn
pktcNcsEndPntConfigMax2=_PktcNcsEndPntConfigMax2_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,15),_PktcNcsEndPntConfigMax2_Type())
pktcNcsEndPntConfigMax2.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigMax2.setStatus(_A)
class _PktcNcsEndPntConfigMax1QEnable_Type(TruthValue):defaultValue=1
_PktcNcsEndPntConfigMax1QEnable_Type.__name__=_N
_PktcNcsEndPntConfigMax1QEnable_Object=MibTableColumn
pktcNcsEndPntConfigMax1QEnable=_PktcNcsEndPntConfigMax1QEnable_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,16),_PktcNcsEndPntConfigMax1QEnable_Type())
pktcNcsEndPntConfigMax1QEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigMax1QEnable.setStatus(_A)
class _PktcNcsEndPntConfigMax2QEnable_Type(TruthValue):defaultValue=1
_PktcNcsEndPntConfigMax2QEnable_Type.__name__=_N
_PktcNcsEndPntConfigMax2QEnable_Object=MibTableColumn
pktcNcsEndPntConfigMax2QEnable=_PktcNcsEndPntConfigMax2QEnable_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,17),_PktcNcsEndPntConfigMax2QEnable_Type())
pktcNcsEndPntConfigMax2QEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigMax2QEnable.setStatus(_A)
class _PktcNcsEndPntConfigMWD_Type(Integer32):defaultValue=600
_PktcNcsEndPntConfigMWD_Type.__name__=_C
_PktcNcsEndPntConfigMWD_Object=MibTableColumn
pktcNcsEndPntConfigMWD=_PktcNcsEndPntConfigMWD_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,18),_PktcNcsEndPntConfigMWD_Type())
pktcNcsEndPntConfigMWD.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigMWD.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigMWD.setUnits(_F)
class _PktcNcsEndPntConfigTdinit_Type(Integer32):defaultValue=15
_PktcNcsEndPntConfigTdinit_Type.__name__=_C
_PktcNcsEndPntConfigTdinit_Object=MibTableColumn
pktcNcsEndPntConfigTdinit=_PktcNcsEndPntConfigTdinit_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,19),_PktcNcsEndPntConfigTdinit_Type())
pktcNcsEndPntConfigTdinit.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigTdinit.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigTdinit.setUnits(_F)
class _PktcNcsEndPntConfigTdmin_Type(Integer32):defaultValue=15
_PktcNcsEndPntConfigTdmin_Type.__name__=_C
_PktcNcsEndPntConfigTdmin_Object=MibTableColumn
pktcNcsEndPntConfigTdmin=_PktcNcsEndPntConfigTdmin_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,20),_PktcNcsEndPntConfigTdmin_Type())
pktcNcsEndPntConfigTdmin.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigTdmin.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigTdmin.setUnits(_F)
class _PktcNcsEndPntConfigTdmax_Type(Integer32):defaultValue=600
_PktcNcsEndPntConfigTdmax_Type.__name__=_C
_PktcNcsEndPntConfigTdmax_Object=MibTableColumn
pktcNcsEndPntConfigTdmax=_PktcNcsEndPntConfigTdmax_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,21),_PktcNcsEndPntConfigTdmax_Type())
pktcNcsEndPntConfigTdmax.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigTdmax.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigTdmax.setUnits(_F)
class _PktcNcsEndPntConfigRtoMax_Type(Integer32):defaultValue=4
_PktcNcsEndPntConfigRtoMax_Type.__name__=_C
_PktcNcsEndPntConfigRtoMax_Object=MibTableColumn
pktcNcsEndPntConfigRtoMax=_PktcNcsEndPntConfigRtoMax_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,22),_PktcNcsEndPntConfigRtoMax_Type())
pktcNcsEndPntConfigRtoMax.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigRtoMax.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigRtoMax.setUnits(_F)
class _PktcNcsEndPntConfigRtoInit_Type(Integer32):defaultValue=200
_PktcNcsEndPntConfigRtoInit_Type.__name__=_C
_PktcNcsEndPntConfigRtoInit_Object=MibTableColumn
pktcNcsEndPntConfigRtoInit=_PktcNcsEndPntConfigRtoInit_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,23),_PktcNcsEndPntConfigRtoInit_Type())
pktcNcsEndPntConfigRtoInit.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigRtoInit.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigRtoInit.setUnits('milliseconds')
class _PktcNcsEndPntConfigLongDurationKeepAlive_Type(Integer32):defaultValue=60
_PktcNcsEndPntConfigLongDurationKeepAlive_Type.__name__=_C
_PktcNcsEndPntConfigLongDurationKeepAlive_Object=MibTableColumn
pktcNcsEndPntConfigLongDurationKeepAlive=_PktcNcsEndPntConfigLongDurationKeepAlive_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,24),_PktcNcsEndPntConfigLongDurationKeepAlive_Type())
pktcNcsEndPntConfigLongDurationKeepAlive.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigLongDurationKeepAlive.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigLongDurationKeepAlive.setUnits('minutes')
class _PktcNcsEndPntConfigThist_Type(Integer32):defaultValue=30
_PktcNcsEndPntConfigThist_Type.__name__=_C
_PktcNcsEndPntConfigThist_Object=MibTableColumn
pktcNcsEndPntConfigThist=_PktcNcsEndPntConfigThist_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,25),_PktcNcsEndPntConfigThist_Type())
pktcNcsEndPntConfigThist.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigThist.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigThist.setUnits(_F)
_PktcNcsEndPntConfigStatus_Type=RowStatus
_PktcNcsEndPntConfigStatus_Object=MibTableColumn
pktcNcsEndPntConfigStatus=_PktcNcsEndPntConfigStatus_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,26),_PktcNcsEndPntConfigStatus_Type())
pktcNcsEndPntConfigStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigStatus.setStatus(_A)
class _PktcNcsEndPntConfigCallWaitingMaxRep_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_PktcNcsEndPntConfigCallWaitingMaxRep_Type.__name__=_C
_PktcNcsEndPntConfigCallWaitingMaxRep_Object=MibTableColumn
pktcNcsEndPntConfigCallWaitingMaxRep=_PktcNcsEndPntConfigCallWaitingMaxRep_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,27),_PktcNcsEndPntConfigCallWaitingMaxRep_Type())
pktcNcsEndPntConfigCallWaitingMaxRep.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigCallWaitingMaxRep.setStatus(_A)
class _PktcNcsEndPntConfigCallWaitingDelay_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_PktcNcsEndPntConfigCallWaitingDelay_Type.__name__=_C
_PktcNcsEndPntConfigCallWaitingDelay_Object=MibTableColumn
pktcNcsEndPntConfigCallWaitingDelay=_PktcNcsEndPntConfigCallWaitingDelay_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,28),_PktcNcsEndPntConfigCallWaitingDelay_Type())
pktcNcsEndPntConfigCallWaitingDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcNcsEndPntConfigCallWaitingDelay.setStatus(_A)
if mibBuilder.loadTexts:pktcNcsEndPntConfigCallWaitingDelay.setUnits(_F)
_PktcNcsEndPntStatusCallIpAddress_Type=IpAddress
_PktcNcsEndPntStatusCallIpAddress_Object=MibTableColumn
pktcNcsEndPntStatusCallIpAddress=_PktcNcsEndPntStatusCallIpAddress_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,29),_PktcNcsEndPntStatusCallIpAddress_Type())
pktcNcsEndPntStatusCallIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:pktcNcsEndPntStatusCallIpAddress.setStatus(_A)
class _PktcNcsEndPntStatusError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('operational',1),('noSecurityAssociation',2),('disconnected',3)))
_PktcNcsEndPntStatusError_Type.__name__=_C
_PktcNcsEndPntStatusError_Object=MibTableColumn
pktcNcsEndPntStatusError=_PktcNcsEndPntStatusError_Object((1,3,6,1,4,1,4491,2,2,2,1,2,1,1,30),_PktcNcsEndPntStatusError_Type())
pktcNcsEndPntStatusError.setMaxAccess(_H)
if mibBuilder.loadTexts:pktcNcsEndPntStatusError.setStatus(_A)
_PktcSigEndPntConfigObjects_ObjectIdentity=ObjectIdentity
pktcSigEndPntConfigObjects=_PktcSigEndPntConfigObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,2,2,1,3))
_PktcSigEndPntConfigTable_Object=MibTable
pktcSigEndPntConfigTable=_PktcSigEndPntConfigTable_Object((1,3,6,1,4,1,4491,2,2,2,1,3,1))
if mibBuilder.loadTexts:pktcSigEndPntConfigTable.setStatus(_A)
_PktcSigEndPntConfigEntry_Object=MibTableRow
pktcSigEndPntConfigEntry=_PktcSigEndPntConfigEntry_Object((1,3,6,1,4,1,4491,2,2,2,1,3,1,1))
pktcSigEndPntConfigEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:pktcSigEndPntConfigEntry.setStatus(_A)
class _PktcSigEndPntCapabilityIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16383))
_PktcSigEndPntCapabilityIndex_Type.__name__=_C
_PktcSigEndPntCapabilityIndex_Object=MibTableColumn
pktcSigEndPntCapabilityIndex=_PktcSigEndPntCapabilityIndex_Object((1,3,6,1,4,1,4491,2,2,2,1,3,1,1,1),_PktcSigEndPntCapabilityIndex_Type())
pktcSigEndPntCapabilityIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:pktcSigEndPntCapabilityIndex.setStatus(_A)
_PktcDcsEndPntConfigObjects_ObjectIdentity=ObjectIdentity
pktcDcsEndPntConfigObjects=_PktcDcsEndPntConfigObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,2,2,1,4))
_PktcSigNotificationPrefix_ObjectIdentity=ObjectIdentity
pktcSigNotificationPrefix=_PktcSigNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,4491,2,2,2,2))
_PktcSigNotification_ObjectIdentity=ObjectIdentity
pktcSigNotification=_PktcSigNotification_ObjectIdentity((1,3,6,1,4,1,4491,2,2,2,2,0))
_PktcSigConformance_ObjectIdentity=ObjectIdentity
pktcSigConformance=_PktcSigConformance_ObjectIdentity((1,3,6,1,4,1,4491,2,2,2,3))
_PktcSigCompliances_ObjectIdentity=ObjectIdentity
pktcSigCompliances=_PktcSigCompliances_ObjectIdentity((1,3,6,1,4,1,4491,2,2,2,3,1))
_PktcSigGroups_ObjectIdentity=ObjectIdentity
pktcSigGroups=_PktcSigGroups_ObjectIdentity((1,3,6,1,4,1,4491,2,2,2,3,2))
pktcSigGroup=ObjectGroup((1,3,6,1,4,1,4491,2,2,2,3,2,1))
pktcSigGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:pktcSigGroup.setStatus(_A)
pktcNcsGroup=ObjectGroup((1,3,6,1,4,1,4491,2,2,2,3,2,2))
pktcNcsGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:pktcNcsGroup.setStatus(_A)
pktcSigObsoleteGroup=ObjectGroup((1,3,6,1,4,1,4491,2,2,2,3,2,3))
pktcSigObsoleteGroup.setObjects(*((_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO)))
if mibBuilder.loadTexts:pktcSigObsoleteGroup.setStatus(_J)
pktcSigBasicCompliance=ModuleCompliance((1,3,6,1,4,1,4491,2,2,2,3,1,1))
pktcSigBasicCompliance.setObjects(*((_B,_AP),(_B,_AQ)))
if mibBuilder.loadTexts:pktcSigBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PktcCodecType':PktcCodecType,_G:PktcRingCadence,'PktcSigType':PktcSigType,'pktcSigMib':pktcSigMib,'pktcSigMibObjects':pktcSigMibObjects,'pktcSigDevConfigObjects':pktcSigDevConfigObjects,'pktcSigDevCodecTable':pktcSigDevCodecTable,'pktcSigDevCodecEntry':pktcSigDevCodecEntry,_P:pktcSigDevCodecIndex,_T:pktcSigDevCodecType,_U:pktcSigDevCodecMax,_V:pktcSigDevEchoCancellation,_W:pktcSigDevSilenceSuppression,_X:pktcSigDevConnectionMode,_Y:pktcSigDevR0Cadence,_Z:pktcSigDevR6Cadence,_a:pktcSigDevR7Cadence,_b:pktcSigDefCallSigTos,_c:pktcSigDefMediaStreamTos,_d:pktcSigTosFormatSelector,'pktcSigCapabilityTable':pktcSigCapabilityTable,'pktcSigCapabilityEntry':pktcSigCapabilityEntry,_R:pktcSignalingIndex,_e:pktcSignalingType,_f:pktcSignalingVersion,_g:pktcSignalingVendorExtension,_i:pktcSigDefNcsReceiveUdpPort,_AL:pktcSigServiceClassNameUS,_AM:pktcSigServiceClassNameDS,_AN:pktcSigServiceClassNameMask,_AO:pktcSigNcsServiceFlowState,_j:pktcSigDevR1Cadence,_k:pktcSigDevR2Cadence,_l:pktcSigDevR3Cadence,_m:pktcSigDevR4Cadence,_n:pktcSigDevR5Cadence,_o:pktcSigDevRgCadence,_p:pktcSigDevRsCadence,_q:pktcSigDevRtCadence,'pktcNcsEndPntConfigObjects':pktcNcsEndPntConfigObjects,'pktcNcsEndPntConfigTable':pktcNcsEndPntConfigTable,'pktcNcsEndPntConfigEntry':pktcNcsEndPntConfigEntry,_r:pktcNcsEndPntConfigCallAgentId,_s:pktcNcsEndPntConfigCallAgentUdpPort,_t:pktcNcsEndPntConfigPartialDialTO,_u:pktcNcsEndPntConfigCriticalDialTO,_v:pktcNcsEndPntConfigBusyToneTO,_w:pktcNcsEndPntConfigDialToneTO,_x:pktcNcsEndPntConfigMessageWaitingTO,_y:pktcNcsEndPntConfigOffHookWarnToneTO,_z:pktcNcsEndPntConfigRingingTO,_A0:pktcNcsEndPntConfigRingBackTO,_A1:pktcNcsEndPntConfigReorderToneTO,_A2:pktcNcsEndPntConfigStutterDialToneTO,_A3:pktcNcsEndPntConfigTSMax,_A4:pktcNcsEndPntConfigMax1,_A5:pktcNcsEndPntConfigMax2,_A6:pktcNcsEndPntConfigMax1QEnable,_A7:pktcNcsEndPntConfigMax2QEnable,_A8:pktcNcsEndPntConfigMWD,_A9:pktcNcsEndPntConfigTdinit,_AA:pktcNcsEndPntConfigTdmin,_AB:pktcNcsEndPntConfigTdmax,_AC:pktcNcsEndPntConfigRtoMax,_AD:pktcNcsEndPntConfigRtoInit,_AE:pktcNcsEndPntConfigLongDurationKeepAlive,_AF:pktcNcsEndPntConfigThist,_AG:pktcNcsEndPntConfigStatus,_AH:pktcNcsEndPntConfigCallWaitingMaxRep,_AI:pktcNcsEndPntConfigCallWaitingDelay,_AJ:pktcNcsEndPntStatusCallIpAddress,_AK:pktcNcsEndPntStatusError,'pktcSigEndPntConfigObjects':pktcSigEndPntConfigObjects,'pktcSigEndPntConfigTable':pktcSigEndPntConfigTable,'pktcSigEndPntConfigEntry':pktcSigEndPntConfigEntry,_h:pktcSigEndPntCapabilityIndex,'pktcDcsEndPntConfigObjects':pktcDcsEndPntConfigObjects,'pktcSigNotificationPrefix':pktcSigNotificationPrefix,'pktcSigNotification':pktcSigNotification,'pktcSigConformance':pktcSigConformance,'pktcSigCompliances':pktcSigCompliances,'pktcSigBasicCompliance':pktcSigBasicCompliance,'pktcSigGroups':pktcSigGroups,_AP:pktcSigGroup,_AQ:pktcNcsGroup,'pktcSigObsoleteGroup':pktcSigObsoleteGroup})