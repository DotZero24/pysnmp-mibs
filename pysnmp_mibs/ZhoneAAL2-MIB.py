_n='aal2ElcpIgOperStatus'
_m='aal2AlarmConfigThreshCongestion'
_l='aal2CpsPerfCongestion'
_k='aal2AlarmConfigThreshCellLoss'
_j='aal2CpsPerfSTFBadSeq'
_i='aal2AlarmConfigEntry'
_h='aal2CpsPerformanceEntry'
_g='aal2ElcpPortType'
_f='aal2ElcpPortId'
_e='accessible-for-notify'
_d='tenths of milliseconds'
_c='aal2ApIndex'
_b='milliseconds'
_a='jetstreamvoice'
_Z='AtmVorXAdminStatus'
_Y='aal2VclAudioProfileIdentifier'
_X='aLaw'
_W='muLaw'
_V='enabledDynamic'
_U='enabledEchoCancelOff'
_T='subVoiceAal2Cid'
_S='ZHONE-GEN-SUBSCRIBER'
_R='not-accessible'
_Q='aal2Cid'
_P='aal2Vci'
_O='aal2vpi'
_N='atmVclVpi'
_M='atmVclVci'
_L='octets'
_K='ifIndex'
_J='IF-MIB'
_I='ATM-MIB'
_H='disabled'
_G='enabled'
_F='read-write'
_E='ZhoneAAL2-MIB'
_D='read-create'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmVclVci,atmVclVpi=mibBuilder.importSymbols(_I,_M,_N)
AtmVcIdentifier,AtmVorXAdminStatus,AtmVorXLastChange,AtmVorXOperStatus,AtmVpIdentifier=mibBuilder.importSymbols('ATM-TC-MIB','AtmVcIdentifier',_Z,'AtmVorXLastChange','AtmVorXOperStatus','AtmVpIdentifier')
ifIndex,=mibBuilder.importSymbols(_J,_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
subVoiceAal2Cid,=mibBuilder.importSymbols(_S,_T)
zhoneAtm,=mibBuilder.importSymbols('Zhone','zhoneAtm')
ZhoneRowStatus,=mibBuilder.importSymbols('Zhone-TC','ZhoneRowStatus')
zhoneAtmAAl2=ModuleIdentity((1,3,6,1,4,1,5504,4,2,1))
if mibBuilder.loadTexts:zhoneAtmAAl2.setRevisions(('2003-11-19 18:00','2003-11-14 14:19','2003-10-03 11:45','2003-09-02 11:30','2003-01-21 16:50','2002-10-01 10:59','2002-05-29 14:15','2001-12-07 17:23','2001-11-16 10:25','2001-10-09 10:28','2001-07-11 13:58','2001-04-11 09:55','2001-01-29 17:10','2000-12-20 11:02','2000-11-06 18:54','2000-10-30 11:58','2000-09-11 14:53'))
_Aal2Traps_ObjectIdentity=ObjectIdentity
aal2Traps=_Aal2Traps_ObjectIdentity((1,3,6,1,4,1,5504,4,2,1,0))
if mibBuilder.loadTexts:aal2Traps.setStatus(_A)
_Aal2VclTable_Object=MibTable
aal2VclTable=_Aal2VclTable_Object((1,3,6,1,4,1,5504,4,2,1,1))
if mibBuilder.loadTexts:aal2VclTable.setStatus(_A)
_Aal2VclEntry_Object=MibTableRow
aal2VclEntry=_Aal2VclEntry_Object((1,3,6,1,4,1,5504,4,2,1,1,1))
aal2VclEntry.setIndexNames((0,_J,_K),(0,_I,_N),(0,_I,_M))
if mibBuilder.loadTexts:aal2VclEntry.setStatus(_A)
class _AtmVccAal2AppId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(10,11,12,13,14,15,16,17,18,255)));namedValues=NamedValues(*(('casPotsOnlyNoElcp',10),('pstnPotsOnlyNoElcp',11),('pstnPotsOnlyElcp',12),('dss1BriOnlyNoElcp',13),('dss1BriOnlyElcp',14),('casPotsDss1BriNoElcp',15),('pstnPotsDss1BriNoElcp',16),('pstnPotsDss1BriElcp',17),('otherCcs',18),('jetstream',255)))
_AtmVccAal2AppId_Type.__name__=_B
_AtmVccAal2AppId_Object=MibTableColumn
atmVccAal2AppId=_AtmVccAal2AppId_Object((1,3,6,1,4,1,5504,4,2,1,1,1,1),_AtmVccAal2AppId_Type())
atmVccAal2AppId.setMaxAccess(_F)
if mibBuilder.loadTexts:atmVccAal2AppId.setStatus(_A)
_AtmVccAal2VccI_Type=Integer32
_AtmVccAal2VccI_Object=MibTableColumn
atmVccAal2VccI=_AtmVccAal2VccI_Object((1,3,6,1,4,1,5504,4,2,1,1,1,2),_AtmVccAal2VccI_Type())
atmVccAal2VccI.setMaxAccess(_F)
if mibBuilder.loadTexts:atmVccAal2VccI.setStatus(_A)
_AtmVccAal2SigVccI_Type=Integer32
_AtmVccAal2SigVccI_Object=MibTableColumn
atmVccAal2SigVccI=_AtmVccAal2SigVccI_Object((1,3,6,1,4,1,5504,4,2,1,1,1,3),_AtmVccAal2SigVccI_Type())
atmVccAal2SigVccI.setMaxAccess(_F)
if mibBuilder.loadTexts:atmVccAal2SigVccI.setStatus(_A)
class _Aal2VclAudioProfileIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_Aal2VclAudioProfileIdentifier_Type.__name__=_B
_Aal2VclAudioProfileIdentifier_Object=MibTableColumn
aal2VclAudioProfileIdentifier=_Aal2VclAudioProfileIdentifier_Object((1,3,6,1,4,1,5504,4,2,1,1,1,4),_Aal2VclAudioProfileIdentifier_Type())
aal2VclAudioProfileIdentifier.setMaxAccess(_F)
if mibBuilder.loadTexts:aal2VclAudioProfileIdentifier.setStatus(_A)
class _Aal2VclSscsDefaultType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('i3661',1),('i3662',2),(_a,3)))
_Aal2VclSscsDefaultType_Type.__name__=_B
_Aal2VclSscsDefaultType_Object=MibTableColumn
aal2VclSscsDefaultType=_Aal2VclSscsDefaultType_Object((1,3,6,1,4,1,5504,4,2,1,1,1,5),_Aal2VclSscsDefaultType_Type())
aal2VclSscsDefaultType.setMaxAccess(_F)
if mibBuilder.loadTexts:aal2VclSscsDefaultType.setStatus(_A)
class _Aal2VclMaxCpsSduSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(45,45),ValueRangeConstraint(64,64))
_Aal2VclMaxCpsSduSize_Type.__name__=_B
_Aal2VclMaxCpsSduSize_Object=MibTableColumn
aal2VclMaxCpsSduSize=_Aal2VclMaxCpsSduSize_Object((1,3,6,1,4,1,5504,4,2,1,1,1,6),_Aal2VclMaxCpsSduSize_Type())
aal2VclMaxCpsSduSize.setMaxAccess(_F)
if mibBuilder.loadTexts:aal2VclMaxCpsSduSize.setStatus(_A)
if mibBuilder.loadTexts:aal2VclMaxCpsSduSize.setUnits(_L)
class _Aal2VclMaxNumberMultiplexChannels_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Aal2VclMaxNumberMultiplexChannels_Type.__name__=_B
_Aal2VclMaxNumberMultiplexChannels_Object=MibTableColumn
aal2VclMaxNumberMultiplexChannels=_Aal2VclMaxNumberMultiplexChannels_Object((1,3,6,1,4,1,5504,4,2,1,1,1,7),_Aal2VclMaxNumberMultiplexChannels_Type())
aal2VclMaxNumberMultiplexChannels.setMaxAccess(_F)
if mibBuilder.loadTexts:aal2VclMaxNumberMultiplexChannels.setStatus(_A)
if mibBuilder.loadTexts:aal2VclMaxNumberMultiplexChannels.setUnits('channels')
class _Aal2VclMinCidForAal2UserChannels_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Aal2VclMinCidForAal2UserChannels_Type.__name__=_B
_Aal2VclMinCidForAal2UserChannels_Object=MibTableColumn
aal2VclMinCidForAal2UserChannels=_Aal2VclMinCidForAal2UserChannels_Object((1,3,6,1,4,1,5504,4,2,1,1,1,8),_Aal2VclMinCidForAal2UserChannels_Type())
aal2VclMinCidForAal2UserChannels.setMaxAccess(_F)
if mibBuilder.loadTexts:aal2VclMinCidForAal2UserChannels.setStatus(_A)
class _Aal2VclMaxCidForAal2UserChannels_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Aal2VclMaxCidForAal2UserChannels_Type.__name__=_B
_Aal2VclMaxCidForAal2UserChannels_Object=MibTableColumn
aal2VclMaxCidForAal2UserChannels=_Aal2VclMaxCidForAal2UserChannels_Object((1,3,6,1,4,1,5504,4,2,1,1,1,9),_Aal2VclMaxCidForAal2UserChannels_Type())
aal2VclMaxCidForAal2UserChannels.setMaxAccess(_F)
if mibBuilder.loadTexts:aal2VclMaxCidForAal2UserChannels.setStatus(_A)
class _Aal2VclNextCid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,255))
_Aal2VclNextCid_Type.__name__=_B
_Aal2VclNextCid_Object=MibTableColumn
aal2VclNextCid=_Aal2VclNextCid_Object((1,3,6,1,4,1,5504,4,2,1,1,1,10),_Aal2VclNextCid_Type())
aal2VclNextCid.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2VclNextCid.setStatus(_A)
_Aal2VclTimerCU_Type=Integer32
_Aal2VclTimerCU_Object=MibTableColumn
aal2VclTimerCU=_Aal2VclTimerCU_Object((1,3,6,1,4,1,5504,4,2,1,1,1,11),_Aal2VclTimerCU_Type())
aal2VclTimerCU.setMaxAccess(_F)
if mibBuilder.loadTexts:aal2VclTimerCU.setStatus(_A)
class _Aal2VclAudioService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_U,3),(_V,4)))
_Aal2VclAudioService_Type.__name__=_B
_Aal2VclAudioService_Object=MibTableColumn
aal2VclAudioService=_Aal2VclAudioService_Object((1,3,6,1,4,1,5504,4,2,1,1,1,12),_Aal2VclAudioService_Type())
aal2VclAudioService.setMaxAccess(_F)
if mibBuilder.loadTexts:aal2VclAudioService.setStatus(_A)
class _Aal2VclCircuitModeData_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Aal2VclCircuitModeData_Type.__name__=_B
_Aal2VclCircuitModeData_Object=MibTableColumn
aal2VclCircuitModeData=_Aal2VclCircuitModeData_Object((1,3,6,1,4,1,5504,4,2,1,1,1,13),_Aal2VclCircuitModeData_Type())
aal2VclCircuitModeData.setMaxAccess(_F)
if mibBuilder.loadTexts:aal2VclCircuitModeData.setStatus(_A)
class _Aal2VclFrameModeData_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Aal2VclFrameModeData_Type.__name__=_B
_Aal2VclFrameModeData_Object=MibTableColumn
aal2VclFrameModeData=_Aal2VclFrameModeData_Object((1,3,6,1,4,1,5504,4,2,1,1,1,14),_Aal2VclFrameModeData_Type())
aal2VclFrameModeData.setMaxAccess(_F)
if mibBuilder.loadTexts:aal2VclFrameModeData.setStatus(_A)
class _Aal2VclFaxDemoRemo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Aal2VclFaxDemoRemo_Type.__name__=_B
_Aal2VclFaxDemoRemo_Object=MibTableColumn
aal2VclFaxDemoRemo=_Aal2VclFaxDemoRemo_Object((1,3,6,1,4,1,5504,4,2,1,1,1,15),_Aal2VclFaxDemoRemo_Type())
aal2VclFaxDemoRemo.setMaxAccess(_F)
if mibBuilder.loadTexts:aal2VclFaxDemoRemo.setStatus(_A)
class _Aal2VclCAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Aal2VclCAS_Type.__name__=_B
_Aal2VclCAS_Object=MibTableColumn
aal2VclCAS=_Aal2VclCAS_Object((1,3,6,1,4,1,5504,4,2,1,1,1,16),_Aal2VclCAS_Type())
aal2VclCAS.setMaxAccess(_F)
if mibBuilder.loadTexts:aal2VclCAS.setStatus(_A)
class _Aal2VclTrunkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('loopstart',2),('groundstart',3),('loopreversebattery',4)))
_Aal2VclTrunkType_Type.__name__=_B
_Aal2VclTrunkType_Object=MibTableColumn
aal2VclTrunkType=_Aal2VclTrunkType_Object((1,3,6,1,4,1,5504,4,2,1,1,1,17),_Aal2VclTrunkType_Type())
aal2VclTrunkType.setMaxAccess(_F)
if mibBuilder.loadTexts:aal2VclTrunkType.setStatus(_A)
class _Aal2VclDTMFDialedDigits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Aal2VclDTMFDialedDigits_Type.__name__=_B
_Aal2VclDTMFDialedDigits_Object=MibTableColumn
aal2VclDTMFDialedDigits=_Aal2VclDTMFDialedDigits_Object((1,3,6,1,4,1,5504,4,2,1,1,1,18),_Aal2VclDTMFDialedDigits_Type())
aal2VclDTMFDialedDigits.setMaxAccess(_F)
if mibBuilder.loadTexts:aal2VclDTMFDialedDigits.setStatus(_A)
class _Aal2VclMfR1DialedDigits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Aal2VclMfR1DialedDigits_Type.__name__=_B
_Aal2VclMfR1DialedDigits_Object=MibTableColumn
aal2VclMfR1DialedDigits=_Aal2VclMfR1DialedDigits_Object((1,3,6,1,4,1,5504,4,2,1,1,1,19),_Aal2VclMfR1DialedDigits_Type())
aal2VclMfR1DialedDigits.setMaxAccess(_F)
if mibBuilder.loadTexts:aal2VclMfR1DialedDigits.setStatus(_A)
class _Aal2VclMfR2DialedDigits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Aal2VclMfR2DialedDigits_Type.__name__=_B
_Aal2VclMfR2DialedDigits_Object=MibTableColumn
aal2VclMfR2DialedDigits=_Aal2VclMfR2DialedDigits_Object((1,3,6,1,4,1,5504,4,2,1,1,1,20),_Aal2VclMfR2DialedDigits_Type())
aal2VclMfR2DialedDigits.setMaxAccess(_F)
if mibBuilder.loadTexts:aal2VclMfR2DialedDigits.setStatus(_A)
class _Aal2VclPCMEncoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_Aal2VclPCMEncoding_Type.__name__=_B
_Aal2VclPCMEncoding_Object=MibTableColumn
aal2VclPCMEncoding=_Aal2VclPCMEncoding_Object((1,3,6,1,4,1,5504,4,2,1,1,1,21),_Aal2VclPCMEncoding_Type())
aal2VclPCMEncoding.setMaxAccess(_F)
if mibBuilder.loadTexts:aal2VclPCMEncoding.setStatus(_A)
class _Aal2VclMaxLengthFrame_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Aal2VclMaxLengthFrame_Type.__name__=_B
_Aal2VclMaxLengthFrame_Object=MibTableColumn
aal2VclMaxLengthFrame=_Aal2VclMaxLengthFrame_Object((1,3,6,1,4,1,5504,4,2,1,1,1,22),_Aal2VclMaxLengthFrame_Type())
aal2VclMaxLengthFrame.setMaxAccess(_F)
if mibBuilder.loadTexts:aal2VclMaxLengthFrame.setStatus(_A)
if mibBuilder.loadTexts:aal2VclMaxLengthFrame.setUnits(_L)
class _Aal2VclMaxSDULength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65568))
_Aal2VclMaxSDULength_Type.__name__=_B
_Aal2VclMaxSDULength_Object=MibTableColumn
aal2VclMaxSDULength=_Aal2VclMaxSDULength_Object((1,3,6,1,4,1,5504,4,2,1,1,1,23),_Aal2VclMaxSDULength_Type())
aal2VclMaxSDULength.setMaxAccess(_F)
if mibBuilder.loadTexts:aal2VclMaxSDULength.setStatus(_A)
if mibBuilder.loadTexts:aal2VclMaxSDULength.setUnits(_L)
_Aal2VclRasTimer_Type=Integer32
_Aal2VclRasTimer_Object=MibTableColumn
aal2VclRasTimer=_Aal2VclRasTimer_Object((1,3,6,1,4,1,5504,4,2,1,1,1,24),_Aal2VclRasTimer_Type())
aal2VclRasTimer.setMaxAccess(_F)
if mibBuilder.loadTexts:aal2VclRasTimer.setStatus(_A)
if mibBuilder.loadTexts:aal2VclRasTimer.setUnits(_b)
_Aal2VclCellsReceived_Type=Gauge32
_Aal2VclCellsReceived_Object=MibTableColumn
aal2VclCellsReceived=_Aal2VclCellsReceived_Object((1,3,6,1,4,1,5504,4,2,1,1,1,25),_Aal2VclCellsReceived_Type())
aal2VclCellsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2VclCellsReceived.setStatus(_A)
if mibBuilder.loadTexts:aal2VclCellsReceived.setUnits('cells')
_Aal2VclCellsSent_Type=Gauge32
_Aal2VclCellsSent_Object=MibTableColumn
aal2VclCellsSent=_Aal2VclCellsSent_Object((1,3,6,1,4,1,5504,4,2,1,1,1,26),_Aal2VclCellsSent_Type())
aal2VclCellsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2VclCellsSent.setStatus(_A)
if mibBuilder.loadTexts:aal2VclCellsSent.setUnits('cells')
_Aal2VclStatsTimeElapsed_Type=Integer32
_Aal2VclStatsTimeElapsed_Object=MibTableColumn
aal2VclStatsTimeElapsed=_Aal2VclStatsTimeElapsed_Object((1,3,6,1,4,1,5504,4,2,1,1,1,27),_Aal2VclStatsTimeElapsed_Type())
aal2VclStatsTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2VclStatsTimeElapsed.setStatus(_A)
if mibBuilder.loadTexts:aal2VclStatsTimeElapsed.setUnits('seconds')
_Aal2CidTable_Object=MibTable
aal2CidTable=_Aal2CidTable_Object((1,3,6,1,4,1,5504,4,2,1,2))
if mibBuilder.loadTexts:aal2CidTable.setStatus(_A)
_Aal2CidEntry_Object=MibTableRow
aal2CidEntry=_Aal2CidEntry_Object((1,3,6,1,4,1,5504,4,2,1,2,1))
aal2CidEntry.setIndexNames((0,_J,_K),(0,_I,_N),(0,_I,_M),(0,_E,_Q))
if mibBuilder.loadTexts:aal2CidEntry.setStatus(_A)
class _Aal2Cid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Aal2Cid_Type.__name__=_B
_Aal2Cid_Object=MibTableColumn
aal2Cid=_Aal2Cid_Object((1,3,6,1,4,1,5504,4,2,1,2,1,1),_Aal2Cid_Type())
aal2Cid.setMaxAccess(_R)
if mibBuilder.loadTexts:aal2Cid.setStatus(_A)
class _Aal2CidAdminStatus_Type(AtmVorXAdminStatus):defaultValue=2
_Aal2CidAdminStatus_Type.__name__=_Z
_Aal2CidAdminStatus_Object=MibTableColumn
aal2CidAdminStatus=_Aal2CidAdminStatus_Object((1,3,6,1,4,1,5504,4,2,1,2,1,2),_Aal2CidAdminStatus_Type())
aal2CidAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2CidAdminStatus.setStatus(_A)
_Aal2CidOperStatus_Type=AtmVorXOperStatus
_Aal2CidOperStatus_Object=MibTableColumn
aal2CidOperStatus=_Aal2CidOperStatus_Object((1,3,6,1,4,1,5504,4,2,1,2,1,3),_Aal2CidOperStatus_Type())
aal2CidOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2CidOperStatus.setStatus(_A)
_Aal2CidLastChange_Type=AtmVorXLastChange
_Aal2CidLastChange_Object=MibTableColumn
aal2CidLastChange=_Aal2CidLastChange_Object((1,3,6,1,4,1,5504,4,2,1,2,1,4),_Aal2CidLastChange_Type())
aal2CidLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2CidLastChange.setStatus(_A)
class _Aal2CidSscsType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('i3661',1),('i3662',2),(_a,3)))
_Aal2CidSscsType_Type.__name__=_B
_Aal2CidSscsType_Object=MibTableColumn
aal2CidSscsType=_Aal2CidSscsType_Object((1,3,6,1,4,1,5504,4,2,1,2,1,5),_Aal2CidSscsType_Type())
aal2CidSscsType.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2CidSscsType.setStatus(_A)
class _Aal2CidAudioService_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_U,3),(_V,4)))
_Aal2CidAudioService_Type.__name__=_B
_Aal2CidAudioService_Object=MibTableColumn
aal2CidAudioService=_Aal2CidAudioService_Object((1,3,6,1,4,1,5504,4,2,1,2,1,6),_Aal2CidAudioService_Type())
aal2CidAudioService.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2CidAudioService.setStatus(_A)
class _Aal2CidCircuitModeData_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Aal2CidCircuitModeData_Type.__name__=_B
_Aal2CidCircuitModeData_Object=MibTableColumn
aal2CidCircuitModeData=_Aal2CidCircuitModeData_Object((1,3,6,1,4,1,5504,4,2,1,2,1,7),_Aal2CidCircuitModeData_Type())
aal2CidCircuitModeData.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2CidCircuitModeData.setStatus(_A)
class _Aal2CidFrameModeData_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Aal2CidFrameModeData_Type.__name__=_B
_Aal2CidFrameModeData_Object=MibTableColumn
aal2CidFrameModeData=_Aal2CidFrameModeData_Object((1,3,6,1,4,1,5504,4,2,1,2,1,8),_Aal2CidFrameModeData_Type())
aal2CidFrameModeData.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2CidFrameModeData.setStatus(_A)
class _Aal2CidFaxDemoRemo_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Aal2CidFaxDemoRemo_Type.__name__=_B
_Aal2CidFaxDemoRemo_Object=MibTableColumn
aal2CidFaxDemoRemo=_Aal2CidFaxDemoRemo_Object((1,3,6,1,4,1,5504,4,2,1,2,1,9),_Aal2CidFaxDemoRemo_Type())
aal2CidFaxDemoRemo.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2CidFaxDemoRemo.setStatus(_A)
class _Aal2CidCAS_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Aal2CidCAS_Type.__name__=_B
_Aal2CidCAS_Object=MibTableColumn
aal2CidCAS=_Aal2CidCAS_Object((1,3,6,1,4,1,5504,4,2,1,2,1,10),_Aal2CidCAS_Type())
aal2CidCAS.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2CidCAS.setStatus(_A)
class _Aal2CidDTMFDialedDigits_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Aal2CidDTMFDialedDigits_Type.__name__=_B
_Aal2CidDTMFDialedDigits_Object=MibTableColumn
aal2CidDTMFDialedDigits=_Aal2CidDTMFDialedDigits_Object((1,3,6,1,4,1,5504,4,2,1,2,1,11),_Aal2CidDTMFDialedDigits_Type())
aal2CidDTMFDialedDigits.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2CidDTMFDialedDigits.setStatus(_A)
class _Aal2CidMfR1DialedDigits_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Aal2CidMfR1DialedDigits_Type.__name__=_B
_Aal2CidMfR1DialedDigits_Object=MibTableColumn
aal2CidMfR1DialedDigits=_Aal2CidMfR1DialedDigits_Object((1,3,6,1,4,1,5504,4,2,1,2,1,12),_Aal2CidMfR1DialedDigits_Type())
aal2CidMfR1DialedDigits.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2CidMfR1DialedDigits.setStatus(_A)
class _Aal2CidMfR2DialedDigits_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Aal2CidMfR2DialedDigits_Type.__name__=_B
_Aal2CidMfR2DialedDigits_Object=MibTableColumn
aal2CidMfR2DialedDigits=_Aal2CidMfR2DialedDigits_Object((1,3,6,1,4,1,5504,4,2,1,2,1,13),_Aal2CidMfR2DialedDigits_Type())
aal2CidMfR2DialedDigits.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2CidMfR2DialedDigits.setStatus(_A)
class _Aal2CidPCMEncoding_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_Aal2CidPCMEncoding_Type.__name__=_B
_Aal2CidPCMEncoding_Object=MibTableColumn
aal2CidPCMEncoding=_Aal2CidPCMEncoding_Object((1,3,6,1,4,1,5504,4,2,1,2,1,14),_Aal2CidPCMEncoding_Type())
aal2CidPCMEncoding.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2CidPCMEncoding.setStatus(_A)
class _Aal2CidMaxLengthFrame_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Aal2CidMaxLengthFrame_Type.__name__=_B
_Aal2CidMaxLengthFrame_Object=MibTableColumn
aal2CidMaxLengthFrame=_Aal2CidMaxLengthFrame_Object((1,3,6,1,4,1,5504,4,2,1,2,1,15),_Aal2CidMaxLengthFrame_Type())
aal2CidMaxLengthFrame.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2CidMaxLengthFrame.setStatus(_A)
if mibBuilder.loadTexts:aal2CidMaxLengthFrame.setUnits(_L)
class _Aal2CidMaxSDULength_Type(Integer32):defaultValue=1536;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65568))
_Aal2CidMaxSDULength_Type.__name__=_B
_Aal2CidMaxSDULength_Object=MibTableColumn
aal2CidMaxSDULength=_Aal2CidMaxSDULength_Object((1,3,6,1,4,1,5504,4,2,1,2,1,16),_Aal2CidMaxSDULength_Type())
aal2CidMaxSDULength.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2CidMaxSDULength.setStatus(_A)
if mibBuilder.loadTexts:aal2CidMaxSDULength.setUnits(_L)
class _Aal2CidRasTimer_Type(Integer32):defaultValue=0
_Aal2CidRasTimer_Type.__name__=_B
_Aal2CidRasTimer_Object=MibTableColumn
aal2CidRasTimer=_Aal2CidRasTimer_Object((1,3,6,1,4,1,5504,4,2,1,2,1,17),_Aal2CidRasTimer_Type())
aal2CidRasTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2CidRasTimer.setStatus(_A)
if mibBuilder.loadTexts:aal2CidRasTimer.setUnits(_b)
class _Aal2CidPreferredApIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_Aal2CidPreferredApIndex_Type.__name__=_B
_Aal2CidPreferredApIndex_Object=MibTableColumn
aal2CidPreferredApIndex=_Aal2CidPreferredApIndex_Object((1,3,6,1,4,1,5504,4,2,1,2,1,18),_Aal2CidPreferredApIndex_Type())
aal2CidPreferredApIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2CidPreferredApIndex.setStatus(_A)
_Aal2CidCellsReceived_Type=Gauge32
_Aal2CidCellsReceived_Object=MibTableColumn
aal2CidCellsReceived=_Aal2CidCellsReceived_Object((1,3,6,1,4,1,5504,4,2,1,2,1,19),_Aal2CidCellsReceived_Type())
aal2CidCellsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2CidCellsReceived.setStatus(_A)
_Aal2CidCellsSent_Type=Gauge32
_Aal2CidCellsSent_Object=MibTableColumn
aal2CidCellsSent=_Aal2CidCellsSent_Object((1,3,6,1,4,1,5504,4,2,1,2,1,20),_Aal2CidCellsSent_Type())
aal2CidCellsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2CidCellsSent.setStatus(_A)
_Aal2CidStatsTimeElapsed_Type=Integer32
_Aal2CidStatsTimeElapsed_Object=MibTableColumn
aal2CidStatsTimeElapsed=_Aal2CidStatsTimeElapsed_Object((1,3,6,1,4,1,5504,4,2,1,2,1,21),_Aal2CidStatsTimeElapsed_Type())
aal2CidStatsTimeElapsed.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2CidStatsTimeElapsed.setStatus(_A)
_Aal2CidRowStatus_Type=ZhoneRowStatus
_Aal2CidRowStatus_Object=MibTableColumn
aal2CidRowStatus=_Aal2CidRowStatus_Object((1,3,6,1,4,1,5504,4,2,1,2,1,22),_Aal2CidRowStatus_Type())
aal2CidRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2CidRowStatus.setStatus(_A)
_Aal2CidCompletedCalls_Type=Counter32
_Aal2CidCompletedCalls_Object=MibTableColumn
aal2CidCompletedCalls=_Aal2CidCompletedCalls_Object((1,3,6,1,4,1,5504,4,2,1,2,1,23),_Aal2CidCompletedCalls_Type())
aal2CidCompletedCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2CidCompletedCalls.setStatus(_A)
_Aal2CidBlockedCallsNoBandwidth_Type=Counter32
_Aal2CidBlockedCallsNoBandwidth_Object=MibTableColumn
aal2CidBlockedCallsNoBandwidth=_Aal2CidBlockedCallsNoBandwidth_Object((1,3,6,1,4,1,5504,4,2,1,2,1,24),_Aal2CidBlockedCallsNoBandwidth_Type())
aal2CidBlockedCallsNoBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2CidBlockedCallsNoBandwidth.setStatus(_A)
_Aal2UserDefinedAudioProfileNextIndexTable_Object=MibTable
aal2UserDefinedAudioProfileNextIndexTable=_Aal2UserDefinedAudioProfileNextIndexTable_Object((1,3,6,1,4,1,5504,4,2,1,3))
if mibBuilder.loadTexts:aal2UserDefinedAudioProfileNextIndexTable.setStatus(_A)
_Aal2UserDefinedAudioProfileNextIndexEntry_Object=MibTableRow
aal2UserDefinedAudioProfileNextIndexEntry=_Aal2UserDefinedAudioProfileNextIndexEntry_Object((1,3,6,1,4,1,5504,4,2,1,3,1))
aal2UserDefinedAudioProfileNextIndexEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:aal2UserDefinedAudioProfileNextIndexEntry.setStatus(_A)
class _Aal2UdApNextIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Aal2UdApNextIndex_Type.__name__=_B
_Aal2UdApNextIndex_Object=MibTableColumn
aal2UdApNextIndex=_Aal2UdApNextIndex_Object((1,3,6,1,4,1,5504,4,2,1,3,1,1),_Aal2UdApNextIndex_Type())
aal2UdApNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2UdApNextIndex.setStatus(_A)
_Aal2AudioProfileTable_Object=MibTable
aal2AudioProfileTable=_Aal2AudioProfileTable_Object((1,3,6,1,4,1,5504,4,2,1,4))
if mibBuilder.loadTexts:aal2AudioProfileTable.setStatus(_A)
_Aal2AudioProfileEntry_Object=MibTableRow
aal2AudioProfileEntry=_Aal2AudioProfileEntry_Object((1,3,6,1,4,1,5504,4,2,1,4,1))
aal2AudioProfileEntry.setIndexNames((0,_E,_Y),(0,_E,_c))
if mibBuilder.loadTexts:aal2AudioProfileEntry.setStatus(_A)
class _Aal2ApIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_Aal2ApIndex_Type.__name__=_B
_Aal2ApIndex_Object=MibTableColumn
aal2ApIndex=_Aal2ApIndex_Object((1,3,6,1,4,1,5504,4,2,1,4,1,1),_Aal2ApIndex_Type())
aal2ApIndex.setMaxAccess(_R)
if mibBuilder.loadTexts:aal2ApIndex.setStatus(_A)
class _Aal2ApMinUUI_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Aal2ApMinUUI_Type.__name__=_B
_Aal2ApMinUUI_Object=MibTableColumn
aal2ApMinUUI=_Aal2ApMinUUI_Object((1,3,6,1,4,1,5504,4,2,1,4,1,2),_Aal2ApMinUUI_Type())
aal2ApMinUUI.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ApMinUUI.setStatus(_A)
class _Aal2ApMaxUUI_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_Aal2ApMaxUUI_Type.__name__=_B
_Aal2ApMaxUUI_Object=MibTableColumn
aal2ApMaxUUI=_Aal2ApMaxUUI_Object((1,3,6,1,4,1,5504,4,2,1,4,1,3),_Aal2ApMaxUUI_Type())
aal2ApMaxUUI.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ApMaxUUI.setStatus(_A)
class _Aal2ApSduMultiples_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Aal2ApSduMultiples_Type.__name__=_B
_Aal2ApSduMultiples_Object=MibTableColumn
aal2ApSduMultiples=_Aal2ApSduMultiples_Object((1,3,6,1,4,1,5504,4,2,1,4,1,4),_Aal2ApSduMultiples_Type())
aal2ApSduMultiples.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ApSduMultiples.setStatus(_A)
class _Aal2ApAlgorithm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('g711',1),('g722',2),('g723',3),('g72632',4),('g727',5),('g728',6),('g729Edu',7),('g729Sid',8),('g72964',9),('g72912',10),('genericSid',11)))
_Aal2ApAlgorithm_Type.__name__=_B
_Aal2ApAlgorithm_Object=MibTableColumn
aal2ApAlgorithm=_Aal2ApAlgorithm_Object((1,3,6,1,4,1,5504,4,2,1,4,1,5),_Aal2ApAlgorithm_Type())
aal2ApAlgorithm.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ApAlgorithm.setStatus(_A)
class _Aal2ApPktTime_Type(Integer32):defaultValue=55;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,110))
_Aal2ApPktTime_Type.__name__=_B
_Aal2ApPktTime_Object=MibTableColumn
aal2ApPktTime=_Aal2ApPktTime_Object((1,3,6,1,4,1,5504,4,2,1,4,1,6),_Aal2ApPktTime_Type())
aal2ApPktTime.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ApPktTime.setStatus(_A)
if mibBuilder.loadTexts:aal2ApPktTime.setUnits(_d)
class _Aal2ApSequence_Type(Integer32):defaultValue=55;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,110))
_Aal2ApSequence_Type.__name__=_B
_Aal2ApSequence_Object=MibTableColumn
aal2ApSequence=_Aal2ApSequence_Object((1,3,6,1,4,1,5504,4,2,1,4,1,7),_Aal2ApSequence_Type())
aal2ApSequence.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ApSequence.setStatus(_A)
if mibBuilder.loadTexts:aal2ApSequence.setUnits(_d)
_Aal2ApRowStatus_Type=ZhoneRowStatus
_Aal2ApRowStatus_Object=MibTableColumn
aal2ApRowStatus=_Aal2ApRowStatus_Object((1,3,6,1,4,1,5504,4,2,1,4,1,8),_Aal2ApRowStatus_Type())
aal2ApRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ApRowStatus.setStatus(_A)
class _Aal2ApSilenceSupression_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Aal2ApSilenceSupression_Type.__name__=_B
_Aal2ApSilenceSupression_Object=MibTableColumn
aal2ApSilenceSupression=_Aal2ApSilenceSupression_Object((1,3,6,1,4,1,5504,4,2,1,4,1,9),_Aal2ApSilenceSupression_Type())
aal2ApSilenceSupression.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ApSilenceSupression.setStatus(_A)
class _Aal2ApPacketLength_Type(Integer32):defaultValue=44;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_Aal2ApPacketLength_Type.__name__=_B
_Aal2ApPacketLength_Object=MibTableColumn
aal2ApPacketLength=_Aal2ApPacketLength_Object((1,3,6,1,4,1,5504,4,2,1,4,1,10),_Aal2ApPacketLength_Type())
aal2ApPacketLength.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ApPacketLength.setStatus(_A)
if mibBuilder.loadTexts:aal2ApPacketLength.setUnits(_L)
_Aal2CpsPerformanceTable_Object=MibTable
aal2CpsPerformanceTable=_Aal2CpsPerformanceTable_Object((1,3,6,1,4,1,5504,4,2,1,5))
if mibBuilder.loadTexts:aal2CpsPerformanceTable.setStatus(_A)
_Aal2CpsPerformanceEntry_Object=MibTableRow
aal2CpsPerformanceEntry=_Aal2CpsPerformanceEntry_Object((1,3,6,1,4,1,5504,4,2,1,5,1))
if mibBuilder.loadTexts:aal2CpsPerformanceEntry.setStatus(_A)
_Aal2CpsPerfSTFParity_Type=Counter32
_Aal2CpsPerfSTFParity_Object=MibTableColumn
aal2CpsPerfSTFParity=_Aal2CpsPerfSTFParity_Object((1,3,6,1,4,1,5504,4,2,1,5,1,1),_Aal2CpsPerfSTFParity_Type())
aal2CpsPerfSTFParity.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2CpsPerfSTFParity.setStatus(_A)
_Aal2CpsPerfSTFBadSeq_Type=Counter32
_Aal2CpsPerfSTFBadSeq_Object=MibTableColumn
aal2CpsPerfSTFBadSeq=_Aal2CpsPerfSTFBadSeq_Object((1,3,6,1,4,1,5504,4,2,1,5,1,2),_Aal2CpsPerfSTFBadSeq_Type())
aal2CpsPerfSTFBadSeq.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2CpsPerfSTFBadSeq.setStatus(_A)
_Aal2CpsPerfBadCPSLength_Type=Counter32
_Aal2CpsPerfBadCPSLength_Object=MibTableColumn
aal2CpsPerfBadCPSLength=_Aal2CpsPerfBadCPSLength_Object((1,3,6,1,4,1,5504,4,2,1,5,1,3),_Aal2CpsPerfBadCPSLength_Type())
aal2CpsPerfBadCPSLength.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2CpsPerfBadCPSLength.setStatus(_A)
_Aal2CpsPerfBadPayloadLength_Type=Counter32
_Aal2CpsPerfBadPayloadLength_Object=MibTableColumn
aal2CpsPerfBadPayloadLength=_Aal2CpsPerfBadPayloadLength_Object((1,3,6,1,4,1,5504,4,2,1,5,1,4),_Aal2CpsPerfBadPayloadLength_Type())
aal2CpsPerfBadPayloadLength.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2CpsPerfBadPayloadLength.setStatus(_A)
_Aal2CpsPerfHEC_Type=Counter32
_Aal2CpsPerfHEC_Object=MibTableColumn
aal2CpsPerfHEC=_Aal2CpsPerfHEC_Object((1,3,6,1,4,1,5504,4,2,1,5,1,5),_Aal2CpsPerfHEC_Type())
aal2CpsPerfHEC.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2CpsPerfHEC.setStatus(_A)
_Aal2CpsPerfPayloadTooLong_Type=Counter32
_Aal2CpsPerfPayloadTooLong_Object=MibTableColumn
aal2CpsPerfPayloadTooLong=_Aal2CpsPerfPayloadTooLong_Object((1,3,6,1,4,1,5504,4,2,1,5,1,6),_Aal2CpsPerfPayloadTooLong_Type())
aal2CpsPerfPayloadTooLong.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2CpsPerfPayloadTooLong.setStatus(_A)
_Aal2CpsPerfRessError_Type=Counter32
_Aal2CpsPerfRessError_Object=MibTableColumn
aal2CpsPerfRessError=_Aal2CpsPerfRessError_Object((1,3,6,1,4,1,5504,4,2,1,5,1,7),_Aal2CpsPerfRessError_Type())
aal2CpsPerfRessError.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2CpsPerfRessError.setStatus(_A)
_Aal2CpsPerfTransError_Type=Counter32
_Aal2CpsPerfTransError_Object=MibTableColumn
aal2CpsPerfTransError=_Aal2CpsPerfTransError_Object((1,3,6,1,4,1,5504,4,2,1,5,1,8),_Aal2CpsPerfTransError_Type())
aal2CpsPerfTransError.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2CpsPerfTransError.setStatus(_A)
_Aal2CpsPerfIllegalUUI_Type=Counter32
_Aal2CpsPerfIllegalUUI_Object=MibTableColumn
aal2CpsPerfIllegalUUI=_Aal2CpsPerfIllegalUUI_Object((1,3,6,1,4,1,5504,4,2,1,5,1,9),_Aal2CpsPerfIllegalUUI_Type())
aal2CpsPerfIllegalUUI.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2CpsPerfIllegalUUI.setStatus(_A)
_Aal2CpsPerfIllegalCID_Type=Counter32
_Aal2CpsPerfIllegalCID_Object=MibTableColumn
aal2CpsPerfIllegalCID=_Aal2CpsPerfIllegalCID_Object((1,3,6,1,4,1,5504,4,2,1,5,1,10),_Aal2CpsPerfIllegalCID_Type())
aal2CpsPerfIllegalCID.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2CpsPerfIllegalCID.setStatus(_A)
_Aal2CpsPerfCongestion_Type=Counter32
_Aal2CpsPerfCongestion_Object=MibTableColumn
aal2CpsPerfCongestion=_Aal2CpsPerfCongestion_Object((1,3,6,1,4,1,5504,4,2,1,5,1,11),_Aal2CpsPerfCongestion_Type())
aal2CpsPerfCongestion.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2CpsPerfCongestion.setStatus(_A)
_Aal2SscsI3662PerfTable_Object=MibTable
aal2SscsI3662PerfTable=_Aal2SscsI3662PerfTable_Object((1,3,6,1,4,1,5504,4,2,1,6))
if mibBuilder.loadTexts:aal2SscsI3662PerfTable.setStatus(_A)
_Aal2SscsI3662PerfEntry_Object=MibTableRow
aal2SscsI3662PerfEntry=_Aal2SscsI3662PerfEntry_Object((1,3,6,1,4,1,5504,4,2,1,6,1))
aal2SscsI3662PerfEntry.setIndexNames((0,_J,_K),(0,_I,_N),(0,_I,_M),(0,_E,_Q))
if mibBuilder.loadTexts:aal2SscsI3662PerfEntry.setStatus(_A)
_Aal2SscsI3662IllegalUUI_Type=Counter32
_Aal2SscsI3662IllegalUUI_Object=MibTableColumn
aal2SscsI3662IllegalUUI=_Aal2SscsI3662IllegalUUI_Object((1,3,6,1,4,1,5504,4,2,1,6,1,1),_Aal2SscsI3662IllegalUUI_Type())
aal2SscsI3662IllegalUUI.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2SscsI3662IllegalUUI.setStatus(_A)
_Aal2SscsI3662Type3CRC_Type=Counter32
_Aal2SscsI3662Type3CRC_Object=MibTableColumn
aal2SscsI3662Type3CRC=_Aal2SscsI3662Type3CRC_Object((1,3,6,1,4,1,5504,4,2,1,6,1,2),_Aal2SscsI3662Type3CRC_Type())
aal2SscsI3662Type3CRC.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2SscsI3662Type3CRC.setStatus(_A)
_Aal2SscsI3662ProfileError_Type=Counter32
_Aal2SscsI3662ProfileError_Object=MibTableColumn
aal2SscsI3662ProfileError=_Aal2SscsI3662ProfileError_Object((1,3,6,1,4,1,5504,4,2,1,6,1,3),_Aal2SscsI3662ProfileError_Type())
aal2SscsI3662ProfileError.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2SscsI3662ProfileError.setStatus(_A)
_Aal2SscsI3661PerfTable_Object=MibTable
aal2SscsI3661PerfTable=_Aal2SscsI3661PerfTable_Object((1,3,6,1,4,1,5504,4,2,1,7))
if mibBuilder.loadTexts:aal2SscsI3661PerfTable.setStatus(_A)
_Aal2SscsI3661PerfEntry_Object=MibTableRow
aal2SscsI3661PerfEntry=_Aal2SscsI3661PerfEntry_Object((1,3,6,1,4,1,5504,4,2,1,7,1))
aal2SscsI3661PerfEntry.setIndexNames((0,_J,_K),(0,_I,_N),(0,_I,_M),(0,_E,_Q))
if mibBuilder.loadTexts:aal2SscsI3661PerfEntry.setStatus(_A)
_Aal2SscsI3661MsgTooLong_Type=Counter32
_Aal2SscsI3661MsgTooLong_Object=MibTableColumn
aal2SscsI3661MsgTooLong=_Aal2SscsI3661MsgTooLong_Object((1,3,6,1,4,1,5504,4,2,1,7,1,1),_Aal2SscsI3661MsgTooLong_Type())
aal2SscsI3661MsgTooLong.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2SscsI3661MsgTooLong.setStatus(_A)
_Aal2SscsI3661RasTimerExpired_Type=Counter32
_Aal2SscsI3661RasTimerExpired_Object=MibTableColumn
aal2SscsI3661RasTimerExpired=_Aal2SscsI3661RasTimerExpired_Object((1,3,6,1,4,1,5504,4,2,1,7,1,2),_Aal2SscsI3661RasTimerExpired_Type())
aal2SscsI3661RasTimerExpired.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2SscsI3661RasTimerExpired.setStatus(_A)
_Aal2SscsI3661MsgTooShort_Type=Counter32
_Aal2SscsI3661MsgTooShort_Object=MibTableColumn
aal2SscsI3661MsgTooShort=_Aal2SscsI3661MsgTooShort_Object((1,3,6,1,4,1,5504,4,2,1,7,1,3),_Aal2SscsI3661MsgTooShort_Type())
aal2SscsI3661MsgTooShort.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2SscsI3661MsgTooShort.setStatus(_A)
_Aal2SscsI3661BadLength_Type=Counter32
_Aal2SscsI3661BadLength_Object=MibTableColumn
aal2SscsI3661BadLength=_Aal2SscsI3661BadLength_Object((1,3,6,1,4,1,5504,4,2,1,7,1,4),_Aal2SscsI3661BadLength_Type())
aal2SscsI3661BadLength.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2SscsI3661BadLength.setStatus(_A)
_Aal2SscsI3661CRC_Type=Counter32
_Aal2SscsI3661CRC_Object=MibTableColumn
aal2SscsI3661CRC=_Aal2SscsI3661CRC_Object((1,3,6,1,4,1,5504,4,2,1,7,1,5),_Aal2SscsI3661CRC_Type())
aal2SscsI3661CRC.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2SscsI3661CRC.setStatus(_A)
_Aal2vpi_Type=AtmVpIdentifier
_Aal2vpi_Object=MibScalar
aal2vpi=_Aal2vpi_Object((1,3,6,1,4,1,5504,4,2,1,8),_Aal2vpi_Type())
aal2vpi.setMaxAccess(_e)
if mibBuilder.loadTexts:aal2vpi.setStatus(_A)
_Aal2Vci_Type=AtmVcIdentifier
_Aal2Vci_Object=MibScalar
aal2Vci=_Aal2Vci_Object((1,3,6,1,4,1,5504,4,2,1,9),_Aal2Vci_Type())
aal2Vci.setMaxAccess(_e)
if mibBuilder.loadTexts:aal2Vci.setStatus(_A)
_Aal2AlarmConfigTable_Object=MibTable
aal2AlarmConfigTable=_Aal2AlarmConfigTable_Object((1,3,6,1,4,1,5504,4,2,1,10))
if mibBuilder.loadTexts:aal2AlarmConfigTable.setStatus(_A)
_Aal2AlarmConfigEntry_Object=MibTableRow
aal2AlarmConfigEntry=_Aal2AlarmConfigEntry_Object((1,3,6,1,4,1,5504,4,2,1,10,1))
if mibBuilder.loadTexts:aal2AlarmConfigEntry.setStatus(_A)
class _Aal2AlarmConfigThreshCellLoss_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_Aal2AlarmConfigThreshCellLoss_Type.__name__=_B
_Aal2AlarmConfigThreshCellLoss_Object=MibTableColumn
aal2AlarmConfigThreshCellLoss=_Aal2AlarmConfigThreshCellLoss_Object((1,3,6,1,4,1,5504,4,2,1,10,1,1),_Aal2AlarmConfigThreshCellLoss_Type())
aal2AlarmConfigThreshCellLoss.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2AlarmConfigThreshCellLoss.setStatus(_A)
class _Aal2AlarmConfigThreshCongestion_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_Aal2AlarmConfigThreshCongestion_Type.__name__=_B
_Aal2AlarmConfigThreshCongestion_Object=MibTableColumn
aal2AlarmConfigThreshCongestion=_Aal2AlarmConfigThreshCongestion_Object((1,3,6,1,4,1,5504,4,2,1,10,1,2),_Aal2AlarmConfigThreshCongestion_Type())
aal2AlarmConfigThreshCongestion.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2AlarmConfigThreshCongestion.setStatus(_A)
_Aal2ElcpPortTable_Object=MibTable
aal2ElcpPortTable=_Aal2ElcpPortTable_Object((1,3,6,1,4,1,5504,4,2,1,11))
if mibBuilder.loadTexts:aal2ElcpPortTable.setStatus(_A)
_Aal2ElcpPortEntry_Object=MibTableRow
aal2ElcpPortEntry=_Aal2ElcpPortEntry_Object((1,3,6,1,4,1,5504,4,2,1,11,1))
aal2ElcpPortEntry.setIndexNames((0,_J,_K),(0,_I,_N),(0,_I,_M),(0,_E,_f),(0,_E,_g))
if mibBuilder.loadTexts:aal2ElcpPortEntry.setStatus(_A)
class _Aal2ElcpPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_Aal2ElcpPortId_Type.__name__=_B
_Aal2ElcpPortId_Object=MibTableColumn
aal2ElcpPortId=_Aal2ElcpPortId_Object((1,3,6,1,4,1,5504,4,2,1,11,1,1),_Aal2ElcpPortId_Type())
aal2ElcpPortId.setMaxAccess(_R)
if mibBuilder.loadTexts:aal2ElcpPortId.setStatus(_A)
class _Aal2ElcpPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pstn',1),('isdnBra',2)))
_Aal2ElcpPortType_Type.__name__=_B
_Aal2ElcpPortType_Object=MibTableColumn
aal2ElcpPortType=_Aal2ElcpPortType_Object((1,3,6,1,4,1,5504,4,2,1,11,1,2),_Aal2ElcpPortType_Type())
aal2ElcpPortType.setMaxAccess(_R)
if mibBuilder.loadTexts:aal2ElcpPortType.setStatus(_A)
class _Aal2ElcpPortAudioService_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_U,3),(_V,4)))
_Aal2ElcpPortAudioService_Type.__name__=_B
_Aal2ElcpPortAudioService_Object=MibTableColumn
aal2ElcpPortAudioService=_Aal2ElcpPortAudioService_Object((1,3,6,1,4,1,5504,4,2,1,11,1,3),_Aal2ElcpPortAudioService_Type())
aal2ElcpPortAudioService.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ElcpPortAudioService.setStatus(_A)
class _Aal2ElcpPortPCMEncoding_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_Aal2ElcpPortPCMEncoding_Type.__name__=_B
_Aal2ElcpPortPCMEncoding_Object=MibTableColumn
aal2ElcpPortPCMEncoding=_Aal2ElcpPortPCMEncoding_Object((1,3,6,1,4,1,5504,4,2,1,11,1,4),_Aal2ElcpPortPCMEncoding_Type())
aal2ElcpPortPCMEncoding.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ElcpPortPCMEncoding.setStatus(_A)
class _Aal2ElcpPortMaxLengthFrame_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Aal2ElcpPortMaxLengthFrame_Type.__name__=_B
_Aal2ElcpPortMaxLengthFrame_Object=MibTableColumn
aal2ElcpPortMaxLengthFrame=_Aal2ElcpPortMaxLengthFrame_Object((1,3,6,1,4,1,5504,4,2,1,11,1,5),_Aal2ElcpPortMaxLengthFrame_Type())
aal2ElcpPortMaxLengthFrame.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ElcpPortMaxLengthFrame.setStatus(_A)
if mibBuilder.loadTexts:aal2ElcpPortMaxLengthFrame.setUnits(_L)
class _Aal2ElcpPortMaxSDULength_Type(Integer32):defaultValue=1536;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65568))
_Aal2ElcpPortMaxSDULength_Type.__name__=_B
_Aal2ElcpPortMaxSDULength_Object=MibTableColumn
aal2ElcpPortMaxSDULength=_Aal2ElcpPortMaxSDULength_Object((1,3,6,1,4,1,5504,4,2,1,11,1,6),_Aal2ElcpPortMaxSDULength_Type())
aal2ElcpPortMaxSDULength.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ElcpPortMaxSDULength.setStatus(_A)
if mibBuilder.loadTexts:aal2ElcpPortMaxSDULength.setUnits(_L)
class _Aal2ElcpPortPreferredApIndex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_Aal2ElcpPortPreferredApIndex_Type.__name__=_B
_Aal2ElcpPortPreferredApIndex_Object=MibTableColumn
aal2ElcpPortPreferredApIndex=_Aal2ElcpPortPreferredApIndex_Object((1,3,6,1,4,1,5504,4,2,1,11,1,7),_Aal2ElcpPortPreferredApIndex_Type())
aal2ElcpPortPreferredApIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ElcpPortPreferredApIndex.setStatus(_A)
_Aal2ElcpPortRowStatus_Type=ZhoneRowStatus
_Aal2ElcpPortRowStatus_Object=MibTableColumn
aal2ElcpPortRowStatus=_Aal2ElcpPortRowStatus_Object((1,3,6,1,4,1,5504,4,2,1,11,1,8),_Aal2ElcpPortRowStatus_Type())
aal2ElcpPortRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:aal2ElcpPortRowStatus.setStatus(_A)
_Aal2ElcpIgTable_Object=MibTable
aal2ElcpIgTable=_Aal2ElcpIgTable_Object((1,3,6,1,4,1,5504,4,2,1,12))
if mibBuilder.loadTexts:aal2ElcpIgTable.setStatus(_A)
_Aal2ElcpIgEntry_Object=MibTableRow
aal2ElcpIgEntry=_Aal2ElcpIgEntry_Object((1,3,6,1,4,1,5504,4,2,1,12,1))
aal2ElcpIgEntry.setIndexNames((0,_J,_K),(0,_I,_N),(0,_I,_M))
if mibBuilder.loadTexts:aal2ElcpIgEntry.setStatus(_A)
_Aal2ElcpIgOperStatus_Type=AtmVorXOperStatus
_Aal2ElcpIgOperStatus_Object=MibTableColumn
aal2ElcpIgOperStatus=_Aal2ElcpIgOperStatus_Object((1,3,6,1,4,1,5504,4,2,1,12,1,1),_Aal2ElcpIgOperStatus_Type())
aal2ElcpIgOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2ElcpIgOperStatus.setStatus(_A)
_Aal2ElcpIgOperStatusChangeCount_Type=Counter32
_Aal2ElcpIgOperStatusChangeCount_Object=MibTableColumn
aal2ElcpIgOperStatusChangeCount=_Aal2ElcpIgOperStatusChangeCount_Object((1,3,6,1,4,1,5504,4,2,1,12,1,2),_Aal2ElcpIgOperStatusChangeCount_Type())
aal2ElcpIgOperStatusChangeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2ElcpIgOperStatusChangeCount.setStatus(_A)
_Aal2ElcpIgLapvReceived_Type=Counter32
_Aal2ElcpIgLapvReceived_Object=MibTableColumn
aal2ElcpIgLapvReceived=_Aal2ElcpIgLapvReceived_Object((1,3,6,1,4,1,5504,4,2,1,12,1,3),_Aal2ElcpIgLapvReceived_Type())
aal2ElcpIgLapvReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2ElcpIgLapvReceived.setStatus(_A)
_Aal2ElcpIgLapvSent_Type=Counter32
_Aal2ElcpIgLapvSent_Object=MibTableColumn
aal2ElcpIgLapvSent=_Aal2ElcpIgLapvSent_Object((1,3,6,1,4,1,5504,4,2,1,12,1,4),_Aal2ElcpIgLapvSent_Type())
aal2ElcpIgLapvSent.setMaxAccess(_C)
if mibBuilder.loadTexts:aal2ElcpIgLapvSent.setStatus(_A)
aal2VclEntry.registerAugmentions((_E,_h))
aal2CpsPerformanceEntry.setIndexNames(*aal2VclEntry.getIndexNames())
aal2VclEntry.registerAugmentions((_E,_i))
aal2AlarmConfigEntry.setIndexNames(*aal2VclEntry.getIndexNames())
aal2ExternalAIS=NotificationType((1,3,6,1,4,1,5504,4,2,1,0,1))
aal2ExternalAIS.setObjects(*((_J,_K),(_E,_O),(_E,_P)))
if mibBuilder.loadTexts:aal2ExternalAIS.setStatus(_A)
aal2ExternalRAI=NotificationType((1,3,6,1,4,1,5504,4,2,1,0,2))
aal2ExternalRAI.setObjects(*((_J,_K),(_E,_O),(_E,_P)))
if mibBuilder.loadTexts:aal2ExternalRAI.setStatus(_A)
aal2InternalAIS=NotificationType((1,3,6,1,4,1,5504,4,2,1,0,3))
aal2InternalAIS.setObjects(*((_J,_K),(_E,_O),(_E,_P),(_S,_T)))
if mibBuilder.loadTexts:aal2InternalAIS.setStatus(_A)
aal2InternalRDI=NotificationType((1,3,6,1,4,1,5504,4,2,1,0,4))
aal2InternalRDI.setObjects(*((_J,_K),(_E,_O),(_E,_P),(_S,_T)))
if mibBuilder.loadTexts:aal2InternalRDI.setStatus(_A)
aal2PvcDown=NotificationType((1,3,6,1,4,1,5504,4,2,1,0,5))
aal2PvcDown.setObjects(*((_J,_K),(_E,_O),(_E,_P)))
if mibBuilder.loadTexts:aal2PvcDown.setStatus(_A)
aal2PerfCellLossThreshTrap=NotificationType((1,3,6,1,4,1,5504,4,2,1,0,6))
aal2PerfCellLossThreshTrap.setObjects(*((_E,_j),(_E,_k)))
if mibBuilder.loadTexts:aal2PerfCellLossThreshTrap.setStatus(_A)
aal2PerfCongestionThreshTrap=NotificationType((1,3,6,1,4,1,5504,4,2,1,0,7))
aal2PerfCongestionThreshTrap.setObjects(*((_E,_l),(_E,_m)))
if mibBuilder.loadTexts:aal2PerfCongestionThreshTrap.setStatus(_A)
aal2ElcpIgOperStatusChange=NotificationType((1,3,6,1,4,1,5504,4,2,1,0,8))
aal2ElcpIgOperStatusChange.setObjects((_E,_n))
if mibBuilder.loadTexts:aal2ElcpIgOperStatusChange.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zhoneAtmAAl2':zhoneAtmAAl2,'aal2Traps':aal2Traps,'aal2ExternalAIS':aal2ExternalAIS,'aal2ExternalRAI':aal2ExternalRAI,'aal2InternalAIS':aal2InternalAIS,'aal2InternalRDI':aal2InternalRDI,'aal2PvcDown':aal2PvcDown,'aal2PerfCellLossThreshTrap':aal2PerfCellLossThreshTrap,'aal2PerfCongestionThreshTrap':aal2PerfCongestionThreshTrap,'aal2ElcpIgOperStatusChange':aal2ElcpIgOperStatusChange,'aal2VclTable':aal2VclTable,'aal2VclEntry':aal2VclEntry,'atmVccAal2AppId':atmVccAal2AppId,'atmVccAal2VccI':atmVccAal2VccI,'atmVccAal2SigVccI':atmVccAal2SigVccI,_Y:aal2VclAudioProfileIdentifier,'aal2VclSscsDefaultType':aal2VclSscsDefaultType,'aal2VclMaxCpsSduSize':aal2VclMaxCpsSduSize,'aal2VclMaxNumberMultiplexChannels':aal2VclMaxNumberMultiplexChannels,'aal2VclMinCidForAal2UserChannels':aal2VclMinCidForAal2UserChannels,'aal2VclMaxCidForAal2UserChannels':aal2VclMaxCidForAal2UserChannels,'aal2VclNextCid':aal2VclNextCid,'aal2VclTimerCU':aal2VclTimerCU,'aal2VclAudioService':aal2VclAudioService,'aal2VclCircuitModeData':aal2VclCircuitModeData,'aal2VclFrameModeData':aal2VclFrameModeData,'aal2VclFaxDemoRemo':aal2VclFaxDemoRemo,'aal2VclCAS':aal2VclCAS,'aal2VclTrunkType':aal2VclTrunkType,'aal2VclDTMFDialedDigits':aal2VclDTMFDialedDigits,'aal2VclMfR1DialedDigits':aal2VclMfR1DialedDigits,'aal2VclMfR2DialedDigits':aal2VclMfR2DialedDigits,'aal2VclPCMEncoding':aal2VclPCMEncoding,'aal2VclMaxLengthFrame':aal2VclMaxLengthFrame,'aal2VclMaxSDULength':aal2VclMaxSDULength,'aal2VclRasTimer':aal2VclRasTimer,'aal2VclCellsReceived':aal2VclCellsReceived,'aal2VclCellsSent':aal2VclCellsSent,'aal2VclStatsTimeElapsed':aal2VclStatsTimeElapsed,'aal2CidTable':aal2CidTable,'aal2CidEntry':aal2CidEntry,_Q:aal2Cid,'aal2CidAdminStatus':aal2CidAdminStatus,'aal2CidOperStatus':aal2CidOperStatus,'aal2CidLastChange':aal2CidLastChange,'aal2CidSscsType':aal2CidSscsType,'aal2CidAudioService':aal2CidAudioService,'aal2CidCircuitModeData':aal2CidCircuitModeData,'aal2CidFrameModeData':aal2CidFrameModeData,'aal2CidFaxDemoRemo':aal2CidFaxDemoRemo,'aal2CidCAS':aal2CidCAS,'aal2CidDTMFDialedDigits':aal2CidDTMFDialedDigits,'aal2CidMfR1DialedDigits':aal2CidMfR1DialedDigits,'aal2CidMfR2DialedDigits':aal2CidMfR2DialedDigits,'aal2CidPCMEncoding':aal2CidPCMEncoding,'aal2CidMaxLengthFrame':aal2CidMaxLengthFrame,'aal2CidMaxSDULength':aal2CidMaxSDULength,'aal2CidRasTimer':aal2CidRasTimer,'aal2CidPreferredApIndex':aal2CidPreferredApIndex,'aal2CidCellsReceived':aal2CidCellsReceived,'aal2CidCellsSent':aal2CidCellsSent,'aal2CidStatsTimeElapsed':aal2CidStatsTimeElapsed,'aal2CidRowStatus':aal2CidRowStatus,'aal2CidCompletedCalls':aal2CidCompletedCalls,'aal2CidBlockedCallsNoBandwidth':aal2CidBlockedCallsNoBandwidth,'aal2UserDefinedAudioProfileNextIndexTable':aal2UserDefinedAudioProfileNextIndexTable,'aal2UserDefinedAudioProfileNextIndexEntry':aal2UserDefinedAudioProfileNextIndexEntry,'aal2UdApNextIndex':aal2UdApNextIndex,'aal2AudioProfileTable':aal2AudioProfileTable,'aal2AudioProfileEntry':aal2AudioProfileEntry,_c:aal2ApIndex,'aal2ApMinUUI':aal2ApMinUUI,'aal2ApMaxUUI':aal2ApMaxUUI,'aal2ApSduMultiples':aal2ApSduMultiples,'aal2ApAlgorithm':aal2ApAlgorithm,'aal2ApPktTime':aal2ApPktTime,'aal2ApSequence':aal2ApSequence,'aal2ApRowStatus':aal2ApRowStatus,'aal2ApSilenceSupression':aal2ApSilenceSupression,'aal2ApPacketLength':aal2ApPacketLength,'aal2CpsPerformanceTable':aal2CpsPerformanceTable,_h:aal2CpsPerformanceEntry,'aal2CpsPerfSTFParity':aal2CpsPerfSTFParity,_j:aal2CpsPerfSTFBadSeq,'aal2CpsPerfBadCPSLength':aal2CpsPerfBadCPSLength,'aal2CpsPerfBadPayloadLength':aal2CpsPerfBadPayloadLength,'aal2CpsPerfHEC':aal2CpsPerfHEC,'aal2CpsPerfPayloadTooLong':aal2CpsPerfPayloadTooLong,'aal2CpsPerfRessError':aal2CpsPerfRessError,'aal2CpsPerfTransError':aal2CpsPerfTransError,'aal2CpsPerfIllegalUUI':aal2CpsPerfIllegalUUI,'aal2CpsPerfIllegalCID':aal2CpsPerfIllegalCID,_l:aal2CpsPerfCongestion,'aal2SscsI3662PerfTable':aal2SscsI3662PerfTable,'aal2SscsI3662PerfEntry':aal2SscsI3662PerfEntry,'aal2SscsI3662IllegalUUI':aal2SscsI3662IllegalUUI,'aal2SscsI3662Type3CRC':aal2SscsI3662Type3CRC,'aal2SscsI3662ProfileError':aal2SscsI3662ProfileError,'aal2SscsI3661PerfTable':aal2SscsI3661PerfTable,'aal2SscsI3661PerfEntry':aal2SscsI3661PerfEntry,'aal2SscsI3661MsgTooLong':aal2SscsI3661MsgTooLong,'aal2SscsI3661RasTimerExpired':aal2SscsI3661RasTimerExpired,'aal2SscsI3661MsgTooShort':aal2SscsI3661MsgTooShort,'aal2SscsI3661BadLength':aal2SscsI3661BadLength,'aal2SscsI3661CRC':aal2SscsI3661CRC,_O:aal2vpi,_P:aal2Vci,'aal2AlarmConfigTable':aal2AlarmConfigTable,_i:aal2AlarmConfigEntry,_k:aal2AlarmConfigThreshCellLoss,_m:aal2AlarmConfigThreshCongestion,'aal2ElcpPortTable':aal2ElcpPortTable,'aal2ElcpPortEntry':aal2ElcpPortEntry,_f:aal2ElcpPortId,_g:aal2ElcpPortType,'aal2ElcpPortAudioService':aal2ElcpPortAudioService,'aal2ElcpPortPCMEncoding':aal2ElcpPortPCMEncoding,'aal2ElcpPortMaxLengthFrame':aal2ElcpPortMaxLengthFrame,'aal2ElcpPortMaxSDULength':aal2ElcpPortMaxSDULength,'aal2ElcpPortPreferredApIndex':aal2ElcpPortPreferredApIndex,'aal2ElcpPortRowStatus':aal2ElcpPortRowStatus,'aal2ElcpIgTable':aal2ElcpIgTable,'aal2ElcpIgEntry':aal2ElcpIgEntry,_n:aal2ElcpIgOperStatus,'aal2ElcpIgOperStatusChangeCount':aal2ElcpIgOperStatusChangeCount,'aal2ElcpIgLapvReceived':aal2ElcpIgLapvReceived,'aal2ElcpIgLapvSent':aal2ElcpIgLapvSent})