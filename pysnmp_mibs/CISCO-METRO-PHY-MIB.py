_A9='cmPhyIfClientSubrateGroup'
_A8='cmPhyIfClientOvsGroup'
_A7='cmPhyIfRateGroup'
_A6='cmPhyStatisticsGroup'
_A5='cmPhyIfGroup'
_A4='cmPhyIfClientSubrateLock'
_A3='cmPhyIfClientSubrate'
_A2='cmPhyIfOverSubscription'
_A1='cmPhyIfNegotiatedRate'
_A0='cmPhyIfRate'
_z='cmPhyIfTransType'
_y='cmPhyIfAutoNegotiation'
_x='cmPhyIfTxBufferSize'
_w='cmPhyHCTxEncapFarEndPktErrors'
_v='cmPhyTxEncapFarEndPktErrOverflow'
_u='cmPhyTxEncapFarEndPktErrors'
_t='cmPhyHCRxCRC'
_s='cmPhyRxCRCOverflow'
_r='cmPhyRxCRC'
_q='cmPhySonetSectionTraceExpected'
_p='cmPhySonetSectionTraceReceived'
_o='cmPhyHCRxHEC'
_n='cmPhyRxHECOverflow'
_m='cmPhyRxHEC'
_l='cmPhyRxPower'
_k='cmPhyIfForwardLaserControl'
_j='cmPhyIfLaserSafetyControl'
_i='TriValue'
_h='tenGbps'
_g='fourGbps'
_f='twoGbps'
_e='oneGbps'
_d='notApplicable'
_c='TruthValue'
_b='cmPhyIfGroupSup1'
_a='cmPhyHCRxCVRD'
_Z='cmPhyRxCVRDOverflow'
_Y='cmPhyRxCVRD'
_X='cmPhyIfOFC'
_W='cmPhyIfLoopback'
_V='cmPhyIfMonitor'
_U='cmPhyIfClockRate'
_T='cmPhyIfProtocol'
_S='cmPhyIfMode'
_R='unknown'
_Q='Unsigned32'
_P='OctetString'
_O='cmPhyIfAutoNegGroup'
_N='ifIndex'
_M='IF-MIB'
_L='cmPhyIfTxBufferSizeGroup'
_K='Integer32'
_J='cmPhyEncapFarEndPktErrorsGroup'
_I='cmPhyCRCErrorsGroup'
_H='cmPhyCVRDErrorsGroup'
_G='cmPhyIf2Group'
_F='cmPhySonetSectionTraceGroup'
_E='deprecated'
_D='read-write'
_C='read-only'
_B='current'
_A='CISCO-METRO-PHY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_P,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ifIndex,=mibBuilder.importSymbols(_M,_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Q,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_c)
ciscoMetroPhyMIB=ModuleIdentity((1,3,6,1,4,1,9,10,69))
if mibBuilder.loadTexts:ciscoMetroPhyMIB.setRevisions(('2005-09-02 00:00','2004-11-19 00:00','2003-08-25 00:00','2003-01-08 00:00','2002-05-14 00:00','2001-08-31 00:00','2001-04-19 00:00'))
class TransmissionType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('copper',2),('optical',3)))
class ProtocolType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*(('other',1),(_R,2),('gigabitEthernet',3),('tenGigabitEthernet',4),('fibreChannel',5),('ficon',6),('escon',7),('sonet',8),('sdh',9),('sysplexIscCompatibility',10),('sysplexIscPeer',11),('sysplexTimerEtr',12),('sysplexTimerClo',13),('fastEthernet',14),('fddi',15),('e1',16),('t1',17),('e3',18),('t3',19),('dvb',20),('sdi',21),('its',22)))
class TriValue(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('true',1),('false',2),(_d,3)))
class CmRateType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_R,1),('auto',2),(_e,3),(_f,4),(_g,5),(_h,6)))
class CmNegotiatedRateType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_d,1),('negotiating',2),(_e,3),(_f,4),(_g,5),(_h,6)))
_CiscoMetroPhyMIBObjects_ObjectIdentity=ObjectIdentity
ciscoMetroPhyMIBObjects=_CiscoMetroPhyMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,69,1))
_CmPhyIf_ObjectIdentity=ObjectIdentity
cmPhyIf=_CmPhyIf_ObjectIdentity((1,3,6,1,4,1,9,10,69,1,1))
_CmPhyIfTable_Object=MibTable
cmPhyIfTable=_CmPhyIfTable_Object((1,3,6,1,4,1,9,10,69,1,1,1))
if mibBuilder.loadTexts:cmPhyIfTable.setStatus(_B)
_CmPhyIfEntry_Object=MibTableRow
cmPhyIfEntry=_CmPhyIfEntry_Object((1,3,6,1,4,1,9,10,69,1,1,1,1))
cmPhyIfEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:cmPhyIfEntry.setStatus(_B)
class _CmPhyIfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mode2R',1),('mode3R',2)))
_CmPhyIfMode_Type.__name__=_K
_CmPhyIfMode_Object=MibTableColumn
cmPhyIfMode=_CmPhyIfMode_Object((1,3,6,1,4,1,9,10,69,1,1,1,1,1),_CmPhyIfMode_Type())
cmPhyIfMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cmPhyIfMode.setStatus(_B)
_CmPhyIfProtocol_Type=ProtocolType
_CmPhyIfProtocol_Object=MibTableColumn
cmPhyIfProtocol=_CmPhyIfProtocol_Object((1,3,6,1,4,1,9,10,69,1,1,1,1,2),_CmPhyIfProtocol_Type())
cmPhyIfProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:cmPhyIfProtocol.setStatus(_B)
class _CmPhyIfClockRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10312000))
_CmPhyIfClockRate_Type.__name__=_K
_CmPhyIfClockRate_Object=MibTableColumn
cmPhyIfClockRate=_CmPhyIfClockRate_Object((1,3,6,1,4,1,9,10,69,1,1,1,1,3),_CmPhyIfClockRate_Type())
cmPhyIfClockRate.setMaxAccess(_D)
if mibBuilder.loadTexts:cmPhyIfClockRate.setStatus(_B)
if mibBuilder.loadTexts:cmPhyIfClockRate.setUnits('kHz')
_CmPhyIfMonitor_Type=TruthValue
_CmPhyIfMonitor_Object=MibTableColumn
cmPhyIfMonitor=_CmPhyIfMonitor_Object((1,3,6,1,4,1,9,10,69,1,1,1,1,4),_CmPhyIfMonitor_Type())
cmPhyIfMonitor.setMaxAccess(_D)
if mibBuilder.loadTexts:cmPhyIfMonitor.setStatus(_B)
class _CmPhyIfLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noLoop',1),('diagnosticLoop',2),('lineLoop',3),('otherLoop',4)))
_CmPhyIfLoopback_Type.__name__=_K
_CmPhyIfLoopback_Object=MibTableColumn
cmPhyIfLoopback=_CmPhyIfLoopback_Object((1,3,6,1,4,1,9,10,69,1,1,1,1,5),_CmPhyIfLoopback_Type())
cmPhyIfLoopback.setMaxAccess(_D)
if mibBuilder.loadTexts:cmPhyIfLoopback.setStatus(_B)
_CmPhyIfOFC_Type=TruthValue
_CmPhyIfOFC_Object=MibTableColumn
cmPhyIfOFC=_CmPhyIfOFC_Object((1,3,6,1,4,1,9,10,69,1,1,1,1,6),_CmPhyIfOFC_Type())
cmPhyIfOFC.setMaxAccess(_D)
if mibBuilder.loadTexts:cmPhyIfOFC.setStatus(_B)
_CmPhyIfLaserSafetyControl_Type=TruthValue
_CmPhyIfLaserSafetyControl_Object=MibTableColumn
cmPhyIfLaserSafetyControl=_CmPhyIfLaserSafetyControl_Object((1,3,6,1,4,1,9,10,69,1,1,1,1,7),_CmPhyIfLaserSafetyControl_Type())
cmPhyIfLaserSafetyControl.setMaxAccess(_D)
if mibBuilder.loadTexts:cmPhyIfLaserSafetyControl.setStatus(_E)
_CmPhyIfForwardLaserControl_Type=TruthValue
_CmPhyIfForwardLaserControl_Object=MibTableColumn
cmPhyIfForwardLaserControl=_CmPhyIfForwardLaserControl_Object((1,3,6,1,4,1,9,10,69,1,1,1,1,8),_CmPhyIfForwardLaserControl_Type())
cmPhyIfForwardLaserControl.setMaxAccess(_D)
if mibBuilder.loadTexts:cmPhyIfForwardLaserControl.setStatus(_E)
class _CmPhyIfTxBufferSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_CmPhyIfTxBufferSize_Type.__name__=_Q
_CmPhyIfTxBufferSize_Object=MibTableColumn
cmPhyIfTxBufferSize=_CmPhyIfTxBufferSize_Object((1,3,6,1,4,1,9,10,69,1,1,1,1,9),_CmPhyIfTxBufferSize_Type())
cmPhyIfTxBufferSize.setMaxAccess(_D)
if mibBuilder.loadTexts:cmPhyIfTxBufferSize.setStatus(_B)
if mibBuilder.loadTexts:cmPhyIfTxBufferSize.setUnits('bytes')
_CmPhyIfAutoNegotiation_Type=TriValue
_CmPhyIfAutoNegotiation_Object=MibTableColumn
cmPhyIfAutoNegotiation=_CmPhyIfAutoNegotiation_Object((1,3,6,1,4,1,9,10,69,1,1,1,1,10),_CmPhyIfAutoNegotiation_Type())
cmPhyIfAutoNegotiation.setMaxAccess(_D)
if mibBuilder.loadTexts:cmPhyIfAutoNegotiation.setStatus(_B)
_CmPhyIfTransType_Type=TransmissionType
_CmPhyIfTransType_Object=MibTableColumn
cmPhyIfTransType=_CmPhyIfTransType_Object((1,3,6,1,4,1,9,10,69,1,1,1,1,11),_CmPhyIfTransType_Type())
cmPhyIfTransType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmPhyIfTransType.setStatus(_B)
_CmPhyIfRate_Type=CmRateType
_CmPhyIfRate_Object=MibTableColumn
cmPhyIfRate=_CmPhyIfRate_Object((1,3,6,1,4,1,9,10,69,1,1,1,1,12),_CmPhyIfRate_Type())
cmPhyIfRate.setMaxAccess(_D)
if mibBuilder.loadTexts:cmPhyIfRate.setStatus(_B)
_CmPhyIfNegotiatedRate_Type=CmNegotiatedRateType
_CmPhyIfNegotiatedRate_Object=MibTableColumn
cmPhyIfNegotiatedRate=_CmPhyIfNegotiatedRate_Object((1,3,6,1,4,1,9,10,69,1,1,1,1,13),_CmPhyIfNegotiatedRate_Type())
cmPhyIfNegotiatedRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cmPhyIfNegotiatedRate.setStatus(_B)
class _CmPhyIfOverSubscription_Type(TriValue):defaultValue=2
_CmPhyIfOverSubscription_Type.__name__=_i
_CmPhyIfOverSubscription_Object=MibTableColumn
cmPhyIfOverSubscription=_CmPhyIfOverSubscription_Object((1,3,6,1,4,1,9,10,69,1,1,1,1,14),_CmPhyIfOverSubscription_Type())
cmPhyIfOverSubscription.setMaxAccess(_D)
if mibBuilder.loadTexts:cmPhyIfOverSubscription.setStatus(_B)
class _CmPhyIfClientSubrate_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4240))
_CmPhyIfClientSubrate_Type.__name__=_Q
_CmPhyIfClientSubrate_Object=MibTableColumn
cmPhyIfClientSubrate=_CmPhyIfClientSubrate_Object((1,3,6,1,4,1,9,10,69,1,1,1,1,15),_CmPhyIfClientSubrate_Type())
cmPhyIfClientSubrate.setMaxAccess(_D)
if mibBuilder.loadTexts:cmPhyIfClientSubrate.setStatus(_B)
if mibBuilder.loadTexts:cmPhyIfClientSubrate.setUnits('mega-bytes-per-second')
class _CmPhyIfClientSubrateLock_Type(TruthValue):defaultValue=2
_CmPhyIfClientSubrateLock_Type.__name__=_c
_CmPhyIfClientSubrateLock_Object=MibTableColumn
cmPhyIfClientSubrateLock=_CmPhyIfClientSubrateLock_Object((1,3,6,1,4,1,9,10,69,1,1,1,1,16),_CmPhyIfClientSubrateLock_Type())
cmPhyIfClientSubrateLock.setMaxAccess(_D)
if mibBuilder.loadTexts:cmPhyIfClientSubrateLock.setStatus(_B)
_CmPhyStatistics_ObjectIdentity=ObjectIdentity
cmPhyStatistics=_CmPhyStatistics_ObjectIdentity((1,3,6,1,4,1,9,10,69,1,2))
_CmPhyStatisticsTable_Object=MibTable
cmPhyStatisticsTable=_CmPhyStatisticsTable_Object((1,3,6,1,4,1,9,10,69,1,2,1))
if mibBuilder.loadTexts:cmPhyStatisticsTable.setStatus(_B)
_CmPhyStatisticsEntry_Object=MibTableRow
cmPhyStatisticsEntry=_CmPhyStatisticsEntry_Object((1,3,6,1,4,1,9,10,69,1,2,1,1))
cmPhyStatisticsEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:cmPhyStatisticsEntry.setStatus(_B)
class _CmPhyRxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-4000,0))
_CmPhyRxPower_Type.__name__=_K
_CmPhyRxPower_Object=MibTableColumn
cmPhyRxPower=_CmPhyRxPower_Object((1,3,6,1,4,1,9,10,69,1,2,1,1,1),_CmPhyRxPower_Type())
cmPhyRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:cmPhyRxPower.setStatus(_E)
if mibBuilder.loadTexts:cmPhyRxPower.setUnits('dBm')
_CmPhyRxCVRD_Type=Counter32
_CmPhyRxCVRD_Object=MibTableColumn
cmPhyRxCVRD=_CmPhyRxCVRD_Object((1,3,6,1,4,1,9,10,69,1,2,1,1,2),_CmPhyRxCVRD_Type())
cmPhyRxCVRD.setMaxAccess(_C)
if mibBuilder.loadTexts:cmPhyRxCVRD.setStatus(_B)
_CmPhyRxCVRDOverflow_Type=Counter32
_CmPhyRxCVRDOverflow_Object=MibTableColumn
cmPhyRxCVRDOverflow=_CmPhyRxCVRDOverflow_Object((1,3,6,1,4,1,9,10,69,1,2,1,1,3),_CmPhyRxCVRDOverflow_Type())
cmPhyRxCVRDOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:cmPhyRxCVRDOverflow.setStatus(_B)
_CmPhyHCRxCVRD_Type=Counter64
_CmPhyHCRxCVRD_Object=MibTableColumn
cmPhyHCRxCVRD=_CmPhyHCRxCVRD_Object((1,3,6,1,4,1,9,10,69,1,2,1,1,4),_CmPhyHCRxCVRD_Type())
cmPhyHCRxCVRD.setMaxAccess(_C)
if mibBuilder.loadTexts:cmPhyHCRxCVRD.setStatus(_B)
_CmPhyRxHEC_Type=Counter32
_CmPhyRxHEC_Object=MibTableColumn
cmPhyRxHEC=_CmPhyRxHEC_Object((1,3,6,1,4,1,9,10,69,1,2,1,1,5),_CmPhyRxHEC_Type())
cmPhyRxHEC.setMaxAccess(_C)
if mibBuilder.loadTexts:cmPhyRxHEC.setStatus(_E)
_CmPhyRxHECOverflow_Type=Counter32
_CmPhyRxHECOverflow_Object=MibTableColumn
cmPhyRxHECOverflow=_CmPhyRxHECOverflow_Object((1,3,6,1,4,1,9,10,69,1,2,1,1,6),_CmPhyRxHECOverflow_Type())
cmPhyRxHECOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:cmPhyRxHECOverflow.setStatus(_E)
_CmPhyHCRxHEC_Type=Counter64
_CmPhyHCRxHEC_Object=MibTableColumn
cmPhyHCRxHEC=_CmPhyHCRxHEC_Object((1,3,6,1,4,1,9,10,69,1,2,1,1,7),_CmPhyHCRxHEC_Type())
cmPhyHCRxHEC.setMaxAccess(_C)
if mibBuilder.loadTexts:cmPhyHCRxHEC.setStatus(_E)
_CmPhyRxCRC_Type=Counter32
_CmPhyRxCRC_Object=MibTableColumn
cmPhyRxCRC=_CmPhyRxCRC_Object((1,3,6,1,4,1,9,10,69,1,2,1,1,8),_CmPhyRxCRC_Type())
cmPhyRxCRC.setMaxAccess(_C)
if mibBuilder.loadTexts:cmPhyRxCRC.setStatus(_B)
_CmPhyRxCRCOverflow_Type=Counter32
_CmPhyRxCRCOverflow_Object=MibTableColumn
cmPhyRxCRCOverflow=_CmPhyRxCRCOverflow_Object((1,3,6,1,4,1,9,10,69,1,2,1,1,9),_CmPhyRxCRCOverflow_Type())
cmPhyRxCRCOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:cmPhyRxCRCOverflow.setStatus(_B)
_CmPhyHCRxCRC_Type=Counter64
_CmPhyHCRxCRC_Object=MibTableColumn
cmPhyHCRxCRC=_CmPhyHCRxCRC_Object((1,3,6,1,4,1,9,10,69,1,2,1,1,10),_CmPhyHCRxCRC_Type())
cmPhyHCRxCRC.setMaxAccess(_C)
if mibBuilder.loadTexts:cmPhyHCRxCRC.setStatus(_B)
_CmPhyTxEncapFarEndPktErrors_Type=Counter32
_CmPhyTxEncapFarEndPktErrors_Object=MibTableColumn
cmPhyTxEncapFarEndPktErrors=_CmPhyTxEncapFarEndPktErrors_Object((1,3,6,1,4,1,9,10,69,1,2,1,1,11),_CmPhyTxEncapFarEndPktErrors_Type())
cmPhyTxEncapFarEndPktErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cmPhyTxEncapFarEndPktErrors.setStatus(_B)
_CmPhyTxEncapFarEndPktErrOverflow_Type=Counter32
_CmPhyTxEncapFarEndPktErrOverflow_Object=MibTableColumn
cmPhyTxEncapFarEndPktErrOverflow=_CmPhyTxEncapFarEndPktErrOverflow_Object((1,3,6,1,4,1,9,10,69,1,2,1,1,12),_CmPhyTxEncapFarEndPktErrOverflow_Type())
cmPhyTxEncapFarEndPktErrOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:cmPhyTxEncapFarEndPktErrOverflow.setStatus(_B)
_CmPhyHCTxEncapFarEndPktErrors_Type=Counter64
_CmPhyHCTxEncapFarEndPktErrors_Object=MibTableColumn
cmPhyHCTxEncapFarEndPktErrors=_CmPhyHCTxEncapFarEndPktErrors_Object((1,3,6,1,4,1,9,10,69,1,2,1,1,13),_CmPhyHCTxEncapFarEndPktErrors_Type())
cmPhyHCTxEncapFarEndPktErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cmPhyHCTxEncapFarEndPktErrors.setStatus(_B)
_CmPhySonetSectionTrace_ObjectIdentity=ObjectIdentity
cmPhySonetSectionTrace=_CmPhySonetSectionTrace_ObjectIdentity((1,3,6,1,4,1,9,10,69,1,3))
_CmPhySonetSectionTraceTable_Object=MibTable
cmPhySonetSectionTraceTable=_CmPhySonetSectionTraceTable_Object((1,3,6,1,4,1,9,10,69,1,3,1))
if mibBuilder.loadTexts:cmPhySonetSectionTraceTable.setStatus(_B)
_CmPhySonetSectionTraceEntry_Object=MibTableRow
cmPhySonetSectionTraceEntry=_CmPhySonetSectionTraceEntry_Object((1,3,6,1,4,1,9,10,69,1,3,1,1))
cmPhySonetSectionTraceEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:cmPhySonetSectionTraceEntry.setStatus(_B)
class _CmPhySonetSectionTraceReceived_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(16,16),ValueSizeConstraint(64,64))
_CmPhySonetSectionTraceReceived_Type.__name__=_P
_CmPhySonetSectionTraceReceived_Object=MibTableColumn
cmPhySonetSectionTraceReceived=_CmPhySonetSectionTraceReceived_Object((1,3,6,1,4,1,9,10,69,1,3,1,1,1),_CmPhySonetSectionTraceReceived_Type())
cmPhySonetSectionTraceReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:cmPhySonetSectionTraceReceived.setStatus(_B)
class _CmPhySonetSectionTraceExpected_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(16,16),ValueSizeConstraint(64,64))
_CmPhySonetSectionTraceExpected_Type.__name__=_P
_CmPhySonetSectionTraceExpected_Object=MibTableColumn
cmPhySonetSectionTraceExpected=_CmPhySonetSectionTraceExpected_Object((1,3,6,1,4,1,9,10,69,1,3,1,1,2),_CmPhySonetSectionTraceExpected_Type())
cmPhySonetSectionTraceExpected.setMaxAccess(_D)
if mibBuilder.loadTexts:cmPhySonetSectionTraceExpected.setStatus(_B)
_CiscoMetroPhyMIBConformance_ObjectIdentity=ObjectIdentity
ciscoMetroPhyMIBConformance=_CiscoMetroPhyMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,69,3))
_CiscoMetroPhyMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoMetroPhyMIBCompliances=_CiscoMetroPhyMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,69,3,1))
_CiscoMetroPhyMIBGroups_ObjectIdentity=ObjectIdentity
ciscoMetroPhyMIBGroups=_CiscoMetroPhyMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,69,3,2))
cmPhyIfGroup=ObjectGroup((1,3,6,1,4,1,9,10,69,3,2,1))
cmPhyIfGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:cmPhyIfGroup.setStatus(_E)
cmPhyStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,10,69,3,2,2))
cmPhyStatisticsGroup.setObjects(*((_A,_l),(_A,_Y),(_A,_Z),(_A,_a),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:cmPhyStatisticsGroup.setStatus(_E)
cmPhySonetSectionTraceGroup=ObjectGroup((1,3,6,1,4,1,9,10,69,3,2,3))
cmPhySonetSectionTraceGroup.setObjects(*((_A,_p),(_A,_q)))
if mibBuilder.loadTexts:cmPhySonetSectionTraceGroup.setStatus(_B)
cmPhyIf2Group=ObjectGroup((1,3,6,1,4,1,9,10,69,3,2,4))
cmPhyIf2Group.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:cmPhyIf2Group.setStatus(_B)
cmPhyCVRDErrorsGroup=ObjectGroup((1,3,6,1,4,1,9,10,69,3,2,5))
cmPhyCVRDErrorsGroup.setObjects(*((_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:cmPhyCVRDErrorsGroup.setStatus(_B)
cmPhyCRCErrorsGroup=ObjectGroup((1,3,6,1,4,1,9,10,69,3,2,6))
cmPhyCRCErrorsGroup.setObjects(*((_A,_r),(_A,_s),(_A,_t)))
if mibBuilder.loadTexts:cmPhyCRCErrorsGroup.setStatus(_B)
cmPhyEncapFarEndPktErrorsGroup=ObjectGroup((1,3,6,1,4,1,9,10,69,3,2,7))
cmPhyEncapFarEndPktErrorsGroup.setObjects(*((_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:cmPhyEncapFarEndPktErrorsGroup.setStatus(_B)
cmPhyIfTxBufferSizeGroup=ObjectGroup((1,3,6,1,4,1,9,10,69,3,2,8))
cmPhyIfTxBufferSizeGroup.setObjects((_A,_x))
if mibBuilder.loadTexts:cmPhyIfTxBufferSizeGroup.setStatus(_B)
cmPhyIfAutoNegGroup=ObjectGroup((1,3,6,1,4,1,9,10,69,3,2,9))
cmPhyIfAutoNegGroup.setObjects((_A,_y))
if mibBuilder.loadTexts:cmPhyIfAutoNegGroup.setStatus(_B)
cmPhyIfGroupSup1=ObjectGroup((1,3,6,1,4,1,9,10,69,3,2,10))
cmPhyIfGroupSup1.setObjects((_A,_z))
if mibBuilder.loadTexts:cmPhyIfGroupSup1.setStatus(_B)
cmPhyIfRateGroup=ObjectGroup((1,3,6,1,4,1,9,10,69,3,2,11))
cmPhyIfRateGroup.setObjects(*((_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:cmPhyIfRateGroup.setStatus(_B)
cmPhyIfClientOvsGroup=ObjectGroup((1,3,6,1,4,1,9,10,69,3,2,12))
cmPhyIfClientOvsGroup.setObjects((_A,_A2))
if mibBuilder.loadTexts:cmPhyIfClientOvsGroup.setStatus(_B)
cmPhyIfClientSubrateGroup=ObjectGroup((1,3,6,1,4,1,9,10,69,3,2,13))
cmPhyIfClientSubrateGroup.setObjects(*((_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:cmPhyIfClientSubrateGroup.setStatus(_B)
cmPhyMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,69,3,1,1))
cmPhyMIBCompliance.setObjects(*((_A,_A5),(_A,_A6),(_A,_F)))
if mibBuilder.loadTexts:cmPhyMIBCompliance.setStatus(_E)
cmPhyMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,10,69,3,1,2))
cmPhyMIBCompliance2.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_F)))
if mibBuilder.loadTexts:cmPhyMIBCompliance2.setStatus(_E)
cmPhyMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,10,69,3,1,3))
cmPhyMIBCompliance3.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_F),(_A,_L)))
if mibBuilder.loadTexts:cmPhyMIBCompliance3.setStatus(_E)
cmPhyMIBComplianceRev4=ModuleCompliance((1,3,6,1,4,1,9,10,69,3,1,4))
cmPhyMIBComplianceRev4.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_F),(_A,_L),(_A,_O)))
if mibBuilder.loadTexts:cmPhyMIBComplianceRev4.setStatus(_E)
cmPhyMIBComplianceRev5=ModuleCompliance((1,3,6,1,4,1,9,10,69,3,1,5))
cmPhyMIBComplianceRev5.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_F),(_A,_L),(_A,_O),(_A,_b)))
if mibBuilder.loadTexts:cmPhyMIBComplianceRev5.setStatus(_E)
cmPhyMIBComplianceRev6=ModuleCompliance((1,3,6,1,4,1,9,10,69,3,1,6))
cmPhyMIBComplianceRev6.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_F),(_A,_L),(_A,_O),(_A,_b),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:cmPhyMIBComplianceRev6.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'TransmissionType':TransmissionType,'ProtocolType':ProtocolType,_i:TriValue,'CmRateType':CmRateType,'CmNegotiatedRateType':CmNegotiatedRateType,'ciscoMetroPhyMIB':ciscoMetroPhyMIB,'ciscoMetroPhyMIBObjects':ciscoMetroPhyMIBObjects,'cmPhyIf':cmPhyIf,'cmPhyIfTable':cmPhyIfTable,'cmPhyIfEntry':cmPhyIfEntry,_S:cmPhyIfMode,_T:cmPhyIfProtocol,_U:cmPhyIfClockRate,_V:cmPhyIfMonitor,_W:cmPhyIfLoopback,_X:cmPhyIfOFC,_j:cmPhyIfLaserSafetyControl,_k:cmPhyIfForwardLaserControl,_x:cmPhyIfTxBufferSize,_y:cmPhyIfAutoNegotiation,_z:cmPhyIfTransType,_A0:cmPhyIfRate,_A1:cmPhyIfNegotiatedRate,_A2:cmPhyIfOverSubscription,_A3:cmPhyIfClientSubrate,_A4:cmPhyIfClientSubrateLock,'cmPhyStatistics':cmPhyStatistics,'cmPhyStatisticsTable':cmPhyStatisticsTable,'cmPhyStatisticsEntry':cmPhyStatisticsEntry,_l:cmPhyRxPower,_Y:cmPhyRxCVRD,_Z:cmPhyRxCVRDOverflow,_a:cmPhyHCRxCVRD,_m:cmPhyRxHEC,_n:cmPhyRxHECOverflow,_o:cmPhyHCRxHEC,_r:cmPhyRxCRC,_s:cmPhyRxCRCOverflow,_t:cmPhyHCRxCRC,_u:cmPhyTxEncapFarEndPktErrors,_v:cmPhyTxEncapFarEndPktErrOverflow,_w:cmPhyHCTxEncapFarEndPktErrors,'cmPhySonetSectionTrace':cmPhySonetSectionTrace,'cmPhySonetSectionTraceTable':cmPhySonetSectionTraceTable,'cmPhySonetSectionTraceEntry':cmPhySonetSectionTraceEntry,_p:cmPhySonetSectionTraceReceived,_q:cmPhySonetSectionTraceExpected,'ciscoMetroPhyMIBConformance':ciscoMetroPhyMIBConformance,'ciscoMetroPhyMIBCompliances':ciscoMetroPhyMIBCompliances,'cmPhyMIBCompliance':cmPhyMIBCompliance,'cmPhyMIBCompliance2':cmPhyMIBCompliance2,'cmPhyMIBCompliance3':cmPhyMIBCompliance3,'cmPhyMIBComplianceRev4':cmPhyMIBComplianceRev4,'cmPhyMIBComplianceRev5':cmPhyMIBComplianceRev5,'cmPhyMIBComplianceRev6':cmPhyMIBComplianceRev6,'ciscoMetroPhyMIBGroups':ciscoMetroPhyMIBGroups,_A5:cmPhyIfGroup,_A6:cmPhyStatisticsGroup,_F:cmPhySonetSectionTraceGroup,_G:cmPhyIf2Group,_H:cmPhyCVRDErrorsGroup,_I:cmPhyCRCErrorsGroup,_J:cmPhyEncapFarEndPktErrorsGroup,_L:cmPhyIfTxBufferSizeGroup,_O:cmPhyIfAutoNegGroup,_b:cmPhyIfGroupSup1,_A7:cmPhyIfRateGroup,_A8:cmPhyIfClientOvsGroup,_A9:cmPhyIfClientSubrateGroup})