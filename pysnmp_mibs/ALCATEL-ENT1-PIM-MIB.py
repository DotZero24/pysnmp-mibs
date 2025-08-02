_AC='alaPimdmConfigMIBGroup'
_AB='alaPimsmConfigMIBGroup'
_AA='alaPimNonBidirHello'
_A9='alaPimV6BfdAllInterfaceStatus'
_A8='alaPimV6BfdStatus'
_A7='alaPimMbrOperStatus'
_A6='alaPimMbrAllSourcesStatus'
_A5='alaPimInterfaceBfdStatus'
_A4='alaPimMoFRRAllRouteStatus'
_A3='alaPimMoFRRStatus'
_A2='alaPimBfdAllInterfaceStatus'
_A1='alaPimBfdStatus'
_A0='alaPimdmDenseGroupRowStatus'
_z='alaPimdmDenseGroupPrecedence'
_y='alaPimdmDenseGroupOverrideDynamic'
_x='alaPimdmV6AdminStatus'
_w='alaPimdmStateRefreshLimitInterval'
_v='alaPimdmStateRefreshTimeToLive'
_u='alaPimdmAdminStatus'
_t='alaPimsmV6SsmFastJoin'
_s='alaPimsmSsmFastJoin'
_r='alaPimsmV6AsmFastJoin'
_q='alaPimsmAsmFastJoin'
_p='alaPimsmV6BidirFastJoin'
_o='alaPimsmBidirFastJoin'
_n='alaPimsmV6BidirSsmCompat'
_m='alaPimsmBidirSsmCompat'
_l='alaPimsmRPHashStatus'
_k='alaPimsmV6BidirStatus'
_j='alaPimsmNonBidirHelloMsgsRcvd'
_i='alaPimsmNonBidirHelloPeriod'
_h='alaPimsmBidirDFAbort'
_g='alaPimsmBidirPeriodicInterval'
_f='alaPimsmBidirStatus'
_e='alaPimsmV6RPSwitchover'
_d='alaPimsmV6SPTConfig'
_c='alaPimsmV6AdminStatus'
_b='alaPimsmRPThreshold'
_a='alaPimsmAdminSPTConfig'
_Z='alaPimsmOldRegisterMessageSupport'
_Y='alaPimsmProbeTime'
_X='alaPimsmMaxRPs'
_W='alaPimsmAdminStatus'
_V='alaPimInterfaceAugEntry'
_U='alaPimdmDenseGroupGrpPrefixLength'
_T='alaPimdmDenseGroupGrpAddress'
_S='alaPimdmDenseGroupAddressType'
_R='TruthValue'
_Q='TimeTicks'
_P='InetAddressPrefixLength'
_O='alaPimConfigMIBGroup'
_N='alaPimsmNonBidirHelloOrigin'
_M='alaPimsmNonBidirHelloAddressType'
_L='read-create'
_K='not-accessible'
_J='seconds'
_I='Unsigned32'
_H='InetAddress'
_G='read-only'
_F='disable'
_E='enable'
_D='read-write'
_C='Integer32'
_B='ALCATEL-ENT1-PIM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
routingIND1Pim,=mibBuilder.importSymbols('ALCATEL-ENT1-BASE','routingIND1Pim')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_H,_P,'InetAddressType')
pimInterfaceEntry,=mibBuilder.importSymbols('PIM-STD-MIB','pimInterfaceEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_Q,_I,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_R)
alcatelIND1PIMMIB=ModuleIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,6,1))
if mibBuilder.loadTexts:alcatelIND1PIMMIB.setRevisions(('2007-04-03 00:00','2015-05-28 00:00'))
_AlaPimNotifications_ObjectIdentity=ObjectIdentity
alaPimNotifications=_AlaPimNotifications_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,0))
_AlcatelIND1PIMMIBObjects_ObjectIdentity=ObjectIdentity
alcatelIND1PIMMIBObjects=_AlcatelIND1PIMMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1))
_AlaPimsmGlobalConfig_ObjectIdentity=ObjectIdentity
alaPimsmGlobalConfig=_AlaPimsmGlobalConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1))
class _AlaPimsmAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimsmAdminStatus_Type.__name__=_C
_AlaPimsmAdminStatus_Object=MibScalar
alaPimsmAdminStatus=_AlaPimsmAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,1),_AlaPimsmAdminStatus_Type())
alaPimsmAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmAdminStatus.setStatus(_A)
class _AlaPimsmMaxRPs_Type(Integer32):defaultValue=32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_AlaPimsmMaxRPs_Type.__name__=_C
_AlaPimsmMaxRPs_Object=MibScalar
alaPimsmMaxRPs=_AlaPimsmMaxRPs_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,2),_AlaPimsmMaxRPs_Type())
alaPimsmMaxRPs.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmMaxRPs.setStatus(_A)
class _AlaPimsmProbeTime_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_AlaPimsmProbeTime_Type.__name__=_C
_AlaPimsmProbeTime_Object=MibScalar
alaPimsmProbeTime=_AlaPimsmProbeTime_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,3),_AlaPimsmProbeTime_Type())
alaPimsmProbeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmProbeTime.setStatus(_A)
if mibBuilder.loadTexts:alaPimsmProbeTime.setUnits(_J)
class _AlaPimsmOldRegisterMessageSupport_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('header',1),('full',2)))
_AlaPimsmOldRegisterMessageSupport_Type.__name__=_C
_AlaPimsmOldRegisterMessageSupport_Object=MibScalar
alaPimsmOldRegisterMessageSupport=_AlaPimsmOldRegisterMessageSupport_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,4),_AlaPimsmOldRegisterMessageSupport_Type())
alaPimsmOldRegisterMessageSupport.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmOldRegisterMessageSupport.setStatus(_A)
class _AlaPimsmAdminSPTConfig_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimsmAdminSPTConfig_Type.__name__=_C
_AlaPimsmAdminSPTConfig_Object=MibScalar
alaPimsmAdminSPTConfig=_AlaPimsmAdminSPTConfig_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,5),_AlaPimsmAdminSPTConfig_Type())
alaPimsmAdminSPTConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmAdminSPTConfig.setStatus(_A)
class _AlaPimsmRPThreshold_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AlaPimsmRPThreshold_Type.__name__=_C
_AlaPimsmRPThreshold_Object=MibScalar
alaPimsmRPThreshold=_AlaPimsmRPThreshold_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,6),_AlaPimsmRPThreshold_Type())
alaPimsmRPThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmRPThreshold.setStatus(_A)
class _AlaPimsmV6AdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimsmV6AdminStatus_Type.__name__=_C
_AlaPimsmV6AdminStatus_Object=MibScalar
alaPimsmV6AdminStatus=_AlaPimsmV6AdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,7),_AlaPimsmV6AdminStatus_Type())
alaPimsmV6AdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmV6AdminStatus.setStatus(_A)
class _AlaPimsmV6SPTConfig_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimsmV6SPTConfig_Type.__name__=_C
_AlaPimsmV6SPTConfig_Object=MibScalar
alaPimsmV6SPTConfig=_AlaPimsmV6SPTConfig_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,8),_AlaPimsmV6SPTConfig_Type())
alaPimsmV6SPTConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmV6SPTConfig.setStatus(_A)
class _AlaPimsmV6RPSwitchover_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimsmV6RPSwitchover_Type.__name__=_C
_AlaPimsmV6RPSwitchover_Object=MibScalar
alaPimsmV6RPSwitchover=_AlaPimsmV6RPSwitchover_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,9),_AlaPimsmV6RPSwitchover_Type())
alaPimsmV6RPSwitchover.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmV6RPSwitchover.setStatus(_A)
class _AlaPimsmBidirStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimsmBidirStatus_Type.__name__=_C
_AlaPimsmBidirStatus_Object=MibScalar
alaPimsmBidirStatus=_AlaPimsmBidirStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,10),_AlaPimsmBidirStatus_Type())
alaPimsmBidirStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmBidirStatus.setStatus(_A)
class _AlaPimsmBidirPeriodicInterval_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_AlaPimsmBidirPeriodicInterval_Type.__name__=_C
_AlaPimsmBidirPeriodicInterval_Object=MibScalar
alaPimsmBidirPeriodicInterval=_AlaPimsmBidirPeriodicInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,11),_AlaPimsmBidirPeriodicInterval_Type())
alaPimsmBidirPeriodicInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmBidirPeriodicInterval.setStatus(_A)
if mibBuilder.loadTexts:alaPimsmBidirPeriodicInterval.setUnits(_J)
class _AlaPimsmBidirDFAbort_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimsmBidirDFAbort_Type.__name__=_C
_AlaPimsmBidirDFAbort_Object=MibScalar
alaPimsmBidirDFAbort=_AlaPimsmBidirDFAbort_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,12),_AlaPimsmBidirDFAbort_Type())
alaPimsmBidirDFAbort.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmBidirDFAbort.setStatus(_A)
class _AlaPimsmNonBidirHelloPeriod_Type(Unsigned32):defaultValue=65535;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,65535))
_AlaPimsmNonBidirHelloPeriod_Type.__name__=_I
_AlaPimsmNonBidirHelloPeriod_Object=MibScalar
alaPimsmNonBidirHelloPeriod=_AlaPimsmNonBidirHelloPeriod_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,13),_AlaPimsmNonBidirHelloPeriod_Type())
alaPimsmNonBidirHelloPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmNonBidirHelloPeriod.setStatus(_A)
if mibBuilder.loadTexts:alaPimsmNonBidirHelloPeriod.setUnits(_J)
_AlaPimsmNonBidirHelloMsgsRcvd_Type=Counter32
_AlaPimsmNonBidirHelloMsgsRcvd_Object=MibScalar
alaPimsmNonBidirHelloMsgsRcvd=_AlaPimsmNonBidirHelloMsgsRcvd_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,14),_AlaPimsmNonBidirHelloMsgsRcvd_Type())
alaPimsmNonBidirHelloMsgsRcvd.setMaxAccess(_G)
if mibBuilder.loadTexts:alaPimsmNonBidirHelloMsgsRcvd.setStatus(_A)
_AlaPimsmNonBidirHelloAddressType_Type=InetAddressType
_AlaPimsmNonBidirHelloAddressType_Object=MibScalar
alaPimsmNonBidirHelloAddressType=_AlaPimsmNonBidirHelloAddressType_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,15),_AlaPimsmNonBidirHelloAddressType_Type())
alaPimsmNonBidirHelloAddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:alaPimsmNonBidirHelloAddressType.setStatus(_A)
class _AlaPimsmNonBidirHelloOrigin_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(8,8),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_AlaPimsmNonBidirHelloOrigin_Type.__name__=_H
_AlaPimsmNonBidirHelloOrigin_Object=MibScalar
alaPimsmNonBidirHelloOrigin=_AlaPimsmNonBidirHelloOrigin_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,16),_AlaPimsmNonBidirHelloOrigin_Type())
alaPimsmNonBidirHelloOrigin.setMaxAccess(_G)
if mibBuilder.loadTexts:alaPimsmNonBidirHelloOrigin.setStatus(_A)
class _AlaPimsmV6BidirStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimsmV6BidirStatus_Type.__name__=_C
_AlaPimsmV6BidirStatus_Object=MibScalar
alaPimsmV6BidirStatus=_AlaPimsmV6BidirStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,17),_AlaPimsmV6BidirStatus_Type())
alaPimsmV6BidirStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmV6BidirStatus.setStatus(_A)
class _AlaPimsmRPHashStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimsmRPHashStatus_Type.__name__=_C
_AlaPimsmRPHashStatus_Object=MibScalar
alaPimsmRPHashStatus=_AlaPimsmRPHashStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,18),_AlaPimsmRPHashStatus_Type())
alaPimsmRPHashStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmRPHashStatus.setStatus(_A)
class _AlaPimsmBidirSsmCompat_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimsmBidirSsmCompat_Type.__name__=_C
_AlaPimsmBidirSsmCompat_Object=MibScalar
alaPimsmBidirSsmCompat=_AlaPimsmBidirSsmCompat_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,19),_AlaPimsmBidirSsmCompat_Type())
alaPimsmBidirSsmCompat.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmBidirSsmCompat.setStatus(_A)
class _AlaPimsmV6BidirSsmCompat_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimsmV6BidirSsmCompat_Type.__name__=_C
_AlaPimsmV6BidirSsmCompat_Object=MibScalar
alaPimsmV6BidirSsmCompat=_AlaPimsmV6BidirSsmCompat_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,20),_AlaPimsmV6BidirSsmCompat_Type())
alaPimsmV6BidirSsmCompat.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmV6BidirSsmCompat.setStatus(_A)
class _AlaPimsmBidirFastJoin_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimsmBidirFastJoin_Type.__name__=_C
_AlaPimsmBidirFastJoin_Object=MibScalar
alaPimsmBidirFastJoin=_AlaPimsmBidirFastJoin_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,21),_AlaPimsmBidirFastJoin_Type())
alaPimsmBidirFastJoin.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmBidirFastJoin.setStatus(_A)
class _AlaPimsmV6BidirFastJoin_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimsmV6BidirFastJoin_Type.__name__=_C
_AlaPimsmV6BidirFastJoin_Object=MibScalar
alaPimsmV6BidirFastJoin=_AlaPimsmV6BidirFastJoin_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,22),_AlaPimsmV6BidirFastJoin_Type())
alaPimsmV6BidirFastJoin.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmV6BidirFastJoin.setStatus(_A)
class _AlaPimsmAsmFastJoin_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimsmAsmFastJoin_Type.__name__=_C
_AlaPimsmAsmFastJoin_Object=MibScalar
alaPimsmAsmFastJoin=_AlaPimsmAsmFastJoin_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,23),_AlaPimsmAsmFastJoin_Type())
alaPimsmAsmFastJoin.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmAsmFastJoin.setStatus(_A)
class _AlaPimsmV6AsmFastJoin_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimsmV6AsmFastJoin_Type.__name__=_C
_AlaPimsmV6AsmFastJoin_Object=MibScalar
alaPimsmV6AsmFastJoin=_AlaPimsmV6AsmFastJoin_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,24),_AlaPimsmV6AsmFastJoin_Type())
alaPimsmV6AsmFastJoin.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmV6AsmFastJoin.setStatus(_A)
class _AlaPimsmSsmFastJoin_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimsmSsmFastJoin_Type.__name__=_C
_AlaPimsmSsmFastJoin_Object=MibScalar
alaPimsmSsmFastJoin=_AlaPimsmSsmFastJoin_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,25),_AlaPimsmSsmFastJoin_Type())
alaPimsmSsmFastJoin.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmSsmFastJoin.setStatus(_A)
class _AlaPimsmV6SsmFastJoin_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimsmV6SsmFastJoin_Type.__name__=_C
_AlaPimsmV6SsmFastJoin_Object=MibScalar
alaPimsmV6SsmFastJoin=_AlaPimsmV6SsmFastJoin_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,1,26),_AlaPimsmV6SsmFastJoin_Type())
alaPimsmV6SsmFastJoin.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimsmV6SsmFastJoin.setStatus(_A)
_AlaPimdmGlobalConfig_ObjectIdentity=ObjectIdentity
alaPimdmGlobalConfig=_AlaPimdmGlobalConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,2))
class _AlaPimdmAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimdmAdminStatus_Type.__name__=_C
_AlaPimdmAdminStatus_Object=MibScalar
alaPimdmAdminStatus=_AlaPimdmAdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,2,1),_AlaPimdmAdminStatus_Type())
alaPimdmAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimdmAdminStatus.setStatus(_A)
class _AlaPimdmStateRefreshTimeToLive_Type(Integer32):defaultValue=16
_AlaPimdmStateRefreshTimeToLive_Type.__name__=_C
_AlaPimdmStateRefreshTimeToLive_Object=MibScalar
alaPimdmStateRefreshTimeToLive=_AlaPimdmStateRefreshTimeToLive_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,2,2),_AlaPimdmStateRefreshTimeToLive_Type())
alaPimdmStateRefreshTimeToLive.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimdmStateRefreshTimeToLive.setStatus(_A)
class _AlaPimdmStateRefreshLimitInterval_Type(TimeTicks):defaultValue=0
_AlaPimdmStateRefreshLimitInterval_Type.__name__=_Q
_AlaPimdmStateRefreshLimitInterval_Object=MibScalar
alaPimdmStateRefreshLimitInterval=_AlaPimdmStateRefreshLimitInterval_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,2,3),_AlaPimdmStateRefreshLimitInterval_Type())
alaPimdmStateRefreshLimitInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimdmStateRefreshLimitInterval.setStatus(_A)
class _AlaPimdmV6AdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimdmV6AdminStatus_Type.__name__=_C
_AlaPimdmV6AdminStatus_Object=MibScalar
alaPimdmV6AdminStatus=_AlaPimdmV6AdminStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,2,4),_AlaPimdmV6AdminStatus_Type())
alaPimdmV6AdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimdmV6AdminStatus.setStatus(_A)
_AlaPimdmDenseGroupTable_Object=MibTable
alaPimdmDenseGroupTable=_AlaPimdmDenseGroupTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,2,5))
if mibBuilder.loadTexts:alaPimdmDenseGroupTable.setStatus(_A)
_AlaPimdmDenseGroupEntry_Object=MibTableRow
alaPimdmDenseGroupEntry=_AlaPimdmDenseGroupEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,2,5,1))
alaPimdmDenseGroupEntry.setIndexNames((0,_B,_S),(0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:alaPimdmDenseGroupEntry.setStatus(_A)
_AlaPimdmDenseGroupAddressType_Type=InetAddressType
_AlaPimdmDenseGroupAddressType_Object=MibTableColumn
alaPimdmDenseGroupAddressType=_AlaPimdmDenseGroupAddressType_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,2,5,1,1),_AlaPimdmDenseGroupAddressType_Type())
alaPimdmDenseGroupAddressType.setMaxAccess(_K)
if mibBuilder.loadTexts:alaPimdmDenseGroupAddressType.setStatus(_A)
class _AlaPimdmDenseGroupGrpAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(8,8),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_AlaPimdmDenseGroupGrpAddress_Type.__name__=_H
_AlaPimdmDenseGroupGrpAddress_Object=MibTableColumn
alaPimdmDenseGroupGrpAddress=_AlaPimdmDenseGroupGrpAddress_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,2,5,1,2),_AlaPimdmDenseGroupGrpAddress_Type())
alaPimdmDenseGroupGrpAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:alaPimdmDenseGroupGrpAddress.setStatus(_A)
class _AlaPimdmDenseGroupGrpPrefixLength_Type(InetAddressPrefixLength):subtypeSpec=InetAddressPrefixLength.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,128))
_AlaPimdmDenseGroupGrpPrefixLength_Type.__name__=_P
_AlaPimdmDenseGroupGrpPrefixLength_Object=MibTableColumn
alaPimdmDenseGroupGrpPrefixLength=_AlaPimdmDenseGroupGrpPrefixLength_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,2,5,1,3),_AlaPimdmDenseGroupGrpPrefixLength_Type())
alaPimdmDenseGroupGrpPrefixLength.setMaxAccess(_K)
if mibBuilder.loadTexts:alaPimdmDenseGroupGrpPrefixLength.setStatus(_A)
class _AlaPimdmDenseGroupOverrideDynamic_Type(TruthValue):defaultValue=2
_AlaPimdmDenseGroupOverrideDynamic_Type.__name__=_R
_AlaPimdmDenseGroupOverrideDynamic_Object=MibTableColumn
alaPimdmDenseGroupOverrideDynamic=_AlaPimdmDenseGroupOverrideDynamic_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,2,5,1,4),_AlaPimdmDenseGroupOverrideDynamic_Type())
alaPimdmDenseGroupOverrideDynamic.setMaxAccess(_L)
if mibBuilder.loadTexts:alaPimdmDenseGroupOverrideDynamic.setStatus(_A)
class _AlaPimdmDenseGroupPrecedence_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AlaPimdmDenseGroupPrecedence_Type.__name__=_I
_AlaPimdmDenseGroupPrecedence_Object=MibTableColumn
alaPimdmDenseGroupPrecedence=_AlaPimdmDenseGroupPrecedence_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,2,5,1,5),_AlaPimdmDenseGroupPrecedence_Type())
alaPimdmDenseGroupPrecedence.setMaxAccess(_L)
if mibBuilder.loadTexts:alaPimdmDenseGroupPrecedence.setStatus(_A)
_AlaPimdmDenseGroupRowStatus_Type=RowStatus
_AlaPimdmDenseGroupRowStatus_Object=MibTableColumn
alaPimdmDenseGroupRowStatus=_AlaPimdmDenseGroupRowStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,2,5,1,6),_AlaPimdmDenseGroupRowStatus_Type())
alaPimdmDenseGroupRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:alaPimdmDenseGroupRowStatus.setStatus(_A)
_AlaPimGlobalConfig_ObjectIdentity=ObjectIdentity
alaPimGlobalConfig=_AlaPimGlobalConfig_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,3))
class _AlaPimBfdStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimBfdStatus_Type.__name__=_C
_AlaPimBfdStatus_Object=MibScalar
alaPimBfdStatus=_AlaPimBfdStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,3,1),_AlaPimBfdStatus_Type())
alaPimBfdStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimBfdStatus.setStatus(_A)
class _AlaPimBfdAllInterfaceStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimBfdAllInterfaceStatus_Type.__name__=_C
_AlaPimBfdAllInterfaceStatus_Object=MibScalar
alaPimBfdAllInterfaceStatus=_AlaPimBfdAllInterfaceStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,3,2),_AlaPimBfdAllInterfaceStatus_Type())
alaPimBfdAllInterfaceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimBfdAllInterfaceStatus.setStatus(_A)
class _AlaPimMoFRRStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimMoFRRStatus_Type.__name__=_C
_AlaPimMoFRRStatus_Object=MibScalar
alaPimMoFRRStatus=_AlaPimMoFRRStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,3,3),_AlaPimMoFRRStatus_Type())
alaPimMoFRRStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimMoFRRStatus.setStatus(_A)
class _AlaPimMoFRRAllRouteStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimMoFRRAllRouteStatus_Type.__name__=_C
_AlaPimMoFRRAllRouteStatus_Object=MibScalar
alaPimMoFRRAllRouteStatus=_AlaPimMoFRRAllRouteStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,3,4),_AlaPimMoFRRAllRouteStatus_Type())
alaPimMoFRRAllRouteStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimMoFRRAllRouteStatus.setStatus(_A)
_AlaPimInterfaceAugTable_Object=MibTable
alaPimInterfaceAugTable=_AlaPimInterfaceAugTable_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,3,5))
if mibBuilder.loadTexts:alaPimInterfaceAugTable.setStatus(_A)
_AlaPimInterfaceAugEntry_Object=MibTableRow
alaPimInterfaceAugEntry=_AlaPimInterfaceAugEntry_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,3,5,1))
if mibBuilder.loadTexts:alaPimInterfaceAugEntry.setStatus(_A)
class _AlaPimInterfaceBfdStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimInterfaceBfdStatus_Type.__name__=_C
_AlaPimInterfaceBfdStatus_Object=MibTableColumn
alaPimInterfaceBfdStatus=_AlaPimInterfaceBfdStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,3,5,1,1),_AlaPimInterfaceBfdStatus_Type())
alaPimInterfaceBfdStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimInterfaceBfdStatus.setStatus(_A)
class _AlaPimMbrAllSourcesStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimMbrAllSourcesStatus_Type.__name__=_C
_AlaPimMbrAllSourcesStatus_Object=MibScalar
alaPimMbrAllSourcesStatus=_AlaPimMbrAllSourcesStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,3,6),_AlaPimMbrAllSourcesStatus_Type())
alaPimMbrAllSourcesStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimMbrAllSourcesStatus.setStatus(_A)
class _AlaPimMbrOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimMbrOperStatus_Type.__name__=_C
_AlaPimMbrOperStatus_Object=MibScalar
alaPimMbrOperStatus=_AlaPimMbrOperStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,3,7),_AlaPimMbrOperStatus_Type())
alaPimMbrOperStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:alaPimMbrOperStatus.setStatus(_A)
class _AlaPimV6BfdStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimV6BfdStatus_Type.__name__=_C
_AlaPimV6BfdStatus_Object=MibScalar
alaPimV6BfdStatus=_AlaPimV6BfdStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,3,8),_AlaPimV6BfdStatus_Type())
alaPimV6BfdStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimV6BfdStatus.setStatus(_A)
class _AlaPimV6BfdAllInterfaceStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPimV6BfdAllInterfaceStatus_Type.__name__=_C
_AlaPimV6BfdAllInterfaceStatus_Object=MibScalar
alaPimV6BfdAllInterfaceStatus=_AlaPimV6BfdAllInterfaceStatus_Object((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,1,3,9),_AlaPimV6BfdAllInterfaceStatus_Type())
alaPimV6BfdAllInterfaceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPimV6BfdAllInterfaceStatus.setStatus(_A)
_AlcatelIND1PIMMIBConformance_ObjectIdentity=ObjectIdentity
alcatelIND1PIMMIBConformance=_AlcatelIND1PIMMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,2))
_AlcatelIND1PIMMIBCompliances_ObjectIdentity=ObjectIdentity
alcatelIND1PIMMIBCompliances=_AlcatelIND1PIMMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,2,1))
_AlcatelIND1PIMMIBGroups_ObjectIdentity=ObjectIdentity
alcatelIND1PIMMIBGroups=_AlcatelIND1PIMMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,2,2))
pimInterfaceEntry.registerAugmentions((_B,_V))
alaPimInterfaceAugEntry.setIndexNames(*pimInterfaceEntry.getIndexNames())
alaPimsmConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,2,2,1))
alaPimsmConfigMIBGroup.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t)))
if mibBuilder.loadTexts:alaPimsmConfigMIBGroup.setStatus(_A)
alaPimdmConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,2,2,2))
alaPimdmConfigMIBGroup.setObjects(*((_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:alaPimdmConfigMIBGroup.setStatus(_A)
alaPimConfigMIBGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,2,2,3))
alaPimConfigMIBGroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:alaPimConfigMIBGroup.setStatus(_A)
alaPimOptionalGroup=ObjectGroup((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,2,2,4))
alaPimOptionalGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:alaPimOptionalGroup.setStatus(_A)
alaPimNonBidirHello=NotificationType((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,0,1))
alaPimNonBidirHello.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:alaPimNonBidirHello.setStatus(_A)
alaPimNotificationGroup=NotificationGroup((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,2,2,5))
alaPimNotificationGroup.setObjects((_B,_AA))
if mibBuilder.loadTexts:alaPimNotificationGroup.setStatus(_A)
alaPimsmCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,2,1,1))
alaPimsmCompliance.setObjects(*((_B,_AB),(_B,_O)))
if mibBuilder.loadTexts:alaPimsmCompliance.setStatus(_A)
alaPimdmCompliance=ModuleCompliance((1,3,6,1,4,1,6486,801,1,2,1,10,6,1,2,1,2))
alaPimdmCompliance.setObjects(*((_B,_AC),(_B,_O)))
if mibBuilder.loadTexts:alaPimdmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1PIMMIB':alcatelIND1PIMMIB,'alaPimNotifications':alaPimNotifications,_AA:alaPimNonBidirHello,'alcatelIND1PIMMIBObjects':alcatelIND1PIMMIBObjects,'alaPimsmGlobalConfig':alaPimsmGlobalConfig,_W:alaPimsmAdminStatus,_X:alaPimsmMaxRPs,_Y:alaPimsmProbeTime,_Z:alaPimsmOldRegisterMessageSupport,_a:alaPimsmAdminSPTConfig,_b:alaPimsmRPThreshold,_c:alaPimsmV6AdminStatus,_d:alaPimsmV6SPTConfig,_e:alaPimsmV6RPSwitchover,_f:alaPimsmBidirStatus,_g:alaPimsmBidirPeriodicInterval,_h:alaPimsmBidirDFAbort,_i:alaPimsmNonBidirHelloPeriod,_j:alaPimsmNonBidirHelloMsgsRcvd,_M:alaPimsmNonBidirHelloAddressType,_N:alaPimsmNonBidirHelloOrigin,_k:alaPimsmV6BidirStatus,_l:alaPimsmRPHashStatus,_m:alaPimsmBidirSsmCompat,_n:alaPimsmV6BidirSsmCompat,_o:alaPimsmBidirFastJoin,_p:alaPimsmV6BidirFastJoin,_q:alaPimsmAsmFastJoin,_r:alaPimsmV6AsmFastJoin,_s:alaPimsmSsmFastJoin,_t:alaPimsmV6SsmFastJoin,'alaPimdmGlobalConfig':alaPimdmGlobalConfig,_u:alaPimdmAdminStatus,_v:alaPimdmStateRefreshTimeToLive,_w:alaPimdmStateRefreshLimitInterval,_x:alaPimdmV6AdminStatus,'alaPimdmDenseGroupTable':alaPimdmDenseGroupTable,'alaPimdmDenseGroupEntry':alaPimdmDenseGroupEntry,_S:alaPimdmDenseGroupAddressType,_T:alaPimdmDenseGroupGrpAddress,_U:alaPimdmDenseGroupGrpPrefixLength,_y:alaPimdmDenseGroupOverrideDynamic,_z:alaPimdmDenseGroupPrecedence,_A0:alaPimdmDenseGroupRowStatus,'alaPimGlobalConfig':alaPimGlobalConfig,_A1:alaPimBfdStatus,_A2:alaPimBfdAllInterfaceStatus,_A3:alaPimMoFRRStatus,_A4:alaPimMoFRRAllRouteStatus,'alaPimInterfaceAugTable':alaPimInterfaceAugTable,_V:alaPimInterfaceAugEntry,_A5:alaPimInterfaceBfdStatus,_A6:alaPimMbrAllSourcesStatus,_A7:alaPimMbrOperStatus,_A8:alaPimV6BfdStatus,_A9:alaPimV6BfdAllInterfaceStatus,'alcatelIND1PIMMIBConformance':alcatelIND1PIMMIBConformance,'alcatelIND1PIMMIBCompliances':alcatelIND1PIMMIBCompliances,'alaPimsmCompliance':alaPimsmCompliance,'alaPimdmCompliance':alaPimdmCompliance,'alcatelIND1PIMMIBGroups':alcatelIND1PIMMIBGroups,_AB:alaPimsmConfigMIBGroup,_AC:alaPimdmConfigMIBGroup,_O:alaPimConfigMIBGroup,'alaPimOptionalGroup':alaPimOptionalGroup,'alaPimNotificationGroup':alaPimNotificationGroup})