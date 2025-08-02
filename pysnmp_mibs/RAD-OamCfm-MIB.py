_AR='dot1agXCfmMepCcStatus'
_AQ='ethOamRMepIntervalNumber'
_AP='ethOamMepIntervalNumber'
_AO='ethOamConfigIdx'
_AN='ethOamMepFlowIndex2'
_AM='ethOamMepFlowIndex1'
_AL='ethOamMepFlowType'
_AK='ethOamMipVlanId'
_AJ='ethOamMipIfIndex'
_AI='ethIfOamCfmMhfIdx'
_AH='ethIfOamCfmMhfMipIdx'
_AG='ethIfOamCfmMhfMdIdx'
_AF='biDirectional'
_AE='ethIfOamCfmMipIdx'
_AD='ethIfOamCfmMipMdIdx'
_AC='radMepRemoteMepIdx'
_AB='radMepLtrReceiveOrder'
_AA='radMdIndex'
_A9='ethOamDelayIntervalBinNumber'
_A8='ethOamDelayIntervalBinCounterType'
_A7='ethOamDelayCurrentBinNumber'
_A6='ethOamDelayCurrentBinCounterType'
_A5='ethOamMeasureBinProfileIndex'
_A4='ethOamSvcRmonConfigPerfAttrib'
_A3='ethOamDestNeIdx'
_A2='charString'
_A1='SNMPv2-MIB'
_A0='SnmpAdminString'
_z='dot1agCfmMepDbRMepIdentifier'
_y='dot1agCfmMaMepListIdentifier'
_x='unexpectedPeriod'
_w='ethOamSvcIntervalNum'
_v='enable'
_u='disable'
_t='yes'
_s='unexpectedMeLevel'
_r='fail'
_q='multicast'
_p='unicast'
_o='disabled'
_n='ethOamRMepStatsRMepId'
_m='unexpectedMep'
_l='mismerge'
_k='Dot1agCfmCcmInterval'
_j='on'
_i='off'
_h='notApplicable'
_g='Bits'
_f='none'
_e='OctetString'
_d='ethOamServiceIdx'
_c='dot1agCfmMepIdentifier'
_b='radOamEvcIdx'
_a='dot1agXCfmMaMepListDescr'
_Z='deprecated'
_Y='dot1agCfmMaIndex'
_X='radMepIdx'
_W='radOamIdx1'
_V='dot1agCfmMdIndex'
_U='ethOamDestNeDescr'
_T='read-write'
_S='seconds'
_R='dot1agCfmMdName'
_Q='dot1agCfmMaNetName'
_P='alarmEventReason'
_O='alarmEventLogSourceName'
_N='alarmEventLogSeverity'
_M='alarmEventLogDescription'
_L='alarmEventLogDateAndTime'
_K='alarmEventLogAlarmOrEventId'
_J='Unsigned32'
_I='not-accessible'
_H='Integer32'
_G='microseconds'
_F='IEEE8021-CFM-MIB'
_E='RAD-OamCfm-MIB'
_D='read-create'
_C='RAD-GEN-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_e,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dot1agCfmCcmInterval,Dot1agCfmMepId,dot1agCfmMaIndex,dot1agCfmMaMepListIdentifier,dot1agCfmMaNetName,dot1agCfmMdIndex,dot1agCfmMdName,dot1agCfmMepDbRMepIdentifier,dot1agCfmMepDbRMepState,dot1agCfmMepDbRdi,dot1agCfmMepDefects,dot1agCfmMepIdentifier=mibBuilder.importSymbols(_F,_k,'Dot1agCfmMepId',_Y,_y,_Q,_V,_R,_z,'dot1agCfmMepDbRMepState','dot1agCfmMepDbRdi','dot1agCfmMepDefects',_c)
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
LldpPortIdSubtype,=mibBuilder.importSymbols('LLDP-MIB','LldpPortIdSubtype')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
ethIf,=mibBuilder.importSymbols('RAD-EthIf-MIB','ethIf')
alarmEventLogAlarmOrEventId,alarmEventLogDateAndTime,alarmEventLogDescription,alarmEventLogSeverity,alarmEventLogSourceName,alarmEventReason=mibBuilder.importSymbols(_C,_K,_L,_M,_N,_O,_P)
DayType,RadTestPbitValues=mibBuilder.importSymbols('RAD-TC','DayType','RadTestPbitValues')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_A0)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_A1,'sysName')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_g,'Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
ethIfOamCfm=ModuleIdentity((1,3,6,1,4,1,164,3,1,6,1,3))
class EthOamBinCounterType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('rtDelay',1),('rtDelayVar',2),('fwDelay',3),('fwDelayVar',4),('bwDelay',5),('bwDelayVar',6)))
_EthIfOamCfmEvents_ObjectIdentity=ObjectIdentity
ethIfOamCfmEvents=_EthIfOamCfmEvents_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,1,3,0))
_RadMepTable_Object=MibTable
radMepTable=_RadMepTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,1))
if mibBuilder.loadTexts:radMepTable.setStatus(_Z)
_RadMepEntry_Object=MibTableRow
radMepEntry=_RadMepEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1))
radMepEntry.setIndexNames((0,_E,_W),(0,_E,_b),(0,_E,_X))
if mibBuilder.loadTexts:radMepEntry.setStatus(_Z)
_RadOamIdx1_Type=Unsigned32
_RadOamIdx1_Object=MibTableColumn
radOamIdx1=_RadOamIdx1_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,1),_RadOamIdx1_Type())
radOamIdx1.setMaxAccess(_I)
if mibBuilder.loadTexts:radOamIdx1.setStatus(_Z)
_RadOamEvcIdx_Type=Unsigned32
_RadOamEvcIdx_Object=MibTableColumn
radOamEvcIdx=_RadOamEvcIdx_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,2),_RadOamEvcIdx_Type())
radOamEvcIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:radOamEvcIdx.setStatus(_Z)
_RadMepIdx_Type=Unsigned32
_RadMepIdx_Object=MibTableColumn
radMepIdx=_RadMepIdx_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,3),_RadMepIdx_Type())
radMepIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:radMepIdx.setStatus(_Z)
_RadMepRowStatus_Type=RowStatus
_RadMepRowStatus_Object=MibTableColumn
radMepRowStatus=_RadMepRowStatus_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,4),_RadMepRowStatus_Type())
radMepRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepRowStatus.setStatus(_Z)
_RadMepLocalMepId_Type=Unsigned32
_RadMepLocalMepId_Object=MibTableColumn
radMepLocalMepId=_RadMepLocalMepId_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,5),_RadMepLocalMepId_Type())
radMepLocalMepId.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepLocalMepId.setStatus(_A)
_RadMepRemoteMepId_Type=Unsigned32
_RadMepRemoteMepId_Object=MibTableColumn
radMepRemoteMepId=_RadMepRemoteMepId_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,6),_RadMepRemoteMepId_Type())
radMepRemoteMepId.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepRemoteMepId.setStatus(_A)
class _RadMepOamMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_o,2),('initiate',3),('react',4)))
_RadMepOamMode_Type.__name__=_H
_RadMepOamMode_Object=MibTableColumn
radMepOamMode=_RadMepOamMode_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,7),_RadMepOamMode_Type())
radMepOamMode.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepOamMode.setStatus(_A)
class _RadMepContinuityVerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_o,2),('ccBased',3),('lbBased',4)))
_RadMepContinuityVerMode_Type.__name__=_H
_RadMepContinuityVerMode_Object=MibTableColumn
radMepContinuityVerMode=_RadMepContinuityVerMode_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,8),_RadMepContinuityVerMode_Type())
radMepContinuityVerMode.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepContinuityVerMode.setStatus(_A)
class _RadMepMeLevel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RadMepMeLevel_Type.__name__=_J
_RadMepMeLevel_Object=MibTableColumn
radMepMeLevel=_RadMepMeLevel_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,9),_RadMepMeLevel_Type())
radMepMeLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepMeLevel.setStatus(_A)
class _RadMepOamDestAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_p,1),(_q,2)))
_RadMepOamDestAddrType_Type.__name__=_H
_RadMepOamDestAddrType_Object=MibTableColumn
radMepOamDestAddrType=_RadMepOamDestAddrType_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,10),_RadMepOamDestAddrType_Type())
radMepOamDestAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepOamDestAddrType.setStatus(_A)
_RadMepOamDestMacAddr_Type=MacAddress
_RadMepOamDestMacAddr_Object=MibTableColumn
radMepOamDestMacAddr=_RadMepOamDestMacAddr_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,11),_RadMepOamDestMacAddr_Type())
radMepOamDestMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepOamDestMacAddr.setStatus(_A)
class _RadMepDefaultPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RadMepDefaultPriority_Type.__name__=_J
_RadMepDefaultPriority_Object=MibTableColumn
radMepDefaultPriority=_RadMepDefaultPriority_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,12),_RadMepDefaultPriority_Type())
radMepDefaultPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepDefaultPriority.setStatus(_A)
class _RadMepCcStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_h,1),(_r,2),('ok',3),(_l,4),(_m,5),(_s,6)))
_RadMepCcStatus_Type.__name__=_H
_RadMepCcStatus_Object=MibTableColumn
radMepCcStatus=_RadMepCcStatus_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,13),_RadMepCcStatus_Type())
radMepCcStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:radMepCcStatus.setStatus(_A)
class _RadMepOamProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('proprietary',1),('standard',2)))
_RadMepOamProtocol_Type.__name__=_H
_RadMepOamProtocol_Object=MibTableColumn
radMepOamProtocol=_RadMepOamProtocol_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,14),_RadMepOamProtocol_Type())
radMepOamProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepOamProtocol.setStatus(_A)
_RadMepMdId_Type=Unsigned32
_RadMepMdId_Object=MibTableColumn
radMepMdId=_RadMepMdId_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,15),_RadMepMdId_Type())
radMepMdId.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepMdId.setStatus(_A)
class _RadMepMaFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,32)));namedValues=NamedValues(*(('primaryVid',1),(_A2,2),('unsignedInt16',3),('rfc2865VpnId',4),('icc',32)))
_RadMepMaFormat_Type.__name__=_H
_RadMepMaFormat_Object=MibTableColumn
radMepMaFormat=_RadMepMaFormat_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,16),_RadMepMaFormat_Type())
radMepMaFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepMaFormat.setStatus(_A)
class _RadMepMaName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,45))
_RadMepMaName_Type.__name__=_e
_RadMepMaName_Object=MibTableColumn
radMepMaName=_RadMepMaName_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,17),_RadMepMaName_Type())
radMepMaName.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepMaName.setStatus(_A)
_RadMepSpVlanId_Type=Unsigned32
_RadMepSpVlanId_Object=MibTableColumn
radMepSpVlanId=_RadMepSpVlanId_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,18),_RadMepSpVlanId_Type())
radMepSpVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepSpVlanId.setStatus(_A)
class _RadMepCcInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('intervalInvalid',0),('interval300Hz',1),('interval10ms',2),('interval100ms',3),('interval1s',4),('interval10s',5),('interval1min',6),('interval10min',7)))
_RadMepCcInterval_Type.__name__=_H
_RadMepCcInterval_Object=MibTableColumn
radMepCcInterval=_RadMepCcInterval_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,19),_RadMepCcInterval_Type())
radMepCcInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepCcInterval.setStatus(_A)
_RadMepTransmitLbmDestMacAddress_Type=MacAddress
_RadMepTransmitLbmDestMacAddress_Object=MibTableColumn
radMepTransmitLbmDestMacAddress=_RadMepTransmitLbmDestMacAddress_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,20),_RadMepTransmitLbmDestMacAddress_Type())
radMepTransmitLbmDestMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepTransmitLbmDestMacAddress.setStatus(_A)
_RadMepTransmitLbmDestMepId_Type=Unsigned32
_RadMepTransmitLbmDestMepId_Object=MibTableColumn
radMepTransmitLbmDestMepId=_RadMepTransmitLbmDestMepId_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,21),_RadMepTransmitLbmDestMepId_Type())
radMepTransmitLbmDestMepId.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepTransmitLbmDestMepId.setStatus(_A)
class _RadMepTransmitLbmDestIsMepId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('no',2),(_t,3)))
_RadMepTransmitLbmDestIsMepId_Type.__name__=_H
_RadMepTransmitLbmDestIsMepId_Object=MibTableColumn
radMepTransmitLbmDestIsMepId=_RadMepTransmitLbmDestIsMepId_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,22),_RadMepTransmitLbmDestIsMepId_Type())
radMepTransmitLbmDestIsMepId.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepTransmitLbmDestIsMepId.setStatus(_A)
class _RadMepTransmitLbmMassages_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_RadMepTransmitLbmMassages_Type.__name__=_H
_RadMepTransmitLbmMassages_Object=MibTableColumn
radMepTransmitLbmMassages=_RadMepTransmitLbmMassages_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,23),_RadMepTransmitLbmMassages_Type())
radMepTransmitLbmMassages.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepTransmitLbmMassages.setStatus(_A)
class _RadMepTransmitLbmVlanPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RadMepTransmitLbmVlanPriority_Type.__name__=_J
_RadMepTransmitLbmVlanPriority_Object=MibTableColumn
radMepTransmitLbmVlanPriority=_RadMepTransmitLbmVlanPriority_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,24),_RadMepTransmitLbmVlanPriority_Type())
radMepTransmitLbmVlanPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepTransmitLbmVlanPriority.setStatus(_A)
class _RadMepTransmitLbmVlanDropEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('no',2),(_t,3)))
_RadMepTransmitLbmVlanDropEnable_Type.__name__=_H
_RadMepTransmitLbmVlanDropEnable_Object=MibTableColumn
radMepTransmitLbmVlanDropEnable=_RadMepTransmitLbmVlanDropEnable_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,25),_RadMepTransmitLbmVlanDropEnable_Type())
radMepTransmitLbmVlanDropEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepTransmitLbmVlanDropEnable.setStatus(_A)
_RadMepLbrIn_Type=Counter32
_RadMepLbrIn_Object=MibTableColumn
radMepLbrIn=_RadMepLbrIn_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,26),_RadMepLbrIn_Type())
radMepLbrIn.setMaxAccess(_B)
if mibBuilder.loadTexts:radMepLbrIn.setStatus(_A)
_RadMepLbrInOutOfOrder_Type=Counter32
_RadMepLbrInOutOfOrder_Object=MibTableColumn
radMepLbrInOutOfOrder=_RadMepLbrInOutOfOrder_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,27),_RadMepLbrInOutOfOrder_Type())
radMepLbrInOutOfOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:radMepLbrInOutOfOrder.setStatus(_A)
_RadMepLbmOut_Type=Counter32
_RadMepLbmOut_Object=MibTableColumn
radMepLbmOut=_RadMepLbmOut_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,28),_RadMepLbmOut_Type())
radMepLbmOut.setMaxAccess(_B)
if mibBuilder.loadTexts:radMepLbmOut.setStatus(_A)
_RadMepTransmitLtmTargetMacAddress_Type=MacAddress
_RadMepTransmitLtmTargetMacAddress_Object=MibTableColumn
radMepTransmitLtmTargetMacAddress=_RadMepTransmitLtmTargetMacAddress_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,29),_RadMepTransmitLtmTargetMacAddress_Type())
radMepTransmitLtmTargetMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepTransmitLtmTargetMacAddress.setStatus(_A)
_RadMepTransmitLtmTargetMepId_Type=Unsigned32
_RadMepTransmitLtmTargetMepId_Object=MibTableColumn
radMepTransmitLtmTargetMepId=_RadMepTransmitLtmTargetMepId_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,30),_RadMepTransmitLtmTargetMepId_Type())
radMepTransmitLtmTargetMepId.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepTransmitLtmTargetMepId.setStatus(_A)
class _RadMepTransmitLtmTargetIsMepId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('no',2),(_t,3)))
_RadMepTransmitLtmTargetIsMepId_Type.__name__=_H
_RadMepTransmitLtmTargetIsMepId_Object=MibTableColumn
radMepTransmitLtmTargetIsMepId=_RadMepTransmitLtmTargetIsMepId_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,31),_RadMepTransmitLtmTargetIsMepId_Type())
radMepTransmitLtmTargetIsMepId.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepTransmitLtmTargetIsMepId.setStatus(_A)
_RadMepTransmitLtmTtl_Type=Unsigned32
_RadMepTransmitLtmTtl_Object=MibTableColumn
radMepTransmitLtmTtl=_RadMepTransmitLtmTtl_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,32),_RadMepTransmitLtmTtl_Type())
radMepTransmitLtmTtl.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepTransmitLtmTtl.setStatus(_A)
class _RadMepTransmitLtmActivationCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_i,2),(_j,3)))
_RadMepTransmitLtmActivationCmd_Type.__name__=_H
_RadMepTransmitLtmActivationCmd_Object=MibTableColumn
radMepTransmitLtmActivationCmd=_RadMepTransmitLtmActivationCmd_Object((1,3,6,1,4,1,164,3,1,6,1,3,1,1,33),_RadMepTransmitLtmActivationCmd_Type())
radMepTransmitLtmActivationCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepTransmitLtmActivationCmd.setStatus(_A)
_EthOamService_ObjectIdentity=ObjectIdentity
ethOamService=_EthOamService_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,1,3,2))
_EthOamServiceTable_Object=MibTable
ethOamServiceTable=_EthOamServiceTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1))
if mibBuilder.loadTexts:ethOamServiceTable.setStatus(_A)
_EthOamServiceEntry_Object=MibTableRow
ethOamServiceEntry=_EthOamServiceEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1))
ethOamServiceEntry.setIndexNames((0,_E,_W),(0,_E,_b),(0,_E,_X),(0,_E,_d))
if mibBuilder.loadTexts:ethOamServiceEntry.setStatus(_A)
_EthOamServiceIdx_Type=Unsigned32
_EthOamServiceIdx_Object=MibTableColumn
ethOamServiceIdx=_EthOamServiceIdx_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,1),_EthOamServiceIdx_Type())
ethOamServiceIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:ethOamServiceIdx.setStatus(_A)
_EthOamServiceRowStatus_Type=RowStatus
_EthOamServiceRowStatus_Object=MibTableColumn
ethOamServiceRowStatus=_EthOamServiceRowStatus_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,2),_EthOamServiceRowStatus_Type())
ethOamServiceRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamServiceRowStatus.setStatus(_A)
class _EthOamServicePriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_EthOamServicePriority_Type.__name__=_J
_EthOamServicePriority_Object=MibTableColumn
ethOamServicePriority=_EthOamServicePriority_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,3),_EthOamServicePriority_Type())
ethOamServicePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamServicePriority.setStatus(_A)
class _EthOamServicePmEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_u,2),(_v,3)))
_EthOamServicePmEnable_Type.__name__=_H
_EthOamServicePmEnable_Object=MibTableColumn
ethOamServicePmEnable=_EthOamServicePmEnable_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,4),_EthOamServicePmEnable_Type())
ethOamServicePmEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamServicePmEnable.setStatus(_A)
class _EthOamServiceFrameLossRatioThresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,10))
_EthOamServiceFrameLossRatioThresh_Type.__name__=_H
_EthOamServiceFrameLossRatioThresh_Object=MibTableColumn
ethOamServiceFrameLossRatioThresh=_EthOamServiceFrameLossRatioThresh_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,5),_EthOamServiceFrameLossRatioThresh_Type())
ethOamServiceFrameLossRatioThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamServiceFrameLossRatioThresh.setStatus(_A)
class _EthOamServiceDelayThresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000000))
_EthOamServiceDelayThresh_Type.__name__=_H
_EthOamServiceDelayThresh_Object=MibTableColumn
ethOamServiceDelayThresh=_EthOamServiceDelayThresh_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,6),_EthOamServiceDelayThresh_Type())
ethOamServiceDelayThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamServiceDelayThresh.setStatus(_A)
class _EthOamServiceDelayVarThresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000000))
_EthOamServiceDelayVarThresh_Type.__name__=_H
_EthOamServiceDelayVarThresh_Object=MibTableColumn
ethOamServiceDelayVarThresh=_EthOamServiceDelayVarThresh_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,7),_EthOamServiceDelayVarThresh_Type())
ethOamServiceDelayVarThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamServiceDelayVarThresh.setStatus(_A)
class _EthOamServiceUnavailRatioThresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,10))
_EthOamServiceUnavailRatioThresh_Type.__name__=_H
_EthOamServiceUnavailRatioThresh_Object=MibTableColumn
ethOamServiceUnavailRatioThresh=_EthOamServiceUnavailRatioThresh_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,8),_EthOamServiceUnavailRatioThresh_Type())
ethOamServiceUnavailRatioThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamServiceUnavailRatioThresh.setStatus(_A)
_EthOamServiceTxFrames_Type=Counter32
_EthOamServiceTxFrames_Object=MibTableColumn
ethOamServiceTxFrames=_EthOamServiceTxFrames_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,9),_EthOamServiceTxFrames_Type())
ethOamServiceTxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceTxFrames.setStatus(_A)
_EthOamServiceOverflowTxFrames_Type=Counter32
_EthOamServiceOverflowTxFrames_Object=MibTableColumn
ethOamServiceOverflowTxFrames=_EthOamServiceOverflowTxFrames_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,10),_EthOamServiceOverflowTxFrames_Type())
ethOamServiceOverflowTxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceOverflowTxFrames.setStatus(_A)
_EthOamServiceFarEndFrameLoss_Type=Counter32
_EthOamServiceFarEndFrameLoss_Object=MibTableColumn
ethOamServiceFarEndFrameLoss=_EthOamServiceFarEndFrameLoss_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,11),_EthOamServiceFarEndFrameLoss_Type())
ethOamServiceFarEndFrameLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceFarEndFrameLoss.setStatus(_A)
_EthOamServiceOverflowFarEndFrameLoss_Type=Counter32
_EthOamServiceOverflowFarEndFrameLoss_Object=MibTableColumn
ethOamServiceOverflowFarEndFrameLoss=_EthOamServiceOverflowFarEndFrameLoss_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,12),_EthOamServiceOverflowFarEndFrameLoss_Type())
ethOamServiceOverflowFarEndFrameLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceOverflowFarEndFrameLoss.setStatus(_A)
_EthOamServiceFarEndFrameLossRatio_Type=Unsigned32
_EthOamServiceFarEndFrameLossRatio_Object=MibTableColumn
ethOamServiceFarEndFrameLossRatio=_EthOamServiceFarEndFrameLossRatio_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,13),_EthOamServiceFarEndFrameLossRatio_Type())
ethOamServiceFarEndFrameLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceFarEndFrameLossRatio.setStatus(_A)
_EthOamServiceElapsedTime_Type=Counter32
_EthOamServiceElapsedTime_Object=MibTableColumn
ethOamServiceElapsedTime=_EthOamServiceElapsedTime_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,14),_EthOamServiceElapsedTime_Type())
ethOamServiceElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceElapsedTime.setStatus(_A)
_EthOamServiceUnavailSec_Type=Counter32
_EthOamServiceUnavailSec_Object=MibTableColumn
ethOamServiceUnavailSec=_EthOamServiceUnavailSec_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,15),_EthOamServiceUnavailSec_Type())
ethOamServiceUnavailSec.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceUnavailSec.setStatus(_A)
_EthOamServiceUnavailRatio_Type=Unsigned32
_EthOamServiceUnavailRatio_Object=MibTableColumn
ethOamServiceUnavailRatio=_EthOamServiceUnavailRatio_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,16),_EthOamServiceUnavailRatio_Type())
ethOamServiceUnavailRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceUnavailRatio.setStatus(_A)
_EthOamServiceFramesAboveDelay_Type=Counter32
_EthOamServiceFramesAboveDelay_Object=MibTableColumn
ethOamServiceFramesAboveDelay=_EthOamServiceFramesAboveDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,17),_EthOamServiceFramesAboveDelay_Type())
ethOamServiceFramesAboveDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceFramesAboveDelay.setStatus(_A)
_EthOamServiceOverflowFramesAboveDelay_Type=Counter32
_EthOamServiceOverflowFramesAboveDelay_Object=MibTableColumn
ethOamServiceOverflowFramesAboveDelay=_EthOamServiceOverflowFramesAboveDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,18),_EthOamServiceOverflowFramesAboveDelay_Type())
ethOamServiceOverflowFramesAboveDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceOverflowFramesAboveDelay.setStatus(_A)
_EthOamServiceFramesAboveDelayVar_Type=Counter32
_EthOamServiceFramesAboveDelayVar_Object=MibTableColumn
ethOamServiceFramesAboveDelayVar=_EthOamServiceFramesAboveDelayVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,19),_EthOamServiceFramesAboveDelayVar_Type())
ethOamServiceFramesAboveDelayVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceFramesAboveDelayVar.setStatus(_A)
_EthOamServiceOverflowFramesAboveDelayVar_Type=Counter32
_EthOamServiceOverflowFramesAboveDelayVar_Object=MibTableColumn
ethOamServiceOverflowFramesAboveDelayVar=_EthOamServiceOverflowFramesAboveDelayVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,20),_EthOamServiceOverflowFramesAboveDelayVar_Type())
ethOamServiceOverflowFramesAboveDelayVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceOverflowFramesAboveDelayVar.setStatus(_A)
_EthOamServiceCurrentDelay_Type=Unsigned32
_EthOamServiceCurrentDelay_Object=MibTableColumn
ethOamServiceCurrentDelay=_EthOamServiceCurrentDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,21),_EthOamServiceCurrentDelay_Type())
ethOamServiceCurrentDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceCurrentDelay.setStatus(_A)
if mibBuilder.loadTexts:ethOamServiceCurrentDelay.setUnits(_G)
_EthOamServiceCurrentDelayVariation_Type=Unsigned32
_EthOamServiceCurrentDelayVariation_Object=MibTableColumn
ethOamServiceCurrentDelayVariation=_EthOamServiceCurrentDelayVariation_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,22),_EthOamServiceCurrentDelayVariation_Type())
ethOamServiceCurrentDelayVariation.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceCurrentDelayVariation.setStatus(_A)
if mibBuilder.loadTexts:ethOamServiceCurrentDelayVariation.setUnits(_G)
class _EthOamServiceResetCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_i,2),(_j,3)))
_EthOamServiceResetCounters_Type.__name__=_H
_EthOamServiceResetCounters_Object=MibTableColumn
ethOamServiceResetCounters=_EthOamServiceResetCounters_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,23),_EthOamServiceResetCounters_Type())
ethOamServiceResetCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamServiceResetCounters.setStatus(_A)
_EthOamServiceNearEndFrameLoss_Type=Counter32
_EthOamServiceNearEndFrameLoss_Object=MibTableColumn
ethOamServiceNearEndFrameLoss=_EthOamServiceNearEndFrameLoss_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,25),_EthOamServiceNearEndFrameLoss_Type())
ethOamServiceNearEndFrameLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceNearEndFrameLoss.setStatus(_A)
_EthOamServiceOverflowNearEndFrameLoss_Type=Counter32
_EthOamServiceOverflowNearEndFrameLoss_Object=MibTableColumn
ethOamServiceOverflowNearEndFrameLoss=_EthOamServiceOverflowNearEndFrameLoss_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,26),_EthOamServiceOverflowNearEndFrameLoss_Type())
ethOamServiceOverflowNearEndFrameLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceOverflowNearEndFrameLoss.setStatus(_A)
_EthOamServiceNearEndFrameLossRatio_Type=Unsigned32
_EthOamServiceNearEndFrameLossRatio_Object=MibTableColumn
ethOamServiceNearEndFrameLossRatio=_EthOamServiceNearEndFrameLossRatio_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,27),_EthOamServiceNearEndFrameLossRatio_Type())
ethOamServiceNearEndFrameLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceNearEndFrameLossRatio.setStatus(_A)
class _EthOamServiceDmmInterval_Type(Dot1agCfmCcmInterval):defaultValue=4
_EthOamServiceDmmInterval_Type.__name__=_k
_EthOamServiceDmmInterval_Object=MibTableColumn
ethOamServiceDmmInterval=_EthOamServiceDmmInterval_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,28),_EthOamServiceDmmInterval_Type())
ethOamServiceDmmInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamServiceDmmInterval.setStatus(_A)
class _EthOamServiceLmmInterval_Type(Dot1agCfmCcmInterval):defaultValue=4
_EthOamServiceLmmInterval_Type.__name__=_k
_EthOamServiceLmmInterval_Object=MibTableColumn
ethOamServiceLmmInterval=_EthOamServiceLmmInterval_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,29),_EthOamServiceLmmInterval_Type())
ethOamServiceLmmInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamServiceLmmInterval.setStatus(_A)
_EthOamServiceTxLmm_Type=Counter32
_EthOamServiceTxLmm_Object=MibTableColumn
ethOamServiceTxLmm=_EthOamServiceTxLmm_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,30),_EthOamServiceTxLmm_Type())
ethOamServiceTxLmm.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceTxLmm.setStatus(_A)
_EthOamServiceOverflowTxLmm_Type=Counter32
_EthOamServiceOverflowTxLmm_Object=MibTableColumn
ethOamServiceOverflowTxLmm=_EthOamServiceOverflowTxLmm_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,31),_EthOamServiceOverflowTxLmm_Type())
ethOamServiceOverflowTxLmm.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceOverflowTxLmm.setStatus(_A)
_EthOamServiceTxDmm_Type=Counter32
_EthOamServiceTxDmm_Object=MibTableColumn
ethOamServiceTxDmm=_EthOamServiceTxDmm_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,32),_EthOamServiceTxDmm_Type())
ethOamServiceTxDmm.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceTxDmm.setStatus(_A)
_EthOamServiceOverflowTxDmm_Type=Counter32
_EthOamServiceOverflowTxDmm_Object=MibTableColumn
ethOamServiceOverflowTxDmm=_EthOamServiceOverflowTxDmm_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,33),_EthOamServiceOverflowTxDmm_Type())
ethOamServiceOverflowTxDmm.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceOverflowTxDmm.setStatus(_A)
_EthOamServiceRxLmr_Type=Counter32
_EthOamServiceRxLmr_Object=MibTableColumn
ethOamServiceRxLmr=_EthOamServiceRxLmr_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,34),_EthOamServiceRxLmr_Type())
ethOamServiceRxLmr.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceRxLmr.setStatus(_A)
_EthOamServiceOverflowRxLmr_Type=Counter32
_EthOamServiceOverflowRxLmr_Object=MibTableColumn
ethOamServiceOverflowRxLmr=_EthOamServiceOverflowRxLmr_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,35),_EthOamServiceOverflowRxLmr_Type())
ethOamServiceOverflowRxLmr.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceOverflowRxLmr.setStatus(_A)
_EthOamServiceRxDmr_Type=Counter32
_EthOamServiceRxDmr_Object=MibTableColumn
ethOamServiceRxDmr=_EthOamServiceRxDmr_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,36),_EthOamServiceRxDmr_Type())
ethOamServiceRxDmr.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceRxDmr.setStatus(_A)
_EthOamServiceOverflowRxDmr_Type=Counter32
_EthOamServiceOverflowRxDmr_Object=MibTableColumn
ethOamServiceOverflowRxDmr=_EthOamServiceOverflowRxDmr_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,37),_EthOamServiceOverflowRxDmr_Type())
ethOamServiceOverflowRxDmr.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceOverflowRxDmr.setStatus(_A)
_EthOamServiceTxForward_Type=Counter32
_EthOamServiceTxForward_Object=MibTableColumn
ethOamServiceTxForward=_EthOamServiceTxForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,38),_EthOamServiceTxForward_Type())
ethOamServiceTxForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceTxForward.setStatus(_A)
_EthOamServiceOverflowTxForward_Type=Counter32
_EthOamServiceOverflowTxForward_Object=MibTableColumn
ethOamServiceOverflowTxForward=_EthOamServiceOverflowTxForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,39),_EthOamServiceOverflowTxForward_Type())
ethOamServiceOverflowTxForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceOverflowTxForward.setStatus(_A)
_EthOamServiceRxForward_Type=Counter32
_EthOamServiceRxForward_Object=MibTableColumn
ethOamServiceRxForward=_EthOamServiceRxForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,40),_EthOamServiceRxForward_Type())
ethOamServiceRxForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceRxForward.setStatus(_A)
_EthOamServiceOverflowRxForward_Type=Counter32
_EthOamServiceOverflowRxForward_Object=MibTableColumn
ethOamServiceOverflowRxForward=_EthOamServiceOverflowRxForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,41),_EthOamServiceOverflowRxForward_Type())
ethOamServiceOverflowRxForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceOverflowRxForward.setStatus(_A)
_EthOamServiceTxBackward_Type=Counter32
_EthOamServiceTxBackward_Object=MibTableColumn
ethOamServiceTxBackward=_EthOamServiceTxBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,42),_EthOamServiceTxBackward_Type())
ethOamServiceTxBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceTxBackward.setStatus(_A)
_EthOamServiceOverflowTxBackward_Type=Counter32
_EthOamServiceOverflowTxBackward_Object=MibTableColumn
ethOamServiceOverflowTxBackward=_EthOamServiceOverflowTxBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,43),_EthOamServiceOverflowTxBackward_Type())
ethOamServiceOverflowTxBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceOverflowTxBackward.setStatus(_A)
_EthOamServiceRxBackward_Type=Counter32
_EthOamServiceRxBackward_Object=MibTableColumn
ethOamServiceRxBackward=_EthOamServiceRxBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,44),_EthOamServiceRxBackward_Type())
ethOamServiceRxBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceRxBackward.setStatus(_A)
_EthOamServiceOverflowRxBackward_Type=Counter32
_EthOamServiceOverflowRxBackward_Object=MibTableColumn
ethOamServiceOverflowRxBackward=_EthOamServiceOverflowRxBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,45),_EthOamServiceOverflowRxBackward_Type())
ethOamServiceOverflowRxBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceOverflowRxBackward.setStatus(_A)
_EthOamServiceConvertedIndex_Type=Unsigned32
_EthOamServiceConvertedIndex_Object=MibTableColumn
ethOamServiceConvertedIndex=_EthOamServiceConvertedIndex_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,1,1,46),_EthOamServiceConvertedIndex_Type())
ethOamServiceConvertedIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamServiceConvertedIndex.setStatus(_A)
_EthOamSvcCurrentStatTable_Object=MibTable
ethOamSvcCurrentStatTable=_EthOamSvcCurrentStatTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2))
if mibBuilder.loadTexts:ethOamSvcCurrentStatTable.setStatus(_A)
_EthOamSvcCurrentStatEntry_Object=MibTableRow
ethOamSvcCurrentStatEntry=_EthOamSvcCurrentStatEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1))
ethOamSvcCurrentStatEntry.setIndexNames((0,_E,_W),(0,_E,_b),(0,_E,_X),(0,_E,_d))
if mibBuilder.loadTexts:ethOamSvcCurrentStatEntry.setStatus(_A)
_EthOamSvcCurrFramesAboveDelayThresh_Type=PerfCurrentCount
_EthOamSvcCurrFramesAboveDelayThresh_Object=MibTableColumn
ethOamSvcCurrFramesAboveDelayThresh=_EthOamSvcCurrFramesAboveDelayThresh_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,1),_EthOamSvcCurrFramesAboveDelayThresh_Type())
ethOamSvcCurrFramesAboveDelayThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrFramesAboveDelayThresh.setStatus(_A)
_EthOamSvcCurrFramesBelowDelayThresh_Type=PerfCurrentCount
_EthOamSvcCurrFramesBelowDelayThresh_Object=MibTableColumn
ethOamSvcCurrFramesBelowDelayThresh=_EthOamSvcCurrFramesBelowDelayThresh_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,2),_EthOamSvcCurrFramesBelowDelayThresh_Type())
ethOamSvcCurrFramesBelowDelayThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrFramesBelowDelayThresh.setStatus(_A)
_EthOamSvcCurrFramesAboveDVarThresh_Type=PerfCurrentCount
_EthOamSvcCurrFramesAboveDVarThresh_Object=MibTableColumn
ethOamSvcCurrFramesAboveDVarThresh=_EthOamSvcCurrFramesAboveDVarThresh_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,3),_EthOamSvcCurrFramesAboveDVarThresh_Type())
ethOamSvcCurrFramesAboveDVarThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrFramesAboveDVarThresh.setStatus(_A)
_EthOamSvcCurrFramesBelowDVarThresh_Type=PerfCurrentCount
_EthOamSvcCurrFramesBelowDVarThresh_Object=MibTableColumn
ethOamSvcCurrFramesBelowDVarThresh=_EthOamSvcCurrFramesBelowDVarThresh_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,4),_EthOamSvcCurrFramesBelowDVarThresh_Type())
ethOamSvcCurrFramesBelowDVarThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrFramesBelowDVarThresh.setStatus(_A)
_EthOamSvcCurrFramesTxCounter_Type=PerfCurrentCount
_EthOamSvcCurrFramesTxCounter_Object=MibTableColumn
ethOamSvcCurrFramesTxCounter=_EthOamSvcCurrFramesTxCounter_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,5),_EthOamSvcCurrFramesTxCounter_Type())
ethOamSvcCurrFramesTxCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrFramesTxCounter.setStatus(_A)
_EthOamSvcCurrFarEndFramesLossCounter_Type=PerfCurrentCount
_EthOamSvcCurrFarEndFramesLossCounter_Object=MibTableColumn
ethOamSvcCurrFarEndFramesLossCounter=_EthOamSvcCurrFarEndFramesLossCounter_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,6),_EthOamSvcCurrFarEndFramesLossCounter_Type())
ethOamSvcCurrFarEndFramesLossCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrFarEndFramesLossCounter.setStatus(_A)
_EthOamSvcCurrMinRoundTripDelay_Type=Unsigned32
_EthOamSvcCurrMinRoundTripDelay_Object=MibTableColumn
ethOamSvcCurrMinRoundTripDelay=_EthOamSvcCurrMinRoundTripDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,7),_EthOamSvcCurrMinRoundTripDelay_Type())
ethOamSvcCurrMinRoundTripDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrMinRoundTripDelay.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcCurrMinRoundTripDelay.setUnits(_G)
_EthOamSvcCurrMaxRoundTripDelay_Type=Unsigned32
_EthOamSvcCurrMaxRoundTripDelay_Object=MibTableColumn
ethOamSvcCurrMaxRoundTripDelay=_EthOamSvcCurrMaxRoundTripDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,8),_EthOamSvcCurrMaxRoundTripDelay_Type())
ethOamSvcCurrMaxRoundTripDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrMaxRoundTripDelay.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcCurrMaxRoundTripDelay.setUnits(_G)
_EthOamSvcCurrAvgRoundTripDelay_Type=Unsigned32
_EthOamSvcCurrAvgRoundTripDelay_Object=MibTableColumn
ethOamSvcCurrAvgRoundTripDelay=_EthOamSvcCurrAvgRoundTripDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,9),_EthOamSvcCurrAvgRoundTripDelay_Type())
ethOamSvcCurrAvgRoundTripDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrAvgRoundTripDelay.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcCurrAvgRoundTripDelay.setUnits(_G)
_EthOamSvcCurrMaxRoundTripDVar_Type=Unsigned32
_EthOamSvcCurrMaxRoundTripDVar_Object=MibTableColumn
ethOamSvcCurrMaxRoundTripDVar=_EthOamSvcCurrMaxRoundTripDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,10),_EthOamSvcCurrMaxRoundTripDVar_Type())
ethOamSvcCurrMaxRoundTripDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrMaxRoundTripDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcCurrMaxRoundTripDVar.setUnits(_G)
_EthOamSvcCurrAvgRoundTripDVar_Type=Unsigned32
_EthOamSvcCurrAvgRoundTripDVar_Object=MibTableColumn
ethOamSvcCurrAvgRoundTripDVar=_EthOamSvcCurrAvgRoundTripDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,11),_EthOamSvcCurrAvgRoundTripDVar_Type())
ethOamSvcCurrAvgRoundTripDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrAvgRoundTripDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcCurrAvgRoundTripDVar.setUnits(_G)
class _EthOamSvcCurrElapsedTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_EthOamSvcCurrElapsedTime_Type.__name__=_H
_EthOamSvcCurrElapsedTime_Object=MibTableColumn
ethOamSvcCurrElapsedTime=_EthOamSvcCurrElapsedTime_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,12),_EthOamSvcCurrElapsedTime_Type())
ethOamSvcCurrElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrElapsedTime.setStatus(_A)
_EthOamSvcCurrUnavailSec_Type=PerfCurrentCount
_EthOamSvcCurrUnavailSec_Object=MibTableColumn
ethOamSvcCurrUnavailSec=_EthOamSvcCurrUnavailSec_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,13),_EthOamSvcCurrUnavailSec_Type())
ethOamSvcCurrUnavailSec.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrUnavailSec.setStatus(_A)
_EthOamSvcCurrLmmTxFrames_Type=PerfCurrentCount
_EthOamSvcCurrLmmTxFrames_Object=MibTableColumn
ethOamSvcCurrLmmTxFrames=_EthOamSvcCurrLmmTxFrames_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,14),_EthOamSvcCurrLmmTxFrames_Type())
ethOamSvcCurrLmmTxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrLmmTxFrames.setStatus(_A)
_EthOamSvcCurrDmmTxFrames_Type=PerfCurrentCount
_EthOamSvcCurrDmmTxFrames_Object=MibTableColumn
ethOamSvcCurrDmmTxFrames=_EthOamSvcCurrDmmTxFrames_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,16),_EthOamSvcCurrDmmTxFrames_Type())
ethOamSvcCurrDmmTxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrDmmTxFrames.setStatus(_A)
_EthOamSvcCurrLmrRxFrames_Type=PerfCurrentCount
_EthOamSvcCurrLmrRxFrames_Object=MibTableColumn
ethOamSvcCurrLmrRxFrames=_EthOamSvcCurrLmrRxFrames_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,19),_EthOamSvcCurrLmrRxFrames_Type())
ethOamSvcCurrLmrRxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrLmrRxFrames.setStatus(_A)
_EthOamSvcCurrDmrRxFrames_Type=PerfCurrentCount
_EthOamSvcCurrDmrRxFrames_Object=MibTableColumn
ethOamSvcCurrDmrRxFrames=_EthOamSvcCurrDmrRxFrames_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,21),_EthOamSvcCurrDmrRxFrames_Type())
ethOamSvcCurrDmrRxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrDmrRxFrames.setStatus(_A)
_EthOamSvcCurrNearEndFramesLossCounter_Type=PerfCurrentCount
_EthOamSvcCurrNearEndFramesLossCounter_Object=MibTableColumn
ethOamSvcCurrNearEndFramesLossCounter=_EthOamSvcCurrNearEndFramesLossCounter_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,22),_EthOamSvcCurrNearEndFramesLossCounter_Type())
ethOamSvcCurrNearEndFramesLossCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrNearEndFramesLossCounter.setStatus(_A)
_EthOamSvcCurrTxFramesForward_Type=PerfCurrentCount
_EthOamSvcCurrTxFramesForward_Object=MibTableColumn
ethOamSvcCurrTxFramesForward=_EthOamSvcCurrTxFramesForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,23),_EthOamSvcCurrTxFramesForward_Type())
ethOamSvcCurrTxFramesForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrTxFramesForward.setStatus(_A)
_EthOamSvcCurrRxFramesForward_Type=PerfCurrentCount
_EthOamSvcCurrRxFramesForward_Object=MibTableColumn
ethOamSvcCurrRxFramesForward=_EthOamSvcCurrRxFramesForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,24),_EthOamSvcCurrRxFramesForward_Type())
ethOamSvcCurrRxFramesForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrRxFramesForward.setStatus(_A)
_EthOamSvcCurrTxFramesBackward_Type=PerfCurrentCount
_EthOamSvcCurrTxFramesBackward_Object=MibTableColumn
ethOamSvcCurrTxFramesBackward=_EthOamSvcCurrTxFramesBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,25),_EthOamSvcCurrTxFramesBackward_Type())
ethOamSvcCurrTxFramesBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrTxFramesBackward.setStatus(_A)
_EthOamSvcCurrRxFramesBackward_Type=PerfCurrentCount
_EthOamSvcCurrRxFramesBackward_Object=MibTableColumn
ethOamSvcCurrRxFramesBackward=_EthOamSvcCurrRxFramesBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,26),_EthOamSvcCurrRxFramesBackward_Type())
ethOamSvcCurrRxFramesBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrRxFramesBackward.setStatus(_A)
_EthOamSvcCurrUnavailableIndForward_Type=PerfCurrentCount
_EthOamSvcCurrUnavailableIndForward_Object=MibTableColumn
ethOamSvcCurrUnavailableIndForward=_EthOamSvcCurrUnavailableIndForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,27),_EthOamSvcCurrUnavailableIndForward_Type())
ethOamSvcCurrUnavailableIndForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrUnavailableIndForward.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcCurrUnavailableIndForward.setUnits(_S)
_EthOamSvcCurrUnavailableIndBackward_Type=PerfCurrentCount
_EthOamSvcCurrUnavailableIndBackward_Object=MibTableColumn
ethOamSvcCurrUnavailableIndBackward=_EthOamSvcCurrUnavailableIndBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,28),_EthOamSvcCurrUnavailableIndBackward_Type())
ethOamSvcCurrUnavailableIndBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrUnavailableIndBackward.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcCurrUnavailableIndBackward.setUnits(_S)
_EthOamSvcCurrNearEndFrameLossRatio_Type=PerfCurrentCount
_EthOamSvcCurrNearEndFrameLossRatio_Object=MibTableColumn
ethOamSvcCurrNearEndFrameLossRatio=_EthOamSvcCurrNearEndFrameLossRatio_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,29),_EthOamSvcCurrNearEndFrameLossRatio_Type())
ethOamSvcCurrNearEndFrameLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrNearEndFrameLossRatio.setStatus(_A)
_EthOamSvcCurrFarEndFrameLossRatio_Type=PerfCurrentCount
_EthOamSvcCurrFarEndFrameLossRatio_Object=MibTableColumn
ethOamSvcCurrFarEndFrameLossRatio=_EthOamSvcCurrFarEndFrameLossRatio_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,30),_EthOamSvcCurrFarEndFrameLossRatio_Type())
ethOamSvcCurrFarEndFrameLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrFarEndFrameLossRatio.setStatus(_A)
_EthOamSvcCurrMinRoundTripDVar_Type=Unsigned32
_EthOamSvcCurrMinRoundTripDVar_Object=MibTableColumn
ethOamSvcCurrMinRoundTripDVar=_EthOamSvcCurrMinRoundTripDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,31),_EthOamSvcCurrMinRoundTripDVar_Type())
ethOamSvcCurrMinRoundTripDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrMinRoundTripDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcCurrMinRoundTripDVar.setUnits(_G)
_EthOamSvcCurrMinForwardDelay_Type=Unsigned32
_EthOamSvcCurrMinForwardDelay_Object=MibTableColumn
ethOamSvcCurrMinForwardDelay=_EthOamSvcCurrMinForwardDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,32),_EthOamSvcCurrMinForwardDelay_Type())
ethOamSvcCurrMinForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrMinForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcCurrMinForwardDelay.setUnits(_G)
_EthOamSvcCurrMaxForwardDelay_Type=Unsigned32
_EthOamSvcCurrMaxForwardDelay_Object=MibTableColumn
ethOamSvcCurrMaxForwardDelay=_EthOamSvcCurrMaxForwardDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,33),_EthOamSvcCurrMaxForwardDelay_Type())
ethOamSvcCurrMaxForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrMaxForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcCurrMaxForwardDelay.setUnits(_G)
_EthOamSvcCurrAvgForwardDelay_Type=Unsigned32
_EthOamSvcCurrAvgForwardDelay_Object=MibTableColumn
ethOamSvcCurrAvgForwardDelay=_EthOamSvcCurrAvgForwardDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,34),_EthOamSvcCurrAvgForwardDelay_Type())
ethOamSvcCurrAvgForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrAvgForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcCurrAvgForwardDelay.setUnits(_G)
_EthOamSvcCurrMinForwardDVar_Type=Unsigned32
_EthOamSvcCurrMinForwardDVar_Object=MibTableColumn
ethOamSvcCurrMinForwardDVar=_EthOamSvcCurrMinForwardDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,35),_EthOamSvcCurrMinForwardDVar_Type())
ethOamSvcCurrMinForwardDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrMinForwardDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcCurrMinForwardDVar.setUnits(_G)
_EthOamSvcCurrMaxForwardDVar_Type=Unsigned32
_EthOamSvcCurrMaxForwardDVar_Object=MibTableColumn
ethOamSvcCurrMaxForwardDVar=_EthOamSvcCurrMaxForwardDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,36),_EthOamSvcCurrMaxForwardDVar_Type())
ethOamSvcCurrMaxForwardDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrMaxForwardDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcCurrMaxForwardDVar.setUnits(_G)
_EthOamSvcCurrAvgForwardDVar_Type=Unsigned32
_EthOamSvcCurrAvgForwardDVar_Object=MibTableColumn
ethOamSvcCurrAvgForwardDVar=_EthOamSvcCurrAvgForwardDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,37),_EthOamSvcCurrAvgForwardDVar_Type())
ethOamSvcCurrAvgForwardDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrAvgForwardDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcCurrAvgForwardDVar.setUnits(_G)
_EthOamSvcCurrMinBackwardDVar_Type=Unsigned32
_EthOamSvcCurrMinBackwardDVar_Object=MibTableColumn
ethOamSvcCurrMinBackwardDVar=_EthOamSvcCurrMinBackwardDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,38),_EthOamSvcCurrMinBackwardDVar_Type())
ethOamSvcCurrMinBackwardDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrMinBackwardDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcCurrMinBackwardDVar.setUnits(_G)
_EthOamSvcCurrMaxBackwardDVar_Type=Unsigned32
_EthOamSvcCurrMaxBackwardDVar_Object=MibTableColumn
ethOamSvcCurrMaxBackwardDVar=_EthOamSvcCurrMaxBackwardDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,39),_EthOamSvcCurrMaxBackwardDVar_Type())
ethOamSvcCurrMaxBackwardDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrMaxBackwardDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcCurrMaxBackwardDVar.setUnits(_G)
_EthOamSvcCurrAvgBackwardDVar_Type=Unsigned32
_EthOamSvcCurrAvgBackwardDVar_Object=MibTableColumn
ethOamSvcCurrAvgBackwardDVar=_EthOamSvcCurrAvgBackwardDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,40),_EthOamSvcCurrAvgBackwardDVar_Type())
ethOamSvcCurrAvgBackwardDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrAvgBackwardDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcCurrAvgBackwardDVar.setUnits(_G)
_EthOamSvcCurrAvailableIndForward_Type=PerfCurrentCount
_EthOamSvcCurrAvailableIndForward_Object=MibTableColumn
ethOamSvcCurrAvailableIndForward=_EthOamSvcCurrAvailableIndForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,41),_EthOamSvcCurrAvailableIndForward_Type())
ethOamSvcCurrAvailableIndForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrAvailableIndForward.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcCurrAvailableIndForward.setUnits(_S)
_EthOamSvcCurrAvailableIndBackward_Type=PerfCurrentCount
_EthOamSvcCurrAvailableIndBackward_Object=MibTableColumn
ethOamSvcCurrAvailableIndBackward=_EthOamSvcCurrAvailableIndBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,2,1,42),_EthOamSvcCurrAvailableIndBackward_Type())
ethOamSvcCurrAvailableIndBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcCurrAvailableIndBackward.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcCurrAvailableIndBackward.setUnits(_S)
_EthOamSvcIntervalTable_Object=MibTable
ethOamSvcIntervalTable=_EthOamSvcIntervalTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3))
if mibBuilder.loadTexts:ethOamSvcIntervalTable.setStatus(_A)
_EthOamSvcIntervalEntry_Object=MibTableRow
ethOamSvcIntervalEntry=_EthOamSvcIntervalEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1))
ethOamSvcIntervalEntry.setIndexNames((0,_E,_W),(0,_E,_b),(0,_E,_X),(0,_E,_d),(0,_E,_w))
if mibBuilder.loadTexts:ethOamSvcIntervalEntry.setStatus(_A)
class _EthOamSvcIntervalNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_EthOamSvcIntervalNum_Type.__name__=_H
_EthOamSvcIntervalNum_Object=MibTableColumn
ethOamSvcIntervalNum=_EthOamSvcIntervalNum_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,1),_EthOamSvcIntervalNum_Type())
ethOamSvcIntervalNum.setMaxAccess(_I)
if mibBuilder.loadTexts:ethOamSvcIntervalNum.setStatus(_A)
_EthOamSvcIntervalFramesAboveDelayThresh_Type=PerfIntervalCount
_EthOamSvcIntervalFramesAboveDelayThresh_Object=MibTableColumn
ethOamSvcIntervalFramesAboveDelayThresh=_EthOamSvcIntervalFramesAboveDelayThresh_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,2),_EthOamSvcIntervalFramesAboveDelayThresh_Type())
ethOamSvcIntervalFramesAboveDelayThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalFramesAboveDelayThresh.setStatus(_A)
_EthOamSvcIntervalFramesBelowDelayThresh_Type=PerfIntervalCount
_EthOamSvcIntervalFramesBelowDelayThresh_Object=MibTableColumn
ethOamSvcIntervalFramesBelowDelayThresh=_EthOamSvcIntervalFramesBelowDelayThresh_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,3),_EthOamSvcIntervalFramesBelowDelayThresh_Type())
ethOamSvcIntervalFramesBelowDelayThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalFramesBelowDelayThresh.setStatus(_A)
_EthOamSvcIntervalFramesAboveDVarThresh_Type=PerfIntervalCount
_EthOamSvcIntervalFramesAboveDVarThresh_Object=MibTableColumn
ethOamSvcIntervalFramesAboveDVarThresh=_EthOamSvcIntervalFramesAboveDVarThresh_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,4),_EthOamSvcIntervalFramesAboveDVarThresh_Type())
ethOamSvcIntervalFramesAboveDVarThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalFramesAboveDVarThresh.setStatus(_A)
_EthOamSvcIntervalFramesBelowDVarThresh_Type=PerfIntervalCount
_EthOamSvcIntervalFramesBelowDVarThresh_Object=MibTableColumn
ethOamSvcIntervalFramesBelowDVarThresh=_EthOamSvcIntervalFramesBelowDVarThresh_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,5),_EthOamSvcIntervalFramesBelowDVarThresh_Type())
ethOamSvcIntervalFramesBelowDVarThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalFramesBelowDVarThresh.setStatus(_A)
_EthOamSvcIntervalFramesTxCounter_Type=PerfIntervalCount
_EthOamSvcIntervalFramesTxCounter_Object=MibTableColumn
ethOamSvcIntervalFramesTxCounter=_EthOamSvcIntervalFramesTxCounter_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,6),_EthOamSvcIntervalFramesTxCounter_Type())
ethOamSvcIntervalFramesTxCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalFramesTxCounter.setStatus(_A)
_EthOamSvcIntervalFarEndFramesLossCounter_Type=PerfIntervalCount
_EthOamSvcIntervalFarEndFramesLossCounter_Object=MibTableColumn
ethOamSvcIntervalFarEndFramesLossCounter=_EthOamSvcIntervalFarEndFramesLossCounter_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,7),_EthOamSvcIntervalFarEndFramesLossCounter_Type())
ethOamSvcIntervalFarEndFramesLossCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalFarEndFramesLossCounter.setStatus(_A)
_EthOamSvcIntervalMinRoundTripDelay_Type=Unsigned32
_EthOamSvcIntervalMinRoundTripDelay_Object=MibTableColumn
ethOamSvcIntervalMinRoundTripDelay=_EthOamSvcIntervalMinRoundTripDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,8),_EthOamSvcIntervalMinRoundTripDelay_Type())
ethOamSvcIntervalMinRoundTripDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalMinRoundTripDelay.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcIntervalMinRoundTripDelay.setUnits(_G)
_EthOamSvcIntervalMaxRoundTripDelay_Type=Unsigned32
_EthOamSvcIntervalMaxRoundTripDelay_Object=MibTableColumn
ethOamSvcIntervalMaxRoundTripDelay=_EthOamSvcIntervalMaxRoundTripDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,9),_EthOamSvcIntervalMaxRoundTripDelay_Type())
ethOamSvcIntervalMaxRoundTripDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalMaxRoundTripDelay.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcIntervalMaxRoundTripDelay.setUnits(_G)
_EthOamSvcIntervalAvgRoundTripDelay_Type=Unsigned32
_EthOamSvcIntervalAvgRoundTripDelay_Object=MibTableColumn
ethOamSvcIntervalAvgRoundTripDelay=_EthOamSvcIntervalAvgRoundTripDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,10),_EthOamSvcIntervalAvgRoundTripDelay_Type())
ethOamSvcIntervalAvgRoundTripDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalAvgRoundTripDelay.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcIntervalAvgRoundTripDelay.setUnits(_G)
_EthOamSvcIntervalMaxRoundTripDVar_Type=Unsigned32
_EthOamSvcIntervalMaxRoundTripDVar_Object=MibTableColumn
ethOamSvcIntervalMaxRoundTripDVar=_EthOamSvcIntervalMaxRoundTripDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,11),_EthOamSvcIntervalMaxRoundTripDVar_Type())
ethOamSvcIntervalMaxRoundTripDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalMaxRoundTripDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcIntervalMaxRoundTripDVar.setUnits(_G)
_EthOamSvcIntervalAvgRoundTripDVar_Type=Unsigned32
_EthOamSvcIntervalAvgRoundTripDVar_Object=MibTableColumn
ethOamSvcIntervalAvgRoundTripDVar=_EthOamSvcIntervalAvgRoundTripDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,12),_EthOamSvcIntervalAvgRoundTripDVar_Type())
ethOamSvcIntervalAvgRoundTripDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalAvgRoundTripDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcIntervalAvgRoundTripDVar.setUnits(_G)
_EthOamSvcIntervalUnavailSec_Type=PerfIntervalCount
_EthOamSvcIntervalUnavailSec_Object=MibTableColumn
ethOamSvcIntervalUnavailSec=_EthOamSvcIntervalUnavailSec_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,13),_EthOamSvcIntervalUnavailSec_Type())
ethOamSvcIntervalUnavailSec.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalUnavailSec.setStatus(_A)
_EthOamSvcIntervalLmmTxFrames_Type=PerfIntervalCount
_EthOamSvcIntervalLmmTxFrames_Object=MibTableColumn
ethOamSvcIntervalLmmTxFrames=_EthOamSvcIntervalLmmTxFrames_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,14),_EthOamSvcIntervalLmmTxFrames_Type())
ethOamSvcIntervalLmmTxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalLmmTxFrames.setStatus(_A)
_EthOamSvcIntervalDmmTxFrames_Type=PerfIntervalCount
_EthOamSvcIntervalDmmTxFrames_Object=MibTableColumn
ethOamSvcIntervalDmmTxFrames=_EthOamSvcIntervalDmmTxFrames_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,16),_EthOamSvcIntervalDmmTxFrames_Type())
ethOamSvcIntervalDmmTxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalDmmTxFrames.setStatus(_A)
_EthOamSvcIntervalLmrRxFrames_Type=PerfIntervalCount
_EthOamSvcIntervalLmrRxFrames_Object=MibTableColumn
ethOamSvcIntervalLmrRxFrames=_EthOamSvcIntervalLmrRxFrames_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,19),_EthOamSvcIntervalLmrRxFrames_Type())
ethOamSvcIntervalLmrRxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalLmrRxFrames.setStatus(_A)
_EthOamSvcIntervalDmrRxFrames_Type=PerfIntervalCount
_EthOamSvcIntervalDmrRxFrames_Object=MibTableColumn
ethOamSvcIntervalDmrRxFrames=_EthOamSvcIntervalDmrRxFrames_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,21),_EthOamSvcIntervalDmrRxFrames_Type())
ethOamSvcIntervalDmrRxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalDmrRxFrames.setStatus(_A)
_EthOamSvcIntervalNearEndFramesLossCounter_Type=PerfIntervalCount
_EthOamSvcIntervalNearEndFramesLossCounter_Object=MibTableColumn
ethOamSvcIntervalNearEndFramesLossCounter=_EthOamSvcIntervalNearEndFramesLossCounter_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,22),_EthOamSvcIntervalNearEndFramesLossCounter_Type())
ethOamSvcIntervalNearEndFramesLossCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalNearEndFramesLossCounter.setStatus(_A)
_EthOamSvcIntervalTxFramesForward_Type=PerfIntervalCount
_EthOamSvcIntervalTxFramesForward_Object=MibTableColumn
ethOamSvcIntervalTxFramesForward=_EthOamSvcIntervalTxFramesForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,23),_EthOamSvcIntervalTxFramesForward_Type())
ethOamSvcIntervalTxFramesForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalTxFramesForward.setStatus(_A)
_EthOamSvcIntervalRxFramesForward_Type=PerfIntervalCount
_EthOamSvcIntervalRxFramesForward_Object=MibTableColumn
ethOamSvcIntervalRxFramesForward=_EthOamSvcIntervalRxFramesForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,24),_EthOamSvcIntervalRxFramesForward_Type())
ethOamSvcIntervalRxFramesForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalRxFramesForward.setStatus(_A)
_EthOamSvcIntervalTxFramesBackward_Type=PerfIntervalCount
_EthOamSvcIntervalTxFramesBackward_Object=MibTableColumn
ethOamSvcIntervalTxFramesBackward=_EthOamSvcIntervalTxFramesBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,25),_EthOamSvcIntervalTxFramesBackward_Type())
ethOamSvcIntervalTxFramesBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalTxFramesBackward.setStatus(_A)
_EthOamSvcIntervalRxFramesBackward_Type=PerfIntervalCount
_EthOamSvcIntervalRxFramesBackward_Object=MibTableColumn
ethOamSvcIntervalRxFramesBackward=_EthOamSvcIntervalRxFramesBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,26),_EthOamSvcIntervalRxFramesBackward_Type())
ethOamSvcIntervalRxFramesBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalRxFramesBackward.setStatus(_A)
_EthOamSvcIntervalUnavailableIndForward_Type=PerfIntervalCount
_EthOamSvcIntervalUnavailableIndForward_Object=MibTableColumn
ethOamSvcIntervalUnavailableIndForward=_EthOamSvcIntervalUnavailableIndForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,27),_EthOamSvcIntervalUnavailableIndForward_Type())
ethOamSvcIntervalUnavailableIndForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalUnavailableIndForward.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcIntervalUnavailableIndForward.setUnits(_S)
_EthOamSvcIntervalUnavailableIndBackward_Type=PerfIntervalCount
_EthOamSvcIntervalUnavailableIndBackward_Object=MibTableColumn
ethOamSvcIntervalUnavailableIndBackward=_EthOamSvcIntervalUnavailableIndBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,28),_EthOamSvcIntervalUnavailableIndBackward_Type())
ethOamSvcIntervalUnavailableIndBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalUnavailableIndBackward.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcIntervalUnavailableIndBackward.setUnits(_S)
_EthOamSvcIntervalNearEndFrameLossRatio_Type=PerfIntervalCount
_EthOamSvcIntervalNearEndFrameLossRatio_Object=MibTableColumn
ethOamSvcIntervalNearEndFrameLossRatio=_EthOamSvcIntervalNearEndFrameLossRatio_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,29),_EthOamSvcIntervalNearEndFrameLossRatio_Type())
ethOamSvcIntervalNearEndFrameLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalNearEndFrameLossRatio.setStatus(_A)
_EthOamSvcIntervalFarEndFrameLossRatio_Type=PerfIntervalCount
_EthOamSvcIntervalFarEndFrameLossRatio_Object=MibTableColumn
ethOamSvcIntervalFarEndFrameLossRatio=_EthOamSvcIntervalFarEndFrameLossRatio_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,30),_EthOamSvcIntervalFarEndFrameLossRatio_Type())
ethOamSvcIntervalFarEndFrameLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalFarEndFrameLossRatio.setStatus(_A)
_EthOamSvcIntervalValidData_Type=TruthValue
_EthOamSvcIntervalValidData_Object=MibTableColumn
ethOamSvcIntervalValidData=_EthOamSvcIntervalValidData_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,31),_EthOamSvcIntervalValidData_Type())
ethOamSvcIntervalValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalValidData.setStatus(_A)
class _EthOamSvcIntervalDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,900))
_EthOamSvcIntervalDuration_Type.__name__=_H
_EthOamSvcIntervalDuration_Object=MibTableColumn
ethOamSvcIntervalDuration=_EthOamSvcIntervalDuration_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,32),_EthOamSvcIntervalDuration_Type())
ethOamSvcIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalDuration.setStatus(_A)
_EthOamSvcIntervalTimeStamp_Type=DateAndTime
_EthOamSvcIntervalTimeStamp_Object=MibTableColumn
ethOamSvcIntervalTimeStamp=_EthOamSvcIntervalTimeStamp_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,33),_EthOamSvcIntervalTimeStamp_Type())
ethOamSvcIntervalTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalTimeStamp.setStatus(_A)
_EthOamSvcIntervalMinRoundTripDVar_Type=Unsigned32
_EthOamSvcIntervalMinRoundTripDVar_Object=MibTableColumn
ethOamSvcIntervalMinRoundTripDVar=_EthOamSvcIntervalMinRoundTripDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,34),_EthOamSvcIntervalMinRoundTripDVar_Type())
ethOamSvcIntervalMinRoundTripDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalMinRoundTripDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcIntervalMinRoundTripDVar.setUnits(_G)
_EthOamSvcIntervalMinForwardDelay_Type=Unsigned32
_EthOamSvcIntervalMinForwardDelay_Object=MibTableColumn
ethOamSvcIntervalMinForwardDelay=_EthOamSvcIntervalMinForwardDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,35),_EthOamSvcIntervalMinForwardDelay_Type())
ethOamSvcIntervalMinForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalMinForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcIntervalMinForwardDelay.setUnits(_G)
_EthOamSvcIntervalMaxForwardDelay_Type=Unsigned32
_EthOamSvcIntervalMaxForwardDelay_Object=MibTableColumn
ethOamSvcIntervalMaxForwardDelay=_EthOamSvcIntervalMaxForwardDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,36),_EthOamSvcIntervalMaxForwardDelay_Type())
ethOamSvcIntervalMaxForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalMaxForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcIntervalMaxForwardDelay.setUnits(_G)
_EthOamSvcIntervalAvgForwardDelay_Type=Unsigned32
_EthOamSvcIntervalAvgForwardDelay_Object=MibTableColumn
ethOamSvcIntervalAvgForwardDelay=_EthOamSvcIntervalAvgForwardDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,37),_EthOamSvcIntervalAvgForwardDelay_Type())
ethOamSvcIntervalAvgForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalAvgForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcIntervalAvgForwardDelay.setUnits(_G)
_EthOamSvcIntervalMinForwardDVar_Type=Unsigned32
_EthOamSvcIntervalMinForwardDVar_Object=MibTableColumn
ethOamSvcIntervalMinForwardDVar=_EthOamSvcIntervalMinForwardDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,38),_EthOamSvcIntervalMinForwardDVar_Type())
ethOamSvcIntervalMinForwardDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalMinForwardDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcIntervalMinForwardDVar.setUnits(_G)
_EthOamSvcIntervalMaxForwardDVar_Type=Unsigned32
_EthOamSvcIntervalMaxForwardDVar_Object=MibTableColumn
ethOamSvcIntervalMaxForwardDVar=_EthOamSvcIntervalMaxForwardDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,39),_EthOamSvcIntervalMaxForwardDVar_Type())
ethOamSvcIntervalMaxForwardDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalMaxForwardDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcIntervalMaxForwardDVar.setUnits(_G)
_EthOamSvcIntervalAvgForwardDVar_Type=Unsigned32
_EthOamSvcIntervalAvgForwardDVar_Object=MibTableColumn
ethOamSvcIntervalAvgForwardDVar=_EthOamSvcIntervalAvgForwardDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,40),_EthOamSvcIntervalAvgForwardDVar_Type())
ethOamSvcIntervalAvgForwardDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalAvgForwardDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcIntervalAvgForwardDVar.setUnits(_G)
_EthOamSvcIntervalMinBackwardDVar_Type=Unsigned32
_EthOamSvcIntervalMinBackwardDVar_Object=MibTableColumn
ethOamSvcIntervalMinBackwardDVar=_EthOamSvcIntervalMinBackwardDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,41),_EthOamSvcIntervalMinBackwardDVar_Type())
ethOamSvcIntervalMinBackwardDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalMinBackwardDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcIntervalMinBackwardDVar.setUnits(_G)
_EthOamSvcIntervalMaxBackwardDVar_Type=Unsigned32
_EthOamSvcIntervalMaxBackwardDVar_Object=MibTableColumn
ethOamSvcIntervalMaxBackwardDVar=_EthOamSvcIntervalMaxBackwardDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,42),_EthOamSvcIntervalMaxBackwardDVar_Type())
ethOamSvcIntervalMaxBackwardDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalMaxBackwardDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcIntervalMaxBackwardDVar.setUnits(_G)
_EthOamSvcIntervalAvgBackwardDVar_Type=Unsigned32
_EthOamSvcIntervalAvgBackwardDVar_Object=MibTableColumn
ethOamSvcIntervalAvgBackwardDVar=_EthOamSvcIntervalAvgBackwardDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,43),_EthOamSvcIntervalAvgBackwardDVar_Type())
ethOamSvcIntervalAvgBackwardDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalAvgBackwardDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcIntervalAvgBackwardDVar.setUnits(_G)
_EthOamSvcIntervalAvailableIndForward_Type=PerfIntervalCount
_EthOamSvcIntervalAvailableIndForward_Object=MibTableColumn
ethOamSvcIntervalAvailableIndForward=_EthOamSvcIntervalAvailableIndForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,44),_EthOamSvcIntervalAvailableIndForward_Type())
ethOamSvcIntervalAvailableIndForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalAvailableIndForward.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcIntervalAvailableIndForward.setUnits(_S)
_EthOamSvcIntervalAvailableIndBackward_Type=PerfIntervalCount
_EthOamSvcIntervalAvailableIndBackward_Object=MibTableColumn
ethOamSvcIntervalAvailableIndBackward=_EthOamSvcIntervalAvailableIndBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,3,1,45),_EthOamSvcIntervalAvailableIndBackward_Type())
ethOamSvcIntervalAvailableIndBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcIntervalAvailableIndBackward.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcIntervalAvailableIndBackward.setUnits(_S)
_EthOamSvcTotalTable_Object=MibTable
ethOamSvcTotalTable=_EthOamSvcTotalTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4))
if mibBuilder.loadTexts:ethOamSvcTotalTable.setStatus(_A)
_EthOamSvcTotalEntry_Object=MibTableRow
ethOamSvcTotalEntry=_EthOamSvcTotalEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1))
ethOamSvcTotalEntry.setIndexNames((0,_E,_W),(0,_E,_b),(0,_E,_X),(0,_E,_d))
if mibBuilder.loadTexts:ethOamSvcTotalEntry.setStatus(_A)
_EthOamSvcTotalFramesAboveDelayThresh_Type=PerfTotalCount
_EthOamSvcTotalFramesAboveDelayThresh_Object=MibTableColumn
ethOamSvcTotalFramesAboveDelayThresh=_EthOamSvcTotalFramesAboveDelayThresh_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,1),_EthOamSvcTotalFramesAboveDelayThresh_Type())
ethOamSvcTotalFramesAboveDelayThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalFramesAboveDelayThresh.setStatus(_A)
_EthOamSvcTotalFramesBelowDelayThresh_Type=PerfTotalCount
_EthOamSvcTotalFramesBelowDelayThresh_Object=MibTableColumn
ethOamSvcTotalFramesBelowDelayThresh=_EthOamSvcTotalFramesBelowDelayThresh_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,2),_EthOamSvcTotalFramesBelowDelayThresh_Type())
ethOamSvcTotalFramesBelowDelayThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalFramesBelowDelayThresh.setStatus(_A)
_EthOamSvcTotalFramesAboveDVarThresh_Type=PerfTotalCount
_EthOamSvcTotalFramesAboveDVarThresh_Object=MibTableColumn
ethOamSvcTotalFramesAboveDVarThresh=_EthOamSvcTotalFramesAboveDVarThresh_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,3),_EthOamSvcTotalFramesAboveDVarThresh_Type())
ethOamSvcTotalFramesAboveDVarThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalFramesAboveDVarThresh.setStatus(_A)
_EthOamSvcTotalFramesBelowDVarThresh_Type=PerfTotalCount
_EthOamSvcTotalFramesBelowDVarThresh_Object=MibTableColumn
ethOamSvcTotalFramesBelowDVarThresh=_EthOamSvcTotalFramesBelowDVarThresh_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,4),_EthOamSvcTotalFramesBelowDVarThresh_Type())
ethOamSvcTotalFramesBelowDVarThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalFramesBelowDVarThresh.setStatus(_A)
_EthOamSvcTotalFramesTxCounter_Type=PerfTotalCount
_EthOamSvcTotalFramesTxCounter_Object=MibTableColumn
ethOamSvcTotalFramesTxCounter=_EthOamSvcTotalFramesTxCounter_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,5),_EthOamSvcTotalFramesTxCounter_Type())
ethOamSvcTotalFramesTxCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalFramesTxCounter.setStatus(_A)
_EthOamSvcTotalFarEndFramesLossCounter_Type=PerfTotalCount
_EthOamSvcTotalFarEndFramesLossCounter_Object=MibTableColumn
ethOamSvcTotalFarEndFramesLossCounter=_EthOamSvcTotalFarEndFramesLossCounter_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,6),_EthOamSvcTotalFarEndFramesLossCounter_Type())
ethOamSvcTotalFarEndFramesLossCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalFarEndFramesLossCounter.setStatus(_A)
_EthOamSvcTotalMinRoundTripDelay_Type=Unsigned32
_EthOamSvcTotalMinRoundTripDelay_Object=MibTableColumn
ethOamSvcTotalMinRoundTripDelay=_EthOamSvcTotalMinRoundTripDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,7),_EthOamSvcTotalMinRoundTripDelay_Type())
ethOamSvcTotalMinRoundTripDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalMinRoundTripDelay.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcTotalMinRoundTripDelay.setUnits(_G)
_EthOamSvcTotalMaxRoundTripDelay_Type=Unsigned32
_EthOamSvcTotalMaxRoundTripDelay_Object=MibTableColumn
ethOamSvcTotalMaxRoundTripDelay=_EthOamSvcTotalMaxRoundTripDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,8),_EthOamSvcTotalMaxRoundTripDelay_Type())
ethOamSvcTotalMaxRoundTripDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalMaxRoundTripDelay.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcTotalMaxRoundTripDelay.setUnits(_G)
_EthOamSvcTotalAvgRoundTripDelay_Type=Unsigned32
_EthOamSvcTotalAvgRoundTripDelay_Object=MibTableColumn
ethOamSvcTotalAvgRoundTripDelay=_EthOamSvcTotalAvgRoundTripDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,9),_EthOamSvcTotalAvgRoundTripDelay_Type())
ethOamSvcTotalAvgRoundTripDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalAvgRoundTripDelay.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcTotalAvgRoundTripDelay.setUnits(_G)
_EthOamSvcTotalMaxRoundTripDVar_Type=Unsigned32
_EthOamSvcTotalMaxRoundTripDVar_Object=MibTableColumn
ethOamSvcTotalMaxRoundTripDVar=_EthOamSvcTotalMaxRoundTripDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,10),_EthOamSvcTotalMaxRoundTripDVar_Type())
ethOamSvcTotalMaxRoundTripDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalMaxRoundTripDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcTotalMaxRoundTripDVar.setUnits(_G)
_EthOamSvcTotalAvgRoundTripDVar_Type=Unsigned32
_EthOamSvcTotalAvgRoundTripDVar_Object=MibTableColumn
ethOamSvcTotalAvgRoundTripDVar=_EthOamSvcTotalAvgRoundTripDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,11),_EthOamSvcTotalAvgRoundTripDVar_Type())
ethOamSvcTotalAvgRoundTripDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalAvgRoundTripDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcTotalAvgRoundTripDVar.setUnits(_G)
_EthOamSvcTotalUnavailSec_Type=PerfTotalCount
_EthOamSvcTotalUnavailSec_Object=MibTableColumn
ethOamSvcTotalUnavailSec=_EthOamSvcTotalUnavailSec_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,12),_EthOamSvcTotalUnavailSec_Type())
ethOamSvcTotalUnavailSec.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalUnavailSec.setStatus(_A)
_EthOamSvcTotalLmmTxFrames_Type=PerfTotalCount
_EthOamSvcTotalLmmTxFrames_Object=MibTableColumn
ethOamSvcTotalLmmTxFrames=_EthOamSvcTotalLmmTxFrames_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,13),_EthOamSvcTotalLmmTxFrames_Type())
ethOamSvcTotalLmmTxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalLmmTxFrames.setStatus(_A)
_EthOamSvcTotalDmmTxFrames_Type=PerfTotalCount
_EthOamSvcTotalDmmTxFrames_Object=MibTableColumn
ethOamSvcTotalDmmTxFrames=_EthOamSvcTotalDmmTxFrames_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,15),_EthOamSvcTotalDmmTxFrames_Type())
ethOamSvcTotalDmmTxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalDmmTxFrames.setStatus(_A)
_EthOamSvcTotalLmrRxFrames_Type=PerfTotalCount
_EthOamSvcTotalLmrRxFrames_Object=MibTableColumn
ethOamSvcTotalLmrRxFrames=_EthOamSvcTotalLmrRxFrames_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,18),_EthOamSvcTotalLmrRxFrames_Type())
ethOamSvcTotalLmrRxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalLmrRxFrames.setStatus(_A)
_EthOamSvcTotalDmrRxFrames_Type=PerfTotalCount
_EthOamSvcTotalDmrRxFrames_Object=MibTableColumn
ethOamSvcTotalDmrRxFrames=_EthOamSvcTotalDmrRxFrames_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,20),_EthOamSvcTotalDmrRxFrames_Type())
ethOamSvcTotalDmrRxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalDmrRxFrames.setStatus(_A)
_EthOamSvcTotalNearEndFramesLossCounter_Type=PerfTotalCount
_EthOamSvcTotalNearEndFramesLossCounter_Object=MibTableColumn
ethOamSvcTotalNearEndFramesLossCounter=_EthOamSvcTotalNearEndFramesLossCounter_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,21),_EthOamSvcTotalNearEndFramesLossCounter_Type())
ethOamSvcTotalNearEndFramesLossCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalNearEndFramesLossCounter.setStatus(_A)
_EthOamSvcTotalTxFramesForward_Type=PerfTotalCount
_EthOamSvcTotalTxFramesForward_Object=MibTableColumn
ethOamSvcTotalTxFramesForward=_EthOamSvcTotalTxFramesForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,22),_EthOamSvcTotalTxFramesForward_Type())
ethOamSvcTotalTxFramesForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalTxFramesForward.setStatus(_A)
_EthOamSvcTotalRxFramesForward_Type=PerfTotalCount
_EthOamSvcTotalRxFramesForward_Object=MibTableColumn
ethOamSvcTotalRxFramesForward=_EthOamSvcTotalRxFramesForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,23),_EthOamSvcTotalRxFramesForward_Type())
ethOamSvcTotalRxFramesForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalRxFramesForward.setStatus(_A)
_EthOamSvcTotalTxFramesBackward_Type=PerfTotalCount
_EthOamSvcTotalTxFramesBackward_Object=MibTableColumn
ethOamSvcTotalTxFramesBackward=_EthOamSvcTotalTxFramesBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,24),_EthOamSvcTotalTxFramesBackward_Type())
ethOamSvcTotalTxFramesBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalTxFramesBackward.setStatus(_A)
_EthOamSvcTotalRxFramesBackward_Type=PerfTotalCount
_EthOamSvcTotalRxFramesBackward_Object=MibTableColumn
ethOamSvcTotalRxFramesBackward=_EthOamSvcTotalRxFramesBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,25),_EthOamSvcTotalRxFramesBackward_Type())
ethOamSvcTotalRxFramesBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalRxFramesBackward.setStatus(_A)
_EthOamSvcTotalUnavailableIndForward_Type=PerfTotalCount
_EthOamSvcTotalUnavailableIndForward_Object=MibTableColumn
ethOamSvcTotalUnavailableIndForward=_EthOamSvcTotalUnavailableIndForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,26),_EthOamSvcTotalUnavailableIndForward_Type())
ethOamSvcTotalUnavailableIndForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalUnavailableIndForward.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcTotalUnavailableIndForward.setUnits(_S)
_EthOamSvcTotalUnavailableIndBackward_Type=PerfTotalCount
_EthOamSvcTotalUnavailableIndBackward_Object=MibTableColumn
ethOamSvcTotalUnavailableIndBackward=_EthOamSvcTotalUnavailableIndBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,27),_EthOamSvcTotalUnavailableIndBackward_Type())
ethOamSvcTotalUnavailableIndBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalUnavailableIndBackward.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcTotalUnavailableIndBackward.setUnits(_S)
_EthOamSvcTotalMinRoundTripDVar_Type=Unsigned32
_EthOamSvcTotalMinRoundTripDVar_Object=MibTableColumn
ethOamSvcTotalMinRoundTripDVar=_EthOamSvcTotalMinRoundTripDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,29),_EthOamSvcTotalMinRoundTripDVar_Type())
ethOamSvcTotalMinRoundTripDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalMinRoundTripDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcTotalMinRoundTripDVar.setUnits(_G)
_EthOamSvcTotalMinForwardDelay_Type=Unsigned32
_EthOamSvcTotalMinForwardDelay_Object=MibTableColumn
ethOamSvcTotalMinForwardDelay=_EthOamSvcTotalMinForwardDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,30),_EthOamSvcTotalMinForwardDelay_Type())
ethOamSvcTotalMinForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalMinForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcTotalMinForwardDelay.setUnits(_G)
_EthOamSvcTotalMaxForwardDelay_Type=Unsigned32
_EthOamSvcTotalMaxForwardDelay_Object=MibTableColumn
ethOamSvcTotalMaxForwardDelay=_EthOamSvcTotalMaxForwardDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,31),_EthOamSvcTotalMaxForwardDelay_Type())
ethOamSvcTotalMaxForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalMaxForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcTotalMaxForwardDelay.setUnits(_G)
_EthOamSvcTotalAvgForwardDelay_Type=Unsigned32
_EthOamSvcTotalAvgForwardDelay_Object=MibTableColumn
ethOamSvcTotalAvgForwardDelay=_EthOamSvcTotalAvgForwardDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,32),_EthOamSvcTotalAvgForwardDelay_Type())
ethOamSvcTotalAvgForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalAvgForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcTotalAvgForwardDelay.setUnits(_G)
_EthOamSvcTotalMinForwardDVar_Type=Unsigned32
_EthOamSvcTotalMinForwardDVar_Object=MibTableColumn
ethOamSvcTotalMinForwardDVar=_EthOamSvcTotalMinForwardDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,33),_EthOamSvcTotalMinForwardDVar_Type())
ethOamSvcTotalMinForwardDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalMinForwardDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcTotalMinForwardDVar.setUnits(_G)
_EthOamSvcTotalMaxForwardDVar_Type=Unsigned32
_EthOamSvcTotalMaxForwardDVar_Object=MibTableColumn
ethOamSvcTotalMaxForwardDVar=_EthOamSvcTotalMaxForwardDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,34),_EthOamSvcTotalMaxForwardDVar_Type())
ethOamSvcTotalMaxForwardDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalMaxForwardDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcTotalMaxForwardDVar.setUnits(_G)
_EthOamSvcTotalAvgForwardDVar_Type=Unsigned32
_EthOamSvcTotalAvgForwardDVar_Object=MibTableColumn
ethOamSvcTotalAvgForwardDVar=_EthOamSvcTotalAvgForwardDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,35),_EthOamSvcTotalAvgForwardDVar_Type())
ethOamSvcTotalAvgForwardDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalAvgForwardDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcTotalAvgForwardDVar.setUnits(_G)
_EthOamSvcTotalMinBackwardDVar_Type=Unsigned32
_EthOamSvcTotalMinBackwardDVar_Object=MibTableColumn
ethOamSvcTotalMinBackwardDVar=_EthOamSvcTotalMinBackwardDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,36),_EthOamSvcTotalMinBackwardDVar_Type())
ethOamSvcTotalMinBackwardDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalMinBackwardDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcTotalMinBackwardDVar.setUnits(_G)
_EthOamSvcTotalMaxBackwardDVar_Type=Unsigned32
_EthOamSvcTotalMaxBackwardDVar_Object=MibTableColumn
ethOamSvcTotalMaxBackwardDVar=_EthOamSvcTotalMaxBackwardDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,37),_EthOamSvcTotalMaxBackwardDVar_Type())
ethOamSvcTotalMaxBackwardDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalMaxBackwardDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcTotalMaxBackwardDVar.setUnits(_G)
_EthOamSvcTotalAvgBackwardDVar_Type=Unsigned32
_EthOamSvcTotalAvgBackwardDVar_Object=MibTableColumn
ethOamSvcTotalAvgBackwardDVar=_EthOamSvcTotalAvgBackwardDVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,38),_EthOamSvcTotalAvgBackwardDVar_Type())
ethOamSvcTotalAvgBackwardDVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalAvgBackwardDVar.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcTotalAvgBackwardDVar.setUnits(_G)
_EthOamSvcTotalForwardFrameLossRatio_Type=PerfTotalCount
_EthOamSvcTotalForwardFrameLossRatio_Object=MibTableColumn
ethOamSvcTotalForwardFrameLossRatio=_EthOamSvcTotalForwardFrameLossRatio_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,39),_EthOamSvcTotalForwardFrameLossRatio_Type())
ethOamSvcTotalForwardFrameLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalForwardFrameLossRatio.setStatus(_A)
_EthOamSvcTotalBackwardFrameLossRatio_Type=PerfTotalCount
_EthOamSvcTotalBackwardFrameLossRatio_Object=MibTableColumn
ethOamSvcTotalBackwardFrameLossRatio=_EthOamSvcTotalBackwardFrameLossRatio_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,40),_EthOamSvcTotalBackwardFrameLossRatio_Type())
ethOamSvcTotalBackwardFrameLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalBackwardFrameLossRatio.setStatus(_A)
_EthOamSvcTotalAvailableIndForward_Type=Counter32
_EthOamSvcTotalAvailableIndForward_Object=MibTableColumn
ethOamSvcTotalAvailableIndForward=_EthOamSvcTotalAvailableIndForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,41),_EthOamSvcTotalAvailableIndForward_Type())
ethOamSvcTotalAvailableIndForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalAvailableIndForward.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcTotalAvailableIndForward.setUnits(_S)
_EthOamSvcTotalAvailableIndBackward_Type=Counter32
_EthOamSvcTotalAvailableIndBackward_Object=MibTableColumn
ethOamSvcTotalAvailableIndBackward=_EthOamSvcTotalAvailableIndBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,4,1,42),_EthOamSvcTotalAvailableIndBackward_Type())
ethOamSvcTotalAvailableIndBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamSvcTotalAvailableIndBackward.setStatus(_A)
if mibBuilder.loadTexts:ethOamSvcTotalAvailableIndBackward.setUnits(_S)
_EthOamDestNeTable_Object=MibTable
ethOamDestNeTable=_EthOamDestNeTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5))
if mibBuilder.loadTexts:ethOamDestNeTable.setStatus(_A)
_EthOamDestNeEntry_Object=MibTableRow
ethOamDestNeEntry=_EthOamDestNeEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1))
ethOamDestNeEntry.setIndexNames((0,_E,_W),(0,_E,_b),(0,_E,_X),(0,_E,_d),(0,_E,_A3))
if mibBuilder.loadTexts:ethOamDestNeEntry.setStatus(_A)
class _EthOamDestNeIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_EthOamDestNeIdx_Type.__name__=_J
_EthOamDestNeIdx_Object=MibTableColumn
ethOamDestNeIdx=_EthOamDestNeIdx_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,1),_EthOamDestNeIdx_Type())
ethOamDestNeIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:ethOamDestNeIdx.setStatus(_A)
_EthOamDestNeRowStatus_Type=RowStatus
_EthOamDestNeRowStatus_Object=MibTableColumn
ethOamDestNeRowStatus=_EthOamDestNeRowStatus_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,2),_EthOamDestNeRowStatus_Type())
ethOamDestNeRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamDestNeRowStatus.setStatus(_A)
_EthOamDestNePmDestAddr_Type=MacAddress
_EthOamDestNePmDestAddr_Object=MibTableColumn
ethOamDestNePmDestAddr=_EthOamDestNePmDestAddr_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,3),_EthOamDestNePmDestAddr_Type())
ethOamDestNePmDestAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamDestNePmDestAddr.setStatus(_A)
_EthOamDestNePmRemoteMepId_Type=Unsigned32
_EthOamDestNePmRemoteMepId_Object=MibTableColumn
ethOamDestNePmRemoteMepId=_EthOamDestNePmRemoteMepId_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,4),_EthOamDestNePmRemoteMepId_Type())
ethOamDestNePmRemoteMepId.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamDestNePmRemoteMepId.setStatus(_A)
class _EthOamDestNePmActivity_Type(Bits):namedValues=NamedValues(*(('singleEndedLoss',0),('dualEndedLoss',1),('oneWayDelay',2),('twoWayDelay',3)))
_EthOamDestNePmActivity_Type.__name__=_g
_EthOamDestNePmActivity_Object=MibTableColumn
ethOamDestNePmActivity=_EthOamDestNePmActivity_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,5),_EthOamDestNePmActivity_Type())
ethOamDestNePmActivity.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamDestNePmActivity.setStatus(_Z)
_EthOamDestNeTxFrames_Type=Counter32
_EthOamDestNeTxFrames_Object=MibTableColumn
ethOamDestNeTxFrames=_EthOamDestNeTxFrames_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,6),_EthOamDestNeTxFrames_Type())
ethOamDestNeTxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeTxFrames.setStatus(_A)
_EthOamDestNeOverflowTxFrames_Type=Counter32
_EthOamDestNeOverflowTxFrames_Object=MibTableColumn
ethOamDestNeOverflowTxFrames=_EthOamDestNeOverflowTxFrames_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,7),_EthOamDestNeOverflowTxFrames_Type())
ethOamDestNeOverflowTxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeOverflowTxFrames.setStatus(_A)
_EthOamDestNeTxLmm_Type=Counter32
_EthOamDestNeTxLmm_Object=MibTableColumn
ethOamDestNeTxLmm=_EthOamDestNeTxLmm_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,8),_EthOamDestNeTxLmm_Type())
ethOamDestNeTxLmm.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeTxLmm.setStatus(_A)
_EthOamDestNeOverflowTxLmm_Type=Counter32
_EthOamDestNeOverflowTxLmm_Object=MibTableColumn
ethOamDestNeOverflowTxLmm=_EthOamDestNeOverflowTxLmm_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,9),_EthOamDestNeOverflowTxLmm_Type())
ethOamDestNeOverflowTxLmm.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeOverflowTxLmm.setStatus(_A)
_EthOamDestNeTxDmm_Type=Counter32
_EthOamDestNeTxDmm_Object=MibTableColumn
ethOamDestNeTxDmm=_EthOamDestNeTxDmm_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,12),_EthOamDestNeTxDmm_Type())
ethOamDestNeTxDmm.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeTxDmm.setStatus(_A)
_EthOamDestNeOverflowTxDmm_Type=Counter32
_EthOamDestNeOverflowTxDmm_Object=MibTableColumn
ethOamDestNeOverflowTxDmm=_EthOamDestNeOverflowTxDmm_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,13),_EthOamDestNeOverflowTxDmm_Type())
ethOamDestNeOverflowTxDmm.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeOverflowTxDmm.setStatus(_A)
_EthOamDestNeRxLmr_Type=Counter32
_EthOamDestNeRxLmr_Object=MibTableColumn
ethOamDestNeRxLmr=_EthOamDestNeRxLmr_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,18),_EthOamDestNeRxLmr_Type())
ethOamDestNeRxLmr.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeRxLmr.setStatus(_A)
_EthOamDestNeOverflowRxLmr_Type=Counter32
_EthOamDestNeOverflowRxLmr_Object=MibTableColumn
ethOamDestNeOverflowRxLmr=_EthOamDestNeOverflowRxLmr_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,19),_EthOamDestNeOverflowRxLmr_Type())
ethOamDestNeOverflowRxLmr.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeOverflowRxLmr.setStatus(_A)
_EthOamDestNeRxDmr_Type=Counter32
_EthOamDestNeRxDmr_Object=MibTableColumn
ethOamDestNeRxDmr=_EthOamDestNeRxDmr_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,22),_EthOamDestNeRxDmr_Type())
ethOamDestNeRxDmr.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeRxDmr.setStatus(_A)
_EthOamDestNeOverflowRxDmr_Type=Counter32
_EthOamDestNeOverflowRxDmr_Object=MibTableColumn
ethOamDestNeOverflowRxDmr=_EthOamDestNeOverflowRxDmr_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,23),_EthOamDestNeOverflowRxDmr_Type())
ethOamDestNeOverflowRxDmr.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeOverflowRxDmr.setStatus(_A)
_EthOamDestNeFarEndFrameLoss_Type=Counter32
_EthOamDestNeFarEndFrameLoss_Object=MibTableColumn
ethOamDestNeFarEndFrameLoss=_EthOamDestNeFarEndFrameLoss_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,24),_EthOamDestNeFarEndFrameLoss_Type())
ethOamDestNeFarEndFrameLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeFarEndFrameLoss.setStatus(_A)
_EthOamDestNeOverflowFarEndFrameLoss_Type=Counter32
_EthOamDestNeOverflowFarEndFrameLoss_Object=MibTableColumn
ethOamDestNeOverflowFarEndFrameLoss=_EthOamDestNeOverflowFarEndFrameLoss_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,25),_EthOamDestNeOverflowFarEndFrameLoss_Type())
ethOamDestNeOverflowFarEndFrameLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeOverflowFarEndFrameLoss.setStatus(_A)
_EthOamDestNeFarEndFrameLossRatio_Type=Unsigned32
_EthOamDestNeFarEndFrameLossRatio_Object=MibTableColumn
ethOamDestNeFarEndFrameLossRatio=_EthOamDestNeFarEndFrameLossRatio_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,26),_EthOamDestNeFarEndFrameLossRatio_Type())
ethOamDestNeFarEndFrameLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeFarEndFrameLossRatio.setStatus(_A)
_EthOamDestNeTimeElapsed_Type=Unsigned32
_EthOamDestNeTimeElapsed_Object=MibTableColumn
ethOamDestNeTimeElapsed=_EthOamDestNeTimeElapsed_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,27),_EthOamDestNeTimeElapsed_Type())
ethOamDestNeTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeTimeElapsed.setStatus(_A)
_EthOamDestNeFramesAboveDelay_Type=Counter32
_EthOamDestNeFramesAboveDelay_Object=MibTableColumn
ethOamDestNeFramesAboveDelay=_EthOamDestNeFramesAboveDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,30),_EthOamDestNeFramesAboveDelay_Type())
ethOamDestNeFramesAboveDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeFramesAboveDelay.setStatus(_A)
_EthOamDestNeOverflowFramesAboveDelay_Type=Counter32
_EthOamDestNeOverflowFramesAboveDelay_Object=MibTableColumn
ethOamDestNeOverflowFramesAboveDelay=_EthOamDestNeOverflowFramesAboveDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,31),_EthOamDestNeOverflowFramesAboveDelay_Type())
ethOamDestNeOverflowFramesAboveDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeOverflowFramesAboveDelay.setStatus(_A)
_EthOamDestNeFramesAboveDelayVar_Type=Counter32
_EthOamDestNeFramesAboveDelayVar_Object=MibTableColumn
ethOamDestNeFramesAboveDelayVar=_EthOamDestNeFramesAboveDelayVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,32),_EthOamDestNeFramesAboveDelayVar_Type())
ethOamDestNeFramesAboveDelayVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeFramesAboveDelayVar.setStatus(_A)
_EthOamDestNeOverflowFramesAboveDelayVar_Type=Counter32
_EthOamDestNeOverflowFramesAboveDelayVar_Object=MibTableColumn
ethOamDestNeOverflowFramesAboveDelayVar=_EthOamDestNeOverflowFramesAboveDelayVar_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,33),_EthOamDestNeOverflowFramesAboveDelayVar_Type())
ethOamDestNeOverflowFramesAboveDelayVar.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeOverflowFramesAboveDelayVar.setStatus(_A)
_EthOamDestNeCurrentDelay_Type=Unsigned32
_EthOamDestNeCurrentDelay_Object=MibTableColumn
ethOamDestNeCurrentDelay=_EthOamDestNeCurrentDelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,34),_EthOamDestNeCurrentDelay_Type())
ethOamDestNeCurrentDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeCurrentDelay.setStatus(_A)
if mibBuilder.loadTexts:ethOamDestNeCurrentDelay.setUnits(_G)
_EthOamDestNeCurrentDelayVariation_Type=Unsigned32
_EthOamDestNeCurrentDelayVariation_Object=MibTableColumn
ethOamDestNeCurrentDelayVariation=_EthOamDestNeCurrentDelayVariation_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,35),_EthOamDestNeCurrentDelayVariation_Type())
ethOamDestNeCurrentDelayVariation.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeCurrentDelayVariation.setStatus(_A)
if mibBuilder.loadTexts:ethOamDestNeCurrentDelayVariation.setUnits(_G)
class _EthOamDestNeResetCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_i,2),(_j,3)))
_EthOamDestNeResetCounters_Type.__name__=_H
_EthOamDestNeResetCounters_Object=MibTableColumn
ethOamDestNeResetCounters=_EthOamDestNeResetCounters_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,36),_EthOamDestNeResetCounters_Type())
ethOamDestNeResetCounters.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamDestNeResetCounters.setStatus(_A)
_EthOamDestNeNearEndFrameLoss_Type=Counter32
_EthOamDestNeNearEndFrameLoss_Object=MibTableColumn
ethOamDestNeNearEndFrameLoss=_EthOamDestNeNearEndFrameLoss_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,37),_EthOamDestNeNearEndFrameLoss_Type())
ethOamDestNeNearEndFrameLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeNearEndFrameLoss.setStatus(_A)
_EthOamDestNeOverflowNearEndFrameLoss_Type=Counter32
_EthOamDestNeOverflowNearEndFrameLoss_Object=MibTableColumn
ethOamDestNeOverflowNearEndFrameLoss=_EthOamDestNeOverflowNearEndFrameLoss_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,38),_EthOamDestNeOverflowNearEndFrameLoss_Type())
ethOamDestNeOverflowNearEndFrameLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeOverflowNearEndFrameLoss.setStatus(_A)
_EthOamDestNeNearEndFrameLossRatio_Type=Unsigned32
_EthOamDestNeNearEndFrameLossRatio_Object=MibTableColumn
ethOamDestNeNearEndFrameLossRatio=_EthOamDestNeNearEndFrameLossRatio_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,39),_EthOamDestNeNearEndFrameLossRatio_Type())
ethOamDestNeNearEndFrameLossRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeNearEndFrameLossRatio.setStatus(_A)
class _EthOamDestNeLmmTraffic_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,255)));namedValues=NamedValues(*(('syntheticTraffic',1),('realTraffic',2),('lmmSynthetic',3),('slm',4),('realTrafficGreen',5),('realTrafficYellow',6),('realTrafficNoCcm',7),('realTrafficGreenNoCcm',8),(_h,255)))
_EthOamDestNeLmmTraffic_Type.__name__=_H
_EthOamDestNeLmmTraffic_Object=MibTableColumn
ethOamDestNeLmmTraffic=_EthOamDestNeLmmTraffic_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,40),_EthOamDestNeLmmTraffic_Type())
ethOamDestNeLmmTraffic.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamDestNeLmmTraffic.setStatus(_A)
_EthOamDestNeFramesAboveDelayBinProfile_Type=Unsigned32
_EthOamDestNeFramesAboveDelayBinProfile_Object=MibTableColumn
ethOamDestNeFramesAboveDelayBinProfile=_EthOamDestNeFramesAboveDelayBinProfile_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,41),_EthOamDestNeFramesAboveDelayBinProfile_Type())
ethOamDestNeFramesAboveDelayBinProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamDestNeFramesAboveDelayBinProfile.setStatus(_A)
_EthOamDestNeFramesAboveDelayVarBinProfile_Type=Unsigned32
_EthOamDestNeFramesAboveDelayVarBinProfile_Object=MibTableColumn
ethOamDestNeFramesAboveDelayVarBinProfile=_EthOamDestNeFramesAboveDelayVarBinProfile_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,42),_EthOamDestNeFramesAboveDelayVarBinProfile_Type())
ethOamDestNeFramesAboveDelayVarBinProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamDestNeFramesAboveDelayVarBinProfile.setStatus(_A)
class _EthOamDestNeDmmDataTlvLength_Type(Unsigned32):defaultValue=0
_EthOamDestNeDmmDataTlvLength_Type.__name__=_J
_EthOamDestNeDmmDataTlvLength_Object=MibTableColumn
ethOamDestNeDmmDataTlvLength=_EthOamDestNeDmmDataTlvLength_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,43),_EthOamDestNeDmmDataTlvLength_Type())
ethOamDestNeDmmDataTlvLength.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamDestNeDmmDataTlvLength.setStatus(_A)
class _EthOamDestNeLossActivity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_f,1),('singleEnded',2),('dualEnded',3)))
_EthOamDestNeLossActivity_Type.__name__=_H
_EthOamDestNeLossActivity_Object=MibTableColumn
ethOamDestNeLossActivity=_EthOamDestNeLossActivity_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,44),_EthOamDestNeLossActivity_Type())
ethOamDestNeLossActivity.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamDestNeLossActivity.setStatus(_A)
class _EthOamDestNeDelayActivity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_f,1),('oneWay',2),('twoWay',3)))
_EthOamDestNeDelayActivity_Type.__name__=_H
_EthOamDestNeDelayActivity_Object=MibTableColumn
ethOamDestNeDelayActivity=_EthOamDestNeDelayActivity_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,45),_EthOamDestNeDelayActivity_Type())
ethOamDestNeDelayActivity.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamDestNeDelayActivity.setStatus(_A)
_EthOamDestNeTxForward_Type=Counter32
_EthOamDestNeTxForward_Object=MibTableColumn
ethOamDestNeTxForward=_EthOamDestNeTxForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,46),_EthOamDestNeTxForward_Type())
ethOamDestNeTxForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeTxForward.setStatus(_A)
_EthOamDestNeOverflowTxForward_Type=Counter32
_EthOamDestNeOverflowTxForward_Object=MibTableColumn
ethOamDestNeOverflowTxForward=_EthOamDestNeOverflowTxForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,47),_EthOamDestNeOverflowTxForward_Type())
ethOamDestNeOverflowTxForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeOverflowTxForward.setStatus(_A)
_EthOamDestNeRxForward_Type=Counter32
_EthOamDestNeRxForward_Object=MibTableColumn
ethOamDestNeRxForward=_EthOamDestNeRxForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,48),_EthOamDestNeRxForward_Type())
ethOamDestNeRxForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeRxForward.setStatus(_A)
_EthOamDestNeOverflowRxForward_Type=Counter32
_EthOamDestNeOverflowRxForward_Object=MibTableColumn
ethOamDestNeOverflowRxForward=_EthOamDestNeOverflowRxForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,49),_EthOamDestNeOverflowRxForward_Type())
ethOamDestNeOverflowRxForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeOverflowRxForward.setStatus(_A)
_EthOamDestNeTxBackward_Type=Counter32
_EthOamDestNeTxBackward_Object=MibTableColumn
ethOamDestNeTxBackward=_EthOamDestNeTxBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,50),_EthOamDestNeTxBackward_Type())
ethOamDestNeTxBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeTxBackward.setStatus(_A)
_EthOamDestNeOverflowTxBackward_Type=Counter32
_EthOamDestNeOverflowTxBackward_Object=MibTableColumn
ethOamDestNeOverflowTxBackward=_EthOamDestNeOverflowTxBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,51),_EthOamDestNeOverflowTxBackward_Type())
ethOamDestNeOverflowTxBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeOverflowTxBackward.setStatus(_A)
_EthOamDestNeRxBackward_Type=Counter32
_EthOamDestNeRxBackward_Object=MibTableColumn
ethOamDestNeRxBackward=_EthOamDestNeRxBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,52),_EthOamDestNeRxBackward_Type())
ethOamDestNeRxBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeRxBackward.setStatus(_A)
_EthOamDestNeOverflowRxBackward_Type=Counter32
_EthOamDestNeOverflowRxBackward_Object=MibTableColumn
ethOamDestNeOverflowRxBackward=_EthOamDestNeOverflowRxBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,53),_EthOamDestNeOverflowRxBackward_Type())
ethOamDestNeOverflowRxBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeOverflowRxBackward.setStatus(_A)
_EthOamDestNeUnavailableIndForward_Type=Counter32
_EthOamDestNeUnavailableIndForward_Object=MibTableColumn
ethOamDestNeUnavailableIndForward=_EthOamDestNeUnavailableIndForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,54),_EthOamDestNeUnavailableIndForward_Type())
ethOamDestNeUnavailableIndForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeUnavailableIndForward.setStatus(_A)
if mibBuilder.loadTexts:ethOamDestNeUnavailableIndForward.setUnits(_S)
_EthOamDestNeOverflowUnavailableIndForward_Type=Counter32
_EthOamDestNeOverflowUnavailableIndForward_Object=MibTableColumn
ethOamDestNeOverflowUnavailableIndForward=_EthOamDestNeOverflowUnavailableIndForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,55),_EthOamDestNeOverflowUnavailableIndForward_Type())
ethOamDestNeOverflowUnavailableIndForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeOverflowUnavailableIndForward.setStatus(_A)
if mibBuilder.loadTexts:ethOamDestNeOverflowUnavailableIndForward.setUnits(_S)
_EthOamDestNeUnavailableIndBackward_Type=Counter32
_EthOamDestNeUnavailableIndBackward_Object=MibTableColumn
ethOamDestNeUnavailableIndBackward=_EthOamDestNeUnavailableIndBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,56),_EthOamDestNeUnavailableIndBackward_Type())
ethOamDestNeUnavailableIndBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeUnavailableIndBackward.setStatus(_A)
if mibBuilder.loadTexts:ethOamDestNeUnavailableIndBackward.setUnits(_S)
_EthOamDestNeOverflowUnavailableIndBackward_Type=Counter32
_EthOamDestNeOverflowUnavailableIndBackward_Object=MibTableColumn
ethOamDestNeOverflowUnavailableIndBackward=_EthOamDestNeOverflowUnavailableIndBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,57),_EthOamDestNeOverflowUnavailableIndBackward_Type())
ethOamDestNeOverflowUnavailableIndBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeOverflowUnavailableIndBackward.setStatus(_A)
if mibBuilder.loadTexts:ethOamDestNeOverflowUnavailableIndBackward.setUnits(_S)
_EthOamDestNeUnavailRatioForward_Type=Unsigned32
_EthOamDestNeUnavailRatioForward_Object=MibTableColumn
ethOamDestNeUnavailRatioForward=_EthOamDestNeUnavailRatioForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,58),_EthOamDestNeUnavailRatioForward_Type())
ethOamDestNeUnavailRatioForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeUnavailRatioForward.setStatus(_A)
_EthOamDestNeUnavailRatioBackward_Type=Unsigned32
_EthOamDestNeUnavailRatioBackward_Object=MibTableColumn
ethOamDestNeUnavailRatioBackward=_EthOamDestNeUnavailRatioBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,59),_EthOamDestNeUnavailRatioBackward_Type())
ethOamDestNeUnavailRatioBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeUnavailRatioBackward.setStatus(_A)
class _EthOamDestNeDescr_Type(SnmpAdminString):defaultValue=OctetString('')
_EthOamDestNeDescr_Type.__name__=_A0
_EthOamDestNeDescr_Object=MibTableColumn
ethOamDestNeDescr=_EthOamDestNeDescr_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,61),_EthOamDestNeDescr_Type())
ethOamDestNeDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamDestNeDescr.setStatus(_A)
_EthOamDestNeConvertedIndex_Type=Unsigned32
_EthOamDestNeConvertedIndex_Object=MibTableColumn
ethOamDestNeConvertedIndex=_EthOamDestNeConvertedIndex_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,62),_EthOamDestNeConvertedIndex_Type())
ethOamDestNeConvertedIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamDestNeConvertedIndex.setStatus(_A)
class _EthOamDestNeSlmDataTlvLength_Type(Unsigned32):defaultValue=0
_EthOamDestNeSlmDataTlvLength_Type.__name__=_J
_EthOamDestNeSlmDataTlvLength_Object=MibTableColumn
ethOamDestNeSlmDataTlvLength=_EthOamDestNeSlmDataTlvLength_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,63),_EthOamDestNeSlmDataTlvLength_Type())
ethOamDestNeSlmDataTlvLength.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamDestNeSlmDataTlvLength.setStatus(_A)
class _EthOamDestNeLmMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rx',1),('txAndRx',2)))
_EthOamDestNeLmMode_Type.__name__=_H
_EthOamDestNeLmMode_Object=MibTableColumn
ethOamDestNeLmMode=_EthOamDestNeLmMode_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,64),_EthOamDestNeLmMode_Type())
ethOamDestNeLmMode.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamDestNeLmMode.setStatus(_A)
class _EthOamDestNeSlmTestId_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_EthOamDestNeSlmTestId_Type.__name__=_J
_EthOamDestNeSlmTestId_Object=MibTableColumn
ethOamDestNeSlmTestId=_EthOamDestNeSlmTestId_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,65),_EthOamDestNeSlmTestId_Type())
ethOamDestNeSlmTestId.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamDestNeSlmTestId.setStatus(_A)
class _EthOamDestNeForwardDelayVarBinProfile_Type(Unsigned32):defaultValue=0
_EthOamDestNeForwardDelayVarBinProfile_Type.__name__=_J
_EthOamDestNeForwardDelayVarBinProfile_Object=MibTableColumn
ethOamDestNeForwardDelayVarBinProfile=_EthOamDestNeForwardDelayVarBinProfile_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,66),_EthOamDestNeForwardDelayVarBinProfile_Type())
ethOamDestNeForwardDelayVarBinProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamDestNeForwardDelayVarBinProfile.setStatus(_A)
class _EthOamDestNeBackwardDelayVarBinProfile_Type(Unsigned32):defaultValue=0
_EthOamDestNeBackwardDelayVarBinProfile_Type.__name__=_J
_EthOamDestNeBackwardDelayVarBinProfile_Object=MibTableColumn
ethOamDestNeBackwardDelayVarBinProfile=_EthOamDestNeBackwardDelayVarBinProfile_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,67),_EthOamDestNeBackwardDelayVarBinProfile_Type())
ethOamDestNeBackwardDelayVarBinProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamDestNeBackwardDelayVarBinProfile.setStatus(_A)
_EthOamDestNeAvailableIndForward_Type=Counter32
_EthOamDestNeAvailableIndForward_Object=MibTableColumn
ethOamDestNeAvailableIndForward=_EthOamDestNeAvailableIndForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,68),_EthOamDestNeAvailableIndForward_Type())
ethOamDestNeAvailableIndForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeAvailableIndForward.setStatus(_A)
if mibBuilder.loadTexts:ethOamDestNeAvailableIndForward.setUnits(_S)
_EthOamDestNeAvailableIndBackward_Type=Counter32
_EthOamDestNeAvailableIndBackward_Object=MibTableColumn
ethOamDestNeAvailableIndBackward=_EthOamDestNeAvailableIndBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,69),_EthOamDestNeAvailableIndBackward_Type())
ethOamDestNeAvailableIndBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeAvailableIndBackward.setStatus(_A)
if mibBuilder.loadTexts:ethOamDestNeAvailableIndBackward.setUnits(_S)
_EthOamDestNeDelayVariationForward_Type=Unsigned32
_EthOamDestNeDelayVariationForward_Object=MibTableColumn
ethOamDestNeDelayVariationForward=_EthOamDestNeDelayVariationForward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,70),_EthOamDestNeDelayVariationForward_Type())
ethOamDestNeDelayVariationForward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeDelayVariationForward.setStatus(_A)
if mibBuilder.loadTexts:ethOamDestNeDelayVariationForward.setUnits(_G)
_EthOamDestNeDelayVariationBackward_Type=Unsigned32
_EthOamDestNeDelayVariationBackward_Object=MibTableColumn
ethOamDestNeDelayVariationBackward=_EthOamDestNeDelayVariationBackward_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,5,1,71),_EthOamDestNeDelayVariationBackward_Type())
ethOamDestNeDelayVariationBackward.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDestNeDelayVariationBackward.setStatus(_A)
if mibBuilder.loadTexts:ethOamDestNeDelayVariationBackward.setUnits(_G)
_EthOamSvcRmonConfigTable_Object=MibTable
ethOamSvcRmonConfigTable=_EthOamSvcRmonConfigTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,6))
if mibBuilder.loadTexts:ethOamSvcRmonConfigTable.setStatus(_A)
_EthOamSvcRmonConfigEntry_Object=MibTableRow
ethOamSvcRmonConfigEntry=_EthOamSvcRmonConfigEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,6,1))
ethOamSvcRmonConfigEntry.setIndexNames((0,_E,_W),(0,_E,_b),(0,_E,_X),(0,_E,_d),(0,_E,_A4))
if mibBuilder.loadTexts:ethOamSvcRmonConfigEntry.setStatus(_A)
class _EthOamSvcRmonConfigPerfAttrib_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('framesAboveDelay',1),('framesAboveDelayVar',2),('farEndFrameLossRatio',3),('nearEndFrameLossRatio',4),('unavailabilityRatio',5),('farEndUnavailabilityRatio',6),('nearEndUnavailabilityRatio',7)))
_EthOamSvcRmonConfigPerfAttrib_Type.__name__=_H
_EthOamSvcRmonConfigPerfAttrib_Object=MibTableColumn
ethOamSvcRmonConfigPerfAttrib=_EthOamSvcRmonConfigPerfAttrib_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,6,1,1),_EthOamSvcRmonConfigPerfAttrib_Type())
ethOamSvcRmonConfigPerfAttrib.setMaxAccess(_I)
if mibBuilder.loadTexts:ethOamSvcRmonConfigPerfAttrib.setStatus(_A)
_EthOamSvcRmonConfigRowStatus_Type=RowStatus
_EthOamSvcRmonConfigRowStatus_Object=MibTableColumn
ethOamSvcRmonConfigRowStatus=_EthOamSvcRmonConfigRowStatus_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,6,1,2),_EthOamSvcRmonConfigRowStatus_Type())
ethOamSvcRmonConfigRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamSvcRmonConfigRowStatus.setStatus(_A)
_EthOamSvcRmonConfigAlarmInterval_Type=Integer32
_EthOamSvcRmonConfigAlarmInterval_Object=MibTableColumn
ethOamSvcRmonConfigAlarmInterval=_EthOamSvcRmonConfigAlarmInterval_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,6,1,3),_EthOamSvcRmonConfigAlarmInterval_Type())
ethOamSvcRmonConfigAlarmInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamSvcRmonConfigAlarmInterval.setStatus(_A)
_EthOamSvcRmonConfigAlarmRisingThresh_Type=Integer32
_EthOamSvcRmonConfigAlarmRisingThresh_Object=MibTableColumn
ethOamSvcRmonConfigAlarmRisingThresh=_EthOamSvcRmonConfigAlarmRisingThresh_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,6,1,4),_EthOamSvcRmonConfigAlarmRisingThresh_Type())
ethOamSvcRmonConfigAlarmRisingThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamSvcRmonConfigAlarmRisingThresh.setStatus(_A)
_EthOamSvcRmonConfigAlarmFallingThresh_Type=Integer32
_EthOamSvcRmonConfigAlarmFallingThresh_Object=MibTableColumn
ethOamSvcRmonConfigAlarmFallingThresh=_EthOamSvcRmonConfigAlarmFallingThresh_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,6,1,5),_EthOamSvcRmonConfigAlarmFallingThresh_Type())
ethOamSvcRmonConfigAlarmFallingThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamSvcRmonConfigAlarmFallingThresh.setStatus(_A)
class _EthOamSvcRmonConfigEventType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_f,1),('log',2),('snmptrap',3),('logandtrap',4)))
_EthOamSvcRmonConfigEventType_Type.__name__=_H
_EthOamSvcRmonConfigEventType_Object=MibTableColumn
ethOamSvcRmonConfigEventType=_EthOamSvcRmonConfigEventType_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,6,1,6),_EthOamSvcRmonConfigEventType_Type())
ethOamSvcRmonConfigEventType.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamSvcRmonConfigEventType.setStatus(_A)
_EthOamMeasureBinProfileTable_Object=MibTable
ethOamMeasureBinProfileTable=_EthOamMeasureBinProfileTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,7))
if mibBuilder.loadTexts:ethOamMeasureBinProfileTable.setStatus(_A)
_EthOamMeasureBinProfileEntry_Object=MibTableRow
ethOamMeasureBinProfileEntry=_EthOamMeasureBinProfileEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,7,1))
ethOamMeasureBinProfileEntry.setIndexNames((0,_E,_A5))
if mibBuilder.loadTexts:ethOamMeasureBinProfileEntry.setStatus(_A)
_EthOamMeasureBinProfileIndex_Type=Unsigned32
_EthOamMeasureBinProfileIndex_Object=MibTableColumn
ethOamMeasureBinProfileIndex=_EthOamMeasureBinProfileIndex_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,7,1,1),_EthOamMeasureBinProfileIndex_Type())
ethOamMeasureBinProfileIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ethOamMeasureBinProfileIndex.setStatus(_A)
_EthOamMeasureBinProfileRowStatus_Type=RowStatus
_EthOamMeasureBinProfileRowStatus_Object=MibTableColumn
ethOamMeasureBinProfileRowStatus=_EthOamMeasureBinProfileRowStatus_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,7,1,2),_EthOamMeasureBinProfileRowStatus_Type())
ethOamMeasureBinProfileRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamMeasureBinProfileRowStatus.setStatus(_A)
_EthOamMeasureBinProfileName_Type=SnmpAdminString
_EthOamMeasureBinProfileName_Object=MibTableColumn
ethOamMeasureBinProfileName=_EthOamMeasureBinProfileName_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,7,1,3),_EthOamMeasureBinProfileName_Type())
ethOamMeasureBinProfileName.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamMeasureBinProfileName.setStatus(_A)
class _EthOamMeasureBinThresh_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(36,36));fixedLength=36
_EthOamMeasureBinThresh_Type.__name__=_e
_EthOamMeasureBinThresh_Object=MibTableColumn
ethOamMeasureBinThresh=_EthOamMeasureBinThresh_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,7,1,4),_EthOamMeasureBinThresh_Type())
ethOamMeasureBinThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamMeasureBinThresh.setStatus(_A)
_EthOamDelayCurrentBinsTable_Object=MibTable
ethOamDelayCurrentBinsTable=_EthOamDelayCurrentBinsTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,8))
if mibBuilder.loadTexts:ethOamDelayCurrentBinsTable.setStatus(_A)
_EthOamDelayCurrentBinsEntry_Object=MibTableRow
ethOamDelayCurrentBinsEntry=_EthOamDelayCurrentBinsEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,8,1))
ethOamDelayCurrentBinsEntry.setIndexNames((0,_E,_W),(0,_E,_b),(0,_E,_X),(0,_E,_d),(0,_E,_A6),(0,_E,_A7))
if mibBuilder.loadTexts:ethOamDelayCurrentBinsEntry.setStatus(_A)
_EthOamDelayCurrentBinCounterType_Type=EthOamBinCounterType
_EthOamDelayCurrentBinCounterType_Object=MibTableColumn
ethOamDelayCurrentBinCounterType=_EthOamDelayCurrentBinCounterType_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,8,1,1),_EthOamDelayCurrentBinCounterType_Type())
ethOamDelayCurrentBinCounterType.setMaxAccess(_I)
if mibBuilder.loadTexts:ethOamDelayCurrentBinCounterType.setStatus(_A)
class _EthOamDelayCurrentBinNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_EthOamDelayCurrentBinNumber_Type.__name__=_J
_EthOamDelayCurrentBinNumber_Object=MibTableColumn
ethOamDelayCurrentBinNumber=_EthOamDelayCurrentBinNumber_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,8,1,2),_EthOamDelayCurrentBinNumber_Type())
ethOamDelayCurrentBinNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:ethOamDelayCurrentBinNumber.setStatus(_A)
_EthOamDelayCurrentBinValue_Type=PerfCurrentCount
_EthOamDelayCurrentBinValue_Object=MibTableColumn
ethOamDelayCurrentBinValue=_EthOamDelayCurrentBinValue_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,8,1,3),_EthOamDelayCurrentBinValue_Type())
ethOamDelayCurrentBinValue.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDelayCurrentBinValue.setStatus(_A)
_EthOamDelayIntervalBinsTable_Object=MibTable
ethOamDelayIntervalBinsTable=_EthOamDelayIntervalBinsTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,10))
if mibBuilder.loadTexts:ethOamDelayIntervalBinsTable.setStatus(_A)
_EthOamDelayIntervalBinsEntry_Object=MibTableRow
ethOamDelayIntervalBinsEntry=_EthOamDelayIntervalBinsEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,10,1))
ethOamDelayIntervalBinsEntry.setIndexNames((0,_E,_W),(0,_E,_b),(0,_E,_X),(0,_E,_d),(0,_E,_w),(0,_E,_A8),(0,_E,_A9))
if mibBuilder.loadTexts:ethOamDelayIntervalBinsEntry.setStatus(_A)
_EthOamDelayIntervalBinCounterType_Type=EthOamBinCounterType
_EthOamDelayIntervalBinCounterType_Object=MibTableColumn
ethOamDelayIntervalBinCounterType=_EthOamDelayIntervalBinCounterType_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,10,1,1),_EthOamDelayIntervalBinCounterType_Type())
ethOamDelayIntervalBinCounterType.setMaxAccess(_I)
if mibBuilder.loadTexts:ethOamDelayIntervalBinCounterType.setStatus(_A)
class _EthOamDelayIntervalBinNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_EthOamDelayIntervalBinNumber_Type.__name__=_J
_EthOamDelayIntervalBinNumber_Object=MibTableColumn
ethOamDelayIntervalBinNumber=_EthOamDelayIntervalBinNumber_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,10,1,2),_EthOamDelayIntervalBinNumber_Type())
ethOamDelayIntervalBinNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:ethOamDelayIntervalBinNumber.setStatus(_A)
_EthOamDelayIntervalBinValue_Type=PerfIntervalCount
_EthOamDelayIntervalBinValue_Object=MibTableColumn
ethOamDelayIntervalBinValue=_EthOamDelayIntervalBinValue_Object((1,3,6,1,4,1,164,3,1,6,1,3,2,10,1,3),_EthOamDelayIntervalBinValue_Type())
ethOamDelayIntervalBinValue.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamDelayIntervalBinValue.setStatus(_A)
_RadMdTable_Object=MibTable
radMdTable=_RadMdTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,3))
if mibBuilder.loadTexts:radMdTable.setStatus(_A)
_RadMdEntry_Object=MibTableRow
radMdEntry=_RadMdEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,3,1))
radMdEntry.setIndexNames((0,_E,_AA))
if mibBuilder.loadTexts:radMdEntry.setStatus(_A)
_RadMdIndex_Type=Unsigned32
_RadMdIndex_Object=MibTableColumn
radMdIndex=_RadMdIndex_Object((1,3,6,1,4,1,164,3,1,6,1,3,3,1,1),_RadMdIndex_Type())
radMdIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:radMdIndex.setStatus(_A)
class _RadMdFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_f,1),('dnsLikeName',2),('macAddressAndUint',3),(_A2,4)))
_RadMdFormat_Type.__name__=_H
_RadMdFormat_Object=MibTableColumn
radMdFormat=_RadMdFormat_Object((1,3,6,1,4,1,164,3,1,6,1,3,3,1,2),_RadMdFormat_Type())
radMdFormat.setMaxAccess(_D)
if mibBuilder.loadTexts:radMdFormat.setStatus(_A)
class _RadMdName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,43))
_RadMdName_Type.__name__=_e
_RadMdName_Object=MibTableColumn
radMdName=_RadMdName_Object((1,3,6,1,4,1,164,3,1,6,1,3,3,1,3),_RadMdName_Type())
radMdName.setMaxAccess(_D)
if mibBuilder.loadTexts:radMdName.setStatus(_A)
_RadMdRowStatus_Type=RowStatus
_RadMdRowStatus_Object=MibTableColumn
radMdRowStatus=_RadMdRowStatus_Object((1,3,6,1,4,1,164,3,1,6,1,3,3,1,4),_RadMdRowStatus_Type())
radMdRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:radMdRowStatus.setStatus(_A)
_RadMepLtrTable_Object=MibTable
radMepLtrTable=_RadMepLtrTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,4))
if mibBuilder.loadTexts:radMepLtrTable.setStatus(_A)
_RadMepLtrEntry_Object=MibTableRow
radMepLtrEntry=_RadMepLtrEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,4,1))
radMepLtrEntry.setIndexNames((0,_E,_W),(0,_E,_X),(0,_E,_AB))
if mibBuilder.loadTexts:radMepLtrEntry.setStatus(_A)
_RadMepLtrReceiveOrder_Type=Unsigned32
_RadMepLtrReceiveOrder_Object=MibTableColumn
radMepLtrReceiveOrder=_RadMepLtrReceiveOrder_Object((1,3,6,1,4,1,164,3,1,6,1,3,4,1,1),_RadMepLtrReceiveOrder_Type())
radMepLtrReceiveOrder.setMaxAccess(_I)
if mibBuilder.loadTexts:radMepLtrReceiveOrder.setStatus(_A)
class _RadMepLtrTtl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RadMepLtrTtl_Type.__name__=_J
_RadMepLtrTtl_Object=MibTableColumn
radMepLtrTtl=_RadMepLtrTtl_Object((1,3,6,1,4,1,164,3,1,6,1,3,4,1,2),_RadMepLtrTtl_Type())
radMepLtrTtl.setMaxAccess(_B)
if mibBuilder.loadTexts:radMepLtrTtl.setStatus(_A)
_RadMepLtrMacAddr_Type=MacAddress
_RadMepLtrMacAddr_Object=MibTableColumn
radMepLtrMacAddr=_RadMepLtrMacAddr_Object((1,3,6,1,4,1,164,3,1,6,1,3,4,1,3),_RadMepLtrMacAddr_Type())
radMepLtrMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:radMepLtrMacAddr.setStatus(_A)
class _RadMepLtrRelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('rlyHit',1),('rlyFdb',2),('rlyMpdb',3)))
_RadMepLtrRelay_Type.__name__=_H
_RadMepLtrRelay_Object=MibTableColumn
radMepLtrRelay=_RadMepLtrRelay_Object((1,3,6,1,4,1,164,3,1,6,1,3,4,1,4),_RadMepLtrRelay_Type())
radMepLtrRelay.setMaxAccess(_B)
if mibBuilder.loadTexts:radMepLtrRelay.setStatus(_A)
class _RadMepLtrIngress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ingNoTlv',1),('ingOk',2),('ingDown',3),('ingBlocked',4),('ingVid',5)))
_RadMepLtrIngress_Type.__name__=_H
_RadMepLtrIngress_Object=MibTableColumn
radMepLtrIngress=_RadMepLtrIngress_Object((1,3,6,1,4,1,164,3,1,6,1,3,4,1,5),_RadMepLtrIngress_Type())
radMepLtrIngress.setMaxAccess(_B)
if mibBuilder.loadTexts:radMepLtrIngress.setStatus(_A)
_RadMepLtrIngressPortIdSubtype_Type=LldpPortIdSubtype
_RadMepLtrIngressPortIdSubtype_Object=MibTableColumn
radMepLtrIngressPortIdSubtype=_RadMepLtrIngressPortIdSubtype_Object((1,3,6,1,4,1,164,3,1,6,1,3,4,1,6),_RadMepLtrIngressPortIdSubtype_Type())
radMepLtrIngressPortIdSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:radMepLtrIngressPortIdSubtype.setStatus(_A)
class _RadMepLtrIngressPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_RadMepLtrIngressPortId_Type.__name__=_e
_RadMepLtrIngressPortId_Object=MibTableColumn
radMepLtrIngressPortId=_RadMepLtrIngressPortId_Object((1,3,6,1,4,1,164,3,1,6,1,3,4,1,7),_RadMepLtrIngressPortId_Type())
radMepLtrIngressPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:radMepLtrIngressPortId.setStatus(_A)
class _RadMepLtrEgress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('egrNoTlv',1),('egrOK',2),('egrDown',3),('egrBlocked',4),('egrVid',5)))
_RadMepLtrEgress_Type.__name__=_H
_RadMepLtrEgress_Object=MibTableColumn
radMepLtrEgress=_RadMepLtrEgress_Object((1,3,6,1,4,1,164,3,1,6,1,3,4,1,8),_RadMepLtrEgress_Type())
radMepLtrEgress.setMaxAccess(_B)
if mibBuilder.loadTexts:radMepLtrEgress.setStatus(_A)
_RadMepLtrEgressPortIdSubtype_Type=LldpPortIdSubtype
_RadMepLtrEgressPortIdSubtype_Object=MibTableColumn
radMepLtrEgressPortIdSubtype=_RadMepLtrEgressPortIdSubtype_Object((1,3,6,1,4,1,164,3,1,6,1,3,4,1,9),_RadMepLtrEgressPortIdSubtype_Type())
radMepLtrEgressPortIdSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:radMepLtrEgressPortIdSubtype.setStatus(_A)
class _RadMepLtrEgressPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_RadMepLtrEgressPortId_Type.__name__=_e
_RadMepLtrEgressPortId_Object=MibTableColumn
radMepLtrEgressPortId=_RadMepLtrEgressPortId_Object((1,3,6,1,4,1,164,3,1,6,1,3,4,1,10),_RadMepLtrEgressPortId_Type())
radMepLtrEgressPortId.setMaxAccess(_B)
if mibBuilder.loadTexts:radMepLtrEgressPortId.setStatus(_A)
_RadMepCcStatusTable_Object=MibTable
radMepCcStatusTable=_RadMepCcStatusTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,5))
if mibBuilder.loadTexts:radMepCcStatusTable.setStatus(_A)
_RadMepCcStatusEntry_Object=MibTableRow
radMepCcStatusEntry=_RadMepCcStatusEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,5,1))
radMepCcStatusEntry.setIndexNames((0,_E,_W),(0,_E,_X),(0,_E,_AC))
if mibBuilder.loadTexts:radMepCcStatusEntry.setStatus(_A)
_RadMepRemoteMepIdx_Type=Unsigned32
_RadMepRemoteMepIdx_Object=MibTableColumn
radMepRemoteMepIdx=_RadMepRemoteMepIdx_Object((1,3,6,1,4,1,164,3,1,6,1,3,5,1,1),_RadMepRemoteMepIdx_Type())
radMepRemoteMepIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:radMepRemoteMepIdx.setStatus(_A)
_RadMepCcStatusRemMepId_Type=Unsigned32
_RadMepCcStatusRemMepId_Object=MibTableColumn
radMepCcStatusRemMepId=_RadMepCcStatusRemMepId_Object((1,3,6,1,4,1,164,3,1,6,1,3,5,1,2),_RadMepCcStatusRemMepId_Type())
radMepCcStatusRemMepId.setMaxAccess(_D)
if mibBuilder.loadTexts:radMepCcStatusRemMepId.setStatus(_A)
class _RadMepCcStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_h,1),(_r,2),('ok',3),(_l,4),(_m,5),(_s,6),(_x,7),('rdi',8)))
_RadMepCcStat_Type.__name__=_H
_RadMepCcStat_Object=MibTableColumn
radMepCcStat=_RadMepCcStat_Object((1,3,6,1,4,1,164,3,1,6,1,3,5,1,3),_RadMepCcStat_Type())
radMepCcStat.setMaxAccess(_B)
if mibBuilder.loadTexts:radMepCcStat.setStatus(_A)
_RadMepCcStatusMacAddr_Type=MacAddress
_RadMepCcStatusMacAddr_Object=MibTableColumn
radMepCcStatusMacAddr=_RadMepCcStatusMacAddr_Object((1,3,6,1,4,1,164,3,1,6,1,3,5,1,4),_RadMepCcStatusMacAddr_Type())
radMepCcStatusMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:radMepCcStatusMacAddr.setStatus(_A)
_EthOamStdEtherType_Type=Unsigned32
_EthOamStdEtherType_Object=MibScalar
ethOamStdEtherType=_EthOamStdEtherType_Object((1,3,6,1,4,1,164,3,1,6,1,3,6),_EthOamStdEtherType_Type())
ethOamStdEtherType.setMaxAccess(_T)
if mibBuilder.loadTexts:ethOamStdEtherType.setStatus(_A)
_EthOamStdMacAddress_Type=MacAddress
_EthOamStdMacAddress_Object=MibScalar
ethOamStdMacAddress=_EthOamStdMacAddress_Object((1,3,6,1,4,1,164,3,1,6,1,3,7),_EthOamStdMacAddress_Type())
ethOamStdMacAddress.setMaxAccess(_T)
if mibBuilder.loadTexts:ethOamStdMacAddress.setStatus(_A)
_Dot1agXCfmMdTable_Object=MibTable
dot1agXCfmMdTable=_Dot1agXCfmMdTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,8))
if mibBuilder.loadTexts:dot1agXCfmMdTable.setStatus(_A)
_Dot1agXCfmMdEntry_Object=MibTableRow
dot1agXCfmMdEntry=_Dot1agXCfmMdEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,8,1))
dot1agXCfmMdEntry.setIndexNames((0,_F,_V))
if mibBuilder.loadTexts:dot1agXCfmMdEntry.setStatus(_A)
class _Dot1agXCfmMdProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('preStandard',1),('standard',2)))
_Dot1agXCfmMdProtocol_Type.__name__=_H
_Dot1agXCfmMdProtocol_Object=MibTableColumn
dot1agXCfmMdProtocol=_Dot1agXCfmMdProtocol_Object((1,3,6,1,4,1,164,3,1,6,1,3,8,1,1),_Dot1agXCfmMdProtocol_Type())
dot1agXCfmMdProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMdProtocol.setStatus(_A)
_Dot1agXCfmMepTable_Object=MibTable
dot1agXCfmMepTable=_Dot1agXCfmMepTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,9))
if mibBuilder.loadTexts:dot1agXCfmMepTable.setStatus(_A)
_Dot1agXCfmMepEntry_Object=MibTableRow
dot1agXCfmMepEntry=_Dot1agXCfmMepEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1))
dot1agXCfmMepEntry.setIndexNames((0,_F,_V),(0,_F,_Y),(0,_F,_c))
if mibBuilder.loadTexts:dot1agXCfmMepEntry.setStatus(_A)
class _Dot1agXCfmMepContinuityVerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_o,2),('ccBased',3),('lbBased',4)))
_Dot1agXCfmMepContinuityVerMode_Type.__name__=_H
_Dot1agXCfmMepContinuityVerMode_Object=MibTableColumn
dot1agXCfmMepContinuityVerMode=_Dot1agXCfmMepContinuityVerMode_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,1),_Dot1agXCfmMepContinuityVerMode_Type())
dot1agXCfmMepContinuityVerMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMepContinuityVerMode.setStatus(_A)
class _Dot1agXCfmMepDestAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_p,1),(_q,2)))
_Dot1agXCfmMepDestAddrType_Type.__name__=_H
_Dot1agXCfmMepDestAddrType_Object=MibTableColumn
dot1agXCfmMepDestAddrType=_Dot1agXCfmMepDestAddrType_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,2),_Dot1agXCfmMepDestAddrType_Type())
dot1agXCfmMepDestAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMepDestAddrType.setStatus(_A)
_Dot1agXCfmMepDestMacAddr_Type=MacAddress
_Dot1agXCfmMepDestMacAddr_Object=MibTableColumn
dot1agXCfmMepDestMacAddr=_Dot1agXCfmMepDestMacAddr_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,3),_Dot1agXCfmMepDestMacAddr_Type())
dot1agXCfmMepDestMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMepDestMacAddr.setStatus(_A)
_Dot1agXCfmMepMappingProfile_Type=Unsigned32
_Dot1agXCfmMepMappingProfile_Object=MibTableColumn
dot1agXCfmMepMappingProfile=_Dot1agXCfmMepMappingProfile_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,4),_Dot1agXCfmMepMappingProfile_Type())
dot1agXCfmMepMappingProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMepMappingProfile.setStatus(_A)
_Dot1agXCfmMepQBlock_Type=ObjectIdentifier
_Dot1agXCfmMepQBlock_Object=MibTableColumn
dot1agXCfmMepQBlock=_Dot1agXCfmMepQBlock_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,5),_Dot1agXCfmMepQBlock_Type())
dot1agXCfmMepQBlock.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMepQBlock.setStatus(_A)
_Dot1agXCfmMepFixedQueueMapping_Type=Unsigned32
_Dot1agXCfmMepFixedQueueMapping_Object=MibTableColumn
dot1agXCfmMepFixedQueueMapping=_Dot1agXCfmMepFixedQueueMapping_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,6),_Dot1agXCfmMepFixedQueueMapping_Type())
dot1agXCfmMepFixedQueueMapping.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMepFixedQueueMapping.setStatus(_A)
_Dot1agXCfmMepQueueMappingProfile_Type=Unsigned32
_Dot1agXCfmMepQueueMappingProfile_Object=MibTableColumn
dot1agXCfmMepQueueMappingProfile=_Dot1agXCfmMepQueueMappingProfile_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,7),_Dot1agXCfmMepQueueMappingProfile_Type())
dot1agXCfmMepQueueMappingProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMepQueueMappingProfile.setStatus(_A)
_Dot1agXCfmMepConvertedIndex_Type=Unsigned32
_Dot1agXCfmMepConvertedIndex_Object=MibTableColumn
dot1agXCfmMepConvertedIndex=_Dot1agXCfmMepConvertedIndex_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,8),_Dot1agXCfmMepConvertedIndex_Type())
dot1agXCfmMepConvertedIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agXCfmMepConvertedIndex.setStatus(_A)
class _Dot1agXCfmMepPmDestAddrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_p,1),(_q,2)))
_Dot1agXCfmMepPmDestAddrType_Type.__name__=_H
_Dot1agXCfmMepPmDestAddrType_Object=MibTableColumn
dot1agXCfmMepPmDestAddrType=_Dot1agXCfmMepPmDestAddrType_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,9),_Dot1agXCfmMepPmDestAddrType_Type())
dot1agXCfmMepPmDestAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMepPmDestAddrType.setStatus(_A)
class _Dot1agXCfmMepForwardingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('eline',1),('elan',2)))
_Dot1agXCfmMepForwardingMode_Type.__name__=_H
_Dot1agXCfmMepForwardingMode_Object=MibTableColumn
dot1agXCfmMepForwardingMode=_Dot1agXCfmMepForwardingMode_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,10),_Dot1agXCfmMepForwardingMode_Type())
dot1agXCfmMepForwardingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMepForwardingMode.setStatus(_A)
class _Dot1agXCfmMepLbmDataTlvLength_Type(Unsigned32):defaultValue=0
_Dot1agXCfmMepLbmDataTlvLength_Type.__name__=_J
_Dot1agXCfmMepLbmDataTlvLength_Object=MibTableColumn
dot1agXCfmMepLbmDataTlvLength=_Dot1agXCfmMepLbmDataTlvLength_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,11),_Dot1agXCfmMepLbmDataTlvLength_Type())
dot1agXCfmMepLbmDataTlvLength.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMepLbmDataTlvLength.setStatus(_A)
class _Dot1agXCfmMepClientMdLevel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot1agXCfmMepClientMdLevel_Type.__name__=_J
_Dot1agXCfmMepClientMdLevel_Object=MibTableColumn
dot1agXCfmMepClientMdLevel=_Dot1agXCfmMepClientMdLevel_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,12),_Dot1agXCfmMepClientMdLevel_Type())
dot1agXCfmMepClientMdLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMepClientMdLevel.setStatus(_A)
class _Dot1agXCfmMepAisTransmit_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_u,2),(_v,3)))
_Dot1agXCfmMepAisTransmit_Type.__name__=_H
_Dot1agXCfmMepAisTransmit_Object=MibTableColumn
dot1agXCfmMepAisTransmit=_Dot1agXCfmMepAisTransmit_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,13),_Dot1agXCfmMepAisTransmit_Type())
dot1agXCfmMepAisTransmit.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMepAisTransmit.setStatus(_A)
class _Dot1agXCfmMepAisInterval_Type(Dot1agCfmCcmInterval):defaultValue=4
_Dot1agXCfmMepAisInterval_Type.__name__=_k
_Dot1agXCfmMepAisInterval_Object=MibTableColumn
dot1agXCfmMepAisInterval=_Dot1agXCfmMepAisInterval_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,14),_Dot1agXCfmMepAisInterval_Type())
dot1agXCfmMepAisInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMepAisInterval.setStatus(_A)
class _Dot1agXCfmMepAisPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Dot1agXCfmMepAisPriority_Type.__name__=_J
_Dot1agXCfmMepAisPriority_Object=MibTableColumn
dot1agXCfmMepAisPriority=_Dot1agXCfmMepAisPriority_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,15),_Dot1agXCfmMepAisPriority_Type())
dot1agXCfmMepAisPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMepAisPriority.setStatus(_A)
class _Dot1agXCfmMepDefects_Type(Bits):namedValues=NamedValues(*(('bDefAIS',0),('bDefLCK',1)))
_Dot1agXCfmMepDefects_Type.__name__=_g
_Dot1agXCfmMepDefects_Object=MibTableColumn
dot1agXCfmMepDefects=_Dot1agXCfmMepDefects_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,16),_Dot1agXCfmMepDefects_Type())
dot1agXCfmMepDefects.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMepDefects.setStatus(_A)
class _Dot1agXCfmMepLastAlarmDefect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_f,1),('defRDICCM',2),('defMACstatus',3),('defRemoteCCM',4),('defErrorCCM',5),('defXconCCM',6),('defAIS',7),('defLCK',8)))
_Dot1agXCfmMepLastAlarmDefect_Type.__name__=_H
_Dot1agXCfmMepLastAlarmDefect_Object=MibTableColumn
dot1agXCfmMepLastAlarmDefect=_Dot1agXCfmMepLastAlarmDefect_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,17),_Dot1agXCfmMepLastAlarmDefect_Type())
dot1agXCfmMepLastAlarmDefect.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agXCfmMepLastAlarmDefect.setStatus(_A)
_Dot1agXCfmMepCosMapping_Type=Unsigned32
_Dot1agXCfmMepCosMapping_Object=MibTableColumn
dot1agXCfmMepCosMapping=_Dot1agXCfmMepCosMapping_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,19),_Dot1agXCfmMepCosMapping_Type())
dot1agXCfmMepCosMapping.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMepCosMapping.setStatus(_A)
_Dot1agXCfmMepCosMappingProfile_Type=Unsigned32
_Dot1agXCfmMepCosMappingProfile_Object=MibTableColumn
dot1agXCfmMepCosMappingProfile=_Dot1agXCfmMepCosMappingProfile_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,20),_Dot1agXCfmMepCosMappingProfile_Type())
dot1agXCfmMepCosMappingProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMepCosMappingProfile.setStatus(_A)
class _Dot1agXCfmMepCcStatus_Type(Bits):namedValues=NamedValues(*((_h,0),('otherFail',1),(_l,2),(_m,3),('unexpectedMepLevel',4),(_x,5)))
_Dot1agXCfmMepCcStatus_Type.__name__=_g
_Dot1agXCfmMepCcStatus_Object=MibTableColumn
dot1agXCfmMepCcStatus=_Dot1agXCfmMepCcStatus_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,24),_Dot1agXCfmMepCcStatus_Type())
dot1agXCfmMepCcStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agXCfmMepCcStatus.setStatus(_A)
class _Dot1agXCfmMepStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_f,1),('y1564',2),('rfc2544',3),('mef46Loop',4)))
_Dot1agXCfmMepStatus_Type.__name__=_H
_Dot1agXCfmMepStatus_Object=MibTableColumn
dot1agXCfmMepStatus=_Dot1agXCfmMepStatus_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,28),_Dot1agXCfmMepStatus_Type())
dot1agXCfmMepStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agXCfmMepStatus.setStatus(_A)
_Dot1agXCfmMepExcludeCustomerTags_Type=TruthValue
_Dot1agXCfmMepExcludeCustomerTags_Object=MibTableColumn
dot1agXCfmMepExcludeCustomerTags=_Dot1agXCfmMepExcludeCustomerTags_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,29),_Dot1agXCfmMepExcludeCustomerTags_Type())
dot1agXCfmMepExcludeCustomerTags.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMepExcludeCustomerTags.setStatus(_A)
class _Dot1agXCfmMepClearStatsCmd_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_i,2),(_j,3)))
_Dot1agXCfmMepClearStatsCmd_Type.__name__=_H
_Dot1agXCfmMepClearStatsCmd_Object=MibTableColumn
dot1agXCfmMepClearStatsCmd=_Dot1agXCfmMepClearStatsCmd_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,30),_Dot1agXCfmMepClearStatsCmd_Type())
dot1agXCfmMepClearStatsCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMepClearStatsCmd.setStatus(_A)
class _Dot1agXCfmMepTimeElapsed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_Dot1agXCfmMepTimeElapsed_Type.__name__=_J
_Dot1agXCfmMepTimeElapsed_Object=MibTableColumn
dot1agXCfmMepTimeElapsed=_Dot1agXCfmMepTimeElapsed_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,31),_Dot1agXCfmMepTimeElapsed_Type())
dot1agXCfmMepTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agXCfmMepTimeElapsed.setStatus(_A)
_Dot1agXCfmMepCcmTx_Type=Counter64
_Dot1agXCfmMepCcmTx_Object=MibTableColumn
dot1agXCfmMepCcmTx=_Dot1agXCfmMepCcmTx_Object((1,3,6,1,4,1,164,3,1,6,1,3,9,1,32),_Dot1agXCfmMepCcmTx_Type())
dot1agXCfmMepCcmTx.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agXCfmMepCcmTx.setStatus(_A)
_Dot1agXCfmMepDbTable_Object=MibTable
dot1agXCfmMepDbTable=_Dot1agXCfmMepDbTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,10))
if mibBuilder.loadTexts:dot1agXCfmMepDbTable.setStatus(_Z)
_Dot1agXCfmMepDbEntry_Object=MibTableRow
dot1agXCfmMepDbEntry=_Dot1agXCfmMepDbEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,10,1))
dot1agXCfmMepDbEntry.setIndexNames((0,_F,_V),(0,_F,_Y),(0,_F,_c),(0,_F,_z))
if mibBuilder.loadTexts:dot1agXCfmMepDbEntry.setStatus(_Z)
class _Dot1agXCfmMepCcStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_h,1),(_r,2),('ok',3),(_l,4),(_m,5),(_s,6),(_x,7),('rdi',8)))
_Dot1agXCfmMepCcStat_Type.__name__=_H
_Dot1agXCfmMepCcStat_Object=MibTableColumn
dot1agXCfmMepCcStat=_Dot1agXCfmMepCcStat_Object((1,3,6,1,4,1,164,3,1,6,1,3,10,1,1),_Dot1agXCfmMepCcStat_Type())
dot1agXCfmMepCcStat.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agXCfmMepCcStat.setStatus(_Z)
_Dot1agXCfmMepDbConvertedIndex_Type=Unsigned32
_Dot1agXCfmMepDbConvertedIndex_Object=MibTableColumn
dot1agXCfmMepDbConvertedIndex=_Dot1agXCfmMepDbConvertedIndex_Object((1,3,6,1,4,1,164,3,1,6,1,3,10,1,2),_Dot1agXCfmMepDbConvertedIndex_Type())
dot1agXCfmMepDbConvertedIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:dot1agXCfmMepDbConvertedIndex.setStatus(_Z)
_Dot1agXCfmMaMepListTable_Object=MibTable
dot1agXCfmMaMepListTable=_Dot1agXCfmMaMepListTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,11))
if mibBuilder.loadTexts:dot1agXCfmMaMepListTable.setStatus(_A)
_Dot1agXCfmMaMepListEntry_Object=MibTableRow
dot1agXCfmMaMepListEntry=_Dot1agXCfmMaMepListEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,11,1))
dot1agXCfmMaMepListEntry.setIndexNames((0,_F,_V),(0,_F,_Y),(0,_F,_y))
if mibBuilder.loadTexts:dot1agXCfmMaMepListEntry.setStatus(_A)
_Dot1agXCfmMaMepListLocalMep_Type=Unsigned32
_Dot1agXCfmMaMepListLocalMep_Object=MibTableColumn
dot1agXCfmMaMepListLocalMep=_Dot1agXCfmMaMepListLocalMep_Object((1,3,6,1,4,1,164,3,1,6,1,3,11,1,1),_Dot1agXCfmMaMepListLocalMep_Type())
dot1agXCfmMaMepListLocalMep.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMaMepListLocalMep.setStatus(_A)
_Dot1agXCfmMaMepListDescr_Type=SnmpAdminString
_Dot1agXCfmMaMepListDescr_Object=MibTableColumn
dot1agXCfmMaMepListDescr=_Dot1agXCfmMaMepListDescr_Object((1,3,6,1,4,1,164,3,1,6,1,3,11,1,2),_Dot1agXCfmMaMepListDescr_Type())
dot1agXCfmMaMepListDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMaMepListDescr.setStatus(_A)
_EthIfOamCfmMip_ObjectIdentity=ObjectIdentity
ethIfOamCfmMip=_EthIfOamCfmMip_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,1,3,12))
_EthIfOamCfmMipTable_Object=MibTable
ethIfOamCfmMipTable=_EthIfOamCfmMipTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,1))
if mibBuilder.loadTexts:ethIfOamCfmMipTable.setStatus(_A)
_EthIfOamCfmMipEntry_Object=MibTableRow
ethIfOamCfmMipEntry=_EthIfOamCfmMipEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,1,1))
ethIfOamCfmMipEntry.setIndexNames((0,_E,_AD),(0,_E,_AE))
if mibBuilder.loadTexts:ethIfOamCfmMipEntry.setStatus(_A)
_EthIfOamCfmMipMdIdx_Type=Unsigned32
_EthIfOamCfmMipMdIdx_Object=MibTableColumn
ethIfOamCfmMipMdIdx=_EthIfOamCfmMipMdIdx_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,1,1,1),_EthIfOamCfmMipMdIdx_Type())
ethIfOamCfmMipMdIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfOamCfmMipMdIdx.setStatus(_A)
_EthIfOamCfmMipIdx_Type=Unsigned32
_EthIfOamCfmMipIdx_Object=MibTableColumn
ethIfOamCfmMipIdx=_EthIfOamCfmMipIdx_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,1,1,2),_EthIfOamCfmMipIdx_Type())
ethIfOamCfmMipIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfOamCfmMipIdx.setStatus(_A)
_EthIfOamCfmMipRowStatus_Type=RowStatus
_EthIfOamCfmMipRowStatus_Object=MibTableColumn
ethIfOamCfmMipRowStatus=_EthIfOamCfmMipRowStatus_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,1,1,3),_EthIfOamCfmMipRowStatus_Type())
ethIfOamCfmMipRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ethIfOamCfmMipRowStatus.setStatus(_A)
_EthIfOamCfmMipBoundedPortIfIndex_Type=InterfaceIndexOrZero
_EthIfOamCfmMipBoundedPortIfIndex_Object=MibTableColumn
ethIfOamCfmMipBoundedPortIfIndex=_EthIfOamCfmMipBoundedPortIfIndex_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,1,1,4),_EthIfOamCfmMipBoundedPortIfIndex_Type())
ethIfOamCfmMipBoundedPortIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ethIfOamCfmMipBoundedPortIfIndex.setStatus(_A)
class _EthIfOamCfmMipFlowType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('uniDirectional',1),(_AF,2)))
_EthIfOamCfmMipFlowType_Type.__name__=_H
_EthIfOamCfmMipFlowType_Object=MibTableColumn
ethIfOamCfmMipFlowType=_EthIfOamCfmMipFlowType_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,1,1,5),_EthIfOamCfmMipFlowType_Type())
ethIfOamCfmMipFlowType.setMaxAccess(_D)
if mibBuilder.loadTexts:ethIfOamCfmMipFlowType.setStatus(_A)
_EthIfOamCfmMipFlowRxIndex_Type=Unsigned32
_EthIfOamCfmMipFlowRxIndex_Object=MibTableColumn
ethIfOamCfmMipFlowRxIndex=_EthIfOamCfmMipFlowRxIndex_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,1,1,6),_EthIfOamCfmMipFlowRxIndex_Type())
ethIfOamCfmMipFlowRxIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ethIfOamCfmMipFlowRxIndex.setStatus(_A)
_EthIfOamCfmMipFlowTxIndex_Type=Unsigned32
_EthIfOamCfmMipFlowTxIndex_Object=MibTableColumn
ethIfOamCfmMipFlowTxIndex=_EthIfOamCfmMipFlowTxIndex_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,1,1,7),_EthIfOamCfmMipFlowTxIndex_Type())
ethIfOamCfmMipFlowTxIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ethIfOamCfmMipFlowTxIndex.setStatus(_A)
_EthIfOamCfmMhfTable_Object=MibTable
ethIfOamCfmMhfTable=_EthIfOamCfmMhfTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,2))
if mibBuilder.loadTexts:ethIfOamCfmMhfTable.setStatus(_A)
_EthIfOamCfmMhfEntry_Object=MibTableRow
ethIfOamCfmMhfEntry=_EthIfOamCfmMhfEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,2,1))
ethIfOamCfmMhfEntry.setIndexNames((0,_E,_AG),(0,_E,_AH),(0,_E,_AI))
if mibBuilder.loadTexts:ethIfOamCfmMhfEntry.setStatus(_A)
_EthIfOamCfmMhfMdIdx_Type=Unsigned32
_EthIfOamCfmMhfMdIdx_Object=MibTableColumn
ethIfOamCfmMhfMdIdx=_EthIfOamCfmMhfMdIdx_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,2,1,1),_EthIfOamCfmMhfMdIdx_Type())
ethIfOamCfmMhfMdIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfOamCfmMhfMdIdx.setStatus(_A)
_EthIfOamCfmMhfMipIdx_Type=Unsigned32
_EthIfOamCfmMhfMipIdx_Object=MibTableColumn
ethIfOamCfmMhfMipIdx=_EthIfOamCfmMhfMipIdx_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,2,1,2),_EthIfOamCfmMhfMipIdx_Type())
ethIfOamCfmMhfMipIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfOamCfmMhfMipIdx.setStatus(_A)
class _EthIfOamCfmMhfIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_EthIfOamCfmMhfIdx_Type.__name__=_J
_EthIfOamCfmMhfIdx_Object=MibTableColumn
ethIfOamCfmMhfIdx=_EthIfOamCfmMhfIdx_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,2,1,3),_EthIfOamCfmMhfIdx_Type())
ethIfOamCfmMhfIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:ethIfOamCfmMhfIdx.setStatus(_A)
_EthIfOamCfmMhfActive_Type=TruthValue
_EthIfOamCfmMhfActive_Object=MibTableColumn
ethIfOamCfmMhfActive=_EthIfOamCfmMhfActive_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,2,1,4),_EthIfOamCfmMhfActive_Type())
ethIfOamCfmMhfActive.setMaxAccess(_T)
if mibBuilder.loadTexts:ethIfOamCfmMhfActive.setStatus(_A)
_EthIfOamCfmMhfOutputPortIfIndex_Type=InterfaceIndexOrZero
_EthIfOamCfmMhfOutputPortIfIndex_Object=MibTableColumn
ethIfOamCfmMhfOutputPortIfIndex=_EthIfOamCfmMhfOutputPortIfIndex_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,2,1,5),_EthIfOamCfmMhfOutputPortIfIndex_Type())
ethIfOamCfmMhfOutputPortIfIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:ethIfOamCfmMhfOutputPortIfIndex.setStatus(_A)
_EthIfOamCfmMhfPrimaryVid_Type=Unsigned32
_EthIfOamCfmMhfPrimaryVid_Object=MibTableColumn
ethIfOamCfmMhfPrimaryVid=_EthIfOamCfmMhfPrimaryVid_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,2,1,6),_EthIfOamCfmMhfPrimaryVid_Type())
ethIfOamCfmMhfPrimaryVid.setMaxAccess(_T)
if mibBuilder.loadTexts:ethIfOamCfmMhfPrimaryVid.setStatus(_A)
_EthIfOamCfmMhfMappingProfile_Type=Unsigned32
_EthIfOamCfmMhfMappingProfile_Object=MibTableColumn
ethIfOamCfmMhfMappingProfile=_EthIfOamCfmMhfMappingProfile_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,2,1,7),_EthIfOamCfmMhfMappingProfile_Type())
ethIfOamCfmMhfMappingProfile.setMaxAccess(_T)
if mibBuilder.loadTexts:ethIfOamCfmMhfMappingProfile.setStatus(_A)
_EthIfOamCfmMhfCosMapping_Type=Unsigned32
_EthIfOamCfmMhfCosMapping_Object=MibTableColumn
ethIfOamCfmMhfCosMapping=_EthIfOamCfmMhfCosMapping_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,2,1,8),_EthIfOamCfmMhfCosMapping_Type())
ethIfOamCfmMhfCosMapping.setMaxAccess(_T)
if mibBuilder.loadTexts:ethIfOamCfmMhfCosMapping.setStatus(_A)
_EthIfOamCfmMhfCosMappingProfile_Type=Unsigned32
_EthIfOamCfmMhfCosMappingProfile_Object=MibTableColumn
ethIfOamCfmMhfCosMappingProfile=_EthIfOamCfmMhfCosMappingProfile_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,2,1,9),_EthIfOamCfmMhfCosMappingProfile_Type())
ethIfOamCfmMhfCosMappingProfile.setMaxAccess(_T)
if mibBuilder.loadTexts:ethIfOamCfmMhfCosMappingProfile.setStatus(_A)
_EthIfOamCfmMhfQBlock_Type=ObjectIdentifier
_EthIfOamCfmMhfQBlock_Object=MibTableColumn
ethIfOamCfmMhfQBlock=_EthIfOamCfmMhfQBlock_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,2,1,10),_EthIfOamCfmMhfQBlock_Type())
ethIfOamCfmMhfQBlock.setMaxAccess(_T)
if mibBuilder.loadTexts:ethIfOamCfmMhfQBlock.setStatus(_A)
_EthIfOamCfmMhfFixedQueueMapping_Type=Unsigned32
_EthIfOamCfmMhfFixedQueueMapping_Object=MibTableColumn
ethIfOamCfmMhfFixedQueueMapping=_EthIfOamCfmMhfFixedQueueMapping_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,2,1,11),_EthIfOamCfmMhfFixedQueueMapping_Type())
ethIfOamCfmMhfFixedQueueMapping.setMaxAccess(_T)
if mibBuilder.loadTexts:ethIfOamCfmMhfFixedQueueMapping.setStatus(_A)
_EthIfOamCfmMhfQueueMappingProfile_Type=Unsigned32
_EthIfOamCfmMhfQueueMappingProfile_Object=MibTableColumn
ethIfOamCfmMhfQueueMappingProfile=_EthIfOamCfmMhfQueueMappingProfile_Object((1,3,6,1,4,1,164,3,1,6,1,3,12,2,1,12),_EthIfOamCfmMhfQueueMappingProfile_Type())
ethIfOamCfmMhfQueueMappingProfile.setMaxAccess(_T)
if mibBuilder.loadTexts:ethIfOamCfmMhfQueueMappingProfile.setStatus(_A)
_EthOamMip_ObjectIdentity=ObjectIdentity
ethOamMip=_EthOamMip_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,1,3,13))
_EthOamMipTable_Object=MibTable
ethOamMipTable=_EthOamMipTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,13,1))
if mibBuilder.loadTexts:ethOamMipTable.setStatus(_A)
_EthOamMipEntry_Object=MibTableRow
ethOamMipEntry=_EthOamMipEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,13,1,1))
ethOamMipEntry.setIndexNames((0,_E,_AJ),(0,_E,_AK))
if mibBuilder.loadTexts:ethOamMipEntry.setStatus(_A)
_EthOamMipIfIndex_Type=Unsigned32
_EthOamMipIfIndex_Object=MibTableColumn
ethOamMipIfIndex=_EthOamMipIfIndex_Object((1,3,6,1,4,1,164,3,1,6,1,3,13,1,1,1),_EthOamMipIfIndex_Type())
ethOamMipIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ethOamMipIfIndex.setStatus(_A)
_EthOamMipVlanId_Type=Unsigned32
_EthOamMipVlanId_Object=MibTableColumn
ethOamMipVlanId=_EthOamMipVlanId_Object((1,3,6,1,4,1,164,3,1,6,1,3,13,1,1,2),_EthOamMipVlanId_Type())
ethOamMipVlanId.setMaxAccess(_I)
if mibBuilder.loadTexts:ethOamMipVlanId.setStatus(_A)
_EthOamMipMdLevel_Type=Unsigned32
_EthOamMipMdLevel_Object=MibTableColumn
ethOamMipMdLevel=_EthOamMipMdLevel_Object((1,3,6,1,4,1,164,3,1,6,1,3,13,1,1,3),_EthOamMipMdLevel_Type())
ethOamMipMdLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamMipMdLevel.setStatus(_A)
class _AgnAutoMipAssign_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('manual',2)))
_AgnAutoMipAssign_Type.__name__=_H
_AgnAutoMipAssign_Object=MibScalar
agnAutoMipAssign=_AgnAutoMipAssign_Object((1,3,6,1,4,1,164,3,1,6,1,3,13,2),_AgnAutoMipAssign_Type())
agnAutoMipAssign.setMaxAccess(_T)
if mibBuilder.loadTexts:agnAutoMipAssign.setStatus(_A)
_EthIfOamCfmSumMipMep_ObjectIdentity=ObjectIdentity
ethIfOamCfmSumMipMep=_EthIfOamCfmSumMipMep_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,1,3,14))
if mibBuilder.loadTexts:ethIfOamCfmSumMipMep.setStatus(_A)
_Dot1agXCfmMaNetTable_Object=MibTable
dot1agXCfmMaNetTable=_Dot1agXCfmMaNetTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,15))
if mibBuilder.loadTexts:dot1agXCfmMaNetTable.setStatus(_A)
_Dot1agXCfmMaNetEntry_Object=MibTableRow
dot1agXCfmMaNetEntry=_Dot1agXCfmMaNetEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,15,1))
dot1agXCfmMaNetEntry.setIndexNames((0,_F,_V),(0,_F,_Y))
if mibBuilder.loadTexts:dot1agXCfmMaNetEntry.setStatus(_A)
_Dot1agXCfmMaNetServiceIdName_Type=SnmpAdminString
_Dot1agXCfmMaNetServiceIdName_Object=MibTableColumn
dot1agXCfmMaNetServiceIdName=_Dot1agXCfmMaNetServiceIdName_Object((1,3,6,1,4,1,164,3,1,6,1,3,15,1,1),_Dot1agXCfmMaNetServiceIdName_Type())
dot1agXCfmMaNetServiceIdName.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1agXCfmMaNetServiceIdName.setStatus(_A)
class _Dot1agXCfmMaNetIfStatusTlv_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_v,1),(_u,2)))
_Dot1agXCfmMaNetIfStatusTlv_Type.__name__=_H
_Dot1agXCfmMaNetIfStatusTlv_Object=MibTableColumn
dot1agXCfmMaNetIfStatusTlv=_Dot1agXCfmMaNetIfStatusTlv_Object((1,3,6,1,4,1,164,3,1,6,1,3,15,1,2),_Dot1agXCfmMaNetIfStatusTlv_Type())
dot1agXCfmMaNetIfStatusTlv.setMaxAccess(_D)
if mibBuilder.loadTexts:dot1agXCfmMaNetIfStatusTlv.setStatus(_A)
_EthOamMepFlowsTable_Object=MibTable
ethOamMepFlowsTable=_EthOamMepFlowsTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,16))
if mibBuilder.loadTexts:ethOamMepFlowsTable.setStatus(_A)
_EthOamMepFlowsEntry_Object=MibTableRow
ethOamMepFlowsEntry=_EthOamMepFlowsEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,16,1))
ethOamMepFlowsEntry.setIndexNames((0,_F,_V),(0,_F,_Y),(0,_F,_c),(0,_E,_AL),(0,_E,_AM),(0,_E,_AN))
if mibBuilder.loadTexts:ethOamMepFlowsEntry.setStatus(_A)
class _EthOamMepFlowType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('uniDirectionalRx',1),('uniDirectionalTx',2),(_AF,3)))
_EthOamMepFlowType_Type.__name__=_H
_EthOamMepFlowType_Object=MibTableColumn
ethOamMepFlowType=_EthOamMepFlowType_Object((1,3,6,1,4,1,164,3,1,6,1,3,16,1,1),_EthOamMepFlowType_Type())
ethOamMepFlowType.setMaxAccess(_I)
if mibBuilder.loadTexts:ethOamMepFlowType.setStatus(_A)
_EthOamMepFlowIndex1_Type=Unsigned32
_EthOamMepFlowIndex1_Object=MibTableColumn
ethOamMepFlowIndex1=_EthOamMepFlowIndex1_Object((1,3,6,1,4,1,164,3,1,6,1,3,16,1,2),_EthOamMepFlowIndex1_Type())
ethOamMepFlowIndex1.setMaxAccess(_I)
if mibBuilder.loadTexts:ethOamMepFlowIndex1.setStatus(_A)
_EthOamMepFlowIndex2_Type=Unsigned32
_EthOamMepFlowIndex2_Object=MibTableColumn
ethOamMepFlowIndex2=_EthOamMepFlowIndex2_Object((1,3,6,1,4,1,164,3,1,6,1,3,16,1,3),_EthOamMepFlowIndex2_Type())
ethOamMepFlowIndex2.setMaxAccess(_I)
if mibBuilder.loadTexts:ethOamMepFlowIndex2.setStatus(_A)
_EthOamMepFlowsRowStatus_Type=RowStatus
_EthOamMepFlowsRowStatus_Object=MibTableColumn
ethOamMepFlowsRowStatus=_EthOamMepFlowsRowStatus_Object((1,3,6,1,4,1,164,3,1,6,1,3,16,1,4),_EthOamMepFlowsRowStatus_Type())
ethOamMepFlowsRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ethOamMepFlowsRowStatus.setStatus(_A)
_EthOamConfigTable_Object=MibTable
ethOamConfigTable=_EthOamConfigTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,17))
if mibBuilder.loadTexts:ethOamConfigTable.setStatus(_A)
_EthOamConfigEntry_Object=MibTableRow
ethOamConfigEntry=_EthOamConfigEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,17,1))
ethOamConfigEntry.setIndexNames((0,_E,_AO))
if mibBuilder.loadTexts:ethOamConfigEntry.setStatus(_A)
_EthOamConfigIdx_Type=Unsigned32
_EthOamConfigIdx_Object=MibTableColumn
ethOamConfigIdx=_EthOamConfigIdx_Object((1,3,6,1,4,1,164,3,1,6,1,3,17,1,1),_EthOamConfigIdx_Type())
ethOamConfigIdx.setMaxAccess(_I)
if mibBuilder.loadTexts:ethOamConfigIdx.setStatus(_A)
class _EthOamConfigAlarmType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('legacy',1),('soam',2)))
_EthOamConfigAlarmType_Type.__name__=_H
_EthOamConfigAlarmType_Object=MibTableColumn
ethOamConfigAlarmType=_EthOamConfigAlarmType_Object((1,3,6,1,4,1,164,3,1,6,1,3,17,1,2),_EthOamConfigAlarmType_Type())
ethOamConfigAlarmType.setMaxAccess(_T)
if mibBuilder.loadTexts:ethOamConfigAlarmType.setStatus(_A)
class _EthOamConfigAvailabilityDeltaT_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1),ValueRangeConstraint(2,2),ValueRangeConstraint(3,3),ValueRangeConstraint(4,4),ValueRangeConstraint(5,5),ValueRangeConstraint(6,6),ValueRangeConstraint(10,10),ValueRangeConstraint(12,12),ValueRangeConstraint(15,15),ValueRangeConstraint(20,20))
_EthOamConfigAvailabilityDeltaT_Type.__name__=_J
_EthOamConfigAvailabilityDeltaT_Object=MibTableColumn
ethOamConfigAvailabilityDeltaT=_EthOamConfigAvailabilityDeltaT_Object((1,3,6,1,4,1,164,3,1,6,1,3,17,1,3),_EthOamConfigAvailabilityDeltaT_Type())
ethOamConfigAvailabilityDeltaT.setMaxAccess(_T)
if mibBuilder.loadTexts:ethOamConfigAvailabilityDeltaT.setStatus(_A)
if mibBuilder.loadTexts:ethOamConfigAvailabilityDeltaT.setUnits(_S)
class _EthOamConfigAvailabilityNumDeltaTs_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_EthOamConfigAvailabilityNumDeltaTs_Type.__name__=_J
_EthOamConfigAvailabilityNumDeltaTs_Object=MibTableColumn
ethOamConfigAvailabilityNumDeltaTs=_EthOamConfigAvailabilityNumDeltaTs_Object((1,3,6,1,4,1,164,3,1,6,1,3,17,1,4),_EthOamConfigAvailabilityNumDeltaTs_Type())
ethOamConfigAvailabilityNumDeltaTs.setMaxAccess(_T)
if mibBuilder.loadTexts:ethOamConfigAvailabilityNumDeltaTs.setStatus(_A)
class _EthOamConfigAvailabilityFwdFlrThreshold_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_EthOamConfigAvailabilityFwdFlrThreshold_Type.__name__=_J
_EthOamConfigAvailabilityFwdFlrThreshold_Object=MibTableColumn
ethOamConfigAvailabilityFwdFlrThreshold=_EthOamConfigAvailabilityFwdFlrThreshold_Object((1,3,6,1,4,1,164,3,1,6,1,3,17,1,5),_EthOamConfigAvailabilityFwdFlrThreshold_Type())
ethOamConfigAvailabilityFwdFlrThreshold.setMaxAccess(_T)
if mibBuilder.loadTexts:ethOamConfigAvailabilityFwdFlrThreshold.setStatus(_A)
if mibBuilder.loadTexts:ethOamConfigAvailabilityFwdFlrThreshold.setUnits('percents')
class _EthOamConfigAvailabilityBckFlrThreshold_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_EthOamConfigAvailabilityBckFlrThreshold_Type.__name__=_J
_EthOamConfigAvailabilityBckFlrThreshold_Object=MibTableColumn
ethOamConfigAvailabilityBckFlrThreshold=_EthOamConfigAvailabilityBckFlrThreshold_Object((1,3,6,1,4,1,164,3,1,6,1,3,17,1,6),_EthOamConfigAvailabilityBckFlrThreshold_Type())
ethOamConfigAvailabilityBckFlrThreshold.setMaxAccess(_T)
if mibBuilder.loadTexts:ethOamConfigAvailabilityBckFlrThreshold.setStatus(_A)
if mibBuilder.loadTexts:ethOamConfigAvailabilityBckFlrThreshold.setUnits('percents')
class _EthOamConfigMdLevelMips_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('mdlLevel0',0),('mdlLevel1',1),('mdlLevel2',2),('mdlLevel3',3),('mdlLevel4',4),('mdlLevel5',5),('mdlLevel6',6),('mdlLevel7',7)))
_EthOamConfigMdLevelMips_Type.__name__=_g
_EthOamConfigMdLevelMips_Object=MibTableColumn
ethOamConfigMdLevelMips=_EthOamConfigMdLevelMips_Object((1,3,6,1,4,1,164,3,1,6,1,3,17,1,7),_EthOamConfigMdLevelMips_Type())
ethOamConfigMdLevelMips.setMaxAccess(_T)
if mibBuilder.loadTexts:ethOamConfigMdLevelMips.setStatus(_A)
_EthOamMepStats_ObjectIdentity=ObjectIdentity
ethOamMepStats=_EthOamMepStats_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,1,3,18))
_EthOamMepCurrentTable_Object=MibTable
ethOamMepCurrentTable=_EthOamMepCurrentTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,1))
if mibBuilder.loadTexts:ethOamMepCurrentTable.setStatus(_A)
_EthOamMepCurrentEntry_Object=MibTableRow
ethOamMepCurrentEntry=_EthOamMepCurrentEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,1,1))
ethOamMepCurrentEntry.setIndexNames((0,_F,_V),(0,_F,_Y),(0,_F,_c))
if mibBuilder.loadTexts:ethOamMepCurrentEntry.setStatus(_A)
_EthOamMepCurrentCcmTx_Type=Counter64
_EthOamMepCurrentCcmTx_Object=MibTableColumn
ethOamMepCurrentCcmTx=_EthOamMepCurrentCcmTx_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,1,1,1),_EthOamMepCurrentCcmTx_Type())
ethOamMepCurrentCcmTx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamMepCurrentCcmTx.setStatus(_A)
_EthOamMepIntervalTable_Object=MibTable
ethOamMepIntervalTable=_EthOamMepIntervalTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,2))
if mibBuilder.loadTexts:ethOamMepIntervalTable.setStatus(_A)
_EthOamMepIntervalEntry_Object=MibTableRow
ethOamMepIntervalEntry=_EthOamMepIntervalEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,2,1))
ethOamMepIntervalEntry.setIndexNames((0,_F,_V),(0,_F,_Y),(0,_F,_c),(0,_E,_AP))
if mibBuilder.loadTexts:ethOamMepIntervalEntry.setStatus(_A)
class _EthOamMepIntervalNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_EthOamMepIntervalNumber_Type.__name__=_J
_EthOamMepIntervalNumber_Object=MibTableColumn
ethOamMepIntervalNumber=_EthOamMepIntervalNumber_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,2,1,1),_EthOamMepIntervalNumber_Type())
ethOamMepIntervalNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:ethOamMepIntervalNumber.setStatus(_A)
_EthOamMepIntervalValidData_Type=TruthValue
_EthOamMepIntervalValidData_Object=MibTableColumn
ethOamMepIntervalValidData=_EthOamMepIntervalValidData_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,2,1,2),_EthOamMepIntervalValidData_Type())
ethOamMepIntervalValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamMepIntervalValidData.setStatus(_A)
class _EthOamMepIntervalDuration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_EthOamMepIntervalDuration_Type.__name__=_J
_EthOamMepIntervalDuration_Object=MibTableColumn
ethOamMepIntervalDuration=_EthOamMepIntervalDuration_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,2,1,3),_EthOamMepIntervalDuration_Type())
ethOamMepIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamMepIntervalDuration.setStatus(_A)
if mibBuilder.loadTexts:ethOamMepIntervalDuration.setUnits(_S)
_EthOamMepIntervalTimeStamp_Type=DateAndTime
_EthOamMepIntervalTimeStamp_Object=MibTableColumn
ethOamMepIntervalTimeStamp=_EthOamMepIntervalTimeStamp_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,2,1,4),_EthOamMepIntervalTimeStamp_Type())
ethOamMepIntervalTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamMepIntervalTimeStamp.setStatus(_A)
_EthOamMepIntervalCcmTx_Type=Counter64
_EthOamMepIntervalCcmTx_Object=MibTableColumn
ethOamMepIntervalCcmTx=_EthOamMepIntervalCcmTx_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,2,1,5),_EthOamMepIntervalCcmTx_Type())
ethOamMepIntervalCcmTx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamMepIntervalCcmTx.setStatus(_A)
_EthOamRMepStatsTable_Object=MibTable
ethOamRMepStatsTable=_EthOamRMepStatsTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,3))
if mibBuilder.loadTexts:ethOamRMepStatsTable.setStatus(_A)
_EthOamRMepStatsEntry_Object=MibTableRow
ethOamRMepStatsEntry=_EthOamRMepStatsEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,3,1))
ethOamRMepStatsEntry.setIndexNames((0,_F,_V),(0,_F,_Y),(0,_F,_c),(0,_E,_n))
if mibBuilder.loadTexts:ethOamRMepStatsEntry.setStatus(_A)
_EthOamRMepStatsRMepId_Type=Dot1agCfmMepId
_EthOamRMepStatsRMepId_Object=MibTableColumn
ethOamRMepStatsRMepId=_EthOamRMepStatsRMepId_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,3,1,1),_EthOamRMepStatsRMepId_Type())
ethOamRMepStatsRMepId.setMaxAccess(_I)
if mibBuilder.loadTexts:ethOamRMepStatsRMepId.setStatus(_A)
_EthOamRMepStatsCcmRx_Type=Counter64
_EthOamRMepStatsCcmRx_Object=MibTableColumn
ethOamRMepStatsCcmRx=_EthOamRMepStatsCcmRx_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,3,1,2),_EthOamRMepStatsCcmRx_Type())
ethOamRMepStatsCcmRx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamRMepStatsCcmRx.setStatus(_A)
class _EthOamRMepStatsClearCmd_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_i,2),(_j,3)))
_EthOamRMepStatsClearCmd_Type.__name__=_H
_EthOamRMepStatsClearCmd_Object=MibTableColumn
ethOamRMepStatsClearCmd=_EthOamRMepStatsClearCmd_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,3,1,3),_EthOamRMepStatsClearCmd_Type())
ethOamRMepStatsClearCmd.setMaxAccess(_T)
if mibBuilder.loadTexts:ethOamRMepStatsClearCmd.setStatus(_A)
_EthOamRMepCurrentTable_Object=MibTable
ethOamRMepCurrentTable=_EthOamRMepCurrentTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,4))
if mibBuilder.loadTexts:ethOamRMepCurrentTable.setStatus(_A)
_EthOamRMepCurrentEntry_Object=MibTableRow
ethOamRMepCurrentEntry=_EthOamRMepCurrentEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,4,1))
ethOamRMepCurrentEntry.setIndexNames((0,_F,_V),(0,_F,_Y),(0,_F,_c),(0,_E,_n))
if mibBuilder.loadTexts:ethOamRMepCurrentEntry.setStatus(_A)
_EthOamRMepCurrentCcmRx_Type=Counter64
_EthOamRMepCurrentCcmRx_Object=MibTableColumn
ethOamRMepCurrentCcmRx=_EthOamRMepCurrentCcmRx_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,4,1,1),_EthOamRMepCurrentCcmRx_Type())
ethOamRMepCurrentCcmRx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamRMepCurrentCcmRx.setStatus(_A)
_EthOamRMepIntervalTable_Object=MibTable
ethOamRMepIntervalTable=_EthOamRMepIntervalTable_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,5))
if mibBuilder.loadTexts:ethOamRMepIntervalTable.setStatus(_A)
_EthOamRMepIntervalEntry_Object=MibTableRow
ethOamRMepIntervalEntry=_EthOamRMepIntervalEntry_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,5,1))
ethOamRMepIntervalEntry.setIndexNames((0,_F,_V),(0,_F,_Y),(0,_F,_c),(0,_E,_n),(0,_E,_AQ))
if mibBuilder.loadTexts:ethOamRMepIntervalEntry.setStatus(_A)
class _EthOamRMepIntervalNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_EthOamRMepIntervalNumber_Type.__name__=_J
_EthOamRMepIntervalNumber_Object=MibTableColumn
ethOamRMepIntervalNumber=_EthOamRMepIntervalNumber_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,5,1,1),_EthOamRMepIntervalNumber_Type())
ethOamRMepIntervalNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:ethOamRMepIntervalNumber.setStatus(_A)
_EthOamRMepIntervalValidData_Type=TruthValue
_EthOamRMepIntervalValidData_Object=MibTableColumn
ethOamRMepIntervalValidData=_EthOamRMepIntervalValidData_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,5,1,2),_EthOamRMepIntervalValidData_Type())
ethOamRMepIntervalValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamRMepIntervalValidData.setStatus(_A)
class _EthOamRMepIntervalDuration_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_EthOamRMepIntervalDuration_Type.__name__=_J
_EthOamRMepIntervalDuration_Object=MibTableColumn
ethOamRMepIntervalDuration=_EthOamRMepIntervalDuration_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,5,1,3),_EthOamRMepIntervalDuration_Type())
ethOamRMepIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamRMepIntervalDuration.setStatus(_A)
if mibBuilder.loadTexts:ethOamRMepIntervalDuration.setUnits(_S)
_EthOamRMepIntervalTimeStamp_Type=DateAndTime
_EthOamRMepIntervalTimeStamp_Object=MibTableColumn
ethOamRMepIntervalTimeStamp=_EthOamRMepIntervalTimeStamp_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,5,1,4),_EthOamRMepIntervalTimeStamp_Type())
ethOamRMepIntervalTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamRMepIntervalTimeStamp.setStatus(_A)
_EthOamRMepIntervalCcmRx_Type=Counter64
_EthOamRMepIntervalCcmRx_Object=MibTableColumn
ethOamRMepIntervalCcmRx=_EthOamRMepIntervalCcmRx_Object((1,3,6,1,4,1,164,3,1,6,1,3,18,5,1,5),_EthOamRMepIntervalCcmRx_Type())
ethOamRMepIntervalCcmRx.setMaxAccess(_B)
if mibBuilder.loadTexts:ethOamRMepIntervalCcmRx.setStatus(_A)
ethOamCfmDefectCondition=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,1))
if mibBuilder.loadTexts:ethOamCfmDefectCondition.setStatus(_A)
oamCfmMepAis=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,4))
oamCfmMepAis.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_a),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmMepAis.setStatus(_A)
oamCfmMepLck=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,5))
oamCfmMepLck.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_a),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmMepLck.setStatus(_A)
oamCfmMepMismatch=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,6))
oamCfmMepMismatch.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_a),(_F,_R),(_F,_Q),(_E,_AR)))
if mibBuilder.loadTexts:oamCfmMepMismatch.setStatus(_A)
oamCfmRmepLoc=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,7))
oamCfmRmepLoc.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_a),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmRmepLoc.setStatus(_A)
oamCfmRmepRdi=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,8))
oamCfmRmepRdi.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_a),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmRmepRdi.setStatus(_A)
oamCfmDestNeDelayTca=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,9))
oamCfmDestNeDelayTca.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_U),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmDestNeDelayTca.setStatus(_A)
oamCfmDestNeDelayTcaOff=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,10))
oamCfmDestNeDelayTcaOff.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_U),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmDestNeDelayTcaOff.setStatus(_A)
oamCfmDestNeDelayVarTca=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,11))
oamCfmDestNeDelayVarTca.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_U),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmDestNeDelayVarTca.setStatus(_A)
oamCfmDestNeDelayVarTcaOff=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,12))
oamCfmDestNeDelayVarTcaOff.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_U),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmDestNeDelayVarTcaOff.setStatus(_A)
oamCfmDestNeLossRatioTca=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,13))
oamCfmDestNeLossRatioTca.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_U),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmDestNeLossRatioTca.setStatus(_A)
oamCfmDestNeLossRatioTcaOff=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,14))
oamCfmDestNeLossRatioTcaOff.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_U),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmDestNeLossRatioTcaOff.setStatus(_A)
oamCfmDestNeLossRatioTcaFe=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,15))
oamCfmDestNeLossRatioTcaFe.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_U),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmDestNeLossRatioTcaFe.setStatus(_A)
oamCfmDestNeLossRatioTcaFeOff=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,16))
oamCfmDestNeLossRatioTcaFeOff.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_U),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmDestNeLossRatioTcaFeOff.setStatus(_A)
oamCfmDestNeUnavailRatioTca=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,17))
oamCfmDestNeUnavailRatioTca.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_U),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmDestNeUnavailRatioTca.setStatus(_A)
oamCfmDestNeUnavailRatioTcaOff=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,18))
oamCfmDestNeUnavailRatioTcaOff.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_U),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmDestNeUnavailRatioTcaOff.setStatus(_A)
oamCfmDestNeUnavailRatioTcaFe=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,19))
oamCfmDestNeUnavailRatioTcaFe.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_U),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmDestNeUnavailRatioTcaFe.setStatus(_A)
oamCfmDestNeUnavailRatioTcaFeOff=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,20))
oamCfmDestNeUnavailRatioTcaFeOff.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_U),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmDestNeUnavailRatioTcaFeOff.setStatus(_A)
oamCfmMepDefXconCCM=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,21))
oamCfmMepDefXconCCM.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_a),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmMepDefXconCCM.setStatus(_A)
oamCfmMepDefErrorCCM=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,22))
oamCfmMepDefErrorCCM.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_a),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmMepDefErrorCCM.setStatus(_A)
oamCfmRmepDefRemoteCCM=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,23))
oamCfmRmepDefRemoteCCM.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_a),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmRmepDefRemoteCCM.setStatus(_A)
oamCfmRmepDefRDICCM=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,24))
oamCfmRmepDefRDICCM.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_a),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmRmepDefRDICCM.setStatus(_A)
oamCfmRmepDefMACstatus=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,25))
oamCfmRmepDefMACstatus.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_E,_a),(_F,_R),(_F,_Q)))
if mibBuilder.loadTexts:oamCfmRmepDefMACstatus.setStatus(_A)
systemCfmSoamRxPacketDropped=NotificationType((1,3,6,1,4,1,164,3,1,6,1,3,0,26))
systemCfmSoamRxPacketDropped.setObjects(*((_C,_O),(_C,_K),(_C,_M),(_C,_N),(_C,_L),(_C,_P),(_A1,'sysName')))
if mibBuilder.loadTexts:systemCfmSoamRxPacketDropped.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'EthOamBinCounterType':EthOamBinCounterType,'ethIfOamCfm':ethIfOamCfm,'ethIfOamCfmEvents':ethIfOamCfmEvents,'ethOamCfmDefectCondition':ethOamCfmDefectCondition,'oamCfmMepAis':oamCfmMepAis,'oamCfmMepLck':oamCfmMepLck,'oamCfmMepMismatch':oamCfmMepMismatch,'oamCfmRmepLoc':oamCfmRmepLoc,'oamCfmRmepRdi':oamCfmRmepRdi,'oamCfmDestNeDelayTca':oamCfmDestNeDelayTca,'oamCfmDestNeDelayTcaOff':oamCfmDestNeDelayTcaOff,'oamCfmDestNeDelayVarTca':oamCfmDestNeDelayVarTca,'oamCfmDestNeDelayVarTcaOff':oamCfmDestNeDelayVarTcaOff,'oamCfmDestNeLossRatioTca':oamCfmDestNeLossRatioTca,'oamCfmDestNeLossRatioTcaOff':oamCfmDestNeLossRatioTcaOff,'oamCfmDestNeLossRatioTcaFe':oamCfmDestNeLossRatioTcaFe,'oamCfmDestNeLossRatioTcaFeOff':oamCfmDestNeLossRatioTcaFeOff,'oamCfmDestNeUnavailRatioTca':oamCfmDestNeUnavailRatioTca,'oamCfmDestNeUnavailRatioTcaOff':oamCfmDestNeUnavailRatioTcaOff,'oamCfmDestNeUnavailRatioTcaFe':oamCfmDestNeUnavailRatioTcaFe,'oamCfmDestNeUnavailRatioTcaFeOff':oamCfmDestNeUnavailRatioTcaFeOff,'oamCfmMepDefXconCCM':oamCfmMepDefXconCCM,'oamCfmMepDefErrorCCM':oamCfmMepDefErrorCCM,'oamCfmRmepDefRemoteCCM':oamCfmRmepDefRemoteCCM,'oamCfmRmepDefRDICCM':oamCfmRmepDefRDICCM,'oamCfmRmepDefMACstatus':oamCfmRmepDefMACstatus,'systemCfmSoamRxPacketDropped':systemCfmSoamRxPacketDropped,'radMepTable':radMepTable,'radMepEntry':radMepEntry,_W:radOamIdx1,_b:radOamEvcIdx,_X:radMepIdx,'radMepRowStatus':radMepRowStatus,'radMepLocalMepId':radMepLocalMepId,'radMepRemoteMepId':radMepRemoteMepId,'radMepOamMode':radMepOamMode,'radMepContinuityVerMode':radMepContinuityVerMode,'radMepMeLevel':radMepMeLevel,'radMepOamDestAddrType':radMepOamDestAddrType,'radMepOamDestMacAddr':radMepOamDestMacAddr,'radMepDefaultPriority':radMepDefaultPriority,'radMepCcStatus':radMepCcStatus,'radMepOamProtocol':radMepOamProtocol,'radMepMdId':radMepMdId,'radMepMaFormat':radMepMaFormat,'radMepMaName':radMepMaName,'radMepSpVlanId':radMepSpVlanId,'radMepCcInterval':radMepCcInterval,'radMepTransmitLbmDestMacAddress':radMepTransmitLbmDestMacAddress,'radMepTransmitLbmDestMepId':radMepTransmitLbmDestMepId,'radMepTransmitLbmDestIsMepId':radMepTransmitLbmDestIsMepId,'radMepTransmitLbmMassages':radMepTransmitLbmMassages,'radMepTransmitLbmVlanPriority':radMepTransmitLbmVlanPriority,'radMepTransmitLbmVlanDropEnable':radMepTransmitLbmVlanDropEnable,'radMepLbrIn':radMepLbrIn,'radMepLbrInOutOfOrder':radMepLbrInOutOfOrder,'radMepLbmOut':radMepLbmOut,'radMepTransmitLtmTargetMacAddress':radMepTransmitLtmTargetMacAddress,'radMepTransmitLtmTargetMepId':radMepTransmitLtmTargetMepId,'radMepTransmitLtmTargetIsMepId':radMepTransmitLtmTargetIsMepId,'radMepTransmitLtmTtl':radMepTransmitLtmTtl,'radMepTransmitLtmActivationCmd':radMepTransmitLtmActivationCmd,'ethOamService':ethOamService,'ethOamServiceTable':ethOamServiceTable,'ethOamServiceEntry':ethOamServiceEntry,_d:ethOamServiceIdx,'ethOamServiceRowStatus':ethOamServiceRowStatus,'ethOamServicePriority':ethOamServicePriority,'ethOamServicePmEnable':ethOamServicePmEnable,'ethOamServiceFrameLossRatioThresh':ethOamServiceFrameLossRatioThresh,'ethOamServiceDelayThresh':ethOamServiceDelayThresh,'ethOamServiceDelayVarThresh':ethOamServiceDelayVarThresh,'ethOamServiceUnavailRatioThresh':ethOamServiceUnavailRatioThresh,'ethOamServiceTxFrames':ethOamServiceTxFrames,'ethOamServiceOverflowTxFrames':ethOamServiceOverflowTxFrames,'ethOamServiceFarEndFrameLoss':ethOamServiceFarEndFrameLoss,'ethOamServiceOverflowFarEndFrameLoss':ethOamServiceOverflowFarEndFrameLoss,'ethOamServiceFarEndFrameLossRatio':ethOamServiceFarEndFrameLossRatio,'ethOamServiceElapsedTime':ethOamServiceElapsedTime,'ethOamServiceUnavailSec':ethOamServiceUnavailSec,'ethOamServiceUnavailRatio':ethOamServiceUnavailRatio,'ethOamServiceFramesAboveDelay':ethOamServiceFramesAboveDelay,'ethOamServiceOverflowFramesAboveDelay':ethOamServiceOverflowFramesAboveDelay,'ethOamServiceFramesAboveDelayVar':ethOamServiceFramesAboveDelayVar,'ethOamServiceOverflowFramesAboveDelayVar':ethOamServiceOverflowFramesAboveDelayVar,'ethOamServiceCurrentDelay':ethOamServiceCurrentDelay,'ethOamServiceCurrentDelayVariation':ethOamServiceCurrentDelayVariation,'ethOamServiceResetCounters':ethOamServiceResetCounters,'ethOamServiceNearEndFrameLoss':ethOamServiceNearEndFrameLoss,'ethOamServiceOverflowNearEndFrameLoss':ethOamServiceOverflowNearEndFrameLoss,'ethOamServiceNearEndFrameLossRatio':ethOamServiceNearEndFrameLossRatio,'ethOamServiceDmmInterval':ethOamServiceDmmInterval,'ethOamServiceLmmInterval':ethOamServiceLmmInterval,'ethOamServiceTxLmm':ethOamServiceTxLmm,'ethOamServiceOverflowTxLmm':ethOamServiceOverflowTxLmm,'ethOamServiceTxDmm':ethOamServiceTxDmm,'ethOamServiceOverflowTxDmm':ethOamServiceOverflowTxDmm,'ethOamServiceRxLmr':ethOamServiceRxLmr,'ethOamServiceOverflowRxLmr':ethOamServiceOverflowRxLmr,'ethOamServiceRxDmr':ethOamServiceRxDmr,'ethOamServiceOverflowRxDmr':ethOamServiceOverflowRxDmr,'ethOamServiceTxForward':ethOamServiceTxForward,'ethOamServiceOverflowTxForward':ethOamServiceOverflowTxForward,'ethOamServiceRxForward':ethOamServiceRxForward,'ethOamServiceOverflowRxForward':ethOamServiceOverflowRxForward,'ethOamServiceTxBackward':ethOamServiceTxBackward,'ethOamServiceOverflowTxBackward':ethOamServiceOverflowTxBackward,'ethOamServiceRxBackward':ethOamServiceRxBackward,'ethOamServiceOverflowRxBackward':ethOamServiceOverflowRxBackward,'ethOamServiceConvertedIndex':ethOamServiceConvertedIndex,'ethOamSvcCurrentStatTable':ethOamSvcCurrentStatTable,'ethOamSvcCurrentStatEntry':ethOamSvcCurrentStatEntry,'ethOamSvcCurrFramesAboveDelayThresh':ethOamSvcCurrFramesAboveDelayThresh,'ethOamSvcCurrFramesBelowDelayThresh':ethOamSvcCurrFramesBelowDelayThresh,'ethOamSvcCurrFramesAboveDVarThresh':ethOamSvcCurrFramesAboveDVarThresh,'ethOamSvcCurrFramesBelowDVarThresh':ethOamSvcCurrFramesBelowDVarThresh,'ethOamSvcCurrFramesTxCounter':ethOamSvcCurrFramesTxCounter,'ethOamSvcCurrFarEndFramesLossCounter':ethOamSvcCurrFarEndFramesLossCounter,'ethOamSvcCurrMinRoundTripDelay':ethOamSvcCurrMinRoundTripDelay,'ethOamSvcCurrMaxRoundTripDelay':ethOamSvcCurrMaxRoundTripDelay,'ethOamSvcCurrAvgRoundTripDelay':ethOamSvcCurrAvgRoundTripDelay,'ethOamSvcCurrMaxRoundTripDVar':ethOamSvcCurrMaxRoundTripDVar,'ethOamSvcCurrAvgRoundTripDVar':ethOamSvcCurrAvgRoundTripDVar,'ethOamSvcCurrElapsedTime':ethOamSvcCurrElapsedTime,'ethOamSvcCurrUnavailSec':ethOamSvcCurrUnavailSec,'ethOamSvcCurrLmmTxFrames':ethOamSvcCurrLmmTxFrames,'ethOamSvcCurrDmmTxFrames':ethOamSvcCurrDmmTxFrames,'ethOamSvcCurrLmrRxFrames':ethOamSvcCurrLmrRxFrames,'ethOamSvcCurrDmrRxFrames':ethOamSvcCurrDmrRxFrames,'ethOamSvcCurrNearEndFramesLossCounter':ethOamSvcCurrNearEndFramesLossCounter,'ethOamSvcCurrTxFramesForward':ethOamSvcCurrTxFramesForward,'ethOamSvcCurrRxFramesForward':ethOamSvcCurrRxFramesForward,'ethOamSvcCurrTxFramesBackward':ethOamSvcCurrTxFramesBackward,'ethOamSvcCurrRxFramesBackward':ethOamSvcCurrRxFramesBackward,'ethOamSvcCurrUnavailableIndForward':ethOamSvcCurrUnavailableIndForward,'ethOamSvcCurrUnavailableIndBackward':ethOamSvcCurrUnavailableIndBackward,'ethOamSvcCurrNearEndFrameLossRatio':ethOamSvcCurrNearEndFrameLossRatio,'ethOamSvcCurrFarEndFrameLossRatio':ethOamSvcCurrFarEndFrameLossRatio,'ethOamSvcCurrMinRoundTripDVar':ethOamSvcCurrMinRoundTripDVar,'ethOamSvcCurrMinForwardDelay':ethOamSvcCurrMinForwardDelay,'ethOamSvcCurrMaxForwardDelay':ethOamSvcCurrMaxForwardDelay,'ethOamSvcCurrAvgForwardDelay':ethOamSvcCurrAvgForwardDelay,'ethOamSvcCurrMinForwardDVar':ethOamSvcCurrMinForwardDVar,'ethOamSvcCurrMaxForwardDVar':ethOamSvcCurrMaxForwardDVar,'ethOamSvcCurrAvgForwardDVar':ethOamSvcCurrAvgForwardDVar,'ethOamSvcCurrMinBackwardDVar':ethOamSvcCurrMinBackwardDVar,'ethOamSvcCurrMaxBackwardDVar':ethOamSvcCurrMaxBackwardDVar,'ethOamSvcCurrAvgBackwardDVar':ethOamSvcCurrAvgBackwardDVar,'ethOamSvcCurrAvailableIndForward':ethOamSvcCurrAvailableIndForward,'ethOamSvcCurrAvailableIndBackward':ethOamSvcCurrAvailableIndBackward,'ethOamSvcIntervalTable':ethOamSvcIntervalTable,'ethOamSvcIntervalEntry':ethOamSvcIntervalEntry,_w:ethOamSvcIntervalNum,'ethOamSvcIntervalFramesAboveDelayThresh':ethOamSvcIntervalFramesAboveDelayThresh,'ethOamSvcIntervalFramesBelowDelayThresh':ethOamSvcIntervalFramesBelowDelayThresh,'ethOamSvcIntervalFramesAboveDVarThresh':ethOamSvcIntervalFramesAboveDVarThresh,'ethOamSvcIntervalFramesBelowDVarThresh':ethOamSvcIntervalFramesBelowDVarThresh,'ethOamSvcIntervalFramesTxCounter':ethOamSvcIntervalFramesTxCounter,'ethOamSvcIntervalFarEndFramesLossCounter':ethOamSvcIntervalFarEndFramesLossCounter,'ethOamSvcIntervalMinRoundTripDelay':ethOamSvcIntervalMinRoundTripDelay,'ethOamSvcIntervalMaxRoundTripDelay':ethOamSvcIntervalMaxRoundTripDelay,'ethOamSvcIntervalAvgRoundTripDelay':ethOamSvcIntervalAvgRoundTripDelay,'ethOamSvcIntervalMaxRoundTripDVar':ethOamSvcIntervalMaxRoundTripDVar,'ethOamSvcIntervalAvgRoundTripDVar':ethOamSvcIntervalAvgRoundTripDVar,'ethOamSvcIntervalUnavailSec':ethOamSvcIntervalUnavailSec,'ethOamSvcIntervalLmmTxFrames':ethOamSvcIntervalLmmTxFrames,'ethOamSvcIntervalDmmTxFrames':ethOamSvcIntervalDmmTxFrames,'ethOamSvcIntervalLmrRxFrames':ethOamSvcIntervalLmrRxFrames,'ethOamSvcIntervalDmrRxFrames':ethOamSvcIntervalDmrRxFrames,'ethOamSvcIntervalNearEndFramesLossCounter':ethOamSvcIntervalNearEndFramesLossCounter,'ethOamSvcIntervalTxFramesForward':ethOamSvcIntervalTxFramesForward,'ethOamSvcIntervalRxFramesForward':ethOamSvcIntervalRxFramesForward,'ethOamSvcIntervalTxFramesBackward':ethOamSvcIntervalTxFramesBackward,'ethOamSvcIntervalRxFramesBackward':ethOamSvcIntervalRxFramesBackward,'ethOamSvcIntervalUnavailableIndForward':ethOamSvcIntervalUnavailableIndForward,'ethOamSvcIntervalUnavailableIndBackward':ethOamSvcIntervalUnavailableIndBackward,'ethOamSvcIntervalNearEndFrameLossRatio':ethOamSvcIntervalNearEndFrameLossRatio,'ethOamSvcIntervalFarEndFrameLossRatio':ethOamSvcIntervalFarEndFrameLossRatio,'ethOamSvcIntervalValidData':ethOamSvcIntervalValidData,'ethOamSvcIntervalDuration':ethOamSvcIntervalDuration,'ethOamSvcIntervalTimeStamp':ethOamSvcIntervalTimeStamp,'ethOamSvcIntervalMinRoundTripDVar':ethOamSvcIntervalMinRoundTripDVar,'ethOamSvcIntervalMinForwardDelay':ethOamSvcIntervalMinForwardDelay,'ethOamSvcIntervalMaxForwardDelay':ethOamSvcIntervalMaxForwardDelay,'ethOamSvcIntervalAvgForwardDelay':ethOamSvcIntervalAvgForwardDelay,'ethOamSvcIntervalMinForwardDVar':ethOamSvcIntervalMinForwardDVar,'ethOamSvcIntervalMaxForwardDVar':ethOamSvcIntervalMaxForwardDVar,'ethOamSvcIntervalAvgForwardDVar':ethOamSvcIntervalAvgForwardDVar,'ethOamSvcIntervalMinBackwardDVar':ethOamSvcIntervalMinBackwardDVar,'ethOamSvcIntervalMaxBackwardDVar':ethOamSvcIntervalMaxBackwardDVar,'ethOamSvcIntervalAvgBackwardDVar':ethOamSvcIntervalAvgBackwardDVar,'ethOamSvcIntervalAvailableIndForward':ethOamSvcIntervalAvailableIndForward,'ethOamSvcIntervalAvailableIndBackward':ethOamSvcIntervalAvailableIndBackward,'ethOamSvcTotalTable':ethOamSvcTotalTable,'ethOamSvcTotalEntry':ethOamSvcTotalEntry,'ethOamSvcTotalFramesAboveDelayThresh':ethOamSvcTotalFramesAboveDelayThresh,'ethOamSvcTotalFramesBelowDelayThresh':ethOamSvcTotalFramesBelowDelayThresh,'ethOamSvcTotalFramesAboveDVarThresh':ethOamSvcTotalFramesAboveDVarThresh,'ethOamSvcTotalFramesBelowDVarThresh':ethOamSvcTotalFramesBelowDVarThresh,'ethOamSvcTotalFramesTxCounter':ethOamSvcTotalFramesTxCounter,'ethOamSvcTotalFarEndFramesLossCounter':ethOamSvcTotalFarEndFramesLossCounter,'ethOamSvcTotalMinRoundTripDelay':ethOamSvcTotalMinRoundTripDelay,'ethOamSvcTotalMaxRoundTripDelay':ethOamSvcTotalMaxRoundTripDelay,'ethOamSvcTotalAvgRoundTripDelay':ethOamSvcTotalAvgRoundTripDelay,'ethOamSvcTotalMaxRoundTripDVar':ethOamSvcTotalMaxRoundTripDVar,'ethOamSvcTotalAvgRoundTripDVar':ethOamSvcTotalAvgRoundTripDVar,'ethOamSvcTotalUnavailSec':ethOamSvcTotalUnavailSec,'ethOamSvcTotalLmmTxFrames':ethOamSvcTotalLmmTxFrames,'ethOamSvcTotalDmmTxFrames':ethOamSvcTotalDmmTxFrames,'ethOamSvcTotalLmrRxFrames':ethOamSvcTotalLmrRxFrames,'ethOamSvcTotalDmrRxFrames':ethOamSvcTotalDmrRxFrames,'ethOamSvcTotalNearEndFramesLossCounter':ethOamSvcTotalNearEndFramesLossCounter,'ethOamSvcTotalTxFramesForward':ethOamSvcTotalTxFramesForward,'ethOamSvcTotalRxFramesForward':ethOamSvcTotalRxFramesForward,'ethOamSvcTotalTxFramesBackward':ethOamSvcTotalTxFramesBackward,'ethOamSvcTotalRxFramesBackward':ethOamSvcTotalRxFramesBackward,'ethOamSvcTotalUnavailableIndForward':ethOamSvcTotalUnavailableIndForward,'ethOamSvcTotalUnavailableIndBackward':ethOamSvcTotalUnavailableIndBackward,'ethOamSvcTotalMinRoundTripDVar':ethOamSvcTotalMinRoundTripDVar,'ethOamSvcTotalMinForwardDelay':ethOamSvcTotalMinForwardDelay,'ethOamSvcTotalMaxForwardDelay':ethOamSvcTotalMaxForwardDelay,'ethOamSvcTotalAvgForwardDelay':ethOamSvcTotalAvgForwardDelay,'ethOamSvcTotalMinForwardDVar':ethOamSvcTotalMinForwardDVar,'ethOamSvcTotalMaxForwardDVar':ethOamSvcTotalMaxForwardDVar,'ethOamSvcTotalAvgForwardDVar':ethOamSvcTotalAvgForwardDVar,'ethOamSvcTotalMinBackwardDVar':ethOamSvcTotalMinBackwardDVar,'ethOamSvcTotalMaxBackwardDVar':ethOamSvcTotalMaxBackwardDVar,'ethOamSvcTotalAvgBackwardDVar':ethOamSvcTotalAvgBackwardDVar,'ethOamSvcTotalForwardFrameLossRatio':ethOamSvcTotalForwardFrameLossRatio,'ethOamSvcTotalBackwardFrameLossRatio':ethOamSvcTotalBackwardFrameLossRatio,'ethOamSvcTotalAvailableIndForward':ethOamSvcTotalAvailableIndForward,'ethOamSvcTotalAvailableIndBackward':ethOamSvcTotalAvailableIndBackward,'ethOamDestNeTable':ethOamDestNeTable,'ethOamDestNeEntry':ethOamDestNeEntry,_A3:ethOamDestNeIdx,'ethOamDestNeRowStatus':ethOamDestNeRowStatus,'ethOamDestNePmDestAddr':ethOamDestNePmDestAddr,'ethOamDestNePmRemoteMepId':ethOamDestNePmRemoteMepId,'ethOamDestNePmActivity':ethOamDestNePmActivity,'ethOamDestNeTxFrames':ethOamDestNeTxFrames,'ethOamDestNeOverflowTxFrames':ethOamDestNeOverflowTxFrames,'ethOamDestNeTxLmm':ethOamDestNeTxLmm,'ethOamDestNeOverflowTxLmm':ethOamDestNeOverflowTxLmm,'ethOamDestNeTxDmm':ethOamDestNeTxDmm,'ethOamDestNeOverflowTxDmm':ethOamDestNeOverflowTxDmm,'ethOamDestNeRxLmr':ethOamDestNeRxLmr,'ethOamDestNeOverflowRxLmr':ethOamDestNeOverflowRxLmr,'ethOamDestNeRxDmr':ethOamDestNeRxDmr,'ethOamDestNeOverflowRxDmr':ethOamDestNeOverflowRxDmr,'ethOamDestNeFarEndFrameLoss':ethOamDestNeFarEndFrameLoss,'ethOamDestNeOverflowFarEndFrameLoss':ethOamDestNeOverflowFarEndFrameLoss,'ethOamDestNeFarEndFrameLossRatio':ethOamDestNeFarEndFrameLossRatio,'ethOamDestNeTimeElapsed':ethOamDestNeTimeElapsed,'ethOamDestNeFramesAboveDelay':ethOamDestNeFramesAboveDelay,'ethOamDestNeOverflowFramesAboveDelay':ethOamDestNeOverflowFramesAboveDelay,'ethOamDestNeFramesAboveDelayVar':ethOamDestNeFramesAboveDelayVar,'ethOamDestNeOverflowFramesAboveDelayVar':ethOamDestNeOverflowFramesAboveDelayVar,'ethOamDestNeCurrentDelay':ethOamDestNeCurrentDelay,'ethOamDestNeCurrentDelayVariation':ethOamDestNeCurrentDelayVariation,'ethOamDestNeResetCounters':ethOamDestNeResetCounters,'ethOamDestNeNearEndFrameLoss':ethOamDestNeNearEndFrameLoss,'ethOamDestNeOverflowNearEndFrameLoss':ethOamDestNeOverflowNearEndFrameLoss,'ethOamDestNeNearEndFrameLossRatio':ethOamDestNeNearEndFrameLossRatio,'ethOamDestNeLmmTraffic':ethOamDestNeLmmTraffic,'ethOamDestNeFramesAboveDelayBinProfile':ethOamDestNeFramesAboveDelayBinProfile,'ethOamDestNeFramesAboveDelayVarBinProfile':ethOamDestNeFramesAboveDelayVarBinProfile,'ethOamDestNeDmmDataTlvLength':ethOamDestNeDmmDataTlvLength,'ethOamDestNeLossActivity':ethOamDestNeLossActivity,'ethOamDestNeDelayActivity':ethOamDestNeDelayActivity,'ethOamDestNeTxForward':ethOamDestNeTxForward,'ethOamDestNeOverflowTxForward':ethOamDestNeOverflowTxForward,'ethOamDestNeRxForward':ethOamDestNeRxForward,'ethOamDestNeOverflowRxForward':ethOamDestNeOverflowRxForward,'ethOamDestNeTxBackward':ethOamDestNeTxBackward,'ethOamDestNeOverflowTxBackward':ethOamDestNeOverflowTxBackward,'ethOamDestNeRxBackward':ethOamDestNeRxBackward,'ethOamDestNeOverflowRxBackward':ethOamDestNeOverflowRxBackward,'ethOamDestNeUnavailableIndForward':ethOamDestNeUnavailableIndForward,'ethOamDestNeOverflowUnavailableIndForward':ethOamDestNeOverflowUnavailableIndForward,'ethOamDestNeUnavailableIndBackward':ethOamDestNeUnavailableIndBackward,'ethOamDestNeOverflowUnavailableIndBackward':ethOamDestNeOverflowUnavailableIndBackward,'ethOamDestNeUnavailRatioForward':ethOamDestNeUnavailRatioForward,'ethOamDestNeUnavailRatioBackward':ethOamDestNeUnavailRatioBackward,_U:ethOamDestNeDescr,'ethOamDestNeConvertedIndex':ethOamDestNeConvertedIndex,'ethOamDestNeSlmDataTlvLength':ethOamDestNeSlmDataTlvLength,'ethOamDestNeLmMode':ethOamDestNeLmMode,'ethOamDestNeSlmTestId':ethOamDestNeSlmTestId,'ethOamDestNeForwardDelayVarBinProfile':ethOamDestNeForwardDelayVarBinProfile,'ethOamDestNeBackwardDelayVarBinProfile':ethOamDestNeBackwardDelayVarBinProfile,'ethOamDestNeAvailableIndForward':ethOamDestNeAvailableIndForward,'ethOamDestNeAvailableIndBackward':ethOamDestNeAvailableIndBackward,'ethOamDestNeDelayVariationForward':ethOamDestNeDelayVariationForward,'ethOamDestNeDelayVariationBackward':ethOamDestNeDelayVariationBackward,'ethOamSvcRmonConfigTable':ethOamSvcRmonConfigTable,'ethOamSvcRmonConfigEntry':ethOamSvcRmonConfigEntry,_A4:ethOamSvcRmonConfigPerfAttrib,'ethOamSvcRmonConfigRowStatus':ethOamSvcRmonConfigRowStatus,'ethOamSvcRmonConfigAlarmInterval':ethOamSvcRmonConfigAlarmInterval,'ethOamSvcRmonConfigAlarmRisingThresh':ethOamSvcRmonConfigAlarmRisingThresh,'ethOamSvcRmonConfigAlarmFallingThresh':ethOamSvcRmonConfigAlarmFallingThresh,'ethOamSvcRmonConfigEventType':ethOamSvcRmonConfigEventType,'ethOamMeasureBinProfileTable':ethOamMeasureBinProfileTable,'ethOamMeasureBinProfileEntry':ethOamMeasureBinProfileEntry,_A5:ethOamMeasureBinProfileIndex,'ethOamMeasureBinProfileRowStatus':ethOamMeasureBinProfileRowStatus,'ethOamMeasureBinProfileName':ethOamMeasureBinProfileName,'ethOamMeasureBinThresh':ethOamMeasureBinThresh,'ethOamDelayCurrentBinsTable':ethOamDelayCurrentBinsTable,'ethOamDelayCurrentBinsEntry':ethOamDelayCurrentBinsEntry,_A6:ethOamDelayCurrentBinCounterType,_A7:ethOamDelayCurrentBinNumber,'ethOamDelayCurrentBinValue':ethOamDelayCurrentBinValue,'ethOamDelayIntervalBinsTable':ethOamDelayIntervalBinsTable,'ethOamDelayIntervalBinsEntry':ethOamDelayIntervalBinsEntry,_A8:ethOamDelayIntervalBinCounterType,_A9:ethOamDelayIntervalBinNumber,'ethOamDelayIntervalBinValue':ethOamDelayIntervalBinValue,'radMdTable':radMdTable,'radMdEntry':radMdEntry,_AA:radMdIndex,'radMdFormat':radMdFormat,'radMdName':radMdName,'radMdRowStatus':radMdRowStatus,'radMepLtrTable':radMepLtrTable,'radMepLtrEntry':radMepLtrEntry,_AB:radMepLtrReceiveOrder,'radMepLtrTtl':radMepLtrTtl,'radMepLtrMacAddr':radMepLtrMacAddr,'radMepLtrRelay':radMepLtrRelay,'radMepLtrIngress':radMepLtrIngress,'radMepLtrIngressPortIdSubtype':radMepLtrIngressPortIdSubtype,'radMepLtrIngressPortId':radMepLtrIngressPortId,'radMepLtrEgress':radMepLtrEgress,'radMepLtrEgressPortIdSubtype':radMepLtrEgressPortIdSubtype,'radMepLtrEgressPortId':radMepLtrEgressPortId,'radMepCcStatusTable':radMepCcStatusTable,'radMepCcStatusEntry':radMepCcStatusEntry,_AC:radMepRemoteMepIdx,'radMepCcStatusRemMepId':radMepCcStatusRemMepId,'radMepCcStat':radMepCcStat,'radMepCcStatusMacAddr':radMepCcStatusMacAddr,'ethOamStdEtherType':ethOamStdEtherType,'ethOamStdMacAddress':ethOamStdMacAddress,'dot1agXCfmMdTable':dot1agXCfmMdTable,'dot1agXCfmMdEntry':dot1agXCfmMdEntry,'dot1agXCfmMdProtocol':dot1agXCfmMdProtocol,'dot1agXCfmMepTable':dot1agXCfmMepTable,'dot1agXCfmMepEntry':dot1agXCfmMepEntry,'dot1agXCfmMepContinuityVerMode':dot1agXCfmMepContinuityVerMode,'dot1agXCfmMepDestAddrType':dot1agXCfmMepDestAddrType,'dot1agXCfmMepDestMacAddr':dot1agXCfmMepDestMacAddr,'dot1agXCfmMepMappingProfile':dot1agXCfmMepMappingProfile,'dot1agXCfmMepQBlock':dot1agXCfmMepQBlock,'dot1agXCfmMepFixedQueueMapping':dot1agXCfmMepFixedQueueMapping,'dot1agXCfmMepQueueMappingProfile':dot1agXCfmMepQueueMappingProfile,'dot1agXCfmMepConvertedIndex':dot1agXCfmMepConvertedIndex,'dot1agXCfmMepPmDestAddrType':dot1agXCfmMepPmDestAddrType,'dot1agXCfmMepForwardingMode':dot1agXCfmMepForwardingMode,'dot1agXCfmMepLbmDataTlvLength':dot1agXCfmMepLbmDataTlvLength,'dot1agXCfmMepClientMdLevel':dot1agXCfmMepClientMdLevel,'dot1agXCfmMepAisTransmit':dot1agXCfmMepAisTransmit,'dot1agXCfmMepAisInterval':dot1agXCfmMepAisInterval,'dot1agXCfmMepAisPriority':dot1agXCfmMepAisPriority,'dot1agXCfmMepDefects':dot1agXCfmMepDefects,'dot1agXCfmMepLastAlarmDefect':dot1agXCfmMepLastAlarmDefect,'dot1agXCfmMepCosMapping':dot1agXCfmMepCosMapping,'dot1agXCfmMepCosMappingProfile':dot1agXCfmMepCosMappingProfile,_AR:dot1agXCfmMepCcStatus,'dot1agXCfmMepStatus':dot1agXCfmMepStatus,'dot1agXCfmMepExcludeCustomerTags':dot1agXCfmMepExcludeCustomerTags,'dot1agXCfmMepClearStatsCmd':dot1agXCfmMepClearStatsCmd,'dot1agXCfmMepTimeElapsed':dot1agXCfmMepTimeElapsed,'dot1agXCfmMepCcmTx':dot1agXCfmMepCcmTx,'dot1agXCfmMepDbTable':dot1agXCfmMepDbTable,'dot1agXCfmMepDbEntry':dot1agXCfmMepDbEntry,'dot1agXCfmMepCcStat':dot1agXCfmMepCcStat,'dot1agXCfmMepDbConvertedIndex':dot1agXCfmMepDbConvertedIndex,'dot1agXCfmMaMepListTable':dot1agXCfmMaMepListTable,'dot1agXCfmMaMepListEntry':dot1agXCfmMaMepListEntry,'dot1agXCfmMaMepListLocalMep':dot1agXCfmMaMepListLocalMep,_a:dot1agXCfmMaMepListDescr,'ethIfOamCfmMip':ethIfOamCfmMip,'ethIfOamCfmMipTable':ethIfOamCfmMipTable,'ethIfOamCfmMipEntry':ethIfOamCfmMipEntry,_AD:ethIfOamCfmMipMdIdx,_AE:ethIfOamCfmMipIdx,'ethIfOamCfmMipRowStatus':ethIfOamCfmMipRowStatus,'ethIfOamCfmMipBoundedPortIfIndex':ethIfOamCfmMipBoundedPortIfIndex,'ethIfOamCfmMipFlowType':ethIfOamCfmMipFlowType,'ethIfOamCfmMipFlowRxIndex':ethIfOamCfmMipFlowRxIndex,'ethIfOamCfmMipFlowTxIndex':ethIfOamCfmMipFlowTxIndex,'ethIfOamCfmMhfTable':ethIfOamCfmMhfTable,'ethIfOamCfmMhfEntry':ethIfOamCfmMhfEntry,_AG:ethIfOamCfmMhfMdIdx,_AH:ethIfOamCfmMhfMipIdx,_AI:ethIfOamCfmMhfIdx,'ethIfOamCfmMhfActive':ethIfOamCfmMhfActive,'ethIfOamCfmMhfOutputPortIfIndex':ethIfOamCfmMhfOutputPortIfIndex,'ethIfOamCfmMhfPrimaryVid':ethIfOamCfmMhfPrimaryVid,'ethIfOamCfmMhfMappingProfile':ethIfOamCfmMhfMappingProfile,'ethIfOamCfmMhfCosMapping':ethIfOamCfmMhfCosMapping,'ethIfOamCfmMhfCosMappingProfile':ethIfOamCfmMhfCosMappingProfile,'ethIfOamCfmMhfQBlock':ethIfOamCfmMhfQBlock,'ethIfOamCfmMhfFixedQueueMapping':ethIfOamCfmMhfFixedQueueMapping,'ethIfOamCfmMhfQueueMappingProfile':ethIfOamCfmMhfQueueMappingProfile,'ethOamMip':ethOamMip,'ethOamMipTable':ethOamMipTable,'ethOamMipEntry':ethOamMipEntry,_AJ:ethOamMipIfIndex,_AK:ethOamMipVlanId,'ethOamMipMdLevel':ethOamMipMdLevel,'agnAutoMipAssign':agnAutoMipAssign,'ethIfOamCfmSumMipMep':ethIfOamCfmSumMipMep,'dot1agXCfmMaNetTable':dot1agXCfmMaNetTable,'dot1agXCfmMaNetEntry':dot1agXCfmMaNetEntry,'dot1agXCfmMaNetServiceIdName':dot1agXCfmMaNetServiceIdName,'dot1agXCfmMaNetIfStatusTlv':dot1agXCfmMaNetIfStatusTlv,'ethOamMepFlowsTable':ethOamMepFlowsTable,'ethOamMepFlowsEntry':ethOamMepFlowsEntry,_AL:ethOamMepFlowType,_AM:ethOamMepFlowIndex1,_AN:ethOamMepFlowIndex2,'ethOamMepFlowsRowStatus':ethOamMepFlowsRowStatus,'ethOamConfigTable':ethOamConfigTable,'ethOamConfigEntry':ethOamConfigEntry,_AO:ethOamConfigIdx,'ethOamConfigAlarmType':ethOamConfigAlarmType,'ethOamConfigAvailabilityDeltaT':ethOamConfigAvailabilityDeltaT,'ethOamConfigAvailabilityNumDeltaTs':ethOamConfigAvailabilityNumDeltaTs,'ethOamConfigAvailabilityFwdFlrThreshold':ethOamConfigAvailabilityFwdFlrThreshold,'ethOamConfigAvailabilityBckFlrThreshold':ethOamConfigAvailabilityBckFlrThreshold,'ethOamConfigMdLevelMips':ethOamConfigMdLevelMips,'ethOamMepStats':ethOamMepStats,'ethOamMepCurrentTable':ethOamMepCurrentTable,'ethOamMepCurrentEntry':ethOamMepCurrentEntry,'ethOamMepCurrentCcmTx':ethOamMepCurrentCcmTx,'ethOamMepIntervalTable':ethOamMepIntervalTable,'ethOamMepIntervalEntry':ethOamMepIntervalEntry,_AP:ethOamMepIntervalNumber,'ethOamMepIntervalValidData':ethOamMepIntervalValidData,'ethOamMepIntervalDuration':ethOamMepIntervalDuration,'ethOamMepIntervalTimeStamp':ethOamMepIntervalTimeStamp,'ethOamMepIntervalCcmTx':ethOamMepIntervalCcmTx,'ethOamRMepStatsTable':ethOamRMepStatsTable,'ethOamRMepStatsEntry':ethOamRMepStatsEntry,_n:ethOamRMepStatsRMepId,'ethOamRMepStatsCcmRx':ethOamRMepStatsCcmRx,'ethOamRMepStatsClearCmd':ethOamRMepStatsClearCmd,'ethOamRMepCurrentTable':ethOamRMepCurrentTable,'ethOamRMepCurrentEntry':ethOamRMepCurrentEntry,'ethOamRMepCurrentCcmRx':ethOamRMepCurrentCcmRx,'ethOamRMepIntervalTable':ethOamRMepIntervalTable,'ethOamRMepIntervalEntry':ethOamRMepIntervalEntry,_AQ:ethOamRMepIntervalNumber,'ethOamRMepIntervalValidData':ethOamRMepIntervalValidData,'ethOamRMepIntervalDuration':ethOamRMepIntervalDuration,'ethOamRMepIntervalTimeStamp':ethOamRMepIntervalTimeStamp,'ethOamRMepIntervalCcmRx':ethOamRMepIntervalCcmRx})