_W='zhoneVaIfEMTimingEntry'
_V='zhoneVaIfEMStatusEntry'
_U='zhoneVaIfFXOTimingEntry'
_T='zhoneVaIfFXOStatusEntry'
_S='zhoneVaIfFXSTimingEntry'
_R='zhoneVaIfFXSStatusEntry'
_Q='zhoneVaIfStatusEntry'
_P='zhonePotsRingIfIndex'
_O='offHook'
_N='onHook'
_M='pps'
_L='read-create'
_K='off'
_J='ifIndex'
_I='IF-MIB'
_H='deprecated'
_G='Zhone-VOICE-ANALOG-IF-MIB'
_F='TruthValue'
_E='milliseconds'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_I,'InterfaceIndex',_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_F)
zhoneModules,zhonePhysical=mibBuilder.importSymbols('Zhone','zhoneModules','zhonePhysical')
ZhoneRowStatus,=mibBuilder.importSymbols('Zhone-TC','ZhoneRowStatus')
zhoneVoiceAnalogIf_MIB=ModuleIdentity((1,3,6,1,4,1,5504,6,13))
if mibBuilder.loadTexts:zhoneVoiceAnalogIf_MIB.setRevisions(('2009-05-05 02:36','2008-03-26 17:45','2007-11-01 02:30','2005-09-06 11:14','2005-08-08 15:00','2005-05-11 15:20','2005-05-02 17:22','2004-10-07 11:34','2001-10-10 11:19','2001-02-15 18:52','2000-09-12 14:21'))
_ZhoneVaIfObjects_ObjectIdentity=ObjectIdentity
zhoneVaIfObjects=_ZhoneVaIfObjects_ObjectIdentity((1,3,6,1,4,1,5504,5,6))
_ZhoneVaIfGeneralObjects_ObjectIdentity=ObjectIdentity
zhoneVaIfGeneralObjects=_ZhoneVaIfGeneralObjects_ObjectIdentity((1,3,6,1,4,1,5504,5,6,1))
_ZhoneVaIfCfgTable_Object=MibTable
zhoneVaIfCfgTable=_ZhoneVaIfCfgTable_Object((1,3,6,1,4,1,5504,5,6,1,1))
if mibBuilder.loadTexts:zhoneVaIfCfgTable.setStatus(_A)
_ZhoneVaIfCfgEntry_Object=MibTableRow
zhoneVaIfCfgEntry=_ZhoneVaIfCfgEntry_Object((1,3,6,1,4,1,5504,5,6,1,1,1))
zhoneVaIfCfgEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:zhoneVaIfCfgEntry.setStatus(_A)
class _ZhoneVaIfCfgImpedance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('ohms600Real',2),('ohms600Complex',3),('ohms900Complex',4),('ohmsComplex1',5),('ohmsComplex2',6)))
_ZhoneVaIfCfgImpedance_Type.__name__=_B
_ZhoneVaIfCfgImpedance_Object=MibTableColumn
zhoneVaIfCfgImpedance=_ZhoneVaIfCfgImpedance_Object((1,3,6,1,4,1,5504,5,6,1,1,1,1),_ZhoneVaIfCfgImpedance_Type())
zhoneVaIfCfgImpedance.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfCfgImpedance.setStatus(_A)
class _ZhoneVaIfCfgReceiveTLP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('fxsRtlpN9db',1),('fxsRtlpN8db',2),('fxsRtlpN7db',3),('fxsRtlpN6db',4),('fxsRtlpN5db',5),('fxsRtlpN4db',6),('fxsRtlpN3db',7),('fxsRtlpN2db',8),('fxsRtlpN1db',9),('fxsRtlp0db',10),('fxsRtlp1db',11),('fxsRtlp2db',12),('fxsRtlp3db',13),('rTlpNummeric',14)))
_ZhoneVaIfCfgReceiveTLP_Type.__name__=_B
_ZhoneVaIfCfgReceiveTLP_Object=MibTableColumn
zhoneVaIfCfgReceiveTLP=_ZhoneVaIfCfgReceiveTLP_Object((1,3,6,1,4,1,5504,5,6,1,1,1,2),_ZhoneVaIfCfgReceiveTLP_Type())
zhoneVaIfCfgReceiveTLP.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfCfgReceiveTLP.setStatus(_A)
class _ZhoneVaIfCfgTransmitTLP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('fxsTtlp9db',1),('fxsTtlp8db',2),('fxsTtlp7db',3),('fxsTtlp6db',4),('fxsTtlp5db',5),('fxsTtlp4db',6),('fxsTtlp3db',7),('fxsTtlp2db',8),('fxsTtlp1db',9),('fxsTtlp0db',10),('fxsTtlpN1db',11),('fxsTtlpN2db',12),('fxsTtlpN3db',13),('tTlpNummeric',14)))
_ZhoneVaIfCfgTransmitTLP_Type.__name__=_B
_ZhoneVaIfCfgTransmitTLP_Object=MibTableColumn
zhoneVaIfCfgTransmitTLP=_ZhoneVaIfCfgTransmitTLP_Object((1,3,6,1,4,1,5504,5,6,1,1,1,3),_ZhoneVaIfCfgTransmitTLP_Type())
zhoneVaIfCfgTransmitTLP.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfCfgTransmitTLP.setStatus(_A)
class _ZhoneVaIfCfgTrunkConditioning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('idle',2),('busy',3)))
_ZhoneVaIfCfgTrunkConditioning_Type.__name__=_B
_ZhoneVaIfCfgTrunkConditioning_Object=MibTableColumn
zhoneVaIfCfgTrunkConditioning=_ZhoneVaIfCfgTrunkConditioning_Object((1,3,6,1,4,1,5504,5,6,1,1,1,4),_ZhoneVaIfCfgTrunkConditioning_Type())
zhoneVaIfCfgTrunkConditioning.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfCfgTrunkConditioning.setStatus(_A)
class _ZhoneVaIfCfgLineType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('fxs',1),('fxo',2),('em',3),('ebs',4)))
_ZhoneVaIfCfgLineType_Type.__name__=_B
_ZhoneVaIfCfgLineType_Object=MibTableColumn
zhoneVaIfCfgLineType=_ZhoneVaIfCfgLineType_Object((1,3,6,1,4,1,5504,5,6,1,1,1,5),_ZhoneVaIfCfgLineType_Type())
zhoneVaIfCfgLineType.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneVaIfCfgLineType.setStatus(_A)
class _ZhoneVaIfCfgIntegratedDSP_Type(TruthValue):defaultValue=2
_ZhoneVaIfCfgIntegratedDSP_Type.__name__=_F
_ZhoneVaIfCfgIntegratedDSP_Object=MibTableColumn
zhoneVaIfCfgIntegratedDSP=_ZhoneVaIfCfgIntegratedDSP_Object((1,3,6,1,4,1,5504,5,6,1,1,1,6),_ZhoneVaIfCfgIntegratedDSP_Type())
zhoneVaIfCfgIntegratedDSP.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneVaIfCfgIntegratedDSP.setStatus(_A)
class _ZhoneVaIfCfgLineCapabilities_Type(Bits):namedValues=NamedValues(*(('fxs',0),('fxo',1),('em',2)))
_ZhoneVaIfCfgLineCapabilities_Type.__name__='Bits'
_ZhoneVaIfCfgLineCapabilities_Object=MibTableColumn
zhoneVaIfCfgLineCapabilities=_ZhoneVaIfCfgLineCapabilities_Object((1,3,6,1,4,1,5504,5,6,1,1,1,7),_ZhoneVaIfCfgLineCapabilities_Type())
zhoneVaIfCfgLineCapabilities.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneVaIfCfgLineCapabilities.setStatus(_A)
class _ZhoneVaIfCfgMaintenanceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('ifDigitalLoopback',2),('ifAnalogLoopback',3)))
_ZhoneVaIfCfgMaintenanceMode_Type.__name__=_B
_ZhoneVaIfCfgMaintenanceMode_Object=MibTableColumn
zhoneVaIfCfgMaintenanceMode=_ZhoneVaIfCfgMaintenanceMode_Object((1,3,6,1,4,1,5504,5,6,1,1,1,8),_ZhoneVaIfCfgMaintenanceMode_Type())
zhoneVaIfCfgMaintenanceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfCfgMaintenanceMode.setStatus(_A)
class _ZhoneVaIfCfgPCMEncoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('alaw',1),('mulaw',2)))
_ZhoneVaIfCfgPCMEncoding_Type.__name__=_B
_ZhoneVaIfCfgPCMEncoding_Object=MibTableColumn
zhoneVaIfCfgPCMEncoding=_ZhoneVaIfCfgPCMEncoding_Object((1,3,6,1,4,1,5504,5,6,1,1,1,9),_ZhoneVaIfCfgPCMEncoding_Type())
zhoneVaIfCfgPCMEncoding.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfCfgPCMEncoding.setStatus(_A)
class _ZhoneVaIfCfgReceiveTLPNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-160,85))
_ZhoneVaIfCfgReceiveTLPNum_Type.__name__=_B
_ZhoneVaIfCfgReceiveTLPNum_Object=MibTableColumn
zhoneVaIfCfgReceiveTLPNum=_ZhoneVaIfCfgReceiveTLPNum_Object((1,3,6,1,4,1,5504,5,6,1,1,1,10),_ZhoneVaIfCfgReceiveTLPNum_Type())
zhoneVaIfCfgReceiveTLPNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfCfgReceiveTLPNum.setStatus(_A)
if mibBuilder.loadTexts:zhoneVaIfCfgReceiveTLPNum.setUnits('dB/10')
class _ZhoneVaIfCfgTransmitTLPNum_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-175,70))
_ZhoneVaIfCfgTransmitTLPNum_Type.__name__=_B
_ZhoneVaIfCfgTransmitTLPNum_Object=MibTableColumn
zhoneVaIfCfgTransmitTLPNum=_ZhoneVaIfCfgTransmitTLPNum_Object((1,3,6,1,4,1,5504,5,6,1,1,1,11),_ZhoneVaIfCfgTransmitTLPNum_Type())
zhoneVaIfCfgTransmitTLPNum.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfCfgTransmitTLPNum.setStatus(_A)
if mibBuilder.loadTexts:zhoneVaIfCfgTransmitTLPNum.setUnits('dB/10')
class _ZhoneVaIfCfgLoopCurrent_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,44))
_ZhoneVaIfCfgLoopCurrent_Type.__name__=_B
_ZhoneVaIfCfgLoopCurrent_Object=MibTableColumn
zhoneVaIfCfgLoopCurrent=_ZhoneVaIfCfgLoopCurrent_Object((1,3,6,1,4,1,5504,5,6,1,1,1,12),_ZhoneVaIfCfgLoopCurrent_Type())
zhoneVaIfCfgLoopCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfCfgLoopCurrent.setStatus(_A)
if mibBuilder.loadTexts:zhoneVaIfCfgLoopCurrent.setUnits('mA')
class _ZhoneVaIfCfgRingVoltage_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('b85vrms',1),('b75vrms',2),('b92vrms',3)))
_ZhoneVaIfCfgRingVoltage_Type.__name__=_B
_ZhoneVaIfCfgRingVoltage_Object=MibTableColumn
zhoneVaIfCfgRingVoltage=_ZhoneVaIfCfgRingVoltage_Object((1,3,6,1,4,1,5504,5,6,1,1,1,13),_ZhoneVaIfCfgRingVoltage_Type())
zhoneVaIfCfgRingVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfCfgRingVoltage.setStatus(_A)
_ZhoneVaIfStatusTable_Object=MibTable
zhoneVaIfStatusTable=_ZhoneVaIfStatusTable_Object((1,3,6,1,4,1,5504,5,6,1,2))
if mibBuilder.loadTexts:zhoneVaIfStatusTable.setStatus(_A)
_ZhoneVaIfStatusEntry_Object=MibTableRow
zhoneVaIfStatusEntry=_ZhoneVaIfStatusEntry_Object((1,3,6,1,4,1,5504,5,6,1,2,1))
if mibBuilder.loadTexts:zhoneVaIfStatusEntry.setStatus(_A)
_ZhoneVaIfStatusSignalErrors_Type=Counter32
_ZhoneVaIfStatusSignalErrors_Object=MibTableColumn
zhoneVaIfStatusSignalErrors=_ZhoneVaIfStatusSignalErrors_Object((1,3,6,1,4,1,5504,5,6,1,2,1,1),_ZhoneVaIfStatusSignalErrors_Type())
zhoneVaIfStatusSignalErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneVaIfStatusSignalErrors.setStatus(_A)
class _ZhoneVaIfStatusInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notype',1),('voice',2),('g3Fax',3)))
_ZhoneVaIfStatusInfoType_Type.__name__=_B
_ZhoneVaIfStatusInfoType_Object=MibTableColumn
zhoneVaIfStatusInfoType=_ZhoneVaIfStatusInfoType_Object((1,3,6,1,4,1,5504,5,6,1,2,1,2),_ZhoneVaIfStatusInfoType_Type())
zhoneVaIfStatusInfoType.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneVaIfStatusInfoType.setStatus(_A)
_ZhoneVaIfFXSObjects_ObjectIdentity=ObjectIdentity
zhoneVaIfFXSObjects=_ZhoneVaIfFXSObjects_ObjectIdentity((1,3,6,1,4,1,5504,5,6,2))
_ZhoneVaIfFXSCfgTable_Object=MibTable
zhoneVaIfFXSCfgTable=_ZhoneVaIfFXSCfgTable_Object((1,3,6,1,4,1,5504,5,6,2,1))
if mibBuilder.loadTexts:zhoneVaIfFXSCfgTable.setStatus(_A)
_ZhoneVaIfFXSCfgEntry_Object=MibTableRow
zhoneVaIfFXSCfgEntry=_ZhoneVaIfFXSCfgEntry_Object((1,3,6,1,4,1,5504,5,6,2,1,1))
zhoneVaIfFXSCfgEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:zhoneVaIfFXSCfgEntry.setStatus(_A)
class _ZhoneVaIfFXSCfgSignalType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('fxsLoopStart',1),('fxsGroundStart',2),('fxsLoopStartFd',3),('fxsGroundStartAutomatic',4),('fxsGroundStartImmediate',5),('fxsdnLoopStart',6),('fxsdnLoopStartFd',7),('fxsdnGroundStart',8),('fxsdnGroundStartImmediate',9),('fxsdnwinkLoopStart',10),('fxsdnwinkLoopStartFd',11),('fxsdnwinkGroundStart',12),('fxsdnwinkGroundStartImmediate',13),('fxstr08SingleParty',14),('fxstr08UniversalVoiceGrade',15),('fxstr08UniversalVoiceGradeAutomatic',16)))
_ZhoneVaIfFXSCfgSignalType_Type.__name__=_B
_ZhoneVaIfFXSCfgSignalType_Object=MibTableColumn
zhoneVaIfFXSCfgSignalType=_ZhoneVaIfFXSCfgSignalType_Object((1,3,6,1,4,1,5504,5,6,2,1,1,1),_ZhoneVaIfFXSCfgSignalType_Type())
zhoneVaIfFXSCfgSignalType.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfFXSCfgSignalType.setStatus(_A)
class _ZhoneVaIfFXSRingFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ringFrequency25',1),('ringFrequency50',2),('ringFrequency20',3),('ringFrequency30',4)))
_ZhoneVaIfFXSRingFrequency_Type.__name__=_B
_ZhoneVaIfFXSRingFrequency_Object=MibTableColumn
zhoneVaIfFXSRingFrequency=_ZhoneVaIfFXSRingFrequency_Object((1,3,6,1,4,1,5504,5,6,2,1,1,2),_ZhoneVaIfFXSRingFrequency_Type())
zhoneVaIfFXSRingFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfFXSRingFrequency.setStatus(_A)
class _ZhoneVaIfFXSRingBack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_K,2)))
_ZhoneVaIfFXSRingBack_Type.__name__=_B
_ZhoneVaIfFXSRingBack_Object=MibTableColumn
zhoneVaIfFXSRingBack=_ZhoneVaIfFXSRingBack_Object((1,3,6,1,4,1,5504,5,6,2,1,1,3),_ZhoneVaIfFXSRingBack_Type())
zhoneVaIfFXSRingBack.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfFXSRingBack.setStatus(_A)
_ZhoneVaIfFXSStatusTable_Object=MibTable
zhoneVaIfFXSStatusTable=_ZhoneVaIfFXSStatusTable_Object((1,3,6,1,4,1,5504,5,6,2,2))
if mibBuilder.loadTexts:zhoneVaIfFXSStatusTable.setStatus(_A)
_ZhoneVaIfFXSStatusEntry_Object=MibTableRow
zhoneVaIfFXSStatusEntry=_ZhoneVaIfFXSStatusEntry_Object((1,3,6,1,4,1,5504,5,6,2,2,1))
if mibBuilder.loadTexts:zhoneVaIfFXSStatusEntry.setStatus(_A)
class _ZhoneVaIfFXSHookStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_ZhoneVaIfFXSHookStatus_Type.__name__=_B
_ZhoneVaIfFXSHookStatus_Object=MibTableColumn
zhoneVaIfFXSHookStatus=_ZhoneVaIfFXSHookStatus_Object((1,3,6,1,4,1,5504,5,6,2,2,1,1),_ZhoneVaIfFXSHookStatus_Type())
zhoneVaIfFXSHookStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneVaIfFXSHookStatus.setStatus(_A)
class _ZhoneVaIfFXSRingActive_Type(TruthValue):defaultValue=2
_ZhoneVaIfFXSRingActive_Type.__name__=_F
_ZhoneVaIfFXSRingActive_Object=MibTableColumn
zhoneVaIfFXSRingActive=_ZhoneVaIfFXSRingActive_Object((1,3,6,1,4,1,5504,5,6,2,2,1,2),_ZhoneVaIfFXSRingActive_Type())
zhoneVaIfFXSRingActive.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneVaIfFXSRingActive.setStatus(_A)
class _ZhoneVaIfFXSRingGround_Type(TruthValue):defaultValue=2
_ZhoneVaIfFXSRingGround_Type.__name__=_F
_ZhoneVaIfFXSRingGround_Object=MibTableColumn
zhoneVaIfFXSRingGround=_ZhoneVaIfFXSRingGround_Object((1,3,6,1,4,1,5504,5,6,2,2,1,3),_ZhoneVaIfFXSRingGround_Type())
zhoneVaIfFXSRingGround.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneVaIfFXSRingGround.setStatus(_A)
class _ZhoneVaIfFXSTipGround_Type(TruthValue):defaultValue=2
_ZhoneVaIfFXSTipGround_Type.__name__=_F
_ZhoneVaIfFXSTipGround_Object=MibTableColumn
zhoneVaIfFXSTipGround=_ZhoneVaIfFXSTipGround_Object((1,3,6,1,4,1,5504,5,6,2,2,1,4),_ZhoneVaIfFXSTipGround_Type())
zhoneVaIfFXSTipGround.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneVaIfFXSTipGround.setStatus(_A)
_ZhoneVaIfFXSTimingTable_Object=MibTable
zhoneVaIfFXSTimingTable=_ZhoneVaIfFXSTimingTable_Object((1,3,6,1,4,1,5504,5,6,2,3))
if mibBuilder.loadTexts:zhoneVaIfFXSTimingTable.setStatus(_A)
_ZhoneVaIfFXSTimingEntry_Object=MibTableRow
zhoneVaIfFXSTimingEntry=_ZhoneVaIfFXSTimingEntry_Object((1,3,6,1,4,1,5504,5,6,2,3,1))
if mibBuilder.loadTexts:zhoneVaIfFXSTimingEntry.setStatus(_A)
class _ZhoneVaIfFXSTimingDigitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_ZhoneVaIfFXSTimingDigitDuration_Type.__name__=_B
_ZhoneVaIfFXSTimingDigitDuration_Object=MibTableColumn
zhoneVaIfFXSTimingDigitDuration=_ZhoneVaIfFXSTimingDigitDuration_Object((1,3,6,1,4,1,5504,5,6,2,3,1,1),_ZhoneVaIfFXSTimingDigitDuration_Type())
zhoneVaIfFXSTimingDigitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfFXSTimingDigitDuration.setStatus(_A)
if mibBuilder.loadTexts:zhoneVaIfFXSTimingDigitDuration.setUnits(_E)
class _ZhoneVaIfFXSTimingInterDigitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_ZhoneVaIfFXSTimingInterDigitDuration_Type.__name__=_B
_ZhoneVaIfFXSTimingInterDigitDuration_Object=MibTableColumn
zhoneVaIfFXSTimingInterDigitDuration=_ZhoneVaIfFXSTimingInterDigitDuration_Object((1,3,6,1,4,1,5504,5,6,2,3,1,2),_ZhoneVaIfFXSTimingInterDigitDuration_Type())
zhoneVaIfFXSTimingInterDigitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfFXSTimingInterDigitDuration.setStatus(_A)
if mibBuilder.loadTexts:zhoneVaIfFXSTimingInterDigitDuration.setUnits(_E)
_ZhonePotsRingTable_Object=MibTable
zhonePotsRingTable=_ZhonePotsRingTable_Object((1,3,6,1,4,1,5504,5,6,2,4))
if mibBuilder.loadTexts:zhonePotsRingTable.setStatus(_H)
_ZhonePotsRingEntry_Object=MibTableRow
zhonePotsRingEntry=_ZhonePotsRingEntry_Object((1,3,6,1,4,1,5504,5,6,2,4,1))
zhonePotsRingEntry.setIndexNames((0,_G,_P))
if mibBuilder.loadTexts:zhonePotsRingEntry.setStatus(_H)
_ZhonePotsRingIfIndex_Type=InterfaceIndex
_ZhonePotsRingIfIndex_Object=MibTableColumn
zhonePotsRingIfIndex=_ZhonePotsRingIfIndex_Object((1,3,6,1,4,1,5504,5,6,2,4,1,1),_ZhonePotsRingIfIndex_Type())
zhonePotsRingIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zhonePotsRingIfIndex.setStatus(_H)
class _ZhonePotsRingRingingCadence_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('ring-cadence-r0',1),('ring-cadence-r1',2),('ring-cadence-r2',3),('ring-cadence-r3',4),('ring-cadence-r4',5),('ring-cadence-r5',6),('ring-cadence-r6',7),('ring-cadence-r7',8),('ring-cadence-common',9),('ring-cadence-splash',10)))
_ZhonePotsRingRingingCadence_Type.__name__=_B
_ZhonePotsRingRingingCadence_Object=MibTableColumn
zhonePotsRingRingingCadence=_ZhonePotsRingRingingCadence_Object((1,3,6,1,4,1,5504,5,6,2,4,1,2),_ZhonePotsRingRingingCadence_Type())
zhonePotsRingRingingCadence.setMaxAccess(_L)
if mibBuilder.loadTexts:zhonePotsRingRingingCadence.setStatus(_H)
class _ZhonePotsRingTimer_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9999))
_ZhonePotsRingTimer_Type.__name__=_B
_ZhonePotsRingTimer_Object=MibTableColumn
zhonePotsRingTimer=_ZhonePotsRingTimer_Object((1,3,6,1,4,1,5504,5,6,2,4,1,3),_ZhonePotsRingTimer_Type())
zhonePotsRingTimer.setMaxAccess(_L)
if mibBuilder.loadTexts:zhonePotsRingTimer.setStatus(_H)
_ZhonePotsRingRowStatus_Type=ZhoneRowStatus
_ZhonePotsRingRowStatus_Object=MibTableColumn
zhonePotsRingRowStatus=_ZhonePotsRingRowStatus_Object((1,3,6,1,4,1,5504,5,6,2,4,1,4),_ZhonePotsRingRowStatus_Type())
zhonePotsRingRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:zhonePotsRingRowStatus.setStatus(_H)
_ZhoneVaIfFXOObjects_ObjectIdentity=ObjectIdentity
zhoneVaIfFXOObjects=_ZhoneVaIfFXOObjects_ObjectIdentity((1,3,6,1,4,1,5504,5,6,3))
_ZhoneVaIfFXOCfgTable_Object=MibTable
zhoneVaIfFXOCfgTable=_ZhoneVaIfFXOCfgTable_Object((1,3,6,1,4,1,5504,5,6,3,1))
if mibBuilder.loadTexts:zhoneVaIfFXOCfgTable.setStatus(_A)
_ZhoneVaIfFXOCfgEntry_Object=MibTableRow
zhoneVaIfFXOCfgEntry=_ZhoneVaIfFXOCfgEntry_Object((1,3,6,1,4,1,5504,5,6,3,1,1))
zhoneVaIfFXOCfgEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:zhoneVaIfFXOCfgEntry.setStatus(_A)
class _ZhoneVaIfFXOCfgSignalType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fxoLoopStart',1),('fxoGroundStart',2),('fxodpt',3)))
_ZhoneVaIfFXOCfgSignalType_Type.__name__=_B
_ZhoneVaIfFXOCfgSignalType_Object=MibTableColumn
zhoneVaIfFXOCfgSignalType=_ZhoneVaIfFXOCfgSignalType_Object((1,3,6,1,4,1,5504,5,6,3,1,1,1),_ZhoneVaIfFXOCfgSignalType_Type())
zhoneVaIfFXOCfgSignalType.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfFXOCfgSignalType.setStatus(_A)
class _ZhoneVaIfFXOCfgNumberRings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_ZhoneVaIfFXOCfgNumberRings_Type.__name__=_B
_ZhoneVaIfFXOCfgNumberRings_Object=MibTableColumn
zhoneVaIfFXOCfgNumberRings=_ZhoneVaIfFXOCfgNumberRings_Object((1,3,6,1,4,1,5504,5,6,3,1,1,2),_ZhoneVaIfFXOCfgNumberRings_Type())
zhoneVaIfFXOCfgNumberRings.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfFXOCfgNumberRings.setStatus(_A)
class _ZhoneVaIfFXOCfgSupDisconnect_Type(TruthValue):defaultValue=2
_ZhoneVaIfFXOCfgSupDisconnect_Type.__name__=_F
_ZhoneVaIfFXOCfgSupDisconnect_Object=MibTableColumn
zhoneVaIfFXOCfgSupDisconnect=_ZhoneVaIfFXOCfgSupDisconnect_Object((1,3,6,1,4,1,5504,5,6,3,1,1,3),_ZhoneVaIfFXOCfgSupDisconnect_Type())
zhoneVaIfFXOCfgSupDisconnect.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfFXOCfgSupDisconnect.setStatus(_A)
class _ZhoneVaIfFXOCfgDialType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dtmf',1),('pulse',2)))
_ZhoneVaIfFXOCfgDialType_Type.__name__=_B
_ZhoneVaIfFXOCfgDialType_Object=MibTableColumn
zhoneVaIfFXOCfgDialType=_ZhoneVaIfFXOCfgDialType_Object((1,3,6,1,4,1,5504,5,6,3,1,1,4),_ZhoneVaIfFXOCfgDialType_Type())
zhoneVaIfFXOCfgDialType.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfFXOCfgDialType.setStatus(_A)
_ZhoneVaIfFXOStatusTable_Object=MibTable
zhoneVaIfFXOStatusTable=_ZhoneVaIfFXOStatusTable_Object((1,3,6,1,4,1,5504,5,6,3,2))
if mibBuilder.loadTexts:zhoneVaIfFXOStatusTable.setStatus(_A)
_ZhoneVaIfFXOStatusEntry_Object=MibTableRow
zhoneVaIfFXOStatusEntry=_ZhoneVaIfFXOStatusEntry_Object((1,3,6,1,4,1,5504,5,6,3,2,1))
if mibBuilder.loadTexts:zhoneVaIfFXOStatusEntry.setStatus(_A)
class _ZhoneVaIfFXOHookStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_ZhoneVaIfFXOHookStatus_Type.__name__=_B
_ZhoneVaIfFXOHookStatus_Object=MibTableColumn
zhoneVaIfFXOHookStatus=_ZhoneVaIfFXOHookStatus_Object((1,3,6,1,4,1,5504,5,6,3,2,1,1),_ZhoneVaIfFXOHookStatus_Type())
zhoneVaIfFXOHookStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneVaIfFXOHookStatus.setStatus(_A)
class _ZhoneVaIfFXORingDetect_Type(TruthValue):defaultValue=2
_ZhoneVaIfFXORingDetect_Type.__name__=_F
_ZhoneVaIfFXORingDetect_Object=MibTableColumn
zhoneVaIfFXORingDetect=_ZhoneVaIfFXORingDetect_Object((1,3,6,1,4,1,5504,5,6,3,2,1,2),_ZhoneVaIfFXORingDetect_Type())
zhoneVaIfFXORingDetect.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneVaIfFXORingDetect.setStatus(_A)
class _ZhoneVaIfFXORingGround_Type(TruthValue):defaultValue=2
_ZhoneVaIfFXORingGround_Type.__name__=_F
_ZhoneVaIfFXORingGround_Object=MibTableColumn
zhoneVaIfFXORingGround=_ZhoneVaIfFXORingGround_Object((1,3,6,1,4,1,5504,5,6,3,2,1,3),_ZhoneVaIfFXORingGround_Type())
zhoneVaIfFXORingGround.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneVaIfFXORingGround.setStatus(_A)
class _ZhoneVaIfFXOTipGround_Type(TruthValue):defaultValue=2
_ZhoneVaIfFXOTipGround_Type.__name__=_F
_ZhoneVaIfFXOTipGround_Object=MibTableColumn
zhoneVaIfFXOTipGround=_ZhoneVaIfFXOTipGround_Object((1,3,6,1,4,1,5504,5,6,3,2,1,4),_ZhoneVaIfFXOTipGround_Type())
zhoneVaIfFXOTipGround.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneVaIfFXOTipGround.setStatus(_A)
_ZhoneVaIfFXOTimingTable_Object=MibTable
zhoneVaIfFXOTimingTable=_ZhoneVaIfFXOTimingTable_Object((1,3,6,1,4,1,5504,5,6,3,3))
if mibBuilder.loadTexts:zhoneVaIfFXOTimingTable.setStatus(_A)
_ZhoneVaIfFXOTimingEntry_Object=MibTableRow
zhoneVaIfFXOTimingEntry=_ZhoneVaIfFXOTimingEntry_Object((1,3,6,1,4,1,5504,5,6,3,3,1))
if mibBuilder.loadTexts:zhoneVaIfFXOTimingEntry.setStatus(_A)
class _ZhoneVaIfFXOTimingDigitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_ZhoneVaIfFXOTimingDigitDuration_Type.__name__=_B
_ZhoneVaIfFXOTimingDigitDuration_Object=MibTableColumn
zhoneVaIfFXOTimingDigitDuration=_ZhoneVaIfFXOTimingDigitDuration_Object((1,3,6,1,4,1,5504,5,6,3,3,1,1),_ZhoneVaIfFXOTimingDigitDuration_Type())
zhoneVaIfFXOTimingDigitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfFXOTimingDigitDuration.setStatus(_A)
if mibBuilder.loadTexts:zhoneVaIfFXOTimingDigitDuration.setUnits(_E)
class _ZhoneVaIfFXOTimingInterDigitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_ZhoneVaIfFXOTimingInterDigitDuration_Type.__name__=_B
_ZhoneVaIfFXOTimingInterDigitDuration_Object=MibTableColumn
zhoneVaIfFXOTimingInterDigitDuration=_ZhoneVaIfFXOTimingInterDigitDuration_Object((1,3,6,1,4,1,5504,5,6,3,3,1,2),_ZhoneVaIfFXOTimingInterDigitDuration_Type())
zhoneVaIfFXOTimingInterDigitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfFXOTimingInterDigitDuration.setStatus(_A)
if mibBuilder.loadTexts:zhoneVaIfFXOTimingInterDigitDuration.setUnits(_E)
class _ZhoneVaIfFXOTimingPulseRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,20))
_ZhoneVaIfFXOTimingPulseRate_Type.__name__=_B
_ZhoneVaIfFXOTimingPulseRate_Object=MibTableColumn
zhoneVaIfFXOTimingPulseRate=_ZhoneVaIfFXOTimingPulseRate_Object((1,3,6,1,4,1,5504,5,6,3,3,1,3),_ZhoneVaIfFXOTimingPulseRate_Type())
zhoneVaIfFXOTimingPulseRate.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfFXOTimingPulseRate.setStatus(_A)
if mibBuilder.loadTexts:zhoneVaIfFXOTimingPulseRate.setUnits(_M)
class _ZhoneVaIfFXOTimingPulseInterDigitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_ZhoneVaIfFXOTimingPulseInterDigitDuration_Type.__name__=_B
_ZhoneVaIfFXOTimingPulseInterDigitDuration_Object=MibTableColumn
zhoneVaIfFXOTimingPulseInterDigitDuration=_ZhoneVaIfFXOTimingPulseInterDigitDuration_Object((1,3,6,1,4,1,5504,5,6,3,3,1,4),_ZhoneVaIfFXOTimingPulseInterDigitDuration_Type())
zhoneVaIfFXOTimingPulseInterDigitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfFXOTimingPulseInterDigitDuration.setStatus(_A)
if mibBuilder.loadTexts:zhoneVaIfFXOTimingPulseInterDigitDuration.setUnits(_M)
_ZhoneVaIfEMObjects_ObjectIdentity=ObjectIdentity
zhoneVaIfEMObjects=_ZhoneVaIfEMObjects_ObjectIdentity((1,3,6,1,4,1,5504,5,6,4))
_ZhoneVaIfEMCfgTable_Object=MibTable
zhoneVaIfEMCfgTable=_ZhoneVaIfEMCfgTable_Object((1,3,6,1,4,1,5504,5,6,4,1))
if mibBuilder.loadTexts:zhoneVaIfEMCfgTable.setStatus(_A)
_ZhoneVaIfEMCfgEntry_Object=MibTableRow
zhoneVaIfEMCfgEntry=_ZhoneVaIfEMCfgEntry_Object((1,3,6,1,4,1,5504,5,6,4,1,1))
zhoneVaIfEMCfgEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:zhoneVaIfEMCfgEntry.setStatus(_A)
class _ZhoneVaIfEMCfgSignalType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('winkStart',1),('immediateDial',2),('delayDial',3)))
_ZhoneVaIfEMCfgSignalType_Type.__name__=_B
_ZhoneVaIfEMCfgSignalType_Object=MibTableColumn
zhoneVaIfEMCfgSignalType=_ZhoneVaIfEMCfgSignalType_Object((1,3,6,1,4,1,5504,5,6,4,1,1,1),_ZhoneVaIfEMCfgSignalType_Type())
zhoneVaIfEMCfgSignalType.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneVaIfEMCfgSignalType.setStatus(_A)
class _ZhoneVaIfEMCfgOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('twoWires',1),('fourWires',2)))
_ZhoneVaIfEMCfgOperation_Type.__name__=_B
_ZhoneVaIfEMCfgOperation_Object=MibTableColumn
zhoneVaIfEMCfgOperation=_ZhoneVaIfEMCfgOperation_Object((1,3,6,1,4,1,5504,5,6,4,1,1,2),_ZhoneVaIfEMCfgOperation_Type())
zhoneVaIfEMCfgOperation.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneVaIfEMCfgOperation.setStatus(_A)
class _ZhoneVaIfEMCfgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('typeI',1),('typeII',2),('typeIII',3),('typeIV',4),('typeV',5),('typeIIE',6),('typeIIM',7),('typeTO',8)))
_ZhoneVaIfEMCfgType_Type.__name__=_B
_ZhoneVaIfEMCfgType_Object=MibTableColumn
zhoneVaIfEMCfgType=_ZhoneVaIfEMCfgType_Object((1,3,6,1,4,1,5504,5,6,4,1,1,3),_ZhoneVaIfEMCfgType_Type())
zhoneVaIfEMCfgType.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfEMCfgType.setStatus(_A)
class _ZhoneVaIfEMCfgDialType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dtmf',1),('pulse',2)))
_ZhoneVaIfEMCfgDialType_Type.__name__=_B
_ZhoneVaIfEMCfgDialType_Object=MibTableColumn
zhoneVaIfEMCfgDialType=_ZhoneVaIfEMCfgDialType_Object((1,3,6,1,4,1,5504,5,6,4,1,1,4),_ZhoneVaIfEMCfgDialType_Type())
zhoneVaIfEMCfgDialType.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneVaIfEMCfgDialType.setStatus(_A)
_ZhoneVaIfEMStatusTable_Object=MibTable
zhoneVaIfEMStatusTable=_ZhoneVaIfEMStatusTable_Object((1,3,6,1,4,1,5504,5,6,4,2))
if mibBuilder.loadTexts:zhoneVaIfEMStatusTable.setStatus(_A)
_ZhoneVaIfEMStatusEntry_Object=MibTableRow
zhoneVaIfEMStatusEntry=_ZhoneVaIfEMStatusEntry_Object((1,3,6,1,4,1,5504,5,6,4,2,1))
if mibBuilder.loadTexts:zhoneVaIfEMStatusEntry.setStatus(_A)
class _ZhoneVaIfEMInSeizureActive_Type(TruthValue):defaultValue=2
_ZhoneVaIfEMInSeizureActive_Type.__name__=_F
_ZhoneVaIfEMInSeizureActive_Object=MibTableColumn
zhoneVaIfEMInSeizureActive=_ZhoneVaIfEMInSeizureActive_Object((1,3,6,1,4,1,5504,5,6,4,2,1,1),_ZhoneVaIfEMInSeizureActive_Type())
zhoneVaIfEMInSeizureActive.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneVaIfEMInSeizureActive.setStatus(_A)
class _ZhoneVaIfEMOutSeizureActive_Type(TruthValue):defaultValue=2
_ZhoneVaIfEMOutSeizureActive_Type.__name__=_F
_ZhoneVaIfEMOutSeizureActive_Object=MibTableColumn
zhoneVaIfEMOutSeizureActive=_ZhoneVaIfEMOutSeizureActive_Object((1,3,6,1,4,1,5504,5,6,4,2,1,2),_ZhoneVaIfEMOutSeizureActive_Type())
zhoneVaIfEMOutSeizureActive.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneVaIfEMOutSeizureActive.setStatus(_A)
_ZhoneVaIfEMTimingTable_Object=MibTable
zhoneVaIfEMTimingTable=_ZhoneVaIfEMTimingTable_Object((1,3,6,1,4,1,5504,5,6,4,3))
if mibBuilder.loadTexts:zhoneVaIfEMTimingTable.setStatus(_A)
_ZhoneVaIfEMTimingEntry_Object=MibTableRow
zhoneVaIfEMTimingEntry=_ZhoneVaIfEMTimingEntry_Object((1,3,6,1,4,1,5504,5,6,4,3,1))
if mibBuilder.loadTexts:zhoneVaIfEMTimingEntry.setStatus(_A)
class _ZhoneVaIfEMTimingDigitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_ZhoneVaIfEMTimingDigitDuration_Type.__name__=_B
_ZhoneVaIfEMTimingDigitDuration_Object=MibTableColumn
zhoneVaIfEMTimingDigitDuration=_ZhoneVaIfEMTimingDigitDuration_Object((1,3,6,1,4,1,5504,5,6,4,3,1,1),_ZhoneVaIfEMTimingDigitDuration_Type())
zhoneVaIfEMTimingDigitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfEMTimingDigitDuration.setStatus(_A)
if mibBuilder.loadTexts:zhoneVaIfEMTimingDigitDuration.setUnits(_E)
class _ZhoneVaIfEMTimingInterDigitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_ZhoneVaIfEMTimingInterDigitDuration_Type.__name__=_B
_ZhoneVaIfEMTimingInterDigitDuration_Object=MibTableColumn
zhoneVaIfEMTimingInterDigitDuration=_ZhoneVaIfEMTimingInterDigitDuration_Object((1,3,6,1,4,1,5504,5,6,4,3,1,2),_ZhoneVaIfEMTimingInterDigitDuration_Type())
zhoneVaIfEMTimingInterDigitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfEMTimingInterDigitDuration.setStatus(_A)
if mibBuilder.loadTexts:zhoneVaIfEMTimingInterDigitDuration.setUnits(_E)
class _ZhoneVaIfEMTimingPulseRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,20))
_ZhoneVaIfEMTimingPulseRate_Type.__name__=_B
_ZhoneVaIfEMTimingPulseRate_Object=MibTableColumn
zhoneVaIfEMTimingPulseRate=_ZhoneVaIfEMTimingPulseRate_Object((1,3,6,1,4,1,5504,5,6,4,3,1,3),_ZhoneVaIfEMTimingPulseRate_Type())
zhoneVaIfEMTimingPulseRate.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfEMTimingPulseRate.setStatus(_A)
if mibBuilder.loadTexts:zhoneVaIfEMTimingPulseRate.setUnits(_M)
class _ZhoneVaIfEMTimingPulseInterDigitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_ZhoneVaIfEMTimingPulseInterDigitDuration_Type.__name__=_B
_ZhoneVaIfEMTimingPulseInterDigitDuration_Object=MibTableColumn
zhoneVaIfEMTimingPulseInterDigitDuration=_ZhoneVaIfEMTimingPulseInterDigitDuration_Object((1,3,6,1,4,1,5504,5,6,4,3,1,4),_ZhoneVaIfEMTimingPulseInterDigitDuration_Type())
zhoneVaIfEMTimingPulseInterDigitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfEMTimingPulseInterDigitDuration.setStatus(_A)
if mibBuilder.loadTexts:zhoneVaIfEMTimingPulseInterDigitDuration.setUnits(_E)
class _ZhoneVaIfEMTimingClearWaitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,2000))
_ZhoneVaIfEMTimingClearWaitDuration_Type.__name__=_B
_ZhoneVaIfEMTimingClearWaitDuration_Object=MibTableColumn
zhoneVaIfEMTimingClearWaitDuration=_ZhoneVaIfEMTimingClearWaitDuration_Object((1,3,6,1,4,1,5504,5,6,4,3,1,5),_ZhoneVaIfEMTimingClearWaitDuration_Type())
zhoneVaIfEMTimingClearWaitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfEMTimingClearWaitDuration.setStatus(_A)
if mibBuilder.loadTexts:zhoneVaIfEMTimingClearWaitDuration.setUnits(_E)
class _ZhoneVaIfEMTimingMaxWinkWaitDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_ZhoneVaIfEMTimingMaxWinkWaitDuration_Type.__name__=_B
_ZhoneVaIfEMTimingMaxWinkWaitDuration_Object=MibTableColumn
zhoneVaIfEMTimingMaxWinkWaitDuration=_ZhoneVaIfEMTimingMaxWinkWaitDuration_Object((1,3,6,1,4,1,5504,5,6,4,3,1,6),_ZhoneVaIfEMTimingMaxWinkWaitDuration_Type())
zhoneVaIfEMTimingMaxWinkWaitDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfEMTimingMaxWinkWaitDuration.setStatus(_A)
if mibBuilder.loadTexts:zhoneVaIfEMTimingMaxWinkWaitDuration.setUnits(_E)
class _ZhoneVaIfEMTimingMaxWinkDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,3000))
_ZhoneVaIfEMTimingMaxWinkDuration_Type.__name__=_B
_ZhoneVaIfEMTimingMaxWinkDuration_Object=MibTableColumn
zhoneVaIfEMTimingMaxWinkDuration=_ZhoneVaIfEMTimingMaxWinkDuration_Object((1,3,6,1,4,1,5504,5,6,4,3,1,7),_ZhoneVaIfEMTimingMaxWinkDuration_Type())
zhoneVaIfEMTimingMaxWinkDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfEMTimingMaxWinkDuration.setStatus(_A)
if mibBuilder.loadTexts:zhoneVaIfEMTimingMaxWinkDuration.setUnits(_E)
class _ZhoneVaIfEMTimingDelayStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,2000))
_ZhoneVaIfEMTimingDelayStart_Type.__name__=_B
_ZhoneVaIfEMTimingDelayStart_Object=MibTableColumn
zhoneVaIfEMTimingDelayStart=_ZhoneVaIfEMTimingDelayStart_Object((1,3,6,1,4,1,5504,5,6,4,3,1,8),_ZhoneVaIfEMTimingDelayStart_Type())
zhoneVaIfEMTimingDelayStart.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfEMTimingDelayStart.setStatus(_A)
if mibBuilder.loadTexts:zhoneVaIfEMTimingDelayStart.setUnits(_E)
class _ZhoneVaIfEMTimingMaxDelayDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_ZhoneVaIfEMTimingMaxDelayDuration_Type.__name__=_B
_ZhoneVaIfEMTimingMaxDelayDuration_Object=MibTableColumn
zhoneVaIfEMTimingMaxDelayDuration=_ZhoneVaIfEMTimingMaxDelayDuration_Object((1,3,6,1,4,1,5504,5,6,4,3,1,9),_ZhoneVaIfEMTimingMaxDelayDuration_Type())
zhoneVaIfEMTimingMaxDelayDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfEMTimingMaxDelayDuration.setStatus(_A)
if mibBuilder.loadTexts:zhoneVaIfEMTimingMaxDelayDuration.setUnits(_E)
class _ZhoneVaIfEMTimingMinDelayPulseWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(140,5000))
_ZhoneVaIfEMTimingMinDelayPulseWidth_Type.__name__=_B
_ZhoneVaIfEMTimingMinDelayPulseWidth_Object=MibTableColumn
zhoneVaIfEMTimingMinDelayPulseWidth=_ZhoneVaIfEMTimingMinDelayPulseWidth_Object((1,3,6,1,4,1,5504,5,6,4,3,1,10),_ZhoneVaIfEMTimingMinDelayPulseWidth_Type())
zhoneVaIfEMTimingMinDelayPulseWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneVaIfEMTimingMinDelayPulseWidth.setStatus(_A)
if mibBuilder.loadTexts:zhoneVaIfEMTimingMinDelayPulseWidth.setUnits(_E)
zhoneVaIfCfgEntry.registerAugmentions((_G,_Q))
zhoneVaIfStatusEntry.setIndexNames(*zhoneVaIfCfgEntry.getIndexNames())
zhoneVaIfFXSCfgEntry.registerAugmentions((_G,_R))
zhoneVaIfFXSStatusEntry.setIndexNames(*zhoneVaIfFXSCfgEntry.getIndexNames())
zhoneVaIfFXSCfgEntry.registerAugmentions((_G,_S))
zhoneVaIfFXSTimingEntry.setIndexNames(*zhoneVaIfFXSCfgEntry.getIndexNames())
zhoneVaIfFXOCfgEntry.registerAugmentions((_G,_T))
zhoneVaIfFXOStatusEntry.setIndexNames(*zhoneVaIfFXOCfgEntry.getIndexNames())
zhoneVaIfFXOCfgEntry.registerAugmentions((_G,_U))
zhoneVaIfFXOTimingEntry.setIndexNames(*zhoneVaIfFXOCfgEntry.getIndexNames())
zhoneVaIfEMCfgEntry.registerAugmentions((_G,_V))
zhoneVaIfEMStatusEntry.setIndexNames(*zhoneVaIfEMCfgEntry.getIndexNames())
zhoneVaIfEMCfgEntry.registerAugmentions((_G,_W))
zhoneVaIfEMTimingEntry.setIndexNames(*zhoneVaIfEMCfgEntry.getIndexNames())
mibBuilder.exportSymbols(_G,**{'zhoneVaIfObjects':zhoneVaIfObjects,'zhoneVaIfGeneralObjects':zhoneVaIfGeneralObjects,'zhoneVaIfCfgTable':zhoneVaIfCfgTable,'zhoneVaIfCfgEntry':zhoneVaIfCfgEntry,'zhoneVaIfCfgImpedance':zhoneVaIfCfgImpedance,'zhoneVaIfCfgReceiveTLP':zhoneVaIfCfgReceiveTLP,'zhoneVaIfCfgTransmitTLP':zhoneVaIfCfgTransmitTLP,'zhoneVaIfCfgTrunkConditioning':zhoneVaIfCfgTrunkConditioning,'zhoneVaIfCfgLineType':zhoneVaIfCfgLineType,'zhoneVaIfCfgIntegratedDSP':zhoneVaIfCfgIntegratedDSP,'zhoneVaIfCfgLineCapabilities':zhoneVaIfCfgLineCapabilities,'zhoneVaIfCfgMaintenanceMode':zhoneVaIfCfgMaintenanceMode,'zhoneVaIfCfgPCMEncoding':zhoneVaIfCfgPCMEncoding,'zhoneVaIfCfgReceiveTLPNum':zhoneVaIfCfgReceiveTLPNum,'zhoneVaIfCfgTransmitTLPNum':zhoneVaIfCfgTransmitTLPNum,'zhoneVaIfCfgLoopCurrent':zhoneVaIfCfgLoopCurrent,'zhoneVaIfCfgRingVoltage':zhoneVaIfCfgRingVoltage,'zhoneVaIfStatusTable':zhoneVaIfStatusTable,_Q:zhoneVaIfStatusEntry,'zhoneVaIfStatusSignalErrors':zhoneVaIfStatusSignalErrors,'zhoneVaIfStatusInfoType':zhoneVaIfStatusInfoType,'zhoneVaIfFXSObjects':zhoneVaIfFXSObjects,'zhoneVaIfFXSCfgTable':zhoneVaIfFXSCfgTable,'zhoneVaIfFXSCfgEntry':zhoneVaIfFXSCfgEntry,'zhoneVaIfFXSCfgSignalType':zhoneVaIfFXSCfgSignalType,'zhoneVaIfFXSRingFrequency':zhoneVaIfFXSRingFrequency,'zhoneVaIfFXSRingBack':zhoneVaIfFXSRingBack,'zhoneVaIfFXSStatusTable':zhoneVaIfFXSStatusTable,_R:zhoneVaIfFXSStatusEntry,'zhoneVaIfFXSHookStatus':zhoneVaIfFXSHookStatus,'zhoneVaIfFXSRingActive':zhoneVaIfFXSRingActive,'zhoneVaIfFXSRingGround':zhoneVaIfFXSRingGround,'zhoneVaIfFXSTipGround':zhoneVaIfFXSTipGround,'zhoneVaIfFXSTimingTable':zhoneVaIfFXSTimingTable,_S:zhoneVaIfFXSTimingEntry,'zhoneVaIfFXSTimingDigitDuration':zhoneVaIfFXSTimingDigitDuration,'zhoneVaIfFXSTimingInterDigitDuration':zhoneVaIfFXSTimingInterDigitDuration,'zhonePotsRingTable':zhonePotsRingTable,'zhonePotsRingEntry':zhonePotsRingEntry,_P:zhonePotsRingIfIndex,'zhonePotsRingRingingCadence':zhonePotsRingRingingCadence,'zhonePotsRingTimer':zhonePotsRingTimer,'zhonePotsRingRowStatus':zhonePotsRingRowStatus,'zhoneVaIfFXOObjects':zhoneVaIfFXOObjects,'zhoneVaIfFXOCfgTable':zhoneVaIfFXOCfgTable,'zhoneVaIfFXOCfgEntry':zhoneVaIfFXOCfgEntry,'zhoneVaIfFXOCfgSignalType':zhoneVaIfFXOCfgSignalType,'zhoneVaIfFXOCfgNumberRings':zhoneVaIfFXOCfgNumberRings,'zhoneVaIfFXOCfgSupDisconnect':zhoneVaIfFXOCfgSupDisconnect,'zhoneVaIfFXOCfgDialType':zhoneVaIfFXOCfgDialType,'zhoneVaIfFXOStatusTable':zhoneVaIfFXOStatusTable,_T:zhoneVaIfFXOStatusEntry,'zhoneVaIfFXOHookStatus':zhoneVaIfFXOHookStatus,'zhoneVaIfFXORingDetect':zhoneVaIfFXORingDetect,'zhoneVaIfFXORingGround':zhoneVaIfFXORingGround,'zhoneVaIfFXOTipGround':zhoneVaIfFXOTipGround,'zhoneVaIfFXOTimingTable':zhoneVaIfFXOTimingTable,_U:zhoneVaIfFXOTimingEntry,'zhoneVaIfFXOTimingDigitDuration':zhoneVaIfFXOTimingDigitDuration,'zhoneVaIfFXOTimingInterDigitDuration':zhoneVaIfFXOTimingInterDigitDuration,'zhoneVaIfFXOTimingPulseRate':zhoneVaIfFXOTimingPulseRate,'zhoneVaIfFXOTimingPulseInterDigitDuration':zhoneVaIfFXOTimingPulseInterDigitDuration,'zhoneVaIfEMObjects':zhoneVaIfEMObjects,'zhoneVaIfEMCfgTable':zhoneVaIfEMCfgTable,'zhoneVaIfEMCfgEntry':zhoneVaIfEMCfgEntry,'zhoneVaIfEMCfgSignalType':zhoneVaIfEMCfgSignalType,'zhoneVaIfEMCfgOperation':zhoneVaIfEMCfgOperation,'zhoneVaIfEMCfgType':zhoneVaIfEMCfgType,'zhoneVaIfEMCfgDialType':zhoneVaIfEMCfgDialType,'zhoneVaIfEMStatusTable':zhoneVaIfEMStatusTable,_V:zhoneVaIfEMStatusEntry,'zhoneVaIfEMInSeizureActive':zhoneVaIfEMInSeizureActive,'zhoneVaIfEMOutSeizureActive':zhoneVaIfEMOutSeizureActive,'zhoneVaIfEMTimingTable':zhoneVaIfEMTimingTable,_W:zhoneVaIfEMTimingEntry,'zhoneVaIfEMTimingDigitDuration':zhoneVaIfEMTimingDigitDuration,'zhoneVaIfEMTimingInterDigitDuration':zhoneVaIfEMTimingInterDigitDuration,'zhoneVaIfEMTimingPulseRate':zhoneVaIfEMTimingPulseRate,'zhoneVaIfEMTimingPulseInterDigitDuration':zhoneVaIfEMTimingPulseInterDigitDuration,'zhoneVaIfEMTimingClearWaitDuration':zhoneVaIfEMTimingClearWaitDuration,'zhoneVaIfEMTimingMaxWinkWaitDuration':zhoneVaIfEMTimingMaxWinkWaitDuration,'zhoneVaIfEMTimingMaxWinkDuration':zhoneVaIfEMTimingMaxWinkDuration,'zhoneVaIfEMTimingDelayStart':zhoneVaIfEMTimingDelayStart,'zhoneVaIfEMTimingMaxDelayDuration':zhoneVaIfEMTimingMaxDelayDuration,'zhoneVaIfEMTimingMinDelayPulseWidth':zhoneVaIfEMTimingMinDelayPulseWidth,'zhoneVoiceAnalogIf-MIB':zhoneVoiceAnalogIf_MIB})