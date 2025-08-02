_A6='acSS7RedundantSNIndex'
_A5='acSS7RedundantSNBoardIndex'
_A4='acSS7SigTranRoutingContextInnerIndex'
_A3='acSS7SigTranRoutingContextIndex'
_A2='acSS7M3UAStaticRoutingIndex'
_A1='acSS7SigTranIFIDIndex'
_A0='acSS7SigTranIFGroupIndex'
_z='acSS7APCIndex'
_y='acSS7APCSNIndex'
_x='acSS7RouteSetRouteInnerRouteIndex'
_w='acSS7RouteSetRouteRoutesetIndex'
_v='acSS7RouteSetRouteSNIndex'
_u='acSS7RouteSetIndex'
_t='acSS7RouteSetSNIndex'
_s='acSS7LinkSetLinkInnerLinkIndex'
_r='acSS7LinkSetLinkLinksetIndex'
_q='acSS7LinkSetLinkSNIndex'
_p='acSS7LinkSetLksetIndex'
_o='acSS7LinkSetSNIndex'
_n='timersIdx4'
_m='timersIdx3'
_l='timersIdx2'
_k='timersIdx1'
_j='timersIdx0'
_i='acSS7SignalingNodeIndex'
_h='ss7monitoring'
_g='traceLevel1'
_f='traceLevel0'
_e='acSS7LinkSetTimersIndex'
_d='acSS7SignalingNodeTimersIndex'
_c='acSS7MTP2AttribIndex'
_b='china'
_a='ansi'
_Z='itu'
_Y='l4Gen'
_X='nill'
_W='ual'
_V='busy'
_U='acSS7LinkCommonIndex'
_T='deActivate'
_S='activate'
_R='yes'
_Q='no'
_P='failed'
_O='inProgress'
_N='succeeded'
_M='SnmpAdminString'
_L='inService'
_K='offLine'
_J='none'
_I='not-accessible'
_H='AC-SS7-MIB'
_G='obsolete'
_F='read-only'
_E='read-write'
_D='Integer32'
_C='read-create'
_B='Unsigned32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
acBoardMibs,acGeneric,acProducts,acRegistrations,audioCodes=mibBuilder.importSymbols('AUDIOCODES-TYPES-MIB','acBoardMibs','acGeneric','acProducts','acRegistrations','audioCodes')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_B,'enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TAddress','TextualConvention')
acSS7=ModuleIdentity((1,3,6,1,4,1,5003,9,10,12))
_AcSS7Configuration_ObjectIdentity=ObjectIdentity
acSS7Configuration=_AcSS7Configuration_ObjectIdentity((1,3,6,1,4,1,5003,9,10,12,1))
_AcSS7MTP2_ObjectIdentity=ObjectIdentity
acSS7MTP2=_AcSS7MTP2_ObjectIdentity((1,3,6,1,4,1,5003,9,10,12,1,1))
class _AcSS7MTP2M3bSlDiscardCongThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcSS7MTP2M3bSlDiscardCongThreshold_Type.__name__=_B
_AcSS7MTP2M3bSlDiscardCongThreshold_Object=MibScalar
acSS7MTP2M3bSlDiscardCongThreshold=_AcSS7MTP2M3bSlDiscardCongThreshold_Object((1,3,6,1,4,1,5003,9,10,12,1,1,1),_AcSS7MTP2M3bSlDiscardCongThreshold_Type())
acSS7MTP2M3bSlDiscardCongThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7MTP2M3bSlDiscardCongThreshold.setStatus(_A)
_AcSS7MTP2AttribTable_Object=MibTable
acSS7MTP2AttribTable=_AcSS7MTP2AttribTable_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21))
if mibBuilder.loadTexts:acSS7MTP2AttribTable.setStatus(_A)
_AcSS7MTP2AttribEntry_Object=MibTableRow
acSS7MTP2AttribEntry=_AcSS7MTP2AttribEntry_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1))
acSS7MTP2AttribEntry.setIndexNames((0,_H,_c))
if mibBuilder.loadTexts:acSS7MTP2AttribEntry.setStatus(_A)
class _AcSS7MTP2AttribIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AcSS7MTP2AttribIndex_Type.__name__=_B
_AcSS7MTP2AttribIndex_Object=MibTableColumn
acSS7MTP2AttribIndex=_AcSS7MTP2AttribIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,1),_AcSS7MTP2AttribIndex_Type())
acSS7MTP2AttribIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7MTP2AttribIndex.setStatus(_A)
class _AcSS7MTP2AttribIsUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_R,1)))
_AcSS7MTP2AttribIsUsed_Type.__name__=_D
_AcSS7MTP2AttribIsUsed_Object=MibTableColumn
acSS7MTP2AttribIsUsed=_AcSS7MTP2AttribIsUsed_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,2),_AcSS7MTP2AttribIsUsed_Type())
acSS7MTP2AttribIsUsed.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7MTP2AttribIsUsed.setStatus(_A)
class _AcSS7MTP2AttribLinkRate_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1))
_AcSS7MTP2AttribLinkRate_Type.__name__=_M
_AcSS7MTP2AttribLinkRate_Object=MibTableColumn
acSS7MTP2AttribLinkRate=_AcSS7MTP2AttribLinkRate_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,3),_AcSS7MTP2AttribLinkRate_Type())
acSS7MTP2AttribLinkRate.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7MTP2AttribLinkRate.setStatus(_A)
class _AcSS7MTP2AttribErrorCorectionMethod_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1))
_AcSS7MTP2AttribErrorCorectionMethod_Type.__name__=_M
_AcSS7MTP2AttribErrorCorectionMethod_Object=MibTableColumn
acSS7MTP2AttribErrorCorectionMethod=_AcSS7MTP2AttribErrorCorectionMethod_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,4),_AcSS7MTP2AttribErrorCorectionMethod_Type())
acSS7MTP2AttribErrorCorectionMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7MTP2AttribErrorCorectionMethod.setStatus(_A)
class _AcSS7MTP2AttribIacCp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_AcSS7MTP2AttribIacCp_Type.__name__=_B
_AcSS7MTP2AttribIacCp_Object=MibTableColumn
acSS7MTP2AttribIacCp=_AcSS7MTP2AttribIacCp_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,5),_AcSS7MTP2AttribIacCp_Type())
acSS7MTP2AttribIacCp.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7MTP2AttribIacCp.setStatus(_A)
class _AcSS7MTP2AttribSUERMThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_AcSS7MTP2AttribSUERMThreshold_Type.__name__=_B
_AcSS7MTP2AttribSUERMThreshold_Object=MibTableColumn
acSS7MTP2AttribSUERMThreshold=_AcSS7MTP2AttribSUERMThreshold_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,6),_AcSS7MTP2AttribSUERMThreshold_Type())
acSS7MTP2AttribSUERMThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7MTP2AttribSUERMThreshold.setStatus(_A)
class _AcSS7MTP2AttribAERMNormalThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_AcSS7MTP2AttribAERMNormalThreshold_Type.__name__=_B
_AcSS7MTP2AttribAERMNormalThreshold_Object=MibTableColumn
acSS7MTP2AttribAERMNormalThreshold=_AcSS7MTP2AttribAERMNormalThreshold_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,7),_AcSS7MTP2AttribAERMNormalThreshold_Type())
acSS7MTP2AttribAERMNormalThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7MTP2AttribAERMNormalThreshold.setStatus(_A)
class _AcSS7MTP2AttribAERMEmerglThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_AcSS7MTP2AttribAERMEmerglThreshold_Type.__name__=_B
_AcSS7MTP2AttribAERMEmerglThreshold_Object=MibTableColumn
acSS7MTP2AttribAERMEmerglThreshold=_AcSS7MTP2AttribAERMEmerglThreshold_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,8),_AcSS7MTP2AttribAERMEmerglThreshold_Type())
acSS7MTP2AttribAERMEmerglThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7MTP2AttribAERMEmerglThreshold.setStatus(_A)
class _AcSS7MTP2AttribSUERMSigUnitDThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_AcSS7MTP2AttribSUERMSigUnitDThreshold_Type.__name__=_B
_AcSS7MTP2AttribSUERMSigUnitDThreshold_Object=MibTableColumn
acSS7MTP2AttribSUERMSigUnitDThreshold=_AcSS7MTP2AttribSUERMSigUnitDThreshold_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,9),_AcSS7MTP2AttribSUERMSigUnitDThreshold_Type())
acSS7MTP2AttribSUERMSigUnitDThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7MTP2AttribSUERMSigUnitDThreshold.setStatus(_A)
class _AcSS7MTP2AttribOctetCounting_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_AcSS7MTP2AttribOctetCounting_Type.__name__=_B
_AcSS7MTP2AttribOctetCounting_Object=MibTableColumn
acSS7MTP2AttribOctetCounting=_AcSS7MTP2AttribOctetCounting_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,10),_AcSS7MTP2AttribOctetCounting_Type())
acSS7MTP2AttribOctetCounting.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7MTP2AttribOctetCounting.setStatus(_A)
class _AcSS7MTP2AttribTimerT1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_AcSS7MTP2AttribTimerT1_Type.__name__=_B
_AcSS7MTP2AttribTimerT1_Object=MibTableColumn
acSS7MTP2AttribTimerT1=_AcSS7MTP2AttribTimerT1_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,11),_AcSS7MTP2AttribTimerT1_Type())
acSS7MTP2AttribTimerT1.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7MTP2AttribTimerT1.setStatus(_A)
class _AcSS7MTP2AttribTimerT2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000))
_AcSS7MTP2AttribTimerT2_Type.__name__=_B
_AcSS7MTP2AttribTimerT2_Object=MibTableColumn
acSS7MTP2AttribTimerT2=_AcSS7MTP2AttribTimerT2_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,12),_AcSS7MTP2AttribTimerT2_Type())
acSS7MTP2AttribTimerT2.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7MTP2AttribTimerT2.setStatus(_A)
class _AcSS7MTP2AttribTimerT3_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20000))
_AcSS7MTP2AttribTimerT3_Type.__name__=_B
_AcSS7MTP2AttribTimerT3_Object=MibTableColumn
acSS7MTP2AttribTimerT3=_AcSS7MTP2AttribTimerT3_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,13),_AcSS7MTP2AttribTimerT3_Type())
acSS7MTP2AttribTimerT3.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7MTP2AttribTimerT3.setStatus(_A)
class _AcSS7MTP2AttribTimerT4Normal_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15000))
_AcSS7MTP2AttribTimerT4Normal_Type.__name__=_B
_AcSS7MTP2AttribTimerT4Normal_Object=MibTableColumn
acSS7MTP2AttribTimerT4Normal=_AcSS7MTP2AttribTimerT4Normal_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,14),_AcSS7MTP2AttribTimerT4Normal_Type())
acSS7MTP2AttribTimerT4Normal.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7MTP2AttribTimerT4Normal.setStatus(_A)
class _AcSS7MTP2AttribTimerT4Emerg_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_AcSS7MTP2AttribTimerT4Emerg_Type.__name__=_B
_AcSS7MTP2AttribTimerT4Emerg_Object=MibTableColumn
acSS7MTP2AttribTimerT4Emerg=_AcSS7MTP2AttribTimerT4Emerg_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,15),_AcSS7MTP2AttribTimerT4Emerg_Type())
acSS7MTP2AttribTimerT4Emerg.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7MTP2AttribTimerT4Emerg.setStatus(_A)
class _AcSS7MTP2AttribTimerT5_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2400))
_AcSS7MTP2AttribTimerT5_Type.__name__=_B
_AcSS7MTP2AttribTimerT5_Object=MibTableColumn
acSS7MTP2AttribTimerT5=_AcSS7MTP2AttribTimerT5_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,16),_AcSS7MTP2AttribTimerT5_Type())
acSS7MTP2AttribTimerT5.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7MTP2AttribTimerT5.setStatus(_A)
class _AcSS7MTP2AttribTimerT6_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_AcSS7MTP2AttribTimerT6_Type.__name__=_B
_AcSS7MTP2AttribTimerT6_Object=MibTableColumn
acSS7MTP2AttribTimerT6=_AcSS7MTP2AttribTimerT6_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,17),_AcSS7MTP2AttribTimerT6_Type())
acSS7MTP2AttribTimerT6.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7MTP2AttribTimerT6.setStatus(_A)
class _AcSS7MTP2AttribTimerT7_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000))
_AcSS7MTP2AttribTimerT7_Type.__name__=_B
_AcSS7MTP2AttribTimerT7_Object=MibTableColumn
acSS7MTP2AttribTimerT7=_AcSS7MTP2AttribTimerT7_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,18),_AcSS7MTP2AttribTimerT7_Type())
acSS7MTP2AttribTimerT7.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7MTP2AttribTimerT7.setStatus(_A)
class _AcSS7MTP2AttribLSSULength_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_AcSS7MTP2AttribLSSULength_Type.__name__=_B
_AcSS7MTP2AttribLSSULength_Object=MibTableColumn
acSS7MTP2AttribLSSULength=_AcSS7MTP2AttribLSSULength_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,19),_AcSS7MTP2AttribLSSULength_Type())
acSS7MTP2AttribLSSULength.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7MTP2AttribLSSULength.setStatus(_A)
class _AcSS7MTP2AttribPcrN2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_AcSS7MTP2AttribPcrN2_Type.__name__=_B
_AcSS7MTP2AttribPcrN2_Object=MibTableColumn
acSS7MTP2AttribPcrN2=_AcSS7MTP2AttribPcrN2_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,20),_AcSS7MTP2AttribPcrN2_Type())
acSS7MTP2AttribPcrN2.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7MTP2AttribPcrN2.setStatus(_A)
_AcSS7MTP2AttribRowStatus_Type=RowStatus
_AcSS7MTP2AttribRowStatus_Object=MibTableColumn
acSS7MTP2AttribRowStatus=_AcSS7MTP2AttribRowStatus_Object((1,3,6,1,4,1,5003,9,10,12,1,1,21,1,21),_AcSS7MTP2AttribRowStatus_Type())
acSS7MTP2AttribRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7MTP2AttribRowStatus.setStatus(_G)
_AcSS7Timers_ObjectIdentity=ObjectIdentity
acSS7Timers=_AcSS7Timers_ObjectIdentity((1,3,6,1,4,1,5003,9,10,12,1,2))
_AcSS7SignalingNodeTimersTable_Object=MibTable
acSS7SignalingNodeTimersTable=_AcSS7SignalingNodeTimersTable_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21))
if mibBuilder.loadTexts:acSS7SignalingNodeTimersTable.setStatus(_A)
_AcSS7SignalingNodeTimersEntry_Object=MibTableRow
acSS7SignalingNodeTimersEntry=_AcSS7SignalingNodeTimersEntry_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1))
acSS7SignalingNodeTimersEntry.setIndexNames((0,_H,_d))
if mibBuilder.loadTexts:acSS7SignalingNodeTimersEntry.setStatus(_A)
class _AcSS7SignalingNodeTimersIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_AcSS7SignalingNodeTimersIndex_Type.__name__=_B
_AcSS7SignalingNodeTimersIndex_Object=MibTableColumn
acSS7SignalingNodeTimersIndex=_AcSS7SignalingNodeTimersIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,1),_AcSS7SignalingNodeTimersIndex_Type())
acSS7SignalingNodeTimersIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersIndex.setStatus(_A)
class _AcSS7SignalingNodeTimersIsUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_R,1)))
_AcSS7SignalingNodeTimersIsUsed_Type.__name__=_D
_AcSS7SignalingNodeTimersIsUsed_Object=MibTableColumn
acSS7SignalingNodeTimersIsUsed=_AcSS7SignalingNodeTimersIsUsed_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,2),_AcSS7SignalingNodeTimersIsUsed_Type())
acSS7SignalingNodeTimersIsUsed.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersIsUsed.setStatus(_A)
class _AcSS7SignalingNodeTimersAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues((_J,0))
_AcSS7SignalingNodeTimersAction_Type.__name__=_D
_AcSS7SignalingNodeTimersAction_Object=MibTableColumn
acSS7SignalingNodeTimersAction=_AcSS7SignalingNodeTimersAction_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,3),_AcSS7SignalingNodeTimersAction_Type())
acSS7SignalingNodeTimersAction.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersAction.setStatus(_A)
class _AcSS7SignalingNodeTimersActionResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2)))
_AcSS7SignalingNodeTimersActionResult_Type.__name__=_D
_AcSS7SignalingNodeTimersActionResult_Object=MibTableColumn
acSS7SignalingNodeTimersActionResult=_AcSS7SignalingNodeTimersActionResult_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,4),_AcSS7SignalingNodeTimersActionResult_Type())
acSS7SignalingNodeTimersActionResult.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersActionResult.setStatus(_A)
class _AcSS7SignalingNodeTimersName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AcSS7SignalingNodeTimersName_Type.__name__=_M
_AcSS7SignalingNodeTimersName_Object=MibTableColumn
acSS7SignalingNodeTimersName=_AcSS7SignalingNodeTimersName_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,5),_AcSS7SignalingNodeTimersName_Type())
acSS7SignalingNodeTimersName.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersName.setStatus(_A)
class _AcSS7SignalingNodeTimersT6_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7SignalingNodeTimersT6_Type.__name__=_B
_AcSS7SignalingNodeTimersT6_Object=MibTableColumn
acSS7SignalingNodeTimersT6=_AcSS7SignalingNodeTimersT6_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,6),_AcSS7SignalingNodeTimersT6_Type())
acSS7SignalingNodeTimersT6.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersT6.setStatus(_A)
class _AcSS7SignalingNodeTimersT8_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7SignalingNodeTimersT8_Type.__name__=_B
_AcSS7SignalingNodeTimersT8_Object=MibTableColumn
acSS7SignalingNodeTimersT8=_AcSS7SignalingNodeTimersT8_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,7),_AcSS7SignalingNodeTimersT8_Type())
acSS7SignalingNodeTimersT8.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersT8.setStatus(_A)
class _AcSS7SignalingNodeTimersT10_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7SignalingNodeTimersT10_Type.__name__=_B
_AcSS7SignalingNodeTimersT10_Object=MibTableColumn
acSS7SignalingNodeTimersT10=_AcSS7SignalingNodeTimersT10_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,8),_AcSS7SignalingNodeTimersT10_Type())
acSS7SignalingNodeTimersT10.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersT10.setStatus(_A)
class _AcSS7SignalingNodeTimersT11_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7SignalingNodeTimersT11_Type.__name__=_B
_AcSS7SignalingNodeTimersT11_Object=MibTableColumn
acSS7SignalingNodeTimersT11=_AcSS7SignalingNodeTimersT11_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,9),_AcSS7SignalingNodeTimersT11_Type())
acSS7SignalingNodeTimersT11.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersT11.setStatus(_A)
class _AcSS7SignalingNodeTimersT15_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7SignalingNodeTimersT15_Type.__name__=_B
_AcSS7SignalingNodeTimersT15_Object=MibTableColumn
acSS7SignalingNodeTimersT15=_AcSS7SignalingNodeTimersT15_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,10),_AcSS7SignalingNodeTimersT15_Type())
acSS7SignalingNodeTimersT15.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersT15.setStatus(_A)
class _AcSS7SignalingNodeTimersT16_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7SignalingNodeTimersT16_Type.__name__=_B
_AcSS7SignalingNodeTimersT16_Object=MibTableColumn
acSS7SignalingNodeTimersT16=_AcSS7SignalingNodeTimersT16_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,11),_AcSS7SignalingNodeTimersT16_Type())
acSS7SignalingNodeTimersT16.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersT16.setStatus(_A)
class _AcSS7SignalingNodeTimersT18ITU_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7SignalingNodeTimersT18ITU_Type.__name__=_B
_AcSS7SignalingNodeTimersT18ITU_Object=MibTableColumn
acSS7SignalingNodeTimersT18ITU=_AcSS7SignalingNodeTimersT18ITU_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,12),_AcSS7SignalingNodeTimersT18ITU_Type())
acSS7SignalingNodeTimersT18ITU.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersT18ITU.setStatus(_A)
class _AcSS7SignalingNodeTimersT19ITU_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7SignalingNodeTimersT19ITU_Type.__name__=_B
_AcSS7SignalingNodeTimersT19ITU_Object=MibTableColumn
acSS7SignalingNodeTimersT19ITU=_AcSS7SignalingNodeTimersT19ITU_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,13),_AcSS7SignalingNodeTimersT19ITU_Type())
acSS7SignalingNodeTimersT19ITU.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersT19ITU.setStatus(_A)
class _AcSS7SignalingNodeTimersT20ITU_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7SignalingNodeTimersT20ITU_Type.__name__=_B
_AcSS7SignalingNodeTimersT20ITU_Object=MibTableColumn
acSS7SignalingNodeTimersT20ITU=_AcSS7SignalingNodeTimersT20ITU_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,14),_AcSS7SignalingNodeTimersT20ITU_Type())
acSS7SignalingNodeTimersT20ITU.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersT20ITU.setStatus(_A)
class _AcSS7SignalingNodeTimersT21ITU_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7SignalingNodeTimersT21ITU_Type.__name__=_B
_AcSS7SignalingNodeTimersT21ITU_Object=MibTableColumn
acSS7SignalingNodeTimersT21ITU=_AcSS7SignalingNodeTimersT21ITU_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,15),_AcSS7SignalingNodeTimersT21ITU_Type())
acSS7SignalingNodeTimersT21ITU.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersT21ITU.setStatus(_A)
class _AcSS7SignalingNodeTimersT24ITU_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7SignalingNodeTimersT24ITU_Type.__name__=_B
_AcSS7SignalingNodeTimersT24ITU_Object=MibTableColumn
acSS7SignalingNodeTimersT24ITU=_AcSS7SignalingNodeTimersT24ITU_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,16),_AcSS7SignalingNodeTimersT24ITU_Type())
acSS7SignalingNodeTimersT24ITU.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersT24ITU.setStatus(_A)
class _AcSS7SignalingNodeTimersT22ANSI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7SignalingNodeTimersT22ANSI_Type.__name__=_B
_AcSS7SignalingNodeTimersT22ANSI_Object=MibTableColumn
acSS7SignalingNodeTimersT22ANSI=_AcSS7SignalingNodeTimersT22ANSI_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,17),_AcSS7SignalingNodeTimersT22ANSI_Type())
acSS7SignalingNodeTimersT22ANSI.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersT22ANSI.setStatus(_A)
class _AcSS7SignalingNodeTimersT23ANSI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7SignalingNodeTimersT23ANSI_Type.__name__=_B
_AcSS7SignalingNodeTimersT23ANSI_Object=MibTableColumn
acSS7SignalingNodeTimersT23ANSI=_AcSS7SignalingNodeTimersT23ANSI_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,18),_AcSS7SignalingNodeTimersT23ANSI_Type())
acSS7SignalingNodeTimersT23ANSI.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersT23ANSI.setStatus(_A)
class _AcSS7SignalingNodeTimersT24ANSI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7SignalingNodeTimersT24ANSI_Type.__name__=_B
_AcSS7SignalingNodeTimersT24ANSI_Object=MibTableColumn
acSS7SignalingNodeTimersT24ANSI=_AcSS7SignalingNodeTimersT24ANSI_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,19),_AcSS7SignalingNodeTimersT24ANSI_Type())
acSS7SignalingNodeTimersT24ANSI.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersT24ANSI.setStatus(_A)
class _AcSS7SignalingNodeTimersT25ANSI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7SignalingNodeTimersT25ANSI_Type.__name__=_B
_AcSS7SignalingNodeTimersT25ANSI_Object=MibTableColumn
acSS7SignalingNodeTimersT25ANSI=_AcSS7SignalingNodeTimersT25ANSI_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,20),_AcSS7SignalingNodeTimersT25ANSI_Type())
acSS7SignalingNodeTimersT25ANSI.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersT25ANSI.setStatus(_A)
class _AcSS7SignalingNodeTimersT26ANSI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7SignalingNodeTimersT26ANSI_Type.__name__=_B
_AcSS7SignalingNodeTimersT26ANSI_Object=MibTableColumn
acSS7SignalingNodeTimersT26ANSI=_AcSS7SignalingNodeTimersT26ANSI_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,21),_AcSS7SignalingNodeTimersT26ANSI_Type())
acSS7SignalingNodeTimersT26ANSI.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersT26ANSI.setStatus(_A)
class _AcSS7SignalingNodeTimersT27ANSI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7SignalingNodeTimersT27ANSI_Type.__name__=_B
_AcSS7SignalingNodeTimersT27ANSI_Object=MibTableColumn
acSS7SignalingNodeTimersT27ANSI=_AcSS7SignalingNodeTimersT27ANSI_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,22),_AcSS7SignalingNodeTimersT27ANSI_Type())
acSS7SignalingNodeTimersT27ANSI.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersT27ANSI.setStatus(_A)
class _AcSS7SignalingNodeTimersT28ANSI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7SignalingNodeTimersT28ANSI_Type.__name__=_B
_AcSS7SignalingNodeTimersT28ANSI_Object=MibTableColumn
acSS7SignalingNodeTimersT28ANSI=_AcSS7SignalingNodeTimersT28ANSI_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,23),_AcSS7SignalingNodeTimersT28ANSI_Type())
acSS7SignalingNodeTimersT28ANSI.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersT28ANSI.setStatus(_A)
class _AcSS7SignalingNodeTimersT29ANSI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7SignalingNodeTimersT29ANSI_Type.__name__=_B
_AcSS7SignalingNodeTimersT29ANSI_Object=MibTableColumn
acSS7SignalingNodeTimersT29ANSI=_AcSS7SignalingNodeTimersT29ANSI_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,24),_AcSS7SignalingNodeTimersT29ANSI_Type())
acSS7SignalingNodeTimersT29ANSI.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersT29ANSI.setStatus(_A)
class _AcSS7SignalingNodeTimersT30ANSI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7SignalingNodeTimersT30ANSI_Type.__name__=_B
_AcSS7SignalingNodeTimersT30ANSI_Object=MibTableColumn
acSS7SignalingNodeTimersT30ANSI=_AcSS7SignalingNodeTimersT30ANSI_Object((1,3,6,1,4,1,5003,9,10,12,1,2,21,1,25),_AcSS7SignalingNodeTimersT30ANSI_Type())
acSS7SignalingNodeTimersT30ANSI.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersT30ANSI.setStatus(_A)
_AcSS7LinkSetTimersTable_Object=MibTable
acSS7LinkSetTimersTable=_AcSS7LinkSetTimersTable_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22))
if mibBuilder.loadTexts:acSS7LinkSetTimersTable.setStatus(_A)
_AcSS7LinkSetTimersEntry_Object=MibTableRow
acSS7LinkSetTimersEntry=_AcSS7LinkSetTimersEntry_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1))
acSS7LinkSetTimersEntry.setIndexNames((0,_H,_e))
if mibBuilder.loadTexts:acSS7LinkSetTimersEntry.setStatus(_A)
class _AcSS7LinkSetTimersIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_AcSS7LinkSetTimersIndex_Type.__name__=_B
_AcSS7LinkSetTimersIndex_Object=MibTableColumn
acSS7LinkSetTimersIndex=_AcSS7LinkSetTimersIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,1),_AcSS7LinkSetTimersIndex_Type())
acSS7LinkSetTimersIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7LinkSetTimersIndex.setStatus(_A)
class _AcSS7LinkSetTimersIsUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_R,1)))
_AcSS7LinkSetTimersIsUsed_Type.__name__=_D
_AcSS7LinkSetTimersIsUsed_Object=MibTableColumn
acSS7LinkSetTimersIsUsed=_AcSS7LinkSetTimersIsUsed_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,2),_AcSS7LinkSetTimersIsUsed_Type())
acSS7LinkSetTimersIsUsed.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7LinkSetTimersIsUsed.setStatus(_A)
class _AcSS7LinkSetTimersAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues((_J,0))
_AcSS7LinkSetTimersAction_Type.__name__=_D
_AcSS7LinkSetTimersAction_Object=MibTableColumn
acSS7LinkSetTimersAction=_AcSS7LinkSetTimersAction_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,3),_AcSS7LinkSetTimersAction_Type())
acSS7LinkSetTimersAction.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7LinkSetTimersAction.setStatus(_A)
class _AcSS7LinkSetTimersActionResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2)))
_AcSS7LinkSetTimersActionResult_Type.__name__=_D
_AcSS7LinkSetTimersActionResult_Object=MibTableColumn
acSS7LinkSetTimersActionResult=_AcSS7LinkSetTimersActionResult_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,4),_AcSS7LinkSetTimersActionResult_Type())
acSS7LinkSetTimersActionResult.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7LinkSetTimersActionResult.setStatus(_A)
class _AcSS7LinkSetTimersName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AcSS7LinkSetTimersName_Type.__name__=_M
_AcSS7LinkSetTimersName_Object=MibTableColumn
acSS7LinkSetTimersName=_AcSS7LinkSetTimersName_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,5),_AcSS7LinkSetTimersName_Type())
acSS7LinkSetTimersName.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7LinkSetTimersName.setStatus(_A)
class _AcSS7LinkSetTimersT1SLT_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7LinkSetTimersT1SLT_Type.__name__=_B
_AcSS7LinkSetTimersT1SLT_Object=MibTableColumn
acSS7LinkSetTimersT1SLT=_AcSS7LinkSetTimersT1SLT_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,6),_AcSS7LinkSetTimersT1SLT_Type())
acSS7LinkSetTimersT1SLT.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7LinkSetTimersT1SLT.setStatus(_A)
class _AcSS7LinkSetTimersT2SLT_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7LinkSetTimersT2SLT_Type.__name__=_B
_AcSS7LinkSetTimersT2SLT_Object=MibTableColumn
acSS7LinkSetTimersT2SLT=_AcSS7LinkSetTimersT2SLT_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,7),_AcSS7LinkSetTimersT2SLT_Type())
acSS7LinkSetTimersT2SLT.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7LinkSetTimersT2SLT.setStatus(_A)
class _AcSS7LinkSetTimersT1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7LinkSetTimersT1_Type.__name__=_B
_AcSS7LinkSetTimersT1_Object=MibTableColumn
acSS7LinkSetTimersT1=_AcSS7LinkSetTimersT1_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,8),_AcSS7LinkSetTimersT1_Type())
acSS7LinkSetTimersT1.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7LinkSetTimersT1.setStatus(_A)
class _AcSS7LinkSetTimersT2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7LinkSetTimersT2_Type.__name__=_B
_AcSS7LinkSetTimersT2_Object=MibTableColumn
acSS7LinkSetTimersT2=_AcSS7LinkSetTimersT2_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,9),_AcSS7LinkSetTimersT2_Type())
acSS7LinkSetTimersT2.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7LinkSetTimersT2.setStatus(_A)
class _AcSS7LinkSetTimersT3_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7LinkSetTimersT3_Type.__name__=_B
_AcSS7LinkSetTimersT3_Object=MibTableColumn
acSS7LinkSetTimersT3=_AcSS7LinkSetTimersT3_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,10),_AcSS7LinkSetTimersT3_Type())
acSS7LinkSetTimersT3.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7LinkSetTimersT3.setStatus(_A)
class _AcSS7LinkSetTimersT4_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7LinkSetTimersT4_Type.__name__=_B
_AcSS7LinkSetTimersT4_Object=MibTableColumn
acSS7LinkSetTimersT4=_AcSS7LinkSetTimersT4_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,11),_AcSS7LinkSetTimersT4_Type())
acSS7LinkSetTimersT4.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7LinkSetTimersT4.setStatus(_A)
class _AcSS7LinkSetTimersT5_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7LinkSetTimersT5_Type.__name__=_B
_AcSS7LinkSetTimersT5_Object=MibTableColumn
acSS7LinkSetTimersT5=_AcSS7LinkSetTimersT5_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,12),_AcSS7LinkSetTimersT5_Type())
acSS7LinkSetTimersT5.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7LinkSetTimersT5.setStatus(_A)
class _AcSS7LinkSetTimersT7_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7LinkSetTimersT7_Type.__name__=_B
_AcSS7LinkSetTimersT7_Object=MibTableColumn
acSS7LinkSetTimersT7=_AcSS7LinkSetTimersT7_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,13),_AcSS7LinkSetTimersT7_Type())
acSS7LinkSetTimersT7.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7LinkSetTimersT7.setStatus(_A)
class _AcSS7LinkSetTimersT12_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7LinkSetTimersT12_Type.__name__=_B
_AcSS7LinkSetTimersT12_Object=MibTableColumn
acSS7LinkSetTimersT12=_AcSS7LinkSetTimersT12_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,14),_AcSS7LinkSetTimersT12_Type())
acSS7LinkSetTimersT12.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7LinkSetTimersT12.setStatus(_A)
class _AcSS7LinkSetTimersT13_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7LinkSetTimersT13_Type.__name__=_B
_AcSS7LinkSetTimersT13_Object=MibTableColumn
acSS7LinkSetTimersT13=_AcSS7LinkSetTimersT13_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,15),_AcSS7LinkSetTimersT13_Type())
acSS7LinkSetTimersT13.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7LinkSetTimersT13.setStatus(_A)
class _AcSS7LinkSetTimersT14_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7LinkSetTimersT14_Type.__name__=_B
_AcSS7LinkSetTimersT14_Object=MibTableColumn
acSS7LinkSetTimersT14=_AcSS7LinkSetTimersT14_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,16),_AcSS7LinkSetTimersT14_Type())
acSS7LinkSetTimersT14.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7LinkSetTimersT14.setStatus(_A)
class _AcSS7LinkSetTimersT17_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7LinkSetTimersT17_Type.__name__=_B
_AcSS7LinkSetTimersT17_Object=MibTableColumn
acSS7LinkSetTimersT17=_AcSS7LinkSetTimersT17_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,17),_AcSS7LinkSetTimersT17_Type())
acSS7LinkSetTimersT17.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7LinkSetTimersT17.setStatus(_A)
class _AcSS7LinkSetTimersT20ANSI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7LinkSetTimersT20ANSI_Type.__name__=_B
_AcSS7LinkSetTimersT20ANSI_Object=MibTableColumn
acSS7LinkSetTimersT20ANSI=_AcSS7LinkSetTimersT20ANSI_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,18),_AcSS7LinkSetTimersT20ANSI_Type())
acSS7LinkSetTimersT20ANSI.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7LinkSetTimersT20ANSI.setStatus(_A)
class _AcSS7LinkSetTimersT21ANSI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7LinkSetTimersT21ANSI_Type.__name__=_B
_AcSS7LinkSetTimersT21ANSI_Object=MibTableColumn
acSS7LinkSetTimersT21ANSI=_AcSS7LinkSetTimersT21ANSI_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,19),_AcSS7LinkSetTimersT21ANSI_Type())
acSS7LinkSetTimersT21ANSI.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7LinkSetTimersT21ANSI.setStatus(_A)
class _AcSS7LinkSetTimersT22ITU_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7LinkSetTimersT22ITU_Type.__name__=_B
_AcSS7LinkSetTimersT22ITU_Object=MibTableColumn
acSS7LinkSetTimersT22ITU=_AcSS7LinkSetTimersT22ITU_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,20),_AcSS7LinkSetTimersT22ITU_Type())
acSS7LinkSetTimersT22ITU.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7LinkSetTimersT22ITU.setStatus(_A)
class _AcSS7LinkSetTimersT23ITU_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,2147483647))
_AcSS7LinkSetTimersT23ITU_Type.__name__=_B
_AcSS7LinkSetTimersT23ITU_Object=MibTableColumn
acSS7LinkSetTimersT23ITU=_AcSS7LinkSetTimersT23ITU_Object((1,3,6,1,4,1,5003,9,10,12,1,2,22,1,21),_AcSS7LinkSetTimersT23ITU_Type())
acSS7LinkSetTimersT23ITU.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7LinkSetTimersT23ITU.setStatus(_A)
_AcSS7Links_ObjectIdentity=ObjectIdentity
acSS7Links=_AcSS7Links_ObjectIdentity((1,3,6,1,4,1,5003,9,10,12,1,3))
_AcSS7LinkCommonTable_Object=MibTable
acSS7LinkCommonTable=_AcSS7LinkCommonTable_Object((1,3,6,1,4,1,5003,9,10,12,1,3,21))
if mibBuilder.loadTexts:acSS7LinkCommonTable.setStatus(_A)
_AcSS7LinkCommonEntry_Object=MibTableRow
acSS7LinkCommonEntry=_AcSS7LinkCommonEntry_Object((1,3,6,1,4,1,5003,9,10,12,1,3,21,1))
acSS7LinkCommonEntry.setIndexNames((0,_H,_U))
if mibBuilder.loadTexts:acSS7LinkCommonEntry.setStatus(_A)
class _AcSS7LinkCommonIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_AcSS7LinkCommonIndex_Type.__name__=_B
_AcSS7LinkCommonIndex_Object=MibTableColumn
acSS7LinkCommonIndex=_AcSS7LinkCommonIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,3,21,1,1),_AcSS7LinkCommonIndex_Type())
acSS7LinkCommonIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7LinkCommonIndex.setStatus(_A)
_AcSS7LinkCommonRowStatus_Type=RowStatus
_AcSS7LinkCommonRowStatus_Object=MibTableColumn
acSS7LinkCommonRowStatus=_AcSS7LinkCommonRowStatus_Object((1,3,6,1,4,1,5003,9,10,12,1,3,21,1,2),_AcSS7LinkCommonRowStatus_Type())
acSS7LinkCommonRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkCommonRowStatus.setStatus(_A)
class _AcSS7LinkCommonAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2),(_S,3),(_T,4),('inhibit',5),('unInhibit',6),('lpo',7),('lpr',8)))
_AcSS7LinkCommonAction_Type.__name__=_D
_AcSS7LinkCommonAction_Object=MibTableColumn
acSS7LinkCommonAction=_AcSS7LinkCommonAction_Object((1,3,6,1,4,1,5003,9,10,12,1,3,21,1,3),_AcSS7LinkCommonAction_Type())
acSS7LinkCommonAction.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkCommonAction.setStatus(_A)
class _AcSS7LinkCommonActionResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2)))
_AcSS7LinkCommonActionResult_Type.__name__=_D
_AcSS7LinkCommonActionResult_Object=MibTableColumn
acSS7LinkCommonActionResult=_AcSS7LinkCommonActionResult_Object((1,3,6,1,4,1,5003,9,10,12,1,3,21,1,4),_AcSS7LinkCommonActionResult_Type())
acSS7LinkCommonActionResult.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7LinkCommonActionResult.setStatus(_A)
class _AcSS7LinkCommonName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AcSS7LinkCommonName_Type.__name__=_M
_AcSS7LinkCommonName_Object=MibTableColumn
acSS7LinkCommonName=_AcSS7LinkCommonName_Object((1,3,6,1,4,1,5003,9,10,12,1,3,21,1,5),_AcSS7LinkCommonName_Type())
acSS7LinkCommonName.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkCommonName.setStatus(_A)
class _AcSS7LinkCommonAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*((_K,0),(_L,2)))
_AcSS7LinkCommonAdminState_Type.__name__=_D
_AcSS7LinkCommonAdminState_Object=MibTableColumn
acSS7LinkCommonAdminState=_AcSS7LinkCommonAdminState_Object((1,3,6,1,4,1,5003,9,10,12,1,3,21,1,6),_AcSS7LinkCommonAdminState_Type())
acSS7LinkCommonAdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7LinkCommonAdminState.setStatus(_A)
class _AcSS7LinkCommonOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),(_V,1),(_L,2)))
_AcSS7LinkCommonOperState_Type.__name__=_D
_AcSS7LinkCommonOperState_Object=MibTableColumn
acSS7LinkCommonOperState=_AcSS7LinkCommonOperState_Object((1,3,6,1,4,1,5003,9,10,12,1,3,21,1,7),_AcSS7LinkCommonOperState_Type())
acSS7LinkCommonOperState.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7LinkCommonOperState.setStatus(_A)
class _AcSS7LinkCommonTraceLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_f,0),(_g,1)))
_AcSS7LinkCommonTraceLevel_Type.__name__=_D
_AcSS7LinkCommonTraceLevel_Object=MibTableColumn
acSS7LinkCommonTraceLevel=_AcSS7LinkCommonTraceLevel_Object((1,3,6,1,4,1,5003,9,10,12,1,3,21,1,8),_AcSS7LinkCommonTraceLevel_Type())
acSS7LinkCommonTraceLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkCommonTraceLevel.setStatus(_A)
class _AcSS7LinkCommonL2TypeSelector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4)));namedValues=NamedValues(*(('nonetype-L2',0),('mtp2',1),('m2ua-mgc',2),(_h,4)))
_AcSS7LinkCommonL2TypeSelector_Type.__name__=_D
_AcSS7LinkCommonL2TypeSelector_Object=MibTableColumn
acSS7LinkCommonL2TypeSelector=_AcSS7LinkCommonL2TypeSelector_Object((1,3,6,1,4,1,5003,9,10,12,1,3,21,1,9),_AcSS7LinkCommonL2TypeSelector_Type())
acSS7LinkCommonL2TypeSelector.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkCommonL2TypeSelector.setStatus(_A)
class _AcSS7LinkCommonL3TypeSelector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('nonetype-L3',0),('m2ua-sg',1),('mtp3',2),('mtp2-tunneling',3),('mtp2OverIP',4),(_h,5)))
_AcSS7LinkCommonL3TypeSelector_Type.__name__=_D
_AcSS7LinkCommonL3TypeSelector_Object=MibTableColumn
acSS7LinkCommonL3TypeSelector=_AcSS7LinkCommonL3TypeSelector_Object((1,3,6,1,4,1,5003,9,10,12,1,3,21,1,10),_AcSS7LinkCommonL3TypeSelector_Type())
acSS7LinkCommonL3TypeSelector.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkCommonL3TypeSelector.setStatus(_A)
class _AcSS7LinkCommonVariant_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Z,1),(_a,2),(_b,3)))
_AcSS7LinkCommonVariant_Type.__name__=_D
_AcSS7LinkCommonVariant_Object=MibTableColumn
acSS7LinkCommonVariant=_AcSS7LinkCommonVariant_Object((1,3,6,1,4,1,5003,9,10,12,1,3,21,1,11),_AcSS7LinkCommonVariant_Type())
acSS7LinkCommonVariant.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkCommonVariant.setStatus(_A)
class _AcSS7LinkCommonMtcBusy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_R,1)))
_AcSS7LinkCommonMtcBusy_Type.__name__=_D
_AcSS7LinkCommonMtcBusy_Object=MibTableColumn
acSS7LinkCommonMtcBusy=_AcSS7LinkCommonMtcBusy_Object((1,3,6,1,4,1,5003,9,10,12,1,3,21,1,12),_AcSS7LinkCommonMtcBusy_Type())
acSS7LinkCommonMtcBusy.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7LinkCommonMtcBusy.setStatus(_A)
class _AcSS7LinkCommonRdcyBoardNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('rdcyBoardNum0',0),('rdcyBoardNum1',1),('rdcyBoardNum2',2)))
_AcSS7LinkCommonRdcyBoardNum_Type.__name__=_D
_AcSS7LinkCommonRdcyBoardNum_Object=MibTableColumn
acSS7LinkCommonRdcyBoardNum=_AcSS7LinkCommonRdcyBoardNum_Object((1,3,6,1,4,1,5003,9,10,12,1,3,21,1,13),_AcSS7LinkCommonRdcyBoardNum_Type())
acSS7LinkCommonRdcyBoardNum.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkCommonRdcyBoardNum.setStatus(_A)
class _AcSS7LinkCommonMonSuFilterRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('filterAll',0),('filterLSSUandFISU',1),('filterFISU',2),('noFilter',3)))
_AcSS7LinkCommonMonSuFilterRequest_Type.__name__=_D
_AcSS7LinkCommonMonSuFilterRequest_Object=MibTableColumn
acSS7LinkCommonMonSuFilterRequest=_AcSS7LinkCommonMonSuFilterRequest_Object((1,3,6,1,4,1,5003,9,10,12,1,3,21,1,14),_AcSS7LinkCommonMonSuFilterRequest_Type())
acSS7LinkCommonMonSuFilterRequest.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkCommonMonSuFilterRequest.setStatus(_A)
_AcSS7LinkTDMTable_Object=MibTable
acSS7LinkTDMTable=_AcSS7LinkTDMTable_Object((1,3,6,1,4,1,5003,9,10,12,1,3,22))
if mibBuilder.loadTexts:acSS7LinkTDMTable.setStatus(_A)
_AcSS7LinkTDMEntry_Object=MibTableRow
acSS7LinkTDMEntry=_AcSS7LinkTDMEntry_Object((1,3,6,1,4,1,5003,9,10,12,1,3,22,1))
acSS7LinkTDMEntry.setIndexNames((0,_H,_U))
if mibBuilder.loadTexts:acSS7LinkTDMEntry.setStatus(_A)
class _AcSS7LinkTDMTrunkNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,84))
_AcSS7LinkTDMTrunkNumber_Type.__name__=_D
_AcSS7LinkTDMTrunkNumber_Object=MibTableColumn
acSS7LinkTDMTrunkNumber=_AcSS7LinkTDMTrunkNumber_Object((1,3,6,1,4,1,5003,9,10,12,1,3,22,1,1),_AcSS7LinkTDMTrunkNumber_Type())
acSS7LinkTDMTrunkNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkTDMTrunkNumber.setStatus(_A)
class _AcSS7LinkTDMTimeSlotNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_AcSS7LinkTDMTimeSlotNumber_Type.__name__=_B
_AcSS7LinkTDMTimeSlotNumber_Object=MibTableColumn
acSS7LinkTDMTimeSlotNumber=_AcSS7LinkTDMTimeSlotNumber_Object((1,3,6,1,4,1,5003,9,10,12,1,3,22,1,2),_AcSS7LinkTDMTimeSlotNumber_Type())
acSS7LinkTDMTimeSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkTDMTimeSlotNumber.setStatus(_A)
class _AcSS7LinkTDMInhibit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unInhibited',0),('inhibited',1)))
_AcSS7LinkTDMInhibit_Type.__name__=_D
_AcSS7LinkTDMInhibit_Object=MibTableColumn
acSS7LinkTDMInhibit=_AcSS7LinkTDMInhibit_Object((1,3,6,1,4,1,5003,9,10,12,1,3,22,1,3),_AcSS7LinkTDMInhibit_Type())
acSS7LinkTDMInhibit.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7LinkTDMInhibit.setStatus(_A)
class _AcSS7LinkTDMMtp2Atts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('mtp2Atts0',0),('mtp2Atts1',1),('mtp2Atts2',2),('mtp2Atts3',3)))
_AcSS7LinkTDMMtp2Atts_Type.__name__=_D
_AcSS7LinkTDMMtp2Atts_Object=MibTableColumn
acSS7LinkTDMMtp2Atts=_AcSS7LinkTDMMtp2Atts_Object((1,3,6,1,4,1,5003,9,10,12,1,3,22,1,4),_AcSS7LinkTDMMtp2Atts_Type())
acSS7LinkTDMMtp2Atts.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkTDMMtp2Atts.setStatus(_A)
class _AcSS7LinkTDMCongestionLowMark_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcSS7LinkTDMCongestionLowMark_Type.__name__=_B
_AcSS7LinkTDMCongestionLowMark_Object=MibTableColumn
acSS7LinkTDMCongestionLowMark=_AcSS7LinkTDMCongestionLowMark_Object((1,3,6,1,4,1,5003,9,10,12,1,3,22,1,5),_AcSS7LinkTDMCongestionLowMark_Type())
acSS7LinkTDMCongestionLowMark.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkTDMCongestionLowMark.setStatus(_A)
class _AcSS7LinkTDMCongestionHighMark_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcSS7LinkTDMCongestionHighMark_Type.__name__=_B
_AcSS7LinkTDMCongestionHighMark_Object=MibTableColumn
acSS7LinkTDMCongestionHighMark=_AcSS7LinkTDMCongestionHighMark_Object((1,3,6,1,4,1,5003,9,10,12,1,3,22,1,6),_AcSS7LinkTDMCongestionHighMark_Type())
acSS7LinkTDMCongestionHighMark.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkTDMCongestionHighMark.setStatus(_A)
class _AcSS7LinkTDMBlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('l3linkunblocked',0),('l3linklocalblocked',1),('l3linkremoteblockde',2),('l3linklocalandremotelocked',3)))
_AcSS7LinkTDMBlock_Type.__name__=_D
_AcSS7LinkTDMBlock_Object=MibTableColumn
acSS7LinkTDMBlock=_AcSS7LinkTDMBlock_Object((1,3,6,1,4,1,5003,9,10,12,1,3,22,1,7),_AcSS7LinkTDMBlock_Type())
acSS7LinkTDMBlock.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7LinkTDMBlock.setStatus(_A)
_AcSS7LinkSigTranTable_Object=MibTable
acSS7LinkSigTranTable=_AcSS7LinkSigTranTable_Object((1,3,6,1,4,1,5003,9,10,12,1,3,23))
if mibBuilder.loadTexts:acSS7LinkSigTranTable.setStatus(_A)
_AcSS7LinkSigTranEntry_Object=MibTableRow
acSS7LinkSigTranEntry=_AcSS7LinkSigTranEntry_Object((1,3,6,1,4,1,5003,9,10,12,1,3,23,1))
acSS7LinkSigTranEntry.setIndexNames((0,_H,_U))
if mibBuilder.loadTexts:acSS7LinkSigTranEntry.setStatus(_A)
class _AcSS7LinkSigTranGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65534))
_AcSS7LinkSigTranGroupId_Type.__name__=_D
_AcSS7LinkSigTranGroupId_Object=MibTableColumn
acSS7LinkSigTranGroupId=_AcSS7LinkSigTranGroupId_Object((1,3,6,1,4,1,5003,9,10,12,1,3,23,1,1),_AcSS7LinkSigTranGroupId_Type())
acSS7LinkSigTranGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkSigTranGroupId.setStatus(_A)
class _AcSS7LinkSigTranIfid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcSS7LinkSigTranIfid_Type.__name__=_D
_AcSS7LinkSigTranIfid_Object=MibTableColumn
acSS7LinkSigTranIfid=_AcSS7LinkSigTranIfid_Object((1,3,6,1,4,1,5003,9,10,12,1,3,23,1,2),_AcSS7LinkSigTranIfid_Type())
acSS7LinkSigTranIfid.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkSigTranIfid.setStatus(_A)
_AcSS7LinkATMTable_Object=MibTable
acSS7LinkATMTable=_AcSS7LinkATMTable_Object((1,3,6,1,4,1,5003,9,10,12,1,3,24))
if mibBuilder.loadTexts:acSS7LinkATMTable.setStatus(_G)
_AcSS7LinkATMEntry_Object=MibTableRow
acSS7LinkATMEntry=_AcSS7LinkATMEntry_Object((1,3,6,1,4,1,5003,9,10,12,1,3,24,1))
acSS7LinkATMEntry.setIndexNames((0,_H,_U))
if mibBuilder.loadTexts:acSS7LinkATMEntry.setStatus(_G)
class _AcSS7LinkATMSAALLinkProfileNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AcSS7LinkATMSAALLinkProfileNum_Type.__name__=_B
_AcSS7LinkATMSAALLinkProfileNum_Object=MibTableColumn
acSS7LinkATMSAALLinkProfileNum=_AcSS7LinkATMSAALLinkProfileNum_Object((1,3,6,1,4,1,5003,9,10,12,1,3,24,1,1),_AcSS7LinkATMSAALLinkProfileNum_Type())
acSS7LinkATMSAALLinkProfileNum.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkATMSAALLinkProfileNum.setStatus(_G)
class _AcSS7LinkATMSAALLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('aTM-VCC-Type-PVC',0),('aTM-VCC-Type-SVC',1)))
_AcSS7LinkATMSAALLinkType_Type.__name__=_D
_AcSS7LinkATMSAALLinkType_Object=MibTableColumn
acSS7LinkATMSAALLinkType=_AcSS7LinkATMSAALLinkType_Object((1,3,6,1,4,1,5003,9,10,12,1,3,24,1,2),_AcSS7LinkATMSAALLinkType_Type())
acSS7LinkATMSAALLinkType.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkATMSAALLinkType.setStatus(_G)
class _AcSS7LinkATMSAALLinkInterfaceNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AcSS7LinkATMSAALLinkInterfaceNum_Type.__name__=_B
_AcSS7LinkATMSAALLinkInterfaceNum_Object=MibTableColumn
acSS7LinkATMSAALLinkInterfaceNum=_AcSS7LinkATMSAALLinkInterfaceNum_Object((1,3,6,1,4,1,5003,9,10,12,1,3,24,1,3),_AcSS7LinkATMSAALLinkInterfaceNum_Type())
acSS7LinkATMSAALLinkInterfaceNum.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkATMSAALLinkInterfaceNum.setStatus(_G)
class _AcSS7LinkATMSAALLinkVPI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcSS7LinkATMSAALLinkVPI_Type.__name__=_B
_AcSS7LinkATMSAALLinkVPI_Object=MibTableColumn
acSS7LinkATMSAALLinkVPI=_AcSS7LinkATMSAALLinkVPI_Object((1,3,6,1,4,1,5003,9,10,12,1,3,24,1,4),_AcSS7LinkATMSAALLinkVPI_Type())
acSS7LinkATMSAALLinkVPI.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkATMSAALLinkVPI.setStatus(_G)
class _AcSS7LinkATMSAALLinkVCI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_AcSS7LinkATMSAALLinkVCI_Type.__name__=_B
_AcSS7LinkATMSAALLinkVCI_Object=MibTableColumn
acSS7LinkATMSAALLinkVCI=_AcSS7LinkATMSAALLinkVCI_Object((1,3,6,1,4,1,5003,9,10,12,1,3,24,1,5),_AcSS7LinkATMSAALLinkVCI_Type())
acSS7LinkATMSAALLinkVCI.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkATMSAALLinkVCI.setStatus(_G)
_AcSS7LinkTNLTable_Object=MibTable
acSS7LinkTNLTable=_AcSS7LinkTNLTable_Object((1,3,6,1,4,1,5003,9,10,12,1,3,25))
if mibBuilder.loadTexts:acSS7LinkTNLTable.setStatus(_A)
_AcSS7LinkTNLEntry_Object=MibTableRow
acSS7LinkTNLEntry=_AcSS7LinkTNLEntry_Object((1,3,6,1,4,1,5003,9,10,12,1,3,25,1))
acSS7LinkTNLEntry.setIndexNames((0,_H,_U))
if mibBuilder.loadTexts:acSS7LinkTNLEntry.setStatus(_A)
class _AcSS7LinkTNLOtherSideLinkNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AcSS7LinkTNLOtherSideLinkNum_Type.__name__=_B
_AcSS7LinkTNLOtherSideLinkNum_Object=MibTableColumn
acSS7LinkTNLOtherSideLinkNum=_AcSS7LinkTNLOtherSideLinkNum_Object((1,3,6,1,4,1,5003,9,10,12,1,3,25,1,1),_AcSS7LinkTNLOtherSideLinkNum_Type())
acSS7LinkTNLOtherSideLinkNum.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkTNLOtherSideLinkNum.setStatus(_A)
class _AcSS7LinkTNLAlignmentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('emergency',1)))
_AcSS7LinkTNLAlignmentMode_Type.__name__=_D
_AcSS7LinkTNLAlignmentMode_Object=MibTableColumn
acSS7LinkTNLAlignmentMode=_AcSS7LinkTNLAlignmentMode_Object((1,3,6,1,4,1,5003,9,10,12,1,3,25,1,2),_AcSS7LinkTNLAlignmentMode_Type())
acSS7LinkTNLAlignmentMode.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkTNLAlignmentMode.setStatus(_A)
class _AcSS7LinkTNLCongestionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('accept',0),('discard',1)))
_AcSS7LinkTNLCongestionMode_Type.__name__=_D
_AcSS7LinkTNLCongestionMode_Object=MibTableColumn
acSS7LinkTNLCongestionMode=_AcSS7LinkTNLCongestionMode_Object((1,3,6,1,4,1,5003,9,10,12,1,3,25,1,3),_AcSS7LinkTNLCongestionMode_Type())
acSS7LinkTNLCongestionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkTNLCongestionMode.setStatus(_A)
class _AcSS7LinkTNLWaitStartCompTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7LinkTNLWaitStartCompTimer_Type.__name__=_B
_AcSS7LinkTNLWaitStartCompTimer_Object=MibTableColumn
acSS7LinkTNLWaitStartCompTimer=_AcSS7LinkTNLWaitStartCompTimer_Object((1,3,6,1,4,1,5003,9,10,12,1,3,25,1,4),_AcSS7LinkTNLWaitStartCompTimer_Type())
acSS7LinkTNLWaitStartCompTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkTNLWaitStartCompTimer.setStatus(_A)
class _AcSS7LinkTNLOosStartDelayTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7LinkTNLOosStartDelayTimer_Type.__name__=_B
_AcSS7LinkTNLOosStartDelayTimer_Object=MibTableColumn
acSS7LinkTNLOosStartDelayTimer=_AcSS7LinkTNLOosStartDelayTimer_Object((1,3,6,1,4,1,5003,9,10,12,1,3,25,1,5),_AcSS7LinkTNLOosStartDelayTimer_Type())
acSS7LinkTNLOosStartDelayTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkTNLOosStartDelayTimer.setStatus(_A)
class _AcSS7LinkTNLWaitOtherSideInsvTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7LinkTNLWaitOtherSideInsvTimer_Type.__name__=_B
_AcSS7LinkTNLWaitOtherSideInsvTimer_Object=MibTableColumn
acSS7LinkTNLWaitOtherSideInsvTimer=_AcSS7LinkTNLWaitOtherSideInsvTimer_Object((1,3,6,1,4,1,5003,9,10,12,1,3,25,1,6),_AcSS7LinkTNLWaitOtherSideInsvTimer_Type())
acSS7LinkTNLWaitOtherSideInsvTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkTNLWaitOtherSideInsvTimer.setStatus(_A)
_AcSS7Nodes_ObjectIdentity=ObjectIdentity
acSS7Nodes=_AcSS7Nodes_ObjectIdentity((1,3,6,1,4,1,5003,9,10,12,1,4))
_AcSS7SignalingNodeTable_Object=MibTable
acSS7SignalingNodeTable=_AcSS7SignalingNodeTable_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21))
if mibBuilder.loadTexts:acSS7SignalingNodeTable.setStatus(_A)
_AcSS7SignalingNodeEntry_Object=MibTableRow
acSS7SignalingNodeEntry=_AcSS7SignalingNodeEntry_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1))
acSS7SignalingNodeEntry.setIndexNames((0,_H,_i))
if mibBuilder.loadTexts:acSS7SignalingNodeEntry.setStatus(_A)
class _AcSS7SignalingNodeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AcSS7SignalingNodeIndex_Type.__name__=_B
_AcSS7SignalingNodeIndex_Object=MibTableColumn
acSS7SignalingNodeIndex=_AcSS7SignalingNodeIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,1),_AcSS7SignalingNodeIndex_Type())
acSS7SignalingNodeIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7SignalingNodeIndex.setStatus(_A)
_AcSS7SignalingNodeRowStatus_Type=RowStatus
_AcSS7SignalingNodeRowStatus_Object=MibTableColumn
acSS7SignalingNodeRowStatus=_AcSS7SignalingNodeRowStatus_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,2),_AcSS7SignalingNodeRowStatus_Type())
acSS7SignalingNodeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SignalingNodeRowStatus.setStatus(_A)
class _AcSS7SignalingNodeAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_J,0),('stop',1),('start',2),(_L,3),(_K,4)))
_AcSS7SignalingNodeAction_Type.__name__=_D
_AcSS7SignalingNodeAction_Object=MibTableColumn
acSS7SignalingNodeAction=_AcSS7SignalingNodeAction_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,3),_AcSS7SignalingNodeAction_Type())
acSS7SignalingNodeAction.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SignalingNodeAction.setStatus(_A)
class _AcSS7SignalingNodeActionResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2)))
_AcSS7SignalingNodeActionResult_Type.__name__=_D
_AcSS7SignalingNodeActionResult_Object=MibTableColumn
acSS7SignalingNodeActionResult=_AcSS7SignalingNodeActionResult_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,4),_AcSS7SignalingNodeActionResult_Type())
acSS7SignalingNodeActionResult.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7SignalingNodeActionResult.setStatus(_A)
class _AcSS7SignalingNodeName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AcSS7SignalingNodeName_Type.__name__=_M
_AcSS7SignalingNodeName_Object=MibTableColumn
acSS7SignalingNodeName=_AcSS7SignalingNodeName_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,5),_AcSS7SignalingNodeName_Type())
acSS7SignalingNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SignalingNodeName.setStatus(_A)
class _AcSS7SignalingNodeTraceLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_f,0),(_g,1)))
_AcSS7SignalingNodeTraceLevel_Type.__name__=_D
_AcSS7SignalingNodeTraceLevel_Object=MibTableColumn
acSS7SignalingNodeTraceLevel=_AcSS7SignalingNodeTraceLevel_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,6),_AcSS7SignalingNodeTraceLevel_Type())
acSS7SignalingNodeTraceLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SignalingNodeTraceLevel.setStatus(_A)
class _AcSS7SignalingNodeAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*((_K,0),(_L,2)))
_AcSS7SignalingNodeAdminState_Type.__name__=_D
_AcSS7SignalingNodeAdminState_Object=MibTableColumn
acSS7SignalingNodeAdminState=_AcSS7SignalingNodeAdminState_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,7),_AcSS7SignalingNodeAdminState_Type())
acSS7SignalingNodeAdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7SignalingNodeAdminState.setStatus(_A)
class _AcSS7SignalingNodeOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),(_V,1),(_L,2)))
_AcSS7SignalingNodeOperState_Type.__name__=_D
_AcSS7SignalingNodeOperState_Object=MibTableColumn
acSS7SignalingNodeOperState=_AcSS7SignalingNodeOperState_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,8),_AcSS7SignalingNodeOperState_Type())
acSS7SignalingNodeOperState.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7SignalingNodeOperState.setStatus(_A)
class _AcSS7SignalingNodeMtcBusy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_R,1)))
_AcSS7SignalingNodeMtcBusy_Type.__name__=_D
_AcSS7SignalingNodeMtcBusy_Object=MibTableColumn
acSS7SignalingNodeMtcBusy=_AcSS7SignalingNodeMtcBusy_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,9),_AcSS7SignalingNodeMtcBusy_Type())
acSS7SignalingNodeMtcBusy.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7SignalingNodeMtcBusy.setStatus(_A)
class _AcSS7SignalingNodeVariant_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Z,1),(_a,2),(_b,3)))
_AcSS7SignalingNodeVariant_Type.__name__=_D
_AcSS7SignalingNodeVariant_Object=MibTableColumn
acSS7SignalingNodeVariant=_AcSS7SignalingNodeVariant_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,10),_AcSS7SignalingNodeVariant_Type())
acSS7SignalingNodeVariant.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SignalingNodeVariant.setStatus(_A)
class _AcSS7SignalingNodeNwIndicator_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('international',0),('internationalSpare',1),('national',2),('nationalSpare',3)))
_AcSS7SignalingNodeNwIndicator_Type.__name__=_D
_AcSS7SignalingNodeNwIndicator_Object=MibTableColumn
acSS7SignalingNodeNwIndicator=_AcSS7SignalingNodeNwIndicator_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,11),_AcSS7SignalingNodeNwIndicator_Type())
acSS7SignalingNodeNwIndicator.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SignalingNodeNwIndicator.setStatus(_A)
class _AcSS7SignalingNodeSpStp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('sp',0),('stp',1)))
_AcSS7SignalingNodeSpStp_Type.__name__=_D
_AcSS7SignalingNodeSpStp_Object=MibTableColumn
acSS7SignalingNodeSpStp=_AcSS7SignalingNodeSpStp_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,12),_AcSS7SignalingNodeSpStp_Type())
acSS7SignalingNodeSpStp.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SignalingNodeSpStp.setStatus(_A)
class _AcSS7SignalingNodeTfc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_R,1)))
_AcSS7SignalingNodeTfc_Type.__name__=_D
_AcSS7SignalingNodeTfc_Object=MibTableColumn
acSS7SignalingNodeTfc=_AcSS7SignalingNodeTfc_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,13),_AcSS7SignalingNodeTfc_Type())
acSS7SignalingNodeTfc.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SignalingNodeTfc.setStatus(_A)
class _AcSS7SignalingNodeOpc_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7SignalingNodeOpc_Type.__name__=_B
_AcSS7SignalingNodeOpc_Object=MibTableColumn
acSS7SignalingNodeOpc=_AcSS7SignalingNodeOpc_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,14),_AcSS7SignalingNodeOpc_Type())
acSS7SignalingNodeOpc.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SignalingNodeOpc.setStatus(_A)
class _AcSS7SignalingNodeRouteSetCongestionWindow_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcSS7SignalingNodeRouteSetCongestionWindow_Type.__name__=_B
_AcSS7SignalingNodeRouteSetCongestionWindow_Object=MibTableColumn
acSS7SignalingNodeRouteSetCongestionWindow=_AcSS7SignalingNodeRouteSetCongestionWindow_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,15),_AcSS7SignalingNodeRouteSetCongestionWindow_Type())
acSS7SignalingNodeRouteSetCongestionWindow.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SignalingNodeRouteSetCongestionWindow.setStatus(_A)
class _AcSS7SignalingNodeTimersIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_j,0),(_k,1),(_l,2),(_m,3),(_n,4)))
_AcSS7SignalingNodeTimersIdx_Type.__name__=_D
_AcSS7SignalingNodeTimersIdx_Object=MibTableColumn
acSS7SignalingNodeTimersIdx=_AcSS7SignalingNodeTimersIdx_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,16),_AcSS7SignalingNodeTimersIdx_Type())
acSS7SignalingNodeTimersIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SignalingNodeTimersIdx.setStatus(_A)
class _AcSS7SignalingNodeIsupApp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4,7)));namedValues=NamedValues(*((_X,0),(_W,4),(_Y,7)))
_AcSS7SignalingNodeIsupApp_Type.__name__=_D
_AcSS7SignalingNodeIsupApp_Object=MibTableColumn
acSS7SignalingNodeIsupApp=_AcSS7SignalingNodeIsupApp_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,17),_AcSS7SignalingNodeIsupApp_Type())
acSS7SignalingNodeIsupApp.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SignalingNodeIsupApp.setStatus(_A)
class _AcSS7SignalingNodeSccpApp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4,7)));namedValues=NamedValues(*((_X,0),(_W,4),(_Y,7)))
_AcSS7SignalingNodeSccpApp_Type.__name__=_D
_AcSS7SignalingNodeSccpApp_Object=MibTableColumn
acSS7SignalingNodeSccpApp=_AcSS7SignalingNodeSccpApp_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,18),_AcSS7SignalingNodeSccpApp_Type())
acSS7SignalingNodeSccpApp.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SignalingNodeSccpApp.setStatus(_A)
class _AcSS7SignalingNodeBisupApp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4,7)));namedValues=NamedValues(*((_X,0),(_W,4),(_Y,7)))
_AcSS7SignalingNodeBisupApp_Type.__name__=_D
_AcSS7SignalingNodeBisupApp_Object=MibTableColumn
acSS7SignalingNodeBisupApp=_AcSS7SignalingNodeBisupApp_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,19),_AcSS7SignalingNodeBisupApp_Type())
acSS7SignalingNodeBisupApp.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SignalingNodeBisupApp.setStatus(_A)
class _AcSS7SignalingNodeAlcapApp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4,5,7)));namedValues=NamedValues(*((_X,0),(_W,4),('alcap',5),(_Y,7)))
_AcSS7SignalingNodeAlcapApp_Type.__name__=_D
_AcSS7SignalingNodeAlcapApp_Object=MibTableColumn
acSS7SignalingNodeAlcapApp=_AcSS7SignalingNodeAlcapApp_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,20),_AcSS7SignalingNodeAlcapApp_Type())
acSS7SignalingNodeAlcapApp.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SignalingNodeAlcapApp.setStatus('deprecated')
class _AcSS7SignalingNodeRdcyOpc_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7SignalingNodeRdcyOpc_Type.__name__=_B
_AcSS7SignalingNodeRdcyOpc_Object=MibTableColumn
acSS7SignalingNodeRdcyOpc=_AcSS7SignalingNodeRdcyOpc_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,21),_AcSS7SignalingNodeRdcyOpc_Type())
acSS7SignalingNodeRdcyOpc.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7SignalingNodeRdcyOpc.setStatus(_A)
class _AcSS7SignalingNodeTupApp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4,7)));namedValues=NamedValues(*((_X,0),(_W,4),(_Y,7)))
_AcSS7SignalingNodeTupApp_Type.__name__=_D
_AcSS7SignalingNodeTupApp_Object=MibTableColumn
acSS7SignalingNodeTupApp=_AcSS7SignalingNodeTupApp_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,22),_AcSS7SignalingNodeTupApp_Type())
acSS7SignalingNodeTupApp.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SignalingNodeTupApp.setStatus(_A)
class _AcSS7SignalingNodeBiccApp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4)));namedValues=NamedValues(*(('nil',0),(_W,4)))
_AcSS7SignalingNodeBiccApp_Type.__name__=_D
_AcSS7SignalingNodeBiccApp_Object=MibTableColumn
acSS7SignalingNodeBiccApp=_AcSS7SignalingNodeBiccApp_Object((1,3,6,1,4,1,5003,9,10,12,1,4,21,1,23),_AcSS7SignalingNodeBiccApp_Type())
acSS7SignalingNodeBiccApp.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SignalingNodeBiccApp.setStatus(_A)
_AcSS7LinkSets_ObjectIdentity=ObjectIdentity
acSS7LinkSets=_AcSS7LinkSets_ObjectIdentity((1,3,6,1,4,1,5003,9,10,12,1,4,31))
_AcSS7LinkSetTable_Object=MibTable
acSS7LinkSetTable=_AcSS7LinkSetTable_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,21))
if mibBuilder.loadTexts:acSS7LinkSetTable.setStatus(_A)
_AcSS7LinkSetEntry_Object=MibTableRow
acSS7LinkSetEntry=_AcSS7LinkSetEntry_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,21,1))
acSS7LinkSetEntry.setIndexNames((0,_H,_o),(0,_H,_p))
if mibBuilder.loadTexts:acSS7LinkSetEntry.setStatus(_A)
class _AcSS7LinkSetSNIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AcSS7LinkSetSNIndex_Type.__name__=_B
_AcSS7LinkSetSNIndex_Object=MibTableColumn
acSS7LinkSetSNIndex=_AcSS7LinkSetSNIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,21,1,1),_AcSS7LinkSetSNIndex_Type())
acSS7LinkSetSNIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7LinkSetSNIndex.setStatus(_A)
class _AcSS7LinkSetLksetIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_AcSS7LinkSetLksetIndex_Type.__name__=_B
_AcSS7LinkSetLksetIndex_Object=MibTableColumn
acSS7LinkSetLksetIndex=_AcSS7LinkSetLksetIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,21,1,2),_AcSS7LinkSetLksetIndex_Type())
acSS7LinkSetLksetIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7LinkSetLksetIndex.setStatus(_A)
_AcSS7LinkSetRowStatus_Type=RowStatus
_AcSS7LinkSetRowStatus_Object=MibTableColumn
acSS7LinkSetRowStatus=_AcSS7LinkSetRowStatus_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,21,1,3),_AcSS7LinkSetRowStatus_Type())
acSS7LinkSetRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkSetRowStatus.setStatus(_A)
class _AcSS7LinkSetAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2),(_S,3),(_T,4)))
_AcSS7LinkSetAction_Type.__name__=_D
_AcSS7LinkSetAction_Object=MibTableColumn
acSS7LinkSetAction=_AcSS7LinkSetAction_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,21,1,4),_AcSS7LinkSetAction_Type())
acSS7LinkSetAction.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkSetAction.setStatus(_A)
class _AcSS7LinkSetActionResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2)))
_AcSS7LinkSetActionResult_Type.__name__=_D
_AcSS7LinkSetActionResult_Object=MibTableColumn
acSS7LinkSetActionResult=_AcSS7LinkSetActionResult_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,21,1,5),_AcSS7LinkSetActionResult_Type())
acSS7LinkSetActionResult.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7LinkSetActionResult.setStatus(_A)
class _AcSS7LinkSetName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AcSS7LinkSetName_Type.__name__=_M
_AcSS7LinkSetName_Object=MibTableColumn
acSS7LinkSetName=_AcSS7LinkSetName_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,21,1,6),_AcSS7LinkSetName_Type())
acSS7LinkSetName.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkSetName.setStatus(_A)
class _AcSS7LinkSetAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*((_K,0),(_L,2)))
_AcSS7LinkSetAdminState_Type.__name__=_D
_AcSS7LinkSetAdminState_Object=MibTableColumn
acSS7LinkSetAdminState=_AcSS7LinkSetAdminState_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,21,1,7),_AcSS7LinkSetAdminState_Type())
acSS7LinkSetAdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7LinkSetAdminState.setStatus(_A)
class _AcSS7LinkSetOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),(_V,1),(_L,2)))
_AcSS7LinkSetOperState_Type.__name__=_D
_AcSS7LinkSetOperState_Object=MibTableColumn
acSS7LinkSetOperState=_AcSS7LinkSetOperState_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,21,1,8),_AcSS7LinkSetOperState_Type())
acSS7LinkSetOperState.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7LinkSetOperState.setStatus(_A)
class _AcSS7LinkSetMtcBusyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_R,1)))
_AcSS7LinkSetMtcBusyState_Type.__name__=_D
_AcSS7LinkSetMtcBusyState_Object=MibTableColumn
acSS7LinkSetMtcBusyState=_AcSS7LinkSetMtcBusyState_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,21,1,9),_AcSS7LinkSetMtcBusyState_Type())
acSS7LinkSetMtcBusyState.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7LinkSetMtcBusyState.setStatus(_A)
class _AcSS7LinkSetDPC_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7LinkSetDPC_Type.__name__=_B
_AcSS7LinkSetDPC_Object=MibTableColumn
acSS7LinkSetDPC=_AcSS7LinkSetDPC_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,21,1,10),_AcSS7LinkSetDPC_Type())
acSS7LinkSetDPC.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkSetDPC.setStatus(_A)
class _AcSS7LinkSetLinksMask_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcSS7LinkSetLinksMask_Type.__name__=_B
_AcSS7LinkSetLinksMask_Object=MibTableColumn
acSS7LinkSetLinksMask=_AcSS7LinkSetLinksMask_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,21,1,11),_AcSS7LinkSetLinksMask_Type())
acSS7LinkSetLinksMask.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkSetLinksMask.setStatus(_A)
class _AcSS7LinkSetLinksAltMask_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcSS7LinkSetLinksAltMask_Type.__name__=_B
_AcSS7LinkSetLinksAltMask_Object=MibTableColumn
acSS7LinkSetLinksAltMask=_AcSS7LinkSetLinksAltMask_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,21,1,12),_AcSS7LinkSetLinksAltMask_Type())
acSS7LinkSetLinksAltMask.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkSetLinksAltMask.setStatus(_A)
class _AcSS7LinkSetTimersIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_j,0),(_k,1),(_l,2),(_m,3),(_n,4)))
_AcSS7LinkSetTimersIdx_Type.__name__=_D
_AcSS7LinkSetTimersIdx_Object=MibTableColumn
acSS7LinkSetTimersIdx=_AcSS7LinkSetTimersIdx_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,21,1,13),_AcSS7LinkSetTimersIdx_Type())
acSS7LinkSetTimersIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkSetTimersIdx.setStatus(_A)
_AcSS7LinkSetLinkTable_Object=MibTable
acSS7LinkSetLinkTable=_AcSS7LinkSetLinkTable_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,22))
if mibBuilder.loadTexts:acSS7LinkSetLinkTable.setStatus(_A)
_AcSS7LinkSetLinkEntry_Object=MibTableRow
acSS7LinkSetLinkEntry=_AcSS7LinkSetLinkEntry_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,22,1))
acSS7LinkSetLinkEntry.setIndexNames((0,_H,_q),(0,_H,_r),(0,_H,_s))
if mibBuilder.loadTexts:acSS7LinkSetLinkEntry.setStatus(_A)
class _AcSS7LinkSetLinkSNIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AcSS7LinkSetLinkSNIndex_Type.__name__=_B
_AcSS7LinkSetLinkSNIndex_Object=MibTableColumn
acSS7LinkSetLinkSNIndex=_AcSS7LinkSetLinkSNIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,22,1,1),_AcSS7LinkSetLinkSNIndex_Type())
acSS7LinkSetLinkSNIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7LinkSetLinkSNIndex.setStatus(_A)
class _AcSS7LinkSetLinkLinksetIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_AcSS7LinkSetLinkLinksetIndex_Type.__name__=_B
_AcSS7LinkSetLinkLinksetIndex_Object=MibTableColumn
acSS7LinkSetLinkLinksetIndex=_AcSS7LinkSetLinkLinksetIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,22,1,2),_AcSS7LinkSetLinkLinksetIndex_Type())
acSS7LinkSetLinkLinksetIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7LinkSetLinkLinksetIndex.setStatus(_A)
class _AcSS7LinkSetLinkInnerLinkIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AcSS7LinkSetLinkInnerLinkIndex_Type.__name__=_B
_AcSS7LinkSetLinkInnerLinkIndex_Object=MibTableColumn
acSS7LinkSetLinkInnerLinkIndex=_AcSS7LinkSetLinkInnerLinkIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,22,1,3),_AcSS7LinkSetLinkInnerLinkIndex_Type())
acSS7LinkSetLinkInnerLinkIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7LinkSetLinkInnerLinkIndex.setStatus(_A)
_AcSS7LinkSetLinkRowStatus_Type=RowStatus
_AcSS7LinkSetLinkRowStatus_Object=MibTableColumn
acSS7LinkSetLinkRowStatus=_AcSS7LinkSetLinkRowStatus_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,22,1,4),_AcSS7LinkSetLinkRowStatus_Type())
acSS7LinkSetLinkRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkSetLinkRowStatus.setStatus(_A)
class _AcSS7LinkSetLinkAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues((_J,0))
_AcSS7LinkSetLinkAction_Type.__name__=_D
_AcSS7LinkSetLinkAction_Object=MibTableColumn
acSS7LinkSetLinkAction=_AcSS7LinkSetLinkAction_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,22,1,5),_AcSS7LinkSetLinkAction_Type())
acSS7LinkSetLinkAction.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkSetLinkAction.setStatus(_A)
class _AcSS7LinkSetLinkActionResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2)))
_AcSS7LinkSetLinkActionResult_Type.__name__=_D
_AcSS7LinkSetLinkActionResult_Object=MibTableColumn
acSS7LinkSetLinkActionResult=_AcSS7LinkSetLinkActionResult_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,22,1,6),_AcSS7LinkSetLinkActionResult_Type())
acSS7LinkSetLinkActionResult.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7LinkSetLinkActionResult.setStatus(_A)
class _AcSS7LinkSetLinkLinkNo_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AcSS7LinkSetLinkLinkNo_Type.__name__=_B
_AcSS7LinkSetLinkLinkNo_Object=MibTableColumn
acSS7LinkSetLinkLinkNo=_AcSS7LinkSetLinkLinkNo_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,22,1,7),_AcSS7LinkSetLinkLinkNo_Type())
acSS7LinkSetLinkLinkNo.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkSetLinkLinkNo.setStatus(_A)
class _AcSS7LinkSetLinkLinkSlc_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_AcSS7LinkSetLinkLinkSlc_Type.__name__=_B
_AcSS7LinkSetLinkLinkSlc_Object=MibTableColumn
acSS7LinkSetLinkLinkSlc=_AcSS7LinkSetLinkLinkSlc_Object((1,3,6,1,4,1,5003,9,10,12,1,4,31,22,1,8),_AcSS7LinkSetLinkLinkSlc_Type())
acSS7LinkSetLinkLinkSlc.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7LinkSetLinkLinkSlc.setStatus(_A)
_AcSS7RouteSets_ObjectIdentity=ObjectIdentity
acSS7RouteSets=_AcSS7RouteSets_ObjectIdentity((1,3,6,1,4,1,5003,9,10,12,1,4,32))
_AcSS7RouteSetTable_Object=MibTable
acSS7RouteSetTable=_AcSS7RouteSetTable_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,21))
if mibBuilder.loadTexts:acSS7RouteSetTable.setStatus(_A)
_AcSS7RouteSetEntry_Object=MibTableRow
acSS7RouteSetEntry=_AcSS7RouteSetEntry_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,21,1))
acSS7RouteSetEntry.setIndexNames((0,_H,_t),(0,_H,_u))
if mibBuilder.loadTexts:acSS7RouteSetEntry.setStatus(_A)
class _AcSS7RouteSetSNIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AcSS7RouteSetSNIndex_Type.__name__=_B
_AcSS7RouteSetSNIndex_Object=MibTableColumn
acSS7RouteSetSNIndex=_AcSS7RouteSetSNIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,21,1,1),_AcSS7RouteSetSNIndex_Type())
acSS7RouteSetSNIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7RouteSetSNIndex.setStatus(_A)
class _AcSS7RouteSetIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,29))
_AcSS7RouteSetIndex_Type.__name__=_B
_AcSS7RouteSetIndex_Object=MibTableColumn
acSS7RouteSetIndex=_AcSS7RouteSetIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,21,1,2),_AcSS7RouteSetIndex_Type())
acSS7RouteSetIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7RouteSetIndex.setStatus(_A)
_AcSS7RouteSetRowStatus_Type=RowStatus
_AcSS7RouteSetRowStatus_Object=MibTableColumn
acSS7RouteSetRowStatus=_AcSS7RouteSetRowStatus_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,21,1,3),_AcSS7RouteSetRowStatus_Type())
acSS7RouteSetRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7RouteSetRowStatus.setStatus(_A)
class _AcSS7RouteSetAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_AcSS7RouteSetAction_Type.__name__=_D
_AcSS7RouteSetAction_Object=MibTableColumn
acSS7RouteSetAction=_AcSS7RouteSetAction_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,21,1,4),_AcSS7RouteSetAction_Type())
acSS7RouteSetAction.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7RouteSetAction.setStatus(_A)
class _AcSS7RouteSetActionResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2)))
_AcSS7RouteSetActionResult_Type.__name__=_D
_AcSS7RouteSetActionResult_Object=MibTableColumn
acSS7RouteSetActionResult=_AcSS7RouteSetActionResult_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,21,1,5),_AcSS7RouteSetActionResult_Type())
acSS7RouteSetActionResult.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7RouteSetActionResult.setStatus(_A)
class _AcSS7RouteSetName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AcSS7RouteSetName_Type.__name__=_M
_AcSS7RouteSetName_Object=MibTableColumn
acSS7RouteSetName=_AcSS7RouteSetName_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,21,1,6),_AcSS7RouteSetName_Type())
acSS7RouteSetName.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7RouteSetName.setStatus(_A)
class _AcSS7RouteSetAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*((_K,0),(_L,2)))
_AcSS7RouteSetAdminState_Type.__name__=_D
_AcSS7RouteSetAdminState_Object=MibTableColumn
acSS7RouteSetAdminState=_AcSS7RouteSetAdminState_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,21,1,7),_AcSS7RouteSetAdminState_Type())
acSS7RouteSetAdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7RouteSetAdminState.setStatus(_A)
class _AcSS7RouteSetOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),(_V,1),(_L,2)))
_AcSS7RouteSetOperState_Type.__name__=_D
_AcSS7RouteSetOperState_Object=MibTableColumn
acSS7RouteSetOperState=_AcSS7RouteSetOperState_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,21,1,8),_AcSS7RouteSetOperState_Type())
acSS7RouteSetOperState.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7RouteSetOperState.setStatus(_A)
class _AcSS7RouteSetDPC_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7RouteSetDPC_Type.__name__=_B
_AcSS7RouteSetDPC_Object=MibTableColumn
acSS7RouteSetDPC=_AcSS7RouteSetDPC_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,21,1,9),_AcSS7RouteSetDPC_Type())
acSS7RouteSetDPC.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7RouteSetDPC.setStatus(_A)
class _AcSS7RouteSetRouteMask_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcSS7RouteSetRouteMask_Type.__name__=_B
_AcSS7RouteSetRouteMask_Object=MibTableColumn
acSS7RouteSetRouteMask=_AcSS7RouteSetRouteMask_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,21,1,10),_AcSS7RouteSetRouteMask_Type())
acSS7RouteSetRouteMask.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7RouteSetRouteMask.setStatus(_A)
_AcSS7RouteSetRouteTable_Object=MibTable
acSS7RouteSetRouteTable=_AcSS7RouteSetRouteTable_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,22))
if mibBuilder.loadTexts:acSS7RouteSetRouteTable.setStatus(_A)
_AcSS7RouteSetRouteEntry_Object=MibTableRow
acSS7RouteSetRouteEntry=_AcSS7RouteSetRouteEntry_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,22,1))
acSS7RouteSetRouteEntry.setIndexNames((0,_H,_v),(0,_H,_w),(0,_H,_x))
if mibBuilder.loadTexts:acSS7RouteSetRouteEntry.setStatus(_A)
class _AcSS7RouteSetRouteSNIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AcSS7RouteSetRouteSNIndex_Type.__name__=_B
_AcSS7RouteSetRouteSNIndex_Object=MibTableColumn
acSS7RouteSetRouteSNIndex=_AcSS7RouteSetRouteSNIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,22,1,1),_AcSS7RouteSetRouteSNIndex_Type())
acSS7RouteSetRouteSNIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7RouteSetRouteSNIndex.setStatus(_A)
class _AcSS7RouteSetRouteRoutesetIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,29))
_AcSS7RouteSetRouteRoutesetIndex_Type.__name__=_B
_AcSS7RouteSetRouteRoutesetIndex_Object=MibTableColumn
acSS7RouteSetRouteRoutesetIndex=_AcSS7RouteSetRouteRoutesetIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,22,1,2),_AcSS7RouteSetRouteRoutesetIndex_Type())
acSS7RouteSetRouteRoutesetIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7RouteSetRouteRoutesetIndex.setStatus(_A)
class _AcSS7RouteSetRouteInnerRouteIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AcSS7RouteSetRouteInnerRouteIndex_Type.__name__=_B
_AcSS7RouteSetRouteInnerRouteIndex_Object=MibTableColumn
acSS7RouteSetRouteInnerRouteIndex=_AcSS7RouteSetRouteInnerRouteIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,22,1,3),_AcSS7RouteSetRouteInnerRouteIndex_Type())
acSS7RouteSetRouteInnerRouteIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7RouteSetRouteInnerRouteIndex.setStatus(_A)
_AcSS7RouteSetRouteRowStatus_Type=RowStatus
_AcSS7RouteSetRouteRowStatus_Object=MibTableColumn
acSS7RouteSetRouteRowStatus=_AcSS7RouteSetRouteRowStatus_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,22,1,4),_AcSS7RouteSetRouteRowStatus_Type())
acSS7RouteSetRouteRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7RouteSetRouteRowStatus.setStatus(_A)
class _AcSS7RouteSetRouteAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues((_J,0))
_AcSS7RouteSetRouteAction_Type.__name__=_D
_AcSS7RouteSetRouteAction_Object=MibTableColumn
acSS7RouteSetRouteAction=_AcSS7RouteSetRouteAction_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,22,1,5),_AcSS7RouteSetRouteAction_Type())
acSS7RouteSetRouteAction.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7RouteSetRouteAction.setStatus(_A)
class _AcSS7RouteSetRouteActionResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2)))
_AcSS7RouteSetRouteActionResult_Type.__name__=_D
_AcSS7RouteSetRouteActionResult_Object=MibTableColumn
acSS7RouteSetRouteActionResult=_AcSS7RouteSetRouteActionResult_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,22,1,6),_AcSS7RouteSetRouteActionResult_Type())
acSS7RouteSetRouteActionResult.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7RouteSetRouteActionResult.setStatus(_A)
class _AcSS7RouteSetRouteLinkSetNo_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AcSS7RouteSetRouteLinkSetNo_Type.__name__=_B
_AcSS7RouteSetRouteLinkSetNo_Object=MibTableColumn
acSS7RouteSetRouteLinkSetNo=_AcSS7RouteSetRouteLinkSetNo_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,22,1,7),_AcSS7RouteSetRouteLinkSetNo_Type())
acSS7RouteSetRouteLinkSetNo.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7RouteSetRouteLinkSetNo.setStatus(_A)
class _AcSS7RouteSetRoutePriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_AcSS7RouteSetRoutePriority_Type.__name__=_B
_AcSS7RouteSetRoutePriority_Object=MibTableColumn
acSS7RouteSetRoutePriority=_AcSS7RouteSetRoutePriority_Object((1,3,6,1,4,1,5003,9,10,12,1,4,32,22,1,8),_AcSS7RouteSetRoutePriority_Type())
acSS7RouteSetRoutePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7RouteSetRoutePriority.setStatus(_A)
_AcSS7AliasPointCode_ObjectIdentity=ObjectIdentity
acSS7AliasPointCode=_AcSS7AliasPointCode_ObjectIdentity((1,3,6,1,4,1,5003,9,10,12,1,4,33))
_AcSS7APCTable_Object=MibTable
acSS7APCTable=_AcSS7APCTable_Object((1,3,6,1,4,1,5003,9,10,12,1,4,33,21))
if mibBuilder.loadTexts:acSS7APCTable.setStatus(_A)
_AcSS7APCEntry_Object=MibTableRow
acSS7APCEntry=_AcSS7APCEntry_Object((1,3,6,1,4,1,5003,9,10,12,1,4,33,21,1))
acSS7APCEntry.setIndexNames((0,_H,_y),(0,_H,_z))
if mibBuilder.loadTexts:acSS7APCEntry.setStatus(_A)
class _AcSS7APCSNIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AcSS7APCSNIndex_Type.__name__=_B
_AcSS7APCSNIndex_Object=MibTableColumn
acSS7APCSNIndex=_AcSS7APCSNIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,4,33,21,1,1),_AcSS7APCSNIndex_Type())
acSS7APCSNIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7APCSNIndex.setStatus(_A)
class _AcSS7APCIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_AcSS7APCIndex_Type.__name__=_B
_AcSS7APCIndex_Object=MibTableColumn
acSS7APCIndex=_AcSS7APCIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,4,33,21,1,2),_AcSS7APCIndex_Type())
acSS7APCIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7APCIndex.setStatus(_A)
_AcSS7APCRowStatus_Type=RowStatus
_AcSS7APCRowStatus_Object=MibTableColumn
acSS7APCRowStatus=_AcSS7APCRowStatus_Object((1,3,6,1,4,1,5003,9,10,12,1,4,33,21,1,3),_AcSS7APCRowStatus_Type())
acSS7APCRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7APCRowStatus.setStatus(_A)
class _AcSS7APCAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2),(_S,3),(_T,4)))
_AcSS7APCAction_Type.__name__=_D
_AcSS7APCAction_Object=MibTableColumn
acSS7APCAction=_AcSS7APCAction_Object((1,3,6,1,4,1,5003,9,10,12,1,4,33,21,1,4),_AcSS7APCAction_Type())
acSS7APCAction.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7APCAction.setStatus(_A)
class _AcSS7APCActionResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_O,1),(_P,2)))
_AcSS7APCActionResult_Type.__name__=_D
_AcSS7APCActionResult_Object=MibTableColumn
acSS7APCActionResult=_AcSS7APCActionResult_Object((1,3,6,1,4,1,5003,9,10,12,1,4,33,21,1,5),_AcSS7APCActionResult_Type())
acSS7APCActionResult.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7APCActionResult.setStatus(_A)
class _AcSS7APCPC_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7APCPC_Type.__name__=_B
_AcSS7APCPC_Object=MibTableColumn
acSS7APCPC=_AcSS7APCPC_Object((1,3,6,1,4,1,5003,9,10,12,1,4,33,21,1,6),_AcSS7APCPC_Type())
acSS7APCPC.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7APCPC.setStatus(_A)
class _AcSS7APCSNI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,5))
_AcSS7APCSNI_Type.__name__=_B
_AcSS7APCSNI_Object=MibTableColumn
acSS7APCSNI=_AcSS7APCSNI_Object((1,3,6,1,4,1,5003,9,10,12,1,4,33,21,1,7),_AcSS7APCSNI_Type())
acSS7APCSNI.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7APCSNI.setStatus(_A)
class _AcSS7APCName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AcSS7APCName_Type.__name__=_M
_AcSS7APCName_Object=MibTableColumn
acSS7APCName=_AcSS7APCName_Object((1,3,6,1,4,1,5003,9,10,12,1,4,33,21,1,8),_AcSS7APCName_Type())
acSS7APCName.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7APCName.setStatus(_A)
class _AcSS7APCMtcBusy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_R,1)))
_AcSS7APCMtcBusy_Type.__name__=_D
_AcSS7APCMtcBusy_Object=MibTableColumn
acSS7APCMtcBusy=_AcSS7APCMtcBusy_Object((1,3,6,1,4,1,5003,9,10,12,1,4,33,21,1,9),_AcSS7APCMtcBusy_Type())
acSS7APCMtcBusy.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7APCMtcBusy.setStatus(_A)
class _AcSS7APCAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),(_V,1),(_L,2)))
_AcSS7APCAdminState_Type.__name__=_D
_AcSS7APCAdminState_Object=MibTableColumn
acSS7APCAdminState=_AcSS7APCAdminState_Object((1,3,6,1,4,1,5003,9,10,12,1,4,33,21,1,10),_AcSS7APCAdminState_Type())
acSS7APCAdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7APCAdminState.setStatus(_A)
class _AcSS7APCOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),(_V,1),(_L,2)))
_AcSS7APCOperState_Type.__name__=_D
_AcSS7APCOperState_Object=MibTableColumn
acSS7APCOperState=_AcSS7APCOperState_Object((1,3,6,1,4,1,5003,9,10,12,1,4,33,21,1,11),_AcSS7APCOperState_Type())
acSS7APCOperState.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7APCOperState.setStatus(_A)
_AcSS7SigTran_ObjectIdentity=ObjectIdentity
acSS7SigTran=_AcSS7SigTran_ObjectIdentity((1,3,6,1,4,1,5003,9,10,12,1,5))
class _AcSS7SigTranM3UATrafficBehavior_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('deactivate',1),('sIPO',2)))
_AcSS7SigTranM3UATrafficBehavior_Type.__name__=_D
_AcSS7SigTranM3UATrafficBehavior_Object=MibScalar
acSS7SigTranM3UATrafficBehavior=_AcSS7SigTranM3UATrafficBehavior_Object((1,3,6,1,4,1,5003,9,10,12,1,5,1),_AcSS7SigTranM3UATrafficBehavior_Type())
acSS7SigTranM3UATrafficBehavior.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7SigTranM3UATrafficBehavior.setStatus(_A)
_AcSS7SigTranIFGroupTable_Object=MibTable
acSS7SigTranIFGroupTable=_AcSS7SigTranIFGroupTable_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21))
if mibBuilder.loadTexts:acSS7SigTranIFGroupTable.setStatus(_A)
_AcSS7SigTranIFGroupEntry_Object=MibTableRow
acSS7SigTranIFGroupEntry=_AcSS7SigTranIFGroupEntry_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1))
acSS7SigTranIFGroupEntry.setIndexNames((0,_H,_A0))
if mibBuilder.loadTexts:acSS7SigTranIFGroupEntry.setStatus(_A)
class _AcSS7SigTranIFGroupIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_AcSS7SigTranIFGroupIndex_Type.__name__=_B
_AcSS7SigTranIFGroupIndex_Object=MibTableColumn
acSS7SigTranIFGroupIndex=_AcSS7SigTranIFGroupIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,1),_AcSS7SigTranIFGroupIndex_Type())
acSS7SigTranIFGroupIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7SigTranIFGroupIndex.setStatus(_A)
_AcSS7SigTranIFGroupRowStatus_Type=RowStatus
_AcSS7SigTranIFGroupRowStatus_Object=MibTableColumn
acSS7SigTranIFGroupRowStatus=_AcSS7SigTranIFGroupRowStatus_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,2),_AcSS7SigTranIFGroupRowStatus_Type())
acSS7SigTranIFGroupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupRowStatus.setStatus(_A)
class _AcSS7SigTranIFGroupAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_S,1),(_T,2)))
_AcSS7SigTranIFGroupAction_Type.__name__=_D
_AcSS7SigTranIFGroupAction_Object=MibTableColumn
acSS7SigTranIFGroupAction=_AcSS7SigTranIFGroupAction_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,3),_AcSS7SigTranIFGroupAction_Type())
acSS7SigTranIFGroupAction.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupAction.setStatus(_A)
class _AcSS7SigTranIFGroupActionResult_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7SigTranIFGroupActionResult_Type.__name__=_B
_AcSS7SigTranIFGroupActionResult_Object=MibTableColumn
acSS7SigTranIFGroupActionResult=_AcSS7SigTranIFGroupActionResult_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,4),_AcSS7SigTranIFGroupActionResult_Type())
acSS7SigTranIFGroupActionResult.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7SigTranIFGroupActionResult.setStatus(_A)
class _AcSS7SigTranIFGroupId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_AcSS7SigTranIFGroupId_Type.__name__=_B
_AcSS7SigTranIFGroupId_Object=MibTableColumn
acSS7SigTranIFGroupId=_AcSS7SigTranIFGroupId_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,5),_AcSS7SigTranIFGroupId_Type())
acSS7SigTranIFGroupId.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupId.setStatus(_A)
class _AcSS7SigTranIFGroupSgMgc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,77,83)));namedValues=NamedValues(*(('nat',1),('mgc',77),('sg',83)))
_AcSS7SigTranIFGroupSgMgc_Type.__name__=_D
_AcSS7SigTranIFGroupSgMgc_Object=MibTableColumn
acSS7SigTranIFGroupSgMgc=_AcSS7SigTranIFGroupSgMgc_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,6),_AcSS7SigTranIFGroupSgMgc_Type())
acSS7SigTranIFGroupSgMgc.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupSgMgc.setStatus(_A)
class _AcSS7SigTranIFGroupSignalingLayer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,6)));namedValues=NamedValues(*(('noLayer',0),('iua',1),('m2ua',2),('m3ua',3),('m2tunnel',4),('dua',6)))
_AcSS7SigTranIFGroupSignalingLayer_Type.__name__=_D
_AcSS7SigTranIFGroupSignalingLayer_Object=MibTableColumn
acSS7SigTranIFGroupSignalingLayer=_AcSS7SigTranIFGroupSignalingLayer_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,7),_AcSS7SigTranIFGroupSignalingLayer_Type())
acSS7SigTranIFGroupSignalingLayer.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupSignalingLayer.setStatus(_A)
class _AcSS7SigTranIFGroupTrafMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('override',1),('loadShare',2),('broadcast',3)))
_AcSS7SigTranIFGroupTrafMode_Type.__name__=_D
_AcSS7SigTranIFGroupTrafMode_Object=MibTableColumn
acSS7SigTranIFGroupTrafMode=_AcSS7SigTranIFGroupTrafMode_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,8),_AcSS7SigTranIFGroupTrafMode_Type())
acSS7SigTranIFGroupTrafMode.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupTrafMode.setStatus(_A)
class _AcSS7SigTranIFGroupRecovTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_AcSS7SigTranIFGroupRecovTimer_Type.__name__=_B
_AcSS7SigTranIFGroupRecovTimer_Object=MibTableColumn
acSS7SigTranIFGroupRecovTimer=_AcSS7SigTranIFGroupRecovTimer_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,9),_AcSS7SigTranIFGroupRecovTimer_Type())
acSS7SigTranIFGroupRecovTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupRecovTimer.setStatus(_A)
class _AcSS7SigTranIFGroupAckTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_AcSS7SigTranIFGroupAckTimer_Type.__name__=_B
_AcSS7SigTranIFGroupAckTimer_Object=MibTableColumn
acSS7SigTranIFGroupAckTimer=_AcSS7SigTranIFGroupAckTimer_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,10),_AcSS7SigTranIFGroupAckTimer_Type())
acSS7SigTranIFGroupAckTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupAckTimer.setStatus(_A)
class _AcSS7SigTranIFGroupHBTimer_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_AcSS7SigTranIFGroupHBTimer_Type.__name__=_B
_AcSS7SigTranIFGroupHBTimer_Object=MibTableColumn
acSS7SigTranIFGroupHBTimer=_AcSS7SigTranIFGroupHBTimer_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,11),_AcSS7SigTranIFGroupHBTimer_Type())
acSS7SigTranIFGroupHBTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupHBTimer.setStatus(_A)
class _AcSS7SigTranIFGroupMinAsp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_AcSS7SigTranIFGroupMinAsp_Type.__name__=_B
_AcSS7SigTranIFGroupMinAsp_Object=MibTableColumn
acSS7SigTranIFGroupMinAsp=_AcSS7SigTranIFGroupMinAsp_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,12),_AcSS7SigTranIFGroupMinAsp_Type())
acSS7SigTranIFGroupMinAsp.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupMinAsp.setStatus(_A)
class _AcSS7SigTranIFGroupBehavior_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7SigTranIFGroupBehavior_Type.__name__=_B
_AcSS7SigTranIFGroupBehavior_Object=MibTableColumn
acSS7SigTranIFGroupBehavior=_AcSS7SigTranIFGroupBehavior_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,13),_AcSS7SigTranIFGroupBehavior_Type())
acSS7SigTranIFGroupBehavior.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupBehavior.setStatus(_A)
class _AcSS7SigTranIFGroupSCTPInst_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_AcSS7SigTranIFGroupSCTPInst_Type.__name__=_B
_AcSS7SigTranIFGroupSCTPInst_Object=MibTableColumn
acSS7SigTranIFGroupSCTPInst=_AcSS7SigTranIFGroupSCTPInst_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,14),_AcSS7SigTranIFGroupSCTPInst_Type())
acSS7SigTranIFGroupSCTPInst.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7SigTranIFGroupSCTPInst.setStatus(_A)
class _AcSS7SigTranIFGroupSCTPLocalPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7SigTranIFGroupSCTPLocalPort_Type.__name__=_B
_AcSS7SigTranIFGroupSCTPLocalPort_Object=MibTableColumn
acSS7SigTranIFGroupSCTPLocalPort=_AcSS7SigTranIFGroupSCTPLocalPort_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,15),_AcSS7SigTranIFGroupSCTPLocalPort_Type())
acSS7SigTranIFGroupSCTPLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupSCTPLocalPort.setStatus(_A)
class _AcSS7SigTranIFGroupNetwork_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Z,1),(_a,2),(_b,3)))
_AcSS7SigTranIFGroupNetwork_Type.__name__=_D
_AcSS7SigTranIFGroupNetwork_Object=MibTableColumn
acSS7SigTranIFGroupNetwork=_AcSS7SigTranIFGroupNetwork_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,16),_AcSS7SigTranIFGroupNetwork_Type())
acSS7SigTranIFGroupNetwork.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupNetwork.setStatus(_A)
class _AcSS7SigTranIFGroupSCTPDestPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_AcSS7SigTranIFGroupSCTPDestPort_Type.__name__=_B
_AcSS7SigTranIFGroupSCTPDestPort_Object=MibTableColumn
acSS7SigTranIFGroupSCTPDestPort=_AcSS7SigTranIFGroupSCTPDestPort_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,17),_AcSS7SigTranIFGroupSCTPDestPort_Type())
acSS7SigTranIFGroupSCTPDestPort.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupSCTPDestPort.setStatus(_A)
_AcSS7SigTranIFGroupDestIp_Type=IpAddress
_AcSS7SigTranIFGroupDestIp_Object=MibTableColumn
acSS7SigTranIFGroupDestIp=_AcSS7SigTranIFGroupDestIp_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,18),_AcSS7SigTranIFGroupDestIp_Type())
acSS7SigTranIFGroupDestIp.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupDestIp.setStatus(_A)
class _AcSS7SigTranIFGroupSCTPMaxInbStreams_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,65534))
_AcSS7SigTranIFGroupSCTPMaxInbStreams_Type.__name__=_B
_AcSS7SigTranIFGroupSCTPMaxInbStreams_Object=MibTableColumn
acSS7SigTranIFGroupSCTPMaxInbStreams=_AcSS7SigTranIFGroupSCTPMaxInbStreams_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,19),_AcSS7SigTranIFGroupSCTPMaxInbStreams_Type())
acSS7SigTranIFGroupSCTPMaxInbStreams.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupSCTPMaxInbStreams.setStatus(_A)
class _AcSS7SigTranIFGroupSCTPMaxOutbStreams_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,65534))
_AcSS7SigTranIFGroupSCTPMaxOutbStreams_Type.__name__=_B
_AcSS7SigTranIFGroupSCTPMaxOutbStreams_Object=MibTableColumn
acSS7SigTranIFGroupSCTPMaxOutbStreams=_AcSS7SigTranIFGroupSCTPMaxOutbStreams_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,20),_AcSS7SigTranIFGroupSCTPMaxOutbStreams_Type())
acSS7SigTranIFGroupSCTPMaxOutbStreams.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupSCTPMaxOutbStreams.setStatus(_A)
class _AcSS7SigTranIFGroupRdcyBoardNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AcSS7SigTranIFGroupRdcyBoardNum_Type.__name__=_B
_AcSS7SigTranIFGroupRdcyBoardNum_Object=MibTableColumn
acSS7SigTranIFGroupRdcyBoardNum=_AcSS7SigTranIFGroupRdcyBoardNum_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,21),_AcSS7SigTranIFGroupRdcyBoardNum_Type())
acSS7SigTranIFGroupRdcyBoardNum.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupRdcyBoardNum.setStatus(_A)
class _AcSS7SigTranIFGroupRoutingContextIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,15))
_AcSS7SigTranIFGroupRoutingContextIndex_Type.__name__=_D
_AcSS7SigTranIFGroupRoutingContextIndex_Object=MibTableColumn
acSS7SigTranIFGroupRoutingContextIndex=_AcSS7SigTranIFGroupRoutingContextIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,22),_AcSS7SigTranIFGroupRoutingContextIndex_Type())
acSS7SigTranIFGroupRoutingContextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupRoutingContextIndex.setStatus(_A)
class _AcSS7SigTranIFGroupRoutingContextValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcSS7SigTranIFGroupRoutingContextValue_Type.__name__=_D
_AcSS7SigTranIFGroupRoutingContextValue_Object=MibTableColumn
acSS7SigTranIFGroupRoutingContextValue=_AcSS7SigTranIFGroupRoutingContextValue_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,23),_AcSS7SigTranIFGroupRoutingContextValue_Type())
acSS7SigTranIFGroupRoutingContextValue.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupRoutingContextValue.setStatus(_A)
class _AcSS7SigTranIFGroupNetworkAppearance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AcSS7SigTranIFGroupNetworkAppearance_Type.__name__=_D
_AcSS7SigTranIFGroupNetworkAppearance_Object=MibTableColumn
acSS7SigTranIFGroupNetworkAppearance=_AcSS7SigTranIFGroupNetworkAppearance_Object((1,3,6,1,4,1,5003,9,10,12,1,5,21,1,24),_AcSS7SigTranIFGroupNetworkAppearance_Type())
acSS7SigTranIFGroupNetworkAppearance.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFGroupNetworkAppearance.setStatus(_A)
_AcSS7SigTranIFIDTable_Object=MibTable
acSS7SigTranIFIDTable=_AcSS7SigTranIFIDTable_Object((1,3,6,1,4,1,5003,9,10,12,1,5,22))
if mibBuilder.loadTexts:acSS7SigTranIFIDTable.setStatus(_A)
_AcSS7SigTranIFIDEntry_Object=MibTableRow
acSS7SigTranIFIDEntry=_AcSS7SigTranIFIDEntry_Object((1,3,6,1,4,1,5003,9,10,12,1,5,22,1))
acSS7SigTranIFIDEntry.setIndexNames((0,_H,_A1))
if mibBuilder.loadTexts:acSS7SigTranIFIDEntry.setStatus(_A)
class _AcSS7SigTranIFIDIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,83))
_AcSS7SigTranIFIDIndex_Type.__name__=_B
_AcSS7SigTranIFIDIndex_Object=MibTableColumn
acSS7SigTranIFIDIndex=_AcSS7SigTranIFIDIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,5,22,1,1),_AcSS7SigTranIFIDIndex_Type())
acSS7SigTranIFIDIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7SigTranIFIDIndex.setStatus(_A)
_AcSS7SigTranIFIDRowStatus_Type=RowStatus
_AcSS7SigTranIFIDRowStatus_Object=MibTableColumn
acSS7SigTranIFIDRowStatus=_AcSS7SigTranIFIDRowStatus_Object((1,3,6,1,4,1,5003,9,10,12,1,5,22,1,2),_AcSS7SigTranIFIDRowStatus_Type())
acSS7SigTranIFIDRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFIDRowStatus.setStatus(_A)
class _AcSS7SigTranIFIDAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_S,1),(_T,2)))
_AcSS7SigTranIFIDAction_Type.__name__=_D
_AcSS7SigTranIFIDAction_Object=MibTableColumn
acSS7SigTranIFIDAction=_AcSS7SigTranIFIDAction_Object((1,3,6,1,4,1,5003,9,10,12,1,5,22,1,3),_AcSS7SigTranIFIDAction_Type())
acSS7SigTranIFIDAction.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFIDAction.setStatus(_A)
class _AcSS7SigTranIFIDActionResult_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7SigTranIFIDActionResult_Type.__name__=_B
_AcSS7SigTranIFIDActionResult_Object=MibTableColumn
acSS7SigTranIFIDActionResult=_AcSS7SigTranIFIDActionResult_Object((1,3,6,1,4,1,5003,9,10,12,1,5,22,1,4),_AcSS7SigTranIFIDActionResult_Type())
acSS7SigTranIFIDActionResult.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7SigTranIFIDActionResult.setStatus(_A)
class _AcSS7SigTranIFIDValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7SigTranIFIDValue_Type.__name__=_B
_AcSS7SigTranIFIDValue_Object=MibTableColumn
acSS7SigTranIFIDValue=_AcSS7SigTranIFIDValue_Object((1,3,6,1,4,1,5003,9,10,12,1,5,22,1,5),_AcSS7SigTranIFIDValue_Type())
acSS7SigTranIFIDValue.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFIDValue.setStatus(_A)
class _AcSS7SigTranIFIDName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_AcSS7SigTranIFIDName_Type.__name__=_M
_AcSS7SigTranIFIDName_Object=MibTableColumn
acSS7SigTranIFIDName=_AcSS7SigTranIFIDName_Object((1,3,6,1,4,1,5003,9,10,12,1,5,22,1,6),_AcSS7SigTranIFIDName_Type())
acSS7SigTranIFIDName.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFIDName.setStatus(_A)
class _AcSS7SigTranIFIDOwnerGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,65534))
_AcSS7SigTranIFIDOwnerGroup_Type.__name__=_D
_AcSS7SigTranIFIDOwnerGroup_Object=MibTableColumn
acSS7SigTranIFIDOwnerGroup=_AcSS7SigTranIFIDOwnerGroup_Object((1,3,6,1,4,1,5003,9,10,12,1,5,22,1,7),_AcSS7SigTranIFIDOwnerGroup_Type())
acSS7SigTranIFIDOwnerGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFIDOwnerGroup.setStatus(_A)
class _AcSS7SigTranIFIDSignalingLayer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,6)));namedValues=NamedValues(*(('noLayer',0),('iua',1),('m2ua',2),('m2tunnel',4),('dua',6)))
_AcSS7SigTranIFIDSignalingLayer_Type.__name__=_D
_AcSS7SigTranIFIDSignalingLayer_Object=MibTableColumn
acSS7SigTranIFIDSignalingLayer=_AcSS7SigTranIFIDSignalingLayer_Object((1,3,6,1,4,1,5003,9,10,12,1,5,22,1,8),_AcSS7SigTranIFIDSignalingLayer_Type())
acSS7SigTranIFIDSignalingLayer.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFIDSignalingLayer.setStatus(_A)
class _AcSS7SigTranIFIDNai_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,124))
_AcSS7SigTranIFIDNai_Type.__name__=_D
_AcSS7SigTranIFIDNai_Object=MibTableColumn
acSS7SigTranIFIDNai=_AcSS7SigTranIFIDNai_Object((1,3,6,1,4,1,5003,9,10,12,1,5,22,1,9),_AcSS7SigTranIFIDNai_Type())
acSS7SigTranIFIDNai.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFIDNai.setStatus(_A)
class _AcSS7SigTranIFIDM3UASpc_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7SigTranIFIDM3UASpc_Type.__name__=_B
_AcSS7SigTranIFIDM3UASpc_Object=MibTableColumn
acSS7SigTranIFIDM3UASpc=_AcSS7SigTranIFIDM3UASpc_Object((1,3,6,1,4,1,5003,9,10,12,1,5,22,1,10),_AcSS7SigTranIFIDM3UASpc_Type())
acSS7SigTranIFIDM3UASpc.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranIFIDM3UASpc.setStatus(_A)
_AcSS7M3UAStaticRoutingTable_Object=MibTable
acSS7M3UAStaticRoutingTable=_AcSS7M3UAStaticRoutingTable_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23))
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingTable.setStatus(_G)
_AcSS7M3UAStaticRoutingEntry_Object=MibTableRow
acSS7M3UAStaticRoutingEntry=_AcSS7M3UAStaticRoutingEntry_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1))
acSS7M3UAStaticRoutingEntry.setIndexNames((0,_H,_A2))
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingEntry.setStatus(_G)
class _AcSS7M3UAStaticRoutingIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AcSS7M3UAStaticRoutingIndex_Type.__name__=_B
_AcSS7M3UAStaticRoutingIndex_Object=MibTableColumn
acSS7M3UAStaticRoutingIndex=_AcSS7M3UAStaticRoutingIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,1),_AcSS7M3UAStaticRoutingIndex_Type())
acSS7M3UAStaticRoutingIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingIndex.setStatus(_G)
_AcSS7M3UAStaticRoutingRowStatus_Type=RowStatus
_AcSS7M3UAStaticRoutingRowStatus_Object=MibTableColumn
acSS7M3UAStaticRoutingRowStatus=_AcSS7M3UAStaticRoutingRowStatus_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,2),_AcSS7M3UAStaticRoutingRowStatus_Type())
acSS7M3UAStaticRoutingRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingRowStatus.setStatus(_G)
class _AcSS7M3UAStaticRoutingAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_S,1),(_T,2)))
_AcSS7M3UAStaticRoutingAction_Type.__name__=_D
_AcSS7M3UAStaticRoutingAction_Object=MibTableColumn
acSS7M3UAStaticRoutingAction=_AcSS7M3UAStaticRoutingAction_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,3),_AcSS7M3UAStaticRoutingAction_Type())
acSS7M3UAStaticRoutingAction.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingAction.setStatus(_G)
class _AcSS7M3UAStaticRoutingActionResult_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7M3UAStaticRoutingActionResult_Type.__name__=_B
_AcSS7M3UAStaticRoutingActionResult_Object=MibTableColumn
acSS7M3UAStaticRoutingActionResult=_AcSS7M3UAStaticRoutingActionResult_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,4),_AcSS7M3UAStaticRoutingActionResult_Type())
acSS7M3UAStaticRoutingActionResult.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingActionResult.setStatus(_G)
class _AcSS7M3UAStaticRoutingOwnerInterfaceGroup_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_AcSS7M3UAStaticRoutingOwnerInterfaceGroup_Type.__name__=_B
_AcSS7M3UAStaticRoutingOwnerInterfaceGroup_Object=MibTableColumn
acSS7M3UAStaticRoutingOwnerInterfaceGroup=_AcSS7M3UAStaticRoutingOwnerInterfaceGroup_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,5),_AcSS7M3UAStaticRoutingOwnerInterfaceGroup_Type())
acSS7M3UAStaticRoutingOwnerInterfaceGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingOwnerInterfaceGroup.setStatus(_G)
class _AcSS7M3UAStaticRoutingRC_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_AcSS7M3UAStaticRoutingRC_Type.__name__=_B
_AcSS7M3UAStaticRoutingRC_Object=MibTableColumn
acSS7M3UAStaticRoutingRC=_AcSS7M3UAStaticRoutingRC_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,6),_AcSS7M3UAStaticRoutingRC_Type())
acSS7M3UAStaticRoutingRC.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingRC.setStatus(_G)
class _AcSS7M3UAStaticRoutingDestinationPointCode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_AcSS7M3UAStaticRoutingDestinationPointCode_Type.__name__=_B
_AcSS7M3UAStaticRoutingDestinationPointCode_Object=MibTableColumn
acSS7M3UAStaticRoutingDestinationPointCode=_AcSS7M3UAStaticRoutingDestinationPointCode_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,7),_AcSS7M3UAStaticRoutingDestinationPointCode_Type())
acSS7M3UAStaticRoutingDestinationPointCode.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingDestinationPointCode.setStatus(_G)
class _AcSS7M3UAStaticRoutingNetworkAppearence_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_AcSS7M3UAStaticRoutingNetworkAppearence_Type.__name__=_B
_AcSS7M3UAStaticRoutingNetworkAppearence_Object=MibTableColumn
acSS7M3UAStaticRoutingNetworkAppearence=_AcSS7M3UAStaticRoutingNetworkAppearence_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,8),_AcSS7M3UAStaticRoutingNetworkAppearence_Type())
acSS7M3UAStaticRoutingNetworkAppearence.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingNetworkAppearence.setStatus(_G)
class _AcSS7M3UAStaticRoutingSeriviceIndicatorList_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AcSS7M3UAStaticRoutingSeriviceIndicatorList_Type.__name__=_B
_AcSS7M3UAStaticRoutingSeriviceIndicatorList_Object=MibTableColumn
acSS7M3UAStaticRoutingSeriviceIndicatorList=_AcSS7M3UAStaticRoutingSeriviceIndicatorList_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,9),_AcSS7M3UAStaticRoutingSeriviceIndicatorList_Type())
acSS7M3UAStaticRoutingSeriviceIndicatorList.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingSeriviceIndicatorList.setStatus(_G)
class _AcSS7M3UAStaticRoutingOPC1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_AcSS7M3UAStaticRoutingOPC1_Type.__name__=_B
_AcSS7M3UAStaticRoutingOPC1_Object=MibTableColumn
acSS7M3UAStaticRoutingOPC1=_AcSS7M3UAStaticRoutingOPC1_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,10),_AcSS7M3UAStaticRoutingOPC1_Type())
acSS7M3UAStaticRoutingOPC1.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingOPC1.setStatus(_G)
class _AcSS7M3UAStaticRoutingOPC2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_AcSS7M3UAStaticRoutingOPC2_Type.__name__=_B
_AcSS7M3UAStaticRoutingOPC2_Object=MibTableColumn
acSS7M3UAStaticRoutingOPC2=_AcSS7M3UAStaticRoutingOPC2_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,11),_AcSS7M3UAStaticRoutingOPC2_Type())
acSS7M3UAStaticRoutingOPC2.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingOPC2.setStatus(_G)
class _AcSS7M3UAStaticRoutingOPC3_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_AcSS7M3UAStaticRoutingOPC3_Type.__name__=_B
_AcSS7M3UAStaticRoutingOPC3_Object=MibTableColumn
acSS7M3UAStaticRoutingOPC3=_AcSS7M3UAStaticRoutingOPC3_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,12),_AcSS7M3UAStaticRoutingOPC3_Type())
acSS7M3UAStaticRoutingOPC3.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingOPC3.setStatus(_G)
class _AcSS7M3UAStaticRoutingOPC4_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_AcSS7M3UAStaticRoutingOPC4_Type.__name__=_B
_AcSS7M3UAStaticRoutingOPC4_Object=MibTableColumn
acSS7M3UAStaticRoutingOPC4=_AcSS7M3UAStaticRoutingOPC4_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,13),_AcSS7M3UAStaticRoutingOPC4_Type())
acSS7M3UAStaticRoutingOPC4.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingOPC4.setStatus(_G)
class _AcSS7M3UAStaticRoutingLowerCICValue1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AcSS7M3UAStaticRoutingLowerCICValue1_Type.__name__=_B
_AcSS7M3UAStaticRoutingLowerCICValue1_Object=MibTableColumn
acSS7M3UAStaticRoutingLowerCICValue1=_AcSS7M3UAStaticRoutingLowerCICValue1_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,14),_AcSS7M3UAStaticRoutingLowerCICValue1_Type())
acSS7M3UAStaticRoutingLowerCICValue1.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingLowerCICValue1.setStatus(_G)
class _AcSS7M3UAStaticRoutingUpperCICValue1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AcSS7M3UAStaticRoutingUpperCICValue1_Type.__name__=_B
_AcSS7M3UAStaticRoutingUpperCICValue1_Object=MibTableColumn
acSS7M3UAStaticRoutingUpperCICValue1=_AcSS7M3UAStaticRoutingUpperCICValue1_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,15),_AcSS7M3UAStaticRoutingUpperCICValue1_Type())
acSS7M3UAStaticRoutingUpperCICValue1.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingUpperCICValue1.setStatus(_G)
class _AcSS7M3UAStaticRoutingLowerCICValue2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AcSS7M3UAStaticRoutingLowerCICValue2_Type.__name__=_B
_AcSS7M3UAStaticRoutingLowerCICValue2_Object=MibTableColumn
acSS7M3UAStaticRoutingLowerCICValue2=_AcSS7M3UAStaticRoutingLowerCICValue2_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,16),_AcSS7M3UAStaticRoutingLowerCICValue2_Type())
acSS7M3UAStaticRoutingLowerCICValue2.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingLowerCICValue2.setStatus(_G)
class _AcSS7M3UAStaticRoutingUpperCICValue2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AcSS7M3UAStaticRoutingUpperCICValue2_Type.__name__=_B
_AcSS7M3UAStaticRoutingUpperCICValue2_Object=MibTableColumn
acSS7M3UAStaticRoutingUpperCICValue2=_AcSS7M3UAStaticRoutingUpperCICValue2_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,17),_AcSS7M3UAStaticRoutingUpperCICValue2_Type())
acSS7M3UAStaticRoutingUpperCICValue2.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingUpperCICValue2.setStatus(_G)
class _AcSS7M3UAStaticRoutingLowerCICValue3_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AcSS7M3UAStaticRoutingLowerCICValue3_Type.__name__=_B
_AcSS7M3UAStaticRoutingLowerCICValue3_Object=MibTableColumn
acSS7M3UAStaticRoutingLowerCICValue3=_AcSS7M3UAStaticRoutingLowerCICValue3_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,18),_AcSS7M3UAStaticRoutingLowerCICValue3_Type())
acSS7M3UAStaticRoutingLowerCICValue3.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingLowerCICValue3.setStatus(_G)
class _AcSS7M3UAStaticRoutingUpperCICValue3_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AcSS7M3UAStaticRoutingUpperCICValue3_Type.__name__=_B
_AcSS7M3UAStaticRoutingUpperCICValue3_Object=MibTableColumn
acSS7M3UAStaticRoutingUpperCICValue3=_AcSS7M3UAStaticRoutingUpperCICValue3_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,19),_AcSS7M3UAStaticRoutingUpperCICValue3_Type())
acSS7M3UAStaticRoutingUpperCICValue3.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingUpperCICValue3.setStatus(_G)
class _AcSS7M3UAStaticRoutingLowerCICValue4_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AcSS7M3UAStaticRoutingLowerCICValue4_Type.__name__=_B
_AcSS7M3UAStaticRoutingLowerCICValue4_Object=MibTableColumn
acSS7M3UAStaticRoutingLowerCICValue4=_AcSS7M3UAStaticRoutingLowerCICValue4_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,20),_AcSS7M3UAStaticRoutingLowerCICValue4_Type())
acSS7M3UAStaticRoutingLowerCICValue4.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingLowerCICValue4.setStatus(_G)
class _AcSS7M3UAStaticRoutingUpperCICValue4_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AcSS7M3UAStaticRoutingUpperCICValue4_Type.__name__=_B
_AcSS7M3UAStaticRoutingUpperCICValue4_Object=MibTableColumn
acSS7M3UAStaticRoutingUpperCICValue4=_AcSS7M3UAStaticRoutingUpperCICValue4_Object((1,3,6,1,4,1,5003,9,10,12,1,5,23,1,21),_AcSS7M3UAStaticRoutingUpperCICValue4_Type())
acSS7M3UAStaticRoutingUpperCICValue4.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7M3UAStaticRoutingUpperCICValue4.setStatus(_G)
_AcSS7SigTranRoutingContextTable_Object=MibTable
acSS7SigTranRoutingContextTable=_AcSS7SigTranRoutingContextTable_Object((1,3,6,1,4,1,5003,9,10,12,1,5,24))
if mibBuilder.loadTexts:acSS7SigTranRoutingContextTable.setStatus(_A)
_AcSS7SigTranRoutingContextEntry_Object=MibTableRow
acSS7SigTranRoutingContextEntry=_AcSS7SigTranRoutingContextEntry_Object((1,3,6,1,4,1,5003,9,10,12,1,5,24,1))
acSS7SigTranRoutingContextEntry.setIndexNames((0,_H,_A3),(0,_H,_A4))
if mibBuilder.loadTexts:acSS7SigTranRoutingContextEntry.setStatus(_A)
class _AcSS7SigTranRoutingContextIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_AcSS7SigTranRoutingContextIndex_Type.__name__=_B
_AcSS7SigTranRoutingContextIndex_Object=MibTableColumn
acSS7SigTranRoutingContextIndex=_AcSS7SigTranRoutingContextIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,5,24,1,1),_AcSS7SigTranRoutingContextIndex_Type())
acSS7SigTranRoutingContextIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7SigTranRoutingContextIndex.setStatus(_A)
class _AcSS7SigTranRoutingContextInnerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AcSS7SigTranRoutingContextInnerIndex_Type.__name__=_B
_AcSS7SigTranRoutingContextInnerIndex_Object=MibTableColumn
acSS7SigTranRoutingContextInnerIndex=_AcSS7SigTranRoutingContextInnerIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,5,24,1,2),_AcSS7SigTranRoutingContextInnerIndex_Type())
acSS7SigTranRoutingContextInnerIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7SigTranRoutingContextInnerIndex.setStatus(_A)
_AcSS7SigTranRoutingContextRowStatus_Type=RowStatus
_AcSS7SigTranRoutingContextRowStatus_Object=MibTableColumn
acSS7SigTranRoutingContextRowStatus=_AcSS7SigTranRoutingContextRowStatus_Object((1,3,6,1,4,1,5003,9,10,12,1,5,24,1,3),_AcSS7SigTranRoutingContextRowStatus_Type())
acSS7SigTranRoutingContextRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranRoutingContextRowStatus.setStatus(_A)
class _AcSS7SigTranRoutingContextAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_S,1),(_T,2)))
_AcSS7SigTranRoutingContextAction_Type.__name__=_D
_AcSS7SigTranRoutingContextAction_Object=MibTableColumn
acSS7SigTranRoutingContextAction=_AcSS7SigTranRoutingContextAction_Object((1,3,6,1,4,1,5003,9,10,12,1,5,24,1,4),_AcSS7SigTranRoutingContextAction_Type())
acSS7SigTranRoutingContextAction.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranRoutingContextAction.setStatus(_A)
class _AcSS7SigTranRoutingContextActionResult_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7SigTranRoutingContextActionResult_Type.__name__=_B
_AcSS7SigTranRoutingContextActionResult_Object=MibTableColumn
acSS7SigTranRoutingContextActionResult=_AcSS7SigTranRoutingContextActionResult_Object((1,3,6,1,4,1,5003,9,10,12,1,5,24,1,5),_AcSS7SigTranRoutingContextActionResult_Type())
acSS7SigTranRoutingContextActionResult.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7SigTranRoutingContextActionResult.setStatus(_A)
class _AcSS7SigTranRoutingContextSnIdx_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_AcSS7SigTranRoutingContextSnIdx_Type.__name__=_B
_AcSS7SigTranRoutingContextSnIdx_Object=MibTableColumn
acSS7SigTranRoutingContextSnIdx=_AcSS7SigTranRoutingContextSnIdx_Object((1,3,6,1,4,1,5003,9,10,12,1,5,24,1,6),_AcSS7SigTranRoutingContextSnIdx_Type())
acSS7SigTranRoutingContextSnIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranRoutingContextSnIdx.setStatus(_A)
class _AcSS7SigTranRoutingContextSpc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,16777215))
_AcSS7SigTranRoutingContextSpc_Type.__name__=_D
_AcSS7SigTranRoutingContextSpc_Object=MibTableColumn
acSS7SigTranRoutingContextSpc=_AcSS7SigTranRoutingContextSpc_Object((1,3,6,1,4,1,5003,9,10,12,1,5,24,1,7),_AcSS7SigTranRoutingContextSpc_Type())
acSS7SigTranRoutingContextSpc.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7SigTranRoutingContextSpc.setStatus(_A)
class _AcSS7SigTranRoutingContextOpc1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,16777215))
_AcSS7SigTranRoutingContextOpc1_Type.__name__=_D
_AcSS7SigTranRoutingContextOpc1_Object=MibTableColumn
acSS7SigTranRoutingContextOpc1=_AcSS7SigTranRoutingContextOpc1_Object((1,3,6,1,4,1,5003,9,10,12,1,5,24,1,8),_AcSS7SigTranRoutingContextOpc1_Type())
acSS7SigTranRoutingContextOpc1.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranRoutingContextOpc1.setStatus(_A)
class _AcSS7SigTranRoutingContextOpc2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,16777215))
_AcSS7SigTranRoutingContextOpc2_Type.__name__=_D
_AcSS7SigTranRoutingContextOpc2_Object=MibTableColumn
acSS7SigTranRoutingContextOpc2=_AcSS7SigTranRoutingContextOpc2_Object((1,3,6,1,4,1,5003,9,10,12,1,5,24,1,9),_AcSS7SigTranRoutingContextOpc2_Type())
acSS7SigTranRoutingContextOpc2.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranRoutingContextOpc2.setStatus(_A)
class _AcSS7SigTranRoutingContextOpc3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,16777215))
_AcSS7SigTranRoutingContextOpc3_Type.__name__=_D
_AcSS7SigTranRoutingContextOpc3_Object=MibTableColumn
acSS7SigTranRoutingContextOpc3=_AcSS7SigTranRoutingContextOpc3_Object((1,3,6,1,4,1,5003,9,10,12,1,5,24,1,10),_AcSS7SigTranRoutingContextOpc3_Type())
acSS7SigTranRoutingContextOpc3.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranRoutingContextOpc3.setStatus(_A)
class _AcSS7SigTranRoutingContextOpc4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,16777215))
_AcSS7SigTranRoutingContextOpc4_Type.__name__=_D
_AcSS7SigTranRoutingContextOpc4_Object=MibTableColumn
acSS7SigTranRoutingContextOpc4=_AcSS7SigTranRoutingContextOpc4_Object((1,3,6,1,4,1,5003,9,10,12,1,5,24,1,11),_AcSS7SigTranRoutingContextOpc4_Type())
acSS7SigTranRoutingContextOpc4.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranRoutingContextOpc4.setStatus(_A)
class _AcSS7SigTranRoutingContextSi1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,15))
_AcSS7SigTranRoutingContextSi1_Type.__name__=_D
_AcSS7SigTranRoutingContextSi1_Object=MibTableColumn
acSS7SigTranRoutingContextSi1=_AcSS7SigTranRoutingContextSi1_Object((1,3,6,1,4,1,5003,9,10,12,1,5,24,1,12),_AcSS7SigTranRoutingContextSi1_Type())
acSS7SigTranRoutingContextSi1.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranRoutingContextSi1.setStatus(_A)
class _AcSS7SigTranRoutingContextSi2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,15))
_AcSS7SigTranRoutingContextSi2_Type.__name__=_D
_AcSS7SigTranRoutingContextSi2_Object=MibTableColumn
acSS7SigTranRoutingContextSi2=_AcSS7SigTranRoutingContextSi2_Object((1,3,6,1,4,1,5003,9,10,12,1,5,24,1,13),_AcSS7SigTranRoutingContextSi2_Type())
acSS7SigTranRoutingContextSi2.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranRoutingContextSi2.setStatus(_A)
class _AcSS7SigTranRoutingContextSi3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,15))
_AcSS7SigTranRoutingContextSi3_Type.__name__=_D
_AcSS7SigTranRoutingContextSi3_Object=MibTableColumn
acSS7SigTranRoutingContextSi3=_AcSS7SigTranRoutingContextSi3_Object((1,3,6,1,4,1,5003,9,10,12,1,5,24,1,14),_AcSS7SigTranRoutingContextSi3_Type())
acSS7SigTranRoutingContextSi3.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranRoutingContextSi3.setStatus(_A)
class _AcSS7SigTranRoutingContextSi4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,15))
_AcSS7SigTranRoutingContextSi4_Type.__name__=_D
_AcSS7SigTranRoutingContextSi4_Object=MibTableColumn
acSS7SigTranRoutingContextSi4=_AcSS7SigTranRoutingContextSi4_Object((1,3,6,1,4,1,5003,9,10,12,1,5,24,1,15),_AcSS7SigTranRoutingContextSi4_Type())
acSS7SigTranRoutingContextSi4.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7SigTranRoutingContextSi4.setStatus(_A)
_AcSS7Redundancy_ObjectIdentity=ObjectIdentity
acSS7Redundancy=_AcSS7Redundancy_ObjectIdentity((1,3,6,1,4,1,5003,9,10,12,1,6))
class _AcSS7RedundancyCrossLinkTransferType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*((_J,0),('tcp',2)))
_AcSS7RedundancyCrossLinkTransferType_Type.__name__=_D
_AcSS7RedundancyCrossLinkTransferType_Object=MibScalar
acSS7RedundancyCrossLinkTransferType=_AcSS7RedundancyCrossLinkTransferType_Object((1,3,6,1,4,1,5003,9,10,12,1,6,1),_AcSS7RedundancyCrossLinkTransferType_Type())
acSS7RedundancyCrossLinkTransferType.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7RedundancyCrossLinkTransferType.setStatus(_A)
class _AcSS7RedundancyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_AcSS7RedundancyMode_Type.__name__=_D
_AcSS7RedundancyMode_Object=MibScalar
acSS7RedundancyMode=_AcSS7RedundancyMode_Object((1,3,6,1,4,1,5003,9,10,12,1,6,2),_AcSS7RedundancyMode_Type())
acSS7RedundancyMode.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7RedundancyMode.setStatus(_A)
class _AcSS7RedundancyBoardNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcSS7RedundancyBoardNum_Type.__name__=_B
_AcSS7RedundancyBoardNum_Object=MibScalar
acSS7RedundancyBoardNum=_AcSS7RedundancyBoardNum_Object((1,3,6,1,4,1,5003,9,10,12,1,6,3),_AcSS7RedundancyBoardNum_Type())
acSS7RedundancyBoardNum.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7RedundancyBoardNum.setStatus(_A)
class _AcSS7RedundancyCrossLinkTraceAll_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_AcSS7RedundancyCrossLinkTraceAll_Type.__name__=_D
_AcSS7RedundancyCrossLinkTraceAll_Object=MibScalar
acSS7RedundancyCrossLinkTraceAll=_AcSS7RedundancyCrossLinkTraceAll_Object((1,3,6,1,4,1,5003,9,10,12,1,6,4),_AcSS7RedundancyCrossLinkTraceAll_Type())
acSS7RedundancyCrossLinkTraceAll.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7RedundancyCrossLinkTraceAll.setStatus(_G)
class _AcSS7RedundancyMTP3RdcyTblSyncInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,144000))
_AcSS7RedundancyMTP3RdcyTblSyncInterval_Type.__name__=_B
_AcSS7RedundancyMTP3RdcyTblSyncInterval_Object=MibScalar
acSS7RedundancyMTP3RdcyTblSyncInterval=_AcSS7RedundancyMTP3RdcyTblSyncInterval_Object((1,3,6,1,4,1,5003,9,10,12,1,6,5),_AcSS7RedundancyMTP3RdcyTblSyncInterval_Type())
acSS7RedundancyMTP3RdcyTblSyncInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7RedundancyMTP3RdcyTblSyncInterval.setStatus(_A)
class _AcSS7RedundancySyncAllBoards_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noAction',0),('sync',1)))
_AcSS7RedundancySyncAllBoards_Type.__name__=_D
_AcSS7RedundancySyncAllBoards_Object=MibScalar
acSS7RedundancySyncAllBoards=_AcSS7RedundancySyncAllBoards_Object((1,3,6,1,4,1,5003,9,10,12,1,6,6),_AcSS7RedundancySyncAllBoards_Type())
acSS7RedundancySyncAllBoards.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7RedundancySyncAllBoards.setStatus(_A)
class _AcSS7RedundancySyncBoard_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7RedundancySyncBoard_Type.__name__=_B
_AcSS7RedundancySyncBoard_Object=MibScalar
acSS7RedundancySyncBoard=_AcSS7RedundancySyncBoard_Object((1,3,6,1,4,1,5003,9,10,12,1,6,7),_AcSS7RedundancySyncBoard_Type())
acSS7RedundancySyncBoard.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7RedundancySyncBoard.setStatus(_A)
class _AcSS7RedundancyKeepAliveWindow_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_AcSS7RedundancyKeepAliveWindow_Type.__name__=_B
_AcSS7RedundancyKeepAliveWindow_Object=MibScalar
acSS7RedundancyKeepAliveWindow=_AcSS7RedundancyKeepAliveWindow_Object((1,3,6,1,4,1,5003,9,10,12,1,6,8),_AcSS7RedundancyKeepAliveWindow_Type())
acSS7RedundancyKeepAliveWindow.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7RedundancyKeepAliveWindow.setStatus(_A)
class _AcSS7RedundancyKeepAliveInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_AcSS7RedundancyKeepAliveInterval_Type.__name__=_B
_AcSS7RedundancyKeepAliveInterval_Object=MibScalar
acSS7RedundancyKeepAliveInterval=_AcSS7RedundancyKeepAliveInterval_Object((1,3,6,1,4,1,5003,9,10,12,1,6,9),_AcSS7RedundancyKeepAliveInterval_Type())
acSS7RedundancyKeepAliveInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:acSS7RedundancyKeepAliveInterval.setStatus(_A)
_AcSS7RedundantSNTable_Object=MibTable
acSS7RedundantSNTable=_AcSS7RedundantSNTable_Object((1,3,6,1,4,1,5003,9,10,12,1,6,21))
if mibBuilder.loadTexts:acSS7RedundantSNTable.setStatus(_A)
_AcSS7RedundantSNEntry_Object=MibTableRow
acSS7RedundantSNEntry=_AcSS7RedundantSNEntry_Object((1,3,6,1,4,1,5003,9,10,12,1,6,21,1))
acSS7RedundantSNEntry.setIndexNames((0,_H,_A5),(0,_H,_A6))
if mibBuilder.loadTexts:acSS7RedundantSNEntry.setStatus(_A)
class _AcSS7RedundantSNBoardIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_AcSS7RedundantSNBoardIndex_Type.__name__=_B
_AcSS7RedundantSNBoardIndex_Object=MibTableColumn
acSS7RedundantSNBoardIndex=_AcSS7RedundantSNBoardIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,6,21,1,1),_AcSS7RedundantSNBoardIndex_Type())
acSS7RedundantSNBoardIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7RedundantSNBoardIndex.setStatus(_A)
class _AcSS7RedundantSNIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_AcSS7RedundantSNIndex_Type.__name__=_B
_AcSS7RedundantSNIndex_Object=MibTableColumn
acSS7RedundantSNIndex=_AcSS7RedundantSNIndex_Object((1,3,6,1,4,1,5003,9,10,12,1,6,21,1,2),_AcSS7RedundantSNIndex_Type())
acSS7RedundantSNIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:acSS7RedundantSNIndex.setStatus(_A)
_AcSS7RedundantSNRowStatus_Type=RowStatus
_AcSS7RedundantSNRowStatus_Object=MibTableColumn
acSS7RedundantSNRowStatus=_AcSS7RedundantSNRowStatus_Object((1,3,6,1,4,1,5003,9,10,12,1,6,21,1,3),_AcSS7RedundantSNRowStatus_Type())
acSS7RedundantSNRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7RedundantSNRowStatus.setStatus(_A)
class _AcSS7RedundantSNAction_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7RedundantSNAction_Type.__name__=_B
_AcSS7RedundantSNAction_Object=MibTableColumn
acSS7RedundantSNAction=_AcSS7RedundantSNAction_Object((1,3,6,1,4,1,5003,9,10,12,1,6,21,1,4),_AcSS7RedundantSNAction_Type())
acSS7RedundantSNAction.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7RedundantSNAction.setStatus(_A)
class _AcSS7RedundantSNActionRes_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7RedundantSNActionRes_Type.__name__=_B
_AcSS7RedundantSNActionRes_Object=MibTableColumn
acSS7RedundantSNActionRes=_AcSS7RedundantSNActionRes_Object((1,3,6,1,4,1,5003,9,10,12,1,6,21,1,5),_AcSS7RedundantSNActionRes_Type())
acSS7RedundantSNActionRes.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7RedundantSNActionRes.setStatus(_A)
_AcSS7RedundantSNBoardIp_Type=IpAddress
_AcSS7RedundantSNBoardIp_Object=MibTableColumn
acSS7RedundantSNBoardIp=_AcSS7RedundantSNBoardIp_Object((1,3,6,1,4,1,5003,9,10,12,1,6,21,1,6),_AcSS7RedundantSNBoardIp_Type())
acSS7RedundantSNBoardIp.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7RedundantSNBoardIp.setStatus(_A)
class _AcSS7RedundantSNOPC_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7RedundantSNOPC_Type.__name__=_B
_AcSS7RedundantSNOPC_Object=MibTableColumn
acSS7RedundantSNOPC=_AcSS7RedundantSNOPC_Object((1,3,6,1,4,1,5003,9,10,12,1,6,21,1,7),_AcSS7RedundantSNOPC_Type())
acSS7RedundantSNOPC.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7RedundantSNOPC.setStatus(_A)
class _AcSS7RedundantSNALCAPOPC_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AcSS7RedundantSNALCAPOPC_Type.__name__=_B
_AcSS7RedundantSNALCAPOPC_Object=MibTableColumn
acSS7RedundantSNALCAPOPC=_AcSS7RedundantSNALCAPOPC_Object((1,3,6,1,4,1,5003,9,10,12,1,6,21,1,8),_AcSS7RedundantSNALCAPOPC_Type())
acSS7RedundantSNALCAPOPC.setMaxAccess(_C)
if mibBuilder.loadTexts:acSS7RedundantSNALCAPOPC.setStatus(_A)
_AcSS7Status_ObjectIdentity=ObjectIdentity
acSS7Status=_AcSS7Status_ObjectIdentity((1,3,6,1,4,1,5003,9,10,12,2))
_AcSS7Constants_ObjectIdentity=ObjectIdentity
acSS7Constants=_AcSS7Constants_ObjectIdentity((1,3,6,1,4,1,5003,9,10,12,2,1))
class _AcSS7ConstantsNumberOfNodes_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_AcSS7ConstantsNumberOfNodes_Type.__name__=_B
_AcSS7ConstantsNumberOfNodes_Object=MibScalar
acSS7ConstantsNumberOfNodes=_AcSS7ConstantsNumberOfNodes_Object((1,3,6,1,4,1,5003,9,10,12,2,1,1),_AcSS7ConstantsNumberOfNodes_Type())
acSS7ConstantsNumberOfNodes.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7ConstantsNumberOfNodes.setStatus(_A)
class _AcSS7ConstantsNumberOfLinks_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_AcSS7ConstantsNumberOfLinks_Type.__name__=_B
_AcSS7ConstantsNumberOfLinks_Object=MibScalar
acSS7ConstantsNumberOfLinks=_AcSS7ConstantsNumberOfLinks_Object((1,3,6,1,4,1,5003,9,10,12,2,1,2),_AcSS7ConstantsNumberOfLinks_Type())
acSS7ConstantsNumberOfLinks.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7ConstantsNumberOfLinks.setStatus(_A)
class _AcSS7ConstantsNumberOfLinkSetsPerSN_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_AcSS7ConstantsNumberOfLinkSetsPerSN_Type.__name__=_B
_AcSS7ConstantsNumberOfLinkSetsPerSN_Object=MibScalar
acSS7ConstantsNumberOfLinkSetsPerSN=_AcSS7ConstantsNumberOfLinkSetsPerSN_Object((1,3,6,1,4,1,5003,9,10,12,2,1,3),_AcSS7ConstantsNumberOfLinkSetsPerSN_Type())
acSS7ConstantsNumberOfLinkSetsPerSN.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7ConstantsNumberOfLinkSetsPerSN.setStatus(_A)
class _AcSS7ConstantsNumberOfLinksPerLinkSet_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_AcSS7ConstantsNumberOfLinksPerLinkSet_Type.__name__=_B
_AcSS7ConstantsNumberOfLinksPerLinkSet_Object=MibScalar
acSS7ConstantsNumberOfLinksPerLinkSet=_AcSS7ConstantsNumberOfLinksPerLinkSet_Object((1,3,6,1,4,1,5003,9,10,12,2,1,4),_AcSS7ConstantsNumberOfLinksPerLinkSet_Type())
acSS7ConstantsNumberOfLinksPerLinkSet.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7ConstantsNumberOfLinksPerLinkSet.setStatus(_A)
class _AcSS7ConstantsNumberOfRouteSetsPerSN_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_AcSS7ConstantsNumberOfRouteSetsPerSN_Type.__name__=_B
_AcSS7ConstantsNumberOfRouteSetsPerSN_Object=MibScalar
acSS7ConstantsNumberOfRouteSetsPerSN=_AcSS7ConstantsNumberOfRouteSetsPerSN_Object((1,3,6,1,4,1,5003,9,10,12,2,1,5),_AcSS7ConstantsNumberOfRouteSetsPerSN_Type())
acSS7ConstantsNumberOfRouteSetsPerSN.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7ConstantsNumberOfRouteSetsPerSN.setStatus(_A)
class _AcSS7ConstantsNumberOfRoutesPerRouteSets_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_AcSS7ConstantsNumberOfRoutesPerRouteSets_Type.__name__=_B
_AcSS7ConstantsNumberOfRoutesPerRouteSets_Object=MibScalar
acSS7ConstantsNumberOfRoutesPerRouteSets=_AcSS7ConstantsNumberOfRoutesPerRouteSets_Object((1,3,6,1,4,1,5003,9,10,12,2,1,6),_AcSS7ConstantsNumberOfRoutesPerRouteSets_Type())
acSS7ConstantsNumberOfRoutesPerRouteSets.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7ConstantsNumberOfRoutesPerRouteSets.setStatus(_A)
class _AcSS7ConstantsNumberOfNodeTimerSets_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_AcSS7ConstantsNumberOfNodeTimerSets_Type.__name__=_B
_AcSS7ConstantsNumberOfNodeTimerSets_Object=MibScalar
acSS7ConstantsNumberOfNodeTimerSets=_AcSS7ConstantsNumberOfNodeTimerSets_Object((1,3,6,1,4,1,5003,9,10,12,2,1,7),_AcSS7ConstantsNumberOfNodeTimerSets_Type())
acSS7ConstantsNumberOfNodeTimerSets.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7ConstantsNumberOfNodeTimerSets.setStatus(_A)
class _AcSS7ConstantsNumberOfLinkSetTimerSets_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_AcSS7ConstantsNumberOfLinkSetTimerSets_Type.__name__=_B
_AcSS7ConstantsNumberOfLinkSetTimerSets_Object=MibScalar
acSS7ConstantsNumberOfLinkSetTimerSets=_AcSS7ConstantsNumberOfLinkSetTimerSets_Object((1,3,6,1,4,1,5003,9,10,12,2,1,8),_AcSS7ConstantsNumberOfLinkSetTimerSets_Type())
acSS7ConstantsNumberOfLinkSetTimerSets.setMaxAccess(_F)
if mibBuilder.loadTexts:acSS7ConstantsNumberOfLinkSetTimerSets.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'acSS7':acSS7,'acSS7Configuration':acSS7Configuration,'acSS7MTP2':acSS7MTP2,'acSS7MTP2M3bSlDiscardCongThreshold':acSS7MTP2M3bSlDiscardCongThreshold,'acSS7MTP2AttribTable':acSS7MTP2AttribTable,'acSS7MTP2AttribEntry':acSS7MTP2AttribEntry,_c:acSS7MTP2AttribIndex,'acSS7MTP2AttribIsUsed':acSS7MTP2AttribIsUsed,'acSS7MTP2AttribLinkRate':acSS7MTP2AttribLinkRate,'acSS7MTP2AttribErrorCorectionMethod':acSS7MTP2AttribErrorCorectionMethod,'acSS7MTP2AttribIacCp':acSS7MTP2AttribIacCp,'acSS7MTP2AttribSUERMThreshold':acSS7MTP2AttribSUERMThreshold,'acSS7MTP2AttribAERMNormalThreshold':acSS7MTP2AttribAERMNormalThreshold,'acSS7MTP2AttribAERMEmerglThreshold':acSS7MTP2AttribAERMEmerglThreshold,'acSS7MTP2AttribSUERMSigUnitDThreshold':acSS7MTP2AttribSUERMSigUnitDThreshold,'acSS7MTP2AttribOctetCounting':acSS7MTP2AttribOctetCounting,'acSS7MTP2AttribTimerT1':acSS7MTP2AttribTimerT1,'acSS7MTP2AttribTimerT2':acSS7MTP2AttribTimerT2,'acSS7MTP2AttribTimerT3':acSS7MTP2AttribTimerT3,'acSS7MTP2AttribTimerT4Normal':acSS7MTP2AttribTimerT4Normal,'acSS7MTP2AttribTimerT4Emerg':acSS7MTP2AttribTimerT4Emerg,'acSS7MTP2AttribTimerT5':acSS7MTP2AttribTimerT5,'acSS7MTP2AttribTimerT6':acSS7MTP2AttribTimerT6,'acSS7MTP2AttribTimerT7':acSS7MTP2AttribTimerT7,'acSS7MTP2AttribLSSULength':acSS7MTP2AttribLSSULength,'acSS7MTP2AttribPcrN2':acSS7MTP2AttribPcrN2,'acSS7MTP2AttribRowStatus':acSS7MTP2AttribRowStatus,'acSS7Timers':acSS7Timers,'acSS7SignalingNodeTimersTable':acSS7SignalingNodeTimersTable,'acSS7SignalingNodeTimersEntry':acSS7SignalingNodeTimersEntry,_d:acSS7SignalingNodeTimersIndex,'acSS7SignalingNodeTimersIsUsed':acSS7SignalingNodeTimersIsUsed,'acSS7SignalingNodeTimersAction':acSS7SignalingNodeTimersAction,'acSS7SignalingNodeTimersActionResult':acSS7SignalingNodeTimersActionResult,'acSS7SignalingNodeTimersName':acSS7SignalingNodeTimersName,'acSS7SignalingNodeTimersT6':acSS7SignalingNodeTimersT6,'acSS7SignalingNodeTimersT8':acSS7SignalingNodeTimersT8,'acSS7SignalingNodeTimersT10':acSS7SignalingNodeTimersT10,'acSS7SignalingNodeTimersT11':acSS7SignalingNodeTimersT11,'acSS7SignalingNodeTimersT15':acSS7SignalingNodeTimersT15,'acSS7SignalingNodeTimersT16':acSS7SignalingNodeTimersT16,'acSS7SignalingNodeTimersT18ITU':acSS7SignalingNodeTimersT18ITU,'acSS7SignalingNodeTimersT19ITU':acSS7SignalingNodeTimersT19ITU,'acSS7SignalingNodeTimersT20ITU':acSS7SignalingNodeTimersT20ITU,'acSS7SignalingNodeTimersT21ITU':acSS7SignalingNodeTimersT21ITU,'acSS7SignalingNodeTimersT24ITU':acSS7SignalingNodeTimersT24ITU,'acSS7SignalingNodeTimersT22ANSI':acSS7SignalingNodeTimersT22ANSI,'acSS7SignalingNodeTimersT23ANSI':acSS7SignalingNodeTimersT23ANSI,'acSS7SignalingNodeTimersT24ANSI':acSS7SignalingNodeTimersT24ANSI,'acSS7SignalingNodeTimersT25ANSI':acSS7SignalingNodeTimersT25ANSI,'acSS7SignalingNodeTimersT26ANSI':acSS7SignalingNodeTimersT26ANSI,'acSS7SignalingNodeTimersT27ANSI':acSS7SignalingNodeTimersT27ANSI,'acSS7SignalingNodeTimersT28ANSI':acSS7SignalingNodeTimersT28ANSI,'acSS7SignalingNodeTimersT29ANSI':acSS7SignalingNodeTimersT29ANSI,'acSS7SignalingNodeTimersT30ANSI':acSS7SignalingNodeTimersT30ANSI,'acSS7LinkSetTimersTable':acSS7LinkSetTimersTable,'acSS7LinkSetTimersEntry':acSS7LinkSetTimersEntry,_e:acSS7LinkSetTimersIndex,'acSS7LinkSetTimersIsUsed':acSS7LinkSetTimersIsUsed,'acSS7LinkSetTimersAction':acSS7LinkSetTimersAction,'acSS7LinkSetTimersActionResult':acSS7LinkSetTimersActionResult,'acSS7LinkSetTimersName':acSS7LinkSetTimersName,'acSS7LinkSetTimersT1SLT':acSS7LinkSetTimersT1SLT,'acSS7LinkSetTimersT2SLT':acSS7LinkSetTimersT2SLT,'acSS7LinkSetTimersT1':acSS7LinkSetTimersT1,'acSS7LinkSetTimersT2':acSS7LinkSetTimersT2,'acSS7LinkSetTimersT3':acSS7LinkSetTimersT3,'acSS7LinkSetTimersT4':acSS7LinkSetTimersT4,'acSS7LinkSetTimersT5':acSS7LinkSetTimersT5,'acSS7LinkSetTimersT7':acSS7LinkSetTimersT7,'acSS7LinkSetTimersT12':acSS7LinkSetTimersT12,'acSS7LinkSetTimersT13':acSS7LinkSetTimersT13,'acSS7LinkSetTimersT14':acSS7LinkSetTimersT14,'acSS7LinkSetTimersT17':acSS7LinkSetTimersT17,'acSS7LinkSetTimersT20ANSI':acSS7LinkSetTimersT20ANSI,'acSS7LinkSetTimersT21ANSI':acSS7LinkSetTimersT21ANSI,'acSS7LinkSetTimersT22ITU':acSS7LinkSetTimersT22ITU,'acSS7LinkSetTimersT23ITU':acSS7LinkSetTimersT23ITU,'acSS7Links':acSS7Links,'acSS7LinkCommonTable':acSS7LinkCommonTable,'acSS7LinkCommonEntry':acSS7LinkCommonEntry,_U:acSS7LinkCommonIndex,'acSS7LinkCommonRowStatus':acSS7LinkCommonRowStatus,'acSS7LinkCommonAction':acSS7LinkCommonAction,'acSS7LinkCommonActionResult':acSS7LinkCommonActionResult,'acSS7LinkCommonName':acSS7LinkCommonName,'acSS7LinkCommonAdminState':acSS7LinkCommonAdminState,'acSS7LinkCommonOperState':acSS7LinkCommonOperState,'acSS7LinkCommonTraceLevel':acSS7LinkCommonTraceLevel,'acSS7LinkCommonL2TypeSelector':acSS7LinkCommonL2TypeSelector,'acSS7LinkCommonL3TypeSelector':acSS7LinkCommonL3TypeSelector,'acSS7LinkCommonVariant':acSS7LinkCommonVariant,'acSS7LinkCommonMtcBusy':acSS7LinkCommonMtcBusy,'acSS7LinkCommonRdcyBoardNum':acSS7LinkCommonRdcyBoardNum,'acSS7LinkCommonMonSuFilterRequest':acSS7LinkCommonMonSuFilterRequest,'acSS7LinkTDMTable':acSS7LinkTDMTable,'acSS7LinkTDMEntry':acSS7LinkTDMEntry,'acSS7LinkTDMTrunkNumber':acSS7LinkTDMTrunkNumber,'acSS7LinkTDMTimeSlotNumber':acSS7LinkTDMTimeSlotNumber,'acSS7LinkTDMInhibit':acSS7LinkTDMInhibit,'acSS7LinkTDMMtp2Atts':acSS7LinkTDMMtp2Atts,'acSS7LinkTDMCongestionLowMark':acSS7LinkTDMCongestionLowMark,'acSS7LinkTDMCongestionHighMark':acSS7LinkTDMCongestionHighMark,'acSS7LinkTDMBlock':acSS7LinkTDMBlock,'acSS7LinkSigTranTable':acSS7LinkSigTranTable,'acSS7LinkSigTranEntry':acSS7LinkSigTranEntry,'acSS7LinkSigTranGroupId':acSS7LinkSigTranGroupId,'acSS7LinkSigTranIfid':acSS7LinkSigTranIfid,'acSS7LinkATMTable':acSS7LinkATMTable,'acSS7LinkATMEntry':acSS7LinkATMEntry,'acSS7LinkATMSAALLinkProfileNum':acSS7LinkATMSAALLinkProfileNum,'acSS7LinkATMSAALLinkType':acSS7LinkATMSAALLinkType,'acSS7LinkATMSAALLinkInterfaceNum':acSS7LinkATMSAALLinkInterfaceNum,'acSS7LinkATMSAALLinkVPI':acSS7LinkATMSAALLinkVPI,'acSS7LinkATMSAALLinkVCI':acSS7LinkATMSAALLinkVCI,'acSS7LinkTNLTable':acSS7LinkTNLTable,'acSS7LinkTNLEntry':acSS7LinkTNLEntry,'acSS7LinkTNLOtherSideLinkNum':acSS7LinkTNLOtherSideLinkNum,'acSS7LinkTNLAlignmentMode':acSS7LinkTNLAlignmentMode,'acSS7LinkTNLCongestionMode':acSS7LinkTNLCongestionMode,'acSS7LinkTNLWaitStartCompTimer':acSS7LinkTNLWaitStartCompTimer,'acSS7LinkTNLOosStartDelayTimer':acSS7LinkTNLOosStartDelayTimer,'acSS7LinkTNLWaitOtherSideInsvTimer':acSS7LinkTNLWaitOtherSideInsvTimer,'acSS7Nodes':acSS7Nodes,'acSS7SignalingNodeTable':acSS7SignalingNodeTable,'acSS7SignalingNodeEntry':acSS7SignalingNodeEntry,_i:acSS7SignalingNodeIndex,'acSS7SignalingNodeRowStatus':acSS7SignalingNodeRowStatus,'acSS7SignalingNodeAction':acSS7SignalingNodeAction,'acSS7SignalingNodeActionResult':acSS7SignalingNodeActionResult,'acSS7SignalingNodeName':acSS7SignalingNodeName,'acSS7SignalingNodeTraceLevel':acSS7SignalingNodeTraceLevel,'acSS7SignalingNodeAdminState':acSS7SignalingNodeAdminState,'acSS7SignalingNodeOperState':acSS7SignalingNodeOperState,'acSS7SignalingNodeMtcBusy':acSS7SignalingNodeMtcBusy,'acSS7SignalingNodeVariant':acSS7SignalingNodeVariant,'acSS7SignalingNodeNwIndicator':acSS7SignalingNodeNwIndicator,'acSS7SignalingNodeSpStp':acSS7SignalingNodeSpStp,'acSS7SignalingNodeTfc':acSS7SignalingNodeTfc,'acSS7SignalingNodeOpc':acSS7SignalingNodeOpc,'acSS7SignalingNodeRouteSetCongestionWindow':acSS7SignalingNodeRouteSetCongestionWindow,'acSS7SignalingNodeTimersIdx':acSS7SignalingNodeTimersIdx,'acSS7SignalingNodeIsupApp':acSS7SignalingNodeIsupApp,'acSS7SignalingNodeSccpApp':acSS7SignalingNodeSccpApp,'acSS7SignalingNodeBisupApp':acSS7SignalingNodeBisupApp,'acSS7SignalingNodeAlcapApp':acSS7SignalingNodeAlcapApp,'acSS7SignalingNodeRdcyOpc':acSS7SignalingNodeRdcyOpc,'acSS7SignalingNodeTupApp':acSS7SignalingNodeTupApp,'acSS7SignalingNodeBiccApp':acSS7SignalingNodeBiccApp,'acSS7LinkSets':acSS7LinkSets,'acSS7LinkSetTable':acSS7LinkSetTable,'acSS7LinkSetEntry':acSS7LinkSetEntry,_o:acSS7LinkSetSNIndex,_p:acSS7LinkSetLksetIndex,'acSS7LinkSetRowStatus':acSS7LinkSetRowStatus,'acSS7LinkSetAction':acSS7LinkSetAction,'acSS7LinkSetActionResult':acSS7LinkSetActionResult,'acSS7LinkSetName':acSS7LinkSetName,'acSS7LinkSetAdminState':acSS7LinkSetAdminState,'acSS7LinkSetOperState':acSS7LinkSetOperState,'acSS7LinkSetMtcBusyState':acSS7LinkSetMtcBusyState,'acSS7LinkSetDPC':acSS7LinkSetDPC,'acSS7LinkSetLinksMask':acSS7LinkSetLinksMask,'acSS7LinkSetLinksAltMask':acSS7LinkSetLinksAltMask,'acSS7LinkSetTimersIdx':acSS7LinkSetTimersIdx,'acSS7LinkSetLinkTable':acSS7LinkSetLinkTable,'acSS7LinkSetLinkEntry':acSS7LinkSetLinkEntry,_q:acSS7LinkSetLinkSNIndex,_r:acSS7LinkSetLinkLinksetIndex,_s:acSS7LinkSetLinkInnerLinkIndex,'acSS7LinkSetLinkRowStatus':acSS7LinkSetLinkRowStatus,'acSS7LinkSetLinkAction':acSS7LinkSetLinkAction,'acSS7LinkSetLinkActionResult':acSS7LinkSetLinkActionResult,'acSS7LinkSetLinkLinkNo':acSS7LinkSetLinkLinkNo,'acSS7LinkSetLinkLinkSlc':acSS7LinkSetLinkLinkSlc,'acSS7RouteSets':acSS7RouteSets,'acSS7RouteSetTable':acSS7RouteSetTable,'acSS7RouteSetEntry':acSS7RouteSetEntry,_t:acSS7RouteSetSNIndex,_u:acSS7RouteSetIndex,'acSS7RouteSetRowStatus':acSS7RouteSetRowStatus,'acSS7RouteSetAction':acSS7RouteSetAction,'acSS7RouteSetActionResult':acSS7RouteSetActionResult,'acSS7RouteSetName':acSS7RouteSetName,'acSS7RouteSetAdminState':acSS7RouteSetAdminState,'acSS7RouteSetOperState':acSS7RouteSetOperState,'acSS7RouteSetDPC':acSS7RouteSetDPC,'acSS7RouteSetRouteMask':acSS7RouteSetRouteMask,'acSS7RouteSetRouteTable':acSS7RouteSetRouteTable,'acSS7RouteSetRouteEntry':acSS7RouteSetRouteEntry,_v:acSS7RouteSetRouteSNIndex,_w:acSS7RouteSetRouteRoutesetIndex,_x:acSS7RouteSetRouteInnerRouteIndex,'acSS7RouteSetRouteRowStatus':acSS7RouteSetRouteRowStatus,'acSS7RouteSetRouteAction':acSS7RouteSetRouteAction,'acSS7RouteSetRouteActionResult':acSS7RouteSetRouteActionResult,'acSS7RouteSetRouteLinkSetNo':acSS7RouteSetRouteLinkSetNo,'acSS7RouteSetRoutePriority':acSS7RouteSetRoutePriority,'acSS7AliasPointCode':acSS7AliasPointCode,'acSS7APCTable':acSS7APCTable,'acSS7APCEntry':acSS7APCEntry,_y:acSS7APCSNIndex,_z:acSS7APCIndex,'acSS7APCRowStatus':acSS7APCRowStatus,'acSS7APCAction':acSS7APCAction,'acSS7APCActionResult':acSS7APCActionResult,'acSS7APCPC':acSS7APCPC,'acSS7APCSNI':acSS7APCSNI,'acSS7APCName':acSS7APCName,'acSS7APCMtcBusy':acSS7APCMtcBusy,'acSS7APCAdminState':acSS7APCAdminState,'acSS7APCOperState':acSS7APCOperState,'acSS7SigTran':acSS7SigTran,'acSS7SigTranM3UATrafficBehavior':acSS7SigTranM3UATrafficBehavior,'acSS7SigTranIFGroupTable':acSS7SigTranIFGroupTable,'acSS7SigTranIFGroupEntry':acSS7SigTranIFGroupEntry,_A0:acSS7SigTranIFGroupIndex,'acSS7SigTranIFGroupRowStatus':acSS7SigTranIFGroupRowStatus,'acSS7SigTranIFGroupAction':acSS7SigTranIFGroupAction,'acSS7SigTranIFGroupActionResult':acSS7SigTranIFGroupActionResult,'acSS7SigTranIFGroupId':acSS7SigTranIFGroupId,'acSS7SigTranIFGroupSgMgc':acSS7SigTranIFGroupSgMgc,'acSS7SigTranIFGroupSignalingLayer':acSS7SigTranIFGroupSignalingLayer,'acSS7SigTranIFGroupTrafMode':acSS7SigTranIFGroupTrafMode,'acSS7SigTranIFGroupRecovTimer':acSS7SigTranIFGroupRecovTimer,'acSS7SigTranIFGroupAckTimer':acSS7SigTranIFGroupAckTimer,'acSS7SigTranIFGroupHBTimer':acSS7SigTranIFGroupHBTimer,'acSS7SigTranIFGroupMinAsp':acSS7SigTranIFGroupMinAsp,'acSS7SigTranIFGroupBehavior':acSS7SigTranIFGroupBehavior,'acSS7SigTranIFGroupSCTPInst':acSS7SigTranIFGroupSCTPInst,'acSS7SigTranIFGroupSCTPLocalPort':acSS7SigTranIFGroupSCTPLocalPort,'acSS7SigTranIFGroupNetwork':acSS7SigTranIFGroupNetwork,'acSS7SigTranIFGroupSCTPDestPort':acSS7SigTranIFGroupSCTPDestPort,'acSS7SigTranIFGroupDestIp':acSS7SigTranIFGroupDestIp,'acSS7SigTranIFGroupSCTPMaxInbStreams':acSS7SigTranIFGroupSCTPMaxInbStreams,'acSS7SigTranIFGroupSCTPMaxOutbStreams':acSS7SigTranIFGroupSCTPMaxOutbStreams,'acSS7SigTranIFGroupRdcyBoardNum':acSS7SigTranIFGroupRdcyBoardNum,'acSS7SigTranIFGroupRoutingContextIndex':acSS7SigTranIFGroupRoutingContextIndex,'acSS7SigTranIFGroupRoutingContextValue':acSS7SigTranIFGroupRoutingContextValue,'acSS7SigTranIFGroupNetworkAppearance':acSS7SigTranIFGroupNetworkAppearance,'acSS7SigTranIFIDTable':acSS7SigTranIFIDTable,'acSS7SigTranIFIDEntry':acSS7SigTranIFIDEntry,_A1:acSS7SigTranIFIDIndex,'acSS7SigTranIFIDRowStatus':acSS7SigTranIFIDRowStatus,'acSS7SigTranIFIDAction':acSS7SigTranIFIDAction,'acSS7SigTranIFIDActionResult':acSS7SigTranIFIDActionResult,'acSS7SigTranIFIDValue':acSS7SigTranIFIDValue,'acSS7SigTranIFIDName':acSS7SigTranIFIDName,'acSS7SigTranIFIDOwnerGroup':acSS7SigTranIFIDOwnerGroup,'acSS7SigTranIFIDSignalingLayer':acSS7SigTranIFIDSignalingLayer,'acSS7SigTranIFIDNai':acSS7SigTranIFIDNai,'acSS7SigTranIFIDM3UASpc':acSS7SigTranIFIDM3UASpc,'acSS7M3UAStaticRoutingTable':acSS7M3UAStaticRoutingTable,'acSS7M3UAStaticRoutingEntry':acSS7M3UAStaticRoutingEntry,_A2:acSS7M3UAStaticRoutingIndex,'acSS7M3UAStaticRoutingRowStatus':acSS7M3UAStaticRoutingRowStatus,'acSS7M3UAStaticRoutingAction':acSS7M3UAStaticRoutingAction,'acSS7M3UAStaticRoutingActionResult':acSS7M3UAStaticRoutingActionResult,'acSS7M3UAStaticRoutingOwnerInterfaceGroup':acSS7M3UAStaticRoutingOwnerInterfaceGroup,'acSS7M3UAStaticRoutingRC':acSS7M3UAStaticRoutingRC,'acSS7M3UAStaticRoutingDestinationPointCode':acSS7M3UAStaticRoutingDestinationPointCode,'acSS7M3UAStaticRoutingNetworkAppearence':acSS7M3UAStaticRoutingNetworkAppearence,'acSS7M3UAStaticRoutingSeriviceIndicatorList':acSS7M3UAStaticRoutingSeriviceIndicatorList,'acSS7M3UAStaticRoutingOPC1':acSS7M3UAStaticRoutingOPC1,'acSS7M3UAStaticRoutingOPC2':acSS7M3UAStaticRoutingOPC2,'acSS7M3UAStaticRoutingOPC3':acSS7M3UAStaticRoutingOPC3,'acSS7M3UAStaticRoutingOPC4':acSS7M3UAStaticRoutingOPC4,'acSS7M3UAStaticRoutingLowerCICValue1':acSS7M3UAStaticRoutingLowerCICValue1,'acSS7M3UAStaticRoutingUpperCICValue1':acSS7M3UAStaticRoutingUpperCICValue1,'acSS7M3UAStaticRoutingLowerCICValue2':acSS7M3UAStaticRoutingLowerCICValue2,'acSS7M3UAStaticRoutingUpperCICValue2':acSS7M3UAStaticRoutingUpperCICValue2,'acSS7M3UAStaticRoutingLowerCICValue3':acSS7M3UAStaticRoutingLowerCICValue3,'acSS7M3UAStaticRoutingUpperCICValue3':acSS7M3UAStaticRoutingUpperCICValue3,'acSS7M3UAStaticRoutingLowerCICValue4':acSS7M3UAStaticRoutingLowerCICValue4,'acSS7M3UAStaticRoutingUpperCICValue4':acSS7M3UAStaticRoutingUpperCICValue4,'acSS7SigTranRoutingContextTable':acSS7SigTranRoutingContextTable,'acSS7SigTranRoutingContextEntry':acSS7SigTranRoutingContextEntry,_A3:acSS7SigTranRoutingContextIndex,_A4:acSS7SigTranRoutingContextInnerIndex,'acSS7SigTranRoutingContextRowStatus':acSS7SigTranRoutingContextRowStatus,'acSS7SigTranRoutingContextAction':acSS7SigTranRoutingContextAction,'acSS7SigTranRoutingContextActionResult':acSS7SigTranRoutingContextActionResult,'acSS7SigTranRoutingContextSnIdx':acSS7SigTranRoutingContextSnIdx,'acSS7SigTranRoutingContextSpc':acSS7SigTranRoutingContextSpc,'acSS7SigTranRoutingContextOpc1':acSS7SigTranRoutingContextOpc1,'acSS7SigTranRoutingContextOpc2':acSS7SigTranRoutingContextOpc2,'acSS7SigTranRoutingContextOpc3':acSS7SigTranRoutingContextOpc3,'acSS7SigTranRoutingContextOpc4':acSS7SigTranRoutingContextOpc4,'acSS7SigTranRoutingContextSi1':acSS7SigTranRoutingContextSi1,'acSS7SigTranRoutingContextSi2':acSS7SigTranRoutingContextSi2,'acSS7SigTranRoutingContextSi3':acSS7SigTranRoutingContextSi3,'acSS7SigTranRoutingContextSi4':acSS7SigTranRoutingContextSi4,'acSS7Redundancy':acSS7Redundancy,'acSS7RedundancyCrossLinkTransferType':acSS7RedundancyCrossLinkTransferType,'acSS7RedundancyMode':acSS7RedundancyMode,'acSS7RedundancyBoardNum':acSS7RedundancyBoardNum,'acSS7RedundancyCrossLinkTraceAll':acSS7RedundancyCrossLinkTraceAll,'acSS7RedundancyMTP3RdcyTblSyncInterval':acSS7RedundancyMTP3RdcyTblSyncInterval,'acSS7RedundancySyncAllBoards':acSS7RedundancySyncAllBoards,'acSS7RedundancySyncBoard':acSS7RedundancySyncBoard,'acSS7RedundancyKeepAliveWindow':acSS7RedundancyKeepAliveWindow,'acSS7RedundancyKeepAliveInterval':acSS7RedundancyKeepAliveInterval,'acSS7RedundantSNTable':acSS7RedundantSNTable,'acSS7RedundantSNEntry':acSS7RedundantSNEntry,_A5:acSS7RedundantSNBoardIndex,_A6:acSS7RedundantSNIndex,'acSS7RedundantSNRowStatus':acSS7RedundantSNRowStatus,'acSS7RedundantSNAction':acSS7RedundantSNAction,'acSS7RedundantSNActionRes':acSS7RedundantSNActionRes,'acSS7RedundantSNBoardIp':acSS7RedundantSNBoardIp,'acSS7RedundantSNOPC':acSS7RedundantSNOPC,'acSS7RedundantSNALCAPOPC':acSS7RedundantSNALCAPOPC,'acSS7Status':acSS7Status,'acSS7Constants':acSS7Constants,'acSS7ConstantsNumberOfNodes':acSS7ConstantsNumberOfNodes,'acSS7ConstantsNumberOfLinks':acSS7ConstantsNumberOfLinks,'acSS7ConstantsNumberOfLinkSetsPerSN':acSS7ConstantsNumberOfLinkSetsPerSN,'acSS7ConstantsNumberOfLinksPerLinkSet':acSS7ConstantsNumberOfLinksPerLinkSet,'acSS7ConstantsNumberOfRouteSetsPerSN':acSS7ConstantsNumberOfRouteSetsPerSN,'acSS7ConstantsNumberOfRoutesPerRouteSets':acSS7ConstantsNumberOfRoutesPerRouteSets,'acSS7ConstantsNumberOfNodeTimerSets':acSS7ConstantsNumberOfNodeTimerSets,'acSS7ConstantsNumberOfLinkSetTimerSets':acSS7ConstantsNumberOfLinkSetTimerSets})